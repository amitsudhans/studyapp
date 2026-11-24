<?php

namespace Tests\Feature;

use App\Models\Answer;
use App\Models\Exam;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Student;
use App\Models\StudentExamDetail;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;
use Tests\TestCase;

class ImageHotspotQuestionTest extends TestCase
{
    use DatabaseTransactions;

    protected User $teacher;

    protected Standard $standard;

    protected function setUp(): void
    {
        parent::setUp();

        $syllabus = Syllabus::firstOrCreate(['name' => 'State Board']);
        $this->standard = Standard::firstOrCreate(['name' => 'Class 9 Biology', 'syllabus_id' => $syllabus->id]);

        $this->teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $this->teacher->id,
            'type' => 1, // Teacher
        ]);
    }

    public function test_teacher_can_create_image_hotspot_question_with_diagram_and_pins(): void
    {
        Storage::fake('public');

        $diagramFile = UploadedFile::fake()->image('flower_parts.png', 600, 400);

        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Identify the labeled parts of the flower diagram below.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_IMAGE_LABELING,
            'marks' => 3,
            'image_file' => $diagramFile,
            'answers' => [
                [
                    'name' => 'Petal',
                    'options' => 'Petal, Sepal, Stamen, Carpel',
                    'x' => 25.5,
                    'y' => 30.2,
                ],
                [
                    'name' => 'Anther',
                    'options' => ['Anther', 'Filament', 'Style', 'Ovary'],
                    'x' => 60.0,
                    'y' => 20.0,
                ],
                [
                    'name' => 'Sepal',
                    'options' => 'Sepal, Petal, Receptacle, Pedicel',
                    'x' => 45.0,
                    'y' => 85.0,
                ],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('name', 'like', '%flower diagram%')->first();
        $this->assertNotNull($question);
        $this->assertTrue($question->isImageLabeling());
        $this->assertEquals(Question::TYPE_IMAGE_LABELING, $question->type);
        $this->assertEquals('Image Hotspot', $question->type_name);
        $this->assertNotNull($question->image);
        Storage::disk('public')->assertExists($question->image);

        $this->assertCount(3, $question->answers);

        $answers = $question->answers()->orderBy('id')->get();
        $this->assertEquals('Petal', $answers[0]->name);
        $coords0 = $answers[0]->getHotspotCoordinates();
        $this->assertEquals(25.5, $coords0['x']);
        $this->assertEquals(30.2, $coords0['y']);
        $this->assertEquals(['Petal', 'Sepal', 'Stamen', 'Carpel'], $answers[0]->getBlankOptions());

        $this->assertEquals('Anther', $answers[1]->name);
        $coords1 = $answers[1]->getHotspotCoordinates();
        $this->assertEquals(60.0, $coords1['x']);
        $this->assertEquals(20.0, $coords1['y']);
        $this->assertEquals(['Anther', 'Filament', 'Style', 'Ovary'], $answers[1]->getBlankOptions());
    }

    public function test_image_hotspot_requires_mandatory_options_for_each_pin(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Diagram without options',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_IMAGE_LABELING,
            'marks' => 1,
            'answers' => [
                ['name' => 'Stigma', 'options' => ''],
            ],
        ]);

        $response->assertSessionHasErrors(['answers']);
    }

    public function test_student_can_answer_image_hotspots_and_receive_auto_graded_marks(): void
    {
        $studentUser = User::factory()->create();
        UserProfile::create([
            'user_id' => $studentUser->id,
            'type' => 2,
            'standard_id' => $this->standard->id,
        ]);
        $student = Student::create([
            'id' => $studentUser->id,
            'name' => $studentUser->name,
            'standard_id' => $this->standard->id,
        ]);

        $question = Question::create([
            'name' => 'Parts of the Human Heart Diagram',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_IMAGE_LABELING,
            'marks' => 3,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $p1 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Aorta',
            'match_answer' => json_encode(['x' => 50, 'y' => 15, 'options' => ['Aorta', 'Vena Cava', 'Pulmonary Artery']]),
            'is_correct' => 1,
            'status' => 1,
        ]);
        $p2 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Left Ventricle',
            'match_answer' => json_encode(['x' => 70, 'y' => 60, 'options' => ['Left Ventricle', 'Right Ventricle', 'Left Atrium']]),
            'is_correct' => 1,
            'status' => 1,
        ]);
        $p3 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Right Atrium',
            'match_answer' => json_encode(['x' => 30, 'y' => 40, 'options' => ['Right Atrium', 'Left Atrium', 'Septum']]),
            'is_correct' => 1,
            'status' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Anatomy Diagram Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 3,
        ]);
        $exam->standards()->attach($this->standard->id);
        $exam->questions()->attach($question->id);

        // Student submits 2 out of 3 correct
        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $p1->id => 'Aorta', // Correct (1)
                $p2->id => 'Left Ventricle', // Correct (2)
                $p3->id => 'Wrong Choice', // Incorrect (0)
            ],
        ]);

        $detail->load('question.answers');

        $this->assertTrue($detail->isImageLabeling());
        $this->assertEquals(2, $detail->getCorrectHotspotsCount());
        $this->assertEquals(2, $detail->getEarnedMarks());
        $this->assertEquals(3, $detail->getQuestionMarks());
        $this->assertFalse($detail->isCorrect());
        $this->assertTrue($detail->isPartiallyCorrect());

        $review = $detail->getHotspotsReview();
        $this->assertCount(3, $review);
        $this->assertTrue($review[0]['is_correct']);
        $this->assertEquals('Aorta', $review[0]['student_answer']);
        $this->assertTrue($review[1]['is_correct']);
        $this->assertEquals('Left Ventricle', $review[1]['student_answer']);
        $this->assertFalse($review[2]['is_correct']);
        $this->assertEquals('Wrong Choice', $review[2]['student_answer']);
        $this->assertEquals('Right Atrium', $review[2]['correct_answer']);
    }

    public function test_teacher_can_create_image_hotspot_question_with_up_to_10_pins(): void
    {
        Storage::fake('public');

        $diagramFile = UploadedFile::fake()->image('human_skeleton.png', 800, 600);

        $answersPayload = [];
        for ($i = 1; $i <= 10; $i++) {
            $answersPayload[] = [
                'name' => "Bone {$i}",
                'options' => "Bone {$i}, Option A, Option B, Option C",
                'x' => $i * 9.5,
                'y' => $i * 9.0,
            ];
        }

        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Identify all 10 labeled bones on the skeleton diagram.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_IMAGE_LABELING,
            'marks' => 10,
            'image_file' => $diagramFile,
            'answers' => $answersPayload,
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('name', 'like', '%10 labeled bones%')->first();
        $this->assertNotNull($question);
        $this->assertCount(10, $question->answers);
        $this->assertEquals(10, $question->marks);

        $firstAnswer = $question->answers()->orderBy('id')->first();
        $this->assertEquals('Bone 1', $firstAnswer->name);
        $coordsFirst = $firstAnswer->getHotspotCoordinates();
        $this->assertEquals(9.5, $coordsFirst['x']);
        $this->assertEquals(9.0, $coordsFirst['y']);

        $lastAnswer = $question->answers()->orderBy('id', 'desc')->first();
        $this->assertEquals('Bone 10', $lastAnswer->name);
        $coordsLast = $lastAnswer->getHotspotCoordinates();
        $this->assertEquals(95.0, $coordsLast['x']);
        $this->assertEquals(90.0, $coordsLast['y']);
    }
}

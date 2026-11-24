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

class CaseBasedQuestionTest extends TestCase
{
    use DatabaseTransactions;

    protected User $teacher;

    protected Standard $standard;

    protected function setUp(): void
    {
        parent::setUp();

        $syllabus = Syllabus::firstOrCreate(['name' => 'CBSE Board']);
        $this->standard = Standard::firstOrCreate(['name' => 'Class 10 Science', 'syllabus_id' => $syllabus->id]);

        $this->teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $this->teacher->id,
            'type' => 1, // Teacher
        ]);
    }

    public function test_teacher_can_create_case_based_question_with_passage_and_sub_questions(): void
    {
        Storage::fake('public');

        $sourceImage = UploadedFile::fake()->image('photosynthesis_experiment.png', 800, 500);

        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => '<p><strong>Read the following case study carefully:</strong></p><p>A student sets up an experiment to study the rate of photosynthesis in Hydrilla plants under different light intensities...</p>',
            'description' => 'CBSE Class 10 Board Section E Case Study question on Photosynthesis and Light Intensity.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_CASE_STUDY,
            'marks' => 3,
            'image_file' => $sourceImage,
            'answers' => [
                [
                    'prompt' => 'Which gas is evolved in the form of bubbles during the experiment?',
                    'name' => 'Oxygen',
                    'options' => 'Oxygen, Carbon Dioxide, Nitrogen, Hydrogen',
                ],
                [
                    'prompt' => 'What is the role of sodium bicarbonate added to the water in this setup?',
                    'name' => 'Provides dissolved CO2',
                    'options' => ['Provides dissolved CO2', 'Maintains pH 7', 'Absorbs excess light', 'Supplies mineral ions'],
                ],
                [
                    'prompt' => 'What happens to the rate of bubbling when the light source is moved further away?',
                    'name' => 'Decreases',
                    'options' => 'Decreases, Increases, Remains constant, Stoppage followed by surge',
                ],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('description', 'like', '%Photosynthesis and Light Intensity%')->first();
        $this->assertNotNull($question);
        $this->assertTrue($question->isCaseStudy());
        $this->assertEquals(9, $question->type);
        $this->assertEquals(3, $question->marks);
        $this->assertEquals(3, $question->answers()->count());

        $firstAnswer = $question->answers->first();
        $this->assertEquals('Oxygen', $firstAnswer->name);
        $this->assertEquals('Which gas is evolved in the form of bubbles during the experiment?', $firstAnswer->getCasePrompt());
        $this->assertEquals(['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'], $firstAnswer->getBlankOptions());
    }

    public function test_case_based_question_requires_at_least_three_sub_questions(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Sample Case Study',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_CASE_STUDY,
            'marks' => 2,
            'answers' => [
                [
                    'prompt' => 'Sub-question 1',
                    'name' => 'Option 1',
                    'options' => 'Option 1, Option 2',
                ],
                [
                    'prompt' => 'Sub-question 2',
                    'name' => 'Option A',
                    'options' => 'Option A, Option B',
                ],
            ],
        ]);

        $response->assertSessionHasErrors('answers');
    }

    public function test_teacher_can_update_case_based_question(): void
    {
        $question = Question::create([
            'name' => 'Initial Passage',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_CASE_STUDY,
            'marks' => 3,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        for ($i = 1; $i <= 3; $i++) {
            Answer::create([
                'question_id' => $question->id,
                'name' => "Ans {$i}",
                'match_answer' => json_encode(['prompt' => "Q{$i}", 'options' => ["Ans {$i}", 'Alt']]),
                'is_correct' => 1,
                'status' => 1,
            ]);
        }

        $response = $this->actingAs($this->teacher)->put(route('questions.update', $question), [
            '_method' => 'PUT',
            'name' => 'Updated Passage',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_CASE_STUDY,
            'marks' => 4,
            'answers' => [
                [
                    'prompt' => 'Updated Sub-Q 1',
                    'name' => 'New Ans 1',
                    'options' => 'New Ans 1, Wrong 1',
                ],
                [
                    'prompt' => 'Updated Sub-Q 2',
                    'name' => 'New Ans 2',
                    'options' => 'New Ans 2, Wrong 2',
                ],
                [
                    'prompt' => 'Updated Sub-Q 3',
                    'name' => 'New Ans 3',
                    'options' => 'New Ans 3, Wrong 3',
                ],
                [
                    'prompt' => 'Updated Sub-Q 4',
                    'name' => 'New Ans 4',
                    'options' => 'New Ans 4, Wrong 4',
                ],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $question->refresh();
        $this->assertEquals('Updated Passage', $question->name);
        $this->assertEquals(4, $question->marks);
        $this->assertEquals(4, $question->answers()->count());
    }

    public function test_student_can_answer_case_based_question_and_auto_gradable_evaluation(): void
    {
        $question = Question::create([
            'name' => 'Passage on Electric Circuits and Ohm\'s Law',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_CASE_STUDY,
            'marks' => 3,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $ans1 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Directly Proportional',
            'match_answer' => json_encode(['prompt' => 'How is current related to voltage?', 'options' => ['Directly Proportional', 'Inversely Proportional', 'Independent']]),
            'is_correct' => 1,
            'status' => 1,
        ]);

        $ans2 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Ohm',
            'match_answer' => json_encode(['prompt' => 'What is the SI unit of resistance?', 'options' => ['Ohm', 'Volt', 'Ampere', 'Watt']]),
            'is_correct' => 1,
            'status' => 1,
        ]);

        $ans3 = Answer::create([
            'question_id' => $question->id,
            'name' => 'Halved',
            'match_answer' => json_encode(['prompt' => 'If resistance is doubled at constant V, current is:', 'options' => ['Halved', 'Doubled', 'Quadrupled', 'Unchanged']]),
            'is_correct' => 1,
            'status' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Physics Mid-Term Exam',
            'standard_id' => $this->standard->id,
            'subject_id' => null,
            'created_by' => $this->teacher->id,
            'total_marks' => 3,
            'passing_marks' => 1,
            'duration' => 30,
            'status' => 1,
        ]);
        $exam->questions()->attach($question->id);

        $student = Student::factory()->create();

        // Case 1: All correct (3 / 3 marks)
        $detailFull = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $ans1->id => 'Directly Proportional',
                $ans2->id => 'Ohm',
                $ans3->id => 'Halved',
            ],
        ]);

        $this->assertEquals(3, $detailFull->getEarnedMarks());
        $this->assertTrue($detailFull->isCorrect());
        $this->assertFalse($detailFull->isPartiallyCorrect());

        // Case 2: Partially correct (2 / 3 marks)
        $detailPartial = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $ans1->id => 'Directly Proportional',
                $ans2->id => 'Volt', // wrong
                $ans3->id => 'Halved',
            ],
        ]);

        $this->assertEquals(2, $detailPartial->getEarnedMarks());
        $this->assertFalse($detailPartial->isCorrect());
        $this->assertTrue($detailPartial->isPartiallyCorrect());

        $review = $detailPartial->getCaseStudyReview();
        $this->assertCount(3, $review);
        $this->assertTrue($review[0]['is_correct']);
        $this->assertFalse($review[1]['is_correct']);
        $this->assertEquals('Volt', $review[1]['student_answer']);
        $this->assertEquals('Ohm', $review[1]['correct_answer']);
        $this->assertTrue($review[2]['is_correct']);
    }
}

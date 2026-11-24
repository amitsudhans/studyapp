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
use Tests\TestCase;

class FillInTheBlanksQuestionTest extends TestCase
{
    use DatabaseTransactions;

    protected User $teacher;

    protected Standard $standard;

    protected function setUp(): void
    {
        parent::setUp();

        $syllabus = Syllabus::firstOrCreate(['name' => 'State Board']);
        $this->standard = Standard::firstOrCreate(['name' => 'Class 8', 'syllabus_id' => $syllabus->id]);

        $this->teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $this->teacher->id,
            'type' => 1, // Teacher
        ]);
    }

    public function test_teacher_can_create_fill_in_the_blanks_question(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'The capital of France is [blank] and the capital of Japan is [blank].',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 2,
            'answers' => [
                ['name' => 'Paris', 'options' => 'Paris, London, Berlin, Madrid'],
                ['name' => 'Tokyo', 'options' => ['Tokyo', 'Kyoto', 'Osaka', 'Seoul']],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('name', 'like', '%capital of France%')->first();
        $this->assertNotNull($question);
        $this->assertTrue($question->isFillInTheBlanks());
        $this->assertEquals(Question::TYPE_FILL_IN_THE_BLANKS, $question->type);
        $this->assertEquals('Fill in the blanks', $question->type_name);
        $this->assertCount(2, $question->answers);

        $answers = $question->answers()->orderBy('id')->get();
        $this->assertEquals(['Paris', 'Tokyo'], $answers->pluck('name')->toArray());
        $this->assertEquals(['Paris', 'London', 'Berlin', 'Madrid'], $answers[0]->getBlankOptions());
        $this->assertEquals(['Tokyo', 'Kyoto', 'Osaka', 'Seoul'], $answers[1]->getBlankOptions());
    }

    public function test_fill_in_the_blanks_requires_mandatory_options_for_each_blank(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Sentence with blank but no options',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 1,
            'answers' => [
                ['name' => 'Oxygen', 'options' => ''],
            ],
        ]);

        $response->assertSessionHasErrors(['answers']);
    }

    public function test_fill_in_the_blanks_caps_options_at_max_four(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Blank with more than 4 options',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 1,
            'answers' => [
                ['name' => 'Apple', 'options' => 'Apple, Banana, Mango, Orange, Grape, Pineapple'],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));

        $question = Question::where('name', 'like', '%Blank with more than 4 options%')->first();
        $this->assertNotNull($question);
        $options = $question->answers->first()->getBlankOptions();
        $this->assertCount(4, $options);
        $this->assertContains('Apple', $options);
    }

    public function test_fill_in_the_blanks_requires_at_least_one_blank(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Sentence without blanks',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 1,
            'answers' => [
                ['name' => ''],
            ],
        ]);

        $response->assertSessionHasErrors(['answers']);
    }

    public function test_student_can_answer_fill_in_the_blanks_and_receive_grades(): void
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
            'name' => 'Water freezes at [blank] degrees Celsius and boils at [blank] degrees Celsius.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 2,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $a1 = Answer::create(['question_id' => $question->id, 'name' => '0', 'is_correct' => 1, 'status' => 1]);
        $a2 = Answer::create(['question_id' => $question->id, 'name' => '100', 'is_correct' => 1, 'status' => 1]);

        $exam = Exam::create([
            'name' => 'Chemistry Blanks Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 2,
        ]);
        $exam->standards()->attach($this->standard->id);
        $exam->questions()->attach($question->id);

        // Case 1: Student gets both right (case-insensitive & trimmed)
        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $a1->id => ' 0 ',
                $a2->id => '100',
            ],
        ]);

        $detail->load('question.answers');

        $this->assertTrue($detail->isFillInTheBlanks());
        $this->assertEquals(2, $detail->getCorrectBlanksCount());
        $this->assertTrue($detail->isCorrect());
        $this->assertFalse($detail->isPartiallyCorrect());
        $this->assertEquals(2, $detail->getEarnedMarks());
        $this->assertStringContainsString('Blank #1: 0', $detail->getSelectedAnswerDisplay());
        $this->assertStringContainsString('Blank #2: 100', $detail->getSelectedAnswerDisplay());

        // Case 2: Partial credit (1 right, 1 wrong)
        $detail2 = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $a1->id => '0',
                $a2->id => '90', // Wrong
            ],
        ]);

        $detail2->load('question.answers');

        $this->assertEquals(1, $detail2->getCorrectBlanksCount());
        $this->assertFalse($detail2->isCorrect());
        $this->assertTrue($detail2->isPartiallyCorrect());
        $this->assertEquals(1, $detail2->getEarnedMarks());

        $review = $detail2->getBlanksReview();
        $this->assertCount(2, $review);
        $this->assertTrue($review[0]['is_correct']);
        $this->assertFalse($review[1]['is_correct']);
        $this->assertEquals('90', $review[1]['student_answer']);
        $this->assertEquals('100', $review[1]['correct_answer']);
    }

    public function test_teacher_cannot_create_question_with_zero_or_negative_marks(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Question with zero marks',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 0,
            'answers' => [
                ['name' => 'Option 1', 'is_correct' => 1],
                ['name' => 'Option 2', 'is_correct' => 0],
            ],
        ]);

        $response->assertSessionHasErrors(['marks']);
    }

    public function test_fill_in_the_blanks_evaluates_exact_count_as_marks_e_g_2_out_of_4_is_2_marks(): void
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
            'name' => 'Four blanks question',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_FILL_IN_THE_BLANKS,
            'marks' => 4,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $b1 = Answer::create(['question_id' => $question->id, 'name' => 'North', 'is_correct' => 1, 'status' => 1]);
        $b2 = Answer::create(['question_id' => $question->id, 'name' => 'South', 'is_correct' => 1, 'status' => 1]);
        $b3 = Answer::create(['question_id' => $question->id, 'name' => 'East', 'is_correct' => 1, 'status' => 1]);
        $b4 = Answer::create(['question_id' => $question->id, 'name' => 'West', 'is_correct' => 1, 'status' => 1]);

        $exam = Exam::create([
            'name' => 'Directions Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 4,
        ]);
        $exam->standards()->attach($this->standard->id);
        $exam->questions()->attach($question->id);

        // Student gets 2 out of 4 correct
        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [
                $b1->id => 'North', // Correct (1)
                $b2->id => 'South', // Correct (2)
                $b3->id => 'WrongEast', // Incorrect
                $b4->id => 'WrongWest', // Incorrect
            ],
        ]);

        $detail->load('question.answers');

        $this->assertEquals(2, $detail->getCorrectBlanksCount());
        $this->assertEquals(2, $detail->getEarnedMarks());
        $this->assertEquals(4, $detail->getQuestionMarks());
        $this->assertTrue($detail->isPartiallyCorrect());
    }
}

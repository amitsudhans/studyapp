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

class AssertionReasonQuestionTest extends TestCase
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

    public function test_teacher_can_create_assertion_reason_question(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => '<p><strong>Assertion (A):</strong> The inner lining of the small intestine has numerous finger-like projections called villi.</p><p><strong>Reason (R):</strong> Villi increase the surface area for efficient absorption of digested food.</p>',
            'description' => 'CBSE Class 10 Biology Question on Digestion and Villi function.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'answers' => [
                [
                    'name' => 'Both (A) and (R) are true, and (R) is the correct explanation of (A).',
                    'is_correct' => 1,
                ],
                [
                    'name' => 'Both (A) and (R) are true, but (R) is not the correct explanation of (A).',
                    'is_correct' => 0,
                ],
                [
                    'name' => '(A) is true, but (R) is false.',
                    'is_correct' => 0,
                ],
                [
                    'name' => '(A) is false, but (R) is true.',
                    'is_correct' => 0,
                ],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('description', 'like', '%Digestion and Villi function%')->first();
        $this->assertNotNull($question);
        $this->assertTrue($question->isAssertionReason());
        $this->assertEquals(10, $question->type);
        $this->assertEquals(1, $question->marks);
        $this->assertEquals(4, $question->answers()->count());

        $correctAnswer = $question->answers()->where('is_correct', 1)->first();
        $this->assertNotNull($correctAnswer);
        $this->assertEquals('Both (A) and (R) are true, and (R) is the correct explanation of (A).', $correctAnswer->name);
    }

    public function test_assertion_reason_requires_all_four_options_and_single_correct_choice(): void
    {
        // Fail when fewer than 4 options provided
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Assertion: A, Reason: R',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'answers' => [
                ['name' => 'Option 1', 'is_correct' => 1],
                ['name' => 'Option 2', 'is_correct' => 0],
            ],
        ]);
        $response->assertSessionHasErrors('answers');

        // Fail when no correct option selected
        $response2 = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Assertion: A, Reason: R',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'answers' => [
                ['name' => 'Option 1', 'is_correct' => 0],
                ['name' => 'Option 2', 'is_correct' => 0],
                ['name' => 'Option 3', 'is_correct' => 0],
                ['name' => 'Option 4', 'is_correct' => 0],
            ],
        ]);
        $response2->assertSessionHasErrors('answers');
    }

    public function test_teacher_can_update_assertion_reason_question(): void
    {
        $question = Question::create([
            'name' => 'Initial A-R Question',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        Answer::create(['question_id' => $question->id, 'name' => 'Option A', 'is_correct' => 1, 'status' => 1]);
        Answer::create(['question_id' => $question->id, 'name' => 'Option B', 'is_correct' => 0, 'status' => 1]);
        Answer::create(['question_id' => $question->id, 'name' => 'Option C', 'is_correct' => 0, 'status' => 1]);
        Answer::create(['question_id' => $question->id, 'name' => 'Option D', 'is_correct' => 0, 'status' => 1]);

        $response = $this->actingAs($this->teacher)->put(route('questions.update', $question), [
            '_method' => 'PUT',
            'name' => 'Updated A-R Question',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'answers' => [
                ['name' => 'Both (A) and (R) are true, and (R) is correct explanation', 'is_correct' => 0],
                ['name' => 'Both (A) and (R) are true, but (R) is NOT correct explanation', 'is_correct' => 1],
                ['name' => '(A) is true, but (R) is false', 'is_correct' => 0],
                ['name' => '(A) is false, but (R) is true', 'is_correct' => 0],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $question->refresh();
        $this->assertEquals('Updated A-R Question', $question->name);
        $correctAnswer = $question->answers()->where('is_correct', 1)->first();
        $this->assertEquals('Both (A) and (R) are true, but (R) is NOT correct explanation', $correctAnswer->name);
    }

    public function test_student_auto_grading_for_assertion_reason_question(): void
    {
        $question = Question::create([
            'name' => 'Assertion: Light travels faster in vacuum than in glass. Reason: Glass is optically denser than vacuum.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_ASSERTION_REASON,
            'marks' => 1,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $ansA = Answer::create([
            'question_id' => $question->id,
            'name' => 'Both (A) and (R) are true, and (R) is the correct explanation of (A).',
            'is_correct' => 1,
            'status' => 1,
        ]);

        $ansB = Answer::create([
            'question_id' => $question->id,
            'name' => 'Both (A) and (R) are true, but (R) is not the correct explanation of (A).',
            'is_correct' => 0,
            'status' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Science Unit Test',
            'standard_id' => $this->standard->id,
            'created_by' => $this->teacher->id,
            'total_marks' => 1,
            'passing_marks' => 1,
            'duration' => 15,
            'status' => 1,
        ]);
        $exam->questions()->attach($question->id);

        $student = Student::factory()->create();

        // 1. Correct selection
        $detailCorrect = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'student_written_ans_id' => $ansA->id,
        ]);

        $this->assertEquals(1, $detailCorrect->getEarnedMarks());
        $this->assertTrue($detailCorrect->isCorrect());
        $this->assertTrue($detailCorrect->isAssertionReason());

        // 2. Incorrect selection
        $detailWrong = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'student_written_ans_id' => $ansB->id,
        ]);

        $this->assertEquals(0, $detailWrong->getEarnedMarks());
        $this->assertFalse($detailWrong->isCorrect());
    }
}

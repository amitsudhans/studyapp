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

class PuzzleQuestionTest extends TestCase
{
    use DatabaseTransactions;

    protected User $teacher;

    protected Standard $standard;

    protected function setUp(): void
    {
        parent::setUp();

        $syllabus = Syllabus::firstOrCreate(['name' => 'State Board']);
        $this->standard = Standard::firstOrCreate(['name' => 'Class 9', 'syllabus_id' => $syllabus->id]);

        $this->teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $this->teacher->id,
            'type' => 1, // Teacher
        ]);
    }

    public function test_teacher_can_create_puzzle_question_with_ordered_pieces(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Arrange the lifecycle of a butterfly in correct sequence.',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_PUZZLE,
            'marks' => 4,
            'answers' => [
                ['name' => '1. Egg'],
                ['name' => '2. Caterpillar'],
                ['name' => '3. Pupa (Chrysalis)'],
                ['name' => '4. Adult Butterfly'],
            ],
        ]);

        $response->assertRedirect(route('questions.index'));
        $response->assertSessionHas('status', 'Question created successfully!');

        $question = Question::where('name', 'Arrange the lifecycle of a butterfly in correct sequence.')->first();
        $this->assertNotNull($question);
        $this->assertTrue($question->isPuzzle());
        $this->assertEquals(Question::TYPE_PUZZLE, $question->type);
        $this->assertEquals('Puzzle', $question->type_name);
        $this->assertCount(4, $question->answers);

        // Verify sequence is preserved and all answers have is_correct = 1
        $pieces = $question->answers()->orderBy('id')->pluck('name')->toArray();
        $this->assertEquals([
            '1. Egg',
            '2. Caterpillar',
            '3. Pupa (Chrysalis)',
            '4. Adult Butterfly',
        ], $pieces);
    }

    public function test_puzzle_question_requires_at_least_two_pieces(): void
    {
        $response = $this->actingAs($this->teacher)->post(route('questions.store'), [
            'name' => 'Arrange the numbers',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_PUZZLE,
            'marks' => 2,
            'answers' => [
                ['name' => 'Only One Piece'],
            ],
        ]);

        $response->assertSessionHasErrors(['answers']);
    }

    public function test_student_can_solve_puzzle_and_earn_full_marks(): void
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
            'name' => 'Order water cycle phases',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_PUZZLE,
            'marks' => 3,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $a1 = Answer::create(['question_id' => $question->id, 'name' => 'Evaporation', 'is_correct' => 1, 'status' => 1]);
        $a2 = Answer::create(['question_id' => $question->id, 'name' => 'Condensation', 'is_correct' => 1, 'status' => 1]);
        $a3 = Answer::create(['question_id' => $question->id, 'name' => 'Precipitation', 'is_correct' => 1, 'status' => 1]);

        $exam = Exam::create([
            'name' => 'Science Puzzle Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 3,
        ]);
        $exam->standards()->attach($this->standard->id);
        $exam->questions()->attach($question->id);

        // Student submits correct sequence: [a1, a2, a3]
        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [$a1->id, $a2->id, $a3->id],
        ]);

        $detail->load('question.answers');

        $this->assertTrue($detail->isPuzzle());
        $this->assertEquals(3, $detail->getCorrectPuzzleCount());
        $this->assertTrue($detail->isCorrect());
        $this->assertFalse($detail->isPartiallyCorrect());
        $this->assertEquals(3, $detail->getEarnedMarks());
        $this->assertStringContainsString('#1 Evaporation', $detail->getSelectedAnswerDisplay());
        $this->assertStringContainsString('#2 Condensation', $detail->getSelectedAnswerDisplay());
        $this->assertStringContainsString('#3 Precipitation', $detail->getSelectedAnswerDisplay());
    }

    public function test_student_earns_partial_marks_for_partially_correct_puzzle(): void
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
            'name' => 'Order numbers 1 to 4',
            'standard_id' => $this->standard->id,
            'type' => Question::TYPE_PUZZLE,
            'marks' => 4,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $a1 = Answer::create(['question_id' => $question->id, 'name' => 'One', 'is_correct' => 1, 'status' => 1]);
        $a2 = Answer::create(['question_id' => $question->id, 'name' => 'Two', 'is_correct' => 1, 'status' => 1]);
        $a3 = Answer::create(['question_id' => $question->id, 'name' => 'Three', 'is_correct' => 1, 'status' => 1]);
        $a4 = Answer::create(['question_id' => $question->id, 'name' => 'Four', 'is_correct' => 1, 'status' => 1]);

        $exam = Exam::create([
            'name' => 'Number Puzzle Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 4,
        ]);
        $exam->standards()->attach($this->standard->id);
        $exam->questions()->attach($question->id);

        // Student places a1 correctly, swaps a2 & a3, and a4 correctly:
        // Position 0: a1 (Correct)
        // Position 1: a3 (Wrong)
        // Position 2: a2 (Wrong)
        // Position 3: a4 (Correct)
        // 2 out of 4 correct -> 2 marks
        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'match_answers' => [$a1->id, $a3->id, $a2->id, $a4->id],
        ]);

        $detail->load('question.answers');

        $this->assertEquals(2, $detail->getCorrectPuzzleCount());
        $this->assertFalse($detail->isCorrect());
        $this->assertTrue($detail->isPartiallyCorrect());
        $this->assertEquals(2, $detail->getEarnedMarks());

        $review = $detail->getPuzzleReview();
        $this->assertCount(4, $review);
        $this->assertTrue($review[0]['is_correct']);
        $this->assertFalse($review[1]['is_correct']);
        $this->assertFalse($review[2]['is_correct']);
        $this->assertTrue($review[3]['is_correct']);
    }
}

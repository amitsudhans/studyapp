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
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Support\Facades\Schema;
use Tests\TestCase;

class StudentExamDetailTest extends TestCase
{
    use DatabaseTransactions;

    public function test_student_exam_details_table_has_expected_columns(): void
    {
        $this->assertTrue(Schema::hasTable('student_exam_details'));
        $this->assertTrue(Schema::hasColumns('student_exam_details', [
            'id',
            'student_id',
            'exam_id',
            'question_id',
            'student_written_ans_id',
            'created_at',
            'updated_at',
        ]));
    }

    public function test_can_create_student_exam_detail_record_and_relations(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);

        $studentUser = User::factory()->create();
        $student = Student::create([
            'id' => $studentUser->id,
            'name' => 'Test Student',
            'standard_id' => $standard->id,
        ]);

        $teacher = User::factory()->create();
        $exam = Exam::create([
            'name' => 'Final Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 10,
        ]);

        $question = Question::create([
            'name' => 'What is 2 + 2?',
            'standard_id' => $standard->id,
            'type' => 1,
            'marks' => 2,
            'created_by' => $teacher->id,
            'status' => 1,
        ]);

        $answer = Answer::create([
            'name' => '4',
            'question_id' => $question->id,
            'is_correct' => 1,
            'status' => 1,
        ]);

        $detail = StudentExamDetail::create([
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'student_written_ans_id' => $answer->id,
        ]);

        $this->assertDatabaseHas('student_exam_details', [
            'id' => $detail->id,
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $question->id,
            'student_written_ans_id' => $answer->id,
        ]);

        $this->assertEquals($student->id, $detail->student->id);
        $this->assertEquals($exam->id, $detail->exam->id);
        $this->assertEquals($question->id, $detail->question->id);
        $this->assertEquals($answer->id, $detail->writtenAnswer->id);
    }
}

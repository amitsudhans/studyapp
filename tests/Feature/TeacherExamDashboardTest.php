<?php

namespace Tests\Feature;

use App\Models\Answer;
use App\Models\Exam;
use App\Models\ExamAssign;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Student;
use App\Models\StudentExamDetail;
use App\Models\Syllabus;
use App\Models\TeacherStandard;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class TeacherExamDashboardTest extends TestCase
{
    use DatabaseTransactions;

    public function test_teacher_sees_exam_performance_report_and_completed_students(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => 'Grade 10', 'syllabus_id' => $syllabus->id]);

        // Create Teacher User
        $teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $teacher->id,
            'name' => 'Prof. Smith',
            'type' => 1, // Teacher
        ]);
        TeacherStandard::create([
            'user_id' => $teacher->id,
            'standard_id' => $standard->id,
        ]);

        // Create Student User
        $studentUser = User::factory()->create();
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Alice Student',
            'type' => 2, // Student
        ]);
        $student = Student::create([
            'id' => $studentUser->id,
            'name' => 'Alice Student',
            'standard_id' => $standard->id,
        ]);

        // Create Exam
        $exam = Exam::create([
            'name' => 'Physics Midterm 2026',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 20,
        ]);
        ExamAssign::create([
            'exam_id' => $exam->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);

        // Create Question & Answer
        $question = Question::create([
            'name' => 'What is the unit of Force?',
            'type' => 1, // MCQ single
            'marks' => 20,
            'status' => 1,
            'created_by' => $teacher->id,
            'standard_id' => $standard->id,
        ]);
        $correctAnswer = Answer::create([
            'question_id' => $question->id,
            'name' => 'Newton',
            'is_correct' => 1,
        ]);
        $exam->questions()->attach($question->id, ['status' => 1]);

        // Create Submission detail
        StudentExamDetail::create([
            'exam_id' => $exam->id,
            'student_id' => $student->id,
            'question_id' => $question->id,
            'student_written_ans_id' => $correctAnswer->id,
        ]);

        // Visit Dashboard as Teacher
        $response = $this->actingAs($teacher)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Exam Performance');
        $response->assertSee('Physics Midterm 2026');
        $response->assertSee('1 Student(s) Completed');
        $response->assertSee('Alice Student');
        $response->assertSee('20 / 20');
        $response->assertSee('View Question Marks');
    }
}

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

class StudentExamSubmissionTest extends TestCase
{
    use DatabaseTransactions;

    public function test_student_can_submit_exam_and_save_to_student_exam_details(): void
    {
        // 1. Setup syllabus, standard, student
        $syllabus = Syllabus::firstOrCreate(['name' => 'State Board']);
        $standard = Standard::firstOrCreate(['name' => '10th Class', 'syllabus_id' => $syllabus->id]);

        $studentUser = User::factory()->create();
        UserProfile::create([
            'user_id' => $studentUser->id,
            'type' => 2, // Student type
            'standard_id' => $standard->id,
        ]);
        $student = Student::create([
            'id' => $studentUser->id,
            'name' => $studentUser->name,
            'standard_id' => $standard->id,
        ]);

        // 2. Setup teacher, exam, questions, and answers
        $teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $teacher->id,
            'type' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Midterm Mathematics Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 20,
        ]);
        $exam->standards()->attach($standard->id);

        // Question 1
        $q1 = Question::create([
            'name' => 'What is the square root of 64?',
            'standard_id' => $standard->id,
            'type' => 1,
            'marks' => 10,
            'created_by' => $teacher->id,
            'status' => 1,
        ]);
        $a1_correct = Answer::create([
            'name' => '8',
            'question_id' => $q1->id,
            'is_correct' => 1,
            'status' => 1,
        ]);
        $a1_wrong = Answer::create([
            'name' => '6',
            'question_id' => $q1->id,
            'is_correct' => 0,
            'status' => 1,
        ]);
        $exam->questions()->attach($q1->id);

        // Question 2
        $q2 = Question::create([
            'name' => 'What is 15 x 3?',
            'standard_id' => $standard->id,
            'type' => 1,
            'marks' => 10,
            'created_by' => $teacher->id,
            'status' => 1,
        ]);
        $a2_correct = Answer::create([
            'name' => '45',
            'question_id' => $q2->id,
            'is_correct' => 1,
            'status' => 1,
        ]);
        $exam->questions()->attach($q2->id);

        // Verify initial state: NO records in student_exam_details
        $this->assertEquals(0, StudentExamDetail::where('student_id', $student->id)->where('exam_id', $exam->id)->count());

        // 3. Submit exam on behalf of student
        $response = $this->actingAs($studentUser)->post(route('student.exams.submit', $exam), [
            'answers' => [
                $q1->id => $a1_correct->id,
                $q2->id => $a2_correct->id,
            ],
        ]);

        $response->assertRedirect(route('dashboard'));
        $response->assertSessionHas('status');

        // 4. Assert records created in student_exam_details
        $this->assertDatabaseHas('student_exam_details', [
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $q1->id,
            'student_written_ans_id' => $a1_correct->id,
        ]);

        $this->assertDatabaseHas('student_exam_details', [
            'student_id' => $student->id,
            'exam_id' => $exam->id,
            'question_id' => $q2->id,
            'student_written_ans_id' => $a2_correct->id,
        ]);

        $this->assertEquals(2, StudentExamDetail::where('student_id', $student->id)->where('exam_id', $exam->id)->count());
    }

    public function test_student_cannot_submit_same_exam_twice(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'CBSE']);
        $standard = Standard::firstOrCreate(['name' => '8th Class', 'syllabus_id' => $syllabus->id]);

        $studentUser = User::factory()->create();
        UserProfile::create([
            'user_id' => $studentUser->id,
            'type' => 2,
            'standard_id' => $standard->id,
        ]);
        $student = Student::create([
            'id' => $studentUser->id,
            'name' => $studentUser->name,
            'standard_id' => $standard->id,
        ]);

        $teacher = User::factory()->create();
        $exam = Exam::create([
            'name' => 'Physics Quiz',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 5,
        ]);

        $q = Question::create([
            'name' => 'Speed of light unit?',
            'standard_id' => $standard->id,
            'type' => 1,
            'marks' => 5,
            'created_by' => $teacher->id,
            'status' => 1,
        ]);
        $a = Answer::create([
            'name' => 'm/s',
            'question_id' => $q->id,
            'is_correct' => 1,
            'status' => 1,
        ]);
        $exam->questions()->attach($q->id);

        // First submission
        $this->actingAs($studentUser)->post(route('student.exams.submit', $exam), [
            'answers' => [$q->id => $a->id],
        ]);

        // Second submission attempt
        $response = $this->actingAs($studentUser)->post(route('student.exams.submit', $exam), [
            'answers' => [$q->id => $a->id],
        ]);

        $response->assertSessionHas('error', 'You have already submitted this exam.');
    }
}

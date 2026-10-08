<?php

namespace Tests\Feature;

use App\Models\Exam;
use App\Models\ExamAssign;
use App\Models\Standard;
use App\Models\Student;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class StudentExamDashboardTest extends TestCase
{
    use DatabaseTransactions;

    public function test_student_sees_exams_assigned_to_their_standard_on_dashboard(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard10 = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);
        $standard12 = Standard::firstOrCreate(['name' => '12th Standard', 'syllabus_id' => $syllabus->id]);

        $teacher = User::factory()->create();

        // Exam for 10th Standard
        $examFor10th = Exam::create([
            'name' => 'Algebra 10th Midterm',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 100,
        ]);
        ExamAssign::create([
            'exam_id' => $examFor10th->id,
            'standard_id' => $standard10->id,
            'status' => 1,
        ]);

        // Exam for 12th Standard
        $examFor12th = Exam::create([
            'name' => 'Calculus 12th Final',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 150,
        ]);
        ExamAssign::create([
            'exam_id' => $examFor12th->id,
            'standard_id' => $standard12->id,
            'status' => 1,
        ]);

        // Create a student enrolled in 10th Standard
        $studentUser = User::factory()->create(['email' => 'student10@example.com']);
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Student Ten',
            'type' => 2, // Student
        ]);
        Student::create([
            'id' => $studentUser->id,
            'name' => 'Student Ten',
            'standard_id' => $standard10->id,
        ]);

        $response = $this->actingAs($studentUser)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Student Dashboard');
        $response->assertSee('10th Standard');
        $response->assertSee('Algebra 10th Midterm');
        $response->assertSee('100 Marks');
        $response->assertDontSee('Calculus 12th Final');
    }

    public function test_student_with_no_exams_assigned_sees_empty_state_message(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '9th Standard', 'syllabus_id' => $syllabus->id]);

        $studentUser = User::factory()->create(['email' => 'student9@example.com']);
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Student Nine',
            'type' => 2,
        ]);
        Student::create([
            'id' => $studentUser->id,
            'name' => 'Student Nine',
            'standard_id' => $standard->id,
        ]);

        $response = $this->actingAs($studentUser)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('No Exams Assigned Yet');
        $response->assertSee('9th Standard');
    }
}

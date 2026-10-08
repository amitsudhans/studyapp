<?php

namespace Tests\Feature;

use App\Models\Exam;
use App\Models\ExamAssign;
use App\Models\Standard;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Support\Facades\Schema;
use Tests\TestCase;

class ExamAssignTest extends TestCase
{
    use DatabaseTransactions;

    public function test_exam_assign_table_has_expected_columns(): void
    {
        $this->assertTrue(Schema::hasTable('exam_assign'));
        $this->assertTrue(Schema::hasColumns('exam_assign', [
            'id',
            'exam_id',
            'standard_id',
            'status',
            'created_at',
            'updated_at',
        ]));
    }

    public function test_can_create_exam_assign_record_and_belongs_to_relations(): void
    {
        $teacher = User::factory()->create();
        $exam = Exam::create([
            'name' => 'Midterm Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 100,
        ]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);

        $assignment = ExamAssign::create([
            'exam_id' => $exam->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);

        $this->assertDatabaseHas('exam_assign', [
            'id' => $assignment->id,
            'exam_id' => $exam->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);

        $this->assertEquals($exam->id, $assignment->exam->id);
        $this->assertEquals($standard->id, $assignment->standard->id);
    }

    public function test_exam_assign_status_inactive(): void
    {
        $teacher = User::factory()->create();
        $exam = Exam::create([
            'name' => 'Final Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 50,
        ]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '12th Standard', 'syllabus_id' => $syllabus->id]);

        $assignment = ExamAssign::create([
            'exam_id' => $exam->id,
            'standard_id' => $standard->id,
            'status' => 2,
        ]);

        $this->assertDatabaseHas('exam_assign', [
            'id' => $assignment->id,
            'status' => 2,
        ]);
    }

    public function test_only_teachers_and_admins_can_assign_exam_to_standard_via_endpoint(): void
    {
        $teacherUser = User::factory()->create(['email' => 'teacherassign@example.com']);
        UserProfile::create([
            'user_id' => $teacherUser->id,
            'name' => 'Teacher User',
            'type' => 1, // Teacher
        ]);

        $adminUser = User::factory()->create(['email' => 'adminassign@example.com']);
        UserProfile::create([
            'user_id' => $adminUser->id,
            'name' => 'Admin User',
            'type' => 0, // Admin
        ]);

        $studentUser = User::factory()->create(['email' => 'studentassign@example.com']);
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Student User',
            'type' => 2, // Student
        ]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate([
            'name' => '10th Standard',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacherUser->id,
        ]);

        $exam = Exam::create([
            'name' => 'Physics Midterm',
            'created_by' => $teacherUser->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 50,
        ]);

        // Student attempt -> 403
        $studentResponse = $this->actingAs($studentUser)->post("/exams/{$exam->id}/assign-standards", [
            'standard_ids' => [$standard->id],
            'status' => 1,
        ]);
        $studentResponse->assertStatus(403);

        // Teacher attempt -> Success (Populates exam_assign table)
        $teacherResponse = $this->actingAs($teacherUser)->post("/exams/{$exam->id}/assign-standards", [
            'standard_ids' => [$standard->id],
            'status' => 1,
        ]);
        $teacherResponse->assertRedirect();

        $this->assertDatabaseHas('exam_assign', [
            'exam_id' => $exam->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);

        // Admin attempt -> Success
        $adminResponse = $this->actingAs($adminUser)->post("/exams/{$exam->id}/assign-standards", [
            'standard_ids' => [$standard->id],
            'status' => 1,
        ]);
        $adminResponse->assertRedirect();
    }

    public function test_teacher_can_only_assign_exam_to_standards_created_by_them(): void
    {
        $teacher1 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher1->id, 'name' => 'Teacher 1', 'type' => 1]);

        $teacher2 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher2->id, 'name' => 'Teacher 2', 'type' => 1]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standardByTeacher2 = Standard::create([
            'name' => 'Class Created By Teacher 2',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher2->id,
        ]);

        $exam = Exam::create([
            'name' => 'Teacher 1 Exam',
            'created_by' => $teacher1->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 20,
        ]);

        // Teacher 1 attempts to assign exam to a standard created by Teacher 2 -> Validation error
        $response = $this->actingAs($teacher1)->post("/exams/{$exam->id}/assign-standards", [
            'standard_ids' => [$standardByTeacher2->id],
            'status' => 1,
        ]);

        $response->assertSessionHasErrors(['standard_ids']);
        $this->assertDatabaseMissing('exam_assign', [
            'exam_id' => $exam->id,
            'standard_id' => $standardByTeacher2->id,
        ]);
    }
}

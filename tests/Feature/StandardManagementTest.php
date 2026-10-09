<?php

namespace Tests\Feature;

use App\Models\Standard;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class StandardManagementTest extends TestCase
{
    use RefreshDatabase;

    public function test_teacher_can_create_standard_with_created_by_their_user_id(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $teacher->id,
            'mobile' => '1234567890',
            'address' => 'Test Address',
            'type' => 1, // Teacher
        ]);

        $response = $this->actingAs($teacher)->post('/standards', [
            'name' => 'Class 10 - Mathematics',
            'syllabus_id' => $syllabus->id,
        ]);

        $response->assertRedirect();
        $this->assertDatabaseHas('standards', [
            'name' => 'Class 10 - Mathematics',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);

        $standard = Standard::where('name', 'Class 10 - Mathematics')->first();
        $this->assertTrue($teacher->standards->contains($standard->id));
    }

    public function test_teacher_can_edit_own_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);
        $teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $teacher->id,
            'mobile' => '1234567890',
            'address' => 'Test Address',
            'type' => 1, // Teacher
        ]);

        $standard = Standard::create(['name' => 'Class 9', 'syllabus_id' => $syllabus->id, 'created_by' => $teacher->id]);

        $response = $this->actingAs($teacher)->put("/standards/{$standard->id}", [
            'name' => 'Class 9 - Advanced',
        ]);

        $response->assertRedirect();
        $this->assertDatabaseHas('standards', [
            'id' => $standard->id,
            'name' => 'Class 9 - Advanced',
            'created_by' => $teacher->id,
        ]);
    }

    public function test_teacher_cannot_edit_admin_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);
        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);
        $adminStandard = Standard::create(['name' => 'Admin Standard Class', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);

        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $response = $this->actingAs($teacher)->put("/standards/{$adminStandard->id}", [
            'name' => 'Attempted Edit By Teacher',
        ]);

        $response->assertStatus(403);
    }

    public function test_teacher_only_sees_own_and_admin_standards(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);
        $adminStandard = Standard::create(['name' => 'Admin Class Alpha', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);

        $teacher1 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher1->id, 'type' => 1]);
        $teacher1Standard = Standard::create(['name' => 'Teacher 1 Unique Standard', 'syllabus_id' => $syllabus->id, 'created_by' => $teacher1->id]);

        $teacher2 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher2->id, 'type' => 1]);
        $teacher2Standard = Standard::create(['name' => 'Teacher 2 Private Standard', 'syllabus_id' => $syllabus->id, 'created_by' => $teacher2->id]);

        $response = $this->actingAs($teacher1)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Admin Class Alpha');
        $response->assertSee('Teacher 1 Unique Standard');
        $response->assertDontSee('Teacher 2 Private Standard');
    }

    public function test_student_cannot_create_or_edit_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);
        $standard = Standard::create(['name' => 'Class 11', 'syllabus_id' => $syllabus->id]);

        $student = User::factory()->create();
        UserProfile::create([
            'user_id' => $student->id,
            'mobile' => '9876543210',
            'address' => 'Student Address',
            'type' => 2, // Student
        ]);

        $this->actingAs($student)->post('/standards', [
            'name' => 'Class 12',
            'syllabus_id' => $syllabus->id,
        ])->assertStatus(403);

        $this->actingAs($student)->put("/standards/{$standard->id}", [
            'name' => 'Class 11 Updated',
        ])->assertStatus(403);
    }

    public function test_teacher_dashboard_shows_add_standard_and_standards_directory(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);
        $standard = Standard::create(['name' => 'Class 8', 'syllabus_id' => $syllabus->id]);

        $teacher = User::factory()->create();
        UserProfile::create([
            'user_id' => $teacher->id,
            'mobile' => '1234567890',
            'address' => 'Test Address',
            'type' => 1, // Teacher
        ]);

        $response = $this->actingAs($teacher)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Add Standard');
        $response->assertSee('Standards / Classes Directory');
        $response->assertSee('Class 8');
    }

    public function test_teacher_can_assign_students_to_own_created_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $standard = Standard::create([
            'name' => 'Teacher Created Class 10',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);
        $teacher->standards()->attach($standard->id);

        $student1 = User::factory()->create(['name' => 'Student One']);
        UserProfile::create(['user_id' => $student1->id, 'type' => 2]);

        $student2 = User::factory()->create(['name' => 'Student Two']);
        UserProfile::create(['user_id' => $student2->id, 'type' => 2]);

        $response = $this->actingAs($teacher)->post("/standards/{$standard->id}/assign-students", [
            'student_ids' => [$student1->id, $student2->id],
            '_assign_mode' => 'bulk',
        ]);

        $response->assertRedirect();
        $this->assertDatabaseHas('students', [
            'id' => $student1->id,
            'standard_id' => $standard->id,
        ]);
        $this->assertDatabaseHas('students', [
            'id' => $student2->id,
            'standard_id' => $standard->id,
        ]);
    }

    public function test_teacher_cannot_assign_students_to_another_teachers_private_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $teacher1 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher1->id, 'type' => 1]);

        $teacher2 = User::factory()->create();
        UserProfile::create(['user_id' => $teacher2->id, 'type' => 1]);

        $otherStandard = Standard::create([
            'name' => 'Teacher 2 Private Class',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher2->id,
        ]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $response = $this->actingAs($teacher1)->post("/standards/{$otherStandard->id}/assign-students", [
            'student_ids' => [$student->id],
        ]);

        $response->assertStatus(403);
    }

    public function test_student_cannot_assign_students_to_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);
        $standard = Standard::create(['name' => 'Class 10', 'syllabus_id' => $syllabus->id]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $response = $this->actingAs($student)->post("/standards/{$standard->id}/assign-students", [
            'student_ids' => [$student->id],
        ]);

        $response->assertStatus(403);
    }

    public function test_admin_can_see_and_manage_all_standards_including_delete_and_search(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $teacherStandard = Standard::create([
            'name' => 'Teacher Standard For Admin Test',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);

        $adminStandard = Standard::create([
            'name' => 'Admin Custom Class',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        // 1. Admin dashboard sees all standards
        $response = $this->actingAs($admin)->get('/dashboard?standards_page=1');
        $response->assertStatus(200);
        $response->assertSee('Teacher Standard For Admin Test');
        $response->assertSee('Admin Custom Class');

        // 2. Admin search filter
        $searchResponse = $this->actingAs($admin)->get('/dashboard?standards_search=Admin+Custom');
        $searchResponse->assertStatus(200);
        $searchResponse->assertSee('Admin Custom Class');

        // 3. Admin can edit teacher created standard
        $editResponse = $this->actingAs($admin)->put("/standards/{$teacherStandard->id}", [
            'name' => 'Updated By Admin',
        ]);
        $editResponse->assertRedirect();
        $this->assertDatabaseHas('standards', [
            'id' => $teacherStandard->id,
            'name' => 'Updated By Admin',
        ]);

        // 4. Admin can delete standard
        $deleteResponse = $this->actingAs($admin)->delete("/standards/{$teacherStandard->id}");
        $deleteResponse->assertRedirect();
        $this->assertDatabaseMissing('standards', [
            'id' => $teacherStandard->id,
        ]);
    }
}

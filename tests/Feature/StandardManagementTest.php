<?php

namespace Tests\Feature;

use App\Models\Standard;
use App\Models\Student;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\DB;
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

        $adminStandard = Standard::create([
            'name' => 'Class 10 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => null,
        ]);
        $teacher->standards()->attach($adminStandard->id);

        $standard = Standard::create([
            'name' => 'Teacher Created Class 10',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);
        $teacher->standards()->attach($standard->id);

        $student1 = User::factory()->create(['name' => 'Student One']);
        UserProfile::create(['user_id' => $student1->id, 'type' => 2]);
        Student::create(['id' => $student1->id, 'name' => $student1->name, 'standard_id' => $adminStandard->id]);
        DB::table('student_standards')->insert(['student_id' => $student1->id, 'standard_id' => $adminStandard->id]);

        $student2 = User::factory()->create(['name' => 'Student Two']);
        UserProfile::create(['user_id' => $student2->id, 'type' => 2]);
        Student::create(['id' => $student2->id, 'name' => $student2->name, 'standard_id' => $adminStandard->id]);
        DB::table('student_standards')->insert(['student_id' => $student2->id, 'standard_id' => $adminStandard->id]);

        $response = $this->actingAs($teacher)->post("/standards/{$standard->id}/assign-students", [
            'student_ids' => [$student1->id, $student2->id],
            '_assign_mode' => 'bulk',
        ]);

        $response->assertRedirect();
        $this->assertDatabaseHas('students', [
            'id' => $student1->id,
            'standard_id' => $adminStandard->id,
        ]);
        $this->assertDatabaseHas('students', [
            'id' => $student2->id,
            'standard_id' => $adminStandard->id,
        ]);
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student1->id,
            'standard_id' => $standard->id,
        ]);
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student2->id,
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

    public function test_student_assigned_to_one_admin_standard_cannot_be_assigned_to_another_admin_standard(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $adminStd1 = Standard::create([
            'name' => 'Class 7 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $adminStd2 = Standard::create([
            'name' => 'Class 8 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $student = User::factory()->create(['name' => 'Student Test']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        // Assign student to adminStd1 (Class 7)
        $this->actingAs($admin)->post("/standards/{$adminStd1->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect();

        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);

        // Attempt to assign student to adminStd2 (Class 8) should fail with validation error
        $response = $this->actingAs($admin)->post("/standards/{$adminStd2->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ]);

        $response->assertSessionHasErrors('student_ids');
        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd2->id,
        ]);
    }

    public function test_student_in_admin_standard_can_still_be_assigned_to_teacher_created_groups(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $adminStd = Standard::create([
            'name' => 'Class 7 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $teacher = User::factory()->create(['name' => 'Teacher Group Owner']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);
        $teacher->standards()->attach($adminStd->id);

        $teacherGroup = Standard::create([
            'name' => 'Gr-1 Math Club',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);

        $student = User::factory()->create(['name' => 'Student In Group']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        // Assign to adminStd
        $this->actingAs($admin)->post("/standards/{$adminStd->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect();

        // Assign to teacher group
        $response = $this->actingAs($teacher)->post("/standards/{$teacherGroup->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ]);

        $response->assertRedirect();
        $response->assertSessionHasNoErrors();

        // Student is in both student_standards records
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd->id,
        ]);
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $teacherGroup->id,
        ]);

        // Official class standard in students table remains the admin standard
        $this->assertDatabaseHas('students', [
            'id' => $student->id,
            'standard_id' => $adminStd->id,
        ]);
    }

    public function test_unassigned_student_from_admin_standard_becomes_free_to_assign_to_other_admin_standards(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $adminStd1 = Standard::create([
            'name' => 'Class 7 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $adminStd2 = Standard::create([
            'name' => 'Class 8 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $student = User::factory()->create(['name' => 'Student Free Test']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        // 1. Assign student to adminStd1 (Class 7)
        $this->actingAs($admin)->post("/standards/{$adminStd1->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect();

        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);

        // 2. While assigned to adminStd1, assigning to adminStd2 fails
        $failResponse = $this->actingAs($admin)->post("/standards/{$adminStd2->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ]);
        $failResponse->assertSessionHasErrors('student_ids');

        // 3. Unassign student from adminStd1 (bulk mode without this student)
        $unassignResponse = $this->actingAs($admin)->post("/standards/{$adminStd1->id}/assign-students", [
            'student_ids' => [],
            '_assign_mode' => 'bulk',
        ]);
        $unassignResponse->assertRedirect();
        $unassignResponse->assertSessionHasNoErrors();

        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);
        $this->assertDatabaseMissing('students', [
            'id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);

        // 4. Now student is free and CAN be assigned to adminStd2 (Class 8)
        $assignResponse = $this->actingAs($admin)->post("/standards/{$adminStd2->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ]);
        $assignResponse->assertRedirect();
        $assignResponse->assertSessionHasNoErrors();

        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd2->id,
        ]);
        $this->assertDatabaseHas('students', [
            'id' => $student->id,
            'standard_id' => $adminStd2->id,
        ]);
    }

    public function test_unassign_single_student_endpoint_frees_student_for_reassignment(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $adminStd1 = Standard::create([
            'name' => 'Class 7 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $adminStd2 = Standard::create([
            'name' => 'Class 8 CBSE',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $student = User::factory()->create(['name' => 'Single Unassign Student']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        // Assign to adminStd1
        $this->actingAs($admin)->post("/standards/{$adminStd1->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect();

        // Unassign via single unassign route
        $unassignResponse = $this->actingAs($admin)->post("/standards/{$adminStd1->id}/unassign-student", [
            'student_id' => $student->id,
        ]);
        $unassignResponse->assertRedirect();
        $unassignResponse->assertSessionHasNoErrors();

        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);
        $this->assertDatabaseMissing('students', [
            'id' => $student->id,
            'standard_id' => $adminStd1->id,
        ]);

        // When viewing dashboard or standards page, freed student has empty data-admin-std-id
        $dashboardResponse = $this->actingAs($admin)->get('/dashboard');
        $dashboardResponse->assertStatus(200);
        $dashboardResponse->assertSee('data-student-id="'.$student->id.'"', false);
        $this->assertMatchesRegularExpression(
            '/data-student-id="'.$student->id.'"[^>]*data-admin-std-id=""/',
            $dashboardResponse->getContent()
        );

        $standardsResponse = $this->actingAs($admin)->get('/standards');
        $standardsResponse->assertStatus(200);
        $this->assertMatchesRegularExpression(
            '/data-student-id="'.$student->id.'"[^>]*data-admin-std-id=""/',
            $standardsResponse->getContent()
        );

        // Now student can be assigned to adminStd2
        $assignResponse = $this->actingAs($admin)->post("/standards/{$adminStd2->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ]);
        $assignResponse->assertRedirect();
        $assignResponse->assertSessionHasNoErrors();

        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $adminStd2->id,
        ]);

        // After assignment, freed student now has adminStd2 id in data-admin-std-id
        $dashboardResponse2 = $this->actingAs($admin)->get('/dashboard');
        $dashboardResponse2->assertStatus(200);
        $this->assertMatchesRegularExpression(
            '/data-student-id="'.$student->id.'"[^>]*data-admin-std-id="'.$adminStd2->id.'"/',
            $dashboardResponse2->getContent()
        );
    }

    public function test_teacher_can_only_assign_students_from_assigned_admin_standards_to_custom_group(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        // 1. Admin creates Class 7, Class 8, Class 9
        $class7 = Standard::create(['name' => 'Class 7 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);
        $class8 = Standard::create(['name' => 'Class 8 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);
        $class9 = Standard::create(['name' => 'Class 9 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);

        // 2. Admin assigns Teacher to Class 7 and Class 8 (NOT Class 9)
        $teacher = User::factory()->create(['name' => 'Teacher Kumar']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);
        $teacher->standards()->attach([$class7->id, $class8->id]);

        // 3. Students
        $studentClass7 = User::factory()->create(['name' => 'Student In Class 7']);
        UserProfile::create(['user_id' => $studentClass7->id, 'type' => 2]);
        Student::create(['id' => $studentClass7->id, 'name' => $studentClass7->name, 'standard_id' => $class7->id]);
        DB::table('student_standards')->insert(['student_id' => $studentClass7->id, 'standard_id' => $class7->id]);

        $studentClass8 = User::factory()->create(['name' => 'Student In Class 8']);
        UserProfile::create(['user_id' => $studentClass8->id, 'type' => 2]);
        Student::create(['id' => $studentClass8->id, 'name' => $studentClass8->name, 'standard_id' => $class8->id]);
        DB::table('student_standards')->insert(['student_id' => $studentClass8->id, 'standard_id' => $class8->id]);

        $studentClass9 = User::factory()->create(['name' => 'Student In Class 9']);
        UserProfile::create(['user_id' => $studentClass9->id, 'type' => 2]);
        Student::create(['id' => $studentClass9->id, 'name' => $studentClass9->name, 'standard_id' => $class9->id]);
        DB::table('student_standards')->insert(['student_id' => $studentClass9->id, 'standard_id' => $class9->id]);

        $unassignedStudent = User::factory()->create(['name' => 'Unassigned Student']);
        UserProfile::create(['user_id' => $unassignedStudent->id, 'type' => 2]);

        // 4. Teacher creates custom group "Math Olympiad Group"
        $customGroup = Standard::create([
            'name' => 'Math Olympiad Group',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);
        $teacher->standards()->attach($customGroup->id);

        // 5. Teacher assigns Class 7 student and Class 8 student -> SUCCESS
        $successResponse = $this->actingAs($teacher)->post("/standards/{$customGroup->id}/assign-students", [
            'student_ids' => [$studentClass7->id, $studentClass8->id],
            '_assign_mode' => 'bulk',
        ]);
        $successResponse->assertRedirect();
        $successResponse->assertSessionHasNoErrors();

        $this->assertDatabaseHas('student_standards', [
            'student_id' => $studentClass7->id,
            'standard_id' => $customGroup->id,
        ]);
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $studentClass8->id,
            'standard_id' => $customGroup->id,
        ]);

        // Official admin standards remain intact
        $this->assertDatabaseHas('students', [
            'id' => $studentClass7->id,
            'standard_id' => $class7->id,
        ]);
        $this->assertDatabaseHas('students', [
            'id' => $studentClass8->id,
            'standard_id' => $class8->id,
        ]);

        // 6. Teacher attempts to assign Student from Class 9 -> FAILS
        $failResponse1 = $this->actingAs($teacher)->post("/standards/{$customGroup->id}/assign-students", [
            'student_ids' => [$studentClass7->id, $studentClass9->id],
            '_assign_mode' => 'bulk',
        ]);
        $failResponse1->assertSessionHasErrors('student_ids');
        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $studentClass9->id,
            'standard_id' => $customGroup->id,
        ]);

        // 7. Teacher attempts to assign Unassigned student -> FAILS
        $failResponse2 = $this->actingAs($teacher)->post("/standards/{$customGroup->id}/assign-students", [
            'student_ids' => [$unassignedStudent->id],
            '_assign_mode' => 'bulk',
        ]);
        $failResponse2->assertSessionHasErrors('student_ids');
        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $unassignedStudent->id,
            'standard_id' => $customGroup->id,
        ]);

        // 8. In UI (Dashboard & Standards directory), only Class 7 and Class 8 students appear in the teacher's assign modal
        $standardsView = $this->actingAs($teacher)->get('/standards');
        $standardsView->assertStatus(200);
        $standardsView->assertSee('Student In Class 7');
        $standardsView->assertSee('Student In Class 8');
        $standardsView->assertDontSee('Student In Class 9');
        $standardsView->assertDontSee('Unassigned Student');

        $dashboardView = $this->actingAs($teacher)->get('/dashboard');
        $dashboardView->assertStatus(200);
        $dashboardView->assertSee('Student In Class 7');
        $dashboardView->assertSee('Student In Class 8');
        $dashboardView->assertDontSee('Student In Class 9');
        $dashboardView->assertDontSee('Unassigned Student');
    }

    public function test_moving_or_unassigning_student_from_admin_standard_removes_student_from_teachers_custom_group(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        // 1. Admin creates Class 3 and Class 4
        $class3 = Standard::create(['name' => 'Class 3 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);
        $class4 = Standard::create(['name' => 'Class 4 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);

        // 2. Admin assigns Class 3 to Teacher
        $teacher = User::factory()->create(['name' => 'Class 3 Teacher']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);
        $teacher->standards()->attach([$class3->id]);

        // 3. Teacher creates a custom group
        $teacherGroup = Standard::create([
            'name' => 'Class 3 Math Wizards',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);
        $teacher->standards()->attach([$teacherGroup->id]);

        // 4. Student enrolled in Class 3
        $student = User::factory()->create(['name' => 'Bobby Student']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);
        Student::create(['id' => $student->id, 'name' => $student->name, 'standard_id' => $class3->id]);
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $class3->id]);

        // 5. Teacher assigns student to custom group
        $this->actingAs($teacher)->post("/standards/{$teacherGroup->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect()->assertSessionHasNoErrors();

        // Verify student is in both Class 3 and Teacher's custom group
        $this->assertDatabaseHas('student_standards', ['student_id' => $student->id, 'standard_id' => $class3->id]);
        $this->assertDatabaseHas('student_standards', ['student_id' => $student->id, 'standard_id' => $teacherGroup->id]);

        // CASE A: Admin unassigns student from Class 3 via single unassign endpoint
        $this->actingAs($admin)->post("/standards/{$class3->id}/unassign-student", [
            'student_id' => $student->id,
        ])->assertRedirect()->assertSessionHasNoErrors();

        // Student is removed from Class 3 AND ALSO removed from Teacher's custom group!
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $class3->id]);
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $teacherGroup->id]);
        $this->assertDatabaseMissing('students', ['id' => $student->id, 'standard_id' => $class3->id]);

        // CASE B: Moving student from Class 3 to Class 4 via Admin User Update
        // Re-enroll student in Class 3 and Teacher's group
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $class3->id]);
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $teacherGroup->id]);
        Student::where('id', $student->id)->update(['standard_id' => $class3->id]);

        $this->assertDatabaseHas('student_standards', ['student_id' => $student->id, 'standard_id' => $teacherGroup->id]);

        // Admin moves student to Class 4
        $this->actingAs($admin)->put("/admin/users/{$student->id}", [
            'name' => $student->name,
            'email' => $student->email,
            'type' => 2,
            'standard_id' => $class4->id,
            'mobile' => '9876543210',
            'address' => 'Sample Address',
        ])->assertRedirect()->assertSessionHasNoErrors();

        // Student is now in Class 4, but REMOVED from Class 3 and REMOVED from Teacher's custom group!
        $this->assertDatabaseHas('student_standards', ['student_id' => $student->id, 'standard_id' => $class4->id]);
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $class3->id]);
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $teacherGroup->id]);
        $this->assertDatabaseHas('students', ['id' => $student->id, 'standard_id' => $class4->id]);

        // CASE C: Admin unassigns student via bulk unassign on Class 4
        // Suppose another teacher of Class 4 had a custom group
        $teacher4 = User::factory()->create(['name' => 'Class 4 Teacher']);
        UserProfile::create(['user_id' => $teacher4->id, 'type' => 1]);
        $teacher4->standards()->attach([$class4->id]);

        $teacher4Group = Standard::create([
            'name' => 'Class 4 Science Club',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher4->id,
        ]);
        $teacher4->standards()->attach([$teacher4Group->id]);

        $this->actingAs($teacher4)->post("/standards/{$teacher4Group->id}/assign-students", [
            'student_ids' => [$student->id],
            '_assign_mode' => 'bulk',
        ])->assertRedirect()->assertSessionHasNoErrors();

        $this->assertDatabaseHas('student_standards', ['student_id' => $student->id, 'standard_id' => $teacher4Group->id]);

        // Admin unassigns student from Class 4 via bulk assign (student omitted)
        $this->actingAs($admin)->post("/standards/{$class4->id}/assign-students", [
            'student_ids' => [],
            '_assign_mode' => 'bulk',
        ])->assertRedirect()->assertSessionHasNoErrors();

        // Student is removed from Class 4 AND ALSO removed from Teacher 4's custom group!
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $class4->id]);
        $this->assertDatabaseMissing('student_standards', ['student_id' => $student->id, 'standard_id' => $teacher4Group->id]);
    }

    public function test_clean_up_all_ineligible_custom_group_enrollments_removes_orphaned_students_and_updates_count_to_zero(): void
    {
        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $class7 = Standard::create(['name' => 'Class 7 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);
        $class9 = Standard::create(['name' => 'Class 9 CBSE', 'syllabus_id' => $syllabus->id, 'created_by' => $admin->id]);

        $teacher = User::factory()->create(['name' => 'Teacher Alpha']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);
        $teacher->standards()->attach([$class7->id]);

        $customGroup = Standard::create([
            'name' => 'Math Alpha Club',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);
        $teacher->standards()->attach([$customGroup->id]);

        $student = User::factory()->create(['name' => 'Orphan Test Student']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);
        Student::create(['id' => $student->id, 'name' => $student->name, 'standard_id' => $class7->id]);
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $class7->id]);
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $customGroup->id]);

        // Student is currently enrolled in custom group (1/100)
        $this->assertEquals(1, $customGroup->fresh()->students()->count());

        // Now simulate student moved directly to Class 9 (not taught by teacher)
        DB::table('student_standards')->where('student_id', $student->id)->where('standard_id', $class7->id)->delete();
        DB::table('student_standards')->insert(['student_id' => $student->id, 'standard_id' => $class9->id]);
        Student::where('id', $student->id)->update(['standard_id' => $class9->id]);

        // Before viewing the page, student_standards still had orphaned row for customGroup
        $this->assertDatabaseHas('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $customGroup->id,
        ]);

        // Visiting standards index triggers automatic cleanup of ineligible custom group enrollments
        $response = $this->actingAs($teacher)->get('/standards');
        $response->assertStatus(200);

        // Orphaned student is automatically purged from custom group!
        $this->assertDatabaseMissing('student_standards', [
            'student_id' => $student->id,
            'standard_id' => $customGroup->id,
        ]);

        // Custom group count is now 0/100, not 1/100!
        $this->assertEquals(0, $customGroup->fresh()->students()->count());
        $response->assertSee('0/100 Students');
        $response->assertDontSee('1/100 Students');
    }
}

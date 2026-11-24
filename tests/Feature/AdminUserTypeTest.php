<?php

namespace Tests\Feature;

use App\Models\School;
use App\Models\Standard;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;

class AdminUserTypeTest extends TestCase
{
    use DatabaseTransactions;

    public function test_admin_can_create_user_with_teacher_type(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::create([
            'user_id' => $admin->id,
            'name' => $admin->name,
            'type' => 0, // Admin
        ]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General']);
        $standard = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);

        $response = $this->actingAs($admin)->post('/admin/users', [
            'name' => 'Jane Teacher',
            'email' => 'teacher@example.com',
            'password' => 'password123',
            'mobile' => '1234567890',
            'address' => '123 School St',
            'type' => 1, // Teacher
            'status' => 1,
            'standards' => [$standard->id],
        ]);

        $response->assertRedirect('/dashboard');

        $user = User::where('email', 'teacher@example.com')->first();
        $this->assertNotNull($user);

        $this->assertDatabaseHas('user_profiles', [
            'user_id' => $user->id,
            'type' => 1,
        ]);

        $this->assertDatabaseHas('teacher_standards', [
            'user_id' => $user->id,
            'standard_id' => $standard->id,
        ]);

        $this->assertDatabaseMissing('students', [
            'id' => $user->id,
        ]);
    }

    public function test_admin_can_create_user_with_student_type_populating_students_table(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::create([
            'user_id' => $admin->id,
            'name' => $admin->name,
            'type' => 0, // Admin
        ]);

        $syllabus = Syllabus::firstOrCreate(['name' => 'General']);
        $standard = Standard::firstOrCreate(['name' => '12th Standard', 'syllabus_id' => $syllabus->id]);

        $response = $this->actingAs($admin)->post('/admin/users', [
            'name' => 'Sam Student',
            'email' => 'student@example.com',
            'password' => 'password123',
            'mobile' => '9876543210',
            'address' => '456 Student Ave',
            'type' => 2, // Student
            'status' => 1,
            'standard_id' => $standard->id,
        ]);

        $response->assertRedirect('/dashboard');

        $user = User::where('email', 'student@example.com')->first();
        $this->assertNotNull($user);

        // Check user_profiles.type = 2
        $this->assertDatabaseHas('user_profiles', [
            'user_id' => $user->id,
            'type' => 2,
        ]);

        // Check students table entry: id = user id, name = user name, standard_id = selected class id
        $this->assertDatabaseHas('students', [
            'id' => $user->id,
            'name' => 'Sam Student',
            'standard_id' => $standard->id,
        ]);

        // Assert no entries in teacher_standards for student
        $this->assertDatabaseMissing('teacher_standards', [
            'user_id' => $user->id,
        ]);
    }

    public function test_admin_can_create_user_with_administrator_type(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::create([
            'user_id' => $admin->id,
            'name' => $admin->name,
            'type' => 3, // Administrator
        ]);

        $response = $this->actingAs($admin)->post('/admin/users', [
            'name' => 'Alex Admin',
            'email' => 'alexadmin@example.com',
            'password' => 'password123',
            'mobile' => '5556667777',
            'address' => '789 Admin HQ',
            'type' => 3, // Administrator
            'status' => 1,
        ]);

        $response->assertRedirect('/dashboard');

        $user = User::where('email', 'alexadmin@example.com')->first();
        $this->assertNotNull($user);

        $this->assertDatabaseHas('user_profiles', [
            'user_id' => $user->id,
            'type' => 3,
        ]);

        $this->assertTrue($user->isAdmin());
    }

    public function test_user_type_cannot_be_edited_on_update(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);

        $studentUser = User::factory()->create(['email' => 'existingstudent@example.com']);
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Existing Student',
            'type' => 2, // Student
            'mobile' => '1112223333',
            'address' => 'Some Address',
        ]);

        // Attempt to update user with type = 1
        $response = $this->actingAs($admin)->put('/admin/users/'.$studentUser->id, [
            'name' => 'Updated Student Name',
            'email' => 'existingstudent@example.com',
            'mobile' => '1112223333',
            'address' => 'Some Address',
            'type' => 1, // Trying to change to Teacher
        ]);

        $response->assertRedirect('/dashboard');

        // Type should remain 2 (Student)
        $this->assertDatabaseHas('user_profiles', [
            'user_id' => $studentUser->id,
            'type' => 2,
        ]);
    }

    public function test_student_sees_student_dashboard(): void
    {
        $studentUser = User::factory()->create(['email' => 'studentview@example.com']);
        UserProfile::create([
            'user_id' => $studentUser->id,
            'name' => 'Student Dashboard View User',
            'type' => 2, // Student
            'mobile' => '1112223333',
            'address' => 'Student Address',
        ]);

        $response = $this->actingAs($studentUser)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Student Dashboard');
        $response->assertSee('My Assigned Exams');
        $response->assertDontSee('User Management & Directory');
    }

    public function test_admin_can_change_password(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('oldpassword123'),
        ]);
        $admin->update(['password' => bcrypt('oldpassword123')]);

        UserProfile::updateOrCreate(
            ['user_id' => $admin->id],
            ['name' => $admin->name, 'type' => 0]
        );

        $response = $this->actingAs($admin)->post('/admin/change-password', [
            'current_password' => 'oldpassword123',
            'password' => 'newsecretpassword',
            'password_confirmation' => 'newsecretpassword',
        ]);

        $response->assertRedirect('/dashboard');
        $response->assertSessionHas('status', 'Admin password changed successfully!');

        $admin->refresh();
        $this->assertTrue(Hash::check('newsecretpassword', $admin->password));
    }

    public function test_admin_can_filter_users_by_role_and_keyword(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::updateOrCreate(
            ['user_id' => $admin->id],
            ['name' => $admin->name, 'type' => 3]
        );

        $teacher = User::factory()->create(['name' => 'UniqueTeacherName', 'email' => 'uniqueteacher@example.com']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1, 'mobile' => '111', 'address' => 'Addr']);

        $student = User::factory()->create(['name' => 'UniqueStudentName', 'email' => 'uniquestudent@example.com']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2, 'mobile' => '222', 'address' => 'Addr']);

        // Filter by role = 1 (Teacher)
        $response = $this->actingAs($admin)->get('/dashboard?role=1');
        $response->assertStatus(200);
        $response->assertSee('UniqueTeacherName');
        $response->assertDontSee('UniqueStudentName');

        // Filter by role = 2 (Student)
        $response = $this->actingAs($admin)->get('/dashboard?role=2');
        $response->assertStatus(200);
        $response->assertSee('UniqueStudentName');
        $response->assertDontSee('UniqueTeacherName');

        // Filter by keyword search
        $response = $this->actingAs($admin)->get('/dashboard?admin_search=UniqueTeacherName');
        $response->assertStatus(200);
        $response->assertSee('UniqueTeacherName');
        $response->assertDontSee('UniqueStudentName');
    }

    public function test_admin_can_create_and_edit_user_with_school_selection(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::updateOrCreate(
            ['user_id' => $admin->id],
            ['name' => $admin->name, 'type' => 3]
        );

        $school = School::firstOrCreate(
            ['name' => 'Kendriya Vidyalaya'],
            ['address' => 'Main Rd', 'country' => 'India']
        );

        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '7th Standard', 'syllabus_id' => $syllabus->id]);

        // Create student with school selected
        $response = $this->actingAs($admin)->post('/admin/users', [
            'name' => 'School Test Student',
            'email' => 'schoolstudent@example.com',
            'password' => 'password123',
            'mobile' => '9876543210',
            'address' => 'Student House',
            'type' => 2, // Student
            'school' => $school->name,
            'school_id' => $school->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);
        $response->assertRedirect('/dashboard');

        $user = User::where('email', 'schoolstudent@example.com')->first();
        $this->assertNotNull($user);
        $this->assertEquals($school->name, $user->profile->school);
        $this->assertEquals($school->id, $user->profile->school_id);

        // Edit user with updated school
        $newSchool = School::firstOrCreate(
            ['name' => 'Model High School'],
            ['address' => 'Second Ave', 'country' => 'India']
        );

        $editResponse = $this->actingAs($admin)->put("/admin/users/{$user->id}", [
            'name' => 'School Test Student Updated',
            'email' => 'schoolstudent@example.com',
            'mobile' => '9876543210',
            'address' => 'Student House',
            'school' => $newSchool->name,
            'school_id' => $newSchool->id,
            'standard_id' => $standard->id,
            'status' => 1,
        ]);
        $editResponse->assertRedirect('/dashboard');

        $user->refresh();
        $this->assertEquals($newSchool->name, $user->profile->school);
        $this->assertEquals($newSchool->id, $user->profile->school_id);
    }

    public function test_admin_can_search_and_filter_users_by_school(): void
    {
        $admin = User::firstOrCreate(['email' => 'admin@example.com'], [
            'name' => 'Admin User',
            'password' => bcrypt('password'),
        ]);
        UserProfile::updateOrCreate(
            ['user_id' => $admin->id],
            ['name' => $admin->name, 'type' => 3]
        );

        $schoolA = School::firstOrCreate(
            ['name' => 'Alpha Public School'],
            ['address' => 'Alpha St', 'country' => 'India']
        );
        $schoolB = School::firstOrCreate(
            ['name' => 'Beta Model Academy'],
            ['address' => 'Beta Ave', 'country' => 'India']
        );

        $userA = User::factory()->create(['name' => 'User From Alpha', 'email' => 'alphauser@example.com']);
        UserProfile::create([
            'user_id' => $userA->id,
            'name' => 'User From Alpha',
            'type' => 2,
            'school' => $schoolA->name,
            'school_id' => $schoolA->id,
        ]);

        $userB = User::factory()->create(['name' => 'User From Beta', 'email' => 'betauser@example.com']);
        UserProfile::create([
            'user_id' => $userB->id,
            'name' => 'User From Beta',
            'type' => 2,
            'school' => $schoolB->name,
            'school_id' => $schoolB->id,
        ]);

        // Filter by school_id for school A
        $responseA = $this->actingAs($admin)->get('/dashboard?school_id='.$schoolA->id);
        $responseA->assertStatus(200);
        $responseA->assertSee('User From Alpha');
        $responseA->assertDontSee('User From Beta');

        // Filter by school_id for school B
        $responseB = $this->actingAs($admin)->get('/dashboard?school_id='.$schoolB->id);
        $responseB->assertStatus(200);
        $responseB->assertSee('User From Beta');
        $responseB->assertDontSee('User From Alpha');

        // Search by school name in admin_search
        $responseSearch = $this->actingAs($admin)->get('/dashboard?admin_search=Alpha+Public');
        $responseSearch->assertStatus(200);
        $responseSearch->assertSee('User From Alpha');
        $responseSearch->assertDontSee('User From Beta');
    }
}

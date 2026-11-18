<?php

namespace Tests\Feature;

use App\Models\Standard;
use App\Models\Student;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class StudentsInMyClassesTest extends TestCase
{
    use RefreshDatabase;

    public function test_teacher_sees_own_custom_groups_and_assigned_groups_only_in_students_in_my_classes(): void
    {
        $syllabus = Syllabus::create(['name' => 'NCERT']);

        // Admin creates Gr 01, Gr 02, and another unassigned group
        $admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create(['user_id' => $admin->id, 'type' => 3]);

        $gr01 = Standard::create([
            'name' => 'Gr 01',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $gr02 = Standard::create([
            'name' => 'Gr 02',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        $unassignedAdminGrp = Standard::create([
            'name' => 'unassigned_admin_grp',
            'syllabus_id' => $syllabus->id,
            'created_by' => $admin->id,
        ]);

        // Teacher Amit creates amt_custom_grp and is assigned to Gr 01 and Gr 02
        $teacher = User::factory()->create(['name' => 'Teacher Amit']);
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);
        $teacher->standards()->attach([$gr01->id, $gr02->id]);

        $amtCustomGrp = Standard::create([
            'name' => 'amt_custom_grp',
            'syllabus_id' => $syllabus->id,
            'created_by' => $teacher->id,
        ]);

        // Another teacher creates a private group
        $otherTeacher = User::factory()->create();
        UserProfile::create(['user_id' => $otherTeacher->id, 'type' => 1]);

        $otherTeacherGrp = Standard::create([
            'name' => 'other_teacher_private_grp',
            'syllabus_id' => $syllabus->id,
            'created_by' => $otherTeacher->id,
        ]);

        // Students in Gr 01 and Gr 02
        $student1 = User::factory()->create(['name' => 'Student In Gr 01']);
        UserProfile::create(['user_id' => $student1->id, 'type' => 2]);
        Student::create(['id' => $student1->id, 'name' => 'Student In Gr 01', 'standard_id' => $gr01->id]);

        $student2 = User::factory()->create(['name' => 'Student In Gr 02']);
        UserProfile::create(['user_id' => $student2->id, 'type' => 2]);
        Student::create(['id' => $student2->id, 'name' => 'Student In Gr 02', 'standard_id' => $gr02->id]);

        // Access Students in My Classes
        $response = $this->actingAs($teacher)->get('/students');

        $response->assertStatus(200);
        // Teacher should see his own assigned groups (Gr 01, Gr 02) and his created group (amt_custom_grp)
        $response->assertSee('Gr 01');
        $response->assertSee('Gr 02');
        $response->assertSee('amt_custom_grp');

        // Teacher should NOT see groups created by others that are not assigned to him
        $response->assertDontSee('other_teacher_private_grp');
        $response->assertDontSee('unassigned_admin_grp');

        // Teacher should see students enrolled in his classes
        $response->assertSee('Student In Gr 01');
        $response->assertSee('Student In Gr 02');

        // Teacher can filter by standard_id for Gr 01
        $filterResponse = $this->actingAs($teacher)->get('/students?standard_id='.$gr01->id);
        $filterResponse->assertStatus(200);
        $filterResponse->assertSee('Student In Gr 01');
        $filterResponse->assertDontSee('Student In Gr 02');
    }
}

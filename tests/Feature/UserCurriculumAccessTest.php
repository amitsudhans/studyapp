<?php

namespace Tests\Feature;

use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class UserCurriculumAccessTest extends TestCase
{
    use DatabaseTransactions;

    private function createUserWithRole(int $type, string $email, string $name): User
    {
        $user = User::factory()->create([
            'name' => $name,
            'email' => $email,
            'status' => 1,
        ]);

        UserProfile::create([
            'user_id' => $user->id,
            'name' => $name,
            'mobile' => '9876543210',
            'address' => 'Campus Road',
            'type' => $type,
            'designation' => $type === 3 ? 'Administrator' : null,
        ]);

        return $user;
    }

    public function test_admin_dashboard_shows_separate_edit_curriculum_option_for_teacher_student_and_admin(): void
    {
        $admin = $this->createUserWithRole(3, 'admin.curr@example.com', 'Admin One');
        $teacher = $this->createUserWithRole(1, 'teacher.curr@example.com', 'Teacher One');
        $student = $this->createUserWithRole(2, 'student.curr@example.com', 'Student One');

        $response = $this->actingAs($admin)->get('/dashboard');

        $response->assertStatus(200);
        $response->assertSee('Edit Curriculum');
        $response->assertSee('editCurriculumModal');
        $response->assertSee('Social Science');
        $response->assertSee('ncert|social-science|class12');
        $response->assertSee('cbse|social-science|class1');
        $response->assertSee('openEditCurriculumModal');
    }

    public function test_non_admin_cannot_update_another_users_curriculum(): void
    {
        $teacher = $this->createUserWithRole(1, 'teacher.auth@example.com', 'Teacher Auth');
        $student = $this->createUserWithRole(2, 'student.auth@example.com', 'Student Auth');

        $this->actingAs($teacher)->put("/admin/users/{$student->id}/curriculum", [
            'mode' => 'restricted',
            'items' => ['ncert|mathematics|class8'],
        ])->assertStatus(403);

        $this->actingAs($student)->put("/admin/users/{$teacher->id}/curriculum", [
            'mode' => 'restricted',
            'items' => ['ncert|mathematics|class8'],
        ])->assertStatus(403);
    }

    public function test_admin_can_enable_and_disable_curriculum_for_teacher_student_and_admin(): void
    {
        $admin = $this->createUserWithRole(3, 'admin.manage@example.com', 'Admin Manager');
        $teacher = $this->createUserWithRole(1, 'teacher.manage@example.com', 'Teacher Target');
        $student = $this->createUserWithRole(2, 'student.manage@example.com', 'Student Target');

        foreach ([$teacher, $student, $admin] as $targetUser) {
            $response = $this->actingAs($admin)->put("/admin/users/{$targetUser->id}/curriculum", [
                'mode' => 'restricted',
                'items' => [
                    'ncert|mathematics|class8',
                    'cbse|social-science|class10',
                ],
            ]);

            $response->assertRedirect('/dashboard');

            $this->assertDatabaseHas('users', [
                'id' => $targetUser->id,
                'curriculum_restricted' => 1,
            ]);

            $this->assertDatabaseHas('user_curricula', [
                'user_id' => $targetUser->id,
                'syllabus' => 'ncert',
                'subject' => 'mathematics',
                'class_key' => 'class8',
                'is_enabled' => 1,
            ]);

            $this->assertDatabaseHas('user_curricula', [
                'user_id' => $targetUser->id,
                'syllabus' => 'cbse',
                'subject' => 'social-science',
                'class_key' => 'class10',
                'is_enabled' => 1,
            ]);
        }
    }

    public function test_restricted_user_only_sees_enabled_curriculum_even_when_requesting_disabled_params(): void
    {
        $admin = $this->createUserWithRole(3, 'admin.filter@example.com', 'Admin Filter');
        $student = $this->createUserWithRole(2, 'student.filter@example.com', 'Student Filter');

        $this->actingAs($admin)->put("/admin/users/{$student->id}/curriculum", [
            'mode' => 'restricted',
            'items' => [
                'ncert|mathematics|class8',
            ],
        ])->assertRedirect('/dashboard');

        // Default /multimedia automatically resolves to enabled NCERT -> Mathematics -> Class 8
        $defaultView = $this->actingAs($student)->get('/multimedia');
        $defaultView->assertStatus(200);
        $defaultView->assertSee('Algebra Play');
        $defaultView->assertDontSee('SCERT Kerala');
        $defaultView->assertDontSee('Social Science');
        $defaultView->assertDontSee('Real Numbers');

        // Attempting to craft disabled syllabus/subject/class query parameters does not expose disabled chapters
        $forcedView = $this->actingAs($student)->get('/multimedia?syllabus=cbse&subject=science&class=class10');
        $forcedView->assertStatus(200);
        $forcedView->assertSee('Algebra Play');
        $forcedView->assertDontSee('Chemical Reactions');
    }

    public function test_user_with_all_curriculum_disabled_sees_empty_access_message(): void
    {
        $admin = $this->createUserWithRole(3, 'admin.zero@example.com', 'Admin Zero');
        $teacher = $this->createUserWithRole(1, 'teacher.zero@example.com', 'Teacher Zero');

        $this->actingAs($admin)->put("/admin/users/{$teacher->id}/curriculum", [
            'mode' => 'restricted',
            'items' => [],
        ])->assertRedirect('/dashboard');

        $response = $this->actingAs($teacher)->get('/multimedia');
        $response->assertStatus(200);
        $response->assertSee('No Curriculum Enabled for Your Account');
        $response->assertDontSee('Real Numbers');
    }

    public function test_admin_can_restore_unrestricted_curriculum_access(): void
    {
        $admin = $this->createUserWithRole(3, 'admin.restore@example.com', 'Admin Restore');
        $student = $this->createUserWithRole(2, 'student.restore@example.com', 'Student Restore');

        $this->actingAs($admin)->put("/admin/users/{$student->id}/curriculum", [
            'mode' => 'restricted',
            'items' => [],
        ])->assertRedirect('/dashboard');

        $this->actingAs($admin)->put("/admin/users/{$student->id}/curriculum", [
            'mode' => 'unrestricted',
        ])->assertRedirect('/dashboard');

        $this->assertDatabaseHas('users', [
            'id' => $student->id,
            'curriculum_restricted' => 0,
        ]);

        $response = $this->actingAs($student)->get('/multimedia?syllabus=ncert&subject=mathematics&class=class10');
        $response->assertStatus(200);
        $response->assertSee('Real Numbers');
        $response->assertSee('Social Science');
    }
}

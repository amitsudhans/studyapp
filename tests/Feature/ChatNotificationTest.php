<?php

namespace Tests\Feature;

use App\Models\ChatMessage;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class ChatNotificationTest extends TestCase
{
    use DatabaseTransactions;

    public function test_teacher_can_fetch_chat_contacts(): void
    {
        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $student = User::factory()->create(['name' => 'John Student']);
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $response = $this->actingAs($teacher)->getJson(route('chat.contacts'));

        $response->assertOk()
            ->assertJsonFragment([
                'id' => $student->id,
                'name' => 'John Student',
                'role' => 'Student',
            ]);
    }

    public function test_teacher_can_send_chat_message_to_student(): void
    {
        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $response = $this->actingAs($teacher)->postJson(route('chat.send'), [
            'receiver_id' => $student->id,
            'message' => 'Hello student, please prepare for your upcoming exam.',
        ]);

        $response->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonPath('message.message', 'Hello student, please prepare for your upcoming exam.');

        $this->assertDatabaseHas('chat_messages', [
            'sender_id' => $teacher->id,
            'receiver_id' => $student->id,
            'message' => 'Hello student, please prepare for your upcoming exam.',
            'is_read' => false,
        ]);
    }

    public function test_student_receives_unread_notification(): void
    {
        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        ChatMessage::create([
            'sender_id' => $teacher->id,
            'receiver_id' => $student->id,
            'message' => 'New assignment details inside.',
            'is_read' => false,
        ]);

        $response = $this->actingAs($student)->getJson(route('chat.notifications'));

        $response->assertOk()
            ->assertJsonPath('unread_count', 1)
            ->assertJsonFragment([
                'message' => 'New assignment details inside.',
            ]);
    }

    public function test_student_can_fetch_messages_and_mark_them_as_read(): void
    {
        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $message = ChatMessage::create([
            'sender_id' => $teacher->id,
            'receiver_id' => $student->id,
            'message' => 'Please submit your answers.',
            'is_read' => false,
        ]);

        $response = $this->actingAs($student)->getJson(route('chat.messages', $teacher));

        $response->assertOk()
            ->assertJsonFragment([
                'message' => 'Please submit your answers.',
                'is_me' => false,
            ]);

        $this->assertDatabaseHas('chat_messages', [
            'id' => $message->id,
            'is_read' => true,
        ]);
    }

    public function test_student_can_reply_to_teacher(): void
    {
        $teacher = User::factory()->create();
        UserProfile::create(['user_id' => $teacher->id, 'type' => 1]);

        $student = User::factory()->create();
        UserProfile::create(['user_id' => $student->id, 'type' => 2]);

        $response = $this->actingAs($student)->postJson(route('chat.send'), [
            'receiver_id' => $teacher->id,
            'message' => 'Thank you teacher, I have completed the study material.',
        ]);

        $response->assertOk()
            ->assertJsonPath('success', true);

        $this->assertDatabaseHas('chat_messages', [
            'sender_id' => $student->id,
            'receiver_id' => $teacher->id,
            'message' => 'Thank you teacher, I have completed the study material.',
            'is_read' => false,
        ]);
    }

    public function test_guest_cannot_send_message(): void
    {
        $user = User::factory()->create();

        $response = $this->postJson(route('chat.send'), [
            'receiver_id' => $user->id,
            'message' => 'Unauthorized message',
        ]);

        $response->assertUnauthorized();
    }
}

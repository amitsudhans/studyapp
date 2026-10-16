<?php

namespace Tests\Feature;

use App\Models\Chapter;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class StandardChapterTopicCrudTest extends TestCase
{
    use RefreshDatabase;

    private User $admin;

    private Standard $standard;

    private Subject $subject;

    protected function setUp(): void
    {
        parent::setUp();

        $syllabus = Syllabus::create(['name' => 'CBSE']);

        $this->admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create([
            'user_id' => $this->admin->id,
            'mobile' => '9999999999',
            'address' => 'Admin HQ',
            'type' => 3, // Administrator
            'designation' => 'Administrator',
        ]);

        $this->standard = Standard::create([
            'name' => 'Class 10 - Science & Math',
            'syllabus_id' => $syllabus->id,
            'created_by' => $this->admin->id,
        ]);

        $this->subject = Subject::create([
            'name' => 'Mathematics',
            'syllabus_id' => $syllabus->id,
        ]);
    }

    public function test_admin_can_create_chapter_inside_standard(): void
    {
        $response = $this->actingAs($this->admin)->postJson("/standards/{$this->standard->id}/chapters", [
            'name' => 'Linear Equations',
            'subject_id' => $this->subject->id,
        ]);

        $response->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonPath('chapter.name', 'Linear Equations')
            ->assertJsonPath('chapter.standard_id', $this->standard->id)
            ->assertJsonPath('chapter.subject_id', $this->subject->id);

        $this->assertDatabaseHas('chapters', [
            'name' => 'Linear Equations',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
        ]);
    }

    public function test_admin_can_update_and_delete_chapter(): void
    {
        $chapter = Chapter::create([
            'name' => 'Algebra Intro',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
            'syllabus_id' => $this->standard->syllabus_id,
        ]);

        // Update
        $updateResponse = $this->actingAs($this->admin)->putJson("/chapters/{$chapter->id}", [
            'name' => 'Algebra Advanced',
            'subject_id' => $this->subject->id,
        ]);

        $updateResponse->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonPath('chapter.name', 'Algebra Advanced');

        $this->assertDatabaseHas('chapters', [
            'id' => $chapter->id,
            'name' => 'Algebra Advanced',
        ]);

        // Delete
        $deleteResponse = $this->actingAs($this->admin)->deleteJson("/chapters/{$chapter->id}");

        $deleteResponse->assertOk()->assertJsonPath('success', true);
        $this->assertDatabaseMissing('chapters', ['id' => $chapter->id]);
    }

    public function test_admin_can_create_topic_inside_chapter(): void
    {
        $chapter = Chapter::create([
            'name' => 'Geometry',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
            'syllabus_id' => $this->standard->syllabus_id,
        ]);

        $response = $this->actingAs($this->admin)->postJson("/chapters/{$chapter->id}/topics", [
            'name' => 'Circles & Theorems',
        ]);

        $response->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonPath('topic.name', 'Circles & Theorems')
            ->assertJsonPath('topic.chapter_id', $chapter->id);

        $this->assertDatabaseHas('topics', [
            'name' => 'Circles & Theorems',
            'chapter_id' => $chapter->id,
        ]);
    }

    public function test_admin_can_update_and_delete_topic(): void
    {
        $chapter = Chapter::create([
            'name' => 'Statistics',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
            'syllabus_id' => $this->standard->syllabus_id,
        ]);

        $topic = Topic::create([
            'name' => 'Mean & Median',
            'chapter_id' => $chapter->id,
        ]);

        // Update
        $updateResponse = $this->actingAs($this->admin)->putJson("/topics/{$topic->id}", [
            'name' => 'Mean, Median, & Mode',
        ]);

        $updateResponse->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonPath('topic.name', 'Mean, Median, & Mode');

        $this->assertDatabaseHas('topics', [
            'id' => $topic->id,
            'name' => 'Mean, Median, & Mode',
        ]);

        // Delete
        $deleteResponse = $this->actingAs($this->admin)->deleteJson("/topics/{$topic->id}");

        $deleteResponse->assertOk()->assertJsonPath('success', true);
        $this->assertDatabaseMissing('topics', ['id' => $topic->id]);
    }

    public function test_deleting_chapter_cascades_to_its_topics(): void
    {
        $chapter = Chapter::create([
            'name' => 'Probability',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
            'syllabus_id' => $this->standard->syllabus_id,
        ]);

        $topic1 = Topic::create(['name' => 'Coin Tosses', 'chapter_id' => $chapter->id]);
        $topic2 = Topic::create(['name' => 'Dice Rolls', 'chapter_id' => $chapter->id]);

        $response = $this->actingAs($this->admin)->deleteJson("/chapters/{$chapter->id}");
        $response->assertOk();

        $this->assertDatabaseMissing('chapters', ['id' => $chapter->id]);
        $this->assertDatabaseMissing('topics', ['id' => $topic1->id]);
        $this->assertDatabaseMissing('topics', ['id' => $topic2->id]);
    }

    public function test_fetching_chapters_for_standard_returns_associated_topics(): void
    {
        $chapter = Chapter::create([
            'name' => 'Trigonometry',
            'standard_id' => $this->standard->id,
            'subject_id' => $this->subject->id,
            'syllabus_id' => $this->standard->syllabus_id,
        ]);

        Topic::create(['name' => 'Sine and Cosine', 'chapter_id' => $chapter->id]);
        Topic::create(['name' => 'Tangent and Cotangent', 'chapter_id' => $chapter->id]);

        $response = $this->actingAs($this->admin)->getJson("/standards/{$this->standard->id}/chapters");

        $response->assertOk()
            ->assertJsonPath('success', true)
            ->assertJsonCount(1, 'chapters')
            ->assertJsonPath('chapters.0.name', 'Trigonometry')
            ->assertJsonCount(2, 'chapters.0.topics');
    }
}

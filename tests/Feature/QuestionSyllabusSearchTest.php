<?php

namespace Tests\Feature;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class QuestionSyllabusSearchTest extends TestCase
{
    use RefreshDatabase;

    private User $admin;

    private Syllabus $cbseSyllabus;

    private Syllabus $scertSyllabus;

    private Question $cbseQuestion;

    private Question $scertQuestion;

    protected function setUp(): void
    {
        parent::setUp();

        $this->admin = User::factory()->create(['email' => 'admin@example.com']);
        UserProfile::create([
            'user_id' => $this->admin->id,
            'mobile' => '9999999999',
            'address' => 'HQ',
            'type' => 3, // Administrator
            'designation' => 'Administrator',
        ]);

        $this->cbseSyllabus = Syllabus::create(['name' => 'CBSE']);
        $this->scertSyllabus = Syllabus::create(['name' => 'SCERT Kerala']);

        $cbseStandard = Standard::create([
            'name' => 'Class 9 CBSE',
            'syllabus_id' => $this->cbseSyllabus->id,
            'created_by' => $this->admin->id,
        ]);

        $scertStandard = Standard::create([
            'name' => 'Class 9 SCERT',
            'syllabus_id' => $this->scertSyllabus->id,
            'created_by' => $this->admin->id,
        ]);

        $cbseSubject = Subject::create([
            'name' => 'Mathematics',
            'syllabus_id' => $this->cbseSyllabus->id,
        ]);

        $scertSubject = Subject::create([
            'name' => 'Mathematics SCERT',
            'syllabus_id' => $this->scertSyllabus->id,
        ]);

        $cbseChapter = Chapter::create([
            'name' => 'Number System',
            'standard_id' => $cbseStandard->id,
            'subject_id' => $cbseSubject->id,
            'syllabus_id' => $this->cbseSyllabus->id,
        ]);

        $scertChapter = Chapter::create([
            'name' => 'Real Numbers',
            'standard_id' => $scertStandard->id,
            'subject_id' => $scertSubject->id,
            'syllabus_id' => $this->scertSyllabus->id,
        ]);

        $this->cbseQuestion = Question::create([
            'name' => 'What is an irrational number in CBSE curriculum?',
            'standard_id' => $cbseStandard->id,
            'subject_id' => $cbseSubject->id,
            'chapter_id' => $cbseChapter->id,
            'type' => 1,
            'created_by' => $this->admin->id,
            'marks' => 1,
            'status' => 1,
        ]);

        Answer::create([
            'question_id' => $this->cbseQuestion->id,
            'name' => 'Non-terminating non-repeating',
            'is_correct' => 1,
            'status' => 1,
        ]);

        $this->scertQuestion = Question::create([
            'name' => 'What is an arithmetic progression in SCERT curriculum?',
            'standard_id' => $scertStandard->id,
            'subject_id' => $scertSubject->id,
            'chapter_id' => $scertChapter->id,
            'type' => 1,
            'created_by' => $this->admin->id,
            'marks' => 1,
            'status' => 1,
        ]);

        Answer::create([
            'question_id' => $this->scertQuestion->id,
            'name' => 'Constant difference sequence',
            'is_correct' => 1,
            'status' => 1,
        ]);
    }

    public function test_question_index_displays_syllabus_filter(): void
    {
        $response = $this->actingAs($this->admin)->get('/questions');

        $response->assertOk()
            ->assertSee('Syllabus')
            ->assertSee('CBSE')
            ->assertSee('SCERT Kerala');
    }

    public function test_questions_can_be_filtered_by_syllabus_id(): void
    {
        $response = $this->actingAs($this->admin)->get('/questions?syllabus_id='.$this->cbseSyllabus->id);

        $response->assertOk()
            ->assertSee($this->cbseQuestion->name)
            ->assertDontSee($this->scertQuestion->name);

        $scertResponse = $this->actingAs($this->admin)->get('/questions?syllabus_id='.$this->scertSyllabus->id);

        $scertResponse->assertOk()
            ->assertSee($this->scertQuestion->name)
            ->assertDontSee($this->cbseQuestion->name);
    }

    public function test_questions_can_be_searched_by_syllabus_name(): void
    {
        $response = $this->actingAs($this->admin)->get('/questions?search=SCERT');

        $response->assertOk()
            ->assertSee($this->scertQuestion->name)
            ->assertDontSee($this->cbseQuestion->name);

        $cbseResponse = $this->actingAs($this->admin)->get('/questions?search=CBSE');

        $cbseResponse->assertOk()
            ->assertSee($this->cbseQuestion->name)
            ->assertDontSee($this->scertQuestion->name);
    }
}

<?php

namespace Tests\Feature;

use App\Models\Exam;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Syllabus;
use App\Models\User;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class ExamManagementTest extends TestCase
{
    use DatabaseTransactions;

    protected User $teacher;

    protected Standard $standard;

    protected function setUp(): void
    {
        parent::setUp();

        $this->teacher = User::factory()->create();
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $this->standard = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);
    }

    public function test_teachers_can_view_exams_page(): void
    {
        $response = $this->actingAs($this->teacher)->get('/exams');

        $response->assertStatus(200);
        $response->assertSee('Exams Management');
    }

    public function test_teachers_can_create_exam_with_name_and_add_questions_from_question_bank(): void
    {
        $q1 = Question::create([
            'name' => 'What is H2O?',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 5,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $q2 = Question::create([
            'name' => 'What is Speed of Light?',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 10,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $response = $this->actingAs($this->teacher)->post('/exams', [
            'name' => 'Physics & Chemistry Midterm',
            'type' => 1,
            'duration' => 60,
            'status' => 1,
            'question_ids' => [$q1->id, $q2->id],
        ]);

        $response->assertRedirect('/exams');

        $this->assertDatabaseHas('exams', [
            'name' => 'Physics & Chemistry Midterm',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'duration' => 60,
            'status' => 1,
            'total_mark' => 15,
        ]);

        $exam = Exam::where('name', 'Physics & Chemistry Midterm')->first();
        $this->assertNotNull($exam);

        $this->assertDatabaseHas('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q1->id,
            'status' => 1,
        ]);

        $this->assertDatabaseHas('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q2->id,
            'status' => 1,
        ]);
    }

    public function test_teachers_can_edit_exam_name_type_status_and_questions(): void
    {
        $q1 = Question::create([
            'name' => 'Question A',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 4,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $q2 = Question::create([
            'name' => 'Question B',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 6,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Old Exam Name',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 4,
        ]);

        $exam->questions()->attach($q1->id, ['status' => 1]);

        $response = $this->actingAs($this->teacher)->put('/exams/'.$exam->id, [
            'name' => 'Updated Exam Name',
            'type' => 2,
            'status' => 1,
            'question_ids' => [$q2->id],
        ]);

        $response->assertRedirect('/exams');

        $this->assertDatabaseHas('exams', [
            'id' => $exam->id,
            'name' => 'Updated Exam Name',
            'type' => 2,
            'total_mark' => 6,
        ]);

        $this->assertDatabaseMissing('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q1->id,
        ]);

        $this->assertDatabaseHas('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q2->id,
            'status' => 1,
        ]);
    }

    public function test_teachers_can_add_questions_to_existing_exam(): void
    {
        $exam = Exam::create([
            'name' => 'Final Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 0,
        ]);

        $q = Question::create([
            'name' => 'Question C',
            'standard_id' => $this->standard->id,
            'type' => 3,
            'marks' => 8,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $response = $this->actingAs($this->teacher)->post('/exams/'.$exam->id.'/questions', [
            'question_ids' => [$q->id],
        ]);

        $response->assertRedirect();

        $this->assertDatabaseHas('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q->id,
            'status' => 1,
        ]);

        $this->assertEquals(8, $exam->fresh()->total_mark);
    }

    public function test_teachers_can_remove_questions_from_exam_updating_exam_questions_table(): void
    {
        $q = Question::create([
            'name' => 'Question D',
            'standard_id' => $this->standard->id,
            'type' => 1,
            'marks' => 5,
            'created_by' => $this->teacher->id,
            'status' => 1,
        ]);

        $exam = Exam::create([
            'name' => 'Test Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 5,
        ]);

        $exam->questions()->attach($q->id, ['status' => 1]);

        $this->assertDatabaseHas('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q->id,
        ]);

        $response = $this->actingAs($this->teacher)->delete('/exams/'.$exam->id.'/questions/'.$q->id);

        $response->assertRedirect();

        $this->assertDatabaseMissing('exam_questions', [
            'exam_id' => $exam->id,
            'question_id' => $q->id,
        ]);

        $this->assertEquals(0, $exam->fresh()->total_mark);
    }

    public function test_teachers_can_delete_exam(): void
    {
        $exam = Exam::create([
            'name' => 'Temporary Exam',
            'created_by' => $this->teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 0,
        ]);

        $response = $this->actingAs($this->teacher)->delete('/exams/'.$exam->id);

        $response->assertRedirect('/exams');

        $this->assertDatabaseMissing('exams', [
            'id' => $exam->id,
        ]);
    }
}

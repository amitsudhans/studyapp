<?php

namespace Tests\Feature;

use App\Models\Answer;
use App\Models\Exam;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Student;
use App\Models\StudentExamDetail;
use App\Models\Syllabus;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Tests\TestCase;

class ExamLeaderboardTest extends TestCase
{
    use DatabaseTransactions;

    public function test_leaderboard_page_loads_and_ranks_students_correctly(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'Leaderboard Syllabus']);
        $standard = Standard::firstOrCreate(['name' => 'Grade 10', 'syllabus_id' => $syllabus->id]);

        $teacher = User::factory()->create();

        // Create an exam
        $exam = Exam::create([
            'name' => 'Physics Final Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 20,
        ]);

        // Question 1: 10 marks
        $q1 = Question::create([
            'name' => 'Speed of Light?',
            'type' => 1,
            'marks' => 10,
            'standard_id' => $standard->id,
            'created_by' => $teacher->id,
        ]);
        $q1CorrectAns = Answer::create(['question_id' => $q1->id, 'name' => '3x10^8 m/s', 'is_correct' => 1]);
        $q1WrongAns = Answer::create(['question_id' => $q1->id, 'name' => '100 m/s', 'is_correct' => 0]);

        // Question 2: 10 marks
        $q2 = Question::create([
            'name' => 'Unit of Force?',
            'type' => 1,
            'marks' => 10,
            'standard_id' => $standard->id,
            'created_by' => $teacher->id,
        ]);
        $q2CorrectAns = Answer::create(['question_id' => $q2->id, 'name' => 'Newton', 'is_correct' => 1]);
        $q2WrongAns = Answer::create(['question_id' => $q2->id, 'name' => 'Joule', 'is_correct' => 0]);

        $exam->questions()->attach([$q1->id => ['status' => 1], $q2->id => ['status' => 1]]);

        // Student A: High score (20/20)
        $userA = User::factory()->create(['name' => 'Alice HighScore']);
        UserProfile::create(['user_id' => $userA->id, 'name' => 'Alice HighScore', 'type' => 2]);
        $studentA = Student::create(['id' => $userA->id, 'name' => 'Alice HighScore', 'standard_id' => $standard->id]);

        StudentExamDetail::create([
            'student_id' => $studentA->id,
            'exam_id' => $exam->id,
            'question_id' => $q1->id,
            'student_written_ans_id' => $q1CorrectAns->id,
            'created_at' => now()->subMinutes(10),
        ]);
        StudentExamDetail::create([
            'student_id' => $studentA->id,
            'exam_id' => $exam->id,
            'question_id' => $q2->id,
            'student_written_ans_id' => $q2CorrectAns->id,
            'created_at' => now()->subMinutes(10),
        ]);

        // Student B: Average score (10/20)
        $userB = User::factory()->create(['name' => 'Bob MidScore']);
        UserProfile::create(['user_id' => $userB->id, 'name' => 'Bob MidScore', 'type' => 2]);
        $studentB = Student::create(['id' => $userB->id, 'name' => 'Bob MidScore', 'standard_id' => $standard->id]);

        StudentExamDetail::create([
            'student_id' => $studentB->id,
            'exam_id' => $exam->id,
            'question_id' => $q1->id,
            'student_written_ans_id' => $q1CorrectAns->id,
            'created_at' => now()->subMinutes(5),
        ]);
        StudentExamDetail::create([
            'student_id' => $studentB->id,
            'exam_id' => $exam->id,
            'question_id' => $q2->id,
            'student_written_ans_id' => $q2WrongAns->id,
            'created_at' => now()->subMinutes(5),
        ]);

        // View Leaderboard Web Page
        $response = $this->actingAs($teacher)->get("/exams/{$exam->id}/leaderboard");

        $response->assertStatus(200);
        $response->assertSee('Physics Final Exam');
        $response->assertSee('Official Exam Leaderboard');
        $response->assertSee('Alice HighScore');
        $response->assertSee('Bob MidScore');

        // View Leaderboard JSON Endpoint
        $jsonResponse = $this->actingAs($userA)
            ->getJson("/exams/{$exam->id}/leaderboard");

        $jsonResponse->assertStatus(200);
        $jsonResponse->assertJsonStructure([
            'exam' => ['id', 'name', 'total_mark', 'questions_count'],
            'summary' => ['total_submissions', 'highest_marks', 'average_marks', 'top_scorer'],
            'leaderboard' => [
                '*' => ['rank', 'student_id', 'student_name', 'obtained_marks', 'total_marks', 'percentage', 'submitted_at', 'is_current_user'],
            ],
        ]);

        $data = $jsonResponse->json();
        $this->assertEquals(2, $data['summary']['total_submissions']);
        $this->assertEquals('Alice HighScore', $data['summary']['top_scorer']);
        $this->assertEquals(20, $data['summary']['highest_marks']);
        $this->assertEquals(15, $data['summary']['average_marks']); // (20 + 10) / 2 = 15

        // Verify Rank 1 is Alice HighScore
        $this->assertEquals(1, $data['leaderboard'][0]['rank']);
        $this->assertEquals('Alice HighScore', $data['leaderboard'][0]['student_name']);
        $this->assertEquals(20, $data['leaderboard'][0]['obtained_marks']);
        $this->assertTrue($data['leaderboard'][0]['is_current_user']);

        // Verify Rank 2 is Bob MidScore
        $this->assertEquals(2, $data['leaderboard'][1]['rank']);
        $this->assertEquals('Bob MidScore', $data['leaderboard'][1]['student_name']);
        $this->assertEquals(10, $data['leaderboard'][1]['obtained_marks']);
        $this->assertFalse($data['leaderboard'][1]['is_current_user']);
    }

    public function test_leaderboard_handles_empty_submissions_gracefully(): void
    {
        $teacher = User::factory()->create();
        $exam = Exam::create([
            'name' => 'Empty Chemistry Exam',
            'created_by' => $teacher->id,
            'type' => 1,
            'status' => 1,
            'total_mark' => 50,
        ]);

        $response = $this->actingAs($teacher)->get("/exams/{$exam->id}/leaderboard");
        $response->assertStatus(200);
        $response->assertSee('No Exam Submissions Yet');

        $jsonResponse = $this->actingAs($teacher)->getJson("/exams/{$exam->id}/leaderboard");
        $jsonResponse->assertStatus(200);
        $jsonResponse->assertJson([
            'summary' => [
                'total_submissions' => 0,
                'highest_marks' => 0,
                'average_marks' => 0,
                'top_scorer' => 'N/A',
            ],
            'leaderboard' => [],
        ]);
    }
}

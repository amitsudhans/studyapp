<?php

namespace Database\Factories;

use App\Models\Answer;
use App\Models\Exam;
use App\Models\Question;
use App\Models\Student;
use App\Models\StudentExamDetail;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<StudentExamDetail>
 */
class StudentExamDetailFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'student_id' => Student::factory(),
            'exam_id' => Exam::factory(),
            'question_id' => Question::factory(),
            'student_written_ans_id' => Answer::factory(),
        ];
    }
}

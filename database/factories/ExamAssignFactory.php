<?php

namespace Database\Factories;

use App\Models\Exam;
use App\Models\ExamAssign;
use App\Models\Standard;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<ExamAssign>
 */
class ExamAssignFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'exam_id' => Exam::factory(),
            'standard_id' => Standard::factory(),
            'status' => 1,
        ];
    }
}

<?php

namespace Database\Factories;

use App\Models\Standard;
use App\Models\Student;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Facades\Hash;

/**
 * @extends Factory<Student>
 */
class StudentFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'standard_id' => fn () => Standard::query()->first()->id ?? Standard::create(['name' => 'Class 1', 'syllabus_id' => 1])->id,
        ];
    }

    /**
     * Configure the model factory.
     */
    public function configure(): static
    {
        return $this->afterMaking(function (Student $student) {
            if (! $student->id) {
                $user = User::create([
                    'name' => $student->name ?: fake()->name(),
                    'email' => fake()->unique()->safeEmail(),
                    'password' => Hash::make('password'),
                    'status' => 1,
                ]);

                UserProfile::create([
                    'user_id' => $user->id,
                    'name' => $user->name,
                    'mobile' => fake()->phoneNumber(),
                    'address' => fake()->address(),
                    'type' => 2, // Student
                ]);

                $student->id = $user->id;
                $student->name = $user->name;
            }
        });
    }
}

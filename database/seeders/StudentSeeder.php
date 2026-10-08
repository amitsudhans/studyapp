<?php

namespace Database\Seeders;

use App\Models\Standard;
use App\Models\Student;
use Illuminate\Database\Seeder;

class StudentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $standard = Standard::firstOrCreate(
            ['name' => 'Class 5'],
            ['syllabus_id' => 1]
        );

        Student::factory()->count(30)->create([
            'standard_id' => $standard->id,
        ]);
    }
}

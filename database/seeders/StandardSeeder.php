<?php

namespace Database\Seeders;

use App\Models\Standard;
use App\Models\Syllabus;
use Illuminate\Database\Seeder;

class StandardSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $syllabus = Syllabus::firstOrCreate(
            ['name' => 'CBSE']
        );

        for ($i = 1; $i <= 9; $i++) {
            Standard::firstOrCreate([
                'name' => "Class {$i}",
                'syllabus_id' => $syllabus->id,
            ]);
        }
    }
}

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
        $syllabi = [
            'NCERT',
            'CBSE',
            'SCERT Kerala',
        ];

        foreach ($syllabi as $name) {
            $syllabus = Syllabus::firstOrCreate(['name' => $name]);

            for ($i = 1; $i <= 12; $i++) {
                Standard::firstOrCreate([
                    'name' => "Class {$i}",
                    'syllabus_id' => $syllabus->id,
                ]);
            }
        }
    }
}

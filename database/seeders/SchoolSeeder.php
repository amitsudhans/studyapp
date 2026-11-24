<?php

namespace Database\Seeders;

use App\Models\School;
use Illuminate\Database\Seeder;

class SchoolSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        School::firstOrCreate(
            ['name' => 'Kendriya Vidyalaya'],
            [
                'address' => 'Central School Campus, Main Road',
                'contactno' => '+91 9876543210',
                'head' => 'Dr. K. S. Sharma',
                'district' => 'Thiruvananthapuram',
                'state' => 'Kerala',
                'country' => 'India',
            ]
        );
    }
}

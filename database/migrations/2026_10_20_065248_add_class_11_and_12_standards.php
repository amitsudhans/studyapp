<?php

use App\Models\Standard;
use App\Models\Syllabus;
use Illuminate\Database\Migrations\Migration;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        $syllabi = Syllabus::all();

        foreach ($syllabi as $syllabus) {
            foreach (['Class 11', 'Class 12'] as $name) {
                Standard::firstOrCreate([
                    'name' => $name,
                    'syllabus_id' => $syllabus->id,
                ]);
            }
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        // Non-destructive
    }
};

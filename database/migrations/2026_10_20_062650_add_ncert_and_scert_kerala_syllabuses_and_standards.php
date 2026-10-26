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
        // 1. Ensure NCERT, CBSE, and SCERT Kerala exist
        $ncert = Syllabus::firstOrCreate(['name' => 'NCERT']);
        $cbse = Syllabus::firstOrCreate(['name' => 'CBSE']);

        $scert = Syllabus::where('name', 'SCERT Kerala Syllabus')->first();
        if ($scert) {
            $scert->update(['name' => 'SCERT Kerala']);
        } else {
            $scert = Syllabus::firstOrCreate(['name' => 'SCERT Kerala']);
        }

        // 2. Ensure standards (Class 1 to 10) exist for all three syllabuses
        $syllabi = [$ncert, $cbse, $scert];
        foreach ($syllabi as $syl) {
            for ($i = 1; $i <= 10; $i++) {
                Standard::firstOrCreate([
                    'name' => "Class {$i}",
                    'syllabus_id' => $syl->id,
                ]);
            }
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        // Keep non-destructive
    }
};

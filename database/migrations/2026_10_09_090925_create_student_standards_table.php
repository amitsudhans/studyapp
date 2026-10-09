<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('student_standards', function (Blueprint $table) {
            $table->id();
            $table->foreignId('student_id')->constrained('users')->cascadeOnDelete();
            $table->foreignId('standard_id')->constrained('standards')->cascadeOnDelete();
            $table->timestamps();

            $table->unique(['student_id', 'standard_id']);
        });

        // Make standard_id nullable in students table
        try {
            DB::statement('ALTER TABLE students MODIFY standard_id BIGINT UNSIGNED NULL');
        } catch (Throwable $e) {
            // Fallback if DB driver varies
        }

        // Migrate existing standard_id data into student_standards
        $existing = DB::table('students')->whereNotNull('standard_id')->get();
        foreach ($existing as $row) {
            DB::table('student_standards')->updateOrInsert(
                [
                    'student_id' => $row->id,
                    'standard_id' => $row->standard_id,
                ],
                [
                    'created_at' => now(),
                    'updated_at' => now(),
                ]
            );
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('student_standards');
    }
};

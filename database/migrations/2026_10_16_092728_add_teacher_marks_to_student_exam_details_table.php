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
        Schema::table('student_exam_details', function (Blueprint $table) {
            $table->integer('teacher_marks')->nullable()->after('student_text_answer');
            $table->text('teacher_feedback')->nullable()->after('teacher_marks');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('student_exam_details', function (Blueprint $table) {
            $table->dropColumn(['teacher_marks', 'teacher_feedback']);
        });
    }
};

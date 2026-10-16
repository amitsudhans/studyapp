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
            if (! Schema::hasColumn('student_exam_details', 'student_text_answer')) {
                $table->longText('student_text_answer')->nullable()->after('match_answers');
            }
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('student_exam_details', function (Blueprint $table) {
            if (Schema::hasColumn('student_exam_details', 'student_text_answer')) {
                $table->dropColumn('student_text_answer');
            }
        });
    }
};

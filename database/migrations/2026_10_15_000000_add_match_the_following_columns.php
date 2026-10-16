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
        Schema::table('answers', function (Blueprint $table) {
            if (! Schema::hasColumn('answers', 'match_answer')) {
                $table->string('match_answer')->nullable()->after('name');
            }
        });

        Schema::table('student_exam_details', function (Blueprint $table) {
            if (! Schema::hasColumn('student_exam_details', 'match_answers')) {
                $table->text('match_answers')->nullable()->after('student_written_ans_id');
            }
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('answers', function (Blueprint $table) {
            if (Schema::hasColumn('answers', 'match_answer')) {
                $table->dropColumn('match_answer');
            }
        });

        Schema::table('student_exam_details', function (Blueprint $table) {
            if (Schema::hasColumn('student_exam_details', 'match_answers')) {
                $table->dropColumn('match_answers');
            }
        });
    }
};

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
        Schema::table('exams', function (Blueprint $table) {
            if (! Schema::hasColumn('exams', 'syllabus_id')) {
                $table->foreignId('syllabus_id')->nullable()->after('status')->constrained('syllabuses')->nullOnDelete();
            }
            if (! Schema::hasColumn('exams', 'standard_id')) {
                $table->foreignId('standard_id')->nullable()->after('syllabus_id')->constrained('standards')->nullOnDelete();
            }
            if (! Schema::hasColumn('exams', 'subject_id')) {
                $table->foreignId('subject_id')->nullable()->after('standard_id')->constrained('subjects')->nullOnDelete();
            }
            if (! Schema::hasColumn('exams', 'chapter_id')) {
                $table->foreignId('chapter_id')->nullable()->after('subject_id')->constrained('chapters')->nullOnDelete();
            }
            if (! Schema::hasColumn('exams', 'topic_id')) {
                $table->foreignId('topic_id')->nullable()->after('chapter_id')->constrained('topics')->nullOnDelete();
            }
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('exams', function (Blueprint $table) {
            if (Schema::hasColumn('exams', 'standard_id')) {
                $table->dropForeign(['standard_id']);
                $table->dropColumn('standard_id');
            }
        });
    }
};

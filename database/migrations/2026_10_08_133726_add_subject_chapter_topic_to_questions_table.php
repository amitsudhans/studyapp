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
        Schema::table('questions', function (Blueprint $table) {
            $table->foreignId('subject_id')->nullable()->after('standard_id')->constrained('subjects')->nullOnDelete();
            $table->foreignId('chapter_id')->nullable()->after('subject_id')->constrained('chapters')->nullOnDelete();
            $table->foreignId('topic_id')->nullable()->after('chapter_id')->constrained('topics')->nullOnDelete();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('questions', function (Blueprint $table) {
            $table->dropForeign(['subject_id']);
            $table->dropForeign(['chapter_id']);
            $table->dropForeign(['topic_id']);
            $table->dropColumn(['subject_id', 'chapter_id', 'topic_id']);
        });
    }
};

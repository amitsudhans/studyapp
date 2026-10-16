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
        Schema::table('chapters', function (Blueprint $table) {
            if (! Schema::hasColumn('chapters', 'standard_id')) {
                $table->foreignId('standard_id')->nullable()->after('id')->constrained('standards')->cascadeOnDelete();
            }
            $table->foreignId('subject_id')->nullable()->change();
            $table->foreignId('syllabus_id')->nullable()->change();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('chapters', function (Blueprint $table) {
            if (Schema::hasColumn('chapters', 'standard_id')) {
                $table->dropForeign(['standard_id']);
                $table->dropColumn('standard_id');
            }
        });
    }
};

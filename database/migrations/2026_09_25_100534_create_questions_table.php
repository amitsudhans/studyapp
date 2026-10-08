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
        Schema::create('questions', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('description')->nullable();
            $table->foreignId('standard_id')->constrained('standards')->cascadeOnDelete();
            $table->tinyInteger('type')->comment('1: single option, 2: multiple option, 3: Text Entry');
            $table->foreignId('created_by')->constrained('users')->cascadeOnDelete();
            $table->integer('marks')->default(1);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('questions');
    }
};

<?php

use App\Models\Exam;
use App\Models\Question;
use Illuminate\Database\Migrations\Migration;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        $matchQuestions = Question::where('type', 5)->with('answers')->get();
        foreach ($matchQuestions as $question) {
            $pairsCount = $question->answers->count();
            if ($pairsCount > 0) {
                $question->update(['marks' => $pairsCount]);
            }
        }

        foreach (Exam::all() as $exam) {
            $exam->recalculateTotalMarks();
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        //
    }
};

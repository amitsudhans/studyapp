<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Support\Facades\DB;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        $options = [
            'Both (A) and (R) are true, and (R) is the correct explanation of (A).',
            'Both (A) and (R) are true, but (R) is not the correct explanation of (A).',
            '(A) is true, but (R) is false.',
            '(A) is false, but (R) is true.',
        ];

        $now = now();

        // 1. Biology Question for Class 7 (standard_id 7, subject_id 4, chapter_id 8)
        $q1Id = DB::table('questions')->insertGetId([
            'name' => '<p><strong>Assertion (A):</strong> Green plants appear green and synthesize their own food through photosynthesis.</p><p><strong>Reason (R):</strong> Green plants contain the green pigment chlorophyll, which traps light energy essential for photosynthesis.</p>',
            'type' => 10, // Assertion & Reason
            'standard_id' => 7,
            'subject_id' => 4,
            'chapter_id' => 8,
            'marks' => 1,
            'status' => 1,
            'created_by' => 36,
            'solution' => '<p>Both (A) and (R) are true, and (R) is the correct explanation of (A). Chlorophyll absorbs blue and red wavelengths of light while reflecting green light, providing the vital solar energy needed to produce carbohydrates.</p>',
            'created_at' => $now,
            'updated_at' => $now,
        ]);

        foreach ($options as $index => $optText) {
            DB::table('answers')->insert([
                'question_id' => $q1Id,
                'name' => $optText,
                'is_correct' => ($index === 0) ? 1 : 0,
                'status' => 1,
                'created_at' => $now,
                'updated_at' => $now,
            ]);
        }

        // 2. Chemistry Question for Class 7 (standard_id 7, subject_id 3, chapter_id 6)
        $q2Id = DB::table('questions')->insertGetId([
            'name' => '<p><strong>Assertion (A):</strong> Rusting of iron is considered a chemical change.</p><p><strong>Reason (R):</strong> During rusting, iron reacts with oxygen and water to form hydrated iron(III) oxide, an entirely new substance with different properties.</p>',
            'type' => 10, // Assertion & Reason
            'standard_id' => 7,
            'subject_id' => 3,
            'chapter_id' => 6,
            'marks' => 1,
            'status' => 1,
            'created_by' => 36,
            'solution' => '<p>Both (A) and (R) are true, and (R) is the correct explanation of (A). A chemical change is characterized by the formation of new chemical substances with altered properties and chemical compositions, which is observed when iron converts into rust.</p>',
            'created_at' => $now,
            'updated_at' => $now,
        ]);

        foreach ($options as $index => $optText) {
            DB::table('answers')->insert([
                'question_id' => $q2Id,
                'name' => $optText,
                'is_correct' => ($index === 0) ? 1 : 0,
                'status' => 1,
                'created_at' => $now,
                'updated_at' => $now,
            ]);
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        $questions = DB::table('questions')
            ->where('type', 10)
            ->whereIn('name', [
                '<p><strong>Assertion (A):</strong> Green plants appear green and synthesize their own food through photosynthesis.</p><p><strong>Reason (R):</strong> Green plants contain the green pigment chlorophyll, which traps light energy essential for photosynthesis.</p>',
                '<p><strong>Assertion (A):</strong> Rusting of iron is considered a chemical change.</p><p><strong>Reason (R):</strong> During rusting, iron reacts with oxygen and water to form hydrated iron(III) oxide, an entirely new substance with different properties.</p>',
            ])
            ->pluck('id');

        if ($questions->isNotEmpty()) {
            DB::table('answers')->whereIn('question_id', $questions)->delete();
            DB::table('questions')->whereIn('id', $questions)->delete();
        }
    }
};

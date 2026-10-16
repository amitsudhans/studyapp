<?php

namespace Database\Seeders;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class ClassNineCbseExamTenQuestionsBatchFiveSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $syllabus = Syllabus::where('name', 'like', '%CBSE%')->first();
        if (! $syllabus) {
            $syllabus = Syllabus::create(['name' => 'CBSE']);
        }

        $standard = Standard::where('name', 'like', '%Class 9%')->first();
        if (! $standard) {
            $standard = Standard::create([
                'name' => 'Class 9',
                'syllabus_id' => $syllabus->id,
                'created_by' => 2,
            ]);
        }

        $subject = Subject::where('name', 'Mathematics')->first();
        if (! $subject) {
            $subject = Subject::create([
                'name' => 'Mathematics',
                'syllabus_id' => $syllabus->id,
            ]);
        }

        $chapter = Chapter::where('standard_id', $standard->id)
            ->where('name', 'like', '%Number System%')
            ->first();

        if (! $chapter) {
            $chapter = Chapter::create([
                'name' => 'Number System',
                'standard_id' => $standard->id,
                'subject_id' => $subject->id,
                'syllabus_id' => $syllabus->id,
            ]);
        }

        $topic = Topic::where('chapter_id', $chapter->id)
            ->where(function ($q) {
                $q->where('name', 'Number System')
                    ->orWhere('name', 'like', '%Number System%');
            })
            ->first();

        if (! $topic) {
            $topic = Topic::create([
                'name' => 'Number System',
                'chapter_id' => $chapter->id,
            ]);
        }

        $questionsData = [
            [
                'name' => 'Which of the following numbers is a rational number lying between 1 and 2?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Identifying rational numbers between consecutive integers.',
                'hint' => 'Check which fraction has a value strictly between 1 and 2, and can be represented as a terminating or repeating decimal.',
                'solution' => "Let's examine each option:\n- 4/3 = 1.333... which is a rational number strictly between 1 and 2.\n- √2 ≈ 1.414... (an irrational number)\n- √3 ≈ 1.732... (an irrational number)\n- √5 ≈ 2.236... (which is greater than 2 and irrational).\n\nTherefore, 4/3 is the rational number between 1 and 2.",
                'options' => [
                    ['name' => '4/3', 'is_correct' => 1],
                    ['name' => '√2', 'is_correct' => 0],
                    ['name' => '√3', 'is_correct' => 0],
                    ['name' => '√5', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The simplified value of [(625)^(−1/2)]^(−1/4) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Nested negative fractional exponents.',
                'hint' => 'Multiply the nested powers first: (-1/2) × (-1/4) = 1/8. Then write 625 as 5⁴.',
                'solution' => "Using the power law of exponents [(a)^m]^n = a^(mn):\n[(625)^(-1/2)]^(-1/4) = (625)^((-1/2) × (-1/4)) = (625)^(1/8)\n\nSince 625 = 5⁴:\n= (5⁴)^(1/8)\n= 5^(4 × 1/8)\n= 5^(1/2)\n= √5.",
                'options' => [
                    ['name' => '√5', 'is_correct' => 1],
                    ['name' => '5', 'is_correct' => 0],
                    ['name' => '25', 'is_correct' => 0],
                    ['name' => '1/√5', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The maximum number of digits that can be in the repeating block of digits in the decimal expansion of 1/17 is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Period of repeating decimal block for unit fractions 1/q.',
                'hint' => 'In the long division of 1/q, the remainders must be less than q. Therefore, the period cannot exceed (q − 1).',
                'solution' => "When dividing 1 by 17, the only possible non-zero remainders are 1, 2, 3, ..., 16 (16 distinct remainders).\n\nOnce a remainder repeats, the sequence of quotient digits begins to repeat.\nHence, the maximum number of digits in the repeating block of digits in 1/17 is 17 - 1 = 16.",
                'options' => [
                    ['name' => '16', 'is_correct' => 1],
                    ['name' => '17', 'is_correct' => 0],
                    ['name' => '18', 'is_correct' => 0],
                    ['name' => '15', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The expanded product of (3 + √3)(2 + √2) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Distributive multiplication of real numbers with square roots.',
                'hint' => 'Apply the distributive property: (a + b)(c + d) = ac + ad + bc + bd.',
                'solution' => "Using the distributive law:\n(3 + √3)(2 + √2) = 3(2 + √2) + √3(2 + √2)\n= (3 × 2) + (3 × √2) + (√3 × 2) + (√3 × √2)\n= 6 + 3√2 + 2√3 + √6.",
                'options' => [
                    ['name' => '6 + 3√2 + 2√3 + √6', 'is_correct' => 1],
                    ['name' => '6 + 5√5 + √6', 'is_correct' => 0],
                    ['name' => '6 + √6', 'is_correct' => 0],
                    ['name' => '5 + 5√6', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The rationalising factor of ∛4 is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Finding the rationalising factor for higher-order cube roots.',
                'hint' => 'Write ∛4 as ∛(2²). What cube root multiplied by ∛(2²) will give ∛(2³) = 2?',
                'solution' => "Notice that ∛4 = ∛(2²).\nTo make the exponent a multiple of 3 (the index of the radical):\n∛(2²) × ∛(2¹) = ∛(2³)\n= 2, which is a rational number.\n\nTherefore, the rationalising factor of ∛4 is ∛2.",
                'options' => [
                    ['name' => '∛2', 'is_correct' => 1],
                    ['name' => '√2', 'is_correct' => 0],
                    ['name' => '4', 'is_correct' => 0],
                    ['name' => '∛16', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If 2^(x + 3) = 32, then the value of x is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Equating exponents when bases are equal.',
                'hint' => 'Express 32 as a power of 2: 32 = 2⁵. Then equate the powers on both sides.',
                'solution' => "Given equation:\n2^(x + 3) = 32\n\nExpress 32 as a power of base 2:\n32 = 2⁵\n\nSo:\n2^(x + 3) = 2⁵\n\nSince the bases are identical, equate the exponents:\nx + 3 = 5\nx = 5 - 3\nx = 2.",
                'options' => [
                    ['name' => '2', 'is_correct' => 1],
                    ['name' => '3', 'is_correct' => 0],
                    ['name' => '5', 'is_correct' => 0],
                    ['name' => '1', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If (5 + 2√3) / (7 + 4√3) = a + b√3, where a and b are rational numbers, then the value of (a + b) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Rationalising denominator with coefficients and linear surds.',
                'hint' => 'Rationalise the denominator by multiplying both numerator and denominator by (7 − 4√3). Find a and b, then add them.',
                'solution' => "Rationalising the denominator of LHS:\n(5 + 2√3) / (7 + 4√3) = [(5 + 2√3)(7 - 4√3)] / [(7 + 4√3)(7 - 4√3)]\n\nDenominator:\n7² - (4√3)² = 49 - (16 × 3) = 49 - 48 = 1\n\nNumerator:\n5(7) - 5(4√3) + 2√3(7) - 2√3(4√3)\n= 35 - 20√3 + 14√3 - (8 × 3)\n= 35 - 24 - 6√3\n= 11 - 6√3\n\nComparing 11 - 6√3 with a + b√3:\na = 11, b = -6\n\nTherefore:\na + b = 11 + (-6) = 5.",
                'options' => [
                    ['name' => '5', 'is_correct' => 1],
                    ['name' => '17', 'is_correct' => 0],
                    ['name' => '−5', 'is_correct' => 0],
                    ['name' => '11', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The simplified value of √48 / √12 is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Division of square roots: √a / √b = √(a/b).',
                'hint' => 'Use the quotient property of square roots: √a / √b = √(a / b). Divide 48 by 12 under the radical.',
                'solution' => "Using the property √a / √b = √(a / b):\n√48 / √12 = √(48 / 12)\n= √4\n= 2.",
                'options' => [
                    ['name' => '2', 'is_correct' => 1],
                    ['name' => '4', 'is_correct' => 0],
                    ['name' => '2√3', 'is_correct' => 0],
                    ['name' => '√36', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Which of the following is the greatest among √2, ∛3, and ∜4?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Comparing surds of different orders using common LCM index.',
                'hint' => 'Find the LCM of the radical indices (2, 3, 4), which is 12. Convert each surd to order 12 and compare the numbers under the root.',
                'solution' => "The orders of the radicals are 2, 3, and 4. The LCM of (2, 3, 4) = 12.\n\nConvert each surd to index 12:\n- √2 = 2^(1/2) = 2^(6/12) = ¹²√(2⁶) = ¹²√64\n- ∛3 = 3^(1/3) = 3^(4/12) = ¹²√(3⁴) = ¹²√81\n- ∜4 = 4^(1/4) = 4^(3/12) = ¹²√(4³) = ¹²√64\n\nComparing the radicands: 81 > 64 = 64.\nHence, ∛3 is the greatest.",
                'options' => [
                    ['name' => '∛3', 'is_correct' => 1],
                    ['name' => '√2', 'is_correct' => 0],
                    ['name' => '∜4', 'is_correct' => 0],
                    ['name' => 'All are equal', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The sum of two irrational numbers is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Arithmetic properties and closure of irrational numbers.',
                'hint' => 'Consider: (2 + √3) + (2 − √3) = 4 (rational), but √2 + √3 is irrational.',
                'solution' => "The sum of two irrational numbers is sometimes rational and sometimes irrational.\n\nExamples:\n1) (3 + √5) + (3 - √5) = 6 (which is rational)\n2) √2 + √3 (which is irrational)\n\nTherefore, irrational numbers are not closed under addition.",
                'options' => [
                    ['name' => 'Sometimes rational, sometimes irrational', 'is_correct' => 1],
                    ['name' => 'Always rational', 'is_correct' => 0],
                    ['name' => 'Always irrational', 'is_correct' => 0],
                    ['name' => 'Always an integer', 'is_correct' => 0],
                ],
            ],
        ];

        foreach ($questionsData as $qData) {
            $existing = Question::where('chapter_id', $chapter->id)
                ->where('name', $qData['name'])
                ->first();

            if ($existing) {
                $this->command->info("Question already exists: {$qData['name']}");

                continue;
            }

            $question = Question::create([
                'name' => $qData['name'],
                'description' => $qData['description'],
                'hint' => $qData['hint'],
                'solution' => $qData['solution'],
                'standard_id' => $standard->id,
                'subject_id' => $subject->id,
                'chapter_id' => $chapter->id,
                'topic_id' => $topic->id,
                'type' => 1, // Single choice MCQ
                'created_by' => 2, // Admin User
                'marks' => 1,
                'status' => 1,
            ]);

            foreach ($qData['options'] as $opt) {
                Answer::create([
                    'question_id' => $question->id,
                    'name' => $opt['name'],
                    'is_correct' => $opt['is_correct'],
                    'status' => 1,
                ]);
            }

            $this->command->info("Created CBSE Class 9 Question #{$question->id}: {$question->name}");
        }
    }
}

<?php

namespace Database\Seeders;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class ClassNineNumberSystemTenMcqSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $standard = Standard::where('name', 'like', '%Class 9%')->first();
        if (! $standard) {
            $standard = Standard::create([
                'name' => 'Class 9',
                'syllabus_id' => 1,
                'created_by' => 2,
            ]);
        }

        $subject = Subject::where('name', 'Mathematics')->first();
        if (! $subject) {
            $subject = Subject::create([
                'name' => 'Mathematics',
                'syllabus_id' => $standard->syllabus_id ?? 1,
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
                'syllabus_id' => $standard->syllabus_id ?? 1,
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
                'name' => 'Between two rational numbers, there exist:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Density property of rational numbers.',
                'hint' => 'Consider finding the arithmetic mean (average) between any two rational numbers; this process can be repeated indefinitely.',
                'solution' => "Between any two distinct rational numbers, there are infinitely many rational numbers (and infinitely many irrational numbers). This is known as the density property of rational numbers.\n\nFor example, between 1/3 and 1/2, one can find (1/3 + 1/2)/2 = 5/12, and then repeat this between any new pair endlessly.",
                'options' => [
                    ['name' => 'No rational number', 'is_correct' => 0],
                    ['name' => 'Exactly one rational number', 'is_correct' => 0],
                    ['name' => 'Infinitely many rational numbers', 'is_correct' => 1],
                    ['name' => 'Only irrational numbers', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Which of the following statements is true for real numbers?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Classification of real numbers.',
                'hint' => 'Every real number is either rational or irrational; consider their decimal expansions on the number line.',
                'solution' => "The set of real numbers consists of all rational numbers and all irrational numbers combined. Every real number is either rational (can be written as p/q) or irrational (non-terminating non-repeating decimal).\n\nTherefore, every real number is either rational or irrational.",
                'options' => [
                    ['name' => 'Every real number is a rational number', 'is_correct' => 0],
                    ['name' => 'Every real number is an irrational number', 'is_correct' => 0],
                    ['name' => 'Every real number is either rational or irrational', 'is_correct' => 1],
                    ['name' => 'Every integer is an irrational number', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The decimal expansion of the number √2 is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Decimal expansion of irrational numbers.',
                'hint' => 'Since 2 is a prime number and not a perfect square, √2 is an irrational number.',
                'solution' => "√2 = 1.41421356... is an irrational number.\n\nBy definition, the decimal expansion of an irrational number is always non-terminating and non-recurring (non-repeating). A terminating or recurring decimal would make it a rational number.",
                'options' => [
                    ['name' => 'A finite decimal', 'is_correct' => 0],
                    ['name' => '1.41421', 'is_correct' => 0],
                    ['name' => 'Non-terminating recurring', 'is_correct' => 0],
                    ['name' => 'Non-terminating non-recurring', 'is_correct' => 1],
                ],
            ],
            [
                'name' => 'The value of 0.3̄ (0.333...) expressed in the form p/q, where p and q are integers and q ≠ 0, is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Conversion of recurring decimals to rational form.',
                'hint' => 'Let x = 0.333... Multiply by 10 to obtain 10x = 3.333... then subtract the two equations.',
                'solution' => "Let x = 0.333... (Equation 1)\nMultiplying by 10 on both sides:\n10x = 3.333... (Equation 2)\nSubtracting Eq 1 from Eq 2:\n10x - x = 3.333... - 0.333...\n9x = 3\nx = 3/9 = 1/3.",
                'options' => [
                    ['name' => '1/3', 'is_correct' => 1],
                    ['name' => '3/10', 'is_correct' => 0],
                    ['name' => '33/100', 'is_correct' => 0],
                    ['name' => '1/9', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (√5 + √2)(√5 − √2) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Algebraic identities involving square roots.',
                'hint' => 'Apply the algebraic identity (a + b)(a − b) = a² − b².',
                'solution' => "Using the identity (a + b)(a - b) = a² - b²:\n(√5 + √2)(√5 - √2) = (√5)² - (√2)²\n= 5 - 2\n= 3.",
                'options' => [
                    ['name' => '3', 'is_correct' => 1],
                    ['name' => '7', 'is_correct' => 0],
                    ['name' => '√10', 'is_correct' => 0],
                    ['name' => '√3', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'On rationalising the denominator of 1 / (√7 − 2), we get:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Rationalisation of denominators.',
                'hint' => 'Multiply both the numerator and denominator by the conjugate of the denominator, (√7 + 2).',
                'solution' => "Multiply numerator and denominator by the conjugate (√7 + 2):\n1 / (√7 - 2) = [1 × (√7 + 2)] / [(√7 - 2)(√7 + 2)]\n= (√7 + 2) / [(√7)² - (2)²]\n= (√7 + 2) / (7 - 4)\n= (√7 + 2) / 3.",
                'options' => [
                    ['name' => '(√7 + 2) / 3', 'is_correct' => 1],
                    ['name' => '(√7 − 2) / 3', 'is_correct' => 0],
                    ['name' => '(√7 + 2) / 5', 'is_correct' => 0],
                    ['name' => '√7 + 2', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (64)^(−1/2) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Laws of exponents for real numbers.',
                'hint' => 'Use the rules: a^(−n) = 1 / a^n and (x²)^(1/2) = x.',
                'solution' => "According to the laws of exponents:\n(64)^(-1/2) = 1 / (64)^(1/2)\nSince 64 = 8²:\n(64)^(1/2) = (8²)^(1/2) = 8^(2 × 1/2) = 8^1 = 8\nTherefore, (64)^(-1/2) = 1/8.",
                'options' => [
                    ['name' => '1/8', 'is_correct' => 1],
                    ['name' => '8', 'is_correct' => 0],
                    ['name' => '−8', 'is_correct' => 0],
                    ['name' => '1/16', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (125)^(1/3) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Fractional exponents.',
                'hint' => 'Express 125 as a power of 5: 125 = 5³.',
                'solution' => "We know that 125 = 5 × 5 × 5 = 5³.\nApplying the law of exponents (a^m)^n = a^(m × n):\n(125)^(1/3) = (5³)^(1/3) = 5^(3 × 1/3) = 5^1 = 5.",
                'options' => [
                    ['name' => '5', 'is_correct' => 1],
                    ['name' => '25', 'is_correct' => 0],
                    ['name' => '1/5', 'is_correct' => 0],
                    ['name' => '5√5', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Simplify: 2^(2/3) · 2^(1/3)',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Multiplication law of exponents with same base.',
                'hint' => 'Apply the law of exponents: a^m · a^n = a^(m + n).',
                'solution' => "Using the product rule of exponents a^m · a^n = a^(m + n):\n2^(2/3) · 2^(1/3) = 2^(2/3 + 1/3)\n= 2^(3/3)\n= 2^1\n= 2.",
                'options' => [
                    ['name' => '2', 'is_correct' => 1],
                    ['name' => '4', 'is_correct' => 0],
                    ['name' => '2^(2/9)', 'is_correct' => 0],
                    ['name' => '1', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Which of the following is an irrational number?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Identifying rational vs irrational numbers.',
                'hint' => 'Simplify each option; notice which one retains a radical of a non-perfect square.',
                'solution' => "Let's simplify each option:\n1) √4 / √9 = 2/3 (which is rational)\n2) √12 / √3 = √(12/3) = √4 = 2 (which is rational)\n3) √7 is non-terminating and non-recurring because 7 is a prime number and not a perfect square (which is irrational)\n4) √81 = 9 (which is rational)\n\nHence, √7 is the irrational number.",
                'options' => [
                    ['name' => '√7', 'is_correct' => 1],
                    ['name' => '√4 / √9', 'is_correct' => 0],
                    ['name' => '√12 / √3', 'is_correct' => 0],
                    ['name' => '√81', 'is_correct' => 0],
                ],
            ],
        ];

        foreach ($questionsData as $qData) {
            // Avoid duplicate question creation
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

            $this->command->info("Created MCQ Question #{$question->id}: {$question->name}");
        }
    }
}

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

class ClassNineCbseNumberSystemTenMoreQuestionsSeeder extends Seeder
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
                'name' => 'The value of 0.9̄ (0.999...) in the form p/q, where p and q are integers and q ≠ 0, is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Expressing non-terminating repeating decimals in rational p/q form.',
                'hint' => 'Let x = 0.999... Multiply both sides by 10 to obtain 10x = 9.999... and then subtract the two equations.',
                'solution' => "Let x = 0.999...  --- (Equation 1)\n\nMultiply both sides by 10:\n10x = 9.999...  --- (Equation 2)\n\nSubtract Equation 1 from Equation 2:\n10x - x = 9.999... - 0.999...\n9x = 9\nx = 9/9 = 1.\n\nThus, 0.999... is mathematically identical to 1.",
                'options' => [
                    ['name' => '1', 'is_correct' => 1],
                    ['name' => '9/10', 'is_correct' => 0],
                    ['name' => '99/100', 'is_correct' => 0],
                    ['name' => '0.9', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The rationalising factor of (√5 + √3) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Identifying the conjugate/rationalising factor of a binomial surd.',
                'hint' => 'To make (√a + √b) a rational number using the identity (a + b)(a − b) = a² − b², multiply it by its conjugate surd.',
                'solution' => "The conjugate (rationalising factor) of (√5 + √3) is (√5 - √3).\n\nVerification:\n(√5 + √3)(√5 - √3) = (√5)² - (√3)² = 5 - 3 = 2, which is a rational number.",
                'options' => [
                    ['name' => '√5 − √3', 'is_correct' => 1],
                    ['name' => '√5 + √3', 'is_correct' => 0],
                    ['name' => '5 − 3', 'is_correct' => 0],
                    ['name' => '√2', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (32)^(2/5) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Evaluating numbers with rational exponents.',
                'hint' => 'Express 32 as a power of 2: 32 = 2⁵, then apply the power of a power rule: (a^m)^n = a^(mn).',
                'solution' => "We know that 32 = 2⁵.\n\nUsing the law of exponents (a^m)^n = a^(m × n):\n(32)^(2/5) = (2⁵)^(2/5)\n= 2^(5 × 2/5)\n= 2²\n= 4.",
                'options' => [
                    ['name' => '4', 'is_correct' => 1],
                    ['name' => '8', 'is_correct' => 0],
                    ['name' => '2', 'is_correct' => 0],
                    ['name' => '16', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (16)^(3/4) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Laws of exponents with rational exponents.',
                'hint' => 'Express 16 as 2⁴ and use the rule (a^m)^n = a^(mn).',
                'solution' => "Express 16 in prime factorized form:\n16 = 2⁴\n\nApply the exponent rule (a^m)^n = a^(m × n):\n(16)^(3/4) = (2⁴)^(3/4)\n= 2^(4 × 3/4)\n= 2³\n= 8.",
                'options' => [
                    ['name' => '8', 'is_correct' => 1],
                    ['name' => '4', 'is_correct' => 0],
                    ['name' => '12', 'is_correct' => 0],
                    ['name' => '16', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If x = 3 + 2√2, then the value of (x² + 1/x²) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. High-yield algebraic manipulation with binomial surds.',
                'hint' => 'First calculate 1/x by rationalising the denominator: 1 / (3 + 2√2) = 3 − 2√2. Then find x + 1/x, and use x² + 1/x² = (x + 1/x)² − 2.',
                'solution' => "Given x = 3 + 2√2.\n\nRationalising 1/x:\n1/x = 1 / (3 + 2√2) = [3 - 2√2] / [(3 + 2√2)(3 - 2√2)]\n= (3 - 2√2) / (3² - (2√2)²)\n= (3 - 2√2) / (9 - 8)\n= 3 - 2√2\n\nNow find x + 1/x:\nx + 1/x = (3 + 2√2) + (3 - 2√2) = 6\n\nUsing the identity x² + 1/x² = (x + 1/x)² - 2:\nx² + 1/x² = 6² - 2 = 36 - 2 = 34.",
                'options' => [
                    ['name' => '34', 'is_correct' => 1],
                    ['name' => '36', 'is_correct' => 0],
                    ['name' => '38', 'is_correct' => 0],
                    ['name' => '32', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Which of the following rational numbers has a terminating decimal expansion?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Condition for terminating decimal expansions (2^m · 5^n).',
                'hint' => 'A rational number p/q in simplest form has a terminating decimal expansion if the prime factors of denominator q consist only of 2s and/or 5s.',
                'solution' => "A fraction in simplest form has a terminating decimal expansion if its denominator is of the form 2^m × 5^n.\n\nEvaluating the options:\nA) 17/20: Denominator 20 = 2² × 5¹ (only factors of 2 and 5) ⇒ Terminating (17/20 = 0.85)\nB) 1/7: Denominator contains prime factor 7 ⇒ Non-terminating recurring\nC) 2/3: Denominator contains prime factor 3 ⇒ Non-terminating recurring\nD) 7/15: Denominator 15 = 3 × 5 (contains 3) ⇒ Non-terminating recurring\n\nTherefore, 17/20 is the terminating decimal.",
                'options' => [
                    ['name' => '17/20', 'is_correct' => 1],
                    ['name' => '1/7', 'is_correct' => 0],
                    ['name' => '2/3', 'is_correct' => 0],
                    ['name' => '7/15', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The simplified value of (√11 − √7)(√11 + √7) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Multiplying conjugate square roots.',
                'hint' => 'Apply the algebraic identity: (a − b)(a + b) = a² − b².',
                'solution' => "Using the difference of squares identity (a - b)(a + b) = a² - b²:\n(√11 - √7)(√11 + √7) = (√11)² - (√7)²\n= 11 - 7\n= 4.",
                'options' => [
                    ['name' => '4', 'is_correct' => 1],
                    ['name' => '18', 'is_correct' => 0],
                    ['name' => '2', 'is_correct' => 0],
                    ['name' => '√44', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'An irrational number lying between √2 (≈ 1.414) and √3 (≈ 1.732) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Constructing and identifying irrational numbers between real numbers.',
                'hint' => 'An irrational number has a non-terminating and non-recurring decimal pattern. Check which number lies between 1.414 and 1.732.',
                'solution' => "We know:\n√2 ≈ 1.41421...\n√3 ≈ 1.73205...\n\nAn irrational number must have a non-terminating and non-repeating decimal expansion.\nThe number 1.5050050005... lies between 1.414 and 1.732 and has a non-terminating, non-repeating pattern. Hence it is an irrational number between √2 and √3.",
                'options' => [
                    ['name' => '1.5050050005...', 'is_correct' => 1],
                    ['name' => '1.8123...', 'is_correct' => 0],
                    ['name' => '1.3123...', 'is_correct' => 0],
                    ['name' => '2.1414...', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (8⁰ × 2⁰) / 4⁰ is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Zero exponent law: a⁰ = 1 for any non-zero real number.',
                'hint' => 'Recall the fundamental law of exponents: any non-zero real number raised to the power 0 equals 1.',
                'solution' => "According to the zero exponent rule, a⁰ = 1 for any non-zero real number a.\n\nTherefore:\n8⁰ = 1\n2⁰ = 1\n4⁰ = 1\n\nSubstituting these values:\n(8⁰ × 2⁰) / 4⁰ = (1 × 1) / 1 = 1.",
                'options' => [
                    ['name' => '1', 'is_correct' => 1],
                    ['name' => '0', 'is_correct' => 0],
                    ['name' => '4', 'is_correct' => 0],
                    ['name' => '2', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (9)^(3/2) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Evaluating square roots and cubic powers.',
                'hint' => 'Write 9 as 3²: (9)^(3/2) = (3²)^(3/2) = 3^(2 × 3/2).',
                'solution' => "We know that 9 = 3².\n\nApplying the law of exponents (a^m)^n = a^(m × n):\n(9)^(3/2) = (3²)^(3/2)\n= 3^(2 × 3/2)\n= 3³\n= 27.",
                'options' => [
                    ['name' => '27', 'is_correct' => 1],
                    ['name' => '9', 'is_correct' => 0],
                    ['name' => '81', 'is_correct' => 0],
                    ['name' => '18', 'is_correct' => 0],
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

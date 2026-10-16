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

class ClassNineCbseExamTenQuestionsBatchFourSeeder extends Seeder
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
                'name' => 'Which of the following statements about the number zero (0) is correct?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Classification and representation of zero as a rational number.',
                'hint' => 'Recall the definition of a rational number: any number that can be expressed in the form p/q, where p and q are integers and q ≠ 0.',
                'solution' => "Zero is a rational number because it can be written in the form p/q (such as 0/1, 0/2, or 0/(-5)), where p = 0 and q ≠ 0 are both integers.\n\nThus, 0 satisfies all conditions of a rational number.",
                'options' => [
                    ['name' => 'Zero is a rational number because it can be written as 0/1', 'is_correct' => 1],
                    ['name' => 'Zero is an irrational number because it has no value', 'is_correct' => 0],
                    ['name' => 'Zero is neither rational nor irrational', 'is_correct' => 0],
                    ['name' => 'Zero cannot be represented on a number line', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The number π (pi) is classified as:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Real numbers and nature of mathematical constant pi.',
                'hint' => 'While 22/7 is an approximate rational representation used for calculations, the exact value of π has a non-terminating and non-recurring decimal expansion.',
                'solution' => "π is an irrational number because its decimal expansion is non-terminating and non-recurring (3.14159265...).\n\nThe fraction 22/7 is only an approximate rational value used for convenient practical calculation, not the exact value of π.",
                'options' => [
                    ['name' => 'An irrational number', 'is_correct' => 1],
                    ['name' => 'A rational number', 'is_correct' => 0],
                    ['name' => 'An integer', 'is_correct' => 0],
                    ['name' => 'A terminating decimal', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of (256)^(0.16) × (256)^(0.09) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Product law of exponents with decimal powers.',
                'hint' => 'Use the law of exponents: a^m × a^n = a^(m+n). Add the decimal exponents: 0.16 + 0.09 = 0.25 = 1/4.',
                'solution' => "Using the product rule of exponents a^m × a^n = a^(m+n):\n(256)^(0.16) × (256)^(0.09) = (256)^(0.16 + 0.09) = (256)^(0.25)\n\nConvert 0.25 to fraction:\n0.25 = 25/100 = 1/4\n\nExpress 256 as 4⁴:\n(4⁴)^(1/4) = 4^(4 × 1/4) = 4¹ = 4.",
                'options' => [
                    ['name' => '4', 'is_correct' => 1],
                    ['name' => '16', 'is_correct' => 0],
                    ['name' => '64', 'is_correct' => 0],
                    ['name' => '256.25', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The number 1.2̄7̄ (1.272727...) expressed in the form p/q in lowest terms is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Converting repeating decimals to rational p/q fraction.',
                'hint' => 'Let x = 1.2727... Since two digits repeat under the bar, multiply by 100 on both sides, then subtract x.',
                'solution' => "Let x = 1.272727...  --- (Equation 1)\n\nMultiply by 100:\n100x = 127.272727...  --- (Equation 2)\n\nSubtract Equation 1 from Equation 2:\n100x - x = 127.2727... - 1.2727...\n99x = 126\nx = 126 / 99\n\nDividing numerator and denominator by 9:\nx = 14 / 11.",
                'options' => [
                    ['name' => '14/11', 'is_correct' => 1],
                    ['name' => '127/100', 'is_correct' => 0],
                    ['name' => '127/99', 'is_correct' => 0],
                    ['name' => '11/14', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'When simplified, 1 / (√3 + √2) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Rationalising denominator of surds.',
                'hint' => 'Multiply the numerator and denominator by the conjugate of the denominator, (√3 − √2).',
                'solution' => "Multiply numerator and denominator by conjugate (√3 - √2):\n1 / (√3 + √2) × (√3 - √2) / (√3 - √2)\n= (√3 - √2) / [ (√3)² - (√2)² ]\n= (√3 - √2) / (3 - 2)\n= √3 - √2.",
                'options' => [
                    ['name' => '√3 − √2', 'is_correct' => 1],
                    ['name' => '√3 + √2', 'is_correct' => 0],
                    ['name' => '5', 'is_correct' => 0],
                    ['name' => '(√3 − √2) / 5', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'To represent √x geometrically on the number line, a segment AB = x is drawn and extended to C such that BC = 1. The radius of the semicircle on diameter AC is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Geometric construction of square roots on number line.',
                'hint' => 'The length of diameter AC = AB + BC = x + 1. The radius is half of diameter AC.',
                'solution' => "The diameter of the semicircle is AC = AB + BC = x + 1 units.\n\nThe radius is half the diameter:\nRadius = AC / 2 = (x + 1) / 2.",
                'options' => [
                    ['name' => '(x + 1) / 2', 'is_correct' => 1],
                    ['name' => '(x − 1) / 2', 'is_correct' => 0],
                    ['name' => '√x / 2', 'is_correct' => 0],
                    ['name' => 'x + 1', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The simplified value of (81/16)^(−3/4) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Negative fractional exponents and power laws.',
                'hint' => 'Use (a/b)^(−n) = (b/a)^n, and note that 16 = 2⁴ and 81 = 3⁴.',
                'solution' => "Using the negative exponent rule (a/b)^(-n) = (b/a)^n:\n(81/16)^(-3/4) = (16/81)^(3/4)\n\nExpress 16 and 81 in terms of power 4:\n16 = 2⁴ and 81 = 3⁴ ⇒ 16/81 = (2/3)⁴\n\nNow apply the power rule ((2/3)⁴)^(3/4):\n= (2/3)^(4 × 3/4)\n= (2/3)³\n= 2³ / 3³\n= 8/27.",
                'options' => [
                    ['name' => '8/27', 'is_correct' => 1],
                    ['name' => '27/8', 'is_correct' => 0],
                    ['name' => '−8/27', 'is_correct' => 0],
                    ['name' => '16/81', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If x = 3 + √8, then the value of (x − 1/x) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Difference of a binomial surd and its reciprocal.',
                'hint' => 'First rationalise 1/x: 1 / (3 + √8) = 3 − √8. Then compute x − 1/x and express √8 as 2√2.',
                'solution' => "Given x = 3 + √8.\n\nRationalise 1/x:\n1/x = 1 / (3 + √8) = (3 - √8) / (3² - (√8)²)\n= (3 - √8) / (9 - 8)\n= 3 - √8.\n\nCalculate x - 1/x:\nx - 1/x = (3 + √8) - (3 - √8)\n= 3 + √8 - 3 + √8\n= 2√8.\n\nSince √8 = √(4 × 2) = 2√2:\n2√8 = 2 × 2√2 = 4√2.",
                'options' => [
                    ['name' => '4√2', 'is_correct' => 1],
                    ['name' => '6', 'is_correct' => 0],
                    ['name' => '2√8 + 6', 'is_correct' => 0],
                    ['name' => '0', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'Which of the following expressions is identically equal to x for all x > 0?',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. NCERT Exemplar problem on exponential identities.',
                'hint' => 'Convert radicals to fractional powers and apply (a^m)^n = a^(mn). Note that √x³ = (x³)^(1/2) = x^(3/2).',
                'solution' => "Let's simplify (√(x³))^(2/3):\n√(x³) = (x³)^(1/2) = x^(3/2)\n\nNow raise to the power 2/3:\n(x^(3/2))^(2/3) = x^((3/2) × (2/3)) = x¹ = x.\n\nNone of the other options simplify to x:\n- x^(12/7) − x^(5/7) ≠ x\n- ¹²√((x⁴)^(1/3)) = x^(4/36) = x^(1/9) ≠ x\n- x^(12/7) × x^(7/12) = x^(193/84) ≠ x.",
                'options' => [
                    ['name' => '(√(x³))^(2/3)', 'is_correct' => 1],
                    ['name' => 'x^(12/7) − x^(5/7)', 'is_correct' => 0],
                    ['name' => '¹²√((x⁴)^(1/3))', 'is_correct' => 0],
                    ['name' => 'x^(12/7) × x^(7/12)', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The expansion of (√3 + √2)² yields:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Binomial surd expansion using algebraic identity.',
                'hint' => 'Apply the algebraic identity (a + b)² = a² + 2ab + b², where a = √3 and b = √2.',
                'solution' => "Using the identity (a + b)² = a² + 2ab + b²:\n(√3 + √2)² = (√3)² + 2(√3)(√2) + (√2)²\n= 3 + 2√6 + 2\n= 5 + 2√6.",
                'options' => [
                    ['name' => '5 + 2√6', 'is_correct' => 1],
                    ['name' => '5 + √6', 'is_correct' => 0],
                    ['name' => '5', 'is_correct' => 0],
                    ['name' => '1 + 2√6', 'is_correct' => 0],
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

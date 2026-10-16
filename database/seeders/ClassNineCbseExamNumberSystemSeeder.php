<?php

namespace Database\Seeders;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class ClassNineCbseExamNumberSystemSeeder extends Seeder
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
                'name' => 'A rational number lying between 3/5 and 4/5 is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Inserting rational numbers between two given rational numbers.',
                'hint' => 'Convert both fractions to an equivalent common denominator of 10, or calculate their average: (3/5 + 4/5) / 2.',
                'solution' => "To find a rational number between 3/5 and 4/5, multiply both numerator and denominator by 2 to convert them to equivalent fractions with denominator 10:\n\n3/5 = (3 × 2) / (5 × 2) = 6/10\n4/5 = (4 × 2) / (5 × 2) = 8/10\n\nThe number 7/10 clearly lies strictly between 6/10 and 8/10.\nHence, 7/10 lies between 3/5 and 4/5.",
                'options' => [
                    ['name' => '7/10', 'is_correct' => 1],
                    ['name' => '7/5', 'is_correct' => 0],
                    ['name' => '3/10', 'is_correct' => 0],
                    ['name' => '4/10', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of 0.474747... (0.4̄7̄) in the form p/q, where p and q are integers and q ≠ 0, is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Converting non-terminating repeating decimals with two recurring digits into rational p/q form.',
                'hint' => "Let x = 0.474747... Since two digits '47' are repeating under the bar, multiply x by 100 and subtract equation (1) from equation (2).",
                'solution' => "Let x = 0.474747...  --- (Equation 1)\n\nSince two digits repeat continuously, multiply both sides by 100:\n100x = 47.474747...  --- (Equation 2)\n\nSubtract Equation 1 from Equation 2:\n100x - x = 47.474747... - 0.474747...\n99x = 47\nx = 47/99.",
                'options' => [
                    ['name' => '47/99', 'is_correct' => 1],
                    ['name' => '47/90', 'is_correct' => 0],
                    ['name' => '43/90', 'is_correct' => 0],
                    ['name' => '47/100', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of 0.23̄ (0.2333...) in the form p/q, where p and q are integers and q ≠ 0, in simplest form is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Converting mixed recurring decimals into p/q form.',
                'hint' => 'Multiply x by 10 to shift the non-repeating digit past the decimal point, and by 100 to shift one period of the repeating digit, then subtract.',
                'solution' => "Let x = 0.2333...  --- (Equation 1)\n\nMultiply by 10:\n10x = 2.333...  --- (Equation 2)\n\nMultiply by 100:\n100x = 23.333...  --- (Equation 3)\n\nSubtract Equation 2 from Equation 3:\n100x - 10x = 23.333... - 2.333...\n90x = 21\nx = 21/90\n\nDividing numerator and denominator by 3:\nx = 7/30.",
                'options' => [
                    ['name' => '7/30', 'is_correct' => 1],
                    ['name' => '23/99', 'is_correct' => 0],
                    ['name' => '23/90', 'is_correct' => 0],
                    ['name' => '21/100', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If (√3 − 1) / (√3 + 1) = a + b√3, where a and b are rational numbers, then the values of a and b are:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Rationalisation of surd denominators and determining coefficients.',
                'hint' => 'Multiply numerator and denominator by the conjugate (√3 − 1), expand using algebraic identities, and compare with a + b√3.',
                'solution' => "Rationalise the denominator of LHS:\n(√3 - 1) / (√3 + 1) = [(√3 - 1)(√3 - 1)] / [(√3 + 1)(√3 - 1)]\n= [(√3)² - 2(√3)(1) + 1²] / [(√3)² - (1)²]\n= (3 - 2√3 + 1) / (3 - 1)\n= (4 - 2√3) / 2\n= 2 - √3\n\nNow equate with a + b√3:\n2 - 1√3 = a + b√3\nComparing rational and irrational parts:\na = 2 and b = -1.",
                'options' => [
                    ['name' => 'a = 2, b = −1', 'is_correct' => 1],
                    ['name' => 'a = 2, b = 1', 'is_correct' => 0],
                    ['name' => 'a = −2, b = 1', 'is_correct' => 0],
                    ['name' => 'a = 1, b = −2', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The simplified value of √8 + √18 − √32 is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Simplification of radicals and operations on real numbers.',
                'hint' => 'Express each radical in terms of √2: √8 = √(4 × 2), √18 = √(9 × 2), and √32 = √(16 × 2).',
                'solution' => "Simplify each square root term:\n√8 = √(4 × 2) = 2√2\n√18 = √(9 × 2) = 3√2\n√32 = √(16 × 2) = 4√2\n\nCombine the like radicals:\n√8 + √18 - √32 = 2√2 + 3√2 - 4√2\n= (2 + 3 - 4)√2\n= 1√2 = √2.",
                'options' => [
                    ['name' => '√2', 'is_correct' => 1],
                    ['name' => '2√2', 'is_correct' => 0],
                    ['name' => '√6', 'is_correct' => 0],
                    ['name' => '0', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of 11^(1/2) / 11^(1/4) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Laws of exponents for division of powers with identical bases.',
                'hint' => 'Apply the quotient law of exponents: a^m / a^n = a^(m − n).',
                'solution' => "Using the quotient law of exponents:\na^m / a^n = a^(m - n)\n\nHere a = 11, m = 1/2, n = 1/4:\n11^(1/2) / 11^(1/4) = 11^(1/2 - 1/4)\n\nCompute the exponent:\n1/2 - 1/4 = 2/4 - 1/4 = 1/4\n\nTherefore:\n11^(1/2) / 11^(1/4) = 11^(1/4).",
                'options' => [
                    ['name' => '11^(1/4)', 'is_correct' => 1],
                    ['name' => '11^(1/8)', 'is_correct' => 0],
                    ['name' => '11^(3/4)', 'is_correct' => 0],
                    ['name' => '1', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of 7^(1/2) · 8^(1/2) is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Laws of exponents for multiplying powers with different bases and equal exponents.',
                'hint' => 'Use the power of a product rule: a^p · b^p = (ab)^p.',
                'solution' => "According to the laws of exponents:\na^p · b^p = (a · b)^p\n\nHere a = 7, b = 8, and p = 1/2:\n7^(1/2) · 8^(1/2) = (7 × 8)^(1/2) = (56)^(1/2).",
                'options' => [
                    ['name' => '(56)^(1/2)', 'is_correct' => 1],
                    ['name' => '(15)^(1/2)', 'is_correct' => 0],
                    ['name' => '(56)^(1/4)', 'is_correct' => 0],
                    ['name' => '56', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'If x = 2 + √3, then the value of x + 1/x is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Reciprocal of binomial surds and symmetric expressions.',
                'hint' => 'First compute 1/x by rationalising: 1 / (2 + √3) = (2 − √3) / [2² − (√3)²] = 2 − √3.',
                'solution' => "Given x = 2 + √3.\n\nCalculate 1/x by rationalising the denominator:\n1/x = 1 / (2 + √3)\n= [1 × (2 - √3)] / [(2 + √3)(2 - √3)]\n= (2 - √3) / (2² - (√3)²)\n= (2 - √3) / (4 - 3)\n= 2 - √3\n\nNow calculate x + 1/x:\nx + 1/x = (2 + √3) + (2 - √3)\n= 2 + 2\n= 4.",
                'options' => [
                    ['name' => '4', 'is_correct' => 1],
                    ['name' => '2√3', 'is_correct' => 0],
                    ['name' => '−4', 'is_correct' => 0],
                    ['name' => '2', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The value of ∜(∛(2²)) is equal to:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Nested radicals and fractional exponent laws.',
                'hint' => 'Express the cube root and fourth root as powers of 1/3 and 1/4, then multiply the exponents: ((2²)^(1/3))^(1/4).',
                'solution' => "Rewrite nested radical in fractional exponent notation:\n∛(2²) = (2²)^(1/3) = 2^(2/3)\n\nNow apply the fourth root:\n∜(∛(2²)) = (2^(2/3))^(1/4)\n= 2^((2/3) × (1/4))\n= 2^(2/12)\n= 2^(1/6).",
                'options' => [
                    ['name' => '2^(1/6)', 'is_correct' => 1],
                    ['name' => '2^(1/12)', 'is_correct' => 0],
                    ['name' => '2^(6)', 'is_correct' => 0],
                    ['name' => '2^(1/24)', 'is_correct' => 0],
                ],
            ],
            [
                'name' => 'The product of two irrational numbers is:',
                'description' => 'CBSE Class 9 Mathematics - Unit I: Number System. Properties and closure of irrational numbers under arithmetic operations.',
                'hint' => 'Test with examples: √2 × √2 = 2 (rational), while √2 × √3 = √6 (irrational).',
                'solution' => "The product of two irrational numbers can be either rational or irrational (sometimes rational, sometimes irrational).\n\nExamples:\n1) √3 × √3 = 3 (rational)\n2) √2 × √5 = √10 (irrational)\n\nHence, the product is sometimes rational, sometimes irrational.",
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
                'created_by' => 2, // Admin
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

            $this->command->info("Created CBSE Exam MCQ Question #{$question->id}: {$question->name}");
        }
    }
}

<?php

namespace Database\Seeders;

use App\Models\Answer;
use App\Models\Question;
use App\Models\Standard;
use App\Models\User;
use Illuminate\Database\Seeder;

class QuestionSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $standards = Standard::pluck('id')->toArray();
        if (empty($standards)) {
            $standards = [1];
        }

        $teachers = User::whereIn('id', [10, 11, 12, 81])->pluck('id')->toArray();
        if (empty($teachers)) {
            $teachers = [User::first()->id ?? 1];
        }

        $templates = [
            // Math
            [
                'q' => 'What is the square root of %d?',
                'generator' => function () {
                    $val = rand(2, 25);
                    $sq = $val * $val;
                    $wrong = array_unique([$val + rand(1, 3), max(1, $val - rand(1, 3)), $val + rand(4, 7)]);
                    while (count($wrong) < 3) {
                        $wrong[] = $val + rand(8, 15);
                        $wrong = array_unique($wrong);
                    }

                    return [
                        'q' => "What is the square root of {$sq}?",
                        'desc' => "Calculate the square root of the given perfect square number {$sq}.",
                        'correct' => (string) $val,
                        'wrong' => array_map('strval', array_slice($wrong, 0, 3)),
                    ];
                },
            ],
            [
                'q' => 'Solve for x: %dx + %d = %d',
                'generator' => function () {
                    $a = rand(2, 9);
                    $x = rand(1, 12);
                    $b = rand(1, 20);
                    $c = ($a * $x) + $b;
                    $wrong = [$x + 1, max(0, $x - 1), $x + 2];

                    return [
                        'q' => "Solve for x: {$a}x + {$b} = {$c}",
                        'desc' => "Find the value of x that satisfies the linear equation {$a}x + {$b} = {$c}.",
                        'correct' => (string) $x,
                        'wrong' => array_map('strval', $wrong),
                    ];
                },
            ],
            [
                'q' => 'What is the area of a rectangle with length %d cm and width %d cm?',
                'generator' => function () {
                    $l = rand(5, 20);
                    $w = rand(3, 15);
                    $area = $l * $w;
                    $wrong = [$area + $l, $area - $w, ($l + $w) * 2];

                    return [
                        'q' => "What is the area of a rectangle with length {$l} cm and width {$w} cm?",
                        'desc' => 'Apply the rectangle area formula (Area = length × width).',
                        'correct' => "{$area} sq cm",
                        'wrong' => [$wrong[0].' sq cm', $wrong[1].' sq cm', $wrong[2].' cm'],
                    ];
                },
            ],
            // Science
            [
                'q' => 'Which element has the chemical symbol %s?',
                'generator' => function () {
                    $elements = [
                        ['Au', 'Gold', ['Silver', 'Copper', 'Aluminum']],
                        ['Fe', 'Iron', ['Lead', 'Zinc', 'Tin']],
                        ['Na', 'Sodium', ['Nitrogen', 'Nickel', 'Neodymium']],
                        ['K', 'Potassium', ['Krypton', 'Phosphorus', 'Calcium']],
                        ['O', 'Oxygen', ['Osmium', 'Oganesson', 'Hydrogen']],
                        ['H', 'Hydrogen', ['Helium', 'Mercury', 'Lithium']],
                        ['Pb', 'Lead', ['Plutonium', 'Platinum', 'Phosphorus']],
                        ['Hg', 'Mercury', ['Hydragyrum', 'Magnesium', 'Silver']],
                        ['Ag', 'Silver', ['Gold', 'Argon', 'Arsenic']],
                        ['Cu', 'Copper', ['Cobalt', 'Curium', 'Calcium']],
                    ];
                    $pick = $elements[array_rand($elements)];

                    return [
                        'q' => "Which chemical element has the symbol '{$pick[0]}'?",
                        'desc' => "Identify the correct chemical element associated with symbol {$pick[0]}.",
                        'correct' => $pick[1],
                        'wrong' => $pick[2],
                    ];
                },
            ],
            [
                'q' => 'What is the primary function of %s in living cells?',
                'generator' => function () {
                    $organelles = [
                        ['Mitochondria', 'Cellular respiration & energy production (ATP)', ['Protein synthesis', 'DNA storage', 'Waste removal']],
                        ['Ribosomes', 'Protein synthesis', ['Lipid storage', 'Energy generation', 'Cell division']],
                        ['Nucleus', 'Storing genetic material (DNA)', ['Photosynthesis', 'Cellular locomotion', 'Protein digestion']],
                        ['Chloroplasts', 'Photosynthesis in plant cells', ['Cell respiration', 'Lipid synthesis', 'Storage of water']],
                        ['Cell Membrane', 'Regulating transport of substances in & out of the cell', ['Energy production', 'Protein packaging', 'DNA replication']],
                    ];
                    $pick = $organelles[array_rand($organelles)];

                    return [
                        'q' => "What is the primary function of {$pick[0]} in a cell?",
                        'desc' => "Select the primary biological function of {$pick[0]}.",
                        'correct' => $pick[1],
                        'wrong' => $pick[2],
                    ];
                },
            ],
            // General Knowledge & Geography
            [
                'q' => 'What is the capital city of %s?',
                'generator' => function () {
                    $countries = [
                        ['France', 'Paris', ['Lyon', 'Marseille', 'Nice']],
                        ['Japan', 'Tokyo', ['Kyoto', 'Osaka', 'Hiroshima']],
                        ['Australia', 'Canberra', ['Sydney', 'Melbourne', 'Brisbane']],
                        ['Canada', 'Ottawa', ['Toronto', 'Vancouver', 'Montreal']],
                        ['Germany', 'Berlin', ['Munich', 'Frankfurt', 'Hamburg']],
                        ['India', 'New Delhi', ['Mumbai', 'Kolkata', 'Bangalore']],
                        ['Brazil', 'Brasília', ['Rio de Janeiro', 'São Paulo', 'Salvador']],
                        ['Italy', 'Rome', ['Milan', 'Venice', 'Naples']],
                        ['Egypt', 'Cairo', ['Alexandria', 'Giza', 'Luxor']],
                        ['Spain', 'Madrid', ['Barcelona', 'Seville', 'Valencia']],
                    ];
                    $pick = $countries[array_rand($countries)];

                    return [
                        'q' => "What is the capital city of {$pick[0]}?",
                        'desc' => "Identify the official capital city of {$pick[0]}.",
                        'correct' => $pick[1],
                        'wrong' => $pick[2],
                    ];
                },
            ],
            // Computer Science
            [
                'q' => 'In computer programming, what does %s stand for?',
                'generator' => function () {
                    $acronyms = [
                        ['HTML', 'HyperText Markup Language', ['HighText Machine Language', 'HyperTransfer Mode Language', 'Hybrid Text Markup Logic']],
                        ['CSS', 'Cascading Style Sheets', ['Computer Style Sheets', 'Creative Sheet System', 'Centralized Style Structure']],
                        ['SQL', 'Structured Query Language', ['Standard Question Logic', 'Simple Query Layout', 'Sequential Query List']],
                        ['RAM', 'Random Access Memory', ['Read Access Memory', 'Rapid Action Module', 'Run Architecture Memory']],
                        ['CPU', 'Central Processing Unit', ['Control Processing Unit', 'Central Power Unit', 'Core Programming Unit']],
                        ['URL', 'Uniform Resource Locator', ['Universal Resource Link', 'Unified Register Location', 'User Redirect Link']],
                        ['API', 'Application Programming Interface', ['Automated Program Integration', 'Applied Process Interaction', 'Application Protocol Index']],
                    ];
                    $pick = $acronyms[array_rand($acronyms)];

                    return [
                        'q' => "What does the abbreviation '{$pick[0]}' stand for?",
                        'desc' => "Select the correct full expansion of the technical term {$pick[0]}.",
                        'correct' => $pick[1],
                        'wrong' => $pick[2],
                    ];
                },
            ],
            // English / Grammar
            [
                'q' => 'Which word is a synonym for %s?',
                'generator' => function () {
                    $synonyms = [
                        ['Abundant', 'Plentiful', ['Scarce', 'Tiny', 'Deficient']],
                        ['Benevolent', 'Kind', ['Cruel', 'Greedy', 'Arrogant']],
                        ['Candid', 'Honest', ['Deceitful', 'Shy', 'Complicated']],
                        ['Diligent', 'Hardworking', ['Lazy', 'Careless', 'Indifferent']],
                        ['Eloquent', 'Persuasive', ['Unclear', 'Silent', 'Awkward']],
                        ['Frugal', 'Economical', ['Wasteful', 'Extravagant', 'Generous']],
                    ];
                    $pick = $synonyms[array_rand($synonyms)];

                    return [
                        'q' => "Which of the following is a synonym for '{$pick[0]}'?",
                        'desc' => "Choose the word closest in meaning to '{$pick[0]}'.",
                        'correct' => $pick[1],
                        'wrong' => $pick[2],
                    ];
                },
            ],
        ];

        $createdCount = 0;

        for ($i = 1; $i <= 100; $i++) {
            $tmpl = $templates[array_rand($templates)];
            $data = ($tmpl['generator'])();

            $stdId = $standards[array_rand($standards)];
            $creatorId = $teachers[array_rand($teachers)];
            $marks = rand(1, 5);

            $question = Question::create([
                'name' => "Q{$i}: ".$data['q'],
                'description' => $data['desc'],
                'standard_id' => $stdId,
                'type' => 1, // Multiple Choice
                'created_by' => $creatorId,
                'marks' => $marks,
                'status' => 1,
            ]);

            // Options: 1 correct answer + 3 wrong answers
            $options = [];
            $options[] = ['name' => $data['correct'], 'is_correct' => 1];
            foreach ($data['wrong'] as $w) {
                $options[] = ['name' => $w, 'is_correct' => 0];
            }
            shuffle($options);

            foreach ($options as $opt) {
                Answer::create([
                    'question_id' => $question->id,
                    'name' => $opt['name'],
                    'is_correct' => $opt['is_correct'],
                    'status' => 1,
                ]);
            }

            $createdCount++;
        }

        $this->command->info("Successfully seeded {$createdCount} questions into the database.");
    }
}

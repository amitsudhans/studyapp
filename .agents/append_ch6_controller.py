with open("app/Http/Controllers/MultimediaController.php", "r", encoding="utf-8") as f:
    text = f.read()

target = """                        'Heritage Geometry: Acharya Baudhayana\\'s Vedic Cord & Peg (Sanku-Rajju) Altars',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

ch6_code = """                        'Heritage Geometry: Acharya Baudhayana\\'s Vedic Cord & Peg (Sanku-Rajju) Altars',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                [
                    'chapter_num' => 6,
                    'name' => 'Number Play',
                    'has_multimedia' => true,
                    'media_key' => 'class7-math-number-play',
                    'media_title' => 'NCERT Class 7 Mathematics • Chapter 6 • Number Play Master Lab',
                    'media_url' => asset('animations/class7-math-number-play.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 7 Mathematics Chapter 6: Number Play with animated mentor avatar Acharya Virahāńka (Pioneer of Indian Combinatorics & Rhythmic Number Sequences), Web Speech API narration, and 16 bespoke SVG laboratory simulators covering Positional Deduction (height queue line-up decoder, inversion sequences, and stepwise elimination), Picking Parity (geometry of even and odd numbers, dot-pair matching, lonely remainder dots), Parity Arithmetic Laws (algebraic proofs of Even + Even = Even, Odd + Odd = Even, Even + Odd = Odd, and multiplication rules), Grid Parity & Checkerboard Coloring (the famous mutilated chessboard domino tiling impossibility proof), Algebraic Parity & Collatz 3n+1 loop, Explorations in Grids (magic square basics, magic constant derivation S=15 for 3x3 grids), The Golden Center Cell Rule (proof that center C = S/3 = 5 and 8 rotational/reflection symmetries), The Chautīsa Yantra (Khajuraho temple 4x4 magic square summing to 34 in 16 distinct sub-patterns), Virahāńka-Fibonacci Numbers (origins in Pingala and Virahāńka\\'s poetic prosody with Laghu and Guru beats), The Recurrence Machine (Fn = Fn-1 + Fn-2 and golden ratio 1.618 convergence), Botanical Petal Counts & Sunflower Interlocking Spirals (21/34 phyllotaxis), Virahāńka Parity Rhythm (proof that every 3rd term is even), Digits in Disguise (cryptarithms and alphametics, carryover rules, AB + B = BC), Solving SEND + MORE = MONEY (stepwise logical deduction of all 8 letters), Heritage of Indian Combinatorics (Pingala\\'s Meru Prastara binomial pyramid and Narayana Pandita\\'s Bhadra Ganita), 32 interactive checkpoints, and 4 dedicated mastery quiz challenge slides (40 questions) with step-by-step pop-up solution derivations.',
                    'topics' => [
                        'Numbers Tell us Things: Positional Logic & The Height Queue Decoder',
                        'Deductive Elimination: Reconstructing Hidden Line-Up Permutations',
                        'Picking Parity: The Geometry of Even & Odd Numbers (Pair-Matching)',
                        'The Universal Arithmetic Laws of Parity: Addition & Multiplication',
                        'Grid Parity: Checkerboard Coloring & The Mutilated Chessboard Dilemma',
                        'Algebraic Parity Sequences: General nth Terms ($2k, 2k+1$) & Collatz $3n+1$',
                        'Explorations in Grids: The 3x3 Magic Square & Magic Constant ($S = 15$)',
                        'The Golden Center Rule: Proof that Center Cell $C = S / 3 = 5$',
                        'Symmetry in Grids: The 8 Rotations and Reflections of the Lo Shu Square',
                        'Ancient Indian Yantras: The Chautīsa Yantra of Khajuraho (Magic Sum 34)',
                        'Pandiagonal Harmony: 16 Unique Sub-Patterns of 4 Numbers Summing to 34',
                        'Poetic Syllable Origins: Pingala & Virahāńka\\'s Prosody Beats ($1, 2, 3, 5, 8\\\\dots$)',
                        'The Additive Machine: Recurrence Relation ($F_n = F_{n-1} + F_{n-2}$) & Golden Ratio ($\\\\Phi$)',
                        'Virahāńka Numbers in Nature: Flower Petal Counts & Sunflower Seed Spirals',
                        'The Parity Rhythm: Why Every 3rd Virahāńka Number is Strictly Even',
                        'Digits in Disguise: Cryptarithms, Unique Digit Rules & Column Carryovers',
                        'Master Alphametic Deduction: Solving $SEND + MORE = MONEY$ Step-by-Step',
                        'Heritage Combinatorics: Pingala\\'s Meru Prastara & Narayana Pandita\\'s Bhadra Ganita',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

assert target in text, "target not found in MultimediaController.php"
text = text.replace(target, ch6_code, 1)

with open("app/Http/Controllers/MultimediaController.php", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully appended Chapter 6 to MultimediaController.php")

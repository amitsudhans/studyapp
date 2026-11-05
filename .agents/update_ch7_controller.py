# -*- coding: utf-8 -*-
with open('app/Http/Controllers/MultimediaController.php', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''                        'Fencing Garden Perimeter: Fixed-Perimeter (20m) Vegetable Beds & Rectangular Geometry',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Mathematics Class 5'''

replacement = '''                        'Fencing Garden Perimeter: Fixed-Perimeter (20m) Vegetable Beds & Rectangular Geometry',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                [
                    'chapter_num' => 7,
                    'name' => 'The Cleanest Village',
                    'has_multimedia' => true,
                    'media_key' => 'class4-maths-the-cleanest-village',
                    'media_title' => 'NCERT Class 4 Mathematics • Chapter 7 • The Cleanest Village Master Lab',
                    'media_url' => asset('animations/class4-maths-the-cleanest-village.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 4 Mathematics Chapter 7: The Cleanest Village (Joyful Mathematics, NEP 2020) featuring spoken classroom audio lectures in authentic Indian English male teacher narration, Web Speech API integration, and 16 bespoke SVG/HTML interactive simulators covering Village Trip Logistics (Mawlynnong field trip poster data analysis, 9-hour travel timetable, 77 families, 414 residents), Market Cart Pricing (per-kg unit rates for beans ₹95, potatoes ₹37, onions ₹32, radishes ₹23, yams ₹45, bananas ₹55), Total Cost Calculations (multi-item shopping combinations, target ₹163 grocery basket assembly), Grocery Balance Math (tendering ₹100 note for ₹64 bill, open number line counting-up strategy, currency note optimization), Orange Purchase Denominations (two oranges at ₹21 each = ₹42 fixed bill, comparing change across ₹50, ₹100, ₹200, and ₹500 tenders), Triangle Magic Sums (combinatorial number placement 1 to 6 along triangle sides to achieve target sums 9, 10, and 12), Base Ten Addition (Dienes blocks concrete bundling: 10 Ones regroup into 1 Ten rod, 10 Tens into 1 Hundred flat), Field Trip Totals (multi-digit column addition with carries: 24 + 28 = 52 staff, 438 + 476 = 914 students), Traditional Snack Expenses (Khasi red rice pusaw steamed cakes ₹38 + spiced tea ₹16 = ₹54, piggy bank savings ₹185 + ₹125 = ₹310), Snack Choice Differences (comparative subtraction: 83 pusaw cakes vs 46 fruit plates, unbundling 1 Ten into 10 Ones to find 37 difference), Regrouping In Subtraction (step-by-step column subtraction with double borrowing: 324 - 176 = 148), Travel Spend Balances (spend-down budget accounting: starting with ₹310 and remaining with ₹179 = ₹131 spent, orchard mango harvest difference), Train Passenger Tracking (sequential multi-station tracking across New Delhi, Dadri, Ghaziabad, and Aligarh junctions), Mental Math Shortcuts (near-tens adjustments: 356 + 99 = 455, 280 - 49 = 231, expanded addition 45 + 32 = 77), Number Target Equations (decomposing target sum 856 and target difference 563 into multiple equivalent expressions), and Number Grid Pairs (analyzing 4×4 spatial matrix for greatest adjacent sum 87 + 94 = 181, smallest adjacent difference 55 - 52 = 3, missing digit logic), plus 32 in-slide checkpoints and 4 dedicated mastery quiz challenge slides with 40 questions and step-by-step solution modals.',
                    'topics' => [
                        'Village Trip Logistics: Field Trip Context, 9-Hour Travel Timetable & Poster Analysis',
                        'Market Cart Pricing: Per-Kilogram Unit Rates for Mountain Produce & Fruits',
                        'Total Cost Calculations: Multi-Step Combinations & Assembling Target ₹163 Bills',
                        'Grocery Balance Math: Cash Registers, Open Number Line Upward Counting & Change Optimization',
                        'Orange Purchase Denominations: Fixed ₹42 Bills Across Varied Currency Banknotes',
                        'Triangle Magic Sums: Combinatorial Digit Placement (1 to 6) for Side Sums 9, 10 & 12',
                        'Base Ten Addition: Physical Dienes Blocks Regrouping (10 Ones to 1 Ten Rod)',
                        'Field Trip Totals: Multi-Digit Column Addition with Regrouping Carries (52 & 914)',
                        'Traditional Snack Expenses: Khasi Red Rice Pusaw Cakes, Tea Bills & Piggy Bank Additions',
                        'Snack Choice Differences: Comparative Subtraction & Unbundling Tens (83 - 46 = 37)',
                        'Regrouping In Subtraction: Decomposing Tens & Hundreds in 3-Digit Column Subtraction (148)',
                        'Travel Spend Balances: Spend-Down Daily Budget Accounting & Crop Yield Comparisons',
                        'Train Passenger Tracking: Sequential Station Boarding & Alighting Multi-Step Arithmetic',
                        'Mental Math Shortcuts: Compensation Strategies for Near-Tens & Near-Hundreds (+99, -49)',
                        'Number Target Equations: Decomposing Target Sums (856) & Invariant Differences (563)',
                        'Number Grid Pairs: 4×4 Spatial Matrix Analysis & Backward Inverse Missing Digit Logic',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Mathematics Class 5'''

assert target in content, 'Target not found in MultimediaController.php!'
content = content.replace(target, replacement, 1)

with open('app/Http/Controllers/MultimediaController.php', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully inserted Chapter 7 into MultimediaController.php')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 10: Proportional Reasoning-2
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Maps Multi Terms",
        "subtitle": "Challenge Arena 1 (10 MCQs): Section 3.1–3.3 Scaling, Cross-Multiplication, RF Maps & Multi-Term Proportions",
        "questions": [
            {
                "question": "Which test confirms that ratios 9 : 15 and 21 : 35 are truly proportional?",
                "options": [
                    "9 × 35 = 315 equals 15 × 21 = 315",
                    "15 − 9 = 6 equals 35 − 21 = 14",
                    "9 + 15 = 24 equals 21 + 35 = 56",
                    "9 × 21 = 189"
                ],
                "answer": 0,
                "hint": "Compare outer product a × d against inner product b × c!",
                "explanation": "9 × 35 = 315 = 15 × 21 confirms 9 : 15 :: 21 : 35 (both reduce to 3 : 5).",
                "solution_steps": [
                    "Write cross-multiplication rule: a × d = b × c.",
                    "Compute a × d = 9 × 35 = 315.",
                    "Compute b × c = 15 × 21 = 315 → equal products prove proportion."
                ]
            },
            {
                "question": "An idli batter recipe mixes 4 cups rice to 1.5 cups urad dal. Using 12 cups of rice, how many cups of urad dal are needed?",
                "options": [
                    "4.5 cups",
                    "9.5 cups",
                    "3.5 cups",
                    "6 cups"
                ],
                "answer": 0,
                "hint": "Find scaling factor from rice: 12 ÷ 4 = 3! Multiply 1.5 by 3!",
                "explanation": "Scaling factor = 12 ÷ 4 = 3 → 1.5 × 3 = 4.5 cups urad dal.",
                "solution_steps": [
                    "Determine scaling multiplier: 12 ÷ 4 = 3.",
                    "Scale urad dal by identical factor 3: 1.5 × 3 = 4.5.",
                    "Verify cross-product: 4 × 4.5 = 18 = 1.5 × 12."
                ]
            },
            {
                "question": "A map carries Representative Fraction (RF) 1 : 50,00,000. How many real kilometres does 1 cm on this map represent?",
                "options": [
                    "50 km",
                    "5 km",
                    "500 km",
                    "5,000 km"
                ],
                "answer": 0,
                "hint": "Divide 50,00,000 cm by 1,00,000 cm/km!",
                "explanation": "50,00,000 cm ÷ 100 cm/m ÷ 1,000 m/km = 50 km per map cm.",
                "solution_steps": [
                    "1 cm on map = 50,00,000 cm on ground.",
                    "Convert cm to metres (÷ 100) = 50,000 m.",
                    "Convert m to kilometres (÷ 1,000) = 50 km."
                ]
            },
            {
                "question": "On an atlas map with scale 1 cm = 60 km, two cities lie 6.5 cm apart. What is the actual straight-line aerial distance between them?",
                "options": [
                    "390 km",
                    "360 km",
                    "66.5 km",
                    "420 km"
                ],
                "answer": 0,
                "hint": "Multiply 6.5 cm × 60 km/cm!",
                "explanation": "6.5 × 60 = 390 km actual aerial distance.",
                "solution_steps": [
                    "Read ground rate: 1 cm → 60 km.",
                    "Multiply map separation 6.5 × 60.",
                    "6 × 60 + 0.5 × 60 = 360 + 30 = 390 km."
                ]
            },
            {
                "question": "A classroom floor plan uses a 1 : 50 scale. If the actual classroom length is 8 metres (800 cm), how long is it drawn on the plan?",
                "options": [
                    "16 cm",
                    "40 cm",
                    "8 cm",
                    "400 cm"
                ],
                "answer": 0,
                "hint": "Divide real length 800 cm by scale denominator 50!",
                "explanation": "800 cm ÷ 50 = 16 cm on the floor plan.",
                "solution_steps": [
                    "Convert real length to centimetres: 8 m = 800 cm.",
                    "Apply 1 : 50 scale: map length = 800 ÷ 50.",
                    "800 ÷ 50 = 16 cm."
                ]
            },
            {
                "question": "A spice mix recipe follows ratio 8 : 4 : 2 : 1 (coriander : cumin : pepper : cloves). If a chef uses 6 teaspoons of pepper, how many teaspoons of coriander are needed?",
                "options": [
                    "24 teaspoons",
                    "12 teaspoons",
                    "16 teaspoons",
                    "32 teaspoons"
                ],
                "answer": 0,
                "hint": "Pepper corresponds to term 2 → factor = 6 ÷ 2 = 3! Multiply coriander term 8 by 3!",
                "explanation": "Factor = 6 ÷ 2 = 3; coriander = 8 × 3 = 24 teaspoons.",
                "solution_steps": [
                    "Match pepper's ratio term: 2 parts → 6 tsp (multiplier = 3).",
                    "Scale coriander (8 parts) by × 3: 8 × 3 = 24 tsp.",
                    "Full scaled recipe = 24 : 12 : 6 : 3."
                ]
            },
            {
                "question": "Which multi-term proportion accurately equates 3 : 4 : 7 with a scaled set?",
                "options": [
                    "3 : 4 : 7 :: 15 : 20 : 35",
                    "3 : 4 : 7 :: 6 : 8 : 15",
                    "3 : 4 : 7 :: 8 : 9 : 12",
                    "3 : 4 : 7 :: 9 : 16 : 49"
                ],
                "answer": 0,
                "hint": "Check where a/p = b/q = c/r stays identical across ALL three terms!",
                "explanation": "3/15 = 4/20 = 7/35 = 1/5 (uniform scaling × 5).",
                "solution_steps": [
                    "Verify multi-term condition a/p = b/q = c/r.",
                    "Check Option 1: 15÷3 = 5, 20÷4 = 5, 35÷7 = 5.",
                    "All ratios share common multiplier 5."
                ]
            },
            {
                "question": "Reinforced concrete combines cement, sand, and gravel in ratio 1 : 1.5 : 3. If 18 bags of gravel are delivered, how many bags of sand should match?",
                "options": [
                    "9 bags of sand",
                    "6 bags of sand",
                    "12 bags of sand",
                    "15 bags of sand"
                ],
                "answer": 0,
                "hint": "Gravel term is 3 → 18 ÷ 3 = 6 multiplier! Multiply sand term 1.5 by 6!",
                "explanation": "Multiplier = 18 ÷ 3 = 6; sand = 1.5 × 6 = 9 bags (cement = 6 bags).",
                "solution_steps": [
                    "Find scaling multiplier from gravel: 18 ÷ 3 = 6.",
                    "Scale sand (1.5) by × 6: 1.5 × 6 = 9 bags.",
                    "Verify ratio: 6 : 9 : 18 simplifies back to 1 : 1.5 : 3."
                ]
            },
            {
                "question": "A paint shade mixes red, blue, and white in ratio 2 : 3 : 5. If 12 mL of red pigment is poured, how much TOTAL paint mixture results?",
                "options": [
                    "60 mL total   (12 + 18 + 30)",
                    "40 mL total",
                    "50 mL total",
                    "30 mL total"
                ],
                "answer": 0,
                "hint": "Red term 2 → 12 mL gives multiplier 6! Multiply total terms (2+3+5 = 10) by 6!",
                "explanation": "Multiplier = 12 ÷ 2 = 6; total = (2 + 3 + 5) × 6 = 60 mL.",
                "solution_steps": [
                    "Find factor from red: 12 ÷ 2 = 6.",
                    "Calculate blue = 3×6 = 18 mL, white = 5×6 = 30 mL.",
                    "Sum total paint = 12 + 18 + 30 = 60 mL."
                ]
            },
            {
                "question": "On a 1 : 25,000 trekking map, two trail camps are 12 cm apart on paper. What is their real distance in kilometres?",
                "options": [
                    "3 km",
                    "30 km",
                    "0.3 km",
                    "1.2 km"
                ],
                "answer": 0,
                "hint": "Multiply 12 cm × 25,000 = 3,00,000 cm, then divide by 1,00,000 cm/km!",
                "explanation": "12 × 25,000 = 3,00,000 cm = 3,000 m = 3 km.",
                "solution_steps": [
                    "Multiply map length by scale: 12 × 25,000 = 300,000 cm.",
                    "Convert cm to metres: 300,000 ÷ 100 = 3,000 m.",
                    "Convert m to km: 3,000 ÷ 1,000 = 3 km."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Partitioning Pie Charts",
        "subtitle": "Challenge Arena 2 (10 MCQs): Section 3.4–3.5 Partitioning Formula, Coins, Triangles & Pie Chart Angles",
        "questions": [
            {
                "question": "Mix 50 mL of shade paint using ratio 2 : 3 : 5 (red : blue : white). How much white paint is required?",
                "options": [
                    "25 mL",
                    "15 mL",
                    "10 mL",
                    "30 mL"
                ],
                "answer": 0,
                "hint": "Sum of terms = 2 + 3 + 5 = 10; white fraction = 5/10 of 50 mL!",
                "explanation": "50 × (5 / 10) = 25 mL white paint.",
                "solution_steps": [
                    "Add ratio terms: 2 + 3 + 5 = 10 parts.",
                    "Value per part = 50 ÷ 10 = 5 mL.",
                    "White share = 5 × 5 = 25 mL."
                ]
            },
            {
                "question": "A school cricket academy divides a 150-minute training session into warm-up, nets, and fielding in the ratio 1 : 3 : 1. How long is spent on nets?",
                "options": [
                    "90 minutes",
                    "30 minutes",
                    "60 minutes",
                    "75 minutes"
                ],
                "answer": 0,
                "hint": "Sum = 1 + 3 + 1 = 5 parts; nets take 3/5 of 150 minutes!",
                "explanation": "150 × (3 / 5) = 90 minutes.",
                "solution_steps": [
                    "Compute total parts: 1 + 3 + 1 = 5.",
                    "One part = 150 ÷ 5 = 30 minutes.",
                    "Nets (3 parts) = 3 × 30 = 90 minutes."
                ]
            },
            {
                "question": "A school library stocks 540 storybooks across Hindi, English, and Tamil in the ratio 4 : 3 : 2. How many Hindi books are there?",
                "options": [
                    "240 Hindi books",
                    "180 Hindi books",
                    "120 Hindi books",
                    "270 Hindi books"
                ],
                "answer": 0,
                "hint": "Sum = 4 + 3 + 2 = 9 parts; Hindi gets 4/9 of 540!",
                "explanation": "540 ÷ 9 = 60 books per part → Hindi = 4 × 60 = 240 books.",
                "solution_steps": [
                    "Sum ratio terms: 4 + 3 + 2 = 9.",
                    "Find 1 part: 540 ÷ 9 = 60 books.",
                    "Multiply for Hindi (4 parts): 4 × 60 = 240 books."
                ]
            },
            {
                "question": "A jar contains ₹1, ₹2, and ₹5 coins whose COUNTS stand in ratio 2 : 3 : 2, totaling ₹90. How many ₹2 coins are inside?",
                "options": [
                    "15 coins of ₹2   (k = 5 → 3×5 = 15)",
                    "10 coins of ₹2",
                    "30 coins of ₹2",
                    "5 coins of ₹2"
                ],
                "answer": 0,
                "hint": "Value = 1(2k) + 2(3k) + 5(2k) = 18k = 90 → find k first!",
                "explanation": "2k + 6k + 10k = 18k = ₹90 → k = 5 → ₹2 coin count = 3k = 15.",
                "solution_steps": [
                    "Express rupee values: ₹1×(2k) + ₹2×(3k) + ₹5×(2k) = 2k + 6k + 10k = 18k.",
                    "Equate total to ₹90: 18k = 90 → k = 5.",
                    "Calculate ₹2 coin count: 3 × 5 = 15 coins."
                ]
            },
            {
                "question": "Which triangle angle ratio divides 180° into 36°, 54°, and 90°?",
                "options": [
                    "2 : 3 : 5",
                    "1 : 2 : 3",
                    "1 : 3 : 5",
                    "3 : 4 : 5"
                ],
                "answer": 0,
                "hint": "Divide 36, 54, and 90 cleanly by HCF(36, 54, 90) = 18!",
                "explanation": "36÷18 : 54÷18 : 90÷18 = 2 : 3 : 5.",
                "solution_steps": [
                    "Find HCF(36, 54, 90) = 18.",
                    "Divide each angle by 18: 36/18 = 2, 54/18 = 3, 90/18 = 5.",
                    "Simplest ratio = 2 : 3 : 5."
                ]
            },
            {
                "question": "Which side-length ratio CANNOT form any valid closed triangle?",
                "options": [
                    "2 : 3 : 7",
                    "3 : 4 : 5",
                    "5 : 6 : 9",
                    "4 : 4 : 5"
                ],
                "answer": 0,
                "hint": "Apply the triangle inequality: two smaller sides summed must EXCEED the largest side!",
                "explanation": "2 + 3 = 5 < 7 violates the triangle inequality, so no closed triangle can form.",
                "solution_steps": [
                    "Test Option 1: 2 + 3 = 5.",
                    "Compare sum 5 with longest side 7: 5 < 7 (fails!).",
                    "All other triples satisfy a + b > c."
                ]
            },
            {
                "question": "In NCERT's Grades A–E pie chart example (frequencies 12, 10, 8, 6, 4 out of 40), what central angle represents Grade C (frequency 8)?",
                "options": [
                    "72°",
                    "90°",
                    "54°",
                    "108°"
                ],
                "answer": 0,
                "hint": "Compute (8 / 40) × 360° = (1/5) × 360°!",
                "explanation": "(8 / 40) × 360° = 72°.",
                "solution_steps": [
                    "Form fraction for Grade C: 8 / 40 = 1 / 5.",
                    "Multiply by full circle 360°: (1/5) × 360°.",
                    "Result = 72°."
                ]
            },
            {
                "question": "A seasonal preference survey of 120 students gets 45 votes for Winter, 45 for Monsoon, and 30 for Summer. What central angle shows Summer on a pie chart?",
                "options": [
                    "90°   ((30 / 120) × 360° = 90°)",
                    "135°",
                    "60°",
                    "120°"
                ],
                "answer": 0,
                "hint": "30 out of 120 simplifies to 1/4!",
                "explanation": "(30 / 120) × 360° = (1/4) × 360° = 90°.",
                "solution_steps": [
                    "Simplify Summer fraction: 30 / 120 = 1 / 4.",
                    "Multiply by 360°: 360° ÷ 4 = 90°.",
                    "Winter & Monsoon take 135° each (135+135+90 = 360°)."
                ]
            },
            {
                "question": "A TV channel category pie chart shows News at 54°. What percentage of viewers watch News?",
                "options": [
                    "15%",
                    "18%",
                    "20%",
                    "12%"
                ],
                "answer": 0,
                "hint": "Divide 54° by 360° and multiply by 100%!",
                "explanation": "(54 / 360) × 100% = (3 / 20) × 100% = 15%.",
                "solution_steps": [
                    "Form sector fraction: 54° / 360°.",
                    "Simplify dividing by 18: 3 / 20.",
                    "Convert to percentage: (3/20) × 100% = 15%."
                ]
            },
            {
                "question": "In a subject popularity survey of 90 students, 15 chose History. What simplified ratio unit does History hold if HCF = 15?",
                "options": [
                    "1 part out of 6 total (60° slice)",
                    "1 part out of 5 total (72° slice)",
                    "2 parts out of 9 total (80° slice)",
                    "1 part out of 4 total (90° slice)"
                ],
                "answer": 0,
                "hint": "Divide both 15 and 90 by HCF = 15!",
                "explanation": "15 / 90 = 1 / 6 of the class → (1/6) × 360° = 60° sector.",
                "solution_steps": [
                    "Divide 15 and total 90 by 15 → fraction = 1/6.",
                    "Calculate angle: (1/6) × 360° = 60°.",
                    "Select 1 out of 6 (60°)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Inverse Variation Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Section 3.6 Direct vs Inverse, x·y = k, Speed-Time, Workforce & Food Provisions",
        "questions": [
            {
                "question": "When variable x is multiplied by factor n = 4 in an INVERSE proportion, by what factor does partner variable y change?",
                "options": [
                    "1/4   (the reciprocal factor 1/n)",
                    "4",
                    "1/2",
                    "−4"
                ],
                "answer": 0,
                "hint": "To keep product x · y unchanged, scaling x by n scales y by 1/n!",
                "explanation": "(4x) · (y/4) = x · y preserves constant product k.",
                "solution_steps": [
                    "Recall inverse law: x · y = k.",
                    "Substitute new x' = 4x into x' · y' = k.",
                    "Solve y' = k / (4x) = (1/4)y."
                ]
            },
            {
                "question": "A car drives between two cities at 45 km/h taking 4 hours. How long does the same trip take at 60 km/h?",
                "options": [
                    "3 hours",
                    "5.33 hours",
                    "2.5 hours",
                    "3.5 hours"
                ],
                "answer": 0,
                "hint": "Constant distance = 45 × 4 = 180 km; divide 180 by 60!",
                "explanation": "45 × 4 = 60 × t₂ → t₂ = 180 ÷ 60 = 3 hours.",
                "solution_steps": [
                    "Compute fixed distance D = 45 × 4 = 180 km.",
                    "Set up s₂t₂ = D: 60 × t₂ = 180.",
                    "Divide: t₂ = 180 ÷ 60 = 3 hours."
                ]
            },
            {
                "question": "Fifteen construction workers finish a bridge repair in 12 days. How many days would 20 workers take working at the same rate?",
                "options": [
                    "9 days",
                    "16 days",
                    "10 days",
                    "8 days"
                ],
                "answer": 0,
                "hint": "Constant worker-days = 15 × 12 = 180; divide 180 by 20!",
                "explanation": "15 × 12 = 20 × d₂ → 180 ÷ 20 = 9 days.",
                "solution_steps": [
                    "Calculate total workload: 15 × 12 = 180 worker-days.",
                    "Divide across 20 workers: 180 ÷ 20.",
                    "Time = 9 days."
                ]
            },
            {
                "question": "A camp stores food provisions for 50 scouts lasting 24 days. Before starting, 10 MORE scouts join (total 60 scouts). How many days will the original food last?",
                "options": [
                    "20 days   (50 × 24 = 60 × d₂)",
                    "28.8 days",
                    "18 days",
                    "15 days"
                ],
                "answer": 0,
                "hint": "Total meals = 50 × 24 = 1,200 scout-days divided among 60 scouts!",
                "explanation": "1,200 ÷ 60 = 20 days.",
                "solution_steps": [
                    "Calculate initial supply: 50 × 24 = 1,200 scout-days.",
                    "New group size = 50 + 10 = 60 scouts.",
                    "Duration = 1,200 ÷ 60 = 20 days."
                ]
            },
            {
                "question": "Which situation is a DIRECT proportion (NOT an inverse proportion)?",
                "options": [
                    "Number of notebooks bought and total cost at a fixed price per book",
                    "Driving speed and travel time for a fixed journey",
                    "Number of workers and days needed to paint a fixed wall",
                    "Number of identical taps and time to fill one tank"
                ],
                "answer": 0,
                "hint": "Ask: if the first quantity doubles, does the second DOUBLE (direct) or HALVE (inverse)?",
                "explanation": "Doubling notebooks doubles total cost (quotient Cost/Count = constant price), which is direct proportion.",
                "solution_steps": [
                    "Check scaling behavior for each situation.",
                    "Speed vs time, workers vs days, taps vs fill time all halve when doubled (inverse).",
                    "Notebooks vs total cost keeps Cost ÷ Count = k constant (direct)."
                ]
            },
            {
                "question": "If x and y are inversely proportional and x = 15 when y = 8, find x when y = 24:",
                "options": [
                    "5",
                    "45",
                    "10",
                    "3"
                ],
                "answer": 0,
                "hint": "Product k = 15 × 8 = 120; divide 120 by 24!",
                "explanation": "15 × 8 = x₂ × 24 → 120 ÷ 24 = 5.",
                "solution_steps": [
                    "Find constant product k = 15 × 8 = 120.",
                    "Solve x₂ × 24 = 120.",
                    "x₂ = 120 ÷ 24 = 5."
                ]
            },
            {
                "question": "A farmer owns enough hay to feed 20 cattle for 6 days. How long would the same hay feed 30 cattle?",
                "options": [
                    "4 days",
                    "9 days",
                    "5 days",
                    "3 days"
                ],
                "answer": 0,
                "hint": "Constant cattle-days = 20 × 6 = 120; divide by 30!",
                "explanation": "20 × 6 = 30 × d → 120 ÷ 30 = 4 days.",
                "solution_steps": [
                    "Total supply = 20 × 6 = 120 cattle-days.",
                    "Divide among 30 cattle: 120 ÷ 30.",
                    "Hay lasts 4 days."
                ]
            },
            {
                "question": "A road crew of 18 workers can finish surfacing a lane in 14 days. How many EXTRA workers must be hired to finish in 9 days instead?",
                "options": [
                    "10 extra workers   (28 total − 18 existing)",
                    "28 extra workers",
                    "9 extra workers",
                    "12 extra workers"
                ],
                "answer": 0,
                "hint": "First find TOTAL workers needed (18 × 14 ÷ 9 = 28), then subtract existing 18!",
                "explanation": "18 × 14 = 252 worker-days; 252 ÷ 9 = 28 total → 28 − 18 = 10 extra workers.",
                "solution_steps": [
                    "Total work = 18 × 14 = 252 worker-days.",
                    "Workers needed for 9 days: 252 ÷ 9 = 28 workers.",
                    "Extra workers required: 28 − 18 = 10."
                ]
            },
            {
                "question": "Does a table containing pairs (2, 10), (4, 20), (8, 40) show direct proportion, inverse proportion, or neither?",
                "options": [
                    "Direct proportion   (quotient y/x = 5 constant across all pairs)",
                    "Inverse proportion",
                    "Neither direct nor inverse",
                    "Both direct and inverse"
                ],
                "answer": 0,
                "hint": "Check y ÷ x (10÷2, 20÷4, 40÷8) vs x × y (20, 80, 320)!",
                "explanation": "y/x = 5 remains constant across every pair, proving direct proportion.",
                "solution_steps": [
                    "Check quotients: 10/2 = 5, 20/4 = 5, 40/8 = 5 (constant!).",
                    "Check products: 20, 80, 320 (not constant).",
                    "Therefore variables are directly proportional."
                ]
            },
            {
                "question": "If speed increases by 25% (factor 5/4) over a fixed journey, by what factor does travel time scale?",
                "options": [
                    "4/5   (20% decrease in time)",
                    "5/4   (25% increase)",
                    "3/4   (25% decrease)",
                    "1/5   (80% decrease)"
                ],
                "answer": 0,
                "hint": "Inverse scaling factor is the reciprocal of 5/4!",
                "explanation": "Reciprocal of 5/4 is 4/5 = 0.80 (saving 20% time).",
                "solution_steps": [
                    "Speed multiplier n = 1 + 0.25 = 5/4.",
                    "Apply inverse rule: time scales by 1/n = 4/5.",
                    "Notice 4/5 = 80%, a 20% time reduction."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Rates Schedules Summary",
        "subtitle": "Challenge Arena 4 (10 MCQs): Combined Work Rates, Pumps/Tanks, Charts, Machine Schedules & Summary",
        "questions": [
            {
                "question": "A carpenter builds a cabinet alone in 6 days, and an apprentice builds it alone in 12 days. Working together, how many days do they take?",
                "options": [
                    "4 days",
                    "9 days",
                    "3 days",
                    "18 days"
                ],
                "answer": 0,
                "hint": "Add daily work fractions: 1/6 + 1/12 = 3/12 = 1/4 per day!",
                "explanation": "Combined daily output = 1/6 + 1/12 = 1/4 cabinet/day → full cabinet takes 4 days.",
                "solution_steps": [
                    "Find individual daily rates: 1/6 and 1/12.",
                    "Sum rates: 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4 per day.",
                    "Invert combined rate: 1 ÷ (1/4) = 4 days."
                ]
            },
            {
                "question": "Pump P fills a pool in 2 hours alone, and Pump Q fills the same pool in 6 hours alone. Opened together, how long until the pool fills?",
                "options": [
                    "1.5 hours (1 hour 30 minutes)",
                    "4 hours",
                    "3 hours",
                    "1.2 hours"
                ],
                "answer": 0,
                "hint": "Add hourly fill rates: 1/2 + 1/6 = 4/6 = 2/3 pool/hr → invert to 3/2 hours!",
                "explanation": "1/2 + 1/6 = 2/3 per hour → total time = 3/2 = 1.5 hours.",
                "solution_steps": [
                    "Hourly fill fractions: Pump P = 1/2, Pump Q = 1/6.",
                    "Add rates: 3/6 + 1/6 = 4/6 = 2/3 tank per hour.",
                    "Invert fraction for duration: 3/2 = 1.5 hours."
                ]
            },
            {
                "question": "Six identical pumps empty a flooded basement in 5 hours. How long will 10 identical pumps take for the exact same task?",
                "options": [
                    "3 hours",
                    "8.33 hours",
                    "4 hours",
                    "2 hours"
                ],
                "answer": 0,
                "hint": "Constant pump-hours = 6 × 5 = 30; divide 30 by 10 pumps!",
                "explanation": "30 pump-hours ÷ 10 pumps = 3 hours.",
                "solution_steps": [
                    "Compute constant product: 6 × 5 = 30 pump-hours.",
                    "Divide across 10 pumps: 30 ÷ 10.",
                    "Result = 3 hours."
                ]
            },
            {
                "question": "Complete the inverse proportion table row where x · y = 72: find missing y when x = 9, and missing x when y = 4.5:",
                "options": [
                    "y = 8 and x = 16",
                    "y = 6 and x = 18",
                    "y = 9 and x = 12",
                    "y = 8 and x = 12"
                ],
                "answer": 0,
                "hint": "Compute 72 ÷ 9 and 72 ÷ 4.5!",
                "explanation": "72 ÷ 9 = 8, and 72 ÷ 4.5 = 16.",
                "solution_steps": [
                    "First missing value: y = 72 ÷ 9 = 8.",
                    "Second missing value: x = 72 ÷ 4.5 = 144 ÷ 9 = 16.",
                    "Verify products: 9×8 = 72 and 16×4.5 = 72."
                ]
            },
            {
                "question": "A school transportation pie chart of 360 pupils shows 108° walking, 144° bus, 72° bicycle, and 36° car. How many students ride bicycles?",
                "options": [
                    "72 students",
                    "108 students",
                    "36 students",
                    "144 students"
                ],
                "answer": 0,
                "hint": "Notice total students = 360, matching 360° one-to-one!",
                "explanation": "(72° / 360°) × 360 = 72 students.",
                "solution_steps": [
                    "Divide sector angle by 360°: 72 / 360 = 1 / 5.",
                    "Multiply by total 360 pupils: (1/5) × 360 = 72.",
                    "72 students travel by bicycle."
                ]
            },
            {
                "question": "A factory needs 12 bottling machines to fulfill a juice order in 8 days. How many machines are needed to fulfill that same order in 6 days?",
                "options": [
                    "16 machines",
                    "9 machines",
                    "14 machines",
                    "18 machines"
                ],
                "answer": 0,
                "hint": "Constant machine-days = 12 × 8 = 96; divide by 6 days!",
                "explanation": "96 ÷ 6 = 16 machines.",
                "solution_steps": [
                    "Calculate total workload: 12 × 8 = 96 machine-days.",
                    "Divide by target 6 days: 96 ÷ 6.",
                    "16 machines are required."
                ]
            },
            {
                "question": "Pipe X fills a tank in 5 hours and Pipe Y fills it in 20 hours. Opening both together, how fast do they fill the tank?",
                "options": [
                    "4 hours",
                    "12.5 hours",
                    "25 hours",
                    "5 hours"
                ],
                "answer": 0,
                "hint": "Add hourly fill fractions: 1/5 + 1/20 = 4/20 + 1/20 = 5/20 = 1/4!",
                "explanation": "Combined rate = 1/4 tank/hr → 4 hours total.",
                "solution_steps": [
                    "Express hourly rates: 1/5 and 1/20.",
                    "Sum rates: 4/20 + 1/20 = 5/20 = 1/4 tank per hour.",
                    "Time = 4 hours."
                ]
            },
            {
                "question": "On a 24-hour daily schedule pie chart, a person spends 1/4 of the day studying, 1/3 sleeping, and 1/6 exercising. What central angle remains for other activities?",
                "options": [
                    "90°   (remaining 1/4 of 360°)",
                    "120°",
                    "60°",
                    "150°"
                ],
                "answer": 0,
                "hint": "Compute remaining fraction: 1 − (1/4 + 1/3 + 1/6) = 1 − 9/12 = 3/12 = 1/4!",
                "explanation": "1/4 + 1/3 + 1/6 = 3/12 + 4/12 + 2/12 = 9/12 = 3/4 used → 1/4 remains → 90°.",
                "solution_steps": [
                    "Add used fractions: 3/12 + 4/12 + 2/12 = 9/12 = 3/4.",
                    "Remaining fraction: 1 − 3/4 = 1/4.",
                    "Multiply by 360°: (1/4) × 360° = 90°."
                ]
            },
            {
                "question": "Compare tables carefully: Table A satisfies y/x = 7 across all rows; Table B satisfies x · y = 48 across all rows. Identify BOTH proportions correctly:",
                "options": [
                    "Table A is Direct Proportion; Table B is Inverse Proportion",
                    "Table A is Inverse Proportion; Table B is Direct Proportion",
                    "Both are Direct Proportions",
                    "Both are Inverse Proportions"
                ],
                "answer": 0,
                "hint": "Quotient = constant → Direct; Product = constant → Inverse!",
                "explanation": "Constant quotient y/x = k defines direct proportion; constant product x·y = k defines inverse proportion.",
                "solution_steps": [
                    "Inspect Table A: y/x = 7 implies y = 7x (Direct).",
                    "Inspect Table B: x · y = 48 implies y = 48/x (Inverse).",
                    "Select Table A = Direct, Table B = Inverse."
                ]
            },
            {
                "question": "Which summary option cleanly states the four master formulas of Chapter 10 (Proportional Reasoning-2)?",
                "options": [
                    "Cross-check ad=bc; Share = x·term/sum; Angle = (freq/total)×360°; Direct x/y=k vs Inverse x·y=k",
                    "Direct x·y=k vs Inverse x/y=k; Share = x×sum/term",
                    "Angle = freq×100°; Cross-check a+d=b+c",
                    "All tables satisfy x+y=k"
                ],
                "answer": 0,
                "hint": "Check every formula against the Chapter 10 Summary!",
                "explanation": "Option 1 accurately captures cross-multiplication, share partitioning, pie central angles, and direct vs inverse invariants.",
                "solution_steps": [
                    "Verify cross-product ad = bc and partitioning share = x × term / sum.",
                    "Verify pie central angle = (freq/total) × 360°.",
                    "Verify Direct (x/y = k) vs Inverse (x · y = k)."
                ]
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 5: Arithmetic Progressions
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (Subba Rao, Ramkali, John, Raghav, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Sum Formulas Sn",
        "subtitle": "Deriving Sₙ = (n/2)[2a + (n − 1)d] and Sₙ = (n/2)(a + l) for Finite AP Totals",
        "speech": (
            "Now turn Gauss's brilliant pairing trick into two sparkling algebraic formulas working for any Arithmetic Progression! Write sum S sub n forward from a and a plus d up to final term a plus n minus 1 times d, then write S sub n completely reversed underneath! "
            "Add vertically: every single one of the n columns sums identically to 2 a plus n minus 1 times d! Dividing twice S sub n by 2 delivers Formula One: S sub n equals n over 2 times 2 a plus n minus 1 times d! "
            "Look how neatly 2 a plus n minus 1 times d splits inside into a plus a plus n minus 1 times d, which equals first term a plus last term l! That yields Formula Two: whenever first term a and last term l are known, S sub n equals simply n over 2 times a plus l! "
            "Test immediately on Textbook Example Eleven: find the sum of the first 22 terms of 8, 3, minus 2, and so on! Plug a equals 8, d equals minus 5, n equals 22 into Formula One: 11 times 16 minus 105 equals 11 times minus 89, giving minus 979! Formula Two shines whenever endpoints are given!"
        ),
        "checkpoints": [
            {
                "question": "If a finite AP has n = 15 terms, first term a = 7, and last term l = 49, which formula computes S₁₅ fastest?",
                "options": [
                    "Sₙ = (n/2)(a + l) = (15/2)(7 + 49) = (15/2)(56) = 15 × 28 = 420",
                    "Sₙ = n(a + l) = 15 × 56 = 840",
                    "Sₙ = (n/2)(l − a) = 315",
                    "Need to compute d first before summing"
                ],
                "answer": 0,
                "hint": "Formula Sₙ = (n/2)(a + l) skips finding common difference d completely when a, l, and n are known!",
                "explanation": "S₁₅ = (15/2)(7 + 49) = 15 × 28 = 420 directly."
            },
            {
                "question": "Find the sum of the first 22 terms of the decreasing AP: 8, 3, −2, ... (Textbook Example 11):",
                "options": [
                    "−979",
                    "+979",
                    "−1,079",
                    "−890"
                ],
                "answer": 0,
                "hint": "Use S₂₂ = (22/2)[2(8) + 21(−5)] = 11 × (16 − 105)!",
                "explanation": "11 × (−89) = −979."
            }
        ]
    },
    {
        "id": 10,
        "title": "Term Sum Relation",
        "subtitle": "Using aₙ = Sₙ − Sₙ₋₁ and Explaining Double-n Solutions via Canceling Positive/Negative Terms",
        "speech": (
            "Discover two awesome insights inside Section Five Point Four! Insight One: Suppose a problem gives a formula not for term a sub n, but for sum S sub n directly, like S sub n equals 4 n minus n squared in Exercise 5.3 Question 11! How do you extract term a sub n from S sub n? "
            "Think clearly: S sub n adds terms 1 through n, while S sub n minus 1 adds terms 1 through n minus 1. Subtracting cancels every earlier term except the last one: a sub n equals S sub n minus S sub n minus 1 for n at least 2, with first term a1 equals S1! "
            "For 4 n minus n squared: S1 gives a1 equals 3; S2 equals 4 gives a2 equals 1; hence d equals minus 2! "
            "Insight Two solves the Double Solution Mystery in Example 13: How many terms of 24, 21, 18, and onward sum to 78? Solving 78 equals n over 2 times 48 plus n minus 1 times minus 3 gives n squared minus 17 n plus 52 equals zero, yielding both n equals 4 and n equals 13 because terms 5 through 13 add symmetrically to zero!"
        ),
        "checkpoints": [
            {
                "question": "If the sum of first n terms of an AP is Sₙ = 4n − n² (Exercise 5.3 Q11), find the first term a₁ and 10th term a₁₀:",
                "options": [
                    "a₁ = S₁ = 3, and a₁₀ = S₁₀ − S₉ = (−60) − (−45) = −15",
                    "a₁ = 4 and a₁₀ = −60",
                    "a₁ = 3 and a₁₀ = −45",
                    "a₁ = 1 and a₁₀ = −10"
                ],
                "answer": 0,
                "hint": "Compute S₁ = 4(1) − 1 = 3, S₁₀ = 40 − 100 = −60, and S₉ = 36 − 81 = −45!",
                "explanation": "Using a₁ = S₁ = 3 and aₙ = Sₙ − Sₙ₋₁ gives a₁₀ = S₁₀ − S₉ = −60 − (−45) = −15."
            },
            {
                "question": "For AP 24, 21, 18, ..., why do BOTH n = 4 terms AND n = 13 terms produce the exact same sum S = 78?",
                "options": [
                    "Because terms 5 through 13 (+12, +9, +6, +3, 0, −3, −6, −9, −12) add up symmetrically to zero!",
                    "Because d changes sign from −3 to +3 at term 5",
                    "Because 78 equals zero",
                    "Because only n = 4 is truly valid"
                ],
                "answer": 0,
                "hint": "Notice decreasing terms cross zero at a₉ = 0 and become negative mirror images!",
                "explanation": "Symmetric positive and negative pairs around middle zero term a₉ = 0 cancel to zero, keeping S₁₃ = S₄ + 0 = 78."
            }
        ]
    },
    {
        "id": 11,
        "title": "Divisible Multiples Sums",
        "subtitle": "Summing Multiples & Divisible Integer Sequences Cleanly (Exercise 5.3 Applications)",
        "speech": (
            "Suppose a puzzle asks you to add every three-digit integer divisible by 7, or find the sum of the first 40 positive integers divisible by 6 from Exercise 5.3 Question 12! Never write out forty or one hundred numbers one by one! "
            "Recognize immediately that multiples of any integer k always climb at constant step d equals k, forming a crisp Arithmetic Progression! Test Exercise Five Point Three Question Twelve first: positive multiples of 6 start at first term a equals 6, step by common difference d equals 6, "
            "and continue cleanly up to n equals 40 terms! Plug directly into Sum Formula One: S sub 40 equals 40 over 2 times 2 times 6 plus 39 times 6, which simplifies to 20 times 12 plus 234, giving 20 times 246 equals 4,920! "
            "Now solve Question Fourteen: find the sum of all odd integers between zero and 50! List the clear endpoints: first odd number a equals 1, constant step d equals 2, and final odd number l equals 49! How many odd numbers exist here? Solving 49 equals 1 plus n minus 1 times 2 gives n equals 25! Formula Two gives 25 over 2 times 1 plus 49, equaling 25 times 25, or exactly 625!"
        ),
        "checkpoints": [
            {
                "question": "Find the sum of the first 15 positive multiples of 8 (Exercise 5.3 Q13):",
                "options": [
                    "960  [a = 8, l = 15×8 = 120, S₁₅ = (15/2)(8 + 120) = 15 × 64]",
                    "840",
                    "1,020",
                    "480"
                ],
                "answer": 0,
                "hint": "First multiple = 8, 15th multiple = 120; apply S₁₅ = (15/2)(a + l)!",
                "explanation": "S₁₅ = (15/2)(8 + 120) = 15 × 64 = 960."
            },
            {
                "question": "Find the sum of ALL odd integers strictly between 0 and 50 (Exercise 5.3 Q14):",
                "options": [
                    "625  (note: sum of first n odd numbers ALWAYS equals n²; here 25² = 625!)",
                    "600",
                    "1,225",
                    "525"
                ],
                "answer": 0,
                "hint": "Count odd numbers from 1 to 49 -> n = 25, then use (25/2)(1 + 49)!",
                "explanation": "1 + 3 + ... + 49 has 25 terms summing to (25/2)(1 + 49) = 25 × 25 = 625."
            }
        ]
    },
    {
        "id": 12,
        "title": "Stacking Logs Race",
        "subtitle": "Solving Physical AP Geometry Models: 200 Timber Logs & Potato Race Running Distances",
        "speech": (
            "Now tackle two famous physical applications from Exercise Five Point Three where quadratic solving produces two roots and physical reality selects only one valid answer! Look at Puzzle One, stacking timber logs in Question 19: "
            "200 heavy timber logs sit neatly stacked so 20 logs rest along the bottom row, 19 in the next row above, 18 above that, continuing steadily upwards! How many rows contain all 200 logs, and how many logs sit on the very top row? "
            "Set first term a equals 20, common difference d equals minus 1, and sum S sub n equals 200. Solving 200 equals n over 2 times 40 plus n minus 1 times minus 1 creates the quadratic n squared minus 41 n plus 400 equals zero, factoring cleanly into n minus 16 times n minus 25 equals zero! "
            "Wait, always check both roots n equals 16 and n equals 25! At n equals 25, the 25th row count becomes 20 plus 24 times minus 1 equals minus 4 logs, which is physically impossible! Reject n equals 25 immediately: only 16 rows stack all 200 logs, with 5 logs on top! "
            "Meanwhile in Question 20, running out and back for 10 potatoes spaced 5m, 8m, 11m away totals 370 meters!"
        ),
        "checkpoints": [
            {
                "question": "In stacking 200 logs (20 bottom, 19 next, 18 next...), solving Sₙ = 200 yields n = 16 or n = 25. Why is n = 25 rejected immediately?",
                "options": [
                    "Row 25 would require a₂₅ = 20 + 24(−1) = −4 logs (impossible negative log count), leaving n = 16 rows with 5 logs on top!",
                    "Because 25 is larger than 20",
                    "Because timber stacks can never exceed 10 rows",
                    "Because 16 + 25 = 41"
                ],
                "answer": 0,
                "hint": "Compute the actual number of logs sitting in the top 25th row!",
                "explanation": "a₂₅ = −4 logs is physically impossible; at n = 16, top row has a₁₆ = 20 − 15 = 5 logs and total = 16/2 × (20 + 5) = 200."
            },
            {
                "question": "In a potato race (Ex 5.3 Q20), a bucket sits at start, first potato lies 5 m away, and next 9 lie 3 m apart in line (8m, 11m, ...). Picking one potato at a time and running BACK to bucket totals:",
                "options": [
                    "370 m  (double the one-way AP 5, 8, 11, ... for n = 10 terms)",
                    "185 m",
                    "340 m",
                    "400 m"
                ],
                "answer": 0,
                "hint": "Each potato requires going OUT AND BACK (round-trip = 2× distance): 10m, 16m, 22m, ... for 10 terms!",
                "explanation": "Round-trip AP starts at a = 10 m, step d = 6 m, n = 10: S₁₀ = (10/2)[20 + 9(6)] = 5 × 74 = 370 m."
            }
        ]
    },
    {
        "id": 13,
        "title": "Spiral Semicircle Length",
        "subtitle": "Calculating Total Arc Length of Alternating Semicircles Forming a Growing Spiral (Ex 5.3 Q18)",
        "speech": (
            "Look carefully at Exercise Five Point Three Question Eighteen, an artistic geometry spiral built by attaching 13 consecutive alternating semicircles cleanly end to end! First semicircle S1 centers at point A with radius 0.5 centimeters. "
            "Semicircle S2 flips below center B with radius 1.0 centimeters. Semicircle S3 curves back above center A with radius 1.5 centimeters, and S4 curves below with radius 2.0 centimeters, repeating steadily for 13 continuous half turns! How long is the total spiral ribbon using pi equals 22 over 7? "
            "Recall the exact arc length formula of one semicircle: half of full circumference 2 pi r equals simply pi times radius r! Let us list every individual semicircular length cleanly: L1 equals pi times 0.5, L2 equals pi times 1.0, L3 equals pi times 1.5, "
            "all the way up to L13! Factor out common constant pi immediately: Total Length equals pi times the bracketed sum 0.5 plus 1.0 plus 1.5 plus onward up to 13 terms! Look inside brackets: a clean AP with a equals 0.5, d equals 0.5, n equals 13! "
            "Summing via S13 gives 13 over 2 times 7 equals 91 over 2 centimeters. Multiply cleanly by 22 over 7 to cancel 7 and get 11 times 13 equals 143 centimeters!"
        ),
        "checkpoints": [
            {
                "question": "What is the exact length of the 13-semicircle spiral whose successive radii are 0.5, 1.0, 1.5, ... cm (taking π = 22/7, Ex 5.3 Q18)?",
                "options": [
                    "143 cm",
                    "286 cm",
                    "91 cm",
                    "71.5 cm"
                ],
                "answer": 0,
                "hint": "Each semicircle arc = πr, so sum = π × S₁₃ of radii (0.5 + 1.0 + ... + 6.5)!",
                "explanation": "Radii sum S₁₃ = (13/2)(0.5 + 6.5) = (13×7)/2 = 91/2 cm; multiplying by π = 22/7 gives (22/7)×(91/2) = 11 × 13 = 143 cm."
            },
            {
                "question": "Why does factoring out π first make summing the spiral lengths vastly simpler?",
                "options": [
                    "Because each term Lₖ = πrₖ shares constant multiplier π, revealing a simple rational AP of radii inside brackets",
                    "Because π equals 0.5",
                    "Because semicircles have area πr²",
                    "Because radius stays constant at 0.5 cm"
                ],
                "answer": 0,
                "hint": "Use distributive property: πr₁ + πr₂ + ... + πr₁₃ = π(r₁ + r₂ + ... + r₁₃)!",
                "explanation": "Factoring out π leaves the straightforward arithmetic series 0.5 + 1.0 + ... + 6.5, and factor 7 cancels cleanly with π = 22/7!"
            }
        ]
    },
    {
        "id": 14,
        "title": "Optional First Negative",
        "subtitle": "Optional Exercise 5.4: Finding First Negative Terms & House Number Balance Index",
        "speech": (
            "Now conquer two crown jewels from Section Five Point Five, Optional Exercise Five Point Four, frequently featured in Olympiad and higher challenge exams! Jewel One from Question 1 asks: Which term of the steadily decreasing AP 121, 117, 113, and onward is its very first negative term? "
            "Identify first term a equals 121 and common difference d equals minus 4! Write out nth term a sub n equals 121 plus n minus 1 times minus 4, simplifying cleanly to 125 minus 4 n! For this term to become negative, set 125 minus 4 n strictly less than zero! Moving 4 n across gives 125 less than 4 n, meaning "
            "n is strictly greater than 125 over 4, or 31.25! What is the very first positive whole integer strictly above 31.25? Integer n equals 32! Check: the 31st term is plus 1, while the 32nd term drops to minus 3! "
            "Jewel Two from Question 4 examines street houses numbered 1 through 49. Find house index x so the sum of numbers preceding x equals the sum following x! Setting S sub x minus 1 equals S49 minus S sub x simplifies cleanly into x squared equals 25 times 49, yielding exact house number x equals 35!"
        ),
        "checkpoints": [
            {
                "question": "Which term of the AP: 121, 117, 113, ... is its FIRST negative term (Optional Ex 5.4 Q1)?",
                "options": [
                    "32nd term  (value −3, since 125 − 4n < 0 ⟹ n > 31.25)",
                    "31st term  (value +1)",
                    "30th term  (value +5)",
                    "33rd term  (value −7)"
                ],
                "answer": 0,
                "hint": "Solve 121 + (n − 1)(−4) < 0 cleanly for the smallest integer n!",
                "explanation": "125 − 4n < 0 gives n > 31.25, so the first integer is n = 32 (yielding a₃₂ = 125 − 128 = −3)."
            },
            {
                "question": "Houses on a row are numbered 1 to 49. There exists a house number x such that sum of preceding house numbers (1 to x−1) equals sum of following numbers (x+1 to 49). Find x (Ex 5.4 Q4):",
                "options": [
                    "x = 35  (since x² = 25 × 49  ⟹  x = 5 × 7)",
                    "x = 25",
                    "x = 30",
                    "x = 40"
                ],
                "answer": 0,
                "hint": "Set (x−1)x/2 = 49×50/2 − x(x+1)/2 and simplify both x sides cleanly!",
                "explanation": "x² − x = 49×50 − x² − x ⟹ 2x² = 49×50 ⟹ x² = 49×25 ⟹ positive x = 7 × 5 = 35!"
            }
        ]
    },
    {
        "id": 15,
        "title": "Concrete Terrace Volume",
        "subtitle": "Optional Ex 5.4 Geometry (Ladder Wood & 15-Step Concrete Terrace) + Arithmetic Mean Note",
        "speech": (
            "Explore two grand 3D spatial puzzles plus our Supplementary Arithmetic Mean bonus note! First, look closely at Question Three's wooden ladder: bottom rung spans 45 centimeters, top rung spans 25 centimeters, and total vertical ladder height equals 2.5 meters (or 250 centimeters) with rungs spaced every 25 centimeters apart! Careful with fence post counting! "
            "How many rungs fit across 250 centimeters when spaced 25 centimeters apart? Divide 250 by 25 and add 1 to get 11 rungs, counting both end rungs cleanly! Total required wood length equals 11 over 2 times 45 plus 25, giving 385 centimeters! "
            "Second, check Question Five's football ground concrete terrace: 15 long steps each 50 meters wide with half meter tread depth, stepping upward by one quarter meter rise each step! Step 1 concrete volume equals 50 times one half times one quarter, or 25 over 4 cubic meters; Step 2 rises twice as tall, continuing cleanly as an AP! "
            "Summing all 15 step volumes equals 15 over 2 times 400 over 4, equaling 750 cubic meters! Finally, remember our Supplementary Note on Arithmetic Mean: whenever three numbers a, A, c form an AP, middle term A equals a plus c divided by 2!"
        ),
        "checkpoints": [
            {
                "question": "A small football-ground concrete terrace has 15 steps, each 50 m long, 1/2 m tread, and rising 1/4 m higher than the previous (Optional Ex 5.4 Q5). What total volume of concrete builds the terrace?",
                "options": [
                    "750 m³",
                    "500 m³",
                    "375 m³",
                    "1,500 m³"
                ],
                "answer": 0,
                "hint": "Step 1 volume V₁ = 50 × (1/2) × (1/4) = 25/4 m³, and each next step adds another 25/4 m³ (so Vₖ = k × 25/4)!",
                "explanation": "Total volume = (25/4) × (1 + 2 + ... + 15) = (25/4) × (15 × 16 / 2) = (25/4) × 120 = 25 × 30 = 750 m³!"
            },
            {
                "question": "According to the Supplementary Note on Arithmetic Mean, if three numbers a, A, and c form an AP, what formula expresses middle term A?",
                "options": [
                    "A = (a + c) / 2  (since A − a = c − A  ⟹  2A = a + c)",
                    "A = √(a × c)",
                    "A = (c − a) / 2",
                    "A = a + c"
                ],
                "answer": 0,
                "hint": "Set the common differences equal: second minus first = third minus second!",
                "explanation": "Constant common difference requires A − a = c − A ⟹ 2A = a + c ⟹ Arithmetic Mean A = (a + c)/2."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Five Summary",
        "subtitle": "Consolidating Definitions, General nth Term, Reversed AP, Both Sₙ Formulas & Arithmetic Mean",
        "speech": (
            "Bravo, young number pattern masters! You have just conquered every key theorem, shortcut, and real-world engineering riddle across NCERT Class Ten Chapter Five on Arithmetic Progressions! Snapshot all six golden tools onto one crisp mental page before launching into our four Interactive Exercise Sets! "
            "First, an AP list a, a plus d, a plus 2 d owns fixed common difference d equal to each term minus its predecessor, which may be positive, negative, or zero. Second, forward general term formula a sub n equals a plus n minus 1 times d computes any target term or checks membership via positive whole integer index n! "
            "Third, finding the kth term from the end reverses the finite AP from last term l using negated step minus d, giving l minus k minus 1 times d! Fourth, Gauss pairing symmetry builds both sum formulas: n over 2 times 2 a plus n minus 1 times d, plus the crisp endpoint form n over 2 times a plus l! "
            "Fifth, extract any term from a sum law using S sub n minus S sub n minus 1! Sixth, any three AP terms share middle Arithmetic Mean a plus c over 2! Now tackle Exercises 5.1 through 5.4 confidently!"
        ),
        "checkpoints": [
            {
                "question": "If the numbers k + 2, 4k − 6, and 3k − 2 are three consecutive terms of an AP, find k using the Arithmetic Mean property:",
                "options": [
                    "k = 3  [since 2(4k − 6) = (k + 2) + (3k − 2)  ⟹  8k − 12 = 4k]",
                    "k = −3",
                    "k = 4",
                    "k = 1"
                ],
                "answer": 0,
                "hint": "Set 2 × (middle term) = first + third!",
                "explanation": "8k − 12 = 4k ⟹ 4k = 12 ⟹ k = 3 (check terms: 5, 6, 7 with d = 1!)."
            },
            {
                "question": "Which statement summarizes Chapter 5 formulas cleanly WITHOUT any error?",
                "options": [
                    "aₙ = a + (n−1)d; Sₙ = (n/2)[2a + (n−1)d] = (n/2)(a + l); aₙ = Sₙ − Sₙ₋₁ (n ≥ 2); Arithmetic Mean = (a+c)/2",
                    "Common difference d must always be strictly positive",
                    "kth term from the end is a + (k − 1)d",
                    "Fibonacci sequence 1, 1, 2, 3, 5... is an Arithmetic Progression"
                ],
                "answer": 0,
                "hint": "Check signs of reverse difference, allowance for d ≤ 0, and constant-difference rule!",
                "explanation": "All four formulas in Option 1 are exact Chapter 5 laws."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch5 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

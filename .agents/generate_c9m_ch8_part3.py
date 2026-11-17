#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Slides Data Generator - Part 3 (Slides 17 to 20 - Silent Mastery Quizzes, 40 Questions Total)
Strictly 1-3 word titles, zero spoken audio, zero human names, hints + 3-step solutions.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Sequences Rules Quiz",
        "subtitle": "Sections 8.1–8.3 Practice Set (10 Questions): Triangular/Square Numbers, Explicit Rules, Membership Tests, Recursive & Virahānka",
        "questions": [
            {
                "question": "What is the 7th triangular number T₇ (sum of the first 7 natural numbers)?",
                "options": ["28", "21", "36", "49"],
                "answer": 0,
                "hint": "Compute 1 + 2 + 3 + 4 + 5 + 6 + 7 (or 7 × 8 / 2)!",
                "explanation": "T₇ = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.",
                "solution_steps": [
                    "Identify triangular number formula Tₙ = 1 + 2 + ... + n = n(n+1)/2.",
                    "Substitute n = 7: 7 × 8 / 2.",
                    "Simplify: 56 / 2 = 28."
                ]
            },
            {
                "question": "Which sum of consecutive odd numbers equals the square number 100?",
                "options": [
                    "Sum of the first 10 odd numbers (1 + 3 + 5 + ... + 19)",
                    "Sum of the first 100 odd numbers",
                    "Sum of the first 9 odd numbers",
                    "Sum of the first 10 even numbers"
                ],
                "answer": 0,
                "hint": "Sum of first n consecutive odd numbers equals n²; here n² = 100 ⇒ n = 10!",
                "explanation": "1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 10² = 100.",
                "solution_steps": [
                    "Recall that the sum of the first n odd numbers equals n².",
                    "Set n² = 100 ⇒ n = 10.",
                    "Confirm first 10 odd numbers run from 1 to 2(10) − 1 = 19."
                ]
            },
            {
                "question": "Using explicit formula uₙ = 2n − 1 for odd numbers, find the 300th odd number u₃₀₀.",
                "options": ["599", "600", "601", "597"],
                "answer": 0,
                "hint": "Substitute n = 300 directly into 2n − 1!",
                "explanation": "u₃₀₀ = 2(300) − 1 = 600 − 1 = 599.",
                "solution_steps": [
                    "Write explicit rule uₙ = 2n − 1.",
                    "Substitute position n = 300: u₃₀₀ = 2 × 300 − 1.",
                    "Compute: 600 − 1 = 599."
                ]
            },
            {
                "question": "Test whether the number 118 belongs to the sequence defined by tₙ = 6n − 2 (for n ∈ ℕ).",
                "options": [
                    "Yes, it is the 20th term (t₂₀ = 118)",
                    "No, because 120 is not divisible by 6",
                    "Yes, it is the 19th term",
                    "No, because 118 is even"
                ],
                "answer": 0,
                "hint": "Solve 6n − 2 = 118 for n and check if n is a positive integer!",
                "explanation": "6n − 2 = 118 ⇒ 6n = 120 ⇒ n = 20 ∈ ℕ, so 118 = t₂₀.",
                "solution_steps": [
                    "Set explicit formula equal to target: 6n − 2 = 118.",
                    "Add 2 to both sides: 6n = 120.",
                    "Divide by 6: n = 20 (a valid positive whole integer), confirming 118 = t₂₀."
                ]
            },
            {
                "question": "A sequence follows recursive rule t₁ = 3, tₙ = 3·tₙ₋₁ − 2 for n ≥ 2. What is t₃?",
                "options": ["19", "7", "55", "11"],
                "answer": 0,
                "hint": "First find t₂ = 3(3) − 2 = 7, then compute t₃ = 3(t₂) − 2!",
                "explanation": "t₁ = 3 ⇒ t₂ = 3(3) − 2 = 7 ⇒ t₃ = 3(7) − 2 = 19.",
                "solution_steps": [
                    "Start at anchor term t₁ = 3.",
                    "Compute t₂ = 3(3) − 2 = 7.",
                    "Compute t₃ = 3(7) − 2 = 19."
                ]
            },
            {
                "question": "In the Virahānka-Fibonacci sequence V₁ = 1, V₂ = 2, Vₙ = Vₙ₋₁ + Vₙ₋₂, what is V₈?",
                "options": ["34", "21", "55", "13"],
                "answer": 0,
                "hint": "Continue 1, 2, 3, 5, 8, 13, 21, ... one more step!",
                "explanation": "V₆ = 13, V₇ = 21 ⇒ V₈ = 13 + 21 = 34.",
                "solution_steps": [
                    "List initial terms: V₁=1, V₂=2, V₃=3, V₄=5, V₅=8.",
                    "Compute V₆ = 5+8 = 13 and V₇ = 8+13 = 21.",
                    "Add last two: V₈ = 13 + 21 = 34."
                ]
            },
            {
                "question": "Why did 7th-century Indian scholar Virahānka (and later Gopāla & Hemachandra) investigate Vₙ = Vₙ₋₁ + Vₙ₋₂?",
                "options": [
                    "To count how many poetic rhythms of n total beats can be formed using 1-beat short and 2-beat long syllables",
                    "To calculate circle circumference π",
                    "To measure triangle medians",
                    "To predict weather rainfall"
                ],
                "answer": 0,
                "hint": "Check Section 8.3: Sanskrit poetic meters (chandas)!",
                "explanation": "Virahānka discovered the recurrence while counting n-beat meters composed of 1-beat and 2-beat syllables.",
                "solution_steps": [
                    "Assign 1 beat to a short syllable and 2 beats to a long syllable.",
                    "Notice n-beat rhythms end in either 1 beat (Vₙ₋₁ ways) or 2 beats (Vₙ₋₂ ways).",
                    "Conclude total n-beat meters follow Vₙ = Vₙ₋₁ + Vₙ₋₂."
                ]
            },
            {
                "question": "Which explicit formula generates the square number sequence 1, 4, 9, 16, 25, ... directly from position n?",
                "options": ["tₙ = n²", "tₙ = 2n", "tₙ = n + 3", "tₙ = 2ⁿ"],
                "answer": 0,
                "hint": "Test n = 1, 2, 3, 4: 1²=1, 2²=4, 3²=9, 4²=16!",
                "explanation": "Squaring the position index n gives tₙ = n² directly.",
                "solution_steps": [
                    "Compare positions n = 1, 2, 3, 4 against terms 1, 4, 9, 16.",
                    "Observe each term equals position squared: 1², 2², 3², 4².",
                    "Write explicit rule tₙ = n²."
                ]
            },
            {
                "question": "What is a major advantage of an EXPLICIT rule over a RECURSIVE rule when finding t₅₀₀?",
                "options": [
                    "An explicit rule computes t₅₀₀ in one direct substitution without calculating t₂ through t₄₉₉ first",
                    "Explicit rules never require multiplication",
                    "Recursive rules cannot compute terms beyond n = 10",
                    "Explicit rules work only for finite sequences"
                ],
                "answer": 0,
                "hint": "Recursive rules depend on t₄₉₉, which depends on t₄₉₈, and so on!",
                "explanation": "Explicit formulas evaluate tₙ directly from n in O(1) calculation steps.",
                "solution_steps": [
                    "Note recursive rules require computing all 499 preceding terms sequentially.",
                    "Note explicit rules plug n = 500 directly into a single formula.",
                    "Conclude direct evaluation saves massive computation and enables membership tests."
                ]
            },
            {
                "question": "If the 6th triangular number is 21 and the 7th triangular number is 28, what is their sum 21 + 28?",
                "options": [
                    "49 = 7² (a perfect square!)",
                    "42",
                    "56",
                    "35"
                ],
                "answer": 0,
                "hint": "Consecutive triangular numbers Tₙ₋₁ + Tₙ always combine to form square number n²!",
                "explanation": "21 + 28 = 49 = 7², illustrating T₆ + T₇ = 7².",
                "solution_steps": [
                    "Add T₆ + T₇ = 21 + 28 = 49.",
                    "Recognize 49 = 7².",
                    "Confirm geometrically that two adjacent triangles combine into a 7 × 7 square!"
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Arithmetic Progressions Quiz",
        "subtitle": "Sections 8.4–8.5 Practice Set (10 Questions): Common Difference d, AP nth Term, Linear Graphs, Gauss & Āryabhaṭa Sums",
        "questions": [
            {
                "question": "Find the common difference d and the next two terms of the AP: 24, 19, 14, 9, ...",
                "options": [
                    "d = −5; next two terms are 4 and −1",
                    "d = 5; next two terms are 14 and 19",
                    "d = −4; next two terms are 5 and 1",
                    "d = −5; next two terms are 4 and 0"
                ],
                "answer": 0,
                "hint": "Compute 19 − 24 = −5 and subtract 5 twice from 9!",
                "explanation": "d = 19 − 24 = −5 ⇒ 9 + (−5) = 4, and 4 + (−5) = −1.",
                "solution_steps": [
                    "Subtract adjacent terms: d = 19 − 24 = −5.",
                    "Compute 5th term: 9 − 5 = 4.",
                    "Compute 6th term: 4 − 5 = −1."
                ]
            },
            {
                "question": "In an AP with first term a = 11 and common difference d = 6, calculate the 18th term t₁₈.",
                "options": ["113", "119", "107", "108"],
                "answer": 0,
                "hint": "Use tₙ = a + (n − 1)d with n = 18!",
                "explanation": "t₁₈ = 11 + (18 − 1) × 6 = 11 + 17 × 6 = 11 + 102 = 113.",
                "solution_steps": [
                    "Identify a = 11, d = 6, n = 18.",
                    "Apply formula: t₁₈ = 11 + (18 − 1) × 6 = 11 + 17 × 6.",
                    "Compute: 11 + 102 = 113."
                ]
            },
            {
                "question": "Which term number n of the AP 4, 11, 18, 25, ... equals 144?",
                "options": ["n = 21 (21st term)", "n = 20", "n = 22", "n = 19"],
                "answer": 0,
                "hint": "Solve 4 + (n − 1)(7) = 144!",
                "explanation": "7(n − 1) = 140 ⇒ n − 1 = 20 ⇒ n = 21.",
                "solution_steps": [
                    "Set tₙ = 4 + (n − 1)(7) = 144.",
                    "Subtract 4: 7(n − 1) = 140.",
                    "Divide by 7: n − 1 = 20 ⇒ n = 21."
                ]
            },
            {
                "question": "If the points (1, 5), (2, 9), (3, 13), (4, 17) represent (n, tₙ) of a sequence on a coordinate plane, what is the sequence and its line slope?",
                "options": [
                    "An AP with common difference d = 4 and straight-line slope = 4",
                    "A GP with r = 4 and curved exponential graph",
                    "An AP with d = 5 and slope = 1",
                    "Not a linear pattern"
                ],
                "answer": 0,
                "hint": "Every +1 step in n lifts tₙ by constant +4!",
                "explanation": "tₙ = 5 + (n−1)4 = 4n + 1 plots collinear points along a straight line of slope d = 4.",
                "solution_steps": [
                    "Extract terms: 5, 9, 13, 17.",
                    "Check constant difference: 9 − 5 = 13 − 9 = 17 − 13 = 4.",
                    "Conclude (n, tₙ) forms a straight line with slope d = 4."
                ]
            },
            {
                "question": "Calculate the sum of the first 40 natural numbers: 1 + 2 + 3 + ... + 40.",
                "options": ["820", "800", "1,640", "780"],
                "answer": 0,
                "hint": "Apply Sₙ = n(n + 1)/2 for n = 40!",
                "explanation": "S₄₀ = 40 × 41 / 2 = 20 × 41 = 820.",
                "solution_steps": [
                    "Use Āryabhaṭa / Gauss natural sum formula Sₙ = n(n + 1)/2.",
                    "Substitute n = 40: (40 × 41) / 2.",
                    "Simplify: 20 × 41 = 820."
                ]
            },
            {
                "question": "In which famous 499 CE Indian mathematical text did Āryabhaṭa state the formula for the sum of the first n natural numbers?",
                "options": [
                    "Āryabhaṭīya",
                    "Śhulbasūtras",
                    "The Elements",
                    "Līlāvatī"
                ],
                "answer": 0,
                "hint": "Named directly after Āryabhaṭa himself!",
                "explanation": "Āryabhaṭa presented Sₙ = n(n + 1)/2 in the Āryabhaṭīya (499 CE).",
                "solution_steps": [
                    "Recall Section 8.5 historical context on natural number sums.",
                    "Identify scholar Āryabhaṭa (499 CE).",
                    "Name his landmark treatise: the Āryabhaṭīya."
                ]
            },
            {
                "question": "Find the sum of consecutive integers from 16 through 35 inclusive (16 + 17 + ... + 35).",
                "options": ["510", "630", "120", "495"],
                "answer": 0,
                "hint": "Compute S₃₅ − S₁₅ = (35×36/2) − (15×16/2)!",
                "explanation": "S₃₅ = 630 and S₁₅ = 120 ⇒ 630 − 120 = 510.",
                "solution_steps": [
                    "Compute S₃₅ = 35 × 36 / 2 = 630.",
                    "Compute S₁₅ = 15 × 16 / 2 = 120.",
                    "Subtract S₁₅ from S₃₅: 630 − 120 = 510."
                ]
            },
            {
                "question": "What is the 1st negative term of the decreasing AP 20, 17, 14, 11, ...?",
                "options": ["−1 (which is the 8th term t₈)", "−2 (8th term)", "−1 (7th term)", "−3 (9th term)"],
                "answer": 0,
                "hint": "Find when 20 + (n − 1)(−3) < 0: 23 − 3n < 0 ⇒ n > 23/3 = 7.67!",
                "explanation": "At n = 7, t₇ = 2; at n = 8, t₈ = 2 − 3 = −1.",
                "solution_steps": [
                    "Set tₙ = 20 + (n − 1)(−3) < 0 ⇒ 23 − 3n < 0.",
                    "Solve: n > 23 / 3 ≈ 7.67 ⇒ smallest integer n = 8.",
                    "Evaluate t₈ = 20 + 7(−3) = 20 − 21 = −1."
                ]
            },
            {
                "question": "Write the recursive formulation matching the explicit AP formula tₙ = 9 + 4(n − 1).",
                "options": [
                    "t₁ = 9, tₙ = tₙ₋₁ + 4 (for n ≥ 2)",
                    "t₁ = 4, tₙ = tₙ₋₁ + 9",
                    "t₁ = 9, tₙ = 4·tₙ₋₁",
                    "t₁ = 5, tₙ = tₙ₋₁ + 4"
                ],
                "answer": 0,
                "hint": "Plug n = 1 to get t₁, and read d = 4 as the step added each turn!",
                "explanation": "t₁ = 9 + 4(0) = 9, and each next term adds d = 4: tₙ = tₙ₋₁ + 4.",
                "solution_steps": [
                    "Evaluate t₁ at n = 1: t₁ = 9 + 4(0) = 9.",
                    "Identify common difference d = 4 multiplying (n − 1).",
                    "Write recursive step: tₙ = tₙ₋₁ + 4 for n ≥ 2."
                ]
            },
            {
                "question": "Why can an Arithmetic Progression NEVER have common difference d = 0 and still climb upward?",
                "options": [
                    "Because d = 0 keeps every term identical to a (a constant horizontal line a, a, a, ...)",
                    "Because d = 0 is forbidden in mathematics",
                    "Because d = 0 turns the AP into a GP",
                    "Because a + 0 equals 0"
                ],
                "answer": 0,
                "hint": "Substitute d = 0 into a, a+d, a+2d, ...!",
                "explanation": "When d = 0, tₙ = a + (n−1)(0) = a for every n, producing a flat horizontal line.",
                "solution_steps": [
                    "Substitute d = 0 into general AP formula tₙ = a + (n−1)d.",
                    "Simplify: tₙ = a for all positions n ≥ 1.",
                    "Observe plotted points (n, a) form a flat horizontal line with zero climb."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Geometric Fractals Quiz",
        "subtitle": "Sections 8.6–8.6.2 Practice Set (10 Questions): Common Ratio r, tₙ = arⁿ⁻¹, Sierpiński Fractals, Exponential Graphs & Bouncing Ball",
        "questions": [
            {
                "question": "Find the common ratio r and the 5th term t₅ of the Geometric Progression 3, 6, 12, 24, ...",
                "options": [
                    "r = 2 and t₅ = 48",
                    "r = 3 and t₅ = 48",
                    "r = 2 and t₅ = 96",
                    "r = 3 and t₅ = 243"
                ],
                "answer": 0,
                "hint": "Divide 6/3 = 2 and evaluate t₅ = 3 × 2⁵⁻¹!",
                "explanation": "r = 6/3 = 2 ⇒ t₅ = 3 × 2⁴ = 3 × 16 = 48.",
                "solution_steps": [
                    "Identify first term a = 3 and common ratio r = 6/3 = 2.",
                    "Apply GP formula tₙ = a·rⁿ⁻¹ for n = 5.",
                    "Compute t₅ = 3 × 2⁴ = 3 × 16 = 48."
                ]
            },
            {
                "question": "In the GP 64, 32, 16, 8, ..., what is the 7th term t₇?",
                "options": ["1", "2", "1/2", "4"],
                "answer": 0,
                "hint": "Here a = 64, r = 1/2, and n = 7 ⇒ 64 × (1/2)⁶!",
                "explanation": "t₇ = 64 × (1/2)⁶ = 64 / 64 = 1.",
                "solution_steps": [
                    "Find ratio r = 32 / 64 = 1/2.",
                    "Use t₇ = a·r⁶ = 64 × (1/2)⁶.",
                    "Evaluate 2⁶ = 64, so 64 / 64 = 1."
                ]
            },
            {
                "question": "At Stage 4 of the Sierpiński Triangle (starting from 1 solid triangle of area 1 at Stage 0), how many shaded sub-triangles exist?",
                "options": ["81 shaded triangles (3⁴)", "27 shaded triangles", "243 shaded triangles", "16 shaded triangles"],
                "answer": 0,
                "hint": "Each stage triples the number of shaded triangles: 1, 3, 9, 27, ...!",
                "explanation": "Shaded triangle count follows GP 3ⁿ; at Stage n = 4, 3⁴ = 81.",
                "solution_steps": [
                    "Track shaded triangle counts: Stage 0 = 1, Stage 1 = 3, Stage 2 = 9, Stage 3 = 27.",
                    "Identify GP 3ⁿ.",
                    "Substitute n = 4: 3⁴ = 81 triangles."
                ]
            },
            {
                "question": "At Stage 2 of the Sierpiński Triangle (starting from area 16 cm² at Stage 0), what shaded area remains?",
                "options": ["9 cm² (16 × (3/4)²)", "12 cm²", "4 cm²", "6.75 cm²"],
                "answer": 0,
                "hint": "Each stage keeps 3/4 of the previous shaded area!",
                "explanation": "Remaining area = 16 × (3/4)² = 16 × (9/16) = 9 cm².",
                "solution_steps": [
                    "Recognize each subdivision removes 1/4, keeping factor r = 3/4.",
                    "Apply decaying GP at n = 2: 16 × (3/4)².",
                    "Compute 16 × 9 / 16 = 9 cm²."
                ]
            },
            {
                "question": "A rubber ball is dropped from 100 m and rebounds to 0.6 of its previous height on every bounce. Which GP expression gives its height after the 3rd bounce?",
                "options": ["100 × (0.6)³ = 21.6 m", "100 × (0.6)² = 36 m", "100 − 3(0.6) = 98.2 m", "100 × 0.6 = 60 m"],
                "answer": 0,
                "hint": "Multiply 100 by r = 0.6 once per bounce (3 bounces ⇒ (0.6)³)!",
                "explanation": "Bounce 1 = 60 m, Bounce 2 = 36 m, Bounce 3 = 21.6 m.",
                "solution_steps": [
                    "Set initial drop height h₀ = 100 m and rebound ratio r = 0.6.",
                    "Track bounces: h₁ = 100(0.6), h₂ = 100(0.6)², h₃ = 100(0.6)³.",
                    "Compute 100 × 0.216 = 21.6 m."
                ]
            },
            {
                "question": "What shape does plotting ordered pairs (n, tₙ) of any Geometric Progression with r > 1 produce on a coordinate plane?",
                "options": [
                    "A steeply rising non-linear exponential curve",
                    "A straight line with constant slope",
                    "A horizontal flat line",
                    "A circle centered at the origin"
                ],
                "answer": 0,
                "hint": "Vertical step sizes grow by factor r each time instead of staying constant!",
                "explanation": "GPs with r > 1 grow exponentially, bending sharply upward rather than forming a straight line.",
                "solution_steps": [
                    "Compare consecutive vertical jumps tₙ₊₁ − tₙ = a·rⁿ⁻¹(r − 1).",
                    "Observe vertical jumps multiply by r each step instead of staying constant.",
                    "Conclude plotted points trace a non-linear exponential curve."
                ]
            },
            {
                "question": "Write the recursive definition of the GP 4, −12, 36, −108, ...",
                "options": [
                    "t₁ = 4, tₙ = −3 · tₙ₋₁ (for n ≥ 2)",
                    "t₁ = 4, tₙ = tₙ₋₁ − 16",
                    "t₁ = −3, tₙ = 4 · tₙ₋₁",
                    "t₁ = 4, tₙ = 3 · tₙ₋₁"
                ],
                "answer": 0,
                "hint": "Check ratio r = −12 / 4 = −3!",
                "explanation": "First term t₁ = 4 and common ratio r = −3 give tₙ = −3 · tₙ₋₁.",
                "solution_steps": [
                    "Identify first term t₁ = 4.",
                    "Divide consecutive terms: r = −12 / 4 = −3.",
                    "Write recursive relation: t₁ = 4, tₙ = −3 · tₙ₋₁."
                ]
            },
            {
                "question": "In a GP, t₁ = 2 and t₄ = 54. What is the common ratio r?",
                "options": ["r = 3", "r = 27", "r = 9", "r = 6"],
                "answer": 0,
                "hint": "Set 2·r³ = 54 ⇒ r³ = 27!",
                "explanation": "t₄ = a·r³ = 2·r³ = 54 ⇒ r³ = 27 ⇒ r = 3.",
                "solution_steps": [
                    "Apply GP formula at n = 4: t₄ = a·r³.",
                    "Substitute t₁ = 2, t₄ = 54: 2·r³ = 54 ⇒ r³ = 27.",
                    "Take cube root: r = 3."
                ]
            },
            {
                "question": "Which sequence is BOTH an Arithmetic Progression AND a Geometric Progression simultaneously?",
                "options": [
                    "7, 7, 7, 7, ... (constant sequence with d = 0 and r = 1)",
                    "1, 2, 4, 8, ...",
                    "2, 4, 6, 8, ...",
                    "1, 3, 6, 10, ..."
                ],
                "answer": 0,
                "hint": "Every term is identical: adding 0 gives the same result as multiplying by 1!",
                "explanation": "Any non-zero constant sequence c, c, c, ... has constant difference d = 0 and constant ratio r = 1.",
                "solution_steps": [
                    "Check constant sequence 7, 7, 7, 7, ... for AP: 7 − 7 = 0 (constant d = 0).",
                    "Check for GP: 7 / 7 = 1 (constant r = 1).",
                    "Confirm non-zero constant sequences satisfy both definitions."
                ]
            },
            {
                "question": "At Stage 2 of the Sierpiński Carpet (3×3 grid removing central square each stage), how many shaded small squares exist?",
                "options": ["64 shaded squares (8²)", "9 shaded squares", "16 shaded squares", "72 shaded squares"],
                "answer": 0,
                "hint": "Each remaining square splits into 8 shaded squares: 1 → 8 → 8²!",
                "explanation": "Stage 0 = 1, Stage 1 = 8, Stage 2 = 8² = 64 shaded squares.",
                "solution_steps": [
                    "Stage 1 leaves 9 − 1 = 8 shaded sub-squares.",
                    "Stage 2 replaces each of those 8 squares with 8 smaller shaded squares.",
                    "Multiply: 8 × 8 = 64."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Progressions Mastery Quiz",
        "subtitle": "Exercise Sets 8.1–8.3 & End-of-Chapter Practice (10 Questions): Linear Systems, Population/Wages, Mixed AP/GP & Conversions",
        "questions": [
            {
                "question": "An employee starts at a monthly salary of ₹24,000 and receives a fixed annual raise of ₹1,500 each year. What will the monthly salary be in the 9th year?",
                "options": ["₹36,000", "₹37,500", "₹34,500", "₹25,500"],
                "answer": 0,
                "hint": "Fixed ₹1,500 annual increase forms an AP with a = 24,000, d = 1,500, and n = 9!",
                "explanation": "t₉ = 24,000 + (9 − 1)(1,500) = 24,000 + 12,000 = ₹36,000.",
                "solution_steps": [
                    "Model annual salary as an AP with a = 24,000 and d = 1,500.",
                    "Evaluate Year 9 (n = 9): t₉ = 24,000 + 8 × 1,500.",
                    "Calculate: 24,000 + 12,000 = ₹36,000."
                ]
            },
            {
                "question": "A town's population starts at 10,000 and grows by 10% every year (multiplying by r = 1.1 each year). What is the population after 2 years?",
                "options": ["12,100", "12,000", "11,000", "13,310"],
                "answer": 0,
                "hint": "Compound percentage growth is a GP: 10,000 × (1.1)²!",
                "explanation": "Year 1 = 10,000 × 1.1 = 11,000; Year 2 = 11,000 × 1.1 = 12,100.",
                "solution_steps": [
                    "Convert +10% annual growth into GP common ratio r = 1 + 0.10 = 1.1.",
                    "Apply GP compounding for 2 years: 10,000 × (1.1)².",
                    "Compute: 10,000 × 1.21 = 12,100."
                ]
            },
            {
                "question": "In an Arithmetic Progression, the 4th term t₄ = 19 and the 10th term t₁₀ = 43. Find the 1st term a and 15th term t₁₅.",
                "options": [
                    "a = 7 and t₁₅ = 63",
                    "a = 4 and t₁₅ = 60",
                    "a = 7 and t₁₅ = 67",
                    "a = 3 and t₁₅ = 59"
                ],
                "answer": 0,
                "hint": "Solve system a + 3d = 19 and a + 9d = 43 ⇒ 6d = 24!",
                "explanation": "6d = 24 ⇒ d = 4; a = 19 − 12 = 7 ⇒ t₁₅ = 7 + 14(4) = 63.",
                "solution_steps": [
                    "Write linear system: a + 9d = 43 and a + 3d = 19.",
                    "Subtract equations: 6d = 24 ⇒ d = 4, and a = 19 − 3(4) = 7.",
                    "Compute t₁₅ = 7 + 14(4) = 7 + 56 = 63."
                ]
            },
            {
                "question": "Convert the recursive rule t₁ = −3, tₙ = tₙ₋₁ + 7 into an explicit formula tₙ.",
                "options": [
                    "tₙ = 7n − 10",
                    "tₙ = 7n − 3",
                    "tₙ = −3n + 7",
                    "tₙ = 7n + 4"
                ],
                "answer": 0,
                "hint": "Use tₙ = a + (n − 1)d with a = −3 and d = 7, then simplify!",
                "explanation": "tₙ = −3 + (n − 1)(7) = −3 + 7n − 7 = 7n − 10.",
                "solution_steps": [
                    "Identify AP parameters from recursion: a = −3, d = 7.",
                    "Substitute into explicit AP rule: tₙ = −3 + 7(n − 1).",
                    "Expand and simplify: 7n − 7 − 3 = 7n − 10."
                ]
            },
            {
                "question": "Determine whether the sequence 5, 15, 45, 135, ... is AP, GP, or neither, and find its explicit formula tₙ.",
                "options": [
                    "GP with tₙ = 5 · 3ⁿ⁻¹",
                    "AP with tₙ = 5 + 10(n − 1)",
                    "GP with tₙ = 3 · 5ⁿ⁻¹",
                    "Neither AP nor GP"
                ],
                "answer": 0,
                "hint": "Check ratio 15/5 = 45/15 = 135/45 = 3!",
                "explanation": "Constant ratio r = 3 with first term a = 5 yields GP tₙ = 5 · 3ⁿ⁻¹.",
                "solution_steps": [
                    "Check differences: 15 − 5 = 10, 45 − 15 = 30 (not AP).",
                    "Check ratios: 15/5 = 3, 45/15 = 3, 135/45 = 3 (GP with r = 3!).",
                    "Write GP explicit rule: tₙ = a·rⁿ⁻¹ = 5 · 3ⁿ⁻¹."
                ]
            },
            {
                "question": "A gardener arranges flower pots in triangular rows: 1 in row 1, 2 in row 2, ..., up to 15 in row 15. How many pots are used in total?",
                "options": ["120 pots", "105 pots", "225 pots", "240 pots"],
                "answer": 0,
                "hint": "Compute T₁₅ = 15 × 16 / 2!",
                "explanation": "1 + 2 + ... + 15 = 15 × 16 / 2 = 15 × 8 = 120 pots.",
                "solution_steps": [
                    "Recognize total pots equal the 15th triangular number T₁₅.",
                    "Apply Sₙ = n(n + 1)/2 for n = 15: 15 × 16 / 2.",
                    "Multiply: 15 × 8 = 120 pots."
                ]
            },
            {
                "question": "In a Geometric Progression, t₂ = 12 and t₅ = 324. Find common ratio r and first term a.",
                "options": [
                    "r = 3 and a = 4",
                    "r = 3 and a = 12",
                    "r = 2 and a = 6",
                    "r = 9 and a = 4/3"
                ],
                "answer": 0,
                "hint": "Divide t₅ / t₂ = (ar⁴) / (ar) = r³ = 324 / 12 = 27!",
                "explanation": "r³ = 27 ⇒ r = 3; then a·r = 12 ⇒ a(3) = 12 ⇒ a = 4.",
                "solution_steps": [
                    "Divide GP equations: t₅ / t₂ = (ar⁴)/(ar) = r³ = 324/12 = 27.",
                    "Solve r³ = 27 ⇒ r = 3.",
                    "Substitute into t₂ = ar = 12 ⇒ 3a = 12 ⇒ a = 4."
                ]
            },
            {
                "question": "What is the explicit value of t₁₀ − t₇ for ANY Arithmetic Progression with common difference d = 5?",
                "options": ["15 (since 3d = 3 × 5)", "5", "20", "Cannot be found without knowing first term a"],
                "answer": 0,
                "hint": "Notice a cancels cleanly: [a + 9d] − [a + 6d] = 3d!",
                "explanation": "t₁₀ − t₇ = (a + 9d) − (a + 6d) = 3d = 3(5) = 15 regardless of a.",
                "solution_steps": [
                    "Expand t₁₀ = a + 9d and t₇ = a + 6d.",
                    "Subtract: (a + 9d) − (a + 6d) = 3d.",
                    "Substitute d = 5: 3 × 5 = 15."
                ]
            },
            {
                "question": "How many terms of the sequence 2, 6, 10, 14, ... come BEFORE the term 78?",
                "options": [
                    "19 terms (since 78 is the 20th term)",
                    "20 terms",
                    "18 terms",
                    "21 terms"
                ],
                "answer": 0,
                "hint": "First solve 2 + 4(n − 1) = 78 to get position n = 20, then subtract 1!",
                "explanation": "2 + 4(n−1) = 78 ⇒ n − 1 = 19 ⇒ n = 20, meaning 19 terms precede 78.",
                "solution_steps": [
                    "Find position of 78 in AP (a = 2, d = 4): 2 + 4(n − 1) = 78.",
                    "Solve: 4(n − 1) = 76 ⇒ n − 1 = 19 ⇒ n = 20.",
                    "Count terms strictly before t₂₀: 20 − 1 = 19 terms."
                ]
            },
            {
                "question": "A culture starts with 500 bacteria and doubles every 30 minutes. How many bacteria are present after 2 hours?",
                "options": [
                    "8,000 bacteria (4 doublings: 500 × 2⁴)",
                    "2,000 bacteria",
                    "4,000 bacteria",
                    "16,000 bacteria"
                ],
                "answer": 0,
                "hint": "2 hours = 120 minutes = 4 intervals of 30 minutes ⇒ multiply by 2⁴!",
                "explanation": "After 4 thirty-minute doublings: 500 × 2⁴ = 500 × 16 = 8,000 bacteria.",
                "solution_steps": [
                    "Count 30-minute doubling intervals in 2 hours (120 min): 120 / 30 = 4 doublings.",
                    "Apply GP multiplication factor r = 2 four times: 500 × 2⁴.",
                    "Compute: 500 × 16 = 8,000 bacteria."
                ]
            }
        ]
    }
]

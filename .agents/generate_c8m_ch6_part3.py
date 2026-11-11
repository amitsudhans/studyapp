#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Product Laws Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Distributive Law, Product Increments, Identity 1, Negative Terms & Fast Shortcuts",
        "questions": [
            {
                "question": "If rectangle side lengths a and b are BOTH increased by 1 to (a + 1) and (b + 1), by how much does area (a × b) increase when a = 12 and b = 8?",
                "options": [
                    "21 sq units   [= a + b + 1 = 12 + 8 + 1;   check 13×9 − 12×8 = 117 − 96 = 21]",
                    "20 sq units",
                    "1 sq unit",
                    "25 sq units"
                ],
                "answer": 0,
                "hint": "Apply the two-variable increment formula: increase = a + b + 1!",
                "explanation": "(12+1)(8+1) = 12×8 + 12 + 8 + 1 → exact increase of 21.",
                "solution_steps": [
                    "Expand (a + 1)(b + 1) = ab + a + b + 1.",
                    "Subtract original product ab to get exact increment a + b + 1.",
                    "Substitute a = 12, b = 8: 12 + 8 + 1 = 21."
                ]
            },
            {
                "question": "When is the opposing-increment product (a + 1)(b − 1) STRICTLY EQUAL to the original product (a × b)?",
                "options": [
                    "When b − a = 1   (i.e. b = a + 1, making change b − a − 1 = 0, e.g. 5×6 = 6×5!)",
                    "When a = b",
                    "When a + b = 1",
                    "Never equal for any positive integers"
                ],
                "answer": 0,
                "hint": "Set increment (b − a − 1) = 0 cleanly and solve!",
                "explanation": "(a+1)(b−1) − ab = b − a − 1 = 0 holds whenever b = a + 1 (swapping consecutive factors!).",
                "solution_steps": [
                    "Expand (a + 1)(b − 1) = ab + b − a − 1.",
                    "Equate change to zero: b − a − 1 = 0 → b = a + 1.",
                    "Check example a = 7, b = 8: 7×8 = 56 equals (7+1)(8−1) = 8×7 = 56."
                ]
            },
            {
                "question": "Expand (2x − 5)(3x + 4) cleanly using signed Identity 1 distribution:",
                "options": [
                    "6x² − 7x − 20",
                    "6x² + 7x − 20",
                    "6x² − 20",
                    "6x² − 23x + 20"
                ],
                "answer": 0,
                "hint": "Combine outer product +8x with inner product −15x carefully!",
                "explanation": "6x² + 8x − 15x − 20 = 6x² − 7x − 20.",
                "solution_steps": [
                    "Multiply first & outer: (2x)(3x) + (2x)(4) = 6x² + 8x.",
                    "Multiply inner & last: (−5)(3x) + (−5)(4) = −15x − 20.",
                    "Combine like middle terms: 8x − 15x = −7x → 6x² − 7x − 20."
                ]
            },
            {
                "question": "Expand (x − 4y)(x − 6y) cleanly, carefully tracking negative × negative:",
                "options": [
                    "x² − 10xy + 24y²",
                    "x² − 10xy − 24y²",
                    "x² + 10xy + 24y²",
                    "x² − 2xy + 24y²"
                ],
                "answer": 0,
                "hint": "(−4y)(−6y) = +24y², while middle terms sum (−6xy) + (−4xy)!",
                "explanation": "x² − 6xy − 4xy + 24y² = x² − 10xy + 24y².",
                "solution_steps": [
                    "Distribute x: x(x) + x(−6y) = x² − 6xy.",
                    "Distribute −4y: (−4y)(x) + (−4y)(−6y) = −4xy + 24y².",
                    "Combine −6xy − 4xy = −10xy → x² − 10xy + 24y²."
                ]
            },
            {
                "question": "Compute 63 × 999 rapidly using Section 6.1's subtractive distributive shortcut:",
                "options": [
                    "62,937   [= 63 × (1000 − 1) = 63,000 − 63]",
                    "63,063",
                    "62,947",
                    "62,837"
                ],
                "answer": 0,
                "hint": "Compute 63,000 − 63 carefully!",
                "explanation": "63(1000 − 1) = 63,000 − 63 = 62,937.",
                "solution_steps": [
                    "Rewrite 999 = 1,000 − 1.",
                    "Distribute: 63 × 1,000 − 63 × 1 = 63,000 − 63.",
                    "Subtract cleanly: 62,937."
                ]
            },
            {
                "question": "Evaluate 3,524 × 11 mentally using the additive neighbor rule dcba × (10 + 1):",
                "options": [
                    "38,764   [= 35,240 + 3,524]",
                    "38,664",
                    "37,764",
                    "35,564"
                ],
                "answer": 0,
                "hint": "Add shifted 35,240 + 3,524 cleanly column by column (units 4, 2+4=6, 5+2=7, 3+5=8, top 3)!",
                "explanation": "35,240 + 3,524 = 38,764.",
                "solution_steps": [
                    "Expand 3,524 × 11 = 3,524 × (10 + 1).",
                    "Write shifted sum: 35,240 + 3,524.",
                    "Add neighbor digits cleanly: 3, (3+5)=8, (5+2)=7, (2+4)=6, 4 → 38,764."
                ]
            },
            {
                "question": "Multiply polynomial pair (x + 2)(x² − 2x + 4) cleanly and simplify by combining like terms:",
                "options": [
                    "x³ + 8   (all x² and x middle terms cancel completely to zero!)",
                    "x³ + 4x² + 8",
                    "x³ − 8",
                    "x³ + 2x² + 4x + 8"
                ],
                "answer": 0,
                "hint": "Distribute x across all 3 terms, distribute +2 across all 3 terms, and watch (−2x² + 2x²) + (4x − 4x) vanish!",
                "explanation": "(x³ − 2x² + 4x) + (2x² − 4x + 8) = x³ + 8.",
                "solution_steps": [
                    "Distribute x: x(x² − 2x + 4) = x³ − 2x² + 4x.",
                    "Distribute +2: 2(x² − 2x + 4) = 2x² − 4x + 8.",
                    "Cancel (−2x² + 2x²) = 0 and (4x − 4x) = 0 → exact x³ + 8!"
                ]
            },
            {
                "question": "What Sanskrit term did Brahmagupta use in Brahmasphuṭasiddhānta (Verse 12.55) for breaking multipliers into convenient parts?",
                "options": [
                    "khaṇḍa-guṇanam   (and fast iṣṭa-guṇana)",
                    "śūnya-bindu",
                    "parārdha-sūtra",
                    "trairāśika"
                ],
                "answer": 0,
                "hint": "Remember 'khaṇḍa' means part/piece and 'guṇanam' means multiplication!",
                "explanation": "Brahmagupta codified khaṇḍa-guṇanam (multiplication by parts) in Verse 12.55 alongside fast iṣṭa-guṇana algorithms.",
                "solution_steps": [
                    "Check Section 6.1 A Pinch of History.",
                    "Identify khaṇḍa-guṇanam ('part-wise multiplication') in Brahmasphuṭasiddhānta Verse 12.55.",
                    "Distinguish it from śūnya-bindu (zero dot) and trairāśika (Rule of Three)."
                ]
            },
            {
                "question": "Using 101 distribution N × (100 + 1), compute 89 × 101 mentally:",
                "options": [
                    "8,989   [= 8,900 + 89]",
                    "8,909",
                    "9,089",
                    "8,899"
                ],
                "answer": 0,
                "hint": "Shift 89 two places left (8,900) and add 89 once!",
                "explanation": "89(100 + 1) = 8,900 + 89 = 8,989.",
                "solution_steps": [
                    "Write 101 = 100 + 1.",
                    "Distribute 89: 89×100 + 89×1 = 8,900 + 89.",
                    "Sum cleanly: 8,989."
                ]
            },
            {
                "question": "Which algebraic statement below qualifies as a true IDENTITY rather than a conditional equation?",
                "options": [
                    "(a + m)(b + n) = ab + mb + an + mn",
                    "3x + 4 = 19",
                    "y² = 25",
                    "2k + 1 = 11"
                ],
                "answer": 0,
                "hint": "An identity holds true for EVERY possible number assigned to its letters!",
                "explanation": "Only Identity 1 holds identically across all real numbers; the others solve only specific values.",
                "solution_steps": [
                    "Test equations: 3x+4=19 holds only for x=5; y²=25 only for ±5; 2k+1=11 only for k=5.",
                    "Test Identity 1: holds true for EVERY choice of a, b, m, n.",
                    "Select (a + m)(b + n) = ab + mb + an + mn."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Special Identities Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Identities 1A, 1B, 1C, Pattern 2(a²+b²), Śrīdharācārya's Trick & Calendar Proofs",
        "questions": [
            {
                "question": "Expand (3x + 5y)² completely using Identity 1A: (a + b)² = a² + 2ab + b²:",
                "options": [
                    "9x² + 30xy + 25y²",
                    "9x² + 15xy + 25y²",
                    "9x² + 25y²",
                    "3x² + 30xy + 5y²"
                ],
                "answer": 0,
                "hint": "Square coefficients cleanly ((3x)² = 9x²; (5y)² = 25y²) AND double middle product 2(3x)(5y)!",
                "explanation": "(3x)² + 2(3x)(5y) + (5y)² = 9x² + 30xy + 25y².",
                "solution_steps": [
                    "Identify a = 3x and b = 5y.",
                    "Compute a² = 9x² and b² = 25y².",
                    "Compute middle term 2ab = 2(3x)(5y) = 30xy → 9x² + 30xy + 25y²."
                ]
            },
            {
                "question": "Expand (4p − 7)² cleanly using Identity 1B: (a − b)² = a² − 2ab + b²:",
                "options": [
                    "16p² − 56p + 49",
                    "16p² − 56p − 49",
                    "16p² − 28p + 49",
                    "16p² − 49"
                ],
                "answer": 0,
                "hint": "Watch +49 at the end and 2 × 4p × 7 = 56p in the middle!",
                "explanation": "(4p)² − 2(4p)(7) + 7² = 16p² − 56p + 49.",
                "solution_steps": [
                    "Set a = 4p, b = 7 inside (a − b)² = a² − 2ab + b².",
                    "Square a² = 16p² and b² = +49.",
                    "Compute −2ab = −2(4p)(7) = −56p → 16p² − 56p + 49."
                ]
            },
            {
                "question": "Evaluate 10.5² − 9.5² rapidly without squaring decimals directly, using Identity 1C:",
                "options": [
                    "20   [= (10.5 + 9.5)(10.5 − 9.5) = 20 × 1]",
                    "19",
                    "21",
                    "10"
                ],
                "answer": 0,
                "hint": "Apply a² − b² = (a + b)(a − b) cleanly with a = 10.5 and b = 9.5!",
                "explanation": "(10.5 + 9.5) × (10.5 − 9.5) = 20 × 1 = 20.",
                "solution_steps": [
                    "Recognize difference of squares with a = 10.5, b = 9.5.",
                    "Factor as (10.5 + 9.5)(10.5 − 9.5).",
                    "Multiply 20 × 1 = 20."
                ]
            },
            {
                "question": "Use Śrīdharācārya's squaring identity a² = (a + b)(a − b) + b² to compute 304² (taking b = 4):",
                "options": [
                    "92,416   [= (308 × 300) + 4² = 92,400 + 16]",
                    "92,384   [= 92,400 − 16]",
                    "92,404",
                    "90,016"
                ],
                "answer": 0,
                "hint": "Move −4 away from 304 to reach 300, and +4 up to 308: multiply 308 × 300, then ADD +16!",
                "explanation": "304² = (304 + 4)(304 − 4) + 4² = 308 × 300 + 16 = 92,400 + 16 = 92,416.",
                "solution_steps": [
                    "Choose shift b = 4 to reach clean anchor 304 − 4 = 300.",
                    "Multiply shifted pair: (304 + 4)(304 − 4) = 308 × 300 = 92,400.",
                    "Add b² = 4² = 16 → 92,416."
                ]
            },
            {
                "question": "Evaluate [(x + 5)² − (x − 5)²] cleanly by expanding both identities and subtracting:",
                "options": [
                    "20x   [since (x² + 10x + 25) − (x² − 10x + 25) = 20x = 4ab!]",
                    "50",
                    "2x² + 50",
                    "10x"
                ],
                "answer": 0,
                "hint": "Remember (a + b)² − (a − b)² = 4ab cleanly, with a = x and b = 5!",
                "explanation": "(x² + 10x + 25) − (x² − 10x + 25) = 20x.",
                "solution_steps": [
                    "Expand (x + 5)² = x² + 10x + 25 and (x − 5)² = x² − 10x + 25.",
                    "Subtract carefully: x² − x² = 0, 25 − 25 = 0, and 10x − (−10x) = +20x.",
                    "Matches 4ab identity directly: 4(x)(5) = 20x."
                ]
            },
            {
                "question": "Evaluate (62² + 38²) cleanly using Pattern 1: (a + b)² + (a − b)² = 2(a² + b²) (where a = 50, b = 12):",
                "options": [
                    "5,288   [= 2 × (50² + 12²) = 2 × (2500 + 144)]",
                    "2,644",
                    "4,712",
                    "5,144"
                ],
                "answer": 0,
                "hint": "Write 62 = 50 + 12 and 38 = 50 − 12, then compute 2(2500 + 144)!",
                "explanation": "(50+12)² + (50−12)² = 2(2500 + 144) = 2 × 2,644 = 5,288.",
                "solution_steps": [
                    "Find midpoint a = (62 + 38)/2 = 50 and offset b = 62 − 50 = 12.",
                    "Apply Pattern 1: 2(a² + b²) = 2(50² + 12²).",
                    "Calculate 2 × (2500 + 144) = 2 × 2,644 = 5,288."
                ]
            },
            {
                "question": "Verify Identity 1C [(x + y)(x − y) = x² − y²] using fractional values x = 3/2 and y = 1/2:",
                "options": [
                    "LHS = (2)(1) = 2;   RHS = 9/4 − 1/4 = 8/4 = 2  (Exact Match!)",
                    "LHS = 2;   RHS = 10/4 = 2.5",
                    "LHS = 1;   RHS = 2",
                    "Identity 1C fails for fractions"
                ],
                "answer": 0,
                "hint": "Compute (3/2 + 1/2) = 2, (3/2 − 1/2) = 1, and compare with (3/2)² − (1/2)²!",
                "explanation": "Both sides evaluate identically to 2, confirming Identity 1C across rational numbers.",
                "solution_steps": [
                    "Evaluate LHS: (3/2 + 1/2)(3/2 − 1/2) = (4/2)(2/2) = 2 × 1 = 2.",
                    "Evaluate RHS: (3/2)² − (1/2)² = 9/4 − 1/4 = 8/4 = 2.",
                    "Confirm LHS = RHS = 2."
                ]
            },
            {
                "question": "In a 3 × 3 calendar grid centered at middle date 'm' (with left m−1, right m+1, top m−7, bottom m+7), compute the difference [(m−7)(m+7) − (m−1)(m+1)]:",
                "options": [
                    "−48   [since (m² − 49) − (m² − 1) = −48 ALWAYS!]",
                    "0",
                    "+48",
                    "−7"
                ],
                "answer": 0,
                "hint": "Apply Identity 1C TWICE: (m² − 7²) − (m² − 1²)!",
                "explanation": "(m² − 49) − (m² − 1) = −49 + 1 = −48 for any centered 3×3 calendar date m.",
                "solution_steps": [
                    "Expand vertical cross product via Identity 1C: (m − 7)(m + 7) = m² − 49.",
                    "Expand horizontal cross product: (m − 1)(m + 1) = m² − 1.",
                    "Subtract cleanly: (m² − 49) − (m² − 1) = −48 regardless of m!"
                ]
            },
            {
                "question": "Expand (2a − 3/a)² cleanly using Identity 1B (with a ≠ 0):",
                "options": [
                    "4a² − 12 + 9/a²   [note middle term: −2(2a)(3/a) = −12 because 'a' cancels!]",
                    "4a² + 12 + 9/a²",
                    "4a² − 6 + 9/a²",
                    "4a² − 9/a²"
                ],
                "answer": 0,
                "hint": "Watch how variable 'a' cancels neatly inside −2 × (2a) × (3/a) = −12!",
                "explanation": "(2a)² − 2(2a)(3/a) + (3/a)² = 4a² − 12 + 9/a².",
                "solution_steps": [
                    "Compute first square (2a)² = 4a² and last square (3/a)² = 9/a².",
                    "Compute middle term: −2 × (2a) × (3/a) = −12 (a cancels a!).",
                    "Combine cleanly: 4a² − 12 + 9/a²."
                ]
            },
            {
                "question": "If (a + b) = 11 and (ab) = 24, evaluate (a² + b²) cleanly WITHOUT finding a and b individually (or checking):",
                "options": [
                    "73   [since a² + b² = (a + b)² − 2ab = 11² − 2(24) = 121 − 48]",
                    "121",
                    "97",
                    "169"
                ],
                "answer": 0,
                "hint": "Rearrange Identity 1A cleanly: a² + b² = (a + b)² − 2ab!",
                "explanation": "121 − 48 = 73 (note a=8, b=3 checks: 64 + 9 = 73!).",
                "solution_steps": [
                    "Start from Identity 1A: (a + b)² = a² + 2ab + b².",
                    "Isolate a² + b² = (a + b)² − 2ab.",
                    "Plug values: 11² − 2(24) = 121 − 48 = 73."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Mistakes Patterns Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Section 6.3 Error Analysis & Section 6.4 Multi-Perspective Borders & I-Beams",
        "questions": [
            {
                "question": "Distribute the outer minus sign across EVERY term inside '−(4a − 3b + 2c)' cleanly:",
                "options": [
                    "−4a + 3b − 2c   (distribute −1 across EVERY term inside the bracket!)",
                    "−4a − 3b + 2c",
                    "−4a − 3b − 2c",
                    "4a + 3b − 2c"
                ],
                "answer": 0,
                "hint": "Multiply (−1) cleanly by +4a, −3b, and +2c!",
                "explanation": "−(4a − 3b + 2c) flips all three signs to −4a + 3b − 2c.",
                "solution_steps": [
                    "Distribute −1 to first term: −1 × 4a = −4a.",
                    "Distribute −1 to second term: −1 × (−3b) = +3b.",
                    "Distribute −1 to third term: −1 × 2c = −2c → −4a + 3b − 2c."
                ]
            },
            {
                "question": "Fix the error in the incorrect algebraic statement:   '(2x + 3y)² = 4x² + 9y² + 6xy':",
                "options": [
                    "Error: forgot factor 2 inside 2ab!   Corrected: 4x² + 12xy + 9y²",
                    "Corrected: 2x² + 12xy + 3y²",
                    "Corrected: 4x² + 6xy + 9y² is right",
                    "Corrected: 4x² − 12xy + 9y²"
                ],
                "answer": 0,
                "hint": "Compute 2 × (2x) × (3y) carefully: 2 × 2 × 3 = 12!",
                "explanation": "Middle term must be 2ab = 2(2x)(3y) = 12xy, not 6xy.",
                "solution_steps": [
                    "Compare against Identity 1A: a² + 2ab + b² with a = 2x, b = 3y.",
                    "Notice the student wrote ab (6xy) instead of 2ab (12xy).",
                    "Write full correction: 4x² + 12xy + 9y²."
                ]
            },
            {
                "question": "A student wrote '(7x + 4y) − (2x − 5y) = 5x − y'. Spot the missing sign flip and mend the solution:",
                "options": [
                    "Error: wrote +4y − 5y = −y instead of +4y − (−5y) = +9y!   Corrected: 5x + 9y",
                    "Corrected: 9x + 9y",
                    "Corrected: 5x + y",
                    "The original answer 5x − y is correct"
                ],
                "answer": 0,
                "hint": "Distribute the minus sign cleanly across (−5y): −(−5y) = +5y!",
                "explanation": "7x + 4y − 2x + 5y combines cleanly to 5x + 9y.",
                "solution_steps": [
                    "Distribute minus across second bracket: −(2x − 5y) = −2x + 5y.",
                    "Group like x-terms: 7x − 2x = 5x.",
                    "Group like y-terms: 4y + 5y = 9y → 5x + 9y."
                ]
            },
            {
                "question": "Compare four student pattern formulas at step n: P₁ = (n + 2)² − 4, P₂ = n(n + 4), P₃ = n² + 4n, and P₄ = n(n + 2) + 2n. Are ALL FOUR algebraically equivalent?",
                "options": [
                    "YES — every single expression expands cleanly to exact (n² + 4n)!",
                    "Only P₂ and P₃ are equal",
                    "P₁ equals n² only",
                    "P₄ expands to n² + 2n instead"
                ],
                "answer": 0,
                "hint": "Expand (n+2)² − 4 and n(n+2) + 2n cleanly and compare with n² + 4n!",
                "explanation": "(n²+4n+4)−4 = n²+4n; n(n+4) = n²+4n; and (n²+2n)+2n = n²+4n — all four match unconditionally!",
                "solution_steps": [
                    "Expand P₁: (n + 2)² − 4 = (n² + 4n + 4) − 4 = n² + 4n.",
                    "Expand P₂: n(n + 4) = n² + 4n, matching P₃ directly.",
                    "Expand P₄: (n² + 2n) + 2n = n² + 4n → all 4 pathways agree identically!"
                ]
            },
            {
                "question": "A square courtyard of side 's' has a uniform inside frame border of width 'w' removed around all 4 inner edges (leaving inner square side s − 2w). Simplify total border area [s² − (s − 2w)²]:",
                "options": [
                    "4ws − 4w²   [= s² − (s² − 4ws + 4w²) = 4w(s − w)]",
                    "4ws + 4w²",
                    "2ws − 2w²",
                    "4w²"
                ],
                "answer": 0,
                "hint": "Expand (s − 2w)² = s² − 4ws + 4w² carefully, then distribute the minus sign!",
                "explanation": "s² − (s² − 4ws + 4w²) = 4ws − 4w² (note signs flip inside subtracted bracket!).",
                "solution_steps": [
                    "Expand inner square via Identity 1B: (s − 2w)² = s² − 4ws + 4w².",
                    "Subtract from s²: s² − s² + 4ws − 4w².",
                    "Simplify to 4ws − 4w² = 4w(s − w)."
                ]
            },
            {
                "question": "Calculate the exact area of a symmetric I-beam metal plate cut from an outer H × W rectangle (width W, total height H) by removing TWO identical side cutouts of height h and depth d each:",
                "options": [
                    "H × W − 2hd   (equivalently sum of top & bottom bars plus center vertical web!)",
                    "H × W + 2hd",
                    "(H − h)(W − d)",
                    "2hd"
                ],
                "answer": 0,
                "hint": "Subtract BOTH symmetric side notches (each h × d) from full outer bounding rectangle H × W!",
                "explanation": "Outer bounding area minus two side cutouts = HW − 2hd.",
                "solution_steps": [
                    "Compute outer bounding rectangle area = H × W.",
                    "Compute area of two symmetric side cutouts = 2 × (h × d).",
                    "Subtract cleanly: Area = HW − 2hd."
                ]
            },
            {
                "question": "Fix this multiplication error:   '(x + 4)(y + 3) = xy + 12' (student multiplied only first×first and last×last):",
                "options": [
                    "Missing BOTH cross-terms +3x and +4y!   Corrected: xy + 3x + 4y + 12",
                    "Corrected: xy + 7xy + 12",
                    "Corrected: xy + 4x + 3y + 12",
                    "xy + 12 is already correct"
                ],
                "answer": 0,
                "hint": "Recall Identity 1 requires ALL FOUR rectangular tiles: x(y), x(3), 4(y), and 4(3)!",
                "explanation": "Distributing every term across every term yields xy + 3x + 4y + 12.",
                "solution_steps": [
                    "Multiply x across (y + 3): xy + 3x.",
                    "Multiply +4 across (y + 3): 4y + 12.",
                    "Combine all four non-like terms cleanly: xy + 3x + 4y + 12."
                ]
            },
            {
                "question": "In a monthly calendar grid, take a horizontal row of 3 dates (m−1, m, m+1). Compute [m² − (m−1)(m+1)] cleanly:",
                "options": [
                    "1   [always equal to 1 for ANY middle date m!]",
                    "7",
                    "2m",
                    "−1"
                ],
                "answer": 0,
                "hint": "Apply Identity 1C: (m − 1)(m + 1) = m² − 1, then subtract from m²!",
                "explanation": "m² − (m² − 1) = 1 unconditionally (e.g., 15² − 14×16 = 225 − 224 = 1).",
                "solution_steps": [
                    "Apply Identity 1C to product (m−1)(m+1) = m² − 1.",
                    "Subtract from m²: m² − (m² − 1).",
                    "Distribute minus sign: m² − m² + 1 = +1 always!"
                ]
            },
            {
                "question": "Which algebraic expression is NOT equivalent to 3(2k + 4) − k?",
                "options": [
                    "5k + 4   (forgot to multiply 3 × 4 = 12!)",
                    "5k + 12",
                    "6k + 12 − k",
                    "5(k + 2) + 2"
                ],
                "answer": 0,
                "hint": "Expand 3(2k + 4) − k = 6k + 12 − k = 5k + 12, then check which option fails 5k + 12!",
                "explanation": "5k + 4 fails to distribute 3 onto 4 (missing +8).",
                "solution_steps": [
                    "Simplify target: 3(2k + 4) − k = 6k + 12 − k = 5k + 12.",
                    "Check equivalents: 6k+12−k = 5k+12 and 5(k+2)+2 = 5k+10+2 = 5k+12.",
                    "Spot non-equivalent trap: 5k + 4 ≠ 5k + 12."
                ]
            },
            {
                "question": "Fix the error inside:   '(5x)² − 25 = 5x² − 25 = 5(x² − 5)':",
                "options": [
                    "Error: (5x)² equals 25x², NOT 5x²!   Corrected: 25x² − 25 = 25(x + 1)(x − 1)",
                    "Corrected: 10x² − 25",
                    "Corrected: 25x − 25",
                    "Original step 5(x² − 5) is already valid"
                ],
                "answer": 0,
                "hint": "Squaring product (5x) squares BOTH factor 5 AND variable x: 5² × x² = 25x²!",
                "explanation": "(5x)² − 25 = 25x² − 25 = 25(x² − 1) = 25(x + 1)(x − 1).",
                "solution_steps": [
                    "Expand (5x)² properly: 5² · x² = 25x² (not 5x²!).",
                    "Factor common 25: 25(x² − 1).",
                    "Apply Identity 1C: 25(x + 1)(x − 1)."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Quiz",
        "subtitle": "Challenge Arena 4 (10 MCQs): Combined Synthesis, Coin Conjoin Puzzles & Advanced Algebraic Equivalence",
        "questions": [
            {
                "question": "If integer N leaves remainder 3 when divided by 5 (N = 5k + 3), use Identity 1A to prove what remainder N² ALWAYS leaves when divided by 5:",
                "options": [
                    "4   [since (5k + 3)² = 25k² + 30k + 9 = 5(5k² + 6k + 1) + 4!]",
                    "3",
                    "1",
                    "0"
                ],
                "answer": 0,
                "hint": "Expand (5k + 3)² = 25k² + 30k + 9 and split 9 = 5 + 4!",
                "explanation": "N² = 5(5k² + 6k + 1) + 4 ALWAYS leaves remainder 4 modulo 5 (check 8² = 64 = 5×12 + 4!).",
                "solution_steps": [
                    "Apply Identity 1A: (5k + 3)² = (5k)² + 2(5k)(3) + 3² = 25k² + 30k + 9.",
                    "Separate multiple of 5 from 9: 9 = 5 + 4.",
                    "Factor 5 cleanly: 5(5k² + 6k + 1) + 4 → remainder 4 ALWAYS!"
                ]
            },
            {
                "question": "Evaluate [(2x + 3y)² − (2x − 3y)²] cleanly without full manual expansion, using (a+b)² − (a−b)² = 4ab:",
                "options": [
                    "24xy   [= 4 × (2x) × (3y)]",
                    "12xy",
                    "8x² + 18y²",
                    "0"
                ],
                "answer": 0,
                "hint": "Set a = 2x and b = 3y inside 4ab!",
                "explanation": "4(2x)(3y) = 24xy.",
                "solution_steps": [
                    "Use algebraic pattern (a + b)² − (a − b)² = 4ab.",
                    "Substitute a = 2x and b = 3y cleanly.",
                    "Multiply 4 × 2x × 3y = 24xy."
                ]
            },
            {
                "question": "In the 'Coin Conjoin' puzzle, a 10-coin upward triangle (rows 1–2–3–4) can be flipped upside down in 3 moves. What triangular inversion rule gives minimum moves for a 21-coin triangle (rows 1..6)?",
                "options": [
                    "7 moves   [floor(21 / 3) = 7; 14 interior coins stay fixed!]",
                    "3 moves",
                    "10 moves",
                    "6 moves"
                ],
                "answer": 0,
                "hint": "Check overlapping hexagonal core: for T₆ = 21 coins, divide 21 by 3 cleanly!",
                "explanation": "General minimum moves to invert triangular array Tₙ equals floor(Tₙ / 3); 21 ÷ 3 = 7 moves.",
                "solution_steps": [
                    "Verify pattern: T₃ = 6 → 2 moves; T₄ = 10 → 3 moves; T₅ = 15 → 5 moves.",
                    "Apply formula floor(Tₙ / 3) for T₆ = 21 coins.",
                    "21 ÷ 3 = 7 outer coins moved (14 central coins never budge!)."
                ]
            },
            {
                "question": "Verify algebraically why (n + 1)(n + 3) + 1 ALWAYS produces a perfect square for EVERY integer n:",
                "options": [
                    "Because (n + 1)(n + 3) + 1 = n² + 4n + 4 = (n + 2)²!",
                    "Only when n is even",
                    "Because it equals (n + 1)²",
                    "Because it equals n² + 3"
                ],
                "answer": 0,
                "hint": "Expand (n+1)(n+3) + 1 = n² + 4n + 3 + 1 and factor via Identity 1A!",
                "explanation": "n² + 4n + 4 matches (n + 2)² identically for all integers n.",
                "solution_steps": [
                    "Expand (n + 1)(n + 3) = n² + 4n + 3.",
                    "Add +1: n² + 4n + 4.",
                    "Recognize Identity 1A square: n² + 2(n)(2) + 2² = (n + 2)²!"
                ]
            },
            {
                "question": "Without a calculator, evaluate (998 × 1002 + 4) instantly using Identity 1C:",
                "options": [
                    "1,000,000   [since (1000 − 2)(1000 + 2) + 4 = (1000² − 4) + 4 = 10⁶!]",
                    "999,996",
                    "1,000,008",
                    "998,004"
                ],
                "answer": 0,
                "hint": "Rewrite 998 × 1002 as (1000 − 2)(1000 + 2) = 1000² − 2²!",
                "explanation": "(1000² − 4) + 4 = 1,000,000 cleanly.",
                "solution_steps": [
                    "Apply Identity 1C: 998 × 1002 = (1000 − 2)(1000 + 2) = 1000² − 4.",
                    "Add +4 directly: (1000² − 4) + 4 = 1000².",
                    "Compute 1000² = 1,000,000."
                ]
            },
            {
                "question": "Which simplified polynomial equals (x + 2)² − (x − 1)(x + 4)?",
                "options": [
                    "x + 8   [since (x² + 4x + 4) − (x² + 3x − 4) = x + 8]",
                    "7x",
                    "2x² + x + 8",
                    "x"
                ],
                "answer": 0,
                "hint": "Expand BOTH parts carefully, then distribute the minus sign across ALL THREE terms of (x² + 3x − 4)!",
                "explanation": "(x² + 4x + 4) − (x² + 3x − 4) = x + 8.",
                "solution_steps": [
                    "Expand first part: (x + 2)² = x² + 4x + 4.",
                    "Expand second part: (x − 1)(x + 4) = x² + 3x − 4.",
                    "Subtract carefully: (x² − x²) + (4x − 3x) + (4 − (−4)) = x + 8."
                ]
            },
            {
                "question": "If (x − y) = 4 and (xy) = 21, find (x + y)² AND (x² + y²) using identities:",
                "options": [
                    "(x + y)² = 100   and   x² + y² = 58",
                    "(x + y)² = 16   and   x² + y² = 58",
                    "(x + y)² = 100   and   x² + y² = 37",
                    "(x + y)² = 58   and   x² + y² = 100"
                ],
                "answer": 0,
                "hint": "Recall (x+y)² = (x−y)² + 4xy = 16 + 84 = 100, and x²+y² = (x−y)² + 2xy!",
                "explanation": "(x+y)² = 4² + 4(21) = 100; x²+y² = 16 + 42 = 58 (check x=7, y=3!).",
                "solution_steps": [
                    "Compute x² + y² from (x − y)² = x² − 2xy + y²: x² + y² = 4² + 2(21) = 58.",
                    "Compute (x + y)² = (x² + y²) + 2xy = 58 + 42 = 100.",
                    "Verify with integers x=7, y=3: 7−3=4, 7×3=21, (7+3)²=100, 49+9=58!"
                ]
            },
            {
                "question": "Fix the error inside:   '3(2a − b)² = (6a − 3b)²':",
                "options": [
                    "Cannot push scalar 3 inside a SQUARED bracket! Correct: 3(4a² − 4ab + b²) = 12a² − 12ab + 3b²",
                    "(6a − 3b)² equals 3(2a − b)² cleanly",
                    "Correct: 6a² − 6ab + 3b²",
                    "Correct: 12a² − 3b²"
                ],
                "answer": 0,
                "hint": "Remember (3(2a − b))² would square 3 into 9, NOT keep scalar 3!",
                "explanation": "Exponents apply before scalar multiplication: expand (2a − b)² FIRST, then multiply by 3.",
                "solution_steps": [
                    "Expand squared binomial first: (2a − b)² = 4a² − 4ab + b².",
                    "Multiply by scalar 3: 12a² − 12ab + 3b².",
                    "Note (6a − 3b)² = 36a² − 36ab + 9b² = 9(2a−b)² (3× too big!)."
                ]
            },
            {
                "question": "Evaluate 99 × 101 × (10,001) mentally in 3 rapid seconds via cascading Difference of Squares (Identity 1C):",
                "options": [
                    "99,999,999   [since (100−1)(100+1) = 10⁴ − 1 = 9,999, then (10⁴−1)(10⁴+1) = 10⁸ − 1!]",
                    "100,000,001",
                    "99,990,001",
                    "9,999,999"
                ],
                "answer": 0,
                "hint": "Notice 99 × 101 = (100 − 1)(100 + 1) = 10,000 − 1! Now multiply (10,000 − 1)(10,000 + 1)!",
                "explanation": "(10² − 1)(10² + 1)(10⁴ + 1) = (10⁴ − 1)(10⁴ + 1) = 10⁸ − 1 = 99,999,999.",
                "solution_steps": [
                    "First pair: 99 × 101 = (100 − 1)(100 + 1) = 10,000 − 1.",
                    "Second pair: (10,000 − 1)(10,000 + 1) = 10,000² − 1² = 10⁸ − 1.",
                    "Write 10⁸ − 1 cleanly: eight consecutive 9s = 99,999,999!"
                ]
            },
            {
                "question": "Which grand takeaway consolidates ALL of Chapter 6: We Distribute, Yet Things Multiply?",
                "options": [
                    "Distribution (a+b)(c+d) = ac + ad + bc + bd underpins mental math shortcuts, all three core square/difference identities, error repair, and equivalent geometric pattern formulas!",
                    "(a + b)² always equals a² + b² cleanly",
                    "(a − b)² always ends with −b²",
                    "Two distinct visual slice methods on the same geometric grid can give completely unrelated polynomials"
                ],
                "answer": 0,
                "hint": "Tie together Sections 6.1, 6.2, 6.3, and 6.4 cleanly!",
                "explanation": "Distributive law unifies binomial products, special identities, bug fixing, and multi-perspective area equivalence.",
                "solution_steps": [
                    "6.1: Universal binomial distribution, increments, and mental math ×11, ×101, ×99.",
                    "6.2: (a±b)² = a² ± 2ab + b², (a+b)(a−b) = a² − b², and Śrīdharācārya's squaring shortcut.",
                    "6.3 & 6.4: Spotting sign/cross-term errors and proving multiple geometric slices yield identical expressions."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch6 Class 8 Maths Part 3.")
    total_q = 0
    for s in slides_part3:
        twc = len(s["title"].split())
        assert 1 <= twc <= 3, f"Slide {s['id']} title {s['title']!r} not 1-3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} needs 10 questions"
        for idx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4
            assert len(q["solution_steps"]) == 3
            assert "hint" in q and q["hint"]
            total_q += 1
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Questions: {len(s['questions'])}")
    assert total_q == 40
    print("All 40 exercise & challenge questions verified successfully!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 5: Number Play
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Parity Algebra Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Consecutive Sums, ±4 Consecutive Signs, Parity Rules, Modulo 4 & LCM Divisibility",
        "questions": [
            {
                "question": "Express 18 as the sum of consecutive positive integers in ALL possible ways (2 or more terms):",
                "options": [
                    "5 + 6 + 7 (three terms)   AND   3 + 4 + 5 + 6 (four terms)",
                    "8 + 10 (even skip) only",
                    "Only 5 + 6 + 7",
                    "18 is a power of 2 so zero ways exist"
                ],
                "answer": 0,
                "hint": "Test 3 terms around 18 ÷ 3 = 6, AND 4 terms straddling 18 ÷ 4 = 4.5!",
                "explanation": "18 = 5+6+7 (mean 6) and 18 = 3+4+5+6 (pair mean 4.5); no 2-term consecutive sum gives even 18.",
                "solution_steps": [
                    "For k=3 consecutive integers: 18 ÷ 3 = 6 (middle term) → 5 + 6 + 7 = 18.",
                    "For k=4 consecutive integers: 18 ÷ 2 = 9 = 4 + 5 (middle pair) → 3 + 4 + 5 + 6 = 18.",
                    "Confirm both representations sum cleanly to 18 (odd factor 3 > 1 permits both)."
                ]
            },
            {
                "question": "Take any 4 consecutive integers 21, 22, 23, 24 and insert '+' or '−' before each. Which target value is GUARANTEED IMPOSSIBLE to obtain?",
                "options": [
                    "15   (since every sign combination must be EVEN, never odd!)",
                    "0   (= 21 − 22 − 23 + 24)",
                    "4   (= −21 − 22 + 23 + 24)",
                    "2   (= −21 + 22 − 23 + 24)"
                ],
                "answer": 0,
                "hint": "Every group of 4 consecutive integers holds 2 odds + 2 evens, locking parity strictly EVEN!",
                "explanation": "Only 15 is odd; 0 = 21−22−23+24, 2 = −21+22−23+24, 4 = −21−22+23+24 all work cleanly.",
                "solution_steps": [
                    "Count odds inside {21, 22, 23, 24}: two odds (21, 23) + two evens (22, 24).",
                    "By parity rules, odd ± odd = even, even ± even = even → total parity MUST be EVEN.",
                    "Reject odd 15 immediately as unreachable."
                ]
            },
            {
                "question": "Evaluate parity cleanly for ALL THREE algebraic expressions (where k, m, p are arbitrary integers):\n(i) 6k + 8m − 2p    (ii) 2k + 5    (iii) n(n + 1)",
                "options": [
                    "(i) ALWAYS EVEN,   (ii) ALWAYS ODD,   (iii) ALWAYS EVEN",
                    "(i) ALWAYS EVEN,   (ii) DEPENDS on k,   (iii) ALWAYS ODD",
                    "(i) ALWAYS ODD,   (ii) ALWAYS EVEN,   (iii) ALWAYS EVEN",
                    "(i) ALWAYS EVEN,   (ii) ALWAYS ODD,   (iii) DEPENDS on n"
                ],
                "answer": 0,
                "hint": "Factor 2 out of (i); 2k+5 = even + odd; n(n+1) multiplies two consecutive integers (one must be even)!",
                "explanation": "6k+8m−2p = 2(3k+4m−p) even; 2k+5 = even+odd odd; n(n+1) contains one even factor so product is always even.",
                "solution_steps": [
                    "(i) 6k+8m−2p = 2(3k+4m−p) is always a multiple of 2 (EVEN).",
                    "(ii) 2k is always even, so adding odd 5 guarantees ODD.",
                    "(iii) Any two consecutive integers n and n+1 include one EVEN integer → product n(n+1) is always EVEN."
                ]
            },
            {
                "question": "Every even integer belongs to either (4p) or (4p + 2). Evaluate (14 + 26) and explain why the sum is divisible by 4 even though neither 14 nor 26 divides by 4:",
                "options": [
                    "14 + 26 = 40 (divisible by 4); both have remainder 2 mod 4 (4p+2), so remainders add up to 2 + 2 = 4!",
                    "14 + 26 = 40, purely by coincidence",
                    "14 divides by 4 cleanly",
                    "Two numbers of form (4p+2) always sum to (4k+2)"
                ],
                "answer": 0,
                "hint": "Write 14 = 4(3)+2 and 26 = 4(6)+2 and factor 4 after adding!",
                "explanation": "(4×3 + 2) + (4×6 + 2) = 4(3 + 6 + 1) = 4 × 10 = 40.",
                "solution_steps": [
                    "Classify 14 = 4(3) + 2 and 26 = 4(6) + 2 (both form 4p + 2).",
                    "Add expressions algebraically: (4a + 2) + (4b + 2) = 4(a + b) + 4 = 4(a + b + 1).",
                    "Since 2 + 2 = 4, any two remainder-2 evens ALWAYS sum to an exact multiple of 4."
                ]
            },
            {
                "question": "If integer x divides cleanly by 12 AND integer y leaves remainder 5 when divided by 12, what remainder does (x + y) leave when divided by 12?",
                "options": [
                    "5   (since 12a + (12b + 5) = 12(a + b) + 5)",
                    "0",
                    "7",
                    "17"
                ],
                "answer": 0,
                "hint": "Factor 12 from both multiples and inspect the leftover constant!",
                "explanation": "12a + 12b + 5 = 12(a + b) + 5 leaves exact remainder 5.",
                "solution_steps": [
                    "Express x = 12a and y = 12b + 5 for integers a, b.",
                    "Add cleanly: x + y = 12(a + b) + 5.",
                    "Read remainder directly: 5 (since 0 ≤ 5 < 12)."
                ]
            },
            {
                "question": "A mystery number M is divisible by BOTH 10 and 12. Which of these numbers MUST ALWAYS divide M cleanly?",
                "options": [
                    "60   (= LCM(10, 12); and all factors of 60 such as 4, 15, 20, 30!)",
                    "120   (= 10 × 12)",
                    "24",
                    "40"
                ],
                "answer": 0,
                "hint": "Test M = 60 itself against 120, 24, and 40 cleanly using the LCM Rule!",
                "explanation": "By the LCM rule, 10 | M and 12 | M guarantee LCM(10, 12) = 60 divides M (whereas 60 fails 120, 24, and 40).",
                "solution_steps": [
                    "Compute prime factorizations: 10 = 2 × 5, 12 = 2² × 3.",
                    "Find LCM(10, 12) = 2² × 3 × 5 = 60.",
                    "Confirm M = 60 passes both 10 and 12 yet fails 120, 24, and 40 → guaranteed divisor is 60."
                ]
            },
            {
                "question": "Which statement accurately completes: 'If integer A is divisible by 9 AND integer B is divisible by 12, then (A + B) is ALWAYS divisible by ____':",
                "options": [
                    "3   (since 9 = 3×3 and 12 = 3×4 share common factor 3, giving 3(3p + 4q)!)",
                    "9",
                    "12",
                    "36"
                ],
                "answer": 0,
                "hint": "Factor HCF(9, 12) cleanly out of (9p + 12q) and test A=9, B=12 (sum 21)!",
                "explanation": "9p + 12q = 3(3p + 4q) guarantees divisibility by 3 (e.g., 9 + 12 = 21 fails 9, 12, and 36).",
                "solution_steps": [
                    "Write A = 9p and B = 12q.",
                    "Factor HCF(9, 12) = 3: A + B = 3(3p + 4q).",
                    "Test counterexample 9 + 12 = 21: divisible by 3, NOT by 9, 12, or 36."
                ]
            },
            {
                "question": "Write two equivalent algebraic expressions for ALL integers leaving remainder 6 when divided by 9:",
                "options": [
                    "9k + 6   and   9m − 3",
                    "9k + 6   and   9m − 6",
                    "6k + 9   and   6m − 3",
                    "9k + 3   and   9m − 6"
                ],
                "answer": 0,
                "hint": "Leaving remainder 6 above a multiple of 9 is equivalent to sitting 3 short of the next multiple of 9 (6 + 3 = 9)!",
                "explanation": "9k + 6 = 9(k + 1) − 3 = 9m − 3 generates 6, 15, 24, 33, ...",
                "solution_steps": [
                    "Forward remainder formula modulo 9: 9k + 6.",
                    "Rewrite using next multiple 9(k+1): 9(k+1) − 3 = 9m − 3.",
                    "Verify k=0 → 6 and m=1 → 9(1) − 3 = 6."
                ]
            },
            {
                "question": "If N leaves remainder 2 when divided by 5 (so N = 5k + 2), what remainder does (3N + 4) leave when divided by 5?",
                "options": [
                    "0   (3(5k+2)+4 = 15k + 10 = 5(3k + 2), exact multiple of 5!)",
                    "2",
                    "4",
                    "1"
                ],
                "answer": 0,
                "hint": "Substitute N = 5k + 2 directly inside (3N + 4) and simplify cleanly!",
                "explanation": "3(5k + 2) + 4 = 15k + 6 + 4 = 15k + 10 = 5(3k + 2) leaves remainder 0.",
                "solution_steps": [
                    "Substitute N = 5k + 2: 3(5k + 2) + 4.",
                    "Expand cleanly: 15k + 6 + 4 = 15k + 10.",
                    "Factor out 5: 5(3k + 2) → exact multiple of 5 (remainder 0!)."
                ]
            },
            {
                "question": "Why does Parity Invariance explain why changing '+' to '−' or swapping signs across 10 consecutive numbers CANNOT match an odd target if the original sum was even?",
                "options": [
                    "Any finite sequence of sign flips only shifts the sum by even integers (±2bᵢ), leaving parity permanently locked to the original sum's parity!",
                    "Because consecutive sums always equal zero",
                    "Because subtracting always halves the total",
                    "Because 10 consecutive numbers have 6 odds and 4 evens"
                ],
                "answer": 0,
                "hint": "Recall flipping +b to −b shifts the total by −2b, and any sum of even shifts stays even!",
                "explanation": "Every sign flip preserves odd/even parity because Δ = ±2b is always even.",
                "solution_steps": [
                    "Start with sum S (note sum of 1..10 has 5 odds → S is ODD; for 10 terms with 5 odds initial sum parity is fixed!).",
                    "Every sign toggle (+b ↔ −b) alters S by ±2b (always even).",
                    "Even adjustments preserve parity forever (invariant)."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Divisibility Shortcuts Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Shortcuts for 2, 4, 8, 5, 10, 3, 9, 11, Coprime Composites & Digital Roots",
        "questions": [
            {
                "question": "Check divisibility of 62,484 by ALL four divisors {2, 3, 4, 9}:",
                "options": [
                    "Divisible by 2, 3, and 4 ONLY (NOT by 9, because digit sum 6+2+4+8+4 = 24 fails 9!)",
                    "Divisible by 2 and 4 ONLY",
                    "Divisible by ALL FOUR (2, 3, 4, and 9)",
                    "Divisible by 3 and 9 ONLY"
                ],
                "answer": 0,
                "hint": "Check units digit (4 → ÷2), last two digits (84 → ÷4), and digit sum (24 → ÷3, remainder 6 mod 9)!",
                "explanation": "Last digit 4 (even → ÷2), last two digits 84 = 4×21 (÷4), digit sum 24 (÷3, NOT ÷9).",
                "solution_steps": [
                    "Units digit 4 is even → divisible by 2.",
                    "Last two digits 84 = 4 × 21 → divisible by 4.",
                    "Digit sum 6+2+4+8+4 = 24 → divisible by 3, NOT divisible by 9."
                ]
            },
            {
                "question": "Test whether 83,721 is divisible by 11, and find its exact remainder when divided by 9:",
                "options": [
                    "Divisible by 11 (alternating sum 1+7+8 − (2+3) = 11);   remainder ÷ 9 is 3 (digit sum = 21 = 18 + 3)",
                    "NOT divisible by 11;   remainder ÷ 9 is 0",
                    "Divisible by 11;   remainder ÷ 9 is 0",
                    "NOT divisible by 11;   remainder ÷ 9 is 7"
                ],
                "answer": 0,
                "hint": "Odd places right-to-left: 1+7+8 = 16; even places: 2+3 = 5 → 16 − 5 = 11! Digit sum: 8+3+7+2+1 = 21!",
                "explanation": "Alternating difference = 11 (divisible by 11: 83,721 = 11×7,611); digit sum 21 = 2×9 + 3 leaves remainder 3.",
                "solution_steps": [
                    "Odd positions (from right): 1 + 7 + 8 = 16; even positions: 2 + 3 = 5.",
                    "Subtract: 16 − 5 = 11 (multiple of 11 → 83,721 divides by 11 cleanly).",
                    "Digit sum = 8+3+7+2+1 = 21 → digital root 2+1 = 3 = exact remainder modulo 9."
                ]
            },
            {
                "question": "Replace '#' with the smallest digit making 91#48 cleanly divisible by 8:",
                "options": [
                    "# = 0   (last 3 digits 048 = 48 = 8 × 6, smallest valid digit!)",
                    "# = 1   (148 ÷ 8 fails)",
                    "# = 2",
                    "# = 4"
                ],
                "answer": 0,
                "hint": "The rule for 8 inspects ONLY the last three digits (#48)! Test # = 0 first: 048 = 48!",
                "explanation": "Testing # = 0 gives last three digits 048 = 48 = 8 × 6 (note # ∈ {0, 2, 4, 6, 8} all satisfy 8 | #48, smallest = 0).",
                "solution_steps": [
                    "Divisibility by 8 depends strictly on the last three digits (#48).",
                    "Test smallest digit # = 0: 048 = 48 = 8 × 6 (zero remainder!).",
                    "Confirm # = 0 makes 91,048 = 8 × 11,381."
                ]
            },
            {
                "question": "Find the Digital Root of (489 × 76) quickly WITHOUT multiplying 489 × 76 directly (Aryabhata II's Mahāsiddhānta check):",
                "options": [
                    "3   (DR(489) = 3, DR(76) = 4, and DR(3 × 4) = DR(12) = 3!)",
                    "6",
                    "9",
                    "7"
                ],
                "answer": 0,
                "hint": "Compute DR(489): 4+8+9=21→3, and DR(76): 7+6=13→4! Then find DR(3 × 4)!",
                "explanation": "DR(489) = 3, DR(76) = 4 → DR(product) = DR(3×4) = DR(12) = 3 (check: 489×76 = 37,164 → 3+7+1+6+4 = 21 → 3!).",
                "solution_steps": [
                    "Compute DR(489): 4 + 8 + 9 = 21 → 2 + 1 = 3.",
                    "Compute DR(76): 7 + 6 = 13 → 1 + 3 = 4.",
                    "Multiply digital roots and cast out nines: 3 × 4 = 12 → 1 + 2 = 3 (matching 37,164)!"
                ]
            },
            {
                "question": "Why does divisibility by BOTH 6 and 4 FAIL to guarantee divisibility by 24?",
                "options": [
                    "Because HCF(4, 6) = 2 ≠ 1, so only LCM(4, 6) = 12 is guaranteed (counterexample: 12 and 36 pass 4 & 6 yet leave remainder 12 ÷ 24!)",
                    "Because 4 is not a factor of 24",
                    "Because 6 × 4 equals 12",
                    "Because 24 is prime"
                ],
                "answer": 0,
                "hint": "Compare LCM(4, 6) = 12 against coprime LCM(3, 8) = 24!",
                "explanation": "Non-coprime tests overlap on shared factor 2, proving only LCM(4, 6) = 12 rather than 24.",
                "solution_steps": [
                    "Factor 4 = 2² and 6 = 2 × 3 (shared factor 2!).",
                    "Compute LCM(4, 6) = 2² × 3 = 12 < 24.",
                    "Check counterexample 36: 36÷4=9 and 36÷6=6, yet 36÷24 leaves remainder 12."
                ]
            },
            {
                "question": "Using coprime factors (3 and 5), determine which 5-digit number below is cleanly divisible by 15:",
                "options": [
                    "72,345   (ends in 5 → ÷5, AND digit sum 7+2+3+4+5 = 21 → ÷3!)",
                    "72,340   (sum = 16 fails 3)",
                    "72,342   (sum = 18 passes 3, fails 5)",
                    "72,355   (sum = 22 fails 3)"
                ],
                "answer": 0,
                "hint": "Must pass BOTH units digit ∈ {0, 5} AND digit sum divisible by 3!",
                "explanation": "72,345 ends in 5 (divisible by 5) and sums to 21 (divisible by 3) → 72,345 = 15 × 4,823.",
                "solution_steps": [
                    "Verify HCF(3, 5) = 1 → test both 5 (units digit 0 or 5) and 3 (digit sum ÷ 3).",
                    "72,342 fails 5; 72,340 (sum 16) and 72,355 (sum 22) fail 3.",
                    "72,345 ends in 5 AND sums to 21 (3×7) → divisible by 15."
                ]
            },
            {
                "question": "What algebraic proof shows why 10ⁿ − 1 (like 9, 99, 999, 9999) is ALWAYS divisible by 9?",
                "options": [
                    "Writing N = 1000d + 100c + 10b + a isolates 999d + 99c + 9b = 9(111d + 11c + b), because every 10ⁿ = (99...9) + 1!",
                    "Because 10 is divisible by 9",
                    "Because units digit 1 ÷ 9 = 0",
                    "Because subtracting 1 turns odds even"
                ],
                "answer": 0,
                "hint": "Look closely at 10 = 9+1, 100 = 99+1, 1000 = 999+1: every 10ⁿ − 1 is strictly a string of n nines = 9 × (11...1)!",
                "explanation": "10ⁿ − 1 consists purely of n consecutive nines = 9 × (11...1), always divisible by 9.",
                "solution_steps": [
                    "Expand 10ⁿ = (10ⁿ − 1) + 1.",
                    "Observe 10¹−1=9, 10²−1=99=9×11, 10³−1=999=9×111 (all exact multiples of 9).",
                    "Hence every power of 10 leaves remainder 1 modulo 9 cleanly."
                ]
            },
            {
                "question": "Find the smallest non-negative digit 'k' making 5k823 cleanly divisible by 11:",
                "options": [
                    "k = 3   (14 − 3 = 11, exact multiple of 11!)",
                    "k = 9",
                    "k = 5",
                    "k = 7"
                ],
                "answer": 0,
                "hint": "Odd places right-to-left: 3 + 8 + 5 = 16; even places: 2 + k! Compute 16 − (2 + k) = 14 − k!",
                "explanation": "14 − k must equal a multiple of 11 (0 or 11); keeping 0 ≤ k ≤ 9 requires 14 − k = 11 → k = 3 (check: 53823 = 11 × 4893).",
                "solution_steps": [
                    "Add odd-position digits from right: 3 + 8 + 5 = 16.",
                    "Add even-position digits from right: 2 + k.",
                    "Set difference 16 − (2 + k) = 14 − k equal to 11 → k = 3 (53,823 ÷ 11 = 4,893)."
                ]
            },
            {
                "question": "If the digital root of a 6-digit integer is 9 (such as 234,567 → 27 → 9), which conclusion is GUARANTEED?",
                "options": [
                    "The original integer is cleanly divisible by BOTH 9 and 3!",
                    "The original integer ends in digit 9",
                    "The integer is an odd number",
                    "The integer divides cleanly by 11"
                ],
                "answer": 0,
                "hint": "Digital root 9 means the full digit sum is a positive multiple of 9!",
                "explanation": "A digital root of 9 proves exact divisibility by 9, and since 3 | 9, also by 3.",
                "solution_steps": [
                    "Digital root 9 implies digit sum ≡ 0 (mod 9).",
                    "Hence 9 divides the integer cleanly.",
                    "By Multiples of Factors (Section 5.1), 3 also divides the integer."
                ]
            },
            {
                "question": "Why does divisibility by 10, 5, and 2 NEVER depend on the hundreds or thousands digits of ANY integer?",
                "options": [
                    "Because 10 = 2 × 5 divides every power 10¹, 10², 10³, ... cleanly with zero remainder, isolating units digit 'a' alone!",
                    "Because hundreds digits are always smaller than 10",
                    "Because digit sums ignore tens places",
                    "Because 10 leaves remainder 1 modulo 5"
                ],
                "answer": 0,
                "hint": "Check N = 10(100d + 10c + b) + a modulo 10, 5, and 2!",
                "explanation": "Since 10 = 2×5 divides 10×M cleanly, N mod 10, mod 5, and mod 2 depend solely on units digit a.",
                "solution_steps": [
                    "Write N = 10 × M + a where a is the units digit.",
                    "Notice 10, 5, and 2 all divide 10 × M with zero remainder.",
                    "Thus divisibility by 10, 5, or 2 rests exclusively on units digit a."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Cryptarithms Puzzles Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Cryptarithm Proofs (BYE×6=RAY, Addition Puzzles), Multi-Variable Constraints & Reversals",
        "questions": [
            {
                "question": "Solve the multiplication cryptarithm BYE × 6 = RAY (where distinct letters B, Y, E, R, A represent unique digits 0–9 and B, R ≠ 0):",
                "options": [
                    "105 × 6 = 630   (B=1, Y=0, E=5, R=6, A=3)",
                    "125 × 6 = 750",
                    "104 × 6 = 624",
                    "205 × 6 = 1230"
                ],
                "answer": 0,
                "hint": "Note 6 × BYE remains 3-digit (< 1000), forcing B = 1 immediately! Also units digit of 6 × E equals Y!",
                "explanation": "With B = 1, testing E = 5 yields Y = 0 (6×5 = 30), giving 105 × 6 = 630 (R=6, A=3 — all 5 letters distinct!).",
                "solution_steps": [
                    "Since 6 × BYE = RAY is 3-digit (< 1000), leading digit B MUST equal 1 (200 × 6 = 1200 overflows).",
                    "Check E × 6 ends in Y (so Y is even). Also 6×100 + 6×(10Y+E) < 1000 means 10Y+E < 67 (Y ≤ 6).",
                    "Testing E = 5 gives Y = 0: 105 × 6 = 630 (B=1, Y=0, E=5, R=6, A=3 — all unique!)."
                ]
            },
            {
                "question": "Solve the classic addition cryptarithm: TWO + TWO = FOUR (standard solution maximizing/or valid leading F=1; find exact digits for F, T, W, O, U, R where R is even):",
                "options": [
                    "734 + 734 = 1468   (T=7, W=3, O=4, F=1, U=6, R=8)",
                    "836 + 836 = 1672",
                    "542 + 542 = 1084",
                    "928 + 928 = 1856"
                ],
                "answer": 0,
                "hint": "Check EVERY option carefully: BOTH middle 'O' in TWO and second digit 'O' in FOUR must represent the EXACT SAME DIGIT!",
                "explanation": "734 + 734 = 1468 matches F=1, O=4 (appearing twice!), T=7, W=3, U=6, R=8 — all 6 digits unique!",
                "solution_steps": [
                    "Leading digit F of 4-digit sum TWO + TWO MUST equal 1 (carry from 2 × T ≥ 10).",
                    "Check consistency of digit O across TWO and FOUR: 734 + 734 = 1468 sets O = 4 in BOTH numbers.",
                    "Confirm all 6 letters map to unique digits: F=1, O=4, T=7, W=3, U=6, R=8."
                ]
            },
            {
                "question": "Subtract ANY 2-digit number AB (= 10A + B) from its reversed twin BA (= 10B + A), or compute (AB − BA). That difference MUST ALWAYS be divisible by:",
                "options": [
                    "9   (since (10A + B) − (10B + A) = 9(A − B))",
                    "11",
                    "4",
                    "5"
                ],
                "answer": 0,
                "hint": "Expand 10A + B − (10B + A) algebraically!",
                "explanation": "10A + B − 10B − A = 9A − 9B = 9(A − B), always divisible by 9.",
                "solution_steps": [
                    "Write 2-digit number cleanly: AB = 10A + B, reversed BA = 10B + A.",
                    "Subtract: (10A + B) − (10B + A) = 9A − 9B.",
                    "Factor out 9: 9(A − B), guaranteeing divisibility by 9."
                ]
            },
            {
                "question": "Add ANY 2-digit number AB (= 10A + B) to its reversed twin BA (= 10B + A). The sum (AB + BA) MUST ALWAYS be divisible by:",
                "options": [
                    "11   (since (10A + B) + (10B + A) = 11(A + B))",
                    "9",
                    "10",
                    "2"
                ],
                "answer": 0,
                "hint": "Expand (10A + B) + (10B + A) and factor out 11!",
                "explanation": "11A + 11B = 11(A + B) is always a multiple of 11.",
                "solution_steps": [
                    "Write AB = 10A + B and BA = 10B + A.",
                    "Add terms: (10A + B) + (10B + A) = 11A + 11B = 11(A + B).",
                    "Thus AB + BA is always divisible by 11 (e.g., 27 + 72 = 99 = 11 × 9)."
                ]
            },
            {
                "question": "Find ALL valid pairs (a, b) making 48a23b divisible by 18 when a = 2:",
                "options": [
                    "b = 8 only   (for a=2, digit sum 4+8+2+2+3+b = 19 + b → 27 gives b = 8, even!)",
                    "b = 0 and b = 9",
                    "b = 4 only",
                    "No valid b exists"
                ],
                "answer": 0,
                "hint": "Sum digits 4+8+2+2+3 = 19, then pick an EVEN digit b ∈ {0,2,4,6,8} making 19 + b divisible by 9!",
                "explanation": "19 + 8 = 27 divides by 9 and b = 8 is even → 482,238 = 18 × 26,791.",
                "solution_steps": [
                    "Split 18 = 2 × 9 (coprime): b must be even AND full digit sum must divide by 9.",
                    "Plug a = 2: 4 + 8 + 2 + 2 + 3 + b = 19 + b.",
                    "Next multiple of 9 is 27 → b = 8 (even, passes both 2 and 9!)."
                ]
            },
            {
                "question": "If the 5-digit number 3p7q8 is divisible by 44 (4 × 11) and tens digit q = 6 (note 68 = 4 × 17), find the digit 'p':",
                "options": [
                    "p = 1   (since (3+7+8) − (p+6) = 12 − p = 11 → p = 1; check 31,768 = 44 × 722!)",
                    "p = 5",
                    "p = 9",
                    "p = 0"
                ],
                "answer": 0,
                "hint": "Check 68 ÷ 4 = 17 cleanly! Then solve alternating sum 18 − (p + 6) = 12 − p ∈ {0, 11}!",
                "explanation": "12 − p = 11 yields p = 1 (note 12 − p = 0 gives p = 12, invalid single digit).",
                "solution_steps": [
                    "Verify 4-rule: q = 6 gives last two digits 68 = 4 × 17 (passes 4).",
                    "Apply 11-rule: (3 + 7 + 8) − (p + 6) = 18 − 6 − p = 12 − p.",
                    "Equate 12 − p = 11 → p = 1 (31,768 ÷ 44 = 722)."
                ]
            },
            {
                "question": "In a 3-digit palindrome ABA (= 101A + 10B), what condition on A and B guarantees ABA is cleanly divisible by 9?",
                "options": [
                    "(2A + B) must be a multiple of 9",
                    "(A + B) must be a multiple of 9",
                    "B must equal 0 always",
                    "A must equal 9 always"
                ],
                "answer": 0,
                "hint": "Sum all three digits of ABA cleanly: A + B + A!",
                "explanation": "Digit sum of ABA is 2A + B, which must be divisible by 9.",
                "solution_steps": [
                    "List the three digits of ABA: A, B, and A.",
                    "Compute digit sum = A + B + A = 2A + B.",
                    "Apply Section 5.2's 9-rule: 9 | ABA ⇔ 9 | (2A + B)."
                ]
            },
            {
                "question": "In any 4-digit palindrome ABBA (= 1001A + 110B), WHICH divisor is GUARANTEED to divide EVERY ABBA without exception?",
                "options": [
                    "11   (since 1001 = 11×91 and 110 = 11×10, OR alternating check (A+B) − (B+A) = 0 ALWAYS!)",
                    "9",
                    "4",
                    "5"
                ],
                "answer": 0,
                "hint": "Check alternating odd/even digit sum (A + B) − (B + A) cleanly!",
                "explanation": "ABBA = 11(91A + 10B) always has alternating digit difference 0, guaranteeing divisibility by 11.",
                "solution_steps": [
                    "Compute odd-position sum from right: A + B.",
                    "Compute even-position sum from right: B + A.",
                    "Subtract cleanly: (A + B) − (B + A) = 0 → EVERY 4-digit palindrome divides by 11!"
                ]
            },
            {
                "question": "Look at nested Venn circles for sets of multiples: Circle M₈ (multiples of 8), Circle M₄ (multiples of 4), Circle M₂ (evens). How are they nested?",
                "options": [
                    "M₈ ⊂ M₄ ⊂ M₂   (Every multiple of 8 is a multiple of 4, which is a multiple of 2!)",
                    "M₂ ⊂ M₄ ⊂ M₈",
                    "M₈ and M₄ never overlap",
                    "M₄ ⊂ M₈ ⊂ M₂"
                ],
                "answer": 0,
                "hint": "Check test values: 8 ∈ M₈, M₄, M₂; 4 ∈ M₄, M₂ yet 4 ∉ M₈!",
                "explanation": "Larger power factors create strictly smaller inner subsets: Multiples of 8 ⊂ Multiples of 4 ⊂ Multiples of 2.",
                "solution_steps": [
                    "Every multiple of 8 (= 4 × 2k) divides cleanly by 4 → M₈ ⊂ M₄.",
                    "Every multiple of 4 (= 2 × 2m) divides cleanly by 2 → M₄ ⊂ M₂.",
                    "Counterexamples like 4 and 6 confirm strict containment M₈ ⊂ M₄ ⊂ M₂."
                ]
            },
            {
                "question": "In the cryptarithm A + B + C = DE where D, E, A, B, C are distinct digits and A + B + C reaches the SMALLEST possible 2-digit sum, what are D and E?",
                "options": [
                    "10   (= 2 + 3 + 5, keeping all 5 digits {2, 3, 5, 1, 0} distinct!)",
                    "12   (= 3 + 4 + 5)",
                    "9   (single digit)",
                    "11   (repeats digit 1)"
                ],
                "answer": 0,
                "hint": "Test smallest remaining digits after reserving {D=1, E=0}: 2 + 3 + 5 = 10!",
                "explanation": "2 + 3 + 5 = 10 achieves the smallest 2-digit sum with five unique digits {2, 3, 5, 1, 0}.",
                "solution_steps": [
                    "Smallest 2-digit value DE with D≠0 is 10 (D=1, E=0).",
                    "Pick smallest 3 distinct remaining digits not in {0, 1}: 2, 3, and 4 sum to 9 (1 digit).",
                    "Replace 4 with 5: 2 + 3 + 5 = 10, keeping {2, 3, 5, 1, 0} all five distinct!"
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Quiz",
        "subtitle": "Challenge Arena 4 (10 MCQs): Combined Number Play Synthesis, Multi-Step Proofs & Navakankari Strategy",
        "questions": [
            {
                "question": "Determine whether ANY integer of the form (n³ − n) is ALWAYS, SOMETIMES, or NEVER divisible by 6:",
                "options": [
                    "ALWAYS TRUE   (since n³ − n = (n − 1) × n × (n + 1) multiplies 3 consecutive integers — always containing both a multiple of 2 AND a multiple of 3!)",
                    "SOMETIMES TRUE",
                    "NEVER TRUE",
                    "Only when n is even"
                ],
                "answer": 0,
                "hint": "Factor n³ − n = n(n² − 1) = (n − 1)n(n + 1) and test 3 consecutive integers!",
                "explanation": "Every product of 3 consecutive integers contains at least one multiple of 2 and one multiple of 3 (coprime → divisible by 6).",
                "solution_steps": [
                    "Factor algebraically: n³ − n = n(n² − 1) = (n − 1)n(n + 1).",
                    "Among any 3 consecutive integers, at least one is even (divisible by 2) and exactly one is divisible by 3.",
                    "Since HCF(2, 3) = 1, 6 always divides n³ − n (e.g., 2³−2=6, 3³−3=24, 4³−4=60)."
                ]
            },
            {
                "question": "Test divisibility of the giant 6-digit number 712,836 by 12, 18, and 11:",
                "options": [
                    "Divisible by 12 AND 18 ONLY (passes 4 via 36, passes 2 via 6, digit sum 27 passes 9 & 3; fails 11 because (6+8+1) − (3+2+7) = 3!)",
                    "Divisible by ALL THREE (12, 18, and 11)",
                    "Divisible by 11 ONLY",
                    "Divisible by 12 ONLY"
                ],
                "answer": 0,
                "hint": "Check units digit (6 → ÷2), last two digits (36 → ÷4), digit sum (7+1+2+8+3+6 = 27 → ÷9 & ÷3), and alternating sum (15 − 12 = 3)!",
                "explanation": "712,836 passes 2, 4, 3, and 9 (so passes 12=3×4 and 18=2×9), yet fails 11 (alternating difference 3).",
                "solution_steps": [
                    "Units digit 6 (÷2) and last two digits 36 (÷4) pass.",
                    "Digit sum 7+1+2+8+3+6 = 27 passes 9 (and 3) → passes 12 (3×4) and 18 (2×9).",
                    "Alternating sum (6+8+1) − (3+2+7) = 15 − 12 = 3 ≠ multiple of 11 → fails 11."
                ]
            },
            {
                "question": "If N is divisible by 8, and M is NOT divisible by 8 (say M = 8q + 4), which divisor GUARANTEES dividing (N + M)?",
                "options": [
                    "4   (since 8p + 8q + 4 = 4(2p + 2q + 1)!)",
                    "8",
                    "16",
                    "3"
                ],
                "answer": 0,
                "hint": "Substitute N = 8p and M = 8q + 4, add cleanly, and factor out the largest guaranteed integer!",
                "explanation": "N + M = 4(2p + 2q + 1) is always divisible by 4 (and 2), never divisible by 8.",
                "solution_steps": [
                    "Write N = 8p and M = 8q + 4.",
                    "Add: N + M = 8p + 8q + 4 = 4(2p + 2q + 1).",
                    "Since (2p + 2q + 1) is always odd, 4 divides N+M whereas 8 never does."
                ]
            },
            {
                "question": "Find BOTH valid 2-digit solutions for the cryptarithm AB × 5 = CAB (where distinct letters A, B, C represent unique digits and A ≠ 0, C ≠ 0):",
                "options": [
                    "25 × 5 = 125   and   75 × 5 = 375",
                    "15 × 5 = 75   and   50 × 5 = 250",
                    "35 × 5 = 175   and   65 × 5 = 325",
                    "20 × 5 = 100   and   40 × 5 = 200"
                ],
                "answer": 0,
                "hint": "Since B × 5 ends in B, test B = 0 vs B = 5; when B = 5, solve 5A + 2 ending in A!",
                "explanation": "If B=0, 10A×5 = 50A never ends in A0 unless A=0; setting B=5 gives 5A + 2 ≡ A (mod 10) → A ∈ {2, 7}, yielding 25×5=125 & 75×5=375.",
                "solution_steps": [
                    "Note B × 5 ends in B → B ∈ {0, 5}. Testing B=0 gives 50A = C A 0 → 5A = 10C + A → 4A = 10C → A = 5 fails 50×5=250 (2≠5).",
                    "Set B = 5: carry 2 from 5×5=25 into tens place requires 5A + 2 ≡ A (mod 10) → 4A + 2 ≡ 0 (mod 10).",
                    "Test digits cleanly: A = 2 gives 25 × 5 = 125 (C=1) and A = 7 gives 75 × 5 = 375 (C=3) — both keep {A, B, C} distinct!"
                ]
            },
            {
                "question": "What happens to the Digital Root of ANY integer N whenever you add 9, 18, 27, or ANY multiple of 9 to N?",
                "options": [
                    "The Digital Root remains 100% UNCHANGED (invariant modulo 9)!",
                    "The Digital Root increases by 9",
                    "The Digital Root doubles",
                    "The Digital Root drops to zero"
                ],
                "answer": 0,
                "hint": "Try examples like 25 (DR = 7): add 9 → 34 (DR = 7); add 27 → 52 (DR = 7)!",
                "explanation": "Adding 9k preserves exact remainder modulo 9, leaving the digital root completely invariant.",
                "solution_steps": [
                    "Recall Digital Root equals N modulo 9 (with 9 for positive multiples).",
                    "Adding 9k shifts N + 9k ≡ N (mod 9).",
                    "Confirm digital root stays completely unchanged."
                ]
            },
            {
                "question": "Inside a Venn diagram showing Multiples of 6 (circle A) and Multiples of 8 (circle B), which numbers occupy the EXACT INTERSECTION region (A ∩ B)?",
                "options": [
                    "Multiples of LCM(6, 8) = 24   (24, 48, 72, 96, ...)",
                    "Only multiples of 48",
                    "Multiples of HCF(6, 8) = 2",
                    "Only 6 and 8"
                ],
                "answer": 0,
                "hint": "Numbers inside BOTH Circle 6 AND Circle 8 must be divisible by LCM(6, 8)!",
                "explanation": "Common multiples of 6 and 8 are precisely multiples of LCM(6, 8) = 24.",
                "solution_steps": [
                    "Overlap A ∩ B holds integers divisible by BOTH 6 and 8.",
                    "Apply Section 5.1 LCM Rule: LCM(6, 8) = 24.",
                    "Confirm 24, 48, 72, ... populate A ∩ B."
                ]
            },
            {
                "question": "When placing 9 pawns each during Phase 1 of Navakankari (Sālu Mane Aṭa / Nine Men's Morris), what is a player's PRIMARY strategic objective?",
                "options": [
                    "Control intersection points to build 3-in-a-row mills (and open double-mill threats) while blocking rival 3-in-a-row formations!",
                    "Stack all 9 pawns onto one center dot",
                    "Move diagonally across corner squares",
                    "Sacrifice 7 pawns on turn one"
                ],
                "answer": 0,
                "hint": "Forming 3 pawns along one straight grid line captures one opponent pawn!",
                "explanation": "3-in-a-row mills eliminate opponent pieces until the opponent drops to 2 pawns (cannot form mills).",
                "solution_steps": [
                    "Navakankari grid consists of 3 concentric squares linked by perpendicular centerlines (24 vertices).",
                    "Players alternate placing 9 pawns each, trying to align 3 collinear pawns along a grid edge (a mill).",
                    "Every mill formed removes 1 rival piece, driving victory when the opponent drops below 3 pawns."
                ]
            },
            {
                "question": "If integer x leaves remainder 3 upon division by 4 (x = 4a + 3) and y leaves remainder 1 upon division by 4 (y = 4b + 1), classify (x + y) and (x × y) modulo 4:",
                "options": [
                    "(x + y) is divisible by 4 (rem 0);   (x × y) leaves remainder 3 modulo 4",
                    "Both are divisible by 4",
                    "(x + y) leaves rem 2;   (x × y) leaves rem 1",
                    "(x + y) is odd"
                ],
                "answer": 0,
                "hint": "Test x = 3 and y = 5 cleanly: 3 + 5 = 8 (rem 0 mod 4), and 3 × 5 = 15 = 4×3 + 3 (rem 3 mod 4)!",
                "explanation": "(4a+3)+(4b+1) = 4(a+b+1) has remainder 0; (4a+3)(4b+1) = 16ab + 4a + 12b + 3 leaves remainder 3.",
                "solution_steps": [
                    "Sum: (4a + 3) + (4b + 1) = 4(a + b + 1) → remainder 0 modulo 4.",
                    "Product: (4a + 3)(4b + 1) = 4(4ab + a + 3b) + 3 → remainder 3 modulo 4.",
                    "Quick test with x=3, y=5: 3+5 = 8 (4|8) and 3×5 = 15 = 12 + 3 (rem 3)."
                ]
            },
            {
                "question": "Can the consecutive-sum number 100 (= 4 × 25) be expressed as a sum of consecutive positive integers? Why or why not?",
                "options": [
                    "YES — 100 holds odd factor 25 > 1 (e.g., 5 terms centered at 20: 18+19+20+21+22 = 100, AND 8 terms around 12.5: 9+10+11+12+13+14+15+16 = 100!)",
                    "NO, because 100 is an even number",
                    "NO, because 100 is a perfect square",
                    "Only using negative numbers"
                ],
                "answer": 0,
                "hint": "Remember Slide 1: ONLY pure powers of 2 (without ANY odd factor > 1) are impossible; 100 = 4 × 25 has odd factor 5 and 25!",
                "explanation": "100 = 18+19+20+21+22 = 9+10+11+12+13+14+15+16 (both express 100 via odd prime factor 5).",
                "solution_steps": [
                    "Factor 100 = 4 × 25 (contains odd factor 5 > 1, NOT a pure power of 2!).",
                    "5 consecutive integers around 100÷5 = 20: 18 + 19 + 20 + 21 + 22 = 100.",
                    "8 consecutive integers (pair sum 25 × 4): 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 = 100."
                ]
            },
            {
                "question": "Which grand takeaway summarizes ALL of Chapter 5: Number Play?",
                "options": [
                    "Algebraic parity, modular remainders, place-value expansions, and coprime factors explain consecutive sums, all divisibility shortcuts, digital roots, and cryptarithm puzzles!",
                    "Divisibility rules work only for numbers below 1,000",
                    "Powers of 10 leave remainder 0 when divided by 9",
                    "Every cryptarithm allows leading zeros freely"
                ],
                "answer": 0,
                "hint": "Synthesize parity invariance (5.1), place-value divisibility proofs (5.2), and logical digit constraints (5.3)!",
                "explanation": "Chapter 5 unifies parity, remainders, place-value expansions, and logical constraints behind everyday number tricks.",
                "solution_steps": [
                    "5.1: Consecutive sums, ±2b parity invariance, modulo 4 pairing, and LCM rules.",
                    "5.2: Place-value proofs for 2, 4, 8, 5, 10, 3, 9, 11, coprime factors, and digital roots.",
                    "5.3: Cryptarithms, multi-digit constraints, and strategic thinking in Navakankari."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch5 Class 8 Maths Part 3.")
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

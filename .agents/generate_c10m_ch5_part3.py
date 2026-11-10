#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 5: Arithmetic Progressions
Data Generator - Part 3 (Slides 17 to 20: Exercises 5.1, 5.2, 5.3 & Optional 5.4)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Questions: Exactly 10 questions per slide (40 questions total)
- Zero spoken lecture on Exercise/Quiz slides ("except exercises")
- Zero fictional human character names, zero lecturer personas
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise 5.1 Quiz",
        "subtitle": "Exercise 5.1 Practice: Real-World APs, Initial Terms, Common Differences & Sequence Extensions",
        "questions": [
            {
                "question": "Write the first four terms of the AP when first term a = −1.25 and common difference d = −0.25 (Exercise 5.1 Q2 v):",
                "options": [
                    "−1.25, −1.50, −1.75, −2.00",
                    "−1.25, −1.00, −0.75, −0.50",
                    "−1.25, −2.50, −3.75, −5.00",
                    "−1.25, −1.50, −2.00, −2.50"
                ],
                "answer": 0,
                "hint": "Add −0.25 carefully at each step!",
                "explanation": "−1.25 + (−0.25) = −1.50, then −1.75, then −2.00.",
                "solution_steps": [
                    "Start at a₁ = −1.25.",
                    "Add d = −0.25 repeatedly: −1.50, −1.75, −2.00.",
                    "Confirm list: −1.25, −1.50, −1.75, −2.00."
                ]
            },
            {
                "question": "For AP: 1/3, 5/3, 9/3, 13/3, ... (Exercise 5.1 Q3 iii), find first term a and common difference d:",
                "options": [
                    "a = 1/3  and  d = 4/3",
                    "a = 1/3  and  d = 5/3",
                    "a = 4/3  and  d = 1/3",
                    "a = 1  and  d = 4"
                ],
                "answer": 0,
                "hint": "Subtract a₁ from a₂: 5/3 − 1/3!",
                "explanation": "First term a = 1/3, common difference d = 5/3 − 1/3 = 4/3.",
                "solution_steps": [
                    "Read initial term a = 1/3.",
                    "Compute difference a₂ − a₁ = 5/3 − 1/3 = 4/3.",
                    "Verify 9/3 − 5/3 = 4/3."
                ]
            },
            {
                "question": "Which sequence below is NOT an Arithmetic Progression (Exercise 5.1 Q4)?",
                "options": [
                    "2, 4, 8, 16, ...  (differences 2, 4, 8 vary!)",
                    "2, 5/2, 3, 7/2, ...  (d = 1/2)",
                    "3, 3 + √2, 3 + 2√2, 3 + 3√2, ...  (d = √2)",
                    "−10, −6, −2, 2, ...  (d = +4)"
                ],
                "answer": 0,
                "hint": "Check consecutive subtraction aₖ₊₁ − aₖ across all four sequences!",
                "explanation": "In 2, 4, 8, 16, differences are 2, 4, 8 (doubling ratios, NOT constant difference), whereas all others have constant differences 1/2, √2, and 4.",
                "solution_steps": [
                    "Check 2, 4, 8, 16: 4 − 2 = 2 while 8 − 4 = 4 (2 ≠ 4).",
                    "Verify Options 2, 3, 4 each maintain constant differences (0.5, √2, 4).",
                    "Confirm 2, 4, 8, 16 is NOT an AP."
                ]
            },
            {
                "question": "Check whether √2, √8, √18, √32, ... forms an AP (Exercise 5.1 Q4 xii), and write the next term!",
                "options": [
                    "Yes! Simplifies to √2, 2√2, 3√2, 4√2 (d = √2); next term = 5√2 = √50",
                    "No—square roots never form constant differences",
                    "Yes, with d = √6; next term = √40",
                    "Yes, next term = √64 = 8"
                ],
                "answer": 0,
                "hint": "Simplify radicals first: √8 = 2√2, √18 = 3√2, √32 = 4√2!",
                "explanation": "Rewriting √2, 2√2, 3√2, 4√2 exposes constant difference d = √2, giving next term 5√2 = √50.",
                "solution_steps": [
                    "Factor perfect squares inside roots: √8=2√2, √18=3√2, √32=4√2.",
                    "Verify constant difference d = √2.",
                    "Next term = 4√2 + √2 = 5√2 = √50."
                ]
            },
            {
                "question": "Does 1², 3², 5², 7², ... (= 1, 9, 25, 49...) form an Arithmetic Progression (Exercise 5.1 Q4 xiv)?",
                "options": [
                    "No—differences are 8, 16, 24, which are NOT equal",
                    "Yes—common difference d = 2",
                    "Yes—common difference d = 8",
                    "Yes—next term is 9² with d = 4"
                ],
                "answer": 0,
                "hint": "Compute actual values 1, 9, 25, 49 first before subtracting!",
                "explanation": "9 − 1 = 8 while 25 − 9 = 16; unequal consecutive differences mean it is NOT an AP.",
                "solution_steps": [
                    "Evaluate squares: 1, 9, 25, 49.",
                    "Check gaps: 9 − 1 = 8, 25 − 9 = 16.",
                    "8 ≠ 16 -> NOT an AP."
                ]
            },
            {
                "question": "Does a, 2a, 3a, 4a, ... (Exercise 5.1 Q4 x) form an AP for any real number a?",
                "options": [
                    "Yes—common difference d = a; next term is 5a",
                    "Only when a > 0",
                    "No—because variables cannot be terms",
                    "Yes, with d = 2a"
                ],
                "answer": 0,
                "hint": "Subtract consecutive terms: 2a − a, 3a − 2a, 4a − 3a!",
                "explanation": "Every consecutive difference equals a consistently, forming an AP with d = a (next term 5a).",
                "solution_steps": [
                    "Compute a₂ − a₁ = 2a − a = a.",
                    "Compute a₃ − a₂ = 3a − 2a = a.",
                    "Constant d = a confirms AP -> next term 5a."
                ]
            },
            {
                "question": "Taxi fare is ₹15 for the first km and ₹8 for each additional km (Exercise 5.1 Q1 i). What are the fares for 1, 2, 3, and 4 km?",
                "options": [
                    "₹15, ₹23, ₹31, ₹39 (AP with d = 8)",
                    "₹15, ₹30, ₹45, ₹60",
                    "₹8, ₹23, ₹38, ₹53",
                    "₹15, ₹24, ₹32, ₹40"
                ],
                "answer": 0,
                "hint": "Start at 15 and add 8 for each new kilometer!",
                "explanation": "15, 15+8=23, 23+8=31, 31+8=39 form a valid AP with d = 8.",
                "solution_steps": [
                    "1st km = ₹15.",
                    "Add ₹8 for km 2, 3, 4: 23, 31, 39.",
                    "Constant step +8 confirms AP."
                ]
            },
            {
                "question": "Which difference check properly verifies a, a², a³, a⁴, ... (Exercise 5.1 Q4 xi) is NOT an AP in general?",
                "options": [
                    "a₂ − a₁ = a(a − 1) whereas a₃ − a₂ = a²(a − 1), unequal whenever a ≠ 0, 1",
                    "Both differences always equal 1",
                    "Powers of a always form constant differences",
                    "a⁴ − a³ equals a"
                ],
                "answer": 0,
                "hint": "Compare (a² − a) vs (a³ − a²) cleanly by factoring!",
                "explanation": "Since a(a−1) ≠ a²(a−1) in general (e.g., for a = 2: 4−2=2 while 8−4=4), it is NOT an AP.",
                "solution_steps": [
                    "Write a₂ − a₁ = a² − a = a(a − 1).",
                    "Write a₃ − a₂ = a³ − a² = a²(a − 1).",
                    "Observe unequal values when a = 2 (2 ≠ 4) -> NOT an AP."
                ]
            },
            {
                "question": "Write the next three terms after 3, 3 + √2, 3 + 2√2, 3 + 3√2, ... (Exercise 5.1 Q4 v):",
                "options": [
                    "3 + 4√2,  3 + 5√2,  3 + 6√2",
                    "3 + 3√4,  3 + 3√6,  3 + 3√8",
                    "6 + 4√2,  9 + 5√2,  12 + 6√2",
                    "3 + 4√4,  3 + 5√6,  3 + 6√8"
                ],
                "answer": 0,
                "hint": "Common difference d = √2 is added repeatedly!",
                "explanation": "Adding √2 increases the √2 coefficient by 1 each term: 3 + 4√2, 3 + 5√2, 3 + 6√2.",
                "solution_steps": [
                    "Compute d = (3 + √2) − 3 = √2.",
                    "Add √2 to 3 + 3√2 -> 3 + 4√2.",
                    "Continue -> 3 + 5√2 and 3 + 6√2."
                ]
            },
            {
                "question": "If an AP has common difference d = −4 and 7th term a₇ = 4 (similar to Ex 5.2 table), find its first term a:",
                "options": [
                    "a = 28",
                    "a = −20",
                    "a = 24",
                    "a = 32"
                ],
                "answer": 0,
                "hint": "Plug into a₇ = a + 6d = 4 -> a + 6(−4) = 4!",
                "explanation": "a − 24 = 4 ⟹ a = 28.",
                "solution_steps": [
                    "Write a₇ = a + (7 − 1)d = 4.",
                    "Substitute d = −4: a + 6(−4) = 4 -> a − 24 = 4.",
                    "Solve a = 28."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise 5.2 Quiz",
        "subtitle": "Exercise 5.2 Practice: Missing Table Values, Two-Term Systems, Multiples & Savings Problems",
        "questions": [
            {
                "question": "Find missing n in the AP table: a = −18.9, d = 2.5, aₙ = 3.6 (Exercise 5.2 Q1 iv):",
                "options": [
                    "n = 10",
                    "n = 9",
                    "n = 11",
                    "n = 12"
                ],
                "answer": 0,
                "hint": "3.6 = −18.9 + (n − 1)(2.5) -> 22.5 = 2.5(n − 1)!",
                "explanation": "3.6 + 18.9 = 22.5; dividing by 2.5 gives n − 1 = 9 ⟹ n = 10.",
                "solution_steps": [
                    "Set up −18.9 + (n − 1)(2.5) = 3.6.",
                    "Add 18.9: (n − 1)(2.5) = 22.5 -> n − 1 = 9.",
                    "Solve n = 10."
                ]
            },
            {
                "question": "In the AP: ___, 13, ___, 3 (Exercise 5.2 Q1 ii box fill), find the two missing boxes cleanly:",
                "options": [
                    "18  and  8  (since a + d = 13 and a + 3d = 3  ⟹  d = −5, a = 18)",
                    "23  and  8",
                    "15  and  5",
                    "10  and  6"
                ],
                "answer": 0,
                "hint": "Two steps from 13 to 3 mean 2d = 3 − 13 = −10 -> d = −5!",
                "explanation": "2d = −10 ⟹ d = −5; going back one step gives a₁ = 13 − (−5) = 18, and forward gives a₃ = 13 + (−5) = 8.",
                "solution_steps": [
                    "Notice a₂ = 13 and a₄ = 3 -> a₄ − a₂ = 2d = −10 -> d = −5.",
                    "Find first box: a₁ = 13 − (−5) = 18.",
                    "Find third box: a₃ = 13 + (−5) = 8."
                ]
            },
            {
                "question": "If the 3rd and 9th terms of an AP are 4 and −8 respectively, WHICH term of this AP equals 0 (Exercise 5.2 Q9)?",
                "options": [
                    "5th term",
                    "4th term",
                    "6th term",
                    "7th term"
                ],
                "answer": 0,
                "hint": "Solve a + 2d = 4 and a + 8d = −8 -> 6d = −12 -> d = −2, a = 8!",
                "explanation": "d = −2, a = 8; setting 8 + (n − 1)(−2) = 0 gives n − 1 = 4 ⟹ 5th term = 0.",
                "solution_steps": [
                    "Subtract equations: 6d = −12 -> d = −2.",
                    "Plug d = −2 into a + 2(−2) = 4 -> a = 8.",
                    "Solve 8 + (n − 1)(−2) = 0 -> n = 5."
                ]
            },
            {
                "question": "Which term of the AP: 3, 15, 27, 39, ... will be 132 MORE than its 54th term (Exercise 5.2 Q11)?",
                "options": [
                    "65th term  (since extra 132 ÷ d = 132 ÷ 12 = +11 terms after 54th!)",
                    "64th term",
                    "66th term",
                    "77th term"
                ],
                "answer": 0,
                "hint": "Notice d = 12, so adding 132 adds 132/12 = 11 steps onto Term 54!",
                "explanation": "aₙ − a₅₄ = (n − 54)d = 132; with d = 12, n − 54 = 11 ⟹ n = 65th term.",
                "solution_steps": [
                    "Identify d = 15 − 3 = 12.",
                    "Target difference = +132 = 11 × 12 -> +11 steps beyond a₅₄.",
                    "54 + 11 = 65th term."
                ]
            },
            {
                "question": "Two APs share the EXACT same common difference d. The difference between their 100th terms is 100; what is the difference between their 1000th terms (Exercise 5.2 Q12)?",
                "options": [
                    "100  (the gap a − b stays permanently constant for ALL n!)",
                    "1,000",
                    "900",
                    "10"
                ],
                "answer": 0,
                "hint": "Compute [a + (n−1)d] − [b + (n−1)d] = a − b!",
                "explanation": "(n − 1)d cancels identically when subtracting corresponding terms, keeping the gap constant at a − b = 100 forever!",
                "solution_steps": [
                    "Write nth terms with equal d: Aₙ = a + (n−1)d, Bₙ = b + (n−1)d.",
                    "Subtract: Aₙ − Bₙ = a − b (independent of n!).",
                    "Since A₁₀₀ − B₁₀₀ = 100, A₁₀₀₀ − B₁₀₀₀ = 100 too."
                ]
            },
            {
                "question": "How many three-digit integers are divisible by 7 (Exercise 5.2 Q13)?",
                "options": [
                    "128  (from 105 to 994 stepping by 7)",
                    "127",
                    "129",
                    "142"
                ],
                "answer": 0,
                "hint": "Smallest 3-digit multiple = 105 (7×15), largest = 994 (7×142)! Solve 105 + (n−1)7 = 994!",
                "explanation": "994 − 105 = 889; 889 ÷ 7 = 127, so n = 127 + 1 = 128 integers.",
                "solution_steps": [
                    "Find endpoints: first = 105 (7×15), last = 994 (7×142).",
                    "Solve 105 + (n − 1)7 = 994 -> n − 1 = 127.",
                    "n = 128 three-digit multiples of 7."
                ]
            },
            {
                "question": "How many multiples of 4 lie between 10 and 250 (Exercise 5.2 Q14)?",
                "options": [
                    "60  (from 12 to 248)",
                    "59",
                    "61",
                    "62"
                ],
                "answer": 0,
                "hint": "First multiple > 10 is 12; last multiple < 250 is 248 (4×62)!",
                "explanation": "12 + (n − 1)4 = 248 ⟹ 4(n − 1) = 236 ⟹ n − 1 = 59 ⟹ n = 60 multiples.",
                "solution_steps": [
                    "Identify endpoints: a = 12, l = 248, d = 4.",
                    "Solve 12 + 4(n − 1) = 248 -> 4(n − 1) = 236 -> n − 1 = 59.",
                    "Conclude n = 60."
                ]
            },
            {
                "question": "For what value of n are the nth terms of TWO APs (63, 65, 67, ...) and (3, 10, 17, ...) EQUAL (Exercise 5.2 Q15)?",
                "options": [
                    "n = 13  (both equal 87)",
                    "n = 12",
                    "n = 14",
                    "n = 11"
                ],
                "answer": 0,
                "hint": "Equate 63 + (n − 1)(2) = 3 + (n − 1)(7) cleanly!",
                "explanation": "60 = 5(n − 1) ⟹ n − 1 = 12 ⟹ n = 13 (check: 63 + 24 = 87 and 3 + 84 = 87!).",
                "solution_steps": [
                    "Write nth terms: 63 + 2(n − 1) and 3 + 7(n − 1).",
                    "Set equal: 63 − 3 = (7 − 2)(n − 1) -> 60 = 5(n − 1).",
                    "Solve n − 1 = 12 -> n = 13."
                ]
            },
            {
                "question": "A saver deposits ₹5 in the first week of a year and increases weekly savings by ₹1.75 each week. In which nth week do weekly savings become ₹20.75 (Exercise 5.2 Q20)?",
                "options": [
                    "10th week",
                    "9th week",
                    "11th week",
                    "12th week"
                ],
                "answer": 0,
                "hint": "Solve 5 + (n − 1)(1.75) = 20.75 -> 15.75 ÷ 1.75 = 9!",
                "explanation": "(n − 1) = 15.75 / 1.75 = 9 ⟹ n = 10th week.",
                "solution_steps": [
                    "Set a = 5, d = 1.75, aₙ = 20.75.",
                    "Subtract 5: (n − 1)(1.75) = 15.75 -> n − 1 = 9.",
                    "n = 10th week."
                ]
            },
            {
                "question": "If the 4th and 8th terms of an AP sum to 24, while the 6th and 10th terms sum to 44 (Exercise 5.2 Q18), find the first three terms of the AP:",
                "options": [
                    "−13, −8, −3  (a = −13, d = +5)",
                    "−8, −3, 2",
                    "13, 8, 3",
                    "−13, −3, 7"
                ],
                "answer": 0,
                "hint": "2a + 10d = 24 and 2a + 14d = 44 subtract cleanly to 4d = 20 -> d = 5!",
                "explanation": "4d = 20 ⟹ d = 5; 2a + 50 = 24 ⟹ a = −13, giving −13, −8, −3.",
                "solution_steps": [
                    "Eq 1: (a + 3d) + (a + 7d) = 24 -> 2a + 10d = 24.",
                    "Eq 2: (a + 5d) + (a + 9d) = 44 -> 2a + 14d = 44.",
                    "Subtract -> 4d = 20 -> d = 5, a = −13 -> −13, −8, −3."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Exercise 5.3 Quiz",
        "subtitle": "Exercise 5.3 Practice: Summing APs, Finding n, Multiple Sums, Penalties & Cash Prizes",
        "questions": [
            {
                "question": "Find the sum of the finite series: 34 + 32 + 30 + ... + 10 (Exercise 5.3 Q2 ii):",
                "options": [
                    "286  (13 terms cleanly summing via (13/2)(34 + 10))",
                    "264",
                    "308",
                    "143"
                ],
                "answer": 0,
                "hint": "Find n first from 10 = 34 + (n − 1)(−2) -> n = 13, then apply (n/2)(a + l)!",
                "explanation": "n = 13; S₁₃ = (13/2)(34 + 10) = 13 × 22 = 286.",
                "solution_steps": [
                    "Compute n: 34 − 2(n − 1) = 10 -> 2(n − 1) = 24 -> n = 13.",
                    "Apply endpoint sum: S₁₃ = (13/2)(34 + 10).",
                    "Multiply 13 × 22 = 286."
                ]
            },
            {
                "question": "In an AP with a = 7 and a₁₃ = 35 (Exercise 5.3 Q3 ii), find d and S₁₃:",
                "options": [
                    "d = 7/3  and  S₁₃ = 273",
                    "d = 3  and  S₁₃ = 273",
                    "d = 7/3  and  S₁₃ = 286",
                    "d = 2.5  and  S₁₃ = 260"
                ],
                "answer": 0,
                "hint": "35 = 7 + 12d gives d = 28/12 = 7/3; S₁₃ = (13/2)(7 + 35)!",
                "explanation": "12d = 28 ⟹ d = 7/3; S₁₃ = (13/2)(42) = 13 × 21 = 273.",
                "solution_steps": [
                    "Solve 7 + 12d = 35 -> 12d = 28 -> d = 7/3.",
                    "Use S₁₃ = (13/2)(a + a₁₃) = (13/2)(7 + 35).",
                    "Compute 13 × 21 = 273."
                ]
            },
            {
                "question": "How many terms of AP: 9, 17, 25, ... must be taken to give a sum of 636 (Exercise 5.3 Q4)?",
                "options": [
                    "12 terms",
                    "13 terms",
                    "10 terms",
                    "15 terms"
                ],
                "answer": 0,
                "hint": "Solve (n/2)[18 + 8(n − 1)] = 636 ⟹ 4n² + 5n − 636 = 0!",
                "explanation": "4n² + 5n − 636 = (n − 12)(4n + 53) = 0 yields positive integer n = 12 terms.",
                "solution_steps": [
                    "Set up Sₙ = (n/2)[2(9) + (n − 1)8] = 636.",
                    "Simplify: n(5 + 4n) = 636 -> 4n² + 5n − 636 = 0.",
                    "Factor (n − 12)(4n + 53) = 0 -> n = 12 terms."
                ]
            },
            {
                "question": "The first term of an AP is 5, last term is 45, and total sum is 400 (Exercise 5.3 Q5). Find number of terms n and common difference d:",
                "options": [
                    "n = 16  and  d = 8/3",
                    "n = 16  and  d = 3",
                    "n = 15  and  d = 8/3",
                    "n = 20  and  d = 2"
                ],
                "answer": 0,
                "hint": "First use 400 = (n/2)(5 + 45) = 25n -> n = 16, then solve 45 = 5 + 15d!",
                "explanation": "25n = 400 ⟹ n = 16; then 5 + 15d = 45 ⟹ 15d = 40 ⟹ d = 8/3.",
                "solution_steps": [
                    "Apply Sₙ = (n/2)(5 + 45) = 400 -> 25n = 400 -> n = 16.",
                    "Set l = a + (n − 1)d -> 45 = 5 + 15d.",
                    "Solve d = 40/15 = 8/3."
                ]
            },
            {
                "question": "Find the sum of first 51 terms of an AP whose 2nd and 3rd terms are 14 and 18 respectively (Exercise 5.3 Q8):",
                "options": [
                    "5,610",
                    "5,510",
                    "5,100",
                    "2,805"
                ],
                "answer": 0,
                "hint": "d = 18 − 14 = 4, so a₁ = 14 − 4 = 10; compute S₅₁ = (51/2)[20 + 50(4)]!",
                "explanation": "S₅₁ = (51/2)(220) = 51 × 110 = 5,610.",
                "solution_steps": [
                    "Find d = a₃ − a₂ = 18 − 14 = 4; a = 14 − 4 = 10.",
                    "Apply S₅₁ = (51/2)[2(10) + 50(4)] = (51/2)(220).",
                    "Multiply 51 × 110 = 5,610."
                ]
            },
            {
                "question": "If the sum of the first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of the first n terms Sₙ (Exercise 5.3 Q9):",
                "options": [
                    "Sₙ = n²  (since a = 1 and d = 2)",
                    "Sₙ = 2n²",
                    "Sₙ = n(n + 1)/2",
                    "Sₙ = 7n"
                ],
                "answer": 0,
                "hint": "Notice S₇ = 7² and S₁₇ = 17² immediately! Verify a = 1, d = 2!",
                "explanation": "S₇/7 = a + 3d = 7 and S₁₇/17 = a + 8d = 17 solve cleanly to d = 2, a = 1; hence Sₙ = (n/2)[2 + 2(n−1)] = n².",
                "solution_steps": [
                    "Write (7/2)(2a + 6d) = 49 -> a + 3d = 7.",
                    "Write (17/2)(2a + 16d) = 289 -> a + 8d = 17.",
                    "Subtract -> 5d = 10 -> d = 2, a = 1 -> Sₙ = n²."
                ]
            },
            {
                "question": "Show that a₁, a₂, ..., aₙ defined by aₙ = 3 + 4n forms an AP (Ex 5.3 Q10 i), and find S₁₅:",
                "options": [
                    "Forms AP (a = 7, d = 4); S₁₅ = 525",
                    "Forms AP (a = 3, d = 4); S₁₅ = 465",
                    "Not an AP",
                    "S₁₅ = 600"
                ],
                "answer": 0,
                "hint": "Evaluate a₁ = 7, a₂ = 11, a₁₅ = 63, then S₁₅ = (15/2)(7 + 63)!",
                "explanation": "aₖ₊₁ − aₖ = 4 consistently (AP with a = 7, d = 4); S₁₅ = (15/2)(7 + 63) = 15 × 35 = 525.",
                "solution_steps": [
                    "Check linear form aₙ = 3 + 4n -> a₁ = 7, a₂ = 11 -> d = 4.",
                    "Compute a₁₅ = 3 + 4(15) = 63.",
                    "Sum S₁₅ = (15/2)(7 + 63) = 15 × 35 = 525."
                ]
            },
            {
                "question": "A construction contract specifies delay penalties: ₹200 for Day 1, ₹250 for Day 2, ₹300 for Day 3... How much total penalty does a 30-day delay cost (Ex 5.3 Q15)?",
                "options": [
                    "₹27,750",
                    "₹25,500",
                    "₹30,000",
                    "₹22,500"
                ],
                "answer": 0,
                "hint": "Use S₃₀ = (30/2)[2(200) + 29(50)] = 15 × (400 + 1450)!",
                "explanation": "S₃₀ = 15 × 1,850 = ₹27,750.",
                "solution_steps": [
                    "Identify a = 200, d = 50, n = 30.",
                    "Substitute: S₃₀ = 15[400 + 29(50)] = 15 × 1,850.",
                    "Multiply cleanly: ₹27,750."
                ]
            },
            {
                "question": "A sum of ₹700 is used to award 7 academic cash prizes where each prize is ₹20 less than the preceding prize (Ex 5.3 Q16). Find the value of the highest (first) prize:",
                "options": [
                    "₹160  (prizes: 160, 140, 120, 100, 80, 60, 40)",
                    "₹140",
                    "₹180",
                    "₹120"
                ],
                "answer": 0,
                "hint": "Set S₇ = (7/2)[2a + 6(−20)] = 700 -> a − 60 = 100!",
                "explanation": "Average prize (4th prize) = 700 ÷ 7 = ₹100; going back 3 steps of +20 gives highest prize 100 + 60 = ₹160!",
                "solution_steps": [
                    "Set S₇ = (7/2)[2a + 6(−20)] = 700.",
                    "Divide both sides by 7 -> a − 60 = 100.",
                    "Solve highest prize a = ₹160."
                ]
            },
            {
                "question": "Students plant trees equal to their class number across 3 sections per class, from Class 1 to Class 12 (Ex 5.3 Q17). How many total trees are planted?",
                "options": [
                    "234 trees  [3 × (1 + 2 + ... + 12) = 3 × 78]",
                    "78 trees",
                    "156 trees",
                    "252 trees"
                ],
                "answer": 0,
                "hint": "Class 1 plants 3×1=3, Class 2 plants 3×2=6, ..., Class 12 plants 3×12=36!",
                "explanation": "AP 3, 6, 9, ..., 36 for n = 12 classes: S₁₂ = (12/2)(3 + 36) = 6 × 39 = 234 trees.",
                "solution_steps": [
                    "Class k across 3 sections plants 3k trees -> AP 3, 6, ..., 36.",
                    "Use S₁₂ = (12/2)(3 + 36) = 6 × 39.",
                    "Total = 234 trees planted."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Optional Challenge Quiz",
        "subtitle": "Optional Exercise 5.4 & Mastery Challenge: Negative Terms, Ladder Wood, House 35 & Mean",
        "questions": [
            {
                "question": "If the sum of the 3rd and 7th terms of an AP is 6 and their product is 8, find the sum of the first 16 terms S₁₆ (Optional Ex 5.4 Q2, taking d > 0):",
                "options": [
                    "76  (note: with d = −1/2, S₁₆ = 20 as second case!)",
                    "84",
                    "64",
                    "48"
                ],
                "answer": 0,
                "hint": "Since (a₃ + a₇) = 2a₅ = 6, middle 5th term a₅ = 3 immediately! Write a₃ = 3 − 2d, a₇ = 3 + 2d -> (3−2d)(3+2d) = 8!",
                "explanation": "9 − 4d² = 8 ⟹ d = ±1/2. Taking d = +1/2 gives a = 3 − 4(1/2) = 1; S₁₆ = 8[2 + 15(1/2)] = 4(19) = 76 (with d = −1/2 giving a = 5, S₁₆ = 20).",
                "solution_steps": [
                    "From a₃ + a₇ = 6 -> 2(a + 4d) = 6 -> a₅ = a + 4d = 3.",
                    "Product (3 − 2d)(3 + 2d) = 8 -> 9 − 4d² = 8 -> d = ±1/2.",
                    "For d = +1/2, a = 1 -> S₁₆ = 8[2 + 7.5] = 76."
                ]
            },
            {
                "question": "A ladder has rungs 25 cm apart decreasing uniformly from 45 cm at bottom to 25 cm at top. If top and bottom rungs lie 2.5 m (250 cm) apart, how many rungs exist and what total wood length is needed (Optional Ex 5.4 Q3)?",
                "options": [
                    "11 rungs totaling 385 cm of wood",
                    "10 rungs totaling 350 cm of wood",
                    "11 rungs totaling 350 cm of wood",
                    "10 rungs totaling 385 cm of wood"
                ],
                "answer": 0,
                "hint": "Fence-post count: number of rungs = (250 ÷ 25) + 1 = 11 rungs; total = (11/2)(45 + 25)!",
                "explanation": "Rung count = 250/25 + 1 = 11 rungs; S₁₁ = (11/2)(45 + 25) = 11 × 35 = 385 cm.",
                "solution_steps": [
                    "Compute number of rungs inclusively: (250 ÷ 25) + 1 = 11.",
                    "Apply endpoint sum formula: S₁₁ = (11/2)(45 + 25).",
                    "Multiply 11 × 35 = 385 cm."
                ]
            },
            {
                "question": "If the sum of the first n terms of an AP is (1/2)(3n² + 7n), find its nth term aₙ cleanly:",
                "options": [
                    "aₙ = 3n + 2",
                    "aₙ = 3n + 5",
                    "aₙ = 6n + 2",
                    "aₙ = 3n − 1"
                ],
                "answer": 0,
                "hint": "Evaluate a₁ = S₁ = 5, S₂ = 13 -> a₂ = 8 -> d = 3, OR compute Sₙ − Sₙ₋₁!",
                "explanation": "a₁ = (3 + 7)/2 = 5, S₂ = (12 + 14)/2 = 13 so a₂ = 13 − 5 = 8 (d = 3), giving aₙ = 5 + (n − 1)3 = 3n + 2.",
                "solution_steps": [
                    "Find S₁ = a₁ = (3 + 7)/2 = 5.",
                    "Find S₂ = (12 + 14)/2 = 13 -> a₂ = 13 − 5 = 8 -> d = 3.",
                    "Write aₙ = 5 + (n − 1)3 = 3n + 2."
                ]
            },
            {
                "question": "If 7 times the 7th term of an AP equals 11 times its 11th term, what MUST its 18th term a₁₈ equal?",
                "options": [
                    "0",
                    "18",
                    "77",
                    "−1"
                ],
                "answer": 0,
                "hint": "Expand 7(a + 6d) = 11(a + 10d) cleanly to solve for a + 17d!",
                "explanation": "7a + 42d = 11a + 110d ⟹ 4a + 68d = 0 ⟹ 4(a + 17d) = 0 ⟹ a₁₈ = a + 17d = 0 ALWAYS!",
                "solution_steps": [
                    "Set up 7(a + 6d) = 11(a + 10d).",
                    "Collect terms: 4a + 68d = 0 -> divide by 4.",
                    "Obtain a + 17d = a₁₈ = 0."
                ]
            },
            {
                "question": "Find the middle term of the finite AP: 6, 13, 20, ..., 216:",
                "options": [
                    "111  (16th term out of 31 terms)",
                    "104",
                    "118",
                    "97"
                ],
                "answer": 0,
                "hint": "First find n from 216 = 6 + 7(n − 1) -> n = 31; middle term is (31+1)/2 = 16th term = (6+216)/2!",
                "explanation": "210 ÷ 7 = 30 ⟹ n = 31 terms; middle term a₁₆ = 6 + 15(7) = 111 (= Arithmetic Mean (6+216)/2!).",
                "solution_steps": [
                    "Find total terms: 6 + 7(n − 1) = 216 -> n = 31.",
                    "Middle position for odd n = 31 is (31 + 1)/2 = 16th term.",
                    "Evaluate a₁₆ = 6 + 15(7) = 111."
                ]
            },
            {
                "question": "If the ratio of sums of first n terms of two APs is (7n + 1) : (4n + 27), find the ratio of their 9th terms (A₉ : B₉):",
                "options": [
                    "24 : 19  (plugging n = 2(9) − 1 = 17 directly into the sum ratio!)",
                    "64 : 63",
                    "7 : 4",
                    "15 : 19"
                ],
                "answer": 0,
                "hint": "Notice S_{2m-1} / s_{2m-1} = (2m−1)[a+(m−1)d] / (2m−1)[A+(m−1)D] = m-th term ratio! Set m = 9 -> n = 17!",
                "explanation": "At n = 2(9) − 1 = 17, S₁₇/S'₁₇ = (a + 8d)/(A + 8D) = a₉/A₉! Plugging n = 17 gives (119 + 1) : (68 + 27) = 120 : 95 = 24 : 19.",
                "solution_steps": [
                    "Match [2a + (n − 1)d]/2 with a + 8d -> set (n − 1)/2 = 8 -> n = 17.",
                    "Evaluate (7(17) + 1) : (4(17) + 27) = 120 : 95.",
                    "Simplify by 5 -> 24 : 19."
                ]
            },
            {
                "question": "If aₙ = 5 − 11n defines an AP, determine its common difference d immediately:",
                "options": [
                    "−11",
                    "5",
                    "−6",
                    "+11"
                ],
                "answer": 0,
                "hint": "In any linear AP formula aₙ = A + Bn, the coefficient of n is ALWAYS d!",
                "explanation": "a₁ = −6, a₂ = −17 ⟹ d = −17 − (−6) = −11 (directly the coefficient of n).",
                "solution_steps": [
                    "Compute a₁ = 5 − 11(1) = −6.",
                    "Compute a₂ = 5 − 11(2) = −17.",
                    "Subtract: d = −17 − (−6) = −11."
                ]
            },
            {
                "question": "If 18, a, b, −3 are in Arithmetic Progression, find a + b directly without even finding d individually:",
                "options": [
                    "15  (since a + b ALWAYS equals first + last = 18 + (−3))",
                    "21",
                    "12",
                    "−15"
                ],
                "answer": 0,
                "hint": "In any finite AP, terms equidistant from the beginning and end sum to the exact same value a₁ + aₙ!",
                "explanation": "(18 + d) + (−3 − d) = 18 + (−3) = 15 (check: d = −7 gives 18, 11, 4, −3 -> 11 + 4 = 15!).",
                "solution_steps": [
                    "Write a = 18 + d and b = −3 − d.",
                    "Add a + b = (18 + d) + (−3 − d) -> d cancels cleanly.",
                    "Sum = 18 − 3 = 15."
                ]
            },
            {
                "question": "How many terms of AP −6, −11/2, −5, ... are needed to give the sum −25?",
                "options": [
                    "5 terms OR 20 terms  (both give −25!)",
                    "Only 5 terms",
                    "Only 10 terms",
                    "No integer number of terms"
                ],
                "answer": 0,
                "hint": "a = −6, d = +1/2; set (n/2)[−12 + (n − 1)(1/2)] = −25 -> n² − 25n + 100 = 0!",
                "explanation": "n² − 25n + 100 = (n − 5)(n − 20) = 0 gives BOTH n = 5 and n = 20 (since terms 6 through 20 cancel symmetrically around zero term a₁₃ = 0!).",
                "solution_steps": [
                    "Identify a = −6, d = +1/2.",
                    "Solve (n/2)[−12 + (n − 1)/2] = −25 -> n² − 25n + 100 = 0.",
                    "Factor (n − 5)(n − 20) = 0 -> n = 5 or 20."
                ]
            },
            {
                "question": "Which comprehensive takeaway accurately unifies NCERT Class 10 Chapter 5: Arithmetic Progressions?",
                "options": [
                    "Constant step d generates aₙ = a + (n−1)d, Gauss's pairing Sₙ = (n/2)[2a + (n−1)d] = (n/2)(a + l), recovery aₙ = Sₙ − Sₙ₋₁, and Arithmetic Mean (a+c)/2",
                    "Only positive integers can be common difference d in an AP",
                    "Sum of terms can never produce two distinct positive integer n solutions",
                    "Terms from the end keep the same positive sign on d"
                ],
                "answer": 0,
                "hint": "Verify every Chapter 5 identity and rule cleanly!",
                "explanation": "Chapter 5 masters linear sequence step d (positive, zero, or negative), nth terms (forward/reverse), Gauss summations, and Arithmetic Mean.",
                "solution_steps": [
                    "Reject false claims (d may be 0 or negative; double Sₙ solutions happen when terms cross 0; reverse d swaps sign).",
                    "Verify aₙ, Sₙ, Sₙ − Sₙ₋₁, and Arithmetic Mean formulas.",
                    "Select master summary statement."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch5 Class 10 Maths Part 3.")
    for s in slides_part3:
        twc = len(s["title"].split())
        q_count = len(s["questions"])
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Questions: {q_count}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert q_count == 10, f"Slide {s['id']} has {q_count} questions, expected 10"
        for qidx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4
            assert 0 <= q["answer"] <= 3
            assert len(q["solution_steps"]) == 3
            assert len(q["hint"]) > 5
            assert len(q["explanation"]) > 10
    print("All 40 exercise & challenge questions verified successfully!")

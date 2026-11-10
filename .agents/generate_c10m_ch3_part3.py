#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 3: Pair of Linear Equations in Two Variables
Data Generator - Part 3 (Slides 17 to 20: Exercises 3.1, 3.2 & Challenges)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Questions: Exactly 10 questions per slide (40 questions total)
- Zero spoken lecture on Exercise/Quiz slides ("except exercises")
- Zero human character names (Akhila, Champa, Aftab, Meena, Nuri, Sonu, Raghav, etc.), zero lecturer personas
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise 3.1 Quiz",
        "subtitle": "Exercise 3.1 Practice: Modeling, Graphical Consistency, Ratio Table 3.1 & Linear Line Plots",
        "questions": [
            {
                "question": "10 students of Class X took part in a Mathematics quiz; number of girls y is 4 more than number of boys x (Exercise 3.1 Q1 i). Model the linear pair:",
                "options": [
                    "x + y = 10   and   y − x = 4   (solving to 3 boys and 7 girls)",
                    "x − y = 10   and   x + y = 4",
                    "x + y = 10   and   x − y = 4   (7 boys, 3 girls)",
                    "x + y = 14   and   y = 4x"
                ],
                "answer": 0,
                "hint": "Girls + Boys = 10, and Girls = Boys + 4!",
                "explanation": "y = x + 4 ⟹ y − x = 4 alongside x + y = 10 gives 2y = 14 ⟹ y = 7 girls, x = 3 boys.",
                "solution_steps": [
                    "Set total students: x + y = 10.",
                    "Express '4 more girls than boys': y = x + 4 -> y − x = 4.",
                    "Solve intersection: x = 3 boys, y = 7 girls."
                ]
            },
            {
                "question": "5 pencils and 7 pens cost ₹50, while 7 pencils and 5 pens cost ₹46 (Exercise 3.1 Q1 ii). Find the cost of 1 pencil (x) and 1 pen (y):",
                "options": [
                    "Pencil = ₹3, Pen = ₹5",
                    "Pencil = ₹5, Pen = ₹3",
                    "Pencil = ₹4, Pen = ₹4",
                    "Pencil = ₹2, Pen = ₹6"
                ],
                "answer": 0,
                "hint": "Add 5x+7y=50 and 7x+5y=46 giving 12(x+y)=96 -> x+y=8, and subtract giving 2(y−x)=4 -> y−x=2!",
                "explanation": "x + y = 8 and y − x = 2 solve cleanly to x = ₹3 (pencil) and y = ₹5 (pen).",
                "solution_steps": [
                    "Add both symmetric equations: 12(x + y) = 96 -> x + y = 8.",
                    "Subtract equations: 2(y − x) = 4 -> y − x = 2.",
                    "Add x + y = 8 and y − x = 2 -> y = 5, x = 3."
                ]
            },
            {
                "question": "Compare ratios a₁/a₂, b₁/b₂, c₁/c₂ for 5x − 4y + 8 = 0 and 7x + 6y − 9 = 0 (Exercise 3.1 Q2 i) to classify the lines:",
                "options": [
                    "Intersecting at a point (since a₁/a₂ = 5/7 ≠ b₁/b₂ = −2/3)",
                    "Parallel lines",
                    "Coincident lines",
                    "Both vertical lines"
                ],
                "answer": 0,
                "hint": "Notice positive 5/7 vs negative −4/6 = −2/3 immediately!",
                "explanation": "a₁/a₂ = 5/7 ≠ b₁/b₂ = −2/3 guarantees intersecting lines with a unique solution.",
                "solution_steps": [
                    "Compute a₁/a₂ = 5/7.",
                    "Compute b₁/b₂ = −4/6 = −2/3.",
                    "Since 5/7 ≠ −2/3, Table 3.1 gives intersecting lines."
                ]
            },
            {
                "question": "Compare ratios for 9x + 3y + 12 = 0 and 18x + 6y + 24 = 0 (Exercise 3.1 Q2 ii):",
                "options": [
                    "Coincident lines (all three ratios equal 1/2)",
                    "Intersecting at one point",
                    "Parallel lines",
                    "Inconsistent pair"
                ],
                "answer": 0,
                "hint": "Simplify 9/18, 3/6, and 12/24 cleanly!",
                "explanation": "9/18 = 3/6 = 12/24 = 1/2 satisfies a₁/a₂ = b₁/b₂ = c₁/c₂ for coincident lines.",
                "solution_steps": [
                    "Evaluate a₁/a₂ = 9/18 = 1/2.",
                    "Evaluate b₁/b₂ = 3/6 = 1/2 and c₁/c₂ = 12/24 = 1/2.",
                    "All three equal -> coincident lines (infinitely many solutions)."
                ]
            },
            {
                "question": "Check consistency of pair (3/2)x + (5/3)y = 7 and 9x − 10y = 14 (Exercise 3.1 Q3 iii):",
                "options": [
                    "Consistent (Intersecting), since a₁/a₂ = 1/6 ≠ b₁/b₂ = −1/6",
                    "Inconsistent (Parallel), since 7/14 = 1/2",
                    "Coincident lines",
                    "Zero solutions"
                ],
                "answer": 0,
                "hint": "Watch the opposite signs on y coefficients: +(5/3) vs −10!",
                "explanation": "(3/2)/9 = 1/6 while (5/3)/(−10) = −1/6. Since +1/6 ≠ −1/6, lines intersect cleanly -> CONSISTENT.",
                "solution_steps": [
                    "Compute a₁/a₂ = (3/2) ÷ 9 = 1/6.",
                    "Compute b₁/b₂ = (5/3) ÷ (−10) = −1/6.",
                    "1/6 ≠ −1/6 implies unique intersection (consistent)."
                ]
            },
            {
                "question": "Which pair below is INCONSISTENT (parallel lines, no solution)? Check carefully!",
                "options": [
                    "2x − 2y − 2 = 0  and  4x − 4y − 5 = 0  (Ex 3.1 Q4 iv: ratios 1/2 = 1/2 ≠ 2/5)",
                    "x + y = 5  and  2x + 2y = 10",
                    "x − y = 8  and  3x − 3y = 24",
                    "2x + y − 6 = 0  and  4x − 2y − 4 = 0"
                ],
                "answer": 0,
                "hint": "Verify a₁/a₂ = b₁/b₂ ≠ c₁/c₂: check 2/4 = (−2)/(−4) = 1/2 vs (−2)/(−5) = 2/5!",
                "explanation": "In 2x − 2y − 2 = 0 and 4x − 4y − 5 = 0, a₁/a₂ = b₁/b₂ = 1/2 while c₁/c₂ = 2/5 ≠ 1/2, making the lines parallel & inconsistent.",
                "solution_steps": [
                    "Compare 2/4 = 1/2 and (−2)/(−4) = 1/2.",
                    "Compare constant ratio (−2)/(−5) = 2/5.",
                    "1/2 = 1/2 ≠ 2/5 confirms parallel inconsistent pair."
                ]
            },
            {
                "question": "Write ANY second equation to accompany 2x + 3y − 8 = 0 so the pair becomes PARALLEL lines (Exercise 3.1 Q6 ii):",
                "options": [
                    "4x + 6y − 10 = 0  (same a:b ratio scaled ×2, different constant c ≠ −16)",
                    "4x + 6y − 16 = 0",
                    "3x + 2y − 8 = 0",
                    "2x − 3y − 8 = 0"
                ],
                "answer": 0,
                "hint": "Multiply 2x + 3y by 2 giving 4x + 6y, and pick ANY constant other than 2×(−8) = −16!",
                "explanation": "4x + 6y − 10 = 0 keeps 2/4 = 3/6 = 1/2 while (−8)/(−10) = 4/5 ≠ 1/2, creating parallel lines (4x+6y−16=0 would be coincident!).",
                "solution_steps": [
                    "Scale x and y terms uniformly: (2x + 3y) × 2 = 4x + 6y.",
                    "Avoid scaling constant −8 by 2 (which gives coincident −16).",
                    "Pick any other constant (e.g., −10) -> parallel lines!"
                ]
            },
            {
                "question": "Determine the vertices of the triangle formed by x − y + 1 = 0, 3x + 2y − 12 = 0, and the x-axis (Exercise 3.1 Q7):",
                "options": [
                    "(2, 3), (−1, 0), and (4, 0)",
                    "(2, 3), (1, 0), and (6, 0)",
                    "(0, 1), (0, 6), and (2, 3)",
                    "(3, 2), (−1, 0), and (4, 0)"
                ],
                "answer": 0,
                "hint": "Check apex (2, 3) inside BOTH lines and set y = 0 in each equation for x-axis corners!",
                "explanation": "Lines intersect at (2, 3); setting y = 0 gives x = −1 on Line 1 -> (−1, 0) and 3x = 12 -> x = 4 on Line 2 -> (4, 0).",
                "solution_steps": [
                    "Solve x − y + 1 = 0 and 3x + 2y − 12 = 0 -> apex (2, 3).",
                    "Set y = 0 in Line 1 -> x = −1 -> base vertex (−1, 0).",
                    "Set y = 0 in Line 2 -> 3x = 12 -> base vertex (4, 0)."
                ]
            },
            {
                "question": "Using the vertices (−1, 0), (4, 0), and (2, 3) from Q8 above, calculate the exact area of that triangular region:",
                "options": [
                    "7.5 square units",
                    "15 square units",
                    "5 square units",
                    "10 square units"
                ],
                "answer": 0,
                "hint": "Base length along x-axis from x = −1 to x = 4 is 5 units, and height y at apex (2, 3) is 3 units!",
                "explanation": "Area = (1/2) × base × height = (1/2) × (4 − (−1)) × 3 = (1/2) × 5 × 3 = 7.5 sq units.",
                "solution_steps": [
                    "Compute base along x-axis: 4 − (−1) = 5 units.",
                    "Read perpendicular height from x-axis to apex (2, 3): 3 units.",
                    "Area = (1/2) × 5 × 3 = 7.5 square units."
                ]
            },
            {
                "question": "If 2x + 3y − 8 = 0 is paired with 4x + 6y − 16 = 0, how many solutions exist?",
                "options": [
                    "Infinitely many solutions (dependent coincident lines)",
                    "Exactly 1 unique solution",
                    "0 solutions",
                    "2 solutions"
                ],
                "answer": 0,
                "hint": "Check 2/4, 3/6, and (−8)/(−16)!",
                "explanation": "2/4 = 3/6 = (−8)/(−16) = 1/2, so all three ratios match -> coincident lines with infinitely many solutions.",
                "solution_steps": [
                    "Verify a₁/a₂ = 2/4 = 1/2 and b₁/b₂ = 3/6 = 1/2.",
                    "Verify c₁/c₂ = (−8)/(−16) = 1/2.",
                    "Conclude infinitely many solutions."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise 3.2 Quiz",
        "subtitle": "Exercise 3.2 Practice: Solving Systems via Substitution & Elimination + Word Applications",
        "questions": [
            {
                "question": "Solve s − t = 3 and (s/3) + (t/2) = 6 cleanly using Substitution (Exercise 3.2 Q1 ii):",
                "options": [
                    "s = 9, t = 6",
                    "s = 6, t = 3",
                    "s = 12, t = 9",
                    "s = 8, t = 5"
                ],
                "answer": 0,
                "hint": "Clear fractions first by multiplying (s/3)+(t/2)=6 by 6 -> 2s + 3t = 36, then substitute s = 3 + t!",
                "explanation": "2(3 + t) + 3t = 36 ⟹ 6 + 5t = 36 ⟹ 5t = 30 ⟹ t = 6, so s = 3 + 6 = 9.",
                "solution_steps": [
                    "Express s = 3 + t from Equation 1; multiply Eq 2 by 6 -> 2s + 3t = 36.",
                    "Substitute: 2(3 + t) + 3t = 36 -> 5t = 30 -> t = 6.",
                    "Back-substitute s = 3 + 6 = 9."
                ]
            },
            {
                "question": "Solve 0.2x + 0.3y = 1.3 and 0.4x + 0.5y = 2.3 (Exercise 3.2 Q1 iv):",
                "options": [
                    "x = 2, y = 3",
                    "x = 3, y = 2",
                    "x = 0.2, y = 0.3",
                    "x = 4, y = 1"
                ],
                "answer": 0,
                "hint": "Multiply BOTH equations by 10 immediately to banish all decimals: 2x + 3y = 13 and 4x + 5y = 23!",
                "explanation": "Doubling 2x+3y=13 gives 4x+6y=26; subtracting 4x+5y=23 gives y = 3, and 2x + 9 = 13 ⟹ x = 2.",
                "solution_steps": [
                    "Multiply both equations by 10: 2x + 3y = 13 and 4x + 5y = 23.",
                    "Double Eq 1 (4x + 6y = 26) and subtract Eq 2 -> y = 3.",
                    "Plug y = 3 into 2x + 9 = 13 -> x = 2."
                ]
            },
            {
                "question": "Solve √2 x + √3 y = 0 and √3 x − √8 y = 0 (Exercise 3.2 Q1 v):",
                "options": [
                    "x = 0, y = 0  (both lines pass through origin with distinct slopes)",
                    "No solution",
                    "x = √2, y = √3",
                    "Infinitely many solutions"
                ],
                "answer": 0,
                "hint": "Check a₁/a₂ = √2/√3 vs b₁/b₂ = −√3/√8 (opposite signs -> intersect at one point!), and note c₁ = c₂ = 0!",
                "explanation": "Since √2/√3 ≠ −√3/√8, the unique solution is (0, 0) (check: substituting x = −√(3/2) y forces y = 0).",
                "solution_steps": [
                    "Isolate x = −(√3/√2)y from Eq 1.",
                    "Substitute into Eq 2: [−3/√2 − √8]y = 0 -> coefficient ≠ 0 -> y = 0.",
                    "Conclude x = 0, y = 0."
                ]
            },
            {
                "question": "Solve 2x + 3y = 11 and 2x − 4y = −24, and hence find m where y = mx + 3 (Exercise 3.2 Q2):",
                "options": [
                    "x = −2, y = 5, giving m = −1",
                    "x = 2, y = 5, giving m = 1",
                    "x = −2, y = −5, giving m = 4",
                    "x = 4, y = 1, giving m = −1/2"
                ],
                "answer": 0,
                "hint": "Subtract the two equations right away to cancel 2x: 7y = 35 -> y = 5!",
                "explanation": "Subtracting gives 7y = 35 ⟹ y = 5, so 2x = 11 − 15 = −4 ⟹ x = −2. Then 5 = m(−2) + 3 ⟹ −2m = 2 ⟹ m = −1.",
                "solution_steps": [
                    "Subtract Eq 2 from Eq 1 directly: 3y − (−4y) = 11 − (−24) -> 7y = 35 -> y = 5.",
                    "Substitute y = 5 into 2x + 15 = 11 -> x = −2.",
                    "Plug (−2, 5) into 5 = −2m + 3 -> m = −1."
                ]
            },
            {
                "question": "The larger of two supplementary angles exceeds the smaller by 18° (Exercise 3.2 Q3 ii). Find both angles:",
                "options": [
                    "99° and 81°",
                    "108° and 72°",
                    "54° and 36°",
                    "100° and 80°"
                ],
                "answer": 0,
                "hint": "Supplementary angles sum to 180° (x + y = 180), and x − y = 18!",
                "explanation": "Adding x + y = 180 and x − y = 18 gives 2x = 198 ⟹ x = 99°, and y = 81°.",
                "solution_steps": [
                    "Set linear pair: x + y = 180° and x − y = 18°.",
                    "Add equations cleanly: 2x = 198° -> x = 99°.",
                    "Subtract to get y = 180° − 99° = 81°."
                ]
            },
            {
                "question": "A taxi charges a fixed flag-down fee plus distance rate/km. 10 km costs ₹105 and 15 km costs ₹155 (Exercise 3.2 Q3 iv). Find fixed charge x, rate y/km, and 25 km fare:",
                "options": [
                    "Fixed ₹5, rate ₹10/km, 25 km fare = ₹255",
                    "Fixed ₹10, rate ₹5/km, 25 km fare = ₹135",
                    "Fixed ₹15, rate ₹9/km, 25 km fare = ₹240",
                    "Fixed ₹5, rate ₹12/km, 25 km fare = ₹305"
                ],
                "answer": 0,
                "hint": "Subtract x + 10y = 105 from x + 15y = 155 immediately!",
                "explanation": "5y = 50 ⟹ rate y = ₹10/km, fixed charge x = 105 − 100 = ₹5; 25 km fare = 5 + 25(10) = ₹255.",
                "solution_steps": [
                    "Model equations: x + 10y = 105 and x + 15y = 155.",
                    "Eliminate x by subtracting -> 5y = 50 -> y = ₹10/km, x = ₹5.",
                    "Compute 25 km cost: 5 + 25×10 = ₹255."
                ]
            },
            {
                "question": "Solve x/2 + 2y/3 = −1 and x − y/3 = 3 by Elimination (Exercise 3.2 Q1 iv):",
                "options": [
                    "x = 2, y = −3",
                    "x = 3, y = −2",
                    "x = −2, y = 3",
                    "x = 4, y = 3"
                ],
                "answer": 0,
                "hint": "Clear denominators: multiply Eq 1 by 6 -> 3x + 4y = −6, and Eq 2 by 3 -> 3x − y = 9!",
                "explanation": "Subtracting (3x − y = 9) from (3x + 4y = −6) gives 5y = −15 ⟹ y = −3, and 3x = 9 − 3 = 6 ⟹ x = 2.",
                "solution_steps": [
                    "Clear fractions: 3x + 4y = −6 and 3x − y = 9.",
                    "Subtract cleanly to eliminate 3x -> 5y = −15 -> y = −3.",
                    "Substitute y = −3 into 3x − (−3) = 9 -> 3x = 6 -> x = 2."
                ]
            },
            {
                "question": "A lending library charges a fixed fee for the first 3 days and a daily fee thereafter. Keeping a book 7 days costs ₹27, and 5 days costs ₹21 (Ex 3.2 Q2 v). Find fixed 3-day charge x and extra daily rate y:",
                "options": [
                    "Fixed 3-day fee = ₹15, extra daily charge = ₹3/day",
                    "Fixed 3-day fee = ₹12, extra daily charge = ₹5/day",
                    "Fixed 3-day fee = ₹18, extra daily charge = ₹3/day",
                    "Fixed 3-day fee = ₹9, extra daily charge = ₹6/day"
                ],
                "answer": 0,
                "hint": "Careful! 7 total days includes 3 fixed days + 4 extra days (x + 4y = 27); 5 total days = 3 fixed + 2 extra (x + 2y = 21)!",
                "explanation": "Subtracting x + 2y = 21 from x + 4y = 27 gives 2y = 6 ⟹ y = ₹3/day, and fixed fee x = 21 − 6 = ₹15.",
                "solution_steps": [
                    "Subtract initial 3 days carefully: 7 days -> x + 4y = 27; 5 days -> x + 2y = 21.",
                    "Subtract equations: 2y = 6 -> extra daily charge y = ₹3.",
                    "Solve fixed 3-day fee x = 21 − 2(3) = ₹15."
                ]
            },
            {
                "question": "A bank customer asks a cashier strictly for ₹50 and ₹100 currency notes totaling ₹2,000 across 25 notes altogether (Ex 3.2 Q2 iv). Find the number of ₹50 (x) and ₹100 (y) notes:",
                "options": [
                    "10 notes of ₹50 and 15 notes of ₹100",
                    "15 notes of ₹50 and 10 notes of ₹100",
                    "5 notes of ₹50 and 20 notes of ₹100",
                    "12 notes of ₹50 and 13 notes of ₹100"
                ],
                "answer": 0,
                "hint": "x + y = 25 and 50x + 100y = 2000 (divide second by 50 -> x + 2y = 40)!",
                "explanation": "Subtracting x + y = 25 from x + 2y = 40 gives y = 15 (₹100 notes) and x = 10 (₹50 notes).",
                "solution_steps": [
                    "Write equations: x + y = 25 and 50x + 100y = 2000.",
                    "Divide Eq 2 by 50 -> x + 2y = 40.",
                    "Subtract Eq 1 -> y = 15 (₹100 notes), x = 10 (₹50 notes)."
                ]
            },
            {
                "question": "If we add 1 to numerator and subtract 1 from denominator, a fraction reduces to 1. It becomes 1/2 if we only add 1 to denominator (Ex 3.2 Q2 i). Find the fraction:",
                "options": [
                    "3 / 5",
                    "2 / 3",
                    "4 / 7",
                    "5 / 9"
                ],
                "answer": 0,
                "hint": "(x+1)/(y−1) = 1 gives x − y = −2; x/(y+1) = 1/2 gives 2x − y = 1!",
                "explanation": "Subtracting (x − y = −2) from (2x − y = 1) eliminates y -> x = 3, and y = 5 (check: 4/4 = 1 and 3/6 = 1/2).",
                "solution_steps": [
                    "Simplify Eq 1: x + 1 = y − 1 -> x − y = −2.",
                    "Simplify Eq 2: 2x = y + 1 -> 2x − y = 1.",
                    "Subtract cleanly -> x = 3, y = 5 -> fraction 3/5."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge Quiz 1",
        "subtitle": "Mastery Challenge: Unknown Constant (k, a, b) Consistency, Ratios & Special Symmetric Pairs",
        "questions": [
            {
                "question": "For which value of k does the system 3x − y − 5 = 0 and 6x − 2y − k = 0 have NO solution?",
                "options": [
                    "Any real number k EXCEPT 10  (k ≠ 10)",
                    "Only k = 10",
                    "Only k = 0",
                    "Only k = −10"
                ],
                "answer": 0,
                "hint": "Notice 3/6 = (−1)/(−2) = 1/2! Parallel lines need (−5)/(−k) ≠ 1/2!",
                "explanation": "k = 10 produces coincident lines (5/10 = 1/2); every other k ≠ 10 forces 5/k ≠ 1/2 -> parallel lines with zero solutions.",
                "solution_steps": [
                    "Verify slope equality: 3/6 = 1/2 and (−1)/(−2) = 1/2.",
                    "Apply parallel condition c₁/c₂ ≠ 1/2: (−5)/(−k) ≠ 1/2.",
                    "Conclude k ≠ 10 yields parallel lines with no solution."
                ]
            },
            {
                "question": "For what exact values of a and b does 2x + 3y = 7 and (a − b)x + (a + b)y = 3a + b − 2 have INFINITELY MANY solutions?",
                "options": [
                    "a = 5, b = 1",
                    "a = 1, b = 5",
                    "a = 3, b = 2",
                    "a = −5, b = 1"
                ],
                "answer": 0,
                "hint": "Set 2/(a−b) = 3/(a+b) = 7/(3a+b−2)! Cross-multiplying first pair gives a = 5b!",
                "explanation": "2(a + b) = 3(a − b) ⟹ a = 5b. Plugging a = 5b into 3/(6b) = 7/(16b − 2) gives 1/(2b) = 7/(16b − 2) ⟹ 16b − 2 = 14b ⟹ b = 1, a = 5.",
                "solution_steps": [
                    "Equate a₁/a₂ = b₁/b₂: 2(a + b) = 3(a − b) -> a = 5b.",
                    "Substitute a = 5b into b₁/b₂ = c₁/c₂: 3/(6b) = 7/(16b − 2).",
                    "Solve 16b − 2 = 14b -> 2b = 2 -> b = 1, a = 5."
                ]
            },
            {
                "question": "For what value of k will 3x + y = 1 and (2k − 1)x + (k − 1)y = 2k + 1 have NO solution?",
                "options": [
                    "k = 2",
                    "k = −2",
                    "k = 1",
                    "k = 0"
                ],
                "answer": 0,
                "hint": "Equate 3/(2k−1) = 1/(k−1) first to solve k, then verify ≠ 1/(2k+1)!",
                "explanation": "3(k − 1) = 2k − 1 ⟹ 3k − 3 = 2k − 1 ⟹ k = 2; checking c ratio: 1/5 ≠ 3/3 = 1 -> strictly parallel!",
                "solution_steps": [
                    "Set parallel slopes: 3/(2k − 1) = 1/(k − 1).",
                    "Cross-multiply: 3k − 3 = 2k − 1 -> k = 2.",
                    "Confirm c₁/c₂ = 1/(2·2 + 1) = 1/5 ≠ 1 -> no solution."
                ]
            },
            {
                "question": "Solve swiftly using swapped-coefficient addition/subtraction: 37x + 43y = 123 and 43x + 37y = 117:",
                "options": [
                    "x = 1, y = 2",
                    "x = 2, y = 1",
                    "x = 3, y = 0",
                    "x = −1, y = 4"
                ],
                "answer": 0,
                "hint": "Add both equations (80x + 80y = 240 -> x + y = 3) and subtract (6x − 6y = −6 -> x − y = −1)!",
                "explanation": "x + y = 3 and x − y = −1 add to 2x = 2 ⟹ x = 1, y = 2.",
                "solution_steps": [
                    "Add both equations: 80(x + y) = 240 -> x + y = 3.",
                    "Subtract Eq 1 from Eq 2: 6(x − y) = −6 -> x − y = −1.",
                    "Solve cleanly: x = 1, y = 2."
                ]
            },
            {
                "question": "Find the unique intersection point of x = −3 and y = 5 on the Cartesian coordinate plane:",
                "options": [
                    "(−3, 5) — vertical line x = −3 meets horizontal line y = 5 perpendicularly",
                    "(5, −3)",
                    "Parallel lines (no intersection)",
                    "(0, 0)"
                ],
                "answer": 0,
                "hint": "Vertical line (constant x = −3) and horizontal line (constant y = 5) ALWAYS intersect orthogonally!",
                "explanation": "Every point on x = −3 has x-coord −3 and every point on y = 5 has y-coord 5, intersecting uniquely at (−3, 5).",
                "solution_steps": [
                    "Recognize x = −3 as vertical line parallel to y-axis.",
                    "Recognize y = 5 as horizontal line parallel to x-axis.",
                    "Read direct meeting coordinate (−3, 5)."
                ]
            },
            {
                "question": "What distance separates parallel horizontal lines y = −2 and y = 6?",
                "options": [
                    "8 units (parallel horizontal lines never intersect, so 0 solutions!)",
                    "4 units",
                    "12 units",
                    "They intersect at (0, 4)"
                ],
                "answer": 0,
                "hint": "Compute 6 − (−2) vertically along the y-axis!",
                "explanation": "y = 6 lies 6 units above the x-axis and y = −2 lies 2 units below, giving vertical separation 6 − (−2) = 8 units.",
                "solution_steps": [
                    "Note both lines are horizontal (slope 0).",
                    "Calculate signed vertical gap: 6 − (−2) = 8.",
                    "Confirm 0 intersections (inconsistent pair)."
                ]
            },
            {
                "question": "If x = a and y = b solves x − y = 2 and x + y = 4, find values of a and b:",
                "options": [
                    "a = 3, b = 1",
                    "a = 1, b = 3",
                    "a = 4, b = 2",
                    "a = 2, b = 0"
                ],
                "answer": 0,
                "hint": "Add (x − y = 2) and (x + y = 4) immediately!",
                "explanation": "2x = 6 ⟹ a = 3, and 3 + b = 4 ⟹ b = 1.",
                "solution_steps": [
                    "Add both equations: 2x = 6 -> x = a = 3.",
                    "Substitute a = 3 into 3 + y = 4 -> y = b = 1.",
                    "Verify 3 − 1 = 2."
                ]
            },
            {
                "question": "Solve for p so that the lines 4x + py + 8 = 0 and 2x + 2y + 2 = 0 have a UNIQUE solution:",
                "options": [
                    "All real values of p EXCEPT 4  (p ≠ 4)",
                    "Only p = 4",
                    "Only p = 2",
                    "No value of p works"
                ],
                "answer": 0,
                "hint": "Unique intersection requires a₁/a₂ ≠ b₁/b₂ -> 4/2 ≠ p/2!",
                "explanation": "4/2 = 2 ≠ p/2 requires p ≠ 4 (note p = 4 produces parallel lines since 4/2 = 4/2 = 2 ≠ 8/2 = 4).",
                "solution_steps": [
                    "Set unique intersection inequality: a₁/a₂ ≠ b₁/b₂.",
                    "Plug values: 4/2 ≠ p/2 -> 2 ≠ p/2.",
                    "Multiply by 2 -> p ≠ 4."
                ]
            },
            {
                "question": "Where does the straight line 3x + 4y = 12 cross the x-axis and y-axis respectively?",
                "options": [
                    "x-axis at (4, 0) and y-axis at (0, 3)",
                    "x-axis at (3, 0) and y-axis at (0, 4)",
                    "Both axes at (0, 0)",
                    "x-axis at (12, 0) and y-axis at (0, 12)"
                ],
                "answer": 0,
                "hint": "Plug y = 0 for x-intercept and x = 0 for y-intercept!",
                "explanation": "At y = 0, 3x = 12 -> (4, 0); at x = 0, 4y = 12 -> (0, 3).",
                "solution_steps": [
                    "Set y = 0 -> 3x = 12 -> x = 4 -> (4, 0).",
                    "Set x = 0 -> 4y = 12 -> y = 3 -> (0, 3).",
                    "Confirm intercepts (4, 0) and (0, 3)."
                ]
            },
            {
                "question": "If the lines given by 3x + 2ky = 2 and 2x + 5y + 1 = 0 are PARALLEL, find k:",
                "options": [
                    "k = 15 / 4",
                    "k = 4 / 15",
                    "k = −15 / 4",
                    "k = 3 / 5"
                ],
                "answer": 0,
                "hint": "Equate 3/2 = (2k)/5 cleanly (note constant ratio −2/1 ≠ 3/2 holds automatically)!",
                "explanation": "Parallel lines satisfy 3/2 = 2k/5 ⟹ 4k = 15 ⟹ k = 15/4 (and constant ratio −2/1 = −2 ≠ 3/2 confirms parallelism).",
                "solution_steps": [
                    "Write standard constants both on LHS: 3x + 2ky − 2 = 0 and 2x + 5y + 1 = 0.",
                    "Equate slope ratios: 3/2 = 2k/5 -> 4k = 15 -> k = 15/4.",
                    "Confirm constant ratio −2/1 ≠ 3/2 -> truly parallel."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Quiz 2",
        "subtitle": "Final Mastery: Digit Reversal, Age Shifts, Father-Child Ratios & Chapter 3 Synthesis",
        "questions": [
            {
                "question": "The sum of the digits of a two-digit number is 9; also, 9 times this number is TWICE the number obtained by reversing its digits (Ex 3.2 Q2 iii). Find the number:",
                "options": [
                    "18  (check: 1+8 = 9, and 9×18 = 162 = 2×81!)",
                    "81",
                    "27",
                    "45"
                ],
                "answer": 0,
                "hint": "Set x + y = 9 and 9(10x + y) = 2(10y + x) -> 88x − 11y = 0 -> y = 8x!",
                "explanation": "88x = 11y ⟹ y = 8x; alongside x + y = 9 gives 9x = 9 ⟹ x = 1, y = 8 -> number 18.",
                "solution_steps": [
                    "Write 9(10x + y) = 2(10y + x) -> 90x + 9y = 20y + 2x -> 88x = 11y -> y = 8x.",
                    "Substitute y = 8x into x + y = 9 -> 9x = 9 -> x = 1.",
                    "Read y = 8 -> number 10(1) + 8 = 18."
                ]
            },
            {
                "question": "A two-digit number is 4 more than 6 times the sum of its digits; if 18 is subtracted from the number, its digits reverse. Find the number:",
                "options": [
                    "64  (check: 6(6+4)+4 = 64, and 64 − 18 = 46!)",
                    "46",
                    "53",
                    "75"
                ],
                "answer": 0,
                "hint": "(10x+y) − 18 = (10y+x) gives x − y = 2, and 10x+y = 6(x+y) + 4 gives 4x − 5y = 4!",
                "explanation": "Substitute x = y + 2 into 4x − 5y = 4: 4(y + 2) − 5y = 4 ⟹ 8 − y = 4 ⟹ y = 4, x = 6 -> 64.",
                "solution_steps": [
                    "Simplify digit reversal: 9(x − y) = 18 -> x − y = 2 -> x = y + 2.",
                    "Translate second clue: 10x + y = 6x + 6y + 4 -> 4x − 5y = 4.",
                    "Substitute x = y + 2 -> 4y + 8 − 5y = 4 -> y = 4, x = 6 -> 64."
                ]
            },
            {
                "question": "A parent's present age is 3 times the sum of the ages of two children. After 5 years, parent's age will be twice the sum of the two children's ages. Find parent's age:",
                "options": [
                    "45 years  (and sum of children's present ages = 15 years)",
                    "40 years",
                    "36 years",
                    "50 years"
                ],
                "answer": 0,
                "hint": "Careful! Let y = SUM of TWO children's ages today! Five years later, BOTH children age +5, so their sum becomes y + 10!",
                "explanation": "x = 3y, and x + 5 = 2(y + 10) ⟹ 3y + 5 = 2y + 20 ⟹ y = 15, so parent age x = 3(15) = 45 years!",
                "solution_steps": [
                    "Let x = parent age, y = sum of TWO children's present ages -> x = 3y.",
                    "5 years later BOTH children age +5 each -> new sum = y + 10 -> x + 5 = 2(y + 10).",
                    "Substitute x = 3y -> 3y + 5 = 2y + 20 -> y = 15, x = 45 years."
                ]
            },
            {
                "question": "A coach buys 3 bats and 6 balls for ₹3,900, and later buys 1 bat and 3 more balls for ₹1,300 (Ex 3.1 style). What is the cost of 1 bat (x) and 1 ball (y)?",
                "options": [
                    "Bat = ₹1,300, Ball = ₹0  (or check: 3x+6y=3900 simplifies to x+2y=1300 alongside x+3y=1300!)",
                    "Bat = ₹1,000, Ball = ₹300",
                    "Bat = ₹900, Ball = ₹400",
                    "Inconsistent pair"
                ],
                "answer": 0,
                "hint": "Divide 3x + 6y = 3900 by 3 giving x + 2y = 1300, then subtract from x + 3y = 1300!",
                "explanation": "(x + 3y) − (x + 2y) = 1300 − 1300 gives y = 0 and x = 1300 algebraically (intersecting on x-axis at (1300, 0)).",
                "solution_steps": [
                    "Divide Eq 1 by 3 -> x + 2y = 1300.",
                    "Subtract from Eq 2 (x + 3y = 1300) -> y = 0.",
                    "Substitute y = 0 -> x = 1300 -> intersection (1300, 0)."
                ]
            },
            {
                "question": "Find values of x and y for a cyclic quadrilateral whose angles are A = 4y + 20, B = 3y − 5, C = −4x, D = −7x + 5:",
                "options": [
                    "x = −15, y = 25  (giving ∠A=120°, ∠B=70°, ∠C=60°, ∠D=110° summing 180° opposite!)",
                    "x = 15, y = 25",
                    "x = −20, y = 30",
                    "x = −10, y = 20"
                ],
                "answer": 0,
                "hint": "Opposite angles of a cyclic quadrilateral ALWAYS sum to 180°: ∠A + ∠C = 180° and ∠B + ∠D = 180°!",
                "explanation": "4y − 4x = 160 -> y − x = 40; 3y − 7x = 180. Substituting y = x + 40 into 3(x+40) − 7x = 180 gives −4x = 60 -> x = −15, y = 25.",
                "solution_steps": [
                    "Set ∠A + ∠C = 180 -> 4y + 20 − 4x = 180 -> y − x = 40.",
                    "Set ∠B + ∠D = 180 -> 3y − 5 − 7x + 5 = 180 -> 3y − 7x = 180.",
                    "Solve cleanly -> x = −15, y = 25."
                ]
            },
            {
                "question": "Two places A and B lie 100 km apart. One car starts from A and another from B at the SAME time. Traveling in the same direction they meet in 5 hours; traveling toward each other they meet in 1 hour. Find their speeds:",
                "options": [
                    "60 km/h and 40 km/h",
                    "70 km/h and 30 km/h",
                    "55 km/h and 45 km/h",
                    "80 km/h and 20 km/h"
                ],
                "answer": 0,
                "hint": "Relative speed same direction = x − y = 100/5 = 20; opposite direction = x + y = 100/1 = 100!",
                "explanation": "x − y = 20 and x + y = 100 add to 2x = 120 ⟹ x = 60 km/h and y = 40 km/h.",
                "solution_steps": [
                    "Same direction gap closure over 5 hrs: 5(x − y) = 100 -> x − y = 20.",
                    "Opposite direction closure over 1 hr: 1(x + y) = 100 -> x + y = 100.",
                    "Add equations -> 2x = 120 -> x = 60 km/h, y = 40 km/h."
                ]
            },
            {
                "question": "If the area of a rectangle shrinks by 9 sq units when length decreases by 5 and breadth increases by 3, AND increases by 67 sq units when length increases by 3 and breadth increases by 2, find length x and breadth y:",
                "options": [
                    "Length x = 17 units, Breadth y = 9 units",
                    "Length x = 19 units, Breadth y = 11 units",
                    "Length x = 15 units, Breadth y = 7 units",
                    "Length x = 12 units, Breadth y = 10 units"
                ],
                "answer": 0,
                "hint": "(x−5)(y+3) = xy − 9 gives 3x − 5y = 6; (x+3)(y+2) = xy + 67 gives 2x + 3y = 61!",
                "explanation": "Multiplying 3x − 5y = 6 by 3 and 2x + 3y = 61 by 5 gives 9x − 15y = 18 and 10x + 15y = 305 -> 19x = 323 -> x = 17, y = 9.",
                "solution_steps": [
                    "Expand Eq 1: xy + 3x − 5y − 15 = xy − 9 -> 3x − 5y = 6.",
                    "Expand Eq 2: xy + 2x + 3y + 6 = xy + 67 -> 2x + 3y = 61.",
                    "Eliminate y -> 19x = 323 -> x = 17, y = 9."
                ]
            },
            {
                "question": "Two lines a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 are graphed cleanly. Which statement is ALWAYS FALSE?",
                "options": [
                    "Two distinct non-parallel straight lines in a plane can intersect at 2 different points",
                    "If lines coincide, the pair is consistent and dependent with infinitely many solutions",
                    "If lines are parallel, a₁/a₂ = b₁/b₂ ≠ c₁/c₂ and the system is inconsistent",
                    "Every solution (x₀, y₀) corresponds to a point lying on BOTH lines"
                ],
                "answer": 0,
                "hint": "Two distinct Euclidean straight lines can share at most ONE single point (or overlap infinitely if identical)!",
                "explanation": "Two distinct straight lines in a plane either intersect at strictly ONE point or run parallel with 0 points—never 2 points.",
                "solution_steps": [
                    "Recall Euclidean geometry: two distinct lines meet at most once.",
                    "Verify the remaining three statements match Table 3.1 directly.",
                    "Identify 'intersect at 2 different points' as always false."
                ]
            },
            {
                "question": "For which linear pair does Elimination immediately eliminate y by ADDING the two equations directly without scaling?",
                "options": [
                    "5x + 3y = 19  and  2x − 3y = 2",
                    "5x + 3y = 19  and  2x + 3y = 10",
                    "3x + 2y = 8  and  2x − 4y = 1",
                    "x + y = 7  and  2x + y = 11"
                ],
                "answer": 0,
                "hint": "Direct addition cancels y when coefficients are ALREADY equal and opposite (+3y and −3y)!",
                "explanation": "Adding 5x + 3y = 19 and 2x − 3y = 2 cancels +3y and −3y immediately -> 7x = 21 -> x = 3, y = 4/3.",
                "solution_steps": [
                    "Inspect coefficients of y in each option.",
                    "Spot +3y and −3y (equal magnitude, opposite signs).",
                    "Adding yields 7x = 21 directly without multiplication."
                ]
            },
            {
                "question": "Which master takeaway unifies NCERT Class 10 Chapter 3: Pair of Linear Equations in Two Variables?",
                "options": [
                    "Linear pairs represent two lines (intersecting/parallel/coincident), diagnosed via Table 3.1 ratios and solved via Graph, Substitution, or Elimination",
                    "Only graphical plotting works for systems with fractional solutions",
                    "Every linear pair always has at least one unique solution",
                    "Elimination requires multiplying both equations by zero"
                ],
                "answer": 0,
                "hint": "Connect geometric interpretation, ratio classification, and exact algebraic methods!",
                "explanation": "Chapter 3 bridges geometry (3 line cases via Table 3.1) with exact algebraic solvers (Substitution & Elimination).",
                "solution_steps": [
                    "Eliminate false statements (graphs fail on fractions; parallels have 0 solutions; never multiply by 0).",
                    "Verify all 3 pillars: Table 3.1 ratios, graphical cases, Substitution/Elimination.",
                    "Select complete unifying statement."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch3 Class 10 Maths Part 3.")
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

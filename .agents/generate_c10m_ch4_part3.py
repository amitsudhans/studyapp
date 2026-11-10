#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 4: Quadratic Equations
Data Generator - Part 3 (Slides 17 to 20: Exercises 4.1, 4.2, 4.3 & Challenge)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Questions: Exactly 10 questions per slide (40 questions total)
- Zero spoken lecture on Exercise/Quiz slides ("except exercises")
- Zero fictional human character names (John, Jivanti, Rohan, Raghav, etc.), zero lecturer personas
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise 4.1 Quiz",
        "subtitle": "Exercise 4.1 Practice: Checking Standard Form Quadratics & Real-World Equation Modeling",
        "questions": [
            {
                "question": "Check whether (x + 1)² = 2(x − 3) is a quadratic equation (Exercise 4.1 Q1 i):",
                "options": [
                    "Yes—simplifies cleanly to x² + 7 = 0 (here a = 1 ≠ 0, b = 0, c = 7)",
                    "No—x² cancels out completely",
                    "Yes—simplifies to x² + 2x − 5 = 0",
                    "No—it has b = 0"
                ],
                "answer": 0,
                "hint": "Expand (x + 1)² = x² + 2x + 1 and 2(x − 3) = 2x − 6; notice +2x cancels while x² remains!",
                "explanation": "x² + 2x + 1 = 2x − 6 simplifies cleanly to x² + 7 = 0, which holds degree 2 (a = 1 ≠ 0).",
                "solution_steps": [
                    "Expand LHS: x² + 2x + 1; expand RHS: 2x − 6.",
                    "Subtract (2x − 6) from both sides: x² + 7 = 0.",
                    "Verify leading coefficient a = 1 ≠ 0 -> quadratic equation."
                ]
            },
            {
                "question": "Check whether x² − 2x = (−2)(3 − x) is a quadratic equation (Exercise 4.1 Q1 ii):",
                "options": [
                    "Yes—simplifies cleanly to x² − 4x + 6 = 0",
                    "No—simplifies to linear 4x − 6 = 0",
                    "Yes—simplifies to x² + 6 = 0",
                    "No—becomes cubic"
                ],
                "answer": 0,
                "hint": "Expand (−2)(3 − x) = −6 + 2x, then move all terms to LHS!",
                "explanation": "x² − 2x = −6 + 2x ⟹ x² − 4x + 6 = 0 (a = 1 ≠ 0, valid quadratic).",
                "solution_steps": [
                    "Distribute −2 carefully on RHS: −6 + 2x.",
                    "Move +2x and −6 across: x² − 2x − 2x + 6 = 0.",
                    "Combine terms cleanly: x² − 4x + 6 = 0 (quadratic)."
                ]
            },
            {
                "question": "(x + 2)³ = 2x(x² − 1) (Exercise 4.1 Q1 vii) looks cubic at first glance. What does its simplified form actually equal?",
                "options": [
                    "Cubic stays: x³ − 6x² − 14x − 8 = 0 (NOT quadratic, since x³ ≠ 2x³!)",
                    "Quadratic 6x² + 14x + 8 = 0",
                    "Linear 14x + 8 = 0",
                    "x² − 8 = 0"
                ],
                "answer": 0,
                "hint": "Compare LHS x³ against RHS 2x³—they do NOT cancel!",
                "explanation": "(x+2)³ = x³ + 6x² + 12x + 8, while RHS = 2x³ − 2x. Moving everything to RHS leaves x³ − 6x² − 14x − 8 = 0 (degree 3 cubic, NOT quadratic!).",
                "solution_steps": [
                    "Expand (x + 2)³ = x³ + 6x² + 12x + 8.",
                    "Expand 2x(x² − 1) = 2x³ − 2x.",
                    "Subtract LHS from RHS: x³ − 6x² − 14x − 8 = 0 (cubic degree 3, not quadratic)."
                ]
            },
            {
                "question": "Check whether (2x − 1)(x − 3) = (x + 5)(x − 1) is a quadratic equation (Exercise 4.1 Q1 v):",
                "options": [
                    "Yes—simplifies cleanly to x² − 11x + 8 = 0",
                    "No—x² terms cancel identically",
                    "Yes—simplifies to x² − 3x − 2 = 0",
                    "No—yields 3x² + 8 = 0"
                ],
                "answer": 0,
                "hint": "LHS has 2x² while RHS has 1x², so 2x² − x² leaves +x² intact!",
                "explanation": "LHS = 2x² − 7x + 3 and RHS = x² + 4x − 5; subtracting RHS gives x² − 11x + 8 = 0 (quadratic!).",
                "solution_steps": [
                    "Expand LHS: 2x² − 6x − x + 3 = 2x² − 7x + 3.",
                    "Expand RHS: x² + 4x − 5.",
                    "Subtract: x² − 11x + 8 = 0 (a = 1 ≠ 0 -> quadratic)."
                ]
            },
            {
                "question": "The area of a rectangular plot is 528 m²; its length is 1 m more than twice its breadth x (Exercise 4.1 Q2 i). Model cleanly:",
                "options": [
                    "2x² + x − 528 = 0",
                    "x² + 2x − 528 = 0",
                    "2x² − x − 528 = 0",
                    "4x² + 2x − 528 = 0"
                ],
                "answer": 0,
                "hint": "Breadth = x, length = 2x + 1, Area = x(2x + 1) = 528!",
                "explanation": "x(2x + 1) = 528 ⟹ 2x² + x − 528 = 0 (breadth 16 m, length 33 m).",
                "solution_steps": [
                    "Assign breadth = x m and length = (2x + 1) m.",
                    "Set Area = length × breadth = x(2x + 1) = 528.",
                    "Rewrite in standard form: 2x² + x − 528 = 0."
                ]
            },
            {
                "question": "An elder parent's age is 26 years more than the child's age x. Product of their ages 3 years from now will be 360 (Exercise 4.1 Q2 iii). Form the quadratic:",
                "options": [
                    "x² + 32x − 273 = 0  (child's present age = 7 yrs)",
                    "x² + 26x − 360 = 0",
                    "x² − 32x − 273 = 0",
                    "x² + 29x − 360 = 0"
                ],
                "answer": 0,
                "hint": "3 years from now, child = x + 3 and parent = (x + 26) + 3 = x + 29!",
                "explanation": "(x + 3)(x + 29) = 360 ⟹ x² + 32x + 87 = 360 ⟹ x² + 32x − 273 = 0 (factors (x + 39)(x − 7) = 0 -> x = 7).",
                "solution_steps": [
                    "Present ages: child = x, parent = x + 26.",
                    "3 years hence: (x + 3) and (x + 29).",
                    "Multiply (x + 3)(x + 29) = 360 -> x² + 32x − 273 = 0."
                ]
            },
            {
                "question": "A train travels 480 km at uniform speed x km/h. Had speed been 8 km/h less, the trip takes 3 hours more (Exercise 4.1 Q2 iv). Find the quadratic:",
                "options": [
                    "x² − 8x − 1280 = 0  (solving cleanly to speed x = 40 km/h)",
                    "x² + 8x − 1280 = 0",
                    "3x² − 8x − 480 = 0",
                    "x² − 8x + 1280 = 0"
                ],
                "answer": 0,
                "hint": "Set up time difference: 480/(x − 8) − 480/x = 3!",
                "explanation": "480[x − (x − 8)] / [x(x − 8)] = 3 ⟹ 480 × 8 = 3x(x − 8) ⟹ 1280 = x² − 8x ⟹ x² − 8x − 1280 = 0.",
                "solution_steps": [
                    "Express travel times: 480/(x − 8) − 480/x = 3.",
                    "Combine over common denominator: (480 × 8) = 3x(x − 8).",
                    "Divide by 3: x² − 8x = 1280 -> x² − 8x − 1280 = 0."
                ]
            },
            {
                "question": "A cottage workshop makes a certain number of toys x daily; cost of each toy is (55 − x) rupees, and total daily cost is ₹750. Which quadratic models x?",
                "options": [
                    "x² − 55x + 750 = 0  (roots: x = 25 or x = 30)",
                    "x² + 55x − 750 = 0",
                    "x² − 55x − 750 = 0",
                    "55x − x = 750"
                ],
                "answer": 0,
                "hint": "Total cost = quantity x × cost per toy (55 − x) = 750!",
                "explanation": "55x − x² = 750 ⟹ x² − 55x + 750 = 0, factoring cleanly into (x − 25)(x − 30) = 0.",
                "solution_steps": [
                    "Multiply units × unit price: x(55 − x) = 750.",
                    "Expand: 55x − x² = 750.",
                    "Move to positive x² side: x² − 55x + 750 = 0."
                ]
            },
            {
                "question": "Which equation below simplifies to a genuine quadratic equation?",
                "options": [
                    "x(2x + 3) = x² + 1  (simplifies cleanly to x² + 3x − 1 = 0)",
                    "(x − 1)(x + 2) = x² + 5",
                    "2x² + 3 = 2x² − x",
                    "x(x + 1) + 8 = (x + 2)(x − 2)"
                ],
                "answer": 0,
                "hint": "Always verify x² survives with nonzero coefficient after subtracting both sides!",
                "explanation": "x(2x + 3) = x² + 1 gives 2x² + 3x = x² + 1 ⟹ x² + 3x − 1 = 0 (degree 2), whereas x² cancels out completely in all other choices.",
                "solution_steps": [
                    "Expand x(2x + 3) = 2x² + 3x.",
                    "Subtract (x² + 1) cleanly -> x² + 3x − 1 = 0.",
                    "Verify a = 1 ≠ 0."
                ]
            },
            {
                "question": "Why is x² − 5√x + 6 = 0 NOT classified as a quadratic equation in variable x?",
                "options": [
                    "Because √x = x^(1/2) is not a whole-number exponent, so LHS is not a quadratic polynomial in x",
                    "Because 6 is an even integer",
                    "Because leading coefficient a = 1",
                    "Because −5 is negative"
                ],
                "answer": 0,
                "hint": "Quadratic equation requires LHS to be a quadratic polynomial of degree 2 with whole-number powers!",
                "explanation": "Standard form ax² + bx + c = 0 requires a polynomial in x; √x violates whole-number polynomial exponents.",
                "solution_steps": [
                    "Check exponents on variable x inside x² − 5√x + 6.",
                    "Spot fractional exponent x^(1/2).",
                    "Conclude not a polynomial equation in x."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise 4.2 Quiz",
        "subtitle": "Exercise 4.2 Practice: Solving via Factorisation, Number Puzzles & Right Triangles",
        "questions": [
            {
                "question": "Find the roots of x² − 3x − 10 = 0 by factorisation (Exercise 4.2 Q1 i):",
                "options": [
                    "5 and −2",
                    "−5 and 2",
                    "5 and 2",
                    "10 and −1"
                ],
                "answer": 0,
                "hint": "Split −3x into −5x + 2x giving (x − 5)(x + 2) = 0!",
                "explanation": "(x − 5)(x + 2) = 0 sets x = 5 or x = −2.",
                "solution_steps": [
                    "Product a·c = −10, sum b = −3 -> −5 and +2.",
                    "Factor: (x − 5)(x + 2) = 0.",
                    "Solve x = 5 and x = −2."
                ]
            },
            {
                "question": "Find the roots of 2x² + x − 6 = 0 by factorisation (Exercise 4.2 Q1 ii):",
                "options": [
                    "−2 and 3/2",
                    "2 and −3/2",
                    "−3 and 1",
                    "6 and −1/2"
                ],
                "answer": 0,
                "hint": "a·c = −12, sum +1 -> split +x = +4x − 3x!",
                "explanation": "2x² + 4x − 3x − 6 = 2x(x + 2) − 3(x + 2) = (2x − 3)(x + 2) = 0 ⟹ roots 3/2 and −2.",
                "solution_steps": [
                    "Split +x = 4x − 3x (since 4 × (−3) = −12).",
                    "Factor: (x + 2)(2x − 3) = 0.",
                    "Obtain roots −2 and 3/2."
                ]
            },
            {
                "question": "Solve 2x² − x + 1/8 = 0 cleanly via factorisation (Exercise 4.2 Q1 iv):",
                "options": [
                    "1/4 and 1/4  [clearing fractions by ×8 gives (4x − 1)² = 0]",
                    "1/2 and 1/4",
                    "−1/4 and −1/4",
                    "4 and 4"
                ],
                "answer": 0,
                "hint": "Multiply the entire equation by 8 first -> 16x² − 8x + 1 = 0!",
                "explanation": "16x² − 8x + 1 = (4x − 1)² = 0 gives equal roots 1/4 and 1/4.",
                "solution_steps": [
                    "Multiply every term by 8: 16x² − 8x + 1 = 0.",
                    "Factor perfect square: (4x − 1)(4x − 1) = 0.",
                    "Solve x = 1/4, 1/4."
                ]
            },
            {
                "question": "Find two numbers whose sum is 27 and product is 182 (Exercise 4.2 Q3):",
                "options": [
                    "13 and 14",
                    "12 and 15",
                    "11 and 16",
                    "9 and 18"
                ],
                "answer": 0,
                "hint": "Solve x(27 − x) = 182 ⟹ x² − 27x + 182 = 0!",
                "explanation": "182 = 13 × 14 and 13 + 14 = 27! Factoring (x − 13)(x − 14) = 0 yields 13 and 14.",
                "solution_steps": [
                    "Let numbers be x and 27 − x -> x(27 − x) = 182.",
                    "Form x² − 27x + 182 = 0.",
                    "Factor (x − 13)(x − 14) = 0 -> 13 and 14."
                ]
            },
            {
                "question": "Find two consecutive positive integers whose squares sum to 365 (Exercise 4.2 Q4):",
                "options": [
                    "13 and 14  (check: 13² + 14² = 169 + 196 = 365!)",
                    "12 and 13",
                    "14 and 15",
                    "11 and 12"
                ],
                "answer": 0,
                "hint": "Solve x² + (x + 1)² = 365 ⟹ 2x² + 2x − 364 = 0 ⟹ x² + x − 182 = 0!",
                "explanation": "x² + x − 182 = (x + 14)(x − 13) = 0 gives positive x = 13 and next integer 14.",
                "solution_steps": [
                    "Set up x² + (x + 1)² = 365 -> 2x² + 2x + 1 = 365.",
                    "Divide by 2 -> x² + x − 182 = 0.",
                    "Factor (x + 14)(x − 13) = 0 -> positive integers 13 and 14."
                ]
            },
            {
                "question": "If x = 3 is one root of quadratic equation kx² − 10x + 3 = 0, determine the value of k:",
                "options": [
                    "k = 3",
                    "k = 10/3",
                    "k = −3",
                    "k = 9"
                ],
                "answer": 0,
                "hint": "Substitute x = 3 directly into kx² − 10x + 3 = 0!",
                "explanation": "k(9) − 10(3) + 3 = 0 ⟹ 9k − 27 = 0 ⟹ k = 3 (check: 3x² − 10x + 3 = (3x − 1)(x − 3) = 0!).",
                "solution_steps": [
                    "Plug known root x = 3 into equation: 9k − 30 + 3 = 0.",
                    "Combine constants: 9k = 27.",
                    "Divide by 9 -> k = 3."
                ]
            },
            {
                "question": "If one root of x² − 5x + 6 = 0 is 2, find its other root cleanly:",
                "options": [
                    "3",
                    "−3",
                    "6",
                    "1"
                ],
                "answer": 0,
                "hint": "Factor (x − 2)(x − 3) = 0 or recall sum of roots = −b/a = 5!",
                "explanation": "(x − 2)(x − 3) = 0 gives roots 2 and 3.",
                "solution_steps": [
                    "Factor middle term: x² − 2x − 3x + 6 = 0.",
                    "(x − 2)(x − 3) = 0.",
                    "Other root is 3."
                ]
            },
            {
                "question": "Find the roots of x − 1/x = 3 (where x ≠ 0):",
                "options": [
                    "(3 + √13)/2  and  (3 − √13)/2",
                    "3 and −1",
                    "(3 + √5)/2  and  (3 − √5)/2",
                    "1 and −1"
                ],
                "answer": 0,
                "hint": "Multiply through by x giving x² − 3x − 1 = 0, then apply Quadratic Formula!",
                "explanation": "x² − 1 = 3x ⟹ x² − 3x − 1 = 0; D = 9 − 4(1)(−1) = 13 ⟹ x = (3 ± √13)/2.",
                "solution_steps": [
                    "Multiply by x ≠ 0: x² − 1 = 3x -> x² − 3x − 1 = 0.",
                    "Compute D = (−3)² − 4(1)(−1) = 13.",
                    "Apply formula: x = (3 ± √13)/2."
                ]
            },
            {
                "question": "Notice carefully! For quadratic equation 4x² + 4√3x + 3 = 0, what are its roots by factorisation?",
                "options": [
                    "−√3/2  and  −√3/2  [recognizing (2x + √3)² = 0]",
                    "+√3/2  and  +√3/2",
                    "−√3  and  +√3",
                    "No real roots"
                ],
                "answer": 0,
                "hint": "Spot perfect square (2x)² + 2(2x)(√3) + (√3)² = 0!",
                "explanation": "(2x + √3)² = 0 yields two equal roots x = −√3/2, −√3/2.",
                "solution_steps": [
                    "Notice a = 4 = 2², c = 3 = (√3)², middle = 2(2x)(√3).",
                    "Factor directly: (2x + √3)² = 0.",
                    "Solve 2x + √3 = 0 -> x = −√3/2."
                ]
            },
            {
                "question": "What happens if someone solves x² = 5x mistakenly by dividing both sides by x, writing x = 5?",
                "options": [
                    "They accidentally LOSE the valid root x = 0; proper factoring x(x − 5) = 0 finds BOTH x = 0 and x = 5!",
                    "Dividing by x gives the complete answer x = 5",
                    "x = 0 is never a valid solution of x² = 5x",
                    "Only negative −5 is lost"
                ],
                "answer": 0,
                "hint": "Never divide any algebraic equation by a variable that could equal zero!",
                "explanation": "Dividing by x assumes x ≠ 0 and silently erases root x = 0. Rearranging to x² − 5x = x(x − 5) = 0 preserves both 0 and 5.",
                "solution_steps": [
                    "Move 5x to LHS: x² − 5x = 0.",
                    "Factor common x: x(x − 5) = 0.",
                    "Recover BOTH roots: x = 0 and x = 5."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Exercise 4.3 Quiz",
        "subtitle": "Exercise 4.3 Practice: Discriminant D, Root Nature, Finding k & Real-World Design Feasibility",
        "questions": [
            {
                "question": "Find the nature of roots of 2x² − 6x + 3 = 0 (Exercise 4.3 Q1 iii), and find them if real:",
                "options": [
                    "D = 12 > 0 -> two distinct real roots: (3 + √3)/2 and (3 − √3)/2",
                    "D = 0 -> equal roots 3/2 and 3/2",
                    "D = −12 < 0 -> no real roots",
                    "D = 60 > 0 -> roots 3 ± √15"
                ],
                "answer": 0,
                "hint": "D = (−6)² − 4(2)(3) = 36 − 24 = 12, √12 = 2√3!",
                "explanation": "x = (6 ± 2√3)/4 = (3 ± √3)/2 (D = 12 > 0 gives two distinct real roots).",
                "solution_steps": [
                    "Compute D = 36 − 24 = 12 > 0 (two distinct real roots).",
                    "Apply formula: x = (6 ± √12) / 4 = (6 ± 2√3) / 4.",
                    "Divide top and bottom by 2 -> (3 ± √3)/2."
                ]
            },
            {
                "question": "For what value(s) of k does x² + k(2x + k − 1) + 2 = 0 have real and equal roots?",
                "options": [
                    "k = 2",
                    "k = −2",
                    "k = 4",
                    "k = ±2"
                ],
                "answer": 0,
                "hint": "Expand into x² + 2kx + (k² − k + 2) = 0, then compute D = (2k)² − 4(1)(k² − k + 2) = 0!",
                "explanation": "4k² − 4k² + 4k − 8 = 0 simplifies cleanly to 4k = 8 ⟹ k = 2.",
                "solution_steps": [
                    "Write standard form: x² + (2k)x + (k² − k + 2) = 0.",
                    "Set D = 4k² − 4(k² − k + 2) = 0.",
                    "Cancel 4k² -> 4k − 8 = 0 -> k = 2."
                ]
            },
            {
                "question": "Is it possible to design a rectangular mango grove whose length is twice its breadth and area is 800 m² (Ex 4.3 Q3)?",
                "options": [
                    "Yes! 2x² = 800 ⟹ x = 20 m breadth and length = 40 m (D > 0)",
                    "No—D < 0 makes it impossible",
                    "Yes! Breadth = 40 m, length = 20 m",
                    "Only possible as a circle"
                ],
                "answer": 0,
                "hint": "Let breadth = x, length = 2x, so Area = 2x² = 800 -> x² = 400!",
                "explanation": "x² = 400 gives positive breadth x = 20 m and length 2(20) = 40 m (area 20 × 40 = 800 m²).",
                "solution_steps": [
                    "Set breadth = x, length = 2x -> 2x² = 800.",
                    "Solve x² = 400 -> positive x = 20 m.",
                    "Find length = 40 m (design feasible!)."
                ]
            },
            {
                "question": "For what condition on p, q, r does quadratic equation px² + qx + r = 0 (p ≠ 0) have TWO EQUAL real roots?",
                "options": [
                    "q² = 4pr  (since discriminant q² − 4pr = 0)",
                    "p² = 4qr",
                    "q² < 4pr",
                    "q = 0 always"
                ],
                "answer": 0,
                "hint": "Rename coefficients a → p, b → q, c → r carefully inside b² − 4ac = 0!",
                "explanation": "Setting discriminant D = (coeff of x)² − 4(coeff of x²)(const) = q² − 4pr = 0 gives q² = 4pr.",
                "solution_steps": [
                    "Map standard coefficients carefully: a = p, b = q, c = r.",
                    "Equal roots condition D = 0 -> q² − 4pr = 0.",
                    "Rearrange cleanly -> q² = 4pr."
                ]
            },
            {
                "question": "Which quadratic equation below has NO real roots (D < 0)?",
                "options": [
                    "x² + 4x + 5 = 0  (D = 16 − 20 = −4 < 0)",
                    "x² − 4x + 4 = 0  (D = 0)",
                    "x² − 5x + 4 = 0  (D = 9 > 0)",
                    "3x² − 2x − 1 = 0  (D = 16 > 0)"
                ],
                "answer": 0,
                "hint": "Compute b² − 4ac for each equation!",
                "explanation": "For x² + 4x + 5 = 0, D = 4² − 4(1)(5) = 16 − 20 = −4 < 0, confirming zero real roots.",
                "solution_steps": [
                    "Compute D for Option 1: 4² − 4(1)(5) = −4.",
                    "Verify −4 < 0 implies square root of negative number (non-real).",
                    "Confirm Options 2, 3, 4 all have D ≥ 0."
                ]
            },
            {
                "question": "If ax² + bx + c = 0 (a ≠ 0) has a > 0 and c < 0 (opposite signs on a and c!), what MUST be true about its roots?",
                "options": [
                    "Discriminant D = b² − 4ac is STRICTLY POSITIVE (> 0), guaranteeing two distinct real roots!",
                    "It has no real roots",
                    "Its roots are strictly equal",
                    "Both roots must equal zero"
                ],
                "answer": 0,
                "hint": "Check the sign of −4ac when a > 0 and c < 0!",
                "explanation": "Since a·c < 0, −4ac is strictly POSITIVE (> 0); adding b² ≥ 0 ensures D = b² − 4ac > 0 ALWAYS!",
                "solution_steps": [
                    "Analyze sign: a > 0 and c < 0 ⟹ ac < 0 ⟹ −4ac > 0.",
                    "Since b² ≥ 0 for every real b, D = b² + |4ac| > 0 strictly.",
                    "Conclude two distinct real roots always exist."
                ]
            },
            {
                "question": "Find positive k for which x² + 4x + k = 0 has real roots (distinct OR equal):",
                "options": [
                    "k ≤ 4  (since real roots require D = 16 − 4k ≥ 0)",
                    "k > 4",
                    "k ≥ 16",
                    "k = 8"
                ],
                "answer": 0,
                "hint": "Real roots exist whenever D ≥ 0 (both D > 0 and D = 0)!",
                "explanation": "D = 16 − 4k ≥ 0 ⟹ 4k ≤ 16 ⟹ k ≤ 4.",
                "solution_steps": [
                    "Recall 'real roots' covers D > 0 and D = 0 -> D ≥ 0.",
                    "Set up 4² − 4(1)(k) ≥ 0 -> 16 − 4k ≥ 0.",
                    "Solve cleanly -> k ≤ 4."
                ]
            },
            {
                "question": "Why does x² − 6x + 10 = 0 yield no real roots geometrically as well as algebraically?",
                "options": [
                    "Algebraically D = 36 − 40 = −4 < 0; geometrically y = (x − 3)² + 1 ≥ 1 floats strictly above the x-axis!",
                    "Because its vertex sits on (3, 0)",
                    "Because leading coefficient is 1",
                    "Because it crosses the x-axis 3 times"
                ],
                "answer": 0,
                "hint": "Complete the square: x² − 6x + 10 = (x − 3)² + 1!",
                "explanation": "D = −4 < 0 matches upward parabola (x − 3)² + 1 having minimum vertex y = +1 > 0, never intersecting the x-axis.",
                "solution_steps": [
                    "Compute D = 36 − 40 = −4 < 0.",
                    "Complete square: (x − 3)² + 1 ≥ 1 > 0.",
                    "Observe zero x-intercepts match D < 0."
                ]
            },
            {
                "question": "Can two real numbers have sum 10 and product 30? Test using a quadratic model and Discriminant D:",
                "options": [
                    "No! Model x² − 10x + 30 = 0 gives D = 100 − 120 = −20 < 0 (impossible)",
                    "Yes, 6 and 5",
                    "Yes, D = 20 > 0",
                    "Yes, 5 and 5"
                ],
                "answer": 0,
                "hint": "Form x(10 − x) = 30 -> x² − 10x + 30 = 0 and check D!",
                "explanation": "D = (−10)² − 4(1)(30) = 100 − 120 = −20 < 0 proves maximum product for sum 10 is 5 × 5 = 25 < 30!",
                "solution_steps": [
                    "Model numbers x and 10 − x: x(10 − x) = 30 -> x² − 10x + 30 = 0.",
                    "Compute D = 100 − 120 = −20 < 0.",
                    "Conclude impossible in real numbers."
                ]
            },
            {
                "question": "If D = 0 for a quadratic equation ax² + bx + c = 0, what MUST be true about its two roots α and β?",
                "options": [
                    "α = β = −b / (2a)",
                    "α + β = 0 always",
                    "α and β are irrational conjugates",
                    "α × β = 0 always"
                ],
                "answer": 0,
                "hint": "Plug D = 0 into Sridharacharya's formula!",
                "explanation": "D = 0 gives (−b ± 0)/(2a), locking both roots equal at −b/(2a).",
                "solution_steps": [
                    "Substitute D = 0 into x = (−b ± √D)/(2a).",
                    "Simplify −b/(2a) for both + and − branches.",
                    "Verify two equal real roots α = β = −b/(2a)."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Mastery Quiz",
        "subtitle": "Final Mastery: Circular Pole, Boats & Streams, Water Taps & Complete Chapter 4 Synthesis",
        "questions": [
            {
                "question": "A motorboat whose speed in still water is 18 km/h takes 1 hour MORE to go 24 km upstream than to return downstream to the same spot. Find the stream's speed x km/h:",
                "options": [
                    "x = 6 km/h  (note check: 24/12 − 24/24 = 2 − 1 = 1 hour!)",
                    "x = 4 km/h",
                    "x = 8 km/h",
                    "x = 3 km/h"
                ],
                "answer": 0,
                "hint": "Upstream speed = (18 − x), downstream speed = (18 + x); solve 24/(18−x) − 24/(18+x) = 1!",
                "explanation": "24(2x) = (18² − x²) ⟹ x² + 48x − 324 = 0 ⟹ (x + 54)(x − 6) = 0 ⟹ x = 6 km/h.",
                "solution_steps": [
                    "Model upstream vs downstream time: 24/(18 − x) − 24/(18 + x) = 1.",
                    "Simplify: 48x = 324 − x² -> x² + 48x − 324 = 0.",
                    "Factor (x + 54)(x − 6) = 0 -> positive stream speed 6 km/h."
                ]
            },
            {
                "question": "Two water taps together fill a tank in 9⅜ hours (= 75/8 hrs). The larger tap takes 10 hours LESS than the smaller tap (x hrs) to fill it alone. Find individual fill times:",
                "options": [
                    "Larger tap = 15 hours, Smaller tap = 25 hours  [since 1/15 + 1/25 = 8/75!]",
                    "Larger tap = 10 hours, Smaller tap = 20 hours",
                    "Larger tap = 20 hours, Smaller tap = 30 hours",
                    "Larger tap = 5 hours, Smaller tap = 15 hours"
                ],
                "answer": 0,
                "hint": "Combine 1-hour fill rates: 1/x + 1/(x − 10) = 8/75!",
                "explanation": "Solving 4x² − 115x + 375 = 0 gives x = 25 hrs (rejecting 15/4 since x − 10 would be negative!); larger tap = 15 hrs.",
                "solution_steps": [
                    "Set combined hourly rate: 1/x + 1/(x − 10) = 8/75.",
                    "Cross-multiply & divide by 2: 4x² − 115x + 375 = 0.",
                    "Solve (x − 25)(4x − 15) = 0 -> smaller x = 25 hrs, larger = 15 hrs."
                ]
            },
            {
                "question": "An express train takes 1 hour less than a passenger train to travel 132 km (average speed of express is 11 km/h more than passenger speed x). Find both speeds:",
                "options": [
                    "Passenger = 33 km/h, Express = 44 km/h",
                    "Passenger = 44 km/h, Express = 55 km/h",
                    "Passenger = 22 km/h, Express = 33 km/h",
                    "Passenger = 30 km/h, Express = 41 km/h"
                ],
                "answer": 0,
                "hint": "Solve 132/x − 132/(x + 11) = 1 ⟹ x² + 11x − 1452 = 0!",
                "explanation": "Factoring (x + 44)(x − 33) = 0 gives positive passenger speed 33 km/h and express speed 44 km/h.",
                "solution_steps": [
                    "Set time difference: 132/x − 132/(x + 11) = 1.",
                    "Simplify: x² + 11x − 1452 = 0.",
                    "Factor (x + 44)(x − 33) = 0 -> 33 km/h and 44 km/h."
                ]
            },
            {
                "question": "Sum of the areas of two squares is 468 m². If the difference of their perimeters is 24 m, find the sides of the two squares:",
                "options": [
                    "18 m and 12 m  (check: 18² + 12² = 324 + 144 = 468!)",
                    "16 m and 10 m",
                    "20 m and 14 m",
                    "15 m and 9 m"
                ],
                "answer": 0,
                "hint": "Perimeter difference 4x − 4y = 24 simplifies immediately to x − y = 6 ⟹ x = y + 6!",
                "explanation": "y² + (y + 6)² = 468 ⟹ y² + 6y − 216 = 0 ⟹ (y + 18)(y − 12) = 0 ⟹ sides 12 m and 18 m.",
                "solution_steps": [
                    "Express sides x and y with 4x − 4y = 24 -> x = y + 6.",
                    "Substitute into areas sum: (y + 6)² + y² = 468 -> y² + 6y − 216 = 0.",
                    "Solve positive root y = 12 m, x = 18 m."
                ]
            },
            {
                "question": "Solve for x cleanly: (1 / (x + 4)) − (1 / (x − 7)) = 11 / 30  (where x ≠ −4, 7):",
                "options": [
                    "x = 1  and  x = 2",
                    "x = −1  and  x = −2",
                    "x = 4  and  x = −7",
                    "x = 3  and  x = 5"
                ],
                "answer": 0,
                "hint": "Numerator simplifies cleanly to (x − 7) − (x + 4) = −11, canceling the 11 on RHS immediately!",
                "explanation": "−11 / [(x+4)(x−7)] = 11 / 30 ⟹ (x+4)(x−7) = −30 ⟹ x² − 3x − 28 = −30 ⟹ x² − 3x + 2 = (x−1)(x−2) = 0!",
                "solution_steps": [
                    "Combine fractions: −11 / [(x + 4)(x − 7)] = 11 / 30.",
                    "Cancel 11 -> x² − 3x − 28 = −30 -> x² − 3x + 2 = 0.",
                    "Factor (x − 1)(x − 2) = 0 -> x = 1, 2."
                ]
            },
            {
                "question": "Notice carefully! Solve 4x² − 4a²x + (a⁴ − b⁴) = 0 cleanly via factorisation:",
                "options": [
                    "(a² + b²)/2  and  (a² − b²)/2",
                    "a² + b²  and  a² − b²",
                    "(a + b)/2  and  (a − b)/2",
                    "±(a² − b²)"
                ],
                "answer": 0,
                "hint": "Write a⁴ − b⁴ = (a² + b²)(a² − b²) and notice 2(a²+b²) + 2(a²−b²) = 4a²!",
                "explanation": "Splitting −4a²x = −2(a² + b²)x − 2(a² − b²)x factors cleanly into [2x − (a² + b²)][2x − (a² − b²)] = 0.",
                "solution_steps": [
                    "Factor constant: a⁴ − b⁴ = (a² + b²)(a² − b²).",
                    "Split middle term: −4a²x = −2(a² + b²)x − 2(a² − b²)x.",
                    "Obtain roots (a² + b²)/2 and (a² − b²)/2."
                ]
            },
            {
                "question": "If −5 is a root of 2x² + px − 15 = 0 AND p(x² + x) + k = 0 has equal roots, find p and k:",
                "options": [
                    "p = 7  and  k = 7 / 4",
                    "p = −7  and  k = −7 / 4",
                    "p = 7  and  k = 7",
                    "p = 5  and  k = 5 / 4"
                ],
                "answer": 0,
                "hint": "Plug x = −5 into first equation to find p = 7, then compute D = 0 on 7x² + 7x + k = 0!",
                "explanation": "2(25) − 5p − 15 = 0 ⟹ 35 = 5p ⟹ p = 7. Next 7x² + 7x + k = 0 with D = 49 − 28k = 0 gives k = 49/28 = 7/4.",
                "solution_steps": [
                    "Substitute x = −5 into 2x² + px − 15 = 0 -> 50 − 5p − 15 = 0 -> p = 7.",
                    "Rewrite second quadratic: 7x² + 7x + k = 0.",
                    "Set D = 7² − 4(7)(k) = 0 -> 28k = 49 -> k = 7/4."
                ]
            },
            {
                "question": "The sum of a positive number x and its reciprocal 1/x equals 10/3. Find the number:",
                "options": [
                    "3  or  1/3",
                    "5  or  1/5",
                    "2  or  1/2",
                    "4  or  1/4"
                ],
                "answer": 0,
                "hint": "Set x + 1/x = 10/3 ⟹ 3x² − 10x + 3 = 0!",
                "explanation": "3x² − 10x + 3 = (3x − 1)(x − 3) = 0 gives 3 and 1/3 (check: 3 + 1/3 = 10/3!).",
                "solution_steps": [
                    "Model sum with reciprocal: x + 1/x = 10/3.",
                    "Clear denominators by ×3x: 3x² − 10x + 3 = 0.",
                    "Factor (3x − 1)(x − 3) = 0 -> 3 or 1/3."
                ]
            },
            {
                "question": "Which historical mathematician's work in Section 4.1 introduced completing the square explicitly into the Quadratic Formula used worldwide today?",
                "options": [
                    "Indian mathematician Sridharacharya (building upon Brahmagupta's work)",
                    "Euclidean circles exclusively",
                    "Isaac Newton",
                    "Carl Gauss alone"
                ],
                "answer": 0,
                "hint": "Recall the Indian scholar mentioned right beside Brahmagupta in Section 4.1!",
                "explanation": "Sridharacharya gave the celebrated Quadratic Formula obtained by completing the square on ax² + bx + c = 0.",
                "solution_steps": [
                    "Recall Section 4.1 historical timeline.",
                    "Match geometric methods (Euclid), Arabic classification (Al-Khwarizmi), Indian explicit rule (Brahmagupta), and formula (Sridharacharya).",
                    "Select Sridharacharya."
                ]
            },
            {
                "question": "Which comprehensive takeaway best summarizes NCERT Class 10 Chapter 4: Quadratic Equations?",
                "options": [
                    "Standard form ax²+bx+c=0 (a≠0) equates polynomial zeroes with equation roots, solved via factoring or Sridharacharya's Formula governed by D = b²−4ac",
                    "A quadratic equation always has 2 distinct positive integer roots",
                    "When D < 0, roots are equal to −b/(2a)",
                    "Standard form allows a = 0 whenever b ≠ 0"
                ],
                "answer": 0,
                "hint": "Verify standard condition a ≠ 0, root-zero tie, solving methods, and discriminant roles!",
                "explanation": "Chapter 4 establishes degree-2 modeling, root-zero equivalence, middle-term splitting, Sridharacharya's formula, and discriminant D criteria.",
                "solution_steps": [
                    "Rule out false statements (D < 0 means no real roots; a = 0 turns linear; roots can be equal/non-real/irrational).",
                    "Confirm all core pillars: standard form, factoring, Quadratic Formula, and D = b² − 4ac.",
                    "Select complete summary statement."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch4 Class 10 Maths Part 3.")
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

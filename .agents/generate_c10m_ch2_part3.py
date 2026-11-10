#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 2: Polynomials
Data Generator - Part 3 (Slides 17 to 20: Exercises 2.1, 2.2 & Challenges)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Questions: Exactly 10 questions per slide (40 questions total)
- Zero spoken lecture on Exercise/Quiz slides ("except exercises")
- Zero fictional human character names, zero lecturer personas
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Exercise 2.1 Quiz",
        "subtitle": "Exercise 2.1 & Section 2.2 Drills: Counting Graphical Zeroes, Parabolas & Degree Bounds",
        "questions": [
            {
                "question": "If the graph of y = p(x) is a straight line completely parallel to and 3 units above the x-axis, how many zeroes does p(x) have (Exercise 2.1)?",
                "options": [
                    "0 zeroes (never intersects the x-axis)",
                    "1 zero (at y = 3)",
                    "3 zeroes",
                    "Infinitely many zeroes"
                ],
                "answer": 0,
                "hint": "Does a horizontal line at y = 3 ever cross y = 0 (the x-axis)?",
                "explanation": "A constant polynomial y = 3 never intersects the horizontal x-axis, so it has 0 zeroes.",
                "solution_steps": [
                    "Recall zeroes equal x-coordinates where y = p(x) intersects the x-axis.",
                    "Visualize horizontal line y = 3 floating 3 units above the x-axis.",
                    "Count 0 intersections -> 0 zeroes."
                ]
            },
            {
                "question": "If graph y = p(x) crosses the x-axis once at (−2, 0) and crosses the y-axis once at (0, 4), how many zeroes does p(x) have?",
                "options": [
                    "1 zero (at x = −2)",
                    "2 zeroes",
                    "0 zeroes",
                    "4 zeroes"
                ],
                "answer": 0,
                "hint": "Only intersections on the x-axis represent zeroes of p(x)!",
                "explanation": "Crossing the y-axis at (0, 4) simply means p(0) = 4; only the single x-axis crossing at (−2, 0) gives 1 zero.",
                "solution_steps": [
                    "Separate x-axis intercepts from y-axis intercepts.",
                    "Ignore (0, 4) since y = 4 ≠ 0.",
                    "Count only (−2, 0) -> 1 zero."
                ]
            },
            {
                "question": "A smooth curve y = p(x) weaves up and down, slicing across the x-axis at x = −3, x = −1, and x = 2.5. How many zeroes does it have?",
                "options": [
                    "3 zeroes",
                    "1 zero",
                    "2 zeroes",
                    "4 zeroes"
                ],
                "answer": 0,
                "hint": "Count the distinct x-intercepts along the horizontal axis!",
                "explanation": "Cutting the x-axis at 3 distinct points yields 3 real zeroes (−3, −1, and 2.5).",
                "solution_steps": [
                    "List x-axis crossings: x = −3, −1, and 2.5.",
                    "Count distinct intersections along y = 0.",
                    "Confirm 3 real zeroes."
                ]
            },
            {
                "question": "An upward-opening parabola touches the x-axis gently at x = 2 without dipping below it. How many zeroes does it have?",
                "options": [
                    "1 zero (two coincident roots equal to 2)",
                    "0 zeroes",
                    "2 distinct zeroes",
                    "3 zeroes"
                ],
                "answer": 0,
                "hint": "Case 2 tangent touch counts as 1 distinct x-intercept!",
                "explanation": "Because the parabola grazes the x-axis at a single point (2, 0), there is 1 real zero (x = 2 repeated).",
                "solution_steps": [
                    "Identify Case 2 quadratic touching behavior.",
                    "Count unique points shared with x-axis: only (2, 0).",
                    "Conclude 1 zero."
                ]
            },
            {
                "question": "If the curve y = p(x) intersects the x-axis at 4 distinct points, what is the MINIMUM possible degree of polynomial p(x)?",
                "options": [
                    "Degree 4 (since degree n allows at most n zeroes)",
                    "Degree 2",
                    "Degree 3",
                    "Degree 1"
                ],
                "answer": 0,
                "hint": "Apply the bound 'degree n has at most n zeroes' in reverse!",
                "explanation": "A polynomial with 4 distinct zeroes cannot have degree 1, 2, or 3, so its degree must be at least 4.",
                "solution_steps": [
                    "Recall Theorem: degree n polynomial has at most n zeroes.",
                    "Given 4 distinct zeroes -> n ≥ 4.",
                    "Identify minimum degree as 4."
                ]
            },
            {
                "question": "Which quadratic polynomial opens DOWNWARDS and passes strictly BELOW the x-axis everywhere (Case 3, zero real zeroes)?",
                "options": [
                    "y = −x² − 5",
                    "y = −x² + 5",
                    "y = x² + 5",
                    "y = x² − 5"
                ],
                "answer": 0,
                "hint": "Need a < 0 (downward) AND maximum vertex y < 0!",
                "explanation": "Since a = −1 < 0 and −x² ≤ 0, y = −x² − 5 ≤ −5 < 0 everywhere, never reaching y = 0.",
                "solution_steps": [
                    "Check downward condition: a < 0 rules out x² + 5 and x² − 5.",
                    "Check y = −x² − 5: since −x² ≤ 0, max y = −5 < 0.",
                    "Confirm 0 x-axis intersections."
                ]
            },
            {
                "question": "What are the x-axis intersection point(s) of the linear polynomial y = 4x + 12?",
                "options": [
                    "(−3, 0)",
                    "(0, 12)",
                    "(3, 0)",
                    "(−12, 0)"
                ],
                "answer": 0,
                "hint": "Plug y = 0 and solve 4x + 12 = 0!",
                "explanation": "4x + 12 = 0 ⟹ x = −12/4 = −3, intersecting the x-axis at (−3, 0).",
                "solution_steps": [
                    "Set y = 0 for x-intercept: 4x + 12 = 0.",
                    "Solve x = −b/a = −12/4 = −3.",
                    "Write ordered pair (−3, 0)."
                ]
            },
            {
                "question": "For polynomial p(x) = x² − 16, identify its opening direction and x-axis crossings:",
                "options": [
                    "Opens upwards (a = 1 > 0), crossing x-axis twice at (−4, 0) and (4, 0)",
                    "Opens downwards, touching x-axis once at (4, 0)",
                    "Opens upwards, never crossing x-axis",
                    "Straight line through (−16, 0)"
                ],
                "answer": 0,
                "hint": "Check sign of x² coefficient (+1) and factor x² − 16 = (x−4)(x+4)!",
                "explanation": "a = +1 > 0 opens upwards; solving (x−4)(x+4) = 0 yields x = 4 and x = −4.",
                "solution_steps": [
                    "Inspect leading coefficient a = +1 > 0 -> opens upwards.",
                    "Factor p(x) = (x − 4)(x + 4) = 0.",
                    "Read two x-intercepts: (−4, 0) and (4, 0)."
                ]
            },
            {
                "question": "If the graph of quadratic ax² + bx + c touches the x-axis at (5, 0) and opens downwards, which statement holds?",
                "options": [
                    "a < 0 and discriminant b² − 4ac = 0 (equation a(x − 5)²)",
                    "a > 0 and two distinct roots",
                    "c = 0 always",
                    "a = 0 and b = 5"
                ],
                "answer": 0,
                "hint": "Downward means a < 0; grazing at a single point means coincident roots!",
                "explanation": "Opening downwards requires a < 0, and touching once at x = 5 means both roots equal 5.",
                "solution_steps": [
                    "Downward parabola implies leading coefficient a < 0.",
                    "Single tangent point at (5, 0) implies repeated zero x = 5.",
                    "Form p(x) = a(x − 5)² with a < 0."
                ]
            },
            {
                "question": "Notice carefully: why is y = 0x² + 3x − 6 NOT a quadratic parabola?",
                "options": [
                    "Because a = 0 eliminates x², leaving linear polynomial 3x − 6 (straight line intersecting once at (2, 0))",
                    "Because constant −6 is negative",
                    "Because 3 is prime",
                    "Because zero cannot be a coefficient anywhere"
                ],
                "answer": 0,
                "hint": "Recall the strict condition a ≠ 0 inside ax² + bx + c!",
                "explanation": "When a = 0, ax² vanishes and the expression collapses to degree 1 (linear), drawing a straight line instead of a parabola.",
                "solution_steps": [
                    "Evaluate 0·x² + 3x − 6 = 3x − 6.",
                    "Check degree = 1 (linear, not quadratic).",
                    "Conclude straight line intersecting x-axis once at (2, 0)."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Exercise 2.2 Quiz",
        "subtitle": "Exercise 2.2 Practice: Factoring Quadratics, Verifying Coefficients & Constructing From Sum/Product",
        "questions": [
            {
                "question": "Find the zeroes of quadratic polynomial 4s² − 4s + 1 and verify their sum and product (Exercise 2.2 Q1 ii):",
                "options": [
                    "Zeroes 1/2, 1/2; Sum = 1 (= −(−4)/4) and Product = 1/4 (= 1/4)",
                    "Zeroes 1, 1/4; Sum = 5/4",
                    "Zeroes −1/2, −1/2; Sum = −1",
                    "Zeroes 2, 1/2; Sum = 5/2"
                ],
                "answer": 0,
                "hint": "Notice 4s² − 4s + 1 = (2s − 1)²!",
                "explanation": "(2s − 1)² = 0 gives equal zeroes 1/2 and 1/2; sum = 1/2 + 1/2 = 1 = −(−4)/4, product = 1/4 = c/a.",
                "solution_steps": [
                    "Recognize perfect square: (2s − 1)² = 0 -> s = 1/2, 1/2.",
                    "Verify sum: 1/2 + 1/2 = 1 and −b/a = −(−4)/4 = 1.",
                    "Verify product: (1/2)(1/2) = 1/4 and c/a = 1/4."
                ]
            },
            {
                "question": "Find the zeroes of 6x² − 3 − 7x cleanly (Exercise 2.2 Q1 iii):",
                "options": [
                    "3/2 and −1/3",
                    "−3/2 and 1/3",
                    "3 and −1/2",
                    "7/6 and −3/6"
                ],
                "answer": 0,
                "hint": "Rewrite first as 6x² − 7x − 3 and split −7x into −9x + 2x!",
                "explanation": "6x² − 9x + 2x − 3 = 3x(2x − 3) + 1(2x − 3) = (2x − 3)(3x + 1) = 0 -> x = 3/2, −1/3.",
                "solution_steps": [
                    "Reorder in standard form: 6x² − 7x − 3.",
                    "Factor by splitting middle term: (3x + 1)(2x − 3) = 0.",
                    "Solve zeroes x = −1/3 and x = 3/2."
                ]
            },
            {
                "question": "Find the zeroes of t² − 15 and verify coefficient relations (Exercise 2.2 Q1 v):",
                "options": [
                    "√15 and −√15; Sum = 0 (= −0/1) and Product = −15 (= −15/1)",
                    "15 and −15",
                    "√15 and 0",
                    "3 and −5"
                ],
                "answer": 0,
                "hint": "Factor using a² − b² with 15 = (√15)²!",
                "explanation": "t² − 15 = (t − √15)(t + √15) = 0 gives ±√15; α + β = 0 = −b/a and αβ = −15 = c/a.",
                "solution_steps": [
                    "Write t² − (√15)² = (t − √15)(t + √15) = 0.",
                    "Obtain zeroes +√15 and −√15.",
                    "Check sum = 0 (−0/1) and product = −15 (−15/1)."
                ]
            },
            {
                "question": "Find the zeroes of 3x² − x − 4 and verify sum & product (Exercise 2.2 Q1 vi):",
                "options": [
                    "4/3 and −1; Sum = 1/3 and Product = −4/3",
                    "−4/3 and 1; Sum = −1/3",
                    "4 and −3; Sum = 1",
                    "3/4 and −1"
                ],
                "answer": 0,
                "hint": "Product a·c = −12, sum b = −1 -> split −x = −4x + 3x!",
                "explanation": "3x² + 3x − 4x − 4 = 3x(x+1) − 4(x+1) = (x+1)(3x−4) -> x = −1 and 4/3; sum = 1/3 = −(−1)/3, prod = −4/3.",
                "solution_steps": [
                    "Split −x cleanly into −4x + 3x.",
                    "Factor (3x − 4)(x + 1) = 0 -> x = 4/3, −1.",
                    "Check 4/3 − 1 = 1/3 = −b/a and (4/3)(−1) = −4/3 = c/a."
                ]
            },
            {
                "question": "Construct a clean quadratic polynomial whose sum of zeroes is √2 and product of zeroes is 1/3 (Exercise 2.2 Q2 ii):",
                "options": [
                    "3x² − 3√2 x + 1",
                    "3x² + 3√2 x + 1",
                    "x² − 3√2 x + 3",
                    "3x² − √2 x − 1"
                ],
                "answer": 0,
                "hint": "Substitute S = √2 and P = 1/3 into k(x² − Sx + P), then take k = 3!",
                "explanation": "3[x² − √2 x + 1/3] = 3x² − 3√2 x + 1 gives sum = 3√2/3 = √2 and product = 1/3.",
                "solution_steps": [
                    "Write template x² − Sx + P -> x² − √2 x + 1/3.",
                    "Multiply by scaling factor k = 3 to clear denominator 3.",
                    "Result: 3x² − 3√2 x + 1."
                ]
            },
            {
                "question": "Form a quadratic polynomial whose sum of zeroes is 0 and product of zeroes is √5 (Exercise 2.2 Q2 iii):",
                "options": [
                    "x² + √5",
                    "x² − √5",
                    "x² + √5 x",
                    "x² − √5 x + 1"
                ],
                "answer": 0,
                "hint": "Plug S = 0 and P = √5 into x² − Sx + P!",
                "explanation": "x² − 0·x + √5 = x² + √5 directly gives α + β = 0 and αβ = √5.",
                "solution_steps": [
                    "Set S = 0 and P = √5.",
                    "Substitute into x² − Sx + P = x² − 0x + √5.",
                    "Simplify to x² + √5."
                ]
            },
            {
                "question": "Find a quadratic polynomial with sum = 1 and product = 1 (Exercise 2.2 Q2 iv):",
                "options": [
                    "x² − x + 1",
                    "x² + x + 1",
                    "x² − x − 1",
                    "x² + x − 1"
                ],
                "answer": 0,
                "hint": "Keep minus sign on Sx inside x² − Sx + P!",
                "explanation": "Plugging S = 1 and P = 1 into x² − Sx + P gives x² − x + 1.",
                "solution_steps": [
                    "Read S = 1, P = 1 carefully.",
                    "Substitute into x² − Sx + P.",
                    "Verify −b/a = 1 and c/a = 1 for x² − x + 1."
                ]
            },
            {
                "question": "Find a clean integer-coefficient quadratic polynomial with sum = −1/4 and product = 1/4 (Exercise 2.2 Q2 v):",
                "options": [
                    "4x² + x + 1",
                    "4x² − x + 1",
                    "4x² + x − 1",
                    "x² + 4x + 1"
                ],
                "answer": 0,
                "hint": "Watch double minus in −(−1/4)x inside 4[x² − Sx + P]!",
                "explanation": "4[x² − (−1/4)x + 1/4] = 4[x² + (1/4)x + 1/4] = 4x² + x + 1.",
                "solution_steps": [
                    "Substitute S = −1/4 and P = 1/4 -> x² + (1/4)x + 1/4.",
                    "Scale cleanly by k = 4.",
                    "Result: 4x² + x + 1."
                ]
            },
            {
                "question": "Find a quadratic polynomial whose sum of zeroes is 4 and product of zeroes is 1 (Exercise 2.2 Q2 vi):",
                "options": [
                    "x² − 4x + 1",
                    "x² + 4x + 1",
                    "x² − x + 4",
                    "x² − 4x − 1"
                ],
                "answer": 0,
                "hint": "Substitute S = 4 and P = 1 into x² − Sx + P!",
                "explanation": "With k = 1, x² − 4x + 1 yields α + β = −(−4)/1 = 4 and αβ = 1/1 = 1.",
                "solution_steps": [
                    "Identify S = 4, P = 1.",
                    "Substitute into x² − Sx + P.",
                    "Obtain x² − 4x + 1."
                ]
            },
            {
                "question": "If zeroes themselves (NOT sum and product!) are given as 5 and −2, which quadratic polynomial has those zeroes?",
                "options": [
                    "x² − 3x − 10",
                    "x² − 5x − 2",
                    "x² + 3x − 10",
                    "x² − 3x + 10"
                ],
                "answer": 0,
                "hint": "Compute S = 5 + (−2) = 3 and P = 5 × (−2) = −10 FIRST before applying x² − Sx + P!",
                "explanation": "Careful! Given individual zeroes α = 5, β = −2: S = 3 and P = −10, giving (x − 5)(x + 2) = x² − 3x − 10.",
                "solution_steps": [
                    "Check wording carefully: individual zeroes α = 5, β = −2 (not S, P).",
                    "Compute S = 5 + (−2) = 3 and P = 5 × (−2) = −10.",
                    "Form x² − 3x − 10."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge Quiz 1",
        "subtitle": "Mastery Challenge: Value-Zero Links, Unknown Constants & Quadratic Algebraic Reasoning",
        "questions": [
            {
                "question": "If −4 is a zero of the quadratic polynomial x² − x − (2k + 2), determine the exact value of constant k:",
                "options": [
                    "k = 9",
                    "k = 7",
                    "k = −9",
                    "k = 5"
                ],
                "answer": 0,
                "hint": "Substitute x = −4 and set p(−4) = 0 cleanly!",
                "explanation": "(−4)² − (−4) − (2k + 2) = 0 ⟹ 16 + 4 − 2k − 2 = 0 ⟹ 18 = 2k ⟹ k = 9.",
                "solution_steps": [
                    "Evaluate p(−4) = 0: (−4)² − (−4) − (2k + 2) = 0.",
                    "Simplify carefully: 16 + 4 − 2k − 2 = 18 − 2k = 0.",
                    "Solve 2k = 18 -> k = 9."
                ]
            },
            {
                "question": "If one zero of polynomial (a² + 9)x² + 13x + 6a is the RECIPROCAL of the other, find a:",
                "options": [
                    "a = 3  (since α·(1/α) = 1 = 6a / (a² + 9)  ⟹  (a − 3)² = 0)",
                    "a = −3",
                    "a = 9",
                    "a = 1"
                ],
                "answer": 0,
                "hint": "The product of two reciprocal zeroes α and 1/α ALWAYS equals 1!",
                "explanation": "Product = c/A = 6a/(a² + 9) = 1 ⟹ a² − 6a + 9 = 0 ⟹ (a − 3)² = 0 ⟹ a = 3.",
                "solution_steps": [
                    "Set β = 1/α so product αβ = 1.",
                    "Equate c/A = 1: 6a / (a² + 9) = 1 ⟹ a² − 6a + 9 = 0.",
                    "Factor (a − 3)² = 0 -> a = 3."
                ]
            },
            {
                "question": "If zeroes of quadratic polynomial x² + (a + 1)x + b are 2 and −3, then find a and b:",
                "options": [
                    "a = 0, b = −6",
                    "a = −2, b = −6",
                    "a = 5, b = −1",
                    "a = 2, b = 6"
                ],
                "answer": 0,
                "hint": "Sum = 2 + (−3) = −1 = −(a + 1), and Product = 2 × (−3) = −6 = b!",
                "explanation": "−(a + 1) = −1 ⟹ a + 1 = 1 ⟹ a = 0; product b = 2 × (−3) = −6.",
                "solution_steps": [
                    "Use sum: 2 + (−3) = −1 = −(a + 1) -> a + 1 = 1 -> a = 0.",
                    "Use product: 2 × (−3) = −6 = b/1 -> b = −6.",
                    "Check polynomial x² + x − 6 = (x − 2)(x + 3)."
                ]
            },
            {
                "question": "How many distinct polynomials can share the exact same two zeroes −2 and 5?",
                "options": [
                    "Infinitely many polynomials: k(x² − 3x − 10) for every non-zero real number k",
                    "Only 1 unique polynomial",
                    "Strictly 2 polynomials",
                    "Zero polynomials"
                ],
                "answer": 0,
                "hint": "Multiply (x + 2)(x − 5) by any non-zero scaling constant k = 1, 2, −5, 1/3...!",
                "explanation": "Changing k ≠ 0 stretches the parabola vertically without shifting its x-intercepts −2 and 5, yielding infinitely many valid polynomials!",
                "solution_steps": [
                    "Recall vertical scaling factor k ≠ 0 in k(x − α)(x − β).",
                    "Note p(x) = 0 still occurs at identical x = α and x = β.",
                    "Conclude infinitely many polynomials exist (1 for each k ≠ 0)."
                ]
            },
            {
                "question": "If the zeroes of ax² + bx + c (c ≠ 0) are EQUAL in magnitude and OPPOSITE in sign (e.g., α and −α), which coefficient must be 0?",
                "options": [
                    "b = 0  (since sum α + (−α) = −b/a = 0)",
                    "c = 0",
                    "a = 0",
                    "b = c"
                ],
                "answer": 0,
                "hint": "What is the sum of α and −α?",
                "explanation": "Opposite zeroes sum to zero: α + (−α) = 0 = −b/a ⟹ b = 0.",
                "solution_steps": [
                    "Write opposite zeroes as α and −α.",
                    "Compute sum = α + (−α) = 0.",
                    "Equate −b/a = 0 (with a ≠ 0) -> b = 0."
                ]
            },
            {
                "question": "If α and β are zeroes of 2x² + 5x + k satisfying α² + β² + αβ = 21/4, find k:",
                "options": [
                    "k = 2",
                    "k = 5",
                    "k = −2",
                    "k = 4"
                ],
                "answer": 0,
                "hint": "Rewrite α² + β² + αβ = (α + β)² − αβ cleanly!",
                "explanation": "α+β = −5/2 and αβ = k/2. Plugging into (α+β)² − αβ = 21/4 gives 25/4 − k/2 = 21/4 ⟹ k/2 = 4/4 = 1 ⟹ k = 2.",
                "solution_steps": [
                    "Read α + β = −5/2 and αβ = k/2.",
                    "Transform identity: α² + β² + αβ = (α + β)² − αβ.",
                    "Solve (25/4) − k/2 = 21/4 -> k/2 = 1 -> k = 2."
                ]
            },
            {
                "question": "Both zeroes of quadratic polynomial x² + 99x + 127 are:",
                "options": [
                    "Both negative (since sum = −99 < 0 and product = +127 > 0)",
                    "Both positive",
                    "One positive and one negative",
                    "Both equal to zero"
                ],
                "answer": 0,
                "hint": "If product αβ is positive, α and β MUST share the same sign; check sum α+β sign!",
                "explanation": "Positive product (+127) forces same signs; negative sum (−99) ensures both zeroes are negative!",
                "solution_steps": [
                    "Check product αβ = +127 > 0 -> same signs (+,+ or −,−).",
                    "Check sum α + β = −99 < 0 -> cannot be two positives.",
                    "Conclude both zeroes are negative."
                ]
            },
            {
                "question": "If 1 is a zero of both ay² + ay + 3 = 0 and y² + y + b = 0, find the product ab:",
                "options": [
                    "ab = 3  (since a = −3/2 and b = −2)",
                    "ab = −3",
                    "ab = 6",
                    "ab = −7/2"
                ],
                "answer": 0,
                "hint": "Substitute y = 1 into each polynomial separately to find a and b!",
                "explanation": "a(1) + a(1) + 3 = 0 ⟹ 2a = −3 ⟹ a = −3/2; 1 + 1 + b = 0 ⟹ b = −2; thus ab = (−3/2)(−2) = +3.",
                "solution_steps": [
                    "Plug y = 1 into first: 2a + 3 = 0 -> a = −3/2.",
                    "Plug y = 1 into second: 2 + b = 0 -> b = −2.",
                    "Multiply ab = (−3/2)(−2) = 3."
                ]
            },
            {
                "question": "What value does k take if α and β are zeroes of x² − (k + 6)x + 2(2k − 1) such that α + β = (1/2) αβ?",
                "options": [
                    "k = 7",
                    "k = 5",
                    "k = −7",
                    "k = 3"
                ],
                "answer": 0,
                "hint": "Equate k + 6 = (1/2) × 2(2k − 1)!",
                "explanation": "α+β = k+6 and αβ = 2(2k−1); setting k + 6 = 2k − 1 gives k = 7.",
                "solution_steps": [
                    "Read sum α + β = k + 6 and product αβ = 2(2k − 1).",
                    "Apply condition k + 6 = (1/2)[2(2k − 1)] = 2k − 1.",
                    "Solve k = 7."
                ]
            },
            {
                "question": "If α and β are zeroes of x² − 5x + 6, compute the value of 1/α + 1/β without even factoring!",
                "options": [
                    "5/6",
                    "6/5",
                    "−5/6",
                    "1/6"
                ],
                "answer": 0,
                "hint": "Combine fractions over common denominator αβ: (α + β)/(αβ)!",
                "explanation": "1/α + 1/β = (α + β)/(αβ) = 5/6 (matching roots 2, 3: 1/2 + 1/3 = 5/6).",
                "solution_steps": [
                    "Find common denominator: 1/α + 1/β = (α + β)/(αβ).",
                    "Substitute α + β = 5 and αβ = 6.",
                    "Obtain 5/6 cleanly."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge Quiz 2",
        "subtitle": "Final Mastery: Cubic Zeroes, Symmetric Identities & Complete Chapter 2 Synthesis",
        "questions": [
            {
                "question": "For cubic polynomial p(x) = 2x³ + x² − 5x + 2, which triple of numbers are its exact zeroes (verify sum, pairs & product)?",
                "options": [
                    "1/2, 1, and −2  (Sum = −1/2, Pairs = −5/2, Product = −1)",
                    "1/2, −1, and 2",
                    "−1/2, 1, and −2",
                    "2, 1, and 5"
                ],
                "answer": 0,
                "hint": "Test −b/a = −1/2, c/a = −5/2, and −d/a = −2/2 = −1!",
                "explanation": "Sum: 1/2 + 1 − 2 = −1/2 (= −b/a); Pairs: 1/2 − 2 − 1 = −5/2 (= c/a); Product: (1/2)(1)(−2) = −1 (= −d/a).",
                "solution_steps": [
                    "Read ratios: −b/a = −1/2, c/a = −5/2, −d/a = −2/2 = −1.",
                    "Verify 1/2 + 1 − 2 = −1/2.",
                    "Verify (1/2)(1)(−2) = −1 and pairwise sum = −5/2."
                ]
            },
            {
                "question": "Construct a cubic polynomial whose sum of zeroes = 2, sum of pairwise products = −7, and triple product = −14:",
                "options": [
                    "x³ − 2x² − 7x + 14",
                    "x³ + 2x² − 7x − 14",
                    "x³ − 2x² + 7x − 14",
                    "x³ − 7x² + 2x + 14"
                ],
                "answer": 0,
                "hint": "Follow alternating signs: x³ − (sum)x² + (pairs)x − (product)!",
                "explanation": "x³ − (2)x² + (−7)x − (−14) = x³ − 2x² − 7x + 14.",
                "solution_steps": [
                    "Recall template k[x³ − (∑α)x² + (∑αβ)x − (αβγ)].",
                    "Substitute ∑α = 2, ∑αβ = −7, αβγ = −14.",
                    "Simplify double negative on constant: x³ − 2x² − 7x + 14."
                ]
            },
            {
                "question": "If the zeroes of cubic polynomial x³ − 3x² + x + 1 are (a − b), a, and (a + b), find a:",
                "options": [
                    "a = 1  (since sum of all three = 3a = −(−3)/1 = 3)",
                    "a = −1",
                    "a = 3",
                    "a = ±√2"
                ],
                "answer": 0,
                "hint": "Notice −b and +b cancel immediately when taking the SUM of the three zeroes!",
                "explanation": "(a − b) + a + (a + b) = 3a = −(−3)/1 = 3 ⟹ a = 1 (and triple product gives 1 − b² = −1 ⟹ b = ±√2).",
                "solution_steps": [
                    "Sum three zeroes: (a − b) + a + (a + b) = 3a.",
                    "Equate to −(coeff of x²)/1 = +3.",
                    "Solve 3a = 3 -> a = 1."
                ]
            },
            {
                "question": "If α, β, γ are zeroes of x³ + 0x² − px + q (no x² term!), find the value of 1/α + 1/β + 1/γ:",
                "options": [
                    "(αβ + βγ + γα) / (αβγ) = (−p) / (−q) = p / q",
                    "−p / q",
                    "0",
                    "q / p"
                ],
                "answer": 0,
                "hint": "Combine over common denominator αβγ first!",
                "explanation": "c/a = −p and −d/a = −q; therefore (αβ + βγ + γα)/(αβγ) = (−p)/(−q) = p/q.",
                "solution_steps": [
                    "Rewrite 1/α + 1/β + 1/γ = (αβ + βγ + γα) / (αβγ).",
                    "Read c/a = −p and −d/a = −q carefully.",
                    "Divide (−p)/(−q) = p/q."
                ]
            },
            {
                "question": "If one zero of cubic polynomial x³ + ax² + bx + c is −1, then what does the product of the OTHER TWO zeroes equal?",
                "options": [
                    "b − a + 1",
                    "a − b + 1",
                    "b − a − 1",
                    "a + b + 1"
                ],
                "answer": 0,
                "hint": "Compute p(−1) = 0 to solve c = b − a + 1, AND note (−1)·β·γ = −c ⟹ βγ = +c!",
                "explanation": "p(−1) = −1 + a − b + c = 0 gives c = b − a + 1. Meanwhile αβγ = (−1)βγ = −c/1 ⟹ βγ = c = b − a + 1!",
                "solution_steps": [
                    "Plug zero x = −1: (−1)³ + a(−1)² + b(−1) + c = 0 -> c = b − a + 1.",
                    "Apply triple product rule: (−1) · β · γ = −c/1 = −c.",
                    "Divide by −1: βγ = c = b − a + 1."
                ]
            },
            {
                "question": "For cubic ax³ + bx² + cx + d with zeroes α, β, γ, if TWO zeroes equal 0, find the third zero:",
                "options": [
                    "−b / a  (also note c = 0 and d = 0 since pairwise & triple products vanish)",
                    "−c / a",
                    "−d / a",
                    "b / a"
                ],
                "answer": 0,
                "hint": "Set β = 0 and γ = 0 in α + β + γ = −b/a!",
                "explanation": "α + 0 + 0 = −b/a directly gives third zero α = −b/a (and c = d = 0).",
                "solution_steps": [
                    "Set two zeroes β = 0, γ = 0.",
                    "Plug into sum α + β + γ = −b/a.",
                    "Obtain α = −b/a immediately."
                ]
            },
            {
                "question": "If α and β are zeroes of x² − 4x + 1, calculate α² + β² cleanly using symmetric identity:",
                "options": [
                    "14",
                    "16",
                    "18",
                    "12"
                ],
                "answer": 0,
                "hint": "Use α² + β² = (α + β)² − 2αβ with α + β = 4 and αβ = 1!",
                "explanation": "α² + β² = 4² − 2(1) = 16 − 2 = 14.",
                "solution_steps": [
                    "Read α + β = 4 and αβ = 1.",
                    "Recall algebraic identity: α² + β² = (α + β)² − 2αβ.",
                    "Compute 16 − 2 = 14."
                ]
            },
            {
                "question": "If α and β are zeroes of p(x) = x² − x − 2, form a NEW quadratic polynomial whose zeroes are 2α + 1 and 2β + 1:",
                "options": [
                    "x² − 4x − 5",
                    "x² + 4x − 5",
                    "x² − 2x − 5",
                    "x² − 4x + 5"
                ],
                "answer": 0,
                "hint": "From α + β = 1, αβ = −2, find new sum S' = 2(α+β) + 2 and new product P' = 4αβ + 2(α+β) + 1!",
                "explanation": "S' = 2(1)+2 = 4; P' = 4(−2)+2(1)+1 = −8+2+1 = −5. Template x² − S'x + P' gives x² − 4x − 5.",
                "solution_steps": [
                    "Read α + β = 1 and αβ = −2.",
                    "Compute new sum S' = (2α+1) + (2β+1) = 2(1) + 2 = 4.",
                    "Compute new product P' = 4αβ + 2(α+β) + 1 = −8 + 2 + 1 = −5 -> x² − 4x − 5."
                ]
            },
            {
                "question": "Which statement about zeroes vs. degree is FALSE?",
                "options": [
                    "A polynomial of degree 2 ALWAYS intersects the x-axis at 2 distinct points",
                    "Every linear polynomial ax + b (a ≠ 0) has exactly 1 zero (−b/a)",
                    "Every cubic polynomial has at most 3 zeroes",
                    "Zeroes of y = p(x) are x-coordinates of x-axis intersections"
                ],
                "answer": 0,
                "hint": "Remember Case 2 (1 touch) and Case 3 (0 crossings like x² + 1)!",
                "explanation": "A degree 2 polynomial has AT MOST 2 real zeroes—it may intersect at 2, 1, or 0 points.",
                "solution_steps": [
                    "Recall Case 3 quadratic x² + 1 has 0 real x-intercepts.",
                    "Confirm Case 2 (x − 2)² has only 1 x-intercept.",
                    "Spot 'ALWAYS 2 distinct points' as false."
                ]
            },
            {
                "question": "If quadratic polynomial ax² + bx + c (a ≠ 0) has zeroes α, β AND linear polynomial px + q intersects at its zero, which master statement ties Chapter 2 together?",
                "options": [
                    "Real zeroes are x-intercepts (≤ degree), while algebraic factor expansions link zeroes directly to polynomial coefficients",
                    "Linear polynomials form curved U-shaped parabolas",
                    "Product of zeroes of ax² + bx + c equals −c/a",
                    "Cubic polynomials allow 4 distinct real zeroes"
                ],
                "answer": 0,
                "hint": "Check signs of αβ = +c/a and degree bounds!",
                "explanation": "Chapter 2 unifies geometry (x-intercepts bounded by degree n) and algebra (Vieta coefficient formulas for linear, quadratic, cubic).",
                "solution_steps": [
                    "Eliminate curved linear lines, −c/a product sign error, and degree-3 > 3 error.",
                    "Verify x-intercepts ≤ degree and coefficient formulas match Chapter 2.",
                    "Select master unifying statement."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch2 Class 10 Maths Part 3.")
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 4: Exploring Algebraic Identities
Slides Data Generator - Part 3 (Slides 17 to 20 - Silent Mastery Quizzes, 40 Questions Total)
Strictly 1-3 word titles, zero spoken audio, zero human names, hints + 3-step solutions.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Basics Patterns Quiz",
        "subtitle": "Sections 4.1–4.3 Practice Set (10 Questions): Consecutive Squares, Binomial Models, Identities vs Equations & Area Geometry",
        "questions": [
            {
                "question": "For any three consecutive integers n − 1, n, and n + 1, what constant value does (n − 1)² + (n + 1)² − 2n² always simplify to?",
                "options": ["2", "0", "4", "n"],
                "answer": 0,
                "hint": "Expand (n² − 2n + 1) + (n² + 2n + 1) − 2n²!",
                "explanation": "The ±2n terms and ±2n² terms cancel cleanly, leaving 1 + 1 = 2 identically for every integer n.",
                "solution_steps": [
                    "Expand first binomial: (n − 1)² = n² − 2n + 1; expand second: (n + 1)² = n² + 2n + 1.",
                    "Add both expansions: (n² − 2n + 1) + (n² + 2n + 1) = 2n² + 2.",
                    "Subtract 2n²: (2n² + 2) − 2n² = 2 (constant invariant for all n)."
                ]
            },
            {
                "question": "Compute 43² mentally using the geometric identity (a + b)² = a² + 2ab + b² with a = 40 and b = 3.",
                "options": ["1849", "1609", "1729", "1840"],
                "answer": 0,
                "hint": "Don't drop the two 40 × 3 rectangles!",
                "explanation": "40² + 2(40)(3) + 3² = 1600 + 240 + 9 = 1849.",
                "solution_steps": [
                    "Rewrite 43² as (40 + 3)² with a = 40 and b = 3.",
                    "Apply identity: 40² + 2(40)(3) + 3² = 1600 + 240 + 9.",
                    "Sum all four tiles: 1600 + 240 + 9 = 1849."
                ]
            },
            {
                "question": "Which of the following is a CONDITIONAL EQUATION rather than a universal algebraic identity?",
                "options": ["x² − 1 = 24", "(x + 2)² = x² + 4x + 4", "(a − b)² = a² − 2ab + b²", "(p + q)(p − q) = p² − q²"],
                "answer": 0,
                "hint": "Test x = 0 in each option!",
                "explanation": "x² − 1 = 24 is only true when x = ±5 (at x = 0, −1 ≠ 24), whereas the other three hold identically for all real numbers.",
                "solution_steps": [
                    "An algebraic identity holds for ALL valid substitutions of its variables.",
                    "Test x = 0 in x² − 1 = 24: LHS = −1 ≠ 24, so it fails for almost all numbers.",
                    "Hence x² − 1 = 24 is a conditional equation (solutions x = 5, −5 only)."
                ]
            },
            {
                "question": "In the geometric square model of side (a + b), what is the combined area of the two non-square rectangular tiles?",
                "options": ["2ab", "ab", "a² + b²", "2(a + b)"],
                "answer": 0,
                "hint": "Each rectangle measures length a and width b!",
                "explanation": "Two rectangles each of area a × b contribute ab + ab = 2ab.",
                "solution_steps": [
                    "Partition a square of side (a + b) vertically and horizontally into segments a and b.",
                    "Main-diagonal regions are squares of areas a² and b².",
                    "Two off-diagonal rectangles each measure a × b, summing to 2ab."
                ]
            },
            {
                "question": "Factorize the quadratic expression 16p² + 40pq + 25q² cleanly using a standard identity.",
                "options": ["(4p + 5q)²", "(4p − 5q)²", "(4p + 5q)(4p − 5q)", "(8p + 5q)²"],
                "answer": 0,
                "hint": "Check a = 4p, b = 5q, and 2ab = 2(4p)(5q)!",
                "explanation": "(4p)² + 2(4p)(5q) + (5q)² = (4p + 5q)².",
                "solution_steps": [
                    "Identify outer square roots: 16p² = (4p)² and 25q² = (5q)².",
                    "Verify middle term: 2(4p)(5q) = 40pq (exact positive match).",
                    "Factor using a² + 2ab + b² = (a + b)² to get (4p + 5q)²."
                ]
            },
            {
                "question": "In the geometric proof of (a − b)², starting from a big square of area a², we remove one rectangle of area ab and one shorter strip of area b(a − b). What algebraic identity does subtracting a² − ab − b(a − b) confirm?",
                "options": ["a² − 2ab + b²", "a² − b²", "a² − ab − b²", "a² + 2ab − b²"],
                "answer": 0,
                "hint": "Distribute −b(a − b) = −ab + b² carefully!",
                "explanation": "a² − ab − (ab − b²) = a² − ab − ab + b² = a² − 2ab + b².",
                "solution_steps": [
                    "Start with full square area a² and subtract full strip ab.",
                    "Subtract remaining bottom strip of area b(a − b) = ab − b².",
                    "Combine: a² − ab − ab + b² = a² − 2ab + b² = (a − b)²."
                ]
            },
            {
                "question": "Expand (3x − 1/2)² cleanly using the identity (a − b)².",
                "options": ["9x² − 3x + 1/4", "9x² − 3x − 1/4", "9x² + 3x + 1/4", "9x² − 1/4"],
                "answer": 0,
                "hint": "Compute (3x)² − 2(3x)(1/2) + (1/2)²!",
                "explanation": "9x² − 3x + 1/4.",
                "solution_steps": [
                    "Set a = 3x and b = 1/2 in (a − b)² = a² − 2ab + b².",
                    "Compute terms: (3x)² = 9x², −2(3x)(1/2) = −3x, and (1/2)² = +1/4.",
                    "Combine cleanly: 9x² − 3x + 1/4."
                ]
            },
            {
                "question": "If x + 1/x = 7, find the exact value of x² + 1/x² using (a + b)².",
                "options": ["47", "49", "51", "45"],
                "answer": 0,
                "hint": "Square both sides of x + 1/x = 7 and note 2(x)(1/x) = 2!",
                "explanation": "(x + 1/x)² = x² + 2 + 1/x² = 49 ⇒ x² + 1/x² = 49 − 2 = 47.",
                "solution_steps": [
                    "Square both sides: (x + 1/x)² = 7² = 49.",
                    "Expand LHS: x² + 2(x)(1/x) + 1/x² = x² + 2 + 1/x².",
                    "Subtract 2 from both sides: x² + 1/x² = 49 − 2 = 47."
                ]
            },
            {
                "question": "Factorize 49y² − 14y + 1 completely.",
                "options": ["(7y − 1)²", "(7y + 1)²", "(7y − 1)(7y + 1)", "(49y − 1)²"],
                "answer": 0,
                "hint": "Notice 49y² = (7y)², 1 = 1², and −14y = −2(7y)(1)!",
                "explanation": "(7y)² − 2(7y)(1) + 1² = (7y − 1)².",
                "solution_steps": [
                    "Spot squares (7y)² and 1² at the ends.",
                    "Verify middle term: −2(7y)(1) = −14y matches.",
                    "Rewrite as perfect square (7y − 1)²."
                ]
            },
            {
                "question": "Evaluate 99² using (100 − 1)².",
                "options": ["9801", "9901", "9899", "9799"],
                "answer": 0,
                "hint": "Compute 10000 − 200 + 1!",
                "explanation": "100² − 2(100)(1) + 1² = 10000 − 200 + 1 = 9801.",
                "solution_steps": [
                    "Write 99² = (100 − 1)².",
                    "Apply (a − b)²: 100² − 2(100)(1) + 1² = 10000 − 200 + 1.",
                    "Evaluate cleanly: 9801."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Tiles Splitting Quiz",
        "subtitle": "Sections 4.4–4.6 Practice Set (10 Questions): (a+b+c)², Śhrīdharāchārya's Method, Algebra Tiles & Middle-Term Splitting",
        "questions": [
            {
                "question": "Expand (2a − b + c)² using the trinomial square identity.",
                "options": ["4a² + b² + c² − 4ab − 2bc + 4ac", "4a² − b² + c² − 4ab + 2bc + 4ac", "4a² + b² + c² − 2ab − bc + 2ac", "4a² + b² + c²"],
                "answer": 0,
                "hint": "Treat second term as (−b): (−b)² = +b², while −b times +c gives −2bc!",
                "explanation": "(2a)² + (−b)² + c² + 2(2a)(−b) + 2(−b)(c) + 2(c)(2a) = 4a² + b² + c² − 4ab − 2bc + 4ac.",
                "solution_steps": [
                    "Assign x = 2a, y = −b, z = c in (x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx.",
                    "Compute squares: (2a)² + (−b)² + c² = 4a² + b² + c².",
                    "Compute cross terms: −4ab − 2bc + 4ac."
                ]
            },
            {
                "question": "Apply Śhrīdharāchārya's mental squaring rule a² = (a + b)(a − b) + b² to evaluate 89² cleanly with shift b = 11.",
                "options": ["7921", "7821", "7911", "8021"],
                "answer": 0,
                "hint": "Evaluate (89 + 11)(89 − 11) + 11² = 100 × 78 + 121!",
                "explanation": "89² = (89 + 11)(89 − 11) + 11² = 100 × 78 + 121 = 7800 + 121 = 7921.",
                "solution_steps": [
                    "Choose shift b = 11 so a + b = 89 + 11 = 100 (easy base multiple).",
                    "Compute a − b = 89 − 11 = 78; multiply (100)(78) = 7800.",
                    "Add b² = 11² = 121: 7800 + 121 = 7921."
                ]
            },
            {
                "question": "Factorize 81x² − 49y² cleanly using difference of squares.",
                "options": ["(9x + 7y)(9x − 7y)", "(9x − 7y)²", "(81x + 49y)(81x − 49y)", "(9x + 7y)²"],
                "answer": 0,
                "hint": "Write 81x² = (9x)² and 49y² = (7y)²!",
                "explanation": "(9x)² − (7y)² = (9x + 7y)(9x − 7y).",
                "solution_steps": [
                    "Express both terms as squares: (9x)² − (7y)².",
                    "Apply identity A² − B² = (A + B)(A − B) with A = 9x, B = 7y.",
                    "Result: (9x + 7y)(9x − 7y)."
                ]
            },
            {
                "question": "Suppose an Algebra Tile rectangle uses 1 x²-tile, 8 rectangular x-tiles, and 15 unit square tiles. Which dimensions match the assembled rectangle?",
                "options": ["(x + 3) by (x + 5)", "(x + 1) by (x + 15)", "(x + 2) by (x + 6)", "(x + 4) by (x + 4)"],
                "answer": 0,
                "hint": "Which positive integers sum to 8 and multiply to 15?",
                "explanation": "Splitting 8 x-tiles into 3 rows and 5 columns creates a 3 × 5 = 15 unit corner, giving dimensions (x + 3) and (x + 5).",
                "solution_steps": [
                    "Total polynomial area represented by tiles is x² + 8x + 15.",
                    "Arrange 8 x-tiles as 3 vertical + 5 horizontal so 3 × 5 = 15 fills the unit corner.",
                    "Outer sides of the unbroken rectangle measure (x + 3) and (x + 5)."
                ]
            },
            {
                "question": "Factorize x² + 15x + 54 using middle-term splitting without tiles.",
                "options": ["(x + 6)(x + 9)", "(x + 3)(x + 18)", "(x + 2)(x + 27)", "(x + 6)(x − 9)"],
                "answer": 0,
                "hint": "Find a + b = 15 and ab = 54!",
                "explanation": "6 + 9 = 15 and 6 × 9 = 54 ⇒ (x + 6)(x + 9).",
                "solution_steps": [
                    "Look for integers summing to +15 and multiplying to +54.",
                    "Pair (6, 9) gives 6 + 9 = 15 and 6 × 9 = 54.",
                    "Split & group: x² + 6x + 9x + 54 = x(x + 6) + 9(x + 6) = (x + 6)(x + 9)."
                ]
            },
            {
                "question": "Factorize x² − 13x + 40 completely.",
                "options": ["(x − 5)(x − 8)", "(x + 5)(x + 8)", "(x − 4)(x − 10)", "(x − 5)(x + 8)"],
                "answer": 0,
                "hint": "Positive product +40 with negative sum −13 forces both numbers negative!",
                "explanation": "(−5) + (−8) = −13 and (−5)(−8) = +40 ⇒ (x − 5)(x − 8).",
                "solution_steps": [
                    "Product +40 > 0 and sum −13 < 0 implies two negative factors.",
                    "Test pairs of 40: (−5) + (−8) = −13 and (−5)(−8) = +40.",
                    "Write factored product: (x − 5)(x − 8)."
                ]
            },
            {
                "question": "Factorize x² + 4x − 32 completely.",
                "options": ["(x + 8)(x − 4)", "(x − 8)(x + 4)", "(x − 16)(x + 2)", "(x + 8)(x + 4)"],
                "answer": 0,
                "hint": "Negative product −32 requires opposite signs whose difference is 4 (larger number gets + sign)!",
                "explanation": "8 + (−4) = +4 and 8 × (−4) = −32 ⇒ (x + 8)(x − 4).",
                "solution_steps": [
                    "Product −32 < 0 requires one positive and one negative factor.",
                    "Pair (+8, −4) satisfies 8 − 4 = +4 and 8(−4) = −32.",
                    "Split & factor: (x + 8)(x − 4)."
                ]
            },
            {
                "question": "How many distinct non-overlapping regions partition the geometric 3 × 3 grid model for (a + b + c)²?",
                "options": ["9 regions (3 diagonal squares and 6 off-diagonal rectangles)", "6 regions", "4 regions", "12 regions"],
                "answer": 0,
                "hint": "Multiply 3 intervals along width by 3 intervals along height!",
                "explanation": "3 × 3 partitioning forms 9 regions: squares a², b², c² along the diagonal plus paired rectangles 2ab, 2bc, 2ca.",
                "solution_steps": [
                    "Divide both top and left edges of length (a + b + c) into 3 parts: a, b, c.",
                    "Grid intersections create 3 × 3 = 9 rectangular tiles.",
                    "3 tiles on diagonal are squares (a², b², c²); 6 off-diagonal tiles form 2ab + 2bc + 2ca."
                ]
            },
            {
                "question": "Factorize 3x² + 11x + 6 cleanly using generalized splitting (split 11x with product 3 × 6 = 18).",
                "options": ["(3x + 2)(x + 3)", "(3x + 3)(x + 2)", "(3x + 1)(x + 6)", "(x + 2)(x + 3)"],
                "answer": 0,
                "hint": "Split 11x = 9x + 2x since 9 × 2 = 18 and 9 + 2 = 11!",
                "explanation": "3x² + 9x + 2x + 6 = 3x(x + 3) + 2(x + 3) = (3x + 2)(x + 3).",
                "solution_steps": [
                    "Multiply leading coefficient by constant: 3 × 6 = 18.",
                    "Find integers adding to 11 with product 18: 9 and 2.",
                    "Group: 3x² + 9x + 2x + 6 = 3x(x + 3) + 2(x + 3) = (3x + 2)(x + 3)."
                ]
            },
            {
                "question": "Evaluate 73² − 27² swiftly using difference of squares.",
                "options": ["4600", "460", "5329", "4500"],
                "answer": 0,
                "hint": "Compute (73 + 27)(73 − 27)!",
                "explanation": "(73 + 27)(73 − 27) = 100 × 46 = 4600.",
                "solution_steps": [
                    "Identify a = 73 and b = 27 in a² − b².",
                    "Apply (a + b)(a − b) = (73 + 27)(73 − 27).",
                    "Multiply cleanly: 100 × 46 = 4600."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Cubic Rational Quiz",
        "subtitle": "Sections 4.7–4.8 Practice Set (10 Questions): Cubic Identities, 3xyz Shortcut, Rational Simplification & Rectangular Areas",
        "questions": [
            {
                "question": "Expand (3x − 2)³ cleanly using (a − b)³ = a³ − 3a²b + 3ab² − b³.",
                "options": ["27x³ − 54x² + 36x − 8", "27x³ − 8", "27x³ − 18x² + 12x − 8", "27x³ + 54x² + 36x − 8"],
                "answer": 0,
                "hint": "Set a = 3x, b = 2; compute 3(9x²)(2) = 54x² and 3(3x)(4) = 36x!",
                "explanation": "(3x)³ − 3(3x)²(2) + 3(3x)(2)² − 2³ = 27x³ − 54x² + 36x − 8.",
                "solution_steps": [
                    "Assign a = 3x and b = 2 into (a − b)³.",
                    "Evaluate each term: (3x)³ = 27x³, −3(9x²)(2) = −54x², +3(3x)(4) = +36x, −2³ = −8.",
                    "Result: 27x³ − 54x² + 36x − 8."
                ]
            },
            {
                "question": "In the 3D volume model of a cube of edge (a + b), what is the total volume of the SIX non-cube cuboids?",
                "options": ["3a²b + 3ab²", "a³ + b³", "6ab", "2a²b + 2ab²"],
                "answer": 0,
                "hint": "Remove a³ and b³ from (a + b)³ = a³ + 3a²b + 3ab² + b³!",
                "explanation": "Three cuboids of dimensions a × a × b contribute 3a²b and three cuboids of a × b × b contribute 3ab².",
                "solution_steps": [
                    "Full cube (a + b)³ decomposes into 8 pieces: 2 cubes + 6 cuboids.",
                    "2 cubes hold volumes a³ and b³.",
                    "Remaining 6 cuboids hold 3(a²b) + 3(ab²) = 3a²b + 3ab²."
                ]
            },
            {
                "question": "Factorize 64p³ − 125q³ completely using difference of two cubes.",
                "options": ["(4p − 5q)(16p² + 20pq + 25q²)", "(4p − 5q)(16p² − 20pq + 25q²)", "(4p + 5q)(16p² − 20pq + 25q²)", "(4p − 5q)³"],
                "answer": 0,
                "hint": "Set x = 4p and y = 5q in x³ − y³ = (x − y)(x² + xy + y²)!",
                "explanation": "(4p)³ − (5q)³ = (4p − 5q)(16p² + 20pq + 25q²).",
                "solution_steps": [
                    "Identify cube roots: 64p³ = (4p)³ and 125q³ = (5q)³.",
                    "Apply x³ − y³ = (x − y)(x² + xy + y²) with x = 4p, y = 5q.",
                    "Compute quadratic bracket: (4p)² + (4p)(5q) + (5q)² = 16p² + 20pq + 25q²."
                ]
            },
            {
                "question": "Without evaluating large cubes, find the exact value of (18)³ + (−10)³ + (−8)³.",
                "options": ["4320", "−4320", "0", "1440"],
                "answer": 0,
                "hint": "Notice 18 + (−10) + (−8) = 0, so sum equals 3xyz!",
                "explanation": "3(18)(−10)(−8) = 54 × 80 = +4320.",
                "solution_steps": [
                    "Sum bases: x + y + z = 18 + (−10) + (−8) = 0.",
                    "By conditional identity: x³ + y³ + z³ = 3xyz.",
                    "Compute 3(18)(−10)(−8) = 54 × 80 = 4320."
                ]
            },
            {
                "question": "Simplify the rational expression (x² − 25) / (x² − 3x − 10) for x ≠ −2, 5.",
                "options": ["(x + 5) / (x + 2)", "(x − 5) / (x + 2)", "(x + 5) / (x − 2)", "5 / (3x + 2)"],
                "answer": 0,
                "hint": "Factor numerator as (x − 5)(x + 5) and denominator as (x − 5)(x + 2)!",
                "explanation": "Cancel common non-zero factor (x − 5) to obtain (x + 5)/(x + 2).",
                "solution_steps": [
                    "Factor numerator using difference of squares: x² − 25 = (x − 5)(x + 5).",
                    "Factor denominator via middle-term splitting (−5 + 2 = −3): (x − 5)(x + 2).",
                    "Cancel common non-zero factor (x − 5): result is (x + 5)/(x + 2)."
                ]
            },
            {
                "question": "Simplify (x³ + 27) / (x² − 3x + 9) for all valid real values of x.",
                "options": ["x + 3", "x − 3", "x + 9", "x² + 3"],
                "answer": 0,
                "hint": "Factor x³ + 3³ using sum of two cubes!",
                "explanation": "(x³ + 27)/(x² − 3x + 9) = [(x + 3)(x² − 3x + 9)] / (x² − 3x + 9) = x + 3.",
                "solution_steps": [
                    "Rewrite numerator using x³ + y³: x³ + 3³ = (x + 3)(x² − 3x + 9).",
                    "Note quadratic denominator (x² − 3x + 9) is strictly positive for all real x.",
                    "Cancel identical non-zero factor (x² − 3x + 9) → x + 3."
                ]
            },
            {
                "question": "A rectangular playground has area (x² + 12x + 35) m² and length (x + 7) m. What is its width?",
                "options": ["(x + 5) m", "(x + 7) m", "(x + 28) m", "(x − 5) m"],
                "answer": 0,
                "hint": "Split 12x = 7x + 5x to factor the area polynomial!",
                "explanation": "Area = (x + 7)(x + 5); dividing by length (x + 7) yields width (x + 5) m.",
                "solution_steps": [
                    "Factor quadratic area: 7 + 5 = 12 and 7 × 5 = 35 → (x + 7)(x + 5).",
                    "Compute Width = Area / Length = [(x + 7)(x + 5)] / (x + 7).",
                    "Cancel (x + 7) ≠ 0 to get width (x + 5) m."
                ]
            },
            {
                "question": "Factorize 8x³ + y³ + 27z³ − 18xyz cleanly.",
                "options": ["(2x + y + 3z)(4x² + y² + 9z² − 2xy − 3yz − 6zx)", "(2x + y + 3z)(4x² + y² + 9z² + 2xy + 3yz + 6zx)", "(2x − y + 3z)(4x² + y² + 9z²)", "(2x + y + 3z)³"],
                "answer": 0,
                "hint": "Identify terms (2x)³, y³, (3z)³, and −3(2x)(y)(3z) = −18xyz!",
                "explanation": "Applying a³ + b³ + c³ − 3abc with a = 2x, b = y, c = 3z gives (2x + y + 3z)(4x² + y² + 9z² − 2xy − 3yz − 6zx).",
                "solution_steps": [
                    "Rewrite expression as (2x)³ + y³ + (3z)³ − 3(2x)(y)(3z).",
                    "Substitute a = 2x, b = y, c = 3z into master cubic identity.",
                    "Result: (2x + y + 3z)(4x² + y² + 9z² − 2xy − 3yz − 6zx)."
                ]
            },
            {
                "question": "If (x² − 4) / (x² − 4x + 4) simplifies to P/Q in lowest terms (x ≠ 2), what is the simplified rational expression?",
                "options": ["(x + 2) / (x − 2)", "(x − 2) / (x + 2)", "1", "−1 / (−4x)"],
                "answer": 0,
                "hint": "Numerator is (x − 2)(x + 2); denominator is perfect square (x − 2)²!",
                "explanation": "Canceling one common factor (x − 2) leaves (x + 2)/(x − 2).",
                "solution_steps": [
                    "Factor numerator: x² − 4 = (x − 2)(x + 2).",
                    "Factor denominator: x² − 4x + 4 = (x − 2)(x − 2).",
                    "Cancel one (x − 2) factor (x ≠ 2) → (x + 2)/(x − 2)."
                ]
            },
            {
                "question": "Evaluate 999³ cleanly using (1000 − 1)³ = a³ − b³ − 3ab(a − b).",
                "options": ["997,002,999", "999,000,001", "997,999,999", "996,002,999"],
                "answer": 0,
                "hint": "Compute 10⁹ − 1 − 3000(999)!",
                "explanation": "1,000,000,000 − 1 − 2,997,000 = 997,002,999.",
                "solution_steps": [
                    "Write 999³ = (1000 − 1)³ with a = 1000 and b = 1.",
                    "Apply a³ − b³ − 3ab(a − b) = 1,000,000,000 − 1 − 3(1000)(1)(999).",
                    "Compute 1,000,000,000 − 2,997,001 = 997,002,999."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Chapter Mastery Quiz",
        "subtitle": "End-of-Chapter Mixed Exercises (10 Questions): Comprehensive Products, Factorisations, Simplifications & Algebraic Proofs",
        "questions": [
            {
                "question": "Evaluate the product 104 × 96 cleanly using an algebraic identity.",
                "options": ["9984", "10016", "9964", "9980"],
                "answer": 0,
                "hint": "Express as (100 + 4)(100 − 4)!",
                "explanation": "100² − 4² = 10000 − 16 = 9984.",
                "solution_steps": [
                    "Rewrite 104 × 96 = (100 + 4)(100 − 4).",
                    "Apply (a + b)(a − b) = a² − b².",
                    "Evaluate 100² − 4² = 10000 − 16 = 9984."
                ]
            },
            {
                "question": "Factorize 4a² + 9b² + 16c² + 12ab − 24bc − 16ac cleanly back into a squared trinomial.",
                "options": ["(2a + 3b − 4c)²", "(2a − 3b + 4c)²", "(2a + 3b + 4c)²", "(4a + 9b − 16c)²"],
                "answer": 0,
                "hint": "Notice both terms containing c (−24bc and −16ac) carry minus signs, while +12ab is positive!",
                "explanation": "Square terms are (2a)², (3b)², (−4c)²; cross terms 2(2a)(3b) = 12ab, 2(3b)(−4c) = −24bc, 2(2a)(−4c) = −16ac match cleanly.",
                "solution_steps": [
                    "Identify positive/negative signs: 12ab > 0 ⇒ a & b share same sign (+); −24bc, −16ac < 0 ⇒ c is negative.",
                    "Take roots 2a, +3b, and −4c.",
                    "Verify all 3 cross terms match (2a + 3b − 4c)²."
                ]
            },
            {
                "question": "Simplify (3x² − 12) / (3x² + 9x + 6) completely in lowest terms (x ≠ −1, −2).",
                "options": ["(x − 2) / (x + 1)", "(x + 2) / (x + 1)", "(x − 2) / (x + 2)", "3(x − 2) / (x + 1)"],
                "answer": 0,
                "hint": "Pull out common constant factor 3 from BOTH numerator and denominator first!",
                "explanation": "3(x² − 4) / 3(x² + 3x + 2) = [(x − 2)(x + 2)] / [(x + 1)(x + 2)] = (x − 2)/(x + 1).",
                "solution_steps": [
                    "Factor GCF 3 from top & bottom: [3(x² − 4)] / [3(x² + 3x + 2)], cancel 3.",
                    "Factor top as (x − 2)(x + 2) and bottom as (x + 1)(x + 2).",
                    "Cancel common factor (x + 2) to obtain (x − 2)/(x + 1)."
                ]
            },
            {
                "question": "If x + y + z = 9 and xy + yz + zx = 26, find the exact value of x² + y² + z².",
                "options": ["29", "81", "55", "107"],
                "answer": 0,
                "hint": "Rearrange (x + y + z)² = x² + y² + z² + 2(xy + yz + zx)!",
                "explanation": "x² + y² + z² = 9² − 2(26) = 81 − 52 = 29.",
                "solution_steps": [
                    "Recall trinomial identity: (x + y + z)² = x² + y² + z² + 2(xy + yz + zx).",
                    "Substitute given values: 9² = x² + y² + z² + 2(26).",
                    "Solve: 81 − 52 = 29."
                ]
            },
            {
                "question": "Factorize x⁴ − 16 completely over polynomials with integer coefficients.",
                "options": ["(x² + 4)(x + 2)(x − 2)", "(x² − 4)(x² − 4)", "(x² + 4)(x² + 4)", "(x − 2)⁴"],
                "answer": 0,
                "hint": "Apply difference of squares TWICE: first x⁴ − 16, then x² − 4!",
                "explanation": "x⁴ − 16 = (x² + 4)(x² − 4) = (x² + 4)(x + 2)(x − 2).",
                "solution_steps": [
                    "Express as difference of squares: (x²)² − 4² = (x² + 4)(x² − 4).",
                    "Notice second factor x² − 4 factors further as (x + 2)(x − 2).",
                    "Complete factorization: (x² + 4)(x + 2)(x − 2)."
                ]
            },
            {
                "question": "Prove what (a + b)² − (a − b)² simplifies to as a single monomial identity.",
                "options": ["4ab", "2(a² + b²)", "2ab", "0"],
                "answer": 0,
                "hint": "Subtract (a² − 2ab + b²) from (a² + 2ab + b²)!",
                "explanation": "a² and b² cancel out while +2ab − (−2ab) = +4ab.",
                "solution_steps": [
                    "Expand first square: a² + 2ab + b²; second square: a² − 2ab + b².",
                    "Subtract second from first: (a² + 2ab + b²) − (a² − 2ab + b²).",
                    "Square terms cancel, leaving 2ab + 2ab = 4ab."
                ]
            },
            {
                "question": "If a − b = 4 and ab = 21, find the exact value of a³ − b³.",
                "options": ["316", "64", "252", "190"],
                "answer": 0,
                "hint": "Use a³ − b³ = (a − b)³ + 3ab(a − b)!",
                "explanation": "a³ − b³ = 4³ + 3(21)(4) = 64 + 252 = 316.",
                "solution_steps": [
                    "Rearrange (a − b)³ = a³ − b³ − 3ab(a − b) to isolate a³ − b³.",
                    "Substitute a − b = 4 and ab = 21: a³ − b³ = 4³ + 3(21)(4).",
                    "Compute 64 + 252 = 316."
                ]
            },
            {
                "question": "A rectangular garden plot has perimeter (4x + 18) m and area (x² + 9x + 14) m². Find its side dimensions.",
                "options": ["(x + 7) m and (x + 2) m", "(x + 14) m and (x + 1) m", "(x + 9) m and (x + 5) m", "(2x + 7) m and (2x + 2) m"],
                "answer": 0,
                "hint": "Factor area x² + 9x + 14 and check 2(Length + Width) equals 4x + 18!",
                "explanation": "(x + 7)(x + 2) gives area x² + 9x + 14 and perimeter 2(2x + 9) = 4x + 18.",
                "solution_steps": [
                    "Factor area polynomial x² + 9x + 14: 7 + 2 = 9 and 7 × 2 = 14 → (x + 7)(x + 2).",
                    "Verify half-perimeter constraint: (4x + 18)/2 = 2x + 9.",
                    "Sum of factored dimensions (x + 7) + (x + 2) = 2x + 9 matches!"
                ]
            },
            {
                "question": "Simplify (a³ − b³) / (a² − b²) cleanly for a ≠ ±b.",
                "options": ["(a² + ab + b²) / (a + b)", "(a² − ab + b²) / (a + b)", "(a − b) / (a + b)", "a − b"],
                "answer": 0,
                "hint": "Factor top using difference of cubes and bottom using difference of squares, then cancel (a − b)!",
                "explanation": "[(a − b)(a² + ab + b²)] / [(a − b)(a + b)] = (a² + ab + b²)/(a + b).",
                "solution_steps": [
                    "Factor numerator: a³ − b³ = (a − b)(a² + ab + b²).",
                    "Factor denominator: a² − b² = (a − b)(a + b).",
                    "Cancel common factor (a − b) ≠ 0 → (a² + ab + b²)/(a + b)."
                ]
            },
            {
                "question": "Verify Śhrīdharāchārya's identity (a + b)(a − b) + b² = a² by choosing b = 10 to compute 60².",
                "options": ["(70)(50) + 100 = 3600", "(70)(50) − 100 = 3400", "(60)(50) + 100 = 3100", "(70)(60) + 100 = 4300"],
                "answer": 0,
                "hint": "Substitute a = 60 and b = 10 into (a + b)(a − b) + b²!",
                "explanation": "(60 + 10)(60 − 10) + 10² = 70 × 50 + 100 = 3500 + 100 = 3600.",
                "solution_steps": [
                    "Plug a = 60 and b = 10 into Śhrīdharāchārya's identity a² = (a + b)(a − b) + b².",
                    "Evaluate product: (60 + 10)(60 − 10) = 70 × 50 = 3500.",
                    "Add b² = 10² = 100: 3500 + 100 = 3600 = 60²."
                ]
            }
        ]
    }
]

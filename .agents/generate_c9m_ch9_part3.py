#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 9: Propositions and their Converses
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Logic Basics Challenge",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Propositions, Implications, Alternative Phrasings & Converses",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which of the following sentences is a valid mathematical PROPOSITION?",
                "options": [
                    "\"19 is a composite number.\" (Unambiguously False)",
                    "\"Solve all ten problems in Exercise 9.1!\"",
                    "\"Why is 2 the only even prime?\"",
                    "\"2x − 1 = 9\" (with x unspecified)"
                ],
                "answer": 0,
                "hint": "A proposition must be a declarative statement that is strictly either True or False.",
                "solution_steps": [
                    "A proposition must be a declarative statement that is strictly either True or False.",
                    "\"19 is a composite number\" is unambiguously False (since 19 is prime), so it has a definite truth value.",
                    "Commands, questions, and open equations with unspecified variables are NOT propositions."
                ]
            },
            {
                "question": "Why is \"x + y = 10\" (without specifying x and y) NOT a proposition?",
                "options": [
                    "Its truth value depends on the values assigned to x and y, so it is neither strictly true nor strictly false",
                    "Because it uses two variables",
                    "Because 10 is an even number",
                    "Because addition cannot appear in propositions"
                ],
                "answer": 0,
                "hint": "An open sentence with free variables varies in truth value (e.g., True for x=4, y=6; False for x=1, y=2).",
                "explanation": "Therefore, an unspecified open equation is not a proposition.",
                "solution_steps": [
                    "An open sentence with free variables varies in truth value (e.g., True for x=4, y=6; False for x=1, y=2).",
                    "A formal proposition must carry one fixed truth value (True or False).",
                    "Therefore, an unspecified open equation is not a proposition."
                ]
            },
            {
                "question": "In \"If a quadrilateral is a rhombus, then all four sides are equal\", what is the CONCLUSION?",
                "options": [
                    "All four sides are equal",
                    "A quadrilateral is a rhombus",
                    "All four angles are 90°",
                    "It is a square"
                ],
                "answer": 0,
                "solution_steps": [
                    "Standard conditional form is \"If X, then Y\".",
                    "X (\"a quadrilateral is a rhombus\") is the premise/hypothesis.",
                    "Y (\"all four sides are equal\") following 'then' is the conclusion."
                ]
            },
            {
                "question": "What is the exact CONVERSE of \"If an integer ends in 5, then it is divisible by 5\"?",
                "options": [
                    "\"If an integer is divisible by 5, then it ends in 5.\"",
                    "\"If an integer does not end in 5, then it is not divisible by 5.\"",
                    "\"If an integer is not divisible by 5, then it does not end in 5.\"",
                    "\"Every integer ending in 5 is odd.\""
                ],
                "answer": 0,
                "solution_steps": [
                    "Identify X = \"an integer ends in 5\" and Y = \"it is divisible by 5\".",
                    "The converse flips X ⇒ Y into Y ⇒ X.",
                    "Result: \"If an integer is divisible by 5, then it ends in 5\" (note: this converse is False, e.g., 20)."
                ]
            },
            {
                "question": "Rewrite \"A natural number is even when its last digit is 4\" in standard \"If X, then Y\" form.",
                "options": [
                    "\"If a natural number's last digit is 4, then it is even.\"",
                    "\"If a natural number is even, then its last digit is 4.\"",
                    "\"If a natural number's last digit is not 4, it is odd.\"",
                    "\"A natural number is 4 only if it is even.\""
                ],
                "answer": 0,
                "solution_steps": [
                    "The alternative phrasing \"Y when X\" means \"If X, then Y\".",
                    "Here Y = \"a natural number is even\" and X = \"its last digit is 4\".",
                    "Standard form: \"If a natural number's last digit is 4, then it is even.\""
                ]
            },
            {
                "question": "What is the converse of \"All equilateral triangles are isosceles\"?",
                "options": [
                    "\"If a triangle is isosceles, then it is equilateral.\" (False — e.g., sides 5, 5, 8)",
                    "\"If a triangle is not equilateral, then it is not isosceles.\"",
                    "\"All isosceles triangles have three 60° angles.\"",
                    "\"If a triangle is equilateral, then it has two equal sides.\""
                ],
                "answer": 0,
                "solution_steps": [
                    "Translate \"All X are Y\" into \"If a triangle is equilateral, then it is isosceles\".",
                    "Swap X and Y to form the converse: \"If a triangle is isosceles, then it is equilateral.\"",
                    "A triangle with sides 5, 5, 8 is isosceles but not equilateral, proving the converse False."
                ]
            },
            {
                "question": "Under what exact condition is \"If X, then Y\" (X ⇒ Y) proven FALSE?",
                "options": [
                    "When there is at least one case where X is True and Y is False",
                    "When X is False and Y is True",
                    "When both X and Y are False",
                    "When X and Y are both True"
                ],
                "answer": 0,
                "solution_steps": [
                    "\"If X, then Y\" promises that whenever X holds, Y must also hold.",
                    "The promise is broken only when X is True while Y fails (is False).",
                    "Cases where X is False do not violate \"If X, then Y\"."
                ]
            },
            {
                "question": "Which English phrasing means the exact same thing as \"If X, then Y\"?",
                "options": [
                    "\"X implies Y\" (or \"Y when X\")",
                    "\"If Y, then X\"",
                    "\"Y implies X\"",
                    "\"Not X implies not Y\""
                ],
                "answer": 0,
                "solution_steps": [
                    "\"If X, then Y\", \"X implies Y\", \"Y when X\", and \"X only if Y\" all express X ⇒ Y.",
                    "\"If Y, then X\" and \"Y implies X\" are the converse (Y ⇒ X).",
                    "Therefore \"X implies Y\" / \"Y when X\" matches X ⇒ Y."
                ]
            },
            {
                "question": "Is \"If a prime number is greater than 2, then it is odd\" true, and is its converse true?",
                "options": [
                    "Forward proposition is TRUE; Converse (\"If an odd number is > 2, then it is prime\") is FALSE (counterexample: 9)",
                    "Both are TRUE",
                    "Forward is FALSE, Converse is TRUE",
                    "Both are FALSE"
                ],
                "answer": 0,
                "hint": "Every prime > 2 cannot be divisible by 2, so it must be odd (Forward: True).",
                "solution_steps": [
                    "Every prime > 2 cannot be divisible by 2, so it must be odd (Forward: True).",
                    "Converse: \"If an odd number is greater than 2, then it is prime.\"",
                    "Counterexample: 9 (or 15, 21, 25) is odd and > 2, yet composite, so Converse is False."
                ]
            },
            {
                "question": "How many counterexamples are needed to disprove \"Every odd number greater than 1 is prime\"?",
                "options": [
                    "Just ONE counterexample (e.g., 9 = 3 × 3)",
                    "At least 5 counterexamples",
                    "Infinitely many counterexamples",
                    "None — it is true"
                ],
                "answer": 0,
                "hint": "A universal statement claims zero exceptions exist.",
                "explanation": "One single valid counterexample conclusively disproves the claim.",
                "solution_steps": [
                    "A universal statement claims zero exceptions exist.",
                    "9 is odd and > 1, yet 9 = 3 × 3 is composite.",
                    "One single valid counterexample conclusively disproves the claim."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Examples Converse Challenge",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Rain, Multiples, Squares/Factors, Area & Baudhāyana-Pythagoras",
        "is_quiz": True,
        "questions": [
            {
                "question": "In Example 1, \"If it rains, then the road is wet\" is True. Which is a valid counterexample to its converse?",
                "options": [
                    "A municipal water tanker spills water on the road on a sunny dry day",
                    "Heavy rain falls and the road gets wet",
                    "It does not rain and the road stays dry",
                    "Rain falls inside a covered tunnel while the tunnel floor stays dry"
                ],
                "answer": 0,
                "solution_steps": [
                    "The converse is \"If the road is wet, then it has rained.\"",
                    "We need a case where \"the road is wet\" is True and \"it has rained\" is False.",
                    "A water tanker spill on a dry day satisfies both conditions, disproving the converse."
                ]
            },
            {
                "question": "Which integer is a counterexample to \"If a number is a multiple of 4, then it is a multiple of 8\"?",
                "options": ["12", "16", "24", "10"],
                "answer": 0,
                "hint": "Premise: number is a multiple of 4. Conclusion: number is a multiple of 8.",
                "explanation": "16 and 24 are multiples of 8; 10 is not a multiple of 4.",
                "solution_steps": [
                    "Premise: number is a multiple of 4. Conclusion: number is a multiple of 8.",
                    "12 = 4 × 3 is a multiple of 4, but 12 ÷ 8 leaves remainder 4 (not a multiple of 8).",
                    "16 and 24 are multiples of 8; 10 is not a multiple of 4."
                ]
            },
            {
                "question": "Why does EVERY perfect square N = k² have an ODD number of positive factors?",
                "options": [
                    "Every factor d ≠ k pairs with a distinct partner N/d, while k pairs with itself (contributing 1 solo factor)",
                    "Because all perfect squares are odd numbers",
                    "Because perfect squares only have 3 factors",
                    "Because 1 is not a factor of non-squares"
                ],
                "answer": 0,
                "hint": "Positive factors of N pair via {d, N/d}.",
                "explanation": "Only when N = k² does d = k = N/k pair with itself, adding 1 solo factor to make the total odd.",
                "solution_steps": [
                    "Positive factors of N pair via {d, N/d}.",
                    "Whenever d ≠ N/d, each pair adds 2 factors (even total).",
                    "Only when N = k² does d = k = N/k pair with itself, adding 1 solo factor to make the total odd."
                ]
            },
            {
                "question": "How many positive factors does 100 (= 10²) have?",
                "options": [
                    "9 factors (1, 2, 4, 5, 10, 20, 25, 50, 100) — an ODD count",
                    "8 factors — an even count",
                    "10 factors",
                    "5 factors"
                ],
                "answer": 0,
                "hint": "List factor pairs of 100: {1, 100}, {2, 50}, {4, 25}, {5, 20}, plus solo {10}.",
                "explanation": "Since 9 is odd, this confirms Example 3 for N = 100.",
                "solution_steps": [
                    "List factor pairs of 100: {1, 100}, {2, 50}, {4, 25}, {5, 20}, plus solo {10}.",
                    "Total count = 4 × 2 + 1 = 9 factors.",
                    "Since 9 is odd, this confirms Example 3 for N = 100."
                ]
            },
            {
                "question": "If a positive integer N has exactly 5 positive factors, what MUST be true about N?",
                "options": [
                    "N must be a perfect square (specifically p⁴ for some prime p, e.g., 16 = 2⁴)",
                    "N cannot be a perfect square",
                    "N must be a prime number",
                    "N must be odd"
                ],
                "answer": 0,
                "hint": "5 is an odd number of positive factors.",
                "explanation": "For example, 16 = 4² has 5 factors: 1, 2, 4, 8, 16.",
                "solution_steps": [
                    "5 is an odd number of positive factors.",
                    "By the converse of Example 3, any integer with an odd factor count is a perfect square.",
                    "For example, 16 = 4² has 5 factors: 1, 2, 4, 8, 16."
                ]
            },
            {
                "question": "Which pair of triangles proves that \"Equal area ⇒ Congruent\" is FALSE?",
                "options": [
                    "Triangle with base 8 cm, height 3 cm (Area 12 cm²) and triangle with base 6 cm, height 4 cm (Area 12 cm²)",
                    "Two triangles both having sides 5 cm, 12 cm, 13 cm",
                    "Two congruent equilateral triangles of side 4 cm",
                    "A triangle of area 10 cm² and one of area 15 cm²"
                ],
                "answer": 0,
                "hint": "Both triangles have area ½ × 8 × 3 = 12 cm² and ½ × 6 × 4 = 12 cm².",
                "explanation": "Hence equal area does NOT imply congruence.",
                "solution_steps": [
                    "Both triangles have area ½ × 8 × 3 = 12 cm² and ½ × 6 × 4 = 12 cm².",
                    "Their base and height combinations (and side lengths) differ, so they cannot be superimposed.",
                    "Hence equal area does NOT imply congruence."
                ]
            },
            {
                "question": "In Example 5 (Converse of Baudhāyana-Pythagoras Theorem), why do we construct an auxiliary right triangle PQR with legs a and b?",
                "options": [
                    "So the forward theorem gives PQ = √(a² + b²) = c, allowing SSS congruence △ABC ≅ △PQR to prove ∠C = ∠R = 90°",
                    "Because △ABC already has ∠C = 90° given",
                    "To prove △ABC is equilateral",
                    "Because SSS only works on right triangles"
                ],
                "answer": 0,
                "hint": "We are given a² + b² = c² in △ABC, and want to prove ∠C = 90°.",
                "explanation": "Then △ABC ≅ △PQR by SSS (sides a, b, c), forcing ∠C = ∠R = 90°.",
                "solution_steps": [
                    "We are given a² + b² = c² in △ABC, and want to prove ∠C = 90°.",
                    "Construct right △PQR with ∠R = 90°, QR = a, PR = b; by forward Pythagoras, PQ = √(a² + b²) = c.",
                    "Then △ABC ≅ △PQR by SSS (sides a, b, c), forcing ∠C = ∠R = 90°."
                ]
            },
            {
                "question": "Which side-length triple forms a right-angled triangle by the converse of the Baudhāyana-Pythagoras theorem?",
                "options": ["8 cm, 15 cm, 17 cm", "5 cm, 6 cm, 8 cm", "7 cm, 10 cm, 12 cm", "4 cm, 5 cm, 6 cm"],
                "answer": 0,
                "hint": "Check a² + b² = c² for the largest side c = 17:",
                "explanation": "Since 8² + 15² = 17², the triangle is right-angled opposite the 17 cm side.",
                "solution_steps": [
                    "Check a² + b² = c² for the largest side c = 17:",
                    "8² + 15² = 64 + 225 = 289, and 17² = 289.",
                    "Since 8² + 15² = 17², the triangle is right-angled opposite the 17 cm side."
                ]
            },
            {
                "question": "If two triangles are congruent, must they have equal perimeters? And is its converse true?",
                "options": [
                    "Forward is TRUE; Converse (\"Equal perimeter ⇒ Congruent\") is FALSE (e.g., 4-4-4 vs 3-4-5, both perimeter 12)",
                    "Both are TRUE",
                    "Forward is FALSE, Converse is TRUE",
                    "Both are FALSE"
                ],
                "answer": 0,
                "hint": "Congruent triangles have identical side lengths, so their perimeters are equal (Forward: True).",
                "explanation": "Therefore, the converse is False.",
                "solution_steps": [
                    "Congruent triangles have identical side lengths, so their perimeters are equal (Forward: True).",
                    "Take equilateral (4, 4, 4) and right (3, 4, 5): both have perimeter 12, yet are not congruent.",
                    "Therefore, the converse is False."
                ]
            },
            {
                "question": "Which pair from Section 9.2 has BOTH the proposition AND its converse TRUE?",
                "options": [
                    "\"N is a perfect square\" ⇔ \"N has an odd number of positive factors\"",
                    "\"It rains\" ⇒ \"The road is wet\"",
                    "\"Number is a multiple of 6\" ⇒ \"Number is a multiple of 3\"",
                    "\"Two triangles are congruent\" ⇒ \"Two triangles have equal area\""
                ],
                "answer": 0,
                "hint": "Example 1 (Rain/Wet road), Example 2 (6/3), and Example 4 (Congruence/Area) all have False converses.",
                "explanation": "Hence Perfect Square ↔ Odd factor count is the biconditional pair.",
                "solution_steps": [
                    "Example 1 (Rain/Wet road), Example 2 (6/3), and Example 4 (Congruence/Area) all have False converses.",
                    "Example 3 (Perfect square ↔ Odd factor count) and Example 5 (Baudhāyana-Pythagoras) hold in both directions.",
                    "Hence Perfect Square ↔ Odd factor count is the biconditional pair."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Geometry Algebra Challenge",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Transversals, Quadrilaterals, Incentres, Squaring & Cubing",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which statement and its converse are BOTH true for two coplanar lines cut by a transversal?",
                "options": [
                    "\"If the lines are parallel, then alternate interior angles are equal\" and its converse",
                    "\"If lines are perpendicular, then corresponding angles are supplementary\"",
                    "\"If lines intersect, then all angles are 90°\"",
                    "\"If co-interior angles are equal, then lines are parallel\""
                ],
                "answer": 0,
                "hint": "Parallel lines ⇒ equal alternate interior angles (True).",
                "explanation": "Note: co-interior angles sum to 180° (supplementary), not necessarily equal.",
                "solution_steps": [
                    "Parallel lines ⇒ equal alternate interior angles (True).",
                    "Conversely, equal alternate interior angles ⇒ parallel lines (True).",
                    "Note: co-interior angles sum to 180° (supplementary), not necessarily equal."
                ]
            },
            {
                "question": "Test: \"If a quadrilateral is a rectangle, then its diagonals are equal.\" Is its converse true?",
                "options": [
                    "No — an isosceles trapezium (non-rectangle) also has equal diagonals",
                    "Yes — only rectangles have equal diagonals",
                    "No — rectangles do not have equal diagonals",
                    "Yes — by SSS congruence"
                ],
                "answer": 0,
                "hint": "Forward: Every rectangle has congruent diagonals (True).",
                "solution_steps": [
                    "Forward: Every rectangle has congruent diagonals (True).",
                    "Converse: \"If diagonals are equal, it is a rectangle.\"",
                    "Counterexample: An isosceles trapezium (bases 4 and 8, equal legs) has equal diagonals but is not a rectangle."
                ]
            },
            {
                "question": "What is the converse of \"If a quadrilateral is a square, then its diagonals are equal and bisect each other at 90°\"?",
                "options": [
                    "\"If the diagonals of a quadrilateral are equal and bisect each other at 90°, then it is a square.\" (TRUE!)",
                    "\"If diagonals are not equal, it is a rhombus.\" (False)",
                    "\"If diagonals bisect at 90°, it is a kite.\" (True)",
                    "\"If a quadrilateral is a rectangle, its diagonals are perpendicular.\" (False)"
                ],
                "answer": 0,
                "hint": "Swap premise (square) and conclusion (diagonals equal AND bisect each other at 90°).",
                "explanation": "Hence this full converse is TRUE!",
                "solution_steps": [
                    "Swap premise (square) and conclusion (diagonals equal AND bisect each other at 90°).",
                    "Bisecting ⇒ parallelogram; perpendicular ⇒ rhombus; equal ⇒ rectangle; rhombus + rectangle = square.",
                    "Hence this full converse is TRUE!"
                ]
            },
            {
                "question": "Two sticks of lengths 10 cm and 6 cm are pinned at their exact midpoints. What shape do their 4 endpoints form?",
                "options": [
                    "A non-rectangle parallelogram (or rhombus if pinned at 90°)",
                    "Always a square",
                    "Always a rectangle",
                    "A trapezium with only one pair of parallel sides"
                ],
                "answer": 0,
                "hint": "Pinned at midpoints ⇒ diagonals bisect each other ⇒ parallelogram.",
                "explanation": "Thus it forms a non-rectangle parallelogram (a rhombus if the angle is 90°).",
                "solution_steps": [
                    "Pinned at midpoints ⇒ diagonals bisect each other ⇒ parallelogram.",
                    "Since 10 cm ≠ 6 cm, the diagonals are unequal, so it cannot be a rectangle or square.",
                    "Thus it forms a non-rectangle parallelogram (a rhombus if the angle is 90°)."
                ]
            },
            {
                "question": "Why do all three internal angle bisectors of any triangle pass through one common point (the incentre)?",
                "options": [
                    "The intersection I of two bisectors is equidistant from all three sides, so by the converse bisector theorem I also lies on the third bisector",
                    "Because all triangles are equilateral",
                    "Because angle bisectors are always perpendicular to the opposite sides",
                    "Because the incentre is always the midpoint of the longest side"
                ],
                "answer": 0,
                "hint": "Let I be the intersection of the bisectors of ∠A and ∠B.",
                "explanation": "By the converse of the angle bisector theorem, I must lie on the bisector of ∠C as well.",
                "solution_steps": [
                    "Let I be the intersection of the bisectors of ∠A and ∠B.",
                    "Distance(I, AB) = Distance(I, AC) and Distance(I, AB) = Distance(I, BC) ⇒ Distance(I, AC) = Distance(I, BC).",
                    "By the converse of the angle bisector theorem, I must lie on the bisector of ∠C as well."
                ]
            },
            {
                "question": "For real numbers x and y, which implication pair is TRUE in BOTH directions?",
                "options": [
                    "x = y ⇔ x³ = y³",
                    "x = y ⇔ x² = y²",
                    "x > 0 ⇔ x² > 0",
                    "x > y ⇔ x² > y²"
                ],
                "answer": 0,
                "hint": "x² = y² fails for (3, −3); x² > 0 fails at x = −2; x > y ⇒ x² > y² fails for (−1, −5).",
                "explanation": "Hence x = y ⇔ x³ = y³ holds in both directions.",
                "solution_steps": [
                    "x² = y² fails for (3, −3); x² > 0 fails at x = −2; x > y ⇒ x² > y² fails for (−1, −5).",
                    "Over ℝ, x³ = y³ implies x = y because odd powers preserve sign and are strictly increasing.",
                    "Hence x = y ⇔ x³ = y³ holds in both directions."
                ]
            },
            {
                "question": "Give a counterexample to \"If x > y, then x² > y²\" for real numbers x, y.",
                "options": [
                    "x = −1, y = −4 (since −1 > −4, yet (−1)² = 1 < 16 = (−4)²)",
                    "x = 5, y = 2",
                    "x = 3, y = 0",
                    "x = 2, y = 3"
                ],
                "answer": 0,
                "hint": "We need x > y (premise True) and x² ≤ y² (conclusion False).",
                "explanation": "Thus (−1, −4) disproves the claim.",
                "solution_steps": [
                    "We need x > y (premise True) and x² ≤ y² (conclusion False).",
                    "Take x = −1, y = −4: −1 > −4 is True, while 1 > 16 is False.",
                    "Thus (−1, −4) disproves the claim."
                ]
            },
            {
                "question": "Test: \"If ab = 0, then a = 0 and b = 0.\" Is this proposition true?",
                "options": [
                    "False — counterexample: a = 0, b = 7 gives ab = 0 even though b ≠ 0",
                    "True — both must be zero",
                    "True — because 0 has no factors",
                    "False — because 0 × 0 = 1"
                ],
                "answer": 0,
                "hint": "ab = 0 means at least one of a or b is 0 (a = 0 OR b = 0), not necessarily both.",
                "explanation": "Note that its converse (a = 0 and b = 0 ⇒ ab = 0) IS true.",
                "solution_steps": [
                    "ab = 0 means at least one of a or b is 0 (a = 0 OR b = 0), not necessarily both.",
                    "Take a = 0, b = 7: premise ab = 0 holds, conclusion 'a = 0 and b = 0' fails.",
                    "Note that its converse (a = 0 and b = 0 ⇒ ab = 0) IS true."
                ]
            },
            {
                "question": "In △ABC, \"If AB = AC, then ∠B = ∠C\" is True. What is its converse, and is it true?",
                "options": [
                    "\"If ∠B = ∠C, then AB = AC\" — TRUE (angles opposite equal sides / sides opposite equal angles)",
                    "\"If ∠B ≠ ∠C, then AB ≠ AC\" — False",
                    "\"If AB = BC, then ∠A = ∠B\" — False",
                    "\"If ∠B = ∠C, then AB = AC\" — False"
                ],
                "answer": 0,
                "hint": "Swap premise (AB = AC) and conclusion (∠B = ∠C).",
                "solution_steps": [
                    "Swap premise (AB = AC) and conclusion (∠B = ∠C).",
                    "Converse: \"If ∠B = ∠C, then AB = AC.\"",
                    "By ASA/AAS congruence via the bisector of ∠A, this converse is TRUE."
                ]
            },
            {
                "question": "If a triangle has side lengths satisfying a² + b² > c² (where c is the longest side), is it right-angled?",
                "options": [
                    "No — it is acute-angled; only a² + b² = c² gives a right angle",
                    "Yes — it is always right-angled",
                    "It is obtuse-angled",
                    "It cannot form a triangle"
                ],
                "answer": 0,
                "hint": "By the Baudhāyana-Pythagoras theorem & converse, ∠C = 90° if and only if a² + b² = c².",
                "explanation": "When a² + b² < c², ∠C > 90° (obtuse).",
                "solution_steps": [
                    "By the Baudhāyana-Pythagoras theorem & converse, ∠C = 90° if and only if a² + b² = c².",
                    "When a² + b² > c² (e.g., 5, 5, 5), ∠C < 90°, making the triangle acute.",
                    "When a² + b² < c², ∠C > 90° (obtuse)."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Number Theory Mastery",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): Divisibility (24, 60, 8, 3), Euler F₅ & Prime Formula Counterexamples",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which integer disproves \"If a number is divisible by both 4 and 6, then it is divisible by 24\"?",
                "options": ["12", "24", "48", "18"],
                "answer": 0,
                "hint": "12 is divisible by 4 (4 × 3) AND by 6 (6 × 2), so the premise is True.",
                "explanation": "Therefore 12 is a valid counterexample.",
                "solution_steps": [
                    "12 is divisible by 4 (4 × 3) AND by 6 (6 × 2), so the premise is True.",
                    "However, 12 is NOT divisible by 24 (since LCM(4, 6) = 12, not 24).",
                    "Therefore 12 is a valid counterexample."
                ]
            },
            {
                "question": "Test: \"If d is a factor of 60, then d is a factor of 120.\" What about its converse?",
                "options": [
                    "Forward is TRUE; Converse is FALSE (counterexamples: 8, 24, 40, 120 divide 120 but NOT 60)",
                    "Both are TRUE",
                    "Forward is FALSE, Converse is TRUE",
                    "Both are FALSE"
                ],
                "answer": 0,
                "hint": "Since 120 = 2 × 60, every factor of 60 automatically divides 120 (Forward: True).",
                "explanation": "Hence the converse is False.",
                "solution_steps": [
                    "Since 120 = 2 × 60, every factor of 60 automatically divides 120 (Forward: True).",
                    "For the converse, take d = 40 (or 24, or 8): 40 divides 120 (120 = 3 × 40), but 40 does not divide 60.",
                    "Hence the converse is False."
                ]
            },
            {
                "question": "Which digit-sum statement is TRUE in BOTH forward and converse directions?",
                "options": [
                    "\"If a number is divisible by 3, its digit sum is divisible by 3\"",
                    "\"If a number is divisible by 4, its digit sum is divisible by 4\"",
                    "\"If a number is divisible by 6, its digit sum is divisible by 6\"",
                    "\"If a number is divisible by 8, its last digit is 8\""
                ],
                "answer": 0,
                "hint": "Every power of 10 leaves remainder 1 mod 3, so a number ≡ its digit sum (mod 3).",
                "explanation": "Divisibility by 4, 6, or 8 does not follow digit-sum rules (e.g., 13 has sum 4, not divisible by 4).",
                "solution_steps": [
                    "Every power of 10 leaves remainder 1 mod 3, so a number ≡ its digit sum (mod 3).",
                    "Thus divisibility by 3 holds if and only if the digit sum is divisible by 3.",
                    "Divisibility by 4, 6, or 8 does not follow digit-sum rules (e.g., 13 has sum 4, not divisible by 4)."
                ]
            },
            {
                "question": "For Fermat numbers Fₙ = 2^(2^n) + 1, which index n first gave a composite counterexample (found by Euler in 1732)?",
                "options": [
                    "n = 5 (F₅ = 2³² + 1 = 641 × 6,700,417)",
                    "n = 2 (F₂ = 17)",
                    "n = 3 (F₃ = 257)",
                    "n = 4 (F₄ = 65,537)"
                ],
                "answer": 0,
                "hint": "F₀ = 3, F₁ = 5, F₂ = 17, F₃ = 257, F₄ = 65,537 are all prime.",
                "explanation": "This single counterexample disproved Fermat's conjecture.",
                "solution_steps": [
                    "F₀ = 3, F₁ = 5, F₂ = 17, F₃ = 257, F₄ = 65,537 are all prime.",
                    "At n = 5, Euler factored F₅ = 4,294,967,297 = 641 × 6,700,417.",
                    "This single counterexample disproved Fermat's conjecture."
                ]
            },
            {
                "question": "Which natural number n ≥ 1 is the smallest counterexample showing \"n² + n + 11 is always prime\" is FALSE?",
                "options": [
                    "n = 10 (gives 10² + 10 + 11 = 121 = 11 × 11, composite)",
                    "n = 1 (gives 13, prime)",
                    "n = 5 (gives 41, prime)",
                    "n = 9 (gives 101, prime)"
                ],
                "answer": 0,
                "hint": "For n = 1..9, n² + n + 11 yields primes: 13, 17, 23, 31, 41, 53, 67, 83, 101.",
                "explanation": "Thus n = 10 is the smallest natural-number counterexample.",
                "solution_steps": [
                    "For n = 1..9, n² + n + 11 yields primes: 13, 17, 23, 31, 41, 53, 67, 83, 101.",
                    "At n = 10: 100 + 10 + 11 = 121 = 11².",
                    "Thus n = 10 is the smallest natural-number counterexample."
                ]
            },
            {
                "question": "Which n ≥ 1 disproves \"4ⁿ + 3 is prime for every natural number n\"?",
                "options": [
                    "n = 4 (gives 4⁴ + 3 = 256 + 3 = 259 = 7 × 37, composite)",
                    "n = 1 (gives 7, prime)",
                    "n = 2 (gives 19, prime)",
                    "n = 3 (gives 67, prime)"
                ],
                "answer": 0,
                "hint": "Check n = 1: 7 (prime); n = 2: 19 (prime); n = 3: 67 (prime).",
                "explanation": "Since 259 = 7 × 37, n = 4 is the smallest counterexample.",
                "solution_steps": [
                    "Check n = 1: 7 (prime); n = 2: 19 (prime); n = 3: 67 (prime).",
                    "At n = 4: 4⁴ + 3 = 256 + 3 = 259.",
                    "Since 259 = 7 × 37, n = 4 is the smallest counterexample."
                ]
            },
            {
                "question": "For Mersenne-style numbers 2ⁿ − 1 (n ≥ 2), which value of n gives a composite number?",
                "options": [
                    "n = 4 (gives 2⁴ − 1 = 15 = 3 × 5, composite)",
                    "n = 2 (gives 3, prime)",
                    "n = 3 (gives 7, prime)",
                    "n = 5 (gives 31, prime)"
                ],
                "answer": 0,
                "hint": "2² − 1 = 3, 2³ − 1 = 7, and 2⁵ − 1 = 31 are all prime.",
                "explanation": "In fact, whenever n is composite, 2ⁿ − 1 is always composite.",
                "solution_steps": [
                    "2² − 1 = 3, 2³ − 1 = 7, and 2⁵ − 1 = 31 are all prime.",
                    "At n = 4: 2⁴ − 1 = 16 − 1 = 15 = 3 × 5 (composite).",
                    "In fact, whenever n is composite, 2ⁿ − 1 is always composite."
                ]
            },
            {
                "question": "Which of the following is a counterexample to \"If n is prime, then 2ⁿ − 1 is prime\"?",
                "options": [
                    "n = 11 (11 is prime, yet 2¹¹ − 1 = 2047 = 23 × 89 is composite!)",
                    "n = 2 (2² − 1 = 3, prime)",
                    "n = 3 (2³ − 1 = 7, prime)",
                    "n = 7 (2⁷ − 1 = 127, prime)"
                ],
                "answer": 0,
                "hint": "For primes n = 2, 3, 5, 7, 2ⁿ − 1 gives primes 3, 7, 31, 127.",
                "explanation": "So n = 11 disproves even the restricted prime-exponent claim!",
                "solution_steps": [
                    "For primes n = 2, 3, 5, 7, 2ⁿ − 1 gives primes 3, 7, 31, 127.",
                    "At the next prime n = 11, 2¹¹ − 1 = 2047 = 23 × 89.",
                    "So n = 11 disproves even the restricted prime-exponent claim!"
                ]
            },
            {
                "question": "Can BOTH a proposition \"If P, then Q\" AND its converse \"If Q, then P\" be FALSE?",
                "options": [
                    "Yes — e.g., \"If a number is odd, then it is prime\" (False: 9) and \"If a number is prime, then it is odd\" (False: 2)",
                    "No — at least one must always be true",
                    "Only if P and Q are identical",
                    "Never in mathematics"
                ],
                "answer": 0,
                "solution_steps": [
                    "\"Odd ⇒ Prime\" fails at 9 (odd, composite).",
                    "\"Prime ⇒ Odd\" fails at 2 (prime, even).",
                    "Thus both a proposition and its converse can be False simultaneously."
                ]
            },
            {
                "question": "Which statement best summarizes the core lesson of Chapter 9 (Propositions and their Converses)?",
                "options": [
                    "A proposition has a definite True/False value; its converse swaps premise and conclusion and must be tested independently—with one counterexample sufficient to disprove a false claim",
                    "Every true theorem automatically has a true converse",
                    "Examples that work 5 times prove a formula works forever",
                    "Open equations like x + 2 = 5 are propositions"
                ],
                "answer": 0,
                "hint": "Propositions must be strictly True or False.",
                "explanation": "One counterexample disproves any false universal proposition.",
                "solution_steps": [
                    "Propositions must be strictly True or False.",
                    "Flipping X ⇒ Y to Y ⇒ X creates the converse, whose truth is logically independent.",
                    "One counterexample disproves any false universal proposition."
                ]
            }
        ]
    }
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("explanation", _q["solution_steps"][-1])
        _q.setdefault("hint", _q["solution_steps"][0])

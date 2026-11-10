#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 4: Quadratic Equations
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (John, Jivanti, Rohan, Raghav, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Triangle And Pottery",
        "subtitle": "Applied Exercise 4.2 Word Problems: Right-Triangle Pythagoras & Cottage Pottery Costs",
        "speech": (
            "Now put factorization cleanly to work solving two beloved real-world puzzles from Exercise Four Point Two! Puzzle One involves geometry: the altitude of a right-angled triangle measures 7 cm less than its base, "
            "while its diagonal hypotenuse equals 13 cm! Let base equal x cm; then altitude equals (x minus 7) cm! Remember Pythagoras' Theorem: base squared plus altitude squared equals hypotenuse squared! Write x squared plus (x minus 7) whole squared "
            "equals 13 squared (169)! Expanding neatly gives 2x squared minus 14x plus 49 equals 169; subtracting 169 and dividing smoothly by 2 unlocks crisp quadratic x squared minus 7x minus 60 equals zero! Factoring (x minus 12)(x plus 5) equals zero "
            "yields x equals 12 or minus 5! Since geometric side lengths CANNOT be negative, reject minus 5 immediately—giving base 12 cm and altitude 5 cm (the famous 5-12-13 right triangle)! Puzzle Two explores a pottery workshop creating x daily pots "
            "where each pot costs (2x plus 3) rupees and daily total production equals 90 rupees: x(2x plus 3) equals 90 solves cleanly to 6 pottery articles costing 15 rupees each—always verifying physical positivity and valid whole number sense after factoring quadratic brackets cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In Exercise 4.2 Q5, a right triangle has base x, altitude x − 7, and hypotenuse 13 cm. Why is negative root x = −5 discarded after solving (x − 12)(x + 5) = 0?",
                "options": [
                    "Geometric side length of a physical triangle must be strictly positive, leaving valid base 12 cm and altitude 5 cm",
                    "Because 13 − 5 = 8",
                    "Because 5 is a prime number",
                    "Because x = −5 creates hypotenuse 169"
                ],
                "answer": 0,
                "hint": "Can a real wooden or chalk triangle ever measure −5 cm wide?",
                "explanation": "Physical lengths cannot be negative, so x = −5 is rejected and valid positive base x = 12 cm (altitude 5 cm) is kept."
            },
            {
                "question": "A pottery workshop produces x articles in a day; each article's cost (in ₹) is 3 more than twice the number of articles, with total cost ₹90 (Ex 4.2 Q6). Solve 2x² + 3x − 90 = 0:",
                "options": [
                    "6 articles produced at ₹15 each",
                    "15 articles produced at ₹6 each",
                    "5 articles produced at ₹18 each",
                    "9 articles produced at ₹10 each"
                ],
                "answer": 0,
                "hint": "Factor (2x + 15)(x − 6) = 0 and check positive integer article count x!",
                "explanation": "x = 6 articles (discarding negative −15/2), giving unit cost 2(6) + 3 = ₹15 (check: 6 × 15 = ₹90)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Sridharacharya Quadratic Formula",
        "subtitle": "Solving Any Quadratic ax² + bx + c = 0 Directly via Sridharacharya's Formula",
        "speech": (
            "What happens whenever an authentic quadratic equation refuses easy mental middle-term splitting—for example 2x squared minus 7x plus 3 equals zero, OR messy roots like 2 plus minus root 3? Instead of guessing factors fruitlessly, "
            "Indian mathematician Sridharacharya gifted humanity an unstoppable master key—the QUADRATIC FORMULA! For ANY standard quadratic a x squared plus b x plus c equals zero (with nonzero a), if b squared minus 4 a c is zero or positive, "
            "its exact real roots stand immediately given by: x equals [minus b plus-or-minus square root of (b squared minus 4 a c)] divided completely by 2a! Look carefully at EVERY symbol inside that fraction bar: first, watch minus b closely—if b is already negative, "
            "say minus 7, then minus b becomes PLUS 7! Second, notice the ENTIRE numerator minus b plus-or-minus the square root gets divided by 2a—never divide only the radical! Test live on 2x squared minus 7x plus 3 equals zero: "
            "here a equals 2, b equals minus 7, c equals 3! Inside the square root sits 49 minus 24 equals 25 (root 5); hence (7 plus 5)/4 gives 3, and (7 minus 5) over 4 simplifies smoothly to 1 half cleanly!"
        ),
        "checkpoints": [
            {
                "question": "State Sridharacharya's Quadratic Formula cleanly for solving ax² + bx + c = 0 (a ≠ 0, b² − 4ac ≥ 0):",
                "options": [
                    "x = [ −b ± √(b² − 4ac) ] / (2a)",
                    "x = −b ± √(b² − 4ac) / (2a)",
                    "x = [ b ± √(b² + 4ac) ] / (2a)",
                    "x = [ −b ± √(b² − 2ac) ] / a"
                ],
                "answer": 0,
                "hint": "The entire numerator −b ± √(b² − 4ac) sits over denominator 2a!",
                "explanation": "Sridharacharya's Quadratic Formula is x = (−b ± √(b² − 4ac)) / (2a)."
            },
            {
                "question": "Use the Quadratic Formula on x² − 4x + 1 = 0 (a = 1, b = −4, c = 1) to find its exact irrational roots:",
                "options": [
                    "2 + √3  and  2 − √3",
                    "4 + √12  and  4 − √12",
                    "−2 + √3  and  −2 − √3",
                    "2 + √5  and  2 − √5"
                ],
                "answer": 0,
                "hint": "Compute b² − 4ac = 16 − 4 = 12 = 4×3, so √12 = 2√3, then divide cleanly by 2a = 2!",
                "explanation": "x = (4 ± √12)/2 = (4 ± 2√3)/2 = 2 ± √3."
            }
        ]
    },
    {
        "id": 11,
        "title": "Discriminant D Value",
        "subtitle": "Understanding D = b² − 4ac Inside the Radical as the Root-Nature Decider (Sec 4.4)",
        "speech": (
            "Zoom sharply inside Sridharacharya's Quadratic Formula onto that crucial algebraic expression locked beneath the square-root roof: b squared minus 4 a c! Because this single number DISCRIMINATES completely "
            "between distinct real roots, equal coincident roots, and impossible non-real roots, mathematicians honor it with the capital symbol D—the DISCRIMINANT: D equals b squared minus 4 a c! "
            "Think logically about WHY real-number arithmetic reacts so dramatically to the sign of D inside square root of D! Case A: Whenever D is STRICTLY POSITIVE (D greater than zero), square root of D produces a clear positive real value, "
            "so adding root D gives one root while subtracting root D gives a SECOND distinct root! Case B: Whenever D equals EXACTLY ZERO (D equals zero), square root of zero collapses to zero, forcing plus 0 and minus 0 to return the IDENTICAL fraction minus b over 2a twice—two EQUAL real roots! "
            "Case C: Whenever D turns NEGATIVE (D less than zero), no real number squared ever gives negative D, so square root of D holds ZERO real values—meaning ZERO REAL ROOTS exist anywhere along the continuous real number line! Thus checking D first predicts instantly what kind of roots exist!"
        ),
        "checkpoints": [
            {
                "question": "What exact expression defines the Discriminant D of quadratic equation ax² + bx + c = 0 (a ≠ 0)?",
                "options": [
                    "D = b² − 4ac",
                    "D = b² + 4ac",
                    "D = √(b² − 4ac)",
                    "D = −b / (2a)"
                ],
                "answer": 0,
                "hint": "D is the quantity sitting INSIDE (without the square root symbol)!",
                "explanation": "Discriminant D = b² − 4ac; its sign (> 0, = 0, or < 0) determines whether √D is positive real, zero, or non-real."
            },
            {
                "question": "Compute discriminant D for 3x² − 2x + 1/3 = 0 (Textbook Example 9) and state what it predicts:",
                "options": [
                    "D = (−2)² − 4(3)(1/3) = 4 − 4 = 0  ⟹  two equal real roots (1/3 and 1/3)",
                    "D = 8 > 0  ⟹  two distinct real roots",
                    "D = −4 < 0  ⟹  no real roots",
                    "D = 4 > 0  ⟹  two distinct roots"
                ],
                "answer": 0,
                "hint": "Evaluate a = 3, b = −2, c = 1/3 inside b² − 4ac carefully!",
                "explanation": "D = 4 − 4(3)(1/3) = 4 − 4 = 0, predicting two equal real roots x = −b/(2a) = 2/6 = 1/3."
            }
        ]
    },
    {
        "id": 12,
        "title": "Three Root Cases",
        "subtitle": "Connecting Discriminant D > 0, D = 0, D < 0 to Roots and Parabola x-Intercepts",
        "speech": (
            "Now connect Chapter Two's parabola curves seamlessly right into Chapter Four's Discriminant D! Remember our three graphical parabola pictures from earlier? They match the three discriminant cases ONE-TO-ONE with crystal precision! "
            "First, when D is POSITIVE (b squared minus 4 a c greater than zero), e.g., 2x squared minus 3x minus 5 equals zero (D equals 9 plus 40 equals 49), the equation yields TWO DISTINCT real roots, matching a Case One parabola slashing the x-axis twice! "
            "Second, when D equals ZERO (b squared minus 4 a c equals zero), e.g., 4x squared minus 12x plus 9 equals zero (D equals 144 minus 144 equals zero), both roots fuse into TWO EQUAL real roots minus b over 2a (here 3/2, 3/2), matching a Case Two parabola grazing tangent once! "
            "Third, when D is NEGATIVE (b squared minus 4 a c less than zero), e.g., 2x squared minus 3x plus 5 equals zero (D equals 9 minus 40 equals minus 31), ZERO real roots exist, matching a Case Three parabola floating completely above or below without ever intersecting the horizontal x-axis! Thus checking discriminant D immediately reveals both root count AND exact graphical parabola behavior together!"
        ),
        "checkpoints": [
            {
                "question": "Determine the nature of roots for 2x² − 3x + 5 = 0 (Exercise 4.3 Q1 i):",
                "options": [
                    "No real roots (since D = (−3)² − 4(2)(5) = 9 − 40 = −31 < 0)",
                    "Two distinct real roots",
                    "Two equal real roots",
                    "One zero root and one positive root"
                ],
                "answer": 0,
                "hint": "Compute b² − 4ac cleanly with a = 2, b = −3, c = 5!",
                "explanation": "D = 9 − 40 = −31 < 0 confirms no real value satisfies the equation."
            },
            {
                "question": "Match 3x² − 4√3x + 4 = 0 (Exercise 4.3 Q1 ii) to its exact discriminant and roots:",
                "options": [
                    "D = 48 − 48 = 0  ⟹  two equal real roots: 2/√3 and 2/√3",
                    "D = 16 > 0  ⟹  two distinct roots",
                    "D = −32 < 0  ⟹  no real roots",
                    "D = 0  ⟹  roots 0 and 4"
                ],
                "answer": 0,
                "hint": "Square (−4√3)² = 16 × 3 = 48, then compare against 4ac = 4(3)(4) = 48!",
                "explanation": "D = 48 − 48 = 0 implies two equal real roots x = (4√3)/(2×3) = 2√3/3 = 2/√3."
            }
        ]
    },
    {
        "id": 13,
        "title": "Circular Boundary Pole",
        "subtitle": "Applying Discriminant & Formula to Textbook Geometric Positioning (Circular Park Pole)",
        "speech": (
            "Now witness how the Discriminant tests geometric feasibility on a brilliant textbook design puzzle (Section Four Point Four, Example Eight)! A civic park forms a neat circle of diameter 13 meters! "
            "Engineers wish to erect a tall lamp pole at point P along the circular boundary fence such that the difference between its straight distances to two opposite diametric gates A and B equals exactly 7 meters! "
            "Wait—is placing pole P there even geometrically possible? Let us translate straight into geometry! Because angle APB sits inside a semicircle on diameter AB equals 13 meters, Class Nine geometry guarantees angle APB is a crisp RIGHT ANGLE (90 degrees)! "
            "Let shorter distance PB equal x meters; then longer distance PA equals (x plus 7) meters! By Pythagoras' Theorem: x squared plus (x plus 7) squared equals 13 squared (169)! Expanding and dividing by 2 yields "
            "x squared plus 7x minus 60 equals zero! Check Discriminant D first: 49 plus 240 equals 289 (positive! 17 squared)—proving placement IS possible! Proving placement IS geometrically possible, solving gives exact positive distance x equals 5 meters for PB and PA equals 12 meters cleanly along opposite sides of the circular park boundary fence satisfying both rules!"
        ),
        "checkpoints": [
            {
                "question": "In the circular park boundary pole problem (diameter AB = 13 m, PA − PB = 7 m), why does x² + (x + 7)² = 13² apply automatically?",
                "options": [
                    "Because an angle inscribed in a semicircle (∠APB) is ALWAYS 90°, forming a right triangle with hypotenuse AB = 13 m",
                    "Because every triangle inside a circle is equilateral",
                    "Because 13 = 7 + 6",
                    "Because circular boundaries double all distances"
                ],
                "answer": 0,
                "hint": "Think of the famous circle theorem about the angle subtended by a diameter at any boundary point P!",
                "explanation": "Diameter AB = 13 m creates right triangle ΔAPB (∠APB = 90°), allowing Pythagoras AP² + PB² = AB²."
            },
            {
                "question": "What positive distances from gates B and A solve x² + 7x − 60 = 0 (D = 289)?",
                "options": [
                    "PB = 5 m and PA = 12 m  (discarding negative x = −12)",
                    "PB = 6 m and PA = 13 m",
                    "PB = 4 m and PA = 11 m",
                    "Impossible (D < 0)"
                ],
                "answer": 0,
                "hint": "Use Quadratic Formula (−7 ± 17)/2 or factor (x + 12)(x − 5) = 0!",
                "explanation": "(-7 + 17)/2 = 5 m (positive valid distance), giving PA = 5 + 7 = 12 m (note 5² + 12² = 13²!)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Finding Constant k",
        "subtitle": "Solving Unknown Coefficient k for Equal Real Roots (Exercise 4.3 Q2)",
        "speech": (
            "One of the most popular board-exam puzzles inside Exercise Four Point Three flips the discriminant backward: instead of asking whether roots are equal, it TELLS you two roots are equal and challenges you to find unknown constant k! "
            "Master BOTH textbook parts cleanly while catching a subtle trap! Look at Part One: 2x squared plus k x plus 3 equals zero possesses two equal real roots! Set Discriminant D equals b squared minus 4 a c equal to ZERO! "
            "Plug a equals 2, b equals k, c equals 3: k squared minus 4(2)(3) equals zero, giving k squared equals 24! Take square roots carefully remembering BOTH positive and negative roots: k equals plus-or-minus square root of 24 equals plus-or-minus 2 root 6! "
            "Now check Part Two carefully for the classic leading-zero trap: k x times (x minus 2) plus 6 equals zero! Expand into k x squared minus 2k x plus 6 equals zero! Setting D equals 4k squared minus 24k equals zero factors into 4k(k minus 6) equals zero—giving k equals 0 OR k equals 6! "
            "WAIT—if k equals 0, x squared vanishes! So reject k equals 0 immediately; ONLY k equals 6 works cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Find all real values of k so that 2x² + kx + 3 = 0 has two EQUAL real roots (Exercise 4.3 Q2 i):",
                "options": [
                    "k = +2√6  or  k = −2√6",
                    "Only k = +2√6",
                    "k = ±6",
                    "k = 24"
                ],
                "answer": 0,
                "hint": "Set b² − 4ac = k² − 24 = 0 and remember square roots give ±!",
                "explanation": "k² = 24 ⟹ k = ±√24 = ±2√6 (both keep leading coefficient a = 2 ≠ 0 valid)."
            },
            {
                "question": "In kx(x − 2) + 6 = 0 (Exercise 4.3 Q2 ii), solving D = 4k² − 24k = 0 yields k = 0 or k = 6. Why MUST k = 0 be rejected?",
                "options": [
                    "Setting k = 0 eliminates the x² term (leaving 6 = 0), violating standard quadratic condition a ≠ 0!",
                    "Because 0 cannot divide 24",
                    "Because k = 6 makes roots negative",
                    "Because 6 is an even number"
                ],
                "answer": 0,
                "hint": "Look at leading coefficient a = k inside kx² − 2kx + 6 = 0!",
                "explanation": "For kx² − 2kx + 6 = 0 to remain a quadratic equation, leading coefficient k must be non-zero; hence k = 6 uniquely."
            }
        ]
    },
    {
        "id": 15,
        "title": "Geometric Design Feasibility",
        "subtitle": "Using Discriminant D to Judge Real-World Garden, Age & Pond Design Possibility (Ex 4.3)",
        "speech": (
            "Suppose a city planner proposes building a rectangular park or mango grove matching strict perimeter and area rules—how can mathematics prove BEFORE laying a single brick whether such a design can ACTUALLY exist or is physically IMPOSSIBLE? "
            "Discriminant D delivers the instant verdict across Exercise Four Point Three! Test Proposal One (Mango Grove): Can we design a rectangular mango grove whose length equals twice its breadth (l equals 2b) and area equals 800 square meters? "
            "Write 2b times b equals 800, giving b squared equals 400 (D > 0)—YES, POSSIBLE! Breadth equals 20 m and length equals 40 m! Test Proposal Two (Age Riddle): Sum of two friends' ages is 20 years, and 4 years ago product of their ages was 48! "
            "Setting x(20 minus x) after subtracting 4 gives (x minus 4)(16 minus x) equals 48, expanding cleanly into x squared minus 20x plus 112 equals zero! Check Discriminant D: 400 minus 448 equals MINUS 48 (less than zero)! Because D is negative, NO real ages exist—PROVEN IMPOSSIBLE! "
            "Similarly, perimeter 80 m and area 400 m² gives D equals 0—possible as a 20 meter by 20 meter square park garden with equal sides cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Is the following situation possible (Ex 4.3 Q4): 'Sum of ages of two friends is 20 years; four years ago, the product of their ages was 48'?",
                "options": [
                    "NO—simplifies to x² − 20x + 112 = 0 with D = 400 − 448 = −48 < 0 (no real roots)",
                    "YES—ages are 12 and 8 years",
                    "YES—D = 0 gives equal ages 10 and 10",
                    "YES—ages are 16 and 4"
                ],
                "answer": 0,
                "hint": "Four years ago ages are (x − 4) and (20 − x − 4) = (16 − x); check D of (x−4)(16−x) = 48!",
                "explanation": "16x − x² − 64 + 4x = 48 ⟹ x² − 20x + 112 = 0. Since D = (−20)² − 4(1)(112) = −48 < 0, no real solution exists!"
            },
            {
                "question": "Is it possible to design a rectangular park of perimeter 80 m and area 400 m² (Exercise 4.3 Q5)?",
                "options": [
                    "YES—x + y = 40 and xy = 400 gives x² − 40x + 400 = 0 (D = 0), forming a 20 m × 20 m square!",
                    "NO—D is negative",
                    "YES—length 30 m and breadth 10 m",
                    "NO—squares are not rectangles"
                ],
                "answer": 0,
                "hint": "Remember a square IS a special rectangle (all angles 90°)! Check x(40 − x) = 400.",
                "explanation": "x² − 40x + 400 = (x − 20)² = 0 has D = 0, giving a valid 20 m × 20 m rectangular square park."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Four Summary",
        "subtitle": "Consolidating Standard Form, Root-Zero Equivalence, Factorisation, Formula & Discriminant",
        "speech": (
            "Outstanding work, Class Ten scholars! You have mastered every cornerstone of NCERT Class Ten Chapter Four: Quadratic Equations! Lock all five foundational ideas firmly together before advancing into Exercises Four Point One, Four Point Two, and Four Point Three! "
            "First, Standard Form: every quadratic simplifies cleanly to a x squared plus b x plus c equals zero with real coefficients and strictly nonzero a—never forget expanding parentheses first to catch cancellation traps! "
            "Second, Root-Zero Identity: real number alpha is a root of quadratic equation ax squared plus bx plus c equals zero IF AND ONLY IF it is a zero of quadratic polynomial ax squared plus bx plus c! "
            "Third, Factorisation: split middle term bx cleanly into two numbers summing to b and multiplying to a times c, equating each linear factor to zero! "
            "Fourth, Sridharacharya's Quadratic Formula solves ANY quadratic via x equals [minus b plus-or-minus root(D)] over 2a! Fifth, Discriminant D equals b squared minus 4 a c decides instantly: D > 0 gives 2 distinct roots, D = 0 gives 2 equal roots, D < 0 means impossible real geometry! Apply these exact five steps calmly across Exercises Four Point One, Four Point Two, Four Point Three, and our final Challenge Quiz next!"
        ),
        "checkpoints": [
            {
                "question": "If discriminant D = b² − 4ac of ax² + bx + c = 0 (a ≠ 0) equals 0, what exact formula gives its two equal real roots directly?",
                "options": [
                    "−b / (2a)  and  −b / (2a)",
                    "−b / a  and  c / a",
                    "+b / (2a)  only",
                    "±√c / a"
                ],
                "answer": 0,
                "hint": "Set D = 0 inside Sridharacharya's formula (−b ± √D)/(2a)!",
                "explanation": "When D = 0, (−b ± 0)/(2a) collapses cleanly to repeated root −b/(2a)."
            },
            {
                "question": "Which summary rule is ALWAYS true across Chapter 4: Quadratic Equations?",
                "options": [
                    "A real number α satisfies aα² + bα + c = 0 iff α is a zero of p(x); D > 0, D = 0, D < 0 govern 2, 1-equal, or 0 real roots",
                    "Every quadratic equation always has two distinct real roots",
                    "Condition a ≠ 0 allows b and c to cancel x² completely",
                    "Setting D = 0 proves no real roots exist"
                ],
                "answer": 0,
                "hint": "Check root-zero equivalence and all three discriminant cases!",
                "explanation": "Roots equal polynomial zeroes, and D = b² − 4ac governs whether 2 distinct, 2 equal, or 0 real roots exist."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch4 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

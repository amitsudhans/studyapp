#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 9: Propositions and their Converses
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Baudhāyana Pythagoras Converse",
        "subtitle": "Section 9.2 Example 5: Proving the Converse of the Baudhāyana-Pythagoras Theorem via SSS Congruence",
        "speech": (
            "Now behold one of the finest geometric proofs in Chapter Nine inside Section Nine Point Two, Example Five: PROVING THE CONVERSE OF THE BAUDHĀYANA-PYTHAGORAS THEOREM! "
            "Recall the famous forward theorem: If triangle ABC is right-angled at vertex C with legs a, b and hypotenuse c, then a squared plus b squared equals c squared! Now ask: Is its CONVERSE true? Specifically: If triangle ABC has side lengths a, b, c satisfying a squared plus b squared equals c squared, MUST angle C be ninety degrees? "
            "Follow this crystal-clear three-step deductive proof! Step One: Construct a separate helper right triangle PQR with angle R fixed at ninety degrees, leg QR equal to a, and leg PR equal to b! Step Two: Apply the forward Baudhāyana-Pythagoras Theorem inside right triangle PQR! Its hypotenuse PQ squared equals a squared plus b squared! Since we are GIVEN that a squared plus b squared equals c squared, taking positive square roots yields PQ equals c! "
            "Step Three: Compare triangle ABC and triangle PQR! Side BC equals QR equals a; side AC equals PR equals b; side AB equals PQ equals c! By SSS CONGRUENCE, triangle ABC is congruent to triangle PQR! Therefore angle C equals angle R equals NINETY DEGREES! Converse proven TRUE!"
        ),
        "checkpoints": [
            {
                "question": "In the proof of the converse of the Baudhāyana-Pythagoras Theorem (given a² + b² = c² in △ABC), which congruence criterion proves △ABC ≅ △PQR?",
                "options": [
                    "SSS Congruence (three pairs of equal sides: a, b, and hypotenuse PQ = c)",
                    "AAA Similarity",
                    "SSA Criterion",
                    "RHS directly on △ABC before proving ∠C = 90°"
                ],
                "answer": 0,
                "hint": "We don't know ∠C = 90° yet—we only know all THREE side lengths match!",
                "explanation": "Constructing right △PQR with legs a, b gives PQ = √(a² + b²) = c, matching all three sides (a, b, c) of △ABC by SSS."
            },
            {
                "question": "Does a triangle with side lengths 9 cm, 12 cm, and 15 cm contain a 90° right angle?",
                "options": [
                    "Yes — because 9² + 12² = 81 + 144 = 225 = 15², so the converse guarantees a right angle opposite the 15 cm side",
                    "No — because 9 + 12 ≠ 15",
                    "Only if it is equilateral",
                    "Cannot be determined without measuring with a protractor"
                ],
                "answer": 0,
                "hint": "Test whether a² + b² = c² holds for 9, 12, 15!",
                "explanation": "9² + 12² = 225 = 15² satisfies the converse of the Baudhāyana-Pythagoras theorem, proving the triangle is right-angled."
            }
        ]
    },
    {
        "id": 10,
        "title": "Alternative Conditional Phrasings",
        "subtitle": "Section 9.2 Note on Alternative Formulations: 'Y when X', 'Y if X', 'All X are Y', 'X only if Y'",
        "speech": (
            "Watch out for a sneaky trap in word problems and proofs inside Section Nine Point Two: ALTERNATIVE ENGLISH PHRASINGS OF IF-THEN PROPOSITIONS! "
            "Mathematicians do NOT always write the neat template 'If X, then Y'! Conditional statements frequently wear everyday disguises while keeping the EXACT same logical meaning! "
            "Learn how to translate four major English phrasings back into standard 'If X, then Y' form before taking any converse! First: 'Y WHEN X' or 'Y IF X'! For example, 'A number is divisible by two when its last digit is even' means 'If a number's last digit is even, then it is divisible by two'! Notice that whatever immediately follows IF or WHEN is ALWAYS Premise X! "
            "Second: 'ALL X ARE Y' or 'EVERY X IS Y'! For example, 'Every square is a rectangle' translates directly into 'If a figure is a square, then it is a rectangle'! Third: 'X ONLY IF Y'! For example, 'A whole number is prime greater than two only if it is odd' means 'If a prime exceeds two, then it is odd'! Always translate into 'If X, then Y' FIRST—otherwise you might accidentally flip the wrong direction when forming the converse!"
        ),
        "checkpoints": [
            {
                "question": "Rewrite \"A triangle is isosceles when two of its sides are equal\" in standard \"If X, then Y\" form.",
                "options": [
                    "\"If two sides of a triangle are equal, then the triangle is isosceles.\"",
                    "\"If a triangle is isosceles, then two of its sides are not equal.\"",
                    "\"If a triangle is not isosceles, then two sides are equal.\"",
                    "\"Two sides are equal only when it is equilateral.\""
                ],
                "answer": 0,
                "hint": "The clause following 'when' is the premise X!",
                "explanation": "'Y when X' translates directly to 'If X, then Y'."
            },
            {
                "question": "What is the CONVERSE of \"All squares are rectangles\" (i.e., \"If a quadrilateral is a square, then it is a rectangle\")?",
                "options": [
                    "\"If a quadrilateral is a rectangle, then it is a square.\" (FALSE — counterexample: 5 × 3 rectangle)",
                    "\"If a quadrilateral is not a square, then it is not a rectangle.\"",
                    "\"All squares are rhombuses.\"",
                    "\"Every rectangle is a polygon.\""
                ],
                "answer": 0,
                "hint": "First rewrite 'All X are Y' as 'If X, then Y', then swap X and Y!",
                "explanation": "Swapping 'square' and 'rectangle' gives 'If a quadrilateral is a rectangle, then it is a square', which is false for non-square rectangles."
            }
        ]
    },
    {
        "id": 11,
        "title": "Parallel Transversal Converses",
        "subtitle": "Exercise 9.1 Geometry: Parallel Lines, Transversal Angles & Quadrilateral Diagonal Converses",
        "speech": (
            "Now apply your logical toolkit to Exercise Nine Point One Geometry problems: PARALLEL LINES, TRANSVERSALS, AND QUADRILATERAL DIAGONALS! "
            "First inspect parallel lines cut by a transversal! Forward proposition: If two straight lines are parallel, then every pair of corresponding angles formed by a transversal is equal! True by the Corresponding Angles Axiom! Now flip it for the converse: If a transversal makes a pair of corresponding angles equal, then the two lines are parallel! ALSO TRUE! Parallel lines and equal corresponding angles (or equal alternate interior angles) form exact TWO-WAY equivalences! "
            "Now test quadrilateral diagonal converses carefully—here traps await! Proposition A: If a quadrilateral is a square, then its diagonals are equal in length! Clearly TRUE! Flip it for the converse: If a quadrilateral's diagonals are equal, must it be a square? FALSE! A non-square rectangle or an isosceles trapezium has equal diagonals without being a square! "
            "Proposition B: If a quadrilateral is a square, then its diagonals bisect each other at ninety degrees! TRUE! Flip it: If diagonals bisect each other at ninety degrees, must it be a square? FALSE—any non-square RHOMBUS has perpendicular bisecting diagonals of unequal lengths and non-right interior corner angles!"
        ),
        "checkpoints": [
            {
                "question": "Which quadrilateral is a valid COUNTEREXAMPLE to \"If the diagonals of a quadrilateral bisect each other at 90°, then it is a square\"?",
                "options": [
                    "A non-square rhombus (e.g., diagonals of lengths 6 cm and 8 cm bisecting at 90°)",
                    "A square of side 5 cm",
                    "A scalene triangle",
                    "A non-rhombus rectangle"
                ],
                "answer": 0,
                "hint": "Perpendicular bisecting diagonals guarantee a rhombus, not necessarily equal diagonals!",
                "explanation": "A rhombus with unequal diagonals (say 6 and 8) has perpendicular bisecting diagonals but its angles are not 90°, so it is not a square."
            },
            {
                "question": "Are BOTH \"If lines are parallel, alternate interior angles are equal\" AND its converse \"If alternate interior angles are equal, lines are parallel\" true?",
                "options": [
                    "Yes — BOTH the proposition and its converse are TRUE",
                    "Only the forward proposition is true",
                    "Only the converse is true",
                    "Neither is true"
                ],
                "answer": 0,
                "hint": "Recall the Parallel Lines & Transversal Theorems from geometry!",
                "explanation": "Equal alternate interior angles (and equal corresponding angles) are both necessary and sufficient for two coplanar lines to be parallel."
            }
        ]
    },
    {
        "id": 12,
        "title": "Incentre Bisector Logic",
        "subtitle": "Exercise 9.1 Geometry: Angle Bisectors, Incentres & Triangle Side-Length Converses",
        "speech": (
            "Now explore triangle angle bisectors, incentres, and side-length converses inside Exercise Nine Point One! "
            "Consider a foundational triangle property: Every point on the internal angle bisector of angle ABC is equidistant from both rays BA and BC! Look at why: dropping perpendiculars from point P onto BA and BC creates two right triangles sharing hypotenuse BP and equal bisected angles—congruent by AAS! And its CONVERSE—if an interior point P is equidistant from rays BA and BC, then P lies on the angle bisector—is ALSO TRUE by RHS congruence! "
            "Applying this two-way equivalence to all three interior angles of a triangle proves why all three angle bisectors meet at ONE SINGLE POINT—the INCENTRE—which sits at the exact same perpendicular distance r (the inradius) from all three sides! "
            "Now test a triangle side-length statement! Proposition: If a triangle is equilateral, then all three medians are equal in length! TRUE! What about its converse—if all three medians of a triangle are equal, must it be equilateral? ALSO TRUE! Contrast that with 'If a triangle is isosceles, two medians are equal'—true both ways—versus 'If two sides are 5 cm and 5 cm, perimeter exceeds 10 cm' (true forward, false converse)!"
        ),
        "checkpoints": [
            {
                "question": "Is the converse of \"If point P lies on the angle bisector of ∠ABC, then P is equidistant from arms BA and BC\" true?",
                "options": [
                    "Yes — by RHS congruence, any interior point equidistant from both arms lies on the angle bisector",
                    "No — only vertices lie on angle bisectors",
                    "Only in equilateral triangles",
                    "No — RHS does not apply to right triangles"
                ],
                "answer": 0,
                "hint": "Drop perpendiculars from P to BA and BC (equal legs, shared hypotenuse BP, two 90° angles)!",
                "explanation": "Equal perpendicular distances + shared hypotenuse + 90° angles give RHS congruence, making the bisector angles equal."
            },
            {
                "question": "What does the concurrence of all three angle bisectors at the INCENTRE guarantee?",
                "options": [
                    "The incentre is equidistant from all three SIDES of the triangle (forming the centre of the incircle)",
                    "The incentre is equidistant from all three vertices",
                    "All three sides have equal length",
                    "The triangle must be right-angled"
                ],
                "answer": 0,
                "hint": "Each angle bisector preserves equal distance to its two adjacent sides!",
                "explanation": "Because the incentre lies on all three angle bisectors, its perpendicular distance to all three sides is identical (the inradius)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Algebraic Squaring Cubing",
        "subtitle": "Exercise 9.1 Algebra: Why x = y ⇒ x² = y² Fails Its Converse, While x = y ⇔ x³ = y³ Holds Both Ways",
        "speech": (
            "Now examine one of the sharpest algebraic traps in Exercise Nine Point One: SQUARING VERSUS CUBING EQUATIONS! "
            "Test the squaring proposition first for any real numbers x and y! Forward proposition: If x equals y, then x squared equals y squared! Obviously TRUE—multiplying identical numbers by themselves yields identical squares! "
            "Now flip it for the CONVERSE: If x squared equals y squared, then x equals y! CAREFUL! Is this converse true across all real numbers? TEST NEGATIVE NUMBERS! Take x equals three and y equals NEGATIVE THREE! Compute x squared equals nine and y squared equals nine—so the premise x squared equals y squared IS TRUE! Yet x does NOT equal y because three is not negative three! Squaring erases minus signs, so x squared equals y squared means x equals y OR x equals negative y! Converse: FALSE! "
            "Now contrast this with CUBING! Forward: If x equals y, then x cubed equals y cubed (TRUE)! Converse: If x cubed equals y cubed, then x equals y! Over real numbers, positive cubes come ONLY from positive roots and negative cubes come ONLY from negative roots—cubing preserves signs! Therefore, BOTH x equals y implies x cubed equals y cubed AND its converse are TRUE!"
        ),
        "checkpoints": [
            {
                "question": "Which pair (x, y) is a valid COUNTEREXAMPLE to the converse \"If x² = y², then x = y\"?",
                "options": [
                    "x = 5, y = −5 (since 5² = 25 = (−5)², yet 5 ≠ −5)",
                    "x = 4, y = 4",
                    "x = 2, y = 3",
                    "x = 0, y = 0"
                ],
                "answer": 0,
                "hint": "Pick two unequal numbers whose squares are identical!",
                "explanation": "5² = (−5)² = 25 satisfies the premise x² = y², while 5 ≠ −5 falsifies the conclusion x = y."
            },
            {
                "question": "Why is the converse \"If x³ = y³, then x = y\" TRUE for all real numbers x and y (unlike x² = y²)?",
                "options": [
                    "Cubing is strictly increasing and preserves sign: x³ − y³ = (x − y)(x² + xy + y²) = 0 forces x = y over real numbers",
                    "Because negative numbers have no real cubes",
                    "Because x³ is always positive",
                    "Because 3 is a prime number"
                ],
                "answer": 0,
                "hint": "Notice that (−5)³ = −125 ≠ +125 = 5³!",
                "explanation": "Odd powers preserve signs and x² + xy + y² > 0 whenever x, y are not both 0, so x³ = y³ implies x = y over ℝ."
            }
        ]
    },
    {
        "id": 14,
        "title": "Divisibility Rules Logic",
        "subtitle": "Exercise 9.1 Number Theory: Factors of 24, 60, 8 & The Two-Way Digit-Sum Rule for 3",
        "speech": (
            "Now inspect divisibility propositions and their converses inside Exercise Nine Point One Number Theory! "
            "Start with the classic digit-sum rule for THREE! Forward proposition: If a whole number is divisible by three, then the sum of its digits is divisible by three! TRUE! Converse: If the sum of a whole number's digits is divisible by three, then the number itself is divisible by three! ALSO TRUE! Both directions hold, which is why the digit-sum test works reliably in both directions! "
            "Now compare ONE-WAY divisibility traps involving factors of twenty-four, sixty, and eight! Test this statement: If a number is divisible by twenty-four, then it is divisible by eight! Since twenty-four equals eight times three, this forward proposition is TRUE! Flip it for the converse: If a number is divisible by eight, then it is divisible by twenty-four! FALSE—counterexample: EIGHT or SIXTEEN divides cleanly by eight, yet NOT by twenty-four! "
            "Similarly, test: If a number divides evenly into sixty, then it divides evenly into one hundred twenty (TRUE, because sixty divides one hundred twenty), whereas its converse fails at FORTY—forty divides one hundred twenty, NOT sixty! Always check divisor direction carefully before reversing any divisibility rule!"
        ),
        "checkpoints": [
            {
                "question": "Which number disproves the converse \"If a positive integer is divisible by 8, then it is divisible by 24\"?",
                "options": ["16 (divisible by 8, NOT divisible by 24)", "24", "48", "12"],
                "answer": 0,
                "hint": "Choose a multiple of 8 that is NOT a multiple of 24!",
                "explanation": "16 = 8 × 2 is divisible by 8, yet 16 is not divisible by 24 (12 is not divisible by 8; 24 and 48 are multiples of 24)."
            },
            {
                "question": "Which divisibility rule is a TRUE two-way equivalence (both proposition AND converse hold)?",
                "options": [
                    "\"A whole number is divisible by 3 if and only if the sum of its digits is divisible by 3.\"",
                    "\"If a number is divisible by 4, it is divisible by 8.\"",
                    "\"If a number ends in 5, it is divisible by 10.\"",
                    "\"If a number is a factor of 60, it is a factor of 24.\""
                ],
                "answer": 0,
                "hint": "Remember 10 ≡ 1 (mod 3), so every power of 10 leaves remainder 1 when divided by 3!",
                "explanation": "A number and its digit sum always leave the exact same remainder upon division by 3, making both directions true."
            }
        ]
    },
    {
        "id": 15,
        "title": "Prime Formula Counterexamples",
        "subtitle": "Exercise 9.1 Number Theory & Geometry: Testing 4n²+1, n²+n+11, 4ⁿ+3, 2ⁿ−1 & Stick Diagonals",
        "speech": (
            "Now put on your mathematical detective hat for Exercise Nine Point One's prime-formula counterexamples and intersecting-stick diagonal puzzles! "
            "Many polynomial or exponential formulas produce primes for the first few natural numbers, tempting hasty guesses! Test four famous formulas from your syllabus! "
            "First, check n squared plus n plus eleven! For n equals one through nine, it outputs primes! Yet at n equals TEN: ten squared plus ten plus eleven equals ONE HUNDRED TWENTY-ONE, which is ELEVEN SQUARED—composite! "
            "Second, check four n squared plus one! At n equals one: five (prime); at n equals two: seventeen (prime); at n equals three: thirty-seven (prime); YET at n equals FOUR: four times sixteen plus one equals SIXTY-FIVE equals five times thirteen—composite! "
            "Third, check four to the power n plus three! At n equals one: seven (prime); at n equals two: nineteen (prime); at n equals three: sixty-seven (prime); YET at n equals FOUR: two hundred fifty-nine equals seven times thirty-seven! Fourth, check Mersenne-style two to the n minus one: prime at n equals two, three, five, YET composite at n equals FOUR (fifteen equals three times five)! And remember stick diagonals: two equal sticks bisecting each other ALWAYS form a rectangle—add ninety degrees for a square!"
        ),
        "checkpoints": [
            {
                "question": "Which value of n provides the smallest natural-number COUNTEREXAMPLE proving \"4n² + 1 is prime for all n ≥ 1\" is FALSE?",
                "options": [
                    "n = 4 (gives 4(16) + 1 = 65 = 5 × 13, composite)",
                    "n = 1 (gives 5, prime)",
                    "n = 2 (gives 17, prime)",
                    "n = 3 (gives 37, prime)"
                ],
                "answer": 0,
                "hint": "Test n = 1, 2, 3, 4 in 4n² + 1!",
                "explanation": "4(1)²+1=5, 4(2)²+1=17, 4(3)²+1=37 are all prime, while 4(4)²+1 = 65 = 5 × 13 is composite."
            },
            {
                "question": "If two straight sticks of EQUAL length are pinned together so they bisect each other at their midpoints, which quadrilateral do their four endpoints ALWAYS form?",
                "options": [
                    "A rectangle (and if they also cross at 90°, a square)",
                    "Only a general trapezium",
                    "A non-parallelogram kite",
                    "A pentagon"
                ],
                "answer": 0,
                "hint": "Bisecting diagonals form a parallelogram; EQUAL bisecting diagonals force all four angles to be 90°!",
                "explanation": "Diagonals that bisect each other create a parallelogram; equal diagonals make that parallelogram a rectangle."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Logic Summary",
        "subtitle": "Chapter 9 Synthesis: Propositions, Converses, Truth Independence & Counterexample Mastery",
        "speech": (
            "Congratulations on completing Chapter Nine: Propositions and Their Converses! Let us synthesize the four foundational pillars of mathematical logic you have mastered! "
            "Pillar One: A PROPOSITION is any clear declarative statement that is strictly True or strictly False—never a question, command, opinion, or open sentence with unspecified variables! "
            "Pillar Two: Conditional theorems take the standard form 'If X, then Y' (X implies Y), where X is the premise and Y is the conclusion—and watch for disguised phrasings like 'Y when X', 'All X are Y', or 'X only if Y'! "
            "Pillar Three: Forming the CONVERSE flips 'If X, then Y' into 'If Y, then X'! Remember the four possible truth combinations: BOTH true (perfect squares and odd factor counts; Baudhāyana-Pythagoras theorem and converse; x equals y and x cubed equals y cubed), forward true and converse false (rain and wet roads; multiples of six and three; congruence and equal area; x equals y and x squared equals y squared), forward false and converse true, or BOTH false! "
            "Pillar Four: ONE SINGLE COUNTEREXAMPLE—where premise X holds while conclusion Y fails—conclusively disproves any universal mathematical proposition! Now test your complete logical mastery across the forty silent quiz challenges ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement about a proposition (P ⇒ Q) and its converse (Q ⇒ P) is ALWAYS accurate?",
                "options": [
                    "A proposition and its converse are logically independent: both can be true, one true and one false, or both false",
                    "Whenever P ⇒ Q is true, Q ⇒ P must also be true",
                    "Whenever P ⇒ Q is true, Q ⇒ P must be false",
                    "A converse is formed by negating both P and Q without swapping"
                ],
                "answer": 0,
                "hint": "Think across all examples: squares/odd factors (T, T), rain/wet road (T, F), wet road/rain (F, T), and impossible claims (F, F)!",
                "explanation": "All four truth-value combinations of (Proposition, Converse) exist across mathematics and everyday logic."
            },
            {
                "question": "How many valid counterexamples are required to prove that a universal \"If X, then Y\" proposition is FALSE?",
                "options": [
                    "Just ONE single counterexample where X is true and Y is false",
                    "At least 10 counterexamples",
                    "More than half of all cases",
                    "Infinitely many counterexamples"
                ],
                "answer": 0,
                "hint": "Remember Euler's single counterexample F₅ = 2³² + 1 = 641 × 6,700,417!",
                "explanation": "A universal claim promises zero exceptions, so a single valid counterexample suffices to disprove it."
            }
        ]
    }
]

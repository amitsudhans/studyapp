#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 9: The Baudhāyana-Pythagoras Theorem
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Root Two Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Doubling/Halving Squares, Isosceles c = a√2, Decimal Bounds & Euclid's Proof",
        "questions": [
            {
                "question": "Verse 1.9 of Baudhāyana's Śulba-Sūtra (c. 800 BCE) constructs a square with DOUBLE the area of a given square. How does it construct that double-area square?",
                "options": [
                    "By building the new square on the DIAGONAL of the original square",
                    "By doubling each side length of the original square",
                    "By cutting off 1/4 of each corner",
                    "By joining the midpoints of all four sides"
                ],
                "answer": 0,
                "hint": "Doubling side length multiplies area by 4, whereas building on the diagonal encloses 4 congruent triangles vs 2!",
                "explanation": "A square built on the diagonal of an original square contains 4 congruent right isosceles triangles instead of 2 — double the area.",
                "solution_steps": [
                    "Original square of side s splits along one diagonal into 2 congruent right isosceles triangles.",
                    "Square built on diagonal contains 4 copies of that exact triangle.",
                    "4 ÷ 2 = 2, proving diagonal-based square has exact double area."
                ]
            },
            {
                "question": "If the side length of a 6 cm square is doubled to 12 cm, by what factor does its area increase?",
                "options": [
                    "4 times   (36 sq cm → 144 sq cm)",
                    "2 times",
                    "6 times",
                    "8 times"
                ],
                "answer": 0,
                "hint": "Multiply scale factors across BOTH length and breadth: 2 × 2!",
                "explanation": "(2s)² = 4s², so doubling side length quadruples area (36 → 144 sq cm).",
                "solution_steps": [
                    "Original area = 6 × 6 = 36 sq cm.",
                    "New area = 12 × 12 = 144 sq cm.",
                    "Divide 144 ÷ 36 = 4 times (multiplicative scaling 2 × 2 = 4)."
                ]
            },
            {
                "question": "Joining the four side midpoints P, Q, R, S of a square with area 100 sq cm creates an inscribed tilted square PQRS. What is the area of PQRS?",
                "options": [
                    "50 sq cm",
                    "25 sq cm",
                    "75 sq cm",
                    "200 sq cm"
                ],
                "answer": 0,
                "hint": "Folding the 4 outer corners inward covers PQRS completely without gaps!",
                "explanation": "Inscribed midpoint square PQRS always holds exact half the outer square's area: 100 ÷ 2 = 50 sq cm.",
                "solution_steps": [
                    "Connect four side midpoints to form inscribed square PQRS.",
                    "Four outer triangular flaps fold inward onto center to match PQRS exactly.",
                    "Half of 100 sq cm = 50 sq cm."
                ]
            },
            {
                "question": "An isosceles right triangle has unit legs measuring 1 cm and 1 cm. What is the exact square of its hypotenuse c² and length c?",
                "options": [
                    "c² = 2; c = √2 cm",
                    "c² = 4; c = 2 cm",
                    "c² = 1; c = 1 cm",
                    "c² = 2; c = 1.4 cm exactly"
                ],
                "answer": 0,
                "hint": "Diagonal square doubles unit square area 1 to 2!",
                "explanation": "c² = 1² + 1² = 2, so c = √2 cm.",
                "solution_steps": [
                    "Set leg a = 1 in isosceles formula c² = 2a².",
                    "Compute c² = 2(1²) = 2.",
                    "Take positive root: c = √2 cm."
                ]
            },
            {
                "question": "If an isosceles right triangle has legs a = 9 cm each, what is its exact hypotenuse length c?",
                "options": [
                    "9√2 cm",
                    "18 cm",
                    "√18 cm",
                    "81 cm"
                ],
                "answer": 0,
                "hint": "Apply the general isosceles right triangle formula c = a√2!",
                "explanation": "c² = 2(9²) = 162, so c = 9√2 cm.",
                "solution_steps": [
                    "Use general relation c² = 2a².",
                    "Substitute a = 9: c² = 2 × 81 = 162.",
                    "Extract square root: c = √(81 × 2) = 9√2 cm."
                ]
            },
            {
                "question": "An isosceles right triangle has a hypotenuse of c = 12 cm. Find the area a² of the square on ONE leg, and leg length a:",
                "options": [
                    "a² = 72 sq cm; a = √72 cm",
                    "a² = 144 sq cm; a = 12 cm",
                    "a² = 36 sq cm; a = 6 cm",
                    "a² = 288 sq cm; a = √288 cm"
                ],
                "answer": 0,
                "hint": "Since c² = 2a², divide c² = 144 by 2!",
                "explanation": "2a² = 12² = 144 → a² = 72 → a = √72 cm.",
                "solution_steps": [
                    "Write 2a² = c² = 12² = 144.",
                    "Divide by 2: a² = 72 sq cm.",
                    "Leg length a = √72 cm."
                ]
            },
            {
                "question": "Knowing 1.414² = 1.999396 and 1.415² = 2.002225 gives which accurate nested decimal bound for √2?",
                "options": [
                    "1.414 < √2 < 1.415",
                    "1.413 < √2 < 1.414",
                    "1.415 < √2 < 1.416",
                    "1.999 < √2 < 2.002"
                ],
                "answer": 0,
                "hint": "Compare 1.999396 < 2 < 2.002225!",
                "explanation": "Since 1.414² < 2 < 1.415², √2 lies strictly between 1.414 and 1.415.",
                "solution_steps": [
                    "Note 1.414² = 1.999396 < 2.",
                    "Note 1.415² = 2.002225 > 2.",
                    "Conclude 1.414 < √2 < 1.415."
                ]
            },
            {
                "question": "Why must √2 have a NON-TERMINATING decimal representation?",
                "options": [
                    "Squaring any terminating decimal leaves a non-zero final digit (1, 4, 5, 6, or 9), never producing exact 2.000...",
                    "Because 2 is an even number",
                    "Because dividing by 10 always repeats",
                    "Because terminating decimals cannot exceed 1.4"
                ],
                "answer": 0,
                "hint": "Test the units digit of d² for every non-zero last digit d from 1 to 9!",
                "explanation": "No non-zero digit 1–9 squares to end in 0, so a terminating decimal squared can never equal 2.",
                "solution_steps": [
                    "Any terminating decimal ends in a non-zero digit d ∈ {1..9}.",
                    "Inspect d² ∈ {1, 4, 9, 16, 25, 36, 49, 64, 81} — none ends in 0.",
                    "Thus x² always ends in a non-zero digit and cannot equal exact 2."
                ]
            },
            {
                "question": "In Euclid's irrationality proof (Elements, c. 300 BCE), assuming √2 = m/n leads to 2n² = m². What contradiction finishes the proof?",
                "options": [
                    "Prime factor 2 appears an ODD number of times on the LHS (2n²) and an EVEN number of times on the RHS (m²)",
                    "m² is always negative while 2n² is positive",
                    "n² must be divisible by 3",
                    "m/n exceeds 2"
                ],
                "answer": 0,
                "hint": "Squaring doubles every prime exponent, forcing even counts of factor 2 in n² and m²!",
                "explanation": "In 2n² = m², n² has even factor-2s so 2n² has odd factor-2s, contradicting m² having even factor-2s.",
                "solution_steps": [
                    "Square √2 = m/n to obtain integer equation 2n² = m².",
                    "Count prime factor 2: every square (n², m²) holds an even count of 2s.",
                    "LHS 2n² adds +1 factor of 2 (odd count ≠ even count on RHS m²): impossible."
                ]
            },
            {
                "question": "Which number equals BOTH the area of an inscribed midpoint square PQRS of a 10 cm square AND the value of c² for an isosceles right triangle with legs a = 5 cm?",
                "options": [
                    "50 sq cm",
                    "25 sq cm",
                    "100 sq cm",
                    "20 sq cm"
                ],
                "answer": 0,
                "hint": "Half of 10² = 50, and 2 × 5² = 50!",
                "explanation": "Half of 100 sq cm is 50 sq cm, and for legs a = 5 cm, c² = 2(5²) = 50 sq cm.",
                "solution_steps": [
                    "Inscribed square PQRS inside 10 × 10 square has area 100 ÷ 2 = 50 sq cm.",
                    "Isosceles right triangle with leg 5 has hypotenuse square c² = 2(5²) = 50 sq cm.",
                    "Both match cleanly at 50 sq cm."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Theorem Dissection Triples",
        "subtitle": "Challenge Arena 2 (10 MCQs): Verse 1.12/2.1 Dissection, a² + b² = c², Verse 1.13 Triples & Odd-Square Generator",
        "questions": [
            {
                "question": "Which statement matches Verse 1.12 of Baudhāyana's Śulba-Sūtra and the Baudhāyana-Pythagoras Theorem?",
                "options": [
                    "The square built on the hypotenuse equals the sum of the squares on the two legs: a² + b² = c²",
                    "The sum of two leg lengths equals hypotenuse: a + b = c",
                    "The area of hypotenuse square equals a × b",
                    "Only isosceles triangles satisfy c² = a² + b²"
                ],
                "answer": 0,
                "hint": "Verse 1.12 combines two unequal squares a² and b² into one single square c²!",
                "explanation": "a² + b² = c² holds universally for every right-angled triangle with legs a, b and hypotenuse c.",
                "solution_steps": [
                    "Build squares of areas a² and b² on the two perpendicular legs.",
                    "Build square of area c² on the hypotenuse.",
                    "Area conservation proves c² = a² + b²."
                ]
            },
            {
                "question": "Why is Baudhāyana credited before Pythagoras (~500 BCE) in stating the general theorem a² + b² = c²?",
                "options": [
                    "Baudhāyana stated it in general form in his Śulba-Sūtra around 800 BCE — centuries before Pythagoras",
                    "Because Baudhāyana discovered it in 1994",
                    "Because Pythagoras only studied cubes",
                    "Because the Śulba-Sūtra was written in Greece"
                ],
                "answer": 0,
                "hint": "Compare c. 800 BCE vs c. 500 BCE!",
                "explanation": "Baudhāyana's Śulba-Sūtra (c. 800 BCE) predates Pythagoras (c. 500 BCE) by around three centuries.",
                "solution_steps": [
                    "Identify Baudhāyana's Śulba-Sūtra (~800 BCE) Verse 1.12.",
                    "Identify Greek mathematician Pythagoras (~500 BCE).",
                    "Conclude NCERT adopts Baudhāyana-Pythagoras Theorem for historical accuracy."
                ]
            },
            {
                "question": "In Baudhāyana's Verse 2.1 dissection proof combining squares of side a and side b, how are the pieces transformed into a single square c²?",
                "options": [
                    "Two right triangles (legs a, b, hypotenuse c) are cut using a rectangle mark and slid/rotated without overlap to form a c × c square",
                    "Both squares are melted and reshaped",
                    "Only the corners of square b² are trimmed and discarded",
                    "A grid of 100 smaller squares is shaded"
                ],
                "answer": 0,
                "hint": "Notice how marking a rectangle of width a inside the larger square slices out two congruent right triangles!",
                "explanation": "Cutting two congruent right triangles (legs a, b) from the joined L-shape and rotating them preserves total area to build a c × c square.",
                "solution_steps": [
                    "Join squares a² and b² along a straight base.",
                    "Mark width a on b² and dissect two right triangles (a, b, c).",
                    "Translate/rotate triangles to complete a seamless c × c square (c² = a² + b²)."
                ]
            },
            {
                "question": "A right-angled triangle has legs a = 9 cm and b = 12 cm. Find its hypotenuse c:",
                "options": [
                    "15 cm",
                    "21 cm",
                    "√63 cm",
                    "10.5 cm"
                ],
                "answer": 0,
                "hint": "Notice 3 × (3, 4, 5) or compute 9² + 12² = 81 + 144!",
                "explanation": "9² + 12² = 81 + 144 = 225, and √225 = 15 cm.",
                "solution_steps": [
                    "Compute a² + b² = 9² + 12² = 81 + 144 = 225.",
                    "Equate to c²: c² = 225.",
                    "Take positive square root: c = √225 = 15 cm."
                ]
            },
            {
                "question": "Which historical Baudhāyana triple is NOT listed among the primitive triples from Verse 1.13?",
                "options": [
                    "(6, 8, 10)   (scaled 2 × (3, 4, 5), not primitive!)",
                    "(3, 4, 5)",
                    "(5, 12, 13)",
                    "(7, 24, 25)"
                ],
                "answer": 0,
                "hint": "Check which triple has a common factor greater than 1!",
                "explanation": "(6, 8, 10) shares common factor 2, whereas (3,4,5), (5,12,13), (8,15,17), and (7,24,25) are primitive triples.",
                "solution_steps": [
                    "Check common divisors: HCF(3,4,5)=1, HCF(5,12,13)=1, HCF(7,24,25)=1.",
                    "Check (6, 8, 10): all divisible by 2 (HCF = 2 > 1).",
                    "Therefore (6, 8, 10) is a scaled non-primitive triple."
                ]
            },
            {
                "question": "If (8, 15, 17) is a valid Baudhāyana triple, which scaled triple is guaranteed to satisfy a² + b² = c² for multiplier k = 5?",
                "options": [
                    "(40, 75, 85)",
                    "(13, 20, 22)   (+5 added to each)",
                    "(40, 15, 17)",
                    "(16, 30, 85)"
                ],
                "answer": 0,
                "hint": "Multiply ALL THREE sides cleanly by k = 5!",
                "explanation": "5 × (8, 15, 17) = (40, 75, 85), obeying 40² + 75² = 1600 + 5625 = 7225 = 85².",
                "solution_steps": [
                    "Apply scaling theorem: (ka, kb, kc) stays a right triple.",
                    "Multiply each term by k = 5: 5×8 = 40, 5×15 = 75, 5×17 = 85.",
                    "Verify 40² + 75² = 85²."
                ]
            },
            {
                "question": "Using the odd-sum generator (n − 1)² + (2n − 1) = n², what happens when you set the nth odd number (2n − 1) = 49 (= 7²)?",
                "options": [
                    "n = 25, generating primitive triple (7, 24, 25)",
                    "n = 24, generating (7, 23, 24)",
                    "n = 49, generating (7, 48, 49)",
                    "n = 7, generating (6, 7, 13)"
                ],
                "answer": 0,
                "hint": "Solve 2n − 1 = 49 → 2n = 50!",
                "explanation": "2n − 1 = 49 gives n = 25, so 24² + 7² = 25², producing (7, 24, 25).",
                "solution_steps": [
                    "Equate middle odd term: 2n − 1 = 49.",
                    "Solve for n: 2n = 50 → n = 25 (so n − 1 = 24).",
                    "Substitute into (n − 1)² + k² = n² → 24² + 7² = 25²."
                ]
            },
            {
                "question": "Use the odd-square generator with k² = 121 (= 11²) to discover the next primitive triple:",
                "options": [
                    "(11, 60, 61)",
                    "(11, 120, 121)",
                    "(11, 59, 60)",
                    "(11, 61, 62)"
                ],
                "answer": 0,
                "hint": "Solve 2n − 1 = 121 → 2n = 122 → n = 61!",
                "explanation": "With n = 61 and n − 1 = 60, 60² + 11² = 3600 + 121 = 3721 = 61².",
                "solution_steps": [
                    "Set 2n − 1 = 121 (= 11²).",
                    "Find n = (121 + 1)/2 = 61, and n − 1 = 60.",
                    "Triple = (11, 60, 61)."
                ]
            },
            {
                "question": "Two separate squares have areas 64 sq cm and 225 sq cm. Combined using Verse 1.12, what is the perimeter of the single unified square?",
                "options": [
                    "68 cm   (side c = 17 cm → perimeter 4 × 17)",
                    "289 cm",
                    "17 cm",
                    "92 cm"
                ],
                "answer": 0,
                "hint": "First add areas 64 + 225 = 289 sq cm to get side c = 17 cm, then multiply by 4 sides!",
                "explanation": "Unified area = 289 sq cm → side c = 17 cm → perimeter = 4 × 17 = 68 cm.",
                "solution_steps": [
                    "Add two square areas: 64 + 225 = 289 sq cm.",
                    "Find new square side length: c = √289 = 17 cm.",
                    "Multiply by 4 sides for perimeter: 4 × 17 = 68 cm."
                ]
            },
            {
                "question": "Check whether (10, 24, 26) is a valid Baudhāyana triple, and identify its primitive parent:",
                "options": [
                    "Yes, valid triple; scaled 2 × (5, 12, 13)",
                    "No, 10² + 24² ≠ 26²",
                    "Yes, valid AND primitive (HCF = 1)",
                    "Yes, scaled 2 × (3, 4, 5)"
                ],
                "answer": 0,
                "hint": "Factor out GCD(10, 24, 26) = 2!",
                "explanation": "10² + 24² = 100 + 576 = 676 = 26², and dividing by 2 reveals primitive parent (5, 12, 13).",
                "solution_steps": [
                    "Check sum of squares: 100 + 576 = 676 = 26² (valid!).",
                    "Find common factor: HCF(10, 24, 26) = 2.",
                    "Divide all terms by 2 → primitive triple (5, 12, 13)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Fermat Lotus Rhombus",
        "subtitle": "Challenge Arena 3 (10 MCQs): Fermat's Last Theorem, Wiles (1994), Bhāskara's Lotus, Missing Legs & Rhombus",
        "questions": [
            {
                "question": "In 1637, Pierre de Fermat conjectured his famous Last Theorem regarding xⁿ + yⁿ = zⁿ. For which exponents n are there NO positive integer solutions (x, y, z)?",
                "options": [
                    "All integers n > 2   (i.e. n = 3, 4, 5, ...)",
                    "All integers n ≥ 2",
                    "Only odd exponents n",
                    "Only n = 2"
                ],
                "answer": 0,
                "hint": "n = 2 has infinite Baudhāyana triples; Fermat's barrier begins strictly above 2!",
                "explanation": "Fermat's Last Theorem states zero positive integer triples solve xⁿ + yⁿ = zⁿ whenever n > 2.",
                "solution_steps": [
                    "Verify n = 2 yields abundant solutions like 3² + 4² = 5².",
                    "Recall Fermat's 1637 margin claim for higher powers n > 2.",
                    "Select n > 2 accurately."
                ]
            },
            {
                "question": "After discovering Fermat's Last Theorem in a library at age 10 in 1963, who finally completed its valid mathematical proof in 1994?",
                "options": [
                    "Andrew Wiles",
                    "Bhāskara II",
                    "Pierre de Fermat",
                    "Pythagoras"
                ],
                "answer": 0,
                "hint": "This breakthrough resolved a 300+ year open problem in 1994!",
                "explanation": "Andrew Wiles proved Fermat's Last Theorem completely in 1994 after 31 years of pursuit since age 10.",
                "solution_steps": [
                    "Note historical timeline: 1637 conjecture → 1963 discovery at age 10 → 1994 resolution.",
                    "Identify Andrew Wiles as the mathematician who completed the proof.",
                    "Confirm 1994 date."
                ]
            },
            {
                "question": "In Bhāskarāchārya's Līlāvatī lotus riddle, the bloom rises 1 cubit above water and meets the surface 3 cubits away when blown by wind. Using 3² + x² = (x + 1)², what is lake depth x?",
                "options": [
                    "4 cubits   (total stem = 5 cubits)",
                    "3 cubits",
                    "5 cubits",
                    "8 cubits"
                ],
                "answer": 0,
                "hint": "Expand 9 + x² = x² + 2x + 1 and cancel x²!",
                "explanation": "9 = 2x + 1 → 2x = 8 → x = 4 cubits (forming a 3-4-5 right triangle).",
                "solution_steps": [
                    "Set up right triangle: depth x, surface drift 3, stem hypotenuse (x + 1).",
                    "Apply theorem: 3² + x² = (x + 1)² = x² + 2x + 1.",
                    "Cancel x²: 9 = 2x + 1 → x = 4 cubits."
                ]
            },
            {
                "question": "Solve a similar Līlāvatī pond problem: a reed stands 1 metre above water and touches the surface 5 metres sideways. Solve 5² + x² = (x + 1)² for water depth x:",
                "options": [
                    "12 metres",
                    "10 metres",
                    "13 metres",
                    "24 metres"
                ],
                "answer": 0,
                "hint": "Expand 25 + x² = x² + 2x + 1 → 25 = 2x + 1!",
                "explanation": "2x = 24 → water depth x = 12 metres (total reed = 13 m: classic 5-12-13 triple!).",
                "solution_steps": [
                    "Set up 5² + x² = (x + 1)².",
                    "Expand: 25 + x² = x² + 2x + 1.",
                    "Solve 2x = 24 → depth x = 12 metres."
                ]
            },
            {
                "question": "Find the missing vertical height reached by a 25 m ladder whose base rests 7 m away from a vertical wall:",
                "options": [
                    "24 m",
                    "18 m",
                    "√674 m",
                    "32 m"
                ],
                "answer": 0,
                "hint": "Compute √(25² − 7²) = √(625 − 49)!",
                "explanation": "h² = 25² − 7² = 625 − 49 = 576 → h = 24 m (7-24-25 triple).",
                "solution_steps": [
                    "Identify hypotenuse c = 25 m and base leg a = 7 m.",
                    "Apply missing-leg subtraction: h² = 25² − 7² = 625 − 49 = 576.",
                    "Take square root: h = √576 = 24 m."
                ]
            },
            {
                "question": "A rhombus has diagonals measuring 24 units and 70 units. What is the perimeter of the entire rhombus?",
                "options": [
                    "148 units   (one side = 37 units × 4)",
                    "37 units",
                    "94 units",
                    "188 units"
                ],
                "answer": 0,
                "hint": "First find one side using half-diagonals 12 and 35 (√(12² + 35²) = 37), then multiply by 4!",
                "explanation": "Half-diagonals 12 and 35 yield side √(144 + 1225) = √1369 = 37; perimeter = 4 × 37 = 148 units.",
                "solution_steps": [
                    "Diagonals bisect at 90°: triangle legs = 24÷2 = 12 and 70÷2 = 35.",
                    "Compute rhombus side: √(12² + 35²) = √1369 = 37 units.",
                    "Multiply 4 equal sides: 4 × 37 = 148 units."
                ]
            },
            {
                "question": "What is the exact diagonal length of a rectangle measuring 20 cm by 21 cm?",
                "options": [
                    "29 cm",
                    "41 cm",
                    "√41 cm",
                    "31 cm"
                ],
                "answer": 0,
                "hint": "Compute √(20² + 21²) = √(400 + 441)!",
                "explanation": "d² = 400 + 441 = 841, and √841 = 29 cm.",
                "solution_steps": [
                    "Rectangle diagonal forms hypotenuse with legs 20 and 21.",
                    "Compute 20² + 21² = 400 + 441 = 841.",
                    "Recognize 29² = 841 → diagonal = 29 cm."
                ]
            },
            {
                "question": "If a rhombus has side length 13 cm and ONE full diagonal measures 10 cm, how long is its SECOND full diagonal?",
                "options": [
                    "24 cm   (half-diagonal = 12 cm → full = 2 × 12)",
                    "12 cm",
                    "26 cm",
                    "16 cm"
                ],
                "answer": 0,
                "hint": "Half of the first diagonal is 5 cm, and rhombus side (hypotenuse) is 13 cm → other half-diagonal = √(13² − 5²)!",
                "explanation": "Half-diagonal 1 = 5 cm, side = 13 cm → half-diagonal 2 = 12 cm → full diagonal 2 = 24 cm.",
                "solution_steps": [
                    "Divide known diagonal by 2: 10 ÷ 2 = 5 cm.",
                    "Solve right triangle leg: √(13² − 5²) = √(169 − 25) = 12 cm.",
                    "Double half-diagonal: 2 × 12 = 24 cm."
                ]
            },
            {
                "question": "Two ships leave harbor together: Ship X sails 15 km due East while Ship Y sails 8 km due North. What is the straight-line distance between them?",
                "options": [
                    "17 km",
                    "23 km",
                    "7 km",
                    "√23 km"
                ],
                "answer": 0,
                "hint": "East and North meet at 90°, forming legs 15 km and 8 km!",
                "explanation": "√(15² + 8²) = √(225 + 64) = √289 = 17 km.",
                "solution_steps": [
                    "Identify perpendicular legs: 15 km East, 8 km North.",
                    "Compute d² = 15² + 8² = 225 + 64 = 289.",
                    "Take square root: d = √289 = 17 km."
                ]
            },
            {
                "question": "A broken bamboo pole snapped at height 9 m above ground, and its tip struck level ground 12 m from its base. What was the original total height of the unbroken pole?",
                "options": [
                    "24 m   (9 m upright + 15 m slanted broken piece)",
                    "15 m",
                    "21 m",
                    "30 m"
                ],
                "answer": 0,
                "hint": "Find the slanted broken part √(9² + 12²) = 15 m, then ADD the standing 9 m part!",
                "explanation": "Slanted piece = √(81 + 144) = 15 m; original total pole = 9 + 15 = 24 m.",
                "solution_steps": [
                    "Compute slanted hypotenuse piece: √(9² + 12²) = 15 m.",
                    "Add unbroken vertical standing stem: 9 m.",
                    "Total pole height = 9 + 15 = 24 m."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Grids Areas Logic",
        "subtitle": "Challenge Arena 4 (10 MCQs): Grid Squares, Equilateral Areas, Converse Tests, Summary & Find the Colours!",
        "questions": [
            {
                "question": "On a 1 cm dot grid, which step offsets (Δx, Δy) construct a tilted square with an EXACT area of 10 sq cm?",
                "options": [
                    "Δx = 3, Δy = 1   (since 3² + 1² = 10)",
                    "Δx = 5, Δy = 5",
                    "Δx = 2, Δy = 2",
                    "Δx = 3, Δy = 2"
                ],
                "answer": 0,
                "hint": "Find two integers whose squares add up to 10!",
                "explanation": "3² + 1² = 9 + 1 = 10, so a tilted segment spanning (3, 1) builds a square of area 10 sq cm.",
                "solution_steps": [
                    "Test sum of two squares Δx² + Δy² = 10.",
                    "Check 3² + 1² = 9 + 1 = 10.",
                    "Reject 2²+2²=8 and 3²+2²=13."
                ]
            },
            {
                "question": "An equilateral triangle has side length s = 8 cm. Splitting it with a perpendicular altitude gives what exact height h and area?",
                "options": [
                    "Height = 4√3 cm; Area = 16√3 sq cm",
                    "Height = 8 cm; Area = 32 sq cm",
                    "Height = 4 cm; Area = 16 sq cm",
                    "Height = 8√3 cm; Area = 32√3 sq cm"
                ],
                "answer": 0,
                "hint": "Right triangle has hypotenuse 8 and half-base 4 → h = √(8² − 4²) = √48 = 4√3!",
                "explanation": "h = √(64 − 16) = √48 = 4√3 cm; Area = (1/2) × 8 × 4√3 = 16√3 sq cm.",
                "solution_steps": [
                    "Drop altitude bisecting base into two halves of 4 cm.",
                    "Compute altitude: h = √(8² − 4²) = √48 = 4√3 cm.",
                    "Compute Area = 1/2 × 8 × 4√3 = 16√3 sq cm."
                ]
            },
            {
                "question": "Which triangle with the given three side lengths is a TRUE 90° right-angled triangle by the converse check a² + b² = c²?",
                "options": [
                    "12 cm, 16 cm, 20 cm",
                    "7 cm, 10 cm, 12 cm",
                    "6 cm, 9 cm, 11 cm",
                    "10 cm, 12 cm, 15 cm"
                ],
                "answer": 0,
                "hint": "Check whether the two smaller squares add up to the largest square!",
                "explanation": "12² + 16² = 144 + 256 = 400 = 20², confirming an exact 90° angle.",
                "solution_steps": [
                    "Test (12, 16, 20): 12² + 16² = 144 + 256 = 400.",
                    "Compare with 20² = 400 — exact equality!",
                    "Notice it equals scaled 4 × (3, 4, 5)."
                ]
            },
            {
                "question": "Three rods measure 5 cm, 7 cm, and 9 cm. What type of largest angle do they form when joined as a triangle?",
                "options": [
                    "Obtuse angle (> 90°), because 5² + 7² = 74 < 9² = 81",
                    "Exact 90° right angle",
                    "Acute angle (< 90°), because 5² + 7² > 9²",
                    "A triangle cannot be formed"
                ],
                "answer": 0,
                "hint": "Compare a² + b² (= 25 + 49) against c² (= 81)!",
                "explanation": "Since a² + b² (74) is smaller than c² (81), the hypotenuse stretched beyond 90°, forcing an obtuse angle.",
                "solution_steps": [
                    "Compute 5² + 7² = 25 + 49 = 74.",
                    "Compute 9² = 81.",
                    "Since 74 < 81 (a² + b² < c²), the largest angle exceeds 90° (obtuse)."
                ]
            },
            {
                "question": "A unit square has side 1. Which statement accurately orders 1, √2, and 2 from smallest to largest?",
                "options": [
                    "1 < √2 < 2   (since 1 < 1.414... < 2)",
                    "√2 < 1 < 2",
                    "1 < 2 < √2",
                    "√2 = 1.5 exactly"
                ],
                "answer": 0,
                "hint": "Recall 1² = 1 < 2 < 4 = 2²!",
                "explanation": "Taking roots across 1 < 2 < 4 establishes 1 < √2 < 2 (approximately 1.414).",
                "solution_steps": [
                    "Compare squares: 1² = 1, (√2)² = 2, 2² = 4.",
                    "Order squares: 1 < 2 < 4.",
                    "Therefore 1 < √2 < 2."
                ]
            },
            {
                "question": "Which set of three squares has exact areas that satisfy Baudhāyana's square-combination equation a² + b² = c²?",
                "options": [
                    "36 sq m, 64 sq m, and 100 sq m",
                    "16 sq m, 25 sq m, and 36 sq m",
                    "9 sq m, 16 sq m, and 36 sq m",
                    "49 sq m, 64 sq m, and 100 sq m"
                ],
                "answer": 0,
                "hint": "Check directly which two areas ADD together to give the third area!",
                "explanation": "36 + 64 = 100 directly (sides 6, 8, 10).",
                "solution_steps": [
                    "Notice areas themselves represent a², b², c² directly.",
                    "Test Option 1: 36 + 64 = 100 (exact match!).",
                    "Sides equal √36 = 6, √64 = 8, √100 = 10."
                ]
            },
            {
                "question": "In the 'Find the Colours!' puzzle, all 3 boxes labeled 'Red', 'Blue', and 'Green' are WRONG. You open the box labeled 'Red' and find a GREEN ball. Which ball sits inside the box labeled 'Green'?",
                "options": [
                    "Blue ball",
                    "Red ball",
                    "Green ball",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "Since Box 'Red' holds Green, remaining balls are Red and Blue—and Box 'Blue' CANNOT hold Blue!",
                "explanation": "Remaining balls for boxes 'Blue' and 'Green' are Red and Blue. Since Box 'Blue' cannot contain Blue, Box 'Blue' holds Red, forcing Box 'Green' to hold Blue!",
                "solution_steps": [
                    "Box 'Red' holds Green (observed).",
                    "Remaining labels 'Blue' and 'Green' must hold Red and Blue.",
                    "Box 'Blue' cannot hold Blue → holds Red; hence Box 'Green' holds Blue."
                ]
            },
            {
                "question": "In the same all-wrong 3-box 'Find the Colours!' puzzle, suppose instead you open Box 'Green' and find a BLUE ball inside. What sits inside Box 'Blue' and Box 'Red'?",
                "options": [
                    "Box 'Blue' holds Red; Box 'Red' holds Green",
                    "Box 'Blue' holds Green; Box 'Red' holds Red",
                    "Box 'Blue' holds Blue; Box 'Red' holds Green",
                    "Need to open a second box"
                ],
                "answer": 0,
                "hint": "Remaining balls are Red and Green, and Box 'Red' CANNOT hold Red!",
                "explanation": "Box 'Red' cannot hold Red → must hold Green! Thus Box 'Blue' holds Red.",
                "solution_steps": [
                    "Box 'Green' contains Blue (observed).",
                    "Remaining colors are Red and Green for boxes 'Red' and 'Blue'.",
                    "Since 'Red' cannot contain Red, 'Red' holds Green and 'Blue' holds Red."
                ]
            },
            {
                "question": "On a square grid, a right triangle has vertical leg 4 units and horizontal leg 3 units. What is the area of the tilted square constructed on its hypotenuse?",
                "options": [
                    "25 sq units",
                    "7 sq units",
                    "5 sq units",
                    "12 sq units"
                ],
                "answer": 0,
                "hint": "Hypotenuse length is 5 units; square area = 3² + 4²!",
                "explanation": "Area = Δx² + Δy² = 3² + 4² = 9 + 16 = 25 sq units.",
                "solution_steps": [
                    "Identify perpendicular step legs: 3 and 4.",
                    "Compute hypotenuse squared: 3² + 4² = 9 + 16 = 25.",
                    "Area of hypotenuse square = 25 sq units."
                ]
            },
            {
                "question": "Which summary statement brings together the central theme of Chapter 9 accurately?",
                "options": [
                    "Right triangles obey a² + b² = c² (c = a√2 for isosceles), generating primitive/scaled integer triples while xⁿ + yⁿ = zⁿ fails for n > 2",
                    "Right triangles satisfy a + b = c for every integer exponent n ≥ 1",
                    "Doubling a square side doubles its area, while √2 = 7/5 exactly",
                    "Baudhāyana proved Fermat's Last Theorem in 1994"
                ],
                "answer": 0,
                "hint": "Verify every core pillar: a² + b² = c², isosceles c = a√2, integer triples, and Fermat's n > 2!",
                "explanation": "This option accurately synthesizes all major theorems, formulas, and historical landmarks of Chapter 9.",
                "solution_steps": [
                    "Check general law a² + b² = c² and isosceles case c = a√2.",
                    "Check primitive/scaled integer triples and Fermat's n > 2 boundary.",
                    "Reject false claims (a+b=c, exact 7/5, misdated Wiles proof)."
                ]
            }
        ]
    }
]

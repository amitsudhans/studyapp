#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 9: The Baudhāyana-Pythagoras Theorem
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 9 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Odd Square Generator",
        "subtitle": "Section 2.5 Algebraic Triple Generation: Consecutive Odd Sums (n-1)² + (2n-1) = n²",
        "speech": (
            "Can we invent brand-new primitive Baudhāyana triples anytime on demand without guessing? YES—using a gorgeous consecutive-odd pattern from Section Two Point Five! Recall from square numbers that adding the nth odd number (2n − 1) to the square (n − 1)² always steps up to the next square n²: algebraically, (n − 1)² + (2n − 1) = n²! "
            "Notice that TWO terms in that identity are ALREADY squares: (n − 1)² and n²! When does the middle term (2n − 1) ALSO turn into a perfect square k²? Simply set 2n − 1 equal to ANY odd square k² (like 9, 25, 49, or 81)! "
            "Watch this algebraic factory run smoothly! Try odd square k² = 9 (= 3²): solve 2n − 1 = 9 → 2n = 10 → n = 5! Plug into (n − 1)² + 3² = n² → 4² + 3² = 5², instantly generating (3, 4, 5)! Try k² = 25 (= 5²): solve 2n − 1 = 25 → n = 13 → 12² + 5² = 13², yielding (5, 12, 13)! Try k² = 49 (= 7²): solve 2n − 1 = 49 → n = 25 → 24² + 7² = 25², cleanly producing (7, 24, 25) and infinite triples beyond!"
        ),
        "checkpoints": [
            {
                "question": "Using the odd-square identity (n − 1)² + (2n − 1) = n², set (2n − 1) = 81 (= 9²). Which primitive triple is generated?",
                "options": [
                    "(9, 40, 41)",
                    "(9, 80, 81)",
                    "(9, 41, 42)",
                    "(8, 15, 17)"
                ],
                "answer": 0,
                "hint": "Solve 2n − 1 = 81 → 2n = 82 → n = 41, so n − 1 = 40!",
                "explanation": "With n = 41, (41 − 1)² + 81 = 41² gives 40² + 9² = 41², generating primitive triple (9, 40, 41)."
            },
            {
                "question": "Which odd numbers (2n − 1) can be chosen in (n − 1)² + (2n − 1) = n² to produce an integer right-triangle triple?",
                "options": [
                    "Any odd number that is itself a perfect square (9, 25, 49, 81, ...)",
                    "Any even number greater than 4",
                    "Every prime number",
                    "Only multiples of 10"
                ],
                "answer": 0,
                "hint": "All three terms in the identity must be perfect integer squares: a² + b² = c²!",
                "explanation": "Setting 2n − 1 = k² for any odd integer k ≥ 3 guarantees three integer squares: k² + (n − 1)² = n²."
            }
        ]
    },
    {
        "id": 10,
        "title": "Fermat Last Theorem",
        "subtitle": "Section 2.6 Open Problem: Pierre de Fermat's Conjecture (x^n + y^n = z^n, n > 2) & Andrew Wiles (1994)",
        "speech": (
            "We just saw infinite integer solutions to x² + y² = z²! Naturally, seventeenth-century French mathematician Pierre de Fermat asked an irresistible follow-up question in Section Two Point Six: what happens when we change exponent 2 to exponent 3, exponent 4, or ANY whole integer power n GREATER than 2? Could three positive whole integers EVER satisfy x³ + y³ = z³, or more generally xⁿ + yⁿ = zⁿ for n > 2? "
            "Around 1637, Fermat famously scribbled a tantalizing Latin note inside the narrow margin of his arithmetic book claiming NO positive integer solutions exist for any n > 2—remarking playfully that the page margin was simply too narrow to contain his truly marvelous proof! "
            "For over three full centuries, brilliant mathematicians everywhere hunted desperately for that missing proof, earning it the legendary name FERMAT'S LAST THEOREM! In 1963, a ten-year-old British schoolboy named Andrew Wiles stumbled across this exact historic riddle in a local public library and dreamed of solving it! Three decades later, after seven years of intense secret focused research using deep modern mathematics, Andrew Wiles stunned the entire mathematical world in 1994 by finally proving Fermat's 300-year-old theorem completely true!"
        ),
        "checkpoints": [
            {
                "question": "What does Fermat's Last Theorem state about the equation xⁿ + yⁿ = zⁿ for positive integers x, y, z?",
                "options": [
                    "It has NO positive integer solutions for any integer exponent n > 2",
                    "It has infinite integer solutions for n = 3",
                    "It only fails when n = 2",
                    "It holds only for even numbers x, y, z"
                ],
                "answer": 0,
                "hint": "Contrast exponent n = 2 (infinite triples) against n ≥ 3!",
                "explanation": "While x² + y² = z² has infinitely many integer triples, Fermat conjectured (and Wiles proved) zero positive integer solutions exist for n > 2."
            },
            {
                "question": "Which mathematician first stumbled on Fermat's Last Theorem at age 10 in 1963 and finally completed its formal proof in 1994?",
                "options": [
                    "Andrew Wiles",
                    "Euclid",
                    "Baudhāyana",
                    "Bhāskarāchārya"
                ],
                "answer": 0,
                "hint": "Look at Section 2.6's 1963 → 1994 milestone resolution!",
                "explanation": "Andrew Wiles read the problem as a 10-year-old in 1963 and solved the 350-year puzzle in 1994."
            }
        ]
    },
    {
        "id": 11,
        "title": "Bhaskara Lotus Riddle",
        "subtitle": "Section 2.7 Further Applications: Bhāskarāchārya's Līlāvatī Lotus Stem Riddle & Lake Depth Equation",
        "speech": (
            "Enter Section Two Point Seven to see the Baudhāyana-Pythagoras Theorem solving clever geometric riddles and engineering challenges! Begin with the poetic lotus puzzle composed by medieval Indian mathematician Bhāskarāchārya (Bhāskara II) inside his classic masterpiece Līlāvatī! "
            "Picture a calm pond whose hidden water depth equals unknown x cubits! A single lotus flower stands upright directly from the muddy lakebed, rising gracefully 1 cubit straight ABOVE the water's surface—meaning total rigid stem length equals (x + 1) cubits! Suddenly a steady breeze blows the stem smoothly sideways without bending until the flower's bloom touches the water's surface 3 cubits horizontally away from its upright spot! How deep is the lake? "
            "Sketch the crisp underwater right triangle cleanly! Its vertical leg equals hidden water depth x, its horizontal water-surface leg equals 3 cubits, and its slanted hypotenuse equals the full rigid unbroken stem (x + 1)! Apply Baudhāyana's law immediately: 3² + x² = (x + 1)²! Expand the right-hand algebraic square cleanly: 9 + x² = x² + 2x + 1! Notice x² cancels neatly off BOTH sides, leaving 9 = 2x + 1 → 2x = 8 → lake depth x = 4 cubits cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In Bhāskarāchārya's Līlāvatī lotus riddle (3² + x² = (x + 1)²), what depth x of the lake and total stem length (x + 1) follow?",
                "options": [
                    "Lake depth x = 4 units; total stem = 5 units",
                    "Lake depth x = 3 units; total stem = 4 units",
                    "Lake depth x = 5 units; total stem = 6 units",
                    "Lake depth x = 8 units; total stem = 9 units"
                ],
                "answer": 0,
                "hint": "Expand (x + 1)² = x² + 2x + 1 and cancel x² from both sides of 9 + x² = x² + 2x + 1!",
                "explanation": "9 + x² = x² + 2x + 1 simplifies to 2x = 8 → x = 4 cubits, forming classic (3, 4, 5) triple!"
            },
            {
                "question": "Suppose another lotus sticks 2 metres straight above a pond and touches water 6 metres horizontally from its stem spot. Using 6² + x² = (x + 2)², find the pond depth x:",
                "options": [
                    "8 metres   (36 = 4x + 4 → x = 8)",
                    "6 metres",
                    "10 metres",
                    "4 metres"
                ],
                "answer": 0,
                "hint": "Expand (x + 2)² = x² + 4x + 4, cancel x², and solve 36 = 4x + 4!",
                "explanation": "36 + x² = x² + 4x + 4 → 4x = 32 → x = 8 metres (forming triple 6, 8, 10!)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Diagonals Rhombus Practice",
        "subtitle": "Section 2.7 Figure it Out: Missing Triangle Legs, Rectangle Diagonals & Rhombus Edge (24 & 70)",
        "speech": (
            "Now tackle the geometric Figure it Out exercises inside Section Two Point Seven! Notice carefully: what if we already know hypotenuse c and ONE leg a, and need the MISSING leg b? Rearrange a² + b² = c² by subtraction cleanly: b² = c² − a², so b = √(c² − a²)! For example, a 13-metre ladder leaning 5 metres from a wall reaches height √(13² − 5²) = √(169 − 25) = √144 = 12 metres! Similarly, any rectangle of sides l and w holds diagonal d = √(l² + w²)! "
            "Apply this cleanly to the celebrated NCERT RHOMBUS EDGE PROBLEM! Suppose a rhombus has perpendicular diagonals measuring 24 units and 70 units! Recall a key quadrilateral fact from earlier chapters: the two diagonals of ANY rhombus bisect each other cleanly at EXACT ninety-degree right angles! "
            "Slice along those diagonals: the rhombus divides into four congruent right-angled triangles meeting at the center! Each leg equals HALF of a full diagonal: half of 24 = 12 units, and half of 70 = 35 units! Compute outer rhombus side s immediately: s² = 12² + 35² = 144 + 1225 = 1369 → side s = √1369 = 37 units!"
        ),
        "checkpoints": [
            {
                "question": "The diagonals of a rhombus measure 24 cm and 70 cm. What is the exact length of each outer side of the rhombus?",
                "options": [
                    "37 cm   (legs 12 cm and 35 cm → √(12² + 35²) = √1369)",
                    "74 cm",
                    "47 cm",
                    "94 cm"
                ],
                "answer": 0,
                "hint": "Diagonals bisect at 90°, so use HALF-diagonals 12 and 35 as legs!",
                "explanation": "12² + 35² = 144 + 1225 = 1369 = 37², giving side length 37 cm (primitive triple 12-35-37!)."
            },
            {
                "question": "A right-angled triangle has hypotenuse c = 17 cm and one leg a = 8 cm. What is the missing leg b?",
                "options": [
                    "15 cm   (b = √(17² − 8²))",
                    "9 cm",
                    "25 cm",
                    "√353 cm"
                ],
                "answer": 0,
                "hint": "Subtract squares carefully: c² − a² = 289 − 64!",
                "explanation": "b² = 17² − 8² = 289 − 64 = 225, so b = √225 = 15 cm."
            }
        ]
    },
    {
        "id": 13,
        "title": "Grid Squares Areas",
        "subtitle": "Section 2.7 Figure it Out: Constructing Tilted Grid Squares (Δx² + Δy²) & Equilateral Triangle Areas",
        "speech": (
            "Explore two creative geometric challenges from Section Two Point Seven's Figure it Out! First: GRID SQUARE CONSTRUCTIONS! On an ordinary 1-centimetre square grid, horizontal and vertical squares only produce square-number areas like 1, 4, 9, and 16! How can you draw exact squares of areas 2, 5, 8, 10, or 13 square centimetres right on grid dots? "
            "Tilt your edge along a right triangle step (Δx horizontally, Δy vertically)! By Baudhāyana's theorem, that slanted edge squared equals Δx² + Δy²! Step across 1 right and 2 up (Δx = 1, Δy = 2) to build a tilted square of exact area 1² + 2² = 5 sq cm! Step across 2 and 3 (Δx = 2, Δy = 3) to capture area 2² + 3² = 13 sq cm effortlessly! "
            "Second: EQUILATERAL TRIANGLE HEIGHT AND AREA! Drop an altitude perpendicular from the top vertex of an equilateral triangle of side s down to its midpoint base! That cuts two congruent right triangles with hypotenuse s and base leg s/2! By Baudhāyana, height h = √(s² − (s/2)²) = √(3s²/4) = (√3 / 2)s, giving Area = 1/2 × base × height = (√3 / 4)s²!"
        ),
        "checkpoints": [
            {
                "question": "On a 1 cm unit grid, a tilted square edge runs from (0, 0) to (3, 2) (Δx = 3, Δy = 2). What exact area does that tilted square enclose?",
                "options": [
                    "13 sq cm   (3² + 2² = 9 + 4)",
                    "5 sq cm",
                    "25 sq cm",
                    "6 sq cm"
                ],
                "answer": 0,
                "hint": "The tilted edge is the hypotenuse of a right triangle with legs 3 and 2!",
                "explanation": "Edge length squared = 3² + 2² = 13, so the square built on that edge has exact area 13 sq cm."
            },
            {
                "question": "An equilateral triangle has side s = 10 cm. Dropping its vertical altitude splits the base into two halves of 5 cm. What is its exact height h?",
                "options": [
                    "√75 cm = 5√3 cm   (since h² = 10² − 5²)",
                    "5 cm",
                    "10 cm",
                    "√125 cm"
                ],
                "answer": 0,
                "hint": "Solve right triangle with hypotenuse 10 cm and base leg 5 cm: h² + 5² = 10²!",
                "explanation": "h² = 100 − 25 = 75, so h = √75 = 5√3 cm, giving Area = 25√3 sq cm."
            }
        ]
    },
    {
        "id": 14,
        "title": "Right Angle Converse",
        "subtitle": "Unified Verification: Testing 90° Corners via a² + b² = c² vs Acute/Obtuse Violations",
        "speech": (
            "Now unify geometric theory with practical building carpentry! How did ancient altar engineers and modern surveyors check whether two long walls truly meet at an exact ninety-degree corner without giant metal protractors? They used knotted cords marked in Baudhāyana triple ratios—especially 3, 4, 5 or 5, 12, 13—relying on the CONVERSE of Baudhāyana's theorem! "
            "State the converse clearly: if a triangle with longest side c satisfies a² + b² = c², then the angle sitting opposite side c MUST equal an EXACT ninety-degree right angle! Whenever the equality breaks, the angle is NOT ninety degrees! Test carefully: suppose three sticks measure 4 cm, 5 cm, and 6 cm! Compute 4² + 5² = 16 + 25 = 41, while longest side squared is 6² = 36! Since 41 differs from 36 (in fact a² + b² > c²), the largest angle shrinks acute—strictly LESS than ninety degrees! "
            "Test 4 cm, 5 cm, and 7 cm next! Compute 16 + 25 = 41 versus 7² = 49! Here a² + b² < c², stretching the opposite angle wide and obtuse—GREATER than ninety degrees! Only exact equality a² + b² = c² cleanly locks a true ninety-degree right corner!"
        ),
        "checkpoints": [
            {
                "question": "Three wooden beams measure 9 cm, 12 cm, and 15 cm. Test whether joining their ends forms an exact 90° right-angled triangle:",
                "options": [
                    "Yes — exact 90° corner because 9² + 12² = 81 + 144 = 225 = 15²",
                    "No — 9 + 12 > 15 makes it impossible",
                    "No — 9² + 12² = 200 ≠ 225",
                    "It forms an obtuse triangle"
                ],
                "answer": 0,
                "hint": "Notice (9, 12, 15) = 3 × (3, 4, 5)! Check 9² + 12² against 15²!",
                "explanation": "81 + 144 = 225 = 15², satisfying a² + b² = c² cleanly and confirming a 90° right triangle."
            },
            {
                "question": "Which set of side lengths does NOT form a right-angled triangle?",
                "options": [
                    "(5, 6, 8)   (since 25 + 36 = 61 ≠ 64)",
                    "(7, 24, 25)",
                    "(8, 15, 17)",
                    "(6, 8, 10)"
                ],
                "answer": 0,
                "hint": "Compute a² + b² vs c² for the largest side c in every triple!",
                "explanation": "5² + 6² = 61 ≠ 8² = 64, whereas (7,24,25), (8,15,17), and (6,8,10) all satisfy a² + b² = c²."
            }
        ]
    },
    {
        "id": 15,
        "title": "Chapter Formula Summary",
        "subtitle": "Chapter Summary Consolidation: a² + b² = c², c = a√2, √2 Irrationality, Triples & Fermat",
        "speech": (
            "Pause here cleanly to synthesize all five pillars of Chapter Nine: The Baudhāyana-Pythagoras Theorem onto one crisp reference summary! First, SQUARE DOUBLING AND HALVING: doubling side length multiplies area by 4, whereas building on the diagonal doubles area (Verse 1.9); conversely, joining side midpoints builds inscribed square PQRS holding exact half-area! "
            "Second, ISOSCELES RIGHT TRIANGLE AND ROOT TWO: unit legs (1, 1) yield hypotenuse √2, and equal legs a give c = a√2 (c² = 2a²)! Tight decimal bounds squeeze 1.414 < √2 < 1.415, terminating decimal squares never end in 0, and Euclid's 2n² = m² prime-factor parity contradiction proves √2 is irrational! "
            "Third, GENERAL THEOREM AND PROOF: in every right triangle, a² + b² = c² (Verse 1.12), proved visually via Verse 2.1's rectangle dissection and rearrangement! "
            "Fourth, INTEGER TRIPLES AND GENERATORS: Verse 1.13 triples (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25) scale as (ka, kb, kc) and generate endlessly from odd squares 2n − 1 = k²! "
            "Fifth, FERMAT AND PRACTICAL APPLICATIONS: xⁿ + yⁿ = zⁿ has no positive integer solutions for n > 2 (Wiles 1994), while Baudhāyana powers Bhāskara's lotus riddle, rhombus diagonals, and tilted grid squares!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement accurately pairs Baudhāyana's core equations for right triangles and isosceles right triangles?",
                "options": [
                    "General right triangle: a² + b² = c²; Isosceles right triangle (legs a): c² = 2a², so c = a√2",
                    "General right triangle: a + b = c; Isosceles: c = 2a",
                    "General: a² + b² = 2c²; Isosceles: c = a/√2",
                    "General: a² − b² = c²; Isosceles: c = a²"
                ],
                "answer": 0,
                "hint": "When b = a in a² + b² = c², notice a² + a² = 2a²!",
                "explanation": "General legs satisfy a² + b² = c², which simplifies to c² = 2a² (c = a√2) whenever both legs equal a."
            },
            {
                "question": "Which key summary proof demonstrates why √2 cannot be written as ANY rational fraction m/n?",
                "options": [
                    "In 2n² = m², the prime factor 2 appears an odd number of times on the LHS and an even number on the RHS",
                    "Because 2 is smaller than 4",
                    "Because decimals stop after 3 places",
                    "Because Baudhāyana triples always use integers"
                ],
                "answer": 0,
                "hint": "Remember Euclid's prime-factor-2 parity contradiction from Elements!",
                "explanation": "Every square holds an even count of 2s, making 2n² odd-count vs m² even-count — impossible for integers."
            }
        ]
    },
    {
        "id": 16,
        "title": "Find The Colours",
        "subtitle": "It's Puzzle Time! Find the Colours!: Three Mislabelled Boxes (Red, Blue, Green) Single-Peek Deduction",
        "speech": (
            "Conclude Chapter Nine with the sharp deductive challenge: IT'S PUZZLE TIME—FIND THE COLOURS! Picture three closed wooden boxes standing side by side on a table! One holds a RED ball, one holds a BLUE ball, and one holds a GREEN ball! Look at their front labels: 'Red', 'Blue', and 'Green'—but EVERY SINGLE LABEL IS WRONG! Not a single box matches the label written on its lid! "
            "Your puzzle rule: you are allowed to open ONLY ONE BOX and look at its single ball, after which you must announce the true contents of ALL THREE boxes with total certainty! Which box should you open? "
            "Watch pure logical elimination work cleanly—remarkably, opening ANY single box solves the whole puzzle in just two deductive steps! Suppose you choose to open the box labeled 'Red' and spot a BLUE ball inside! Think carefully: which color must lie inside the box labeled 'Green'? It CANNOT hold Green (remember every single label is wrong!), and it CANNOT hold Blue (Blue already sits inside the 'Red' box)! Therefore, the 'Green' box MUST hold RED! That leaves ONLY Green for the box labeled 'Blue'! Test every case cleanly on our interactive three-box simulator!"
        ),
        "checkpoints": [
            {
                "question": "All three boxes ('Red', 'Blue', 'Green') are mislabeled (none matches its label). You open ONLY the box labeled 'Blue' and find a RED ball inside. What are the true contents of boxes 'Red' and 'Green'?",
                "options": [
                    "Box 'Red' holds Green; Box 'Green' holds Blue",
                    "Box 'Red' holds Blue; Box 'Green' holds Green",
                    "Box 'Red' holds Red; Box 'Green' holds Green",
                    "Impossible to determine without opening two boxes"
                ],
                "answer": 0,
                "hint": "Since every label is wrong, Box 'Green' CANNOT hold Green and cannot hold Red (already found in 'Blue')!",
                "explanation": "Box 'Green' cannot contain Green or Red → must hold Blue! Thus remaining Box 'Red' holds Green."
            },
            {
                "question": "When three distinct labels ('Red', 'Blue', 'Green') are ALL placed on the WRONG boxes, how many possible mislabeled arrangements exist, and why does peeking inside ANY single box break the tie immediately?",
                "options": [
                    "Exactly 2 completely wrong arrangements exist, and any single box holds two different balls across them",
                    "6 arrangements exist, requiring at least 3 boxes opened",
                    "3 arrangements exist, requiring 2 boxes opened",
                    "Only 1 arrangement exists"
                ],
                "answer": 0,
                "hint": "List the derangements of (R, B, G): (B, G, R) and (G, R, B)!",
                "explanation": "Only two derangements exist: (R→B, B→G, G→R) and (R→G, G→B, B→R). Checking any single box uniquely identifies which one is active."
            }
        ]
    }
]

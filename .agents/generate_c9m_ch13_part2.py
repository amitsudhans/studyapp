#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 13: Two Variables, One Line
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Elimination Solving Method",
        "subtitle": "Section 13.5.1 Algebraic Methods: Coefficient Matching & Elimination Method",
        "speech": (
            "On Slide Nine, we master Method Two inside Section Thirteen Point Five Point One: THE ELIMINATION METHOD! "
            "When neither variable has coefficient one, substitution creates messy fractions! Elimination avoids fractions "
            "completely by matching the coefficient of one variable and adding or subtracting the equations! "
            "Test this on two equations: Equation One is three x plus two y equals nineteen, and Equation Two is five x "
            "minus three y equals nineteen! Suppose we want to eliminate y! The coefficients of y are plus two and "
            "minus three, whose least common multiple is six! "
            "Step One: Multiply every term of Equation One by three to get nine x plus six y equals fifty-seven! "
            "Multiply every term of Equation Two by two to get ten x minus six y equals thirty-eight! "
            "Step Two: Because plus six y and minus six y have OPPOSITE signs, ADD the two scaled equations vertically! "
            "The y-terms cancel to zero! Nine x plus ten x equals nineteen x, and fifty-seven plus thirty-eight equals "
            "ninety-five! Dividing by nineteen gives x equals five! "
            "Step Three: Substitute x equals five into three x plus two y equals nineteen: fifteen plus two y equals "
            "nineteen, so y equals two! Solution: (5, 2)!"
        ),
        "checkpoints": [
            {
                "question": "To eliminate y from 4x + 3y = 18 and 5x − 6y = 3 without fractions, what is the cleanest first step?",
                "options": [
                    "Multiply the first equation by 2, then ADD the two equations",
                    "Multiply the first equation by 5 and subtract",
                    "Divide both equations by 3",
                    "Set y = 0 in both equations",
                ],
                "answer": 0,
                "hint": "Multiplying 4x + 3y = 18 by 2 turns +3y into +6y, which cancels −6y on addition!",
                "explanation": "8x + 6y = 36 added to 5x − 6y = 3 gives 13x = 39 ⇒ x = 3, y = 2.",
            },
            {
                "question": "Solve by elimination: 2x + y = 11 and 2x − y = 5. What is (x, y)?",
                "options": ["(4, 3)", "(3, 4)", "(5, 1)", "(8, 3)"],
                "answer": 0,
                "hint": "Add the two equations directly to eliminate y!",
                "explanation": "Adding gives 4x = 16 ⇒ x = 4; then 2(4) + y = 11 ⇒ y = 3.",
            },
        ],
    },
    {
        "id": 10,
        "title": "Algebraic Solution Criteria",
        "subtitle": "Section 13.5.1 Algebraic Solvability Rules: Coefficient Ratio Tests",
        "speech": (
            "Before spending five minutes solving a system, wouldn't it be wonderful to know INSTANTLY whether it has "
            "one solution, infinitely many solutions, or NO solution at all? Inside Section Thirteen Point Five Point "
            "One, COEFFICIENT RATIO CRITERIA give you X-ray vision into any system a one x plus b one y plus c one "
            "equals zero and a two x plus b two y plus c two equals zero! "
            "Case One—UNIQUE SOLUTION: If a one over a two is NOT EQUAL to b one over b two, the two lines have "
            "different slopes, so they MUST cross at exactly ONE point! Example: two x plus three y equals seven and "
            "four x minus y equals five, since two-fourths does not equal three over minus one! "
            "Case Two—INFINITELY MANY SOLUTIONS: If ALL THREE ratios match—a one over a two equals b one over b two "
            "equals c one over c two—the second equation is simply a scaled copy of the first! Both equations describe "
            "the exact same line, sharing infinitely many solutions! "
            "Case Three—NO SOLUTION: If a one over a two equals b one over b two, BUT does NOT equal c one over c two, "
            "the lines share the same slope yet have different intercepts—meaning parallel lines that NEVER meet!"
        ),
        "checkpoints": [
            {
                "question": "Without solving, classify the system: 2x + 3y = 8 and 4x + 6y = 15.",
                "options": [
                    "No solution (a₁/a₂ = b₁/b₂ ≠ c₁/c₂)",
                    "Unique solution",
                    "Infinitely many solutions",
                    "Exactly two solutions",
                ],
                "answer": 0,
                "hint": "Compare 2/4, 3/6, and 8/15!",
                "explanation": "2/4 = 3/6 = 1/2, whereas 8/15 ≠ 1/2, so the lines are parallel with no solution.",
            },
            {
                "question": "For what value of k does the system kx + 2y = 5 and 6x + 4y = 10 have infinitely many solutions?",
                "options": ["k = 3", "k = 2", "k = 6", "k = 12"],
                "answer": 0,
                "hint": "Set k/6 = 2/4 = 5/10!",
                "explanation": "2/4 = 5/10 = 1/2, so k/6 = 1/2 gives k = 3.",
            },
        ],
    },
    {
        "id": 11,
        "title": "History Linear Systems",
        "subtitle": "Section 13.5.1 A Pinch of History: Babylon, Nine Chapters (Fangcheng), Āryabhaṭa & Brahmagupta",
        "speech": (
            "Take a fascinating journey through time inside Section Thirteen Point Five Point One: A PINCH OF HISTORY! "
            "Long before modern x and y symbols existed, ancient civilisations invented brilliant ways to solve systems "
            "of linear equations! "
            "Around two thousand BCE, BABYLONIAN clay tablets recorded word problems about fields, weights, and silver "
            "equivalent to two linear equations in two unknowns—solved by clever verbal balancing recipes! "
            "Two millennia later, in Han Dynasty China, the classic mathematical treatise THE NINE CHAPTERS ON THE "
            "MATHEMATICAL ART introduced FANGCHENG—literally rectangular arrays! Mathematicians arranged coefficients "
            "as red and black counting rods on a grid and eliminated columns step by step, inventing matrix row "
            "reduction and negative-number arithmetic eighteen hundred years before Carl Friedrich Gauss! "
            "Meanwhile, in India, ĀRYABHAṬA in four hundred ninety-nine CE and BRAHMAGUPTA in six hundred twenty-eight "
            "CE developed systematic rules for solving multi-unknown linear problems in astronomy, commerce, and integer "
            "equations—known as kuttaka and avyakta-ganita, the mathematics of unknowns! These classical Indian works "
            "showed how to isolate and balance multiple unknowns step by step without modern symbols! Modern linear "
            "algebra, scientific engineering simulations, and computer spreadsheets descend directly from these ancient Babylonian, "
            "Chinese counting-rod, and classical Sanskrit traditions!"
        ),
        "checkpoints": [
            {
                "question": "What ancient Chinese method in 'The Nine Chapters on the Mathematical Art' used counting rods in rectangular arrays to eliminate variables?",
                "options": [
                    "Fangcheng (rectangular array elimination)",
                    "Euclidean compass bisection",
                    "Monte Carlo dartboards",
                    "Cartesian graphing",
                ],
                "answer": 0,
                "hint": "Its name literally means 'rectangular arrays'!",
                "explanation": "Fangcheng arranged linear system coefficients in rod arrays and performed systematic column elimination.",
            },
            {
                "question": "Which two classical Indian mathematicians (499 CE and 628 CE) developed systematic methods for solving multi-unknown linear problems?",
                "options": [
                    "Āryabhaṭa and Brahmagupta",
                    "Euclid and Archimedes",
                    "Newton and Leibniz",
                    "Gauss and Euler",
                ],
                "answer": 0,
                "hint": "They wrote the Āryabhaṭīya (499 CE) and Brāhmasphuṭasiddhānta (628 CE)!",
                "explanation": "Āryabhaṭa (499 CE) and Brahmagupta (628 CE) advanced systematic linear and indeterminate equation solving.",
            },
        ],
    },
    {
        "id": 12,
        "title": "Graphical System Analysis",
        "subtitle": "Section 13.6 Graphical Method for Solving a Pair of Linear Equations",
        "speech": (
            "Welcome to Section Thirteen Point Six: THE GRAPHICAL METHOD FOR SOLVING A PAIR OF LINEAR EQUATIONS! When "
            "we plot BOTH equations a one x plus b one y plus c one equals zero AND a two x plus b two y plus c two "
            "equals zero on the SAME Cartesian coordinate plane, geometry reveals the algebra before our eyes! "
            "Every point on Line One satisfies Equation One, and every point on Line Two satisfies Equation Two! "
            "Therefore, a point (x, y) solves BOTH equations simultaneously if and only if it lies on BOTH lines at once! "
            "Three and ONLY three geometric configurations can occur for two straight lines in a plane! "
            "First, INTERSECTING LINES: the two lines cross at a single point P(x naught, y naught), giving a UNIQUE "
            "SOLUTION and a consistent system! "
            "Second, PARALLEL LINES: the two lines keep a constant gap and never meet anywhere, giving NO SOLUTION and "
            "an inconsistent system! "
            "Third, COINCIDENT LINES: one line lies completely on top of the other, so EVERY point on the line is "
            "shared, giving INFINITELY MANY SOLUTIONS and a dependent consistent system! Use the simulator to drag "
            "coefficients and watch algebraic ratios match geometric intersections live!"
        ),
        "checkpoints": [
            {
                "question": "If the graphs of two linear equations in two variables are coincident (overlapping identical lines), how many solutions does the system have?",
                "options": [
                    "Infinitely many solutions",
                    "Exactly one solution",
                    "No solution",
                    "Exactly two solutions",
                ],
                "answer": 0,
                "hint": "Every single point on the shared line satisfies both equations!",
                "explanation": "Coincident lines share all infinitely many points along the line.",
            },
            {
                "question": "A linear system is called 'inconsistent' when its two lines are:",
                "options": [
                    "Parallel with no point of intersection",
                    "Intersecting at the origin (0, 0)",
                    "Perpendicular at (3, 4)",
                    "Coincident",
                ],
                "answer": 0,
                "hint": "Inconsistent means no common solution exists!",
                "explanation": "Parallel lines never intersect, so there is no (x, y) satisfying both equations simultaneously.",
            },
        ],
    },
    {
        "id": 13,
        "title": "Ramp Gradient Temperature",
        "subtitle": "Exercises 13.1–13.3: Wheelchair Accessibility Ramp Gradients & Celsius–Fahrenheit Scale",
        "speech": (
            "Now apply our toolkit to flagship problems from Exercises Thirteen Point One through Thirteen Point Three! "
            "First, look at WHEELCHAIR ACCESSIBILITY RAMPS! Building safety codes specify a maximum ramp gradient "
            "(slope) of one in twelve—meaning for every one metre of vertical rise, the ramp must provide at least "
            "twelve metres of horizontal run! Written as a linear equation from the ground origin, height y equals "
            "(one over twelve) times horizontal distance x! If a doorway sits zero point six metres above the pavement, "
            "solving zero point six equals x over twelve immediately demands a minimum horizontal ramp run of seven "
            "point two metres! "
            "Second, explore TEMPERATURE CONVERSION between Celsius C and Fahrenheit F: F equals (nine over five) C "
            "plus thirty-two! Notice this is already in slope-intercept form y equals m x plus d, with slope nine-fifths "
            "and F-intercept thirty-two! What temperature reads the EXACT SAME number on both thermometers? Set F "
            "equals C: C equals (nine over five) C plus thirty-two! Subtracting C gives four-fifths C equals minus "
            "thirty-two, solving cleanly to minus forty degrees—where minus forty Celsius equals minus forty Fahrenheit "
            "on both scales simultaneously, a famous crossover point on our interactive temperature graph!"
        ),
        "checkpoints": [
            {
                "question": "A wheelchair ramp has maximum allowed slope m = 1/12. To climb a vertical rise of 0.5 m safely, what minimum horizontal run is required?",
                "options": ["6.0 m", "4.0 m", "12.0 m", "2.4 m"],
                "answer": 0,
                "hint": "Use Slope = Rise / Run, so 1/12 = 0.5 / Run!",
                "explanation": "Run = 0.5 × 12 = 6.0 metres.",
            },
            {
                "question": "Using F = (9/5)C + 32, at what temperature do the Celsius and Fahrenheit scales show the exact same numerical reading?",
                "options": ["−40°", "0°", "32°", "−273°"],
                "answer": 0,
                "hint": "Set F = C in F = (9/5)C + 32 and solve for C!",
                "explanation": "C = (9/5)C + 32 ⇒ −(4/5)C = 32 ⇒ C = −40°.",
            },
        ],
    },
    {
        "id": 14,
        "title": "Ancient Puzzles Plans",
        "subtitle": "Exercises 13.4–13.5: Mahāvīrāchārya's Gaṇita Sāra Saṅgraha & Mobile Plan Thresholds",
        "speech": (
            "On Slide Fourteen, we tackle two brilliant problem types from Exercises Thirteen Point Four and Thirteen "
            "Point Five! First, travel back to c. eight hundred fifty CE and MAHĀVĪRĀCHĀRYA'S GAṆITA SĀRA SAṄGRAHA! "
            "One famous puzzle asks: Two merchants carry unknown amounts of money x and y! If the first receives one "
            "hundred coins from the second, he becomes twice as rich as the second: x plus one hundred equals two times "
            "(y minus one hundred)! If instead the second receives ten coins from the first, he becomes six times as "
            "rich as the first: y plus ten equals six times (x minus ten)! Expanding both gives x minus two y equals "
            "minus three hundred and six x minus y equals seventy, which solves cleanly by elimination to x equals "
            "forty and y equals one hundred seventy! "
            "Second, compare MOBILE DATA PLANS! Plan A charges two hundred rupees fixed plus two rupees per gigabyte: "
            "y equals two x plus two hundred! Plan B charges one hundred rupees fixed plus four rupees per gigabyte: "
            "y equals four x plus one hundred! Setting them equal gives two x equals one hundred, so x equals fifty "
            "gigabytes—the exact break-even crossover threshold!"
        ),
        "checkpoints": [
            {
                "question": "Plan A costs ₹200 + ₹2/GB and Plan B costs ₹100 + ₹4/GB. At how many GB do both plans cost the exact same?",
                "options": ["50 GB", "25 GB", "100 GB", "75 GB"],
                "answer": 0,
                "hint": "Set 2x + 200 = 4x + 100 and solve for x!",
                "explanation": "200 − 100 = 4x − 2x ⇒ 100 = 2x ⇒ x = 50 GB (both cost ₹300).",
            },
            {
                "question": "In Mahāvīrāchārya's puzzle, if A gets ₹100 from B then A + 100 = 2(B − 100). Which standard linear equation is this?",
                "options": [
                    "A − 2B + 300 = 0",
                    "A − 2B − 100 = 0",
                    "A + 2B = 300",
                    "2A − B = 100",
                ],
                "answer": 0,
                "hint": "Expand 2(B − 100) = 2B − 200 and bring all terms to the left!",
                "explanation": "A + 100 = 2B − 200 ⇒ A − 2B + 300 = 0.",
            },
        ],
    },
    {
        "id": 15,
        "title": "Angles Trains Systems",
        "subtitle": "End-of-Chapter Exercises: Cyclic Quadrilateral Angles & Train Speed/Distance Systems",
        "speech": (
            "Welcome to Slide Fifteen, solving two classic end-of-chapter linear system applications! First, remember "
            "from geometry that opposite angles of a CYCLIC QUADRILATERAL sum to one hundred eighty degrees! Suppose "
            "opposite angles are given algebraically as angle A equals four y plus twenty, angle C equals minus four x, "
            "angle B equals three y minus five, and angle D equals minus seven x plus five! Setting angle A plus "
            "angle C equals one hundred eighty and angle B plus angle D equals one hundred eighty creates a clean "
            "two-variable linear system! Simplifying gives y minus x equals forty and three y minus seven x equals "
            "one hundred eighty—solving by elimination to x equals minus fifteen and y equals twenty-five! "
            "Second, solve a TRAIN SPEED-DISTANCE SYSTEM! Two stations A and B are one hundred kilometres apart! When "
            "two trains start simultaneously in the SAME direction, they meet in five hours, so relative speed is "
            "u minus v equals one hundred over five, which is twenty! When they travel TOWARD each other, they meet in "
            "one hour, so u plus v equals one hundred! Adding both equations gives two u equals one hundred twenty, "
            "so u equals sixty and v equals forty kilometres per hour!"
        ),
        "checkpoints": [
            {
                "question": "Two trains 120 km apart meet in 1 hour when moving toward each other (u + v = 120) and in 6 hours when moving in the same direction (u − v = 20). Find u and v.",
                "options": [
                    "u = 70 km/h, v = 50 km/h",
                    "u = 80 km/h, v = 40 km/h",
                    "u = 60 km/h, v = 60 km/h",
                    "u = 90 km/h, v = 30 km/h",
                ],
                "answer": 0,
                "hint": "Add u + v = 120 and u − v = 20 to get 2u = 140!",
                "explanation": "2u = 140 ⇒ u = 70 km/h; then v = 120 − 70 = 50 km/h.",
            },
            {
                "question": "In a cyclic quadrilateral ABCD, ∠A = 2x + 4, ∠C = 2y + 10. Which linear equation must hold?",
                "options": [
                    "2x + 2y + 14 = 180 (⇒ x + y = 83)",
                    "2x + 2y + 14 = 360",
                    "2x − 2y = 180",
                    "x + y = 90",
                ],
                "answer": 0,
                "hint": "Opposite angles of a cyclic quadrilateral are supplementary (sum to 180°)!",
                "explanation": "(2x + 4) + (2y + 10) = 180 ⇒ 2x + 2y = 166 ⇒ x + y = 83.",
            },
        ],
    },
    {
        "id": 16,
        "title": "Two Variables Summary",
        "subtitle": "Chapter Summary: Standard Form, Slope-Intercept, Algebraic & Graphical Solution Criteria",
        "speech": (
            "Congratulations on reaching Slide Sixteen, our complete synthesis of Chapter Thirteen: Two Variables, One "
            "Line! Let us review the unified architecture connecting algebra, geometry, and history! "
            "First, a linear equation in two variables takes the standard form a x plus b y plus c equals zero, with "
            "a and b not both zero! Every ordered pair (x, y) satisfying the equation plots onto one continuous "
            "straight line, easily sketched using its x-intercept and y-intercept! "
            "Second, slope m equals Rise over Run measures line steepness—positive climbing, negative falling, zero "
            "horizontal, and undefined vertical! Rewriting standard form into slope-intercept form y equals m x plus d "
            "reveals m equals minus a over b and y-intercept d equals minus c over b! "
            "Third, when two equations form a simultaneous system, Substitution and Elimination solve for the shared "
            "intersection point! Even faster, coefficient ratios classify every system instantly: unequal a-to-b ratios "
            "give intersecting lines with a unique solution; all three ratios equal give coincident lines with "
            "infinitely many solutions; equal a-to-b ratios differing from c-ratio give parallel lines with no "
            "solution! You are now completely ready for the four silent interactive mastery quiz challenges on Slides Seventeen through Twenty!"
        ),
        "checkpoints": [
            {
                "question": "Which trio of conditions correctly classifies a pair of linear equations as having NO solution?",
                "options": [
                    "a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (Parallel lines)",
                    "a₁/a₂ ≠ b₁/b₂ (Intersecting lines)",
                    "a₁/a₂ = b₁/b₂ = c₁/c₂ (Coincident lines)",
                    "a₁ + b₁ = 0",
                ],
                "answer": 0,
                "hint": "Parallel lines have equal slopes (a₁/a₂ = b₁/b₂) but different intercepts (≠ c₁/c₂)!",
                "explanation": "a₁/a₂ = b₁/b₂ ≠ c₁/c₂ guarantees parallel lines with zero intersection points.",
            },
            {
                "question": "For any non-vertical line ax + by + c = 0 (b ≠ 0), what are its slope m and y-intercept d?",
                "options": [
                    "m = −a/b and d = −c/b",
                    "m = a/b and d = c/b",
                    "m = −b/a and d = −c/a",
                    "m = a and d = c",
                ],
                "answer": 0,
                "hint": "Isolate y in ax + by + c = 0 to get y = (−a/b)x + (−c/b)!",
                "explanation": "by = −ax − c ⇒ y = (−a/b)x + (−c/b), so m = −a/b and d = −c/b.",
            },
        ],
    },
]

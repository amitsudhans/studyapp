#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 1: Orienting Yourself: The Use of Coordinates
Slides Data Generator - Part 3 (Slides 17 to 20: 40 Mastery Quiz Questions)
Silent quiz/exercise slides with 3-step mathematical solutions, zero fictional human names.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Coordinate System Quiz",
        "subtitle": "Exercise Set 1 (Questions 1–10): Historical Coordinate Roots, Tactile Maps, Axes, Origin, Quadrants & Distance from Axes",
        "questions": [
            {
                "question": "Cities of the Sindhu-Sarasvatī Civilisation used grid streets intersecting at right angles with major avenues roughly how wide?",
                "options": [
                    "Around 10 metres wide dividing residential areas into rectangular blocks",
                    "Less than 0.5 metres wide forming circular rings",
                    "Around 100 metres wide curved in spirals",
                    "Non-intersecting parallel strips without cross-lanes"
                ],
                "answer": 0,
                "hint": "Recall Section 1.1 urban archaeology in Harappan cities.",
                "explanation": "Sindhu-Sarasvatī towns featured ~10 m wide main north-south and east-west grid streets meeting at 90°.",
                "solution_steps": [
                    "Historical context: Excavations of Sindhu-Sarasvatī sites reveal deliberate municipal grid engineering.",
                    "Geometric structure: Main streets (~10 m wide) ran perpendicularly north-south and east-west, creating rectangular blocks.",
                    "Hence Option A accurately describes Sindhu-Sarasvatī urban coordinate planning."
                ]
            },
            {
                "question": "In ancient Indian mathematical astronomy, which city served as the central zero-longitude prime meridian?",
                "options": [
                    "Ujjayinī",
                    "Pāṭaliputra",
                    "Kāñcīpuram",
                    "Takṣaśilā"
                ],
                "answer": 0,
                "hint": "Recall the historic astronomical meridian city highlighted in the Siddhāntas.",
                "explanation": "Ancient Indian astronomers anchored longitude 0° along the meridian passing through Ujjayinī.",
                "solution_steps": [
                    "Coordinate systems require a shared zero reference line to assign unambiguous positions.",
                    "Classical Indian Siddhānta treatises used the north-south line passing through Ujjayinī as zero longitude.",
                    "Therefore Ujjayinī served as the prime meridian."
                ]
            },
            {
                "question": "Why were Brahmagupta's rules for zero and negative numbers (628 CE) essential for the full 2D Cartesian plane?",
                "options": [
                    "They made negative coordinates on both axes meaningful, enabling Quadrants II, III, and IV",
                    "They eliminated the vertical axis completely",
                    "They forced all distances to remain zero",
                    "They applied only to spherical stars and never to flat planes"
                ],
                "answer": 0,
                "hint": "Think about what numbers appear when you move left of the Origin or below the x-axis.",
                "explanation": "Zero defines the Origin (0,0), and negative arithmetic gives meaning to negative abscissae and ordinates across all 4 quadrants.",
                "solution_steps": [
                    "Pre-Brahmagupta geometry used positive magnitudes only, limiting coordinates to a single positive quadrant.",
                    "Brahmagupta formalized zero and signed negative numbers in Brāhmasphuṭasiddhānta (628 CE).",
                    "This allowed axes to extend indefinitely in negative directions, completing all four quadrants."
                ]
            },
            {
                "question": "Which two 17th-century scholars unified algebra and geometry by plotting equations on two perpendicular coordinate axes?",
                "options": [
                    "Pierre de Fermat and René Descartes",
                    "Hipparchus and Ptolemy",
                    "Āryabhaṭa and Baudhāyana",
                    "Al-Bīrūnī and Hipparchus"
                ],
                "answer": 0,
                "hint": "One of them gave his name to the 'Cartesian' plane.",
                "explanation": "Fermat and René Descartes independently developed analytic coordinate geometry using perpendicular axes.",
                "solution_steps": [
                    "While Hipparchus, Ptolemy, Āryabhaṭa, Al-Bīrūnī, and Omar Khayyām built foundations, analytic algebra-geometry began in 17th-century France.",
                    "Pierre de Fermat and René Descartes independently linked equations in (x, y) to curves on perpendicular axes.",
                    "Descartes's Latin name Cartesius gives us the term 'Cartesian plane'."
                ]
            },
            {
                "question": "On a tactile pin-and-thread floor plan scaled at 1 cm : 1 foot, a wardrobe spans from pin (3, 8) to pin (9, 8) and has depth 2 cm. What is its actual length and depth?",
                "options": [
                    "6 feet long and 2 feet deep",
                    "9 feet long and 8 feet deep",
                    "3 feet long and 2 feet deep",
                    "12 feet long and 4 feet deep"
                ],
                "answer": 0,
                "hint": "Compute horizontal span |9 - 3| cm, then apply scale 1 cm = 1 foot.",
                "explanation": "Horizontal length on board = 9 - 3 = 6 cm → 6 feet; depth = 2 cm → 2 feet.",
                "solution_steps": [
                    "Wardrobe endpoints along the horizontal thread: x₁ = 3 cm, x₂ = 9 cm at constant y = 8 cm.",
                    "Board length = |9 - 3| = 6 cm; board depth = 2 cm.",
                    "Applying tactile scale 1 cm : 1 foot yields actual dimensions 6 feet long by 2 feet deep."
                ]
            },
            {
                "question": "In which quadrant does the point (-6, 4) lie?",
                "options": [
                    "Quadrant II",
                    "Quadrant I",
                    "Quadrant III",
                    "Quadrant IV"
                ],
                "answer": 0,
                "hint": "x = -6 is negative (left), y = +4 is positive (up).",
                "explanation": "Points with sign pattern (-, +) lie in Quadrant II (top-left).",
                "solution_steps": [
                    "Check signs of coordinates in (-6, 4): abscissa x = -6 < 0 and ordinate y = 4 > 0.",
                    "Counter-clockwise sign convention: QI (+,+), QII (-,+), QIII (-,-), QIV (+,-).",
                    "Sign pattern (-, +) places (-6, 4) squarely in Quadrant II."
                ]
            },
            {
                "question": "Where does the point (5, 0) lie in the Cartesian coordinate plane?",
                "options": [
                    "On the positive x-axis (not in any quadrant)",
                    "In Quadrant I",
                    "In Quadrant IV",
                    "On the positive y-axis"
                ],
                "answer": 0,
                "hint": "Whenever y = 0, there is zero vertical motion up or down from the horizontal axis.",
                "explanation": "Points of form (x, 0) with x > 0 lie directly on the positive x-axis.",
                "solution_steps": [
                    "Given ordered pair: (5, 0), so x = 5 and y = 0.",
                    "Since y = 0, the point does not rise into QI or drop into QIV; it sits on the boundary x-axis.",
                    "Because x = +5 > 0, (5, 0) lies on the positive x-axis."
                ]
            },
            {
                "question": "What is the perpendicular distance of the point P(-8, -3) from the y-axis?",
                "options": [
                    "8 units",
                    "3 units",
                    "-8 units",
                    "11 units"
                ],
                "answer": 0,
                "hint": "Perpendicular distance from the vertical y-axis is horizontal magnitude |x|!",
                "explanation": "Distance from the y-axis equals |x| = |-8| = 8 units (non-negative).",
                "solution_steps": [
                    "Distance from the vertical y-axis is measured horizontally along x.",
                    "For P(-8, -3), x = -8, so the point sits 8 units to the left of the y-axis.",
                    "Since geometric distance is always non-negative, distance = |x| = |-8| = 8 units."
                ]
            },
            {
                "question": "What is the perpendicular distance of the point Q(4, -9) from the x-axis?",
                "options": [
                    "9 units",
                    "4 units",
                    "-9 units",
                    "5 units"
                ],
                "answer": 0,
                "hint": "Distance from the horizontal x-axis is vertical height |y|.",
                "explanation": "Distance from the x-axis equals |y| = |-9| = 9 units.",
                "solution_steps": [
                    "Distance from the horizontal x-axis is measured vertically along y.",
                    "For Q(4, -9), y = -9, meaning Q lies 9 units directly below the x-axis.",
                    "Taking non-negative magnitude |y| = |-9| = 9 units."
                ]
            },
            {
                "question": "For which values of k does the ordered pair (k, 7) represent the EXACT same point as (7, k)?",
                "options": [
                    "Only when k = 7",
                    "For every real number k",
                    "Only when k = -7",
                    "When k = 0"
                ],
                "answer": 0,
                "hint": "Remember the rule: (x, y) = (y, x) if and only if x = y!",
                "explanation": "Two ordered pairs match iff both x-coordinates match and both y-coordinates match, forcing k = 7.",
                "solution_steps": [
                    "Equate ordered pairs: (k, 7) = (7, k).",
                    "Equality of ordered pairs requires matching first components (k = 7) and matching second components (7 = k).",
                    "Hence (k, 7) = (7, k) holds if and only if k = 7."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Distance Formula Quiz",
        "subtitle": "Exercise Set 2 (Questions 1–10): Baudhāyana-Pythagoras Derivation, Distance Formula Calculations, Origin Radius & Reflections",
        "questions": [
            {
                "question": "In the Distance Formula derivation between P(x₁, y₁) and Q(x₂, y₂), which theorem relates the horizontal leg |x₂ - x₁| and vertical leg |y₂ - y₁| to segment PQ?",
                "options": [
                    "The Baudhāyana-Pythagoras Theorem",
                    "The Fundamental Theorem of Arithmetic",
                    "The Angle Sum Property of Triangles",
                    "The Pigeonhole Principle"
                ],
                "answer": 0,
                "hint": "Horizontal and vertical lines meet at 90°, forming a right-angled triangle!",
                "explanation": "Right triangle PRQ has legs |x₂ - x₁| and |y₂ - y₁|, so Baudhāyana-Pythagoras yields PQ² = (x₂ - x₁)² + (y₂ - y₁)².",
                "solution_steps": [
                    "Draw horizontal through P(x₁, y₁) and vertical through Q(x₂, y₂) intersecting perpendicularly at R(x₂, y₁).",
                    "Right triangle PRQ has legs PR = |x₂ - x₁| and RQ = |y₂ - y₁|.",
                    "Applying the Baudhāyana-Pythagoras Theorem gives hypotenuse PQ = √((x₂ - x₁)² + (y₂ - y₁)²)."
                ]
            },
            {
                "question": "Compute the exact distance between P(1, -2) and Q(7, 6).",
                "options": [
                    "10 units",
                    "14 units",
                    "√20 units",
                    "8 units"
                ],
                "answer": 0,
                "hint": "Evaluate Δx = 7 - 1 = 6 and Δy = 6 - (-2) = 8!",
                "explanation": "d = √(6² + 8²) = √(36 + 64) = √100 = 10 units.",
                "solution_steps": [
                    "Given P(1, -2) and Q(7, 6): horizontal shift Δx = 7 - 1 = 6, vertical shift Δy = 6 - (-2) = 8.",
                    "Substitute into Distance Formula: PQ = √(6² + 8²) = √(36 + 64) = √100.",
                    "Therefore PQ = 10 units."
                ]
            },
            {
                "question": "What is the straight-line distance from Origin O(0, 0) to point R(-8, -15)?",
                "options": [
                    "17 units",
                    "23 units",
                    "7 units",
                    "√161 units"
                ],
                "answer": 0,
                "hint": "Use Origin distance formula √(x² + y²) = √((-8)² + (-15)²).",
                "explanation": "OR = √(64 + 225) = √289 = 17 units.",
                "solution_steps": [
                    "Distance from Origin O(0, 0) to (x, y) is √(x² + y²).",
                    "Substitute x = -8, y = -15: √((-8)² + (-15)²) = √(64 + 225) = √289.",
                    "Since 17² = 289, OR = 17 units."
                ]
            },
            {
                "question": "Find the distance between A(-3, 5) and B(9, 5) without using a radical calculation.",
                "options": [
                    "12 units",
                    "6 units",
                    "10 units",
                    "√144 + 25 units"
                ],
                "answer": 0,
                "hint": "Notice both points have identical y-coordinate y = 5, forming a purely horizontal segment!",
                "explanation": "Since y₁ = y₂ = 5, vertical difference Δy = 0, so distance = |9 - (-3)| = 12 units.",
                "solution_steps": [
                    "Identify shared coordinate: both A(-3, 5) and B(9, 5) lie on the horizontal line y = 5.",
                    "With Δy = 0, √((Δx)² + 0²) reduces directly to |x₂ - x₁|.",
                    "Compute |9 - (-3)| = |12| = 12 units."
                ]
            },
            {
                "question": "What is the distance between P(a, b) and Q(-a, -b)?",
                "options": [
                    "2√(a² + b²)",
                    "√(a² + b²)",
                    "0",
                    "2(a + b)"
                ],
                "answer": 0,
                "hint": "Compute Δx = -a - a = -2a and Δy = -b - b = -2b, then factor out 4!",
                "explanation": "PQ = √((-2a)² + (-2b)²) = √(4a² + 4b²) = 2√(a² + b²).",
                "solution_steps": [
                    "Evaluate differences: Δx = -a - a = -2a and Δy = -b - b = -2b.",
                    "Substitute into Distance Formula: PQ = √((-2a)² + (-2b)²) = √(4(a² + b²)).",
                    "Taking √4 = 2 out of the radical yields PQ = 2√(a² + b²)."
                ]
            },
            {
                "question": "If the distance between A(k, 2) and B(3, -6) is 10 units, find all possible values of k.",
                "options": [
                    "k = 9 or k = -3",
                    "k = 9 only",
                    "k = 3 or k = -9",
                    "k = 6 or k = -6"
                ],
                "answer": 0,
                "hint": "Solve (3 - k)² + (-6 - 2)² = 10², so (3 - k)² = 36!",
                "explanation": "(3 - k)² + 64 = 100 → (3 - k)² = 36 → 3 - k = ±6 → k = -3 or k = 9.",
                "solution_steps": [
                    "Apply Distance Formula squared: (3 - k)² + (-6 - 2)² = 10².",
                    "Simplify: (3 - k)² + 64 = 100 ⇒ (3 - k)² = 36 ⇒ 3 - k = +6 or -6.",
                    "Solving gives k = -3 or k = 9."
                ]
            },
            {
                "question": "If point A(-4, 7) is reflected across the y-axis, what are the coordinates of its image A'?",
                "options": [
                    "(4, 7)",
                    "(-4, -7)",
                    "(4, -7)",
                    "(7, -4)"
                ],
                "answer": 0,
                "hint": "Reflecting across the vertical y-axis flips x to -x and preserves y.",
                "explanation": "Reflection across the y-axis sends (x, y) → (-x, y), so (-4, 7) maps to (4, 7).",
                "solution_steps": [
                    "For reflection across the vertical y-axis, perpendicular distance to the y-axis reverses horizontally while height y stays fixed.",
                    "Rule: (x, y) ↦ (-x, y).",
                    "Thus A(-4, 7) maps to A'(-(-4), 7) = (4, 7)."
                ]
            },
            {
                "question": "Triangle ABC has vertices A(1, 2), B(5, 2), and C(5, 5). After reflecting ΔABC across the x-axis to ΔA'B'C', what is the perimeter of ΔA'B'C'?",
                "options": [
                    "12 units (identical to ΔABC)",
                    "6 units (halved by negative y-values)",
                    "24 units",
                    "Cannot be determined without measuring angles"
                ],
                "answer": 0,
                "hint": "Compute sides AB = 4, BC = 3, AC = 5 of ΔABC and apply reflection isometry!",
                "explanation": "ΔABC is a 3-4-5 right triangle with perimeter 12; x-axis reflection preserves all lengths, so perimeter stays 12 units.",
                "solution_steps": [
                    "Compute side lengths of ΔABC: AB = |5-1| = 4, BC = |5-2| = 3, AC = √(4² + 3²) = 5.",
                    "Perimeter of ΔABC = 4 + 3 + 5 = 12 units.",
                    "Reflection across the x-axis preserves every distance ((x,-y) leaves Δx² + (-Δy)² unchanged), so ΔA'B'C' also has perimeter 12 units."
                ]
            },
            {
                "question": "Which transformation maps P(2, -3) to P'(-2, 3) while keeping its distance from the Origin equal to √13?",
                "options": [
                    "Double reflection across both x-axis and y-axis (reflection through Origin O)",
                    "Reflection across the x-axis only",
                    "Reflection across the y-axis only",
                    "Horizontal translation right by 4 units"
                ],
                "answer": 0,
                "hint": "Notice BOTH coordinates changed signs: (2, -3) → (-2, 3)!",
                "explanation": "Origin reflection maps (x, y) → (-x, -y), preserving OP = √((-2)² + 3²) = √13.",
                "solution_steps": [
                    "Compare pre-image P(2, -3) and image P'(-2, 3): both abscissa and ordinate negated.",
                    "Rule (x, y) ↦ (-x, -y) corresponds to reflecting across both axes (Origin reflection).",
                    "Origin distances: OP = √(2² + (-3)²) = √13 and OP' = √((-2)² + 3²) = √13."
                ]
            },
            {
                "question": "Why does the Distance Formula yield the exact same answer whether you substitute P first or Q first?",
                "options": [
                    "Because squaring reverses sign differences: (x₂ - x₁)² = (x₁ - x₂)² and (y₂ - y₁)² = (y₁ - y₂)²",
                    "Because square roots can produce negative distances",
                    "Because x₁ must always equal x₂",
                    "Because P and Q always share the same quadrant"
                ],
                "answer": 0,
                "hint": "Evaluate (-5)² versus (+5)²!",
                "explanation": "Since (-Δx)² = (Δx)² and (-Δy)² = (Δy)², swapping endpoints leaves the sum under the square root unchanged.",
                "solution_steps": [
                    "Note that (x₁ - x₂) = -(x₂ - x₁) and (y₁ - y₂) = -(y₂ - y₁).",
                    "Squaring removes the negative sign: (-k)² = k² for every real number k.",
                    "Thus √((x₂ - x₁)² + (y₂ - y₁)²) = √((x₁ - x₂)² + (y₁ - y₂)²), guaranteeing symmetric distance."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Collinearity Circle Quiz",
        "subtitle": "Exercise Set 3 (Questions 1–10): Axes Intersections, Midpoints, Equidistance, Collinearity Checks & Circle Boundaries",
        "questions": [
            {
                "question": "A vertical line segment runs from P(-3, -4) to Q(-3, 5). At what exact point does segment PQ intersect the x-axis?",
                "options": [
                    "(-3, 0)",
                    "(0, -3)",
                    "(-3, 0.5)",
                    "(0, 5)"
                ],
                "answer": 0,
                "hint": "Along a vertical segment x stays -3, and the x-axis is defined by y = 0!",
                "explanation": "Every point on PQ has x = -3, and y rises from -4 through 0 to 5, intersecting the x-axis at (-3, 0).",
                "solution_steps": [
                    "Check endpoints P(-3, -4) and Q(-3, 5): x remains constant at -3.",
                    "The x-axis consists of all points where y = 0; since 0 lies strictly between -4 and 5, the segment crosses it.",
                    "Intersection point is (-3, 0)."
                ]
            },
            {
                "question": "Find the midpoint M of the segment joining A(-6, 4) and B(10, -8).",
                "options": [
                    "(2, -2)",
                    "(8, -6)",
                    "(-8, 6)",
                    "(4, -4)"
                ],
                "answer": 0,
                "hint": "Compute ((-6 + 10)/2, (4 - 8)/2).",
                "explanation": "M = (4/2, -4/2) = (2, -2).",
                "solution_steps": [
                    "Apply Midpoint Formula M = ((x₁ + x₂)/2, (y₁ + y₂)/2).",
                    "x_M = (-6 + 10)/2 = 4/2 = 2; y_M = (4 + (-8))/2 = -4/2 = -2.",
                    "Hence M = (2, -2), equidistant from A and B."
                ]
            },
            {
                "question": "Which point on the y-axis is equidistant from A(6, 5) and B(-4, 3)?",
                "options": [
                    "(0, 9)",
                    "(0, 4)",
                    "(0, -9)",
                    "(9, 0)"
                ],
                "answer": 0,
                "hint": "Set P = (0, y) and solve PA² = PB²: (0-6)² + (y-5)² = (0+4)² + (y-3)²!",
                "explanation": "36 + y² - 10y + 25 = 16 + y² - 6y + 9 → 61 - 10y = 25 - 6y → 36 = 4y → y = 9 → (0, 9).",
                "solution_steps": [
                    "Any point on the y-axis has coordinates P(0, y).",
                    "Equate squared distances: (0 - 6)² + (y - 5)² = (0 - (-4))² + (y - 3)² ⇒ 36 + y² - 10y + 25 = 16 + y² - 6y + 9.",
                    "Solve 61 - 10y = 25 - 6y ⇒ 4y = 36 ⇒ y = 9, giving point (0, 9)."
                ]
            },
            {
                "question": "Test whether A(1, 5), B(2, 3), and C(-2, -11) are collinear.",
                "options": [
                    "Not collinear, because AB + BC ≠ AC",
                    "Collinear, because AB + BC = AC",
                    "Collinear, because AB = BC = AC",
                    "Collinear, because A and B both lie in Quadrant I"
                ],
                "answer": 0,
                "hint": "Compute AB = √5, BC = √212, and AC = √265; compare √5 + √212 against √265!",
                "explanation": "AB = √5 ≈ 2.24, BC = √212 ≈ 14.56 (sum ≈ 16.80), while AC = √265 ≈ 16.28; since √5 + √212 > √265, they are NOT collinear.",
                "solution_steps": [
                    "Compute distances: AB = √((2-1)² + (3-5)²) = √(1 + 4) = √5 ≈ 2.24.",
                    "BC = √((-2-2)² + (-11-3)²) = √(16 + 196) = √212 ≈ 14.56; AC = √((-2-1)² + (-11-5)²) = √(9 + 256) = √265 ≈ 16.28.",
                    "Since AB + BC ≈ 16.80 ≠ 16.28 = AC, the points satisfy strict triangle inequality and are NOT collinear."
                ]
            },
            {
                "question": "Are the three points P(0, 1), Q(3, 5), and R(6, 9) collinear?",
                "options": [
                    "Yes—PQ = 5, QR = 5, and PR = 10, so PQ + QR = PR",
                    "No—they form an acute isosceles triangle",
                    "No—PR = √110 while PQ + QR = 10",
                    "Cannot be tested using coordinates"
                ],
                "answer": 0,
                "hint": "Calculate PQ = √(3²+4²), QR = √(3²+4²), and PR = √(6²+8²)!",
                "explanation": "PQ = 5, QR = 5, and PR = 10; since 5 + 5 = 10, Q lies straight on segment PR and P, Q, R are collinear.",
                "solution_steps": [
                    "Compute pairwise distances: PQ = √((3-0)² + (5-1)²) = √(9+16) = 5.",
                    "QR = √((6-3)² + (9-5)²) = √(9+16) = 5; PR = √((6-0)² + (9-1)²) = √(36+64) = 10.",
                    "Exact equality PQ + QR = 5 + 5 = 10 = PR proves P, Q, and R are collinear."
                ]
            },
            {
                "question": "A circle centered at the Origin O(0, 0) passes through A(6, 8). What is the radius of this circle?",
                "options": [
                    "10 units",
                    "14 units",
                    "7 units",
                    "√28 units"
                ],
                "answer": 0,
                "hint": "The radius equals distance OA = √(6² + 8²)!",
                "explanation": "r = OA = √(36 + 64) = √100 = 10 units.",
                "solution_steps": [
                    "Since O(0, 0) is the centre and A(6, 8) lies on the circle, radius r = OA.",
                    "Apply Origin Distance Formula: r = √(6² + 8²) = √(36 + 64) = √100.",
                    "Therefore radius r = 10 units."
                ]
            },
            {
                "question": "A circle centered at O(0, 0) has radius r = 13 units. Where does the point K(5, -11) lie?",
                "options": [
                    "Strictly INSIDE the circle, because OK = √146 < 13",
                    "ON the circle boundary, because OK = 13",
                    "Strictly OUTSIDE the circle, because OK > 13",
                    "At the centre O(0, 0)"
                ],
                "answer": 0,
                "hint": "Compare OK² = 5² + (-11)² = 146 against r² = 13² = 169!",
                "explanation": "OK² = 25 + 121 = 146 < 169 = 13², so OK < 13 and K lies strictly inside the circle.",
                "solution_steps": [
                    "Compare squared distance OK² against squared radius r² to avoid decimal approximation.",
                    "OK² = 5² + (-11)² = 25 + 121 = 146, whereas r² = 13² = 169.",
                    "Since 146 < 169 (OK ≈ 12.08 < 13), point K lies strictly inside the circle."
                ]
            },
            {
                "question": "For a circle of radius r = 5 centered at O(0, 0), where does the point T(-4, 4) lie?",
                "options": [
                    "Strictly OUTSIDE the circle, because OT = √32 > 5",
                    "Strictly INSIDE the circle, because OT < 5",
                    "ON the circle boundary, because OT = 5",
                    "On the x-axis"
                ],
                "answer": 0,
                "hint": "Compare OT² = (-4)² + 4² = 32 against r² = 5² = 25!",
                "explanation": "OT² = 16 + 16 = 32 > 25 = r², so OT = √32 ≈ 5.66 > 5 places T outside the circle.",
                "solution_steps": [
                    "Compute squared distance from Origin: OT² = (-4)² + 4² = 16 + 16 = 32.",
                    "Compare with r² = 5² = 25.",
                    "Since 32 > 25, OT > r, proving T(-4, 4) lies strictly outside the circle."
                ]
            },
            {
                "question": "If M(3, -1) is the midpoint of segment PQ where P is (-2, 5), what are the coordinates of endpoint Q?",
                "options": [
                    "(8, -7)",
                    "(0.5, 2)",
                    "(4, -3)",
                    "(7, -6)"
                ],
                "answer": 0,
                "hint": "Set (-2 + x)/2 = 3 and (5 + y)/2 = -1!",
                "explanation": "-2 + x = 6 → x = 8; 5 + y = -2 → y = -7, so Q = (8, -7).",
                "solution_steps": [
                    "Let Q = (x, y). By Midpoint Formula, ((-2 + x)/2, (5 + y)/2) = (3, -1).",
                    "Solve x: -2 + x = 6 ⇒ x = 8. Solve y: 5 + y = -2 ⇒ y = -7.",
                    "Thus endpoint Q has coordinates (8, -7)."
                ]
            },
            {
                "question": "Which point on the line joining A(0, 8) and B(6, 0) is equidistant from A and B?",
                "options": [
                    "(3, 4), which is also 5 units from the Origin O(0, 0)",
                    "(4, 3)",
                    "(6, 8)",
                    "(0, 0)"
                ],
                "answer": 0,
                "hint": "The point on segment AB equidistant from A and B is the midpoint of AB!",
                "explanation": "Midpoint M = ((0+6)/2, (8+0)/2) = (3, 4); distance OM = √(3² + 4²) = 5 units.",
                "solution_steps": [
                    "The unique point ON segment AB equidistant from endpoints A and B is its midpoint M.",
                    "M = ((0 + 6)/2, (8 + 0)/2) = (3, 4).",
                    "Verify distances: AM = BM = 5 units, and OM = √(3² + 4²) = 5 units."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Applied Coordinates Quiz",
        "subtitle": "Exercise Set 4 (Questions 1–10): City Street Grids, Screen Pixel Coordinates, Shape Areas & Chapter Summary Mastery",
        "questions": [
            {
                "question": "A city's planned street grid aligns north-south avenues along x = 1, 2, 3... and east-west streets along y = 1, 2, 3... (100 m per grid unit). How much shorter is the straight aerial drone path from (1, 2) to (9, 8) than walking along the grid streets?",
                "options": [
                    "400 m shorter (1000 m aerial vs 1400 m along grid streets)",
                    "200 m shorter (1200 m aerial vs 1400 m along grid streets)",
                    "400 m longer",
                    "Equal distance of 1000 m"
                ],
                "answer": 0,
                "hint": "Street path = (|9-1| + |8-2|) units; aerial path = √(8² + 6²) units; multiply each by 100 m!",
                "explanation": "Street path = 8 + 6 = 14 units = 1400 m; aerial path = √(64 + 36) = 10 units = 1000 m; difference = 400 m.",
                "solution_steps": [
                    "Evaluate grid shifts: Δx = 9 - 1 = 8 units, Δy = 8 - 2 = 6 units.",
                    "Street distance = (8 + 6) × 100 m = 1400 m; Aerial Euclidean distance = √(8² + 6²) × 100 m = 10 × 100 m = 1000 m.",
                    "Aerial path is 1400 - 1000 = 400 m shorter."
                ]
            },
            {
                "question": "On a 1920 × 1080 computer screen where pixel (0, 0) is at the TOP-LEFT corner (x rightward, y downward), where does pixel (200, 150) sit relative to pixel (200, 900)?",
                "options": [
                    "Directly ABOVE pixel (200, 900) by 750 pixels",
                    "Directly BELOW pixel (200, 900) by 750 pixels",
                    "750 pixels to the RIGHT of pixel (200, 900)",
                    "In Quadrant IV below the bottom edge"
                ],
                "answer": 0,
                "hint": "Remember on computer displays, smaller y means closer to the TOP edge!",
                "explanation": "Both share x = 200; since screen y increases downward, y = 150 lies 750 pixels ABOVE y = 900.",
                "solution_steps": [
                    "Both pixels share horizontal column x = 200.",
                    "In screen coordinates, y = 0 is the top edge and y increases downward.",
                    "Because 150 < 900, pixel (200, 150) sits 900 - 150 = 750 pixels above pixel (200, 900)."
                ]
            },
            {
                "question": "A UI rectangle on a screen has top-left pixel corner at (100, 80) and bottom-right pixel corner at (420, 280). What are its pixel dimensions and area?",
                "options": [
                    "320 px wide × 200 px high; area = 64,000 square pixels",
                    "520 px wide × 360 px high; area = 187,200 square pixels",
                    "200 px wide × 320 px high; area = 32,000 square pixels",
                    "320 px wide × 200 px high; area = 32,000 square pixels"
                ],
                "answer": 0,
                "hint": "Width = 420 - 100 and height = 280 - 80!",
                "explanation": "Width = 320 px, height = 200 px, so Area = 320 × 200 = 64,000 px².",
                "solution_steps": [
                    "Compute horizontal width: Δx = 420 - 100 = 320 pixels.",
                    "Compute vertical height: Δy = 280 - 80 = 200 pixels.",
                    "Multiply width × height = 320 × 200 = 64,000 square pixels."
                ]
            },
            {
                "question": "Calculate the area of rectangle PQRS with vertices P(-2, -1), Q(5, -1), R(5, 4), and S(-2, 4).",
                "options": [
                    "35 square units",
                    "24 square units",
                    "15 square units",
                    "21 square units"
                ],
                "answer": 0,
                "hint": "Base PQ = |5 - (-2)| = 7 units; height QR = |4 - (-1)| = 5 units.",
                "explanation": "Width = 7 units, height = 5 units, so Area = 7 × 5 = 35 square units.",
                "solution_steps": [
                    "Bottom horizontal edge PQ spans from x = -2 to x = 5: base = 5 - (-2) = 7 units.",
                    "Right vertical edge QR spans from y = -1 to y = 4: height = 4 - (-1) = 5 units.",
                    "Area of rectangle PQRS = 7 × 5 = 35 square units."
                ]
            },
            {
                "question": "Find the area of triangle ABC with vertices A(-3, 0), B(5, 0), and C(2, 6).",
                "options": [
                    "24 square units",
                    "48 square units",
                    "15 square units",
                    "12 square units"
                ],
                "answer": 0,
                "hint": "Base AB lies on the x-axis from -3 to 5 (length 8); altitude from C(2, 6) to the x-axis is |6| = 6.",
                "explanation": "Base = 8 units and height = 6 units, so Area = ½ × 8 × 6 = 24 square units.",
                "solution_steps": [
                    "Side AB sits directly along the x-axis (y = 0) with length |5 - (-3)| = 8 units.",
                    "Perpendicular altitude from C(2, 6) down to the x-axis is |y_C| = 6 units.",
                    "Triangle Area = ½ × 8 × 6 = 24 square units."
                ]
            },
            {
                "question": "Find the area of triangle OAB formed by Origin O(0, 0), A(0, -7), and B(4, -7).",
                "options": [
                    "14 square units",
                    "28 square units",
                    "11 square units",
                    "7 square units"
                ],
                "answer": 0,
                "hint": "OA runs vertically 7 units down the y-axis and AB runs horizontally 4 units at right angle to OA!",
                "explanation": "ΔOAB is right-angled at A(0, -7) with legs OA = 7 and AB = 4, giving Area = ½ × 7 × 4 = 14 square units.",
                "solution_steps": [
                    "Segment OA lies on the y-axis (x = 0) from (0, 0) to (0, -7), length 7 units.",
                    "Segment AB runs horizontally from (0, -7) to (4, -7), length 4 units, perpendicular to OA at A.",
                    "Right triangle Area = ½ × 7 × 4 = 14 square units."
                ]
            },
            {
                "question": "Classify the triangle with vertices P(-2, 0), Q(2, 0), and R(0, 3) using the Distance Formula.",
                "options": [
                    "Isosceles triangle (PR = QR = √13 units, PQ = 4 units)",
                    "Equilateral triangle (all sides = 4 units)",
                    "Scalene right-angled triangle",
                    "Collinear degenerate points with zero area"
                ],
                "answer": 0,
                "hint": "Calculate PQ, PR, and QR cleanly via √(Δx² + Δy²)!",
                "explanation": "PQ = 4, PR = √(2² + 3²) = √13, and QR = √((-2)² + 3²) = √13; since PR = QR ≠ PQ, ΔPQR is isosceles.",
                "solution_steps": [
                    "PQ = |2 - (-2)| = 4 units.",
                    "PR = √((0 - (-2))² + (3 - 0)²) = √(4 + 9) = √13; QR = √((0 - 2)² + (3 - 0)²) = √(4 + 9) = √13.",
                    "Two equal sides (PR = QR = √13) prove ΔPQR is an isosceles triangle."
                ]
            },
            {
                "question": "A square ABCD has opposite corners at A(1, 1) and C(5, 5), with sides parallel to the axes. What are the other two vertices and the area of the square?",
                "options": [
                    "Vertices (5, 1) and (1, 5); area = 16 square units",
                    "Vertices (5, 0) and (0, 5); area = 25 square units",
                    "Vertices (4, 1) and (1, 4); area = 9 square units",
                    "Vertices (5, 1) and (1, 5); area = 32 square units"
                ],
                "answer": 0,
                "hint": "With axis-aligned sides, horizontal side = |5 - 1| = 4 and vertical side = |5 - 1| = 4!",
                "explanation": "The axis-aligned corners completing (1,1) and (5,5) are (5,1) and (1,5), giving side 4 and area 4² = 16 sq units.",
                "solution_steps": [
                    "For axis-parallel rectangle/square with opposite corners (x₁, y₁) and (x₂, y₂), the other corners are (x₂, y₁) and (x₁, y₂).",
                    "Here B = (5, 1) and D = (1, 5), giving equal side length |5 - 1| = 4 units.",
                    "Area of square ABCD = 4 × 4 = 16 square units."
                ]
            },
            {
                "question": "On a 2D coordinate grid, why is the area of ΔA'B'C' (reflected across the y-axis) ALWAYS equal to the area of ΔABC?",
                "options": [
                    "Because reflection preserves all side lengths and right angles (rigid congruence)",
                    "Because reflecting across the y-axis cancels negative heights",
                    "Because area depends only on Quadrant I coordinates",
                    "Because every triangle changes into a square under reflection"
                ],
                "answer": 0,
                "hint": "Recall that (-x₂ - (-x₁))² = (x₂ - x₁)² preserves every side length of the triangle!",
                "explanation": "Y-axis reflection maps (x, y) → (-x, y), an isometry preserving all three triangle side lengths and hence exact area.",
                "solution_steps": [
                    "Under reflection across the y-axis, each vertex (xᵢ, yᵢ) maps to (-xᵢ, yᵢ).",
                    "Distance formula gives identical side lengths A'B' = AB, B'C' = BC, and A'C' = AC.",
                    "By SSS congruence, ΔA'B'C' ≅ ΔABC, guaranteeing identical enclosed area."
                ]
            },
            {
                "question": "Which unified principle summarizes Chapter 1 (Orienting Yourself: The Use of Coordinates)?",
                "options": [
                    "Ordered pairs (x, y) relative to perpendicular axes and Origin (0,0) encode positions, signs, reflections, and distances algebraically",
                    "Coordinate systems only apply to ancient street plans and cannot measure circles or areas",
                    "Distance between two points depends strictly on subtracting x from y without squaring",
                    "Only positive integers in Quadrant I can represent geometric figures"
                ],
                "answer": 0,
                "hint": "Combine Section 1.1–1.4 concepts: axes, Origin, ordered pairs, signs, reflections, and Distance Formula.",
                "explanation": "From ancient grids and tactile plans to the 4-quadrant Cartesian plane and Distance Formula, coordinates unify geometry and algebra.",
                "solution_steps": [
                    "Axes & Origin setup assigns a unique ordered pair (x, y) to every point across 4 signed quadrants.",
                    "Coordinate rules govern distances to axes (|x|, |y|), equality (x,y)=(y,x) ⇔ x=y, midpoints, and axis reflections.",
                    "The Distance Formula √((x₂-x₁)² + (y₂-y₁)²) unlocks collinearity, circles, city grids, screen pixels, and area calculations."
                ]
            }
        ]
    }
]

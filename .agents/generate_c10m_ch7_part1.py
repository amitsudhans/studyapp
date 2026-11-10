#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 7: Coordinate Geometry
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (no Niharika, Preet, Champa, Chameli, Rashmi, Raghav, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Coordinate Axes Review",
        "subtitle": "Abscissa (x), Ordinate (y), Points on Axes & Bridging Algebra With Geometry (Section 7.1)",
        "speech": (
            "Welcome, curious math navigators, to Class Ten Chapter Seven on Coordinate Geometry! Let us begin by refreshing the crisp Cartesian coordinate grid you mastered back in Class Nine! "
            "Every point P sitting on a flat coordinate plane owns an ordered pair address x comma y! That first number x wears the title abscissa, measuring signed horizontal distance away from the vertical y axis! "
            "The second number y wears the title ordinate, measuring signed vertical distance away from the horizontal x axis! Watch what happens whenever a point sits directly on an axis: every point lying along the x axis has y coordinate zero, taking clean form x comma zero! "
            "Every point lying along the y axis has x coordinate zero, taking clean form zero comma y! Why do scientists love Coordinate Geometry so deeply? Because it constructs an algebraic bridge directly over classical geometry, translating shapes into clean numerical coordinates! "
            "Engineers, pilots, ocean navigators, earthquake seismologists locating tremor epicenters, and digital graphic artists all depend heavily on coordinate geometry every single day! "
            "In this exciting chapter, we unlock TWO core tools: measuring exact straight distances between coordinate points, and splitting line segments cleanly in any ratio!"
        ),
        "checkpoints": [
            {
                "question": "In the ordered coordinate pair P(−5, 8), identify the abscissa and ordinate accurately:",
                "options": [
                    "Abscissa = −5 (x-coordinate) and Ordinate = 8 (y-coordinate)",
                    "Abscissa = 8 and Ordinate = −5",
                    "Abscissa = 5 and Ordinate = −8",
                    "Both equal 3"
                ],
                "answer": 0,
                "hint": "Recall alphabetical pairing: x comes before y, and Abscissa (x) comes before Ordinate (y)!",
                "explanation": "In (x, y), x = −5 is the abscissa (distance along x-direction) and y = 8 is the ordinate (vertical height)."
            },
            {
                "question": "Any point lying directly on the y-axis ALWAYS takes which algebraic coordinate form?",
                "options": [
                    "(0, y)  (since horizontal distance from the y-axis is zero)",
                    "(x, 0)",
                    "(y, x)",
                    "(1, y)"
                ],
                "answer": 0,
                "hint": "Moving straight up or down along the y-axis means zero horizontal shift x!",
                "explanation": "Every point on the y-axis has abscissa x = 0, giving coordinate form (0, y)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Axes And Origin",
        "subtitle": "Distances Along Axes, Town A-B Problem (39 km) & Distance From Origin √(x² + y²)",
        "speech": (
            "Before jumping straight to diagonal lines tilted anywhere in space, start right along the straight coordinate axes! Suppose point A sits at (4, 0) and point B sits at (6, 0) along the x axis. How far apart are A and B? "
            "Simply subtract along the number line: six minus four equals two clean units! What if point C sits at (0, 3) and point D sits at (0, 8) straight up the y axis? Subtract heights cleanly: eight minus three equals five units! "
            "Now tilt into Textbook Section Seven Point Two's famous Two Towns riddle! Town B stands thirty six kilometers east and fifteen kilometers north of Town A located at the origin (0, 0), placing Town B squarely at coordinate (36, 15)! "
            "How do road engineers calculate the straight line flying distance from Origin O(0, 0) directly to P(36, 15)? Draw vertical drop PB down to the x axis, creating a crisp right angled triangle! "
            "By Pythagoras Theorem, squared distance equals 36 squared plus 15 squared, giving 1,296 plus 225 equals 1,521, whose positive square root equals 39 kilometers! "
            "That gives our Origin Distance rule: distance from origin (0, 0) to any point (x, y) equals square root of x squared plus y squared!"
        ),
        "checkpoints": [
            {
                "question": "Find the straight-line distance between Town A(0, 0) and Town B(36, 15) (Section 7.2 Opening Problem):",
                "options": [
                    "39 km  [since √(36² + 15²) = √(1296 + 225) = √1521 = 39]",
                    "51 km",
                    "21 km",
                    "42 km"
                ],
                "answer": 0,
                "hint": "Apply Pythagoras to horizontal 36 km and vertical 15 km legs!",
                "explanation": "√(36² + 15²) = √(1296 + 225) = √1521 = 39 km."
            },
            {
                "question": "Using the special-case Origin Distance formula, what is the distance of point P(−6, 8) from the origin O(0, 0)?",
                "options": [
                    "10 units",
                    "14 units",
                    "2 units",
                    "100 units"
                ],
                "answer": 0,
                "hint": "Compute √((−6)² + 8²) = √(36 + 64)!",
                "explanation": "Distance OP = √((−6)² + 8²) = √(36 + 64) = √100 = 10 units."
            }
        ]
    },
    {
        "id": 3,
        "title": "Deriving Distance Formula",
        "subtitle": "Pythagorean Proof of PQ = √[(x₂ − x₁)² + (y₂ − y₁)²] Between Any Two Plane Points",
        "speech": (
            "Now unlock the full universal Distance Formula working anywhere across ALL four quadrants of the plane! Take ANY two distinct points P at (x1, y1) and Q at (x2, y2). Draw a horizontal ray right from P and a vertical drop straight down from Q until they intersect cleanly at right angle corner T! "
            "Notice corner T sits right at x coordinate x2 and y coordinate y1! Compute both legs of right angled triangle PTQ using pure axis subtraction! "
            "Horizontal base PT equals x2 minus x1, while vertical height QT equals y2 minus y1! Now apply Pythagoras Theorem cleanly to hypotenuse PQ: PQ squared equals PT squared plus QT squared, meaning PQ squared equals (x2 minus x1) squared plus (y2 minus y1) squared! "
            "Because physical straight length is NEVER negative, always take ONLY the positive square root: PQ equals square root of (x2 minus x1) whole squared plus (y2 minus y1) whole squared! "
            "Watch this awesome symmetry comfort: whether you subtract x2 minus x1 or reverse into x1 minus x2, squaring wipes out minus signs identically! Test quickly on (2, 3) and (4, 1): two squared plus minus two squared gives square root of 8, or 2 root 2!"
        ),
        "checkpoints": [
            {
                "question": "Find the distance between points (2, 3) and (4, 1) (Exercise 7.1 Q1 i):",
                "options": [
                    "2√2 units",
                    "4 units",
                    "√2 units",
                    "2√3 units"
                ],
                "answer": 0,
                "hint": "Compute √[(4 − 2)² + (1 − 3)²] = √(4 + 4) = √8!",
                "explanation": "√((4−2)² + (1−3)²) = √(2² + (−2)²) = √8 = 2√2 units."
            },
            {
                "question": "Find the distance between points (a, b) and (−a, −b) (Exercise 7.1 Q1 iii):",
                "options": [
                    "2√(a² + b²)",
                    "√(a² + b²)",
                    "0",
                    "4(a + b)"
                ],
                "answer": 0,
                "hint": "Compute x₂ − x₁ = −a − a = −2a and y₂ − y₁ = −b − b = −2b, then square and simplify!",
                "explanation": "√((−2a)² + (−2b)²) = √(4a² + 4b²) = 2√(a² + b²)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Classifying Triangles Planes",
        "subtitle": "Identifying Scalene, Isosceles, Equilateral & Right-Angled Triangles via Side Lengths",
        "speech": (
            "Given just three numerical coordinates A, B, and C, how can you identify instantly whether they build a scalene, isosceles, equilateral, or right angled triangle without using a protractor? Compute ALL THREE side distances AB, BC, and AC using the Distance Formula! "
            "Look carefully at two landmark textbook examples! First check Textbook Example One: do points (3, 2), (-2, -3), and (2, 3) form a triangle, and which type? Compute squared lengths: "
            "PQ squared equals (-2 minus 3) squared plus (-3 minus 2) squared equals 50! QR squared equals (2 minus -2) squared plus (3 minus -3) squared equals 52! PR squared equals (2 minus 3) squared plus (3 minus 2) squared equals 2! "
            "Pause and check! Not only do square roots of 50, 52, and 2 confirm triangle inequality, look at squared sums: PQ squared plus PR squared equals 50 plus 2 equals 52 equals QR squared! By Converse of Pythagoras, angle P equals ninety degrees (Right Triangle)! "
            "Next check Exercise Seven Point One Question Four cleanly: vertices (5, -2), (6, 4), and (7, -2) yield TWO strictly equal slant lengths square root of 37 alongside base length 2, proving an Isosceles Triangle instantly!"
        ),
        "checkpoints": [
            {
                "question": "Check what type of triangle is formed by points (5, −2), (6, 4), and (7, −2) (Exercise 7.1 Q4):",
                "options": [
                    "Isosceles triangle  (two sides equal √37 while third side equals 2)",
                    "Equilateral triangle",
                    "Right-angled scalene triangle",
                    "Collinear (no triangle)"
                ],
                "answer": 0,
                "hint": "Find distances between each pair: √[(6−5)²+(4+2)²], √[(7−6)²+(−2−4)²], and √[(7−5)²+(−2+2)²]!",
                "explanation": "AB = √(1 + 36) = √37, BC = √(1 + 36) = √37, and AC = 2; two equal sides confirm an isosceles triangle."
            },
            {
                "question": "Given three points P, Q, R with squared distances PQ² = 50, PR² = 2, and QR² = 52 (Textbook Example 1), which triangle property holds?",
                "options": [
                    "Right-angled triangle at P (by Converse of Pythagoras: PQ² + PR² = 50 + 2 = 52 = QR²)",
                    "Equilateral triangle",
                    "Isosceles triangle",
                    "Collinear points"
                ],
                "answer": 0,
                "hint": "Add the two smaller squared lengths and compare against the largest squared length!",
                "explanation": "Since PQ² + PR² = 52 = QR², the Converse of Pythagoras proves ∠P = 90°."
            }
        ]
    },
    {
        "id": 5,
        "title": "Verifying Square Properties",
        "subtitle": "Proving Squares via 4 Equal Sides AND 2 Equal Diagonals (Excluding Non-Square Rhombuses)",
        "speech": (
            "Now tackle one of the biggest coordinate traps across Class Ten geometry! Suppose four students sit in a classroom grid at seats A(3, 4), B(6, 7), C(9, 4), and D(6, 1) from Exercise Seven Point One Question Five! Do those four seats form a true SQUARE? "
            "Let us test rigorously! First compute all four perimeter edge lengths AB, BC, CD, and DA! Every single edge gives square root of (3 squared plus 3 squared), which equals square root of 18, or 3 root 2 units! "
            "WAIT! Can we stop right here after checking four equal sides and shout SQUARE? DANGER, NEVER STOP EARLY! A tilted rhombus ALSO has four equal sides! "
            "How do we prove definitively that quadrilateral ABCD is a crisp 90 degree SQUARE rather than a tilted diamond rhombus? Compute BOTH DIAGONALS AC and BD! Diagonal AC between (3, 4) and (9, 4) equals six! Diagonal BD between (6, 7) and (6, 1) ALSO equals six! "
            "Four equal sides PLUS two equal diagonals locks in all four corner angles at 90 degrees, proving a true Square! Meanwhile in Ex 7.1 Q6, testing four points with equal sides yet UNEQUAL diagonals reveals a Rhombus!"
        ),
        "checkpoints": [
            {
                "question": "To prove four vertices A, B, C, D form a SQUARE (and NOT merely a rhombus) using Distance Formula, what MUST you verify?",
                "options": [
                    "All 4 sides equal (AB = BC = CD = DA) AND both diagonals equal (AC = BD)",
                    "Only all 4 sides equal",
                    "Only opposite sides equal",
                    "Only both diagonals equal"
                ],
                "answer": 0,
                "hint": "Rhombuses share equal edges, whereas squares equalize BOTH edges and diagonals!",
                "explanation": "Equal 4 edges confirms rhombus; equal diagonals guarantees 90° corners, confirming a true Square."
            },
            {
                "question": "Four classroom seats sit at A(3, 4), B(6, 7), C(9, 4), and D(6, 1) (Ex 7.1 Q5). Find side AB and diagonal AC:",
                "options": [
                    "Side AB = 3√2 units and Diagonal AC = 6 units (BD = 6 units too ⟹ Square!)",
                    "Side AB = 6 and Diagonal AC = 3√2",
                    "Side AB = 3 and Diagonal AC = 3",
                    "Unequal diagonals ⟹ Rhombus only"
                ],
                "answer": 0,
                "hint": "Compute √[(6−3)² + (7−4)²] for AB, and (9 − 3) for horizontal AC!",
                "explanation": "AB = BC = CD = DA = √18 = 3√2 and AC = BD = 6, proving ABCD is a Square."
            }
        ]
    },
    {
        "id": 6,
        "title": "Testing Point Collinearity",
        "subtitle": "Checking Straight-Line Alignment via Sum of Two Shorter Distances Equal to Longest (Ex 7.1 Q3)",
        "speech": (
            "Suppose a map plots three bus stops at A(1, 5), B(2, 3), and C(-2, -11) from Exercise Seven Point One Question Three! Do all three bus stops sit cleanly along ONE single straight road, meaning are they COLLINEAR? "
            "Watch how cleanly the Distance Formula settles collinearity without ever needing slopes or graphing paper! Compute ALL THREE pairwise distances AB, BC, and CA! "
            "First, AB equals square root of (2 minus 1) squared plus (3 minus 5) squared equals square root of (1 plus 4) equals square root of 5! "
            "Second, BC equals square root of (-2 minus 2) squared plus (-11 minus 3) squared equals square root of (16 plus 196) equals square root of 212! "
            "Third, CA equals square root of (-2 minus 1) squared plus (-11 minus 5) squared equals square root of (9 plus 256) equals square root of 265! "
            "Compare carefully: does the sum of the two shorter segments AB plus BC (root 5 plus root 212) equal longest segment CA (root 265)? Wait, approximately 2.24 plus 14.56 equals 16.80, whereas root 265 equals only 16.28! Since AB plus BC does NOT equal AC, these points are NOT collinear along one line!"
        ),
        "checkpoints": [
            {
                "question": "How do you prove three coordinate points A, B, and C ARE collinear using Distance Formula?",
                "options": [
                    "Show that the sum of the TWO shorter distances equals the LONGEST distance (e.g., AB + BC = AC)",
                    "Show that AB² + BC² = AC²",
                    "Show that AB = BC = AC",
                    "Show that all x-coordinates are positive"
                ],
                "answer": 0,
                "hint": "By Triangle Inequality, three non-collinear points satisfy AB + BC > AC strictly!",
                "explanation": "If B lies directly on segment AC, straight distance along AC equals AB + BC; otherwise AB + BC > AC."
            },
            {
                "question": "Test whether points A(1, 5), B(2, 3), and C(−2, −11) (Ex 7.1 Q3) are collinear:",
                "options": [
                    "Not collinear  (AB = √5, BC = √212, AC = √265, and √5 + √212 ≠ √265)",
                    "Collinear cleanly (√5 + √212 = √265)",
                    "Form an equilateral triangle",
                    "Form a right triangle with hypotenuse √265"
                ],
                "answer": 0,
                "hint": "Square √5 + √212 vs √265 cleanly: 5 + 212 + 2√1060 ≈ 282 ≠ 265!",
                "explanation": "Since AB + BC ≈ 16.80 ≠ AC ≈ 16.28, points A, B, C do not lie on a straight line."
            }
        ]
    },
    {
        "id": 7,
        "title": "Equidistant Axis Loci",
        "subtitle": "Finding Equidistant Points (x, 0) / (0, y) & Linear Relation 3x + y = 5 (Ex 7.1 Q7-10)",
        "speech": (
            "Now conquer the favorite Class Ten geometry board exam problems closing out Exercise Seven Point One: Equidistant Axis Points and Straight Loci! "
            "Whenever a problem says point P is EQUIDISTANT from point A and point B, immediately write PA equals PB, and smartly square BOTH sides right away into PA squared equals PB squared so ugly square root signs vanish cleanly in one second! "
            "Test Exercise Seven Point One Question Seven carefully: Find the exact point on the x axis equidistant from (2, -5) and (-2, 9)! Since point P sits along the horizontal x axis, set P as (x, 0)! "
            "Equate squared distances cleanly: (x minus 2) squared plus (0 minus -5) squared equals (x minus -2) squared plus (0 minus 9) squared! Expand smoothly so x squared cancels cleanly from BOTH sides! "
            "We get minus 4x plus 29 equals plus 4x plus 85, giving 8x equals minus 56 and x equals minus 7, giving point (-7, 0)! "
            "Similarly in Exercise Question Ten, setting a general point (x, y) strictly equidistant from (3, 6) and (-3, 4) cancels BOTH x squared and y squared cleanly, delivering the perpendicular bisector line equation 3x plus y equals 5!"
        ),
        "checkpoints": [
            {
                "question": "Find the point on the y-axis equidistant from A(6, 5) and B(−4, 3) (Textbook Example 5):",
                "options": [
                    "(0, 9)",
                    "(0, 4)",
                    "(9, 0)",
                    "(0, −9)"
                ],
                "answer": 0,
                "hint": "Set P(0, y) and solve (0 − 6)² + (y − 5)² = (0 + 4)² + (y − 3)²!",
                "explanation": "36 + y² − 10y + 25 = 16 + y² − 6y + 9 ⟹ 61 − 10y = 25 − 6y ⟹ 4y = 36 ⟹ y = 9 ⟹ (0, 9)."
            },
            {
                "question": "If Q(0, 1) is equidistant from P(5, −3) and R(x, 6) (Ex 7.1 Q9), find the possible values of x:",
                "options": [
                    "x = ±4  (since QP² = 25 + 16 = 41 forces x² + 25 = 41 ⟹ x² = 16)",
                    "x = +4 only",
                    "x = ±5",
                    "x = ±√41"
                ],
                "answer": 0,
                "hint": "Don't drop the negative root when solving x² = 16!",
                "explanation": "QP² = (5−0)² + (−3−1)² = 41; QR² = x² + (6−1)² = x² + 25 = 41 ⟹ x² = 16 ⟹ x = +4 or −4."
            }
        ]
    },
    {
        "id": 8,
        "title": "Deriving Section Formula",
        "subtitle": "Deriving Internal Division P(x, y) Using AA Similarity (Section 7.3)",
        "speech": (
            "Now step boldly into Section Seven Point Three: the celebrated Internal Section Formula! Suppose line segment AB connects endpoints A at (x1, y1) and B at (x2, y2), and an interior point P at (x, y) divides segment AB internally in exact ratio m1 is to m2! "
            "How do we derive exact coordinates (x, y) from scratch? Notice our Chapter Six superstar: AA Triangle Similarity! Drop perpendiculars AR, PS, and BT straight down onto the x axis, and draw horizontal legs AQ and PC! "
            "Because horizontal lines AQ and PC run strictly parallel, corresponding angles match identically along slanted line AB alongside crisp ninety degree right angles! By AA Similarity, right triangle PAQ is strictly similar to right triangle BPC! "
            "Therefore side ratios match ratio m1 over m2: horizontal leg AQ over PC equals AP over PB equals m1 over m2! Substitute horizontal gaps (x minus x1) over (x2 minus x) equals m1 over m2! "
            "Cross multiply cleanly and solve for coordinate x step by step: m1 x2 minus m1 x equals m2 x minus m2 x1, grouping terms cleanly to yield x equals (m1 x2 plus m2 x1) divided by (m1 plus m2), and identically for vertical y!"
        ),
        "checkpoints": [
            {
                "question": "Which Chapter 6 theorem is used in NCERT Section 7.3 to derive the Internal Section Formula?",
                "options": [
                    "AA Similarity Criterion (proving right △PAQ ~ right △BPC)",
                    "SSS Congruence",
                    "Tangent-Secant Theorem",
                    "Converse of Pythagoras alone"
                ],
                "answer": 0,
                "hint": "Horizontal lines AQ ∥ PC and vertical lines QS ∥ BT form two equiangular right triangles!",
                "explanation": "AA Similarity gives AQ/PC = PQ/BC = AP/PB = m₁/m₂, yielding x = (m₁x₂ + m₂x₁)/(m₁ + m₂) and y = (m₁y₂ + m₂y₁)/(m₁ + m₂)."
            },
            {
                "question": "Find coordinates of the point dividing the join of A(−1, 7) and B(4, −3) internally in ratio 2 : 3 (Ex 7.2 Q1):",
                "options": [
                    "(1, 3)",
                    "(2, 1)",
                    "(3, 1)",
                    "(1.5, 2)"
                ],
                "answer": 0,
                "hint": "Remember to cross-multiply weights: m₁ = 2 multiplies B(4, −3) while m₂ = 3 multiplies A(−1, 7)!",
                "explanation": "x = (2·4 + 3·(−1))/(2+3) = 5/5 = 1; y = (2·(−3) + 3·7)/5 = 15/5 = 3 ⟹ (1, 3)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch7 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 7: Coordinate Geometry
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (no Niharika, Preet, Champa, Chameli, Rashmi, Raghav, etc.), zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Midpoint Special Case",
        "subtitle": "Mid-Point Formula ((x₁+x₂)/2, (y₁+y₂)/2), Circle Diameter Endpoints & Parallelograms",
        "speech": (
            "Now inspect the sleekest special case of our Internal Section Formula: when ratio m1 is to m2 equals 1 is to 1! Setting m1 equals 1 and m2 equals 1 inside (m1 x2 plus m2 x1) divided by (m1 plus m2) collapses immediately to simple average (x1 plus x2) divided by 2! "
            "Likewise vertical height becomes (y1 plus y2) divided by 2! That gives our super clean Midpoint Formula: simply average the two x coordinates and average the two y coordinates! "
            "Watch how effortlessly the Midpoint Formula solves TWO classic Exercise Seven Point Two riddles! Riddle One (Question Seven): Point A sits on a circle whose center O is (2, -3) and opposite diameter endpoint B is (1, 4)! Find endpoint A! "
            "Since circle center O MUST be the exact midpoint of diameter AB, set (x plus 1) over 2 equals 2 and (y plus 4) over 2 equals minus 3, solving cleanly to A(3, -10)! "
            "Riddle Two (Question Six): Given four parallelogram vertices (1, 2), (4, y), (x, 6), and (3, 5) in cyclic order! Remember parallelogram diagonals ALWAYS bisect each other at one shared midpoint, giving x equals 6 and y equals 3!"
        ),
        "checkpoints": [
            {
                "question": "If AB is a diameter of a circle with center (2, −3) and point B is (1, 4) (Exercise 7.2 Q7), find the coordinates of A:",
                "options": [
                    "(3, −10)",
                    "(1.5, 0.5)",
                    "(0, −7)",
                    "(3, 10)"
                ],
                "answer": 0,
                "hint": "Center (2, −3) is the midpoint of A(x, y) and B(1, 4) ⟹ (x + 1)/2 = 2 and (y + 4)/2 = −3!",
                "explanation": "x + 1 = 4 ⟹ x = 3; y + 4 = −6 ⟹ y = −10 ⟹ A(3, −10)."
            },
            {
                "question": "If (1, 2), (4, y), (x, 6), and (3, 5) are vertices of a parallelogram taken in order (Ex 7.2 Q6), find x and y:",
                "options": [
                    "x = 6,  y = 3",
                    "x = 4,  y = 5",
                    "x = 5,  y = 4",
                    "x = 6,  y = 7"
                ],
                "answer": 0,
                "hint": "Equate Midpoint(diagonal AC) = Midpoint(diagonal BD): ((1+x)/2, (2+6)/2) = ((4+3)/2, (y+5)/2)!",
                "explanation": "1 + x = 4 + 3 = 7 ⟹ x = 6; and 2 + 6 = y + 5 ⟹ y = 3."
            }
        ]
    },
    {
        "id": 10,
        "title": "Finding Division Ratios",
        "subtitle": "The k : 1 Single-Variable Shortcut to Find Ratios When Split Point Is Known (Ex 7 & Ex 7.2 Q4)",
        "speech": (
            "Suppose a geometry question turns completely around: instead of asking WHERE dividing point P sits, it GIVES you endpoint A, endpoint B, AND point P, then asks in what RATIO point P divides segment AB! "
            "Could you write m1 and m2 with two separate unknowns? Never waste effort juggling TWO variables when ONE single unknown solves it twice as fast! "
            "Adopt NCERT's golden k is to 1 Ratio Trick! Divide both terms m1 is to m2 by m2, renaming the unknown ratio cleanly as k is to 1 (where k equals m1 over m2)! Now section formula takes only ONE unknown k: (k x2 plus x1) divided by (k plus 1)! "
            "Test immediately on Exercise Seven Point Two Question Four: in what ratio does point P(-1, 6) divide the segment joining A(-3, 10) and B(6, -8)? "
            "Plug ONLY the x coordinates into k is to 1: (6k minus 3) over (k plus 1) equals minus 1! Cross multiplying gives 6k minus 3 equals minus k minus 1, yielding 7k equals 2 -> k equals 2 over 7, or exact ratio 2 is to 7! Verify y right away: (2 times minus 8 plus 7 times 10) divided by 9 equals 54 over 9 equals 6!"
        ),
        "checkpoints": [
            {
                "question": "Why is assuming ratio k : 1 better than m₁ : m₂ when finding an unknown division ratio?",
                "options": [
                    "It reduces two unknowns (m₁, m₂) into a single variable k = m₁/m₂, letting just ONE coordinate equation solve k immediately",
                    "Because every segment always divides at 1 unit length",
                    "Because k must equal zero",
                    "Because Distance Formula requires k : 1"
                ],
                "answer": 0,
                "hint": "Once you find k = p/q cleanly from x (or y), the ratio is immediately p : q!",
                "explanation": "Setting m₁:m₂ = k:1 produces a single-variable linear equation in k, solving the exact ratio fast."
            },
            {
                "question": "In what ratio does P(−4, 6) divide the segment joining A(−6, 10) and B(3, −8) (Textbook Example 7)?",
                "options": [
                    "2 : 7  (check: (2·3 + 7·(−6))/9 = −36/9 = −4)",
                    "7 : 2",
                    "3 : 4",
                    "1 : 3"
                ],
                "answer": 0,
                "hint": "Set (3k − 6)/(k + 1) = −4 ⟹ 3k − 6 = −4k − 4!",
                "explanation": "7k = 2 ⟹ k = 2/7, giving exact internal ratio 2 : 7."
            }
        ]
    },
    {
        "id": 11,
        "title": "Points Of Trisection",
        "subtitle": "Splitting Segments Into 3 Equal Parts (1:2 & 2:1) & 4 Equal Parts via Repeated Midpoints",
        "speech": (
            "Now master multi point division from Textbook Example Eight and Exercise Seven Point Two Questions Two and Nine: Points of Trisection AND Four Equal Parts! "
            "First clarify the exact meaning of TRISECTION! Trisecting a line segment AB means cutting it cleanly into THREE strictly EQUAL subsegments AP equals PQ equals QB using TWO interior dividing points P and Q! "
            "Pause and verify the exact ratio for EACH point before calculating! Point P sits ONE equal piece away from A and TWO equal pieces away from B, so P divides AB internally in exact ratio 1 is to 2! "
            "Meanwhile Point Q sits TWO equal pieces away from A and ONE equal piece away from B, so Q divides AB internally in exact ratio 2 is to 1 (or even faster, Q is simply the exact midpoint of P and B)! "
            "Test Exercise Seven Point Two Question Two joining (4, -1) and (-2, -3): Point P using 1 is to 2 gives (2, -5/3), while Point Q using 2 is to 1 gives (0, -7/3)! "
            "Even slicker for splitting into FOUR equal parts (Question Nine): simply compute Midpoint Q of segment AB first, then take Midpoint P of AQ and Midpoint R of QB!"
        ),
        "checkpoints": [
            {
                "question": "If points P and Q TRISECT line segment AB (creating AP = PQ = QB), in what internal ratios do P and Q divide AB?",
                "options": [
                    "P divides AB in ratio 1 : 2, and Q divides AB in ratio 2 : 1",
                    "Both divide AB in ratio 1 : 3",
                    "P divides in 1 : 3 and Q divides in 2 : 3",
                    "P divides in 1 : 1 and Q divides in 2 : 1"
                ],
                "answer": 0,
                "hint": "Count equal pieces to the LEFT and RIGHT of P, and then to the LEFT and RIGHT of Q!",
                "explanation": "P has 1 piece before it and 2 after (1:2); Q has 2 pieces before it and 1 after (2:1)."
            },
            {
                "question": "Find the coordinates of the points of trisection P (1:2) and Q (2:1) of the segment joining (4, −1) and (−2, −3) (Ex 7.2 Q2):",
                "options": [
                    "P(2, −5/3)  and  Q(0, −7/3)",
                    "P(1, −2)  and  Q(−1, −2.5)",
                    "P(0, −7/3)  and  Q(2, −5/3)",
                    "P(3, −4/3)  and  Q(1, −8/3)"
                ],
                "answer": 0,
                "hint": "For P(1:2): x = (1·(−2) + 2·4)/3 = 6/3 = 2; for Q(2:1): x = (2·(−2) + 1·4)/3 = 0!",
                "explanation": "Ratio 1:2 yields P(2, −5/3); ratio 2:1 yields Q(0, −7/3)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rhombus Area Formula",
        "subtitle": "Computing Rhombus Area (½ × d₁ × d₂) & Shape Verification From Coordinates (Ex 7.2 Q10)",
        "speech": (
            "Look carefully at the brilliant grand finale of Exercise Seven Point Two, Question Ten: Find the exact area of a rhombus whose vertices taken strictly in cyclic order are A(3, 0), B(4, 5), C(-1, 4), and D(-2, -1)! "
            "Notice that our NCERT Reprint syllabus computes rhombus area cleanly without needing any Heron or determinant area formulas—strictly using Distance Formula plus classic Rhombus Area Geometry! "
            "Recall that the diagonals of ANY rhombus bisect each other perpendicularly at ninety degrees, cutting the diamond cleanly into four identical right triangles whose total area equals ONE HALF times Diagonal One times Diagonal Two! "
            "Let us compute Diagonal AC joining (3, 0) to (-1, 4) right away: (-1 minus 3) squared plus (4 minus 0) squared gives 16 plus 16 equals 32, meaning AC equals four root two units! "
            "Next compute Diagonal BD joining (4, 5) directly to (-2, -1): (-2 minus 4) squared plus (-1 minus 5) squared gives 36 plus 36 equals 72, meaning BD equals six root two units! "
            "Multiply both diagonal lengths neatly together: one half times four root two times six root two equals half times 48, giving exact rhombus area 24 square units cleanly!"
        ),
        "checkpoints": [
            {
                "question": "Find the area of the rhombus whose cyclic vertices are (3, 0), (4, 5), (−1, 4), and (−2, −1) (Exercise 7.2 Q10):",
                "options": [
                    "24 square units",
                    "48 square units",
                    "12√2 square units",
                    "36 square units"
                ],
                "answer": 0,
                "hint": "Compute diagonals AC = √32 = 4√2 and BD = √72 = 6√2, then apply ½ × d₁ × d₂!",
                "explanation": "Area = ½ × (4√2) × (6√2) = ½ × 24 × 2 = 24 square units."
            },
            {
                "question": "Which formula computes rhombus area directly from opposite-vertex diagonals AC and BD using Section 7.2 & 7.3 tools?",
                "options": [
                    "Area = ½ × AC × BD  (half the product of its perpendicular diagonals)",
                    "Area = AC + BD",
                    "Area = (AC × BD) / 4",
                    "Area = AC² + BD²"
                ],
                "answer": 0,
                "hint": "Rhombus diagonals intersect at 90°, splitting it like a kite into triangles of total area ½ d₁ d₂!",
                "explanation": "Perpendicular diagonals d₁ and d₂ yield Rhombus Area = ½ · d₁ · d₂ cleanly via the Distance Formula."
            }
        ]
    },
    {
        "id": 13,
        "title": "Axis Cut Problems",
        "subtitle": "Finding x-Axis (y=0) & y-Axis (x=0) Intercept Ratios + Fractional Split AP = (3/7)AB (Ex 7.2 Q5, Q8)",
        "speech": (
            "Now conquer two slick Exercise Seven Point Two questions where students frequently trip over hidden clues! "
            "Clue One (Question Five): Find the ratio in which the line segment joining A(1, -5) and B(-4, 5) is divided by the X AXIS, AND find the exact intersection point! Wait, the question never gave us the dividing point coordinates! Where is our hidden equation? "
            "Every single point sitting directly on the x axis MUST have y coordinate equal to ZERO! So write cutting point P as (x, 0) with unknown ratio k is to 1! Set the y Section Formula directly equal to zero: (5k minus 5) divided by (k plus 1) equals zero, giving 5k equals 5 -> k equals 1 (ratio 1 is to 1 midpoint)! Plug k equals 1 into x to get (-3/2, 0)! "
            "Clue Two (Question Eight): Find point P on segment AB joining A(-2, -2) and B(2, -4) such that AP equals three sevenths of WHOLE segment AB! Careful—ratio AP over PB is NOT 3 is to 7! Since AP takes 3 parts out of 7 total parts, remaining PB leaves 7 minus 3 equals 4 parts, giving ratio 3 is to 4 -> P(-2/7, -20/7)!"
        ),
        "checkpoints": [
            {
                "question": "Find the ratio in which the x-axis divides the segment joining A(1, −5) and B(−4, 5), AND find the cut point (Ex 7.2 Q5):",
                "options": [
                    "Ratio 1 : 1  and cut point (−3/2, 0)",
                    "Ratio 1 : 4  and cut point (−3/5, 0)",
                    "Ratio 2 : 1  and cut point (0, −3/2)",
                    "Ratio 4 : 1  and cut point (−3, 0)"
                ],
                "answer": 0,
                "hint": "On the x-axis, y = 0 ⟹ solve (k(5) + 1(−5))/(k + 1) = 0 cleanly!",
                "explanation": "5k − 5 = 0 gives k = 1 (1 : 1 ratio); midpoint x = (1 + (−4))/2 = −3/2 ⟹ (−3/2, 0)."
            },
            {
                "question": "If point P lies on segment AB such that AP = (3/7) AB (Exercise 7.2 Q8), what is the internal ratio AP : PB?",
                "options": [
                    "3 : 4  (since PB = AB − (3/7)AB = (4/7)AB)",
                    "3 : 7",
                    "7 : 3",
                    "4 : 3"
                ],
                "answer": 0,
                "hint": "Out of 7 total equal pieces along AB, AP spans 3 pieces so remaining PB spans 7 − 3 = 4 pieces!",
                "explanation": "Section Formula uses part-to-part ratio AP : PB = 3 : (7 − 3) = 3 : 4, never part-to-whole 3 : 7."
            }
        ]
    },
    {
        "id": 14,
        "title": "Sports Track Flags",
        "subtitle": "Solving the Rectangular Chalk Track Flag Problem Using Distance & Midpoint (Ex 7.2 Q3)",
        "speech": (
            "Now solve Exercise Seven Point Two Question Three, the beloved Sports Day rectangular chalk track problem, using purely neutral labels with zero fictional names! "
            "Picture a rectangular school ground ABCD marked with vertical chalk lines spaced one meter apart horizontally along AD, plus 100 flower pots stacked one meter apart vertically up along AB! "
            "Runner One sprints one fourth of the full distance AD (one fourth of 100 equals 25 meters) along the second line, posting a green flag squarely at coordinate G(2, 25)! "
            "Runner Two sprints one fifth of the full distance AD (one fifth of 100 equals 20 meters) along the eighth line, posting a red flag squarely at coordinate R(8, 20)! "
            "Question A asks: what is the straight flying distance between BOTH flags G(2, 25) and R(8, 20)? Apply Distance Formula cleanly: square root of (8 minus 2) squared plus (20 minus 25) squared equals square root of 36 plus 25 equals square root of 61 meters! "
            "Question B asks: if a third runner must place a blue flag exactly halfway along the straight line joining G and R, apply Midpoint Formula cleanly: x equals (2 plus 8)/2 equals 5th line, and y equals (25 plus 20)/2 equals 22.5 meters!"
        ),
        "checkpoints": [
            {
                "question": "On the 100-pot rectangular track (Ex 7.2 Q3), Green Flag sits on Line 2 at 1/4 of 100 m, and Red Flag sits on Line 8 at 1/5 of 100 m. Find the distance between the two flags:",
                "options": [
                    "√61 m  [distance between (2, 25) and (8, 20)]",
                    "√11 m",
                    "√85 m",
                    "11 m"
                ],
                "answer": 0,
                "hint": "Compute √[(8 − 2)² + (20 − 25)²] = √(6² + (−5)²)!",
                "explanation": "Coordinates are G(2, 25) and R(8, 20); GR = √(36 + 25) = √61 m."
            },
            {
                "question": "Where should the blue halfway flag be posted exactly midway along the segment joining G(2, 25) and R(8, 20)?",
                "options": [
                    "On the 5th line at a height of 22.5 m  [(5, 22.5)]",
                    "On the 5th line at 25 m",
                    "On the 4th line at 22.5 m",
                    "On the 6th line at 20 m"
                ],
                "answer": 0,
                "hint": "Average coordinates via Midpoint Formula: ((2+8)/2, (25+20)/2)!",
                "explanation": "Midpoint = ((2+8)/2, (25+20)/2) = (5, 22.5), placing the blue flag on the 5th line at 22.5 m."
            }
        ]
    },
    {
        "id": 15,
        "title": "Algebra Geometry Bridge",
        "subtitle": "Connecting Distance & Section Formulas to Medians, Centroids & Perpendicular Bisectors",
        "speech": (
            "Discover how seamlessly Distance Formula, Midpoint Formula, and Internal Section Formula join forces to unlock deeper geometric centers inside any triangle ABC with vertices (x1, y1), (x2, y2), and (x3, y3)! "
            "Recall from geometry that a triangle's MEDIAN connects any vertex directly to the exact MIDPOINT of its opposite side, and all three medians always meet concurrently at one balance point called the CENTROID G! "
            "Even cooler, remember the classic property of a triangle Centroid: G divides every median internally from vertex toward base in exact ratio 2 is to 1! Watch our Section Formula derive the Centroid Formula cleanly in two quick moves! "
            "Move One: Midpoint D of opposite base BC equals ((x2 plus x3)/2, (y2 plus y3)/2)! Move Two: Apply Internal Section Formula cleanly using ratio 2 is to 1 starting from vertex A(x1, y1) toward midpoint D! "
            "Multiplying midpoint D by factor 2 neatly cancels denominator 2, leaving horizontal average (x1 plus x2 plus x3) divided by 3, and vertically (y1 plus y2 plus y3) divided by 3! "
            "That proves Centroid coordinates always equal the simple three vertex arithmetic average along both coordinate axes, bridging school algebra directly with balanced geometric physical centers!"
        ),
        "checkpoints": [
            {
                "question": "How does Section Formula derive the Centroid G of △ABC given vertices A(x₁, y₁), B(x₂, y₂), C(x₃, y₃) (Ex 7.3/Extension logic)?",
                "options": [
                    "Find midpoint D of BC via Midpoint Formula, then divide median AD internally in ratio 2 : 1 via Section Formula ⟹ ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)",
                    "Multiply all coordinates by 3",
                    "Divide AB in ratio 1 : 2 only",
                    "Use Distance Formula squared"
                ],
                "answer": 0,
                "hint": "Set m₁ = 2 multiplying D((x₂+x₃)/2, (y₂+y₃)/2) and m₂ = 1 multiplying A(x₁, y₁), divided by 2 + 1 = 3!",
                "explanation": "G = (2·((x₂+x₃)/2) + 1·x₁)/3 = (x₁ + x₂ + x₃)/3 cleanly for both x and y."
            },
            {
                "question": "Find the Centroid G of the triangle with vertices A(3, −5), B(−7, 4), and C(10, −2):",
                "options": [
                    "(2, −1)",
                    "(3, −1)",
                    "(6, −3)",
                    "(2, 1)"
                ],
                "answer": 0,
                "hint": "Average all three x-values and average all three y-values: (3 − 7 + 10)/3 and (−5 + 4 − 2)/3!",
                "explanation": "x_G = (3 − 7 + 10)/3 = 6/3 = 2; y_G = (−5 + 4 − 2)/3 = −3/3 = −1 ⟹ G(2, −1)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Seven Summary",
        "subtitle": "Complete Formula Recap: Axes Points, Distance, Origin, Section Ratio & Midpoint",
        "speech": (
            "Bravo, master coordinate navigators! You have conquered every theorem, proof, and real world coordinate application across NCERT Class Ten Chapter Seven on Coordinate Geometry! Snapshot all five golden laws cleanly before entering our four Interactive Exercise Sets! "
            "One: Points along the x axis hold form x comma zero, while points along the y axis hold form zero comma y. Two: The straight distance between ANY two points (x1, y1) and (x2, y2) equals square root of (x2 minus x1) squared plus (y2 minus y1) squared, simplifying smoothly from the origin (0, 0) to square root of x squared plus y squared! "
            "Three: Classify shapes rigorously using distances: collinearity checks whether two shorter lengths sum to the longest length, while proving a Square requires equal four edges PLUS equal two diagonals! "
            "Four: Point P dividing A to B internally in ratio m1 is to m2 uses weighted average (m1 x2 plus m2 x1) divided by (m1 plus m2), while finding an unknown ratio shines fastest using k is to 1! "
            "Five: Setting equal ratio 1 is to 1 delivers Midpoint average (x1 plus x2)/2 and (y1 plus y2)/2 cleanly! Now go solve Exercises 7.1, 7.2, and our Mastery Quizzes!"
        ),
        "checkpoints": [
            {
                "question": "Identify the formula set that contains ZERO errors across Chapter 7:",
                "options": [
                    "d = √[(x₂−x₁)² + (y₂−y₁)²]; Origin d = √(x² + y²); Section = ((m₁x₂+m₂x₁)/(m₁+m₂), (m₁y₂+m₂y₁)/(m₁+m₂)); Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2)",
                    "Section x = (m₁x₁ + m₂x₂)/(m₁ + m₂)",
                    "Midpoint = ((x₂ − x₁)/2, (y₂ − y₁)/2)",
                    "Origin d = x + y"
                ],
                "answer": 0,
                "hint": "Check carefully which endpoint x₂ gets multiplied by first ratio term m₁!",
                "explanation": "Option 1 states all four Chapter 7 formulas with exact signs, cross-multiplied weights, and midpoint averages."
            },
            {
                "question": "What is the distance between (−5, 7) and (−1, 3) (Exercise 7.1 Q1 ii)?",
                "options": [
                    "4√2 units",
                    "8 units",
                    "2√2 units",
                    "16 units"
                ],
                "answer": 0,
                "hint": "Compute √[(−1 − (−5))² + (3 − 7)²] = √[4² + (−4)²] = √32!",
                "explanation": "√(4² + (−4)²) = √32 = √(16 × 2) = 4√2 units."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch7 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 1: Orienting Yourself: The Use of Coordinates
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 1.4 Distance Formula, Reflections, Exercises & Chapter Summary
with 1-3 word headings, 195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Distance Theorem Derivation",
        "subtitle": "Section 1.4 Distance Between Two Points: Right Triangle Legs |x₂ - x₁| & |y₂ - y₁| via Baudhāyana-Pythagoras Theorem",
        "speech": (
            "Suppose we know the exact coordinates of two points P and Q anywhere in the plane—how do we compute the straight-line distance between them without holding up a physical ruler? "
            "Welcome to Section One Point Four: Distance Between Two Points! Let point P have coordinates x-one comma y-one and point Q have coordinates x-two comma y-two! "
            "Draw a horizontal line through P and a vertical line through Q until they meet sharply at a third corner R! "
            "Because horizontal and vertical grid lines stand perpendicular to each other, angle PRQ forms an exact ninety-degree right angle, creating a crisp right triangle PRQ with segment PQ as its hypotenuse! "
            "Now read off both perpendicular leg lengths straight from the coordinates! "
            "Moving horizontally from P to R spans the horizontal shift: absolute value of x-two minus x-one! "
            "Moving vertically from R to Q spans the vertical shift: absolute value of y-two minus y-one! "
            "By the classic Baudhāyana-Pythagoras Theorem—that the square on the hypotenuse equals the sum of the squares on the two perpendicular sides—we immediately obtain PQ squared equals x-two minus x-one whole squared plus y-two minus y-one whole squared! "
            "Geometry and algebra lock hands cleanly! Drag any corner below to watch the triangle form dynamically!"
        ),
        "checkpoints": [
            {
                "question": "When forming right triangle PRQ between P(x₁, y₁) and Q(x₂, y₂) using horizontal and vertical grid lines, what are the lengths of its two perpendicular legs?",
                "options": [
                    "|x₂ - x₁| (horizontal run) and |y₂ - y₁| (vertical rise)",
                    "|x₁ + y₁| and |x₂ + y₂|",
                    "|x₂ - y₁| and |x₁ - y₂|",
                    "x₁ · x₂ and y₁ · y₂"
                ],
                "answer": 0,
                "hint": "Horizontal leg tracks difference in x-coordinates; vertical leg tracks difference in y-coordinates!",
                "explanation": "Corner R(x₂, y₁) gives horizontal leg PR = |x₂ - x₁| and vertical leg RQ = |y₂ - y₁|, perpendicular at R."
            },
            {
                "question": "If P is at (1, 2) and Q is at (4, 6), what are the horizontal and vertical leg lengths of the right triangle PRQ?",
                "options": [
                    "Horizontal leg = 3 units and vertical leg = 4 units",
                    "Horizontal leg = 5 units and vertical leg = 8 units",
                    "Horizontal leg = 2 units and vertical leg = 3 units",
                    "Horizontal leg = 4 units and vertical leg = 3 units"
                ],
                "answer": 0,
                "hint": "Compute |4 - 1| for horizontal shift and |6 - 2| for vertical shift!",
                "explanation": "|x₂ - x₁| = |4 - 1| = 3 and |y₂ - y₁| = |6 - 2| = 4, forming a 3-4-5 Baudhāyana-Pythagorean triangle."
            }
        ]
    },
    {
        "id": 10,
        "title": "The Distance Formula",
        "subtitle": "Section 1.4 Formula: d = √((x₂ - x₁)² + (y₂ - y₁)²), Origin Distance √(x² + y²) & Order-Invariance",
        "speech": (
            "Take the positive square root of our Baudhāyana-Pythagorean relation to reveal the celebrated Distance Formula of coordinate geometry! "
            "Between any two points P open-parenthesis x-one comma y-one close-parenthesis and Q open-parenthesis x-two comma y-two close-parenthesis, the exact distance PQ equals square root of open-parenthesis x-two minus x-one close-parenthesis squared plus open-parenthesis y-two minus y-one close-parenthesis squared! "
            "Wait—check three powerful properties! First, squaring eliminates any minus signs cleanly, so swapping P and Q gives identical results: x-two minus x-one whole squared equals x-one minus x-two whole squared! Distance never depends on which endpoint you label first! "
            "Second, test an alignment shortcut: if two points share the same y-coordinate—say two comma five and negative four comma five—then y-two minus y-one is zero, leaving distance simply absolute value of x-two minus x-one, equal to six units! "
            "Third, measure distance directly from the Origin O zero comma zero to any point P x comma y! Setting x-one and y-one to zero yields the compact Origin Distance Formula: OP equals square root of x squared plus y squared! "
            "For example, point three comma four sits square root of nine plus sixteen, which equals five units from the Origin! Test negative and positive coordinates below to confirm invariance!"
        ),
        "checkpoints": [
            {
                "question": "What is the straight-line distance between A(-2, 1) and B(4, 9)?",
                "options": [
                    "10 units",
                    "14 units",
                    "√28 units",
                    "8 units"
                ],
                "answer": 0,
                "hint": "Find Δx = 4 - (-2) = 6 and Δy = 9 - 1 = 8, then evaluate √(6² + 8²)!",
                "explanation": "d = √((4 - (-2))² + (9 - 1)²) = √(6² + 8²) = √(36 + 64) = √100 = 10 units."
            },
            {
                "question": "How far is the point P(-5, 12) from the Origin O(0, 0)?",
                "options": [
                    "13 units",
                    "7 units",
                    "17 units",
                    "√119 units"
                ],
                "answer": 0,
                "hint": "Use OP = √(x² + y²) = √((-5)² + 12²)!",
                "explanation": "OP = √((-5)² + 12²) = √(25 + 144) = √169 = 13 units."
            }
        ]
    },
    {
        "id": 11,
        "title": "Reflections Preserving Distance",
        "subtitle": "Section 1.4 Geometric Transformations: Reflections Across Axes ((x,-y), (-x,y), (-x,-y)) Preserve Segment Lengths",
        "speech": (
            "What happens to shapes and distances when we reflect points cleanly across the coordinate axes like looking into a flat mirror? "
            "Explore Geometric Transformations in Section One Point Four! "
            "First, mirror a point P x comma y across the horizontal x-axis! Its left-right x-position stays identical, while its height y flips to the opposite side, landing at P-prime x comma negative y! "
            "Second, mirror P x comma y across the vertical y-axis! Its height y stays fixed while x flips sign, landing at negative x comma y! "
            "Third, double-reflect across both axes—equivalent to rotating one hundred eighty degrees through the Origin—sending x comma y to negative x comma negative y! "
            "Now apply the Distance Formula to verify a fundamental geometric truth: reflections are rigid isometries that preserve EVERY side length and segment distance! "
            "Why? Suppose a triangle has vertices A, B, and C, and we reflect it across the x-axis to A-prime, B-prime, and C-prime! "
            "Notice that x-differences stay unchanged and y-differences merely reverse sign—and when squared inside the Distance Formula, negative shifts square to the exact same positive values! Therefore A-prime B-prime equals AB across every segment and triangle edge—mirroring changes orientation without stretching or shrinking shape!"
        ),
        "checkpoints": [
            {
                "question": "If point P(3, -5) is reflected across the x-axis, what are the coordinates of its image P'?",
                "options": [
                    "(3, 5)",
                    "(-3, -5)",
                    "(-3, 5)",
                    "(-5, 3)"
                ],
                "answer": 0,
                "hint": "Mirroring across the horizontal x-axis keeps x unchanged and flips the sign of y!",
                "explanation": "Reflection across the x-axis transforms (x, y) → (x, -y), so (3, -5) reflects to (3, 5)."
            },
            {
                "question": "When a segment PQ is reflected across the y-axis to segment P'Q', how does the length P'Q' compare to PQ?",
                "options": [
                    "P'Q' = PQ strictly, because coordinate differences square to identical values under reflection",
                    "P'Q' becomes negative of PQ",
                    "P'Q' doubles in length when crossing into Quadrant II",
                    "P'Q' shrinks by half unless both points have positive coordinates"
                ],
                "answer": 0,
                "hint": "Check (-x₂ - (-x₁))² vs (x₂ - x₁)² inside the Distance Formula!",
                "explanation": "Axis reflections preserve all distances because (-Δx)² = (Δx)² and (-Δy)² = (Δy)², keeping the hypotenuse √(Δx² + Δy²) invariant."
            }
        ]
    },
    {
        "id": 12,
        "title": "Axes and Midpoints",
        "subtitle": "Exercises & Applications: Axes Intersections, Equidistant Axis Points & Midpoint Formula ((x₁+x₂)/2, (y₁+y₂)/2)",
        "speech": (
            "Now let us apply the Distance Formula to core end-of-chapter problems involving axes intersections, midpoints, and equidistant points! "
            "First, check where a line segment meets a coordinate axis! Suppose point A sits at two comma negative three in Quadrant Four and point B sits at two comma five in Quadrant One. "
            "Moving vertically from y equals negative three up to y equals positive five forces the segment to slice directly across the x-axis—where y equals zero—at two comma zero! "
            "Next, examine midpoints! If M is the exact midpoint joining P x-one comma y-one and Q x-two comma y-two, its coordinates equal the arithmetic average of the endpoints: M equals open-parenthesis x-one plus x-two divided by two comma y-one plus y-two divided by two close-parenthesis! "
            "You can immediately verify M using our Distance Formula: distance PM and distance MQ calculate to identical lengths, each equal to half of PQ! "
            "Now solve classic equidistance challenges: find a point P on the x-axis—written x comma zero—that lies at equal distance from A and B! "
            "Setting PA squared equals PB squared eliminates the square roots cleanly and leaves a single linear equation for x that solves directly in two steps!"
        ),
        "checkpoints": [
            {
                "question": "What are the coordinates of the midpoint M of the segment joining P(-4, 7) and Q(8, -3)?",
                "options": [
                    "(2, 2)",
                    "(4, 4)",
                    "(6, 5)",
                    "(-2, 5)"
                ],
                "answer": 0,
                "hint": "Average the x-coordinates (-4 + 8)/2 and average the y-coordinates (7 + (-3))/2!",
                "explanation": "M = ((-4 + 8)/2, (7 - 3)/2) = (4/2, 4/2) = (2, 2). Indeed PM = √(6² + (-5)²) = √61 and MQ = √(6² + (-5)²) = √61."
            },
            {
                "question": "Which point on the x-axis is equidistant from A(2, -5) and B(-2, 9)?",
                "options": [
                    "(-7, 0)",
                    "(7, 0)",
                    "(0, -7)",
                    "(2, 0)"
                ],
                "answer": 0,
                "hint": "Let P = (x, 0) and set (x - 2)² + (0 - (-5))² = (x + 2)² + (0 - 9)²!",
                "explanation": "(x - 2)² + 25 = (x + 2)² + 81 simplifies to x² - 4x + 29 = x² + 4x + 85, giving -8x = 56, so x = -7 → P(-7, 0)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Collinearity and Circles",
        "subtitle": "Exercises & Applications: Collinearity Check (AB + BC = AC) & Circle Boundary Checks Relative to Origin",
        "speech": (
            "Two more essential coordinate tests appear throughout end-of-chapter exercises: proving collinearity and testing circle boundaries! "
            "First, how do you verify whether three points A, B, and C lie on a single straight line—meaning they are collinear—using only distances? "
            "Compute all three segment lengths AB, BC, and AC via the Distance Formula! "
            "Remember the Triangle Inequality: for any non-collinear triangle, adding two side lengths strictly exceeds the third side! "
            "Therefore, points A, B, and C are collinear if and only if the two smaller distances add up EXACTLY to the largest distance, such as AB plus BC equals AC! "
            "For example, if A is zero comma zero, B is three comma four giving distance five, and C is six comma eight giving BC equal to five and AC equal to ten, then five plus five equals ten proves exact collinearity! "
            "Second, test circle boundaries centered at the Origin O zero comma zero with radius r! "
            "Compute point P's distance from the Origin: d equals square root of x squared plus y squared! "
            "If d is strictly less than r, P lies INSIDE the circle; if d equals r, P sits ON the boundary; if d exceeds r, P lies OUTSIDE!"
        ),
        "checkpoints": [
            {
                "question": "How do you prove that three points A, B, and C are collinear using the Distance Formula?",
                "options": [
                    "Show that the sum of the two shorter distances equals the longest distance (e.g., AB + BC = AC)",
                    "Show that AB = BC = AC simultaneously",
                    "Check that all three points lie in Quadrant I",
                    "Verify that AB² + BC² = AC²"
                ],
                "answer": 0,
                "hint": "Think of the Triangle Inequality becoming an exact equality when a triangle flattens into a straight line!",
                "explanation": "Three points lie on one straight line iff the two smaller pairwise distances sum exactly to the largest pairwise distance."
            },
            {
                "question": "A circle centered at the Origin O(0, 0) has radius r = 5 units. Where does the point P(-3, 4) lie relative to this circle?",
                "options": [
                    "On the circle boundary, because OP = √((-3)² + 4²) = 5 = r",
                    "Strictly inside the circle, because OP < 5",
                    "Strictly outside the circle, because OP > 5",
                    "At the centre of the circle"
                ],
                "answer": 0,
                "hint": "Compare OP = √(x² + y²) against the radius r = 5!",
                "explanation": "OP = √((-3)² + 4²) = √(9 + 16) = √25 = 5 units, which matches the radius r = 5 exactly, so P lies ON the circle."
            }
        ]
    },
    {
        "id": 14,
        "title": "Grids and Pixels",
        "subtitle": "Exercises & Applications: City Street Grid Planning Models & Computer Screen Pixel Coordinate Mappings",
        "speech": (
            "Now connect Cartesian coordinates directly to modern city street planning and computer graphics! "
            "Consider a grid-based city street plan—echoing Sindhu-Sarasvatī layouts, Jaipur, or Chandigarh—where evenly spaced avenues run north-south along x and cross-streets run east-west along y! "
            "Notice a vital real-world distinction! An aerial drone flies straight from intersection A two comma one to intersection B six comma four along the Euclidean Distance Formula: square root of four squared plus three squared equals five blocks! "
            "However, a cyclist following perpendicular paved city streets cannot cut diagonally through buildings; the grid street distance equals horizontal blocks plus vertical blocks—four plus three equals seven blocks! "
            "Next, peek inside any smartphone or computer monitor! Screen pixels use a genuine two-dimensional grid coordinate system, with ONE surprising twist! "
            "While Cartesian graphs put zero comma zero near the centre with y increasing UPWARD, computer screen pixel coordinates typically anchor Origin zero comma zero at the TOP-LEFT corner, with x increasing rightward and y increasing DOWNWARD! "
            "Understanding how axes, coordinate scales, and reference origins shift lets engineers convert effortlessly between mathematical Cartesian graphs, mobile user interfaces, animated game sprites, architectural street layouts, and crisp interactive screen pixel arrays across every modern digital device!"
        ),
        "checkpoints": [
            {
                "question": "In a city planned on perpendicular grid streets, how many blocks must a pedestrian walk along the streets from intersection (2, 1) to (5, 5), compared to straight-line aerial distance?",
                "options": [
                    "7 blocks walking along streets (|5-2| + |5-1|), versus 5 blocks straight-line Euclidean distance",
                    "5 blocks walking along streets, versus 7 blocks aerial distance",
                    "12 blocks walking along streets, versus 5 blocks aerial distance",
                    "Both street distance and aerial distance equal 5 blocks"
                ],
                "answer": 0,
                "hint": "Walking along orthogonal grid streets adds horizontal blocks Δx plus vertical blocks Δy!",
                "explanation": "Street-grid travel covers |5 - 2| + |5 - 1| = 3 + 4 = 7 blocks, whereas Euclidean distance √(3² + 4²) = 5 blocks."
            },
            {
                "question": "How do standard computer screen pixel coordinates differ from the traditional Cartesian plane?",
                "options": [
                    "Screen origin (0, 0) is placed at the top-left corner, with y increasing downward instead of upward",
                    "Screen pixel coordinates use only one number instead of an ordered pair",
                    "Screen origin (0, 0) is fixed at Quadrant III (-100, -100)",
                    "Computer screens measure x vertically and y horizontally"
                ],
                "answer": 0,
                "hint": "Think of how rows of pixels count from the top edge of a monitor downward!",
                "explanation": "Digital displays place pixel (0, 0) at the top-left corner so positive x runs right and positive y counts rows downward."
            }
        ]
    },
    {
        "id": 15,
        "title": "Coordinate Shape Areas",
        "subtitle": "Exercises & Applications: Computing Areas of Rectangles, Triangles & Shapes Using Coordinate Side Lengths",
        "speech": (
            "Coordinates not only measure distances between pairs of points—they also compute exact enclosed areas and classify geometric shapes cleanly! "
            "Suppose a rectangle has vertices A one comma two, B seven comma two, C seven comma six, and D one comma six! "
            "Since A and B share y equals two, base length AB equals seven minus one, which is six units. Since B and C share x equals seven, vertical height BC equals six minus two, which is four units! "
            "Multiplying base by height immediately delivers area six times four equals twenty-four square units—even if the rectangle sits tilted or spans across multiple quadrants! "
            "Now test a triangle with vertices O zero comma zero, P six comma zero along the x-axis, and Q two comma five! "
            "Its horizontal base along the x-axis spans six units, while the perpendicular altitude from Q down to the x-axis equals simply the absolute y-coordinate of Q, which is five units! "
            "Applying one-half times base times height yields one-half times six times five equals fifteen square units! "
            "Furthermore, computing all three side lengths with the Distance Formula lets you verify equilateral, isosceles, or right-angled triangles cleanly using Baudhāyana-Pythagoras's converse across any quadrant!"
        ),
        "checkpoints": [
            {
                "question": "What is the exact area of a triangle with vertices at O(0, 0), A(8, 0), and B(3, 5)?",
                "options": [
                    "20 square units",
                    "40 square units",
                    "15 square units",
                    "13 square units"
                ],
                "answer": 0,
                "hint": "Take OA along the x-axis as base = 8 units and vertical height = |y_B| = 5 units, then use ½ × base × height!",
                "explanation": "Base OA = 8 units along the x-axis and perpendicular altitude from B(3, 5) to the x-axis is 5 units, so Area = ½ × 8 × 5 = 20 sq units."
            },
            {
                "question": "A triangle has vertices P(0, 0), Q(3, 0), and R(0, 4). What type of triangle is ΔPQR and what is its area?",
                "options": [
                    "Right-angled triangle (sides 3, 4, 5) with area 6 square units",
                    "Equilateral triangle with area 12 square units",
                    "Right-angled triangle with area 12 square units",
                    "Isosceles triangle with area 7.5 square units"
                ],
                "answer": 0,
                "hint": "PQ lies on the x-axis (3 units) and PR lies on the y-axis (4 units); axes meet at 90°!",
                "explanation": "Since the x-axis and y-axis are perpendicular at Origin P(0,0), ΔPQR is right-angled with legs 3 and 4, hypotenuse 5, and Area = ½ × 3 × 4 = 6 sq units."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary Matrix",
        "subtitle": "Chapter Summary: Cartesian Plane Components, Axes, Ordered Pairs, Quadrant Signs, Distance Formula & Applications",
        "speech": (
            "Congratulations on reaching Slide Sixteen—our complete Chapter Summary Matrix for Orienting Yourself: The Use of Coordinates! "
            "Review every pillar you have mastered across this chapter! "
            "First, Historical Evolution: coordinate thinking grew from Sindhu-Sarasvatī perpendicular ten-metre street grids and Baudhāyana's orthogonal cords to Ujjayinī's zero-longitude prime meridian, enriched by Hipparchus, Ptolemy, Āryabhaṭa, Al-Bīrūnī, Omar Khayyām, and Brahmagupta's zero and negative numbers, before Fermat and René Descartes forged the modern algebraic plane! "
            "Second, Tactile and Practical Mapping: pin-and-thread boards at one centimetre to one foot turn architectural floor plans into touchable coordinates! "
            "Third, Two-D Cartesian Anatomy: perpendicular x-axis and y-axis intersect at Origin zero comma zero, dividing the plane counter-clockwise into Quadrants One plus-plus, Two minus-plus, Three minus-minus, and Four plus-minus! "
            "Fourth, Coordinate Rules: distance from the y-axis equals absolute x; distance from the x-axis equals absolute y; and open-parenthesis x comma y close-parenthesis equals open-parenthesis y comma x close-parenthesis if and only if x equals y! "
            "Fifth, Distance Formula and Transformations: d equals square root of delta-x squared plus delta-y squared comes straight from Baudhāyana-Pythagoras, remains invariant under axis reflections, and powers collinearity, circle, midpoint, street-grid, pixel, and area problems! Now conquer the four silent mastery quizzes ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement correctly pairs every essential rule of the 2-D Cartesian Coordinate System?",
                "options": [
                    "Origin is (0,0); perpendicular axes give 4 counter-clockwise quadrants; |x| measures distance from y-axis; |y| measures distance from x-axis",
                    "Origin is (1,1); |x| measures distance from x-axis; Quadrant III has signs (+, -)",
                    "(x, y) always equals (y, x) everywhere in the plane",
                    "Distance formula subtracts Δy² from Δx² inside the square root"
                ],
                "answer": 0,
                "hint": "Check every component carefully: Origin, counter-clockwise quadrant order, axis distances, and positive sum under the radical!",
                "explanation": "Origin (0,0), perpendicular axes creating QI–QIV counter-clockwise, |x| = distance from y-axis, and |y| = distance from x-axis are all exact."
            },
            {
                "question": "Which transformation or formula in coordinate geometry preserves every distance between reflected points?",
                "options": [
                    "Reflections across the x-axis (x,-y) and y-axis (-x,y) preserve d = √((x₂-x₁)² + (y₂-y₁)²)",
                    "Only multiplying all coordinates by 2 preserves distance",
                    "Deleting negative signs changes all right triangles into equilateral triangles",
                    "Swapping screen top-left (0,0) shifts distances inside a rectangle"
                ],
                "answer": 0,
                "hint": "Recall why squaring signed differences (-Δx)² and (-Δy)² makes reflections isometric!",
                "explanation": "Because (-Δx)² = (Δx)² and (-Δy)² = (Δy)², axis reflections are rigid transformations preserving all segment lengths."
            }
        ]
    }
]

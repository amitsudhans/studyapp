"""
Data module for Class 9 Mathematics Chapter 6: Coordinate Geometry
Syllabus: CG-4, C-4.5, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Brief History & Philosophy of Coordinate Geometry",
        "subtitle": "Unifying Algebra & Geometry: René Descartes & The Tiled Ceiling",
        "category": "History & Concepts",
        "badge": "CG-4 • Historical Foundations",
        "summary": "In the early 17th century, French philosopher and mathematician René Descartes revolutionized mathematics by discovering that geometric curves and figures can be described through algebraic equations, and vice versa. While resting in bed watching a fly crawling across the tiled ceiling, Descartes realized that the fly's exact location at any instant could be uniquely determined by its horizontal distance from one wall and its vertical distance from the adjacent wall. This profound synthesis gave birth to Analytical Geometry and the Cartesian coordinate system, named in his honor.",
        "key_points": [
            "René Descartes (1596–1650) published 'La Géométrie' in 1637, introducing coordinate geometry.",
            "Historical legend: Observing a crawling fly on a ceiling grid led to the concept of two reference lines.",
            "Unification: Transformed geometry from ruler-and-compass constructions into algebraic equations.",
            "Analytical Geometry enables solving geometric problems algebraically and visualising algebraic formulas geometrically.",
            "The coordinate plane is called the 'Cartesian Plane' in honor of Descartes (Latin: Cartesius)."
        ],
        "narration": "Welcome to Coordinate Geometry! In 1637, René Descartes looked up at his tiled ceiling and noticed a crawling fly. He realized that two perpendicular walls gave the exact position of the fly with just two numbers. This breakthrough bridged algebra and geometry, giving birth to the Cartesian plane!",
        "sim_type": "descartes_fly",
        "sim_title": "Descartes' Fly on the Ceiling Simulator",
        "checkpoints": [
            {
                "q": "Which mathematician is credited with inventing Cartesian Coordinate Geometry in 1637?",
                "options": ["Euclid", "René Descartes", "Archimedes", "Pythagoras"],
                "ans": 1,
                "exp": "René Descartes invented coordinate geometry, published in 'La Géométrie' (1637), uniting algebra and geometry."
            },
            {
                "q": "In Descartes' famous thought experiment, how was the position of the crawling fly uniquely specified?",
                "options": [
                    "By its color and speed",
                    "By measuring perpendicular distances from two adjacent walls",
                    "By drawing a circle around it",
                    "By measuring its shadow length at noon"
                ],
                "ans": 1,
                "exp": "Descartes identified the fly's position using two perpendicular distances from adjacent walls (the axes)."
            }
        ]
    },
    {
        "id": 2,
        "title": "The 2-D Cartesian Coordinate System & Four Quadrants",
        "subtitle": "Reference Axes, Abscissa, Ordinate & Signs in the Four Quadrants",
        "category": "Cartesian Coordinate System",
        "badge": "CG-4 • C-4.5 • Cartesian Plane",
        "summary": "The Cartesian coordinate system consists of two mutually perpendicular real number lines intersecting at their common zero point, known as the Origin $O(0, 0)$. The horizontal number line is the $x$-axis (its coordinate is the Abscissa), and the vertical number line is the $y$-axis (its coordinate is the Ordinate). These perpendicular axes partition the infinite 2D plane into four regions called Quadrants, numbered I, II, III, and IV in a counter-clockwise direction.",
        "key_points": [
            "The Origin $O(0, 0)$ is the reference intersection where $x = 0$ and $y = 0$.",
            "Abscissa = horizontal directed distance ($x$-coordinate); Ordinate = vertical directed distance ($y$-coordinate).",
            "Quadrant I: $x > 0, y > 0$ (signs: $+ , +$); Quadrant II: $x < 0, y > 0$ (signs: $- , +$).",
            "Quadrant III: $x < 0, y < 0$ (signs: $- , -$); Quadrant IV: $x > 0, y < 0$ (signs: $+ , -$).",
            "Points lying strictly on axes do not belong to any quadrant: on $x$-axis $(x, 0)$ and on $y$-axis $(0, y)$."
        ],
        "narration": "The Cartesian plane is divided by two perpendicular lines into four quadrants. Notice how the signs change counter-clockwise: (+, +) in Quadrant 1, (-, +) in Quadrant 2, (-, -) in Quadrant 3, and (+, -) in Quadrant 4. The horizontal value is the abscissa, and the vertical is the ordinate!",
        "sim_type": "four_quadrants",
        "sim_title": "Interactive 4-Quadrant Explorer",
        "checkpoints": [
            {
                "q": "In which quadrant does the point P(-5, -8) lie?",
                "options": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
                "ans": 2,
                "exp": "Both coordinates are negative ($x < 0$ and $y < 0$), which uniquely defines Quadrant III."
            },
            {
                "q": "A point has abscissa 0 and ordinate -7. Where does this point lie?",
                "options": ["On the positive x-axis", "In Quadrant IV", "On the negative y-axis", "At the Origin"],
                "ans": 2,
                "exp": "With $x = 0$ and $y = -7$, the point lies on the negative $y$-axis at $(0, -7)$."
            }
        ]
    },
    {
        "id": 3,
        "title": "Specifying Locations: Absolute & Relative Coordinates",
        "subtitle": "Navigating from Origin vs. Position of One Point Relative to Another",
        "category": "Relative Navigation",
        "badge": "C-4.5 • Spatial Reasoning",
        "summary": "Every point in the Cartesian plane has an absolute coordinate $(x, y)$ measured relative to the origin $(0, 0)$. However, practical navigation often requires describing the relative position of one point $B(x_2, y_2)$ with respect to another reference point $A(x_1, y_1)$. This relative displacement is given by the coordinate differences $\\Delta x = x_2 - x_1$ (horizontal displacement: East if positive, West if negative) and $\\Delta y = y_2 - y_1$ (vertical displacement: North if positive, South if negative).",
        "key_points": [
            "Absolute Position: Measured directly from the fixed origin $(0, 0)$ as $(x, y)$.",
            "Relative Position: $\\vec{AB} = (x_2 - x_1, y_2 - y_1) = (\\Delta x, \\Delta y)$.",
            "Directional mapping: $+\\Delta x = \\text{East / Right}$, $-\\Delta x = \\text{West / Left}$.",
            "Vertical mapping: $+\\Delta y = \\text{North / Up}$, $-\\Delta y = \\text{South / Down}$.",
            "Relative positioning is the foundational basis of vector displacement and robotics motion planning."
        ],
        "narration": "In daily life, we constantly describe positions relative to where we are standing. If point A is at (2, 3) and point B is at (7, 8), the relative position from A to B is plus 5 horizontally and plus 5 vertically! That's 5 units East and 5 units North.",
        "sim_type": "relative_navigator",
        "sim_title": "City Landmark Relative Navigator",
        "checkpoints": [
            {
                "q": "If your home is at A(2, 3) and the library is at B(8, 11), what is the relative position of the library from home?",
                "options": [
                    "6 units East, 8 units North",
                    "8 units East, 6 units North",
                    "10 units East, 14 units North",
                    "6 units West, 8 units South"
                ],
                "ans": 0,
                "exp": "$\\Delta x = 8 - 2 = +6$ (East) and $\\Delta y = 11 - 3 = +8$ (North)."
            },
            {
                "q": "Starting at P(-3, 4), you move 5 units East and 6 units South. What are your final coordinates?",
                "options": ["(2, -2)", "(-8, 10)", "(2, 10)", "(-2, -2)"],
                "ans": 0,
                "exp": "$x = -3 + 5 = 2$, and $y = 4 - 6 = -2$. Final position is $(2, -2)$."
            }
        ]
    },
    {
        "id": 4,
        "title": "Representing Floor Plans on a Coordinate Grid",
        "subtitle": "Architectural Layouts, Room Dimensions, and Perimeter Modeling",
        "category": "Practical Modeling",
        "badge": "C-4.5 • Floor Plan Modeling",
        "summary": "Architects, engineers, and digital CAD software represent building floor plans by placing a Cartesian grid over the architectural canvas. Room corners, partition walls, doors, and furniture are mapped as coordinate vertices. By using coordinates, room dimensions (length $= |x_2 - x_1|$, width $= |y_2 - y_1|$), wall perimeters ($2(\\text{length} + \\text{width})$), and floor surface areas ($\\text{length} \\times \\text{width}$) can be calculated instantly and validated mathematically.",
        "key_points": [
            "Floor plan blueprints map structural elements to a standard scaled 2-D coordinate grid.",
            "Horizontal wall length along $y = c$ is $|x_2 - x_1|$; vertical wall height along $x = k$ is $|y_2 - y_1|$.",
            "Rectangular room area: $\\text{Area} = |x_2 - x_1| \\times |y_2 - y_1|$ square units.",
            "Room perimeter: $P = 2(|x_2 - x_1| + |y_2 - y_1|)$ units.",
            "Enables collision detection, automated room dimension checking, and robotic vacuum path planning."
        ],
        "narration": "Architects rely heavily on coordinate grids! When designing a house, every room's corners are plotted as coordinates. If a bedroom has corners from x equals 1 to 7 and y equals 2 to 6, its length is 6 meters and width is 4 meters, giving a floor area of 24 square meters!",
        "sim_type": "floor_plan_grid",
        "sim_title": "Interactive Architectural Floor Plan Modeler",
        "checkpoints": [
            {
                "q": "A rectangular living room has corners at (2, 1), (8, 1), (8, 7), and (2, 7). What is its floor area?",
                "options": ["36 square units", "24 square units", "18 square units", "48 square units"],
                "ans": 0,
                "exp": "Length $= |8 - 2| = 6$; Width $= |7 - 1| = 6$. Floor area $= 6 \\times 6 = 36$ square units."
            },
            {
                "q": "What is the total perimeter of the room with corners at (2, 1), (8, 1), (8, 7), and (2, 7)?",
                "options": ["24 units", "36 units", "12 units", "48 units"],
                "ans": 0,
                "exp": "Perimeter $= 2(\\text{length} + \\text{width}) = 2(6 + 6) = 24$ units."
            }
        ]
    },
    {
        "id": 5,
        "title": "Distance Between Points Parallel to the Coordinate Axes",
        "subtitle": "Horizontal Distance, Vertical Distance & Absolute Value Rules",
        "category": "Distance Fundamentals",
        "badge": "CG-4 • Axis Distances",
        "summary": "When two points lie on a line parallel to one of the coordinate axes, calculating the distance between them is straightforward: for two points $A(x_1, y)$ and $B(x_2, y)$ lying on a horizontal line ($y$ constant), the distance is simply the absolute difference between their $x$-coordinates: $d = |x_2 - x_1|$. For two points $C(x, y_1)$ and $D(x, y_2)$ lying on a vertical line ($x$ constant), the distance is the absolute difference between their $y$-coordinates: $d = |y_2 - y_1|$. Distance is always a non-negative scalar quantity.",
        "key_points": [
            "Horizontal line segment ($y_1 = y_2 = y$): $d = |x_2 - x_1| = \\max(x_1, x_2) - \\min(x_1, x_2)$.",
            "Vertical line segment ($x_1 = x_2 = x$): $d = |y_2 - y_1| = \\max(y_1, y_2) - \\min(y_1, y_2)$.",
            "Perpendicular distance of point $P(x, y)$ from $x$-axis is $|y|$ (the absolute ordinate).",
            "Perpendicular distance of point $P(x, y)$ from $y$-axis is $|x|$ (the absolute abscissa).",
            "The absolute value guarantees distance is never negative, regardless of quadrant location."
        ],
        "narration": "When points share the same horizontal or vertical line, distance is just a subtraction! Between (2, 5) and (9, 5), the distance is 9 minus 2, which is 7. And remember: distance from the x-axis is always the absolute value of y!",
        "sim_type": "axis_ruler",
        "sim_title": "Axis-Parallel Dynamic Distance Ruler",
        "checkpoints": [
            {
                "q": "What is the perpendicular distance of the point P(-6, 9) from the x-axis?",
                "options": ["6 units", "9 units", "-6 units", "15 units"],
                "ans": 1,
                "exp": "Distance from the $x$-axis is given by $|y| = |9| = 9$ units."
            },
            {
                "q": "What is the distance between the two points A(-7, 4) and B(5, 4)?",
                "options": ["2 units", "12 units", "-12 units", "10 units"],
                "ans": 1,
                "exp": "Since both points have $y = 4$, distance $= |5 - (-7)| = |5 + 7| = 12$ units."
            }
        ]
    },
    {
        "id": 6,
        "title": "The Distance Formula: Derivation via Pythagoras Theorem",
        "subtitle": "Connecting Coordinate Differences to Hypotenuse of a Right Triangle",
        "category": "Distance Formula",
        "badge": "CG-4 • Distance Formula Proof",
        "summary": "To find the straight-line Euclidean distance between any two arbitrary points $P(x_1, y_1)$ and $Q(x_2, y_2)$ in the 2-D plane, we construct a right-angled triangle $\\triangle PQR$ with right angle at $R(x_2, y_1)$. The horizontal leg has length $PR = |x_2 - x_1|$ and the vertical leg has length $RQ = |y_2 - y_1|$. By the Pythagorean theorem, $PQ^2 = PR^2 + RQ^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$. Taking the positive square root gives the universal Distance Formula: $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
        "key_points": [
            "Universal Distance Formula: $d(P, Q) = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
            "Pythagorean derivation: $(\\text{Hypotenuse})^2 = (\\text{Base})^2 + (\\text{Perpendicular})^2 = (\\Delta x)^2 + (\\Delta y)^2$.",
            "Order invariance: $(x_2 - x_1)^2 = (x_1 - x_2)^2$, so order of endpoints does not change the result.",
            "Distance of any point $P(x, y)$ from the Origin $O(0, 0)$: $OP = \\sqrt{x^2 + y^2}$.",
            "Foundation of analytic geometry, metric spaces, and computational computer vision."
        ],
        "narration": "Here is the celebrated Distance Formula! By drawing horizontal and vertical lines from two points, we form a right triangle. Pythagoras theorem tells us that the square of the distance equals delta x squared plus delta y squared! Taking the square root gives our formula.",
        "sim_type": "pythagorean_distance",
        "sim_title": "Pythagorean Distance Triangle Visualizer",
        "checkpoints": [
            {
                "q": "What is the distance between points P(1, 2) and Q(4, 6)?",
                "options": ["5 units", "7 units", "25 units", "4 units"],
                "ans": 0,
                "exp": "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$ units."
            },
            {
                "q": "What is the distance of the point A(-6, 8) from the Origin O(0, 0)?",
                "options": ["14 units", "10 units", "2 units", "100 units"],
                "ans": 1,
                "exp": "$OP = \\sqrt{(-6)^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10$ units."
            }
        ]
    },
    {
        "id": 7,
        "title": "Properties of Distance & Equidistant Points",
        "subtitle": "Metric Axioms, Symmetry, and Finding Loci Equidistant from Two Points",
        "category": "Distance Properties",
        "badge": "CG-4 • Equidistant Points",
        "summary": "Euclidean distance in the Cartesian plane satisfies the three classical metric axioms: (1) Non-negativity: $d(A, B) \\ge 0$, and $d(A, B) = 0 \\iff A = B$; (2) Symmetry: $d(A, B) = d(B, A)$; (3) Triangle Inequality: $d(A, C) \\le d(A, B) + d(B, C)$. A common problem is finding a point on an axis equidistant from two given points. If a point $P(x, 0)$ on the $x$-axis is equidistant from $A(x_1, y_1)$ and $B(x_2, y_2)$, we set $PA^2 = PB^2$ and solve the resulting linear equation for $x$.",
        "key_points": [
            "Non-negativity: Distance is strictly positive between distinct points; zero only between identical points.",
            "Symmetry: Measuring from $A$ to $B$ gives identical length as measuring from $B$ to $A$.",
            "Triangle Inequality: Direct straight-line distance is always less than or equal to detour paths.",
            "Equidistant locus: All points equidistant from two points $A$ and $B$ lie on the perpendicular bisector of segment $AB$.",
            "Algebraic setup: When finding an equidistant point on the $x$-axis, assume coordinates $(x, 0)$ and equate $PA^2 = PB^2$."
        ],
        "narration": "Distance has elegant rules: it can never be negative, it is symmetric, and the straight path is always the shortest! To find a point on the x-axis equidistant from two points, we write PA squared equals PB squared and solve for x.",
        "sim_type": "equidistant_explorer",
        "sim_title": "Equidistant Point & Perpendicular Bisector Explorer",
        "checkpoints": [
            {
                "q": "Find a point on the x-axis which is equidistant from A(2, -5) and B(-2, 9).",
                "options": ["(-7, 0)", "(7, 0)", "(0, -7)", "(-5, 0)"],
                "ans": 0,
                "exp": "Let $P(x, 0)$. $(x-2)^2 + (0 - (-5))^2 = (x - (-2))^2 + (0 - 9)^2 \\implies x^2 - 4x + 29 = x^2 + 4x + 85 \\implies -8x = 56 \\implies x = -7$. So $P(-7, 0)$."
            },
            {
                "q": "If the distance between A(3, -1) and B(11, y) is 10 units, what are the possible values of y?",
                "options": ["5 or -7", "6 or -6", "7 or -5", "8 or -4"],
                "ans": 0,
                "exp": "$(11-3)^2 + (y - (-1))^2 = 10^2 \\implies 64 + (y+1)^2 = 100 \\implies (y+1)^2 = 36 \\implies y+1 = \\pm 6 \\implies y = 5 \\text{ or } -7$."
            }
        ]
    },
    {
        "id": 8,
        "title": "Midpoint of a Line Segment in the 2-D Plane",
        "subtitle": "Coordinate Averaging Formula & Geometric Center of a Segment",
        "category": "Midpoint Formula",
        "badge": "CG-4 • Midpoint Formula",
        "summary": "The midpoint $M$ of a line segment connecting two points $A(x_1, y_1)$ and $B(x_2, y_2)$ is the unique point dividing the segment into two equal segments ($AM = MB = \\frac{1}{2}AB$). Geometrically, the $x$-coordinate of $M$ is the arithmetic mean of the abscissas, and the $y$-coordinate is the arithmetic mean of the ordinates: $M = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$. This is derived by constructing congruent right triangles under segments $AM$ and $MB$.",
        "key_points": [
            "Midpoint Formula: $M = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$.",
            "Arithmetic average: Middle of horizontal span + middle of vertical span.",
            "Congruent triangles proof: $\\triangle AM P \\cong \\triangle MB Q$ via AAS or ASA congruence.",
            "Endpoint recovery: If midpoint $M(x_m, y_m)$ and one endpoint $A(x_1, y_1)$ are known, endpoint $B$ is $(2x_m - x_1, 2y_m - y_1)$.",
            "Special case of the section formula where division ratio $m : n = 1 : 1$."
        ],
        "narration": "The midpoint is simply the average of the coordinates! Add the x values and divide by 2, then add the y values and divide by 2. If you know the midpoint and one endpoint, you can easily work backwards to find the other endpoint!",
        "sim_type": "midpoint_balancer",
        "sim_title": "Interactive Midpoint Balance Simulator",
        "checkpoints": [
            {
                "q": "What are the coordinates of the midpoint of the line segment joining A(-3, 8) and B(7, -2)?",
                "options": ["(2, 3)", "(5, 3)", "(2, 6)", "(4, 6)"],
                "ans": 0,
                "exp": "$x_m = \\frac{-3 + 7}{2} = \\frac{4}{2} = 2$; $y_m = \\frac{8 + (-2)}{2} = \\frac{6}{2} = 3$. Midpoint is $(2, 3)$."
            },
            {
                "q": "If M(2, -1) is the midpoint of segment AB and A is (-2, 3), what are the coordinates of endpoint B?",
                "options": ["(6, -5)", "(0, 1)", "(6, -2)", "(4, -5)"],
                "ans": 0,
                "exp": "$x_B = 2(2) - (-2) = 4 + 2 = 6$; $y_B = 2(-1) - 3 = -2 - 3 = -5$. So $B(6, -5)$."
            }
        ]
    },
    {
        "id": 9,
        "title": "Geometric Verification: Classifying Triangles via Distance",
        "subtitle": "Equilateral, Isosceles, and Scalene Verification using Side Lengths",
        "category": "Geometric Verification",
        "badge": "CG-4 • Triangle Classification",
        "summary": "Coordinate geometry provides a powerful analytical tool to determine the exact geometric nature of figures without measuring physical drawings. Given three non-collinear vertices $A(x_1, y_1)$, $B(x_2, y_2)$, and $C(x_3, y_3)$, we compute the three side lengths $a = d(B, C)$, $b = d(C, A)$, and $c = d(A, B)$ using the distance formula. We then classify the triangle: Equilateral if all 3 sides are equal ($a = b = c$); Isosceles if any 2 sides are equal; or Scalene if all 3 sides are distinct.",
        "key_points": [
            "Compute all three side lengths: $AB$, $BC$, and $CA$ using the Distance Formula.",
            "Equilateral Triangle: $AB = BC = CA$ (all three sides equal).",
            "Isosceles Triangle: Two sides equal and third side distinct (e.g. $AB = AC \\ne BC$).",
            "Scalene Triangle: All three side lengths distinct ($AB \\ne BC \\ne CA$).",
            "Triangle Existence Criterion: The sum of any two sides must strictly exceed the third side ($a + b > c$)."
        ],
        "narration": "How can we prove what kind of triangle three points make? Calculate the lengths of all three sides! If all three are equal, it's equilateral. If two are equal, it's isosceles. And if all three are different, it's scalene!",
        "sim_type": "triangle_classifier",
        "sim_title": "Dynamic Triangle Side Length & Type Classifier",
        "checkpoints": [
            {
                "q": "The vertices of a triangle are A(0, 0), B(3, 0), and C(0, 4). What type of triangle is it by side lengths?",
                "options": ["Equilateral", "Isosceles", "Scalene", "Not a triangle"],
                "ans": 2,
                "exp": "$AB = 3$, $AC = 4$, and $BC = \\sqrt{3^2 + 4^2} = 5$. Since all three sides (3, 4, 5) are distinct, it is a Scalene triangle."
            },
            {
                "q": "The vertices of triangle ABC are A(3, 0), B(6, 4), and C(-1, 3). What is the relationship between AB and AC?",
                "options": ["AB = AC = 5 (Isosceles)", "AB = 5, AC = 6 (Scalene)", "AB = AC = 7", "AB = 3, AC = 4"],
                "ans": 0,
                "exp": "$AB = \\sqrt{(6-3)^2 + 4^2} = \\sqrt{9+16} = 5$; $AC = \\sqrt{(-1-3)^2 + 3^2} = \\sqrt{16+9} = 5$. Since $AB = AC = 5$, it is an Isosceles triangle."
            }
        ]
    },
    {
        "id": 10,
        "title": "Testing Right-Angled Triangles via Coordinates",
        "subtitle": "Converse of Pythagoras Theorem & Orthogonal Slope Properties",
        "category": "Right-Angled Triangles",
        "badge": "CG-4 • Right Triangle Detection",
        "summary": "To verify whether three given points form a right-angled triangle in the Cartesian plane, we apply the Converse of Pythagoras Theorem: if the square of the longest side (hypotenuse) equals the sum of the squares of the other two sides ($a^2 + b^2 = c^2$), the triangle is strictly right-angled. Alternatively, we can calculate the slopes of the sides: two line segments are perpendicular if and only if the product of their slopes is $-1$ ($m_1 \\cdot m_2 = -1$).",
        "key_points": [
            "Converse of Pythagoras: In $\\triangle ABC$, if $AB^2 + BC^2 = AC^2$, then $\\angle B = 90^\\circ$.",
            "The vertex opposite the longest side is always the vertex containing the right angle.",
            "Slope method: Two non-vertical lines with slopes $m_1$ and $m_2$ are perpendicular $\\iff m_1 \\cdot m_2 = -1$.",
            "Area of a right-angled triangle: $\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{perpendicular} = \\frac{1}{2} \\times AB \\times BC$.",
            "Essential for computer graphics ray tracing, orthogonal projection, and game physics engines."
        ],
        "narration": "To prove a triangle is right-angled, calculate the square of each side length! If the sum of the two smaller squares equals the largest square, then by the converse of Pythagoras theorem, it is a right-angled triangle!",
        "sim_type": "right_triangle_detector",
        "sim_title": "Interactive Right-Angle Detector & Slope Checker",
        "checkpoints": [
            {
                "q": "The points A(2, -2), B(8, 4), and C(5, 7) form a triangle. Is it right-angled?",
                "options": [
                    "Yes, right-angled at B",
                    "Yes, right-angled at A",
                    "Yes, right-angled at C",
                    "No, it is acute"
                ],
                "ans": 0,
                "exp": "$AB^2 = (6)^2 + (6)^2 = 72$; $BC^2 = (-3)^2 + (3)^2 = 18$; $AC^2 = (3)^2 + (9)^2 = 90$. Since $AB^2 + BC^2 = 72 + 18 = 90 = AC^2$, it is right-angled at vertex $B$."
            },
            {
                "q": "Which vertex contains the right angle in triangle PQR with vertices P(1, 1), Q(4, 5), and R(1, 5)?",
                "options": ["Vertex R", "Vertex P", "Vertex Q", "No right angle"],
                "ans": 0,
                "exp": "$PR$ is vertical ($x = 1$, length 4), $RQ$ is horizontal ($y = 5$, length 3). The angle between them at $R(1, 5)$ is exactly $90^\\circ$."
            }
        ]
    },
    {
        "id": 11,
        "title": "Collinearity of Three Points",
        "subtitle": "Distance Degeneracy Criterion, Slope Equality & Collinear Verification",
        "category": "Collinearity",
        "badge": "CG-4 • Collinearity Test",
        "summary": "Three or more points are Collinear if they all lie on the exact same single straight line. In coordinate geometry, there are two primary methods to verify collinearity without graphing: (1) Distance Method: Points $A, B, C$ are collinear if the sum of the distances between two pairs equals the distance between the third pair ($AB + BC = AC$ when $B$ lies between $A$ and $C$). (2) Slope Method: The slope of segment $AB$ must equal the slope of segment $BC$ ($\\frac{y_2 - y_1}{x_2 - x_1} = \\frac{y_3 - y_2}{x_3 - x_2}$).",
        "key_points": [
            "Collinear definition: Points that lie along the same straight line.",
            "Distance condition: $AB + BC = AC$ (triangle inequality collapses to equality; degenerate triangle).",
            "Slope condition: $\\text{Slope}(AB) = \\text{Slope}(BC) = \\text{Slope}(AC)$.",
            "Area criterion: The area of the triangle formed by three collinear points is exactly zero ($\\text{Area} = 0$).",
            "If $AB + BC > AC$ for all orderings, the three points form a genuine non-degenerate triangle."
        ],
        "narration": "When three points lie on a single straight line, they are collinear. You can test this in two ways: either the slopes between pairs are equal, or the sum of two smaller distances equals the total distance. If they add up, there's no triangle—just a line!",
        "sim_type": "collinearity_tester",
        "sim_title": "Collinearity Alignment & Degeneracy Tester",
        "checkpoints": [
            {
                "q": "Are the three points A(1, 5), B(2, 3), and C(-2, -11) collinear?",
                "options": [
                    "No, slope(AB) = -2 while slope(BC) = 3.5",
                    "Yes, they all lie on y = 2x + 3",
                    "Yes, AB + BC = AC",
                    "No, because all three are in different quadrants"
                ],
                "ans": 0,
                "exp": "$\\text{Slope}(AB) = \\frac{3-5}{2-1} = -2$, whereas $\\text{Slope}(BC) = \\frac{-11-3}{-2-2} = \\frac{-14}{-4} = 3.5$. Since slopes are unequal, they are not collinear."
            },
            {
                "q": "For what value of k are the points A(2, 3), B(4, k), and C(6, -3) collinear?",
                "options": ["k = 0", "k = 1", "k = -1", "k = 2"],
                "ans": 0,
                "exp": "$\\text{Slope}(AB) = \\text{Slope}(BC) \\implies \\frac{k-3}{4-2} = \\frac{-3-k}{6-4} \\implies \\frac{k-3}{2} = \\frac{-3-k}{2} \\implies k-3 = -3-k \\implies 2k = 0 \\implies k = 0$."
            }
        ]
    },
    {
        "id": 12,
        "title": "Classifying Quadrilaterals via Coordinate Geometry",
        "subtitle": "Distances, Midpoints & Diagonal Bisector Properties of 4-Sided Polygons",
        "category": "Quadrilaterals",
        "badge": "CG-4 • Quadrilateral Verification",
        "summary": "Any 4-sided polygon $ABCD$ can be definitively classified by computing side lengths, diagonal lengths, and diagonal midpoints: (1) Parallelogram: Opposite sides equal ($AB = CD$ and $BC = DA$), or diagonals $AC$ and $BD$ bisect each other (have identical midpoints). (2) Rectangle: Parallelogram with equal diagonals ($AC = BD$). (3) Rhombus: All 4 sides equal ($AB = BC = CD = DA$) and diagonals bisect perpendicularly. (4) Square: All 4 sides equal AND equal diagonals ($AC = BD$).",
        "key_points": [
            "Parallelogram test: Opposite sides equal, or Midpoint of $AC$ = Midpoint of $BD$.",
            "Rectangle test: Opposite sides equal AND diagonals equal ($AC = BD$).",
            "Rhombus test: All 4 side lengths equal ($AB = BC = CD = DA$).",
            "Square test: All 4 sides equal AND both diagonals equal ($AC = BD$).",
            "The midpoint shortcut: Checking if midpoints of diagonals coincide is often the fastest proof that a figure is a parallelogram."
        ],
        "narration": "To classify a quadrilateral, look at its four sides and two diagonals! If all four sides are equal, it's a rhombus. If its diagonals are also equal, that rhombus becomes a square! Checking if diagonals share the same midpoint is the quickest proof of a parallelogram.",
        "sim_type": "quadrilateral_inspector",
        "sim_title": "Interactive Quadrilateral Shape Inspector",
        "checkpoints": [
            {
                "q": "In quadrilateral ABCD, if the midpoint of diagonal AC equals the midpoint of diagonal BD, what can we definitively conclude?",
                "options": [
                    "ABCD is at least a parallelogram",
                    "ABCD must be a square",
                    "ABCD must be a trapezoid",
                    "ABCD is a kite"
                ],
                "ans": 0,
                "exp": "A quadrilateral whose diagonals bisect each other (share the same midpoint) is always a parallelogram."
            },
            {
                "q": "If all four sides of a quadrilateral are equal in length, but the two diagonals are NOT equal, what is the shape?",
                "options": ["A Rhombus", "A Square", "A Rectangle", "A Trapezium"],
                "ans": 0,
                "exp": "All 4 sides equal means it is a rhombus; unequal diagonals mean it is not a square."
            }
        ]
    },
    {
        "id": 13,
        "title": "Circles in Coordinate Geometry: Center & Radius",
        "subtitle": "Equation of a Circle as an Equidistant Locus & Point Position Testing",
        "category": "Circles & Loci",
        "badge": "CG-4 • Circle Geometry",
        "summary": "A circle is geometrically defined as the locus of all points $P(x, y)$ that maintain a constant distance (the radius $r$) from a fixed point (the center $C(h, k)$). Using the distance formula, $CP = r \\implies \\sqrt{(x - h)^2 + (y - k)^2} = r$. Squaring both sides yields the standard equation of a circle: $(x - h)^2 + (y - k)^2 = r^2$. For a circle centered at the origin $(0, 0)$, this simplifies to $x^2 + y^2 = r^2$. We can test any point $Q(x_1, y_1)$: if $CQ < r$ it is inside, if $CQ = r$ it lies on the circle, and if $CQ > r$ it lies outside.",
        "key_points": [
            "Circle definition: Set of all points equidistant from a fixed center $C(h, k)$.",
            "Standard Circle Equation: $(x - h)^2 + (y - k)^2 = r^2$; Origin center: $x^2 + y^2 = r^2$.",
            "Point location test: Compute distance $d$ from center: $d < r$ (Inside), $d = r$ (On Boundary), $d > r$ (Outside).",
            "Diameter endpoints: If endpoints of a diameter are $A(x_1, y_1)$ and $B(x_2, y_2)$, the center is their midpoint $M$.",
            "Radius is half the diameter: $r = \\frac{1}{2}d(A, B)$."
        ],
        "narration": "A circle is simply every point that is exactly distance r away from the center! If you calculate the distance from the center to any point, you can instantly tell if it's inside, right on the boundary, or outside the circle.",
        "sim_type": "circle_radar",
        "sim_title": "Interactive Circle Radar & Proximity Scanner",
        "checkpoints": [
            {
                "q": "A circle has center C(2, -3) and passes through the point P(5, 1). What is the radius of the circle?",
                "options": ["5 units", "25 units", "7 units", "4 units"],
                "ans": 0,
                "exp": "Radius $r = CP = \\sqrt{(5-2)^2 + (1 - (-3))^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5$ units."
            },
            {
                "q": "Does the point Q(4, 2) lie inside, on, or outside a circle centered at the origin with radius r = 5?",
                "options": ["Inside the circle", "On the boundary", "Outside the circle", "Cannot be determined"],
                "ans": 0,
                "exp": "Distance from origin $= \\sqrt{4^2 + 2^2} = \\sqrt{16+4} = \\sqrt{20} \\approx 4.47$. Since $4.47 < 5$, it lies strictly inside."
            }
        ]
    },
    {
        "id": 14,
        "title": "Real-World Modeling: GPS Navigation & Triangulation",
        "subtitle": "Manhattan vs. Euclidean Distance & Finding Lost Positions with Cell Towers",
        "category": "Real-World Applications",
        "badge": "CG-9 • GPS & Navigation",
        "summary": "Real-world navigation systems rely heavily on coordinate geometry. In urban cities laid out in rectangular blocks (like Manhattan), travel distance between two intersections is the sum of horizontal and vertical steps: Manhattan Distance $= |x_2 - x_1| + |y_2 - y_1|$. For airborne flight or GPS satellites, Euclidean Distance $= \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}$ applies. GPS satellites and cell towers locate mobile phones through Trilateration: measuring distances from three known reference stations $(x_i, y_i)$ creates three distance circles that intersect at one unique coordinate point $(x, y)$.",
        "key_points": [
            "Manhattan Distance (Taxicab metric): $d_M = |x_2 - x_1| + |y_2 - y_1|$ (travel along grid streets).",
            "Euclidean Distance (Straight-line flight): $d_E = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
            "Inequality: $d_E \\le d_M$ always holds (straight line is always shorter than or equal to grid paths).",
            "Trilateration / Triangulation: Intersecting circles from 3 transmitters uniquely resolves a 2D location.",
            "Powers Google Maps, ride-sharing routing algorithms, autonomous drones, and GPS navigation."
        ],
        "narration": "When you use GPS on your phone, you are using coordinate geometry! Satellites calculate the distance from three stations. Where all three circles overlap is your exact location. In a grid city, walking distance is Manhattan distance, while drone flight is Euclidean distance!",
        "sim_type": "gps_triangulation",
        "sim_title": "GPS Cell Tower Triangulation Station",
        "checkpoints": [
            {
                "q": "In a grid-planned city, walking from intersection (1, 2) to (6, 8) along avenues requires walking how many blocks?",
                "options": ["11 blocks", "7.8 blocks", "13 blocks", "10 blocks"],
                "ans": 0,
                "exp": "Manhattan distance $= |6 - 1| + |8 - 2| = 5 + 6 = 11$ blocks."
            },
            {
                "q": "What is the mathematical technique of determining a location by intersecting distance circles from 3 reference towers?",
                "options": ["Trilateration (Triangulation)", "Interpolation", "Extrapolation", "Factorisation"],
                "ans": 0,
                "exp": "Trilateration uses distance circles from three known base stations to pinpoint an exact position."
            }
        ]
    },
    {
        "id": 15,
        "title": "Computational Thinking: Coordinate Algorithms & Verification",
        "subtitle": "Algorithmic Geometry, Float Precision Tolerance & Complexity Analysis",
        "category": "Computational Thinking",
        "badge": "CG-9 • Computational Geometry",
        "summary": "Computational geometry translates spatial relationships into discrete, efficient algorithms executed by computer software. Key algorithms include: (1) `euclideanDistance(p1, p2)` in $O(1)$ time; (2) `midpoint(p1, p2)` in $O(1)$ time; (3) `collinearTest(p1, p2, p3)` using cross-product $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) == 0$. When implementing geometry in software, computers encounter roundoff error with floating-point numbers; hence, equality checks use an epsilon threshold $|a - b| < \\epsilon$ (typically $\\epsilon = 10^{-7}$).",
        "key_points": [
            "Algorithmic decomposition: Breaking complex geometric shapes into coordinate point arrays.",
            "Distance Algorithm: $O(1)$ arithmetic operations ($3$ subtractions, $2$ multiplications, $1$ addition, $1$ square root).",
            "Cross-Product Collinearity: $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) = 0$ avoids division by zero.",
            "Floating-Point Epsilon Tolerance: Using $|v_1 - v_2| < \\epsilon$ prevents computer precision roundoff errors.",
            "Forms the core engine of 3D game engines (Unreal, Unity), CAD modeling, robotics, and medical imaging."
        ],
        "narration": "Computers don't draw with rulers; they calculate with coordinates! Every 3D video game and robotics system runs thousands of distance and collision checks every second in constant O(1) time. We also use a tiny epsilon value to avoid computer rounding errors!",
        "sim_type": "computational_engine",
        "sim_title": "Algorithmic Computational Geometry Engine",
        "checkpoints": [
            {
                "q": "What is the computational time complexity of computing the distance between two coordinate points?",
                "options": ["O(1) Constant Time", "O(n) Linear Time", "O(n²) Quadratic Time", "O(log n)"],
                "ans": 0,
                "exp": "Distance requires a fixed sequence of basic arithmetic operations, taking $O(1)$ constant time."
            },
            {
                "q": "Why do computational geometry algorithms use an epsilon tolerance (e.g., |a - b| < 10⁻⁶) instead of direct equality (a == b)?",
                "options": [
                    "To prevent floating-point rounding inaccuracies",
                    "To make the code run slower",
                    "To round numbers to integers",
                    "Because coordinates cannot be decimals"
                ],
                "ans": 0,
                "exp": "Computers represent real numbers as floating-point approximations, so epsilon tolerances avoid false inequalities."
            }
        ]
    },
    {
        "id": 16,
        "title": "Comprehensive Synthesis & Mathematical Mindset",
        "subtitle": "Connecting History, Formulas, Geometric Proofs & Modern Frontiers",
        "category": "Mastery Synthesis",
        "badge": "CG-4 • CG-9 • Holistic Synthesis",
        "summary": "Coordinate Geometry forms the indispensable bridge connecting pure algebra and spatial geometry. Beginning with Descartes' insight and the 4-quadrant Cartesian grid, we established how any spatial point can be identified by an ordered pair $(x, y)$. From this foundation, the Distance Formula ($d = \\sqrt{\\Delta x^2 + \\Delta y^2}$) and Midpoint Formula ($M = (\\bar{x}, \\bar{y})$) enable rigorous proofs of collinearity, triangle classifications, right-angle properties, and quadrilateral attributes. Today, these exact formulas drive modern innovations in GPS navigation, robotics, autonomous vehicles, 3D CGI animation, and machine learning.",
        "key_points": [
            "Complete Pipeline: Descartes $\\to$ Axes $\\to$ Ordered Pairs $\\to$ Distance & Midpoint $\\to$ Geometric Proofs.",
            "Distance Formula powers length, perimeter, collinearity, and Pythagorean right-angle verification.",
            "Midpoint Formula powers diagonal bisector tests, centers of circles, and segment bisection.",
            "Relative displacements $(\\Delta x, \\Delta y)$ translate spatial direction into computational vectors.",
            "Analytical geometry empowers higher mathematics: vectors, calculus, differential geometry, and artificial intelligence."
        ],
        "narration": "Congratulations on mastering Coordinate Geometry! From Descartes' ceiling fly to GPS navigation and computer graphics, you now possess the algebraic tools to explore, calculate, and prove any 2D geometric property. Let's head into our mastery quiz challenges!",
        "sim_type": "master_playground",
        "sim_title": "Master Coordinate Sandbox & Multi-Tool Playground",
        "checkpoints": [
            {
                "q": "Which fundamental principle allows coordinate geometry to prove geometric properties using algebra?",
                "options": [
                    "Every geometric point is an ordered pair, and geometric relations correspond to algebraic equations",
                    "Only integers can be plotted on graphs",
                    "Geometry does not require logical proofs",
                    "Lines can only be drawn horizontally"
                ],
                "ans": 0,
                "exp": "Coordinate geometry creates a 1-to-1 isomorphism between geometric figures and algebraic equations."
            },
            {
                "q": "Which modern technology relies fundamentally on the Cartesian coordinate system?",
                "options": [
                    "GPS Satellite Navigation",
                    "3D Video Game Graphics Engines",
                    "Robotics and Autonomous Driving",
                    "All of the above"
                ],
                "ans": 3,
                "exp": "All modern spatial computational systems (GPS, 3D CGI graphics, robotics) operate on coordinate systems."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 17,
        "title": "Mastery Challenge Part 1: Cartesian Plane & Quadrants",
        "subtitle": "10 Questions on Axes, Abscissa, Ordinate, Signs & Relative Positions",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 1 • Foundations",
        "questions": [
            {
                "id": 1,
                "q": "The point (-4, 7) lies in which quadrant of the Cartesian plane?",
                "options": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
                "ans": 1,
                "solution": "In the Cartesian plane, Quadrant II is defined by $x < 0$ and $y > 0$. Here $x = -4 < 0$ and $y = 7 > 0$. Therefore, $(-4, 7)$ lies strictly in Quadrant II."
            },
            {
                "id": 2,
                "q": "What is the abscissa of the point P(-9, 4)?",
                "options": ["-9", "4", "9", "-4"],
                "ans": 0,
                "solution": "The abscissa is the $x$-coordinate of a point. For $P(-9, 4)$, the abscissa is $-9$ (and the ordinate is $4$)."
            },
            {
                "id": 3,
                "q": "A point lies on the x-axis at a distance of 5 units to the left of the origin. Its coordinates are:",
                "options": ["(0, -5)", "(-5, 0)", "(5, 0)", "(0, 5)"],
                "ans": 1,
                "solution": "Any point on the $x$-axis has $y = 0$. Five units to the left of the origin means $x = -5$. Thus, the coordinates are $(-5, 0)$."
            },
            {
                "id": 4,
                "q": "What are the coordinates of the Origin where the two axes intersect?",
                "options": ["(0, 0)", "(1, 1)", "(0, 1)", "(1, 0)"],
                "ans": 0,
                "solution": "The origin is the intersection of the $x$-axis ($y = 0$) and $y$-axis ($x = 0$), so its coordinates are $(0, 0)$."
            },
            {
                "id": 5,
                "q": "If the coordinates of a point are (a, b) where a > 0 and b < 0, in which quadrant does it lie?",
                "options": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
                "ans": 3,
                "solution": "Quadrant IV corresponds to points with a positive $x$-coordinate ($a > 0$) and a negative $y$-coordinate ($b < 0$)."
            },
            {
                "id": 6,
                "q": "The perpendicular distance of the point P(4, -7) from the y-axis is:",
                "options": ["4 units", "7 units", "-7 units", "-4 units"],
                "ans": 0,
                "solution": "The perpendicular distance of any point $(x, y)$ from the $y$-axis is given by $|x|$. For $P(4, -7)$, the distance is $|4| = 4$ units."
            },
            {
                "id": 7,
                "q": "What is the perpendicular distance of the point Q(-8, -6) from the x-axis?",
                "options": ["6 units", "8 units", "-6 units", "10 units"],
                "ans": 0,
                "solution": "The perpendicular distance of $(x, y)$ from the $x$-axis is $|y|$. For $Q(-8, -6)$, the distance is $|-6| = 6$ units."
            },
            {
                "id": 8,
                "q": "Point A is at (3, 2). Point B is located 4 units West and 5 units North of Point A. What are the coordinates of B?",
                "options": ["(-1, 7)", "(7, 7)", "(-1, -3)", "(1, -7)"],
                "ans": 0,
                "solution": "Moving West means subtracting from $x$: $x_B = 3 - 4 = -1$. Moving North means adding to $y$: $y_B = 2 + 5 = 7$. Thus, $B(-1, 7)$."
            },
            {
                "id": 9,
                "q": "Which of the following points lies on the positive y-axis?",
                "options": ["(0, 8)", "(8, 0)", "(8, 8)", "(-8, 0)"],
                "ans": 0,
                "solution": "A point on the positive $y$-axis must have $x = 0$ and $y > 0$. Point $(0, 8)$ satisfies both criteria."
            },
            {
                "id": 10,
                "q": "Points P(2, 3), Q(2, -5), and R(2, 8) all lie on:",
                "options": [
                    "A line parallel to the y-axis",
                    "A line parallel to the x-axis",
                    "The x-axis itself",
                    "The line y = x"
                ],
                "ans": 0,
                "solution": "All three points have the identical $x$-coordinate $x = 2$. The equation $x = 2$ represents a vertical line parallel to the $y$-axis."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge Part 2: The Distance Formula",
        "subtitle": "10 Questions on Distances, Origin Proximity & Equidistant Loci",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 2 • Distance Calculations",
        "questions": [
            {
                "id": 11,
                "q": "What is the distance between the points A(2, 3) and B(5, 7)?",
                "options": ["5 units", "25 units", "7 units", "4 units"],
                "ans": 0,
                "solution": "By the distance formula: $d = \\sqrt{(5 - 2)^2 + (7 - 3)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$ units."
            },
            {
                "id": 12,
                "q": "What is the distance of the point P(-5, 12) from the Origin O(0, 0)?",
                "options": ["13 units", "17 units", "7 units", "169 units"],
                "ans": 0,
                "solution": "Distance from origin: $OP = \\sqrt{(-5)^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13$ units."
            },
            {
                "id": 13,
                "q": "Find the distance between the points P(a, b) and Q(-a, -b).",
                "options": ["2√(a² + b²)", "√(a² + b²)", "2(a + b)", "0"],
                "ans": 0,
                "solution": "$d = \\sqrt{(-a - a)^2 + (-b - b)^2} = \\sqrt{(-2a)^2 + (-2b)^2} = \\sqrt{4a^2 + 4b^2} = \\sqrt{4(a^2 + b^2)} = 2\\sqrt{a^2 + b^2}$."
            },
            {
                "id": 14,
                "q": "What is the distance between the points A(0, 6) and B(0, -2)?",
                "options": ["8 units", "4 units", "-8 units", "6 units"],
                "ans": 0,
                "solution": "Both points lie on the $y$-axis ($x = 0$). Distance $= |6 - (-2)| = |6 + 2| = 8$ units."
            },
            {
                "id": 15,
                "q": "Find the value of k if the distance between (4, k) and (1, 0) is 5 units.",
                "options": ["±4", "±3", "±5", "±2"],
                "ans": 0,
                "solution": "$d^2 = (4 - 1)^2 + (k - 0)^2 = 5^2 \\implies 3^2 + k^2 = 25 \\implies 9 + k^2 = 25 \\implies k^2 = 16 \\implies k = \\pm 4$."
            },
            {
                "id": 16,
                "q": "Which point on the y-axis is equidistant from A(6, 5) and B(-4, 3)?",
                "options": ["(0, 9)", "(0, -9)", "(9, 0)", "(0, 4)"],
                "ans": 0,
                "solution": "Let point be $P(0, y)$. $PA^2 = PB^2 \\implies (0 - 6)^2 + (y - 5)^2 = (0 - (-4))^2 + (y - 3)^2 \\implies 36 + y^2 - 10y + 25 = 16 + y^2 - 6y + 9 \\implies 61 - 10y = 25 - 6y \\implies -4y = -36 \\implies y = 9$. Point is $(0, 9)$."
            },
            {
                "id": 17,
                "q": "What is the perimeter of a triangle with vertices at (0, 0), (4, 0), and (0, 3)?",
                "options": ["12 units", "7 units", "14 units", "10 units"],
                "ans": 0,
                "solution": "Side lengths: $a = |4 - 0| = 4$; $b = |3 - 0| = 3$; Hypotenuse $c = \\sqrt{4^2 + 3^2} = 5$. Total perimeter $= 4 + 3 + 5 = 12$ units."
            },
            {
                "id": 18,
                "q": "What is the distance between A(cos θ, sin θ) and B(sin θ, -cos θ)?",
                "options": ["√2", "1", "2", "0"],
                "ans": 0,
                "solution": "$d^2 = (\\sin\\theta - \\cos\\theta)^2 + (-\\cos\\theta - \\sin\\theta)^2 = (\\sin^2\\theta - 2\\sin\\theta\\cos\\theta + \\cos^2\\theta) + (\\cos^2\\theta + 2\\cos\\theta\\sin\\theta + \\sin^2\\theta) = 1 + 1 = 2$. Therefore, $d = \\sqrt{2}$."
            },
            {
                "id": 19,
                "q": "A town B is located 36 km East and 15 km North of town A(0, 0). What is the straight-line distance between them?",
                "options": ["39 km", "51 km", "45 km", "36 km"],
                "ans": 0,
                "solution": "Coordinates of town B are $(36, 15)$. Distance $d = \\sqrt{36^2 + 15^2} = \\sqrt{1296 + 225} = \\sqrt{1521} = 39$ km."
            },
            {
                "id": 20,
                "q": "If the point P(x, y) is equidistant from the points (5, 1) and (-1, 5), which linear relation holds?",
                "options": ["3x = 2y", "3x = -2y", "2x = 3y", "x = y"],
                "ans": 0,
                "solution": "$PA^2 = PB^2 \\implies (x - 5)^2 + (y - 1)^2 = (x + 1)^2 + (y - 5)^2 \\implies x^2 - 10x + 25 + y^2 - 2y + 1 = x^2 + 2x + 1 + y^2 - 10y + 25 \\implies -10x - 2y = 2x - 10y \\implies 8y = 12x \\implies 2y = 3x$ (or $3x = 2y$)."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge Part 3: Midpoints, Floor Plans & Real-World Grids",
        "subtitle": "10 Questions on Midpoints, Unknown Endpoints, Architecture & Grid Navigation",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 3 • Midpoints & Grids",
        "questions": [
            {
                "id": 21,
                "q": "Find the coordinates of the midpoint of the line segment joining (4, -5) and (8, 3).",
                "options": ["(6, -1)", "(12, -2)", "(6, -2)", "(2, 4)"],
                "ans": 0,
                "solution": "Midpoint $M = \\left( \\frac{4 + 8}{2}, \\frac{-5 + 3}{2} \\right) = \\left( \\frac{12}{2}, \\frac{-2}{2} \\right) = (6, -1)$."
            },
            {
                "id": 22,
                "q": "If M(3, 4) is the midpoint of segment AB and A is (1, 2), what are the coordinates of B?",
                "options": ["(5, 6)", "(2, 3)", "(4, 6)", "(5, 8)"],
                "ans": 0,
                "solution": "$x_B = 2(3) - 1 = 6 - 1 = 5$; $y_B = 2(4) - 2 = 8 - 2 = 6$. Therefore, $B(5, 6)$."
            },
            {
                "id": 23,
                "q": "The center of a circle is C(2, -3) and one end of a diameter is A(1, 4). What are the coordinates of the other end B?",
                "options": ["(3, -10)", "(0, -7)", "(3, -7)", "(1, -10)"],
                "ans": 0,
                "solution": "The center is the midpoint of the diameter $AB$. $x_B = 2(2) - 1 = 4 - 1 = 3$; $y_B = 2(-3) - 4 = -6 - 4 = -10$. So $B(3, -10)$."
            },
            {
                "id": 24,
                "q": "On an architectural floor plan, a hallway connects door A(3, 8) to door B(11, 8). What is the length of the hallway?",
                "options": ["8 units", "14 units", "6 units", "11 units"],
                "ans": 0,
                "solution": "Both doors share $y = 8$. Length $= |11 - 3| = 8$ units."
            },
            {
                "id": 25,
                "q": "A warehouse floor has corners at (0, 0), (12, 0), (12, 8), and (0, 8) in meters. What is the floor area in square meters?",
                "options": ["96 m²", "40 m²", "80 m²", "48 m²"],
                "ans": 0,
                "exp": "Length $= 12$ m, Width $= 8$ m. Area $= 12 \\times 8 = 96\\text{ m}^2$.",
                "solution": "The length along the $x$-axis is $12$ m and the width along the $y$-axis is $8$ m. Floor area $= \\text{length} \\times \\text{width} = 12 \\times 8 = 96\\text{ m}^2$."
            },
            {
                "id": 26,
                "q": "Find the midpoint of the line segment joining (-6, 5) and (-2, -3).",
                "options": ["(-4, 1)", "(-4, 2)", "(-8, 2)", "(-2, 1)"],
                "ans": 0,
                "solution": "$M = \\left( \\frac{-6 + (-2)}{2}, \\frac{5 + (-3)}{2} \\right) = \\left( \\frac{-8}{2}, \\frac{2}{2} \\right) = (-4, 1)$."
            },
            {
                "id": 27,
                "q": "In a taxi grid, traveling from (2, 3) to (7, 9) along streets takes how many blocks (Manhattan distance)?",
                "options": ["11 blocks", "7.8 blocks", "14 blocks", "10 blocks"],
                "ans": 0,
                "solution": "Manhattan distance $d_M = |7 - 2| + |9 - 3| = 5 + 6 = 11$ blocks."
            },
            {
                "id": 28,
                "q": "If the midpoints of the sides of a triangle are plotted, how many sub-triangles does this partition the original triangle into?",
                "options": ["4 congruent triangles", "2 triangles", "3 triangles", "6 triangles"],
                "ans": 0,
                "solution": "Connecting the three midpoints of the sides of a triangle forms the medial triangle, which partitions the original triangle into 4 smaller congruent triangles."
            },
            {
                "id": 29,
                "q": "A security camera at the origin (0, 0) detects an intruder at (9, 12). What is the straight-line distance to the intruder?",
                "options": ["15 units", "21 units", "13 units", "18 units"],
                "ans": 0,
                "solution": "$d = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15$ units."
            },
            {
                "id": 30,
                "q": "What point divides the segment joining A(1, 2) and B(7, 8) into the ratio 1 : 1?",
                "options": ["(4, 5)", "(3, 4)", "(5, 6)", "(3.5, 4.5)"],
                "ans": 0,
                "solution": "A ratio of $1 : 1$ is the midpoint: $M = \\left( \\frac{1 + 7}{2}, \\frac{2 + 8}{2} \\right) = (4, 5)$."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Part 4: Collinearity, Triangles & Quadrilaterals",
        "subtitle": "10 Questions on Right Triangles, Collinear Tests, Shapes & Computational Logic",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 4 • Advanced Geometric Reasoning",
        "questions": [
            {
                "id": 31,
                "q": "Check whether points A(3, 1), B(6, 4), and C(9, 7) are collinear.",
                "options": [
                    "Yes, slope(AB) = slope(BC) = 1",
                    "No, they form a right triangle",
                    "No, because coordinates are positive",
                    "Cannot be determined without a graph"
                ],
                "ans": 0,
                "solution": "Slope of $AB = \\frac{4 - 1}{6 - 3} = \\frac{3}{3} = 1$. Slope of $BC = \\frac{7 - 4}{9 - 6} = \\frac{3}{3} = 1$. Since both segments share point $B$ and have identical slopes of 1, the three points are strictly collinear."
            },
            {
                "id": 32,
                "q": "The points A(1, 7), B(4, 2), C(-1, -1), and D(-4, 4) form the vertices of which quadrilateral?",
                "options": ["A Square", "A Rectangle but not square", "A Rhombus but not square", "A Trapezium"],
                "ans": 0,
                "solution": "Side lengths: $AB^2 = 3^2 + (-5)^2 = 34$; $BC^2 = (-5)^2 + (-3)^2 = 34$; $CD^2 = (-3)^2 + 5^2 = 34$; $DA^2 = 5^2 + 3^2 = 34$. All 4 sides equal $\\sqrt{34}$. Diagonals: $AC^2 = (-2)^2 + (-8)^2 = 68$; $BD^2 = (-8)^2 + 2^2 = 68$. Equal diagonals ($AC = BD = \\sqrt{68}$). Four equal sides and equal diagonals proves $ABCD$ is a Square."
            },
            {
                "id": 33,
                "q": "In triangle ABC with vertices A(5, -2), B(6, 4), and C(7, -2), what type of triangle is it?",
                "options": ["Isosceles", "Equilateral", "Scalene", "Right-angled"],
                "ans": 0,
                "solution": "$AB^2 = (6-5)^2 + (4 - (-2))^2 = 1 + 36 = 37 \\implies AB = \\sqrt{37}$. $BC^2 = (7-6)^2 + (-2 - 4)^2 = 1 + 36 = 37 \\implies BC = \\sqrt{37}$. $AC = |7 - 5| = 2$. Since $AB = BC = \\sqrt{37} \\ne 2$, it is an Isosceles triangle."
            },
            {
                "id": 34,
                "q": "The points A(0, 0), B(3, 0), and C(0, 4) form a right triangle. What is the length of its hypotenuse?",
                "options": ["5 units", "7 units", "25 units", "4 units"],
                "ans": 0,
                "solution": "Hypotenuse $BC = \\sqrt{(0 - 3)^2 + (4 - 0)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$ units."
            },
            {
                "id": 35,
                "q": "Find the value of p for which the points (-5, 1), (1, p), and (4, -2) are collinear.",
                "options": ["p = -1", "p = 0", "p = 1", "p = -2"],
                "ans": 0,
                "solution": "Slope of $AB = \\text{Slope of } BC \\implies \\frac{p - 1}{1 - (-5)} = \\frac{-2 - p}{4 - 1} \\implies \\frac{p - 1}{6} = \\frac{-2 - p}{3} \\implies p - 1 = 2(-2 - p) = -4 - 2p \\implies 3p = -3 \\implies p = -1$."
            },
            {
                "id": 36,
                "q": "Which of the following conditions proves that a parallelogram is a rectangle?",
                "options": [
                    "Its diagonals are equal in length",
                    "Its diagonals are perpendicular",
                    "All four sides are equal",
                    "Its perimeter is greater than 20"
                ],
                "ans": 0,
                "solution": "A parallelogram is a rectangle if and only if its diagonals are equal in length ($AC = BD$)."
            },
            {
                "id": 37,
                "q": "The points A(3, 0), B(4, 5), C(-1, 4), and D(-2, -1) form a rhombus. What is its area if diagonal lengths are d₁ = 2√26 and d₂ = 2√6? (Formula: Area = ½ d₁ d₂)",
                "options": ["4√39 ≈ 24.98", "2√39", "12", "48"],
                "ans": 0,
                "solution": "Area of a rhombus $= \\frac{1}{2} \\times d_1 \\times d_2 = \\frac{1}{2} \\times 2\\sqrt{26} \\times 2\\sqrt{6} = 2\\sqrt{156} = 2 \\times 2\\sqrt{39} = 4\\sqrt{39}$ square units."
            },
            {
                "id": 38,
                "q": "If in triangle PQR, PQ² + QR² = PR², which vertex contains the right angle?",
                "options": ["Vertex Q", "Vertex P", "Vertex R", "None"],
                "ans": 0,
                "solution": "The side opposite vertex $Q$ is the hypotenuse $PR$. Therefore, the $90^\\circ$ right angle is located at vertex $Q$."
            },
            {
                "id": 39,
                "q": "In computational geometry, testing whether three points are collinear using the cross-product avoids which critical programming error?",
                "options": [
                    "Division by zero (undefined slope on vertical lines)",
                    "Memory overflow",
                    "Infinite loops",
                    "Syntax errors"
                ],
                "ans": 0,
                "solution": "Calculating slope $\\frac{\\Delta y}{\\Delta x}$ crashes with division by zero when $\\Delta x = 0$ (vertical lines). The cross-product formulation $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) = 0$ completely avoids division."
            },
            {
                "id": 40,
                "q": "Three points A, B, and C have distances AB = 4, BC = 6, and AC = 10. What can be concluded about points A, B, and C?",
                "options": [
                    "They are collinear with B between A and C",
                    "They form an acute triangle",
                    "They form an obtuse triangle",
                    "They form a right triangle"
                ],
                "ans": 0,
                "solution": "Since $AB + BC = 4 + 6 = 10 = AC$, the triangle inequality collapses into equality, proving that points $A, B$, and $C$ are collinear with $B$ situated between $A$ and $C$."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Total Content Slides: {len(SLIDES)}")
    total_checkpoints = sum(len(s["checkpoints"]) for s in SLIDES)
    print(f"Total Checkpoints: {total_checkpoints}")
    print(f"Total Quiz Slides: {len(QUIZZES)}")
    total_quiz_q = sum(len(q["questions"]) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_quiz_q}")
    assert len(SLIDES) == 16, "Must have exactly 16 content slides"
    assert total_checkpoints == 32, "Must have exactly 32 checkpoints (2 per slide)"
    assert len(QUIZZES) == 4, "Must have exactly 4 quiz slides"
    assert total_quiz_q == 40, "Must have exactly 40 quiz questions"

    for i, s in enumerate(SLIDES):
        assert len(s["checkpoints"]) == 2, f"Slide {i+1} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert "q" in cp and "options" in cp and "ans" in cp and "exp" in cp
            assert 0 <= cp["ans"] < len(cp["options"])

    for q_slide in QUIZZES:
        assert len(q_slide["questions"]) == 10, f"Quiz slide {q_slide['id']} must have 10 questions"
        for q in q_slide["questions"]:
            assert "q" in q and "options" in q and "ans" in q and "solution" in q
            assert 0 <= q["ans"] < len(q["options"])

    print("All validations PASSED!")


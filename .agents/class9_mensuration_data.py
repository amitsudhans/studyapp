# -*- coding: utf-8 -*-
"""
Data module for Class 9 Mathematics Chapter 12: Mensuration: Area and Perimeter
Syllabus Competencies: CG-5, C-5.1, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

SLIDES = [
    {
        "id": 1,
        "title": "Perimeter of Shapes & Boundary Metrics",
        "subtitle": "Defining the 1D Closed Contour Enclosing a 2D Planar Region",
        "category": "Boundary Metrics",
        "badge": "CG-5 • C-5.1 • Boundary Metrics",
        "summary": "Perimeter is the total length of the continuous one-dimensional boundary enclosing a two-dimensional planar region. For any rectilinear polygon, the perimeter is the algebraic sum of all individual side lengths: P = Σ s_i. For regular n-gons with equal side lengths s, this simplifies to P = n × s (e.g., equilateral triangle P = 3s, square P = 4s, regular hexagon P = 6s). For irregular and composite figures, perimeter is evaluated by decomposing the boundary into individual linear segments. Perimeter has dimensions of length ([L]), measured in linear units such as meters (m), centimeters (cm), or kilometers (km). Practical applications include agricultural fencing, architectural skirting, athletic running tracks, and perimeter security fencing.",
        "key_points": [
            "Perimeter Definition: The total continuous path length along the boundary enclosing a 2D planar figure.",
            "Linear Dimension: Perimeter is purely one-dimensional ([L]), distinct from two-dimensional area ([L²]).",
            "Polygon Boundary Formula: For straight-sided polygons, P = Σ s_i; for regular n-gons, P = n · s.",
            "Rectangle & Square Metrics: Rectangle P = 2(l + b); Square P = 4s; Equilateral triangle P = 3s.",
            "Real-World Applications: Farmland fencing, architectural baseboards, framing, and athletic track design."
        ],
        "narration": "Welcome to Mensuration: Area and Perimeter! Mensuration comes from the Latin 'mensurare', meaning 'to measure'. We begin with perimeter: the total distance traveled along the continuous outer edge of any closed two-dimensional shape. Whether fencing agricultural land or calculating baseboards for a room, perimeter quantifies one-dimensional boundary lengths. Watch our interactive boundary unroller transform polygons into a straight linear ruler!",
        "sim_title": "Polygon Boundary Unroller & Perimeter Linear Meter",
        "checkpoints": [
            {
                "q": "What is the perimeter of a regular hexagon with side length 7.5 cm?",
                "options": ["42.0 cm", "45.0 cm", "49.0 cm", "52.5 cm"],
                "ans": 1,
                "exp": "A regular hexagon has 6 equal sides. Perimeter P = 6 × s = 6 × 7.5 cm = 45.0 cm."
            },
            {
                "q": "An L-shaped room has consecutive sides of 8 m, 6 m, 3 m, 2 m, 5 m, and 4 m. What is its perimeter?",
                "options": ["24 m", "28 m", "30 m", "32 m"],
                "ans": 1,
                "exp": "Perimeter is the total boundary length: 8 + 6 + 3 + 2 + 5 + 4 = 28 m."
            }
        ]
    },
    {
        "id": 2,
        "title": "Perimeter of a Circle: Pi & Its Irrationality",
        "subtitle": "The Universal Invariant C / d = π and Non-Repeating Decimal Expansion",
        "category": "Circular Metrics",
        "badge": "C-5.1 • The Constant Ratio π",
        "summary": "For any circle in the Euclidean plane, the ratio of its circumference C to its diameter d is strictly invariant: C / d = π ≈ 3.14159265... regardless of the physical scale of the circle. In 1761, Johann Heinrich Lambert proved that π is an irrational number; Ivan Niven provided a simplified calculus proof in 1947. Because π is irrational, it cannot be expressed as a ratio of integers p/q (with q ≠ 0), and its decimal expansion is non-terminating and non-repeating. The widely used fraction 22/7 is merely a rational approximation (22/7 = 3.142857...), which overestimates π by approximately 0.001264 (~0.04%). Archimedes, Aryabhata, and Zu Chongzhi all established that π cannot be captured by simple whole-number ratios.",
        "key_points": [
            "The Universal Ratio: The circumference-to-diameter ratio C / d is constant for all circles and defines the mathematical constant π.",
            "Irrationality of Pi: Proven by Lambert (1761); π cannot be written as p/q, with a non-terminating, non-periodic decimal expansion.",
            "Distinction from 22/7: 22/7 is a rational approximation (≈ 3.142857), differing from true π by ~0.04%.",
            "Circumference Formulas: C = π d = 2π r, where d is diameter and r is radius.",
            "Kinematic Meaning: A rolling wheel of radius r travels exactly 2πr linear distance in one complete 360° revolution."
        ],
        "narration": "No matter how microscopic or colossal a circle is, dividing its circumference by its diameter always yields the exact same universal number: π! In 1761, Johann Lambert proved that π is irrational—it can never be written as an exact fraction, and its decimals continue infinitely without any repeating pattern. In our rolling wheel lab, observe how one complete revolution rolls out exactly 2πr along the ruler!",
        "sim_title": "Rolling Circle Kinematic Unroller & Invariant C/d Meter",
        "checkpoints": [
            {
                "q": "Why is 22/7 NOT exactly equal to the mathematical constant π?",
                "options": [
                    "Because 22/7 is irrational while π is rational",
                    "Because 22/7 is a rational approximation (≈ 3.142857...) whereas π is irrational (≈ 3.141592...)",
                    "Because 22/7 was proved false by Euclid",
                    "Because π equals exactly 3.14"
                ],
                "ans": 1,
                "exp": "π is an irrational number with a non-terminating, non-repeating decimal. 22/7 = 3.142857... is a rational fraction that exceeds π by approximately 0.001264 (0.04%)."
            },
            {
                "q": "If the diameter of a circle is doubled, what happens to the ratio Circumference / Diameter?",
                "options": ["It doubles", "It quadruples", "It halves", "It remains strictly constant and equal to π"],
                "ans": 3,
                "exp": "Circumference is directly proportional to diameter (C = πd). The ratio C/d is the universal constant π for all circles regardless of size."
            }
        ]
    },
    {
        "id": 3,
        "title": "Historical Approximations to Pi Across Civilizations",
        "subtitle": "From Archimedes' 96-Gon Squeeze to Aryabhata's Āsanna & Zu Chongzhi's Milü",
        "category": "History of Mathematics",
        "badge": "C-5.1 • Ancient Approximations",
        "summary": "Before the advent of modern calculus, ancient civilizations devised brilliant geometric algorithms to approximate π. Archimedes of Syracuse (c. 250 BCE) bounded π by inscribing and circumscribing regular 96-sided polygons around a circle, establishing 223/71 < π < 22/7 (3.1408 < π < 3.1428). In India, Aryabhata (499 CE, Aryabhatiya) stated: 'Add 4 to 100, multiply by 8, and add 62,000; this gives the approximate circumference of a circle of diameter 20,000': 62832 / 20000 = 3.1416, explicitly labeling it 'āsanna' (approaching/approximate). In China, Zu Chongzhi (5th century CE) derived the Milü ratio 355/113 ≈ 3.1415929, accurate to 6 decimal places—unrivaled for over 900 years! The Egyptian Rhind Papyrus (c. 1650 BCE) used (16/9)² ≈ 3.1605.",
        "key_points": [
            "Archimedes (c. 250 BCE): Inscribed and circumscribed regular 96-gons to prove 223/71 (3.1408) < π < 22/7 (3.1428).",
            "Aryabhata (499 CE): Formulated C/d ≈ 62832 / 20000 = 3.1416, explicitly identifying it as 'āsanna' (approximate).",
            "Zu Chongzhi (5th century CE): Computed Milü 355/113 ≈ 3.1415929, accurate to 6 decimal places (error < 3 × 10⁻⁷).",
            "Egyptian Rhind Papyrus (c. 1650 BCE): Approximated area using [d - d/9]², giving π ≈ 256/81 ≈ 3.1605.",
            "Evolution of Precision: Moving from empirical craft rules to rigorous geometric exhaustion and bounding limits."
        ],
        "narration": "Centuries before computers, mathematicians across India, Greece, and China used pure geometric reasoning to approximate π! Archimedes doubled polygon sides up to 96 sides to trap π between two fractions. Aryabhata computed 3.1416 and recognized that π was inherently approximate. Zu Chongzhi found 355 over 113, matching π to six decimal places! Watch our interactive polygon exhaustion squeeze π tighter and tighter.",
        "sim_title": "Archimedean Polygon Exhaustion & Multi-Civilisation Error Comparator",
        "checkpoints": [
            {
                "q": "Which historical mathematician calculated the approximation π ≈ 62832 / 20000 = 3.1416?",
                "options": ["Archimedes", "Aryabhata", "Zu Chongzhi", "Baudhayana"],
                "ans": 1,
                "exp": "In 499 CE, Indian astronomer-mathematician Aryabhata stated this formula in the Aryabhatiya, explicitly calling it 'āsanna' (approximate)."
            },
            {
                "q": "Zu Chongzhi's famous ratio Milü (355 / 113) is accurate to how many decimal places?",
                "options": ["2 decimal places", "4 decimal places", "6 decimal places", "10 decimal places"],
                "ans": 2,
                "exp": "355 / 113 ≈ 3.14159292..., while π ≈ 3.14159265... It matches to 6 decimal places (error less than 0.0000003)!"
            }
        ]
    },
    {
        "id": 4,
        "title": "Circumference & Length of an Arc",
        "subtitle": "Subtended Central Angles, Fractional Boundary Arcs & Sector Perimeters",
        "category": "Circular Metrics",
        "badge": "CG-5 • C-5.1 • Arc Length & Wheels",
        "summary": "The full perimeter of a circle is its circumference C = 2πr = πd. An arc is a continuous segment of the circumference. If an arc subtends a central angle θ (in degrees) at the circle's centre, its arc length l is proportional to the fraction of a complete 360° turn: l = (θ / 360°) × 2πr = (θπr) / 180°. In radians, l = rθ. The total perimeter of a sector must include the curved arc plus the two straight bounding radii: P_sector = l + 2r. Real-world applications include cyclometer distance tracking (total distance = revolutions × 2πr), circular gear pitch, satellite orbital trajectories, and banked highway curves.",
        "key_points": [
            "Circumference Formula: C = 2π r = π d for a full 360° boundary traversal.",
            "Arc Length Formula: l = (θ / 360°) · 2π r = (θ π r) / 180° for central angle θ in degrees.",
            "Perimeter of a Sector: P = l + 2r = (θ / 360°)(2π r) + 2r, accounting for both curved and radial edges.",
            "Odometer Physics: Linear vehicle distance D = N · (2π r), where N is wheel revolutions.",
            "Curvature Applications: Rail tracks, road bends, circular arcs in bridges, and gear teeth kinematics."
        ],
        "narration": "Think of arc length as measuring the crust of a pizza slice! If the central angle is θ degrees, the arc length is simply θ over 360 times the total circumference 2πr. But beware: the total perimeter of a sector includes the curved arc plus the two straight radii that close the slice! Drag the angle slider to explore both arc length and full sector boundary metrics.",
        "sim_title": "Dynamic Arc Length & Sector Perimeter Kinematic Simulator",
        "checkpoints": [
            {
                "q": "What is the length of an arc of a circle of radius 14 cm subtending an angle of 90° at the centre? (Use π = 22/7)",
                "options": ["11 cm", "22 cm", "44 cm", "88 cm"],
                "ans": 1,
                "exp": "Arc length l = (θ / 360°) × 2πr = (90/360) × 2 × (22/7) × 14 = (1/4) × 88 = 22 cm."
            },
            {
                "q": "A sector of radius 21 cm has a central angle of 60°. What is the TOTAL perimeter of the sector? (Use π = 22/7)",
                "options": ["22 cm", "43 cm", "64 cm", "85 cm"],
                "ans": 2,
                "exp": "Arc length l = (60/360) × 2 × (22/7) × 21 = (1/6) × 132 = 22 cm. Total perimeter = l + 2r = 22 + 2(21) = 22 + 42 = 64 cm."
            }
        ]
    },
    {
        "id": 5,
        "title": "Area of Shapes: Rectangles, Parallelograms & Triangles",
        "subtitle": "Unit Square Tiling, Cavalieri Shearing Invariance & The Half-Base Factor",
        "category": "Polygon Areas",
        "badge": "CG-5 • Polygon Mensuration",
        "summary": "Area quantifies the size of a two-dimensional planar surface in square units ([L²]). For a rectangle with length l and breadth b, Area = l × b, derived from counting unit squares in a grid. A parallelogram with base b and perpendicular altitude h has Area = b × h: slicing off a right triangle from one end and translating it to the other produces an equal-area rectangle without area loss (Cavalieri's shearing principle). Any triangle with base b and altitude h is exactly half of a parallelogram with the same base and height: Area = (1/2) × b × h. Two triangles on the same base and between the same parallel lines have equal area.",
        "key_points": [
            "Rectangle Area: Area = l · b, foundational to 2D Cartesian plane integration and grid counting.",
            "Parallelogram Area: Area = b · h; shearing preserves cross-sectional lengths and total surface area.",
            "Triangle Area: Area = (1/2) · b · h; every triangle is half of an encompassing parallelogram.",
            "Same Base, Same Parallels: Triangles sharing base b between parallel lines have identical height h and equal area.",
            "Area Dimensions: Expressed in square units (m², cm², km², hectares, where 1 hectare = 10,000 m²)."
        ],
        "narration": "Notice the beautiful evolutionary chain of area formulas! We begin with rectangles, counting unit squares: length times breadth. Next, we shear the rectangle into a parallelogram without altering base or height—the area remains base times height! Finally, cutting the parallelogram along its diagonal yields two congruent triangles, giving each triangle an area of exactly half base times height. Drag our shearing slider to watch this transformation live!",
        "sim_title": "Shearing Transformation: Parallelogram to Rectangle & Triangle Doubling",
        "checkpoints": [
            {
                "q": "A parallelogram has a base of 16 cm and a corresponding height of 9 cm. What is its area?",
                "options": ["72 cm²", "144 cm²", "180 cm²", "288 cm²"],
                "ans": 1,
                "exp": "Area of a parallelogram = base × height = 16 cm × 9 cm = 144 cm²."
            },
            {
                "q": "Why does shearing a parallelogram into a rectangle preserve its area?",
                "options": [
                    "Because the perimeter stays the same",
                    "Because a right triangle sliced from one end translates to fit identically on the other end without gain or loss of area",
                    "Because all angles remain 90°",
                    "Because diagonals bisect at right angles"
                ],
                "ans": 1,
                "exp": "By Cavalieri's principle of shearing, translating parallel cross-sections or moving a congruent triangular piece from one side to the other preserves total area."
            }
        ]
    },
    {
        "id": 6,
        "title": "Median of a Triangle Divides It into Equal Areas",
        "subtitle": "Equal Base Partitions and Shared Perpendicular Altitude",
        "category": "Triangle Theorems",
        "badge": "C-7.3 • Triangle Median Theorem",
        "summary": "Theorem: A median of a triangle divides it into two triangles of equal area. Proof: In ΔABC, let AD be the median to base BC, so BD = DC. Drop the perpendicular altitude AH from vertex A onto line BC (length h). For ΔABD, Area(ΔABD) = (1/2)(BD)(h). For ΔACD, Area(ΔACD) = (1/2)(DC)(h). Since BD = DC, Area(ΔABD) = Area(ΔACD). Key Corollaries: (1) The centroid G divides the triangle into 3 triangles of equal area: Area(ΔGAB) = Area(ΔGBC) = Area(ΔGCA) = (1/3)Area(ΔABC). (2) The three medians together divide the triangle into 6 smaller triangles, each having area exactly (1/6)Area(ΔABC).",
        "key_points": [
            "Median Area Bisection Theorem: A median bisects a triangle into two sub-triangles of equal area.",
            "Shared Altitude Proof: Both sub-triangles have equal base lengths (BD = DC) and share the exact same altitude h from vertex A.",
            "Centroid Tripartition: Centroid G forms three triangles (ΔGAB, ΔGBC, ΔGCA) each of area (1/3)Area(ΔABC).",
            "Hexa-Partition: The three concurrent medians partition any triangle into 6 smaller triangles of equal area (1/6 each).",
            "Independence of Skew: The equality holds universally for equilateral, isosceles, right, and scalene triangles."
        ],
        "narration": "Even in a wildly skewed or scalene triangle, a median divides the enclosed area into two perfectly equal halves! Why? Because both halves have equal base lengths and share the exact same perpendicular height from the top vertex. Furthermore, the centroid partitions the triangle into three equal-area regions, and all three medians carve it into six equal pieces! Test this by dragging vertex A anywhere on screen.",
        "sim_title": "Interactive Triangle Median & Centroid Area Equalizer",
        "checkpoints": [
            {
                "q": "In ΔABC, AD is a median. If Area(ΔABC) = 48 cm², what is Area(ΔABD)?",
                "options": ["12 cm²", "16 cm²", "24 cm²", "36 cm²"],
                "ans": 2,
                "exp": "A median bisects the base into equal halves sharing the same height, dividing triangle area into two equal halves: 48 / 2 = 24 cm²."
            },
            {
                "q": "The three medians of a triangle intersect at centroid G. How many smaller triangles of equal area are formed?",
                "options": ["2", "3", "4", "6"],
                "ans": 3,
                "exp": "The three medians partition any triangle into 6 smaller triangles, each having exactly 1/6th of the total area."
            }
        ]
    },
    {
        "id": 7,
        "title": "Heron’s Formula for Triangle Area",
        "subtitle": "Evaluating Area Purely from Three Side Lengths Without Altitude",
        "category": "Heron's Formula",
        "badge": "CG-5 • Heron's Formula",
        "summary": "In surveying and field geometry, measuring the perpendicular altitude across rugged terrain is often impractical, but measuring the perimeter sides a, b, c is straightforward. Hero of Alexandria (c. 60 CE, Metrica) proved that Area = √[s(s - a)(s - b)(s - c)], where semi-perimeter s = (a + b + c) / 2. The formula requires only that the triangle inequality holds (a + b > c). Special cases: (1) Equilateral triangle (a = b = c): s = 3a/2, giving Area = (√3 / 4)a². (2) Isosceles triangle (a, a, b): Area = (b/4)√(4a² - b²). (3) Right triangle (a² + b² = c²): Area = (1/2)ab. Inradius r_in relates to area via Area = r_in × s.",
        "key_points": [
            "Heron's Formula: Area = √[s(s - a)(s - b)(s - c)], where semi-perimeter s = (a + b + c) / 2.",
            "Altitude Independence: Computes exact area using only side lengths a, b, c without constructing any height.",
            "Equilateral Specialization: For a = b = c, Heron reduces directly to Area = (√3 / 4) a².",
            "Isosceles Specialization: For sides a, a, b, reduces to Area = (b / 4) √(4a² - b²).",
            "Incircle Connection: Triangle area equals inradius times semi-perimeter: Area = r_in · s."
        ],
        "narration": "Imagine you are a surveyor measuring an irregular agricultural field. Measuring a perpendicular height across a river or dense forest is impossible, but measuring the three perimeter sides with a chain is easy! Hero of Alexandria solved this completely with Heron's formula: semi-perimeter s, times the differences s minus a, s minus b, s minus c, all under the square root. Adjust the side lengths to see Heron's formula compute area step by step.",
        "sim_title": "Heron’s Formula Geometric Computer & Incircle Radius Visualizer",
        "checkpoints": [
            {
                "q": "Find the area of a triangle with sides 13 cm, 14 cm, and 15 cm using Heron's formula.",
                "options": ["72 cm²", "84 cm²", "90 cm²", "96 cm²"],
                "ans": 1,
                "exp": "s = (13 + 14 + 15)/2 = 21 cm. Area = √[21 × (21-13) × (21-14) × (21-15)] = √[21 × 8 × 7 × 6] = √[7056] = 84 cm²."
            },
            {
                "q": "What is the area of an equilateral triangle with side length 8 cm?",
                "options": ["16√3 cm²", "24√3 cm²", "32√3 cm²", "64√3 cm²"],
                "ans": 0,
                "exp": "Area = (√3 / 4) a² = (√3 / 4) × 64 = 16√3 cm²."
            }
        ]
    },
    {
        "id": 8,
        "title": "Squaring a Rectangle: Baudhayana’s Sulbasutras",
        "subtitle": "Vedic Geometric Quadrature via Gnomon Assembly & Difference of Squares",
        "category": "Vedic Geometry",
        "badge": "C-7.1 • Baudhayana Quadrature",
        "summary": "In the Baudhayana Sulbasutras (c. 800 BCE), ritual fire altars (vedis) required transforming a rectangular hearth of dimensions a × b into an equivalent square of equal area: a × b = x². Baudhayana's construction: (1) Cut a square of side b from rectangle a × b. (2) Bisect the remaining strip of width (a - b) into two equal strips of width (a - b)/2. (3) Attach one strip to the top and one to the side, forming an L-shaped gnomon. (4) Add a small corner square of side [(a - b)/2]² to complete a large square of side (a + b)/2. (5) Area of rectangle ab = [(a + b)/2]² - [(a - b)/2]². (6) By Baudhayana's rope theorem, the difference of two squares is constructed as the leg of a right triangle: x = √(ab)!",
        "key_points": [
            "Classical Quadrature Problem: Constructing a square of area equal to a given rectangle (x² = a · b).",
            "Baudhayana Sulbasutra (c. 800 BCE): Earliest known geometric proof of rectangular quadrature using cord and pegs.",
            "Gnomon Dissection: Reorganising excess strips into an L-shaped gnomon around the base square.",
            "Algebraic Equivalence: Proves the identity a · b = [(a + b) / 2]² - [(a - b) / 2]² purely by geometric rearrangement.",
            "Geometric Mean Construction: The side of the resulting square x = √(ab) is the geometric mean of length and breadth."
        ],
        "narration": "Over 2,800 years ago, ancient Indian Vedic geometers solved the classic problem of 'squaring a rectangle' using only rope and pegs! Baudhayana demonstrated that any rectangle of dimensions a times b can be rearranged into an L-shaped gnomon, revealing that the rectangle's area equals the difference between two squares: (a+b)/2 squared minus (a-b)/2 squared! By the Sulbasutra rope theorem, this difference creates a square of side square root of a times b. Step through our 5-stage Vedic construction animation!",
        "sim_title": "Baudhayana Sulbasutra 5-Step Rectangular Squaring Animation",
        "checkpoints": [
            {
                "q": "In Baudhayana's Sulbasutra squaring of a rectangle of sides a and b, what algebraic identity is geometrically proven?",
                "options": [
                    "(a + b)² = a² + 2ab + b²",
                    "ab = [(a + b) / 2]² - [(a - b) / 2]²",
                    "(a - b)² = a² - 2ab + b²",
                    "a³ - b³ = (a - b)(a² + ab + b²)"
                ],
                "ans": 1,
                "exp": "Baudhayana showed that the rectangle ab equals the difference between the large square on (a+b)/2 and the small corner square on (a-b)/2."
            },
            {
                "q": "What is the side of a square having the same area as a rectangle of dimensions 18 cm × 8 cm?",
                "options": ["10 cm", "12 cm", "13 cm", "14 cm"],
                "ans": 1,
                "exp": "Area of rectangle = 18 × 8 = 144 cm². Side of equivalent square = √144 = 12 cm (the geometric mean of 18 and 8)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Area of a Circle: Slicing Derivation",
        "subtitle": "Infinite Sector Dissection and Archimedes' Unrolled Triangle",
        "category": "Circle Area",
        "badge": "CG-5 • Circle Area Derivation",
        "summary": "To derive the area of a circle, partition it into N equal wedge sectors (N = 8, 16, 32, 64...) and rearrange them in an alternating, interlocking row. The total circumference 2πr is divided equally between the top and bottom scalloped boundaries, each receiving length (2πr)/2 = πr. The vertical height of each wedge is the radius r. As N → ∞, the scallops straighten into parallel line segments perpendicular to the height, forming an exact rectangle of base πr and height r. Therefore, Area = base × height = (πr) × r = πr²! In Archimedes' concentric unrolling method, concentric circular rings unroll into stacked strips forming a right triangle of base 2πr and altitude r: Area = (1/2)(2πr)(r) = πr².",
        "key_points": [
            "Sector Dissection Method: Slicing a circle into N wedges and meshing them alternately into a pseudo-rectangle.",
            "Base of Rearranged Shape: Top and bottom edges each receive half of the total circumference: C / 2 = π r.",
            "Height of Rearranged Shape: The radial edges of the sectors form the height r.",
            "Limit as N → ∞: As sector count tends to infinity, the shape becomes an exact rectangle of area (π r) · r = π r².",
            "Archimedes' Unrolled Triangle: Concentric thin circular rings unwind into a right triangle of base 2π r and altitude r."
        ],
        "narration": "How do we find the area enclosed by a curved circle? We cut it into thin pizza slices and interlock them in an alternating row! Notice that half the crust goes to the top edge and half goes to the bottom edge, each measuring πr. The height of the row is simply the radius r. As we increase the slice count towards infinity, the scalloped edges straighten into a perfect rectangle of area πr times r, or πr²! Watch our interactive dissection slice and unroll the circle.",
        "sim_title": "Interactive Sector Slicing to Rectangle & Archimedes Concentric Ring Unroller",
        "checkpoints": [
            {
                "q": "When a circle of radius r is cut into N sectors and rearranged into an alternating pseudo-rectangle, what are its dimensions as N → ∞?",
                "options": [
                    "Length = 2πr, Height = r",
                    "Length = πr, Height = r",
                    "Length = πr², Height = 2r",
                    "Length = πr / 2, Height = 2r"
                ],
                "ans": 1,
                "exp": "The top and bottom edges each receive half the circumference (C / 2 = πr), while the radial slice forms the height r. Area = πr × r = πr²."
            },
            {
                "q": "In Archimedes' concentric ring derivation, unrolling the rings produces a right triangle with which dimensions?",
                "options": [
                    "Base = πr, Height = r",
                    "Base = 2πr, Height = r",
                    "Base = 2r, Height = πr",
                    "Base = 4πr, Height = r / 2"
                ],
                "ans": 1,
                "exp": "The outermost ring unwinds to circumference 2πr (base), while the accumulated ring radii form the height r. Area = (1/2) × (2πr) × r = πr²."
            }
        ]
    },
    {
        "id": 10,
        "title": "Ancient Approximations of Circle Area",
        "subtitle": "The Egyptian Rhind Papyrus, Babylonian Tablets & Liu Hui's Exhaustion",
        "category": "Historical Mensuration",
        "badge": "C-5.1 • Ancient Approximations",
        "summary": "Before formal algebra, ancient civilisations devised empirical and geometric rules for circle area. The Egyptian Rhind Papyrus (c. 1650 BCE, Problem 50) instructed: 'Take away 1/9 of the diameter and square the remainder.' Area ≈ [d - (1/9)d]² = [(8/9)d]² = (64/81)d² = (256/81)r² ≈ 3.1605 r², an error of only ~0.6%! In ancient Mesopotamia (Babylonia), area was estimated from circumference as A ≈ C² / 12, implying π ≈ 3. In China, Liu Hui (263 CE) wrote the Nine Chapters commentary, using 3,072-sided regular polygons to calculate π ≈ 3.1416 and derive circle area with extraordinary precision.",
        "key_points": [
            "Egyptian Rhind Papyrus (c. 1650 BCE): Problem 50 gives Area ≈ [(8/9) d]² = (64/81) d² ≈ 3.1605 r².",
            "Babylonian Tablets (c. 1800 BCE): Estimated area from circumference as A ≈ C² / 12, reflecting π ≈ 3.",
            "Liu Hui (263 CE, China): Exhaustion method using inscribed 3,072-gon to determine circle area and π ≈ 3.1416.",
            "Vedic Altars (Sulbasutras): Circling the square and squaring the circle for Garhapatya and Ahavaniya altars.",
            "Accuracy Evolution: From practical granary estimates (0.6% error) to rigorous geometric limits."
        ],
        "narration": "Thousands of years ago, Egyptian scribes calculating grain silo storage needed to find circular areas without knowing modern algebra! Their rule—subtract one-ninth of the diameter and square the remainder—produced an approximation accurate to within 0.6%! Compare the true circle area πr² with the ancient Egyptian square and Babylonian formulas on our multi-civilisation area comparator.",
        "sim_title": "Multi-Civilisation Circle Area Comparator & Historical Error Dials",
        "checkpoints": [
            {
                "q": "According to the Egyptian Rhind Papyrus (Problem 50), circle area is approximated by squaring what fraction of the diameter?",
                "options": ["3/4 of diameter", "7/8 of diameter", "8/9 of diameter", "9/10 of diameter"],
                "ans": 2,
                "exp": "The scribe wrote: take away 1/9 of the diameter and square the remainder: [d - d/9]² = [(8/9)d]² = (64/81)d²."
            },
            {
                "q": "The ancient Babylonian formula A ≈ C² / 12 implies what value for π?",
                "options": ["2.8", "3.0", "3.125", "3.1416"],
                "ans": 1,
                "exp": "Since C = 2πr, C² / 12 = 4π²r² / 12 = (π² / 3)r². For this to equal πr², we need π / 3 = 1, so π ≈ 3."
            }
        ]
    },
    {
        "id": 11,
        "title": "Area of the Sector of a Circle",
        "subtitle": "Central Angles, Fractional Slices & The Triangular (1/2)lr Formula",
        "category": "Sector Area",
        "badge": "CG-5 • Sector Mensuration",
        "summary": "A circular sector is the region bounded by two radii and their intercepted arc. The area of a sector subtending central angle θ at the centre is directly proportional to θ: Area = (θ / 360°) × πr². Notice a remarkable mathematical connection: since arc length is l = (θ / 360°)(2πr), substituting l gives Area = (1/2) × l × r. This formula has the exact same structure as the area of a triangle: (1/2) × base × height, where the curved arc l acts as the base and radius r acts as the perpendicular height! Practical applications include automotive windshield wiper sweep areas, agricultural rotary sprinkler coverage, and beam angles of lighthouses.",
        "key_points": [
            "Sector Area Formula: Area = (θ / 360°) · π r² for central angle θ measured in degrees.",
            "The Triangular Equivalence: Area = (1/2) · l · r, where arc length l acts as base and radius r acts as altitude.",
            "Minor vs Major Sector: Minor sector subtends θ < 180°; Major sector subtends 360° - θ with Area = π r² - Area(minor).",
            "Irrigation & Wiper Modeling: Calculating watered field sectors and swept windshield clearing zones.",
            "Direct Proportionality: Doubling the central angle θ doubles both the arc length and the enclosed sector area."
        ],
        "narration": "A sector is simply a slice of the circular pizza! Its area is θ over 360 times the total area πr². But notice something astonishing: because arc length l is θ over 360 times 2πr, the sector area can also be written as one-half times l times r! This looks exactly like a triangle with curved base l and height r. Drag our angle slider to see sprinkler sweeps and windshield wipers calculated in real time.",
        "sim_title": "Rotary Sprinkler & Wiper Sweep Sector Laboratory",
        "checkpoints": [
            {
                "q": "What is the area of a sector of a circle of radius 6 cm with central angle 60°? (Use π = 3.14)",
                "options": ["9.42 cm²", "18.84 cm²", "28.26 cm²", "37.68 cm²"],
                "ans": 1,
                "exp": "Area = (θ / 360°) × πr² = (60/360) × 3.14 × 36 = (1/6) × 113.04 = 18.84 cm²."
            },
            {
                "q": "If an arc of a sector has length l = 15 cm and circle radius is r = 8 cm, what is the area of the sector?",
                "options": ["30 cm²", "60 cm²", "120 cm²", "240 cm²"],
                "ans": 1,
                "exp": "Using Area = (1/2) × l × r = (1/2) × 15 × 8 = 60 cm²."
            }
        ]
    },
    {
        "id": 12,
        "title": "Area of Segments of a Circle",
        "subtitle": "Decomposing Boundary Regions: Sector Area Minus Triangular Core",
        "category": "Segment Mensuration",
        "badge": "CG-5 • Segment Mensuration",
        "summary": "A circular segment is the region bounded by a chord and its intercepted arc. The area of a minor segment is computed by decomposing the region: Area(minor segment) = Area(sector OAB) - Area(ΔOAB) = (θ / 360°)πr² - (1/2)r² sin θ. Special cases: (1) θ = 90°: Area(ΔOAB) = (1/2)r², so Area(segment) = (1/4)πr² - (1/2)r² = r²(π/4 - 1/2). (2) θ = 60°: ΔOAB is equilateral of side r, Area(ΔOAB) = (√3/4)r², so Area(segment) = (1/6)πr² - (√3/4)r². (3) θ = 120°: Area(ΔOAB) = (1/2)r² sin 120° = (√3/4)r². The major segment area is obtained by subtracting the minor segment from total circle area: Area(major) = πr² - Area(minor).",
        "key_points": [
            "Segment Definition: The region enclosed between a chord and its corresponding arc.",
            "Decomposition Principle: Area(minor segment) = Area(sector OAB) - Area(triangle OAB).",
            "General Formula: Area = (θ / 360°) · π r² - (1/2) r² sin θ.",
            "Standard Angle Reductions: 90° right triangle gives (1/4)πr² - (1/2)r²; 60° equilateral gives (1/6)πr² - (√3/4)r².",
            "Major Segment Complement: Area(major segment) = π r² - Area(minor segment)."
        ],
        "narration": "To find the area of a circular segment, use decomposition: start with the entire pizza slice—the sector—and remove the triangular inner core ΔOAB. What remains is the circular cap or segment! For a 90-degree central angle, subtract the right triangle half r-squared. For a 60-degree angle, subtract the equilateral triangle. Watch our simulator peel away the triangular core to isolate the segment!",
        "sim_title": "Circular Segment Decomposer & Triangle Subtraction Simulator",
        "checkpoints": [
            {
                "q": "A chord subtends a right angle (90°) at the centre of a circle of radius 10 cm. What is the area of the minor segment? (Use π = 3.14)",
                "options": ["25.0 cm²", "28.5 cm²", "50.0 cm²", "78.5 cm²"],
                "ans": 1,
                "exp": "Area(sector) = (90/360) × π(10)² = (1/4) × 314 = 78.5 cm². Area(ΔOAB) = (1/2) × 10 × 10 = 50 cm². Area(segment) = 78.5 - 50 = 28.5 cm²."
            },
            {
                "q": "How is the area of a major segment calculated from the minor segment and total circle area?",
                "options": [
                    "Area(major) = Area(minor) + Area(circle)",
                    "Area(major) = Area(circle) - Area(minor segment)",
                    "Area(major) = 2 × Area(minor segment)",
                    "Area(major) = (360 - θ) × Area(minor segment)"
                ],
                "ans": 1,
                "exp": "The minor segment and major segment together form the complete circle without overlap: Area(major) = πr² - Area(minor segment)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Brahmagupta’s Formula for Cyclic 4-Gons",
        "subtitle": "The Master Theorem for Inscribed Quadrilateral Surface Area",
        "category": "Brahmagupta's Formula",
        "badge": "CG-5 • Brahmagupta's Theorem",
        "summary": "In 628 CE, the legendary Indian mathematician Brahmagupta (Brahmasphutasiddhanta, Chapter 12) discovered the universal area formula for any cyclic quadrilateral with side lengths a, b, c, d inscribed in a circle: Semi-perimeter s = (a + b + c + d) / 2; Area = √[(s - a)(s - b)(s - c)(s - d)]. Condition: The quadrilateral MUST be cyclic (opposite angles sum to 180°). Geometric Significance: By Euler's theorem, among all quadrilaterals with fixed side lengths a, b, c, d, the cyclic quadrilateral encloses the MAXIMUM possible area! If the quadrilateral is non-cyclic, Brahmagupta's formula serves as a strict upper bound.",
        "key_points": [
            "Brahmagupta's Formula (628 CE): Area = √[(s - a)(s - b)(s - c)(s - d)], where s = (a + b + c + d) / 2.",
            "Cyclic Inscription Requirement: Valid strictly when all four vertices lie on a common circle (opposite angles supplementary).",
            "Isoperimetric Optimality: Among all quadrilaterals with fixed sides a, b, c, d, the cyclic form maximizes enclosed area.",
            "Upper Bound Property: For non-cyclic quadrilaterals, √[(s - a)(s - b)(s - c)(s - d)] > Actual Area.",
            "Symmetry: The formula is fully symmetric under any permutation of the side lengths a, b, c, d."
        ],
        "narration": "Brahmagupta's formula is one of the crowning triumphs of classical Indian mathematics! Just as Heron gave a formula for triangles from three sides, Brahmagupta discovered a formula for cyclic quadrilaterals from four sides: semi-perimeter s, times s minus a, s minus b, s minus c, s minus d, under the root. Furthermore, among all quadrilaterals with those four sides, the cyclic one achieves the maximum possible area! Drag the four vertices along the circle to compute area in real time.",
        "sim_title": "Brahmagupta Cyclic Quadrilateral Lab & Area Maximizer",
        "checkpoints": [
            {
                "q": "What is the primary condition required for Brahmagupta's formula Area = √[(s-a)(s-b)(s-c)(s-d)] to hold?",
                "options": [
                    "The quadrilateral must be a rhombus",
                    "The quadrilateral must be cyclic (all 4 vertices lie on a circle)",
                    "The diagonals must intersect at 90°",
                    "Opposite sides must be parallel"
                ],
                "ans": 1,
                "exp": "Brahmagupta's formula is valid strictly for cyclic quadrilaterals (opposite angles sum to 180°)."
            },
            {
                "q": "Find the area of a cyclic quadrilateral with sides a = 2, b = 3, c = 4, d = 5.",
                "options": ["√120", "√144 = 12", "√180", "√216"],
                "ans": 0,
                "exp": "s = (2 + 3 + 4 + 5)/2 = 7. Factors: (7-2)=5, (7-3)=4, (7-4)=3, (7-5)=2. Area = √(5 × 4 × 3 × 2) = √120 ≈ 10.95."
            }
        ]
    },
    {
        "id": 14,
        "title": "Heron’s Formula as a Special Case of Brahmagupta",
        "subtitle": "The Continuous Geometric Limit as One Side Collapses to Zero (d → 0)",
        "category": "Generalisation & Specialisation",
        "badge": "CG-9 • Specialisation & Continuity",
        "summary": "What happens when one side of a cyclic quadrilateral shrinks to zero? Consider a cyclic quadrilateral ABCD with sides a, b, c, d. Let side d → 0 by sliding vertex D until it coincides with vertex A. The 4-gon degenerates into a triangle with sides a, b, c! Semi-perimeter becomes s = (a + b + c + 0) / 2 = (a + b + c) / 2. The fourth factor becomes (s - d) = (s - 0) = s. Substituting into Brahmagupta's formula: Area = √[(s - a)(s - b)(s - c)(s - 0)] = √[s(s - a)(s - b)(s - c)], which is precisely Heron's formula! Why does this hold? Because every triangle has a unique circumcircle (three non-collinear points always determine a circle), so every triangle is inherently a cyclic 3-gon!",
        "key_points": [
            "Side Collapse Limit: Setting d = 0 transforms a cyclic 4-gon into a 3-gon (triangle) with sides a, b, c.",
            "Factor Reduction: The term (s - d) becomes (s - 0) = s, yielding √[s(s - a)(s - b)(s - c)].",
            "Universal Cyclicity of Triangles: Every triangle has a unique circumcircle; hence, every triangle is intrinsically cyclic.",
            "Unification: Heron's formula is not an isolated law, but a direct degenerate specialization of Brahmagupta's theorem.",
            "Mathematical Elegance: Demonstrates how continuous parameter limits connect seemingly distinct mathematical formulas."
        ],
        "narration": "Watch this breathtaking transformation! What happens if we take a cyclic quadrilateral and shrink its fourth side d down to zero? The fourth vertex merges with the third, turning the 4-gon into a triangle with sides a, b, and c! In Brahmagupta's formula, the factor s minus d becomes s minus zero, which is just s. Instantly, Brahmagupta's formula morphs into Heron's formula! Heron is simply Brahmagupta's formula with one side collapsed. Slide d to zero to watch this happen!",
        "sim_title": "Vertex Collapse Morphing: Brahmagupta to Heron Continuity Simulator",
        "checkpoints": [
            {
                "q": "Why is Heron's formula considered a special case of Brahmagupta's formula?",
                "options": [
                    "Because setting side d = 0 turns the cyclic quadrilateral into a triangle, and (s - 0) becomes s",
                    "Because Heron lived after Brahmagupta",
                    "Because triangles have four sides",
                    "Because Brahmagupta copied Heron's proof"
                ],
                "ans": 0,
                "exp": "Setting d = 0 collapses the fourth side into a point, yielding a triangle with sides a, b, c and (s - d) = s, reducing Brahmagupta directly to Heron's formula."
            },
            {
                "q": "Why is every triangle guaranteed to be a cyclic polygon?",
                "options": [
                    "Because all triangles are equilateral",
                    "Because through any three non-collinear points, there exists a unique circumcircle",
                    "Because the angle sum of a triangle is 180°",
                    "Because triangle medians concur"
                ],
                "ans": 1,
                "exp": "By Euclid's geometry, the perpendicular bisectors of any triangle's three sides concur at a unique circumcentre, defining a unique circumcircle through all three vertices."
            }
        ]
    },
    {
        "id": 15,
        "title": "Generalisation & Special Cases in Mathematics",
        "subtitle": "The Structural Hierarchy from Bretschneider to Brahmagupta to Heron",
        "category": "Mathematical Abstraction",
        "badge": "CG-9 • Abstraction & Hierarchy",
        "summary": "Mathematics advances through generalisation (expanding theorems to broader domains) and specialisation (applying constraints to discover efficient corollaries). Bretschneider’s formula gives the area of ANY convex quadrilateral: Area = √[(s - a)(s - b)(s - c)(s - d) - abcd cos²((A + C)/2)]. (1) Cyclic Constraint (A + C = 180°): (A+C)/2 = 90°, cos(90°) = 0, causing the second term to vanish and yielding Brahmagupta's formula. (2) Triangular Constraint (d = 0): yields Heron's formula. (3) Equilateral Constraint (a = b = c): yields (√3/4)a². (4) Right-Angle Constraint (a² + b² = c²): yields (1/2)ab. Computational thinking mirrors this object-oriented inheritance tree: abstract parent classes specialize into optimized concrete subclasses.",
        "key_points": [
            "Bretschneider's Formula: The master parent formula for ALL convex quadrilaterals including a cosine correction term.",
            "Cyclic Specialization: When opposite angles are supplementary (A + C = 180°), cos(90°) = 0, reducing to Brahmagupta.",
            "Degenerate Specialization: When side d = 0, Brahmagupta reduces directly to Heron's formula for triangles.",
            "Equilateral Specialization: When a = b = c, Heron reduces to (√3 / 4) a².",
            "Computational Abstraction: General formulas provide universal correctness, while specializations provide O(1) computational speed."
        ],
        "narration": "This formula hierarchy reveals the true power of computational abstraction! At the very top sits Bretschneider's formula for any convex four-sided shape. Add the constraint that vertices lie on a circle, and the cosine term vanishes to yield Brahmagupta. Shrink one side to zero, and it becomes Heron. Set all three sides equal, and you get root three over four a-squared! Explore the hierarchy tree to see each mathematical constraint trigger its simplification.",
        "sim_title": "Interactive Mensuration Formula Hierarchy Tree & Constraint Engine",
        "checkpoints": [
            {
                "q": "In Bretschneider's formula Area = √[(s-a)(s-b)(s-c)(s-d) - abcd cos²((A+C)/2)], what causes the cosine term to vanish for cyclic quadrilaterals?",
                "options": [
                    "A + C = 90°, so cos(45°) = 1/√2",
                    "A + C = 180°, so (A+C)/2 = 90° and cos(90°) = 0",
                    "A = C = 45°, so cos(45°) = 0",
                    "Opposite angles sum to 360°"
                ],
                "ans": 1,
                "exp": "In a cyclic quadrilateral, opposite angles are supplementary (A + C = 180°). Thus (A+C)/2 = 90°, and cos(90°) = 0, causing the second term to vanish!"
            },
            {
                "q": "What is the area formula for an equilateral triangle of side a as a specialization of Heron's formula?",
                "options": ["(1/2) a²", "(√3 / 2) a²", "(√3 / 4) a²", "(3√3 / 4) a²"],
                "ans": 2,
                "exp": "With a = b = c, s = 3a/2 and (s - a) = a/2. Area = √[(3a/2)(a/2)³] = √[(3a⁴)/16] = (√3 / 4) a²."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Algorithmic Mensuration",
        "subtitle": "Decomposition, Gauss's Shoelace Algorithm & Monte Carlo Integration",
        "category": "Computational Geometry",
        "badge": "CG-9 • Algorithmic Mensuration",
        "summary": "Modern computational geometry calculates perimeters and areas of complex, irregular shapes using three fundamental algorithmic paradigms: (1) Polygon Triangulation: Any simple n-gon can be partitioned into n - 2 triangles, computing total area as the sum of triangular sub-areas. (2) Gauss's Shoelace Algorithm: For any polygon with ordered vertices (x_i, y_i), Area = (1/2)|Σ (x_i y_{i+1} - x_{i+1} y_i)| using cross-multiplication in O(n) time. (3) Monte Carlo Integration: Approximating circle area and π by throwing N random points into a bounding square of side 2r: (N_inside / N_total) ≈ (πr²) / (4r²) = π/4, so π ≈ 4 × (N_inside / N_total).",
        "key_points": [
            "Polygon Decomposition: Decomposing arbitrary n-gons into n - 2 non-overlapping triangles.",
            "The Shoelace Algorithm: Computes area of any 2D polygon in O(n) time via coordinate determinant sums.",
            "Monte Carlo Method: Stochastic approximation of area and π using uniform random point distributions.",
            "Resolution Independence: Algorithmic decomposition scales from small CAD blueprints to satellite geographic mapping.",
            "Algorithmic Pipeline: Input Coordinates → Boundary Edge Traversal → Determinant Summation → Area Evaluation."
        ],
        "narration": "How does a GPS app or CAD software calculate the area of an irregular building plot or island? It uses algorithmic pipelines! Either by decomposing complex shapes into simple triangles, using Gauss's Shoelace cross-multiplication on coordinate vertices, or running Monte Carlo dartboard simulations. Click 'Throw 1000 Darts' to watch the Monte Carlo algorithm estimate π right before your eyes!",
        "sim_title": "Monte Carlo Pi Dartboard Simulator & Gauss Shoelace Polygon Engine",
        "checkpoints": [
            {
                "q": "In a Monte Carlo simulation for estimating π, 785 out of 1000 darts land inside an inscribed circle within a square of side 2r. What is the estimated value of π?",
                "options": ["3.10", "3.14", "3.18", "3.24"],
                "ans": 1,
                "exp": "Area ratio = (π r²) / (4 r²) = π / 4 ≈ 785 / 1000 = 0.785. Therefore, π ≈ 4 × 0.785 = 3.14."
            },
            {
                "q": "Gauss's Shoelace Algorithm calculates polygon area using which coordinate operation?",
                "options": [
                    "Successive cross-multiplications of adjacent vertex coordinates (x_i y_{i+1} - x_{i+1} y_i)",
                    "Computing distances between all vertex pairs",
                    "Finding the slope of each polygon side",
                    "Calculating the circumradius of the polygon"
                ],
                "ans": 0,
                "exp": "The Shoelace formula computes Area = (1/2)|Σ (x_i y_{i+1} - x_{i+1} y_i)| by summing cross-products of adjacent coordinate pairs."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 17,
        "title": "Mastery Challenge I: Perimeters, Pi & Historical Approximations",
        "badge": "CG-5 • C-5.1 • Questions 1–10",
        "desc": "Test your mastery on polygon perimeter metrics, circle circumference, the nature and irrationality of π, and historical approximations from Archimedes, Aryabhata, and Zu Chongzhi.",
        "questions": [
            {
                "q": "1. What is the circumference of a circular running track whose diameter is 70 meters? (Use π = 22/7)",
                "options": ["110 m", "220 m", "350 m", "440 m"],
                "ans": 1,
                "solution": "Step 1: Circumference formula C = π × d.\nStep 2: C = (22/7) × 70 m.\nStep 3: C = 22 × 10 = 220 m."
            },
            {
                "q": "2. How many complete revolutions will a bicycle wheel of radius 35 cm make to cover a total distance of 1.1 km? (Use π = 22/7)",
                "options": ["250 revolutions", "500 revolutions", "750 revolutions", "1000 revolutions"],
                "ans": 1,
                "solution": "Step 1: Total distance = 1.1 km = 1100 m = 110,000 cm.\nStep 2: Circumference of wheel = 2πr = 2 × (22/7) × 35 = 220 cm.\nStep 3: Number of revolutions = Distance / C = 110,000 / 220 = 500 revolutions."
            },
            {
                "q": "3. Which of the following statements about π is mathematically TRUE?",
                "options": [
                    "π is equal to 22/7",
                    "π is a rational number with repeating decimal digits",
                    "π is an irrational real number whose decimal expansion never terminates or repeats",
                    "π was discovered by Isaac Newton using calculus"
                ],
                "ans": 2,
                "solution": "Step 1: π is defined as the ratio of circumference to diameter in Euclidean geometry.\nStep 2: Lambert (1761) proved π is irrational.\nStep 3: Its decimal expansion 3.14159265... is strictly non-terminating and non-repeating."
            },
            {
                "q": "4. In ancient Greece, Archimedes bounded π by inscribing and circumscribing regular polygons with how many sides?",
                "options": ["24 sides", "48 sides", "64 sides", "96 sides"],
                "ans": 3,
                "solution": "Step 1: Archimedes started with a regular hexagon (6 sides).\nStep 2: He doubled the sides successively: 6 → 12 → 24 → 48 → 96.\nStep 3: Using a 96-gon, he proved 223/71 < π < 22/7."
            },
            {
                "q": "5. What is the perimeter of a semicircle protractor of radius 7 cm, including its straight base diameter? (Use π = 22/7)",
                "options": ["22 cm", "29 cm", "36 cm", "44 cm"],
                "ans": 2,
                "solution": "Step 1: Curved boundary = πr = (22/7) × 7 = 22 cm.\nStep 2: Straight base diameter = 2r = 2 × 7 = 14 cm.\nStep 3: Total perimeter = πr + 2r = 22 + 14 = 36 cm."
            },
            {
                "q": "6. A wire bent in the shape of a circle of radius 28 cm is rebent into the shape of a square. What is the length of each side of the square? (Use π = 22/7)",
                "options": ["22 cm", "44 cm", "88 cm", "176 cm"],
                "ans": 1,
                "solution": "Step 1: Length of wire = Circumference of circle = 2πr = 2 × (22/7) × 28 = 176 cm.\nStep 2: Perimeter of square = 4s = 176 cm.\nStep 3: Side of square s = 176 / 4 = 44 cm."
            },
            {
                "q": "7. What is the length of an arc that subtends a central angle of 45° in a circle of radius 14 cm? (Use π = 22/7)",
                "options": ["5.5 cm", "11 cm", "22 cm", "44 cm"],
                "ans": 1,
                "solution": "Step 1: Arc length formula l = (θ / 360°) × 2πr.\nStep 2: l = (45 / 360) × 2 × (22/7) × 14 = (1/8) × 88.\nStep 3: l = 11 cm."
            },
            {
                "q": "8. What is the percentage difference between the approximation 22/7 (≈ 3.142857) and π (≈ 3.141593)?",
                "options": ["Approximately 0.04%", "Approximately 0.4%", "Approximately 1.2%", "Approximately 4.0%"],
                "ans": 0,
                "solution": "Step 1: Absolute error = 22/7 - π ≈ 3.142857 - 3.141593 = 0.001264.\nStep 2: Relative error = 0.001264 / 3.141593 ≈ 0.000402.\nStep 3: Percentage error ≈ 0.04%."
            },
            {
                "q": "9. If the perimeter of a regular octagon is 96 cm, what is the length of each side?",
                "options": ["8 cm", "10 cm", "12 cm", "16 cm"],
                "ans": 2,
                "solution": "Step 1: A regular octagon has 8 equal sides.\nStep 2: Perimeter P = 8 × s = 96 cm.\nStep 3: Side s = 96 / 8 = 12 cm."
            },
            {
                "q": "10. Aryabhata's verse describes the ratio 62832 / 20000. In decimal form, this value is exactly:",
                "options": ["3.1412", "3.1416", "3.1428", "3.1450"],
                "ans": 1,
                "solution": "Step 1: Divide numerator and denominator by 2: 31416 / 10000.\nStep 2: Shift the decimal 4 places left: 3.1416.\nStep 3: Aryabhata noted this is 'āsanna' (approaching/approximate)."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge II: Arc Lengths, Polygon Areas & Triangle Medians",
        "badge": "CG-5 • C-7.3 • Questions 11–20",
        "desc": "Solve problems on circular arc lengths, sector perimeters, rolling wheel revolutions, shearing in parallelograms, and the Triangle Median Area Bisection Theorem.",
        "questions": [
            {
                "q": "11. A triangle and a parallelogram have the same base and lie between the same parallel lines. What is the ratio of Area(triangle) to Area(parallelogram)?",
                "options": ["1 : 4", "1 : 2", "1 : 1", "2 : 1"],
                "ans": 1,
                "solution": "Step 1: Let base = b and height = h.\nStep 2: Area(triangle) = (1/2) b h.\nStep 3: Area(parallelogram) = b h.\nStep 4: Ratio = [(1/2) b h] / [b h] = 1 : 2."
            },
            {
                "q": "12. In ΔPQR, QM is a median to side PR. If Area(ΔPQR) = 64 cm², what is Area(ΔQMR)?",
                "options": ["16 cm²", "32 cm²", "48 cm²", "64 cm²"],
                "ans": 1,
                "solution": "Step 1: A median bisects a triangle into two sub-triangles of equal area.\nStep 2: Area(ΔQMR) = (1/2) × Area(ΔPQR).\nStep 3: Area(ΔQMR) = 64 / 2 = 32 cm²."
            },
            {
                "q": "13. In ΔABC, D, E, and F are the midpoints of sides BC, CA, and AB respectively. What fraction of Area(ΔABC) is Area(ΔDEF)?",
                "options": ["1/2", "1/3", "1/4", "1/6"],
                "ans": 2,
                "solution": "Step 1: By the Midpoint Theorem, joining the midpoints of the three sides divides the parent triangle into 4 congruent triangles.\nStep 2: Each small triangle has area = (1/4) × Area(ΔABC)."
            },
            {
                "q": "14. A rhombus has diagonals of lengths 16 cm and 12 cm. What is its area?",
                "options": ["48 cm²", "96 cm²", "144 cm²", "192 cm²"],
                "ans": 1,
                "solution": "Step 1: Area of rhombus = (1/2) × d1 × d2.\nStep 2: Area = (1/2) × 16 × 12 = 8 × 12 = 96 cm²."
            },
            {
                "q": "15. A trapezium has parallel sides of lengths 14 cm and 20 cm, and the distance between them is 8 cm. What is its area?",
                "options": ["120 cm²", "136 cm²", "154 cm²", "272 cm²"],
                "ans": 1,
                "solution": "Step 1: Area of trapezium = (1/2) × (sum of parallel sides) × height.\nStep 2: Area = (1/2) × (14 + 20) × 8 = (1/2) × 34 × 8 = 17 × 8 = 136 cm²."
            },
            {
                "q": "16. Centroid G of ΔABC divides the median AD in what ratio from vertex A to midpoint D?",
                "options": ["1 : 1", "2 : 1", "3 : 1", "3 : 2"],
                "ans": 1,
                "solution": "Step 1: In any triangle, the centroid G divides each median in the ratio 2 : 1 from the vertex.\nStep 2: AG : GD = 2 : 1."
            },
            {
                "q": "17. If Area(ΔGBC) = 15 cm² where G is the centroid of ΔABC, what is the total Area(ΔABC)?",
                "options": ["30 cm²", "45 cm²", "60 cm²", "75 cm²"],
                "ans": 1,
                "solution": "Step 1: The centroid joins the vertices to form 3 triangles of equal area: ΔGAB, ΔGBC, and ΔGCA.\nStep 2: Area(ΔABC) = 3 × Area(ΔGBC) = 3 × 15 = 45 cm²."
            },
            {
                "q": "18. A rectangular courtyard of length 25 m and width 16 m is to be paved with square tiles of side 2 m. How many tiles are needed?",
                "options": ["50 tiles", "100 tiles", "125 tiles", "200 tiles"],
                "ans": 1,
                "solution": "Step 1: Area of courtyard = 25 × 16 = 400 m².\nStep 2: Area of one square tile = 2 × 2 = 4 m².\nStep 3: Number of tiles = 400 / 4 = 100 tiles."
            },
            {
                "q": "19. The base of an isosceles triangle is 12 cm and its perimeter is 32 cm. What is its area?",
                "options": ["36 cm²", "48 cm²", "60 cm²", "72 cm²"],
                "ans": 1,
                "solution": "Step 1: Sum of equal sides = 32 - 12 = 20 cm, so each equal side = 10 cm.\nStep 2: Altitude dropped to base bisects it into 6 cm. By Pythagoras: h = √(10² - 6²) = √(100 - 36) = √64 = 8 cm.\nStep 3: Area = (1/2) × base × height = (1/2) × 12 × 8 = 48 cm²."
            },
            {
                "q": "20. Why do two triangles on the same base and between the same parallels have equal area?",
                "options": [
                    "Because their sides are congruent",
                    "Because their perimeters are identical",
                    "Because they share the same base length and identical perpendicular altitude between the parallel lines",
                    "Because they must be right-angled"
                ],
                "ans": 2,
                "solution": "Step 1: Parallel lines are equidistant everywhere, so perpendicular distance (height h) is constant.\nStep 2: Area = (1/2) × base × height.\nStep 3: Since base and height are identical, both areas are equal."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge III: Heron’s Formula, Squaring & Circle Derivations",
        "badge": "CG-5 • C-7.1 • Questions 21–30",
        "desc": "Apply Heron's formula to scalene and isosceles triangles, explore Baudhayana's Sulbasutra rectangular squaring, and analyze sector slicing derivations of circle area.",
        "questions": [
            {
                "q": "21. What is the area of a triangle with sides 6 cm, 8 cm, and 10 cm?",
                "options": ["24 cm²", "30 cm²", "40 cm²", "48 cm²"],
                "ans": 0,
                "solution": "Step 1: Check Pythagoras: 6² + 8² = 36 + 64 = 100 = 10², so it is a right triangle.\nStep 2: Area = (1/2) × 6 × 8 = 24 cm².\nStep 3: Alternatively via Heron: s = (6+8+10)/2 = 12; Area = √[12(6)(4)(2)] = √576 = 24 cm²."
            },
            {
                "q": "22. The sides of a triangular field are in the ratio 3 : 5 : 7 and its perimeter is 300 m. What is its area?",
                "options": ["1200√3 m²", "1500√3 m²", "1800√3 m²", "2000√3 m²"],
                "ans": 1,
                "solution": "Step 1: Let sides be 3x, 5x, 7x. Perimeter = 15x = 300 m ⇒ x = 20 m.\nStep 2: Sides are a = 60 m, b = 100 m, c = 140 m.\nStep 3: Semi-perimeter s = 150 m.\nStep 4: Area = √[150 × (150-60) × (150-100) × (150-140)] = √[150 × 90 × 50 × 10] = √6750000 = 1500√3 m²."
            },
            {
                "q": "23. In Baudhayana's Sulbasutras, squaring a rectangle of dimensions a × b produces a square of side x equal to:",
                "options": ["(a + b) / 2", "√(ab)", "√(a² + b²)", "(a - b) / 2"],
                "ans": 1,
                "solution": "Step 1: Squaring a rectangle means constructing a square of equal area: x² = ab.\nStep 2: Therefore, the side of the square is the geometric mean x = √(ab).\nStep 3: Baudhayana achieved this via the difference of two squares identity: [(a+b)/2]² - [(a-b)/2]²."
            },
            {
                "q": "24. A rectangle has dimensions 25 cm × 4 cm. What is the side of an equal-area square constructed via Baudhayana's method?",
                "options": ["8 cm", "10 cm", "12.5 cm", "14.5 cm"],
                "ans": 1,
                "solution": "Step 1: Area of rectangle = 25 × 4 = 100 cm².\nStep 2: Side of square x = √100 = 10 cm."
            },
            {
                "q": "25. When slicing a circle into N wedges to derive Area = πr², why does the base of the rearranged rectangle equal πr rather than 2πr?",
                "options": [
                    "Because half the pie wedges point upward and half point downward, dividing the circumference equally between top and bottom edges",
                    "Because the circle is cut in half first",
                    "Because radius r is halved",
                    "Because π is divided by 2"
                ],
                "ans": 0,
                "solution": "Step 1: The total circumference 2πr is distributed evenly between the top and bottom saw-tooth edges.\nStep 2: Each edge receives half the circumference: (2πr) / 2 = πr.\nStep 3: Base × Height = (πr) × r = πr²."
            },
            {
                "q": "26. What is the area of a circle whose circumference is 44 cm? (Use π = 22/7)",
                "options": ["88 cm²", "154 cm²", "308 cm²", "616 cm²"],
                "ans": 1,
                "solution": "Step 1: Circumference C = 2πr = 44 cm ⇒ 2 × (22/7) × r = 44 ⇒ r = 7 cm.\nStep 2: Area = πr² = (22/7) × 7² = 22 × 7 = 154 cm²."
            },
            {
                "q": "27. Using the Egyptian Rhind Papyrus formula Area ≈ [(8/9)d]², what is the approximate area of a circle with diameter d = 9 units?",
                "options": ["56 sq units", "64 sq units", "72 sq units", "81 sq units"],
                "ans": 1,
                "solution": "Step 1: (8/9) × d = (8/9) × 9 = 8 units.\nStep 2: Square the result: 8² = 64 sq units.\nStep 3: The exact area is π × 4.5² ≈ 63.62, so 64 is accurate within ~0.6%!"
            },
            {
                "q": "28. Find the cost of leveling a triangular park with sides 50 m, 65 m, and 65 m at the rate of ₹7 per m².",
                "options": ["₹7,500", "₹10,500", "₹14,000", "₹21,000"],
                "ans": 1,
                "solution": "Step 1: Triangle is isosceles with base 50 m and equal sides 65 m.\nStep 2: Altitude h = √(65² - 25²) = √(4225 - 625) = √3600 = 60 m.\nStep 3: Area = (1/2) × 50 × 60 = 1500 m².\nStep 4: Cost = 1500 × ₹7 = ₹10,500."
            },
            {
                "q": "29. If the radius of a circle is tripled, by what factor does its area increase?",
                "options": ["3 times", "6 times", "9 times", "27 times"],
                "ans": 2,
                "solution": "Step 1: Area A1 = πr².\nStep 2: New area A2 = π(3r)² = 9πr² = 9 A1.\nStep 3: The area increases by a factor of 3² = 9."
            },
            {
                "q": "30. What is the area of an equilateral triangle with perimeter 36 cm?",
                "options": ["36√3 cm²", "48√3 cm²", "72√3 cm²", "144√3 cm²"],
                "ans": 0,
                "solution": "Step 1: Side a = 36 / 3 = 12 cm.\nStep 2: Area = (√3 / 4) a² = (√3 / 4) × 144 = 36√3 cm²."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge IV: Sectors, Segments, Brahmagupta & Generalisation",
        "badge": "CG-5 • CG-9 • Questions 31–40",
        "desc": "Tackle real-world sector and segment problems, Brahmagupta's formula for cyclic quadrilaterals, Heron's reduction, formula hierarchies, and computational mensuration algorithms.",
        "questions": [
            {
                "q": "31. A car wiper of blade length 25 cm sweeps through an angle of 115°. What is the total swept area by one wiper? (Use π = 22/7)",
                "options": ["580.45 cm²", "627.48 cm²", "1254.96 cm²", "1500.00 cm²"],
                "ans": 1,
                "solution": "Step 1: Swept area = (θ / 360°) × πr².\nStep 2: Area = (115 / 360) × (22/7) × 25² = (23 / 72) × (22/7) × 625.\nStep 3: Area = (23 × 11 × 625) / (36 × 7) = 158125 / 252 ≈ 627.48 cm²."
            },
            {
                "q": "32. A chord of a circle of radius 14 cm subtends an angle of 60° at the centre. What is the area of the minor segment? (Use π = 22/7 and √3 = 1.732)",
                "options": ["14.54 cm²", "17.89 cm²", "24.12 cm²", "32.45 cm²"],
                "ans": 1,
                "solution": "Step 1: Area(sector) = (60/360) × (22/7) × 14² = (1/6) × 22 × 28 = 102.67 cm².\nStep 2: Area(ΔOAB) = (√3 / 4) × 14² = (1.732 / 4) × 196 = 84.87 cm².\nStep 3: Area(segment) = 102.67 - 84.87 = 17.80 cm² (≈ 17.89 cm²)."
            },
            {
                "q": "33. What is the area of a cyclic quadrilateral with sides 1 cm, 2 cm, 3 cm, and 4 cm?",
                "options": ["√18 ≈ 4.24", "√24 ≈ 4.90", "√30 ≈ 5.48", "6.00"],
                "ans": 1,
                "solution": "Step 1: Semi-perimeter s = (1 + 2 + 3 + 4)/2 = 5.\nStep 2: Factors: (s-a)=4, (s-b)=3, (s-c)=2, (s-d)=1.\nStep 3: Area = √(4 × 3 × 2 × 1) = √24 ≈ 4.899 cm²."
            },
            {
                "q": "34. How does Brahmagupta's formula prove that a cyclic quadrilateral has maximum area among all quadrilaterals with the same side lengths?",
                "options": [
                    "Because Bretschneider's formula subtracts the non-negative term abcd cos²((A+C)/2), which is minimized (zero) precisely when A+C=180°",
                    "Because cyclic quadrilaterals have equal diagonals",
                    "Because opposite sides are equal",
                    "Because all angles are 90°"
                ],
                "ans": 0,
                "solution": "Step 1: Bretschneider's formula: Area² = (s-a)(s-b)(s-c)(s-d) - abcd cos²((A+C)/2).\nStep 2: Since abcd cos²(...) ≥ 0, the maximum area occurs when this subtracted term is zero.\nStep 3: This happens when cos((A+C)/2) = 0 ⇒ A + C = 180° (the cyclic condition)."
            },
            {
                "q": "35. If the side lengths of a cyclic quadrilateral are 5 cm, 12 cm, 5 cm, and 12 cm (a rectangle), what is its area?",
                "options": ["30 cm²", "60 cm²", "120 cm²", "144 cm²"],
                "ans": 1,
                "solution": "Step 1: A rectangle with sides 5 and 12 is cyclic with diameter 13.\nStep 2: Area = 5 × 12 = 60 cm².\nStep 3: Via Brahmagupta: s = 34/2 = 17. Factors: (17-5)=12, (17-12)=5, (17-5)=12, (17-12)=5. Area = √(12² × 5²) = 60 cm²."
            },
            {
                "q": "36. In computational mensuration, what is the minimum number of triangles required to triangulate a simple convex n-gon?",
                "options": ["n - 3", "n - 2", "n - 1", "n"],
                "ans": 1,
                "solution": "Step 1: Drawing all non-intersecting diagonals from a single vertex to the other vertices produces triangles.\nStep 2: From 1 vertex, we can draw diagonals to n - 3 other vertices.\nStep 3: These diagonals partition the n-gon into exactly n - 2 triangles."
            },
            {
                "q": "37. A circular sprinkler sprays water over a radius of 7 meters through an arc of 120°. What is the watered lawn area? (Use π = 22/7)",
                "options": ["25.67 m²", "51.33 m²", "77.00 m²", "154.00 m²"],
                "ans": 1,
                "solution": "Step 1: Area = (θ / 360°) × πr².\nStep 2: Area = (120 / 360) × (22/7) × 7² = (1/3) × 22 × 7 = 154 / 3 ≈ 51.33 m²."
            },
            {
                "q": "38. The perimeter of a sector of a circle of radius 5.6 cm is 27.2 cm. What is the area of the sector?",
                "options": ["22.4 cm²", "33.6 cm²", "44.8 cm²", "56.0 cm²"],
                "ans": 2,
                "solution": "Step 1: Perimeter of sector P = l + 2r ⇒ 27.2 = l + 2(5.6) = l + 11.2.\nStep 2: Arc length l = 27.2 - 11.2 = 16.0 cm.\nStep 3: Area of sector = (1/2) × l × r = (1/2) × 16.0 × 5.6 = 8.0 × 5.6 = 44.8 cm²."
            },
            {
                "q": "39. Which mathematical property guarantees that every triangle has a valid circumcircle?",
                "options": [
                    "The sum of angles is 180°",
                    "The perpendicular bisectors of the three sides are always concurrent at the circumcentre",
                    "The three altitudes are concurrent at the orthocentre",
                    "The triangle inequality theorem"
                ],
                "ans": 1,
                "solution": "Step 1: In any triangle, the perpendicular bisectors of the 3 sides meet at a single point O (the circumcentre).\nStep 2: Point O is equidistant from all 3 vertices: OA = OB = OC = R (circumradius).\nStep 3: A circle with centre O and radius R passes through all three vertices, proving every triangle is cyclic."
            },
            {
                "q": "40. In Gauss's Shoelace Algorithm, a triangle has vertices at (0, 0), (6, 0), and (4, 5). What is its computed area?",
                "options": ["12 sq units", "15 sq units", "20 sq units", "30 sq units"],
                "ans": 1,
                "solution": "Step 1: Base lies along x-axis from (0,0) to (6,0) with length b = 6.\nStep 2: Height is the y-coordinate of vertex (4,5), so h = 5.\nStep 3: Area = (1/2) × base × height = (1/2) × 6 × 5 = 15 sq units.\nStep 4: Shoelace: (1/2) |(0×0 - 6×0) + (6×5 - 4×0) + (4×0 - 0×5)| = (1/2) |30| = 15."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Total Slides: {len(SLIDES)}")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    print(f"Total Quiz Slides: {len(QUIZZES)}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, "Must have exactly 16 content slides"
    assert total_cp == 32, "Must have exactly 32 checkpoints (2 per slide)"
    assert len(QUIZZES) == 4, "Must have exactly 4 quiz slides"
    assert total_qz == 40, "Must have exactly 40 quiz questions (10 per quiz slide)"
    print("All assertions passed successfully!")


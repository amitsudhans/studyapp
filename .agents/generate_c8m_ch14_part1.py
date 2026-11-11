#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 14: Area
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 14 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Square Equal Quarters",
        "subtitle": "Section 7.1 Equal Area Divisions: Partitioning Squares into Four Equal-Area Parts via Edge Compression & Expansion",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Fourteen: Area! Open Section Seven Point One by challenging an everyday habit: how many genuinely different ways can you slice a crisp flat square sheet into FOUR pieces having EXACTLY EQUAL AREA? "
            "Almost everyone slices vertically into four parallel strips, cuts like a plus sign into four congruent small squares, or slices along BOTH diagonals into four congruent right triangles! Now watch the deeper geometric principle behind EQUAL AREA DIVISIONS: pieces sharing IDENTICAL AREA do NOT need identical shapes or congruent boundaries! "
            "Suppose a unit square of side 1 unit has total area 1 square unit, so every quarter MUST carry area exactly one-fourth square unit! Try cutting the top half into two equal rectangles, then slicing the bottom half with one slant or step! Even more remarkably, explore EDGE COMPRESSION AND EXPANSION! If one side edge of a strip shrinks by factor k inside a region while its perpendicular height expands cleanly by exact compensating factor 1 divided by k, the interior area locks completely invariant! Comparing parts by overlaying, reassembling half-triangles, and compensating compression with expansion establishes the central theme of this chapter: AREA measures true interior two-dimensional space!"
        ),
        "checkpoints": [
            {
                "question": "If a square of side 8 cm is divided into four parts having equal area, must all four parts have the exact same shape (be congruent)?",
                "options": [
                    "No—any four shapes whose areas each equal 16 cm² form a valid equal-area partition",
                    "Yes—equal area always requires identical congruent shapes",
                    "Only squares can divide a square equally",
                    "Only diagonal cuts produce equal areas"
                ],
                "answer": 0,
                "hint": "Think about comparing a 2×8 cm strip (16 cm²) with a 4×4 cm corner square (16 cm²) inside the same 8×8 cm square!",
                "explanation": "8 × 8 = 64 cm², so each quarter must measure 16 cm². Different non-congruent shapes (e.g., strips, squares, and triangles) can each cover 16 cm²."
            },
            {
                "question": "When transforming a rectangle of fixed area 36 cm² by compressing its width to half (× 1/2), how must its length change to preserve total area?",
                "options": [
                    "Length must double (× 2) to compensate for halving the width",
                    "Length must also halve (× 1/2)",
                    "Length stays completely unchanged",
                    "Length increases by 2 cm only"
                ],
                "answer": 0,
                "hint": "Ensure (width / 2) × (new length) = original width × original length!",
                "explanation": "Multiplying width by 1/2 and length by 2 preserves exact product: (w/2) × (2l) = w × l = 36 cm²."
            }
        ]
    },
    {
        "id": 2,
        "title": "Rectangle Unit Packing",
        "subtitle": "Section 7.1 Unit Squares & Diagonal Bisection: Area = Length × Width (cm², m²) & Half-Area Congruent Triangles",
        "speech": (
            "Now formalize flat area measurement inside Section Seven Point One using UNIT SQUARES! Cover any flat rectangle seamlessly from edge to edge with identical non-overlapping 1 cm by 1 cm unit squares—called square centimeters (cm²)—or 1 m by 1 m unit squares for large classroom floors (m²)! "
            "Place a crisp rectangle measuring 6 cm long and 4 cm wide directly over a unit square grid! Along the bottom row sit 6 complete unit squares; stacked upwards sit 4 identical rows! Counting every packed tile gives 6 + 6 + 6 + 6 = 4 × 6 = 24 unit squares! Even when side lengths involve fractions like 3.5 cm by 2.2 cm, subdividing into smaller hundredth squares proves universally that AREA OF A RECTANGLE equals LENGTH × WIDTH! For a square of side s, length equals width, yielding Area = s²! "
            "Next, slice ANY rectangle diagonally from corner A to opposite corner C! Because opposite sides match identically (AB = CD and AD = CB) alongside shared diagonal chord AC, SSS congruence proves BOTH triangles ΔABC and ΔCDA are EXACTLY CONGRUENT! Therefore, every diagonal bisects EVERY rectangle cleanly into TWO right-angled triangles, each covering EXACTLY HALF of the full rectangle's enclosed area!"
        ),
        "checkpoints": [
            {
                "question": "A rectangular study desk measures 120 cm in length and 65 cm in width. What is its exact surface area and what area does one diagonal cut assign to each triangular half?",
                "options": [
                    "Total area = 7,800 cm²; each diagonal triangle = 3,900 cm²",
                    "Total area = 370 cm²; each triangle = 185 cm²",
                    "Total area = 7,800 cm²; each triangle = 1,950 cm²",
                    "Total area = 7,200 cm²; each triangle = 3,600 cm²"
                ],
                "answer": 0,
                "hint": "Compute 120 × 65 first, then take exactly half (÷ 2) because the diagonal creates two congruent triangles!",
                "explanation": "Rectangle Area = 120 × 65 = 7,800 cm². Each congruent triangle along the diagonal covers 7,800 ÷ 2 = 3,900 cm²."
            },
            {
                "question": "Why does diagonal AC divide rectangle ABCD into two triangles of guaranteed equal area?",
                "options": [
                    "By SSS congruence (AB = CD, BC = DA, AC = AC), ΔABC ≅ ΔCDA, and congruent figures always share equal areas",
                    "Only when ABCD is a square with equal width and length",
                    "Because every triangle has equal side lengths",
                    "Because perimeters of both triangles equal half the diagonal"
                ],
                "answer": 0,
                "hint": "Compare the three pairs of sides of ΔABC and ΔCDA!",
                "explanation": "Opposite sides of a rectangle are equal and AC is common, making ΔABC ≅ ΔCDA by SSS congruence with exactly half the rectangle's area each."
            }
        ]
    },
    {
        "id": 3,
        "title": "Perimeter Versus Area",
        "subtitle": "Independence of Boundary & Region: Identical Perimeters with Different Areas & Larger Perimeter with Smaller Area",
        "speech": (
            "Pause carefully to answer a classic mathematical misconception from Section Seven Point One: WHY CAN'T PERIMETER BE A MEASURE OF AREA? Suppose two farmers own rectangular fields surrounded by the exact same length of fencing wire—say PERIMETER = 24 meters! Surely identical fence lengths enclose identical farmland inside?! Test two clean examples immediately! "
            "Field One is a sleek 6 m × 6 m square: Perimeter = 4 × 6 = 24 m, and Area = 6 × 6 = 36 m²! Field Two is a narrow 11 m × 1 m strip: Perimeter = 2(11 + 1) = 24 m—IDENTICAL boundary fence—yet its enclosed Area collapses dramatically to ONLY 11 × 1 = 11 m²! Less than ONE-THIRD the area with the exact same perimeter! "
            "Can a shape even have a MUCH LARGER PERIMETER alongside a SMALLER AREA?! YES! Take a 4 × 4 square (Perimeter 16 units, Area 16 sq units) and nibble tiny square notches inward along its top edge! Removing 2 unit squares REDUCES enclosed area down to 14 sq units, while adding jagged vertical boundary steps PUSHES total perimeter UP to 20 units! Perimeter tracks ONLY 1D boundary length; Area measures enclosed 2D space!"
        ),
        "checkpoints": [
            {
                "question": "Compare a 5 cm × 5 cm square with a 9 cm × 1 cm rectangle. Which statement holds completely true?",
                "options": [
                    "Both have identical perimeter 20 cm, yet the square encloses 25 cm² while the slim rectangle encloses only 9 cm²",
                    "Both enclose identical area 25 cm² because their perimeters match",
                    "The 9 cm × 1 cm rectangle encloses more area because 9 > 5",
                    "Perimeter uniquely determines area for all rectangles"
                ],
                "answer": 0,
                "hint": "Check 2(l + w) and l × w separately for both shapes!",
                "explanation": "2(5+5) = 20 cm and 2(9+1) = 20 cm (same perimeter), whereas areas differ sharply: 25 cm² vs 9 cm²."
            },
            {
                "question": "If you carve a rectangular inward notch out of the middle of one side of a 10 cm × 6 cm board (removing part of the wood without cutting corner vertices), how do area and perimeter change?",
                "options": [
                    "Area strictly DECREASES while Perimeter strictly INCREASES due to the two new inward wall segments",
                    "Both area and perimeter stay strictly unchanged",
                    "Area increases while perimeter decreases",
                    "Area decreases and perimeter always decreases by the exact same number"
                ],
                "answer": 0,
                "hint": "Trace the path along the notch: horizontal bottom matches removed top, plus two brand-new vertical side walls!",
                "explanation": "Cutting inward removes material (Area drops), while introducing two extra perpendicular walls increases boundary length (Perimeter rises)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Triangles In Rectangles",
        "subtitle": "Triangle Area Foundation: Enclosing Acute & Right Triangles Inside Rectangles Using Base & Perpendicular Height",
        "speech": (
            "Step inside the Triangles section by comparing areas of triangles tightly fitted inside bounding rectangles! Draw ANY horizontal rectangle PQRS having base length b along bottom edge PQ and perpendicular height h along vertical edge QR! Now pick ANY point T sitting anywhere along top horizontal edge SR—whether dead center or shifted sideways toward corner S or R—and connect straight sides to draw triangle ΔPQT! What exact fraction of enclosing rectangle PQRS does ΔPQT cover?! "
            "Drop a vertical dashed perpendicular altitude TM straight downward from peak vertex T onto bottom base PQ! Notice segment TM equals exact rectangle height h, slicing BOTH outer rectangle PQRS AND interior triangle ΔPQT cleanly into left and right sub-rectangles! "
            "Inspect the LEFT sub-rectangle (PMTS): triangle edge PT acts as its exact diagonal, cutting left box area strictly in HALF! Inspect the RIGHT sub-rectangle (MQRT): edge TQ acts as its exact diagonal, cutting right box area strictly in HALF! Sum both triangular halves together cleanly: half of left sub-rectangle plus half of right sub-rectangle equals EXACTLY HALF OF THE ENTIRE RECTANGLE PQRS! Therefore, for EVERY right-angled or acute triangle sharing base b and perpendicular height h, Area = 1/2 × base × height!"
        ),
        "checkpoints": [
            {
                "question": "Point T slides freely anywhere along the top edge SR of a rectangle PQRS (base PQ = 14 cm, height = 8 cm). What happens to the area of ΔPQT?",
                "options": [
                    "Area stays locked identically at 1/2 × 14 × 8 = 56 cm² everywhere along SR",
                    "Area reaches maximum when T hits corner R and shrinks in the middle",
                    "Area changes randomly depending on slanted edge lengths PT and QT",
                    "Area equals 112 cm² when T is centered"
                ],
                "answer": 0,
                "hint": "Every point on SR maintains the exact same perpendicular height 8 cm above fixed base PQ = 14 cm!",
                "explanation": "Dropping an altitude from T splits the rectangle into two sub-rectangles, each halved by PT and TQ, preserving total triangle area = 1/2(14)(8) = 56 cm²."
            },
            {
                "question": "A right-angled triangle has legs (perpendicular sides) measuring 9 cm and 12 cm. Find its exact area:",
                "options": [
                    "54 cm²",
                    "108 cm²",
                    "21 cm²",
                    "42 cm²"
                ],
                "answer": 0,
                "hint": "In a right triangle, one perpendicular leg acts as base (9 cm) and the other acts as height (12 cm)!",
                "explanation": "Area = 1/2 × base × height = 1/2 × 9 × 12 = 54 cm²."
            }
        ]
    },
    {
        "id": 5,
        "title": "Obtuse Triangle Formula",
        "subtitle": "General Triangle Proof: Validating Area = 1/2 × Base × Height for Obtuse Triangles Using Enclosure Subtraction",
        "speech": (
            "Earlier, our two-box slicing proof worked smoothly whenever peak vertex T hovered directly ABOVE interior base PQ! Now answer the tricky case: what happens when triangle ΔABC is OBTUSE so its top peak C overhangs COMPLETELY OUTSIDE horizontal base AB?! Does Area = 1/2 × base × height STILL hold universally across acute, right, and obtuse triangles? PROVE IT using bounding rectangle subtraction right now! "
            "Extend horizontal base AB smoothly rightward to point D directly beneath overhanging peak C, dropping perpendicular altitude CD of exact height h outside the triangle! Notice CD lands strictly OUTSIDE segment AB! Let bottom base AB = b and horizontal overhang extension BD = x! "
            "Observe TWO right-angled triangles anchored at shared right-angle corner D: BIG right triangle ΔADC spans total base (b + x) and height h, covering exact area 1/2 × (b + x) × h = 1/2 bh + 1/2 xh! SMALL white overhanging right triangle ΔBDC has base x and height h, covering exact area 1/2 xh! Subtract small right triangle ΔBDC cleanly from big right triangle ΔADC: (1/2 bh + 1/2 xh) − 1/2 xh! Both 1/2 xh overhang terms CANCEL ZERO—proving universally across acute, right, AND obtuse triangles: Area = 1/2 × base × height!"
        ),
        "checkpoints": [
            {
                "question": "An obtuse triangle ΔABC has bottom horizontal base AB = 10 cm, and the perpendicular altitude dropped from peak C hits the extended base line at D (4 cm outside B) with height CD = 6 cm. Find the exact area of ΔABC:",
                "options": [
                    "30 cm²   (Area(ΔADC) − Area(ΔBDC) = 42 − 12 = 30 cm², matching 1/2 × 10 × 6)",
                    "42 cm²   (using extended base 14 cm)",
                    "12 cm²",
                    "60 cm²"
                ],
                "answer": 0,
                "hint": "Either compute big right triangle 1/2(14)(6) minus white triangle 1/2(4)(6), or apply 1/2 × AB × height!",
                "explanation": "Area(ΔADC) − Area(ΔBDC) = 1/2(10+4)(6) − 1/2(4)(6) = 42 − 12 = 30 cm², identically equal to 1/2 × 10 × 6 = 30 cm²."
            },
            {
                "question": "For ANY triangle—whether acute, right-angled, or obtuse—how is height h ALWAYS measured relative to a chosen base side?",
                "options": [
                    "Perpendicular shortest distance (90°) from the opposite vertex straight to the line containing that base",
                    "Length of the longest slanted edge touching that base",
                    "Average of the other two side lengths",
                    "Always strictly lying inside the triangle's interior"
                ],
                "answer": 0,
                "hint": "In an obtuse triangle, the 90° altitude lands perpendicular to the extended line of the base!",
                "explanation": "Height is strictly the perpendicular distance from the opposite vertex to the base (or its extension in obtuse triangles)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Finding Unknown Altitudes",
        "subtitle": "Applications of Area Formula: Equating Dual Base-Altitude Expressions (1/2 b₁h₁ = 1/2 b₂h₂) to Find Missing Lengths",
        "speech": (
            "Now put the universal triangle area law directly to work inside Section Applications of the Area Formula! Notice ANY triangle possesses THREE distinct side edges, meaning THREE completely valid choices of base—each paired cleanly with its OWN matching perpendicular altitude! Regardless of which base-altitude pair you select to measure, the physical triangle encloses ONE SINGLE FIXED TWO-DIMENSIONAL AREA! "
            "Watch how equating TWO different base-altitude area expressions unlocks unknown side lengths or hidden altitudes effortlessly! Suppose triangle ΔPQR has side QR = 12 cm carrying corresponding perpendicular altitude PM = 5 cm! Compute its area immediately: Area = 1/2 × 12 × 5 = 30 cm²! Now suppose second side edge PR measures 10 cm—what is the exact unknown altitude QN dropped perpendicularly from opposite vertex Q onto side PR? "
            "Simply set BOTH area expressions equal cleanly to each other: 1/2 × PR × QN = 30 cm² → 1/2 × 10 × QN = 30 → 5 × QN = 30 → divide by 5 → QN = 6 cm instantly! Even better, cancel factor 1/2 directly to reveal b₁ × h₁ = b₂ × h₂: shorter bases ALWAYS pair with taller altitudes so products match identically!"
        ),
        "checkpoints": [
            {
                "question": "In ΔABC, base BC = 16 cm has altitude AD = 9 cm. If second side AC = 12 cm, use equal areas (b₁h₁ = b₂h₂) to find altitude BE dropped onto AC:",
                "options": [
                    "12 cm   (since 16 × 9 = 144 = 12 × BE → BE = 12 cm)",
                    "9 cm",
                    "6 cm",
                    "16 cm"
                ],
                "answer": 0,
                "hint": "Compute Area = 1/2 × 16 × 9 = 72 cm², then solve 1/2 × 12 × BE = 72!",
                "explanation": "1/2 × 16 × 9 = 72 cm². Setting 1/2 × 12 × BE = 72 gives 6 × BE = 72, so BE = 12 cm."
            },
            {
                "question": "A right-angled triangle has legs 6 cm and 8 cm, and hypotenuse 10 cm. Using dual area expressions, find the perpendicular altitude h dropped from the right-angle vertex onto the hypotenuse:",
                "options": [
                    "4.8 cm   (6 × 8 = 10 × h → 48 / 10 = 4.8 cm)",
                    "7 cm",
                    "5 cm",
                    "2.4 cm"
                ],
                "answer": 0,
                "hint": "Compare Area using legs (1/2 × 6 × 8) against Area using hypotenuse (1/2 × 10 × h)!",
                "explanation": "Area = 1/2 × 6 × 8 = 24 cm². Equating 1/2 × 10 × h = 24 gives 5h = 24, so h = 4.8 cm."
            }
        ]
    },
    {
        "id": 7,
        "title": "Triangle Median Bisection",
        "subtitle": "Median Area Property: Proving Any Median Joining Vertex to Opposite Midpoint Divides a Triangle into Equal Areas",
        "speech": (
            "Uncover one of geometry's cleanest area theorems in Median Properties! Pick ANY arbitrary triangle ΔABC—no matter how slanted, scalene, wide, or irregular—and locate exact midpoint M directly along bottom base BC so left segment BM EQUALS right segment MC! Now draw a straight line segment connecting opposite top vertex A directly down to midpoint M! This special line segment AM is called a MEDIAN of ΔABC! Does median AM ALWAYS divide ΔABC into two smaller sub-triangles having IDENTICAL AREA? "
            "Inspect left triangle ΔABM and right triangle ΔACM carefully side by side! Check their base lengths first: because point M sits at the exact midpoint of edge BC, base length BM EQUALS base length MC! Now check their perpendicular heights! Drop one single vertical dashed altitude AH straight down from shared top vertex A onto straight base line BC! Because BOTH triangles share the exact same top vertex A and sit along the exact same straight base line BC, BOTH ΔABM and ΔACM share IDENTICAL PERPENDICULAR HEIGHT h = AH! "
            "Compare their areas immediately: Area(ΔABM) = 1/2 × BM × h equals Area(ΔACM) = 1/2 × MC × h! Therefore EVERY MEDIAN BISECTS TRIANGLE AREA INTO TWO EXACT EQUAL HALVES!"
        ),
        "checkpoints": [
            {
                "question": "If the total area of scalene triangle ΔXYZ is 84 cm² and median XN joins vertex X to midpoint N of side YZ, what are the areas of ΔXYN and ΔXZN?",
                "options": [
                    "42 cm² each   (even though ΔXYN and ΔXZN are NOT congruent!)",
                    "Only equal if XY = XZ",
                    "40 cm² and 44 cm²",
                    "28 cm² and 56 cm²"
                ],
                "answer": 0,
                "hint": "Compare bases (YN = NZ) and perpendicular height from shared vertex X!",
                "explanation": "Equal bases YN = NZ and shared perpendicular height from X guarantee Area(ΔXYN) = Area(ΔXZN) = 84 ÷ 2 = 42 cm²."
            },
            {
                "question": "Suppose point P lies along base BC of ΔABC such that BP is ONE-THIRD of whole base BC (BP : PC = 1 : 2). If total Area(ΔABC) = 60 cm², find Area(ΔABP) and Area(ΔAPC):",
                "options": [
                    "Area(ΔABP) = 20 cm² and Area(ΔAPC) = 40 cm²",
                    "Area(ΔABP) = 30 cm² and Area(ΔAPC) = 30 cm²",
                    "Area(ΔABP) = 15 cm² and Area(ΔAPC) = 45 cm²",
                    "Area(ΔABP) = 25 cm² and Area(ΔAPC) = 35 cm²"
                ],
                "answer": 0,
                "hint": "With identical height from vertex A, triangle areas split in exact ratio of their bases (1 : 2)!",
                "explanation": "Same altitude h from A means areas scale linearly with base length: 1/3 × 60 = 20 cm² and 2/3 × 60 = 40 cm²."
            }
        ]
    },
    {
        "id": 8,
        "title": "Parallel Base Triangles",
        "subtitle": "Triangles Between Parallel Lines: Constant Area Shearing & Minimum Perimeter Optimization via Mirror Reflection",
        "speech": (
            "Explore two dazzling theorems uniting parallel lines, constant areas, and mirror reflection optimization! Draw two parallel horizontal tracks—bottom line l and top line m separated by constant vertical perpendicular distance h! Anchor a fixed base AB along bottom track l, then slide apex vertex P freely anywhere along upper parallel track m! Notice every resulting triangle ΔABP, ΔABQ, and ΔABR shares IDENTICAL base AB AND IDENTICAL perpendicular height h between parallel tracks! Therefore, ALL triangles sharing a common base between the same parallel lines possess IDENTICAL AREA (1/2 × AB × h)! "
            "Now solve a brilliant OPTIMIZATION PUZZLE: as apex P glides along top line m while keeping Area FIXED, WHERE should P sit so ΔABP achieves MINIMUM PERIMETER (shortest path AP + PB)?! "
            "Reflect point B perpendicularly across top mirror line m to mirror image B'! By reflection symmetry, distance PB ALWAYS matches distance PB'! So minimizing AP + PB is IDENTICAL to minimizing path A → P → B'! What is the shortest route between points A and B'? ONE STRAIGHT LINE! Intersection point P* occurs precisely where straight segment AB' crosses line m—forming a SYMMETRIC ISOSCELES TRIANGLE (AP* = P*B) with equal reflection angles!"
        ),
        "checkpoints": [
            {
                "question": "Lines l and m are parallel and 7 cm apart. Triangles ΔABC, ΔABD, and ΔABE all share fixed base AB = 10 cm on line l while C, D, E sit at different points along line m. Compare their areas:",
                "options": [
                    "All three triangles have exact equal area = 35 cm² because both base AB and parallel height h = 7 cm match",
                    "The symmetric triangle has larger area than slanted triangles",
                    "The widest slanted triangle has largest area because its side edges are longest",
                    "Areas depend on angles at A and B"
                ],
                "answer": 0,
                "hint": "Remember parallel lines keep constant perpendicular distance h everywhere between them!",
                "explanation": "Common base AB = 10 cm and constant perpendicular distance h = 7 cm between parallel tracks give equal Area = 1/2 × 10 × 7 = 35 cm²."
            },
            {
                "question": "Among all equal-area triangles sharing common base AB on line l with apex P gliding along parallel line m, which placement of P gives the STRICT MINIMUM PERIMETER (shortest sum AP + PB)?",
                "options": [
                    "Directly equidistant above the perpendicular bisector of AB where AP = BP (proved by reflecting B across line m into straight line AB')",
                    "Shifting P infinitely far to the right along line m",
                    "Placing P directly vertically above A (right triangle)",
                    "All triangles between parallels share identical perimeter too"
                ],
                "answer": 0,
                "hint": "Reflect B across mirror line m to B' and connect A to B' with a straight segment!",
                "explanation": "Reflecting B across parallel line m yields shortest straight path AP* + P*B' when P* lies vertically above the midpoint of AB, making ΔAP*B isosceles."
            }
        ]
    }
]

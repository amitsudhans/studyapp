#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 14: Area
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 14 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Polygon Triangulation Method",
        "subtitle": "Area of Any Polygon: Decomposing Complex Quadrilaterals, Pentagons & Irregular Plots into Triangles via Diagonals",
        "speech": (
            "Now solve a seemingly daunting geometric challenge in Area of Any Polygon: how can anyone measure the exact AREA OF ANY IRREGULAR POLYGON—whether a slanted quadrilateral, five-sided pentagon, six-sided hexagon, or multi-cornered farmland survey plot?! Rely on the universal geometric divide-and-conquer tool called TRIANGULATION! "
            "Draw non-intersecting straight diagonals cleanly from ONE single chosen corner vertex A straight across the interior of an n-sided convex polygon to all other non-adjacent vertices! Watch a four-sided quadrilateral split cleanly into TWO crisp triangles! Watch a five-sided pentagon split neatly into THREE non-overlapping triangles! Watch a hexagon yield FOUR triangles! In general, EVERY convex n-sided polygon decomposes completely into (n − 2) crisp triangles! "
            "Once broken down cleanly into elementary triangles, land surveyors measure each triangle's base along the diagonal chord and drop perpendicular offset heights straight from each remaining outer corner onto that central interior diagonal! Summing every component triangle area—1/2 × d × h₁ + 1/2 × d × h₂ + ...—instantly recovers the exact total polygon area! Notice a classic quadrilateral result: for diagonal AC of length d and perpendicular offsets h₁, h₂ from corners B and D, Quadrilateral Area = 1/2 × d × (h₁ + h₂)!"
        ),
        "checkpoints": [
            {
                "question": "A diagonal AC of an irregular quadrilateral ABCD measures 18 cm. The perpendicular offsets dropped onto AC from opposite vertices B and D measure 5 cm and 7 cm. Find the exact area of quadrilateral ABCD:",
                "options": [
                    "108 cm²   (1/2 × 18 × (5 + 7) = 9 × 12 = 108 cm²)",
                    "216 cm²",
                    "90 cm²",
                    "126 cm²"
                ],
                "answer": 0,
                "hint": "Split into ΔABC (area 1/2 × 18 × 5) + ΔADC (area 1/2 × 18 × 7), or use 1/2 × d × (h₁ + h₂)!",
                "explanation": "Area = 1/2(18)(5) + 1/2(18)(7) = 45 + 63 = 108 cm²."
            },
            {
                "question": "By drawing non-overlapping diagonals from a single vertex, into how many component triangles does ANY 6-sided convex polygon (hexagon) decompose?",
                "options": [
                    "4 triangles   (following the universal n − 2 rule)",
                    "6 triangles",
                    "3 triangles",
                    "5 triangles"
                ],
                "answer": 0,
                "hint": "Recall n = 6 sides gives (n − 2) triangles from one vertex!",
                "explanation": "Any n-sided convex polygon triangulates from one vertex into n − 2 = 6 − 2 = 4 triangles."
            }
        ]
    },
    {
        "id": 10,
        "title": "Parallelogram Cut Shift",
        "subtitle": "Parallelogram Dissection Method: Transforming into an Equivalent Rectangle via Perpendicular Cut & RHS Congruence",
        "speech": (
            "Enter the Parallelogram section and transform a slanted parallelogram into an upright, axis-aligned rectangle using clean scissor dissection! Consider parallelogram ABCD resting squarely on horizontal bottom base AB with slanted side edges AD and BC! Drop a dashed perpendicular line segment DE straight from top-left vertex D down at a crisp 90° angle onto bottom base AB, defining perpendicular height h = DE! "
            "Now imagine slicing right triangle ΔAED cleanly off the left corner along vertical cut DE and sliding that exact triangular paper wedge straight rightward across to the opposite slanted edge BC! Check carefully whether slanted side AD locks seamlessly onto parallel opposite edge BC: because opposite sides of every parallelogram match identically, edge AD EQUALS edge BC and remains strictly parallel to BC! Now extend bottom base AB slightly rightward to point F and drop vertical perpendicular CF of identical height h! "
            "Compare left cut wedge ΔAED with right extension triangle ΔBFC: ∠AED = ∠BFC = 90° (Right angle), slanted hypotenuse AD = BC (Hypotenuse), and perpendicular vertical height DE = CF = h (Side)! By RHS CONGRUENCE, ΔAED ≅ ΔBFC identically—reassembling both pieces seamlessly into exact upright rectangle EFCD of identical base b and height h!"
        ),
        "checkpoints": [
            {
                "question": "In the dissection transforming parallelogram ABCD (height DE = CF) into rectangle EFCD by sliding left cut-piece ΔAED to the right edge BC, which triangle congruence criterion proves ΔAED ≅ ΔBFC?",
                "options": [
                    "RHS Congruence   (∠AED = ∠BFC = 90°, Hypotenuse AD = BC, Side DE = CF)",
                    "AAA Similarity only",
                    "SSA Non-congruence",
                    "Only valid when ABCD is a square"
                ],
                "answer": 0,
                "hint": "Inspect the 90° right angles, equal opposite sides AD = BC (hypotenuses), and equal perpendicular heights DE = CF!",
                "explanation": "Right angles (90°), equal hypotenuses (AD = BC), and equal altitude sides (DE = CF) guarantee ΔAED ≅ ΔBFC by RHS congruence."
            },
            {
                "question": "What happens to the PERIMETER vs the AREA when parallelogram ABCD (base 10 cm, slant side 6 cm, height 4 cm) is sheared/dissected into a 10 cm × 4 cm rectangle?",
                "options": [
                    "Area stays strictly conserved (40 cm²), while Perimeter DECREASES from 32 cm (parallelogram) to 28 cm (rectangle)",
                    "Both Area and Perimeter remain completely unchanged",
                    "Area increases while Perimeter stays 32 cm",
                    "Area becomes 60 cm²"
                ],
                "answer": 0,
                "hint": "Compare 2(10 + 6) vs 2(10 + 4) for perimeter, while checking 10 × 4 for area!",
                "explanation": "Dissection preserves exact interior Area = 10 × 4 = 40 cm², whereas shorter perpendicular height edges (4 cm < 6 cm) shrink perimeter from 32 cm to 28 cm."
            }
        ]
    },
    {
        "id": 11,
        "title": "Parallelogram Base Height",
        "subtitle": "Parallelogram Area Formula: Area = Base × Perpendicular Height Using Any Pair of Opposite Parallel Sides",
        "speech": (
            "Having cleanly dissected parallelogram ABCD into exact equivalent rectangle EFCD, state the grand law immediately: AREA OF A PARALLELOGRAM equals BASE × HEIGHT (A = b × h)! Guard carefully against the number-one geometry mistake right here: NEVER multiply the two adjacent edge lengths together! Inside a slanted parallelogram with bottom base 12 cm, slant side 8 cm, and vertical height 5 cm, area equals 12 × 5 = 60 cm², NOT 12 × 8 = 96 cm²! Why? Because pushing a hinged parallelogram flatter lowers its vertical height h while keeping all four edge lengths fixed, strictly shrinking enclosed interior space! "
            "Now inspect a crucial second property: ANY side edge of a parallelogram may act as the chosen BASE, provided you always multiply by its OWN corresponding PERPENDICULAR HEIGHT (the 90° distance separating that chosen base from its opposite parallel edge)! "
            "Test dual heights cleanly on parallelogram PQRS: suppose longer base PQ = 15 cm carries perpendicular altitude ST = 8 cm → Area = 15 × 8 = 120 cm²! When shorter side QR measures 10 cm, its taller matching altitude SU satisfies 10 × SU = 120 → SU = 12 cm cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A parallelogram has adjacent sides measuring 14 cm and 7 cm. The perpendicular distance (height) between the pair of 14 cm sides is 5 cm. Find its exact area AND the perpendicular height between the pair of 7 cm sides:",
                "options": [
                    "Area = 70 cm²; height on 7 cm base = 10 cm",
                    "Area = 98 cm²; height on 7 cm base = 14 cm",
                    "Area = 35 cm²; height on 7 cm base = 5 cm",
                    "Area = 70 cm²; height on 7 cm base = 5 cm"
                ],
                "answer": 0,
                "hint": "First compute Area = 14 × 5 = 70 cm², then solve 7 × h₂ = 70!",
                "explanation": "Area = base₁ × h₁ = 14 × 5 = 70 cm². Using the 7 cm side as base gives 7 × h₂ = 70 → h₂ = 10 cm."
            },
            {
                "question": "Why does folding or pushing a flexible 4-bar hinged rectangle (10 cm × 6 cm) into a flatter parallelogram with identical side lengths strictly DECREASE its enclosed area?",
                "options": [
                    "Because perpendicular height h between parallel sides drops strictly below 6 cm as the frame tilts",
                    "Because base length shrinks below 10 cm",
                    "Because perimeter increases",
                    "Actually area stays 60 cm² regardless of tilt angle"
                ],
                "answer": 0,
                "hint": "Observe what happens to the vertical height of the top bar above the table as the hinged side leans closer to horizontal!",
                "explanation": "Area = base × height. While edge length remains 6 cm, the perpendicular height h = 6 sin(θ) drops below 6 cm, reducing enclosed area."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rhombus Orthogonal Diagonals",
        "subtitle": "Rhombus Dissection & Formula: Using Perpendicular Bisecting Diagonals to Prove Area = 1/2 × d₁ × d₂",
        "speech": (
            "Now unlock the diamond-shaped RHOMBUS using diagonal dissection! Recall two essential geometric facts governing EVERY rhombus PQRS: First, every rhombus is automatically a special equilateral parallelogram (with all four sides identical), so base × perpendicular height STILL applies cleanly whenever side edge and perpendicular altitude are provided! Second, its two interior diagonals PR = d₁ and QS = d₂ act as exact PERPENDICULAR BISECTORS of each other—crossing squarely at a crisp 90° right angle right at center intersection O! "
            "Use that exact 90° orthogonal diagonal crossing in TWO brilliant ways to prove Rhombus Area = 1/2 × d₁ × d₂! Method One—TWO TRIANGLES: diagonal PR (length d₁) splits rhombus PQRS cleanly into upper triangle ΔPQR and lower triangle ΔPSR! Because second diagonal QS (length d₂) meets PR at 90° and bisects evenly at O, BOTH triangles share common base d₁ and exact perpendicular altitude d₂/2! Sum both triangles right now: 1/2(d₁)(d₂/2) + 1/2(d₁)(d₂/2) = 1/2 × d₁ × d₂! "
            "Method Two—BOUNDING RECTANGLE: enclose all four rhombus corners inside a neat rectangle of sides d₁ and d₂! The outer rectangle covers d₁ × d₂—twice each of the four inner right triangles—proving Area = 1/2 × d₁ × d₂!"
        ),
        "checkpoints": [
            {
                "question": "A rhombus-shaped kite floor tile has diagonals measuring d₁ = 24 cm and d₂ = 14 cm. Find its exact surface area:",
                "options": [
                    "168 cm²   (1/2 × 24 × 14)",
                    "336 cm²",
                    "76 cm²",
                    "196 cm²"
                ],
                "answer": 0,
                "hint": "Apply the rhombus diagonal formula Area = 1/2 × d₁ × d₂!",
                "explanation": "Area = 1/2 × 24 × 14 = 12 × 14 = 168 cm²."
            },
            {
                "question": "A rhombus has total area 96 cm² and one diagonal measuring d₁ = 16 cm. What is the exact length of its second diagonal d₂, AND what is each side length of the rhombus?",
                "options": [
                    "d₂ = 12 cm; each side = 10 cm   (half-diagonals 8 cm and 6 cm form a 6-8-10 right triangle!)",
                    "d₂ = 6 cm; each side = 10 cm",
                    "d₂ = 12 cm; each side = 14 cm",
                    "d₂ = 24 cm; each side = 20 cm"
                ],
                "answer": 0,
                "hint": "First solve 1/2 × 16 × d₂ = 96 for d₂, then apply Baudhāyana-Pythagoras on half-diagonals d₁/2 and d₂/2!",
                "explanation": "8 × d₂ = 96 gives d₂ = 12 cm. Half-diagonals 8 cm and 6 cm meet at 90°, giving side √(8² + 6²) = √100 = 10 cm."
            }
        ]
    },
    {
        "id": 13,
        "title": "Trapezium Splitting Method",
        "subtitle": "Trapezium Dissection Derivation: Computing Area by Splitting into Rectangles & Triangles (or Diagonal Triangles)",
        "speech": (
            "Step forward to the TRAPEZIUM—a quadrilateral featuring ONE pair of parallel opposite sides labeled top length a and bottom length b, separated cleanly by constant perpendicular distance height h! How can we compute any trapezium's area using only geometric tools already proved—rectangles and triangles? Watch TWO rock-solid decomposition strategies! "
            "Strategy One—PERPENDICULAR DROP DISSECTION! Drop two dashed vertical perpendicular heights straight down from upper corners D and C onto bottom base AB at feet E and F! Notice the interior divides cleanly into ONE central upright rectangle of width a and height h (Area = a × h), PLUS two side right-angled triangular wings of bases x and y and shared height h (wing areas = 1/2 xh and 1/2 yh)! Sum all three component pieces right now: ah + 1/2(x + y)h! Notice top width plus both wing bases (a + x + y) equals full bottom base b, meaning x + y = b − a! Simplify algebraically: ah + 1/2(b − a)h = 1/2 h(a + b)! "
            "Strategy Two—DIAGONAL TRIANGULATION! Drawing one interior diagonal cuts the trapezium into TWO triangles sharing exact height h with parallel bases a and b: 1/2 ah + 1/2 bh = 1/2 h(a + b)!"
        ),
        "checkpoints": [
            {
                "question": "A trapezium has parallel sides 12 cm (top) and 20 cm (bottom), with perpendicular height 7 cm. Split it vertically into a central 12 × 7 cm rectangle plus flanking right triangles totaling base 8 cm. What is its total area?",
                "options": [
                    "112 cm²   (Central rectangle 84 cm² + Flanking wings 28 cm² = 112 cm²)",
                    "140 cm²",
                    "84 cm²",
                    "224 cm²"
                ],
                "answer": 0,
                "hint": "Rectangle = 12 × 7 = 84 cm²; combined flanking wings = 1/2 × (20 − 12) × 7 = 28 cm²!",
                "explanation": "84 + 1/2(8)(7) = 84 + 28 = 112 cm², matching 1/2 × 7 × (12 + 20) = 112 cm²."
            },
            {
                "question": "Drawing single diagonal AC inside trapezium ABCD (parallel bases AB = b and CD = a, perpendicular height h) cuts it into ΔABC and ΔACD. What are their individual areas?",
                "options": [
                    "Area(ΔABC) = 1/2 bh and Area(ΔACD) = 1/2 ah, summing cleanly to 1/2 h(a + b)",
                    "Both triangles ALWAYS have identical area 1/2 ah",
                    "Area(ΔABC) = bh and Area(ΔACD) = ah",
                    "Cannot be computed without knowing slanted legs AD and BC"
                ],
                "answer": 0,
                "hint": "Observe that parallel bases AB and CD are separated by the exact same perpendicular distance h for both triangles!",
                "explanation": "ΔABC has base b and height h (1/2 bh), while upside-down ΔACD has base a and identical height h (1/2 ah), totaling 1/2 h(a + b)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Trapezium Double Copy",
        "subtitle": "Trapezium Formula Proof: Rotating a Congruent Copy to Form a Parallelogram Proving Area = 1/2 × h × (a + b)",
        "speech": (
            "Now inspect geometry's cleanest visual proof of the Trapezium Area Law: THE CONGRUENT TWO-COPY PARALLELOGRAM METHOD! Take ANY general trapezium having parallel top side a, parallel bottom base b, and perpendicular height h! Now cut out an IDENTICAL congruent paper clone copy of that exact same trapezium right beside the original shape! "
            "Rotate the second congruent copy upside down by 180 degrees around one slanted midpoint and slide its slanted non-parallel edge neatly up against the matching slanted edge of the original trapezium! Watch what snaps together seamlessly without any gaps or overlaps: original bottom base b aligns straight alongside inverted top edge a along the bottom border—creating exact total bottom base (b + a)! Original top edge a aligns straight alongside inverted bottom edge b along the top border—creating identical total top base (a + b)! Because opposite boundaries remain strictly equal and parallel, both congruent copies fuse smoothly into ONE GIANT PARALLELOGRAM of base (a + b) and height h! "
            "Compute that giant parallelogram's area immediately: Base × Height = (a + b) × h! Since TWO identical trapeziums built that complete parallelogram, ONE single trapezium covers EXACTLY HALF: Area of Trapezium = 1/2 × height × (sum of parallel sides)!"
        ),
        "checkpoints": [
            {
                "question": "A canal cross-section is shaped like a trapezium with top width 18 m, bottom floor width 10 m, and vertical depth 6 m. Applying 1/2 × h × (a + b), find its exact cross-sectional area:",
                "options": [
                    "84 m²   (1/2 × 6 × (18 + 10) = 3 × 28)",
                    "168 m²",
                    "108 m²",
                    "54 m²"
                ],
                "answer": 0,
                "hint": "Add the two parallel widths (18 + 10 = 28), multiply by height 6, and divide by 2!",
                "explanation": "Area = 1/2 × 6 × (18 + 10) = 3 × 28 = 84 m²."
            },
            {
                "question": "A trapezium has total area 95 cm², perpendicular height 10 cm, and one parallel side measuring 7 cm. Find the exact length of its second parallel side:",
                "options": [
                    "12 cm   (1/2 × 10 × (7 + b) = 95 → 5(7 + b) = 95 → 7 + b = 19)",
                    "19 cm",
                    "9.5 cm",
                    "14 cm"
                ],
                "answer": 0,
                "hint": "Solve 5 × (7 + b) = 95 step by step!",
                "explanation": "1/2 × 10 × (7 + b) = 95 simplifies to 5(7 + b) = 95 → 7 + b = 19 → b = 12 cm."
            }
        ]
    },
    {
        "id": 15,
        "title": "Practical Local Units",
        "subtitle": "Areas in Real Life: Metric & Imperial Units (cm², m², ft², km², acres, 1 in = 2.54 cm) & Indian Land Units",
        "speech": (
            "Now bridge classroom geometry formulas directly into REAL-LIFE AREA MEASUREMENTS AND UNITS! Choosing sensible units keeps practical numbers clean and manageable: measure postage stamps, A4 paper sheets, or mobile screens in square centimeters (cm²); measure classroom floors, tabletops, and carpets in square meters (m²) or square feet (ft²); and measure entire cities, lakes, and agricultural districts in square kilometers (km²) or acres! "
            "Watch UNIT CONVERSIONS carefully—NEVER convert areas using a single 1D factor! Because 1 meter = 100 cm, ONE square meter equals 100 cm × 100 cm = 10,000 cm²! Similarly, using exact international standard 1 inch = 2.54 centimeters, ONE square inch equals 2.54 × 2.54 ≈ 6.45 cm², while 1 square foot (12 in × 12 in = 144 in²) equals roughly 929 cm² (or 0.0929 m²)! And 1 hectare = 100 m × 100 m = 10,000 m² (about 2.47 acres), whereas 1 km² = 100 hectares! "
            "Across rural and urban India, land deeds also preserve traditional LOCAL UNITS rich in regional heritage: learn key terms such as GAJ (square yard, ~0.836 m²), CENT (~435.6 ft², popular in South India), ANKANAM (Andhra/Karnataka), and BIGHA divided into KATHA and DHUR across North and East India!"
        ),
        "checkpoints": [
            {
                "question": "A rectangular study mat measures 2 meters long by 1.5 meters wide. Using 1 m² = 10,000 cm², what is its exact area in BOTH m² and cm²?",
                "options": [
                    "3 m² = 30,000 cm²",
                    "3 m² = 300 cm²",
                    "3 m² = 3,000 cm²",
                    "30 m² = 300,000 cm²"
                ],
                "answer": 0,
                "hint": "Remember area conversion multiplies length scale twice: 100 cm × 100 cm = 10,000 cm² per m²!",
                "explanation": "Area = 2 × 1.5 = 3 m². Since 1 m² = 100 × 100 = 10,000 cm², 3 m² = 30,000 cm²."
            },
            {
                "question": "Given 1 inch = 2.54 cm exactly, what is the approximate area in cm² of a square tile measuring 1 inch × 1 inch (1 sq in)?",
                "options": [
                    "2.54 × 2.54 ≈ 6.45 cm²",
                    "2.54 cm²",
                    "5.08 cm²",
                    "25.4 cm²"
                ],
                "answer": 0,
                "hint": "Square BOTH sides of 1 in = 2.54 cm!",
                "explanation": "1 in² = (2.54 cm) × (2.54 cm) = 6.4516 cm² ≈ 6.45 cm²."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Area Summary",
        "subtitle": "Summary Consolidation: Core Area Laws for Triangles, Polygons, Parallelograms, Rhombuses, Trapeziums & Conversions",
        "speech": (
            "Step back cleanly right now to synthesize the complete architecture of Chapter Fourteen: AREA! Notice how EVERY polygon area law unfolds logically step by step from ONE single foundational building block—packing identical non-overlapping unit squares inside a RECTANGLE (Area = length × width)! "
            "First, PERIMETER VERSUS AREA: identical boundary perimeters can enclose wildly different interior areas (such as 6 × 6 vs 11 × 1), and carving inward notches shrinks area while increasing total perimeter! "
            "Second, TRIANGLES AND OPTIMIZATION: enclosing acute, right, and obtuse triangles inside bounding rectangles proves universally that Area = 1/2 × base × height! This immediately unlocks unknown altitudes (b₁h₁ = b₂h₂), equal-area median bisection, constant-area shearing between parallel lines, and minimum-perimeter triangles proved via mirror reflection! "
            "Third, QUADRILATERALS AND POLYGONS: triangulating any convex n-gon creates (n − 2) triangles! Dissecting an RHS-congruent wedge converts parallelograms into rectangles (b × h)! Crossing perpendicular diagonals prove Rhombus Area = 1/2 × d₁ × d₂! Splitting or doubling a congruent copy proves Trapezium Area = 1/2 × h × (a + b)! "
            "Fourth, REAL-LIFE UNITS: convert cm², m², ft², in² (1 in = 2.54 cm), km², and acres confidently alongside traditional Indian units—bigha, gaj, katha, dhur, cent, and ankanam!"
        ),
        "checkpoints": [
            {
                "question": "Which summary table correctly collects the exact area formulas across four quadrilaterals & triangles from Chapter 14?",
                "options": [
                    "Triangle = 1/2 bh; Parallelogram = bh; Rhombus = 1/2 d₁d₂; Trapezium = 1/2 h(a + b)",
                    "Triangle = bh; Parallelogram = 1/2 bh; Rhombus = d₁d₂; Trapezium = h(a + b)",
                    "Triangle = 1/2(b + h); Parallelogram = 2(b + h); Rhombus = 4s; Trapezium = a × b × h",
                    "Triangle = 1/2 d₁d₂; Parallelogram = 1/2 bh; Rhombus = 1/2 h(a + b)"
                ],
                "answer": 0,
                "hint": "Check every coefficient cleanly (especially which formulas carry factor 1/2 vs base × height)!",
                "explanation": "Option 1 states every core geometric area formula accurately."
            },
            {
                "question": "Which geometric derivation method converts BOTH parallelograms and trapeziums visually into easier known shapes?",
                "options": [
                    "Perpendicular height dissection / congruent copy rearrangement preserving enclosed two-dimensional area",
                    "Equating perimeter to area",
                    "Measuring diagonal length alone without perpendicular height",
                    "Multiplying slant sides together"
                ],
                "answer": 0,
                "hint": "Recall sliding ΔAED onto ΔBFC for parallelograms and rotating a second copy for trapeziums!",
                "explanation": "Area-preserving dissection and congruent duplication transform parallelograms into rectangles and double trapeziums into parallelograms."
            }
        ]
    }
]

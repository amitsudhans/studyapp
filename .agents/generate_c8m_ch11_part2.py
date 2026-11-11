#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 11: Exploring Some Geometric Themes
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 11 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Cylinder Cone Polyhedra",
        "subtitle": "Section 4.2 Specific Nets: Cuboid, Square Pyramid, Cylinder, Cone Sector, Octahedron (11) & Dodecahedron (43,380)",
        "speech": (
            "Explore the rich family of 3D solid nets highlighted in Section Four Point Two! First: CUBOID AND SQUARE PYRAMID! A brick cuboid unfolds into 6 rectangles arranged as three matching opposite pairs, while a square pyramid unfolds neatly into 1 central square surrounded by 4 pointing isosceles triangles (resembling a four-pointed star)! "
            "Second: CURVED SOLIDS—CYLINDER AND CONE! Unroll the curved label around a soup tin cylinder and what flat geometry appears? One smooth RECTANGLE whose width matches the exact circular circumference 2πr, flanked cleanly by 2 equal circular lids attached on top and bottom! Unwrap a pointed party CONE instead, and its curved lateral surface opens into a curved CIRCULAR SECTOR (pie slice whose arc length equals base circumference 2πr) paired with 1 single circular base! "
            "Third: REGULAR POLYHEDRA NET COMBINATORIAL COMPLEXITY EXPLOSION! Just like a regular cube's 6 square faces yield 11 distinct valid nets, a regular diamond-shaped OCTAHEDRON (built symmetrically from 8 congruent equilateral triangular faces meeting four per vertex) ALSO unfolds neatly into exactly 11 unique distinct nets! Step upward to a 12-pentagon regular DODECAHEDRON, and geometric folding combinatorics suddenly explodes dramatically into an astonishing mathematical total of 43,380 distinct valid flat nets!"
        ),
        "checkpoints": [
            {
                "question": "Which two 2D flat shapes combine to form the net of a closed solid CONE versus a closed solid CYLINDER?",
                "options": [
                    "Cone: 1 circular sector + 1 circle; Cylinder: 1 rectangle + 2 congruent circles",
                    "Cone: 1 triangle + 1 circle; Cylinder: 2 squares + 1 triangle",
                    "Cone: 4 triangles + 1 square; Cylinder: 6 rectangles",
                    "Cone: 2 circles + 1 rectangle; Cylinder: 1 sector + 1 circle"
                ],
                "answer": 0,
                "hint": "Unwrap a paper party hat (cone) vs unrolling a soup-can label (cylinder)!",
                "explanation": "A cylinder unrolls to 1 rectangle plus 2 circular ends; a cone unwraps to 1 circular sector plus 1 circular base."
            },
            {
                "question": "How many distinct valid nets exist for a regular Octahedron (8 triangular faces) versus a regular Dodecahedron (12 pentagonal faces)?",
                "options": [
                    "Octahedron: 11 nets; Regular Dodecahedron: 43,380 nets",
                    "Octahedron: 2 nets; Regular Dodecahedron: 11 nets",
                    "Octahedron: 8 nets; Regular Dodecahedron: 12 nets",
                    "Octahedron: 11 nets; Regular Dodecahedron: 120 nets"
                ],
                "answer": 0,
                "hint": "Octahedron matches the cube (11 nets!), while the 12-faced dodecahedron leaps to 43,380!",
                "explanation": "Dual symmetry links the 6-face cube and 8-face octahedron at 11 nets each, whereas a regular dodecahedron has 43,380 nets."
            }
        ]
    },
    {
        "id": 10,
        "title": "Shortest Cube Paths",
        "subtitle": "Section 4.2 Shortest Surface Paths on a Cube/Cuboid: Net Unfolding & Baudhāyana-Pythagoras Geodesics",
        "speech": (
            "Discover one of Chapter Eleven's cleverest bridges linking 3D nets directly back to Chapter Nine's Baudhāyana-Pythagoras Theorem! Imagine an ant standing on the outer corner of a cardboard cube or cuboid box of candy, itching to crawl strictly ALONG THE OUTER SURFACE to reach a sweet laddu sitting on the opposite corner! Remember: the ant cannot bore straight through empty air inside the box—it MUST walk across flat solid faces! "
            "Why do surface paths look curved or zigzagged across 3D edges? Because our eyes stay trapped in 3D space! Unfold those adjacent faces cleanly flat onto a 2D NET! Instant magic: the shortest distance between two points on ANY flat plane is a single STRAIGHT LINE SEGMENT! "
            "Test a unit cube of side s = 1 unit: unfold front and top square faces cleanly flat side by side into a 2 × 1 rectangle! The straight diagonal corner-to-corner hypotenuse has perpendicular legs 2 and 1 → shortest surface path = √(2² + 1²) = √5 units (beating edge-crawling length 3)! On an unequal cuboid (L, W, H), test all three pairs of unfolded faces and pick whichever yields the MINIMUM √((s₁ + s₂)² + M²)!"
        ),
        "checkpoints": [
            {
                "question": "An ant on a 1 m × 1 m × 1 m cube crawls strictly along the outer surface from a bottom-front-left corner to the opposite top-back-right corner. Unfolding two adjacent faces into a 2 m × 1 m rectangle gives what shortest surface distance?",
                "options": [
                    "√5 m ≈ 2.24 m   (much shorter than crawling 1+1+1 = 3 m along edges!)",
                    "3 m",
                    "√2 m ≈ 1.41 m",
                    "2 m"
                ],
                "answer": 0,
                "hint": "Form a right triangle on the flat 2 × 1 unfolded rectangle and apply √(2² + 1²)!",
                "explanation": "Unfolding 2 adjacent unit faces creates a 2 × 1 rectangle; the straight hypotenuse equals √(2² + 1²) = √5 m."
            },
            {
                "question": "For an unequal cuboid room (Length 4 m, Width 3 m, Height 2 m), an ant crawls from bottom-front-left corner to top-back-right corner across two walls. Which unfolded leg pairing minimizes √((a + b)² + c²)?",
                "options": [
                    "Pair the two SMALLER dimensions together: √((2 + 3)² + 4²) = √(25 + 16) = √41 m",
                    "Pair the two LARGER dimensions: √((4 + 3)² + 2²) = √53 m",
                    "Follow 3 edges directly: 4 + 3 + 2 = 9 m",
                    "Use √(4² + 2²) = √20 m"
                ],
                "answer": 0,
                "hint": "Compare (2+3)² + 4² = 41 vs (4+2)² + 3² = 45 vs (4+3)² + 2² = 53!",
                "explanation": "Keeping the longest edge (4) separate and summing the two shorter edges (2 + 3 = 5) minimizes the squared sum at 41."
            }
        ]
    },
    {
        "id": 11,
        "title": "Orthographic Plane Projections",
        "subtitle": "Section 4.2 Representation on a Plane: Perpendicular Orthographic Projections (Front, Top & Side Views)",
        "speech": (
            "Engineers, architects, and industrial designers need flat paper blueprints that reveal exact true lengths of 3D machines without perspective distortion! Enter ORTHOGRAPHIC PROJECTIONS in Section Four Point Two! Imagine dropping perpendicular rays straight down from every point, edge, and corner of a 3D object onto a flat glass sheet—that perpendicular footprint is an ORTHOGRAPHIC PROJECTION! "
            "Notice how a tilted 3D rod looks shorter when slanted against a projection plane yet reveals full true length whenever held parallel to the plane! To capture every hidden recess, step, and overhang of a complex 3D block stack cleanly, designers project the solid onto THREE MUTUALLY PERPENDICULAR PLANES simultaneously! "
            "Memorize all three crisp engineering blueprint views cleanly: First, look straight horizontally from directly in front onto the VERTICAL PLANE to capture the FRONT VIEW (showing true height and left-to-right width)! Second, look straight vertically downward from high overhead onto the HORIZONTAL PLANE to capture the TOP VIEW (architectural plan view, showing true left-to-right width and front-to-back depth)! Third, look straight horizontally from left or right onto the SIDE PLANE to capture the SIDE VIEW (showing true height and depth)! Together, three mutually aligned views define any complex 3D object completely!"
        ),
        "checkpoints": [
            {
                "question": "Which three mutually perpendicular projection views completely specify a 3D solid on flat engineering blueprints?",
                "options": [
                    "Front View (Vertical Plane), Top View (Horizontal Plane), and Side View (Side Plane)",
                    "Shadow View, Isometric View, and Fractal View",
                    "Front View, Corner View, and Diagonal Net",
                    "Inside View, Back View, and Curved View"
                ],
                "answer": 0,
                "hint": "Think of standing in front, hovering overhead, and looking from the side at 90° angles!",
                "explanation": "Orthographic engineering blueprints align Front (Vertical Plane), Top (Horizontal Plane), and Side (Side Plane) views."
            },
            {
                "question": "Looking straight down at the TOP VIEW of an upright regular square pyramid, what 2D diagram appears?",
                "options": [
                    "A square with two crossing diagonals meeting at the center apex point",
                    "A single plain triangle",
                    "A circle with one center dot",
                    "A 3-column staircase"
                ],
                "answer": 0,
                "hint": "Looking vertically down from above, you see the square outer rim PLUS all 4 slanted edges converging to the center apex!",
                "explanation": "From directly above, the square base outlines the shape and the 4 triangular edges project onto the diagonals meeting at center."
            }
        ]
    },
    {
        "id": 12,
        "title": "Light And Shadows",
        "subtitle": "Section 4.2 Shadows: Connecting Orthographic Projections to Perpendicular Beams vs Distant Sunlight",
        "speech": (
            "Spot the gorgeous real-world physics connection inside Section Four Point Two: SHADOWS are nature's own instant geometric projections! Hold a wooden cylinder, cone, or stacked cube model between a glowing light source and a flat classroom wall! Watch closely how two completely different light geometries shape the dark shadow outline cast onto the wall! "
            "Case One: DISTANT PARALLEL SUNLIGHT! Because our Sun lies roughly 150 million kilometres away, solar rays arrive nearly perfectly parallel to one another! When sunlight strikes an object straight-on perpendicular to a flat wall, the dark shadow silhouette matches the solid's EXACT ORTHOGRAPHIC PROJECTION at 1 : 1 true width and height! "
            "Case Two: CLOSE POINT LAMP OR TORCHLIGHT! When a classroom flashlight shines from close range, light rays spread outward inside a widening bright cone (central divergence)! Hold your hand or wooden cube closer toward the glowing torch bulb, and its dark flat wall shadow balloons dramatically LARGER than true object size, stretching and warping geometric angles whenever tilted! Compare long morning and evening shadows versus short overhead noon shadows, and test how tilting a flat circular coin smoothly turns its shadow from a circle into an ellipse or thin straight line!"
        ),
        "checkpoints": [
            {
                "question": "Why does distant sunlight falling perpendicular onto a wall produce a shadow matching a 3D object's true orthographic projection size?",
                "options": [
                    "Because sunlight arrives in nearly parallel rays, matching perpendicular orthographic projection geometry",
                    "Because sunlight shrinks every solid by half",
                    "Because nearby bulbs make smaller parallel shadows",
                    "Because shadows ignore viewing angles"
                ],
                "answer": 0,
                "hint": "Compare parallel rays from 150 million km away against diverging rays from a close flashlight!",
                "explanation": "Distant solar rays are effectively parallel, creating an unmagnified orthographic silhouette on a perpendicular screen."
            },
            {
                "question": "If you hold a flat circular coin directly parallel to a screen under perpendicular parallel sunlight, then slowly rotate the coin edge-on by 90°, how does its flat shadow evolve?",
                "options": [
                    "Circle → narrowing Oval/Ellipse → thin straight Line segment",
                    "Circle → Triangle → Square",
                    "Square → Circle → Hexagon",
                    "Always stays an identical Circle"
                ],
                "answer": 0,
                "hint": "Watch a round dinner plate tilt until you only view its thin flat rim!",
                "explanation": "Tilting a circle narrows its projected width continuously from a full circle through ellipses down to a line segment."
            }
        ]
    },
    {
        "id": 13,
        "title": "Isometric Equal Measure",
        "subtitle": "Section 4.2 Isometric Projections: 'Equal Measure' Principle & Cube Corner Balanced into Regular Hexagon",
        "speech": (
            "Orthographic views separate Front, Top, and Side onto three flat panels—what if an artist wants ONE single 3D picture showing all three dimensions simultaneously WITHOUT distorted lengths? Enter ISOMETRIC PROJECTION in Section Four Point Two! Look at its crisp Greek roots: 'iso' means EQUAL and 'metric' means MEASURE—ISOMETRIC literally means EQUAL MEASURE! "
            "Why call it equal measure? Tilt a standard solid wooden cube cleanly forward and diagonally so your eyes stare STRAIGHT DOWN its longest internal body space diagonal while one bottom corner vertex touches your flat wooden desk symmetrically! Look closely at all three visible perpendicular edges meeting cleanly at the front central corner—vertical height edge, left depth edge, and right length edge! Because all three mutually perpendicular 3D axes tilt at the EXACT SAME elevation angle toward your flat plane of view, EVERY SINGLE CUBE EDGE projects cleanly at the IDENTICAL SCALE RATIO, separated evenly around the center by symmetric 120-degree corner angles! "
            "Behold the stunning geometric visual surprise highlighted in NCERT: when viewed straight down its body diagonal, the outer silhouette boundary of ANY solid 3D isometric cube forms a completely symmetric REGULAR SIX-SIDED HEXAGON tiled cleanly into three identical diamond-shaped rhombi!"
        ),
        "checkpoints": [
            {
                "question": "What does the mathematical term 'isometric' literally translate to, and what angles separate the three principal 3D axes at the front corner of an isometric cube?",
                "options": [
                    "'Equal measure'; the three axes separate symmetrically at equal 120° angles",
                    "'Three shadows'; separated at 90° and 45°",
                    "'Half depth'; separated at 180°",
                    "'Infinite zoom'; separated at 60°"
                ],
                "answer": 0,
                "hint": "Iso = equal, metric = measure; three equal slices around a full 360° corner = 360° ÷ 3!",
                "explanation": "Isometric means 'equal measure', scaling height, length, and depth equally along three 120°-spaced axes."
            },
            {
                "question": "When a regular cube is balanced diagonally on one corner in a true isometric view, what regular 2D polygon forms its outer perimeter silhouette?",
                "options": [
                    "A regular 6-sided HEXAGON (made of 3 visible rhombus faces)",
                    "A plain 4-sided square",
                    "An equilateral triangle",
                    "A regular octagon"
                ],
                "answer": 0,
                "hint": "Count the 6 outer boundary edges visible around the 3 diamond faces of the cube!",
                "explanation": "Looking along a cube's space diagonal projects the 6 outer edges into a perfectly symmetric regular hexagon."
            }
        ]
    },
    {
        "id": 14,
        "title": "Isometric Block Grids",
        "subtitle": "Section 4.2 Drawing on Isometric Grids: Three Principal Axes (|, /, \\) & Tetris Cube Arrangements",
        "speech": (
            "Turn plain triangular dot paper into your personal 3D drafting studio inside Section Four Point Two: DRAWING ON ISOMETRIC GRIDS! Look at an isometric dot grid sheet—neighboring dots sit spaced evenly along equilateral triangles at exact 60-degree grid steps! "
            "Memorize the three clean principal movement directions (axes) on isometric dot paper right away! Direction One—HEIGHT ( | ): jump straight vertically UP or DOWN along vertical dot columns! Direction Two—DEPTH ( / ): step diagonally upward to the RIGHT along 30-degree slant lines! Direction Three—LENGTH ( \\ ): step diagonally upward to the LEFT along matching 30-degree slant lines! Notice how cleanly these three directions—vertical |, slant-right /, and slant-left \\—give every corner crisp 120-degree isometric separation! "
            "Sketch stepped L-shaped Tetris cube block towers effortlessly by counting exact grid unit steps cleanly along |, /, and \\! Want a rectangular solid cuboid block measuring exactly 2 units tall, 3 units wide, and 2 units deep? Simply step 2 equal dot units vertically along |, 3 equal units along \\, and 2 equal units along /—opposite parallel edges always remain strictly parallel across the page without ever shrinking toward distant perspective vanishing points like camera photos!"
        ),
        "checkpoints": [
            {
                "question": "On standard isometric triangular dot paper, which three line directions represent Height, Depth, and Length cleanly?",
                "options": [
                    "Vertical (|), slant-up-right (/), and slant-up-left (\\)",
                    "Strictly horizontal (—) and vertical (|) only",
                    "Curved arcs and vertical lines",
                    "Random freehand angles converging to one point"
                ],
                "answer": 0,
                "hint": "Think of the three Y-shaped branches meeting at 120° angles on equilateral triangular dots!",
                "explanation": "Isometric grids align Height vertically (|), Depth along 30° slant (/), and Length along opposite 30° slant (\\)."
            },
            {
                "question": "If you draw a 4-cube L-shaped Tetris tower on isometric dot paper (3 cubes tall on the left column plus 1 cube attached forward at the base), how do true isometric edge steps behave?",
                "options": [
                    "Every 1-unit cube edge spans the exact same grid spacing regardless of position or depth",
                    "Back edges shrink to half length like perspective drawings",
                    "Horizontal edges stay flat along 0°",
                    "Vertical edges tilt sideways by 45°"
                ],
                "answer": 0,
                "hint": "Remember 'equal measure' — front and back parallel edges stay equal and parallel!",
                "explanation": "Isometric grids preserve uniform unit spacing ('equal measure') across height, width, and depth without perspective foreshortening."
            }
        ]
    },
    {
        "id": 15,
        "title": "Impossible Optical Illusions",
        "subtitle": "Section 4.2 3D Visual Illusions: Perpetual Ball Paths & The Penrose Triangle on Isometric Grids",
        "speech": (
            "Now uncover a mind-bending geometric twist hiding right inside Section Four Point Two's isometric grids: 3D VISUAL ILLUSIONS AND IMPOSSIBLE OBJECTS! Why can an innocent-looking 2D drawing on isometric dot paper trick our human brain into seeing solid 3D shapes that CANNOT PHYSICALLY EXIST anywhere in real three-dimensional space?! "
            "Examine the celebrated PENROSE TRIANGLE (impossible wooden tribar) drawn effortlessly along an equilateral triangular isometric dot grid! Look closely at ONE corner at a time: each individual corner connects two crisp square beams neatly at a sensible ninety-degree right-angle turn! Yet as your eye chases all three corners endlessly around the closed triangle loop—vertical |, slant /, and slant \\—each solid beam twists impossibly right back onto the starting bar at incompatible 3D depths simultaneously! Locally every single corner joint looks completely logical, solid, and physically buildable; globally the closed triangle loop breaks real 3D Euclidean space geometry completely! "
            "Spot identical visual trickery inside Escher-inspired perpetual waterfalls and impossible ball staircases looping endlessly downhill yet returning smoothly right back up to the exact top starting elevation—pure 2D isometric projection flattening vastly different spatial 3D depths cleanly onto identical flat paper grid dots right before our eyes!"
        ),
        "checkpoints": [
            {
                "question": "Why does an isometric drawing of the Penrose Triangle fool the eye into thinking it is a valid 3D solid when it cannot actually be built in 3D space?",
                "options": [
                    "Each single corner looks locally valid in 3D, while 2D isometric projection collapses distant depths onto the same grid points",
                    "Because triangles cannot be drawn on dot paper",
                    "Because all three sides have unequal curved arcs",
                    "Because 3D cubes have 8 faces"
                ],
                "answer": 0,
                "hint": "Examine each corner individually vs tracing all 3 corners around the closed triangle!",
                "explanation": "Different 3D depth points map onto identical 2D coordinates along an isometric line of sight, allowing locally valid joints to form globally impossible loops."
            },
            {
                "question": "In an isometric 'perpetual descending staircase / ball loop' illusion, what actually makes the loop impossible in physical 3D gravity?",
                "options": [
                    "Descending continuously in a closed loop would require the same vertex to sit simultaneously higher and lower in 3D height",
                    "Because isometric paper cannot show vertical lines",
                    "Because balls always bounce upward",
                    "Because staircases need 4 directions"
                ],
                "answer": 0,
                "hint": "If every step drops strictly downward around a closed loop, where does the end meet the start?!",
                "explanation": "Going strictly downward around a closed cycle returns to the starting elevation — physically impossible without a 2D depth-projection trick."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Theme Summary",
        "subtitle": "Summary Consolidation: Fractals, 3D Nets, Surface Shortest Paths, Orthographic Views & Isometric Grids",
        "speech": (
            "Pause cleanly to unify all five geometric themes of Chapter Eleven onto one memorable study dashboard! First, SELF-SIMILAR FRACTALS: Sierpinski Carpet follows Rₙ = 8ⁿ remaining squares and Hₙ = (8ⁿ − 1)/7 holes; Sierpinski Gasket retains 3ⁿ corner triangles; Koch Snowflake grows outward with ×(4/3) perimeter per step; while Indian temple spires, Nigerian blankets, and Escher prints bring fractals into art! "
            "Second, POLYHEDRA AND FOLDING NETS: count Faces, Edges, and Vertices across prisms and pyramids; cubes and octahedrons each unfold into 11 distinct nets, regular tetrahedrons into 2, cylinders into rectangle + 2 circles, cones into sector + circle, and dodecahedrons into 43,380 nets! "
            "Third, SHORTEST SURFACE PATHS: unfold connected cuboid faces flat into a 2D net and compute straight-line diagonals using Baudhāyana's Theorem (like √5 on a unit cube)! "
            "Fourth, ORTHOGRAPHIC VIEWS AND SHADOWS: combine Front (vertical plane), Top (horizontal plane), and Side perpendicular projections—cleanly mirrored by parallel distant sunlight shadows! "
            "Fifth, ISOMETRIC PROJECTIONS AND ILLUSIONS: align equal-measure grid steps along height (|), depth (/), and length (\\) axes separated at 120°—turning balanced cubes into regular hexagons, sketching Tetris blocks cleanly, and revealing how depth overlaps create impossible optical illusions like the Penrose Triangle!"
        ),
        "checkpoints": [
            {
                "question": "Which summary pairing accurately matches Chapter 11's fractal counts, polyhedron nets, and shortest cube path?",
                "options": [
                    "Carpet Rₙ = 8ⁿ; Cube nets = 11; Unit-cube opposite-corner surface path = √5",
                    "Carpet Rₙ = 9ⁿ; Cube nets = 6; Unit-cube path = 3",
                    "Gasket triangles = 4ⁿ; Tetrahedron nets = 11; Cylinder net = sector + circle",
                    "Koch edges per step ×3; Dodecahedron nets = 2; Isometric cube outline = square"
                ],
                "answer": 0,
                "hint": "Check every formula cleanly: Sierpinski Carpet leaves 8/9 each step, cube has 11 nets, 2×1 unfolded face diagonal = √5!",
                "explanation": "Sierpinski Carpet Rₙ = 8ⁿ, cube nets = 11, and unit-cube surface geodesic = √(2² + 1²) = √5."
            },
            {
                "question": "Which two projection systems represent 3D solids cleanly on flat paper in Section 4.2?",
                "options": [
                    "Orthographic 3-Views (Front, Top, Side perpendicular planes) & Isometric Equal-Measure Grids (|, /, \\)",
                    "Only circular bar charts & random sketches",
                    "Only pie charts & Sierpinski gaskets",
                    "Only 43,380 dodecahedron tabs"
                ],
                "answer": 0,
                "hint": "Compare multi-view blueprints against single-view 120°-axis 3D dot drawings!",
                "explanation": "Section 4.2 teaches Orthographic projections (Front, Top, Side views) and Isometric equal-measure projections (|, /, \\)."
            }
        ]
    }
]

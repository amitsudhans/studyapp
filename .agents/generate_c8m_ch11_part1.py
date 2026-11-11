#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 11: Exploring Some Geometric Themes
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 11 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Self Similar Fractals",
        "subtitle": "Section 4.1 Fractals: Self-Similarity Across Scales in Ferns, Trees, Clouds, Coastlines & Lightning",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Eleven: Exploring Some Geometric Themes! Begin in Section Four Point One with one of nature's most breathtaking geometric ideas: FRACTALS! Unlike smooth classroom circles, squares, or rigid straight lines, real nature bursts with rugged branching complexity! Define a FRACTAL simply as a self-similar geometric figure whose intricate pattern repeats endlessly at smaller and smaller scales! Zoom closely into one tiny part of a fractal, and that miniature piece closely mirrors the entire larger whole! "
            "Spot vivid fractals surrounding you everywhere outdoors! Look at a delicate green fern leaf: each tiny leaflet along the stem reproduces the miniature silhouette of the entire curved fern frond! Gaze upward at winter tree branches splitting into twigs that fork again into micro-twigs! Even billowing cumulus clouds, jagged mountain ranges, winding ocean coastlines, river networks, and sudden forked lightning bolts display natural self-similarity across dozens of magnifying steps! "
            "Mathematicians generate crisp idealized fractals by repeating one simple geometric replacement rule infinitely many times—building astonishingly rich, endless boundary complexity from tiny elementary steps! Even better, because each scaled piece echoes the whole figure closely, simple geometric multipliers reveal fractal counts, perimeters, and areas effortlessly across any chosen stage!"
        ),
        "checkpoints": [
            {
                "question": "Which geometric property defines a fractal across different levels of magnification?",
                "options": [
                    "Self-similarity: smaller parts repeat the shape pattern of the larger whole",
                    "Every edge must form a smooth circular arc",
                    "All interior angles must always equal 90 degrees",
                    "The shape stops repeating after exactly two steps"
                ],
                "answer": 0,
                "hint": "Think about zooming into a single fern leaflet and recognizing the full fern leaf!",
                "explanation": "Fractals exhibit self-similarity, repeating their structure consistently across smaller and smaller scales."
            },
            {
                "question": "Which group contains genuine natural fractals highlighted in NCERT Section 4.1?",
                "options": [
                    "Ferns, trees, clouds, coastlines, mountains, and lightning",
                    "Steel cubes, window panes, and railway tracks",
                    "Flat billiard balls and coins",
                    "Protractors and set squares"
                ],
                "answer": 0,
                "hint": "Look for branching and jagged natural geometry that repeats across scales!",
                "explanation": "Branching ferns, trees, clouds, coastlines, mountain ridges, and lightning bolts are classic natural fractals."
            }
        ]
    },
    {
        "id": 2,
        "title": "Sierpinski Carpet Math",
        "subtitle": "Section 4.1 Sierpinski Carpet: 3×3 Square Subdivision, Remaining Squares R_n = 8^n & Holes H_n",
        "speech": (
            "Discover how Polish mathematician Wacław Sierpiński built an infinite lace square called the SIERPINSKI CARPET! Start at Step Zero with 1 solid whole square—meaning remaining solid squares R₀ = 1 and punched holes H₀ = 0! "
            "Execute Step One right now: divide that single square into a 3 by 3 grid of 9 identical smaller squares, and PUNCH OUT the 1 central middle square! How many solid smaller squares remain? Count cleanly around the border: R₁ = 8 remaining squares, with total punched holes H₁ = 1! "
            "Now apply self-similarity at Step Two: subdivide EACH of those 8 surviving squares into its own 3 by 3 grid and remove EVERY center square! Each of the 8 squares multiplies into 8 tiny squares, yielding R₂ = 8 × 8 = 8² = 64 remaining solid squares, while punching 8 fresh smaller holes to total H₂ = 1 + 8 = 9 holes! "
            "Generalize smoothly to ANY Step n! Remaining solid squares follow exponential powers of eight: Rₙ = 8ⁿ! Meanwhile, cumulative punched-out holes sum neat geometric powers: Hₙ = 1 + 8 + 8² + ... + 8ⁿ⁻¹ = (8ⁿ − 1) ÷ 7, leaving porous mathematical lace!"
        ),
        "checkpoints": [
            {
                "question": "After completing Step 3 of constructing the Sierpinski Carpet, how many solid remaining squares (R₃ = 8³) are left?",
                "options": [
                    "512 remaining squares   (8³ = 512)",
                    "27 remaining squares",
                    "64 remaining squares",
                    "729 remaining squares"
                ],
                "answer": 0,
                "hint": "Each step multiplies surviving solid squares by 8: Step 1 → 8, Step 2 → 64, Step 3 → 8 × 64!",
                "explanation": "At step n, Rₙ = 8ⁿ, so R₃ = 8³ = 8 × 64 = 512 remaining squares."
            },
            {
                "question": "Calculate the total number of punched-out square holes (H₃ = 1 + 8 + 8²) at Step 3 of the Sierpinski Carpet:",
                "options": [
                    "73 total holes",
                    "64 total holes",
                    "9 total holes",
                    "24 total holes"
                ],
                "answer": 0,
                "hint": "Sum 1 (Step 1 hole) + 8 (Step 2 holes) + 64 (Step 3 holes)!",
                "explanation": "H₃ = 1 + 8 + 64 = 73 punched holes (matching (8³ − 1)/7 = 511/7 = 73)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Sierpinski Gasket Triangle",
        "subtitle": "Section 4.1 Sierpinski Gasket: Midpoint Subdivision into 4 Equilateral Triangles & Center Removal",
        "speech": (
            "Now shift from squares to triangles to construct Sierpiński's famous cousin: the SIERPINSKI GASKET (or Sierpinski Triangle)! Begin at Step Zero with 1 solid shaded equilateral triangle! "
            "Follow the crisp iterative construction rule step by step! Find the exact midpoint of each of the three outer sides, and connect those three midpoints neatly with straight segments! Look at what automatically appears inside: four smaller congruent equilateral triangles—three upright triangles tucked into the outer corners, and ONE inverted upside-down triangle sitting dead in the middle! Next, REMOVE that central inverted triangle completely to leave a glowing empty triangular hole! At Step One, 3 shaded corner triangles remain! "
            "Repeat the EXACT same midpoint-and-remove geometric rule recursively inside each of those 3 surviving upright corner triangles! Step Two preserves 3 × 3 = 9 smaller shaded triangles! Step Three yields 3³ = 27 smaller shaded corner triangles! At ANY general Step n, surviving solid shaded triangles scale cleanly and exponentially as 3ⁿ, while every single outer triangle side length shrinks sharply by exact factor 1/2ⁿ—producing delicate self-similar gossamer triangular fractal lace whose remaining shaded total area multiplies cleanly by 3/4 each step and shrinks steadily downward toward zero!"
        ),
        "checkpoints": [
            {
                "question": "During Step 1 of creating the Sierpinski Gasket, connecting the three edge midpoints divides an equilateral triangle into 4 smaller triangles. How many remain shaded after removing the center inverted triangle?",
                "options": [
                    "3 shaded corner triangles   (3¹ = 3)",
                    "4 shaded triangles",
                    "2 shaded triangles",
                    "1 shaded triangle"
                ],
                "answer": 0,
                "hint": "Out of 4 equal sub-triangles, 1 center inverted piece is removed!",
                "explanation": "Removing the central upside-down triangle leaves 3 upright equilateral triangles at the corners."
            },
            {
                "question": "How many solid shaded triangles survive at Step 4 of constructing the Sierpinski Gasket?",
                "options": [
                    "81 triangles   (3⁴ = 81)",
                    "16 triangles   (4²)",
                    "64 triangles   (4³)",
                    "256 triangles"
                ],
                "answer": 0,
                "hint": "Each step triples the count of solid triangles: 3 → 9 → 27 → ...",
                "explanation": "Surviving triangles follow 3ⁿ; at step 4, 3⁴ = 81 shaded triangles remain."
            }
        ]
    },
    {
        "id": 4,
        "title": "Koch Snowflake Curve",
        "subtitle": "Section 4.1 Helge von Koch (1904): Trisecting Edges, Middle Equilateral Bump & Infinite Self-Similarity",
        "speech": (
            "Look next at a mesmerizing icy crystal invented by Swedish mathematician Helge von Koch in 1904: the KOCH SNOWFLAKE! Unlike the Sierpinski carpet and gasket—which carve holes INWARD—the Koch Snowflake grows dazzling triangular spikes OUTWARD around its perimeter! "
            "Trace Step Zero starting cleanly from 1 plain equilateral triangle having 3 straight sides! Now apply Koch's clean three-part rule to EVERY existing straight segment! Step One: divide each side into 3 equal thirds! Next, erase the middle third segment and raise an outward-pointing equilateral triangle bump using two fresh edges of identical one-third length! Watch what happens to every original straight segment: 1 line segment transforms cleanly into 4 shorter connected segments (each 1/3 the previous length)! So at Step One, the original 3 sides bloom into 3 × 4 = 12 edges forming a crisp six-pointed Star of David! "
            "Step Two turns those 12 straight edges into 12 × 4 = 48 sharper jagged edges! At ANY Step n, total edge count grows as 3 × 4ⁿ while each tiny segment shrinks to (1/3)ⁿ! Notice the astounding geometric paradox emerging before your eyes: total boundary length multiplies by factor 4/3 every single step without ever stopping—producing an infinitely long curve enclosing a finite snowflake!"
        ),
        "checkpoints": [
            {
                "question": "In Helge von Koch's 1904 snowflake construction, how many straight edges replace EACH single edge after one iteration of trisecting and raising the middle equilateral bump?",
                "options": [
                    "4 edges (each of length 1/3 of the original edge)",
                    "3 edges",
                    "2 edges",
                    "6 edges"
                ],
                "answer": 0,
                "hint": "Left third (1) + left bump slope (2) + right bump slope (3) + right third (4)!",
                "explanation": "Replacing the middle 1/3 with 2 sides of an equilateral triangle yields 4 equal segments of length 1/3 each."
            },
            {
                "question": "If Step 0 (original equilateral triangle) starts with perimeter 9 cm, what is the perimeter after Step 1 (12 edges of length 1 cm each) and does the perimeter grow forever?",
                "options": [
                    "12 cm at Step 1 (× 4/3 factor); perimeter grows infinitely while enclosing finite area",
                    "6 cm at Step 1; perimeter shrinks toward zero",
                    "9 cm unchanged forever",
                    "27 cm at Step 1"
                ],
                "answer": 0,
                "hint": "Every step multiplies edge length by 4/3 (since 4 segments of 1/3 replace 1 segment)!",
                "explanation": "9 cm × (4/3) = 12 cm at Step 1; repeating infinitely yields infinite perimeter inside a bounded region."
            }
        ]
    },
    {
        "id": 5,
        "title": "Fractals In Art",
        "subtitle": "Section 4.1 Historical Architectural & Textile Fractals: Indian Temples, Fulani Blankets & M.C. Escher",
        "speech": (
            "Think fractals belong solely to modern twentieth-century computer graphics? Centuries before mathematicians coined the word fractal, master artisans and architects carved astonishing self-similar fractals into stone and cloth! "
            "Travel across India's magnificent temple architecture highlighted in NCERT Section Four Point One! Look up at the soaring spire (shikhara) of the Kandariya Mahadev Temple in Khajuraho, or grand gopurams at Madurai, Hampi, and Rameswaram! Notice how one majestic central tower rises surrounded by clustered miniature replicas of that exact same curved tower profile—and each smaller sub-tower bristles with even tinier scaled miniature spires! Self-similar stone geometry creates heavenly upward rhythm! "
            "Journey far across West Africa to admire traditional geometric weaving and vibrant patterned wool textiles, such as handwoven Nigerian Fulani wedding blankets featuring crisp nested rhombic and diamond geometric motifs shrinking recursively inward layer after intricate protective layer! And explore famous twentieth-century mathematical optical lithographs carefully crafted by celebrated Dutch graphic master artist M.C. Escher—especially his famous geometric woodcut print titled 'Smaller and Smaller', where interlocking geometric reptiles and mythical winged creatures tile smoothly inward across endless diminishing scaled generations straight toward the exact central focus point without ever leaving a single tiny open empty gap!"
        ),
        "checkpoints": [
            {
                "question": "Which famous Indian temple tower explicitly showcases self-similar fractal design with miniature spires echoing the central spire?",
                "options": [
                    "Kandariya Mahadev Temple in Khajuraho (along with Madurai, Hampi, and Rameswaram)",
                    "Eiffel Tower in Paris",
                    "Great Pyramid of Giza",
                    "Parthenon in Athens"
                ],
                "answer": 0,
                "hint": "Recall the historic Madhya Pradesh and South Indian temple architecture mentioned in Section 4.1!",
                "explanation": "Kandariya Mahadev (Khajuraho) and temples in Madurai, Hampi, and Rameswaram feature self-similar nested shikhara spires."
            },
            {
                "question": "Which artwork by M.C. Escher and which traditional African weaving showcase fractal recursion across diminishing scales?",
                "options": [
                    "Escher's 'Smaller and Smaller' and Nigerian Fulani wedding blankets",
                    "Da Vinci's Mona Lisa and Scottish kilts",
                    "Van Gogh's Starry Night and Roman togas",
                    "Monet's Water Lilies and Greek mosaics"
                ],
                "answer": 0,
                "hint": "Check the exact Escher print title and West African textile cited in Section 4.1!",
                "explanation": "Escher's 'Smaller and Smaller' shrinks creatures recursively inward, and Nigerian Fulani blankets feature nested fractal patterns."
            }
        ]
    },
    {
        "id": 6,
        "title": "Spatial Mind Cuts",
        "subtitle": "Section 4.2 Visualising Solids: Build it in Your Imagination, Backward Spelling, Slicing Corners & Profiles",
        "speech": (
            "Enter Section Four Point Two: Visualising Solids! Sharpen your mental canvas first with 'Build it in Your Imagination'—spatial puzzles you solve purely inside your mind WITHOUT lifting a pencil! Try picturing a familiar five-letter word printed brightly in mid-air, then reading its mirrored letters backward purely by mental eye! "
            "Next imagine holding a crisp wooden cube or paper square and SLICING off corners with a sharp straight knife! Slice ONE single corner cleanly off a flat 4-corner square: how many corners remain? Eliminating 1 sharp point creates TWO brand-new corners along the cut line—turning a 4-sided square into a 5-sided pentagon! Imagine slicing EVERY corner cleanly off a solid 3D cube: each of the cube's 8 pointed vertices transforms into a fresh triangular face, adding 8 triangular corner faces onto the 6 original squares (forming a 14-faced truncated cube)! "
            "Finally notice how any solid 3D geometric object's flat 2D outer silhouette profile alters dramatically depending strictly on your chosen viewing angle and direction: an upright ice-cream cone appears perfectly circular when viewed straight from directly below, flat and triangular when viewed horizontally sideways across the desk, and oval when tilted slightly in front of your eyes!"
        ),
        "checkpoints": [
            {
                "question": "If you take a flat 4-corner square and slice off ALL 4 sharp corners with straight cuts, how many sides/corners does the resulting polygon have?",
                "options": [
                    "8 sides (an octagon — each cut removes 1 corner and creates 2 new corners)",
                    "4 sides",
                    "0 corners (a circle)",
                    "12 sides"
                ],
                "answer": 0,
                "hint": "Each straight corner cut subtracts 1 vertex and adds 2 fresh vertices (+1 net corner per cut)!",
                "explanation": "Removing 1 corner creates 2 vertices along the cut; across 4 corners, 4 + 4 = 8 edges/vertices form an octagon."
            },
            {
                "question": "If you hold a solid cylinder directly in front of your eyes, which two distinct 2D silhouettes appear from its circular base end versus its curved side?",
                "options": [
                    "Circle from the end view; Rectangle from the perpendicular side view",
                    "Triangle from the end; Circle from the side",
                    "Square from the end; Hexagon from the side",
                    "Pentagon from both views"
                ],
                "answer": 0,
                "hint": "Look down onto the flat lid vs horizontally across the soup-can body!",
                "explanation": "A cylinder projects a circular outline from its top/bottom axis and a flat rectangular profile from its side."
            }
        ]
    },
    {
        "id": 7,
        "title": "Polyhedra Prisms Pyramids",
        "subtitle": "Section 4.2 Making Solids: Faces, Edges, Vertices & Comparing Prisms vs Pyramids (Tetrahedrons)",
        "speech": (
            "Build clear 3D vocabulary cleanly inside Section Four Point Two! Any closed three-dimensional solid bounded entirely by flat polygonal surfaces is called a POLYHEDRON! Count its three structural parts carefully: flat polygonal surfaces are FACES (F); straight line segments where two faces meet are EDGES (E); and sharp corner points where edges meet are VERTICES (V)! Verify a familiar brick-shaped cuboid right away: 6 rectangular faces, 12 straight edges, and 8 sharp corner vertices! "
            "Distinguish two major polyhedron families! Family One: PRISMS! A prism holds TWO congruent parallel polygonal bases (such as two triangles, two squares, or two hexagons) joined around the middle by flat parallelogram (usually rectangular) side faces! A triangular prism therefore packs 5 faces (2 triangles + 3 rectangles), 9 edges, and 6 vertices! "
            "Family Two: PYRAMIDS! Unlike prisms, a solid pyramid stands firmly upon ONE single flat polygonal base, while flat triangular side faces rise slantwise upward from every base edge and converge together neatly at ONE single sharp top corner point called the APEX! A triangular pyramid—whose 4 bounding flat surfaces are all flat triangles—carries the special classical geometric name TETRAHEDRON (counting exactly 4 faces, 6 straight edges, and 4 sharp corner vertices)!"
        ),
        "checkpoints": [
            {
                "question": "How do the side faces and bases of a PRISM differ structurally from those of a PYRAMID?",
                "options": [
                    "Prisms have 2 congruent parallel bases joined by parallelogram faces; Pyramids have 1 base with triangular faces meeting at 1 apex",
                    "Prisms always have 1 circular base; Pyramids have 2 bases",
                    "Prisms taper to an apex point; Pyramids never have edges",
                    "Prisms and Pyramids are identical shapes"
                ],
                "answer": 0,
                "hint": "Compare a box-like Toblerone bar (prism) with an Egyptian monument tapering to one top point (pyramid)!",
                "explanation": "Prisms feature two parallel congruent bases connected by parallelograms; pyramids rise from one base via triangles to a single apex."
            },
            {
                "question": "Count the exact Faces (F), Edges (E), and Vertices (V) of a triangular pyramid (Tetrahedron):",
                "options": [
                    "F = 4 faces, E = 6 edges, V = 4 vertices",
                    "F = 5 faces, E = 9 edges, V = 6 vertices",
                    "F = 6 faces, E = 12 edges, V = 8 vertices",
                    "F = 5 faces, E = 8 edges, V = 5 vertices"
                ],
                "answer": 0,
                "hint": "1 triangular base + 3 triangular side faces = 4 faces; 3 base edges + 3 slanted edges = 6 edges!",
                "explanation": "A tetrahedron has 4 triangular faces, 6 edges, and 4 corner vertices (note V − E + F = 4 − 6 + 4 = 2)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Unfolding Solid Nets",
        "subtitle": "Section 4.2 Nets of Solids: 2D Unfolded Patterns, Assembly Tabs, 11 Cube Nets & 2 Tetrahedron Nets",
        "speech": (
            "Slice carefully along selected edges of a hollow cardboard box, flatten every face completely down onto a desk without disconnecting it, and you reveal a NET! Define a NET concisely: a two-dimensional flat pattern that folds cleanly along crease lines to build a three-dimensional hollow solid! "
            "Why do real cardboard manufacturers use sturdy cardstock with slanted ATTACHMENT TABS (flaps) along net borders? Because tabs catch glue cleanly inside seams so finished models hold crisp rigid edges! "
            "Watch carefully—not every random flat cluster of 6 attached unit squares folds cleanly into a closed wooden cube! Some flat square layouts force two square faces to overlap and crash directly onto the exact same side! Mathematicians proved mathematically there are EXACTLY ELEVEN (11) unique distinct valid cube nets (counting mirror flips and planar rotations as identical geometric patterns) that fold cleanly into a complete closed 6-faced cube—including the classic cross, 'T', and zig-zag staircase patterns! Now fold a smaller 4-faced regular TETRAHEDRON (where all 4 flat faces are congruent equilateral triangles): there are ONLY TWO (2) unique valid nets—one central triangle wearing three folding flaps around all outer edges (forming one larger equilateral triangle!), and one slanted four-triangle parallelogram chain!"
        ),
        "checkpoints": [
            {
                "question": "Counting rotations and reflections as identical shapes, how many UNIQUE valid 2D nets fold into a complete cube (6 squares), and how many fold into a regular tetrahedron (4 equilateral triangles)?",
                "options": [
                    "Cube: 11 unique nets; Regular Tetrahedron: 2 unique nets",
                    "Cube: 6 unique nets; Regular Tetrahedron: 4 unique nets",
                    "Cube: 12 unique nets; Regular Tetrahedron: 3 unique nets",
                    "Cube: 2 unique nets; Regular Tetrahedron: 11 unique nets"
                ],
                "answer": 0,
                "hint": "Recall the exact NCERT counts: 11 distinct hexomino nets for cubes and 2 for tetrahedrons!",
                "explanation": "There are exactly 11 distinct cube nets and 2 distinct regular tetrahedron nets."
            },
            {
                "question": "Why does an arrangement of 6 squares arranged in a single 2 × 3 solid rectangle FAIL to fold into a cube?",
                "options": [
                    "Opposite squares overlap onto the same cube face while leaving ends open (and four faces cannot wrap around 4 sides cleanly)",
                    "Because a cube requires 8 square faces",
                    "Because rectangles cannot fold at 90 degrees",
                    "Because 2 × 3 uses only 5 squares"
                ],
                "answer": 0,
                "hint": "Notice any 2×2 square cluster folds into colliding faces around a shared vertex!",
                "explanation": "Any net containing a 2 × 2 square block creates overlapping folded faces, preventing a closed 6-face cube."
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 14: Math of Space: Surface Area and Volume
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Cuboids Rectangular Solids",
        "subtitle": "Section 14.1 Cuboids and Cubes: Total Surface Area 2(wl + hl + hw) & Volume lwh",
        "speech": (
            "Welcome to Chapter Fourteen: Math of Space, Surface Area and Volume! Look around your room—books, brick "
            "walls, shoeboxes, and cupboards are all CUBOIDS inside Section Fourteen Point One! A cuboid is a "
            "rectangular 3D solid bounded by six rectangular faces meeting at right angles, defined by three dimensions: "
            "length l, width w, and height h! "
            "How much wrapping paper covers the entire outside? Notice the six faces come in three identical opposite "
            "pairs! The top and bottom each have area w times l! The front and back each have area h times l! The left "
            "and right sides each have area h times w! Adding all six faces gives Total Surface Area TSA equals two "
            "times (w l plus h l plus h w)! "
            "Now how much space fits inside? Imagine stacking thin rectangular cards of area l times w, one on top "
            "of another, up to height h! Each card contributes a thin slice of area l w, so stacking up to height h "
            "sweeps out Volume V equals length times width times height—l w h! Whether measuring a wooden crate or "
            "a swimming pool, surface area measures the outer skin in square units, while volume measures the inner "
            "capacity in cubic units!"
        ),
        "checkpoints": [
            {
                "question": "A closed rectangular box has length 5 cm, width 4 cm, and height 3 cm. What are its Total Surface Area and Volume?",
                "options": [
                    "TSA = 94 cm², V = 60 cm³",
                    "TSA = 47 cm², V = 60 cm³",
                    "TSA = 60 cm², V = 94 cm³",
                    "TSA = 94 cm², V = 12 cm³",
                ],
                "answer": 0,
                "hint": "Use TSA = 2(wl + hl + hw) and V = lwh!",
                "explanation": "TSA = 2(20 + 15 + 12) = 2(47) = 94 cm²; V = 5 × 4 × 3 = 60 cm³.",
            },
            {
                "question": "Why does stacking thin rectangular cards of length l and width w up to height h explain the volume formula V = lwh?",
                "options": [
                    "Volume equals base area (lw) multiplied by the stack height (h)",
                    "Volume equals perimeter multiplied by height",
                    "Volume only depends on the top face",
                    "Cards have zero width",
                ],
                "answer": 0,
                "hint": "Think of each card as a horizontal cross-section of area lw!",
                "explanation": "Accumulating cross-sectional area lw through height h gives V = (lw) × h = lwh.",
            },
        ],
    },
    {
        "id": 2,
        "title": "Cube Special Properties",
        "subtitle": "Section 14.1 Cuboids and Cubes: Equilateral Special Case (TSA = 6a², V = a³)",
        "speech": (
            "Now look at the most symmetric cuboid of all inside Section Fourteen Point One: THE CUBE! A cube is "
            "simply a special cuboid where length, width, and height are ALL equal: l equals w equals h equals a! "
            "Let us substitute l equals a, w equals a, and h equals a directly into our cuboid formulas! First, "
            "Total Surface Area becomes two times (a-squared plus a-squared plus a-squared), which simplifies to six "
            "times a-squared! Why? Because all six faces are identical squares of area a-squared! If you leave the top "
            "open—like an open-top cubical aquarium—you count five squares, giving five a-squared! "
            "Second, Volume becomes a times a times a, which is a-cubed! Look at what happens as edge length a grows "
            "through the natural numbers one, two, three, four, five! The volumes generate the famous sequence of "
            "CUBE NUMBERS: one, eight, twenty-seven, sixty-four, one hundred twenty-five! Notice how doubling a cube's "
            "side from a to two a multiplies its surface area by four (two squared), yet multiplies its volume by "
            "EIGHT (two cubed)! That explosive cubic growth explains why small boxes hold far less than you expect—and "
            "why cube numbers grow so rapidly across every dimension!"
        ),
        "checkpoints": [
            {
                "question": "If the edge length of a cube is tripled from a to 3a, by what factor does its Volume increase?",
                "options": ["27 times", "9 times", "3 times", "6 times"],
                "answer": 0,
                "hint": "Substitute 3a into V = (side)³!",
                "explanation": "V_new = (3a)³ = 27a³, which is 27 times the original volume.",
            },
            {
                "question": "A cube has Total Surface Area 150 cm². What is its edge length a and Volume V?",
                "options": [
                    "a = 5 cm, V = 125 cm³",
                    "a = 6 cm, V = 216 cm³",
                    "a = 25 cm, V = 625 cm³",
                    "a = 5 cm, V = 25 cm³",
                ],
                "answer": 0,
                "hint": "Set 6a² = 150 to find a² = 25, then compute a³!",
                "explanation": "6a² = 150 ⇒ a² = 25 ⇒ a = 5 cm, so V = 5³ = 125 cm³.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Right Circular Cylinders",
        "subtitle": "Section 14.2 Right Circular Cylinder: Right vs Oblique, Cross-Sections & MRI Scans",
        "speech": (
            "Welcome to Section Fourteen Point Two: THE RIGHT CIRCULAR CYLINDER! Tin cans, water pipes, pillars, and "
            "roller drums share this smooth circular shape! Carefully distinguish a RIGHT circular cylinder from an "
            "OBLIQUE circular cylinder! In a right circular cylinder, the central axis connecting the centres of the "
            "top and bottom circular bases stands strictly PERPENDICULAR (at ninety degrees) to both bases! In an "
            "oblique cylinder—like a leaning stack of coins—the axis tilts at a slanted angle! "
            "Now slice a right circular cylinder with an imaginary plane to discover its 3D CROSS-SECTIONS! Slice it "
            "PARALLEL to the circular base: every horizontal slice is an identical CIRCLE of radius r! Slice it "
            "PARALLEL to the central axis (vertically straight down): the cross-section is a RECTANGLE of height h "
            "and width up to two r! "
            "Where do cross-sections save lives every day? In MEDICAL MRI SCANS! An MRI machine does not cut the "
            "human body open; instead, magnetic fields capture hundreds of thin two-dimensional cross-sectional slices "
            "along the body's axis, and computers stack those slices back into a complete three-dimensional image for "
            "doctors to inspect soft tissues, internal organs, and bones non-invasively with pinpoint medical precision every day!"
        ),
        "checkpoints": [
            {
                "question": "What two shapes appear when a right circular cylinder is sliced (1) parallel to its base and (2) parallel to its central axis?",
                "options": [
                    "(1) Circle and (2) Rectangle",
                    "(1) Triangle and (2) Circle",
                    "(1) Square and (2) Triangle",
                    "(1) Ellipse and (2) Pentagon",
                ],
                "answer": 0,
                "hint": "Horizontal slices match the circular base; vertical slices cut straight down the wall!",
                "explanation": "Slicing parallel to the circular base yields a circle; slicing parallel to the axis yields a rectangle.",
            },
            {
                "question": "What defines a 'right' circular cylinder compared to an oblique cylinder?",
                "options": [
                    "Its central axis is perpendicular (90°) to the circular bases",
                    "Its radius equals its height",
                    "It has no curved surface",
                    "Its bases are squares",
                ],
                "answer": 0,
                "hint": "Think of 'right' as in right angle (90°)!",
                "explanation": "In a right circular cylinder, the line joining the centres of the bases is perpendicular to both bases.",
            },
        ],
    },
    {
        "id": 4,
        "title": "Cylinder Area Volume",
        "subtitle": "Section 14.2 & 14.2.1 Formulas: CSA 2πrh, TSA, Volume πr²h & Khakhra Stack",
        "speech": (
            "Let us derive all four cylinder formulas inside Section Fourteen Point Two and Section Fourteen Point Two "
            "Point One! First, wrap a sheet of paper tightly around a cylindrical tin of radius r and height h, then "
            "unroll it flat onto your desk! What shape appears? A perfect RECTANGLE! Its height is h, and its length "
            "equals the circumference of the circular base, two pi r! Multiplying length by height immediately proves "
            "Curved Surface Area CSA equals two pi r h! "
            "Second, to cover a CLOSED cylinder at both ends, add two circular lids of area pi r-squared each: Total "
            "Surface Area TSA equals two pi r h plus two pi r-squared, which factors cleanly as two pi r times (h plus "
            "r)! What if the cylinder has an OPEN TOP, like a drinking glass? Add only ONE circular bottom: open-top "
            "TSA equals pi r times (two h plus r)! "
            "Third, why is Volume V equals pi r-squared h? Imagine stacking thin circular flatbreads—KHAKHRAS—each "
            "of area pi r-squared, one atop another up to height h! Base area pi r-squared multiplied by stack height "
            "h gives Volume V equals pi r-squared h—simple, physical, and completely unforgettable!"
        ),
        "checkpoints": [
            {
                "question": "An open-top cylindrical mug has radius r = 7 cm and height h = 10 cm (use π = 22/7). What is its outer surface area?",
                "options": [
                    "594 cm² (CSA 440 + base 154)",
                    "748 cm²",
                    "440 cm²",
                    "1540 cm²",
                ],
                "answer": 0,
                "hint": "An open-top cylinder has CSA = 2πrh plus ONE circular base πr²!",
                "explanation": "CSA = 2(22/7)(7)(10) = 440 cm²; one base = (22/7)(49) = 154 cm²; total = 594 cm².",
            },
            {
                "question": "If you double the radius r of a cylinder while keeping its height h unchanged, what happens to its Volume?",
                "options": [
                    "It becomes 4 times as large (since V ∝ r²)",
                    "It doubles",
                    "It becomes 8 times as large",
                    "It stays the same",
                ],
                "answer": 0,
                "hint": "Replace r with 2r in V = πr²h!",
                "explanation": "V_new = π(2r)²h = 4πr²h = 4V.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Cones Slant Height",
        "subtitle": "Section 14.3 Cones: Right Triangle Revolution & Baudhāyana-Pythagoras Relation",
        "speech": (
            "Now step into Section Fourteen Point Three: RIGHT CIRCULAR CONES! Ice-cream cones, traffic pylons, "
            "birthday caps, and volcanic peaks are cones! How is a right circular cone generated geometrically? Take a "
            "right-angled triangle with vertical leg h and horizontal leg r, and spin it rapidly around its vertical "
            "leg h! The spinning horizontal leg sweeps out a flat circular base of radius r, while the spinning "
            "hypotenuse sweeps out the sloping conical wall! "
            "Every right circular cone has three key lengths meeting at a hidden right-angled triangle inside: the "
            "base radius r, the vertical perpendicular height h from the centre of the base to the pointed apex, and "
            "the SLANT HEIGHT l measured along the outer sloped edge from the rim to the apex! "
            "Because the vertical height h meets the base radius r at ninety degrees, the Baudhāyana-Pythagoras "
            "Theorem connects all three lengths with an unbreakable equation: l-squared equals h-squared plus "
            "r-squared! Whenever a problem gives you radius r and height h—say r equals three and h equals four—you "
            "immediately compute slant height l equals square root of nine plus sixteen, which is five—forming a "
            "classic three-four-five right triangle hidden neatly inside the cone!"
        ),
        "checkpoints": [
            {
                "question": "A conical tent has base radius r = 6 m and vertical height h = 8 m. What is its slant height l?",
                "options": ["10 m", "14 m", "48 m", "7 m"],
                "answer": 0,
                "hint": "Apply Baudhāyana-Pythagoras: l² = h² + r²!",
                "explanation": "l = √(8² + 6²) = √(64 + 36) = √100 = 10 m.",
            },
            {
                "question": "Spinning a right-angled triangle around one of its perpendicular legs generates which 3D solid?",
                "options": [
                    "A right circular cone",
                    "A cylinder",
                    "A sphere",
                    "A square pyramid",
                ],
                "answer": 0,
                "hint": "The spinning hypotenuse traces the sloped wall meeting at a single apex!",
                "explanation": "Revolving a right triangle about one leg creates a circular base and a conical surface meeting at an apex.",
            },
        ],
    },
    {
        "id": 6,
        "title": "Cone Area Volume",
        "subtitle": "Section 14.3 Cones: Sector Unrolling (CSA = πrl), V = ⅓πr²h & Archimedes (c. 225 BCE)",
        "speech": (
            "Now derive the area and volume of a cone inside Section Fourteen Point Three! Cut a paper cone straight "
            "along one slant edge l and unroll it flat! It opens into a CIRCULAR SECTOR of radius l whose curved arc "
            "length equals the cone's base circumference, two pi r! Just like a triangle of base two pi r and height "
            "l, the sector's area equals one-half times arc length times radius: one-half times two pi r times l, "
            "which simplifies cleanly to Curved Surface Area CSA equals pi r l! Adding the flat circular base pi "
            "r-squared gives Total Surface Area TSA equals pi r times (l plus r)! "
            "Next, what is the volume of a cone compared to a cylinder of the EXACT same base radius r and height h? "
            "Test it physically with salt or clay! Fill the cone to the brim with salt and pour it into the matching "
            "cylinder: it takes EXACTLY THREE FULL CONES to fill one cylinder! Around two hundred twenty-five BCE, "
            "Archimedes proved this exact one-third factor rigorously: Volume of a cone equals one-third pi r-squared h, "
            "saving two-thirds of the material compared to an equal cylinder of identical base and height!"
        ),
        "checkpoints": [
            {
                "question": "A cone has radius r = 7 cm and slant height l = 10 cm (π = 22/7). What is its Curved Surface Area?",
                "options": ["220 cm²", "440 cm²", "154 cm²", "374 cm²"],
                "answer": 0,
                "hint": "Use CSA = πrl!",
                "explanation": "CSA = (22/7) × 7 × 10 = 220 cm².",
            },
            {
                "question": "How many congruent cones of radius r and height h fill a cylinder of the same radius r and height h?",
                "options": ["3 cones", "2 cones", "4 cones", "6 cones"],
                "answer": 0,
                "hint": "Compare V_cone = (1/3)πr²h with V_cylinder = πr²h!",
                "explanation": "Since V_cone = (1/3) V_cylinder, exactly 3 full cones fill 1 matching cylinder.",
            },
        ],
    },
    {
        "id": 7,
        "title": "Pyramidal Shapes Geometry",
        "subtitle": "Section 14.4 Pyramidal Shapes: Polygonal Bases, Apex & Iconic Real-World Pyramids",
        "speech": (
            "Welcome to Section Fourteen Point Four: PYRAMIDAL SHAPES! Unlike a prism or cylinder that keeps the same "
            "cross-section from bottom to top, a pyramid tapers smoothly from a flat polygonal base to a single sharp "
            "point called the APEX! Every lateral face of a pyramid is a TRIANGLE connecting one edge of the base up "
            "to the shared apex! "
            "Name a pyramid by its base polygon! A triangle base gives a triangular pyramid (or tetrahedron) with "
            "four triangular faces—just like Erno Rubik's famous Pyraminx triangular pyramid puzzle! A square base "
            "gives a square pyramid with one square floor and four triangular walls—just like the Great Pyramids of "
            "Egypt! "
            "Even nature sculpts monumental pyramids! Look at Shivling Peak in the Garhwal Himalayas of Uttarakhand, "
            "rising like a dramatic four-sided snow pyramid, or the Matterhorn in the Swiss Alps! Notice also how the "
            "horizontal cross-sections of a pyramid stay geometrically similar to its polygonal base while shrinking "
            "steadily toward zero right at the apex! Engineers, architects, and mountaineers admire pyramids because "
            "their wide bases and sloped triangular faces distribute enormous structural weight safely downward into the solid ground below, standing remarkably strong and stable for thousands of years!"
        ),
        "checkpoints": [
            {
                "question": "How many faces does a square pyramid have in total?",
                "options": [
                    "5 faces (1 square base + 4 triangular lateral faces)",
                    "4 faces",
                    "6 faces",
                    "8 faces",
                ],
                "answer": 0,
                "hint": "Count the square bottom plus one triangle per base edge!",
                "explanation": "A square base has 4 edges, each supporting a triangular face meeting at the apex: 1 + 4 = 5 faces.",
            },
            {
                "question": "What shape is every lateral face of a pyramid?",
                "options": ["Triangle", "Rectangle", "Circle", "Hexagon"],
                "answer": 0,
                "hint": "Each side connects a straight base edge to a single point (the apex)!",
                "explanation": "Joining both endpoints of a base edge to the single apex forms a triangle.",
            },
        ],
    },
    {
        "id": 8,
        "title": "Pyramid Volume Formula",
        "subtitle": "Section 14.4 Pyramidal Shapes: V = ⅓ × Base Area × Height & Cones as Circular Pyramids",
        "speech": (
            "Discover one of the most unifying laws in all of 3D geometry inside Section Fourteen Point Four: THE "
            "UNIVERSAL PYRAMID VOLUME FORMULA! Take ANY pyramid—whether its base is a triangle, a square, a pentagon, "
            "or an irregular polygon—with base area B and perpendicular vertical height h! Its volume is ALWAYS "
            "one-third times Base Area times height: V equals one-third B h! "
            "Why does the exact same one-third factor appear for every pyramid? Think of a cube of side a sliced "
            "from its centre to all six square faces: that splits the cube into six identical square pyramids, each "
            "having base area a-squared and height a over two! Each pyramid therefore holds one-sixth of a-cubed, "
            "which equals one-third times (a-squared) times (a over two)—proving V equals one-third B h! "
            "Now watch the grand unification! Imagine increasing the number of sides of a regular polygon base from "
            "four to eight, to sixty, to infinity: the polygon approaches a smooth CIRCLE of area pi r-squared! Thus a "
            "CONE IS SIMPLY A PYRAMID WITH A CIRCULAR BASE, and one-third B h immediately becomes one-third pi "
            "r-squared h—uniting all pyramids and circular cones together under one single timeless volume law!"
        ),
        "checkpoints": [
            {
                "question": "A square pyramid has base side 6 cm and vertical height 10 cm. What is its Volume?",
                "options": ["120 cm³", "360 cm³", "180 cm³", "60 cm³"],
                "answer": 0,
                "hint": "First find Base Area B = 6 × 6 = 36 cm², then use V = (1/3)Bh!",
                "explanation": "V = (1/3) × 36 × 10 = 120 cm³.",
            },
            {
                "question": "How does the cone volume formula V = (1/3)πr²h connect to the pyramid volume formula V = (1/3)Bh?",
                "options": [
                    "A cone is a pyramid whose base is a circle of area B = πr²",
                    "A cone has no apex",
                    "A cone has half the volume of a square pyramid",
                    "They are completely unrelated",
                ],
                "answer": 0,
                "hint": "Substitute the area of a circular base B = πr² into V = (1/3)Bh!",
                "explanation": "Replacing polygonal base area B with circular base area πr² turns (1/3)Bh into (1/3)πr²h.",
            },
        ],
    },
]

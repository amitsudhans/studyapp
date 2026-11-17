#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 14: Math of Space: Surface Area and Volume
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Cuboids Cylinders Quiz",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Cuboids, Cubes & Right Circular Cylinders (14.1–14.2)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Find the Total Surface Area of a cuboid with l = 8 cm, w = 5 cm, and h = 4 cm.",
                "options": ["184 cm²", "160 cm²", "92 cm²", "120 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use TSA = 2(wl + hl + hw).",
                    "Compute wl = 40, hl = 32, hw = 20; sum = 92.",
                    "TSA = 2 × 92 = 184 cm².",
                ],
            },
            {
                "question": "What is the volume of a cuboid whose base area is 45 cm² and height is 6 cm?",
                "options": ["270 cm³", "90 cm³", "135 cm³", "540 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Recall V = Base Area × height = (lw) × h.",
                    "Substitute lw = 45 and h = 6.",
                    "V = 45 × 6 = 270 cm³.",
                ],
            },
            {
                "question": "An open-top cubical box has side a = 4 cm. What is its outer surface area?",
                "options": ["80 cm²", "96 cm²", "64 cm²", "48 cm²"],
                "answer": 0,
                "solution_steps": [
                    "An open-top cube has 5 square faces (4 walls + 1 bottom).",
                    "Each face has area a² = 4² = 16 cm².",
                    "Outer surface area = 5 × 16 = 80 cm².",
                ],
            },
            {
                "question": "Which sequence lists the volumes of cubes with edges 1, 2, 3, 4, 5?",
                "options": [
                    "1, 8, 27, 64, 125",
                    "1, 4, 9, 16, 25",
                    "6, 24, 54, 96, 150",
                    "2, 4, 6, 8, 10",
                ],
                "answer": 0,
                "solution_steps": [
                    "Volume of a cube of side a is V = a³.",
                    "Compute 1³ = 1, 2³ = 8, 3³ = 27, 4³ = 64, 5³ = 125.",
                    "These are the standard cube numbers.",
                ],
            },
            {
                "question": "If a right circular cylinder is sliced by a plane parallel to its central axis, what shape is the cross-section?",
                "options": ["Rectangle", "Circle", "Triangle", "Sphere"],
                "answer": 0,
                "solution_steps": [
                    "A plane parallel to the central axis cuts straight down from the top circle to the bottom circle.",
                    "Both top and bottom cuts are parallel straight chords of equal length.",
                    "The vertical side walls meet them at 90°, forming a rectangle.",
                ],
            },
            {
                "question": "Find the Curved Surface Area of a cylinder of radius r = 3.5 cm and height h = 10 cm (π = 22/7).",
                "options": ["220 cm²", "110 cm²", "440 cm²", "385 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use CSA = 2πrh.",
                    "CSA = 2 × (22/7) × 3.5 × 10 = 2 × 11 × 10.",
                    "CSA = 220 cm².",
                ],
            },
            {
                "question": "What is the Total Surface Area of a closed cylinder with radius r = 7 cm and height h = 3 cm (π = 22/7)?",
                "options": ["440 cm²", "132 cm²", "308 cm²", "286 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use TSA = 2πr(h + r).",
                    "TSA = 2 × (22/7) × 7 × (3 + 7) = 44 × 10.",
                    "TSA = 440 cm².",
                ],
            },
            {
                "question": "Find the volume of a cylinder of radius r = 7 cm and height h = 5 cm (π = 22/7).",
                "options": ["770 cm³", "154 cm³", "385 cm³", "1540 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use V = πr²h.",
                    "V = (22/7) × 7 × 7 × 5 = 154 × 5.",
                    "V = 770 cm³.",
                ],
            },
            {
                "question": "Which everyday physical analogy explains V = πr²h for a cylinder?",
                "options": [
                    "Stacking thin circular khakhras of area πr² up to height h",
                    "Folding six squares into a box",
                    "Wrapping string around a ball",
                    "Spinning a rectangle around its diagonal",
                ],
                "answer": 0,
                "solution_steps": [
                    "Each thin circular khakhra has area πr².",
                    "Stacking them vertically to height h sweeps out volume (πr²) × h.",
                    "This gives V = πr²h.",
                ],
            },
            {
                "question": "If the height of a cylinder is halved and its radius is doubled, what happens to its Volume?",
                "options": [
                    "It doubles (2V)",
                    "It stays the same",
                    "It quadruples (4V)",
                    "It halves (0.5V)",
                ],
                "answer": 0,
                "solution_steps": [
                    "New radius = 2r, new height = h/2.",
                    "V_new = π(2r)²(h/2) = π(4r²)(h/2) = 2πr²h.",
                    "Therefore the volume doubles.",
                ],
            },
        ],
    },
    {
        "id": 18,
        "title": "Cones Pyramids Quiz",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Cones, Slant Height & Pyramidal Shapes (14.3–14.4)",
        "is_quiz": True,
        "questions": [
            {
                "question": "A right circular cone has radius r = 5 cm and vertical height h = 12 cm. Find its slant height l.",
                "options": ["13 cm", "17 cm", "7 cm", "15 cm"],
                "answer": 0,
                "solution_steps": [
                    "Use Baudhāyana-Pythagoras: l² = h² + r².",
                    "l² = 12² + 5² = 144 + 25 = 169.",
                    "l = √169 = 13 cm.",
                ],
            },
            {
                "question": "Find the Curved Surface Area of a cone with r = 7 cm and slant height l = 15 cm (π = 22/7).",
                "options": ["330 cm²", "660 cm²", "154 cm²", "484 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use CSA = πrl.",
                    "CSA = (22/7) × 7 × 15 = 22 × 15.",
                    "CSA = 330 cm².",
                ],
            },
            {
                "question": "Find the Total Surface Area of a solid cone with r = 7 cm and slant height l = 13 cm (π = 22/7).",
                "options": ["440 cm²", "286 cm²", "154 cm²", "616 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use TSA = πr(l + r).",
                    "TSA = (22/7) × 7 × (13 + 7) = 22 × 20.",
                    "TSA = 440 cm².",
                ],
            },
            {
                "question": "What shape do you obtain when you cut a cone along a slant edge and unroll its curved surface flat?",
                "options": [
                    "A circular sector of radius l and arc length 2πr",
                    "A rectangle of length 2πr",
                    "A square of side l",
                    "An equilateral triangle",
                ],
                "answer": 0,
                "solution_steps": [
                    "Every point on the base rim is distance l from the apex.",
                    "Unrolling the cone flattens those slant edges into radii of length l.",
                    "Thus it forms a circular sector of radius l and arc length 2πr.",
                ],
            },
            {
                "question": "Find the volume of a cone with radius r = 7 cm and height h = 12 cm (π = 22/7).",
                "options": ["616 cm³", "1848 cm³", "308 cm³", "924 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use V = (1/3)πr²h.",
                    "V = (1/3) × (22/7) × 7 × 7 × 12 = 154 × 4.",
                    "V = 616 cm³.",
                ],
            },
            {
                "question": "A cylinder and a cone have equal base radii and equal heights. If the cylinder holds 900 mL, how much does the cone hold?",
                "options": ["300 mL", "450 mL", "600 mL", "2700 mL"],
                "answer": 0,
                "solution_steps": [
                    "V_cone = (1/3) V_cylinder for equal base and height.",
                    "V_cone = (1/3) × 900 mL.",
                    "V_cone = 300 mL.",
                ],
            },
            {
                "question": "What is the volume of a triangular pyramid whose base area is 24 cm² and vertical height is 10 cm?",
                "options": ["80 cm³", "240 cm³", "120 cm³", "40 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use V = (1/3) × Base Area × height.",
                    "V = (1/3) × 24 × 10 = 8 × 10.",
                    "V = 80 cm³.",
                ],
            },
            {
                "question": "How many faces does a triangular pyramid (tetrahedron, like Erno Rubik's Pyraminx) have?",
                "options": ["4 triangular faces", "5 faces", "6 faces", "3 faces"],
                "answer": 0,
                "solution_steps": [
                    "A triangular pyramid has 1 triangular base.",
                    "Each of its 3 base edges supports 1 triangular lateral face.",
                    "Total = 1 + 3 = 4 triangular faces.",
                ],
            },
            {
                "question": "Why can a cone be viewed as a special case of a pyramid?",
                "options": [
                    "Its polygonal base approaches a circle as the number of sides grows to infinity, keeping V = (1/3)Bh",
                    "Because a cone has 4 triangular faces",
                    "Because a pyramid has no apex",
                    "Because l = h in every pyramid",
                ],
                "answer": 0,
                "solution_steps": [
                    "Increasing sides of a regular polygon base approaches a circle of area B = πr².",
                    "All slant edges still meet at a single apex at height h.",
                    "Hence V = (1/3)Bh becomes V = (1/3)πr²h.",
                ],
            },
            {
                "question": "Which famous Himalayan peak in Uttarakhand is cited as a natural pyramidal mountain?",
                "options": [
                    "Shivling Peak",
                    "Mount Fuji",
                    "Mount Vesuvius",
                    "Krakatoa",
                ],
                "answer": 0,
                "solution_steps": [
                    "NCERT Chapter 14 highlights Shivling Peak in Uttarakhand and the Matterhorn in the Swiss Alps.",
                    "Both exhibit dramatic sharp pyramidal faces tapering to an apex.",
                    "Thus Shivling Peak is the correct answer.",
                ],
            },
        ],
    },
    {
        "id": 19,
        "title": "Spheres Hemispheres Quiz",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Spheres, Archimedes' Proof & Hemispheres (14.5)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Find the surface area of a sphere of radius r = 3.5 cm (π = 22/7).",
                "options": ["154 cm²", "77 cm²", "308 cm²", "616 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use Surface Area = 4πr².",
                    "4 × (22/7) × 3.5 × 3.5 = 4 × 11 × 3.5 = 44 × 3.5.",
                    "Surface Area = 154 cm².",
                ],
            },
            {
                "question": "Find the volume of a sphere of radius r = 3 cm in terms of π.",
                "options": ["36π cm³", "12π cm³", "27π cm³", "108π cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use V = (4/3)πr³.",
                    "V = (4/3) × π × 3³ = (4/3) × 27π.",
                    "V = 36π cm³.",
                ],
            },
            {
                "question": "What is the Curved Surface Area of a hemisphere of radius r = 7 cm (π = 22/7)?",
                "options": ["308 cm²", "462 cm²", "616 cm²", "154 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Use Hemisphere CSA = 2πr².",
                    "CSA = 2 × (22/7) × 7 × 7 = 2 × 154.",
                    "CSA = 308 cm².",
                ],
            },
            {
                "question": "What is the Total Surface Area of a SOLID hemisphere of radius 10 cm (π = 3.14)?",
                "options": ["942 cm²", "628 cm²", "314 cm²", "1256 cm²"],
                "answer": 0,
                "solution_steps": [
                    "Solid hemisphere TSA = CSA (2πr²) + flat circular base (πr²) = 3πr².",
                    "TSA = 3 × 3.14 × 10² = 3 × 314.",
                    "TSA = 942 cm².",
                ],
            },
            {
                "question": "In Archimedes' proof, what is the height h of the cylinder that tightly circumscribes a sphere of radius r?",
                "options": ["h = 2r", "h = r", "h = πr", "h = 4r"],
                "answer": 0,
                "solution_steps": [
                    "The sphere touches both the bottom and top lids of the circumscribed cylinder.",
                    "The distance from bottom to top of a sphere is its diameter 2r.",
                    "Thus h = 2r, giving Cylinder CSA = 2πr(2r) = 4πr².",
                ],
            },
            {
                "question": "What is the ratio of the Volume of a sphere of radius r to the Volume of its circumscribed cylinder (radius r, height 2r)?",
                "options": ["2 : 3", "1 : 2", "3 : 4", "1 : 3"],
                "answer": 0,
                "solution_steps": [
                    "V_sphere = (4/3)πr³ and V_cylinder = πr²(2r) = 2πr³.",
                    "Ratio = (4/3) ÷ 2 = 4/6 = 2/3.",
                    "Archimedes engraved this famous 2 : 3 ratio on his tomb.",
                ],
            },
            {
                "question": "In the string-wrapping experiment, the string covering a sphere of radius r fills how many flat circles of radius r?",
                "options": ["4 circles", "2 circles", "3 circles", "1 circle"],
                "answer": 0,
                "solution_steps": [
                    "Sphere Surface Area = 4πr².",
                    "One flat circle of radius r has area πr².",
                    "4πr² ÷ πr² = 4 circles.",
                ],
            },
            {
                "question": "If the radius of a sphere is doubled from r to 2r, by what factor does its Surface Area increase?",
                "options": ["4 times", "2 times", "8 times", "16 times"],
                "answer": 0,
                "solution_steps": [
                    "Surface Area = 4πr².",
                    "Replacing r with 2r gives 4π(2r)² = 4 × (4πr²).",
                    "Surface area increases by 4 times.",
                ],
            },
            {
                "question": "Why does an equirectangular world map distort Greenland's size compared to equatorial countries?",
                "options": [
                    "Cylindrical projection stretches shrinking polar latitude circles to match the equator's width",
                    "Greenland is closer to the Sun",
                    "Oceans have negative area",
                    "Equatorial countries are triangles",
                ],
                "answer": 0,
                "solution_steps": [
                    "On a sphere, latitude circles shrink toward zero at the poles.",
                    "Mapping onto a flat cylinder stretches every latitude circle to full width 2πr.",
                    "This magnifies high-latitude land areas like Greenland.",
                ],
            },
            {
                "question": "A hemispherical bowl has inner radius r = 7 cm (π = 22/7). How many cm³ of soup can it hold?",
                "options": ["718.67 cm³", "1437.33 cm³", "308 cm³", "154 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use Hemisphere Volume V = (2/3)πr³.",
                    "V = (2/3) × (22/7) × 7 × 7 × 7 = (2/3) × 1078.",
                    "V = 2156 / 3 ≈ 718.67 cm³.",
                ],
            },
        ],
    },
    {
        "id": 20,
        "title": "Estimation Applications Quiz",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): Guesstimates, Painted Cubes, Packing & Crow Pitcher (14.6 & Exercises)",
        "is_quiz": True,
        "questions": [
            {
                "question": "A 5×5×5 cube is painted green on all 6 faces and cut into 125 unit cubes. How many unit cubes have EXACTLY 2 painted faces?",
                "options": ["36", "24", "54", "8"],
                "answer": 0,
                "solution_steps": [
                    "2-face painted cubes lie along the 12 edges, excluding the 8 corner cubes.",
                    "Formula: 12(n − 2) with n = 5.",
                    "12 × (5 − 2) = 12 × 3 = 36 unit cubes.",
                ],
            },
            {
                "question": "In the same 5×5×5 painted cube, how many unit cubes have EXACTLY 3 painted faces?",
                "options": ["8 (always the 8 corners)", "12", "27", "54"],
                "answer": 0,
                "solution_steps": [
                    "Only corner cubes touch three outer faces.",
                    "Every cube has exactly 8 corners regardless of n ≥ 2.",
                    "Thus there are 8 three-face painted cubes.",
                ],
            },
            {
                "question": "A cylindrical tub (r = 6 cm, h = 10 cm) of ice cream is served in hemispherical scoops of r = 3 cm. How many scoops fit?",
                "options": ["20 scoops", "10 scoops", "30 scoops", "40 scoops"],
                "answer": 0,
                "solution_steps": [
                    "V_tub = π(6²)(10) = 360π cm³.",
                    "V_scoop = (2/3)π(3³) = 18π cm³.",
                    "Number of scoops = 360π ÷ 18π = 20 scoops.",
                ],
            },
            {
                "question": "When estimating how many tennis balls fit in a classroom, why do we multiply Room Volume by ~0.64 to 0.74?",
                "options": [
                    "To account for sphere packing efficiency and empty void spaces between balls",
                    "Because 36% of the room is walls",
                    "Because tennis balls melt",
                    "To convert cm³ to m³",
                ],
                "answer": 0,
                "solution_steps": [
                    "Identical spheres cannot fill 100% of 3D space without gaps.",
                    "Dense sphere packing fills ~74% (random packing ~64%), leaving ~26%–36% void.",
                    "Multiplying by packing efficiency gives a realistic estimate.",
                ],
            },
            {
                "question": "A cylindrical pitcher of radius 4 cm has 5 cm of empty height to the rim (empty volume = 80π cm³). How many spheres of r = 1 cm (volume 4π/3) raise the water to the rim?",
                "options": ["60 spheres", "80 spheres", "40 spheres", "120 spheres"],
                "answer": 0,
                "solution_steps": [
                    "Empty cylinder volume = π(4²)(5) = 80π cm³.",
                    "One sphere displaces (4/3)π cm³.",
                    "Count = 80π ÷ (4π/3) = 80 × 3 / 4 = 60 spheres.",
                ],
            },
            {
                "question": "A storeroom is 3 m × 2 m × 2 m, and each textbook box is 0.5 m × 0.4 m × 0.25 m (aligned along axes). How many whole boxes fit?",
                "options": ["240 boxes", "400 boxes", "300 boxes", "360 boxes"],
                "answer": 0,
                "solution_steps": [
                    "Along 3 m: 3 / 0.5 = 6; along 2 m: 2 / 0.4 = 5; along 2 m: 2 / 0.25 = 8.",
                    "Multiply the integer counts along each axis: 6 × 5 × 8.",
                    "Total = 240 whole textbook boxes.",
                ],
            },
            {
                "question": "A water tank holds 4.2 m³ of water. How many litres is that?",
                "options": ["4200 L", "420 L", "42 L", "42000 L"],
                "answer": 0,
                "solution_steps": [
                    "1 cubic metre (1 m³) = 1000 litres.",
                    "Multiply 4.2 by 1000.",
                    "4.2 × 1000 = 4200 litres.",
                ],
            },
            {
                "question": "A cylindrical golgappa pot has radius 14 cm and water depth 25 cm (π = 22/7). What is the water volume?",
                "options": ["15,400 cm³", "7,700 cm³", "3,080 cm³", "22,000 cm³"],
                "answer": 0,
                "solution_steps": [
                    "Use V = πr²h.",
                    "V = (22/7) × 14 × 14 × 25 = 616 × 25.",
                    "V = 15,400 cm³ (15.4 litres).",
                ],
            },
            {
                "question": "If a person drinks 3 litres of water daily for 80 years (365 days/yr), roughly how many cubic metres is their lifetime water?",
                "options": ["~87.6 m³", "~8.76 m³", "~876 m³", "~0.87 m³"],
                "answer": 0,
                "solution_steps": [
                    "Total litres = 3 × 365 × 80 = 87,600 L.",
                    "Divide by 1000 L/m³ to convert to cubic metres.",
                    "87,600 ÷ 1000 = 87.6 m³.",
                ],
            },
            {
                "question": "Which Appendix tool helps students physically build cuboids, cones, and pyramids from flat paper?",
                "options": [
                    "Printable fold-out 2D nets on grid paper",
                    "A compass alone",
                    "A 3D telescope",
                    "A thermometer",
                ],
                "answer": 0,
                "solution_steps": [
                    "The Chapter 14 Appendix provides fold-out 2D nets on grid paper.",
                    "Folding along edges transforms 2D faces into 3D cuboids, cubes, cylinders, cones, and pyramids.",
                    "This directly connects surface area (2D net) to volume (enclosed 3D space).",
                ],
            },
        ],
    },
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("hint", _q["solution_steps"][0])
        _q.setdefault("explanation", _q["solution_steps"][-1])

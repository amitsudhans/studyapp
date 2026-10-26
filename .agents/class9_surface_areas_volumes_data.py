# -*- coding: utf-8 -*-
"""
Data module for Class 9 Mathematics Chapter 13: Mensuration: Surface Area and Volume
Syllabus Competencies: CG-5, C-5.1, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

SLIDES = [
    {
        "id": 1,
        "title": "Cuboids in Real Life: Anatomy, Surface Area & Volume",
        "subtitle": "Rectangular Prisms, 6 Faces, 12 Edges, 8 Vertices & 3D Interior Capacity",
        "category": "Cuboids & Cubes",
        "badge": "CG-5 • 3D Boundary & Volume",
        "summary": "A cuboid (rectangular parallelepiped) is a three-dimensional closed solid bounded by six rectangular faces. Any two opposite faces are parallel and congruent. A cuboid has 6 faces, 12 edges, and 8 vertices. If length, breadth, and height are denoted by l, b, and h: (1) Total Surface Area: TSA = 2(lb + bh + hl), measuring the combined area of all 6 faces. (2) Lateral Surface Area (Area of 4 vertical walls): LSA = 2h(l + b). (3) Volume (Interior Capacity): V = l · b · h, measuring the 3D space enclosed in cubic units ([L³]). (4) Space Diagonal: d = √(l² + b² + h²), representing the longest rigid rod that can fit inside the cuboid. Real-world applications include freight shipping containers, brick masonry, room painting/whitewashing, and water tank capacities.",
        "key_points": [
            "Cuboid Anatomy: 6 rectangular faces, 12 straight edges, and 8 vertices; opposite faces are congruent.",
            "Total Surface Area: TSA = 2(lb + bh + hl) in square units ([L²]).",
            "Lateral Surface Area: LSA = 2(l + b)h, equivalent to base perimeter times vertical height.",
            "Volume of Cuboid: V = l · b · h in cubic units ([L³]); measures 3D space occupancy and capacity.",
            "Internal Space Diagonal: d = √(l² + b² + h²), derived via double application of Pythagoras' theorem."
        ],
        "narration": "Welcome to Surface Area and Volume! We now step from the flat two-dimensional world into three-dimensional space! Think of cereal boxes, brick buildings, and shipping containers—they are all cuboids. To wrap a cuboid, you need its Total Surface Area, two times lb plus bh plus hl. To fill it with grain or water, you need its Volume, length times breadth times height. Explore our 3D box unfurler to see all six faces unroll into a flat net!",
        "sim_title": "3D Cuboid Unfolder to 2D Net & Volume Unit Cube Meter",
        "checkpoints": [
            {
                "q": "What is the total surface area of a cuboid with length 10 cm, breadth 6 cm, and height 4 cm?",
                "options": ["124 cm²", "248 cm²", "240 cm²", "312 cm²"],
                "ans": 1,
                "exp": "TSA = 2(lb + bh + hl) = 2(10×6 + 6×4 + 4×10) = 2(60 + 24 + 40) = 2(124) = 248 cm²."
            },
            {
                "q": "What is the length of the longest pole that can be placed in a room of dimensions 12 m × 9 m × 8 m?",
                "options": ["15 m", "17 m", "19 m", "21 m"],
                "ans": 1,
                "exp": "The longest pole is the space diagonal d = √(l² + b² + h²) = √(12² + 9² + 8²) = √(144 + 81 + 64) = √289 = 17 m."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Cube: A Special Case of a Cuboid",
        "subtitle": "Applying the Equilateral Constraint l = b = h = a to 3D Prisms",
        "category": "Cuboids & Cubes",
        "badge": "CG-9 • Specialisation in 3D",
        "summary": "A cube is a regular hexahedron where all three linear dimensions are equal: length = breadth = height = a. It is a direct mathematical specialization of the general cuboid. Substituting l = b = h = a into the cuboid formulas yields: (1) Total Surface Area: TSA = 2(a·a + a·a + a·a) = 2(3a²) = 6a² (composed of 6 identical square faces). (2) Lateral Surface Area: LSA = 2a(a + a) = 4a² (the 4 vertical square walls). (3) Volume: V = a · a · a = a³. (4) Space Diagonal: d = √(a² + a² + a²) = a√3. In manufacturing and gaming, dice, Rubik's cubes, and sugar cubes represent uniform cubic geometry where edge symmetries maximize structural and rotational uniformity.",
        "key_points": [
            "Cube Definition: A regular cuboid with all 12 edge lengths equal to a (l = b = h = a).",
            "Surface Area Formulas: Total Surface Area TSA = 6a²; Lateral Surface Area LSA = 4a².",
            "Volume of Cube: V = a³; scales cubically with edge length.",
            "Cube Space Diagonal: d = a√3 ≈ 1.732 a, connecting diametrically opposed opposite vertices.",
            "Special Case Concept: Demonstrates how setting parameter equality reduces 3-variable formulas to single-variable powers."
        ],
        "narration": "What happens when you squeeze a rectangular brick until its length, breadth, and height are all perfectly identical? You get a cube! Because all six faces become identical squares of side a, the total surface area simplifies directly to 6 a-squared, and the volume becomes a-cubed. Notice how the space diagonal reduces from the square root of l-squared plus b-squared plus h-squared to a times root 3. Drag our constraint slider to watch a brick morph into a cube!",
        "sim_title": "Cuboid-to-Cube Constraint Lock Morph & Isometric Dissector",
        "checkpoints": [
            {
                "q": "If the total surface area of a cube is 294 cm², what is the length of each edge?",
                "options": ["6 cm", "7 cm", "8 cm", "9 cm"],
                "ans": 1,
                "exp": "TSA = 6a² = 294 ⇒ a² = 294 / 6 = 49 ⇒ a = √49 = 7 cm."
            },
            {
                "q": "If the edge of a cube is doubled from a to 2a, by what factor does its volume increase?",
                "options": ["2 times", "4 times", "6 times", "8 times"],
                "ans": 3,
                "exp": "Initial volume V1 = a³. New volume V2 = (2a)³ = 8a³ = 8 V1. The volume increases by a factor of 2³ = 8."
            }
        ]
    },
    {
        "id": 3,
        "title": "Right Circular Cylinders: Formation, Radius & Height",
        "subtitle": "Revolution of a Rectangle, Circular Bases & The Curved Surface Net",
        "category": "Cylinders",
        "badge": "CG-5 • C-5.1 • Cylinder Geometry",
        "summary": "A right circular cylinder is a three-dimensional solid generated by revolving a rectangle of dimensions r × h through 360° around one of its sides (the axis of revolution). It consists of two parallel, congruent circular bases of radius r, separated by perpendicular height h. Slicing the curved lateral boundary vertically and flattening it unrolls into a single rectangle whose length equals the base circumference 2πr and width equals height h. (1) Curved Surface Area: CSA = 2πrh. (2) Total Surface Area: TSA = CSA + 2(Base Area) = 2πrh + 2πr² = 2πr(h + r). Daily life examples: food cans, oil drums, road rollers (area leveled per revolution = 2πrh), and architectural columns.",
        "key_points": [
            "Axis of Revolution: Generated by revolving a rectangle around one fixed side through a complete 360° turn.",
            "Curved Surface Net: Unfurls into an exact rectangle of dimensions length = 2π r and height = h.",
            "Curved Surface Area (CSA): CSA = 2π r h in square units.",
            "Total Surface Area (TSA): TSA = 2π r h + 2π r² = 2π r(h + r), enclosing both flat circular end-caps.",
            "Kinematics: A road roller of radius r and width h levels an area equal to 2π r h in one complete rotation."
        ],
        "narration": "Look at an ordinary soda can or oil drum: that is a right circular cylinder! How is it formed? Imagine revolving a rectangle of width r and height h around one edge: it sweeps out a solid cylinder! Now, slice the curved label off the can and lay it flat: it becomes a rectangle whose length is the circle's circumference, 2πr, and height h. That is why the curved surface area is simply 2πrh. Add the two circular lids to get the total surface area: 2πr(h + r)!",
        "sim_title": "Cylinder Revolution Generator & Curved Surface Net Unroller",
        "checkpoints": [
            {
                "q": "A cylindrical pillar has a diameter of 50 cm and height 3.5 m. What is its curved surface area? (Use π = 22/7)",
                "options": ["4.5 m²", "5.5 m²", "6.5 m²", "7.5 m²"],
                "ans": 1,
                "exp": "r = d/2 = 25 cm = 0.25 m = 1/4 m; h = 3.5 m = 7/2 m. CSA = 2πrh = 2 × (22/7) × (1/4) × (7/2) = 11/2 = 5.5 m²."
            },
            {
                "q": "When the curved surface of a cylinder of radius r and height h is unrolled, what shape does it form?",
                "options": [
                    "A circle of radius r",
                    "A rectangle of length 2πr and width h",
                    "A triangle of base 2πr and height h",
                    "A sector of central angle 180°"
                ],
                "ans": 1,
                "exp": "The curved boundary unrolls into a rectangle whose length is the circumference of the circular base (2πr) and whose width is the height of the cylinder (h)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Volume of Right Circular Cylinders & Hollow Pipes",
        "subtitle": "Base Area Extrusion, Capacity Metrics & Concentric Hollow Shells",
        "category": "Cylinders",
        "badge": "CG-5 • Cylindrical Capacity",
        "summary": "The volume of any uniform right cylinder is the area of its cross-sectional base extruded through its perpendicular height: Volume = Base Area × Height = πr²h. Capacity metric relationships: 1 m³ = 1,000 litres; 1,000 cm³ = 1 litre; 1 cm³ = 1 ml. For a hollow cylinder (such as a metal pipe or drainage conduit) with inner radius r, outer radius R, and length h: (1) Volume of metal material: V = π(R² - r²)h. (2) Total Surface Area of hollow pipe: TSA = External CSA + Internal CSA + Area of 2 circular end rings = 2πRh + 2πrh + 2π(R² - r²) = 2π(R + r)h + 2π(R² - r²).",
        "key_points": [
            "Volume Formula: V = π r² h, derived as continuous extrusion of circular disc area π r² along height h.",
            "Liquid Capacity Conversions: 1 m³ = 1,000 L; 1 L = 1,000 cm³ = 1,000 ml; 1 cm³ = 1 ml.",
            "Hollow Pipe Metal Volume: V_material = π(R² - r²)h, subtracting inner hollow cylinder from outer cylinder.",
            "Hollow Pipe Total Surface: TSA = 2π(R + r)h + 2π(R² - r²), including both curved walls and end rings.",
            "Industrial Application: Calculating water tank storage, pipe weights, and well embankment earth excavation."
        ],
        "narration": "To find how much liquid a cylindrical tank holds, we use the principle of cross-sectional extrusion: stack infinitely many circular pancakes of area πr² on top of each other up to height h! The volume is πr²h. Remember that 1,000 cubic centimeters equals exactly one liter. For hollow pipes, subtract the inner hollow core from the outer cylinder to find the metal volume. Test our interactive liquid capacity filler!",
        "sim_title": "Cylindrical Liquid Reservoir Filler & Hollow Pipe Material Meter",
        "checkpoints": [
            {
                "q": "A cylindrical water tank has radius 1.4 m and height 5 m. How many litres of water can it hold? (Use π = 22/7)",
                "options": ["15,400 L", "30,800 L", "46,200 L", "61,600 L"],
                "ans": 1,
                "exp": "V = πr²h = (22/7) × (1.4)² × 5 = (22/7) × 1.96 × 5 = 22 × 0.28 × 5 = 30.8 m³. Capacity in litres = 30.8 × 1000 = 30,800 L."
            },
            {
                "q": "A hollow iron pipe of length 20 cm has an outer diameter of 16 cm and inner diameter of 12 cm. What is the volume of iron in the pipe? (Use π = 3.14)",
                "options": ["1456 cm³", "1758.4 cm³", "2198 cm³", "2480 cm³"],
                "ans": 1,
                "exp": "R = 8 cm, r = 6 cm. V = π(R² - r²)h = 3.14 × (64 - 36) × 20 = 3.14 × 28 × 20 = 3.14 × 560 = 1758.4 cm³."
            }
        ]
    },
    {
        "id": 5,
        "title": "Right Circular Cones: Daily Life, Slant Height & Apex",
        "subtitle": "Revolving a Right Triangle: Radius r, Vertical Height h & Slant Hypotenuse l",
        "category": "Cones",
        "badge": "CG-5 • Cone Anatomy",
        "summary": "A right circular cone is a three-dimensional solid formed by revolving a right-angled triangle around one of its legs through 360°. The fixed leg forms the vertical height h (axis of the cone), the other leg forms the radius r of the circular base, and the hypotenuse sweeps out the curved lateral boundary, forming the slant height l. By the Pythagorean theorem: l² = r² + h² ⇒ l = √(r² + h²). The highest single point where the curved lateral surface converges is called the apex (vertex). Daily life occurrences: ice-cream cones, conical traffic cones, funnel filters, clown hats, sharpened pencil tips, and circus canvas tents (shamianas).",
        "key_points": [
            "Right Triangle Generator: Formed by revolving a right triangle of legs r and h around vertical leg h.",
            "Apex & Base: Converges to a single pointed apex directly over the centre of the circular base.",
            "Slant Height Equation: l = √(r² + h²), derived directly via Pythagoras on cross-sectional triangle ΔOAP.",
            "Physical Meaning of Slant Height: The shortest straight line distance along the outer surface from apex to rim.",
            "Real-World Recognition: Conical party hats, funnels, volcanic cones, conical grain piles, and circus tents."
        ],
        "narration": "From ice-cream cones to birthday party hats and traffic cones, conical geometry is everywhere! How is a right circular cone born? Take a right-angled triangle with legs r and h, and spin it around its vertical leg: the hypotenuse sweeps out the cone's curved surface, becoming the slant height, l. Because of Pythagoras, l equals the square root of r-squared plus h-squared. Watch our 3D right triangle spin to generate a cone!",
        "sim_title": "Right Triangle Revolution Simulator & Slant Height Pythagorean Lock",
        "checkpoints": [
            {
                "q": "What is the slant height of a right circular cone whose base radius is 7 cm and vertical height is 24 cm?",
                "options": ["25 cm", "26 cm", "28 cm", "31 cm"],
                "ans": 0,
                "exp": "l = √(r² + h²) = √(7² + 24²) = √(49 + 576) = √625 = 25 cm."
            },
            {
                "q": "If the slant height l of a cone is 10 cm and its base radius r is 6 cm, what is its vertical height h?",
                "options": ["7 cm", "8 cm", "9 cm", "12 cm"],
                "ans": 1,
                "exp": "h = √(l² - r²) = √(10² - 6²) = √(100 - 36) = √64 = 8 cm."
            }
        ]
    },
    {
        "id": 6,
        "title": "Surface Area of a Cone: Unrolling the Conical Net",
        "subtitle": "Dissecting the Curved Wall into a Sector of Radius l (CSA = πrl)",
        "badge": "CG-5 • Cone Surface Area",
        "summary": "If you slice a cone along its slant height l and unroll its curved surface flat onto a table, it forms a sector of a circle! The radius of this unrolled sector is the slant height l, and its curved outer arc length is exactly equal to the circumference of the cone's circular base, 2πr. Recall from sector geometry: Area = (1/2) × arc length × radius = (1/2) × (2πr) × l = πrl! Therefore: (1) Curved Surface Area (CSA): CSA = πrl. (2) Total Surface Area (TSA): TSA = CSA + Base Area = πrl + πr² = πr(l + r). When designing conical tents, only the curved canvas CSA = πrl is required since the floor is ground.",
        "key_points": [
            "Conical Net Dissection: Slicing along slant height l unrolls the curved wall into a circular sector of radius l.",
            "Arc Length Equality: The unrolled sector's curved boundary equals the base circumference 2π r.",
            "CSA Derivation: Sector Area = (1/2) · (2π r) · l = π r l in square units.",
            "Total Surface Area: TSA = π r l + π r² = π r(l + r), adding the flat circular bottom disc.",
            "Fabric Optimization: Calculating canvas required for conical tents without including the ground floor."
        ],
        "narration": "How do you calculate the canvas needed for a conical tent? Slice the cone open along its slant height and flatten it out: surprise! It becomes a circular sector with radius l and curved edge equal to the base circle, 2πr. Using our sector area formula—one half times base arc times radius—we get one half times 2πr times l, which simplifies to the famous formula: πrl! Add the bottom circular floor to get the total surface area: πr(l + r). Watch our cone unfurl into a flat sector!",
        "sim_title": "Conical Net Unroller to Circular Sector & Fabric Calculator",
        "checkpoints": [
            {
                "q": "What is the curved surface area of a conical tent with base radius 7 m and slant height 10 m? (Use π = 22/7)",
                "options": ["110 m²", "154 m²", "220 m²", "374 m²"],
                "ans": 2,
                "exp": "CSA = πrl = (22/7) × 7 × 10 = 220 m²."
            },
            {
                "q": "What is the total surface area of a cone of radius 6 cm and slant height 14 cm? (Use π = 22/7)",
                "options": ["264 cm²", "377.14 cm²", "440 cm²", "528 cm²"],
                "ans": 1,
                "exp": "TSA = πr(l + r) = (22/7) × 6 × (14 + 6) = (22/7) × 6 × 20 = 2640 / 7 ≈ 377.14 cm²."
            }
        ]
    },
    {
        "id": 7,
        "title": "Volume of a Cone: The 1/3 Cylinder Relationship",
        "subtitle": "Experimental Verification: 3 Cones of Water Fill Exactly 1 Matching Cylinder",
        "category": "Cones",
        "badge": "CG-5 • Cone Volume Ratio",
        "summary": "The volume of a right circular cone is exactly one-third the volume of a right circular cylinder having the same base radius r and vertical height h: Volume = (1/3)πr²h. This fundamental relationship can be verified experimentally: taking a hollow cone and a hollow cylinder of identical radius r and height h, filling the cone with water or sand and pouring it into the cylinder requires exactly THREE full cones to fill the cylinder to its brim! Practical applications: granular materials (sand, grain, gravel) dumped from conveyors naturally form conical piles whose volumes are evaluated using V = (1/3)πr²h.",
        "key_points": [
            "Volume Formula: V = (1/3) π r² h, one-third of the enclosing cylinder of identical dimensions.",
            "The 3:1 Pouring Ratio: Exactly 3 full cones of liquid or sand are required to completely fill the matching cylinder.",
            "Dependence on Vertical Height: Volume depends strictly on perpendicular vertical height h, NOT slant height l.",
            "Granular Heaps: Stockpiled grain and mining slag naturally form cones dictated by the angle of repose.",
            "Dimensional Comparison: With equal base and height, Prism : Pyramid = 3 : 1; Cylinder : Cone = 3 : 1."
        ],
        "narration": "Here is one of the most elegant facts in all of mathematics: a cone has exactly one-third the volume of a cylinder with the same radius and height! If you fill a cone with sand and pour it into a matching cylinder, the cylinder is only one-third full. Pour a second cone, it reaches two-thirds. Pour a third cone, and it fills the cylinder perfectly to the top! That is why the volume of a cone is one-third πr²h. Click 'Pour Cone' in our simulator to run this classic experiment!",
        "sim_title": "Interactive 3-Cone Pouring Experiment to Matching Cylinder",
        "checkpoints": [
            {
                "q": "Find the volume of a right circular cone with radius 6 cm and height 7 cm. (Use π = 22/7)",
                "options": ["132 cm³", "264 cm³", "396 cm³", "792 cm³"],
                "ans": 1,
                "exp": "V = (1/3)πr²h = (1/3) × (22/7) × 6² × 7 = (1/3) × (22/7) × 36 × 7 = (1/3) × 22 × 36 = 22 × 12 = 264 cm³."
            },
            {
                "q": "A cylindrical vessel and a conical vessel have identical base radius and height. If the cylinder holds 1500 ml of liquid, how much does the cone hold?",
                "options": ["300 ml", "500 ml", "750 ml", "1000 ml"],
                "ans": 1,
                "exp": "V_cone = (1/3) × V_cylinder = 1500 / 3 = 500 ml."
            }
        ]
    },
    {
        "id": 8,
        "title": "Pyramids in Architecture: Base, Slant Height & Apex",
        "subtitle": "Polygonal Bases, Triangular Lateral Faces & Vertical vs Slant Heights",
        "category": "Pyramids",
        "badge": "CG-5 • Pyramid Geometry",
        "summary": "A pyramid is a three-dimensional polyhedron whose base is a polygon (triangle, square, rectangle, or regular n-gon) and whose lateral faces are triangles meeting at a single common vertex called the apex. In a right regular pyramid, the base is a regular polygon and the apex lies vertically above the centre of the base. Key metric distinctions: (1) Vertical height h: Perpendicular distance from apex to base center. (2) Slant height l: Altitude of each triangular lateral face from apex to base edge midpoint. For a regular square pyramid of base side a: l = √[h² + (a/2)²]. (3) Lateral edge e: Distance from apex to a base corner vertex: e = √[l² + (a/2)²]. Architectural marvels: The Great Pyramid of Giza (Egypt), the Louvre Glass Pyramid (Paris), and pagoda roofs.",
        "key_points": [
            "Pyramid Definition: Polyhedron with a polygonal base and triangular lateral faces meeting at a single apex.",
            "Regular Square Pyramid: Base is a square a × a; 4 congruent isosceles triangle lateral faces.",
            "Slant Height Equation: l = √[h² + (a/2)²], measuring the altitude along the sloping triangular faces.",
            "Apex Convergence: All lateral edges meet at a single shared summit point.",
            "Architectural Stability: Pyramidal mass distribution has a low center of gravity, enduring for millennia."
        ],
        "narration": "Think of the colossal Great Pyramid of Giza, built over 4,500 years ago! A pyramid has a flat polygon base—like a square—and triangular faces that slope upward to meet at a single pointed apex. But be careful not to confuse the vertical height inside the tomb with the slant height along the outside face! Because the slant height is the hypotenuse of the triangle inside, l equals the square root of h-squared plus (a/2)-squared. Explore our 3D pyramid net as its four triangular walls drop open!",
        "sim_title": "3D Square Pyramid Net Unfolder & Slant Height Geometry",
        "checkpoints": [
            {
                "q": "In a right regular square pyramid with base side a = 12 m and vertical height h = 8 m, what is the slant height l?",
                "options": ["9 m", "10 m", "12 m", "14 m"],
                "ans": 1,
                "exp": "Half-side of base = a/2 = 6 m. Slant height l = √[h² + (a/2)²] = √(8² + 6²) = √(64 + 36) = √100 = 10 m."
            },
            {
                "q": "How many total faces, edges, and vertices does a square pyramid have?",
                "options": [
                    "4 faces, 6 edges, 4 vertices",
                    "5 faces, 8 edges, 5 vertices",
                    "6 faces, 10 edges, 6 vertices",
                    "6 faces, 12 edges, 8 vertices"
                ],
                "ans": 1,
                "exp": "A square pyramid has 1 square base + 4 triangular faces = 5 faces; 4 base edges + 4 lateral edges = 8 edges; 4 base vertices + 1 apex = 5 vertices."
            }
        ]
    },
    {
        "id": 9,
        "title": "Surface Area & Volume of a Pyramid",
        "subtitle": "Cube Dissection into 6 Pyramids & The Master Formula V = (1/3) B h",
        "category": "Pyramids",
        "badge": "CG-5 • CG-9 • Pyramid Mensuration",
        "summary": "For any regular pyramid with base perimeter P, base area B, vertical height h, and slant height l: (1) Lateral Surface Area (LSA): LSA = (1/2) × Perimeter of Base × slant height = (1/2) P l. For a square pyramid: LSA = 4 × [(1/2) a l] = 2al. (2) Total Surface Area (TSA): TSA = Base Area + LSA = a² + 2al. (3) Volume of ANY Pyramid: V = (1/3) × Base Area × Height = (1/3) B h. Geometric Dissection Proof: A solid cube of edge a can be partitioned into exactly SIX congruent square pyramids with their vertices meeting at the cube's central point! Each pyramid has base a² and height h = a/2. Total volume of 6 pyramids = a³, so Volume of 1 pyramid = (1/6)a³ = (1/6)a²(2h) = (1/3)a²h = (1/3) B h!",
        "key_points": [
            "Lateral Surface Area: LSA = (1/2) · P · l, summing the areas of all n triangular lateral faces.",
            "Total Surface Area: TSA = Base Area + (1/2) · P · l = a² + 2al for a square pyramid.",
            "Universal Pyramid Volume: V = (1/3) · Base Area · Height = (1/3) B h for any polygon base.",
            "Cube Dissection Proof: A cube partitions into 6 identical pyramids meeting at center O, proving V = (1/6) a³ = (1/3) B h.",
            "Cross-Discipline Unity: The factor 1/3 applies equally to circular cones and polygonal pyramids."
        ],
        "narration": "Why is the volume of every pyramid one-third base area times height? Here is a proof that will blow your mind! Take a solid cube and draw diagonals from its center to all eight corners: the cube splits into exactly SIX identical square pyramids! Since all six together make up the cube's volume a-cubed, and the height of each pyramid is half the cube's edge, one pyramid's volume is exactly one-third base area times height! Click 'Disassemble Cube' to watch the cube explode into six pyramids!",
        "sim_title": "6-Pyramid Cube Dissection Explosion & Volume Equivalence",
        "checkpoints": [
            {
                "q": "What is the volume of a square pyramid with base edge 10 cm and vertical height 12 cm?",
                "options": ["200 cm³", "400 cm³", "600 cm³", "1200 cm³"],
                "ans": 1,
                "exp": "Base area B = a² = 10² = 100 cm². Volume V = (1/3) B h = (1/3) × 100 × 12 = 100 × 4 = 400 cm³."
            },
            {
                "q": "What is the total surface area of a square pyramid with base side 10 cm and slant height 13 cm?",
                "options": ["260 cm²", "360 cm²", "420 cm²", "520 cm²"],
                "ans": 1,
                "exp": "Base area = 10² = 100 cm². LSA = 2al = 2 × 10 × 13 = 260 cm². TSA = Base + LSA = 100 + 260 = 360 cm²."
            }
        ]
    },
    {
        "id": 10,
        "title": "Spheres in Nature & Geometry: Center and Radius",
        "subtitle": "The Perfectly Isotropic 3D Surface Equidistant from a Single Point",
        "category": "Spheres",
        "badge": "CG-5 • C-5.1 • Sphere Geometry",
        "summary": "A sphere is the set of all points in three-dimensional space situated at a constant distance (radius r) from a fixed interior point (the center O). The distance between any two diametrically opposed surface points passing through O is the diameter d = 2r. The sphere is the most symmetrical geometric object in the universe: it possesses point reflection symmetry through its center, rotational symmetry of every degree around every axis, and reflection symmetry across every plane passing through its center. The cross-section of a sphere cut by a plane passing through its center is called a Great Circle (radius r, area = πr²). Nature adopts spheres because surface tension naturally minimizes surface area for a given volume (soap bubbles, raindrops, planets).",
        "key_points": [
            "Sphere Definition: The locus of points in 3D space equidistant (r) from a central point O (x² + y² + z² = r²).",
            "Universal Isotropic Symmetry: Infinite planes and axes of symmetry; perfectly uniform in all directions.",
            "Great Circle: The largest possible circle on a sphere, created by slicing through the center (Area = π r²).",
            "Small Circles: Cross-sections formed by planes that do not pass through the center.",
            "Physical Optimization: Surface tension pulls liquids into spheres because a sphere encloses maximum volume with minimum surface area."
        ],
        "narration": "From soap bubbles floating in air to planets and stars orbiting in space, nature loves spheres! Why? Because surface tension always pulls liquids into the shape that has the absolute smallest surface area for a given volume: a sphere! Every single point on its surface is at the exact same distance r from the center. Slicing right through the center produces a Great Circle, like the Earth's equator. Spin our 3D wireframe sphere and slice it with planes!",
        "sim_title": "3D Wireframe Sphere Rotator & Great Circle Slicer",
        "checkpoints": [
            {
                "q": "What is the cross-section of a sphere cut by any plane passing through its center called?",
                "options": ["A Small Circle", "A Great Circle", "A Parabola", "An Ellipsoid"],
                "ans": 1,
                "exp": "A cross-section through the center of a sphere is called a Great Circle; its radius equals the sphere's radius r and its area is πr²."
            },
            {
                "q": "Why do raindrops and soap bubbles naturally form spherical shapes?",
                "options": [
                    "Because spheres weigh less than other shapes",
                    "Because surface tension minimizes surface energy by adopting the shape of minimum surface area for a given volume",
                    "Because gravity pushes only in straight lines",
                    "Because air resistance forces 90° angles"
                ],
                "ans": 1,
                "exp": "Surface tension pulls liquid molecules together to minimize surface area; the sphere mathematically achieves the lowest surface area per unit volume."
            }
        ]
    },
    {
        "id": 11,
        "title": "Surface Area of a Sphere: Archimedes' Cylinder & 4 Discs",
        "subtitle": "Archimedes' Hat-Box Theorem: Area Equals Exactly 4 Great Circles (4πr²)",
        "category": "Spheres",
        "badge": "CG-5 • Sphere Surface Area",
        "summary": "The total surface area of a sphere of radius r is given by: TSA = 4πr². Physical Demonstration (The 4 Discs): If you wrap a cord tightly around the curved boundary of a hemisphere and then uncoil it, the cord covers exactly two flat circular discs of radius r; for the entire sphere, it covers exactly FOUR flat circular discs of area πr²! Archimedes' Hat-Box Theorem: Archimedes proved that the surface area of a sphere of radius r equals the curved lateral surface area of a circumscribing cylinder with the same radius r and height equal to the sphere's diameter h = 2r: CSA_cylinder = 2πr × h = 2πr × (2r) = 4πr²! Any zone of the sphere between two parallel planes has the exact same surface area as the corresponding zone on the cylinder.",
        "key_points": [
            "Surface Area Formula: TSA = 4π r² in square units, exactly four times the area of its great circle.",
            "The 4-Disc Equivalence: The outer skin of a sphere unwinds to cover four flat circles of radius r.",
            "Archimedes' Hat-Box Theorem: A sphere has the exact same surface area as the lateral wall of its bounding cylinder (2π r · 2r = 4π r²).",
            "Zone Projection Invariance: The surface area of any horizontal slice depends only on the slice height Δh: Area = 2π r Δh.",
            "Coating Costs: Calculating paint or plating required for spherical domes, storage tanks, and ball bearings."
        ],
        "narration": "How did Archimedes discover the surface area of a sphere without modern calculus? He found something astonishing: if you slide a sphere inside a snug cylinder of height 2r, the surface area of the sphere exactly equals the curved wall of the cylinder! The cylinder's curved area is 2πr times 2r, which is 4πr-squared! This means the surface of a sphere is equal to exactly FOUR flat circular discs of radius r. Watch our interactive simulator peel the sphere's skin into four flat circles!",
        "sim_title": "Archimedes' Hat-Box Projection & 4-Disc Skin Peeling Simulator",
        "checkpoints": [
            {
                "q": "What is the surface area of a sphere of radius 7 cm? (Use π = 22/7)",
                "options": ["154 cm²", "308 cm²", "616 cm²", "1232 cm²"],
                "ans": 2,
                "exp": "TSA = 4πr² = 4 × (22/7) × 7² = 4 × 22 × 7 = 616 cm²."
            },
            {
                "q": "According to Archimedes, the surface area of a sphere of radius r equals the lateral curved surface area of a cylinder of radius r and height:",
                "options": ["r", "2r", "πr", "4r"],
                "ans": 1,
                "exp": "The circumscribing cylinder has height equal to the sphere's diameter, h = 2r. Its lateral area is 2πr(2r) = 4πr²."
            }
        ]
    },
    {
        "id": 12,
        "title": "Volume of a Sphere: Archimedes’ 2/3 Ratio",
        "subtitle": "The Tombstone Inscription: Sphere Volume is 2/3 of its Circumscribing Cylinder",
        "category": "Spheres",
        "badge": "CG-5 • Sphere Volume",
        "summary": "The volume of a sphere of radius r is given by: Volume = (4/3)πr³. Archimedes considered this his greatest mathematical triumph, requesting a sphere inscribed in a cylinder to be engraved upon his tombstone. He proved that the volume of a sphere is exactly TWO-THIRDS the volume of its circumscribing cylinder: V_cylinder = Base Area × Height = (πr²) × (2r) = 2πr³. Therefore: V_sphere = (2/3) × V_cylinder = (2/3)(2πr³) = (4/3)πr³! Infinitesimal Pyramid Summation: We can also imagine partitioning the sphere into millions of microscopic pyramids whose apexes meet at the center O: each has base ΔA and height r, with volume (1/3) ΔA · r. Summing: V = (1/3) r Σ ΔA = (1/3) r (4πr²) = (4/3)πr³.",
        "key_points": [
            "Volume Formula: V = (4/3) π r³ in cubic units, proportional to the cube of the radius.",
            "Archimedes' Tombstone Ratio: Sphere volume is exactly 2/3 of its bounding cylinder (2/3 · 2π r³ = 4/3 π r³).",
            "The 1:2:3 Volume Balance: Cone (1/3 · 2πr³ = 2/3 πr³) + Sphere (4/3 πr³) = Cylinder (2πr³).",
            "Infinitesimal Pyramids: Summing infinite pyramid wedges of height r and base sum 4πr² yields (1/3)r(4πr²) = (4/3)πr³.",
            "Weight and Mass: Calculating the payload of weather balloons, planet masses, and steel ball bearing weights."
        ],
        "narration": "Archimedes was so proud of discovering the volume of a sphere that he asked for a sphere inside a cylinder to be carved onto his gravestone! He proved that a sphere holds exactly two-thirds the volume of the cylinder around it. Two-thirds times 2πr-cubed gives the famous formula: four-thirds πr-cubed! Furthermore, a cone plus a sphere equals the cylinder: one plus two equals three! Check out our Archimedean volume balance scale in action.",
        "sim_title": "Archimedean Tombstone 1:2:3 Volume Balance Scale",
        "checkpoints": [
            {
                "q": "Find the volume of a sphere of radius 3 cm. (Use π = 3.14)",
                "options": ["37.68 cm³", "84.78 cm³", "113.04 cm³", "339.12 cm³"],
                "ans": 2,
                "exp": "V = (4/3)πr³ = (4/3) × 3.14 × 27 = 4 × 3.14 × 9 = 113.04 cm³."
            },
            {
                "q": "If the diameter of a sphere is reduced by half, what fraction of its original volume remains?",
                "options": ["1/2", "1/4", "1/6", "1/8"],
                "ans": 3,
                "exp": "Halving the diameter halves the radius (r → r/2). Volume scales cubically: (1/2)³ = 1/8th of the original volume."
            }
        ]
    },
    {
        "id": 13,
        "title": "Hemispheres: Curved Surface, Flat Base & Solid TSA",
        "subtitle": "Bisection Across a Great Circle: CSA = 2πr², Flat Base = πr² & Solid TSA = 3πr²",
        "category": "Hemispheres",
        "badge": "CG-5 • Hemispherical Metrics",
        "summary": "When a plane cuts a sphere through its center, it divides it into two congruent halves called hemispheres. For a hemisphere of radius r: (1) Curved Surface Area (CSA): CSA = (1/2) × 4πr² = 2πr². (2) Flat Base: A circular disc of area πr². (3) Total Surface Area of a SOLID Hemisphere: TSA = CSA + Flat Base = 2πr² + πr² = 3πr²! (4) Volume of a Hemisphere: V = (1/2) × (4/3)πr³ = (2/3)πr³. For a hollow hemispherical bowl with inner radius r and outer radius R: Internal CSA = 2πr²; External CSA = 2πR²; Ring Rim Area = π(R² - r²); Total Surface Area = 2πR² + 2πr² + π(R² - r²); Material Volume = (2/3)π(R³ - r³). Daily examples: hemispherical bowls, planetarium observatory domes, igloos, and radar domes.",
        "key_points": [
            "Hemisphere Definition: Half of a sphere created by bisection across a great circle plane.",
            "Curved Surface Area: CSA = 2π r², exactly half of the full sphere's outer skin.",
            "Solid Total Surface Area: TSA = 2π r² + π r² = 3π r², accounting for the flat circular base.",
            "Volume of Hemisphere: V = (2/3) π r³ in cubic units, exactly half of the sphere's volume.",
            "Hollow Bowl Geometry: Accounting for internal curved wall, external wall, circular rim, and shell thickness."
        ],
        "narration": "What happens when you cut a solid wooden ball right through the middle? You get two hemispheres! Each hemisphere has a dome with curved area 2πr-squared, plus a flat circular bottom of area πr-squared. Add them together, and the total surface area of a solid hemisphere is three πr-squared! But if the hemisphere is a hollow bowl, you must paint both the inside and outside, plus the top circular rim. Toggle between solid and hollow modes on our hemisphere lab!",
        "sim_title": "Solid vs. Hollow Hemisphere 3D Dissector & Rim Meter",
        "checkpoints": [
            {
                "q": "What is the total surface area of a SOLID hemisphere of radius 7 cm? (Use π = 22/7)",
                "options": ["308 cm²", "462 cm²", "616 cm²", "924 cm²"],
                "ans": 1,
                "exp": "Solid TSA = 3πr² = 3 × (22/7) × 7² = 3 × 22 × 7 = 462 cm²."
            },
            {
                "q": "A hemispherical bowl has an internal radius of 9 cm. What is the volume of soup it can hold? (Use π = 3.14)",
                "options": ["763.02 cm³", "1017.36 cm³", "1526.04 cm³", "3052.08 cm³"],
                "ans": 2,
                "exp": "Volume = (2/3)πr³ = (2/3) × 3.14 × 729 = 2 × 3.14 × 243 = 1526.04 cm³."
            }
        ]
    },
    {
        "id": 14,
        "title": "Conversion of Solids: Melting & Recasting Conservation",
        "subtitle": "Invariance of Volume: Transforming Spheres into Wires, Cones & Cylinders",
        "category": "Volume Conservation",
        "badge": "CG-9 • Conservation Principles",
        "summary": "In industrial casting, metallurgy, and civil engineering, solids of one geometric shape are frequently melted, reshaped, or recast into entirely different geometries. Fundamental Law of Conservation: Assuming no material is added, lost, or vaporized during the process, the TOTAL VOLUME of the original solid(s) equals the TOTAL VOLUME of the newly formed solid(s): V_initial = V_final. Common recasting transformations: (1) Melting a large metallic sphere of radius R into n small spheres of radius r: (4/3)πR³ = n × (4/3)πr³ ⇒ n = R³ / r³. (2) Recasting a sphere into a long thin cylindrical wire of length L and radius r_wire: (4/3)πR³ = π(r_wire)² L. (3) Digging a cylindrical well and spreading the excavated earth as an embankment (hollow cylinder).",
        "key_points": [
            "Volume Conservation Law: Total mass and volume remain strictly invariant during melting and recasting (V_1 = V_2).",
            "Surface Area Non-Conservation: While volume remains invariant, the surface area almost always changes dramatically!",
            "Sphere to Small Spheres: The number of balls formed is n = (R / r)³.",
            "Solid to Wire Transformation: Modeled as transforming a solid into an elongated cylinder of cross-sectional area π r² and length L.",
            "Well Embankment Excavation: Volume of dug earth π r² h equals the volume of the hollow embankment ring π(R² - r²)h_emb."
        ],
        "narration": "In metal foundries, blacksmiths melt heavy bronze spheres and pour the molten metal into molds to make long wires, hollow pipes, or hundreds of tiny ball bearings! Here is the golden rule: even though the shape changes completely, the total volume of metal remains strictly conserved! However, beware: the surface area does NOT stay the same—making smaller balls dramatically increases the total surface area! Watch our virtual crucible melt a sphere into ball bearings and wires.",
        "sim_title": "Molten Metal Crucible Recasting & Invariant Volume Engine",
        "checkpoints": [
            {
                "q": "How many small spherical lead shots of radius 1 cm can be made by melting a solid metallic sphere of radius 8 cm?",
                "options": ["64", "256", "512", "1024"],
                "ans": 2,
                "exp": "n = R³ / r³ = 8³ / 1³ = 512 / 1 = 512 lead shots."
            },
            {
                "q": "A metallic sphere of radius 4.2 cm is melted and recast into the shape of a cylinder of radius 6 cm. What is the height of the cylinder? (Use π = 22/7)",
                "options": ["1.88 cm", "2.74 cm", "3.12 cm", "4.20 cm"],
                "ans": 1,
                "exp": "V_cylinder = V_sphere ⇒ π r² h = (4/3)π R³ ⇒ 6² h = (4/3) × (4.2)³ ⇒ 36 h = (4/3) × 74.088 = 98.784 ⇒ h = 98.784 / 36 = 2.744 cm ≈ 2.74 cm."
            }
        ]
    },
    {
        "id": 15,
        "title": "Surface Area-to-Volume Ratio & Scaling Laws",
        "subtitle": "Galileo’s Square-Cube Law: Why Cells are Microscopic & Polar Bears are Large",
        "category": "Scaling Laws",
        "badge": "CG-9 • Scaling & Biological Physics",
        "summary": "The Surface Area-to-Volume ratio (SA/V) governs heat loss, chemical reaction rates, and biological physiology. (1) Cube of edge a: SA/V = (6a²) / a³ = 6/a. (2) Sphere of radius r: SA/V = (4πr²) / ((4/3)πr³) = 3/r. Notice that as an object increases in size, its SA/V ratio decreases inversely! Galileo's Square-Cube Law: When linear dimensions are multiplied by a scale factor k: Linear scale ~ k; Surface Area scales ~ k²; Volume and Mass scale ~ k³! Biological Consequences: (1) Living cells cannot grow indefinitely large because volume (which produces waste/heat) grows faster than surface area (which absorbs oxygen/nutrients). (2) Bergmann's Rule: Polar animals (polar bears, walruses) are large and spherical to minimize heat loss per unit mass.",
        "key_points": [
            "The Inverted Ratio: For a sphere, SA/V = 3/r; for a cube, SA/V = 6/a. Larger objects have smaller SA/V ratios.",
            "Galileo's Square-Cube Law: Surface Area ∝ k² while Volume ∝ k³ under linear scaling k.",
            "Cell Biology Boundary: Cells must stay microscopic (high SA/V) to allow efficient nutrient diffusion across membranes.",
            "Thermodynamics of Heat Loss: Small animals lose body heat rapidly; large Arctic animals have small SA/V to conserve warmth.",
            "Chemical Kinetics: Crushed ice or fine powder dissolves/reacts exponentially faster due to vast aggregate surface area."
        ],
        "narration": "Why are biological cells microscopic? And why are Arctic polar bears so huge and rounded? The answer is Galileo's Square-Cube Law! When you double the size of an animal, its skin area quadruples, but its volume and weight multiply by eight! Because heat is generated by volume and lost through skin, large rounded animals retain heat easily, while tiny mice lose heat so fast they must eat constantly. Drag our scale slider to see the surface area-to-volume ratio plummet as size increases!",
        "sim_title": "Square-Cube Law Scaling Lab & Biological Heat Loss Curve",
        "checkpoints": [
            {
                "q": "If the radius of a sphere is multiplied by 3, what happens to its Surface Area-to-Volume ratio (SA/V)?",
                "options": [
                    "It triples",
                    "It is divided by 3 (becomes 1/3 of original)",
                    "It increases by 9 times",
                    "It remains unchanged"
                ],
                "ans": 1,
                "exp": "For a sphere, SA/V = 3/r. If r increases to 3r, the ratio becomes 3/(3r) = (1/3)(3/r), which is divided by 3."
            },
            {
                "q": "Why does crushed ice cool a drink much faster than a solid block of ice of the exact same mass?",
                "options": [
                    "Crushed ice is at a lower temperature",
                    "Crushed ice has a vastly larger aggregate surface area exposed to the liquid, accelerating heat transfer",
                    "Crushed ice has less mass",
                    "Crushed ice floats deeper"
                ],
                "ans": 1,
                "exp": "Crushing divides the ice into thousands of tiny pieces, dramatically increasing total surface area (SA/V ratio), which speeds up thermal conduction."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: 3D Mensuration & Optimization",
        "subtitle": "Composite Polyhedra Decomposition & Optimal Industrial Can Dimensions (h = 2r)",
        "category": "Computational Optimization",
        "badge": "CG-9 • Algorithmic Optimization",
        "summary": "Computational geometry algorithms compute perimeters, surface areas, and volumes for complex, composite machinery by decomposing them into primitive geometries: V_total = Σ V_primitives. Industrial Packaging Optimization: Consider manufacturing a cylindrical tin can to hold a fixed volume V (e.g., 355 ml). What radius r and height h will MINIMIZE the amount of sheet metal (total surface area TSA = 2πr² + 2πrh) and minimize production cost? Expressing h in terms of V: h = V / (πr²). Substituting gives TSA(r) = 2πr² + (2V / r). Minimizing with respect to r gives: 4πr - (2V / r²) = 0 ⇒ 2V = 4πr³ ⇒ 2(πr²h) = 4πr³ ⇒ h = 2r! Theorem: A cylindrical can minimizes surface area and manufacturing cost precisely when its height equals its diameter (h = 2r)!",
        "key_points": [
            "Decomposition Pipeline: Complex 3D CAD assemblies decompose into primitive solids (cuboid, cylinder, cone, sphere).",
            "Hidden Interface Rule: When two solids are joined, the shared contact faces are subtracted from the total surface area.",
            "Industrial Cost Optimization: Minimizing material usage (TSA) while maintaining required fluid volume V.",
            "The Optimal Can Ratio: Minimum surface area occurs when height equals diameter: h = 2r.",
            "Algorithmic Parameter Sweep: Exploring dimension configurations across 3D simulation spaces."
        ],
        "narration": "How do industrial software engineers design beverage cans to save millions of dollars in aluminum? They use mathematical optimization! If a can must hold exactly 355 milliliters, what dimensions require the absolute least amount of metal? By setting the surface area derivative to zero, mathematics reveals an astonishing universal rule: the height of the can must equal its diameter: h = 2r! Move the radius slider on our can packaging optimizer to see the total metal cost dip to its perfect minimum!",
        "sim_title": "Industrial Beverage Can Metal Optimizer & Cost Minimum Graph",
        "checkpoints": [
            {
                "q": "For a cylindrical can of fixed volume V, what ratio of height h to radius r minimizes the total surface area and metal cost?",
                "options": ["h = r", "h = 2r (height equals diameter)", "h = πr", "h = 4r"],
                "ans": 1,
                "exp": "Minimizing TSA = 2πr² + 2V/r leads to the condition h = 2r, meaning the optimal can has height equal to its diameter."
            },
            {
                "q": "A toy is in the shape of a cone mounted on a hemisphere of the same radius r = 3.5 cm. In computing its total surface area, which surfaces are included?",
                "options": [
                    "Cone TSA + Hemisphere TSA",
                    "Cone CSA + Hemisphere CSA (excluding the hidden circular joint)",
                    "Cone Volume + Hemisphere Volume",
                    "Cone CSA only"
                ],
                "ans": 1,
                "exp": "Because the circular base is fused internally inside the toy, the exterior total surface area is the sum of the curved surface areas: CSA_cone + CSA_hemisphere = πrl + 2πr²."
            }
        ]
    }
]

QUIZZES = [
    # Quiz 1: Slide 17 (Questions 1 to 10: Cuboids, Cubes, Surface Areas, Diagonals & Walls)
    {
        "id": 17,
        "title": "Mastery Challenge I: Cuboids, Cubes & Rectangular Prisms",
        "badge": "CG-5 • Questions 1–10",
        "desc": "Test your mastery on cuboid surface areas, lateral wall whitewashing, cubic edge scaling, space diagonals, and interior storage capacities.",
        "questions": [
            {
                "q": "1. What is the total surface area of a box with dimensions length 8 cm, breadth 5 cm, and height 3 cm?",
                "options": ["79 cm²", "120 cm²", "158 cm²", "180 cm²"],
                "ans": 2,
                "solution": "Step 1: TSA = 2(lb + bh + hl).\nStep 2: TSA = 2(8×5 + 5×3 + 3×8) = 2(40 + 15 + 24) = 2(79).\nStep 3: TSA = 158 cm²."
            },
            {
                "q": "2. Find the cost of whitewashing the 4 walls of a room of length 5 m, breadth 4 m, and height 3 m at the rate of ₹12 per m².",
                "options": ["₹540", "₹648", "₹720", "₹864"],
                "ans": 1,
                "solution": "Step 1: Area of 4 walls = LSA = 2h(l + b).\nStep 2: LSA = 2 × 3 × (5 + 4) = 6 × 9 = 54 m².\nStep 3: Cost = 54 × ₹12 = ₹648."
            },
            {
                "q": "3. The volume of a cube is 512 cm³. What is its total surface area?",
                "options": ["256 cm²", "384 cm²", "448 cm²", "512 cm²"],
                "ans": 1,
                "solution": "Step 1: V = a³ = 512 ⇒ a = 8 cm.\nStep 2: TSA = 6a² = 6 × 8² = 6 × 64 = 384 cm²."
            },
            {
                "q": "4. What is the length of the longest rod that can be placed inside a cubical box of edge 10 cm?",
                "options": ["10 cm", "10√2 cm", "10√3 cm", "20 cm"],
                "ans": 2,
                "solution": "Step 1: The longest rod is the space diagonal of the cube.\nStep 2: Diagonal d = a√3 = 10√3 cm (≈ 17.32 cm)."
            },
            {
                "q": "5. A cuboidal water tank is 6 m long, 5 m wide, and 4.5 m deep. How many litres of water can it hold?",
                "options": ["13,500 L", "27,000 L", "135,000 L", "270,000 L"],
                "ans": 2,
                "solution": "Step 1: Volume V = l × b × h = 6 × 5 × 4.5 = 135 m³.\nStep 2: Since 1 m³ = 1000 litres, Capacity = 135 × 1000 = 135,000 litres."
            },
            {
                "q": "6. If the ratio of the edges of two cubes is 2 : 3, what is the ratio of their total surface areas?",
                "options": ["2 : 3", "4 : 9", "8 : 27", "16 : 81"],
                "ans": 1,
                "solution": "Step 1: TSA of a cube = 6a².\nStep 2: Ratio of surface areas = (a1 / a2)² = (2 / 3)² = 4 / 9 = 4 : 9."
            },
            {
                "q": "7. The lateral surface area of a cube is 256 cm². What is the volume of the cube?",
                "options": ["256 cm³", "512 cm³", "768 cm³", "1024 cm³"],
                "ans": 1,
                "solution": "Step 1: LSA = 4a² = 256 ⇒ a² = 64 ⇒ a = 8 cm.\nStep 2: Volume = a³ = 8³ = 512 cm³."
            },
            {
                "q": "8. Three metallic cubes of sides 3 cm, 4 cm, and 5 cm are melted to form a single new cube. What is the edge of the new cube?",
                "options": ["6 cm", "7 cm", "8 cm", "9 cm"],
                "ans": 0,
                "solution": "Step 1: Total volume = 3³ + 4³ + 5³ = 27 + 64 + 125 = 216 cm³.\nStep 2: New cube volume A³ = 216 ⇒ A = ∛216 = 6 cm."
            },
            {
                "q": "9. A rectangular diesel tanker has dimensions 4 m × 2.5 m × 2 m. If diesel costs ₹90 per litre, what is the total value of diesel when full?",
                "options": ["₹90,000", "₹180,000", "₹900,000", "₹1,800,000"],
                "ans": 3,
                "solution": "Step 1: Volume = 4 × 2.5 × 2 = 20 m³.\nStep 2: Volume in litres = 20 × 1000 = 20,000 litres.\nStep 3: Total value = 20,000 × ₹90 = ₹1,800,000."
            },
            {
                "q": "10. In a cuboid, if length, breadth, and height are all doubled, its volume increases by a factor of:",
                "options": ["2", "4", "6", "8"],
                "ans": 3,
                "solution": "Step 1: Initial volume V1 = lbh.\nStep 2: New volume V2 = (2l)(2b)(2h) = 8 lbh = 8 V1.\nStep 3: The volume increases by a factor of 8."
            }
        ]
    },

    # Quiz 2: Slide 18 (Questions 11 to 20: Cylinders, Curved Surfaces, Pipes & Capacities)
    {
        "id": 18,
        "title": "Mastery Challenge II: Right Circular Cylinders & Hollow Pipes",
        "badge": "CG-5 • C-5.1 • Questions 11–20",
        "desc": "Solve problems on cylinder curved surface areas, unrolling into rectangular sheets, hollow pipes, road roller rotations, and water storage capacities.",
        "questions": [
            {
                "q": "11. The curved surface area of a right circular cylinder of height 14 cm is 88 cm². What is the diameter of the base? (Use π = 22/7)",
                "options": ["1 cm", "2 cm", "3 cm", "4 cm"],
                "ans": 1,
                "solution": "Step 1: CSA = 2πrh = 88 cm².\nStep 2: 2 × (22/7) × r × 14 = 88 ⇒ 88 r = 88 ⇒ r = 1 cm.\nStep 3: Diameter d = 2r = 2 × 1 = 2 cm."
            },
            {
                "q": "12. A cylindrical road roller of length 1.2 m and diameter 84 cm takes 500 complete revolutions to level a playground. What is the area of the playground? (Use π = 22/7)",
                "options": ["1267.2 m²", "1584 m²", "1840 m²", "2112 m²"],
                "ans": 1,
                "solution": "Step 1: Radius r = 84 / 2 = 42 cm = 0.42 m; Height (length) h = 1.2 m.\nStep 2: Area leveled in 1 rev = CSA = 2πrh = 2 × (22/7) × 0.42 × 1.2 = 2 × 22 × 0.06 × 1.2 = 3.168 m².\nStep 3: Total area in 500 revs = 500 × 3.168 = 1584 m²."
            },
            {
                "q": "13. What is the total surface area of a closed cylindrical petrol storage tank of diameter 4.2 m and height 4.5 m? (Use π = 22/7)",
                "options": ["72.6 m²", "87.12 m²", "98.4 m²", "105.6 m²"],
                "ans": 1,
                "solution": "Step 1: Radius r = 4.2 / 2 = 2.1 m; Height h = 4.5 m.\nStep 2: TSA = 2πr(h + r) = 2 × (22/7) × 2.1 × (4.5 + 2.1) = 2 × 22 × 0.3 × 6.6 = 13.2 × 6.6 = 87.12 m²."
            },
            {
                "q": "14. A soft drink is available in a cylindrical can with a circular base of diameter 7 cm and height 10 cm. What is its capacity in ml? (Use π = 22/7)",
                "options": ["285 ml", "350 ml", "385 ml", "425 ml"],
                "ans": 2,
                "solution": "Step 1: Radius r = 3.5 cm = 7/2 cm; Height h = 10 cm.\nStep 2: Volume = πr²h = (22/7) × (7/2) × (7/2) × 10 = (22 × 7 × 10) / 4 = 1540 / 4 = 385 cm³.\nStep 3: Since 1 cm³ = 1 ml, capacity = 385 ml."
            },
            {
                "q": "15. A hollow garden roller of length 2 m has an outer radius of 28 cm and thickness 7 cm. What is the volume of iron used? (Use π = 22/7)",
                "options": ["1.1 m³", "0.2156 m³", "0.452 m³", "0.684 m³"],
                "ans": 1,
                "solution": "Step 1: Outer radius R = 28 cm = 0.28 m; Inner radius r = 28 - 7 = 21 cm = 0.21 m; Height h = 2 m.\nStep 2: V = π(R² - r²)h = (22/7) × (0.28² - 0.21²) × 2 = (22/7) × (0.0784 - 0.0441) × 2 = (22/7) × 0.0343 × 2 = 22 × 0.0049 × 2 = 0.2156 m³."
            },
            {
                "q": "16. If the radius of a cylinder is doubled and its height is halved, what happens to its volume?",
                "options": ["It is halved", "It remains unchanged", "It is doubled", "It is quadrupled"],
                "ans": 2,
                "solution": "Step 1: Initial volume V1 = π r² h.\nStep 2: New volume V2 = π (2r)² (h/2) = π (4r²) (h/2) = 2 π r² h = 2 V1.\nStep 3: The volume is doubled."
            },
            {
                "q": "17. A rectangular sheet of paper 44 cm × 18 cm is rolled along its length to form a cylinder. What is the volume of the cylinder? (Use π = 22/7)",
                "options": ["1386 cm³", "2772 cm³", "3696 cm³", "4158 cm³"],
                "ans": 1,
                "solution": "Step 1: Rolling along length means base circumference C = 2πr = 44 cm ⇒ r = 7 cm.\nStep 2: Height of cylinder h = 18 cm.\nStep 3: Volume = πr²h = (22/7) × 7² × 18 = 22 × 7 × 18 = 154 × 18 = 2772 cm³."
            },
            {
                "q": "18. A well of diameter 3 m is dug 14 m deep. What is the volume of earth taken out? (Use π = 22/7)",
                "options": ["49.5 m³", "99 m³", "148.5 m³", "198 m³"],
                "ans": 1,
                "solution": "Step 1: Radius r = 3/2 = 1.5 m; Depth h = 14 m.\nStep 2: Volume = πr²h = (22/7) × (3/2) × (3/2) × 14 = (22 × 9 × 14) / (7 × 4) = (22 × 9 × 2) / 4 = 198 / 2 = 99 m³."
            },
            {
                "q": "19. The ratio of the curved surface area to the total surface area of a right circular cylinder is 1 : 2. If its total surface area is 616 cm², what is its volume? (Use π = 22/7)",
                "options": ["539 cm³", "1078 cm³", "1617 cm³", "2156 cm³"],
                "ans": 1,
                "solution": "Step 1: CSA / TSA = 2πrh / [2πr(h + r)] = h / (h + r) = 1/2 ⇒ 2h = h + r ⇒ h = r.\nStep 2: TSA = 2πr(2r) = 4πr² = 616 ⇒ 4 × (22/7) × r² = 616 ⇒ r² = 49 ⇒ r = 7 cm, h = 7 cm.\nStep 3: Volume = πr²h = (22/7) × 7² × 7 = 22 × 49 = 1078 cm³."
            },
            {
                "q": "20. How many cubic metres of water can a cylindrical pipe of internal diameter 20 cm and length 70 m hold? (Use π = 22/7)",
                "options": ["1.1 m³", "2.2 m³", "4.4 m³", "7.7 m³"],
                "ans": 1,
                "solution": "Step 1: Radius r = 10 cm = 0.1 m; Length h = 70 m.\nStep 2: Volume = πr²h = (22/7) × (0.1)² × 70 = (22/7) × 0.01 × 70 = 22 × 0.1 = 2.2 m³."
            }
        ]
    },

    # Quiz 3: Slide 19 (Questions 21 to 30: Cones, Slant Heights, 1/3 Volume Ratio & Pyramids)
    {
        "id": 19,
        "title": "Mastery Challenge III: Right Circular Cones & Pyramids",
        "badge": "CG-5 • C-5.1 • Questions 21–30",
        "desc": "Master calculations of slant heights, conical canvas tents, the 3-to-1 cylinder pouring relationship, and square pyramid volumes and lateral surface areas.",
        "questions": [
            {
                "q": "21. What is the curved surface area of a cone of base diameter 14 cm and slant height 25 cm? (Use π = 22/7)",
                "options": ["275 cm²", "550 cm²", "616 cm²", "1100 cm²"],
                "ans": 1,
                "solution": "Step 1: Radius r = 14 / 2 = 7 cm; Slant height l = 25 cm.\nStep 2: CSA = πrl = (22/7) × 7 × 25 = 22 × 25 = 550 cm²."
            },
            {
                "q": "22. The volume of a right circular cone of height 9 cm is 48π cm³. What is the diameter of its base?",
                "options": ["4 cm", "6 cm", "8 cm", "12 cm"],
                "ans": 2,
                "solution": "Step 1: V = (1/3)πr²h = 48π ⇒ (1/3) r² (9) = 48 ⇒ 3 r² = 48 ⇒ r² = 16 ⇒ r = 4 cm.\nStep 2: Base diameter d = 2r = 2 × 4 = 8 cm."
            },
            {
                "q": "23. A conical tent is 10 m high and the radius of its base is 24 m. Find the cost of canvas required to make the tent at ₹70 per m². (Use π = 22/7)",
                "options": ["₹68,400", "₹112,640", "₹137,280", "₹154,000"],
                "ans": 2,
                "solution": "Step 1: Slant height l = √(r² + h²) = √(24² + 10²) = √(576 + 100) = √676 = 26 m.\nStep 2: Canvas needed = CSA = πrl = (22/7) × 24 × 26 = 13728 / 7 m².\nStep 3: Cost = (13728 / 7) × ₹70 = 13728 × 10 = ₹137,280."
            },
            {
                "q": "24. A heap of wheat is in the form of a cone whose diameter is 10.5 m and height is 3 m. What is its volume? (Use π = 22/7)",
                "options": ["43.31 m³", "86.625 m³", "129.94 m³", "173.25 m³"],
                "ans": 1,
                "solution": "Step 1: Radius r = 10.5 / 2 = 5.25 m = 21/4 m; Height h = 3 m.\nStep 2: Volume = (1/3)πr²h = (1/3) × (22/7) × (21/4) × (21/4) × 3 = (22/7) × (21/4) × (21/4) = (22 × 3 × 21) / 16 = 1386 / 16 = 86.625 m³."
            },
            {
                "q": "25. When the curved surface of a cone of radius r and slant height l is unrolled into a flat sector, what is the radius of the resulting sector?",
                "options": ["r", "h", "l (slant height)", "r + h"],
                "ans": 2,
                "solution": "Step 1: The cone is sliced along its slant edge l.\nStep 2: The straight edges that formed the slant height now form the radius of the unrolled sector, which is l."
            },
            {
                "q": "26. What is the volume of a regular square pyramid of base edge 6 cm and vertical height 10 cm?",
                "options": ["60 cm³", "120 cm³", "180 cm³", "360 cm³"],
                "ans": 1,
                "solution": "Step 1: Base area B = a² = 6² = 36 cm².\nStep 2: Volume = (1/3) B h = (1/3) × 36 × 10 = 12 × 10 = 120 cm³."
            },
            {
                "q": "27. In a regular square pyramid, the base edge is 16 m and the slant height is 17 m. What is its vertical height h?",
                "options": ["12 m", "15 m", "18 m", "20 m"],
                "ans": 1,
                "solution": "Step 1: The right triangle inside has hypotenuse l = 17 m and base leg = a/2 = 8 m.\nStep 2: Vertical height h = √(l² - (a/2)²) = √(17² - 8²) = √(289 - 64) = √225 = 15 m."
            },
            {
                "q": "28. If a solid cube of side a is divided into 6 congruent pyramids meeting at the center of the cube, what is the height of each pyramid?",
                "options": ["a", "a / 2", "a / 3", "a / √2"],
                "ans": 1,
                "solution": "Step 1: The apex of each pyramid is at the center of the cube.\nStep 2: The distance from the center of the cube to any face is half the side length: h = a / 2."
            },
            {
                "q": "29. If the radius of the base of a cone is doubled while keeping its slant height constant, its curved surface area:",
                "options": ["Is halved", "Remains unchanged", "Is doubled", "Is quadrupled"],
                "ans": 2,
                "solution": "Step 1: CSA = π r l.\nStep 2: If r becomes 2r, New CSA = π (2r) l = 2 (π r l) = 2 CSA.\nStep 3: The curved surface area is doubled."
            },
            {
                "q": "30. A cone, a hemisphere, and a cylinder stand on equal bases and have the same height. What is the ratio of their volumes?",
                "options": ["1 : 2 : 3", "1 : 3 : 2", "2 : 3 : 1", "3 : 2 : 1"],
                "ans": 0,
                "solution": "Step 1: Let base radius be r. For hemisphere to have height r, the cone and cylinder also have height h = r.\nStep 2: V_cone = (1/3)πr²(r) = (1/3)πr³.\nStep 3: V_hemi = (2/3)πr³.\nStep 4: V_cyl = πr²(r) = πr³.\nStep 5: Ratio = 1/3 : 2/3 : 1 = 1 : 2 : 3."
            }
        ]
    },

    # Quiz 4: Slide 20 (Questions 31 to 40: Spheres, Hemispheres, Archimedes' Ratio, Recasting & SA/V)
    {
        "id": 20,
        "title": "Mastery Challenge IV: Spheres, Hemispheres, Recasting & Scaling",
        "badge": "CG-5 • CG-9 • Questions 31–40",
        "desc": "Tackle challenging problems on sphere and hemisphere surface areas, Archimedes' cylinder theorem, volume conservation during melting, and the Square-Cube Law.",
        "questions": [
            {
                "q": "31. The surface area of a sphere is 154 cm². What is the diameter of the sphere? (Use π = 22/7)",
                "options": ["3.5 cm", "7 cm", "10.5 cm", "14 cm"],
                "ans": 1,
                "solution": "Step 1: TSA = 4πr² = 154 ⇒ 4 × (22/7) × r² = 154.\nStep 2: r² = (154 × 7) / 88 = (7 × 7) / 4 = 49 / 4 ⇒ r = 7 / 2 = 3.5 cm.\nStep 3: Diameter d = 2r = 2 × 3.5 = 7 cm."
            },
            {
                "q": "32. What is the total surface area of a solid hemisphere of radius 10 cm? (Use π = 3.14)",
                "options": ["628 cm²", "942 cm²", "1256 cm²", "1570 cm²"],
                "ans": 1,
                "solution": "Step 1: Solid hemisphere TSA = 3πr².\nStep 2: TSA = 3 × 3.14 × 10² = 3 × 3.14 × 100 = 942 cm²."
            },
            {
                "q": "33. A sphere, a cylinder of height 2r, and a cone of height 2r all have the same radius r. What is the ratio of their volumes?",
                "options": ["1 : 2 : 3", "2 : 3 : 1", "Cone : Sphere : Cylinder = 1 : 2 : 3", "Cone : Sphere : Cylinder = 2 : 1 : 3"],
                "ans": 2,
                "solution": "Step 1: V_cone = (1/3)πr²(2r) = (2/3)πr³.\nStep 2: V_sphere = (4/3)πr³.\nStep 3: V_cylinder = πr²(2r) = 2πr³ = (6/3)πr³.\nStep 4: Dividing by (2/3)πr³ yields ratio 1 : 2 : 3."
            },
            {
                "q": "34. A metallic sphere of radius 10.5 cm is melted and recast into small cones, each of radius 3.5 cm and height 3 cm. How many cones are obtained?",
                "options": ["63", "84", "105", "126"],
                "ans": 3,
                "solution": "Step 1: Volume of sphere = (4/3) × π × (10.5)³ = (4/3) × π × (21/2)³ = (4/3) × π × 9261 / 8 = 3087 π / 2.\nStep 2: Volume of one cone = (1/3) × π × (3.5)² × 3 = π × (7/2)² = 49 π / 4.\nStep 3: Number of cones = (3087 π / 2) / (49 π / 4) = (3087 / 2) × (4 / 49) = 63 × 2 = 126 cones."
            },
            {
                "q": "35. If the surface area of a sphere is 4πr², what is the area of the shadow it casts on a screen when illuminated by parallel light rays?",
                "options": ["πr²", "2πr²", "3πr²", "4πr²"],
                "ans": 0,
                "solution": "Step 1: Parallel light rays project the maximum cross-sectional silhouette of the sphere.\nStep 2: The maximum cross-section of a sphere is its Great Circle.\nStep 3: Area of great circle = πr² (exactly one-quarter of the sphere's total surface area)."
            },
            {
                "q": "36. A hemispherical dome of a building needs to be painted outside. If the circumference of the base of the dome is 17.6 m, what is the cost of painting it at ₹5 per m²? (Use π = 22/7)",
                "options": ["₹123.20", "₹246.40", "₹492.80", "₹985.60"],
                "ans": 1,
                "solution": "Step 1: Base circumference = 2πr = 17.6 m ⇒ 2 × (22/7) × r = 17.6 ⇒ r = (17.6 × 7) / 44 = 2.8 m.\nStep 2: Exterior area to paint = CSA = 2πr² = 2 × (22/7) × (2.8)² = 2 × (22/7) × 7.84 = 2 × 22 × 1.12 = 49.28 m².\nStep 3: Cost = 49.28 × ₹5 = ₹246.40."
            },
            {
                "q": "37. According to Galileo's Square-Cube Law, if an animal is scaled up by a factor of 4 in all linear dimensions, its weight increases by how many times?",
                "options": ["4 times", "8 times", "16 times", "64 times"],
                "ans": 3,
                "solution": "Step 1: Weight is proportional to volume (mass = density × volume).\nStep 2: Under linear scaling factor k = 4, volume scales by k³ = 4³ = 64 times.\nStep 3: Its weight increases by 64 times."
            },
            {
                "q": "38. For an industrial cylindrical beverage can of fixed volume V, the surface area and manufacturing cost are minimized when:",
                "options": ["h = r", "h = 2r (height equals diameter)", "h = 3r", "h = 4r"],
                "ans": 1,
                "solution": "Step 1: TSA = 2πr² + 2V/r.\nStep 2: Setting derivative d(TSA)/dr = 4πr - 2V/r² = 0 gives 2V = 4πr³.\nStep 3: Since V = πr²h, 2πr²h = 4πr³ ⇒ h = 2r (height equals diameter)."
            },
            {
                "q": "39. 27 solid iron spheres, each of radius r and surface area S, are melted to form a single large sphere of surface area S'. What is the ratio S' : S?",
                "options": ["3 : 1", "6 : 1", "9 : 1", "27 : 1"],
                "ans": 2,
                "solution": "Step 1: Volume of large sphere = 27 × (4/3)πr³ = (4/3)π(3r)³ ⇒ radius R = 3r.\nStep 2: Surface area S = 4πr²; S' = 4πR² = 4π(3r)² = 9(4πr²) = 9 S.\nStep 3: Ratio S' : S = 9 : 1."
            },
            {
                "q": "40. A solid sphere of radius 6 cm is melted and drawn into a wire of uniform diameter 0.2 cm. What is the length of the wire in meters?",
                "options": ["144 m", "288 m", "432 m", "576 m"],
                "ans": 1,
                "solution": "Step 1: Radius of sphere R = 6 cm. Volume V = (4/3)πR³ = (4/3)π(216) = 288π cm³.\nStep 2: Radius of wire r = 0.2 / 2 = 0.1 cm = 1/10 cm.\nStep 3: Wire volume = πr²L = π(0.01)L = 288π ⇒ 0.01 L = 288 ⇒ L = 28,800 cm = 288 m."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(SLIDES)} slides, {len(QUIZZES)} quiz challenge slides.")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, f"Expected 16 content slides, got {len(SLIDES)}"
    assert total_cp == 32, f"Expected 32 checkpoints, got {total_cp}"
    assert len(QUIZZES) == 4, f"Expected 4 quiz challenge slides, got {len(QUIZZES)}"
    assert total_qz == 40, f"Expected 40 quiz questions, got {total_qz}"
    print("All assertions passed cleanly!")


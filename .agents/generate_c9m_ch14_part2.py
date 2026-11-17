#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 14: Math of Space: Surface Area and Volume
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Spheres Archimedes Proof",
        "subtitle": "Section 14.5 Spheres & Hemispheres: 4πr², Circumscribed Cylinder, Map Distortion & ⁴⁄₃πr³",
        "speech": (
            "Welcome to Section Fourteen Point Five: SPHERES AND HEMISPHERES! A sphere is the set of all points in "
            "three-dimensional space at a fixed distance—radius r—from a central point O! Think of a cricket ball, "
            "soap bubble, or planet Earth! "
            "How did Archimedes prove the surface area of a sphere around two hundred twenty-five BCE? He wrapped a "
            "sphere of radius r tightly inside a circumscribed cylinder of radius r and height h equals two r! "
            "Remarkably, projecting any horizontal band of the sphere outward onto the cylinder wall preserves area "
            "EXACTLY! Therefore the sphere's surface area equals the cylinder's curved surface area: two pi r times "
            "(two r), which is FOUR pi r-squared! "
            "Cartographers use this exact cylindrical projection to make EQUIRECTANGULAR WORLD MAPS—flattening Earth "
            "onto a rectangle! However, because polar latitude circles are stretched horizontally to match the equator, "
            "regions near the poles like Greenland look wildly oversized! Finally, Archimedes proved the sphere's "
            "volume is two-thirds the cylinder's volume: two-thirds of pi r-squared times (two r), giving V equals "
            "FOUR-THIRDS pi r-cubed—a monumental geometric discovery that Archimedes valued so deeply that he asked for a "
            "sphere inside a cylinder to be carved on his tombstone!"
        ),
        "checkpoints": [
            {
                "question": "A sphere of radius r fits tightly inside a cylinder of radius r and height 2r. How does the sphere's surface area compare to the cylinder's CSA?",
                "options": [
                    "They are exactly equal: both equal 4πr²",
                    "The sphere has half the area",
                    "The cylinder has twice the area",
                    "The sphere has area 2πr²",
                ],
                "answer": 0,
                "hint": "Compute Cylinder CSA = 2πr(2r)!",
                "explanation": "Archimedes' Hat-Box theorem proves Sphere Surface Area = Cylinder CSA = 2πr(2r) = 4πr².",
            },
            {
                "question": "Why do high-latitude regions like Greenland look distorted and oversized on an equirectangular world map?",
                "options": [
                    "Narrow polar latitude circles are stretched horizontally to match the full width of the equator",
                    "Earth is actually a cube",
                    "Equators are shrunk to zero",
                    "Map makers omit the oceans",
                ],
                "answer": 0,
                "hint": "Think about unrolling a sphere onto a flat cylinder wall!",
                "explanation": "Projecting a sphere onto a cylinder stretches shrinking polar circles to the full equatorial circumference 2πr.",
            },
        ],
    },
    {
        "id": 10,
        "title": "Sphere String Experiment",
        "subtitle": "Section 14.5.1 Hands-on Activity: Wrapping String Around a Sphere Fills Four Circles",
        "speech": (
            "On Slide Ten, we test Archimedes' four pi r-squared discovery with your own hands inside Section Fourteen "
            "Point Five Point One! Take a smooth spherical ball of radius r—such as a wooden or rubber ball—and mark "
            "a pin at its top pole! Wind a uniform thin string tightly around the ball in neat touching coils until "
            "the entire curved surface of the sphere is completely covered without any gaps or overlaps! Cut the "
            "string right at the bottom pole! "
            "Now draw four flat circles on a sheet of cardboard, each with the EXACT same radius r as the ball! "
            "Unwind the string from the ball and coil it spirally inside the first flat circle until it is full! "
            "Move to the second circle, then the third, then the fourth! Astonishingly, the string from one single "
            "sphere fills ALL FOUR FLAT CIRCLES completely to the brim, with nothing left over! "
            "Since each flat circle has area pi r-squared, four circles hold total area four times pi r-squared! This "
            "classic hands-on classroom activity visually confirms that the curved outer skin of a sphere equals four "
            "flat great-circle discs of the exact same radius r every single time!"
        ),
        "checkpoints": [
            {
                "question": "In the string-wrapping experiment on a ball of radius r, how many flat circles of radius r does the unwound string fill?",
                "options": ["4 circles", "2 circles", "3 circles", "6 circles"],
                "answer": 0,
                "hint": "Recall Sphere Surface Area = 4πr², and one circle has area πr²!",
                "explanation": "4πr² ÷ πr² = 4 identical flat circles of radius r.",
            },
            {
                "question": "If a solid sphere has radius r = 7 cm (use π = 22/7), what is its surface area?",
                "options": ["616 cm²", "154 cm²", "308 cm²", "1232 cm²"],
                "answer": 0,
                "hint": "Compute 4 × (22/7) × 7 × 7!",
                "explanation": "4 × (22/7) × 49 = 4 × 154 = 616 cm².",
            },
        ],
    },
    {
        "id": 11,
        "title": "Hemisphere Area Volume",
        "subtitle": "Section 14.5.2 Hemisphere: CSA = 2πr², Solid TSA = 3πr² & Volume = ⅔πr³",
        "speech": (
            "Now slice a solid sphere cleanly right through its centre O into two equal halves inside Section Fourteen "
            "Point Five Point Two: EACH HALF IS A HEMISPHERE! Think of a half-watermelon, a dome, or a soup bowl! "
            "Be extra careful to distinguish Curved Surface Area from Total Surface Area on a solid hemisphere! "
            "First, the curved outer dome is exactly half of the sphere's surface: half of four pi r-squared gives "
            "Curved Surface Area CSA equals TWO pi r-squared! "
            "Second, when you slice a solid sphere open, you expose a brand-new flat circular cross-section right "
            "across the cut face, with area pi r-squared! Adding that flat circular base to the curved dome gives "
            "Total Surface Area TSA equals two pi r-squared plus pi r-squared, which equals THREE pi r-squared! "
            "(For a thin hollow bowl open at the top, you only paint the outside or inside, not a solid flat lid!) "
            "Third, slicing a sphere in half divides its volume cleanly by two: half of four-thirds pi r-cubed gives "
            "Volume of a hemisphere equals TWO-THIRDS pi r-cubed—always keeping curved area, flat circular lid, and "
            "internal volume clearly distinct in every single 3D geometry problem you solve!"
        ),
        "checkpoints": [
            {
                "question": "A solid wooden hemisphere has radius r = 7 cm (π = 22/7). What is its Total Surface Area (including the flat circular face)?",
                "options": ["462 cm²", "308 cm²", "154 cm²", "616 cm²"],
                "answer": 0,
                "hint": "A solid hemisphere has CSA = 2πr² plus one flat circular base πr², totaling 3πr²!",
                "explanation": "TSA = 3 × (22/7) × 7² = 3 × 154 = 462 cm².",
            },
            {
                "question": "What is the volume of a hemisphere of radius r = 3 cm in terms of π?",
                "options": ["18π cm³", "36π cm³", "9π cm³", "27π cm³"],
                "answer": 0,
                "hint": "Use V = (2/3)πr³ with r = 3!",
                "explanation": "V = (2/3) × π × 3³ = (2/3) × 27π = 18π cm³.",
            },
        ],
    },
    {
        "id": 12,
        "title": "Spaces Around Us",
        "subtitle": "Section 14.6 Areas and Volumes Around Us: Measuring Cylinders, Tanks & Buckets",
        "speech": (
            "Welcome to Section Fourteen Point Six: AREAS AND VOLUMES AROUND US! Geometry does not live only inside "
            "textbooks—every kitchen, rooftop, and street corner is filled with 3D solids waiting to be measured! "
            "Look at a domestic LPG cooking-gas cylinder: its middle body is a right circular cylinder capped by "
            "rounded hemispherical domes! Look at a rooftop overhead water tank: a tall cylinder whose capacity in "
            "litres equals its cubic-metre volume multiplied by one thousand, because one cubic metre holds exactly "
            "one thousand litres! Look at an upturned bucket or lampshade: a frustum, formed by slicing the tip off "
            "a cone parallel to its base! "
            "Whenever you measure a real object, ask three practical questions! First, which 3D solid—or combination "
            "of solids—best approximates it? Second, do we need OUTER SURFACE AREA (for painting, wrapping, or metal "
            "sheets) or INNER VOLUME (for water, grain, or gas capacity)? Third, are all measurements converted to "
            "matching units—all centimetres or all metres—before multiplying? Mastering unit conversion and solid "
            "identification prevents thousand-fold engineering errors in real-world construction, plumbing, storage, "
            "packaging, and everyday manufacturing across homes, schools, workshops, and large industrial factories "
            "everywhere around us in daily life and modern civil engineering!"
        ),
        "checkpoints": [
            {
                "question": "A cylindrical rooftop tank has volume 2.5 m³. How many litres of water can it hold (1 m³ = 1000 L)?",
                "options": ["2500 L", "250 L", "25 L", "25000 L"],
                "answer": 0,
                "hint": "Multiply cubic metres by 1000 to convert to litres!",
                "explanation": "2.5 m³ × 1000 L/m³ = 2500 litres.",
            },
            {
                "question": "Which quantity should you calculate to find how much paint is needed to coat the outside of a closed water drum?",
                "options": [
                    "Total Surface Area (TSA)",
                    "Volume",
                    "Base perimeter only",
                    "Diameter",
                ],
                "answer": 0,
                "hint": "Paint covers the outer 2D skin of the closed drum!",
                "explanation": "Painting an outer closed surface requires Total Surface Area (TSA) in square units.",
            },
        ],
    },
    {
        "id": 13,
        "title": "Golgappas Ball Packing",
        "subtitle": "Section 14.6.1 Guesstimates: Spiced Water Containers & Tennis Ball Packing Efficiency",
        "speech": (
            "Now sharpen your real-world intuition inside Section Fourteen Point Six Point One: GUESSTIMATES—DID YOU "
            "EVER WONDER? Often we lack a ruler or exact blueprints, yet smart mathematical modeling delivers "
            "impressively accurate estimates! "
            "Guesstimate One—HOW MANY GOLGAPPAS CAN A STREET VENDOR SERVE FROM ONE POT? Model the vendor's pot as a "
            "cylinder—say radius fifteen centimetres and spiced water depth twenty centimetres—giving volume pi times "
            "two hundred twenty-five times twenty, roughly fourteen thousand cubic centimetres! Next, model one "
            "golgappa as a hollow sphere of radius two centimetres holding roughly twenty cubic centimetres of water! "
            "Dividing fourteen thousand by twenty estimates about seven hundred golgappas! "
            "Guesstimate Two—HOW MANY TENNIS BALLS FIT IN A CLASSROOM? Never divide classroom volume by one ball's "
            "volume directly—because spheres CANNOT pack without empty air gaps between them! Even tightest 3D "
            "sphere packing fills only about seventy-four percent of space (roughly sixty-four percent for random "
            "pouring), leaving twenty-six to thirty-six percent void! Multiplying room volume by packing efficiency "
            "gives a realistic ball count—and teaches scientists how atoms, marbles, oranges, and grains pack tightly "
            "in nature without ever filling one hundred percent of available three-dimensional container space in real-world sphere packing problems in science and engineering!"
        ),
        "checkpoints": [
            {
                "question": "Why can't you find how many tennis balls fit in a classroom simply by dividing Room Volume by One Ball Volume?",
                "options": [
                    "Spheres leave empty void gaps between them (packing efficiency is ~64%–74%, never 100%)",
                    "Because tennis balls are cubes",
                    "Because air has infinite volume",
                    "Because π equals 3",
                ],
                "answer": 0,
                "hint": "Think of oranges stacked in a crate—there are always air pockets between round balls!",
                "explanation": "Spheres cannot tile 3D space without gaps; packing efficiency (~74% max) must be factored in.",
            },
            {
                "question": "A cylindrical pot holds 12,000 cm³ of spiced water, and each golgappa takes 24 cm³. About how many golgappas can be served?",
                "options": ["500", "240", "1200", "50"],
                "answer": 0,
                "hint": "Divide total water volume by water per golgappa!",
                "explanation": "12,000 ÷ 24 = 500 golgappas.",
            },
        ],
    },
    {
        "id": 14,
        "title": "Painted Cubes Scoops",
        "subtitle": "Exercises 14.1–14.4: Painted Cut-Cube Face Counts & Ice Cream Container Scoops",
        "speech": (
            "Welcome to Slide Fourteen, where we solve two favorite problems from Exercises Fourteen Point One through "
            "Fourteen Point Four! First, the PAINTED CUT-CUBE PUZZLE! Paint all six outer faces of a large n-by-n-by-n "
            "wooden cube blue, then saw it into n-cubed unit cubes! How many small cubes have three, two, one, or "
            "zero painted faces? Look at the geometry! Only the EIGHT CORNERS touch three outer faces, so THREE-FACE "
            "cubes ALWAYS equal eight! Cubes along the twelve edges (excluding corners) have TWO painted faces: "
            "twelve times (n minus two)! Cubes inside the six flat faces (excluding borders) have ONE painted face: "
            "six times (n minus two) squared! Hidden deep inside sits an unpainted core of (n minus two) cubed! "
            "Second, solve the ICE CREAM SCOOP CHALLENGE! A cylindrical tub of radius six centimetres and height "
            "fifteen centimetres is filled with ice cream! How many hemispherical scoops of radius three centimetres "
            "can it serve? Divide cylinder volume pi times thirty-six times fifteen by hemisphere volume two-thirds "
            "pi times twenty-seven: pi cancels cleanly, giving five hundred forty divided by eighteen, which equals "
            "thirty scoops—every single time, proving how cleanly volume conservation solves multi-shape container "
            "and serving problems in daily life!"
        ),
        "checkpoints": [
            {
                "question": "A 4×4×4 cube is painted red on all 6 faces and cut into 64 unit cubes. How many unit cubes have ZERO painted faces?",
                "options": ["8", "16", "24", "27"],
                "answer": 0,
                "hint": "The unpainted inner core is an (n − 2) × (n − 2) × (n − 2) cube!",
                "explanation": "(4 − 2)³ = 2³ = 8 hidden interior unit cubes.",
            },
            {
                "question": "A cylindrical ice cream tub (r = 6 cm, h = 15 cm) is scooped into hemispherical scoops of radius 3 cm. How many scoops fit?",
                "options": ["30 scoops", "15 scoops", "60 scoops", "20 scoops"],
                "answer": 0,
                "hint": "Divide V_cylinder = π(6²)(15) by V_hemisphere = (2/3)π(3³)!",
                "explanation": "540π ÷ 18π = 30 hemispherical scoops.",
            },
        ],
    },
    {
        "id": 15,
        "title": "Water Crow Displacement",
        "subtitle": "End-of-Chapter Exercises: Earth Water Layer, Lifetime Water & Archimedes' Crow-Pitcher Marbles",
        "speech": (
            "On Slide Fifteen, we explore three extraordinary real-world problems from the End-of-Chapter Exercises! "
            "First, ARCHIMEDES' CROW-AND-PITCHER MARBLE CHALLENGE! A cylindrical pitcher of radius five centimetres "
            "holds water ten centimetres deep, leaving four centimetres of empty height to the rim! How many spherical "
            "marbles of radius one centimetre must the clever crow drop in to raise the water to the brim? Empty "
            "cylinder volume is pi times twenty-five times four, or one hundred pi! Each marble displaces four-thirds "
            "pi! Dividing one hundred pi by four-thirds pi gives EXACTLY seventy-five marbles! "
            "Second, LIFETIME WATER AND EARTH WATER LAYER! Drinking three litres daily for eighty years totals "
            "roughly eighty-seven thousand six hundred litres—about eighty-eight cubic metres, fitting inside a "
            "single classroom! Meanwhile, spreading Earth's ocean volume across Earth's surface area four pi R-squared "
            "estimates an average global water layer thickness of nearly three kilometres! "
            "Third, TEXTBOOK PACKING: packing rectangular textbooks inside a storeroom uses integer division along "
            "each edge—floor(L/l) times floor(W/w) times floor(H/h)—so rigid books never get sliced in half along "
            "any wall, floor, or shelf in the entire storeroom—unlike pouring liquids, solid boxes always keep rigid "
            "fixed dimensions along every edge of the entire storeroom and shelf space!"
        ),
        "checkpoints": [
            {
                "question": "A cylindrical pitcher (r = 5 cm) needs water raised by 4 cm (empty volume 100π cm³). How many spherical marbles of r = 1 cm (volume 4/3 π) are needed?",
                "options": ["75 marbles", "100 marbles", "50 marbles", "25 marbles"],
                "answer": 0,
                "hint": "Divide empty volume 100π by one marble's volume (4/3)π!",
                "explanation": "100π ÷ (4π/3) = 100 × 3 / 4 = 75 marbles.",
            },
            {
                "question": "Why must storeroom textbook packing multiply floor(L/l) × floor(W/w) × floor(H/h) rather than dividing total volumes?",
                "options": [
                    "Books are rigid cuboids that cannot be cut into fractions along the walls",
                    "Because books expand in heat",
                    "Because volume is measured in litres",
                    "Because storerooms are spheres",
                ],
                "answer": 0,
                "hint": "Can you fit 3.7 books along a shelf?",
                "explanation": "Only whole integer counts of books fit along each dimension without cutting them.",
            },
        ],
    },
    {
        "id": 16,
        "title": "Space Math Summary",
        "subtitle": "Chapter Summary & Appendix: 3D Formula Reference Table & Printable Fold-Out Nets",
        "speech": (
            "Congratulations on reaching Slide Sixteen, our complete synthesis of Chapter Fourteen: Math of Space, "
            "Surface Area and Volume! Review every essential formula in our master reference table! "
            "For a CUBOID (l, w, h): TSA is two times (w l plus h l plus h w) and Volume is l w h; for a CUBE of "
            "side a: TSA is six a-squared and Volume is a-cubed! "
            "For a RIGHT CIRCULAR CYLINDER (r, h): CSA is two pi r h, closed TSA is two pi r (h plus r), and Volume "
            "is pi r-squared h! "
            "For a RIGHT CIRCULAR CONE (r, h, l): slant height l-squared equals h-squared plus r-squared, CSA is pi "
            "r l, TSA is pi r (l plus r), and Volume is one-third pi r-squared h—matching the general PYRAMID formula "
            "one-third Base Area times height! "
            "For a SPHERE of radius r: Surface Area is four pi r-squared and Volume is four-thirds pi r-cubed; for a "
            "solid HEMISPHERE: CSA is two pi r-squared, TSA is three pi r-squared, and Volume is two-thirds pi "
            "r-cubed! Finally, use the Appendix fold-out 2D nets to build every 3D solid yourself! You are now ready "
            "for the four silent mastery quizzes on Slides Seventeen through Twenty!"
        ),
        "checkpoints": [
            {
                "question": "Which 2D net folds cleanly into a right circular cylinder?",
                "options": [
                    "One rectangle (width 2πr, height h) plus two circles of radius r",
                    "Four triangles and one square",
                    "One circular sector and one circle",
                    "Six congruent squares",
                ],
                "answer": 0,
                "hint": "Unroll the curved wall and detach the top and bottom lids!",
                "explanation": "A cylinder's net consists of one rectangle (2πr × h) and two circular bases (radius r).",
            },
            {
                "question": "Which solid has Volume (2/3)πr³ and solid Total Surface Area 3πr²?",
                "options": [
                    "Solid Hemisphere",
                    "Full Sphere",
                    "Right Circular Cone",
                    "Cylinder",
                ],
                "answer": 0,
                "hint": "Half a sphere's volume plus a curved dome (2πr²) and flat circular cut face (πr²)!",
                "explanation": "A solid hemisphere has V = (2/3)πr³ and TSA = 2πr² + πr² = 3πr².",
            },
        ],
    },
]

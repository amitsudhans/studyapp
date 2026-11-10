#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 12: Surface Areas and Volumes
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Combining Basic Solids",
        "subtitle": "Section 12.1 Introduction: Reviewing Cuboid, Cylinder, Cone, Sphere & Real-Life Combined Objects",
        "speech": (
            "Welcome to NCERT Class Ten Chapter Twelve: Surface Areas and Volumes! In Class Nine, you mastered the curved surface area, total surface area, and volume of individual basic shapes: cuboid, cube, right circular cylinder, right circular cone, sphere, and hemisphere! "
            "Now look closely at real world engineering objects around us! Look at a giant oil tanker truck cruising along a highway: it is NOT a pure cylinder alone—it is a central cylinder capped seamlessly at BOTH ends by TWO hemispheres! Look at a glass laboratory test tube: a straight cylindrical tube closed smoothly at the bottom by ONE hemisphere! "
            "Look at a wooden spinning top, a medicine capsule, a circus tent, or an ice cream cone topped with a scoop: almost every practical container, building, or toy is built by COMBINING TWO OR MORE basic solids! "
            "Recall quickly before slicing them: Cube TSA is 6a² and Volume is a³; Cuboid TSA is 2(lb + bh + hl) and Volume is lbh; Cylinder CSA is 2πrh and Volume is πr²h; Cone CSA is πrl (with slant height l = √(r² + h²)) and Volume is ⅓ πr²h; Sphere Area is 4πr² and Volume is 4/3 πr³! Let us master combining them!"
        ),
        "checkpoints": [
            {
                "question": "Which combination of basic three-dimensional solids forms a standard highway oil-tanker container or medicine capsule?",
                "options": [
                    "One Cylinder joined smoothly with Two Hemispheres (one at each circular end)",
                    "One Cuboid joined with Two Cones",
                    "Two Cylinders joined with One Sphere",
                    "One Cone mounted on a Cube"
                ],
                "answer": 0,
                "hint": "Inspect the flat-sided middle body and the two rounded hemispherical caps on both ends!",
                "explanation": "A capsule or oil tanker consists of a central right circular cylinder capped by two identical hemispheres."
            },
            {
                "question": "Which formula pair accurately matches Slant Height (l) and Curved Surface Area (CSA) of a right circular cone of radius r and vertical height h?",
                "options": [
                    "l = √(r² + h²),   CSA = π r l",
                    "l = r + h,   CSA = 2π r h",
                    "l = √(r² − h²),   CSA = ⅓ π r² h",
                    "l = √(r² + h²),   CSA = 2π r l"
                ],
                "answer": 0,
                "hint": "Use the right triangle formed by radius r, vertical height h, and slant edge l!",
                "explanation": "By Pythagoras theorem l = √(r² + h²), and cone Curved Surface Area is π r l."
            }
        ]
    },
    {
        "id": 2,
        "title": "Visible Surface Rule",
        "subtitle": "Section 12.2 Core Law: Hidden Joined Faces Disappear, Only Exposed Surfaces Count Toward TSA",
        "speech": (
            "Master the SINGLE most important rule of Section Twelve Point Two right now, and you will NEVER get trapped on composite surface area problems! "
            "Whenever two or more basic solids are glued together face to face, what happens to the flat circular or square faces that touch each other inside? They become HIDDEN inside the solid! Because you can no longer touch or paint those glued interior faces from the outside, they DISAPPEAR completely from the Total Surface Area! "
            "For example, take a medicine test tube built from one cylinder and one bottom hemisphere of equal radius r! Never blindly add Cylinder TSA plus Hemisphere TSA! Instead, add ONLY the visible outside surfaces: Cylinder Curved Surface Area (2πrh) PLUS Top Open Rim (if closed) PLUS Hemisphere Curved Surface Area (2πr²)! Notice both internal base circles vanished cleanly! "
            "What if a hemisphere or cone is carved cleanly INSIDE a solid wooden block? You MUST SUBTRACT the flat circular disc opening that got scooped out, YET ADD the brand new exposed curved interior wall you can now touch directly inside the hollow cavity! Always pause carefully and ask yourself ONE golden rule: Where would exterior paint actually stick?"
        ),
        "checkpoints": [
            {
                "question": "A solid toy is made by joining a cone and a hemisphere along their equal circular bases (radius r). Why is its TSA = πrl + 2πr², NOT (πrl + πr²) + (2πr² + πr²)?",
                "options": [
                    "Because both circular base faces (πr² + πr²) get hidden inside upon joining and are NOT visible externally",
                    "Because a cone does not have a base",
                    "Because volume stays zero",
                    "Because hemisphere CSA is πr²"
                ],
                "answer": 0,
                "hint": "Ask where exterior paint can reach after the cone base and hemisphere rim are glued together!",
                "explanation": "Touching circular bases become completely internal and hidden, leaving only the two curved surfaces πrl + 2πr²."
            },
            {
                "question": "If a solid hemisphere of radius r is scooped OUT from the top flat face of a solid wooden cylinder (radius r, height h), what is the resulting TSA?",
                "options": [
                    "2πrh + πr² + 2πr²   (= 2πrh + 3πr², counting cylinder CSA, solid bottom base & curved hemispherical pit)",
                    "2πrh + πr² − 2πr²",
                    "2πrh + 2πr²",
                    "πr²h − 2/3 πr³"
                ],
                "answer": 0,
                "hint": "Every carved scoop creates NEW touchable curved surface area inside the cavity!",
                "explanation": "Visible faces are outer cylinder wall (2πrh), solid bottom circle (πr²), plus newly exposed inner hemisphere (2πr²)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Playing Top Lattu",
        "subtitle": "Section 12.2 Example 1: Spinning Top (Cone + Hemisphere, H=5 cm, d=3.5 cm) Coloring Area ≈ 39.6 cm²",
        "speech": (
            "Now apply our paint rule straight onto Section Twelve Point Two Worked Example One: a classic spinning wooden playing top shaped like a sharp cone mounted cleanly onto a hemisphere! "
            "Read every dimension with laser precision! The ENTIRE spinning top has total height five centimeters, and the circular diameter of the top is three point five centimeters! First convert diameter cleanly to radius: r equals 3.5 divided by 2 equals 1.75 centimeters (or neatly seven over four centimeters)! "
            "Notice ONE crucial trap students make on combined heights: the height of the HEMISPHERE part equals its own radius 1.75 cm! Therefore, the vertical height of the CONICAL part alone equals total height 5 minus 1.75 equals THREE POINT TWO FIVE centimeters! "
            "Next find slant height l of the cone using Pythagoras theorem: l equals square root of (1.75 squared plus 3.25 squared), which simplifies to roughly three point seven centimeters! "
            "Finally factor cleanly before multiplying decimals! Total Painting Area equals Hemisphere CSA (2πr²) plus Cone CSA (πrl) equals πr(2r + l) = (22/7) × (3.5/2) × (3.5 + 3.7) = 5.5 × 7.2 = exact THIRTY NINE POINT SIX square centimeters across the whole spinning top!"
        ),
        "checkpoints": [
            {
                "question": "In Worked Example 1, a playing top has total height 5 cm and diameter 3.5 cm (r = 1.75 cm). What is the vertical height (h) of the CONICAL part alone?",
                "options": [
                    "3.25 cm   (= Total Height 5 cm − Hemisphere Radius 1.75 cm)",
                    "5 cm",
                    "1.5 cm",
                    "1.75 cm"
                ],
                "answer": 0,
                "hint": "A hemisphere's height equals its own radius r!",
                "explanation": "Conical height = 5 − 1.75 = 3.25 cm."
            },
            {
                "question": "Compute the total area to be coloured on the playing top (l ≈ 3.7 cm, r = 1.75 cm, π = 22/7, Example 1):",
                "options": [
                    "39.6 cm² (approx.)   [= πr(2r + l) = (22/7)×1.75×7.2]",
                    "79.2 cm²",
                    "19.8 cm²",
                    "35.6 cm²"
                ],
                "answer": 0,
                "hint": "Factor πr outside cleanly: πr(2r + l) = 5.5 × (3.5 + 3.7)!",
                "explanation": "CSA = πr(2r + l) = (22/7)×(3.5/2)×(3.5 + 3.7) = 5.5 × 7.2 = 39.6 cm²."
            }
        ]
    },
    {
        "id": 4,
        "title": "Decorative Cube Block",
        "subtitle": "Section 12.2 Example 2: Cube (a=5 cm) + Top Hemisphere (d=4.2 cm) → TSA = 6a² + πr² = 163.86 cm²",
        "speech": (
            "Inspect Section Twelve Point Two Worked Example Two—one of the cleverest visual geometry tricks in the entire chapter! "
            "Imagine a solid cubical decorative wooden block with edge length five centimeters! Fixed squarely on the TOP face of this cube is a hemisphere of circular diameter four point two centimeters (so radius r equals two point one centimeters)! Notice 4.2 cm fits strictly INSIDE the 5 cm square top! "
            "Let us find the exact Total Surface Area of this block! Start with all SIX square faces of the cube: 6a² equals 6 × 25 equals 150 square centimeters! "
            "Wait—what gets COVERED and HIDDEN on the top square face where the flat circular base of the hemisphere sits glued? ONE circular disc of area pi r squared disappears cleanly! So subtract πr²! "
            "Yet what NEW curved dome surface gets ADDED rising up into the air? Hemisphere Curved Surface Area equals TWO pi r squared! "
            "Watch that magical algebraic simplification happen right before your eyes: Cube TSA (6a²) MINUS hidden base (πr²) PLUS exposed dome (2πr²) equals simply 6a² PLUS ONE πr²! Plug values: 150 + (22/7) × 2.1 × 2.1 = 150 + 13.86 = 163.86 square centimeters!"
        ),
        "checkpoints": [
            {
                "question": "A decorative block is made of a cube (edge a) with a smaller hemisphere (radius r) glued on top (Example 2). Why does its TSA simplify cleanly to 6a² + πr²?",
                "options": [
                    "Because hiding circular base (−πr²) and adding curved dome (+2πr²) leaves net +πr² above the cube's 6a²",
                    "Because cube TSA equals 4a²",
                    "Because hemisphere CSA is πr² alone",
                    "Because the bottom face of the cube disappears"
                ],
                "answer": 0,
                "hint": "Combine (−πr²) + (+2πr²) cleanly!",
                "explanation": "6a² − πr² + 2πr² simplifies directly to 6a² + πr²."
            },
            {
                "question": "Calculate the exact TSA of the decorative block with cube edge 5 cm and hemisphere diameter 4.2 cm (π = 22/7, Example 2):",
                "options": [
                    "163.86 cm²   (= 150 + 13.86)",
                    "177.72 cm²",
                    "136.14 cm²",
                    "163.50 cm²"
                ],
                "answer": 0,
                "hint": "6(5²) + (22/7) × 2.1 × 2.1 = 150 + 22 × 0.3 × 2.1!",
                "explanation": "150 + 13.86 = 163.86 cm²."
            }
        ]
    },
    {
        "id": 5,
        "title": "Rocket Model Painting",
        "subtitle": "Section 12.2 Example 3: Wooden Toy Rocket (Overhanging Cone Base + Cylinder) → Orange 63.585, Yellow 195.465 cm²",
        "speech": (
            "Now solve Section Twelve Point Two Worked Example Three—the Wooden Toy Rocket! This problem tests whether you spot OVERHANGING base areas when two mounted solids have DIFFERENT radii! "
            "Read carefully: A wooden toy rocket stands twenty six centimeters tall total! Its upper cone stands six centimeters tall with wider circular base diameter five centimeters (radius capital R = 2.5 cm), while its lower cylindrical body stands twenty centimeters tall with narrower diameter three centimeters (radius small r = 1.5 cm)! "
            "Notice the cone base OVERHANGS the narrower cylinder! The conical cap must be painted ORANGE, and the cylindrical base must be painted YELLOW! Let us paint BOTH colors cleanly (pi = 3.14)! "
            "First find cone slant height l: l = √(2.5² + 6²) = √(6.25 + 36) = √42.25 = exact SIX POINT FIVE centimeters! "
            "What surfaces receive ORANGE paint? Cone CSA (π R l) PLUS the flat circular ring hanging out beneath the cone's wider skirt: π(R² − r²)! Check: 3.14 × [2.5×6.5 + (6.25 − 2.25)] = 3.14 × 20.25 = 63.585 cm²! "
            "And YELLOW paint covers Cylinder CSA PLUS solid bottom base circle: 2πrh + πr² = 3.14 × (60 + 2.25) = 195.465 cm²!"
        ),
        "checkpoints": [
            {
                "question": "In the Wooden Toy Rocket (Example 3), cone radius R = 2.5 cm sits on narrower cylinder radius r = 1.5 cm. Besides Cone CSA, what extra flat region on the cone gets painted ORANGE?",
                "options": [
                    "The overhanging circular ring (annulus) area π(R² − r²) under the wider cone base",
                    "The entire bottom circle of the cylinder",
                    "Only the inner joined circle πr²",
                    "No extra region at all"
                ],
                "answer": 0,
                "hint": "Subtract the cylinder's top circle πr² from the wider cone base πR²!",
                "explanation": "Orange area = Cone CSA (πRl) + Overhanging annular ring π(R² − r²) = 63.585 cm²."
            },
            {
                "question": "What are the exact ORANGE and YELLOW painted areas on the wooden rocket (H=26, h_cone=6, R=2.5, r=1.5, π=3.14, Example 3)?",
                "options": [
                    "Orange = 63.585 cm²,   Yellow = 195.465 cm²",
                    "Orange = 51.025 cm²,   Yellow = 188.40 cm²",
                    "Orange = 70.65 cm²,   Yellow = 195.465 cm²",
                    "Orange = 63.585 cm²,   Yellow = 188.40 cm²"
                ],
                "answer": 0,
                "hint": "Cone slant l = 6.5; Orange = 3.14×(16.25 + 4); Yellow = 3.14×(2×1.5×20 + 2.25)!",
                "explanation": "Orange = 3.14×20.25 = 63.585 cm²; Yellow = 3.14×62.25 = 195.465 cm²."
            }
        ]
    },
    {
        "id": 6,
        "title": "Bird Bath Cylinder",
        "subtitle": "Section 12.2 Example 4: Hollow Cylinder With Top Hemispherical Depression (h=1.45 m, r=30 cm → 3.3 m²)",
        "speech": (
            "Take a garden walk into Section Twelve Point Two Worked Example Four: crafting a Cylindrical Bird Bath with a Hemispherical Depression hollowed smoothly out of one flat circular end! "
            "Read the unit trap right at the start: the cylindrical stand has height one point four five METERS, while the circular radius is given as thirty CENTIMETERS! ALWAYS convert units to match BEFORE plugging numbers! Convert height 1.45 m cleanly into one hundred forty five centimeters (145 cm)! "
            "Now inspect EVERY exterior surface visible on this bird bath! Notice in the textbook cylindrical stand diagram, hollow thin legs or open base rests flat, so textbook TSA explicitly computes ONLY outer Cylinder Curved Surface Area PLUS inner Hemispherical bowl surface! Let us check NCERT's exact algebraic steps: "
            "Total Surface Area equals Cylinder CSA (2πrh) PLUS Hemispherical bowl CSA (2πr²)! Notice how smoothly 2πr factors out in front: TSA equals 2πr(h + r)! "
            "Substitute r = 30 cm, h = 145 cm, and pi = 22/7: 2 × (22/7) × 30 × (145 + 30) = 2 × (22/7) × 30 × 175! Cancel 7 into 175 cleanly to get 25, giving 33,000 square centimeters equals exact 3.3 square meters!"
        ),
        "checkpoints": [
            {
                "question": "A bird-bath is a hollow cylinder of height 1.45 m and radius 30 cm with a hemispherical depression at one end (Example 4, π = 22/7). What is its TSA?",
                "options": [
                    "3.3 m²   (= 33,000 cm²)",
                    "33 m²",
                    "0.33 m²",
                    "4.5 m²"
                ],
                "answer": 0,
                "hint": "Use 2πr(h + r) with h = 145 cm, r = 30 cm, then divide cm² by 10,000 for m²!",
                "explanation": "2×(22/7)×30×175 = 33,000 cm² = 3.3 m² (since 1 m² = 10,000 cm²)."
            },
            {
                "question": "Why does 175 inside 2πr(145 + 30) cancel denominator 7 SO cleanly in Example 4?",
                "options": [
                    "Because 175 ÷ 7 = 25 exact integer, eliminating fractions completely before converting 10,000 cm² = 1 m²",
                    "Because 30 divides by 7",
                    "Because 1.45 is a multiple of 7",
                    "Because π = 3.14"
                ],
                "answer": 0,
                "hint": "Always add (h + r) inside brackets BEFORE multiplying 22/7!",
                "explanation": "145 + 30 = 175 = 7 × 25, turning 2 × (22/7) × 30 × 175 straight into clean integer 33,000 cm²."
            }
        ]
    },
    {
        "id": 7,
        "title": "Capsule And Tent",
        "subtitle": "Exercise 12.1 Classic Models: Joined Cubes (160 cm²), Medicine Capsule (220 mm²) & Tent Canvas (₹22,000)",
        "speech": (
            "Now conquer THREE famous Exercise Twelve Point One surface area problems sharing the exact same hidden face logic! "
            "Model One (Ex 12.1 Q1, Twin Cubes): Two cubes each of volume 64 cm³ are joined end to end! Since edge a³ equals 64, each cube has edge a = 4 cm! Joining them side by side builds a cuboid of length 8 cm, breadth 4 cm, and height 4 cm! Its TSA equals 2(32 + 16 + 32) = 160 cm² (Notice 2×96 − 2×16 = 160 cm²)! "
            "Model Two (Ex 12.1 Q6, Medicine Capsule): Total length is 14 mm and circular diameter is 5 mm (radius r = 2.5 mm)! Two hemispherical caps consume 2.5 + 2.5 = 5 mm of total length, leaving straight cylinder length h = 14 − 5 = 9 mm! Capsule TSA equals Cylinder CSA + TWO Hemispheres = 2πrh + 4πr² = 2πr(h + 2r) = 2 × (22/7) × 2.5 × 14 = exact 220 mm²! "
            "Model Three (Ex 12.1 Q7, Circus Tent): Cylinder (h = 2.1 m, d = 4 m → r = 2 m) topped by Cone (slant height l = 2.8 m)! Canvas TSA = 2πrh + πrl = 44 m²; cost at ₹500/m² equals ₹22,000!"
        ),
        "checkpoints": [
            {
                "question": "A medicine capsule is a cylinder with two hemispheres stuck to each end (Ex 12.1 Q6). Entire length is 14 mm and diameter is 5 mm. Find its surface area (π = 22/7):",
                "options": [
                    "220 mm²   [h_cyl = 9 mm; 2πr(h + 2r) = 2×(22/7)×2.5×14]",
                    "110 mm²",
                    "440 mm²",
                    "195 mm²"
                ],
                "answer": 0,
                "hint": "Cylinder length = 14 − 5 = 9 mm; Notice 2πrh + 4πr² = 2πr(h + 2r) where h + 2r = total length 14!",
                "explanation": "2 × (22/7) × (5/2) × 14 = 220 mm²!"
            },
            {
                "question": "Two cubes each of volume 64 cm³ are joined end to end (Ex 12.1 Q1). Find the surface area of the resulting cuboid:",
                "options": [
                    "160 cm²   (dimensions 8 cm × 4 cm × 4 cm)",
                    "192 cm²",
                    "128 cm²",
                    "144 cm²"
                ],
                "answer": 0,
                "hint": "Cube side = ∛64 = 4 cm; joined cuboid has l = 8, b = 4, h = 4!",
                "explanation": "TSA = 2(8×4 + 4×4 + 4×8) = 2(80) = 160 cm²."
            }
        ]
    },
    {
        "id": 8,
        "title": "Cavity Cube Toy",
        "subtitle": "Exercise 12.1 Q4, Q5, Q8 & Q9: Cube Dome/Pit (l²/4(24+π)), Conical Drill Cylinder (18 cm²) & Twin-Scoop (374 cm²)",
        "speech": (
            "Now inspect FOUR remarkable Exercise Twelve Point One problems comparing raised domes against carved interior cavities! "
            "First compare Question Four vs Question Five! In Q4, a cubical block of side 7 cm is surmounted by the largest possible hemisphere (diameter 7 cm → r = 3.5 cm)! Using Example Two's rule: TSA = 6a² + πr² = 294 + 38.5 = 332.5 cm²! "
            "Now look at Q5: instead of mounting a dome on top, a hemispherical depression of diameter l is carved INSIDE one face of a cube of edge l! What happens? Removing top circle (−πr²) yet exposing inner bowl wall (+2πr²) gives the EXACT SAME algebraic formula: 6l² + π(l/2)² = l²/4 × (24 + π)! "
            "Next test Question Eight (Conical Cavity in Solid Cylinder): height 2.4 cm, diameter 1.4 cm (r = 0.7 cm), slant height l = √(0.7² + 2.4²) = 2.5 cm! Remaining TSA counts THREE surfaces: outer cylinder wall (2πrh) + solid bottom base (πr²) + inner conical pit wall (πrl) = 17.6 cm² ≈ 18 cm²! "
            "And Question Nine (Solid wooden Cylinder of height 10 cm and base radius 3.5 cm scooped cleanly with hemispheres at BOTH ends): TSA = 2πrh + 4πr² = 374 square centimeters!"
        ),
        "checkpoints": [
            {
                "question": "From a solid cylinder (height 2.4 cm, diameter 1.4 cm), a conical cavity of the SAME height and diameter is hollowed out (Ex 12.1 Q8). Find TSA to nearest cm² (π = 22/7):",
                "options": [
                    "18 cm²   (exact sum = 17.6 cm² from 2πrh + πr² + πrl)",
                    "12 cm²",
                    "24 cm²",
                    "15 cm²"
                ],
                "answer": 0,
                "hint": "r = 0.7, h = 2.4 gives slant height l = 2.5 cm! Sum cylinder wall + bottom circle + inner cone CSA!",
                "explanation": "πr(2h + r + l) = (22/7)×0.7×(4.8 + 0.7 + 2.5) = 2.2 × 8 = 17.6 cm² ≈ 18 cm²."
            },
            {
                "question": "A hemispherical depression is cut out from one face of a cubical wooden block of edge l (diameter = l, Ex 12.1 Q5). Find remaining solid's TSA:",
                "options": [
                    "(l² / 4)(24 + π)   [= 6l² + π(l/2)²]",
                    "(l² / 4)(24 − π)",
                    "6l² − πl²",
                    "(l² / 2)(12 + π)"
                ],
                "answer": 0,
                "hint": "6l² − π(l/2)² + 2π(l/2)² simplifies to 6l² + πl²/4!",
                "explanation": "Factoring l²/4 from 6l² + πl²/4 yields (l²/4)(24 + π)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch12 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 12: Surface Areas and Volumes
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Volume Addition Rule",
        "subtitle": "Section 12.3 Additive Principle & Example 5: Industrial Shed Air Volume (Cuboid + Half-Cylinder = 1128.75 m³)",
        "speech": (
            "Welcome to Section Twelve Point Three: Volume of a Combination of Solids! Here comes the BEST news in geometry: unlike surface area where touching faces vanished cleanly inside, VOLUME NEVER DISAPPEARS when you join basic solids together! "
            "Joining two solid pieces cleanly adds their interior spaces: Combined Volume ALWAYS equals V₁ + V₂ + V₃! Conversely, carving or scooping out a hollow cavity SUBTRACTS cleanly: Remaining Volume equals V_outer MINUS V_cavity! "
            "Test this right away on Section Twelve Point Three Worked Example Five: the Industrial Shed! An industrial workshop shed has a rectangular cuboid base measuring fifteen meters long, seven meters wide, and eight meters tall, surmounted neatly by a HALF-CYLINDRICAL curved roof of diameter seven meters (radius r = 3.5 m) running along the fifteen meter length! "
            "Step One: Compute Cuboid Volume equals 15 × 7 × 8 equals 840 cubic meters! "
            "Step Two: Add Half Cylinder Volume equals ½ × (22/7) × 3.5 × 3.5 × 15 equals 288.75 cubic meters! Total shed space equals 1,128.75 m³! "
            "Finally remember air-capacity adjustment: if machinery occupies 300 m³ and 20 workers occupy 0.08 m³ each (1.6 m³), remaining air volume equals 1128.75 − 301.6 = 827.15 m³!"
        ),
        "checkpoints": [
            {
                "question": "When a cone and a hemisphere are joined cleanly base-to-base, how do Surface Area and Volume behave differently?",
                "options": [
                    "Touching circular faces disappear from TSA (exposed CSAs only), whereas Volumes simply ADD together (V₁ + V₂)",
                    "Both TSA and Volume lose the circular base",
                    "Volumes also vanish upon touching",
                    "TSA adds everything including internal faces while Volume subtracts"
                ],
                "answer": 0,
                "hint": "Interior space never disappears when gluing solids; only external surface access shrinks!",
                "explanation": "Glued faces become internal (removed from TSA), whereas occupied space (volume) adds directly."
            },
            {
                "question": "An industrial shed is a 15 m × 7 m × 8 m cuboid topped by a half-cylinder (Example 5, π = 22/7). Total volume of the shed:",
                "options": [
                    "1,128.75 m³   (= 840 + 288.75)",
                    "840 m³",
                    "1,417.5 m³",
                    "984.38 m³"
                ],
                "answer": 0,
                "hint": "Cuboid 15×7×8 = 840; Half-Cylinder ½ × (22/7) × (7/2)² × 15 = 288.75!",
                "explanation": "840 + 288.75 = 1,128.75 m³."
            }
        ]
    },
    {
        "id": 10,
        "title": "Juice Glass Capacity",
        "subtitle": "Section 12.3 Example 6: Cylindrical Glass With Raised Hemispherical Base (196.25 − 32.71 = 163.54 cm³)",
        "speech": (
            "Now inspect Section Twelve Point Three Worked Example Six—a clever real world trick used by some street juice sellers! "
            "A cylindrical glass looks tall and generous from outside: inner diameter five centimeters (so radius r equals 2.5 cm) and outer vertical height ten centimeters! Yet look closely inside the bottom of the glass: there is a RAISED HEMISPHERICAL bulge pushing upward into the cylinder, secretly reducing the actual liquid capacity! "
            "Let us catch BOTH numbers with crystal clarity using pi equals 3.14! "
            "First compute APPARENT Capacity (what a customer guesses ignoring the bottom bulge): Cylinder Volume equals π r² h = 3.14 × 2.5 × 2.5 × 10 = exact 196.25 cubic centimeters! "
            "Next compute the solid glass hemisphere bulge rising up inside from the bottom: Hemisphere Volume equals (2/3) × π × r³ = (2/3) × 3.14 × 2.5³ = exact 32.71 cubic centimeters! "
            "Because solid thick glass occupies those bottom 32.71 cubic centimeters permanently, poured liquid juice cannot enter that lower dome! Subtract cleanly: ACTUAL Juice Capacity equals 196.25 minus 32.71 equals exact ONE HUNDRED SIXTY THREE POINT FIVE FOUR cubic centimeters! Always inspect whether a hemisphere bulges INWARD (subtract) or protrudes OUTWARD (add)!"
        ),
        "checkpoints": [
            {
                "question": "A cylindrical juice glass (inner diameter 5 cm, height 10 cm) has a raised hemispherical bottom pushing inward (Example 6, π = 3.14). Find Apparent and Actual Capacity:",
                "options": [
                    "Apparent = 196.25 cm³,   Actual = 163.54 cm³",
                    "Apparent = 196.25 cm³,   Actual = 228.96 cm³",
                    "Apparent = 163.54 cm³,   Actual = 130.83 cm³",
                    "Apparent = 392.5 cm³,   Actual = 327.08 cm³"
                ],
                "answer": 0,
                "hint": "Apparent = π(2.5)²(10) = 196.25; subtract ⅔π(2.5)³ ≈ 32.71!",
                "explanation": "Actual = 196.25 − 32.71 = 163.54 cm³."
            },
            {
                "question": "Why did we SUBTRACT the hemisphere volume in Example 6 instead of adding it?",
                "options": [
                    "Because the solid raised hemisphere pushes UPWARD INSIDE the cylinder, stealing space that juice would otherwise fill",
                    "Because cylinders have smaller volume than hemispheres",
                    "Because radius was less than 3 cm",
                    "Because surface area is smaller"
                ],
                "answer": 0,
                "hint": "Visualize whether the rounded bottom sticks OUT underneath or INWARD into the liquid!",
                "explanation": "An inward raised bulge occupies interior cylinder space, so Actual Liquid Volume = Cylinder − Hemisphere."
            }
        ]
    },
    {
        "id": 11,
        "title": "Circumscribed Cylinder Space",
        "subtitle": "Section 12.3 Example 7: Cone-Hemisphere Toy Circumscribed by Right Cylinder (Exact 1 : 2 Volume Ratio = 25.12 cm³)",
        "speech": (
            "Explore Section Twelve Point Three Worked Example Seven, showcasing Archimedes' timeless 1 : 2 symmetry inside circumscribed solids! "
            "A solid wooden toy is shaped as a right circular cone mounted cleanly onto a hemisphere: cone height equals 2 cm and circular diameter equals 4 cm (so common radius r equals 2 cm)! "
            "Step One: Find the exact Volume of the Toy (pi = 3.14)! Cone Volume equals ⅓ π r² h = ⅓ π (4)(2) = (8/3)π! Hemisphere Volume equals ⅔ π r³ = ⅔ π (8) = (16/3)π! Notice (8/3)π + (16/3)π equals EXACT EIGHT PI (8π = 25.12 cm³)! "
            "Step Two: Now place a tight right circular cylinder completely CIRCUMSCRIBING this toy so the bottom touches cleanly, the curved wall hugs the equator, and the top touches the cone apex! What are the cylinder's radius and total height? Radius R equals 2 cm, and total height H equals cone height 2 PLUS hemisphere radius 2 equals FOUR centimeters! "
            "Cylinder Volume equals π R² H = π(4)(4) = SIXTEEN PI (16π = 50.24 cm³)! Subtracting toy volume leaves leftover empty difference 50.24 minus 25.12 equals exact 25.12 cubic centimeters—meaning this cone-hemisphere toy fills HALF the circumscribing cylinder!"
        ),
        "checkpoints": [
            {
                "question": "A cone (h = 2 cm, r = 2 cm) on a hemisphere (r = 2 cm) is circumscribed by a tight right cylinder (Example 7, π = 3.14). Find the DIFFERENCE in their volumes:",
                "options": [
                    "25.12 cm³   (= Cylinder 50.24 − Toy 25.12)",
                    "50.24 cm³",
                    "12.56 cm³",
                    "37.68 cm³"
                ],
                "answer": 0,
                "hint": "Cylinder H = 2 + 2 = 4 cm; Toy = 8π, Cylinder = 16π!",
                "explanation": "Cylinder Volume = 16π = 50.24 cm³; Toy Volume = 8π = 25.12 cm³; Difference = 25.12 cm³."
            },
            {
                "question": "What exact height H must the circumscribing cylinder have to tightly enclose the cone-on-hemisphere toy?",
                "options": [
                    "H = h_cone + r_hemisphere = 2 + 2 = 4 cm",
                    "H = h_cone alone = 2 cm",
                    "H = 2r + 2h = 8 cm",
                    "H = r_hemisphere = 2 cm"
                ],
                "answer": 0,
                "hint": "Total height runs from bottom pole of hemisphere up to top vertex of cone!",
                "explanation": "Total height H = hemisphere radius (2) + cone height (2) = 4 cm."
            }
        ]
    },
    {
        "id": 12,
        "title": "Cone On Hemisphere",
        "subtitle": "Exercise 12.2 Q1 (r=1, h=1 → π cm³) & Q2 Engineering Rocket-Model (L=12 cm, d=3 cm → 66 cm³)",
        "speech": (
            "Now solve Exercise Twelve Point Two Questions One and Two cleanly! Question One is crisp mental poetry: a solid cone stands neatly on a hemisphere with BOTH their radii equal to ONE centimeter, and the cone height equals its radius (1 cm)! Find volume strictly in terms of pi! "
            "Hemisphere Volume equals (2/3)π(1³) equals two thirds pi! Cone Volume equals (1/3)π(1²)(1) equals one third pi! Adding two thirds pi plus one third pi delivers EXACTLY ONE PI cubic centimeters (π cm³)—equivalent to one cylinder of radius 1 and height 1! "
            "Now inspect Question Two: an engineering model shaped like a central cylinder capped symmetrically with TWO identical cones at both ends! Read dimensions carefully: circular diameter is three centimeters (radius r = 1.5 cm), total model length is twelve centimeters, and EACH end cone has height two centimeters! "
            "Subtract both cone heights cleanly from twelve: Cylinder height h equals 12 − 2 − 2 equals EIGHT centimeters! "
            "Total Air Volume contained inside the model equals Cylinder π r² h PLUS Two End Cones 2 × (⅓ π r² h_cone) = (22/7) × 1.5 × 1.5 × (8 + 4/3) = (22/7) × (9/4) × (28/3) = exact SIXTY SIX cubic centimeters!"
        ),
        "checkpoints": [
            {
                "question": "A solid is a cone standing on a hemisphere with equal radii 1 cm and cone height 1 cm (Ex 12.2 Q1). Exact volume in terms of π:",
                "options": [
                    "π cm³   (= ⅔π + ⅓π)",
                    "2π cm³",
                    "⅓π cm³",
                    "4/3 π cm³"
                ],
                "answer": 0,
                "hint": "Add Hemisphere ⅔π(1³) + Cone ⅓π(1²)(1)!",
                "explanation": "⅔π + ⅓π = (3/3)π = π cm³."
            },
            {
                "question": "An engineering cylinder capped with two 2 cm cones at both ends has diameter 3 cm and total length 12 cm (Ex 12.2 Q2, π = 22/7). Air volume:",
                "options": [
                    "66 cm³   [Cyl h = 8; πr²(8 + 2/3 + 2/3) = (22/7)×2.25×(28/3)]",
                    "33 cm³",
                    "132 cm³",
                    "88 cm³"
                ],
                "answer": 0,
                "hint": "Factor πr²(h_cyl + ⅔ h_cone) = (22/7) × 1.5² × (28/3)!",
                "explanation": "(22/7) × (9/4) × (28/3) = 22 × 3 = 66 cm³!"
            }
        ]
    },
    {
        "id": 13,
        "title": "Gulab Jamun Syrup",
        "subtitle": "Exercise 12.2 Q3 Board Favorite: 45 Gulab Jamuns (L=5 cm, d=2.8 cm) Holding 30% Sugar Syrup ≈ 338 cm³",
        "speech": (
            "Celebrate solving NCERT's most delicious board exam favorite: Exercise Twelve Point Two Question Three, the Forty Five Gulab Jamuns in Sugar Syrup! "
            "Read carefully: EACH sweet gulab jamun is shaped like a cylinder capped cleanly at BOTH ends by TWO hemispheres, measuring total length FIVE centimeters and diameter TWO POINT EIGHT centimeters! "
            "Step One: Radius r equals 2.8 divided by 2 equals 1.4 centimeters! Since BOTH hemispherical ends together consume 1.4 + 1.4 = 2.8 cm of length, the middle cylindrical length h equals 5 − 2.8 equals TWO POINT TWO centimeters! "
            "Step Two: Factor volume cleanly for ONE gulab jamun! Cylinder Volume (πr²h) PLUS Two Hemispheres (4/3 πr³) equals π r² (h + 4/3 r) = (22/7) × 1.4 × 1.4 × (2.2 + 5.6/3)! Notice (22/7) × 1.4 × 1.4 = 6.16, and (12.2/3) gives single jamun volume ≈ 25.05 cubic centimeters! "
            "Step Three: Multiply single jamun volume cleanly by 45 jamuns to get total sweet volume 1,127.28 cubic centimeters! Because sugar syrup equals THIRTY PERCENT (30 divided by 100) of each gulab jamun's total volume, multiply cleanly: Syrup Volume equals 0.30 × 1127.28 = 338.18 ≈ THREE HUNDRED THIRTY EIGHT cubic centimeters of sweet syrup!"
        ),
        "checkpoints": [
            {
                "question": "A gulab jamun (cylinder + 2 hemispherical ends) has total length 5 cm and diameter 2.8 cm (Ex 12.2 Q3). What is the length h of its middle cylindrical part?",
                "options": [
                    "2.2 cm   (= 5 − 1.4 − 1.4)",
                    "5 cm",
                    "3.6 cm",
                    "2.8 cm"
                ],
                "answer": 0,
                "hint": "Subtract BOTH hemispherical radii (r + r = d = 2.8 cm) from total length 5 cm!",
                "explanation": "h = 5 − 2(1.4) = 2.2 cm."
            },
            {
                "question": "Each gulab jamun contains sugar syrup about 30% of its volume. Approximately how much syrup is inside 45 gulab jamuns (Ex 12.2 Q3, π = 22/7)?",
                "options": [
                    "338 cm³ (approx.)   [45 × 25.05 × 0.30 = 338.18 cm³]",
                    "1,127 cm³",
                    "169 cm³",
                    "450 cm³"
                ],
                "answer": 0,
                "hint": "Find 1 jamun = (22/7)×1.4²×(2.2 + 5.6/3) ≈ 25.05 cm³, then compute 0.30 × 45 × 25.05!",
                "explanation": "Syrup = 30% × (45 × 25.0507) = 338.18 cm³ ≈ 338 cm³."
            }
        ]
    },
    {
        "id": 14,
        "title": "Pen Stand Cavities",
        "subtitle": "Exercise 12.2 Q4 (Wood Pen Stand 523.53 cm³) & Q6 (Twin-Cylinder Iron Pole Mass = 892.26 kg)",
        "speech": (
            "Now inspect TWO contrasting solid craft problems inside Exercise Twelve Point Two Questions Four and Six: drilling subtractive cavities versus stacking twin metallic cylinders for mass calculation! "
            "First check Question Four, the Wooden Pen Stand! A craftsman carves FOUR conical pen depressions straight into a solid rectangular wooden cuboid measuring 15 cm × 10 cm × 3.5 cm! Each conical hole has radius 0.5 cm and vertical depth 1.4 cm! "
            "Cuboid Wood Volume equals 15 × 10 × 3.5 equals 525 cubic centimeters! Volume scooped out by ALL FOUR cones equals 4 × ⅓ × (22/7) × 0.5 × 0.5 × 1.4 equals 4.4 over 3 ≈ 1.47 cm³! Remaining solid wood volume equals 525 minus 1.47 equals 523.53 cubic centimeters cleanly! "
            "Next hoist Question Six: the Solid Iron Pole! A tall heavy lower cylinder (height 220 cm, base diameter 24 cm gives radius 12 cm) supports a narrower upper cylinder (height 60 cm, radius 8 cm)! Using pi equals 3.14: Total Iron Volume equals 3.14 × (12² × 220 + 8² × 60) = 3.14 × 35,520 = 111,532.8 cm³! Multiplying by iron density 8 grams per cubic centimeter equals 892,262.4 grams equals exact 892.26 kilograms!"
        ),
        "checkpoints": [
            {
                "question": "A cuboid pen stand (15 cm × 10 cm × 3.5 cm) has 4 conical depressions (r = 0.5 cm, depth = 1.4 cm, Ex 12.2 Q4, π = 22/7). Remaining wood volume:",
                "options": [
                    "523.53 cm³   (= 525 − 1.47)",
                    "526.47 cm³",
                    "520.53 cm³",
                    "525 cm³"
                ],
                "answer": 0,
                "hint": "Cuboid = 525; 4 Cones = 4 × ⅓ × (22/7) × 0.25 × 1.4 = 1.47 cm³!",
                "explanation": "525 − 1.47 = 523.53 cm³."
            },
            {
                "question": "A solid iron pole has lower cylinder (h=220 cm, d=24 cm) topped by upper cylinder (h=60 cm, r=8 cm). Find mass at 8 g/cm³ (Ex 12.2 Q6, π = 3.14):",
                "options": [
                    "892.26 kg (approx.)",
                    "89.23 kg",
                    "1,115.33 kg",
                    "446.13 kg"
                ],
                "answer": 0,
                "hint": "Total V = 3.14 × (144×220 + 64×60) = 111,532.8 cm³; Mass(kg) = (V × 8) ÷ 1000!",
                "explanation": "111,532.8 × 8 g = 892,262.4 g = 892.2624 kg."
            }
        ]
    },
    {
        "id": 15,
        "title": "Lead Shot Displacement",
        "subtitle": "Exercise 12.2 Q5 (100 Lead Shots in Cone), Q7 (Immersed Solid Water 1.131 m³) & Q8 (Glass Vessel 346.51 cm³)",
        "speech": (
            "Now master Archimedes Water Displacement inside Exercise Twelve Point Two's thrilling finale—Questions Five, Seven, and Eight! "
            "Check Question Five first: an inverted conical vessel (height 8 cm, top radius 5 cm) sits completely brim-full of water! Tiny spherical lead shots, each of radius 0.5 cm, are dropped quietly inside until EXACTLY ONE FOURTH of the water overflows! Find the exact number N of lead shots dropped! "
            "Apply conservation cleanly: Volume of N spheres MUST equal ONE FOURTH of Cone Volume! Notice pi cancels cleanly on BOTH sides without needing 22/7 or 3.14! Write N × (4/3)π(0.5)³ = ¼ × ⅓ π(5²)(8)! Multiply cleanly: N = (50) ÷ (0.5) = EXACT ONE HUNDRED lead shots! "
            "Check Question Seven: a cone-hemisphere toy (r = 60 cm, h_cone = 120 cm) lowered gently upright inside a full water cylinder (R = 60, H = 180) displaces its own solid volume, leaving remaining water 1,131,428.57 cm³ equals 1.131 cubic meters! "
            "And Question Eight: a spherical glass water vessel (diameter 8.5 cm gives radius 4.25 cm) topped smoothly by a cylindrical neck (h = 8 cm, d = 2 cm gives r = 1 cm) holds exact 346.51 cubic centimeters!"
        ),
        "checkpoints": [
            {
                "question": "A full conical vessel (h = 8 cm, r = 5 cm) overflows ¼ of its water when N spherical lead shots (r = 0.5 cm) are dropped in (Ex 12.2 Q5). Find N:",
                "options": [
                    "100 lead shots",
                    "50 lead shots",
                    "200 lead shots",
                    "400 lead shots"
                ],
                "answer": 0,
                "hint": "Cancel π cleanly: N × (4/3)(½)³ = ¼ × ⅓ × 25 × 8 ⟹ N/6 = 50/3!",
                "explanation": "N × (1/6)π = (50/3)π ⟹ N = 100 shots."
            },
            {
                "question": "A solid (cone h=120 cm, r=60 cm on hemisphere r=60 cm) is placed in a full cylinder (r=60 cm, h=180 cm, Ex 12.2 Q7). Water left in cylinder:",
                "options": [
                    "1.131 m³ (approx.)   [= Cylinder 180π(3600) − Toy 80π(3600) = 100π(3600) cm³]",
                    "2.035 m³",
                    "0.904 m³",
                    "3.142 m³"
                ],
                "answer": 0,
                "hint": "1 m³ = 1,000,000 cm³; remaining volume = π(60²)(180 − 40 − 40) = 360,000π cm³!",
                "explanation": "360,000 × (22/7) cm³ = 1,131,428.57 cm³ ≈ 1.131 m³."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Twelve Summary",
        "subtitle": "Section 12.4 Complete Mastery Card: Composite Surface Area vs Additive Volume Across All 6 Basic Solids",
        "speech": (
            "Bravo, three-dimensional geometry champions! You have conquered EVERY theorem, real world engineering model, and board exam trap inside NCERT Class Ten Chapter Twelve: Surface Areas and Volumes! Lock in your complete Section Twelve Point Four checklist before launching into forty Interactive Quizzes! "
            "Rule One, Surface Area of Combined Solids: Identify every individual curved or flat piece visible from the OUTSIDE—glued interior faces disappear completely, whereas carved cavities subtract ONLY the surface opening circle while adding the newly exposed inner curved wall! "
            "Rule Two, Overhanging & Height Traps: Always subtract hemisphere radii from total object height to isolate cylindrical or conical heights cleanly, and include overhanging annular rings π(R² − r²) when joining mismatched radii! "
            "Rule Three, Volume of Combined Solids: Volumes ALWAYS add directly (V₁ + V₂) for joined solids, subtract cleanly (V_outer − V_cavity) for hollow cups, raised bottoms, or pen stand depressions, and cancel pi cleanly whenever counting displaced spheres! "
            "Rule Four, Unit & Density Vigilance: Match centimeters vs meters carefully BEFORE substituting numerical values (recall 1 m² equals 10,000 cm², 1 m³ equals 1,000,000 cm³, and 1 Liter equals 1,000 cm³), and convert calculated grams into kilograms cleanly by dividing by one thousand!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement across NCERT Chapter 12 is 100% mathematically accurate?",
                "options": [
                    "Combined TSA sums ONLY exposed outer & inner cavity walls (excluding glued hidden faces); Combined Volume directly sums constituent solids",
                    "Combined TSA always equals sum of individual Total Surface Areas of constituent solids",
                    "1 m³ equals 10,000 cm³",
                    "When a hemisphere is hollowed from a cube, surface area strictly decreases"
                ],
                "answer": 0,
                "hint": "Recall 1 m³ = 100×100×100 = 10⁶ cm³, and cavities add +πr² net to cube TSA!",
                "explanation": "Option 1 states both fundamental Section 12.2 and Section 12.3 principles accurately."
            },
            {
                "question": "Convert volume 338,000 cm³ cleanly into cubic meters (m³) and also convert 3.3 m² into square centimeters (cm²):",
                "options": [
                    "0.338 m³   and   33,000 cm²",
                    "3.38 m³   and   330 cm²",
                    "33.8 m³   and   33,000 cm²",
                    "0.338 m³   and   3,300 cm²"
                ],
                "answer": 0,
                "hint": "Divide cm³ by 10⁶ for m³, and multiply m² by 10⁴ for cm²!",
                "explanation": "338,000 / 1,000,000 = 0.338 m³; 3.3 × 10,000 = 33,000 cm²."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch12 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

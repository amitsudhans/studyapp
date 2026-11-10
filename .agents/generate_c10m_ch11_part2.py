#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 11: Areas Related to Circles
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
        "title": "Horse Grazing Field",
        "subtitle": "Exercise 11.1 Q8: Grazing Quadrant in a 15 m Square Field & Rope Extension From 5 m to 10 m",
        "speech": (
            "Now tour EVERY colorful real world application problem inside Exercise Eleven Point One, starting directly with Question Eight, the Grazing Horse inside a Square Grass Field! "
            "Read every measurement carefully: a horse is tied securely to one corner peg of a square shaped grass field of side fifteen meters by means of a five meter long rope! "
            "Part One asks: find the exact grass area the horse can graze! Because every corner of a square field holds a crisp ninety degree right angle, swinging a five meter taut rope inside the field traces a neat ninety degree QUADRANT of radius five meters! "
            "Compute Quadrant One cleanly using pi equals 3.14: one fourth times 3.14 times 25 equals exact nineteen point six two five square meters! "
            "Part Two increases the rope length from five meters to TEN meters! Since ten meters is still safely shorter than the fifteen meter square fence, the grazed region remains a pure quadrant! Find the exact INCREASE in grazing area! New ten meter quadrant equals one fourth times 3.14 times 100 equals seventy eight point five square meters! Subtracting initial 19.625 leaves exact grazing increase fifty eight point eight seven five square meters!"
        ),
        "checkpoints": [
            {
                "question": "A horse is tied to one corner of a 15 m square field with a 5 m rope, later extended to 10 m (Ex 11.1 Q8, π = 3.14). Find the INCREASE in grazing area:",
                "options": [
                    "58.875 m²   (= 78.5 m² − 19.625 m²)",
                    "78.5 m²",
                    "19.625 m²",
                    "39.25 m²"
                ],
                "answer": 0,
                "hint": "Increase = ¼ × 3.14 × (10² − 5²) = ¼ × 3.14 × 75!",
                "explanation": "78.5 − 19.625 = 58.875 m² (note ¼ π(10² − 5²) skips subtracting separately)."
            },
            {
                "question": "Why does doubling the grazing rope length from 5 m to 10 m QUADRUPLE (4×) total grazing area rather than doubling it?",
                "options": [
                    "Because circular sector area depends on r² (doubling r gives 2² = 4 times the area!)",
                    "Because quadrant angle doubled from 45° to 90°",
                    "Because square perimeter quadrupled",
                    "Because π doubled"
                ],
                "answer": 0,
                "hint": "Notice r² inside Area = (90°/360°) π r²!",
                "explanation": "Since Area ∝ r², doubling radius multiplies grazing area by 2² = 4 (from 19.625 m² to 78.5 m²)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Silver Wire Brooch",
        "subtitle": "Exercise 11.1 Q9: 35 mm Silver Brooch With 5 Diameters Dividing Into 10 Equal Sectors (285 mm Wire)",
        "speech": (
            "Next craft jewelry geometry inside Exercise Eleven Point One Question Nine: the Silver Wire Brooch! Read every piece carefully: "
            "A circular brooch is crafted from fine silver wire with a total circular diameter of thirty five millimeters! Inside the rim, that exact same silver wire is also used to make FIVE straight diameters which divide the circular brooch cleanly into TEN equal pie shaped sectors! "
            "Part One asks: find the TOTAL length of silver wire required! Be careful: students often forget to include the outer circle boundary or double count diameters! Add BOTH pieces cleanly: Outer Circumference equals pi times diameter equals (twenty two over seven) times thirty five equals one hundred ten millimeters! "
            "Plus five straight diameters equal five times thirty five equals one hundred seventy five millimeters! Total silver wire equals 110 plus 175 equals TWO HUNDRED EIGHTY FIVE millimeters! "
            "Part Two asks: Area of EACH of the ten equal sectors! Note each sector subtends thirty six degrees around center O, and radius r equals 35 divided by 2! Divide full circle area cleanly by 10: (1/10) × (22/7) × (35/2)² equals exact three hundred eighty five over four square millimeters (96.25 mm²)!"
        ),
        "checkpoints": [
            {
                "question": "A silver wire brooch has diameter 35 mm and 5 diameters dividing it into 10 equal sectors (Ex 11.1 Q9). Find TOTAL wire length required:",
                "options": [
                    "285 mm   (Circumference 110 mm + 5 Diameters 175 mm)",
                    "110 mm",
                    "175 mm",
                    "320 mm"
                ],
                "answer": 0,
                "hint": "Total Wire = πd + 5d = (22/7)×35 + 5×35!",
                "explanation": "Circumference = (22/7)×35 = 110 mm; 5 diameters = 5×35 = 175 mm; Total = 285 mm."
            },
            {
                "question": "What is the area of EACH of the 10 equal sectors in the 35 mm brooch (Ex 11.1 Q9 ii)?",
                "options": [
                    "385/4 mm²   (= 96.25 mm²)",
                    "385/2 mm²",
                    "770/4 mm²",
                    "385 mm²"
                ],
                "answer": 0,
                "hint": "Radius r = 35/2 mm; Area per sector = (1/10) × (22/7) × (35/2) × (35/2)!",
                "explanation": "(1/10) × (22/7) × (35/2) × (35/2) = (11 × 35)/4 = 385/4 mm²."
            }
        ]
    },
    {
        "id": 11,
        "title": "Umbrella And Wipers",
        "subtitle": "Exercise 11.1 Q10 (8-Rib Umbrella: 22275/28 cm²) & Q11 (Twin Non-Overlapping Car Wipers)",
        "speech": (
            "Now inspect two practical everyday sector machines from Exercise Eleven Point One Questions Ten and Eleven: Umbrellas and Car Windshield Wipers! "
            "First check Question Ten, the 8 Rib Umbrella! Treat an open umbrella approximately as a flat circular disk of radius forty five centimeters containing EIGHT equally spaced ribs! What is the central angle between TWO consecutive ribs? Divide 360 degrees cleanly by 8 ribs to get forty five degrees, or exact fraction one eighth of a full circle! "
            "Find the exact area between two consecutive ribs: one eighth times (22 over 7) times 45 times 45 equals exact fraction 22,275 divided by 28 square centimeters (about 795.54 cm²)! "
            "Next step inside a rainy car for Question Eleven! A car carries TWO identical front windshield wipers that NEVER overlap! Each wiper blade spans length twenty five centimeters sweeping smoothly across central angle one hundred fifteen degrees! "
            "Find the TOTAL glass area cleaned at EACH single sweep of BOTH blades across the glass! First notice one wiper sweeps 158,125 divided by 252 square centimeters! Multiply ONE sector cleanly by TWO blades: 2 × (115/360) × (22/7) × 25 × 25 simplifies cleanly to exact fraction 158,125 divided by 126 square centimeters (1254.96 cm²)!"
        ),
        "checkpoints": [
            {
                "question": "An umbrella has 8 equally spaced ribs forming a flat circle of radius 45 cm (Ex 11.1 Q10, π = 22/7). Area between two consecutive ribs:",
                "options": [
                    "22,275 / 28 cm²   (≈ 795.54 cm²)",
                    "22,275 / 14 cm²",
                    "44,550 / 7 cm²",
                    "2,227.5 cm²"
                ],
                "answer": 0,
                "hint": "8 equal ribs give (1/8) × (22/7) × 45 × 45!",
                "explanation": "(1/8) × (22/7) × 2025 = (11 × 2025)/(4 × 7) = 22,275 / 28 cm²."
            },
            {
                "question": "A car has two non-overlapping wipers each of blade length 25 cm sweeping an angle of 115° (Ex 11.1 Q11). Combined cleaned area per sweep:",
                "options": [
                    "158,125 / 126 cm²   (≈ 1254.96 cm²)",
                    "158,125 / 252 cm²",
                    "79,062.5 / 126 cm²",
                    "62,500 / 7 cm²"
                ],
                "answer": 0,
                "hint": "Two identical wipers = 2 × (115/360) × (22/7) × 25²!",
                "explanation": "2 × (23/72) × (22/7) × 625 = (23 × 11 × 625) / (18 × 7) = 158,125 / 126 cm²."
            }
        ]
    },
    {
        "id": 12,
        "title": "Lighthouse Sea Warning",
        "subtitle": "Exercise 11.1 Q12: Calculating Sea Danger Sector Area (80°, 16.5 km) Spread by a Lighthouse",
        "speech": (
            "Sail straight out to coastal navigation safety in Exercise Eleven Point One Question Twelve! To warn ocean cargo ships away from hidden underwater rocks, a tall coastal lighthouse flashes a bright red warning light beam across a wide circular sector of central angle EIGHTY DEGREES up to a radial distance of SIXTEEN POINT FIVE KILOMETERS! "
            "Find the exact total surface area of the sea over which ships are safely warned! "
            "Read the textbook note carefully: notice pi is specified explicitly as THREE POINT ONE FOUR! Always check which pi approximation (22/7 or 3.14) a question demands before multiplying so your decimal digits stay completely accurate! "
            "Plug angle theta equals eighty degrees, radius r equals sixteen point five kilometers, and pi equals three point one four cleanly into Sector Area! "
            "Simplify fraction eighty over three hundred sixty neatly by dividing numerator and denominator by forty to get TWO NINTHS! Next notice sixteen point five divided by three equals five point five cleanly, TWICE! Canceling denominator nine completely gives 2 × 3.14 × 5.5 × 5.5 = 2 × 3.14 × 30.25 = 60.5 × 3.14 = exact ONE HUNDRED EIGHTY NINE POINT NINE SEVEN square kilometers!"
        ),
        "checkpoints": [
            {
                "question": "A lighthouse spreads red light over a sector of angle 80° to a distance of 16.5 km (Ex 11.1 Q12, use π = 3.14). Sea area warned:",
                "options": [
                    "189.97 km²",
                    "94.985 km²",
                    "379.94 km²",
                    "190.08 km²"
                ],
                "answer": 0,
                "hint": "(80/360) = 2/9; divide BOTH 16.5 factors by 3 cleanly into 5.5 × 5.5 = 30.25!",
                "explanation": "(2/9) × 3.14 × 16.5 × 16.5 = 2 × 3.14 × 5.5 × 5.5 = 189.97 km²."
            },
            {
                "question": "Why does canceling 9 into (16.5 × 16.5) BEFORE multiplying decimals prevent messy rounding mistakes in Question 12?",
                "options": [
                    "Because 16.5 = 3 × 5.5 cleanly, so 16.5² / 9 simplifies EXACTLY to 5.5² = 30.25 with zero repeating decimals!",
                    "Because 9 divides 3.14 evenly",
                    "Because 80/360 equals 1/4",
                    "Because 16.5² equals 200"
                ],
                "answer": 0,
                "hint": "Check divisibility of 1 + 6 + 5 = 12 by 3!",
                "explanation": "Canceling 3 twice turns (16.5 × 16.5)/9 cleanly into exact 5.5 × 5.5 = 30.25."
            }
        ]
    },
    {
        "id": 13,
        "title": "Round Table Cover",
        "subtitle": "Exercise 11.1 Q13: Six Hexagonal Edge Segments on a 28 cm Table Cover & Cost ₹162.68",
        "speech": (
            "Now conquer Exercise Eleven Point One's grand multi step design finale, Question Thirteen: the Round Table Cover with Six Equal Curved Segment Designs! "
            "Picture a round circular table cover of radius twenty eight centimeters bearing SIX symmetric outer curved segment designs wrapping around a central inscribed regular hexagon! Let us calculate the exact cost of making ALL SIX designs at the given rate of thirty five paise (0.35 rupees) per square centimeter, taking square root three equal to one point seven! "
            "Notice TWO equally neat ways to calculate all six segments! Divide 360 degrees by 6 chords: each outer design sits on a 60° minor segment! Since 6 × 60° equals 360°, six 60° sectors combine cleanly into ONE FULL CIRCLE AREA minus SIX EQUILATERAL TRIANGLES (the central regular hexagon)! "
            "Compute Full Circle first: (22/7) × 28 × 28 equals 22 × 4 × 28 equals 2,464 square centimeters! Next compute all 6 equilateral triangles of side 28 cm: 6 × (√3 / 4) × 28 × 28 equals 6 × 1.7 × 7 × 28 equals 1,999.2 square centimeters! "
            "Subtracting gives total design area 464.8 cm²; finally multiplying 464.8 square centimeters by cost rate ₹0.35 delivers exact rupees cost ₹162.68!"
        ),
        "checkpoints": [
            {
                "question": "A round table cover has 6 equal curved designs with radius 28 cm (Ex 11.1 Q13, √3 = 1.7, π = 22/7). Total design area and cost at ₹0.35/cm²:",
                "options": [
                    "Area = 464.8 cm²,   Cost = ₹162.68",
                    "Area = 1999.2 cm²,   Cost = ₹699.72",
                    "Area = 2464 cm²,   Cost = ₹862.40",
                    "Area = 77.47 cm²,   Cost = ₹27.11"
                ],
                "answer": 0,
                "hint": "Total Circle (2464) − Hexagon of 6 equilateral triangles (1999.2) = 464.8 cm²!",
                "explanation": "Design Area = 2464 − 1999.2 = 464.8 cm²; Cost = 464.8 × 0.35 = ₹162.68."
            },
            {
                "question": "Why do 6 equal outer segments around a circle simplify directly into (Full Circle − Inscribed Regular Hexagon)?",
                "options": [
                    "Each of the 6 segments subtends 360°/6 = 60°, forming 6 congruent equilateral triangles inside the circle!",
                    "Because a hexagon has 6 right angles",
                    "Because radius equals side × 2",
                    "Because π = 1.7"
                ],
                "answer": 0,
                "hint": "6 equal chords divide 360° symmetrically into six 60° sectors!",
                "explanation": "Six 60° minor segments equal six sectors (full circle) minus six 60° equilateral triangles (regular hexagon)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Angle Scaling Effects",
        "subtitle": "Exercise 11.1 Q14 Formula Check (p/720 × 2πR²) & How Radius vs Angle Scaling Changes Measures",
        "speech": (
            "Inspect Exercise Eleven Point One Question Fourteen, a clever multiple choice trick that tests algebraic awareness and dimensional reasoning rather than blind memorization! "
            "Question Fourteen asks: tick the correct area of a sector of central angle p (in degrees) inside a circle of radius capital R! Look closely at NCERT's four choices: Choice A gives (p over 180) × 2πR, Choice B gives (p over 180) × πR², Choice C gives (p over 360) × 2πR, and Choice D gives (p over 720) × 2πR²! "
            "Pause and test ALL FOUR options carefully by dimensional units! Choices A and C contain radius R raised to the power ONE—those measure LENGTH in centimeters, never AREA in square centimeters (wrong dimensions immediately)! Choice B uses R squared, yet places 180 in the denominator instead of 360 (making it twice too large)! "
            "Now simplify Choice D cleanly: p over 720 times TWO pi R squared! Notice TWO over 720 simplifies smoothly down to ONE over 360! So Choice D equals exact (p over 360) × π R²! "
            "Finally remember scaling laws: doubling central angle doubles BOTH arc length and sector area (2×), whereas doubling radius doubles arc length (2×) yet QUADRUPLES sector area (4×)!"
        ),
        "checkpoints": [
            {
                "question": "Which option equals the area of a sector of angle p (in degrees) of a circle with radius R (Exercise 11.1 Q14)?",
                "options": [
                    "(p / 720°) × 2πR²   [simplifies cleanly to (p / 360°) × πR²]",
                    "(p / 180°) × 2πR",
                    "(p / 180°) × πR²",
                    "(p / 360°) × 2πR"
                ],
                "answer": 0,
                "hint": "Cancel the extra factor 2 inside numerator 2πR² against denominator 720°!",
                "explanation": "(p / 720) × 2πR² = (p / 360) × πR², whereas choices with R alone give length (not area)."
            },
            {
                "question": "If the central angle stays fixed at 60° while a circle's radius TRIPLES (r → 3r), how do arc length and sector area transform?",
                "options": [
                    "Arc length TRIPLES (3×), while Sector Area becomes NINE TIMES larger (3² = 9×)",
                    "Both become 3× larger",
                    "Arc length becomes 9× and area becomes 3×",
                    "Both remain unchanged"
                ],
                "answer": 0,
                "hint": "Compare l ∝ r¹ against A ∝ r²!",
                "explanation": "Arc length scales linearly with r (3×), whereas sector area scales quadratically with r² (9×)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Triangle Arc Trick",
        "subtitle": "Universal Chord Triangle Area ½ r² sin θ, Concentric Ring π(R² − r²) & Wheel Revolutions",
        "speech": (
            "Before summarizing Chapter Eleven, unlock THREE high utility master geometry shortcuts linking sectors, segments, concentric rings, and rolling wheels together smoothly! "
            "Shortcut One, Universal Segment Triangle Area: earlier you applied three separate rules for chord triangles: half r squared for 90°, root three over four r squared for 60°, and altitude splitting for 120°! Notice ONE compact formula unites ALL acute and obtuse angles cleanly from Chapter Eight Trigonometry: Area of chord triangle OAB equals ONE HALF r squared times SINE THETA! Verify quickly: at 90°, sin 90° = 1 gives ½ r²; at BOTH 60° and 120°, sin 60° = sin 120° = √3/2 gives (√3/4) r² identically! "
            "Shortcut Two, Flat Circular Ring: the area enclosed cleanly between two concentric circles of outer radius capital R and inner radius small r equals pi times (R² − r²), which factors cleanly into pi(R + r)(R − r) for ultra fast mental arithmetic! "
            "Shortcut Three, Rolling Wheel Revolutions: linear distance covered along a flat road in ONE complete wheel rotation equals circumference two pi r! Always match length units first (convert kilometers to meters and radius centimeters to meters cleanly), then divide Total Distance by 2 pi r!"
        ),
        "checkpoints": [
            {
                "question": "A circular wheel of radius r = 35 cm rolls cleanly without slipping along a straight road. How many complete revolutions does it make to travel 11 km (π = 22/7)?",
                "options": [
                    "5,000 revolutions   [Circumference = 2×(22/7)×35 = 220 cm = 2.2 m; 11,000 m ÷ 2.2 m = 5,000]",
                    "2,500 revolutions",
                    "10,000 revolutions",
                    "500 revolutions"
                ],
                "answer": 0,
                "hint": "Always convert BOTH distance and circumference to identical units (meters or cm) before dividing!",
                "explanation": "Circumference = 2×(22/7)×35 = 220 cm = 2.2 m; Revolutions = 11,000 m / 2.2 m = 5,000."
            },
            {
                "question": "What is the area of a flat circular ring bounded between two concentric circles of outer radius 10 cm and inner radius 6 cm?",
                "options": [
                    "64π cm²   [= π(10² − 6²) = π(10+6)(10−6)]",
                    "16π cm²",
                    "40π cm²",
                    "136π cm²"
                ],
                "answer": 0,
                "hint": "Apply π(R² − r²) = π(R + r)(R − r) cleanly!",
                "explanation": "π(10² − 6²) = π(100 − 36) = 64π cm²."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Eleven Summary",
        "subtitle": "Complete Section 11.2 Synthesis: Arc Length, Sector Area & Perimeter, Minor/Major Segments",
        "speech": (
            "Congratulations, geometry masters! You have conquered every derivation, real world problem, and practical engineering exercise inside NCERT Class Ten Chapter Eleven: Areas Related to Circles! Snapshot all five core Section Eleven Point Two formulas onto one crystal clear formula card before entering our forty Interactive Quizzes! "
            "One: A Sector sits bounded cleanly by TWO radii and a curved arc, whereas a Segment sits bounded by ONE straight chord and a curved arc! "
            "Two: Length of an arc of central angle theta equals theta over three hundred sixty degrees times two pi r! "
            "Three: Area of a sector of central angle theta equals theta over three hundred sixty degrees times pi r squared, which also equals ONE HALF times arc length l times radius r! Never forget Sector Perimeter equals arc l plus two straight radii 2r! "
            "Four: Area of a Minor Segment equals Area of Corresponding Sector MINUS Area of Triangle OAB (using ½ r² for 90° and √3/4 r² for BOTH 60° and 120°)! "
            "Five: Major Sector or Major Segment ALWAYS equals Full Circle Area pi r squared minus its corresponding minor counterpart! Always double check whether the question specifies pi equals 22/7 or 3.14!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement across NCERT Chapter 11 is 100% mathematically accurate?",
                "options": [
                    "Arc l = (θ/360°)2πr; Sector Area = (θ/360°)πr² = ½lr; Sector Perimeter = l + 2r; Minor Segment = Sector − △OAB",
                    "Sector Perimeter equals arc length l alone",
                    "Major Segment equals Major Sector minus △OAB",
                    "120° chord triangle area is ½ r²"
                ],
                "answer": 0,
                "hint": "Check Sector Perimeter (must include +2r!) and Major Segment (must add, not subtract, △OAB)!",
                "explanation": "Option 1 accurately records all Chapter 11 sector, arc, perimeter, and segment formulas."
            },
            {
                "question": "If the perimeter of a semicircular protractor of radius r is 36 cm (take π = 22/7), find radius r:",
                "options": [
                    "7 cm   (since πr + 2r = r(22/7 + 2) = (36/7)r = 36)",
                    "14 cm",
                    "3.5 cm",
                    "11 cm"
                ],
                "answer": 0,
                "hint": "A semicircular protractor's perimeter is semicircular arc πr PLUS straight diameter 2r!",
                "explanation": "r(22/7 + 2) = r(36/7) = 36 ⟹ r = 7 cm!"
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch11 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

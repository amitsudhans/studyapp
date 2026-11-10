#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 11: Areas Related to Circles
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
        "title": "Sectors And Segments",
        "subtitle": "Section 11.1 Foundations: Minor vs Major Sectors (Radii + Arc) & Minor vs Major Segments (Chord + Arc)",
        "speech": (
            "Welcome to NCERT Class Ten Chapter Eleven: Areas Related to Circles! You already know how to calculate full circle circumference two pi r and full circle area pi r squared from earlier classes. Now let us slice a circular disk cleanly into TWO famous geometric pieces: Sectors and Segments! "
            "First picture slicing a round pizza straight from its exact center point O out to two points A and B on the circular boundary! The wedge-shaped circular region enclosed cleanly by TWO radii OA and OB together with the curved boundary arc APB is called a SECTOR of the circle! "
            "Notice TWO sectors appear immediately whenever you cut two radii: the smaller wedge with central angle less than 180 degrees is the MINOR SECTOR OAPB, whereas the remaining large wedge is the MAJOR SECTOR OAQB! "
            "Next picture cutting a round pancake with ONE straight knife cut joining points A and B directly—that straight line segment AB is a CHORD! The circular region enclosed between a straight chord AB and its curved arc APB is called a SEGMENT of the circle! "
            "Again, the smaller dome is the MINOR SEGMENT, while the large region holding the circle center is the MAJOR SEGMENT!"
        ),
        "checkpoints": [
            {
                "question": "Which exact boundary pieces enclose a circular SECTOR versus a circular SEGMENT?",
                "options": [
                    "Sector: TWO radii + corresponding arc;   Segment: ONE straight chord + corresponding arc",
                    "Sector: ONE chord + arc;   Segment: TWO radii + arc",
                    "Both are enclosed by two chords",
                    "Sector encloses only the perimeter without interior area"
                ],
                "answer": 0,
                "hint": "Think pizza slice (two straight cuts to the center O = Sector) vs straight crust slice (one chord = Segment)!",
                "explanation": "A sector is enclosed by two radii and an arc, whereas a segment is enclosed by a chord and an arc."
            },
            {
                "question": "If Minor Sector OAPB subtends central angle θ = 75° at the center, what central angle subtends the Major Sector OAQB?",
                "options": [
                    "285°   (= 360° − 75°)",
                    "105°   (= 180° − 75°)",
                    "75°",
                    "195°"
                ],
                "answer": 0,
                "hint": "Minor Sector + Major Sector complete one full circle around the center (360°)!",
                "explanation": "Full angle around center O is 360°, so Major Sector angle = 360° − 75° = 285°."
            }
        ]
    },
    {
        "id": 2,
        "title": "Sector Area Formula",
        "subtitle": "Unitary Method Derivation: (θ / 360°) × πr², Plus Major Sector = πr² − Minor Sector",
        "speech": (
            "Let us derive the exact Area of a Sector from scratch using the classic Unitary Method so you never have to memorize blindly! Think of the full circular region as ONE giant complete sector around center O! "
            "When the two bounding radii sweep all the way around to complete central angle three hundred sixty degrees, the total circular area enclosed equals pi r squared! "
            "Therefore, by the unitary method, when the central angle is just ONE DEGREE, how much circular area is enclosed? Divide by three hundred sixty: Area for 1 degree equals pi r squared divided by 360! "
            "Now multiply cleanly by ANY central angle theta degrees! Area of Sector of angle theta equals theta divided by three hundred sixty degrees, multiplied by pi r squared! "
            "Test quick fractions right away: when theta equals 90 degrees, 90 over 360 equals ONE FOURTH, giving quadrant area one fourth pi r squared! When theta equals 180 degrees, 180 over 360 equals ONE HALF, giving semicircle area one half pi r squared! "
            "And whenever you need Major Sector Area, either compute (360 minus theta) over 360 times pi r squared, or even faster: subtract Minor Sector from Full Circle pi r squared!"
        ),
        "checkpoints": [
            {
                "question": "Using the unitary method, why does a sector of central angle θ° have area (θ / 360°) × πr²?",
                "options": [
                    "Because 360° encloses πr², so 1° encloses πr²/360°, and θ° encloses θ × (πr²/360°)",
                    "Because 180° encloses πr²",
                    "Because circumference is 2πr",
                    "Because sector area is independent of radius"
                ],
                "answer": 0,
                "hint": "Proportional fraction of the full 360° turn multiplies the full circle area πr²!",
                "explanation": "Full 360° has area πr²; unitary division gives πr²/360° per degree, so θ° yields (θ/360°) × πr²."
            },
            {
                "question": "Find the area of a sector of radius 4 cm with angle 30°, and also the corresponding MAJOR sector area (use π = 3.14, Textbook Example 1):",
                "options": [
                    "Minor = 4.19 cm² (approx.),   Major = 46.05 cm² (approx.)",
                    "Minor = 8.38 cm²,   Major = 41.86 cm²",
                    "Minor = 4.19 cm²,   Major = 25.12 cm²",
                    "Minor = 12.56 cm²,   Major = 37.68 cm²"
                ],
                "answer": 0,
                "hint": "Minor = (30/360)×3.14×16 = 50.24/12 ≈ 4.19 cm²; Major = 3.14×16 − 4.19 ≈ 46.05 cm²!",
                "explanation": "Minor Sector = (1/12)×3.14×16 = 4.19 cm²; Major Sector = 50.24 − 4.19 = 46.05 cm²."
            }
        ]
    },
    {
        "id": 3,
        "title": "Arc Length Formula",
        "subtitle": "Unitary Arc Length l = (θ / 360°) × 2πr, Shortcut Area = ½ l r & Sector Perimeter = l + 2r",
        "speech": (
            "Now apply that EXACT same unitary reasoning to find the curved rim length along the circle—the Length of an Arc! "
            "When a central angle sweeps a full complete turn of three hundred sixty degrees, the boundary length traced all around equals total circumference two pi r! "
            "Dividing by three hundred sixty gives arc length for ONE degree equals two pi r over 360! Multiplying by theta gives the golden Arc Length formula: l equals theta divided by three hundred sixty degrees, multiplied by two pi r! "
            "Watch what magical shortcut pops out when you compare Sector Area against Arc Length! Write Sector Area as one half times [(theta over 360) times two pi r] times r! Inside those brackets sits exact arc length l! Therefore, Sector Area ALWAYS equals ONE HALF times arc length l times radius r—looking just like triangle area one half base times height! "
            "Also watch ONE crucial board exam trap on Sector Perimeter! Perimeter of a sector is NOT just curved arc length l alone! A closed sector is bounded by arc l PLUS TWO straight radii r and r meeting at center O! So ALWAYS compute Sector Perimeter equal to l plus two r!"
        ),
        "checkpoints": [
            {
                "question": "A sector has arc length l = 11 cm and radius r = 7 cm. Find BOTH its Sector Area AND its complete Sector Perimeter:",
                "options": [
                    "Area = 38.5 cm² (= ½ × 11 × 7),   Perimeter = 25 cm (= 11 + 2×7)",
                    "Area = 77 cm²,   Perimeter = 11 cm",
                    "Area = 38.5 cm²,   Perimeter = 18 cm",
                    "Area = 19.25 cm²,   Perimeter = 25 cm"
                ],
                "answer": 0,
                "hint": "Use Area = ½ l r and Perimeter = l + 2r!",
                "explanation": "Area = ½ × 11 × 7 = 77/2 = 38.5 cm²; Perimeter = 11 + 7 + 7 = 25 cm."
            },
            {
                "question": "Why does Sector Area = ½ × l × r hold identically for EVERY central angle θ?",
                "options": [
                    "Because ½ × [(θ/360°)×2πr] × r cancels 2 and simplifies directly to (θ/360°)×πr²",
                    "Because l equals πr²",
                    "Because a sector has three straight sides",
                    "Because θ cancels radius r"
                ],
                "answer": 0,
                "hint": "Substitute l = (θ/360°)×2πr into ½ × l × r!",
                "explanation": "½ × [(θ/360°)2πr] × r = (θ/360°)πr² identically for all θ and r."
            }
        ]
    },
    {
        "id": 4,
        "title": "Quadrant Area Applications",
        "subtitle": "Exercise 11.1 Q1 (60° Sector, r=6 → 132/7 cm²) & Q2 (Quadrant From Circumference 22 cm → 77/8 cm²)",
        "speech": (
            "Let us launch directly into Exercise Eleven Point One Questions One and Two to cement speed and fraction accuracy! Keep exact fractions wherever possible when taking pi equals twenty two over seven! "
            "Check Question One: Find the area of a sector of a circle with radius six centimeters if the angle of the sector is sixty degrees! Plug theta equals sixty and radius r equals six cleanly: (60 over 360) times (22 over 7) times 6 times 6! Simplify 60 over 360 to one sixth, cancel one six cleanly with denominator six, leaving exact numerator 22 times 6 equals 132 over 7 square centimeters! Leave 132/7 cm² neatly without messy rounding unless requested! "
            "Now solve Question Two, a classic two-step board favorite: Find the area of a QUADRANT of a circle whose circumference is twenty two centimeters! "
            "Step One: Decode radius from circumference 2 pi r equals 22! Two times (22 over 7) times r equals 22 simplifies immediately to r equals seven over two centimeters (3.5 cm)! "
            "Step Two: A quadrant means ONE FOURTH of a circle (theta = 90°)! Compute one fourth × (22/7) × (7/2) × (7/2) = exact seventy seven over eight square centimeters!"
        ),
        "checkpoints": [
            {
                "question": "Find the area of a sector with radius r = 6 cm and central angle θ = 60° (Ex 11.1 Q1, π = 22/7):",
                "options": [
                    "132/7 cm²",
                    "66/7 cm²",
                    "264/7 cm²",
                    "44/7 cm²"
                ],
                "answer": 0,
                "hint": "(60/360) × (22/7) × 6 × 6 cancels one factor of 6!",
                "explanation": "(1/6) × (22/7) × 36 = (22 × 6)/7 = 132/7 cm²."
            },
            {
                "question": "Find the area of a quadrant of a circle whose circumference is 22 cm (Ex 11.1 Q2, π = 22/7):",
                "options": [
                    "77/8 cm²   (= 9.625 cm²)",
                    "77/4 cm²",
                    "77/2 cm²",
                    "154/8 cm²"
                ],
                "answer": 0,
                "hint": "2×(22/7)×r = 22 gives r = 7/2 cm; Quadrant = ¼ π r²!",
                "explanation": "r = 7/2 cm; Quadrant Area = ¼ × (22/7) × (7/2) × (7/2) = 77/8 cm²."
            }
        ]
    },
    {
        "id": 5,
        "title": "Clock Hand Sweeps",
        "subtitle": "Exercise 11.1 Q3: Minute Hand Angular Speed (6°/min) & 5-Minute Sweep Area (154/3 cm²)",
        "speech": (
            "Now inspect every rotating clock face through Exercise Eleven Point One Question Three! Read the problem carefully: The length of the minute hand of a clock is fourteen centimeters! Find the area swept by the minute hand in FIVE MINUTES! "
            "Think visually! As the minute hand rotates cleanly around the clock center, its length fourteen centimeters acts directly as the circle RADIUS r = 14 cm! "
            "Wait—what central angle theta does a clock's minute hand sweep in five minutes? Let us compute its exact angular speed! One complete rotation around a circular clock takes SIXTY MINUTES and sweeps three hundred sixty degrees! "
            "Therefore, in ONE SINGLE MINUTE, the minute hand rotates 360 divided by 60 equals SIX DEGREES per minute! Remember that golden constant: Minute Hand moves 6° per minute! "
            "In FIVE MINUTES, central angle theta equals 5 times 6 equals THIRTY DEGREES (one twelfth of the clock face)! "
            "Plug r = 14 cm and theta = 30° cleanly into Sector Area: (30 over 360) × (22 over 7) × 14 × 14! Simplify: (1/12) × 22 × 2 × 14 = 616 / 12 = exact ONE HUNDRED FIFTY FOUR OVER THREE square centimeters!"
        ),
        "checkpoints": [
            {
                "question": "What central angle does a clock's minute hand sweep per minute, and in 5 minutes?",
                "options": [
                    "6° per minute;   30° in 5 minutes",
                    "12° per minute;   60° in 5 minutes",
                    "3° per minute;   15° in 5 minutes",
                    "30° per minute;   150° in 5 minutes"
                ],
                "answer": 0,
                "hint": "Full 360° circle takes 60 minutes, so 1 minute = 360° ÷ 60!",
                "explanation": "360° / 60 = 6° per minute; therefore 5 minutes sweeps 5 × 6° = 30°."
            },
            {
                "question": "A clock's minute hand is 14 cm long (Ex 11.1 Q3, π = 22/7). Find the exact area swept in 5 minutes:",
                "options": [
                    "154/3 cm²",
                    "154 cm²",
                    "77/3 cm²",
                    "308/3 cm²"
                ],
                "answer": 0,
                "hint": "Area = (30/360) × (22/7) × 14 × 14 = (1/12) × 616!",
                "explanation": "(1/12) × (22/7) × 14 × 14 = 616 / 12 = 154/3 cm² (51.33 cm² approx)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Circular Segment Method",
        "subtitle": "Core Deduction: Minor Segment = Sector − △OAB, Ex 11.1 Q4 (Right-Angled Segment r=10 → 28.5 cm²)",
        "speech": (
            "Now conquer the centerpiece deduction of Section Eleven Point One: calculating the exact area of a Circular Segment! "
            "Look carefully at a Minor Sector OAPB split cleanly by straight chord AB! Notice the Sector consists of TWO disjoint puzzle pieces fitting edge to edge: central Triangle OAB PLUS outer Minor Segment APB! "
            "Therefore, isolating the Minor Segment requires ONE crisp geometric subtraction: Area of Minor Segment APB equals Area of Corresponding Sector OAPB MINUS Area of Triangle OAB! And once you know Minor Segment, Major Segment equals Full Circle Area pi r squared MINUS Minor Segment! "
            "Test this immediately on Exercise Eleven Point One Question Four! A chord of a circle of radius ten centimeters subtends a right angle (90°) at the center (use pi = 3.14)! Find (i) minor segment and (ii) major sector! "
            "Step One: Minor Sector equals one fourth × 3.14 × 10 × 10 equals 78.5 cm²! "
            "Step Two: Since angle AOB equals ninety degrees, Triangle OAB is a right triangle with legs ten and ten! Area of triangle equals one half × 10 × 10 equals 50 cm²! "
            "Step Three: Minor Segment equals 78.5 minus 50 equals exact TWENTY EIGHT POINT FIVE cm²! Major Sector equals 314 minus 78.5 equals 235.5 cm²!"
        ),
        "checkpoints": [
            {
                "question": "A chord of a circle of radius 10 cm subtends a 90° right angle at the center (Ex 11.1 Q4, π = 3.14). Find BOTH Minor Segment and Major Sector areas:",
                "options": [
                    "Minor Segment = 28.5 cm²,   Major Sector = 235.5 cm²",
                    "Minor Segment = 78.5 cm²,   Major Sector = 235.5 cm²",
                    "Minor Segment = 50 cm²,   Major Sector = 264 cm²",
                    "Minor Segment = 28.5 cm²,   Major Sector = 285.5 cm²"
                ],
                "answer": 0,
                "hint": "Minor Sector = ¼×314 = 78.5; Triangle = ½×10×10 = 50; subtract!",
                "explanation": "Minor Segment = 78.5 − 50 = 28.5 cm²; Major Sector = 314 − 78.5 = 235.5 cm²."
            },
            {
                "question": "Once Minor Segment Area is known, which formula computes Major Segment Area?",
                "options": [
                    "Full Circle Area πr² − Minor Segment Area",
                    "Major Sector Area − Area(△OAB)",
                    "Full Circle Area πr² − Minor Sector Area",
                    "2 × Minor Segment Area"
                ],
                "answer": 0,
                "hint": "Major Segment equals Major Sector PLUS △OAB—or equivalently Full Circle minus Minor Segment!",
                "explanation": "Minor Segment + Major Segment = Full Circle πr², so Major Segment = πr² − Minor Segment."
            }
        ]
    },
    {
        "id": 7,
        "title": "Equilateral Chord Segments",
        "subtitle": "60° Angle Geometry: Ex 11.1 Q5 (r=21 cm: Arc 22 cm, Sector 231 cm², Segment) & Q6 (r=15 cm, π=3.14)",
        "speech": (
            "What happens when the chord subtends SIXTY DEGREES at the circle center instead of ninety degrees? Look at Triangle OAB! Two sides OA and OB are BOTH circle radii equal to r, making base angles equal! Since apex angle is 60 degrees, the remaining 120 degrees splits cleanly into 60 degrees and 60 degrees—meaning Triangle OAB is a pure EQUILATERAL TRIANGLE of side r! "
            "Recall equilateral triangle area equals (root three over four) times r squared! "
            "Apply this immediately to Exercise Eleven Point One Question Five (circle radius 21 cm, angle 60°, pi = 22/7)! "
            "Part (i) Arc length equals (60/360) × 2 × (22/7) × 21 equals exact TWENTY TWO centimeters! "
            "Part (ii) Sector Area equals (60/360) × (22/7) × 21 × 21 equals exact TWO HUNDRED THIRTY ONE square centimeters! "
            "Part (iii) Minor Segment equals 231 minus (441 root 3 over 4) square centimeters! "
            "Now check Question Six (radius 15 cm, angle 60°, pi = 3.14, root 3 = 1.73): Minor Sector equals one sixth × 3.14 × 225 equals 117.75 cm²; Equilateral triangle equals (1.73/4) × 225 equals 97.3125 cm²! Subtracting yields Minor Segment 20.4375 cm², and Major Segment 706.5 minus 20.4375 equals 686.0625 cm²!"
        ),
        "checkpoints": [
            {
                "question": "Why is △OAB always an EQUILATERAL triangle whenever central angle θ = 60°?",
                "options": [
                    "Because OA = OB = r makes base angles equal: (180° − 60°)/2 = 60° each, so all three angles equal 60°!",
                    "Because every chord equals diameter",
                    "Because 60° is half of 120°",
                    "Because arc AB equals chord AB"
                ],
                "answer": 0,
                "hint": "Equal radii OA = OB force ∠OAB = ∠OBA!",
                "explanation": "OA = OB implies ∠OAB = ∠OBA = (180° − 60°)/2 = 60°, forming an equilateral triangle of side r."
            },
            {
                "question": "In a circle of radius 21 cm, an arc subtends 60° at the centre (Ex 11.1 Q5, π = 22/7). Find (i) Arc length, (ii) Sector Area, and (iii) Segment Area:",
                "options": [
                    "Arc = 22 cm,   Sector = 231 cm²,   Segment = (231 − 441√3 / 4) cm²",
                    "Arc = 44 cm,   Sector = 462 cm²,   Segment = (462 − 441√3 / 2) cm²",
                    "Arc = 22 cm,   Sector = 231 cm²,   Segment = (231 − 441/2) cm²",
                    "Arc = 11 cm,   Sector = 115.5 cm²,   Segment = (115.5 − 441√3 / 4) cm²"
                ],
                "answer": 0,
                "hint": "Use (1/6)×2πr, (1/6)×πr², and subtract equilateral (√3/4)r²!",
                "explanation": "Arc = 22 cm; Sector = ½ × 22 × 21 = 231 cm²; Segment = 231 − (441√3/4) cm²."
            }
        ]
    },
    {
        "id": 8,
        "title": "Obtuse Segment Splitting",
        "subtitle": "Textbook Example 3 & Ex 11.1 Q7: 120° Chord Altitude Splitting via Trigonometry → 88.44 cm²",
        "speech": (
            "Now master one of the finest derivations in Class Ten Trigonometry plus Circles—solving a ONE HUNDRED TWENTY DEGREE obtuse chord segment, featured in Textbook Example Three AND Exercise Eleven Point One Question Seven! "
            "Take radius r = 12 cm and central angle 120 degrees (pi = 3.14, root 3 = 1.73)! First compute Sector Area easily: (120 over 360) equals ONE THIRD of circle: (1/3) × 3.14 × 12 × 12 equals exact 150.72 cm²! "
            "Next, how do we find obtuse isosceles Triangle OAB area cleanly? Draw altitude OM perpendicular from center O straight onto chord AB! Because Triangle OAB is isosceles (OA = OB), perpendicular OM cleanly BISECTS BOTH angle AOB (into two crisp 60° right triangles!) AND chord AB (AM = MB)! "
            "In right triangle OMA: cos 60° = OM / 12 gives height OM = 6 cm, while sin 60° = AM / 12 gives half base AM = 6 root 3 cm, so full chord AB = 12 root 3 cm! "
            "Area of Triangle OAB equals ½ × AB × OM = ½ × 12 root 3 × 6 = 36 × 1.73 = 62.28 cm²! Subtracting leaves Minor Segment 150.72 minus 62.28 equals exact 88.44 cm²!"
        ),
        "checkpoints": [
            {
                "question": "For an isosceles △OAB with OA = OB = 12 cm and ∠AOB = 120°, drawing OM ⊥ AB gives what exact height OM and full chord length AB?",
                "options": [
                    "OM = 6 cm,   AB = 12√3 cm",
                    "OM = 6√3 cm,   AB = 12 cm",
                    "OM = 6 cm,   AB = 6√3 cm",
                    "OM = 12 cm,   AB = 24 cm"
                ],
                "answer": 0,
                "hint": "∠AOM = 60°, hypotenuse OA = 12 cm → OM = 12 cos 60°, AM = 12 sin 60°, AB = 2 AM!",
                "explanation": "OM = 12 × ½ = 6 cm; AM = 12 × (√3/2) = 6√3 cm; AB = 2 AM = 12√3 cm."
            },
            {
                "question": "A chord of a circle of radius 12 cm subtends 120° at the centre (Ex 11.1 Q7, π = 3.14, √3 = 1.73). Find Minor Segment Area:",
                "options": [
                    "88.44 cm²   (= 150.72 − 62.28)",
                    "150.72 cm²",
                    "62.28 cm²",
                    "114.72 cm²"
                ],
                "answer": 0,
                "hint": "Sector = (1/3)×3.14×144 = 150.72; △OAB = ½×(12√3)×6 = 36×1.73 = 62.28!",
                "explanation": "Sector = 150.72 cm²; △OAB = 62.28 cm²; Segment = 150.72 − 62.28 = 88.44 cm²."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch11 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

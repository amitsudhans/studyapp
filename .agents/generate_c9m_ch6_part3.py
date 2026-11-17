#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 6: Measuring Space: Perimeter and Area
Slides Data Generator - Part 3 (Slides 17 to 20 - Silent Mastery Quizzes, 40 Questions Total)
Strictly 1-3 word titles, zero spoken audio, zero human names, hints + 3-step solutions.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Pi Arcs Quiz",
        "subtitle": "Sections 6.1–6.5 Practice Set (10 Questions): Perimeters, π History & Irrationality, Arc Lengths, Track Staggers & Path Puzzles",
        "questions": [
            {
                "question": "What is the total closed perimeter of a semicircular protractor whose straight diameter measures 14 cm (use π ≈ 22/7)?",
                "options": ["36 cm (curved πr + straight diameter 2r = 22 + 14)", "22 cm", "44 cm", "154 cm"],
                "answer": 0,
                "hint": "Don't forget the straight closing diameter edge along the bottom of the protractor!",
                "explanation": "Closed semicircle perimeter = πr + 2r = (22/7)(7) + 14 = 22 + 14 = 36 cm.",
                "solution_steps": [
                    "Identify radius r = 14 / 2 = 7 cm.",
                    "Compute curved semicircular arc = πr = (22/7) × 7 = 22 cm.",
                    "Add straight diameter closing boundary: 22 + 14 = 36 cm."
                ]
            },
            {
                "question": "Which mathematician rigorously proved in 1761 that π is genuinely an IRRATIONAL number?",
                "options": ["Johann Heinrich Lambert", "Archimedes", "Zu Chongzhi", "Mādhava of Saṅgamagrāma"],
                "answer": 0,
                "hint": "Check Section 6.3 π is Irrational!",
                "explanation": "Johann Lambert proved π irrational in 1761 using continued fractions.",
                "solution_steps": [
                    "Ancient scholars found ever-closer rational approximations like 22/7 and 355/113.",
                    "In 1761, Johann Heinrich Lambert gave the first rigorous proof that π ≠ p/q.",
                    "Hence decimal digits of π never terminate and never repeat periodically."
                ]
            },
            {
                "question": "Match these historical π approximations cleanly: (i) Mesopotamia c. 1900 BCE, (ii) Zu Chongzhi 480 CE, (iii) Āryabhaṭa 499 CE.",
                "options": ["(i) 3.125, (ii) 355/113, (iii) 3.1416", "(i) 355/113, (ii) 3.125, (iii) 22/7", "(i) 3.1416, (ii) 3.125, (iii) √10", "(i) √10, (ii) 3.14, (iii) 355/113"],
                "answer": 0,
                "hint": "Mesopotamia used 3 1/8 = 3.125; Zu Chongzhi found 355/113; Āryabhaṭa gave 3927/1250 = 3.1416!",
                "explanation": "Mesopotamia: 3.125 (inscribed hexagon ratio); Zu Chongzhi: 355/113; Āryabhaṭa: 3.1416.",
                "solution_steps": [
                    "Mesopotamian clay tablets refined hexagon ratio to 25/8 = 3.125.",
                    "Zu Chongzhi (480 CE) used 24,576-gons to discover 355/113.",
                    "Āryabhaṭa (499 CE) calculated 62832/20000 = 3.1416."
                ]
            },
            {
                "question": "Calculate the arc length of a quarter circle of radius r = 28 cm (use π ≈ 22/7).",
                "options": ["44 cm", "88 cm", "22 cm", "176 cm"],
                "answer": 0,
                "hint": "Quarter circle arc = (πr)/2 = (22/7 × 28) / 2!",
                "explanation": "Arc = 2πr × (90°/360°) = πr / 2 = (22/7 × 28)/2 = 88/2 = 44 cm.",
                "solution_steps": [
                    "A quarter circle spans central angle θ = 90° (1/4 of a circle).",
                    "Apply ½ πr = ½ × (22/7) × 28.",
                    "Simplify: ½ × 88 = 44 cm."
                ]
            },
            {
                "question": "On a 400 m athletic track, each straight section measures 84.39 m and two semicircular bends enclose inner lane radius r = 36.8 m. If outer lane 2 widens radius by w = 1.22 m, approximately how much extra distance (stagger) must Lane 2 cover around ONE full lap (use π ≈ 3.1416)?",
                "options": ["≈ 7.67 m (2πw = 2 × 3.1416 × 1.22)", "≈ 3.83 m", "≈ 1.22 m", "≈ 15.33 m"],
                "answer": 0,
                "hint": "Straight sections match identically; two semicircular bends equal ONE complete extra ring circumference 2πw!",
                "explanation": "Extra curve length = 2π(r + w) − 2πr = 2πw ≈ 2 × 3.1416 × 1.22 ≈ 7.67 m.",
                "solution_steps": [
                    "Notice both straight runs stay equal (2 × 84.39 m) across all lanes.",
                    "Two semicircular ends combine into one full circle: inner C₁ = 2πr, outer C₂ = 2π(r + w).",
                    "Difference = 2πw ≈ 6.2832 × 1.22 ≈ 7.67 m stagger ahead!"
                ]
            },
            {
                "question": "Path P connects points X and Y via one large semicircle of diameter 20 cm. Path Q connects X and Y via 4 small equal semicircles of diameter 5 cm each. Compare the lengths of Path P and Path Q.",
                "options": ["Path P = Path Q = 10π cm identically", "Path P is 4 times longer", "Path Q is twice as long as Path P", "Path P is longer by 5 cm"],
                "answer": 0,
                "hint": "Sum 4 × (π × 5 / 2) and compare against π × 20 / 2!",
                "explanation": "Path P = 10π cm; Path Q = 4 × (2.5π) = 10π cm. Identical total arc length!",
                "solution_steps": [
                    "Path P length = ½(π × D) = ½(π × 20) = 10π cm.",
                    "Path Q length = 4 × ½(π × 5) = 2 × 5π = 10π cm.",
                    "Because sum of sub-diameters equals 20 cm, both paths match!"
                ]
            },
            {
                "question": "An arc of radius 18 cm has curved length 15π cm. What central angle θ° does this arc subtend at the centre?",
                "options": ["150°", "120°", "75°", "300°"],
                "answer": 0,
                "hint": "Solve 2π(18) × (θ° / 360°) = 15π for θ!",
                "explanation": "36π(θ/360) = 15π ⇒ θ/10 = 15 ⇒ θ = 150°.",
                "solution_steps": [
                    "Full circumference = 2πr = 2π(18) = 36π cm.",
                    "Set arc fraction: 36π × (θ/360) = 15π.",
                    "Divide by π and simplify: θ/10 = 15 ⇒ θ = 150°."
                ]
            },
            {
                "question": "Why are Archimedes' 96-gon bounds written cleanly as 3 10/71 < π < 3 1/7?",
                "options": [
                    "Inscribed 96-gon perimeter < circle circumference < circumscribed 96-gon perimeter",
                    "Circle area is strictly greater than any circumscribed polygon",
                    "Archimedes used 96 circles instead of polygons",
                    "3 10/71 equals 355/113"
                ],
                "answer": 0,
                "hint": "Think geometrically: an inner polygon stays strictly shorter than the curved circle, while an outer tangent polygon stays strictly longer!",
                "explanation": "Bounding circumference between inner (223/71) and outer (22/7) 96-gons tightly traps π!",
                "solution_steps": [
                    "Every inscribed polygon lies inside the circle with shorter straight chords ⇒ lower bound 3 10/71.",
                    "Every circumscribed polygon wraps around the outside ⇒ upper bound 3 1/7 = 22/7.",
                    "At 96 sides, these squeeze π between 3.1408... and 3.1428..."
                ]
            },
            {
                "question": "If the perimeter of a semicircular garden equals 72 m (closed boundary, use π ≈ 22/7), what is its radius r?",
                "options": ["14 m", "7 m", "21 m", "28 m"],
                "answer": 0,
                "hint": "Set πr + 2r = r(22/7 + 2) = r(36/7) = 72!",
                "explanation": "r(22/7 + 2) = (36/7)r = 72 ⇒ r = 72 × 7 / 36 = 14 m.",
                "solution_steps": [
                    "Write closed semicircle perimeter: πr + 2r = r(π + 2).",
                    "Substitute π ≈ 22/7: r(22/7 + 14/7) = (36/7)r = 72.",
                    "Solve for radius: r = 72 × 7 / 36 = 14 m."
                ]
            },
            {
                "question": "Which formula matches Mādhava's 14th-century Kerala School series for π?",
                "options": ["π = 4 × (1 − 1/3 + 1/5 − 1/7 + 1/9 − ...)", "π = 4 × (1 + 1/2 + 1/3 + ...)", "π = 3 + 1/7 − 1/10", "π = √(2 + 3 + 5)"],
                "answer": 0,
                "hint": "Recall Section 6.2 Historical Approximations!",
                "explanation": "Mādhava proved π/4 = 1 − 1/3 + 1/5 − 1/7 + ... alternating over odd reciprocals.",
                "solution_steps": [
                    "Mādhava analyzed arctan(1) = π/4 via infinite power series.",
                    "Evaluating at x = 1 yields alternating odd reciprocals: 1 − 1/3 + 1/5 − 1/7 + ...",
                    "Multiplying both sides by 4 gives π = 4(1 − 1/3 + 1/5 − 1/7 + ...)."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Polygon Heron Quiz",
        "subtitle": "Sections 6.6–6.9 Practice Set (10 Questions): Parallelogram Height, Triangle Medians, Heron, R & r Circles, Brahmagupta & Baudhāyana",
        "questions": [
            {
                "question": "A parallelogram ABCD has base AB = 18 cm, slanted side AD = 12 cm, and perpendicular altitude h = 7 cm between AB and CD (falling outside AB). Find its area.",
                "options": ["126 cm²", "216 cm²", "63 cm²", "84 cm²"],
                "answer": 0,
                "hint": "Parallelogram area ALWAYS uses base × perpendicular altitude, even for oblique angles!",
                "explanation": "Area = base × height = 18 × 7 = 126 cm².",
                "solution_steps": [
                    "Ignore slanted side AD = 12 cm for area calculation.",
                    "Use vertical perpendicular height h = 7 cm corresponding to base AB = 18 cm.",
                    "Compute Area = 18 × 7 = 126 cm²."
                ]
            },
            {
                "question": "In ΔABC, median BE joins vertex B to midpoint E of AC, and median EF splits ΔBEC. If Area(ΔABC) = 80 cm², what is Area(ΔABE)?",
                "options": ["40 cm²", "20 cm²", "80 cm²", "16 cm²"],
                "answer": 0,
                "hint": "Every median divides its triangle into two equal-area halves!",
                "explanation": "Median BE splits ΔABC into equal-area halves ΔABE and ΔCBE: 80 / 2 = 40 cm².",
                "solution_steps": [
                    "Point E is the midpoint of AC, so AE = EC.",
                    "Triangles ABE and CBE share identical perpendicular altitude from vertex B.",
                    "Equal bases + equal height ⇒ Area(ΔABE) = ½ Area(ΔABC) = 40 cm²."
                ]
            },
            {
                "question": "Using Heron's formula, calculate the exact area of a triangular park whose sides measure 9 m, 12 m, and 15 m.",
                "options": ["54 m²", "108 m²", "36 m²", "67.5 m²"],
                "answer": 0,
                "hint": "Semi-perimeter s = (9 + 12 + 15)/2 = 18; compute √(18 × 9 × 6 × 3)!",
                "explanation": "s = 18 ⇒ Area = √(18 × 9 × 6 × 3) = √(2916) = 54 m².",
                "solution_steps": [
                    "Compute semi-perimeter s = (9 + 12 + 15)/2 = 18 m.",
                    "Find differences: s − a = 9, s − b = 6, s − c = 3.",
                    "Area = √(18 × 9 × 6 × 3) = √((18 × 3) × (9 × 6)) = √(54 × 54) = 54 m²."
                ]
            },
            {
                "question": "An equilateral triangle has side length a = 12 cm. Use Heron's formula to find its exact area.",
                "options": ["36√3 cm²", "72√3 cm²", "144√3 cm²", "18√3 cm²"],
                "answer": 0,
                "hint": "Semi-perimeter s = 18, and all three differences s − a equal 6!",
                "explanation": "Area = √(18 × 6 × 6 × 6) = 6 × 6√(3) = 36√3 cm².",
                "solution_steps": [
                    "Compute s = (12 + 12 + 12)/2 = 18 cm; s − a = 18 − 12 = 6 cm (all three).",
                    "Apply Heron: Area = √(18 × 6 × 6 × 6) = √(3 × 6 × 6³) = 36√3 cm².",
                    "Note this matches general equilateral rule (√3/4)a² = (√3/4)(144) = 36√3 cm²."
                ]
            },
            {
                "question": "Find the circumcircle radius R of a triangle with sides a = 13, b = 14, c = 15 and Area = 84 sq. units using Area = abc / (4R).",
                "options": ["R = 8.125 units (or 65/8)", "R = 4 units", "R = 16.25 units", "R = 7.5 units"],
                "answer": 0,
                "hint": "Rearrange R = (13 × 14 × 15) / (4 × 84)!",
                "explanation": "R = (13 × 14 × 15) / (4 × 84) = (13 × 15) / (4 × 6) = 195 / 24 = 65/8 = 8.125 units.",
                "solution_steps": [
                    "Use circle connection formula Area = abc / (4R) ⇒ R = abc / (4 · Area).",
                    "Substitute a=13, b=14, c=15, Area=84: R = (13 × 14 × 15)/(4 × 84).",
                    "Cancel 14 into 84 (= 6) and 3 into 15/6: R = (13 × 5)/(4 × 2) = 65/8 = 8.125."
                ]
            },
            {
                "question": "Using Brahmagupta's formula √[(s − a)(s − b)(s − c)(s − d)], calculate the area of a cyclic quadrilateral with consecutive sides 4 cm, 5 cm, 6 cm, and 7 cm.",
                "options": ["2√210 cm² (since s = 11 ⇒ √(7×6×5×4))", "√105 cm²", "42 cm²", "11 cm²"],
                "answer": 0,
                "hint": "Compute s = (4 + 5 + 6 + 7)/2 = 11, then take √[(11−4)(11−5)(11−6)(11−7)]!",
                "explanation": "s = 11 ⇒ √(7 × 6 × 5 × 4) = √840 = 2√210 cm².",
                "solution_steps": [
                    "Compute semi-perimeter s = (4 + 5 + 6 + 7)/2 = 11 cm.",
                    "Differences: 11−4 = 7, 11−5 = 6, 11−6 = 5, 11−7 = 4.",
                    "Product = 7 × 6 × 5 × 4 = 840 = 4 × 210 ⇒ √840 = 2√210 cm²."
                ]
            },
            {
                "question": "Evaluate the exact area of a cyclic quadrilateral with consecutive sides a = 1 cm, b = 3 cm, c = 4 cm, and d = 6 cm using Brahmagupta's formula √[(s − a)(s − b)(s − c)(s − d)].",
                "options": ["6√2 cm² (since s = 7 ⇒ √(6×4×3×1) = √72)", "4√3 cm²", "6 cm²", "8√2 cm²"],
                "answer": 0,
                "hint": "Compute s = (1 + 3 + 4 + 6)/2 = 7, then evaluate √(6 × 4 × 3 × 1)!",
                "explanation": "s = 7 ⇒ (7−1)(7−3)(7−4)(7−6) = 6 × 4 × 3 × 1 = 72 ⇒ √72 = 6√2 cm².",
                "solution_steps": [
                    "Compute semi-perimeter s = (1 + 3 + 4 + 6)/2 = 7 cm.",
                    "Multiply differences: (7−1)(7−3)(7−4)(7−6) = 6 × 4 × 3 × 1 = 72.",
                    "Simplify √72 = √(36 × 2) = 6√2 cm²."
                ]
            },
            {
                "question": "If a rectangle measures 9 cm by 4 cm, what exact side length must Baudhāyana's equal-area constructed square have?",
                "options": ["6 cm (√(9 × 4) = √36)", "6.5 cm", "13 cm", "18 cm"],
                "answer": 0,
                "hint": "Target square area must equal rectangle area 9 × 4 = 36 cm²!",
                "explanation": "Baudhāyana's construction produces a square of side √(ab) = √(9 × 4) = 6 cm.",
                "solution_steps": [
                    "Rectangle area = 9 × 4 = 36 cm².",
                    "Baudhāyana forms right triangle with hypotenuse (9+4)/2 = 6.5 and leg (9−4)/2 = 2.5.",
                    "Remaining leg (square side) = √(6.5² − 2.5²) = √(42.25 − 6.25) = √36 = 6 cm."
                ]
            },
            {
                "question": "Why does Brahmagupta's formula √[(s − a)(s − b)(s − c)(s − d)] give the EXACT maximum possible area among all quadrilaterals with fixed sides a, b, c, d?",
                "options": [
                    "Because it strictly requires opposite angles to sum to 180° (cyclic quadrilateral, where cos²((A+C)/2) = 0)",
                    "Because non-cyclic squares have smaller angles",
                    "Because diagonal lengths equal zero",
                    "Because semi-perimeter stays smaller"
                ],
                "answer": 0,
                "hint": "General Bretschneider formula subtracts abcd·cos²((A+C)/2); only cyclic quads make cos(90°) = 0!",
                "explanation": "Brahmagupta's formula applies exclusively to cyclic quadrilaterals (opposite angles 180°), achieving maximum area for given sides.",
                "solution_steps": [
                    "Non-cyclic quadrilaterals can deform, decreasing enclosed area until cos²((A+C)/2) reduces the square root.",
                    "Cyclic quadrilaterals satisfy ∠A + ∠C = 180° ⇒ (A+C)/2 = 90° ⇒ cos(90°) = 0.",
                    "Hence cyclic shapes enclose maximum area √[(s−a)(s−b)(s−c)(s−d)]."
                ]
            },
            {
                "question": "A triangle has area 42 cm² and semi-perimeter s = 14 cm. What is the exact radius r of its inscribed circle?",
                "options": ["3 cm", "6 cm", "21 cm", "1.5 cm"],
                "answer": 0,
                "hint": "Apply Area = r × s!",
                "explanation": "r = Area / s = 42 / 14 = 3 cm.",
                "solution_steps": [
                    "Use triangle incircle relation Area = r(a + b + c)/2 = r × s.",
                    "Substitute Area = 42 cm² and s = 14 cm: 42 = r × 14.",
                    "Divide: r = 42 / 14 = 3 cm."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Circle Sector Quiz",
        "subtitle": "Sections 6.10–6.10.1 Practice Set (10 Questions): Circle Area Proofs (Archimedes & Nilakantha), Sectors & Circular Segments",
        "questions": [
            {
                "question": "Find the area of a circular disc whose circumference equals 44 cm (use π ≈ 22/7).",
                "options": ["154 cm²", "44 cm²", "308 cm²", "77 cm²"],
                "answer": 0,
                "hint": "First solve 2(22/7)r = 44 to get r = 7 cm, then compute πr²!",
                "explanation": "r = 7 cm ⇒ Area = (22/7) × 7² = 22 × 7 = 154 cm².",
                "solution_steps": [
                    "Find radius from circumference: 2 × (22/7) × r = 44 ⇒ r = 7 cm.",
                    "Apply circle area formula: Area = πr² = (22/7) × 7 × 7.",
                    "Multiply: 22 × 7 = 154 cm²."
                ]
            },
            {
                "question": "In Nilakantha Somayājī's visual rearrangement of circular wedges into a parallelogram-like shape, why does the base measure πr rather than 2πr?",
                "options": [
                    "Half of the wedges point upward (πr top edge) and half point downward (πr bottom edge), splitting total circumference 2πr in half",
                    "Half the slices are thrown away",
                    "Only semicircles have base πr",
                    "Because radius equals π"
                ],
                "answer": 0,
                "hint": "Alternate the crust edges half along the top and half along the bottom!",
                "explanation": "Alternating sectors evenly puts πr along the bottom base and πr along the top edge with height r, yielding πr × r = πr².",
                "solution_steps": [
                    "Divide the full circle (circumference 2πr) into many identical narrow sectors.",
                    "Arrange alternating wedges pointing up and down side by side.",
                    "Half the total boundary (πr) forms the base while radius r forms height ⇒ Area = πr²."
                ]
            },
            {
                "question": "Find the area of a sector of a circle with radius 14 cm and central angle 45° (use π ≈ 22/7).",
                "options": ["77 cm²", "154 cm²", "308 cm²", "38.5 cm²"],
                "answer": 0,
                "hint": "Note 45° / 360° = 1/8 of the circle!",
                "explanation": "Area = (22/7) × 14 × 14 × (45/360) = 616 × (1/8) = 77 cm².",
                "solution_steps": [
                    "Compute sector fraction: θ/360° = 45°/360° = 1/8.",
                    "Full circle area = (22/7) × 14² = 22 × 28 = 616 cm².",
                    "Sector area = 616 / 8 = 77 cm²."
                ]
            },
            {
                "question": "Which formula correctly connects a sector's area A_sector directly to its curved arc length L and radius r?",
                "options": ["A_sector = ½ × L × r", "A_sector = L × r", "A_sector = 2L × r", "A_sector = L / r"],
                "answer": 0,
                "hint": "Check A_sector / (πr²) = L / (2πr)!",
                "explanation": "Since L = 2πr(θ/360), ½ L r = πr²(θ/360) = Area of sector!",
                "solution_steps": [
                    "Write both formulas: L = 2πr(θ/360) and A_sector = πr²(θ/360).",
                    "Factor πr²(θ/360) as ½ · [2πr(θ/360)] · r.",
                    "Substitute L inside: A_sector = ½ L r (behaving like a curved-base triangle!)."
                ]
            },
            {
                "question": "In a circle of radius r = 10 cm, a chord AB subtends a right angle (90°) at Centre O. Calculate the area of the minor CIRCULAR SEGMENT cut off by chord AB (use π ≈ 3.14).",
                "options": ["28.5 cm² (Sector 78.5 − Triangle 50)", "78.5 cm²", "50 cm²", "128.5 cm²"],
                "answer": 0,
                "hint": "Subtract right-triangle area ½(10)(10) = 50 cm² from quadrant sector area ¼(3.14 × 100)!",
                "explanation": "Quadrant sector = ¼(3.14 × 100) = 78.5 cm²; right ΔOAB = ½(10)(10) = 50 cm² ⇒ Segment = 78.5 − 50 = 28.5 cm².",
                "solution_steps": [
                    "Sector area (90° quadrant) = ¼ × πr² = ¼ × 3.14 × 100 = 78.5 cm².",
                    "Triangle OAB is right-angled at O with legs 10 cm ⇒ Area(ΔOAB) = ½(10)(10) = 50 cm².",
                    "Minor segment area = Sector − Triangle = 78.5 − 50 = 28.5 cm²."
                ]
            },
            {
                "question": "If a circle's radius triples from r to 3r, how does its area change?",
                "options": ["It becomes 9 times larger (9πr²)", "It triples (3πr²)", "It becomes 6 times larger", "It increases by 9π"],
                "answer": 0,
                "hint": "Square the scale factor 3 inside π(3r)²!",
                "explanation": "π(3r)² = 9πr², scaling area by 3² = 9.",
                "solution_steps": [
                    "Original area = πr².",
                    "Replace r with 3r: New area = π(3r)² = 9πr².",
                    "Area scales quadratically by 3² = 9 times."
                ]
            },
            {
                "question": "The area of a sector is 55 cm² and its radius is 10 cm. Find its arc length L directly using A_sector = ½Lr.",
                "options": ["11 cm", "5.5 cm", "22 cm", "110 cm"],
                "answer": 0,
                "hint": "Solve 55 = ½ × L × 10!",
                "explanation": "55 = 5L ⇒ L = 11 cm.",
                "solution_steps": [
                    "Apply sector-arc relation: Area = ½ × L × r.",
                    "Plug in Area = 55 and r = 10: 55 = ½(10)L = 5L.",
                    "Divide both sides by 5: L = 11 cm."
                ]
            },
            {
                "question": "Two concentric circles have outer radius R = 15 cm and inner radius r = 13 cm. Find the exact area of the circular ring between them (in terms of π) using algebraic factoring.",
                "options": ["56π cm² (π(15 + 13)(15 − 13))", "28π cm²", "4π cm²", "394π cm²"],
                "answer": 0,
                "hint": "Factor π(R² − r²) = π(R + r)(R − r)!",
                "explanation": "π(15 + 13)(15 − 13) = π(28)(2) = 56π cm².",
                "solution_steps": [
                    "Ring area = Outer area − Inner area = πR² − πr² = π(R² − r²).",
                    "Factor difference of squares: π(R + r)(R − r) = π(15 + 13)(15 − 13).",
                    "Evaluate: π(28)(2) = 56π cm²."
                ]
            },
            {
                "question": "A clock minute hand is 14 cm long. What area does the minute hand sweep in 10 minutes (use π ≈ 22/7)?",
                "options": ["102.67 cm² (308/3 cm², sweeping 60° sector)", "154 cm²", "616 cm²", "51.33 cm²"],
                "answer": 0,
                "hint": "60 minutes = 360°, so 10 minutes sweeps 60° (1/6 of the full circle)!",
                "explanation": "Angle = (10/60) × 360° = 60° ⇒ Area = (22/7) × 14² × (1/6) = 616 / 6 = 308/3 ≈ 102.67 cm².",
                "solution_steps": [
                    "In 60 minutes, minute hand sweeps 360°, so 10 minutes sweeps 60° (1/6 circle).",
                    "Full circle area = (22/7) × 14 × 14 = 616 cm².",
                    "Swept sector area = 616 / 6 = 308/3 ≈ 102.67 cm²."
                ]
            },
            {
                "question": "Compare a major circular segment against its corresponding minor circular segment on chord AB. Which relation holds true?",
                "options": [
                    "Area(Major Segment) = Full Circle Area πr² − Area(Minor Segment)",
                    "Area(Major Segment) = Area(Major Sector) − Area(ΔOAB)",
                    "Major segment and minor segment always have equal area",
                    "Major segment area excludes the central triangle OAB"
                ],
                "answer": 0,
                "hint": "Chord AB splits the full circular disc into exactly two pieces: minor segment + major segment!",
                "explanation": "A chord divides a circle into two complementary segments summing to πr², or equivalently Area(Major Sector) + Area(ΔOAB).",
                "solution_steps": [
                    "Chord AB cuts the circle into minor segment (smaller cap) and major segment (containing Centre O).",
                    "Both non-overlapping regions cover the entire disc: Minor + Major = πr².",
                    "Equivalently, Major Segment = Major Sector + Area(ΔOAB)."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Chapter Mastery Quiz",
        "subtitle": "End-of-Chapter Mixed Exercises (10 Questions): Wheel Rotations, Identity Areas, Inscribed Polygons & Multi-Shape Composite Proofs",
        "questions": [
            {
                "question": "A car wheel has diameter 70 cm (radius 35 cm). How many full revolutions must each wheel turn for the car to travel 660 m (66,000 cm)? (Use π ≈ 22/7).",
                "options": ["300 revolutions", "600 revolutions", "150 revolutions", "30 revolutions"],
                "answer": 0,
                "hint": "1 turn covers circumference πD = (22/7) × 70 = 220 cm; divide 66,000 by 220!",
                "explanation": "Circumference = 220 cm; Revolutions = 66,000 / 220 = 300.",
                "solution_steps": [
                    "Convert distance to cm: 660 m = 66,000 cm.",
                    "Compute wheel circumference: C = πD = (22/7) × 70 = 220 cm.",
                    "Number of turns = Total distance / C = 66,000 / 220 = 300 revolutions."
                ]
            },
            {
                "question": "A square park of side 50 m is surrounded externally by a uniform 5 m wide walking path. Using a² − b², calculate the exact area of the paved path.",
                "options": ["1100 m²", "2500 m²", "3600 m²", "500 m²"],
                "answer": 0,
                "hint": "Outer side expands on BOTH sides: 50 + 2(5) = 60 m! Compute 60² − 50² = (60 + 50)(60 − 50)!",
                "explanation": "Outer side = 60 m, inner side = 50 m ⇒ Path Area = 60² − 50² = (110)(10) = 1100 m².",
                "solution_steps": [
                    "Add 5 m path width on both left/right and top/bottom: outer side = 50 + 5 + 5 = 60 m.",
                    "Path area = Outer square − Inner square = 60² − 50².",
                    "Apply difference of squares: (60 + 50)(60 − 50) = 110 × 10 = 1100 m²."
                ]
            },
            {
                "question": "A regular hexagon is inscribed inside a circle of radius r = 6 cm. What is the exact area of the inscribed regular hexagon?",
                "options": ["54√3 cm²", "36√3 cm²", "108√3 cm²", "216 cm²"],
                "answer": 0,
                "hint": "Connecting all 6 hexagon vertices to Centre O splits it into 6 congruent equilateral triangles of side 6 cm!",
                "explanation": "6 equilateral triangles of side 6 each have area (√3/4)(36) = 9√3, so 6 × 9√3 = 54√3 cm².",
                "solution_steps": [
                    "Central angle per hexagon edge = 360° / 6 = 60°, with two radii r = 6 forming 6 equilateral triangles.",
                    "Area of one equilateral triangle of side 6 = (√3/4)(6²) = 9√3 cm².",
                    "Total hexagon area = 6 × 9√3 = 54√3 cm²."
                ]
            },
            {
                "question": "Two opposite corners of a square of side 14 cm act as centres for two quarter-circle quadrants of radius 14 cm drawn inside the square. Find the area of the overlapping leaf region between the two arcs (use π ≈ 22/7).",
                "options": ["112 cm² (2 × 154 − 196)", "196 cm²", "308 cm²", "84 cm²"],
                "answer": 0,
                "hint": "Add the two quadrants together (forming a semicircle of area ½π(14²)) and subtract the square once (inclusion-exclusion)!",
                "explanation": "Two quadrants = 2 × ¼(22/7)(196) = 308 cm²; Square = 196 cm² ⇒ Overlap leaf = 308 − 196 = 112 cm².",
                "solution_steps": [
                    "Each quadrant covers ¼πr² = ¼(22/7)(14²) = 154 cm²; two quadrants total 308 cm².",
                    "Together the two quadrants cover the entire square (196 cm²) while double-counting the middle leaf.",
                    "Leaf area = 308 − 196 = 112 cm²."
                ]
            },
            {
                "question": "A rhombus-shaped field has green grass for 18 cows to graze. Each side of the rhombus measures 30 m and its longer diagonal is 48 m. Using Heron's formula on one triangle half, how much total area does the rhombus cover?",
                "options": ["864 m²", "432 m²", "720 m²", "1440 m²"],
                "answer": 0,
                "hint": "Diagonal splits the rhombus into TWO congruent triangles of sides 30, 30, 48! Compute one triangle (432 m²) and double it!",
                "explanation": "s = (30 + 30 + 48)/2 = 54; Δ Area = √(54 × 24 × 24 × 6) = 24 × √324 = 24 × 18 = 432 m² ⇒ Rhombus = 864 m².",
                "solution_steps": [
                    "Diagonal 48 m divides the rhombus into two congruent triangles of sides 30, 30, 48.",
                    "For one triangle: s = 54 ⇒ Area = √(54 × 24 × 24 × 6) = 24 × √(324) = 24 × 18 = 432 m².",
                    "Total rhombus area = 2 × 432 = 864 m²."
                ]
            },
            {
                "question": "If the perimeter of a square equals the circumference of a circle, which shape encloses the GREATER interior area?",
                "options": ["The circle encloses strictly greater area (by factor 4/π ≈ 1.273)", "The square encloses greater area", "Both always enclose equal area", "Depends on the perimeter length"],
                "answer": 0,
                "hint": "Test C = 4a = 2πr ⇒ r = 2a/π; compare πr² = 4a²/π against square area a²!",
                "explanation": "For fixed perimeter P, Circle Area = P²/(4π) > P²/16 = Square Area because 4π ≈ 12.566 < 16!",
                "solution_steps": [
                    "Set common perimeter P: Square side a = P/4 ⇒ Square Area = P²/16.",
                    "Circle radius r = P/(2π) ⇒ Circle Area = π[P/(2π)]² = P²/(4π) ≈ P²/12.57.",
                    "Since denominator 4π < 16, Circle Area > Square Area ALWAYS!"
                ]
            },
            {
                "question": "Find the area of a shaded triangle inside a square of side 10 cm, where one vertex lies anywhere on the top edge and the base spans the full bottom edge.",
                "options": ["50 cm² (always exactly half the square)", "100 cm²", "25 cm²", "Depends on exact top vertex location"],
                "answer": 0,
                "hint": "Base = 10 cm and perpendicular height between parallel top/bottom edges = 10 cm!",
                "explanation": "Regardless of where the vertex slides along the top edge, Area = ½ × 10 × 10 = 50 cm².",
                "solution_steps": [
                    "Triangle base spans bottom edge: b = 10 cm.",
                    "Since top edge runs parallel at distance 10 cm, perpendicular height h = 10 cm.",
                    "Area = ½ × 10 × 10 = 50 cm² (half of square)."
                ]
            },
            {
                "question": "An athletic field consists of a 100 m × 70 m central rectangle joined to two semicircles along its two shorter 70 m ends (diameter 70 m, use π ≈ 22/7). Find the field's total area AND outer perimeter.",
                "options": ["Area = 10,850 m² and Perimeter = 420 m", "Area = 7,000 m² and Perimeter = 340 m", "Area = 10,850 m² and Perimeter = 340 m", "Area = 3,850 m² and Perimeter = 220 m"],
                "answer": 0,
                "hint": "Two semicircles of diameter 70 m combine into ONE full circle of radius 35 m (area 3850 m², circumference 220 m)!",
                "explanation": "Area = (100 × 70) + (22/7)(35²) = 7000 + 3850 = 10,850 m². Outer border = 2(100) + 2(22/7)(35) = 200 + 220 = 420 m.",
                "solution_steps": [
                    "Rectangle area = 100 × 70 = 7000 m²; two semicircles = 1 circle (r = 35 m) of area (22/7)(35²) = 3850 m².",
                    "Total Area = 7000 + 3850 = 10,850 m².",
                    "Outer perimeter skips internal 70 m seams: 2(100) + 2π(35) = 200 + 220 = 420 m."
                ]
            },
            {
                "question": "If the three sides of a triangle are each doubled (2a, 2b, 2c), by what factor does Heron's triangle area multiply?",
                "options": ["4 times (since s becomes 2s, multiplying 4 factors under √ gives √16 = 4)", "2 times", "8 times", "16 times"],
                "answer": 0,
                "hint": "Pull 2 out of each of the 4 factors inside √[(2s)(2s−2a)(2s−2b)(2s−2c)]!",
                "explanation": "√[16 · s(s−a)(s−b)(s−c)] = 4 × Original Area.",
                "solution_steps": [
                    "Doubling a, b, c makes new semi-perimeter s' = (2a + 2b + 2c)/2 = 2s.",
                    "Substitute into Heron: √[(2s)(2s − 2a)(2s − 2b)(2s − 2c)] = √[16 · s(s−a)(s−b)(s−c)].",
                    "Factor √16 = 4 outside the radical → 4 times original area!"
                ]
            },
            {
                "question": "A circular mirror of radius 10.5 cm sits inside a circular frame of outer radius 14 cm (use π ≈ 22/7). Find the area of the surrounding circular frame.",
                "options": ["269.5 cm² (π(14 + 10.5)(14 − 10.5))", "616 cm²", "346.5 cm²", "134.75 cm²"],
                "answer": 0,
                "hint": "Use π(R² − r²) = (22/7)(24.5)(3.5)!",
                "explanation": "Frame area = (22/7)(14 + 10.5)(14 − 10.5) = (22/7)(24.5)(3.5) = 22 × 24.5 × 0.5 = 11 × 24.5 = 269.5 cm².",
                "solution_steps": [
                    "Frame area = πR² − πr² = π(R + r)(R − r).",
                    "Compute R + r = 14 + 10.5 = 24.5 cm; R − r = 14 − 10.5 = 3.5 cm.",
                    "Multiply: (22/7) × 24.5 × 3.5 = 22 × 24.5 × 0.5 = 269.5 cm²."
                ]
            }
        ]
    }
]

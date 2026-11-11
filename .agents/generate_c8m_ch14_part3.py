#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 14: Area
Slides Data Generator - Part 3 (Slides 17 to 20: 40 Mastery Quiz Questions)
Zero lecture audio on exercises/quizzes (Slides 17-20).
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Squares Triangles Quiz",
        "subtitle": "Mastery Quiz Part 1 (10 Questions): Equal Area Divisions, Rectangles, Perimeter vs Area & General Triangles",
        "type": "quiz",
        "questions": [
            {
                "question": "A square of side 12 cm is divided into four non-congruent parts having equal area. What is the exact area of each part?",
                "options": [
                    "36 cm²",
                    "12 cm²",
                    "48 cm²",
                    "24 cm²"
                ],
                "answer": 0,
                "hint": "Compute total square area (12 × 12) and divide evenly by 4!",
                "explanation": "Total area = 12² = 144 cm². Dividing equally among 4 parts gives 144 ÷ 4 = 36 cm² each.",
                "solution_steps": [
                    "Step 1: Compute square area: 12 cm × 12 cm = 144 cm².",
                    "Step 2: Divide total area into 4 equal parts: 144 ÷ 4 = 36 cm².",
                    "Step 3: Note that all 4 parts share 36 cm² regardless of shape."
                ]
            },
            {
                "question": "If one edge of a rectangular sheet (area 48 cm²) expands by factor 3 while preserving total area, how must its perpendicular side transform?",
                "options": [
                    "Compress to one-third (× 1/3)",
                    "Expand by factor 3",
                    "Subtract 3 cm",
                    "Halve (× 1/2)"
                ],
                "answer": 0,
                "hint": "To keep L × W constant when L becomes 3L, solve (3L) × W_new = L × W!",
                "explanation": "(3L) × (W / 3) = L × W = 48 cm², keeping total enclosed area strictly invariant.",
                "solution_steps": [
                    "Step 1: Original area A = L × W.",
                    "Step 2: With L_new = 3L, set (3L) × W_new = L × W.",
                    "Step 3: Divide both sides by 3L → W_new = W / 3."
                ]
            },
            {
                "question": "A rectangle of length 15 cm and width 8 cm is sliced neatly along one diagonal AC into ΔABC and ΔCDA. Find the area of ΔABC:",
                "options": [
                    "60 cm²",
                    "120 cm²",
                    "23 cm²",
                    "46 cm²"
                ],
                "answer": 0,
                "hint": "Rectangle area = 15 × 8; diagonal AC cuts it into two congruent triangles of half area each!",
                "explanation": "Rectangle area = 15 × 8 = 120 cm²; by SSS congruence, ΔABC covers half = 60 cm².",
                "solution_steps": [
                    "Step 1: Rectangle area = 15 cm × 8 cm = 120 cm².",
                    "Step 2: Diagonal AC forms ΔABC ≅ ΔCDA (SSS).",
                    "Step 3: Area(ΔABC) = 120 ÷ 2 = 60 cm²."
                ]
            },
            {
                "question": "Two rectangular plots both use exactly 40 m of boundary fencing (Perimeter = 40 m). Plot A is 10 m × 10 m, and Plot B is 18 m × 2 m. How much more area does Plot A enclose than Plot B?",
                "options": [
                    "64 m²   (100 m² − 36 m²)",
                    "0 m²   (equal perimeter forces equal area)",
                    "40 m²",
                    "80 m²"
                ],
                "answer": 0,
                "hint": "Calculate Area(A) = 10 × 10 and Area(B) = 18 × 2, then subtract!",
                "explanation": "Plot A = 100 m², Plot B = 36 m², showing equal perimeter gives drastically different areas (100 − 36 = 64 m²).",
                "solution_steps": [
                    "Step 1: Verify perimeters: 2(10+10) = 40 m and 2(18+2) = 40 m.",
                    "Step 2: Compute areas: A = 10 × 10 = 100 m²; B = 18 × 2 = 36 m².",
                    "Step 3: Difference = 100 − 36 = 64 m²."
                ]
            },
            {
                "question": "A 6 × 6 unit square (Perimeter 24, Area 36) has a 2 × 1 notch removed inward from the middle of its top side. What are the new Area and new Perimeter?",
                "options": [
                    "Area drops to 34 sq units; Perimeter rises to 26 units",
                    "Area = 34; Perimeter = 22",
                    "Area = 36; Perimeter = 26",
                    "Area = 32; Perimeter = 24"
                ],
                "answer": 0,
                "hint": "2 unit squares were removed (Area − 2), while two vertical depth-1 walls were added inside (+2 to Perimeter)!",
                "explanation": "Removing 2×1 units reduces area from 36 to 34, while inward indentation exposes 2 extra unit walls (24 + 2 = 26).",
                "solution_steps": [
                    "Step 1: Original square has Area = 36, Perimeter = 24.",
                    "Step 2: Removing a 2 × 1 rectangle subtracts 2 sq units → Area = 34.",
                    "Step 3: Bottom of notch replaces top 2-unit gap; two vertical depth-1 edges add +2 → Perimeter = 26."
                ]
            },
            {
                "question": "Rectangle PQRS has PQ = 22 cm and QR = 9 cm. Point T lies on opposite side SR (anywhere between S and R). What is Area(ΔPQT)?",
                "options": [
                    "99 cm²",
                    "198 cm²",
                    "49.5 cm²",
                    "Cannot determine without knowing distance ST"
                ],
                "answer": 0,
                "hint": "Every point T on SR sits perpendicular distance 9 cm from base PQ = 22 cm!",
                "explanation": "Base = 22 cm, height = 9 cm → Area(ΔPQT) = 1/2 × 22 × 9 = 99 cm².",
                "solution_steps": [
                    "Step 1: Identify base PQ = 22 cm.",
                    "Step 2: Distance from T on SR to base PQ is fixed at 9 cm.",
                    "Step 3: Area = 1/2 × 22 × 9 = 99 cm²."
                ]
            },
            {
                "question": "An obtuse triangle ΔABC has base AB = 14 cm. Extending AB past B to D places perpendicular altitude CD = 9 cm outside the base (with BD = 5 cm). Find Area(ΔABC):",
                "options": [
                    "63 cm²",
                    "85.5 cm²   (using base AD = 19 cm)",
                    "22.5 cm²",
                    "126 cm²"
                ],
                "answer": 0,
                "hint": "Use only the triangle's true base AB = 14 cm (or subtract right ΔBDC from ΔADC)!",
                "explanation": "Area(ΔADC) − Area(ΔBDC) = 1/2(19)(9) − 1/2(5)(9) = 85.5 − 22.5 = 63 cm², matching 1/2 × 14 × 9.",
                "solution_steps": [
                    "Step 1: True base is AB = 14 cm and perpendicular altitude to AB's line is CD = 9 cm.",
                    "Step 2: Compute 1/2 × 14 × 9 = 63 cm².",
                    "Step 3: Check via subtraction: 1/2(19)(9) − 1/2(5)(9) = 85.5 − 22.5 = 63 cm²."
                ]
            },
            {
                "question": "A right-angled triangle has area 45 cm² and one perpendicular leg measuring 9 cm. Find the length of its other perpendicular leg:",
                "options": [
                    "10 cm",
                    "5 cm",
                    "18 cm",
                    "20 cm"
                ],
                "answer": 0,
                "hint": "Solve 1/2 × 9 × h = 45!",
                "explanation": "9h / 2 = 45 gives 9h = 90, so the second perpendicular leg measures 10 cm.",
                "solution_steps": [
                    "Step 1: Use Area = 1/2 × leg₁ × leg₂.",
                    "Step 2: Substitute: 45 = 1/2 × 9 × leg₂.",
                    "Step 3: Multiply by 2 and divide by 9: leg₂ = 90 / 9 = 10 cm."
                ]
            },
            {
                "question": "Doubling BOTH the base AND the height of a triangle multiplies its original area by what exact factor?",
                "options": [
                    "4 times   (2 × 2 = 4)",
                    "2 times",
                    "8 times",
                    "16 times"
                ],
                "answer": 0,
                "hint": "Compute 1/2 × (2b) × (2h) relative to 1/2 × b × h!",
                "explanation": "New Area = 1/2 × (2b) × (2h) = 4 × (1/2 bh), quadrupling the original area.",
                "solution_steps": [
                    "Step 1: Original Area A = 1/2 × b × h.",
                    "Step 2: New Area A' = 1/2 × (2b) × (2h) = 4 × (1/2 × b × h).",
                    "Step 3: Thus A' = 4A."
                ]
            },
            {
                "question": "In a unit-square grid, tiling a 3.5 cm by 4 cm rectangle produces what exact area?",
                "options": [
                    "14 cm²",
                    "15 cm²",
                    "7.5 cm²",
                    "28 cm²"
                ],
                "answer": 0,
                "hint": "Multiply length 3.5 cm by width 4 cm!",
                "explanation": "3 rows of 4 plus a half-row of 4 (2 sq units) equals 12 + 2 = 14 cm².",
                "solution_steps": [
                    "Step 1: Length l = 3.5 cm, width w = 4 cm.",
                    "Step 2: Area = l × w = 3.5 × 4.",
                    "Step 3: 3.5 × 4 = 14 cm²."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Medians Parallels Quiz",
        "subtitle": "Mastery Quiz Part 2 (10 Questions): Altitudes, Medians, Parallel Lines, Reflection Min-Perimeter & Triangulation",
        "type": "quiz",
        "questions": [
            {
                "question": "In ΔPQR, base QR = 20 cm has altitude PM = 12 cm. If another side PQ measures 15 cm, find its corresponding altitude RN dropped from R onto PQ:",
                "options": [
                    "16 cm",
                    "12 cm",
                    "10 cm",
                    "24 cm"
                ],
                "answer": 0,
                "hint": "Equate b₁h₁ = b₂h₂ → 20 × 12 = 15 × RN!",
                "explanation": "Area = 1/2(20)(12) = 120 cm². Solving 1/2(15)(RN) = 120 gives RN = 240 ÷ 15 = 16 cm.",
                "solution_steps": [
                    "Step 1: Compute Area using QR and PM: 1/2 × 20 × 12 = 120 cm².",
                    "Step 2: Set Area using PQ and RN: 1/2 × 15 × RN = 120.",
                    "Step 3: Solve RN = 240 / 15 = 16 cm."
                ]
            },
            {
                "question": "In a right-angled triangle with legs 5 cm and 12 cm and hypotenuse 13 cm, what is the altitude h dropped perpendicularly onto the hypotenuse?",
                "options": [
                    "60/13 cm   (≈ 4.62 cm)",
                    "13/2 cm",
                    "30/13 cm",
                    "10 cm"
                ],
                "answer": 0,
                "hint": "Equate 5 × 12 = 13 × h!",
                "explanation": "Area = 1/2(5)(12) = 30 cm². Setting 1/2(13)(h) = 30 yields h = 60 / 13 cm.",
                "solution_steps": [
                    "Step 1: Area via perpendicular legs = 1/2 × 5 × 12 = 30 cm².",
                    "Step 2: Area via hypotenuse = 1/2 × 13 × h.",
                    "Step 3: Solve 13h = 60 → h = 60/13 cm."
                ]
            },
            {
                "question": "In ΔABC (total area 96 cm²), D is the midpoint of BC, and E is the midpoint of AD. What is the exact area of ΔABD and of ΔABE?",
                "options": [
                    "Area(ΔABD) = 48 cm²; Area(ΔABE) = 24 cm²",
                    "Area(ΔABD) = 48 cm²; Area(ΔABE) = 32 cm²",
                    "Area(ΔABD) = 64 cm²; Area(ΔABE) = 32 cm²",
                    "Area(ΔABD) = 32 cm²; Area(ΔABE) = 16 cm²"
                ],
                "answer": 0,
                "hint": "Median AD cuts ΔABC in half (48 cm²), then median BE of ΔABD cuts ΔABD in half again!",
                "explanation": "AD is median of ΔABC → Area(ΔABD) = 96/2 = 48 cm². BE is median of ΔABD → Area(ΔABE) = 48/2 = 24 cm².",
                "solution_steps": [
                    "Step 1: D is midpoint of BC, so median AD bisects Area(ΔABC) → Area(ΔABD) = 96 ÷ 2 = 48 cm².",
                    "Step 2: E is midpoint of AD, so BE is a median of ΔABD.",
                    "Step 3: Area(ΔABE) = 48 ÷ 2 = 24 cm²."
                ]
            },
            {
                "question": "Segment BC of ΔABC is divided at P such that BP = 3 cm and PC = 9 cm. If Area(ΔABC) = 72 cm², find Area(ΔABP):",
                "options": [
                    "18 cm²",
                    "24 cm²",
                    "36 cm²",
                    "54 cm²"
                ],
                "answer": 0,
                "hint": "Triangles ΔABP and ΔABC share identical height from A, so area ratio equals base ratio 3 : 12!",
                "explanation": "BC = 3 + 9 = 12 cm. Since BP = 3/12 = 1/4 of BC, Area(ΔABP) = 1/4 × 72 = 18 cm².",
                "solution_steps": [
                    "Step 1: Total base BC = 3 + 9 = 12 cm.",
                    "Step 2: ΔABP and ΔABC share identical perpendicular altitude from A.",
                    "Step 3: Area(ΔABP) = (3 / 12) × 72 = 1/4 × 72 = 18 cm²."
                ]
            },
            {
                "question": "Parallel lines p and q are separated by vertical distance 11 cm. Two triangles ΔABX and ΔABY share common base AB = 12 cm on line p, with X and Y positioned anywhere along line q. Compare their areas:",
                "options": [
                    "Both triangles have exact equal area = 66 cm²",
                    "ΔABX has larger area if AX > AY",
                    "Only right-angled triangles on AB equal 66 cm²",
                    "Sum of both areas equals 66 cm²"
                ],
                "answer": 0,
                "hint": "Common base 12 cm and constant parallel height 11 cm fix area = 1/2 × 12 × 11!",
                "explanation": "Between parallel lines, altitude remains constant at 11 cm everywhere along q, locking Area = 1/2(12)(11) = 66 cm².",
                "solution_steps": [
                    "Step 1: Common base AB = 12 cm on line p.",
                    "Step 2: Constant distance between parallel tracks gives height h = 11 cm for both.",
                    "Step 3: Area(ΔABX) = Area(ΔABY) = 1/2 × 12 × 11 = 66 cm²."
                ]
            },
            {
                "question": "Why does reflecting point B across parallel line m to image B' prove which position P* on m minimizes the perimeter of ΔABP (with fixed base AB on line l)?",
                "options": [
                    "Because PB = PB', so AP + PB = AP + PB', which reaches absolute minimum when A → P* → B' forms one straight line (making ΔAP*B isosceles)",
                    "Because reflecting shrinks base AB",
                    "Because P* must lie vertically above point A",
                    "Because parallel lines make all triangles equilateral"
                ],
                "answer": 0,
                "hint": "The shortest distance between two fixed points A and B' is always a straight line segment!",
                "explanation": "By mirror symmetry, PB = PB'. Straight path AB' crosses m at P* directly above AB's midpoint, minimizing AP + PB.",
                "solution_steps": [
                    "Step 1: Reflect B perpendicularly across line m to image B' (so PB = PB').",
                    "Step 2: Total path AP + PB equals path AP + PB'.",
                    "Step 3: Straight segment AB' yields shortest path at P* on the perpendicular bisector of AB (AP* = P*B)."
                ]
            },
            {
                "question": "Which convex polygon ALWAYS splits into 5 non-overlapping triangles when all diagonals are drawn from a single vertex?",
                "options": [
                    "Heptagon (7-sided polygon)",
                    "Pentagon (5-sided polygon)",
                    "Hexagon (6-sided polygon)",
                    "Octagon (8-sided polygon)"
                ],
                "answer": 0,
                "hint": "Solve n − 2 = 5 for number of sides n!",
                "explanation": "Since triangulation from one vertex yields (n − 2) triangles, n − 2 = 5 gives n = 7 sides (heptagon).",
                "solution_steps": [
                    "Step 1: Recall triangulation count from one vertex = n − 2.",
                    "Step 2: Set n − 2 = 5.",
                    "Step 3: Solve n = 7 sides (heptagon)."
                ]
            },
            {
                "question": "Diagonal AC = 24 cm splits irregular quadrilateral ABCD into ΔABC (altitude from B = 8 cm) and ΔADC (altitude from D = 5 cm). Find total area of quadrilateral ABCD:",
                "options": [
                    "156 cm²",
                    "312 cm²",
                    "120 cm²",
                    "192 cm²"
                ],
                "answer": 0,
                "hint": "Compute 1/2 × 24 × (8 + 5)!",
                "explanation": "Area(ABCD) = 1/2(24)(8) + 1/2(24)(5) = 96 + 60 = 156 cm².",
                "solution_steps": [
                    "Step 1: Area(ΔABC) = 1/2 × 24 × 8 = 96 cm².",
                    "Step 2: Area(ΔADC) = 1/2 × 24 × 5 = 60 cm².",
                    "Step 3: Sum both triangles: 96 + 60 = 156 cm²."
                ]
            },
            {
                "question": "A pentagon ABCDE is triangulated from vertex A into three triangles with areas 18 cm², 27 cm², and 15 cm². What is the total area of pentagon ABCDE?",
                "options": [
                    "60 cm²",
                    "20 cm²",
                    "45 cm²",
                    "120 cm²"
                ],
                "answer": 0,
                "hint": "Non-overlapping component triangles add directly to total polygon area!",
                "explanation": "Total area = sum of non-overlapping triangle areas = 18 + 27 + 15 = 60 cm².",
                "solution_steps": [
                    "Step 1: Triangulation cuts pentagon into 3 disjoint triangles.",
                    "Step 2: Add component areas: 18 + 27 + 15.",
                    "Step 3: Total Pentagon Area = 60 cm²."
                ]
            },
            {
                "question": "Two lines l and m are parallel. Triangle ΔPQR sits with base QR on line l and vertex P on m. If P moves right along m to P' while base length QR doubles, how does the new area compare to the old area?",
                "options": [
                    "New area exactly DOUBLES (since height stays constant while base doubles)",
                    "New area stays equal",
                    "New area quadruples",
                    "New area halves"
                ],
                "answer": 0,
                "hint": "Height h between parallel tracks l and m never changes when P slides along m!",
                "explanation": "Constant height h and doubled base (2 × QR) yield 1/2(2·QR)h = 2 × original area.",
                "solution_steps": [
                    "Step 1: Height h between parallel lines l and m remains constant.",
                    "Step 2: Base doubles from b to 2b.",
                    "Step 3: New Area = 1/2(2b)h = 2 × (1/2 bh), exactly double."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Parallelograms Rhombuses Quiz",
        "subtitle": "Mastery Quiz Part 3 (10 Questions): Parallelogram Dissection, Dual Heights, Rhombus Diagonals & Trapeziums",
        "type": "quiz",
        "questions": [
            {
                "question": "A parallelogram has base 18 cm, slanted side 11 cm, and perpendicular altitude onto the 18 cm base equal to 7 cm. What is its exact area?",
                "options": [
                    "126 cm²",
                    "198 cm²",
                    "77 cm²",
                    "63 cm²"
                ],
                "answer": 0,
                "hint": "Multiply base (18 cm) by its perpendicular height (7 cm), NOT the slant side 11 cm!",
                "explanation": "Area = base × perpendicular height = 18 × 7 = 126 cm².",
                "solution_steps": [
                    "Step 1: Identify base b = 18 cm and corresponding perpendicular height h = 7 cm.",
                    "Step 2: Apply A = b × h = 18 × 7.",
                    "Step 3: Parallelogram Area = 126 cm²."
                ]
            },
            {
                "question": "In the dissection transforming parallelogram ABCD (cut height DE, extension height CF) into rectangle EFCD, which theorem proves ΔAED ≅ ΔBFC?",
                "options": [
                    "RHS congruence (90° right angles, equal hypotenuses AD = BC, equal sides DE = CF)",
                    "SSS congruence using unknown slant base",
                    "AAA angle congruence",
                    "Trapezium copy theorem"
                ],
                "answer": 0,
                "hint": "Check what is equal in ΔAED and ΔBFC: 90° angles, opposite parallel sides AD = BC, and equal heights DE = CF!",
                "explanation": "∠AED = ∠BFC = 90° (R), AD = BC (H), DE = CF (S) proves ΔAED ≅ ΔBFC by RHS.",
                "solution_steps": [
                    "Step 1: Heights DE and CF make ∠AED = ∠BFC = 90° (Right angle).",
                    "Step 2: Opposite sides of parallelogram give AD = BC (Hypotenuse).",
                    "Step 3: Parallel tracks give equal height DE = CF (Side) → ΔAED ≅ ΔBFC by RHS."
                ]
            },
            {
                "question": "Adjacent sides of a parallelogram measure 20 cm and 12 cm. If the perpendicular height corresponding to the 20 cm base is 9 cm, find the perpendicular height onto the 12 cm side:",
                "options": [
                    "15 cm",
                    "9 cm",
                    "5.4 cm",
                    "20 cm"
                ],
                "answer": 0,
                "hint": "Equate 20 × 9 = 12 × h₂!",
                "explanation": "Area = 20 × 9 = 180 cm². Solving 12 × h₂ = 180 gives h₂ = 15 cm.",
                "solution_steps": [
                    "Step 1: Area = 20 cm × 9 cm = 180 cm².",
                    "Step 2: Using 12 cm base: 12 × h₂ = 180.",
                    "Step 3: h₂ = 180 ÷ 12 = 15 cm."
                ]
            },
            {
                "question": "Why are diagonals AC and BD of every rhombus critical in deriving its area formula Area = 1/2 × d₁ × d₂?",
                "options": [
                    "Because rhombus diagonals bisect each other perpendicularly at 90°, splitting the rhombus into right/altitude triangles totaling half the bounding rectangle d₁ × d₂",
                    "Because rhombus diagonals are always equal in length",
                    "Because diagonals match perimeter",
                    "Only when the rhombus is a square"
                ],
                "answer": 0,
                "hint": "Think about the 90° crossing angle and equal half-diagonals!",
                "explanation": "Perpendicular bisection creates four right triangles (or two altitude-d₂/2 triangles on base d₁) summing to 1/2 × d₁ × d₂.",
                "solution_steps": [
                    "Step 1: Rhombus diagonals intersect at 90° and bisect each other.",
                    "Step 2: Diagonal d₁ forms shared base of two triangles each having height d₂/2.",
                    "Step 3: Combined area = 2 × [1/2 × d₁ × (d₂/2)] = 1/2 × d₁ × d₂."
                ]
            },
            {
                "question": "Find the area of a rhombus whose diagonals measure 18 cm and 26 cm:",
                "options": [
                    "234 cm²",
                    "468 cm²",
                    "88 cm²",
                    "117 cm²"
                ],
                "answer": 0,
                "hint": "Compute 1/2 × 18 × 26!",
                "explanation": "Area = 1/2 × 18 × 26 = 9 × 26 = 234 cm².",
                "solution_steps": [
                    "Step 1: Identify diagonals d₁ = 18 cm, d₂ = 26 cm.",
                    "Step 2: Apply Area = 1/2 × d₁ × d₂ = 1/2 × 18 × 26.",
                    "Step 3: 9 × 26 = 234 cm²."
                ]
            },
            {
                "question": "A rhombus has area 120 cm² and one diagonal measuring 10 cm. Find its second diagonal d₂:",
                "options": [
                    "24 cm",
                    "12 cm",
                    "6 cm",
                    "48 cm"
                ],
                "answer": 0,
                "hint": "Solve 1/2 × 10 × d₂ = 120!",
                "explanation": "5 × d₂ = 120 yields d₂ = 24 cm.",
                "solution_steps": [
                    "Step 1: Set up 1/2 × 10 × d₂ = 120.",
                    "Step 2: Simplify to 5 × d₂ = 120.",
                    "Step 3: Divide by 5: d₂ = 24 cm."
                ]
            },
            {
                "question": "Find the area of a trapezium with parallel sides measuring 13 cm and 21 cm separated by perpendicular height 8 cm:",
                "options": [
                    "136 cm²",
                    "272 cm²",
                    "34 cm²",
                    "68 cm²"
                ],
                "answer": 0,
                "hint": "Compute 1/2 × 8 × (13 + 21)!",
                "explanation": "Area = 1/2 × 8 × 34 = 4 × 34 = 136 cm².",
                "solution_steps": [
                    "Step 1: Sum parallel bases: a + b = 13 + 21 = 34 cm.",
                    "Step 2: Multiply by height and 1/2: 1/2 × 8 × 34.",
                    "Step 3: 4 × 34 = 136 cm²."
                ]
            },
            {
                "question": "Rotating a congruent copy of a trapezium (parallel sides a and b, height h) by 180° and joining along a non-parallel side creates what shape?",
                "options": [
                    "A parallelogram of total base (a + b) and height h, proving 1 trapezium covers 1/2 × h × (a + b)",
                    "A square of side (a + b)",
                    "A rhombus of diagonals a and b",
                    "A triangle of base (a − b)"
                ],
                "answer": 0,
                "hint": "Top edge a joins upside-down bottom edge b along both parallel borders!",
                "explanation": "Two congruent trapeziums form a parallelogram of base (a + b) and height h; half of it is 1/2 × h × (a + b).",
                "solution_steps": [
                    "Step 1: Inverted copy aligns top base a with original bottom base b → total base (a + b).",
                    "Step 2: Resulting parallelogram has Area = (a + b) × h.",
                    "Step 3: Single trapezium covers half = 1/2 × h × (a + b)."
                ]
            },
            {
                "question": "A trapezium-shaped garden bed has area 140 m², parallel front edge 12 m, and parallel back edge 23 m. What is its perpendicular depth (height)?",
                "options": [
                    "8 m",
                    "4 m",
                    "16 m",
                    "10 m"
                ],
                "answer": 0,
                "hint": "Solve 1/2 × h × (12 + 23) = 140!",
                "explanation": "1/2 × h × 35 = 140 → 35h = 280 → h = 8 m.",
                "solution_steps": [
                    "Step 1: Sum parallel edges: 12 + 23 = 35 m.",
                    "Step 2: Set 1/2 × h × 35 = 140 → 35h = 280.",
                    "Step 3: h = 280 ÷ 35 = 8 m."
                ]
            },
            {
                "question": "A rhombus has side length 13 cm and one diagonal equal to 24 cm. Using perpendicular bisection and Baudhāyana-Pythagoras, find the area of the rhombus:",
                "options": [
                    "120 cm²   (second diagonal = 10 cm → 1/2 × 24 × 10)",
                    "312 cm²",
                    "240 cm²",
                    "156 cm²"
                ],
                "answer": 0,
                "hint": "Half-diagonal = 12 cm with hypotenuse side 13 cm gives other half-diagonal √(13² − 12²) = 5 cm → d₂ = 10 cm!",
                "explanation": "12² + 5² = 13² makes half-diagonals 12 cm and 5 cm (full diagonals 24 cm and 10 cm). Area = 1/2 × 24 × 10 = 120 cm².",
                "solution_steps": [
                    "Step 1: Half of given diagonal = 24 ÷ 2 = 12 cm.",
                    "Step 2: Right triangle gives other half-diagonal = √(13² − 12²) = √25 = 5 cm → d₂ = 10 cm.",
                    "Step 3: Rhombus Area = 1/2 × 24 × 10 = 120 cm²."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Units Applications Summary",
        "subtitle": "Mastery Quiz Part 4 (10 Questions): Real-Life Units (cm², m², ft², km², acres, 1 in = 2.54 cm) & Indian Local Units",
        "type": "quiz",
        "questions": [
            {
                "question": "How many square centimeters (cm²) equal 2.5 square meters (m²)?",
                "options": [
                    "25,000 cm²",
                    "250 cm²",
                    "2,500 cm²",
                    "250,000 cm²"
                ],
                "answer": 0,
                "hint": "Multiply 2.5 by 100 × 100 = 10,000!",
                "explanation": "Since 1 m² = 100 cm × 100 cm = 10,000 cm², 2.5 m² = 2.5 × 10,000 = 25,000 cm².",
                "solution_steps": [
                    "Step 1: Note 1 m = 100 cm.",
                    "Step 2: 1 m² = 100 cm × 100 cm = 10,000 cm².",
                    "Step 3: 2.5 × 10,000 = 25,000 cm²."
                ]
            },
            {
                "question": "Given 1 inch = 2.54 cm, find the exact area in cm² of a rectangular sticker measuring 2 inches by 5 inches:",
                "options": [
                    "64.516 cm²   (10 × 2.54² = 64.516 cm²)",
                    "25.4 cm²",
                    "10 cm²",
                    "50.8 cm²"
                ],
                "answer": 0,
                "hint": "Area = 10 in², and each 1 in² = (2.54)² = 6.4516 cm²!",
                "explanation": "(2 × 2.54 cm) × (5 × 2.54 cm) = 5.08 × 12.7 = 64.516 cm².",
                "solution_steps": [
                    "Step 1: Convert sides to cm: 2 in = 5.08 cm, 5 in = 12.70 cm.",
                    "Step 2: Multiply: 5.08 × 12.7 = 64.516 cm².",
                    "Step 3: Equivalently, 10 in² × (2.54)² = 64.516 cm²."
                ]
            },
            {
                "question": "Which unit scale is MOST practical for measuring the surface area of an entire city or national park?",
                "options": [
                    "Square kilometers (km²) or hectares / acres",
                    "Square millimeters (mm²)",
                    "Square centimeters (cm²)",
                    "Square inches (in²)"
                ],
                "answer": 0,
                "hint": "Think which unit avoids billions of tiny digits when expressing city sizes!",
                "explanation": "Large geographic regions such as cities and parks are measured in km², hectares, or acres.",
                "solution_steps": [
                    "Step 1: Paper/stamps use cm²; rooms/classrooms use m² or ft².",
                    "Step 2: Farms/plots use acres, hectares, or local land units.",
                    "Step 3: Cities/states use km² (1 km² = 1,000,000 m²)."
                ]
            },
            {
                "question": "In traditional Indian land measurement across states, which set lists genuine traditional local area units studied in Chapter 14?",
                "options": [
                    "Bigha, gaj, katha, dhur, cent, and ankanam",
                    "Meter, liter, kilogram, and ampere",
                    "Radian, degree, minute, and second",
                    "Pixel, byte, hertz, and watt"
                ],
                "answer": 0,
                "hint": "Recall the six local Indian land units highlighted in Areas in Real Life!",
                "explanation": "Bigha, gaj, katha, dhur, cent, and ankanam are traditional Indian land measurement units.",
                "solution_steps": [
                    "Step 1: Metric units include cm², m², hectares, and km².",
                    "Step 2: Imperial units include in², ft², and acres.",
                    "Step 3: Traditional Indian local land units include bigha, gaj, katha, dhur, cent, and ankanam."
                ]
            },
            {
                "question": "How many square meters (m²) equal 1 square kilometer (km²)?",
                "options": [
                    "1,000,000 m²   (1,000 m × 1,000 m)",
                    "1,000 m²",
                    "10,000 m²",
                    "100,000 m²"
                ],
                "answer": 0,
                "hint": "Since 1 km = 1,000 m, square BOTH sides!",
                "explanation": "1 km² = 1,000 m × 1,000 m = 1,000,000 m² (= 100 hectares).",
                "solution_steps": [
                    "Step 1: 1 km = 1,000 m.",
                    "Step 2: Area = 1 km × 1 km = 1,000 m × 1,000 m.",
                    "Step 3: Product = 1,000,000 m²."
                ]
            },
            {
                "question": "A classroom floor measures 9 m by 6 m. If square floor tiles each have side 50 cm (0.5 m), how many tiles cover the floor exactly?",
                "options": [
                    "216 tiles",
                    "108 tiles",
                    "54 tiles",
                    "432 tiles"
                ],
                "answer": 0,
                "hint": "Floor area = 54 m²; one 0.5 m × 0.5 m tile covers 0.25 m² (so 4 tiles per m²)!",
                "explanation": "Floor = 54 m². Tile = 0.25 m². Number of tiles = 54 ÷ 0.25 = 54 × 4 = 216 tiles.",
                "solution_steps": [
                    "Step 1: Classroom Area = 9 m × 6 m = 54 m².",
                    "Step 2: Tile side = 0.5 m → Tile Area = 0.5 × 0.5 = 0.25 m².",
                    "Step 3: Tiles needed = 54 ÷ 0.25 = 216 tiles."
                ]
            },
            {
                "question": "How many square inches (in²) equal exactly 1 square foot (ft²)?",
                "options": [
                    "144 in²   (12 in × 12 in)",
                    "12 in²",
                    "24 in²",
                    "100 in²"
                ],
                "answer": 0,
                "hint": "Recall 1 foot = 12 inches, then square BOTH dimensions!",
                "explanation": "1 ft² = 12 in × 12 in = 144 in².",
                "solution_steps": [
                    "Step 1: 1 foot = 12 inches.",
                    "Step 2: 1 ft² = (12 in) × (12 in).",
                    "Step 3: 12 × 12 = 144 in²."
                ]
            },
            {
                "question": "In northern and eastern India, larger agricultural plots measured in BIGHA are commonly subdivided into smaller regional units called:",
                "options": [
                    "Katha and dhur",
                    "Litres and millilitres",
                    "Newtons and pascals",
                    "Inches and centimeters"
                ],
                "answer": 0,
                "hint": "Recall the hierarchical pair katha and dhur used alongside bigha!",
                "explanation": "Bigha subdivides regionally into katha and dhur (while cent and ankanam are widely used in South India and gaj equals a square yard).",
                "solution_steps": [
                    "Step 1: Identify metric/imperial units vs regional units.",
                    "Step 2: Recall bigha → katha → dhur subdivision hierarchy.",
                    "Step 3: Confirm option 'Katha and dhur'."
                ]
            },
            {
                "question": "A rectangular path around a lawn (outer 22 m × 14 m, inner lawn 18 m × 10 m) is paved at ₹150 per m². Find the exact paving cost:",
                "options": [
                    "₹19,200   (Path area = 308 − 180 = 128 m²)",
                    "₹46,200",
                    "₹27,000",
                    "₹9,600"
                ],
                "answer": 0,
                "hint": "Subtract inner lawn area (18 × 10) from outer rectangle area (22 × 14), then multiply by ₹150!",
                "explanation": "Path area = 308 − 180 = 128 m². Cost = 128 × ₹150 = ₹19,200.",
                "solution_steps": [
                    "Step 1: Outer area = 22 × 14 = 308 m².",
                    "Step 2: Inner lawn = 18 × 10 = 180 m² → Path area = 308 − 180 = 128 m².",
                    "Step 3: Paving cost = 128 × 150 = ₹19,200."
                ]
            },
            {
                "question": "Which grand insight summarizes all area formulas across Chapter 14?",
                "options": [
                    "Triangles, parallelograms, rhombuses, trapeziums, and arbitrary polygons derive logically from rectangle unit-square packing (l × w) via dissection and doubling",
                    "Perimeter length always uniquely determines polygon area",
                    "Only squares can measure area without height",
                    "Multiplying slant edge lengths gives exact parallelogram and trapezium areas"
                ],
                "answer": 0,
                "hint": "Look back at how half-rectangles, RHS shifts, 90° diagonals, and inverted copies reduce everything to rectangles!",
                "explanation": "Every formula builds logically from rectangle l × w via area-preserving dissections and congruent pairings.",
                "solution_steps": [
                    "Step 1: Rectangle Area = l × w comes from non-overlapping unit squares.",
                    "Step 2: Triangle (1/2 bh), Parallelogram (bh), Rhombus (1/2 d₁d₂), Trapezium (1/2 h(a+b)) derive by dissection/copying.",
                    "Step 3: Any n-gon triangulates into (n − 2) triangles."
                ]
            }
        ]
    }
]

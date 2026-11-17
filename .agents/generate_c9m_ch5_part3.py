#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 5: I'm Up and Down, and Round and Round
Slides Data Generator - Part 3 (Slides 17 to 20 - Silent Mastery Quizzes, 40 Questions Total)
Strictly 1-3 word titles, zero spoken audio, zero human names, hints + 3-step solutions.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Symmetry Chords Quiz",
        "subtitle": "Sections 5.1–5.5 Practice Set (10 Questions): Locus Definition, Symmetries, Circumcircles (Thm 1) & Equal Chords/Bisectors (Thm 2–5)",
        "questions": [
            {
                "question": "What is the geometric locus of all points in a plane that remain at a constant distance r from a fixed point O?",
                "options": ["A circle with centre O and radius r", "A straight line through O", "A square of side r", "A perpendicular bisector"],
                "answer": 0,
                "hint": "Check Section 5.1 Definitions!",
                "explanation": "By definition, a circle is the plane locus of points equidistant (distance r) from fixed centre O.",
                "solution_steps": [
                    "Fix centre O and constant positive distance r in the plane.",
                    "Collect all points P satisfying OP = r.",
                    "That closed curve is the circle of centre O and radius r."
                ]
            },
            {
                "question": "How many distinct lines of reflection symmetry pass through a circle of radius 5 cm?",
                "options": ["Infinitely many (every diameter line)", "Exactly 4", "Exactly 2", "Only 1"],
                "answer": 0,
                "hint": "Every line passing through Centre O is a diameter and splits the circle into two congruent halves!",
                "explanation": "Any diameter acts as a mirror reflection line; infinitely many lines pass through Centre O.",
                "solution_steps": [
                    "Every reflection axis of a circle must fold one half identically onto the other.",
                    "Any diameter passing through Centre O cuts the circle into two congruent semicircles.",
                    "Since infinitely many diameters pass through O, there are infinitely many reflection lines."
                ]
            },
            {
                "question": "All circles passing simultaneously through two fixed distinct points A and B have their centres located strictly along:",
                "options": ["The perpendicular bisector of segment AB", "Segment AB itself only", "A line parallel to AB at distance 2 cm", "Only Point A"],
                "answer": 0,
                "hint": "A centre O must satisfy OA = OB!",
                "explanation": "Points equidistant from endpoints A and B form the perpendicular bisector of AB.",
                "solution_steps": [
                    "For any circle through A and B, radius constraint forces OA = OB.",
                    "Every point equidistant from A and B lies on the perpendicular bisector of AB.",
                    "Any point along that line (infinitely many) defines a valid circle."
                ]
            },
            {
                "question": "What is the minimum number of non-collinear points required to determine ONE UNIQUE circle?",
                "options": ["3 non-collinear points (Theorem 1)", "1 point", "2 points", "5 points"],
                "answer": 0,
                "hint": "Two perpendicular bisectors intersect uniquely when points aren't collinear!",
                "explanation": "By Theorem 1, exactly one circle passes through three given non-collinear points.",
                "solution_steps": [
                    "1 or 2 points admit infinitely many circles.",
                    "3 non-collinear points A, B, C produce non-parallel perpendicular bisectors of AB and BC.",
                    "Their single intersection O is the unique circumcentre satisfying OA = OB = OC."
                ]
            },
            {
                "question": "In a right-angled triangle ABC with right angle at B (∠B = 90°), where does its circumcentre strictly lie?",
                "options": ["At the exact midpoint of hypotenuse AC", "Outside the triangle beyond vertex B", "Inside ΔABC away from all three edges", "At vertex A"],
                "answer": 0,
                "hint": "Recall the semicircle corollary: hypotenuse AC acts as a diameter!",
                "explanation": "If M is midpoint of AC, MA = MC = MB = AC/2 because ∠ABC = 90° sits in a semicircle.",
                "solution_steps": [
                    "Right triangle ABC has ∠B = 90° facing hypotenuse AC.",
                    "Angle in a semicircle is 90°, so AC must be the circumcircle's diameter.",
                    "The centre of a diameter lies at its midpoint M, making M the circumcentre."
                ]
            },
            {
                "question": "Where is the circumcentre located for an OBTUSE-angled triangle?",
                "options": ["Strictly OUTSIDE the triangle (on the side opposite the obtuse angle)", "Always inside the triangle", "On the shortest side", "At the obtuse vertex"],
                "answer": 0,
                "hint": "Check whether the major arc > 180° keeps Centre O outside the triangle!",
                "explanation": "For an obtuse angle > 90°, the opposite side spans a minor arc on one side while O sits outside on the opposite side.",
                "solution_steps": [
                    "Suppose ∠B > 90° in ΔABC.",
                    "Arc AC subtending ∠B at vertex B must be a major arc (> 180° central reflex angle) on the B-side.",
                    "Hence Centre O lies outside ΔABC beyond longest side AC."
                ]
            },
            {
                "question": "In a circle with Centre O, chords AB and CD both measure 9 cm. If ∠AOB = 64°, what does ∠COD equal by Theorem 2?",
                "options": ["64°", "32°", "128°", "26°"],
                "answer": 0,
                "hint": "Equal chords subtend equal angles at the centre!",
                "explanation": "By Theorem 2, equal chords AB = CD yield congruent triangles ΔAOB ≅ ΔCOD (SSS), so ∠COD = ∠AOB = 64°.",
                "solution_steps": [
                    "Compare ΔAOB and ΔCOD: OA = OC (radii), OB = OD (radii), and AB = CD = 9 cm.",
                    "By SSS congruence, ΔAOB ≅ ΔCOD.",
                    "Corresponding central angles match: ∠COD = ∠AOB = 64°."
                ]
            },
            {
                "question": "Conversely (Theorem 3), if two chords PQ and RS subtend equal central angles ∠POQ = ∠ROS = 75° and PQ = 11.4 cm, what is RS?",
                "options": ["11.4 cm", "5.7 cm", "22.8 cm", "7.5 cm"],
                "answer": 0,
                "hint": "Use SAS congruence on ΔPOQ and ΔROS!",
                "explanation": "Equal radii and equal included central angles imply ΔPOQ ≅ ΔROS (SAS) ⇒ RS = PQ = 11.4 cm.",
                "solution_steps": [
                    "In ΔPOQ and ΔROS: OP = OR (radii), ∠POQ = ∠ROS = 75°, OQ = OS (radii).",
                    "By SAS congruence, ΔPOQ ≅ ΔROS.",
                    "Therefore RS = PQ = 11.4 cm (CPCTC)."
                ]
            },
            {
                "question": "If Centre O is joined straight to the midpoint M of chord AB (where AB is not a diameter), what angle does OM make with chord AB (Theorem 4)?",
                "options": ["90° (OM ⊥ AB)", "45°", "60°", "180°"],
                "answer": 0,
                "hint": "ΔOAM ≅ ΔOBM by SSS splits the 180° straight line at M into two equal halves!",
                "explanation": "Theorem 4 proves the line from centre to chord midpoint is perpendicular to the chord: 90°.",
                "solution_steps": [
                    "In ΔOAM and ΔOBM: OA = OB (radii), AM = MB (midpoint), OM = OM (shared).",
                    "By SSS congruence, ∠OMA = ∠OMB.",
                    "Since ∠OMA + ∠OMB = 180° (linear pair), ∠OMA = 90°."
                ]
            },
            {
                "question": "A perpendicular dropped from Centre O hits chord XY at K. If full chord length XY = 26 cm, what is segment XK by Theorem 5?",
                "options": ["13 cm", "26 cm", "6.5 cm", "52 cm"],
                "answer": 0,
                "hint": "Theorem 5 states the perpendicular from the centre bisects the chord!",
                "explanation": "Perpendicular OK bisects XY via RHS congruence (ΔOKX ≅ ΔOKY), so XK = XY/2 = 13 cm.",
                "solution_steps": [
                    "OK ⊥ XY gives ∠OKX = ∠OKY = 90°.",
                    "In right triangles ΔOKX and ΔOKY: OX = OY (radii) and OK is shared ⇒ ΔOKX ≅ ΔOKY (RHS).",
                    "Hence XK = KY = 26/2 = 13 cm."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Chord Distance Quiz",
        "subtitle": "Sections 5.5–5.6.1 Practice Set (10 Questions): Perpendicular Bisectors, Chord-Centre Distances (Thm 6–7) & Longer Chords Closer (Thm 8)",
        "questions": [
            {
                "question": "A chord of length 24 cm sits at a perpendicular distance of 5 cm from the centre O of a circle. Calculate the radius of the circle.",
                "options": ["13 cm", "12 cm", "19 cm", "29 cm"],
                "answer": 0,
                "hint": "First bisect chord 24 cm into 12 cm using Theorem 5, then apply Pythagoras to legs 12 and 5!",
                "explanation": "Half-chord = 12 cm, distance d = 5 cm ⇒ r = √(12² + 5²) = √169 = 13 cm.",
                "solution_steps": [
                    "Perpendicular OM from O bisects chord AB = 24 cm, so AM = 12 cm.",
                    "In right ΔOMA, OM = 5 cm and AM = 12 cm.",
                    "Radius OA = √(12² + 5²) = √(144 + 25) = √169 = 13 cm."
                ]
            },
            {
                "question": "In a circle of radius 17 cm, find the length of a chord located 8 cm away from the centre.",
                "options": ["30 cm", "15 cm", "9 cm", "25 cm"],
                "answer": 0,
                "hint": "Compute half-chord = √(17² − 8²) first, then DOUBLE it!",
                "explanation": "Half-chord = √(289 − 64) = √225 = 15 cm; full chord = 2 × 15 = 30 cm.",
                "solution_steps": [
                    "Right triangle OMA has hypotenuse r = 17 cm and distance OM = 8 cm.",
                    "Half-chord AM = √(17² − 8²) = √(289 − 64) = 15 cm.",
                    "By Theorem 5, full chord length AB = 2 × AM = 30 cm."
                ]
            },
            {
                "question": "If two chords AB and CD in the same circle satisfy AB = CD = 18 cm, and chord AB sits 4 cm from Centre O, how far does chord CD sit from Centre O (Theorem 6)?",
                "options": ["4 cm", "8 cm", "9 cm", "2 cm"],
                "answer": 0,
                "hint": "Theorem 6: Equal chords of a circle are equidistant from the centre!",
                "explanation": "Equal chords AB = CD ensure ON = OM = 4 cm.",
                "solution_steps": [
                    "Chords AB and CD have equal length 18 cm (half-chords both 9 cm).",
                    "Both share the same circle radius r, so √(r² − 9²) gives identical distance.",
                    "Thus ON = OM = 4 cm by Theorem 6."
                ]
            },
            {
                "question": "Conversely (Theorem 7), chords PQ and RS both sit at perpendicular distance 7 cm from Centre O. If PQ = 14 cm, what is RS?",
                "options": ["14 cm", "7 cm", "28 cm", "21 cm"],
                "answer": 0,
                "hint": "Chords equidistant from the centre must have equal length!",
                "explanation": "Equidistant distances OM = ON = 7 cm imply ΔOAM ≅ ΔOCN (RHS) ⇒ RS = PQ = 14 cm.",
                "solution_steps": [
                    "Perpendicular distances from O to PQ and RS are both 7 cm.",
                    "In right triangles formed with radii, hypotenuse r and leg 7 cm match (RHS).",
                    "Half-chords match, forcing full chord RS = PQ = 14 cm."
                ]
            },
            {
                "question": "Three chords inside a single circle of radius 10 cm have lengths AB = 18 cm, CD = 12 cm, and EF = 20 cm. Rank them from CLOSEST to FARTHEST from Centre O.",
                "options": ["EF (closest, distance 0), then AB, then CD (farthest)", "CD (closest), then AB, then EF (farthest)", "AB (closest), then EF, then CD", "All three are equidistant from O"],
                "answer": 0,
                "hint": "Theorem 8: Longer chord ⇒ smaller distance from Centre O! Note EF = 2r = 20 cm is a diameter!",
                "explanation": "Since 20 > 18 > 12, distances satisfy d(EF) = 0 < d(AB) < d(CD).",
                "solution_steps": [
                    "Recall Theorem 8: longer chords sit closer to Centre O.",
                    "Compare lengths: EF = 20 cm (diameter, d = 0) > AB = 18 cm > CD = 12 cm.",
                    "Ordering from closest to farthest: EF → AB → CD."
                ]
            },
            {
                "question": "Two chords AB and CD of a circle have perpendicular distances from Centre O of d₁ = 3 cm and d₂ = 7 cm respectively. Which chord is LONGER?",
                "options": ["Chord AB (smaller distance 3 cm means longer chord)", "Chord CD", "Both have identical length", "Cannot be compared without knowing radius"],
                "answer": 0,
                "hint": "Apply Theorem 8 inversely: smaller distance d leaves larger √(r² − d²)!",
                "explanation": "Since d₁ = 3 cm < d₂ = 7 cm, r² − 3² > r² − 7², so chord AB > chord CD.",
                "solution_steps": [
                    "Half-chord squared equals r² − d².",
                    "Compare distances: 3 cm < 7 cm ⇒ r² − 9 > r² − 49.",
                    "Therefore AB > CD (closer chord AB is longer)."
                ]
            },
            {
                "question": "A circle has diameter 50 cm (radius 25 cm). A chord of length 48 cm sits how many centimetres away from the centre?",
                "options": ["7 cm", "14 cm", "24 cm", "2 cm"],
                "answer": 0,
                "hint": "Half-chord = 24 cm, radius = 25 cm; compute √(25² − 24²)!",
                "explanation": "d = √(25² − 24²) = √(625 − 576) = √49 = 7 cm.",
                "solution_steps": [
                    "Radius r = 50/2 = 25 cm; half-chord = 48/2 = 24 cm.",
                    "Apply Pythagoras: d² = 25² − 24² = 625 − 576 = 49.",
                    "Take positive square root: d = 7 cm."
                ]
            },
            {
                "question": "How many chords of length strictly equal to the diameter (2r) can share the same orientation (parallel direction)?",
                "options": ["Only 1 (the unique diameter in that direction passes through O)", "2 chords (one on each side of O)", "Infinitely many", "0 chords"],
                "answer": 0,
                "hint": "Any chord parallel to a diameter sits at distance d > 0 and is strictly shorter!",
                "explanation": "Every chord of length 2r must pass through O (d = 0); only one line through O has a given slope.",
                "solution_steps": [
                    "Longest chord L = 2r occurs uniquely when distance d = 0 (passing through Centre O).",
                    "Only one straight line passes through fixed point O in a given direction.",
                    "All parallel chords sit at d > 0 and have length < 2r."
                ]
            },
            {
                "question": "If chords AB and CD intersect inside a circle at P and line OP bisects ∠APD, why must chords AB and CD be EQUAL in length?",
                "options": [
                    "OP bisecting ∠APD makes perpendicular distances OM = ON from O to both chords equal (RHS), forcing AB = CD by Theorem 7",
                    "Every pair of intersecting chords is automatically equal",
                    "Because OP must equal radius r",
                    "Because intersecting chords are always diameters"
                ],
                "answer": 0,
                "hint": "Drop perpendiculars OM ⊥ AB and ON ⊥ CD and compare right triangles ΔOMP and ΔONP!",
                "explanation": "AAS congruence on ΔOMP and ΔONP proves OM = ON, which guarantees equal chords AB = CD by Theorem 7.",
                "solution_steps": [
                    "Drop perpendiculars OM ⊥ AB and ON ⊥ CD.",
                    "In ΔOMP and ΔONP: ∠OMP = ∠ONP = 90°, ∠OPM = ∠OPN (angle bisector), OP shared ⇒ ΔOMP ≅ ΔONP (AAS).",
                    "Hence OM = ON ⇒ chords AB = CD by Theorem 7."
                ]
            },
            {
                "question": "In a circle of radius 5 cm, two parallel chords AB = 8 cm and CD = 6 cm lie on the SAME side of Centre O. What is the distance between them?",
                "options": ["1 cm (4 cm − 3 cm)", "7 cm (4 cm + 3 cm)", "2 cm", "5 cm"],
                "answer": 0,
                "hint": "Find distances d₁ = √(5² − 4²) = 3 cm and d₂ = √(5² − 3²) = 4 cm, then SUBTRACT for same side!",
                "explanation": "Distance of AB is 3 cm and CD is 4 cm on the same side of O, so gap = 4 − 3 = 1 cm.",
                "solution_steps": [
                    "Half-chords are 4 cm (for AB) and 3 cm (for CD) in circle of radius r = 5 cm.",
                    "Distances from Centre O: d(AB) = √(5² − 4²) = 3 cm; d(CD) = √(5² − 3²) = 4 cm.",
                    "On the SAME side of O, gap = 4 − 3 = 1 cm."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Arcs Concyclic Quiz",
        "subtitle": "Sections 5.7–5.8 Practice Set (10 Questions): Theorem 9 (Central = 2×Inscribed), Corollaries & Cyclic Quadrilaterals (Thm 10–12)",
        "questions": [
            {
                "question": "In a circle with Centre O, minor arc PQ subtends ∠POQ = 108° at the centre. Find the angle ∠PRQ subtended at a point R on the major arc.",
                "options": ["54°", "216°", "72°", "108°"],
                "answer": 0,
                "hint": "Apply Theorem 9: inscribed angle = ½ × central angle!",
                "explanation": "∠PRQ = ½ ∠POQ = ½(108°) = 54°.",
                "solution_steps": [
                    "Arc PQ subtends central angle ∠POQ = 108° at O.",
                    "Point R lies on the remaining circle outside arc PQ.",
                    "By Theorem 9: ∠PRQ = 108° / 2 = 54°."
                ]
            },
            {
                "question": "If inscribed angle ∠ACB = 47° sits on minor arc AB, what central angle ∠AOB does arc AB subtend at Centre O?",
                "options": ["94°", "23.5°", "133°", "47°"],
                "answer": 0,
                "hint": "Central angle is TWICE the inscribed angle!",
                "explanation": "By Theorem 9, ∠AOB = 2 × ∠ACB = 2(47°) = 94°.",
                "solution_steps": [
                    "Identify inscribed angle ∠ACB = 47° facing minor arc AB.",
                    "Apply Theorem 9: central angle ∠AOB = 2 × ∠ACB.",
                    "Compute 2 × 47° = 94°."
                ]
            },
            {
                "question": "Triangle ABC is inscribed in a circle such that side AC passes directly through Centre O. If ∠BAC = 38°, calculate ∠ACB.",
                "options": ["52°", "38°", "90°", "62°"],
                "answer": 0,
                "hint": "Side AC through O is a diameter, making ∠ABC = 90° (angle in a semicircle)!",
                "explanation": "∠ABC = 90° (semicircle corollary); inside ΔABC, ∠ACB = 180° − 90° − 38° = 52°.",
                "solution_steps": [
                    "Since AC passes through Centre O, AC is a diameter.",
                    "Angle in a semicircle makes ∠ABC = 90°.",
                    "Angle sum in ΔABC: ∠ACB = 90° − 38° = 52°."
                ]
            },
            {
                "question": "Points A, B, C, D lie sequentially on a circle. Chord AD and chord BC cross inside, while points C and D both stand above chord AB. If ∠ACB = 63° and ∠BAC = 45°, find ∠ADB.",
                "options": ["63° (angles in the same segment)", "45°", "72°", "108°"],
                "answer": 0,
                "hint": "Both ∠ACB and ∠ADB subtend the exact same arc AB on the same side!",
                "explanation": "Angles subtended by the same arc AB in the same segment are equal: ∠ADB = ∠ACB = 63°.",
                "solution_steps": [
                    "Check segment of chord AB containing both points C and D.",
                    "Both ∠ACB and ∠ADB sit on arc AB in the same segment.",
                    "By Theorem 9 corollary, ∠ADB = ∠ACB = 63°."
                ]
            },
            {
                "question": "In cyclic quadrilateral KLMN, ∠K = (3x + 10)° and opposite angle ∠M = (2x + 20)°. Solve for x and find ∠K.",
                "options": ["x = 30, ∠K = 100°", "x = 20, ∠K = 70°", "x = 18, ∠K = 64°", "x = 36, ∠K = 118°"],
                "answer": 0,
                "hint": "Opposite angles of a cyclic quadrilateral sum to 180° (Theorem 11)!",
                "explanation": "(3x + 10) + (2x + 20) = 180 ⇒ 5x + 30 = 180 ⇒ 5x = 150 ⇒ x = 30 ⇒ ∠K = 100°.",
                "solution_steps": [
                    "By Theorem 11, opposite angles satisfy ∠K + ∠M = 180°.",
                    "Set (3x + 10) + (2x + 20) = 180 ⇒ 5x = 150 ⇒ x = 30.",
                    "Evaluate ∠K = 3(30) + 10 = 100° (and ∠M = 80°)."
                ]
            },
            {
                "question": "In cyclic quadrilateral ABCD, side AB is extended outward to ray ABE. If interior opposite angle ∠ADC = 118°, what is exterior angle ∠CBE?",
                "options": ["118° (exterior angle of cyclic quad equals interior opposite angle)", "62°", "90°", "59°"],
                "answer": 0,
                "hint": "First use ∠CBA = 180° − 118° = 62°, then subtract from straight line 180°!",
                "explanation": "∠CBA = 180° − 118° = 62°, so linear pair ∠CBE = 180° − 62° = 118° = ∠ADC.",
                "solution_steps": [
                    "By Theorem 11, opposite angle ∠ABC = 180° − ∠ADC = 180° − 118° = 62°.",
                    "Angles ∠ABC and ∠CBE form a straight-line linear pair (180°).",
                    "Hence exterior angle ∠CBE = 180° − 62° = 118° (equal to ∠ADC)."
                ]
            },
            {
                "question": "Points P and Q lie on the same side of segment AB. If ∠APB = 74° and ∠AQB = 74°, what theorem immediately proves A, B, P, and Q lie on one circle?",
                "options": ["Theorem 10 (equal angles subtended on the same side of a line segment are concyclic)", "Theorem 4 (centre-midpoint perpendicular)", "Theorem 8 (longest chord diameter)", "Triangle exterior angle theorem only"],
                "answer": 0,
                "hint": "Recall Section 5.8 Concyclicity of Points!",
                "explanation": "Theorem 10 directly establishes concyclicity when equal angles stand on the same side of segment AB.",
                "solution_steps": [
                    "Check side: both P and Q lie on the same side of AB.",
                    "Check equality: ∠APB = ∠AQB = 74°.",
                    "By Theorem 10, vertices A, B, Q, P all lie on one unique circle."
                ]
            },
            {
                "question": "An arc subtends central reflex angle ∠AOB = 240° at Centre O (major arc). What is the inscribed angle ∠APB standing at a point P on the minor arc?",
                "options": ["120°", "60°", "80°", "150°"],
                "answer": 0,
                "hint": "Theorem 9 applies equally to reflex central angles: ∠APB = ½ (reflex ∠AOB)!",
                "explanation": "∠APB = ½ × 240° = 120°. (Notice this matches cyclic quad 180° − 60° = 120°!)",
                "solution_steps": [
                    "Point P on minor arc faces the major arc whose central reflex angle is 240°.",
                    "Apply Theorem 9 directly: ∠APB = ½ (reflex ∠AOB).",
                    "Compute ½ × 240° = 120° (obtuse inscribed angle!)."
                ]
            },
            {
                "question": "Which set of four interior quadrilateral angles CANNOT belong to a cyclic quadrilateral (going sequentially around vertices A, B, C, D)?",
                "options": ["95°, 110°, 95°, 60°", "90°, 90°, 90°, 90°", "115°, 80°, 65°, 100°", "72°, 108°, 108°, 72°"],
                "answer": 0,
                "hint": "Check opposite pairs ∠A + ∠C = 180° AND ∠B + ∠D = 180°!",
                "explanation": "In 95°, 110°, 95°, 60°, opposite pairs give 95 + 95 = 190° ≠ 180° and 110 + 60 = 170° ≠ 180°.",
                "solution_steps": [
                    "By Theorem 11, BOTH opposite pairs (1st+3rd) and (2nd+4th) must sum to 180°.",
                    "Check Option 1: 95° + 95° = 190° ≠ 180° (fails Theorem 11!).",
                    "All other three options satisfy 180° opposite sums."
                ]
            },
            {
                "question": "In a circle with Centre O, ∠OAB = 32° inside ΔOAB. Find the angle ∠ACB subtended by minor chord AB on the major arc.",
                "options": ["58°", "32°", "116°", "64°"],
                "answer": 0,
                "hint": "ΔOAB is isosceles (OA = OB), so find ∠AOB first, then halve it!",
                "explanation": "Since OA = OB, ∠OBA = 32° ⇒ ∠AOB = 180° − 64° = 116° ⇒ ∠ACB = ½(116°) = 58°.",
                "solution_steps": [
                    "Triangle OAB has radii OA = OB ⇒ ∠OBA = ∠OAB = 32°.",
                    "Compute central angle: ∠AOB = 180° − (32° + 32°) = 116°.",
                    "By Theorem 9: ∠ACB = ½(116°) = 58°."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Exercises Mastery Quiz",
        "subtitle": "End-of-Chapter Mixed Exercises (10 Questions): Multi-Step Chord Calculations, Intersecting Circles & Theorem Proofs",
        "questions": [
            {
                "question": "If two equal chords AB and CD of a circle intersect internally at point X, what geometric equality always holds between their split segments (Theorem 2/6 application)?",
                "options": ["Corresponding segments are equal: AX = CX (longer parts) and BX = DX (shorter parts)", "All four pieces AX, BX, CX, DX must be equal", "AX = DX only when chords are perpendicular", "Segments cannot be compared"],
                "answer": 0,
                "hint": "Drop perpendiculars OM ⊥ AB and ON ⊥ CD (OM = ON by Theorem 6), join OX, and use RHS!",
                "explanation": "ΔOMX ≅ ΔONX (RHS) yields MX = NX; adding/subtracting equal half-chords AM = CN gives AX = CX and BX = DX.",
                "solution_steps": [
                    "Drop perpendiculars OM ⊥ AB and ON ⊥ CD; since AB = CD, Theorem 6 gives OM = ON and AM = MB = CN = ND.",
                    "Right triangles ΔOMX and ΔONX match by RHS (OX shared, OM = ON) ⇒ MX = NX.",
                    "Adding AM + MX = CN + NX gives AX = CX, and subtracting leaves BX = DX."
                ]
            },
            {
                "question": "A chord PQ of length 16 cm lies inside a circle of radius 10 cm. Find the perpendicular distance from Centre O to chord PQ.",
                "options": ["6 cm", "8 cm", "12 cm", "4 cm"],
                "answer": 0,
                "hint": "Half of 16 cm is 8 cm inside radius-10 right triangle!",
                "explanation": "d = √(10² − 8²) = √(100 − 64) = 6 cm.",
                "solution_steps": [
                    "Perpendicular OM from O bisects PQ = 16 cm into PM = 8 cm.",
                    "In right triangle ΔOMP, hypotenuse OP = radius = 10 cm.",
                    "Distance OM = √(10² − 8²) = √36 = 6 cm."
                ]
            },
            {
                "question": "In a circle with Centre O, chord AB equals the radius r of the circle (AB = r). Find BOTH the angle subtended by AB on the MAJOR arc AND the angle subtended on the MINOR arc.",
                "options": ["30° on major arc and 150° on minor arc", "60° on major arc and 120° on minor arc", "45° on major arc and 135° on minor arc", "30° on both arcs"],
                "answer": 0,
                "hint": "Triangle OAB has OA = OB = AB (equilateral ⇒ ∠AOB = 60°)! Halve 60° for major arc, then use cyclic quad for minor arc!",
                "explanation": "Equilateral ΔOAB gives ∠AOB = 60° ⇒ major arc inscribed angle = 30° ⇒ minor arc cyclic angle = 180° − 30° = 150°.",
                "solution_steps": [
                    "Since OA = OB = AB = r, ΔOAB is equilateral, so central ∠AOB = 60°.",
                    "Inscribed angle on major arc = ½ ∠AOB = 30° (Theorem 9).",
                    "Any point on minor arc forms a cyclic quad with a major-arc point ⇒ 180° − 30° = 150° (Theorem 11)."
                ]
            },
            {
                "question": "In cyclic quadrilateral PQRS, interior angle ∠QRS = 105° and ∠PQR = 78°. Calculate the exact opposite angle ∠QPS.",
                "options": ["75°", "102°", "105°", "78°"],
                "answer": 0,
                "hint": "Identify which vertex sits directly OPPOSITE vertex P in cyclic PQRS: ∠QPS + ∠QRS = 180°!",
                "explanation": "Vertex P is opposite vertex R (∠QRS = 105°), so ∠QPS = 180° − 105° = 75°.",
                "solution_steps": [
                    "List cyclic vertices in circular order: P → Q → R → S.",
                    "Angle opposite ∠QPS is ∠QRS = 105°.",
                    "By Theorem 11: ∠QPS = 180° − 105° = 75°."
                ]
            },
            {
                "question": "Two concentric circles (same Centre O) are cut by a straight line at A, B, C, and D in order (outer circle at A, D; inner circle at B, C). Why MUST AB always equal CD?",
                "options": [
                    "Perpendicular OM dropped from shared Centre O bisects BOTH outer chord AD (AM = MD) and inner chord BC (BM = MC); subtracting yields AB = CD",
                    "Because concentric circles have equal radii",
                    "Because line ABCD must pass through Centre O",
                    "Because inner chords are longer than outer chords"
                ],
                "answer": 0,
                "hint": "Apply Theorem 5 simultaneously to BOTH concentric circles from shared Centre O!",
                "explanation": "AM = MD and BM = MC ⇒ AM − BM = MD − MC ⇒ AB = CD.",
                "solution_steps": [
                    "Draw OM ⊥ line AD from shared Centre O.",
                    "By Theorem 5 on outer circle: AM = MD. By Theorem 5 on inner circle: BM = MC.",
                    "Subtract inner half from outer half: AM − BM = MD − MC ⇒ AB = CD."
                ]
            },
            {
                "question": "ABCD is a cyclic quadrilateral whose diagonals AC and BD are BOTH diameters of the circle. What exact shape MUST ABCD be?",
                "options": ["A rectangle (all four angles equal 90°)", "Only a rhombus with 60° angles", "A non-cyclic kite", "An isosceles trapezium with non-right angles"],
                "answer": 0,
                "hint": "Every vertex faces a diameter through O, making EVERY corner angle in a semicircle 90°!",
                "explanation": "Both AC and BD are diameters, so ∠B = ∠D = 90° (on AC) and ∠A = ∠C = 90° (on BD) ⇒ ABCD is a rectangle.",
                "solution_steps": [
                    "Diameter AC subtends angles in semicircles: ∠ABC = 90° and ∠ADC = 90°.",
                    "Diameter BD subtends angles in semicircles: ∠BAD = 90° and ∠BCD = 90°.",
                    "All four angles = 90° proves ABCD is a rectangle."
                ]
            },
            {
                "question": "Two circles intersect at two points P and Q, and diameter PA is drawn in the first circle while diameter PB is drawn in the second circle. Why must A, Q, and B lie on one straight line (collinear)?",
                "options": [
                    "∠PQA = 90° (semicircle PA) and ∠PQB = 90° (semicircle PB), so ∠PQA + ∠PQB = 180° forms straight angle ∠AQB",
                    "Because PQ is parallel to AB",
                    "Because both diameters have equal radius",
                    "Because P, Q, A, B form a triangle"
                ],
                "answer": 0,
                "hint": "Connect Q to P, A, and B and apply the Semicircle Corollary TWICE at Q!",
                "explanation": "Angle in semicircle 1 makes ∠PQA = 90°; angle in semicircle 2 makes ∠PQB = 90° ⇒ ∠AQB = 180° (straight line).",
                "solution_steps": [
                    "Join common chord PQ, plus AQ and QB.",
                    "PA is a diameter of circle 1 ⇒ ∠PQA = 90° (angle in semicircle).",
                    "PB is a diameter of circle 2 ⇒ ∠PQB = 90° ⇒ ∠PQA + ∠PQB = 180°, so A–Q–B is a straight line."
                ]
            },
            {
                "question": "In a circle of radius 13 cm, two parallel chords of lengths 24 cm and 10 cm lie on OPPOSITE sides of Centre O. Find the perpendicular gap separating them.",
                "options": ["17 cm (5 cm + 12 cm)", "7 cm (12 cm − 5 cm)", "13 cm", "34 cm"],
                "answer": 0,
                "hint": "Calculate d₁ = √(13² − 12²) = 5 and d₂ = √(13² − 5²) = 12, then ADD for opposite sides!",
                "explanation": "Distances from O are 5 cm and 12 cm on opposite sides ⇒ total distance = 5 + 12 = 17 cm.",
                "solution_steps": [
                    "For 24 cm chord: half-chord = 12 cm ⇒ d₁ = √(13² − 12²) = 5 cm.",
                    "For 10 cm chord: half-chord = 5 cm ⇒ d₂ = √(13² − 5²) = 12 cm.",
                    "Chords on opposite sides of O give total distance = 5 + 12 = 17 cm."
                ]
            },
            {
                "question": "If a pair of opposite sides of a cyclic quadrilateral ABCD are equal (AD = BC), what special property holds for its diagonals AC and BD?",
                "options": ["Diagonals AC and BD are strictly EQUAL in length (and AB ∥ CD)", "Diagonals must be perpendicular to each other", "One diagonal must be twice the other", "Diagonals cannot cross inside the circle"],
                "answer": 0,
                "hint": "Equal chords AD = BC subtend equal inscribed angles in the same segment and form congruent triangles ΔADC ≅ ΔBCD (or arc addition)!",
                "explanation": "Equal chords AD = BC cut off equal arcs; adding shared arc AB makes arc(DAB) = arc(CBA) ⇒ chord BD = chord AC!",
                "solution_steps": [
                    "Equal chords AD = BC carve equal minor arcs: arc(AD) = arc(BC).",
                    "Add shared arc(AB) (or arc(CD)) to both sides: arc(DAB) = arc(CBA).",
                    "Equal arcs subtend equal chords ⇒ diagonal BD = diagonal AC."
                ]
            },
            {
                "question": "Verify why every cyclic trapezium (with AB ∥ DC) is automatically an ISOSCELES trapezium (AD = BC).",
                "options": [
                    "AB ∥ DC gives ∠A + ∠D = 180°, while cyclic Theorem 11 gives ∠B + ∠D = 180°, forcing base angles ∠A = ∠B and hence AD = BC",
                    "Because all trapeziums have equal diagonal angles",
                    "Because AB = DC in every trapezium",
                    "Because every cyclic quadrilateral is a square"
                ],
                "answer": 0,
                "hint": "Compare co-interior parallel sum ∠A + ∠D = 180° against cyclic opposite sum ∠B + ∠D = 180°!",
                "explanation": "Since ∠A + ∠D = 180° = ∠B + ∠D, base angles ∠A = ∠B match, forcing equal non-parallel legs AD = BC.",
                "solution_steps": [
                    "Parallel sides AB ∥ DC make co-interior angles sum to 180°: ∠A + ∠D = 180°.",
                    "Cyclic property (Theorem 11) gives opposite angles: ∠B + ∠D = 180°.",
                    "Equating both yields ∠A = ∠B ⇒ trapezium is isosceles (AD = BC)."
                ]
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 4: Quadrilaterals
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Rectangles Angles Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Quadrilateral Definitions, Carpenter's Rectangle Proofs, Squares & 360° Angle Sum",
        "questions": [
            {
                "question": "If a quadrilateral has interior angles measuring 75°, 110°, and 85°, calculate the exact measure of its fourth interior angle:",
                "options": [
                    "90°",
                    "80°",
                    "100°",
                    "95°"
                ],
                "answer": 0,
                "hint": "Use Section 4.2 Angle Sum Property: all 4 angles always total 360°!",
                "explanation": "360° − (75° + 110° + 85°) = 360° − 270° = 90°.",
                "solution_steps": [
                    "Apply the Quadrilateral Angle Sum Theorem: ∠A + ∠B + ∠C + ∠D = 360°.",
                    "Add the three given angles: 75° + 110° + 85° = 270°.",
                    "Subtract from 360°: 360° − 270° = 90°."
                ]
            },
            {
                "question": "A quadrilateral's four interior angles are in the ratio 2 : 3 : 4 : 3. Find the largest interior angle:",
                "options": [
                    "120°   (since 12x = 360° → x = 30°; 4 × 30° = 120°)",
                    "90°",
                    "108°",
                    "135°"
                ],
                "answer": 0,
                "hint": "Set angles as 2x, 3x, 4x, 3x and solve 12x = 360°!",
                "explanation": "2x + 3x + 4x + 3x = 12x = 360° → x = 30°, so the largest angle 4x = 120°.",
                "solution_steps": [
                    "Express angles cleanly as 2x, 3x, 4x, and 3x.",
                    "Sum to 360°: 12x = 360° → x = 30°.",
                    "Compute the largest part: 4 × 30° = 120° (angles: 60°, 90°, 120°, 90°)."
                ]
            },
            {
                "question": "In rectangle PQRS, diagonals PR and QS intersect at center O. If OP = 6.5 cm, what is the full length of the OTHER diagonal QS?",
                "options": [
                    "13 cm   (diagonals are equal and bisect each other: PR = QS = 2 × 6.5 cm)",
                    "6.5 cm",
                    "19.5 cm",
                    "26 cm"
                ],
                "answer": 0,
                "hint": "Combine Deduction 1 (PR = QS) and Deduction 2 (O is the midpoint of PR)!",
                "explanation": "Since O bisects PR, PR = 2 × 6.5 = 13 cm; since rectangle diagonals are equal, QS = PR = 13 cm.",
                "solution_steps": [
                    "Use Deduction 2 (diagonals bisect each other): PR = 2 × OP = 2 × 6.5 = 13 cm.",
                    "Use Deduction 1 (rectangle diagonals are equal via SAS ΔADC ≅ ΔDAB): QS = PR.",
                    "Conclude QS = 13 cm."
                ]
            },
            {
                "question": "In rectangle ABCD, diagonals AC and BD meet at O with ∠OAB = 32°. Find ∠OBA and central obtuse ∠AOD:",
                "options": [
                    "∠OBA = 32°   and   ∠AOD = 64°   (since ΔAOB is isosceles: ∠AOB = 116°, linear pair ∠AOD = 64°)",
                    "∠OBA = 58°   and   ∠AOD = 116°",
                    "∠OBA = 32°   and   ∠AOD = 116°",
                    "∠OBA = 64°   and   ∠AOD = 58°"
                ],
                "answer": 0,
                "hint": "Remember OA = OB (equal bisecting diagonals make ΔAOB isosceles!), and ∠AOD is the exterior angle of ΔAOB!",
                "explanation": "OA = OB gives ∠OBA = ∠OAB = 32°; exterior angle ∠AOD = 32° + 32° = 64°.",
                "solution_steps": [
                    "Because diagonals are equal and bisect each other, OA = OB, making ΔAOB isosceles so ∠OBA = ∠OAB = 32°.",
                    "Compute ∠AOB = 180° − (32° + 32°) = 116°.",
                    "Use linear pair at O: ∠AOD = 180° − 116° = 64°."
                ]
            },
            {
                "question": "Why does Carpenter's Deduction 3 show that changing the central crossing angle between two equal bisecting strips ALWAYS keeps the outer boundary a rectangle?",
                "options": [
                    "Because equal diagonal halves (OA = OB = OC = OD) create 4 isosceles triangles whose base angles sum cleanly to 90° at every single corner!",
                    "Because strips bend into curved arcs",
                    "Because only 90° crossing creates a quadrilateral",
                    "Because equal strips force all 4 sides equal"
                ],
                "answer": 0,
                "hint": "Let central angle be θ and adjacent linear-pair angle be 180°−θ; compute corner sum (180−θ)/2 + θ/2!",
                "explanation": "At every pivot angle θ, base angles add to (180°−θ)/2 + θ/2 = 90°, locking all 4 outer vertices at exact right angles.",
                "solution_steps": [
                    "Equal bisecting diagonals imply OA = OB = OC = OD.",
                    "In isosceles ΔAOB and ΔAOD, corner ∠DAB = (180°−∠AOB)/2 + (180°−∠AOD)/2.",
                    "Since ∠AOB + ∠AOD = 180°, corner ∠DAB = 180° − 90° = 90° always!"
                ]
            },
            {
                "question": "Which statement accurately justifies why every Square is a Rectangle, yet NOT every Rectangle is a Square?",
                "options": [
                    "Every square has all four 90° angles (meeting rectangle definition), whereas an oblong 9 cm × 4 cm rectangle fails the 4-equal-sides square rule",
                    "A rectangle has unequal opposite sides",
                    "A square has only two 90° corners",
                    "Rectangles cannot have equal diagonals"
                ],
                "answer": 0,
                "hint": "Compare the required definitions: Rectangle = 4×90° angles; Square = 4×90° angles + 4 equal sides!",
                "explanation": "Squares satisfy all rectangle axioms plus equal adjacent edges, forming a strict subset inside Rectangles.",
                "solution_steps": [
                    "Check Square → Rectangle: 4 equal sides & four 90° angles satisfies four 90° angles (TRUE).",
                    "Check Rectangle → Square: 9 cm × 4 cm has four 90° angles yet 9 ≠ 4 (FALSE).",
                    "Confirm strict Venn subset relationship: Squares ⊂ Rectangles."
                ]
            },
            {
                "question": "In square MATH, diagonals MT and AH intersect at O. Find ∠MOT and ∠MHA cleanly using Deduction 5:",
                "options": [
                    "∠MOT = 90°   and   ∠MHA = 45°",
                    "∠MOT = 45°   and   ∠MHA = 90°",
                    "∠MOT = 60°   and   ∠MHA = 30°",
                    "∠MOT = 120°   and   ∠MHA = 45°"
                ],
                "answer": 0,
                "hint": "Square diagonals cross perpendicularly at O (90°) and bisect every 90° corner (45°)!",
                "explanation": "By SSS congruence (Deduction 5), center crossing ∠MOT = 90° and corner split ∠MHA = 90° ÷ 2 = 45°.",
                "solution_steps": [
                    "By SSS congruence around O, diagonals meet perpendicularly: ∠MOT = 90°.",
                    "In isosceles right triangle ΔAMH, MH = MA and ∠M = 90°.",
                    "Thus corner bisection yields ∠MHA = (180° − 90°)/2 = 45°."
                ]
            },
            {
                "question": "Can a simple quadrilateral ever possess interior angles measuring 90°, 90°, 90°, and 85°?",
                "options": [
                    "NO — 90 + 90 + 90 + 85 = 355° ≠ 360°, violating the Quadrilateral Angle Sum Theorem!",
                    "YES, if two sides are curved",
                    "YES, in any tilted rectangle",
                    "YES, because triangles sum to 175°"
                ],
                "answer": 0,
                "hint": "Add 90° + 90° + 90° + 85° and compare strictly with 360°!",
                "explanation": "Section 4.2 proves every quadrilateral must sum to exactly 360° (355° leaves an unclosed gap).",
                "solution_steps": [
                    "Compute the sum of proposed angles: 90° + 90° + 90° + 85° = 355°.",
                    "Recall Section 4.2 proves ANY quadrilateral's 4 interior angles sum strictly to 360°.",
                    "Since 355° ≠ 360°, having exactly three right angles is impossible."
                ]
            },
            {
                "question": "In Deduction 2, why do diagonals of a rectangle ABCD bisect each other via ΔAOB ≅ ΔCOD?",
                "options": [
                    "By AAS Congruence: alternate interior angles ∠OAB = ∠OCD, ∠OBA = ∠ODC (from AB ∥ CD) and equal opposite sides AB = CD",
                    "By assuming diagonals cross at 90° first",
                    "Because AO = BC always",
                    "Because triangles only need two equal sides"
                ],
                "answer": 0,
                "hint": "Parallel opposite sides AB ∥ CD give two pairs of equal alternate interior angles plus AB = CD!",
                "explanation": "AB ∥ CD establishes matching alternate angles along both diagonals plus AB = CD (AAS congruence → AO = CO, BO = DO).",
                "solution_steps": [
                    "Since AB ∥ CD, alternate interior angles match: ∠OAB = ∠OCD and ∠OBA = ∠ODC.",
                    "Since AB = CD (opposite sides of rectangle), AAS guarantees ΔAOB ≅ ΔCOD.",
                    "Corresponding sides confirm AO = CO and BO = DO (mutual bisection)."
                ]
            },
            {
                "question": "Which polygon fails to qualify as a valid quadrilateral by definition?",
                "options": [
                    "A 4-segment closed shape containing one curved side or a self-intersecting bowtie boundary",
                    "A square rotated 45° on a dot grid",
                    "A kite with two 5 cm edges and two 9 cm edges",
                    "A trapezium with 1 pair of parallel edges"
                ],
                "answer": 0,
                "hint": "Review the four straight-edge, non-crossing, closed 4-sided boundary requirements!",
                "explanation": "Curved edges or crossed bowtie segments break simple closed 4-sided polygon rules.",
                "solution_steps": [
                    "Check quadrilateral definition: 4 straight segments forming one closed simple boundary.",
                    "Rotating a square, kite, or trapezium preserves all straight closed edges.",
                    "Curved arcs or self-crossing bowties fail polygon rules."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Parallelograms Rhombus Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Parallelogram Angle/Side/Diagonal Deductions 6–8 & Rhombus Deductions 9–10",
        "questions": [
            {
                "question": "In parallelogram WXYZ, ∠W = (3x − 10)° and adjacent angle ∠X = (2x + 40)°. Solve for x and ∠Z:",
                "options": [
                    "x = 30°,   ∠Z = ∠X = 100°",
                    "x = 50°,   ∠Z = 140°",
                    "x = 20°,   ∠Z = 80°",
                    "x = 40°,   ∠Z = 120°"
                ],
                "answer": 0,
                "hint": "By Deduction 6, adjacent angles ∠W + ∠X = 180°, and opposite angle ∠Z equals ∠X!",
                "explanation": "(3x − 10) + (2x + 40) = 180 → 5x + 30 = 180 → 5x = 150 → x = 30; ∠Z = ∠X = 2(30)+40 = 100°.",
                "solution_steps": [
                    "Apply Deduction 6 (adjacent supplementary): (3x − 10) + (2x + 40) = 180.",
                    "Simplify cleanly: 5x + 30 = 180 → 5x = 150 → x = 30.",
                    "Calculate ∠X = 2(30) + 40 = 100°; by opposite angle equality, ∠Z = ∠X = 100°."
                ]
            },
            {
                "question": "In parallelogram PQRS, perimeter = 46 cm and side PQ = 14 cm. Find the lengths of QR, RS, and SP:",
                "options": [
                    "RS = 14 cm,   QR = SP = 9 cm",
                    "RS = 14 cm,   QR = SP = 18 cm",
                    "RS = 9 cm,   QR = SP = 14 cm",
                    "All four sides equal 11.5 cm"
                ],
                "answer": 0,
                "hint": "Use Deduction 7 (opposite sides equal: RS = 14 cm) and subtract 2×14 = 28 from perimeter 46!",
                "explanation": "Remaining sum QR + SP = 46 − 28 = 18 cm; since QR = SP, each = 9 cm.",
                "solution_steps": [
                    "By Deduction 7, opposite side RS = PQ = 14 cm.",
                    "Perimeter gives 14 + QR + 14 + SP = 46 → 2×QR = 18.",
                    "Therefore QR = SP = 9 cm."
                ]
            },
            {
                "question": "In parallelogram EASY with diagonals ES and AY meeting at O (Deduction 8), EO = 4y − 3, OS = 17, AO = 2z + 5, OY = 19. Find y and z:",
                "options": [
                    "y = 5   and   z = 7",
                    "y = 4   and   z = 6",
                    "y = 6   and   z = 8",
                    "y = 5   and   z = 12"
                ],
                "answer": 0,
                "hint": "Diagonals bisect each other cleanly: set 4y − 3 = 17 and 2z + 5 = 19!",
                "explanation": "4y = 20 → y = 5; 2z = 14 → z = 7.",
                "solution_steps": [
                    "Apply Deduction 8 (bisecting diagonals): EO = OS → 4y − 3 = 17 → 4y = 20 → y = 5.",
                    "Similarly AO = OY → 2z + 5 = 19 → 2z = 14 → z = 7.",
                    "Confirm solution pair: y = 5, z = 7."
                ]
            },
            {
                "question": "In rhombus GAME, diagonal GE makes ∠EGM = 28° with side GM. Find all four interior angles ∠G, ∠A, ∠M, ∠E:",
                "options": [
                    "∠G = ∠M = 56°,   ∠A = ∠E = 124°",
                    "∠G = ∠M = 28°,   ∠A = ∠E = 152°",
                    "∠G = ∠A = 56°,   ∠M = ∠E = 124°",
                    "∠G = ∠M = 62°,   ∠A = ∠E = 118°"
                ],
                "answer": 0,
                "hint": "Remember Deduction 9: diagonal GE BISECTS corner angle ∠G, so ∠G = 2 × 28°!",
                "explanation": "∠G = 2×28° = 56°; opposite ∠M = 56°; adjacent ∠A = ∠E = 180° − 56° = 124°.",
                "solution_steps": [
                    "By Deduction 9, rhombus diagonals bisect vertex angles: ∠G = 2 × 28° = 56°.",
                    "Opposite angles match: ∠M = ∠G = 56°.",
                    "Adjacent angles are supplementary: ∠A = ∠E = 180° − 56° = 124°."
                ]
            },
            {
                "question": "In rhombus ABCD, diagonals AC = 16 cm and BD = 12 cm intersect at O. Using Deduction 10 (90° bisectors), find the length of side AB:",
                "options": [
                    "10 cm   (right triangle ΔAOB with legs 8 cm and 6 cm → √(8² + 6²) = 10 cm!)",
                    "14 cm",
                    "20 cm",
                    "√28 cm"
                ],
                "answer": 0,
                "hint": "Split diagonals into halves at O (OA = 8 cm, OB = 6 cm) inside right triangle ΔAOB (∠AOB = 90°)!",
                "explanation": "Diagonals bisect at 90°, giving right triangle legs 8 cm and 6 cm; AB = √(64 + 36) = 10 cm.",
                "solution_steps": [
                    "Deduction 10 guarantees AO = 16/2 = 8 cm, BO = 12/2 = 6 cm, and ∠AOB = 90°.",
                    "Apply Pythagoras Theorem in ΔAOB: AB² = AO² + BO² = 8² + 6² = 64 + 36 = 100.",
                    "Take square root cleanly: AB = 10 cm (perimeter = 40 cm)."
                ]
            },
            {
                "question": "Which combination of traits places a quadrilateral right inside the intersection (Rectangle ∩ Rhombus) of Section 4.4's Venn diagram?",
                "options": [
                    "Four equal sides AND four 90° angles (a Square!)",
                    "Only opposite sides equal and 60°–120° angles",
                    "Only one pair of parallel opposite sides",
                    "Unequal adjacent edges and oblique 75° diagonals"
                ],
                "answer": 0,
                "hint": "Intersection means satisfying BOTH Rectangle (4 × 90°) AND Rhombus (4 equal sides)!",
                "explanation": "Combining 4 equal sides (Rhombus) with four 90° corners (Rectangle) uniquely defines a Square.",
                "solution_steps": [
                    "List Rectangle condition: four 90° interior angles.",
                    "List Rhombus condition: four equal sidelengths.",
                    "Verify Intersection (Square): satisfies both conditions simultaneously."
                ]
            },
            {
                "question": "Why does EVERY rhombus qualify as a parallelogram, whereas NOT every parallelogram is a rhombus?",
                "options": [
                    "Equal sides guarantee parallel opposite sides via Deduction 9, while a 10 cm × 4 cm parallelogram has unequal adjacent sides",
                    "Because rhombuses have four 90° corners",
                    "Because parallelograms have three sides",
                    "Because rhombus opposite angles add to 90°"
                ],
                "answer": 0,
                "hint": "Check a counterexample parallelogram whose adjacent sides differ (e.g., 10 cm vs 4 cm)!",
                "explanation": "4 equal sides imply parallel opposite pairs (every rhombus is a parallelogram), but unequal adjacent sides fail the rhombus test.",
                "solution_steps": [
                    "Deduction 9 proves SSS across a rhombus diagonal establishes parallel opposite sides.",
                    "Hence Rhombuses ⊂ Parallelograms.",
                    "Counterexample: a 10×4 parallelogram is NOT a rhombus because 10 ≠ 4."
                ]
            },
            {
                "question": "Which congruence rule proves Deduction 8 (diagonals of parallelogram EASY bisect each other: ΔAOE ≅ ΔYOS)?",
                "options": [
                    "ASA Congruence  (alternate angles ∠OEA = ∠OSY, equal opposite sides AE = SY, alternate angles ∠OAE = ∠OYS)",
                    "AAA Angle-only check",
                    "Assume diagonals bisect first",
                    "Right-angle only without parallel lines"
                ],
                "answer": 0,
                "hint": "Alternate interior angles along parallel opposite sides AE ∥ SY straddle equal sides AE = SY!",
                "explanation": "AE ∥ SY (definition) and AE = SY (Deduction 7) satisfy ASA congruence for ΔAOE ≅ ΔYOS.",
                "solution_steps": [
                    "Parallel sides AE ∥ SY yield equal alternate angles ∠OEA = ∠OSY and ∠OAE = ∠OYS.",
                    "Deduction 7 already proves opposite sides AE = SY.",
                    "By ASA, ΔAOE ≅ ΔYOS → AO = OY and EO = OS."
                ]
            },
            {
                "question": "In a step-by-step compass construction of a rhombus with side 6 cm and ∠A = 60°, after marking B (6 cm) and D (6 cm) on the angle rays, how do you find C?",
                "options": [
                    "Swing two 6 cm radius arcs centered at B and D; their intersection point C completes BC = CD = 6 cm!",
                    "Swing 3 cm arcs from A and B",
                    "Connect B to D directly as a square corner",
                    "Draw a 90° perpendicular at B"
                ],
                "answer": 0,
                "hint": "All 4 sides of a rhombus equal 6 cm, so C must sit 6 cm away from BOTH B and D!",
                "explanation": "Intersecting 6 cm arcs from B and D locates vertex C so AB = BC = CD = DA = 6 cm.",
                "solution_steps": [
                    "Set compass radius strictly to side length 6 cm.",
                    "Draw arcs of 6 cm centered at B and at D cleanly.",
                    "Mark intersection C so all 4 edges equal 6 cm."
                ]
            },
            {
                "question": "Which property holds TRUE for a Square, a Rectangle, a Rhombus, AND a general Parallelogram alike?",
                "options": [
                    "Diagonals bisect each other cleanly at center O",
                    "Diagonals are always equal in length",
                    "Diagonals always meet at 90°",
                    "All four interior angles equal 90°"
                ],
                "answer": 0,
                "hint": "Which property belongs to the PARENT family Parallelogram, and is inherited by EVERY child shape?",
                "explanation": "Because Square, Rectangle, and Rhombus are all Parallelograms, ALL four share mutually bisecting diagonals (plus equal opposite sides/angles).",
                "solution_steps": [
                    "Recall Venn hierarchy: Square, Rectangle, Rhombus ⊂ Parallelogram.",
                    "Check shared parent trait: Deduction 8 proves ALL parallelograms have mutually bisecting diagonals.",
                    "Reject equal diagonals (fails Rhombus/Parallelogram) and 90° crossing (fails Rectangle/Parallelogram)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Kites Trapeziums Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Geoboard Diagonals, Joined Triangles, Kites, Trapeziums & Isosceles Trapeziums",
        "questions": [
            {
                "question": "In kite ABCD with AB = BC = 7 cm and CD = DA = 11 cm, main diagonal BD bisects ∠B = 70° and ∠D = 40°. Find ∠A and ∠C:",
                "options": [
                    "∠A = ∠C = 125°   (sum = 360° − 70° − 40° = 250°; split equally: 250° ÷ 2 = 125°)",
                    "∠A = 70°,   ∠C = 40°",
                    "∠A = ∠C = 110°",
                    "∠A = 140°,   ∠C = 110°"
                ],
                "answer": 0,
                "hint": "Compute ∠A + ∠C = 360° − (70° + 40°) and remember wing angles ∠A = ∠C are equal!",
                "explanation": "250° remaining splits cleanly across symmetric wing angles: ∠A = ∠C = 125°.",
                "solution_steps": [
                    "Apply Quadrilateral Angle Sum: ∠A + ∠C = 360° − (70° + 40°) = 250°.",
                    "By SSS symmetry ΔABD ≅ ΔCBD, ∠A = ∠C.",
                    "Divide equally: 250° ÷ 2 = 125° each."
                ]
            },
            {
                "question": "In kite PQRS (PQ = QR and RS = SP), diagonals PR = 12 cm and QS = 15 cm cross at O. What are ∠POQ and PO cleanly?",
                "options": [
                    "∠POQ = 90°   and   PO = OR = 6 cm   (note QS is NOT bisected unless kite is a rhombus!)",
                    "∠POQ = 60°   and   PO = 12 cm",
                    "∠POQ = 90°   and   QO = OS = 7.5 cm",
                    "∠POQ = 45°   and   PO = 6 cm"
                ],
                "answer": 0,
                "hint": "Line of symmetry QS passes through unequal-pair tips Q and S, perpendicularly bisecting cross-bar PR = 12 cm!",
                "explanation": "Symmetry spine QS perpendicularly bisects PR at O: ∠POQ = 90° and PO = 12/2 = 6 cm.",
                "solution_steps": [
                    "Identify main symmetry diagonal QS connecting vertex Q (between equal PQ=QR) to S (between equal SP=SR).",
                    "Main diagonal QS intersects PR at exact 90° (∠POQ = 90°).",
                    "Cross-diagonal PR is bisected cleanly: PO = 12 ÷ 2 = 6 cm."
                ]
            },
            {
                "question": "In isosceles trapezium TUVW with TU ∥ VW and equal slanted legs TW = UV, if bottom base angle ∠W = 68°, find ∠V, ∠T, and ∠U:",
                "options": [
                    "∠V = 68°,   ∠T = 112°,   ∠U = 112°",
                    "∠V = 112°,   ∠T = 68°,   ∠U = 68°",
                    "∠V = 68°,   ∠T = 68°,   ∠U = 112°",
                    "∠V = 90°,   ∠T = 90°,   ∠U = 90°"
                ],
                "answer": 0,
                "hint": "Opposite equal legs give congruent base angles (∠V = ∠W), and co-interior leg pairs sum to 180°!",
                "explanation": "∠V = ∠W = 68°, and co-interior supplements give ∠T = ∠U = 180° − 68° = 112°.",
                "solution_steps": [
                    "Isosceles trapezium symmetry equates lower base angles: ∠V = ∠W = 68°.",
                    "Apply transversal supplement along leg TW: ∠T = 180° − 68° = 112°.",
                    "Symmetry gives ∠U = ∠T = 112° (check sum: 68+68+112+112 = 360°)."
                ]
            },
            {
                "question": "If a geoboard rubber band connects the tips of two UNEQUAL diagonals bisecting each other at an oblique angle of 55° (≠ 90°), which shape forms?",
                "options": [
                    "A non-rectangular, non-rhombus Parallelogram",
                    "A Rectangle",
                    "A Rhombus",
                    "A Square"
                ],
                "answer": 0,
                "hint": "Mutually bisecting diagonals guarantee a Parallelogram; unequal lengths rule out Rectangles/Squares, and 55° ≠ 90° rules out Rhombuses!",
                "explanation": "Only a general parallelogram has unequal diagonals bisecting each other at a non-right angle.",
                "solution_steps": [
                    "Check bisection: diagonals bisect each other → Parallelogram guaranteed.",
                    "Check equality: diagonals are UNEQUAL → neither Rectangle nor Square.",
                    "Check crossing angle: 55° ≠ 90° → not a Rhombus."
                ]
            },
            {
                "question": "Joining two identical ISOSCELES triangle cutouts (legs = 8 cm, base = 5 cm) along matching sides can produce which two quadrilaterals?",
                "options": [
                    "A Rhombus (joined along the 5 cm base) or a Kite (joined symmetrically along equal 8 cm legs)",
                    "Only a Square",
                    "Only a Triangle",
                    "An Open Hexagon"
                ],
                "answer": 0,
                "hint": "Review Section 4.5's triangle-cutout pairing rules cleanly!",
                "explanation": "Section 4.5 notes identical isosceles triangles form a Rhombus (joined along base) or a Kite depending on joined edges.",
                "solution_steps": [
                    "Join the two congruent isosceles triangles along their shared base (5 cm): all 4 outer sides equal leg 8 cm → Rhombus!",
                    "Join equal edges differently (matching adjacent equal legs 8 cm alongside bases 5 cm) → Kite!",
                    "Matches Section 4.5 directly: Isosceles pair → Rhombus or Kite."
                ]
            },
            {
                "question": "Wait—look carefully at trapezium KLMN with KL ∥ NM. Can BOTH ∠K and ∠N equal 90° simultaneously?",
                "options": [
                    "YES — a right-angled trapezium has one perpendicular leg (90° + 90° = 180° along leg KN), while the other leg slopes obliquely!",
                    "NO — any 90° angle forces all 4 corners to be 90°",
                    "YES, and all 4 angles must be 60°",
                    "NO — trapeziums cannot contain right angles"
                ],
                "answer": 0,
                "hint": "Verify ∠K + ∠N = 90° + 90° = 180° along leg KN while ∠L = 60°, ∠M = 120°!",
                "explanation": "Having two consecutive 90° angles along one perpendicular leg simply forms a valid Right Trapezium.",
                "solution_steps": [
                    "Check leg KN between parallel bases KL ∥ NM: ∠K + ∠N = 90° + 90° = 180° (satisfied!).",
                    "Set remaining leg LM to slant: e.g., ∠L = 120°, ∠M = 60° (sums to 180° too!).",
                    "Total sum = 90 + 90 + 120 + 60 = 360° → valid Right Trapezium!"
                ]
            },
            {
                "question": "Using a geoboard, which two diagonal adjustments transform a constructed RECTANGLE cleanly into a SQUARE?",
                "options": [
                    "Keep both bisecting diagonals EQUAL in length while rotating their crossing angle from oblique to exact 90°!",
                    "Keep crossing angle oblique at 60° while making one diagonal twice as long",
                    "Stop bisecting both diagonals",
                    "Delete one diagonal completely"
                ],
                "answer": 0,
                "hint": "Rectangles already have EQUAL bisecting diagonals; what single extra diagonal condition turns Rectangle → Square?",
                "explanation": "Making equal bisecting diagonals cross perpendicularly (at 90°) produces a Square.",
                "solution_steps": [
                    "Inspect Rectangle diagonals: equal and mutually bisecting (angle ≠ 90°).",
                    "Adjust diagonal pivot angle strictly to 90° while keeping equal lengths.",
                    "Resulting 4 right triangles at center O force all 4 outer sides equal → Square!"
                ]
            },
            {
                "question": "Why does NCERT Section 4.6 define a TRAPEZIUM as having 'at least one pair' of parallel sides rather than 'exactly one pair'?",
                "options": [
                    "Because inclusive definitions place Parallelograms cleanly as special Trapeziums (just as Squares are special Rectangles)!",
                    "Because trapeziums have zero parallel sides",
                    "To exclude isosceles trapeziums",
                    "Because every triangle is a trapezium"
                ],
                "answer": 0,
                "hint": "Compare inclusive math taxonomy (Parallelogram ⊂ Trapezium) vs exclusive separation!",
                "explanation": "Defining trapeziums by 'at least one parallel pair' creates a clean subset chain: Squares ⊂ Rectangles/Rhombuses ⊂ Parallelograms ⊂ Trapeziums.",
                "solution_steps": [
                    "Notice every Parallelogram has TWO pairs of parallel sides.",
                    "Having 2 parallel pairs automatically satisfies having 'at least 1' parallel pair.",
                    "Thus Parallelograms sit cleanly inside Trapeziums in NCERT's hierarchy."
                ]
            },
            {
                "question": "In kite WXYZ (WX = XY and YZ = ZW), why does cross-diagonal XZ NOT bisect main diagonal WY in a general non-rhombus kite?",
                "options": [
                    "Because top crown WX ≠ bottom tail ZW, making the top triangle XWO shorter or taller than bottom triangle XZO along spine WY!",
                    "Because kites have no cross-diagonals",
                    "Because diagonals never cross inside a kite",
                    "Because ∠W = ∠Z = 90° always"
                ],
                "answer": 0,
                "hint": "Think of a classic flying kite with a short upper nose and a long lower tail!",
                "explanation": "Unequal distinct edge pairs (WX ≠ ZW) create unequal vertical segments along main axis WY.",
                "solution_steps": [
                    "Draw a standard kite: short top edges WX = XY, long bottom edges YZ = ZW.",
                    "Cross-diagonal XZ connects wing tips at unequal distances from W and Y.",
                    "Only when WX = ZW (turning the kite into a rhombus!) does XZ also bisect WY."
                ]
            },
            {
                "question": "Cut a scalene paper triangle twice identically and place both cutouts with the SAME edge shared yet one triangle rotated 180° around that edge's midpoint. What forms?",
                "options": [
                    "A Parallelogram  (rotating 180° maps opposite edges parallel and equal!)",
                    "A Kite",
                    "A Square",
                    "A Regular Pentagon"
                ],
                "answer": 0,
                "hint": "A 180° half-turn places alternate interior angles equal along the shared diagonal seam!",
                "explanation": "180° rotation around an edge midpoint places equal lengths on opposite parallel sides, guaranteeing a Parallelogram.",
                "solution_steps": [
                    "Start with two congruent scalene triangles sharing longest side c.",
                    "Rotate one triangle 180° around the midpoint of side c.",
                    "Opposite sides match cleanly (a = a, b = b) with equal alternate angles → Parallelogram!"
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Quiz",
        "subtitle": "Challenge Arena 4 (10 MCQs): Square-in-a-Square Proofs, True/False Logic, Venn Hierarchy & Which Quad Puzzles",
        "questions": [
            {
                "question": "Square ABCD has side 7 cm. Points P, Q, R, S sit along AB, BC, CD, DA at AP = BQ = CR = DS = 3 cm (leaving PB = QC = RD = SA = 4 cm). Find the SIDE LENGTH and AREA of inner square PQRS:",
                "options": [
                    "Side = 5 cm,   Area = 25 cm²   (via 3–4–5 Pythagoras right triangles!)",
                    "Side = 7 cm,   Area = 49 cm²",
                    "Side = 4 cm,   Area = 16 cm²",
                    "Side = 12 cm,   Area = 25 cm²"
                ],
                "answer": 0,
                "hint": "Check right triangle ΔPBQ with legs PB = 4 cm and BQ = 3 cm!",
                "explanation": "Each corner right triangle has legs 3 cm and 4 cm → hypotenuse PQ = √(3² + 4²) = 5 cm, so inner square area = 5² = 25 cm².",
                "solution_steps": [
                    "Inspect corner right triangle ΔPBQ: PB = 7 − 3 = 4 cm, BQ = 3 cm, ∠B = 90°.",
                    "Compute hypotenuse PQ = √(4² + 3²) = √(16 + 9) = 5 cm.",
                    "Since Section 4.6 proves PQRS is a square, Area(PQRS) = 5² = 25 cm²."
                ]
            },
            {
                "question": "A rectangular sheet of paper is folded ONCE along one diagonal crease, trimmed cleanly so symmetric wings overlap equally, or folded twice perpendicularly and cut diagonally across the folded center corner. Which symmetry holds?",
                "options": [
                    "Two perpendicular fold creases act as perpendicular bisecting diagonals, guaranteeing the unfolded shape is ALWAYS a Rhombus (or Square at 45° cut)!",
                    "One straight cut across two perpendicular folds always unfolds into a Trapezium",
                    "Paper folds can never produce equal side lengths",
                    "All unfolded shapes become circles"
                ],
                "answer": 0,
                "hint": "Think which quadrilateral is defined by perpendicular bisecting diagonals matching two orthogonal paper folds!",
                "explanation": "Every point reflected across two orthogonal axes keeps all four outer hypotenuse cuts equal in length = a Rhombus.",
                "solution_steps": [
                    "Fold once vertically, then fold once horizontally at 90° (4 layers total).",
                    "Make 1 straight slanted corner snip connecting both folded axes.",
                    "Unfolding reflects that hypotenuse across 90° axes into 4 congruent edges → Rhombus!"
                ]
            },
            {
                "question": "Evaluate ALL THREE True/False statements across NCERT Chapter 4's hierarchy:\n(i) Every square is a kite.   (ii) Every kite is a rhombus.   (iii) Every rectangle is a trapezium.",
                "options": [
                    "(i) TRUE,   (ii) FALSE,   (iii) TRUE",
                    "(i) TRUE,   (ii) TRUE,   (iii) FALSE",
                    "(i) FALSE,   (ii) FALSE,   (iii) TRUE",
                    "(i) TRUE,   (ii) FALSE,   (iii) FALSE"
                ],
                "answer": 0,
                "hint": "Check: square has equal adjacent pairs (TRUE); kite 5,5,9,9 ≠ rhombus (FALSE); rectangle has 2 ≥ 1 parallel pairs (TRUE)!",
                "explanation": "(i) Square has equal adjacent sides → kite (TRUE); (ii) 5-5-9-9 kite isn't equilateral (FALSE); (iii) rectangle has ≥1 parallel pair (TRUE).",
                "solution_steps": [
                    "(i) Square (a,a,a,a) satisfies equal adjacent pairs (a=a and a=a) → TRUE.",
                    "(ii) Kite (5,5,9,9) has unequal opposite sides → NOT a rhombus → FALSE.",
                    "(iii) Rectangle has 2 parallel pairs (≥ 1 required by trapezium) → TRUE."
                ]
            },
            {
                "question": "A mystery quadrilateral has:\n• Diagonals NOT equal in length\n• Diagonals intersecting at EXACT 90°\n• BOTH diagonals bisecting each other.\nWhich quadrilateral am I?",
                "options": [
                    "A non-square Rhombus",
                    "A Rectangle",
                    "A Square",
                    "An Isosceles Trapezium"
                ],
                "answer": 0,
                "hint": "Mutual bisection + 90° crossing narrows strictly to Rhombus vs Square; UNEQUAL diagonals eliminates Square!",
                "explanation": "Perpendicular mutual bisectors with unequal lengths uniquely identify a non-square Rhombus.",
                "solution_steps": [
                    "Mutual bisection → must be a Parallelogram.",
                    "90° crossing narrows strictly to Rhombus or Square.",
                    "Unequal diagonal lengths rule out Square → leaves non-square Rhombus."
                ]
            },
            {
                "question": "A mystery quadrilateral has:\n• NO pair of parallel opposite sides\n• Diagonals crossing at 90°\n• ONLY ONE diagonal gets bisected.\nWhich quadrilateral am I?",
                "options": [
                    "A non-rhombus Kite",
                    "A Trapezium",
                    "A Rhombus",
                    "A Rectangle"
                ],
                "answer": 0,
                "hint": "In which family does ONLY the symmetry diagonal bisect the cross-diagonal at 90° without parallel edges?",
                "explanation": "Only a non-rhombus Kite features perpendicular diagonals where strictly one diagonal bisects the other.",
                "solution_steps": [
                    "Zero parallel opposite sides rules out Parallelograms and Trapeziums.",
                    "90° diagonals with single-axis bisection matches Section 4.6 Kite proof.",
                    "Confirm non-rhombus Kite."
                ]
            },
            {
                "question": "In isosceles trapezium ABCD (AB ∥ CD, non-parallel AD = BC), diagonals AC and BD ALWAYS satisfy which property?",
                "options": [
                    "Diagonals AC and BD are EQUAL in length (via SAS congruence ΔADC ≅ ΔBCD!), though they do NOT bisect each other!",
                    "Diagonals bisect each other cleanly at center O",
                    "Diagonals must cross at 90° always",
                    "One diagonal is double the other"
                ],
                "answer": 0,
                "hint": "Compare ΔADC and ΔBCD: AD = BC, ∠D = ∠C (base angles equal!), and DC = CD shared!",
                "explanation": "SAS proves ΔADC ≅ ΔBCD, guaranteeing AC = BD (equal diagonals) while unequal bases AB ≠ CD prevent bisection.",
                "solution_steps": [
                    "Notice AD = BC and equal base angles ∠ADC = ∠BCD (Section 4.6 Isosceles Trapezium).",
                    "Common side DC gives SAS congruence: ΔADC ≅ ΔBCD → AC = BD.",
                    "Note unequal bases AB ≠ CD make upper/lower diagonal segments unequal (no mutual bisection)."
                ]
            },
            {
                "question": "In quadrilateral PQRS, ∠P = 2x, ∠Q = 3x, ∠R = 5x, and exterior angle adjacent to ∠S is 60° (so interior ∠S = 120°). Find x and ∠R:",
                "options": [
                    "x = 24°,   ∠R = 120°   (10x + 120° = 360° → 10x = 240° → x = 24°)",
                    "x = 30°,   ∠R = 150°",
                    "x = 18°,   ∠R = 90°",
                    "x = 20°,   ∠R = 100°"
                ],
                "answer": 0,
                "hint": "Subtract 120° from 360° first, then divide 240° across 2x + 3x + 5x = 10x!",
                "explanation": "10x + 120° = 360° → 10x = 240° → x = 24°, making ∠R = 5 × 24° = 120°.",
                "solution_steps": [
                    "Find interior ∠S = 180° − 60° = 120°.",
                    "Set total sum 2x + 3x + 5x + 120° = 360° → 10x = 240° → x = 24°.",
                    "Compute ∠R = 5(24°) = 120°."
                ]
            },
            {
                "question": "Join two identical 3-4-5 cm right triangles along their shared 5 cm hypotenuse in mirror orientation. Which quadrilateral forms?",
                "options": [
                    "A Kite  (with adjacent pairs 3 cm = 3 cm and 4 cm = 4 cm, and right angles ∠B = ∠D = 90°!)",
                    "A Rhombus with four 5 cm sides",
                    "A Trapezium",
                    "A Parallelogram with unequal opposite sides"
                ],
                "answer": 0,
                "hint": "Mirroring across the 5 cm hypotenuse matches the 3 cm legs adjacent at one tip and 4 cm legs adjacent at the other tip!",
                "explanation": "Adjacent pairs (3,3) and (4,4) form a Right Kite (whereas rotating 180° around the midpoint would form a 3×4 Rectangle!).",
                "solution_steps": [
                    "Place both 3–4–5 right triangles mirror-symmetrically along shared 5 cm hypotenuse.",
                    "Equal 3 cm edges meet at one vertex; equal 4 cm edges meet at the opposite vertex.",
                    "Two distinct pairs of equal adjacent sides (3=3, 4=4) uniquely form a Kite!"
                ]
            },
            {
                "question": "In parallelogram ABCD, perpendicular heights dropped from B or diagonal bisectors reveal: can ONE parallelogram EVER have diagonal lengths 10 cm & 10 cm AND meet at 90° without being a square?",
                "options": [
                    "NO — equal bisecting diagonals force a Rectangle, and 90° crossing forces a Rhombus, so BOTH together ALWAYS force an exact Square!",
                    "YES, any slanted parallelogram can have equal perpendicular diagonals",
                    "YES, if side AB ≠ BC",
                    "NO, squares never have equal diagonals"
                ],
                "answer": 0,
                "hint": "Evaluate 4 congruent right triangles around center O when diagonals are 10 cm (halves 5 cm) crossing at 90°!",
                "explanation": "Equal halves (5 cm & 5 cm) at 90° create four congruent 5–5–√50 isosceles right triangles → 4 equal sides & four 90° angles = Square.",
                "solution_steps": [
                    "Halves equal 5 cm each at center O with 90° intersection angles.",
                    "All 4 outer corners form 45°-45°-90° triangles → every corner angle = 45° + 45° = 90°.",
                    "All 4 sides equal 5√2 cm → uniquely a Square!"
                ]
            },
            {
                "question": "Which grand takeaway consolidates ALL of Chapter 4: Quadrilaterals?",
                "options": [
                    "Every quadrilateral sums to 360° interior angles; adding parallel sides, equal edges, 90° corners, and diagonal symmetry builds the unified hierarchy from Trapeziums and Kites up to Squares!",
                    "Rectangles and Rhombuses never intersect in a Square",
                    "Quadrilateral angle sums change from 360° in slanted parallelograms",
                    "Only squares have bisecting diagonals"
                ],
                "answer": 0,
                "hint": "Check the unified taxonomy connecting all 6 families cleanly via sides, angles, and diagonals!",
                "explanation": "Angle sum 360° holds universally; diagonal symmetry and side/angle rules organize Trapeziums, Kites, Parallelograms, Rectangles, Rhombuses, and Squares.",
                "solution_steps": [
                    "Confirm universal invariant: sum of interior angles = 360° (two triangles).",
                    "Review diagonal signatures: bisect (Parallelogram), +equal (Rectangle), +90° (Rhombus), +both (Square), 1-axis 90° bisect (Kite).",
                    "Confirm hierarchy: Squares = Rectangles ∩ Rhombuses ⊂ Parallelograms ⊂ Trapeziums."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch4 Class 8 Maths Part 3.")
    total_q = 0
    for s in slides_part3:
        twc = len(s["title"].split())
        assert 1 <= twc <= 3, f"Slide {s['id']} title {s['title']!r} not 1-3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} needs 10 questions"
        for idx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4
            assert len(q["solution_steps"]) == 3
            assert "hint" in q and q["hint"]
            total_q += 1
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Questions: {len(s['questions'])}")
    assert total_q == 40
    print("All 40 exercise & challenge questions verified successfully!")

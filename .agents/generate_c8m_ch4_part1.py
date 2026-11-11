#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 4: Quadrilaterals
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 4 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "What Are Quadrilaterals",
        "subtitle": "Introduction: Latin Etymology ('quadri' + 'latus') & Identifying Valid Closed 4-Sided Polygons",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Four: Quadrilaterals! Look everywhere around your entire everyday environment—blackboards, notebooks, window panes, tiled floors, flying outdoor kites, and roadside traffic signs all share one classic geometric design architecture: four straight boundaries enclosing flat space cleanly! "
            "Learn the exact Latin origin of the word QUADRILATERAL right away! 'Quadri' means FOUR, and 'latus' means SIDE! Together, a quadrilateral simply defines ANY closed two-dimensional flat polygon built strictly from FOUR straight line segments meeting cleanly end to end at FOUR distinct corner vertices! "
            "Test every boundary rule sharply so you never confuse shapes anywhere! Check four essential conditions for EVERY valid quadrilateral: First, it must stay completely CLOSED with zero open gaps anywhere! Second, EVERY boundary edge must be a STRAIGHT line segment—any curved arc disqualifies a shape immediately! Third, it must contain EXACTLY FOUR straight edges and four distinct corner vertices (unlike triangles with three or pentagons with five)! Fourth, non-adjacent opposite sides must never cross awkwardly through one another inside simple plane school geometry! Mastering those crisp visual structural definitions unlocks rectangles, squares, parallelograms, rhombuses, symmetric kites, and trapeziums effortlessly across EVERY geometry theorem and problem inside this entire chapter!"
        ),
        "checkpoints": [
            {
                "question": "From which two Latin root words does the mathematical term 'quadrilateral' come, and what do they mean?",
                "options": [
                    "quadri (four) and latus (side)",
                    "quadra (right angle) and lateral (circle)",
                    "quattuor (triangle) and linea (curve)",
                    "quadri (diagonal) and poly (many)"
                ],
                "answer": 0,
                "hint": "Look at 'quad-' (as in quarter/quadruple) paired with 'latus' (side)!",
                "explanation": "Latin quadri means four and latus means side, naming every closed four-sided straight polygon."
            },
            {
                "question": "Which shape MUST be rejected from the family of simple quadrilaterals?",
                "options": [
                    "A 4-segment boundary where one side is a curved arc or two corners remain disconnected",
                    "A tilted roof truss with 4 unequal straight sides",
                    "A diamond-shaped tile rotated 45 degrees",
                    "A trapezoid table top with 4 straight edges"
                ],
                "answer": 0,
                "hint": "Every quadrilateral requires 4 straight segments forming one closed loop!",
                "explanation": "Curved edges or open gaps violate the definition of a closed four-sided straight polygon."
            }
        ]
    },
    {
        "id": 2,
        "title": "Rectangles And Properties",
        "subtitle": "Section 4.1: Definition (Four 90° Angles, Equal Opposite Sides) & Deduction 4 Proof",
        "speech": (
            "Enter Section Four Point One: Rectangles and Squares! Picture building a crisp wooden picture frame or rectangular tabletop! How does geometry formally define a RECTANGLE? A rectangle is ANY quadrilateral whose FOUR interior corner angles each equal an exact RIGHT ANGLE of NINETY DEGREES! "
            "Inspect Deduction Four cleanly right away: if a closed four-sided shape ALREADY has four ninety-degree corners, why MUST its opposite sides automatically become parallel AND equal in length? Test consecutive corners angle A and angle B: since angle A plus angle B equals ninety plus ninety equals ONE HUNDRED EIGHTY DEGREES, adjacent sides meet perpendicularly, forcing top and bottom edges to remain perfectly PARALLEL without ever diverging or converging! Identical perpendicular distance locks opposite sides to EXACT EQUAL LENGTH! "
            "Check all five gold-standard rectangle geometry properties together cleanly right now: First, opposite sides are ALWAYS EQUAL in exact length; second, opposite sides ALWAYS run PARALLEL without touching; third, every single interior corner angle measures an exact NINETY DEGREES right angle; fourth, adjacent boundary sides meet cleanly perpendicularly; and fifth, both connecting corner-to-corner straight diagonals hold extraordinary hidden geometric symmetry waiting inside our Carpenter's wooden-strip construction problem coming up on the very next slide!"
        ),
        "checkpoints": [
            {
                "question": "According to Deduction 4, if a four-sided wooden frame has ALL FOUR corners equal to 90°, what automatically follows about its opposite sides?",
                "options": [
                    "Opposite sides are automatically parallel AND equal in length",
                    "All four sides must be equal like a square",
                    "Opposite sides can have completely different lengths",
                    "Diagonals cannot intersect inside the shape"
                ],
                "answer": 0,
                "hint": "Consecutive 90° + 90° = 180° forces opposite edges parallel at fixed constant separation!",
                "explanation": "Four 90° angles create consecutive 180° supplementary pairs, forcing both pairs of opposite sides parallel and equal."
            },
            {
                "question": "Which property does a general rectangle NOT have to satisfy?",
                "options": [
                    "All four sides having the exact same length (only opposite sides must match!)",
                    "Four 90° interior angles",
                    "Equal-length diagonals bisecting each other",
                    "Two pairs of parallel opposite sides"
                ],
                "answer": 0,
                "hint": "Think of a 10 cm × 4 cm rectangular door — all corners are 90°, yet width ≠ height!",
                "explanation": "A general rectangle guarantees equal opposite sides; forcing all four sides equal turns it into a special square."
            }
        ]
    },
    {
        "id": 3,
        "title": "Rectangle Diagonal Proofs",
        "subtitle": "Section 4.1 Carpenter's Problem: Deductions 1, 2 & 3 (ΔADC ≅ ΔDAB, Bisecting Equal Diagonals)",
        "speech": (
            "Now solve Section Four Point One's famous CARPENTER'S PROBLEM using wooden diagonal strips and pins! Imagine two identical wooden sticks hinged right through their exact MIDPOINTS at point O! As you widen or narrow the crossing angle between both equal sticks, look carefully at the outer four tips A, B, C, and D! What quadrilateral ALWAYS forms around those four hinged endpoints? AN EXACT RECTANGLE EVERY SINGLE TIME! "
            "Prove both halves rigorously using Deductions One, Two, and Three! First, Deduction One: inside any rectangle ABCD, compare right triangles ADC and DAB cleanly! Side AD stays shared between both triangles; angle ADC equals angle DAB equals NINETY DEGREES; and opposite sides DC equals AB! By SAS triangle congruence (triangle ADC congruent to triangle DAB), diagonal AC ALWAYS EQUALS diagonal BD! "
            "Second, Deduction Two: watch triangles AOB and COD carefully where diagonals cross at center O! Because opposite sides AB equals CD and alternate parallel-line interior angles match cleanly, AAS congruence (triangle AOB congruent to triangle COD) proves AO = OC and BO = OD—the diagonals ALWAYS BISECT each other! Deduction Three confirms altering central pivot angle O reshapes slim versus wide rectangles smoothly while locking every outer corner at ninety degrees!"
        ),
        "checkpoints": [
            {
                "question": "In Deduction 1, which congruence test proves rectangle diagonals AC and BD are equal via ΔADC ≅ ΔDAB?",
                "options": [
                    "SAS Congruence  (AD = DA shared, ∠ADC = ∠DAB = 90°, DC = AB)",
                    "AAA Similarity only",
                    "SSA without right angles",
                    "Three unequal sides"
                ],
                "answer": 0,
                "hint": "Look at the shared base AD, the 90° angles at A and D, and opposite edges DC = AB!",
                "explanation": "Side AD (common), Angle 90° (at D and A), and Side DC = AB satisfy SAS, proving AC = BD."
            },
            {
                "question": "Two wooden strips of length 14 cm each are pinned together through their exact midpoints (7 cm each half). Joining all four endpoints ALWAYS produces which shape regardless of pivot angle (between 0° and 180°)?",
                "options": [
                    "A rectangle  (because diagonals are equal AND bisect each other!)",
                    "A trapezoid with unequal sides",
                    "A circle",
                    "A triangle"
                ],
                "answer": 0,
                "hint": "Compare Deduction 3 (Carpenter's strip hinge!): equal diagonals bisecting at O guarantee four 90° corners!",
                "explanation": "Equal bisecting diagonals uniquely characterize rectangles; only when the pivot angle hits 90° does the rectangle become a square."
            }
        ]
    },
    {
        "id": 4,
        "title": "Special Rectangle Squares",
        "subtitle": "Section 4.1: Squares, Subset Venn Diagrams & Deduction 5 (90° Diagonal Bisection + 45° Corner Split)",
        "speech": (
            "Now meet the crown jewel of rectangles inside Section Four Point One: THE SQUARE! How do we define a square cleanly? A square is a SPECIAL RECTANGLE whose FOUR SIDES ALL HAVE EXACTLY EQUAL LENGTH alongside four ninety-degree interior angles! "
            "Draw a crisp VENN DIAGRAM in your mind immediately: draw a wide oval labeled RECTANGLES, and place a smaller circle labeled SQUARES completely INSIDE that Rectangles oval! Why? Because EVERY square inherits every single rectangle law automatically—opposite sides parallel, four ninety-degree corners, and equal bisecting diagonals—making every square a rectangle! Conversely, an oblong 8-by-5 rectangle sits outside the Squares circle, proving NOT every rectangle is a square! "
            "Now unlock Deduction Five cleanly using SSS triangle congruence! Because all four outer sides equal one fixed value in square ABCD, compare triangles AOB and COB sharing side BO: AB = BC, AO = OC (diagonal midpoint), and BO = BO! By SSS congruence, central angles AOB and COB are completely equal along straight line AC, forcing EACH center angle to measure exact NINETY DEGREES! Plus base angles of isosceles right triangle ABC measure exact FORTY FIVE DEGREES—proving square diagonals bisect EVERY corner cleanly into two exact 45-degree halves!"
        ),
        "checkpoints": [
            {
                "question": "In a Venn diagram relating Rectangles and Squares, which statement is ALWAYS TRUE?",
                "options": [
                    "The set of Squares sits completely INSIDE the set of Rectangles (every square is a rectangle, not vice versa)",
                    "Squares and Rectangles are completely disjoint circles",
                    "Every rectangle is automatically a square",
                    "A square has only two 90° angles"
                ],
                "answer": 0,
                "hint": "Does a square meet every requirement of a rectangle (4 right angles)? Does a 3×7 rectangle meet every requirement of a square?",
                "explanation": "A square has four 90° angles (so it IS a rectangle) plus 4 equal sides (extra condition)."
            },
            {
                "question": "According to Deduction 5, at what exact angle do a square's diagonals cross at center O, and into what angles do they split each 90° corner?",
                "options": [
                    "Center intersection = 90° (perpendicular bisectors);   each corner splits into 45° and 45°",
                    "Center = 60°;   corners split into 30° and 60°",
                    "Center = 120°;   corners split into 40° and 50°",
                    "Diagonals never intersect inside a square"
                ],
                "answer": 0,
                "hint": "SSS proves adjacent center angles equal along a 180° straight line (180° ÷ 2), and equal legs make 45°-45°-90° right triangles!",
                "explanation": "Square diagonals are equal perpendicular bisectors (90° at O) that bisect each 90° corner into two 45° angles."
            }
        ]
    },
    {
        "id": 5,
        "title": "Quadrilateral Angle Sum",
        "subtitle": "Section 4.2: Triangulation Proof (ΔSEM + ΔSOM = 360°) & Impossibility of Three Exact Right Angles",
        "speech": (
            "Enter Section Four Point Two: Angles in a Quadrilateral! Question of the day: what MUST the four interior corner angles of ANY quadrilateral—even a lopsided jagged tent shape—ALWAYS add up to? Let us PROVE it permanently in three clean steps! "
            "Sketch ANY convex quadrilateral S-E-M-O and connect opposite corners S and M with ONE crisp diagonal line segment SM! Look what instantly appears inside: diagonal SM slices quadrilateral SEMO cleanly into TWO TRIANGLES—triangle SEM and triangle SOM! Notice every corner angle inside SEMO combines either single triangle corners at E and O, or two split triangle corners joined smoothly at S and M! "
            "Recall triangle angle-sum theorem: interior angles inside triangle SEM sum to exact ONE HUNDRED EIGHTY DEGREES, and interior angles inside triangle SOM ALSO sum to exact ONE HUNDRED EIGHTY DEGREES! Adding all six angles gives 180 + 180 = THREE HUNDRED SIXTY DEGREES ALWAYS! "
            "Spot one super-clever proof deduction immediately: CAN ANY quadrilateral have EXACTLY THREE right angles (90°, 90°, 90°) and one non-90° fourth angle? IMPOSSIBLE! Check arithmetic cleanly: 360° minus (90° + 90° + 90°) equals EXACT NINETY DEGREES—forcing the fourth angle to become a fourth right angle (rectangle) automatically!"
        ),
        "checkpoints": [
            {
                "question": "How does drawing one diagonal across ANY quadrilateral SEMO (splitting it into ΔSEM and ΔSOM) prove its interior angle sum equals 360°?",
                "options": [
                    "Because both triangles sum to 180° each, and adding all six triangle angles equals all four quadrilateral angles: 180° + 180° = 360°!",
                    "Because every corner angle measures 90°",
                    "Because diagonals divide into four 90° squares",
                    "Because external angles always equal 180°"
                ],
                "answer": 0,
                "hint": "Add the 180° interior angle sum of ΔSEM and the 180° sum of ΔSOM!",
                "explanation": "Triangulating any quadrilateral produces 2 triangles: 2 × 180° = 360°."
            },
            {
                "question": "Why is it mathematically IMPOSSIBLE for a quadrilateral to have EXACTLY three 90° angles (with a fourth angle ≠ 90°)?",
                "options": [
                    "Because the fourth angle equals 360° − (90° + 90° + 90°) = 90°, forcing all FOUR corners to be right angles!",
                    "Because 3 × 90° already exceeds 360°",
                    "Because quadrilaterals can only have two 90° angles",
                    "Because triangles sum to 360°"
                ],
                "answer": 0,
                "hint": "Subtract three right angles (270°) from total quadrilateral sum 360°!",
                "explanation": "If 3 angles are 90° each, the 4th angle is forced to be 360° − 270° = 90° (making all 4 right angles)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Parallel Opposite Sides",
        "subtitle": "Section 4.3: Parallelograms Definition, Set-Square/Compass Construction & Venn Hierarchy",
        "speech": (
            "Now unlock Section Four Point Three: More Quadrilaterals with Parallel Opposite Sides! Take an ordinary rectangle frame and gently tilt or push its top corner sideways until its angles lean cleanly at 60 degrees and 120 degrees while keeping BOTH opposite pairs completely parallel! What shape did you just create? A PARALLELOGRAM! "
            "Learn the exact definition sharply: a PARALLELOGRAM is ANY quadrilateral containing TWO PAIRS OF PARALLEL OPPOSITE SIDES! Look at your growing Venn family hierarchy right now: draw a huge outer region labeled PARALLELOGRAMS! Notice Rectangles have BOTH pairs of opposite sides parallel, so ALL RECTANGLES sit neatly INSIDE Parallelograms! And since ALL Squares sit inside Rectangles, EVERY square is automatically BOTH a rectangle AND a parallelogram! Yet slanted 60°-120° parallelograms sit outside Rectangles! "
            "Construct a clean parallelogram manually using ruler, set-square, or geometric compass step by step: First draw straight base AB and mark desired acute or obtuse corner angle A along side AD; second use sliding set-squares (or copy parallel distance and swing equal compass arcs AD = BC alongside AB = DC) to lock fourth corner intersection point C cleanly—producing crisp parallel boundary rails completely ready for Deductions Six, Seven, and Eight!"
        ),
        "checkpoints": [
            {
                "question": "Which Venn hierarchy containment chain holds 100% TRUE for parallel-sided quadrilaterals?",
                "options": [
                    "Squares ⊂ Rectangles ⊂ Parallelograms",
                    "Parallelograms ⊂ Rectangles ⊂ Squares",
                    "Rectangles ⊂ Squares ⊂ Parallelograms",
                    "Squares and Parallelograms never overlap"
                ],
                "answer": 0,
                "hint": "Every square has four 90° angles (is a rectangle); every rectangle has two pairs of parallel sides (is a parallelogram)!",
                "explanation": "Squares sit inside Rectangles, which sit inside Parallelograms."
            },
            {
                "question": "How do you locate the fourth vertex C cleanly with a compass after drawing adjacent sides AB and AD of a parallelogram?",
                "options": [
                    "Draw an arc of radius AB from D and an arc of radius AD from B; their intersection gives C!",
                    "Draw an arc of radius 90 cm from A only",
                    "Connect B directly to D with a perpendicular line",
                    "Measure only diagonal AC without side lengths"
                ],
                "answer": 0,
                "hint": "Recall opposite sides of a parallelogram must match: DC = AB and BC = AD!",
                "explanation": "Intersecting arcs centered at D (radius AB) and B (radius AD) locates C so DC = AB and BC = AD (two parallel pairs)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Parallelogram Angle Rules",
        "subtitle": "Section 4.3 Deduction 6: Transversal Parallel Properties (Adjacent Sum = 180°, Opposite Angles Equal)",
        "speech": (
            "Prove Deduction Six inside Section Four Point Three using parallel lines cut by straight transversals! Picture parallelogram ABCD where top side AB runs parallel to bottom side DC, AND left side AD runs parallel to right side BC! "
            "Watch transversal AD cut parallel rails AB and DC cleanly: remember Class Seven geometry! Interior angles sitting on the SAME SIDE of a transversal between parallel lines ALWAYS sum to ONE HUNDRED EIGHTY DEGREES! Immediately conclude: ANY TWO ADJACENT ANGLES inside EVERY parallelogram are SUPPLEMENTARY! That gives angle A + angle D = 180°, angle A + angle B = 180°, angle B + angle C = 180°, and angle C + angle D = 180°! "
            "Now watch the magic consequence pop right out immediately: since BOTH angle B AND angle D complement the exact same angle A up to 180 degrees (angle B = 180 − A and angle D = 180 − A), OPPOSITE ANGLES OF EVERY PARALLELOGRAM MUST ALWAYS EQUAL EACH OTHER! Test with clean numbers right now: if angle A measures 65°, adjacent corners B and D BOTH immediately equal 180° − 65° = 115°, while opposite corner C snaps to exact 65°!"
        ),
        "checkpoints": [
            {
                "question": "In parallelogram ABCD, if ∠A = 68°, find ∠B, ∠C, and ∠D using Deduction 6:",
                "options": [
                    "∠B = 112°,   ∠C = 68°,   ∠D = 112°",
                    "∠B = 68°,   ∠C = 112°,   ∠D = 112°",
                    "∠B = 90°,   ∠C = 68°,   ∠D = 90°",
                    "∠B = 122°,   ∠C = 68°,   ∠D = 122°"
                ],
                "answer": 0,
                "hint": "Adjacent angles add to 180° (180 − 68 = 112°), and opposite angles are equal!",
                "explanation": "Opposite ∠C = ∠A = 68°; adjacent ∠B = ∠D = 180° − 68° = 112°."
            },
            {
                "question": "What parallel-line geometry law directly proves Deduction 6 (adjacent parallelogram angles are supplementary and opposite angles are equal)?",
                "options": [
                    "Co-interior (same-side interior) angles along a transversal between two parallel lines always sum to 180°",
                    "All four angles must always equal 90°",
                    "Opposite sides never share angles",
                    "Exterior triangle angles equal 90°"
                ],
                "answer": 0,
                "hint": "Treat side AB as a transversal crossing parallel sides AD ∥ BC!",
                "explanation": "Parallel opposite sides make co-interior adjacent angles sum to 180°, forcing opposite angles equal."
            }
        ]
    },
    {
        "id": 8,
        "title": "Parallelogram Side Proofs",
        "subtitle": "Section 4.3 Deductions 7 & 8: Triangle Congruence (ΔABD ≅ ΔCDB Equal Sides & ASA Bisecting Diagonals)",
        "speech": (
            "Now conquer Deductions Seven and Eight inside Section Four Point Three to prove parallelogram SIDE LENGTHS and DIAGONAL BISECTION rigorously! "
            "Start with Deduction Seven: take parallelogram ABCD and draw crisp diagonal BD splitting it into two triangles ABD and CDB! Because AB runs parallel to DC, alternate interior angles ABD and CDB match identically! Likewise because AD runs parallel to BC, alternate interior angles ADB and CBD match identically! Plus diagonal BD stays shared cleanly in the middle! By ASA TRIANGLE CONGRUENCE, triangle ABD is strictly CONGRUENT to triangle CDB—immediately proving opposite sides AB = CD AND AD = BC ALWAYS! "
            "Next tackle Deduction Eight inside parallelogram EASY with crossing diagonals intersecting cleanly at center O! Compare opposing triangles AOE and YOS carefully: alternate interior angles along parallel opposite sides AE and SY match cleanly at E and S, and opposite sides AE = SY already match identically by Deduction Seven! By ASA congruence (triangle AOE congruent to triangle YOS), AO = OY AND EO = OS! Remember one vital geometry exam trap carefully: parallelogram diagonals ALWAYS bisect each other cleanly, yet remain generally UNEQUAL in total length unless every interior corner hits 90° (forming rectangles)!"
        ),
        "checkpoints": [
            {
                "question": "In Deduction 7, which congruence criterion proves opposite sides of parallelogram ABCD are equal (ΔABD ≅ ΔCDB)?",
                "options": [
                    "ASA Congruence  (alternate angles ∠ABD = ∠CDB, common side BD, alternate angles ∠ADB = ∠CBD)",
                    "AAA Angle Similarity only",
                    "SSS assuming opposite sides equal before proving them",
                    "SAS with 90° angles"
                ],
                "answer": 0,
                "hint": "Use parallel pairs AB ∥ DC and AD ∥ BC to get two pairs of alternate interior angles straddling shared diagonal BD!",
                "explanation": "Alternate angles match on both ends of common side BD (ASA), giving AB = CD and AD = BC."
            },
            {
                "question": "How do diagonals behave in a general non-rectangular parallelogram EASY with diagonals intersecting at O (Deduction 8)?",
                "options": [
                    "They BISECT each other (AO = OY and EO = OS via ASA ΔAOE ≅ ΔYOS), though the two diagonals need NOT be equal in length!",
                    "They are always equal in length",
                    "They always intersect at 90° right angles",
                    "They never cross inside the shape"
                ],
                "answer": 0,
                "hint": "Slanted parallelograms stretch one diagonal longer than the other, yet midpoint O still splits both cleanly in half!",
                "explanation": "Parallelogram diagonals always bisect each other cleanly, though unequal length distinguishes non-rectangles."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch4 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 5: I'm Up and Down, and Round and Round
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 5.7 to 5.8 (Theorems 9 to 12, Corollaries), Exercises & Summary with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Arcs Central Angles",
        "subtitle": "Section 5.7 Angles Subtended by an Arc: Minor Arc, Major Arc, Semicircle & Congruent Arc Central Angles",
        "speech": (
            "Now shift focus from straight chords cutting across a circle's interior to curved slices along the circular rim itself! Welcome to Section Five Point Seven: ANGLES SUBTENDED BY AN ARC! "
            "Whenever two boundary points A and B sit on a circle, they split the circular perimeter cleanly into TWO curved pieces called ARCS! If A and B are NOT diameter endpoints, the shorter curve between them is called the MINOR ARC AB, while the longer curved path wrapping the opposite way is called the MAJOR ARC AB! When chord AB passes through Centre O, both arcs equal exact SEMICIRCLES! "
            "Now ask: what angle does a curved arc AB subtend at Centre O? Simply connect arc endpoints A and B straight to O! Notice that a minor arc subtends an ordinary central angle below one hundred eighty degrees, a semicircle subtends a crisp straight angle one hundred eighty degrees, and a major arc subtends a REFLEX central angle exceeding one hundred eighty degrees! "
            "Check congruent arcs carefully too: just like equal straight chords in Theorem Two, congruent curved arcs carve strictly equal central angles at Centre O and match equal chord lengths seamlessly across the circle!"
        ),
        "checkpoints": [
            {
                "question": "If minor arc AB subtends central angle ∠AOB = 70° at Centre O, what reflex angle does the corresponding MAJOR arc AB subtend at Centre O?",
                "options": [
                    "290° (360° − 70°)",
                    "110° (180° − 70°)",
                    "35°",
                    "140°"
                ],
                "answer": 0,
                "hint": "Minor central angle + major reflex angle complete one full revolution around Centre O!",
                "explanation": "Full angle around O is 360°, so major arc AB subtends reflex angle 360° − 70° = 290°."
            },
            {
                "question": "What central angle does an exact semicircle arc subtend at Centre O?",
                "options": [
                    "180° (a straight angle along its diameter)",
                    "90°",
                    "360°",
                    "60°"
                ],
                "answer": 0,
                "hint": "A semicircle spans halfway around the 360° circle!",
                "explanation": "Endpoints of a semicircle form a diameter through O, subtending straight angle 180°."
            }
        ]
    },
    {
        "id": 10,
        "title": "Central Inscribed Double",
        "subtitle": "Section 5.7.1 Theorem 9: Central Angle Subtended by an Arc Equals Double the Inscribed Angle Outside the Arc",
        "speech": (
            "Prepare for the powerhouse theorem of circle angle geometry—SECTION FIVE POINT SEVEN POINT ONE, THEOREM NINE! "
            "Pick an arc AB on a circle with Centre O, and place ANY third point P sitting along the remaining outer part of the circle outside arc AB! Connect P to A and B to form inscribed angle APB! Theorem Nine declares cleanly: THE ANGLE SUBTENDED BY AN ARC AT THE CENTRE IS DOUBLE THE ANGLE SUBTENDED BY IT AT ANY POINT ON THE REMAINING PART OF THE CIRCLE—angle AOB equals TWICE angle APB! "
            "Watch how cleanly the isosceles-triangle proof works! Draw ray PO straight through Centre O to point M across the circle! Look at triangle OAP: since OA equals OP (both radii!), base angles OAP and OPA are EQUAL—call both alpha! "
            "By triangle exterior-angle rule, outer angle AOM equals TWO alpha! Repeat on triangle OBP: radius OB equals OP makes base angles equal beta, so outer angle BOM equals TWO beta! "
            "Adding or subtracting those exterior central angles cleanly reveals total central angle AOB strictly equals two times open alpha plus beta close—meaning TWICE inscribed angle APB across minor arcs, exact semicircles, and reflex major arcs alike!"
        ),
        "checkpoints": [
            {
                "question": "An arc AB subtends central angle ∠AOB = 136° at Centre O. What inscribed angle ∠APB does arc AB subtend at point P on the circle outside the arc?",
                "options": [
                    "68° (half of 136°)",
                    "272°",
                    "136°",
                    "44°"
                ],
                "answer": 0,
                "hint": "Apply Theorem 9: ∠AOB = 2 × ∠APB ⇒ ∠APB = ∠AOB / 2!",
                "explanation": "By Theorem 9, central angle is double the inscribed angle: ∠APB = 136° / 2 = 68°."
            },
            {
                "question": "If inscribed angle ∠APB = 55° (with P outside minor arc AB), what is the central angle ∠AOB AND what is reflex ∠AOB?",
                "options": [
                    "Central ∠AOB = 110° and reflex ∠AOB = 250°",
                    "Central ∠AOB = 27.5° and reflex = 332.5°",
                    "Central ∠AOB = 125° and reflex = 235°",
                    "Central ∠AOB = 110° and reflex = 110°"
                ],
                "answer": 0,
                "hint": "Double 55° for central ∠AOB, then subtract from 360° for reflex!",
                "explanation": "Theorem 9 gives ∠AOB = 2(55°) = 110°; reflex angle = 360° − 110° = 250°."
            }
        ]
    },
    {
        "id": 11,
        "title": "Semicircle Same Segment",
        "subtitle": "Section 5.7.1 Corollaries of Theorem 9: Angle in a Semicircle Equals 90° & Angles in Same Segment Are Equal",
        "speech": (
            "Watch Theorem Nine effortlessly drop TWO stunning corollaries straight into our lap in Section Five Point Seven Point One! "
            "Corollary One—THE ANGLE IN A SEMICIRCLE IS ALWAYS NINETY DEGREES! Test why in one mental step! Draw diameter AB passing straight through Centre O! That straight diameter arc subtends central angle AOB equal to ONE HUNDRED EIGHTY DEGREES! Now pick ANY point P anywhere along the semicircular arch and connect PA and PB! By Theorem Nine, inscribed angle APB equals HALF the central angle—half of one hundred eighty equals EXACTLY NINETY DEGREES every single time! Builders check square corners instantly with this semicircle theorem! "
            "Corollary Two—ANGLES SUBTENDED IN THE SAME SEGMENT OF A CIRCLE ARE ALWAYS EQUAL TO ONE ANOTHER! Keep chord arc AB fixed and choose two DIFFERENT observation points P and Q sitting anywhere along the same remaining upper arc segment! Connect both points P and Q cleanly straight back to endpoints A and B! Look carefully: angle APB equals HALF central angle AOB, AND angle AQB ALSO equals HALF that exact same central angle AOB! Two inscribed angles equaling half the exact same central angle always match identically every single time across the segment!"
        ),
        "checkpoints": [
            {
                "question": "If AB is a diameter of a circle with Centre O and C is any point on the circle other than A and B, what does ∠ACB always measure?",
                "options": [
                    "90° (angle in a semicircle)",
                    "180°",
                    "45°",
                    "60°"
                ],
                "answer": 0,
                "hint": "Diameter AB subtends 180° at Centre O; divide by 2 using Theorem 9!",
                "explanation": "∠ACB = ½ × ∠AOB = ½(180°) = 90°, so every triangle inscribed on a diameter is right-angled at C."
            },
            {
                "question": "Points P, Q, and R all lie in the same major segment above chord AB. If ∠APB = 42°, what are ∠AQB and ∠ARB?",
                "options": [
                    "Both ∠AQB and ∠ARB equal 42° (angles in the same segment are equal)",
                    "84° and 21°",
                    "138° each",
                    "They vary depending on where Q and R sit"
                ],
                "answer": 0,
                "hint": "All three inscribed angles equal ½ of the exact same central angle ∠AOB!",
                "explanation": "By the same-segment corollary of Theorem 9, ∠APB = ∠AQB = ∠ARB = ½∠AOB = 42°."
            }
        ]
    },
    {
        "id": 12,
        "title": "Concyclic Points Rule",
        "subtitle": "Section 5.8 Concyclicity of Points: Definition of Concyclic Points & Theorem 10 (Equal Angles on Same Side)",
        "speech": (
            "Earlier in Theorem One, we learned that EVERY triangle of three non-collinear points automatically shares a unique circle! Now ask the deeper question in Section Five Point Eight: do FOUR or more points automatically lie on one common circle? NO—just try three triangle vertices plus one random fourth point inside or way outside the circle! "
            "Whenever four or more points DO happen to share one single circle passing cleanly through all of them, we call them CONCYCLIC POINTS! How can geometricians prove four points A, B, C, and D are concyclic WITHOUT literally swinging a compass? "
            "Unlock THEOREM TEN! Suppose straight line segment AB joins points A and B, and on ONE SAME SIDE of line AB sit two points C and D such that angle ACB STRICTLY EQUALS angle ADB! Theorem Ten proves all four points A, B, C, D are CONCYCLIC! "
            "How does proof by contradiction seal Theorem Ten cleanly? Draw the unique circumcircle passing through three non-collinear points A, B, and C! If that circle ever missed D—cutting line AD at D-prime instead—then same-segment angles ACB and AD-prime-B would both equal ADB, forcing an impossible triangle exterior-angle contradiction unless D lands squarely ON the circle!"
        ),
        "checkpoints": [
            {
                "question": "When are four points A, B, C, and D mathematically called CONCYCLIC?",
                "options": [
                    "When a single circle passes through all four points simultaneously",
                    "When all four points lie on one straight line",
                    "When only two of them touch a circle",
                    "When their pairwise distances are all equal"
                ],
                "answer": 0,
                "hint": "Think 'con-cyclic' = sharing one common circle!",
                "explanation": "Points lying on the circumference of the same single circle are concyclic."
            },
            {
                "question": "In Theorem 10, if line segment AB subtends ∠ACB = 50° and ∠ADB = 50° at points C and D lying on the SAME side of AB, what must follow?",
                "options": [
                    "Points A, B, C, and D are concyclic (lie on the same circle)",
                    "Segment CD is perpendicular to AB",
                    "Points A, C, D must be collinear",
                    "Angle ACB and ADB must sum to 180°"
                ],
                "answer": 0,
                "hint": "Equal angles subtended on the same side of a segment satisfy the converse of same-segment angles!",
                "explanation": "Theorem 10 guarantees that if AB subtends equal angles at two points on the same side, all four points share one circle."
            }
        ]
    },
    {
        "id": 13,
        "title": "Cyclic Opposite Sum",
        "subtitle": "Section 5.8 Cyclic Quadrilaterals: Theorem 11 (Opposite Angles Sum to 180°) & Theorem 12 (Converse Concyclicity)",
        "speech": (
            "Now inspect what happens when ALL FOUR vertices of a closed quadrilateral ABCD sit squarely on one circle—forming a CYCLIC QUADRILATERAL in Section Five Point Eight! "
            "Test THEOREM ELEVEN: THE SUM OF EITHER PAIR OF OPPOSITE ANGLES OF A CYCLIC QUADRILATERAL EQUALS ONE HUNDRED EIGHTY DEGREES! "
            "Prove this diamond of geometry cleanly using Theorem Nine! Connect opposite vertices B and D back to Centre O! Notice vertex angle A (angle DAB) faces minor arc BD, so by Theorem Nine, angle A equals HALF the central angle BOD facing A! Look directly across at opposite vertex angle C (angle DCB): C faces the remaining major arc BD, so angle C equals HALF the REFLEX central angle BOD! "
            "Add both opposite angles together: angle A plus angle C equals HALF times open central angle plus reflex angle close—which is HALF OF THREE HUNDRED SIXTY DEGREES equals ONE HUNDRED EIGHTY DEGREES! (And if you extend one side outward, the exterior angle matches the interior opposite angle!) "
            "Flip it cleanly for THEOREM TWELVE (Converse): IF ONE PAIR OF OPPOSITE ANGLES OF ANY QUADRILATERAL SUMS TO ONE HUNDRED EIGHTY DEGREES, THEN ALL FOUR VERTICES ARE GUARANTEED CONCYCLIC—automatically forming a valid cyclic quadrilateral!"
        ),
        "checkpoints": [
            {
                "question": "In cyclic quadrilateral PQRS, if ∠P = 112° and ∠Q = 83°, what are the exact measures of opposite angles ∠R and ∠S?",
                "options": [
                    "∠R = 68° and ∠S = 97°",
                    "∠R = 83° and ∠S = 112°",
                    "∠R = 112° and ∠S = 83°",
                    "∠R = 78° and ∠S = 87°"
                ],
                "answer": 0,
                "hint": "Use Theorem 11: ∠P + ∠R = 180° and ∠Q + ∠S = 180°!",
                "explanation": "∠R = 180° − 112° = 68°, and ∠S = 180° − 83° = 97°."
            },
            {
                "question": "Using Theorem 12 (converse), why is EVERY rectangle (and square) guaranteed to be a cyclic quadrilateral, whereas a general non-rectangular parallelogram is NOT?",
                "options": [
                    "In a rectangle, opposite angles are 90° + 90° = 180° (satisfying Theorem 12), whereas non-rectangular parallelograms have acute+acute < 180° or obtuse+obtuse > 180°",
                    "Rectangles only have 3 vertices on a circle",
                    "Parallelograms always have opposite angles summing to 180°",
                    "Circles cannot pass through equal-length edges"
                ],
                "answer": 0,
                "hint": "Check opposite angle sums inside a parallelogram with angles 70°, 110°, 70°, 110°!",
                "explanation": "A parallelogram's opposite angles are equal, so α + α = 180° ⇔ α = 90° (only true for rectangles/squares!)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Chord Pythagoras Applications",
        "subtitle": "End-of-Chapter Computational Techniques: Dual-Chord Distances (Same Side vs Opposite Sides of Centre) & Common Chords",
        "speech": (
            "Preview how End-of-Chapter Exercises combine Theorem Five and Pythagoras into crystal-clear chord calculations! "
            "Keep our core chord triangle formula locked in: perpendicular OM from Centre O bisects chord AB at M, creating right triangle OMA with radius r squared equal to half-chord AM squared plus distance OM squared! "
            "Watch one classic two-chord exam puzzle carefully: TWO PARALLEL CHORDS of lengths sixteen centimetres and twelve centimetres sit inside a circle of radius ten centimetres! What separates those two parallel chords? Wait—STOP AND CHECK BOTH CASES! "
            "First find each chord's perpendicular distance from O! For sixteen-centimetre chord, half-chord equals eight, so distance one equals square root of ten squared minus eight squared equals SIX centimetres! For twelve-centimetre chord, half-chord equals six, so distance two equals square root of ten squared minus six squared equals EIGHT centimetres! "
            "Now inspect BOTH physical arrangements carefully before writing any final answer! If both parallel chords lie on OPPOSITE SIDES of Centre O, add distances together: six plus eight equals FOURTEEN centimetres! If both chords lie on the SAME SIDE of Centre O, subtract shorter distance from longer: eight minus six equals TWO centimetres! Always verify same-side versus opposite-side placement carefully before answering!"
        ),
        "checkpoints": [
            {
                "question": "Two parallel chords of lengths 30 cm and 16 cm lie on OPPOSITE sides of Centre O in a circle of radius 17 cm. What is the distance between them?",
                "options": [
                    "23 cm (8 cm + 15 cm)",
                    "7 cm (15 cm − 8 cm)",
                    "17 cm",
                    "46 cm"
                ],
                "answer": 0,
                "hint": "Calculate d₁ = √(17² − 15²) = 8 cm and d₂ = √(17² − 8²) = 15 cm, then ADD for opposite sides!",
                "explanation": "Half-chords are 15 cm and 8 cm; distances are √(289 − 225) = 8 cm and √(289 − 64) = 15 cm. Opposite sides ⇒ 8 + 15 = 23 cm."
            },
            {
                "question": "When two circles of radii 5 cm and 3 cm intersect at two points with centres 4 cm apart, what geometric relation links line of centres OO' and common chord AB?",
                "options": [
                    "The line of centres OO' is the exact perpendicular bisector of common chord AB (giving common chord length 6 cm here)",
                    "OO' is parallel to AB",
                    "Common chord equals 4 cm",
                    "AB passes strictly through the smaller circle's tangent only"
                ],
                "answer": 0,
                "hint": "Every point equidistant from circle endpoints (O and O' each have OA=OB and O'A=O'B) sits on the perpendicular bisector!",
                "explanation": "Since OA=OB and O'A=O'B, OO' lies on the perpendicular bisector of AB! Notice 3² + 4² = 5² places O' right at midpoint of AB ⇒ AB = 2(3) = 6 cm."
            }
        ]
    },
    {
        "id": 15,
        "title": "Cyclic Angle Proofs",
        "subtitle": "End-of-Chapter Geometric Proofs: Angle-Chasing Chains Combining Theorem 9, Same Segment & Cyclic Quadrilaterals",
        "speech": (
            "Now sharpen multi-step geometric proving skills from the End-of-Chapter Exercises, uniting Theorems Nine, Ten, Eleven, and Twelve seamlessly! "
            "Whenever an exercise hands you circles crossed by triangles, inscribed quadrilaterals, and diameters, follow a disciplined THREE-TOOL ANGLE CHASE! "
            "Tool One: scan immediately for ANY diameter chord passing through Centre O—mark its opposite inscribed circle angle NINETY DEGREES using the semicircle corollary! "
            "Tool Two: scan for shared arcs holding BOTH a central vertex at O and boundary vertices on the rim—lock in the exact TWO-TO-ONE Theorem Nine ratio, plus equal angles standing in the SAME SEGMENT! "
            "Tool Three: trace every four-sided figure whose four corners touch the circle—unlock OPPOSITE ANGLES SUMMING TO ONE HUNDRED EIGHTY DEGREES! "
            "Test one iconic circle theorem proof right now: prove EVERY CYCLIC PARALLELOGRAM MUST ALWAYS BE A RECTANGLE! Inside cyclic parallelogram ABCD, opposite interior angles are strictly equal (angle A equals angle C from parallelogram symmetry) AND strictly supplementary (angle A plus angle C equals one hundred eighty degrees from Theorem Eleven)! Twice angle A equals one hundred eighty forces angle A strictly equal to NINETY DEGREES—immediately proving every interior corner measures ninety degrees and quadrilateral ABCD must be a true rectangle!"
        ),
        "checkpoints": [
            {
                "question": "In cyclic quadrilateral ABCD, diagonal BD is a diameter and ∠ABD = 35°. Using Theorem 9 corollaries and Theorem 11, find ∠ADB and ∠BCD.",
                "options": [
                    "∠ADB = 55° and ∠BCD = 90°",
                    "∠ADB = 35° and ∠BCD = 145°",
                    "∠ADB = 90° and ∠BCD = 55°",
                    "∠ADB = 55° and ∠BCD = 125°"
                ],
                "answer": 0,
                "hint": "Diameter BD creates 90° at BOTH semicircle vertices A and C!",
                "explanation": "Since BD is a diameter, ∠BAD = 90° and ∠BCD = 90°. Inside ΔABD, ∠ADB = 180° − 90° − 35° = 55°."
            },
            {
                "question": "If the non-parallel sides AD and BC of a trapezium ABCD are EQUAL (isosceles trapezium), how does Theorem 12 prove ABCD is ALWAYS cyclic?",
                "options": [
                    "Isosceles trapezium symmetry makes base angles ∠B = ∠A while co-interior angles give ∠A + ∠D = 180°, forcing opposite angles ∠B + ∠D = 180°",
                    "Because all trapeziums are squares",
                    "Because opposite angles equal 90° each always",
                    "Because AB equals CD always"
                ],
                "answer": 0,
                "hint": "Replace ∠A with equal base angle ∠B inside the parallel co-interior sum ∠A + ∠D = 180°!",
                "explanation": "Since AB ∥ DC, ∠A + ∠D = 180°; AD = BC gives ∠A = ∠B, hence ∠B + ∠D = 180°, confirming ABCD is cyclic by Theorem 12."
            }
        ]
    },
    {
        "id": 16,
        "title": "Circle Chapter Summary",
        "subtitle": "Chapter Summary: Complete Synthesis of Locus, Symmetries, Theorems 1–12, Corollaries & Cyclic Angle Laws",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your master Circle Synthesis consolidating EVERY definition, symmetry, and ALL TWELVE THEOREMS of Chapter Five! "
            "Review every structural pillar! Pillar One—LOCUS AND SYMMETRIES: every circle boundary point stays equidistant distance r from Centre O, granting complete rotational symmetry around O and infinitely many diameter reflection axes! "
            "Pillar Two—CIRCLES THROUGH POINTS: infinitely many circles cross two points along their perpendicular bisector, while THREE non-collinear points define ONE UNIQUE CIRCUMCIRCLE (Theorem One) whose circumcentre moves inside acute, onto right hypotenuse, and outside obtuse triangles! "
            "Pillar Three—CHORDS AND PERPENDICULARS: Theorems Two through Eight establish equal chords match equal central angles and equal centre distances; perpendiculars bisect chords; and longer chords sit closer to Centre O via r squared equals half-chord squared plus distance squared! "
            "Pillar Four—ARCS, ANGLES AND CONCYCLICITY: Theorem Nine halves central angles cleanly onto inscribed circle points, instantly forcing ninety-degree semicircle angles and equal same-segment angles; Theorems Ten, Eleven, and Twelve link equal same-side angles and one-hundred-eighty-degree opposite angle sums directly to concyclic four-point circles! Apply chord-bisector Pythagoras distances and clean multi-step geometric angle-chasing proof chains with complete precision and confidence—now test your full chapter mastery cleanly across all four silent exercise quizzes!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement accurately states ALL three foundational circle properties together?",
                "options": [
                    "Equal chords are equidistant from Centre O; central angle = 2 × inscribed angle; opposite angles of a cyclic quadrilateral sum to 180°",
                    "Longer chords sit farther from O; central angle = ½ inscribed angle; all parallelograms are cyclic",
                    "Only 2 diameters exist per circle; 3 collinear points define a unique circle",
                    "Angle in a semicircle measures 60°; equal chords subtend different central angles"
                ],
                "answer": 0,
                "hint": "Check Theorems 6, 9, 11 and their corollaries carefully!",
                "explanation": "All three clauses accurately synthesize Sections 5.6 (Theorem 6), 5.7 (Theorem 9), and 5.8 (Theorem 11)."
            },
            {
                "question": "Which converse theorem lets you PROVE that four given points A, B, C, D lie on one circle without drawing the circle first?",
                "options": [
                    "Theorem 10 (equal angles on the same side of a segment) OR Theorem 12 (opposite quadrilateral angles summing to 180°)",
                    "Theorem 2 (equal chords subtend equal central angles) alone",
                    "Theorem 4 (centre to midpoint is perpendicular) alone",
                    "Triangle angle sum equals 180° alone"
                ],
                "answer": 0,
                "hint": "Look back at Section 5.8 Concyclicity of Points!",
                "explanation": "Both Theorem 10 and Theorem 12 provide direct sufficiency conditions proving four points are concyclic."
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 5: I'm Up and Down, and Round and Round
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 5.1 to 5.6.1 (Theorems 1 to 8) with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Circle Locus Components",
        "subtitle": "Section 5.1 Definitions: Circle as Equidistant Locus, Centre, Radius, Chords, Diameters & Subtended Central Angles",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Five: I'm Up and Down, and Round and Round—our complete geometric journey into Circles! "
            "Begin with the pure mathematical locus definition in Section Five Point One! What exactly IS a circle? Fix one special anchor point O on a flat plane—called the CENTRE—and pick one positive constant distance r—called the RADIUS! Collect EVERY single point on the plane standing at that exact fixed distance r from Centre O! That continuous closed curve of equidistant points forms a CIRCLE! "
            "Now inspect key structural parts connecting points along this circular boundary! Connect ANY two boundary points P and Q with a straight line segment: we call PQ a CHORD! Notice what happens when you slide a chord straight through Centre O! That special longest chord splits the circle into two equal halves and measures twice the radius—the DIAMETER! "
            "Next connect both chord endpoints P and Q straight back to Centre O! The resulting central angle POQ opening cleanly at Centre O is called the ANGLE SUBTENDED BY CHORD PQ AT THE CENTRE! Notice equal circles share equal radii, and every chord divides a circle into two regions! Mastering these core geometric definitions unlocks every circle theorem ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which statement accurately defines a circle as a geometric locus in a plane?",
                "options": [
                    "The collection of all points in a plane sitting at a fixed constant distance (radius) from a fixed point (centre)",
                    "Any closed four-sided polygon with equal opposite sides",
                    "The set of points closer to a line than to a point",
                    "A single straight chord joining two points"
                ],
                "answer": 0,
                "hint": "Think about pinning one compass needle at Centre O and rotating a fixed radius r!",
                "explanation": "Every point P on the circle satisfies distance OP = r (constant radius) from fixed centre O."
            },
            {
                "question": "If chord AB passes directly through Centre O of a circle with radius 6.5 cm, what special name and length does AB have?",
                "options": [
                    "Diameter, of length 13 cm (equal to 2 × radius)",
                    "Minor arc, of length 6.5 cm",
                    "Perpendicular bisector, of length 3.25 cm",
                    "Radius, of length 13 cm"
                ],
                "answer": 0,
                "hint": "Any chord passing through the centre O spans two opposite radii along one straight line!",
                "explanation": "A chord passing through Centre O is a diameter of length d = 2r = 2(6.5) = 13 cm."
            }
        ]
    },
    {
        "id": 2,
        "title": "Complete Circle Symmetries",
        "subtitle": "Section 5.2 Symmetries of a Circle: Continuous Rotational Symmetry & Infinite Reflection Axes Across Diameters",
        "speech": (
            "Why do bicycle wheels roll effortlessly round and round without bumping up and down? Explore Section Five Point Two: SYMMETRIES OF A CIRCLE! "
            "Compare a regular square or equilateral triangle against a pure circle! An equilateral triangle maps neatly onto itself ONLY at three rotation stops—one hundred twenty, two hundred forty, and three hundred sixty degrees! A regular square matches at just four ninety-degree turns! "
            "Now spin a circle around its Centre O by ANY angle whatsoever—one degree, seventeen degrees, forty-five degrees, or even zero point zero zero one degrees! Because every boundary point maintains exact fixed distance r from O, the circle lands PERFECTLY back onto itself under EVERY angle of rotation! That continuous property is COMPLETE ROTATIONAL SYMMETRY around Centre O! "
            "Next test mirror reflection folds! Draw ANY straight line passing directly through Centre O—meaning ANY diameter line cutting straight across the circle! Folding the flat circular plane seamlessly along that diameter maps the left semicircle cleanly onto the right semicircle point for exact point! Since infinitely many distinct diameter lines cut through fixed Centre O at every angle, a pure circle enjoys INFINITELY MANY AXES OF REFLECTION SYMMETRY alongside continuous rotational perfection!"
        ),
        "checkpoints": [
            {
                "question": "How many lines of reflection symmetry and what rotational symmetry does a circle possess?",
                "options": [
                    "Infinitely many lines of reflection symmetry (every diameter line) and complete rotational symmetry for every angle about its centre",
                    "Exactly 4 reflection lines and 90° rotational symmetry only",
                    "Exactly 2 reflection lines (horizontal and vertical axes) and 180° rotational symmetry",
                    "Zero reflection lines outside regular polygons"
                ],
                "answer": 0,
                "hint": "Think: how many diameters can you draw through Centre O, and what happens if you rotate by 13°?",
                "explanation": "Every diameter acts as a mirror reflection axis (infinitely many), and every rotation by any angle maps the circle onto itself."
            },
            {
                "question": "Which point of a circle always remains stationary under BOTH every reflection across a diameter AND every rotation mapping the circle to itself?",
                "options": [
                    "The Centre O",
                    "Only the topmost point of the circle",
                    "A midpoint of an off-centre chord",
                    "No point stays fixed"
                ],
                "answer": 0,
                "hint": "Every diameter passes through one common point, and all rotations spin around it!",
                "explanation": "Every diameter contains O and all circular rotations pivot around O, keeping Centre O invariant."
            }
        ]
    },
    {
        "id": 3,
        "title": "Circles Through Two",
        "subtitle": "Section 5.3 How Many Circles?: Infinitely Many Circles Through Two Points A, B & Centres Along Perpendicular Bisector",
        "speech": (
            "Now play geometric detective in Section Five Point Three: HOW MANY CIRCLES CAN PASS THROUGH GIVEN POINTS? "
            "Test ONE single point A first! Place Centre O anywhere on the plane and open your compass straight to A—infinitely many circles pass effortlessly through one point! "
            "Next fix TWO distinct points A and B separated by segment AB! How many distinct circles pass simultaneously through BOTH A and B? Wait—any candidate Centre O must keep distance OA strictly equal to distance OB! "
            "Where on a flat plane do ALL points equidistant from endpoints A and B live? Recall fundamental triangle congruence geometry: EVERY point equidistant from A and B lies along the exact PERPENDICULAR BISECTOR line of segment AB! "
            "Pick a centre point sitting very close to midpoint M of segment AB: you trace the smallest possible circle whose full diameter equals AB! Slide Centre O steadily upward or downward along that perpendicular bisector line: your compass radius stretches larger and larger without any upper limit, tracing giant sweeping circular arcs passing cleanly through BOTH points A and B! Since a straight line contains infinitely many distinct centre spots, INFINITELY MANY CIRCLES pass through two given points!"
        ),
        "checkpoints": [
            {
                "question": "Where must the centre O of ANY circle passing through two distinct points A and B strictly lie?",
                "options": [
                    "On the perpendicular bisector of segment AB",
                    "Strictly at the midpoint M of segment AB only",
                    "On the circle having A as centre and AB as radius only",
                    "Strictly outside the plane of A and B"
                ],
                "answer": 0,
                "hint": "Requirement OA = OB defines the exact geometric locus of points equidistant from A and B!",
                "explanation": "All points equidistant from A and B lie along the perpendicular bisector of AB; any point on that line can serve as a circle centre through A and B."
            },
            {
                "question": "How many distinct circles pass through two fixed points A and B, and which one has the minimum possible radius?",
                "options": [
                    "Infinitely many circles; the smallest circle has segment AB as its diameter (radius = AB/2)",
                    "Only 1 unique circle",
                    "Exactly 2 circles (one on each side of AB)",
                    "Zero circles unless angle AOB = 90°"
                ],
                "answer": 0,
                "hint": "Notice OA ≥ AM by right triangle OAM, with minimum OA = AM occurring when O hits midpoint M!",
                "explanation": "Choosing any point O along the perpendicular bisector yields a valid circle through A and B; minimum radius OA = AB/2 happens when O is midpoint M."
            }
        ]
    },
    {
        "id": 4,
        "title": "Unique Three-Point Circumcircle",
        "subtitle": "Section 5.3 Theorem 1: Unique Circle Through Three Non-Collinear Points, Circumcentre & Acute/Right/Obtuse Triangles",
        "speech": (
            "Wait—what happens the moment you add a THIRD point C not lying on the straight line through A and B? Unlock THEOREM ONE in Section Five Point Three! "
            "Can infinitely many circles still fit A, B, and C, or does that third point lock down ONE UNIQUE CIRCLE? Check perpendicular bisectors! Any centre O fitting A and B MUST sit along line l, the perpendicular bisector of AB! Similarly, fitting B and C forces Centre O to ALSO sit along line m, the perpendicular bisector of BC! "
            "Since A, B, C are NOT collinear, lines l and m cannot be parallel—they intersect cleanly at ONE AND ONLY ONE point O! Because OA equals OB and OB equals OC, O sits strictly equidistant from A, B, and C! Wait—why can THREE COLLINEAR points never share a circle? Their perpendicular bisectors stay strictly parallel, never crossing! "
            "We call that unique circle passing cleanly through all three vertices A, B, and C the CIRCUMCIRCLE, and unique intersection O the CIRCUMCENTRE! Notice a sleek triangle rule: in an ACUTE triangle, circumcentre O sits strictly INSIDE; in a RIGHT triangle, O lands RIGHT AT THE HYPOTENUSE MIDPOINT; in an OBTUSE triangle, O sits strictly OUTSIDE!"
        ),
        "checkpoints": [
            {
                "question": "Why does NO circle pass through three distinct collinear points P, Q, and R lying on a single straight line?",
                "options": [
                    "The perpendicular bisectors of PQ and QR are parallel lines and never intersect to provide a common centre",
                    "Collinear points are always equidistant from each other",
                    "Three points always form a square",
                    "The radius would automatically equal negative length"
                ],
                "answer": 0,
                "hint": "Two distinct lines both perpendicular to the same straight line PQR stay parallel!",
                "explanation": "Because perpendiculars to line PQR are parallel, there is no point O satisfying OP = OQ = OR simultaneously."
            },
            {
                "question": "Where does the circumcentre O lie for an acute-angled triangle, a right-angled triangle, and an obtuse-angled triangle?",
                "options": [
                    "Inside for acute, midpoint of hypotenuse for right, outside the triangle for obtuse",
                    "Always inside all three triangle types",
                    "Always on the longest side for every triangle",
                    "Outside for acute and inside for obtuse"
                ],
                "answer": 0,
                "hint": "Think about the angle subtended by the longest side at the opposite vertex compared with 90°!",
                "explanation": "Circumcentre lies inside an acute triangle, exactly on the hypotenuse midpoint in a right triangle, and outside an obtuse triangle (opposite the obtuse vertex)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Chords Central Angles",
        "subtitle": "Section 5.4 Chords & Subtended Angles: Theorem 2 (Equal Chords ⇒ Equal Central Angles) & Theorem 3 (Converse)",
        "speech": (
            "Now bridge chord lengths directly with central angles in Section Five Point Four through THEOREM TWO and its partner THEOREM THREE! "
            "THEOREM TWO states cleanly: EQUAL CHORDS OF A CIRCLE SUBTEND EQUAL ANGLES AT THE CENTRE! Prove it in ten seconds using triangle congruence! Draw two equal chords AB and CD inside circle Centre O (AB equals CD). Connect all four endpoints straight to Centre O, creating two central triangles AOB and COD! "
            "Check all three sides cleanly! Side OA equals OC (both circle radii!), side OB equals OD (also radii!), and chord AB equals CD (given)! By SIDE-SIDE-SIDE congruence, triangles AOB and COD are identical twins—forcing angle AOB strictly equal to angle COD! "
            "Now flip it completely around for THEOREM THREE (Converse): IF ANGLES SUBTENDED BY TWO CHORDS AT THE CENTRE ARE STRICTLY EQUAL, THEN THE CHORDS THEMSELVES ARE ALWAYS EQUAL IN LENGTH! Compare central triangles AOB and COD carefully again: side OA equals OC (both circle radii), side OB equals OD (both circle radii), and the included central angle AOB equals central angle COD (given)! By SIDE-ANGLE-SIDE congruence, both central triangles match identically everywhere, immediately forcing opposite chords AB and CD STRICTLY EQUAL!"
        ),
        "checkpoints": [
            {
                "question": "In Theorem 2, which triangle congruence criterion directly proves that equal chords AB = CD subtend equal angles ∠AOB = ∠COD at Centre O?",
                "options": [
                    "SSS Congruence (OA = OC, OB = OD as radii, and given AB = CD)",
                    "AAA Similarity only",
                    "RHS Congruence with 90° angles",
                    "ASA Congruence without using chord length"
                ],
                "answer": 0,
                "hint": "Notice all three pairs of sides in ΔAOB and ΔCOD match directly!",
                "explanation": "Since OA = OC = r, OB = OD = r, and AB = CD, ΔAOB ≅ ΔCOD by SSS, so ∠AOB = ∠COD (CPCTC)."
            },
            {
                "question": "In Theorem 3 (converse), given ∠AOB = ∠COD inside circle Centre O, which criterion proves chord AB = chord CD?",
                "options": [
                    "SAS Congruence (two pairs of radii and the included central angles)",
                    "SSS Congruence",
                    "AAS Congruence using tangent lines",
                    "Equilateral triangle sum theorem"
                ],
                "answer": 0,
                "hint": "Two sides are circle radii with the equal central angle sandwiched in between!",
                "explanation": "OA = OC, ∠AOB = ∠COD, OB = OD ⇒ ΔAOB ≅ ΔCOD by SAS ⇒ AB = CD."
            }
        ]
    },
    {
        "id": 6,
        "title": "Chord Bisector Theorems",
        "subtitle": "Section 5.5 Midpoints & Perpendicular Bisectors: Theorem 4 (Centre-to-Midpoint ⊥ Chord) & Theorem 5 (Converse)",
        "speech": (
            "Discover the golden right-angle link between a circle's centre and any chord's midpoint in Section Five Point Five—THEOREM FOUR and THEOREM FIVE! "
            "Draw ANY chord AB inside circle Centre O, locate midpoint M of AB (so AM equals BM), and connect O straight down to M! THEOREM FOUR proves that line OM stands STRICTLY PERPENDICULAR to chord AB (ninety degrees)! "
            "Watch how effortlessly congruence proves it: inside triangles OAM and OBM, side OA equals OB (radii), AM equals BM (midpoint M), and OM equals OM (shared side)! By SSS congruence, adjacent linear-pair angles OMA and OMB match identically—and since they add along straight line AB to one hundred eighty degrees, EACH angle MUST equal ninety degrees! "
            "Now flip Theorem Four cleanly to unlock THEOREM FIVE (Converse): ANY PERPENDICULAR LINE DROPPED STRAIGHT FROM THE CENTRE OF A CIRCLE ONTO A CHORD ALWAYS BISECTS THE CHORD INTO TWO EQUAL HALVES! Given both right angles OMA and OMB equal ninety degrees, examine right triangles OAM and OBM closely: hypotenuse OA equals OB (both circle radii) and shared perpendicular leg OM is completely common! By RHS right-triangle congruence, both matching half-chords AM and MB MUST be strictly EQUAL in length!"
        ),
        "checkpoints": [
            {
                "question": "If O is the centre of a circle and M is the midpoint of chord AB, what does Theorem 4 prove about segment OM?",
                "options": [
                    "OM is perpendicular to AB (∠OMA = ∠OMB = 90°)",
                    "OM equals half the length of radius OA",
                    "OM is always parallel to chord AB",
                    "Triangle OAB must be equilateral"
                ],
                "answer": 0,
                "hint": "Triangles OAM and OBM match by SSS, splitting the 180° straight angle at M equally!",
                "explanation": "ΔOAM ≅ ΔOBM (SSS) ⇒ ∠OMA = ∠OMB = 180°/2 = 90°, so OM ⊥ AB."
            },
            {
                "question": "In a circle of radius 10 cm, perpendicular OM from Centre O meets chord AB at M with OM = 6 cm. Using Theorem 5 and Pythagoras, find full chord length AB.",
                "options": [
                    "16 cm (since AM = √(10² − 6²) = 8 cm, so AB = 2 × 8 = 16 cm)",
                    "8 cm",
                    "12 cm",
                    "20 cm"
                ],
                "answer": 0,
                "hint": "Find half-chord AM from right triangle OMA first, then double it using Theorem 5!",
                "explanation": "AM = √(OA² − OM²) = √(100 − 36) = 8 cm; by Theorem 5 OM bisects AB, giving AB = 2(8) = 16 cm."
            }
        ]
    },
    {
        "id": 7,
        "title": "Equidistant Chord Properties",
        "subtitle": "Section 5.6 Distance of Chords from Centre: Theorems 6 & 7 (Equal Chords ⇔ Equidistant from Centre)",
        "speech": (
            "How far does any chord sit from a circle's centre, and how does chord length govern that perpendicular gap? Open Section Five Point Six: THEOREMS SIX AND SEVEN! "
            "First clarify how geometry measures the DISTANCE OF A LINE FROM A POINT: always drop the shortest PERPENDICULAR segment OM from Centre O straight onto chord AB—whose length d equals OM! "
            "Now inspect THEOREM SIX: EQUAL CHORDS OF A CIRCLE ARE EQUIDISTANT FROM THE CENTRE! Suppose two chords AB and CD have identical lengths (AB equals CD), with perpendiculars OM onto AB and ON onto CD! By Theorem Five, perpendiculars bisect chords, meaning half-chord AM equals half of AB equals half of CD equals CN! Inside right triangles OAM and OCN, hypotenuse OA equals OC (radii) and leg AM equals CN! By RHS congruence, perpendicular distances OM and ON are strictly EQUAL! "
            "Flip it cleanly around for THEOREM SEVEN (Converse): IF TWO CHORDS IN A CIRCLE STAND EQUIDISTANT FROM THE CENTRE (distance OM equals ON), examine right triangles OAM and OCN again! Hypotenuses OA and OC are equal circle radii, while legs OM and ON are given equal! RHS congruence forces half-chords AM equals CN, immediately proving full chords AB and CD STRICTLY EQUAL in length!"
        ),
        "checkpoints": [
            {
                "question": "Suppose two chords PQ and RS of a circle sit at perpendicular distances OM = 5 cm and ON = 5 cm from Centre O. If PQ = 24 cm, what must RS equal by Theorem 7?",
                "options": [
                    "24 cm (chords equidistant from the centre are equal in length)",
                    "12 cm",
                    "10 cm",
                    "48 cm"
                ],
                "answer": 0,
                "hint": "Equal distances OM = ON imply equal half-chords PM = RN via RHS congruence!",
                "explanation": "Theorem 7 guarantees that chords equidistant from the centre are equal: RS = PQ = 24 cm."
            },
            {
                "question": "How is the perpendicular distance d of chord AB from Centre O algebraically linked to radius r and chord length L?",
                "options": [
                    "r² = (L/2)² + d²",
                    "r = L + d",
                    "L² = r² + d²",
                    "d² = r² + (L/2)²"
                ],
                "answer": 0,
                "hint": "Apply Pythagoras to right triangle OMA with hypotenuse r and legs L/2 and d!",
                "explanation": "Perpendicular OM bisects chord L into L/2, forming a right triangle with hypotenuse r: r² = (L/2)² + d²."
            }
        ]
    },
    {
        "id": 8,
        "title": "Chord Length Distance",
        "subtitle": "Section 5.6.1 Theorem 8: Longer Chords Lie Closer to the Centre (Diameter as Longest Chord with Distance Zero)",
        "speech": (
            "Now compare TWO UNEQUAL CHORDS inside the same circle in Section Five Point Six Point One! Which chord sits farther away from Centre O—the shorter chord or the longer chord? "
            "Picture pulling a rubber band horizontally downward across a circular plate! Right across the middle through Centre O—where perpendicular distance d equals ZERO—it stretches widest to form the DIAMETER! As you push the chord farther outward toward the rim, notice its perpendicular distance d from O grows larger while the chord shrinks shorter and shorter! "
            "Prove this rock-solid inverse relation in THEOREM EIGHT! Let chord AB be longer than chord CD (AB greater than CD), with perpendicular distances OM and ON! Compare right triangles OAM and OCN! Both share identical hypotenuse radius r (OA squared equals OC squared equals r squared)! "
            "Therefore half-chord AM squared plus perpendicular distance OM squared strictly equals CN squared plus ON squared! Since longer chord AB strictly exceeds shorter chord CD, half-chord AM squared STRICTLY EXCEEDS CN squared—which algebraically forces perpendicular distance ON squared STRICTLY GREATER THAN OM squared! Thus longer chords always sit much closer to Centre O, leaving the diameter (distance zero) as the undisputed longest possible chord!"
        ),
        "checkpoints": [
            {
                "question": "Inside the same circle, Chord AB has length 16 cm and Chord CD has length 10 cm. Which chord sits CLOSER to Centre O?",
                "options": [
                    "Chord AB sits closer to the centre (longer chord ⇒ smaller perpendicular distance d)",
                    "Chord CD sits closer to the centre",
                    "Both sit at the exact same distance",
                    "Chords cannot differ in length inside one circle"
                ],
                "answer": 0,
                "hint": "From (L/2)² + d² = r² (constant!), larger L/2 leaves smaller d!",
                "explanation": "By Theorem 8, longer chords have smaller perpendicular distance from O: since 16 cm > 10 cm, AB lies closer to O."
            },
            {
                "question": "Why does Theorem 8 prove that a diameter is always the LONGEST possible chord of any circle?",
                "options": [
                    "Because a diameter passes directly through Centre O, achieving the minimum possible perpendicular distance d = 0 (so L/2 = r, L = 2r)",
                    "Because diameters have negative perpendicular distance",
                    "Because every chord outside the centre exceeds 2r",
                    "Because d must exceed r"
                ],
                "answer": 0,
                "hint": "Maximize (L/2)² = r² − d² by making d² as small as possible!",
                "explanation": "Since d ≥ 0, chord length L = 2√(r² − d²) reaches its strict maximum 2r precisely when d = 0 (chord passes through O)."
            }
        ]
    }
]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 4: Quadrilaterals
Slides Data Generator - Part 2 (Slides 9 to 16)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Rhombus Equal Sides",
        "subtitle": "Section 4.4: Rhombus Definition, Compass Construction & Deduction 9 (Rhombus Is a Parallelogram)",
        "speech": (
            "Enter Section Four Point Four: Quadrilaterals with Equal Sidelengths! What happens when you push a SQUARE gently sideways so all FOUR sides stay IDENTICAL in length, yet corner angles tilt away from 90 degrees into tilted diamonds like 60° and 120°? Meet the RHOMBUS! "
            "Define RHOMBUS precisely: ANY quadrilateral whose FOUR SIDES ARE ALL EQUAL in length! Notice we didn't even mention parallel lines in the definition—yet watch Deduction Nine prove EVERY rhombus is AUTOMATICALLY A PARALLELOGRAM! Construct any rhombus ABCD cleanly first with a compass given angle A: mark equal side distances AB = AD = s along angle A's arms, then swing identical radius s arcs from BOTH B and D to intersect at C! "
            "Now trace Deduction Nine carefully step by step: draw straight diagonal AC splitting rhombus ABCD cleanly into triangles ABC and ADC! Since AB = AD, BC = DC, and diagonal AC stays common, SSS CONGRUENCE (triangle ABC congruent to triangle ADC) proves diagonal AC BISECTS corner angles A and C cleanly! Moreover matching alternate interior angles instantly prove opposite side AB runs PARALLEL to DC AND AD runs PARALLEL to BC—establishing cleanly EVERY rhombus automatically belongs squarely inside the Parallelogram family!"
        ),
        "checkpoints": [
            {
                "question": "In Deduction 9, how do we prove that EVERY rhombus (defined solely by 4 equal sides) is automatically a parallelogram?",
                "options": [
                    "Diagonal AC creates ΔABC ≅ ΔADC by SSS, making alternate interior angles equal so AB ∥ DC and AD ∥ BC!",
                    "Because all four angles are automatically 90°",
                    "Because opposite sides have unequal lengths",
                    "By assuming it is a rectangle first"
                ],
                "answer": 0,
                "hint": "Check SSS triangle congruence across diagonal AC to compare alternate interior angles!",
                "explanation": "SSS proves ΔABC ≅ ΔADC, equating alternate interior angles to establish parallel opposite sides cleanly."
            },
            {
                "question": "If one corner angle of a rhombus ABCD equals 70°, what are the remaining three angles ∠B, ∠C, and ∠D?",
                "options": [
                    "∠B = 110°,   ∠C = 70°,   ∠D = 110°",
                    "∠B = 90°,   ∠C = 70°,   ∠D = 90°",
                    "∠B = 70°,   ∠C = 110°,   ∠D = 110°",
                    "∠B = 140°,   ∠C = 70°,   ∠D = 140°"
                ],
                "answer": 0,
                "hint": "Since every rhombus IS a parallelogram, adjacent angles sum to 180° and opposite angles match!",
                "explanation": "Opposite ∠C = 70° and adjacent ∠B = ∠D = 180° − 70° = 110°."
            }
        ]
    },
    {
        "id": 10,
        "title": "Rhombus Diagonal Proofs",
        "subtitle": "Section 4.4: Deduction 10 (ΔGEO ≅ ΔMEO Perpendicular 90° Bisectors) & Multi-Set Venn Diagram",
        "speech": (
            "Conquer Deduction Ten and draw the complete MULTI-SET VENN DIAGRAM inside Section Four Point Four right now! First compare two intersecting diagonals GE and OM crossing at center O inside rhombus GAME! Because every rhombus is already a parallelogram (Deduction Nine), diagonal midpoint O ALREADY splits GO = EO AND MO = AO! "
            "Now inspect neighboring triangles GEO and MEO sharing common central segment EO! Outer side GE equals side ME (rhombus four equal sides), GO equals MO (diagonals bisect), and EO stays common! By SSS (or SAS) triangle congruence, triangle GEO is strictly congruent to triangle MEO—forcing angles EOG and EOM to match identically along straight diagonal line GM! Splitting straight 180 degrees equally yields NINETY DEGREES each! Thus RHOMBUS DIAGONALS ALWAYS BISECT EACH OTHER AT RIGHT ANGLES (90°), though diagonal lengths stay unequal unless it turns into a square! "
            "Inspect Section Four Point Four's complete multi-set Venn Diagram cleanly: draw ONE large outer Parallelogram oval containing TWO OVERLAPPING interior ovals inside—RECTANGLES (with four 90° corner angles) and RHOMBUSES (with four equal sides)! Notice their EXACT CENTER OVERLAP INTERSECTION REGION: ANY quadrilateral possessing BOTH four 90° angles AND four equal sides IS ALWAYS A SQUARE!"
        ),
        "checkpoints": [
            {
                "question": "In the multi-set Venn Diagram inside Parallelograms, which quadrilateral sits right in the EXACT INTERSECTION overlap of Rectangles AND Rhombuses?",
                "options": [
                    "Square  (combining 4 right angles from Rectangles AND 4 equal sides from Rhombuses)",
                    "General Trapezium",
                    "Oblique Kite",
                    "Scalene Triangle"
                ],
                "answer": 0,
                "hint": "Which shape satisfies BOTH conditions: Rectangle (4×90° corners) AND Rhombus (4 equal sides)?",
                "explanation": "Square = Rectangle ∩ Rhombus, inheriting equal AND perpendicular bisecting diagonals."
            },
            {
                "question": "What does Deduction 10 (ΔGEO ≅ ΔMEO via SSS) prove about the diagonals of ANY rhombus?",
                "options": [
                    "They bisect each other perpendicularly at 90° (forming four congruent right triangles around center O!)",
                    "They never bisect each other",
                    "They must always have equal total lengths",
                    "They cross at 45°"
                ],
                "answer": 0,
                "hint": "Check linear pair ∠EOG + ∠EOM = 180° when congruent triangles force ∠EOG = ∠EOM!",
                "explanation": "Equal adjacent linear-pair angles force 90° perpendicular bisection at center O."
            }
        ]
    },
    {
        "id": 11,
        "title": "Geoboard Diagonal Lab",
        "subtitle": "Section 4.5 Geoboard Activity: Controlling Diagonal Length & Intersection Angle to Generate Shapes",
        "speech": (
            "Jump straight into Section Four Point Five: Playing with Quadrilaterals! Imagine stretching colorful rubber bands tightly across a wooden dot-grid GEOBOARD to construct quadrilaterals NOT by tracing outer sides first, but by anchoring their CROSSING DIAGONALS first! Watch the magical master blueprint controlling FOUR famous quadrilateral families cleanly from just TWO diagonal dials: EQUALITY OF DIAGONAL LENGTHS and CENTRAL INTERSECTION ANGLE! "
            "Test every single peg combination on your dot-grid geoboard right now! Dial One: stretch TWO EQUAL bisecting rubber bands crossing perpendicularly at EXACT NINETY DEGREES! Connect all four endpoints—what snaps cleanly onto the wooden pegs? AN EXACT SQUARE! "
            "Dial Two: keep BOTH diagonal bands EQUAL and mutually bisecting, yet pivot their crossing angle AWAY from ninety degrees (say 60° or 70°)! Connecting the four vertices automatically builds an OBLONG RECTANGLE! "
            "Dial Three: stretch ONE LONG band and ONE SHORT band bisecting each other perpendicularly at NINETY DEGREES! Connecting those tips produces a crisp RHOMBUS! "
            "Dial Four: keep BOTH diagonal bands UNEQUAL in length and mutually bisecting cleanly at ANY oblique non-90° angle—instantly creating a general slanted PARALLELOGRAM! Interactive wooden pegboard geometry exercises make diagonal length and angle classification super visual and permanently unforgettable for every student!"
        ),
        "checkpoints": [
            {
                "question": "On a dot-grid geoboard, stretching two UNEQUAL diagonals that bisect each other at EXACT 90° right angles produces which quadrilateral?",
                "options": [
                    "A non-square Rhombus",
                    "A Rectangle",
                    "A Square",
                    "An Isosceles Trapezium"
                ],
                "answer": 0,
                "hint": "Perpendicular bisection makes all 4 sides equal (hypotenuses of 4 congruent right triangles!), while unequal lengths stop corners from hitting 90°!",
                "explanation": "Unequal perpendicular bisecting diagonals uniquely build a non-square rhombus."
            },
            {
                "question": "On a geoboard, stretching two EQUAL diagonals that bisect each other at a 70° oblique angle (NOT 90°) produces which quadrilateral?",
                "options": [
                    "A non-square Rectangle",
                    "A Square",
                    "A Rhombus",
                    "A Scalene Kite"
                ],
                "answer": 0,
                "hint": "Compare with the Carpenter's strip problem: equal bisecting diagonals ALWAYS guarantee four 90° corner angles!",
                "explanation": "Equal bisecting diagonals create a rectangle (only 90° diagonal crossing upgrades it to a square)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Joining Congruent Triangles",
        "subtitle": "Section 4.5 Joining Cutouts: Equilateral → Rhombus; Isosceles → Rhombus/Kite; Scalene → Parallelogram/Kite",
        "speech": (
            "Continue playing with quadrilaterals inside Section Four Point Five by cutting TWO IDENTICAL paper triangle cutouts and snapping matching equal edges cleanly together side by side! Watch carefully what surprising shapes pop out depending purely upon triangle classification AND WHICH pair of edges you glue together! "
            "Case One, Two Identical EQUILATERAL Triangles: since ALL three triangle edges share exact equal length s, joining ANY edge cleanly matches all four outer borders identically to length s! Result ALWAYS: AN EXACT EQUILATERAL RHOMBUS (specifically a crisp 60°-120° diamond rhombus)! "
            "Case Two, Two Identical ISOSCELES Triangles: carefully inspect WHICH side meets along the center seam! Joining along their symmetric equal-angle base edge places identical legs symmetrically around all four outer edges, forming a crisp equilateral RHOMBUS! Conversely, flipping carefully and pairing equal adjacent side legs symmetrically builds a classic flying KITE instead! "
            "Case Three, Two Identical SCALENE Triangles (three completely unequal edge lengths a, b, c): joining one shared diagonal seam edge with reversed 180-degree half-turn orientation places equal opposite edge pairs strictly parallel, always forming a PARALLELOGRAM; whereas mirror-reflecting both congruent scalene cutouts directly across a shared seam builds a symmetric KITE cleanly every single time without fail!"
        ),
        "checkpoints": [
            {
                "question": "Joining two identical EQUILATERAL triangle cutouts cleanly edge-to-edge ALWAYS produces which quadrilateral?",
                "options": [
                    "A Rhombus  (specifically with 60° and 120° corner angles!)",
                    "A Square",
                    "A Rectangle",
                    "A Trapezium"
                ],
                "answer": 0,
                "hint": "All 4 outer sides equal the equilateral side length s, while shared seam corners stay 60°!",
                "explanation": "All 4 outer edges share equal length s, producing a 60°–120° rhombus."
            },
            {
                "question": "Depending on orientation (reversed translation vs mirror reflection along a shared side), joining two identical SCALENE triangles produces which two possible quadrilaterals?",
                "options": [
                    "A Parallelogram (reversed orientation) or a Kite (mirror reflection)",
                    "A Square or a Rectangle",
                    "A Rhombus or a Square",
                    "A Circle or a Pentagon"
                ],
                "answer": 0,
                "hint": "Reversed match puts equal edges opposite (parallelogram); mirror reflection puts equal edges adjacent (kite)!",
                "explanation": "Scalene congruent triangles pair up either as a parallelogram (equal opposite sides) or a kite (equal adjacent pairs)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Kite Symmetric Geometry",
        "subtitle": "Section 4.6 Kite: Equal Adjacent Pairs (AB=BC, CD=DA) & Perpendicular Diagonal Bisection Proofs",
        "speech": (
            "Enter Section Four Point Six: Kite and Trapezium! Look upward at a classic paper diamond KITE soaring cleanly across the sky—what exact geometric property distinguishes a KITE from a parallelogram? Unlike parallelograms (equal OPPOSITE sides), a KITE has TWO DISTINCT PAIRS OF EQUAL ADJACENT SIDES: AB equals BC along its upper crown, AND CD equals DA along its lower tail! Note carefully: if all four edges happen to equal one length, a rhombus even qualifies as a special symmetric kite! "
            "Trace TWO crisp kite diagonal theorems cleanly via triangle congruence! First draw main symmetry spine BD linking crown vertex B to tail vertex D! Since AB = BC, AD = CD, and BD stays common, SSS CONGRUENCE proves triangle ABD is strictly congruent to triangle CBD! Instantly deduce: main diagonal BD BISECTS BOTH VERTEX ANGLES B and D cleanly, AND opposite wing angles A and C ALWAYS EQUAL EACH OTHER! "
            "Second check cross diagonal AC crossing BD at O: SAS congruence on top triangles AOB and COB proves AO = OC AND center crossing angles measure exact NINETY DEGREES! So a kite's main spine PERPENDICULARLY BISECTS the shorter cross-bar (though NOT vice versa unless it is a rhombus)!"
        ),
        "checkpoints": [
            {
                "question": "Which statement accurately defines a KITE and compares its diagonals carefully?",
                "options": [
                    "Two pairs of equal ADJACENT sides (AB=BC, CD=DA); the main diagonal bisects vertex angles and perpendicularly bisects the OTHER diagonal at 90°",
                    "Two pairs of equal OPPOSITE sides only; diagonals are always equal",
                    "Four 90° angles with unequal adjacent edges",
                    "Diagonals cross at 60° and never bisect"
                ],
                "answer": 0,
                "hint": "Notice ONLY the line of symmetry diagonal gets to bisect the cross-bar and both tip angles!",
                "explanation": "A kite has equal adjacent pairs AB=BC and CD=DA; its symmetry axis perpendicularly bisects the cross-diagonal and vertex angles."
            },
            {
                "question": "In kite ABCD with AB = BC and CD = DA, if wing angle ∠A = 108°, what MUST opposite wing angle ∠C equal?",
                "options": [
                    "108°   (since SSS congruence ΔABD ≅ ΔCBD guarantees ∠A = ∠C!)",
                    "72°",
                    "90°",
                    "54°"
                ],
                "answer": 0,
                "hint": "By reflection symmetry across main diagonal BD, ΔABD and ΔCBD are mirror-congruent!",
                "explanation": "ΔABD ≅ ΔCBD (SSS) proves the angles between unequal edges (∠A and ∠C) are strictly equal: 108°."
            }
        ]
    },
    {
        "id": 14,
        "title": "Trapezium And Isosceles",
        "subtitle": "Section 4.6 Trapezium (At Least 1 Parallel Pair, ∠S+∠P=180°) & Isosceles Trapezium Base Angles",
        "speech": (
            "Now inspect the final major quadrilateral family inside Section Four Point Six: TRAPEZIUMS! Define a TRAPEZIUM accurately using NCERT's modern inclusive standard: a quadrilateral featuring AT LEAST ONE PAIR OF PARALLEL OPPOSITE SIDES! Because 'at least one pair' includes 'two pairs', parallelograms even qualify peacefully under this inclusive umbrella while non-parallelogram trapeziums have ONLY ONE parallel base pair! "
            "Check transversal interior angle sums immediately along non-parallel leg SP connecting parallel top side PQ to bottom base SR: co-interior angles sitting along EITHER slanted leg ALWAYS sum cleanly to ONE HUNDRED EIGHTY DEGREES! So angle S plus angle P equals exact 180°, AND angle R plus angle Q equals exact 180°! "
            "Now add symmetric geometric elegance to construct an ISOSCELES TRAPEZIUM (named TUVW with parallel top side TU ∥ longer base side VW and EQUAL slanting non-parallel side legs TW = UV)! Drop neat perpendicular height lines or slide a parallel copy of leg TW from vertex U straight down to base VW: forming a crisp parallelogram alongside an ISOSCELES triangle proves base angles sitting opposite equal slanted legs MUST BE CONGRUENT (lower angle V equals exact angle W, AND upper interior angles U equals exact T)!"
        ),
        "checkpoints": [
            {
                "question": "In trapezium PQRS with PQ ∥ SR, if ∠S = 74° and ∠Q = 115°, compute ∠P and ∠R cleanly:",
                "options": [
                    "∠P = 106°  (180° − 74°),   ∠R = 65°  (180° − 115°)",
                    "∠P = 74°,   ∠R = 115°",
                    "∠P = 115°,   ∠R = 74°",
                    "∠P = 90°,   ∠R = 90°"
                ],
                "answer": 0,
                "hint": "Co-interior angles along EACH separate non-parallel leg sum to 180° (∠S + ∠P = 180° and ∠R + ∠Q = 180°)!",
                "explanation": "Same-side interior angles between parallel bases PQ ∥ SR sum to 180°: ∠P = 106°, ∠R = 65°."
            },
            {
                "question": "What extra symmetry defines an ISOSCELES trapezium TUVW (TU ∥ VW), and what follows about its base angles?",
                "options": [
                    "The two non-parallel legs are equal in length (TW = UV), forcing pairs of base angles equal (∠V = ∠W and ∠T = ∠U)!",
                    "All four sides are equal",
                    "Both pairs of opposite sides are parallel",
                    "Adjacent angles on the same base always differ by 90°"
                ],
                "answer": 0,
                "hint": "Recall congruent slanted legs mirror cleanly like an isosceles triangle with a sliced top!",
                "explanation": "Equal non-parallel legs establish congruent base angles (∠V = ∠W and ∠T = ∠U) plus equal diagonals."
            }
        ]
    },
    {
        "id": 15,
        "title": "Square Inside Square",
        "subtitle": "Section 4.6 Figure It Out: Tilted Inner Square Proofs, Venn Logic & True/False Geometric Reasoning",
        "speech": (
            "Tackle Section Four Point Six's signature 'Figure it Out' puzzles right now: SQUARE-IN-A-SQUARE CONSTRUCTIONS and TRUE-FALSE LOGIC CHECKS! "
            "Picture outer square ABCD, and mark points P, Q, R, S along edges AB, BC, CD, and DA at IDENTICAL split distance x from each corner (so AP = BQ = CR = DS = x, leaving remaining segments PB = QC = RD = SA = y)! Connect P to Q, Q to R, R to S, and S back to P! What shape ALWAYS sits tilted symmetrically inside? PROVE IT IS AN EXACT SQUARE! "
            "Check right triangles SAP, PBQ, QCR, and RDS inside all four outer square corners cleanly: EVERY outer corner holds ninety degrees, EVERY short leg measures exact length x, and EVERY long leg measures exact length y! By SAS CONGRUENCE, all four corner triangles are strictly identical—forcing all four tilted hypotenuses PQ = QR = RS = SP (four equal sides)! Moreover sharp complementary acute angles add up nicely to ninety degrees along each outer edge (180° − 90° = 90°), locking EVERY inner corner at exact NINETY DEGREES! "
            "Finally check classic True/False hierarchy traps carefully: Every square is a rhombus (TRUE); Every rhombus is a square (FALSE); Every parallelogram has perpendicular diagonals (FALSE—only rhombuses and squares guarantee 90° crossing)!"
        ),
        "checkpoints": [
            {
                "question": "Points P, Q, R, S split edges AB, BC, CD, DA of outer square ABCD identically (AP = BQ = CR = DS = x). Why MUST inner quadrilateral PQRS ALWAYS be a SQUARE?",
                "options": [
                    "SAS proves all 4 corner right triangles congruent (giving 4 equal hypotenuses PQ = QR = RS = SP), and complementary acute angles force each inner corner to equal 90°!",
                    "Because P, Q, R, S connect to center O only",
                    "Because PQRS has only two equal sides",
                    "Because outer angles sum to 180°"
                ],
                "answer": 0,
                "hint": "Check triangle legs (x, y with 90° corner) for equal sides, then check linear pair at P: α + inner∠ + (90° − α) = 180°!",
                "explanation": "Four congruent SAS corner right triangles give equal hypotenuses and 180° − (α + 90°−α) = 90° inner angles."
            },
            {
                "question": "Which True/False classification check across Chapter 4 quadrilateral families is 100% ACCURATE?",
                "options": [
                    "'Every rectangle is a parallelogram' = TRUE;   'Every parallelogram is a rectangle' = FALSE",
                    "'Every rhombus is a square' = TRUE",
                    "'Every trapezium is a parallelogram' = TRUE",
                    "'Every kite has parallel opposite sides' = TRUE"
                ],
                "answer": 0,
                "hint": "Check direction carefully: specialized shapes inherit parent traits (Square → Rectangle → Parallelogram), NEVER the reverse!",
                "explanation": "All rectangles have 2 pairs of parallel sides (Parallelogram), whereas slanted parallelograms lack 90° corners."
            }
        ]
    },
    {
        "id": 16,
        "title": "Which Quad Summary",
        "subtitle": "Chapter Consolidation Hierarchy Matrix & Puzzle Time ('Which Quad?' Paper-Folding & Corner Cuts)",
        "speech": (
            "Congratulations on mastering NCERT Class Eight Chapter Four: Quadrilaterals! Lock all six quadrilateral families cleanly into ONE crystal-clear comparison hierarchy right now before tackling forty Mastery Quiz questions and 'Which Quad?' paper folding! "
            "Check our complete Master Summary Checklist cleanly: First, ALL closed 4-sided polygons sum strictly to 360° interior angles! Second, TRAPEZIUM has at least one parallel side pair (isosceles trapezium adds equal slanted legs alongside congruent base angles)! Third, PARALLELOGRAM has two parallel pairs, equal opposite sides, equal opposite angles, supplementary adjacent angles, and mutually bisecting diagonals! Fourth, RECTANGLE upgrades every corner angle to 90° AND makes bisecting diagonals EQUAL! Fifth, RHOMBUS makes all 4 sides equal AND makes bisecting diagonals PERPENDICULAR (90°)! Sixth, SQUARE unites Rectangle plus Rhombus—equal perpendicular bisecting diagonals splitting 45° corners! Seventh, KITE pairs equal adjacent edges with ONE perpendicular symmetry diagonal spine! "
            "Try IT'S PUZZLE TIME—Which Quad? activity right now: Fold a clean rectangular sheet carefully along perpendicular centerline axes or tilted diagonal creases, snip crisp straight edge cuts cleanly across folded outer sheet corners, and carefully unfold the folded paper symmetrically to reveal exact equilateral rhombuses, symmetric flying kites, isosceles trapeziums, and nested tilted interior squares instantaneously!"
        ),
        "checkpoints": [
            {
                "question": "Which single quadrilateral possesses BOTH equal diagonals (like a Rectangle) AND perpendicular bisecting diagonals (like a Rhombus)?",
                "options": [
                    "A Square",
                    "A non-square Rectangle",
                    "A non-square Rhombus",
                    "An Isosceles Trapezium"
                ],
                "answer": 0,
                "hint": "Which shape sits at Rectangle ∩ Rhombus and inherits EVERY diagonal property simultaneously?",
                "explanation": "Only a Square guarantees diagonals that are equal in length, bisect each other, AND intersect at 90°."
            },
            {
                "question": "In the 'Which Quad?' paper-folding puzzle, folding a rectangular sheet twice along BOTH perpendicular centerlines (quadrant fold) and making ONE straight diagonal slant cut across the closed corner unfolds into which exact quadrilateral?",
                "options": [
                    "A Rhombus  (4 equal slanted cut edges with 2 perpendicular lines of symmetry along the fold creases!)",
                    "A Scalene Triangle",
                    "An Open Pentagon",
                    "A Trapezium with unequal non-parallel sides"
                ],
                "answer": 0,
                "hint": "Two perpendicular mirror fold lines become perpendicular bisecting diagonals, making all 4 unfolded cut edges equal!",
                "explanation": "Reflecting one straight slant across two perpendicular axes builds 4 equal sides around 90° bisecting diagonals = a Rhombus (or Square if cut at 45°)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch4 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")

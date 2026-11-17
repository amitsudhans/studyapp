#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 12: Quadrilaterals
Part 2: Slides 9 to 16 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Centroid Median Theorem",
        "subtitle": "Section 12.3.2 Applications of Midpoint Theorem: Centroid Concurrency & 2:1 Ratio",
        "speech": (
            "Welcome to Slide Nine, where we prove Theorem Eight on the centroid of a triangle! A median connects a "
            "vertex to the midpoint of the opposite side. Remarkably, all three medians of any triangle meet at a single "
            "point called the centroid G, dividing each median in the ratio two to one from vertex to midpoint! "
            "Let us prove this using the Midpoint Theorem! Draw medians BE and CF intersecting at G, where E is the "
            "midpoint of AC and F is the midpoint of AB. Mark P as the midpoint of BG and Q as the midpoint of CG! "
            "In triangle ABC, FE joins midpoints of AB and AC, so FE is parallel to BC and equals half of BC! In "
            "triangle GBC, PQ joins midpoints of GB and GC, so PQ is also parallel to BC and equals half of BC! "
            "Therefore FE and PQ are equal and parallel, making FEQP a parallelogram! "
            "Because diagonals FQ and PE of parallelogram FEQP bisect each other at G, we have PG equals GE and QG "
            "equals GF! Since P is the midpoint of BG, BP equals PG equals GE—so BG equals twice GE! Repeating with "
            "median AD proves all three medians concur at G in the exact ratio two to one!"
        ),
        "checkpoints": [
            {
                "question": "If median AD of ∆ABC has total length 18 cm, what is the distance from vertex A to centroid G?",
                "options": ["6 cm", "9 cm", "12 cm", "15 cm"],
                "answer": 2,
                "hint": "Centroid G divides AD in the ratio AG : GD = 2 : 1 from vertex to midpoint.",
                "explanation": "AG = (2/3) × 18 cm = 12 cm, while GD = 6 cm.",
            },
            {
                "question": "Which theorem directly proves that FE and PQ are both parallel to BC and equal to ½BC in the centroid proof?",
                "options": [
                    "SSS Congruence",
                    "Theorem 6 (Midpoint Theorem)",
                    "Thales Circle Theorem",
                    "Angle Sum Property",
                ],
                "answer": 1,
                "hint": "FE joins midpoints in ∆ABC and PQ joins midpoints in ∆GBC!",
                "explanation": "Applying Theorem 6 (Midpoint Theorem) to ∆ABC gives FE ∥ BC, FE = ½BC, and to ∆GBC gives PQ ∥ BC, PQ = ½BC.",
            },
        ],
    },
    {
        "id": 10,
        "title": "Varignon Parallelogram Theorem",
        "subtitle": "Section 12.3.2 Applications of Midpoint Theorem: Midpoint Quadrilateral PQRS",
        "speech": (
            "On Slide Ten, we explore Pierre Varignon's stunning Theorem Nine, published in seventeen thirty-one! Take "
            "ANY planar quadrilateral ABCD—whether convex, non-convex, irregular, or kite-shaped—and mark the midpoints "
            "P, Q, R, and S of sides AB, BC, CD, and DA! When you connect P to Q, Q to R, R to S, and S back to P, "
            "the inner quadrilateral PQRS is ALWAYS, without exception, a parallelogram! "
            "Why does perfect order emerge from arbitrary chaos? Draw diagonal AC, splitting ABCD into triangles ABC "
            "and ADC! In triangle ABC, P and Q are midpoints of AB and BC, so by the Midpoint Theorem, PQ is parallel "
            "to AC and equals half of AC! In triangle ADC, S and R are midpoints of AD and DC, so SR is also parallel "
            "to AC and equals half of AC! Thus PQ and SR are parallel and equal in length! By Theorem Five, PQRS is "
            "guaranteed to be a parallelogram! "
            "Even better, drawing diagonal BD shows QR equals PS equals half of BD—so the perimeter of PQRS equals "
            "AC plus BD, and its area is ALWAYS half the area of ABCD! Test special cases in the simulator: equal "
            "diagonals yield a rhombus, perpendicular diagonals yield a rectangle, and both yield a square!"
        ),
        "checkpoints": [
            {
                "question": "If the diagonals of quadrilateral ABCD measure 14 cm and 20 cm, what is the perimeter of its Varignon parallelogram?",
                "options": ["17 cm", "34 cm", "68 cm", "280 cm"],
                "answer": 1,
                "hint": "Opposite pairs of Varignon sides equal ½AC and ½BD!",
                "explanation": "Perimeter = 2(½AC) + 2(½BD) = AC + BD = 14 + 20 = 34 cm.",
            },
            {
                "question": "If the diagonals of quadrilateral ABCD are equal AND perpendicular, what shape is the Varignon parallelogram?",
                "options": ["Kite", "Trapezium", "Square", "Scalene parallelogram"],
                "answer": 2,
                "hint": "Equal diagonals make all 4 Varignon sides equal; perpendicular diagonals make adjacent sides meet at 90°.",
                "explanation": "Equal sides plus right angles produce a square.",
            },
        ],
    },
    {
        "id": 11,
        "title": "Plane Tessellation Rotations",
        "subtitle": "Section 12.4 Tiling the Plane Using Any 4-Gon: Method 1 (180° Midpoint Rotations)",
        "speech": (
            "Welcome to Slide Eleven and Section Twelve Point Four: Tiling the Plane Using Any Four-Gon! You already "
            "know that squares and rectangles tile a floor effortlessly! What about an awkward, lopsided, or even "
            "non-convex dart-shaped quadrilateral? Remarkably, EVERY planar quadrilateral tiles the entire infinite "
            "plane with zero gaps and zero overlaps! "
            "Let us study Method One: successive one-hundred-eighty-degree rotations around edge midpoints! Take any "
            "quadrilateral ABCD and locate the midpoint M of side BC! Rotate the tile by one hundred eighty degrees "
            "about M! Because M is the midpoint, vertex B swaps with vertex C, so the rotated edge fits flush against "
            "the original edge BC with zero gap! Next, repeat this one-hundred-eighty-degree rotation around the "
            "midpoints of all four edges! "
            "Look closely at what meets around any single vertex of the tiling: exactly one copy each of interior angles "
            "A, B, C, and D! Because the interior angles of EVERY planar quadrilateral sum to exactly three hundred sixty "
            "degrees, those four angles complete a full circle around every vertex! Even a non-convex quadrilateral with "
            "a reflex angle over one hundred eighty degrees tiles cleanly, because its four angles still sum to three "
            "hundred sixty degrees! Experiment with the rotation lab to grow a seamless infinite mosaic!"
        ),
        "checkpoints": [
            {
                "question": "Why do four copies of any planar quadrilateral meet without gaps or overlaps around a vertex under 180° edge-midpoint rotations?",
                "options": [
                    "All sides become equal after rotation",
                    "Angles A, B, C, and D meet once each and sum to 360°",
                    "Only convex shapes can rotate 180°",
                    "Each angle is 90° on average",
                ],
                "answer": 1,
                "hint": "Check which four angles gather around each shared vertex!",
                "explanation": "Rotating 180° about adjacent edge midpoints places ∠A, ∠B, ∠C, and ∠D around one vertex, summing to 360°.",
            },
            {
                "question": "Does a non-convex quadrilateral with an interior angle of 220° tile the plane by 180° midpoint rotations?",
                "options": [
                    "No, reflex angles always overlap",
                    "Yes, because its four interior angles still sum to 360°",
                    "Only if it has parallel sides",
                    "Only if two sides are equal",
                ],
                "answer": 1,
                "hint": "Does the 360° interior angle sum still hold for non-convex planar 4-gons?",
                "explanation": "Yes! Non-convex planar 4-gons still satisfy ∠A + ∠B + ∠C + ∠D = 360°, so they tile without gaps.",
            },
        ],
    },
    {
        "id": 12,
        "title": "Varignon Grid Tessellation",
        "subtitle": "Section 12.4 Tiling the Plane: Method 2 (Varignon Grid), Quasicrystals & Hat Monotile",
        "speech": (
            "On Slide Twelve, we explore Method Two for quadrilateral tiling via Varignon's parallelogram, and connect "
            "it to Nobel Prize winning science! Inside any quadrilateral ABCD, draw its Varignon parallelogram PQRS! "
            "Notice that ABCD consists of PQRS in the centre plus four corner triangles at A, B, C, and D! When you "
            "rotate ABCD by one hundred eighty degrees around midpoints P, Q, R, and S, the corner triangles fold "
            "outward to match neighbouring tiles, forming a repeating translation grid whose fundamental parallelogram "
            "unit has twice the area of PQRS! "
            "Now zoom out to modern mathematics and physics! Every quadrilateral tiling we just built is PERIODIC, "
            "meaning you can shift the entire pattern sideways and it lands right back on itself! For centuries, "
            "scientists assumed all atomic crystals had periodic tilings! Then in nineteen eighty-two, Dan Shechtman "
            "discovered QUASICRYSTALS—real metallic alloys whose atoms pack in ordered, non-repeating aperiodic "
            "patterns, earning him the twenty-eleven Nobel Prize in Chemistry! "
            "Even more recently, in twenty twenty-three, mathematicians solved a sixty-year-old geometry puzzle by "
            "discovering the HAT MONOTILE—a single thirteen-sided polygon that tiles the entire infinite plane ONLY "
            "aperiodically, never repeating its pattern by any simple translation shift anywhere across the infinite plane!"
        ),
        "checkpoints": [
            {
                "question": "What did Dan Shechtman win the 2011 Nobel Prize in Chemistry for discovering?",
                "options": [
                    "The Varignon parallelogram",
                    "Quasicrystals with ordered, non-periodic atomic tilings",
                    "The 2023 hat monotile",
                    "Cubic crystal lattices",
                ],
                "answer": 1,
                "hint": "His 1982 discovery overturned the assumption that all crystals repeat periodically!",
                "explanation": "Dan Shechtman discovered quasicrystals—ordered atomic structures with aperiodic, non-repeating patterns.",
            },
            {
                "question": "What makes the 2023 'hat' monotile historically special in geometry?",
                "options": [
                    "It is a regular pentagon",
                    "It is a single shape that tiles the plane only aperiodically",
                    "It cannot tile the plane at all",
                    "It has four equal sides",
                ],
                "answer": 1,
                "hint": "It solved the 'einstein' (one stone) tiling problem!",
                "explanation": "The 13-sided 'hat' monotile covers the infinite plane with no gaps or overlaps, yet never repeats periodically.",
            },
        ],
    },
    {
        "id": 13,
        "title": "Linkages Bisector Proofs",
        "subtitle": "Exercises 12.1 & 12.2: 4-Bar Parallelogram Linkages & Angle Bisector Rectangle Proof",
        "speech": (
            "Welcome to Slide Thirteen, where we tackle two flagship problems from Exercises Twelve Point One and Twelve "
            "Point Two! First, consider a mechanical four-bar linkage made of four rigid bars pinned at their ends, with "
            "opposite bars equal: AB equals CD and BC equals DA! As you push bar AB, the linkage flexes smoothly, yet "
            "by Theorem Two, opposite sides remain equal, so ABCD stays a parallelogram at every angle—until you push "
            "it past flat into a crossed BOWTIE configuration! That crossed bowtie is self-intersecting, demonstrating "
            "vividly why our formal definition of a planar quadrilateral forbids intersecting non-adjacent edges! "
            "Second, let us prove a classic NCERT exercise: the internal angle bisectors of ANY parallelogram ABCD "
            "always enclose a rectangle! Let the bisectors of adjacent angles A and B meet at point P! Since AD is "
            "parallel to BC, co-interior angles A and B sum to one hundred eighty degrees! Dividing both sides by two, "
            "half of angle A plus half of angle B equals ninety degrees! In triangle APB, the angle at P must therefore "
            "be one hundred eighty minus ninety, which is ninety degrees! By the exact same argument at all four "
            "intersections, every interior angle is ninety degrees, proving the enclosed figure is a rectangle!"
        ),
        "checkpoints": [
            {
                "question": "Why do the internal angle bisectors of two adjacent vertices of a parallelogram meet at 90°?",
                "options": [
                    "All sides of a parallelogram are equal",
                    "Adjacent angles sum to 180°, so their halves sum to 90°",
                    "Diagonals bisect the angles",
                    "Opposite angles are complementary",
                ],
                "answer": 1,
                "hint": "Co-interior angles on parallel lines satisfy ∠A + ∠B = 180°.",
                "explanation": "Since ½∠A + ½∠B = 90°, the third angle in ∆APB must be 180° − 90° = 90°.",
            },
            {
                "question": "When a four-bar parallelogram linkage flips into a bowtie shape, which quadrilateral condition is violated?",
                "options": [
                    "Planarity",
                    "Closure",
                    "Non-self-intersection",
                    "Four vertices",
                ],
                "answer": 2,
                "hint": "Look at what happens to the two opposite bars in a bowtie!",
                "explanation": "In a crossed bowtie, two non-adjacent bars cross each other, violating non-self-intersection.",
            },
        ],
    },
    {
        "id": 14,
        "title": "Varignon Scissors Folding",
        "subtitle": "Exercise 12.3: Varignon Special Cases, Scissors Congruence & Triangle Paper Folding",
        "speech": (
            "On Slide Fourteen, we explore Exercise Twelve Point Three through Varignon special cases and hands-on "
            "scissors congruence! Remember that a rhombus has perpendicular diagonals while a rectangle has equal "
            "diagonals! When you join the midpoints of a rectangle's sides, its equal diagonals force all four Varignon "
            "sides to have equal length, producing a RHOMBUS! Conversely, when you join the midpoints of a rhombus's "
            "sides, its perpendicular diagonals force all four Varignon angles to be ninety degrees, producing a "
            "RECTANGLE! "
            "Next, explore scissors congruence and paper folding using the Midpoint Theorem! Take any triangle ABC, "
            "draw midline DE connecting the midpoints of AB and AC, and cut off the top triangle ADE! Rotate that small "
            "triangle by one hundred eighty degrees around midpoint E and place it beside trapezoid DBCE! Instantly, "
            "the two pieces lock together into a parallelogram with the exact same area as triangle ABC! "
            "Even better, fold vertex A down to the base along midline DE, and fold vertices B and C inward to meet A! "
            "All three interior angles sit side by side along a straight line of one hundred eighty degrees, while "
            "forming a neat double-layered rectangle whose area is half the original triangle!"
        ),
        "checkpoints": [
            {
                "question": "What quadrilateral is formed by joining the midpoints of the sides of a rectangle?",
                "options": ["Rectangle", "Rhombus", "Trapezium", "Kite"],
                "answer": 1,
                "hint": "A rectangle's diagonals are equal—how do Varignon's side lengths depend on the diagonals?",
                "explanation": "Each Varignon side equals half a diagonal; equal diagonals make all four Varignon sides equal, forming a rhombus.",
            },
            {
                "question": "When you cut ∆ABC along its midline DE and rotate ∆ADE 180° around E, what shape is formed?",
                "options": [
                    "A larger triangle",
                    "A parallelogram of equal area",
                    "A regular pentagon",
                    "A circle sector",
                ],
                "answer": 1,
                "hint": "Midline DE is parallel to BC and half its length!",
                "explanation": "Rotating ∆ADE 180° around E aligns AE with EC and makes the top edge equal and parallel to BC, forming a parallelogram.",
            },
        ],
    },
    {
        "id": 15,
        "title": "Trisection Diagonals Skew",
        "subtitle": "Exercises 12.3 & 12.4: Trapezium Midsegment, Trisection, n(n−3)/2 & Skew 4-Gons",
        "speech": (
            "Welcome to Slide Fifteen, covering four gem problems from Exercises Twelve Point Three and Twelve Point "
            "Four! First, in any trapezium with parallel bases a and b, the midsegment joining the midpoints of the "
            "two non-parallel sides is parallel to both bases and has length half of a plus b! You prove this in one "
            "step by drawing a diagonal and applying the Midpoint Theorem to each triangle! "
            "Second, the Converse Midpoint Theorem lets us trisect—or divide into any n equal parts—a segment AB! "
            "Draw an auxiliary ray from A, step off three equal compass arcs, connect the third mark to B, and draw "
            "parallels through the other marks back to AB! "
            "Third, how many diagonals does an n-sided polygon have? Each of the n vertices connects to n minus three "
            "non-adjacent vertices, and dividing by two avoids double-counting, giving n times n minus three over "
            "two—which gives two diagonals for a quadrilateral and nine for a hexagon! "
            "Finally, what happens if a four-gon is non-planar, or skew, bent out of the plane along its diagonal? "
            "Folding in three dimensions reduces the corner angles, making the interior angle sum of a skew "
            "quadrilateral strictly LESS than three hundred sixty degrees!"
        ),
        "checkpoints": [
            {
                "question": "A trapezium has parallel bases of lengths 10 cm and 18 cm. What is the length of its midsegment?",
                "options": ["8 cm", "14 cm", "28 cm", "90 cm"],
                "answer": 1,
                "hint": "Use the trapezium midsegment formula m = ½(a + b).",
                "explanation": "m = ½(10 + 18) = ½(28) = 14 cm.",
            },
            {
                "question": "How many diagonals does a convex hexagon (n = 6) have?",
                "options": ["6", "9", "12", "18"],
                "answer": 1,
                "hint": "Substitute n = 6 into n(n − 3)/2.",
                "explanation": "6 × (6 − 3) / 2 = 6 × 3 / 2 = 9 diagonals.",
            },
        ],
    },
    {
        "id": 16,
        "title": "Chapter Quadrilaterals Summary",
        "subtitle": "Complete Chapter 12 Synthesis: Definitions, Theorems 2–9 & Universal Plane Tiling",
        "speech": (
            "Congratulations on reaching Slide Sixteen, our complete synthesis of Chapter Twelve: Quadrilaterals! Step "
            "back and admire how every theorem in this chapter locks together like precision clockwork! "
            "First, we built a rock-solid definition of a planar quadrilateral by ruling out collinear points, open "
            "chains, crossed bowties, and non-planar skew shapes, and we contrasted convex shapes with non-convex "
            "dented shapes! "
            "Second, we proved four powerful converse tests—Theorems Two through Five—giving four distinct ways to "
            "certify a parallelogram: equal opposite sides, equal opposite angles, bisecting diagonals, or a single "
            "pair of equal and parallel sides! "
            "Third, we unlocked the Midpoint Theorem and its converse, powering James Watt's parallel motion linkage, "
            "triangle centroid concurrency in the two-to-one ratio, trapezium midsegments, segment trisection, and "
            "Pierre Varignon's universal parallelogram theorem! "
            "Finally, we saw how the three-hundred-sixty-degree interior angle sum lets ANY planar quadrilateral—whether "
            "convex or non-convex—tile the infinite plane via one-hundred-eighty-degree edge-midpoint rotations or "
            "Varignon translation grids, bridging school geometry to Dan Shechtman's Nobel-winning quasicrystals and "
            "the twenty-twenty-three hat monotile! You are now completely ready to test your geometry mastery across all "
            "four silent interactive quiz challenges on Slides Seventeen through Twenty—read every question carefully, think logically, and enjoy the challenge!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following is NOT one of the four sufficient tests (Theorems 2–5) for a quadrilateral to be a parallelogram?",
                "options": [
                    "Both pairs of opposite sides are equal",
                    "Diagonals bisect each other",
                    "One pair of opposite sides is equal and the other pair is parallel",
                    "One pair of opposite sides is both equal and parallel",
                ],
                "answer": 2,
                "hint": "Think of an isosceles trapezium!",
                "explanation": "An isosceles trapezium has one pair of parallel sides and the other pair equal, yet it is not a parallelogram.",
            },
            {
                "question": "Which theorem guarantees that the midpoints of ANY planar quadrilateral form a parallelogram?",
                "options": [
                    "Theorem 2 (Opposite Sides)",
                    "Theorem 8 (Centroid)",
                    "Theorem 9 (Varignon's Theorem)",
                    "Theorem 3 (Opposite Angles)",
                ],
                "answer": 2,
                "hint": "Named after French mathematician Pierre Varignon!",
                "explanation": "Theorem 9 (Varignon's Theorem) proves that joining consecutive side midpoints of any planar 4-gon always yields a parallelogram.",
            },
        ],
    },
]

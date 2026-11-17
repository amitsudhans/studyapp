#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 12: Quadrilaterals
Part 3: Slides 17 to 20 (Silent Mastery Quiz Slides - 40 Questions with 3-Step Solutions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Definitions Convexity Quiz",
        "subtitle": "Mastery Quiz 1 (Silent Exercise): Formal Definition, Convexity & Diagonals (Section 12.1)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which condition is violated by a figure formed by 4 points where 3 of them lie on the same straight line?",
                "options": [
                    "Planarity",
                    "No three vertices are collinear",
                    "Non-self-intersection",
                    "Closed path",
                ],
                "answer": 1,
                "solution_steps": [
                    "A valid quadrilateral requires 4 vertices such that no three are collinear.",
                    "If 3 vertices are collinear, two sides merge into a straight line and the figure collapses into a triangle.",
                    "Therefore, the non-collinearity condition is violated.",
                ],
            },
            {
                "question": "How many pairs of non-adjacent edges may intersect in a valid planar quadrilateral?",
                "options": ["0", "1", "2", "4"],
                "answer": 0,
                "solution_steps": [
                    "By definition, a planar quadrilateral is non-self-intersecting.",
                    "Only adjacent edges may meet at their shared vertex; opposite edges must never cross.",
                    "Hence, 0 pairs of non-adjacent edges may intersect.",
                ],
            },
            {
                "question": "Which statement is always true for every convex quadrilateral?",
                "options": [
                    "All four angles are acute",
                    "All four interior angles are strictly less than 180°",
                    "Its diagonals are always equal",
                    "Its diagonals always bisect at 90°",
                ],
                "answer": 1,
                "solution_steps": [
                    "A quadrilateral is convex if and only if every interior angle is strictly less than 180°.",
                    "Diagonals need not be equal or perpendicular in general convex 4-gons.",
                    "Therefore, all four interior angles being less than 180° is always true.",
                ],
            },
            {
                "question": "What is the interior angle sum of a non-convex (dart-shaped) planar quadrilateral?",
                "options": ["180°", "270°", "360°", "540°"],
                "answer": 2,
                "solution_steps": [
                    "Draw the internal diagonal from the reflex vertex to the opposite vertex.",
                    "This splits any non-convex planar 4-gon into two triangles.",
                    "Each triangle has angle sum 180°, so total sum = 180° + 180° = 360°.",
                ],
            },
            {
                "question": "If three interior angles of a planar quadrilateral are 40°, 35°, and 55°, what is the fourth angle and shape type?",
                "options": [
                    "230°, non-convex",
                    "130°, convex",
                    "230°, convex",
                    "130°, non-convex",
                ],
                "answer": 0,
                "solution_steps": [
                    "Sum of the three given angles = 40° + 35° + 55° = 130°.",
                    "Fourth angle = 360° − 130° = 230°.",
                    "Since 230° > 180°, the quadrilateral is non-convex.",
                ],
            },
            {
                "question": "In a non-convex quadrilateral ABCD with reflex angle at C (> 180°), where does diagonal BD lie?",
                "options": [
                    "Completely inside ABCD",
                    "Completely outside ABCD",
                    "Along side AB",
                    "Intersecting AC inside ABCD",
                ],
                "answer": 1,
                "solution_steps": [
                    "The reflex vertex C creates an inward dent between B and D.",
                    "Connecting B to D bridges across the outside dent.",
                    "Thus, diagonal BD lies completely outside the quadrilateral.",
                ],
            },
            {
                "question": "Do the two diagonals of a non-convex quadrilateral intersect each other?",
                "options": [
                    "Yes, always at their midpoints",
                    "Yes, always inside the shape",
                    "No, one is interior and one is exterior",
                    "Only when three sides are equal",
                ],
                "answer": 2,
                "solution_steps": [
                    "In a non-convex 4-gon, one diagonal lies inside the shape and the other lies outside.",
                    "Because their interiors are separated by the boundary, the segments cannot cross.",
                    "Therefore, the diagonals do not intersect.",
                ],
            },
            {
                "question": "Which real-world object represents a non-planar (skew) 4-gon?",
                "options": [
                    "A flat rectangular windowpane",
                    "A folded paper kite bent out of a single plane",
                    "A painted crosswalk stripe",
                    "A flat square tile",
                ],
                "answer": 1,
                "solution_steps": [
                    "A planar 4-gon has all four vertices in one flat 2D plane.",
                    "Bending a kite out of the plane puts its vertices in 3D space without a common plane.",
                    "Hence, it is a non-planar (skew) 4-gon.",
                ],
            },
            {
                "question": "In a convex quadrilateral, the angles are x, 2x, 3x, and 4x. Find the largest angle.",
                "options": ["36°", "72°", "108°", "144°"],
                "answer": 3,
                "solution_steps": [
                    "Sum of angles: x + 2x + 3x + 4x = 10x = 360°.",
                    "Solving gives x = 36°.",
                    "Largest angle = 4x = 4 × 36° = 144° (< 180°, so convex).",
                ],
            },
            {
                "question": "Why does a crossed bowtie shape fail to be a valid planar quadrilateral?",
                "options": [
                    "It has 5 vertices",
                    "Its opposite edges intersect at a non-vertex point",
                    "Its angles sum to 720°",
                    "It has no diagonals",
                ],
                "answer": 1,
                "solution_steps": [
                    "A bowtie has 4 vertices, but two non-adjacent edges cross each other.",
                    "Planar quadrilaterals must be non-self-intersecting.",
                    "Thus, it violates the non-self-intersection requirement.",
                ],
            },
        ],
    },
    {
        "id": 18,
        "title": "Parallelogram Tests Quiz",
        "subtitle": "Mastery Quiz 2 (Silent Exercise): Theorems 2–5 & Congruence Proofs (Section 12.2)",
        "is_quiz": True,
        "questions": [
            {
                "question": "Which congruence criterion proves Theorem 2 (if both pairs of opposite sides are equal, ABCD is a parallelogram)?",
                "options": ["ASA", "SSS", "RHS", "SAS"],
                "answer": 1,
                "solution_steps": [
                    "Draw diagonal AC to split ABCD into ∆ABC and ∆CDA.",
                    "We have AB = CD, BC = DA, and AC = CA (common side).",
                    "By SSS congruence, ∆ABC ≅ ∆CDA, yielding equal alternate interior angles and parallel sides.",
                ],
            },
            {
                "question": "In Theorem 3 (opposite angles equal: ∠A = ∠C and ∠B = ∠D), what does 2∠A + 2∠B = 360° simplify to?",
                "options": [
                    "∠A + ∠B = 90°",
                    "∠A + ∠B = 180°",
                    "∠A = ∠B",
                    "∠A − ∠B = 90°",
                ],
                "answer": 1,
                "solution_steps": [
                    "Interior angle sum gives ∠A + ∠B + ∠C + ∠D = 360°.",
                    "Substituting ∠C = ∠A and ∠D = ∠B gives 2∠A + 2∠B = 360°.",
                    "Dividing by 2 gives ∠A + ∠B = 180° (co-interior angles supplementary ⇒ AD ∥ BC).",
                ],
            },
            {
                "question": "Which congruence criterion proves Theorem 4 (diagonals bisect each other ⇒ parallelogram)?",
                "options": ["SSS", "SAS", "ASA", "RHS"],
                "answer": 1,
                "solution_steps": [
                    "Let diagonals AC and BD bisect at O, so OA = OC and OB = OD.",
                    "Vertically opposite angles ∠AOB and ∠COD are equal.",
                    "By SAS congruence, ∆AOB ≅ ∆COD, giving equal alternate angles and parallel opposite sides.",
                ],
            },
            {
                "question": "In Theorem 5, if AB = CD and AB ∥ CD in quadrilateral ABCD, which triangle congruence proves AD ∥ BC?",
                "options": ["SSS", "SAS", "RHS", "AAS"],
                "answer": 1,
                "solution_steps": [
                    "Draw diagonal AC. Since AB ∥ CD, alternate interior angles ∠BAC = ∠DCA.",
                    "Also AB = CD and AC = AC (common).",
                    "By SAS congruence, ∆ABC ≅ ∆CDA, so ∠BCA = ∠DAC ⇒ AD ∥ BC.",
                ],
            },
            {
                "question": "Which condition alone does NOT guarantee that quadrilateral ABCD is a parallelogram?",
                "options": [
                    "AB = CD and BC = DA",
                    "∠A = ∠C and ∠B = ∠D",
                    "AB ∥ CD and BC = DA",
                    "AB ∥ CD and AB = CD",
                ],
                "answer": 2,
                "solution_steps": [
                    "AB ∥ CD and BC = DA can hold for an isosceles trapezium.",
                    "In an isosceles trapezium, the parallel sides AB and CD have different lengths.",
                    "Thus, AB ∥ CD and BC = DA is NOT sufficient for a parallelogram.",
                ],
            },
            {
                "question": "In quadrilateral PQRS, diagonals PR and QS intersect at O with PO = 5 cm, OR = 5 cm, QO = 7 cm, OS = 7 cm. What is PQRS?",
                "options": [
                    "Kite",
                    "Trapezium",
                    "Parallelogram",
                    "Cannot be determined",
                ],
                "answer": 2,
                "solution_steps": [
                    "PO = OR = 5 cm and QO = OS = 7 cm means both diagonals bisect each other.",
                    "By Theorem 4, any quadrilateral whose diagonals bisect each other is a parallelogram.",
                    "Therefore, PQRS is a parallelogram.",
                ],
            },
            {
                "question": "If a quadrilateral has three angles measuring 70°, 110°, and 70°, what is the fourth angle and shape?",
                "options": [
                    "110°, parallelogram",
                    "100°, trapezium",
                    "110°, kite only",
                    "90°, rectangle",
                ],
                "answer": 0,
                "solution_steps": [
                    "Fourth angle = 360° − (70° + 110° + 70°) = 110°.",
                    "Opposite angles are equal: 70° = 70° and 110° = 110°.",
                    "By Theorem 3, it is a parallelogram.",
                ],
            },
            {
                "question": "In ∆ABC and ∆DEF, AB = DE, AB ∥ DE, BC = EF, and BC ∥ EF. What kind of quadrilateral is ACFD?",
                "options": [
                    "Kite",
                    "Parallelogram",
                    "Non-convex 4-gon",
                    "Right trapezium",
                ],
                "answer": 1,
                "solution_steps": [
                    "Since AB = DE and AB ∥ DE, ABED is a parallelogram (Theorem 5), so AD = BE and AD ∥ BE.",
                    "Similarly, BC = EF and BC ∥ EF makes BEFC a parallelogram, so CF = BE and CF ∥ BE.",
                    "Thus AD = CF and AD ∥ CF, making ACFD a parallelogram by Theorem 5.",
                ],
            },
            {
                "question": "Why does a rhombus always qualify as a parallelogram?",
                "options": [
                    "All four angles are 90°",
                    "All four sides are equal, so both pairs of opposite sides are equal (Theorem 2)",
                    "Its diagonals are equal",
                    "It has only one pair of parallel sides",
                ],
                "answer": 1,
                "solution_steps": [
                    "In a rhombus, AB = BC = CD = DA.",
                    "In particular, AB = CD and BC = DA (both pairs of opposite sides equal).",
                    "By Theorem 2, every rhombus is a parallelogram.",
                ],
            },
            {
                "question": "If the internal angle bisectors of parallelogram ABCD meet at P, Q, R, S, what is PQRS?",
                "options": [
                    "Trapezium",
                    "Kite",
                    "Rectangle",
                    "Non-convex 4-gon",
                ],
                "answer": 2,
                "solution_steps": [
                    "Adjacent angles of a parallelogram satisfy ∠A + ∠B = 180°.",
                    "Their bisectors meet at angle 180° − ½(∠A + ∠B) = 90°.",
                    "All four interior angles of PQRS are 90°, so PQRS is a rectangle.",
                ],
            },
        ],
    },
    {
        "id": 19,
        "title": "Midpoint Varignon Quiz",
        "subtitle": "Mastery Quiz 3 (Silent Exercise): Midpoint Theorem, Centroid & Varignon (Section 12.3)",
        "is_quiz": True,
        "questions": [
            {
                "question": "In ∆ABC, D and E are midpoints of AB and AC. If BC = 16 cm, what is the length of DE?",
                "options": ["4 cm", "8 cm", "16 cm", "32 cm"],
                "answer": 1,
                "solution_steps": [
                    "By Theorem 6 (Midpoint Theorem), the segment joining midpoints of two sides is half the third side.",
                    "DE = ½ × BC = ½ × 16 = 8 cm.",
                    "Also, DE ∥ BC.",
                ],
            },
            {
                "question": "In ∆PQR, X is the midpoint of PQ and a line through X parallel to QR meets PR at Y. If PY = 6.5 cm, what is PR?",
                "options": ["6.5 cm", "13 cm", "3.25 cm", "19.5 cm"],
                "answer": 1,
                "solution_steps": [
                    "By Theorem 7 (Converse Midpoint Theorem), the line through X parallel to QR bisects PR at Y.",
                    "Therefore, Y is the midpoint of PR, so PY = YR = 6.5 cm.",
                    "PR = 2 × 6.5 = 13 cm.",
                ],
            },
            {
                "question": "In ∆ABC, medians AD and BE intersect at centroid G. If BG = 10 cm, find the length of GE and BE.",
                "options": [
                    "GE = 5 cm, BE = 15 cm",
                    "GE = 10 cm, BE = 20 cm",
                    "GE = 20 cm, BE = 30 cm",
                    "GE = 2.5 cm, BE = 12.5 cm",
                ],
                "answer": 0,
                "solution_steps": [
                    "By Theorem 8, centroid G divides median BE in the ratio BG : GE = 2 : 1.",
                    "Since BG = 10 cm, GE = 10 / 2 = 5 cm.",
                    "Total median BE = BG + GE = 10 + 5 = 15 cm.",
                ],
            },
            {
                "question": "What is the key auxiliary construction used to prove Theorem 6 (DE ∥ BC and DE = ½BC)?",
                "options": [
                    "Draw the altitude from A to BC",
                    "Extend DE to F so EF = DE and join CF to form parallelogram BCFD",
                    "Draw the circumcircle of ∆ABC",
                    "Bisect angle B",
                ],
                "answer": 1,
                "solution_steps": [
                    "Extending DE to F with EF = DE gives ∆ADE ≅ ∆CFE (SAS).",
                    "This makes CF = AD = BD and CF ∥ BD.",
                    "By Theorem 5, BCFD is a parallelogram, so DF ∥ BC and DE = ½DF = ½BC.",
                ],
            },
            {
                "question": "In any planar quadrilateral ABCD with diagonals AC = 12 cm and BD = 18 cm, what is the perimeter of its Varignon parallelogram PQRS?",
                "options": ["15 cm", "30 cm", "60 cm", "216 cm"],
                "answer": 1,
                "solution_steps": [
                    "By the Midpoint Theorem, PQ = SR = ½AC = 6 cm and QR = PS = ½BD = 9 cm.",
                    "Perimeter of PQRS = 6 + 9 + 6 + 9 = 30 cm.",
                    "Equivalently, Perimeter(PQRS) = AC + BD = 12 + 18 = 30 cm.",
                ],
            },
            {
                "question": "If the area of quadrilateral ABCD is 84 cm², what is the area of its Varignon parallelogram PQRS?",
                "options": ["21 cm²", "42 cm²", "84 cm²", "168 cm²"],
                "answer": 1,
                "solution_steps": [
                    "The four corner triangles cut off by the midlines each have 1/4 the area of their respective half-triangles.",
                    "Together, the four corner triangles sum to ½ Area(ABCD).",
                    "Thus Area(PQRS) = ½ × 84 = 42 cm².",
                ],
            },
            {
                "question": "What special Varignon parallelogram is formed when you join the midpoints of a kite?",
                "options": ["Rhombus", "Rectangle", "Trapezium", "Pentagon"],
                "answer": 1,
                "solution_steps": [
                    "A kite has perpendicular diagonals (AC ⊥ BD).",
                    "Since Varignon sides are parallel to AC and BD, adjacent Varignon sides are perpendicular.",
                    "A parallelogram with a 90° angle is a rectangle.",
                ],
            },
            {
                "question": "In a trapezium with parallel sides 12 cm and 22 cm, what is the length of the segment joining the midpoints of its non-parallel sides?",
                "options": ["5 cm", "10 cm", "17 cm", "34 cm"],
                "answer": 2,
                "solution_steps": [
                    "By the trapezium midsegment theorem, midsegment length = ½(a + b).",
                    "m = ½(12 + 22) = ½(34) = 17 cm.",
                    "It is also parallel to both bases.",
                ],
            },
            {
                "question": "In James Watt's parallel motion linkage, why does the tracer point move in a nearly straight vertical line?",
                "options": [
                    "The beams stretch elastically",
                    "Two opposing circular arcs cancel out horizontal drift at the midpoint",
                    "A hidden gear locks the rod",
                    "The pivot is fixed at infinity",
                ],
                "answer": 1,
                "solution_steps": [
                    "Two pivoted rockers swing in opposite circular arcs.",
                    "The midpoint of the connecting link averages their opposite horizontal curvatures.",
                    "Combined with a pantograph parallelogram, this produces accurate straight-line motion.",
                ],
            },
            {
                "question": "In physics, how is the resultant of two forces acting at a point represented using the Parallelogram Law?",
                "options": [
                    "By the shorter side of the parallelogram",
                    "By the diagonal passing through the common origin of the two force vectors",
                    "By the perimeter of the parallelogram",
                    "By the angle between the forces",
                ],
                "answer": 1,
                "solution_steps": [
                    "Place the two force vectors tail-to-tail as adjacent sides of a parallelogram.",
                    "Complete the parallelogram with parallel copies of both vectors.",
                    "The diagonal from the common tail represents the magnitude and direction of the resultant force.",
                ],
            },
        ],
    },
    {
        "id": 20,
        "title": "Tessellation Polygons Quiz",
        "subtitle": "Mastery Quiz 4 (Silent Exercise): Tiling, Polygons & Skew 4-Gons (Section 12.4 & Exercises)",
        "is_quiz": True,
        "questions": [
            {
                "question": "In Method 1 of quadrilateral tiling, around which points are 180° rotations performed?",
                "options": [
                    "The four vertices",
                    "The midpoints of the four sides",
                    "The centroid only",
                    "External points 10 cm away",
                ],
                "answer": 1,
                "solution_steps": [
                    "Rotating 180° around the midpoint of a side maps that side onto itself in reverse.",
                    "This aligns adjacent tiles flush along every edge without gaps.",
                    "Repeating around all side midpoints tiles the infinite plane.",
                ],
            },
            {
                "question": "Why does ANY planar quadrilateral (even non-convex) tile the plane without gaps around each vertex?",
                "options": [
                    "Its sides are all equal",
                    "The four angles meeting at each vertex are A, B, C, D and sum to 360°",
                    "It is always symmetric",
                    "All its angles are 90°",
                ],
                "answer": 1,
                "solution_steps": [
                    "180° midpoint rotations bring one copy each of ∠A, ∠B, ∠C, and ∠D around every vertex.",
                    "For any planar 4-gon (convex or non-convex), ∠A + ∠B + ∠C + ∠D = 360°.",
                    "360° fills a full circle around each vertex with zero gap or overlap.",
                ],
            },
            {
                "question": "In Method 2 of tiling, how does the area of one quadrilateral ABCD compare to its Varignon parallelogram PQRS?",
                "options": [
                    "Area(ABCD) = Area(PQRS)",
                    "Area(ABCD) = 2 × Area(PQRS)",
                    "Area(ABCD) = 4 × Area(PQRS)",
                    "Area(ABCD) = ½ × Area(PQRS)",
                ],
                "answer": 1,
                "solution_steps": [
                    "Varignon's parallelogram PQRS occupies exactly half the area of ABCD.",
                    "The remaining half consists of four corner triangles that fold outward to complete the grid.",
                    "Thus Area(ABCD) = 2 × Area(PQRS).",
                ],
            },
            {
                "question": "What is the key difference between a periodic tiling and an aperiodic tiling?",
                "options": [
                    "Periodic tilings use curved edges",
                    "Periodic tilings repeat identically under translation, whereas aperiodic tilings never repeat by shifting",
                    "Aperiodic tilings leave 10% empty space",
                    "Periodic tilings only use triangles",
                ],
                "answer": 1,
                "solution_steps": [
                    "A periodic tiling can be shifted (translated) onto itself cleanly.",
                    "An aperiodic tiling covers the entire plane with no gaps, yet has no translational symmetry.",
                    "Quasicrystals and the 2023 'hat' monotile exhibit aperiodic order.",
                ],
            },
            {
                "question": "How many diagonals does a convex octagon (n = 8) have?",
                "options": ["8", "16", "20", "40"],
                "answer": 2,
                "solution_steps": [
                    "Use the formula D = n(n − 3) / 2.",
                    "Substitute n = 8: D = 8 × (8 − 3) / 2 = 8 × 5 / 2.",
                    "D = 20 diagonals.",
                ],
            },
            {
                "question": "What happens to the sum of the four interior angles when a planar square is bent out of its plane along a diagonal?",
                "options": [
                    "It stays 360°",
                    "It becomes strictly less than 360°",
                    "It becomes strictly greater than 360°",
                    "It becomes 540°",
                ],
                "answer": 1,
                "solution_steps": [
                    "Bending along diagonal AC keeps the two angles at B and D unchanged, while folding reduces the 3D angles at A and C.",
                    "By the 3D triangle inequality for angles, each folded corner angle is strictly less than the sum of its two planar halves.",
                    "Hence the total interior angle sum of a skew 4-gon is strictly less than 360°.",
                ],
            },
            {
                "question": "When cutting ∆ABC along midline DE and rotating ∆ADE 180° around E, what theorem guarantees the resulting shape is a parallelogram?",
                "options": [
                    "Theorem 2 or Theorem 5",
                    "Theorem 8 only",
                    "Pythagoras Theorem",
                    "Thales Circle Theorem",
                ],
                "answer": 0,
                "solution_steps": [
                    "After rotating ∆ADE 180° about E, the new base equals 2·DE = BC and is parallel to BC.",
                    "Having one pair of opposite sides both equal and parallel certifies a parallelogram by Theorem 5.",
                    "Opposite sides are also equal, matching Theorem 2.",
                ],
            },
            {
                "question": "To trisect segment AB using a compass and straightedge, how many equal arcs do you step off on the auxiliary ray from A?",
                "options": ["2", "3", "4", "6"],
                "answer": 1,
                "solution_steps": [
                    "To divide a segment into n equal parts, mark n equal intervals along an auxiliary ray from A.",
                    "For trisection (n = 3), mark 3 equal arcs P₁, P₂, P₃.",
                    "Connect P₃ to B and draw parallels through P₁ and P₂ to trisect AB.",
                ],
            },
            {
                "question": "Which scientist discovered quasicrystals in 1982 and won the 2011 Nobel Prize in Chemistry?",
                "options": [
                    "Pierre Varignon",
                    "James Watt",
                    "Dan Shechtman",
                    "Euclid",
                ],
                "answer": 2,
                "solution_steps": [
                    "Dan Shechtman discovered icosahedral quasicrystals in 1982.",
                    "Their atomic structure is ordered yet non-periodic (aperiodic tiling).",
                    "He received the 2011 Nobel Prize in Chemistry for this breakthrough.",
                ],
            },
            {
                "question": "Which single summary statement captures the power of Chapter 12 (Quadrilaterals)?",
                "options": [
                    "Only squares can tile the plane",
                    "Parallelogram tests (Theorems 2–5) and Midpoint engines (Theorems 6–9) unify linkages, centroids, Varignon, and universal tiling",
                    "Non-convex quadrilaterals have angle sum 180°",
                    "Diagonals of every quadrilateral bisect each other",
                ],
                "answer": 1,
                "solution_steps": [
                    "Theorems 2–5 provide exact tests for parallelograms.",
                    "Theorems 6–9 power linkages, centroid 2:1 ratios, and Varignon's universal parallelogram.",
                    "Together with the 360° angle sum, any planar 4-gon tiles the infinite plane.",
                ],
            },
        ],
    },
]

for _s in slides_part3:
    for _q in _s["questions"]:
        _q.setdefault("hint", _q["solution_steps"][0])
        _q.setdefault("explanation", _q["solution_steps"][-1])

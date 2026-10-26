"""
Data module for Class 9 Mathematics Chapter 10: 4-gons (Quadrilaterals)
Syllabus Competencies: CG-4, C-4.2, C-7.3, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Precise Definition & Anatomy of a 4-gon (Quadrilateral)",
        "subtitle": "Non-Collinear Coplanar Points, Convex vs Concave Polygons & The 360° Angle Sum Theorem",
        "category": "Foundations",
        "badge": "CG-4 • C-4.2 • Definition & Angle Sum",
        "summary": "What is a 4-gon? A 4-gon (or quadrilateral, from Latin 'quadri' = four and 'latus' = side) is a closed, planar geometric figure bounded by four straight line segments formed by joining four coplanar points, no three of which are collinear, such that the segments intersect only at their endpoints. A quadrilateral ABCD has 4 vertices (A, B, C, D), 4 sides (AB, BC, CD, DA), 4 interior angles (∠A, ∠B, ∠C, ∠D), and 2 diagonals (AC, BD) connecting opposite vertices. Quadrilaterals are classified into Convex 4-gons (where every interior angle is strictly less than 180° and all diagonals lie entirely within the interior) and Concave 4-gons (where one interior angle exceeds 180° and one diagonal lies outside). The foundational Angle Sum Theorem states: 'The sum of all four interior angles of any planar quadrilateral is exactly 360°'. This is proven by drawing a single diagonal dividing the 4-gon into two triangles: (2 × 180° = 360°).",
        "key_points": [
            "Formal Definition: A closed plane figure formed by 4 line segments connecting 4 coplanar points (no 3 collinear) intersecting only at endpoints.",
            "Anatomy: 4 vertices, 4 sides, 4 interior angles, 2 diagonals, opposite sides (no common vertex), and adjacent sides (share a vertex).",
            "Convex vs Concave: In convex 4-gons, all angles are < 180° and both diagonals lie inside; in concave, one angle is reflex (> 180°).",
            "Angle Sum Theorem: ∠A + ∠B + ∠C + ∠D = (4 - 2) × 180° = 360°.",
            "Diagonal Partition: Any single diagonal splits a 4-gon into two non-overlapping triangles, immediately establishing the 360° sum."
        ],
        "narration": "Welcome to 4-gons and Quadrilaterals! A 4-gon is simply a closed four-sided polygon in a flat plane. Did you know that no matter how you stretch or distort a quadrilateral, the sum of its four interior angles is ALWAYS exactly 360 degrees? That is because any single diagonal cuts it neatly into two triangles, each contributing 180 degrees!",
        "sim_title": "Interactive 4-gon Builder & 360° Angle Sum Inspector",
        "checkpoints": [
            {
                "q": "What is the sum of the four interior angles of any planar quadrilateral?",
                "options": ["180°", "270°", "360°", "540°"],
                "ans": 2,
                "exp": "Drawing one diagonal divides any planar quadrilateral into two non-overlapping triangles. Since the angles of each triangle sum to 180°, the total interior angle sum is 2 × 180° = 360°."
            },
            {
                "q": "A quadrilateral ABCD has interior angles in the ratio 3 : 5 : 9 : 13. What is the measure of the largest angle?",
                "options": ["108°", "120°", "156°", "168°"],
                "ans": 2,
                "exp": "Let the angles be 3x, 5x, 9x, 13x. Their sum is 3x + 5x + 9x + 13x = 30x = 360°, giving x = 12°. The largest angle is 13x = 13 × 12° = 156°."
            }
        ]
    },
    {
        "id": 2,
        "title": "Parallelogram Definition & Equivalent Characterisations",
        "subtitle": "Opposite Sides Parallel, Opposite Angles Equal & The 5 Definitive Tests",
        "category": "Parallelograms",
        "badge": "CG-4 • C-4.2 • C-7.3 • Parallelogram Characterisations",
        "summary": "A Parallelogram is fundamentally defined as a quadrilateral in which both pairs of opposite sides are parallel: AB ∥ CD and AD ∥ BC. In geometry, an 'equivalent characterisation' is an alternative set of conditions that guarantees a quadrilateral is a parallelogram. In fact, a quadrilateral ABCD is a parallelogram IF AND ONLY IF any ONE of the following five conditions is satisfied: 1. Both pairs of opposite sides are parallel (Definition). 2. Both pairs of opposite sides are equal (AB = CD and AD = BC). 3. Both pairs of opposite angles are equal (∠A = ∠C and ∠B = ∠D). 4. Adjacent (consecutive) interior angles are supplementary (e.g., ∠A + ∠B = 180°). 5. The two diagonals bisect each other (OA = OC and OB = OD). 6. ONE pair of opposite sides is BOTH equal and parallel (AB = CD and AB ∥ CD). Establishing any single one of these criteria mathematically proves all the others!",
        "key_points": [
            "Primary Definition: A quadrilateral with both pairs of opposite sides parallel (AB ∥ CD and AD ∥ BC).",
            "Characterisation 1 (Equal Sides): Both pairs of opposite sides are equal in length.",
            "Characterisation 2 (Equal Angles): Both pairs of opposite angles are equal.",
            "Characterisation 3 (Supplementary Angles): Any two consecutive angles add up to 180°.",
            "Characterisation 4 (Diagonals Bisect): Diagonals bisect each other at their mutual intersection point.",
            "Golden Criterion 5: A quadrilateral is a parallelogram if ONE pair of opposite sides is both equal AND parallel."
        ],
        "narration": "A parallelogram is defined as a four-sided shape with both pairs of opposite sides parallel. But here is the beauty of geometry: there are multiple equivalent ways to prove a shape is a parallelogram! If both pairs of opposite sides are equal, or opposite angles are equal, or diagonals bisect each other, it is guaranteed to be a parallelogram!",
        "sim_title": "Parallelogram Characterisation Tester",
        "checkpoints": [
            {
                "q": "Which of the following conditions alone is sufficient to prove that a quadrilateral ABCD is a parallelogram?",
                "options": [
                    "One pair of opposite sides is equal, and the other pair is parallel",
                    "One pair of opposite sides is both equal and parallel",
                    "The diagonals are perpendicular to each other",
                    "Two adjacent angles are equal"
                ],
                "ans": 1,
                "exp": "Theorem 8.8 states: A quadrilateral is a parallelogram if a pair of opposite sides is both equal and parallel. Having one pair equal and a DIFFERENT pair parallel can produce an isosceles trapezium, not a parallelogram."
            },
            {
                "q": "If one interior angle of a parallelogram ABCD is 75°, what are the measures of the remaining three angles?",
                "options": [
                    "75°, 75°, 75°",
                    "105°, 75°, 105°",
                    "115°, 65°, 115°",
                    "90°, 90°, 90°"
                ],
                "ans": 1,
                "exp": "Opposite angles of a parallelogram are equal (75°), and consecutive angles are supplementary (180° - 75° = 105°). Thus, the angles are 75°, 105°, 75°, 105°."
            }
        ]
    },
    {
        "id": 3,
        "title": "Proofs of Core Parallelogram Theorems (Theorems 8.1, 8.2 & 8.3)",
        "subtitle": "Diagonal Congruence Partition, Opposite Sides Equality & Converse Proof via SSS",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 8.1 - 8.3",
        "summary": "Theorem 8.1 states: 'A diagonal of a parallelogram divides it into two congruent triangles.' Proof: Let ABCD be a parallelogram and AC be a diagonal. Since AB ∥ DC with transversal AC, alternate interior angles ∠BAC = ∠DCA. Since AD ∥ BC with transversal AC, alternate interior angles ∠BCA = ∠DAC. Common side AC = CA. Therefore, △ABC ≅ △CDA by the ASA congruence criterion! Theorem 8.2 immediately follows by CPCTC: 'In a parallelogram, opposite sides are equal' (AB = CD and BC = DA) and 'opposite angles are equal' (∠B = ∠D). Theorem 8.3 is the Converse: 'If each pair of opposite sides of a quadrilateral is equal, then it is a parallelogram.' Proof: Draw diagonal AC. In △ABC and △CDA: AB = CD (given), BC = DA (given), AC = CA (common). Thus △ABC ≅ △CDA by SSS! By CPCTC, ∠BAC = ∠DCA (so AB ∥ CD) and ∠BCA = ∠DAC (so AD ∥ BC). Hence ABCD is a parallelogram.",
        "key_points": [
            "Theorem 8.1: Diagonal AC divides parallelogram ABCD into two congruent triangles (△ABC ≅ △CDA via ASA).",
            "Theorem 8.2: In a parallelogram, opposite sides are equal (AB = CD and BC = DA) proven directly by CPCTC.",
            "Theorem 8.3 (Converse): If each pair of opposite sides of a quadrilateral is equal, it is a parallelogram.",
            "Proof Method for Converse: SSS congruence proves alternate interior angles are equal, establishing parallel sides.",
            "Area Corollary: A diagonal divides a parallelogram into two triangles of equal area."
        ],
        "narration": "Let's prove Theorem 8.1! Draw a diagonal AC through parallelogram ABCD. Notice the iconic Z-patterns of parallel lines: alternate interior angles match, and the diagonal is shared. By ASA, the two triangles are congruent! And by CPCTC, opposite sides must be equal. Flipping the logic gives us Theorem 8.3: if opposite sides are equal, SSS proves it's a parallelogram!",
        "sim_title": "Diagonal Partition & CPCTC Congruence Explorer",
        "checkpoints": [
            {
                "q": "By which congruence criterion does a diagonal divide a parallelogram into two congruent triangles in Theorem 8.1?",
                "options": ["SSS", "SAS", "ASA", "RHS"],
                "ans": 2,
                "exp": "Transversal AC creates two pairs of equal alternate interior angles, with diagonal AC acting as the common included side. Thus, △ABC ≅ △CDA by ASA."
            },
            {
                "q": "In the proof of Theorem 8.3 (Converse of Theorem 8.2), which congruence criterion proves △ABC ≅ △CDA when opposite sides are given equal?",
                "options": ["SSS", "ASA", "AAS", "RHS"],
                "ans": 0,
                "exp": "Since AB = CD, BC = DA, and AC = CA (common), all three corresponding sides are equal. Hence the triangles are congruent by SSS, proving alternate interior angles equal."
            }
        ]
    },
    {
        "id": 4,
        "title": "Parallelogram Angle Theorems & Converse (Theorems 8.4 & 8.5)",
        "subtitle": "Opposite Angles Equality, Consecutive Supplementary Angles & Converse Proof",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 8.4 & 8.5",
        "summary": "Theorem 8.4 states: 'In a parallelogram, opposite angles are equal' (∠A = ∠C and ∠B = ∠D). Proof: In parallelogram ABCD, side AB ∥ CD with transversal AD. Consecutive interior angles on the same side of the transversal are supplementary: ∠A + ∠D = 180°. Similarly, AD ∥ BC with transversal AB gives ∠A + ∠B = 180°. Equating the two sums: ∠A + ∠D = ∠A + ∠B ⇒ ∠D = ∠B! By identical reasoning, ∠A = ∠C. Theorem 8.5 is the Converse: 'If in a quadrilateral, each pair of opposite angles is equal, then it is a parallelogram.' Proof: Given ∠A = ∠C and ∠B = ∠D. In quadrilateral ABCD, the angle sum is ∠A + ∠B + ∠C + ∠D = 360°. Substituting ∠C = ∠A and ∠D = ∠B yields 2∠A + 2∠B = 360° ⇒ ∠A + ∠B = 180°. Since consecutive interior angles between lines AD and BC are supplementary, line AD is parallel to BC. Similarly, AB ∥ CD. Therefore, ABCD is a parallelogram!",
        "key_points": [
            "Theorem 8.4: Opposite angles of a parallelogram are equal (∠A = ∠C and ∠B = ∠D).",
            "Consecutive Supplementary Rule: Any pair of consecutive angles sums to 180° (co-interior angles of parallel lines).",
            "Theorem 8.5 (Converse): If opposite angles of a 4-gon are equal, then it is a parallelogram.",
            "Converse Proof Mechanism: 2∠A + 2∠B = 360° ⇒ ∠A + ∠B = 180°, proving parallel lines via consecutive interior angle converse.",
            "Direct Application: If an angle is a right angle (90°), all four angles become 90°, making it a rectangle."
        ],
        "narration": "Theorem 8.4 tells us that opposite angles in any parallelogram are identical! Why? Because consecutive angles are co-interior angles between parallel lines, adding up to 180 degrees. If angle A plus angle D is 180, and angle A plus angle B is 180, then angle D must equal angle B!",
        "sim_title": "Opposite Angle Balancer & Supplementary Angle Wheel",
        "checkpoints": [
            {
                "q": "If two adjacent angles of a parallelogram are in the ratio 2 : 3, what is the measure of the smaller angle?",
                "options": ["36°", "54°", "72°", "108°"],
                "ans": 2,
                "exp": "Adjacent angles of a parallelogram are supplementary: 2x + 3x = 5x = 180° ⇒ x = 36°. The smaller angle is 2x = 2 × 36° = 72°."
            },
            {
                "q": "In the proof of Theorem 8.5, what key fact converts 2∠A + 2∠B = 360° into proof of parallel lines?",
                "options": [
                    "Converse of Consecutive Interior Angles: If co-interior angles sum to 180°, the lines are parallel",
                    "Pythagorean theorem",
                    "RHS congruence",
                    "Exterior angle theorem"
                ],
                "ans": 0,
                "exp": "Since ∠A + ∠B = 180°, the consecutive interior angles on the same side of transversal AB sum to two right angles, proving AD ∥ BC by the parallel line converse."
            }
        ]
    },
    {
        "id": 5,
        "title": "Diagonal Bisection Theorems & Converse (Theorems 8.6 & 8.7)",
        "subtitle": "Mutual Midpoints, Proof via Vertically Opposite Angles & Coordinate Symmetry",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 8.6 & 8.7",
        "summary": "Theorem 8.6 states: 'The diagonals of a parallelogram bisect each other.' Proof: Let ABCD be a parallelogram with diagonals AC and BD intersecting at point O. We wish to prove OA = OC and OB = OD. Consider △AOB and △COD: AB = CD (opposite sides of a parallelogram are equal). Since AB ∥ CD with transversal AC, alternate interior angles ∠OAB = ∠OCD. Since AB ∥ CD with transversal BD, alternate interior angles ∠OBA = ∠ODC. Therefore, △AOB ≅ △COD by the ASA congruence criterion! By CPCTC, OA = OC and OB = OD. Thus, point O is the mutual midpoint of both diagonals! Theorem 8.7 is the Converse: 'If the diagonals of a quadrilateral bisect each other, then it is a parallelogram.' Proof: If OA = OC and OB = OD, then in △AOB and △COD: OA = OC, OB = OD, and vertically opposite angles ∠AOB = ∠COD. Hence △AOB ≅ △COD by SAS! By CPCTC, ∠OAB = ∠OCD (proving AB ∥ CD) and AB = CD. A 4-gon with one pair of opposite sides equal and parallel is a parallelogram!",
        "key_points": [
            "Theorem 8.6: Diagonals AC and BD of a parallelogram bisect each other at their mutual intersection O.",
            "Deductive Proof: △AOB ≅ △COD by ASA establishes OA = OC and OB = OD via CPCTC.",
            "Theorem 8.7 (Converse): If diagonals of a 4-gon bisect each other, it is a parallelogram.",
            "Converse Proof: SAS congruence between vertically opposite triangles proves alternate interior angles and side equality.",
            "Shared Midpoint Property: Point O is simultaneously the midpoint of AC and the midpoint of BD."
        ],
        "narration": "Here is one of the most useful theorems in geometry: the diagonals of a parallelogram bisect each other! They cut each other right at their exact middle point O. The proof compares the two opposite triangles formed by the intersecting diagonals: by ASA, they are congruent, meaning OA equals OC, and OB equals OD!",
        "sim_title": "Diagonal Bisection & Mutual Midpoint Simulator",
        "checkpoints": [
            {
                "q": "In a parallelogram ABCD, diagonals AC and BD intersect at O. If AC = 16 cm and BD = 12 cm, what are the lengths of OA and OD?",
                "options": ["8 cm and 6 cm", "16 cm and 12 cm", "8 cm and 8 cm", "10 cm and 10 cm"],
                "ans": 0,
                "exp": "By Theorem 8.6, diagonals bisect each other. Thus OA = AC / 2 = 16 / 2 = 8 cm, and OD = BD / 2 = 12 / 2 = 6 cm."
            },
            {
                "q": "What congruence criterion is used to prove Theorem 8.7 (that bisecting diagonals imply a parallelogram)?",
                "options": ["SSS", "SAS", "ASA", "AAS"],
                "ans": 1,
                "exp": "In △AOB and △COD: OA = OC, OB = OD (given bisection), and included vertically opposite angles ∠AOB = ∠COD. Thus △AOB ≅ △COD by SAS."
            }
        ]
    },
    {
        "id": 6,
        "title": "Special Parallelograms: Rectangle, Rhombus & Square",
        "subtitle": "Hierarchical Classification, Orthogonal Diagonals & Equal Diagonals Criteria",
        "category": "Parallelograms",
        "badge": "CG-4 • C-4.2 • Special 4-gons",
        "summary": "All special quadrilaterals inherit all the core properties of parallelograms, but possess unique defining symmetry traits: 1. Rectangle: A parallelogram with one right angle. By supplementary and opposite angle rules, ALL four angles are 90°. Unique Property: The diagonals of a rectangle are EQUAL in length (AC = BD, proven via △ABC ≅ △DCB by SAS). Converse: If diagonals of a parallelogram are equal, it is a rectangle. 2. Rhombus: A parallelogram with all four sides equal in length. Unique Property: The diagonals of a rhombus are PERPENDICULAR bisectors of each other (AC ⊥ BD, proven via △AOB ≅ △COB by SSS giving ∠AOB = ∠COB = 90°). Converse: If diagonals of a parallelogram are perpendicular, it is a rhombus. 3. Square: A quadrilateral that is simultaneously a rectangle and a rhombus! All four sides are equal, all four angles are 90°, and diagonals are both EQUAL and PERPENDICULAR bisectors of each other.",
        "key_points": [
            "Hierarchy: Square ⊂ Rhombus ⊂ Parallelogram; Square ⊂ Rectangle ⊂ Parallelogram.",
            "Rectangle Diagnostic: A parallelogram whose diagonals are equal (AC = BD).",
            "Rhombus Diagnostic: A parallelogram whose diagonals are perpendicular (AC ⊥ BD) and bisect vertex angles.",
            "Square Diagnostic: A regular 4-gon whose diagonals are equal, perpendicular, and bisect each other.",
            "Kite vs Rhombus: A kite has perpendicular diagonals, but only one diagonal bisects the other (not a parallelogram in general)."
        ],
        "narration": "Rectangles, rhombuses, and squares are all members of the parallelogram family! A rectangle is a parallelogram with four right angles, which forces its diagonals to be equal. A rhombus has four equal sides, which forces its diagonals to intersect at right angles! And a square has the best of both worlds: equal diagonals that cross at 90 degrees!",
        "sim_title": "Special 4-gon Morphing Transformer & Diagnostic Lab",
        "checkpoints": [
            {
                "q": "If the diagonals of a parallelogram are equal in length, what specific type of quadrilateral must it be?",
                "options": ["Rhombus", "Rectangle", "Trapezium", "Kite"],
                "ans": 1,
                "exp": "If diagonals of a parallelogram are equal (AC = BD), consider △ABC and △DCB: AB = DC, BC = CB, and AC = BD. By SSS, △ABC ≅ △DCB, so ∠B = ∠C = 90°, making it a rectangle."
            },
            {
                "q": "Which property is TRUE for a rhombus but NOT necessarily true for every general parallelogram?",
                "options": [
                    "Opposite sides are parallel",
                    "Opposite angles are equal",
                    "Diagonals bisect each other at right angles (90°)",
                    "Consecutive angles sum to 180°"
                ],
                "ans": 2,
                "exp": "In a general parallelogram, diagonals bisect each other but do not meet at 90°. Diagonals are perpendicular bisectors if and only if all four sides are equal (a rhombus)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Central Symmetry (Point Symmetry) in Parallelograms",
        "subtitle": "Half-Turn 180° Rotations, Point of Inversion & Bisection of Transverse Segments",
        "category": "Symmetry & Transformations",
        "badge": "CG-4 • C-4.2 • Central Symmetry",
        "summary": "In transformation geometry, a figure has Central Symmetry (or Point Symmetry) about a fixed center O if a half-turn rotation (180° rotation) about O maps the figure precisely onto itself. For every point P on the figure, its reflection across O is a point P' such that O is the exact midpoint of segment PP'. A parallelogram possesses central symmetry about the mutual intersection point O of its diagonals! Because OA = OC and OB = OD, a 180° rotation around O swaps vertex A with C, and vertex B with D. This profound symmetry explains why: 1. Any straight line drawn through center O divides the parallelogram into two congruent halves of identical area. 2. Any line segment passing through O with endpoints on opposite sides of the parallelogram is bisected by O. 3. Opposite sides and opposite angles are automatically equal due to the 180° point inversion.",
        "key_points": [
            "Central Symmetry Definition: Invariant under a 180° half-turn rotation about a central point O (point inversion).",
            "Center of Symmetry: The intersection of diagonals O is the unique center of central symmetry for any parallelogram.",
            "Vertex Swapping: Under a 180° rotation about O: A ↦ C, B ↦ D, C ↦ A, D ↦ B.",
            "Area Bisection Property: Any line passing through O cuts the parallelogram into two congruent trapeziums or triangles of equal area.",
            "Segment Bisection: Any chord through center O connecting opposite sides has O as its midpoint."
        ],
        "narration": "Did you know that a parallelogram has central symmetry? That means if you stick a pin right at the intersection of its diagonals and spin the shape by 180 degrees, it lands right back on itself! Vertex A swaps with C, and B swaps with D. Any straight line passing through this center splits the parallelogram into two congruent halves!",
        "sim_title": "180° Half-Turn Central Symmetry Visualizer",
        "checkpoints": [
            {
                "q": "What happens to a parallelogram when it is rotated by 180° about the intersection point of its diagonals?",
                "options": [
                    "It turns upside down into an inverted triangle",
                    "It maps perfectly onto itself, with opposite vertices swapping positions",
                    "Its area is doubled",
                    "Its diagonals become parallel"
                ],
                "ans": 1,
                "exp": "Because the diagonals bisect each other, a 180° half-turn about center O maps A to C, B to D, and every point P on a side to its opposite counterpart P', mapping the figure onto itself."
            },
            {
                "q": "Any straight line drawn through the intersection point of the diagonals of a parallelogram divides the parallelogram into:",
                "options": [
                    "Two shapes with unequal areas",
                    "Two congruent figures of equal area",
                    "Four equilateral triangles",
                    "A square and a rectangle"
                ],
                "ans": 1,
                "exp": "By 180° central symmetry, the two regions formed on either side of the line passing through center O are congruent by half-turn rotation, and thus have identical areas."
            }
        ]
    },
    {
        "id": 8,
        "title": "Reflection & Rotation Symmetries of 4-gons",
        "subtitle": "Axes of Symmetry, Rotational Orders & The Complete Symmetry Classification Table",
        "category": "Symmetry & Transformations",
        "badge": "CG-4 • C-4.2 • Reflection & Rotation",
        "summary": "Symmetry classifies 4-gons by their rigid isometries: Reflection Symmetry (folding across an axis of symmetry) and Rotational Symmetry (turning about a center by angle 360°/n). 1. General Parallelogram: 0 lines of reflection symmetry; Rotational symmetry of order 2 (180°, 360°). 2. Rectangle: 2 lines of reflection symmetry (lines joining midpoints of opposite sides); Rotational symmetry of order 2. (Note: Diagonals are NOT lines of symmetry unless it is a square!). 3. Rhombus: 2 lines of reflection symmetry (the two diagonals themselves); Rotational symmetry of order 2. 4. Square: 4 lines of reflection symmetry (2 diagonals + 2 midpoint lines); Rotational symmetry of order 4 (90°, 180°, 270°, 360°). 5. Kite: 1 line of reflection symmetry (the main diagonal); Rotational symmetry of order 1 (trivial). 6. Isosceles Trapezium: 1 line of reflection symmetry (line connecting midpoints of parallel bases); Rotational symmetry of order 1.",
        "key_points": [
            "Reflection Symmetry: Folding across an axis maps the figure onto its mirror image.",
            "Rotational Order n: Number of times a shape looks identical during a full 360° turn.",
            "Rectangle: 2 reflection axes (midpoint lines, NOT diagonals), order 2 rotation.",
            "Rhombus: 2 reflection axes (the diagonals), order 2 rotation.",
            "Square: Maximum symmetry (4 reflection axes, order 4 rotation).",
            "General Parallelogram: Has rotational symmetry (order 2) but ZERO reflection symmetry axes."
        ],
        "narration": "Let's explore the symmetries of 4-gons! A general parallelogram has rotational symmetry of order 2, but has zero mirror lines. A rectangle has 2 mirror lines connecting opposite midpoints, while a rhombus has 2 mirror lines along its diagonals. And the champion of symmetry is the square, with 4 mirror lines and order-4 rotation!",
        "sim_title": "4-gon Symmetry Mirror & Rotation Analyzer",
        "checkpoints": [
            {
                "q": "How many lines of reflection symmetry does a non-square rectangle possess?",
                "options": ["0", "1", "2", "4"],
                "ans": 2,
                "exp": "A non-square rectangle has exactly 2 lines of reflection symmetry: the two lines connecting the midpoints of opposite sides. Its diagonals are not lines of symmetry."
            },
            {
                "q": "Which quadrilateral has order-2 rotational symmetry but ZERO lines of reflection symmetry?",
                "options": ["Square", "Rhombus", "General Parallelogram (non-rhombus, non-rectangle)", "Kite"],
                "ans": 2,
                "exp": "A general parallelogram has 180° rotational symmetry (order 2), but folding it along any line fails to produce mirror symmetry. Hence it has 0 reflection axes."
            }
        ]
    },
    {
        "id": 9,
        "title": "The Midpoint Theorem (Theorem 8.9)",
        "subtitle": "Midpoints of Triangle Sides, Parallelism & The 1/2 Base Ratio Proof",
        "category": "The Midpoint Theorem",
        "badge": "CG-4 • C-4.2 • C-7.3 • Midpoint Theorem",
        "summary": "Theorem 8.9 (The Midpoint Theorem) is one of the crowning achievements of Euclidean geometry: 'The line segment joining the midpoints of two sides of a triangle is parallel to the third side and equal to half of it.' Let △ABC have D as the midpoint of AB, and E as the midpoint of AC. We wish to prove DE ∥ BC and DE = 1/2 BC. Proof: Extend segment DE to point F such that EF = DE. Join CF. In △ADE and △CFE: AE = CE (E is midpoint of AC), ∠AED = ∠CEF (vertically opposite angles), and DE = EF (by construction). Therefore, △ADE ≅ △CFE by the SAS axiom! By CPCTC, AD = CF and ∠ADE = ∠CFE. Since alternate interior angles are equal, AD ∥ CF. But AD = BD (D is midpoint of AB), so BD = CF and BD ∥ CF! A quadrilateral with one pair of opposite sides equal and parallel is a parallelogram, so BCFD is a parallelogram! Therefore, DF ∥ BC and DF = BC. Since DE = 1/2 DF, we conclude DE ∥ BC and DE = 1/2 BC!",
        "key_points": [
            "Theorem 8.9 Statement: Segment joining midpoints of two triangle sides is parallel to third side and half its length.",
            "Auxiliary Construction: Extend DE to F such that EF = DE, then join CF.",
            "SAS Congruence: △ADE ≅ △CFE proves AD = CF and AD ∥ CF.",
            "Parallelogram Emergence: BCFD is proven to be a parallelogram because BD = CF and BD ∥ CF.",
            "Conclusion: DF = BC and DF ∥ BC ⇒ DE = 1/2 BC and DE ∥ BC."
        ],
        "narration": "Here is the famous Midpoint Theorem! If you take the midpoints of two sides of any triangle and connect them with a segment DE, that segment is parallel to the base BC, and its length is exactly half of BC! The proof is pure genius: extend DE by its own length, and a secret parallelogram BCFD appears!",
        "sim_title": "Midpoint Theorem Proof & Parallelogram Emergence Lab",
        "checkpoints": [
            {
                "q": "In △ABC, D and E are midpoints of sides AB and AC. If BC = 14 cm, what is the length of DE?",
                "options": ["7 cm", "14 cm", "21 cm", "28 cm"],
                "ans": 0,
                "exp": "By the Midpoint Theorem, DE = 1/2 BC = 1/2 × 14 cm = 7 cm, and DE is parallel to BC."
            },
            {
                "q": "In the classical deductive proof of the Midpoint Theorem, which auxiliary quadrilateral is proven to be a parallelogram?",
                "options": ["ADEC", "BCFD", "ABCF", "BDEF"],
                "ans": 1,
                "exp": "By extending DE to F with EF = DE and joining CF, quadrilateral BCFD has BD = CF and BD ∥ CF, proving BCFD is a parallelogram."
            }
        ]
    },
    {
        "id": 10,
        "title": "Converse of the Midpoint Theorem (Theorem 8.10)",
        "subtitle": "Line Through Midpoint Parallel to Base Bisects the Third Side",
        "category": "The Midpoint Theorem",
        "badge": "CG-4 • C-4.2 • C-7.3 • Converse Midpoint",
        "summary": "Theorem 8.10 (Converse of the Midpoint Theorem) states: 'The line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side.' In △ABC, let D be the midpoint of side AB (AD = DB), and let a line l be drawn through D parallel to BC, intersecting side AC at point E. We wish to prove that E is the midpoint of AC (AE = EC). Proof: Draw a line through C parallel to BA, meeting the extension of line DE at point F. In quadrilateral BCFD: DF ∥ BC (given) and CF ∥ BD (by construction). Thus, BCFD is a parallelogram! By opposite sides of a parallelogram, BD = CF. But BD = AD (D is midpoint), so AD = CF. Now compare △ADE and △CFE: ∠DAE = ∠FCE (alternate interior angles since BA ∥ CF), AD = CF (proven), and ∠ADE = ∠CFE (alternate interior angles since DF ∥ BC). Therefore, △ADE ≅ △CFE by ASA! By CPCTC, AE = CE. Hence, point E is the midpoint of AC!",
        "key_points": [
            "Theorem 8.10: Line through midpoint of one side parallel to base bisects the opposite side.",
            "Given: D is midpoint of AB (AD = DB) and DE ∥ BC.",
            "To Prove: AE = EC (E is midpoint of AC).",
            "Proof Method: Auxiliary line CF ∥ AB forms parallelogram BCFD, reducing to ASA congruence △ADE ≅ △CFE.",
            "Applications: Subdividing line segments, proportional intercepts, and architectural drafting."
        ],
        "narration": "What is the converse of the Midpoint Theorem? If you start at the midpoint D of side AB and draw a line parallel to the base BC, where will it hit the other side AC? Exactly at its midpoint E! This theorem is used by carpenters and architects to find the exact center of beams without measuring!",
        "sim_title": "Converse Midpoint & Parallel Ray Intercept Simulator",
        "checkpoints": [
            {
                "q": "In △ABC, D is the midpoint of AB and DE ∥ BC. If AC = 18 cm, what is the length of AE?",
                "options": ["6 cm", "9 cm", "12 cm", "18 cm"],
                "ans": 1,
                "exp": "By the Converse of the Midpoint Theorem (Theorem 8.10), line DE bisects side AC. Therefore, E is the midpoint of AC, and AE = 18 / 2 = 9 cm."
            },
            {
                "q": "Which congruence criterion proves △ADE ≅ △CFE in the proof of Theorem 8.10?",
                "options": ["ASA", "SSS", "RHS", "SSA"],
                "ans": 0,
                "exp": "With CF ∥ AB and DF ∥ BC, two pairs of alternate interior angles are equal, with AD = CF. Thus △ADE ≅ △CFE by ASA, giving AE = CE by CPCTC."
            }
        ]
    },
    {
        "id": 11,
        "title": "Concurrency of Medians & The 2:1 Centroid Ratio Proof",
        "subtitle": "Intersection of Three Medians, Parallelogram FEQP & The Universal Center of Mass",
        "category": "Medians & Centroid",
        "badge": "CG-4 • C-4.2 • C-7.3 • Centroid 2:1 Ratio",
        "summary": "A Median of a triangle is a line segment connecting a vertex to the midpoint of the opposite side. One of the most elegant applications of the Midpoint Theorem is proving that the three medians of any triangle are concurrent at a single point G (called the Centroid), and that G divides each median in the ratio 2 : 1! Proof: Let medians BE and CF of △ABC intersect at point G. Let P be the midpoint of BG, and Q be the midpoint of CG. In △ABC, F is midpoint of AB and E is midpoint of AC. By the Midpoint Theorem, FE ∥ BC and FE = 1/2 BC. In △GBC, P is midpoint of BG and Q is midpoint of CG. By the Midpoint Theorem, PQ ∥ BC and PQ = 1/2 BC. Therefore, FE ∥ PQ and FE = PQ! Since a quadrilateral with one pair of opposite sides equal and parallel is a parallelogram, FEQP is a parallelogram! The diagonals of FEQP bisect each other, meaning GP = GE and GQ = GF. But since BP = PG, we have BG = BP + PG = 2GE ⇒ BG : GE = 2 : 1! Similarly, CG : GF = 2 : 1. By symmetry, the third median AD must also pass through G and be divided in the ratio 2 : 1.",
        "key_points": [
            "Centroid (G): The point of concurrency where all three medians of a triangle intersect.",
            "2:1 Division: G divides every median in the ratio 2 : 1 (vertex to midpoint: AG = 2GD, BG = 2GE, CG = 2GF).",
            "Midpoint Theorem Application: Applied simultaneously to △ABC (giving FE = 1/2 BC) and △GBC (giving PQ = 1/2 BC).",
            "Parallelogram FEQP: Diagonal bisection in FEQP proves GP = GE, instantly establishing the 2:1 ratio.",
            "Physical Meaning: The centroid G is the physical Center of Mass (balance point) of a uniform triangular lamina."
        ],
        "narration": "A median connects a corner to the opposite side's midpoint. A triangle has three medians, and miraculously, all three meet at the exact same point: the Centroid G! Even more amazing: G cuts every single median into a 2-to-1 ratio! We prove this using the Midpoint Theorem to reveal a hidden parallelogram FEQP inside the medians!",
        "sim_title": "Centroid 2:1 Lever & Median Concurrency Visualizer",
        "checkpoints": [
            {
                "q": "The centroid G of △ABC divides the median AD (where D is on BC) in what ratio from vertex A to midpoint D?",
                "options": ["1 : 1", "2 : 1", "3 : 1", "3 : 2"],
                "ans": 1,
                "exp": "The centroid divides every median in the ratio 2 : 1, measuring from the vertex to the opposite side's midpoint (AG : GD = 2 : 1)."
            },
            {
                "q": "If median AD has a total length of 15 cm, what is the length of segment AG (from vertex A to centroid G)?",
                "options": ["5 cm", "7.5 cm", "10 cm", "12 cm"],
                "ans": 2,
                "exp": "Since AG : GD = 2 : 1, AG represents 2/3 of the total median length. AG = (2/3) × 15 cm = 10 cm."
            }
        ]
    },
    {
        "id": 12,
        "title": "Varignon's Theorem: Midpoint 4-gon is a Parallelogram",
        "subtitle": "Connecting Midpoints of ANY Arbitrary 4-gon, Area Bisector & Shape Invariants",
        "category": "Varignon's Theorem",
        "badge": "CG-4 • C-4.2 • C-7.3 • Varignon's Theorem",
        "summary": "Theorem (Pierre Varignon, 1731): 'The quadrilateral formed by joining in order the midpoints of the sides of ANY quadrilateral is ALWAYS a parallelogram.' This theorem holds for convex, concave, and even self-intersecting 4-gons! Proof: Let ABCD be any arbitrary quadrilateral. Let P, Q, R, S be the midpoints of AB, BC, CD, DA respectively. Draw diagonal AC. In △ABC, P is midpoint of AB and Q is midpoint of BC. By the Midpoint Theorem, PQ ∥ AC and PQ = 1/2 AC. In △ADC, S is midpoint of AD and R is midpoint of CD. By the Midpoint Theorem, SR ∥ AC and SR = 1/2 AC. Therefore, PQ ∥ SR and PQ = SR! A quadrilateral with one pair of opposite sides equal and parallel is a parallelogram. Thus, PQRS is a parallelogram! Corollary: The perimeter of Varignon parallelogram PQRS equals the sum of diagonals of ABCD (AC + BD), and its area is exactly HALF the area of the original quadrilateral: Area(PQRS) = 1/2 Area(ABCD).",
        "key_points": [
            "Varignon's Theorem: Midpoints of sides of any 4-gon form a parallelogram (PQRS).",
            "Universal Validity: Holds true for ANY shape—convex, dart-shaped concave, or skewed.",
            "Proof via Diagonal AC: Midpoint Theorem gives PQ ∥ AC, SR ∥ AC, and PQ = SR = 1/2 AC.",
            "Area Corollary: Area of the Varignon parallelogram is strictly half the area of the parent quadrilateral: Area(PQRS) = 1/2 Area(ABCD).",
            "Perimeter Corollary: Perimeter of PQRS = AC + BD (sum of lengths of parent diagonals)."
        ],
        "narration": "In 1731, French mathematician Pierre Varignon discovered an incredible secret. Take ANY random, lopsided four-sided shape. Find the exact midpoints of its four sides, and connect them. You will ALWAYS get a perfect parallelogram! The proof is so clean: diagonal AC proves top and bottom are parallel, and diagonal BD proves left and right are parallel!",
        "sim_title": "Varignon's Parallelogram Playground & Area Halver",
        "checkpoints": [
            {
                "q": "If the area of an irregular convex quadrilateral ABCD is 48 cm², what is the area of the Varignon parallelogram formed by joining the midpoints of its sides?",
                "options": ["12 cm²", "24 cm²", "36 cm²", "48 cm²"],
                "ans": 1,
                "exp": "By Varignon's Theorem area corollary, the area of the midpoint parallelogram is exactly half the area of the original quadrilateral: 48 / 2 = 24 cm²."
            },
            {
                "q": "What determines whether the Varignon parallelogram PQRS is a RHOMBUS?",
                "options": [
                    "The original quadrilateral has equal sides",
                    "The original quadrilateral has equal diagonals (AC = BD)",
                    "The original quadrilateral has perpendicular diagonals (AC ⊥ BD)",
                    "All four angles of ABCD are acute"
                ],
                "ans": 1,
                "exp": "The sides of PQRS have lengths 1/2 AC and 1/2 BD. For all four sides of PQRS to be equal (a rhombus), we must have 1/2 AC = 1/2 BD ⇒ AC = BD (equal diagonals in ABCD)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Coordinate Geometry of Midpoints & The Fourth Vertex",
        "subtitle": "Midpoint Averaging Formula, Diagonal Intersection & Algebraic Fourth Vertex Algorithm",
        "category": "Coordinate Geometry",
        "badge": "CG-4 • C-4.2 • Coordinate Methods",
        "summary": "Coordinate geometry provides an algebraic bridge to parallelogram properties: 1. Midpoint Formula: The midpoint M of segment with endpoints (x₁, y₁) and (x₂, y₂) is M = ((x₁ + x₂)/2, (y₁ + y₂)/2). 2. Shared Midpoint Property: In a parallelogram ABCD, diagonals AC and BD bisect each other at the same point O. Therefore: Midpoint of AC = Midpoint of BD. 3. Finding the Fourth Vertex Algorithm: Given three consecutive vertices A(x_A, y_A), B(x_B, y_B), C(x_C, y_C), we find fourth vertex D(x_D, y_D) by equating midpoints: (x_A + x_C)/2 = (x_B + x_D)/2 ⇒ x_D = x_A + x_C - x_B, and (y_A + y_C)/2 = (y_B + y_D)/2 ⇒ y_D = y_A + y_C - y_B! This vector addition formula D = A + C - B is instantaneous, elegant, and completely bypasses complicated slope or distance calculations.",
        "key_points": [
            "Midpoint Coordinates: M = ((x₁ + x₂)/2, (y₁ + y₂)/2).",
            "Parallelogram Diagonal Equivalence: Midpoint of AC ≡ Midpoint of BD.",
            "Fourth Vertex Formula: x_D = x_A + x_C - x_B and y_D = y_A + y_C - y_B.",
            "Vector Interpretation: D = A + (C - B) (displacing point A by vector BC).",
            "Collinearity Verification: Midpoint methods verify whether 4 points form a parallelogram in O(1) computation."
        ],
        "narration": "How do computers calculate coordinates of shapes? In a parallelogram, diagonals AC and BD share the exact same midpoint! If you know the coordinates of vertices A, B, and C, you can find the fourth vertex D instantly with our magic formula: x-D equals x-A plus x-C minus x-B! It works every single time.",
        "sim_title": "4th Vertex Coordinate Calculator & Vector Grid",
        "checkpoints": [
            {
                "q": "If the coordinates of three vertices of a parallelogram ABCD in order are A(1, 2), B(4, 3), and C(6, 6), what are the coordinates of vertex D?",
                "options": ["(3, 5)", "(5, 7)", "(3, 7)", "(2, 4)"],
                "ans": 0,
                "exp": "Using D = A + C - B: x_D = 1 + 6 - 4 = 3, and y_D = 2 + 6 - 3 = 5. Thus, D is (3, 5)."
            },
            {
                "q": "What is the midpoint of diagonal AC for vertices A(-2, 4) and C(6, 8)?",
                "options": ["(2, 6)", "(4, 12)", "(1, 5)", "(0, 6)"],
                "ans": 0,
                "exp": "Midpoint M = ((-2 + 6)/2, (4 + 8)/2) = (4/2, 12/2) = (2, 6)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Universal Plane Tiling (Tessellation) by ANY 4-gon",
        "subtitle": "The 360° Vertex Angle Meeting, 180° Edge-Midpoint Rotations & Wallpaper Patterns",
        "category": "Plane Tiling",
        "badge": "CG-4 • C-4.2 • Plane Tiling",
        "summary": "Can any polygon tile a flat floor without gaps or overlaps? While only 3 regular polygons can tile the plane (triangles, squares, hexagons), a spectacular mathematical theorem proves: ANY arbitrary quadrilateral—no matter how scalene, lopsided, or irregular—can completely tile the entire 2D plane! Why does this work? The secret lies in two geometric principles: 1. Interior Angle Sum: The four angles of any 4-gon sum to 360° (∠A + ∠B + ∠C + ∠D = 360°). 2. Central Symmetry via Edge Midpoints: By rotating the quadrilateral by 180° around the midpoint of each of its four edges, four congruent copies of the 4-gon meet at every vertex. At every joint, exactly one copy of angle A, angle B, angle C, and angle D cluster together. Because their sum is 360°, they fill the full circle around the vertex with zero gap and zero overlap! This creates a repeating periodic lattice of interlocking parallelograms.",
        "key_points": [
            "Universal Tiling Theorem: Every quadrilateral (convex or concave) can tile the plane seamlessly.",
            "The 360° Criterion: At every junction vertex, angles A + B + C + D meet to form a complete 360° circle.",
            "Midpoint Rotation Mechanism: A 180° rotation about the midpoint of each side generates the adjacent tiling tile.",
            "Interlocking Parallelograms: Any 4-gon tile pairs with its 180° rotation to form a centrally symmetric hexagon/parallelogram that packs the plane.",
            "Applications: M.C. Escher artwork, bricklaying patterns, fabric weaving, and ceramic tile manufacturing."
        ],
        "narration": "Can an irregular, lopsided quadrilateral tile a floor? You might be shocked to learn that ANY 4-gon in the universe can tile a flat plane without leaving a single gap! How? Because its four angles add up to 360 degrees. If you rotate copies around their edge midpoints, four corners meet at every joint, forming a perfect 360-degree circle!",
        "sim_title": "Interactive 4-gon Tessellation & Floor Tiling Engine",
        "checkpoints": [
            {
                "q": "Why can ANY irregular quadrilateral tile the 2D plane without gaps or overlaps?",
                "options": [
                    "Because all quadrilaterals have 4 equal sides",
                    "Because its 4 interior angles sum to 360°, allowing one copy of each angle (A, B, C, D) to meet at every vertex",
                    "Because gravity flattens the tiles",
                    "Because quadrilaterals always have right angles"
                ],
                "ans": 1,
                "exp": "At every lattice junction, a 180° rotation around edge midpoints places angles A, B, C, and D together. Since A + B + C + D = 360°, they completely surround the vertex with zero gap."
            },
            {
                "q": "How many copies of a quadrilateral meet at each vertex in an edge-midpoint rotation tessellation?",
                "options": ["2", "3", "4", "6"],
                "ans": 2,
                "exp": "Exactly 4 copies meet at each junction vertex, contributing angles ∠A, ∠B, ∠C, and ∠D to complete the 360° circle."
            }
        ]
    },
    {
        "id": 15,
        "title": "Logical Converses & Geometric Questioning Strategies",
        "subtitle": "Framing Precise Converses, The Isosceles Trapezium Trap & Questioning Intuition",
        "category": "Mathematical Logic",
        "badge": "CG-4 • C-7.3 • Converses & Counterexamples",
        "summary": "Mastering geometry requires not only memorising theorems, but actively formulating their converses and rigorously testing them: 1. Statement: 'If a 4-gon is a rectangle, then its diagonals are equal' (TRUE). Converse: 'If the diagonals of a 4-gon are equal, is it a rectangle?' (FALSE! The celebrated counterexample is an ISOSCELES TRAPEZIUM, which has equal diagonals but non-parallel legs!). Refined Converse: 'If the diagonals of a PARALLELOGRAM are equal, is it a rectangle?' (TRUE!). 2. Statement: 'If a 4-gon is a rhombus, then its diagonals are perpendicular' (TRUE). Converse: 'If the diagonals of a 4-gon are perpendicular, is it a rhombus?' (FALSE! Counterexample: A KITE has perpendicular diagonals, but unequal adjacent sides!). Refined Converse: 'If the diagonals of a PARALLELOGRAM are perpendicular, is it a rhombus?' (TRUE!). Good mathematicians always ask: 'What minimal constraint makes the converse true?'",
        "key_points": [
            "Converse Questioning: Swapping hypothesis and conclusion tests whether a geometric property is sufficient or merely necessary.",
            "Equal Diagonals Trap: Equal diagonals alone do NOT make a rectangle (counterexample: isosceles trapezium).",
            "Perpendicular Diagonals Trap: Perpendicular diagonals alone do NOT make a rhombus (counterexample: kite).",
            "Refined Converses: Adding the precondition 'in a parallelogram' restores truth to both converses.",
            "Critical Thinking: Mathematical rigor requires testing edge cases and constructing counterexamples before accepting a claim."
        ],
        "narration": "To think like a true mathematician, always ask: Is the converse true? For instance, every rectangle has equal diagonals. But if a shape has equal diagonals, is it a rectangle? Careful! An isosceles trapezium has equal diagonals, but it is NOT a rectangle! But if it's already a parallelogram, equal diagonals DO guarantee a rectangle!",
        "sim_title": "Converse Questioning Lab & Counterexample Tester",
        "checkpoints": [
            {
                "q": "A student claims: 'If the diagonals of a quadrilateral are equal in length, it must be a rectangle'. What is a valid counterexample?",
                "options": [
                    "A square",
                    "An isosceles trapezium",
                    "A rhombus with 60° angles",
                    "A scalene triangle"
                ],
                "ans": 1,
                "exp": "An isosceles trapezium has equal diagonals, but its non-parallel sides are not parallel, so it is not even a parallelogram, completely refuting the claim."
            },
            {
                "q": "What additional condition turns the false claim 'perpendicular diagonals implies a rhombus' into a TRUE theorem?",
                "options": [
                    "The quadrilateral must have at least one obtuse angle",
                    "The quadrilateral must already be known to be a parallelogram",
                    "The diagonals must have integer lengths",
                    "The perimeter must be greater than 20 cm"
                ],
                "ans": 1,
                "exp": "In a parallelogram, diagonals already bisect each other. If they are also perpendicular, △AOB ≅ △COB by SAS, proving adjacent sides are equal (a rhombus)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Hands-on Paper Folding, Origami Patterns & Synthesis",
        "subtitle": "Crease Patterns, Varignon Paper Folding & Algorithmic Polygon Classification Trees",
        "category": "Hands-on Synthesis",
        "badge": "CG-4 • C-4.2 • C-7.3 • Paper Folding & Algorithms",
        "summary": "1. Origami & Paper Folding Deductions: Concrete geometric patterns can be discovered without compasses using simple paper folds: - Folding a sheet in half and creasing matches parallel lines and medians. - The Varignon Fold: Cut out any random 4-gon from paper. Fold each vertex to the opposite side to form corner triangles along the edge midpoints. The four corner flaps fold inwards to cover the central Varignon parallelogram EXACTLY twice, visually proving Area(PQRS) = 1/2 Area(ABCD)! 2. Computational Classification Algorithm: Modern CAD and robotics software classify 4-gons using vector arithmetic: Given vertices A, B, C, D: Calculate edge vectors v₁ = B - A, v₂ = C - B, v₃ = D - C, v₄ = A - D. Test: Is v₁ = -v₃ and v₂ = -v₄? If YES → Parallelogram! If YES and dot product v₁ · v₂ = 0 → Rectangle! If YES and |v₁| = |v₂| → Rhombus! If both → Square! All evaluated in O(1) constant time.",
        "key_points": [
            "Varignon Paper Fold: Folding corner flaps along midpoints shows the 4 corners have total area equal to the central parallelogram.",
            "Crease Geometry: Axiomatic folding (Huzita-Hatori axioms) constructs bisectors, perpendiculars, and midpoints physically.",
            "CAD Vector Decision Tree: v₁ = -v₃ and v₂ = -v₄ tests parallelism in O(1) time.",
            "Orthogonality via Dot Product: v₁ · v₂ = 0 detects 90° right angles (rectangles and squares).",
            "Synthesis of Geometry: Combining physical paper manipulation with computational vector mathematics."
        ],
        "narration": "Let's wrap up with hands-on discovery and computer algorithms! If you fold a paper quadrilateral along its edge midpoints, the four corner flaps fold inside to cover the central parallelogram with zero overlap! And in computer graphics, vector dot products classify any 4-gon into a parallelogram, rectangle, or square in a fraction of a microsecond!",
        "sim_title": "Interactive Paper Folding & CAD Vector Classifier",
        "checkpoints": [
            {
                "q": "In the Varignon paper folding activity, when the four corner triangles of a quadrilateral are folded along the midpoints, their total combined area equals:",
                "options": [
                    "One-quarter of the quadrilateral's area",
                    "Exactly the area of the central Varignon parallelogram (half the total area)",
                    "Twice the total area",
                    "Zero"
                ],
                "ans": 1,
                "exp": "Since the central Varignon parallelogram occupies 1/2 of the total area, the remaining four corner triangles also sum to 1/2 of the total area, covering the parallelogram perfectly."
            },
            {
                "q": "In computer geometry, what vector test confirms that consecutive sides AB and BC of a parallelogram form a 90° angle (making it a rectangle)?",
                "options": [
                    "Their cross product is 1",
                    "Their dot product equals zero (AB · BC = 0)",
                    "Their lengths sum to 180",
                    "Their slopes are both positive"
                ],
                "ans": 1,
                "exp": "Two non-zero vectors are perpendicular if and only if their scalar dot product is zero: v₁ · v₂ = 0."
            }
        ]
    }
]

QUIZZES = [
    {
        "slide_id": 17,
        "title": "Mastery Quiz 1: Parallelogram Characterisations & Theorems",
        "subtitle": "Theorems 8.1 through 8.8, Opposites Sides & Angles, and CPCTC",
        "category": "Mastery Challenge",
        "badge": "Quiz 1 • Parallelogram Theorems",
        "questions": [
            {
                "q": "If the diagonals of a quadrilateral bisect each other at right angles, what is the quadrilateral?",
                "options": ["Rectangle", "Trapezium", "Rhombus", "Kite only"],
                "ans": 2,
                "exp": "Diagonals bisecting each other proves it is a parallelogram. If they are also perpendicular, adjacent sides are equal by SAS, proving it is a rhombus."
            },
            {
                "q": "In a parallelogram ABCD, ∠A = (3x - 20)° and ∠C = (x + 40)°. What is the measure of ∠B?",
                "options": ["70°", "110°", "140°", "150°"],
                "ans": 1,
                "exp": "Opposite angles are equal: 3x - 20 = x + 40 ⇒ 2x = 60 ⇒ x = 30°. Thus ∠A = 3(30) - 20 = 70°. Consecutive angles are supplementary: ∠B = 180° - 70° = 110°."
            },
            {
                "q": "Theorem 8.1 states that a diagonal of a parallelogram divides it into two congruent triangles. Which congruence criterion proves this?",
                "options": ["SAS", "ASA", "SSS", "RHS"],
                "ans": 1,
                "exp": "Transversal AC creates two pairs of equal alternate interior angles, and AC is common. △ABC ≅ △CDA by ASA."
            },
            {
                "q": "Which of the following is NOT a property of every parallelogram?",
                "options": [
                    "Opposite sides are parallel",
                    "Opposite angles are equal",
                    "Diagonals are equal in length",
                    "Diagonals bisect each other"
                ],
                "ans": 2,
                "exp": "Diagonals are equal in length ONLY in rectangles and squares, not in general parallelograms or rhombuses."
            },
            {
                "q": "In quadrilateral ABCD, AB = CD and AB ∥ CD. What theorem guarantees ABCD is a parallelogram?",
                "options": ["Theorem 8.1", "Theorem 8.4", "Theorem 8.8", "Midpoint Theorem"],
                "ans": 2,
                "exp": "Theorem 8.8 states: A quadrilateral is a parallelogram if ONE pair of opposite sides is both equal and parallel."
            },
            {
                "q": "If ABCD is a rhombus, what is the angle between its diagonals AC and BD?",
                "options": ["45°", "60°", "90°", "120°"],
                "ans": 2,
                "exp": "The diagonals of a rhombus are perpendicular bisectors of each other, intersecting at 90°."
            },
            {
                "q": "In parallelogram ABCD, perimeter is 40 cm and side AB = 12 cm. What is the length of side BC?",
                "options": ["8 cm", "14 cm", "16 cm", "28 cm"],
                "ans": 0,
                "exp": "Perimeter = 2(AB + BC) = 40 ⇒ AB + BC = 20. With AB = 12 cm, BC = 20 - 12 = 8 cm."
            },
            {
                "q": "If the angle bisectors of ∠A and ∠B of parallelogram ABCD intersect at P, what is the measure of ∠APB?",
                "options": ["45°", "60°", "90°", "120°"],
                "ans": 2,
                "exp": "∠A + ∠B = 180°. In △APB, the angles are ∠A/2 and ∠B/2. Their sum is (∠A + ∠B)/2 = 90°. Hence ∠APB = 180° - 90° = 90°."
            },
            {
                "q": "A quadrilateral whose all sides are equal and all angles are equal is a:",
                "options": ["Rectangle", "Rhombus", "Square", "Trapezium"],
                "ans": 2,
                "exp": "By definition, a regular 4-gon (equilateral and equiangular) is a square."
            },
            {
                "q": "Diagonals of a rectangle ABCD intersect at O. If ∠BOC = 70°, what is ∠ODA?",
                "options": ["35°", "55°", "70°", "110°"],
                "ans": 1,
                "exp": "Vertically opposite angle ∠AOD = ∠BOC = 70°. In rectangle, diagonals are equal and bisect, so OA = OD. △OAD is isosceles: ∠ODA = (180° - 70°)/2 = 55°."
            }
        ]
    },
    {
        "slide_id": 18,
        "title": "Mastery Quiz 2: Midpoint Theorem & Median Concurrency",
        "subtitle": "Theorems 8.9 & 8.10, Triangle Midpoints & 2:1 Centroid Division",
        "category": "Mastery Challenge",
        "badge": "Quiz 2 • Midpoint & Centroid",
        "questions": [
            {
                "q": "In △ABC, D and E are midpoints of AB and AC. If DE = 4.5 cm, what is the length of BC?",
                "options": ["4.5 cm", "9 cm", "13.5 cm", "18 cm"],
                "ans": 1,
                "exp": "By the Midpoint Theorem, DE = 1/2 BC. Therefore, BC = 2 × DE = 2 × 4.5 cm = 9 cm."
            },
            {
                "q": "In △ABC, D, E, F are the midpoints of sides AB, BC, CA. If perimeter of △ABC is 32 cm, what is the perimeter of △DEF?",
                "options": ["8 cm", "16 cm", "24 cm", "64 cm"],
                "ans": 1,
                "exp": "Each side of △DEF is half the corresponding side of △ABC (DE = 1/2 AC, EF = 1/2 AB, FD = 1/2 BC). Perimeter(△DEF) = 1/2 × Perimeter(△ABC) = 32 / 2 = 16 cm."
            },
            {
                "q": "In △ABC, G is the centroid and median BE = 12 cm. What is the length of segment BG?",
                "options": ["4 cm", "6 cm", "8 cm", "9 cm"],
                "ans": 2,
                "exp": "The centroid divides the median in the ratio 2 : 1 from vertex to midpoint. BG = (2/3) × BE = (2/3) × 12 cm = 8 cm."
            },
            {
                "q": "The Converse of the Midpoint Theorem states that a line through the midpoint of one side parallel to another side:",
                "options": [
                    "Is perpendicular to the third side",
                    "Bisects the third side",
                    "Is equal to one-third of the third side",
                    "Passes through the centroid"
                ],
                "ans": 1,
                "exp": "Theorem 8.10 (Converse) states that the line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side."
            },
            {
                "q": "In △ABC, D is the midpoint of AB and DE ∥ BC meets AC at E. If AE = 7 cm, what is AC?",
                "options": ["7 cm", "14 cm", "21 cm", "28 cm"],
                "ans": 1,
                "exp": "By the Converse of Midpoint Theorem, E is the midpoint of AC. Thus AC = 2 × AE = 2 × 7 = 14 cm."
            },
            {
                "q": "In the proof of the concurrency of medians, which auxiliary quadrilateral formed by the medians is proven to be a parallelogram?",
                "options": ["ABCD", "FEQP", "ABEF", "CDEG"],
                "ans": 1,
                "exp": "Quadrilateral FEQP (where F, E are triangle midpoints and P, Q are lower median midpoints) has FE ∥ PQ and FE = PQ, proving it is a parallelogram."
            },
            {
                "q": "The four smaller triangles formed by joining the midpoints of the three sides of any triangle △ABC are:",
                "options": [
                    "Equilateral only",
                    "All congruent to each other",
                    "Of unequal areas",
                    "Right-angled"
                ],
                "ans": 1,
                "exp": "By the Midpoint Theorem, all four sub-triangles have sides equal to half the corresponding sides of △ABC, making them all mutually congruent by SSS."
            },
            {
                "q": "If the area of △ABC is 60 cm², what is the area of the medial triangle formed by joining its side midpoints?",
                "options": ["15 cm²", "20 cm²", "30 cm²", "45 cm²"],
                "ans": 0,
                "exp": "The medial triangle is one of four congruent triangles partitioning △ABC. Its area is 60 / 4 = 15 cm²."
            },
            {
                "q": "In a right triangle with hypotenuse 10 cm, what is the length of the segment connecting the midpoints of the two legs?",
                "options": ["2.5 cm", "5 cm", "7.5 cm", "10 cm"],
                "ans": 1,
                "exp": "By the Midpoint Theorem, the segment connecting the midpoints of the two legs is parallel to and half the length of the hypotenuse: 10 / 2 = 5 cm."
            },
            {
                "q": "What physical property does the centroid G represent for a uniform triangular cardboard sheet?",
                "options": [
                    "The point of maximum friction",
                    "The Center of Gravity / Center of Mass (balance point)",
                    "The optical focus point",
                    "The perimeter midpoint"
                ],
                "ans": 1,
                "exp": "The centroid is the geometric center and the exact Center of Mass (Center of Gravity) of a uniform planar lamina; the sheet will balance on a pin placed at G."
            }
        ]
    },
    {
        "slide_id": 19,
        "title": "Mastery Quiz 3: Varignon's Theorem & Coordinate Geometry",
        "subtitle": "Midpoint Polygons, Area Invariants & The 4th Vertex Algorithm",
        "category": "Mastery Challenge",
        "badge": "Quiz 3 • Varignon & Coordinates",
        "questions": [
            {
                "q": "Varignon's Theorem states that the 4-gon formed by joining the midpoints of ANY 4-gon is always a:",
                "options": ["Trapezium", "Rectangle", "Parallelogram", "Rhombus"],
                "ans": 2,
                "exp": "By drawing a diagonal and applying the Midpoint Theorem, opposite sides of the midpoint polygon are both parallel to and half of that diagonal, proving it is a parallelogram."
            },
            {
                "q": "If the diagonals of quadrilateral ABCD are perpendicular (AC ⊥ BD), what specific shape is the Varignon parallelogram PQRS?",
                "options": ["Parallelogram only", "Rectangle", "Rhombus", "Trapezium"],
                "ans": 1,
                "exp": "The sides of PQRS are parallel to the diagonals of ABCD. If the diagonals are perpendicular (AC ⊥ BD), the adjacent sides of PQRS meet at 90°, making PQRS a rectangle."
            },
            {
                "q": "If the diagonals of quadrilateral ABCD are equal (AC = BD), what specific shape is the Varignon parallelogram PQRS?",
                "options": ["Rectangle", "Rhombus", "Trapezium", "Kite"],
                "ans": 1,
                "exp": "The side lengths of PQRS are 1/2 AC and 1/2 BD. If AC = BD, all four sides of PQRS are equal, making it a rhombus."
            },
            {
                "q": "Three vertices of a parallelogram in order are A(2, 3), B(6, 5), and C(8, 9). What are the coordinates of vertex D?",
                "options": ["(4, 7)", "(5, 8)", "(4, 6)", "(3, 8)"],
                "ans": 0,
                "exp": "Using the 4th vertex formula D = A + C - B: x_D = 2 + 8 - 6 = 4, and y_D = 3 + 9 - 5 = 7. Thus D is (4, 7)."
            },
            {
                "q": "If the area of a convex quadrilateral is 72 cm², what is the area of its Varignon midpoint parallelogram?",
                "options": ["18 cm²", "36 cm²", "54 cm²", "72 cm²"],
                "ans": 1,
                "exp": "The area of the Varignon parallelogram is always exactly half the area of the original quadrilateral: 72 / 2 = 36 cm²."
            },
            {
                "q": "What is the midpoint of the segment joining P(-4, 7) and Q(6, -3)?",
                "options": ["(1, 2)", "(2, 4)", "(5, 2)", "(-1, 2)"],
                "ans": 0,
                "exp": "Midpoint M = ((-4 + 6)/2, (7 + (-3))/2) = (2/2, 4/2) = (1, 2)."
            },
            {
                "q": "If the perimeter of the Varignon parallelogram PQRS is 30 cm, what is the sum of the diagonals AC + BD of the parent quadrilateral?",
                "options": ["15 cm", "30 cm", "60 cm", "45 cm"],
                "ans": 1,
                "exp": "The sides of PQRS are 1/2 AC, 1/2 BD, 1/2 AC, 1/2 BD. Perimeter = 2(1/2 AC + 1/2 BD) = AC + BD = 30 cm."
            },
            {
                "q": "In a parallelogram ABCD, the diagonals intersect at M(3, 4). If vertex A is (1, 1), what are the coordinates of vertex C?",
                "options": ["(5, 7)", "(2, 3)", "(4, 5)", "(6, 8)"],
                "ans": 0,
                "exp": "M is the midpoint of AC: (1 + x_C)/2 = 3 ⇒ x_C = 5, and (1 + y_C)/2 = 4 ⇒ y_C = 7. Thus C is (5, 7)."
            },
            {
                "q": "If the midpoints of the sides of a RECTANGLE are joined in order, the resulting 4-gon is always a:",
                "options": ["Square", "Rhombus", "Non-rhombus parallelogram", "Trapezium"],
                "ans": 1,
                "exp": "A rectangle has equal diagonals (AC = BD). Since AC = BD, the Varignon parallelogram has 4 equal sides, making it a rhombus."
            },
            {
                "q": "If the midpoints of the sides of a RHOMBUS are joined in order, the resulting 4-gon is always a:",
                "options": ["Rectangle", "Square", "Rhombus", "Kite"],
                "ans": 0,
                "exp": "A rhombus has perpendicular diagonals (AC ⊥ BD). Since the diagonals are perpendicular, the Varignon parallelogram has 90° angles, making it a rectangle."
            }
        ]
    },
    {
        "slide_id": 20,
        "title": "Mastery Quiz 4: Symmetry, Tessellations & Logical Converses",
        "subtitle": "Rotational & Reflection Symmetries, Plane Tiling & False Converses",
        "category": "Mastery Challenge",
        "badge": "Quiz 4 • Advanced Synthesis",
        "questions": [
            {
                "q": "Which quadrilateral can tile the entire 2D plane without gaps or overlaps?",
                "options": [
                    "Only squares and rectangles",
                    "Only parallelograms and rhombuses",
                    "ANY arbitrary planar quadrilateral (even scalene or concave)",
                    "No quadrilateral can tile the plane"
                ],
                "ans": 2,
                "exp": "Any quadrilateral can tile the plane because its interior angles sum to 360°, allowing four copies (one of each angle A, B, C, D) to meet seamlessly at every vertex via 180° edge-midpoint rotations."
            },
            {
                "q": "How many axes of reflection symmetry does a rhombus (that is not a square) have?",
                "options": ["0", "1", "2", "4"],
                "ans": 2,
                "exp": "A non-square rhombus has exactly 2 axes of reflection symmetry, which are its two diagonals."
            },
            {
                "q": "What is the order of rotational symmetry of a square?",
                "options": ["1", "2", "3", "4"],
                "ans": 3,
                "exp": "A square matches itself under rotations of 90°, 180°, 270°, and 360°, giving it an order-4 rotational symmetry."
            },
            {
                "q": "Statement: 'If a quadrilateral is a square, its diagonals are perpendicular bisectors of each other'. Is the converse 'If the diagonals of a quadrilateral are perpendicular bisectors of each other, it is a square' true or false?",
                "options": [
                    "True, it guarantees a square",
                    "False; a non-square rhombus has perpendicular bisecting diagonals (counterexample)",
                    "True by SAS",
                    "Cannot be determined"
                ],
                "ans": 1,
                "exp": "The converse is false. The diagonals of any rhombus are perpendicular bisectors of each other, but the sides do not need to meet at 90° (it is not a square unless diagonals are also equal)."
            },
            {
                "q": "In the context of parallelograms, what does 'central symmetry' mean?",
                "options": [
                    "All sides are equidistant from the center",
                    "A 180° rotation about the diagonal intersection maps the parallelogram onto itself",
                    "It has four lines of symmetry",
                    "Its diagonals are equal"
                ],
                "ans": 1,
                "exp": "Central symmetry (point inversion) means that a half-turn (180° rotation) around the center O maps every point P to opposite point P', leaving the figure invariant."
            },
            {
                "q": "If a line passing through the center of symmetry O of a parallelogram intersects opposite sides at P and Q, what is the relation between OP and OQ?",
                "options": ["OP = OQ", "OP = 2 OQ", "OP + OQ = AC", "OP ⊥ OQ"],
                "ans": 0,
                "exp": "By central symmetry about center O, point P maps to point Q under a 180° rotation, meaning O is the exact midpoint of segment PQ (OP = OQ)."
            },
            {
                "q": "A kite has diagonals that are perpendicular. Does a kite have central symmetry?",
                "options": [
                    "Yes, always",
                    "No, because rotating a kite by 180° turns its wide end to its narrow end (unless it is a rhombus)",
                    "Only if it has right angles",
                    "Yes, about its longest diagonal"
                ],
                "ans": 1,
                "exp": "A kite has line reflection symmetry along its main diagonal, but lacks 180° central rotational symmetry because its opposite sides are unequal."
            },
            {
                "q": "In the Varignon paper folding activity, when a paper quadrilateral is folded along its four side midpoints, what shape is formed by the creases?",
                "options": ["Trapezium", "Kite", "Parallelogram", "Isosceles triangle"],
                "ans": 2,
                "exp": "The crease lines connect the midpoints of adjacent sides, forming the Varignon parallelogram."
            },
            {
                "q": "What is the order of rotational symmetry of a general non-rhombus, non-rectangle parallelogram?",
                "options": ["1", "2", "3", "4"],
                "ans": 1,
                "exp": "A general parallelogram has order-2 rotational symmetry (mapping onto itself after 180° and 360° rotations)."
            },
            {
                "q": "Which of the following converses is completely TRUE without needing extra preconditions?",
                "options": [
                    "If diagonals are equal, it is a rectangle",
                    "If diagonals are perpendicular, it is a rhombus",
                    "If diagonals bisect each other, it is a parallelogram",
                    "If one pair of sides is parallel, it is a parallelogram"
                ],
                "ans": 2,
                "exp": "Theorem 8.7 states: If the diagonals of any quadrilateral bisect each other, it is guaranteed to be a parallelogram (proven by SAS between vertically opposite triangles)."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Total Slides: {len(SLIDES)}")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    print(f"Total Quiz Slides: {len(QUIZZES)}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, "Must have exactly 16 content slides"
    assert total_cp == 32, "Must have exactly 32 checkpoints (2 per slide)"
    assert len(QUIZZES) == 4, "Must have exactly 4 quiz slides"
    assert total_qz == 40, "Must have exactly 40 quiz questions (10 per quiz slide)"
    print("All assertions passed successfully!")


"""
Data module for Class 9 Mathematics Chapter 8: Lines and Angles
Syllabus: CG-7, C-7.1, C-7.3, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Notion of a Ray & Formation of Angles",
        "subtitle": "Endpoints, Directed Rays, Common Vertex, Arms & Angle Interiors",
        "category": "Foundations",
        "badge": "CG-7 • C-7.1 • Rays & Angles",
        "summary": "In geometry, a ray is a portion of a straight line that has one fixed starting point (called its endpoint or origin) and extends endlessly in one direction, denoted as ray OA. An angle is the geometric figure formed by two rays originating from the exact same common starting point. The common starting point O is called the Vertex of the angle, and the two rays OA and OB are called the Arms or sides of the angle. An angle is designated as ∠AOB or ∠BOA. The region enclosed between the two arms is called the interior of the angle.",
        "key_points": [
            "Ray: A part of a line with one fixed endpoint, extending infinitely in one direction (ray OA).",
            "Angle: Formed when two rays share a common initial point (Vertex).",
            "The two rays are called the Arms of the angle.",
            "Notation: Symbol ∠ is used; vertex letter is always placed in the middle (∠AOB).",
            "An angle partitions the plane into three distinct sets of points: the interior, the angle itself, and the exterior."
        ],
        "narration": "Welcome to Lines and Angles! A ray starts at one fixed point and shoots endlessly in one direction, like a beam of light. When two rays share the exact same starting point, they form an angle! That shared point is the vertex, and the two rays are the arms.",
        "sim_title": "Ray Spinner & Angle Generator",
        "checkpoints": [
            {
                "q": "What is the common starting point of two rays forming an angle called?",
                "options": ["Origin", "Vertex", "Intersect", "Midpoint"],
                "ans": 1,
                "exp": "The common starting point of the two rays forming an angle is called the Vertex."
            },
            {
                "q": "In the notation ∠XYZ, which letter represents the vertex of the angle?",
                "options": ["X", "Y", "Z", "Any of them"],
                "ans": 1,
                "exp": "By mathematical convention, the middle letter (Y) always designates the vertex of the angle."
            }
        ]
    },
    {
        "id": 2,
        "title": "Measures of Angles & Angle Classification",
        "subtitle": "Degree Measurement System, Right Angles, Straight Angles & Reflex Angles",
        "category": "Classification",
        "badge": "CG-7 • C-7.1 • Angle Types",
        "summary": "Angle measure is quantified in degrees (°), where one complete revolution of a ray about its vertex is divided into 360 equal parts (1 complete angle = 360°). Angles are classified by their magnitude: (1) Acute angle: 0° < θ < 90°; (2) Right angle: θ = 90° (one quarter turn); (3) Obtuse angle: 90° < θ < 180°; (4) Straight angle: θ = 180° (half turn, equals two right angles, arms form a straight line); (5) Reflex angle: 180° < θ < 360°; (6) Complete angle: θ = 360°.",
        "key_points": [
            "One complete rotation = 360°; 1 right angle = 90°; 1 straight angle = 180° (equals 2 right angles).",
            "Acute angle: Strictly between 0° and 90° (0° < θ < 90°).",
            "Right angle: Exactly 90° (arms are perpendicular: OA ⊥ OB).",
            "Obtuse angle: Strictly between 90° and 180° (90° < θ < 180°).",
            "Reflex angle: Strictly between 180° and 360° (180° < θ < 360°)."
        ],
        "narration": "Angles come in all sizes! A 90-degree angle is a right angle. Any angle smaller than 90 degrees is acute—sharp and small. Between 90 and 180 degrees is obtuse. A straight line is exactly 180 degrees, which equals two right angles! And anything larger than 180 degrees is called a reflex angle.",
        "sim_title": "Interactive Angle Gauge & Dynamic Classifier",
        "checkpoints": [
            {
                "q": "An angle measuring 135° is classified as which type of angle?",
                "options": ["Acute angle", "Right angle", "Obtuse angle", "Reflex angle"],
                "ans": 2,
                "exp": "Since 90° < 135° < 180°, it is an Obtuse angle."
            },
            {
                "q": "How many right angles make up a straight angle?",
                "options": ["1 right angle", "2 right angles", "3 right angles", "4 right angles"],
                "ans": 1,
                "exp": "A straight angle measures 180°, which equals 2 right angles (2 × 90° = 180°)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Complementary & Supplementary Angles",
        "subtitle": "Sum to 90° vs Sum to 180° & Algebraic Complement/Supplement Finding",
        "category": "Angle Pairs",
        "badge": "CG-7 • C-7.1 • Complement & Supplement",
        "summary": "Two angles are called Complementary Angles if their sum is 90° (α + β = 90°); each angle is said to be the complement of the other. For example, 35° and 55° are complementary because 35° + 55° = 90°. Two angles are called Supplementary Angles if their sum is 180° (α + β = 180°); each is the supplement of the other. For example, 70° and 110° are supplementary because 70° + 110° = 180°. Notice that complementary and supplementary angles do NOT need to be adjacent; they can be separate angles.",
        "key_points": [
            "Complementary angles: α + β = 90° (Complement of θ is 90° - θ).",
            "Supplementary angles: α + β = 180° (Supplement of θ is 180° - θ).",
            "Complementary angles can only be acute (both must be < 90°).",
            "Supplementary angles can consist of two right angles, or one acute and one obtuse angle.",
            "Angles need not share a vertex to be complementary or supplementary."
        ],
        "narration": "Complementary and supplementary angles are fundamental pairs. If two angles add up to 90 degrees, they are complementary! Think 'C' for Corner (90°). If they add up to 180 degrees, they are supplementary! Think 'S' for Straight line (180°).",
        "sim_title": "Twin Angle Complement & Supplement Balancer",
        "checkpoints": [
            {
                "q": "What is the complement of an angle measuring 38°?",
                "options": ["52°", "142°", "62°", "42°"],
                "ans": 0,
                "exp": "Complement = 90° - 38° = 52°."
            },
            {
                "q": "An angle is equal to its own supplement. What is the measure of the angle?",
                "options": ["45°", "90°", "180°", "60°"],
                "ans": 1,
                "exp": "Let the angle be x. x + x = 180° ⇒ 2x = 180° ⇒ x = 90°."
            }
        ]
    },
    {
        "id": 4,
        "title": "Adjacent Angles & Linear Pair Axiom (Axiom 6.1)",
        "subtitle": "Common Arm, Opposite Non-Common Arms & Sum on a Line = 180°",
        "category": "Linear Pair",
        "badge": "CG-7 • C-7.1 • Linear Pair Axiom",
        "summary": "Two angles are called Adjacent Angles if: (1) They have a common vertex O; (2) They have a common arm OC; (3) Their non-common arms OA and OB lie on opposite sides of the common arm. Axiom 6.1 (Linear Pair Axiom): 'If a ray stands on a line, then the sum of two adjacent angles so formed is 180°.' When the non-common arms of two adjacent angles form a straight line, the adjacent angles are said to form a Linear Pair of angles (∠AOC + ∠BOC = 180°).",
        "key_points": [
            "Adjacent angles criteria: Common vertex, common arm, non-common arms on opposite sides.",
            "Axiom 6.1: A ray standing on a straight line forms two adjacent angles whose sum is 180°.",
            "Linear Pair: Adjacent angles whose non-common arms are opposite rays forming a straight line.",
            "Linear pair angles are always supplementary (sum = 180°).",
            "If ∠AOC = x and ∠BOC = y, then x + y = 180°."
        ],
        "narration": "Look at adjacent angles: they are next-door neighbors! They share a common vertex and a common wall. When a ray stands on a straight line, it divides the straight angle into two adjacent pieces. Axiom 6.1 tells us these two pieces always add up to 180 degrees!",
        "sim_title": "Linear Pair Dynamic Beam Visualizer",
        "checkpoints": [
            {
                "q": "Ray OC stands on line AB. If ∠AOC = 65°, what is the measure of ∠BOC?",
                "options": ["115°", "125°", "25°", "135°"],
                "ans": 0,
                "exp": "By the Linear Pair Axiom: ∠AOC + ∠BOC = 180° ⇒ 65° + ∠BOC = 180° ⇒ ∠BOC = 115°."
            },
            {
                "q": "Which condition is NOT required for two angles to be adjacent?",
                "options": [
                    "They must share a common vertex",
                    "They must share a common arm",
                    "Their sum must always equal 180°",
                    "Their non-common arms must lie on opposite sides of the common arm"
                ],
                "ans": 2,
                "exp": "Adjacent angles do not have to sum to 180°; they only sum to 180° when they form a linear pair on a straight line."
            }
        ]
    },
    {
        "id": 5,
        "title": "Converse of Linear Pair Axiom & Straight Line Criteria (Axiom 6.2)",
        "subtitle": "Proving that Non-Common Arms Form a Straight Line",
        "category": "Linear Pair Converse",
        "badge": "CG-7 • C-7.3 • Straight Line Criterion",
        "summary": "Axiom 6.2 (Converse of Linear Pair Axiom): 'If the sum of two adjacent angles is 180°, then the non-common arms of the angles form a line.' Axiom 6.1 and Axiom 6.2 together are called the Linear Pair Axiom. This converse axiom provides a vital geometric test: to prove that three points A, O, B lie on a straight line (are collinear), it is necessary and sufficient to show that the adjacent angles ∠AOC and ∠BOC sum to 180°.",
        "key_points": [
            "Axiom 6.2: If adjacent angles sum to 180°, their non-common arms form a single straight line.",
            "Two-way equivalence: Ray on a line ⇔ Adjacent angles sum to 180°.",
            "Collinearity proof: Proving that A-O-B is a straight line requires proving ∠AOC + ∠COB = 180°.",
            "Enables testing structural straightness in carpentry, masonry, and computer graphics.",
            "Forms the foundation for proving theorems on intersecting and parallel lines."
        ],
        "narration": "Axiom 6.2 is the converse: if two adjacent angles add up to 180 degrees, their outer arms MUST form a straight line! This is how architects and builders test if a beam is perfectly straight: check if the angles add up to 180 degrees!",
        "sim_title": "Straight Line Alignment Verifier & Angle Snapper",
        "checkpoints": [
            {
                "q": "Two adjacent angles ∠AOC and ∠BOC measure (2x + 10)° and (3x + 20)°. If AOB is a straight line, what is x?",
                "options": ["30", "25", "35", "40"],
                "ans": 0,
                "exp": "(2x + 10) + (3x + 20) = 180 ⇒ 5x + 30 = 180 ⇒ 5x = 150 ⇒ x = 30."
            },
            {
                "q": "If ∠POQ = 110° and ∠QOR = 70° are adjacent angles, what can be deduced about rays OP and OR?",
                "options": [
                    "They are perpendicular",
                    "They form a single straight line POR",
                    "They are parallel",
                    "They form a reflex angle"
                ],
                "ans": 1,
                "exp": "Since 110° + 70° = 180°, by Axiom 6.2, rays OP and OR are opposite rays forming a straight line POR."
            }
        ]
    },
    {
        "id": 6,
        "title": "Angle Sum Around a Point & Rays in a Star",
        "subtitle": "The 360° Complete Revolution Property for Multiple Rays",
        "category": "Angle Sum",
        "badge": "CG-7 • C-7.1 • Angles at a Point",
        "summary": "When multiple rays emanate from a single common vertex O, the sum of all consecutive adjacent angles around that point equals 360° (a complete angle). Theorem / Property: 'The sum of all the angles formed around a point is 360°.' To prove this, we draw a ray opposite to one of the given rays, creating a straight line, and apply the linear pair property to both sides: the top half sums to 180° and the bottom half sums to 180°, yielding 180° + 180° = 360°.",
        "key_points": [
            "Sum of all consecutive angles meeting at a point is 360° (one full revolution).",
            "Proof technique: Construct an opposite auxiliary ray to create a straight line, dividing the plane into two 180° halves.",
            "Applicable to clock faces (360° divided into 12 hours = 30° per hour).",
            "Radial spokes in bicycle wheels and turbine rotors distribute angles summing to 360°.",
            "If n equal rays emanate from a point, each angle is 360° / n."
        ],
        "narration": "What happens when many rays meet at a single point like spokes on a bicycle wheel? They make a full turn! The sum of all angles around a point is always 360 degrees. If you have 6 equal spokes, each angle is 360 divided by 6, which is 60 degrees!",
        "sim_title": "Radial Angle Wheel & 360° Sum Engine",
        "checkpoints": [
            {
                "q": "Four rays meet at point O forming angles x°, 2x°, 3x°, and 4x°. What is the value of x?",
                "options": ["36", "30", "40", "45"],
                "ans": 0,
                "exp": "x + 2x + 3x + 4x = 360° ⇒ 10x = 360° ⇒ x = 36."
            },
            {
                "q": "What is the angle between the hour hand and the minute hand of a clock at 4:00 o'clock?",
                "options": ["90°", "120°", "150°", "100°"],
                "ans": 1,
                "exp": "Each hour represents 360° / 12 = 30°. At 4:00, the hands are 4 hours apart: 4 × 30° = 120°."
            }
        ]
    },
    {
        "id": 7,
        "title": "Vertically Opposite Angles Theorem (Theorem 6.1)",
        "subtitle": "Proof by Linear Pairs: Opposite Angles Formed by Intersecting Lines are Equal",
        "category": "Theorems",
        "badge": "CG-7 • C-7.3 • Vertically Opposite Angles",
        "summary": "Theorem 6.1: 'If two lines intersect each other, then the vertically opposite angles are equal.' Formal Deductive Proof: Let lines AB and CD intersect at point O. Ray OA stands on line CD ⇒ ∠AOC + ∠AOD = 180° (by Linear Pair Axiom). Ray OD stands on line AB ⇒ ∠AOD + ∠BOD = 180° (by Linear Pair Axiom). By Euclid's Axiom 1 (things equal to the same thing are equal): ∠AOC + ∠AOD = ∠AOD + ∠BOD. Subtracting ∠AOD from both sides (Axiom 3): ∠AOC = ∠BOD! Similarly, ∠AOD = ∠BOC.",
        "key_points": [
            "Theorem 6.1: Vertically opposite angles are equal (∠AOC = ∠BOD and ∠AOD = ∠BOC).",
            "Proof uses only the Linear Pair Axiom and Euclid's Axioms 1 and 3.",
            "Vertically opposite angles share a vertex but have no common arm (their arms form opposite rays).",
            "Independent of angle magnitude: holds whether intersection is acute, right, or obtuse.",
            "Core building block for proving parallel line transversal theorems."
        ],
        "narration": "When two lines cross each other like a pair of scissors, they create two pairs of vertically opposite angles. Theorem 6.1 proves that these opposite angles are always identical! Watch the proof: both angles share a linear pair with the middle angle. Subtracting the shared angle proves they must be equal!",
        "sim_title": "Scissors Mechanism & Vertically Opposite Angle Prover",
        "checkpoints": [
            {
                "q": "Two lines AB and CD intersect at O. If ∠AOC = 50°, what is the measure of vertically opposite angle ∠BOD?",
                "options": ["50°", "130°", "40°", "140°"],
                "ans": 0,
                "exp": "Vertically opposite angles are equal (Theorem 6.1), so ∠BOD = ∠AOC = 50°."
            },
            {
                "q": "In the intersection of lines AB and CD, if ∠AOC = 50°, what is the measure of adjacent angle ∠AOD?",
                "options": ["50°", "130°", "90°", "100°"],
                "ans": 1,
                "exp": "∠AOC and ∠AOD form a linear pair on line CD: ∠AOD = 180° - 50° = 130°."
            }
        ]
    },
    {
        "id": 8,
        "title": "Angle Bisectors of a Linear Pair: Perpendicularity Proof",
        "subtitle": "Proving that the Bisectors of a Linear Pair Form a 90° Right Angle",
        "category": "Geometric Proofs",
        "badge": "CG-7 • C-7.3 • Bisector Orthogonality",
        "summary": "An Angle Bisector is a ray that divides an angle into two equal halves. Theorem: 'The bisectors of the two angles forming a linear pair are perpendicular to each other.' Proof: Let ray OC stand on line AB, forming linear pair angles ∠AOC and ∠BOC with ∠AOC + ∠BOC = 180°. Let ray OE bisect ∠AOC (so ∠COE = ½ ∠AOC), and ray OF bisect ∠BOC (so ∠COF = ½ ∠BOC). Then the angle between the bisectors is ∠EOF = ∠COE + ∠COF = ½ ∠AOC + ½ ∠BOC = ½(∠AOC + ∠BOC) = ½(180°) = 90°! Hence, OE ⊥ OF.",
        "key_points": [
            "Angle Bisector: A ray dividing an angle into two congruent angles.",
            "Linear pair angle bisectors are always perpendicular (enclose an angle of exactly 90°).",
            "Proof uses halving axiom (Axiom 7): ½(180°) = 90°.",
            "Crucial result in optical reflection: angle of incidence equals angle of reflection.",
            "Used in constructing perpendiculars without a protractor."
        ],
        "narration": "Here is an elegant theorem: take any linear pair of angles on a straight line. Now draw the bisector of each angle. The angle between these two bisector rays is ALWAYS exactly 90 degrees! Half of 180 degrees is always 90 degrees!",
        "sim_title": "Linear Pair Bisector Orthogonality Tool",
        "checkpoints": [
            {
                "q": "If the angle bisectors of two adjacent angles are perpendicular (90°), what must be the sum of the original two angles?",
                "options": ["90°", "180°", "270°", "360°"],
                "ans": 1,
                "exp": "Since ∠EOF = ½(sum) = 90°, the sum must be 2 × 90° = 180° (they form a linear pair)."
            },
            {
                "q": "Ray OE bisects ∠AOC (80°) and ray OF bisects adjacent angle ∠BOC (100°). What is ∠EOF?",
                "options": ["80°", "90°", "100°", "45°"],
                "ans": 1,
                "exp": "∠EOF = ½(80°) + ½(100°) = 40° + 50° = 90°."
            }
        ]
    },
    {
        "id": 9,
        "title": "Parallel Lines Cut by a Transversal: The 8-Angle System",
        "subtitle": "Transversal Definition, Interior/Exterior Classification & Angle Pairs",
        "category": "Parallel Lines",
        "badge": "CG-7 • C-7.1 • The 8-Angle System",
        "summary": "A straight line that intersects two or more coplanar lines at distinct points is called a Transversal (line t). When transversal t intersects two lines l and m, exactly 8 angles are formed (numbered 1 through 8). These 8 angles are systematically classified into: (1) Corresponding Angles (same relative corner: 1 & 5, 2 & 6, 4 & 8, 3 & 7); (2) Alternate Interior Angles (opposite sides between lines: 3 & 5, 4 & 6); (3) Alternate Exterior Angles (opposite sides outside lines: 1 & 7, 2 & 8); (4) Consecutive Interior / Co-interior Angles (same side between lines: 4 & 5, 3 & 6).",
        "key_points": [
            "Transversal: A line intersecting two or more coplanar lines at distinct points.",
            "8 angles are formed: 4 exterior angles (1, 2, 7, 8) and 4 interior angles (3, 4, 5, 6).",
            "Corresponding angles occupy identical relative positions at each intersection vertex.",
            "Alternate interior angles form the classic 'Z-shape' on opposite sides of the transversal.",
            "Co-interior angles form the 'C-shape' on the same interior side of the transversal."
        ],
        "narration": "When a transversal line cuts across two parallel lines, it creates an 8-angle system! Four angles are interior (between the lines), and four are exterior. Notice how they pair up: corresponding angles look in the same direction, alternate interior angles make a Z-shape, and co-interior angles make a C-shape!",
        "sim_title": "Transversal 8-Angle Color-Coded Inspector",
        "checkpoints": [
            {
                "q": "In a transversal intersecting two lines, which of the following represents an Alternate Interior angle pair?",
                "options": ["∠1 and ∠5", "∠3 and ∠5", "∠4 and ∠5", "∠2 and ∠8"],
                "ans": 1,
                "exp": "∠3 and ∠5 lie on opposite (alternate) sides of the transversal between the two lines (interior)."
            },
            {
                "q": "How many total angles are formed when a transversal intersects two lines in a plane?",
                "options": ["4 angles", "6 angles", "8 angles", "12 angles"],
                "ans": 2,
                "exp": "At each of the 2 intersection points, 4 angles are formed, giving 4 + 4 = 8 total angles."
            }
        ]
    },
    {
        "id": 10,
        "title": "Corresponding Angles Axiom & Its Converse (Axioms 6.3 & 6.4)",
        "subtitle": "The Foundational Assumption Linking Parallel Lines to Angle Congruence",
        "category": "Axioms",
        "badge": "CG-7 • C-7.1 • Corresponding Angles",
        "summary": "Axiom 6.3 (Corresponding Angles Axiom): 'If a transversal intersects two parallel lines, then each pair of corresponding angles is equal' (∠1 = ∠5, ∠2 = ∠6, ∠4 = ∠8, ∠3 = ∠7). Axiom 6.4 (Converse): 'If a transversal intersects two lines such that a pair of corresponding angles is equal, then the two lines are parallel to each other.' These axioms are accepted without proof and serve as the foundational bedrock to prove all subsequent theorems on alternate and interior angles.",
        "key_points": [
            "Axiom 6.3: Parallel lines cut by transversal ⇒ Corresponding angles are equal.",
            "Axiom 6.4 (Converse): Corresponding angles are equal ⇒ Lines are parallel.",
            "These two axioms establish an 'if and only if' bidirectional equivalence.",
            "Drafting T-squares and parallel rulers work directly by enforcing equal corresponding angles.",
            "Enables proving that alternate interior angles are equal (Theorem 6.2)."
        ],
        "narration": "Axiom 6.3 is the master key to parallel lines: if the lines are parallel, corresponding angles are identical! And the converse is equally powerful: if you can measure and prove that just ONE pair of corresponding angles is equal, the lines are guaranteed to be parallel!",
        "sim_title": "T-Square & Parallel Glide Simulator",
        "checkpoints": [
            {
                "q": "Line l is parallel to line m, and transversal t intersects them. If ∠1 = 72°, what is its corresponding angle ∠5?",
                "options": ["72°", "108°", "18°", "90°"],
                "ans": 0,
                "exp": "By Axiom 6.3 (Corresponding Angles Axiom), corresponding angles are equal, so ∠5 = ∠1 = 72°."
            },
            {
                "q": "A transversal cuts two lines such that a pair of corresponding angles both measure 85°. What can be concluded about the two lines?",
                "options": ["They are perpendicular", "They are parallel", "They will intersect", "They coincide"],
                "ans": 1,
                "exp": "By Axiom 6.4 (Converse of Corresponding Angles Axiom), equal corresponding angles prove the lines are parallel."
            }
        ]
    },
    {
        "id": 11,
        "title": "Alternate Interior Angles: Theorem & Converse (Theorems 6.2 & 6.3)",
        "subtitle": "The Iconic 'Z-Pattern' & Proof via Corresponding and Vertically Opposite Angles",
        "category": "Alternate Angles",
        "badge": "CG-7 • C-7.3 • Alternate Interior Angles",
        "summary": "Theorem 6.2: 'If a transversal intersects two parallel lines, then each pair of alternate interior angles is equal' (∠3 = ∠5 and ∠4 = ∠6). Proof: Let line AB ∥ CD and transversal t intersect them. By Axiom 6.3, corresponding angles are equal: ∠1 = ∠5. By Theorem 6.1, vertically opposite angles are equal: ∠1 = ∠3. By Euclid's Axiom 1 (things equal to the same thing are equal): ∠3 = ∠5! Theorem 6.3 (Converse): 'If a transversal intersects two lines such that a pair of alternate interior angles is equal, then the lines are parallel.'",
        "key_points": [
            "Theorem 6.2: Alternate interior angles are equal for parallel lines (Z-pattern: ∠3 = ∠5, ∠4 = ∠6).",
            "Proof combines Corresponding Angles Axiom (∠1 = ∠5) with Vertically Opposite Theorem (∠1 = ∠3).",
            "Theorem 6.3 (Converse): Equal alternate interior angles prove parallelism.",
            "Alternate exterior angles are also equal (∠1 = ∠7 and ∠2 = ∠8).",
            "Vital for engineering trusses, bridge beams, and conveyor belts."
        ],
        "narration": "Look for the letter Z! The alternate interior angles nestled inside the corners of the Z are always equal when the lines are parallel. And we can prove it easily: corresponding angles equal vertically opposite angles, so alternate interior angles must be equal!",
        "sim_title": "The 'Z-Pattern' Alternate Interior Angle Prover",
        "checkpoints": [
            {
                "q": "Lines AB and CD are parallel. Transversal t intersects them. If ∠4 = 115°, what is alternate interior angle ∠6?",
                "options": ["65°", "115°", "90°", "125°"],
                "ans": 1,
                "exp": "By Theorem 6.2, alternate interior angles are equal, so ∠6 = ∠4 = 115°."
            },
            {
                "q": "Which two geometric principles are combined to prove Theorem 6.2 (Alternate interior angles are equal)?",
                "options": [
                    "Corresponding Angles Axiom and Vertically Opposite Angles Theorem",
                    "Pythagorean Theorem and Midpoint Formula",
                    "Linear Pair Axiom and Exterior Angle Theorem",
                    "Playfair's Axiom and Thales' Theorem"
                ],
                "ans": 0,
                "exp": "Proof: ∠1 = ∠5 (Corresponding) and ∠1 = ∠3 (Vertically opposite) ⇒ ∠3 = ∠5 by transitivity."
            }
        ]
    },
    {
        "id": 12,
        "title": "Consecutive Interior Angles (Co-interior): Theorems 6.4 & 6.5",
        "subtitle": "The 'C-Pattern' Supplementary Criterion & Proof via Linear Pairs",
        "category": "Co-Interior Angles",
        "badge": "CG-7 • C-7.3 • Co-Interior Angles",
        "summary": "Theorem 6.4: 'If a transversal intersects two parallel lines, then each pair of consecutive interior angles on the same side of the transversal is supplementary' (∠4 + ∠5 = 180° and ∠3 + ∠6 = 180°). Proof: On line AB, ray t forms linear pair: ∠3 + ∠4 = 180°. But AB ∥ CD ⇒ alternate interior angles are equal: ∠3 = ∠5. Substituting ∠5 for ∠3 gives: ∠4 + ∠5 = 180°! Theorem 6.5 (Converse): 'If a transversal intersects two lines such that consecutive interior angles sum to 180°, then the lines are parallel.'",
        "key_points": [
            "Theorem 6.4: Consecutive interior (co-interior) angles sum to 180° (C-pattern: ∠4 + ∠5 = 180°).",
            "Proof substitutes alternate interior angles into a linear pair.",
            "Theorem 6.5 (Converse): If consecutive interior angles sum to 180°, lines are parallel.",
            "Direct link to Euclid's Fifth Postulate: Parallel lines occur when the interior angle sum is exactly 180°.",
            "Crucial for trapezoid and parallelogram angle calculations."
        ],
        "narration": "Inside the parallel lines on the same side of the transversal, we have co-interior angles forming a C-shape. These two angles are supplementary—they always add up to 180 degrees! If one angle is 120 degrees, the other must be 60 degrees.",
        "sim_title": "The 'C-Pattern' Co-Interior Sum Gauge",
        "checkpoints": [
            {
                "q": "Lines l ∥ m are cut by transversal t. If co-interior angle ∠4 = 130°, what is ∠5?",
                "options": ["50°", "130°", "60°", "140°"],
                "ans": 0,
                "exp": "Co-interior angles sum to 180° (Theorem 6.4): ∠5 = 180° - 130° = 50°."
            },
            {
                "q": "Transversal t cuts lines p and q. Interior angles on the same side are 2x° and 3x°. If p ∥ q, find x.",
                "options": ["36", "30", "45", "60"],
                "ans": 0,
                "exp": "2x + 3x = 180 ⇒ 5x = 180 ⇒ x = 36."
            }
        ]
    },
    {
        "id": 13,
        "title": "Transitivity of Parallelism (Theorem 6.6)",
        "subtitle": "Lines Parallel to the Same Line are Parallel to Each Other",
        "category": "Parallel Transitivity",
        "badge": "CG-7 • C-7.1 • Transitivity Theorem",
        "summary": "Theorem 6.6: 'Lines which are parallel to the same line are parallel to each other.' That is, if line l ∥ line m and line m ∥ line n, then line l ∥ line n. Proof: Draw a transversal line t cutting all three lines l, m, and n. Let corresponding angles formed be ∠1, ∠2, and ∠3 respectively. Since l ∥ m, ∠1 = ∠2 (Axiom 6.3). Since m ∥ n, ∠2 = ∠3 (Axiom 6.3). By Euclid's Axiom 1 (things equal to the same thing are equal), ∠1 = ∠3. Since corresponding angles ∠1 and ∠3 are equal, by Axiom 6.4, line l ∥ line n! This property extends to any number of parallel lines.",
        "key_points": [
            "Theorem 6.6 (Transitivity): l ∥ m and m ∥ n ⇒ l ∥ n.",
            "Proof uses corresponding angles and Euclid's Axiom 1 (transitivity of equality).",
            "Explains why ruled lined paper, railroad tracks, and Venetian blinds maintain uniform parallel spacing.",
            "Works for 3D planes as well as 2D lines.",
            "Fundamental theorem in Euclidean geometry."
        ],
        "narration": "Parallelism is transitive! If line l is parallel to m, and m is parallel to n, then l is automatically parallel to n. Think of railway tracks or lined notebook paper: every single line stays parallel to all the others across the entire page!",
        "sim_title": "Venetian Blinds & Multi-Line Parallelism Rail",
        "checkpoints": [
            {
                "q": "If line a ∥ line b, and line b ∥ line c, what is the geometric relationship between line a and line c?",
                "options": ["Line a ⊥ line c", "Line a ∥ line c", "Line a intersects line c", "Cannot be determined"],
                "ans": 1,
                "exp": "By Theorem 6.6, lines parallel to the same line are parallel to each other, so line a ∥ line c."
            },
            {
                "q": "Which Euclid's axiom is directly utilized in the proof of Theorem 6.6?",
                "options": [
                    "Axiom 1: Things equal to the same thing are equal to one another",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 2: If equals are added to equals, wholes are equal",
                    "Axiom 4: Things coinciding are equal"
                ],
                "ans": 0,
                "exp": "Since ∠1 = ∠2 and ∠2 = ∠3, by Axiom 1 (transitivity of equality), ∠1 = ∠3."
            }
        ]
    },
    {
        "id": 14,
        "title": "Angle Sum Property of a Triangle (Theorem 6.7)",
        "subtitle": "Proof via Auxiliary Parallel Line: Sum of Interior Angles Equals 180°",
        "category": "Triangle Angle Sum",
        "badge": "CG-7 • C-7.3 • Triangle Sum Proof",
        "summary": "Theorem 6.7: 'The sum of the angles of a triangle is 180°' (∠A + ∠B + ∠C = 180°). Master Proof: Consider triangle ABC. Through vertex A, construct an auxiliary line XAY parallel to base BC. Since XAY is a straight line, the angles on it sum to 180°: ∠XAB + ∠BAC + ∠YAC = 180°. But line XAY ∥ BC and AB, AC are transversals: ∠XAB = ∠B (alternate interior angles) and ∠YAC = ∠C (alternate interior angles). Substituting gives: ∠B + ∠A + ∠C = 180°! Hence, ∠A + ∠B + ∠C = 180°.",
        "key_points": [
            "Theorem 6.7: The sum of the three interior angles of any triangle is always 180°.",
            "Proof relies on constructing an auxiliary line through one vertex parallel to the opposite base.",
            "Connects straight line linear pair (180°) with triangle interior angles via alternate interior angles.",
            "True for ALL triangles: acute, right, obtuse, equilateral, isosceles, and scalene.",
            "Fundamental constraint of flat 2D Euclidean geometry."
        ],
        "narration": "Why do the three angles of a triangle always add up to 180 degrees? Here is Euclid's genius proof: draw a line through the top vertex parallel to the bottom base! The straight line makes 180 degrees, and the two alternate interior angles fold right into the triangle's corners!",
        "sim_title": "Triangle Angle Sum Unfolder & Parallel Auxiliary Line Prover",
        "checkpoints": [
            {
                "q": "In triangle ABC, ∠A = 55° and ∠B = 65°. What is the measure of ∠C?",
                "options": ["60°", "70°", "50°", "80°"],
                "ans": 0,
                "exp": "∠C = 180° - (55° + 65°) = 180° - 120° = 60°."
            },
            {
                "q": "In the proof of the Triangle Angle Sum theorem, what auxiliary construction is made?",
                "options": [
                    "A circle inscribed in the triangle",
                    "A line through one vertex parallel to the opposite side",
                    "A perpendicular bisector of the base",
                    "An altitude from the vertex"
                ],
                "ans": 1,
                "exp": "The proof requires drawing a line through a vertex parallel to the opposite side."
            }
        ]
    },
    {
        "id": 15,
        "title": "Exterior Angle Theorem & Triangle Angle Constraints",
        "subtitle": "Proof by Contradiction: Why Triangles Must Have at Least Two Acute Angles",
        "category": "Angle Constraints",
        "badge": "CG-7 • CG-9 • Proof by Contradiction",
        "summary": "Theorem 6.8 (Exterior Angle Theorem): 'If a side of a triangle is produced, the exterior angle so formed is equal to the sum of the two interior opposite angles' (Exterior ∠ACD = ∠A + ∠B). From this and Theorem 6.7, we deduce vital triangle angle constraints using Proof by Contradiction: (1) A triangle MUST have at least two acute angles! If it had fewer than two acute angles, it would have two or more angles ≥ 90°, so their sum would exceed 180°, contradicting Theorem 6.7! (2) A triangle CANNOT have two right angles or two obtuse angles; (3) A triangle CANNOT have all three angles strictly less than 60° (if all < 60°, sum < 180°, impossible!).",
        "key_points": [
            "Exterior Angle Theorem: Exterior angle = sum of two interior opposite angles (∠ACD = ∠A + ∠B).",
            "An exterior angle of a triangle is strictly greater than either of its interior opposite angles.",
            "Every triangle must have AT LEAST two acute angles (proof by contradiction).",
            "A triangle can have AT MOST one right angle or at most one obtuse angle.",
            "A triangle cannot have all three angles < 60° (sum would be < 180°); in an equilateral triangle, all three are exactly 60°."
        ],
        "narration": "The Exterior Angle Theorem states that any outside angle equals the sum of the two opposite inside angles! From this, we discover strict rules through proof by contradiction: a triangle MUST have at least two acute angles. It can never have two obtuse angles, and it can never have all three angles less than 60 degrees!",
        "sim_title": "Triangle Angle Constraints & Contradiction Tester",
        "checkpoints": [
            {
                "q": "An exterior angle of a triangle is 110°, and one of its interior opposite angles is 45°. What is the other interior opposite angle?",
                "options": ["65°", "75°", "55°", "70°"],
                "ans": 0,
                "exp": "By Exterior Angle Theorem: Exterior = ∠1 + ∠2 ⇒ 110° = 45° + ∠2 ⇒ ∠2 = 110° - 45° = 65°."
            },
            {
                "q": "Can a triangle have all three interior angles measuring less than 60°?",
                "options": [
                    "Yes, in an acute triangle",
                    "No, because their sum would be strictly less than 180° (contradiction)",
                    "Yes, in a scalene triangle",
                    "Only if the sides are very small"
                ],
                "ans": 1,
                "exp": "If all three angles are < 60°, their sum would be < 180°, violating the Angle Sum Theorem (Proof by Contradiction)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Step-by-Step Geometric Inference Engine",
        "subtitle": "Algorithmic Geometry, Rule-Based Production Systems & Automated Angle Deduction",
        "category": "Computational Thinking",
        "badge": "CG-9 • Computational Geometry",
        "summary": "Computational thinking applies computer science paradigms to geometry by representing geometric axioms and theorems as production rules in an automated expert inference engine: Rule 1: linear_pair(a, b) ⇒ b = 180 - a; Rule 2: vert_opposite(a, b) ⇒ b = a; Rule 3: parallel(l, m) & alt_interior(a, b) ⇒ b = a; Rule 4: triangle(a, b, c) ⇒ c = 180 - (a + b). By applying forward-chaining deduction, a computer can systematically solve for all unknown angles in complex CAD blueprints and robotic linkages step by step.",
        "key_points": [
            "Geometric Production Rules: Encoding axioms and theorems as executable software rules.",
            "Forward-chaining inference: Repeatedly applying known angle rules until all unknowns are resolved.",
            "Proof trees: Representing geometric proofs as directed acyclic graphs (DAGs) of logical justifications.",
            "Powers modern CAD engineering software (AutoCAD, SolidWorks) and computer graphics ray tracing.",
            "Verification of geometric consistency and automated theorem proving in Artificial Intelligence."
        ],
        "narration": "How do computers solve geometry? They use computational thinking! Every theorem we learned—linear pair, vertically opposite, alternate interior, triangle sum—becomes an if-then rule. By chaining these rules together, a computer algorithm can solve dozens of unknown angles in a fraction of a millisecond!",
        "sim_title": "Geometric Rule-Based Forward Chaining Engine",
        "checkpoints": [
            {
                "q": "In computational geometry, representing theorems as 'IF premise THEN conclusion' rules is called a:",
                "options": [
                    "Production Rule Inference Engine",
                    "Sorting Algorithm",
                    "Hashing Function",
                    "Binary Tree Search"
                ],
                "ans": 0,
                "exp": "Production rule inference engines apply IF-THEN rules to deduce new facts step by step."
            },
            {
                "q": "Given ∠1 = 40° in a complex figure with parallel lines, what is the computational time complexity to determine its alternate interior angle?",
                "options": ["O(1) Constant Time", "O(n) Linear Time", "O(n²)", "O(log n)"],
                "ans": 0,
                "exp": "Applying a direct equality rule (alternate interior angles are equal) requires a single O(1) assignment operation."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 17,
        "title": "Mastery Challenge Part 1: Rays, Angles & Pairs",
        "subtitle": "10 Questions on Rays, Angle Classifications, Complementary & Supplementary Angles",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 1 • Foundations & Pairs",
        "questions": [
            {
                "id": 1,
                "q": "How many endpoints does a geometric ray possess?",
                "options": ["Zero", "One", "Two", "Infinitely many"],
                "ans": 1,
                "solution": "A ray has exactly one fixed starting point (endpoint) and extends infinitely in the other direction."
            },
            {
                "id": 2,
                "q": "An angle measuring 240° is classified as which type of angle?",
                "options": ["Obtuse angle", "Straight angle", "Reflex angle", "Complete angle"],
                "ans": 2,
                "solution": "Since 180° < 240° < 360°, it is a Reflex angle."
            },
            {
                "id": 3,
                "q": "If two angles are complementary, and one is 20° larger than the other, what is the measure of the smaller angle?",
                "options": ["35°", "55°", "45°", "25°"],
                "ans": 0,
                "solution": "Let smaller angle be x. x + (x + 20°) = 90° ⇒ 2x + 20° = 90° ⇒ 2x = 70° ⇒ x = 35°."
            },
            {
                "id": 4,
                "q": "Find the measure of an angle whose supplement is four times its complement.",
                "options": ["60°", "45°", "30°", "75°"],
                "ans": 0,
                "solution": "Let angle be x. Supplement = 180° - x; Complement = 90° - x. Equation: 180 - x = 4(90 - x) ⇒ 180 - x = 360 - 4x ⇒ 3x = 180 ⇒ x = 60°."
            },
            {
                "id": 5,
                "q": "Two supplementary angles are in the ratio 4 : 5. What is the measure of the larger angle?",
                "options": ["80°", "100°", "90°", "120°"],
                "ans": 1,
                "solution": "4x + 5x = 180° ⇒ 9x = 180° ⇒ x = 20°. Larger angle = 5(20°) = 100°."
            },
            {
                "id": 6,
                "q": "What is the measure of the reflex angle corresponding to an interior angle of 70°?",
                "options": ["110°", "290°", "200°", "180°"],
                "ans": 1,
                "solution": "Reflex angle = 360° - 70° = 290°."
            },
            {
                "id": 7,
                "q": "Can two obtuse angles be supplementary?",
                "options": [
                    "Yes, always",
                    "No, because both are > 90°, so their sum is strictly > 180°",
                    "Only if they are equal",
                    "Only in a triangle"
                ],
                "ans": 1,
                "solution": "Since an obtuse angle is > 90°, the sum of two obtuse angles is > 180°, so they can never be supplementary."
            },
            {
                "id": 8,
                "q": "If the arms of an angle form two opposite rays lying along a straight line, what is the measure of the angle?",
                "options": ["90°", "180°", "360°", "0°"],
                "ans": 1,
                "solution": "Two opposite rays form a straight line, which measures exactly 180° (a straight angle)."
            },
            {
                "id": 9,
                "q": "At 3:00 o'clock, what is the angle between the hour hand and the minute hand of a clock?",
                "options": ["60°", "90°", "120°", "45°"],
                "ans": 1,
                "solution": "At 3:00, the hands are 3 hours apart. Each hour is 360° / 12 = 30°, so 3 × 30° = 90° (a right angle)."
            },
            {
                "id": 10,
                "q": "What is the complement of a right angle (90°)?",
                "options": ["0°", "90°", "180°", "45°"],
                "ans": 0,
                "solution": "Complement = 90° - 90° = 0°."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge Part 2: Linear Pairs & Intersecting Lines",
        "subtitle": "10 Questions on Linear Pair Axioms, Vertically Opposite Angles & Bisectors",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 2 • Linear Pairs & Intersecting Lines",
        "questions": [
            {
                "id": 11,
                "q": "In a linear pair of angles, if one angle is acute, the other angle must be:",
                "options": ["Acute", "Right", "Obtuse", "Reflex"],
                "ans": 2,
                "solution": "Since linear pair angles sum to 180°, if one is < 90° (acute), the other must be > 90° (obtuse)."
            },
            {
                "id": 12,
                "q": "Two lines AB and CD intersect at O. If ∠AOC + ∠BOD = 140°, what is the measure of ∠AOC?",
                "options": ["70°", "140°", "110°", "40°"],
                "ans": 0,
                "solution": "∠AOC and ∠BOD are vertically opposite angles, so ∠AOC = ∠BOD. Thus, 2∠AOC = 140° ⇒ ∠AOC = 70°."
            },
            {
                "id": 13,
                "q": "Ray OC stands on line AB. If ∠AOC = 4x and ∠BOC = 5x, what is the measure of ∠AOC?",
                "options": ["80°", "100°", "20°", "40°"],
                "ans": 0,
                "solution": "4x + 5x = 180° ⇒ 9x = 180° ⇒ x = 20°. Thus, ∠AOC = 4(20°) = 80°."
            },
            {
                "id": 14,
                "q": "Two adjacent angles on a line are in the ratio 2 : 3. What is the measure of the smaller angle?",
                "options": ["72°", "108°", "36°", "54°"],
                "ans": 0,
                "solution": "2x + 3x = 180° ⇒ 5x = 180° ⇒ x = 36°. Smaller angle = 2(36°) = 72°."
            },
            {
                "id": 15,
                "q": "What is the angle between the bisectors of two vertically opposite angles?",
                "options": ["90°", "180° (they form a straight line)", "45°", "60°"],
                "ans": 1,
                "solution": "The bisectors of two vertically opposite angles lie along the exact same straight line, so the angle between them is 180°."
            },
            {
                "id": 16,
                "q": "Five rays OA, OB, OC, OD, and OE form consecutive angles x°, (x+10)°, (x+20)°, (x+30)°, and (x+40)° around point O. What is x?",
                "options": ["52", "60", "48", "72"],
                "ans": 0,
                "solution": "Sum around point = 360° ⇒ 5x + 100 = 360 ⇒ 5x = 260 ⇒ x = 52."
            },
            {
                "id": 17,
                "q": "Lines AB and CD intersect at O. If ∠AOC : ∠AOD = 5 : 7, what is the measure of ∠BOD?",
                "options": ["75°", "105°", "85°", "95°"],
                "ans": 0,
                "solution": "∠AOC + ∠AOD = 180° (linear pair) ⇒ 5x + 7x = 180° ⇒ 12x = 180° ⇒ x = 15°. Thus, ∠AOC = 5(15°) = 75°. Since ∠BOD is vertically opposite to ∠AOC, ∠BOD = 75°."
            },
            {
                "id": 18,
                "q": "If the angle bisectors of two adjacent angles form an angle of 90°, what must be true about the two adjacent angles?",
                "options": [
                    "They form a linear pair (sum = 180°)",
                    "They are complementary (sum = 90°)",
                    "They are equal",
                    "They are both obtuse"
                ],
                "ans": 0,
                "solution": "Angle between bisectors = ½(sum) = 90° ⇒ sum = 180°, meaning the non-common arms form a straight line (linear pair)."
            },
            {
                "id": 19,
                "q": "Three coplanar lines intersect at a single common point O. How many pairs of vertically opposite angles are formed?",
                "options": ["3 pairs", "6 pairs", "4 pairs", "2 pairs"],
                "ans": 1,
                "solution": "Each pair of lines produces 2 pairs of vertically opposite angles. With 3 lines, there are 3 choose 2 = 3 pairs of lines, yielding 3 × 2 = 6 pairs of vertically opposite angles."
            },
            {
                "id": 20,
                "q": "If an angle is 30° less than twice its supplement, what is the angle?",
                "options": ["110°", "70°", "120°", "60°"],
                "ans": 0,
                "solution": "Let angle be x. Supplement = 180 - x. Equation: x = 2(180 - x) - 30 ⇒ x = 360 - 2x - 30 ⇒ 3x = 330 ⇒ x = 110°."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge Part 3: Parallel Lines & Transversals",
        "subtitle": "10 Questions on Corresponding, Alternate Interior, and Co-Interior Angle Theorems",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 3 • Parallel Lines",
        "questions": [
            {
                "id": 21,
                "q": "Lines AB ∥ CD are cut by transversal t. If one interior angle is 68°, what is its alternate interior angle?",
                "options": ["68°", "112°", "22°", "90°"],
                "ans": 0,
                "solution": "By Theorem 6.2, alternate interior angles are equal, so the alternate interior angle is 68°."
            },
            {
                "id": 22,
                "q": "Lines l ∥ m are cut by transversal t. If consecutive interior angles on the same side are (3x - 10)° and (2x + 20)°, find x.",
                "options": ["34", "30", "36", "40"],
                "ans": 0,
                "solution": "Consecutive interior angles are supplementary (Theorem 6.4): (3x - 10) + (2x + 20) = 180 ⇒ 5x + 10 = 180 ⇒ 5x = 170 ⇒ x = 34."
            },
            {
                "id": 23,
                "q": "If a transversal intersects two parallel lines, how are the bisectors of any pair of alternate interior angles related?",
                "options": ["They are parallel to each other", "They are perpendicular to each other", "They intersect at 45°", "They coincide"],
                "ans": 0,
                "solution": "The bisectors of a pair of alternate interior angles are parallel to each other (because they form equal alternate interior angles of measure θ/2)."
            },
            {
                "id": 24,
                "q": "If a transversal intersects two parallel lines, what geometric figure is formed by the bisectors of the four interior angles?",
                "options": ["A Rectangle", "A Rhombus", "A Trapezium", "A Kite"],
                "ans": 0,
                "solution": "The bisectors form a parallelogram whose interior angles are all 90° (since linear pair bisectors are perpendicular), which defines a Rectangle."
            },
            {
                "id": 25,
                "q": "In a figure, AB ∥ CD and CD ∥ EF. If ∠ABC = 70° and ∠CEF = 130°, what is the reflex angle ∠BCE?",
                "options": ["240°", "120°", "300°", "260°"],
                "ans": 0,
                "solution": "Draw auxiliary parallel through C: ∠BCC' = 70° (alternate to ∠ABC). Co-interior angle with EF: 180° - 130° = 50°. Interior ∠BCE = 70° + 50° = 120°. Reflex ∠BCE = 360° - 120° = 240°."
            },
            {
                "id": 26,
                "q": "If two lines are both perpendicular to the same line, what is their relationship to each other?",
                "options": ["They are parallel to each other", "They are perpendicular to each other", "They intersect at 45°", "They coincide"],
                "ans": 0,
                "solution": "If two coplanar lines are both perpendicular to a transversal line, their corresponding angles are both 90°, proving the two lines are parallel."
            },
            {
                "id": 27,
                "q": "Lines AB ∥ CD. A transversal intersects them at P and Q. If the ratio of two interior angles on the same side is 2 : 7, what is the larger angle?",
                "options": ["140°", "120°", "135°", "150°"],
                "ans": 0,
                "solution": "2x + 7x = 180° ⇒ 9x = 180° ⇒ x = 20°. Larger angle = 7(20°) = 140°."
            },
            {
                "id": 28,
                "q": "Which theorem states that 'Lines which are parallel to the same line are parallel to each other'?",
                "options": ["Theorem 6.6 (Transitivity of Parallelism)", "Theorem 6.1", "Theorem 6.4", "Linear Pair Axiom"],
                "ans": 0,
                "solution": "Theorem 6.6 establishes the transitivity of parallelism (l ∥ m and m ∥ n ⇒ l ∥ n)."
            },
            {
                "id": 29,
                "q": "If a transversal cuts two lines such that alternate interior angles are (5x - 20)° and (3x + 10)°, for what value of x are the lines parallel?",
                "options": ["15", "20", "10", "25"],
                "ans": 0,
                "solution": "For lines to be parallel, alternate interior angles must be equal: 5x - 20 = 3x + 10 ⇒ 2x = 30 ⇒ x = 15."
            },
            {
                "id": 30,
                "q": "What is the maximum number of acute angles formed when a transversal intersects two parallel lines?",
                "options": ["4", "2", "6", "8"],
                "ans": 0,
                "solution": "Unless the transversal is perpendicular (where all 8 are 90°), exactly 4 angles are equal acute angles and 4 are equal obtuse angles."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Part 4: Triangles, Exterior Angles & Contradictions",
        "subtitle": "10 Questions on Triangle Angle Sum, Exterior Angles & Indirect Proofs",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 4 • Advanced Geometric Deductions",
        "questions": [
            {
                "id": 31,
                "q": "The angles of a triangle are in the ratio 2 : 3 : 4. What is the measure of the largest angle?",
                "options": ["80°", "60°", "90°", "100°"],
                "ans": 0,
                "solution": "2x + 3x + 4x = 180° ⇒ 9x = 180° ⇒ x = 20°. Largest angle = 4(20°) = 80°."
            },
            {
                "id": 32,
                "q": "In triangle ABC, the bisectors of ∠B and ∠C intersect at point O. What is the formula for ∠BOC?",
                "options": ["90° + ½ ∠A", "90° - ½ ∠A", "180° - ∠A", "2 ∠A"],
                "ans": 0,
                "solution": "In triangle OBC: ∠BOC = 180° - ½(∠B + ∠C) = 180° - ½(180° - ∠A) = 180° - 90° + ½ ∠A = 90° + ½ ∠A."
            },
            {
                "id": 33,
                "q": "An exterior angle of a triangle is 105°, and its two interior opposite angles are equal. What is the measure of each of these equal angles?",
                "options": ["52.5°", "75°", "65°", "45°"],
                "ans": 0,
                "solution": "By Exterior Angle Theorem: x + x = 105° ⇒ 2x = 105° ⇒ x = 52.5°."
            },
            {
                "id": 34,
                "q": "Why can a triangle NOT have two right angles? (Proof by Contradiction)",
                "options": [
                    "Because 90° + 90° = 180°, leaving 0° for the third angle (violating angle sum theorem)",
                    "Because triangles can only have acute angles",
                    "Because right angles cannot touch",
                    "Because right triangles have only 2 sides"
                ],
                "ans": 0,
                "solution": "If two angles were 90°, their sum is 180°, forcing the third angle to be 0°, which is impossible for a non-degenerate triangle."
            },
            {
                "id": 35,
                "q": "The side BC of triangle ABC is produced to D. If ∠ACD = 120° and ∠B = ½ ∠A, find ∠A.",
                "options": ["80°", "40°", "60°", "90°"],
                "ans": 0,
                "solution": "∠A + ∠B = 120° ⇒ ∠A + ½ ∠A = 120° ⇒ 1.5 ∠A = 120° ⇒ ∠A = 80° (and ∠B = 40°)."
            },
            {
                "id": 36,
                "q": "What is the sum of the three exterior angles of any triangle (one at each vertex)?",
                "options": ["360°", "180°", "540°", "270°"],
                "ans": 0,
                "solution": "Each exterior angle is 180° - interior angle. Total sum = 3(180°) - (sum of interior angles) = 540° - 180° = 360°."
            },
            {
                "id": 37,
                "q": "In a right-angled triangle, what is the sum of the two acute angles?",
                "options": ["90° (they are complementary)", "180°", "45°", "120°"],
                "ans": 0,
                "solution": "Since the right angle is 90°, the other two angles must sum to 180° - 90° = 90° (complementary)."
            },
            {
                "id": 38,
                "q": "In triangle PQR, if ∠P - ∠Q = 42° and ∠Q - ∠R = 21°, find ∠Q.",
                "options": ["53°", "95°", "32°", "60°"],
                "ans": 0,
                "solution": "∠P = ∠Q + 42° and ∠R = ∠Q - 21°. Sum = 180° ⇒ (∠Q + 42) + ∠Q + (∠Q - 21) = 180 ⇒ 3∠Q + 21 = 180 ⇒ 3∠Q = 159 ⇒ ∠Q = 53°."
            },
            {
                "id": 39,
                "q": "Why must every triangle have at least two acute angles?",
                "options": [
                    "If a triangle had 2 or more non-acute angles (≥ 90°), their sum would be ≥ 180°, leaving nothing for the third angle",
                    "Because all polygons have acute angles",
                    "Because acute angles are smaller",
                    "It is an unproven assumption"
                ],
                "ans": 0,
                "exp": "Proof by contradiction: If a triangle had fewer than two acute angles, at least two angles would be ≥ 90°, making their sum ≥ 180°, which violates the Triangle Angle Sum Theorem.",
                "solution": "Proof by contradiction: If a triangle had fewer than two acute angles, at least two angles would be ≥ 90°, making their sum ≥ 180°, which violates the Triangle Angle Sum Theorem."
            },
            {
                "id": 40,
                "q": "In computational geometry, what graph data structure best represents a deductive geometric proof where theorems depend on earlier theorems?",
                "options": [
                    "Directed Acyclic Graph (DAG)",
                    "Circular Linked List",
                    "Stack",
                    "Hash Map"
                ],
                "ans": 0,
                "solution": "A Directed Acyclic Graph (DAG) perfectly models deductive proofs, where premises flow towards conclusions without circular dependencies."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Total Content Slides: {len(SLIDES)}")
    total_cp = sum(len(s["checkpoints"]) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    print(f"Total Quiz Slides: {len(QUIZZES)}")
    total_qz = sum(len(q["questions"]) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, "Must have exactly 16 content slides"
    assert total_cp == 32, "Must have exactly 32 checkpoints"
    assert len(QUIZZES) == 4, "Must have exactly 4 quiz slides"
    assert total_qz == 40, "Must have exactly 40 quiz questions"

    for i, s in enumerate(SLIDES):
        assert len(s["checkpoints"]) == 2, f"Slide {i+1} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert "q" in cp and "options" in cp and "ans" in cp and "exp" in cp
            assert 0 <= cp["ans"] < len(cp["options"])

    for q_slide in QUIZZES:
        assert len(q_slide["questions"]) == 10, f"Quiz slide {q_slide['id']} must have 10 questions"
        for q in q_slide["questions"]:
            assert "q" in q and "options" in q and "ans" in q and "solution" in q
            assert 0 <= q["ans"] < len(q["options"])

    print("All Lines and Angles validations PASSED cleanly!")


# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 5: Parallel and Intersecting Lines Data
Author: Antigravity
Avatar: Acharya Baudhayana (Master of Sulba Sutra Geometry & Cord-Constructions)
"""

SLIDES_DATA = [
    # Slide 1: Across the Line - Intersecting Lines
    {
        "id": 1,
        "section": "5.1",
        "tag": "Section 5.1 • Across the Line: Intersecting Lines",
        "title": "Lines on a Plane & The Point of Intersection",
        "key_terms": ["Intersecting Lines", "Point of Intersection", "Plane Surface", "Vertically Opposite Angles"],
        "sim_id": "intersecting_lines_scissors_sim",
        "sim_title": "Interactive Scissor Lines & Angular Relationships",
        "narration": "Namaste, young geometers! I am Acharya Baudhayana. When two straight lines lie on the same flat plane, they either cross each other or never meet. When two straight lines meet at exactly one common point, we call them intersecting lines! Observe how two crossed lines create four distinct angles around their meeting point.",
        "theory": [
            "A **plane** is a flat two-dimensional surface that extends infinitely in all directions without thickness. When two distinct straight lines lie in the same plane, they can share at most **one single point**.",
            "If lines $l$ and $m$ meet at point $O$, they are called **intersecting lines**, and point $O$ is called their **point of intersection**.",
            "Intersecting lines act like an open pair of scissors: as one angle widens, its opposite angle widens by the exact same amount! Angles that face directly opposite each other across the intersection point are called **vertically opposite angles**.",
            "**Fundamental Theorem**: When two straight lines intersect, the **vertically opposite angles are always equal to each other**."
        ],
        "fact_box": "In ancient India, the Sulba Sutras used crossed cords (*rajju*) tied to central pegs (*sanku*) to align sacred fire altars with true cardinal directions.",
        "checkpoints": [
            {
                "id": "c1_1",
                "question": "What is the maximum number of points at which two distinct straight lines on a flat plane can intersect?",
                "options": ["Zero points", "Exactly one point", "Two points", "Infinitely many points"],
                "correct": 1,
                "explanation": "Two distinct straight lines can cross at no more than exactly one single point of intersection."
            },
            {
                "id": "c1_2",
                "question": "If two straight lines intersect and one of the angles formed is 65°, what is the measure of its vertically opposite angle?",
                "options": ["25°", "65°", "115°", "180°"],
                "correct": 1,
                "explanation": "Vertically opposite angles are always equal in measure. Therefore, the opposite angle is also exactly 65°."
            }
        ]
    },

    # Slide 2: Linear Pairs and Supplementary Adjacent Angles
    {
        "id": 2,
        "section": "5.1",
        "tag": "Section 5.1 • Angular Relationships: Linear Pairs",
        "title": "Adjacent Angles on a Line: The 180° Linear Pair",
        "key_terms": ["Adjacent Angles", "Common Arm", "Linear Pair", "Supplementary Angles"],
        "sim_id": "linear_pair_slider_sim",
        "sim_title": "Dynamic Linear Pair Balance & Straight Angle Split",
        "narration": "When two angles share a common vertex and a common side, while lying on opposite sides of that arm, they are adjacent. If their outer, non-common sides form a straight line, they form a linear pair! Notice that because a straight line measures 180 degrees, the two angles of any linear pair always sum to 180 degrees.",
        "theory": [
            "**Adjacent Angles** share a common vertex, a common ray (arm), and have no overlapping interior points.",
            "When two adjacent angles sit on a straight line, their non-common arms point in opposite directions along that line. Such an angle pair is called a **Linear Pair**.",
            "**Linear Pair Axiom**: The sum of two angles forming a linear pair is always equal to two right angles, or **180°** ($\angle 1 + \angle 2 = 180°$).",
            "**Proof that Vertically Opposite Angles are Equal**: Let lines $AB$ and $CD$ cross at $O$. Then $\angle AOC + \angle AOD = 180°$ (linear pair on $CD$), and $\angle AOD + \angle BOD = 180°$ (linear pair on $AB$). Equating both sums: $\angle AOC + \angle AOD = \angle AOD + \angle BOD \implies \angle AOC = \angle BOD$!"
        ],
        "fact_box": "The word 'linear' comes from the Latin word for line (*linea*). A linear pair is literally a pair of angles that together build a straight line.",
        "checkpoints": [
            {
                "id": "c2_1",
                "question": "Two angles form a linear pair. If one angle measures 128°, what is the measure of the adjacent angle?",
                "options": ["52°", "62°", "128°", "180°"],
                "correct": 0,
                "explanation": "Angles of a linear pair are supplementary: 180° - 128° = 52°."
            },
            {
                "id": "c2_2",
                "question": "Can two obtuse angles ever form a linear pair?",
                "options": ["Yes, always", "Yes, if they are equal", "No, never", "Only if both lines are curved"],
                "correct": 2,
                "explanation": "An obtuse angle is greater than 90°. The sum of two obtuse angles would strictly exceed 180°, so they can never form a linear pair."
            }
        ]
    },

    # Slide 3: Perpendicular Lines
    {
        "id": 3,
        "section": "5.2",
        "tag": "Section 5.2 • Perpendicular Lines",
        "title": "Perpendicular Lines: The Universal 90° Right Angle Cross",
        "key_terms": ["Perpendicular Lines", "Right Angle", "Symbol ⊥", "Equiangular Intersection"],
        "sim_id": "perpendicular_lines_cross_sim",
        "sim_title": "Interactive 90° Cross & Perpendicularity Detector",
        "narration": "What happens when intersecting lines divide the circle into four perfectly identical parts? Each of the four angles becomes exactly 90 degrees! When two lines meet at right angles, we call them perpendicular lines, represented by the symbol upside-down T.",
        "theory": [
            "**Perpendicular Lines**: When two intersecting lines form equal adjacent angles, each of the four angles measures exactly **90°** ($360° \div 4 = 90°$).",
            "Such lines are said to be **perpendicular** to each other. If line $AB$ is perpendicular to line $CD$, we write: $$AB \perp CD$$",
            "In geometric sketches, perpendicularity is marked with a small square corner symbol ($\llcorner$) at the vertex of intersection.",
            "Real-world examples of perpendicular lines include adjacent edges of a sheet of paper, the crosshairs of a surveyor's level, window frames, and the upright goalposts meeting the crossbar."
        ],
        "fact_box": "In the Baudhayana Sulba Sutra, perpendiculars were established using right triangles with sides 3-4-5 and 5-12-13 cords, centuries before Pythagoras!",
        "checkpoints": [
            {
                "id": "c3_1",
                "question": "If line p is perpendicular to line q (p ⊥ q), what is the measure of each angle formed at their intersection?",
                "options": ["45°", "60°", "90°", "180°"],
                "correct": 2,
                "explanation": "Perpendicular lines meet at right angles; every one of the four angles formed measures exactly 90°."
            },
            {
                "id": "c3_2",
                "question": "Which standard mathematical symbol denotes that line m is perpendicular to line n?",
                "options": ["m ∥ n", "m ⊥ n", "m = n", "m ≈ n"],
                "correct": 1,
                "explanation": "The symbol '⊥' (an inverted T) represents perpendicularity: m ⊥ n."
            }
        ]
    },

    # Slide 4: Between Lines - Parallel Lines
    {
        "id": 4,
        "section": "5.3",
        "tag": "Section 5.3 • Between Lines: Parallel Lines",
        "title": "Lines That Never Meet: The Invariant Distance of Parallel Lines",
        "key_terms": ["Parallel Lines", "Equidistant", "Perpendicular Distance", "Non-Intersecting Lines"],
        "sim_id": "parallel_railway_tracks_sim",
        "sim_title": "Railway Tracks & Invariant Perpendicular Distance Lab",
        "narration": "Imagine train tracks stretching straight to the horizon. Do the two steel rails ever cross each other? Never! Lines on the same plane that never meet, no matter how far extended in either direction, are called parallel lines. The perpendicular distance between them remains constant everywhere.",
        "theory": [
            "**Parallel Lines**: Two or more straight lines in the same plane that do not intersect at any point, even when extended indefinitely in both directions.",
            "If line $l$ is parallel to line $m$, we write: $$l \parallel m$$",
            "**Equidistant Property**: The perpendicular distance between two parallel lines is constant throughout their entire length. If you measure distance at point $A$, it is identical to the distance measured at point $B$.",
            "Everyday instances of parallel lines: opposite edges of a ruler, railway tracks, electric power cables suspended on poles, and ruled lines on your notebook pages."
        ],
        "fact_box": "Notice the condition 'in the same plane'! Two lines that never meet in 3D space but lie on different planes are called 'skew lines'. True parallel lines MUST be coplanar.",
        "checkpoints": [
            {
                "id": "c4_1",
                "question": "Two straight lines lie on the same flat table and never intersect, even if extended infinitely. These lines are called:",
                "options": ["Perpendicular lines", "Parallel lines", "Intersecting lines", "Concurrent lines"],
                "correct": 1,
                "explanation": "Lines in the same plane that never meet are by definition parallel lines."
            },
            {
                "id": "c4_2",
                "question": "The perpendicular distance between two parallel lines at point X is 4.5 cm. What will be the perpendicular distance between them 100 meters away?",
                "options": ["0 cm (they meet)", "9.0 cm (doubled)", "4.5 cm (exactly the same)", "Cannot be determined"],
                "correct": 2,
                "explanation": "Parallel lines are equidistant everywhere; the perpendicular distance remains strictly constant at 4.5 cm."
            }
        ]
    },

    # Slide 5: Paper Folding - Perpendicular Lines
    {
        "id": 5,
        "section": "5.4",
        "tag": "Section 5.4 • Paper Folding Constructions: Perpendiculars",
        "title": "Hands-On Origami Geometry: Creasing Perpendicular Lines",
        "key_terms": ["Paper Folding", "Crease", "Folding Superposition", "Square Corner Notations"],
        "sim_id": "paper_folding_perpendicular_sim",
        "sim_title": "Interactive Paper Folding: Creating a 90° Perpendicular Crease",
        "narration": "You do not always need a brass compass to create geometry! Take a sheet of paper. Fold it once to create a baseline crease. Now, fold the paper over onto itself so that the baseline lies exactly on top of itself. When you unfold, the new crease crosses the first at precisely 90 degrees!",
        "theory": [
            "**Origami Geometry (Paper Folding)** relies on reflection symmetry and exact edge superposition.",
            "**Constructing a Perpendicular by Folding**:",
            "1. Take an irregular or rectangular sheet of paper and make a straight crease line $AB$.",
            "2. Pick a point $P$ on line $AB$. Fold the paper over so that the segment of $AB$ on one side of $P$ lies exactly over the segment of $AB$ on the other side.",
            "3. Flatten the fold firmly to produce crease $PQ$.",
            "4. When unfolded, the two halves of the straight angle ($180°$) have been folded onto each other. By symmetry, both angles are equal: $180° \div 2 = 90°$. Hence, $PQ \perp AB$!"
        ],
        "fact_box": "Paper folding geometry (called 'Origamics' in modern math) was formalized by Humiaki Huzita into seven geometric folding axioms that can solve cubic equations!",
        "checkpoints": [
            {
                "id": "c5_1",
                "question": "Why does folding a straight crease onto itself produce an angle of exactly 90°?",
                "options": ["Paper has 90° fibers", "It divides the 180° straight angle into two equal halves", "Every fold creates 45°", "Because paper is flat"],
                "correct": 1,
                "explanation": "Superimposing a straight line (180°) onto itself splits the straight angle into two equal congruent parts: 180° / 2 = 90°."
            },
            {
                "id": "c5_2",
                "question": "What geometric symbol is drawn at the intersection of two perpendicular folded creases?",
                "options": ["A small circle", "A triangle", "A small square box (∟)", "A wavy curve"],
                "correct": 2,
                "explanation": "A small square corner box (∟) is the universal symbol indicating a 90° right angle."
            }
        ]
    },

    # Slide 6: Paper Folding - Parallel Lines & Chevron Notations
    {
        "id": 6,
        "section": "5.4",
        "tag": "Section 5.4 • Paper Folding Constructions: Parallel Lines",
        "title": "Double Fold to Parallel Lines & Standard Arrow Symbols",
        "key_terms": ["Parallel Creases", "Double Perpendicular", "Chevron Arrow Notation", "Parallel Symbol"],
        "sim_id": "paper_folding_parallel_sim",
        "sim_title": "Double-Fold Parallel Crease & Arrowhead Generator",
        "narration": "How can you create two parallel lines using paper folding? If you fold a crease perpendicular to a line, and then make a second crease perpendicular to that new line, the first and third creases are parallel! We mark parallel lines with matching arrowheads.",
        "theory": [
            "**The Double-Perpendicular Principle**: Two straight lines that are both perpendicular to the same common line are parallel to each other ($l \perp t$ and $m \perp t \implies l \parallel m$).",
            "**Paper Folding Steps for Parallel Lines**:",
            "1. Make an initial crease $l$ across the paper.",
            "2. Fold a crease $t$ perpendicular to $l$.",
            "3. At a different location along $t$, fold a third crease $m$ perpendicular to $t$.",
            "4. Unfold the paper: creases $l$ and $m$ will never meet—they are strictly parallel!",
            "**Geometric Arrowhead Notation**: In drawings, parallel lines are distinguished by single matching chevrons ($\rangle$) or double chevrons ($\gg$). Lines with the same number of matching arrows are parallel."
        ],
        "fact_box": "Carpenters use this exact double-perpendicular principle every day: using a try-square to rule parallel cutting guidelines across wood planks.",
        "checkpoints": [
            {
                "id": "c6_1",
                "question": "If line a is perpendicular to line t, and line b is also perpendicular to line t, what is the relationship between lines a and b?",
                "options": ["a is perpendicular to b", "a is parallel to b", "a intersects b at 45°", "a and b are coincident"],
                "correct": 1,
                "explanation": "Two lines perpendicular to the same straight line on a plane are parallel to each other (a ∥ b)."
            },
            {
                "id": "c6_2",
                "question": "In a geometric textbook diagram, what do matching single arrowheads (>) drawn along two lines indicate?",
                "options": ["The lines have infinite length", "The lines are parallel", "The lines are perpendicular", "The lines move at the same speed"],
                "correct": 1,
                "explanation": "Matching arrowheads along line segments indicate that those lines are parallel to each other."
            }
        ]
    },

    # Slide 7: Transversals - The 8-Angle Intersection
    {
        "id": 7,
        "section": "5.5",
        "tag": "Section 5.5 • Transversals",
        "title": "The Transversal: 8 Angles at a Double Crossing",
        "key_terms": ["Transversal", "Interior Angles", "Exterior Angles", "Eight-Angle System"],
        "sim_id": "transversal_eight_angles_sim",
        "sim_title": "Transversal Anatomy: 8 Angles & Region Explorer",
        "narration": "A straight line that cuts across two or more other lines at distinct points is called a transversal. Look closely at the double crossing: exactly eight angles are created in total! Let us classify them into interior angles living between the lines, and exterior angles living on the outside.",
        "theory": [
            "**Definition of Transversal**: A straight line that intersects two or more lines at distinct points is known as a **transversal**.",
            "When a transversal $t$ crosses two lines $l$ and $m$, it creates **two intersection vertices**, generating **8 angles** in total (numbered 1 through 8).",
            "**Interior Angles**: The four angles located in the region *between* the two lines: $$\angle 3, \angle 4, \angle 5, \angle 6$$",
            "**Exterior Angles**: The four angles located on the outer sides *outside* the two lines: $$\angle 1, \angle 2, \angle 7, \angle 8$$",
            "Even if lines $l$ and $m$ are NOT parallel, a transversal still creates these eight labeled angles."
        ],
        "fact_box": "The word 'transversal' originates from the Latin 'transversus', meaning 'turned across' or 'lying athwart'. It literally cuts across a family of lines.",
        "checkpoints": [
            {
                "id": "c7_1",
                "question": "A straight line intersects two distinct lines at two different points. This line is termed a:",
                "options": ["Tangent", "Transversal", "Radius", "Chord"],
                "correct": 1,
                "explanation": "A line crossing two or more distinct lines at distinct points is defined as a transversal."
            },
            {
                "id": "c7_2",
                "question": "How many total angles are formed when a single transversal cuts across two lines?",
                "options": ["4 angles", "6 angles", "8 angles", "12 angles"],
                "correct": 2,
                "explanation": "Four angles are formed at each of the two intersection points, giving 4 + 4 = 8 angles in total."
            }
        ]
    },

    # Slide 8: Corresponding Angles - The F-Shape Explorer
    {
        "id": 8,
        "section": "5.6",
        "tag": "Section 5.6 • Corresponding Angles",
        "title": "Matching Positions: Corresponding Angles & The 'F-Shape'",
        "key_terms": ["Corresponding Angles", "F-Shape Pattern", "Relative Position", "Parallel Lines Postulate"],
        "sim_id": "corresponding_angles_f_shape_sim",
        "sim_title": "The Iconic 'F-Shape' Corresponding Angles Explorer",
        "narration": "Look at the angles that occupy the exact same relative position at each intersection—both top-right, both top-left, both bottom-right, or both bottom-left. These matching pairs are called corresponding angles! They trace out the letter F. When the lines are parallel, corresponding angles are always equal!",
        "theory": [
            "**Corresponding Angles**: Angles that hold matching relative locations at each vertex created by the transversal.",
            "The **4 Pairs of Corresponding Angles** are:",
            "1. Top-Right: $\angle 1$ and $\angle 5$",
            "2. Top-Left: $\angle 2$ and $\angle 6$",
            "3. Bottom-Right: $\angle 4$ and $\angle 8$",
            "4. Bottom-Left: $\angle 3$ and $\angle 7$",
            "**The Visual Memory Aid: The 'F-Shape'**: Corresponding angles lie at the inner corners of an **'F'** shape (which may be upright, inverted, backwards, or tilted).",
            "**The Fundamental Parallel Rule**: If two parallel lines are cut by a transversal, each pair of corresponding angles is **strictly equal** ($\angle 1 = \angle 5$, etc.)."
        ],
        "fact_box": "Euclid recognized the equality of corresponding angles as an unprovable universal axiom, making it the foundation of his famous Fifth Postulate.",
        "checkpoints": [
            {
                "id": "c8_1",
                "question": "Which letter of the English alphabet visually highlights the position of corresponding angles?",
                "options": ["Z-shape", "C-shape", "F-shape", "X-shape"],
                "correct": 2,
                "explanation": "Corresponding angles lie at the matching arm corners of the letter 'F' (upright or inverted)."
            },
            {
                "id": "c8_2",
                "question": "Lines l and m are parallel. If ∠1 = 70° (top-right), what is the measure of its corresponding angle ∠5 at the second intersection?",
                "options": ["110°", "70°", "20°", "140°"],
                "correct": 1,
                "explanation": "When lines are parallel, corresponding angles are equal. Therefore, ∠5 = ∠1 = 70°."
            }
        ]
    },

    # Slide 9: Corresponding Angles as a Parallelism Test
    {
        "id": 9,
        "section": "5.6",
        "tag": "Section 5.6 • Testing for Parallel Lines",
        "title": "The Converse Test: Proving Lines are Parallel",
        "key_terms": ["Converse Property", "Parallelism Test", "Angle Equality Check", "Geometric Verification"],
        "sim_id": "parallelism_detector_sim",
        "sim_title": "Interactive Parallelism Detector: Aligning Corresponding Angles",
        "narration": "Geometry works in both directions! If lines are parallel, corresponding angles are equal. Conversely, if a transversal cuts two lines and ANY single pair of corresponding angles is equal, the lines MUST be parallel! This gives us a foolproof test to check if two tracks or walls are truly parallel.",
        "theory": [
            "**The Converse of the Corresponding Angles Axiom**: When a transversal cuts two coplanar lines, if a pair of corresponding angles is found to be equal, then the two lines are **guaranteed to be parallel**.",
            "**How to test if two lines are parallel in practice**:",
            "1. Draw any transversal crossing both lines.",
            "2. Measure a corresponding angle pair (e.g. top-right angle $\alpha$ and top-right angle $\beta$).",
            "3. If $\alpha = \beta$, the lines are strictly parallel ($l \parallel m$).",
            "4. If $\alpha \neq \beta$, the lines are NOT parallel and will eventually intersect on the side where the interior angles sum to less than 180°!"
        ],
        "fact_box": "Masons and civil engineers use this converse test with optical theodolites to ensure high-rise building pillars remain perfectly parallel to vertical plumb lines.",
        "checkpoints": [
            {
                "id": "c9_1",
                "question": "A transversal cuts two lines. One corresponding angle is 85° and the other corresponding angle is 82°. Are the two lines parallel?",
                "options": ["Yes, because both are acute", "Yes, they differ by only 3°", "No, because corresponding angles are not equal", "Yes, if extended far enough"],
                "correct": 2,
                "explanation": "For lines to be parallel, corresponding angles must be exactly equal. Since 85° ≠ 82°, the lines are not parallel."
            },
            {
                "id": "c9_2",
                "question": "If you want to verify that two lines are parallel, how many pairs of corresponding angles do you need to prove are equal?",
                "options": ["Just one pair", "All 4 pairs independently", "At least 3 pairs", "8 pairs"],
                "correct": 0,
                "explanation": "If any single pair of corresponding angles is equal, vertically opposite and linear pair laws automatically ensure all other pairs are equal, confirming parallelism."
            }
        ]
    },

    # Slide 10: Drawing Parallel Lines with Ruler and Set Square
    {
        "id": 10,
        "section": "5.7",
        "tag": "Section 5.7 • Drawing Parallel Lines",
        "title": "Practical Construction: The Ruler and Set Square Slide Method",
        "key_terms": ["Set Square", "Ruler Construction", "External Point P", "Sliding Edge Principle"],
        "sim_id": "ruler_set_square_construction_sim",
        "sim_title": "Interactive 4-Step Ruler & Set Square Parallel Drafter",
        "narration": "How do architects and draftsmen draw a line parallel to a given line through an external point? They use a ruler and a triangular set square! By sliding the set square along the fixed ruler, the angle of the set square edge remains unchanged, copying the corresponding angle perfectly!",
        "theory": [
            "**Objective**: To draw a line parallel to line $l$ passing through an external point $P$ not lying on $l$.",
            "**Step-by-Step Construction Procedure**:",
            "1. **Step 1**: Place one edge of a set square along the given line $l$.",
            "2. **Step 2**: Place a straight ruler firmly against another edge of the set square (this ruler edge serves as the transversal line!).",
            "3. **Step 3**: Hold the ruler tightly in place, and slide the set square along the ruler edge until its drawing edge passes through point $P$.",
            "4. **Step 4**: Draw line $m$ along the set square edge through $P$.",
            "**Mathematical Principle**: The ruler acts as a transversal. The angle between the ruler and the set square edge remains identical during sliding. Since corresponding angles are equal, line $m$ is strictly parallel to line $l$!"
        ],
        "fact_box": "Drafting T-squares and parallel rolling rulers used in engineering offices operate on this exact identical sliding corresponding angle mechanism.",
        "checkpoints": [
            {
                "id": "c10_1",
                "question": "In the ruler and set square construction method, which instrument acts as the transversal?",
                "options": ["The pencil", "The fixed straight ruler", "The paper edge", "The hypotenuse of the table"],
                "correct": 1,
                "explanation": "The fixed edge of the ruler against which the set square slides acts as the transversal cutting both lines."
            },
            {
                "id": "c10_2",
                "question": "Why does sliding the set square along the ruler guarantee that the newly drawn line is parallel to the original line?",
                "options": ["Because rulers are made of plastic", "Because the corresponding angle remains constant during sliding", "Because points on paper never move", "Because set squares have right angles"],
                "correct": 1,
                "explanation": "Sliding preserves the orientation angle between the set square edge and ruler edge, creating equal corresponding angles which guarantees parallelism."
            }
        ]
    },

    # Slide 11: Alternate Interior Angles - The Z-Shape Explorer
    {
        "id": 11,
        "section": "5.8",
        "tag": "Section 5.8 • Alternate Angles: Interior",
        "title": "Alternate Interior Angles: The Famous 'Z-Shape' & Rigorous Proof",
        "key_terms": ["Alternate Interior Angles", "Z-Shape Pattern", "Zig-Zag Angles", "Deductive Proof"],
        "sim_id": "alternate_interior_z_shape_sim",
        "sim_title": "The 'Z-Shape' Alternate Interior Angles & Proof Engine",
        "narration": "Now look inside the two lines on opposite sides of the transversal. One angle is to the left, one is to the right. These are alternate interior angles! They form the famous letter Z. Let us prove mathematically why they must be equal when the lines are parallel.",
        "theory": [
            "**Alternate Interior Angles**: Angles lying inside the region between the two lines, but on opposite (alternate) sides of the transversal line.",
            "The **2 Pairs of Alternate Interior Angles** are:",
            "- Pair 1: $\angle 3$ and $\angle 5$",
            "- Pair 2: $\angle 4$ and $\angle 6$",
            "**The Visual Memory Aid: The 'Z-Shape'**: Look for the letter **'Z'** (or backwards 'Z'). The angles tucked in the alternate inner nooks of the Z are alternate interior angles.",
            "**Logical Mathematical Proof**:",
            "1. By Corresponding Angles Postulate: $\angle 1 = \angle 5$ (matching top-right positions).",
            "2. By Vertically Opposite Angles Theorem: $\angle 1 = \angle 3$.",
            "3. Therefore, by transitive equality: $$\angle 3 = \angle 5$$",
            "Hence, when lines are parallel, **alternate interior angles are always equal**!"
        ],
        "fact_box": "In Indian classical architecture (*Vastu Vidya*), the Z-shape diagonal brace was used in wooden roof trusses to keep parallel rafters rigid and stable.",
        "checkpoints": [
            {
                "id": "c11_1",
                "question": "Which letter of the alphabet represents the alternate interior angles pattern?",
                "options": ["Letter F", "Letter Z", "Letter C", "Letter T"],
                "correct": 1,
                "explanation": "Alternate interior angles are found tucked inside the corners of the letter 'Z' (upright or reversed)."
            },
            {
                "id": "c11_2",
                "question": "Two parallel lines are crossed by a transversal. If one interior angle is 54°, what is the measure of its alternate interior angle?",
                "options": ["126°", "54°", "36°", "90°"],
                "correct": 1,
                "explanation": "When lines are parallel, alternate interior angles are equal in measure. Therefore, it is also exactly 54°."
            }
        ]
    },

    # Slide 12: Alternate Exterior Angles
    {
        "id": 12,
        "section": "5.8",
        "tag": "Section 5.8 • Alternate Angles: Exterior",
        "title": "Alternate Exterior Angles: Outer Zigzag Balance",
        "key_terms": ["Alternate Exterior Angles", "Outer Zigzag", "Transversal Boundary", "Equal Angle Pairs"],
        "sim_id": "alternate_exterior_angles_sim",
        "sim_title": "Alternate Exterior Angles Explorer & Dynamic Sync",
        "narration": "Just as we have alternate angles on the inside, we also have alternate angles on the outside! Lying on opposite sides of the transversal and outside the parallel lines, alternate exterior angles are also equal to each other.",
        "theory": [
            "**Alternate Exterior Angles**: Angles lying outside the two parallel lines on opposite (alternate) sides of the transversal.",
            "The **2 Pairs of Alternate Exterior Angles** are:",
            "- Pair 1: $\angle 1$ and $\angle 7$ (top-right and bottom-left outside)",
            "- Pair 2: $\angle 2$ and $\angle 8$ (top-left and bottom-right outside)",
            "**Proof that Alternate Exterior Angles are Equal**:",
            "- $\angle 1 = \angle 5$ (Corresponding angles)",
            "- $\angle 5 = \angle 7$ (Vertically opposite angles)",
            "- Substituting gives: $$\angle 1 = \angle 7$$",
            "Similarly, $\angle 2 = \angle 6 = \angle 8 \implies \angle 2 = \angle 8$."
        ],
        "fact_box": "Because every angle in the 8-angle parallel system is either equal to angle x or supplementary to it (180° - x), there are ONLY TWO distinct angle values in the entire system!",
        "checkpoints": [
            {
                "id": "c12_1",
                "question": "Which pair represents alternate exterior angles in the 8-angle transversal system?",
                "options": ["∠1 and ∠5", "∠3 and ∠5", "∠1 and ∠7", "∠4 and ∠5"],
                "correct": 2,
                "explanation": "Angles ∠1 (top exterior right) and ∠7 (bottom exterior left) are alternate exterior angles."
            },
            {
                "id": "c12_2",
                "question": "If lines l ∥ m and exterior angle ∠2 = 115°, what is the measure of alternate exterior angle ∠8?",
                "options": ["65°", "115°", "25°", "180°"],
                "correct": 1,
                "explanation": "Alternate exterior angles are equal when lines are parallel. Hence, ∠8 = 115°."
            }
        ]
    },

    # Slide 13: Interior Angles on the Same Side of Transversal (Co-Interior / C-Shape)
    {
        "id": 13,
        "section": "5.8",
        "tag": "Section 5.8 • Co-Interior Angles",
        "title": "Interior Angles on the Same Side: The 'C-Shape' 180° Rule",
        "key_terms": ["Co-Interior Angles", "Consecutive Interior Angles", "Allied Angles", "C-Shape / U-Shape"],
        "sim_id": "co_interior_c_shape_sim",
        "sim_title": "The 'C-Shape' Co-Interior Angles Supplementary Lab",
        "narration": "What about the two interior angles that lie on the SAME side of the transversal line? They form the shape of the letter C! Unlike alternate angles, co-interior angles are NOT equal. Instead, they always add up to exactly 180 degrees. They are supplementary!",
        "theory": [
            "**Interior Angles on the Same Side of Transversal** (also called **Co-Interior** or **Allied Angles**): The pair of interior angles located on the same side of the transversal line.",
            "The **2 Pairs of Co-Interior Angles** are:",
            "- Pair 1 (Right Side): $\angle 4$ and $\angle 5$",
            "- Pair 2 (Left Side): $\angle 3$ and $\angle 6$",
            "**The Visual Memory Aid: The 'C-Shape'** (or 'U-Shape'): These angles are captured inside the jaws of the letter **'C'**.",
            "**Proof of Supplementary Property**:",
            "1. $\angle 4 + \angle 1 = 180°$ (Linear pair on line $l$).",
            "2. But $\angle 1 = \angle 5$ (Corresponding angles since $l \parallel m$).",
            "3. Replacing $\angle 1$ with $\angle 5$: $$\angle 4 + \angle 5 = 180°$$",
            "**Theorem**: Interior angles on the same side of a transversal across parallel lines are **always supplementary (add to 180°)**."
        ],
        "fact_box": "This theorem is the exact contrapositive of Euclid's 5th Postulate: if interior angles on one side add to less than 180°, the lines MUST converge and meet on that side!",
        "checkpoints": [
            {
                "id": "c13_1",
                "question": "What is the sum of two interior angles on the same side of a transversal cutting parallel lines?",
                "options": ["90°", "180°", "270°", "360°"],
                "correct": 1,
                "explanation": "Interior angles on the same side of a transversal (co-interior angles) are supplementary and always sum to 180°."
            },
            {
                "id": "c13_2",
                "question": "If two parallel lines are cut by a transversal and one co-interior angle is 105°, what is the other co-interior angle?",
                "options": ["105°", "75°", "85°", "15°"],
                "correct": 1,
                "explanation": "Co-interior angles add to 180°: 180° - 105° = 75°."
            }
        ]
    },

    # Slide 14: Parallel Illusions - The Café Wall Illusion
    {
        "id": 14,
        "section": "5.9",
        "tag": "Section 5.9 • Parallel Illusions: Café Wall",
        "title": "Geometric Illusions: The Famous Café Wall Optical Puzzle",
        "key_terms": ["Café Wall Illusion", "Optical Illusion", "Visual Perception", "Mortar Lines"],
        "sim_id": "cafe_wall_illusion_sim",
        "sim_title": "Café Wall Illusion Lab: Unmasking the Parallel Lines",
        "narration": "Can your eyes deceive you? In 1973, psychologist Richard Gregory observed a tiled wall in a café in Bristol, England. The horizontal grout lines looked wildly crooked and wedge-shaped! Yet every single horizontal line on that wall was mathematically dead straight and parallel. Explore why our brain gets tricked!",
        "theory": [
            "**The Café Wall Illusion** is a geometrical-optical illusion where straight, parallel horizontal mortar lines between staggered rows of black and white tiles appear to be sloped at alternating angles.",
            "**Why does the illusion happen?**",
            "- The brain's visual cortex uses edge-detecting neurons (retinal luminance cells) to interpret high-contrast borders.",
            "- The offset black-and-white tiles create brightness contrasts across the thin grey dividing line ('mortar line').",
            "- This trick causes the visual system to perceive small diagonal shear forces at each corner, tilting the perceived orientation of the continuous line.",
            "**Mathematical Reality**: If you place a straight ruler across the rows, or remove the tile contrast, every horizontal line is **strictly parallel**!"
        ],
        "fact_box": "The Café Wall pattern was originally published in 1897 as the 'Kindergarten Illusion' because it appeared in early children's tile-pattern playbooks.",
        "checkpoints": [
            {
                "id": "c14_1",
                "question": "In the Café Wall illusion, the horizontal mortar lines between alternating black and white tiles are actually:",
                "options": ["Curved downwards", "Wedge-shaped and zigzagged", "Strictly straight and parallel", "Converging to a vanishing point"],
                "correct": 2,
                "explanation": "Despite appearing tilted to human eyes, the horizontal mortar lines are mathematically completely straight and parallel."
            },
            {
                "id": "c14_2",
                "question": "What happens when you align the black and white tiles into a normal chessboard grid (no offset)?",
                "options": ["The illusion becomes stronger", "The illusion completely disappears and lines look straight", "The lines look circular", "The lines vanish"],
                "correct": 1,
                "explanation": "When tiles are aligned in a standard grid without horizontal shift, luminance symmetry is restored and the illusion vanishes completely."
            }
        ]
    },

    # Slide 15: Parallel Illusions - Hering and Zöllner Illusions
    {
        "id": 15,
        "section": "5.9",
        "tag": "Section 5.9 • Parallel Illusions: Hering & Zöllner",
        "title": "The Hering & Zöllner Illusions: Radiating Angles Distorting Space",
        "key_terms": ["Hering Illusion", "Zöllner Illusion", "Angle Overestimation", "Bowing Illusion"],
        "sim_id": "hering_zollner_illusions_sim",
        "sim_title": "Hering & Zöllner Illusions: Interactive Angle Stripper",
        "narration": "Look at these two red lines: do they bow outwards like a barrel? Look at the diagonal lines: do they seem tilted in opposite directions? This is the Hering and Zöllner effect! The acute intersecting background lines force our brain to overestimate acute angles, distorting our perception of parallel lines.",
        "theory": [
            "**The Hering Illusion (1861)**: Two straight, parallel vertical lines are superimposed over a background of radiating spokes (like a bicycle wheel). The parallel lines appear to **bow outwards** in the middle away from the central vanishing point.",
            "**The Zöllner Illusion (1860)**: Parallel lines crossed by short, alternating diagonal hatch lines appear to diverge and converge, looking crooked rather than parallel.",
            "**Neuroscientific Explanation**:",
            "- Human vision suffers from **perceptual acute angle expansion**: our visual cortex tends to overestimate acute angles and underestimate obtuse angles.",
            "- The intersecting hatch lines or radial spokes 'push' the perceived orientation of the parallel lines away from the acute intersections.",
            "- Toggle the background lines off in our simulator to witness the red lines snap into undeniable parallel perfection!"
        ],
        "fact_box": "German astrophysicist Johann Zöllner discovered this illusion in 1860 while studying patterned fabric designs in a Leipzig textile shop!",
        "checkpoints": [
            {
                "id": "c15_1",
                "question": "In the Hering illusion, what causes two parallel lines to look bent or bowed outwards?",
                "options": ["The red color of the lines", "A background of radial lines spreading outward from a center point", "The thickness of the paper", "Poor lighting in the room"],
                "correct": 1,
                "explanation": "Radial background lines crossing the parallel lines trigger acute-angle expansion in the human brain, causing the lines to appear bent outward."
            },
            {
                "id": "c15_2",
                "question": "How can you scientifically prove to an observer that the lines in the Zöllner illusion are truly parallel?",
                "options": ["By measuring the perpendicular distance between the lines at multiple points with a ruler", "By guessing", "By rotating the screen 90 degrees", "By squinting your eyes"],
                "correct": 0,
                "explanation": "Measuring the perpendicular distance between the main lines at different points demonstrates that it is constant, proving they are parallel."
            }
        ]
    },

    # Slide 16: Heritage Review - Acharya Baudhayana's Sulba Sutra Geometry
    {
        "id": 16,
        "section": "Review",
        "tag": "Chapter Review • Vedic Geometric Heritage",
        "title": "Baudhayana's Sacred Geometry: The Cord & Peg (*Sanku-Rajju*) Method",
        "key_terms": ["Sulba Sutras", "Baudhayana", "Sanku (Gnomon)", "Rajju (Cord)", "Altar Geometry"],
        "sim_id": "baudhayana_sulba_ropes_sim",
        "sim_title": "Baudhayana's Ancient Rope & Peg Geometrical Construction Lab",
        "narration": "Centuries before modern rulers, ancient Indian masters used simple ropes (*rajju*) and wooden pegs (*sanku*) to lay out exact East-West parallel lines and North-South perpendiculars for sacred altars like the Shyena-chiti (Falcon Altar). Let us celebrate this grand heritage of Indian geometry!",
        "theory": [
            "**The Sulba Sutras (800–500 BCE)** are the world's earliest known manuals of practical geometry and geometric algebra.",
            "**Baudhayana's Parallel & Perpendicular Construction Method**:",
            "1. **Establishing the Meridian (North-South Perpendicular)**: Fix a vertical rod (*sanku*) in the ground. Trace its morning and evening shadow tips on a circle. The line joining these points gives a true East-West base line.",
            "2. **Constructing Perpendiculars by Cord Arcs**: Tie a cord to the East and West pegs. Strike intersecting circular arcs north and south. The line connecting the arc intersections creates a perfect North-South **perpendicular** line!",
            "3. **Constructing Parallel Lines**: By erecting two identical perpendicular cords along the East-West baseline, the line joining their tops is guaranteed to be **strictly parallel** to the base!",
            "This cord geometry provided flawless parallel lines and right angles for monuments across thousands of years."
        ],
        "fact_box": "The Sanskrit word 'Sulba' means 'cord or measuring rope', and 'Sutra' means 'rule or aphorism'. Sulba Sutras were literally the science of rope geometry!",
        "checkpoints": [
            {
                "id": "c16_1",
                "question": "What instruments did ancient Indian mathematicians like Baudhayana use to construct parallel lines and right angles?",
                "options": ["Laser levels and theodolites", "Cords (Rajju) and wooden pegs (Sanku)", "Steel rulers and plastic set squares", "Calculators"],
                "correct": 1,
                "explanation": "Ancient Sulba geometers used measuring cords (Rajju) and vertical pegs (Sanku) with circular arc intersections."
            },
            {
                "id": "c16_2",
                "question": "What is the meaning of the Sanskrit word 'Sulba' in the title 'Sulba Sutras'?",
                "options": ["Metal knife", "Measuring cord or rope", "Clay brick", "Flame of fire"],
                "correct": 1,
                "explanation": "'Sulba' translates to a measuring rope or cord used for accurate geometrical layout."
            }
        ]
    },

    # Slide 17: Mastery Challenge 1 (Questions 1 to 10)
    {
        "id": 17,
        "section": "Quiz 1",
        "is_quiz": True,
        "quiz_range": (1, 10),
        "tag": "Mastery Challenge • Part 1",
        "title": "Mastery Quiz 1: Intersecting Lines, Linear Pairs & Perpendiculars",
        "narration": "Welcome to Part 1 of the Chapter Mastery Challenge! Test your knowledge on intersecting lines, vertically opposite angles, linear pairs, and perpendicular relationships. Choose your answer and view the step-by-step mathematical proof for each problem."
    },

    # Slide 18: Mastery Challenge 2 (Questions 11 to 20)
    {
        "id": 18,
        "section": "Quiz 2",
        "is_quiz": True,
        "quiz_range": (11, 20),
        "tag": "Mastery Challenge • Part 2",
        "title": "Mastery Quiz 2: Parallel Lines, Paper Folding & Transversals",
        "narration": "Mastery Quiz Part 2! Here we test parallel line properties, equidistant measurements, paper folding constructions, and the 8-angle transversal system. Focus on geometric definitions and visual reasoning."
    },

    # Slide 19: Mastery Challenge 3 (Questions 21 to 30)
    {
        "id": 19,
        "section": "Quiz 3",
        "is_quiz": True,
        "quiz_range": (21, 30),
        "tag": "Mastery Challenge • Part 3",
        "title": "Mastery Quiz 3: Corresponding, Alternate & Co-Interior Angles",
        "narration": "Welcome to Mastery Quiz Part 3! Put the F-shape, Z-shape, and C-shape angle properties to work! Calculate unknown angles across parallel lines and verify whether given lines are parallel."
    },

    # Slide 20: Mastery Challenge 4 (Questions 31 to 40)
    {
        "id": 20,
        "section": "Quiz 4",
        "is_quiz": True,
        "quiz_range": (31, 40),
        "tag": "Mastery Challenge • Part 4 (Final)",
        "title": "Mastery Quiz 4: Complex Multi-Step Geometric Problems & Heritage",
        "narration": "The Final Mastery Challenge! Solve advanced multi-step angle puzzles, constructions with set squares, optical illusions, and historical Sulba Sutra geometry. When you complete this slide, you will have mastered Chapter 5!"
    }
]

QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "Two straight lines AB and CD intersect at point O. If ∠AOC = 48°, what is the measure of ∠BOD?",
        "options": ["42°", "48°", "132°", "180°"],
        "correct": 1,
        "solution": "Step 1: Identify the relationship between ∠AOC and ∠BOD.\nStep 2: Since lines AB and CD cross at O, ∠AOC and ∠BOD are vertically opposite angles.\nStep 3: Vertically opposite angles are always equal.\nConclusion: ∠BOD = ∠AOC = 48°."
    },
    # Q2
    {
        "id": 2,
        "question": "In the same intersection of lines AB and CD at point O with ∠AOC = 48°, what is the measure of adjacent angle ∠AOD?",
        "options": ["48°", "90°", "132°", "142°"],
        "correct": 2,
        "solution": "Step 1: Point O lies on the straight line CD, with ray OA standing on it.\nStep 2: ∠AOC and ∠AOD form a linear pair, so their sum is 180°.\nStep 3: ∠AOD = 180° - ∠AOC = 180° - 48° = 132°.\nConclusion: ∠AOD = 132°."
    },
    # Q3
    {
        "id": 3,
        "question": "Two angles in a linear pair are in the ratio 2 : 3. What is the measure of the smaller angle?",
        "options": ["36°", "60°", "72°", "108°"],
        "correct": 2,
        "solution": "Step 1: Let the two angles be 2x and 3x.\nStep 2: Since they form a linear pair, their sum is 180°: 2x + 3x = 180° ➔ 5x = 180° ➔ x = 36°.\nStep 3: Smaller angle = 2x = 2 × 36° = 72°.\n(Larger angle = 3x = 3 × 36° = 108°).\nConclusion: The smaller angle is 72°."
    },
    # Q4
    {
        "id": 4,
        "question": "If two straight lines intersect such that one of the angles formed is a right angle (90°), what must be true about the remaining three angles?",
        "options": ["Two are 45° and one is 90°", "Each of the other three angles is also 90°", "Two are 60° and one is 120°", "Their measures cannot be determined"],
        "correct": 1,
        "solution": "Step 1: Let one angle be ∠1 = 90°.\nStep 2: Its vertically opposite angle ∠3 = 90°.\nStep 3: Its linear pair neighbor ∠2 = 180° - 90° = 90°, and ∠4 = 180° - 90° = 90°.\nConclusion: All four angles at the intersection are exactly 90°, making the lines perpendicular."
    },
    # Q5
    {
        "id": 5,
        "question": "Which of the following capital letters of the English alphabet contains perpendicular line segments?",
        "options": ["Letter V", "Letter L", "Letter S", "Letter M"],
        "correct": 1,
        "solution": "Step 1: Examine the segments of each letter.\nStep 2: Letter 'L' consists of a vertical line segment meeting a horizontal baseline at an angle of exactly 90°.\nConclusion: Letter 'L' features perpendicular line segments (as do T, H, E, F)."
    },
    # Q6
    {
        "id": 6,
        "question": "Can two complementary angles form a linear pair?",
        "options": ["Yes, if both are 45°", "Yes, if one is 30° and the other is 60°", "No, because complementary angles add to 90°, while a linear pair must add to 180°", "Yes, in 3D geometry"],
        "correct": 2,
        "solution": "Step 1: By definition, complementary angles sum to 90°.\nStep 2: By definition, a linear pair must sum to 180° (a straight angle).\nConclusion: Since 90° ≠ 180°, complementary angles can never form a linear pair."
    },
    # Q7
    {
        "id": 7,
        "question": "An angle is 28° more than its linear pair partner. What is the measure of this angle?",
        "options": ["76°", "104°", "116°", "152°"],
        "correct": 1,
        "solution": "Step 1: Let the smaller partner be x. Then the angle is x + 28°.\nStep 2: Since they form a linear pair: x + (x + 28°) = 180° ➔ 2x + 28° = 180° ➔ 2x = 152° ➔ x = 76°.\nStep 3: The angle = x + 28° = 76° + 28° = 104°.\nConclusion: The angle is 104° (and its partner is 76°; check: 104° + 76° = 180°)."
    },
    # Q8
    {
        "id": 8,
        "question": "Three rays meet at point O on a straight line AB, forming angles measuring (2x)°, (3x)°, and (5x)°. What is the value of x?",
        "options": ["12°", "18°", "20°", "36°"],
        "correct": 1,
        "solution": "Step 1: Angles on one side of a straight line add up to 180°.\nStep 2: 2x + 3x + 5x = 180° ➔ 10x = 180° ➔ x = 18°.\nConclusion: x = 18° (the angles are 36°, 54°, and 90°)."
    },
    # Q9
    {
        "id": 9,
        "question": "Two straight lines intersect. If the sum of two vertically opposite angles is 130°, what is the measure of each of these two angles?",
        "options": ["50°", "65°", "130°", "25°"],
        "correct": 1,
        "solution": "Step 1: Let the two vertically opposite angles be y and y.\nStep 2: Vertically opposite angles are equal, so y + y = 130° ➔ 2y = 130° ➔ y = 65°.\nConclusion: Each of the two vertically opposite angles measures 65°."
    },
    # Q10
    {
        "id": 10,
        "question": "In the question above where two vertically opposite angles sum to 130° (each being 65°), what is the sum of the other two vertically opposite angles?",
        "options": ["130°", "180°", "230°", "360°"],
        "correct": 2,
        "solution": "Step 1: All four angles around an intersection point sum to 360°.\nStep 2: Sum of first two = 130°.\nStep 3: Sum of remaining two = 360° - 130° = 230°.\n(Each of the other two angles is 230° ÷ 2 = 115°).\nConclusion: The sum of the other two angles is 230°."
    },

    # Q11
    {
        "id": 11,
        "question": "Which of the following is NOT an example of parallel lines in daily life?",
        "options": ["The two opposite long edges of a standard ruler", "The two rails of a straight railway track", "The blades of an open pair of scissors", "The horizontal lines ruled on notebook paper"],
        "correct": 2,
        "solution": "Step 1: Parallel lines never meet and remain equidistant.\nStep 2: The blades of an open pair of scissors cross and pivot at a single hinge pin.\nConclusion: Scissor blades are intersecting lines, not parallel lines."
    },
    # Q12
    {
        "id": 12,
        "question": "If line l is parallel to line m, and line m is parallel to line n, what is the relationship between line l and line n?",
        "options": ["l is perpendicular to n", "l is parallel to n", "l intersects n at 45°", "No relationship can be deduced"],
        "correct": 1,
        "solution": "Step 1: By the Transitivity of Parallelism: Two lines that are each parallel to the same line are parallel to each other.\nStep 2: Since l ∥ m and m ∥ n, line l is strictly parallel to line n (l ∥ n).\nConclusion: l ∥ n."
    },
    # Q13
    {
        "id": 13,
        "question": "In paper folding, what angle is formed when you fold a straight baseline crease onto itself so that its two halves match perfectly?",
        "options": ["45°", "60°", "90°", "180°"],
        "correct": 2,
        "explanation": "Folding a straight line (180°) onto itself divides it into two congruent halves: 180° / 2 = 90°.",
        "solution": "Step 1: A straight crease measures 180°.\nStep 2: Folding edge over edge forces both adjacent angles to be identical by symmetry.\nStep 3: Two identical angles that sum to 180° must each be 180° ÷ 2 = 90°.\nConclusion: The crease is perpendicular, measuring 90°."
    },
    # Q14
    {
        "id": 14,
        "question": "Line t intersects line l at point P and line m at point Q (where P ≠ Q). Line t is called a:",
        "options": ["Radius", "Transversal", "Parallel line", "Bisector"],
        "correct": 1,
        "solution": "Step 1: A line intersecting two distinct lines at distinct points is defined as a transversal.\nConclusion: Line t is a transversal."
    },
    # Q15
    {
        "id": 15,
        "question": "A transversal cuts two parallel lines. How many distinct, different angle measures exist among the eight angles formed?",
        "options": ["Exactly 1 (if all are 90°) or 2 (acute and obtuse)", "4 different measures", "8 different measures", "16 different measures"],
        "correct": 0,
        "solution": "Step 1: When lines are parallel, all four acute angles are equal (say x°), and all four obtuse angles are equal (180° - x°).\nStep 2: If x = 90°, all 8 angles are 90° (1 distinct value).\nStep 3: If x ≠ 90°, there are exactly 2 distinct angle values: x° and 180° - x°.\nConclusion: At most 2 distinct angle measures exist (or 1 if perpendicular)."
    },
    # Q16
    {
        "id": 16,
        "question": "In the standard 8-angle transversal diagram, which of the following is an interior angle?",
        "options": ["An angle lying outside line l", "An angle lying in the space between line l and line m", "An angle outside line m", "An angle with vertex not on the transversal"],
        "correct": 1,
        "solution": "Step 1: 'Interior' in transversal geometry refers strictly to the region sandwiched between the two main lines.\nConclusion: An angle lying between line l and line m is an interior angle."
    },
    # Q17
    {
        "id": 17,
        "question": "How many pairs of interior angles exist when a transversal crosses two lines?",
        "options": ["1 pair", "2 pairs (4 interior angles total)", "4 pairs", "8 pairs"],
        "correct": 1,
        "solution": "Step 1: There are 4 interior angles: ∠3, ∠4, ∠5, ∠6.\nStep 2: They form 2 alternate interior pairs (∠3 & ∠5, ∠4 & ∠6) and 2 co-interior pairs (∠3 & ∠6, ∠4 & ∠5).\nConclusion: There are 4 interior angles forming 2 pairs."
    },
    # Q18
    {
        "id": 18,
        "question": "If line p ⊥ line r, and line q ⊥ line r (in the same plane), what can you conclude about p and q?",
        "options": ["p and q are perpendicular", "p and q are parallel", "p and q intersect at 60°", "p and q form a linear pair"],
        "correct": 1,
        "solution": "Step 1: Both lines p and q make an angle of 90° with the transversal line r.\nStep 2: Since corresponding angles are both 90° (equal), lines p and q must be parallel.\nConclusion: p ∥ q (two lines perpendicular to the same line are parallel)."
    },
    # Q19
    {
        "id": 19,
        "question": "What is the perpendicular distance between two lines if they intersect at a 30° angle?",
        "options": ["Constant 5 cm", "Constant 10 cm", "Not constant (it varies from 0 at the vertex to infinity)", "Always 0 everywhere"],
        "correct": 2,
        "solution": "Step 1: For non-parallel intersecting lines, the distance between them grows as you move further from the intersection point.\nStep 2: At the point of intersection, the distance is 0; further away, it increases without bound.\nConclusion: Perpendicular distance is only constant for parallel lines."
    },
    # Q20
    {
        "id": 20,
        "question": "If you make two successive perpendicular folds across a strip of paper, what is the geometric relationship between the first crease and the second crease?",
        "options": ["They are parallel", "They are perpendicular", "They intersect at 45°", "They overlap completely"],
        "correct": 1,
        "solution": "Step 1: The first fold makes crease 1.\nStep 2: Folding perpendicular across crease 1 creates crease 2.\nStep 3: Crease 1 and crease 2 are at 90° to each other (perpendicular).\n(Note: Folding a third crease perpendicular to crease 2 would make crease 1 and crease 3 parallel).\nConclusion: The two creases are perpendicular."
    },

    # Q21
    {
        "id": 21,
        "question": "A transversal cuts two parallel lines. If a top-left corresponding angle is 112°, what is the measure of the bottom-left corresponding angle at the second vertex?",
        "options": ["68°", "112°", "224°", "90°"],
        "correct": 1,
        "solution": "Step 1: Corresponding angles occupy matching relative positions.\nStep 2: When lines are parallel, corresponding angles are equal.\nConclusion: The corresponding angle is exactly 112°."
    },
    # Q22
    {
        "id": 22,
        "question": "Which letter of the alphabet is universally associated with alternate interior angles?",
        "options": ["F", "Z", "C", "X"],
        "correct": 1,
        "solution": "Step 1: The letter 'Z' has parallel top and bottom horizontal strokes connected by a diagonal transversal.\nStep 2: The interior angles tucked inside the corners of the 'Z' are alternate interior angles.\nConclusion: The letter 'Z'."
    },
    # Q23
    {
        "id": 23,
        "question": "Two parallel lines are cut by a transversal. If one interior angle is 63°, what is the measure of its alternate interior angle?",
        "options": ["27°", "63°", "117°", "180°"],
        "correct": 1,
        "solution": "Step 1: Alternate interior angles are equal when lines are parallel.\nConclusion: The alternate interior angle is 63°."
    },
    # Q24
    {
        "id": 24,
        "question": "Two parallel lines are cut by a transversal. If one interior angle is 63°, what is the measure of the interior angle on the SAME side of the transversal (co-interior angle)?",
        "options": ["63°", "90°", "117°", "127°"],
        "correct": 2,
        "solution": "Step 1: Interior angles on the same side of a transversal across parallel lines are supplementary.\nStep 2: Angle = 180° - 63° = 117°.\nConclusion: The co-interior angle is 117°."
    },
    # Q25
    {
        "id": 25,
        "question": "A transversal cuts two lines. A pair of corresponding angles measures 79° and 81°. What can you deduce about the two lines?",
        "options": ["They are parallel", "They are perpendicular", "They are NOT parallel and will intersect", "They are coincident"],
        "correct": 2,
        "solution": "Step 1: By the Converse of the Corresponding Angles Postulate, lines are parallel if and only if corresponding angles are equal.\nStep 2: Since 79° ≠ 81°, the lines are not parallel.\nConclusion: They are not parallel and will eventually intersect."
    },
    # Q26
    {
        "id": 26,
        "question": "In the diagram of parallel lines cut by a transversal, two co-interior angles are represented by (3x + 10)° and (2x + 20)°. What is the value of x?",
        "options": ["20°", "30°", "40°", "50°"],
        "correct": 1,
        "solution": "Step 1: Co-interior angles across parallel lines sum to 180°.\nStep 2: (3x + 10) + (2x + 20) = 180° ➔ 5x + 30 = 180° ➔ 5x = 150° ➔ x = 30°.\nConclusion: x = 30° (the angles are 100° and 80°; check: 100° + 80° = 180°)."
    },
    # Q27
    {
        "id": 27,
        "question": "Which angle pair is always supplementary when two parallel lines are crossed by a transversal?",
        "options": ["Alternate interior angles", "Corresponding angles", "Interior angles on the same side of the transversal", "Vertically opposite angles"],
        "correct": 2,
        "solution": "Step 1: Alternate interior angles are equal.\nStep 2: Corresponding angles are equal.\nStep 3: Vertically opposite angles are equal.\nStep 4: Interior angles on the same side of the transversal sum to 180° (supplementary).\nConclusion: Interior angles on the same side of the transversal."
    },
    # Q28
    {
        "id": 28,
        "question": "If alternate interior angles are denoted by (5y - 15)° and (3y + 25)° across parallel lines, find the value of y.",
        "options": ["10°", "20°", "25°", "30°"],
        "correct": 1,
        "solution": "Step 1: Across parallel lines, alternate interior angles are equal.\nStep 2: 5y - 15 = 3y + 25 ➔ 5y - 3y = 25 + 15 ➔ 2y = 40 ➔ y = 20°.\n(Check: 5(20) - 15 = 85°, and 3(20) + 25 = 85°).\nConclusion: y = 20°."
    },
    # Q29
    {
        "id": 29,
        "question": "A transversal cuts two lines. If interior angles on the same side of the transversal sum to 176°, on which side will the lines intersect if extended?",
        "options": ["On the side where the angles sum to 176°", "On the opposite side where the angles sum to 184°", "They will never intersect", "They will intersect on both sides"],
        "correct": 0,
        "solution": "Step 1: Euclid's Fifth Postulate states: If a transversal falls on two lines making interior angles on one side less than two right angles (180°), the lines will intersect on THAT side.\nStep 2: 176° < 180°.\nConclusion: The lines will intersect on the side where the interior angles sum to 176°."
    },
    # Q30
    {
        "id": 30,
        "question": "In the letter 'H', the two vertical legs are parallel and the crossbar is perpendicular to both. What is the measure of each interior angle formed?",
        "options": ["45°", "60°", "90°", "180°"],
        "correct": 2,
        "solution": "Step 1: The crossbar acts as a perpendicular transversal to the two parallel vertical legs.\nStep 2: A perpendicular transversal forms right angles with both lines.\nConclusion: Every interior angle is exactly 90°."
    },

    # Q31
    {
        "id": 31,
        "question": "In the ruler and set square method for drawing parallel lines, what ensures that the drawn line is parallel to the original line?",
        "options": ["The length of the ruler", "The sliding of the set square along a fixed straight edge preserves equal corresponding angles", "The sharp point of the pencil", "The triangular shape of the set square"],
        "correct": 1,
        "solution": "Step 1: The straight ruler edge acts as a transversal line.\nStep 2: The set square's edge forms a fixed angle with the ruler.\nStep 3: Sliding the set square transfers this angle without rotation to the external point P, reproducing an equal corresponding angle.\nConclusion: Equal corresponding angles guarantee parallelism."
    },
    # Q32
    {
        "id": 32,
        "question": "Why do the horizontal mortar lines in the Café Wall illusion look tilted even though they are parallel?",
        "options": ["The lines are drawn with a ruler that was bent", "The alternating black-and-white staggered tiles trick the brain's edge-detecting neurons into perceiving local tilts", "The computer monitor is tilted", "The light in the room bends the image"],
        "correct": 1,
        "solution": "Step 1: The Café Wall illusion is a neurological visual phenomenon.\nStep 2: Luminance contrast between staggered black and white tiles triggers acute-angle expansion in the brain's visual cortex, creating perceived diagonal shifts.\nConclusion: The brain's edge-detection mechanism creates the illusion of tilt."
    },
    # Q33
    {
        "id": 33,
        "question": "In the Hering illusion, two straight parallel red lines look bowed outwards in the middle. What visual element causes this distortion?",
        "options": ["A checkerboard background", "A background of radial lines spreading out from a central point like bicycle spokes", "Wavy horizontal curves", "A dark border around the frame"],
        "correct": 1,
        "solution": "Step 1: The background in the Hering illusion consists of rays radiating outward from a central focal point.\nStep 2: Where these radial spokes cross the straight red lines, the brain overestimates the acute angles, pushing the perceived middle section outwards.\nConclusion: Radial spokes radiating from a central point."
    },
    # Q34
    {
        "id": 34,
        "question": "Two parallel lines l and m are intersected by transversal t. If ∠1 = (4x - 10)° and its vertically opposite angle is ∠3, while its corresponding angle is ∠5 = (3x + 15)°, find ∠1.",
        "options": ["25°", "65°", "90°", "115°"],
        "correct": 2,
        "solution": "Step 1: Since l ∥ m, corresponding angles are equal: ∠1 = ∠5.\nStep 2: 4x - 10 = 3x + 15 ➔ 4x - 3x = 15 + 10 ➔ x = 25°.\nStep 3: Calculate ∠1 = 4(25) - 10 = 100 - 10 = 90°.\n(Notice: when ∠1 = 90°, the transversal is perpendicular!).\nConclusion: ∠1 = 90°."
    },
    # Q35
    {
        "id": 35,
        "question": "In a zig-zag lightning bolt shape, line AB is parallel to line CD. A transversal from B meets an intermediate point E at 35°, and a transversal from D meets E at 45°. What is the measure of reflex or reflex-interior angle ∠BED?",
        "options": ["80°", "100°", "120°", "140°"],
        "correct": 0,
        "solution": "Step 1: Draw an auxiliary line EF through vertex E parallel to both AB and CD.\nStep 2: Angle ∠BEF and ∠ABE are alternate interior angles, so ∠BEF = 35°.\nStep 3: Angle ∠FED and ∠CDE are alternate interior angles, so ∠FED = 45°.\nStep 4: Total ∠BED = ∠BEF + ∠FED = 35° + 45° = 80°.\nConclusion: ∠BED = 80°."
    },
    # Q36
    {
        "id": 36,
        "question": "In the Zöllner illusion, parallel lines appear non-parallel. What pattern is drawn across the main lines to produce this effect?",
        "options": ["Concentric circles", "Short alternating diagonal hatch marks crossing the lines", "Spotted polka dots", "Black and white squares"],
        "correct": 1,
        "solution": "Step 1: In the Zöllner illusion, parallel main lines are crossed by short diagonal hatching segments.\nStep 2: The hatch lines alternate direction between adjacent parallel lines, making them appear to diverge and converge.\nConclusion: Short alternating diagonal hatch marks."
    },
    # Q37
    {
        "id": 37,
        "question": "In ancient Indian Sulba Sutra geometry, how did Baudhayana verify that an East-West cord and a North-South cord formed a true perpendicular (90°)?",
        "options": ["Using a plastic protractor", "By measuring with 3-4-5 cord lengths to form a right triangle (Baudhayana-Pythagorean triple)", "By looking at the clouds", "By counting strides"],
        "correct": 1,
        "solution": "Step 1: The Baudhayana Sulba Sutra explicitly defines cord lengths of 3, 4, and 5 units (and 5, 12, 13 units).\nStep 2: When stretched tightly into a triangle, the square of the longest cord equals the sum of squares of the other two (3² + 4² = 5²), creating a guaranteed 90° right angle.\nConclusion: Using 3-4-5 cord lengths to form a right triangle."
    },
    # Q38
    {
        "id": 38,
        "question": "Lines l and m are parallel. Transversal t intersects them. The bisectors of two interior angles on the same side of the transversal intersect at point X. What is the measure of the angle formed at point X?",
        "options": ["45°", "60°", "90°", "180°"],
        "correct": 2,
        "solution": "Step 1: Let the two co-interior angles be 2a and 2b. Since l ∥ m, 2a + 2b = 180° ➔ a + b = 90°.\nStep 2: The angle bisectors split these angles into 'a' and 'b'.\nStep 3: In the triangle formed by the bisectors and the transversal segment, the three angles sum to 180°: a + b + ∠X = 180°.\nStep 4: Since a + b = 90°, ∠X = 180° - 90° = 90°.\nConclusion: The bisectors of co-interior angles always meet at a right angle (90°)."
    },
    # Q39
    {
        "id": 39,
        "question": "If two parallel lines are intersected by a transversal, the angle bisectors of all four interior angles enclose a quadrilateral. What special type of quadrilateral is formed?",
        "options": ["Trapezium", "Parallelogram that is a Rectangle", "Kite", "Rhombus with no right angles"],
        "correct": 1,
        "solution": "Step 1: From Question 38, the adjacent bisectors meet at 90°.\nStep 2: The alternate angle bisectors are parallel because alternate interior angles are equal.\nStep 3: A parallelogram with all four interior angles equal to 90° is a rectangle!\nConclusion: The enclosed quadrilateral is always a Rectangle."
    },
    # Q40
    {
        "id": 40,
        "question": "A line segment AB is 6 cm long. How many distinct lines in the same plane can be drawn parallel to AB passing through a specific point P that lies 3 cm away from AB?",
        "options": ["Infinitely many lines", "Exactly two lines", "Exactly one unique line", "Zero lines"],
        "correct": 2,
        "solution": "Step 1: This is Playfair's Axiom (equivalent to Euclid's Fifth Postulate):\n'Given a straight line and a point not on it, there exists one and ONLY ONE line in the same plane that passes through the point and is parallel to the given line.'\nConclusion: Exactly one unique line."
    }
]

"""
Data module for Class 9 Mathematics Chapter 9: Triangles: Congruence Theorems
Syllabus Competencies: CG-4, C-4.1, C-7.3, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Structural Rigidity of Triangles vs. Quadrilaterals",
        "subtitle": "Kinematic Degrees of Freedom, 3-Bar vs 4-Bar Linkages & Practical Truss Engineering",
        "category": "Practical Applications",
        "badge": "CG-4 • C-4.1 • Structural Rigidity",
        "summary": "Why is a triangle the universal foundational shape of structural engineering? Consider a mechanical linkage made of rigid rods connected by frictionless pin joints. A 4-bar linkage (quadrilateral) has one kinematic degree of freedom: without altering the lengths of any of its four sides, its vertex angles can freely flex, causing it to deform and collapse into an oblique parallelogram. In sharp contrast, a 3-bar linkage (triangle) has zero internal degrees of freedom: fixing the lengths of the three sides strictly locks all three internal angles into place (by the SSS principle). Consequently, adding a single diagonal rod to a rectangular gate or shelf frame divides it into two interconnected triangles, instantly rendering the entire structure rigid and stable against shearing forces.",
        "key_points": [
            "Kinematic Rigidity: A 3-bar pinned linkage cannot change its angles without breaking or stretching its sides.",
            "Quadrilateral Flexibility: A 4-bar pinned linkage has 1 internal degree of freedom and easily shears under load.",
            "Diagonal Bracing: Adding a diagonal strut to a quadrilateral partitions it into two triangles, creating complete structural rigidity.",
            "Engineering Applications: Truss bridges (Warren, Pratt, Howe), construction cranes, roof rafters, bicycle diamond frames, and geodesic domes (Buckminster Fuller).",
            "Statics & Stability: Triangles distribute external compressive and tensile forces along axial lines directly into joints."
        ],
        "narration": "Welcome to Triangles: Congruence Theorems! Have you ever wondered why construction cranes, truss bridges, and bicycle frames are made of triangles rather than squares? If you pin four rods together into a quadrilateral, it easily wobbles and collapses under load. But pin three rods into a triangle, and it locks completely rigid! Let's explore how triangle rigidity forms the backbone of modern engineering.",
        "sim_title": "Linkage Rigidity Comparator (3-Bar vs. 4-Bar Linkage)",
        "checkpoints": [
            {
                "q": "Why is a hinged 3-bar triangular linkage mechanically rigid, while a 4-bar quadrilateral linkage deforms easily?",
                "options": [
                    "Triangles have stronger metal than quadrilaterals",
                    "Three fixed side lengths uniquely lock all three vertex angles (0 degrees of freedom)",
                    "A triangle has fewer joints, making it lighter",
                    "Gravity only acts on 4-sided shapes"
                ],
                "ans": 1,
                "exp": "By the SSS congruence principle, once the three side lengths of a triangle are fixed, all three vertex angles are uniquely determined. Hence, a 3-bar linkage has 0 degrees of freedom and cannot deform."
            },
            {
                "q": "How can a wobbly rectangular wooden gate or bookshelf frame be instantly made structurally rigid?",
                "options": [
                    "By painting it with weatherproof lacquer",
                    "By adding a diagonal brace rod that divides the rectangle into two triangles",
                    "By removing one of the vertical posts",
                    "By loosening the corner hinges"
                ],
                "ans": 1,
                "exp": "Installing a diagonal strut partitions the flexible 4-sided polygon into two interconnected triangles, locking the angles and transferring shear forces into axial tension/compression."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Concept of Congruence & Geometric Superposition",
        "subtitle": "Identical Shape and Size, Rigid Transformations (Isometries) & Euclid's Common Notion 4",
        "category": "Congruence Foundations",
        "badge": "CG-4 • C-4.1 • Congruence & Superposition",
        "summary": "In Euclidean geometry, two figures are defined to be Congruent (symbol: ≅) if they have exactly the same shape and the exact same size. The word congruence originates from the Latin 'congruere', meaning 'to come together or coincide'. Formally, two figures F₁ and F₂ are congruent if one can be superimposed onto the other through an isometry—a sequence of rigid motions (translation, rotation, and reflection) that preserves all distances and angles. This embodies Euclid's famous Common Notion 4: 'Things which coincide with one another are equal to one another.' Everyday examples include mass-produced machine parts, identical minted coins, sheets of paper from the same ream, and stamped industrial components.",
        "key_points": [
            "Definition of Congruence: Two figures are congruent (≅) if and only if they possess identical shape and identical size.",
            "Euclid's Common Notion 4: Things which coincide with one another (superposition) are equal to one another.",
            "Rigid Motions (Isometries): Translation (sliding), rotation (turning), and reflection (flipping) preserve distances and angles.",
            "Superposition Principle: If figure A can be picked up, moved without deformation, and placed over figure B such that every boundary coincides, then A ≅ B.",
            "Real-World Value: Interchangeability of parts in modern manufacturing and precision architectural blueprints."
        ],
        "narration": "What does it mean for two objects to be congruent? In everyday life, think of two identical coins or carbon copies. In geometry, two figures are congruent if they have both the exact same shape and the exact same size. If you can slide, turn, or flip one figure so it covers the other perfectly, they are congruent!",
        "sim_title": "Interactive Superposition & Rigid Transformation Lab",
        "checkpoints": [
            {
                "q": "Two plane geometric figures are congruent if and only if:",
                "options": [
                    "They have equal perimeter, regardless of shape",
                    "They have both the exact same shape and the exact same size",
                    "They have the same shape, but may differ in size",
                    "Their areas are proportional by a factor of 2"
                ],
                "ans": 1,
                "exp": "Congruence requires both identical shape (equal corresponding angles) and identical size (equal corresponding side lengths). Equal shape alone produces similarity, not congruence."
            },
            {
                "q": "Which set of geometric transformations preserves both side lengths and angle measures during superposition?",
                "options": [
                    "Dilations and perspective projections",
                    "Translations, rotations, and reflections (isometries)",
                    "Non-uniform horizontal scaling",
                    "Shear mappings"
                ],
                "ans": 1,
                "exp": "Translations, rotations, and reflections are isometric rigid motions that preserve all Euclidean distances and angle measures, making them the basis of superposition."
            }
        ]
    },
    {
        "id": 3,
        "title": "Correspondence of Vertices, Sides, Angles & CPCTC",
        "subtitle": "Bijection of Triangle Elements, Notation Sensitivity & The CPCTC Axiom",
        "category": "Correspondence & CPCTC",
        "badge": "CG-4 • C-4.1 • CPCTC",
        "summary": "When two triangles are congruent, there exists a unique one-to-one correspondence between their vertices, sides, and angles. If triangle ABC is congruent to triangle DEF under the vertex mapping A ↔ D, B ↔ E, and C ↔ F, this statement MUST be written strictly as △ABC ≅ △DEF. The order of the letters matters crucially: the first vertex corresponds to the first, the second to the second, and the third to the third! Writing △ABC ≅ △EDF is mathematically false if B corresponds to E and not D. Once congruence is established, we invoke the foundational principle CPCTC: 'Corresponding Parts of Congruent Triangles are Congruent'. This grants six simultaneous equality relations: AB = DE, BC = EF, CA = FD, and ∠A = ∠D, ∠B = ∠E, ∠C = ∠F.",
        "key_points": [
            "One-to-One Correspondence: Mapping of vertices A ↔ D, B ↔ E, C ↔ F governs all side and angle equalities.",
            "Strict Notation Order: △ABC ≅ △DEF explicitly asserts that AB corresponds to DE, BC to EF, and CA to FD.",
            "CPCTC Principle: Corresponding Parts of Congruent Triangles are Congruent.",
            "Six Equalities: Congruence between two triangles yields 3 pairs of equal sides and 3 pairs of equal angles.",
            "Common Error: Never scramble vertex order; writing △ABC ≅ △FED when A matches D asserts incorrect geometric relations."
        ],
        "narration": "In geometry, order is everything! When we write that triangle ABC is congruent to triangle DEF, we are making an exact statement about which vertices match: A corresponds to D, B corresponds to E, and C corresponds to F. From this correspondence, we get CPCTC: Corresponding Parts of Congruent Triangles are Congruent!",
        "sim_title": "Vertex Correspondence & CPCTC Mapper",
        "checkpoints": [
            {
                "q": "If △PQR ≅ △XYZ, which side of triangle XYZ corresponds to side PR?",
                "options": ["XY", "YZ", "XZ", "ZY"],
                "ans": 2,
                "exp": "In the notation △PQR ≅ △XYZ, P corresponds to X and R corresponds to Z. Therefore, segment PR corresponds to segment XZ."
            },
            {
                "q": "If △ABC ≅ △RPQ, which of the following angle equalities is guaranteed to be true by CPCTC?",
                "options": [
                    "∠A = ∠P",
                    "∠B = ∠P",
                    "∠B = ∠R",
                    "∠C = ∠R"
                ],
                "ans": 1,
                "exp": "Comparing corresponding positions in △ABC and △RPQ: first position A ↔ R, second position B ↔ P, third position C ↔ Q. Thus, ∠B = ∠P."
            }
        ]
    },
    {
        "id": 4,
        "title": "SAS Congruence Axiom (Side-Angle-Side)",
        "subtitle": "Axiom 7.1: Two Sides and the Included Angle & Why it is an Axiom",
        "category": "Congruence Criteria",
        "badge": "CG-4 • C-7.3 • SAS Axiom",
        "summary": "The Side-Angle-Side (SAS) Congruence Criterion (Axiom 7.1) states: 'Two triangles are congruent if two sides and the included angle of one triangle are equal to two sides and the included angle of the other triangle.' The word 'included' is critical: the angle must be the one formed between the two specified sides. For instance, in △ABC, the angle included between sides AB and AC is ∠A. If AB = DE, AC = DF, and ∠A = ∠D, then △ABC ≅ △DEF. In Euclidean geometry, SAS is accepted as an Axiom (a fundamental self-evident truth) because Euclid proved it using physical superposition (Proposition 4 of Book I), which relies on the intuitive notion of moving rigid bodies without deformation.",
        "key_points": [
            "Axiom 7.1 Statement: Two sides and the included angle of one triangle equal two sides and the included angle of another.",
            "Included Angle: The angle situated strictly between the two given sides (e.g., ∠A is included between AB and AC).",
            "Why an Axiom: Proven in Euclid's Elements via rigid superposition; in modern Hilbert axiomatics, it is taken as an axiom.",
            "Uniqueness of Third Side: Fixing lengths AB, AC and included angle ∠A uniquely determines the position of B and C, locking side BC.",
            "Non-Example: If the angle is not included (e.g. SSA), congruence is not guaranteed in general."
        ],
        "narration": "Our first congruence rule is the SAS Axiom: Side-Angle-Side. It says that if two sides and the included angle between them in one triangle equal two sides and the included angle in another triangle, the triangles are completely congruent! Notice the word included: the angle must sit right between the two sides.",
        "sim_title": "SAS Constructor & Superposition Visualizer",
        "checkpoints": [
            {
                "q": "In △ABC, which angle is the INCLUDED angle between sides BC and CA?",
                "options": ["∠A", "∠B", "∠C", "Both ∠A and ∠B"],
                "ans": 2,
                "exp": "Sides BC and CA share the common vertex C. Therefore, the angle formed between them is ∠C."
            },
            {
                "q": "Why is SAS classified as an Axiom in NCERT geometry rather than a derived Theorem?",
                "options": [
                    "Because it cannot be tested with a protractor",
                    "Because its proof relies on the intuitive concept of rigid superposition rather than prior axioms",
                    "Because it only applies to right-angled triangles",
                    "Because it was discovered before algebra was invented"
                ],
                "ans": 1,
                "exp": "SAS is accepted as an axiom because establishing it deductively requires the physical intuition of superimposing rigid bodies (Euclid's Proposition 4), which serves as the foundational starting point for deriving other theorems."
            }
        ]
    },
    {
        "id": 5,
        "title": "ASA Congruence Condition (Angle-Side-Angle) & Deductive Proof",
        "subtitle": "Theorem 7.1: Two Angles and the Included Side with Rigorous Deductive Proof",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • ASA Theorem",
        "summary": "Theorem 7.1 (ASA Congruence) states: 'Two triangles are congruent if two angles and the included side of one triangle are equal to two angles and the included side of the other triangle.' Let △ABC and △DEF have ∠B = ∠E, ∠C = ∠F, and included side BC = EF. The rigorous proof proceeds by examining three exhaustive cases regarding the sides AB and DE: Case 1: If AB = DE, then △ABC ≅ △DEF immediately by the SAS axiom. Case 2: If AB > DE, choose a point P on AB such that PB = DE. In △PBC and △DEF, PB = DE, BC = EF, and ∠B = ∠E, so △PBC ≅ △DEF by SAS. By CPCTC, ∠PCB = ∠F. But we are given ∠ACB = ∠F. This implies ∠PCB = ∠ACB, which means a proper part equals the whole—a logical contradiction! Hence AB cannot be greater than DE. Case 3: If AB < DE, an identical contradiction arises. Therefore, AB MUST equal DE, proving △ABC ≅ △DEF.",
        "key_points": [
            "Theorem 7.1 (ASA): Triangles with two equal angles and an equal included side are congruent.",
            "Included Side: The side connecting the vertices of the two given angles (e.g., BC connects ∠B and ∠C).",
            "Deductive Proof Strategy: Three-case analysis (AB = DE, AB > DE, AB < DE) using proof by contradiction.",
            "Contradiction Mechanism: Assuming AB > DE forces ray CP to coincide with ray CA, proving P must be A.",
            "Reduction to SAS: The proof cleverly constructs an auxiliary segment to reduce the problem to the SAS axiom."
        ],
        "narration": "Now for our first proven theorem: ASA Congruence! If two angles and the side included between them match, the triangles are congruent. The proof is a masterpiece of logic: it tests three cases—whether the side is equal, longer, or shorter. Assuming it is longer or shorter leads to an impossible contradiction where a part equals the whole!",
        "sim_title": "ASA 3-Case Deductive Proof Visualizer",
        "checkpoints": [
            {
                "q": "In the deductive proof of the ASA theorem, what impossible contradiction arises if we assume AB > DE?",
                "options": [
                    "The sum of angles exceeds 360°",
                    "A smaller sub-angle ∠PCB must equal the larger whole angle ∠ACB",
                    "The side BC becomes zero in length",
                    "The triangle becomes a quadrilateral"
                ],
                "ans": 1,
                "exp": "Assuming AB > DE leads to a point P on AB where CPCTC forces ∠PCB = ∠F = ∠ACB. A proper part of an angle cannot equal the whole angle, exposing a fatal contradiction."
            },
            {
                "q": "In △XYZ and △UVW, ∠X = ∠U and ∠Y = ∠V. Which side must be equal for ASA to apply directly?",
                "options": ["YZ = VW", "XY = UV", "XZ = UW", "XZ = VW"],
                "ans": 1,
                "exp": "The included side between angles ∠X and ∠Y is segment XY, and between ∠U and ∠V is UV. Thus, XY = UV is required for direct ASA."
            }
        ]
    },
    {
        "id": 6,
        "title": "AAS Congruence Condition (Angle-Angle-Side)",
        "subtitle": "Corollary to ASA via the Triangle Angle Sum Property (180° Sum)",
        "category": "Congruence Criteria",
        "badge": "CG-4 • C-7.3 • AAS Criterion",
        "summary": "The Angle-Angle-Side (AAS) Congruence Criterion states: 'Two triangles are congruent if any two angles and a non-included side of one triangle are equal to the corresponding two angles and side of the other triangle.' Unlike ASA, the equal side in AAS is NOT situated between the two given angles. Why is AAS unconditionally valid? By the Triangle Angle Sum Theorem, the sum of all three interior angles in any triangle is exactly 180°. If two angles of △ABC equal two angles of △DEF (say, ∠A = ∠D and ∠B = ∠E), then the third angle ∠C MUST equal ∠F because ∠C = 180° - (∠A + ∠B) = 180° - (∠D + ∠E) = ∠F. With the third angle equal, the non-included side now becomes an included side between ∠B and ∠C (or ∠A and ∠C), immediately converting AAS into ASA!",
        "key_points": [
            "AAS Statement: Congruence holds when two angles and any non-included side are equal in corresponding order.",
            "Angle Sum Link: In any triangle, ∠A + ∠B + ∠C = 180°; knowing two angles automatically fixes the third.",
            "Deductive Reduction: AAS is a direct mathematical corollary of ASA: ∠3 = 180° - (∠1 + ∠2).",
            "Correspondence Preservation: The given side must correspond in position relative to the equal angles (e.g., side opposite ∠A equals side opposite ∠D).",
            "Efficiency: In problem-solving, AAS saves students from explicitly calculating the third angle."
        ],
        "narration": "What if the equal side is NOT between the two angles? That gives us AAS: Angle-Angle-Side! Because the three angles of any triangle always add up to 180 degrees, if two angles match, the third angle is guaranteed to match as well. This instantly turns AAS into an ASA problem!",
        "sim_title": "AAS to ASA Dynamic Converter & Angle Sum Simulator",
        "checkpoints": [
            {
                "q": "Why is the AAS criterion mathematically valid even though the side is non-included?",
                "options": [
                    "Because all triangles can be turned into right triangles",
                    "Because the Angle Sum Property (180°) ensures the third angle must also be equal, reducing AAS to ASA",
                    "Because side lengths do not affect angles",
                    "Because circles can be inscribed in all triangles"
                ],
                "ans": 1,
                "exp": "Since ∠C = 180° - (∠A + ∠B), knowing two angles determines the third. The non-included side thereby becomes the included side between the known angle and the newly determined third angle."
            },
            {
                "q": "In △ABC, ∠A = 45°, ∠B = 65°, and BC = 8 cm. In △PQR, ∠P = 45°, ∠Q = 65°, and QR = 8 cm. By which criterion are they congruent?",
                "options": ["SAS", "AAS", "SSS", "RHS"],
                "ans": 1,
                "exp": "We are given two angles (∠A = ∠P, ∠B = ∠Q) and the side opposite ∠A (BC = QR = 8 cm), which is a non-included side. Thus, the triangles are congruent by AAS."
            }
        ]
    },
    {
        "id": 7,
        "title": "SSS Congruence Condition (Side-Side-Side)",
        "subtitle": "Theorem 7.4: Three Sides Equal & The Compass Arc Intersection Principle",
        "category": "Congruence Criteria",
        "badge": "CG-4 • C-4.1 • C-7.3 • SSS Theorem",
        "summary": "Theorem 7.4 (SSS Congruence) states: 'If three sides of one triangle are equal to three sides of another triangle, then the two triangles are congruent.' This theorem provides the geometric foundation for triangle rigidity. Geometrically, when we construct a triangle using a straightedge and compass with base BC, the location of vertex A is found by intersecting two circles: one centered at B with radius c = AB, and one centered at C with radius b = AC. In the half-plane above line BC, two circles can intersect at at most ONE point. Therefore, specifying the three side lengths (satisfying the triangle inequality) uniquely determines all three vertex positions, fixing every internal angle. In Euclid's proof, an auxiliary triangle is constructed below the base, forming two isosceles triangles whose base angles prove the vertex angles are equal.",
        "key_points": [
            "Theorem 7.4 (SSS): Equality of all three pairs of corresponding sides implies complete congruence.",
            "Compass Arc Uniqueness: Two intersecting circles in a plane intersect at at most two points (one in each half-plane).",
            "Rigidity Foundation: SSS proves why a 3-bar pinned linkage cannot flex—the three sides lock the angles completely.",
            "Euclid's Auxiliary Construction: Reflecting one triangle and connecting corresponding vertices generates isosceles base angles.",
            "Contrast with AAA: Three equal sides guarantee equal angles (SSS works), but three equal angles do NOT guarantee equal sides (AAA gives similarity, not congruence)."
        ],
        "narration": "Side-Side-Side, or SSS! If all three sides of one triangle equal all three sides of another, they are identical in every way. Think about drawing a triangle with a compass: once you draw the base and swing two arcs of given radii, they intersect at exactly one point. The sides completely dictate the angles!",
        "sim_title": "SSS Compass Arc Intersection & Rigidity Lab",
        "checkpoints": [
            {
                "q": "If two triangles have all three pairs of corresponding sides equal, what can be deduced about their corresponding angles?",
                "options": [
                    "They may differ by up to 10°",
                    "All corresponding angles are strictly equal by CPCTC",
                    "Only the largest angle is guaranteed to be equal",
                    "Their angle sums are proportional to side lengths"
                ],
                "ans": 1,
                "exp": "By the SSS congruence theorem, the two triangles are congruent, meaning all three pairs of corresponding angles are strictly equal by CPCTC."
            },
            {
                "q": "Why does SSS guarantee congruence, whereas AAA (Angle-Angle-Angle) does not?",
                "options": [
                    "Angles cannot be measured with a ruler",
                    "Equal angles preserve shape (similarity) but allow the size to scale up or down arbitrarily",
                    "Three angles always sum to 360°",
                    "AAA is only valid in spherical geometry"
                ],
                "ans": 1,
                "exp": "AAA guarantees identical shape (similarity), but the triangles can have completely different sizes (e.g. an equilateral triangle of side 1 cm vs side 10 cm). SSS fixes the physical size, ensuring congruence."
            }
        ]
    },
    {
        "id": 8,
        "title": "RHS Congruence Condition (Right Angle-Hypotenuse-Side)",
        "subtitle": "Theorem 7.5: Right-Angled Triangles & Connection to the Pythagorean Theorem",
        "category": "Congruence Criteria",
        "badge": "CG-4 • C-7.3 • RHS Theorem",
        "summary": "Theorem 7.5 (RHS Congruence) states: 'If in two right triangles, the hypotenuse and one side of one triangle are equal to the hypotenuse and one side of the other triangle, then the two triangles are congruent.' The acronym RHS stands specifically for Right angle, Hypotenuse, and Side. Notice that RHS is technically an instance of Side-Side-Angle (SSA), where the known angle is 90° and opposite the hypotenuse. Why is RHS always valid while general SSA is not? The answer lies in the Pythagorean Theorem: for any right triangle with hypotenuse h and leg b, the third leg a is uniquely determined by a = √(h² - b²). Because h and b are equal in both triangles, their third sides must also be equal! This instantly converts RHS into an SSS congruence. In classical geometry, it is proven by placing the two right triangles back-to-back along the common leg to create a larger isosceles triangle.",
        "key_points": [
            "Theorem 7.5 (RHS): Hypotenuse and one leg equal in right-angled triangles guarantees congruence.",
            "RHS Decoded: R = Right angle (90°), H = Hypotenuse (side opposite 90°), S = Any one of the remaining two legs.",
            "Pythagorean Connection: Third leg a = √(h² - b²) is uniquely locked, reducing RHS directly to SSS.",
            "Back-to-Back Proof: Placing two triangles along equal leg forms an isosceles triangle whose base angles prove congruence.",
            "Special Case of SSA: RHS succeeds because the 90° angle forces the swinging leg to be tangent to the base ray."
        ],
        "narration": "Next up is RHS: Right angle, Hypotenuse, and Side! When two right-angled triangles share the same hypotenuse length and one matching leg, they are congruent. Why does this work? By the Pythagorean theorem, the third side is locked by square root of h-squared minus b-squared. There is no wiggle room!",
        "sim_title": "RHS Pythagorean Lock & Back-to-Back Isosceles Visualizer",
        "checkpoints": [
            {
                "q": "In right triangles △ABC and △PQR, ∠B = ∠Q = 90°, AC = PR = 13 cm, and AB = PQ = 5 cm. By which theorem are they congruent?",
                "options": ["SAS", "ASA", "RHS", "AAS"],
                "ans": 2,
                "exp": "Both triangles have a right angle, equal hypotenuses (AC = PR = 13 cm), and one equal leg (AB = PQ = 5 cm). Thus, they are congruent by RHS."
            },
            {
                "q": "How does the Pythagorean Theorem prove that the RHS condition always yields congruence?",
                "options": [
                    "It shows that the sum of the angles is 180°",
                    "It proves that the unmeasured third side must equal √(hypotenuse² - leg²), which matches in both triangles (reducing to SSS)",
                    "It doubles the area of both triangles",
                    "It eliminates the right angle"
                ],
                "ans": 1,
                "exp": "By Pythagoras, the third side of both triangles is uniquely determined as √(h² - b²). Since h and b are identical, the third sides are equal, proving congruence by SSS."
            }
        ]
    },
    {
        "id": 9,
        "title": "Isosceles Triangle Properties: Pons Asinorum & Converse",
        "subtitle": "Theorems 7.2 & 7.3: Equal Sides Subtend Equal Angles & The Angle Bisector Proof",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Isosceles Theorems",
        "summary": "An isosceles triangle has at least two equal sides. Theorem 7.2 states: 'Angles opposite to equal sides of an isosceles triangle are equal.' Historically known as the 'Pons Asinorum' (Bridge of Asses) in Euclid's Elements (Proposition 5), this theorem is proven elegantly: in △ABC with AB = AC, draw the angle bisector of ∠A meeting base BC at point D. In △ABD and △ACD: AB = AC (given), ∠BAD = ∠CAD (AD is bisector), and AD = AD (common). Therefore, △ABD ≅ △ACD by the SAS axiom! By CPCTC, ∠B = ∠C. Furthermore, CPCTC gives BD = CD (AD is a median) and ∠ADB = ∠ADC = 90° (AD is perpendicular to BC). Theorem 7.3 is the Converse: 'The sides opposite to equal angles of a triangle are equal.' If ∠B = ∠C, drawing perpendicular AD proves △ABD ≅ △ACD by AAS, yielding AB = AC by CPCTC.",
        "key_points": [
            "Theorem 7.2: In an isosceles triangle, sides AB = AC implies base angles ∠B = ∠C.",
            "Pons Asinorum: Latin for 'Bridge of Asses', Euclid's classical hurdle in geometric deduction.",
            "Angle Bisector Proof: Constructing angle bisector AD splits △ABC into two congruent triangles by SAS.",
            "Triple Role of AD: In an isosceles triangle, the angle bisector from vertex A is ALSO the median and altitude to base BC.",
            "Theorem 7.3 (Converse): If base angles ∠B = ∠C, then sides AB = AC (proven via AAS)."
        ],
        "narration": "An isosceles triangle has two equal sides. Theorem 7.2 tells us that the angles opposite those equal sides are also equal! This famous result was called the Pons Asinorum, or Bridge of Asses. If you fold the triangle right down the middle along the vertex angle bisector, the two halves match like mirror images!",
        "sim_title": "Pons Asinorum Folding Symmetry & Bisector Proof Lab",
        "checkpoints": [
            {
                "q": "In △ABC, AB = AC and vertex angle ∠A = 50°. What is the measure of base angle ∠B?",
                "options": ["50°", "65°", "75°", "130°"],
                "ans": 1,
                "exp": "Since AB = AC, base angles ∠B = ∠C. The angle sum is 180°: ∠B + ∠C = 180° - 50° = 130°. Therefore, ∠B = 130° / 2 = 65°."
            },
            {
                "q": "In an isosceles triangle △ABC with AB = AC, the line segment drawn from vertex A perpendicular to BC also:",
                "options": [
                    "Triples the base length",
                    "Bisects both the base BC (median) and the vertex angle ∠A (angle bisector)",
                    "Forms an equilateral triangle",
                    "Passes outside the triangle"
                ],
                "ans": 1,
                "exp": "Due to the reflective symmetry and congruence △ABD ≅ △ACD, the altitude from vertex A simultaneously bisects the base BC (BD = CD) and bisects vertex angle ∠A."
            }
        ]
    },
    {
        "id": 10,
        "title": "Propositions & Conditional Statements in Geometry",
        "subtitle": "The Structure of Mathematical Logic: Hypotheses, Conclusions & Truth Values",
        "category": "Mathematical Logic",
        "badge": "CG-4 • C-7.3 • Mathematical Logic",
        "summary": "In mathematics, a Proposition (or statement) is a declarative sentence that is either definitively True or definitively False, but never both or ambiguous. Opinions or questions ('Triangles are pretty') are not propositions. Most geometric theorems are formulated as Conditional Propositions in the standard format: 'If P, then Q', symbolized as P ⇒ Q. Here, P is the Hypothesis (or Antecedent)—the condition assumed to be given—and Q is the Conclusion (or Consequent)—the result that necessarily follows. For example: 'If a triangle has three equal sides (P), then it has three equal angles (Q)'. In Euclidean geometry, a conditional proposition P ⇒ Q is mathematically true if, whenever hypothesis P is satisfied, conclusion Q is guaranteed to follow by deductive proof.",
        "key_points": [
            "Mathematical Proposition: A declarative sentence with an unambiguous truth value (strictly True or strictly False).",
            "Conditional Statement: Formulated as 'If P, then Q' (symbolized P ⇒ Q).",
            "Hypothesis (P): The assumed given premise or condition.",
            "Conclusion (Q): The logical consequence deduced from the hypothesis.",
            "Deductive Chain: Axioms + Definitions + Logic ⇒ Proven Propositions (Theorems).",
            "Euler Diagram: P ⇒ Q means the set of objects satisfying P is a subset of those satisfying Q (P ⊆ Q)."
        ],
        "narration": "To master geometric proofs, we need the language of mathematical logic! A proposition is a clear statement that is either true or false. Most geometric rules are conditional statements: If P happens, then Q must follow. P is the hypothesis, what we are given; Q is the conclusion, what we prove!",
        "sim_title": "Proposition Builder & Truth Value Tester",
        "checkpoints": [
            {
                "q": "Which of the following is a valid mathematical proposition?",
                "options": [
                    "Why do triangles have three sides?",
                    "Every equilateral triangle is equiangular.",
                    "Drawing circles is more fun than drawing lines.",
                    "Let x be a big number."
                ],
                "ans": 1,
                "exp": "'Every equilateral triangle is equiangular' is a definitive declarative statement with an objective truth value (it is True), making it a mathematical proposition."
            },
            {
                "q": "In the conditional theorem 'If a quadrilateral is a rectangle, then its diagonals are equal', what is the hypothesis P?",
                "options": [
                    "Its diagonals are equal",
                    "A quadrilateral is a rectangle",
                    "All quadrilaterals have 4 sides",
                    "Diagonals bisect each other at right angles"
                ],
                "ans": 1,
                "exp": "The hypothesis P is the condition following 'If', which is 'A quadrilateral is a rectangle'."
            }
        ]
    },
    {
        "id": 11,
        "title": "The Converse of a Proposition (Q ⇒ P)",
        "subtitle": "Swapping Hypothesis and Conclusion, Theorem-Converse Pairs & Biconditionals",
        "category": "Mathematical Logic",
        "badge": "CG-4 • C-7.3 • Converse of Proposition",
        "summary": "Given any conditional proposition 'If P, then Q' (P ⇒ Q), its Converse is formed by directly swapping the hypothesis and the conclusion: 'If Q, then P' (Q ⇒ P). For example: Original Statement: 'If a triangle is equilateral (P), then all its angles are 60° (Q).' Converse: 'If all angles of a triangle are 60° (Q), then the triangle is equilateral (P).' In this case, both the original statement and its converse are true! When both P ⇒ Q and Q ⇒ P are simultaneously true, they combine into a powerful Biconditional Statement: 'P if and only if Q' (symbolized P ⇔ Q). Geometric theorems and their converses often come in celebrated pairs, such as the Linear Pair Axiom and its converse, and the Isosceles Triangle Theorem and its converse.",
        "key_points": [
            "Converse Definition: The converse of 'If P, then Q' is the reversed statement 'If Q, then P'.",
            "Swapping Roles: The original conclusion becomes the new hypothesis; the original hypothesis becomes the new conclusion.",
            "Biconditional Statement: If both statement and converse are true, we write 'P if and only if Q' (P ⇔ Q).",
            "Famous True Converse Pair: Theorem 7.2 (Equal sides ⇒ Equal angles) and Theorem 7.3 (Equal angles ⇒ Equal sides).",
            "Caution: Never assume a converse is true automatically; it requires an independent mathematical proof!"
        ],
        "narration": "What happens if you turn a statement backwards? That is its converse! If the original rule says 'If P, then Q', the converse says 'If Q, then P'. In some wonderful cases, like isosceles triangles, both the statement and its converse are true, giving us an 'if and only if' rule!",
        "sim_title": "Converse Swapper Machine & Biconditional Validator",
        "checkpoints": [
            {
                "q": "What is the converse of the proposition: 'If two lines are parallel, then alternate interior angles are equal'?",
                "options": [
                    "If two lines are not parallel, then alternate interior angles are not equal",
                    "If alternate interior angles are equal, then the two lines are parallel",
                    "If corresponding angles are equal, then lines are parallel",
                    "If two lines intersect, they form vertically opposite angles"
                ],
                "ans": 1,
                "exp": "Swapping hypothesis ('two lines are parallel') and conclusion ('alternate interior angles are equal') yields: 'If alternate interior angles are equal, then the two lines are parallel'."
            },
            {
                "q": "When a mathematical theorem P ⇒ Q and its converse Q ⇒ P are both proven to be true, they form a:",
                "options": [
                    "Contradiction",
                    "Biconditional statement ('P if and only if Q')",
                    "Postulate without proof",
                    "Counterexample"
                ],
                "ans": 1,
                "exp": "When both implications hold in both directions, the relationship is equivalence or biconditional, denoted P ⇔ Q ('P if and only if Q')."
            }
        ]
    },
    {
        "id": 12,
        "title": "Why Converses Are Not Always True & Counterexamples",
        "subtitle": "Logical Asymmetry, Necessary vs Sufficient Conditions & The Power of a Single Counterexample",
        "category": "Mathematical Logic",
        "badge": "CG-4 • C-7.3 • Counterexamples",
        "summary": "One of the most dangerous logical fallacies in mathematics is assuming that because a statement is true, its converse must also be true! This is demonstrably false: truth in one direction does NOT imply truth in reverse. To prove a universal proposition false, one does not need a thousand arguments—a single valid Counterexample is sufficient to shatter it. Consider these classic geometric examples: 1. Statement: 'If a shape is a square, then it has 4 right angles' (TRUE). Converse: 'If a shape has 4 right angles, then it is a square' (FALSE! Counterexample: A non-square rectangle has 4 right angles, but unequal sides). 2. Statement: 'If two triangles are congruent, then they have equal areas' (TRUE). Converse: 'If two triangles have equal areas, then they are congruent' (FALSE! Counterexample: A triangle with base 4 and height 3 has area 6; a triangle with base 6 and height 2 also has area 6, but they are not congruent!).",
        "key_points": [
            "Logical Fallacy: Assuming P ⇒ Q implies Q ⇒ P is called the fallacy of affirming the consequent.",
            "Counterexample: A single specific instance where the hypothesis is satisfied but the conclusion fails, disproving the converse.",
            "Rectangle Counterexample: Having 4 right angles does not make a quadrilateral a square.",
            "Area Counterexample: Equal areas do NOT guarantee congruent triangles; base and height can vary inversely.",
            "Vertically Opposite Angle Counterexample: Two equal 40° angles do not need to be vertically opposite.",
            "Sufficient vs Necessary: P being sufficient for Q does not mean Q is sufficient for P."
        ],
        "narration": "Here is a golden rule of mathematical logic: just because a statement is true, does NOT mean its converse is true! For example, every square is a rectangle, but is every rectangle a square? Absolutely not! A rectangle with sides 2 and 5 has four right angles but is not a square. That single counterexample disproves the converse!",
        "sim_title": "Counterexample Generator & Converse Refuter",
        "checkpoints": [
            {
                "q": "The statement 'If two triangles are congruent, then they have equal area' is true. Is its converse true?",
                "options": [
                    "Yes, equal area always guarantees identical side lengths",
                    "No, triangles with completely different dimensions can have the exact same area (counterexample)",
                    "Yes, by the SSS theorem",
                    "Only if both triangles are equilateral"
                ],
                "ans": 1,
                "exp": "The converse is false. A triangle of base 8 cm and height 3 cm has area 12 cm², and a triangle of base 6 cm and height 4 cm also has area 12 cm², yet they are not congruent."
            },
            {
                "q": "What is the mathematical role of a 'counterexample' in geometry?",
                "options": [
                    "To prove that all theorems in a chapter are correct",
                    "To definitively disprove a general claim or false converse by providing a single contradictory case",
                    "To calculate the area of an irregular polygon",
                    "To construct parallel lines using a compass"
                ],
                "ans": 1,
                "exp": "A single counterexample is mathematically sufficient to disprove any universal proposition by showing a case where the hypothesis holds but the conclusion fails."
            }
        ]
    },
    {
        "id": 13,
        "title": "Why SSA is NOT in General a Valid Congruence Criterion",
        "subtitle": "The Ambiguous Case: The Swinging Pendulum & Two Non-Congruent Triangles",
        "category": "The Ambiguous Case",
        "badge": "CG-4 • C-7.3 • SSA Ambiguous Case",
        "summary": "Why is there no 'SSA' (Side-Side-Angle) congruence theorem? When two sides and a non-included angle are given, it is known historically as the Ambiguous Case. Consider fixing acute angle A and adjacent side b = AC. From vertex C, let a side of length a = BC hang like a swinging pendulum toward the horizontal base ray extending from A. The perpendicular altitude from C to the base ray has length h = b · sin(A). If a < h, side a cannot even reach the base ray—no triangle exists! If a = h, exactly one right triangle is formed (this is RHS). But if h < a < b (the swinging side is longer than the altitude but shorter than adjacent side b), the swinging pendulum cuts the base ray at TWO distinct points, B₁ and B₂! This creates two completely different, non-congruent triangles: acute △AB₁C and obtuse △AB₂C, both sharing identical side lengths b, a and angle A!",
        "key_points": [
            "The Ambiguous Case: SSA gives two sides and a non-included angle, failing to guarantee uniqueness.",
            "Altitude Threshold: The critical altitude from vertex C to base ray is h = b · sin(A).",
            "Double Intersection: When h < a < b, the swinging arm intersects the base ray at two distinct locations B₁ and B₂.",
            "Two Non-Congruent Triangles: One triangle is acute (△AB₁C) and the other is obtuse (△AB₂C) with equal SSA data.",
            "Why it Fails: Congruence requires a unique triangle shape; having two possible shapes invalidates SSA as a general theorem."
        ],
        "narration": "Why don't we have an SSA congruence rule? Imagine swinging a rod of length 'a' from the top vertex. If that rod is shorter than the adjacent side but longer than the height, it can swing inside or swing outside, hitting the base line in TWO different places! This creates two totally different triangles with the exact same two sides and angle!",
        "sim_title": "The SSA Swinging Pendulum Simulator (Ambiguous Case)",
        "checkpoints": [
            {
                "q": "Why does Side-Side-Angle (SSA) fail as a general congruence criterion for triangles?",
                "options": [
                    "Because protractors cannot measure angles when two sides are given",
                    "Because it can produce two distinct, non-congruent triangles (one acute, one obtuse) from identical given data",
                    "Because side lengths cannot be compared to angles",
                    "Because SSA only works for squares"
                ],
                "ans": 1,
                "exp": "In the ambiguous range (b sin A < a < b), the swinging side intersects the base ray at two different points, producing two non-congruent triangles (the Ambiguous Case)."
            },
            {
                "q": "In △ABC, given angle A = 30° and adjacent side b = 10 cm. What is the perpendicular altitude h to the base line?",
                "options": ["10 cm", "5 cm", "8.66 cm", "2.5 cm"],
                "ans": 1,
                "exp": "The altitude is h = b · sin(A) = 10 · sin(30°) = 10 · 0.5 = 5 cm. Any opposite side a between 5 cm and 10 cm creates two distinct triangles!"
            }
        ]
    },
    {
        "id": 14,
        "title": "When SSA IS a Valid Congruence Condition (Special Cases)",
        "subtitle": "Right Angles (RHS), Opposite Side ≥ Adjacent Side (a ≥ b) & Unique Geometry",
        "category": "The Ambiguous Case",
        "badge": "CG-4 • C-7.3 • Valid SSA Situations",
        "summary": "Although SSA is not universally valid, there are specific, well-defined mathematical situations where SSA DOES uniquely determine a triangle and therefore guarantees congruence! Case 1: Right Angle (RHS): If the non-included angle is 90°, the swinging arm is perpendicular to the base, producing exactly one unique right triangle. Case 2: Tangency (a = h = b · sin A): The swinging arm just touches the base line at a single tangent point, forming a unique right triangle. Case 3: Longest Side (a ≥ b): If the side opposite the given angle is greater than or equal to the adjacent side, the swinging circle can only intersect the positive base ray once! The second circle intersection falls on the negative backward ray behind vertex A, which cannot form a geometric triangle. Case 4: Obtuse Angle (A > 90° with a > b): A triangle can only have at most one obtuse angle, forcing the second intersection to be discarded.",
        "key_points": [
            "Condition 1 (Right Angle): When angle A = 90°, SSA becomes the RHS theorem and is 100% valid.",
            "Condition 2 (Tangency): When a = b · sin A, only one unique right triangle is formed.",
            "Condition 3 (a ≥ b with Acute A): When the opposite side is greater than or equal to the adjacent side, only one intersection lies on the forward ray.",
            "Condition 4 (Obtuse A with a > b): When angle A is obtuse, only one triangle is physically possible.",
            "Geometric Principle: SSA is valid whenever the algebraic equation for the third side has exactly one positive real root."
        ],
        "narration": "So when DOES SSA actually work? There are three wonderful exceptions! First, when the angle is 90 degrees, which is our familiar RHS rule. Second, when the opposite side is longer than the adjacent side: the swinging arm swings past the vertex, leaving only one possible triangle on the positive ray!",
        "sim_title": "SSA Parameter Space & Uniqueness Zone Explorer",
        "checkpoints": [
            {
                "q": "Under which condition does SSA guarantee a unique triangle (and thus congruence) when angle A is acute?",
                "options": [
                    "When the opposite side is shorter than the altitude (a < h)",
                    "When the opposite side is greater than or equal to the adjacent side (a ≥ b)",
                    "When all three angles are acute",
                    "When side b is three times side a"
                ],
                "ans": 1,
                "exp": "When a ≥ b, the circle centered at C intersects the forward ray from A at exactly one point; the other intersection lies backwards on the negative ray, guaranteeing a unique triangle."
            },
            {
                "q": "If angle A = 90°, hypotenuse a = 13 cm, and leg b = 12 cm, why does SSA yield a unique congruent triangle?",
                "options": [
                    "Because it is the RHS condition, where Pythagoras locks the third side to √(13² - 12²) = 5 cm",
                    "Because 90° angles cannot be bisected",
                    "Because 13 is a prime number",
                    "Because SSA always works for odd numbers"
                ],
                "ans": 0,
                "exp": "When the non-included angle is 90°, SSA is precisely the RHS criterion, where the Pythagorean theorem uniquely locks the third side, eliminating all ambiguity."
            }
        ]
    },
    {
        "id": 15,
        "title": "The Role & Danger of Diagram Accuracy in Geometry",
        "subtitle": "Visual Deceptions, The Fallacy of Lewis Carroll & The Need for Deductive Rigor",
        "category": "Deductive Rigor",
        "badge": "CG-4 • C-7.3 • Diagram Accuracy & Fallacies",
        "summary": "In geometry, diagrams are powerful cognitive aids to guide our intuition, but they are NOT proofs! Relying on diagram appearance rather than rigorous deduction is one of the most famous traps in mathematics. The most celebrated demonstration of this danger is the classic Fallacy of Lewis Carroll (and W. W. Rouse Ball): 'A deductive proof that all triangles are isosceles!' In this fallacy, one draws a scalene triangle ABC, constructs the angle bisector of ∠A and the perpendicular bisector of base BC, and assumes their intersection point O lies inside the triangle. By establishing a series of seemingly flawless SAS and RHS triangle congruences, one 'proves' that AB = AC! Where is the fatal error? An accurate compass-and-ruler construction reveals that point O NEVER lies inside a scalene triangle—it always lies outside on the circumcircle! The false proof relied entirely on an inaccurate hand-drawn diagram.",
        "key_points": [
            "Diagrams as Heuristics: Diagrams assist visualization but possess zero deductive authority in a proof.",
            "Diagram Deceit: A slightly misplaced point or misdrawn line can visually hide logical contradictions.",
            "The 'All Triangles are Isosceles' Fallacy: A famous fake proof that exploits assuming an external intersection point lies inside.",
            "Axiomatic Independence: Every geometric assertion must be justified by an axiom, definition, or previously proven theorem, NEVER by 'it looks that way'.",
            "Collinearity and Betweenness: David Hilbert introduced explicit axioms of 'Betweenness' to fix Euclid's implicit reliance on diagram appearance."
        ],
        "narration": "Can your eyes deceive you in geometry? Absolutely! In mathematics, a diagram is just a sketch to help you think—it is never proof. In fact, mathematician Lewis Carroll showed that if you draw a slightly inaccurate diagram, you can 'prove' that every triangle in the world is isosceles! Always trust deductive logic over visual sketches.",
        "sim_title": "Lewis Carroll's Fallacy & Accurate Construction Inspector",
        "checkpoints": [
            {
                "q": "Why can a geometric theorem never be proven solely by visual inspection of a hand-drawn diagram?",
                "options": [
                    "Because diagrams cannot be drawn with colored pens",
                    "Hand-drawn diagrams can contain subtle inaccuracies of point placement and betweenness that mask false assumptions",
                    "Because Euclidean geometry forbids rulers",
                    "Because angles change when paper is rotated"
                ],
                "ans": 1,
                "exp": "A sketch can deceive the eye regarding collinearity, betweenness, or whether an intersection lies inside or outside a polygon, leading to false conclusions like Carroll's fallacy."
            },
            {
                "q": "In the famous geometric fallacy 'proving all triangles are isosceles', what was the hidden false assumption?",
                "options": [
                    "Assuming the sum of angles in a triangle is 180°",
                    "Assuming the intersection of the angle bisector and perpendicular bisector lies inside the triangle, when it actually lies outside on the circumcircle",
                    "Using the Pythagorean theorem backwards",
                    "Assuming right angles equal 90°"
                ],
                "ans": 1,
                "exp": "The entire false proof hinges on drawing point O inside the triangle. In an accurate construction, O lies strictly outside the triangle on its circumcircle, invalidating the segment additions."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Congruence Engine & Truss Solvers",
        "subtitle": "Algorithmic Decision Trees, Laman's Theorem & Planar Pin-Jointed Statics (m = 2j - 3)",
        "category": "Computational Thinking",
        "badge": "CG-4 • C-4.1 • C-7.3 • CG-9 • Computational Thinking",
        "summary": "How do modern CAD software and structural engineering simulations apply triangle congruence and rigidity? 1. Congruence Decision Algorithm: Given any three measurements of two triangles, an automated inference engine executes a deterministic decision tree: If 3 sides known → check triangle inequality, return SSS. If 2 sides + included angle → return SAS. If 2 angles + side → return ASA/AAS. If 2 sides + non-included angle → test if angle = 90° (RHS) or opposite side ≥ adjacent side (Unique SSA), else flag Ambiguous SSA! If 3 angles → return Similar (Not Congruent). 2. Graph Theory & Planar Truss Rigidity (Laman's Theorem & Maxwell's Rule): In a 2D pin-jointed framework with j joints and m member bars, minimal structural rigidity requires m = 2j - 3. If m < 2j - 3, the structure has internal mechanisms and will collapse; if m = 2j - 3 with triangular subgraphs, it is a statically determinate rigid truss!",
        "key_points": [
            "Automated Congruence Pipeline: Decision tree branching based on element combinations (SSS, SAS, ASA, AAS, RHS, Ambiguous SSA, AAA).",
            "Pattern Recognition & Validation: Pre-checking metric constraints (Triangle Inequality: a + b > c).",
            "Planar Truss Formula: Maxwell's rigidity rule for pinned trusses: m = 2j - 3 (m = members, j = joints).",
            "Kinematic Under-constraint (m < 2j - 3): Unstable framework that deforms under shear loads.",
            "Statically Determinate Truss (m = 2j - 3): Minimally rigid framework composed of interconnected triangles.",
            "CAD Integration: Finite Element Analysis (FEA) meshes complex 3D surfaces into interconnected triangles for stress calculation."
        ],
        "narration": "Let's bring it all together with Computational Thinking! How does computer software verify triangle congruence and structural safety? We can write an algorithm that checks the given pieces step-by-step: SSS, SAS, ASA, AAS, or RHS! And for structural engineers, Maxwell's formula m = 2j - 3 uses triangles to calculate whether a giant bridge will stand rigid under heavy traffic!",
        "sim_title": "Algorithmic Congruence Decision Tree & Truss Rigidity Solver",
        "checkpoints": [
            {
                "q": "What does an automated geometric inference engine output when provided with three equal corresponding angles (AAA) for two triangles?",
                "options": [
                    "The triangles are congruent by AAA",
                    "The triangles are similar in shape, but congruence cannot be determined without at least one corresponding side length",
                    "The triangles have equal perimeter",
                    "Error: Three angles cannot be measured together"
                ],
                "ans": 1,
                "exp": "AAA guarantees similarity (same shape and angle proportions), but cannot determine congruence because the scale factor between side lengths is unknown."
            },
            {
                "q": "According to Maxwell's formula for planar pin-jointed trusses (m = 2j - 3), how many member bars m are required to make a framework with j = 6 pin joints minimally rigid?",
                "options": [
                    "m = 6 bars",
                    "m = 9 bars",
                    "m = 12 bars",
                    "m = 15 bars"
                ],
                "ans": 1,
                "exp": "Using m = 2j - 3 with j = 6 joints: m = 2(6) - 3 = 12 - 3 = 9 member bars arranged in triangular cells."
            }
        ]
    }
]

QUIZZES = [
    {
        "slide_id": 17,
        "title": "Mastery Quiz 1: Congruence Criteria & CPCTC",
        "subtitle": "SAS, ASA, AAS, SSS, RHS & Vertex Correspondence Precision",
        "category": "Mastery Challenge",
        "badge": "Quiz 1 • Congruence Criteria",
        "questions": [
            {
                "q": "If △ABC ≅ △FDE, which of the following statements is FALSE?",
                "options": ["AB = FD", "BC = DE", "AC = FE", "∠B = ∠F"],
                "ans": 3,
                "exp": "From the correspondence △ABC ≅ △FDE: A ↔ F, B ↔ D, C ↔ E. Thus, ∠B corresponds to ∠D, NOT ∠F. Statement ∠B = ∠F is false."
            },
            {
                "q": "In △PQR, PQ = 6 cm, PR = 8 cm, and ∠P = 70°. In △XYZ, XY = 6 cm, XZ = 8 cm, and ∠X = 70°. By which criterion are they congruent?",
                "options": ["SSS", "SAS", "ASA", "RHS"],
                "ans": 1,
                "exp": "Two pairs of sides are equal (PQ = XY = 6, PR = XZ = 8) and the included angle formed between them is equal (∠P = ∠X = 70°). Hence, congruent by SAS."
            },
            {
                "q": "In △ABC and △DEF, ∠A = ∠D = 55°, ∠B = ∠E = 65°, and AC = DF = 9 cm. By which criterion are the triangles congruent?",
                "options": ["SAS", "ASA", "AAS", "SSS"],
                "ans": 2,
                "exp": "Two angles are equal (∠A = ∠D, ∠B = ∠E) and a non-included side is equal (AC = DF = 9 cm, opposite ∠B and ∠E). Thus, congruent by AAS."
            },
            {
                "q": "Two right-angled triangles △ABC and △PQR have ∠B = ∠Q = 90°. If AC = PR = 15 cm and BC = QR = 9 cm, by which condition are they congruent?",
                "options": ["SAS", "ASA", "RHS", "SSS"],
                "ans": 2,
                "exp": "Both triangles are right-angled, share equal hypotenuses (AC = PR = 15 cm), and have one equal leg (BC = QR = 9 cm). Thus, congruent by RHS."
            },
            {
                "q": "If all three sides of △ABC equal the three corresponding sides of △DEF, what guarantees that ∠A = ∠D?",
                "options": ["Angle Sum Theorem", "CPCTC following SSS Congruence", "Pythagorean Theorem", "Linear Pair Axiom"],
                "ans": 1,
                "exp": "By SSS, △ABC ≅ △DEF. Once congruence is established, all corresponding angles are equal by CPCTC (Corresponding Parts of Congruent Triangles are Congruent)."
            },
            {
                "q": "In △LMN, LM = LN. A line segment LP is drawn perpendicular to MN, with P on MN. By which condition are △LPM and △LPN congruent?",
                "options": ["RHS (or SAS)", "AAA", "SSA", "None"],
                "ans": 0,
                "exp": "In right-angled △LPM and △LPN: ∠LPM = ∠LPN = 90°, hypotenuses LM = LN (given), and leg LP = LP (common). They are congruent by RHS."
            },
            {
                "q": "Which of the following combinations of triangle elements does NOT guarantee congruence in general?",
                "options": ["Side-Angle-Side (SAS)", "Side-Side-Side (SSS)", "Side-Side-Angle (SSA)", "Angle-Side-Angle (ASA)"],
                "ans": 2,
                "exp": "SSA (Side-Side-Angle) can produce two different triangles (the Ambiguous Case), failing to guarantee congruence in general."
            },
            {
                "q": "If △ABC ≅ △PQR and the perimeter of △ABC is 36 cm, what is the perimeter of △PQR?",
                "options": ["18 cm", "36 cm", "72 cm", "Cannot be determined"],
                "ans": 1,
                "exp": "Congruent triangles have identical corresponding side lengths (AB = PQ, BC = QR, CA = RP). Therefore, their perimeters are strictly identical (36 cm)."
            },
            {
                "q": "In △ABC and △DEF, AB = DE and BC = EF. Which additional piece of information is needed to prove congruence by SAS?",
                "options": ["∠A = ∠D", "∠B = ∠E", "∠C = ∠F", "AC = DF"],
                "ans": 1,
                "exp": "The included angle between sides AB and BC is ∠B, and between DE and EF is ∠E. Therefore, ∠B = ∠E is needed for SAS."
            },
            {
                "q": "If △XYZ ≅ △BAC, which angle of △BAC corresponds to ∠Z?",
                "options": ["∠B", "∠A", "∠C", "Cannot be determined"],
                "ans": 2,
                "exp": "In the notation △XYZ ≅ △BAC, vertex Z is in the third position, corresponding to vertex C in the third position. Thus, ∠Z corresponds to ∠C."
            }
        ]
    },
    {
        "slide_id": 18,
        "title": "Mastery Quiz 2: Isosceles Triangles & Deductive Proofs",
        "subtitle": "Pons Asinorum, Angle Bisectors, Medians & Altitudes",
        "category": "Mastery Challenge",
        "badge": "Quiz 2 • Isosceles Triangles",
        "questions": [
            {
                "q": "In an isosceles triangle △ABC with AB = AC, vertex angle ∠A = 40°. What are the measures of the two base angles?",
                "options": ["40° and 100°", "70° and 70°", "60° and 80°", "50° and 50°"],
                "ans": 1,
                "exp": "Angles opposite to equal sides are equal (∠B = ∠C). The sum of angles is 180°, so ∠B + ∠C = 180° - 40° = 140°. Each base angle is 140° / 2 = 70°."
            },
            {
                "q": "In △ABC, ∠B = ∠C = 45° and BC = 10 cm. What type of triangle is △ABC?",
                "options": ["Equilateral triangle", "Isosceles right-angled triangle", "Scalene right-angled triangle", "Obtuse isosceles triangle"],
                "ans": 1,
                "exp": "Since ∠B = ∠C = 45°, sides AB = AC (isosceles). The third angle ∠A = 180° - (45° + 45°) = 90°. Hence, it is an isosceles right-angled triangle."
            },
            {
                "q": "The median drawn to the base of an isosceles triangle is also:",
                "options": [
                    "A line parallel to the legs",
                    "Both the altitude to the base and the angle bisector of the vertical angle",
                    "Twice the length of the base",
                    "A line of symmetry dividing the area in a 2:1 ratio"
                ],
                "ans": 1,
                "exp": "In an isosceles triangle, the median to the base splits the triangle into two congruent halves (by SSS), making it simultaneously the altitude (perpendicular) and the angle bisector."
            },
            {
                "q": "If △ABC is an equilateral triangle, what is the measure of each interior angle?",
                "options": ["45°", "60°", "90°", "120°"],
                "ans": 1,
                "exp": "Since all three sides are equal, by repeated application of the isosceles triangle theorem, all three angles are equal: 3θ = 180° ⇒ θ = 60°."
            },
            {
                "q": "In △PQR, PQ = PR and S is the midpoint of QR. Which congruence criterion proves △PQS ≅ △PRS most directly?",
                "options": ["SSS", "AAA", "SSA", "None"],
                "ans": 0,
                "exp": "PQ = PR (given), QS = RS (S is midpoint), and PS = PS (common side). All three pairs of sides are equal, proving congruence by SSS."
            },
            {
                "q": "In △ABC with AB = AC, the bisectors of base angles ∠B and ∠C intersect at O. What can be concluded about △OBC?",
                "options": ["It is a scalene triangle", "It is an isosceles triangle with OB = OC", "It is an equilateral triangle", "It is a right-angled triangle"],
                "ans": 1,
                "exp": "Since ∠B = ∠C, their halves are equal: ∠OBC = ∠B/2 = ∠C/2 = ∠OCB. By the converse of the isosceles triangle theorem, OB = OC, so △OBC is isosceles."
            },
            {
                "q": "If the altitude AD of △ABC bisects base BC, what kind of triangle must △ABC be?",
                "options": ["Scalene", "Isosceles with AB = AC", "Right-angled at A", "Equilateral only"],
                "ans": 1,
                "exp": "In △ABD and △ACD: BD = CD, ∠ADB = ∠ADC = 90°, and AD = AD (common). △ABD ≅ △ACD by SAS. By CPCTC, AB = AC, so △ABC is isosceles."
            },
            {
                "q": "In △ABC, AB = AC. If an exterior angle at vertex B measures 115°, what is the vertex angle ∠A?",
                "options": ["50°", "65°", "50°", "50°"],
                "ans": 0,
                "exp": "Interior angle ∠B = 180° - 115° = 65°. Since AB = AC, ∠C = ∠B = 65°. Vertex angle ∠A = 180° - (65° + 65°) = 180° - 130° = 50°."
            },
            {
                "q": "Why was Theorem 7.2 historically called the 'Pons Asinorum' (Bridge of Asses)?",
                "options": [
                    "Because donkeys were used to measure the pyramids",
                    "Because Euclid's diagram resembled a bridge, and it served as the first rigorous test separating capable students from struggling ones",
                    "Because it is an unsolvable paradox",
                    "Because it only applies to quadrilateral bridges"
                ],
                "ans": 1,
                "exp": "In medieval universities, Euclid's Proposition 5 had a diagram resembling a trestle bridge, and was considered the first steep intellectual hurdle testing whether a student could follow abstract deductive proof."
            },
            {
                "q": "If △ABC is isosceles with AB = AC, and D, E are points on BC such that BD = CE. Why is AD = AE?",
                "options": [
                    "Because △ABD ≅ △ACE by SAS, hence AD = AE by CPCTC",
                    "Because all lines inside a triangle are equal",
                    "Because AD and AE are parallel",
                    "By the Pythagorean theorem"
                ],
                "ans": 0,
                "exp": "In △ABD and △ACE: AB = AC (given), ∠B = ∠C (isosceles base angles), and BD = CE (given). Thus △ABD ≅ △ACE by SAS, giving AD = AE by CPCTC."
            }
        ]
    },
    {
        "slide_id": 19,
        "title": "Mastery Quiz 3: Propositions, Converses & Counterexamples",
        "subtitle": "Mathematical Logic, Truth Tables & Refuting False Implications",
        "category": "Mastery Challenge",
        "badge": "Quiz 3 • Logic & Converses",
        "questions": [
            {
                "q": "What is the converse of the proposition: 'If a triangle is equilateral, then it is isosceles'?",
                "options": [
                    "If a triangle is not equilateral, then it is not isosceles",
                    "If a triangle is isosceles, then it is equilateral",
                    "If a triangle has three sides, it has three angles",
                    "All scalene triangles are equilateral"
                ],
                "ans": 1,
                "exp": "Swapping hypothesis ('a triangle is equilateral') and conclusion ('it is isosceles') yields: 'If a triangle is isosceles, then it is equilateral'."
            },
            {
                "q": "Is the converse statement 'If a triangle is isosceles, then it is equilateral' true or false?",
                "options": [
                    "True, all isosceles triangles are equilateral",
                    "False; an isosceles triangle with sides 5 cm, 5 cm, and 6 cm is not equilateral (counterexample)",
                    "True, by the SAS axiom",
                    "Cannot be determined without a protractor"
                ],
                "ans": 1,
                "exp": "The converse is false. An isosceles triangle requires only 2 equal sides; if the third side is different, it is not equilateral, serving as a decisive counterexample."
            },
            {
                "q": "Consider: 'If x = 3, then x² = 9'. What is its converse, and is the converse true for all real numbers?",
                "options": [
                    "Converse: 'If x² = 9, then x = 3'; False, because x = -3 is a counterexample",
                    "Converse: 'If x ≠ 3, then x² ≠ 9'; True",
                    "Converse: 'If x² = 9, then x = 3'; True",
                    "Converse: 'If x = 9, then x² = 3'; False"
                ],
                "ans": 0,
                "exp": "The converse is 'If x² = 9, then x = 3'. This converse is FALSE for real numbers because x = -3 also satisfies (-3)² = 9, providing a valid counterexample."
            },
            {
                "q": "Which of the following statements has a TRUE converse?",
                "options": [
                    "If a number is divisible by 4, it is even",
                    "If two angles form a linear pair, their sum is 180°",
                    "If a quadrilateral is a rhombus, it is a parallelogram",
                    "If a bird is a penguin, it cannot fly"
                ],
                "ans": 1,
                "exp": "The converse of the Linear Pair theorem is: 'If the sum of two adjacent angles is 180°, then their non-common arms form a straight line' (Axiom 6.2), which is completely TRUE."
            },
            {
                "q": "To disprove a proposed geometric converse 'All rectangles with equal diagonals are squares', one must:",
                "options": [
                    "Provide a mathematical proof of 50 steps",
                    "Provide a single counterexample (e.g. an ordinary non-square rectangle, which already has equal diagonals)",
                    "Redraw the diagram in 3D",
                    "Show that squares do not have diagonals"
                ],
                "ans": 1,
                "exp": "In mathematical logic, a single counterexample is sufficient to disprove a universal claim. Every standard non-square rectangle has equal diagonals but is not a square."
            },
            {
                "q": "When a conditional statement 'If P, then Q' is true, what is its relationship to the statement 'If not Q, then not P'?",
                "options": [
                    "It is the converse and may be false",
                    "It is the contrapositive, and it is logically equivalent (always shares the same truth value)",
                    "It is an axiom without proof",
                    "It is a contradiction"
                ],
                "ans": 1,
                "exp": "'If not Q, then not P' is the contrapositive. In formal logic, a conditional statement and its contrapositive are strictly logically equivalent."
            },
            {
                "q": "Statement: 'If two triangles are congruent, their corresponding angles are equal'. Converse: 'If all corresponding angles of two triangles are equal, they are congruent'. Why is this converse false?",
                "options": [
                    "Angles can never be equal in two different triangles",
                    "Triangles can have identical angles but different sizes (similarity), e.g. equilateral triangles of side 2 cm and 10 cm",
                    "The Angle Sum Property forbids it",
                    "Protractor errors make it impossible"
                ],
                "ans": 1,
                "exp": "AAA guarantees similarity (same shape), but not congruence (same size). Two equilateral triangles of sides 2 cm and 10 cm have identical angles (60°) but are not congruent."
            },
            {
                "q": "Which logical connective is represented by the phrase 'if and only if'?",
                "options": ["Conjunction (AND)", "Disjunction (OR)", "Biconditional (Equivalence)", "Negation (NOT)"],
                "ans": 2,
                "exp": "'If and only if' signifies a biconditional statement (P ⇔ Q), meaning both the implication P ⇒ Q and its converse Q ⇒ P are simultaneously true."
            },
            {
                "q": "If proposition P is 'n is an even number' and Q is 'n is divisible by 2', which of the following is true?",
                "options": [
                    "Only P ⇒ Q is true",
                    "Only Q ⇒ P is true",
                    "Both P ⇒ Q and Q ⇒ P are true (P ⇔ Q)",
                    "Neither is true"
                ],
                "ans": 2,
                "exp": "By definition, an integer is even if and only if it is divisible by 2. Both the conditional and its converse are true."
            },
            {
                "q": "A student claims: 'Whenever I multiply two numbers and get an even product, both numbers must have been even'. What is a counterexample?",
                "options": ["2 × 4 = 8", "3 × 4 = 12", "3 × 5 = 15", "6 × 6 = 36"],
                "ans": 1,
                "exp": "In 3 × 4 = 12, the product 12 is even, but the factor 3 is odd. This single counterexample refutes the student's universal claim."
            }
        ]
    },
    {
        "slide_id": 20,
        "title": "Mastery Quiz 4: SSA Ambiguity, Diagram Accuracy & Truss Solvers",
        "subtitle": "The Ambiguous Case, Lewis Carroll Fallacy & Engineering Rigidity",
        "category": "Mastery Challenge",
        "badge": "Quiz 4 • Advanced Synthesis",
        "questions": [
            {
                "q": "In △ABC, angle A = 30°, side b = 12 cm, and side a = 8 cm. How many distinct, non-congruent triangles can be constructed?",
                "options": ["0 triangles", "Exactly 1 triangle", "Exactly 2 triangles (Ambiguous Case)", "Infinitely many triangles"],
                "ans": 2,
                "exp": "Altitude h = b · sin(A) = 12 · sin(30°) = 6 cm. Since h (6 cm) < a (8 cm) < b (12 cm), this falls directly in the Ambiguous Case, yielding exactly 2 non-congruent triangles."
            },
            {
                "q": "If angle A = 30°, side b = 10 cm, and side a = 4 cm, how many triangles can be constructed?",
                "options": ["0 triangles (Impossible)", "1 triangle", "2 triangles", "3 triangles"],
                "ans": 0,
                "exp": "Altitude h = b · sin(A) = 10 · 0.5 = 5 cm. Since opposite side a = 4 cm is shorter than the minimum altitude (4 < 5), side a cannot reach the base line. No triangle exists."
            },
            {
                "q": "Under which circumstance does SSA (two sides and a non-included angle) guarantee a unique triangle?",
                "options": [
                    "When the opposite side a is strictly less than the altitude h",
                    "When the given angle is obtuse and the opposite side is strictly greater than the adjacent side (a > b)",
                    "Whenever the perimeter is an even integer",
                    "SSA never guarantees a unique triangle under any condition"
                ],
                "ans": 1,
                "exp": "When the given angle is obtuse (or right) and the opposite side is greater than the adjacent side (a > b), only one unique triangle can be formed."
            },
            {
                "q": "Why does RHS succeed as a valid congruence criterion while general SSA fails?",
                "options": [
                    "Because right angles are larger than acute angles",
                    "Because when the angle is 90°, the Pythagorean theorem locks the third side to a single unique value, eliminating the second intersection",
                    "Because right triangles have only two vertices",
                    "Because circles cannot intersect at 90°"
                ],
                "ans": 1,
                "exp": "In a right triangle, the third side is strictly fixed as √(hypotenuse² - leg²). This prevents an ambiguous second intersection, reducing the situation to SSS."
            },
            {
                "q": "What core lesson does Lewis Carroll's 'All Triangles are Isosceles' fallacy teach geometry students?",
                "options": [
                    "That all triangles are indeed isosceles if drawn carefully",
                    "That deductive proofs must be grounded strictly in axioms and theorems, never on the visual assumptions of an inaccurate sketch",
                    "That angle bisectors do not exist in scalene triangles",
                    "That perpendicular lines never intersect"
                ],
                "ans": 1,
                "exp": "The fallacy proves that diagrams can deceive our intuition. In formal geometry, every step must be justified by proven axioms and theorems rather than visual appearance."
            },
            {
                "q": "In Lewis Carroll's fallacy, where does the intersection of the angle bisector of ∠A and the perpendicular bisector of BC actually lie for a scalene triangle?",
                "options": [
                    "Inside the triangle",
                    "Strictly outside the triangle on its circumcircle",
                    "At vertex A",
                    "At the midpoint of side AB"
                ],
                "ans": 1,
                "exp": "For any non-isosceles triangle, the angle bisector of the vertex and the perpendicular bisector of the opposite base intersect strictly OUTSIDE the triangle on its circumcircle."
            },
            {
                "q": "According to Maxwell's rule for planar pin-jointed trusses (m = 2j - 3), what happens if a framework has j = 4 joints and only m = 4 member bars?",
                "options": [
                    "It is rigid and statically determinate",
                    "It is under-constrained (m < 2(4) - 3 = 5) and will collapse under shear like a parallelogram mechanism",
                    "It is over-constrained and indestructible",
                    "It becomes a 3D dome"
                ],
                "ans": 1,
                "exp": "For j = 4 joints, rigidity requires m = 2(4) - 3 = 5 bars. With only 4 bars (a quadrilateral), it has an internal degree of freedom and will collapse into a parallelogram unless a 5th diagonal bar is added."
            },
            {
                "q": "In truss bridge design (such as Warren or Pratt trusses), why are structural steel beams arranged exclusively in repeating triangles?",
                "options": [
                    "Triangles use less paint than squares",
                    "Triangular sub-units are inherently rigid, converting bending loads into direct axial tension and compression without deformation",
                    "Because steel can only be welded at 60° angles",
                    "To prevent wind from passing through the bridge"
                ],
                "ans": 1,
                "exp": "Triangles cannot change angle without changing side length (SSS). This rigidity ensures forces are transmitted axially through the members rather than causing bending moments that collapse the structure."
            },
            {
                "q": "What is the computational complexity of verifying whether two triangles are congruent given their six numerical elements (3 sides, 3 angles)?",
                "options": ["O(1) constant time", "O(N²) quadratic time", "O(N!) factorial time", "Undecidable"],
                "ans": 0,
                "exp": "A congruence decision algorithm only performs a fixed number of arithmetic comparisons and trigonometric checks (at most a dozen operations), executing in O(1) constant time."
            },
            {
                "q": "If a planar pin-jointed bridge truss has j = 10 joints, what is the minimum number of member bars m required for static rigidity?",
                "options": ["m = 10", "m = 14", "m = 17", "m = 20"],
                "ans": 2,
                "exp": "Using Maxwell's formula m = 2j - 3 for j = 10 joints: m = 2(10) - 3 = 20 - 3 = 17 structural member bars."
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


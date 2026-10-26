"""
Data module for Class 9 Mathematics Chapter 11: Circles
Syllabus Competencies: CG-4, C-7.3, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Practical Applications, Wheels & Cultural Motifs",
        "subtitle": "Kinematic Rolling Resistance, Ancient Civilisation Inventions & Sacred Chakra Geometry",
        "category": "Practical Applications",
        "badge": "CG-4 • CG-9 • Practical & Cultural",
        "summary": "Why is the circle the most transformative shape in human civilisation? The invention of the circular wheel around 3500 BCE in Mesopotamia revolutionised transport, agriculture, and industry because rolling resistance is orders of magnitude smaller than sliding friction: a round wheel converts surface friction into smooth rotational contact at a single instantaneous point. Circular geometry enabled water wheels for milling and irrigation, gear trains for mechanical power, pulleys for lifting colossal stones, and circular arches in architectural monuments. Culturally, the circle symbolises perfection, cosmic cycles, and infinite truth: the Dharmachakra (Wheel of the Law), the Ashoka Chakra (featured on India's national flag with 24 spokes representing 24 virtues of dynamic righteousness), and the Sudarshan Chakra (the supreme weapon of cosmic balance).",
        "key_points": [
            "Rolling vs. Sliding Friction: Circular wheels minimise energy dissipation by replacing dragging with rotational contact.",
            "Historical Impact: Invention of the wheel (c. 3500 BCE) transformed transport, pottery, irrigation, and mechanical machinery.",
            "Architectural & Engineering Uses: Circular pulleys, gear teeth, clock mechanisms, and Roman dome keystones.",
            "The Ashoka Chakra: 24 spokes in India's national flag symbolising 24 hours of continuous righteous movement and progress.",
            "Universal Symmetry: A circle possesses infinite axes of reflection symmetry and rotational symmetry of every order."
        ],
        "narration": "Welcome to Circles! The circle is arguably humanity's greatest discovery. When ancient humans invented the circular wheel, they replaced high sliding friction with smooth rolling contact, changing transportation, farming, and engineering forever! In Indian culture, the circle represents cosmic order—from the Sudarshan Chakra to the 24 spokes of the Ashoka Chakra on our national flag.",
        "sim_title": "Wheel Rolling vs. Sliding Kinematics & 24-Spoke Chakra Generator",
        "checkpoints": [
            {
                "q": "Why is transporting heavy loads on circular wheels far more efficient than dragging them along the ground?",
                "options": [
                    "Circular wheels eliminate all gravity",
                    "Rolling motion replaces continuous sliding friction with point-contact rotation, drastically reducing resistive force",
                    "A circular shape weighs less than a flat sled",
                    "Circles produce magnetic levitation"
                ],
                "ans": 1,
                "exp": "Rolling resistance is vastly smaller than kinetic sliding friction because the contact surface is continuously lifted and set down rather than scraped across the ground."
            },
            {
                "q": "How many spokes are present in the Ashoka Chakra depicted on the National Flag of India?",
                "options": ["12 spokes", "16 spokes", "24 spokes", "32 spokes"],
                "ans": 2,
                "exp": "The Ashoka Chakra has exactly 24 evenly spaced radial spokes, each separated by 360° / 24 = 15°, representing the 24 hours of continuous righteous progress."
            }
        ]
    },
    {
        "id": 2,
        "title": "Definitions & Anatomy of a Circle",
        "subtitle": "Centre, Radius, Diameter, Chord, Secant, Arc, Segment & Sector",
        "category": "Foundations",
        "badge": "CG-4 • C-7.3 • Circle Anatomy",
        "summary": "In Euclidean geometry, a Circle is defined as the collection of all coplanar points that lie at a constant distance (called the Radius, r) from a fixed coplanar point (called the Centre, O). The perimeter of the circle is its Circumference (C = 2πr). Key anatomical elements: 1. Chord: A straight line segment connecting any two points on the circle. 2. Diameter: A chord that passes through the centre of the circle (length d = 2r); it is the longest possible chord. 3. Secant: A straight line that cuts the circle in two distinct points. 4. Arc: A continuous piece of the circle between two points; divided into Minor Arc (less than a semicircle) and Major Arc (greater than a semicircle). 5. Segment: The planar region enclosed between a chord and its corresponding arc (Minor Segment and Major Segment). 6. Sector: The planar region enclosed between two radii and their corresponding arc (Minor Sector and Major Sector).",
        "key_points": [
            "Formal Definition: Locus of all points in a plane equidistant from a fixed center O.",
            "Radius & Diameter: Radius r = OA; Diameter d = 2r (the longest chord passing through center O).",
            "Chord vs. Secant: A chord is a line segment between two boundary points; a secant is an extended intersecting line.",
            "Segment vs. Sector: A segment is bounded by a chord and an arc; a sector is bounded by two radii and an arc (slice of pie).",
            "Plane Partition: A circle divides its plane into three disjoint sets: interior, circle boundary, and exterior."
        ],
        "narration": "Let's learn the anatomy of a circle! The centre is the fixed heart, and the radius is the constant distance to the edge. A line segment joining any two points on the circle is a chord, and the longest chord passing through the center is the diameter! Be careful not to confuse a segment and a sector: a sector is like a slice of pizza cut by two radii, while a segment is cut by a straight chord!",
        "sim_title": "Interactive Circle Anatomy & Element Inspector",
        "checkpoints": [
            {
                "q": "What is the region enclosed between a chord and the corresponding arc called?",
                "options": ["Sector", "Segment", "Secant", "Quadrant"],
                "ans": 1,
                "exp": "A segment is the planar region bounded by a chord and its subtended arc. A sector is bounded by two radii and an arc."
            },
            {
                "q": "If the radius of a circle is 8.5 cm, what is the length of its longest chord?",
                "options": ["4.25 cm", "8.5 cm", "17.0 cm", "26.7 cm"],
                "ans": 2,
                "exp": "The longest chord of any circle is its diameter, which is twice the radius: d = 2r = 2 × 8.5 cm = 17.0 cm."
            }
        ]
    },
    {
        "id": 3,
        "title": "Unique Circle Through Three Non-Collinear Points",
        "subtitle": "Theorem 9.5: Existence, Uniqueness, Perpendicular Bisectors & Circumcircle Construction",
        "category": "Constructions & Theorems",
        "badge": "CG-4 • C-7.3 • Unique Circle Proof",
        "summary": "Theorem: 'There is one and only one circle passing through three given non-collinear points.' Proof: Let A, B, and C be three non-collinear points. Join AB and BC. Draw the perpendicular bisector l of AB and the perpendicular bisector m of BC. Because A, B, and C do not lie on a single straight line, segments AB and BC are not parallel; therefore, their perpendicular bisectors l and m are not parallel and must intersect at a unique point O! By the perpendicular bisector theorem, any point on l is equidistant from A and B (OA = OB). Any point on m is equidistant from B and C (OB = OC). Since point O lies on both lines simultaneously, OA = OB = OC = R! With O as centre and R as radius, a circle drawn through A will pass precisely through B and C. Since two straight lines can intersect in at most ONE point, centre O and radius R are strictly unique!",
        "key_points": [
            "Theorem: Exactly one unique circle passes through any three non-collinear points.",
            "Circumcentre (O): The point of concurrency where the perpendicular bisectors of the sides intersect.",
            "Equidistant Property: OA = OB = OC = R (the Circumradius).",
            "Why Non-Collinear Matters: If three points are collinear, their perpendicular bisectors are parallel and never intersect (no circle exists).",
            "Construction Procedure: Bisect two chords/sides; their intersection is the compass pivot point."
        ],
        "narration": "Can you draw a circle through any three points? If the points are in a straight line, it's impossible! But if they form a triangle, there is ALWAYS exactly one unique circle that passes through all three! Why? Because the perpendicular bisectors of the sides meet at a single magic point O called the Circumcentre, which is at the exact same distance from all three corners!",
        "sim_title": "3-Point Circumcircle & Perpendicular Bisector Intersection Lab",
        "checkpoints": [
            {
                "q": "How many circles can pass through three given collinear points (lying on a straight line)?",
                "options": ["0 (None)", "Exactly 1", "Exactly 3", "Infinitely many"],
                "ans": 0,
                "exp": "No circle can pass through three distinct collinear points because the perpendicular bisectors of collinear segments are parallel and never intersect to provide a center."
            },
            {
                "q": "What is the common intersection point of the perpendicular bisectors of the sides of a triangle called?",
                "options": ["Incentre", "Centroid", "Circumcentre", "Orthocentre"],
                "ans": 2,
                "exp": "The circumcentre is the point of concurrency of the perpendicular bisectors of the sides of a triangle, serving as the center of the circumcircle."
            }
        ]
    },
    {
        "id": 4,
        "title": "Location of the Circumcentre Across Triangle Types",
        "subtitle": "Interior for Acute Triangles, Hypotenuse Midpoint for Right Triangles & Exterior for Obtuse",
        "category": "Geometric Analysis",
        "badge": "CG-4 • C-7.3 • Circumcentre Location",
        "summary": "Where does the circumcentre O lie relative to a triangle? Its position depends fundamentally on the largest angle of the triangle: 1. Acute-Angled Triangle: All three angles are < 90°. The perpendicular bisectors meet inside the triangle. Circumcentre O lies strictly IN THE INTERIOR. 2. Right-Angled Triangle: One angle is exactly 90°. By Thales' Theorem, the hypotenuse is the diameter of the circumcircle! The circumcentre O lies EXACTLY ON THE HYPOTENUSE, precisely at its MIDPOINT. The circumradius R equals half the hypotenuse: R = (Hypotenuse)/2. 3. Obtuse-Angled Triangle: One angle is > 90°. The opposite arc is a major arc, forcing the center of curvature outward. The circumcentre O lies strictly OUTSIDE (in the exterior of) the triangle, beyond the longest side opposite the obtuse angle.",
        "key_points": [
            "Acute Triangle: Circumcentre O lies strictly inside the interior.",
            "Right Triangle: Circumcentre O lies exactly at the midpoint of the hypotenuse (R = Hypotenuse / 2).",
            "Obtuse Triangle: Circumcentre O lies strictly outside in the exterior.",
            "Thales' Connection: In a right triangle, hypotenuse = diameter, so median to hypotenuse = R.",
            "Continuous Migration: Moving a vertex smoothly shifts the circumcentre from inside, onto the edge, to outside."
        ],
        "narration": "Where does the circumcentre hide? For an acute triangle, it sits peacefully inside. But stretch one angle to 90 degrees, and the circumcentre moves right onto the midpoint of the hypotenuse! Push the angle wider into an obtuse angle, and the circumcentre pops completely outside the triangle! Watch how it smoothly migrates in our simulator.",
        "sim_title": "Triangle Angle Morph & Circumcentre Migration Tracker",
        "checkpoints": [
            {
                "q": "In a right-angled triangle with legs 6 cm and 8 cm, where is the circumcentre located and what is the circumradius?",
                "options": [
                    "Inside the triangle, radius = 5 cm",
                    "At the midpoint of the hypotenuse, radius = 5 cm",
                    "Outside the triangle, radius = 10 cm",
                    "At the 90° vertex, radius = 7 cm"
                ],
                "ans": 1,
                "exp": "By Pythagoras, hypotenuse = √(6² + 8²) = 10 cm. In a right triangle, the circumcentre is the midpoint of the hypotenuse, and the circumradius is half the hypotenuse: 10 / 2 = 5 cm."
            },
            {
                "q": "For which type of triangle does the circumcentre lie in the exterior (outside) of the triangle?",
                "options": ["Equilateral triangle", "Acute-angled triangle", "Obtuse-angled triangle", "Right-angled triangle"],
                "ans": 2,
                "exp": "For an obtuse-angled triangle (one angle > 90°), the perpendicular bisectors intersect in the exterior region outside the triangle."
            }
        ]
    },
    {
        "id": 5,
        "title": "Chords & Angles Subtended at the Centre (Theorems 9.1 & 9.2)",
        "subtitle": "Equal Chords Subtend Equal Central Angles & Converse Proof via SSS and SAS",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 9.1 & 9.2",
        "summary": "What is an 'angle subtended by a chord at the centre'? If AB is a chord and O is the centre, the angle ∠AOB formed by the radii OA and OB is the angle subtended by chord AB at the centre. Theorem 9.1 states: 'Equal chords of a circle subtend equal angles at the centre.' Proof: Let AB and CD be equal chords of a circle with centre O (AB = CD). In △AOB and △COD: OA = OC (radii of the same circle), OB = OD (radii of the same circle), and AB = CD (given). Therefore, △AOB ≅ △COD by the SSS congruence criterion! By CPCTC, ∠AOB = ∠COD. Theorem 9.2 is the Converse: 'If the angles subtended by the chords of a circle at the centre are equal, then the chords are equal.' Proof: Given ∠AOB = ∠COD. In △AOB and △COD: OA = OC (radii), ∠AOB = ∠COD (given), OB = OD (radii). Thus △AOB ≅ △COD by the SAS axiom! By CPCTC, chord AB = chord CD.",
        "key_points": [
            "Theorem 9.1: Chord AB = CD ⇒ Central angle ∠AOB = ∠COD (proven via SSS congruence).",
            "Theorem 9.2 (Converse): Central angle ∠AOB = ∠COD ⇒ Chord AB = CD (proven via SAS congruence).",
            "Subtended Definition: The angle formed at a point by rays passing through the endpoints of an arc or chord.",
            "Congruent Circles Generalisation: The theorems hold identically across two distinct congruent circles of equal radii.",
            "Direct Symmetry: Equal central sectors produce equal chords and equal arc lengths."
        ],
        "narration": "Theorem 9.1 is all about symmetry! If two chords in a circle have the exact same length, they subtend identical angles at the centre. Why? Because the triangles formed with the centre share the same radii, making them congruent by SSS! And if the angles at the centre match, SAS proves the chords must be equal!",
        "sim_title": "Chord Equalizer & Central Angle Subtended Dial",
        "checkpoints": [
            {
                "q": "In a circle with centre O, chords AB and CD subtend angles of 70° and 70° at O. If AB = 8 cm, what is the length of CD?",
                "options": ["4 cm", "8 cm", "14 cm", "16 cm"],
                "ans": 1,
                "exp": "By Theorem 9.2 (Converse), chords that subtend equal angles at the centre are equal in length. Since ∠AOB = ∠COD = 70°, CD = AB = 8 cm."
            },
            {
                "q": "Which congruence criterion proves Theorem 9.1 (that equal chords subtend equal angles at the centre)?",
                "options": ["SSS", "SAS", "ASA", "RHS"],
                "ans": 0,
                "exp": "In △AOB and △COD: OA = OC (radii), OB = OD (radii), and AB = CD (given). All three pairs of sides are equal, proving congruence by SSS, so ∠AOB = ∠COD by CPCTC."
            }
        ]
    },
    {
        "id": 6,
        "title": "Perpendicular from Centre Bisects a Chord (Theorems 9.3 & 9.4)",
        "subtitle": "The Perpendicular-Midpoint Equivalence & Proof via RHS and SSS Congruence",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 9.3 & 9.4",
        "summary": "Theorem 9.3 states: 'The perpendicular from the centre of a circle to a chord bisects the chord.' Let AB be a chord of a circle with centre O, and let OM ⊥ AB with M on AB. We wish to prove AM = MB. Proof: Join OA and OB. In right-angled triangles △OMA and △OMB: ∠OMA = ∠OMB = 90° (given OM ⊥ AB), hypotenuse OA = hypotenuse OB (radii of the same circle), and OM = OM (common leg). Therefore, △OMA ≅ △OMB by the RHS congruence criterion! By CPCTC, AM = MB. Hence M is the midpoint of chord AB! Theorem 9.4 is the Converse: 'The line drawn through the centre of a circle to bisect a chord is perpendicular to the chord.' Proof: Let M be the midpoint of chord AB (AM = MB). In △OMA and △OMB: OA = OB (radii), AM = MB (given), OM = OM (common). Thus △OMA ≅ △OMB by SSS! By CPCTC, ∠OMA = ∠OMB. Since ∠OMA + ∠OMB = 180° (linear pair), 2∠OMA = 180° ⇒ ∠OMA = 90°. Thus OM ⊥ AB!",
        "key_points": [
            "Theorem 9.3: OM ⊥ AB ⇒ AM = MB (perpendicular bisects the chord, proven via RHS).",
            "Theorem 9.4 (Converse): AM = MB ⇒ OM ⊥ AB (line to midpoint is perpendicular, proven via SSS and linear pair).",
            "Right Triangle Foundation: Creates a right triangle △OMA with legs OM (distance d), AM (half-chord L/2), and hypotenuse OA (radius r).",
            "Construction Value: To find the centre of an unknown circle, draw any two chords and intersect their perpendicular bisectors.",
            "Diameter Bisection: A diameter perpendicular to a chord bisects both the chord and its subtended arc."
        ],
        "narration": "If you drop a perpendicular line from the centre O onto any chord AB, it hits the chord at its exact midpoint M! Why? In the two right triangles formed, both have the circle's radius as their hypotenuse and share the vertical leg OM. By RHS, the triangles are identical, so AM must equal MB!",
        "sim_title": "Perpendicular Bisector & Chord Midpoint Explorer",
        "checkpoints": [
            {
                "q": "In a circle of radius 10 cm, a perpendicular OM is drawn from centre O to a chord AB of length 16 cm. What is the length of AM?",
                "options": ["5 cm", "8 cm", "10 cm", "12 cm"],
                "ans": 1,
                "exp": "By Theorem 9.3, the perpendicular from the centre bisects the chord. AM = AB / 2 = 16 / 2 = 8 cm."
            },
            {
                "q": "Which congruence condition proves Theorem 9.3 (perpendicular from centre bisects chord)?",
                "options": ["RHS", "ASA", "AAS", "AAA"],
                "ans": 0,
                "exp": "In right triangles △OMA and △OMB: right angles at M, equal hypotenuses OA = OB = r, and common leg OM. Congruence is established by RHS, yielding AM = MB by CPCTC."
            }
        ]
    },
    {
        "id": 7,
        "title": "Distance of a Chord from the Centre & Pythagoras",
        "subtitle": "The Fundamental Metric Formula: r² = d² + (L/2)² & The Inverse Distance-Length Law",
        "category": "Metric Properties",
        "badge": "CG-4 • C-7.3 • Chord Distance Formula",
        "summary": "In geometry, the 'distance' of a chord from the centre is defined as the length of the perpendicular segment drawn from the centre to the chord (OM = d). Consider the right-angled triangle △OMA, where hypotenuse OA = r (radius), base AM = L/2 (half the chord length), and perpendicular OM = d (distance from centre). Applying the Pythagorean Theorem yields the fundamental circle metric identity: r² = d² + (L/2)². Rearranging for chord length L gives: L = 2√(r² - d²). This mathematical relationship reveals two profound geometric truths: 1. Inverse Relationship: As distance d increases, the expression √(r² - d²) decreases, meaning chord length L decreases! 2. Limits: When d = r, L = 0 (the chord shrinks to a tangent point). When d = 0, L = 2r (the chord passes through the centre, becoming the diameter!).",
        "key_points": [
            "Perpendicular Distance: Distance d is the shortest straight-line distance from centre O to chord AB (OM ⊥ AB).",
            "Pythagorean Identity: r² = d² + (L/2)², connecting radius r, distance d, and chord length L.",
            "Half-Chord Formula: Half-chord AM = √(r² - d²); Full chord L = 2√(r² - d²).",
            "Distance vs. Length: Chords closer to the centre (smaller d) are strictly longer than chords farther away (larger d).",
            "Boundary Conditions: d = 0 yields maximum chord (diameter L = 2r); d = r yields minimum chord (point tangent L = 0)."
        ],
        "narration": "How is chord length related to its distance from the centre? Look at the right triangle inside: the radius is the hypotenuse, distance d is one leg, and half the chord is the other leg! By Pythagoras, r-squared equals d-squared plus half-chord squared. The closer a chord gets to the centre, the longer it grows!",
        "sim_title": "Chord Distance Slider & Pythagorean Calculator",
        "checkpoints": [
            {
                "q": "A chord of length 24 cm is drawn in a circle of radius 13 cm. What is the perpendicular distance of the chord from the centre?",
                "options": ["5 cm", "7 cm", "10 cm", "12 cm"],
                "ans": 0,
                "exp": "Half-chord = 24 / 2 = 12 cm. Radius r = 13 cm. By Pythagoras: d = √(r² - (L/2)²) = √(13² - 12²) = √(169 - 144) = √25 = 5 cm."
            },
            {
                "q": "If a chord of a circle of radius 5 cm is at a distance of 3 cm from the centre, what is the total length of the chord?",
                "options": ["4 cm", "6 cm", "8 cm", "10 cm"],
                "ans": 2,
                "exp": "Half-chord = √(5² - 3²) = √(25 - 9) = √16 = 4 cm. Total chord length L = 2 × 4 cm = 8 cm."
            }
        ]
    },
    {
        "id": 8,
        "title": "Equal Chords & Equidistance from Centre (Theorems 9.5 & 9.6)",
        "subtitle": "Theorem 9.5: Equal Chords Are Equidistant from the Centre & Theorem 9.6 Converse",
        "category": "Theorems & Proofs",
        "badge": "CG-4 • C-7.3 • Theorems 9.5 & 9.6",
        "summary": "Theorem 9.5 states: 'Equal chords of a circle (or of congruent circles) are equidistant from the centre.' Let AB and CD be equal chords of a circle with centre O (AB = CD). Draw OM ⊥ AB and ON ⊥ CD. We wish to prove OM = ON. Proof: Since perpendicular from centre bisects chord, AM = 1/2 AB and CN = 1/2 CD. Given AB = CD, we have AM = CN. In right triangles △OMA and △ONC: ∠OMA = ∠ONC = 90° (by construction), hypotenuse OA = hypotenuse OC (radii of the same circle), and leg AM = leg CN (proven). Therefore, △OMA ≅ △ONC by RHS! By CPCTC, OM = ON. Hence equal chords are equidistant from the centre! Theorem 9.6 is the Converse: 'Chords equidistant from the centre of a circle are equal in length.' Proof: Given OM = ON. In right △OMA and △ONC: OA = OC (radii), OM = ON (given), ∠OMA = ∠ONC = 90°. Thus △OMA ≅ △ONC by RHS! By CPCTC, AM = CN ⇒ 2AM = 2CN ⇒ AB = CD!",
        "key_points": [
            "Theorem 9.5: AB = CD ⇒ OM = ON (equal chords are equidistant from centre, proven via RHS).",
            "Theorem 9.6 (Converse): OM = ON ⇒ AB = CD (chords equidistant from centre are equal in length).",
            "Congruent Circles Extension: Holds identically for chords in two separate circles having the same radius.",
            "Concentric Circles Application: If a line intersects two concentric circles at A, B, C, D, then AB = CD.",
            "RHS Mechanism: Both proofs rely on RHS congruence in right triangles formed with radius hypotenuses."
        ],
        "narration": "Theorem 9.5 reveals that equal chords must stand at the exact same distance from the centre! If chord AB equals chord CD, their perpendicular distances OM and ON are identical. And the reverse is also true: if two chords are equally distant from the center, RHS proves they must have the exact same length!",
        "sim_title": "Equidistant Chords Balancer & Concentric Circle Explorer",
        "checkpoints": [
            {
                "q": "Two chords AB and CD of a circle of radius 10 cm are both at a distance of 6 cm from the centre. If AB = 16 cm, what is the length of CD?",
                "options": ["8 cm", "12 cm", "16 cm", "20 cm"],
                "ans": 2,
                "exp": "By Theorem 9.6 (Converse), chords that are equidistant from the centre are equal in length. Since both are at distance 6 cm, CD = AB = 16 cm."
            },
            {
                "q": "In two concentric circles with common centre O, a line cuts the outer circle at A, D and inner circle at B, C. What is the relationship between AB and CD?",
                "options": ["AB = 2 CD", "AB = CD", "AB + CD = BC", "AB ⊥ CD"],
                "ans": 1,
                "exp": "Drawing perpendicular OM from O to the line bisects AD (AM = MD) and bisects BC (BM = MC). Subtracting gives AM - BM = MD - MC ⇒ AB = CD."
            }
        ]
    },
    {
        "id": 9,
        "title": "Unequal Chords & Diameter as the Longest Chord",
        "subtitle": "The Closer the Chord the Longer It Is & Proof that Diameter Reaches 2r",
        "category": "Metric Properties",
        "badge": "CG-4 • C-7.3 • Longest Chord Theorem",
        "summary": "What happens when two chords are unequal in length? Theorem: 'Among unequal chords in a circle, the longer chord is closer to the centre (and conversely, the chord closer to the centre is longer).' Proof: Let chords have lengths L₁ and L₂ with distances d₁ and d₂ from centre O. By Pythagoras: r² = d₁² + (L₁/2)² and r² = d₂² + (L₂/2)². Therefore: d₁² + (L₁/2)² = d₂² + (L₂/2)². If L₁ > L₂, then (L₁/2)² > (L₂/2)², which strictly forces d₁² < d₂² ⇒ d₁ < d₂! Hence the longer chord is closer to the centre. The Ultimate Corollary: 'The diameter is the longest chord in any circle.' Proof: A chord AB achieves its absolute minimum distance from the centre when d = 0 (passing through O). Substituting d = 0 gives L = 2√(r² - 0) = 2r = diameter! By the Triangle Inequality in △AOB, for any chord AB not passing through O, AB < OA + OB = r + r = 2r. Hence no chord can ever exceed 2r.",
        "key_points": [
            "Unequal Chords Theorem: L₁ > L₂ ⇔ d₁ < d₂ (longer chord is strictly closer to the centre).",
            "Algebraic Invariance: d² + (L/2)² = r² (sum of squares is constant; as one increases, other must decrease).",
            "Diameter as Longest Chord: Passing through center O (d = 0) maximizes length to exactly 2r.",
            "Triangle Inequality Proof: For any chord AB, AB ≤ OA + OB = r + r = 2r, with equality if and only if O lies on AB.",
            "Extremum Principle: Diameter is the unique maximum chord; tangent point is the minimum."
        ],
        "narration": "Here is an intuitive rule: the closer a chord is to the centre of the circle, the longer it is! If chord 1 is longer than chord 2, it must be closer to the centre. What chord is the closest of all? The one that passes right through the centre, where distance is zero! That chord is the diameter, and it is the longest possible chord in any circle.",
        "sim_title": "Chord Length Maximizer & Distance Comparator",
        "checkpoints": [
            {
                "q": "Two chords AB and CD of a circle have lengths 14 cm and 10 cm respectively. Which chord is closer to the centre?",
                "options": ["Chord CD", "Chord AB", "Both are at the same distance", "Cannot be determined without the radius"],
                "ans": 1,
                "exp": "By the Unequal Chords Theorem, among two unequal chords, the longer chord is strictly closer to the centre. Since 14 cm > 10 cm, chord AB is closer."
            },
            {
                "q": "Why is the diameter of a circle of radius r the longest possible chord?",
                "options": [
                    "Because its distance from the centre is d = 0, maximizing length to 2√(r² - 0) = 2r",
                    "Because it has no endpoints",
                    "Because all circles are round",
                    "Because it divides the circle into three sectors"
                ],
                "ans": 0,
                "exp": "Since distance d ≥ 0, chord length L = 2√(r² - d²) achieves its maximum possible value when d = 0, giving L = 2r (the diameter)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Inscribed Angle Theorem: Central Angle is Double (Theorem 9.7)",
        "subtitle": "Angle Subtended by an Arc at the Centre is Double That at the Boundary (∠AOB = 2∠APB)",
        "category": "Subtended Angles",
        "badge": "CG-4 • C-7.3 • Theorem 9.7 (2θ vs θ)",
        "summary": "Theorem 9.7 (The Inscribed Angle Theorem) is the central pivot of circle geometry: 'The angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle' (∠AOB = 2∠APB). Proof: Let arc AB subtend ∠AOB at centre O and ∠APB at point P on the remaining boundary. Join PO and extend it to a point Q outside the circle. In △OPA, OA = OP (radii), so △OPA is isosceles with ∠OPA = ∠OAP. In △OPA, exterior angle ∠AOQ = ∠OPA + ∠OAP = 2∠OPA. Similarly, in △OPB, OB = OP (radii), so exterior angle ∠BOQ = ∠OPB + ∠OBP = 2∠OPB. Adding the two equations: ∠AOB = ∠AOQ + ∠BOQ = 2∠OPA + 2∠OPB = 2(∠OPA + ∠OPB) = 2∠APB! This master proof holds in all three geometric cases: Case 1 (arc AB is minor), Case 2 (arc AB is a semicircle), and Case 3 (arc AB is major, where reflex ∠AOB = 2∠APB).",
        "key_points": [
            "Theorem 9.7 Statement: ∠AOB = 2∠APB (central angle is strictly double the inscribed angle subtending the same arc).",
            "Isosceles Triangle Logic: Radii OA = OP = OB create two isosceles triangles whose base angles double into exterior angles.",
            "Exterior Angle Mechanism: ∠AOQ = 2∠APO and ∠BOQ = 2∠BPO.",
            "Three Universal Cases: Minor arc, semicircle (180°), and major arc (reflex angle > 180°).",
            "Foundational Role: Almost all subsequent circle theorems (angles in same segment, cyclic quadrilaterals) derive directly from Theorem 9.7."
        ],
        "narration": "Here is the master theorem of circle geometry: Theorem 9.7! Take an arc AB. The angle it makes at the centre O is ALWAYS exactly TWICE the angle it makes at any point P on the circle boundary! If the angle at the edge is 40 degrees, the angle at the center MUST be 80 degrees! Let's trace the rays in our interactive simulator.",
        "sim_title": "Inscribed Angle vs. Central Angle Ray Tracer (2θ vs θ)",
        "checkpoints": [
            {
                "q": "An arc AB subtends an angle of 110° at the centre O of a circle. What angle does it subtend at a point P on the remaining major arc?",
                "options": ["55°", "70°", "110°", "220°"],
                "ans": 0,
                "exp": "By Theorem 9.7, the inscribed angle is half the central angle: ∠APB = 1/2 ∠AOB = 1/2 × 110° = 55°."
            },
            {
                "q": "If an inscribed angle ∠APB equals 42°, what is the measure of the central angle ∠AOB subtended by the same arc?",
                "options": ["21°", "42°", "84°", "138°"],
                "ans": 2,
                "exp": "By Theorem 9.7, central angle ∠AOB = 2 × ∠APB = 2 × 42° = 84°."
            }
        ]
    },
    {
        "id": 11,
        "title": "Angles in the Same Segment Are Equal (Theorem 9.8)",
        "subtitle": "Invariance of the Inscribed Angle Along an Arc & Fixed Central Angle Reduction",
        "category": "Subtended Angles",
        "badge": "CG-4 • C-7.3 • Theorem 9.8 (Same Segment)",
        "summary": "Theorem 9.8 states: 'Angles in the same segment of a circle are equal.' Let AB be a chord dividing a circle into a minor segment and a major segment. Let P and Q be any two distinct points lying on the major arc. We wish to prove that ∠APB = ∠AQB. Proof: Let O be the centre of the circle. By Theorem 9.7, the angle subtended by arc AB at the centre is double the angle subtended by it at any point on the remaining part of the circle. Therefore: ∠AOB = 2∠APB ⇒ ∠APB = 1/2 ∠AOB. Similarly, for point Q on the same arc: ∠AOB = 2∠AQB ⇒ ∠AQB = 1/2 ∠AOB. Equating the two expressions: ∠APB = 1/2 ∠AOB = ∠AQB! Thus, ∠APB = ∠AQB. This means that as point P slides anywhere along the boundary arc, the angle formed by its arms looking at base AB remains rigidly locked at a constant angle!",
        "key_points": [
            "Theorem 9.8 Statement: All inscribed angles subtending the same chord from the same arc segment are equal (∠APB = ∠AQB).",
            "Derivation from Theorem 9.7: Both angles equal half of the identical fixed central angle: ∠P = ∠Q = 1/2 ∠AOB.",
            "Segment Invariance: As point P glides continuously along the arc, angle measure θ never changes.",
            "Bow-Tie Pattern: Two intersecting chords AC and BD create equal angles ∠BAC = ∠BDC and ∠ABD = ∠ACD.",
            "Opposite Segment Contrast: Angles in the opposite (minor) segment are obtuse and supplementary to the major segment angles."
        ],
        "narration": "Imagine standing on the circle at point P, looking at two fixed posts A and B. As you walk along the circle boundary, does your viewing angle change? Remarkably, NO! By Theorem 9.8, angles in the same segment are completely equal! Every single point on that arc sees chord AB under the exact same angle!",
        "sim_title": "Same-Segment Angle Glider & Constant Angle Tracer",
        "checkpoints": [
            {
                "q": "In a circle, points P and Q lie in the same segment of chord AB. If ∠APB = 64°, what is the measure of ∠AQB?",
                "options": ["32°", "64°", "116°", "128°"],
                "ans": 1,
                "exp": "By Theorem 9.8, angles in the same segment of a circle are strictly equal. Therefore, ∠AQB = ∠APB = 64°."
            },
            {
                "q": "Why do all angles in the same segment of a circle have identical measures?",
                "options": [
                    "Because each angle equals exactly half of the same fixed central angle (1/2 ∠AOB)",
                    "Because chords are always equal to radii",
                    "Because all triangles are equilateral",
                    "Because circles have 360 degrees"
                ],
                "ans": 0,
                "exp": "By the Inscribed Angle Theorem, every angle inscribed in that segment equals 1/2 ∠AOB. Since ∠AOB is constant, all inscribed angles are identical."
            }
        ]
    },
    {
        "id": 12,
        "title": "Angle in a Semicircle is a Right Angle (Thales' Theorem)",
        "subtitle": "The 180° Diameter Straight Angle & The First Deductive Proof in Human History",
        "category": "Subtended Angles",
        "badge": "CG-4 • C-7.3 • Thales' Semicircle 90°",
        "summary": "One of the most celebrated corollaries in the history of mathematics is Thales' Theorem: 'The angle in a semicircle is a right angle' (90°). Proof: Let AB be a diameter of a circle with centre O, and let P be any point on the semicircle. Because AB is a diameter passing through centre O, the angle subtended by diameter AB at the centre is a straight angle: ∠AOB = 180°. By Theorem 9.7, the angle subtended by arc AB at the centre is double the angle subtended by it at any point P on the circle: ∠AOB = 2∠APB. Substituting ∠AOB = 180°: 180° = 2∠APB ⇒ ∠APB = 180° / 2 = 90°! Historical Significance: Attributed to Thales of Miletus (c. 624 – 546 BCE), this was the very first theorem in recorded history to be established by deductive mathematical proof rather than empirical measurement.",
        "key_points": [
            "Thales' Theorem: Any angle inscribed in a semicircle is strictly a right angle (90°).",
            "Proof Mechanism: Direct application of Theorem 9.7 to a straight central angle: ∠APB = 1/2(180°) = 90°.",
            "Converse of Thales' Theorem: If a triangle has a 90° angle, its hypotenuse is the diameter of its circumcircle.",
            "Right Triangle Drafting: A carpenter's square or protractor can instantly locate a circle's diameter by placing the 90° corner on the rim.",
            "Historical Milestone: Marks the historical birth of deductive geometry with Thales of Miletus in ancient Greece."
        ],
        "narration": "What happens when you draw a triangle inside a semicircle where the base is the diameter? No matter WHERE you place the third corner on the curve, the angle is ALWAYS exactly 90 degrees! This famous result was discovered by Thales of Miletus over 2,500 years ago—the very first mathematical proof in human history!",
        "sim_title": "Thales' Semicircle 90° Right-Angle Explorer",
        "checkpoints": [
            {
                "q": "In a circle with diameter AB, point P lies on the circumference. What is the measure of ∠APB?",
                "options": ["45°", "60°", "90°", "180°"],
                "ans": 2,
                "exp": "By Thales' Theorem (angle in a semicircle), diameter AB subtends a 180° straight angle at the centre, so the inscribed angle ∠APB = 180° / 2 = 90°."
            },
            {
                "q": "If a right-angled triangle △ABC with ∠B = 90° is inscribed in a circle, which side of the triangle is the diameter of the circle?",
                "options": ["Side AB", "Side BC", "Hypotenuse AC", "None of them"],
                "ans": 2,
                "exp": "By the converse of Thales' Theorem, the side opposite the 90° angle (the hypotenuse AC) must be the diameter of the circumcircle."
            }
        ]
    },
    {
        "id": 13,
        "title": "Cyclicity of Points & 4-Point Concyclicity Conditions",
        "subtitle": "Concyclic Points Definition, The Equal Subtended Angle Test & Circumcircle Testing",
        "category": "Cyclic Geometry",
        "badge": "CG-4 • C-7.3 • Concyclic Points",
        "summary": "In geometry, four or more points are defined to be Concyclic if they all lie on the circumference of the same single circle. While any three non-collinear points are always concyclic (Slide 3), a fourth point D is NOT guaranteed to lie on that circle! When is a set of four points concyclic? Theorem (Concyclicity Criterion): 'If a line segment joining two points subtends equal angles at two other points lying on the same side of the line containing the segment, then the four points are concyclic.' That is, if points C and D lie on the same side of line AB, and ∠ACB = ∠ADB, then points A, B, C, D all lie on a common circle! Proof by contradiction: If D does not lie on the circle through A, B, C, let the circle intersect line segment AD at D'. Then ∠ACD' = ∠ACB = ∠ADB, which forces an exterior angle of △CDD' to equal its interior opposite angle—an impossible contradiction unless D coincides with D'!",
        "key_points": [
            "Concyclic Definition: A set of points that lie on the perimeter of a single common circle.",
            "Subtended Angle Test: If segment AB subtends equal angles at C and D on the same side (∠ACB = ∠ADB), then A, B, C, D are concyclic.",
            "Proof by Contradiction: Assuming point D lies inside or outside the circle leads to an impossible exterior angle contradiction.",
            "Contrast with 3 Points: 3 non-collinear points always define a circle; 4 points require a strict angular constraint.",
            "Orthogonal Concyclicity: If ∠ACB = 90° and ∠ADB = 90°, AB is a diameter and all 4 points are automatically concyclic."
        ],
        "narration": "What does it mean for points to be concyclic? It means they all sit happily on the same circle! Any three points always have a circle, but what about four points? If line segment AB makes the EXACT same angle at point C and point D on the same side, then all four points are guaranteed to be concyclic!",
        "sim_title": "4-Point Concyclicity Detector & Circumcircle Snapper",
        "checkpoints": [
            {
                "q": "Points C and D lie on the same side of line segment AB such that ∠ACB = 50° and ∠ADB = 50°. Are points A, B, C, D concyclic?",
                "options": [
                    "Yes, because line segment AB subtends equal angles at C and D on the same side",
                    "No, because the angles must be 90°",
                    "Only if AB is horizontal",
                    "Cannot be determined without side lengths"
                ],
                "ans": 0,
                "exp": "By the Concyclicity Criterion, if a line segment subtends equal angles at two points lying on the same side of the line, the four points lie on the same circle."
            },
            {
                "q": "In △ABC, altitudes BD and CE are drawn to opposite sides AC and AB. Why are points B, C, D, E concyclic?",
                "options": [
                    "Because segment BC subtends right angles at both D and E (∠BDC = ∠BEC = 90°)",
                    "Because all altitudes are equal",
                    "Because triangle ABC must be equilateral",
                    "By the Midpoint Theorem"
                ],
                "ans": 0,
                "exp": "Segment BC subtends equal 90° angles at points D and E on the same side of BC. Hence B, C, D, E are concyclic with BC as diameter."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cyclic Quadrilaterals & Supplementary Opposite Angles (Theorems 9.9 & 9.10)",
        "subtitle": "Opposite Angles Sum to 180° & The Exterior Angle Corollary",
        "category": "Cyclic Geometry",
        "badge": "CG-4 • C-7.3 • Theorems 9.9 & 9.10",
        "summary": "A quadrilateral ABCD is called a Cyclic Quadrilateral if all four of its vertices lie on a circle. Theorem 9.9 states: 'The sum of either pair of opposite angles of a cyclic quadrilateral is 180°' (∠A + ∠C = 180° and ∠B + ∠D = 180°). Proof: Let ABCD be cyclic. Minor arc BCD subtends angle ∠BOD = α at the centre. Major arc BAD subtends reflex angle reflex-∠BOD = β at the centre. The complete angle around centre O is α + β = 360°. By Theorem 9.7, inscribed angle ∠A = 1/2 α, and inscribed angle ∠C = 1/2 β. Adding them: ∠A + ∠C = 1/2(α + β) = 1/2(360°) = 180°! Similarly, ∠B + ∠D = 180°. Theorem 9.10 is the Converse: 'If the sum of a pair of opposite angles of a quadrilateral is 180°, then the quadrilateral is cyclic.' Exterior Angle Corollary: If one side of a cyclic quadrilateral is extended, the exterior angle is equal to the interior opposite angle!",
        "key_points": [
            "Theorem 9.9: In a cyclic quadrilateral, opposite angles are supplementary (∠A + ∠C = 180° and ∠B + ∠D = 180°).",
            "Proof via Central Angles: ∠A + ∠C = 1/2(α + β) = 1/2(360°) = 180°.",
            "Theorem 9.10 (Converse): If opposite angles sum to 180°, the quadrilateral is cyclic.",
            "Exterior Angle Rule: Exterior angle at any vertex equals the interior opposite angle.",
            "Fundamental Test: Used in structural engineering and geometry to verify when a frame can be inscribed in a ring."
        ],
        "narration": "A cyclic quadrilateral is a four-sided shape whose corners all touch a circle. And here is its magical property: opposite angles ALWAYS add up to 180 degrees! If angle A is 80 degrees, opposite angle C MUST be 100 degrees! And if you extend any side, the outside angle equals the opposite inside angle!",
        "sim_title": "Cyclic Quadrilateral Opposite Angle Balancer & Exterior Angle Lab",
        "checkpoints": [
            {
                "q": "In a cyclic quadrilateral ABCD, ∠A = 70°. What is the measure of the opposite angle ∠C?",
                "options": ["70°", "110°", "140°", "290°"],
                "ans": 1,
                "exp": "By Theorem 9.9, opposite angles of a cyclic quadrilateral are supplementary: ∠A + ∠C = 180° ⇒ ∠C = 180° - 70° = 110°."
            },
            {
                "q": "One side AB of a cyclic quadrilateral ABCD is extended to point E. If interior opposite angle ∠D = 105°, what is exterior angle ∠CBE?",
                "options": ["75°", "90°", "105°", "180°"],
                "ans": 2,
                "exp": "By the Exterior Angle Corollary of cyclic quadrilaterals, the exterior angle at vertex B equals the interior opposite angle: ∠CBE = ∠D = 105°."
            }
        ]
    },
    {
        "id": 15,
        "title": "Cyclic Quadrilaterals: Special Shapes & Ptolemy's Theorem",
        "subtitle": "Cyclic Parallelograms Are Rectangles, Cyclic Rhombuses Are Squares & Isosceles Trapeziums",
        "category": "Cyclic Geometry",
        "badge": "CG-4 • C-7.3 • Special Cyclic 4-gons",
        "summary": "Applying circle cyclicity constraints to special 4-gons yields surprising geometric restrictions: 1. Cyclic Parallelogram is a Rectangle: In a parallelogram, opposite angles are equal (∠A = ∠C). In a cyclic quadrilateral, opposite angles are supplementary (∠A + ∠C = 180°). Combining them: 2∠A = 180° ⇒ ∠A = 90°! Since a parallelogram with one right angle is a rectangle, every cyclic parallelogram MUST be a rectangle! 2. Cyclic Rhombus is a Square: A rhombus is a parallelogram; being cyclic forces all angles to be 90°, making it a square! 3. Cyclic Trapezium is an Isosceles Trapezium: If a trapezium ABCD (AB ∥ CD) is cyclic, its non-parallel sides are equal (AD = BC), and its diagonals are equal (AC = BD). 4. Ptolemy's Theorem (Historical Jewel): For any cyclic quadrilateral ABCD, the product of the diagonals equals the sum of the products of opposite sides: AC · BD = AB · CD + BC · AD.",
        "key_points": [
            "Cyclic Parallelogram Theorem: Every cyclic parallelogram is strictly a rectangle (∠A = ∠C and ∠A + ∠C = 180° ⇒ ∠A = 90°).",
            "Cyclic Rhombus: Every cyclic rhombus is strictly a square.",
            "Cyclic Trapezium: If a trapezium is cyclic, it must be an isosceles trapezium (AD = BC and AC = BD).",
            "Ptolemy's Theorem: AC · BD = (AB · CD) + (BC · AD) for any cyclic quadrilateral.",
            "Geometric Rigor: Circles eliminate the shear degree of freedom from parallelograms."
        ],
        "narration": "What happens when you force a parallelogram inside a circle? It cannot slant! Because opposite angles must be equal AND add up to 180 degrees, each angle is locked at 90 degrees. That means every cyclic parallelogram is automatically a rectangle! And any cyclic trapezium must be an isosceles trapezium with equal diagonals!",
        "sim_title": "Special Cyclic Shapes Morphing Lab & Ptolemy's Calculator",
        "checkpoints": [
            {
                "q": "Prove that every cyclic parallelogram must be a rectangle. What is the core reasoning?",
                "options": [
                    "Opposite angles are equal (∠A = ∠C) and supplementary (∠A + ∠C = 180°), forcing each angle to be 90°",
                    "All parallelograms are already rectangles",
                    "Because radii bisect each other",
                    "By the Midpoint Theorem"
                ],
                "ans": 0,
                "exp": "In a parallelogram, ∠A = ∠C. In a cyclic 4-gon, ∠A + ∠C = 180°. Substituting gives 2∠A = 180° ⇒ ∠A = 90°. A parallelogram with a 90° angle is a rectangle."
            },
            {
                "q": "If a trapezium ABCD with AB ∥ CD is inscribed in a circle, what can be deduced about its non-parallel legs AD and BC?",
                "options": ["AD = 2 BC", "AD = BC (Isosceles Trapezium)", "AD ⊥ BC", "Cannot be determined"],
                "ans": 1,
                "exp": "A cyclic trapezium is always an isosceles trapezium; its non-parallel legs are equal in length (AD = BC) and its diagonals are equal (AC = BD)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Circle Algorithms & Forward Deduction Engine",
        "subtitle": "Algorithmic Rule Chaining, Cyclic Verification Pipelines & Fast Geometry Solvers",
        "category": "Computational Thinking",
        "badge": "CG-4 • C-7.3 • CG-9 • Computational Thinking",
        "summary": "How do CAD engines, GPS satellites, and computer vision algorithms solve circle geometry? 1. Automated Forward-Chaining Deduction Engine: A computational geometry pipeline applies production rules iteratively: - Rule 1 (Central Angle): If arc AB subtends ∠AOB at center, set inscribed angle = ∠AOB / 2. - Rule 2 (Same Segment): If P, Q in same segment of AB, set ∠APB = ∠AQB. - Rule 3 (Thales): If chord is diameter, set subtended angle = 90°. - Rule 4 (Cyclic 4-gon): If ABCD cyclic, set opposite angle sum = 180°. - Rule 5 (Chord Distance): d = √(r² - (L/2)²). 2. Concyclicity Matrix Determinant: Four points (x_i, y_i) are concyclic if and only if the 4×4 determinant of [x_i² + y_i², x_i, y_i, 1] equals 0! This allows a computer to test whether 4 GPS receivers lie on a circle in O(1) time.",
        "key_points": [
            "Rule-Based Deduction: Forward chaining applies circle theorems step-by-step until all unknown angles and lengths are solved.",
            "Determinant Concyclicity Test: A 4×4 matrix determinant evaluates whether 4 Cartesian points are concyclic in O(1) operations.",
            "CAD Circle Solvers: Computer graphics uses parametric circle equations (x = r cos θ, y = r sin θ) for sub-pixel ray tracing.",
            "Decomposition & Pattern Recognition: Breaking complex multi-chord circle puzzles into elementary cyclic triangles.",
            "Algorithmic Verification: Systematic theorem checks eliminate geometric contradictions."
        ],
        "narration": "Let's bring it all together with Computational Thinking! How do GPS navigation systems and computer vision detect circles and verify angles? We can program a forward-chaining deduction engine that applies our circle theorems step-by-step: Central Angle Rule, Same Segment Rule, Thales' 90° Rule, and Cyclic Quadrilateral Rule! Watch the algorithm solve complex circle puzzles automatically.",
        "sim_title": "Interactive Circle Theorem Inference Engine & Algorithmic Solver",
        "checkpoints": [
            {
                "q": "What is the computational role of a forward-chaining inference engine in circle geometry software?",
                "options": [
                    "To draw circles using random pixels",
                    "To systematically apply proven geometric rules step-by-step to deduce all unknown angles and chord lengths from given inputs",
                    "To calculate the value of π to a billion digits",
                    "To convert 2D circles into 3D spheres"
                ],
                "ans": 1,
                "exp": "A forward-chaining deduction engine matches known facts against geometric theorems (rules) to iteratively infer new angle and length values until the problem is solved."
            },
            {
                "q": "In a computer algorithm, what is the fastest test to verify whether a given chord passes through the centre of a circle of radius r?",
                "options": [
                    "Check if the perpendicular distance from the centre d equals 0 (or chord length L equals 2r)",
                    "Rotate the circle 100 times",
                    "Measure the area of the entire screen",
                    "Draw 50 random chords"
                ],
                "ans": 0,
                "exp": "Testing if d = 0 (or equivalently L = 2r) takes a single O(1) numerical comparison, instantly verifying that the chord is a diameter."
            }
        ]
    }
]

QUIZZES = [
    {
        "slide_id": 17,
        "title": "Mastery Quiz 1: Circle Definitions, Anatomy & Chords",
        "subtitle": "Radii, Chords, Subtended Angles & Theorems 9.1 and 9.2",
        "category": "Mastery Challenge",
        "badge": "Quiz 1 • Circle Foundations",
        "questions": [
            {
                "q": "What is the longest possible chord in a circle of radius r?",
                "options": ["Radius r", "Diameter 2r", "Circumference 2πr", "Chord of length r√2"],
                "ans": 1,
                "exp": "The longest chord of any circle passes through its centre and has length 2r, which is the diameter."
            },
            {
                "q": "In a circle with centre O, chord AB = 10 cm and subtends a central angle of 60°. What is the radius of the circle?",
                "options": ["5 cm", "10 cm", "15 cm", "20 cm"],
                "ans": 1,
                "exp": "In △AOB, OA = OB = r (radii), so ∠OAB = ∠OBA = (180° - 60°)/2 = 60°. Thus △AOB is equilateral! Therefore radius r = AB = 10 cm."
            },
            {
                "q": "Two equal chords AB and CD of a circle with centre O subtend central angles of ∠AOB and ∠COD. If ∠AOB = 75°, what is ∠COD?",
                "options": ["37.5°", "75°", "105°", "150°"],
                "ans": 1,
                "exp": "By Theorem 9.1, equal chords subtend equal angles at the centre. Therefore, ∠COD = ∠AOB = 75°."
            },
            {
                "q": "What is the geometric region enclosed between two radii and their corresponding arc called?",
                "options": ["Segment", "Sector", "Chord", "Secant"],
                "ans": 1,
                "exp": "A sector is the region bounded by two radii and the arc between them (like a slice of pizza)."
            },
            {
                "q": "A chord of length 16 cm is drawn in a circle of radius 10 cm. How many such 16 cm chords can be drawn in this circle?",
                "options": ["Exactly 1", "Exactly 2", "Infinitely many", "None"],
                "ans": 2,
                "exp": "Infinitely many chords of length 16 cm can be drawn by choosing any point on the circumference as the starting point; all will be tangent to a concentric circle of radius 6 cm."
            },
            {
                "q": "If a line intersects a circle at two distinct points, the line is called a:",
                "options": ["Tangent", "Secant", "Radius", "Normal"],
                "ans": 1,
                "exp": "A secant is a straight line that cuts or intersects a circle in two distinct points."
            },
            {
                "q": "Which congruence criterion proves Theorem 9.2 (chords subtending equal angles at centre are equal)?",
                "options": ["SSS", "SAS", "RHS", "AAS"],
                "ans": 1,
                "exp": "In △AOB and △COD: OA = OC (radii), included angle ∠AOB = ∠COD (given), and OB = OD (radii). They are congruent by SAS, so AB = CD by CPCTC."
            },
            {
                "q": "A circle divides the plane on which it lies into how many parts?",
                "options": ["1 part", "2 parts", "3 parts", "4 parts"],
                "ans": 2,
                "exp": "A circle partitions the plane into 3 disjoint parts: the interior (inside), the circle itself (boundary), and the exterior (outside)."
            },
            {
                "q": "If an arc of a circle is less than a semicircle, it is called a:",
                "options": ["Minor arc", "Major arc", "Chord", "Sector"],
                "ans": 0,
                "exp": "An arc smaller than half the circumference is called a minor arc. An arc larger than half is a major arc."
            },
            {
                "q": "In a circle with centre O, chords AB and CD are such that AB = 12 cm and CD = 12 cm. If distance of AB from O is 5 cm, what is distance of CD from O?",
                "options": ["2.5 cm", "5 cm", "10 cm", "12 cm"],
                "ans": 1,
                "exp": "By Theorem 9.5, equal chords are equidistant from the centre. Since AB = CD = 12 cm, both chords are at distance 5 cm from O."
            }
        ]
    },
    {
        "slide_id": 18,
        "title": "Mastery Quiz 2: Circumcentre & Chord Distance Theorems",
        "subtitle": "Theorems 9.3 through 9.6, Pythagoras & Circumcircle Properties",
        "category": "Mastery Challenge",
        "badge": "Quiz 2 • Distances & Circumcentre",
        "questions": [
            {
                "q": "A perpendicular from the centre of a circle of radius 17 cm is drawn to a chord, meeting it at distance 8 cm. What is the length of the chord?",
                "options": ["15 cm", "20 cm", "30 cm", "34 cm"],
                "ans": 2,
                "exp": "By Pythagoras, half-chord = √(17² - 8²) = √(289 - 64) = √225 = 15 cm. The total chord length is 2 × 15 cm = 30 cm."
            },
            {
                "q": "Where does the circumcentre of an obtuse-angled triangle lie?",
                "options": ["Inside the triangle", "At the midpoint of the longest side", "Outside the triangle", "At the obtuse vertex"],
                "ans": 2,
                "exp": "For an obtuse-angled triangle, the perpendicular bisectors of the sides intersect in the exterior, strictly outside the triangle."
            },
            {
                "q": "A chord of length 30 cm is at a distance of 8 cm from the centre of a circle. What is the radius of the circle?",
                "options": ["15 cm", "17 cm", "19 cm", "23 cm"],
                "ans": 1,
                "exp": "Half-chord = 30 / 2 = 15 cm. Radius r = √(d² + (L/2)²) = √(8² + 15²) = √(64 + 225) = √289 = 17 cm."
            },
            {
                "q": "In a right-angled triangle with sides 5 cm, 12 cm, and 13 cm, what is the circumradius?",
                "options": ["2.5 cm", "6 cm", "6.5 cm", "13 cm"],
                "ans": 2,
                "exp": "The circumcentre of a right triangle is the midpoint of the hypotenuse (13 cm). Circumradius R = 13 / 2 = 6.5 cm."
            },
            {
                "q": "Theorem 9.3 states that the perpendicular from the centre to a chord bisects the chord. Which congruence criterion proves this?",
                "options": ["RHS", "SAS", "ASA", "SSS"],
                "ans": 0,
                "exp": "In right triangles △OMA and △OMB: right angles at M, common leg OM, and hypotenuses OA = OB = r. Thus congruent by RHS, giving AM = MB."
            },
            {
                "q": "Two parallel chords of length 6 cm and 8 cm are drawn on the same side of the centre of a circle of radius 5 cm. What is the distance between the two chords?",
                "options": ["1 cm", "2 cm", "3 cm", "4 cm"],
                "ans": 0,
                "exp": "Distance of 8 cm chord: d₁ = √(5² - 4²) = 3 cm. Distance of 6 cm chord: d₂ = √(5² - 3²) = 4 cm. Since they are on the same side: distance = d₂ - d₁ = 4 - 3 = 1 cm."
            },
            {
                "q": "If the two parallel chords of length 6 cm and 8 cm were on OPPOSITE sides of the centre in the same circle (radius 5 cm), what would be the distance between them?",
                "options": ["1 cm", "5 cm", "7 cm", "8 cm"],
                "ans": 2,
                "exp": "On opposite sides, their distances from the centre add up: distance = d₁ + d₂ = 3 cm + 4 cm = 7 cm."
            },
            {
                "q": "How many non-collinear points are required to uniquely determine a circle?",
                "options": ["1", "2", "3", "4"],
                "ans": 2,
                "exp": "By Theorem 9.5, exactly three non-collinear points uniquely determine one and only one circle."
            },
            {
                "q": "In a circle of radius r, if chord AB has length r, what is the perpendicular distance of AB from the centre?",
                "options": ["r / 2", "(r√3) / 2", "r / √2", "r√3"],
                "ans": 1,
                "exp": "Half-chord = r/2. Distance d = √(r² - (r/2)²) = √(r² - r²/4) = √(3r²/4) = (r√3)/2."
            },
            {
                "q": "What happens to the perpendicular distance d of a chord from the centre as the chord length L increases?",
                "options": [
                    "Distance d increases",
                    "Distance d decreases",
                    "Distance d remains constant",
                    "Distance d doubles"
                ],
                "ans": 1,
                "exp": "Since d² + (L/2)² = r² (a constant), as chord length L increases, distance d must strictly decrease (longer chords are closer to the centre)."
            }
        ]
    },
    {
        "slide_id": 19,
        "title": "Mastery Quiz 3: Subtended Angles & Semicircle Theorems",
        "subtitle": "Theorems 9.7 & 9.8, Thales' Theorem & Inscribed Angles",
        "category": "Mastery Challenge",
        "badge": "Quiz 3 • Inscribed Angles",
        "questions": [
            {
                "q": "An arc subtends an angle of 130° at the centre of a circle. What is the angle subtended by it at any point on the remaining part of the circle?",
                "options": ["65°", "75°", "130°", "260°"],
                "ans": 0,
                "exp": "By Theorem 9.7, inscribed angle = 1/2 × central angle = 1/2 × 130° = 65°."
            },
            {
                "q": "In a circle with centre O, diameter AB subtends angle ∠APB at point P on the circumference. What is ∠APB?",
                "options": ["45°", "60°", "90°", "180°"],
                "ans": 2,
                "exp": "By Thales' Theorem (angle in a semicircle), the angle subtended by a diameter at any point on the semicircle is strictly 90°."
            },
            {
                "q": "If points P, Q, R lie in the same segment of chord AB and ∠APB = 52°, what is ∠AQB?",
                "options": ["26°", "52°", "104°", "128°"],
                "ans": 1,
                "exp": "By Theorem 9.8, angles in the same segment of a circle are equal. Thus ∠AQB = ∠APB = 52°."
            },
            {
                "q": "In a circle with centre O, △ABC is inscribed with ∠BOC = 120°. What is the measure of ∠BAC?",
                "options": ["30°", "60°", "120°", "240°"],
                "ans": 1,
                "exp": "Arc BC subtends central angle ∠BOC = 120° and inscribed angle ∠BAC at vertex A. By Theorem 9.7: ∠BAC = 1/2 × 120° = 60°."
            },
            {
                "q": "In a circle with centre O, chord AB subtends ∠AOB = 100°. If P is on the minor arc AB, what is ∠APB?",
                "options": ["50°", "80°", "100°", "130°"],
                "ans": 3,
                "exp": "Reflex central angle subtended by major arc AB = 360° - 100° = 260°. By Theorem 9.7, inscribed angle ∠APB = 1/2 × 260° = 130°."
            },
            {
                "q": "In △ABC inscribed in a circle, AB is a diameter. If ∠ABC = 35°, what is the measure of ∠BAC?",
                "options": ["35°", "55°", "70°", "90°"],
                "ans": 1,
                "exp": "Since AB is diameter, ∠ACB = 90° (Thales' theorem). By angle sum: ∠BAC = 180° - (90° + 35°) = 55°."
            },
            {
                "q": "If an inscribed angle ∠APB = 90°, what conclusion can be drawn about segment AB?",
                "options": [
                    "AB is a tangent to the circle",
                    "AB is a diameter of the circle",
                    "AB is equal to the radius",
                    "AB is perpendicular to the radius at P"
                ],
                "ans": 1,
                "exp": "By the converse of Thales' Theorem, any chord that subtends a 90° angle on the circumference is a diameter of the circle."
            },
            {
                "q": "Two chords AC and BD of a circle intersect at E. If ∠BEC = 130° and ∠ECD = 20°, what is ∠BAC?",
                "options": ["20°", "70°", "110°", "130°"],
                "ans": 2,
                "exp": "In △CDE, exterior angle ∠BEC = ∠EDC + ∠ECD ⇒ 130° = ∠EDC + 20° ⇒ ∠EDC = 110°. Since ∠BAC and ∠BDC (∠EDC) are in the same segment of chord BC, ∠BAC = ∠BDC = 110°."
            },
            {
                "q": "If an equilateral triangle is inscribed in a circle with centre O, what is the central angle subtended by each side?",
                "options": ["60°", "90°", "120°", "180°"],
                "ans": 2,
                "exp": "The 3 equal sides divide the circle into 3 equal arcs. Each central angle = 360° / 3 = 120° (and inscribed angle = 120°/2 = 60°)."
            },
            {
                "q": "Who is historically credited with the first recorded deductive proof in geometry (proving that the angle in a semicircle is a right angle)?",
                "options": ["Pythagoras", "Euclid", "Thales of Miletus", "Archimedes"],
                "ans": 2,
                "exp": "Thales of Miletus (c. 600 BCE) is credited with establishing the first known deductive proof in human history for this theorem."
            }
        ]
    },
    {
        "slide_id": 20,
        "title": "Mastery Quiz 4: Concyclicity, Cyclic Quadrilaterals & Applications",
        "subtitle": "Theorems 9.9 & 9.10, Cyclic Parallelograms & Cultural Chakras",
        "category": "Mastery Challenge",
        "badge": "Quiz 4 • Cyclic Quadrilaterals",
        "questions": [
            {
                "q": "In a cyclic quadrilateral ABCD, ∠B = 82°. What is the measure of the opposite angle ∠D?",
                "options": ["82°", "98°", "108°", "164°"],
                "ans": 1,
                "exp": "By Theorem 9.9, opposite angles of a cyclic quadrilateral are supplementary: ∠B + ∠D = 180° ⇒ ∠D = 180° - 82° = 98°."
            },
            {
                "q": "If a parallelogram is cyclic (inscribed in a circle), what specific geometric shape must it be?",
                "options": ["Rhombus", "Rectangle", "Kite", "Trapezium"],
                "ans": 1,
                "exp": "In a parallelogram, ∠A = ∠C. In a cyclic 4-gon, ∠A + ∠C = 180°. Thus 2∠A = 180° ⇒ ∠A = 90°. A parallelogram with a 90° angle is a rectangle."
            },
            {
                "q": "One side of a cyclic quadrilateral is extended. The exterior angle formed is always equal to:",
                "options": [
                    "The adjacent interior angle",
                    "The interior opposite angle",
                    "90 degrees",
                    "Half the central angle"
                ],
                "ans": 1,
                "exp": "By the Exterior Angle Corollary, the exterior angle of a cyclic quadrilateral equals its interior opposite angle."
            },
            {
                "q": "In cyclic quadrilateral ABCD, side AB is extended to E. If ∠CBE = 78°, what is the measure of angle ∠ADC?",
                "options": ["78°", "102°", "156°", "180°"],
                "ans": 0,
                "exp": "Exterior angle ∠CBE equals the interior opposite angle ∠ADC. Thus ∠ADC = 78°."
            },
            {
                "q": "If the sum of a pair of opposite angles of a quadrilateral is 180°, what can be deduced about the quadrilateral?",
                "options": [
                    "It is a rectangle",
                    "It is cyclic (its vertices lie on a circle)",
                    "It has perpendicular diagonals",
                    "Its area is zero"
                ],
                "ans": 1,
                "exp": "By Theorem 9.10 (Converse), if the sum of a pair of opposite angles of a quadrilateral is 180°, the quadrilateral is cyclic."
            },
            {
                "q": "A cyclic rhombus is always a:",
                "options": ["Square", "Rectangle only", "Kite", "Non-square rhombus"],
                "ans": 0,
                "exp": "A rhombus is a parallelogram. Being cyclic forces its angles to be 90° (a rectangle). A rhombus with 90° angles is a square."
            },
            {
                "q": "If a trapezium ABCD (AB ∥ CD) is cyclic, what is TRUE about its non-parallel sides AD and BC?",
                "options": ["AD = 2 BC", "AD = BC (It is an isosceles trapezium)", "AD ⊥ BC", "They are parallel"],
                "ans": 1,
                "exp": "Any cyclic trapezium is an isosceles trapezium; its non-parallel sides are equal (AD = BC) and its diagonals are equal (AC = BD)."
            },
            {
                "q": "In cyclic quadrilateral ABCD, diagonals AC and BD intersect at E. If ∠DBC = 55° and ∠BAC = 45°, what is ∠BCD?",
                "options": ["55°", "80°", "100°", "125°"],
                "ans": 1,
                "exp": "∠DAC and ∠DBC are in the same segment of chord CD, so ∠DAC = ∠DBC = 55°. Thus ∠DAB = ∠DAC + ∠BAC = 55° + 45° = 100°. Opposite angles sum to 180°: ∠BCD = 180° - 100° = 80°."
            },
            {
                "q": "Ptolemy's Theorem states that for any cyclic quadrilateral ABCD, the product of diagonals AC · BD equals:",
                "options": [
                    "AB · BC + CD · DA",
                    "AB · CD + BC · AD",
                    "AB² + CD²",
                    "Radius squared"
                ],
                "ans": 1,
                "exp": "Ptolemy's Theorem states: AC · BD = (AB · CD) + (BC · AD) (the product of diagonals equals the sum of the products of opposite sides)."
            },
            {
                "q": "What is the angle between any two adjacent spokes in the 24-spoke Ashoka Chakra?",
                "options": ["10°", "12°", "15°", "24°"],
                "ans": 2,
                "exp": "A full circle has 360°. With 24 spokes evenly spaced, the angle between adjacent spokes is 360° / 24 = 15°."
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


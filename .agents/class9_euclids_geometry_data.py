"""
Data module for Class 9 Mathematics Chapter 7: Introduction to Euclid's Geometry: Axioms and Postulates
Syllabus: CG-7, C-7.1, C-7.3
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

import json

SLIDES = [
    {
        "id": 1,
        "title": "Practical Origins of Geometry & Ancient Civilisations",
        "subtitle": "Land Surveying, River Nile Floods & The Roots of Measurement",
        "category": "Historical Origins",
        "badge": "CG-7 • C-7.1 • Ancient Origins",
        "summary": "The word 'Geometry' originates from the Greek words 'Geo' (meaning Earth) and 'Metrein' or 'Metron' (meaning to measure). In ancient times, geometry developed out of practical necessity rather than abstract theory. In ancient Egypt, annual flooding of the River Nile regularly washed away agricultural boundary marks between farmland plots. The Pharaoh's land surveyors, known as 'harpedonaptai' (rope-stretchers), used knotted measuring ropes to re-establish property boundaries and calculate land areas for taxation. Similarly, building massive monuments, irrigation canals, and pyramids required practical rules for computing lengths, areas, and volumes.",
        "key_points": [
            "Etymology: Greek 'Geo' (Earth) + 'Metrein' (to measure) = measurement of the Earth.",
            "Egyptian origins: Annual River Nile floods necessitated re-surveying boundaries using knotted cords.",
            "Egyptian surveyors were called 'harpedonaptai' (rope-stretchers).",
            "Geometric rules in Egypt, Babylonia, and China were empirical rules of thumb without formal deductive proofs.",
            "Pyramids of Egypt demonstrated early mastery of spatial geometry (square bases, triangular faces meeting at an apex)."
        ],
        "narration": "Welcome to Introduction to Euclid's Geometry! Did you know the word geometry means 'Earth measurement'? Thousands of years ago, annual floods of the River Nile washed away farm boundaries in Egypt. Surveyors with knotted ropes had to measure and redraw the land. Geometry began not as abstract equations, but as a practical necessity!",
        "sim_title": "Nile Flood & Land Re-Surveyor Simulator",
        "checkpoints": [
            {
                "q": "What is the literal meaning of the Greek word 'Geometry'?",
                "options": ["Sky Mapping", "Earth Measurement", "Building Design", "Stone Carving"],
                "ans": 1,
                "exp": "Geometry comes from Greek 'Geo' (Earth) and 'Metrein' (to measure), meaning Earth measurement."
            },
            {
                "q": "What practical necessity drove the early development of geometry in ancient Egypt?",
                "options": [
                    "Re-establishing boundary lines washed away by the annual Nile floods",
                    "Navigating across oceans at night",
                    "Designing mechanical clocks",
                    "Predicting solar eclipses"
                ],
                "ans": 0,
                "exp": "The annual flooding of the River Nile erased boundary markers, requiring surveyors to remeasure farm fields."
            }
        ]
    },
    {
        "id": 2,
        "title": "Geometry in Ancient India: Harappa & Vedic Altars",
        "subtitle": "Town Planning, Standardized Bricks & Sacred Ritual Geometries",
        "category": "Ancient India",
        "badge": "CG-7 • C-7.1 • Indian Contributions",
        "summary": "Excavations at Harappa and Mohenjo-daro (Indus Valley Civilisation, c. 2500 BCE) reveal that ancient India possessed extraordinary geometric town planning: wide streets arranged in parallel grids intersecting at precise right angles, sophisticated underground drainage systems, and standardized kiln-burnt building bricks manufactured in the fixed dimensional ratio of Length : Breadth : Thickness = 4 : 2 : 1. In the later Vedic period (c. 1500–500 BCE), elaborate fire altars ('Vedi') were constructed for sacred religious rituals, demanding exact geometric shapes with strictly preserved areas.",
        "key_points": [
            "Indus Valley Civilisation (c. 2500 BCE): Planned cities with orthogonal street grids intersecting at 90°.",
            "Standardized Harappan brick ratio: Length : Breadth : Thickness = 4 : 2 : 1.",
            "Vedic sacred fire altars ('Vedi') required precise geometric shapes for domestic and public rituals.",
            "Domestic household altars: Square ('Ahavaniya') and Circular ('Garhapatya').",
            "Public altars: Complex shapes such as 'Syenaciti' (falcon/hawk shaped), tortoise, and chariot wheel."
        ],
        "narration": "In ancient India, geometry flourished in town planning and sacred rituals! In Harappa and Mohenjo-daro, streets intersected at precise right angles, and kiln-burnt bricks followed the standard ratio of 4 is to 2 is to 1. In the Vedic period, priests constructed sacred fire altars in shapes of squares, circles, and soaring falcons!",
        "sim_title": "Harappan Standard Brick & City Grid Planner",
        "checkpoints": [
            {
                "q": "What was the standardized dimensional ratio of bricks used in the Harappan Civilisation?",
                "options": ["3 : 2 : 1", "4 : 2 : 1", "5 : 3 : 1", "2 : 2 : 1"],
                "ans": 1,
                "exp": "Harappan bricks were standardized in the dimensional ratio of Length : Breadth : Thickness = 4 : 2 : 1."
            },
            {
                "q": "Which shape was used for the domestic Garhapatya fire altar in Vedic rituals?",
                "options": ["Circular", "Square", "Hexagonal", "Octagonal"],
                "ans": 0,
                "exp": "The Garhapatya altar was circular, whereas the Ahavaniya altar was square; both were required to have equal areas."
            }
        ]
    },
    {
        "id": 3,
        "title": "Baudhayana’s Sulbasutras & Sacred Fire Altars",
        "subtitle": "Rope Geometry, Area Preservation & The Sri Yantra Masterpiece",
        "category": "Vedic Geometry",
        "badge": "CG-7 • C-7.1 • Sulbasutras",
        "summary": "The 'Sulbasutras' (manuals of the cord, c. 800–500 BCE) composed by Baudhayana, Apastamba, Katyayana, and Manava are the oldest known Indian mathematical texts on geometry. The word 'Sulba' means rope or cord, and 'Sutra' means an aphorism. Vedic geometry focused on constructing altars of specific areas: converting a square altar into a circular altar of equal area, doubling a square's area, and designing intricate geometric diagrams like the 'Sri Yantra' consisting of 9 interwoven isosceles triangles producing 43 subordinate triangles.",
        "key_points": [
            "Sulbasutras ('manuals of the cord') are ancient Indian treatises on geometric rope constructions.",
            "Renowned authors: Baudhayana (c. 800 BCE), Apastamba (c. 600 BCE), and Katyayana (c. 200 BCE).",
            "Sacred rule of Vedi: Household altars of different shapes (square, circle, semicircle) must have identical surface area.",
            "The Sri Yantra: 9 interwoven isosceles triangles arranged around a central point (Bindu) creating 43 small triangles.",
            "Anticipated key theorems including the relation between the diagonal and sides of a rectangle."
        ],
        "narration": "The Sulbasutras are ancient Indian texts dedicated to rope geometry! 'Sulba' means rope, which was used like a modern compass and straightedge. Priests had to solve complex challenges, like transforming a square altar into a circle of the exact same area, or constructing the famous Sri Yantra with 9 interwoven triangles!",
        "sim_title": "Vedic Sacred Altar Transformer & Area Balancer",
        "checkpoints": [
            {
                "q": "What does the Sanskrit word 'Sulba' in Sulbasutras mean?",
                "options": ["Fire altar", "Rope or cord", "Stone chisel", "Golden rule"],
                "ans": 1,
                "exp": "'Sulba' means a rope or cord, which was the fundamental tool for geometric constructions in ancient India."
            },
            {
                "q": "How many interwoven isosceles triangles form the ancient geometric diagram known as the Sri Yantra?",
                "options": ["7 triangles", "9 triangles", "12 triangles", "43 triangles"],
                "ans": 1,
                "exp": "The Sri Yantra is formed by 9 interwoven isosceles triangles, which intersect to produce 43 smaller triangles."
            }
        ]
    },
    {
        "id": 4,
        "title": "Constructing a Square in Baudhayana’s Sulbasutras",
        "subtitle": "Rope-and-Peg Algorithm for Erecting Perpendiculars & Baudhayana's Theorem",
        "category": "Sulbasutra Constructions",
        "badge": "CG-7 • C-7.3 • Square Construction",
        "summary": "Baudhayana described an ingenious method to construct a square using only a rope and wooden pegs: To construct a square of side 'a', first stretch a rope of length 'a' along the East-West line (Praci) between pegs A and B. Mark the midpoint. Sweep arcs of radius greater than half with the cord to construct the North-South perpendicular line (Udici). Measure length 'a' along both perpendiculars at A and B, fixing pegs C and D. Connecting the pegs yields a perfect square. Baudhayana also recorded the theorem: 'The rope stretched along the diagonal of a rectangle produces an area equal to the sum of areas produced by its sides.'",
        "key_points": [
            "Baudhayana's Sulbasutra gives the earliest explicit geometric construction of a square using a rope and pegs.",
            "The baseline was aligned with the East-West celestial direction ('Praci').",
            "The perpendicular was erected using intersecting circular cord arcs, creating the North-South axis ('Udici').",
            "Baudhayana's Theorem (pre-dating Pythagoras): The diagonal of a rectangle produces area equal to the sum of areas of both sides.",
            "Diagonal of a square of side a: d² = a² + a² = 2a² ⇒ d = a√2 (Baudhayana gave √2 ≈ 1 + 1/3 + 1/(3×4) - 1/(3×4×34))."
        ],
        "narration": "Let's see how ancient Indian geometers constructed a perfect square using only a rope and pegs! Baudhayana laid out an East-West line called Praci, used intersecting cord arcs to erect the North-South perpendicular called Udici, and tied off four equal sides. Baudhayana also stated that the diagonal of a rectangle produces an area equal to the sum of both sides!",
        "sim_title": "Baudhayana Sulba Rope-and-Peg Square Constructor",
        "checkpoints": [
            {
                "q": "In Baudhayana's Sulbasutra, what was the primary tool used to construct perpendiculars and squares?",
                "options": ["A magnetic compass", "A rope (cord) and wooden pegs", "A calibrated metal ruler", "A protractor"],
                "ans": 1,
                "exp": "Baudhayana's constructions relied entirely on cords (ropes) and pegs driven into the ground."
            },
            {
                "q": "What did Baudhayana's theorem state regarding the diagonal of a rectangle?",
                "options": [
                    "The diagonal is always double the shorter side",
                    "The area produced by the diagonal equals the sum of areas produced by the two sides",
                    "The diagonal divides the rectangle into unequal areas",
                    "The diagonal length is equal to the perimeter"
                ],
                "ans": 1,
                "exp": "Baudhayana stated: 'The rope stretched along the length of the diagonal of a rectangle produces an area which the vertical and horizontal sides make together.'"
            }
        ]
    },
    {
        "id": 5,
        "title": "Greek Geometry: The Transition to Logical Deductive Proofs",
        "subtitle": "Thales of Miletus, Pythagoras & The Birth of Abstract Mathematical Reason",
        "category": "Greek Mathematics",
        "badge": "CG-7 • C-7.1 • Deductive Reasoning",
        "summary": "While ancient Egypt, Babylonia, and India used geometry for practical applications, the Greeks transformed geometry into an abstract, deductive science. Thales of Miletus (c. 624–546 BCE) is universally recognized as the father of deductive geometry: he was the first mathematician to prove mathematical statements logically rather than merely asserting empirical observations. Thales proved that a circle is bisected by its diameter and that angles opposite equal sides of an isosceles triangle are equal. His pupil Pythagoras (c. 570–495 BCE) and his secret brotherhood elevated geometry into a study of pure logical truths.",
        "key_points": [
            "Shift from empirical geometry (Egypt, Babylonia) to deductive mathematical proof (Greece).",
            "Thales of Miletus is credited with the very first recorded mathematical proofs in human history.",
            "Thales' theorems: A circle is bisected by any diameter; base angles of an isosceles triangle are equal.",
            "Pythagoras and his school proved the universal geometric property of right-angled triangles.",
            "Discovery of incommensurable lengths (irrational numbers like √2) forced Greeks to prioritize pure geometry over arithmetic."
        ],
        "narration": "The Greeks brought a revolutionary change to geometry: they demanded proof! Thales of Miletus was the first person in history recorded to logically prove a theorem, showing that a diameter bisects a circle into two equal halves. Geometry moved from measuring fields to discovering timeless logical truths!",
        "sim_title": "Thales' Circle Bisection & Inscribed Angle Theorem Visualizer",
        "checkpoints": [
            {
                "q": "Who is credited with being the first mathematician in history to provide a formal deductive geometric proof?",
                "options": ["Euclid", "Thales of Miletus", "Archimedes", "Aristotle"],
                "ans": 1,
                "exp": "Thales of Miletus (c. 624–546 BCE) is credited with providing the first deductive geometric proofs."
            },
            {
                "q": "Which fundamental theorem did Thales prove regarding circles?",
                "options": [
                    "A circle has an area equal to πr²",
                    "A circle is bisected by any of its diameters",
                    "All chords in a circle have the same length",
                    "A circle cannot be drawn with a rope"
                ],
                "ans": 1,
                "exp": "Thales proved that any diameter divides a circle into two equal congruent halves."
            }
        ]
    },
    {
        "id": 6,
        "title": "Euclid of Alexandria and 'The Elements'",
        "subtitle": "Systematizing Human Knowledge into 13 Books of Pure Deductive Logic",
        "category": "Euclid & Elements",
        "badge": "CG-7 • C-7.1 • The Elements",
        "summary": "Around 300 BCE, Euclid, a Greek mathematician teaching at Alexandria in Egypt, accomplished one of the greatest intellectual feats in human history: he gathered, refined, and logically structured all known geometry of his era into a single master treatise in 13 books called 'The Elements' (Stoicheia). Euclid organized mathematics hierarchically: starting with basic Definitions, self-evident Axioms and Postulates, and then rigorously proving 465 Propositions (theorems) step by step, where every theorem rests strictly on preceding proofs.",
        "key_points": [
            "Euclid of Alexandria (c. 300 BCE) compiled all ancient geometric knowledge into 'The Elements'.",
            "'The Elements' consists of 13 books and is the most influential mathematical textbook ever written.",
            "Book I starts with 23 Definitions, 5 Postulates, and 5 Common Notions (Axioms).",
            "Deductive hierarchy: Undefined Terms → Definitions → Axioms / Postulates → Theorems → Proofs.",
            "Proposition 47 of Book I is Euclid's celebrated proof of the Pythagorean Theorem ('Windmill Proof')."
        ],
        "narration": "Around 300 BCE, Euclid of Alexandria revolutionized mathematics by writing 'The Elements'. He organized geometry into a logical pyramid: starting with basic definitions, axioms, and postulates, and systematically proving 465 theorems! For over two thousand years, 'The Elements' was the ultimate textbook of truth.",
        "sim_title": "Euclid's 13 Books of Elements Explorer & Logic Tree",
        "checkpoints": [
            {
                "q": "How many individual books make up Euclid's master treatise, 'The Elements'?",
                "options": ["5 books", "7 books", "13 books", "23 books"],
                "ans": 2,
                "exp": "Euclid's 'The Elements' is divided into 13 distinct books covering plane geometry, number theory, and 3D solid geometry."
            },
            {
                "q": "What is the correct logical sequence of Euclid's deductive mathematical system?",
                "options": [
                    "Theorems → Proofs → Definitions → Axioms",
                    "Definitions & Axioms → Postulates → Propositions (Theorems) → Proofs",
                    "Calculations → Graphs → Rules → Conjectures",
                    "Experiments → Measurements → Approximations → Rules"
                ],
                "ans": 1,
                "exp": "Euclid begins with definitions, axioms, and postulates, from which propositions (theorems) are proven deductively."
            }
        ]
    },
    {
        "id": 7,
        "title": "Euclid's Definitions & The Need for Undefined Terms",
        "subtitle": "Points, Lines, Surfaces & Why Modern Geometry Accepts Undefined Terms",
        "category": "Definitions",
        "badge": "CG-7 • C-7.1 • Undefined Terms",
        "summary": "In Book I of 'The Elements', Euclid began by giving 23 definitions for basic geometric terms: (1) A point is that which has no part; (2) A line is breadthless length; (3) The ends of a line are points; (4) A straight line is a line which lies evenly with the points on itself; (5) A surface is that which has length and breadth only; (6) The edges of a surface are lines; (7) A plane surface is a surface which lies evenly with straight lines on itself. However, defining 'point' using 'part' requires defining 'part', leading to an endless circular loop. Hence, modern geometry takes Point, Line, and Plane as intuitive 'Undefined Terms'.",
        "key_points": [
            "Dimensional hierarchy: Solid (3D) → Surface (2D) → Line (1D) → Point (0D).",
            "A solid has shape, size, position, and can be moved; its boundaries are surfaces (2D).",
            "The boundaries of surfaces are lines (1D); the boundaries of lines are points (0D).",
            "Circular definitions: Attempting to define every word leads to an infinite circular chain of definitions.",
            "Modern resolution: Point, Line, and Plane are accepted as foundational Undefined Terms with intuitive physical representations."
        ],
        "narration": "Euclid defined a point as 'that which has no part' and a line as 'breadthless length'. But wait! What is a 'part'? What is 'breadth'? If we try to define every word, we end up in an infinite loop! That's why in modern mathematics, we accept point, line, and plane as intuitive undefined terms.",
        "sim_title": "Dimensional Hierarchy & Boundary Peeler Simulator",
        "checkpoints": [
            {
                "q": "How did Euclid define a 'point' in Book I of The Elements?",
                "options": [
                    "A tiny dot on paper",
                    "That which has no part",
                    "The intersection of two circles",
                    "A unit of length"
                ],
                "ans": 1,
                "exp": "Euclid's Definition 1 states: 'A point is that which has no part.'"
            },
            {
                "q": "Why does modern mathematics treat Point, Line, and Plane as 'Undefined Terms'?",
                "options": [
                    "Because mathematicians do not know what they mean",
                    "To prevent an endless circular chain of definitions",
                    "Because they cannot be drawn on paper",
                    "Because they only exist in three dimensions"
                ],
                "ans": 1,
                "exp": "To define a term, we must use simpler terms. To avoid infinite circular definitions, foundational terms like point and line are left undefined."
            }
        ]
    },
    {
        "id": 8,
        "title": "Axioms vs. Postulates: Self-Evident Truths",
        "subtitle": "Universal Assumptions in Mathematics vs. Domain-Specific Geometric Rules",
        "category": "Axioms & Postulates",
        "badge": "CG-7 • C-7.1 • Axioms vs Postulates",
        "summary": "Euclid divided his foundational unproven assumptions into two distinct categories: (1) Postulates: Assumptions that are specific strictly to geometry (e.g. drawing straight lines, describing circles, equality of right angles). (2) Axioms (Common Notions): Assumptions that are common and self-evidently true across ALL branches of mathematics, including arithmetic, algebra, and geometry (e.g. 'the whole is greater than the part'). Today, the terms 'axiom' and 'postulate' are often used interchangeably, representing statements accepted as true without proof.",
        "key_points": [
            "Axioms (Common Notions): Universal self-evident mathematical truths applied across arithmetic, algebra, and geometry.",
            "Postulates: Specific assumptions tied exclusively to geometric constructions and figures.",
            "Neither axioms nor postulates are proven; they are the starting rules of the mathematical game.",
            "Theorems: Mathematical propositions whose truth is established through rigorous deductive logic using axioms.",
            "In modern mathematics, axioms and postulates are regarded as synonymous starting premises."
        ],
        "narration": "What is the difference between an axiom and a postulate? In Euclid's world, an axiom is a universal truth used throughout all mathematics, like 'the whole is greater than the part'. A postulate is an assumption specific only to geometry, like 'you can draw a circle with any center and radius'!",
        "sim_title": "Axiom vs. Postulate Categorizer & Truth Balancer",
        "checkpoints": [
            {
                "q": "In Euclid's geometry, how does a Postulate differ from an Axiom?",
                "options": [
                    "Postulates are proven while Axioms are unproven",
                    "Postulates are specific to geometry, while Axioms apply across all mathematics",
                    "Axioms are only for triangles, while Postulates are for circles",
                    "Postulates are written in Latin, while Axioms are in Greek"
                ],
                "ans": 1,
                "exp": "Postulates are assumptions specific to geometry, whereas Axioms (Common Notions) are universal mathematical truths."
            },
            {
                "q": "Which of the following is an example of an Axiom rather than a Postulate?",
                "options": [
                    "A circle can be described with any center and radius",
                    "All right angles are equal to one another",
                    "If equals are added to equals, the wholes are equal",
                    "A straight line can be drawn from any point to any other point"
                ],
                "ans": 2,
                "exp": "'If equals are added to equals, the wholes are equal' applies to numbers, algebra, and geometry, making it a universal Axiom."
            }
        ]
    },
    {
        "id": 9,
        "title": "Euclid's 7 Common Notions (Axioms)",
        "subtitle": "Transitivity, Addition, Subtraction, Superposition & The Whole vs. Part",
        "category": "Axioms",
        "badge": "CG-7 • C-7.1 • 7 Common Notions",
        "summary": "Euclid listed 5 Common Notions in Book I, which commentators expanded to 7 fundamental axioms: (1) Things equal to the same thing are equal to one another (Transitivity: a = c and b = c ⇒ a = b); (2) If equals are added to equals, the wholes are equal (a = b ⇒ a + c = b + c); (3) If equals are subtracted from equals, the remainders are equal (a = b ⇒ a - c = b - c); (4) Things which coincide with one another are equal to one another (Principle of Superposition); (5) The whole is greater than the part (if b is a proper part of a, then a > b); (6) Things which are double of the same things are equal to one another; (7) Things which are halves of the same things are equal to one another.",
        "key_points": [
            "Axiom 1 (Transitivity of equality): If a = c and b = c, then a = b.",
            "Axiom 2 (Addition of equals): If a = b, then a + c = b + c.",
            "Axiom 3 (Subtraction of equals): If a = b, then a - c = b - c.",
            "Axiom 4 (Principle of Superposition): If figure A exactly covers figure B, they are congruent and equal.",
            "Axiom 5 (Whole is greater than part): Defines the fundamental concept of 'greater than' (A = B + C, C > 0 ⇒ A > B).",
            "Axioms 6 & 7: Equal scaling by doubling (2a = 2b) and halving (a/2 = b/2) preserves equality."
        ],
        "narration": "Euclid's 7 axioms are the bedrock of logical deduction. If A equals C and B equals C, then A must equal B! If you add equals to equals, the totals remain equal. And Axiom 5 gives us common sense: the whole is always greater than any of its parts!",
        "sim_title": "Euclid's 7 Axioms Interactive Balance Scale",
        "checkpoints": [
            {
                "q": "If line segment AB = CD and CD = EF, which Euclid's axiom proves that AB = EF?",
                "options": [
                    "Axiom 1: Things equal to the same thing are equal to one another",
                    "Axiom 4: Things which coincide with one another are equal",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 2: If equals are added to equals, the wholes are equal"
                ],
                "ans": 0,
                "exp": "Axiom 1 states that things equal to the same thing are equal to one another (transitive property of equality)."
            },
            {
                "q": "Which Euclid's axiom justifies the geometric method of 'Superposition' (placing one figure over another to test congruence)?",
                "options": ["Axiom 2", "Axiom 4", "Axiom 5", "Axiom 7"],
                "ans": 1,
                "exp": "Axiom 4 states: 'Things which coincide with one another are equal to one another' (the principle of superposition)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Euclid's Postulates 1 & 2: Straight Lines & Extensions",
        "subtitle": "Connecting Two Points & Infinite Line Segments (Axiom 5.1)",
        "category": "Postulates",
        "badge": "CG-7 • C-7.1 • Postulates 1 & 2",
        "summary": "Postulate 1: 'A straight line may be drawn from any one point to any other point.' Euclid assumed that through two distinct points, a unique line can be drawn. In modern NCERT geometry, this is stated as Axiom 5.1: 'Given two distinct points, there is a unique line that passes through them.' While an infinite number of lines can pass through a single point P, exactly one unique straight line passes through both point P and point Q. Postulate 2: 'A terminated line can be produced indefinitely.' In Euclid's terminology, a 'terminated line' corresponds to what we call a line segment today; it can be continuously extended in both directions to form a line.",
        "key_points": [
            "Postulate 1: A straight line can be drawn joining any two points.",
            "NCERT Axiom 5.1: Given two distinct points, there exists a unique line passing through them.",
            "Points collinearity: If a line passes through points A, B, and C, the points are collinear.",
            "Infinitely many lines pass through 1 point; exactly 1 line passes through 2 distinct points.",
            "Postulate 2: A line segment ('terminated line') can be extended endlessly in either direction."
        ],
        "narration": "Postulate 1 says that you can always draw a straight line between any two points. Even more importantly: only one unique line can connect them! Postulate 2 tells us that any line segment can be extended forever in both directions, turning a finite segment into an infinite line.",
        "sim_title": "Unique Line & Infinite Extension Ray Gun Simulator",
        "checkpoints": [
            {
                "q": "How many straight lines can pass through two distinct points P and Q?",
                "options": ["Infinitely many", "Exactly one", "Two", "Zero"],
                "ans": 1,
                "exp": "Axiom 5.1 / Postulate 1 establishes that exactly one unique straight line passes through two distinct points."
            },
            {
                "q": "In modern geometric terminology, what did Euclid mean by a 'terminated line' in Postulate 2?",
                "options": ["A ray", "A line segment", "A curve", "An angle"],
                "ans": 1,
                "exp": "Euclid called a line segment with two endpoints a 'terminated line', which can be produced indefinitely."
            }
        ]
    },
    {
        "id": 11,
        "title": "Euclid's Postulates 3 & 4: Circles & Universal Right Angles",
        "subtitle": "The Idealized Compass & The Invariance of Perpendicularity",
        "category": "Postulates",
        "badge": "CG-7 • C-7.1 • Postulates 3 & 4",
        "summary": "Postulate 3: 'A circle can be described with any centre and any radius.' This postulate authorizes the use of a compass as an idealized geometric drawing tool: given any point as center and any line segment length as radius, a perfect circle exists. Postulate 4: 'All right angles are equal to one another.' While this statement may seem obvious (every right angle equals 90°), it is a profound declaration about the geometry of the plane: it guarantees that space is uniform and homogeneous. No matter where a right angle is drawn, or how it is rotated, its magnitude is universally identical.",
        "key_points": [
            "Postulate 3: Any point can serve as the center of a circle of arbitrary radius.",
            "Euclidean collapsible compass: Once lifted from paper, the compass collapsed, ensuring radius transfer required proof.",
            "Postulate 4: All right angles are equal to one another (congruence of all 90° angles).",
            "Homogeneity of Euclidean space: Space is isotropic; figures do not change size or shape upon translation or rotation.",
            "Perpendicularity is a universal constant throughout the plane."
        ],
        "narration": "Postulate 3 gives us the power of the compass: you can draw a circle with any center and any radius. Postulate 4 states that all right angles are equal to one another! This ensures that our geometry is flat and uniform—a 90-degree angle here is identical to a 90-degree angle anywhere in the universe!",
        "sim_title": "Universal Circle Compass & Right-Angle Superposition Tool",
        "checkpoints": [
            {
                "q": "Which Euclid's postulate authorizes the construction of a circle with any center and any radius?",
                "options": ["Postulate 1", "Postulate 2", "Postulate 3", "Postulate 4"],
                "ans": 2,
                "exp": "Postulate 3 states: 'A circle can be described with any centre and any radius.'"
            },
            {
                "q": "What fundamental property of flat Euclidean space does Postulate 4 ('All right angles are equal') establish?",
                "options": [
                    "Space is curved like a sphere",
                    "Space is uniform and homogeneous (angles are invariant under rotation and translation)",
                    "Triangles always have three right angles",
                    "Lines cannot intersect"
                ],
                "ans": 1,
                "exp": "Postulate 4 establishes that Euclidean space is uniform, so orientation and position do not alter the magnitude of right angles."
            }
        ]
    },
    {
        "id": 12,
        "title": "Euclid's Famous Fifth Postulate (The Parallel Postulate)",
        "subtitle": "Interior Consecutive Angles & The Historic Criterion for Intersection",
        "category": "Fifth Postulate",
        "badge": "CG-7 • C-7.1 • Postulate 5",
        "summary": "Postulate 5 is the most celebrated and analyzed postulate in mathematics: 'If a straight line falling on two straight lines makes the interior angles on the same side of it taken together less than two right angles, the two straight lines, if produced indefinitely, meet on that side on which the sum of angles is less than two right angles.' In modern notation: if a transversal line t intersects lines l and m such that interior consecutive angles ∠1 and ∠2 satisfy ∠1 + ∠2 < 180°, lines l and m are guaranteed to intersect on that side if extended far enough.",
        "key_points": [
            "Verbatim: Interior angles on the same side sum to less than two right angles (< 180°).",
            "Consequence: The two lines will intersect on the side where the interior angle sum is < 180°.",
            "Divergence: On the opposite side where the angle sum is > 180°, the lines diverge further apart.",
            "Boundary condition: If interior angles sum exactly to 180° on both sides (∠1 + ∠2 = 180°), the lines NEVER meet (Parallel lines!).",
            "Unlike the first four brief postulates, Postulate 5 reads like a complex theorem."
        ],
        "narration": "Here is the famous Fifth Postulate! When a transversal cuts two lines, look at the interior angles on one side. If their sum is less than 180 degrees (two right angles), the lines will eventually crash into each other on that side! But if the sum is exactly 180 degrees, they will never meet—they are parallel!",
        "sim_title": "Euclid's 5th Postulate Transversal & Intersection Engine",
        "checkpoints": [
            {
                "q": "According to Euclid's Fifth Postulate, two straight lines will intersect on the side where the sum of interior angles is:",
                "options": [
                    "Greater than two right angles (> 180°)",
                    "Equal to two right angles (= 180°)",
                    "Less than two right angles (< 180°)",
                    "Zero"
                ],
                "ans": 2,
                "exp": "Euclid's Postulate 5 states that lines meet on that side where the interior angles taken together are less than two right angles (< 180°)."
            },
            {
                "q": "If a transversal intersects two lines such that interior angles on one side sum to exactly 180°, what can be concluded?",
                "options": [
                    "The two lines are parallel and will never intersect",
                    "The lines intersect immediately",
                    "The lines are perpendicular",
                    "The lines form an equilateral triangle"
                ],
                "ans": 0,
                "exp": "When the sum of interior consecutive angles equals 180° on both sides, the lines never intersect and are strictly parallel."
            }
        ]
    },
    {
        "id": 13,
        "title": "Equivalent Versions of the Fifth Postulate & Parallelism",
        "subtitle": "Playfair's Axiom & The Fundamental Definition of Parallel Lines",
        "category": "Parallelism",
        "badge": "CG-7 • C-7.1 • Playfair's Axiom",
        "summary": "Because Euclid's Fifth Postulate was long and cumbersome, mathematicians formulated simpler, equivalent statements. The most famous equivalent version is Playfair's Axiom (Scottish mathematician John Playfair, 1795): 'For every line l and for every point P not lying on l, there exists a unique line m passing through P and parallel to l.' An immediate equivalent consequence: 'Two distinct intersecting lines cannot be parallel to the same line.' Definition of Parallel Lines: Two coplanar straight lines that do not intersect, no matter how far they are produced in both directions, maintaining a constant perpendicular distance throughout.",
        "key_points": [
            "Playfair's Axiom (1795): Through a given point P not on line l, exactly one line parallel to l can be drawn.",
            "Equivalent corollary: Two intersecting lines cannot both be parallel to the same line.",
            "Definition of parallel lines: Coplanar lines having no common point of intersection.",
            "Equidistant property: The perpendicular distance between two parallel lines is constant everywhere.",
            "Playfair's axiom is logically completely equivalent to Euclid's 5th postulate."
        ],
        "narration": "In 1795, John Playfair gave us a much cleaner way to state the fifth postulate: take a line l and a point P not on it. Through point P, there is exactly one line that never touches l! That's Playfair's Axiom. This also means two lines that cross each other can never be parallel to the same line!",
        "sim_title": "Playfair's Parallel Line Beam Generator",
        "checkpoints": [
            {
                "q": "What does Playfair's Axiom state regarding a line l and a point P not lying on l?",
                "options": [
                    "Infinitely many lines through P are parallel to l",
                    "No line can be drawn through P parallel to l",
                    "There exists a unique line passing through P parallel to l",
                    "All lines passing through P intersect line l perpendicularly"
                ],
                "ans": 2,
                "exp": "Playfair's Axiom states that through a point not on a given line, there exists a unique line parallel to the given line."
            },
            {
                "q": "Can two distinct lines that intersect each other at a point both be parallel to a third line?",
                "options": [
                    "Yes, always",
                    "No, two intersecting lines cannot be parallel to the same line",
                    "Only if they are perpendicular to each other",
                    "Only in spherical geometry"
                ],
                "ans": 1,
                "exp": "By Playfair's Axiom, two intersecting lines cannot both be parallel to the same third line."
            }
        ]
    },
    {
        "id": 14,
        "title": "Justifying Constructions Using Axioms & Postulates",
        "subtitle": "Proposition 1: Constructing an Equilateral Triangle on a Given Segment",
        "category": "Geometric Proofs",
        "badge": "CG-7 • C-7.3 • Justifying Constructions",
        "summary": "Euclid demonstrated that every geometric construction must be strictly justified using axioms and postulates. Consider Proposition 1 of Book I: 'To construct an equilateral triangle on a given finite line segment AB': (1) Using center A and radius AB, draw circle C₁ (Postulate 3); (2) Using center B and radius BA, draw circle C₂ (Postulate 3); (3) Let circles intersect at point C; draw segments AC and BC (Postulate 1); (4) AC = AB (radii of circle C₁) and BC = AB (radii of circle C₂); (5) By Axiom 1 ('things equal to the same thing are equal to one another'), AC = BC = AB. Hence, triangle ABC is proven to be equilateral!",
        "key_points": [
            "Proposition 1 of Book I constructs an equilateral triangle on a segment AB.",
            "Step 1: Draw circle with center A and radius AB (justified by Postulate 3).",
            "Step 2: Draw circle with center B and radius BA (justified by Postulate 3).",
            "Step 3: Connect intersection point C to A and B (justified by Postulate 1).",
            "Step 4: Prove AC = AB and BC = AB by definition of circle radii.",
            "Step 5: Conclude AC = BC = AB by Euclid's Axiom 1 (Transitivity of equality)."
        ],
        "narration": "In Euclid's world, you cannot just draw a shape and say 'it looks equilateral'—you must prove it! In Proposition 1, Euclid used Postulate 3 to draw two intersecting circles, Postulate 1 to connect the vertices, and Axiom 1 to prove all three sides are equal. That is the beauty of deductive proof!",
        "sim_title": "Euclid Proposition 1 Step-by-Step Triangle Prover",
        "checkpoints": [
            {
                "q": "In Euclid's proof of Proposition 1 (equilateral triangle), which axiom proves that AC = BC?",
                "options": [
                    "Axiom 1: Things equal to the same thing are equal to one another",
                    "Axiom 2: If equals are added to equals, the wholes are equal",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 4: Things which coincide are equal"
                ],
                "ans": 0,
                "exp": "Since AC = AB (circle 1) and BC = AB (circle 2), Axiom 1 proves AC = BC, making all three sides equal."
            },
            {
                "q": "Which postulate authorizes drawing the two intersecting circles in Proposition 1?",
                "options": ["Postulate 1", "Postulate 2", "Postulate 3", "Postulate 5"],
                "ans": 2,
                "exp": "Postulate 3 allows describing a circle with any center and radius."
            }
        ]
    },
    {
        "id": 15,
        "title": "The Quest to Prove Postulate 5 & Non-Euclidean Geometries",
        "subtitle": "2,000 Years of Attempts, Saccheri, Lobachevsky, Bolyai & Riemann",
        "category": "Non-Euclidean Horizons",
        "badge": "CG-7 • C-7.1 • Non-Euclidean Geometry",
        "summary": "For over two millennia, mathematicians believed the Fifth Postulate was too complicated to be an axiom and tried to prove it as a theorem from Postulates 1–4. Renowned scholars including Ptolemy, Proclus, Ibn al-Haytham, Omar Khayyam, and Saccheri attempted proofs, but all unwittingly assumed an equivalent statement (like Playfair's axiom). In the 19th century, Gauss, Lobachevsky, Bolyai, and Riemann made an astonishing discovery: Postulate 5 CANNOT be proven because it is independent! Denying Postulate 5 created valid, consistent 'Non-Euclidean Geometries': (1) Spherical Geometry (no parallels, triangle sum > 180°); (2) Hyperbolic Geometry (infinite parallels, triangle sum < 180°).",
        "key_points": [
            "2000-year quest: Mathematicians tried to prove Postulate 5 from the first four postulates.",
            "All historical attempts failed because they relied on circular reasoning (hidden assumptions).",
            "19th-century revolution: Gauss, Lobachevsky (1829), Bolyai (1832), and Riemann (1854).",
            "Hyperbolic Geometry: Infinitely many lines parallel to l pass through P; triangle angle sum < 180°.",
            "Spherical / Elliptic Geometry (Riemann): No parallel lines exist (great circles always intersect); triangle angle sum > 180°.",
            "Einstein's General Relativity proved our physical universe's spacetime is curved (Non-Euclidean)!"
        ],
        "narration": "For 2,000 years, mathematicians tried to prove the Fifth Postulate. They all failed! In the 1800s, Gauss, Lobachevsky, and Riemann realized why: on a curved surface like a sphere or a saddle, Euclid's 5th postulate is false! This opened up Non-Euclidean geometry, which Einstein later used to describe the curved spacetime of gravity!",
        "sim_title": "Euclidean vs. Spherical vs. Hyperbolic Universe Comparer",
        "checkpoints": [
            {
                "q": "In Spherical Geometry (geometry on the surface of a sphere), how many parallel lines pass through a point not on a given line?",
                "options": [
                    "Zero (no parallel lines exist; all great circles intersect)",
                    "Exactly one",
                    "Infinitely many",
                    "Exactly two"
                ],
                "ans": 0,
                "exp": "On a sphere, lines are great circles (like the equator). Any two great circles intersect, so no parallel lines exist."
            },
            {
                "q": "What is the sum of angles of a triangle in Hyperbolic (saddle-shaped) Geometry?",
                "options": [
                    "Strictly less than 180°",
                    "Exactly equal to 180°",
                    "Strictly greater than 180°",
                    "Always 360°"
                ],
                "ans": 0,
                "exp": "In hyperbolic geometry, the sum of angles of any triangle is strictly less than 180°."
            }
        ]
    },
    {
        "id": 16,
        "title": "Comprehensive Synthesis & The Axiomatic Method",
        "subtitle": "Connecting Practical Needs, Vedic Ropes, Euclid's Logic & Modern AI",
        "category": "Mastery Synthesis",
        "badge": "CG-7 • C-7.1 • C-7.3 • Synthesis",
        "summary": "Euclid's greatest gift to human civilization was not just geometry, but the 'Axiomatic Method'—the idea that an entire domain of knowledge can be built upon a tiny foundation of clear definitions and self-evident axioms through pure deductive reasoning. From the muddy banks of the River Nile and the sacred altar ropes of the Sulbasutras, geometry evolved into the logical bedrock of science. Today, the axiomatic method powers modern mathematics, computer science algorithms, formal software verification, and automated theorem proving in Artificial Intelligence.",
        "key_points": [
            "Evolutionary arc: Practical land surveying → Vedic sacrificial ropes → Greek deductive proofs → Axiomatic foundations.",
            "Axiomatic Method: Start with minimal axioms; deduce all truths through rigorous logic.",
            "Euclid's 5 Postulates define the geometry of flat planes; modifying them yields curved spacetime.",
            "Proof standards: Observation suggests a conjecture, but only formal deductive proof establishes mathematical truth.",
            "Modern impact: Powers computer graphics, CAD engineering, robotics, cryptography, and AI theorem provers."
        ],
        "narration": "Congratulations on exploring Euclid's Geometry! From the flooded banks of the Nile and the rope mathematics of ancient India, to Euclid's 13 books and curved non-Euclidean space, you now understand the power of axioms and proof. Let's test your knowledge in our mastery quiz challenges!",
        "sim_title": "Axiomatic Sandbox & Logic Chain Verifier",
        "checkpoints": [
            {
                "q": "What is the core idea of the 'Axiomatic Method' introduced by Euclid?",
                "options": [
                    "Measuring shapes with physical instruments",
                    "Deducing all mathematical truths logically from a small set of unproven axioms and postulates",
                    "Accepting mathematical statements based on authority",
                    "Only using computer simulations to verify facts"
                ],
                "ans": 1,
                "exp": "The axiomatic method establishes all theorems through deductive logic starting from a minimal set of accepted axioms."
            },
            {
                "q": "Which statement best summarizes why a mathematical conjecture requires a proof?",
                "options": [
                    "Observations can be misleading; only logical deduction from axioms guarantees universal truth",
                    "Proofs make textbooks longer",
                    "A theorem is only true if verified on a computer",
                    "Conjectures are never true"
                ],
                "ans": 0,
                "exp": "Empirical observation can reveal patterns, but only a formal deductive proof ensures a statement is true in all cases."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 17,
        "title": "Mastery Challenge Part 1: History of Geometry & Sulbasutras",
        "subtitle": "10 Questions on Ancient Civilisations, Harappa, Vedic Altars & Baudhayana",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 1 • Historical Foundations",
        "questions": [
            {
                "id": 1,
                "q": "The word 'Geometry' is derived from two Greek words meaning:",
                "options": ["Sky measurement", "Earth measurement", "Triangle study", "Building construction"],
                "ans": 1,
                "solution": "Geometry comes from Greek words 'Geo' (Earth) and 'Metrein' (to measure), signifying 'Earth measurement'."
            },
            {
                "id": 2,
                "q": "In ancient Egypt, surveyors who re-established agricultural land boundaries were known as:",
                "options": ["Harpedonaptai (rope-stretchers)", "Scribes", "Geometers", "Mason-builders"],
                "ans": 0,
                "solution": "Egyptian surveyors were called 'harpedonaptai', meaning 'rope-stretchers', because they used knotted ropes to measure field boundaries after the Nile floods."
            },
            {
                "id": 3,
                "q": "The bricks used for construction in the Indus Valley (Harappan) Civilisation had dimensions in the ratio:",
                "options": ["3 : 2 : 1", "4 : 2 : 1", "5 : 3 : 2", "4 : 3 : 1"],
                "ans": 1,
                "solution": "Harappan bricks exhibited a standardized ratio of Length : Breadth : Thickness = 4 : 2 : 1."
            },
            {
                "id": 4,
                "q": "The ancient Indian mathematical texts detailing geometric constructions using ropes are called:",
                "options": ["Vedas", "Sulbasutras", "Upanishads", "Puranas"],
                "ans": 1,
                "solution": "The 'Sulbasutras' (manuals of the cord/rope) are ancient Indian treatises containing rules for geometric constructions."
            },
            {
                "id": 5,
                "q": "Which Vedic fire altar was constructed in the shape of a soaring falcon or hawk?",
                "options": ["Garhapatya", "Ahavaniya", "Syenaciti", "Dakshinagni"],
                "ans": 2,
                "solution": "The 'Syenaciti' was a massive public altar constructed in the intricate geometric shape of a falcon or hawk in flight."
            },
            {
                "id": 6,
                "q": "In Vedic rituals, the domestic Garhapatya altar was circular and the Ahavaniya altar was square. What was the mandatory condition connecting them?",
                "options": [
                    "They had to have identical perimeters",
                    "They were required to have the exact same surface area",
                    "The circular altar had to be twice as large",
                    "The square altar had to be twice as large"
                ],
                "ans": 1,
                "solution": "Vedic ritual rules strictly mandated that the circular Garhapatya and square Ahavaniya altars must have identical surface area."
            },
            {
                "id": 7,
                "q": "How many small subordinate triangles are formed by the 9 interwoven isosceles triangles in the Sri Yantra?",
                "options": ["27", "36", "43", "49"],
                "ans": 2,
                "solution": "The Sri Yantra consists of 9 interwoven isosceles triangles that intersect to create 43 smaller subsidiary triangles surrounding the central Bindu."
            },
            {
                "id": 8,
                "q": "Baudhayana's Sulbasutra is celebrated for stating an ancient Indian theorem equivalent to:",
                "options": [
                    "Pythagorean Theorem",
                    "Thales Theorem",
                    "Euler's Formula",
                    "Fermat's Last Theorem"
                ],
                "ans": 0,
                "solution": "Baudhayana stated that the diagonal of a rectangle produces an area equal to the sum of areas produced by its sides, anticipating the Pythagorean theorem."
            },
            {
                "id": 9,
                "q": "In Baudhayana's square construction, what was the baseline aligned with the East-West direction called?",
                "options": ["Praci", "Udici", "Sulba", "Vedi"],
                "ans": 0,
                "solution": "The East-West baseline was called 'Praci', while the North-South perpendicular line was called 'Udici'."
            },
            {
                "id": 10,
                "q": "Who was the Greek mathematician from Miletus credited with providing the first recorded deductive proofs in history?",
                "options": ["Euclid", "Thales", "Archimedes", "Pythagoras"],
                "ans": 1,
                "solution": "Thales of Miletus (c. 624–546 BCE) is universally credited with introducing deductive proofs into geometry, proving that a circle is bisected by its diameter."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge Part 2: Euclid's Definitions & Common Notions",
        "subtitle": "10 Questions on Undefined Terms, 23 Definitions & The 7 Axioms",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 2 • Definitions & Axioms",
        "questions": [
            {
                "id": 11,
                "q": "In Euclid's 'The Elements', a line is defined as:",
                "options": [
                    "A collection of dots",
                    "Breadthless length",
                    "A path between two points",
                    "A surface of zero area"
                ],
                "ans": 1,
                "solution": "Definition 2 of Book I states: 'A line is breadthless length.'"
            },
            {
                "id": 12,
                "q": "According to Euclid, the boundaries or ends of a surface are:",
                "options": ["Points", "Lines", "Angles", "Solids"],
                "ans": 1,
                "solution": "Definition 6 of Book I states: 'The edges of a surface are lines.'"
            },
            {
                "id": 13,
                "q": "How many dimensions does a geometric 'point' have?",
                "options": ["0", "1", "2", "3"],
                "ans": 0,
                "solution": "A point has no length, breadth, or height; it is zero-dimensional (0D)."
            },
            {
                "id": 14,
                "q": "Why does modern mathematics treat Point, Line, and Plane as 'Undefined Terms'?",
                "options": [
                    "To avoid an infinite regress of circular definitions",
                    "Because they cannot be visualized",
                    "Because Euclid forgot to define them",
                    "Because they change in 3D space"
                ],
                "ans": 0,
                "solution": "Every definition relies on other words. To avoid an infinite regress of circular definitions, foundational concepts like Point, Line, and Plane are taken as undefined starting terms."
            },
            {
                "id": 15,
                "q": "If x = z and y = z, which Euclid's axiom implies that x = y?",
                "options": [
                    "Axiom 1: Things equal to the same thing are equal to one another",
                    "Axiom 2: If equals are added to equals, wholes are equal",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 4: Things which coincide are equal"
                ],
                "ans": 0,
                "solution": "Axiom 1 states: 'Things which are equal to the same thing are equal to one another' (the transitive property of equality)."
            },
            {
                "id": 16,
                "q": "If a = b, then a + 7 = b + 7. Which axiom justifies this statement?",
                "options": [
                    "Axiom 2: If equals are added to equals, the wholes are equal",
                    "Axiom 3: If equals are subtracted from equals, remainders are equal",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 6: Things double of same things are equal"
                ],
                "ans": 0,
                "solution": "Axiom 2 states: 'If equals are added to equals, the wholes are equal.'"
            },
            {
                "id": 17,
                "q": "A cake is cut into 8 equal slices. Which axiom mathematically proves that the whole cake is larger than any single slice?",
                "options": [
                    "Axiom 1",
                    "Axiom 4",
                    "Axiom 5: The whole is greater than the part",
                    "Axiom 7: Things halves of same things are equal"
                ],
                "ans": 2,
                "solution": "Axiom 5 states: 'The whole is greater than the part.'"
            },
            {
                "id": 18,
                "q": "Which Euclid's axiom provides the logical foundation for testing geometric congruence by placing one shape over another (Superposition)?",
                "options": [
                    "Axiom 1",
                    "Axiom 3",
                    "Axiom 4: Things which coincide with one another are equal to one another",
                    "Axiom 6"
                ],
                "ans": 2,
                "solution": "Axiom 4 states: 'Things which coincide with one another are equal to one another'—this is the principle of superposition."
            },
            {
                "id": 19,
                "q": "If a = b, then a - 5 = b - 5. This is justified by:",
                "options": [
                    "Axiom 1",
                    "Axiom 2",
                    "Axiom 3: If equals are subtracted from equals, the remainders are equal",
                    "Axiom 5"
                ],
                "ans": 2,
                "solution": "Axiom 3 states: 'If equals are subtracted from equals, the remainders are equal.'"
            },
            {
                "id": 20,
                "q": "How many propositions (theorems) did Euclid prove throughout the 13 books of The Elements?",
                "options": ["23", "48", "465", "1000"],
                "ans": 2,
                "solution": "Euclid systematically proved 465 propositions (theorems) across the 13 books of 'The Elements'."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge Part 3: Euclid's Five Postulates",
        "subtitle": "10 Questions on Straight Lines, Rays, Circles, Right Angles & Postulate 5",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 3 • The 5 Postulates",
        "questions": [
            {
                "id": 21,
                "q": "Which of Euclid's postulates asserts that 'A straight line may be drawn from any one point to any other point'?",
                "options": ["Postulate 1", "Postulate 2", "Postulate 3", "Postulate 4"],
                "ans": 0,
                "solution": "Postulate 1 states that a straight line may be drawn from any one point to any other point."
            },
            {
                "id": 22,
                "q": "NCERT Axiom 5.1, based on Postulate 1, states that given two distinct points, there exists:",
                "options": [
                    "Infinitely many lines passing through them",
                    "A unique line passing through them",
                    "At least two lines passing through them",
                    "No straight line"
                ],
                "ans": 1,
                "solution": "Axiom 5.1 states: 'Given two distinct points, there is a unique line that passes through them.'"
            },
            {
                "id": 23,
                "q": "Postulate 2 states that 'A terminated line can be produced indefinitely.' Today, a 'terminated line' is called:",
                "options": ["A ray", "A line segment", "An arc", "A polygon"],
                "ans": 1,
                "solution": "A 'terminated line' in Euclid's terminology is what we call a 'line segment' today."
            },
            {
                "id": 24,
                "q": "Which postulate authorizes the use of a compass to construct a circle of any size anywhere in the plane?",
                "options": ["Postulate 1", "Postulate 2", "Postulate 3", "Postulate 4"],
                "ans": 2,
                "solution": "Postulate 3 states: 'A circle can be described with any centre and any radius.'"
            },
            {
                "id": 25,
                "q": "What does Euclid's Postulate 4 state?",
                "options": [
                    "All equilateral triangles are congruent",
                    "All right angles are equal to one another",
                    "All straight lines have infinite length",
                    "Parallel lines never intersect"
                ],
                "ans": 1,
                "solution": "Postulate 4 states: 'All right angles are equal to one another.'"
            },
            {
                "id": 26,
                "q": "In Euclid's Fifth Postulate, on which side will two lines intersect when cut by a transversal?",
                "options": [
                    "On the side where the interior angles sum to more than two right angles",
                    "On the side where the interior angles sum to less than two right angles (< 180°)",
                    "On both sides simultaneously",
                    "They will never intersect on any side"
                ],
                "ans": 1,
                "solution": "The Fifth Postulate states that the lines meet on that side on which the sum of the interior angles is less than two right angles (< 180°)."
            },
            {
                "id": 27,
                "q": "A transversal cuts lines l and m. If the consecutive interior angles on one side are 85° and 92°, what will happen if l and m are produced indefinitely on that side?",
                "options": [
                    "They will intersect because 85° + 92° = 177° < 180°",
                    "They will never intersect because they are parallel",
                    "They will diverge and move further apart",
                    "They will form a circle"
                ],
                "ans": 0,
                "solution": "The sum of interior angles is 85° + 92° = 177°. Since 177° < 180° (less than two right angles), Euclid's Postulate 5 guarantees that the lines will intersect on that side."
            },
            {
                "id": 28,
                "q": "If the interior angles on one side of a transversal sum to exactly 180°, what is the relationship between the two lines?",
                "options": ["They are perpendicular", "They are parallel", "They coincide", "They intersect at 90°"],
                "ans": 1,
                "solution": "When interior angles sum to exactly 180° (two right angles) on both sides, the lines never meet and are parallel."
            },
            {
                "id": 29,
                "q": "What is Playfair's Axiom, the most famous equivalent form of Euclid's Fifth Postulate?",
                "options": [
                    "For every line l and point P not on l, there exists a unique line passing through P parallel to l",
                    "Two lines parallel to a third line intersect each other",
                    "All triangles have angles summing to 180°",
                    "Parallel lines meet at infinity"
                ],
                "ans": 0,
                "solution": "Playfair's Axiom (1795) states: 'For every line l and for every point P not lying on l, there exists a unique line m passing through P and parallel to l.'"
            },
            {
                "id": 30,
                "q": "Which logical deduction directly follows from Playfair's Axiom?",
                "options": [
                    "Two distinct intersecting lines cannot be parallel to the same line",
                    "All parallel lines have equal length",
                    "A point has length and breadth",
                    "Every triangle is right-angled"
                ],
                "ans": 0,
                "solution": "If two intersecting lines could both be parallel to the same line, there would be two parallels through the intersection point, violating Playfair's Axiom."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Part 4: Proofs, Constructions & Non-Euclidean Horizons",
        "subtitle": "10 Questions on Proposition 1, Equilateral Triangles & Curved Geometries",
        "category": "Quiz Challenge",
        "badge": "Quiz Part 4 • Advanced Concepts",
        "questions": [
            {
                "id": 31,
                "q": "In Proposition 1 of Book I, Euclid constructs which geometric figure on a given segment AB?",
                "options": ["A Square", "An Equilateral Triangle", "A Regular Hexagon", "A Right Triangle"],
                "ans": 1,
                "solution": "Proposition 1 of Book I is the classic construction of an equilateral triangle on a given finite line segment AB."
            },
            {
                "id": 32,
                "q": "In Euclid's construction of an equilateral triangle on segment AB, what is the radius of the two intersecting circles?",
                "options": ["AB / 2", "AB", "2 AB", "AB √2"],
                "ans": 1,
                "solution": "Both circles are drawn with radius equal to the segment length AB (one centered at A and the other at B)."
            },
            {
                "id": 33,
                "q": "If AC = AB (radii of circle 1) and BC = AB (radii of circle 2), which axiom justifies concluding that AC = BC?",
                "options": [
                    "Axiom 1: Things equal to the same thing are equal to one another",
                    "Axiom 2: If equals are added to equals, wholes are equal",
                    "Axiom 4: Things coinciding are equal",
                    "Axiom 5: The whole is greater than the part"
                ],
                "ans": 0,
                "solution": "Since both AC and BC equal the same length AB, by Axiom 1 (transitivity), AC = BC. Therefore, AB = BC = CA."
            },
            {
                "id": 34,
                "q": "Why were 2,000 years of mathematical attempts to prove Postulate 5 from Postulates 1–4 unsuccessful?",
                "options": [
                    "Ancient mathematicians made arithmetic errors",
                    "Postulate 5 is completely independent and cannot be deduced from Postulates 1 to 4",
                    "Geometry was not studied during the Renaissance",
                    "Postulate 5 is false on a flat plane"
                ],
                "ans": 1,
                "solution": "Postulate 5 is logically independent of the first four postulates; it cannot be proven from them without introducing an equivalent unproven assumption."
            },
            {
                "id": 35,
                "q": "Which 19th-century mathematicians are celebrated for discovering Non-Euclidean Geometry?",
                "options": [
                    "Gauss, Lobachevsky, Bolyai, and Riemann",
                    "Newton, Leibniz, and Descartes",
                    "Euler, Fermat, and Pascal",
                    "Galileo, Kepler, and Copernicus"
                ],
                "ans": 0,
                "solution": "Carl Friedrich Gauss, Nikolai Lobachevsky (1829), János Bolyai (1832), and Bernhard Riemann (1854) independently developed Non-Euclidean geometries."
            },
            {
                "id": 36,
                "q": "What are 'lines' on the surface of a sphere in Spherical Geometry?",
                "options": ["Straight line segments", "Great Circles (like the Equator)", "Parabolas", "Hyperbolas"],
                "ans": 1,
                "solution": "On a sphere, the shortest path between two points ('straight line') is an arc of a Great Circle whose center coincides with the center of the sphere."
            },
            {
                "id": 37,
                "q": "On the surface of the Earth (a sphere), consider a triangle formed by the North Pole, (0°N, 0°E) on the Equator, and (0°N, 90°E) on the Equator. What is the sum of its three interior angles?",
                "options": ["180°", "270° (90° + 90° + 90°)", "360°", "120°"],
                "ans": 1,
                "solution": "Each meridian meets the equator at 90°, and the two meridians meet at the North Pole at 90°. Thus, 90° + 90° + 90° = 270° > 180°, proving spherical triangles have angle sums > 180°."
            },
            {
                "id": 38,
                "q": "In Hyperbolic Geometry (developed by Lobachevsky and Bolyai), how many lines parallel to line l can be drawn through a point P not on l?",
                "options": ["Zero", "Exactly one", "Infinitely many", "Exactly three"],
                "ans": 2,
                "solution": "In hyperbolic geometry, through any point P not on line l, there exist infinitely many lines that never intersect line l."
            },
            {
                "id": 39,
                "q": "Albert Einstein's General Theory of Relativity describes gravity using which type of geometry?",
                "options": [
                    "Flat Euclidean Geometry",
                    "Curved Non-Euclidean Geometry (Riemannian spacetime)",
                    "Vedic Sulba geometry",
                    "Coordinate geometry with only whole numbers"
                ],
                "ans": 1,
                "solution": "Einstein showed that mass and energy curve spacetime, so gravity is modeled using curved Riemannian (Non-Euclidean) geometry."
            },
            {
                "id": 40,
                "q": "If point C lies between A and B on a line, and AC = BC, what is point C called, and what does AC + BC equal?",
                "options": [
                    "C is the midpoint of AB, and AC + BC = AB",
                    "C is an external point, and AC + BC > AB",
                    "C is a vertex, and AC + BC = 2AB",
                    "C is the origin, and AC + BC = 0"
                ],
                "ans": 0,
                "solution": "When C is between A and B with AC = BC, C is the midpoint of segment AB, and by segment addition (Axiom 4/5), AC + BC = AB."
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

    print("All validations PASSED cleanly!")


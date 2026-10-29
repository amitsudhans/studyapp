# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 7 Mathematics: Chapter 6 - Constructions and Tilings
SLIDES_DATA containing 20 slides, 32 checkpoints, and 40 mastery quiz questions with detailed step-by-step solutions.
Strictly zero occurrences of prohibited textbook titles.
"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "The Geometer's Tools & The Symmetrical Eye",
        "subtitle": "Unmarked Straightedge, Compass & The Vesica Piscis",
        "content": (
            "<p>In classical geometry, we explore the universe of exact shapes using only two pure, ancient tools: an <strong>unmarked straightedge</strong> (for drawing straight lines through points) and a <strong>compass</strong> (for transferring distances and drawing circles of equal radius).</p>"
            "<p class='mt-2'>When two circles of equal radius $r$ pass through each other's centers ($A$ and $B$, where $AB = r$), they intersect at two points $X$ and $Y$. The overlapping lens-like region is celebrated across cultures as the <strong>symmetric 'eye'</strong> (or <em>Vesica Piscis</em>).</p>"
            "<p class='mt-2'>Because all four radii are identical:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$AX = AY = BX = BY = r$$"
            "</div>"
            "<p class='mt-2'>The quadrilateral $AXBY$ forms an equilateral rhombus. The vertical chord $XY$ intersects the horizontal line segment $AB$ at right angles ($90^\\circ$) and bisects it, forming the mathematical foundation for all perpendicular constructions!</p>"
        ),
        "key_takeaways": [
            "Geometric constructions rely exclusively on an unmarked straightedge and a compass.",
            "Intersecting two identical circles through each other's centers creates a symmetric 'eye' shape.",
            "All four bounding segments are equal: $AX = AY = BX = BY = r$, proving symmetry by equilateral rhombus properties.",
            "The line connecting intersection points $XY$ is the perpendicular bisector of segment $AB$."
        ],
        "formula": "$$AX = AY = BX = BY = r \\implies XY \\perp AB \\text{ and bisects } AB$$",
        "simulator_type": "vesica_piscis_eye_sim",
        "checkpoints": [
            {
                "question": "In the construction of the symmetric 'eye' with segment AB of length r, why is quadrilateral AXBY an equilateral rhombus?",
                "options": [
                    "Because all four sides are drawn with a ruler of arbitrary lengths",
                    "Because AX, AY, BX, and BY are all radii of two identical circles of radius r, making AX = AY = BX = BY = r",
                    "Because all angles are 90 degrees",
                    "Because it is inscribed in a square"
                ],
                "correct": 1,
                "explanation": "Points X and Y lie on both circles centered at A and B with radius r. Thus, AX = r, AY = r, BX = r, and BY = r. Since all 4 sides are equal to r, AXBY is an equilateral rhombus!"
            },
            {
                "question": "What is the angle between the segment AB and the vertical chord XY in the symmetric eye construction?",
                "options": ["45 degrees", "60 degrees", "90 degrees", "180 degrees"],
                "correct": 2,
                "explanation": "The diagonals of any rhombus are perpendicular bisectors of each other. Therefore, XY is perpendicular to AB at exactly 90 degrees!"
            }
        ]
    },
    {
        "id": 2,
        "title": "Perpendicular Bisector: Equidistant Points & SSS Proof",
        "subtitle": "Finding Points Equidistant from Endpoints via Arcs",
        "content": (
            "<p>A <strong>perpendicular bisector</strong> of a segment $AB$ is a line that divides $AB$ into two equal halves at exactly $90^\\circ$. How do we construct it without measuring?</p>"
            "<p class='mt-2'><strong>Step-by-Step Compass Procedure:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Open the compass to any radius strictly greater than half the length of $AB$ ($r > \\frac{1}{2}AB$).</li>"
            "<li>With center $A$, draw arcs above and below the segment.</li>"
            "<li>With center $B$ and the <em>exact same radius</em>, draw intersecting arcs to locate points $P$ and $Q$.</li>"
            "<li>Draw the straight line passing through $P$ and $Q$. This line intersects $AB$ at midpoint $M$.</li>"
            "</ol>"
            "<p class='mt-2'><strong>Geometric Proof via SSS Congruence:</strong> Since $AP = BP = r$ and $AQ = BQ = r$ and $PQ$ is common, $\\triangle APQ \\cong \\triangle BPQ$ by SSS. This proves $\\angle APM = \\angle BPM$, which leads directly to $\\triangle APM \\cong \\triangle BPM$ by SAS, establishing $AM = BM$ and $\\angle AMP = 90^\\circ$!</p>"
        ),
        "key_takeaways": [
            "The compass radius must be greater than $\\frac{1}{2}AB$; otherwise the arcs will never intersect.",
            "Any point on the perpendicular bisector is equidistant from the two endpoints: $PA = PB$.",
            "Conversely, any point equidistant from $A$ and $B$ must lie on the perpendicular bisector.",
            "Congruence criteria (SSS followed by SAS) provide the rigorous mathematical proof of this construction."
        ],
        "formula": "$$\\text{Perpendicular Bisector Theorem: } P \\text{ lies on bisector of } AB \\iff PA = PB$$",
        "simulator_type": "perp_bisector_stepper_sim",
        "checkpoints": [
            {
                "question": "What happens if you attempt to construct a perpendicular bisector using a compass radius less than half of AB?",
                "options": [
                    "The bisector is drawn inverted",
                    "The arcs from A and B will not intersect, making the construction impossible",
                    "The angle becomes 45 degrees instead of 90 degrees",
                    "The line divides AB in the ratio 2:1"
                ],
                "correct": 1,
                "explanation": "If radius r < AB/2, the two circles do not reach each other and cannot intersect. The radius must strictly exceed half the distance (r > AB/2)."
            },
            {
                "question": "In the perpendicular bisector proof, which triangle congruence criterion proves that triangle APQ is congruent to triangle BPQ?",
                "options": ["AAA", "SSS (Side-Side-Side)", "RHS only", "SSA"],
                "correct": 1,
                "explanation": "AP = BP = r (equal compass radii), AQ = BQ = r (equal compass radii), and PQ is common to both triangles. Three pairs of equal sides guarantee congruence by SSS!"
            }
        ]
    },
    {
        "id": 3,
        "title": "Erecting a 90° Angle at a Given Point",
        "subtitle": "Creating a Perpendicular Ray from Any Point on a Line",
        "content": (
            "<p>What if you need to construct a perpendicular at a <em>specific point</em> $P$ located on a given line $L$, rather than bisecting an existing segment?</p>"
            "<p class='mt-2'>We transform this challenge into a perpendicular bisector problem using symmetry!</p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Place the compass pointer at point $P$. Draw two small arcs of equal radius $r_1$ on opposite sides of $P$ to mark points $A$ and $B$ on the line. Now, $P$ is the exact midpoint of $AB$ ($AP = PB$).</li>"
            "<li>Expand the compass to a larger radius $r_2 > r_1$.</li>"
            "<li>Place the compass needle at $A$ and strike an arc above $P$. Repeat from $B$ with the same radius $r_2$ to intersect at point $C$.</li>"
            "<li>Draw the ray passing through $P$ and $C$. Ray $PC$ is strictly perpendicular to line $L$ at point $P$!</li>"
            "</ol>"
            "<p class='mt-2'>Because $\\triangle APC \\cong \\triangle BPC$ by SSS ($AC = BC = r_2$, $AP = BP = r_1$, and $PC$ common), the adjacent angles on the straight line are equal: $\\angle APC = \\angle BPC = \\frac{180^\\circ}{2} = 90^\\circ$.</p>"
        ),
        "key_takeaways": [
            "Erecting a perpendicular at a point is achieved by making that point the midpoint of an auxiliary segment $AB$.",
            "Equal arcs from $P$ create symmetric endpoints: $AP = PB = r_1$.",
            "Intersecting arcs of radius $r_2 > r_1$ from $A$ and $B$ locate point $C$ directly above $P$.",
            "Linear pair equal angles guarantee $90^\\circ$: $\\angle APC + \\angle BPC = 180^\\circ \\implies 2\\angle APC = 180^\\circ \\implies 90^\\circ$."
        ],
        "formula": "$$\\angle APC + \\angle BPC = 180^\\circ \\quad \\text{and} \\quad \\angle APC = \\angle BPC \\implies \\angle APC = 90^\\circ$$",
        "simulator_type": "erect_90_point_sim",
        "checkpoints": [
            {
                "question": "Why do we first mark points A and B equidistant from P before drawing the intersecting arcs?",
                "options": [
                    "To make the drawing look artistic",
                    "To turn point P into the midpoint of an auxiliary segment AB, so its perpendicular bisector passes through P",
                    "Because compasses only work with three points",
                    "To double the length of line L"
                ],
                "correct": 1,
                "explanation": "By ensuring AP = PB, the point P becomes the midpoint of AB. Any point C equidistant from A and B lies on the perpendicular bisector, ensuring PC is perpendicular to L at P."
            },
            {
                "question": "What must be true about the radius r2 used from points A and B compared to radius r1 used to mark A and B?",
                "options": [
                    "r2 must be strictly greater than r1 (r2 > r1)",
                    "r2 must be equal to zero",
                    "r2 must be smaller than r1/2",
                    "r2 must be negative"
                ],
                "correct": 0,
                "explanation": "Since the distance between A and B is 2*r1, half that distance is r1. To intersect above line L, the radius r2 must exceed r1 (r2 > r1)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Construction Methods in the Śulba-Sūtras",
        "subtitle": "Ancient Indian Cord Geometry of Kātyāyana & Baudhāyana",
        "content": (
            "<p>Long before metal compasses and printed textbooks, ancient Indian mathematicians developed master geometric construction techniques documented in the <strong>Śulba-Sūtras</strong> (part of the <em>Vedāṅgas</em>, composed around 800–500 BCE by Baudhāyana, Mānava, Āpastamba, and Kātyāyana).</p>"
            "<p class='mt-2'>The word <em>Śulba</em> signifies a 'measuring cord' or rope. Vedic geometers (<em>Śulbavids</em>) used knotted ropes and wooden pegs (<em>śaṅku</em>) driven into flat ground to lay out sacred ritual fire altars with astronomical precision:</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>The Prācī (East-West Cardinal Line):</strong> Determined precisely by observing the shadows of a vertical gnomon (pole) cast at sunrise and sunset.</li>"
            "<li><strong>The Rope Vesica (Pṛṣṭhyā Construction):</strong> As detailed in the <em>Kātyāyana-Śulbasūtra</em>, a cord of length $2L$ with tied loop ends is anchored at pegs $A$ and $B$. Pulling a knot at the midpoint creates circular arcs that intersect to establish the true North-South meridian perpendicular to the East-West axis.</li>"
            "<li><strong>Sacred Fire Altars:</strong> Altars such as the square <em>Āhavanīya</em>, circular <em>Gārhapatya</em>, and falcon-shaped <em>Śyenaciti</em> required exact right angles and equal area transformations using only cord geometry!</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "The Śulba-Sūtras (Baudhāyana, Kātyāyana) are among the world's earliest systematic geometric construction treatises.",
            "Ancient Indian geometers used cords (rajju/śulba) and pegs (śaṅku) to execute exact perpendicular and circular constructions.",
            "The East-West cardinal line (Prācī) was oriented astronomically using solar shadow gnomons.",
            "Tying loops and folding cords allowed ancient sages to construct perpendiculars, squares, and altars without modern instruments."
        ],
        "formula": "$$\\text{Śulba Principle: Cord with center knot } C, \\; AC + CB = \\text{const} \\implies \\text{True Perpendicular Meridian}$$",
        "simulator_type": "sulba_sutra_altar_sim",
        "checkpoints": [
            {
                "question": "What primary physical tools did ancient Indian geometers use according to the Śulba-Sūtras to construct sacred altars?",
                "options": [
                    "Plastic protractors and mechanical dividers",
                    "Knotted measuring cords (śulba/rajju) and wooden ground pegs (śaṅku)",
                    "Laser measuring tapes and digital theodolites",
                    "Only eye estimation without measurements"
                ],
                "correct": 1,
                "explanation": "The Śulba-Sūtras describe geometry executed on the ground using cords (śulba or rajju) with fixed knots and wooden pegs (śaṅku)."
            },
            {
                "question": "What is the ancient Sanskrit term for the fundamental East-West cardinal line used as the baseline for altar geometry?",
                "options": ["Prācī", "Śanku", "Manojava", "Vedī"],
                "correct": 0,
                "explanation": "The Prācī is the cardinal East-West baseline established from solar shadows, across which North-South perpendiculars were erected."
            }
        ]
    },
    {
        "id": 5,
        "title": "Angle Bisection: SSS Congruence & Symmetric Halving",
        "subtitle": "Dividing Any Angle into Two Equal Halves",
        "content": (
            "<p>To <strong>bisect an angle</strong> means to draw a ray from its vertex that divides the original angle $\\angle AOB$ into two strictly equal halves: $\\angle AOC = \\angle BOC = \\frac{1}{2}\\angle AOB$.</p>"
            "<p class='mt-2'><strong>The Compass & Straightedge Method:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Place the compass needle at vertex $O$. Strike an arc of convenient radius $r_1$ intersecting ray $OA$ at $P$ and ray $OB$ at $Q$. (Note: $OP = OQ = r_1$).</li>"
            "<li>From point $P$, draw an arc inside the angle opening with radius $r_2$.</li>"
            "<li>With the <em>same radius</em> $r_2$, draw an arc from point $Q$ intersecting the previous arc at point $C$.</li>"
            "<li>Draw ray $OC$. This ray is the exact angle bisector of $\\angle AOB$!</li>"
            "</ol>"
            "<p class='mt-2'><strong>Proof via SSS Congruence:</strong> Consider triangles $\\triangle OPC$ and $\\triangle OQC$:</p>"
            "<div class='p-1 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$OP = OQ = r_1, \\quad PC = QC = r_2, \\quad OC \\text{ is common} \\implies \\triangle OPC \\cong \\triangle OQC \\text{ (SSS)}$$"
            "</div>"
            "<p class='mt-1'>Corresponding parts of congruent triangles (CPCT) prove $\\angle POC = \\angle QOC$. The angle is divided symmetrically!</p>"
        ),
        "key_takeaways": [
            "Angle bisection creates two equal adjacent angles sharing the vertex and bisector ray.",
            "Initial arc from vertex $O$ ensures equidistant arms: $OP = OQ = r_1$.",
            "Intersecting arcs create an equidistant interior point: $PC = QC = r_2$.",
            "Triangle congruence by SSS (Side-Side-Side) mathematically guarantees $\\angle POC = \\angle QOC$."
        ],
        "formula": "$$\\triangle OPC \\cong \\triangle OQC \\text{ (SSS)} \\implies \\angle AOC = \\angle BOC = \\frac{1}{2}\\angle AOB$$",
        "simulator_type": "angle_bisector_studio_sim",
        "checkpoints": [
            {
                "question": "If an angle of 76 degrees is bisected, what is the measure of each resulting half-angle?",
                "options": ["38 degrees", "35 degrees", "42 degrees", "152 degrees"],
                "correct": 0,
                "explanation": "Bisection divides an angle into two equal parts: 76° / 2 = 38°."
            },
            {
                "question": "In the angle bisection construction, which side is common to both triangles OPC and OQC?",
                "options": ["Side OP", "Side PC", "The bisector ray segment OC", "Side PQ"],
                "correct": 2,
                "explanation": "Segment OC connects the vertex O to the arc intersection C and is shared by both triangles (common side)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Repeating Units & Designing with Angle Bisection",
        "subtitle": "Generating 45°, 22.5°, Rosettes & Multi-Petalled Mandalas",
        "content": (
            "<p>Angle bisection is not merely an isolated textbook procedure—it is the generative engine of geometric art, floral mandalas, and intricate architectural ornamentation!</p>"
            "<p class='mt-2'>By applying angle bisection repeatedly, we produce geometric cascades:</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>Right Angle Cascade:</strong> $90^\\circ \\xrightarrow{\\text{bisect}} 45^\\circ \\xrightarrow{\\text{bisect}} 22.5^\\circ \\xrightarrow{\\text{bisect}} 11.25^\\circ$. Bisecting $90^\\circ$ gives the 8-pointed star compass rose!</li>"
            "<li><strong>Equilateral Cascade:</strong> $60^\\circ \\xrightarrow{\\text{bisect}} 30^\\circ \\xrightarrow{\\text{bisect}} 15^\\circ \\xrightarrow{\\text{bisect}} 7.5^\\circ$. This enables 12-petalled and 24-petalled circular designs!</li>"
            "<li><strong>Symmetric Flower Petals (Kolam / Rangoli):</strong> Starting with a circle divided into 4, 6, 8, or 12 equal sectors via angle bisection, striking compass arcs from peripheral intersection points creates interlocking curved petals with perfect bilateral symmetry!</li>"
            "</ul>"
            "<p class='mt-2'>Every traditional Indian <em>Yantra</em> and <em>Māṇḍala</em> uses this principle of repeated angle bisection to partition $360^\\circ$ into harmonic angular frequencies.</p>"
        ),
        "key_takeaways": [
            "Repeated angle bisection halves angle measures successively: $\\theta, \\frac{\\theta}{2}, \\frac{\\theta}{4}, \\frac{\\theta}{8}$.",
            "Bisecting a right angle ($90^\\circ$) yields $45^\\circ$, which creates 8-directional quadrant navigation grids.",
            "Bisecting $60^\\circ$ yields $30^\\circ$ and $15^\\circ$, generating 12-petalled and 24-petalled floral rosettes.",
            "Radial symmetry in traditional Indian Kolams, Rangolis, and Islamic tilework is generated through repeated bisections."
        ],
        "formula": "$$\\theta_k = \\frac{\\theta_0}{2^k}, \\quad \\text{Circle Partition: } N = 2^k \\times n_0 \\text{ equal angular sectors}$$",
        "simulator_type": "mandala_rosette_generator_sim",
        "checkpoints": [
            {
                "question": "Starting with a 90-degree angle, how many successive angle bisections are needed to obtain a 22.5-degree angle?",
                "options": ["1 bisection", "2 bisections", "3 bisections", "4 bisections"],
                "correct": 1,
                "explanation": "First bisection: 90° / 2 = 45°. Second bisection: 45° / 2 = 22.5°. Exactly 2 bisections are needed!"
            },
            {
                "question": "If a full circle (360 degrees) is divided into 8 equal sectors using repeated perpendicular and angle bisections, what is each central angle?",
                "options": ["30 degrees", "45 degrees", "60 degrees", "90 degrees"],
                "correct": 1,
                "explanation": "360° / 8 = 45° (or 90° / 2 = 45°). Each sector measures 45°."
            }
        ]
    },
    {
        "id": 7,
        "title": "Repeating Units & Repeating Angles",
        "subtitle": "Copying an Angle via Congruent Isosceles Triangles",
        "content": (
            "<p>To construct repeating patterns, friezes, and parallel lines, a geometer must be able to <strong>duplicate an angle</strong>—copying $\\angle A$ to a new vertex $P$ along a new ray, using only a compass and straightedge.</p>"
            "<p class='mt-2'><strong>How the Angle Copier Works:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Given original angle with vertex $O$. Draw an arc with center $O$ and radius $R$, intersecting the angle's rays at $X$ and $Y$. (This creates chord distance $XY$).</li>"
            "<li>At the new vertex $P$ on ray $L$, draw an identical arc of the <em>same radius</em> $R$, intersecting the ray at point $X'$.</li>"
            "<li>Set the compass opening equal to the chord distance between $X$ and $Y$ ($d = XY$).</li>"
            "<li>Place the compass needle at $X'$ and strike an arc of radius $d$ intersecting the first arc at point $Y'$.</li>"
            "<li>Draw the ray passing from $P$ through $Y'$.</li>"
            "</ol>"
            "<p class='mt-2'><strong>Congruence Proof:</strong> In $\\triangle OXY$ and $\\triangle PX'Y'$: $OX = PX' = R$, $OY = PY' = R$, and $XY = X'Y' = d$. By <strong>SSS Congruence</strong>, $\\triangle OXY \\cong \\triangle PX'Y'$. Hence $\\angle XOY = \\angle X'PY'$!</p>"
        ),
        "key_takeaways": [
            "Copying an angle reproduces the exact opening without measuring degrees with a protractor.",
            "The method constructs two congruent triangles by transferring two equal radius sides and the cross-chord length.",
            "SSS congruence guarantees that the copied angle precisely matches the original: $\\angle P = \\angle O$.",
            "This procedure is the core building block for drawing parallel lines, polygons, and repeated decorative friezes."
        ],
        "formula": "$$OX = PX' = R, \\; OY = PY' = R, \\; XY = X'Y' = d \\implies \\triangle OXY \\cong \\triangle PX'Y' \\implies \\angle P = \\angle O$$",
        "simulator_type": "angle_copier_sim",
        "checkpoints": [
            {
                "question": "What measurement does the compass capture in step 3 to ensure the duplicated angle matches the original angle?",
                "options": [
                    "The length of the entire ray to infinity",
                    "The straight-line chord distance between intersection points X and Y (XY)",
                    "The temperature of the paper",
                    "The perimeter of the drawing board"
                ],
                "correct": 1,
                "explanation": "The compass captures the chord width XY across the arc of radius R. Transferring this chord to the new arc guarantees congruent triangles by SSS!"
            },
            {
                "question": "Which triangle congruence criterion proves that the copied angle is equal to the original angle?",
                "options": ["AAA", "SSS (Side-Side-Side)", "SSA", "Angle-Side-Angle with no sides equal"],
                "correct": 1,
                "explanation": "Both radius sides (R) and the third chord side (d) are identical in both triangles. Congruence is rigorously proven by SSS!"
            }
        ]
    },
    {
        "id": 8,
        "title": "Constructing a Line Parallel to a Given Line",
        "subtitle": "Copying Corresponding Angles Along a Transversal",
        "content": (
            "<p>How do we draw a line that never meets a given line $L$ and passes through an external point $P$? By leveraging the <strong>Corresponding Angles Postulate</strong>!</p>"
            "<p class='mt-2'>If a transversal line intersects two coplanar lines such that a pair of <strong>corresponding angles are equal</strong>, then the two lines are strictly <strong>parallel</strong> ($m \\parallel L$).</p>"
            "<p class='mt-2'><strong>Construction Sequence:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Take any point $Q$ on line $L$. Draw a transversal line through $Q$ and external point $P$. This forms an angle $\\theta = \\angle PQR$ with line $L$.</li>"
            "<li>At vertex $P$, copy angle $\\angle PQR$ on the same side of the transversal line, so that the new angle $\\angle SPQ = \\theta$.</li>"
            "<li>Extend the ray $PS$ in both directions to form line $m$.</li>"
            "</ol>"
            "<p class='mt-2'>Because line $m$ and line $L$ make equal corresponding angles $\\theta$ with the transversal $QP$, lines $m$ and $L$ are mathematically guaranteed to be parallel!</p>"
        ),
        "key_takeaways": [
            "Parallel lines in a plane maintain a constant perpendicular distance and never intersect.",
            "Constructing a line parallel to line $L$ through point $P$ reduces to copying an angle along a transversal.",
            "The Corresponding Angles Axiom states: $\\angle 1 = \\angle 2 \\implies \\text{Line } m \\parallel \\text{Line } L$.",
            "Alternative equivalent constructions can use equal alternate interior angles (Z-shape)."
        ],
        "formula": "$$\\angle \\text{Corresponding}_1 = \\angle \\text{Corresponding}_2 \\implies m \\parallel L$$",
        "simulator_type": "parallel_line_transversal_sim",
        "checkpoints": [
            {
                "question": "Which geometric relationship between angles formed by a transversal proves that the constructed line is parallel to the original line?",
                "options": [
                    "The two angles sum to 90 degrees",
                    "A pair of corresponding angles (or alternate interior angles) are equal",
                    "The angles are both acute and different",
                    "The lines intersect at point P"
                ],
                "correct": 1,
                "explanation": "When a transversal intersects two lines such that corresponding angles are equal, Euclid's parallel postulate proves the lines are parallel."
            },
            {
                "question": "If the transversal makes an angle of 65 degrees with the original line L, what angle must be copied at point P to create a parallel line?",
                "options": ["25 degrees", "65 degrees", "115 degrees", "180 degrees"],
                "correct": 1,
                "explanation": "To make the lines parallel, the corresponding angle at point P must be identical: exactly 65 degrees!"
            }
        ]
    },
    {
        "id": 9,
        "title": "Architectural Arches: Trefoil & Pointed Arches",
        "subtitle": "Geometry of Heritage Structures: Red Fort's Diwan-i-Aam",
        "content": (
            "<p>Look at historic Indian monuments like the <strong>Diwan-i-Aam</strong> in Delhi's Red Fort, the Taj Mahal, or ancient rock-cut caves: their graceful, sweeping archways are masterpieces of compass and straightedge geometry!</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>Pointed Arch (Equilateral Gothic Arch):</strong> Formed by two circular arcs. An arc centered at base point $A$ passes through $B$ and sweeps upward; an identical arc centered at $B$ sweeps upward from $A$. They meet at apex $C$ directly above the center, forming an equilateral triangle of centers $\\triangle ABC$!</li>"
            "<li><strong>Trefoil Arch (Cusped Multi-Foil Arch):</strong> Features three overlapping circular foils (lobes) meeting at pointed cusps. It is constructed on an equilateral triangle framework where three circles of equal radius meet at $120^\\circ$ symmetry!</li>"
            "<li><strong>Supporting Geometric Skeleton:</strong> Behind every monumental arch lies a hidden skeleton of tangent circles, perpendicular bisectors, and harmonic ratios that distribute structural weight safely to the pillars.</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Architectural arches in heritage monuments are constructed from intersecting circular arcs.",
            "An equilateral pointed arch uses the span length as the radius from each springing point: $r = AB$.",
            "Trefoil (3-lobed) arches are constructed around an equilateral triangular grid with three intersecting circles.",
            "Geometric arches provide both structural stability (distributing compressive loads) and aesthetic harmony."
        ],
        "formula": "$$\\text{Pointed Arch Apex } C: AC = BC = AB = \\text{Span } s, \\quad \\text{Apex Height } h = \\frac{\\sqrt{3}}{2}s$$",
        "simulator_type": "historic_arch_architect_sim",
        "checkpoints": [
            {
                "question": "In an equilateral pointed arch spanning distance s between pillars A and B, what is the radius of each circular arc forming the arch?",
                "options": [
                    "Half the span: s/2",
                    "The full span: s (radius = AB)",
                    "Double the span: 2s",
                    "An arbitrary random radius"
                ],
                "correct": 1,
                "explanation": "In a classical equilateral pointed arch, each arc is drawn with a radius equal to the full span distance s, centered at the opposite springing pillar."
            },
            {
                "question": "How many circular lobes (foils) make up a classic Trefoil arch seen in medieval and Mughal architecture?",
                "options": ["Two lobes", "Three lobes", "Five lobes", "Eight lobes"],
                "correct": 1,
                "explanation": "'Trefoil' comes from Latin 'trifolium' (three leaves), consisting of three symmetrical circular lobes meeting at cusps."
            }
        ]
    },
    {
        "id": 10,
        "title": "Constructing a 60° Angle & Equilateral Triangles",
        "subtitle": "The Pure Radius Step: Side Equals Radius",
        "content": (
            "<p>The number $60^\\circ$ is one of the most magical angles in geometry because in an <strong>equilateral triangle</strong>, all three sides are equal ($s$), and all three interior angles measure exactly $60^\\circ$ ($3 \\times 60^\\circ = 180^\\circ$).</p>"
            "<p class='mt-2'><strong>Constructing 60° in Three Elegant Steps:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Draw a baseline ray with vertex $O$.</li>"
            "<li>With center $O$ and any radius $r$, draw an arc cutting the ray at point $A$. (Note: $OA = r$).</li>"
            "<li>Without altering the compass radius, place the needle at point $A$ and strike an arc cutting the first arc at point $B$. (Note: $AB = r$).</li>"
            "<li>Draw ray $OB$.</li>"
            "</ol>"
            "<p class='mt-2'>Since $OA = r$, $AB = r$, and $OB = r$ (as $B$ lies on the circle centered at $O$), triangle $\\triangle OAB$ is an <strong>equilateral triangle</strong>! Therefore, all its angles are equal, and $\\angle AOB = 60^\\circ$ exactly!</p>"
        ),
        "key_takeaways": [
            "Constructing a $60^\\circ$ angle requires NO protractor—only striking an arc with unchanged radius.",
            "Setting the chord distance equal to the radius ($AB = r$) forms an equilateral triangle $\\triangle OAB$.",
            "Since the interior angle sum of a triangle is $180^\\circ$, each angle in an equilateral triangle is $\\frac{180^\\circ}{3} = 60^\\circ$.",
            "This construction is the gateway to $30^\\circ$, $15^\\circ$, regular hexagons, and 6-pointed stars."
        ],
        "formula": "$$OA = OB = AB = r \\implies \\triangle OAB \\text{ is equilateral} \\implies \\angle AOB = 60^\\circ$$",
        "simulator_type": "equilateral_60_constructor_sim",
        "checkpoints": [
            {
                "question": "Why does striking an arc of radius r from point A to intersect the arc centered at O create exactly a 60-degree angle?",
                "options": [
                    "Because all three sides of triangle OAB become equal to r, creating an equilateral triangle where each angle is 180° / 3 = 60°",
                    "Because a compass only draws 60-degree angles by default",
                    "Because 60 is divisible by 10",
                    "Because point B is at infinity"
                ],
                "correct": 0,
                "explanation": "Since OA = OB = AB = r, triangle OAB has three equal sides. All angles in an equilateral triangle are equal to 180° / 3 = 60°."
            },
            {
                "question": "What happens if you accidentally change the compass opening between drawing the first arc from O and the second arc from A?",
                "options": [
                    "The angle will still be exactly 60 degrees",
                    "The triangle will no longer be equilateral, so the angle will not be 60 degrees",
                    "The line will become curved",
                    "The angle becomes 90 degrees"
                ],
                "correct": 1,
                "explanation": "The radius MUST remain unchanged so that AB = OA = r. Any change in compass width destroys the equilateral property!"
            }
        ]
    },
    {
        "id": 11,
        "title": "The Angle Hierarchy: 30°, 15°, 75°, 105° & Hexagrams",
        "subtitle": "Combinatorial Constructions & The Shatkona 6-Pointed Star",
        "content": (
            "<p>Once you master constructing $90^\\circ$ and $60^\\circ$, you can construct an entire family of precise angles using bisection, addition, and subtraction:</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>Halving Angles:</strong> Bisect $60^\\circ \\to 30^\\circ$. Bisect $30^\\circ \\to 15^\\circ$.</li>"
            "<li><strong>Angle Additions:</strong> $60^\\circ + 15^\\circ = 75^\\circ$ (or bisect the $30^\\circ$ gap between $60^\\circ$ and $90^\\circ$: $60^\\circ + 15^\\circ = 75^\\circ$).</li>"
            "<li><strong>Angle Combinations:</strong> $90^\\circ + 15^\\circ = 105^\\circ$; $90^\\circ + 45^\\circ = 135^\\circ$; $180^\\circ - 60^\\circ = 120^\\circ$.</li>"
            "<li><strong>The Shatkona (6-Pointed Star / Hexagram):</strong> Inverting one equilateral triangle over another centered at the same origin creates the ancient Indian <em>Shatkona</em> symbol (representing the union of Śiva and Śakti, Puruṣa and Prakṛti). All 12 boundary vertices and interior intersections are unlocked by $60^\\circ$ and $30^\\circ$ rays!</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Any angle of the form $k \\times 15^\\circ$ ($15^\\circ, 30^\\circ, 45^\\circ, 60^\\circ, 75^\\circ, 90^\\circ, 105^\\circ, \\dots$) can be constructed with straightedge and compass.",
            "Constructing $75^\\circ$ is done by bisecting the interval between $60^\\circ$ and $90^\\circ$ ($60^\\circ + \\frac{30^\\circ}{2} = 75^\\circ$).",
            "Constructing $105^\\circ$ is done by adding $15^\\circ$ to $90^\\circ$ ($90^\\circ + 15^\\circ = 105^\\circ$).",
            "Two interlocking congruent equilateral triangles rotated by $60^\\circ$ form the 6-pointed Shatkona hexagram."
        ],
        "formula": "$$\\text{Constructible Family: } \\theta = 15^\\circ \\times m, \\quad 75^\\circ = \\frac{60^\\circ + 90^\\circ}{2}, \\quad 105^\\circ = 90^\\circ + 15^\\circ$$",
        "simulator_type": "angle_hierarchy_shatkona_sim",
        "checkpoints": [
            {
                "question": "How can you construct an angle of 75 degrees using only straightedge and compass?",
                "options": [
                    "By guessing between 70 and 80 degrees",
                    "By constructing a 60-degree angle and a 90-degree angle, then bisecting the 30-degree angle between them (60° + 15° = 75°)",
                    "By tripling a 20-degree angle",
                    "It is mathematically impossible to construct 75 degrees"
                ],
                "correct": 1,
                "explanation": "Construct 60° and 90° on the same vertex. The angle between them is 90° - 60° = 30°. Bisecting this 30° angle gives 15°. Thus, 60° + 15° = 75°!"
            },
            {
                "question": "Which of the following angles CANNOT be constructed using only an unmarked ruler and compass via standard integer subdivisions of 60° and 90°?",
                "options": ["15 degrees", "45 degrees", "20 degrees", "105 degrees"],
                "correct": 2,
                "explanation": "20° cannot be constructed with an unmarked straightedge and compass because trisecting an arbitrary 60° angle is proven impossible by Pierre Wantzel (1837)!"
            }
        ]
    },
    {
        "id": 12,
        "title": "Regular Hexagons: Six Triangles Around a Point",
        "subtitle": "Stepping the Radius Around a Circle: 6 × 60° = 360°",
        "content": (
            "<p>A <strong>regular hexagon</strong> is a 6-sided polygon with all sides equal and all interior angles measuring $120^\\circ$. It holds a profound mathematical secret:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$\\text{Side Length of Inscribed Regular Hexagon } s = \\text{Radius } r$$"
            "</div>"
            "<p class='mt-2'><strong>The 'Walk-Around-the-Circle' Construction:</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>Draw a circle of radius $r$ centered at $O$.</li>"
            "<li>Pick any starting point $P_1$ on the circumference. With the compass radius still set to $r$, strike an arc to find $P_2$.</li>"
            "<li>Repeat from $P_2$ to find $P_3$, $P_4$, $P_5$, and $P_6$.</li>"
            "<li>The 6th step lands <em>exactly</em> back on the starting point $P_1$!</li>"
            "</ol>"
            "<p class='mt-2'>Connecting each vertex to center $O$ partitions the hexagon into <strong>six congruent equilateral triangles</strong>. At center $O$, the six angles meet: $6 \\times 60^\\circ = 360^\\circ$. Because $360^\\circ$ is fully closed with zero gap, the hexagon fits together in flawless radial symmetry!</p>"
        ),
        "key_takeaways": [
            "The side length of a regular hexagon inscribed in a circle is strictly equal to the circle's radius: $s = r$.",
            "Stepping the compass around the circumference visits exactly 6 equidistant vertices without changing radius.",
            "A regular hexagon decomposes into 6 congruent equilateral triangles sharing the central origin.",
            "Central angle sum: $6 \\times 60^\\circ = 360^\\circ$; interior vertex angles: $2 \\times 60^\\circ = 120^\\circ$."
        ],
        "formula": "$$s = r, \\quad \\sum \\angle_{\\text{center}} = 6 \\times 60^\\circ = 360^\\circ, \\quad \\angle_{\\text{interior}} = \\frac{(6-2)\\times 180^\\circ}{6} = 120^\\circ$$",
        "simulator_type": "regular_hexagon_stepper_sim",
        "checkpoints": [
            {
                "question": "If a regular hexagon is inscribed in a circle of radius 7 cm, what is the perimeter of the hexagon?",
                "options": ["21 cm", "35 cm", "42 cm", "49 cm"],
                "correct": 2,
                "explanation": "In an inscribed regular hexagon, side s = radius r = 7 cm. The perimeter is 6 * s = 6 * 7 = 42 cm!"
            },
            {
                "question": "Why do exactly six equilateral triangles fit together around a single central point with no gaps or overlaps?",
                "options": [
                    "Because each equilateral triangle has a 60° vertex angle, and 6 * 60° = 360°, which equals a full turn",
                    "Because circles have 6 sides",
                    "Because the compass has two legs",
                    "Because 6 is an even number"
                ],
                "correct": 0,
                "explanation": "A complete circular revolution is 360°. Since each equilateral triangle vertex measures 60°, exactly 360° / 60° = 6 triangles pack perfectly around the center."
            }
        ]
    },
    {
        "id": 13,
        "title": "The Mathematics of Tiling: Tangrams & Polygonal Covering",
        "subtitle": "Covering Regions Completely with No Gaps and No Overlaps",
        "content": (
            "<p>A <strong>tiling</strong> (or tessellation) is a collection of plane shapes called <em>tiles</em> that cover a target region completely such that:</p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li>There are <strong>no gaps</strong> between adjacent tiles.</li>"
            "<li>There are <strong>no overlaps</strong> between tiles (they touch only along edges or vertices).</li>"
            "</ol>"
            "<p class='mt-2'><strong>The 7-Piece Tangram:</strong> The celebrated Chinese <em>qi qiao ban</em> (Tangram puzzle) consists of 7 geometric pieces cut from a single parent square:</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li>$2$ large congruent isosceles right triangles (area $\\frac{1}{4}$ each).</li>"
            "<li>$1$ medium isosceles right triangle (area $\\frac{1}{8}$).</li>"
            "<li>$2$ small congruent isosceles right triangles (area $\\frac{1}{16}$ each).</li>"
            "<li>$1$ square (area $\\frac{1}{8}$) and $1$ parallelogram (area $\\frac{1}{8}$).</li>"
            "</ul>"
            "<p class='mt-2'><strong>Conservation of Area:</strong> Regardless of whether you assemble the 7 pieces into a running horse, a swan, or a rectangle, the total area is strictly conserved: $\\text{Total Area} = 2(\\frac{1}{4}) + \\frac{1}{8} + 2(\\frac{1}{16}) + \\frac{1}{8} + \\frac{1}{8} = 1$!</p>"
        ),
        "key_takeaways": [
            "A tiling covers a geometric region seamlessly: zero gaps and zero overlapping areas.",
            "The 7-piece Tangram demonstrates how complex figures can be tiled using a minimal set of polygon building blocks.",
            "Area is invariant under rigid motions (translations, rotations, reflections): total area remains constant.",
            "Decomposing polygons into unit triangles is a foundational method for proving geometric area formulas."
        ],
        "formula": "$$\\text{Tiling Rule: } \\bigcup_{i=1}^k T_i = \\Omega \\quad \\text{and} \\quad \\text{Area}(T_i \\cap T_j) = 0 \\; (i \\ne j) \\implies \\sum \\text{Area}(T_i) = \\text{Area}(\\Omega)$$",
        "simulator_type": "tangram_tessellation_sim",
        "checkpoints": [
            {
                "question": "What are the two fundamental defining conditions of a mathematical tiling?",
                "options": [
                    "All tiles must be circles and all colors must match",
                    "There must be NO gaps and NO overlaps between tiles",
                    "The tiles must be drawn with a wooden ruler only",
                    "The perimeter must be infinite"
                ],
                "correct": 1,
                "explanation": "By definition, a tiling must cover the plane or region completely without leaving any gaps and without any tiles overlapping."
            },
            {
                "question": "If the 7 pieces of a Tangram are rearranged from a square into a silhouette of a flying bird, what happens to the total area?",
                "options": [
                    "The area increases because wings spread out",
                    "The area decreases because of empty air around the bird",
                    "The total area remains exactly the same due to conservation of area",
                    "The area depends on the speed of the bird"
                ],
                "correct": 2,
                "explanation": "Rigid rearrangement of shapes preserves their individual areas. The sum of the areas of the 7 pieces is strictly conserved!"
            }
        ]
    },
    {
        "id": 14,
        "title": "Grid Tilings with 2×1 Dominoes & Parity",
        "subtitle": "Area Divisibility & Necessary Conditions for Grid Tilings",
        "content": (
            "<p>Can a given grid of square cells be completely covered by simple $2 \\times 1$ rectangular tiles (commonly called <strong>dominoes</strong>)?</p>"
            "<p class='mt-2'>Let the target grid have dimensions $m \\times n$, containing a total of $N = m \\times n$ unit squares. Each domino tile has dimensions $2 \\times 1$, covering exactly $2$ unit squares.</p>"
            "<p class='mt-2'><strong>The Fundamental Divisibility Criterion:</strong></p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$\\text{Total Area } = m \\times n = 2 \\times k \\implies m \\times n \\text{ must be an EVEN integer!}$$"
            "</div>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li>If both $m$ and $n$ are odd (e.g., $5 \\times 5 = 25$ cells), tiling with $2 \\times 1$ dominoes is <strong>mathematically impossible</strong>! Any attempt leaves at least $1$ uncovered square ($25 = 2 \\times 12 + 1$).</li>"
            "<li>If at least one dimension is even (e.g., $4 \\times 6 = 24$), the grid can always be tiled trivially by laying dominoes in parallel rows or columns.</li>"
            "<li>However, having an even total area is only a <em>necessary</em> condition, not always a <em>sufficient</em> condition when shapes are irregular!</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Each $2 \\times 1$ domino covers exactly 2 unit grid cells.",
            "A grid of $N$ cells can be tiled by dominoes only if $N$ is an even number: $N \\equiv 0 \\pmod 2$.",
            "An odd $\\times$ odd grid ($2k+1 \\times 2m+1$) has an odd total area and can NEVER be completely tiled by dominoes.",
            "Area parity is our first mathematical invariant tool to prove impossibility without exhaustive trial-and-error."
        ],
        "formula": "$$\\text{Necessary Condition: } \\text{Area}(\\text{Grid}) = m \\cdot n = 2k \\iff m \\text{ is even OR } n \\text{ is even}$$",
        "simulator_type": "domino_grid_tiling_sim",
        "checkpoints": [
            {
                "question": "Can a 7 × 9 rectangular checkerboard be completely tiled with 2 × 1 dominoes without overlapping?",
                "options": [
                    "Yes, by placing them diagonally",
                    "No, because the total area is 7 × 9 = 63, which is an odd number, leaving at least 1 square uncovered",
                    "Yes, because 7 and 9 are coprime",
                    "Only if the dominoes are cut into triangles"
                ],
                "correct": 1,
                "explanation": "Each domino covers 2 squares. Any number of dominoes covers an even total number of squares. Since 63 is odd, tiling is strictly impossible!"
            },
            {
                "question": "How many 2 × 1 dominoes are required to completely tile an 8 × 8 square chessboard?",
                "options": ["16 dominoes", "32 dominoes", "64 dominoes", "128 dominoes"],
                "correct": 1,
                "explanation": "Total squares = 8 * 8 = 64. Since each domino covers 2 squares, exactly 64 / 2 = 32 dominoes are needed."
            }
        ]
    },
    {
        "id": 15,
        "title": "The Black-and-White Coloring Invariant",
        "subtitle": "The Mutilated Chessboard Problem & Impossibility Proofs",
        "content": (
            "<p>Consider a standard $8 \\times 8$ chessboard with $64$ squares, colored alternately in black and white ($32$ white squares and $32$ black squares). Now, cut off and remove <strong>two diagonally opposite corner squares</strong>. We are left with $62$ squares.</p>"
            "<p class='mt-2'>Since $62$ is an even number, can this mutilated board be tiled with $31$ dominoes ($2 \\times 1$)?</p>"
            "<p class='mt-2'>Most people spend hours trying thousands of configurations. But a geometer solves it in 10 seconds using the <strong>Coloring Invariant</strong>!</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>The Invariant:</strong> Any $2 \\times 1$ domino placed anywhere on a chessboard—whether placed horizontally or vertically—MUST cover <strong>exactly one white square and exactly one black square</strong>!</li>"
            "<li>Therefore, $31$ dominoes must cover exactly $31$ white squares and $31$ black squares.</li>"
            "<li><strong>The Fatal Imbalance:</strong> On any standard chessboard, diagonally opposite corners have the <em>same color</em> (both white or both black). Removing them leaves $32$ squares of one color, but only $30$ squares of the other!</li>"
            "<li>Since $32 \\ne 30$, tiling the mutilated board is <strong>strictly impossible</strong>!</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Coloring squares in a dual checkerboard pattern creates a powerful mathematical invariant.",
            "Every $2 \\times 1$ domino covers exactly 1 black cell and 1 white cell: $\\Delta(B - W) = 0$.",
            "Diagonally opposite corners of a chessboard always share the identical color.",
            "Removing two same-colored corners breaks color parity ($32 \\ne 30$), rendering tiling mathematically impossible."
        ],
        "formula": "$$\\text{Each Domino: } \\{1B, 1W\\} \\implies 31 \\text{ Dominoes require } 31B + 31W. \\quad \\text{Board has } 30B + 32W \\implies \\text{IMPOSSIBLE}$$",
        "simulator_type": "mutilated_chessboard_sim",
        "checkpoints": [
            {
                "question": "Why can the 62-square mutilated chessboard (with two diagonally opposite corners removed) never be tiled by 31 dominoes?",
                "options": [
                    "Because 62 is not divisible by 2",
                    "Because both removed opposite corners have the same color, leaving 32 squares of one color and 30 of the other, whereas 31 dominoes require exactly 31 of each",
                    "Because dominoes cannot turn corners",
                    "Because the board is made of wood"
                ],
                "correct": 1,
                "explanation": "Every domino covers 1 white and 1 black square. Removing two opposite corners of the same color creates a 32 vs 30 imbalance, making tiling impossible!"
            },
            {
                "question": "What colors are the two diagonally opposite corners of any standard 8 × 8 chessboard?",
                "options": [
                    "Always opposite colors (one black, one white)",
                    "Always the exact same color (both white, or both black)",
                    "They have no color",
                    "They change color depending on viewing angle"
                ],
                "correct": 1,
                "explanation": "On an 8x8 chessboard, coordinates (1,1) and (8,8) have sum 1+1=2 (even) and 8+8=16 (even). They are guaranteed to be the exact same color!"
            }
        ]
    },
    {
        "id": 16,
        "title": "Tiling the Entire Plane: The Three Regular Tessellations",
        "subtitle": "Why Only Triangles, Squares & Hexagons Tile the Plane; Honeycombs & Escher",
        "content": (
            "<p>A <strong>regular tessellation</strong> is a tiling of the infinite plane using only a single type of regular polygon, meeting edge-to-edge. How many such polygons can tile the flat plane? <strong>Exactly THREE!</strong></p>"
            "<p class='mt-2'><strong>The Angle Sum Condition:</strong> For regular polygons to fit seamlessly around every shared vertex without gaps or overlaps, the sum of their interior angles must equal exactly $360^\\circ$:</p>"
            "<div class='p-1 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$k \\times \\theta = 360^\\circ \\implies k \\times \\frac{(n-2) \\times 180^\\circ}{n} = 360^\\circ \\implies \\frac{1}{n} + \\frac{1}{k} = \\frac{1}{2}$$"
            "</div>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>Equilateral Triangles ($n=3$):</strong> Interior angle $= 60^\\circ$. Exactly $6 \\times 60^\\circ = 360^\\circ$ ($6$ meet at a vertex).</li>"
            "<li><strong>Squares ($n=4$):</strong> Interior angle $= 90^\\circ$. Exactly $4 \\times 90^\\circ = 360^\\circ$ ($4$ meet at a vertex).</li>"
            "<li><strong>Regular Hexagons ($n=6$):</strong> Interior angle $= 120^\\circ$. Exactly $3 \\times 120^\\circ = 360^\\circ$ ($3$ meet at a vertex).</li>"
            "<li><strong>Why Regular Pentagons Fail ($n=5$):</strong> Angle $= 108^\\circ$. Three pentagons give $324^\\circ$ (gap of $36^\\circ$); four pentagons give $432^\\circ$ (overlap)!</li>"
            "<li><strong>Nature's Honeycomb & M.C. Escher:</strong> Honeybees build hexagonal wax cells because the <em>Honeycomb Theorem</em> proves hexagons minimize cell perimeter for a given storage area, saving precious wax! Dutch artist M.C. Escher transformed these geometric grids into interlocking birds, fish, and reptiles.</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Only three regular polygons tile the Euclidean plane: equilateral triangles, squares, and regular hexagons.",
            "The vertex angle sum must divide $360^\\circ$ evenly with an integer number of meeting polygons.",
            "Regular pentagons ($108^\\circ$) and octagons ($135^\\circ$) cannot tile the plane alone because $360^\\circ$ is not a multiple of their angles.",
            "The Honeycomb Theorem proves that hexagonal tessellations minimize total perimeter, maximizing storage efficiency for bees."
        ],
        "formula": "$$\\text{Vertex Condition: } k \\cdot \\theta = 360^\\circ \\implies \\{3^6, 4^4, 6^3\\} \\text{ are the ONLY three regular tessellations!}$$",
        "simulator_type": "master_tessellation_studio_sim",
        "checkpoints": [
            {
                "question": "Why cannot a floor be tiled using only regular pentagons with no gaps or overlaps?",
                "options": [
                    "Because pentagons are too sharp",
                    "Because each interior angle of a regular pentagon is 108°, and 360° is not evenly divisible by 108° (3 × 108° = 324°, leaving a 36° gap)",
                    "Because pentagons can only be drawn with a golden compass",
                    "Because bees do not like pentagons"
                ],
                "correct": 1,
                "explanation": "To tile around a vertex, interior angles must sum to 360°. Three pentagons leave a 36° gap (324°), and four overlap (432°). It is mathematically impossible!"
            },
            {
                "question": "What geometric advantage led bees to evolve the hexagonal honeycomb structure instead of square or triangular cells?",
                "options": [
                    "Hexagons are easier to count",
                    "Regular hexagons have the smallest perimeter for a given area, saving the maximum amount of beeswax",
                    "Hexagons produce sweeter honey",
                    "Square cells cannot hold liquids"
                ],
                "correct": 1,
                "explanation": "The Honeycomb Conjecture (proven by Thomas Hales in 1999) proves that a hexagonal grid divides a surface into equal-area cells with the minimal total perimeter, saving bees wax."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "subtitle": "Perpendicular Bisectors, 90° Angles, Śulba-Sūtras & The Eye",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q1",
                "question": "In the construction of a perpendicular bisector of segment AB, why must the compass radius r be strictly greater than half of AB?",
                "options": [
                    "To save paper space",
                    "Because if r ≤ AB/2, the circular arcs drawn from A and B will not intersect to form two reference points",
                    "To make the line horizontal",
                    "Because compasses cannot be set smaller than 5 cm"
                ],
                "correct": 1,
                "solution": "Step 1: The distance between A and B is AB.<br>Step 2: Two circles intersect if and only if the sum of their radii is greater than the center distance: $r + r > AB \\implies 2r > AB \\implies r > \\frac{AB}{2}$.<br>Step 3: If $r \\le AB/2$, the circles either touch at one point or do not meet at all, yielding zero pairs of intersection points above and below the line."
            },
            {
                "id": "q2",
                "question": "If point P lies on the perpendicular bisector of segment XY, and PX = 8.5 cm, what is the length of PY?",
                "options": ["4.25 cm", "8.5 cm", "17.0 cm", "Cannot be determined"],
                "correct": 1,
                "solution": "Step 1: By the Perpendicular Bisector Theorem, every point on the perpendicular bisector of a line segment is equidistant from the two endpoints.<br>Step 2: Therefore, $PY = PX$.<br>Step 3: Since $PX = 8.5\\text{ cm}$, $PY = 8.5\\text{ cm}$."
            },
            {
                "id": "q3",
                "question": "In the symmetric 'eye' construction with segment AB = 6 cm and two circles of radius 6 cm, what kind of polygon is formed by vertices A, X, B, Y?",
                "options": [
                    "A square",
                    "An equilateral rhombus with side length 6 cm",
                    "A scalene kite",
                    "A trapezium"
                ],
                "correct": 1,
                "solution": "Step 1: Point X is on both circles, so $AX = 6\\text{ cm}$ and $BX = 6\\text{ cm}$.<br>Step 2: Point Y is on both circles, so $AY = 6\\text{ cm}$ and $BY = 6\\text{ cm}$.<br>Step 3: A quadrilateral with all four sides equal ($AX = XB = BY = YA = 6\\text{ cm}$) is an equilateral rhombus."
            },
            {
                "id": "q4",
                "question": "When erecting a 90° angle at a point P on a straight line, why do we first mark points A and B such that AP = PB?",
                "options": [
                    "To convert the problem into finding the perpendicular bisector of segment AB passing through its midpoint P",
                    "To test the sharpness of the pencil",
                    "To measure the length of the line",
                    "To ensure the line is parallel to the equator"
                ],
                "correct": 0,
                "solution": "Step 1: If $AP = PB$, then $P$ is the exact midpoint of $AB$.<br>Step 2: The perpendicular bisector of $AB$ passes through its midpoint $P$ at $90^\\circ$.<br>Step 3: Any point $C$ equidistant from $A$ and $B$ lies on this bisector, so ray $PC \\perp AB$ at $P$."
            },
            {
                "id": "q5",
                "question": "Which ancient Indian geometric text describes the construction of true perpendiculars and ritual altars using knotted measuring cords and pegs?",
                "options": [
                    "Kātyāyana-Śulbasūtra",
                    "Nāṭyaśāstra",
                    "Arthaśāstra",
                    "Charaka Saṃhitā"
                ],
                "correct": 0,
                "solution": "Step 1: The Śulba-Sūtras (including Baudhāyana, Āpastamba, and Kātyāyana) are ancient Indian treatises on altar geometry.<br>Step 2: The Kātyāyana-Śulbasūtra explicitly outlines rope-and-peg constructions of cardinal perpendicular lines."
            },
            {
                "id": "q6",
                "question": "In triangle APB, if PA = PB, what is the line of symmetry of the triangle?",
                "options": [
                    "Side AB",
                    "The perpendicular bisector of base AB passing through vertex P",
                    "A line through A parallel to PB",
                    "The triangle has no line of symmetry"
                ],
                "correct": 1,
                "solution": "Step 1: Triangle $APB$ is an isosceles triangle with $PA = PB$.<br>Step 2: The altitude from vertex $P$ to base $AB$ bisects $AB$ at right angles.<br>Step 3: This line is the perpendicular bisector of $AB$ and the bilateral axis of symmetry."
            },
            {
                "id": "q7",
                "question": "In the Śulba-Sūtra altar orientation method, what astronomical phenomenon was used to establish the initial East-West Prācī line?",
                "options": [
                    "The position of the Pole Star at midnight",
                    "The shadow cast by a vertical gnomon (pole) on a horizontal surface at equal times before and after midday",
                    "The direction of monsoon winds",
                    "The flight path of eagles"
                ],
                "correct": 1,
                "solution": "Step 1: A vertical gnomon (*śanku*) casts shadows throughout the day.<br>Step 2: Points on a circle centered at the gnomon where the shadow tip touches in forenoon and afternoon mark true West and East.<br>Step 3: Joining them gives the cardinal baseline Prācī."
            },
            {
                "id": "q8",
                "question": "How many reference points are necessary and sufficient to determine a unique straight line in Euclidean geometry?",
                "options": ["1 point", "2 distinct points", "3 points", "4 points"],
                "correct": 1,
                "solution": "Step 1: Euclid's First Postulate states that a straight line may be drawn from any one point to any other point.<br>Step 2: Two distinct points uniquely define a line."
            },
            {
                "id": "q9",
                "question": "In constructing a perpendicular bisector of segment AB of length 10 cm, which of the following compass radii CANNOT be used?",
                "options": ["6 cm", "8 cm", "4 cm", "12 cm"],
                "correct": 2,
                "solution": "Step 1: The compass radius must satisfy $r > \\frac{AB}{2}$.<br>Step 2: Here $\\frac{AB}{2} = \\frac{10}{2} = 5\\text{ cm}$.<br>Step 3: Radius $4\\text{ cm} < 5\\text{ cm}$, so arcs of radius 4 cm will never intersect!"
            },
            {
                "id": "q10",
                "question": "What is the angle between the two diagonals of any rhombus constructed by intersecting compass arcs?",
                "options": ["45 degrees", "60 degrees", "90 degrees", "120 degrees"],
                "correct": 2,
                "solution": "Step 1: In any rhombus with four equal sides, the diagonals are mutual perpendicular bisectors.<br>Step 2: Therefore, they meet at exactly $90^\\circ$."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "subtitle": "Angle Bisections, Angle Duplication, Parallel Lines & Arches",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q11",
                "question": "If an angle of 140° is bisected, and one of the resulting angles is bisected again, what is the measure of the smallest angle produced?",
                "options": ["70 degrees", "35 degrees", "25 degrees", "17.5 degrees"],
                "correct": 1,
                "solution": "Step 1: First bisection: $140^\\circ / 2 = 70^\\circ$.<br>Step 2: Second bisection: $70^\\circ / 2 = 35^\\circ$."
            },
            {
                "id": "q12",
                "question": "In the compass construction to copy an angle, which property ensures that the new angle is identical to the original?",
                "options": [
                    "SSS Congruence between the triangle on the original angle and the triangle on the new ray",
                    "Measuring the degrees with a transparent protractor",
                    "Extending both rays to 10 cm",
                    "Drawing circles with different radii"
                ],
                "correct": 0,
                "solution": "Step 1: The original angle contains triangle with sides $R, R, d$.<br>Step 2: The copied angle is constructed with the identical side lengths $R, R, d$.<br>Step 3: By SSS congruence, corresponding angles are strictly equal."
            },
            {
                "id": "q13",
                "question": "To construct a line parallel to line L through point P, we draw a transversal line through P intersecting L at Q. What is the next essential step?",
                "options": [
                    "Measure line L with a ruler",
                    "Copy the angle formed at Q by the transversal and line L at point P so that corresponding angles are equal",
                    "Erect a 45-degree angle at Q",
                    "Draw a random line through P"
                ],
                "correct": 1,
                "solution": "Step 1: The transversal creates an angle $\\theta$ with line $L$ at $Q$.<br>Step 2: By copying this angle at vertex $P$ on the transversal, we produce equal corresponding angles.<br>Step 3: Equal corresponding angles guarantee the lines are parallel."
            },
            {
                "id": "q14",
                "question": "An equilateral pointed arch has span AB = 4 meters. What is the radius of the circular arcs that form the arch?",
                "options": ["2 meters", "4 meters", "8 meters", "16 meters"],
                "correct": 1,
                "solution": "Step 1: In an equilateral pointed arch, each arc is drawn from one base springing point to the other.<br>Step 2: Hence, radius $r = \\text{span} = AB = 4\\text{ meters}$."
            },
            {
                "id": "q15",
                "question": "If a line m is parallel to line L, and a transversal line intersects them such that one interior angle on line L is 72°, what is the corresponding angle on line m?",
                "options": ["18 degrees", "72 degrees", "108 degrees", "144 degrees"],
                "correct": 1,
                "solution": "Step 1: Corresponding angles formed by a transversal across parallel lines are strictly equal.<br>Step 2: Therefore, the corresponding angle is $72^\\circ$."
            },
            {
                "id": "q16",
                "question": "If you wish to divide a 360° full circular rotation into 16 equal decorative sectors using angle bisection, how many successive bisections of a 90° quadrant are needed?",
                "options": ["1 bisection", "2 bisections", "3 bisections", "4 bisections"],
                "correct": 1,
                "solution": "Step 1: A quadrant is $360^\\circ / 4 = 90^\\circ$.<br>Step 2: We need 16 sectors, so each sector must be $360^\\circ / 16 = 22.5^\\circ$.<br>Step 3: Bisecting $90^\\circ$ gives $45^\\circ$ (1st bisection).<br>Step 4: Bisecting $45^\\circ$ gives $22.5^\\circ$ (2nd bisection). Exactly 2 bisections of the quadrant are needed."
            },
            {
                "id": "q17",
                "question": "In the trefoil arch design found in historic architecture like the Red Fort's Diwan-i-Aam, what geometric polygon forms the underlying symmetry framework?",
                "options": ["An equilateral triangle", "A scalene trapezoid", "A regular nonagon", "A square"],
                "correct": 0,
                "solution": "Step 1: A trefoil arch contains three identical circular lobes meeting at $120^\\circ$ rotational symmetry.<br>Step 2: The centers of these three lobes form the vertices of an equilateral triangle."
            },
            {
                "id": "q18",
                "question": "What happens if two lines in a plane are cut by a transversal such that consecutive interior angles sum to 180°?",
                "options": [
                    "The lines intersect at a 45° angle",
                    "The two lines are parallel",
                    "The two lines are perpendicular",
                    "The lines coincide as a single line"
                ],
                "correct": 1,
                "solution": "Step 1: By Euclid's Parallel Postulate (and interior angle theorem), if consecutive interior angles sum to $180^\\circ$, the lines never meet.<br>Step 2: Hence, the lines are parallel."
            },
            {
                "id": "q19",
                "question": "Which tool is strictly forbidden when performing classical Euclidean geometric constructions?",
                "options": [
                    "An unmarked straightedge",
                    "A compass",
                    "A protractor with marked degree graduations",
                    "A sharp pencil"
                ],
                "correct": 2,
                "solution": "Step 1: Classical Euclidean constructions permit only an unmarked straightedge and a compass.<br>Step 2: Marked rulers and protractors are excluded because geometry must be derived purely by logical construction, not mechanical reading."
            },
            {
                "id": "q20",
                "question": "If angle AOB is bisected by ray OC, and angle AOC = (3x + 5)° while angle BOC = (5x - 15)°, what is the value of x?",
                "options": ["5", "10", "15", "20"],
                "correct": 1,
                "solution": "Step 1: Since $OC$ is the angle bisector, $\\angle AOC = \\angle BOC$.<br>Step 2: Set $3x + 5 = 5x - 15$.<br>Step 3: $5 + 15 = 5x - 3x \\implies 20 = 2x \\implies x = 10$."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "subtitle": "60°, 30°, 15° Angles, Regular Hexagons & Central Packing",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q21",
                "question": "What is the interior angle of a regular hexagon?",
                "options": ["60 degrees", "108 degrees", "120 degrees", "135 degrees"],
                "correct": 2,
                "solution": "Step 1: Interior angle formula $= \\frac{(n-2) \\times 180^\\circ}{n}$.<br>Step 2: For $n = 6$: $\\frac{(6-2) \\times 180^\\circ}{6} = \\frac{4 \\times 180^\\circ}{6} = \\frac{720^\\circ}{6} = 120^\\circ$."
            },
            {
                "id": "q22",
                "question": "How can an angle of 45° be constructed using compass and straightedge?",
                "options": [
                    "By dividing 180° into four parts using repeated perpendicular bisector constructions",
                    "By drawing a random angle and guessing",
                    "By bisecting a 60° angle",
                    "By tripling a 15° angle without construction"
                ],
                "correct": 0,
                "solution": "Step 1: Construct a $90^\\circ$ right angle by erecting a perpendicular.<br>Step 2: Bisect the $90^\\circ$ angle with a compass.<br>Step 3: $90^\\circ / 2 = 45^\\circ$."
            },
            {
                "id": "q23",
                "question": "Why does a compass walk around a circle of radius r step exactly 6 times back to the starting point?",
                "options": [
                    "Because each step subtends a central angle of 60° in an equilateral triangle, and 6 × 60° = 360°",
                    "Because all circles have a circumference of 6r",
                    "Because the straightedge has 6 edges",
                    "Because 6 is a prime number"
                ],
                "correct": 0,
                "solution": "Step 1: Connecting two adjacent step points to the circle center forms a triangle with sides $r, r, r$ (equilateral).<br>Step 2: The central angle of an equilateral triangle is $60^\\circ$.<br>Step 3: A full circle is $360^\\circ$. Exactly $360^\\circ / 60^\\circ = 6$ steps complete the round."
            },
            {
                "id": "q24",
                "question": "How do you construct a 105° angle using standard constructible angles?",
                "options": [
                    "By bisecting 210°",
                    "By constructing a 90° right angle and adding a constructed 15° angle (90° + 15° = 105°)",
                    "By subtracting 15° from 60°",
                    "By multiplying 30° by 3"
                ],
                "correct": 1,
                "solution": "Step 1: Construct a $90^\\circ$ perpendicular.<br>Step 2: Construct an adjacent $60^\\circ$ angle and bisect it twice to obtain $15^\\circ$.<br>Step 3: $90^\\circ + 15^\\circ = 105^\\circ$."
            },
            {
                "id": "q25",
                "question": "What is the area of a regular hexagon with side length s = 4 cm?",
                "options": [
                    "24 cm²",
                    "24√3 cm² (approx 41.57 cm²)",
                    "48 cm²",
                    "16√3 cm²"
                ],
                "correct": 1,
                "solution": "Step 1: A regular hexagon decomposes into 6 equilateral triangles of side $s$.<br>Step 2: Area of one equilateral triangle $= \\frac{\\sqrt{3}}{4}s^2 = \\frac{\\sqrt{3}}{4}(4^2) = 4\\sqrt{3}\\text{ cm}^2$.<br>Step 3: Total area $= 6 \\times 4\\sqrt{3} = 24\\sqrt{3}\\text{ cm}^2 \\approx 41.57\\text{ cm}^2$."
            },
            {
                "id": "q26",
                "question": "Which ancient 6-pointed star figure is formed by superimposing two congruent equilateral triangles rotated by 60°?",
                "options": ["Pentagram", "Shatkona (Hexagram)", "Octagram", "Decagram"],
                "correct": 1,
                "solution": "Step 1: Superimposing two equilateral triangles with inverted orientations yields a 6-pointed star.<br>Step 2: In Indian sacred geometry and architecture, this is the celebrated Shatkona."
            },
            {
                "id": "q27",
                "question": "Can an angle of 20° be constructed using only an unmarked ruler and compass?",
                "options": [
                    "Yes, by trisecting a 60° angle with a compass",
                    "No, because the trisection of an arbitrary 60° angle is mathematically proven impossible with straightedge and compass",
                    "Yes, by bisecting a 40° angle",
                    "Yes, using five 4° angles"
                ],
                "correct": 1,
                "solution": "Step 1: Constructing $20^\\circ$ would require trisecting $60^\\circ$.<br>Step 2: Pierre Wantzel proved in 1837 that angle trisection requires solving a cubic equation $4\\cos^3(20^\\circ) - 3\\cos(20^\\circ) = \\frac{1}{2}$, which cannot be expressed using square roots alone.<br>Step 3: Hence, $20^\\circ$ is strictly non-constructible with classical tools."
            },
            {
                "id": "q28",
                "question": "If the side length of an equilateral triangle is 6 cm, what is the length of its altitude?",
                "options": ["3 cm", "3√3 cm (approx 5.2 cm)", "6√3 cm", "4.5 cm"],
                "correct": 1,
                "solution": "Step 1: An altitude drops perpendicular to the base, bisecting it into two segments of $3\\text{ cm}$.<br>Step 2: By Pythagoras theorem, $h^2 + 3^2 = 6^2 \\implies h^2 + 9 = 36 \\implies h^2 = 27$.<br>Step 3: $h = \\sqrt{27} = 3\\sqrt{3}\\text{ cm} \\approx 5.196\\text{ cm}$."
            },
            {
                "id": "q29",
                "question": "How many lines of symmetry does a regular hexagon possess?",
                "options": ["3", "4", "6", "12"],
                "correct": 2,
                "solution": "Step 1: 3 lines of symmetry pass through pairs of opposite vertices.<br>Step 2: 3 lines of symmetry pass through the midpoints of opposite sides.<br>Step 3: Total lines of symmetry $= 3 + 3 = 6$."
            },
            {
                "id": "q30",
                "question": "If you bisect a 30° angle, what angle do you obtain?",
                "options": ["10 degrees", "15 degrees", "20 degrees", "25 degrees"],
                "correct": 1,
                "solution": "Step 1: Bisecting an angle divides its measure by 2.<br>Step 2: $30^\\circ / 2 = 15^\\circ$."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "subtitle": "Tangrams, Grid Tilings, Parity Invariants & Master Tessellations",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q31",
                "question": "What is the sum of the angles around any interior vertex in a flat plane tiling?",
                "options": ["180 degrees", "270 degrees", "360 degrees", "720 degrees"],
                "correct": 2,
                "solution": "Step 1: A complete turn around a point in the flat Euclidean plane is a full circle.<br>Step 2: To leave zero gap and zero overlap, the angles of all polygons meeting at that vertex must sum to exactly $360^\\circ$."
            },
            {
                "id": "q32",
                "question": "How many regular polygons can individually tile the infinite 2D plane in a regular tessellation?",
                "options": ["Only 1 (Square)", "Exactly 3 (Equilateral triangle, Square, Regular hexagon)", "5 (All Platonic shapes)", "Infinitely many"],
                "correct": 1,
                "solution": "Step 1: The condition is $k \\times \\theta = 360^\\circ$ where $\\theta = \\frac{(n-2)180^\\circ}{n}$.<br>Step 2: This simplifies to $\\frac{1}{n} + \\frac{1}{k} = \\frac{1}{2}$.<br>Step 3: The only integer solutions $(n, k)$ for $n \\ge 3$ are $(3, 6)$, $(4, 4)$, and $(6, 3)$.<br>Step 4: Thus, only equilateral triangles, squares, and regular hexagons can tile the plane."
            },
            {
                "id": "q33",
                "question": "Can a 5 × 7 rectangular grid of square cells be completely covered by 2 × 1 dominoes?",
                "options": [
                    "Yes, by turning them vertically",
                    "No, because the total area is 5 × 7 = 35 cells, which is an odd number, so at least 1 cell is always left uncovered",
                    "Yes, if we start from the center",
                    "Only on Thursdays"
                ],
                "correct": 1,
                "solution": "Step 1: Total area $= 5 \\times 7 = 35$ unit squares.<br>Step 2: Each domino covers exactly 2 unit squares.<br>Step 3: Any integer number of dominoes $k$ covers $2k$ squares (an even number).<br>Step 4: Since 35 is odd, $2k = 35$ has no integer solution. Tiling is impossible."
            },
            {
                "id": "q34",
                "question": "In the mutilated chessboard problem, two diagonally opposite corners are removed from an 8 × 8 board. Why can the remaining 62 squares never be tiled by 31 dominoes?",
                "options": [
                    "Because 62 is odd",
                    "Because each domino covers 1 black and 1 white square, but removing two opposite corners of the same color leaves 32 squares of one color and 30 of the other",
                    "Because the board falls apart",
                    "Because 8 is divisible by 4"
                ],
                "correct": 1,
                "solution": "Step 1: Opposite corners on an 8x8 chessboard always share the same color (e.g., both white).<br>Step 2: Removing them leaves $30$ white and $32$ black squares.<br>Step 3: 31 dominoes must cover exactly 31 white and 31 black squares.<br>Step 4: Since $30 \\ne 31$, tiling is mathematically impossible."
            },
            {
                "id": "q35",
                "question": "If a regular polygon has an interior angle of 135° (regular octagon), can it tile the plane alone?",
                "options": [
                    "Yes, because 135 is an odd multiple of 5",
                    "No, because 360° is not divisible by 135° (2 × 135° = 270°, 3 × 135° = 405°), leaving either a gap or an overlap",
                    "Yes, if octagons are placed diagonally",
                    "Yes, bees use octagons"
                ],
                "correct": 1,
                "solution": "Step 1: Check vertex condition: $360^\\circ / 135^\\circ = 2.666\\dots$<br>Step 2: Since $2.666$ is not an integer, octagons cannot meet edge-to-edge around a point without gaps.<br>Step 3: Two octagons give $270^\\circ$ (leaving a $90^\\circ$ gap, which can only be filled by a square in a semi-regular tiling)."
            },
            {
                "id": "q36",
                "question": "What mathematical theorem proved in 1999 by Thomas Hales explains why honeybees build hexagonal honeycombs?",
                "options": [
                    "The Honeycomb Theorem (hexagons divide a surface into equal-area cells with the minimal total perimeter)",
                    "Pythagoras' Theorem",
                    "Euler's Polyhedral Formula",
                    "Fermat's Last Theorem"
                ],
                "correct": 0,
                "solution": "Step 1: The Honeycomb Conjecture states that regular hexagonal grids are the most economical way to partition a plane into equal areas with the least perimeter.<br>Step 2: Thomas Hales gave the rigorous mathematical proof in 1999."
            },
            {
                "id": "q37",
                "question": "How many pieces are in a standard traditional Chinese Tangram puzzle?",
                "options": ["5 pieces", "7 pieces", "9 pieces", "12 pieces"],
                "correct": 1,
                "solution": "Step 1: A traditional Tangram contains exactly 7 pieces: 5 triangles (2 large, 1 medium, 2 small), 1 square, and 1 parallelogram."
            },
            {
                "id": "q38",
                "question": "Which celebrated Dutch artist is world-famous for transforming regular geometric tessellations into interlocking figures of birds, fish, and lizards?",
                "options": ["Vincent van Gogh", "M. C. Escher", "Rembrandt", "Johannes Vermeer"],
                "correct": 1,
                "solution": "Step 1: M. C. Escher (1898–1972) created legendary woodcuts and lithographs based on mathematical symmetries, reflections, and tessellations."
            },
            {
                "id": "q39",
                "question": "In a semi-regular tessellation where regular octagons and squares tile the plane (8.8.4), how many octagons and how many squares meet at each vertex?",
                "options": [
                    "1 octagon and 2 squares",
                    "2 octagons and 1 square (135° + 135° + 90° = 360°)",
                    "3 octagons and 1 square",
                    "4 squares only"
                ],
                "correct": 1,
                "solution": "Step 1: The interior angle of a regular octagon is $135^\\circ$.<br>Step 2: The interior angle of a square is $90^\\circ$.<br>Step 3: Sum at vertex $= 135^\\circ + 135^\\circ + 90^\\circ = 360^\\circ$. Exactly 2 octagons and 1 square meet at every vertex."
            },
            {
                "id": "q40",
                "question": "What is an aperiodic tiling of the plane?",
                "options": [
                    "A tiling that has holes",
                    "A non-repeating tiling that covers the plane without gaps or overlaps but never repeats in a translational periodic pattern (like Penrose tilings)",
                    "A tiling that only lasts for one hour",
                    "A tiling made of circles"
                ],
                "correct": 1,
                "solution": "Step 1: An aperiodic tiling covers the infinite plane completely with no gaps or overlaps, yet lacks translational symmetry (it never repeats periodically).<br>Step 2: Discovered by Roger Penrose in 1974, and recent 'Ein-Stein' single-tile discoveries in 2023!"
            }
        ]
    }
]

if __name__ == "__main__":
    with open(".agents/class7_math_constructions_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Mathematics Chapter 6: Constructions and Tilings Data File"""\n\n')
        f.write("SLIDES_DATA = " + repr(SLIDES_DATA) + "\n")
    print(f"Successfully generated .agents/class7_math_constructions_data.py with {len(SLIDES_DATA)} slides.")

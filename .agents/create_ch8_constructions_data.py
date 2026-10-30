# -*- coding: utf-8 -*-
"""
Data generator for NCERT Class 6 Mathematics Chapter 8: Playing with Constructions
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, \circ, etc.).
All math rendered in clean Unicode (°, •, ², ³, ⁿ, ₁, ₂, ×, ÷, +, −, =, ≠, ≤, ≥, √, π, →, 1/2, 3/4).
"""

CHAPTER_META = {
    "title": "NCERT Class 6 Mathematics • Chapter 8 • Constructions",
    "mentors": "Acharya Baudhāyana & Euclid of Alexandria (Masters of Sulba Cord Geometry & Compass-and-Straightedge Constructions)",
    "description": "Comprehensive 20-slide interactive master lab covering freehand vs instrument drawing, circles and radius, wave and eye arc motifs, properties of rectangles and squares, vertex naming rules, rotated shapes on dot grids, step-by-step square and rectangle construction, point distance variation, decomposing rectangles into squares, nested shapes and hole designs, diagonal lengths and angle splits, construction from side and diagonal, equidistant point arc intersections, and composite structural construction."
}

SLIDES = [
    # Slide 1: Ruler & Compass
    {
        "id": 1,
        "badge": "Core Concept",
        "title": "Ruler & Compass",
        "subtitle": "Precision Instruments vs Freehand Sketching",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                In art, freehand sketching allows expressive, approximate forms. In geometry, however, precision is paramount. We use two classical instruments to create exact geometric shapes:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='flex items-start gap-2'>
                    <span class='px-2 py-0.5 rounded font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0'>Ruler (Straightedge)</span>
                    <span class='text-slate-300'>Used to draw perfectly straight line segments and to measure linear distances in centimeters and millimeters.</span>
                </div>
                <div class='flex items-start gap-2'>
                    <span class='px-2 py-0.5 rounded font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0'>Compass</span>
                    <span class='text-slate-300'>Used to draw circles and arcs of fixed radii, and to transfer exact lengths from one segment to another without reading numeric markings.</span>
                </div>
                <div class='flex items-start gap-2'>
                    <span class='px-2 py-0.5 rounded font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0'>Protractor</span>
                    <span class='text-slate-300'>Used to measure and construct exact angles, particularly the critical 90° right angles needed for squares and rectangles.</span>
                </div>
            </div>
            <p class='text-xs text-slate-400 leading-relaxed'>
                A geometric construction differs from a simple drawing because every line, corner, and arc is defined by logical geometric relationships rather than guesswork.
            </p>
        """,
        "summary": "Geometry requires precision instruments: a straightedge for lines, a compass for circles and length transfers, and a protractor for angles.",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "Which instrument is used to transfer an exact length from one line to another without reading ruler numbers?",
                "options": ["Compass", "Protractor", "Eraser", "Set-square only"],
                "correct": 0,
                "explanation": "A compass locks in a fixed span between its needle and pencil tip, allowing exact transfer of lengths without numeric ruler error."
            },
            {
                "id": "cp1_2",
                "question": "What is the primary difference between a freehand drawing and a geometric construction?",
                "options": [
                    "Freehand drawings use colored ink",
                    "Constructions rely on precision instruments and exact geometric rules",
                    "Freehand drawings are always larger",
                    "Constructions cannot contain curves"
                ],
                "correct": 1,
                "explanation": "Constructions strictly obey geometric theorems and instrument-guided steps, ensuring exact angle and length specifications."
            }
        ]
    },

    # Slide 2: Circles & Radius
    {
        "id": 2,
        "badge": "Core Concept",
        "title": "Circles & Radius",
        "subtitle": "The Locus of Points Equidistant from a Central Point",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A <span class='text-amber-400 font-semibold'>curve</span> is any continuous path drawn on paper without lifting the pencil. When points are plotted such that every single point is at the exact same distance from a fixed center point <span class='font-mono text-cyan-300'>P</span>, they form a <span class='text-amber-400 font-semibold'>circle</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Center (P):</span> The fixed interior point where the metal compass needle rests.<br>
                    • <span class='text-cyan-300 font-bold'>Radius (r):</span> The constant distance from the center to any point on the boundary curve (e.g., r = 4 cm).<br>
                    • <span class='text-emerald-300 font-bold'>Diameter (d):</span> A straight segment passing through the center connecting two boundary points (d = 2 × r = 8 cm).
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 text-xs'>
                    Geometric Definition: Circle = { Point X : Distance(P, X) = r }
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                If the compass needle slips, the radius varies, and the resulting curve is no longer a circle.
            </p>
        """,
        "summary": "A circle is the set of all points at a fixed distance (radius r) from a central point P. Diameter is twice the radius (d = 2r).",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "If a compass is set to an opening of 5 cm and rotated about point P, what is the diameter of the resulting circle?",
                "options": ["5 cm", "10 cm", "2.5 cm", "25 cm"],
                "correct": 1,
                "explanation": "The compass opening sets the radius (r = 5 cm). The diameter is twice the radius: d = 2 × 5 cm = 10 cm."
            },
            {
                "id": "cp2_2",
                "question": "Which of the following points lies OUTSIDE a circle of radius 4 cm centered at point O?",
                "options": [
                    "A point at distance 3.5 cm from O",
                    "A point at distance 4.0 cm from O",
                    "A point at distance 4.8 cm from O",
                    "A point at distance 0 cm from O (the center)"
                ],
                "correct": 2,
                "explanation": "Points at a distance strictly greater than the radius (4.8 cm > 4.0 cm) lie outside the circle."
            }
        ]
    },

    # Slide 3: Waves & Motifs
    {
        "id": 3,
        "badge": "Core Concept",
        "title": "Waves & Motifs",
        "subtitle": "Constructing Semicircles, Waves & Eye Arcs",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                By placing the compass needle at strategically spaced points along a straight baseline, we can construct elegant repeating curves and natural motifs:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Three Classical Arc Constructions:</p>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>The Wavy Wave:</span> Divide a baseline AB (e.g., 8 cm) into equal 2 cm intervals. Draw alternating semicircles: first above the line using center C₁, then below using center C₂, producing an undulating continuous wave.
                </p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>The Symmetrical Eye:</span> Mark two points B and C. Draw an upward arc from B centered at C, and a downward arc from C centered at B. The two intersecting arcs enclose an almond or eye-shaped motif.
                </p>
                <p class='text-slate-300'>
                    • <span class='text-emerald-300 font-bold'>Composite Figures:</span> A round head circle joined to shoulder arcs by selecting exact tangent center positions.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Complex patterns in traditional Indian Rangoli and Islamic geometric art are built entirely from intersecting circular arcs centered on regular grids.
            </p>
        """,
        "summary": "Alternating semicircular arcs along a baseline create smooth waves. Intersecting dual arcs create symmetrical eye motifs.",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "To draw a continuous wave on an 8 cm baseline with 4 equal semicircles, what should be the diameter of each semicircle?",
                "options": ["1 cm", "2 cm", "4 cm", "8 cm"],
                "correct": 1,
                "explanation": "Dividing the 8 cm baseline into 4 equal segments gives 8 cm ÷ 4 = 2 cm per semicircle diameter (radius = 1 cm)."
            },
            {
                "id": "cp3_2",
                "question": "How is a symmetrical eye-shaped motif constructed using two points B and C?",
                "options": [
                    "By drawing two concentric full circles",
                    "By drawing intersecting arcs from center B and center C with radius equal to distance BC",
                    "By drawing a triangle and erasing the corners",
                    "By drawing two parallel straight lines"
                ],
                "correct": 1,
                "explanation": "Drawing dual intersecting arcs centered at B and C with radius BC creates an upper and lower boundary forming a symmetrical eye."
            }
        ]
    },

    # Slide 4: Rectangles & Squares
    {
        "id": 4,
        "badge": "Core Concept",
        "title": "Rectangles & Squares",
        "subtitle": "The Sacred Right-Angle Quadrilaterals",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Squares and rectangles are four-sided closed figures (<span class='text-amber-400 font-semibold'>quadrilaterals</span>) defined by strict side-length and interior-angle rules:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-cyan-500/30 text-cyan-200'>
                    <span class='font-bold text-cyan-300 font-mono'>Rectangle Properties:</span><br>
                    • <strong>R1:</strong> Opposite sides are equal in length (AB = CD and BC = DA).<br>
                    • <strong>R2:</strong> All four interior angles are right angles (∠A = ∠B = ∠C = ∠D = 90°).
                </div>
                <div class='p-2 rounded bg-slate-900 border border-amber-500/30 text-amber-200'>
                    <span class='font-bold text-amber-300 font-mono'>Square Properties:</span><br>
                    • <strong>S1:</strong> All four sides are equal in length (AB = BC = CD = DA).<br>
                    • <strong>S2:</strong> All four interior angles are right angles (90° each).
                </div>
                <p class='text-emerald-300 font-semibold text-[11px]'>
                    Mathematical Heirarchy: Every square is a special rectangle (since all sides equal implies opposite sides are equal), but not every rectangle is a square!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                A quadrilateral with four equal sides is a rhombus; only when its angles are also 90° does it become a square.
            </p>
        """,
        "summary": "A rectangle has opposite sides equal and 4 right angles (90°). A square has all 4 sides equal and 4 right angles. Every square is a rectangle.",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "Which statement correctly describes the relationship between squares and rectangles?",
                "options": [
                    "A square is never a rectangle",
                    "Every rectangle is a square",
                    "Every square is a rectangle, but not every rectangle is a square",
                    "Squares and rectangles share no common properties"
                ],
                "correct": 2,
                "explanation": "A square satisfies all rectangle conditions (opposite sides equal and all angles 90°), plus has all 4 sides equal."
            },
            {
                "id": "cp4_2",
                "question": "If a quadrilateral has all four sides equal to 6 cm, is it guaranteed to be a square?",
                "options": [
                    "Yes, equal sides always make a square",
                    "No, all four interior angles must also be verified to equal 90°",
                    "Yes, because 6 cm is a standard length",
                    "No, it must have diagonals of 6 cm"
                ],
                "correct": 1,
                "explanation": "A shape with four equal sides could be a tilted rhombus. It is only a square if its interior angles are exactly 90°."
            }
        ]
    },

    # Slide 5: Naming Vertices
    {
        "id": 5,
        "badge": "Core Concept",
        "title": "Naming Vertices",
        "subtitle": "The Universal Cyclical Perimeter Rule",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                In geometry, naming a polygon is not arbitrary. You cannot mix up vertex letters across diagonals:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>The Golden Rule of Vertex Naming:</p>
                <p class='text-slate-300'>
                    Letters must be listed in <span class='text-amber-300 font-bold'>consecutive cyclical order</span> as you walk around the perimeter (either clockwise or counterclockwise).
                </p>
                <div class='grid grid-cols-2 gap-2 text-center font-mono mt-2'>
                    <div class='p-2 rounded bg-emerald-950/60 border border-emerald-500/40 text-emerald-300'>
                        <span class='block font-bold text-sm'>VALID NAMES</span>
                        ABCD • BCDA<br>CDAB • DABC<br>ADCB • DCBA
                    </div>
                    <div class='p-2 rounded bg-rose-950/60 border border-rose-500/40 text-rose-300'>
                        <span class='block font-bold text-sm'>INVALID NAMES</span>
                        ABDC • ACBD<br>ACDB • BDCA<br>(Jumps across diagonal!)
                    </div>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                If you name a square 'ABDC', you are implying that edge B connects directly to edge D, crossing through the center of the shape!
            </p>
        """,
        "summary": "Vertices must be named consecutively along the outer perimeter (clockwise or counter-clockwise): ABCD is valid, ABDC is invalid.",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "For a rectangle with corners A, B, C, D in clockwise order, which of the following is an INVALID name?",
                "options": ["BCDA", "CDAB", "ABDC", "DABC"],
                "correct": 2,
                "explanation": "ABDC skips from B across the interior diagonal to D instead of walking consecutively along edge BC to C."
            },
            {
                "id": "cp5_2",
                "question": "If you walk counter-clockwise around rectangle ABCD starting at corner D, what is the correct polygon name?",
                "options": ["DCBA", "DABC", "DBCA", "DACB"],
                "correct": 0,
                "explanation": "Walking counter-clockwise from D takes you to C, then B, then A, giving the valid name DCBA."
            }
        ]
    },

    # Slide 6: Rotated Shapes
    {
        "id": 6,
        "badge": "Core Concept",
        "title": "Rotated Shapes",
        "subtitle": "Orientation Invariance on Dot Grids",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A common misconception is that a square tilted on its corner is no longer a square, but a "diamond". In mathematics, <span class='text-amber-400 font-semibold'>orientation does not change identity</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Properties are Invariant under Rotation:</p>
                <p class='text-slate-300'>
                    • Rotating a square by 45° tilts its sides relative to the page margins, but every side remains exactly equal in length (<span class='font-mono text-cyan-300'>s</span>).<br>
                    • Every corner remains an exact <span class='font-mono text-amber-300'>90° right angle</span>.<br>
                    • Therefore, a rotated square remains 100% a mathematical square!
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-emerald-300 text-xs'>
                    Dot Grid Test: Slanted sides with steps (e.g. 2 right, 1 up) must have perpendicular steps (1 right, 2 down) to form 90° corners!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                A "diamond" is an informal everyday word. In geometry, if its angles are 90°, it is a rotated square; if not 90°, it is a rhombus.
            </p>
        """,
        "summary": "Rotation preserves side lengths and interior angles. A square rotated at 45° on a dot grid remains a true geometric square.",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "A student rotates a cardboard square by 45°. What happens to its corner angles?",
                "options": [
                    "They change from 90° to 45°",
                    "They remain exactly 90°",
                    "Two angles become 60° and two become 120°",
                    "The shape becomes an equilateral triangle"
                ],
                "correct": 1,
                "explanation": "Rigid body rotation does not alter interior angles; all four corners remain exactly 90° right angles."
            },
            {
                "id": "cp6_2",
                "question": "On dot paper, a quadrilateral has sides of equal length. How can you verify whether it is a rotated square?",
                "options": [
                    "Check if the paper is held straight",
                    "Count the dots inside only",
                    "Verify with a protractor or corner of a paper that all 4 angles equal 90°",
                    "A tilted shape can never be a square"
                ],
                "correct": 2,
                "explanation": "To confirm it is a square, you must verify that adjacent sides meet at exactly 90° right angles."
            }
        ]
    },

    # Slide 7: Constructing Squares
    {
        "id": 7,
        "badge": "Core Concept",
        "title": "Constructing Squares",
        "subtitle": "Step-by-Step Compass & Protractor Protocol",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                To construct a square of side length <span class='font-mono text-amber-400 font-bold'>s = 6 cm</span> with absolute precision, follow this 4-step sequence:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs font-mono'>
                <div class='p-1.5 rounded bg-slate-900 border border-slate-700 text-cyan-300'>
                    <strong>Step 1 (Baseline):</strong> Draw straight horizontal segment AB = 6 cm using a ruler.
                </div>
                <div class='p-1.5 rounded bg-slate-900 border border-slate-700 text-amber-300'>
                    <strong>Step 2 (Perpendiculars):</strong> At vertex A and vertex B, construct rays perpendicular to AB (90° angles using a protractor or compass arcs).
                </div>
                <div class='p-1.5 rounded bg-slate-900 border border-slate-700 text-emerald-300'>
                    <strong>Step 3 (Compass Arcs):</strong> Set compass opening to exactly 6 cm. Place needle at A and cut an arc on the ray to locate point D. Place needle at B and cut an arc to locate point C.
                </div>
                <div class='p-1.5 rounded bg-slate-900 border border-slate-700 text-purple-300'>
                    <strong>Step 4 (Closing Edge):</strong> Join point D to point C with a straight ruler segment.
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Always draw a quick rough sketch first with dimensions labeled to guide your formal instrument construction!
            </p>
        """,
        "summary": "Construct a square by drawing baseline s, raising 90° perpendiculars at both endpoints, cutting arcs of length s, and joining the top.",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "What is the purpose of setting the compass to 6 cm when constructing a 6 cm square?",
                "options": [
                    "To draw a full circle around the square",
                    "To mark exactly 6 cm along the vertical perpendicular rays",
                    "To measure the diagonal length",
                    "To erase pencil errors"
                ],
                "correct": 1,
                "explanation": "The compass ensures the vertical edges AD and BC are cut to exactly 6 cm, matching baseline AB."
            },
            {
                "id": "cp7_2",
                "question": "Why is a rough diagram recommended before beginning an instrument construction?",
                "options": [
                    "It serves as the final graded submission",
                    "It helps plan the sequence of steps, labels, and dimensions before drawing accurately",
                    "It replaces the need for a ruler",
                    "It guarantees the paper will not tear"
                ],
                "correct": 1,
                "explanation": "A rough diagram clarifies which points need perpendiculars and compass arcs, preventing procedural errors."
            }
        ]
    },

    # Slide 8: Constructing Rectangles
    {
        "id": 8,
        "badge": "Core Concept",
        "title": "Constructing Rectangles",
        "subtitle": "Unequal Length & Breadth with Perpendicular Corners",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                To construct a rectangle of length <span class='font-mono text-cyan-300 font-bold'>l = 6 cm</span> and breadth <span class='font-mono text-amber-300 font-bold'>b = 4 cm</span>, the procedure mirrors the square, but uses two distinct compass settings:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='text-slate-300'>
                    1. <span class='text-cyan-300 font-bold'>Baseline:</span> Draw base segment AB = 6 cm.<br>
                    2. <span class='text-amber-300 font-bold'>Perpendicular Rays:</span> Use a protractor to erect 90° perpendicular lines upward from point A and point B.<br>
                    3. <span class='text-emerald-300 font-bold'>Breadth Arcs:</span> Set compass radius to 4 cm. Place needle at A to cut ray at D; place needle at B to cut ray at C (AD = BC = 4 cm).<br>
                    4. <span class='text-purple-300 font-bold'>Closing Segment:</span> Draw segment CD. Measure CD with ruler: it must measure exactly 6 cm!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Verification check: If CD does not equal 6 cm, or if ∠C and ∠D are not 90°, one of your perpendiculars was inaccurate.
            </p>
        """,
        "summary": "Constructing a rectangle l × b requires drawing base l, raising 90° rays, cutting arcs of length b, and connecting the top edge l.",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "When constructing a rectangle of 7 cm × 3 cm, what compass radius is used to cut the vertical side rays?",
                "options": ["7 cm", "3 cm", "10 cm", "4 cm"],
                "correct": 1,
                "explanation": "The breadth is 3 cm, so the compass is set to radius 3 cm to mark points along the perpendicular rays."
            },
            {
                "id": "cp8_2",
                "question": "If your completed rectangle ABCD has AB = 6 cm, AD = 4 cm, but CD measures 6.5 cm, what went wrong?",
                "options": [
                    "Nothing, opposite sides can vary slightly",
                    "The side rays were not constructed at exact 90° perpendicular angles",
                    "The compass radius was too large",
                    "The pencil was too sharp"
                ],
                "correct": 1,
                "explanation": "In a true rectangle, opposite sides must be strictly equal (CD = AB = 6 cm). An unequal CD indicates non-90° angles."
            }
        ]
    },

    # Slide 9: Point-to-Point Distance
    {
        "id": 9,
        "badge": "Core Concept",
        "title": "Point-to-Point Distance",
        "subtitle": "Dynamic Distance Variation Across Rectangle Edges",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Consider rectangle ABCD of dimensions <span class='font-mono text-cyan-300'>7 cm × 4 cm</span>. Let point <span class='font-mono text-amber-300 font-bold'>X</span> move along top edge AD, and point <span class='font-mono text-emerald-300 font-bold'>Y</span> move along bottom edge BC:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>What happens to the straight-line distance XY?</p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 space-y-1.5'>
                    <div class='text-emerald-300 font-mono'>
                        • <strong>Minimum Distance:</strong> When X and Y are directly opposite each other (perpendicular line segment XY ⊥ AD). Here, <span class='font-bold text-amber-300'>XY = 4 cm</span> (the breadth of the rectangle).
                    </div>
                    <div class='text-cyan-300 font-mono'>
                        • <strong>Maximum Distance:</strong> When X is at one corner (A) and Y is at the furthest opposite corner (C). Here, XY is the <span class='font-bold text-amber-300'>diagonal AC</span> (approx 8.06 cm).
                    </div>
                </div>
                <p class='text-slate-300 text-xs'>
                    As point Y glides away from the perpendicular alignment, the line segment XY slants, forming the hypotenuse of a right triangle, which is always longer than the perpendicular breadth!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Geometric Invariant: The perpendicular distance between two parallel lines is the shortest possible path connecting them.
            </p>
        """,
        "summary": "Between opposite sides of a rectangle, the minimum distance is the perpendicular breadth (4 cm); the maximum distance is the diagonal.",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "In a rectangle of 8 cm × 5 cm, what is the SHORTEST distance between a point on the top edge and a point on the bottom edge?",
                "options": ["8 cm", "5 cm", "13 cm", "3 cm"],
                "correct": 1,
                "explanation": "The shortest distance between parallel sides is the perpendicular segment, which equals the breadth (5 cm)."
            },
            {
                "id": "cp9_2",
                "question": "What geometric feature represents the MAXIMUM possible distance between any two points in a rectangle?",
                "options": ["The perimeter", "The diagonal connecting opposite vertices", "The longer length edge", "The perpendicular bisector"],
                "correct": 1,
                "explanation": "The diagonal connects opposite corners, forming the hypotenuse across the full length and breadth, which is the maximum span."
            }
        ]
    },

    # Slide 10: Rectangles from Squares
    {
        "id": 10,
        "badge": "Core Concept",
        "title": "Rectangles from Squares",
        "subtitle": "Partitioning and Length Transfer with a Compass",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A rectangle whose length is an exact integer multiple of its breadth can be partitioned into identical adjoining squares:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Examples of Modular Rectangles:</p>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>2-Square Rectangle:</span> Dimensions <span class='font-mono text-cyan-300'>8 cm × 4 cm</span> divides into two 4 cm × 4 cm squares.<br>
                    • <span class='text-amber-300 font-bold'>3-Square Rectangle:</span> Dimensions <span class='font-mono text-cyan-300'>12 cm × 4 cm</span> divides into three 4 cm × 4 cm squares.
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-slate-300 text-xs'>
                    <strong>Compass Transfer Technique:</strong> Instead of measuring with a ruler, open your compass to breadth AD (4 cm). Step the needle from A along AB to mark point E, and from E to mark point B. Then raise perpendicular EF to split the rectangle into perfect congruent squares!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Stepping a compass along a line transfers exact lengths without cumulative ruler-reading parallax errors.
            </p>
        """,
        "summary": "Rectangles with length = k × breadth divide into k equal squares. Compass stepping transfers breadth lengths accurately without ruler marks.",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "How many identical squares can be formed inside a rectangle of 15 cm × 5 cm?",
                "options": ["2", "3", "4", "5"],
                "correct": 1,
                "explanation": "Length 15 cm divided by breadth 5 cm = 3 squares of size 5 cm × 5 cm."
            },
            {
                "id": "cp10_2",
                "question": "If you want to construct a rectangle that divides into exactly two squares of side 6 cm, what must its dimensions be?",
                "options": ["6 cm × 6 cm", "12 cm × 6 cm", "12 cm × 12 cm", "18 cm × 6 cm"],
                "correct": 1,
                "explanation": "Two side-by-side squares of 6 cm produce a rectangle of length 6 + 6 = 12 cm and breadth 6 cm."
            }
        ]
    },

    # Slide 11: Nested Shapes & Holes
    {
        "id": 11,
        "badge": "Core Concept",
        "title": "Nested Shapes & Holes",
        "subtitle": "Stepped Squares, Centers & Cut-out Circular Holes",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Mastering basic constructions enables complex multi-layered architectural patterns and structural designs:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Three Classical Geometric Design Archetypes:</p>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Square Centered in a Rectangle:</span> In an 8 cm × 4 cm rectangle, find the center point by intersecting the two diagonals. Construct a 2 cm × 2 cm square concentric with the outer rectangle.
                </p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>Stepped / Falling Squares:</span> A sequence of squares of decreasing side lengths (e.g. 5 cm, 4 cm, 3 cm, 2 cm) sharing a common baseline or cascading diagonally corner-to-corner.
                </p>
                <p class='text-slate-300'>
                    • <span class='text-emerald-300 font-bold'>Circular Hole Design:</span> Locate the center of a square via diagonal intersection, then use a compass to draw a circular hole (e.g. radius 1.5 cm) inside the square.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                The intersection of diagonals is the most reliable way to pinpoint the exact geometric center of any rectangle or square.
            </p>
        """,
        "summary": "Complex designs include nested concentric squares, stepped sequences, and central circular holes located via diagonal intersections.",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "How can you locate the exact geometric center of a square to construct a circular hole?",
                "options": [
                    "Guess by looking with the eye",
                    "Draw both diagonals; their point of intersection is the exact center",
                    "Measure 1 cm from the left edge",
                    "Fold the paper in half once only"
                ],
                "correct": 1,
                "explanation": "The diagonals of a square intersect at its center of symmetry, providing the precise center for a compass needle."
            },
            {
                "id": "cp11_2",
                "question": "In a 6 cm × 6 cm square, what is the maximum radius a central circular hole can have without cutting outside the edges?",
                "options": ["6 cm", "3 cm", "1.5 cm", "4 cm"],
                "correct": 1,
                "explanation": "The distance from the center to any edge is half the side: 6 cm ÷ 2 = 3 cm. Any radius > 3 cm would spill outside the square."
            }
        ]
    },

    # Slide 12: Diagonals of Quadrilaterals
    {
        "id": 12,
        "badge": "Core Concept",
        "title": "Diagonals of Quadrilaterals",
        "subtitle": "Connecting Opposite Corners & Equality in Rectangles",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A <span class='text-amber-400 font-semibold'>diagonal</span> is a straight line segment connecting two opposite (non-adjacent) vertices of a polygon. A quadrilateral has exactly two diagonals:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Sacred Properties of Rectangular Diagonals:</p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 space-y-1 font-mono text-cyan-300'>
                    • In rectangle ABCD, diagonals are <strong>AC</strong> and <strong>BD</strong>.<br>
                    • <strong>Equality Theorem:</strong> The two diagonals are always exactly equal in length (<span class='text-amber-300 font-bold'>AC = BD</span>).<br>
                    • <strong>Mutual Bisection:</strong> The diagonals cut each other into two equal halves at their intersection point M (<span class='text-emerald-300 font-bold'>AM = MC = BM = MD</span>).
                </div>
                <p class='text-slate-300 text-xs'>
                    Carpenter's Square Test: Builders verify that a window frame or rectangular foundation is truly square (has 90° corners) by measuring both diagonals. If the diagonals are equal, the corners are 90°!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                In a general parallelogram, diagonals are unequal. Equality of diagonals is a defining hallmark of rectangles and squares.
            </p>
        """,
        "summary": "A rectangle's diagonals connect opposite vertices, are strictly equal in length (AC = BD), and bisect each other at their midpoint.",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "If diagonal AC of rectangle ABCD measures 8.5 cm, what is the length of diagonal BD?",
                "options": ["4.25 cm", "8.5 cm", "17 cm", "Cannot be determined without side lengths"],
                "correct": 1,
                "explanation": "In any rectangle, both diagonals are strictly equal in length. Therefore, BD = AC = 8.5 cm."
            },
            {
                "id": "cp12_2",
                "question": "How do carpenters use diagonals to check if a wooden door frame has true 90° right angles?",
                "options": [
                    "They check if the diagonals cross each other",
                    "They measure both diagonal lengths; if they are equal, the frame is rectangular",
                    "They weigh the frame on both sides",
                    "They measure the perimeter twice"
                ],
                "correct": 1,
                "explanation": "If opposite sides are parallel and both diagonals measure identical lengths, the frame is guaranteed to have 90° corners."
            }
        ]
    },

    # Slide 13: Diagonal Angle Splits
    {
        "id": 13,
        "badge": "Core Concept",
        "title": "Diagonal Angle Splits",
        "subtitle": "Rectangles (Unequal Angles) vs Squares (Exact 45° Bisectors)",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A diagonal passes through a 90° right-angle corner, splitting it into two complementary acute angles (<span class='font-mono text-cyan-300'>α + β = 90°</span>). How do rectangles and squares compare?
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-cyan-500/30 text-cyan-200'>
                    <span class='font-bold text-cyan-300 font-mono'>General Rectangle (Length ≠ Breadth):</span><br>
                    • The diagonal does <strong>NOT</strong> bisect the corner angle!<br>
                    • It splits 90° into two unequal angles (e.g. 60° and 30°, or 55° and 35°). The longer side faces the larger angle.
                </div>
                <div class='p-2 rounded bg-slate-900 border border-amber-500/30 text-amber-200'>
                    <span class='font-bold text-amber-300 font-mono'>Square (All Sides Equal):</span><br>
                    • The diagonal is an exact <strong>angle bisector</strong>!<br>
                    • Because both adjacent sides are equal, the diagonal splits 90° into two perfectly equal angles: <span class='font-bold text-amber-300'>45° and 45°</span>.
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                A diagonal also splits a square into two congruent isosceles right triangles (45°-45°-90°).
            </p>
        """,
        "summary": "In a rectangle, diagonals split 90° into unequal angles (e.g. 60°/30°). In a square, diagonals bisect 90° into equal 45° angles.",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "A diagonal of a square splits one of its corner angles. What is the measure of each resulting angle?",
                "options": ["30° and 60°", "45° and 45°", "50° and 40°", "90° and 0°"],
                "correct": 1,
                "explanation": "Because a square has equal sides, its diagonal bisects the 90° angle into two equal 45° angles."
            },
            {
                "id": "cp13_2",
                "question": "In a rectangle, a diagonal splits a 90° corner into two angles, one of which measures 32°. What is the other angle?",
                "options": ["32°", "58°", "48°", "68°"],
                "correct": 1,
                "explanation": "The two angles are complementary and sum to 90°: 90° − 32° = 58°."
            }
        ]
    },

    # Slide 14: Constructing from Diagonals
    {
        "id": 14,
        "badge": "Core Concept",
        "title": "Constructing from Diagonals",
        "subtitle": "Given One Side and Diagonal: Compass Arc Intersection",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Suppose you are given one side <span class='font-mono text-cyan-300 font-bold'>AB = 5 cm</span> and diagonal <span class='font-mono text-amber-300 font-bold'>AC = 7 cm</span>. How do you construct the rectangle without knowing the breadth BC?
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs font-mono'>
                <p class='text-slate-300'>
                    1. <span class='text-cyan-300 font-bold'>Baseline:</span> Draw segment AB = 5 cm using a ruler.<br>
                    2. <span class='text-amber-300 font-bold'>Perpendicular Ray:</span> At vertex B, erect a perpendicular ray BX (90° to AB). Vertex C must lie somewhere on this ray.<br>
                    3. <span class='text-emerald-300 font-bold'>Diagonal Arc Intersection:</span> Set your compass opening to exactly 7 cm. Place the compass needle at vertex A. Swing an arc cutting ray BX. The intersection point is vertex <span class='text-amber-300 font-bold'>C</span>!<br>
                    4. <span class='text-purple-300 font-bold'>Complete Rectangle:</span> Now measure breadth BC with compass. Cut arc from A, cut 5 cm arc from C, locating D.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                This construction uses the right-triangle property (hypotenuse AC = 7 cm, base AB = 5 cm) to locate vertex C automatically!
            </p>
        """,
        "summary": "Given side AB and diagonal AC, erect a 90° ray at B, and strike an arc of radius AC from A. The intersection point defines vertex C.",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "To construct rectangle ABCD given AB = 5 cm and diagonal AC = 7 cm, where is the compass needle placed to strike the 7 cm arc?",
                "options": ["At vertex B", "At vertex A", "At the midpoint of AB", "Anywhere on the ray"],
                "correct": 1,
                "explanation": "Since AC is the diagonal connecting A to C, the compass needle is placed at A with radius 7 cm to locate C on the perpendicular ray from B."
            },
            {
                "id": "cp14_2",
                "question": "Can a rectangle have side AB = 6 cm and diagonal AC = 5 cm?",
                "options": [
                    "Yes, any dimensions are valid",
                    "No, because the diagonal (hypotenuse) must always be longer than any side",
                    "Only if the breadth is 1 cm",
                    "Yes, by rotating the rectangle"
                ],
                "correct": 1,
                "explanation": "The diagonal forms the hypotenuse of a right triangle with the sides. The hypotenuse is strictly longer than each leg (AC must be > AB)."
            }
        ]
    },

    # Slide 15: Equidistant Points
    {
        "id": 15,
        "badge": "Core Concept",
        "title": "Equidistant Points",
        "subtitle": "Finding Points at Equal Distance via Dual Compass Arcs",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Suppose you have two fixed points <span class='font-mono text-cyan-300'>B</span> and <span class='font-mono text-amber-300'>C</span> (distance 6 cm apart). You need to find a point <span class='font-mono text-emerald-300 font-bold'>A</span> that is at an equal distance of <span class='font-mono text-emerald-300'>5 cm</span> from both B and C:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>The Dual Arc Intersection Method:</p>
                <p class='text-slate-300'>
                    1. Set compass radius to 5 cm.<br>
                    2. Place needle at point B; draw an arc above the segment.<br>
                    3. Without changing the compass radius (keep at 5 cm), place needle at point C; draw an intersecting arc.<br>
                    4. The point where the two arcs cross is point <span class='font-mono text-emerald-300 font-bold'>A</span>!
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 text-center font-mono text-cyan-300 text-xs'>
                    AB = 5 cm and AC = 5 cm → Triangle ABC is an Isosceles Triangle!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                If you also draw intersecting arcs below the segment, you locate a second equidistant point A'. Line AA' is the perpendicular bisector of BC!
            </p>
        """,
        "summary": "Dual intersecting compass arcs of equal radius centered at B and C locate an equidistant point A (AB = AC) without trial and error.",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "If B and C are 6 cm apart, what is the MINIMUM compass radius needed for arcs from B and C to touch each other?",
                "options": ["2 cm", "3 cm", "6 cm", "1 cm"],
                "correct": 1,
                "explanation": "The distance between centers is 6 cm. For two arcs to meet, each radius must be at least half the distance: 6 cm ÷ 2 = 3 cm."
            },
            {
                "id": "cp15_2",
                "question": "What type of triangle is formed when you connect point A to points B and C if AB = AC = 5 cm and BC = 6 cm?",
                "options": ["Equilateral triangle", "Isosceles triangle", "Scalene triangle", "Right triangle"],
                "correct": 1,
                "explanation": "A triangle with two equal sides (AB = AC = 5 cm) and one different base (BC = 6 cm) is an isosceles triangle."
            }
        ]
    },

    # Slide 16: The Composite House
    {
        "id": 16,
        "badge": "Core Concept",
        "title": "The Composite House",
        "subtitle": "Combining Squares, Rectangles, Arcs & Triangular Roofs",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Real-world architectural blueprints integrate all basic geometric constructions into a single unified composite structure (the "Dream House"):
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Blueprint Construction Steps:</p>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Base Walls (Square):</span> Construct square ABCD of side 6 cm using baseline and 90° perpendiculars.<br>
                    • <span class='text-cyan-300 font-bold'>Door (Rectangle):</span> Construct a centered rectangular opening (2 cm × 3 cm) along bottom edge AB.<br>
                    • <span class='text-emerald-300 font-bold'>Eave (Circular Arc):</span> Use a compass to swing a graceful curved eave over the entrance.<br>
                    • <span class='text-purple-300 font-bold'>Roof Peak (Equidistant Point):</span> From top corners D and C, draw dual intersecting compass arcs of radius 5 cm to locate apex point R. Connect RD and RC to form the triangular pitched roof!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Every complex structure—from ancient Indian temples to modern skyscrapers—is a composite synthesis of straight perpendiculars, circles, and equidistant triangles.
            </p>
        """,
        "summary": "A composite house blueprint combines a square foundation, rectangular door, curved eaves, and an equidistant triangular roof.",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "Which construction technique is used to locate the symmetrical apex peak R of the triangular roof above wall corners D and C?",
                "options": [
                    "Freehand guesswork",
                    "Dual intersecting compass arcs of equal radius centered at D and C",
                    "Drawing a circle around the whole house",
                    "Measuring with a protractor only"
                ],
                "correct": 1,
                "explanation": "Drawing equal-radius arcs from corners D and C finds the equidistant apex point R, ensuring the roof peak is centered."
            },
            {
                "id": "cp16_2",
                "question": "What geometric shapes make up the walls, door, and roof of the composite house structure?",
                "options": [
                    "Circle, oval, and pentagon",
                    "Square (walls), rectangle (door), and triangle (roof)",
                    "Hexagon, rhombus, and trapezoid",
                    "Triangles only"
                ],
                "correct": 1,
                "explanation": "The composite house integrates a square body, a rectangular door, and an equidistant triangular roof."
            }
        ]
    },

    # Quiz Slide 1: Questions 1 to 10
    {
        "id": 17,
        "badge": "Mastery Challenge",
        "title": "Quiz 1",
        "subtitle": "Compass Basics, Circles, Waves & Motifs",
        "is_quiz": True,
        "quiz_range": (1, 10)
    },

    # Quiz Slide 2: Questions 11 to 20
    {
        "id": 18,
        "badge": "Mastery Challenge",
        "title": "Quiz 2",
        "subtitle": "Square & Rectangle Properties, Vertex Naming & Rotations",
        "is_quiz": True,
        "quiz_range": (11, 20)
    },

    # Quiz Slide 3: Questions 21 to 30
    {
        "id": 19,
        "badge": "Mastery Challenge",
        "title": "Quiz 3",
        "subtitle": "Step-by-Step Construction, Point Distances & Nested Shapes",
        "is_quiz": True,
        "quiz_range": (21, 30)
    },

    # Quiz Slide 4: Questions 31 to 40
    {
        "id": 20,
        "badge": "Mastery Challenge",
        "title": "Quiz 4",
        "subtitle": "Diagonals, Angle Splits, Equidistant Arcs & Blueprints",
        "is_quiz": True,
        "quiz_range": (31, 40)
    }
]

QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "What is the primary function of a compass in geometric constructions?",
        "options": [
            "To measure angles in degrees",
            "To draw circles, arcs, and transfer exact segment lengths",
            "To erase stray pencil lines",
            "To measure lengths in millimeters"
        ],
        "correct": 1,
        "solution": "A compass holds a fixed radius span to draw perfect circles and arcs, and transfers distances without reading numeric markings."
    },
    # Q2
    {
        "id": 2,
        "question": "If a circle has a radius of 4.5 cm, what is the length of its diameter?",
        "options": ["4.5 cm", "9.0 cm", "2.25 cm", "18.0 cm"],
        "correct": 1,
        "solution": "The diameter of a circle is twice its radius: d = 2 × r = 2 × 4.5 cm = 9.0 cm."
    },
    # Q3
    {
        "id": 3,
        "question": "A point Q is at distance 6 cm from the center of a circle of radius 6 cm. Where does point Q lie?",
        "options": ["Inside the circle", "Outside the circle", "Exactly on the circle boundary", "At the center"],
        "correct": 2,
        "solution": "The circle boundary consists of all points whose distance from the center equals the radius. Since distance = 6 cm = r, Q lies exactly on the circle."
    },
    # Q4
    {
        "id": 4,
        "question": "In constructing an alternating wavy wave along an 8 cm line AB with 4 equal semicircles, how many semicircle centers are placed on AB?",
        "options": ["2", "4", "8", "1"],
        "correct": 1,
        "solution": "Each semicircle requires its own center point along the baseline. 4 semicircles require 4 center points spaced 2 cm apart."
    },
    # Q5
    {
        "id": 5,
        "question": "An almond/eye-shaped motif is drawn using two points B and C. If the distance BC is 4 cm, what radius is used for the intersecting arcs?",
        "options": ["2 cm", "4 cm", "8 cm", "1 cm"],
        "correct": 1,
        "solution": "The classical eye motif uses the distance between the two points (4 cm) as the radius for each arc centered at B and C."
    },
    # Q6
    {
        "id": 6,
        "question": "Which of the following is defined as a continuous line drawn on paper without lifting the pencil?",
        "options": ["Curve", "Segment only", "Angle", "Polygon only"],
        "correct": 0,
        "solution": "In geometry, a curve is any continuous path traced on a plane without lifting the drawing instrument (including straight lines and circles)."
    },
    # Q7
    {
        "id": 7,
        "question": "How many endpoints does a full circle have?",
        "options": ["1", "2", "Infinite", "0 (it is a closed curve)"],
        "correct": 3,
        "solution": "A circle is a closed continuous curve that loops back onto itself, having zero endpoints."
    },
    # Q8
    {
        "id": 8,
        "question": "If you double the radius of a circle, what happens to its diameter?",
        "options": ["It remains the same", "It doubles", "It quadruples", "It halves"],
        "correct": 1,
        "solution": "Diameter is directly proportional to radius (d = 2r). If r doubles, d also doubles: 2(2r) = 2d."
    },
    # Q9
    {
        "id": 9,
        "question": "What instrument is specifically used to erect exact 90° perpendicular lines when constructing rectangles?",
        "options": ["Compass or Protractor", "Ruler only", "Divider only", "Tracing paper"],
        "correct": 0,
        "solution": "A protractor directly measures 90°, and a compass can construct 90° perpendicular bisectors."
    },
    # Q10
    {
        "id": 10,
        "question": "A student attempts to draw a circle of radius 3 cm, but the compass joint is loose and widens to 4 cm during the stroke. What shape results?",
        "options": ["A larger circle", "An imperfect non-circular spiral or oval curve", "A straight line", "A square"],
        "correct": 1,
        "solution": "A circle requires a strictly constant distance from the center. If the compass widens, the radius varies and the resulting path is a spiral or distorted curve."
    },

    # Q11
    {
        "id": 11,
        "question": "What are the two defining properties of a rectangle?",
        "options": [
            "All four sides equal and all angles 90°",
            "Opposite sides equal and all four interior angles equal 90°",
            "Opposite sides parallel and angles equal 60°",
            "Adjacent sides equal and one angle 90°"
        ],
        "correct": 1,
        "solution": "A rectangle is defined by: (1) opposite sides equal in length, and (2) all four interior angles equal 90°."
    },
    # Q12
    {
        "id": 12,
        "question": "Which of the following is true for EVERY square?",
        "options": [
            "It is also a rectangle",
            "It has diagonals of different lengths",
            "Its interior angles sum to 180°",
            "It has only two right angles"
        ],
        "correct": 0,
        "solution": "Every square satisfies all properties of a rectangle (opposite sides equal and all four angles 90°). Thus, every square is a rectangle."
    },
    # Q13
    {
        "id": 13,
        "question": "For a quadrilateral with vertices P, Q, R, S in clockwise order, which of the following names is INVALID?",
        "options": ["PQRS", "QRSP", "PRQS", "SPQR"],
        "correct": 2,
        "solution": "PRQS is invalid because it skips from P across the diagonal to R instead of following consecutive perimeter order."
    },
    # Q14
    {
        "id": 14,
        "question": "When a square drawn on paper is rotated clockwise by 30°, what happens to its geometric classification?",
        "options": [
            "It becomes a trapezoid",
            "It becomes a non-square rhombus",
            "It remains a square",
            "It becomes a scalene quadrilateral"
        ],
        "correct": 2,
        "solution": "Rotation is a rigid motion that preserves all side lengths and interior right angles. A rotated square remains a square."
    },
    # Q15
    {
        "id": 15,
        "question": "What is the sum of all four interior angles of any rectangle or square?",
        "options": ["180°", "270°", "360°", "400°"],
        "correct": 2,
        "solution": "Each interior angle is 90°. For four corners: 4 × 90° = 360°."
    },
    # Q16
    {
        "id": 16,
        "question": "Can a rectangle have sides of lengths 5 cm, 3 cm, 5 cm, and 4 cm in perimeter order?",
        "options": [
            "Yes, if the angles are 90°",
            "No, because opposite sides must be equal in length (3 cm ≠ 4 cm)",
            "Yes, if constructed with a compass",
            "Only on dot paper"
        ],
        "correct": 1,
        "solution": "In a rectangle, opposite sides must be strictly equal. Here, opposite sides are 3 cm and 4 cm, which violates rectangle property R1."
    },
    # Q17
    {
        "id": 17,
        "question": "On a square dot grid, four vertices form a tilted square. If each side steps 3 dots horizontally and 1 dot vertically, what must the perpendicular side step?",
        "options": [
            "3 dots horizontally and 1 dot vertically in the same direction",
            "1 dot horizontally and 3 dots vertically (perpendicular step)",
            "2 dots horizontally and 2 dots vertically",
            "4 dots horizontally only"
        ],
        "correct": 1,
        "solution": "To form a 90° angle on a grid, a slope of 1/3 must meet a perpendicular slope of −3/1 (step 1 dot horizontally, 3 dots vertically)."
    },
    # Q18
    {
        "id": 18,
        "question": "If you start at corner C of rectangle ABCD and walk clockwise around its perimeter, what is its valid polygon name?",
        "options": ["CDAB", "CDBA", "CADB", "CBDA"],
        "correct": 0,
        "solution": "Walking clockwise from C proceeds to D, then A, then B, giving the valid cyclical name CDAB."
    },
    # Q19
    {
        "id": 19,
        "question": "How many pairs of parallel sides does a rectangle have?",
        "options": ["1 pair", "2 pairs", "4 pairs", "0 pairs"],
        "correct": 1,
        "solution": "A rectangle has two pairs of opposite parallel sides (top parallel to bottom, left parallel to right)."
    },
    # Q20
    {
        "id": 20,
        "question": "A shape has 4 equal sides of 5 cm, but its corner angles measure 70° and 110°. What is this shape?",
        "options": ["A square", "A rectangle", "A rhombus (not a square)", "A trapezoid"],
        "correct": 2,
        "solution": "A quadrilateral with 4 equal sides but non-90° angles is a rhombus, not a square."
    },

    # Q21
    {
        "id": 21,
        "question": "What is the first step in constructing a square of side 5 cm?",
        "options": [
            "Draw a circle of radius 5 cm",
            "Draw a horizontal baseline segment AB = 5 cm using a ruler",
            "Draw two diagonal lines",
            "Erase the corners"
        ],
        "correct": 1,
        "solution": "The construction begins by establishing the baseline segment AB = 5 cm."
    },
    # Q22
    {
        "id": 22,
        "question": "In constructing rectangle ABCD with AB = 7 cm and AD = 4 cm, what angle must be erected at vertex A?",
        "options": ["45°", "60°", "90°", "120°"],
        "correct": 2,
        "solution": "Every corner of a rectangle must be an exact 90° right angle."
    },
    # Q23
    {
        "id": 23,
        "question": "In rectangle ABCD of size 8 cm × 6 cm, what is the SHORTEST distance between a point on AD and a point on BC?",
        "options": ["8 cm", "6 cm", "10 cm", "2 cm"],
        "correct": 1,
        "solution": "The shortest distance between parallel edges AD and BC is the perpendicular segment connecting them, which equals breadth AB = 6 cm."
    },
    # Q24
    {
        "id": 24,
        "question": "In the same rectangle of 8 cm × 6 cm, what is the LONGEST distance between any two points in the rectangle?",
        "options": ["8 cm", "6 cm", "The diagonal AC = 10 cm", "The perimeter = 28 cm"],
        "correct": 2,
        "solution": "The maximum distance between any two points in a rectangle is the diagonal connecting opposite corners (√(8² + 6²) = √(64 + 36) = √100 = 10 cm)."
    },
    # Q25
    {
        "id": 25,
        "question": "A rectangle measures 12 cm in length and 4 cm in breadth. How many 4 cm × 4 cm squares can it be divided into?",
        "options": ["2", "3", "4", "6"],
        "correct": 1,
        "solution": "12 cm ÷ 4 cm = 3 squares."
    },
    # Q26
    {
        "id": 26,
        "question": "How can you divide a rectangle into identical squares without using ruler millimeter markings?",
        "options": [
            "By guessing the midpoint",
            "By setting a compass to the breadth and stepping it repeatedly along the length",
            "By folding the paper randomly",
            "By drawing diagonal circles"
        ],
        "correct": 1,
        "solution": "Using a compass to capture the breadth and stepping it along the length transfers equal side lengths with pure geometric accuracy."
    },
    # Q27
    {
        "id": 27,
        "question": "To construct a centered circular hole inside an 8 cm × 8 cm square, what is the center point of the circle?",
        "options": [
            "Any of the 4 corners",
            "The intersection of the two diagonals of the square",
            "The midpoint of the bottom edge",
            "Point (0, 0)"
        ],
        "correct": 1,
        "solution": "The intersection point of the two diagonals is the exact geometric center of the square."
    },
    # Q28
    {
        "id": 28,
        "question": "What is the maximum diameter of a circular hole that fits entirely inside a 10 cm × 10 cm square without cutting edges?",
        "options": ["5 cm", "10 cm", "15 cm", "20 cm"],
        "correct": 1,
        "solution": "The maximum circle touches all four edges, having a diameter equal to the side of the square: 10 cm (radius = 5 cm)."
    },
    # Q29
    {
        "id": 29,
        "question": "A sequence of stepped squares has side lengths 5 cm, 4 cm, and 3 cm resting on a common baseline. What is the total length of the baseline covered?",
        "options": ["5 cm", "9 cm", "12 cm", "15 cm"],
        "correct": 2,
        "solution": "The total baseline covered is the sum of the side lengths: 5 cm + 4 cm + 3 cm = 12 cm."
    },
    # Q30
    {
        "id": 30,
        "question": "When constructing a square inside an 8 cm × 4 cm rectangle, if the square has side 4 cm, how much area of the rectangle remains?",
        "options": ["0 cm²", "16 cm²", "32 cm²", "8 cm²"],
        "correct": 1,
        "solution": "Area of rectangle = 8 × 4 = 32 cm². Area of square = 4 × 4 = 16 cm². Remaining area = 32 − 16 = 16 cm²."
    },

    # Q31
    {
        "id": 31,
        "question": "Which of the following is true about the diagonals of a rectangle?",
        "options": [
            "They are perpendicular to each other",
            "They are strictly equal in length",
            "One is always twice as long as the other",
            "They never intersect"
        ],
        "correct": 1,
        "solution": "A fundamental property of every rectangle is that its two diagonals are strictly equal in length (AC = BD)."
    },
    # Q32
    {
        "id": 32,
        "question": "In a square, what angle does a diagonal make with an adjacent side?",
        "options": ["30°", "45°", "60°", "90°"],
        "correct": 1,
        "solution": "The diagonal of a square bisects the 90° corner angle into two equal 45° angles."
    },
    # Q33
    {
        "id": 33,
        "question": "In a non-square rectangle, does the diagonal bisect the corner right angle?",
        "options": [
            "Yes, always into 45° each",
            "No, it splits the 90° angle into two unequal angles (e.g. 60° and 30°)",
            "Only if the length is an odd number",
            "Only on dot paper"
        ],
        "correct": 1,
        "solution": "In a general rectangle where length ≠ breadth, the diagonal divides the 90° angle into two unequal complementary angles."
    },
    # Q34
    {
        "id": 34,
        "question": "To construct a rectangle with side AB = 4 cm and diagonal AC = 6 cm, you erect a 90° ray at B and strike an arc of what radius from A?",
        "options": ["4 cm", "6 cm", "10 cm", "2 cm"],
        "correct": 1,
        "solution": "The diagonal connects A to C. Striking an arc of radius AC = 6 cm with the needle at A locates vertex C on the perpendicular ray from B."
    },
    # Q35
    {
        "id": 35,
        "question": "If points B and C are 8 cm apart, what happens if you try to find an equidistant point A by drawing arcs of radius 3 cm from B and C?",
        "options": [
            "The arcs will intersect at two points",
            "The arcs will not meet at all because 3 cm + 3 cm = 6 cm < 8 cm",
            "The arcs will form a square",
            "Point A will be at the center"
        ],
        "correct": 1,
        "solution": "The sum of the two radii (3 + 3 = 6 cm) is less than the distance between centers (8 cm), so the arcs cannot touch or intersect."
    },
    # Q36
    {
        "id": 36,
        "question": "Where does every point equidistant from two fixed points B and C lie?",
        "options": [
            "On a circle around B",
            "On the perpendicular bisector line of segment BC",
            "On segment BC itself only",
            "At infinity only"
        ],
        "correct": 1,
        "solution": "The locus of all points equidistant from two points B and C is the perpendicular bisector of segment BC."
    },
    # Q37
    {
        "id": 37,
        "question": "In the composite house construction, what shape forms the main body/walls?",
        "options": ["A triangle", "A circle", "A square", "A hexagon"],
        "correct": 2,
        "solution": "The main walls of the composite house structure are formed by a square."
    },
    # Q38
    {
        "id": 38,
        "question": "How is the roof apex R located symmetrically above the top corners D and C of the house?",
        "options": [
            "By extending edge CD by 5 cm",
            "By drawing dual intersecting arcs of equal radius from D and C",
            "By drawing a random dot above the house",
            "By measuring 90° from corner D"
        ],
        "correct": 1,
        "solution": "Intersecting arcs of equal radius from corners D and C locate an equidistant point R, ensuring the triangular roof is perfectly centered."
    },
    # Q39
    {
        "id": 39,
        "question": "In rectangle ABCD, diagonals AC and BD intersect at point M. If AC = 12 cm, what is the length of AM?",
        "options": ["12 cm", "6 cm", "3 cm", "24 cm"],
        "correct": 1,
        "solution": "The diagonals of a rectangle bisect each other, so AM = AC ÷ 2 = 12 cm ÷ 2 = 6 cm."
    },
    # Q40
    {
        "id": 40,
        "question": "Why can a triangle NOT have interior angles of 90°, 90°, and 45°?",
        "options": [
            "It would have too many sides",
            "The interior angles of any planar triangle must strictly sum to 180° (90° + 90° + 45° = 225° > 180°)",
            "Angles must all be equal",
            "A triangle cannot contain a 90° angle"
        ],
        "correct": 1,
        "solution": "The sum of interior angles in a triangle is always 180°. Two 90° angles already equal 180°, so a third angle is impossible in plane geometry."
    }
]

def verify_data():
    import json
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    data_str = json.dumps(SLIDES) + json.dumps(QUIZ_QUESTIONS) + json.dumps(CHAPTER_META)
    for word in forbidden:
        if word in data_str:
            raise ValueError(f"Found forbidden LaTeX token: {word}")
    for ch in data_str:
        if 0xD800 <= ord(ch) <= 0xDFFF:
            raise ValueError(f"Found surrogate character: {ch}")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in Constructions data!")

if __name__ == "__main__":
    verify_data()
    with open(".agents/class6_math_constructions_data.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch8_constructions_data.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_constructions_data.py")


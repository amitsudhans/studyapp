# -*- coding: utf-8 -*-
"""
Data generator for NCERT Class 6 Mathematics Chapter 9: Symmetry
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, \circ, etc.).
All math rendered in clean Unicode (°, •, ², ³, ⁿ, ₁, ₂, ×, ÷, +, −, =, ≠, ≤, ≥, √, π, →, 1/2, 3/4).
"""

CHAPTER_META = {
    "title": "NCERT Class 6 Mathematics • Chapter 9 • Symmetry",
    "mentors": "Acharya Hemachandra & Johannes Kepler (Pioneers of Visual Harmonies & Snowflake Rotational Symmetry)",
    "description": "Comprehensive 20-slide interactive master lab covering patterns in nature and architecture, mirror lines of symmetry, paper folding and cutting, why rectangle diagonals are not lines of symmetry, ink blot patterns, the hole punching game, rotational symmetry and center of rotation, angle of symmetry, radial arms (360°/n), order of rotational symmetry, infinite symmetries of a circle, tile symmetry grids, the 6×6 symmetry game, and the 4-way symmetry classification matrix."
}

SLIDES = [
    # Slide 1: Nature's Balance
    {
        "id": 1,
        "badge": "Core Concept",
        "title": "Nature's Balance",
        "subtitle": "Discovering Symmetrical Harmonies in Nature & Architecture",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When you look at a butterfly with outstretched wings, a starfish on the ocean floor, or a blooming lotus flower, you notice a pleasing sense of harmony and balance. This balance is called <span class='text-amber-400 font-semibold'>symmetry</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Symmetrical Objects:</span> Have parts that repeat in a definite, balanced pattern. If divided, one part matches another (e.g., butterfly wings, honeycomb cells, leaf veins, the Taj Mahal, and temple gopurams).<br>
                    • <span class='text-rose-300 font-bold'>Asymmetrical Objects:</span> Lack any regular repetition or balanced balance (e.g., drifting rain clouds, jagged rocks, or an irregular puddle of water).
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-cyan-300 text-xs'>
                    Symmetry = Balance, Proportion & Congruence between Parts
                </div>
            </div>
            <p class='text-xs text-slate-400 leading-relaxed'>
                Ancient Indian temple architects (*Sthapatis*) used geometric symmetry principles from the *Vastu Shastra* to design monuments that express cosmic order.
            </p>
        """,
        "summary": "Symmetry means a balanced repetition of parts. Living organisms and great architecture exhibit symmetry, while irregular clouds and rocks are asymmetrical.",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "Which of the following real-world objects exhibits geometric symmetry?",
                "options": ["A butterfly with open wings", "A random rain cloud", "A jagged broken rock", "A footprint in mud"],
                "correct": 0,
                "explanation": "A butterfly displays bilateral symmetry: its left wing is an exact mirror match of its right wing."
            },
            {
                "id": "cp1_2",
                "question": "Why is an irregular cloud considered asymmetrical?",
                "options": [
                    "It has too many colors",
                    "It lacks any regular repeating structure or matching halves",
                    "It is too high in the sky",
                    "It contains water droplets"
                ],
                "correct": 1,
                "explanation": "Asymmetry means lacking any line or center of balance where parts coincide or repeat."
            }
        ]
    },

    # Slide 2: Line of Symmetry
    {
        "id": 2,
        "badge": "Core Concept",
        "title": "Line of Symmetry",
        "subtitle": "Folding Along an Axis of Reflection",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Take a sheet of paper with a drawing of a heart or an equilateral leaf. When folded along a straight crease, if the two halves completely cover each other without overlapping edges, that crease is a <span class='text-amber-400 font-semibold'>line of symmetry</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Formal Definition:</p>
                <p class='text-slate-300'>
                    A line of symmetry (or <span class='text-cyan-300 font-semibold'>axis of symmetry</span>) divides a figure into two identical halves that coincide exactly when folded along the line.
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 text-xs'>
                    Half A on one side of the line is the exact mirror image of Half B on the other side.
                </div>
                <p class='text-slate-300 text-[11px]'>
                    A shape may have 1 line of symmetry (like the letter M), 2 lines (like the letter H), multiple lines (like an equilateral triangle), or zero lines (like the letter F or a scalene triangle).
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                A figure with at least one line of symmetry is said to have bilateral (or reflectional) symmetry.
            </p>
        """,
        "summary": "A line of symmetry divides a figure into two congruent halves that match exactly upon folding. Each half is the mirror reflection of the other.",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "How many lines of symmetry does the capital English letter 'M' possess?",
                "options": ["1 (vertical)", "2 (horizontal and vertical)", "0", "Infinite"],
                "correct": 0,
                "explanation": "The letter 'M' has exactly 1 vertical line of symmetry passing straight down through its middle peak."
            },
            {
                "id": "cp2_2",
                "question": "What happens when you fold a symmetrical shape along its line of symmetry?",
                "options": [
                    "One half covers the other half exactly with no overhang",
                    "The shape tears in half",
                    "The perimeter doubles",
                    "The corners turn into circles"
                ],
                "correct": 0,
                "explanation": "By definition, the two halves coincide and overlap perfectly without any overhang."
            }
        ]
    },

    # Slide 3: Squares vs Rectangles
    {
        "id": 3,
        "badge": "Core Concept",
        "title": "Squares vs Rectangles",
        "subtitle": "Why Rectangle Diagonals Are NOT Lines of Symmetry",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                One of the most famous traps in school geometry concerns the diagonals of a rectangle. Let us compare a square and a general rectangle:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-amber-500/30 text-amber-200'>
                    <span class='font-bold text-amber-300 font-mono'>Square (4 Lines of Symmetry):</span><br>
                    • 1 Vertical line (folding left to right).<br>
                    • 1 Horizontal line (folding top to bottom).<br>
                    • 2 Diagonal lines (folding corner to opposite corner). Because adjacent sides are equal, folding along either diagonal makes the edges coincide perfectly!
                </div>
                <div class='p-2 rounded bg-slate-900 border border-cyan-500/30 text-cyan-200'>
                    <span class='font-bold text-cyan-300 font-mono'>Rectangle (Only 2 Lines of Symmetry):</span><br>
                    • 1 Vertical line and 1 Horizontal line.<br>
                    • <strong class='text-rose-400'>The Diagonal is NOT a Line of Symmetry!</strong> Even though a diagonal splits the rectangle into two triangles of equal area, folding along the diagonal causes the corners to stick out in opposite directions!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Equal area does not guarantee symmetry. A fold must make boundaries coincide, which only happens along diagonals if all sides are equal (a square or rhombus).
            </p>
        """,
        "summary": "A square has 4 lines of symmetry (horizontal, vertical, 2 diagonals). A general rectangle has only 2 (horizontal and vertical; its diagonals are NOT lines of symmetry).",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "How many lines of symmetry does a general non-square rectangle possess?",
                "options": ["2", "4", "1", "0"],
                "correct": 0,
                "explanation": "A rectangle has only 2 lines of symmetry: horizontal and vertical lines connecting opposite midpoints."
            },
            {
                "id": "cp3_2",
                "question": "Why is the diagonal of a rectangle NOT a line of symmetry, even though it divides the rectangle into two congruent triangles?",
                "options": [
                    "The triangles have different areas",
                    "When folded along the diagonal, the opposite corners stick out and do not overlap",
                    "The diagonal is curved",
                    "Diagonals can never be lines of symmetry in any shape"
                ],
                "correct": 1,
                "explanation": "Symmetry requires exact physical overlap upon folding. A diagonal fold on a rectangle leaves corners projecting outward."
            }
        ]
    },

    # Slide 4: Polygons & Snowflakes
    {
        "id": 4,
        "badge": "Core Concept",
        "title": "Polygons & Snowflakes",
        "subtitle": "Regular Polygons with n Sides Have Exactly n Lines of Symmetry",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A <span class='text-amber-400 font-semibold'>regular polygon</span> has all sides equal and all interior angles equal. There is a magnificent mathematical law governing regular polygons:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-mono font-bold text-amber-300 text-center text-sm'>
                    General Law: A regular polygon with n sides has exactly n lines of symmetry!
                </p>
                <div class='grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center font-mono text-[11px] mt-2'>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-cyan-300'>Equilateral Triangle<br><strong>3 Lines</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-amber-300'>Square<br><strong>4 Lines</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-emerald-300'>Regular Pentagon<br><strong>5 Lines</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-purple-300'>Regular Hexagon<br><strong>6 Lines</strong></div>
                </div>
                <p class='text-slate-300 text-xs mt-2'>
                    • <span class='text-cyan-300 font-bold'>Kepler's Snowflakes:</span> In 1611, Johannes Kepler wrote <em>De Nive Sexangula</em> ('On the Six-Cornered Snowflake'), marveling at why water ice crystals always form 6-cornered star shapes with exactly 6 lines of symmetry!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Irregular polygons with n sides do not follow this rule; only regular polygons have n lines of symmetry.
            </p>
        """,
        "summary": "Every regular polygon with n sides has exactly n lines of symmetry. Natural ice snowflakes display 6 lines of hexagonal symmetry.",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "How many lines of symmetry does a regular octagon (8 equal sides) have?",
                "options": ["4", "6", "8", "16"],
                "correct": 2,
                "explanation": "A regular polygon with n sides has n lines of symmetry. For an octagon, n = 8 lines."
            },
            {
                "id": "cp4_2",
                "question": "How many lines of symmetry does a natural hexagonal snowflake exhibit?",
                "options": ["3", "4", "6", "12"],
                "correct": 2,
                "explanation": "Snow crystals freeze in a hexagonal lattice, producing 6-fold radial symmetry with 6 lines of symmetry."
            }
        ]
    },

    # Slide 5: Mirror Reflections
    {
        "id": 5,
        "badge": "Core Concept",
        "title": "Mirror Reflections",
        "subtitle": "Perpendicular Distances Across the Mirror Line",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A line of symmetry behaves exactly like a double-sided flat mirror. When you place a mirror along the line, the reflection in the glass completes the other half of the figure:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Two Sacred Rules of Reflection:</p>
                <p class='text-slate-300'>
                    1. <span class='text-cyan-300 font-bold'>Perpendicular Alignment:</span> The line segment joining any original point P to its reflected image P' is strictly perpendicular to the mirror line (<span class='font-mono'>PP' ⊥ Line</span>).
                </p>
                <p class='text-slate-300'>
                    2. <span class='text-amber-300 font-bold'>Equal Distance Invariance:</span> Point P and its reflection P' are at the exact same perpendicular distance from the mirror line (<span class='font-mono'>Distance(P, Mirror) = Distance(P', Mirror)</span>).
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-emerald-300 text-xs'>
                    The mirror line is the perpendicular bisector of segment PP'!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Lateral Inversion: A mirror reverses left and right, which is why your right hand appears as a left hand in your reflection.
            </p>
        """,
        "summary": "Reflection across a line preserves distances: the line connecting a point and its image is perpendicular to the mirror and bisected by it.",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "If point P is 3 cm in front of a mirror line, where does its reflected image P' appear?",
                "options": [
                    "3 cm behind the mirror line along the perpendicular",
                    "6 cm in front of the mirror",
                    "Exactly on the mirror line",
                    "1.5 cm behind the mirror"
                ],
                "correct": 0,
                "explanation": "The image is located at the exact same perpendicular distance behind the mirror line: 3 cm."
            },
            {
                "id": "cp5_2",
                "question": "What is the angle between the mirror line and the line segment joining any point to its reflected image?",
                "options": ["45°", "90°", "180°", "60°"],
                "correct": 1,
                "explanation": "The line segment connecting a point to its reflection is strictly perpendicular (90°) to the mirror line."
            }
        ]
    },

    # Slide 6: Ink Blot Patterns
    {
        "id": 6,
        "badge": "Core Concept",
        "title": "Ink Blot Patterns",
        "subtitle": "Generating Symmetrical Forms by Crease Folding",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                One of the most enjoyable hands-on experiments to produce instant, intricate bilateral symmetry is the classic <span class='text-amber-400 font-semibold'>ink blot</span> technique:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>The 3-Step Ink Blot Activity:</p>
                <p class='text-slate-300'>
                    1. <span class='text-cyan-300 font-bold'>Fold & Crease:</span> Fold a blank sheet of paper in half and press down firmly to create a straight center crease line.<br>
                    2. <span class='text-amber-300 font-bold'>Apply Ink:</span> Unfold the sheet and place a few drops of wet ink or tempera paint on only one half of the paper.<br>
                    3. <span class='text-emerald-300 font-bold'>Press & Reveal:</span> Fold the paper back along the crease and press down gently. When you unfold it, the wet ink has transferred identically to the opposite side!
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 text-xs'>
                    Result: The central crease line is guaranteed to be a true line of symmetry!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Swiss psychiatrist Hermann Rorschach famously adapted ink blot symmetry in the 1920s for psychological perception studies.
            </p>
        """,
        "summary": "Folding paper over wet ink forces the ink to imprint symmetrically across the crease. The crease line becomes the axis of symmetry.",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "In the ink blot activity, what role does the fold crease play in the finished artwork?",
                "options": [
                    "It is the line of symmetry",
                    "It is the outer boundary",
                    "It has no geometric significance",
                    "It acts as an eraser"
                ],
                "correct": 0,
                "explanation": "Because the wet ink transfers directly across the fold, the crease line acts as the axis of symmetry."
            },
            {
                "id": "cp6_2",
                "question": "Can an ink blot pattern have 2 perpendicular lines of symmetry?",
                "options": [
                    "No, only 1 is ever possible",
                    "Yes, by folding the paper in half, and then in half again (quarters) before applying ink at the corner",
                    "Only if round paper is used",
                    "Only with colored ink"
                ],
                "correct": 1,
                "explanation": "Folding in half and then folding perpendicularly creates two intersecting crease lines, producing 2 lines of symmetry."
            }
        ]
    },

    # Slide 7: Paper Folding & Cuts
    {
        "id": 7,
        "badge": "Core Concept",
        "title": "Paper Folding & Cuts",
        "subtitle": "Kirigami Art: Creating Symmetrical Cutouts",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Paper cutting (<span class='text-amber-400 font-semibold'>Kirigami</span>) uses single or multiple folds to construct decorative garlands, stars, and snowflakes:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Single vs Double Fold Cutouts:</p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>Single Fold (1 Line of Symmetry):</span> Fold paper once in half. Cut a profile along the folded spine (e.g. half a heart or half a pine tree). Unfolding reveals a complete symmetrical figure with 1 line of symmetry along the crease.
                </p>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Double Fold (2 Lines of Symmetry):</span> Fold paper in half horizontally, then vertically into quarters. Cutting a shape along the folded corner produces a 4-petal flower or decorative doily with 2 perpendicular lines of symmetry!
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-emerald-300 text-xs'>
                    k Folds along radiating angles create 2^k or regular n-fold symmetrical cutouts!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Every cut along a folded edge mirrors across that fold, ensuring perfect symmetry when the paper is flattened.
            </p>
        """,
        "summary": "Cutting shapes from folded paper creates symmetrical cutouts. A single fold yields 1 line of symmetry; a double fold yields 2 perpendicular lines.",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "To cut out a symmetrical heart shape with 1 vertical line of symmetry, how should the paper be folded?",
                "options": [
                    "Once in half vertically, cutting half the heart along the folded edge",
                    "In quarters into a small square",
                    "Rolled into a cylinder",
                    "Folded into 3 equal parts"
                ],
                "correct": 0,
                "explanation": "Folding once in half and cutting half the heart profile along the crease creates a full symmetrical heart upon unfolding."
            },
            {
                "id": "cp7_2",
                "question": "If a paper folded in half twice (into quarters) has a small triangle snipped from its folded corner, how many triangle holes appear when unfolded?",
                "options": ["1", "2", "4", "8"],
                "correct": 2,
                "explanation": "The 4-layer folded corner unfolds into 4 symmetrical cuts arranged around the center."
            }
        ]
    },

    # Slide 8: The Punching Game
    {
        "id": 8,
        "badge": "Core Concept",
        "title": "The Punching Game",
        "subtitle": "Punching Holes in Folded Sheets & Identifying Creases",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                In the classic NCERT <span class='text-amber-400 font-semibold'>Punching Game</span>, students explore the relationship between hole positions and fold lines:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>How the Game Works:</p>
                <p class='text-slate-300'>
                    1. A square paper is folded in half (vertically, horizontally, or diagonally).<br>
                    2. One or two circular holes are punched through all layers with a hole puncher.<br>
                    3. The paper is unfolded flat.<br>
                    4. <em>The Detective Challenge:</em> Given the pattern of punched holes on the flat paper, determine where the original fold line was located!
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-cyan-300 text-xs'>
                    Rule: The fold line is ALWAYS the perpendicular bisector connecting each pair of matching holes!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                If you connect any hole to its matching partner, the line of symmetry is the exact perpendicular bisector halfway between them.
            </p>
        """,
        "summary": "Punching a hole in folded paper creates pairs of holes equidistant from the fold line. The fold line is the perpendicular bisector between matching holes.",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "A square sheet is folded along its vertical centerline, and 1 hole is punched. How many holes are visible when unfolded?",
                "options": ["1", "2", "4", "0"],
                "correct": 1,
                "explanation": "The punch penetrates both layers of paper, producing 2 matching holes equidistant from the center vertical fold."
            },
            {
                "id": "cp8_2",
                "question": "If you see two punched holes symmetrically placed near the top-left and bottom-right corners of a square, along which line was the paper folded?",
                "options": [
                    "Along the vertical centerline",
                    "Along the horizontal centerline",
                    "Along the diagonal connecting bottom-left to top-right",
                    "Along the bottom edge"
                ],
                "correct": 2,
                "explanation": "The diagonal from bottom-left to top-right serves as the mirror axis perpendicular to the segment joining top-left and bottom-right."
            }
        ]
    },

    # Slide 9: Rotational Center
    {
        "id": 9,
        "badge": "Core Concept",
        "title": "Rotational Center",
        "subtitle": "Figures that Coincide When Spun Around a Fixed Point",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Consider a child's toy paper windmill (or pinwheel) with 4 curved curved blades. If you try to fold it in half, the curved blades stick out; it has <span class='text-rose-400 font-semibold'>zero lines of symmetry</span>. Yet it is undeniably symmetrical! Why?
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Rotational Symmetry Defined:</p>
                <p class='text-slate-300'>
                    A figure has <span class='text-amber-400 font-semibold'>rotational symmetry</span> if it can be spun around a fixed central point and look exactly identical to its original position before making a full 360° turn!
                </p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>Centre of Rotation:</span> The fixed point about which the figure rotates (like the pin in the center of the windmill or the axle of a ceiling fan).<br>
                    • <span class='text-emerald-300 font-bold'>Direction:</span> Rotation can occur clockwise or counter-clockwise; the symmetry properties remain identical.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                A ceiling fan with 3 identical blades looks unchanged after being rotated by one-third of a turn (120°).
            </p>
        """,
        "summary": "A figure has rotational symmetry if spinning it around a central point by less than 360° matches its original appearance. The fixed point is the center of rotation.",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "What is the fixed central point about which a figure rotates called?",
                "options": ["Center of rotation", "Axis of reflection", "Vertex", "Radius"],
                "correct": 0,
                "explanation": "The central pivot point that remains motionless while the figure spins is the center of rotation."
            },
            {
                "id": "cp9_2",
                "question": "Can a figure have rotational symmetry even if it has ZERO lines of reflection symmetry?",
                "options": [
                    "No, rotational symmetry requires lines of symmetry",
                    "Yes, like a 4-blade paper pinwheel or the letter 'S'",
                    "Only if it is a perfect square",
                    "Only in 3D geometry"
                ],
                "correct": 1,
                "explanation": "A paper pinwheel or the letter 'S' has no lines of folding symmetry, yet coincides with itself upon rotating (rotational symmetry)."
            }
        ]
    },

    # Slide 10: Angle of Symmetry
    {
        "id": 10,
        "badge": "Core Concept",
        "title": "Angle of Symmetry",
        "subtitle": "The Minimum Angle to Match Original Appearance",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Every physical object in the universe returns to its original position after a complete full turn of <span class='font-mono text-cyan-300 font-bold'>360°</span>. Therefore, 360° is trivial. What matters is rotation by <em>less than 360°</em>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Angle of Symmetry:</span> The smallest non-zero angle through which a figure must be rotated to match its original position.
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-cyan-300 text-xs'>
                    Criteria: 0° < Smallest Angle of Symmetry < 360°
                </div>
                <p class='text-slate-300'>
                    • If a figure only matches itself after a full 360° turn (like a scalene triangle or the letter P), it is said to have <strong>NO rotational symmetry</strong> (or order 1, which is considered trivial).<br>
                    • All subsequent angles of symmetry for a figure are exact integer multiples of its smallest angle of symmetry!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Example: A square matches at 90°, 180°, 270°, and 360°. Its smallest angle of symmetry is 90°.
            </p>
        """,
        "summary": "The angle of symmetry is the smallest non-zero angle of rotation that brings a figure onto itself. All other symmetry angles are multiples of this smallest angle.",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "What is the smallest angle of symmetry for a square rotated about its center?",
                "options": ["45°", "90°", "180°", "360°"],
                "correct": 1,
                "explanation": "Rotating a square by a quarter-turn (90°) maps each corner to the next corner, matching its original shape."
            },
            {
                "id": "cp10_2",
                "question": "If a figure has a smallest angle of symmetry equal to 60°, what are all its angles of symmetry within one full turn?",
                "options": [
                    "Only 60°",
                    "60°, 120°, 180°, 240°, 300°, and 360°",
                    "60° and 180°",
                    "60° and 90°"
                ],
                "correct": 1,
                "explanation": "All angles of symmetry are multiples of the smallest angle (60°): 60°, 120°, 180°, 240°, 300°, 360°."
            }
        ]
    },

    # Slide 11: Radial Windmills
    {
        "id": 11,
        "badge": "Core Concept",
        "title": "Radial Windmills",
        "subtitle": "Formula for n Equally Spaced Radial Arms: 360° / n",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When a shape has <span class='font-mono text-cyan-300 font-bold'>n</span> identical, equally spaced arms or petals radiating from a central point, there is a direct mathematical formula for its smallest angle of symmetry:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2.5 rounded bg-slate-900 border border-amber-500/30 text-center font-mono text-amber-300 font-bold text-sm'>
                    Smallest Angle of Symmetry = 360° / n
                </div>
                <div class='grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono text-[11px] mt-2'>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-cyan-300'>3-Blade Fan<br>360° ÷ 3 = <strong>120°</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-amber-300'>4-Blade Windmill<br>360° ÷ 4 = <strong>90°</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-emerald-300'>5-Arm Starfish<br>360° ÷ 5 = <strong>72°</strong></div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-purple-300'>6-Fold Snowflake<br>360° ÷ 6 = <strong>60°</strong></div>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Because the circle encompasses 360°, n equally spaced blades divide that total angle into n equal rotational sectors.
            </p>
        """,
        "summary": "For a figure with n identical equally spaced radial arms, the smallest angle of symmetry is 360° / n.",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "What is the smallest angle of symmetry for a 5-pointed regular star (or 5-arm starfish)?",
                "options": ["50°", "60°", "72°", "90°"],
                "correct": 2,
                "explanation": "360° divided by 5 equal arms = 72°."
            },
            {
                "id": "cp11_2",
                "question": "A ceiling fan has 3 identical blades spaced equally. By what minimum angle must it be rotated to look unchanged?",
                "options": ["90°", "120°", "180°", "360°"],
                "correct": 1,
                "explanation": "360° divided by 3 blades = 120°."
            }
        ]
    },

    # Slide 12: Order of Rotation
    {
        "id": 12,
        "badge": "Core Concept",
        "title": "Order of Rotation",
        "subtitle": "Counting Coinciding Positions During One Complete Turn",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Mathematicians describe rotational symmetry using the concept of <span class='text-amber-400 font-semibold'>order</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Definition of Order of Rotational Symmetry:</p>
                <p class='text-slate-300'>
                    The <span class='text-cyan-300 font-bold'>order</span> is the total number of distinct positions during a full 360° rotation where the figure looks exactly like its starting position (including the final 360° position).
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 text-xs'>
                    Order of Rotational Symmetry = 360° / (Smallest Angle of Symmetry)
                </div>
                <div class='space-y-1 text-slate-300 text-[11px] mt-1'>
                    • <strong>Rectangle:</strong> Coincides at 180° and 360° → <strong>Order 2</strong>.<br>
                    • <strong>Equilateral Triangle:</strong> Coincides at 120°, 240°, 360° → <strong>Order 3</strong>.<br>
                    • <strong>Square:</strong> Coincides at 90°, 180°, 270°, 360° → <strong>Order 4</strong>.<br>
                    • <strong>Regular Hexagon:</strong> Coincides every 60° → <strong>Order 6</strong>.
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                A figure must have order ≥ 2 to be said to possess rotational symmetry. Order 1 simply means full 360° rotation (no symmetry).
            </p>
        """,
        "summary": "The order of rotational symmetry is the number of times a figure matches its starting shape in a 360° turn: Order = 360° / smallest angle.",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "What is the order of rotational symmetry for a non-square rectangle?",
                "options": ["1", "2", "4", "0"],
                "correct": 1,
                "explanation": "A rectangle matches itself after a half-turn (180°) and a full-turn (360°), giving an order of 2."
            },
            {
                "id": "cp12_2",
                "question": "If a shape has a smallest angle of symmetry of 45°, what is its order of rotational symmetry?",
                "options": ["4", "6", "8", "10"],
                "correct": 2,
                "explanation": "Order = 360° ÷ 45° = 8."
            }
        ]
    },

    # Slide 13: Symmetries of a Circle
    {
        "id": 13,
        "badge": "Core Concept",
        "title": "Symmetries of a Circle",
        "subtitle": "The Champion of Geometry: Infinitely Symmetrical",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                The circle stands supreme as the most perfectly symmetrical figure in the entire universe, possessing <span class='text-amber-400 font-semibold'>infinite symmetries</span> in both reflection and rotation:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-cyan-500/30 text-cyan-200'>
                    <span class='font-bold text-cyan-300 font-mono'>Infinite Lines of Reflection Symmetry:</span><br>
                    • Every straight line passing through the center of a circle (a diameter) is a line of symmetry!<br>
                    • Since infinitely many diameters can be drawn, a circle has <strong>infinitely many lines of symmetry</strong>.
                </div>
                <div class='p-2 rounded bg-slate-900 border border-amber-500/30 text-amber-200'>
                    <span class='font-bold text-amber-300 font-mono'>Infinite Rotational Symmetry:</span><br>
                    • Rotate a circle by 1°, 5°, 0.001°, or any angle whatsoever about its center—it coincides with itself perfectly!<br>
                    • It has an <strong>infinite order of rotational symmetry</strong>.
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                No polygon can claim infinite symmetry; as the number of sides n of a regular polygon approaches infinity, it approaches the perfection of the circle.
            </p>
        """,
        "summary": "A circle has infinite lines of symmetry (every diameter) and infinite rotational symmetry (it matches itself under rotation by any angle).",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "Which lines passing through a circle act as lines of reflection symmetry?",
                "options": [
                    "Only the vertical and horizontal diameters",
                    "Any straight line passing through the center (every diameter)",
                    "Chords that do not pass through the center",
                    "Tangent lines touching the outside"
                ],
                "correct": 1,
                "explanation": "Every diameter cuts the circle into two identical semicircular halves that fold onto each other."
            },
            {
                "id": "cp13_2",
                "question": "How many lines of symmetry does a semicircle have?",
                "options": ["Infinite", "2", "1", "0"],
                "correct": 2,
                "explanation": "A semicircle has only 1 line of symmetry: the perpendicular bisector of its straight diameter base."
            }
        ]
    },

    # Slide 14: Tile Symmetry Studio
    {
        "id": 14,
        "badge": "Core Concept",
        "title": "Tile Symmetry Studio",
        "subtitle": "Completing Grid Patterns Across 1, 2 or 4 Symmetry Axes",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Artists creating rangoli, mosaic tiles, and floor patterns use grid reflection rules to mirror colored tiles across designated axes of symmetry:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Mirroring Rules on a Square Grid:</p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>1 Line (Vertical Axis):</span> A shaded cell at column 1, row 2 must be mirrored across the vertical center to column 4, row 2.<br>
                    • <span class='text-amber-300 font-bold'>2 Lines (Vertical + Horizontal):</span> The cell must be reflected across both axes, appearing in all 4 quadrants (4 tiles total).<br>
                    • <span class='text-emerald-300 font-bold'>4 Lines (Dual Axes + Diagonals):</span> Shading 1 cell near a corner automatically propagates to 8 symmetric positions around the square!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Every traditional Indian Kolam or Persian carpet border relies on these exact 2-axis or 4-axis grid reflections.
            </p>
        """,
        "summary": "Shading tiles on a grid across symmetry lines creates multi-axis designs. 1 line duplicates tiles; 2 lines quadruples them; 4 lines octuples them.",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "If a design has 2 perpendicular lines of symmetry, into how many identical quadrant quadrants is the grid divided?",
                "options": ["2", "4", "6", "8"],
                "correct": 1,
                "explanation": "Two perpendicular lines (horizontal and vertical) partition the plane into 4 identical quadrants."
            },
            {
                "id": "cp14_2",
                "question": "If you color 1 cell in a corner of a square grid that has 4 lines of symmetry, how many total cells must be colored to preserve symmetry?",
                "options": ["2", "4", "8", "16"],
                "correct": 2,
                "explanation": "With 4 lines of symmetry (horizontal, vertical, 2 diagonals), a single asymmetrical corner point reflects into 8 symmetric positions."
            }
        ]
    },

    # Slide 15: The Symmetry Grid Game
    {
        "id": 15,
        "badge": "Core Concept",
        "title": "The Symmetry Grid Game",
        "subtitle": "Strategic Spatial Play on a 6×6 Grid",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Mathematics transforms into strategy in the NCERT <span class='text-amber-400 font-semibold'>6×6 Grid Game</span>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Rules of the 2-Player Grid Game:</p>
                <p class='text-slate-300'>
                    1. The board is a 6×6 grid of dots.<br>
                    2. Players take turns drawing a straight line segment of length 1 unit between two adjacent dots.<br>
                    3. No two line segments may cross or touch.<br>
                    4. The player who cannot place a valid line segment loses.
                </p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-emerald-300 text-xs'>
                    The Winning Symmetry Strategy: Player 2 can guarantee a win by playing the exact rotational counterpart (180° rotation) of whatever move Player 1 makes!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Symmetry is not just decorative—it provides unbeatable mathematical winning strategies in combinatorial game theory.
            </p>
        """,
        "summary": "In the 6×6 grid line-placement game, Player 2 can mirror Player 1's moves using point reflection (180° rotational symmetry) to ensure a winning move always exists.",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "In a 2-player spatial grid game, what symmetry strategy allows a player to guarantee a matching valid response to every move?",
                "options": [
                    "Random guessing",
                    "Playing the symmetrical counterpart of the opponent's move across the center",
                    "Playing only in the corners",
                    "Passing turns"
                ],
                "correct": 1,
                "explanation": "Mirroring the opponent's move through the central point of symmetry guarantees that if their move was valid, the symmetrical counterpart is also unoccupied."
            },
            {
                "id": "cp15_2",
                "question": "What type of symmetry is used when a response move is placed at the point directly opposite the center (180° spin)?",
                "options": [
                    "Point symmetry (Order 2 rotational symmetry)",
                    "Vertical reflection only",
                    "Translational symmetry",
                    "No symmetry"
                ],
                "correct": 0,
                "explanation": "Reflecting through a center point is mathematically identical to a 180° rotation (point symmetry)."
            }
        ]
    },

    # Slide 16: The Symmetry Matrix
    {
        "id": 16,
        "badge": "Core Concept",
        "title": "The Symmetry Matrix",
        "subtitle": "Classifying Shapes: Line, Rotational, Both, or Neither",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Every 2D geometric figure can be comprehensively classified into one of four distinct categories based on its symmetries:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono'>
                    <div class='p-2.5 rounded bg-slate-900 border border-emerald-500/40 text-emerald-300'>
                        <strong>1. Both Line & Rotational:</strong><br>
                        • Square (4 lines, order 4)<br>
                        • Rectangle (2 lines, order 2)<br>
                        • Equilateral Triangle (3 lines, order 3)<br>
                        • Circle (infinite lines, infinite order)
                    </div>
                    <div class='p-2.5 rounded bg-slate-900 border border-cyan-500/40 text-cyan-300'>
                        <strong>2. Rotational Only (No Lines):</strong><br>
                        • Paper Pinwheel / Windmill<br>
                        • The Letter 'Z' (order 2)<br>
                        • The Letter 'S' (order 2)<br>
                        • Parallelogram (order 2)
                    </div>
                    <div class='p-2.5 rounded bg-slate-900 border border-amber-500/40 text-amber-300'>
                        <strong>3. Line Only (No Rotation):</strong><br>
                        • Isosceles Triangle (1 line, order 1)<br>
                        • The Letter 'A' (1 line)<br>
                        • The Letter 'M' (1 line)<br>
                        • Kite (1 line)
                    </div>
                    <div class='p-2.5 rounded bg-slate-900 border border-rose-500/40 text-rose-300'>
                        <strong>4. Neither (Asymmetrical):</strong><br>
                        • Scalene Triangle (0 lines, order 1)<br>
                        • The Letter 'F'<br>
                        • The Letter 'P'<br>
                        • General Quadrilateral
                    </div>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                This 4-way classification matrix unifies the study of reflectional and rotational transformations in plane geometry.
            </p>
        """,
        "summary": "Shapes fall into 4 groups: Both Line and Rotational (Square, Rectangle), Rotational Only (Pinwheel, Z, S), Line Only (Isosceles Triangle, A), or Neither (Scalene Triangle, F).",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "Which category does a non-rectangular parallelogram belong to?",
                "options": [
                    "Both line and rotational symmetry",
                    "Rotational symmetry only (Order 2, zero lines of symmetry)",
                    "Line symmetry only",
                    "Neither line nor rotational"
                ],
                "correct": 1,
                "explanation": "A general parallelogram has order 2 rotational symmetry (180°), but has 0 lines of reflection symmetry."
            },
            {
                "id": "cp16_2",
                "question": "Which of the following shapes has NEITHER line symmetry NOR rotational symmetry?",
                "options": ["A scalene triangle", "An equilateral triangle", "A square", "A rectangle"],
                "correct": 0,
                "explanation": "A scalene triangle has 3 unequal sides, giving it 0 lines of symmetry and only trivial order 1 rotation."
            }
        ]
    },

    # Quiz Slide 1: Questions 1 to 10
    {
        "id": 17,
        "badge": "Mastery Challenge",
        "title": "Quiz 1",
        "subtitle": "Lines of Symmetry, Folding & Reflection Basics",
        "is_quiz": True,
        "quiz_range": (1, 10)
    },

    # Quiz Slide 2: Questions 11 to 20
    {
        "id": 18,
        "badge": "Mastery Challenge",
        "title": "Quiz 2",
        "subtitle": "Polygons, Rectangles, Hole Punches & Snowflakes",
        "is_quiz": True,
        "quiz_range": (11, 20)
    },

    # Quiz Slide 3: Questions 21 to 30
    {
        "id": 19,
        "badge": "Mastery Challenge",
        "title": "Quiz 3",
        "subtitle": "Rotational Centers, Angles of Symmetry & Radial Arms",
        "is_quiz": True,
        "quiz_range": (21, 30)
    },

    # Quiz Slide 4: Questions 31 to 40
    {
        "id": 20,
        "badge": "Mastery Challenge",
        "title": "Quiz 4",
        "subtitle": "Circle Symmetries, Tile Grids & Classification Matrix",
        "is_quiz": True,
        "quiz_range": (31, 40)
    }
]

QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "What is a line of symmetry?",
        "options": [
            "A line that divides a shape into two parts that overlap exactly upon folding",
            "Any diagonal line inside a polygon",
            "A line that touches the outside of a circle",
            "The longest side of a triangle"
        ],
        "correct": 0,
        "solution": "A line of symmetry is an axis that partitions a figure into two identical halves that coincide exactly when folded along it."
    },
    # Q2
    {
        "id": 2,
        "question": "How many lines of symmetry does a square have?",
        "options": ["2", "4", "8", "Infinite"],
        "correct": 1,
        "solution": "A square has 4 lines of symmetry: 1 vertical, 1 horizontal, and 2 diagonals."
    },
    # Q3
    {
        "id": 3,
        "question": "How many lines of symmetry does a non-square rectangle have?",
        "options": ["1", "2", "4", "0"],
        "correct": 1,
        "solution": "A rectangle has only 2 lines of symmetry (connecting opposite midpoints). Its diagonals are not lines of symmetry."
    },
    # Q4
    {
        "id": 4,
        "question": "Which of the following capital letters has BOTH vertical and horizontal lines of symmetry?",
        "options": ["A", "M", "H", "C"],
        "correct": 2,
        "solution": "The letter 'H' can be folded in half vertically and horizontally with exact overlap, giving 2 lines of symmetry."
    },
    # Q5
    {
        "id": 5,
        "question": "How many lines of symmetry does an equilateral triangle possess?",
        "options": ["1", "2", "3", "6"],
        "correct": 2,
        "solution": "An equilateral triangle has 3 lines of symmetry, each passing through a vertex and the midpoint of the opposite side."
    },
    # Q6
    {
        "id": 6,
        "question": "How many lines of symmetry does an isosceles triangle with only two equal sides possess?",
        "options": ["0", "1", "2", "3"],
        "correct": 1,
        "solution": "An isosceles triangle has exactly 1 line of symmetry: the altitude passing from the vertex between the two equal sides to the base."
    },
    # Q7
    {
        "id": 7,
        "question": "In mirror reflection, if an object point is 7 cm in front of the mirror, how far behind the mirror is the reflected image?",
        "options": ["3.5 cm", "7 cm", "14 cm", "0 cm"],
        "correct": 1,
        "solution": "Mirror reflection preserves perpendicular distance. The virtual image is located at the exact same distance: 7 cm behind the mirror."
    },
    # Q8
    {
        "id": 8,
        "question": "What is the result of folding a piece of paper over wet ink?",
        "options": [
            "The paper dissolves",
            "An ink blot pattern with the crease line as the axis of symmetry",
            "A circle of radius 5 cm",
            "An asymmetrical blob"
        ],
        "correct": 1,
        "solution": "Pressing the folded paper transfers the wet ink to identical matching positions across the crease line, creating bilateral symmetry."
    },
    # Q9
    {
        "id": 9,
        "question": "How many lines of symmetry does a scalene triangle have?",
        "options": ["0", "1", "2", "3"],
        "correct": 0,
        "solution": "A scalene triangle has 3 unequal sides and 3 unequal angles, so no fold line can produce matching overlapping halves. It has 0 lines of symmetry."
    },
    # Q10
    {
        "id": 10,
        "question": "Which of the following geometric figures has ZERO lines of symmetry?",
        "options": ["A parallelogram (with unequal sides and angles)", "A square", "An isosceles trapezoid", "A regular pentagon"],
        "correct": 0,
        "solution": "A general parallelogram cannot be folded along any line to match its halves. It has 0 lines of symmetry."
    },

    # Q11
    {
        "id": 11,
        "question": "How many lines of symmetry does a regular hexagon have?",
        "options": ["3", "6", "12", "1"],
        "correct": 1,
        "solution": "A regular polygon with n sides has n lines of symmetry. For a regular hexagon, n = 6."
    },
    # Q12
    {
        "id": 12,
        "question": "Why does a diagonal of a general rectangle fail to be a line of symmetry?",
        "options": [
            "Because the diagonal is longer than the sides",
            "Because upon folding along the diagonal, the adjacent unequal sides do not coincide, causing corners to project outward",
            "Because a rectangle has right angles",
            "Because opposite sides are parallel"
        ],
        "correct": 1,
        "solution": "Folding a rectangle along its diagonal does not cause the perimeter edges to coincide because adjacent sides have unequal lengths."
    },
    # Q13
    {
        "id": 13,
        "question": "A square paper is folded along both diagonals. A hole is punched through all 4 layers near the outer edge. How many holes appear upon unfolding?",
        "options": ["1", "2", "4", "8"],
        "correct": 2,
        "solution": "Folding along both diagonals creates 4 triangular layers. Punching once through the 4 layers produces 4 symmetrical holes."
    },
    # Q14
    {
        "id": 14,
        "question": "What famous 1611 treatise by Johannes Kepler investigated the 6-fold radial symmetry of snowflakes?",
        "options": ["Harmonices Mundi", "De Nive Sexangula", "Astronomia Nova", "Mystrium Cosmographicum"],
        "correct": 1,
        "solution": "Johannes Kepler wrote 'De Nive Sexangula' (The Six-Cornered Snowflake) in 1611, exploring the mathematical hexagonal symmetry of ice crystals."
    },
    # Q15
    {
        "id": 15,
        "question": "How many lines of symmetry does a kite quadrilateral have (with 2 distinct pairs of adjacent equal sides)?",
        "options": ["0", "1", "2", "4"],
        "correct": 1,
        "solution": "A kite has exactly 1 line of symmetry: the main diagonal that connects the vertices between the pairs of equal sides."
    },
    # Q16
    {
        "id": 16,
        "question": "How many lines of symmetry does a regular decagon (10 equal sides) have?",
        "options": ["5", "10", "20", "2"],
        "correct": 1,
        "solution": "A regular polygon with n sides has exactly n lines of symmetry. For a decagon, n = 10."
    },
    # Q17
    {
        "id": 17,
        "question": "In the punching game, if two holes appear on an unfolded sheet, where is the fold line located?",
        "options": [
            "Through one of the holes",
            "Along the perpendicular bisector of the line segment joining the two holes",
            "Along the bottom edge of the paper",
            "Diagonally at 45° always"
        ],
        "correct": 1,
        "solution": "The fold line is always the mirror axis, which is the perpendicular bisector connecting each pair of corresponding punched holes."
    },
    # Q18
    {
        "id": 18,
        "question": "How many lines of symmetry does the capital letter 'Z' have?",
        "options": ["0", "1", "2", "4"],
        "correct": 0,
        "solution": "The letter 'Z' cannot be folded along any line to match its halves. It has 0 lines of symmetry (though it has rotational symmetry)."
    },
    # Q19
    {
        "id": 19,
        "question": "A rhombus that is NOT a square has how many lines of symmetry?",
        "options": ["1", "2", "4", "0"],
        "correct": 1,
        "solution": "A rhombus has 2 lines of symmetry: its two diagonals. (Unlike a square, lines through side midpoints are not lines of symmetry)."
    },
    # Q20
    {
        "id": 20,
        "question": "How many lines of symmetry does a regular pentagon have?",
        "options": ["3", "5", "10", "1"],
        "correct": 1,
        "solution": "A regular pentagon has 5 lines of symmetry, each connecting a vertex to the midpoint of the opposite side."
    },

    # Q21
    {
        "id": 21,
        "question": "What is meant by 'rotational symmetry'?",
        "options": [
            "A figure coincides with its original appearance when rotated by an angle less than 360° about a fixed center",
            "A figure can only be reflected in a mirror",
            "A figure rolls down a hill",
            "A figure grows larger when spun"
        ],
        "correct": 0,
        "solution": "A figure possesses rotational symmetry if it matches its starting outline after a rotation strictly between 0° and 360°."
    },
    # Q22
    {
        "id": 22,
        "question": "What is the smallest angle of symmetry for a 4-blade paper windmill?",
        "options": ["45°", "90°", "180°", "360°"],
        "correct": 1,
        "solution": "With 4 identical equally spaced blades, smallest angle = 360° ÷ 4 = 90°."
    },
    # Q23
    {
        "id": 23,
        "question": "What is the order of rotational symmetry of a square?",
        "options": ["2", "4", "8", "1"],
        "correct": 1,
        "solution": "A square matches itself at 90°, 180°, 270°, and 360°—a total of 4 times during a full rotation (Order 4)."
    },
    # Q24
    {
        "id": 24,
        "question": "What is the order of rotational symmetry of an equilateral triangle?",
        "options": ["1", "2", "3", "6"],
        "correct": 2,
        "solution": "An equilateral triangle matches itself at 120°, 240°, and 360° (Order 3)."
    },
    # Q25
    {
        "id": 25,
        "question": "What is the smallest angle of symmetry for a figure with 8 identical radial arms?",
        "options": ["30°", "40°", "45°", "60°"],
        "correct": 2,
        "solution": "360° ÷ 8 = 45°."
    },
    # Q26
    {
        "id": 26,
        "question": "What is the order of rotational symmetry of the capital letter 'N'?",
        "options": ["1", "2", "4", "0"],
        "correct": 1,
        "solution": "Rotating the letter 'N' by 180° reproduces the letter 'N'. It matches at 180° and 360°, giving an order of 2."
    },
    # Q27
    {
        "id": 27,
        "question": "If a shape has rotational symmetry of order 6, what is its smallest angle of symmetry?",
        "options": ["30°", "45°", "60°", "90°"],
        "correct": 2,
        "solution": "Smallest angle = 360° ÷ order = 360° ÷ 6 = 60°."
    },
    # Q28
    {
        "id": 28,
        "question": "Does a non-square rectangle have rotational symmetry? If so, what is its order?",
        "options": [
            "No, order 1 only",
            "Yes, order 2 (it matches at 180° and 360°)",
            "Yes, order 4 (matches every 90°)",
            "Yes, order 3"
        ],
        "correct": 1,
        "solution": "A rectangle looks unchanged after a half-turn (180°) and a full turn (360°), so its order of rotational symmetry is 2."
    },
    # Q29
    {
        "id": 29,
        "question": "Which of the following figures has rotational symmetry but NO lines of reflection symmetry?",
        "options": ["Square", "Equilateral triangle", "Paper pinwheel / windmill", "Circle"],
        "correct": 2,
        "solution": "A paper windmill has curved blades that prevent reflection folding, but matches itself every 90° rotation (rotational symmetry only)."
    },
    # Q30
    {
        "id": 30,
        "question": "What is the smallest angle of symmetry for a ceiling fan with 3 equally spaced blades?",
        "options": ["60°", "90°", "120°", "180°"],
        "correct": 2,
        "solution": "360° ÷ 3 = 120°."
    },

    # Q31
    {
        "id": 31,
        "question": "How many lines of symmetry does a complete circle have?",
        "options": ["360", "1000", "Infinitely many", "4"],
        "correct": 2,
        "solution": "Every diameter passing through the center of a circle forms a line of reflection symmetry. There are infinitely many diameters, so a circle has infinitely many lines of symmetry."
    },
    # Q32
    {
        "id": 32,
        "question": "What is the order of rotational symmetry of a circle about its center?",
        "options": ["360", "Infinitely many (infinite order)", "100", "4"],
        "correct": 1,
        "solution": "A circle coincides with itself when rotated by ANY angle about its center, possessing infinite rotational symmetry."
    },
    # Q33
    {
        "id": 33,
        "question": "Which English capital letter has order 2 rotational symmetry but NO line of symmetry?",
        "options": ["H", "Z", "A", "O"],
        "correct": 1,
        "solution": "The letter 'Z' has 0 lines of symmetry, but looks identical when rotated by 180° (order 2 rotational symmetry)."
    },
    # Q34
    {
        "id": 34,
        "question": "Which English capital letter has BOTH 1 line of symmetry AND NO rotational symmetry (order 1)?",
        "options": ["A", "H", "N", "X"],
        "correct": 0,
        "solution": "The letter 'A' has 1 vertical line of symmetry, but does not match itself under 180° rotation (no rotational symmetry)."
    },
    # Q35
    {
        "id": 35,
        "question": "Which English capital letter has BOTH 2 lines of symmetry AND order 2 rotational symmetry?",
        "options": ["M", "H", "P", "F"],
        "correct": 1,
        "solution": "The letter 'H' has 2 lines of symmetry (horizontal and vertical) and matches itself after a 180° rotation (order 2)."
    },
    # Q36
    {
        "id": 36,
        "question": "In a 6×6 symmetry grid game, what strategy can Player 2 employ to guarantee that a legal move is always available?",
        "options": [
            "Playing at random",
            "Playing the 180° point-reflection counterpart of Player 1's previous move",
            "Always playing on the outer border",
            "Passing their turn"
        ],
        "correct": 1,
        "solution": "By playing the 180° rotation counterpart through the center, Player 2 ensures that as long as Player 1 found an empty segment, its opposite partner is also empty."
    },
    # Q37
    {
        "id": 37,
        "question": "How many lines of symmetry does a regular nonagon (9 equal sides) have?",
        "options": ["3", "6", "9", "18"],
        "correct": 2,
        "solution": "A regular polygon with n sides has n lines of symmetry. For a nonagon, n = 9."
    },
    # Q38
    {
        "id": 38,
        "question": "A shape has order 3 rotational symmetry. What are all its angles of symmetry within 360°?",
        "options": ["120°, 240°, 360°", "90°, 180°, 270°", "60°, 120°, 180°", "30°, 60°, 90°"],
        "correct": 0,
        "solution": "360° ÷ 3 = 120°. The angles of symmetry are 120°, 240°, and 360°."
    },
    # Q39
    {
        "id": 39,
        "question": "What is the order of rotational symmetry of a regular hexagon?",
        "options": ["3", "4", "6", "12"],
        "correct": 2,
        "solution": "Smallest angle is 360° ÷ 6 = 60°. It matches at 60°, 120°, 180°, 240°, 300°, 360° (Order 6)."
    },
    # Q40
    {
        "id": 40,
        "question": "Why does a scalene triangle have an order of rotational symmetry of 1?",
        "options": [
            "Because it has 1 right angle",
            "Because it only coincides with itself after a complete full turn of 360°",
            "Because it has 1 line of symmetry",
            "Because it is an equilateral triangle"
        ],
        "correct": 1,
        "solution": "An order of 1 means a shape does not coincide at any intermediate angle, returning to its starting position only after a full 360° turn."
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
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in Symmetry data!")

if __name__ == "__main__":
    verify_data()
    with open(".agents/class6_math_symmetry_data.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch9_symmetry_data.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_symmetry_data.py")

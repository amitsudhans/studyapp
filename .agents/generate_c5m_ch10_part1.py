# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 10: Symmetrical Designs
Part 1: Slides 1 to 8 (Theory, Narration 195-215 words, 16 Checkpoints)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Reflection Symmetry",
        "tagline": "Mirror Lines • Bilateral Symmetry & Birthday Banner Paper Crafts",
        "lecture": (
            "Welcome to the delightful world of symmetry. When we look around our homes, nature, and festive decorations, "
            "we see shapes that possess perfect balance. Imagine making decorative triangular flags or festive letter cutouts "
            "for a birthday celebration. If you take a sheet of brightly colored craft paper, fold it exactly down the middle, "
            "and draw half of a heart or butterfly along the creased fold, cutting it out produces a completely balanced figure. "
            "When you unfold the paper, the central crease acts as a mirror line, known in geometry as the line of symmetry. "
            "The left half and right half match each other identically in size, shape, and orientation. If you place a real "
            "flat mirror directly along this crease, the reflection in the glass recreates the hidden half seamlessly. This "
            "phenomenon is called reflection symmetry or line symmetry. A single line divides the whole figure into two congruent "
            "congruent parts that overlap perfectly when folded. Natural objects like peepal leaves, flying birds, and handcrafted "
            "paper festoons all display this bilateral beauty. Understanding reflection lines allows craftspeople and artists to produce "
            "harmonious patterns with half the effort, because cutting one side creates both sides instantly with geometric precision."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">What is Reflection Symmetry?</h3>
                <p>A figure possesses <strong>reflection symmetry</strong> (also called <em>line symmetry</em> or <em>bilateral balance</em>) if a straight line can be drawn across it such that folding the shape along this line causes both halves to coincide exactly.</p>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">The Mirror Line:</span>
                    <p class="text-[11px] text-slate-300">Acts as a reflective axis. Every point on one side has a corresponding point on the other side at the exact same perpendicular distance.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold block mb-1">Paper Craft Magic:</span>
                    <p class="text-[11px] text-slate-300">By folding paper along the mirror line, you cut only one half; unfolding produces a perfectly balanced whole figure.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "What happens when a symmetrical shape is folded along its line of symmetry?",
                "options": [
                    "The two halves overlap perfectly without extending beyond",
                    "One half is twice as large as the other half",
                    "The shape rotates by 90 degrees",
                    "The line disappears completely"
                ],
                "answer": 0,
                "explanation": "By definition of reflection symmetry, folding along the axis of symmetry causes both halves to coincide and overlap completely."
            },
            {
                "id": "cp1_2",
                "question": "If you place a flat mirror directly along the crease of a folded cutout, what do you observe?",
                "options": [
                    "The reflected image completes the original full symmetrical design",
                    "The shape looks completely distorted and inverted",
                    "The reflection shows an upside-down triangle only",
                    "Nothing is visible in the mirror"
                ],
                "answer": 0,
                "explanation": "Because each half is a mirror reflection of the other, placing a mirror along the axis reconstructs the complete symmetrical shape."
            }
        ]
    },

    {
        "id": 2,
        "title": "Folding Letters",
        "tagline": "Paper Cutting Techniques • Single Fold for Letter A & Double Fold for Letter H",
        "lecture": (
            "Let us explore how craftspersons cut out neat capital English letters using paper folds. Consider the letter A. "
            "If you look closely at capital letter A, it has an upright symmetry. An imaginary vertical line passes straight through "
            "its top vertex and cuts across the middle crossbar. Therefore, to cut out letter A cleanly without drawing both sides, "
            "take a rectangular sheet of craft paper, fold it once vertically along its length, and sketch only the outer slope "
            "and inner triangular hole against the fold. When you cut along the drawn lines and unfold the paper, you get an immaculate "
            "letter A with one vertical line of symmetry. Now examine the letter H. Letter H is doubly special because it has two "
            "independent lines of symmetry: one vertical line splitting the two tall upright bars, and one horizontal line splitting "
            "the middle crossbar. To cut letter H with maximum speed, fold the sheet in half vertically, and then fold it again horizontally "
            "into quarters. By cutting a simple notch into the open corners of this small 4-layer packet and unfolding, four identical "
            "quadrants emerge simultaneously. Multi-fold cutting proves how symmetry saves labor and guarantees flawless alignment."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Single Fold vs Double Fold Crafting</h3>
                <p>The number of symmetry axes determines how many times you can fold paper before cutting:</p>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <div class="p-2.5 rounded-lg bg-indigo-950/30 border border-indigo-800/40 font-mono">
                    <span class="text-cyan-300 font-bold block mb-1">Letter A (1 Vertical Axis):</span>
                    <p class="text-[11px] text-slate-300">• Fold once vertically (2 layers).<br>• Cut outer leg and half crossbar.<br>• Unfold to reveal 1 symmetrical letter A.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/30 border border-emerald-800/40 font-mono">
                    <span class="text-emerald-300 font-bold block mb-1">Letter H (2 Axes: V + H):</span>
                    <p class="text-[11px] text-slate-300">• Fold vertically, then horizontally (4 layers).<br>• Cut one small rectangular corner notch.<br>• Unfold to reveal a complete letter H!</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "How many lines of reflection symmetry does the capital letter A possess?",
                "options": [
                    "Exactly 1 vertical line of symmetry",
                    "Exactly 1 horizontal line of symmetry",
                    "2 lines of symmetry (both vertical and horizontal)",
                    "Zero lines of symmetry"
                ],
                "answer": 0,
                "explanation": "Letter A has only 1 vertical line of symmetry running from its top apex down through the center of its crossbar."
            },
            {
                "id": "cp2_2",
                "question": "Why can capital letter H be cut by folding paper into four layers (quarters)?",
                "options": [
                    "Because H has 2 perpendicular lines of symmetry (1 vertical and 1 horizontal)",
                    "Because H has 4 diagonal lines of symmetry",
                    "Because H is made of circles",
                    "Because four layers are always required for all alphabets"
                ],
                "answer": 0,
                "explanation": "Letter H possesses two lines of symmetry at right angles to each other, so each quadrant is identical and unfolds into the complete letter."
            }
        ]
    },

    {
        "id": 3,
        "title": "Letter Symmetry",
        "tagline": "Alphabet Classification • Vertical, Horizontal, Both, or No Symmetry Lines",
        "lecture": (
            "Not all letters in the alphabet share the same symmetrical properties. In mathematics, we classify uppercase letters "
            "into four distinct groups based on their lines of reflection symmetry. The first group contains letters with only a vertical "
            "line of symmetry. Examples include capital letters A, M, T, U, V, W, and Y. If you hold a mirror vertically beside half "
            "of letter M or T, the full letter appears unchanged. The second group contains letters with only a horizontal line of symmetry. "
            "Examples include B, C, D, E, and K. A horizontal mirror placed across their middle reflects the top half into the bottom half. "
            "The third group is especially fascinating: letters that have both vertical and horizontal lines of symmetry. These versatile "
            "letters are H, I, O, and X. They can be folded top-to-bottom as well as left-to-right. Finally, the fourth group includes "
            "asymmetrical letters like F, G, J, L, P, Q, R, and S, which have zero lines of reflection symmetry. Notice letter N: although "
            "it looks balanced, folding it vertically or horizontally never matches its slanted diagonal line! Testing letters with mirrors "
            "sharpens our spatial reasoning and visual accuracy across every geometric shape we study."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Symmetry Category</th>
                            <th class="p-1.5 border-b border-slate-700">Alphabet Examples</th>
                            <th class="p-1.5 border-b border-slate-700">Fold Orientation</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Vertical Line Only</td>
                            <td class="p-1.5 text-slate-200">A, M, T, U, V, W, Y</td>
                            <td class="p-1.5 text-slate-400">Left-to-right fold</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-cyan-300 font-bold">Horizontal Line Only</td>
                            <td class="p-1.5 text-slate-200">B, C, D, E, K</td>
                            <td class="p-1.5 text-slate-400">Top-to-bottom fold</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-emerald-400 font-bold">Both (V and H)</td>
                            <td class="p-1.5 text-slate-200">H, I, O, X</td>
                            <td class="p-1.5 text-slate-400">Quadrant fold (4 layers)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-rose-400 font-bold">No Symmetry Line</td>
                            <td class="p-1.5 text-slate-200">F, G, J, L, N, P, Q, R, S, Z</td>
                            <td class="p-1.5 text-slate-400">Cannot be folded to overlap</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="p-2 rounded bg-amber-950/30 border border-amber-800/40 text-[11px] text-amber-200">
                ⚠️ <strong>Common Trap:</strong> Letters like <strong>N</strong> and <strong>Z</strong> do <em>not</em> have reflection symmetry across vertical or horizontal lines, even though they look balanced!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "Which of the following letters has BOTH vertical and horizontal lines of symmetry?",
                "options": [
                    "Letter X",
                    "Letter M",
                    "Letter E",
                    "Letter P"
                ],
                "answer": 0,
                "explanation": "Letter X can be divided symmetrically by both a vertical mirror line and a horizontal mirror line."
            },
            {
                "id": "cp3_2",
                "question": "Does capital letter N possess a vertical line of reflection symmetry?",
                "options": [
                    "No, because folding left-to-right reverses the diagonal cross-stroke",
                    "Yes, it folds into a letter V",
                    "Yes, every letter has at least one line of symmetry",
                    "Only on odd days of the week"
                ],
                "answer": 0,
                "explanation": "Folding letter N vertically causes its diagonal stroke to point in the wrong direction, so it has no reflection line."
            }
        ]
    },

    {
        "id": 4,
        "title": "Decorative Cutouts",
        "tagline": "Festive Bilateral Art • Crafting Clay Diyas, Sailboats & Garland Chains",
        "lecture": (
            "Bilateral reflection symmetry is the guiding principle behind festive craftwork throughout India. During festival seasons, "
            "people fold sheets of metallic and colored glaze paper to cut out strings of traditional earthen oil lamps, called diyas, "
            "as well as sailing boats, blooming lotuses, and rangoli borders. To make a symmetrical diya cutout, fold a rectangular sheet "
            "of yellow or orange paper in half vertically. The folded edge becomes the central vertical symmetry axis. Using a pencil, "
            "sketch half of the curved bowl and half of the flickering flame along this creased fold. Carefully cut along your pencil line, "
            "keeping the fold intact. When you unfold the paper, a gorgeous, perfectly balanced diya appears. The left curve of the clay "
            "pot reflects the right curve, and the flame points straight up in serene alignment. If you do not keep the fold intact, the "
            "two halves separate into disconnected slivers! Similarly, folding paper like an accordion fan allows you to cut a half-motif "
            "that unfolds into a repeating garland of connected diyas holding hands. Geometry and traditional art merge seamlessly through symmetry, "
            "filling homes with vibrant festive harmony and demonstrating how simple mathematical balance creates captivating decorative beauty."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">The Anatomy of a Diya Cutout</h3>
                <p>Traditional Indian crafts use bilateral symmetry along a folded spine to generate iconic motifs:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 text-center font-mono">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-sm mb-1">1. Fold Paper</span>
                    <p class="text-[10px] text-slate-400">Crease down the vertical center line.</p>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block text-sm mb-1">2. Draw Half Diya</span>
                    <p class="text-[10px] text-slate-400">Spine must lie on the creased edge.</p>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-emerald-400 font-bold block text-sm mb-1">3. Unfold Art</span>
                    <p class="text-[10px] text-slate-300">Perfect bilateral balance revealed!</p>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                💡 <strong>Accordion Garland Trick:</strong> Folding paper back-and-forth into pleats before cutting allows the flame tips or base edges to remain connected, creating continuous strings of dancing diyas!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "Where must the central vertical axis of a diya sketch be aligned on the paper?",
                "options": [
                    "Directly along the folded creased spine",
                    "Along the open outer raw edges",
                    "Across the corner at 45 degrees",
                    "Anywhere away from the paper folds"
                ],
                "answer": 0,
                "explanation": "Drawing along the folded spine ensures both halves remain joined together upon unfolding, creating a single unified motif."
            },
            {
                "id": "cp4_2",
                "question": "What geometric property ensures the left and right halves of a cutout diya look identical?",
                "options": [
                    "Bilateral reflection symmetry across the vertical crease",
                    "Rotational symmetry of order 10",
                    "The color of the paper used",
                    "The thickness of the scissors blade"
                ],
                "answer": 0,
                "explanation": "Folding in half creates bilateral reflection symmetry across the central vertical crease line."
            }
        ]
    },

    {
        "id": 5,
        "title": "Windmill Craft",
        "tagline": "Paper Firki Engineering • Folding, Slitting & Pin-Mounted Spinning Blades",
        "lecture": (
            "Every child loves holding a colorful paper windmill, known locally in India as a firki, and watching it spin furiously "
            "in the breeze. Building a firki is a wonderful lesson in practical geometry. To make one, start with an exact square "
            "sheet of paper. Fold the square along both of its diagonal corners to find the exact central point where the two diagonal "
            "creases intersect. Using scissors, make four straight cuts from each corner along the diagonal fold lines, stopping halfway "
            "towards the center. Now you have eight triangular corners. Take every alternating corner tip—one from each triangular blade—and "
            "gently curve it inward towards the center point without making a sharp crease. Hold all four bent tips together at the central hub "
            "and push a small metal pin straight through them into an eraser or wooden stick. When the breeze blows against the curved pockets, "
            "the firki whirs into energetic motion. Notice that a firki does not have simple reflection symmetry because its blades all slant "
            "in the same rotational direction. Instead, it embodies a whole new kind of geometric wonder: rotational symmetry, where parts "
            "whirl in balanced cyclic harmony around a single fixed pivot."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Step-by-Step Firki Construction</h3>
                <p>Constructing a 4-blade paper windmill reveals the transition from square reflection to spinning dynamic balance:</p>
            </div>
            <div class="grid grid-cols-4 gap-1.5 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-xs">Step 1</span>
                    <span class="text-[10px] text-slate-400">Square sheet diagonal creasing</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block text-xs">Step 2</span>
                    <span class="text-[10px] text-slate-400">Cut 4 diagonals halfway to center</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-indigo-400 font-bold block text-xs">Step 3</span>
                    <span class="text-[10px] text-slate-400">Fold alternate tips to central hub</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/60 border border-emerald-800/40">
                    <span class="text-emerald-400 font-bold block text-xs">Step 4</span>
                    <span class="text-[10px] text-slate-300">Mount pin onto wooden stick</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                🌬️ <strong>Aerodynamic Principle:</strong> Alternate bending creates four uniform air pockets facing the same cyclic direction, causing incoming wind to spin the firki smoothly around its pin axis.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "What shape of paper sheet is required to make a standard 4-blade firki?",
                "options": [
                    "An exact square sheet of paper",
                    "A long thin triangular ribbon",
                    "An irregular oval cutout",
                    "A semicircle sheet"
                ],
                "answer": 0,
                "explanation": "A square sheet provides four equal sides and equal 90-degree diagonal sectors essential for uniform windmill blades."
            },
            {
                "id": "cp5_2",
                "question": "Why do the blades of a completed spinning firki lack bilateral reflection symmetry?",
                "options": [
                    "Because all four blades curve in the same rotational (clockwise or counter-clockwise) direction",
                    "Because the pin is made of metal",
                    "Because paper is too light to have symmetry",
                    "Because squares do not possess diagonal lines"
                ],
                "answer": 0,
                "explanation": "Bending alternate corners gives all blades a one-directional twist, breaking mirror symmetry but generating rotational symmetry."
            }
        ]
    },

    {
        "id": 6,
        "title": "Tracking Turns",
        "tagline": "Angular Fractions • Tracking 1/4 Turn (90°), 1/2 Turn (180°) & 3/4 Turn (270°)",
        "lecture": (
            "To understand how shapes move in rotational geometry, we track their positions through fractional turns. Imagine placing "
            "a bright red dot on the top blade of our 4-blade firki. When the firki stands upright in its starting position, we call this "
            "the zero turn. Now gently rotate the firki clockwise around its central pin. When the marked blade moves from the top position "
            "to the right horizontal position, the firki has completed a 1/4 turn, which equals a rotation of 90 degrees. Turn it further "
            "until the red dot points straight down: it has now completed a 1/2 turn, equivalent to 180 degrees or half of a full circle. "
            "Rotate it once more until the dot points to the left: that represents a 3/4 turn, or 270 degrees. Finally, rotating the marked "
            "blade back to its original top position completes a full turn of 360 degrees. At every 1/4 turn, notice something extraordinary: "
            "even though the red dot has moved to a new corner, the overall shape and outline of the firki looks completely identical to its "
            "starting view! Tracking the dot proves that motion occurred while the figure's visual silhouette remained invariant, showing "
            "how rotational repetition creates flawless geometric continuity."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="grid grid-cols-4 gap-2 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Starting Point</span>
                    <span class="text-amber-400 font-bold text-sm block">0° Turn</span>
                    <span class="text-[10px] text-slate-300">Dot at 12 o'clock</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">1/4 Turn</span>
                    <span class="text-cyan-400 font-bold text-sm block">90° Turn</span>
                    <span class="text-[10px] text-slate-300">Dot at 3 o'clock</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">1/2 Turn</span>
                    <span class="text-indigo-400 font-bold text-sm block">180° Turn</span>
                    <span class="text-[10px] text-slate-300">Dot at 6 o'clock</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">3/4 Turn</span>
                    <span class="text-emerald-400 font-bold text-sm block">270° Turn</span>
                    <span class="text-[10px] text-slate-300">Dot at 9 o'clock</span>
                </div>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-700 text-[11px] leading-relaxed">
                💡 <strong>The Tracking Dot Secret:</strong> Without the red dot, a person walking into the room cannot tell whether the 4-blade firki has turned by 90°, 180°, or 270°, because each blade perfectly replaces the next!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "How many degrees does a shape rotate through during a 1/4 turn?",
                "options": [
                    "90 degrees (one right angle)",
                    "180 degrees (straight line)",
                    "45 degrees (half right angle)",
                    "360 degrees (full circle)"
                ],
                "answer": 0,
                "explanation": "A full circle has 360 degrees. Therefore, 1/4 of 360 degrees is 360 ÷ 4 = 90 degrees."
            },
            {
                "id": "cp6_2",
                "question": "If a marked dot starts at the top (12 o'clock), where will it be located after a 1/2 turn clockwise?",
                "options": [
                    "At the bottom (6 o'clock position)",
                    "At the right (3 o'clock position)",
                    "Back at the top (12 o'clock position)",
                    "At the left (9 o'clock position)"
                ],
                "answer": 0,
                "explanation": "A 1/2 turn rotates through 180 degrees, carrying the top marker directly opposite to the bottom 6 o'clock position."
            }
        ]
    },

    {
        "id": 7,
        "title": "Rotational Symmetry",
        "tagline": "Concept Definition • Invariance Under Fixed Central Point Rotation",
        "lecture": (
            "We can now formally define one of the most elegant ideas in mathematics: rotational symmetry. A two-dimensional figure "
            "is said to possess rotational symmetry if, when rotated about its fixed central point by an angle less than 360 degrees, "
            "it fits exactly onto its own original outline and looks completely unchanged. Every single object looks identical to itself "
            "after a full 360-degree revolution, but that does not give it rotational symmetry! To possess true rotational symmetry, "
            "the figure must match its starting view at intermediate resting stages during the spin. For instance, consider an equilateral "
            "triangle. Rotating it by 1/3 of a turn, which is 120 degrees, or 2/3 of a turn, which is 240 degrees, makes it look completely "
            "identical to its initial appearance. A square fits onto itself at 1/4 turn, 1/2 turn, and 3/4 turn. The number of times a figure "
            "matches its starting silhouette during one complete 360-degree rotation is called its order of rotational symmetry. A firki "
            "has rotational symmetry of order 4, because it matches at 90 degrees, 180 degrees, 270 degrees, and 360 degrees. Recognizing this "
            "order helps architects, designers, and mathematicians analyze spinning wheels, turbine blades, and intricate ceramic tiles."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Formal Rule of Rotational Symmetry</h3>
                <p>A shape has <strong>rotational symmetry</strong> if rotating it about its center by an angle less than 360° yields an orientation indistinguishable from the starting shape.</p>
            </div>
            <div class="grid grid-cols-3 gap-2 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">Order 2 (1/2 Turn)</span>
                    <p class="text-[10px] text-slate-300">Matches at 180° and 360°.<br><em>Examples: Rectangle, Letter H, Letter S, Digit 8</em></p>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block mb-1">Order 3 (1/3 Turn)</span>
                    <p class="text-[10px] text-slate-300">Matches at 120°, 240°, 360°.<br><em>Examples: Equilateral triangle, 3-blade ceiling fan</em></p>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-emerald-400 font-bold block mb-1">Order 4 (1/4 Turn)</span>
                    <p class="text-[10px] text-slate-300">Matches at 90°, 180°, 270°, 360°.<br><em>Examples: Square, 4-blade firki, Plus sign (+)</em></p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "What is the order of rotational symmetry of a standard 4-blade paper firki?",
                "options": [
                    "Order 4 (matches at 1/4, 1/2, 3/4, and full turn)",
                    "Order 2 (matches only after a 1/2 turn)",
                    "Order 1 (matches only at full 360°)",
                    "Order 0 (it has no symmetry)"
                ],
                "answer": 0,
                "explanation": "A 4-blade firki coincides with its original outline 4 times during a full 360-degree rotation (every 90 degrees)."
            },
            {
                "id": "cp7_2",
                "question": "Does a scalene triangle with three unequal sides have rotational symmetry?",
                "options": [
                    "No, because it only looks the same after a full 360-degree turn",
                    "Yes, of order 3",
                    "Yes, of order 2",
                    "Yes, after a 1/4 turn"
                ],
                "answer": 0,
                "explanation": "Shapes that only look identical after a full 360-degree rotation are said to have no rotational symmetry (order 1 is trivial)."
            }
        ]
    },

    {
        "id": 8,
        "title": "Rotation vs Reflection",
        "tagline": "Comparing Invariances • Tracing Paper Overlays, Letter H vs Letter S",
        "lecture": (
            "A crucial milestone in geometry is distinguishing between reflection symmetry and rotational symmetry. They are fundamentally "
            "different transformations! Reflection symmetry involves flipping a shape over an axis, reversing its left and right orientation "
            "like a mirror. Rotational symmetry involves turning a shape smoothly around a central pivot without ever flipping it over. "
            "You can test this using transparent tracing paper. Place tracing paper over capital letter H, trace its outline, and stick a pin "
            "through its exact center. If you flip the tracing paper over, letter H matches (reflection symmetry). If you leave the paper flat "
            "and rotate it by a 1/2 turn (180 degrees), letter H also matches! Thus, letter H possesses both reflection and rotational symmetry. "
            "Now trace capital letter S or letter N. If you flip letter S over, it turns backwards and looks inverted—it fails the mirror test completely! "
            "However, if you pin letter S at its center and rotate the tracing paper by a 1/2 turn (180 degrees), the top loop and bottom loop swap "
            "places seamlessly. Letter S has rotational symmetry of order 2, despite having zero lines of reflection symmetry! Testing shapes with "
            "flips and turns reveals their unique geometric personalities."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Shape / Letter</th>
                            <th class="p-1.5 border-b border-slate-700">Reflection Symmetry?</th>
                            <th class="p-1.5 border-b border-slate-700">Rotational Symmetry?</th>
                            <th class="p-1.5 border-b border-slate-700">Distinctive Behavior</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Letter A</td>
                            <td class="p-1.5 text-emerald-400">Yes (1 Vertical line)</td>
                            <td class="p-1.5 text-rose-400">No (looks upside down at 180°)</td>
                            <td class="p-1.5 text-slate-400">Reflection only</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-cyan-300 font-bold">Letter S & N</td>
                            <td class="p-1.5 text-rose-400">No (zero mirror lines)</td>
                            <td class="p-1.5 text-emerald-400">Yes (Order 2 at 1/2 turn 180°)</td>
                            <td class="p-1.5 text-slate-400">Rotation only!</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-emerald-400 font-bold">Letter H, I, X, O</td>
                            <td class="p-1.5 text-emerald-400">Yes (2 lines: V & H)</td>
                            <td class="p-1.5 text-emerald-400">Yes (Order 2 at 1/2 turn 180°)</td>
                            <td class="p-1.5 text-slate-400">Both symmetries present</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-purple-400 font-bold">Firki (4-blade)</td>
                            <td class="p-1.5 text-rose-400">No (blades have cyclic tilt)</td>
                            <td class="p-1.5 text-emerald-400">Yes (Order 4: 90°, 180°, 270°)</td>
                            <td class="p-1.5 text-slate-400">Pure cyclic rotation</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="p-2 rounded bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-cyan-200">
                🔍 <strong>Key Rule:</strong> A shape does NOT need reflection symmetry to possess rotational symmetry (e.g., Letter S, Letter Z, Letter N, and the spinning Firki).
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "Which of the following letters has rotational symmetry of order 2, but NO line of reflection symmetry?",
                "options": [
                    "Capital Letter S",
                    "Capital Letter H",
                    "Capital Letter A",
                    "Capital Letter M"
                ],
                "answer": 0,
                "explanation": "Letter S looks identical after a 1/2 turn (180°), but cannot be folded along any line to match."
            },
            {
                "id": "cp8_2",
                "question": "What is the difference in action between testing reflection symmetry versus rotational symmetry?",
                "options": [
                    "Reflection involves flipping over an axis; rotation involves turning around a fixed central point",
                    "Reflection uses scissors while rotation uses glue",
                    "They are identical actions with different names",
                    "Rotation can only be done in complete darkness"
                ],
                "answer": 0,
                "explanation": "Reflection flips the orientation across a mirror line, while rotation pivots the plane around a central point without flipping."
            }
        ]
    }
]

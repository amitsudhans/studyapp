# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 7: Shapes and Patterns - Part 2 (Slides 9 to 16)
NEP 2020 / Joyful Mathematics
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Folding Kites",
        "tag": "Make Your Own Kite • Step-by-Step Origami Geometry",
        "lecture": (
            "Origami—the ancient Japanese art of paper folding—is pure tactile geometry! In our workshop, we fold an exact physical "
            "kite shape starting from a single square sheet of paper. Step one: take a square paper and fold it in half along one of "
            "its diagonal corners to form a sharp crease line. Unfold it: this diagonal serves as our central axis of symmetry. "
            "Step two: take the top-left edge of the square and fold it inward so that it lies perfectly flush along the diagonal crease. "
            "Step three: take the top-right edge and fold it symmetrically inward along the same diagonal crease. Press both folds firmly! "
            "Look at the shape you have created: it is an authentic mathematical kite! The two top folded edges are equal to each other, "
            "and the two bottom edges of the original square are equal to each other. The diagonal crease bisects the top vertex angle, "
            "and by placing a straight bamboo sliver along the horizontal corners, you see that the two diagonals meet at a strict "
            "90-degree right angle. Paper folding proves that complex geometric theorems are physically verifiable right in your hands."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Paper folding creates precise geometric forms through angle bisections and line reflections along a square's diagonal axis:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-2 flex items-center gap-2">
                            <span>📄</span> The Origami Folding Sequence
                        </h4>
                        <ol class="text-slate-300 space-y-2 list-decimal pl-4">
                            <li><strong>Start with a Square:</strong> 4 equal sides and 4 right angles (90°).</li>
                            <li><strong>Diagonal Crease:</strong> Fold diagonally corner-to-corner to form line of symmetry AC.</li>
                            <li><strong>Left Wing Fold:</strong> Fold top-left edge inward along diagonal AC.</li>
                            <li><strong>Right Wing Fold:</strong> Fold top-right edge symmetrically inward along diagonal AC.</li>
                            <li><strong>Result:</strong> A true geometric kite with 2 pairs of adjacent equal sides!</li>
                        </ol>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-2 flex items-center gap-2">
                            <span>📐</span> Geometric Verifications
                        </h4>
                        <ul class="text-slate-300 space-y-2">
                            <li>• <strong>Angle Bisection:</strong> The diagonal fold bisects the original 90° corner into two equal 45° angles.</li>
                            <li>• <strong>Congruent Triangles:</strong> The kite consists of two mirror-image right-angled triangles folded across the diagonal.</li>
                            <li>• <strong>Perpendicular Struts:</strong> Attaching horizontal bamboo cross-struts forms the 90° diagonal intersection.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>Origami Axiom:</strong> Folding a straight edge onto another creates an exact angle bisector without using a protractor!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_9",
        "checkpoints": [
            {
                "question": "What is the initial fold made on a square paper to construct an origami kite?",
                "options": [
                    "Fold along the diagonal corner-to-corner",
                    "Fold horizontally across the middle",
                    "Fold in four equal squares",
                    "Cut off the corners"
                ],
                "correct": 0,
                "explanation": "Folding diagonally corner-to-corner establishes the central axis of symmetry for the kite wings."
            },
            {
                "question": "When both top edges are folded along the diagonal crease, what property is guaranteed?",
                "options": [
                    "The two top folded edges are equal in length",
                    "All four sides become equal",
                    "The shape becomes a circle",
                    "The diagonals become curved"
                ],
                "correct": 0,
                "explanation": "Because the folds are symmetric reflections along the diagonal, the two top folded edges are identical in length."
            }
        ]
    },
    {
        "id": 10,
        "title": "Circle Geometry",
        "tag": "Play with Circles • Compass Construction & Inscribed Quadrilaterals",
        "lecture": (
            "A circle is the most symmetrical curve in the universe: every point on its boundary lies at the exact same distance from "
            "a central fixed point! Using a pencil compass, we anchor the metal needle at the centre O and sweep the pencil around to "
            "trace the circumference. The fixed distance between the needle and pencil is the radius. A straight line passing through "
            "the centre from one edge of the circle to the opposite edge is a diameter. Every diameter equals exactly twice the radius, "
            "and all diameters of a circle are equal in length. Now let us conduct a fascinating geometric experiment: draw two diameters "
            "inside a circle and connect their four endpoints with straight lines to form an inscribed quadrilateral. What shape emerges? "
            "If the two diameters cross at an arbitrary angle, connecting their four endpoints produces a rectangle! Why? Because the "
            "two diameters are equal in length and bisect each other at the circle's centre. But if you make the two diameters intersect "
            "at exactly 90 degrees—perpendicular to each other—connecting their endpoints produces a perfect square! Circles generate "
            "the most fundamental quadrilaterals of geometry."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Diameters inscribed in a circle act as diagonals of geometric quadrilaterals whose vertices lie on the circumference:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-2 flex items-center gap-2">
                            <span>⭕</span> Core Circle Metrics
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Centre (O):</strong> The unique point equidistant from all points on the circumference.</li>
                            <li>• <strong>Radius (r):</strong> Distance from centre to any boundary point.</li>
                            <li>• <strong>Diameter (d):</strong> Longest straight line passing through the centre: <strong class="text-cyan-300">d = 2r</strong>.</li>
                            <li>• <strong>Chord:</strong> Any line segment connecting two points on the circle.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>🟩</span> Inscribed Quadrilateral Theorem
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Case 1 (Non-Perpendicular Diameters):</strong> Any two diameters have equal length (d₁ = d₂) and bisect at O. Connecting endpoints yields a <strong class="text-amber-300">Rectangle</strong>!</li>
                            <li>• <strong>Case 2 (Perpendicular Diameters at 90°):</strong> The two equal diameters cross at 90°. Connecting endpoints yields a <strong class="text-emerald-300">Square</strong>!</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-cyan-950/40 border border-cyan-500/30 rounded-lg text-xs text-cyan-200">
                    <strong>Thales' Theorem:</strong> Any angle inscribed in a semicircle is a right angle (90°). Because diagonals are diameters, all 4 corner angles must be 90°!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_10",
        "checkpoints": [
            {
                "question": "If the radius of a circle drawn with a compass is 4.5 cm, what is the length of its diameter?",
                "options": ["9 cm", "4.5 cm", "18 cm", "13.5 cm"],
                "correct": 0,
                "explanation": "Diameter = 2 × radius = 2 × 4.5 cm = 9 cm."
            },
            {
                "question": "When two diameters of a circle intersect at a 90° right angle, connecting their four endpoints always produces which shape?",
                "options": ["A square", "A parallelogram", "A kite", "A scalene triangle"],
                "correct": 0,
                "explanation": "Because the diagonals are equal, bisect each other, and cross at 90°, the inscribed shape is a square."
            }
        ]
    },
    {
        "id": 11,
        "title": "Circle Art",
        "tag": "Circle Designs • String Art & Modular Chord Patterns",
        "lecture": (
            "Circles are not just mechanical tools—they are canvases for stunning geometric art! In our circle design studio, we divide "
            "the circumference of a circle into 24 equally spaced points, numbered sequentially from 1 to 24 like a giant clockface. "
            "By connecting these points using straight rule chords, breathtaking curved illusions and star polygons come alive. "
            "This technique is called string art or curve stitching. For example, if we use a constant jump rule—connecting point n "
            "to point n plus 5 (so point 1 connects to 6, point 6 connects to 11, point 11 to 16, and so on)—a beautiful 24-pointed "
            "geometric star emerges! If we use a multiplication modulo rule—connecting point n to two times n (so point 1 to 2, 2 to 4, "
            "3 to 6, 4 to 8)—the straight lines envelop a delicate heart-shaped curve called a cardioid! Straight lines, when drawn "
            "following systematic mathematical rules across a circle, create the optical illusion of smooth organic curves."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    String art and envelope geometry connect numbered points on a circle using straight chord segments to generate radiant star polygons and caustic curves:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-violet-500/30">
                        <h4 class="font-bold text-violet-400 mb-2 flex items-center gap-2">
                            <span>⭐</span> Constant Step Jump Rule (n ➔ n + k)
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• 24 points spaced evenly by 360° ÷ 24 = 15° each.</li>
                            <li>• <strong>Step 5:</strong> 1 ➔ 6 ➔ 11 ➔ 16 ➔ 21 ➔ 2 ... produces a sharp 24-pointed woven star.</li>
                            <li>• <strong>Step 7:</strong> Connects points with longer chords, creating an inner circular ring boundary.</li>
                            <li>• If step k and 24 share no common factors (coprime), the string visits all 24 points in a single unbroken loop!</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-2">
                            <span>💖</span> Modular Multiplication (n ➔ 2n (mod 24))
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• Point 1 connects to 2; Point 2 to 4; Point 3 to 6; Point 4 to 8.</li>
                            <li>• Point 12 connects to 24; Point 13 connects to 26 = 2.</li>
                            <li>• <strong>Enveloping Caustic:</strong> The dense lines form a curved optical envelope known as a <strong>Cardioid</strong>!</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-violet-950/40 border border-violet-500/30 rounded-lg text-xs text-violet-200">
                    <strong>Envelope Geometry:</strong> Pure straight chords tangents to an invisible curved caustic boundary, proving how straight-line mathematics creates curved artistic beauty.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_11",
        "checkpoints": [
            {
                "question": "On a circle divided into 24 points, what is the angle between each consecutive numbered point?",
                "options": ["15°", "24°", "10°", "30°"],
                "correct": 0,
                "explanation": "360° ÷ 24 points = 15° between each adjacent point."
            },
            {
                "question": "Starting at point 1 on a 24-point circle with a step jump of 7, which point is connected next?",
                "options": ["Point 8", "Point 7", "Point 14", "Point 9"],
                "correct": 0,
                "explanation": "1 + 7 = Point 8."
            }
        ]
    },
    {
        "id": 12,
        "title": "Cube Nets",
        "tag": "Spatial Reasoning • 11 Hexomino Nets & 3-D Cube Folding",
        "lecture": (
            "Step into the three-dimensional world! A solid cube has six square faces, twelve straight edges, and eight corner vertices. "
            "If we take scissors and cut along seven edges of a hollow cardboard cube, it unrolls flat onto a table. This two-dimensional "
            "unfolded pattern is called a net! How many distinct ways can six connected squares fold up into a closed cube? In mathematics, "
            "there are exactly eleven unique cube nets—no more, no less! Not every arrangement of six squares works. For example, six "
            "squares in a single straight row of six will wrap around four sides, leaving two overlapping on the top while leaving the "
            "bottom gaping open! A four-in-a-row arrangement with one flap on top and one flap on the bottom—known as a T-net or "
            "cross-net—folds into a perfect cube. In a folded cube, opposite faces never touch each other; in a net, opposite faces are "
            "always separated by exactly one intervening square. Testing nets develops powerful spatial 3D mental rotation."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    A cube net is a flat arrangement of six connected squares that can be folded along its edges to construct a hollow 3-D cube:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>📦</span> Cube Metrics & Net Rules
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Faces:</strong> 6 identical congruent squares.</li>
                            <li>• <strong>Edges:</strong> 12 straight equal line segments.</li>
                            <li>• <strong>Vertices:</strong> 8 corner points where 3 faces meet.</li>
                            <li>• <strong>Exactly 11 Distinct Nets:</strong> Only 11 hexomino patterns can fold into a closed cube.</li>
                            <li>• <strong>Opposite Face Rule:</strong> In any linear strip of a net, opposite faces are separated by exactly 1 square.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-2">
                            <span>❌</span> Illegal Net Configurations
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>6 in a line:</strong> Fails (faces overlap, leaving ends open).</li>
                            <li>• <strong>2×2 block of 4 squares:</strong> Fails (cannot fold closed).</li>
                            <li>• <strong>Corner clusters:</strong> If 4 squares meet at a single vertex point, they cannot fold without colliding.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Standard Die Invariant:</strong> On standard gaming dice, numbers on opposite faces always sum to 7: 1 opposite 6, 2 opposite 5, and 3 opposite 4!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_12",
        "checkpoints": [
            {
                "question": "How many total distinct unfolded nets can form a closed cube?",
                "options": ["11 nets", "6 nets", "14 nets", "8 nets"],
                "correct": 0,
                "explanation": "Mathematicians have proven there are exactly 11 valid hexomino nets that fold into a closed cube."
            },
            {
                "question": "On a standard die net, if the top face is 3, what number must be on the opposite bottom face?",
                "options": ["4", "5", "6", "2"],
                "correct": 0,
                "explanation": "Opposite faces on a die sum to 7. 7 - 3 = 4."
            }
        ]
    },
    {
        "id": 13,
        "title": "Painted Cubes",
        "tag": "Cube Connections • 3×3×3 Dissection & Painted Face Counting",
        "lecture": (
            "Here is one of the most famous spatial reasoning challenges in all of school mathematics: The Painted Cube Puzzle! "
            "Imagine a solid wooden cube measuring 3 centimetres by 3 centimetres by 3 centimetres. We dip this entire cube into a vat "
            "of bright red paint so that all six exterior faces are painted red. Once the paint dries, a carpenter cuts the cube with "
            "saws into tiny 1-centimetre solid cubes. How many small cubes are formed? 3 times 3 times 3 equals 27 small cubes in total. "
            "Now examine the paint on these 27 small cubes! The 8 cubes located at the outer corners have three faces painted red. "
            "The cubes located along the edges, between the corners, have two faces painted red: each of the 12 edges has one such cube, "
            "giving 12 cubes with two painted faces. The cubes located in the exact centre of each of the 6 faces have only one face "
            "painted red, giving 6 cubes with one painted face. And in the very dark, hidden heart of the large cube sits exactly one "
            "inner cube that received zero paint at all! 8 plus 12 plus 6 plus 1 equals exactly 27 cubes."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Analyzing a 3 × 3 × 3 painted cube dissection categorizes the 27 unit cubes by their spatial coordinates and exterior exposures:
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left bg-slate-800/80 rounded-xl border border-slate-700">
                        <thead class="bg-slate-700/60 text-emerald-300">
                            <tr>
                                <th class="p-2.5">Cube Category</th>
                                <th class="p-2.5">Spatial Location</th>
                                <th class="p-2.5">Painted Faces</th>
                                <th class="p-2.5">Formula (n=3)</th>
                                <th class="p-2.5">Count</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700/60 text-slate-200 font-mono">
                            <tr>
                                <td class="p-2 font-bold text-rose-400">Corners</td>
                                <td class="p-2">8 exterior corners</td>
                                <td class="p-2 text-amber-300 font-bold">3 faces</td>
                                <td class="p-2">Fixed (always 8)</td>
                                <td class="p-2 font-bold text-white">8</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-cyan-400">Edge Middles</td>
                                <td class="p-2">Centres of 12 edges</td>
                                <td class="p-2 text-amber-300 font-bold">2 faces</td>
                                <td class="p-2">12 × (n - 2)</td>
                                <td class="p-2 font-bold text-white">12</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-indigo-400">Face Centres</td>
                                <td class="p-2">Centres of 6 faces</td>
                                <td class="p-2 text-amber-300 font-bold">1 face</td>
                                <td class="p-2">6 × (n - 2)²</td>
                                <td class="p-2 font-bold text-white">6</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-slate-400">Central Core</td>
                                <td class="p-2">Interior hidden center</td>
                                <td class="p-2 text-slate-500 font-bold">0 faces</td>
                                <td class="p-2">(n - 2)³</td>
                                <td class="p-2 font-bold text-white">1</td>
                            </tr>
                            <tr class="bg-slate-900/60 font-bold">
                                <td class="p-2 text-emerald-400" colspan="4">Total Small Cubes (n³)</td>
                                <td class="p-2 text-emerald-400 text-sm">27</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Sum Verification:</strong> 8{ (corners)} + 12{ (edges)} + 6{ (faces)} + 1{ (core)} = 27{ small cubes} (3 × 3 × 3 = 27).
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_13",
        "checkpoints": [
            {
                "question": "In a 3×3×3 painted cube, how many small cubes have exactly 3 faces painted?",
                "options": ["8 cubes (the corners)", "12 cubes", "6 cubes", "1 cube"],
                "correct": 0,
                "explanation": "Only the 8 corner cubes have 3 exposed exterior faces painted."
            },
            {
                "question": "How many small cubes in a 3×3×3 painted cube have ZERO painted faces?",
                "options": ["1 cube (the inner core)", "0 cubes", "8 cubes", "6 cubes"],
                "correct": 0,
                "explanation": "There is exactly 1 cube buried completely inside the centre: (3 - 2)³ = 1³ = 1 cube."
            }
        ]
    },
    {
        "id": 14,
        "title": "Shape Puzzles",
        "tag": "Linear Clue Puzzles • Positional Geometry & Deductive Ordering",
        "lecture": (
            "Mathematics exercises our deductive powers through positional logic puzzles. Picture a row of five pedestals numbered "
            "one through five from left to right. Five geometric shapes—a Circle, a Square, a Triangle, a Hexagon, and a Rectangle—must "
            "be placed on these pedestals following a set of strict clues. Clue one: 'The Circle is located somewhere to the left of "
            "the Triangle.' Clue two: 'The Hexagon sits at the exact centre on pedestal three.' Clue three: 'The Square is immediately "
            "between the Triangle and the Rectangle.' Clue four: 'The Triangle is not at an outer edge.' Let us deduce step by step! "
            "Pedestal three is locked: it must be the Hexagon. Since the Triangle is not at an outer edge, it cannot be on pedestal five; "
            "and since the Square sits between the Triangle and the Rectangle, pedestals two, three, and four or pedestals four, five "
            "must be examined. Because the Hexagon is on three, the block of Triangle, Square, and Rectangle must occupy pedestals "
            "two, four, and five or similar. By testing clues systematically, every shape locks into its unique pedestal position."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Positional logic puzzles combine spatial orientation, relational constraints, and elimination to determine unique linear arrangements:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>🔍</span> The Puzzle Clues
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>5 Pedestals:</strong> Position 1 (Left) to Position 5 (Right).</li>
                            <li>• <strong>Clue 1 (Anchor):</strong> The <strong>Hexagon</strong> is on Position 3 (Exact Centre).</li>
                            <li>• <strong>Clue 2 (Adjacency):</strong> The <strong>Square</strong> is directly between <strong>Triangle</strong> and <strong>Rectangle</strong>.</li>
                            <li>• <strong>Clue 3 (Order):</strong> The <strong>Circle</strong> is on the far left (Position 1).</li>
                            <li>• <strong>Clue 4 (Non-Edge):</strong> The <strong>Triangle</strong> is not on Position 5.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-2 flex items-center gap-2">
                            <span>💡</span> Step-by-Step Solution
                        </h4>
                        <ol class="text-slate-300 space-y-1.5 list-decimal pl-4">
                            <li>Position 1 = <strong>Circle</strong> (Clue 3).</li>
                            <li>Position 3 = <strong>Hexagon</strong> (Clue 1).</li>
                            <li>Position 2 = <strong>Triangle</strong> (Clue 4).</li>
                            <li>Positions 4 and 5: Square is between Triangle (Pos 2) and Rectangle (Pos 5) with Hexagon on 3.</li>
                            <li>Therefore, the unique valid line is: <strong>Circle, Triangle, Hexagon, Square, Rectangle</strong>!</li>
                        </ol>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Elimination Principle:</strong> Anchor absolute positions first, then test contiguous blocks to eliminate impossible permutations.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_14",
        "checkpoints": [
            {
                "question": "If the Hexagon is at the exact centre of 5 positions, what is its position number?",
                "options": ["Position 3", "Position 2", "Position 4", "Position 1"],
                "correct": 0,
                "explanation": "In 5 positions (1, 2, 3, 4, 5), the exact centre is Position 3."
            },
            {
                "question": "In the deduction above, which shape sits at Position 1 on the far left?",
                "options": ["Circle", "Square", "Hexagon", "Triangle"],
                "correct": 0,
                "explanation": "Clue 3 directly anchors the Circle at Position 1 on the far left."
            }
        ]
    },
    {
        "id": 15,
        "title": "Platonic Solids",
        "tag": "Icosahedron & Dodecahedron • Regular Polyhedra & Euler's Formula",
        "lecture": (
            "We now encounter the most majestic geometric solids in three dimensions: the Platonic Solids! A Platonic solid is a "
            "regular polyhedron where every face is an identical regular polygon, and the exact same number of faces meet at every single "
            "vertex. In our textbook cutouts, we construct two magnificent Platonic solids: the icosahedron and the dodecahedron. Look "
            "first at the icosahedron: its name comes from the Greek word 'icosa', meaning twenty! It has twenty equilateral triangular "
            "faces, twelve vertices, and thirty edges. Five triangles meet at each vertex. Next, look at the dodecahedron: 'dodeca' means "
            "twelve! It has twelve regular pentagonal faces, twenty vertices, and thirty edges. Three pentagons meet at each vertex. "
            "Now look at the edges of both solids: thirty edges each! The great mathematician Leonhard Euler discovered a universal "
            "law for all convex polyhedra: Vertices minus Edges plus Faces always equals 2! For the icosahedron: 12 minus 30 plus 20 "
            "equals 2. For the dodecahedron: 20 minus 30 plus 12 equals 2! Euler's formula binds all polyhedra together."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The five Platonic solids are the only convex polyhedra with identical regular polygon faces meeting at identical vertices:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-mono">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 font-sans flex items-center gap-1.5">
                            <span>🔷</span> Icosahedron (20 Faces)
                        </h4>
                        <div class="space-y-1 bg-slate-900/60 p-3 rounded-lg text-slate-200">
                            <p>• Faces (F): <span class="text-emerald-400 font-bold">20</span> (Equilateral Triangles)</p>
                            <p>• Vertices (V): <span class="text-cyan-400 font-bold">12</span> (5 triangles at each)</p>
                            <p>• Edges (E): <span class="text-amber-400 font-bold">30</span></p>
                            <p class="pt-1 border-t border-slate-700 font-sans text-[11px] text-slate-300">Euler Check: V - E + F = 12 - 30 + 20 = 2 ✓</p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-2 font-sans flex items-center gap-1.5">
                            <span>⬟</span> Dodecahedron (12 Faces)
                        </h4>
                        <div class="space-y-1 bg-slate-900/60 p-3 rounded-lg text-slate-200">
                            <p>• Faces (F): <span class="text-emerald-400 font-bold">12</span> (Regular Pentagons)</p>
                            <p>• Vertices (V): <span class="text-cyan-400 font-bold">20</span> (3 pentagons at each)</p>
                            <p>• Edges (E): <span class="text-amber-400 font-bold">30</span></p>
                            <p class="pt-1 border-t border-slate-700 font-sans text-[11px] text-slate-300">Euler Check: V - E + F = 20 - 30 + 12 = 2 ✓</p>
                        </div>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Dual Polyhedra:</strong> The icosahedron and dodecahedron are geometric duals: swapping the centers of the icosahedron's 20 faces produces the 20 vertices of the dodecahedron!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_15",
        "checkpoints": [
            {
                "question": "What is the shape of each of the 20 faces of an icosahedron?",
                "options": ["Equilateral triangle", "Regular pentagon", "Square", "Hexagon"],
                "correct": 0,
                "explanation": "An icosahedron has 20 congruent equilateral triangular faces."
            },
            {
                "question": "According to Euler's formula V - E + F = 2, if a polyhedron has 12 vertices and 20 faces, how many edges must it have?",
                "options": ["30 edges", "32 edges", "28 edges", "24 edges"],
                "correct": 0,
                "explanation": "V - E + F = 2 implies 12 - E + 20 = 2, so 32 - E = 2, which gives E = 30 edges."
            }
        ]
    },
    {
        "id": 16,
        "title": "Skeletal Frames",
        "tag": "Straw and Clay Models • Structural Rigidity & 3D Engineering",
        "lecture": (
            "We culminate our study by stepping into the boots of structural engineers! Using simple paper straws or bamboo sticks "
            "for edges, and small balls of modeling clay or play dough for vertices, we construct 3D skeletal frames of polyhedra. "
            "Build a square frame with four straws and four clay balls. Hold it up and push gently on two opposite corners: the square "
            "distorts easily into a slanted rhombus! It wobbles and collapses because a four-sided quadrilateral frame is mechanically "
            "unstable. Now insert a fifth diagonal straw across the square, dividing it into two triangles. Push again: the frame is "
            "now rock-solid and rigid! A triangle is the only polygon whose shape cannot be deformed without bending or breaking its "
            "edges. This is why construction cranes, railway bridges, electricity pylons, and geodesic domes are all built out of "
            "triangular trusses. By building cubes, tetrahedrons, and pyramids with straws and clay, we discover that mathematics is "
            "the invisible foundation supporting the bridges, buildings, and skyscrapers of our modern world."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Constructing skeletal models with straws (edges) and clay balls (vertices) reveals the principles of 3-D structural rigidity:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
                        <h4 class="font-bold text-teal-400 mb-2 flex items-center gap-2">
                            <span>🏗️</span> Triangulation & Rigidity
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Square Frame (Wobbly):</strong> 4 straws + 4 clay balls deform into a rhombus under lateral shear force.</li>
                            <li>• <strong>Diagonal Bracing:</strong> Adding 1 diagonal straw locks the angles completely, creating two rigid triangles.</li>
                            <li>• <strong>Engineering Reality:</strong> High-voltage towers, roof trusses, and Ferris wheels rely on triangular bracing.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>📦</span> Polyhedral Skeletal Recipes
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Cube:</strong> 12 straws (equal length) + 8 clay balls.</li>
                            <li>• <strong>Square Pyramid:</strong> 8 straws (4 base + 4 slant) + 5 clay balls.</li>
                            <li>• <strong>Tetrahedron:</strong> 6 straws + 4 clay balls (inherently rigid!).</li>
                            <li>• <strong>Octahedron:</strong> 12 straws + 6 clay balls.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Rigidity Principle:</strong> A triangle is rigid because its three side lengths uniquely fix all three interior angles. No angle can change without altering the side lengths!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_16",
        "checkpoints": [
            {
                "question": "How many clay balls (vertices) and straws (edges) are needed to build a skeletal cube?",
                "options": [
                    "8 clay balls and 12 straws",
                    "6 clay balls and 12 straws",
                    "8 clay balls and 6 straws",
                    "12 clay balls and 8 straws"
                ],
                "correct": 0,
                "explanation": "A cube has 8 vertices (clay balls) and 12 edges (straws)."
            },
            {
                "question": "Why are bridge trusses and construction cranes built out of triangular frames rather than square frames?",
                "options": [
                    "Because triangles are structurally rigid and cannot deform without changing edge lengths",
                    "Because triangles look prettier",
                    "Because squares use fewer straws",
                    "Because triangles have four sides"
                ],
                "correct": 0,
                "explanation": "Triangles are inherently rigid; unlike squares, their angles cannot shift or collapse under external load."
            }
        ]
    }
]

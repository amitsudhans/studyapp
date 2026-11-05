# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 7: Shapes and Patterns - Part 1 (Slides 1 to 8)
NEP 2020 / Joyful Mathematics
"""

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Weaving Mats",
        "tag": "Paper Weaving • Row Instructions & Grid Patterns",
        "lecture": (
            "Welcome to our geometry and pattern studio! We begin our exploration with the ancient art of weaving, which connects "
            "mathematical periodicity to everyday craft. To make a paper weaving mat, we take a sheet of colored paper, fold it in "
            "half, and make parallel slits from the fold line to within one centimetre of the outer edge. This slit sheet serves as "
            "the warp, or the fixed vertical base. Next, we cut bright contrasting paper strips to act as the weft, or the horizontal "
            "weaving threads. Weaving proceeds row by row following clear algorithmic rules. A classic plain weave uses the rule: "
            "one over, one under, repeated across the row. In the second row, we must invert the rule: one under, one over! Why must "
            "we invert the sequence? If we do not invert it, the horizontal strip simply slides out because it lacks interlacing tension! "
            "By altering the numerical rules, such as two over, one under, or three over, two under, intricate geometric chevron and "
            "diamond patterns emerge on grid paper. Notice how mathematical parity—alternating between odd and even positions—creates "
            "both structural strength and aesthetic symmetry."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Paper weaving combines spatial geometry, sequence algorithms, and structural tension through interlacing vertical slits (warp) and horizontal strips (weft).
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>📐</span> The Weaving Algorithm
                        </h4>
                        <ul class="text-xs space-y-2 text-slate-300">
                            <li>• <strong>Warp (Vertical Base):</strong> Folded paper with parallel cuts forming fixed vertical bands.</li>
                            <li>• <strong>Weft (Horizontal Strips):</strong> Movable colored strips woven horizontally through the warp.</li>
                            <li>• <strong>Standard Alternating Weave:</strong>
                                <ul class="pl-4 mt-1 space-y-1 font-mono text-[11px] text-amber-300">
                                    <li>Row 1: 1 Over, 1 Under, 1 Over, 1 Under...</li>
                                    <li>Row 2: 1 Under, 1 Over, 1 Under, 1 Over...</li>
                                    <li>Row 3: 1 Over, 1 Under, 1 Over, 1 Under...</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-2 flex items-center gap-2">
                            <span>🎨</span> Advanced Pattern Rules
                        </h4>
                        <ul class="text-xs space-y-2 text-slate-300">
                            <li>• <strong>Twill Weave (2 Over, 1 Under):</strong> Shifting the starting point by 1 unit each row produces diagonal staircases and herringbone textures.</li>
                            <li>• <strong>Basket Weave (2 Over, 2 Under):</strong> Creates bold checkerboard blocks of paired colors.</li>
                            <li>• <strong>Structural Principle:</strong> Interlacing locks paper fibers perpendicularly, preventing the mat from unravelling.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Binary Matrix Insight:</strong> A woven mat can be represented as a mathematical grid of 1s (strip over) and 0s (strip under), where alternating rows satisfy the parity rule <em>Cell(r, c) = (r + c) mod 2</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_1",
        "checkpoints": [
            {
                "question": "In a standard alternating weave, if Row 1 follows '1 over, 1 under', what must Row 2 follow to lock the paper strips?",
                "options": [
                    "1 under, 1 over",
                    "1 over, 1 under (same as Row 1)",
                    "2 over, 2 under",
                    "All over"
                ],
                "correct": 0,
                "explanation": "Row 2 must invert the sequence to '1 under, 1 over' so the strip is held firmly by the alternating warp bands."
            },
            {
                "question": "On a grid of 8 columns, how many 'over' positions are there in a row following '1 over, 1 under'?",
                "options": ["4 over positions", "8 over positions", "2 over positions", "6 over positions"],
                "correct": 0,
                "explanation": "With 8 columns alternating 1 over and 1 under, exactly half (8 ÷ 2 = 4) are over positions."
            }
        ]
    },
    {
        "id": 2,
        "title": "Plane Tessellations",
        "tag": "Tiling & Tessellation • Covering Surfaces Without Gaps or Overlaps",
        "lecture": (
            "Look down at tiled floors in train stations, verandas, and historic monuments: identical tiles cover the entire surface "
            "completely without leaving any gaps or overlapping one another! In mathematics, covering an infinite two-dimensional "
            "plane with repeating shapes is called a tessellation, or tiling. Why do certain geometric shapes tile seamlessly while "
            "others fail? The secret lies in vertex angles! When tiles meet around a single vertex point, their interior angles must "
            "add up to exactly 360 degrees, completing a full circle. Consider a square: each corner has a right angle of 90 degrees. "
            "When four squares meet at a vertex, four times 90 equals exactly 360 degrees! The tiles fit flush without leaving any space. "
            "Now consider an equilateral triangle: each corner is 60 degrees. Six triangles meeting at a point give six times 60, which "
            "equals 360 degrees! Now look at a regular hexagon: each corner is 120 degrees. Three hexagons meeting at a vertex give "
            "three times 120, which equals 360 degrees! This is why honeybees build hexagonal honeycombs: hexagons tile the plane "
            "with the least boundary wax, proving the power of geometric efficiency."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    A tessellation is a pattern formed by repeating figures that completely covers a plane with no gaps and no overlapping regions.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-1.5 flex items-center gap-1.5">
                            <span>🟦</span> Square Tiling
                        </h4>
                        <p class="text-slate-300">• Corner Angle: <strong>90°</strong></p>
                        <p class="text-slate-300">• Tiles per Vertex: <strong>4</strong></p>
                        <p class="font-mono text-emerald-300 font-bold">• 4 × 90° = 360° ✓</p>
                        <p class="text-slate-400 text-[11px] mt-1">Found in graph paper, floor tiles, and chessboards.</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-1.5 flex items-center gap-1.5">
                            <span>🔺</span> Triangular Tiling
                        </h4>
                        <p class="text-slate-300">• Corner Angle: <strong>60°</strong></p>
                        <p class="text-slate-300">• Tiles per Vertex: <strong>6</strong></p>
                        <p class="font-mono text-cyan-300 font-bold">• 6 × 60° = 360° ✓</p>
                        <p class="text-slate-400 text-[11px] mt-1">Forms rigid isometric grids and bridge trusses.</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-1.5 flex items-center gap-1.5">
                            <span>⬡</span> Hexagonal Tiling
                        </h4>
                        <p class="text-slate-300">• Corner Angle: <strong>120°</strong></p>
                        <p class="text-slate-300">• Tiles per Vertex: <strong>3</strong></p>
                        <p class="font-mono text-amber-300 font-bold">• 3 × 120° = 360° ✓</p>
                        <p class="text-slate-400 text-[11px] mt-1">Nature's choice for beehive honeycombs and basalt columns.</p>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>The 360° Vertex Invariant:</strong> Only shapes whose interior angles evenly divide 360° can form monohedral regular tessellations of the plane!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_2",
        "checkpoints": [
            {
                "question": "Why do regular hexagons tile a flat plane without gaps?",
                "options": [
                    "Because three 120° angles meet at a vertex: 3 × 120° = 360°",
                    "Because they have 6 sides",
                    "Because they are shaped like circles",
                    "Because 6 × 90° = 540°"
                ],
                "correct": 0,
                "explanation": "A regular hexagon has interior angles of 120°. Exactly 3 hexagons meet around a point: 3 × 120° = 360°, completely filling the vertex."
            },
            {
                "question": "How many equilateral triangles must meet at a vertex to tessellate the plane?",
                "options": ["6 triangles", "4 triangles", "5 triangles", "3 triangles"],
                "correct": 0,
                "explanation": "Each angle of an equilateral triangle is 60°. Since 360° ÷ 60° = 6, exactly 6 triangles meet at each vertex."
            }
        ]
    },
    {
        "id": 3,
        "title": "Polygon Tiling",
        "tag": "Exploring Shapes • Why Pentagons Fail & Multi-Shape Tilings",
        "lecture": (
            "What happens if we attempt to tile a floor using regular pentagons, which have five equal sides? Let us do the mathematics. "
            "In a regular pentagon, each interior corner angle measures 108 degrees. If we place three regular pentagons around a vertex, "
            "three times 108 equals 324 degrees. That leaves an unfilled gap of 360 minus 324, which is 36 degrees! But a fourth pentagon "
            "needs 108 degrees, which is far too wide, causing it to overlap! Because 108 does not divide 360 evenly, regular pentagons "
            "can never tile the plane alone! Now test regular octagons, which have eight sides. Each interior corner of an octagon is "
            "135 degrees. Two octagons meeting at a point occupy two times 135 equals 270 degrees. To reach 360 degrees, we need an angle "
            "of 360 minus 270, which is exactly 90 degrees! What shape has 90-degree corners? A square! By pairing octagons with small "
            "squares, we create a magnificent semi-regular tessellation. We can also combine triangles, squares, and rhombuses to "
            "design intricate multi-shape tiling pavements."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Shapes whose interior angles do not evenly divide 360° cannot tile alone, but can form hybrid tessellations when paired with matching partner shapes.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-2">
                            <span>❌</span> Why Regular Pentagons Fail
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• Interior angle of regular pentagon = <strong>108°</strong>.</li>
                            <li>• 3 pentagons at a vertex: 3 × 108° = <strong>324°</strong>.</li>
                            <li>• Remaining gap = 360° - 324° = <strong class="text-amber-300">36°</strong>.</li>
                            <li>• 4 pentagons: 4 × 108° = <strong>432° > 360°</strong> (overlap!).</li>
                            <li>• Conclusion: 360 ÷ 108 = 3.33 (not a whole number). Pentagons cannot tile alone!</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>✓</span> Octagon-Square Hybrid Tiling
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• Interior angle of regular octagon = <strong>135°</strong>.</li>
                            <li>• 2 octagons at a vertex: 2 × 135° = <strong>270°</strong>.</li>
                            <li>• Deficit angle to complete 360°: 360° - 270° = <strong class="text-cyan-300">90°</strong>.</li>
                            <li>• A square has 90° corners: <strong>135° + 135° + 90° = 360°</strong>!</li>
                            <li>• Octagons and squares tile the plane together in perfect harmony.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-slate-800/80 border border-slate-700 rounded-lg text-xs text-slate-300">
                    <strong>Only Three Regular Monotilings:</strong> There are only three regular polygons that can tile the plane by themselves: the <em>Equilateral Triangle</em>, the <em>Square</em>, and the <em>Regular Hexagon</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_3",
        "checkpoints": [
            {
                "question": "What is the angle gap left when three regular pentagons meet around a point?",
                "options": ["36°", "45°", "54°", "0°"],
                "correct": 0,
                "explanation": "3 × 108° = 324°. The remaining gap around the 360° vertex is 360° - 324° = 36°."
            },
            {
                "question": "Which shape fills the vertex gap between two regular octagons (135° each) to make 360°?",
                "options": ["Square (90°)", "Equilateral triangle (60°)", "Hexagon (120°)", "Pentagon (108°)"],
                "correct": 0,
                "explanation": "Two octagons take 135° + 135° = 270°. The remaining angle is 360° - 270° = 90°, which is exactly the corner angle of a square."
            }
        ]
    },
    {
        "id": 4,
        "title": "Triangle Types",
        "tag": "Classification by Sides & Angles • Rhombus Dissection",
        "lecture": (
            "Triangles are three-sided polygons, the most fundamental rigid building blocks of geometry. We can classify every triangle "
            "by the relationships among its three sides and three angles. First, take a rhombus cutout and fold it along both its "
            "diagonals. When cut along the diagonals, the rhombus divides into four identical right-angled triangles! Examine the properties "
            "of triangles carefully. An equilateral triangle has all three sides equal in length, and all three interior angles equal to "
            "60 degrees. An isosceles triangle has exactly two sides of equal length. By folding an isosceles triangle down its central "
            "line of symmetry, the two side edges match perfectly, proving that the two base angles opposite the equal sides are also "
            "completely equal! Finally, a scalene triangle has three sides of completely different lengths, and consequently all three "
            "interior angles have different measures. Remember the golden angle sum property: in every triangle, regardless of its "
            "shape or size, the three interior angles always add up to exactly 180 degrees, forming a straight angle!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Triangles are classified into three distinct families based on the equality of their side lengths and interior angles:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-1.5 flex items-center gap-1.5">
                            <span>🔺</span> Equilateral Triangle
                        </h4>
                        <p class="text-slate-300">• Sides: <strong>All 3 equal</strong> (a = b = c)</p>
                        <p class="text-slate-300">• Angles: <strong>All 3 equal = 60°</strong></p>
                        <p class="text-slate-300">• Symmetry: <strong>3 lines of symmetry</strong></p>
                        <p class="font-mono text-emerald-300 font-bold mt-1">• 60° + 60° + 60° = 180°</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-1.5 flex items-center gap-1.5">
                            <span>📐</span> Isosceles Triangle
                        </h4>
                        <p class="text-slate-300">• Sides: <strong>At least 2 equal</strong></p>
                        <p class="text-slate-300">• Angles: <strong>2 base angles equal</strong></p>
                        <p class="text-slate-300">• Symmetry: <strong>1 line of symmetry</strong></p>
                        <p class="font-mono text-cyan-300 font-bold mt-1">• If sides equal, opp angles equal!</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-1.5 flex items-center gap-1.5">
                            <span>📏</span> Scalene Triangle
                        </h4>
                        <p class="text-slate-300">• Sides: <strong>All 3 different</strong></p>
                        <p class="text-slate-300">• Angles: <strong>All 3 different</strong></p>
                        <p class="text-slate-300">• Symmetry: <strong>0 lines of symmetry</strong></p>
                        <p class="font-mono text-rose-300 font-bold mt-1">• Sum still equals 180°</p>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Rhombus Dissection:</strong> Cutting a rhombus along its perpendicular diagonals divides it into 4 congruent right-angled scalene (or isosceles) triangles meeting at 90°.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_4",
        "checkpoints": [
            {
                "question": "In an isosceles triangle, if the two equal sides are 7 cm and the third side is 4 cm, what is true about its angles?",
                "options": [
                    "Two of its angles are equal",
                    "All three angles are 60°",
                    "All three angles are different",
                    "It must have a right angle"
                ],
                "correct": 0,
                "explanation": "In an isosceles triangle, the angles opposite the equal sides are always equal."
            },
            {
                "question": "If two angles of a triangle are 50° and 60°, what is the third angle, and what type of triangle is it?",
                "options": [
                    "70° (Scalene triangle)",
                    "60° (Equilateral triangle)",
                    "50° (Isosceles triangle)",
                    "90° (Right triangle)"
                ],
                "correct": 0,
                "explanation": "Third angle = 180° - (50° + 60°) = 180° - 110° = 70°. Since all angles (50°, 60°, 70°) are different, all sides are different: a scalene triangle."
            }
        ]
    },
    {
        "id": 5,
        "title": "Kite Geometry",
        "tag": "Quadrilateral Properties • Adjacent Equal Sides & Diagonal Symmetry",
        "lecture": (
            "During the vibrant harvest festival of Makar Sankranti, millions of colorful kites soar into the clear blue sky. Have you "
            "ever stopped to investigate the exact geometric definition of a kite? In mathematics, a kite is a quadrilateral—a "
            "four-sided polygon—with a very special side relationship. Unlike a parallelogram where opposite sides are equal, in a "
            "kite, two pairs of adjacent, neighboring sides are equal in length! The two shorter top sides are equal to each other, "
            "and the two longer bottom sides are equal to each other. Now look at the internal diagonals of a kite. Fold a kite paper "
            "model along its long vertical axis: the left half folds over and matches the right half perfectly! This vertical diagonal "
            "is an axis of symmetry. When we draw the second horizontal diagonal, something wonderful occurs: the two diagonals intersect "
            "at exactly 90 degrees, forming perpendicular right angles! Furthermore, the main vertical diagonal bisects the horizontal "
            "cross-diagonal, cutting it into two equal halves. These geometric properties give the kite aerodynamic balance in the wind."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    A kite is a quadrilateral characterized by two pairs of equal-length adjacent sides and mutually perpendicular diagonals.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-2 flex items-center gap-2">
                            <span>🪁</span> Side & Angle Properties
                        </h4>
                        <ul class="text-slate-300 space-y-2">
                            <li>• <strong>Adjacent Equal Sides:</strong> Top pair AB = AD, bottom pair CB = CD.</li>
                            <li>• <strong>Opposite Sides:</strong> Are <em>not</em> equal (AB ≠ CD).</li>
                            <li>• <strong>One Pair of Equal Angles:</strong> The angles between the unequal sides are equal (∠ B = ∠ D).</li>
                            <li>• <strong>Line of Symmetry:</strong> The main diagonal AC is a line of reflective symmetry.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-2 flex items-center gap-2">
                            <span>✛</span> Diagonal Relationships
                        </h4>
                        <ul class="text-slate-300 space-y-2">
                            <li>• <strong>Perpendicular Diagonals:</strong> The two diagonals cross at a <strong>90° right angle</strong> (AC ⊥ BD).</li>
                            <li>• <strong>Bisecting Property:</strong> The vertical diagonal bisects the horizontal cross-diagonal into two equal segments.</li>
                            <li>• <strong>Special Case (Rhombus):</strong> A rhombus is an equilateral kite where all 4 sides are equal!</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>Aerodynamic Geometry:</strong> The symmetry axis and perpendicular cross-struts provide maximum stability and wind resistance when flying in the sky.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_5",
        "checkpoints": [
            {
                "question": "Which statement correctly defines a kite quadrilateral?",
                "options": [
                    "A quadrilateral with two pairs of adjacent equal sides",
                    "A quadrilateral with two pairs of opposite equal sides",
                    "A quadrilateral with four equal angles of 90°",
                    "A shape with only 3 sides"
                ],
                "correct": 0,
                "explanation": "A kite has two pairs of adjacent (neighboring) sides that are equal in length."
            },
            {
                "question": "At what angle do the diagonals of a kite intersect?",
                "options": ["90° (Perpendicular)", "60°", "45°", "180°"],
                "correct": 0,
                "explanation": "The diagonals of any kite are always perpendicular, meeting at 90°."
            }
        ]
    },
    {
        "id": 6,
        "title": "Parallelograms and Rectangles",
        "tag": "Quadrilateral Taxonomy • Opposites, Rights Angles & Rhombuses",
        "lecture": (
            "Let us expand our quadrilateral gallery to investigate parallelograms, rectangles, and rhombuses. Picture a flexible "
            "wooden frame made of four hinged rods. When opposite sides are parallel and equal in length, the shape is a parallelogram. "
            "In any parallelogram, opposite sides are equal, and opposite angles are equal! Now take this slanted parallelogram frame "
            "and push it upright until all four interior angles become crisp 90-degree right angles. What have you created? A rectangle! "
            "A rectangle is a special parallelogram with four right angles. Because it is a parallelogram, its opposite sides are still "
            "equal, but its diagonals now have the remarkable property of being exactly equal in length! Next, take a frame where all "
            "four sides are equal in length: that is a rhombus. In a rhombus, opposite sides are parallel, but all four sides are equal, "
            "and its diagonals intersect at 90 degrees. Finally, what if a shape has four equal sides AND four right angles? That is "
            "a square! A square is the king of quadrilaterals: simultaneously a rectangle, a rhombus, and a parallelogram."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The quadrilateral family tree connects parallelograms, rectangles, rhombuses, and squares through progressive angle and side constraints:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-2">
                            <span>▱</span> Parallelogram vs Rectangle
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Parallelogram:</strong> Opposite sides parallel & equal; opposite angles equal; diagonals bisect each other.</li>
                            <li>• <strong>Rectangle:</strong> A parallelogram where <strong>all 4 angles = 90°</strong>.</li>
                            <li>• <strong>Diagonal Invariant:</strong> In a rectangle, the two diagonals are <strong>equal in length</strong> (d₁ = d₂).</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-2 flex items-center gap-2">
                            <span>◇</span> Rhombus vs Square
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>Rhombus:</strong> A parallelogram where <strong>all 4 sides are equal</strong>; diagonals cross at <strong>90°</strong>.</li>
                            <li>• <strong>Square:</strong> Combines rectangle and rhombus properties: 4 equal sides AND 4 right angles (90°)!</li>
                            <li>• <strong>Hierarchy:</strong> Every square is a rectangle, every square is a rhombus, and all are parallelograms.</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Diagonal Diagnostic:</strong> Bisect each other ➔ Parallelogram; Equal length ➔ Rectangle; Perpendicular (90°) ➔ Rhombus or Kite; Both equal and perpendicular ➔ Square!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_6",
        "checkpoints": [
            {
                "question": "Which property is true for a rectangle but NOT necessarily true for all parallelograms?",
                "options": [
                    "All four angles are 90° right angles",
                    "Opposite sides are equal",
                    "Opposite sides are parallel",
                    "Diagonals bisect each other"
                ],
                "correct": 0,
                "explanation": "All four angles being 90° is the defining property of a rectangle. General parallelograms have slanted angles."
            },
            {
                "question": "A quadrilateral has 4 equal sides and diagonals that cross at 90°, but its angles are not 90°. What shape is it?",
                "options": ["A rhombus", "A square", "A rectangle", "A trapezoid"],
                "correct": 0,
                "explanation": "A shape with 4 equal sides and non-right angles is a rhombus."
            }
        ]
    },
    {
        "id": 7,
        "title": "Seven Tangrams",
        "tag": "Tangram Puzzle • Geometric Dissection & Shape Synthesis",
        "lecture": (
            "Originating in ancient China, the tangram is one of the world's most famous geometric dissection puzzles. A single square "
            "is cut into exactly seven geometric pieces, known as tans: two large right-angled triangles, one medium right-angled "
            "triangle, two small right-angled triangles, one small square, and one parallelogram. Notice that all five triangles in the "
            "tangram set are isosceles right-angled triangles, meaning each has one 90-degree corner and two 45-degree corners! This "
            "common angle relationship allows the pieces to combine in astonishing ways. For instance, putting the two small triangles "
            "together hypotenuse-to-hypotenuse forms the small square! Joining them leg-to-leg forms the medium triangle or the "
            "parallelogram! Using all seven pieces without overlapping, we can form animals, boats, dancers, and even recreate the "
            "original large square. Tangrams teach us spatial transformation: complex structures can be dissected into simpler shapes, "
            "and simple shapes can synthesize infinite artistic and mathematical forms."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The 7-piece tangram puzzle decomposes a unit square into proportional geometric tiles sharing 45°, 90°, and 135° angles:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-violet-500/30">
                        <h4 class="font-bold text-violet-400 mb-2 flex items-center gap-2">
                            <span>🧩</span> The 7 Tan Pieces
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• <strong>2 Large Triangles:</strong> Each has area = 1/4 of total square.</li>
                            <li>• <strong>1 Medium Triangle:</strong> Area = 1/8 of total square.</li>
                            <li>• <strong>2 Small Triangles:</strong> Each area = 1/16 of total square.</li>
                            <li>• <strong>1 Square:</strong> Area = 1/8 of total square.</li>
                            <li>• <strong>1 Parallelogram:</strong> Area = 1/8 of total square.</li>
                            <li>• All 5 triangles are <strong>45°-45°-90° isosceles triangles</strong>!</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
                        <h4 class="font-bold text-teal-400 mb-2 flex items-center gap-2">
                            <span>🔄</span> Equivalent Compositions
                        </h4>
                        <ul class="text-slate-300 space-y-1.5">
                            <li>• 2 Small Triangles = <strong>1 Square</strong> (hypotenuse joined).</li>
                            <li>• 2 Small Triangles = <strong>1 Medium Triangle</strong> (legs joined).</li>
                            <li>• 2 Small Triangles = <strong>1 Parallelogram</strong> (reversed legs joined).</li>
                            <li>• 2 Large Triangles + 1 Medium + 2 Small + 1 Square + 1 Parallelogram = <strong>1 Big Whole Square</strong>!</li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-violet-950/40 border border-violet-500/30 rounded-lg text-xs text-violet-200">
                    <strong>Conservation of Area:</strong> No matter how the 7 pieces are rearranged (into a swan, a running person, or a house), the total surface area remains exactly equal to the original square.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_7",
        "checkpoints": [
            {
                "question": "How many triangles are there in a standard 7-piece tangram set?",
                "options": ["5 triangles", "4 triangles", "7 triangles", "3 triangles"],
                "correct": 0,
                "explanation": "A standard tangram has 5 triangles (2 large, 1 medium, 2 small), 1 square, and 1 parallelogram (total 7 pieces)."
            },
            {
                "question": "What shape can be formed by joining the two small tangram triangles along their longest side (hypotenuse)?",
                "options": ["The small square", "A hexagon", "The large triangle", "A circle"],
                "correct": 0,
                "explanation": "Joining the hypotenuses of two 45°-45°-90° small triangles forms a square identical to the tangram square."
            }
        ]
    },
    {
        "id": 8,
        "title": "Shape Riddles",
        "tag": "Which Shape Am I? • Deductive Geometry Logic & Property Matching",
        "lecture": (
            "Put on your mathematical detective hats for our popular game: 'Which Shape Am I?' In this inquiry, we use logical deduction "
            "to identify mystery geometric figures from forensic property clues. Clue one: 'I am a quadrilateral. All four of my sides "
            "are equal in length, but none of my corner angles are 90 degrees. Which shape am I?' Since all four sides are equal, it "
            "must be either a square or a rhombus; because its angles are not 90 degrees, it is definitively a rhombus! Clue two: 'I am a "
            "polygon. I have two pairs of adjacent sides that are equal, but my opposite sides are not parallel. My diagonals cross at "
            "perpendicular right angles. Which shape am I?' That is the hallmark of a kite! Clue three: 'I am a four-sided polygon. "
            "My opposite sides are parallel and equal, but my diagonals are of different lengths and do not meet at 90 degrees.' That is "
            "a general parallelogram! Clue four: 'I have four sides, two pairs of parallel opposite sides, and two equal diagonals.' That "
            "is a rectangle! By linking geometric definitions to precise properties, you master the deductive language of geometry."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Test your deductive geometry skills by analyzing property clues to identify mystery 2-D shapes:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30">
                        <span class="font-bold text-cyan-400 block mb-1">Riddle 1</span>
                        <p class="text-slate-300 italic mb-1">"I have 4 equal sides, 4 right angles, and equal perpendicular diagonals."</p>
                        <p class="font-mono text-emerald-300 font-bold">➔ Answer: Square</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-amber-500/30">
                        <span class="font-bold text-amber-400 block mb-1">Riddle 2</span>
                        <p class="text-slate-300 italic mb-1">"I have 4 sides. Opposite sides are equal, all angles are 90°, and diagonals are equal."</p>
                        <p class="font-mono text-emerald-300 font-bold">➔ Answer: Rectangle</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-purple-500/30">
                        <span class="font-bold text-purple-400 block mb-1">Riddle 3</span>
                        <p class="text-slate-300 italic mb-1">"I have 4 equal sides, opposite angles are equal, but no right angles."</p>
                        <p class="font-mono text-emerald-300 font-bold">➔ Answer: Rhombus</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-rose-500/30">
                        <span class="font-bold text-rose-400 block mb-1">Riddle 4</span>
                        <p class="text-slate-300 italic mb-1">"Adjacent pairs of sides are equal, diagonals are perpendicular, exactly 1 line of symmetry."</p>
                        <p class="font-mono text-emerald-300 font-bold">➔ Answer: Kite</p>
                    </div>
                </div>
                <div class="p-3 bg-slate-800/80 border border-slate-700 rounded-lg text-xs text-slate-300">
                    <strong>Deduction Strategy:</strong> Filter shapes step-by-step: 1. Count sides ➔ 2. Check side equality ➔ 3. Inspect corner angles ➔ 4. Check diagonal properties.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_8",
        "checkpoints": [
            {
                "question": "A shape has 4 sides, opposite sides are parallel and equal, but its diagonals are NOT equal in length. What shape is it?",
                "options": [
                    "A parallelogram",
                    "A rectangle",
                    "A square",
                    "A circle"
                ],
                "correct": 0,
                "explanation": "In a general parallelogram, diagonals are of unequal length (one long, one short). If diagonals were equal, it would be a rectangle."
            },
            {
                "question": "Which quadrilateral has exactly one line of reflective symmetry and perpendicular diagonals?",
                "options": ["Kite", "Parallelogram", "Rhombus", "Scalene triangle"],
                "correct": 0,
                "explanation": "A kite has exactly one line of reflective symmetry (down its main diagonal) and perpendicular diagonals."
            }
        ]
    }
]

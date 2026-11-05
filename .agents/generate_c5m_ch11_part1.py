# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
Part 1: Slides 1 to 8 (Theory, Narration 195-215 words, 16 Checkpoints)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Quilt Perimeter",
        "tagline": "Outer Boundaries • Grandmother's Quilt Lace Border & Total Edge Length",
        "lecture": (
            "Welcome to the inspiring world of perimeter and area. Our journey begins with a heartwarming story from Preetha "
            "and Adrit's home. Their grandmother has just finished stitching a beautiful rectangular patchwork quilt made from soft "
            "cotton fabric scraps. To give the quilt a neat and festive finish, she wants to stitch a continuous decorative lace ribbon "
            "all the way around its outer edge. How can grandmother determine the exact length of lace ribbon she needs to buy from the market? "
            "She uses a measuring tape to measure each of the four outer edges: the top edge, the bottom edge, the left edge, and the right "
            "edge. When she adds these four side lengths together, she calculates what mathematicians call the perimeter. Perimeter is the total "
            "continuous distance around the outside boundary of any closed two-dimensional shape. If a quilt measures 200 centimetres in length "
            "and 150 centimetres in breadth, grandmother needs 200 plus 150 plus 200 plus 150 centimetres of lace ribbon, which equals 700 "
            "centimetres or 7 metres. Whether you are fencing a farming field, framing a family photograph, or running around a jogging track, "
            "you are always measuring perimeter along the outer boundary lines."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">What is Perimeter?</h3>
                <p>The <strong>perimeter</strong> of any closed two-dimensional shape is the <em>total path length</em> along its outer boundary edge. It is measured in linear units like centimetres (cm) or metres (m).</p>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">Grandmother's Quilt:</span>
                    <p class="text-[11px] text-slate-300">Length = 200 cm, Breadth = 150 cm.<br>Perimeter = 200 + 150 + 200 + 150 = 700 cm (7 m of lace ribbon needed).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold block mb-1">Everyday Boundaries:</span>
                    <p class="text-[11px] text-slate-300">• Fencing wire around a garden.<br">• Picture frame around a canvas.<br">• Running track outer lane.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "What does the perimeter of a closed shape represent?",
                "options": [
                    "The total continuous length of its outer boundary",
                    "The flat surface region enclosed inside",
                    "The weight of the cardboard sheet",
                    "The number of corners inside the shape"
                ],
                "answer": 0,
                "explanation": "Perimeter is strictly the total length around the outer boundary edges of a closed figure."
            },
            {
                "id": "cp1_2",
                "question": "If a rectangular quilt measures 3 metres in length and 2 metres in breadth, what is its perimeter?",
                "options": [
                    "10 metres (3 + 2 + 3 + 2)",
                    "6 metres (3 × 2)",
                    "5 metres (3 + 2)",
                    "12 metres"
                ],
                "answer": 0,
                "explanation": "Perimeter = Top + Bottom + Left + Right = 3 + 3 + 2 + 2 = 10 metres."
            }
        ]
    },

    {
        "id": 2,
        "title": "Regular Polygons",
        "tagline": "Equal-Sided Shapes • Equilateral Triangles, Squares & Hexagonal Perimeters",
        "lecture": (
            "When all the sides of a polygon are equal in length, mathematicians call it a regular polygon. Calculating the perimeter "
            "of regular polygons is delightfully fast and simple because you do not have to add each side individually. Instead, you can "
            "use multiplication! Consider an equilateral triangle, which has three identical sides. If each side measures 6 centimetres, its "
            "perimeter is simply 3 times 6 centimetres, which equals 18 centimetres. Next, consider a square, which has four identical sides. "
            "If each side of a square patch measures 8 centimetres, its perimeter is 4 times 8 centimetres, which equals 32 centimetres. For a "
            "regular pentagon with five equal sides of 5 centimetres, the perimeter is 5 times 5, or 25 centimetres. For a regular hexagon with "
            "six equal sides of 4 centimetres, the perimeter is 6 times 4, or 24 centimetres. The universal formula for any regular polygon with "
            "n equal sides is simply n multiplied by the length of one side. This shortcut saves enormous time when craftspersons construct "
            "hexagonal tile mosaics, star badges, and geometric quilt patches with matching borders, enabling builders to measure outer boundaries "
            "swiftly without repeatedly measuring each individual identical edge with a ruler."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Perimeter Formula for Regular Polygons</h3>
                <p>For any regular polygon having <strong>n equal sides</strong> each of length <strong>s</strong>:</p>
                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center mt-2">
                    Perimeter = n × Side Length (s)
                </div>
            </div>
            <div class="grid grid-cols-3 gap-2 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-300 font-bold block text-xs">Equilateral Triangle</span>
                    <span class="text-cyan-300 font-bold block my-1">3 × s</span>
                    <span class="text-[10px] text-slate-400">3 equal sides</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-300 font-bold block text-xs">Square</span>
                    <span class="text-cyan-300 font-bold block my-1">4 × s</span>
                    <span class="text-[10px] text-slate-400">4 equal sides</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-300 font-bold block text-xs">Regular Hexagon</span>
                    <span class="text-cyan-300 font-bold block my-1">6 × s</span>
                    <span class="text-[10px] text-slate-400">6 equal sides</span>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "What is the perimeter of a regular pentagon having side length of 7 cm?",
                "options": [
                    "35 cm (5 × 7 cm)",
                    "28 cm (4 × 7 cm)",
                    "49 cm (7 × 7 cm)",
                    "12 cm (5 + 7 cm)"
                ],
                "answer": 0,
                "explanation": "A regular pentagon has 5 equal sides. Perimeter = 5 × 7 cm = 35 cm."
            },
            {
                "id": "cp2_2",
                "question": "If a regular hexagon has a perimeter of 48 cm, what is the length of one side?",
                "options": [
                    "8 cm (48 ÷ 6)",
                    "6 cm (48 ÷ 8)",
                    "12 cm (48 ÷ 4)",
                    "24 cm (48 ÷ 2)"
                ],
                "answer": 0,
                "explanation": "Side length = Perimeter ÷ Number of sides = 48 cm ÷ 6 = 8 cm."
            }
        ]
    },

    {
        "id": 3,
        "title": "Drawing Rectangles",
        "tagline": "Constrained Boundaries • Constructing Multiple Rectangles with a Fixed Target Perimeter",
        "lecture": (
            "Here is an intriguing mathematical puzzle: can multiple different rectangles share the exact same perimeter? Absolutely! "
            "Let us investigate how to draw distinct rectangles that all have a fixed target perimeter of 26 centimetres. Remember that "
            "the perimeter of a rectangle consists of two lengths and two breadths: two times length plus two times breadth equals 26 centimetres. "
            "If we divide 26 by 2, we discover a powerful secret: the sum of one length plus one breadth must always equal half the perimeter, "
            "which is 13 centimetres! Now, we simply find whole-number pairs that add up to 13. We can draw a long, narrow rectangle with a length "
            "of 12 centimetres and a breadth of 1 centimetre. We can draw a second rectangle with a length of 11 centimetres and a breadth of 2 "
            "centimetres. Other valid pairs include 10 and 3, 9 and 4, 8 and 5, or 7 and 6. Every single one of these different rectangles "
            "uses exactly 26 centimetres of lace ribbon around its edge! The half-perimeter strategy unlocks an entire family of shapes from "
            "a single boundary measurement, showing how one fixed piece of ribbon can enclose shapes with widely varying dimensions."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">The Half-Perimeter Secret</h3>
                <p>Because Perimeter = 2 × (Length + Breadth), dividing the target perimeter by 2 gives the sum of one length and one breadth:</p>
                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center mt-2">
                    Length + Breadth = Perimeter ÷ 2
                </div>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Target Perimeter</th>
                            <th class="p-1.5 border-b border-slate-700">Half-Perimeter (L + B)</th>
                            <th class="p-1.5 border-b border-slate-700">Distinct (Length, Breadth) Combinations</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">26 cm</td>
                            <td class="p-1.5 text-cyan-300">13 cm</td>
                            <td class="p-1.5 text-slate-200">(12, 1), (11, 2), (10, 3), (9, 4), (8, 5), (7, 6)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">18 cm</td>
                            <td class="p-1.5 text-cyan-300">9 cm</td>
                            <td class="p-1.5 text-slate-200">(8, 1), (7, 2), (6, 3), (5, 4)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "If a rectangle has a perimeter of 18 cm, what must the sum of its length and breadth equal?",
                "options": [
                    "9 cm (18 ÷ 2)",
                    "18 cm",
                    "36 cm",
                    "4.5 cm"
                ],
                "answer": 0,
                "explanation": "Length + Breadth = Half-Perimeter = 18 cm ÷ 2 = 9 cm."
            },
            {
                "id": "cp3_2",
                "question": "Which of the following (length, breadth) pairs produces a rectangle with a perimeter of 26 cm?",
                "options": [
                    "Length = 10 cm, Breadth = 3 cm",
                    "Length = 10 cm, Breadth = 6 cm",
                    "Length = 13 cm, Breadth = 13 cm",
                    "Length = 5 cm, Breadth = 5 cm"
                ],
                "answer": 0,
                "explanation": "10 + 3 = 13 cm. Perimeter = 2 × 13 cm = 26 cm."
            }
        ]
    },

    {
        "id": 4,
        "title": "Area & Tiling",
        "tagline": "Surface Coverage • Tessellation Without Gaps vs Circular Empty Spaces",
        "lecture": (
            "While perimeter measures the boundary ribbon running around a quilt, area measures something entirely different: "
            "the flat surface region enclosed inside the boundary! Area is defined as the amount of flat surface covered by a shape "
            "without any gaps or overlapping edges. To understand area deeply, imagine tiling a bathroom floor or assembling patchwork "
            "cloth blocks for grandmother's quilt. What shapes can tile a flat surface completely? If you use square cloth patches, "
            "they fit together seamlessly at every corner with zero gaps. Rectangular blocks and equilateral triangles also tile a surface "
            "flawlessly without leaving empty spots. However, try tiling a table surface with round circular coins or circular coasters! "
            "No matter how tightly you press circles together, tiny diamond-shaped empty gaps always remain between them. Circles cannot "
            "tile a flat plane completely! Polygons that fit together edge-to-edge without gaps create what mathematicians call a tessellation. "
            "Because squares tile perfectly without gaps or overlaps, the unit square was chosen as the universal standard unit for measuring area "
            "across science, design, and mathematics, allowing architects, builders, craftspersons, and landowners to quantify floor space, tile counts, "
            "carpet needs, and farming plots with absolute geometric clarity and precision."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">What is Area?</h3>
                <p><strong>Area</strong> is the measure of the <em>flat surface region</em> enclosed within a boundary, quantified by the number of unit shapes needed to cover it completely without gaps or overlaps.</p>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-emerald-950/30 border border-emerald-800/40">
                    <span class="text-emerald-300 font-bold block mb-1">Shapes that Tile (Zero Gaps):</span>
                    <p class="text-[11px] text-slate-300">• Squares (Standard unit!)<br">• Rectangles<br">• Equilateral Triangles<br>• Regular Hexagons</p>
                </div>
                <div class="p-2.5 rounded-lg bg-rose-950/30 border border-rose-800/40">
                    <span class="text-rose-300 font-bold block mb-1">Shapes with Gaps:</span>
                    <p class="text-[11px] text-slate-300">• Circles & Ovals<br>• Irregular curved shapes<br>Always leave empty diamond-like voids between contact points!</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "What is the key difference between perimeter and area?",
                "options": [
                    "Perimeter measures outer boundary length; area measures enclosed flat surface",
                    "Perimeter is measured in square centimetres; area in linear metres",
                    "Perimeter applies only to circles; area applies only to squares",
                    "They are identical terms measuring the exact same quantity"
                ],
                "answer": 0,
                "explanation": "Perimeter is 1-dimensional boundary length; area is 2-dimensional surface coverage."
            },
            {
                "id": "cp4_2",
                "question": "Why are squares chosen as the standard unit for measuring area instead of circles?",
                "options": [
                    "Squares pack together tightly leaving zero gaps or overlaps",
                    "Squares are colorful and circles are colorless",
                    "Circles are too heavy to hold on paper",
                    "Squares have no perimeter"
                ],
                "answer": 0,
                "explanation": "Squares tessellate a plane perfectly without leaving empty gaps, making them ideal standard units."
            }
        ]
    },

    {
        "id": 5,
        "title": "Non-Standard Units",
        "tagline": "Informal Area Benchmarks • Table Surface Covering & Triangular Patch Equivalence",
        "lecture": (
            "Before using standard square centimetres, students learn to measure and estimate surface areas using everyday classroom "
            "objects as non-standard units. For example, how many math textbooks are required to cover your study desk completely? "
            "You might lay out 6 textbooks neatly in 2 rows of 3, concluding that the desk has an area of 6 textbook units. You could "
            "also measure the same desk using pencil boxes or lunch boxes, discovering that smaller units yield a larger count to cover "
            "the same surface! In patchwork quilt design, grandmother uses geometric fabric tiles of different sizes. Consider a decorative "
            "mat filled with blue squares and green triangles. If you slice a 1 centimetre square along its diagonal, you produce two "
            "identical right-angled triangles. That means two small triangular patches equal the area of one full square patch! If a quilt "
            "design contains 10 blue squares and 8 green triangles, its total area in square units is 10 plus half of 8, which equals 10 "
            "plus 4, or 14 square units. Grouping partial units into whole units is the foundational stepping stone to rigorous area calculation, "
            "helping young mathematicians grasp fractional combinations before working with abstract algebraic formulas."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Composite Tile Equivalence</h3>
                <p>When measuring area with multi-shape tile sets, convert smaller non-standard units into full square units:</p>
                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center mt-2">
                    2 Half-Triangles = 1 Full Unit Square
                </div>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block mb-1">Desk Tiling Example:</span>
                    <p class="text-[11px] text-slate-300">Desk covered by: 12 Blue Squares + 6 Green Triangles.<br>Area = 12 + (6 ÷ 2) = 12 + 3 = 15 square units.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">Unit Size Principle:</span>
                    <p class="text-[11px] text-slate-300">Smaller non-standard units (e.g. pencil boxes) require a higher count to cover the same table than larger units (e.g. textbooks).</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "If two identical right-angled triangles combine to form one square tile, how many triangles equal 5 square tiles?",
                "options": [
                    "10 triangles (5 × 2)",
                    "7 triangles (5 + 2)",
                    "2.5 triangles (5 ÷ 2)",
                    "25 triangles"
                ],
                "answer": 0,
                "explanation": "Each square requires 2 triangles, so 5 squares require 5 × 2 = 10 triangles."
            },
            {
                "id": "cp5_2",
                "question": "A patchwork mat contains 8 whole squares and 6 half-triangles. What is its total area in square units?",
                "options": [
                    "11 square units (8 + 3)",
                    "14 square units (8 + 6)",
                    "7 square units",
                    "48 square units"
                ],
                "answer": 0,
                "explanation": "6 half-triangles = 3 whole squares. Total area = 8 + 3 = 11 square units."
            }
        ]
    },

    {
        "id": 6,
        "title": "Grid Measurement",
        "tagline": "Standard Grids • 1 cm Square Grid Overlays & Unit Square Foundations",
        "lecture": (
            "Because non-standard units like books and lunch boxes vary in size across different schools and homes, mathematicians "
            "established a universal standard: the 1 centimetre square grid. A unit square is defined as an exact square whose sides each "
            "measure 1 centimetre. The flat surface region enclosed inside this unit square is defined as exactly 1 square centimetre, "
            "abbreviated as 1 sq cm or cm squared. When you place any geometric shape onto a 1 centimetre grid paper, you can determine "
            "its exact area by counting the unit squares it covers! To count accurately, we follow three simple rules: first, count every "
            "full square covered as 1; second, count every half-square covered as half; and third, if a boundary cuts a square irregularly, "
            "count squares that are more than half covered as 1 full square, while ignoring squares that are less than half covered. "
            "By pairing up half squares into whole numbers, you can determine the area of irregular garden plots, triangular sails, "
            "and patchwork mats with remarkable geometric accuracy, establishing an objective baseline that remains identical in every classroom "
            "and scientific laboratory across the entire world, enabling learners to communicate spatial measurements without any misunderstanding."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Standard 1 cm² Grid Counting Rules</h3>
                <p>When finding the area of any shape overlaid on a 1 cm square grid:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold block text-xs">Full Squares</span>
                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1</span>
                    <span class="text-[10px] text-slate-400">Completely filled cells</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-xs">Half Squares</span>
                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1/2</span>
                    <span class="text-[10px] text-slate-400">Two half cells = 1 cm²</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-indigo-400 font-bold block text-xs">&gt; Half Squares</span>
                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1</span>
                    <span class="text-[10px] text-slate-400">Ignore cells &lt; half</span>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "What is the area of a square whose sides each measure 1 cm?",
                "options": [
                    "1 square centimetre (1 sq cm)",
                    "4 centimetres",
                    "2 square centimetres",
                    "10 millimetres"
                ],
                "answer": 0,
                "explanation": "A unit square with sides of 1 cm covers an area of 1 cm × 1 cm = 1 square centimetre."
            },
            {
                "id": "cp6_2",
                "question": "A shape on grid paper covers 6 full squares and 4 half-squares. What is its total area?",
                "options": [
                    "8 sq cm (6 + 2)",
                    "10 sq cm (6 + 4)",
                    "12 sq cm",
                    "7 sq cm"
                ],
                "answer": 0,
                "explanation": "4 half-squares = 2 full sq cm. Total area = 6 + 2 = 8 sq cm."
            }
        ]
    },

    {
        "id": 7,
        "title": "Palm Tracing",
        "tagline": "Organic Area Estimation • Tracing Handprints on 1 cm Grids",
        "lecture": (
            "How large is your own hand? We can answer this question with scientific precision through the palm tracing activity. "
            "Place your hand flat on a sheet of 1 centimetre squared grid paper, keeping your fingers gently spread. Using a sharp pencil, "
            "trace the outline of your palm and fingers carefully along the paper. When you lift your hand, an organic silhouette appears "
            "across the grid lines. How do we compute the area of such an irregular shape with curved fingertips? We apply the standard grid "
            "counting conventions. First, mark every completely filled square with a blue dot and count them up. Next, look for squares that "
            "are cut by your skin boundary: count squares that are more than half covered as 1, count squares that are roughly half covered as "
            "half, and ignore tiny slivers that cover less than half. Adding these counts gives a close estimate of your palm area in square "
            "centimetres! Comparing handprints with classmates reveals fascinating variations: taller students often have palm areas exceeding "
            "80 square centimetres, while smaller hands measure around 50 square centimetres, demonstrating how empirical grid counting bridges "
            "geometry with human anatomy and personal biology in an engaging, interactive classroom experiment."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Estimating Irregular Organic Surfaces</h3>
                <p>Natural objects like human hands, footprints, and water puddles do not have straight edges. Square grids allow estimation via threshold counting:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">Step-by-Step Procedure:</span>
                    <p class="text-[11px] text-slate-300">1. Trace hand flat on 1 cm grid.<br>2. Count full cells (N_full).<br>3. Count cells &gt; 1/2 covered (N_more).<br>4. Estimated Area ≈ N_full + N_more.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold block mb-1">Typical Class Results:</span>
                    <p class="text-[11px] text-slate-300">• Grade 5 student palm: ~50 to 75 cm²<br>• Adult teacher palm: ~90 to 120 cm²<br>Enables direct empirical comparison!</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "When tracing an irregular curved handprint on grid paper, how should a square that is more than half covered be counted?",
                "options": [
                    "As 1 full square centimetre",
                    "Ignored completely as 0",
                    "Divided by 10",
                    "Multiplied by 4"
                ],
                "answer": 0,
                "explanation": "In grid area approximation, any cell more than half covered is rounded up and counted as 1 full square."
            },
            {
                "id": "cp7_2",
                "question": "A student traces their palm and counts 42 fully covered squares and 14 squares that are more than half covered. What is the estimated palm area?",
                "options": [
                    "56 sq cm (42 + 14)",
                    "28 sq cm (42 - 14)",
                    "588 sq cm (42 × 14)",
                    "42 sq cm"
                ],
                "answer": 0,
                "explanation": "Estimated area = Full squares + More-than-half squares = 42 + 14 = 56 square centimetres."
            }
        ]
    },

    {
        "id": 8,
        "title": "Leaf Area",
        "tagline": "Botanical Surface Comparison • Tracing Garden Leaves from Smallest to Largest",
        "lecture": (
            "Just as we estimated handprint areas, we can venture into the school garden to explore the diverse geometry of plant leaves. "
            "Collect a variety of fallen leaves from different plants: a tiny coriander or neem leaf, a slender mango leaf, a broad banyan "
            "leaf, and an expansive peepal leaf. Lay each leaf flat against your 1 centimetre grid paper, press it gently with your fingers, "
            "and trace its outer contour with a fine pencil. By counting the enclosed unit squares using our established estimation guidelines, "
            "you can calculate and rank the surface areas of these botanical wonders with confidence. A small rose leaflet might cover only 4 "
            "square centimetres, whereas a mature peepal leaf can span over 65 square centimetres! Biologists use this exact mathematical grid "
            "method to study photosynthesis, because a leaf with a larger surface area captures more sunlight and carbon dioxide to produce food. "
            "Comparing leaf areas bridges mathematics and botany, illustrating how living organisms adapt their flat surface geometry to thrive "
            "in their natural forest habitats, showing that mathematical principles of surface coverage govern the living natural world all around "
            "our homes, classrooms, school courtyards, parks, and diverse outdoor natural environments."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Botanical Leaf Surface Ranking</h3>
                <p>Grid paper provides an objective tool to compare organic shapes without complex calculus:</p>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Leaf Sample</th>
                            <th class="p-1.5 border-b border-slate-700">Shape Character</th>
                            <th class="p-1.5 border-b border-slate-700">Estimated Area</th>
                            <th class="p-1.5 border-b border-slate-700">Biological Significance</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Neem Leaflet</td>
                            <td class="p-1.5 text-slate-200">Serrated, slender</td>
                            <td class="p-1.5 text-cyan-300">~3 to 5 cm²</td>
                            <td class="p-1.5 text-slate-400">Minimizes water loss in dry climates</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Mango Leaf</td>
                            <td class="p-1.5 text-slate-200">Elongated lanceolate</td>
                            <td class="p-1.5 text-cyan-300">~25 to 35 cm²</td>
                            <td class="p-1.5 text-slate-400">Balanced sun capture and wind tolerance</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Peepal Leaf</td>
                            <td class="p-1.5 text-slate-200">Broad cordate with drip tip</td>
                            <td class="p-1.5 text-cyan-300">~55 to 70 cm²</td>
                            <td class="p-1.5 text-slate-400">High photosynthetic surface area</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "Why is grid paper useful for finding the area of a peepal leaf?",
                "options": [
                    "A leaf has irregular curved edges that cannot be calculated with simple ruler multiplication",
                    "Grid paper changes the color of the leaf",
                    "Grid paper makes the leaf grow larger",
                    "Leaves only grow in perfect rectangular shapes"
                ],
                "answer": 0,
                "explanation": "Because organic leaves have irregular curved boundaries, counting unit squares on grid paper provides an accurate surface estimate."
            },
            {
                "id": "cp8_2",
                "question": "Leaf A covers 28 unit squares on a 1 cm grid, while Leaf B covers 45 unit squares. Which leaf has a larger surface area?",
                "options": [
                    "Leaf B is larger by 17 sq cm",
                    "Leaf A is larger by 17 sq cm",
                    "Both leaves have identical area",
                    "Cannot be determined without weighing them"
                ],
                "answer": 0,
                "explanation": "45 sq cm - 28 sq cm = 17 sq cm. Leaf B covers 17 more unit squares than Leaf A."
            }
        ]
    }
]

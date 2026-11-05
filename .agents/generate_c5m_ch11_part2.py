# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
Part 2 Data: Slides 9 to 16
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Same Area Perimeters",
        "tagline": "Fixed Area Investigation • Arranging 12 Unit Squares into Multiple Perimeters",
        "lecture": (
            "A fascinating mathematical mystery unfolds when we explore shapes with identical surface areas: do shapes that cover the exact "
            "same area always have the same perimeter? Let us test this using twelve unit squares, each measuring 1 square centimetre. "
            "Because we are using twelve squares, every single arrangement will have an identical area of 12 square centimetres. "
            "If we arrange all twelve tiles into a single long strip measuring 1 centimetre wide and 12 centimetres long, the perimeter "
            "equals 1 plus 12 plus 1 plus 12, which totals 26 centimetres! Next, rearrange the twelve tiles into two rows of six. "
            "Now the length is 6 centimetres and the breadth is 2 centimetres. The perimeter becomes 2 plus 6 plus 2 plus 6, "
            "giving 16 centimetres! Finally, arrange them into three rows of four. The perimeter is now 3 plus 4 plus 3 plus 4, "
            "which is only 14 centimetres! Notice what occurred: while every shape maintained an identical area of 12 square centimetres, "
            "their perimeters changed drastically from 26 down to 14 centimetres! As shapes become more compact and closer to a square, "
            "their perimeter shrinks, proving that having the same area does not guarantee having the same perimeter."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Core Investigation</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Shapes having the <strong>exact same area</strong> can possess vastly different perimeters depending on how their unit tiles are configured!
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Strip: 1 × 12</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-white">Area = 12 cm²</div>
                <div class="text-xs text-rose-400 font-mono mt-1">P = 2 × (1 + 12) = 26 cm</div>
            </div>
            <p class="text-xs text-slate-400">Extremely elongated shape yields the maximum border perimeter.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Grid: 2 × 6</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-white">Area = 12 cm²</div>
                <div class="text-xs text-cyan-400 font-mono mt-1">P = 2 × (2 + 6) = 16 cm</div>
            </div>
            <p class="text-xs text-slate-400">Moderately compact arrangement with a reduced perimeter.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Block: 3 × 4</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-white">Area = 12 cm²</div>
                <div class="text-xs text-emerald-400 font-mono mt-1">P = 2 × (3 + 4) = 14 cm</div>
            </div>
            <p class="text-xs text-slate-400">Most compact rectangle configuration gives the smallest perimeter.</p>
        </div>
    </div>

    <div class="bg-blue-950/40 border border-blue-500/30 rounded-xl p-3 flex items-center justify-between">
        <span class="text-xs text-blue-300 font-medium">Key Takeaway</span>
        <span class="text-xs text-slate-300">More compact / squarish shapes have smaller perimeters for a fixed area!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If you arrange 16 unit squares into a 1 × 16 rectangle and a 4 × 4 square, what are their perimeters?",
                "options": [
                    "1 × 16 has P = 34 cm; 4 × 4 has P = 16 cm",
                    "Both shapes have identical perimeters of 16 cm",
                    "1 × 16 has P = 17 cm; 4 × 4 has P = 8 cm",
                    "1 × 16 has P = 32 cm; 4 × 4 has P = 24 cm"
                ],
                "answer": 0,
                "explanation": "For 1 × 16: P = 2 × (1 + 16) = 34 cm. For 4 × 4: P = 4 × 4 = 16 cm. The compact square has less than half the perimeter of the strip!",
                "hint": "Add length and breadth, then double for the rectangle; multiply side by 4 for the square."
            },
            {
                "question": "Which rectangle with an area of 18 cm² has the smallest perimeter?",
                "options": [
                    "1 cm × 18 cm (P = 38 cm)",
                    "2 cm × 9 cm (P = 22 cm)",
                    "3 cm × 6 cm (P = 18 cm)",
                    "All rectangles of 18 cm² have the same perimeter"
                ],
                "answer": 2,
                "explanation": "As the factors get closer together (3 and 6), the shape becomes more compact, minimizing perimeter to 2 × (3 + 6) = 18 cm.",
                "hint": "Check which factor pair has the smallest sum."
            }
        ]
    },
    {
        "id": 10,
        "title": "Same Perimeter Areas",
        "tagline": "Boundary Optimization • Maximizing Enclosed Area for a Fixed Perimeter",
        "lecture": (
            "Now let us turn the question upside down and investigate the reverse puzzle: do shapes that share the exact same perimeter "
            "enclose the same surface area? Suppose you are given a piece of wire or lace measuring 24 centimetres in total length. "
            "You can bend this wire to form many different rectangles, but the sum of length and breadth must always equal 12 centimetres. "
            "If you make a very thin rectangle with a breadth of 1 centimetre and length of 11 centimetres, its perimeter is 24 centimetres, "
            "but its area is only 11 square centimetres! If you change the dimensions to 2 centimetres by 10 centimetres, the perimeter remains "
            "24 centimetres, but the enclosed area jumps to 20 square centimetres! Make it 3 by 9, and the area climbs to 27 square centimetres! "
            "Keep adjusting until the sides are 6 centimetres by 6 centimetres: a perfect square. The perimeter is still 24 centimetres, "
            "but look at the area: 36 square centimetres! That is over three times the area of the 1 by 11 rectangle! For any given fixed perimeter, "
            "a square always encloses the maximum possible rectangular area, a principle used by farmers, architects, and designers worldwide."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Perimeter Optimization Rule</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Given a fixed perimeter, as length and breadth become closer to equal, the enclosed area increases until it reaches its <strong>maximum in a square</strong>!
        </p>
    </div>

    <div class="overflow-hidden border border-slate-700 rounded-xl bg-slate-900/80">
        <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-slate-800 text-slate-200 font-semibold uppercase tracking-wider">
                <tr>
                    <th class="p-3">Dimensions (L × B)</th>
                    <th class="p-3">Sum (L + B)</th>
                    <th class="p-3">Perimeter (cm)</th>
                    <th class="p-3">Enclosed Area (cm²)</th>
                    <th class="p-3">Efficiency</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono">
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">11 cm × 1 cm</td>
                    <td class="p-3">12 cm</td>
                    <td class="p-3 text-cyan-400">24 cm</td>
                    <td class="p-3 text-rose-400 font-bold">11 cm²</td>
                    <td class="p-3 text-slate-400">Lowest area (skinny)</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">10 cm × 2 cm</td>
                    <td class="p-3">12 cm</td>
                    <td class="p-3 text-cyan-400">24 cm</td>
                    <td class="p-3 text-amber-400 font-bold">20 cm²</td>
                    <td class="p-3 text-slate-400">Moderate area</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">9 cm × 3 cm</td>
                    <td class="p-3">12 cm</td>
                    <td class="p-3 text-cyan-400">24 cm</td>
                    <td class="p-3 text-yellow-400 font-bold">27 cm²</td>
                    <td class="p-3 text-slate-400">Substantial area</td>
                </tr>
                <tr class="hover:bg-slate-800/40 bg-emerald-950/30">
                    <td class="p-3 text-emerald-300 font-bold">6 cm × 6 cm (Square)</td>
                    <td class="p-3">12 cm</td>
                    <td class="p-3 text-cyan-400">24 cm</td>
                    <td class="p-3 text-emerald-400 font-bold">36 cm²</td>
                    <td class="p-3 text-emerald-300 font-bold">★ Maximum Area!</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A string of length 20 cm is bent into different rectangles. What is the maximum area that can be enclosed?",
                "options": [
                    "25 cm² (when shaped as a 5 cm × 5 cm square)",
                    "24 cm² (when shaped as a 6 cm × 4 cm rectangle)",
                    "9 cm² (when shaped as a 9 cm × 1 cm rectangle)",
                    "20 cm² (when shaped as a 10 cm × 2 cm rectangle)"
                ],
                "answer": 0,
                "explanation": "With P = 20 cm, L + B = 10 cm. The maximum area occurs when L = B = 5 cm (a square), giving 5 × 5 = 25 cm².",
                "hint": "Divide the perimeter by 4 to find the side of the optimal square."
            },
            {
                "question": "If two rectangles have the exact same perimeter of 16 cm, must their areas be equal?",
                "options": [
                    "No, their areas can differ (e.g., 7 cm × 1 cm gives 7 cm², while 4 cm × 4 cm gives 16 cm²)",
                    "Yes, shapes with equal perimeters always have identical areas",
                    "No, but the area of any rectangle with P = 16 cm must always be at least 20 cm²",
                    "Yes, because both require the exact same length of boundary wire"
                ],
                "answer": 0,
                "explanation": "Different factor pairs with the same sum give different products. 7 × 1 = 7 cm², but 4 × 4 = 16 cm².",
                "hint": "Think about a thin ribbon rectangle compared to a square."
            }
        ]
    },
    {
        "id": 11,
        "title": "Array Multiplication",
        "tagline": "From Counting to Multiplication • The Row-Column Array Structure of Area",
        "lecture": (
            "Counting every single unit square one by one is wonderful for small shapes, but imagine counting thousands of squares to measure "
            "a playground or house floor! Fortunately, rectangles have an elegant mathematical property: their unit squares are arranged "
            "in neat, uniform rows and columns. This organized grid structure allows us to replace slow counting with rapid multiplication! "
            "Suppose a rectangle is 5 centimetres long and 3 centimetres wide. It contains exactly 3 horizontal rows of squares, with each "
            "row containing 5 unit squares. Instead of counting one, two, three all the way to fifteen, we simply multiply the number of rows "
            "by the number of squares in each row: 3 times 5 equals 15! We can also view it vertically as 5 vertical columns, each containing "
            "3 unit squares: 5 times 3 equals 15! This powerful row-column array model connects basic arithmetic multiplication directly and visually to two-dimensional geometric area. Whether you "
            "are laying bathroom tiles, assembling quilt patches, planting orderly tomato beds in an agricultural field, or designing pixel "
            "arrays on computer screens, the total count of squares is always the product of rows and columns, unlocking rapid spatial "
            "calculation without tedious manual counting."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Array Multiplication Model</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            In any rectangular grid, unit squares align in uniform rows and columns:
            <span class="text-amber-300 font-bold">Total Area = Number of Rows × Number of Columns</span>.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Row Perspective</span>
            <div class="mt-2 text-sm text-slate-300">
                <p>3 horizontal rows</p>
                <p class="text-xs text-slate-400 mt-1">Each row contains 5 unit squares:</p>
                <div class="mt-2 p-2 bg-slate-900/80 rounded border border-slate-700 font-mono text-cyan-300 font-bold">
                    5 + 5 + 5 = 3 × 5 = 15 cm²
                </div>
            </div>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Column Perspective</span>
            <div class="mt-2 text-sm text-slate-300">
                <p>5 vertical columns</p>
                <p class="text-xs text-slate-400 mt-1">Each column contains 3 unit squares:</p>
                <div class="mt-2 p-2 bg-slate-900/80 rounded border border-slate-700 font-mono text-indigo-300 font-bold">
                    3 + 3 + 3 + 3 + 3 = 5 × 3 = 15 cm²
                </div>
            </div>
        </div>
    </div>

    <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl flex items-center justify-between text-xs">
        <span class="text-amber-300 font-bold">Commutative Property:</span>
        <span class="text-slate-300 font-mono">3 × 5 = 5 × 3 = 15 cm²</span>
        <span class="text-slate-400">Rotating the rectangle does not alter its area!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A chocolate bar has 4 rows of squares with 6 squares in each row. What is the total area in squares?",
                "options": [
                    "24 squares (4 × 6)",
                    "20 squares (4 + 6 + 4 + 6)",
                    "10 squares (4 + 6)",
                    "36 squares (6 × 6)"
                ],
                "answer": 0,
                "explanation": "Total squares = Rows × Columns = 4 × 6 = 24 squares. (Notice that 20 is the perimeter, not the area!).",
                "hint": "Multiply the number of rows by the number of squares in each row."
            },
            {
                "question": "A floor is tiled with 7 rows of 8 tiles each. How many tiles are on the floor in total?",
                "options": [
                    "56 tiles",
                    "30 tiles",
                    "15 tiles",
                    "64 tiles"
                ],
                "answer": 0,
                "explanation": "Total tiles = 7 × 8 = 56 tiles.",
                "hint": "Use multiplication table of 7 and 8."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rectangle Formulas",
        "tagline": "Mastering the Equations • Area = Length × Breadth and Perimeter = 2 × (L + B)",
        "lecture": (
            "From the row and column array model, we can now state the two foundational formulas that govern every rectangle in mathematics. "
            "First, the area formula: the number of columns corresponds to the length of the rectangle, and the number of rows corresponds "
            "to its breadth or width. Therefore, the area of any rectangle is calculated by multiplying its length by its breadth: "
            "Area equals Length times Breadth! For example, a rectangle with length 8 centimetres and breadth 5 centimetres has an area of "
            "8 times 5, which equals 40 square centimetres. Second, the perimeter formula: to traverse the outer border of a rectangle, "
            "you walk along its length, down its breadth, back along its opposite length, and up its opposite breadth. Since there are "
            "two lengths and two breadths, the perimeter equals two times the length plus two times the breadth, or more elegantly: "
            "Perimeter equals 2 times the sum of Length plus Breadth! For our 8 by 5 rectangle, the perimeter is 2 times 8 plus 5, "
            "which is 2 times 13, giving 26 centimetres. Always remember the distinction: perimeter measures outer boundary in centimetres, "
            "while area measures flat surface coverage in square centimetres!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Area Card -->
        <div class="bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Surface Coverage</span>
                <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded font-mono">2-Dimensional</span>
            </div>
            <h4 class="text-white font-extrabold text-lg">Area of Rectangle</h4>
            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-indigo-500/30 text-center font-mono">
                <span class="text-amber-400 text-lg font-black">Area = Length × Breadth</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Measures square units enclosed inside. Units: cm², m², km².
            </p>
        </div>

        <!-- Perimeter Card -->
        <div class="bg-gradient-to-br from-rose-950/60 to-slate-900 border border-rose-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Boundary Length</span>
                <span class="text-xs bg-rose-500/20 text-rose-300 px-2 py-0.5 rounded font-mono">1-Dimensional</span>
            </div>
            <h4 class="text-white font-extrabold text-lg">Perimeter of Rectangle</h4>
            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-rose-500/30 text-center font-mono">
                <span class="text-emerald-400 text-lg font-black">Perimeter = 2 × (L + B)</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Measures total outer boundary length. Units: cm, m, km.
            </p>
        </div>
    </div>

    <!-- Comparative Example -->
    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3 text-xs">
        <span class="text-slate-400 uppercase tracking-wider font-semibold">Worked Example: L = 8 cm, B = 5 cm</span>
        <div class="mt-2 grid grid-cols-2 gap-3 text-center font-mono">
            <div class="bg-slate-800 p-2 rounded border border-indigo-500/30 text-indigo-300">
                Area = 8 × 5 = <strong class="text-white">40 cm²</strong>
            </div>
            <div class="bg-slate-800 p-2 rounded border border-rose-500/30 text-rose-300">
                Perimeter = 2 × (8 + 5) = <strong class="text-white">26 cm</strong>
            </div>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A rectangular rug has a length of 7 m and a breadth of 4 m. What are its perimeter and area?",
                "options": [
                    "Perimeter = 22 m; Area = 28 m²",
                    "Perimeter = 28 m; Area = 22 m²",
                    "Perimeter = 11 m; Area = 28 m²",
                    "Perimeter = 44 m; Area = 56 m²"
                ],
                "answer": 0,
                "explanation": "P = 2 × (7 + 4) = 2 × 11 = 22 m. Area = 7 × 4 = 28 m².",
                "hint": "Perimeter is 2 × (L + B); Area is L × B."
            },
            {
                "question": "If a rectangle has an area of 48 cm² and a length of 8 cm, what is its breadth?",
                "options": [
                    "6 cm (since 48 ÷ 8 = 6)",
                    "40 cm (since 48 - 8 = 40)",
                    "12 cm (since 48 ÷ 4 = 12)",
                    "8 cm (since all rectangles have equal sides)"
                ],
                "answer": 0,
                "explanation": "Breadth = Area ÷ Length = 48 ÷ 8 = 6 cm. Check: 8 × 6 = 48 cm².",
                "hint": "Divide the total area by the given length."
            }
        ]
    },
    {
        "id": 13,
        "title": "Square Formulas",
        "tagline": "Equilateral Symmetry • Area = Side × Side and Perimeter = 4 × Side",
        "lecture": (
            "A square is a special, wonderfully symmetrical rectangle where all four sides are exactly equal in length! "
            "Because the length equals the breadth, the formulas for the perimeter and area of a square become even simpler and more elegant. "
            "Let us call the length of any side 's'. To find the perimeter of a square, we simply add the four equal sides: side plus side "
            "plus side plus side, which is four times the side length: Perimeter equals 4 times Side! For a square napkin with sides of "
            "6 centimetres, the perimeter of decorative border lace needed is 4 times 6, which equals 24 centimetres. To find the area of "
            "the square, we apply our rectangle formula of length times breadth; but since length and breadth are both equal to 's', "
            "the formula becomes side times side: Area equals Side times Side! For our 6 centimetre napkin, the surface area covered is "
            "6 times 6, which equals 36 square centimetres. Notice the power of units: the perimeter is measured in linear centimetres, "
            "whereas the area is measured in square centimetres! Knowing these formulas allows you to calculate both border trims and surface "
            "materials for tiles, gameboards, handkerchiefs, and picture frames in an instant."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Square Area -->
        <div class="bg-gradient-to-br from-emerald-950/60 to-slate-900 border border-emerald-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Surface Area</span>
                <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded font-mono">s²</span>
            </div>
            <h4 class="text-white font-extrabold text-lg">Area of a Square</h4>
            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-emerald-500/30 text-center font-mono">
                <span class="text-emerald-300 text-lg font-black">Area = Side × Side</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Multiply the side length by itself. Example: 6 cm × 6 cm = 36 cm².
            </p>
        </div>

        <!-- Square Perimeter -->
        <div class="bg-gradient-to-br from-cyan-950/60 to-slate-900 border border-cyan-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Boundary Length</span>
                <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded font-mono">4s</span>
            </div>
            <h4 class="text-white font-extrabold text-lg">Perimeter of a Square</h4>
            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-cyan-500/30 text-center font-mono">
                <span class="text-cyan-300 text-lg font-black">Perimeter = 4 × Side</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Add all 4 identical sides together. Example: 4 × 6 cm = 24 cm.
            </p>
        </div>
    </div>

    <!-- Quick Reference Comparison -->
    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3">
        <h5 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Square Dimensions Quick Guide</h5>
        <div class="grid grid-cols-4 gap-2 text-center text-xs font-mono">
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">Side = 3 cm</div>
                <div class="text-cyan-400 mt-1">P = 12 cm</div>
                <div class="text-emerald-400">A = 9 cm²</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">Side = 5 cm</div>
                <div class="text-cyan-400 mt-1">P = 20 cm</div>
                <div class="text-emerald-400">A = 25 cm²</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">Side = 7 cm</div>
                <div class="text-cyan-400 mt-1">P = 28 cm</div>
                <div class="text-emerald-400">A = 49 cm²</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">Side = 10 cm</div>
                <div class="text-cyan-400 mt-1">P = 40 cm</div>
                <div class="text-emerald-400">A = 100 cm²</div>
            </div>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A square chessboard has sides of 30 cm. What is its perimeter and area?",
                "options": [
                    "Perimeter = 120 cm; Area = 900 cm²",
                    "Perimeter = 60 cm; Area = 900 cm²",
                    "Perimeter = 120 cm; Area = 60 cm²",
                    "Perimeter = 300 cm; Area = 1200 cm²"
                ],
                "answer": 0,
                "explanation": "P = 4 × 30 = 120 cm. Area = 30 × 30 = 900 cm².",
                "hint": "Perimeter is 4 times the side; Area is side multiplied by side."
            },
            {
                "question": "If the perimeter of a square garden is 36 metres, what is the area of the garden?",
                "options": [
                    "81 m² (side = 36 ÷ 4 = 9 m; Area = 9 × 9 = 81 m²)",
                    "144 m² (side = 12 m; Area = 12 × 12 = 144 m²)",
                    "36 m² (side = 6 m; Area = 6 × 6 = 36 m²)",
                    "72 m² (side = 9 m; Area = 9 × 8 = 72 m²)"
                ],
                "answer": 0,
                "explanation": "First find the side: 36 ÷ 4 = 9 m. Then find the area: 9 × 9 = 81 m².",
                "hint": "Divide perimeter by 4 to get side, then square it."
            }
        ]
    },
    {
        "id": 14,
        "title": "Real-World Measurement",
        "tagline": "Practical Applications • Sizing Classroom Floors, Notebooks, and Blackboards",
        "lecture": (
            "Mathematics truly comes alive when we apply perimeter and area to everyday real-world objects around us! "
            "Depending on the physical size of what we are measuring, we choose appropriate standard metric units. For small handheld objects "
            "like a postage stamp, an eraser, or a mobile phone screen, we measure perimeter in centimetres and area in square centimetres. "
            "For example, a student notebook cover measuring 20 centimetres by 15 centimetres has an area of 300 square centimetres. "
            "However, when measuring larger architectural spaces such as our classroom floor, a basketball court, or an outdoor garden, "
            "centimetres are far too small! Instead, we measure boundaries in metres and floor surfaces in square metres. "
            "A square metre represents the area of a square whose sides are each 1 metre long. If our classroom floor measures 8 metres long "
            "and 6 metres wide, its perimeter for skirting boards is 2 times 8 plus 6, which equals 28 metres, while the floor area for "
            "laying ceramic floor tiles is 8 times 6, which equals 48 square metres! From buying chalkboard paint for school blackboards to "
            "purchasing wire fencing for agricultural fields, mastering real-world dimensions ensures accurate planning and zero wasted material."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-violet-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Scale & Unit Selection</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Always match the metric unit to the physical scale of the object:
            <span class="text-amber-300 font-bold">cm and cm²</span> for desk objects;
            <span class="text-emerald-300 font-bold">m and m²</span> for rooms and fields!
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Notebook Cover</span>
            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">
                <div>Dimensions: 20 cm × 15 cm</div>
                <div>Perimeter: 2 × (20 + 15) = 70 cm</div>
                <div class="text-cyan-300 font-bold">Area = 300 cm²</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Unit: Square Centimetres (cm²)</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Classroom Blackboard</span>
            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">
                <div>Dimensions: 3 m × 1.5 m</div>
                <div>Perimeter: 2 × (3 + 1.5) = 9 m</div>
                <div class="text-emerald-300 font-bold">Area = 4.5 m²</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Unit: Square Metres (m²)</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Classroom Floor</span>
            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">
                <div>Dimensions: 8 m × 6 m</div>
                <div>Skirting: 2 × (8 + 6) = 28 m</div>
                <div class="text-amber-300 font-bold">Area = 48 m²</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Unit: Square Metres (m²)</p>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400">Remember:</span>
        <span class="text-indigo-300 font-bold font-mono">1 m² = 100 cm × 100 cm = 10,000 cm²</span>
        <span class="text-slate-400">A square metre contains 10,000 square centimetres!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which metric unit is most appropriate for measuring the area of a school football ground?",
                "options": [
                    "Square metres (m²)",
                    "Square centimetres (cm²)",
                    "Centimetres (cm)",
                    "Metres (m)"
                ],
                "answer": 0,
                "explanation": "A football ground is large, so square metres (m²) is the standard unit. (Centimetres are for lengths, not areas!).",
                "hint": "Area requires square units, and large open grounds are measured in metres."
            },
            {
                "question": "A square ludo board has a side length of 40 cm. What is the area of the ludo board?",
                "options": [
                    "1,600 cm²",
                    "160 cm²",
                    "80 cm²",
                    "1,200 cm²"
                ],
                "answer": 0,
                "explanation": "Area = Side × Side = 40 × 40 = 1,600 cm².",
                "hint": "Multiply 40 by 40."
            }
        ]
    },
    {
        "id": 15,
        "title": "Applied Word Problems",
        "tagline": "Real-Life Problem Solving • Fencing Costs, Missing Dimensions, and Composite Surfaces",
        "lecture": (
            "Real-world challenges often require using both perimeter and area formulas together to solve practical questions. "
            "Consider a rectangular agricultural plot measuring 25 metres long and 10 metres wide. A farmer wants to fence the entire plot "
            "with barbed wire that costs 20 rupees per metre. To calculate the total fencing cost, we first find the perimeter: "
            "two times 25 plus 10, which equals 70 metres of fence. Then we multiply 70 metres by 20 rupees, giving a total cost of "
            "1,400 rupees! Notice that fencing goes along the border, so it uses perimeter, not area! Now consider a second problem: "
            "a gardener has a rectangular flowerbed with an area of 72 square metres. The length is known to be 9 metres, but what is its "
            "breadth? Since Area equals Length times Breadth, we divide the area by the length: 72 divided by 9 equals 8 metres! "
            "For composite L-shaped or T-shaped regions, you can split the complex shape into two simpler rectangles, calculate the area of "
            "each rectangle separately, and then add their areas together. Always identify whether the practical question asks for boundary "
            "length or surface coverage before choosing your mathematical formulas and problem-solving strategy."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Problem 1: Fencing Cost -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Type A: Boundary Cost</span>
            <h5 class="text-white font-bold text-sm mt-1">Fencing a 25 m × 10 m Field</h5>
            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 rounded border border-slate-700">
                <p>1. Perimeter = 2 × (25 + 10) = <span class="text-cyan-400 font-bold">70 m</span></p>
                <p>2. Rate = ₹20 per metre</p>
                <p>3. Cost = 70 × 20 = <span class="text-emerald-400 font-bold">₹1,400</span></p>
            </div>
            <p class="text-xs text-slate-400 mt-2">Rule: Fencing = Perimeter × Rate per unit length.</p>
        </div>

        <!-- Problem 2: Missing Dimension -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Type B: Missing Side</span>
            <h5 class="text-white font-bold text-sm mt-1">Flowerbed: Area = 72 m², Length = 9 m</h5>
            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 rounded border border-slate-700">
                <p>1. Area = Length × Breadth</p>
                <p>2. 72 = 9 × Breadth</p>
                <p>3. Breadth = 72 ÷ 9 = <span class="text-indigo-400 font-bold">8 m</span></p>
            </div>
            <p class="text-xs text-slate-400 mt-2">Rule: Breadth = Area ÷ Length (or Length = Area ÷ Breadth).</p>
        </div>
    </div>

    <!-- Composite Shapes Tip -->
    <div class="bg-gradient-to-r from-teal-950/40 to-slate-900 border border-teal-500/30 rounded-xl p-3 text-xs">
        <span class="text-teal-300 font-bold uppercase tracking-wider">Composite Shapes Tip:</span>
        <span class="text-slate-300 ml-2">
            To find the area of an L-shape, partition it with a dotted line into two rectangles, find each area, and add them together!
        </span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A square courtyard of side 15 m needs fencing. If wire costs ₹10 per metre, what is the total fencing cost?",
                "options": [
                    "₹600 (Perimeter = 60 m; 60 × 10 = ₹600)",
                    "₹2,250 (Area = 225 m²; 225 × 10 = ₹2,250)",
                    "₹150 (15 × 10 = ₹150)",
                    "₹300 (Perimeter = 30 m; 30 × 10 = ₹300)"
                ],
                "answer": 0,
                "explanation": "Fencing requires perimeter: P = 4 × 15 = 60 m. Total cost = 60 × ₹10 = ₹600. (Do not confuse area with fencing!).",
                "hint": "Find the perimeter of the square first, then multiply by ₹10."
            },
            {
                "question": "A rectangular swimming pool has an area of 120 m² and a breadth of 8 m. What is its length?",
                "options": [
                    "15 m (120 ÷ 8 = 15)",
                    "112 m (120 - 8 = 112)",
                    "960 m (120 × 8 = 960)",
                    "12 m (120 ÷ 10 = 12)"
                ],
                "answer": 0,
                "explanation": "Length = Area ÷ Breadth = 120 ÷ 8 = 15 m. Check: 15 × 8 = 120 m².",
                "hint": "Divide total area by breadth."
            }
        ]
    },
    {
        "id": 16,
        "title": "Perimeter Dice Game",
        "tagline": "Two-Player Strategic Math Game • Roll, Append Square Tiles, and Race to Perimeter 24",
        "lecture": (
            "To celebrate everything we have discovered about perimeter and area, class five students play the exciting Perimeter Building "
            "Dice Game! This thrilling two-player game brings geometry to life through playful strategy. Players take turns rolling a standard "
            "six-sided die. When it is your turn, the number rolled indicates how many unit square tiles you must add to your expanding geometric "
            "creation. Each new tile must connect firmly along at least one complete edge of an existing tile: no diagonal corners allowed! "
            "After attaching your new tiles, you must recalculate the total outer perimeter of your shape. Here is the strategic twist: "
            "if you attach your tiles in a long straight line, each new tile exposes two new border edges, causing your perimeter to surge! "
            "However, if you tuck tiles snugly into inside corners, edges touch and cancel out, keeping your perimeter compact. The goal of the "
            "game is to be the first player to construct a valid connected shape whose outer boundary perimeter reaches exactly 24 units! "
            "Through this hands-on interactive gameplay, you develop sharp tactical intuition for how edge-sharing transforms boundary "
            "perimeter while simultaneously growing the total enclosed area and surface coverage on the game grid."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-yellow-900/30 to-amber-900/40 border border-yellow-500/30 rounded-xl p-4">
        <h4 class="text-yellow-300 font-bold text-sm tracking-wider uppercase mb-1">Game Rules & Strategy</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Players take turns rolling a die, adding that number of unit tiles edge-to-edge, and updating their shape's outer perimeter.
            <span class="text-emerald-300 font-bold">Goal: Reach an exact perimeter of 24 units!</span>
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Perimeter Expansion Tactic</span>
            <h5 class="text-white font-bold text-sm mt-1">Linear Extension</h5>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Adding tiles in a straight chain exposes 2 new exterior edges per tile (+2 to perimeter). Great for surging toward 24 quickly!
            </p>
            <div class="mt-2 text-xs font-mono text-rose-300 bg-slate-900/80 p-2 rounded border border-rose-500/30">
                1 tile: P=4 ➔ 2 tiles: P=6 ➔ 3 tiles: P=8
            </div>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Perimeter Control Tactic</span>
            <h5 class="text-white font-bold text-sm mt-1">Corner Filling</h5>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Tucking a tile into an inside L-corner touches 2 existing edges, adding 0 net edges to the outer perimeter (+0 change)!
            </p>
            <div class="mt-2 text-xs font-mono text-cyan-300 bg-slate-900/80 p-2 rounded border border-cyan-500/30">
                Corner tuck: +1 tile, +0 to perimeter!
            </div>
        </div>
    </div>

    <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-xl flex items-center justify-between text-xs">
        <span class="text-indigo-300 font-bold">Rule Check:</span>
        <span class="text-slate-300">Tiles must touch along whole edges (no vertex-only diagonal contacts allowed).</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If you add 1 square tile to the end of a straight strip of squares, how much does the perimeter increase?",
                "options": [
                    "By 2 units",
                    "By 4 units",
                    "By 1 unit",
                    "By 0 units"
                ],
                "answer": 0,
                "explanation": "The new tile has 4 edges. 1 edge connects to the existing strip (hidden), 1 edge covers an existing boundary edge, and 3 edges become new boundary. Net change = +3 - 1 = +2 units.",
                "hint": "Count how many new outer sides are exposed minus the edge that got covered."
            },
            {
                "question": "If you place a unit tile into an inside 'L' corner where 2 edges touch existing tiles, how does the perimeter change?",
                "options": [
                    "Perimeter does not change (+0 units)",
                    "Perimeter increases by 2 units",
                    "Perimeter decreases by 2 units",
                    "Perimeter increases by 4 units"
                ],
                "answer": 0,
                "explanation": "2 edges of the new tile touch the existing shape (replacing 2 boundary edges) and 2 edges become new boundary. Net perimeter change = +2 - 2 = 0!",
                "hint": "Two edges are covered, and two new outer edges are created."
            }
        ]
    }
]

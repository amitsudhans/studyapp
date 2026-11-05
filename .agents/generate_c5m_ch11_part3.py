# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
Part 3 Data: Slides 17 to 20 (40 Mastery Quiz Questions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Boundary Lengths & Regular Polygons",
        "lecture": "Welcome to Mastery Challenge 1. In this interactive session, you will test your understanding of boundary lengths, perimeter calculations, and the geometry of regular polygons.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 to-indigo-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your skills on finding outer boundaries, sum of all sides, regular polygons, and drawing rectangles with fixed perimeters. Solve all 10 questions to unlock the next level!
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "What is the mathematical definition of perimeter?",
                "options": [
                    "The total length of the continuous outer boundary of a closed 2D shape",
                    "The total flat surface area enclosed inside a shape",
                    "The number of square units required to cover a shape completely",
                    "The product of all side lengths of a polygon"
                ],
                "answer": 0,
                "hint": "Think about the lace ribbon running around grandmother's quilt.",
                "explanation": "Perimeter is strictly a 1D measurement of the outer boundary length around a closed shape.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. <strong>Perimeter</strong> comes from Greek <em>peri</em> (around) and <em>metron</em> (measure).</p>
    <p>2. It measures the total distance traveled along the outer border or edge of a closed shape.</p>
    <p>3. Surface coverage inside is called <em>area</em>, while outer edge length is called <em>perimeter</em>.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "Grandmother's quilt is 2 metres long and 1.5 metres wide. How many metres of lace border ribbon are needed to trim all four edges?",
                "options": [
                    "7 metres",
                    "3 metres",
                    "3.5 metres",
                    "14 metres"
                ],
                "answer": 0,
                "hint": "Add length and breadth, then double it: P = 2 × (L + B).",
                "explanation": "P = 2 × (2 m + 1.5 m) = 2 × 3.5 m = 7 metres.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Length (L) = 2 m, Breadth (B) = 1.5 m.</p>
    <p>2. Formula: Perimeter = 2 × (L + B).</p>
    <p>3. P = 2 × (2 + 1.5) = 2 × 3.5 = <strong>7 metres</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "An equilateral triangle has sides measuring 8 cm each. What is its perimeter?",
                "options": [
                    "24 cm",
                    "16 cm",
                    "32 cm",
                    "64 cm"
                ],
                "answer": 0,
                "hint": "An equilateral triangle has 3 equal sides.",
                "explanation": "Perimeter = 3 × side = 3 × 8 cm = 24 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Number of sides in an equilateral triangle = 3.</p>
    <p>2. Side length s = 8 cm.</p>
    <p>3. Perimeter = 3 × 8 = <strong>24 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "A regular hexagon has a perimeter of 42 cm. What is the length of each side?",
                "options": [
                    "7 cm",
                    "6 cm",
                    "8 cm",
                    "14 cm"
                ],
                "answer": 0,
                "hint": "A regular hexagon has 6 equal sides: Side = Perimeter ÷ 6.",
                "explanation": "Side = 42 cm ÷ 6 = 7 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Regular hexagon has 6 equal sides.</p>
    <p>2. Formula: Side = Perimeter ÷ 6.</p>
    <p>3. Side = 42 ÷ 6 = <strong>7 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "Which formula gives the perimeter of a regular pentagon with side length s?",
                "options": [
                    "5 × s",
                    "4 × s",
                    "s × s",
                    "6 × s"
                ],
                "answer": 0,
                "hint": "A pentagon has 5 sides.",
                "explanation": "A regular pentagon has 5 equal sides, so Perimeter = 5 × s.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. A pentagon is a 5-sided polygon.</p>
    <p>2. In a regular pentagon, all 5 sides are equal.</p>
    <p>3. Perimeter = s + s + s + s + s = <strong>5 × s</strong>.</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "If you want to draw a rectangle with a perimeter of 26 cm, what must the sum of its length and breadth be?",
                "options": [
                    "13 cm (half of 26 cm)",
                    "26 cm",
                    "52 cm",
                    "6.5 cm"
                ],
                "answer": 0,
                "hint": "Perimeter = 2 × (L + B), so L + B = Perimeter ÷ 2.",
                "explanation": "Sum of length and breadth = 26 ÷ 2 = 13 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Formula: P = 2 × (L + B).</p>
    <p>2. L + B = P ÷ 2.</p>
    <p>3. L + B = 26 ÷ 2 = <strong>13 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "Which of the following whole-number pairs can form a rectangle with a perimeter of 18 cm?",
                "options": [
                    "7 cm and 2 cm",
                    "6 cm and 4 cm",
                    "9 cm and 9 cm",
                    "10 cm and 8 cm"
                ],
                "answer": 0,
                "hint": "The sum of L and B must equal 18 ÷ 2 = 9 cm.",
                "explanation": "7 + 2 = 9 cm, giving P = 2 × (7 + 2) = 18 cm. (6 + 4 = 10; 9 + 9 = 18).",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Target perimeter = 18 cm, so L + B = 18 ÷ 2 = 9 cm.</p>
    <p>2. Check 7 + 2: 7 + 2 = 9 cm. P = 2 × 9 = 18 cm (Valid!).</p>
    <p>3. Check 6 + 4: 6 + 4 = 10 cm. P = 20 cm (Invalid).</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "A square photo frame has a side of 12 cm. What is the length of wooden moulding required to make the frame?",
                "options": [
                    "48 cm",
                    "24 cm",
                    "144 cm",
                    "36 cm"
                ],
                "answer": 0,
                "hint": "A square frame has 4 equal sides.",
                "explanation": "Perimeter = 4 × side = 4 × 12 cm = 48 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Wooden moulding forms the outer border (perimeter).</p>
    <p>2. Square perimeter = 4 × Side.</p>
    <p>3. P = 4 × 12 = <strong>48 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "A triangular park has sides of 25 m, 30 m, and 35 m. What distance does an athlete run in completing one full round of the park?",
                "options": [
                    "90 m",
                    "60 m",
                    "80 m",
                    "105 m"
                ],
                "answer": 0,
                "hint": "Add all three sides: 25 + 30 + 35.",
                "explanation": "Perimeter = 25 + 30 + 35 = 90 metres.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Running one round of a park covers its perimeter.</p>
    <p>2. Perimeter = Side 1 + Side 2 + Side 3.</p>
    <p>3. P = 25 + 30 + 35 = <strong>90 m</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "A regular octagon has an outer perimeter of 64 cm. What is the length of one side?",
                "options": [
                    "8 cm",
                    "7 cm",
                    "6 cm",
                    "16 cm"
                ],
                "answer": 0,
                "hint": "An octagon has 8 equal sides: Side = 64 ÷ 8.",
                "explanation": "Side = 64 cm ÷ 8 = 8 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. An octagon has 8 sides.</p>
    <p>2. For a regular octagon, all 8 sides are equal.</p>
    <p>3. Side = 64 ÷ 8 = <strong>8 cm</strong>.</p>
</div>
"""
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Area, Tiling & Grid Estimation",
        "lecture": "Welcome to Mastery Challenge 2. In this round, you will test your knowledge of tessellation, unit squares, grid counting rules, and estimating irregular handprints and leaves.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 to-emerald-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your understanding of surface coverage, why circles leave gaps, unit square definitions, counting whole and partial squares, and palm/leaf area estimation.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "What is meant by the geometric term 'tessellation'?",
                "options": [
                    "Covering a flat surface completely with shapes without leaving any gaps or overlaps",
                    "Measuring the outer boundary of a polygon with a ruler",
                    "Drawing a shape that has reflectional symmetry",
                    "Dividing a shape into two equal halves"
                ],
                "answer": 0,
                "hint": "Think about tiling a floor perfectly with square tiles.",
                "explanation": "A tessellation or tiling is covering a plane using geometric shapes without overlaps or empty spaces.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. <strong>Tessellation</strong> means tiling a surface with repeating geometric shapes.</p>
    <p>2. Rule 1: No gaps between tiles.</p>
    <p>3. Rule 2: No overlapping edges.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "Why are circles unable to tessellate a flat surface?",
                "options": [
                    "Because curved boundaries leave empty diamond-shaped gaps between adjacent circles",
                    "Because circles have infinite sides",
                    "Because circles have no area",
                    "Because circles cannot be measured in centimetres"
                ],
                "answer": 0,
                "hint": "Think of placing circular coins next to each other on a table.",
                "explanation": "Curved edges cannot meet edge-to-edge; they leave empty voids (interstices) between circles.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Circular edges curve away from contact points.</p>
    <p>2. When circular coins touch, diamond-shaped gaps are left behind.</p>
    <p>3. Therefore, circles cannot tile a flat plane completely without leaving empty gaps.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "How many half-triangle tiles are needed to cover the same area as 1 full unit square?",
                "options": [
                    "2 half-triangles",
                    "4 half-triangles",
                    "1 half-triangle",
                    "3 half-triangles"
                ],
                "answer": 0,
                "hint": "Cutting a square diagonally produces 2 identical triangles.",
                "explanation": "Two diagonal half-triangles join together to make 1 full unit square.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Cut a 1 cm × 1 cm square diagonally into 2 triangles.</p>
    <p>2. Each triangle has an area of 1/2 cm².</p>
    <p>3. Two half-triangles = 1/2 + 1/2 = <strong>1 unit square</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "What is the area of a square whose sides are each 1 centimetre long?",
                "options": [
                    "1 square centimetre (1 cm²)",
                    "4 centimetres (4 cm)",
                    "2 square centimetres (2 cm²)",
                    "1 centimetre (1 cm)"
                ],
                "answer": 0,
                "hint": "Area = 1 cm × 1 cm.",
                "explanation": "Area of a unit square = 1 cm × 1 cm = 1 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Side s = 1 cm.</p>
    <p>2. Area = s × s = 1 cm × 1 cm = <strong>1 cm²</strong>.</p>
    <p>3. (Note: 4 cm is its perimeter, not its area!).</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "When estimating area on a 1 cm² grid, how do we count a square that is more than half covered by a shape?",
                "options": [
                    "Count it as 1 full square",
                    "Ignore it completely",
                    "Count it as 1/2 square",
                    "Count it as 2 squares"
                ],
                "answer": 0,
                "hint": "The standard rule: full squares = 1, more than half = 1, less than half = 0.",
                "explanation": "Squares more than half covered are rounded up and counted as 1 full square.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Standard Grid Counting Convention:</p>
    <p>• Fully covered: Count as 1.</p>
    <p>• More than half covered: <strong>Count as 1</strong>.</p>
    <p>• Exactly half covered: Count as 1/2 (pair them up).</p>
    <p>• Less than half covered: Ignore (0).</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "A traced shape covers 14 fully enclosed squares and 6 exactly half-covered squares on a 1 cm grid. What is its total area?",
                "options": [
                    "17 cm² (14 + 3)",
                    "20 cm² (14 + 6)",
                    "15 cm² (14 + 1)",
                    "12 cm² (14 - 2)"
                ],
                "answer": 0,
                "hint": "Each pair of half-covered squares equals 1 full square: 6 halves = 3 full squares.",
                "explanation": "Total area = 14 + (6 × 0.5) = 14 + 3 = 17 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Fully covered squares = 14 cm².</p>
    <p>2. Half-covered squares = 6 × 1/2 = 3 cm².</p>
    <p>3. Total Area = 14 + 3 = <strong>17 cm²</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "When tracing a handprint on a 1 cm² grid, which student has the larger handprint?",
                "options": [
                    "Adrit whose handprint covers 52 unit squares",
                    "Preetha whose handprint covers 46 unit squares",
                    "Both handprints have equal surface area",
                    "It cannot be determined without measuring fingers"
                ],
                "answer": 0,
                "hint": "Compare the number of unit squares covered: 52 vs 46.",
                "explanation": "52 cm² > 46 cm², so Adrit has the larger handprint surface area.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Adrit's hand covers 52 square centimetres.</p>
    <p>2. Preetha's hand covers 46 square centimetres.</p>
    <p>3. Since 52 > 46, <strong>Adrit</strong> has the larger handprint.</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "Rank the following leaves in order from smallest to largest surface area: Peepal, Coriander, Mango.",
                "options": [
                    "Coriander < Mango < Peepal",
                    "Peepal < Mango < Coriander",
                    "Mango < Coriander < Peepal",
                    "Peepal < Coriander < Mango"
                ],
                "answer": 0,
                "hint": "A coriander leaflet is tiny; a peepal leaf is very broad.",
                "explanation": "Coriander (~2-4 cm²) < Mango (~25-35 cm²) < Peepal (~65-80 cm²).",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Coriander: small compound leaflet (~3 cm²).</p>
    <p>2. Mango: medium slender leaf (~30 cm²).</p>
    <p>3. Peepal: broad heart-shaped leaf (~70 cm²).</p>
    <p>4. Ascending order: <strong>Coriander < Mango < Peepal</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "If a tabletop is completely covered by 24 identical mathematics textbooks, what is the area of the table in textbook units?",
                "options": [
                    "24 textbook units",
                    "12 textbook units",
                    "48 textbook units",
                    "6 textbook units"
                ],
                "answer": 0,
                "hint": "The area is the number of non-standard units needed to cover the surface.",
                "explanation": "Area = 24 textbook units, because 24 books cover the surface without gaps or overlaps.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. A non-standard unit of area is any consistent object used to tile a surface.</p>
    <p>2. 24 books cover the table surface without gaps.</p>
    <p>3. Table Area = <strong>24 textbook units</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "Why do mathematicians prefer a standard 1 cm² grid over non-standard units like pencil boxes or erasers?",
                "options": [
                    "Because 1 cm² is universally uniform, standardized, and communicates identical sizes across the world",
                    "Because pencil boxes are too heavy to carry",
                    "Because squares are the only shapes that exist",
                    "Because erasers cannot be placed next to each other"
                ],
                "answer": 0,
                "hint": "Think about why standard units were invented.",
                "explanation": "Standard units like cm² ensure universal consistency regardless of who is measuring.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Non-standard units vary in size between brands and individuals.</p>
    <p>2. Standard 1 cm² units are identical across the globe.</p>
    <p>3. They allow reproducible, accurate, and universal measurement.</p>
</div>
"""
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Area vs Perimeter & Rectangle Formulas",
        "lecture": "Welcome to Mastery Challenge 3. In this section, you will evaluate the mathematical relationships between area and perimeter, row-column arrays, and the formulas for rectangles and squares.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 to-pink-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your mastery of fixed area variations, fixed perimeter optimizations, array multiplication, rectangle formulas, and square properties.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "Three rectangles each have an area of 12 cm²: (1 × 12), (2 × 6), and (3 × 4). Which one has the largest perimeter?",
                "options": [
                    "The 1 cm × 12 cm rectangle (P = 26 cm)",
                    "The 2 cm × 6 cm rectangle (P = 16 cm)",
                    "The 3 cm × 4 cm rectangle (P = 14 cm)",
                    "All three have identical perimeters"
                ],
                "answer": 0,
                "hint": "The most elongated, stretched-out shape has the largest perimeter.",
                "explanation": "P for 1 × 12 = 2 × (1 + 12) = 26 cm, which is greater than 16 cm and 14 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. P(1 × 12) = 2 × (1 + 12) = 26 cm.</p>
    <p>2. P(2 × 6) = 2 × (2 + 6) = 16 cm.</p>
    <p>3. P(3 × 4) = 2 × (3 + 4) = 14 cm.</p>
    <p>4. The long thin strip <strong>1 cm × 12 cm</strong> has the largest perimeter (26 cm).</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "For a fixed perimeter of 24 cm, which rectangular shape encloses the maximum possible area?",
                "options": [
                    "A 6 cm × 6 cm square (Area = 36 cm²)",
                    "An 8 cm × 4 cm rectangle (Area = 32 cm²)",
                    "A 10 cm × 2 cm rectangle (Area = 20 cm²)",
                    "An 11 cm × 1 cm rectangle (Area = 11 cm²)"
                ],
                "answer": 0,
                "hint": "A square maximizes area for any fixed perimeter.",
                "explanation": "Among all rectangles with P = 24 cm, the 6 × 6 square achieves maximum area: 36 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Fixed perimeter P = 24 cm ➔ L + B = 12 cm.</p>
    <p>2. Check products: 11 × 1 = 11, 10 × 2 = 20, 8 × 4 = 32, 6 × 6 = 36.</p>
    <p>3. The <strong>6 cm × 6 cm square</strong> maximizes area at 36 cm².</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "A grid has 6 horizontal rows and 9 vertical columns of unit squares. What is the total area?",
                "options": [
                    "54 cm²",
                    "30 cm²",
                    "15 cm²",
                    "60 cm²"
                ],
                "answer": 0,
                "hint": "Multiply rows by columns: 6 × 9.",
                "explanation": "Total Area = Rows × Columns = 6 × 9 = 54 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Number of rows = 6.</p>
    <p>2. Number of columns = 9.</p>
    <p>3. Area = 6 × 9 = <strong>54 cm²</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "What is the area of a rectangular classroom blackboard measuring 4 metres in length and 2 metres in breadth?",
                "options": [
                    "8 m²",
                    "12 m",
                    "16 m²",
                    "6 m²"
                ],
                "answer": 0,
                "hint": "Area = Length × Breadth = 4 × 2.",
                "explanation": "Area = 4 m × 2 m = 8 m².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Length = 4 m, Breadth = 2 m.</p>
    <p>2. Formula: Area = Length × Breadth.</p>
    <p>3. Area = 4 × 2 = <strong>8 m²</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "What is the perimeter of a rectangular rug measuring 9 metres long and 5 metres wide?",
                "options": [
                    "28 metres",
                    "45 square metres",
                    "14 metres",
                    "56 metres"
                ],
                "answer": 0,
                "hint": "P = 2 × (L + B) = 2 × (9 + 5).",
                "explanation": "Perimeter = 2 × (9 + 5) = 2 × 14 = 28 m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Length = 9 m, Breadth = 5 m.</p>
    <p>2. Perimeter = 2 × (9 + 5) = 2 × 14 = <strong>28 m</strong>.</p>
    <p>3. (Note: 45 m² is its area, not its perimeter!).</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "A square garden has sides of 9 metres. What are its perimeter and area?",
                "options": [
                    "Perimeter = 36 m; Area = 81 m²",
                    "Perimeter = 81 m; Area = 36 m²",
                    "Perimeter = 18 m; Area = 81 m²",
                    "Perimeter = 36 m; Area = 18 m²"
                ],
                "answer": 0,
                "hint": "P = 4 × 9; Area = 9 × 9.",
                "explanation": "Perimeter = 4 × 9 = 36 m. Area = 9 × 9 = 81 m².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Side s = 9 m.</p>
    <p>2. Perimeter = 4 × s = 4 × 9 = <strong>36 m</strong>.</p>
    <p>3. Area = s × s = 9 × 9 = <strong>81 m²</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "If a square has an area of 49 cm², what is its perimeter?",
                "options": [
                    "28 cm",
                    "14 cm",
                    "49 cm",
                    "36 cm"
                ],
                "answer": 0,
                "hint": "First find the side: what number multiplied by itself gives 49? Then multiply by 4.",
                "explanation": "Side = 7 cm (since 7 × 7 = 49). Perimeter = 4 × 7 = 28 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Area = s × s = 49 cm² ➔ s = 7 cm.</p>
    <p>2. Perimeter = 4 × s = 4 × 7 = <strong>28 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "A rectangle has an area of 60 cm² and a length of 12 cm. What is its breadth?",
                "options": [
                    "5 cm",
                    "48 cm",
                    "10 cm",
                    "6 cm"
                ],
                "answer": 0,
                "hint": "Breadth = Area ÷ Length = 60 ÷ 12.",
                "explanation": "Breadth = 60 ÷ 12 = 5 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Area = Length × Breadth.</p>
    <p>2. 60 = 12 × Breadth.</p>
    <p>3. Breadth = 60 ÷ 12 = <strong>5 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "If you double both the length and breadth of a rectangle, what happens to its area?",
                "options": [
                    "The area becomes 4 times as large",
                    "The area doubles (becomes 2 times)",
                    "The area remains the same",
                    "The area increases by 2 cm²"
                ],
                "answer": 0,
                "hint": "Original: L × B. New: (2 × L) × (2 × B) = 4 × (L × B).",
                "explanation": "Doubling both dimensions multiplies the area by 2 × 2 = 4 times.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Original Area = L × B.</p>
    <p>2. New Area = (2L) × (2B) = 4 × (L × B).</p>
    <p>3. The area increases by a factor of <strong>4</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "Which of the following statements is ALWAYS true?",
                "options": [
                    "Perimeter is measured in linear units (cm, m), while area is measured in square units (cm², m²)",
                    "Two shapes with the same area must always have the exact same perimeter",
                    "Two shapes with the same perimeter must always have the exact same area",
                    "A longer rectangle always has a larger area than a square"
                ],
                "answer": 0,
                "hint": "Consider the difference between 1D boundary length and 2D surface coverage.",
                "explanation": "Perimeter is 1-dimensional (cm, m); Area is 2-dimensional (cm², m²).",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Perimeter measures distance around boundary ➔ linear units (cm, m).</p>
    <p>2. Area measures surface coverage ➔ square units (cm², m²).</p>
    <p>3. Shapes can share area with different perimeters, and vice versa.</p>
</div>
"""
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Real-World Costs & Strategic Math",
        "lecture": "Welcome to Mastery Challenge 4. In this final challenge, you will prove your mastery of fencing costs, real-world metric scales, composite surface regions, and Perimeter Dice Game strategies.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 to-rose-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Final Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Apply your geometric knowledge to practical word problems: calculating fencing costs, tiling floors, solving composite L-shapes, and mastering the Perimeter Dice Game.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "A farmer has a rectangular field 30 metres long and 20 metres wide. He wants to fence it with wire costing ₹15 per metre. What is the total cost?",
                "options": [
                    "₹1,500",
                    "₹9,000",
                    "₹750",
                    "₹3,000"
                ],
                "answer": 0,
                "hint": "Fencing requires perimeter: P = 2 × (30 + 20) = 100 m. Cost = 100 × ₹15.",
                "explanation": "Perimeter = 2 × (30 + 20) = 100 m. Total cost = 100 m × ₹15/m = ₹1,500.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Perimeter = 2 × (30 + 20) = 2 × 50 = 100 m.</p>
    <p>2. Rate = ₹15 per metre.</p>
    <p>3. Total Cost = 100 × 15 = <strong>₹1,500</strong>.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "A classroom floor is 10 metres long and 8 metres wide. It is to be paved with square tiles of side 1 metre. How many tiles are required?",
                "options": [
                    "80 tiles",
                    "36 tiles",
                    "40 tiles",
                    "100 tiles"
                ],
                "answer": 0,
                "hint": "Floor Area = 10 × 8 = 80 m². Each tile covers 1 m².",
                "explanation": "Number of tiles = Floor Area ÷ Tile Area = (10 × 8) ÷ (1 × 1) = 80 tiles.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Floor Area = 10 m × 8 m = 80 m².</p>
    <p>2. Area of 1 tile = 1 m × 1 m = 1 m².</p>
    <p>3. Number of tiles = 80 ÷ 1 = <strong>80 tiles</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "How many square centimetres (cm²) are in 1 square metre (m²)?",
                "options": [
                    "10,000 cm²",
                    "100 cm²",
                    "1,000 cm²",
                    "1,000,000 cm²"
                ],
                "answer": 0,
                "hint": "1 m = 100 cm. So 1 m² = 100 cm × 100 cm.",
                "explanation": "1 m² = 100 cm × 100 cm = 10,000 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 1 metre = 100 centimetres.</p>
    <p>2. 1 m² = 1 m × 1 m = 100 cm × 100 cm.</p>
    <p>3. 100 × 100 = <strong>10,000 cm²</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "An L-shaped room is split into two rectangles: Rectangle A (4 m × 3 m) and Rectangle B (5 m × 2 m). What is the total floor area?",
                "options": [
                    "22 m²",
                    "14 m²",
                    "28 m²",
                    "20 m²"
                ],
                "answer": 0,
                "hint": "Area A = 4 × 3 = 12 m². Area B = 5 × 2 = 10 m². Add them together.",
                "explanation": "Total Area = Area A + Area B = 12 + 10 = 22 m².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Area of Rectangle A = 4 × 3 = 12 m².</p>
    <p>2. Area of Rectangle B = 5 × 2 = 10 m².</p>
    <p>3. Total Area = 12 + 10 = <strong>22 m²</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "A square garden has an area of 64 m². A runner jogs around its boundary 3 times. What total distance did the runner travel?",
                "options": [
                    "96 metres",
                    "32 metres",
                    "192 metres",
                    "64 metres"
                ],
                "answer": 0,
                "hint": "Side = 8 m (since 8 × 8 = 64). Perimeter = 4 × 8 = 32 m. 3 rounds = 3 × 32 m.",
                "explanation": "Side = 8 m. One round (perimeter) = 32 m. 3 rounds = 3 × 32 = 96 m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Area = 64 m² ➔ Side = 8 m.</p>
    <p>2. Perimeter (1 round) = 4 × 8 = 32 m.</p>
    <p>3. 3 rounds = 3 × 32 = <strong>96 m</strong>.</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "In the Perimeter Dice Game, what is the winning objective?",
                "options": [
                    "To be the first player to build a connected shape with an exact outer perimeter of 24 units",
                    "To cover the entire board with the most tiles",
                    "To roll a six on three consecutive turns",
                    "To make the smallest possible perimeter with 50 tiles"
                ],
                "answer": 0,
                "hint": "Recall the game rules from Slide 16.",
                "explanation": "The winner is the first player whose shape's outer boundary reaches exactly 24 units.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. In the Joyful Mathematics Perimeter Building Game:</p>
    <p>2. Players take turns rolling dice and attaching unit tiles edge-to-edge.</p>
    <p>3. The goal is to reach an <strong>exact perimeter of 24 units</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "In the Perimeter Dice Game, why would a player choose to attach tiles in a long straight line?",
                "options": [
                    "Because a linear chain exposes 2 new exterior edges per tile, rapidly increasing perimeter",
                    "Because straight lines are not allowed by the opponent",
                    "Because straight lines reduce the perimeter to zero",
                    "Because it rolls higher numbers on the die"
                ],
                "answer": 0,
                "hint": "Adding to the end of a line adds 2 to the outer perimeter.",
                "explanation": "Linear chains maximize exposed edges, expanding perimeter by +2 for every tile added.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. A new tile at the end of a chain covers 1 boundary edge but introduces 3 new ones.</p>
    <p>2. Net perimeter increase = +3 - 1 = <strong>+2 units</strong> per tile.</p>
    <p>3. This linear tactic surges the perimeter toward the target 24 rapidly.</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "If your current shape in the dice game has a perimeter of 22 units, and you roll a 1, where should you place the tile to win the game immediately?",
                "options": [
                    "At the open end of a straight row (adding +2 to reach exactly 24)",
                    "In an inside corner (adding +0)",
                    "Diagonally at a corner (which is an illegal move)",
                    "On top of an existing tile"
                ],
                "answer": 0,
                "hint": "You need 24 - 22 = +2 units. An end-of-row placement adds +2.",
                "explanation": "Placing the tile at the end of a row adds +2, turning 22 into exactly 24 to win!",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Current perimeter = 22. Target = 24. Needed increase = 24 - 22 = <strong>+2</strong>.</p>
    <p>2. End-of-row placement gives net change of +2.</p>
    <p>3. 22 + 2 = 24 ➔ Immediate victory!</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "A wire of length 36 cm is bent into a rectangle with breadth 6 cm. What is the length of this rectangle?",
                "options": [
                    "12 cm",
                    "24 cm",
                    "18 cm",
                    "30 cm"
                ],
                "answer": 0,
                "hint": "Perimeter = 36 cm. So L + B = 36 ÷ 2 = 18 cm. Length = 18 - 6.",
                "explanation": "L + B = 36 ÷ 2 = 18 cm. Length = 18 - 6 = 12 cm.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Wire length = Perimeter = 36 cm.</p>
    <p>2. L + B = 36 ÷ 2 = 18 cm.</p>
    <p>3. Given Breadth B = 6 cm ➔ Length = 18 - 6 = <strong>12 cm</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "A square photo with side 10 cm is pasted in the center of a rectangular cardboard sheet 16 cm by 12 cm. What area of the cardboard sheet remains uncovered?",
                "options": [
                    "92 cm²",
                    "192 cm²",
                    "100 cm²",
                    "52 cm²"
                ],
                "answer": 0,
                "hint": "Cardboard Area = 16 × 12 = 192 cm². Photo Area = 10 × 10 = 100 cm². Uncovered = 192 - 100.",
                "explanation": "Uncovered Area = Total Area - Photo Area = 192 - 100 = 92 cm².",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Cardboard Area = 16 cm × 12 cm = 192 cm².</p>
    <p>2. Square Photo Area = 10 cm × 10 cm = 100 cm².</p>
    <p>3. Uncovered Area = 192 - 100 = <strong>92 cm²</strong>.</p>
</div>
"""
            }
        ]
    }
]

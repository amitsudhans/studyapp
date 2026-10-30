"""NCERT Class 6 Mathematics Chapter 6: Perimeter and Area Data Module."""

CHAPTER_META = {
    "chapter_num": 6,
    "title": "Perimeter & Area",
    "subtitle": "NCERT Class 6 Mathematics • Chapter 6 Interactive Master Laboratory",
    "mentors": "Acharya Baudhāyana & Archimedes of Syracuse",
    "mentors_title": "Pioneers of Geometric Sulba Sutras & Plane Mensuration",
    "badge": "Ganita Prakash • Mensuration & Spatial Reasoning",
    "total_slides": 20,
    "checkpoints_count": 32,
    "quiz_questions_count": 40
}

SLIDES = [
    {
        "id": 1,
        "slide_num": 1,
        "title": "Boundary Walk",
        "subtitle": "Total Distance Enclosing a Plane Figure",
        "badge": "6.1 Perimeter Foundations",
        "summary": "Perimeter is the total continuous distance covered when walking once entirely along the outer boundary of a closed plane figure. For any polygon, perimeter is simply the sum of the lengths of all its straight boundary sides.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">What is Perimeter?</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Imagine an ant walking along the outer edge of a closed geometric shape, starting at one corner and returning to where it began. The total distance walked is the <strong>Perimeter</strong> (from Greek <em>peri</em> = around, <em>metron</em> = measure).\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">General Polygon Rule:</span>\n                        <p class=\"font-mono text-slate-200\">Perimeter = Sum of all side lengths</p>\n                        <span class=\"text-[11px] text-slate-400\">For a 4-sided field: a + b + c + d</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Real-World Examples:</span>\n                        <ul class=\"list-disc list-inside text-slate-300 space-y-0.5 text-[11px]\">\n                            <li>Barbed wire fencing around a crop farm</li>\n                            <li>Decorative lace border around a dupatta</li>\n                            <li>Distance run around a sports track</li>\n                        </ul>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300\">\n                    <strong class=\"text-emerald-400\">Essential Condition:</strong>\n                    The figure must be <em>closed</em>! An open boundary has no defined perimeter.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_1_1",
                "question": "A triangular park has sides measuring 30 m, 40 m, and 50 m. What is its total perimeter?",
                "options": [
                    "60 m",
                    "120 m",
                    "150 m",
                    "1200 m"
                ],
                "correct": 1,
                "explanation": "Perimeter of any triangle is the sum of its three sides: 30 + 40 + 50 = 120 m."
            },
            {
                "id": "cp_1_2",
                "question": "Can an open curve or an unclosed line segment have a perimeter?",
                "options": [
                    "Yes, by doubling its length",
                    "No, perimeter is defined only for closed plane figures",
                    "Only if it is made of straight lines",
                    "Yes, if its area is zero"
                ],
                "correct": 1,
                "explanation": "Perimeter represents a complete closed loop around an enclosed region. Open figures have length, but no enclosed perimeter."
            }
        ]
    },
    {
        "id": 2,
        "slide_num": 2,
        "title": "Perimeter Formulas",
        "subtitle": "Shortcuts for Rectangles and Squares",
        "badge": "6.1 Standard Formulas",
        "summary": "Because opposite sides of a rectangle are equal in length, its perimeter equals 2 × (length + breadth). Because all four sides of a square are identical, its perimeter equals 4 × side length.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Deducing the Formulas</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Instead of adding all four sides individually, symmetries provide elegant multiplication shortcuts:\n                </p>\n                <div class=\"space-y-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Rectangle (Length l, Breadth b):</span>\n                        <p class=\"text-slate-300\">Opposite sides are equal: l + b + l + b = 2l + 2b</p>\n                        <span class=\"font-mono text-emerald-300 font-bold\">Perimeter = 2 × (length + breadth) = 2(l + b)</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Square (Side s):</span>\n                        <p class=\"text-slate-300\">All four sides are equal: s + s + s + s = 4s</p>\n                        <span class=\"font-mono text-emerald-300 font-bold\">Perimeter = 4 × side = 4s</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300\">\n                    <strong class=\"text-amber-400\">Finding the Side from Perimeter:</strong>\n                    If a square has perimeter P, each side length is: <span class=\"font-mono font-bold text-cyan-300\">side = P ÷ 4</span>.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_2_1",
                "question": "What is the perimeter of a table top measuring 150 cm long and 50 cm wide?",
                "options": [
                    "200 cm",
                    "300 cm",
                    "400 cm",
                    "7500 cm"
                ],
                "correct": 2,
                "explanation": "Perimeter = 2 × (length + breadth) = 2 × (150 + 50) = 2 × 200 = 400 cm (or 4 meters)."
            },
            {
                "id": "cp_2_2",
                "question": "If a square garden requires 80 meters of fencing to enclose it completely, what is the length of each side?",
                "options": [
                    "40 m",
                    "20 m",
                    "10 m",
                    "16 m"
                ],
                "correct": 1,
                "explanation": "Side of square = Perimeter ÷ 4 = 80 ÷ 4 = 20 meters."
            }
        ]
    },
    {
        "id": 3,
        "slide_num": 3,
        "title": "Regular Polygons",
        "subtitle": "Equilateral Triangles, Pentagons & Beyond",
        "badge": "6.1 Equal Sides & Angles",
        "summary": "A polygon is regular if all its sides are equal in length and all its interior angles are equal. The perimeter of any regular polygon with n sides is simply n multiplied by the length of one side.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The General Regular Polygon Rule</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    When all sides of an <em>n</em>-sided polygon have equal length <strong>s</strong>:\n                    <span class=\"font-mono text-emerald-300 font-bold block my-1\">Perimeter = n × side length</span>\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs mb-3 text-center\">\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Equilateral Triangle</span>\n                        <p class=\"font-mono text-slate-200\">n = 3</p>\n                        <span class=\"font-mono text-emerald-400 font-bold\">P = 3 × s</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Regular Pentagon</span>\n                        <p class=\"font-mono text-slate-200\">n = 5</p>\n                        <span class=\"font-mono text-emerald-400 font-bold\">P = 5 × s</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-violet-300 block mb-0.5\">Regular Hexagon</span>\n                        <p class=\"font-mono text-slate-200\">n = 6</p>\n                        <span class=\"font-mono text-emerald-400 font-bold\">P = 6 × s</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs\">\n                    <strong class=\"text-amber-400\">Crucial Distinction:</strong>\n                    A rhombus has 4 equal sides, but unequal angles, so it is equilateral but not regular. A square has both equal sides and equal angles, so it is a regular quadrilateral.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_3_1",
                "question": "What is the perimeter of a regular hexagon whose side length is 8 cm?",
                "options": [
                    "24 cm",
                    "48 cm",
                    "64 cm",
                    "40 cm"
                ],
                "correct": 1,
                "explanation": "A regular hexagon has 6 equal sides: Perimeter = 6 × side = 6 × 8 = 48 cm."
            },
            {
                "id": "cp_3_2",
                "question": "A piece of string is 30 cm long. If it is formed into an equilateral triangle, what is the length of each side?",
                "options": [
                    "15 cm",
                    "10 cm",
                    "5 cm",
                    "6 cm"
                ],
                "correct": 1,
                "explanation": "Side = Perimeter ÷ 3 = 30 ÷ 3 = 10 cm."
            }
        ]
    },
    {
        "id": 4,
        "slide_num": 4,
        "title": "Track Stagger Puzzle",
        "subtitle": "Concentric Lanes & Fair Starting Lines",
        "badge": "6.1 Real-World Application",
        "summary": "In sports running tracks, outer lanes have larger perimeters than inner lanes. To ensure all runners run the exact same total distance to a common finish line, outer runners must be given staggered starting positions ahead of the inner runners!",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The Geometry of Running Lanes</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Consider two square running tracks where the outer track is 1 meter wider on all sides than the inner track:\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Inner Track (Side = 20 m):</span>\n                        <p class=\"font-mono text-slate-200\">Perimeter = 4 × 20 = <strong>80 m</strong></p>\n                        <span class=\"text-[11px] text-slate-400\">Runner A runs 80 meters per lap.</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Outer Track (Side = 22 m):</span>\n                        <p class=\"font-mono text-slate-200\">Perimeter = 4 × 22 = <strong>88 m</strong></p>\n                        <span class=\"text-[11px] text-slate-400\">Runner B runs 88 meters per lap!</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n                    <strong class=\"text-emerald-400\">The Fair Stagger:</strong>\n                    The outer runner's track is 88 − 80 = <strong>8 meters longer</strong>.\n                    To make the race fair, Runner B must start <strong>8 meters ahead</strong> of Runner A!\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_4_1",
                "question": "If the outer square track is 2 meters wider on each side (side increases by 2 m), by how much does the perimeter increase?",
                "options": [
                    "2 m",
                    "4 m",
                    "8 m",
                    "16 m"
                ],
                "correct": 2,
                "explanation": "Since a square has 4 sides, increasing each side by 2 m increases the total perimeter by 4 × 2 = 8 m."
            },
            {
                "id": "cp_4_2",
                "question": "Why do 400m Olympic track runners not start side-by-side on the same line?",
                "options": [
                    "To prevent collisions only",
                    "Because outer lanes curve wider and have longer perimeters, requiring staggered starts",
                    "Because the fastest runner gets the inside lane",
                    "Because outer lanes are downhill"
                ],
                "correct": 1,
                "explanation": "The outer lanes have larger perimeters. Staggered starts ensure that every athlete runs exactly 400 meters to the finish line."
            }
        ]
    },
    {
        "id": 5,
        "slide_num": 5,
        "title": "Dot Grid Perimeter",
        "subtitle": "Straight Units (s) vs Diagonal Units (d)",
        "badge": "6.1 Measurement Units",
        "summary": "When measuring paper cutouts on dot grids, boundaries consist of two distinct types of steps: straight unit steps between horizontally or vertically adjacent dots (s), and slanted diagonal steps across grid squares (d). Because d is longer than s, we record perimeters as combinations like 6s + 3d.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Straight vs Diagonal Grid Steps</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    On a standard square dot grid:\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Straight Step (s):</span>\n                        <p class=\"text-slate-300\">Distance between adjacent dots horizontally or vertically = <strong>1 unit (s)</strong>.</p>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Diagonal Step (d):</span>\n                        <p class=\"text-slate-300\">Distance corner-to-corner across a square = <strong>d ≈ 1.414 units</strong>.</p>\n                        <span class=\"text-[11px] text-amber-400\">Diagonal d is strictly longer than straight s!</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-200\">\n                    <strong class=\"text-emerald-400\">Combined Perimeter Notation:</strong>\n                    If a shape has 6 straight edges and 4 diagonal edges on the dot grid, its exact boundary length is written as:\n                    <span class=\"font-mono font-bold text-emerald-300\">Perimeter = 6s + 4d</span>.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_5_1",
                "question": "Which distance is longer on a square dot grid: 1 straight step (s) or 1 diagonal step (d)?",
                "options": [
                    "Straight step (s)",
                    "Diagonal step (d)",
                    "Both are exactly equal",
                    "It depends on the grid size"
                ],
                "correct": 1,
                "explanation": "By geometry, the hypotenuse across a unit square is d = √2 ≈ 1.414 units, which is longer than s = 1 unit."
            },
            {
                "id": "cp_5_2",
                "question": "A shape has boundary segments consisting of 8 straight steps and 2 diagonal steps. How is its perimeter recorded?",
                "options": [
                    "10 units",
                    "8s + 2d",
                    "16sd",
                    "8d + 2s"
                ],
                "correct": 1,
                "explanation": "Because straight steps and diagonal steps have different physical lengths, we record them together as 8s + 2d."
            }
        ]
    },
    {
        "id": 6,
        "slide_num": 6,
        "title": "Split & Rejoin",
        "subtitle": "Perimeter Changes While Area Stays Constant",
        "badge": "6.1 Conservation Principle",
        "summary": "Cutting a geometric shape into pieces and rearranging them into a new configuration preserves the total material and surface area, but can drastically alter the total perimeter! Internal cuts expose new outer edges that increase boundary length.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The Split-and-Rejoin Experiment</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Take a square paper of side <strong>4 cm</strong>:\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Original Square (4 × 4):</span>\n                        <p class=\"font-mono text-slate-200\">Area = 4 × 4 = 16 cm²</p>\n                        <p class=\"font-mono text-slate-200\">Perimeter = 4 × 4 = <strong>16 cm</strong></p>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Cut in Half & Joined into (8 × 2):</span>\n                        <p class=\"font-mono text-slate-200\">Area = 8 × 2 = 16 cm² (Same!)</p>\n                        <p class=\"font-mono text-slate-200\">Perimeter = 2(8 + 2) = <strong>20 cm</strong> (Increased!)</p>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n                    <strong class=\"text-emerald-400\">Core Insight:</strong>\n                    Area is conserved under cutting and rearranging, but <strong>perimeter is NOT conserved</strong>!\n                    Whenever an internal cut is pulled apart, two new boundary edges are created.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_6_1",
                "question": "When a shape is cut into two pieces and rejoined edge-to-edge in a different way, what remains strictly unchanged?",
                "options": [
                    "Perimeter",
                    "Surface Area",
                    "Both Perimeter and Area",
                    "Neither Perimeter nor Area"
                ],
                "correct": 1,
                "explanation": "The amount of paper or material (surface area) remains constant, but the perimeter generally changes depending on how edges are joined."
            },
            {
                "id": "cp_6_2",
                "question": "A 4 cm × 4 cm square (P = 16 cm) is cut along a vertical line into two 2 cm × 4 cm rectangles. What is the sum of the perimeters of the two separate pieces?",
                "options": [
                    "16 cm",
                    "20 cm",
                    "24 cm",
                    "32 cm"
                ],
                "correct": 2,
                "explanation": "Each piece has perimeter 2(2 + 4) = 12 cm. Together, 12 + 12 = 24 cm. The 4 cm cut line exposed two new 4 cm edges (16 + 8 = 24 cm)."
            }
        ]
    },
    {
        "id": 7,
        "slide_num": 7,
        "title": "Area & Grid Units",
        "subtitle": "Why We Measure Surface in Unit Squares",
        "badge": "6.2 Area Foundations",
        "summary": "Area is the measure of the enclosed flat region bounded by a shape, expressed in square units (cm², m²). We use square units because squares tile flat surfaces seamlessly without leaving any empty gaps, unlike circular tiles which leave unfilled holes.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">What is Area?</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    While perimeter measures the boundary edge line, <strong>Area</strong> measures the enclosed flat surface inside the boundary.\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30\">\n                        <span class=\"font-bold text-emerald-300 block mb-0.5\">Unit Square (1 sq unit):</span>\n                        <p class=\"text-slate-300\">A square with side length of 1 unit. Area of a 1 cm square is written as <strong>1 sq cm (or 1 cm²)</strong>.</p>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30\">\n                        <span class=\"font-bold text-rose-300 block mb-0.5\">Why NOT Circles?</span>\n                        <p class=\"text-slate-300\">If you try to cover a floor with circular coins, they leave diamond-shaped gaps between them! Squares tile without gaps.</p>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300\">\n                    <strong class=\"text-amber-400\">Tiling Property:</strong>\n                    Shapes that fill a plane completely without overlapping or leaving gaps are called <em>tessellations</em>.\n                    Squares, equilateral triangles, and regular hexagons can tile the plane; circles cannot.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_7_1",
                "question": "What is the primary reason mathematicians measure surface area in square units instead of circular units?",
                "options": [
                    "Squares are easier to draw with a ruler",
                    "Squares pack and tile a flat surface completely without leaving gaps or overlapping",
                    "Circles have no area",
                    "Square units are smaller"
                ],
                "correct": 1,
                "explanation": "Unit squares pack side-by-side with zero wasted gaps, making them the standard universal tiling unit for surface measurement."
            },
            {
                "id": "cp_7_2",
                "question": "A rectangle is completely covered by 24 unit squares of 1 cm × 1 cm without overlap. What is its area?",
                "options": [
                    "24 cm",
                    "24 sq cm (24 cm²)",
                    "48 cm²",
                    "12 cm²"
                ],
                "correct": 1,
                "explanation": "Since 24 unit squares of 1 cm² cover the region, its area is 24 square centimeters (24 cm²)."
            }
        ]
    },
    {
        "id": 8,
        "slide_num": 8,
        "title": "Area Formulas",
        "subtitle": "Multiplication Rules & Multi-Step Practical Problems",
        "badge": "6.2 Standard Formulas",
        "summary": "Area of a rectangle is calculated by length × breadth, and area of a square is side × side. Practical real-life problems involve multi-step arithmetic, such as finding uncarpeted border floors or remaining field areas after digging corner flower beds.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Standard Formulas</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    In a grid of <em>l</em> columns and <em>b</em> rows:\n                </p>\n                <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Rectangle Area:</span>\n                        <span class=\"font-mono text-emerald-300 font-bold\">Area = length × breadth = l × b</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Square Area:</span>\n                        <span class=\"font-mono text-emerald-300 font-bold\">Area = side × side = s²</span>\n                    </div>\n                </div>\n                <h4 class=\"text-sm font-bold text-emerald-300 mb-1\">Multi-Step Subtraction Problem: Uncarpeted Floor</h4>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs space-y-1\">\n                    <p class=\"text-slate-300\">Room is <strong>5 m long × 4 m wide</strong>. Total Floor Area = 5 × 4 = <strong>20 m²</strong>.</p>\n                    <p class=\"text-slate-300\">A square carpet of <strong>side 3 m</strong> is laid on the floor. Carpet Area = 3 × 3 = <strong>9 m²</strong>.</p>\n                    <p class=\"text-amber-300 font-bold\">Uncarpeted Area = Total Floor − Carpet = 20 − 9 = 11 m².</p>\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_8_1",
                "question": "What is the area of a square plot of land whose side length is 12 meters?",
                "options": [
                    "48 m²",
                    "144 m²",
                    "24 m²",
                    "120 m²"
                ],
                "correct": 1,
                "explanation": "Area of square = side × side = 12 × 12 = 144 square meters (m²)."
            },
            {
                "id": "cp_8_2",
                "question": "A piece of cloth is 2 m long and 1.5 m wide. What is its surface area in square meters?",
                "options": [
                    "3.0 m²",
                    "3.5 m²",
                    "7.0 m²",
                    "2.5 m²"
                ],
                "correct": 0,
                "explanation": "Area = length × width = 2 × 1.5 = 3.0 m²."
            }
        ]
    },
    {
        "id": 9,
        "slide_num": 9,
        "title": "Tangram Exploration",
        "subtitle": "7-Piece Puzzle & Relative Area Ratios",
        "badge": "6.2 Geometric Dissection",
        "summary": "The ancient Chinese 7-piece Tangram consists of 2 large triangles, 1 medium triangle, 2 small triangles, 1 square, and 1 parallelogram. Comparing relative piece sizes reveals that the 2 small triangles together equal the area of the square, the parallelogram, and the medium triangle!",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The 7 Tangram Pieces & Their Relative Units</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Let the area of <strong>one small triangle = 1 unit</strong>. Then:\n                </p>\n                <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs mb-3 text-center\">\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">Small Triangle (×2)</span>\n                        <span class=\"font-bold text-emerald-300 font-mono\">1 unit each</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">Tangram Square</span>\n                        <span class=\"font-bold text-cyan-300 font-mono\">2 units</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">Parallelogram</span>\n                        <span class=\"font-bold text-amber-300 font-mono\">2 units</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">Medium Triangle</span>\n                        <span class=\"font-bold text-violet-300 font-mono\">2 units</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300\">\n                    <p class=\"mb-1\"><strong class=\"text-amber-400\">Large Triangles (×2):</strong> Each large triangle equals <strong>4 units</strong>.</p>\n                    <p class=\"font-mono text-emerald-300 font-bold\">Total Tangram Square Area = 1 + 1 + 2 + 2 + 2 + 4 + 4 = 16 units!</p>\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_9_1",
                "question": "If each small tangram triangle has an area of 5 cm², what is the area of the tangram square piece?",
                "options": [
                    "5 cm²",
                    "10 cm²",
                    "15 cm²",
                    "20 cm²"
                ],
                "correct": 1,
                "explanation": "The tangram square piece is formed exactly by 2 small triangles: Area = 2 × 5 = 10 cm²."
            },
            {
                "id": "cp_9_2",
                "question": "If all 7 pieces are rearranged from a square into a long rectangle, does the total area change?",
                "options": [
                    "Yes, the rectangle has larger area",
                    "No, the total surface area remains strictly identical",
                    "Yes, the square has larger area",
                    "It depends on the order of pieces"
                ],
                "correct": 1,
                "explanation": "Conservation of area ensures that rearranging the exact same 7 pieces always yields the exact same total area."
            }
        ]
    },
    {
        "id": 10,
        "slide_num": 10,
        "title": "Estimating on Grids",
        "subtitle": "The 4-Step Standard Graph Paper Counting Rule",
        "badge": "6.2 Irregular Shapes",
        "summary": "To estimate the area of irregular natural shapes (such as a fallen leaf or hand outline) placed over 1 cm² graph paper, follow the universal 4-step counting protocol: full squares count as 1, portions greater than half count as 1, exact halves count as 0.5, and portions less than half are ignored.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The Universal Graph Paper Protocol</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    When an irregular boundary cuts across grid squares:\n                </p>\n                <div class=\"space-y-1.5 text-xs mb-3\">\n                    <div class=\"p-2 rounded-lg bg-emerald-950/40 border border-emerald-500/30 flex justify-between items-center\">\n                        <span class=\"text-emerald-300 font-medium\">1. Fully filled grid square:</span>\n                        <span class=\"font-mono font-bold text-emerald-400\">Count as 1 sq unit</span>\n                    </div>\n                    <div class=\"p-2 rounded-lg bg-cyan-950/40 border border-cyan-500/30 flex justify-between items-center\">\n                        <span class=\"text-cyan-300 font-medium\">2. More than half filled:</span>\n                        <span class=\"font-mono font-bold text-cyan-400\">Count as 1 sq unit</span>\n                    </div>\n                    <div class=\"p-2 rounded-lg bg-amber-950/40 border border-amber-500/30 flex justify-between items-center\">\n                        <span class=\"text-amber-300 font-medium\">3. Exactly half filled:</span>\n                        <span class=\"font-mono font-bold text-amber-400\">Count as 0.5 sq unit</span>\n                    </div>\n                    <div class=\"p-2 rounded-lg bg-slate-900 border border-slate-700 flex justify-between items-center\">\n                        <span class=\"text-slate-400 font-medium\">4. Less than half filled:</span>\n                        <span class=\"font-mono font-bold text-slate-400\">Ignore (Count as 0)</span>\n                    </div>\n                </div>\n                <p class=\"text-xs text-slate-400\">\n                    Why ignore less than half while counting more than half as 1? Because the small ignored portions statistically balance out the rounded-up portions!\n                </p>\n            ",
        "checkpoints": [
            {
                "id": "cp_10_1",
                "question": "A leaf on squared graph paper covers 11 fully filled squares, 6 more-than-half squares, and 4 exact-half squares. What is its estimated area?",
                "options": [
                    "17 sq units",
                    "19 sq units",
                    "21 sq units",
                    "23 sq units"
                ],
                "correct": 1,
                "explanation": "Estimated Area = (11 × 1) + (6 × 1) + (4 × 0.5) = 11 + 6 + 2 = 19 sq units."
            },
            {
                "id": "cp_10_2",
                "question": "Under the standard NCERT grid estimation protocol, what value is assigned to a square that is only 20% covered by the shape?",
                "options": [
                    "0 (ignored)",
                    "0.5 sq unit",
                    "1 sq unit",
                    "0.2 sq unit"
                ],
                "correct": 0,
                "explanation": "Portions less than half (less than 50%) are completely ignored and count as 0."
            }
        ]
    },
    {
        "id": 11,
        "slide_num": 11,
        "title": "Same Area, Varied Perimeters",
        "subtitle": "How Shape Proportions Govern Boundary Length",
        "badge": "6.2 Area vs Perimeter Dynamics",
        "summary": "Rectangles with the exact same fixed area can have drastically different perimeters! Long, skinny rectangular strips have massive perimeters, while compact, squarish shapes minimize perimeter for the same enclosed area.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Fixed Area = 24 sq units</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Examine all whole-number factor pairs that form an area of 24 cm²:\n                </p>\n                <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs mb-3 text-center\">\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">1 × 24 Rectangle</span>\n                        <span class=\"text-amber-300 font-bold block\">P = 2(1 + 24)</span>\n                        <span class=\"font-mono text-rose-400 font-bold text-sm\">P = 50 cm</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">2 × 12 Rectangle</span>\n                        <span class=\"text-amber-300 font-bold block\">P = 2(2 + 12)</span>\n                        <span class=\"font-mono text-cyan-400 font-bold text-sm\">P = 28 cm</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">3 × 8 Rectangle</span>\n                        <span class=\"text-amber-300 font-bold block\">P = 2(3 + 8)</span>\n                        <span class=\"font-mono text-cyan-400 font-bold text-sm\">P = 22 cm</span>\n                    </div>\n                    <div class=\"p-2 rounded bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-400 block text-[10px]\">4 × 6 Rectangle</span>\n                        <span class=\"text-amber-300 font-bold block\">P = 2(4 + 6)</span>\n                        <span class=\"font-mono text-emerald-400 font-bold text-sm\">P = 20 cm</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n                    <strong class=\"text-emerald-400\">The Compactness Principle:</strong>\n                    As the rectangle becomes closer to a square (sides more equal: 4 and 6), its perimeter drops from 50 cm to 20 cm!\n                    Squarish shapes enclose the most area with the least fencing.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_11_1",
                "question": "Which rectangle of area 36 cm² has the SMALLEST possible perimeter?",
                "options": [
                    "1 cm × 36 cm (P = 74 cm)",
                    "2 cm × 18 cm (P = 40 cm)",
                    "4 cm × 9 cm (P = 26 cm)",
                    "6 cm × 6 cm square (P = 24 cm)"
                ],
                "correct": 3,
                "explanation": "A square (6 × 6) minimizes the perimeter for any given rectangular area. Its perimeter is only 24 cm."
            },
            {
                "id": "cp_11_2",
                "question": "If two shapes have the exact same perimeter, must their areas also be equal?",
                "options": [
                    "Yes, equal perimeter always guarantees equal area",
                    "No, shapes with identical perimeters can enclose very different areas",
                    "Only for squares",
                    "Only if they have the same number of sides"
                ],
                "correct": 1,
                "explanation": "No! For example, a 1×5 rectangle has P = 12 and Area = 5, while a 3×3 square has P = 12 and Area = 9."
            }
        ]
    },
    {
        "id": 12,
        "slide_num": 12,
        "title": "Making It More or Less",
        "subtitle": "Adding Unit Squares to Alter Perimeter",
        "badge": "6.2 Perimeter Surgery",
        "summary": "Attaching a new unit square to a figure always increases the total area by 1 sq unit. However, whether the perimeter increases, decreases, or stays the same depends entirely on where you attach it: attaching at an edge adds +2 edges, inside an indentation can decrease perimeter!",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Attaching a 1 × 1 Square to a Boundary</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Every 1 × 1 unit square has 4 edges. When you stick it onto an existing shape:\n                </p>\n                <div class=\"space-y-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30\">\n                        <strong class=\"text-emerald-300\">1. Attached to a Flat Edge (1 shared edge):</strong>\n                        <p class=\"text-slate-300\">Covers 1 existing edge, but exposes 3 new outer edges. Net change: 3 − 1 = <strong>+2 units</strong>!</p>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30\">\n                        <strong class=\"text-amber-300\">2. Tucked into a Corner Indentation (2 shared edges):</strong>\n                        <p class=\"text-slate-300\">Covers 2 existing edges and exposes 2 new outer edges. Net change: 2 − 2 = <strong>0 (Perimeter Unchanged!)</strong></p>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30\">\n                        <strong class=\"text-cyan-300\">3. Slotting into a 3-Sided Pocket (3 shared edges):</strong>\n                        <p class=\"text-slate-300\">Covers 3 existing edges and exposes only 1 new outer edge. Net change: 1 − 3 = <strong>−2 units (Perimeter Decreases!)</strong></p>\n                    </div>\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_12_1",
                "question": "If you glue a unit square onto a straight outer wall of a shape, what happens to the perimeter?",
                "options": [
                    "Increases by 4 units",
                    "Increases by 2 units",
                    "Decreases by 1 unit",
                    "Stays unchanged"
                ],
                "correct": 1,
                "explanation": "One edge is glued shut (lost), but three new edges are exposed to the outside. Net change = +3 − 1 = +2 units."
            },
            {
                "id": "cp_12_2",
                "question": "Can adding an extra unit square to a shape ever DECREASE its total perimeter?",
                "options": [
                    "Never, adding area always increases perimeter",
                    "Yes, if it fills a 3-sided gap (covering 3 edges and exposing only 1)",
                    "Only if the shape is a circle",
                    "Only on dot grids"
                ],
                "correct": 1,
                "explanation": "If a unit square fills a 3-sided pocket, 3 existing boundary edges are sealed away and only 1 new edge is exposed (net change: 1 − 3 = −2)."
            }
        ]
    },
    {
        "id": 13,
        "slide_num": 13,
        "title": "Floor Plans",
        "subtitle": "Charan & Sharan's House Room Areas",
        "badge": "6.2 Applied Geometry",
        "summary": "Architects represent buildings through 2D floor plans. Finding missing wall dimensions, individual room areas (living room, kitchen, bedroom), and total house footprints requires decomposing composite floor plans into separate rectangles.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Decomposing a House Floor Plan</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    A typical house plan consists of adjoining rectangular rooms:\n                </p>\n                <div class=\"p-3 rounded-xl bg-slate-900 border border-slate-700/80 mb-3 text-xs space-y-1.5 font-mono\">\n                    <div class=\"flex justify-between border-b border-slate-800 pb-1\">\n                        <span class=\"text-amber-300\">Living Room (6 m × 4 m):</span>\n                        <span class=\"text-emerald-400 font-bold\">Area = 24 m²</span>\n                    </div>\n                    <div class=\"flex justify-between border-b border-slate-800 pb-1\">\n                        <span class=\"text-cyan-300\">Master Bedroom (4 m × 3 m):</span>\n                        <span class=\"text-emerald-400 font-bold\">Area = 12 m²</span>\n                    </div>\n                    <div class=\"flex justify-between border-b border-slate-800 pb-1\">\n                        <span class=\"text-emerald-300\">Kitchen (3 m × 3 m):</span>\n                        <span class=\"text-emerald-400 font-bold\">Area = 9 m²</span>\n                    </div>\n                    <div class=\"flex justify-between pt-0.5\">\n                        <span class=\"text-slate-300 font-bold\">Total Enclosed House Footprint:</span>\n                        <span class=\"text-amber-400 font-black\">24 + 12 + 9 = 45 m²</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30 text-xs\">\n                    <strong class=\"text-cyan-300\">Deducing Missing Walls:</strong>\n                    If the total width is 7 m and the bedroom takes 4 m, the adjacent bathroom must have width: 7 − 4 = <strong>3 m</strong>!\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_13_1",
                "question": "A living room is 7 meters long and 5 meters wide. What is the cost of tiling its floor at Rs 50 per square meter?",
                "options": [
                    "Rs 1,200",
                    "Rs 1,750",
                    "Rs 600",
                    "Rs 3,500"
                ],
                "correct": 1,
                "explanation": "Floor Area = 7 × 5 = 35 m². Total Cost = 35 × 50 = Rs 1,750."
            },
            {
                "id": "cp_13_2",
                "question": "An L-shaped house floor can be split into two rectangles: 6 m × 3 m and 4 m × 2 m. What is its total area?",
                "options": [
                    "26 m²",
                    "30 m²",
                    "15 m²",
                    "48 m²"
                ],
                "correct": 0,
                "explanation": "Total Area = (6 × 3) + (4 × 2) = 18 + 8 = 26 m²."
            }
        ]
    },
    {
        "id": 14,
        "slide_num": 14,
        "title": "Area Maze Puzzles",
        "subtitle": "Japanese Menseki Meiro Deduction",
        "badge": "6.2 Geometric Deduction",
        "summary": "Area Mazes (Menseki Meiro) are Japanese geometric logic puzzles. By using the relationship Area = length × breadth, you deduce missing side lengths and unknown regional areas step-by-step without using complicated fractions or decimals!",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">How Area Mazes Work</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Every section is a rectangle with whole-number dimensions:\n                </p>\n                <div class=\"p-3 rounded-xl bg-slate-900 border border-slate-700/80 mb-3 text-xs space-y-2\">\n                    <div class=\"p-2 rounded bg-amber-950/40 border border-amber-500/30\">\n                        <span class=\"font-bold text-amber-300 block mb-0.5\">Clue 1: Rectangle A has Area = 18 cm², Width = 3 cm</span>\n                        <p class=\"font-mono text-slate-200\">Length = 18 ÷ 3 = <strong>6 cm</strong></p>\n                    </div>\n                    <div class=\"p-2 rounded bg-cyan-950/40 border border-cyan-500/30\">\n                        <span class=\"font-bold text-cyan-300 block mb-0.5\">Clue 2: Adjacent Rectangle B shares this 6 cm side and has Area = 24 cm²</span>\n                        <p class=\"font-mono text-slate-200\">Other side = 24 ÷ 6 = <strong>4 cm</strong></p>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n                    <strong class=\"text-emerald-400\">The Secret:</strong>\n                    Never guess or measure with a ruler! Use division (<span class=\"font-mono\">Length = Area ÷ Width</span>) to unlock adjacent cells step-by-step.\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_14_1",
                "question": "A rectangle has an area of 42 cm² and a height of 6 cm. What is its width?",
                "options": [
                    "6 cm",
                    "7 cm",
                    "8 cm",
                    "36 cm"
                ],
                "correct": 1,
                "explanation": "Width = Area ÷ Height = 42 ÷ 6 = 7 cm."
            },
            {
                "id": "cp_14_2",
                "question": "Two adjoining rectangles share the same height. Rectangle 1 has width 4 cm and area 20 cm². If Rectangle 2 has width 6 cm, what is its area?",
                "options": [
                    "24 cm²",
                    "30 cm²",
                    "36 cm²",
                    "12 cm²"
                ],
                "correct": 1,
                "explanation": "Shared Height = 20 ÷ 4 = 5 cm. Therefore, Area of Rectangle 2 = 6 × 5 = 30 cm²."
            }
        ]
    },
    {
        "id": 15,
        "slide_num": 15,
        "title": "Area of a Triangle",
        "subtitle": "Diagonal Folding & Half-Rectangle Derivation",
        "badge": "6.3 Triangle Formula",
        "summary": "Drawing a diagonal across any rectangle divides it into two congruent, identical right-angled triangles of equal area. Therefore, the area of each triangle is exactly half the area of the enclosing rectangle: Area = 1/2 × base × height!",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">Deriving the Triangle Formula</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    Take a rectangle with <strong>base b</strong> and <strong>height h</strong>:\n                </p>\n                <div class=\"space-y-2 text-xs mb-3\">\n                    <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700\">\n                        <span class=\"text-slate-300\">Area of enclosing rectangle = <strong>b × h</strong></span><br>\n                        <span class=\"text-cyan-300\">The diagonal splits it into 2 equal congruent triangles.</span>\n                    </div>\n                    <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30\">\n                        <span class=\"font-bold text-emerald-300 block mb-0.5\">The Universal Triangle Formula:</span>\n                        <span class=\"font-mono text-base font-black text-emerald-300\">Area = (1/2) × base × height = (b × h) ÷ 2</span>\n                    </div>\n                </div>\n                <div class=\"p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300\">\n                    <strong class=\"text-amber-400\">Works for Any Triangle:</strong>\n                    Even for non-right triangles, dropping a perpendicular height splits the triangle into two right triangles, confirming that <span class=\"font-mono font-bold text-slate-100\">Area = 1/2 × b × h</span> always holds!\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_15_1",
                "question": "A right triangle has base 8 cm and perpendicular height 5 cm. What is its area?",
                "options": [
                    "40 cm²",
                    "20 cm²",
                    "13 cm²",
                    "26 cm²"
                ],
                "correct": 1,
                "explanation": "Area of triangle = (1/2) × base × height = (1/2) × 8 × 5 = 20 cm²."
            },
            {
                "id": "cp_15_2",
                "question": "A rectangle of dimensions 10 cm × 6 cm is cut along its diagonal into two triangles. What is the area of each triangle?",
                "options": [
                    "60 cm²",
                    "30 cm²",
                    "16 cm²",
                    "15 cm²"
                ],
                "correct": 1,
                "explanation": "Rectangle area = 10 × 6 = 60 cm². Each diagonal triangle is exactly half: 60 ÷ 2 = 30 cm²."
            }
        ]
    },
    {
        "id": 16,
        "slide_num": 16,
        "title": "Composite Grid Shapes",
        "subtitle": "Decomposition into Rectangles and Triangles",
        "badge": "6.3 Spatial Decomposition",
        "summary": "Complex polygons drawn on square grids can be measured with exact mathematical precision by decomposing them into a patchwork of simple non-overlapping rectangles and right triangles, then summing their individual areas.",
        "theory": "\n                <h4 class=\"text-sm font-bold text-amber-300 mb-1\">The Divide-and-Conquer Technique</h4>\n                <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                    To find the area of an arrow, house outline, or irregular polygon on a grid:\n                </p>\n                <ol class=\"list-decimal list-inside text-xs text-slate-300 space-y-1 mb-3\">\n                    <li>Draw horizontal or vertical slice lines to partition the shape into familiar pieces.</li>\n                    <li>Calculate each rectangle piece via <span class=\"font-mono text-cyan-300\">length × breadth</span>.</li>\n                    <li>Calculate each triangular corner via <span class=\"font-mono text-amber-300\">(1/2) × base × height</span>.</li>\n                    <li>Add all piece areas together for the exact total!</li>\n                </ol>\n                <div class=\"p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs\">\n                    <span class=\"font-bold text-emerald-300 block mb-0.5\">Example: House Shape (Wall + Roof)</span>\n                    <p class=\"text-slate-300 font-mono\">Wall Rectangle (4 × 3) = 12 sq units</p>\n                    <p class=\"text-slate-300 font-mono\">Roof Triangle (base 4, height 2) = (1/2) × 4 × 2 = 4 sq units</p>\n                    <span class=\"text-emerald-400 font-bold block mt-1\">Total House Area = 12 + 4 = 16 sq units!</span>\n                </div>\n            ",
        "checkpoints": [
            {
                "id": "cp_16_1",
                "question": "A composite shape on a grid consists of a central 5 × 4 rectangle flanked by two right triangles of base 2 and height 4. What is the total area?",
                "options": [
                    "20 sq units",
                    "24 sq units",
                    "28 sq units",
                    "36 sq units"
                ],
                "correct": 2,
                "explanation": "Rectangle = 5 × 4 = 20. Each triangle = (1/2) × 2 × 4 = 4. Total Area = 20 + 4 + 4 = 28 sq units."
            },
            {
                "id": "cp_16_2",
                "question": "Can the area of any polygon on a grid be calculated by subtracting empty corner triangles from a bounding box rectangle?",
                "options": [
                    "Yes, the box subtraction method is a powerful alternative to direct splitting",
                    "No, subtraction only works for squares",
                    "Only if all angles are right angles",
                    "Never"
                ],
                "correct": 0,
                "explanation": "Yes! The bounding box method draws an outer rectangle around the polygon and subtracts the empty negative space triangles, giving the exact interior area."
            }
        ]
    },
    {
        "id": 17,
        "slide_num": 17,
        "title": "Quiz 1",
        "subtitle": "Perimeter Definitions, Formulas, Regular Polygons & Tracks • Questions 1 to 10",
        "badge": "Quiz 1 • Perimeter",
        "is_quiz": True,
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": 18,
        "slide_num": 18,
        "title": "Quiz 2",
        "subtitle": "Dot Grids, Split-Rejoin Paradox & Unit Squares • Questions 11 to 20",
        "badge": "Quiz 2 • Foundations",
        "is_quiz": True,
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": 19,
        "slide_num": 19,
        "title": "Quiz 3",
        "subtitle": "Tangrams, Grid Estimation & Area-Perimeter Dynamics • Questions 21 to 30",
        "badge": "Quiz 3 • Area Dynamics",
        "is_quiz": True,
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": 20,
        "slide_num": 20,
        "title": "Quiz 4",
        "subtitle": "Floor Plans, Area Mazes, Triangle Formula & Composites • Questions 31 to 40",
        "badge": "Quiz 4 • Advanced Mensuration",
        "is_quiz": True,
        "quiz_range": [
            31,
            40
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the perimeter of a rectangle with length 18 cm and breadth 12 cm?",
        "options": [
            "30 cm",
            "60 cm",
            "216 cm",
            "45 cm"
        ],
        "correct": 1,
        "explanation": "Perimeter = 2 × (length + breadth) = 2 × (18 + 12) = 2 × 30 = 60 cm."
    },
    {
        "id": 2,
        "question": "An athlete takes 5 complete rounds of a square park of side 50 m. What total distance does she run?",
        "options": [
            "250 m",
            "500 m",
            "1,000 m (1 km)",
            "2,500 m"
        ],
        "correct": 2,
        "explanation": "One round = 4 × 50 = 200 m. For 5 rounds: 5 × 200 = 1,000 m (1 kilometer)."
    },
    {
        "id": 3,
        "question": "What is the length of one side of a regular pentagon if its perimeter is 65 cm?",
        "options": [
            "11 cm",
            "13 cm",
            "15 cm",
            "25 cm"
        ],
        "correct": 1,
        "explanation": "A regular pentagon has 5 equal sides: side = Perimeter ÷ 5 = 65 ÷ 5 = 13 cm."
    },
    {
        "id": 4,
        "question": "What is the cost of fencing a rectangular field 250 m long and 150 m wide at the rate of Rs 20 per meter?",
        "options": [
            "Rs 8,000",
            "Rs 16,000",
            "Rs 37,500",
            "Rs 75,000"
        ],
        "correct": 1,
        "explanation": "Perimeter = 2 × (250 + 150) = 2 × 400 = 800 m. Cost = 800 × 20 = Rs 16,000."
    },
    {
        "id": 5,
        "question": "An equilateral triangle has a perimeter of 42 cm. What is the length of each of its sides?",
        "options": [
            "12 cm",
            "14 cm",
            "21 cm",
            "7 cm"
        ],
        "correct": 1,
        "explanation": "An equilateral triangle has 3 equal sides: side = 42 ÷ 3 = 14 cm."
    },
    {
        "id": 6,
        "question": "A regular octagon has side length 9 cm. What is its perimeter?",
        "options": [
            "54 cm",
            "63 cm",
            "72 cm",
            "81 cm"
        ],
        "correct": 2,
        "explanation": "A regular octagon has 8 equal sides: Perimeter = 8 × 9 = 72 cm."
    },
    {
        "id": 7,
        "question": "On two concentric square tracks, Lane 2 is 1.5 m further out on all sides than Lane 1. How much longer is Lane 2?",
        "options": [
            "6 m",
            "12 m",
            "8 m",
            "15 m"
        ],
        "correct": 1,
        "explanation": "Each of the 4 sides is longer by 1.5 m on both ends (total 3 m per side). 4 sides × 3 m = 12 meters."
    },
    {
        "id": 8,
        "question": "A rectangular photo frame requires 70 cm of wood. If the breadth is 15 cm, what is the length?",
        "options": [
            "20 cm",
            "25 cm",
            "35 cm",
            "55 cm"
        ],
        "correct": 0,
        "explanation": "Perimeter = 2(l + b) = 70 → l + 15 = 35 → l = 35 − 15 = 20 cm."
    },
    {
        "id": 9,
        "question": "What is the perimeter of a regular decagon (10-sided polygon) with side length 4.5 cm?",
        "options": [
            "45 cm",
            "40 cm",
            "50 cm",
            "90 cm"
        ],
        "correct": 0,
        "explanation": "Perimeter = 10 × 4.5 = 45 cm."
    },
    {
        "id": 10,
        "question": "Which of the following plane figures with side length 6 cm has the LARGEST perimeter?",
        "options": [
            "Equilateral triangle",
            "Square",
            "Regular pentagon",
            "Regular hexagon"
        ],
        "correct": 3,
        "explanation": "Triangle P = 3×6=18; Square P = 4×6=24; Pentagon P = 5×6=30; Hexagon P = 6×6=36 cm."
    },
    {
        "id": 11,
        "question": "On a square dot grid, a paper shape has boundary 10 straight units (s) and 4 diagonal units (d). How is its perimeter written?",
        "options": [
            "14 units",
            "10s + 4d",
            "40sd",
            "10d + 4s"
        ],
        "correct": 1,
        "explanation": "Because straight units and diagonal units are geometrically unequal, the perimeter is expressed as 10s + 4d."
    },
    {
        "id": 12,
        "question": "If you take a square of paper and cut it along any line, then tape the two pieces together in a new shape, what happens to the area?",
        "options": [
            "The area increases",
            "The area decreases",
            "The area remains strictly unchanged",
            "The area doubles"
        ],
        "correct": 2,
        "explanation": "The total amount of paper material is conserved, so the surface area is strictly unchanged."
    },
    {
        "id": 13,
        "question": "In the split-and-rejoin activity, why does the perimeter usually increase after rearranging cut pieces?",
        "options": [
            "Because paper stretches when cut",
            "Because the internal cut exposes two new outer edges that were previously hidden inside",
            "Because angles become sharper",
            "Because diagonals are created"
        ],
        "correct": 1,
        "explanation": "Cutting creates new boundary edges where the paper was sliced open, adding to the total outer boundary when separated."
    },
    {
        "id": 14,
        "question": "What is the standard metric unit used to measure the area of a classroom floor?",
        "options": [
            "Meters (m)",
            "Square meters (m²)",
            "Cubic meters (m³)",
            "Centimeters (cm)"
        ],
        "correct": 1,
        "explanation": "Surface area is measured in two-dimensional square units, such as square meters (m²)."
    },
    {
        "id": 15,
        "question": "Why can flat planes NOT be measured without gaps using circular unit tiles?",
        "options": [
            "Circles are round",
            "Circles leave unfilled gap spaces between their contact points when packed together",
            "Circles have no radius",
            "Circles have infinite perimeter"
        ],
        "correct": 1,
        "explanation": "Circles cannot tessellate (tile) a flat plane without leaving empty gaps, whereas squares fit together seamlessly."
    },
    {
        "id": 16,
        "question": "A square has perimeter 28 cm. What is its area?",
        "options": [
            "49 cm²",
            "56 cm²",
            "14 cm²",
            "196 cm²"
        ],
        "correct": 0,
        "explanation": "Side of square = 28 ÷ 4 = 7 cm. Area = 7 × 7 = 49 cm²."
    },
    {
        "id": 17,
        "question": "A rectangular lawn is 20 m long and 15 m wide. What is its total surface area?",
        "options": [
            "70 m²",
            "300 m²",
            "150 m²",
            "35 m²"
        ],
        "correct": 1,
        "explanation": "Area of rectangle = length × breadth = 20 × 15 = 300 m²."
    },
    {
        "id": 18,
        "question": "A room floor of 4 m × 3 m (12 m²) has a 2 m × 2 m square rug placed in its center. What is the uncovered floor area?",
        "options": [
            "4 m²",
            "6 m²",
            "8 m²",
            "10 m²"
        ],
        "correct": 2,
        "explanation": "Total Area = 12 m². Rug Area = 2 × 2 = 4 m². Uncovered Area = 12 − 4 = 8 m²."
    },
    {
        "id": 19,
        "question": "How many 1 cm × 1 cm square tiles are required to completely cover a rectangle of 6 cm × 4 cm?",
        "options": [
            "20 tiles",
            "24 tiles",
            "10 tiles",
            "48 tiles"
        ],
        "correct": 1,
        "explanation": "Total Area = 6 × 4 = 24 cm². Since each tile is 1 cm², exactly 24 tiles are required."
    },
    {
        "id": 20,
        "question": "If the side of a square is doubled, what happens to its area?",
        "options": [
            "It doubles (2×)",
            "It quadruples (4×)",
            "It stays the same",
            "It triples (3×)"
        ],
        "correct": 1,
        "explanation": "If side changes from s to 2s, new Area = (2s)² = 4s². The area increases by a factor of 4!"
    },
    {
        "id": 21,
        "question": "In a standard 7-piece tangram puzzle, how many pieces are triangles?",
        "options": [
            "3 pieces",
            "4 pieces",
            "5 pieces",
            "6 pieces"
        ],
        "correct": 2,
        "explanation": "A tangram consists of 5 triangles (2 large, 1 medium, 2 small), 1 square, and 1 parallelogram."
    },
    {
        "id": 22,
        "question": "If each small tangram triangle has area 4 cm², what is the total area of the entire assembled 7-piece square?",
        "options": [
            "32 cm²",
            "64 cm²",
            "48 cm²",
            "16 cm²"
        ],
        "correct": 1,
        "explanation": "The entire tangram equals 16 small triangle units: 16 × 4 = 64 cm²."
    },
    {
        "id": 23,
        "question": "Using the standard graph paper counting rule, how is a square that is 80% covered by a leaf counted?",
        "options": [
            "0",
            "0.5 sq unit",
            "1 sq unit",
            "0.8 sq unit"
        ],
        "correct": 2,
        "explanation": "Any grid square that is more than half covered (≥ 50%) is counted as 1 full square unit."
    },
    {
        "id": 24,
        "question": "An irregular shape covers 8 full squares, 4 exact half squares, and 5 more-than-half squares. What is its estimated area?",
        "options": [
            "13 sq units",
            "15 sq units",
            "17 sq units",
            "19 sq units"
        ],
        "correct": 1,
        "explanation": "Estimated Area = (8 × 1) + (4 × 0.5) + (5 × 1) = 8 + 2 + 5 = 15 sq units."
    },
    {
        "id": 25,
        "question": "Consider four rectangles, each with an area of 36 cm². Which dimension pair produces the LARGEST perimeter?",
        "options": [
            "6 cm × 6 cm (P = 24 cm)",
            "4 cm × 9 cm (P = 26 cm)",
            "2 cm × 18 cm (P = 40 cm)",
            "1 cm × 36 cm (P = 74 cm)"
        ],
        "correct": 3,
        "explanation": "The most elongated, narrow strip (1 × 36) has the maximum perimeter: 2 × (1 + 36) = 74 cm."
    },
    {
        "id": 26,
        "question": "When a 1 × 1 unit square is attached to a flat outer edge of a polygon, how does the perimeter change?",
        "options": [
            "Increases by 1 unit",
            "Increases by 2 units",
            "Increases by 3 units",
            "Does not change"
        ],
        "correct": 1,
        "explanation": "It covers 1 existing edge and creates 3 new outer edges: net change = +3 − 1 = +2 units."
    },
    {
        "id": 27,
        "question": "If a unit square is slotted into an internal L-shaped corner (covering 2 existing edges), how does the perimeter change?",
        "options": [
            "Increases by 2",
            "Decreases by 2",
            "Perimeter remains strictly unchanged (0 net change)",
            "Increases by 1"
        ],
        "correct": 2,
        "explanation": "It covers 2 existing edges and exposes 2 new edges: net change = +2 − 2 = 0."
    },
    {
        "id": 28,
        "question": "Can two rectangles have the exact same perimeter of 20 cm but different areas?",
        "options": [
            "No, equal perimeter always forces equal area",
            "Yes, e.g., 1 × 9 (Area = 9 cm²) and 5 × 5 (Area = 25 cm²)",
            "Only if one of them is a triangle",
            "Only with decimal side lengths"
        ],
        "correct": 1,
        "explanation": "Both have perimeter 2(1 + 9) = 20 and 4(5) = 20, but their areas are 9 cm² and 25 cm²."
    },
    {
        "id": 29,
        "question": "A farmer has 40 meters of wire fencing to enclose a rectangular vegetable garden. Which dimensions will give him the MAXIMUM growing area?",
        "options": [
            "1 m × 19 m (Area = 19 m²)",
            "5 m × 15 m (Area = 75 m²)",
            "8 m × 12 m (Area = 96 m²)",
            "10 m × 10 m square (Area = 100 m²)"
        ],
        "correct": 3,
        "explanation": "For any fixed perimeter, a square shape always encloses the maximum possible rectangular area: 10 × 10 = 100 m²."
    },
    {
        "id": 30,
        "question": "Under the grid estimation protocol, squares that are less than half filled by an irregular outline are:",
        "options": [
            "Counted as 0.25",
            "Counted as 0.5",
            "Completely ignored (counted as 0)",
            "Subtracted from the total"
        ],
        "correct": 2,
        "explanation": "Any grid square covered less than 50% is ignored (count = 0) to balance out the squares rounded up to 1."
    },
    {
        "id": 31,
        "question": "In a house floor plan, a bedroom is 4 m × 3 m and an adjacent bathroom is 2 m × 3 m. What is their combined area?",
        "options": [
            "12 m²",
            "14 m²",
            "18 m²",
            "24 m²"
        ],
        "correct": 2,
        "explanation": "Combined Area = (4 × 3) + (2 × 3) = 12 + 6 = 18 m² (or combined width 6 m × 3 m = 18 m²)."
    },
    {
        "id": 32,
        "question": "In an Area Maze, a rectangle has Area = 35 cm² and height = 5 cm. What is its horizontal length?",
        "options": [
            "5 cm",
            "6 cm",
            "7 cm",
            "8 cm"
        ],
        "correct": 2,
        "explanation": "Length = Area ÷ Height = 35 ÷ 5 = 7 cm."
    },
    {
        "id": 33,
        "question": "In an Area Maze, two rectangles share a common vertical edge. Left rectangle has width 4 cm and area 28 cm². Right rectangle has width 3 cm. What is the area of the right rectangle?",
        "options": [
            "21 cm²",
            "24 cm²",
            "18 cm²",
            "15 cm²"
        ],
        "correct": 0,
        "explanation": "Shared Height = 28 ÷ 4 = 7 cm. Area of right rectangle = 3 × 7 = 21 cm²."
    },
    {
        "id": 34,
        "question": "What is the formula for the area of any triangle with base b and perpendicular height h?",
        "options": [
            "b × h",
            "(1/2) × b × h",
            "2 × (b + h)",
            "b + h"
        ],
        "correct": 1,
        "explanation": "A triangle is half of an enclosing rectangle of dimensions b × h, so its area is (1/2) × b × h."
    },
    {
        "id": 35,
        "question": "A right-angled triangle has perpendicular legs measuring 6 cm and 8 cm. What is its area?",
        "options": [
            "48 cm²",
            "24 cm²",
            "14 cm²",
            "28 cm²"
        ],
        "correct": 1,
        "explanation": "Area = (1/2) × base × height = (1/2) × 6 × 8 = 24 cm²."
    },
    {
        "id": 36,
        "question": "A triangle has base 14 cm and perpendicular altitude (height) 9 cm. What is its area?",
        "options": [
            "126 cm²",
            "63 cm²",
            "23 cm²",
            "46 cm²"
        ],
        "correct": 1,
        "explanation": "Area = (1/2) × 14 × 9 = 7 × 9 = 63 cm²."
    },
    {
        "id": 37,
        "question": "A rectangular cardboard measuring 10 cm × 8 cm is cut along both diagonals into 4 equal triangles. What is the area of each triangle?",
        "options": [
            "80 cm²",
            "40 cm²",
            "20 cm²",
            "10 cm²"
        ],
        "correct": 2,
        "explanation": "Total Cardboard Area = 10 × 8 = 80 cm². Each of the 4 equal triangles has area 80 ÷ 4 = 20 cm²."
    },
    {
        "id": 38,
        "question": "An arrow shape on a grid is decomposed into a rectangular shaft of 6 × 2 and a triangular head with base 6 and height 3. What is the total area?",
        "options": [
            "15 sq units",
            "21 sq units",
            "24 sq units",
            "18 sq units"
        ],
        "correct": 1,
        "explanation": "Shaft Area = 6 × 2 = 12. Head Area = (1/2) × 6 × 3 = 9. Total Area = 12 + 9 = 21 sq units."
    },
    {
        "id": 39,
        "question": "A square garden has side 10 m. A 1 m wide gravel path is built all around the outside of the garden. What is the area of the gravel path?",
        "options": [
            "44 m²",
            "40 m²",
            "21 m²",
            "100 m²"
        ],
        "correct": 0,
        "explanation": "Inner Garden Area = 10 × 10 = 100 m². Outer boundary side = 10 + 1 + 1 = 12 m. Outer Area = 12 × 12 = 144 m². Path Area = 144 − 100 = 44 m²."
    },
    {
        "id": 40,
        "question": "Which of the following statements is ALWAYS true for any closed polygon?",
        "options": [
            "Perimeter is measured in square units",
            "Area represents the boundary length",
            "Perimeter is 1-dimensional length (cm, m), while Area is 2-dimensional surface (cm², m²)",
            "Shapes with different perimeters cannot have the same area"
        ],
        "correct": 2,
        "explanation": "Perimeter is a 1D linear measurement of the boundary (cm, m), while Area is a 2D measure of the enclosed surface (cm², m²)."
    }
]

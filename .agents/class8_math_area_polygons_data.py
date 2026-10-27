# Class 8 Mathematics Chapter 14: Area (Area of Polygons & Mensuration)
# Complete 20-slide dataset: 16 lesson slides with bespoke simulators & 32 checkpoints + 4 mastery challenge slides (40 questions with detailed step-by-step solutions)

SLIDES_DATA = [
  {
    "id": 1,
    "title": "Area",
    "subtitle": "2D Spatial Measure & Square Unit Tiling",
    "content": "<p>What is <strong>area</strong>? While length is a one-dimensional measure of distance along a path, area is the <strong>two-dimensional measure of the surface enclosed within a closed boundary</strong>.</p><p class='mt-2'>We measure area by counting how many identical <strong>unit squares</strong> (e.g., $1\\text{ cm} \\times 1\\text{ cm} = 1\\text{ cm}^2$ or $1\\text{ m} \\times 1\\text{ m} = 1\\text{ m}^2$) are required to pave or tessellate the region completely without overlaps or gaps.</p><p class='mt-2'>Two fundamental axioms govern all area calculations:</p><ol class='list-decimal pl-5 space-y-1'><li><strong>Congruence Invariant:</strong> If two planar figures are congruent, their areas are strictly equal.</li><li><strong>Additive Property:</strong> If a figure is dissected into non-overlapping sub-regions, the total area is the sum of the areas of its parts.</li></ol>",
    "key_takeaways": [
      "Area is the 2D measure of the interior region enclosed by a closed planar boundary.",
      "Area is quantified in square units ($1\\text{ cm}^2, 1\\text{ m}^2$) by tiling without gaps or overlaps.",
      "The total area of any complex shape is the sum of its non-overlapping dissected parts."
    ],
    "formula": "$$\\text{Unit Square: } \\text{Area} = 1\\text{ unit} \\times 1\\text{ unit} = 1\\text{ unit}^2 \\quad \\implies \\quad \\text{Area}(A \\cup B) = \\text{Area}(A) + \\text{Area}(B)$$",
    "simulator_type": "area_square_unit_tiling_sim",
    "checkpoints": [
      {
        "question": "What does an area of $12\\text{ cm}^2$ physically represent?",
        "options": [
          "A boundary length of 12 centimeters around a figure",
          "A flat surface that can be exactly tiled by twelve $1\\text{ cm} \\times 1\\text{ cm}$ unit squares without overlap",
          "A solid 3D block with twelve cubic corners",
          "A triangle with three sides of 4 centimeters each"
        ],
        "correct": 1,
        "explanation": "Area measures 2D planar coverage: $12\\text{ cm}^2$ indicates the interior region contains the exact surface equivalent of twelve $1\\text{ cm} \\times 1\\text{ cm}$ unit squares."
      },
      {
        "question": "If a planar shape is cut into three separate non-overlapping pieces and rearranged into a new shape, what happens to the total area?",
        "options": [
          "The area increases because there are more pieces",
          "The area decreases because the perimeter becomes longer",
          "The area remains strictly unchanged due to the additive area invariant",
          "The area changes depending on the color of the pieces"
        ],
        "correct": 2,
        "explanation": "By the dissection and additive property of area, rearranging non-overlapping pieces preserves the exact total amount of surface, keeping the area invariant."
      }
    ]
  },
  {
    "id": 2,
    "title": "Rectangles & Squares",
    "subtitle": "Dimension Products: L × W and s²",
    "content": "<p>For a rectangle with length $L$ and width $W$, unit squares naturally form an orderly grid array: $W$ rows, each containing $L$ unit squares. Hence, the total number of unit squares is simply their product:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of Rectangle} = \\text{Length} \\times \\text{Width} = L \\times W$$</div><p class='mt-2'>A <strong>square</strong> is a special regular rectangle where length equals width ($L = W = s$). The area formula simplifies to:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of Square} = \\text{side} \\times \\text{side} = s^2$$</div><p class='mt-2'>Every other 2D polygon area formula in mathematics is derived by slicing, shearing, or rearranging shapes back into equivalent rectangles!</p>",
    "key_takeaways": [
      "The area of a rectangle is $\\text{Length} \\times \\text{Width}$, counting $W$ rows of $L$ unit squares.",
      "A square of side $s$ has area $s^2$, representing a quadratic scaling of surface.",
      "Rectangular area serves as the foundational benchmark for all polygon mensuration."
    ],
    "formula": "$$\\text{Rectangle: } A = L \\times W, \\qquad \\text{Square: } A = s^2$$",
    "simulator_type": "rectangle_square_dimension_scaler",
    "checkpoints": [
      {
        "question": "If the side length of a square is tripled from $s$ to $3s$, by what factor does its area increase?",
        "options": [
          "3 times",
          "6 times",
          "9 times",
          "27 times"
        ],
        "correct": 2,
        "explanation": "New area = $(3s)^2 = 9s^2$. Because area depends quadratically on linear dimension, tripling the side length multiplies the area by $3^2 = 9$."
      },
      {
        "question": "A rectangular hallway is $8\\text{ m}$ long and $3.5\\text{ m}$ wide. What is its floor area?",
        "options": [
          "$23\\text{ m}^2$",
          "$24.5\\text{ m}^2$",
          "$28\\text{ m}^2$",
          "$32\\text{ m}^2$"
        ],
        "correct": 2,
        "explanation": "Area = $L \\times W = 8\\text{ m} \\times 3.5\\text{ m} = 28\\text{ m}^2$."
      }
    ]
  },
  {
    "id": 3,
    "title": "Perimeter vs Area",
    "subtitle": "Why Can't Perimeter be a Measure of Area?",
    "content": "<p>A common misconception is that a longer perimeter automatically means a larger enclosed area. <strong>Why can't perimeter be a measure of area?</strong></p><p class='mt-2'><strong>Perimeter</strong> measures the <em>1D length of the outer fence</em>. <strong>Area</strong> measures the <em>2D surface enclosed inside the fence</em>. Shapes with the exact same perimeter can have wildly different areas!</p><p class='mt-2'>Consider a fixed wire of length $P = 24\\text{ cm}$ formed into rectangles ($2(L + W) = 24 \\implies L + W = 12$):</p><ul><li>$11\\text{ cm} \\times 1\\text{ cm} \\implies \\text{Perimeter} = 24\\text{ cm}, \\quad \\text{Area} = 11\\text{ cm}^2$</li><li>$9\\text{ cm} \\times 3\\text{ cm} \\implies \\text{Perimeter} = 24\\text{ cm}, \\quad \\text{Area} = 27\\text{ cm}^2$</li><li>$7\\text{ cm} \\times 5\\text{ cm} \\implies \\text{Perimeter} = 24\\text{ cm}, \\quad \\text{Area} = 35\\text{ cm}^2$</li><li>$6\\text{ cm} \\times 6\\text{ cm} \\implies \\text{Perimeter} = 24\\text{ cm}, \\quad \\text{Area} = \\mathbf{36\\text{ cm}^2}$ (Square!)</li></ul><p class='mt-2'>Flattening the rectangle reduces its area toward zero while keeping the perimeter constant at 24 cm!</p>",
    "key_takeaways": [
      "Perimeter (1D linear length) and Area (2D surface coverage) measure fundamentally different geometric quantities.",
      "Shapes with identical perimeters can enclose drastically different areas.",
      "For a fixed perimeter, the closer a rectangle is to a square, the greater the area it encloses."
    ],
    "formula": "$$P = 2(L + W) = \\text{constant} \\implies A = L(W) = L\\left(\\frac{P}{2} - L\\right) \\le \\left(\\frac{P}{4}\\right)^2$$",
    "simulator_type": "perimeter_vs_area_comparator",
    "checkpoints": [
      {
        "question": "Two rectangles each have a perimeter of $40\\text{ cm}$. Rectangle A is $10\\text{ cm} \\times 10\\text{ cm}$, while Rectangle B is $18\\text{ cm} \\times 2\\text{ cm}$. Which has the larger area?",
        "options": [
          "Both have the same area because their perimeters are equal",
          "Rectangle A ($100\\text{ cm}^2$) is much larger than Rectangle B ($36\\text{ cm}^2$)",
          "Rectangle B is larger because it is much longer",
          "Neither rectangle has any area"
        ],
        "correct": 1,
        "explanation": "Area of A = $10 \\times 10 = 100\\text{ cm}^2$. Area of B = $18 \\times 2 = 36\\text{ cm}^2$. The square encloses almost three times the area of the long, skinny rectangle despite having identical perimeters."
      },
      {
        "question": "If you squeeze a flexible rectangular wire loop into a very thin ribbon of width nearly 0, what happens to its perimeter and its area?",
        "options": [
          "Perimeter drops to 0, area stays constant",
          "Both perimeter and area drop to 0",
          "Perimeter stays constant, but area shrinks toward 0",
          "Area becomes infinite"
        ],
        "correct": 2,
        "explanation": "The loop wire length (perimeter) remains constant, but as the gap between opposite sides closes ($W \\to 0$), the enclosed 2D surface area vanishes toward 0."
      }
    ]
  },
  {
    "id": 4,
    "title": "Area of Triangles",
    "subtitle": "Half of an Enclosing Rectangle or Parallelogram",
    "content": "<p>How do we find the area of any triangle? The answer lies in the beautiful symmetry of <strong>halving a parallelogram or rectangle</strong>!</p><p class='mt-2'>Every triangle with base $b$ and perpendicular altitude $h$ can be cloned. If you duplicate the triangle, rotate the copy $180^\\circ$, and glue it along the third side, the two congruent triangles form an exact <strong>parallelogram</strong> of base $b$ and height $h$!</p><p class='mt-2'>Since the parallelogram has area $\\text{base} \\times \\text{height}$, the single original triangle occupies exactly <strong>half</strong> of that area:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of Triangle} = \\frac{1}{2} \\times \\text{Base} \\times \\text{Height} = \\frac{1}{2} b h$$</div><p class='mt-2'>This holds true for acute, right-angled, and obtuse triangles alike!</p>",
    "key_takeaways": [
      "Any triangle is exactly half of a parallelogram with the same base and perpendicular height.",
      "The area formula is strictly $\\frac{1}{2} \\times \\text{base} \\times \\text{perpendicular height}$.",
      "The height $h$ must always be perpendicular to the chosen base line (not the slanted side)."
    ],
    "formula": "$$\\text{Area}(\\triangle) = \\frac{1}{2} \\times b \\times h$$",
    "simulator_type": "triangle_half_rectangle_dissector",
    "checkpoints": [
      {
        "question": "A right-angled triangle has perpendicular legs of length $6\\text{ cm}$ and $8\\text{ cm}$, and a hypotenuse of $10\\text{ cm}$. What is its area?",
        "options": [
          "$48\\text{ cm}^2$",
          "$30\\text{ cm}^2$",
          "$24\\text{ cm}^2$",
          "$40\\text{ cm}^2$"
        ],
        "correct": 2,
        "explanation": "In a right triangle, the two perpendicular legs serve as the base and height: $\\text{Area} = \\frac{1}{2} \\times 6 \\times 8 = 24\\text{ cm}^2$."
      },
      {
        "question": "In an obtuse triangle, where does the perpendicular height line fall when drawn from the opposite vertex to the base?",
        "options": [
          "Always strictly inside the triangle",
          "Along the hypotenuse",
          "Outside the triangle on the extended base line",
          "It cannot be drawn"
        ],
        "correct": 2,
        "explanation": "For an obtuse triangle, the perpendicular dropped from the acute vertex opposite the obtuse angle meets the extension of the opposite base line outside the triangle."
      }
    ]
  },
  {
    "id": 5,
    "title": "Triangles & Parallels",
    "subtitle": "Triangles between Parallel Lines with a Common Base",
    "content": "<p>Here is one of the most remarkable theorems in geometry: <strong>Triangles on the same base and between the same parallel lines have equal areas!</strong></p><p class='mt-2'>Let base $AB$ lie on a line $L_1$, and let vertex $C$ lie on a line $L_2$ parallel to $L_1$ ($L_1 \\parallel L_2$).</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 text-center'><div class='text-cyan-300 font-bold'>Base = b (fixed length on $L_1$)</div><div class='text-amber-300 font-bold mt-1'>Distance between parallel lines = h (strictly constant everywhere)</div></div><p class='mt-2'>No matter where vertex $C$ slides along line $L_2$, the perpendicular distance $h$ to base $AB$ never changes! Because $\\text{Area} = \\frac{1}{2} b h$, and both $b$ and $h$ are constant:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area}(\\triangle ABC_1) = \\text{Area}(\\triangle ABC_2) = \\text{Area}(\\triangle ABC_3) = \\frac{1}{2} b h$$</div><p class='mt-2'>The shape shears dramatically from right to acute to obtuse, but its <strong>area is completely invariant</strong>!</p>",
    "key_takeaways": [
      "The perpendicular distance between two parallel lines is constant at all points.",
      "Triangles sharing a common base and having vertices on a line parallel to the base have identical areas.",
      "This shearing principle (Cavalieri's principle) allows continuous deformation without changing area."
    ],
    "formula": "$$L_1 \\parallel L_2 \\implies h = \\text{const} \\implies \\text{Area}(\\triangle ABC) = \\frac{1}{2} b h = \\text{invariant}$$",
    "simulator_type": "cavalieri_triangles_parallel_shearing",
    "checkpoints": [
      {
        "question": "Two triangles $\\triangle ABC$ and $\\triangle ABD$ share the same base $AB$. If the line connecting $C$ and $D$ is parallel to $AB$, how do their areas compare?",
        "options": [
          "$\\text{Area}(\\triangle ABC) > \\text{Area}(\\triangle ABD)$",
          "$\\text{Area}(\\triangle ABC) < \\text{Area}(\\triangle ABD)$",
          "Both triangles have strictly equal areas",
          "Their areas cannot be compared without knowing all side lengths"
        ],
        "correct": 2,
        "explanation": "Because $CD \\parallel AB$, both vertices $C$ and $D$ are at the exact same perpendicular height $h$ from the base $AB$. Since base and height are identical, their areas are strictly equal."
      },
      {
        "question": "A median of a triangle connects a vertex to the midpoint of the opposite side. How does a median divide the area of a triangle?",
        "options": [
          "Into two triangles of equal area",
          "In the ratio $1:2$",
          "In the ratio $1:3$",
          "It depends on the angles of the triangle"
        ],
        "correct": 0,
        "explanation": "Both halves share the same height $h$, and their bases are equal ($b/2$ each, by definition of midpoint). Thus each smaller triangle has area $\\frac{1}{2}(b/2)h = \\frac{1}{4}bh$, dividing the area into two equal halves."
      }
    ]
  },
  {
    "id": 6,
    "title": "Triangle Applications",
    "subtitle": "Heron's Formula & Altitude Partitioning",
    "content": "<p>What if you know all three side lengths of a triangle ($a, b, c$), but the perpendicular height $h$ is unknown? We use the celebrated <strong>Heron's Formula</strong>, discovered by Heron of Alexandria in 60 CE!</p><p class='mt-2'>First calculate the <strong>semi-perimeter</strong> $s$ (half of the perimeter):</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$s = \\frac{a + b + c}{2}$$</div><p class='mt-2'>Then the area is given by the symmetrical radical product:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area} = \\sqrt{s(s - a)(s - b)(s - c)}$$</div><p class='mt-2'>Once the area is known from Heron's formula, you can reverse-engineer any perpendicular height: $h_a = \\frac{2 \\times \\text{Area}}{a}$!</p>",
    "key_takeaways": [
      "Heron's formula computes triangle area directly from the 3 side lengths $a, b, c$ without needing an altitude.",
      "The semi-perimeter is $s = \\frac{a + b + c}{2}$.",
      "Any perpendicular height can be derived once the area is known: $h = \\frac{2A}{\\text{base}}$."
    ],
    "formula": "$$\\text{Area} = \\sqrt{s(s - a)(s - b)(s - c)}, \\qquad s = \\frac{a + b + c}{2}$$",
    "simulator_type": "triangle_altitude_heron_explorer",
    "checkpoints": [
      {
        "question": "What is the area of a triangle with side lengths $13\\text{ cm}, 14\\text{ cm}$, and $15\\text{ cm}$?",
        "options": [
          "$72\\text{ cm}^2$",
          "$84\\text{ cm}^2$",
          "$96\\text{ cm}^2$",
          "$105\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "$s = (13+14+15)/2 = 21$. Area = $\\sqrt{21(21-13)(21-14)(21-15)} = \\sqrt{21 \\times 8 \\times 7 \\times 6} = \\sqrt{7056} = 84\\text{ cm}^2$."
      },
      {
        "question": "What is the area of an equilateral triangle with side length $s$?",
        "options": [
          "$\\frac{1}{2} s^2$",
          "$\\frac{\\sqrt{3}}{4} s^2$",
          "$\\frac{\\sqrt{3}}{2} s^2$",
          "$\\frac{3}{4} s^2$"
        ],
        "correct": 1,
        "explanation": "Height of an equilateral triangle is $h = \\frac{\\sqrt{3}}{2}s$. Area = $\\frac{1}{2} \\times s \\times \\frac{\\sqrt{3}}{2}s = \\frac{\\sqrt{3}}{4}s^2$."
      }
    ]
  },
  {
    "id": 7,
    "title": "Parallelogram",
    "subtitle": "Base × Height: Dissecting and Shearing into a Rectangle",
    "content": "<p>A <strong>parallelogram</strong> has opposite sides that are parallel and equal in length. But how do we prove its area formula?</p><p class='mt-2'>Let a parallelogram have base $b$ and perpendicular height $h$. Drop a perpendicular line from one top vertex to the base line. This slices off a right-angled triangle from one side!</p><p class='mt-2'>Now pick up that sliced triangle, translate it across the figure, and fit it perfectly against the opposite slanted side. The parallelogram transforms into a <strong>standard rectangle</strong> with length $b$ and width $h$!</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of Parallelogram} = \\text{Base} \\times \\text{Perpendicular Height} = b \\times h$$</div><p class='mt-2'><strong>Caution:</strong> Never multiply the two adjacent side lengths ($a \\times b$) unless the angle between them is $90^\\circ$! The height $h$ is strictly the perpendicular distance between the parallel bases.</p>",
    "key_takeaways": [
      "A parallelogram can be rearranged into a rectangle of dimensions $b \\times h$ by translating a corner triangle.",
      "Area is strictly $\\text{base} \\times \\text{perpendicular height}$ ($b \\times h$).",
      "Slanted side length is always greater than perpendicular height ($a > h$) when angles are not $90^\\circ$."
    ],
    "formula": "$$\\text{Area}(\\text{Parallelogram}) = b \\times h = a b \\sin(\\theta)$$",
    "simulator_type": "parallelogram_shear_rect_converter",
    "checkpoints": [
      {
        "question": "A parallelogram has adjacent sides of length $10\\text{ cm}$ and $6\\text{ cm}$. The perpendicular distance between the $10\\text{ cm}$ sides is $4\\text{ cm}$. What is its area?",
        "options": [
          "$60\\text{ cm}^2$",
          "$40\\text{ cm}^2$",
          "$24\\text{ cm}^2$",
          "$20\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "Area = $\\text{Base} \\times \\text{Height} = 10\\text{ cm} \\times 4\\text{ cm} = 40\\text{ cm}^2$. The slanted side length of 6 cm is not used in the calculation."
      },
      {
        "question": "What is the perpendicular distance between the $6\\text{ cm}$ sides of the parallelogram described in the previous question?",
        "options": [
          "$4\\text{ cm}$",
          "$5.33\\text{ cm}$",
          "$6.67\\text{ cm}$",
          "$8\\text{ cm}$"
        ],
        "correct": 2,
        "explanation": "Area is constant ($40\\text{ cm}^2$). With base $b = 6\\text{ cm}$: $6 \\times h_2 = 40 \\implies h_2 = 40 / 6 = 6.67\\text{ cm}$."
      }
    ]
  },
  {
    "id": 8,
    "title": "Rhombus",
    "subtitle": "Perpendicular Diagonals: 1/2 × d1 × d2",
    "content": "<p>A <strong>rhombus</strong> is an equilateral parallelogram—all four sides have equal length $s$. Because it is a parallelogram, its area can be found by $\\text{base} \\times \\text{height}$. But a rhombus possesses a much more powerful property: its <strong>diagonals bisect each other at right angles ($90^\\circ$)</strong>!</p><p class='mt-2'>Let the two diagonals have lengths $d_1$ and $d_2$. The diagonals divide the rhombus into four identical right-angled triangles, each having legs of length $\\frac{d_1}{2}$ and $\\frac{d_2}{2}$:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center text-sm'>$$\\text{Area of 1 triangle} = \\frac{1}{2} \\times \\left(\\frac{d_1}{2}\\right) \\times \\left(\\frac{d_2}{2}\\right) = \\frac{d_1 d_2}{8}$$</div><p class='mt-2'>Multiplying by 4 triangles gives the universal rhombus formula:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of Rhombus} = 4 \\times \\left(\\frac{d_1 d_2}{8}\\right) = \\frac{1}{2} d_1 d_2$$</div><p class='mt-2'>The area of a rhombus is exactly <strong>half the product of its diagonals</strong>!</p>",
    "key_takeaways": [
      "The diagonals of a rhombus intersect perpendicularly at their midpoints.",
      "The four right-angled triangles formed by the diagonals each have area $\\frac{1}{8} d_1 d_2$.",
      "The total area of a rhombus is $\\frac{1}{2} \\times d_1 \\times d_2$."
    ],
    "formula": "$$\\text{Area}(\\text{Rhombus}) = \\frac{1}{2} d_1 d_2 = s \\times h$$",
    "simulator_type": "rhombus_diagonal_product_visualizer",
    "checkpoints": [
      {
        "question": "A decorative floor tile is shaped like a rhombus with diagonals of $16\\text{ cm}$ and $12\\text{ cm}$. What is the area of the tile?",
        "options": [
          "$192\\text{ cm}^2$",
          "$96\\text{ cm}^2$",
          "$48\\text{ cm}^2$",
          "$144\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "Area = $\\frac{1}{2} d_1 d_2 = \\frac{1}{2} \\times 16 \\times 12 = 96\\text{ cm}^2$."
      },
      {
        "question": "A square has diagonals of length $10\\text{ cm}$. Using the rhombus diagonal formula, what is its area?",
        "options": [
          "$25\\text{ cm}^2$",
          "$50\\text{ cm}^2$",
          "$100\\text{ cm}^2$",
          "$70.7\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "A square is a rhombus with equal diagonals ($d_1 = d_2 = 10$). Area = $\\frac{1}{2} d_1 d_2 = \\frac{1}{2} \\times 10 \\times 10 = 50\\text{ cm}^2$."
      }
    ]
  },
  {
    "id": 9,
    "title": "Trapezium",
    "subtitle": "Parallel Bases & Altitude: 1/2 × (a + b) × h",
    "content": "<p>A <strong>trapezium</strong> (or trapezoid) is a quadrilateral with at least one pair of parallel sides. Let the two parallel sides have lengths $a$ and $b$, and let the perpendicular distance between them be $h$.</p><p class='mt-2'>How do we find its area? Draw a diagonal across the trapezium! This slices the trapezium into two triangles:</p><ul><li><strong>Triangle 1:</strong> Base $a$, height $h \\implies \\text{Area}_1 = \\frac{1}{2} a h$</li><li><strong>Triangle 2:</strong> Base $b$, height $h \\implies \\text{Area}_2 = \\frac{1}{2} b h$</li></ul><p class='mt-2'>Adding both triangles gives:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area} = \\frac{1}{2} a h + \\frac{1}{2} b h = \\frac{1}{2} (a + b) h$$</div><p class='mt-2'>The area of a trapezium equals <strong>half the sum of parallel sides multiplied by the perpendicular distance between them</strong> (or the average base $\\frac{a+b}{2}$ times height $h$).</p>",
    "key_takeaways": [
      "A diagonal splits a trapezium into two triangles with bases $a$ and $b$, both sharing height $h$.",
      "Area of a trapezium is $\\frac{1}{2} (a + b) h$.",
      "The quantity $\\frac{a+b}{2}$ represents the average length of the parallel bases (the midline)."
    ],
    "formula": "$$\\text{Area}(\\text{Trapezium}) = \\frac{a + b}{2} \\times h = \\text{Midline} \\times h$$",
    "simulator_type": "trapezium_two_copies_rotator",
    "checkpoints": [
      {
        "question": "A trapezium has parallel sides of length $9\\text{ cm}$ and $15\\text{ cm}$, and a perpendicular height of $8\\text{ cm}$. What is its area?",
        "options": [
          "$96\\text{ cm}^2$",
          "$192\\text{ cm}^2$",
          "$72\\text{ cm}^2$",
          "$120\\text{ cm}^2$"
        ],
        "correct": 0,
        "explanation": "Area = $\\frac{1}{2}(a + b)h = \\frac{1}{2}(9 + 15) \\times 8 = \\frac{1}{2}(24) \\times 8 = 12 \\times 8 = 96\\text{ cm}^2$."
      },
      {
        "question": "The area of a trapezium is $120\\text{ cm}^2$ and its height is $10\\text{ cm}$. If one parallel base is $14\\text{ cm}$, what is the other parallel base?",
        "options": [
          "$8\\text{ cm}$",
          "$10\\text{ cm}$",
          "$12\\text{ cm}$",
          "$16\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "$\\frac{1}{2}(14 + b) \\times 10 = 120 \\implies 5(14 + b) = 120 \\implies 14 + b = 24 \\implies b = 10\\text{ cm}$."
      }
    ]
  },
  {
    "id": 10,
    "title": "Two-Copy Trapezium",
    "subtitle": "Finding the Area Using Two Copies of the Trapezium",
    "content": "<p>One of the most elegant geometric proofs of the trapezium area formula uses <strong>two congruent copies</strong> of the trapezium.</p><p class='mt-2'>Take two identical paper cut-outs of a trapezium with parallel sides $a$ and $b$, and height $h$. Rotate the second copy upside down ($180^\\circ$) and place it adjacent to the first along their non-parallel slanted edge.</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 text-center'><div class='text-cyan-300 font-bold'>Combined Figure: Parallelogram!</div><div class='text-amber-300 text-sm mt-1'>Base of Parallelogram = a + b &nbsp; | &nbsp; Height = h</div></div><p class='mt-2'>The area of this giant parallelogram is $\\text{Base} \\times \\text{Height} = (a + b) \\times h$. Since this parallelogram was built from <strong>two identical trapeziums</strong>, the area of a single trapezium is exactly half:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area of 1 Trapezium} = \\frac{1}{2} (a + b) h$$</div>",
    "key_takeaways": [
      "Joining two congruent trapeziums (one rotated $180^\\circ$) forms a parallelogram of base $(a + b)$ and height $h$.",
      "The area of the composite parallelogram is $(a + b) h$.",
      "Halving the parallelogram yields the formula $\\frac{1}{2}(a+b)h$ without needing algebraic fractions."
    ],
    "formula": "$$2 \\times \\text{Area}(\\text{Trapezium}) = \\text{Area}(\\text{Parallelogram}) = (a + b) h \\implies A = \\frac{1}{2}(a+b)h$$",
    "simulator_type": "trapezium_two_copies_rotator",
    "checkpoints": [
      {
        "question": "When two congruent trapeziums with parallel sides 6 cm and 10 cm and height 5 cm are joined into a parallelogram, what is the base of the parallelogram?",
        "options": [
          "10 cm",
          "12 cm",
          "16 cm",
          "20 cm"
        ],
        "correct": 2,
        "explanation": "The base of the joined parallelogram is the sum of the two parallel sides: $a + b = 6 + 10 = 16\\text{ cm}$."
      },
      {
        "question": "What is the area of the combined parallelogram from the previous question, and what does it confirm for the trapezium?",
        "options": [
          "Parallelogram is $80\\text{ cm}^2$, confirming trapezium area is $40\\text{ cm}^2$",
          "Parallelogram is $160\\text{ cm}^2$, confirming trapezium area is $80\\text{ cm}^2$",
          "Parallelogram is $50\\text{ cm}^2$, confirming trapezium area is $25\\text{ cm}^2$",
          "Parallelogram is $60\\text{ cm}^2$, confirming trapezium area is $30\\text{ cm}^2$"
        ],
        "correct": 0,
        "explanation": "Area of parallelogram = $\\text{base} \\times \\text{height} = 16 \\times 5 = 80\\text{ cm}^2$. Halving gives the single trapezium area: $80 / 2 = 40\\text{ cm}^2$."
      }
    ]
  },
  {
    "id": 11,
    "title": "Polygon Area",
    "subtitle": "Area of any Polygon: Triangulation & Surveyor Field Book",
    "content": "<p>Real-world land plots, estates, and architectural boundaries are rarely neat rectangles or trapeziums. How do land surveyors find the <strong>area of any general polygon</strong>?</p><p class='mt-2'>They use the method of <strong>triangulation</strong> and <strong>offset field-book partitioning</strong>:</p><ol class='list-decimal pl-5 space-y-1'><li>Draw a straight central baseline (a diagonal $AD$) across the polygon.</li><li>From each remaining vertex, drop perpendicular offsets to the baseline.</li><li>These offsets slice the complex polygon into elementary shapes: <strong>right triangles</strong> and <strong>trapeziums</strong>!</li><li>Calculate the area of each triangle ($\\frac{1}{2} b h$) and trapezium ($\\frac{1}{2}(a+b)h$).</li><li>Sum all sub-areas together to obtain the total polygon area.</li></ol><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Area}(\\text{Polygon}) = \\sum \\text{Area}(\\text{Triangles}) + \\sum \\text{Area}(\\text{Trapeziums})$$</div>",
    "key_takeaways": [
      "Any polygon can be partitioned into non-overlapping triangles and trapeziums by drawing a diagonal and dropping perpendicular offsets.",
      "Land surveyors record offset distances along a central baseline in a field book.",
      "The total polygon area is strictly the arithmetic sum of the sub-divided triangles and trapeziums."
    ],
    "formula": "$$\\text{Area}(\\text{Polygon}) = \\sum_{i} A(\\triangle_i) + \\sum_{j} A(\\text{Trapezium}_j)$$",
    "simulator_type": "polygon_triangulation_surveyor_lab",
    "checkpoints": [
      {
        "question": "A quadrilateral has a diagonal of length $20\\text{ cm}$. The perpendicular offsets drawn to this diagonal from the other two vertices are $6\\text{ cm}$ and $9\\text{ cm}$. What is the area of the quadrilateral?",
        "options": [
          "$300\\text{ cm}^2$",
          "$150\\text{ cm}^2$",
          "$120\\text{ cm}^2$",
          "$180\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "The diagonal divides the quadrilateral into two triangles sharing base $d = 20\\text{ cm}$. $\\text{Area} = \\frac{1}{2} d(h_1 + h_2) = \\frac{1}{2}(20)(6 + 9) = 10(15) = 150\\text{ cm}^2$."
      },
      {
        "question": "Why is triangulation considered the most universal method in land surveying?",
        "options": [
          "Because triangles are the only shapes that have perpendicular heights",
          "Because any $n$-sided polygon can always be triangulated into $(n - 2)$ triangles",
          "Because all surveyed lands are triangular",
          "Because triangles always have equal side lengths"
        ],
        "correct": 1,
        "explanation": "Every polygon with $n$ vertices can be triangulated into $(n - 2)$ triangles using diagonals that do not intersect, allowing universal calculation."
      }
    ]
  },
  {
    "id": 12,
    "title": "Apothem & Perimeter",
    "subtitle": "Regular Polygons: 1/2 × Perimeter × Apothem",
    "content": "<p>A <strong>regular polygon</strong> has all sides equal and all interior angles equal (e.g., regular pentagon, hexagon, octagon). What is the formula for its area?</p><p class='mt-2'>Every regular $n$-sided polygon has an <strong>incircle</strong>. The perpendicular distance from the center to any side is called the <strong>apothem</strong> ($r$ or $a$).</p><p class='mt-2'>Drawing line segments from the center to all $n$ vertices divides the polygon into $n$ congruent triangles, each having base $s$ and height $r$:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center text-sm'>$$\\text{Area of 1 triangle} = \\frac{1}{2} s r$$</div><p class='mt-2'>Summing all $n$ triangles gives:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Total Area} = n \\times \\left(\\frac{1}{2} s r\\right) = \\frac{1}{2} (n s) r = \\frac{1}{2} \\times \\text{Perimeter} \\times \\text{Apothem}$$</div><p class='mt-2'>As the number of sides $n \\to \\infty$, the perimeter approaches $2\\pi r$, and the area becomes $\\frac{1}{2}(2\\pi r)r = \\pi r^2$—the area of a circle!</p>",
    "key_takeaways": [
      "The apothem is the perpendicular distance from the center of a regular polygon to the midpoint of any side.",
      "A regular polygon with $n$ sides is composed of $n$ congruent isosceles triangles.",
      "Area of any regular polygon is $\\frac{1}{2} \\times \\text{Perimeter} \\times \\text{Apothem}$."
    ],
    "formula": "$$\\text{Area}(\\text{Regular Polygon}) = \\frac{1}{2} P \\cdot r, \\qquad P = n \\cdot s$$",
    "simulator_type": "regular_polygon_apothem_unfolder",
    "checkpoints": [
      {
        "question": "A regular hexagon has a side length of $6\\text{ cm}$ and an apothem of $5.2\\text{ cm}$. What is its area?",
        "options": [
          "$62.4\\text{ cm}^2$",
          "$93.6\\text{ cm}^2$",
          "$124.8\\text{ cm}^2$",
          "$187.2\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "Perimeter $P = 6 \\times 6 = 36\\text{ cm}$. Area = $\\frac{1}{2} P \\cdot r = \\frac{1}{2} \\times 36 \\times 5.2 = 18 \\times 5.2 = 93.6\\text{ cm}^2$."
      },
      {
        "question": "If you unfold the 6 triangles of a regular hexagon into an alternating row, what shape do they approximate?",
        "options": [
          "A circle",
          "A parallelogram of base equal to half the perimeter and height equal to the apothem",
          "A cube",
          "An isosceles trapezoid"
        ],
        "correct": 1,
        "explanation": "Interlocking the triangles creates a parallelogram with base $\\frac{P}{2}$ and height $r$, confirming area = $\\frac{P}{2} \\times r = \\frac{1}{2} P r$."
      }
    ]
  },
  {
    "id": 13,
    "title": "Composite Shapes",
    "subtitle": "Possibilities: Combining & Subtracting Geometric Shapes",
    "content": "<p>In real-world design, floor plans and architectural elevations are rarely single polygons; they are <strong>composite shapes</strong> formed by joining or removing simpler figures.</p><p class='mt-2'>Two primary strategies solve all composite area challenges:</p><ol class='list-decimal pl-5 space-y-1'><li><strong>Additive Decomposition:</strong> Slice an L-shaped room into two rectangles, or a house elevation into a triangle (roof) plus a rectangle (walls):<br>$$\\text{Total Area} = \\text{Area}_1 + \\text{Area}_2$$</li><li><strong>Subtractive Decomposition:</strong> Enclose the figure in a simple bounding rectangle and subtract empty cutout corners, or calculate a circular washer/picture frame by subtracting inner area from outer area:<br>$$\\text{Shaded Area} = \\text{Area}(\\text{Outer}) - \\text{Area}(\\text{Hole})$$</li></ol>",
    "key_takeaways": [
      "Composite figures can be calculated by adding sub-regions or subtracting cutout cavities.",
      "Picture frames, paths around parks, and washers always use outer area minus inner area.",
      "Always ensure shared boundary dimensions are correctly deduced before calculating component areas."
    ],
    "formula": "$$\\text{Additive: } A = A_1 + A_2 + \\dots + A_k, \\qquad \\text{Subtractive: } A = A_{\\text{outer}} - A_{\\text{inner}}$$",
    "simulator_type": "composite_shape_additive_subtractive_sim",
    "checkpoints": [
      {
        "question": "A concrete path $2\\text{ m}$ wide runs around the outside of a rectangular garden of dimensions $20\\text{ m} \\times 15\\text{ m}$. What is the area of the path?",
        "options": [
          "$156\\text{ m}^2$",
          "$140\\text{ m}^2$",
          "$160\\text{ m}^2$",
          "$300\\text{ m}^2$"
        ],
        "correct": 0,
        "explanation": "Inner garden area = $20 \\times 15 = 300\\text{ m}^2$. Outer dimensions = $(20 + 4) \\times (15 + 4) = 24 \\times 19 = 456\\text{ m}^2$. Path area = $456 - 300 = 156\\text{ m}^2$."
      },
      {
        "question": "An L-shaped room has outer dimensions $10\\text{ m} \\times 8\\text{ m}$ with a cutout corner of $4\\text{ m} \\times 3\\text{ m}$. What is its floor area?",
        "options": [
          "$68\\text{ m}^2$",
          "$72\\text{ m}^2$",
          "$80\\text{ m}^2$",
          "$64\\text{ m}^2$"
        ],
        "correct": 0,
        "explanation": "By subtractive decomposition: Bounding rectangle = $10 \\times 8 = 80\\text{ m}^2$. Cutout = $4 \\times 3 = 12\\text{ m}^2$. Room floor area = $80 - 12 = 68\\text{ m}^2$."
      }
    ]
  },
  {
    "id": 14,
    "title": "Areas in Real Life",
    "subtitle": "Flooring, Paint, Agriculture & Land Surveying",
    "content": "<p>Where does area impact our everyday lives? In construction, interior design, manufacturing, and farming, area is the direct foundation of <strong>material budgeting and cost calculation</strong>!</p><p class='mt-2'>Key real-world applications include:</p><ul><li><strong>Tiling a Floor:</strong> Number of tiles = $\\frac{\\text{Total Floor Area}}{\\text{Area of 1 Tile}}$.</li><li><strong>Wall Painting:</strong> Paint coverage is rated in $\\text{m}^2 / \\text{liter}$. Subtract window and door cutouts to determine the net paintable area!</li><li><strong>Agricultural Yield & Fertilizer:</strong> Fertilizer and seed quantities are specified per hectare ($1\\text{ hectare} = 10,000\\text{ m}^2$) or per acre ($1\\text{ acre} \\approx 4047\\text{ m}^2$).</li><li><strong>Fabric & Carpeting:</strong> Fabric rolls have fixed widths; finding pattern cutouts minimizes fabric scrap waste.</li></ul>",
    "key_takeaways": [
      "Number of tiles or bricks required is always $\\frac{\\text{Total Area}}{\\text{Single Tile Area}}$.",
      "Painting and plastering calculations require subtracting door and window openings from gross wall area.",
      "Standard large area units: $1\\text{ hectare} = 10,000\\text{ m}^2$, $1\\text{ km}^2 = 1,000,000\\text{ m}^2$."
    ],
    "formula": "$$\\text{Tiles} = \\frac{\\text{Area}_{\\text{floor}}}{\\text{Area}_{\\text{tile}}}, \\qquad \\text{Total Cost} = \\text{Net Area} \\times \\text{Rate per unit area}$$",
    "simulator_type": "real_life_cost_coverage_calculator",
    "checkpoints": [
      {
        "question": "A room floor is $6\\text{ m} \\times 4\\text{ m}$. How many square tiles of side $40\\text{ cm}$ are needed to cover the floor?",
        "options": [
          "120 tiles",
          "150 tiles",
          "180 tiles",
          "200 tiles"
        ],
        "correct": 1,
        "explanation": "Floor area = $600\\text{ cm} \\times 400\\text{ cm} = 240,000\\text{ cm}^2$. Tile area = $40 \\times 40 = 1,600\\text{ cm}^2$. Number of tiles = $240,000 / 1,600 = 150$ tiles."
      },
      {
        "question": "A farmer has a rectangular field $250\\text{ m}$ long and $160\\text{ m}$ wide. What is the area of the field in hectares?",
        "options": [
          "4 hectares",
          "40 hectares",
          "400 hectares",
          "0.4 hectares"
        ],
        "correct": 0,
        "explanation": "Area = $250 \\times 160 = 40,000\\text{ m}^2$. Since $1\\text{ hectare} = 10,000\\text{ m}^2$, the area is $40,000 / 10,000 = 4$ hectares."
      }
    ]
  },
  {
    "id": 15,
    "title": "Area Scaling",
    "subtitle": "Scaling Laws: Area Scales as k^2 with Linear Scale k",
    "content": "<p>What happens to the area of a polygon when its dimensions are enlarged or shrunk by a scale factor $k$?</p><p class='mt-2'>Suppose every linear dimension of a polygon is multiplied by $k$ (for example, doubling: $k = 2$):</p><ul><li>Lengths scale linearly: $\\text{Length}' = k \\times \\text{Length}$</li><li>Perimeter scales linearly: $\\text{Perimeter}' = k \\times \\text{Perimeter}$</li><li><strong>Area scales quadratically:</strong> $\\mathbf{\\text{Area}' = k^2 \\times \\text{Area}}$!</li></ul><p class='mt-2'>If you double the dimensions of a map ($k = 2$), the surface area quadruples ($2^2 = 4$). If you scale by $k = 3$, the area increases 9-fold ($3^2 = 9$). If dimensions are halved ($k = \\frac{1}{2}$), the area shrinks to one-quarter ($\\frac{1}{4}$)!</p>",
    "key_takeaways": [
      "Linear dimensions scale by $k$; 2D areas scale by $k^2$.",
      "Doubling all sides of any 2D figure quadruples its enclosed area ($2^2 = 4$).",
      "This fundamental quadratic scaling law applies to all geometric shapes: circles, triangles, polygons."
    ],
    "formula": "$$\\text{Length} \\to k \\cdot L, \\quad \\text{Perimeter} \\to k \\cdot P, \\quad \\mathbf{\\text{Area} \\to k^2 \\cdot A}$$",
    "simulator_type": "area_scaling_k_squared_visualizer",
    "checkpoints": [
      {
        "question": "A blueprint with scale factor $1:50$ shows a patio of area $12\\text{ cm}^2$. What is the actual patio area in square meters in real life?",
        "options": [
          "$3\\text{ m}^2$",
          "$6\\text{ m}^2$",
          "$30\\text{ m}^2$",
          "$300\\text{ m}^2$"
        ],
        "correct": 0,
        "explanation": "Scale factor $k = 50$. Actual area in $\\text{cm}^2 = 12 \\times 50^2 = 12 \\times 2500 = 30,000\\text{ cm}^2$. Since $1\\text{ m}^2 = 10,000\\text{ cm}^2$, the actual area is $30,000 / 10,000 = 3\\text{ m}^2$."
      },
      {
        "question": "If you reduce the radius of a circular pizza by half, what fraction of the original pizza area remains?",
        "options": [
          "One-half (1/2)",
          "One-third (1/3)",
          "One-quarter (1/4)",
          "One-eighth (1/8)"
        ],
        "correct": 2,
        "explanation": "Because area scales as $k^2$, with scale factor $k = 1/2$, the new area is $(1/2)^2 = 1/4$ of the original area."
      }
    ]
  },
  {
    "id": 16,
    "title": "Area Matrix",
    "subtitle": "The Comprehensive 2D Area Formula Matrix",
    "content": "<p>Here is our complete master reference matrix of 2D polygon area formulas:</p><div class='overflow-x-auto my-2'><table class='w-full text-left text-xs border border-indigo-500/30 rounded'><thead class='bg-indigo-950/60 text-cyan-300'><tr><th class='p-2'>Polygon</th><th class='p-2'>Parameters</th><th class='p-2'>Area Formula</th></tr></thead><tbody class='divide-y divide-slate-800 text-slate-300'><tr><td class='p-2 font-bold text-white'>Rectangle</td><td class='p-2'>Length $L$, Width $W$</td><td class='p-2 font-mono text-emerald-300'>A = L \\times W</td></tr><tr><td class='p-2 font-bold text-white'>Square</td><td class='p-2'>Side $s$</td><td class='p-2 font-mono text-emerald-300'>A = s^2</td></tr><tr><td class='p-2 font-bold text-white'>Triangle</td><td class='p-2'>Base $b$, Height $h$</td><td class='p-2 font-mono text-emerald-300'>A = \\frac{1}{2} b h</td></tr><tr><td class='p-2 font-bold text-white'>Parallelogram</td><td class='p-2'>Base $b$, Height $h$</td><td class='p-2 font-mono text-emerald-300'>A = b \\times h</td></tr><tr><td class='p-2 font-bold text-white'>Rhombus</td><td class='p-2'>Diagonals $d_1, d_2$</td><td class='p-2 font-mono text-emerald-300'>A = \\frac{1}{2} d_1 d_2</td></tr><tr><td class='p-2 font-bold text-white'>Trapezium</td><td class='p-2'>Parallel sides $a, b$, Height $h$</td><td class='p-2 font-mono text-emerald-300'>A = \\frac{1}{2}(a + b) h</td></tr><tr><td class='p-2 font-bold text-white'>Regular Polygon</td><td class='p-2'>Perimeter $P$, Apothem $r$</td><td class='p-2 font-mono text-emerald-300'>A = \\frac{1}{2} P r</td></tr></tbody></table></div>",
    "key_takeaways": [
      "All polygon area formulas stem from the rectangular grid product $L \\times W$.",
      "Triangles, rhombuses, and trapeziums feature the factor $\\frac{1}{2}$ because each can be doubled into an enclosing rectangle or parallelogram.",
      "General polygons are evaluated by triangulation into component sub-regions."
    ],
    "formula": "$$\\text{Mensuration Matrix: } \\text{Rectangle} \\to \\text{Triangle} \\to \\text{Parallelogram} \\to \\text{Rhombus} \\to \\text{Trapezium} \\to \\text{Polygon}$$",
    "simulator_type": "area_formulas_interactive_matrix",
    "checkpoints": [
      {
        "question": "Which polygon area formula does NOT include the factor $\\frac{1}{2}$?",
        "options": [
          "Triangle",
          "Rhombus",
          "Parallelogram",
          "Trapezium"
        ],
        "correct": 2,
        "explanation": "A parallelogram has area $b \\times h$. Triangles, rhombuses, and trapeziums all include the factor $\\frac{1}{2}$ because they represent half of their respective bounding parallelograms."
      },
      {
        "question": "If you know only the perimeter of a regular hexagon, what additional measurement is required to calculate its area using the formula $\\frac{1}{2} P r$?",
        "options": [
          "The weight of the hexagon",
          "The apothem (perpendicular distance from center to side)",
          "The color of the border",
          "The coordinates of the origin"
        ],
        "correct": 1,
        "explanation": "The formula $\\text{Area} = \\frac{1}{2} P r$ requires the perimeter $P$ and the apothem $r$."
      }
    ]
  },
  {
    "id": 17,
    "title": "Mastery Challenge • Part I",
    "subtitle": "Questions 1–10: Rectangles, Squares, Perimeter vs Area & Triangles",
    "questions": [
      {
        "id": 1,
        "question": "A rectangle has length $14\\text{ cm}$ and width $9\\text{ cm}$. What is its area?",
        "options": ["$116\\text{ cm}^2$", "$126\\text{ cm}^2$", "$136\\text{ cm}^2$", "$146\\text{ cm}^2$"],
        "correct": 1,
        "solution": "$\\text{Area} = \\text{Length} \\times \\text{Width} = 14\\text{ cm} \\times 9\\text{ cm} = 126\\text{ cm}^2$."
      },
      {
        "id": 2,
        "question": "The area of a square is $144\\text{ cm}^2$. What is its perimeter?",
        "options": ["$36\\text{ cm}$", "$48\\text{ cm}$", "$56\\text{ cm}$", "$72\\text{ cm}$"],
        "correct": 1,
        "solution": "Side $s = \\sqrt{144} = 12\\text{ cm}$.<br>Perimeter $P = 4s = 4 \\times 12 = 48\\text{ cm}$."
      },
      {
        "id": 3,
        "question": "A wire of length $36\\text{ cm}$ is bent into a rectangle of maximum possible area. What is this maximum area?",
        "options": ["$72\\text{ cm}^2$", "$80\\text{ cm}^2$", "$81\\text{ cm}^2$", "$90\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Perimeter $P = 36\\text{ cm} \\implies L + W = 18\\text{ cm}$.<br>The product $L \\times W$ is maximized when the rectangle is a square: $L = W = 18 / 2 = 9\\text{ cm}$.<br>Maximum Area = $9 \\times 9 = 81\\text{ cm}^2$."
      },
      {
        "id": 4,
        "question": "A triangle has base $16\\text{ cm}$ and altitude $7.5\\text{ cm}$. What is its area?",
        "options": ["$50\\text{ cm}^2$", "$60\\text{ cm}^2$", "$70\\text{ cm}^2$", "$120\\text{ cm}^2$"],
        "correct": 1,
        "solution": "$\\text{Area} = \\frac{1}{2} b h = \\frac{1}{2} \\times 16 \\times 7.5 = 8 \\times 7.5 = 60\\text{ cm}^2$."
      },
      {
        "id": 5,
        "question": "If the base of a triangle is doubled and its height is halved, what happens to its area?",
        "options": ["It doubles", "It is halved", "It remains unchanged", "It quadruples"],
        "correct": 2,
        "solution": "New Area = $\\frac{1}{2}(2b)\\left(\\frac{h}{2}\\right) = \\frac{1}{2} b h = \\text{Original Area}$. The area remains invariant."
      },
      {
        "id": 6,
        "question": "An isosceles right-angled triangle has an area of $50\\text{ cm}^2$. What is the length of each of its two equal perpendicular legs?",
        "options": ["$5\\text{ cm}$", "$10\\text{ cm}$", "$12\\text{ cm}$", "$15\\text{ cm}$"],
        "correct": 1,
        "solution": "Area = $\\frac{1}{2} x^2 = 50 \\implies x^2 = 100 \\implies x = 10\\text{ cm}$."
      },
      {
        "id": 7,
        "question": "What is the area of a right-angled triangle whose hypotenuse is $13\\text{ cm}$ and one leg is $5\\text{ cm}$?",
        "options": ["$25\\text{ cm}^2$", "$30\\text{ cm}^2$", "$60\\text{ cm}^2$", "$65\\text{ cm}^2$"],
        "correct": 1,
        "solution": "By the Baudhāyana-Pythagoras theorem: other leg = $\\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ cm}$.<br>$\\text{Area} = \\frac{1}{2} \\times 5 \\times 12 = 30\\text{ cm}^2$."
      },
      {
        "id": 8,
        "question": "Two triangles are between the same parallel lines. Triangle 1 has base $8\\text{ cm}$ and Triangle 2 has base $12\\text{ cm}$. What is the ratio of their areas?",
        "options": ["$1:2$", "$2:3$", "$4:9$", "$1:1$"],
        "correct": 1,
        "solution": "Since both are between the same parallel lines, their heights are equal: $h_1 = h_2 = h$.<br>Ratio of areas = $\\frac{\\frac{1}{2}(8)h}{\\frac{1}{2}(12)h} = \\frac{8}{12} = \\frac{2}{3}$."
      },
      {
        "id": 9,
        "question": "A rectangle has perimeter $30\\text{ cm}$ and length $10\\text{ cm}$. What is its area?",
        "options": ["$40\\text{ cm}^2$", "$50\\text{ cm}^2$", "$60\\text{ cm}^2$", "$70\\text{ cm}^2$"],
        "correct": 1,
        "solution": "$2(L + W) = 30 \\implies 10 + W = 15 \\implies W = 5\\text{ cm}$.<br>Area = $L \\times W = 10 \\times 5 = 50\\text{ cm}^2$."
      },
      {
        "id": 10,
        "question": "What is the semi-perimeter $s$ of a triangle with sides $7\\text{ cm}, 8\\text{ cm}$, and $9\\text{ cm}$?",
        "options": ["$12\\text{ cm}$", "$14\\text{ cm}$", "$24\\text{ cm}$", "$28\\text{ cm}$"],
        "correct": 0,
        "solution": "$s = \\frac{a + b + c}{2} = \\frac{7 + 8 + 9}{2} = \\frac{24}{2} = 12\\text{ cm}$."
      }
    ]
  },
  {
    "id": 18,
    "title": "Mastery Challenge • Part II",
    "subtitle": "Questions 11–20: Parallelograms, Rhombuses & Shearing Invariance",
    "questions": [
      {
        "id": 11,
        "question": "A parallelogram has base $15\\text{ cm}$ and corresponding height $8\\text{ cm}$. What is its area?",
        "options": ["$60\\text{ cm}^2$", "$90\\text{ cm}^2$", "$120\\text{ cm}^2$", "$150\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Area = $\\text{Base} \\times \\text{Height} = 15\\text{ cm} \\times 8\\text{ cm} = 120\\text{ cm}^2$."
      },
      {
        "id": 12,
        "question": "The area of a parallelogram is $72\\text{ cm}^2$ and its base is $12\\text{ cm}$. What is its perpendicular height?",
        "options": ["$4\\text{ cm}$", "$6\\text{ cm}$", "$8\\text{ cm}$", "$9\\text{ cm}$"],
        "correct": 1,
        "solution": "$\\text{Height} = \\frac{\\text{Area}}{\\text{Base}} = \\frac{72}{12} = 6\\text{ cm}$."
      },
      {
        "id": 13,
        "question": "A rhombus has diagonals of length $18\\text{ cm}$ and $10\\text{ cm}$. What is its area?",
        "options": ["$45\\text{ cm}^2$", "$90\\text{ cm}^2$", "$180\\text{ cm}^2$", "$135\\text{ cm}^2$"],
        "correct": 1,
        "solution": "$\\text{Area} = \\frac{1}{2} d_1 d_2 = \\frac{1}{2} \\times 18 \\times 10 = 90\\text{ cm}^2$."
      },
      {
        "id": 14,
        "question": "The area of a rhombus is $84\\text{ cm}^2$ and one diagonal is $14\\text{ cm}$. What is the length of the other diagonal?",
        "options": ["$6\\text{ cm}$", "$10\\text{ cm}$", "$12\\text{ cm}$", "$14\\text{ cm}$"],
        "correct": 2,
        "solution": "$\\frac{1}{2} \\times 14 \\times d_2 = 84 \\implies 7 d_2 = 84 \\implies d_2 = 12\\text{ cm}$."
      },
      {
        "id": 15,
        "question": "A rhombus has side length $10\\text{ cm}$ and perpendicular height $7.2\\text{ cm}$. What is its area?",
        "options": ["$36\\text{ cm}^2$", "$54\\text{ cm}^2$", "$72\\text{ cm}^2$", "$144\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Because every rhombus is a parallelogram: $\\text{Area} = \\text{base} \\times \\text{height} = 10\\text{ cm} \\times 7.2\\text{ cm} = 72\\text{ cm}^2$."
      },
      {
        "id": 16,
        "question": "If a rhombus has diagonals of $16\\text{ cm}$ and $12\\text{ cm}$, what is the length of its side $s$?",
        "options": ["$8\\text{ cm}$", "$10\\text{ cm}$", "$14\\text{ cm}$", "$20\\text{ cm}$"],
        "correct": 1,
        "solution": "The diagonals bisect each other at $90^\\circ$, creating right triangles with legs $\\frac{16}{2} = 8$ and $\\frac{12}{2} = 6$.<br>Side $s = \\sqrt{8^2 + 6^2} = \\sqrt{64 + 36} = \\sqrt{100} = 10\\text{ cm}$."
      },
      {
        "id": 17,
        "question": "A rectangle and a parallelogram have the same base and lie between the same parallel lines. How do their areas compare?",
        "options": [
          "The rectangle has larger area",
          "The parallelogram has larger area",
          "Both have exactly equal area",
          "It depends on the slant angle"
        ],
        "correct": 2,
        "solution": "Both have the exact same base $b$ and the exact same perpendicular height $h$. By Cavalieri's shearing principle, their areas are identically $b \\times h$."
      },
      {
        "id": 18,
        "question": "A parallelogram has adjacent sides of $8\\text{ cm}$ and $12\\text{ cm}$. Can its area ever exceed $96\\text{ cm}^2$?",
        "options": [
          "Yes, if the angles are very sharp",
          "No, the maximum area is $8 \\times 12 = 96\\text{ cm}^2$, occurring only when it is a rectangle",
          "Yes, if the diagonals are equal",
          "It is always $96\\text{ cm}^2$"
        ],
        "correct": 1,
        "solution": "Area = $a b \\sin(\\theta)$. Since $\\sin(\\theta) \\le 1$, the maximum possible area is $a \\times b = 8 \\times 12 = 96\\text{ cm}^2$, attained when $\\theta = 90^\\circ$ (a rectangle)."
      },
      {
        "id": 19,
        "question": "In a rhombus, each side is $13\\text{ cm}$ and one diagonal is $24\\text{ cm}$. What is the area of the rhombus?",
        "options": ["$120\\text{ cm}^2$", "$140\\text{ cm}^2$", "$156\\text{ cm}^2$", "$240\\text{ cm}^2$"],
        "correct": 0,
        "solution": "Half-diagonal $d_1/2 = 12\\text{ cm}$.<br>Other half-diagonal = $\\sqrt{13^2 - 12^2} = \\sqrt{169 - 144} = \\sqrt{25} = 5\\text{ cm} \\implies d_2 = 10\\text{ cm}$.<br>Area = $\\frac{1}{2} d_1 d_2 = \\frac{1}{2} \\times 24 \\times 10 = 120\\text{ cm}^2$."
      },
      {
        "id": 20,
        "question": "What is the area of a square tile with diagonal $8\\text{ cm}$?",
        "options": ["$16\\text{ cm}^2$", "$32\\text{ cm}^2$", "$48\\text{ cm}^2$", "$64\\text{ cm}^2$"],
        "correct": 1,
        "solution": "A square is a rhombus with equal diagonals ($d_1 = d_2 = 8\\text{ cm}$).<br>Area = $\\frac{1}{2} d^2 = \\frac{1}{2} \\times 8 \\times 8 = 32\\text{ cm}^2$."
      }
    ]
  },
  {
    "id": 19,
    "title": "Mastery Challenge • Part III",
    "subtitle": "Questions 21–30: Trapeziums, Two-Copy Proofs & Polygon Triangulation",
    "questions": [
      {
        "id": 21,
        "question": "A trapezium has parallel sides of length $12\\text{ cm}$ and $18\\text{ cm}$, and perpendicular height $6\\text{ cm}$. What is its area?",
        "options": ["$72\\text{ cm}^2$", "$90\\text{ cm}^2$", "$108\\text{ cm}^2$", "$180\\text{ cm}^2$"],
        "correct": 1,
        "solution": "Area = $\\frac{1}{2}(a + b)h = \\frac{1}{2}(12 + 18) \\times 6 = \\frac{1}{2}(30) \\times 6 = 15 \\times 6 = 90\\text{ cm}^2$."
      },
      {
        "id": 22,
        "question": "Two identical copies of a trapezium with parallel bases $7\\text{ cm}$ and $11\\text{ cm}$ and height $4\\text{ cm}$ are joined into a parallelogram. What is the area of the parallelogram?",
        "options": ["$36\\text{ cm}^2$", "$54\\text{ cm}^2$", "$72\\text{ cm}^2$", "$144\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Base of parallelogram = $7 + 11 = 18\\text{ cm}$.<br>Area of parallelogram = $\\text{base} \\times \\text{height} = 18 \\times 4 = 72\\text{ cm}^2$."
      },
      {
        "id": 23,
        "question": "The area of a trapezium is $105\\text{ cm}^2$. The parallel sides are in the ratio $2:3$, and the height is $7\\text{ cm}$. What are the lengths of the parallel sides?",
        "options": [
          "$10\\text{ cm}$ and $15\\text{ cm}$",
          "$12\\text{ cm}$ and $18\\text{ cm}$",
          "$8\\text{ cm}$ and $12\\text{ cm}$",
          "$14\\text{ cm}$ and $21\\text{ cm}$"
        ],
        "correct": 1,
        "solution": "Let bases be $2x$ and $3x$.<br>Area = $\\frac{1}{2}(2x + 3x) \\times 7 = 105 \\implies \\frac{1}{2}(5x)(7) = 105 \\implies 35x = 210 \\implies x = 6$.<br>Bases are $2(6) = 12\\text{ cm}$ and $3(6) = 18\\text{ cm}$."
      },
      {
        "id": 24,
        "question": "In a quadrilateral $ABCD$, diagonal $AC = 18\\text{ cm}$. The perpendiculars dropped from $B$ and $D$ to $AC$ are $5\\text{ cm}$ and $7\\text{ cm}$ respectively. What is the area of $ABCD$?",
        "options": ["$90\\text{ cm}^2$", "$108\\text{ cm}^2$", "$126\\text{ cm}^2$", "$216\\text{ cm}^2$"],
        "correct": 1,
        "solution": "$\\text{Area} = \\frac{1}{2} AC (h_1 + h_2) = \\frac{1}{2}(18)(5 + 7) = 9(12) = 108\\text{ cm}^2$."
      },
      {
        "id": 25,
        "question": "A field in the shape of a trapezium has parallel sides of $100\\text{ m}$ and $250\\text{ m}$, and the distance between them is $80\\text{ m}$. What is its area in hectares?",
        "options": ["$1.4\\text{ hectares}$", "$1.8\\text{ hectares}$", "$2.8\\text{ hectares}$", "$3.5\\text{ hectares}$"],
        "correct": 0,
        "solution": "Area = $\\frac{1}{2}(100 + 250) \\times 80 = \\frac{1}{2}(350)(80) = 350 \\times 40 = 14,000\\text{ m}^2$.<br>In hectares ($10,000\\text{ m}^2 = 1\\text{ ha}$): $14,000 / 10,000 = 1.4\\text{ hectares}$."
      },
      {
        "id": 26,
        "question": "A regular octagon has perimeter $48\\text{ cm}$ and apothem $7.2\\text{ cm}$. What is its area?",
        "options": ["$172.8\\text{ cm}^2$", "$245.6\\text{ cm}^2$", "$345.6\\text{ cm}^2$", "$691.2\\text{ cm}^2$"],
        "correct": 0,
        "solution": "Area = $\\frac{1}{2} P r = \\frac{1}{2} \\times 48 \\times 7.2 = 24 \\times 7.2 = 172.8\\text{ cm}^2$."
      },
      {
        "id": 27,
        "question": "A trapezium has parallel sides of $20\\text{ cm}$ and $10\\text{ cm}$, and non-parallel sides of $13\\text{ cm}$ each (isosceles trapezium). What is its height?",
        "options": ["$10\\text{ cm}$", "$11\\text{ cm}$", "$12\\text{ cm}$", "$13\\text{ cm}$"],
        "correct": 2,
        "solution": "Difference of bases = $20 - 10 = 10\\text{ cm}$. Each right-triangle base projection = $10 / 2 = 5\\text{ cm}$.<br>By Pythagoras theorem: $h = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ cm}$."
      },
      {
        "id": 28,
        "question": "Using the dimensions from the previous question (bases 20 cm and 10 cm, height 12 cm), what is the area of the isosceles trapezium?",
        "options": ["$150\\text{ cm}^2$", "$180\\text{ cm}^2$", "$200\\text{ cm}^2$", "$240\\text{ cm}^2$"],
        "correct": 1,
        "solution": "Area = $\\frac{1}{2}(a + b)h = \\frac{1}{2}(20 + 10) \\times 12 = 15 \\times 12 = 180\\text{ cm}^2$."
      },
      {
        "id": 29,
        "question": "In surveyor field notes, a baseline $AD = 80\\text{ m}$ has offsets $BF = 20\\text{ m}$ (at distance $AF = 30\\text{ m}$) and $CE = 30\\text{ m}$ (at distance $AE = 60\\text{ m}$) on opposite sides. This naturally decomposes the plot into:",
        "options": [
          "Four right-angled triangles",
          "Two right-angled triangles and one rectangle",
          "Right-angled triangles and trapeziums",
          "Equilateral triangles only"
        ],
        "correct": 2,
        "solution": "Offsets dropped perpendicularly from a straight survey baseline produce right-angled triangles at the outer apex ends and trapeziums in the intermediate segments between successive offset stations."
      },
      {
        "id": 30,
        "question": "The midline (segment connecting midpoints of non-parallel sides) of a trapezium has length $16\\text{ cm}$. If the height is $7\\text{ cm}$, what is its area?",
        "options": ["$56\\text{ cm}^2$", "$96\\text{ cm}^2$", "$112\\text{ cm}^2$", "$224\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Midline = $\\frac{a + b}{2} = 16\\text{ cm}$.<br>$\\text{Area} = \\text{Midline} \\times h = 16 \\times 7 = 112\\text{ cm}^2$."
      }
    ]
  },
  {
    "id": 20,
    "title": "Mastery Challenge • Part IV",
    "subtitle": "Questions 31–40: Real-Life Mensuration, Scaling Laws & Composite Figures",
    "questions": [
      {
        "id": 31,
        "question": "A room floor of $8\\text{ m} \\times 6\\text{ m}$ is to be paved with rectangular tiles of $40\\text{ cm} \\times 25\\text{ cm}$. How many tiles are needed?",
        "options": ["360 tiles", "400 tiles", "480 tiles", "540 tiles"],
        "correct": 2,
        "solution": "Floor area = $800\\text{ cm} \\times 600\\text{ cm} = 480,000\\text{ cm}^2$.<br>Tile area = $40 \\times 25 = 1,000\\text{ cm}^2$.<br>Tiles needed = $480,000 / 1,000 = 480$ tiles."
      },
      {
        "id": 32,
        "question": "If the side of a square is increased by $20\\%$, by what percentage does its area increase?",
        "options": ["$20\\%$", "$40\\%$", "$44\\%$", "$48\\%$"],
        "correct": 2,
        "solution": "New side = $1.2s$. New area = $(1.2s)^2 = 1.44s^2$.<br>Increase = $1.44 - 1 = 0.44 = 44\\%$."
      },
      {
        "id": 33,
        "question": "A circular swimming pool of radius $7\\text{ m}$ is surrounded by a walking deck of width $3.5\\text{ m}$. What is the area of the walking deck? (Use $\\pi = 22/7$)",
        "options": ["$192.5\\text{ m}^2$", "$210\\text{ m}^2$", "$231\\text{ m}^2$", "$245.5\\text{ m}^2$"],
        "correct": 0,
        "solution": "Inner radius $r = 7\\text{ m}$. Outer radius $R = 7 + 3.5 = 10.5\\text{ m} = 21/2\\text{ m}$.<br>Deck Area = $\\pi(R^2 - r^2) = \\frac{22}{7}\\left(\\frac{441}{4} - 49\\right) = \\frac{22}{7}\\left(\\frac{245}{4}\\right) = \\frac{22 \\times 35}{4} = \\frac{770}{4} = 192.5\\text{ m}^2$."
      },
      {
        "id": 34,
        "question": "The dimensions of a photograph are $15\\text{ cm} \\times 10\\text{ cm}$. It is mounted on a cardboard mat leaving a uniform border of $2.5\\text{ cm}$ around it. What is the area of the border mat?",
        "options": ["$100\\text{ cm}^2$", "$125\\text{ cm}^2$", "$150\\text{ cm}^2$", "$175\\text{ cm}^2$"],
        "correct": 2,
        "solution": "Photo area = $15 \\times 10 = 150\\text{ cm}^2$.<br>Cardboard dimensions = $(15 + 5) \\times (10 + 5) = 20 \\times 15 = 300\\text{ cm}^2$.<br>Border area = $300 - 150 = 150\\text{ cm}^2$."
      },
      {
        "id": 35,
        "question": "A triangular park has side lengths $120\\text{ m}, 80\\text{ m}$, and $50\\text{ m}$. What is the cost of planting grass at ₹$10\\text{ per m}^2$ if its area is $1450\\text{ m}^2$?",
        "options": ["₹7,250", "₹14,500", "₹29,000", "₹145,000"],
        "correct": 1,
        "solution": "$\\text{Cost} = \\text{Area} \\times \\text{Rate} = 1450\\text{ m}^2 \\times ₹10/\\text{m}^2 = ₹14,500$."
      },
      {
        "id": 36,
        "question": "If all linear dimensions of any polygon are scaled by factor $k = 4$, by what factor does its area increase?",
        "options": ["4 times", "8 times", "16 times", "64 times"],
        "correct": 2,
        "solution": "By the 2D area scaling law, area scales as $k^2 = 4^2 = 16$ times."
      },
      {
        "id": 37,
        "question": "A hall of $12\\text{ m} \\times 9\\text{ m}$ has a carpet laid in the center leaving an uncovered margin of $1.5\\text{ m}$ all around. What is the area of the carpet?",
        "options": ["$45\\text{ m}^2$", "$54\\text{ m}^2$", "$63\\text{ m}^2$", "$72\\text{ m}^2$"],
        "correct": 1,
        "solution": "Carpet length = $12 - 2(1.5) = 12 - 3 = 9\\text{ m}$.<br>Carpet width = $9 - 2(1.5) = 9 - 3 = 6\\text{ m}$.<br>Carpet area = $9 \\times 6 = 54\\text{ m}^2$."
      },
      {
        "id": 38,
        "question": "A quadrilateral garden has perpendicular diagonals of lengths $25\\text{ m}$ and $32\\text{ m}$. What is its area?",
        "options": ["$200\\text{ m}^2$", "$400\\text{ m}^2$", "$600\\text{ m}^2$", "$800\\text{ m}^2$"],
        "correct": 1,
        "solution": "For any quadrilateral whose diagonals are perpendicular (an orthodiagonal quadrilateral): $\\text{Area} = \\frac{1}{2} d_1 d_2 = \\frac{1}{2} \\times 25 \\times 32 = 25 \\times 16 = 400\\text{ m}^2$."
      },
      {
        "id": 39,
        "question": "The cross-section of a drainage canal is a trapezium with top width $14\\text{ m}$, bottom width $8\\text{ m}$, and depth $3\\text{ m}$. What is the cross-sectional area of water when the canal is full?",
        "options": ["$33\\text{ m}^2$", "$44\\text{ m}^2$", "$66\\text{ m}^2$", "$88\\text{ m}^2$"],
        "correct": 0,
        "solution": "Area = $\\frac{1}{2}(a + b)h = \\frac{1}{2}(14 + 8) \\times 3 = \\frac{1}{2}(22) \\times 3 = 11 \\times 3 = 33\\text{ m}^2$."
      },
      {
        "id": 40,
        "question": "A rectangular metal plate $30\\text{ cm} \\times 20\\text{ cm}$ has four circular holes of radius $3.5\\text{ cm}$ punched out of it. What is the remaining area of the plate? (Use $\\pi = 22/7$)",
        "options": ["$424\\text{ cm}^2$", "$446\\text{ cm}^2$", "$480\\text{ cm}^2$", "$512\\text{ cm}^2$"],
        "correct": 1,
        "solution": "Plate area = $30 \\times 20 = 600\\text{ cm}^2$.<br>Area of 1 hole = $\\pi r^2 = \\frac{22}{7} \\times 3.5 \\times 3.5 = 38.5\\text{ cm}^2$.<br>Area of 4 holes = $4 \\times 38.5 = 154\\text{ cm}^2$.<br>Remaining area = $600 - 154 = 446\\text{ cm}^2$."
      }
    ]
  }
]

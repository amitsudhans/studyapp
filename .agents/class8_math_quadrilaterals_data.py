# Class 8 Mathematics Chapter 4: Quadrilaterals - Master Curriculum Data
# NCERT Class 8 Mathematics Syllabus

slides_data = [
    # Slide 1: 4.1 Rectangles and Squares
    {
        "id": 1,
        "title": "4.1 Rectangles and Squares: Foundations of 4-Sided Polygons",
        "subtitle": "Equiangular Polygons, Perpendicular Geometry & The Regular Square",
        "content": """
<p class="lead">A <strong>quadrilateral</strong> is a closed two-dimensional polygon bounded by <strong>four straight line segments</strong>. It possesses 4 vertices, 4 interior angles, 4 edges, and exactly 2 diagonals connecting non-adjacent vertices.</p>

<div class="theory-box">
  <h4>Geometric Anatomy of a Quadrilateral</h4>
  <ul>
    <li><strong>Vertices & Sides:</strong> Let the vertices in cyclical order be $A, B, C, D$. The line segments $AB, BC, CD, DA$ form the four sides.</li>
    <li><strong>Opposite vs. Consecutive Sides:</strong> $AB$ and $CD$ are opposite sides (sharing no common vertex); $AB$ and $BC$ are consecutive (adjacent) sides.</li>
    <li><strong>Diagonals:</strong> The segments $AC$ and $BD$ joining opposite vertices are the <strong>diagonals</strong>.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Definition: The Rectangle</h4>
  <p>A <strong>rectangle</strong> is a quadrilateral where <em>all four interior angles are equal</em> (equiangular):</p>
  $$\\angle A = \\angle B = \\angle C = \\angle D = \\frac{360^\\circ}{4} = 90^\\circ$$
  <p>Because each angle is a right angle ($90^\\circ$), opposite sides are automatically parallel and equal in length: $AB = CD$ and $BC = DA$.</p>
</div>

<div class="theory-box">
  <h4>The Square: The Ultimate Regular Quadrilateral</h4>
  <p>A <strong>square</strong> is a special rectangle that is also <strong>equilateral</strong> (all four sides are equal):</p>
  $$AB = BC = CD = DA = s \\quad \\text{and} \\quad \\angle A = \\angle B = \\angle C = \\angle D = 90^\\circ$$
  <p>Every square is both a rectangle and a rhombus, representing the highest symmetry among all quadrilaterals.</p>
</div>
""",
        "sim_type": "rectangle_square_geometry_lab",
        "voice": "Welcome to Chapter 4: Quadrilaterals. We begin with rectangles and squares. A quadrilateral is any four-sided polygon. When all four angles are right angles of 90 degrees, we obtain a rectangle. If all four sides are also equal, the rectangle becomes a square, the most symmetrical four-sided polygon in geometry.",
        "checkpoints": [
            {
                "question": "If a quadrilateral has all four interior angles equal to each other, what must each angle measure?",
                "options": ["60°", "90°", "120°", "180°"],
                "correct": 1,
                "explanation": "The sum of interior angles in any quadrilateral is $360^\\circ$. If all four are equal, each angle is $\\frac{360^\\circ}{4} = 90^\\circ$, defining an equiangular quadrilateral (rectangle)."
            },
            {
                "question": "Which statement accurately describes the relationship between squares and rectangles?",
                "options": [
                    "All rectangles are squares, but not all squares are rectangles",
                    "All squares are rectangles, but not all rectangles are squares",
                    "No square can ever be considered a rectangle",
                    "Squares and rectangles have no shared geometric properties"
                ],
                "correct": 1,
                "explanation": "A rectangle is defined as a quadrilateral with four right angles. Since every square possesses four right angles, every square is a rectangle with the additional constraint that all sides are equal."
            }
        ]
    },

    # Slide 2: Properties of Rectangles & Squares: Diagonals and Symmetry
    {
        "id": 2,
        "title": "Properties of Rectangles & Squares: Diagonals & Symmetry",
        "subtitle": "Diagonal Congruence, Perpendicular Bisection & Symmetry Axes",
        "content": """
<p class="lead">The internal diagonals of rectangles and squares possess distinctive geometric properties derived directly from triangle congruence and the Pythagorean theorem.</p>

<div class="theory-box">
  <h4>Theorem: Rectangle Diagonals are Equal in Length</h4>
  <p>In rectangle $ABCD$, consider right-angled triangles $\\triangle ABC$ and $\\triangle BAD$:</p>
  <ul>
    <li>Side $AB$ is common to both triangles ($AB = BA$).</li>
    <li>Right angles are equal: $\\angle ABC = \\angle BAD = 90^\\circ$.</li>
    <li>Opposite sides are equal: $BC = AD$.</li>
  </ul>
  <p>By the <strong>SAS (Side-Angle-Side) Congruence Criterion</strong>, $\\triangle ABC \\cong \\triangle BAD$. Therefore, corresponding hypotenuses are equal:</p>
  $$AC = BD = \\sqrt{l^2 + w^2}$$
</div>

<div class="formula-box">
  <h4>Square Diagonals: Perpendicular Bisectors</h4>
  <p>In a square of side length $s$:</p>
  <ul>
    <li><strong>Equal Diagonals:</strong> $d_1 = d_2 = s\\sqrt{2} \\approx 1.414 s$.</li>
    <li><strong>Mutual Bisection:</strong> The diagonals bisect each other at center $O$: $OA = OB = OC = OD = \\frac{s}{\\sqrt{2}}$.</li>
    <li><strong>Perpendicular Intersection:</strong> Diagonals cross at right angles: $AC \\perp BD$ ($90^\\circ$).</li>
    <li><strong>Angle Bisection:</strong> Each diagonal bisects the $90^\\circ$ corner angles into two $45^\\circ$ angles.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>Lines of Symmetry</h4>
  <p>A non-square rectangle has <strong>2 lines of symmetry</strong> (the perpendicular bisectors of opposite sides). A square has <strong>4 lines of symmetry</strong> (2 through midpoints of sides, plus 2 along the diagonals).</p>
</div>
""",
        "sim_type": "diagonal_pythagorean_explorer",
        "voice": "Examining the diagonals of rectangles and squares reveals fascinating symmetry. In any rectangle, the two diagonals are equal in length, calculated by the square root of length squared plus width squared. In a square, the diagonals are not only equal, but they also intersect at perpendicular 90 degree angles and bisect the corner angles into 45 degrees.",
        "checkpoints": [
            {
                "question": "If a rectangle has length 8 cm and width 6 cm, what is the length of each diagonal?",
                "options": ["10 cm", "14 cm", "12 cm", "7 cm"],
                "correct": 0,
                "explanation": "Using the Pythagorean theorem: $d = \\sqrt{l^2 + w^2} = \\sqrt{8^2 + 6^2} = \\sqrt{64 + 36} = \\sqrt{100} = 10\\text{ cm}$."
            },
            {
                "question": "At what angle do the diagonals of a square intersect each other at the center?",
                "options": ["45°", "60°", "90°", "120°"],
                "correct": 2,
                "explanation": "The diagonals of a square are perpendicular bisectors of each other, intersecting at right angles ($90^\\circ$)."
            }
        ]
    },

    # Slide 3: 4.2 Angles in a Quadrilateral
    {
        "id": 3,
        "title": "4.2 Angles in a Quadrilateral: The 360° Interior Angle Theorem",
        "subtitle": "Triangulation Partition, Convex Polygons & Angle Sum Proof",
        "content": """
<p class="lead">Why does the sum of interior angles in <em>every single quadrilateral</em> always equal exactly $360^\\circ$? The answer lies in dividing the quadrilateral with a diagonal into two triangles.</p>

<div class="theory-box">
  <h4>The Triangulation Proof</h4>
  <p>Consider any quadrilateral $ABCD$. Draw the diagonal $AC$, which partitions the polygon into two non-overlapping triangles: $\\triangle ABC$ and $\\triangle ACD$.</p>
  <ol>
    <li>In $\\triangle ABC$: $\\angle CAB + \\angle B + \\angle BCA = 180^\\circ$.</li>
    <li>In $\\triangle ACD$: $\\angle DAC + \\angle D + \\angle ACD = 180^\\circ$.</li>
  </ol>
  <p>Adding these two equations together:</p>
  $$(\\angle CAB + \\angle DAC) + \\angle B + (\\angle BCA + \\angle ACD) + \\angle D = 180^\\circ + 180^\\circ$$
  $$\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ$$
</div>

<div class="formula-box">
  <h4>General Polygon Angle Sum Formula</h4>
  <p>For any $n$-sided polygon, the sum of interior angles is given by:</p>
  $$S = (n - 2) \\times 180^\\circ$$
  <p>For a quadrilateral where $n = 4$:</p>
  $$S = (4 - 2) \\times 180^\\circ = 2 \\times 180^\\circ = 360^\\circ$$
</div>

<div class="theory-box">
  <h4>Convex vs. Concave Quadrilaterals</h4>
  <p>In a <strong>convex</strong> quadrilateral, every interior angle is strictly less than $180^\\circ$, and both diagonals lie entirely inside the figure. In a <strong>concave</strong> quadrilateral, one interior angle is a reflex angle ($> 180^\\circ$), and one diagonal lies outside the polygon. Even so, the interior angle sum remains $360^\\circ$!</p>
</div>
""",
        "sim_type": "angle_sum_partition_lab",
        "voice": "The angle sum property is fundamental in quadrilateral geometry. By drawing a single diagonal between two opposite vertices, any quadrilateral is split into two non-overlapping triangles. Because the angles of each triangle add to 180 degrees, the total interior angle sum of any quadrilateral is always 180 plus 180, which equals 360 degrees.",
        "checkpoints": [
            {
                "question": "Three angles of a quadrilateral are 75°, 85°, and 110°. What is the measure of the fourth angle?",
                "options": ["80°", "90°", "95°", "100°"],
                "correct": 1,
                "explanation": "The sum of all four interior angles is $360^\\circ$. Therefore: $\\text{Fourth angle} = 360^\\circ - (75^\\circ + 85^\\circ + 110^\\circ) = 360^\\circ - 270^\\circ = 90^\\circ$."
            },
            {
                "question": "If the angles of a quadrilateral are in the ratio 1 : 2 : 3 : 4, what is the largest angle?",
                "options": ["36°", "72°", "108°", "144°"],
                "correct": 3,
                "explanation": "Let the angles be $x, 2x, 3x, 4x$. Their sum is $x + 2x + 3x + 4x = 10x = 360^\\circ$, giving $x = 36^\\circ$. The largest angle is $4x = 4 \\times 36^\\circ = 144^\\circ$."
            }
        ]
    },

    # Slide 4: Exterior Angles of a Quadrilateral
    {
        "id": 4,
        "title": "Exterior Angles of a Quadrilateral & The 360° Outer Turn",
        "subtitle": "Linear Pairs, The Total Turn Principle & Convex Polygon Walk",
        "content": """
<p class="lead">If you walk completely around the boundary of any convex polygon until you face your original direction, your body has completed one full rotation of $360^\\circ$. This geometric intuition governs <strong>exterior angles</strong>.</p>

<div class="theory-box">
  <h4>Definition of an Exterior Angle</h4>
  <p>An <strong>exterior angle</strong> is formed between any side of a polygon and the extension of its adjacent side. At each vertex $i$, the interior angle $I_i$ and the exterior angle $E_i$ form a <strong>linear pair</strong> on a straight line:</p>
  $$I_i + E_i = 180^\\circ \\implies E_i = 180^\\circ - I_i$$
</div>

<div class="formula-box">
  <h4>Sum of Exterior Angles Theorem</h4>
  <p>Summing the linear pairs across all 4 vertices of a quadrilateral:</p>
  $$\\sum_{i=1}^4 (I_i + E_i) = 4 \\times 180^\\circ = 720^\\circ$$
  $$(\\sum_{i=1}^4 I_i) + (\\sum_{i=1}^4 E_i) = 720^\\circ$$
  <p>Since the interior angle sum $\\sum I_i = 360^\\circ$:</p>
  $$360^\\circ + \\sum_{i=1}^4 E_i = 720^\\circ \\implies \\sum_{i=1}^4 E_i = 720^\\circ - 360^\\circ = 360^\\circ$$
</div>

<div class="theory-box">
  <h4>Key Takeaway</h4>
  <p>The sum of the exterior angles (taken one at each vertex) of <strong>any convex polygon</strong>—whether a triangle, quadrilateral, or decagon—is <strong>always $360^\\circ$</strong>!</p>
</div>
""",
        "sim_type": "exterior_angles_rotator",
        "voice": "Now let us examine exterior angles. At each corner, extending a side creates an exterior angle that forms a linear pair with the interior angle. When you trace the entire perimeter of any convex quadrilateral, the four exterior angles make one complete 360 degree turn. Therefore, the sum of exterior angles is always 360 degrees.",
        "checkpoints": [
            {
                "question": "If three exterior angles of a quadrilateral are 100°, 70°, and 80°, what is the fourth exterior angle?",
                "options": ["100°", "110°", "120°", "90°"],
                "correct": 1,
                "explanation": "The sum of all four exterior angles is $360^\\circ$. The fourth angle is $360^\\circ - (100^\\circ + 70^\\circ + 80^\\circ) = 360^\\circ - 250^\\circ = 110^\\circ$."
            },
            {
                "question": "If an interior angle of a convex quadrilateral is 115°, what is its corresponding exterior angle?",
                "options": ["65°", "75°", "85°", "95°"],
                "correct": 0,
                "explanation": "Interior and exterior angles at any vertex form a linear pair on a straight line: $\\text{Exterior} = 180^\\circ - 115^\\circ = 65^\\circ$."
            }
        ]
    },

    # Slide 5: 4.3 More Quadrilaterals with Parallel Opposite Sides (Parallelograms)
    {
        "id": 5,
        "title": "4.3 Parallelograms: Parallel Opposite Sides & Angle Laws",
        "subtitle": "Opposite Side Equality, Opposite Angle Parity & Consecutive Angle Supplements",
        "content": """
<p class="lead">A <strong>parallelogram</strong> is a quadrilateral in which <strong>both pairs of opposite sides are parallel</strong>. This parallel structure generates powerful angle and side relationships.</p>

<div class="theory-box">
  <h4>Fundamental Definition</h4>
  <p>In quadrilateral $ABCD$, if $AB \\parallel CD$ and $AD \\parallel BC$, then $ABCD$ is a <strong>parallelogram</strong> (abbreviated $\\parallel\\text{gm}$).</p>
</div>

<div class="formula-box">
  <h4>Three Core Theorems of Parallelograms</h4>
  <ol>
    <li><strong>Opposite Sides are Equal:</strong>
      $$AB = CD \\quad \\text{and} \\quad AD = BC$$
    </li>
    <li><strong>Opposite Angles are Equal:</strong>
      $$\\angle A = \\angle C \\quad \\text{and} \\quad \\angle B = \\angle D$$
    </li>
    <li><strong>Consecutive (Adjacent) Angles are Supplementary:</strong>
      Because opposite sides are parallel, consecutive angles form co-interior angles between parallel lines cut by a transversal:
      $$\\angle A + \\angle B = 180^\\circ, \\quad \\angle B + \\angle C = 180^\\circ, \\quad \\angle C + \\angle D = 180^\\circ, \\quad \\angle D + \\angle A = 180^\\circ$$
    </li>
  </ol>
</div>

<div class="theory-box">
  <h4>Proof Insight: Diagonal Congruence</h4>
  <p>Drawing diagonal $BD$ creates two alternate interior angle pairs because of the parallel lines. By the <strong>ASA (Angle-Side-Angle) criterion</strong>, $\\triangle ABD \\cong \\triangle CDB$, proving simultaneously that opposite sides and opposite angles must be equal!</p>
</div>
""",
        "sim_type": "parallelogram_parallel_sides_lab",
        "voice": "Section 4.3 introduces parallelograms. In a parallelogram, both pairs of opposite sides are parallel. This simple condition guarantees three major geometric truths: opposite sides are equal, opposite angles are equal, and any two consecutive angles are supplementary, adding up to 180 degrees.",
        "checkpoints": [
            {
                "question": "In a parallelogram ABCD, if angle A = 70°, what are the measures of angle B and angle C?",
                "options": [
                    "angle B = 70°, angle C = 110°",
                    "angle B = 110°, angle C = 70°",
                    "angle B = 110°, angle C = 110°",
                    "angle B = 70°, angle C = 70°"
                ],
                "correct": 1,
                "explanation": "Consecutive angles are supplementary: $\\angle B = 180^\\circ - \\angle A = 180^\\circ - 70^\\circ = 110^\\circ$. Opposite angles are equal: $\\angle C = \\angle A = 70^\\circ$."
            },
            {
                "question": "Two adjacent angles of a parallelogram are in the ratio 4 : 5. What is the measure of the smaller angle?",
                "options": ["80°", "100°", "75°", "90°"],
                "correct": 0,
                "explanation": "Adjacent angles are supplementary: $4x + 5x = 9x = 180^\\circ \\implies x = 20^\\circ$. The smaller angle is $4x = 4 \\times 20^\\circ = 80^\\circ$."
            }
        ]
    },

    # Slide 6: Diagonals of a Parallelogram
    {
        "id": 6,
        "title": "Diagonals of a Parallelogram & Mutual Bisection",
        "subtitle": "Intersection at Midpoints, Coordinate Balances & The Parallelogram Law",
        "content": """
<p class="lead">While the diagonals of a general parallelogram are typically unequal in length, they always share an exact point of mutual intersection: the <strong>geometric centroid</strong>.</p>

<div class="theory-box">
  <h4>Theorem: Diagonals Bisect Each Other</h4>
  <p>Let diagonals $AC$ and $BD$ of parallelogram $ABCD$ intersect at point $O$. Then:</p>
  $$OA = OC = \\frac{1}{2} AC \\quad \\text{and} \\quad OB = OD = \\frac{1}{2} BD$$
  <p><strong>Proof via ASA Congruence:</strong> Consider $\\triangle AOB$ and $\\triangle COD$:</p>
  <ul>
    <li>$AB = CD$ (opposite sides of a parallelogram).</li>
    <li>$\\angle OAB = \\angle OCD$ (alternate interior angles since $AB \\parallel CD$).</li>
    <li>$\\angle OBA = \\angle ODC$ (alternate interior angles since $AB \\parallel CD$).</li>
  </ul>
  <p>Therefore, $\\triangle AOB \\cong \\triangle COD$ by ASA, which proves $OA = OC$ and $OB = OD$.</p>
</div>

<div class="formula-box">
  <h4>The Parallelogram Law (Identity)</h4>
  <p>For any parallelogram with side lengths $a, b$ and diagonals $d_1, d_2$, the sum of the squares of the diagonals equals the sum of the squares of all four sides:</p>
  $$d_1^2 + d_2^2 = 2(a^2 + b^2)$$
</div>

<div class="theory-box">
  <h4>Midpoint Coordinate Invariance</h4>
  <p>If vertices are given in Cartesian coordinates, the midpoint of diagonal $AC$ is $\\left(\\frac{x_A+x_C}{2}, \\frac{y_A+y_C}{2}\\right)$, which matches the midpoint of $BD$. This allows rapid calculation of missing fourth vertex coordinates!</p>
</div>
""",
        "sim_type": "parallelogram_diagonal_bisector",
        "voice": "The diagonals of a parallelogram possess a key property: they bisect each other. This means their point of intersection divides each diagonal into two equal halves. We prove this using triangle congruence with alternate interior angles. Furthermore, the sum of squares of the two diagonals equals twice the sum of squares of the two adjacent sides.",
        "checkpoints": [
            {
                "question": "Diagonals AC and BD of a parallelogram intersect at O. If AC = 16 cm and BD = 12 cm, what is the length of OA and OB?",
                "options": [
                    "OA = 8 cm, OB = 6 cm",
                    "OA = 16 cm, OB = 12 cm",
                    "OA = 4 cm, OB = 3 cm",
                    "OA = 10 cm, OB = 5 cm"
                ],
                "correct": 0,
                "explanation": "Because diagonals bisect each other: $OA = \\frac{AC}{2} = \\frac{16}{2} = 8\\text{ cm}$, and $OB = \\frac{BD}{2} = \\frac{12}{2} = 6\\text{ cm}$."
            },
            {
                "question": "If side lengths of a parallelogram are 5 cm and 7 cm, what is the sum of the squares of its two diagonals?",
                "options": ["74 cm²", "148 cm²", "120 cm²", "200 cm²"],
                "correct": 1,
                "explanation": "By the Parallelogram Law: $d_1^2 + d_2^2 = 2(a^2 + b^2) = 2(5^2 + 7^2) = 2(25 + 49) = 2(74) = 148\\text{ cm}^2$."
            }
        ]
    },

    # Slide 7: Sufficient Conditions for Parallelograms
    {
        "id": 7,
        "title": "Sufficient Conditions: Proving a Quadrilateral is a Parallelogram",
        "subtitle": "Diagnostic Criteria, Minimal Necessary Conditions & Geometry Tests",
        "content": """
<p class="lead">How can we prove that a given quadrilateral is definitely a parallelogram without checking every single side and angle? Mathematics provides several <strong>minimal sufficient conditions</strong>.</p>

<div class="formula-box">
  <h4>Four Distinct Tests for a Parallelogram</h4>
  <p>A quadrilateral $ABCD$ is guaranteed to be a parallelogram if <em>any one</em> of the following conditions is satisfied:</p>
  <ol>
    <li><strong>Both pairs of opposite sides are equal:</strong> $AB = CD$ and $BC = DA$.</li>
    <li><strong>Both pairs of opposite angles are equal:</strong> $\\angle A = \\angle C$ and $\\angle B = \\angle D$.</li>
    <li><strong>One pair of opposite sides is BOTH equal AND parallel:</strong>
      $$AB = CD \\quad \\text{and} \\quad AB \\parallel CD$$
      <em>(This is often the fastest and most elegant proof in geometry!)</em>
    </li>
    <li><strong>The diagonals bisect each other:</strong> $OA = OC$ and $OB = OD$.</li>
  </ol>
</div>

<div class="theory-box">
  <h4>Caution: Common Geometric Traps</h4>
  <ul>
    <li><strong>Trap 1:</strong> Having only <em>one pair of opposite sides parallel</em> does NOT make it a parallelogram—that is a trapezium!</li>
    <li><strong>Trap 2:</strong> Having only <em>one pair of opposite sides equal</em> and another pair parallel does NOT guarantee a parallelogram (an isosceles trapezium has this property).</li>
    <li><strong>Golden Rule:</strong> The SAME pair of sides must be both equal and parallel.</li>
  </ul>
</div>
""",
        "sim_type": "parallelogram_condition_tester",
        "voice": "To prove that a four-sided shape is a parallelogram, we do not need to measure everything. Just one sufficient condition is enough. For instance, if one pair of opposite sides is both equal in length and parallel, or if the diagonals bisect each other, the shape is guaranteed to be a parallelogram.",
        "checkpoints": [
            {
                "question": "Which of the following conditions alone is sufficient to prove that quadrilateral ABCD is a parallelogram?",
                "options": [
                    "AB is parallel to CD, and AD = BC",
                    "AB = CD, and AB is parallel to CD",
                    "Angle A = Angle B, and Angle C = Angle D",
                    "Diagonals AC and BD are equal in length"
                ],
                "correct": 1,
                "explanation": "If one pair of opposite sides is BOTH equal and parallel ($AB = CD$ and $AB \\parallel CD$), the quadrilateral is guaranteed to be a parallelogram."
            },
            {
                "question": "If a quadrilateral has diagonals that bisect each other, which shape is it guaranteed to be at minimum?",
                "options": ["Trapezium", "Kite", "Parallelogram", "Square"],
                "correct": 2,
                "explanation": "Mutual bisection of diagonals is a necessary and sufficient condition for a quadrilateral to be a parallelogram."
            }
        ]
    },

    # Slide 8: 4.4 Quadrilaterals with Equal Sidelengths (The Rhombus)
    {
        "id": 8,
        "title": "4.4 Quadrilaterals with Equal Sidelengths: The Rhombus",
        "subtitle": "Equilateral Parallelograms & Perpendicular Diagonal Bisection",
        "content": """
<p class="lead">A <strong>rhombus</strong> (plural: rhombi or rhombuses) is a quadrilateral in which <strong>all four sides have equal length</strong>. It represents the equilateral member of the parallelogram family.</p>

<div class="theory-box">
  <h4>Definition & Inherited Properties</h4>
  <p>In quadrilateral $ABCD$, if $AB = BC = CD = DA = s$, then $ABCD$ is a <strong>rhombus</strong>.</p>
  <p>Since all 4 sides are equal, opposite sides are automatically equal ($AB = CD$ and $BC = AD$). Therefore:</p>
  <ul>
    <li><strong>Every rhombus is a parallelogram.</strong></li>
    <li>Opposite sides are parallel: $AB \\parallel CD$ and $AD \\parallel BC$.</li>
    <li>Opposite angles are equal: $\\angle A = \\angle C$ and $\\angle B = \\angle D$.</li>
    <li>Consecutive angles are supplementary: $\\angle A + \\angle B = 180^\\circ$.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Special Rhombus Theorem: Perpendicular Diagonals</h4>
  <p>The diagonals of a rhombus are <strong>perpendicular bisectors of each other</strong>:</p>
  $$AC \\perp BD \\quad (\\angle AOB = 90^\\circ)$$
  <p>Furthermore, each diagonal <strong>bisects the interior vertex angles</strong> through which it passes.</p>
</div>

<div class="theory-box">
  <h4>Proof of Perpendicularity</h4>
  <p>In $\\triangle AOB$ and $\\triangle COB$:</p>
  <ul>
    <li>$AB = CB$ (all sides of rhombus are equal).</li>
    <li>$OB$ is common.</li>
    <li>$OA = OC$ (diagonals of parallelogram bisect each other).</li>
  </ul>
  <p>By SSS congruence, $\\triangle AOB \\cong \\triangle COB$. Thus $\\angle AOB = \\angle COB$. Since they form a linear pair on straight line $AC$, each must be $\\frac{180^\\circ}{2} = 90^\\circ$!</p>
</div>
""",
        "sim_type": "rhombus_equilateral_stepper",
        "voice": "Section 4.4 focuses on rhombuses. A rhombus is a parallelogram with all four sides equal in length. Because of this equilateral symmetry, its diagonals cross each other at exactly 90 degrees, forming perpendicular bisectors, and they divide the vertex angles into equal halves.",
        "checkpoints": [
            {
                "question": "What is the angle of intersection between the two diagonals of any rhombus?",
                "options": ["45°", "60°", "90°", "180°"],
                "correct": 2,
                "explanation": "A distinguishing property of a rhombus is that its diagonals are perpendicular bisectors of each other, crossing at $90^\\circ$."
            },
            {
                "question": "In a rhombus ABCD, if angle A = 60°, what is the measure of angle B?",
                "options": ["30°", "60°", "90°", "120°"],
                "correct": 3,
                "explanation": "Since a rhombus is a parallelogram, consecutive angles are supplementary: $\\angle B = 180^\\circ - \\angle A = 180^\\circ - 60^\\circ = 120^\\circ$."
            }
        ]
    },

    # Slide 9: Rhombus Area & Diagonal Formulas
    {
        "id": 9,
        "title": "Rhombus Area & The Half-Product Diagonal Theorem",
        "subtitle": "Four Congruent Right Triangles, Area Derivation & Side-Diagonal Relations",
        "content": """
<p class="lead">Calculating the area of a rhombus is remarkably straightforward when its diagonal lengths are known, relying on the four congruent right triangles formed by its diagonals.</p>

<div class="formula-box">
  <h4>The Half-Product Diagonal Area Formula</h4>
  <p>If the diagonals of a rhombus have lengths $d_1$ and $d_2$:</p>
  $$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2$$
</div>

<div class="theory-box">
  <h4>Visual Geometric Proof</h4>
  <p>The two perpendicular diagonals divide the rhombus into <strong>4 congruent right-angled triangles</strong>, each with base $\\frac{d_1}{2}$ and height $\\frac{d_2}{2}$:</p>
  $$\\text{Area of one triangle} = \\frac{1}{2} \\times \\left(\\frac{d_1}{2}\\right) \\times \\left(\\frac{d_2}{2}\\right) = \\frac{d_1 d_2}{8}$$
  $$\\text{Total Area} = 4 \\times \\left(\\frac{d_1 d_2}{8}\\right) = \\frac{d_1 d_2}{2}$$
  <p>Notice also that the rhombus occupies exactly <strong>half the area</strong> of the surrounding bounding rectangle of dimensions $d_1 \\times d_2$.</p>
</div>

<div class="formula-box">
  <h4>Relationship Between Side Length and Diagonals</h4>
  <p>Applying the Pythagorean theorem to any one of the four central right-angled triangles:</p>
  $$s^2 = \\left(\\frac{d_1}{2}\\right)^2 + \\left(\\frac{d_2}{2}\\right)^2 = \\frac{d_1^2 + d_2^2}{4}$$
  $$s = \\frac{1}{2} \\sqrt{d_1^2 + d_2^2} \\quad \\iff \\quad 4s^2 = d_1^2 + d_2^2$$
  <p>This allows calculating the perimeter $P = 4s$ directly from the diagonal lengths!</p>
</div>
""",
        "sim_type": "rhombus_area_triangle_splitter",
        "voice": "The area of a rhombus is half the product of its two diagonals. Because the diagonals cut the rhombus into four identical right-angled triangles, rearranging them proves the area is exactly half of a rectangle with length d1 and width d2. Using the Pythagorean theorem on any of these triangles also gives the side length.",
        "checkpoints": [
            {
                "question": "What is the area of a rhombus whose diagonals measure 14 cm and 10 cm?",
                "options": ["70 cm²", "140 cm²", "35 cm²", "24 cm²"],
                "correct": 0,
                "explanation": "$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2 = \\frac{1}{2} \\times 14 \\times 10 = 70\\text{ cm}^2$."
            },
            {
                "question": "If the diagonals of a rhombus are 6 cm and 8 cm, what is the length of each side?",
                "options": ["5 cm", "7 cm", "10 cm", "14 cm"],
                "correct": 0,
                "explanation": "Half-diagonals are $\\frac{6}{2} = 3\\text{ cm}$ and $\\frac{8}{2} = 4\\text{ cm}$. Using Pythagoras: $s = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\\text{ cm}$."
            }
        ]
    },

    # Slide 10: 4.5 Playing with Quadrilaterals: Rigidity vs. Linkages
    {
        "id": 10,
        "title": "4.5 Playing with Quadrilaterals: Rigidity vs. Linkages",
        "subtitle": "Degrees of Freedom, Structural Deformation & Triangular Bracing in Engineering",
        "content": """
<p class="lead">Why are bicycle frames, electric transmission towers, and bridge trusses built with <strong>triangles</strong> instead of <strong>quadrilaterals</strong>? The answer lies in structural rigidity.</p>

<div class="theory-box">
  <h4>Triangle Rigidity (SSS Congruence)</h4>
  <p>Three rigid bars pinned together at their ends form a <strong>rigid structure</strong>. By the SSS Congruence Theorem, specifying the lengths of the three sides uniquely locks all three angles. It cannot deform without bending or breaking the bars.</p>
</div>

<div class="formula-box">
  <h4>Quadrilateral Flexibility (1 Degree of Freedom)</h4>
  <p>A four-bar linkage pinned at its four corners is <strong>not rigid</strong>. Even if the four side lengths are strictly fixed, the angles can continuously change:</p>
  $$\\text{Degrees of Freedom (DoF)} = 1$$
  <p>A rectangle can easily collapse into an oblique parallelogram under shear force. To eliminate this flexibility, engineers install a <strong>diagonal brace</strong>.</p>
</div>

<div class="theory-box">
  <h4>The Diagonal Bracing Principle</h4>
  <p>Adding a single diagonal rod across opposite vertices divides the flexible 4-gon into <strong>two rigid triangles</strong> ($\\triangle ABD$ and $\\triangle BCD$). This reduces the degrees of freedom from $1 \\to 0$, creating total structural stability.</p>
</div>
""",
        "sim_type": "quadrilateral_rigidity_linkage",
        "voice": "Section 4.5 explores the mechanical nature of quadrilaterals. While a three-sided triangle is inherently rigid and cannot deform, a four-sided quadrilateral has one degree of freedom and deforms under pressure. In engineering and architecture, adding a single diagonal strut splits the quadrilateral into two rigid triangles, locking the entire framework firmly in place.",
        "checkpoints": [
            {
                "question": "Why is a four-bar linkage with fixed side lengths flexible rather than rigid?",
                "options": [
                    "Because its angles can freely change without altering its side lengths",
                    "Because its sides are made of elastic material",
                    "Because its interior angle sum changes under pressure",
                    "Because the sum of its sides is less than 360°"
                ],
                "correct": 0,
                "explanation": "A quadrilateral has one degree of internal freedom: knowing the 4 side lengths alone does not fix its angles. It can shear into different parallelograms."
            },
            {
                "question": "What is the minimum number of diagonal braces required to make a four-sided quadrilateral frame rigid?",
                "options": ["1", "2", "3", "4"],
                "correct": 0,
                "explanation": "Adding just 1 diagonal brace splits the 4-gon into two triangles, each of which is locked by SSS congruence, making the entire structure rigid."
            }
        ]
    },

    # Slide 11: Varignon's Theorem & Quadrilateral Tessellations
    {
        "id": 11,
        "title": "Varignon's Theorem & Quadrilateral Tessellations",
        "subtitle": "Midpoint Parallelograms, Half-Area Invariance & Plane-Tiling Magic",
        "content": """
<p class="lead">In 1731, French mathematician Pierre Varignon discovered an astonishing geometric law connecting every quadrilateral—no matter how irregular—to a perfect parallelogram.</p>

<div class="formula-box">
  <h4>Varignon's Theorem</h4>
  <p>Given <em>any</em> arbitrary quadrilateral $ABCD$ (convex, concave, or self-intersecting):</p>
  <p>If $P, Q, R, S$ are the midpoints of sides $AB, BC, CD, DA$ respectively, then the figure $PQRS$ is <strong>always a parallelogram</strong>!</p>
  $$\\text{Area}(PQRS) = \\frac{1}{2} \\times \\text{Area}(ABCD)$$
</div>

<div class="theory-box">
  <h4>Proof via the Midpoint Theorem</h4>
  <p>Draw diagonal $AC$. In $\\triangle ABC$, segment $PQ$ connects midpoints of $AB$ and $BC$. By the <strong>Triangle Midpoint Theorem</strong>:</p>
  $$PQ \\parallel AC \\quad \\text{and} \\quad PQ = \\frac{1}{2} AC$$
  <p>Similarly, in $\\triangle ADC$, segment $SR$ connects midpoints of $AD$ and $CD$:</p>
  $$SR \\parallel AC \\quad \\text{and} \\quad SR = \\frac{1}{2} AC$$
  <p>Since $PQ$ and $SR$ are both parallel to $AC$ and equal to $\\frac{1}{2} AC$, they are equal and parallel to each other. This guarantees $PQRS$ is a parallelogram!</p>
</div>

<div class="theory-box">
  <h4>Tessellation: Any Quadrilateral Tiles the Plane</h4>
  <p>Remarkably, <strong>any quadrilateral</strong>—even totally asymmetric and irregular—can tile the 2D infinite plane with zero gaps and zero overlaps by performing $180^\\circ$ rotations around side midpoints. At each corner vertex of the tessellation, the four interior angles gather together: $\\angle 1 + \\angle 2 + \\angle 3 + \\angle 4 = 360^\\circ$.</p>
</div>
""",
        "sim_type": "varignon_parallelogram_tessellation",
        "voice": "Pierre Varignon discovered that connecting the midpoints of the four sides of any quadrilateral always produces a parallelogram whose area is exactly half the original quadrilateral. Furthermore, because the four angles of any quadrilateral sum to 360 degrees, any quadrilateral can tile the two-dimensional plane without leaving any gaps.",
        "checkpoints": [
            {
                "question": "If an irregular quadrilateral has an area of 56 cm², what is the area of the Varignon parallelogram formed by joining its side midpoints?",
                "options": ["28 cm²", "14 cm²", "56 cm²", "112 cm²"],
                "correct": 0,
                "explanation": "By Varignon's Theorem, the area of the midpoint parallelogram is exactly half the area of the original quadrilateral: $\\frac{56}{2} = 28\\text{ cm}^2$."
            },
            {
                "question": "Why can any arbitrary convex quadrilateral tile the plane seamlessly?",
                "options": [
                    "Because all four of its interior angles sum to 360°",
                    "Because its opposite sides are always parallel",
                    "Because its diagonals are equal in length",
                    "Because its sides are integer multiples of each other"
                ],
                "correct": 0,
                "explanation": "When tiles are rotated $180^\\circ$ around side midpoints, one of each of the four angles ($\\angle A, \\angle B, \\angle C, \\angle D$) meets at every shared vertex, summing to $360^\\circ$ and completely filling the space around that point."
            }
        ]
    },

    # Slide 12: 4.6 Kite: Two Pairs of Equal Adjacent Sides
    {
        "id": 12,
        "title": "4.6 Kite: Two Pairs of Equal Adjacent Sides",
        "subtitle": "Bilateral Symmetry, Perpendicular Diagonals & One Bisected Axis",
        "content": """
<p class="lead">A <strong>kite</strong> is a quadrilateral that possesses <strong>two distinct pairs of adjacent equal sides</strong>. Unlike a parallelogram, opposite sides are generally not equal.</p>

<div class="theory-box">
  <h4>Formal Definition</h4>
  <p>In quadrilateral $ABCD$, if:</p>
  $$AB = AD \\quad \\text{and} \\quad CB = CD \\quad (\\text{with } AB \\neq BC)$$
  <p>then $ABCD$ is a <strong>kite</strong>. Sides that meet at vertex $A$ are equal, and sides meeting at vertex $C$ are equal.</p>
</div>

<div class="formula-box">
  <h4>Four Distinguishing Properties of a Kite</h4>
  <ol>
    <li><strong>Perpendicular Diagonals:</strong> The diagonals intersect at right angles: $AC \\perp BD$.</li>
    <li><strong>One Diagonal is Bisected:</strong> The main symmetry diagonal $AC$ bisects the cross diagonal $BD$:
      $$BM = MD$$
    </li>
    <li><strong>Exactly One Pair of Equal Opposite Angles:</strong>
      $$\\angle B = \\angle D \\quad (\\text{but } \\angle A \\neq \\angle C)$$
    </li>
    <li><strong>Line of Symmetry:</strong> The main diagonal $AC$ is the single line of reflectional symmetry, bisecting both $\\angle A$ and $\\angle C$.</li>
  </ol>
</div>

<div class="formula-box">
  <h4>Area of a Kite</h4>
  <p>Since the diagonals are perpendicular and one bisects the other, the area formula matches that of a rhombus:</p>
  $$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2$$
</div>
""",
        "sim_type": "kite_symmetry_explorer",
        "voice": "Section 4.6 introduces kites. A kite has two pairs of equal adjacent sides. The main axis diagonal acts as a line of mirror symmetry. It perpendicularly bisects the cross diagonal and bisects the top and bottom angles. Exactly one pair of opposite angles, the wings, are equal to each other.",
        "checkpoints": [
            {
                "question": "In a kite ABCD where AB = AD and CB = CD, if angle B = 105° and angle A = 70°, what is the measure of angle C?",
                "options": ["80°", "105°", "70°", "90°"],
                "correct": 0,
                "explanation": "In a kite, the non-vertex opposite angles are equal, so $\\angle D = \\angle B = 105^\\circ$. The angle sum is $360^\\circ$: $\\angle C = 360^\\circ - (70^\\circ + 105^\\circ + 105^\\circ) = 360^\\circ - 280^\\circ = 80^\\circ$."
            },
            {
                "question": "If the diagonals of a kite measure 12 cm and 9 cm, what is the area of the kite?",
                "options": ["54 cm²", "108 cm²", "27 cm²", "42 cm²"],
                "correct": 0,
                "explanation": "$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2 = \\frac{1}{2} \\times 12 \\times 9 = 54\\text{ cm}^2$."
            }
        ]
    },

    # Slide 13: 4.6 Trapezium: Exactly One Pair of Parallel Sides
    {
        "id": 13,
        "title": "4.6 Trapezium: One Pair of Parallel Bases",
        "subtitle": "Bases, Legs, Altitudes & Consecutive Interior Angle Supplements",
        "content": """
<p class="lead">A <strong>trapezium</strong> (known as a <em>trapezoid</em> in North American terminology) is a quadrilateral with <strong>at least one pair of parallel sides</strong>.</p>

<div class="theory-box">
  <h4>Anatomy of a Trapezium</h4>
  <ul>
    <li><strong>Bases:</strong> The two parallel sides $AB$ and $CD$ are called the <strong>bases</strong> ($a$ and $b$).</li>
    <li><strong>Legs:</strong> The non-parallel sides $AD$ and $BC$ are called the <strong>legs</strong>.</li>
    <li><strong>Altitude (Height $h$):</strong> The perpendicular distance between the parallel bases.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Consecutive Interior Angles on Each Leg</h4>
  <p>Because the bases are parallel ($AB \\parallel CD$), the angles on the same non-parallel leg form consecutive interior (co-interior) angles and are <strong>supplementary</strong>:</p>
  $$\\angle A + \\angle D = 180^\\circ \\quad \\text{and} \\quad \\angle B + \\angle C = 180^\\circ$$
  <p><em>(Note: $\\angle A + \\angle B$ is generally not equal to $180^\\circ$ unless the shape is a parallelogram!)</em></p>
</div>

<div class="theory-box">
  <h4>Right-Angled Trapezium</h4>
  <p>If one leg is perpendicular to the bases, the figure has two right angles and is called a <strong>right trapezium</strong>. The perpendicular leg directly serves as the altitude $h$.</p>
</div>
""",
        "sim_type": "trapezium_parallel_base_slider",
        "voice": "Next, we study trapeziums. A trapezium has at least one pair of parallel sides called bases, while the other two sides are called legs. Because the bases are parallel, the two interior angles along each leg always add up to 180 degrees. The perpendicular distance between the bases is the height or altitude.",
        "checkpoints": [
            {
                "question": "In a trapezium ABCD where AB is parallel to CD, if angle A = 55° and angle B = 75°, what is angle D?",
                "options": ["125°", "105°", "135°", "115°"],
                "correct": 0,
                "explanation": "Angles along the transversal leg $AD$ are supplementary: $\\angle A + \\angle D = 180^\\circ \\implies \\angle D = 180^\\circ - 55^\\circ = 125^\\circ$."
            },
            {
                "question": "Which statement is true for EVERY trapezium?",
                "options": [
                    "Opposite angles are always equal",
                    "At least one pair of opposite sides is parallel",
                    "Diagonals are always equal in length",
                    "All four sides are equal"
                ],
                "correct": 1,
                "explanation": "By definition, a trapezium must have at least one pair of parallel opposite sides."
            }
        ]
    },

    # Slide 14: Isosceles Trapezium & Derivation of Trapezium Area
    {
        "id": 14,
        "title": "Isosceles Trapezium & Derivation of Trapezium Area",
        "subtitle": "Equal Legs, Base Angle Symmetry & The Rotational Duplication Proof",
        "content": """
<p class="lead">An <strong>isosceles trapezium</strong> occurs when the two non-parallel legs are equal in length. It possesses exceptional symmetry and leads naturally to the famous area formula.</p>

<div class="theory-box">
  <h4>Properties of an Isosceles Trapezium</h4>
  <p>In trapezium $ABCD$ where $AB \\parallel CD$ and non-parallel legs $AD = BC$:</p>
  <ul>
    <li><strong>Equal Base Angles:</strong> $\\angle A = \\angle B$ and $\\angle C = \\angle D$.</li>
    <li><strong>Equal Diagonals:</strong> $AC = BD$.</li>
    <li><strong>One Axis of Symmetry:</strong> The perpendicular bisector of the two parallel bases forms a line of reflectional symmetry.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Formula for the Area of Any Trapezium</h4>
  <p>For any trapezium with parallel base lengths $a$ and $b$, and perpendicular height $h$:</p>
  $$\\text{Area} = \\frac{1}{2} (a + b) \\times h$$
  <p><em>(Area equals the average of the bases multiplied by the height.)</em></p>
</div>

<div class="theory-box">
  <h4>Elegant Proof via Duplication & Rotation</h4>
  <p>Take an exact replica of the trapezium, rotate it by $180^\\circ$, and join it along its slanted leg to the original. The combined shape is a <strong>parallelogram</strong> with base $(a + b)$ and height $h$:</p>
  $$\\text{Area of Parallelogram} = (a + b) \\times h$$
  $$\\text{Area of One Trapezium} = \\frac{1}{2} (a + b) \\times h$$
</div>
""",
        "sim_type": "isosceles_trapezium_area_lab",
        "voice": "When the non-parallel legs of a trapezium are equal, it is called an isosceles trapezium, featuring equal base angles and equal diagonals. To find the area of any trapezium, we add the two parallel bases, divide by two to get their average, and multiply by the height. This formula is proven by rotating a second identical trapezium to create a large parallelogram.",
        "checkpoints": [
            {
                "question": "A trapezium has parallel bases of 12 cm and 8 cm, and a perpendicular height of 5 cm. What is its area?",
                "options": ["50 cm²", "100 cm²", "40 cm²", "60 cm²"],
                "correct": 0,
                "explanation": "$\\text{Area} = \\frac{1}{2} (a + b) h = \\frac{1}{2} (12 + 8) \\times 5 = \\frac{1}{2} (20) \\times 5 = 10 \\times 5 = 50\\text{ cm}^2$."
            },
            {
                "question": "Which of the following is a special property of an isosceles trapezium that is NOT true for general trapeziums?",
                "options": [
                    "Bases are parallel",
                    "Diagonals are equal in length",
                    "Interior angles sum to 360°",
                    "Adjacent angles along a leg are supplementary"
                ],
                "correct": 1,
                "explanation": "In an isosceles trapezium, the diagonals are equal in length ($AC = BD$) and base angles are equal, which is not true for general scalene trapeziums."
            }
        ]
    },

    # Slide 15: Quadrilateral Family Hierarchy & Summary
    {
        "id": 15,
        "title": "Comprehensive Quadrilateral Family Hierarchy",
        "subtitle": "The Euler-Venn Classification Tree & Taxonomic Inheritance Laws",
        "content": """
<p class="lead">All quadrilaterals belong to a rich, interconnected family tree. Understanding which shapes inherit properties from other shapes resolves common geometric confusions.</p>

<div class="theory-box">
  <h4>The Hierarchy of Inclusions</h4>
  <ul>
    <li><strong>Quadrilateral:</strong> Any 4-sided closed polygon.</li>
    <li><strong>Trapezium:</strong> Quadrilateral with at least 1 pair of parallel sides.</li>
    <li><strong>Parallelogram:</strong> Quadrilateral with 2 pairs of parallel sides (a subset of trapeziums).</li>
    <li><strong>Rectangle:</strong> Parallelogram with 4 right angles.</li>
    <li><strong>Rhombus:</strong> Parallelogram with 4 equal sides.</li>
    <li><strong>Square:</strong> Quadrilateral that is SIMULTANEOUSLY a rectangle AND a rhombus!</li>
    <li><strong>Kite:</strong> Quadrilateral with 2 pairs of equal adjacent sides.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Master Property Comparison Table</h4>
  <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:12.5px;">
    <thead>
      <tr style="border-bottom:1px solid #475569; color:#38bdf8;">
        <th style="text-align:left; padding:4px;">Property</th>
        <th>Parallelogram</th>
        <th>Rectangle</th>
        <th>Rhombus</th>
        <th>Square</th>
      </tr>
    </thead>
    <tbody style="color:#cbd5e1;">
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">Opposite sides parallel</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">Opposite sides equal</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">All 4 sides equal</td><td align="center">✗</td><td align="center">✗</td><td align="center">✓</td><td align="center">✓</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">All 4 angles 90°</td><td align="center">✗</td><td align="center">✓</td><td align="center">✗</td><td align="center">✓</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">Diagonals bisect</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td style="padding:4px;">Diagonals equal</td><td align="center">✗</td><td align="center">✓</td><td align="center">✗</td><td align="center">✓</td></tr>
      <tr><td style="padding:4px;">Diagonals perpendicular</td><td align="center">✗</td><td align="center">✗</td><td align="center">✓</td><td align="center">✓</td></tr>
    </tbody>
  </table>
</div>
""",
        "sim_type": "quadrilateral_family_tree_matrix",
        "voice": "The quadrilateral family tree connects all four-sided shapes hierarchically. Parallelograms branch into rectangles with four right angles and rhombuses with four equal sides. At the intersection of both branches sits the square, which inherits every single property of both rectangles and rhombuses.",
        "checkpoints": [
            {
                "question": "Which statement is false?",
                "options": [
                    "Every square is a rhombus",
                    "Every square is a rectangle",
                    "Every rectangle is a square",
                    "Every rhombus is a parallelogram"
                ],
                "correct": 2,
                "explanation": "Every rectangle has four right angles, but its adjacent sides need not be equal. Therefore, not every rectangle is a square."
            },
            {
                "question": "Which quadrilateral possesses BOTH equal diagonals AND perpendicular diagonals?",
                "options": ["Rectangle", "Rhombus", "Square", "Parallelogram"],
                "correct": 2,
                "explanation": "A rectangle has equal diagonals, a rhombus has perpendicular diagonals, and the square uniquely possesses BOTH properties simultaneously."
            }
        ]
    },

    # Slide 16: IT'S PUZZLE TIME! Which Quad?
    {
        "id": 16,
        "title": "IT'S PUZZLE TIME! Which Quad?",
        "subtitle": "Geometric Detective Clues, Property Elimination & Classification Mastery",
        "content": """
<p class="lead">Put on your mathematical detective hat! In this puzzle challenge, analyze subtle clues about angles, sides, and diagonals to determine the exact identity of the mystery quadrilateral.</p>

<div class="theory-box">
  <h4>Diagnostic Decision Protocol</h4>
  <ul>
    <li><strong>Clue 1 (Parallelism):</strong> Are 0, 1, or 2 pairs of opposite sides parallel?
      <br>• 0 pairs $\\to$ Kite or general quadrilateral.
      <br>• Exactly 1 pair $\\to$ Trapezium.
      <br>• 2 pairs $\\to$ Member of the Parallelogram family.
    </li>
    <li><strong>Clue 2 (Diagonals):</strong>
      <br>• Diagonals equal only $\\to$ Rectangle or Isosceles Trapezium.
      <br>• Diagonals perpendicular only $\\to$ Rhombus or Kite.
      <br>• Diagonals BOTH equal AND perpendicular $\\to$ <strong>Square</strong>!
    </li>
    <li><strong>Clue 3 (Angles):</strong>
      <br>• All 4 angles $90^\\circ \\to$ Rectangle or Square.
      <br>• Exactly one pair of opposite angles equal $\\to$ Kite.
    </li>
  </ul>
</div>

<div class="formula-box">
  <h4>Sample Detective Mystery</h4>
  <p><em>"My diagonals bisect each other at right angles, but my diagonals are NOT equal in length. All four of my sides are 7 cm. Who am I?"</em></p>
  <p><strong>Deduction:</strong> All sides equal $\\implies$ Rhombus or Square. Diagonals not equal $\\implies$ It cannot be a square. Therefore, the shape is a <strong>Rhombus</strong>!</p>
</div>
""",
        "sim_type": "which_quad_puzzle_game",
        "voice": "It is puzzle time! In Which Quad, you test your geometric intuition by analyzing diagnostic clues. By examining how many sides are parallel, whether diagonals are equal or perpendicular, and checking angle symmetries, you can deduce the exact name of any quadrilateral.",
        "checkpoints": [
            {
                "question": "Clue: 'My diagonals bisect each other and are equal in length, but my adjacent sides are unequal.' Who am I?",
                "options": ["Rhombus", "Rectangle", "Kite", "Trapezium"],
                "correct": 1,
                "explanation": "Diagonals bisecting each other $\\implies$ Parallelogram. Diagonals equal in length $\\implies$ Rectangle. Adjacent sides unequal $\\implies$ Not a square."
            },
            {
                "question": "Clue: 'I have perpendicular diagonals and two pairs of equal adjacent sides, but my opposite sides are not parallel.' Who am I?",
                "options": ["Kite", "Rhombus", "Parallelogram", "Square"],
                "correct": 0,
                "explanation": "A kite has two pairs of equal adjacent sides and perpendicular diagonals, but no parallel opposite sides."
            }
        ]
    },

    # Slides 17 to 20: Mastery Quiz Challenges
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Rectangles, Squares & Angle Sum Properties",
        "subtitle": "Questions 1 to 10 • Comprehensive Diagnostic & Step-by-Step Proofs",
        "content": "<p class='lead'>Test your foundational mastery of quadrilateral angle sums, rectangular and square properties, and exterior turn geometry. Answer each question and click <strong>💡 View Solution</strong> to inspect step-by-step proofs.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [1, 10],
        "voice": "Welcome to Mastery Quiz Challenge 1. Solve the first ten questions covering interior and exterior angles, rectangles, and squares. Remember to click View Solution on any question to examine the detailed mathematical derivation.",
        "checkpoints": []
    },
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Parallelograms & Diagonal Properties",
        "subtitle": "Questions 11 to 20 • Parallel Rails, Angle Supplements & Mutual Bisections",
        "content": "<p class='lead'>Challenge your knowledge of parallelograms, opposite side equality, consecutive angle supplements, and diagonal bisection laws. Answer each question and click <strong>💡 View Solution</strong> for full proofs.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [11, 20],
        "voice": "Now tackle Mastery Quiz Challenge 2. These ten questions focus on parallelograms, supplementary angles, and diagonal bisection theorems. Use View Solution to review your work step by step.",
        "checkpoints": []
    },
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Rhombuses, Rigidity & Varignon's Theorem",
        "subtitle": "Questions 21 to 30 • Equilateral Symmetry, Linkage Mechanics & Tessellations",
        "content": "<p class='lead'>Test your understanding of rhombus area formulas, perpendicular diagonals, structural linkage rigidity, and Varignon's midpoint theorem. Click <strong>💡 View Solution</strong> for step-by-step reasoning.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [21, 30],
        "voice": "Mastery Quiz Challenge 3 covers rhombuses, diagonal area formulas, structural rigidity, and Varignon's theorem. Inspect the solutions to deepen your understanding of geometric proofs.",
        "checkpoints": []
    },
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Kites, Trapeziums & The Grand Family Hierarchy",
        "subtitle": "Questions 31 to 40 • Symmetry Axes, Area Derivations & Puzzle Deductions",
        "content": "<p class='lead'>Complete the final challenge on kites, trapeziums, isosceles symmetry, and the comprehensive quadrilateral taxonomy. Click <strong>💡 View Solution</strong> on any question for full details.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [31, 40],
        "voice": "Congratulations on reaching Mastery Quiz Challenge 4, the final slide of this chapter. Complete the final ten questions on kites, trapeziums, and the quadrilateral family tree. You have reached the last slide of this chapter.",
        "checkpoints": []
    }
]

# 40 Comprehensive Quiz Questions with In-Depth Step-by-Step Solutions
quiz_questions = [
    # Q1
    {
        "num": 1,
        "question": "The sum of all four interior angles of any convex quadrilateral is equal to:",
        "options": ["180°", "270°", "360°", "540°"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the quadrilateral be $ABCD$. Draw a diagonal from vertex $A$ to vertex $C$.
2. This diagonal partitions the quadrilateral into two non-overlapping triangles: $\\triangle ABC$ and $\\triangle ADC$.
3. By the Angle Sum Property of a triangle:
   - In $\\triangle ABC$: $\\angle CAB + \\angle B + \\angle BCA = 180^\\circ$
   - In $\\triangle ADC$: $\\angle DAC + \\angle D + \\angle ACD = 180^\\circ$
4. Adding the angles of both triangles:
   $$\\text{Total Sum} = (\\angle CAB + \\angle DAC) + \\angle B + (\\angle BCA + \\angle ACD) + \\angle D = 180^\\circ + 180^\\circ = 360^\\circ$$
5. Thus, $\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ$.
<strong>Correct Answer:</strong> (C) 360°
"""
    },

    # Q2
    {
        "num": 2,
        "question": "Three angles of a quadrilateral measure 65°, 115°, and 85°. What is the measure of the fourth angle?",
        "options": ["85°", "95°", "105°", "115°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the four interior angles be $\\angle A = 65^\\circ$, $\\angle B = 115^\\circ$, $\\angle C = 85^\\circ$, and $\\angle D = x$.
2. By the Quadrilateral Interior Angle Sum Theorem:
   $$\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ$$
3. Substitute the known angle measures:
   $$65^\\circ + 115^\\circ + 85^\\circ + x = 360^\\circ$$
4. Compute the sum of the three given angles:
   $$65^\\circ + 115^\\circ = 180^\\circ$$
   $$180^\\circ + 85^\\circ = 265^\\circ$$
5. Solve for $x$:
   $$x = 360^\\circ - 265^\\circ = 95^\\circ$$
<strong>Correct Answer:</strong> (B) 95°
"""
    },

    # Q3
    {
        "num": 3,
        "question": "The angles of a quadrilateral are in the ratio 2 : 3 : 5 : 8. What is the measure of the smallest angle?",
        "options": ["20°", "40°", "60°", "80°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the common ratio factor be $x$.
2. The four angles can be written as $2x$, $3x$, $5x$, and $8x$.
3. The sum of all four angles in a quadrilateral is $360^\\circ$:
   $$2x + 3x + 5x + 8x = 360^\\circ$$
4. Combine like terms:
   $$18x = 360^\\circ \\implies x = \\frac{360^\\circ}{18} = 20^\\circ$$
5. The smallest angle is:
   $$\\text{Smallest angle} = 2x = 2 \\times 20^\\circ = 40^\\circ$$
6. (Verification: Other angles are $60^\\circ, 100^\\circ, 160^\\circ$; $40 + 60 + 100 + 160 = 360^\\circ$.)
<strong>Correct Answer:</strong> (B) 40°
"""
    },

    # Q4
    {
        "num": 4,
        "question": "If a rectangle has length 12 cm and diagonal 13 cm, what is its width?",
        "options": ["5 cm", "7 cm", "8 cm", "10 cm"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In rectangle $ABCD$, each corner is a right angle ($90^\\circ$).
2. The diagonal $d$, length $l$, and width $w$ form a right-angled triangle where the diagonal is the hypotenuse.
3. Apply the Pythagorean theorem:
   $$d^2 = l^2 + w^2$$
4. Substitute the given values $d = 13$ and $l = 12$:
   $$13^2 = 12^2 + w^2$$
   $$169 = 144 + w^2$$
5. Solve for $w^2$:
   $$w^2 = 169 - 144 = 25 \\implies w = \\sqrt{25} = 5\\text{ cm}$$
<strong>Correct Answer:</strong> (A) 5 cm
"""
    },

    # Q5
    {
        "num": 5,
        "question": "What is the sum of the exterior angles (taken one at each vertex) of ANY convex quadrilateral?",
        "options": ["180°", "360°", "540°", "720°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. At each of the 4 vertices, the interior angle $I_i$ and the exterior angle $E_i$ lie on a straight line, forming a linear pair:
   $$I_i + E_i = 180^\\circ$$
2. Summing this relationship over all 4 vertices:
   $$\\sum_{i=1}^4 (I_i + E_i) = 4 \\times 180^\\circ = 720^\\circ$$
3. Separate the interior and exterior sums:
   $$\\left(\\sum_{i=1}^4 I_i\\right) + \\left(\\sum_{i=1}^4 E_i\\right) = 720^\\circ$$
4. We know the interior angle sum is $\\sum I_i = 360^\\circ$:
   $$360^\\circ + \\sum E_i = 720^\\circ \\implies \\sum E_i = 720^\\circ - 360^\\circ = 360^\\circ$$
<strong>Correct Answer:</strong> (B) 360°
"""
    },

    # Q6
    {
        "num": 6,
        "question": "If three exterior angles of a quadrilateral are 80°, 110°, and 75°, what is the measure of the fourth exterior angle?",
        "options": ["85°", "95°", "105°", "115°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. By the Exterior Angle Sum Theorem, the sum of all 4 exterior angles of a convex polygon is always $360^\\circ$.
2. Let the fourth exterior angle be $E_4$.
3. Set up the equation:
   $$80^\\circ + 110^\\circ + 75^\\circ + E_4 = 360^\\circ$$
4. Calculate the sum of the three given angles:
   $$80^\\circ + 110^\\circ + 75^\\circ = 265^\\circ$$
5. Subtract from $360^\\circ$:
   $$E_4 = 360^\\circ - 265^\\circ = 95^\\circ$$
<strong>Correct Answer:</strong> (B) 95°
"""
    },

    # Q7
    {
        "num": 7,
        "question": "In a square of side length 10 cm, what is the exact length of each diagonal?",
        "options": ["10 cm", "14 cm", "10√2 cm", "20 cm"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a square, all four sides have equal length $s = 10\\text{ cm}$ and all four angles are $90^\\circ$.
2. A diagonal divides the square into two congruent isosceles right-angled triangles with legs $s = 10$ and hypotenuse $d$.
3. Applying the Pythagorean theorem:
   $$d = \\sqrt{s^2 + s^2} = \\sqrt{2s^2} = s\\sqrt{2}$$
4. Substituting $s = 10$:
   $$d = 10\\sqrt{2}\\text{ cm} \\approx 14.14\\text{ cm}$$
<strong>Correct Answer:</strong> (C) 10√2 cm
"""
    },

    # Q8
    {
        "num": 8,
        "question": "How many lines of reflectional symmetry does a square possess?",
        "options": ["1", "2", "4", "Infinite"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. A line of symmetry is a line along which a shape can be folded so that both halves match identically.
2. For a square:
   - Line 1: Perpendicular bisector of the top and bottom horizontal sides.
   - Line 2: Perpendicular bisector of the left and right vertical sides.
   - Line 3: Diagonal joining the top-left vertex to bottom-right vertex.
   - Line 4: Diagonal joining the top-right vertex to bottom-left vertex.
3. Therefore, a square has exactly 4 lines of reflectional symmetry. (In comparison, a non-square rectangle has only 2).
<strong>Correct Answer:</strong> (C) 4
"""
    },

    # Q9
    {
        "num": 9,
        "question": "A quadrilateral has two angles of 110° and 80°. If the other two angles are equal to each other, what is the measure of each of these equal angles?",
        "options": ["80°", "85°", "90°", "95°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the two unknown equal angles be $x$ each.
2. The four interior angles of the quadrilateral are $110^\\circ$, $80^\\circ$, $x$, and $x$.
3. The sum of interior angles in a quadrilateral is $360^\\circ$:
   $$110^\\circ + 80^\\circ + x + x = 360^\\circ$$
4. Simplify:
   $$190^\\circ + 2x = 360^\\circ$$
5. Solve for $x$:
   $$2x = 360^\\circ - 190^\\circ = 170^\\circ$$
   $$x = \\frac{170^\\circ}{2} = 85^\\circ$$
<strong>Correct Answer:</strong> (B) 85°
"""
    },

    # Q10
    {
        "num": 10,
        "question": "Which of the following figures is ALWAYS an equiangular quadrilateral?",
        "options": ["Rhombus", "Parallelogram", "Rectangle", "Trapezium"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. An <strong>equiangular</strong> polygon is one in which all interior angles are equal in measure.
2. In a quadrilateral, the total sum of angles is $360^\\circ$. If all four are equal, each must be:
   $$\\frac{360^\\circ}{4} = 90^\\circ$$
3. By definition, a quadrilateral with four right angles is a <strong>rectangle</strong>.
4. (Rhombuses and parallelograms can have unequal adjacent angles like $60^\\circ$ and $120^\\circ$).
<strong>Correct Answer:</strong> (C) Rectangle
"""
    },

    # Q11
    {
        "num": 11,
        "question": "In parallelogram ABCD, if angle A = 115°, what is the measure of angle D?",
        "options": ["65°", "115°", "75°", "90°"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In parallelogram $ABCD$, side $AB$ is parallel to side $CD$ ($AB \\parallel CD$), and side $AD$ acts as a transversal line intersecting them.
2. Angles $\\angle A$ and $\\angle D$ are consecutive interior (co-interior) angles on the same side of the transversal $AD$.
3. By the properties of parallel lines, consecutive interior angles are supplementary:
   $$\\angle A + \\angle D = 180^\\circ$$
4. Substitute the value $\\angle A = 115^\\circ$:
   $$115^\\circ + \\angle D = 180^\\circ \\implies \\angle D = 180^\\circ - 115^\\circ = 65^\\circ$$
<strong>Correct Answer:</strong> (A) 65°
"""
    },

    # Q12
    {
        "num": 12,
        "question": "The perimeter of a parallelogram is 48 cm. If one side is 6 cm longer than the adjacent side, what are the lengths of the two sides?",
        "options": ["10 cm and 14 cm", "9 cm and 15 cm", "8 cm and 16 cm", "12 cm and 18 cm"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a parallelogram, opposite sides are equal in length. Let the two adjacent sides be $x$ and $x + 6$.
2. The perimeter of a parallelogram is the sum of all four sides:
   $$P = 2(a + b) = 2(x + (x + 6)) = 48\\text{ cm}$$
3. Simplify the equation:
   $$2(2x + 6) = 48$$
   $$4x + 12 = 48$$
4. Solve for $x$:
   $$4x = 48 - 12 = 36 \\implies x = 9\\text{ cm}$$
5. The longer side is:
   $$x + 6 = 9 + 6 = 15\\text{ cm}$$
6. Verification: $2(9 + 15) = 2(24) = 48\\text{ cm}$.
<strong>Correct Answer:</strong> (B) 9 cm and 15 cm
"""
    },

    # Q13
    {
        "num": 13,
        "question": "Diagonals AC and BD of parallelogram ABCD intersect at O. If AC = 18 cm and BD = 14 cm, what is the length of segment OD?",
        "options": ["7 cm", "9 cm", "14 cm", "18 cm"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Theorem: The diagonals of a parallelogram bisect each other.
2. This means the intersection point $O$ is the exact midpoint of both diagonal $AC$ and diagonal $BD$.
3. Therefore:
   $$OB = OD = \\frac{1}{2} BD$$
4. Given $BD = 14\\text{ cm}$:
   $$OD = \\frac{14}{2} = 7\\text{ cm}$$
5. (Similarly, $OA = OC = \\frac{18}{2} = 9\\text{ cm}$).
<strong>Correct Answer:</strong> (A) 7 cm
"""
    },

    # Q14
    {
        "num": 14,
        "question": "If the ratio of two adjacent angles of a parallelogram is 2 : 3, what is the measure of the larger angle?",
        "options": ["72°", "108°", "120°", "144°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the two adjacent angles be $2x$ and $3x$.
2. Adjacent (consecutive) angles of any parallelogram are supplementary:
   $$2x + 3x = 180^\\circ$$
3. Combine terms:
   $$5x = 180^\\circ \\implies x = \\frac{180^\\circ}{5} = 36^\\circ$$
4. The larger angle is:
   $$\\text{Larger angle} = 3x = 3 \\times 36^\\circ = 108^\\circ$$
5. (The smaller angle is $2x = 72^\\circ$; $72^\\circ + 108^\\circ = 180^\\circ$).
<strong>Correct Answer:</strong> (B) 108°
"""
    },

    # Q15
    {
        "num": 15,
        "question": "In a parallelogram ABCD, side AB = (3x - 4) cm and CD = (x + 10) cm. What is the actual length of side AB?",
        "options": ["7 cm", "17 cm", "21 cm", "24 cm"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a parallelogram, opposite sides are equal in length:
   $$AB = CD$$
2. Substitute the algebraic expressions:
   $$3x - 4 = x + 10$$
3. Rearrange the equation to isolate $x$:
   $$3x - x = 10 + 4$$
   $$2x = 14 \\implies x = 7$$
4. Substitute $x = 7$ back into the expression for $AB$:
   $$AB = 3(7) - 4 = 21 - 4 = 17\\text{ cm}$$
5. Verification: $CD = 7 + 10 = 17\\text{ cm}$. Both sides are equal.
<strong>Correct Answer:</strong> (B) 17 cm
"""
    },

    # Q16
    {
        "num": 16,
        "question": "Which of the following conditions is NOT sufficient to prove that quadrilateral ABCD is a parallelogram?",
        "options": [
            "AB is parallel to CD, and AB = CD",
            "AB = CD and AD = BC",
            "Angle A = Angle C and Angle B = Angle D",
            "AB is parallel to CD, and AD = BC"
        ],
        "correct": 3,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let us analyze condition (D): \"$AB \\parallel CD$ and $AD = BC$\".
2. Here, one pair of opposite sides ($AB, CD$) is parallel, while the <em>other</em> pair of sides ($AD, BC$) is equal.
3. This is precisely the defining characteristic of an <strong>isosceles trapezium</strong>! In an isosceles trapezium, the non-parallel legs are equal, but the shape is definitely NOT a parallelogram.
4. For one pair of sides to guarantee a parallelogram, the <strong>SAME</strong> pair must be both parallel AND equal ($AB \\parallel CD$ and $AB = CD$, which is option A).
<strong>Correct Answer:</strong> (D) AB is parallel to CD, and AD = BC
"""
    },

    # Q17
    {
        "num": 17,
        "question": "In parallelogram ABCD, angle A = (2x + 15)° and opposite angle C = (3x - 20)°. What is the measure of angle B?",
        "options": ["85°", "95°", "105°", "115°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a parallelogram, opposite angles are equal:
   $$\\angle A = \\angle C$$
2. Substitute the expressions:
   $$2x + 15 = 3x - 20$$
3. Solve for $x$:
   $$15 + 20 = 3x - 2x \\implies x = 35$$
4. Find the measure of $\\angle A$:
   $$\\angle A = 2(35) + 15 = 70 + 15 = 85^\\circ$$
5. Consecutive angles are supplementary:
   $$\\angle A + \\angle B = 180^\\circ \\implies \\angle B = 180^\\circ - 85^\\circ = 95^\\circ$$
<strong>Correct Answer:</strong> (B) 95°
"""
    },

    # Q18
    {
        "num": 18,
        "question": "The diagonals of a parallelogram are 10 cm and 12 cm. At what distance from the vertices do they intersect?",
        "options": [
            "5 cm along one and 6 cm along the other",
            "10 cm and 12 cm",
            "2.5 cm and 3 cm",
            "Cannot be determined without side lengths"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. A fundamental property of every parallelogram is that its diagonals bisect each other.
2. If the first diagonal has total length $d_1 = 10\\text{ cm}$, the intersection point $O$ is at a distance of:
   $$\\frac{d_1}{2} = \\frac{10}{2} = 5\\text{ cm}$$ from its ends.
3. If the second diagonal has total length $d_2 = 12\\text{ cm}$, the intersection point $O$ is at a distance of:
   $$\\frac{d_2}{2} = \\frac{12}{2} = 6\\text{ cm}$$ from its ends.
4. Hence, the point of intersection is 5 cm along the first diagonal and 6 cm along the second.
<strong>Correct Answer:</strong> (A) 5 cm along one and 6 cm along the other
"""
    },

    # Q19
    {
        "num": 19,
        "question": "If all four angles of a parallelogram are equal, what specific shape must it be?",
        "options": ["Trapezium", "Rhombus", "Rectangle", "Kite"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The sum of all four interior angles of any quadrilateral is $360^\\circ$.
2. If all four angles are equal, let each angle be $\\theta$:
   $$4\\theta = 360^\\circ \\implies \\theta = \\frac{360^\\circ}{4} = 90^\\circ$$
3. A parallelogram having all four angles equal to $90^\\circ$ is, by definition, a <strong>rectangle</strong>.
<strong>Correct Answer:</strong> (C) Rectangle
"""
    },

    # Q20
    {
        "num": 20,
        "question": "Using the Parallelogram Law, if adjacent sides are 3 cm and 4 cm, what is the sum of the squares of the two diagonals (d₁² + d₂²)?",
        "options": ["25 cm²", "50 cm²", "100 cm²", "144 cm²"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The Parallelogram Law states that the sum of the squares of the diagonals equals the sum of the squares of all four sides:
   $$d_1^2 + d_2^2 = 2(a^2 + b^2)$$
2. Here, side lengths are $a = 3\\text{ cm}$ and $b = 4\\text{ cm}$.
3. Calculate the sum of squares of the sides:
   $$a^2 + b^2 = 3^2 + 4^2 = 9 + 16 = 25$$
4. Multiply by 2:
   $$d_1^2 + d_2^2 = 2(25) = 50\\text{ cm}^2$$
<strong>Correct Answer:</strong> (B) 50 cm²
"""
    },

    # Q21
    {
        "num": 21,
        "question": "The diagonals of a rhombus are 16 cm and 12 cm. What is the area of the rhombus?",
        "options": ["96 cm²", "192 cm²", "48 cm²", "112 cm²"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The area of a rhombus is given by half the product of its two diagonals:
   $$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2$$
2. Substitute the given diagonal lengths $d_1 = 16\\text{ cm}$ and $d_2 = 12\\text{ cm}$:
   $$\\text{Area} = \\frac{1}{2} \\times 16 \\times 12$$
3. Simplify:
   $$\\text{Area} = 8 \\times 12 = 96\\text{ cm}^2$$
<strong>Correct Answer:</strong> (A) 96 cm²
"""
    },

    # Q22
    {
        "num": 22,
        "question": "If the diagonals of a rhombus are 24 cm and 10 cm, what is the length of each side of the rhombus?",
        "options": ["12 cm", "13 cm", "17 cm", "26 cm"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The diagonals of a rhombus bisect each other at right angles ($90^\\circ$).
2. This creates four congruent right-angled triangles at the center.
3. The legs of each right triangle are half the diagonal lengths:
   $$\\text{Leg}_1 = \\frac{24}{2} = 12\\text{ cm}, \\quad \\text{Leg}_2 = \\frac{10}{2} = 5\\text{ cm}$$
4. The hypotenuse of each triangle is the side length $s$ of the rhombus.
5. Apply the Pythagorean theorem:
   $$s = \\sqrt{12^2 + 5^2} = \\sqrt{144 + 25} = \\sqrt{169} = 13\\text{ cm}$$
<strong>Correct Answer:</strong> (B) 13 cm
"""
    },

    # Q23
    {
        "num": 23,
        "question": "The perimeter of a rhombus is 40 cm. If one of its diagonals is 12 cm, what is the length of the other diagonal?",
        "options": ["12 cm", "14 cm", "16 cm", "18 cm"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. All four sides of a rhombus are equal:
   $$\\text{Side } s = \\frac{\\text{Perimeter}}{4} = \\frac{40}{4} = 10\\text{ cm}$$
2. Given one diagonal $d_1 = 12\\text{ cm}$, its half-length is:
   $$\\frac{d_1}{2} = \\frac{12}{2} = 6\\text{ cm}$$
3. In any central right triangle formed by the perpendicular diagonals:
   $$s^2 = \\left(\\frac{d_1}{2}\\right)^2 + \\left(\\frac{d_2}{2}\\right)^2$$
4. Substitute $s = 10$ and $\\frac{d_1}{2} = 6$:
   $$10^2 = 6^2 + \\left(\\frac{d_2}{2}\\right)^2$$
   $$100 = 36 + \\left(\\frac{d_2}{2}\\right)^2$$
   $$\\left(\\frac{d_2}{2}\\right)^2 = 100 - 36 = 64 \\implies \\frac{d_2}{2} = \\sqrt{64} = 8\\text{ cm}$$
5. Total length of the other diagonal is:
   $$d_2 = 2 \\times 8 = 16\\text{ cm}$$
<strong>Correct Answer:</strong> (C) 16 cm
"""
    },

    # Q24
    {
        "num": 24,
        "question": "In a rhombus ABCD, angle CAB = 35°. What is the measure of angle ABC?",
        "options": ["35°", "70°", "110°", "145°"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a rhombus, the diagonal $AC$ bisects the vertex angle $\\angle A$.
2. Given $\\angle CAB = 35^\\circ$, the entire interior angle $\\angle A$ is:
   $$\\angle A = 2 \\times 35^\\circ = 70^\\circ$$
3. Since a rhombus is a parallelogram, consecutive angles $\\angle A$ and $\\angle ABC$ are supplementary:
   $$\\angle A + \\angle ABC = 180^\\circ$$
4. Solve for $\\angle ABC$:
   $$\\angle ABC = 180^\\circ - 70^\\circ = 110^\\circ$$
<strong>Correct Answer:</strong> (C) 110°
"""
    },

    # Q25
    {
        "num": 25,
        "question": "Why does a triangular frame hold its shape under load while a quadrilateral frame deforms easily?",
        "options": [
            "Because three side lengths uniquely determine a triangle (SSS congruence), giving it 0 internal degrees of freedom",
            "Because triangles always have three 60° angles",
            "Because triangles are heavier than quadrilaterals",
            "Because quadrilaterals have obtuse angles"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. By the SSS (Side-Side-Side) Congruence Theorem, fixing the lengths of the three sides of a triangle locks all three of its angles into a single unique configuration. It has 0 internal degrees of freedom.
2. In contrast, four side lengths do NOT uniquely lock a quadrilateral; it has 1 internal degree of freedom and can deform into infinitely many different parallelograms without changing side lengths.
3. This is why engineering structures (roof trusses, bridges, cranes) are triangulated.
<strong>Correct Answer:</strong> (A) Because three side lengths uniquely determine a triangle (SSS congruence), giving it 0 internal degrees of freedom
"""
    },

    # Q26
    {
        "num": 26,
        "question": "According to Varignon's Theorem, joining the midpoints of the consecutive sides of ANY quadrilateral always forms a:",
        "options": ["Square", "Rectangle", "Parallelogram", "Trapezium"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let $ABCD$ be any arbitrary quadrilateral, and let $P, Q, R, S$ be the midpoints of sides $AB, BC, CD, DA$.
2. Draw diagonal $AC$.
3. In $\\triangle ABC$, $P$ and $Q$ are midpoints. By the Midpoint Theorem:
   $$PQ \\parallel AC \\quad \\text{and} \\quad PQ = \\frac{1}{2} AC$$
4. In $\\triangle ADC$, $S$ and $R$ are midpoints. By the Midpoint Theorem:
   $$SR \\parallel AC \\quad \\text{and} \\quad SR = \\frac{1}{2} AC$$
5. Thus, $PQ$ and $SR$ are both parallel to $AC$ and equal in length ($PQ = SR$).
6. A quadrilateral with one pair of opposite sides equal and parallel is guaranteed to be a <strong>parallelogram</strong>.
<strong>Correct Answer:</strong> (C) Parallelogram
"""
    },

    # Q27
    {
        "num": 27,
        "question": "If the area of quadrilateral ABCD is 84 cm², what is the area of the Varignon parallelogram formed by joining its side midpoints?",
        "options": ["21 cm²", "42 cm²", "84 cm²", "168 cm²"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Varignon's Theorem states that the area of the midpoint parallelogram $PQRS$ is exactly half of the total area of the original quadrilateral $ABCD$:
   $$\\text{Area}(PQRS) = \\frac{1}{2} \\times \\text{Area}(ABCD)$$
2. Given $\\text{Area}(ABCD) = 84\\text{ cm}^2$:
   $$\\text{Area}(PQRS) = \\frac{1}{2} \\times 84 = 42\\text{ cm}^2$$
<strong>Correct Answer:</strong> (B) 42 cm²
"""
    },

    # Q28
    {
        "num": 28,
        "question": "What shape is formed by joining the midpoints of the sides of a RECTANGLE?",
        "options": ["A Rectangle", "A Rhombus", "A Trapezium", "A Scalene Parallelogram"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let $ABCD$ be a rectangle. Its diagonals are equal in length: $AC = BD$.
2. By the Midpoint Theorem, each side of the Varignon parallelogram has length equal to half of a diagonal:
   $$PQ = RS = \\frac{1}{2} AC \\quad \\text{and} \\quad QR = SP = \\frac{1}{2} BD$$
3. Since $AC = BD$, all four sides of $PQRS$ are equal:
   $$PQ = QR = RS = SP$$
4. A parallelogram with all four sides equal is a <strong>rhombus</strong>!
<strong>Correct Answer:</strong> (B) A Rhombus
"""
    },

    # Q29
    {
        "num": 29,
        "question": "What shape is formed by joining the midpoints of the sides of a RHOMBUS?",
        "options": ["A Rhombus", "A Rectangle", "A Square", "A Kite"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a rhombus $ABCD$, the diagonals intersect at right angles: $AC \\perp BD$.
2. The sides of the midpoint quadrilateral $PQRS$ are parallel to the diagonals ($PQ \\parallel AC$ and $QR \\parallel BD$).
3. Since $AC \\perp BD$, the angle between adjacent sides $PQ$ and $QR$ must also be $90^\\circ$.
4. A parallelogram with right angles is a <strong>rectangle</strong>!
5. (Note the beautiful dual relationship: midpoints of a rectangle form a rhombus, and midpoints of a rhombus form a rectangle!)
<strong>Correct Answer:</strong> (B) A Rectangle
"""
    },

    # Q30
    {
        "num": 30,
        "question": "Any quadrilateral can tile (tessellate) the plane without gaps because:",
        "options": [
            "All four sides can be arranged in parallel lines",
            "The sum of the four interior angles at each shared vertex is exactly 360°",
            "Quadrilaterals always possess lines of symmetry",
            "Diagonals bisect the perimeter"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. To tile a two-dimensional plane without leaving gaps or overlaps, the sum of the angles meeting at any common vertex must equal a full rotation of $360^\\circ$.
2. By rotating arbitrary quadrilateral tiles by $180^\\circ$ around their side midpoints, one copy of each of the four interior angles ($\\angle A, \\angle B, \\angle C, \\angle D$) meets at each shared vertex.
3. Since $\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ$, they perfectly fill the entire space around that point, allowing any arbitrary quadrilateral to tile the plane!
<strong>Correct Answer:</strong> (B) The sum of the four interior angles at each shared vertex is exactly 360°
"""
    },

    # Q31
    {
        "num": 31,
        "question": "Which of the following is a TRUE property of every kite?",
        "options": [
            "Opposite sides are parallel",
            "Both pairs of opposite angles are equal",
            "The diagonals are perpendicular to each other",
            "Diagonals are equal in length"
        ],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. By definition, a kite has two distinct pairs of equal adjacent sides.
2. The main axis diagonal acts as a line of reflectional symmetry.
3. As a direct consequence of this bilateral symmetry, the diagonals of a kite are always <strong>perpendicular to each other</strong> ($AC \\perp BD$).
4. (Opposite sides are not parallel, diagonals are usually unequal, and only one pair of opposite angles is equal).
<strong>Correct Answer:</strong> (C) The diagonals are perpendicular to each other
"""
    },

    # Q32
    {
        "num": 32,
        "question": "In kite ABCD with AB = AD and CB = CD, if angle A = 80° and angle C = 40°, what is the measure of angle B?",
        "options": ["100°", "120°", "130°", "140°"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In a kite, the two opposite angles between the unequal sides are equal:
   $$\\angle B = \\angle D$$
2. The sum of all four interior angles in any quadrilateral is $360^\\circ$:
   $$\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ$$
3. Substitute the known values:
   $$80^\\circ + \\angle B + 40^\\circ + \\angle B = 360^\\circ$$
4. Simplify:
   $$120^\\circ + 2\\angle B = 360^\\circ$$
5. Solve for $\\angle B$:
   $$2\\angle B = 360^\\circ - 120^\\circ = 240^\\circ \\implies \\angle B = \\frac{240^\\circ}{2} = 120^\\circ$$
<strong>Correct Answer:</strong> (B) 120°
"""
    },

    # Q33
    {
        "num": 33,
        "question": "The diagonals of a kite are 15 cm and 8 cm. What is the area of the kite?",
        "options": ["60 cm²", "120 cm²", "30 cm²", "46 cm²"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Because the diagonals of a kite intersect at right angles ($90^\\circ$) and the main diagonal bisects the cross diagonal into two equal segments, the area formula is:
   $$\\text{Area} = \\frac{1}{2} \\times d_1 \\times d_2$$
2. Substitute $d_1 = 15\\text{ cm}$ and $d_2 = 8\\text{ cm}$:
   $$\\text{Area} = \\frac{1}{2} \\times 15 \\times 8 = 15 \\times 4 = 60\\text{ cm}^2$$
<strong>Correct Answer:</strong> (A) 60 cm²
"""
    },

    # Q34
    {
        "num": 34,
        "question": "In trapezium ABCD with AB parallel to CD, if angle A = 65° and angle B = 80°, find the measure of angle C.",
        "options": ["100°", "115°", "120°", "135°"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In trapezium $ABCD$, base $AB$ is parallel to base $CD$ ($AB \\parallel CD$).
2. Leg $BC$ acts as a transversal intersecting these parallel lines.
3. Interior angles on the same side of the transversal line ($BC$) are supplementary:
   $$\\angle B + \\angle C = 180^\\circ$$
4. Substitute $\\angle B = 80^\\circ$:
   $$80^\\circ + \\angle C = 180^\\circ \\implies \\angle C = 180^\\circ - 80^\\circ = 100^\\circ$$
5. (Similarly, $\\angle D = 180^\\circ - \\angle A = 180^\\circ - 65^\\circ = 115^\\circ$).
<strong>Correct Answer:</strong> (A) 100°
"""
    },

    # Q35
    {
        "num": 35,
        "question": "A trapezium has parallel bases of lengths 14 cm and 10 cm, and its area is 96 cm². What is the perpendicular distance (height) between the bases?",
        "options": ["6 cm", "8 cm", "10 cm", "12 cm"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The formula for the area of a trapezium is:
   $$\\text{Area} = \\frac{1}{2} (a + b) \\times h$$
2. Substitute the given values $\\text{Area} = 96$, $a = 14$, and $b = 10$:
   $$96 = \\frac{1}{2} (14 + 10) \\times h$$
3. Simplify the base sum:
   $$96 = \\frac{1}{2} (24) \\times h$$
   $$96 = 12 \\times h$$
4. Solve for $h$:
   $$h = \\frac{96}{12} = 8\\text{ cm}$$
<strong>Correct Answer:</strong> (B) 8 cm
"""
    },

    # Q36
    {
        "num": 36,
        "question": "Which of the following is true for an ISOSCELES trapezium?",
        "options": [
            "All four sides are equal",
            "The non-parallel sides are equal, and diagonals are equal",
            "Opposite angles are supplementary, but base angles are unequal",
            "Diagonals bisect each other at 90°"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. An isosceles trapezium is defined as a trapezium whose non-parallel sides (legs) are equal in length ($AD = BC$).
2. Due to its bilateral reflectional symmetry across the perpendicular bisector of the bases:
   - Base angles are equal: $\\angle A = \\angle B$ and $\\angle C = \\angle D$.
   - Diagonals are equal in length: $AC = BD$.
<strong>Correct Answer:</strong> (B) The non-parallel sides are equal, and diagonals are equal
"""
    },

    # Q37
    {
        "num": 37,
        "question": "Which of the following statements is mathematically TRUE?",
        "options": [
            "Every rectangle is a square",
            "Every rhombus is a square",
            "Every square is a rhombus",
            "Every trapezium is a parallelogram"
        ],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. A rhombus is defined as any parallelogram with four equal sides.
2. Every square is a parallelogram with four equal sides (and additionally has four $90^\\circ$ angles).
3. Therefore, every square satisfies all requirements of a rhombus: <strong>Every square is a rhombus</strong>.
4. Conversely, a rhombus is only a square if its angles are $90^\\circ$, so not all rhombuses are squares.
<strong>Correct Answer:</strong> (C) Every square is a rhombus
"""
    },

    # Q38
    {
        "num": 38,
        "question": "Riddle: 'I am a quadrilateral. My diagonals are equal in length and bisect each other at right angles. Who am I?'",
        "options": ["Rectangle", "Rhombus", "Square", "Kite"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Clue 1: \"Diagonals bisect each other\" $\\implies$ Must be a member of the <strong>Parallelogram family</strong>.
2. Clue 2: \"Diagonals are equal in length\" $\\implies$ Must be a <strong>Rectangle</strong>.
3. Clue 3: \"Diagonals bisect at right angles (perpendicular)\" $\\implies$ Must be a <strong>Rhombus</strong>.
4. The unique shape that is simultaneously both a rectangle and a rhombus is the <strong>Square</strong>!
<strong>Correct Answer:</strong> (C) Square
"""
    },

    # Q39
    {
        "num": 39,
        "question": "Riddle: 'My diagonals bisect each other at right angles, but they are NOT equal in length. My opposite sides are parallel. Who am I?'",
        "options": ["Square", "Rhombus", "Rectangle", "Trapezium"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Clue 1: \"Diagonals bisect each other and opposite sides are parallel\" $\\implies$ Parallelogram.
2. Clue 2: \"Diagonals intersect at right angles\" $\\implies$ Rhombus or Square.
3. Clue 3: \"Diagonals are NOT equal in length\" $\\implies$ It cannot be a square (which requires equal diagonals).
4. Therefore, the shape is a <strong>Rhombus</strong>.
<strong>Correct Answer:</strong> (B) Rhombus
"""
    },

    # Q40
    {
        "num": 40,
        "question": "In an isosceles trapezium, if one angle is 70°, what are the measures of the other three angles?",
        "options": [
            "70°, 110°, 110°",
            "70°, 70°, 150°",
            "110°, 110°, 140°",
            "90°, 90°, 110°"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the isosceles trapezium have bases $AB \\parallel CD$.
2. In an isosceles trapezium, angles adjacent to the same base are equal:
   - If $\\angle A = 70^\\circ$, then $\\angle B = 70^\\circ$.
3. Consecutive interior angles along each leg are supplementary ($AB \\parallel CD$):
   $$\\angle A + \\angle D = 180^\\circ \\implies \\angle D = 180^\\circ - 70^\\circ = 110^\\circ$$
   $$\\angle B + \\angle C = 180^\\circ \\implies \\angle C = 180^\\circ - 70^\\circ = 110^\\circ$$
4. Therefore, the four angles are $70^\\circ, 70^\\circ, 110^\\circ, 110^\\circ$. The other three angles measure $70^\\circ, 110^\\circ, 110^\\circ$.
<strong>Correct Answer:</strong> (A) 70°, 110°, 110°
"""
    }
]


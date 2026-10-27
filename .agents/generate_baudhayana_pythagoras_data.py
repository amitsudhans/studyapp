import json
import sys
import os

slides = [
    {
        "id": 1,
        "title": "The Baudhāyana-Pythagoras Theorem",
        "subtitle": "The Universal Law of Right-Angled Triangles & Squares",
        "sim_type": "baudhayana_pythagoras_theater",
        "voice": "Welcome to our laboratory on the Baudhāyana-Pythagoras Theorem. In any right-angled triangle, the area of the square constructed on the hypotenuse equals the sum of the areas of the squares on the other two sides.",
        "content": """
<h4>The Fundamental Geometric Law</h4>
<p>In any right-angled triangle, the side opposite the right angle ($90^\\circ$) is called the <strong>hypotenuse</strong>. It is always the strictly longest side of the triangle.</p>
<p>If the lengths of the two legs enclosing the right angle are $a$ and $b$, and the length of the hypotenuse is $c$, then:</p>
<div style="background:#0f172a; border-left:4px solid #6366f1; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{a^2 + b^2 = c^2}$$
</div>
<h4>Baudhāyana's Ancient Formulation (c. 800 BCE)</h4>
<p>Centuries before Pythagoras of Samos, the Indian mathematician <strong>Baudhāyana</strong> recorded this fundamental principle in the <em>Baudhāyana Śulbasūtra</em> (1.48):</p>
<blockquote style="font-style:italic; color:#93c5fd; border-left:3px solid #38bdf8; padding-left:10px; margin:10px 0;">
  "dīrghacaturasrasyākṣṇayā rajjuḥ pārśvamānī tiryaṅmānī ca yat pṛthagbhūte kurutas tadubhayaṁ karoti."<br>
  — <em>The diagonal cord of a rectangle produces by itself an area equal to the sum of the areas produced separately by its length and breadth.</em>
</blockquote>
<p>Geometrically, this means that if you construct a geometric square on each of the three sides of a right triangle, the area of the square on side $c$ equals the combined areas of the squares on sides $a$ and $b$.</p>
""",
        "checkpoints": [
            {
                "q": "In a right-angled triangle with legs measuring $6\\text{ cm}$ and $8\\text{ cm}$, what is the length of the hypotenuse?",
                "options": ["9 cm", "10 cm", "12 cm", "14 cm"],
                "ans": 1,
                "feedback": "Using $a^2 + b^2 = c^2$: $6^2 + 8^2 = 36 + 64 = 100$. Therefore, $c = \\sqrt{100} = \\mathbf{10\\text{ cm}}$."
            },
            {
                "q": "What is the historical significance of the Baudhāyana Śulbasūtras regarding this theorem?",
                "options": [
                    "They were the earliest known texts to explicitly state the theorem for rectangles and right triangles",
                    "They proved the theorem only for equilateral triangles",
                    "They disproved the theorem using circles",
                    "They were written in the 18th century"
                ],
                "ans": 0,
                "feedback": "The Baudhāyana Śulbasūtra (c. 800 BCE) is universally recognized as the earliest surviving explicit statement and constructive application of this theorem."
            }
        ]
    },
    {
        "id": 2,
        "title": "Doubling a Square",
        "subtitle": "Diagonal Construction & Area Expansion",
        "sim_type": "square_doubler_diagonal_grid",
        "voice": "How do you construct a square whose area is exactly twice that of a given square? The secret lies along the diagonal.",
        "content": """
<h4>The Diagonal of a Square</h4>
<p>Consider a square of side length $1\\text{ unit}$. Its area is $A_1 = 1 \\times 1 = 1\\text{ sq unit}$.</p>
<p>How can we construct another square that has exactly <strong>double the area</strong> ($2\\text{ sq units}$)?</p>
<ul>
  <li>If you simply double the side length to $2$, the new area becomes $2^2 = 4\\text{ sq units}$, which is <strong>four times</strong>, not twice!</li>
  <li>To double the area, draw the diagonal of the unit square. By the theorem:
  $$d^2 = 1^2 + 1^2 = 2 \\implies d = \\sqrt{2}$$</li>
</ul>
<p>If you construct a new square using this diagonal $d$ as the side length, its area will be:</p>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{\\text{Area}} = d^2 = (\\sqrt{2})^2 = \\mathbf{2\\text{ sq units}} = 2 \\times A_1$$
</div>
<h4>Visualizing with 4 Triangular Quarters</h4>
<p>The unit square can be partitioned into $4$ congruent right isosceles triangles. The new tilted square built on the diagonal is composed of exactly $4$ such half-squares, proving directly without algebra that its area is exactly twice that of the original square.</p>
""",
        "checkpoints": [
            {
                "q": "If a square has an area of $25\\text{ cm}^2$, what is the area of a square constructed on its diagonal?",
                "options": ["35 cm²", "50 cm²", "75 cm²", "100 cm²"],
                "ans": 1,
                "feedback": "The square on the diagonal always has exactly double the area of the original square: $2 \\times 25 = \\mathbf{50\\text{ cm}^2}$."
            },
            {
                "q": "If you double the side length of a square from $s$ to $2s$, by what factor does its area increase?",
                "options": ["2 times", "3 times", "4 times", "8 times"],
                "ans": 2,
                "feedback": "Area scales quadratically: $\\text{New Area} = (2s)^2 = 4s^2$, which is $\\mathbf{4\\text{ times}}$ the original area."
            }
        ]
    },
    {
        "id": 3,
        "title": "Halving a Square",
        "subtitle": "Connecting Midpoints & Inscribed Geometries",
        "sim_type": "square_halver_origami_lab",
        "voice": "Just as the diagonal doubles a square, connecting the midpoints of its four sides produces a square with exactly half the original area.",
        "content": """
<h4>The Midpoint Square Construction</h4>
<p>Suppose you have a square $ABCD$ with side length $s$ and area $A_0 = s^2$.</p>
<p>Mark the midpoints of the four sides: $P, Q, R, S$. Connect them in order to form the quadrilateral $PQRS$.</p>
<ul>
  <li>Each corner cut off is a right-angled isosceles triangle with legs $\\frac{s}{2}$ and $\\frac{s}{2}$.</li>
  <li>Area of each corner triangle:
  $$\\text{Area}_{\\text{corner}} = \\frac{1}{2} \\times \\frac{s}{2} \\times \\frac{s}{2} = \\frac{s^2}{8}$$</li>
  <li>Total area removed by all $4$ corner triangles:
  $$4 \\times \\frac{s^2}{8} = \\frac{s^2}{2}$$</li>
</ul>
<div style="background:#0f172a; border-left:4px solid #f59e0b; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{\\text{Area}(PQRS)} = s^2 - \\frac{s^2}{2} = \\mathbf{\\frac{s^2}{2}} = \\mathbf{\\frac{1}{2} \\text{Area}(ABCD)}$$
</div>
<h4>Side Length of the Inscribed Square</h4>
<p>Using Baudhāyana's theorem on one corner triangle:</p>
$$PQ^2 = \\left(\\frac{s}{2}\\right)^2 + \\left(\\frac{s}{2}\\right)^2 = \\frac{s^2}{4} + \\frac{s^2}{4} = \\frac{s^2}{2} \\implies PQ = \\frac{s}{\\sqrt{2}}$$
<p>This provides an elegant geometric method to halve any square without measuring fractions.</p>
""",
        "checkpoints": [
            {
                "q": "A square has an area of $64\\text{ sq units}$. A new square is formed by joining the midpoints of its four sides. What is the area of this new square?",
                "options": ["16 sq units", "32 sq units", "48 sq units", "64 sq units"],
                "ans": 1,
                "feedback": "Connecting midpoints of the sides produces a square of half the area: $\\frac{64}{2} = \\mathbf{32\\text{ sq units}}$."
            },
            {
                "q": "What is the side length of the inner square formed by joining the midpoints of a square of side $10\\text{ cm}$?",
                "options": ["5 cm", "5√2 cm", "10√2 cm", "7.5 cm"],
                "ans": 1,
                "feedback": "Each leg of the corner triangle is $5\\text{ cm}$. The hypotenuse is $\\sqrt{5^2 + 5^2} = \\sqrt{50} = \\mathbf{5\\sqrt{2}\\text{ cm}}$."
            }
        ]
    },
    {
        "id": 4,
        "title": "Hypotenuse of an Isosceles Right Triangle",
        "subtitle": "The 45°-45°-90° Triangle & The √2 Invariant Ratio",
        "sim_type": "isosceles_right_hypotenuse_explorer",
        "voice": "In an isosceles right triangle, both legs are equal in length. The hypotenuse is always equal to the leg length multiplied by the square root of two.",
        "content": """
<h4>The Special 45°-45°-90° Triangle</h4>
<p>When a right-angled triangle has two equal legs ($a = b = s$), the two acute angles must each be $45^\\circ$ because the angle sum of any triangle is $180^\\circ$:</p>
$$90^\\circ + 45^\\circ + 45^\\circ = 180^\\circ$$
<h4>Computing the Hypotenuse</h4>
<p>Applying the theorem with $a = s$ and $b = s$:</p>
$$c^2 = s^2 + s^2 = 2s^2$$
<div style="background:#0f172a; border-left:4px solid #38bdf8; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{c = \\sqrt{2s^2} = s\\sqrt{2}}$$
</div>
<h4>The Universal Ratio of Diagonal to Side</h4>
<ul>
  <li>If $s = 1$, then $c = \\sqrt{2} \\approx 1.4142$</li>
  <li>If $s = 5$, then $c = 5\\sqrt{2} \\approx 7.071$</li>
  <li>If $s = 10$, then $c = 10\\sqrt{2} \\approx 14.142$</li>
</ul>
<p>In every square and isosceles right triangle in the universe, the ratio of the diagonal (hypotenuse) to the side is the mathematical constant $\\mathbf{\\sqrt{2}}$.</p>
""",
        "checkpoints": [
            {
                "q": "What is the exact hypotenuse of an isosceles right triangle whose legs are each $7\\text{ cm}$?",
                "options": ["7 cm", "14 cm", "7√2 cm", "49 cm"],
                "ans": 2,
                "feedback": "$c = \\sqrt{7^2 + 7^2} = \\sqrt{49 \\times 2} = \\mathbf{7\\sqrt{2}\\text{ cm}}$."
            },
            {
                "q": "If the hypotenuse of an isosceles right triangle is $12\\sqrt{2}\\text{ cm}$, what is the length of each leg?",
                "options": ["6 cm", "12 cm", "24 cm", "12√2 cm"],
                "ans": 1,
                "feedback": "Since $c = s\\sqrt{2}$, if $c = 12\\sqrt{2}$, then each leg $s = \\mathbf{12\\text{ cm}}$."
            }
        ]
    },
    {
        "id": 5,
        "title": "Decimal Representation of √2",
        "subtitle": "Baudhāyana's Brilliant Ancient Rational Approximation",
        "sim_type": "root2_baudhayana_approximation_dial",
        "voice": "The square root of two is an irrational number with non-repeating, non-terminating decimals. Over twenty-eight centuries ago, Baudhāyana discovered an astonishing rational formula accurate to five decimal places.",
        "content": """
<h4>The Nature of √2</h4>
<p>$\\sqrt{2}$ cannot be written as a simple fraction $\\frac{p}{q}$ of integers. It is an <strong>irrational number</strong> whose decimal expansion never repeats and never terminates:</p>
$$\\sqrt{2} = 1.414213562373095...$$
<h4>Baudhāyana's Śulbasūtra Approximation</h4>
<p>In the <em>Baudhāyana Śulbasūtra</em> (verse 1.61), Baudhāyana gave a celebrated rule for finding the diagonal of a unit square:</p>
<blockquote style="font-style:italic; color:#93c5fd; border-left:3px solid #f59e0b; padding-left:10px; margin:10px 0;">
  "pramāṇaṁ tṛtīyena vardhayet tac ca caturthenātmacatustriṁśonena saviśeṣaḥ."<br>
  — <em>Increase the measure by its third, and this third by its own fourth, less the thirty-fourth part of that fourth.</em>
</blockquote>
<h4>Mathematical Translation</h4>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{\\sqrt{2} \\approx 1 + \\frac{1}{3} + \\frac{1}{3 \\times 4} - \\frac{1}{3 \\times 4 \\times 34} = 1 + \\frac{1}{3} + \\frac{1}{12} - \\frac{1}{408}}$$
</div>
<p>Bringing this to a common denominator of $408$:</p>
$$\\frac{408 + 136 + 34 - 1}{408} = \\mathbf{\\frac{577}{408}} \\approx \\mathbf{1.414215686...}$$
<p>Comparing with the true value $1.41421356...$, Baudhāyana's approximation differs by only $0.000002$, an astonishing accuracy of <strong>$99.99985\\%$</strong> achieved in ancient times!</p>
""",
        "checkpoints": [
            {
                "q": "What is the single rational fraction resulting from Baudhāyana's formula $1 + 1/3 + 1/12 - 1/408$?",
                "options": ["577/408", "333/235", "707/500", "408/577"],
                "ans": 0,
                "feedback": "$\\frac{408 + 136 + 34 - 1}{408} = \\mathbf{\\frac{577}{408}} \\approx 1.4142156...$"
            },
            {
                "q": "Why is √2 classified as an irrational number?",
                "options": [
                    "Because it is negative",
                    "Because its decimal representation is non-terminating and non-repeating",
                    "Because it equals zero",
                    "Because it can be written as a ratio of two integers"
                ],
                "ans": 1,
                "feedback": "An irrational number cannot be expressed as a ratio of integers and has an infinite, non-repeating decimal expansion."
            }
        ]
    },
    {
        "id": 6,
        "title": "General Solution: Dissection Proofs",
        "subtitle": "Geometric Proof by Rearrangement of Congruent Triangles",
        "sim_type": "general_dissection_proof_animator",
        "voice": "The theorem holds for right triangles of all proportions. By arranging four identical right triangles within an enclosing square, the geometric proof reveals itself without words.",
        "content": """
<h4>The Four-Triangle Enclosing Square Proof</h4>
<p>Consider four identical right-angled triangles with legs $a$ and $b$, and hypotenuse $c$.</p>
<p>Arrange these four triangles inside a large square of side length $(a + b)$:</p>
<ul>
  <li>The total area of the large outer square is:
  $$\\text{Area}_{\\text{outer}} = (a + b)^2 = a^2 + 2ab + b^2$$</li>
  <li>The four right triangles each have area $\\frac{1}{2}ab$. Combined area of all four triangles:
  $$4 \\times \\left(\\frac{1}{2}ab\\right) = 2ab$$</li>
  <li>The unfilled space inside the four triangles forms a square of side $c$, with area $c^2$.</li>
</ul>
<h4>Equating Areas</h4>
<p>The total area of the outer square equals the sum of the four triangles plus the inner square:</p>
$$(a + b)^2 = 4 \\times \\left(\\frac{1}{2}ab\\right) + c^2$$
$$a^2 + 2ab + b^2 = 2ab + c^2$$
<div style="background:#0f172a; border-left:4px solid #6366f1; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{a^2 + b^2 = c^2}$$
</div>
<p>Subtracting $2ab$ from both sides immediately proves the theorem universally for <em>any</em> side lengths $a$ and $b$!</p>
""",
        "checkpoints": [
            {
                "q": "In the dissection proof using an enclosing square of side $(a + b)$, what does the central unshaded shape represent?",
                "options": [
                    "A circle of diameter c",
                    "A square of side c with area c²",
                    "A rectangle of area ab",
                    "A triangle of area c²/2"
                ],
                "ans": 1,
                "feedback": "The four hypotenuses form the perimeter of a tilted inner square of side length $c$, with area $c^2$."
            },
            {
                "q": "If $a = 3$ and $b = 4$, what is the total area of the outer square $(a + b)^2$?",
                "options": ["25", "49", "12", "36"],
                "ans": 1,
                "feedback": "The outer side length is $a + b = 3 + 4 = 7$. The area is $7^2 = \\mathbf{49}$."
            }
        ]
    },
    {
        "id": 7,
        "title": "Combining Two Different Squares",
        "subtitle": "Adding Areas: a² + b² = c² in Action",
        "sim_type": "two_squares_area_combiner",
        "voice": "Given two squares of different sizes, how can we combine their areas into one single square? We construct a right triangle whose legs are the sides of the two given squares.",
        "content": """
<h4>The Area Addition Problem</h4>
<p>Suppose you are given two squares:</p>
<ul>
  <li>Square 1 has side $a = 3\\text{ cm}$ $\\implies \\text{Area} = a^2 = 9\\text{ cm}^2$</li>
  <li>Square 2 has side $b = 4\\text{ cm}$ $\\implies \\text{Area} = b^2 = 16\\text{ cm}^2$</li>
</ul>
<p>We want to find a single new square whose area is the exact sum of both squares:</p>
$$\\text{Target Area} = 9 + 16 = 25\\text{ cm}^2$$
<h4>The Construction Principle</h4>
<p>Instead of calculating square roots numerically, place the two side lengths $a$ and $b$ perpendicular to each other to form a right angle.</p>
<p>Connect the two remaining vertices with a line segment. This segment is the <strong>hypotenuse</strong> $c$ of the right triangle:</p>
$$c = \\sqrt{a^2 + b^2} = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5\\text{ cm}$$
<div style="background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{\\text{Area of square on } c = c^2 = a^2 + b^2 = 25\\text{ cm}^2}$$
</div>
<p>This geometric principle was utilized in the ancient Śulbasūtras for altar reshaping, ensuring altar areas could be combined without waste.</p>
""",
        "checkpoints": [
            {
                "q": "You want to combine a square of area $36\\text{ m}^2$ and a square of area $64\\text{ m}^2$ into a single square. What must be the side length of the combined square?",
                "options": ["10 m", "12 m", "14 m", "100 m"],
                "ans": 0,
                "feedback": "Total area $= 36 + 64 = 100\\text{ m}^2$. The side length of the combined square is $\\sqrt{100} = \\mathbf{10\\text{ m}}$."
            },
            {
                "q": "If two squares have side lengths $5\\text{ cm}$ and $12\\text{ cm}$, what is the area of the single square formed by combining them?",
                "options": ["144 cm²", "169 cm²", "17 cm²", "289 cm²"],
                "ans": 1,
                "feedback": "Total area $= 5^2 + 12^2 = 25 + 144 = \\mathbf{169\\text{ cm}^2}$ (which has side length $\\sqrt{169} = 13\\text{ cm}$)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Combining Two Squares Using Paper",
        "subtitle": "Hands-on Origami & Geometric Jigsaw Transformation",
        "sim_type": "paper_folding_pythagoras_jigsaw",
        "voice": "With just a pair of scissors and two paper squares, we can cut and rearrange them into a single perfect large square. This is a tactile geometric jigsaw puzzle.",
        "content": """
<h4>The Paper Transformation Experiment</h4>
<p>Take two paper squares of sides $a$ and $b$ (with $b \\ge a$). Place them side-by-side so their bases form a straight line of length $(a + b)$.</p>
<h4>The Cutting Lines</h4>
<ol>
  <li>Mark a segment of length $a$ along the top edge of square $b$.</li>
  <li>Draw two straight cutting lines connecting this point to the bottom outer corners of the combined shape.</li>
  <li>Each cutting line has a length exactly equal to the hypotenuse $c = \\sqrt{a^2 + b^2}$.</li>
  <li>Cut along these two lines to produce three or four puzzle pieces.</li>
</ol>
<h4>The Reassembly</h4>
<p>When you rotate and translate these cut pieces, they assemble seamlessly into a <strong>single square of side $c$</strong> without any overlap or gaps!</p>
<div style="background:#0f172a; border-left:4px solid #a855f7; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{\\text{Area}(Square}_a) + \\text{Area}(Square_b) = \\mathbf{\\text{Area}(Square}_c)$$
</div>
<p>This hands-on dissection shows conservation of area: no paper is lost or added, proving $a^2 + b^2 = c^2$ tangibly.</p>
""",
        "checkpoints": [
            {
                "q": "In a paper cutting proof combining two squares of sides $a$ and $b$, what is the length of the boundary lines of the final assembled square?",
                "options": ["a + b", "√(a² + b²)", "2(a + b)", "b - a"],
                "ans": 1,
                "feedback": "The sides of the final assembled square are the cut edges, each having length $c = \\mathbf{\\sqrt{a^2 + b^2}}$."
            },
            {
                "q": "What fundamental geometric law guarantees that the pieces from the two squares fit into the larger square?",
                "options": [
                    "Conservation of geometric area under rigid motion (rotation and translation)",
                    "Dilation scaling",
                    "Curvature of space",
                    "Spherical trigonometry"
                ],
                "ans": 0,
                "feedback": "Rigid motions preserve distances and areas. Cutting and rearranging pieces preserves the total area exactly."
            }
        ]
    },
    {
        "id": 9,
        "title": "Using Baudhāyana's Theorem",
        "subtitle": "Real-World Distance, Altitude & Diagonal Problems",
        "sim_type": "baudhayana_altitude_ladder_workbench",
        "voice": "From ladders propped against walls to television screens and tree heights, Baudhāyana's theorem solves critical engineering and surveying problems every day.",
        "content": """
<h4>Common Practical Applications</h4>
<p>The theorem allows us to calculate any one of the three sides of a right triangle when the other two are known:</p>
<ol>
  <li><strong>To find the Hypotenuse:</strong> $c = \\sqrt{a^2 + b^2}$</li>
  <li><strong>To find a Leg ($a$ or $b$):</strong> $a = \\sqrt{c^2 - b^2}$ and $b = \\sqrt{c^2 - a^2}$</li>
</ol>
<h4>Case 1: The Leaning Ladder Problem</h4>
<p>A ladder of length $13\\text{ m}$ is placed against a vertical wall. If its foot is $5\\text{ m}$ away from the base of the wall, how high up the wall does it reach?</p>
$$h = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = \\mathbf{12\\text{ m}}$$
<h4>Case 2: The Broken Tree Problem</h4>
<p>A tree breaks at a height of $9\\text{ m}$ from the ground and its top touches the ground at a distance of $12\\text{ m}$ from its base. What was the original height of the tree?</p>
$$\\text{Broken part} = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15\\text{ m}$$
$$\\text{Total Height} = 9 + 15 = \\mathbf{24\\text{ m}}$$
""",
        "checkpoints": [
            {
                "q": "A $15\\text{ m}$ ladder reaches a window $12\\text{ m}$ high. How far is the foot of the ladder from the wall?",
                "options": ["6 m", "9 m", "10 m", "11 m"],
                "ans": 1,
                "feedback": "$d = \\sqrt{15^2 - 12^2} = \\sqrt{225 - 144} = \\sqrt{81} = \\mathbf{9\\text{ m}}$."
            },
            {
                "q": "A rectangular field has length $40\\text{ m}$ and width $30\\text{ m}$. What is the straight-line distance across its diagonal?",
                "options": ["45 m", "50 m", "60 m", "70 m"],
                "ans": 1,
                "feedback": "$\\text{Diagonal} = \\sqrt{40^2 + 30^2} = \\sqrt{1600 + 900} = \\sqrt{2500} = \\mathbf{50\\text{ m}}$."
            }
        ]
    },
    {
        "id": 10,
        "title": "Right-Triangles with Integer Sidelengths",
        "subtitle": "Pythagorean Triples & Ancient Parametric Generators",
        "sim_type": "pythagorean_triples_generator",
        "voice": "When all three sides of a right triangle are whole numbers, they form a Pythagorean triple. The smallest and most famous is 3, 4, 5.",
        "content": """
<h4>Definition of a Pythagorean Triple</h4>
<p>A set of three positive integers $(a, b, c)$ that satisfy the equation $a^2 + b^2 = c^2$ is called a <strong>Pythagorean Triple</strong>.</p>
<p>If $\\gcd(a, b, c) = 1$, the triple is called <strong>primitive</strong>.</p>
<h4>Classic Primitive Triples</h4>
<div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px; margin:12px 0;">
  <div style="background:#1e293b; padding:10px; border-radius:8px; border:1px solid #334155;">
    <strong>(3, 4, 5):</strong> $9 + 16 = 25$
  </div>
  <div style="background:#1e293b; padding:10px; border-radius:8px; border:1px solid #334155;">
    <strong>(5, 12, 13):</strong> $25 + 144 = 169$
  </div>
  <div style="background:#1e293b; padding:10px; border-radius:8px; border:1px solid #334155;">
    <strong>(7, 24, 25):</strong> $49 + 576 = 625$
  </div>
  <div style="background:#1e293b; padding:10px; border-radius:8px; border:1px solid #334155;">
    <strong>(8, 15, 17):</strong> $64 + 225 = 289$
  </div>
</div>
<h4>Euclid's & Indian Parametric Generator</h4>
<p>For any two integers $m > n > 0$ of opposite parity and $\\gcd(m, n) = 1$:</p>
<div style="background:#0f172a; border-left:4px solid #f59e0b; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{a = m^2 - n^2, \\quad b = 2mn, \\quad c = m^2 + n^2}$$
</div>
<p>Verifying the identity algebraically:</p>
$$(m^2 - n^2)^2 + (2mn)^2 = m^4 - 2m^2n^2 + n^4 + 4m^2n^2 = m^4 + 2m^2n^2 + n^4 = (m^2 + n^2)^2$$
""",
        "checkpoints": [
            {
                "q": "Which of the following sets of side lengths forms a valid Pythagorean Triple?",
                "options": ["(6, 8, 10)", "(5, 10, 15)", "(4, 5, 6)", "(7, 11, 13)"],
                "ans": 0,
                "feedback": "$6^2 + 8^2 = 36 + 64 = 100 = 10^2$. This is a multiple of $(3, 4, 5)$ scaled by $2$."
            },
            {
                "q": "Using the generator formula with $m = 3$ and $n = 2$, which primitive triple is generated?",
                "options": ["(3, 4, 5)", "(5, 12, 13)", "(7, 24, 25)", "(8, 15, 17)"],
                "ans": 1,
                "feedback": "$a = 3^2 - 2^2 = 5$, $b = 2(3)(2) = 12$, $c = 3^2 + 2^2 = 13$. The triple is $\\mathbf{(5, 12, 13)}$."
            }
        ]
    },
    {
        "id": 11,
        "title": "A Long-Standing Open Problem",
        "subtitle": "Euler's Brick & The Unsolved Perfect Cuboid Mystery",
        "sim_type": "euler_brick_open_problem_explorer",
        "voice": "Can we extend the theorem into three dimensions? While Euler discovered bricks where all face diagonals are integers, whether a cuboid exists where every edge, face diagonal, AND space diagonal are all integers remains one of mathematics' greatest unsolved mysteries.",
        "content": """
<h4>From 2D Triangles to 3D Cuboids</h4>
<p>In two dimensions, infinitely many integer right triangles exist. What happens in three dimensions with a rectangular box (cuboid) having edges $a, b, c$?</p>
<ul>
  <li>Face diagonals: $d_1 = \\sqrt{a^2 + b^2}$, $d_2 = \\sqrt{b^2 + c^2}$, $d_3 = \\sqrt{c^2 + a^2}$</li>
  <li>Space diagonal (interior diagonal): $D = \\sqrt{a^2 + b^2 + c^2}$</li>
</ul>
<h4>Euler's Brick (Discovered by Paul Halcke in 1719)</h4>
<p>An <strong>Euler Brick</strong> is a cuboid where all edges $a, b, c$ and all three face diagonals $d_1, d_2, d_3$ are integers.</p>
<p>The smallest Euler brick has edges:</p>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{a = 44, \\quad b = 117, \\quad c = 240}$$
  $$d_1 = \\sqrt{44^2 + 117^2} = 125, \\quad d_2 = \\sqrt{117^2 + 240^2} = 267, \\quad d_3 = \\sqrt{44^2 + 240^2} = 244$$
</div>
<h4>The Unsolved \"Perfect Cuboid\" Problem</h4>
<p>In Halcke's brick, the space diagonal is $\\sqrt{44^2 + 117^2 + 240^2} = \\sqrt{77225} \\approx 277.89$ (not an integer!).</p>
<p>To this day, <strong>nobody knows</strong> if a \"Perfect Cuboid\" exists where all seven quantities ($a, b, c, d_1, d_2, d_3, D$) are integers, despite exhaustive computer searches up to edge lengths of trillions!</p>
""",
        "checkpoints": [
            {
                "q": "What condition must be satisfied for a rectangular box to qualify as an Euler Brick?",
                "options": [
                    "All edges and all 3 face diagonals must be integers",
                    "All edges must be equal (a cube)",
                    "The volume must be a perfect square",
                    "The space diagonal must be zero"
                ],
                "ans": 0,
                "feedback": "An Euler brick requires all 3 edges ($a, b, c$) and all 3 face diagonals to be integers."
            },
            {
                "q": "What makes the 'Perfect Cuboid' a long-standing open mathematical problem?",
                "options": [
                    "It was proven impossible by Euclid",
                    "No one has found one, yet no one has proven that one cannot exist",
                    "Computers cannot compute square roots",
                    "It only exists in non-Euclidean space"
                ],
                "ans": 1,
                "feedback": "Mathematicians do not know whether a perfect cuboid exists or is mathematically impossible—it remains completely unsolved."
            }
        ]
    },
    {
        "id": 12,
        "title": "Further Applications of the Theorem",
        "subtitle": "3D Space Diagonals, Coordinate Distance & Circle Chords",
        "sim_type": "three_d_space_diagonal_scanner",
        "voice": "The theorem extends naturally to three dimensions and coordinate planes, enabling GPS navigation, 3D graphics rendering, and celestial tracking.",
        "content": """
<h4>1. The 3D Space Diagonal of a Room</h4>
<p>What is the longest straight pole that can fit inside a rectangular room of length $l$, width $w$, and height $h$?</p>
<ul>
  <li>First find the floor diagonal: $d_\\text{floor}^2 = l^2 + w^2$</li>
  <li>The vertical height $h$ is perpendicular to the floor, forming a right triangle with $d_\\text{floor}$ and the 3D space diagonal $D$:
  $$D^2 = d_\\text{floor}^2 + h^2 = (l^2 + w^2) + h^2$$</li>
</ul>
<div style="background:#0f172a; border-left:4px solid #38bdf8; padding:12px; margin:12px 0; border-radius:6px;">
  $$\\mathbf{D = \\sqrt{l^2 + w^2 + h^2}}$$
</div>
<h4>2. The Coordinate Distance Formula</h4>
<p>In Cartesian coordinate geometry, the straight-line distance between two points $P(x_1, y_1)$ and $Q(x_2, y_2)$ is obtained by constructing a right triangle with horizontal leg $\\Delta x = x_2 - x_1$ and vertical leg $\\Delta y = y_2 - y_1$:</p>
$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
<h4>3. Circle Geometry: Distance of a Chord from the Center</h4>
<p>A perpendicular from the center of a circle of radius $R$ bisects any chord of length $L$. The distance $d$ of the chord from the center satisfies:</p>
$$d = \\sqrt{R^2 - (L/2)^2}$$
""",
        "checkpoints": [
            {
                "q": "What is the length of the longest rod that can be placed inside a box measuring $12\\text{ cm} \\times 4\\text{ cm} \\times 3\\text{ cm}$?",
                "options": ["13 cm", "14 cm", "15 cm", "19 cm"],
                "ans": 0,
                "feedback": "$D = \\sqrt{12^2 + 4^2 + 3^2} = \\sqrt{144 + 16 + 9} = \\sqrt{169} = \\mathbf{13\\text{ cm}}$."
            },
            {
                "q": "Find the distance between points $A(1, 2)$ and $B(4, 6)$ on the coordinate plane.",
                "options": ["3", "4", "5", "7"],
                "ans": 2,
                "feedback": "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = \\mathbf{5}$."
            }
        ]
    },
    {
        "id": 13,
        "title": "Converse of the Baudhāyana-Pythagoras Theorem",
        "subtitle": "Classifying Triangles: Acute, Right, or Obtuse",
        "sim_type": "converse_triangle_classifier",
        "voice": "The converse of the theorem is equally powerful. If the square of the longest side equals the sum of the squares of the other two sides, the triangle is guaranteed to be a right-angled triangle.",
        "content": """
<h4>The Converse Theorem</h4>
<p>If in a triangle with side lengths $a, b, c$ (where $c$ is the longest side), the condition $a^2 + b^2 = c^2$ holds true, then the angle opposite to side $c$ is strictly a <strong>right angle ($90^\\circ$)</strong>.</p>
<h4>Tri-Fold Triangle Classification Rule</h4>
<p>By comparing $a^2 + b^2$ with $c^2$, you can determine the nature of <em>any</em> triangle without measuring angles:</p>
<div style="display:flex; flex-direction:column; gap:8px; margin:14px 0;">
  <div style="background:rgba(16,185,129,0.15); border-left:4px solid #10b981; padding:10px; border-radius:4px;">
    <strong>1. Right-Angled Triangle:</strong> $a^2 + b^2 = c^2$ (one angle equals $90^\\circ$)
  </div>
  <div style="background:rgba(6,182,212,0.15); border-left:4px solid #06b6d4; padding:10px; border-radius:4px;">
    <strong>2. Acute-Angled Triangle:</strong> $a^2 + b^2 > c^2$ (all three angles are $< 90^\\circ$)
  </div>
  <div style="background:rgba(244,63,94,0.15); border-left:4px solid #f43f5e; padding:10px; border-radius:4px;">
    <strong>3. Obtuse-Angled Triangle:</strong> $a^2 + b^2 < c^2$ (the largest angle is $> 90^\\circ$)
  </div>
</div>
<h4>Example Case</h4>
<p>Consider sides $6, 7, 9$. Longest side is $9$.</p>
$$6^2 + 7^2 = 36 + 49 = 85, \\quad 9^2 = 81$$
<p>Since $85 > 81$ ($a^2 + b^2 > c^2$), the triangle is <strong>acute</strong>!</p>
""",
        "checkpoints": [
            {
                "q": "A triangle has side lengths $7\\text{ cm}$, $8\\text{ cm}$, and $12\\text{ cm}$. What type of triangle is it?",
                "options": ["Right-angled", "Acute-angled", "Obtuse-angled", "Equilateral"],
                "ans": 2,
                "feedback": "$7^2 + 8^2 = 49 + 64 = 113$. $12^2 = 144$. Since $113 < 144$ ($a^2 + b^2 < c^2$), the triangle is $\\mathbf{obtuse}$."
            },
            {
                "q": "If sides are $9, 12, 15$, verify if the triangle contains a right angle.",
                "options": [
                    "Yes, because 9² + 12² = 81 + 144 = 225 = 15²",
                    "No, because 15 is odd",
                    "No, because 9 + 12 > 15",
                    "Cannot be determined without a protractor"
                ],
                "ans": 0,
                "feedback": "$81 + 144 = 225 = 15^2$. By the converse of Baudhāyana's theorem, it is strictly a right-angled triangle."
            }
        ]
    },
    {
        "id": 14,
        "title": "Baudhāyana's Rope Geometry & Śulbasūtras",
        "subtitle": "Ancient Altar Constructions & Perpendicular Cords",
        "sim_type": "sulbasutra_rope_altar_builder",
        "voice": "The word Sulba means rope or cord. Ancient Indian master architects used knotted measuring ropes to construct perfect perpendicular corners and majestic ritual altars.",
        "content": """
<h4>The Vedic Science of Cord Geometry (Śulba-vijñāna)</h4>
<p>The <em>Śulbasūtras</em> (composed between 800 BCE and 500 BCE by Baudhāyana, Mānava, Āpastamba, and Kātyāyana) are the world's earliest geometry manuals dedicated to altar engineering.</p>
<h4>How Ancient Architects Created 90° Corners Using Knotted Cords</h4>
<p>How do you construct a perfectly square corner on a vast open field without modern optical instruments?</p>
<ol>
  <li>Take a long rope and tie knots to divide it into sections of $3$, $4$, and $5$ units (total length $12$ units).</li>
  <li>Fasten the two ends together.</li>
  <li>Peg the $3$-unit section along the designated east-west baseline.</li>
  <li>Pull the remaining knot taut to form a triangle: the angle between the $3$-unit and $4$-unit sides is guaranteed to be an <strong>exact right angle ($90^\\circ$)</strong>!</li>
</ol>
<h4>Śyenaciti (The Falcon Altar) & Mahāvedi</h4>
<p>Vedic altars required precise geometric areas while adopting complex symbolic shapes like flying falcons (<em>Śyenaciti</em>). The priests used Baudhāyana's theorem to transform shapes—such as turning a square into a rectangle, or combining multiple squares—while preserving total altar area exactly.</p>
""",
        "checkpoints": [
            {
                "q": "What is the meaning of the Sanskrit root word 'Śulba' in Śulbasūtra?",
                "options": ["Stone or brick", "Rope, cord, or string", "Chariot", "Fire"],
                "ans": 1,
                "feedback": "'Śulba' means a rope or measuring cord, highlighting that ancient geometry was practiced through precise cord manipulation."
            },
            {
                "q": "Which knotted rope length combinations were commonly used in the Śulbasūtras to construct right angles?",
                "options": ["(3, 4, 5) and (5, 12, 13)", "(2, 3, 4) and (4, 5, 6)", "(1, 1, 1) only", "(10, 20, 30)"],
                "ans": 0,
                "feedback": "Both $(3, 4, 5)$ and $(5, 12, 13)$ are prominent triples recorded in the Baudhāyana and Āpastamba Śulbasūtras."
            }
        ]
    },
    {
        "id": 15,
        "title": "Chapter Summary & Master Formulas",
        "subtitle": "The Unified Repository of Geometric Relations",
        "sim_type": "baudhayana_master_formula_matrix",
        "voice": "Here is our master synthesis of all fundamental formulas and geometric identities discovered across this chapter.",
        "content": """
<h4>The Master Theorem Matrix</h4>
<div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; font-size:13.5px;">
  <table style="width:100%; border-collapse:collapse; color:#cbd5e1;">
    <tr style="border-bottom:1px solid #475569; color:#fcd34d;">
      <th style="padding:6px; text-align:left;">Relation / Application</th>
      <th style="padding:6px; text-align:left;">Mathematical Formula</th>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Right Triangle Hypotenuse</td>
      <td style="padding:6px; color:#38bdf8;">$c = \\sqrt{a^2 + b^2}$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Right Triangle Leg</td>
      <td style="padding:6px; color:#38bdf8;">$a = \\sqrt{c^2 - b^2}$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Diagonal of a Square (side s)</td>
      <td style="padding:6px; color:#34d399;">$d = s\\sqrt{2}$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Diagonal of a Rectangle (l × w)</td>
      <td style="padding:6px; color:#34d399;">$d = \\sqrt{l^2 + w^2}$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">3D Space Diagonal of a Cuboid</td>
      <td style="padding:6px; color:#a5b4fc;">$D = \\sqrt{l^2 + w^2 + h^2}$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Altitude of Equilateral Triangle</td>
      <td style="padding:6px; color:#fcd34d;">$h = \\frac{\\sqrt{3}}{2}s$</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px;">Baudhāyana's √2 Approximation</td>
      <td style="padding:6px; color:#fda4af;">$1 + \\frac{1}{3} + \\frac{1}{12} - \\frac{1}{408} = \\frac{577}{408}$</td>
    </tr>
    <tr>
      <td style="padding:6px;">Pythagorean Triple Generator</td>
      <td style="padding:6px; color:#f59e0b;">$m^2 - n^2, \\; 2mn, \\; m^2 + n^2$</td>
    </tr>
  </table>
</div>
""",
        "checkpoints": [
            {
                "q": "What is the altitude of an equilateral triangle of side $6\\text{ cm}$?",
                "options": ["3 cm", "3√3 cm", "6√3 cm", "12 cm"],
                "ans": 1,
                "feedback": "Using right triangle with hypotenuse $6$ and base half-side $3$: $h = \\sqrt{6^2 - 3^2} = \\sqrt{36 - 9} = \\sqrt{27} = \\mathbf{3\\sqrt{3}\\text{ cm}}$."
            },
            {
                "q": "What is the length of the diagonal of a rectangle of sides $8\\text{ cm}$ and $15\\text{ cm}$?",
                "options": ["16 cm", "17 cm", "23 cm", "25 cm"],
                "ans": 1,
                "feedback": "$d = \\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = \\sqrt{289} = \\mathbf{17\\text{ cm}}$."
            }
        ]
    },
    {
        "id": 16,
        "title": "Puzzle Time: Find the Colours!",
        "subtitle": "Hypotenuse Distance & Chromatic Grid Geometry",
        "sim_type": "find_the_colours_puzzle_room",
        "voice": "Welcome to Puzzle Time! In 'Find the Colours', we explore graph distances and grid points. Can you color points so that no two vertices at distance square-root of 5 share the same hue?",
        "content": """
<h4>The 'Find the Colours' Geometry Challenge</h4>
<p>On an integer grid, consider points that are separated by a straight-line distance of $\\sqrt{5}$.</p>
<ul>
  <li>Notice that $1^2 + 2^2 = 1 + 4 = 5$, so the distance between any point $(x, y)$ and $(x \\pm 1, y \\pm 2)$ or $(x \\pm 2, y \\pm 1)$ is exactly:
  $$d = \\sqrt{(\\pm 1)^2 + (\\pm 2)^2} = \\mathbf{\\sqrt{5}}$$</li>
  <li>This is exactly the movement of a <strong>Knight in chess</strong>!</li>
</ul>
<h4>The Chromatic Problem</h4>
<p>What is the minimum number of colours required to colour the grid so that <strong>no two points at distance $\\sqrt{5}$ share the same colour</strong>?</p>
<ul>
  <li>Can it be done with $2$ colours? No, because cycles of odd length (like triangles or 5-cycles) can be formed.</li>
  <li>Can it be done with $4$ or $5$ colours? Yes! By tiling the plane with a periodic $5$-colour pattern based on the knight's L-movements!</li>
</ul>
<p>This puzzle connects Baudhāyana's right-triangle theorem directly to modern discrete mathematics and the chromatic number of the plane.</p>
""",
        "checkpoints": [
            {
                "q": "What is the straight-line distance between the grid origin (0, 0) and the point (2, 1)?",
                "options": ["3", "√3", "√5", "5"],
                "ans": 2,
                "feedback": "$d = \\sqrt{2^2 + 1^2} = \\sqrt{4 + 1} = \\mathbf{\\sqrt{5}}$."
            },
            {
                "q": "Why does a knight's move in chess correspond to a distance of √5 on a coordinate grid?",
                "options": [
                    "Because it moves 2 squares in one direction and 1 square perpendicular: 2² + 1² = 5",
                    "Because it moves 5 squares diagonally",
                    "Because a chessboard has 5 rows",
                    "Because a knight is worth 5 points"
                ],
                "ans": 0,
                "feedback": "The L-move represents legs of $2$ and $1$. By Baudhāyana's theorem, hypotenuse is $\\sqrt{2^2 + 1^2} = \\sqrt{5}$."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge — Part I (Questions 1 to 10)",
        "subtitle": "Core Principles, Squares & √2 Arithmetic",
        "sim_type": "quiz_slide",
        "voice": "Now begin Part One of the Mastery Challenge. Test your understanding of fundamental theorem concepts, doubling squares, and Baudhāyana's approximation.",
        "quiz_range": [1, 10]
    },
    {
        "id": 18,
        "title": "Mastery Challenge — Part II (Questions 11 to 20)",
        "subtitle": "Combining Squares, Dissections & Real-World Heights",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Part Two. Here you will solve problems on combining squares, paper folding proofs, ladders, and broken tree heights.",
        "quiz_range": [11, 20]
    },
    {
        "id": 19,
        "title": "Mastery Challenge — Part III (Questions 21 to 30)",
        "subtitle": "Pythagorean Triples, Euler's Brick & 3D Spaces",
        "sim_type": "quiz_slide",
        "voice": "Proceed to Part Three. Explore integer triples, parametric generators, 3D space diagonals, and Euler's Brick mystery.",
        "quiz_range": [21, 30]
    },
    {
        "id": 20,
        "title": "Mastery Challenge — Part IV (Questions 31 to 40)",
        "subtitle": "Converse Theorems, Śulbasūtra Altars & Color Puzzles",
        "sim_type": "quiz_slide",
        "voice": "Final stretch! Test your mastery on the converse theorem, triangle classification, ancient cord geometry, and grid distance puzzles.",
        "quiz_range": [31, 40]
    }
]

questions = [
    # Slide 17: Questions 1 to 10
    {
        "num": 1,
        "slide": 17,
        "question": "In a right-angled triangle, the lengths of the two legs are $9\\text{ cm}$ and $12\\text{ cm}$. Find the length of the hypotenuse.",
        "options": ["13 cm", "14 cm", "15 cm", "18 cm"],
        "correct": 2,
        "solution": "Using the Baudhāyana-Pythagoras theorem:\\n$$c^2 = a^2 + b^2 = 9^2 + 12^2 = 81 + 144 = 225$$\\n$$c = \\sqrt{225} = \\mathbf{15\\text{ cm}}$$\\n\\nNotice this is the primitive triple $(3, 4, 5)$ scaled by a factor of $3$ ($3 \\times 3 = 9$, $4 \\times 3 = 12$, $5 \\times 3 = 15$)."
    },
    {
        "num": 2,
        "slide": 17,
        "question": "A square has a side length of $6\\text{ cm}$. What is the exact area of the square constructed on its diagonal?",
        "options": ["36 cm²", "48 cm²", "72 cm²", "144 cm²"],
        "correct": 2,
        "solution": "Original square area $= 6^2 = 36\\text{ cm}^2$.\\n\\nThe square constructed on the diagonal has side length $d = 6\\sqrt{2}$.\\nIts area is:\\n$$\\text{Area} = d^2 = (6\\sqrt{2})^2 = 36 \\times 2 = \\mathbf{72\\text{ cm}^2}$$\\n\\nThe square on the diagonal always has exactly **twice the area** of the original square."
    },
    {
        "num": 3,
        "slide": 17,
        "question": "In an isosceles right triangle, the hypotenuse is $16\\text{ cm}$. What is the area of this triangle?",
        "options": ["32 cm²", "64 cm²", "128 cm²", "256 cm²"],
        "correct": 1,
        "solution": "Let both legs be $s$. Then $c^2 = s^2 + s^2 = 2s^2 = 16^2 = 256$, so $s^2 = 128$.\\n\\nThe area of the right triangle is:\\n$$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2}s^2 = \\frac{1}{2}(128) = \\mathbf{64\\text{ cm}^2}$$\\n\\nQuick shortcut: For any right isosceles triangle with hypotenuse $c$, $\\text{Area} = \\frac{c^2}{4} = \\frac{256}{4} = 64$."
    },
    {
        "num": 4,
        "slide": 17,
        "question": "What is the value of Baudhāyana's rational approximation $1 + \\frac{1}{3} + \\frac{1}{12} - \\frac{1}{408}$ expressed as an improper fraction?",
        "options": ["333/235", "577/408", "707/500", "408/577"],
        "correct": 1,
        "solution": "Find a common denominator ($408$):\\n$$1 = \\frac{408}{408}, \\quad \\frac{1}{3} = \\frac{136}{408}, \\quad \\frac{1}{12} = \\frac{34}{408}, \\quad -\\frac{1}{408}$$\\n$$\\text{Sum} = \\frac{408 + 136 + 34 - 1}{408} = \\mathbf{\\frac{577}{408}}$$\\n\\nDividing gives $1.414215686...$, which matches $\\sqrt{2} = 1.41421356...$ to $5$ decimal places!"
    },
    {
        "num": 5,
        "slide": 17,
        "question": "If the diagonal of a square is $10\\text{ cm}$, what is its perimeter?",
        "options": ["20 cm", "20√2 cm", "40 cm", "40√2 cm"],
        "correct": 1,
        "solution": "Since $d = s\\sqrt{2} = 10$, we have:\\n$$s = \\frac{10}{\\sqrt{2}} = \\frac{10\\sqrt{2}}{2} = 5\\sqrt{2}\\text{ cm}$$\\n\\nPerimeter of square $= 4s = 4 \\times 5\\sqrt{2} = \\mathbf{20\\sqrt{2}\\text{ cm}}$."
    },
    {
        "num": 6,
        "slide": 17,
        "question": "A right triangle has hypotenuse $25\\text{ cm}$ and one leg $7\\text{ cm}$. Find the length of the other leg.",
        "options": ["20 cm", "22 cm", "24 cm", "26 cm"],
        "correct": 2,
        "solution": "Using $b = \\sqrt{c^2 - a^2}$:\\n$$b = \\sqrt{25^2 - 7^2} = \\sqrt{625 - 49} = \\sqrt{576} = \\mathbf{24\\text{ cm}}$$\\n\\nThis corresponds to the primitive triple $(7, 24, 25)$."
    },
    {
        "num": 7,
        "slide": 17,
        "question": "A square of side length $12\\text{ cm}$ has its midpoints connected to form an inscribed square. What is the area of this inscribed square?",
        "options": ["36 cm²", "48 cm²", "72 cm²", "108 cm²"],
        "correct": 2,
        "solution": "Original square area $= 12^2 = 144\\text{ cm}^2$.\\n\\nJoining midpoints of the four sides always creates an inscribed square with exactly **half the original area**:\\n$$\\text{Inscribed Area} = \\frac{144}{2} = \\mathbf{72\\text{ cm}^2}$$."
    },
    {
        "num": 8,
        "slide": 17,
        "question": "What is the ratio of the diagonal of a square to its side length?",
        "options": ["1 : 1", "√2 : 1", "√3 : 1", "2 : 1"],
        "correct": 1,
        "solution": "For any square of side $s$, the diagonal is $d = s\\sqrt{2}$.\\n\\n$$\\text{Ratio} = \\frac{d}{s} = \\frac{s\\sqrt{2}}{s} = \\mathbf{\\sqrt{2} : 1}$$\\n\\nThis invariant holds for every Euclidean square."
    },
    {
        "num": 9,
        "slide": 17,
        "question": "If the area of a square is $50\\text{ m}^2$, what is the length of its diagonal?",
        "options": ["5 m", "10 m", "10√2 m", "25 m"],
        "correct": 1,
        "solution": "Area $= s^2 = 50\\text{ m}^2$.\\n\\nThe square of the diagonal is:\\n$$d^2 = s^2 + s^2 = 2s^2 = 2(50) = 100$$\\n$$d = \\sqrt{100} = \\mathbf{10\\text{ m}}$$"
    },
    {
        "num": 10,
        "slide": 17,
        "question": "In which ancient Indian text was the geometric statement of this theorem first recorded?",
        "options": [
            "Aryabhatiya",
            "Baudhāyana Śulbasūtra",
            "Lilavati",
            "Brahmasphutasiddhanta"
        ],
        "correct": 1,
        "solution": "The earliest explicit statement is found in the **Baudhāyana Śulbasūtra** (dating to approximately 800 BCE), long predating Greek records."
    },

    # Slide 18: Questions 11 to 20
    {
        "num": 11,
        "slide": 18,
        "question": "Two squares have areas of $81\\text{ cm}^2$ and $144\\text{ cm}^2$. If they are combined into a single square, what is the side length of the new square?",
        "options": ["12 cm", "15 cm", "17 cm", "225 cm"],
        "correct": 1,
        "solution": "Combined area $= 81 + 144 = 225\\text{ cm}^2$.\\n$$\\text{Side length} = \\sqrt{225} = \\mathbf{15\\text{ cm}}$$\\n\\nNotice the original sides were $9\\text{ cm}$ and $12\\text{ cm}$, forming the right triangle $(9, 12, 15)$."
    },
    {
        "num": 12,
        "slide": 18,
        "question": "A $20\\text{ m}$ long wire is tied from the top of an electric pole to a ground stake $12\\text{ m}$ away from the pole's base. What is the height of the pole?",
        "options": ["14 m", "15 m", "16 m", "18 m"],
        "correct": 2,
        "solution": "Using $h = \\sqrt{c^2 - b^2}$:\\n$$h = \\sqrt{20^2 - 12^2} = \\sqrt{400 - 144} = \\sqrt{256} = \\mathbf{16\\text{ m}}$$\\n\\nThis is a scaling of $(3, 4, 5)$ by $4$ ($12, 16, 20$)."
    },
    {
        "num": 13,
        "slide": 18,
        "question": "A tree breaks at a height of $5\\text{ m}$ from the ground. Its broken top touches the ground at a distance of $12\\text{ m}$ from the foot of the tree. What was the total original height of the tree?",
        "options": ["13 m", "17 m", "18 m", "20 m"],
        "correct": 2,
        "solution": "Step 1: Compute length of broken fallen section (hypotenuse):\\n$$c = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ m}$$\\nStep 2: Add upright trunk height ($5\\text{ m}$):\\n$$\\text{Original Height} = 5 + 13 = \\mathbf{18\\text{ m}}$$"
    },
    {
        "num": 14,
        "slide": 18,
        "question": "A person walks $8\\text{ km}$ due East and then $6\\text{ km}$ due North. How far are they from their starting point?",
        "options": ["10 km", "12 km", "14 km", "16 km"],
        "correct": 0,
        "solution": "East and North form a perpendicular angle of $90^\\circ$.\\n$$\\text{Displacement} = \\sqrt{8^2 + 6^2} = \\sqrt{64 + 36} = \\sqrt{100} = \\mathbf{10\\text{ km}}$$"
    },
    {
        "num": 15,
        "slide": 18,
        "question": "In the four-triangle dissection proof of $a^2 + b^2 = c^2$, if $a = 5$ and $b = 12$, what is the area of the inner tilted square?",
        "options": ["120", "144", "169", "289"],
        "correct": 2,
        "solution": "The side of the inner tilted square is the hypotenuse $c$:\\n$$c = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = 13$$\\n$$\\text{Inner Square Area} = c^2 = 13^2 = \\mathbf{169}$$"
    },
    {
        "num": 16,
        "slide": 18,
        "question": "A rectangular television screen has a width of $32\\text{ inches}$ and a height of $24\\text{ inches}$. What is the advertised diagonal size of the screen?",
        "options": ["36 inches", "40 inches", "42 inches", "48 inches"],
        "correct": 1,
        "solution": "$$\\text{Diagonal} = \\sqrt{32^2 + 24^2} = \\sqrt{1024 + 576} = \\sqrt{1600} = \\mathbf{40\\text{ inches}}$$\\n\\nNotice: $24 = 3 \\times 8$, $32 = 4 \\times 8$, so diagonal $= 5 \\times 8 = 40\\text{ inches}$."
    },
    {
        "num": 17,
        "slide": 18,
        "question": "If two squares of sides $s_1 = 4\\text{ cm}$ and $s_2 = 7\\text{ cm}$ are cut and rearranged into a single square, what is the exact area of the resulting square?",
        "options": ["53 cm²", "65 cm²", "72 cm²", "121 cm²"],
        "correct": 1,
        "solution": "By conservation of area in paper cutting and rearrangement:\\n$$\\text{Total Area} = s_1^2 + s_2^2 = 4^2 + 7^2 = 16 + 49 = \\mathbf{65\\text{ cm}^2}$$"
    },
    {
        "num": 18,
        "slide": 18,
        "question": "A ladder $17\\text{ m}$ long reaches a wall height of $15\\text{ m}$. If the foot of the ladder is pulled $7\\text{ m}$ further away from the wall, how far does the top slide down?",
        "options": ["3 m", "5 m", "7 m", "9 m"],
        "correct": 2,
        "solution": "Initial distance from wall:\\n$$d_1 = \\sqrt{17^2 - 15^2} = \\sqrt{289 - 225} = \\sqrt{64} = 8\\text{ m}$$\\nWhen pulled $7\\text{ m}$ further, new distance $= 8 + 7 = 15\\text{ m}$.\\nNew height on wall:\\n$$h_2 = \\sqrt{17^2 - 15^2} = \\sqrt{64} = 8\\text{ m}$$\\nSlide distance $= 15 - 8 = \\mathbf{7\\text{ m}}$."
    },
    {
        "num": 19,
        "slide": 18,
        "question": "An equilateral triangle has sides of length $10\\text{ cm}$. What is the length of its altitude?",
        "options": ["5 cm", "5√2 cm", "5√3 cm", "10√3 cm"],
        "correct": 2,
        "solution": "The altitude drops perpendicularly to the midpoint of the base (half-base $= 5\\text{ cm}$):\\n$$h = \\sqrt{10^2 - 5^2} = \\sqrt{100 - 25} = \\sqrt{75} = \\sqrt{25 \\times 3} = \\mathbf{5\\sqrt{3}\\text{ cm}}$$"
    },
    {
        "num": 20,
        "slide": 18,
        "question": "A rectangular door frame is $2.1\\text{ m}$ high and $0.9\\text{ m}$ wide. What is the maximum width of a circular table top that can fit through the door?",
        "options": ["2.1 m", "2.28 m", "2.5 m", "3.0 m"],
        "correct": 1,
        "solution": "The maximum dimension through which the circular disc can pass tilted is the door's diagonal:\\n$$d = \\sqrt{2.1^2 + 0.9^2} = \\sqrt{4.41 + 0.81} = \\sqrt{5.22} \\approx \\mathbf{2.28\\text{ m}}$$"
    },

    # Slide 19: Questions 21 to 30
    {
        "num": 21,
        "slide": 19,
        "question": "Which of the following is NOT a primitive Pythagorean Triple?",
        "options": ["(3, 4, 5)", "(5, 12, 13)", "(6, 8, 10)", "(8, 15, 17)"],
        "correct": 2,
        "solution": "$(6, 8, 10)$ is **not primitive** because all three terms share a common factor of $2$ ($\\gcd(6, 8, 10) = 2$). Its primitive generator is $(3, 4, 5)$."
    },
    {
        "num": 22,
        "slide": 19,
        "question": "Using the parametric generator $a = m^2 - n^2, b = 2mn, c = m^2 + n^2$, find the triple generated by $m = 4$ and $n = 1$.",
        "options": ["(15, 8, 17)", "(7, 24, 25)", "(9, 40, 41)", "(12, 16, 20)"],
        "correct": 0,
        "solution": "$$a = 4^2 - 1^2 = 16 - 1 = 15$$\\n$$b = 2(4)(1) = 8$$\\n$$c = 4^2 + 1^2 = 16 + 1 = 17$$\\n\\nThus, the triple is $\\mathbf{(15, 8, 17)}$ (or $(8, 15, 17)$)."
    },
    {
        "num": 23,
        "slide": 19,
        "question": "What is the length of the 3D interior space diagonal of a room measuring $8\\text{ m} \\times 6\\text{ m} \\times 24\\text{ m}$?",
        "options": ["25 m", "26 m", "28 m", "30 m"],
        "correct": 1,
        "solution": "Using $D = \\sqrt{l^2 + w^2 + h^2}$:\\n$$D = \\sqrt{8^2 + 6^2 + 24^2} = \\sqrt{64 + 36 + 576} = \\sqrt{100 + 576} = \\sqrt{676} = \\mathbf{26\\text{ m}}$$"
    },
    {
        "num": 24,
        "slide": 19,
        "question": "In the smallest Euler Brick discovered by Paul Halcke (44, 117, 240), which of the following is NOT one of the three face diagonals?",
        "options": ["125", "244", "267", "280"],
        "correct": 3,
        "solution": "Face diagonals of Halcke's brick:\\n1. $d_1 = \\sqrt{44^2 + 117^2} = \\sqrt{1936 + 13689} = \\sqrt{15625} = 125$\\n2. $d_2 = \\sqrt{44^2 + 240^2} = \\sqrt{1936 + 57600} = \\sqrt{59536} = 244$\\n3. $d_3 = \\sqrt{117^2 + 240^2} = \\sqrt{13689 + 57600} = \\sqrt{71289} = 267$\\n\\nTherefore, $\\mathbf{280}$ is not a face diagonal."
    },
    {
        "num": 25,
        "slide": 19,
        "question": "What is the distance of a chord of length $16\\text{ cm}$ from the center of a circle with radius $10\\text{ cm}$?",
        "options": ["5 cm", "6 cm", "8 cm", "9 cm"],
        "correct": 1,
        "solution": "The perpendicular from the center bisects the chord into two $8\\text{ cm}$ halves.\\n\\nUsing the right triangle formed by radius $R$, half-chord $L/2$, and distance $d$:\\n$$d = \\sqrt{R^2 - (L/2)^2} = \\sqrt{10^2 - 8^2} = \\sqrt{100 - 64} = \\sqrt{36} = \\mathbf{6\\text{ cm}}$$"
    },
    {
        "num": 26,
        "slide": 19,
        "question": "Find the perimeter of a rhombus whose diagonals measure $16\\text{ cm}$ and $12\\text{ cm}$.",
        "options": ["32 cm", "40 cm", "48 cm", "56 cm"],
        "correct": 1,
        "solution": "Diagonals of a rhombus bisect each other at right angles ($90^\\circ$).\\nHalf-diagonals are $8\\text{ cm}$ and $6\\text{ cm}$.\\n\\nEach side $s$ of the rhombus is:\\n$$s = \\sqrt{8^2 + 6^2} = \\sqrt{64 + 36} = \\sqrt{100} = 10\\text{ cm}$$\\n$$\\text{Perimeter} = 4s = 4 \\times 10 = \\mathbf{40\\text{ cm}}$$"
    },
    {
        "num": 27,
        "slide": 19,
        "question": "What is the distance between the coordinate points $P(-3, 2)$ and $Q(5, -4)$?",
        "options": ["8", "10", "12", "14"],
        "correct": 1,
        "solution": "$$\\Delta x = 5 - (-3) = 8, \\quad \\Delta y = -4 - 2 = -6$$\\n$$d = \\sqrt{8^2 + (-6)^2} = \\sqrt{64 + 36} = \\sqrt{100} = \\mathbf{10}$$"
    },
    {
        "num": 28,
        "slide": 19,
        "question": "In a right triangle, the hypotenuse is $41\\text{ cm}$ and one leg is $9\\text{ cm}$. What is the area of the triangle?",
        "options": ["180 cm²", "360 cm²", "400 cm²", "720 cm²"],
        "correct": 0,
        "solution": "Find the second leg:\\n$$b = \\sqrt{41^2 - 9^2} = \\sqrt{(41-9)(41+9)} = \\sqrt{32 \\times 50} = \\sqrt{1600} = 40\\text{ cm}$$\\n$$\\text{Area} = \\frac{1}{2} \\times a \\times b = \\frac{1}{2} \\times 9 \\times 40 = \\mathbf{180\\text{ cm}^2}$$"
    },
    {
        "num": 29,
        "slide": 19,
        "question": "If a cube has a space diagonal of $6\\sqrt{3}\\text{ cm}$, what is its total surface area?",
        "options": ["144 cm²", "180 cm²", "216 cm²", "256 cm²"],
        "correct": 2,
        "solution": "For a cube of side $a$, the 3D space diagonal is $D = a\\sqrt{3}$.\\n$$a\\sqrt{3} = 6\\sqrt{3} \\implies a = 6\\text{ cm}$$\\n$$\\text{Total Surface Area} = 6a^2 = 6(6^2) = 6 \\times 36 = \\mathbf{216\\text{ cm}^2}$$"
    },
    {
        "num": 30,
        "slide": 19,
        "question": "Which mathematician formulated the famous conjecture that $a^n + b^n = c^n$ has no positive integer solutions for $n > 2$?",
        "options": ["Euclid", "Pierre de Fermat", "Leonhard Euler", "Baudhāyana"],
        "correct": 1,
        "solution": "**Pierre de Fermat** in 1637 proposed Fermat's Last Theorem, noting that while squares ($n=2$) have infinitely many integer solutions (Pythagorean triples), cubes and higher powers ($n \\ge 3$) have none."
    },

    # Slide 20: Questions 31 to 40
    {
        "num": 31,
        "slide": 20,
        "question": "A triangle has side lengths $8\\text{ cm}$, $15\\text{ cm}$, and $17\\text{ cm}$. Which of the following is true?",
        "options": [
            "It is acute-angled",
            "It is obtuse-angled",
            "It is right-angled opposite the 17 cm side",
            "It is not a valid triangle"
        ],
        "correct": 2,
        "solution": "$$8^2 + 15^2 = 64 + 225 = 289 = 17^2$$\\nBy the converse of Baudhāyana's theorem, the triangle is strictly **right-angled opposite the 17 cm hypotenuse**."
    },
    {
        "num": 32,
        "slide": 20,
        "question": "A triangle has sides $4, 6, 8$. Classify the triangle by angle.",
        "options": ["Right-angled", "Acute-angled", "Obtuse-angled", "Degenerate"],
        "correct": 2,
        "solution": "Check triangle inequality: $4 + 6 = 10 > 8$ (valid triangle).\\nCompare $a^2 + b^2$ with $c^2$:\\n$$4^2 + 6^2 = 16 + 36 = 52$$\\n$$8^2 = 64$$\\nSince $52 < 64$ ($a^2 + b^2 < c^2$), the triangle is **obtuse-angled**."
    },
    {
        "num": 33,
        "slide": 20,
        "question": "A triangle has sides $5, 6, 7$. Classify the triangle by angle.",
        "options": ["Right-angled", "Acute-angled", "Obtuse-angled", "Equilateral"],
        "correct": 1,
        "solution": "$$5^2 + 6^2 = 25 + 36 = 61$$\\n$$7^2 = 49$$\\nSince $61 > 49$ ($a^2 + b^2 > c^2$), the triangle is **acute-angled** (all angles $< 90^\\circ$)."
    },
    {
        "num": 34,
        "slide": 20,
        "question": "In the puzzle 'Find the Colours', what is the straight-line distance between two grid points separated by a knight's move (2 units horizontally, 1 unit vertically)?",
        "options": ["2", "3", "√5", "5"],
        "correct": 2,
        "solution": "By Baudhāyana's theorem:\\n$$d = \\sqrt{2^2 + 1^2} = \\sqrt{4 + 1} = \\mathbf{\\sqrt{5}}$$"
    },
    {
        "num": 35,
        "slide": 20,
        "question": "What is the radius of the incircle (inradius $r$) of a right triangle with legs $a = 6$ and $b = 8$ and hypotenuse $c = 10$?",
        "options": ["2 cm", "3 cm", "4 cm", "5 cm"],
        "correct": 0,
        "solution": "For any right triangle, the inradius formula is:\\n$$r = \\frac{a + b - c}{2} = \\frac{6 + 8 - 10}{2} = \\frac{4}{2} = \\mathbf{2\\text{ cm}}$$"
    },
    {
        "num": 36,
        "slide": 20,
        "question": "What is the radius of the circumcircle (circumradius $R$) of a right triangle with hypotenuse $c = 18\\text{ cm}$?",
        "options": ["6 cm", "9 cm", "12 cm", "18 cm"],
        "correct": 1,
        "solution": "The midpoint of the hypotenuse of any right triangle is its circumcenter (Thales' theorem).\\n$$R = \\frac{c}{2} = \\frac{18}{2} = \\mathbf{9\\text{ cm}}$$"
    },
    {
        "num": 37,
        "slide": 20,
        "question": "An isosceles triangle has base $16\\text{ cm}$ and equal sides $17\\text{ cm}$. Find its area.",
        "options": ["120 cm²", "136 cm²", "240 cm²", "272 cm²"],
        "correct": 0,
        "solution": "The altitude bisects the base into two $8\\text{ cm}$ segments.\\n$$h = \\sqrt{17^2 - 8^2} = \\sqrt{289 - 64} = \\sqrt{225} = 15\\text{ cm}$$\\n$$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times h = \\frac{1}{2} \\times 16 \\times 15 = 8 \\times 15 = \\mathbf{120\\text{ cm}^2}$$"
    },
    {
        "num": 38,
        "slide": 20,
        "question": "How did ancient Vedic altar builders ensure that ropes did not stretch and distort right-angle constructions?",
        "options": [
            "They used woven cords of specific grasses (Mūñja or Kuśa) treated with natural oils",
            "They only built altars indoors",
            "They used steel wire cables",
            "They never measured angles"
        ],
        "correct": 0,
        "solution": "The Śulbasūtras specify making measuring cords from seasoned **Mūñja or Kuśa grass fibers** woven tightly and treated against thermal stretching."
    },
    {
        "num": 39,
        "slide": 20,
        "question": "If a right-angled triangle has area $30\\text{ cm}^2$ and perimeter $30\\text{ cm}$, what is the length of its hypotenuse?",
        "options": ["12 cm", "13 cm", "14 cm", "15 cm"],
        "correct": 1,
        "solution": "We know $a + b + c = 30$ and $\\frac{1}{2}ab = 30 \\implies ab = 60$.\\nSince $a + b = 30 - c$, square both sides:\\n$$(a + b)^2 = (30 - c)^2$$\\n$$a^2 + 2ab + b^2 = 900 - 60c + c^2$$\\nSince $a^2 + b^2 = c^2$:\\n$$c^2 + 2(60) = 900 - 60c + c^2$$\\n$$120 = 900 - 60c \\implies 60c = 780 \\implies c = \\mathbf{13\\text{ cm}}$$"
    },
    {
        "num": 40,
        "slide": 20,
        "question": "In the puzzle 'Find the Colours', why is it impossible to colour an integer grid with only 2 colours such that no two points at distance √5 have the same colour?",
        "options": [
            "Because there exist closed odd-length cycles of knight moves (e.g. triangles or 5-cycles)",
            "Because √5 is irrational",
            "Because 2 is an even number",
            "Because squares have 4 corners"
        ],
        "correct": 0,
        "solution": "Graph theory proves that a graph is $2$-colourable (bipartite) if and only if it contains **no odd cycles**. Points at distance $\\sqrt{5}$ form pentagons and odd cycles, making $2$-colouring mathematically impossible."
    }
]

with open('.agents/class8_math_baudhayana_pythagoras_data.py', 'w', encoding='utf-8') as f:
    f.write("# Data for Class 8 Mathematics Chapter 9: The Baudhāyana-Pythagoras Theorem Lab\n\n")
    f.write("slides_data = " + json.dumps(slides, indent=4, ensure_ascii=False) + "\n\n")
    f.write("quiz_questions = " + json.dumps(questions, indent=4, ensure_ascii=False) + "\n")

print("Generated .agents/class8_math_baudhayana_pythagoras_data.py successfully!")

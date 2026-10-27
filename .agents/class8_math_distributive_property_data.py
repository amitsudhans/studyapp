# Class 8 Mathematics Chapter 6: We Distribute, Yet Things Multiply - Master Curriculum Data
# NCERT Class 8 Mathematics Syllabus

slides_data = [
    # Slide 1: 6.1 Some Properties of Multiplication & The Distributive Law
    {
        "id": 1,
        "title": "6.1 The Distributive Property: Multiplication Over Addition",
        "subtitle": "Geometric Area Model, Partitioned Rectangles & Fundamental Distributive Law",
        "content": """
<p class="lead">The <strong>Distributive Property of Multiplication over Addition</strong> is one of the most powerful and unifying principles in all of mathematics. It connects addition and multiplication through geometry.</p>

<div class="theory-box">
  <h4>Formal Statement of the Distributive Law</h4>
  <p>For any real numbers or algebraic variables $a, b,$ and $c$:</p>
  $$a(b + c) = ab + ac$$
  <p>Similarly, for subtraction:</p>
  $$a(b - c) = ab - ac$$
  <p>The factor $a$ outside the parentheses distributes to <em>every single term</em> inside the parentheses.</p>
</div>

<div class="formula-box">
  <h4>The Geometric Area Model Proof</h4>
  <p>Consider a large rectangle of height $a$ and total width $(b + c)$:</p>
  <ul>
    <li>The total area of the undivided rectangle is: $\\text{Area} = \\text{height} \\times \\text{width} = a(b + c)$.</li>
    <li>Now slice the rectangle vertically into two smaller side-by-side rectangles:
      <br>• Left rectangle has dimensions $a \\times b$, with area $ab$.
      <br>• Right rectangle has dimensions $a \\times c$, with area $ac$.
    </li>
  </ul>
  <p>Because the whole area is the sum of its parts:</p>
  $$a(b + c) = ab + ac$$
</div>

<div class="theory-box">
  <h4>Why It Matters</h4>
  <p>The distributive property allows us to break down daunting multi-digit calculations into easy mental steps and forms the cornerstone of polynomial algebra.</p>
</div>
""",
        "sim_type": "distributive_rectangle_area_splitter",
        "voice": "Welcome to Chapter 6: We Distribute, Yet Things Multiply! We begin with the distributive property. Multiplying a number a by the sum b plus c equals ab plus ac. Geometrically, if a rectangle of height a has its base divided into two parts b and c, its total area is the sum of the two smaller rectangles, ab plus ac.",
        "checkpoints": [
            {
                "question": "Which algebraic expression illustrates the Distributive Property of multiplication over addition?",
                "options": [
                    "a(b + c) = ab + ac",
                    "a + (b + c) = (a + b) + c",
                    "a × b = b × a",
                    "a(bc) = (ab)c"
                ],
                "correct": 0,
                "explanation": "$a(b + c) = ab + ac$ represents the Distributive Property. (The others represent associative and commutative properties)."
            },
            {
                "question": "If a rectangle has height 6 cm and width (10 + 4) cm, what is its total area calculated by the distributive property?",
                "options": ["60 cm²", "24 cm²", "84 cm²", "96 cm²"],
                "correct": 2,
                "explanation": "Using $a(b + c) = ab + ac$: $6 \\times (10 + 4) = 6 \\times 10 + 6 \\times 4 = 60 + 24 = 84\\text{ cm}^2$."
            }
        ]
    },

    # Slide 2: Increments in Products
    {
        "id": 2,
        "title": "Increments in Products: Growth When Factors Change",
        "subtitle": "Marginal Growth, The (a + 1)(b + 1) Expansion & Cross-Strips",
        "content": """
<p class="lead">When the dimensions of a rectangle are each increased by 1, how much does the product actually grow? The answer is far more than just 1!</p>

<div class="theory-box">
  <h4>The Unit Increment Formula</h4>
  <p>Consider two numbers $a$ and $b$ whose product is $ab$. If both are increased by 1:</p>
  $$(a + 1)(b + 1) = a(b + 1) + 1(b + 1) = ab + a + b + 1$$
  <p>The new product exceeds the original product $ab$ by exactly:</p>
  $$\\Delta \\text{Product} = (a + 1)(b + 1) - ab = a + b + 1$$
</div>

<div class="formula-box">
  <h4>Geometric Decomposition of the Growth</h4>
  <p>In terms of geometric area, increasing a rectangle of $a \\times b$ by 1 unit in both directions adds three distinct regions:</p>
  <ol>
    <li>A horizontal strip of area $1 \\times a = a$.</li>
    <li>A vertical strip of area $b \\times 1 = b$.</li>
    <li>A small corner square of area $1 \\times 1 = 1$.</li>
  </ol>
  <p>Example: If $a = 10$ and $b = 7$, $ab = 70$. The new product is $11 \\times 8 = 88$. The growth is $10 + 7 + 1 = 18$, and $70 + 18 = 88$!</p>
</div>

<div class="theory-box">
  <h4>General Increment Theorem</h4>
  <p>For arbitrary increases $\\Delta a$ and $\\Delta b$:</p>
  $$(a + \\Delta a)(b + \\Delta b) = ab + b\\Delta a + a\\Delta b + \\Delta a\\Delta b$$
</div>
""",
        "sim_type": "product_increment_visualizer",
        "voice": "What happens when factors grow? If we increase both dimensions a and b of a rectangle by 1, the new product is a plus 1 times b plus 1. Expanding this gives ab plus a plus b plus 1. The product increases by the sum of the two dimensions plus 1, which represents two edge strips and one tiny corner square.",
        "checkpoints": [
            {
                "question": "If a = 8 and b = 5, by how much does the product (a + 1)(b + 1) exceed the original product (ab)?",
                "options": ["1", "13", "14", "40"],
                "correct": 2,
                "explanation": "Growth is $a + b + 1 = 8 + 5 + 1 = 14$. Original product was $8 \\times 5 = 40$; new product is $9 \\times 6 = 54$; difference is $54 - 40 = 14$."
            },
            {
                "question": "Which algebraic expression represents the exact difference (a + 2)(b + 2) - ab?",
                "options": ["2a + 2b + 2", "2a + 2b + 4", "4a + 4b + 4", "a + b + 4"],
                "correct": 1,
                "explanation": "$(a + 2)(b + 2) = ab + 2a + 2b + 4$. Subtracting $ab$ leaves $2a + 2b + 4$."
            }
        ]
    },

    # Slide 3: Fast Multiplications Using the Distributive Property
    {
        "id": 3,
        "title": "Fast Mental Multiplications Using Distribution",
        "subtitle": "Base-Ten Decompositions, Subtractive Splits & Lightning Mental Math",
        "content": """
<p class="lead">By strategically splitting numbers into round bases (like 10, 50, 100, or 1000), the distributive property turns complex paper-and-pencil multiplication into instant mental math.</p>

<div class="formula-box">
  <h4>Technique 1: Decomposing with Subtraction (Numbers Ending in 8 or 9)</h4>
  <p>Instead of multiplying by 99 or 48, rewrite them as differences from friendly round numbers:</p>
  <ul>
    <li><strong>Multiply $43 \\times 99$:</strong>
      $$43 \\times (100 - 1) = 43 \\times 100 - 43 \\times 1 = 4300 - 43 = 4257$$
    </li>
    <li><strong>Multiply $25 \\times 48$:</strong>
      $$25 \\times (50 - 2) = 25 \\times 50 - 25 \\times 2 = 1250 - 50 = 1200$$
    </li>
  </ul>
</div>

<div class="formula-box">
  <h4>Technique 2: Decomposing with Addition (Numbers Just Over a Base)</h4>
  <p>For numbers slightly exceeding a round base:</p>
  <ul>
    <li><strong>Multiply $32 \\times 105$:</strong>
      $$32 \\times (100 + 5) = 32 \\times 100 + 32 \\times 5 = 3200 + 160 = 3360$$
    </li>
    <li><strong>Multiply $18 \\times 52$:</strong>
      $$18 \\times (50 + 2) = 18 \\times 50 + 18 \\times 2 = 900 + 36 = 936$$
    </li>
  </ul>
</div>

<div class="theory-box">
  <h4>Golden Mental Math Rule</h4>
  <p>Always identify the closest \"friendly number\" (multiple of 10 or 100) and distribute across the small adjustment.</p>
</div>
""",
        "sim_type": "mental_math_distributive_speed_lab",
        "voice": "The distributive property makes mental multiplication lightning fast. Instead of multiplying 43 by 99, think of 99 as 100 minus 1. Then 43 times 100 is 4300, minus 43 gives 4257. Similarly, for 105 times 32, use 100 plus 5 to get 3200 plus 160, equaling 3360.",
        "checkpoints": [
            {
                "question": "What is the fastest way to calculate 56 × 98 using the distributive property?",
                "options": [
                    "56 × (100 - 2) = 5600 - 112 = 5488",
                    "56 × (90 + 8) = 5040 + 448 = 5488",
                    "(50 + 6) × 98 = 4900 + 588 = 5488",
                    "(60 - 4) × 98 = 5880 - 392 = 5488"
                ],
                "correct": 0,
                "explanation": "Rewriting 98 as $(100 - 2)$ requires only multiplying by 100 and 2: $5600 - 112 = 5488$."
            },
            {
                "question": "Evaluate 104 × 25 using distribution over addition:",
                "options": ["2500", "2600", "2700", "2800"],
                "correct": 1,
                "explanation": "$25 \\times (100 + 4) = 25 \\times 100 + 25 \\times 4 = 2500 + 100 = 2600$."
            }
        ]
    },

    # Slide 4: Double Distribution: Product of Two Binomials
    {
        "id": 4,
        "title": "Double Distribution: Product of Two Binomials",
        "subtitle": "The 4-Quadrant Area Grid, FOIL Expansion & Polynomial Geometry",
        "content": """
<p class="lead">When multiplying two expressions that each contain two terms (binomials), distribution happens <em>twice</em>. This creates a 4-part product.</p>

<div class="formula-box">
  <h4>The Double Distributive Law</h4>
  <p>To multiply $(a + b)(c + d)$, treat the entire second binomial $(c + d)$ as a single package and distribute both $a$ and $b$ across it:</p>
  $$(a + b)(c + d) = a(c + d) + b(c + d)$$
  <p>Now distribute $a$ and $b$ individually:</p>
  $$= ac + ad + bc + bd$$
</div>

<div class="theory-box">
  <h4>The 4-Quadrant Rectangle Model</h4>
  <p>Imagine a rectangle divided horizontally into lengths $a$ and $b$, and vertically into widths $c$ and $d$. The rectangle splits into 4 distinct compartments:</p>
  <ul>
    <li>Top-Left quadrant: Area $a \\times c = ac$</li>
    <li>Top-Right quadrant: Area $a \\times d = ad$</li>
    <li>Bottom-Left quadrant: Area $b \\times c = bc$</li>
    <li>Bottom-Right quadrant: Area $b \\times d = bd$</li>
  </ul>
  <p>Summing the 4 quadrants yields the total area: $ac + ad + bc + bd$.</p>
</div>

<div class="formula-box">
  <h4>Example: $(x + 3)(x + 5)$</h4>
  $$(x + 3)(x + 5) = x(x + 5) + 3(x + 5) = x^2 + 5x + 3x + 15 = x^2 + 8x + 15$$
</div>
""",
        "sim_type": "four_quadrant_binomial_grid",
        "voice": "When multiplying two binomials, we perform double distribution. The product a plus b times c plus d equals ac plus ad plus bc plus bd. Geometrically, this divides a large rectangle into four quadrants. Adding the areas of all four quadrants yields the complete algebraic expansion.",
        "checkpoints": [
            {
                "question": "Expand (x + 4)(x + 7):",
                "options": [
                    "x² + 28",
                    "x² + 11x + 28",
                    "x² + 28x + 11",
                    "2x + 11"
                ],
                "correct": 1,
                "explanation": "$(x + 4)(x + 7) = x(x + 7) + 4(x + 7) = x^2 + 7x + 4x + 28 = x^2 + 11x + 28$."
            },
            {
                "question": "How many separate product terms are initially produced when multiplying (a + b)(c + d) before combining like terms?",
                "options": ["2", "3", "4", "6"],
                "correct": 2,
                "explanation": "Double distribution produces exactly 4 terms: $ac, ad, bc,$ and $bd$."
            }
        ]
    },

    # Slide 5: 6.2 Special Cases: Square of the Sum (a + b)²
    {
        "id": 5,
        "title": "6.2 Special Cases: Square of the Sum (a + b)²",
        "subtitle": "The Dissection Proof, The 2ab Cross-Term & The Universal Identity",
        "content": """
<p class="lead">What is $(a + b)^2$? It is the area of a square of side length $(a + b)$. Expanding this algebraically and geometrically reveals the famous <strong>first algebraic identity</strong>.</p>

<div class="formula-box">
  <h4>Algebraic Derivation of Identity I</h4>
  <p>Apply double distribution to $(a + b)(a + b)$:</p>
  $$(a + b)^2 = (a + b)(a + b) = a(a + b) + b(a + b)$$
  $$= a^2 + ab + ba + b^2$$
  <p>Since multiplication is commutative ($ba = ab$), we combine the two middle terms:</p>
  $$(a + b)^2 = a^2 + 2ab + b^2$$
</div>

<div class="theory-box">
  <h4>The Geometric Dissection of a Square</h4>
  <p>A square of side $(a + b)$ naturally partitions into <strong>4 regions</strong>:</p>
  <ul>
    <li>One square of area $a^2$ in the upper-left.</li>
    <li>One square of area $b^2$ in the lower-right.</li>
    <li>Two identical rectangular strips of area $ab$, one top-right and one bottom-left.</li>
  </ul>
  <p>Summing these 4 regions: $\\text{Total Area} = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$.</p>
</div>

<div class="formula-box">
  <h4>Warning: The Classic Student Trap!</h4>
  <p><strong>NEVER</strong> write $(a + b)^2 = a^2 + b^2$! Doing so completely forgets the two rectangular strips of area $2ab$. (For example: $(3 + 4)^2 = 7^2 = 49$, but $3^2 + 4^2 = 9 + 16 = 25 \\neq 49$!).</p>
</div>
""",
        "sim_type": "square_of_sum_geometric_prover",
        "voice": "Section 6.2 explores special cases of the distributive property, starting with the square of a sum, a plus b squared. When we expand a plus b times a plus b, we get a squared plus 2ab plus b squared. The area divides into two squares, a squared and b squared, plus two identical rectangular strips of area ab. Never forget the 2ab term!",
        "checkpoints": [
            {
                "question": "What is the expansion of (2x + 3y)²?",
                "options": [
                    "4x² + 9y²",
                    "4x² + 6xy + 9y²",
                    "4x² + 12xy + 9y²",
                    "2x² + 12xy + 3y²"
                ],
                "correct": 2,
                "explanation": "$(2x + 3y)^2 = (2x)^2 + 2(2x)(3y) + (3y)^2 = 4x^2 + 12xy + 9y^2$."
            },
            {
                "question": "If a = 30 and b = 2, calculate 32² using the identity (a + b)² = a² + 2ab + b²:",
                "options": ["904", "964", "1024", "1044"],
                "correct": 2,
                "explanation": "$32^2 = (30 + 2)^2 = 30^2 + 2(30)(2) + 2^2 = 900 + 120 + 4 = 1024$."
            }
        ]
    },

    # Slide 6: Square of the Difference (a - b)²
    {
        "id": 6,
        "title": "Square of the Difference (a - b)²: Subtractive Geometry",
        "subtitle": "Double Subtraction, The Restored Corner & Identity II Derivation",
        "content": """
<p class="lead">What happens when we square a difference, $(a - b)^2$? The expansion mirrors $(a + b)^2$, but with a negative cross-term.</p>

<div class="formula-box">
  <h4>Algebraic Derivation of Identity II</h4>
  <p>Write $(a - b)^2$ as the product of two binomials:</p>
  $$(a - b)^2 = (a - b)(a - b) = a(a - b) - b(a - b)$$
  $$= a^2 - ab - ba + b^2$$
  <p>Since $-ba = -ab$, combining like terms yields:</p>
  $$(a - b)^2 = a^2 - 2ab + b^2$$
</div>

<div class="theory-box">
  <h4>Why is the Last Term $+b^2$ and NOT $-b^2$?</h4>
  <p>By the fundamental rule of signs, multiplying two negative numbers always yields a positive number:</p>
  $$(-b) \\times (-b) = +b^2$$
  <p>Geometrically, when we cut away two strips of area $ab$ from the large square $a^2$, the corner of size $b \\times b$ is <strong>subtracted twice</strong>! To compensate, we must <strong>add back</strong> $+b^2$.</p>
</div>

<div class="formula-box">
  <h4>Mental Math Application: $99^2$</h4>
  $$99^2 = (100 - 1)^2 = 100^2 - 2(100)(1) + 1^2 = 10000 - 200 + 1 = 9801$$
</div>
""",
        "sim_type": "square_of_difference_overlap_lab",
        "voice": "Now let us examine the square of a difference, a minus b squared. Expanding gives a squared minus 2ab plus b squared. Notice that the last term is positive b squared because negative b times negative b is positive. Geometrically, subtracting two strips of area ab removes the corner square twice, so we add back b squared to restore it.",
        "checkpoints": [
            {
                "question": "Expand (3x - 5)²:",
                "options": [
                    "9x² - 25",
                    "9x² - 15x + 25",
                    "9x² - 30x + 25",
                    "9x² + 30x - 25"
                ],
                "correct": 2,
                "explanation": "$(3x - 5)^2 = (3x)^2 - 2(3x)(5) + 5^2 = 9x^2 - 30x + 25$."
            },
            {
                "question": "Evaluate 49² using the identity (a - b)² = a² - 2ab + b²:",
                "options": ["2401", "2499", "2501", "2399"],
                "correct": 0,
                "explanation": "$49^2 = (50 - 1)^2 = 50^2 - 2(50)(1) + 1^2 = 2500 - 100 + 1 = 2401$."
            }
        ]
    },

    # Slide 7: Difference of Two Squares: (a + b)(a - b) = a² - b²
    {
        "id": 7,
        "title": "Difference of Two Squares: (a + b)(a - b) = a² - b²",
        "subtitle": "Cancellation of Cross-Terms, Reshaping L-Shapes & Lightning Products",
        "content": """
<p class="lead">What happens when you multiply the sum of two numbers by their difference? The two cross-terms have opposite signs and cancel each other out completely!</p>

<div class="formula-box">
  <h4>Algebraic Derivation of Identity III</h4>
  <p>Expanding $(a + b)(a - b)$ using double distribution:</p>
  $$(a + b)(a - b) = a(a - b) + b(a - b) = a^2 - ab + ba - b^2$$
  <p>Because $-ab + ba = 0$ (they cancel):</p>
  $$(a + b)(a - b) = a^2 - b^2$$
  <p>This is famously known as the <strong>Difference of Two Squares (DOTS)</strong> identity.</p>
</div>

<div class="theory-box">
  <h4>Geometric Cut-and-Paste Proof</h4>
  <p>Start with a square of area $a^2$ and cut out a smaller corner square of area $b^2$. The remaining figure has area $a^2 - b^2$ and is an L-shaped region.</p>
  <p>Cut this L-shape into two rectangles and rearrange them end-to-end: they form a single long rectangle with length $(a + b)$ and width $(a - b)$! Thus $\\text{Area} = (a + b)(a - b) = a^2 - b^2$.</p>
</div>

<div class="formula-box">
  <h4>Lightning Multiplication Trick</h4>
  <p>Any product of two numbers equidistant from a round number can be calculated instantly:</p>
  $$53 \\times 47 = (50 + 3)(50 - 3) = 50^2 - 3^2 = 2500 - 9 = 2491$$
  $$106 \\times 94 = (100 + 6)(100 - 6) = 100^2 - 6^2 = 10000 - 36 = 9964$$
</div>
""",
        "sim_type": "difference_of_squares_animator",
        "voice": "The difference of two squares identity is one of the most elegant in mathematics. When we multiply a plus b by a minus b, the middle cross terms cancel each other, leaving simply a squared minus b squared. To multiply 53 by 47, we write 50 plus 3 times 50 minus 3, which is 2500 minus 9, giving 2491 in seconds.",
        "checkpoints": [
            {
                "question": "What is the product (7x + 4)(7x - 4)?",
                "options": [
                    "49x² - 16",
                    "49x² + 16",
                    "49x² - 28x - 16",
                    "49x² + 56x - 16"
                ],
                "correct": 0,
                "explanation": "Using $(a + b)(a - b) = a^2 - b^2$: $(7x)^2 - 4^2 = 49x^2 - 16$."
            },
            {
                "question": "Evaluate 82 × 78 in your head using the difference of squares identity:",
                "options": ["6396", "6404", "6384", "6416"],
                "correct": 0,
                "explanation": "$82 \\times 78 = (80 + 2)(80 - 2) = 80^2 - 2^2 = 6400 - 4 = 6396$."
            }
        ]
    },

    # Slide 8: Investigating Pattern 1: Same Tens Digit & Units Adding to 10
    {
        "id": 8,
        "title": "Investigating Pattern 1: Same Tens & Units Adding to 10",
        "subtitle": "The T(T + 1) Rule, Vedic Multiplications & Place-Value Algebraic Proof",
        "content": """
<p class="lead">Observe these remarkable multiplications: $34 \\times 36 = 1224$, $73 \\times 77 = 5621$, $65 \\times 65 = 4225$. What secret rule generates their answers in seconds?</p>

<div class="theory-box">
  <h4>The Two Conditions of Pattern 1</h4>
  <ol>
    <li>Both two-digit numbers share the <strong>exact same tens digit</strong> ($T$).</li>
    <li>Their units digits ($u_1$ and $u_2$) <strong>add up to 10</strong> ($u_1 + u_2 = 10$).</li>
  </ol>
</div>

<div class="formula-box">
  <h4>The Shortcut Rule</h4>
  <ul>
    <li><strong>Left part of answer:</strong> Multiply tens digit by its successor: $T \\times (T + 1)$.</li>
    <li><strong>Right part of answer:</strong> Multiply the units digits: $u_1 \\times u_2$ (written as 2 digits).</li>
  </ul>
  <p>Example: $73 \\times 77$: Left $= 7 \\times 8 = 56$; Right $= 3 \\times 7 = 21$. Combined: <strong>5621</strong>!</p>
  <p>Example: $45 \\times 45$: Left $= 4 \\times 5 = 20$; Right $= 5 \\times 5 = 25$. Combined: <strong>2025</strong>!</p>
</div>

<div class="theory-box">
  <h4>Algebraic Proof Using the Distributive Property</h4>
  <p>Let the numbers be $(10T + u_1)$ and $(10T + u_2)$ where $u_1 + u_2 = 10$:</p>
  $$(10T + u_1)(10T + u_2) = 100T^2 + 10T(u_1 + u_2) + u_1 u_2$$
  <p>Since $u_1 + u_2 = 10$:</p>
  $$= 100T^2 + 10T(10) + u_1 u_2 = 100T^2 + 100T + u_1 u_2$$
  $$= 100T(T + 1) + u_1 u_2$$
  <p>The term $100T(T + 1)$ shifts $T(T+1)$ to the hundreds place, leaving the last two digits for $u_1 u_2$!</p>
</div>
""",
        "sim_type": "vedic_pattern_one_explorer",
        "voice": "Pattern 1 applies to numbers with the same tens digit whose units digits add to 10. To multiply 73 by 77, multiply 7 by the next number 8 to get 56, and multiply 3 by 7 to get 21, giving 5621. Algebraically, expanding 10T plus u1 times 10T plus u2 produces 100 times T times T plus 1, which shifts the product into the hundreds place.",
        "checkpoints": [
            {
                "question": "Using Pattern 1, what is 82 × 88?",
                "options": ["7216", "7224", "6416", "7016"],
                "correct": 0,
                "explanation": "Tens: $8 \\times (8 + 1) = 8 \\times 9 = 72$. Units: $2 \\times 8 = 16$. Result is 7216."
            },
            {
                "question": "Using Pattern 1, what is 91 × 99?",
                "options": ["9090", "9009", "9909", "9019"],
                "correct": 1,
                "explanation": "Tens: $9 \\times 10 = 90$. Units: $1 \\times 9 = 09$ (must be written as 2 digits). Result is 9009."
            }
        ]
    },

    # Slide 9: Pattern 2: Product of Numbers Near 100 (Base Deviations)
    {
        "id": 9,
        "title": "Pattern 2: Product of Numbers Near 100",
        "subtitle": "Base-100 Deviation Algebra, Excesses, Deficits & Cross-Addition",
        "content": """
<p class="lead">When multiplying numbers close to 100, measuring their <strong>deviations</strong> from 100 unlocks an astonishingly rapid mental calculation method.</p>

<div class="theory-box">
  <h4>Case 1: Both Numbers Above 100 (Excesses)</h4>
  <p>Multiply $104 \\times 107$:</p>
  <ul>
    <li>Deviations from 100: $+4$ and $+7$.</li>
    <li><strong>Left part:</strong> Cross-add either number with the other's deviation: $104 + 7 = 111$ (or $107 + 4 = 111$).</li>
    <li><strong>Right part:</strong> Multiply the deviations: $4 \\times 7 = 28$.</li>
    <li>Combined answer: <strong>11,128</strong>!</li>
  </ul>
</div>

<div class="theory-box">
  <h4>Case 2: Both Numbers Below 100 (Deficits)</h4>
  <p>Multiply $96 \\times 94$:</p>
  <ul>
    <li>Deviations from 100: $-4$ and $-6$.</li>
    <li><strong>Left part:</strong> Cross-subtract: $96 - 6 = 90$ (or $94 - 4 = 90$).</li>
    <li><strong>Right part:</strong> Multiply deviations: $(-4) \\times (-6) = +24$.</li>
    <li>Combined answer: <strong>9,024</strong>!</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Algebraic Proof of Base Deviations</h4>
  $$(100 + d_1)(100 + d_2) = 10000 + 100(d_1 + d_2) + d_1 d_2$$
  $$= 100(100 + d_1 + d_2) + d_1 d_2$$
  <p>The term $(100 + d_1 + d_2)$ is precisely our cross-addition sum shifted by 100!</p>
</div>
""",
        "sim_type": "base_hundred_deviation_slider",
        "voice": "Pattern 2 handles numbers near 100 using deviations. For 104 times 107, add 104 plus 7 to get 111, then multiply the deviations 4 times 7 to get 28, producing 11,128. For numbers below 100, such as 96 times 94, cross-subtract to get 90 and multiply negative 4 by negative 6 to get positive 24, giving 9024.",
        "checkpoints": [
            {
                "question": "Using the deviation method, what is 103 × 106?",
                "options": ["10,918", "10,818", "11,018", "10,908"],
                "correct": 0,
                "explanation": "Cross-add: $103 + 6 = 109$. Product of deviations: $3 \\times 6 = 18$. Result: 10,918."
            },
            {
                "question": "Using the deviation method, what is 97 × 95?",
                "options": ["9,215", "9,115", "9,315", "9,225"],
                "correct": 0,
                "explanation": "Deviations: $-3$ and $-5$. Cross-subtract: $97 - 5 = 92$. Multiply deviations: $(-3) \\times (-5) = 15$. Result: 9,215."
            }
        ]
    },

    # Slide 10: Consecutive Product Patterns: n(n + 2) + 1 = (n + 1)²
    {
        "id": 10,
        "title": "Consecutive Product Patterns: n(n + 2) + 1 = (n + 1)²",
        "subtitle": "Completing the Square, Gap Products & Nested Symmetry",
        "content": """
<p class="lead">Multiply any two numbers separated by a gap of 2, and add 1. What happens? You <strong>always get a perfect square</strong>!</p>

<div class="theory-box">
  <h4>Numerical Exploration</h4>
  <ul>
    <li>$3 \\times 5 + 1 = 15 + 1 = 16 = 4^2$</li>
    <li>$5 \\times 7 + 1 = 35 + 1 = 36 = 6^2$</li>
    <li>$9 \\times 11 + 1 = 99 + 1 = 100 = 10^2$</li>
    <li>$19 \\times 21 + 1 = 399 + 1 = 400 = 20^2$</li>
    <li>$99 \\times 101 + 1 = 9999 + 1 = 10000 = 100^2$</li>
  </ul>
</div>

<div class="formula-box">
  <h4>The Algebraic Proof</h4>
  <p>Let the two numbers be $n$ and $n + 2$ (centered around the middle integer $m = n + 1$):</p>
  $$n(n + 2) + 1 = n^2 + 2n + 1$$
  <p>Recognizing Identity I: $n^2 + 2n + 1 = (n + 1)^2$.</p>
  <p>Alternatively, using Difference of Squares with $n = m - 1$ and $n + 2 = m + 1$:</p>
  $$(m - 1)(m + 1) + 1 = (m^2 - 1) + 1 = m^2$$
  <p>The product of two numbers differing by 2 is always <strong>1 less than the square of their average</strong>!</p>
</div>

<div class="theory-box">
  <h4>Generalization for Gap $2k$</h4>
  <p>For any two numbers differing by $2k$: $(m - k)(m + k) + k^2 = m^2$. To make it a square, simply add $k^2$!</p>
</div>
""",
        "sim_type": "consecutive_gap_square_lab",
        "voice": "Here is another beautiful pattern. Take any two numbers with a gap of 2, multiply them, and add 1. You always get the square of the middle number! For example, 19 times 21 is 399, plus 1 is 400, which is 20 squared. Algebraically, n times n plus 2 plus 1 expands to n squared plus 2n plus 1, which factors into n plus 1 squared.",
        "checkpoints": [
            {
                "question": "What is the value of 49 × 51 + 1?",
                "options": ["2400", "2500", "2600", "2501"],
                "correct": 1,
                "explanation": "By the theorem: $(50 - 1)(50 + 1) + 1 = 50^2 - 1 + 1 = 50^2 = 2500$."
            },
            {
                "question": "What number must be added to 38 × 42 to make it a perfect square?",
                "options": ["1", "2", "4", "16"],
                "correct": 2,
                "explanation": "Here numbers are $40 - 2$ and $40 + 2$. $(40 - 2)(40 + 2) = 40^2 - 2^2 = 1600 - 4$. Adding $2^2 = 4$ yields $40^2 = 1600$."
            }
        ]
    },

    # Slide 11: 6.3 Mind the Mistake, Mend the Mistake: Common Algebraic Traps
    {
        "id": 11,
        "title": "6.3 Mind the Mistake, Mend the Mistake",
        "subtitle": "The Freshman's Dream, Sign Distribution Errors & Diagnostic Repairs",
        "content": """
<p class="lead">Algebraic errors frequently occur because of faulty mental generalizations. In section 6.3, we diagnose the most common traps and learn how to <strong>mend the mistake</strong>.</p>

<div class="theory-box">
  <h4>Trap 1: The Freshman's Dream $(a + b)^2 = a^2 + b^2$</h4>
  <ul>
    <li><strong style="color:#f43f5e;">The Mistake:</strong> Writing $(x + 5)^2 = x^2 + 25$.</li>
    <li><strong style="color:#34d399;">Mending the Mistake:</strong> Powers do NOT distribute over addition! You must include the cross-term $2ab$:
      $$(x + 5)^2 = x^2 + 2(x)(5) + 5^2 = x^2 + 10x + 25$$
    </li>
  </ul>
</div>

<div class="theory-box">
  <h4>Trap 2: The Negative Sign Distribution Omission</h4>
  <ul>
    <li><strong style="color:#f43f5e;">The Mistake:</strong> $-(3x - 7) = -3x - 7$.</li>
    <li><strong style="color:#34d399;">Mending the Mistake:</strong> The negative sign is a multiplier of $-1$, which must distribute to <em>every</em> term inside:
      $$-(3x - 7) = -1(3x) + (-1)(-7) = -3x + 7$$
    </li>
  </ul>
</div>

<div class="formula-box">
  <h4>Trap 3: Distribution Over Multiplication $a(bc) \\neq (ab)(ac)$</h4>
  <ul>
    <li><strong style="color:#f43f5e;">The Mistake:</strong> Writing $2(3 \\times 4) = (2 \\times 3) \\times (2 \\times 4) = 6 \\times 8 = 48$.</li>
    <li><strong style="color:#34d399;">Mending the Mistake:</strong> Multiplication distributes over <strong>addition</strong>, NEVER over multiplication! $2(3 \\times 4) = 2 \\times 12 = 24$.</li>
  </ul>
</div>
""",
        "sim_type": "algebraic_mistake_mender",
        "voice": "Section 6.3 is called Mind the Mistake, Mend the Mistake. The most famous algebraic trap is writing a plus b squared equals a squared plus b squared, which completely forgets the 2ab cross term. Another frequent error is distributing a negative sign without changing the signs of all inside terms. Always distribute carefully to every term.",
        "checkpoints": [
            {
                "question": "Which of the following is the CORRECT expansion of (3x - 2y)²?",
                "options": [
                    "9x² - 4y²",
                    "9x² + 4y²",
                    "9x² - 12xy + 4y²",
                    "9x² - 6xy + 4y²"
                ],
                "correct": 2,
                "explanation": "$(3x - 2y)^2 = (3x)^2 - 2(3x)(2y) + (2y)^2 = 9x^2 - 12xy + 4y^2$."
            },
            {
                "question": "Simplify correctly: 5 - (2x - 3)",
                "options": [
                    "2 - 2x",
                    "8 - 2x",
                    "5 - 2x - 3",
                    "-2x - 2"
                ],
                "correct": 1,
                "explanation": "Distribute the negative sign: $5 - 2x - (-3) = 5 - 2x + 3 = 8 - 2x$."
            }
        ]
    },

    # Slide 12: 6.4 This Way or That Way, All Ways Lead to the Bay
    {
        "id": 12,
        "title": "6.4 This Way or That Way, All Ways Lead to the Bay",
        "subtitle": "Equivalent Computational Pathways, Order Invariance & Verification",
        "content": """
<p class="lead">In mathematics, whether you sail east or west, consistent logic guarantees that <strong>all valid pathways lead to the exact same bay</strong>.</p>

<div class="theory-box">
  <h4>Pathway 1 vs. Pathway 2: Evaluating $7(15 + 25)$</h4>
  <ul>
    <li><strong>Pathway A (Parentheses First):</strong>
      $$7 \\times (15 + 25) = 7 \\times 40 = 280$$
    </li>
    <li><strong>Pathway B (Distribute First):</strong>
      $$7(15) + 7(25) = 105 + 175 = 280$$
    </li>
    <li>Both pathways yield the exact same answer: $280$. The choice depends on which is easier mentally!</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Factoring by Taking Common Factors in Reverse</h4>
  <p>The distributive property works in both directions. Going left-to-right is <strong>expansion</strong>; going right-to-left is <strong>factoring</strong>:</p>
  $$ab + ac = a(b + c)$$
  <p>Evaluate $37 \\times 68 + 37 \\times 32$:</p>
  <ul>
    <li>Calculating both products directly is tedious ($2516 + 1184$).</li>
    <li>Factoring out the common $37$:
      $$37 \\times (68 + 32) = 37 \\times 100 = 3700$$
    </li>
  </ul>
</div>

<div class="theory-box">
  <h4>Strategic Flexibility</h4>
  <p>A master of mathematics does not blindly follow a single procedure, but chooses the pathway that offers the cleanest calculation.</p>
</div>
""",
        "sim_type": "multiple_pathways_convergence_engine",
        "voice": "Section 6.4 is titled This Way or That Way, All Ways Lead to the Bay. Whether you add inside parentheses first or distribute first, the result is identical. In reverse, factoring out a common factor simplifies difficult calculations. For 37 times 68 plus 37 times 32, pulling out 37 gives 37 times 100, which is 3700 in an instant.",
        "checkpoints": [
            {
                "question": "What is the most efficient way to compute: 84 × 73 + 84 × 27?",
                "options": [
                    "84 × (73 + 27) = 84 × 100 = 8400",
                    "Multiply 84 × 73, then multiply 84 × 27, and add them",
                    "Multiply 84 × 84 and add 100",
                    "(84 + 84) × (73 + 27)"
                ],
                "correct": 0,
                "explanation": "Factoring out 84 using $ab + ac = a(b + c)$: $84(73 + 27) = 84 \\times 100 = 8400$."
            },
            {
                "question": "Evaluate 25 × 199 + 25:",
                "options": ["4975", "5000", "5025", "5250"],
                "correct": 1,
                "explanation": "Notice $25 = 25 \\times 1$. Factor out 25: $25(199 + 1) = 25 \\times 200 = 5000$."
            }
        ]
    },

    # Slide 13: Factoring by Taking Out Common Monomial Factors
    {
        "id": 13,
        "title": "Factoring Monomials: The Reverse Distributive Tool",
        "subtitle": "Greatest Common Factors (GCF), Variable Powers & Complete Factorization",
        "content": """
<p class="lead"><strong>Factorization</strong> is the process of writing an algebraic expression as a product of its irreducible factors. It is the exact inverse of polynomial expansion.</p>

<div class="formula-box">
  <h4>The Common Monomial Factor Protocol</h4>
  <p>To factor an expression such as $12x^2y + 18xy^2$:</p>
  <ol>
    <li><strong>Find GCF of numerical coefficients:</strong> $\\gcd(12, 18) = 6$.</li>
    <li><strong>Find smallest power of each common variable:</strong>
      <br>• Powers of $x$: $x^2$ and $x^1 \\implies \\text{Common } x^1$.
      <br>• Powers of $y$: $y^1$ and $y^2 \\implies \\text{Common } y^1$.
    </li>
    <li><strong>Greatest Common Monomial:</strong> $6xy$.</li>
    <li><strong>Divide each term by the GCF:</strong>
      $$\\frac{12x^2y}{6xy} = 2x, \\quad \\frac{18xy^2}{6xy} = 3y$$
    </li>
    <li><strong>Final Factored Form:</strong>
      $$12x^2y + 18xy^2 = 6xy(2x + 3y)$$
    </li>
  </ol>
</div>

<div class="theory-box">
  <h4>Verification by Expansion</h4>
  <p>To check your factorization, distribute the monomial back: $6xy(2x) + 6xy(3y) = 12x^2y + 18xy^2$. If it returns to the original polynomial, your factorization is 100% correct!</p>
</div>
""",
        "sim_type": "common_factor_extractor_lab",
        "voice": "Factoring is the reverse of expanding. To factor an expression, find the greatest common factor of the numbers and the lowest power of each common variable. For 12x squared y plus 18x y squared, the greatest common factor is 6xy, leaving 2x plus 3y inside parentheses.",
        "checkpoints": [
            {
                "question": "Factor completely: 15a³b² - 25a²b³",
                "options": [
                    "5ab(3a²b - 5ab²)",
                    "5a²b²(3a - 5b)",
                    "a²b²(15a - 25b)",
                    "5a³b³(3 - 5)"
                ],
                "correct": 1,
                "explanation": "GCF of 15 and 25 is 5. Smallest power of $a$ is $a^2$; smallest power of $b$ is $b^2$. GCF is $5a^2b^2$, leaving $(3a - 5b)$."
            },
            {
                "question": "What is the common factor in 7x(a - b) + 5y(a - b)?",
                "options": ["7x", "5y", "(a - b)", "(7x + 5y)"],
                "correct": 2,
                "explanation": "The binomial $(a - b)$ is common to both terms: $(a - b)(7x + 5y)$."
            }
        ]
    },

    # Slide 14: Factoring by Grouping Terms
    {
        "id": 14,
        "title": "Factoring by Grouping Terms: 4-Term Polynomials",
        "subtitle": "Pairwise Association, Sign Inversions & The Common Binomial Core",
        "content": """
<p class="lead">When an expression contains 4 terms and shares no single factor across all four, we group the terms into <strong>pairs</strong> that share common binomial factors.</p>

<div class="formula-box">
  <h4>Step-by-Step Grouping Algorithm</h4>
  <p>Factor: $ax + ay + bx + by$</p>
  <ol>
    <li><strong>Group into two pairs:</strong>
      $$(ax + ay) + (bx + by)$$
    </li>
    <li><strong>Factor each pair separately:</strong>
      $$a(x + y) + b(x + y)$$
    </li>
    <li><strong>Notice the shared binomial factor $(x + y)$:</strong> Factor out $(x + y)$:
      $$= (a + b)(x + y)$$
    </li>
  </ol>
</div>

<div class="theory-box">
  <h4>Managing Negative Signs: $xy - 3y + 2x - 6$</h4>
  <p>Pair the terms carefully:</p>
  $$(xy - 3y) + (2x - 6) = y(x - 3) + 2(x - 3)$$
  <p>Factoring out the common $(x - 3)$:</p>
  $$= (y + 2)(x - 3)$$
</div>

<div class="formula-box">
  <h4>Warning: Reordering Terms May Be Required!</h4>
  <p>Sometimes the original order does not immediately reveal factors. Example: $6xy - 4y + 6 - 9x$. Reorder as $(6xy - 9x) - (4y - 6) = 3x(2y - 3) - 2(2y - 3) = (3x - 2)(2y - 3)$.</p>
</div>
""",
        "sim_type": "grouping_terms_algebra_workbench",
        "voice": "When factoring an expression with four terms, we use factoring by grouping. Group the terms into pairs, factor out the common monomial from each pair, and then factor out the shared binomial. If signs are tricky, remember that factoring out a negative reverses the inside signs.",
        "checkpoints": [
            {
                "question": "Factor by grouping: px + py + qx + qy",
                "options": [
                    "(p + q)(x + y)",
                    "(p + x)(q + y)",
                    "(px + qy)(1 + 1)",
                    "pq(x + y)"
                ],
                "correct": 0,
                "explanation": "$p(x + y) + q(x + y) = (p + q)(x + y)$."
            },
            {
                "question": "Factor by grouping: ab - bc + ad - cd",
                "options": [
                    "(a - c)(b + d)",
                    "(a + c)(b - d)",
                    "(b - c)(a + d)",
                    "b(a - c) + d"
                ],
                "correct": 0,
                "explanation": "$b(a - c) + d(a - c) = (a - c)(b + d)$."
            }
        ]
    },

    # Slide 15: Master Identity Matrix & Algebraic Toolkit
    {
        "id": 15,
        "title": "Master Identity Matrix & Algebraic Toolkit",
        "subtitle": "The 4 Pillar Identities, Geometric Equivalence & Systematic Overview",
        "content": """
<p class="lead">All polynomial multiplications in Grade 8 mathematics are unified by four foundational algebraic identities derived directly from the distributive property.</p>

<div class="formula-box">
  <h4>The Master Algebraic Identity Table</h4>
  <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:12.5px;">
    <thead>
      <tr style="border-bottom:1px solid #475569; color:#38bdf8;">
        <th align="left" style="padding:4px;">Identity Name</th>
        <th align="left" style="padding:4px;">Standard Form</th>
        <th align="left" style="padding:4px;">Expansion</th>
        <th align="left" style="padding:4px;">Geometric Meaning</th>
      </tr>
    </thead>
    <tbody style="color:#cbd5e1;">
      <tr style="border-bottom:1px solid #1e293b;">
        <td style="padding:4px;"><strong>Identity I</strong></td>
        <td>$(a + b)^2$</td>
        <td>$a^2 + 2ab + b^2$</td>
        <td>Square dissected into 2 squares + 2 rectangles</td>
      </tr>
      <tr style="border-bottom:1px solid #1e293b;">
        <td style="padding:4px;"><strong>Identity II</strong></td>
        <td>$(a - b)^2$</td>
        <td>$a^2 - 2ab + b^2$</td>
        <td>Square with 2 strips removed + corner restored</td>
      </tr>
      <tr style="border-bottom:1px solid #1e293b;">
        <td style="padding:4px;"><strong>Identity III</strong></td>
        <td>$(a + b)(a - b)$</td>
        <td>$a^2 - b^2$</td>
        <td>Difference of squares reshaped into rectangle</td>
      </tr>
      <tr>
        <td style="padding:4px;"><strong>Identity IV</strong></td>
        <td>$(x + a)(x + b)$</td>
        <td>$x^2 + (a + b)x + ab$</td>
        <td>Rectangle with shared base $x$</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="theory-box">
  <h4>Application Strategy</h4>
  <ul>
    <li>Multiplying identical sums $\\to$ Use Identity I.</li>
    <li>Multiplying identical differences $\\to$ Use Identity II.</li>
    <li>Multiplying sum and difference of same terms $\\to$ Use Identity III.</li>
    <li>Common variable with different constants $\\to$ Use Identity IV.</li>
  </ul>
</div>
""",
        "sim_type": "algebraic_identity_master_matrix",
        "voice": "The Master Identity Matrix unites all four fundamental identities of algebra. Whether expanding a plus b squared, a minus b squared, or the difference of squares a squared minus b squared, each identity represents an exact geometric area relationship. Master these four identities to navigate algebra with confidence.",
        "checkpoints": [
            {
                "question": "Which identity should be used to calculate 103 × 97 quickly?",
                "options": [
                    "Identity I: (a + b)²",
                    "Identity II: (a - b)²",
                    "Identity III: (a + b)(a - b) = a² - b²",
                    "Identity IV: (x + a)(x + b)"
                ],
                "correct": 2,
                "explanation": "$103 \\times 97 = (100 + 3)(100 - 3) = 100^2 - 3^2 = 10000 - 9 = 9991$, which is Identity III."
            },
            {
                "question": "Expand (x + 3)(x - 5) using Identity IV: (x + a)(x + b) = x² + (a + b)x + ab:",
                "options": [
                    "x² - 2x - 15",
                    "x² + 2x - 15",
                    "x² - 8x - 15",
                    "x² - 15"
                ],
                "correct": 0,
                "explanation": "Here $a = 3, b = -5$. $a + b = 3 + (-5) = -2$, and $ab = 3(-5) = -15$. Thus $x^2 - 2x - 15$."
            }
        ]
    },

    # Slide 16: SUMMARY & IT'S PUZZLE TIME! Secret Area & Missing Term Riddles
    {
        "id": 16,
        "title": "SUMMARY & IT'S PUZZLE TIME! Detective Room",
        "subtitle": "Mystery Missing Terms, Cryptic Coefficients & Area Deductions",
        "content": """
<p class="lead">Welcome to the Algebraic Detective Room! In this puzzle challenge, determine missing coefficients and secret terms using the identities and distributive laws you have mastered.</p>

<div class="theory-box">
  <h4>Chapter 6 Core Synthesis</h4>
  <ul>
    <li><strong>Distributive Property:</strong> $a(b + c) = ab + ac$ and $a(b - c) = ab - ac$.</li>
    <li><strong>Increments:</strong> $(a + 1)(b + 1) - ab = a + b + 1$.</li>
    <li><strong>The 3 Landmark Identities:</strong>
      <br>1. $(a + b)^2 = a^2 + 2ab + b^2$
      <br>2. $(a - b)^2 = a^2 - 2ab + b^2$
      <br>3. $(a + b)(a - b) = a^2 - b^2$
    </li>
    <li><strong>Factorization:</strong> Reverse distribution by taking out common monomials or grouping in pairs.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Sample Detective Case</h4>
  <p><em>\"If $(x + 5)(x + A) = x^2 + Bx + 35$, find the values of secret constants $A$ and $B$.\"</em></p>
  <p><strong>Deduction:</strong>
  <br>1. The constant term is $5 \\times A = 35 \\implies A = \\frac{35}{5} = 7$.
  <br>2. The middle coefficient is $B = 5 + A = 5 + 7 = 12$.
  <br>Therefore, $A = 7$ and $B = 12$!</p>
</div>
""",
        "sim_type": "algebraic_puzzle_detective_room",
        "voice": "It is puzzle time! In the Algebraic Detective Room, use your mastery of identities and distribution to solve missing term riddles and determine secret constants. Test your skills in our interactive puzzle simulator.",
        "checkpoints": [
            {
                "question": "If (x + 3)(x + K) = x² + 11x + 24, what is the value of K?",
                "options": ["6", "7", "8", "9"],
                "correct": 2,
                "explanation": "Constant term: $3 \\times K = 24 \\implies K = 8$. Also, $3 + 8 = 11$, which matches the middle coefficient."
            },
            {
                "question": "If 4x² + Kx + 25 is a perfect square trinomial (2x + 5)², what is the value of K?",
                "options": ["10", "20", "25", "50"],
                "correct": 1,
                "explanation": "In $(2x + 5)^2 = 4x^2 + 2(2x)(5) + 25 = 4x^2 + 20x + 25$. Therefore, $K = 20$."
            }
        ]
    },

    # Slides 17 to 20: Mastery Quiz Challenges
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: The Distributive Property & Area Geometry",
        "subtitle": "Questions 1 to 10 • Foundational Expansions & Increments",
        "content": "<p class='lead'>Test your foundational mastery of the distributive property, area models, unit increments in products, and fast mental multiplication. Click <strong>💡 View Solution</strong> for step-by-step reasoning.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [1, 10],
        "voice": "Welcome to Mastery Quiz Challenge 1. Solve the first ten questions covering the distributive property, geometric area models, and increments in products. Click View Solution to inspect the step-by-step mathematical reasoning.",
        "checkpoints": []
    },
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: The Landmark Algebraic Identities",
        "subtitle": "Questions 11 to 20 • Expansions of (a+b)², (a-b)², and (a+b)(a-b)",
        "content": "<p class='lead'>Challenge your knowledge of the three landmark identities, difference of squares, and mental shortcuts for numbers near 100. Click <strong>💡 View Solution</strong> for full derivations.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [11, 20],
        "voice": "Now tackle Mastery Quiz Challenge 2. These ten questions focus on expanding squares of sums and differences and using the difference of squares identity. Check your work with View Solution.",
        "checkpoints": []
    },
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Mental Math Patterns & Mending Mistakes",
        "subtitle": "Questions 21 to 30 • Pattern 1, Pattern 2, and Algebraic Diagnostic Repairs",
        "content": "<p class='lead'>Test your ability to spot algebraic traps, mend common student mistakes, and apply mental patterns for products with equal tens digits. Click <strong>💡 View Solution</strong> for step-by-step proofs.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [21, 30],
        "voice": "Mastery Quiz Challenge 3 tests special multiplication patterns and diagnostic error repairs. Review your answers carefully using the solution pop-up modal.",
        "checkpoints": []
    },
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Factorization by Grouping & Detective Puzzles",
        "subtitle": "Questions 31 to 40 • Common Monomials, Grouping Terms & Missing Coefficients",
        "content": "<p class='lead'>Complete the final challenge on factoring by grouping, reverse distribution, and solving mystery coefficient puzzles. Click <strong>💡 View Solution</strong> on any question for full details.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [31, 40],
        "voice": "Congratulations on reaching Mastery Quiz Challenge 4, the final slide of this chapter. Complete the final ten questions on factoring by grouping and mystery algebraic riddles. You have reached the last slide of this chapter.",
        "checkpoints": []
    }
]

# 40 Comprehensive Quiz Questions with In-Depth Step-by-Step Solutions
quiz_questions = [
    # Q1
    {
        "num": 1,
        "question": "Which of the following equations correctly illustrates the Distributive Property of multiplication over subtraction?",
        "options": [
            "a(b - c) = ab - ac",
            "a - (b - c) = (a - b) - c",
            "a(b - c) = ab - c",
            "(a - b)c = ac - b"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The distributive property of multiplication states that a multiplier outside parentheses distributes to every term inside.
2. For subtraction:
   $$a(b - c) = a \\times b - a \\times c = ab - ac$$
3. Both terms $b$ and $c$ must be multiplied by $a$.
4. Option (A) is the exact algebraic statement of the property.
<strong>Correct Answer:</strong> (A) a(b - c) = ab - ac
"""
    },

    # Q2
    {
        "num": 2,
        "question": "If a rectangle has length (2x + 5) and width 4, what is its total area?",
        "options": ["8x + 5", "8x + 20", "2x + 20", "6x + 9"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Area of a rectangle is $\\text{width} \\times \\text{length}$.
2. Applying the distributive property:
   $$\\text{Area} = 4(2x + 5)$$
3. Distribute 4 to both terms:
   $$= 4 \\times 2x + 4 \\times 5 = 8x + 20$$
<strong>Correct Answer:</strong> (B) 8x + 20
"""
    },

    # Q3
    {
        "num": 3,
        "question": "If a = 12 and b = 8, by how much does (a + 1)(b + 1) exceed ab?",
        "options": ["1", "20", "21", "96"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The increment formula for $(a + 1)(b + 1) - ab$ is:
   $$\\Delta = (a + 1)(b + 1) - ab = a + b + 1$$
2. Substitute $a = 12$ and $b = 8$:
   $$\\Delta = 12 + 8 + 1 = 21$$
3. Verification:
   - Original product: $ab = 12 \\times 8 = 96$.
   - New product: $(12 + 1)(8 + 1) = 13 \\times 9 = 117$.
   - Difference: $117 - 96 = 21$.
<strong>Correct Answer:</strong> (C) 21
"""
    },

    # Q4
    {
        "num": 4,
        "question": "Calculate 75 × 99 mentally using the distributive property:",
        "options": ["7425", "7415", "7435", "7495"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Rewrite 99 as $(100 - 1)$:
   $$75 \\times 99 = 75 \\times (100 - 1)$$
2. Distribute 75:
   $$= 75 \\times 100 - 75 \\times 1$$
   $$= 7500 - 75$$
3. Compute the subtraction:
   $$7500 - 75 = 7425$$
<strong>Correct Answer:</strong> (A) 7425
"""
    },

    # Q5
    {
        "num": 5,
        "question": "What is the result of expanding (2x + 3)(3x + 4)?",
        "options": [
            "6x² + 12",
            "6x² + 17x + 12",
            "6x² + 14x + 12",
            "5x² + 17x + 7"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use double distribution:
   $$(2x + 3)(3x + 4) = 2x(3x + 4) + 3(3x + 4)$$
2. Distribute each part:
   $$= (6x^2 + 8x) + (9x + 12)$$
3. Combine like terms:
   $$= 6x^2 + (8x + 9x) + 12 = 6x^2 + 17x + 12$$
<strong>Correct Answer:</strong> (B) 6x² + 17x + 12
"""
    },

    # Q6
    {
        "num": 6,
        "question": "Evaluate 103 × 45 using distribution over addition:",
        "options": ["4635", "4535", "4645", "4735"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Decompose 103 as $(100 + 3)$:
   $$45 \\times 103 = 45 \\times (100 + 3)$$
2. Apply the distributive property:
   $$= 45 \\times 100 + 45 \\times 3$$
3. Compute each product:
   $$= 4500 + 135 = 4635$$
<strong>Correct Answer:</strong> (A) 4635
"""
    },

    # Q7
    {
        "num": 7,
        "question": "If both dimensions of a square of side x are increased by 2, what is the increase in area?",
        "options": ["4", "2x + 4", "4x + 4", "x² + 4"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Original area of the square of side $x$ is $x^2$.
2. New side length is $(x + 2)$, so new area is:
   $$(x + 2)^2 = x^2 + 4x + 4$$
3. The increase in area is:
   $$\\text{New Area} - \\text{Old Area} = (x^2 + 4x + 4) - x^2 = 4x + 4$$
<strong>Correct Answer:</strong> (C) 4x + 4
"""
    },

    # Q8
    {
        "num": 8,
        "question": "What is the product of (a - 3)(b + 4)?",
        "options": [
            "ab - 12",
            "ab + 4a - 3b - 12",
            "ab - 3a + 4b - 12",
            "ab - 4a + 3b + 12"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Distribute $(a - 3)$ across $(b + 4)$:
   $$(a - 3)(b + 4) = a(b + 4) - 3(b + 4)$$
2. Multiply each term:
   $$= ab + 4a - 3b - 12$$
<strong>Correct Answer:</strong> (B) ab + 4a - 3b - 12
"""
    },

    # Q9
    {
        "num": 9,
        "question": "Evaluate mentally: 68 × 25 using 25 = 100 / 4:",
        "options": ["1600", "1700", "1750", "1800"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Since $25 = \\frac{100}{4}$:
   $$68 \\times 25 = 68 \\times \\frac{100}{4} = \\frac{68}{4} \\times 100$$
2. Divide 68 by 4:
   $$68 \\div 4 = 17$$
3. Multiply by 100:
   $$17 \\times 100 = 1700$$
<strong>Correct Answer:</strong> (B) 1700
"""
    },

    # Q10
    {
        "num": 10,
        "question": "If (x + a)(x + b) = x² + 9x + 20, what are the values of a and b (where a < b)?",
        "options": ["a = 1, b = 20", "a = 2, b = 10", "a = 4, b = 5", "a = 3, b = 6"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Identity IV states:
   $$(x + a)(x + b) = x^2 + (a + b)x + ab$$
2. Comparing coefficients:
   - Sum: $a + b = 9$
   - Product: $ab = 20$
3. Find two numbers whose product is 20 and sum is 9:
   - Factors of 20: $(1, 20) \\to 21$; $(2, 10) \\to 12$; $(4, 5) \\to 9$.
4. Thus $a = 4$ and $b = 5$.
<strong>Correct Answer:</strong> (C) a = 4, b = 5
"""
    },

    # Q11
    {
        "num": 11,
        "question": "What is the expansion of (3a + 4b)²?",
        "options": [
            "9a² + 16b²",
            "9a² + 12ab + 16b²",
            "9a² + 24ab + 16b²",
            "6a² + 24ab + 8b²"
        ],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use Identity I: $(A + B)^2 = A^2 + 2AB + B^2$.
2. Here $A = 3a$ and $B = 4b$.
3. Compute each term:
   - $A^2 = (3a)^2 = 9a^2$
   - $2AB = 2(3a)(4b) = 24ab$
   - $B^2 = (4b)^2 = 16b^2$
4. Combining: $9a^2 + 24ab + 16b^2$.
<strong>Correct Answer:</strong> (C) 9a² + 24ab + 16b²
"""
    },

    # Q12
    {
        "num": 12,
        "question": "What is the expansion of (5x - 2y)²?",
        "options": [
            "25x² - 4y²",
            "25x² - 10xy + 4y²",
            "25x² - 20xy + 4y²",
            "25x² + 20xy - 4y²"
        ],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use Identity II: $(A - B)^2 = A^2 - 2AB + B^2$.
2. Here $A = 5x$ and $B = 2y$.
3. Compute each term:
   - $A^2 = (5x)^2 = 25x^2$
   - $2AB = 2(5x)(2y) = 20xy$
   - $B^2 = (2y)^2 = 4y^2$
4. Combining: $25x^2 - 20xy + 4y^2$.
<strong>Correct Answer:</strong> (C) 25x² - 20xy + 4y²
"""
    },

    # Q13
    {
        "num": 13,
        "question": "What is the product of (6x + 7)(6x - 7)?",
        "options": [
            "36x² - 49",
            "36x² + 49",
            "36x² - 84x - 49",
            "12x² - 49"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use Identity III (Difference of Two Squares):
   $$(A + B)(A - B) = A^2 - B^2$$
2. Here $A = 6x$ and $B = 7$.
3. Compute squares:
   - $A^2 = (6x)^2 = 36x^2$
   - $B^2 = 7^2 = 49$
4. Combining: $36x^2 - 49$.
<strong>Correct Answer:</strong> (A) 36x² - 49
"""
    },

    # Q14
    {
        "num": 14,
        "question": "Evaluate 105 × 95 using Identity III:",
        "options": ["9975", "9985", "9965", "9955"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Notice that 105 and 95 are symmetric around 100:
   $$105 = 100 + 5 \\quad \\text{and} \\quad 95 = 100 - 5$$
2. Apply $(a + b)(a - b) = a^2 - b^2$:
   $$105 \\times 95 = (100 + 5)(100 - 5) = 100^2 - 5^2$$
3. Compute the squares:
   $$= 10000 - 25 = 9975$$
<strong>Correct Answer:</strong> (A) 9975
"""
    },

    # Q15
    {
        "num": 15,
        "question": "If x + 1/x = 5, what is the value of x² + 1/x²?",
        "options": ["23", "25", "27", "21"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Square both sides of the equation $x + \\frac{1}{x} = 5$:
   $$\\left(x + \\frac{1}{x}\\right)^2 = 5^2$$
2. Expand the left-hand side using Identity I:
   $$x^2 + 2(x)\\left(\\frac{1}{x}\\right) + \\frac{1}{x^2} = 25$$
3. Notice that $x \\times \\frac{1}{x} = 1$:
   $$x^2 + 2 + \\frac{1}{x^2} = 25$$
4. Subtract 2 from both sides:
   $$x^2 + \\frac{1}{x^2} = 25 - 2 = 23$$
<strong>Correct Answer:</strong> (A) 23
"""
    },

    # Q16
    {
        "num": 16,
        "question": "If x - 1/x = 6, what is the value of x² + 1/x²?",
        "options": ["34", "36", "38", "40"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Square both sides of the equation $x - \\frac{1}{x} = 6$:
   $$\\left(x - \\frac{1}{x}\\right)^2 = 6^2$$
2. Expand the left-hand side using Identity II:
   $$x^2 - 2(x)\\left(\\frac{1}{x}\\right) + \\frac{1}{x^2} = 36$$
   $$x^2 - 2 + \\frac{1}{x^2} = 36$$
3. Add 2 to both sides:
   $$x^2 + \\frac{1}{x^2} = 36 + 2 = 38$$
<strong>Correct Answer:</strong> (C) 38
"""
    },

    # Q17
    {
        "num": 17,
        "question": "Evaluate 198 × 202 using the difference of squares identity:",
        "options": ["39,996", "39,984", "39,994", "40,004"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Notice that 198 and 202 are centered around 200:
   $$198 = 200 - 2 \\quad \\text{and} \\quad 202 = 200 + 2$$
2. Apply $(a - b)(a + b) = a^2 - b^2$:
   $$198 \\times 202 = 200^2 - 2^2$$
3. Calculate:
   $$= 40000 - 4 = 39996$$
<strong>Correct Answer:</strong> (A) 39,996
"""
    },

    # Q18
    {
        "num": 18,
        "question": "What is the value of 52² - 48² calculated using Identity III?",
        "options": ["400", "200", "100", "800"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use $a^2 - b^2 = (a + b)(a - b)$ with $a = 52$ and $b = 48$:
   $$52^2 - 48^2 = (52 + 48)(52 - 48)$$
2. Simplify the factors:
   $$= (100) \\times (4) = 400$$
<strong>Correct Answer:</strong> (A) 400
"""
    },

    # Q19
    {
        "num": 19,
        "question": "If (2a + b)² = 4a² + 12a + b², what must the value of b be?",
        "options": ["2", "3", "4", "6"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Expand $(2a + b)^2$:
   $$(2a + b)^2 = 4a^2 + 2(2a)(b) + b^2 = 4a^2 + 4ab + b^2$$
2. We are given this equals $4a^2 + 12a + b^2$.
3. Equate the middle terms:
   $$4ab = 12a$$
4. Divide both sides by $4a$ (for $a \\neq 0$):
   $$b = \\frac{12a}{4a} = 3$$
<strong>Correct Answer:</strong> (B) 3
"""
    },

    # Q20
    {
        "num": 20,
        "question": "What is the simplified form of (a + b)² - (a - b)²?",
        "options": ["2a² + 2b²", "4ab", "2ab", "0"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Expand both terms:
   $$(a + b)^2 = a^2 + 2ab + b^2$$
   $$(a - b)^2 = a^2 - 2ab + b^2$$
2. Subtract the second expansion from the first:
   $$(a^2 + 2ab + b^2) - (a^2 - 2ab + b^2)$$
   $$= a^2 + 2ab + b^2 - a^2 + 2ab - b^2$$
3. The terms $a^2$ and $b^2$ cancel:
   $$= 2ab + 2ab = 4ab$$
<strong>Correct Answer:</strong> (B) 4ab
"""
    },

    # Q21
    {
        "num": 21,
        "question": "Using Pattern 1 (same tens digit, units adding to 10), calculate 63 × 67:",
        "options": ["4221", "4211", "3621", "4231"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Tens digit is $T = 6$. Units digits are $3$ and $7$ ($3 + 7 = 10$).
2. Left part: $T \\times (T + 1) = 6 \\times 7 = 42$.
3. Right part: $3 \\times 7 = 21$.
4. Combined result: 4221.
<strong>Correct Answer:</strong> (A) 4221
"""
    },

    # Q22
    {
        "num": 22,
        "question": "Using Pattern 1, what is 75²?",
        "options": ["5625", "5425", "4925", "5635"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Tens digit $T = 7$.
2. Left part: $T \\times (T + 1) = 7 \\times 8 = 56$.
3. Right part: $5 \\times 5 = 25$.
4. Combined result: 5625.
<strong>Correct Answer:</strong> (A) 5625
"""
    },

    # Q23
    {
        "num": 23,
        "question": "Using the base-100 deviation method (Pattern 2), calculate 108 × 103:",
        "options": ["11,124", "11,024", "11,224", "11,134"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Deviations from 100 are $+8$ and $+3$.
2. Left part: $108 + 3 = 111$ (or $103 + 8 = 111$).
3. Right part: Multiply deviations: $8 \\times 3 = 24$.
4. Combined result: 11,124.
<strong>Correct Answer:</strong> (A) 11,124
"""
    },

    # Q24
    {
        "num": 24,
        "question": "Using the base-100 deviation method, calculate 92 × 98:",
        "options": ["9,016", "9,116", "9,026", "8,916"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Deviations from 100 are $-8$ and $-2$.
2. Left part: Cross-subtract: $92 - 2 = 90$ (or $98 - 8 = 90$).
3. Right part: Multiply deviations: $(-8) \\times (-2) = +16$.
4. Combined result: 9,016.
<strong>Correct Answer:</strong> (A) 9,016
"""
    },

    # Q25
    {
        "num": 25,
        "question": "A student wrote: (2x - 3y)² = 4x² - 9y². What error did the student commit?",
        "options": [
            "Forgot the cross-term -12xy and made the last term negative instead of positive",
            "Multiplied 2 by 3 incorrectly",
            "The expansion is completely correct",
            "Forgot to divide by 2"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The student committed two classic errors:
   - Completely omitted the middle cross-term $-2AB = -2(2x)(3y) = -12xy$.
   - Wrote $-9y^2$ instead of $+9y^2$, forgetting that $(-3y)^2 = +9y^2$.
2. Correct expansion: $4x^2 - 12xy + 9y^2$.
<strong>Correct Answer:</strong> (A) Forgot the cross-term -12xy and made the last term negative instead of positive
"""
    },

    # Q26
    {
        "num": 26,
        "question": "Simplify: -(4x - 9) + (2x - 5)",
        "options": ["-2x + 4", "-2x - 14", "2x + 4", "-6x + 14"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Distribute the negative sign across the first parentheses:
   $$-(4x - 9) = -4x + 9$$
2. Add the second expression:
   $$(-4x + 9) + (2x - 5)$$
3. Combine like terms:
   $$(-4x + 2x) + (9 - 5) = -2x + 4$$
<strong>Correct Answer:</strong> (A) -2x + 4
"""
    },

    # Q27
    {
        "num": 27,
        "question": "Evaluate 29 × 31 + 1 without a calculator:",
        "options": ["899", "900", "901", "920"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Notice that 29 and 31 have a gap of 2 around the average $m = 30$:
   $$29 \\times 31 = (30 - 1)(30 + 1) = 30^2 - 1 = 900 - 1 = 899$$
2. Adding 1:
   $$899 + 1 = 900 = 30^2$$
<strong>Correct Answer:</strong> (B) 900
"""
    },

    # Q28
    {
        "num": 28,
        "question": "What is the value of: 3(x + 4) - 2(x - 3)?",
        "options": ["x + 6", "x + 18", "x - 6", "5x + 6"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Distribute 3 across $(x + 4)$:
   $$3(x) + 3(4) = 3x + 12$$
2. Distribute $-2$ across $(x - 3)$ (carefully watching signs!):
   $$-2(x) + (-2)(-3) = -2x + 6$$
3. Combine like terms:
   $$(3x - 2x) + (12 + 6) = x + 18$$
<strong>Correct Answer:</strong> (B) x + 18
"""
    },

    # Q29
    {
        "num": 29,
        "question": "Which of the following is an example of an expression that CANNOT be factored over the real numbers?",
        "options": ["x² - 9", "x² + 9", "x² - 4", "x² - 25"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Difference of squares $x^2 - 9 = (x - 3)(x + 3)$, $x^2 - 4 = (x - 2)(x + 2)$, and $x^2 - 25 = (x - 5)(x + 5)$ all factor easily.
2. However, the sum of two squares $x^2 + 9$ has no real roots and cannot be factored into real linear factors.
<strong>Correct Answer:</strong> (B) x² + 9
"""
    },

    # Q30
    {
        "num": 30,
        "question": "Compute mentally: 17 × 43 + 17 × 57",
        "options": ["1700", "1750", "1600", "1800"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Factor out 17 using the distributive property in reverse:
   $$17 \\times 43 + 17 \\times 57 = 17 \\times (43 + 57)$$
2. Add inside parentheses:
   $$43 + 57 = 100$$
3. Multiply:
   $$17 \\times 100 = 1700$$
<strong>Correct Answer:</strong> (A) 1700
"""
    },

    # Q31
    {
        "num": 31,
        "question": "Factor completely: 18x²y - 24xy²",
        "options": [
            "6xy(3x - 4y)",
            "3xy(6x - 8y)",
            "6x²y²(3 - 4)",
            "xy(18x - 24y)"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Find the GCF of the coefficients: $\\gcd(18, 24) = 6$.
2. Find the lowest power of common variables:
   - For $x$: lowest power is $x^1$.
   - For $y$: lowest power is $y^1$.
3. The common monomial factor is $6xy$.
4. Divide each term by $6xy$:
   $$\\frac{18x^2y}{6xy} = 3x, \\quad \\frac{-24xy^2}{6xy} = -4y$$
5. Factored form: $6xy(3x - 4y)$.
<strong>Correct Answer:</strong> (A) 6xy(3x - 4y)
"""
    },

    # Q32
    {
        "num": 32,
        "question": "Factor by grouping: ax + bx - ay - by",
        "options": [
            "(a + b)(x - y)",
            "(a - b)(x + y)",
            "(a + b)(x + y)",
            "(a - b)(x - y)"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Group into pairs:
   $$(ax + bx) - (ay + by)$$
2. Factor out common terms from each pair:
   $$x(a + b) - y(a + b)$$
3. Factor out the shared binomial $(a + b)$:
   $$= (a + b)(x - y)$$
<strong>Correct Answer:</strong> (A) (a + b)(x - y)
"""
    },

    # Q33
    {
        "num": 33,
        "question": "Factor by grouping: 15xy - 6x + 5y - 2",
        "options": [
            "(3x + 1)(5y - 2)",
            "(3x - 1)(5y + 2)",
            "(5x + 1)(3y - 2)",
            "(15x + 1)(y - 2)"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Group into pairs:
   $$(15xy - 6x) + (5y - 2)$$
2. Factor $3x$ from the first pair:
   $$3x(5y - 2) + 1(5y - 2)$$
3. Factor out the common binomial $(5y - 2)$:
   $$= (3x + 1)(5y - 2)$$
<strong>Correct Answer:</strong> (A) (3x + 1)(5y - 2)
"""
    },

    # Q34
    {
        "num": 34,
        "question": "Factor completely: 49x² - 64y²",
        "options": [
            "(7x - 8y)²",
            "(7x + 8y)(7x - 8y)",
            "(49x + 64y)(x - y)",
            "7x(7x - 64y)"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Recognize the Difference of Two Squares:
   $$49x^2 = (7x)^2 \\quad \\text{and} \\quad 64y^2 = (8y)^2$$
2. Apply $A^2 - B^2 = (A + B)(A - B)$:
   $$(7x + 8y)(7x - 8y)$$
<strong>Correct Answer:</strong> (B) (7x + 8y)(7x - 8y)
"""
    },

    # Q35
    {
        "num": 35,
        "question": "Factor: x² + 14x + 49",
        "options": [
            "(x + 7)²",
            "(x - 7)²",
            "(x + 7)(x - 7)",
            "(x + 14)(x + 1)"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Observe that this is a perfect square trinomial:
   - First term is $x^2 = (x)^2$.
   - Last term is $49 = (7)^2$.
   - Middle term is $2(x)(7) = 14x$.
2. It matches Identity I: $(x + 7)^2$.
<strong>Correct Answer:</strong> (A) (x + 7)²
"""
    },

    # Q36
    {
        "num": 36,
        "question": "Detective Riddle: 'If (x + P)(x + Q) = x² - 10x + 21, and P < Q, what is the value of P - Q?'",
        "options": ["-4", "-2", "2", "4"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Identity IV: $(x + P)(x + Q) = x^2 + (P + Q)x + PQ$.
2. Equating coefficients:
   - Sum: $P + Q = -10$
   - Product: $PQ = 21$
3. Find two numbers that multiply to $+21$ and add to $-10$:
   - The numbers are $-7$ and $-3$.
4. Since $P < Q$, we have $P = -7$ and $Q = -3$.
5. Compute $P - Q$:
   $$P - Q = -7 - (-3) = -7 + 3 = -4$$
<strong>Correct Answer:</strong> (A) -4
"""
    },

    # Q37
    {
        "num": 37,
        "question": "What is the value of (1001² - 999²) / 4000?",
        "options": ["1", "2", "4", "10"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use Difference of Squares in the numerator:
   $$1001^2 - 999^2 = (1001 + 999)(1001 - 999)$$
2. Compute the factors:
   $$1001 + 999 = 2000$$
   $$1001 - 999 = 2$$
3. Numerator $= 2000 \\times 2 = 4000$.
4. Divide by denominator:
   $$\\frac{4000}{4000} = 1$$
<strong>Correct Answer:</strong> (A) 1
"""
    },

    # Q38
    {
        "num": 38,
        "question": "Find the missing term K so that 9x² - Kx + 16 is a perfect square trinomial:",
        "options": ["12", "24", "36", "48"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. A perfect square trinomial has the form $(Ax - B)^2 = A^2x^2 - 2ABx + B^2$.
2. Here:
   - $A^2x^2 = 9x^2 \\implies Ax = 3x$
   - $B^2 = 16 \\implies B = 4$
3. The middle term is:
   $$2ABx = 2(3x)(4) = 24x$$
4. Therefore, $K = 24$.
<strong>Correct Answer:</strong> (B) 24
"""
    },

    # Q39
    {
        "num": 39,
        "question": "If a + b = 9 and ab = 14, what is the value of a² + b²?",
        "options": ["53", "67", "81", "95"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Start with Identity I:
   $$(a + b)^2 = a^2 + 2ab + b^2$$
2. Rearrange to solve for $a^2 + b^2$:
   $$a^2 + b^2 = (a + b)^2 - 2ab$$
3. Substitute the given values $a + b = 9$ and $ab = 14$:
   $$a^2 + b^2 = 9^2 - 2(14) = 81 - 28 = 53$$
<strong>Correct Answer:</strong> (A) 53
"""
    },

    # Q40
    {
        "num": 40,
        "question": "If a - b = 7 and ab = 18, what is the value of a² + b²?",
        "options": ["49", "67", "85", "103"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Start with Identity II:
   $$(a - b)^2 = a^2 - 2ab + b^2$$
2. Rearrange to solve for $a^2 + b^2$:
   $$a^2 + b^2 = (a - b)^2 + 2ab$$
3. Substitute the given values $a - b = 7$ and $ab = 18$:
   $$a^2 + b^2 = 7^2 + 2(18) = 49 + 36 = 85$$
<strong>Correct Answer:</strong> (C) 85
"""
    }
]


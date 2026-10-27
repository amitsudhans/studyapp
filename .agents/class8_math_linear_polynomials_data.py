# -*- coding: utf-8 -*-
"""
Curriculum and Slide Data for NCERT Class 8 Mathematics Chapter 2:
Introduction to Linear Polynomials (Mathematics Grade 8)
Syllabus:
- 2.1 INTRODUCTION & EXERCISE SET 2.1
- 2.2 LINEAR POLYNOMIALS & EXERCISE SET 2.2
- 2.3 EXPLORING LINEAR PATTERNS & EXERCISE SET 2.3
- 2.4 LINEAR GROWTH AND LINEAR DECAY & EXERCISE SET 2.4
- 2.5 LINEAR RELATIONSHIPS & EXERCISE SET 2.5
- 2.6 VISUALISING LINEAR RELATIONSHIPS & EXERCISE SET 2.6
- END-OF-CHAPTER EXERCISES & CHAPTER SUMMARY
Structure:
- 20 Slides (16 Comprehensive Interactive Lessons + 4 Dedicated Quiz Slides)
- 32 In-Slide Checkpoints (2 per lesson slide)
- 40 Comprehensive Quiz Questions (10 per quiz slide) with step-by-step pop-up solution modals
- Teacher avatar: Prof. Ramanujan Sharma (Senior Mathematics Mentor)
"""

slides_data = [
    # Slide 1: 2.1 Introduction to Algebraic Expressions & Patterns
    {
        "id": 1,
        "title": "2.1 Introduction to Algebraic Expressions & Patterns",
        "subtitle": "From Arithmetic Sequences to General Algebraic Formulas (NCERT Section 2.1)",
        "content": r"""
<p class="lead-p">Algebra is the generalized language of arithmetic. When quantities change predictably—such as the number of matchsticks required to construct a chain of geometric figures, or the fare of an auto-rickshaw across distances—we use <strong>variables</strong> to express dynamic relationships that hold universally.</p>

<div class="theory-box">
  <h4>1. Constants, Variables & Algebraic Terms</h4>
  <p>In mathematics, an algebraic expression is assembled from three foundational components:</p>
  <ul>
    <li><strong>Constants:</strong> Fixed numerical values that do not change (e.g., $5, -12, \frac{3}{4}, 0$).</li>
    <li><strong>Variables (Indeterminates):</strong> Letters representing unknown or varying quantities (e.g., $x, y, t, n$). A variable can take different numerical values.</li>
    <li><strong>Terms:</strong> A product of constants and variables raised to non-negative integer powers, such as $4x, -7x^2, 15$. The constant factor is called the <strong>coefficient</strong>.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Matchstick Geometric Patterns</h4>
    <p>Consider constructing a row of adjoining squares using matchsticks:</p>
    <ul>
      <li>1 square: 4 matchsticks ($3 \times 1 + 1 = 4$).</li>
      <li>2 squares: 7 matchsticks ($3 \times 2 + 1 = 7$).</li>
      <li>3 squares: 10 matchsticks ($3 \times 3 + 1 = 10$).</li>
    </ul>
    <p class="highlight-eq">$$\text{For } n \text{ squares, Matchsticks } = 3n + 1$$</p>
    <p>Here, $3n + 1$ is an algebraic expression where $n$ is the variable representing the number of squares.</p>
  </div>
  <div class="card-item">
    <h4>Exercise Set 2.1 Foundations</h4>
    <p>Translating verbal word patterns into algebraic expressions:</p>
    <ul>
      <li><em>"5 more than twice a number":</em> $2x + 5$</li>
      <li><em>"7 subtracted from three times a quantity":</em> $3y - 7$</li>
      <li><em>"A base charge of ₹20 plus ₹12 per kilometre":</em> $12k + 20$</li>
    </ul>
    <p class="highlight-eq">$$\text{Evaluating at } x = 4: \quad 2(4) + 5 = 13$$</p>
  </div>
</div>
""",
        "sim_type": "matchstick_pattern_builder",
        "voice": "Welcome to Chapter 2 of Class 8 Mathematics: Introduction to Linear Polynomials! Notice how geometric patterns in nature and arithmetic follow strict algebraic rules. Look at our matchstick simulator: each new square requires exactly 3 more sticks! That gives us the rule: three n plus one! Adjust the slider to see this live.",
        "checkpoints": [
            {
                "question": "How many matchsticks are needed to build a chain of 15 adjoining squares using the rule 3n + 1?",
                "options": ["45", "46", "48", "50"],
                "correct": 1,
                "explanation": "Substitute n = 15 into the formula: 3(15) + 1 = 45 + 1 = 46 matchsticks."
            },
            {
                "question": "In the algebraic term -8x, what is the numerical coefficient of x?",
                "options": ["8", "-8", "x", "-1"],
                "correct": 1,
                "explanation": "The numerical coefficient is the constant multiplying the variable, which is -8."
            }
        ]
    },

    # Slide 2: Exercise Set 2.1 — Problem Solving & Pattern Formulations
    {
        "id": 2,
        "title": "Exercise Set 2.1: Pattern Formulation & Evaluation",
        "subtitle": "Mastering Substitution, Table Construction and Sequence Rules",
        "content": r"""
<p class="lead-p">Exercise Set 2.1 trains students to analyze numerical tables, detect common constant differences, formulate the underlying algebraic expression, and evaluate it for arbitrary values.</p>

<div class="theory-box">
  <h4>1. Table Analysis & Common Difference Method</h4>
  <p>Suppose an input-output table shows the following values:</p>
  <p class="highlight-eq">$$\text{Input } n: \quad 1 \to 5, \quad 2 \to 9, \quad 3 \to 13, \quad 4 \to 17$$</p>
  <ol>
    <li><strong>Compute First Differences:</strong> $9 - 5 = 4$, $13 - 9 = 4$, $17 - 13 = 4$. The difference is a constant $d = 4$.</li>
    <li><strong>Set up Candidate Form:</strong> Since difference is constant 4, the term contains $4n$.</li>
    <li><strong>Find the Zero-Term Offset ($c$):</strong> For $n = 1$, $4(1) + c = 5 \implies c = 1$.</li>
    <li><strong>General Formula:</strong> $T(n) = 4n + 1$.</li>
  </ol>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Triangular and Border Patterns</h4>
    <p>A garden border requires 4 corner tiles plus 2 tiles along each unit of length $L$:</p>
    <p class="highlight-eq">$$\text{Total Border Tiles } B(L) = 2L + 4$$</p>
    <p>For $L = 25 \text{ meters}$, $B(25) = 2(25) + 4 = 54 \text{ tiles}$.</p>
    <p>Linear expressions allow engineers and landscapers to order exact quantities without manual counting.</p>
  </div>
  <div class="card-item">
    <h4>Verifying Algebraic Invariance</h4>
    <p>An algebraic formula must hold true for all positive integers $n \in \mathbb{N}$:</p>
    <ul>
      <li>$n = 1: \quad 4(1) + 1 = 5$ ✓</li>
      <li>$n = 50: \quad 4(50) + 1 = 201$</li>
      <li>$n = 100: \quad 4(100) + 1 = 401$</li>
    </ul>
    <p>Algebra eliminates the need to calculate terms one-by-one!</p>
  </div>
</div>
""",
        "sim_type": "table_difference_analyzer",
        "voice": "When you examine an arithmetic table, check the difference between consecutive outputs! If the step size is always constant, like plus 4, then your expression begins with 4n! Then simply adjust for the starting term. Test different sequence patterns in our interactive Table Difference Analyzer!",
        "checkpoints": [
            {
                "question": "What is the general nth term for the sequence: 7, 12, 17, 22, 27...?",
                "options": ["5n + 2", "5n + 7", "7n + 5", "5n - 2"],
                "correct": 0,
                "explanation": "The common difference is 12 - 7 = 5. For n = 1, 5(1) + c = 7 => c = 2. Hence, the nth term is 5n + 2."
            },
            {
                "question": "If the pattern rule is T(n) = 6n - 3, what is the 20th term?",
                "options": ["114", "117", "120", "123"],
                "correct": 1,
                "explanation": "Substitute n = 20: T(20) = 6(20) - 3 = 120 - 3 = 117."
            }
        ]
    },

    # Slide 3: 2.2 Linear Polynomials — Definition, Degree & Classification
    {
        "id": 3,
        "title": "2.2 What is a Linear Polynomial?",
        "subtitle": "Polynomial Definition, Degree 1 Criterion and Standard Form ax + b (NCERT Section 2.2)",
        "content": r"""
<p class="lead-p">The word <em>polynomial</em> comes from Greek <em>poly</em> (many) and Latin <em>nomen</em> (name or term). In algebra, a polynomial in one variable $x$ is an algebraic expression where the powers of $x$ are strictly non-negative integers ($0, 1, 2, 3 \dots$).</p>

<div class="theory-box">
  <h4>1. Formal Mathematical Definition of Linear Polynomial</h4>
  <p>A polynomial $P(x)$ of <strong>degree 1</strong> is called a <strong>linear polynomial</strong>. Its general standard form is:</p>
  <p class="highlight-eq">$$P(x) = ax + b, \quad \text{where } a, b \in \mathbb{R} \text{ and } a \neq 0$$</p>
  <ul>
    <li>$a$ is the <strong>leading coefficient</strong> (coefficient of $x$). It must be non-zero ($a \neq 0$), otherwise the term $x$ vanishes and it becomes a constant!</li>
    <li>$b$ is the <strong>constant term</strong> ($b \cdot x^0 = b$).</li>
    <li>The exponent of the variable $x$ is strictly <strong>1</strong> (which is why its degree is 1).</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Examples of Linear Polynomials</h4>
    <ul>
      <li>$3x + 5$ &emsp; ($a = 3, b = 5$)</li>
      <li>$-7y + 2$ &emsp; ($a = -7, b = 2$)</li>
      <li>$\frac{2}{3}u - 9$ &emsp; ($a = 2/3, b = -9$)</li>
      <li>$4z$ &emsp; ($a = 4, b = 0$, linear monomial)</li>
      <li>$\sqrt{2}t + 8$ &emsp; ($a = \sqrt{2}, b = 8$, real coefficients)</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Non-Linear Expressions (Disqualifications)</h4>
    <p>The following are <strong>NOT linear polynomials</strong>:</p>
    <ul>
      <li>$x^2 + 3x - 1$ &emsp; (Degree 2, <em>quadratic</em>)</li>
      <li>$\frac{5}{x} + 2 = 5x^{-1} + 2$ &emsp; (Negative exponent $-1$)</li>
      <li>$\sqrt{x} + 4 = x^{1/2} + 4$ &emsp; (Fractional exponent)</li>
      <li>$0x + 7 = 7$ &emsp; (Constant, degree 0)</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "polynomial_classifier_engine",
        "voice": "What makes a polynomial linear? Two strict rules: first, the variable can only be raised to the power of 1, and second, its leading coefficient a cannot be zero! The standard form is a x plus b. If you have an x squared, it is quadratic. If x is in the denominator, it is not even a polynomial! Try classifying different expressions on your screen.",
        "checkpoints": [
            {
                "question": "Which of the following is a linear polynomial in one variable?",
                "options": ["3x² + 5", "7x - 4", "4/x + 9", "2√x + 1"],
                "correct": 1,
                "explanation": "7x - 4 is of the form ax + b with a = 7 ≠ 0 and degree 1. The others have exponent 2, exponent -1, or exponent 1/2."
            },
            {
                "question": "Why is P(x) = 0x + 8 NOT a linear polynomial?",
                "options": ["Because 8 is a constant", "Because the coefficient a is zero, making its degree 0", "Because x has degree 1", "Because it has no variable"],
                "correct": 1,
                "explanation": "For a polynomial to be linear, the coefficient of x must satisfy a ≠ 0. If a = 0, P(x) = 8, which is a constant polynomial of degree 0."
            }
        ]
    },

    # Slide 4: Exercise Set 2.2 — Coefficients, Degree & Standard Form
    {
        "id": 4,
        "title": "Exercise Set 2.2: Standard Form ax + b & Identification",
        "subtitle": "Extracting Parameters a and b, Polynomial Addition and Zeroes (NCERT Section 2.2)",
        "content": r"""
<p class="lead-p">In Exercise Set 2.2, students master rearranging mixed expressions into the standard form $ax + b$, identifying the leading coefficient $a$ and constant term $b$, and finding the <strong>zero of a linear polynomial</strong>.</p>

<div class="theory-box">
  <h4>1. Rearranging into Standard Form</h4>
  <p>Often expressions appear in scrambled or expanded form. We collect like terms and simplify:</p>
  <ul>
    <li>$E_1(x) = 5 - 3x \implies -3x + 5 \quad (a = -3, b = 5)$</li>
    <li>$E_2(x) = 4(2x - 3) + 7 = 8x - 12 + 7 = 8x - 5 \quad (a = 8, b = -5)$</li>
    <li>$E_3(x) = \frac{6x - 9}{3} = \frac{6x}{3} - \frac{9}{3} = 2x - 3 \quad (a = 2, b = -3)$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Zero (Root) of a Linear Polynomial</h4>
    <p>A number $k$ is called a <strong>zero</strong> of $P(x)$ if $P(k) = 0$:</p>
    <p class="highlight-eq">$$ax + b = 0 \implies ax = -b \implies x = -\frac{b}{a}$$</p>
    <p>Every linear polynomial has <strong>exactly one unique real zero</strong>:</p>
    <p>For $P(x) = 2x - 6$: Zero is $x = -\frac{-6}{2} = 3$.<br>Check: $P(3) = 2(3) - 6 = 6 - 6 = 0$.</p>
  </div>
  <div class="card-item">
    <h4>3. Linear Polynomial vs. Linear Equation</h4>
    <ul>
      <li><strong>Linear Polynomial:</strong> An expression $P(x) = ax + b$ that can be evaluated for any input $x$.</li>
      <li><strong>Linear Equation:</strong> A statement of equality $ax + b = c$ which can be solved for a specific unknown $x$.</li>
    </ul>
    <p class="highlight-eq">$$\text{Setting } P(x) = 0 \text{ transforms it into an equation!}$$</p>
  </div>
</div>
""",
        "sim_type": "standard_form_transformer",
        "voice": "Here is an important distinction: a polynomial is an algebraic expression like 2x minus 6. But when you set it equal to zero, 2x minus 6 equals 0, you create an equation! The value of x that makes the polynomial equal to zero is called its root or zero, and it is always equal to minus b divided by a!",
        "checkpoints": [
            {
                "question": "What is the zero of the linear polynomial P(x) = 5x + 15?",
                "options": ["x = 3", "x = -3", "x = 15", "x = -15"],
                "correct": 1,
                "explanation": "Set P(x) = 0: 5x + 15 = 0 => 5x = -15 => x = -15/5 = -3."
            },
            {
                "question": "Simplify 3(4x - 2) - 5x + 7 into standard form ax + b and find a and b.",
                "options": ["a = 7, b = 1", "a = 7, b = -1", "a = 12, b = 1", "a = 7, b = 13"],
                "correct": 0,
                "explanation": "Expand: 12x - 6 - 5x + 7 = (12 - 5)x + (-6 + 7) = 7x + 1. Thus a = 7 and b = 1."
            }
        ]
    },

    # Slide 5: 2.3 Exploring Linear Patterns — Constant Rate of Change
    {
        "id": 5,
        "title": "2.3 Exploring Linear Patterns & Rate of Change",
        "subtitle": "Discrete Step Differences and the Constant Slope Principle (NCERT Section 2.3)",
        "content": r"""
<p class="lead-p">The defining hallmark of all linear polynomials is their <strong>constant rate of change</strong>. If the input increases by equal steps, the output also changes by a fixed, constant amount. This constant step difference is identical to the coefficient $a$.</p>

<div class="theory-box">
  <h4>1. The First Difference Theorem</h4>
  <p>Let $P(x) = ax + b$. Consider evaluating $P(x)$ at consecutive integer values $x$ and $x + 1$:</p>
  <p class="highlight-eq">$$\Delta P = P(x + 1) - P(x) = [a(x + 1) + b] - [ax + b] = ax + a + b - ax - b = a$$</p>
  <p>Notice that the variable $x$ completely cancels out! The difference between any two consecutive values is <strong>always the constant $a$</strong>, regardless of the value of $x$.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Visualizing Step Ladders</h4>
    <p>For $P(x) = 3x + 2$:</p>
    <ul>
      <li>$P(1) = 3(1) + 2 = 5$</li>
      <li>$P(2) = 3(2) + 2 = 8 \quad (+3)$</li>
      <li>$P(3) = 3(3) + 2 = 11 \quad (+3)$</li>
      <li>$P(4) = 3(4) + 2 = 14 \quad (+3)$</li>
    </ul>
    <p>Every step forward by 1 unit in $x$ produces an exact vertical rise of 3 units in $P(x)$.</p>
  </div>
  <div class="card-item">
    <h4>Non-Linear Comparison</h4>
    <p>In contrast, for a quadratic polynomial $Q(x) = x^2$:</p>
    <ul>
      <li>$Q(1) = 1, \quad Q(2) = 4 \quad (+3)$</li>
      <li>$Q(3) = 9 \quad (+5)$</li>
      <li>$Q(4) = 16 \quad (+7)$</li>
    </ul>
    <p>The differences $\{3, 5, 7\}$ are changing! <em>Only linear polynomials possess a constant first difference.</em></p>
  </div>
</div>
""",
        "sim_type": "rate_of_change_stepper",
        "voice": "Here is the master secret of linear polynomials: their rate of change is absolutely constant! If you increase x by 1, P of x always increases by exactly a. Look at our step ladder simulator: every single step has the exact same height! In quadratic polynomials, the steps get taller and taller, but linear polynomials climb with unwavering constancy.",
        "checkpoints": [
            {
                "question": "For the linear polynomial P(x) = -4x + 9, what is the value of P(x + 1) - P(x)?",
                "options": ["+4", "-4", "+9", "0"],
                "correct": 1,
                "explanation": "For any linear polynomial P(x) = ax + b, the difference P(x + 1) - P(x) is always equal to the leading coefficient a. Here a = -4."
            },
            {
                "question": "If an output sequence is 11, 15, 19, 23, 27..., what is the constant rate of change a?",
                "options": ["2", "3", "4", "5"],
                "correct": 2,
                "explanation": "Rate of change = 15 - 11 = 19 - 15 = 4."
            }
        ]
    },

    # Slide 6: Exercise Set 2.3 — Word Problems & Sequences
    {
        "id": 6,
        "title": "Exercise Set 2.3: Pattern Sequences & Real Scenarios",
        "subtitle": "Formulating Linear Rules from Word Problems and Tabular Sequences",
        "content": r"""
<p class="lead-p">In Exercise Set 2.3, students apply the constant rate of change to construct linear models for everyday phenomena: mobile call plans, staircase heights, savings accounts, and utility bills.</p>

<div class="theory-box">
  <h4>1. The Fixed-Base + Variable-Rate Structure</h4>
  <p>Most real-world billing and measurement models naturally adopt the linear form $ax + b$:</p>
  <p class="highlight-eq">$$\text{Total Cost } C(x) = (\text{Rate per unit } a) \times x + (\text{Fixed Base Fee } b)$$</p>
  <ul>
    <li><strong>Taxi Meter:</strong> Base fare ₹30 plus ₹15 per km $\implies C(k) = 15k + 30$.</li>
    <li><strong>Water Tank Filling:</strong> Initial 100 litres plus 25 litres per minute $\implies V(t) = 25t + 100$.</li>
    <li><strong>Savings Growth:</strong> Initial piggy bank balance ₹250 plus weekly savings of ₹50 $\implies S(w) = 50w + 250$.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Example Problem: Cinema Group Discount</h4>
    <p>A theatre charges an annual membership of ₹150, after which movie tickets cost ₹80 each.</p>
    <p>1. Formulate the polynomial for $n$ tickets: $P(n) = 80n + 150$.</p>
    <p>2. Calculate total expenditure for 6 movies: $P(6) = 80(6) + 150 = 480 + 150 = ₹630$.</p>
    <p>3. If a student spent ₹950, how many movies did they watch? $80n + 150 = 950 \implies 80n = 800 \implies n = 10 \text{ movies}$.</p>
  </div>
  <div class="card-item">
    <h4>Inverse Inquiries</h4>
    <p>Using the linear model to solve for the input $x$ given the output $y$:</p>
    <p class="highlight-eq">$$x = \frac{y - b}{a}$$</p>
    <p>This simple inversion is the foundation for solving linear equations in one variable throughout algebra and science.</p>
  </div>
</div>
""",
        "sim_type": "real_world_cost_modeler",
        "voice": "Think of mobile tariffs, taxi fares, or water tanks: they all have a fixed starting value, plus a variable rate per unit! In algebra, the starting value is b, and the rate per unit is a! If an auto charges 30 rupees flag-down plus 15 rupees per kilometer, that is exactly 15k plus 30! Adjust the distance in our simulator to see the total cost calculated instantly.",
        "checkpoints": [
            {
                "question": "A gym charges a one-time registration fee of ₹500 and a monthly fee of ₹300. Which polynomial models total cost for m months?",
                "options": ["C(m) = 500m + 300", "C(m) = 300m + 500", "C(m) = 800m", "C(m) = 300m - 500"],
                "correct": 1,
                "explanation": "The monthly fee of ₹300 varies with m (300m), while the registration fee of ₹500 is fixed. Total cost is C(m) = 300m + 500."
            },
            {
                "question": "Using C(m) = 300m + 500, what is the cost of attending the gym for 8 months?",
                "options": ["₹2400", "₹2800", "₹2900", "₹3200"],
                "correct": 2,
                "explanation": "C(8) = 300(8) + 500 = 2400 + 500 = ₹2900."
            }
        ]
    },

    # Slide 7: 2.4 Linear Growth and Linear Decay
    {
        "id": 7,
        "title": "2.4 Linear Growth & Linear Decay",
        "subtitle": "Positive vs. Negative Slope: Accumulation vs. Depletion (NCERT Section 2.4)",
        "content": r"""
<p class="lead-p">The sign of the leading coefficient $a$ in $P(x) = ax + b$ dictates the entire directional behavior of the system. If $a > 0$, the quantity experiences <strong>linear growth</strong>. If $a < 0$, the quantity experiences <strong>linear decay</strong>.</p>

<div class="theory-box">
  <h4>1. The Sign of Coefficient a</h4>
  <div class="grid-2col">
    <div class="card-item" style="border-left: 3px solid #10b981;">
      <h5 style="color:#34d399;">Linear Growth ($a > 0$)</h5>
      <p>As $x$ increases, $P(x)$ steadily <strong>increases</strong>.</p>
      <p>Rate of change is positive: $\Delta P > 0$.</p>
      <p>Examples: Height of a growing bamboo stalk, accumulation of simple interest, filling a reservoir.</p>
      <p class="highlight-eq">$$H(t) = +5t + 20 \quad (\text{Grows by 5 cm/day})$$</p>
    </div>
    <div class="card-item" style="border-left: 3px solid #f43f5e;">
      <h5 style="color:#fb7185;">Linear Decay ($a < 0$)</h5>
      <p>As $x$ increases, $P(x)$ steadily <strong>decreases</strong>.</p>
      <p>Rate of change is negative: $\Delta P < 0$.</p>
      <p>Examples: Fuel remaining in a vehicle tank, burning length of a candle, melting ice block.</p>
      <p class="highlight-eq">$$F(d) = -0.08d + 40 \quad (\text{Loses 0.08 L/km})$$</p>
    </div>
  </div>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Depletion to Zero (Extinction Event)</h4>
    <p>In linear decay models, finding when the resource is completely exhausted requires finding the zero of the polynomial:</p>
    <p class="highlight-eq">$$ax + b = 0 \implies x_{\text{empty}} = -\frac{b}{a}$$</p>
    <p>For $F(d) = -0.08d + 40$:<br>
    $-0.08d + 40 = 0 \implies 0.08d = 40 \implies d = \frac{40}{0.08} = 500 \text{ km}$.</p>
  </div>
  <div class="card-item">
    <h4>Visual Trajectory Comparison</h4>
    <p>On a Cartesian plane:</p>
    <ul>
      <li>$a > 0$: The line slopes <strong>upward</strong> from left to right.</li>
      <li>$a < 0$: The line slopes <strong>downward</strong> from left to right.</li>
      <li>$a = 0$: The line is completely <strong>horizontal</strong> (constant, no growth).</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "growth_decay_comparator",
        "voice": "Look at what happens when the sign of a changes! When a is positive, the line climbs upward—that is linear growth, like a plant growing or savings increasing. But when a is negative, the line descends downward—that is linear decay, like water draining from a tub or fuel burning in a car! Toggle between growth and decay in our simulator to witness the stark contrast.",
        "checkpoints": [
            {
                "question": "A candle is 30 cm tall and burns down at a steady rate of 2.5 cm per hour. Which linear polynomial describes its height h after t hours?",
                "options": ["h(t) = 2.5t + 30", "h(t) = -2.5t + 30", "h(t) = 30t - 2.5", "h(t) = -30t + 2.5"],
                "correct": 1,
                "explanation": "Since the candle decreases in height, the rate is negative: a = -2.5. The initial height is b = 30. Therefore, h(t) = -2.5t + 30."
            },
            {
                "question": "After how many hours will the candle be completely burned down (h = 0)?",
                "options": ["10 hours", "12 hours", "15 hours", "20 hours"],
                "correct": 1,
                "explanation": "Set h(t) = 0: -2.5t + 30 = 0 => 2.5t = 30 => t = 30 / 2.5 = 12 hours."
            }
        ]
    },

    # Slide 8: Exercise Set 2.4 — Linear Dynamics & Half-Life Comparisons
    {
        "id": 8,
        "title": "Exercise Set 2.4: Real Dynamics of Depletion & Accumulation",
        "subtitle": "Solving Decay Intercepts, Fuel Gauges and Tank Drainage Problems",
        "content": r"""
<p class="lead-p">Exercise Set 2.4 tests the application of linear growth and decay to practical real-world contexts, emphasizing domain constraints (where physical variables like time or fuel cannot be negative).</p>

<div class="theory-box">
  <h4>1. Physical Domain & Range Restrictions</h4>
  <p>In pure mathematics, a linear polynomial $P(x) = ax + b$ is defined for all real numbers $x \in (-\infty, \infty)$. However, in real-world physical models:</p>
  <ul>
    <li>Time $t \ge 0$ (time cannot run backward).</li>
    <li>Remaining volume $V(t) \ge 0$ (a tank cannot hold negative liquid).</li>
    <li>Distance $d \ge 0$.</li>
  </ul>
  <p class="highlight-eq">$$\text{Valid Domain: } 0 \le t \le t_{\text{exhaustion}}$$</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Example: Overhead Water Tank Drain</h4>
    <p>A full tank holds 1200 litres of water. A valve at the bottom drains water at a constant rate of 40 litres per minute.</p>
    <p>1. <strong>Model:</strong> $V(t) = -40t + 1200$.</p>
    <p>2. <strong>Water at $t = 15 \text{ min}$?</strong><br>
    $V(15) = -40(15) + 1200 = -600 + 1200 = 600 \text{ L}$.</p>
    <p>3. <strong>Empty Time?</strong><br>
    $-40t + 1200 = 0 \implies 40t = 1200 \implies t = 30 \text{ minutes}$.</p>
  </div>
  <div class="card-item">
    <h4>Linear vs. Non-Linear Decay</h4>
    <p>Linear decay decreases by the <em>same fixed quantity</em> in every unit interval ($\Delta V = -40 \text{ L/min}$).</p>
    <p>In contrast, radioactive decay or cooling coffee loses a fixed <em>percentage</em> (exponential decay), which slows down over time.</p>
    <p class="highlight-eq">$$\text{Linear: Constant Absolute Loss } (\Delta y = a)$$</p>
  </div>
</div>
""",
        "sim_type": "tank_drainage_simulator",
        "voice": "Always pay attention to physical boundaries! A water tank can never hold negative water, and time cannot be negative. When a tank drains at 40 liters a minute, its volume is minus 40 t plus 1200. At 30 minutes, the tank hits zero, and the model stops! Run the drainage simulation to watch the water level drop linearly to zero.",
        "checkpoints": [
            {
                "question": "A water tank holds 800 L and drains at 25 L/min. How much water remains after 20 minutes?",
                "options": ["200 L", "300 L", "400 L", "500 L"],
                "correct": 1,
                "explanation": "V(20) = -25(20) + 800 = -500 + 800 = 300 litres."
            },
            {
                "question": "How long will it take for the 800 L tank to become completely empty?",
                "options": ["28 minutes", "30 minutes", "32 minutes", "36 minutes"],
                "correct": 2,
                "explanation": "Set V(t) = 0: -25t + 800 = 0 => 25t = 800 => t = 800 / 25 = 32 minutes."
            }
        ]
    },

    # Slide 9: 2.5 Linear Relationships — Two-Variable Functions
    {
        "id": 9,
        "title": "2.5 Linear Relationships & Two-Variable Form",
        "subtitle": "Connecting Polynomials P(x) to Equations y = ax + b (NCERT Section 2.5)",
        "content": r"""
<p class="lead-p">When we set the output of a linear polynomial equal to a dependent variable $y$, we establish a <strong>linear relationship</strong> between two co-varying quantities: $y = ax + b$. Every pair of values $(x, y)$ that satisfies this equation corresponds to a point on the two-dimensional Cartesian plane.</p>

<div class="theory-box">
  <h4>1. Independent vs. Dependent Variables</h4>
  <p>In a linear relationship $y = ax + b$:</p>
  <ul>
    <li><strong>Independent Variable ($x$):</strong> The input quantity that can be freely chosen or varied (e.g., time, distance, hours worked). Conventionally plotted along the horizontal axis (Abscissa).</li>
    <li><strong>Dependent Variable ($y$):</strong> The output quantity whose value depends on $x$ (e.g., total fee, temperature, displacement). Conventionally plotted along the vertical axis (Ordinate).</li>
    <li><strong>Relation Rule:</strong> Every single input $x$ produces one, and only one, output $y$.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Table of Ordered Pairs</h4>
    <p>For the relationship $y = 2x + 1$:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:12px; text-align:center;">
      <tr style="border-bottom:1px solid #475569;">
        <th style="padding:4px; color:#38bdf8;">$x$</th>
        <td>$-2$</td><td>$-1$</td><td>$0$</td><td>$1$</td><td>$2$</td><td>$3$</td>
      </tr>
      <tr>
        <th style="padding:4px; color:#34d399;">$y$</th>
        <td>$-3$</td><td>$-1$</td><td>$1$</td><td>$3$</td><td>$5$</td><td>$7$</td>
      </tr>
    </table>
    <p style="margin-top:8px;">Ordered pairs: $\{(-2, -3), (-1, -1), (0, 1), (1, 3), (2, 5), (3, 7)\}$.</p>
  </div>
  <div class="card-item">
    <h4>3. The Intercepts of a Line</h4>
    <ul>
      <li><strong>y-intercept:</strong> The point where the relationship crosses the y-axis (set $x = 0$):<br>
      $y = a(0) + b = b \implies (0, b)$.</li>
      <li><strong>x-intercept:</strong> The point where the relationship crosses the x-axis (set $y = 0$):<br>
      $0 = ax + b \implies x = -\frac{b}{a} \implies \left(-\frac{b}{a}, 0\right)$.</li>
    </ul>
    <p class="highlight-eq">$$\text{Intercepts determine the line completely!}$$</p>
  </div>
</div>
""",
        "sim_type": "ordered_pair_generator",
        "voice": "When you write y equals a x plus b, you are connecting two quantities that move together! The variable x is your independent choice, and y is the dependent result. Look at the y-intercept: when x is zero, y is simply b! And when y is zero, x is minus b over a. These two anchor points fix the line in space. Try changing a and b to watch the ordered pairs update.",
        "checkpoints": [
            {
                "question": "What is the y-intercept of the linear relationship y = 3x - 7?",
                "options": ["(0, 3)", "(0, -7)", "(-7, 0)", "(3, 0)"],
                "correct": 1,
                "explanation": "The y-intercept occurs when x = 0. Substituting x = 0 yields y = 3(0) - 7 = -7. The coordinates are (0, -7)."
            },
            {
                "question": "Which of the following points lies on the line y = 4x + 2?",
                "options": ["(1, 5)", "(2, 10)", "(3, 12)", "(0, 4)"],
                "correct": 1,
                "explanation": "Substitute x = 2: y = 4(2) + 2 = 8 + 2 = 10. The point (2, 10) satisfies the relationship."
            }
        ]
    },

    # Slide 10: Exercise Set 2.5 — Intercepts & Coordinate Pairs
    {
        "id": 10,
        "title": "Exercise Set 2.5: Determining Intercepts & Solving Pairs",
        "subtitle": "Collinearity Verification, Coordinate Algebra and Two-Point Form (NCERT Section 2.5)",
        "content": r"""
<p class="lead-p">In Exercise Set 2.5, students verify whether given coordinate points are <strong>collinear</strong> (lie on the exact same straight line), calculate intercepts, and reconstruct the governing linear relationship from two known data points.</p>

<div class="theory-box">
  <h4>1. Finding the Linear Relationship from Two Points</h4>
  <p>Any two distinct points $(x_1, y_1)$ and $(x_2, y_2)$ uniquely define a straight line:</p>
  <p class="highlight-eq">$$\text{Slope (Leading Coefficient) } a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$</p>
  <p>Once $a$ is found, substitute either point to solve for $b$:</p>
  <p class="highlight-eq">$$b = y_1 - a \cdot x_1$$</p>
  <p><strong>Example:</strong> Find the line passing through $(2, 7)$ and $(5, 16)$:<br>
  $a = \frac{16 - 7}{5 - 2} = \frac{9}{3} = 3$.<br>
  $b = 7 - 3(2) = 7 - 6 = 1$.<br>
  Hence, the relationship is $y = 3x + 1$.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Collinearity Test</h4>
    <p>Three points $A, B, C$ are collinear if the slope between $A$ and $B$ equals the slope between $B$ and $C$:</p>
    <p class="highlight-eq">$$\frac{y_2 - y_1}{x_2 - x_1} = \frac{y_3 - y_2}{x_3 - x_2}$$</p>
    <p>If the slopes are unequal, the points form a triangle rather than a straight line.</p>
  </div>
  <div class="card-item">
    <h4>3. Temperature Conversion Model</h4>
    <p>The relationship between Celsius ($C$) and Fahrenheit ($F$) is a celebrated linear relationship:</p>
    <p class="highlight-eq">$$F = \frac{9}{5}C + 32$$</p>
    <p>Slope $a = \frac{9}{5} = 1.8$, and $y$-intercept $b = 32$.</p>
    <p>At what temperature do they agree? $C = \frac{9}{5}C + 32 \implies -\frac{4}{5}C = 32 \implies C = -40^\circ$.</p>
  </div>
</div>
""",
        "sim_type": "two_point_slope_calculator",
        "voice": "Did you know that any two points on a plane lock down a unique line? You find the slope a by dividing the change in y by the change in x: delta y over delta x! Look at Celsius and Fahrenheit: F equals 9 fifths C plus 32! It is a pure linear relationship with a slope of 1.8 and an intercept of 32! Drag the two points in our simulator to see the slope calculated live.",
        "checkpoints": [
            {
                "question": "What is the slope a of the line passing through (1, 3) and (4, 15)?",
                "options": ["3", "4", "5", "6"],
                "correct": 1,
                "explanation": "Slope a = (y₂ - y₁) / (x₂ - x₁) = (15 - 3) / (4 - 1) = 12 / 3 = 4."
            },
            {
                "question": "Using the slope a = 4 and point (1, 3), what is the equation of the line?",
                "options": ["y = 4x + 1", "y = 4x - 1", "y = 4x + 3", "y = 4x - 3"],
                "correct": 1,
                "explanation": "y = ax + b => 3 = 4(1) + b => b = 3 - 4 = -1. Therefore, y = 4x - 1."
            }
        ]
    },

    # Slide 11: 2.6 Visualising Linear Relationships — The Straight Line Graph
    {
        "id": 11,
        "title": "2.6 Visualising Linear Relationships",
        "subtitle": "The Geometry of the Straight Line, Slope Meaning & Cartesian Graphing (NCERT Section 2.6)",
        "content": r"""
<p class="lead-p">The word <strong>linear</strong> originates directly from the word <em>line</em>. The geometric graph of any relationship of the form $y = ax + b$ on a Cartesian coordinate plane is <strong>always an unbroken straight line</strong>. This is why polynomials of degree 1 are called linear!</p>

<div class="theory-box">
  <h4>1. Geometric Interpretation of Parameters a and b</h4>
  <ul>
    <li><strong>The Slope $a$ (Gradient):</strong> Measures the steepness and direction of the line.
      <ul>
        <li>$a > 0$: Slopes upward (growth). Larger $|a|$ means a steeper climb.</li>
        <li>$a < 0$: Slopes downward (decay).</li>
        <li>$a = 0$: Horizontal line $y = b$.</li>
        <li>$a = \text{Rise} / \text{Run} = \Delta y / \Delta x$.</li>
      </ul>
    </li>
    <li><strong>The y-intercept $b$:</strong> The exact height at which the line slices across the vertical axis (at $x = 0$). Moving $b$ shifts the entire line vertically up or down without changing its tilt.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Parallel Lines & Identical Slopes</h4>
    <p>Two linear lines are <strong>parallel</strong> if and only if they possess identical slopes ($a_1 = a_2$) but different intercepts ($b_1 \neq b_2$):</p>
    <ul>
      <li>$y = 2x + 3$</li>
      <li>$y = 2x - 5$</li>
      <li>$y = 2x + 8$</li>
    </ul>
    <p>These lines will never intersect, representing systems that maintain a constant gap forever.</p>
  </div>
  <div class="card-item">
    <h4>3. Graphing via the Two-Point Rule</h4>
    <p>Euclid's First Postulate states: <em>A straight line may be drawn from any one point to any other point.</em></p>
    <p class="highlight-eq">$$\text{You only need TWO distinct points to graph a linear polynomial!}$$</p>
    <p>The easiest two points to choose are always the <strong>y-intercept $(0, b)$</strong> and the <strong>x-intercept $(-b/a, 0)$</strong>.</p>
  </div>
</div>
""",
        "sim_type": "interactive_line_grapher",
        "voice": "This is why they are called linear polynomials: their graph is always a straight line! Look at the two controls: the slope a tilts the line, making it steeper or flatter, while the intercept b slides the entire line up or down like an elevator! Adjust the sliders on the screen to see how the line dances on the Cartesian grid.",
        "checkpoints": [
            {
                "question": "What is the geometric shape of the graph of P(x) = -2x + 5 on a coordinate grid?",
                "options": ["A parabola", "A straight line sloping downward", "A circle", "A horizontal line"],
                "correct": 1,
                "explanation": "Since P(x) is of degree 1 with a = -2 < 0, its graph is a straight line sloping downward from left to right."
            },
            {
                "question": "Which of the following lines is PARALLEL to the line y = 5x - 3?",
                "options": ["y = -5x + 3", "y = 5x + 7", "y = (1/5)x - 3", "y = 3x - 5"],
                "correct": 1,
                "explanation": "Parallel lines must have the exact same slope a. The line y = 5x + 7 has slope a = 5, matching y = 5x - 3."
            }
        ]
    },

    # Slide 12: Exercise Set 2.6 — Graph Plotting & Graphical Intersections
    {
        "id": 12,
        "title": "Exercise Set 2.6: Graph Plotting & Graphical Solutions",
        "subtitle": "Plotting from Tables, Finding Points of Intersection and Break-Even Points",
        "content": r"""
<p class="lead-p">In Exercise Set 2.6, students plot lines on graph paper, read coordinates of intersection between two competing linear models, and determine <strong>break-even points</strong> in economic and physical systems.</p>

<div class="theory-box">
  <h4>1. The Graphical Intersection of Two Lines</h4>
  <p>Suppose two rival phone companies offer different rate plans:</p>
  <ul>
    <li><strong>Plan Alpha:</strong> $y_1 = 2x + 10$ &emsp; (Lower base, higher per-GB rate)</li>
    <li><strong>Plan Beta:</strong> $y_2 = x + 20$ &emsp; (Higher base, lower per-GB rate)</li>
  </ul>
  <p>To find the <strong>break-even point</strong> where both plans cost exactly the same, we set $y_1 = y_2$:</p>
  <p class="highlight-eq">$$2x + 10 = x + 20 \implies 2x - x = 20 - 10 \implies x = 10 \text{ GB}$$</p>
  <p>For $x = 10$, $y = 2(10) + 10 = ₹30$. The point of intersection on the graph is <strong>$(10, 30)$</strong>.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Decision Regions</h4>
    <ul>
      <li>For $x < 10 \text{ GB}$: Line $y_1$ lies below $y_2$, so <strong>Plan Alpha is cheaper</strong>.</li>
      <li>At $x = 10 \text{ GB}$: Both plans cost the exact same (₹30).</li>
      <li>For $x > 10 \text{ GB}$: Line $y_2$ lies below $y_1$, so <strong>Plan Beta is cheaper</strong>.</li>
    </ul>
    <p>Graphs provide instant visual answers to real economic decisions!</p>
  </div>
  <div class="card-item">
    <h4>3. Graphical Meaning of the Zero</h4>
    <p>The zero of the polynomial $P(x) = ax + b$ is simply the <strong>x-coordinate where the graph cuts the x-axis</strong> (where $y = 0$).</p>
    <p class="highlight-eq">$$\text{Zero of } P(x) \iff x\text{-intercept of } y = P(x)$$</p>
    <p>Geometry and algebra unite into one seamless science.</p>
  </div>
</div>
""",
        "sim_type": "break_even_intersection_sim",
        "voice": "When two lines cross on a graph, that intersection point is a magical moment: it is the break-even point where both competing options cost the exact same! Below 10 gigabytes, Plan Alpha is cheaper because its line is lower. Above 10 gigabytes, Plan Beta is cheaper! Use our Break-Even Simulator to slide the data usage and see which plan wins.",
        "checkpoints": [
            {
                "question": "At what point do the lines y = 3x + 4 and y = x + 10 intersect?",
                "options": ["(2, 10)", "(3, 13)", "(4, 16)", "(3, 11)"],
                "correct": 1,
                "explanation": "Set 3x + 4 = x + 10 => 2x = 6 => x = 3. Then y = 3 + 10 = 13. The intersection point is (3, 13)."
            },
            {
                "question": "If line 1 is below line 2 on a cost graph, what does it mean for the consumer?",
                "options": ["Line 1 represents higher cost", "Line 1 represents lower cost", "Both lines have the same cost", "The lines cannot be compared"],
                "correct": 1,
                "explanation": "The vertical y-axis represents cost. A line that is physically lower on the graph has a smaller y-value, representing a cheaper, lower cost."
            }
        ]
    },

    # Slide 13: End-of-Chapter Exercises — Advanced Word Problems
    {
        "id": 13,
        "title": "End-of-Chapter Exercises: Multi-Step Word Problems",
        "subtitle": "Combining Rates, Ages, Perimeter Constraints & Digit Problems (NCERT Exercises)",
        "content": r"""
<p class="lead-p">The End-of-Chapter exercises present rich, multi-step problem-solving scenarios that connect linear polynomials to geometric shapes, perimeter constraints, speed-distance-time problems, and age relationships.</p>

<div class="theory-box">
  <h4>1. Geometry & Perimeter Constraint Problems</h4>
  <p><strong>Problem:</strong> The length of a rectangle is 5 cm more than twice its width. If its perimeter is 46 cm, find its dimensions.</p>
  <ol>
    <li>Let width $= w$ cm.</li>
    <li>Length $= 2w + 5$ cm (a linear polynomial in $w$!).</li>
    <li>Perimeter formula: $P = 2(\text{Length} + \text{Width}) = 2[(2w + 5) + w] = 2(3w + 5) = 6w + 10$.</li>
    <li>Set equal to 46: $6w + 10 = 46 \implies 6w = 36 \implies w = 6 \text{ cm}$.</li>
    <li>Length $= 2(6) + 5 = 17 \text{ cm}$. Check: $2(17 + 6) = 2(23) = 46 \text{ cm}$ ✓.</li>
  </ol>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Age Relationship Problems</h4>
    <p>A mother is 3 times as old as her son. In 12 years, her age will be 6 years more than twice his age.</p>
    <ul>
      <li>Present ages: Son $= s$, Mother $= 3s$.</li>
      <li>In 12 years: Son $= s + 12$, Mother $= 3s + 12$.</li>
      <li>Condition: $3s + 12 = 2(s + 12) + 6 = 2s + 24 + 6 = 2s + 30$.</li>
      <li>$3s - 2s = 30 - 12 \implies s = 18 \text{ years}$. Mother $= 54 \text{ years}$.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>3. Speed, Distance & Simultaneous Travel</h4>
    <p>Two cyclists start 90 km apart and ride toward each other at speeds of $v$ and $v + 5$ km/h. They meet in 2 hours.</p>
    <p class="highlight-eq">$$\text{Total Distance} = 2v + 2(v + 5) = 4v + 10 = 90$$</p>
    <p>$4v = 80 \implies v = 20 \text{ km/h}$, and the second cyclist rides at 25 km/h.</p>
  </div>
</div>
""",
        "sim_type": "rectangle_perimeter_solver",
        "voice": "Algebra shows its true power when solving practical geometric puzzles! Look at our rectangle model: length is 2w plus 5! When we express perimeter in terms of width w, we get the linear expression 6w plus 10. Drag the width slider to watch the rectangle rescale and see the perimeter calculate in real time.",
        "checkpoints": [
            {
                "question": "The perimeter of a rectangle is given by P(w) = 6w + 10. If the perimeter is 46 cm, what is the width w?",
                "options": ["5 cm", "6 cm", "7 cm", "8 cm"],
                "correct": 1,
                "explanation": "6w + 10 = 46 => 6w = 36 => w = 6 cm."
            },
            {
                "question": "If Rahul's present age is x, what was his age 7 years ago?",
                "options": ["7 - x", "x + 7", "x - 7", "7x"],
                "correct": 2,
                "explanation": "His age 7 years ago was x - 7 years."
            }
        ]
    },

    # Slide 14: End-of-Chapter Exercises — Speed, Ratios & Number Riddles
    {
        "id": 14,
        "title": "End-of-Chapter Exercises: Number Riddles & Ratios",
        "subtitle": "Two-Digit Number Reversals, Consecutive Integers and Ratio Partitioning",
        "content": r"""
<p class="lead-p">Classic algebra riddles—such as consecutive integers summing to a target, or two-digit numbers whose digits swap—rely directly on the structure of linear polynomials.</p>

<div class="theory-box">
  <h4>1. Two-Digit Number Structure Theorem</h4>
  <p>In our base-10 decimal place value system, a two-digit number with tens digit $t$ and units digit $u$ has the numerical value:</p>
  <p class="highlight-eq">$$N = 10t + u$$</p>
  <p>If the sum of digits is 9 ($u = 9 - t$), the number is a linear polynomial in $t$:</p>
  <p class="highlight-eq">$$N(t) = 10t + (9 - t) = 9t + 9$$</p>
  <p>When the digits are reversed, the new number is $N_{\text{rev}} = 10u + t = 10(9 - t) + t = 90 - 9t$.</p>
  <p>If the reversed number is 27 greater than the original: $(90 - 9t) - (9t + 9) = 27 \implies 81 - 18t = 27 \implies 18t = 54 \implies t = 3$. Units digit $u = 6$. The original number is <strong>36</strong>!</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Consecutive Integer Riddles</h4>
    <p>The sum of three consecutive integers is 72. Find the numbers.</p>
    <ul>
      <li>Let the integers be $x, x+1, x+2$.</li>
      <li>Sum: $x + (x + 1) + (x + 2) = 3x + 3$.</li>
      <li>$3x + 3 = 72 \implies 3x = 69 \implies x = 23$.</li>
      <li>The integers are $23, 24, 25$. Check: $23 + 24 + 25 = 72$ ✓.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>3. Ratio Partitioning</h4>
    <p>Two numbers are in the ratio $5 : 3$. If they differ by 18, find the numbers.</p>
    <p>Let numbers be $5x$ and $3x$.</p>
    <p class="highlight-eq">$$\text{Difference} = 5x - 3x = 2x = 18 \implies x = 9$$</p>
    <p>The numbers are $5(9) = 45$ and $3(9) = 27$.</p>
  </div>
</div>
""",
        "sim_type": "two_digit_reversal_sim",
        "voice": "Place value is linear algebra in disguise! Any two-digit number is 10 times the tens digit plus the units digit. When you reverse the digits, you get 10 times the units digit plus the tens digit! Look at 36: reverse it, and you get 63. The difference is 27! Test different digit combinations in our interactive place value simulator.",
        "checkpoints": [
            {
                "question": "The sum of three consecutive multiples of 5 is 135. What is the smallest of these multiples?",
                "options": ["35", "40", "45", "50"],
                "correct": 1,
                "explanation": "Let multiples be 5x, 5x + 5, 5x + 10. Sum = 15x + 15 = 135 => 15x = 120 => x = 8. Smallest is 5(8) = 40. (Multiples are 40, 45, 50; 40 + 45 + 50 = 135)."
            },
            {
                "question": "A two-digit number has tens digit t and units digit u. What is its algebraic expression?",
                "options": ["t + u", "10t + u", "10(t + u)", "tu"],
                "correct": 1,
                "explanation": "By decimal place value, the tens digit represents 10t and units digit represents u. The value is 10t + u."
            }
        ]
    },

    # Slide 15: Chapter Summary — Synthesizing Linear Polynomials
    {
        "id": 15,
        "title": "Chapter Summary: Core Concepts & Formulas",
        "subtitle": "Comprehensive Review of Definitions, Theorems and Analytical Tools",
        "content": r"""
<p class="lead-p">Here is the unified mathematical map of Chapter 2: Introduction to Linear Polynomials. Review every core definition, algebraic formula, and graphical property before proceeding to the mastery examinations.</p>

<div class="theory-box">
  <h4>1. Master Summary Matrix</h4>
  <table style="width:100%; border-collapse:collapse; font-size:12px; line-height:1.6;">
    <tr style="border-bottom:2px solid #6366f1; color:#38bdf8;">
      <th style="padding:6px; text-align:left;">Concept</th>
      <th style="padding:6px; text-align:left;">Mathematical Formula / Form</th>
      <th style="padding:6px; text-align:left;">Significance</th>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px; font-weight:bold; color:#fff;">Standard Form</td>
      <td style="padding:6px; color:#a5b4fc;">$P(x) = ax + b, \quad a \neq 0$</td>
      <td style="padding:6px;">Degree is strictly 1. $a$ is leading coefficient, $b$ is constant.</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px; font-weight:bold; color:#fff;">Zero of Polynomial</td>
      <td style="padding:6px; color:#a5b4fc;">$x = -\frac{b}{a}$</td>
      <td style="padding:6px;">Unique root where $P(x) = 0$ and graph cuts x-axis.</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px; font-weight:bold; color:#fff;">Rate of Change</td>
      <td style="padding:6px; color:#a5b4fc;">$\Delta P = P(x+1) - P(x) = a$</td>
      <td style="padding:6px;">Constant first difference across all inputs.</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px; font-weight:bold; color:#fff;">Linear Growth / Decay</td>
      <td style="padding:6px; color:#a5b4fc;">$a > 0 \implies \text{Growth}; \quad a < 0 \implies \text{Decay}$</td>
      <td style="padding:6px;">Governs upward vs. downward trajectory.</td>
    </tr>
    <tr style="border-bottom:1px solid #334155;">
      <td style="padding:6px; font-weight:bold; color:#fff;">Slope Formula</td>
      <td style="padding:6px; color:#a5b4fc;">$a = \frac{y_2 - y_1}{x_2 - x_1}$</td>
      <td style="padding:6px;">Slope calculated from any two points $(x_1, y_1), (x_2, y_2)$.</td>
    </tr>
    <tr>
      <td style="padding:6px; font-weight:bold; color:#fff;">Cartesian Graph</td>
      <td style="padding:6px; color:#a5b4fc;">Straight line with y-intercept $(0, b)$</td>
      <td style="padding:6px;">Geometric representation of linear relationship.</td>
    </tr>
  </table>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Key Error Traps to Avoid</h4>
    <ul>
      <li>Never divide by zero: $a \neq 0$ is strictly required for linearity.</li>
      <li>Variables with fractional or negative exponents (like $\sqrt{x}$ or $1/x$) are <strong>not polynomials</strong>.</li>
      <li>Do not confuse $P(x)$ (an expression) with $P(x) = 0$ (an equation).</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Forward Connection to Class 9 & 10</h4>
    <p>This chapter is the direct stepping stone to:</p>
    <ul>
      <li>Linear Equations in Two Variables ($ax + by + c = 0$).</li>
      <li>Quadratic Polynomials ($ax^2 + bx + c$).</li>
      <li>Coordinate Geometry and Calculus slopes ($dy/dx$).</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "chapter_summary_matrix",
        "voice": "Congratulations on completing all lessons of Chapter 2! Take a moment to review this comprehensive summary matrix. Remember: standard form is a x plus b, the zero is minus b over a, the first difference is always a, and the graph is an unbroken straight line. You are now fully prepared for the four mastery quiz challenges!",
        "checkpoints": [
            {
                "question": "What is the degree of a non-zero constant polynomial such as P(x) = 9?",
                "options": ["1", "0", "Undefined", "9"],
                "correct": 1,
                "explanation": "A constant polynomial P(x) = 9 can be written as 9x⁰, so its degree is 0. (A linear polynomial has degree 1)."
            },
            {
                "question": "What is the unique zero of the linear polynomial P(x) = -6x + 24?",
                "options": ["x = -4", "x = 4", "x = 6", "x = -6"],
                "correct": 1,
                "explanation": "Set -6x + 24 = 0 => 6x = 24 => x = 4."
            }
        ]
    },

    # Slide 16: Historical Journey — Diophantus, Brahmagupta & Al-Khwarizmi
    {
        "id": 16,
        "title": "A Pinch of History: The Evolution of Algebra",
        "subtitle": "From Diophantus's Syncopated Shorthand to Brahmagupta and Al-Khwarizmi",
        "content": r"""
<p class="lead-p">The algebra of linear polynomials did not appear overnight. It was forged over three millennia through the brilliant insights of ancient Egyptian scribes, Indian astronomers, Greek mathematicians, and Baghdad scholars.</p>

<div class="theory-box">
  <h4>1. Landmarks in the History of Algebra</h4>
  <ul>
    <li><strong>Rhind Mathematical Papyrus (Egypt, c. 1650 BCE):</strong> Scribe Ahmes solved "Aha" (quantity) problems: <em>"Aha, its whole, its seventh, it makes 19"</em> $\implies x + \frac{x}{7} = 19$, the world's oldest linear equations!</li>
    <li><strong>Diophantus of Alexandria (c. 250 CE):</strong> Author of <em>Arithmetica</em>, introduced syncopated abbreviations for unknown quantities and powers, moving away from purely verbal prose.</li>
    <li><strong>Brahmagupta (India, 628 CE):</strong> In the <em>Brahmasphutasiddhanta</em>, formulated rigorous arithmetic rules for <strong>zero (shunya)</strong> and <strong>negative numbers (debts / rina)</strong>, enabling generalized linear forms $ax + b$ without restriction.</li>
    <li><strong>Muhammad ibn Musa al-Khwarizmi (Baghdad, 820 CE):</strong> Wrote <em>Al-Kitab al-mukhtasar fi hisab al-jabr wal-muqabala</em>. The word <strong>al-jabr</strong> (restoration / transposing negative terms) gave birth to our modern word <strong>Algebra</strong>!</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Brahmagupta's Linear Equation Rule</h4>
    <p>Brahmagupta gave the universal poetic rule for solving linear equations $ax + b = cx + d$:</p>
    <blockquote style="font-style:italic; border-left:3px solid #10b981; padding-left:8px;">
      "The difference between the known quantities divided by the difference between the unknowns gives the value of the unknown."
    </blockquote>
    <p class="highlight-eq">$$x = \frac{d - b}{a - c}$$</p>
  </div>
  <div class="card-item">
    <h4>René Descartes & The Cartesian Bridge (1637)</h4>
    <p>French philosopher René Descartes fused algebra and geometry by introducing the $(x, y)$ coordinate plane in <em>La Géométrie</em>, proving that every linear algebraic polynomial corresponds to a straight geometric line.</p>
  </div>
</div>
""",
        "sim_type": "historical_timeline_stepper",
        "voice": "The story of algebra spans civilizations! From Egyptian scribes solving Aha riddles 3600 years ago, to Brahmagupta in India defining operations on negative numbers and zero, to Al-Khwarizmi in Baghdad whose book gave us the very name Algebra! And finally Descartes connected algebra with coordinate geometry. Enjoy our interactive historical timeline!",
        "checkpoints": [
            {
                "question": "Which ancient civilization wrote the Rhind Papyrus featuring 'Aha' linear problems?",
                "options": ["Ancient Rome", "Ancient Egypt", "Ancient Greece", "Babylonia"],
                "correct": 1,
                "explanation": "The Rhind Mathematical Papyrus was written in Ancient Egypt around 1650 BCE by the scribe Ahmes."
            },
            {
                "question": "From which Arabic term in Al-Khwarizmi's book title does our modern word 'Algebra' derive?",
                "options": ["Al-Muqabala", "Al-Jabr", "Algorism", "Al-Kemi"],
                "correct": 1,
                "explanation": "Algebra comes from 'al-jabr', meaning restoration or transposing negative terms to the other side of an equation."
            }
        ]
    },

    # Slide 17: Dedicated Quiz Challenge 1 (Questions 1 to 10)
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Fundamentals & Degree",
        "subtitle": "10 Diagnostic Questions on Polynomial Definitions, Coefficients and Standard Form",
        "content": r"""
<p class="lead-p">Welcome to Quiz Challenge I! Test your foundational mastery of polynomial definitions, degree 1 classification, standard form $ax + b$, and parameter identification. Select your answers and click <strong>View Solution</strong> to examine the complete mathematical explanation.</p>
<div id="quizContainer1" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge 1! Let us test your foundational understanding of linear polynomials, degree, and standard form. Work through each question carefully, and open View Solution for step-by-step guidance.",
        "quiz_range": [1, 10]
    },

    # Slide 18: Dedicated Quiz Challenge 2 (Questions 11 to 20)
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Patterns & Rate of Change",
        "subtitle": "10 Diagnostic Questions on Constant Differences, Sequences and Zero Finding",
        "content": r"""
<p class="lead-p">Quiz Challenge II focuses on finding zeroes of linear polynomials ($x = -b/a$), analyzing arithmetic sequences, determining constant first differences, and modeling linear tables.</p>
<div id="quizContainer2" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Time for Quiz Challenge 2! Here we test your mastery of roots, zeroes, and constant rates of change. Select your options and verify your derivations using the View Solution buttons.",
        "quiz_range": [11, 20]
    },

    # Slide 19: Dedicated Quiz Challenge 3 (Questions 21 to 30)
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Growth, Decay & Relationships",
        "subtitle": "10 Diagnostic Questions on Positive/Negative Slopes, Drainage and Intercepts",
        "content": r"""
<p class="lead-p">Quiz Challenge III assesses real-world applications of linear growth ($a > 0$) and decay ($a < 0$), physical depletion time, coordinate pairs $(x, y)$, and intercept calculation.</p>
<div id="quizContainer3" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge 3! Put your knowledge of linear growth, decay, depletion events, and coordinate intercepts to work. Solve each problem with care and inspect the detailed solutions.",
        "quiz_range": [21, 30]
    },

    # Slide 20: Dedicated Quiz Challenge 4 (Questions 31 to 40)
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Graphs, Word Problems & History",
        "subtitle": "10 Diagnostic Questions on Straight Line Graphs, Break-Even Points and Ancient History",
        "content": r"""
<p class="lead-p">Congratulations on reaching the final mastery examination! Challenge IV covers Cartesian graphing, parallel slope conditions, break-even intersections, multi-step word problems, and historical mathematical landmarks.</p>
<div id="quizContainer4" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "You have reached the final mastery challenge of Chapter 2! Tackle these 10 comprehensive questions on straight line graphing, break-even intersections, and algebra history. When you complete this slide, you have achieved full mastery of Linear Polynomials!",
        "quiz_range": [31, 40]
    }
]

# 40 Comprehensive Quiz Questions with Detailed Step-by-Step Solutions
quiz_questions = [
    # Questions 1 to 10 (Quiz Challenge 1)
    {
        "num": 1,
        "question": "What is the degree of the linear polynomial P(x) = 7x - 11?",
        "options": ["0", "1", "2", "7"],
        "correct": 1,
        "solution": "Step 1: The degree of a polynomial in one variable is the highest exponent of the variable with a non-zero coefficient.\nStep 2: In P(x) = 7x - 11, the term 7x is 7x¹.\nStep 3: The highest exponent of x is 1.\nTherefore, the degree is 1 (linear polynomial)."
    },
    {
        "num": 2,
        "question": "Which of the following expressions is NOT a linear polynomial?",
        "options": ["-5x + 8", "4y", "2x² + 3x - 1", "√3 t - 5"],
        "correct": 2,
        "solution": "Step 1: A linear polynomial must have degree 1 (highest power of the variable is 1).\nStep 2: In 2x² + 3x - 1, the highest power of x is 2.\nStep 3: A polynomial of degree 2 is quadratic, not linear.\nTherefore, 2x² + 3x - 1 is not a linear polynomial."
    },
    {
        "num": 3,
        "question": "What is the leading coefficient a and constant term b in the linear polynomial P(x) = 9 - 4x?",
        "options": ["a = 9, b = -4", "a = -4, b = 9", "a = 4, b = 9", "a = 9, b = 4"],
        "correct": 1,
        "solution": "Step 1: Rearrange P(x) into standard form ax + b.\nStep 2: P(x) = -4x + 9.\nStep 3: The coefficient of x is a = -4, and the constant term is b = 9."
    },
    {
        "num": 4,
        "question": "Why is the algebraic expression 3/x + 5 NOT a polynomial?",
        "options": [
            "Because 5 is an integer",
            "Because 3/x = 3x⁻¹, and polynomial variable exponents must be non-negative integers",
            "Because it has two terms",
            "Because x has a positive exponent"
        ],
        "correct": 1,
        "solution": "Step 1: Rewrite 3/x using exponent notation: 3/x = 3x⁻¹.\nStep 2: By definition, a polynomial requires all exponents of the variable to be whole numbers (0, 1, 2, 3...).\nStep 3: Since -1 is a negative integer, 3/x + 5 is an algebraic rational expression, not a polynomial."
    },
    {
        "num": 5,
        "question": "Express 5(3x - 2) - 4(2x + 1) in standard linear form ax + b.",
        "options": ["7x - 14", "7x - 6", "15x - 14", "7x + 14"],
        "correct": 0,
        "solution": "Step 1: Distribute multiplication over parentheses:\n5(3x - 2) = 15x - 10\n-4(2x + 1) = -8x - 4\nStep 2: Combine like terms:\n(15x - 8x) + (-10 - 4) = 7x - 14.\nTherefore, in standard form, it is 7x - 14 (with a = 7, b = -14)."
    },
    {
        "num": 6,
        "question": "In the standard form ax + b, what condition must the coefficient a satisfy for the polynomial to be linear?",
        "options": ["a > 0", "a < 0", "a ≠ 0", "a must be an integer"],
        "correct": 2,
        "solution": "Step 1: If a = 0, the expression becomes P(x) = 0x + b = b.\nStep 2: The term containing x vanishes, leaving a constant polynomial of degree 0.\nStep 3: Hence, a ≠ 0 is the essential condition for a polynomial to be linear."
    },
    {
        "num": 7,
        "question": "Evaluate the linear polynomial P(x) = 6x - 15 at x = -3.",
        "options": ["-33", "-3", "+3", "+33"],
        "correct": 0,
        "solution": "Step 1: Substitute x = -3 into P(x):\nP(-3) = 6(-3) - 15.\nStep 2: Perform multiplication: 6 × (-3) = -18.\nStep 3: Subtract: -18 - 15 = -33."
    },
    {
        "num": 8,
        "question": "Which of the following is a linear monomial?",
        "options": ["5x + 2", "8x", "7x²", "12"],
        "correct": 1,
        "solution": "Step 1: A monomial has exactly one non-zero term.\nStep 2: A linear expression has degree 1.\nStep 3: 8x has exactly one term and degree 1, making it a linear monomial.\n(5x + 2 is a binomial, 7x² is quadratic, and 12 is a constant monomial)."
    },
    {
        "num": 9,
        "question": "What is the degree of the zero polynomial P(x) = 0?",
        "options": ["0", "1", "Undefined", "-1"],
        "correct": 2,
        "solution": "Step 1: A non-zero constant polynomial like P(x) = 5 has degree 0 (5 = 5x⁰).\nStep 2: For P(x) = 0, it can be written as 0x¹, 0x², 0x³ with any arbitrary power.\nStep 3: By international convention in algebra, the degree of the zero polynomial is left undefined (or sometimes defined as -∞)."
    },
    {
        "num": 10,
        "question": "If P(x) = (k - 3)x² + 5x + 2 is a linear polynomial, what is the value of k?",
        "options": ["k = 0", "k = 3", "k = -3", "k = 5"],
        "correct": 1,
        "solution": "Step 1: For P(x) to be a linear polynomial, the coefficient of x² must be 0 (so the quadratic term vanishes).\nStep 2: Set coefficient of x² equal to 0: k - 3 = 0.\nStep 3: Solving for k: k = 3.\nWhen k = 3, P(x) = 0x² + 5x + 2 = 5x + 2, which is linear."
    },

    # Questions 11 to 20 (Quiz Challenge 2)
    {
        "num": 11,
        "question": "Find the zero of the linear polynomial P(x) = 4x - 20.",
        "options": ["x = -5", "x = 4", "x = 5", "x = 20"],
        "correct": 2,
        "solution": "Step 1: A zero of a polynomial is the value of x where P(x) = 0.\nStep 2: Set 4x - 20 = 0.\nStep 3: Add 20 to both sides: 4x = 20.\nStep 4: Divide by 4: x = 20 / 4 = 5.\nCheck: P(5) = 4(5) - 20 = 20 - 20 = 0."
    },
    {
        "num": 12,
        "question": "What is the zero of the general linear polynomial P(x) = ax + b (where a ≠ 0)?",
        "options": ["x = b / a", "x = -b / a", "x = -a / b", "x = a / b"],
        "correct": 1,
        "solution": "Step 1: Set P(x) = 0: ax + b = 0.\nStep 2: Subtract b from both sides: ax = -b.\nStep 3: Divide by a (since a ≠ 0): x = -b / a.\nEvery linear polynomial has exactly one real zero, given by x = -b/a."
    },
    {
        "num": 13,
        "question": "For the linear sequence 8, 14, 20, 26, 32..., what is the nth term formula T(n)?",
        "options": ["6n + 2", "6n + 8", "8n + 6", "6n - 2"],
        "correct": 0,
        "solution": "Step 1: Find the common first difference d: 14 - 8 = 6, 20 - 14 = 6. So d = 6.\nStep 2: The formula has form 6n + c.\nStep 3: For n = 1: 6(1) + c = 8 => 6 + c = 8 => c = 2.\nStep 4: Therefore, T(n) = 6n + 2.\nCheck for n = 2: 6(2) + 2 = 14 ✓."
    },
    {
        "num": 14,
        "question": "If P(x) = 5x + 3, what is the value of the first difference P(x + 1) - P(x)?",
        "options": ["3", "5", "8", "5x"],
        "correct": 1,
        "solution": "Step 1: P(x + 1) = 5(x + 1) + 3 = 5x + 5 + 3 = 5x + 8.\nStep 2: Subtract P(x): (5x + 8) - (5x + 3) = 5x + 8 - 5x - 3 = 5.\nStep 3: For any linear polynomial P(x) = ax + b, P(x + 1) - P(x) is always equal to the leading coefficient a. Here a = 5."
    },
    {
        "num": 15,
        "question": "What is the zero of the linear polynomial P(x) = -3x + 12?",
        "options": ["x = -4", "x = 4", "x = 3", "x = 12"],
        "correct": 1,
        "solution": "Step 1: Set -3x + 12 = 0.\nStep 2: -3x = -12.\nStep 3: x = -12 / (-3) = 4."
    },
    {
        "num": 16,
        "question": "Given the sequence rule T(n) = 7n - 4, which term in the sequence is equal to 101?",
        "options": ["13th term", "14th term", "15th term", "16th term"],
        "correct": 2,
        "solution": "Step 1: Set T(n) = 101: 7n - 4 = 101.\nStep 2: Add 4 to both sides: 7n = 105.\nStep 3: Divide by 7: n = 105 / 7 = 15.\nTherefore, 101 is the 15th term of the sequence."
    },
    {
        "num": 17,
        "question": "In a matchstick pattern for triangular shapes, 1 triangle takes 3 sticks, 2 triangles take 5 sticks, 3 triangles take 7 sticks. How many sticks are needed for n triangles?",
        "options": ["3n", "2n + 1", "2n + 3", "n + 2"],
        "correct": 1,
        "solution": "Step 1: Differences: 5 - 3 = 2, 7 - 5 = 2 (constant difference of 2).\nStep 2: Formula has form 2n + c.\nStep 3: For n = 1: 2(1) + c = 3 => c = 1.\nStep 4: Formula is 2n + 1.\n(For n = 1: 2(1)+1=3; n = 2: 2(2)+1=5; n = 3: 2(3)+1=7)."
    },
    {
        "num": 18,
        "question": "What is the zero of the linear polynomial P(x) = (2/3)x - 8?",
        "options": ["x = 8", "x = 10", "x = 12", "x = 16"],
        "correct": 2,
        "solution": "Step 1: Set (2/3)x - 8 = 0.\nStep 2: (2/3)x = 8.\nStep 3: Multiply both sides by 3/2: x = 8 × (3/2) = 24 / 2 = 12.\nCheck: (2/3)(12) - 8 = 8 - 8 = 0."
    },
    {
        "num": 19,
        "question": "An arithmetic table has inputs n = 1, 2, 3, 4 and outputs y = 13, 10, 7, 4. What is the linear formula?",
        "options": ["y = 3n + 10", "y = -3n + 16", "y = -3n + 13", "y = 3n + 16"],
        "correct": 1,
        "solution": "Step 1: Differences: 10 - 13 = -3, 7 - 10 = -3. Constant rate a = -3.\nStep 2: Form: y = -3n + c.\nStep 3: For n = 1: -3(1) + c = 13 => -3 + c = 13 => c = 16.\nStep 4: Formula is y = -3n + 16."
    },
    {
        "num": 20,
        "question": "How many zeroes can a linear polynomial have in total?",
        "options": ["At most two zeroes", "Exactly one zero", "Infinitely many zeroes", "No zeroes"],
        "correct": 1,
        "solution": "Step 1: By the Fundamental Theorem of Algebra, a polynomial of degree n has exactly n complex roots.\nStep 2: For a linear polynomial, degree is 1 and a ≠ 0.\nStep 3: The equation ax + b = 0 has the single unique solution x = -b/a.\nTherefore, every linear polynomial has exactly one zero."
    },

    # Questions 21 to 30 (Quiz Challenge 3)
    {
        "num": 21,
        "question": "Which of the following linear polynomials represents LINEAR DECAY?",
        "options": ["P(x) = 4x + 10", "P(x) = 0.5x - 3", "P(x) = -3x + 50", "P(x) = 7x"],
        "correct": 2,
        "solution": "Step 1: Linear decay occurs when the leading coefficient a is negative (a < 0), causing P(x) to decrease as x increases.\nStep 2: In P(x) = -3x + 50, a = -3 < 0.\nStep 3: Therefore, P(x) = -3x + 50 represents linear decay."
    },
    {
        "num": 22,
        "question": "A car fuel tank starts with 50 litres of petrol and uses 0.05 litres per kilometre. Which polynomial gives remaining fuel F(d) after d km?",
        "options": ["F(d) = 0.05d + 50", "F(d) = -0.05d + 50", "F(d) = 50d - 0.05", "F(d) = -50d + 0.05"],
        "correct": 1,
        "solution": "Step 1: Fuel is being consumed, so the rate of change is negative: a = -0.05 L/km.\nStep 2: Initial fuel when d = 0 is 50 L: b = 50.\nStep 3: The linear polynomial is F(d) = -0.05d + 50."
    },
    {
        "num": 23,
        "question": "Using F(d) = -0.05d + 50, what is the maximum driving range of the car before the tank is empty?",
        "options": ["500 km", "800 km", "1000 km", "1250 km"],
        "correct": 2,
        "solution": "Step 1: When the tank is empty, remaining fuel F(d) = 0.\nStep 2: Set -0.05d + 50 = 0.\nStep 3: 0.05d = 50.\nStep 4: d = 50 / 0.05 = 5000 / 5 = 1000 km."
    },
    {
        "num": 24,
        "question": "What is the y-intercept of the linear relationship y = -2x + 8?",
        "options": ["(0, -2)", "(0, 8)", "(4, 0)", "(8, 0)"],
        "correct": 1,
        "solution": "Step 1: The y-intercept occurs where the graph crosses the y-axis (at x = 0).\nStep 2: Substitute x = 0: y = -2(0) + 8 = 8.\nStep 3: The coordinates are (0, 8)."
    },
    {
        "num": 25,
        "question": "What is the x-intercept of the same linear relationship y = -2x + 8?",
        "options": ["(4, 0)", "(-4, 0)", "(0, 4)", "(0, 8)"],
        "correct": 0,
        "solution": "Step 1: The x-intercept occurs where the graph crosses the x-axis (at y = 0).\nStep 2: Set y = 0: -2x + 8 = 0 => 2x = 8 => x = 4.\nStep 3: The coordinates are (4, 0)."
    },
    {
        "num": 26,
        "question": "A water reservoir has 1500 cubic meters of water and loses 60 cubic meters per day due to evaporation and usage. When will it have 300 cubic meters left?",
        "options": ["15 days", "18 days", "20 days", "25 days"],
        "correct": 2,
        "solution": "Step 1: Model: V(t) = -60t + 1500.\nStep 2: Set V(t) = 300: -60t + 1500 = 300.\nStep 3: 60t = 1500 - 300 = 1200.\nStep 4: t = 1200 / 60 = 20 days."
    },
    {
        "num": 27,
        "question": "If the slope a of a linear relationship is zero (y = 0x + 7 = 7), what does its graph look like?",
        "options": ["A vertical line", "A horizontal line at y = 7", "A line passing through the origin", "A diagonal line of 45 degrees"],
        "correct": 1,
        "solution": "Step 1: When a = 0, y = 7 for every single choice of x.\nStep 2: The y-value never changes, producing a horizontal line parallel to the x-axis at distance 7 units above it."
    },
    {
        "num": 28,
        "question": "Which of the following points satisfies the linear relationship y = -3x + 1?",
        "options": ["(2, -5)", "(1, 4)", "(-1, -2)", "(0, -3)"],
        "correct": 0,
        "solution": "Step 1: Test point (2, -5): substitute x = 2.\nStep 2: y = -3(2) + 1 = -6 + 1 = -5.\nStep 3: Since the output matches y = -5, (2, -5) lies on the line."
    },
    {
        "num": 29,
        "question": "An electrician charges ₹150 for a home visit plus ₹100 for every hour of work. What is the total cost for 4.5 hours of work?",
        "options": ["₹500", "₹550", "₹600", "₹650"],
        "correct": 2,
        "solution": "Step 1: Formula: C(h) = 100h + 150.\nStep 2: For h = 4.5: C(4.5) = 100(4.5) + 150 = 450 + 150 = ₹600."
    },
    {
        "num": 30,
        "question": "What happens to the graph of y = ax + b when only the value of b is increased by 3 units?",
        "options": [
            "The line becomes steeper",
            "The line rotates clockwise",
            "The entire line shifts vertically upwards by 3 units parallel to itself",
            "The line flips horizontally"
        ],
        "correct": 2,
        "solution": "Step 1: In y = ax + b, b represents the vertical position (y-intercept).\nStep 2: Since the slope a does not change, the steepness remains unchanged.\nStep 3: Increasing b shifts every point on the line vertically upwards by 3 units, creating a parallel line."
    },

    # Questions 31 to 40 (Quiz Challenge 4)
    {
        "num": 31,
        "question": "Find the slope a of the line passing through the points (2, 5) and (6, 17).",
        "options": ["2", "3", "4", "5"],
        "correct": 1,
        "solution": "Step 1: The slope formula is a = (y₂ - y₁) / (x₂ - x₁).\nStep 2: Substitute (x₁, y₁) = (2, 5) and (x₂, y₂) = (6, 17):\na = (17 - 5) / (6 - 2) = 12 / 4 = 3.\nTherefore, the slope is 3."
    },
    {
        "num": 32,
        "question": "What is the equation of the line passing through (2, 5) and (6, 17)?",
        "options": ["y = 3x + 1", "y = 3x - 1", "y = 3x + 2", "y = 3x - 2"],
        "correct": 1,
        "solution": "Step 1: From Question 31, slope a = 3.\nStep 2: Standard form is y = 3x + b.\nStep 3: Substitute point (2, 5): 5 = 3(2) + b => 5 = 6 + b => b = 5 - 6 = -1.\nStep 4: The equation is y = 3x - 1."
    },
    {
        "num": 33,
        "question": "At what point do the lines y = 2x + 3 and y = -x + 9 intersect?",
        "options": ["(2, 7)", "(3, 9)", "(1, 5)", "(4, 11)"],
        "correct": 0,
        "solution": "Step 1: At the intersection point, both y-values are equal: 2x + 3 = -x + 9.\nStep 2: Add x to both sides: 3x + 3 = 9.\nStep 3: Subtract 3: 3x = 6 => x = 2.\nStep 4: Substitute x = 2 into y = 2x + 3: y = 2(2) + 3 = 7.\nTherefore, the intersection point is (2, 7)."
    },
    {
        "num": 34,
        "question": "Company A offers a phone plan with a ₹100 base fee and ₹2 per minute. Company B offers ₹40 base fee and ₹3 per minute. At how many minutes do both plans cost the same?",
        "options": ["40 minutes", "50 minutes", "60 minutes", "70 minutes"],
        "correct": 2,
        "solution": "Step 1: Cost of A: y₁ = 2m + 100.\nStep 2: Cost of B: y₂ = 3m + 40.\nStep 3: Break-even point: 2m + 100 = 3m + 40.\nStep 4: 100 - 40 = 3m - 2m => m = 60 minutes.\nCheck: A costs 2(60)+100 = 220; B costs 3(60)+40 = 220 ✓."
    },
    {
        "num": 35,
        "question": "Which ancient Indian mathematician gave the general solution for linear equations x = (d - b)/(a - c) in his 628 CE treatise Brahmasphutasiddhanta?",
        "options": ["Aryabhata", "Brahmagupta", "Bhaskara II", "Varahamihira"],
        "correct": 1,
        "solution": "Step 1: Brahmagupta (598–668 CE) wrote the Brahmasphutasiddhanta in 628 CE.\nStep 2: He formulated the universal rule for linear equations: 'The difference between the known quantities divided by the difference between the unknowns gives the value of the unknown.'"
    },
    {
        "num": 36,
        "question": "The perimeter of a rectangular garden is 80 m. If its length is 10 m more than its width, what are its dimensions?",
        "options": ["Width = 12 m, Length = 22 m", "Width = 15 m, Length = 25 m", "Width = 20 m, Length = 30 m", "Width = 10 m, Length = 20 m"],
        "correct": 1,
        "solution": "Step 1: Let width = w. Length = w + 10.\nStep 2: Perimeter = 2(Length + Width) = 2(w + 10 + w) = 2(2w + 10) = 4w + 20.\nStep 3: Set equal to 80: 4w + 20 = 80 => 4w = 60 => w = 15 m.\nStep 4: Length = 15 + 10 = 25 m.\nCheck: 2(15 + 25) = 2(40) = 80 m ✓."
    },
    {
        "num": 37,
        "question": "The sum of three consecutive odd numbers is 69. What is the largest of these numbers?",
        "options": ["21", "23", "25", "27"],
        "correct": 2,
        "solution": "Step 1: Let the three consecutive odd numbers be x, x + 2, and x + 4.\nStep 2: Sum: x + (x + 2) + (x + 4) = 3x + 6.\nStep 3: Set equal to 69: 3x + 6 = 69 => 3x = 63 => x = 21.\nStep 4: The numbers are 21, 23, 25. The largest is 25."
    },
    {
        "num": 38,
        "question": "Which 17th-century French mathematician unified algebra and geometry by introducing the coordinate system in his 1637 work La Géométrie?",
        "options": ["Pierre de Fermat", "Blaise Pascal", "René Descartes", "François Viète"],
        "correct": 2,
        "solution": "Step 1: René Descartes published La Géométrie in 1637 as an appendix to Discourse on Method.\nStep 2: He created Cartesian coordinates (named in his honor), showing that algebraic linear equations represent geometric straight lines."
    },
    {
        "num": 39,
        "question": "Two parallel railway tracks are modeled by the lines y = 3x + 5 and y = 3x - 4. Why will these two tracks never cross?",
        "options": [
            "Because their intercepts are equal",
            "Because they have the exact same slope a = 3, maintaining a constant separation",
            "Because both slopes are negative",
            "Because they cross at infinity"
        ],
        "correct": 1,
        "solution": "Step 1: Two lines on a flat plane are parallel if and only if their slopes are identical (a₁ = a₂ = 3) and their intercepts are distinct (b₁ = 5 ≠ b₂ = -4).\nStep 2: Having the same slope ensures their vertical separation remains fixed at 9 units everywhere, so they never intersect."
    },
    {
        "num": 40,
        "question": "A sum of ₹800 is divided between A and B in the ratio 3 : 5. How much does B receive?",
        "options": ["₹300", "₹400", "₹500", "₹600"],
        "correct": 2,
        "solution": "Step 1: Let the parts be 3x and 5x.\nStep 2: Total = 3x + 5x = 8x = 800 => x = 100.\nStep 3: B receives 5x = 5 × 100 = ₹500. (A receives 3x = ₹300)."
    }
]

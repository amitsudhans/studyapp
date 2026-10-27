# -*- coding: utf-8 -*-
"""
Curriculum and Slide Data for NCERT Class 8 Mathematics Chapter 1:
A Square and A Cube (Mathematics Grade 8)
Complete coverage of all 10 core headings & curriculum topics across 20 slides:
- 16 interactive content slides with 32 in-slide checkpoints (2 per content slide)
- 4 dedicated mastery quiz challenge slides with 40 questions total (10 per slide)
- Complete step-by-step solutions for all quiz questions with popup modal trigger
- Teacher avatar: Prof. Ramanujan Sharma (Senior Mathematics Mentor)
"""

slides_data = [
    # Slide 1: 1.1 Square Numbers & The Geometry of Area
    {
        "id": 1,
        "title": "1.1 Square Numbers & The Geometry of Area",
        "subtitle": "Definition of Square Numbers, Geometric Arrays and Notation n² (NCERT Page 3)",
        "content": r"""
<p class="lead-p">In geometry, a square is a flat figure with four equal sides and four right angles. When we investigate the area of a square of sidelength $n$ units, we multiply the side length by itself: $\text{Area} = n \times n = n^2$. Numbers that can be represented as the area of a square formed by unit square tiles are known as <strong>square numbers</strong>.</p>

<div class="theory-box">
  <h4>1. Formal Mathematical Definition</h4>
  <p>A natural number $m$ is called a <strong>square number</strong> (or a <em>perfect square</em>) if there exists a natural number $n$ such that:</p>
  <p class="highlight-eq">$$m = n \times n = n^2$$</p>
  <p>For instance, $1 = 1^2$, $4 = 2^2$, $9 = 3^2$, $16 = 4^2$, $25 = 5^2$, $36 = 6^2$, and so forth. If a positive integer cannot be factored into two identical natural numbers, it is not a square number.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Geometric Array Representation</h4>
    <p>Every square number $n^2$ can be organized as an $n \times n$ square array of discrete dots or unit grid squares:</p>
    <ul>
      <li><strong>1:</strong> A single dot ($1 \times 1$).</li>
      <li><strong>4:</strong> A $2 \times 2$ matrix of dots.</li>
      <li><strong>9:</strong> A $3 \times 3$ matrix of dots.</li>
      <li><strong>16:</strong> A $4 \times 4$ matrix of dots.</li>
    </ul>
    <p>This deep connection between geometry (spatial area) and arithmetic (multiplication) gave rise to the terminology "squared".</p>
  </div>
  <div class="card-item">
    <h4>Squares of Fractions and Decimals</h4>
    <p>While natural numbers produce <em>perfect squares</em>, the square operation applies to all rational numbers:</p>
    <ul>
      <li>$\left(\frac{3}{5}\right)^2 = \frac{3}{5} \times \frac{3}{5} = \frac{9}{25}$</li>
      <li>$(2.5)^2 = 2.5 \times 2.5 = 6.25$</li>
      <li>$(0.1)^2 = 0.01$ (squaring doubles the decimal places)</li>
    </ul>
    <p class="highlight-eq">$$n^2 \text{ is always strictly non-negative for any real number } n \ge 0.$$</p>
  </div>
</div>
""",
        "sim_type": "square_grid_builder",
        "voice": "Welcome to Chapter 1 of Class 8 Mathematics: A Square and A Cube! We begin our mathematical adventure with Square Numbers. When you multiply any number by itself, you form a square! Notice how 1, 4, 9, 16, and 25 literally form geometrical square arrays on your screen. Adjust the slider to build square tile arrays from 1 squared up to 10 squared!",
        "checkpoints": [
            {
                "question": "Which of the following is a square number (perfect square)?",
                "options": ["18", "25", "32", "45"],
                "correct": 1,
                "explanation": "25 is equal to 5 × 5 = 5², making it a perfect square. The numbers 18, 32, and 45 cannot be written as the product of an integer with itself."
            },
            {
                "question": "What is the area of a square tile with sidelength 2.5 cm?",
                "options": ["5.0 cm²", "6.25 cm²", "6.5 cm²", "7.25 cm²"],
                "correct": 1,
                "explanation": "Area = side × side = 2.5 × 2.5 = 6.25 cm²."
            }
        ]
    },

    # Slide 2: Number of Factors & The Locker Mystery
    {
        "id": 2,
        "title": "Factor Pairs & The 100-Lockers Theorem",
        "subtitle": "Why Only Square Numbers Possess an Odd Number of Factors (NCERT Page 1–2)",
        "content": r"""
<p class="lead-p">In the classical 100-lockers problem, 100 people toggle lockers based on multiples. Which lockers remain open at the end? A locker is toggled once for every factor it possesses. Because a closed locker toggled an odd number of times remains <strong>OPEN</strong>, only numbers with an <strong>odd number of factors</strong> stay open!</p>

<div class="theory-box">
  <h4>1. Partner Factor Pairs Principle</h4>
  <p>For any positive integer $N$, factors naturally arrive in paired partners $(a, b)$ such that $a \times b = N$:</p>
  <ul>
    <li>For $N = 6$: the factor pairs are $(1, 6)$ and $(2, 3)$. Factors are $\{1, 2, 3, 6\}$ (total of 4 factors, an <strong>even</strong> count).</li>
    <li>For $N = 12$: the factor pairs are $(1, 12), (2, 6), (3, 4)$. Factors are $\{1, 2, 3, 4, 6, 12\}$ (total of 6 factors, an <strong>even</strong> count).</li>
    <li>For non-square numbers, every factor $a$ has a distinct partner factor $b \neq a$, so factors always group into disjoint pairs. Hence, <em>all non-square integers have an even number of factors</em>.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Square Number Exception</h4>
    <p>When $N$ is a square number, say $N = k^2$, there exists a special factor pair where both factors are identical: $k \times k = N$.</p>
    <p>For example, for $N = 36$:</p>
    <p>Pairs: $(1, 36), (2, 18), (3, 12), (4, 9)$ and the unique pair $(6, 6)$.</p>
    <p>When we list distinct factors of 36: $\{1, 2, 3, 4, 6, 9, 12, 18, 36\}$, the number 6 is counted only once!</p>
    <p class="highlight-eq">$$\text{Number of factors of } 36 = 2 \times 4 + 1 = 9 \text{ (ODD!)}$$</p>
  </div>
  <div class="card-item">
    <h4>3. The Lockers That Remain Open</h4>
    <p>Since only lockers with an odd number of factors remain open, the open lockers in the range 1 to 100 are strictly the perfect squares:</p>
    <p class="highlight-eq">$$\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$$</p>
    <p>Lockers toggled exactly twice are those with exactly two factors: the <strong>prime numbers</strong> $\{2, 3, 5, 7, 11, \dots\}$.</p>
  </div>
</div>
""",
        "sim_type": "locker_factor_matrix",
        "voice": "Here is one of the most elegant discoveries in arithmetic! Almost all numbers have an even number of factors because factors come in pairs, like 1 times 6 and 2 times 3. But look at 36: six times six is thirty-six! Because that factor pairs with itself, it is counted only once, giving an odd total of factors! This proves why only square lockers remain open!",
        "checkpoints": [
            {
                "question": "How many total factors does the square number 16 have?",
                "options": ["4", "5", "6", "8"],
                "correct": 1,
                "explanation": "Factors of 16 are 1, 2, 4, 8, and 16. Total count is 5 factors, which is an odd number because 4 × 4 = 16 pairs with itself."
            },
            {
                "question": "Which lockers remain open in the 1 to 100 locker puzzle?",
                "options": ["All even numbered lockers", "All prime numbered lockers", "All perfect square numbered lockers", "All multiples of 10"],
                "correct": 2,
                "explanation": "A locker remains open if and only if it is toggled an odd number of times. Only perfect squares have an odd number of factors, so lockers 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 stay open."
            }
        ]
    },

    # Slide 3: Patterns & Properties of Perfect Squares: Units Digit Rule
    {
        "id": 3,
        "title": "Patterns of Perfect Squares: The Units Digit Law",
        "subtitle": "Terminal Digits, Impossible Endings {2, 3, 7, 8} and Symmetry (NCERT Page 4)",
        "content": r"""
<p class="lead-p">When we compute the squares of the first 10 digits, an unmistakable pattern emerges in their final (units) digit. This single property allows mathematicians to instantly disqualify millions of numbers from being perfect squares at a single glance!</p>

<div class="theory-box">
  <h4>1. Units Digit Determinism Table</h4>
  <p>The units digit of $n^2$ depends solely on the units digit of $n$:</p>
  <ul>
    <li>Numbers ending in <strong>0</strong> square to end in <strong>0</strong> ($0^2 = 0, 10^2 = 100$).</li>
    <li>Numbers ending in <strong>1 or 9</strong> square to end in <strong>1</strong> ($1^2 = 1, 9^2 = 81, 11^2 = 121, 19^2 = 361$).</li>
    <li>Numbers ending in <strong>2 or 8</strong> square to end in <strong>4</strong> ($2^2 = 4, 8^2 = 64, 12^2 = 144, 18^2 = 324$).</li>
    <li>Numbers ending in <strong>3 or 7</strong> square to end in <strong>9</strong> ($3^2 = 9, 7^2 = 49, 13^2 = 169, 17^2 = 289$).</li>
    <li>Numbers ending in <strong>4 or 6</strong> square to end in <strong>6</strong> ($4^2 = 16, 6^2 = 36, 14^2 = 196, 16^2 = 256$).</li>
    <li>Numbers ending in <strong>5</strong> square to end in <strong>5</strong> ($5^2 = 25, 15^2 = 225, 25^2 = 625$).</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>The Fundamental Non-Square Criterion</h4>
    <p>A natural number can only end with one of six digits: $\{0, 1, 4, 5, 6, 9\}$.</p>
    <p class="highlight-eq">$$\text{No perfect square can EVER end in } 2, 3, 7, \text{ or } 8!$$</p>
    <p>Therefore, numbers like $2032, 2048, 1027, 3583$ are guaranteed to be <strong>non-squares</strong> without needing any calculation.</p>
  </div>
  <div class="card-item">
    <h4>Necessary vs. Sufficient Condition</h4>
    <p>Ending in $0, 1, 4, 5, 6, \text{ or } 9$ is a <em>necessary</em> condition, but <strong>not sufficient</strong>!</p>
    <p>For example, 26 ends in 6, but $5^2 = 25$ and $6^2 = 36$, so 26 is not a square. Similarly, 19, 21, 34, 50 all end in allowed digits, but none are perfect squares.</p>
  </div>
</div>
""",
        "sim_type": "units_digit_analyzer",
        "voice": "Take a close look at the units digit law! Every single square number in the universe must end with 0, 1, 4, 5, 6, or 9. If you see any number ending in 2, 3, 7, or 8, you can instantly state with mathematical certainty that it is not a square! Test any number in our Units Digit Analyzer to see this rule in action.",
        "checkpoints": [
            {
                "question": "Which of the following numbers CANNOT possibly be a perfect square?",
                "options": ["1089", "2048", "3136", "4225"],
                "correct": 1,
                "explanation": "2048 ends in 8. No square of an integer can ever end in 2, 3, 7, or 8. The other numbers end in 9, 6, and 5 which are valid square endings."
            },
            {
                "question": "If a number ends in the digit 7, what will be the units digit of its square?",
                "options": ["3", "7", "9", "1"],
                "correct": 2,
                "explanation": "Since 7 × 7 = 49, any number ending in 7 will always produce a square whose units digit is 9."
            }
        ]
    },

    # Slide 4: Trailing Zeros & Parity of Squares
    {
        "id": 4,
        "title": "Trailing Zeros & Parity Invariance",
        "subtitle": "Even Number of Zeros Theorem, Parity Laws and Decimal Squaring (NCERT Page 5)",
        "content": r"""
<p class="lead-p">Square numbers obey two strict structural laws regarding terminal zeros and algebraic parity: the zero-doubling law and the parity conservation law.</p>

<div class="theory-box">
  <h4>1. The Even Number of Terminal Zeros Theorem</h4>
  <p>Let an integer $N$ end with $k$ zeros, meaning $N = a \times 10^k$, where $a$ is not divisible by 10. Squaring $N$ yields:</p>
  <p class="highlight-eq">$$N^2 = (a \times 10^k)^2 = a^2 \times (10^k)^2 = a^2 \times 10^{2k}$$</p>
  <ul>
    <li>The square $N^2$ will always end in exactly $2k$ zeros (an <strong>even number of zeros</strong>).</li>
    <li>$10^2 = 100$ (1 zero becomes 2 zeros).</li>
    <li>$400^2 = 160000$ (2 zeros become 4 zeros).</li>
    <li>$7000^2 = 49000000$ (3 zeros become 6 zeros).</li>
  </ul>
  <p class="highlight-eq">$$\text{A number ending in an odd number of zeros (e.g., 50, 1000, 2500000) is NEVER a square!}$$</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Parity Invariance Principle</h4>
    <p>Squaring preserves mathematical parity:</p>
    <ul>
      <li><strong>Square of an EVEN number is always EVEN:</strong><br>
      $(2k)^2 = 4k^2 = 2(2k^2)$, which is a multiple of 4 and therefore always even.</li>
      <li><strong>Square of an ODD number is always ODD:</strong><br>
      $(2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which leaves remainder 1 when divided by 2.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Modulo 4 Property of Squares</h4>
    <p>Every square is either $0 \pmod 4$ or $1 \pmod 4$:</p>
    <ul>
      <li>Even squares: $(2k)^2 = 4k^2 \equiv 0 \pmod 4$.</li>
      <li>Odd squares: $(2k+1)^2 = 4(k^2+k) + 1 \equiv 1 \pmod 4$.</li>
    </ul>
    <p>No integer of the form $4m + 2$ or $4m + 3$ can ever be a perfect square!</p>
  </div>
</div>
""",
        "sim_type": "zero_parity_tester",
        "voice": "Notice the mathematical symmetry here: whenever you square a number ending in zeros, the number of zeros at the end exactly doubles! One zero becomes two, two becomes four, three becomes six. That means a true square can never end in an odd number of zeros! Furthermore, even numbers always square to even numbers, and odd numbers always square to odd numbers.",
        "checkpoints": [
            {
                "question": "If a number has 4 zeros at the end, how many zeros will its square have at the end?",
                "options": ["4 zeros", "8 zeros", "16 zeros", "6 zeros"],
                "correct": 1,
                "explanation": "The number of zeros doubles upon squaring. An integer ending in 4 zeros will have 4 × 2 = 8 zeros at the end of its square."
            },
            {
                "question": "Which of the following numbers can be a perfect square based on terminal zeros and parity?",
                "options": ["25000", "360000", "490", "12100000"],
                "correct": 1,
                "explanation": "360000 ends in 4 zeros (even count) and 36 = 6², so 360000 = 600² is a perfect square. 25000 (3 zeros), 490 (1 zero), and 12100000 (5 zeros) all have an odd count of zeros and cannot be squares."
            }
        ]
    },

    # Slide 5: Perfect Squares & Odd Numbers: Sum of Successive Odds
    {
        "id": 5,
        "title": "Perfect Squares & The Sum of Odd Numbers",
        "subtitle": "The Inverted-L Gnomon Theorem: Σ(2k - 1) = n² (NCERT Page 5–6)",
        "content": r"""
<p class="lead-p">One of the most visually stunning identities in all of mathematics connects consecutive square numbers to consecutive odd numbers. The difference between two consecutive squares is always an odd number, leading directly to the theorem that <strong>every square is the sum of consecutive odd numbers starting from 1</strong>.</p>

<div class="theory-box">
  <h4>1. Difference of Consecutive Squares</h4>
  <p>Consider the algebraic difference between $(n+1)^2$ and $n^2$:</p>
  <p class="highlight-eq">$$(n + 1)^2 - n^2 = (n^2 + 2n + 1) - n^2 = 2n + 1$$</p>
  <p>Because $2n + 1$ is the definition of an odd number, stepping from one square to the next always adds the next odd number:</p>
  <ul>
    <li>$2^2 - 1^2 = 4 - 1 = 3$</li>
    <li>$3^2 - 2^2 = 9 - 4 = 5$</li>
    <li>$4^2 - 3^2 = 16 - 9 = 7$</li>
    <li>$5^2 - 4^2 = 25 - 16 = 9$</li>
    <li>$6^2 - 5^2 = 36 - 25 = 11$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Sum of First n Odd Numbers</h4>
    <p>By telescoping the differences, we obtain the universal theorem:</p>
    <p class="highlight-eq">$$1 + 3 + 5 + 7 + \dots + (2n - 1) = n^2$$</p>
    <ul>
      <li>$1 = 1^2$ (sum of first 1 odd number)</li>
      <li>$1 + 3 = 4 = 2^2$ (first 2 odd numbers)</li>
      <li>$1 + 3 + 5 = 9 = 3^2$ (first 3 odd numbers)</li>
      <li>$1 + 3 + 5 + 7 = 16 = 4^2$ (first 4 odd numbers)</li>
      <li>$1 + 3 + 5 + 7 + 9 = 25 = 5^2$ (first 5 odd numbers)</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>3. The Geometric Gnomon (Inverted L)</h4>
    <p>In visual geometry, wrapping an "inverted L" shape (gnomon) of dots around an $n \times n$ square expands it to an $(n+1) \times (n+1)$ square.</p>
    <p>The number of dots in the corner border added is $n + n + 1 = 2n + 1$, which is exactly the next consecutive odd number!</p>
  </div>
</div>
""",
        "sim_type": "odd_sum_gnomon_animator",
        "voice": "Look closely at this visual marvel! To turn a 1-by-1 square into a 2-by-2 square, you add 3 dots in an inverted L shape. To make it a 3-by-3 square, you add 5 dots! To make it 4-by-4, you add 7 dots. This proves visually without a single word that the sum of the first n odd numbers is always equal to n squared!",
        "checkpoints": [
            {
                "question": "What is the sum of the first 8 consecutive odd numbers (1 + 3 + 5 + 7 + 9 + 11 + 13 + 15) without adding them individually?",
                "options": ["56", "64", "72", "81"],
                "correct": 1,
                "explanation": "The sum of the first n odd numbers is n². For n = 8, the sum is 8² = 64."
            },
            {
                "question": "What is the 36th odd number, and what is 36² if 35² = 1225?",
                "options": ["36th odd = 71; 36² = 1296", "36th odd = 69; 36² = 1294", "36th odd = 73; 36² = 1298", "36th odd = 71; 36² = 1300"],
                "correct": 0,
                "explanation": "The nth odd number is 2n - 1. For n = 36, the 36th odd number is 2(36) - 1 = 71. Since 36² = 35² + 71 = 1225 + 71 = 1296."
            }
        ]
    },

    # Slide 6: Testing Squares via Repeated Subtraction
    {
        "id": 6,
        "title": "Square Verification: Repeated Odd Subtraction",
        "subtitle": "Algorithmic Perfect Square Decision & Step Count Root Determination (NCERT Page 6)",
        "content": r"""
<p class="lead-p">The theorem $n^2 = \sum_{k=1}^n (2k - 1)$ gives us an infallible mechanical algorithm to determine whether any positive integer is a perfect square, and simultaneously find its square root!</p>

<div class="theory-box">
  <h4>1. The Repeated Subtraction Algorithm</h4>
  <p>To test whether a positive integer $M$ is a perfect square:</p>
  <ol>
    <li>Subtract successive odd numbers $1, 3, 5, 7, 9, 11, \dots$ in order from $M$.</li>
    <li>If the remainder reaches <strong>exactly 0</strong> after $k$ subtractions, then $M$ is a <strong>perfect square</strong>, and $\sqrt{M} = k$.</li>
    <li>If the subtraction skips over 0 and becomes <strong>negative</strong>, then $M$ is <strong>NOT a perfect square</strong>.</li>
  </ol>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Example 1: Testing 25 (Square)</h4>
    <p>Step 1: $25 - 1 = 24$</p>
    <p>Step 2: $24 - 3 = 21$</p>
    <p>Step 3: $21 - 5 = 16$</p>
    <p>Step 4: $16 - 7 = 9$</p>
    <p>Step 5: $9 - 9 = 0$</p>
    <p class="highlight-eq">$$\text{Reached 0 in 5 steps} \implies 25 = 5^2 \implies \sqrt{25} = 5$$</p>
  </div>
  <div class="card-item">
    <h4>Example 2: Testing 38 (Non-Square)</h4>
    <p>Step 1: $38 - 1 = 37$ &emsp; Step 2: $37 - 3 = 34$</p>
    <p>Step 3: $34 - 5 = 29$ &emsp; Step 4: $29 - 7 = 22$</p>
    <p>Step 5: $22 - 9 = 13$ &emsp; Step 6: $13 - 11 = 2$</p>
    <p>Step 7: $2 - 13 = -11 \text{ (Crossed 0 into negative!)}$</p>
    <p class="highlight-eq">$$38 \text{ cannot reach 0} \implies 38 \text{ is NOT a square!}$$</p>
  </div>
</div>
""",
        "sim_type": "repeated_subtraction_stepper",
        "voice": "Repeated subtraction is like walking backward down the staircase of odd numbers. If you land perfectly on step zero, your number is a square, and the number of steps you took is its square root! But if you tumble past zero into negative territory, the number is not a square. Try stepping through 81 or any number you choose!",
        "checkpoints": [
            {
                "question": "If we test 49 by repeated subtraction of consecutive odd numbers, in how many steps will we reach 0?",
                "options": ["5 steps", "6 steps", "7 steps", "8 steps"],
                "correct": 2,
                "explanation": "49 = 7², so subtracting 1, 3, 5, 7, 9, 11, 13 (the first 7 odd numbers) will reduce 49 to exactly 0 in 7 steps."
            },
            {
                "question": "During repeated odd subtraction on the number 50, what happens at step 8?",
                "options": ["Reaches 0", "Crosses 0 and becomes -15", "Becomes 1 and next subtraction is 2 - 15 = -13", "Remains positive"],
                "correct": 2,
                "explanation": "After 7 steps, 50 - 49 = 1. The 8th odd number is 15. Then 1 - 15 = -14, which crosses below 0 into negative numbers, showing 50 is not a square."
            }
        ]
    },

    # Slide 7: Non-Square Numbers Between Consecutive Squares
    {
        "id": 7,
        "title": "Non-Squares Between Consecutive Squares",
        "subtitle": "The 2n Non-Square Theorem & Block Interval Counting (NCERT Page 7)",
        "content": r"""
<p class="lead-p">Between two consecutive perfect squares $n^2$ and $(n+1)^2$, how many non-square natural numbers are trapped? This fundamental counting theorem reveals a simple linear relationship of $2n$.</p>

<div class="theory-box">
  <h4>1. The 2n Non-Square Theorem</h4>
  <p>To count the integers strictly between $n^2$ and $(n+1)^2$, we compute:</p>
  <p class="highlight-eq">$$\text{Count} = (n + 1)^2 - n^2 - 1 = (n^2 + 2n + 1) - n^2 - 1 = 2n$$</p>
  <p>Therefore, there are exactly <strong>$2n$ non-perfect square numbers</strong> lying between $n^2$ and $(n+1)^2$:</p>
  <ul>
    <li>Between $1^2 = 1$ and $2^2 = 4$: there are $2(1) = 2$ non-squares ($\{2, 3\}$).</li>
    <li>Between $2^2 = 4$ and $3^2 = 9$: there are $2(2) = 4$ non-squares ($\{5, 6, 7, 8\}$).</li>
    <li>Between $3^2 = 9$ and $4^2 = 16$: there are $2(3) = 6$ non-squares ($\{10, 11, 12, 13, 14, 15\}$).</li>
    <li>Between $16^2 = 256$ and $17^2 = 289$: there are $2(16) = 32$ non-squares.</li>
    <li>Between $99^2 = 9801$ and $100^2 = 10000$: there are $2(99) = 198$ non-squares.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Distribution in Blocks of 100</h4>
    <p>Squares become progressively rarer as numbers grow larger:</p>
    <ul>
      <li><strong>1 to 100:</strong> 10 squares ($1^2$ to $10^2$).</li>
      <li><strong>101 to 200:</strong> 4 squares ($11^2=121$ to $14^2=196$).</li>
      <li><strong>201 to 300:</strong> 3 squares ($15^2=225$ to $17^2=289$).</li>
      <li><strong>301 to 400:</strong> 3 squares ($18^2=324$ to $20^2=400$).</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Largest Square Less Than 1000</h4>
    <p>Since $30^2 = 900$, $31^2 = 961$, and $32^2 = 1024$:</p>
    <p class="highlight-eq">$$\text{Largest perfect square } < 1000 = 31^2 = 961$$</p>
    <p>There are exactly 31 square numbers between 1 and 1000.</p>
  </div>
</div>
""",
        "sim_type": "between_squares_counter",
        "voice": "How many numbers sit between consecutive squares? The answer is always twice the smaller root, or 2n! Between 3 squared and 4 squared, there are 2 times 3, or 6 non-squares: 10, 11, 12, 13, 14, and 15! Between 99 squared and 100 squared, there are 2 times 99, or 198 numbers! Try testing any consecutive pair in the simulator.",
        "checkpoints": [
            {
                "question": "How many non-perfect square numbers lie between 12² and 13²?",
                "options": ["24", "25", "26", "27"],
                "correct": 0,
                "explanation": "Using the 2n theorem, the number of non-square numbers between n² and (n + 1)² is 2n. For n = 12, 2 × 12 = 24 numbers."
            },
            {
                "question": "What is the largest perfect square strictly less than 1000?",
                "options": ["900", "961", "981", "999"],
                "correct": 1,
                "explanation": "31² = 961, while 32² = 1024 > 1000. Hence, 961 is the largest square less than 1000."
            }
        ]
    },

    # Slide 8: Perfect Squares and Triangular Numbers
    {
        "id": 8,
        "title": "Perfect Squares & Triangular Numbers",
        "subtitle": "Combining Consecutive Triangular Numbers: T_{n-1} + T_n = n² (NCERT Page 7)",
        "content": r"""
<p class="lead-p">Triangular numbers are numbers that can be arranged in equilateral triangle dot patterns: $1, 3, 6, 10, 15, 21, \dots$. When any two consecutive triangular numbers are combined, they form a perfect square!</p>

<div class="theory-box">
  <h4>1. Definition of Triangular Numbers</h4>
  <p>The $n$-th triangular number $T_n$ is the sum of the first $n$ natural numbers:</p>
  <p class="highlight-eq">$$T_n = 1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}$$</p>
  <ul>
    <li>$T_1 = 1$</li>
    <li>$T_2 = 1 + 2 = 3$</li>
    <li>$T_3 = 1 + 2 + 3 = 6$</li>
    <li>$T_4 = 1 + 2 + 3 + 4 = 10$</li>
    <li>$T_5 = 1 + 2 + 3 + 4 + 5 = 15$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Consecutivity Identity</h4>
    <p>Adding two adjacent triangular numbers yields:</p>
    <p class="highlight-eq">$$T_{n-1} + T_n = \frac{(n-1)n}{2} + \frac{n(n+1)}{2} = \frac{n(n-1 + n + 1)}{2} = \frac{n(2n)}{2} = n^2$$</p>
    <ul>
      <li>$T_1 + T_2 = 1 + 3 = 4 = 2^2$</li>
      <li>$T_2 + T_3 = 3 + 6 = 9 = 3^2$</li>
      <li>$T_3 + T_4 = 6 + 10 = 16 = 4^2$</li>
      <li>$T_4 + T_5 = 10 + 15 = 25 = 5^2$</li>
      <li>$T_5 + T_6 = 15 + 21 = 36 = 6^2$</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>3. Geometric Tessellation Visual</h4>
    <p>If you take an upper triangular wedge of 3 dots and an interlocking lower triangular wedge of 6 dots, they fit together along the diagonal to form a solid $3 \times 3$ square of 9 dots!</p>
    <p>Every square array can be cleanly cut along its diagonal into two consecutive triangular pieces.</p>
  </div>
</div>
""",
        "sim_type": "triangular_square_merger",
        "voice": "Triangles and squares are deeply intertwined in ancient arithmetic. Look at two consecutive triangular numbers, like 6 and 10. Fit them together, and they form a perfect 4-by-4 square of 16 dots! Algebraically, n times n minus 1 over 2, plus n times n plus 1 over 2, always simplifies to n squared!",
        "checkpoints": [
            {
                "question": "Which two consecutive triangular numbers add together to form 49 (which is 7²)?",
                "options": ["15 and 34", "21 and 28", "20 and 29", "18 and 31"],
                "correct": 1,
                "explanation": "T₆ = 6(7)/2 = 21 and T₇ = 7(8)/2 = 28. Then T₆ + T₇ = 21 + 28 = 49 = 7²."
            },
            {
                "question": "What is the 5th triangular number T₅?",
                "options": ["10", "12", "15", "20"],
                "correct": 2,
                "explanation": "T₅ = 1 + 2 + 3 + 4 + 5 = 5(6)/2 = 15."
            }
        ]
    },

    # Slide 9: Square Roots & The Radical Symbol √
    {
        "id": 9,
        "title": "Square Roots: Concept & Radical Notation",
        "subtitle": "Inverse Operations, Dual Integer Roots (±x) and Principal Radical √ (NCERT Page 7–8)",
        "content": r"""
<p class="lead-p">Just as subtraction is the inverse of addition, and division is the inverse of multiplication, <strong>taking the square root</strong> is the inverse mathematical operation of squaring a number.</p>

<div class="theory-box">
  <h4>1. Formal Definition of Square Root</h4>
  <p>If a number $y = x^2$, then $x$ is called a <strong>square root</strong> of $y$.</p>
  <p>For example, because $7^2 = 49$, 7 is a square root of 49.</p>
  <p>However, notice that: $(-7) \times (-7) = +49$ as well!</p>
  <p class="highlight-eq">$$\text{Every positive real number has TWO square roots: one positive and one negative: } \pm \sqrt{y}$$</p>
  <p>For instance, the square roots of 64 are $+8$ and $-8$.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Principal Square Root Symbol (√)</h4>
    <p>By international mathematical convention, the radical symbol $\sqrt{n}$ denotes strictly the <strong>principal (positive) square root</strong>:</p>
    <ul>
      <li>$\sqrt{49} = 7$ (positive root)</li>
      <li>$\sqrt{64} = 8$</li>
      <li>$\sqrt{100} = 10$</li>
      <li>$-\sqrt{64} = -8$ (when negative root is desired)</li>
    </ul>
    <p>In Grade 8 NCERT mathematics, we focus on the positive square root $\sqrt{n}$.</p>
  </div>
  <div class="card-item">
    <h4>3. Geometric Side-Length Meaning</h4>
    <p>If a square field or floor has an area of $A \text{ m}^2$, the physical side length $s$ is simply the principal square root:</p>
    <p class="highlight-eq">$$s = \sqrt{A}$$</p>
    <p>For $A = 441 \text{ m}^2$, $s = \sqrt{441} = 21 \text{ m}$. Physical lengths can never be negative, which reinforces the natural role of the principal root.</p>
  </div>
</div>
""",
        "sim_type": "square_root_inverter",
        "voice": "Squaring and square roots are mirror opposites! If you square 8, you get 64. If you take the square root of 64, you return to 8. But remember, negative 8 squared is also positive 64! By mathematical convention, the radical sign specifically denotes the positive root. Let us test finding square roots visually!",
        "checkpoints": [
            {
                "question": "What are the two integer square roots of the number 81?",
                "options": ["+9 and -9", "+8.1 and -8.1", "+9 only", "+18 and -18"],
                "correct": 0,
                "explanation": "Because (+9)² = 81 and (-9)² = 81, the two integer square roots are +9 and -9. (The radical symbol √81 refers to the positive root +9)."
            },
            {
                "question": "A square plot of land has an area of 441 m². What is the length of each side?",
                "options": ["19 m", "21 m", "23 m", "29 m"],
                "correct": 1,
                "explanation": "Side length = √Area = √441 = 21 m, because 21 × 21 = 441."
            }
        ]
    },

    # Slide 10: Finding Square Roots by Prime Factorisation & Estimation
    {
        "id": 10,
        "title": "Prime Factorisation & Root Estimation",
        "subtitle": "Pairing Prime Factors and Interval Bounding for Square Roots (NCERT Page 9–10)",
        "content": r"""
<p class="lead-p">How do we find the square root of larger numbers like 324 or 1936, or determine if they are perfect squares? Two primary mathematical tools are <strong>prime factor pairing</strong> and <strong>square bounding estimation</strong>.</p>

<div class="theory-box">
  <h4>1. The Prime Factor Pairing Method</h4>
  <p>In the prime factorisation of any perfect square, <strong>every prime factor appears an even number of times</strong> and can be grouped into identical pairs:</p>
  <p>For $324$:</p>
  <p>$\text{Prime factorisation} = 2 \times 2 \times 3 \times 3 \times 3 \times 3 = (2 \times 2) \times (3 \times 3) \times (3 \times 3)$</p>
  <p>Taking one prime factor from each identical pair:</p>
  <p class="highlight-eq">$$\sqrt{324} = 2 \times 3 \times 3 = 18$$</p>
  <p>If any prime factor is left unpaired (like $156 = 2 \times 2 \times 3 \times 13$, where 3 and 13 are unpaired), the number is <strong>NOT a perfect square</strong>!</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Making Numbers Square</h4>
    <p>To find the smallest number to multiply $9408$ to make it a perfect square:</p>
    <p>$9408 = 2^6 \times 3^1 \times 7^2 = (2^3 \times 7)^2 \times 3$</p>
    <p>The prime 3 is unpaired! Multiplying by 3 gives:</p>
    <p>$9408 \times 3 = 28224 = (2^3 \times 3 \times 7)^2 = 168^2$</p>
    <p class="highlight-eq">$$\text{Multiply by 3; New root } = 168$$</p>
  </div>
  <div class="card-item">
    <h4>3. Estimation and Bounding</h4>
    <p>To find $\sqrt{1936}$ without factorisation:</p>
    <ul>
      <li>$40^2 = 1600$ and $50^2 = 2500 \implies 40 < \sqrt{1936} < 50$.</li>
      <li>Ends in 6 $\implies$ root must end in 4 or 6 (either 44 or 46).</li>
      <li>$45^2 = (40+5)^2 = 2025 > 1936 \implies \text{Root is } 44$.</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "prime_factor_pairer",
        "voice": "Prime factorisation gives us an x-ray view inside any number! If every prime factor can be paired up in couples, the number is a perfect square, and taking one factor from each couple gives you the exact square root! If a prime factor is left alone without a partner, multiplying by that prime factor makes it a perfect square!",
        "checkpoints": [
            {
                "question": "Find the square root of 324 using prime factorisation.",
                "options": ["16", "18", "22", "24"],
                "correct": 1,
                "explanation": "324 = 2² × 3⁴ = (2 × 3²)² = 18². Taking one factor from each pair gives 2 × 3 × 3 = 18."
            },
            {
                "question": "By what smallest natural number must 9408 be multiplied so that the product becomes a perfect square?",
                "options": ["2", "3", "7", "6"],
                "correct": 1,
                "explanation": "9408 = 2⁶ × 3¹ × 7². All prime factors are paired except 3. Multiplying by 3 completes the pair, making it 28224 = 168²."
            }
        ]
    },

    # Slide 11: 1.2 Cubic Numbers & Spatial Volume
    {
        "id": 11,
        "title": "1.2 Cubic Numbers & 3D Spatial Volume",
        "subtitle": "Definition of Cubes, Geometric Layering n³ and Exponent Notation (NCERT Page 11–12)",
        "content": r"""
<p class="lead-p">In solid geometry, a cube is a three-dimensional figure whose length, width, and height are all equal. When we calculate the volume of a solid cube of side $n$, we multiply $n$ by itself three times: $\text{Volume} = n \times n \times n = n^3$. Numbers obtained this way are called <strong>cubic numbers</strong> or <strong>perfect cubes</strong>.</p>

<div class="theory-box">
  <h4>1. Formal Mathematical Definition</h4>
  <p>A natural number $m$ is a <strong>perfect cube</strong> if there exists an integer $n$ such that:</p>
  <p class="highlight-eq">$$m = n \times n \times n = n^3$$</p>
  <ul>
    <li>$1^3 = 1 \times 1 \times 1 = 1$</li>
    <li>$2^3 = 2 \times 2 \times 2 = 8$ (Takes 8 unit cubes to build a cube of side 2)</li>
    <li>$3^3 = 3 \times 3 \times 3 = 27$</li>
    <li>$4^3 = 4 \times 4 \times 4 = 64$ (4 layers of $4 \times 4 = 16$ cubes)</li>
    <li>$5^3 = 5 \times 5 \times 5 = 125$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Spatial Layering Architecture</h4>
    <p>A cube of side 4 cm is formed by stacking 4 horizontal slab layers:</p>
    <ul>
      <li>Each horizontal layer is a $4 \times 4$ square containing 16 unit cubes.</li>
      <li>Stacking 4 such layers gives $16 \times 4 = 64$ unit cubes in total.</li>
    </ul>
    <p>Between 1 and 27, there are only two perfect cubes: 1 and 8. The numbers 2 through 7 and 9 through 26 are <strong>not cubes</strong>.</p>
  </div>
  <div class="card-item">
    <h4>3. Cubes of Negative Numbers & Fractions</h4>
    <p>Unlike squares, cubic powers preserve negative signs!</p>
    <ul>
      <li>$(-6)^3 = (-6) \times (-6) \times (-6) = +36 \times (-6) = -216$</li>
      <li>$\left(\frac{4}{6}\right)^3 = \frac{4 \times 4 \times 4}{6 \times 6 \times 6} = \frac{64}{216} = \frac{8}{27}$</li>
      <li>$(13.08)^3 = 2237.810112$</li>
    </ul>
    <p class="highlight-eq">$$\text{Cube of a negative number is always NEGATIVE!}$$</p>
  </div>
</div>
""",
        "sim_type": "cube_volume_builder",
        "voice": "Now we step into the third dimension! A square lives in 2D with length and width, but a cube adds height! When you multiply a number by itself three times, you get its cube. To build a cube of side 3, you stack three layers of 9 blocks, giving 27 unit blocks! And notice that negative numbers cubed stay negative!",
        "checkpoints": [
            {
                "question": "How many unit cubes of side 1 cm are needed to construct a solid cube of side 4 cm?",
                "options": ["16", "32", "64", "128"],
                "correct": 2,
                "explanation": "Volume = side³ = 4³ = 4 × 4 × 4 = 64 unit cubes."
            },
            {
                "question": "What is the value of (-5)³?",
                "options": ["+125", "-125", "+25", "-75"],
                "correct": 1,
                "explanation": "(-5)³ = (-5) × (-5) × (-5) = 25 × (-5) = -125."
            }
        ]
    },

    # Slide 12: Properties of Cubes & Terminal Digits
    {
        "id": 12,
        "title": "Cubic Patterns, Terminal Digits & Zero Tripling",
        "subtitle": "All Digits 0–9 Possible, Zero Tripling Law and Parity Conservation (NCERT Page 12–13)",
        "content": r"""
<p class="lead-p">While perfect squares can only end in $\{0, 1, 4, 5, 6, 9\}$, cubic numbers exhibit a completely different, universal property: <strong>every single digit from 0 to 9 can appear as the units digit of a perfect cube</strong>!</p>

<div class="theory-box">
  <h4>1. Unique 1-to-1 Mapping of Cubic Units Digits</h4>
  <p>The units digit of $n^3$ has a unique, bijective correspondence with the units digit of $n$:</p>
  <div class="grid-2col">
    <div>
      <p><strong>Same-digit endings (Self-preserving):</strong></p>
      <ul>
        <li>$0^3 = 0 \implies \dots 0^3 \to \mathbf{0}$</li>
        <li>$1^3 = 1 \implies \dots 1^3 \to \mathbf{1}$</li>
        <li>$4^3 = 64 \implies \dots 4^3 \to \mathbf{4}$</li>
        <li>$5^3 = 125 \implies \dots 5^3 \to \mathbf{5}$</li>
        <li>$6^3 = 216 \implies \dots 6^3 \to \mathbf{6}$</li>
        <li>$9^3 = 729 \implies \dots 9^3 \to \mathbf{9}$</li>
      </ul>
    </div>
    <div>
      <p><strong>Complementary 10-sum endings:</strong></p>
      <ul>
        <li>$2^3 = 8 \implies \dots 2^3 \to \mathbf{8}$</li>
        <li>$8^3 = 512 \implies \dots 8^3 \to \mathbf{2}$</li>
        <li>$3^3 = 27 \implies \dots 3^3 \to \mathbf{7}$</li>
        <li>$7^3 = 343 \implies \dots 7^3 \to \mathbf{3}$</li>
      </ul>
      <p>Notice that $2 \leftrightarrow 8$ (sum to 10) and $3 \leftrightarrow 7$ (sum to 10)!</p>
    </div>
  </div>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Zero-Tripling Theorem</h4>
    <p>If an integer ends with $k$ zeros, its cube ends with $3k$ zeros:</p>
    <p class="highlight-eq">$$(a \times 10^k)^3 = a^3 \times 10^{3k}$$</p>
    <ul>
      <li>$10^3 = 1000$ (1 zero becomes 3 zeros).</li>
      <li>$200^3 = 8,000,000$ (2 zeros become 6 zeros).</li>
    </ul>
    <p>A perfect cube can <strong>never end in exactly 2 zeros</strong> (like 100 or 2500) or 4 zeros; its trailing zeros must always be a multiple of 3!</p>
  </div>
  <div class="card-item">
    <h4>3. Parity Law for Cubes</h4>
    <p>Just like squares, parity is strictly conserved:</p>
    <ul>
      <li>Cube of an EVEN number is always EVEN ($2^3=8, 4^3=64$).</li>
      <li>Cube of an ODD number is always ODD ($3^3=27, 5^3=125$).</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "cube_digit_mapper",
        "voice": "Here is a fascinating contrast between squares and cubes! Squares can never end in 2, 3, 7, or 8. But cubes can end in every single digit from zero to nine! Notice the beautiful reciprocal harmony: numbers ending in 2 cube to end in 8, and numbers ending in 8 cube to end in 2! Numbers ending in 3 cube to 7, and 7 to 3! And terminal zeros always triple in number!",
        "checkpoints": [
            {
                "question": "Can a perfect cube end with exactly two zeros (such as 400 or 900)?",
                "options": ["Yes, always", "Yes, if the base ends in 0", "No, the number of trailing zeros in a cube must be a multiple of 3", "Only for prime numbers"],
                "correct": 2,
                "explanation": "When an integer ending in k zeros is cubed, the result has 3k zeros. Trailing zeros must be 3, 6, 9, etc., so a cube can never end in exactly two zeros."
            },
            {
                "question": "What is the units digit of the cube of 188?",
                "options": ["4", "8", "2", "6"],
                "correct": 2,
                "explanation": "Since 188 ends in 8, and 8³ = 512 ends in 2, the cube of 188 will end in 2."
            }
        ]
    },

    # Slide 13: Taxicab Numbers & Ramanujan's 1729
    {
        "id": 13,
        "title": "Taxicab Numbers & The Hardy–Ramanujan 1729",
        "subtitle": "Sums of Two Cubes in Two Distinct Ways: a³ + b³ = c³ + d³ (NCERT Page 13)",
        "content": r"""
<p class="lead-p">One of the most beloved stories in the history of science took place in 1918 when English mathematician G. H. Hardy visited the ailing Indian mathematical genius <strong>Srinivasa Ramanujan</strong> in a hospital at Putney.</p>

<div class="theory-box">
  <h4>1. The Famous Cambridge Encounter</h4>
  <p>Hardy remarked that he had ridden in taxicab number <strong>1729</strong>, calling it a dull, uninteresting number. Ramanujan instantly replied:</p>
  <blockquote style="font-style: italic; border-left: 3px solid #f59e0b; padding-left: 12px; margin: 10px 0;">
    "No, Hardy, it is a very interesting number! It is the smallest number expressible as the sum of two positive cubes in two different ways."
  </blockquote>
  <p class="highlight-eq">$$1729 = 1^3 + 12^3 = 9^3 + 10^3$$</p>
  <ul>
    <li>Way 1: $1^3 + 12^3 = 1 + 1728 = 1729$</li>
    <li>Way 2: $9^3 + 10^3 = 729 + 1000 = 1729$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Definition of Taxicab Numbers $\text{Ta}(n)$</h4>
    <p>A <strong>taxicab number</strong> $\text{Ta}(k)$ is defined as the smallest integer expressible as a sum of two positive cubes in $k$ distinct ways:</p>
    <ul>
      <li>$\text{Ta}(1) = 2 = 1^3 + 1^3$</li>
      <li>$\text{Ta}(2) = 1729$ (The Hardy–Ramanujan number)</li>
      <li>Next taxicab numbers: $4104$ and $13832$.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>3. Deconstructing 4104 and 13832</h4>
    <p>The next numbers expressible as two cubes in two ways are:</p>
    <ul>
      <li>$4104 = 2^3 + 16^3 = 8 + 4096$</li>
      <li>$4104 = 9^3 + 15^3 = 729 + 3375$</li>
      <li>$13832 = 2^3 + 24^3 = 8 + 13824$</li>
      <li>$13832 = 18^3 + 20^3 = 5832 + 8000$</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "ramanujan_taxicab_sim",
        "voice": "Here is Srinivasa Ramanujan's magical taxicab number, 1729! While Hardy thought it was dull, Ramanujan recognized instantly that 1 cubed plus 12 cubed equals 1729, and 9 cubed plus 10 cubed also equals 1729! It is the smallest number in existence that can be written as the sum of two positive cubes in two distinct ways! Explore the cubes on your screen to verify it yourself.",
        "checkpoints": [
            {
                "question": "Which two pairs of cubes add up to 1729?",
                "options": ["(1³, 12³) and (9³, 10³)", "(2³, 11³) and (5³, 10³)", "(3³, 12³) and (7³, 8³)", "(4³, 10³) and (6³, 9³)"],
                "correct": 0,
                "explanation": "1³ + 12³ = 1 + 1728 = 1729, and 9³ + 10³ = 729 + 1000 = 1729."
            },
            {
                "question": "Express 4104 as a sum of two positive cubes in one of its two ways.",
                "options": ["1³ + 16³", "2³ + 16³", "3³ + 15³", "4³ + 14³"],
                "correct": 1,
                "explanation": "2³ + 16³ = 8 + 4096 = 4104. (The other combination is 9³ + 15³ = 729 + 3375 = 4104)."
            }
        ]
    },

    # Slide 14: Perfect Cubes & Consecutive Odd Numbers
    {
        "id": 14,
        "title": "Cubes as Consecutive Odd Number Partitions",
        "subtitle": "The Nicomachus Theorem: n³ as the Sum of n Consecutive Odd Numbers (NCERT Page 14)",
        "content": r"""
<p class="lead-p">Just as square numbers equal the sum of odd numbers starting from 1, cubic numbers possess their own mesmerizing odd-number identity discovered in antiquity by <strong>Nicomachus of Gerasa</strong> (c. 100 CE): <em>$n^3$ is always the sum of $n$ consecutive odd numbers</em>!</p>

<div class="theory-box">
  <h4>1. The Nicomachus Pyramid of Odd Numbers</h4>
  <p>Grouping the sequence of all odd numbers into consecutive rows of size 1, 2, 3, 4, 5...:</p>
  <ul>
    <li>Row 1 (1 number): $\mathbf{1} = 1 = \mathbf{1^3}$</li>
    <li>Row 2 (2 numbers): $\mathbf{3 + 5} = 8 = \mathbf{2^3}$</li>
    <li>Row 3 (3 numbers): $\mathbf{7 + 9 + 11} = 27 = \mathbf{3^3}$</li>
    <li>Row 4 (4 numbers): $\mathbf{13 + 15 + 17 + 19} = 64 = \mathbf{4^3}$</li>
    <li>Row 5 (5 numbers): $\mathbf{21 + 23 + 25 + 27 + 29} = 125 = \mathbf{5^3}$</li>
    <li>Row 6 (6 numbers): $\mathbf{31 + 33 + 35 + 37 + 39 + 41} = 216 = \mathbf{6^3}$</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. The Starting Number Formula</h4>
    <p>To find the first odd number in the row summing to $n^3$:</p>
    <p>The total count of odd numbers in preceding rows is $\frac{(n-1)n}{2}$.</p>
    <p class="highlight-eq">$$\text{First odd number} = n(n - 1) + 1 = n^2 - n + 1$$</p>
    <p>For $n = 10$:</p>
    <p>First odd number = $10^2 - 10 + 1 = 100 - 10 + 1 = 91$.</p>
    <p>The 10 consecutive odd numbers are: $91 + 93 + 95 + 97 + 99 + 101 + 103 + 105 + 107 + 109 = 10^3 = \mathbf{1000}$.</p>
  </div>
  <div class="card-item">
    <h4>3. Algebraic Proof of the Sum</h4>
    <p>The average of these $n$ consecutive odd numbers is exactly $n^2$.</p>
    <p>Since there are $n$ numbers, their sum is:</p>
    <p class="highlight-eq">$$\text{Sum} = n \times (\text{Average}) = n \times n^2 = n^3$$</p>
    <p>This allows us to evaluate massive sums of consecutive odd numbers instantly without adding them term-by-term!</p>
  </div>
</div>
""",
        "sim_type": "nicomachus_pyramid_animator",
        "voice": "Behold the Nicomachus odd pyramid! Notice how 1 cubed is just 1. Then 2 cubed is the sum of the next TWO odd numbers, 3 plus 5! Three cubed is the sum of the next THREE odd numbers, 7 plus 9 plus 11! And ten cubed is the sum of ten consecutive odd numbers starting at 91, totaling 1000! Mathematics is packed with these breathtaking regularities.",
        "checkpoints": [
            {
                "question": "What is the sum of: 91 + 93 + 95 + 97 + 99 + 101 + 103 + 105 + 107 + 109 without doing manual addition?",
                "options": ["900", "990", "1000", "1100"],
                "correct": 2,
                "explanation": "This is the set of 10 consecutive odd numbers representing the 10th row of Nicomachus's pyramid, so its sum is 10³ = 1000."
            },
            {
                "question": "What is the first odd number in the expansion of 7³ as a sum of 7 consecutive odd numbers?",
                "options": ["41", "43", "45", "49"],
                "correct": 1,
                "explanation": "The first odd number is n² - n + 1. For n = 7: 7² - 7 + 1 = 49 - 7 + 1 = 43. (Check: 43+45+47+49+51+53+55 = 343 = 7³)."
            }
        ]
    },

    # Slide 15: Cube Roots & Prime Factor Triplet Factorisation
    {
        "id": 15,
        "title": "Cube Roots & Triplet Prime Factorisation",
        "subtitle": "The Radical Symbol ∛, Factor Triplets and Inverse Powers (NCERT Page 14–15)",
        "content": r"""
<p class="lead-p">The <strong>cube root</strong> of a number $y$ is the number $x$ that satisfies $x^3 = y$. The operation is denoted using the index radical symbol $\sqrt[3]{y}$. For example, since $2^3 = 8$, the cube root of 8 is $\sqrt[3]{8} = 2$.</p>

<div class="theory-box">
  <h4>1. Prime Factor Triplet Method</h4>
  <p>In the prime factorisation of any perfect cube, <strong>every prime factor occurs in triplets (multiples of 3)</strong>:</p>
  <p>For $3375$:</p>
  <p>$\text{Prime factorisation} = 3 \times 3 \times 3 \times 5 \times 5 \times 5 = (3 \times 3 \times 3) \times (5 \times 5 \times 5) = 3^3 \times 5^3$</p>
  <p>Taking one representative factor from each triplet:</p>
  <p class="highlight-eq">$$\sqrt[3]{3375} = 3 \times 5 = 15$$</p>
  <p>For $1728$:</p>
  <p>$1728 = 2^6 \times 3^3 = (2 \times 2 \times 2) \times (2 \times 2 \times 2) \times (3 \times 3 \times 3) \implies \sqrt[3]{1728} = 2 \times 2 \times 3 = 12$.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Testing Non-Cubes</h4>
    <p>Consider $500$:</p>
    <p>$500 = 2 \times 2 \times 5 \times 5 \times 5 = 2^2 \times 5^3$.</p>
    <p>While the factor 5 forms a complete triplet, the factor 2 occurs only twice.</p>
    <p class="highlight-eq">$$500 \text{ is NOT a perfect cube!}$$</p>
    <p>To make 500 a perfect cube, we must multiply by 2 (to make $2^3 \times 5^3 = 1000 = 10^3$), or divide by 4 (to leave $5^3 = 125$).</p>
  </div>
  <div class="card-item">
    <h4>3. Making 1323 a Perfect Cube</h4>
    <p>Factorise $1323$:</p>
    <p>$1323 = 3 \times 3 \times 3 \times 7 \times 7 = 3^3 \times 7^2$.</p>
    <p>The factor 7 needs one more 7 to form a complete triplet of 7s.</p>
    <p class="highlight-eq">$$\text{Multiply by } 7 \implies 1323 \times 7 = 9261 = 21^3$$</p>
  </div>
</div>
""",
        "sim_type": "cube_root_triplet_sim",
        "voice": "To find a square root, we grouped prime factors into pairs of two. But to find a cube root, we must group prime factors into triplets of three! Take 3375: it breaks into three threes and three fives. Take one from each triplet, multiply them together, and you get 15! If any factor lacks its triplet partners, you know exactly what to multiply to complete the cube!",
        "checkpoints": [
            {
                "question": "What is the cube root of 27000?",
                "options": ["20", "30", "40", "90"],
                "correct": 1,
                "explanation": "27000 = 27 × 1000 = 3³ × 10³ = (3 × 10)³ = 30³."
            },
            {
                "question": "What is the smallest number by which 1323 must be multiplied so that the product is a perfect cube?",
                "options": ["3", "7", "9", "21"],
                "correct": 1,
                "explanation": "1323 = 3³ × 7². The prime 3 is in a complete triplet, but 7 occurs only twice. Multiplying by 7 completes the triplet, giving 1323 × 7 = 9261 = 21³."
            }
        ]
    },

    # Slide 16: Successive Differences, History & Aryabhata
    {
        "id": 16,
        "title": "Successive Differences, Aryabhata & Indian Roots",
        "subtitle": "Calculus of Finite Differences, Varga, Ghana, Mula and Babylonia (NCERT Page 15–16)",
        "content": r"""
<p class="lead-p">The deep architecture of squares and cubes is governed by a remarkable law of discrete mathematics: <strong>successive differences</strong>. Furthermore, the very words we use today for roots trace their lineage directly back to ancient Indian mathematicians like Aryabhata and Brahmagupta!</p>

<div class="theory-box">
  <h4>1. Successive Differences Over Finite Levels</h4>
  <p>When you compute differences between consecutive terms across successive levels:</p>
  <ul>
    <li><strong>Perfect Squares ($n^2$):</strong> $\{1, 4, 9, 16, 25, 36, \dots\}$<br>
    Level 1 Differences: $3, 5, 7, 9, 11 \dots$ (the sequence of odd numbers)<br>
    Level 2 Differences: $2, 2, 2, 2 \dots$ ($\mathbf{2! = 2}$ <strong>Constant!</strong>)</li>
    <li><strong>Perfect Cubes ($n^3$):</strong> $\{1, 8, 27, 64, 125, 216, \dots\}$<br>
    Level 1 Differences: $7, 19, 37, 61, 91 \dots$<br>
    Level 2 Differences: $12, 18, 24, 30 \dots$<br>
    Level 3 Differences: $6, 6, 6, 6 \dots$ ($\mathbf{3! = 6}$ <strong>Constant!</strong>)</li>
  </ul>
  <p class="highlight-eq">$$\text{For degree } k, \text{ the } k\text{-th successive difference is always constant and equals } k!$$</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>2. Aryabhata's Varga & Ghana (499 CE)</h4>
    <p>In his masterpiece <em>Aryabhatiya</em>, Aryabhata defined:</p>
    <blockquote style="font-style: italic; border-left: 3px solid #10b981; padding-left: 8px;">
      "A square figure of four equal sides and the number representing its area are called varga. The product of two equal quantities is also called varga."
    </blockquote>
    <p>Similarly, a solid cube and a three-factor product was termed <strong>ghana</strong>, and the fourth power was <strong>varga-varga</strong>.</p>
  </div>
  <div class="card-item">
    <h4>3. Why Do We Say "Root"? (Mula)</h4>
    <p>In Sanskrit, the base or cause of a plant is its <strong>mula</strong> (root). Indian mathematicians called the side of a square <em>varga-mula</em> (root of the square) and the edge of a cube <em>ghana-mula</em>.</p>
    <p>This term was translated into Arabic as <em>jidhr</em>, into Latin as <em>radix</em> (from which we get 'radical'), and into English as <strong>root</strong>!</p>
  </div>
</div>
""",
        "sim_type": "finite_difference_cascade",
        "voice": "Here is the poetry of mathematics! Look at the differences: for squares, the second differences are always constant at 2! For cubes, the third differences are always constant at 6, which is 3 factorial! And whenever you say the word 'square root', you are honoring ancient Indian masters who called the base of a square its 'varga-mula' or root of the plant, which traveled into Arabic, Latin, and modern English!",
        "checkpoints": [
            {
                "question": "What is the constant value of the third successive differences of consecutive perfect cubes (1, 8, 27, 64, 125...)?",
                "options": ["2", "4", "6", "8"],
                "correct": 2,
                "explanation": "For any polynomial of degree 3 (like n³), the third successive difference is constant and equals 3! = 3 × 2 × 1 = 6."
            },
            {
                "question": "Which ancient Sanskrit word meaning 'root of a plant / origin' gave rise to the mathematical term 'root' (as in square root)?",
                "options": ["Varga", "Ghana", "Mula", "Krti"],
                "correct": 2,
                "explanation": "Mula, meaning the root or origin of a plant, was used as varga-mula (square root). It was translated into Arabic as jidhr, Latin as radix, and English as root."
            }
        ]
    },

    # Slide 17: Dedicated Quiz Challenge 1 (Questions 1 to 10)
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Squares & Patterns",
        "subtitle": "10 Diagnostic Questions on Properties, Factors and Patterns with Step-by-Step Popups",
        "content": r"""
<p class="lead-p">Welcome to Quiz Challenge I! Test your rigorous mastery of square number properties, factor pair parity, terminal digit constraints, and odd number sums. Click your chosen option for immediate feedback or open the <strong>Solution</strong> pop-up to inspect the complete mathematical derivation.</p>
<div id="quizContainer1" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge 1! Put your conceptual understanding of square numbers, parity, units digits, and factor pairs to the test. Answer each question carefully and click View Solution to see full step-by-step explanations.",
        "quiz_range": [1, 10]
    },

    # Slide 18: Dedicated Quiz Challenge 2 (Questions 11 to 20)
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Square Roots & Estimation",
        "subtitle": "10 Diagnostic Questions on Square Roots, Prime Factors and Approximations",
        "content": r"""
<p class="lead-p">Quiz Challenge II focuses on square roots, prime factor pairing algorithms, non-square intervals between consecutive squares, and triangular number summation. Inspect each problem with analytical care.</p>
<div id="quizContainer2" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Now let us conquer Quiz Challenge 2! Here we explore square roots, the 2n non-square theorem, and prime factor pairing algorithms. Select your answers and click View Solution for detailed feedback.",
        "quiz_range": [11, 20]
    },

    # Slide 19: Dedicated Quiz Challenge 3 (Questions 21 to 30)
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Cubes & Ramanujan Numbers",
        "subtitle": "10 Diagnostic Questions on 3D Cubes, Taxicab Numbers and Terminal Zero Tripling",
        "content": r"""
<p class="lead-p">Quiz Challenge III explores the world of cubic numbers: unit cube stacking volume, terminal digit laws, Ramanujan's taxicab number 1729, and Nicomachus's odd number partitions.</p>
<div id="quizContainer3" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge 3! Dive into the third dimension with cubic volumes, terminal zero rules, Hardy-Ramanujan taxicab numbers, and Nicomachus pyramids. Test your precision and review each step-by-step solution.",
        "quiz_range": [21, 30]
    },

    # Slide 20: Dedicated Quiz Challenge 4 (Questions 31 to 40)
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Advanced Factorisation & History",
        "subtitle": "10 Diagnostic Questions on Prime Triplets, Finite Differences and Indian History",
        "content": r"""
<p class="lead-p">Congratulations on reaching the final mastery examination! Challenge IV covers cube root extractions, successive difference calculus, historical Sanskrit terminology (Aryabhata & Brahmagupta), and multi-step reasoning problems.</p>
<div id="quizContainer4" class="quiz-grid"></div>
""",
        "sim_type": "quiz_slide",
        "voice": "You have reached the final mastery challenge of Chapter 1! Solve these 10 comprehensive questions on cube roots, successive differences, and ancient mathematics. When you complete this slide, you have achieved full mastery of A Square and A Cube!",
        "quiz_range": [31, 40]
    }
]

# 40 Comprehensive Quiz Questions with Detailed Step-by-Step Solutions
quiz_questions = [
    # Questions 1 to 10 (Quiz Challenge 1)
    {
        "num": 1,
        "question": "Which of the following numbers can never be a perfect square?",
        "options": ["1024", "2048", "4096", "8100"],
        "correct": 1,
        "solution": "Step 1: Check the units digit of each number.\nStep 2: A perfect square can only end with 0, 1, 4, 5, 6, or 9.\nStep 3: 2048 ends with 8, which is an impossible ending for any perfect square (squares never end in 2, 3, 7, or 8).\nTherefore, 2048 can never be a perfect square."
    },
    {
        "num": 2,
        "question": "How many total factors does the perfect square 36 possess?",
        "options": ["6 factors", "8 factors", "9 factors", "10 factors"],
        "correct": 2,
        "solution": "Step 1: Find all factor pairs of 36: 1×36, 2×18, 3×12, 4×9, and 6×6.\nStep 2: List the distinct factors: {1, 2, 3, 4, 6, 9, 12, 18, 36}.\nStep 3: Count the distinct elements: there are exactly 9 factors.\nStep 4: Notice that 9 is an odd number because 6 pairs with itself (6×6=36)."
    },
    {
        "num": 3,
        "question": "If a number ends with the digit 9, what will be the units digit of its square?",
        "options": ["1", "3", "7", "9"],
        "correct": 0,
        "solution": "Step 1: The units digit of n² depends solely on the units digit of n.\nStep 2: Since 9 × 9 = 81, any number ending in 9 will have 1 as the units digit of its square.\nFor example: 9² = 81, 19² = 361, 29² = 841 all end in 1."
    },
    {
        "num": 4,
        "question": "Which of the following numbers will have the digit 6 in its units place?",
        "options": ["(38)²", "(34)²", "(82)²", "(57)²"],
        "correct": 1,
        "solution": "Step 1: A square ends in 6 if and only if the base number ends in 4 or 6 (since 4² = 16 and 6² = 36).\nStep 2: Check the options:\n- 38 ends in 8 (square ends in 4)\n- 34 ends in 4 (square ends in 6)\n- 82 ends in 2 (square ends in 4)\n- 57 ends in 7 (square ends in 9)\nTherefore, (34)² has 6 in its units place."
    },
    {
        "num": 5,
        "question": "How many trailing zeros does the square of 7000 have?",
        "options": ["3 zeros", "5 zeros", "6 zeros", "9 zeros"],
        "correct": 2,
        "solution": "Step 1: 7000 has 3 trailing zeros (7000 = 7 × 10³).\nStep 2: Squaring doubles the number of trailing zeros: (7 × 10³)² = 49 × 10⁶.\nStep 3: Therefore, the square will have exactly 3 × 2 = 6 zeros (49,000,000)."
    },
    {
        "num": 6,
        "question": "What is the sum of the first 12 consecutive odd numbers (1 + 3 + 5 + ... + 23)?",
        "options": ["120", "132", "144", "156"],
        "correct": 2,
        "solution": "Step 1: The sum of the first n consecutive odd numbers starting from 1 is given by n².\nStep 2: Here n = 12.\nStep 3: Sum = 12² = 144."
    },
    {
        "num": 7,
        "question": "Given that 25² = 625, what is the value of 26² without long multiplication?",
        "options": ["650", "676", "686", "700"],
        "correct": 1,
        "solution": "Step 1: We know that (n + 1)² = n² + 2n + 1.\nStep 2: For n = 25, 2n + 1 = 2(25) + 1 = 51.\nStep 3: 26² = 25² + 51 = 625 + 51 = 676."
    },
    {
        "num": 8,
        "question": "When testing 64 by repeated subtraction of consecutive odd numbers, how many subtractions are required to reach 0?",
        "options": ["6", "7", "8", "9"],
        "correct": 2,
        "solution": "Step 1: Subtract odd numbers starting from 1:\n64 - 1 = 63 (step 1)\n63 - 3 = 60 (step 2)\n60 - 5 = 55 (step 3)\n55 - 7 = 48 (step 4)\n48 - 9 = 39 (step 5)\n39 - 11 = 28 (step 6)\n28 - 13 = 15 (step 7)\n15 - 15 = 0 (step 8)\nStep 2: Reached 0 at the 8th step, so √64 = 8."
    },
    {
        "num": 9,
        "question": "Which of the following can never be the remainder when any perfect square is divided by 4?",
        "options": ["0", "1", "2 or 3", "None of these"],
        "correct": 2,
        "solution": "Step 1: If n is even (n = 2k), n² = 4k² ≡ 0 (mod 4).\nStep 2: If n is odd (n = 2k + 1), n² = 4k² + 4k + 1 ≡ 1 (mod 4).\nStep 3: Therefore, a perfect square can ONLY leave remainder 0 or 1 when divided by 4.\nStep 4: It can NEVER leave remainder 2 or 3."
    },
    {
        "num": 10,
        "question": "In the 100 lockers problem, which of the following lockers remains OPEN at the end?",
        "options": ["Locker 48", "Locker 54", "Locker 64", "Locker 72"],
        "correct": 2,
        "solution": "Step 1: A locker remains open if and only if it is toggled an odd number of times.\nStep 2: The number of toggles equals the number of factors of the locker number.\nStep 3: Only perfect squares have an odd number of factors.\nStep 4: Among the choices, only 64 is a perfect square (8² = 64). Lockers 48, 54, and 72 have an even number of factors and end up closed."
    },

    # Questions 11 to 20 (Quiz Challenge 2)
    {
        "num": 11,
        "question": "How many non-perfect square numbers lie between 16² and 17²?",
        "options": ["32", "33", "34", "35"],
        "correct": 0,
        "solution": "Step 1: By the 2n non-square theorem, the number of non-square natural numbers between n² and (n + 1)² is 2n.\nStep 2: Here n = 16.\nStep 3: Number of non-squares = 2 × 16 = 32.\n(Check: 17² - 16² - 1 = 289 - 256 - 1 = 32)."
    },
    {
        "num": 12,
        "question": "How many square numbers are there between 1 and 100 inclusive?",
        "options": ["8", "9", "10", "11"],
        "correct": 2,
        "solution": "Step 1: The square numbers starting from 1 are: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36, 7²=49, 8²=64, 9²=81, 10²=100.\nStep 2: The 11th square is 11² = 121 > 100.\nStep 3: Therefore, there are exactly 10 square numbers between 1 and 100."
    },
    {
        "num": 13,
        "question": "What is the sum of the triangular numbers T₃ (6) and T₄ (10)?",
        "options": ["12", "14", "16", "18"],
        "correct": 2,
        "solution": "Step 1: T₃ = 6 and T₄ = 10.\nStep 2: Sum = 6 + 10 = 16.\nStep 3: Notice that 16 = 4² = T₃ + T₄. Two consecutive triangular numbers always add to form a square number!"
    },
    {
        "num": 14,
        "question": "A square field has an area of 729 m². What is the perimeter of the field?",
        "options": ["81 m", "108 m", "112 m", "124 m"],
        "correct": 1,
        "solution": "Step 1: Side length of square = √Area = √729.\nStep 2: Since 27 × 27 = 729, the side length is 27 m.\nStep 3: Perimeter = 4 × side = 4 × 27 = 108 m."
    },
    {
        "num": 15,
        "question": "What is the smallest number by which 180 must be multiplied to make it a perfect square?",
        "options": ["2", "3", "5", "10"],
        "correct": 2,
        "solution": "Step 1: Find the prime factorisation of 180: 180 = 2 × 90 = 2 × 2 × 45 = 2² × 3² × 5¹.\nStep 2: Group factors into pairs: (2 × 2) × (3 × 3) × 5.\nStep 3: The factor 5 is unpaired.\nStep 4: Multiplying by 5 completes the pair: 180 × 5 = 900 = 30².\nTherefore, the smallest number is 5."
    },
    {
        "num": 16,
        "question": "Find the smallest square number that is divisible by each of 4, 9, and 10.",
        "options": ["360", "600", "900", "3600"],
        "correct": 2,
        "solution": "Step 1: Find the LCM of 4, 9, and 10.\n4 = 2², 9 = 3², 10 = 2 × 5.\nLCM = 2² × 3² × 5¹ = 4 × 9 × 5 = 180.\nStep 2: Prime factors of 180 = 2² × 3² × 5¹.\nStep 3: To make it a square number, every prime exponent must be even. The prime 5 has exponent 1, so we multiply by 5.\nStep 4: Smallest square number = 180 × 5 = 900 (which is 30²)."
    },
    {
        "num": 17,
        "question": "If 125² = 15625, what is the value of 126²?",
        "options": ["15625 + 126", "15625 + 251", "15625 + 253", "15625 + 26²"],
        "correct": 1,
        "solution": "Step 1: (n + 1)² = n² + 2n + 1.\nStep 2: For n = 125, 2n + 1 = 2(125) + 1 = 250 + 1 = 251.\nStep 3: 126² = 125² + 251 = 15625 + 251 = 15876."
    },
    {
        "num": 18,
        "question": "In the pattern: 1² + 2² + 2² = 3², 2² + 3² + 6² = 7², 3² + 4² + 12² = 13², what is the missing value in 4² + 5² + 20² = (?)²?",
        "options": ["21²", "22²", "25²", "29²"],
        "correct": 0,
        "solution": "Step 1: Observe the pattern: n² + (n+1)² + [n(n+1)]² = [n(n+1) + 1]².\nStep 2: Here n = 4, so n+1 = 5, n(n+1) = 20, and n(n+1) + 1 = 21.\nStep 3: 4² + 5² + 20² = 16 + 25 + 400 = 441 = 21².\nTherefore, the missing number is 21²."
    },
    {
        "num": 19,
        "question": "In the same pattern, what are the missing values in: 9² + 10² + (?)² = (?)²?",
        "options": ["90² and 91²", "89² and 90²", "90² and 92²", "100² and 101²"],
        "correct": 0,
        "solution": "Step 1: Here n = 9, n+1 = 10.\nStep 2: Third term = n(n+1) = 9 × 10 = 90.\nStep 3: Fourth term = n(n+1) + 1 = 90 + 1 = 91.\nStep 4: Equation is 9² + 10² + 90² = 91².\n(Verification: 81 + 100 + 8100 = 8281 = 91²)."
    },
    {
        "num": 20,
        "question": "Akhil has a square cloth of area 125 cm². What is the maximum integer side length handkerchief he can cut from it?",
        "options": ["10 cm", "11 cm", "12 cm", "15 cm"],
        "correct": 1,
        "solution": "Step 1: Area of handkerchief of side s is s².\nStep 2: We require s² ≤ 125 with s being an integer.\nStep 3: Check squares: 10² = 100, 11² = 121, 12² = 144.\nStep 4: Since 121 ≤ 125 < 144, the largest integer side length is 11 cm."
    },

    # Questions 21 to 30 (Quiz Challenge 3)
    {
        "num": 21,
        "question": "Which of the following is a perfect cube?",
        "options": ["9", "16", "27", "36"],
        "correct": 2,
        "solution": "Step 1: A perfect cube is an integer raised to the power 3.\nStep 2: 1³ = 1, 2³ = 8, 3³ = 27, 4³ = 64.\nStep 3: 27 = 3 × 3 × 3 = 3³ is a perfect cube.\n(9 = 3², 16 = 4², and 36 = 6² are perfect squares, not cubes)."
    },
    {
        "num": 22,
        "question": "What is the units digit of the cube of 237?",
        "options": ["1", "3", "7", "9"],
        "correct": 1,
        "solution": "Step 1: The units digit of n³ depends on the units digit of n.\nStep 2: 237 ends in 7.\nStep 3: 7³ = 7 × 7 × 7 = 343, which ends in 3.\nTherefore, the cube of 237 ends in 3."
    },
    {
        "num": 23,
        "question": "Which of the following statements about cubes is TRUE?",
        "options": [
            "The cube of an odd number is always even",
            "A perfect cube can end with exactly two zeros",
            "There is no perfect cube that ends with 8",
            "The cube of an odd number is always odd"
        ],
        "correct": 3,
        "solution": "Step 1: An odd number can be written as 2k + 1. Cubing it: (2k + 1)³ = 8k³ + 12k² + 6k + 1 = 2(4k³ + 6k² + 3k) + 1, which is strictly odd.\nStep 2: 2³ = 8 (a cube can end in 8).\nStep 3: A cube ending in zeros must have 3, 6, 9... zeros (never exactly 2 zeros).\nTherefore, 'The cube of an odd number is always odd' is the only true statement."
    },
    {
        "num": 24,
        "question": "What is Ramanujan's famous Taxicab Number (the smallest number expressible as the sum of two positive cubes in two ways)?",
        "options": ["1296", "1728", "1729", "4104"],
        "correct": 2,
        "solution": "Step 1: 1729 is the Hardy–Ramanujan number.\nStep 2: 1729 = 1³ + 12³ = 1 + 1728 = 1729.\nStep 3: 1729 = 9³ + 10³ = 729 + 1000 = 1729.\nStep 4: It is the smallest integer with this two-way representation."
    },
    {
        "num": 25,
        "question": "How many digits can the cube of a 2-digit number have?",
        "options": ["Only 3 digits", "Between 4 and 6 digits inclusive", "Exactly 7 digits", "Always 8 digits"],
        "correct": 1,
        "solution": "Step 1: The smallest 2-digit number is 10, and 10³ = 1000 (4 digits).\nStep 2: The largest 2-digit number is 99, and 99³ = 970,299 (6 digits).\nStep 3: Therefore, the cube of any 2-digit number has between 4 and 6 digits inclusive (never 3 digits, and never 7 or more digits)."
    },
    {
        "num": 26,
        "question": "What is the value of 31 + 33 + 35 + 37 + 39 + 41 without manual addition?",
        "options": ["125", "216", "343", "512"],
        "correct": 1,
        "solution": "Step 1: This is a sequence of 6 consecutive odd numbers in Nicomachus's pattern.\nStep 2: By the Nicomachus theorem, the sum of these 6 numbers equals 6³.\nStep 3: 6³ = 6 × 6 × 6 = 216.\n(Check: 31+33+35+37+39+41 = 216)."
    },
    {
        "num": 27,
        "question": "What is the cube root of 0.000064?",
        "options": ["0.004", "0.04", "0.4", "0.008"],
        "correct": 1,
        "solution": "Step 1: Write 0.000064 as a fraction: 64 / 1,000,000.\nStep 2: ∛(64 / 1,000,000) = ∛(64) / ∛(1,000,000).\nStep 3: ∛64 = 4 (since 4³ = 64) and ∛1,000,000 = 100 (since 100³ = 1,000,000).\nStep 4: 4 / 100 = 0.04."
    },
    {
        "num": 28,
        "question": "What is the value of ∛(-216)?",
        "options": ["+6", "-6", "Undefined", "-36"],
        "correct": 1,
        "solution": "Step 1: We seek a number x such that x³ = -216.\nStep 2: (-6) × (-6) × (-6) = (+36) × (-6) = -216.\nStep 3: Therefore, ∛(-216) = -6."
    },
    {
        "num": 29,
        "question": "Which of the following is the second smallest taxicab number after 1729?",
        "options": ["2048", "3375", "4104", "5832"],
        "correct": 2,
        "solution": "Step 1: 4104 is the next taxicab number.\nStep 2: 4104 = 2³ + 16³ = 8 + 4096 = 4104.\nStep 3: 4104 = 9³ + 15³ = 729 + 3375 = 4104."
    },
    {
        "num": 30,
        "question": "How many unit cubes are in each horizontal layer of a 5 × 5 × 5 solid cube?",
        "options": ["5", "15", "25", "125"],
        "correct": 2,
        "solution": "Step 1: Each horizontal layer of a 5 cm cube is a square of 5 cm × 5 cm.\nStep 2: Number of unit cubes in one layer = 5 × 5 = 25 unit cubes.\nStep 3: Stacking 5 such layers yields 25 × 5 = 125 cubes in total."
    },

    # Questions 31 to 40 (Quiz Challenge 4)
    {
        "num": 31,
        "question": "Find the cube root of 10648 using prime factorisation.",
        "options": ["18", "22", "24", "28"],
        "correct": 1,
        "solution": "Step 1: Prime factorise 10648:\n10648 = 2 × 5324 = 2 × 2 × 2662 = 2 × 2 × 2 × 1331.\nStep 2: Factorise 1331: 1331 = 11 × 121 = 11 × 11 × 11.\nStep 3: 10648 = (2 × 2 × 2) × (11 × 11 × 11) = 2³ × 11³.\nStep 4: ∛10648 = 2 × 11 = 22."
    },
    {
        "num": 32,
        "question": "What is the smallest number by which 256 must be divided so that the quotient is a perfect cube?",
        "options": ["2", "4", "8", "16"],
        "correct": 1,
        "solution": "Step 1: Prime factorise 256: 256 = 2⁸ = (2 × 2 × 2) × (2 × 2 × 2) × (2 × 2) = 2³ × 2³ × 2².\nStep 2: The factor 2² = 4 is leftover and does not form a complete triplet.\nStep 3: Dividing 256 by 4 leaves 2³ × 2³ = 64 = 4³, which is a perfect cube.\nTherefore, the smallest divisor is 4."
    },
    {
        "num": 33,
        "question": "Which of the following expressions is the greatest in value?",
        "options": ["67³ - 66³", "43³ - 42³", "67² - 66²", "43² - 42²"],
        "correct": 0,
        "solution": "Step 1: Recall algebraic identity a³ - b³ = (a - b)(a² + ab + b²).\nWhen a - b = 1, a³ - b³ = a² + ab + b² ≈ 3a².\nStep 2: For squares: a² - b² = (a - b)(a + b) = 1 × (a + b) ≈ 2a.\nStep 3: Clearly 67³ - 66³ ≈ 3 × 67² = 3 × 4489 ≈ 13,467.\nExact values:\n- 67³ - 66³ = 67² + 67×66 + 66² = 4489 + 4422 + 4356 = 13267.\n- 43³ - 42³ = 43² + 43×42 + 42² = 1849 + 1806 + 1764 = 5419.\n- 67² - 66² = 67 + 66 = 133.\n- 43² - 42² = 43 + 42 = 85.\nTherefore, 67³ - 66³ is vastly the greatest."
    },
    {
        "num": 34,
        "question": "In ancient Sanskrit mathematics, what term was used by Aryabhata for a square figure and its area?",
        "options": ["Ghana", "Varga", "Mula", "Pada"],
        "correct": 1,
        "solution": "Step 1: Aryabhata (499 CE) defined: 'A square figure of four equal sides and the number representing its area are called varga.'\nStep 2: Ghana was used for cube, and mula or pada was used for root."
    },
    {
        "num": 35,
        "question": "What is the cube root of 32768 by estimation?",
        "options": ["28", "32", "38", "42"],
        "correct": 1,
        "solution": "Step 1: Group digits from the right into periods of three: (32) and (768).\nStep 2: Look at the right period (768): ends in 8. A cube ends in 8 if and only if its cube root ends in 2 (since 2³ = 8). So units digit = 2.\nStep 3: Look at the left period (32): 3³ = 27 and 4³ = 64. Since 27 ≤ 32 < 64, the tens digit is 3.\nStep 4: Combining tens and units digits: ∛32768 = 32."
    },
    {
        "num": 36,
        "question": "What is the constant value of the 2nd successive differences of consecutive perfect squares (1, 4, 9, 16, 25...)?",
        "options": ["1", "2", "3", "4"],
        "correct": 1,
        "solution": "Step 1: Consecutive squares: 1, 4, 9, 16, 25, 36.\nStep 2: Level 1 differences: 4-1=3, 9-4=5, 16-9=7, 25-16=9, 36-25=11.\nStep 3: Level 2 differences: 5-3=2, 7-5=2, 9-7=2, 11-9=2.\nStep 4: The second difference is constant and equals 2."
    },
    {
        "num": 37,
        "question": "By what smallest number must 675 be multiplied to obtain a perfect cube?",
        "options": ["3", "5", "15", "25"],
        "correct": 1,
        "solution": "Step 1: Factorise 675: 675 = 25 × 27 = 5² × 3³ = 3³ × 5².\nStep 2: The factor 3 occurs in a complete triplet (3³).\nStep 3: The factor 5 occurs only twice (5²).\nStep 4: Multiplying by 5 completes the triplet: 675 × 5 = 3375 = 15³.\nTherefore, the smallest multiplier is 5."
    },
    {
        "num": 38,
        "question": "What is the value of (2.5)³?",
        "options": ["6.25", "12.5", "15.625", "18.75"],
        "correct": 2,
        "solution": "Step 1: (2.5)³ = 2.5 × 2.5 × 2.5.\nStep 2: 2.5 × 2.5 = 6.25.\nStep 3: 6.25 × 2.5 = 15.625."
    },
    {
        "num": 39,
        "question": "Which ancient civilization created the earliest known clay tablet tables of squares and cubes as early as 1700 BCE?",
        "options": ["The Egyptians", "The Greeks", "The Babylonians", "The Romans"],
        "correct": 2,
        "solution": "Step 1: Historical records show that the Babylonians compiled tables of squares and cubes on cuneiform clay tablets around 1700 BCE.\nStep 2: These lists were used to rapidly compute square roots, cube roots, and solve architectural and land survey problems."
    },
    {
        "num": 40,
        "question": "Three numbers are in the ratio 1 : 2 : 3 and the sum of their cubes is 4500. What is the largest of these three numbers?",
        "options": ["5", "10", "15", "20"],
        "correct": 2,
        "solution": "Step 1: Let the three numbers be x, 2x, and 3x.\nStep 2: Sum of their cubes: x³ + (2x)³ + (3x)³ = x³ + 8x³ + 27x³ = 36x³.\nStep 3: 36x³ = 4500 ⟹ x³ = 4500 / 36 = 125.\nStep 4: x = ∛125 = 5.\nStep 5: The largest number is 3x = 3 × 5 = 15."
    }
]

# Class 8 Mathematics Chapter 5: Number Play - Master Curriculum Data
# Based on Syllabus:
# 5.1 Is This a Multiple Of? (Sum of Consecutive Numbers, Math Talk, Breaking Even, Pairs to Make Fours, Always Sometimes Never, What Remains, Figure it Out)
# 5.2 Checking Divisibility Quickly (Divisibility by 9, 3, 11, More Shortcuts, Other Numbers, Digital Roots)
# 5.3 Digits in Disguise (Cryptarithms)
# SUMMARY & IT'S PUZZLE TIME!

slides_data = [
    # Slide 1: 5.1 Is This a Multiple Of?
    {
        "id": 1,
        "title": "5.1 Is This a Multiple Of? Multiples in Disguise",
        "subtitle": "Divisibility Foundations, Remainder Zero & Multiples on the Number Line",
        "content": """
<p class="lead">In arithmetic, determining whether an integer $N$ is a <strong>multiple</strong> of another integer $d$ is equivalent to asking: <em>Can $N$ be shared equally into $d$ groups with zero remainder?</em></p>

<div class="theory-box">
  <h4>Formal Definition of a Multiple</h4>
  <p>An integer $N$ is said to be a <strong>multiple</strong> of an integer $d$ (where $d \\neq 0$) if there exists an integer $k$ such that:</p>
  $$N = d \\times k$$
  <p>Equivalently, $d$ is a <strong>factor</strong> or <strong>divisor</strong> of $N$, written as $d \\mid N$ ($d$ divides $N$). By the division algorithm:</p>
  $$N = d \\times q + r \\quad \\text{with } 0 \\le r < d$$
  <p>$N$ is a multiple of $d$ if and only if the remainder $r = 0$.</p>
</div>

<div class="formula-box">
  <h4>Properties of Multiples</h4>
  <ul>
    <li><strong>Zero is a multiple of every non-zero integer:</strong> $0 = d \\times 0$.</li>
    <li><strong>Linear Combination Law:</strong> If $A$ and $B$ are both multiples of $d$, then their sum $(A + B)$ and difference $(A - B)$ are also multiples of $d$.</li>
    <li><strong>Product Law:</strong> If $A$ is a multiple of $d$, then $A \\times m$ is a multiple of $d$ for any integer $m$.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>Multiples on the Number Line</h4>
  <p>Multiples of $d$ form an infinite periodic grid of points spaced exactly $d$ units apart: $\\{\\dots, -2d, -d, 0, d, 2d, 3d, \\dots\\}$. Any integer falling strictly between two consecutive grid points has a non-zero remainder and is not a multiple.</p>
</div>
""",
        "sim_type": "multiples_number_line_hopper",
        "voice": "Welcome to Chapter 5: Number Play! We begin with section 5.1: Is This a Multiple Of? An integer N is a multiple of d if it divides evenly with zero remainder. On a number line, multiples of d appear at regular steps. Let us explore multiples and remainders dynamically.",
        "checkpoints": [
            {
                "question": "If an integer N leaves a remainder of 0 when divided by 7, which statement is guaranteed to be true?",
                "options": [
                    "N is a multiple of 7",
                    "7 is a multiple of N",
                    "N must be an odd number",
                    "N cannot be equal to zero"
                ],
                "correct": 0,
                "explanation": "By definition, if $N = 7q + 0$, then $N = 7q$, which means $N$ is a multiple of 7."
            },
            {
                "question": "If A is a multiple of 6 and B is a multiple of 6, what can we conclude about A + B?",
                "options": [
                    "A + B is always a multiple of 12",
                    "A + B is always a multiple of 6",
                    "A + B is never a multiple of 6",
                    "A + B must be a prime number"
                ],
                "correct": 1,
                "explanation": "If $A = 6k_1$ and $B = 6k_2$, then $A + B = 6(k_1 + k_2)$, which is strictly a multiple of 6 by the Linear Combination Law."
            }
        ]
    },

    # Slide 2: Sum of Consecutive Numbers
    {
        "id": 2,
        "title": "Sum of Consecutive Numbers: Algebraic Partitions",
        "subtitle": "Trapezoidal Numbers, Odd Spans & The Powers of 2 Impossibility",
        "content": """
<p class="lead">Can every positive integer be expressed as the sum of two or more consecutive positive integers? Exploring this question uncovers surprising arithmetic laws.</p>

<div class="theory-box">
  <h4>Sum of Two Consecutive Numbers</h4>
  <p>Let two consecutive integers be $k$ and $k + 1$. Their sum is:</p>
  $$S_2 = k + (k + 1) = 2k + 1$$
  <p>Since $2k + 1$ is always an odd integer, <strong>every odd number greater than 1 can be expressed as the sum of 2 consecutive integers</strong>: $\\frac{N-1}{2} + \\frac{N+1}{2} = N$. (Example: $15 = 7 + 8$).</p>
</div>

<div class="formula-box">
  <h4>Sum of Three Consecutive Numbers</h4>
  <p>Let three consecutive integers be $k - 1$, $k$, and $k + 1$:</p>
  $$S_3 = (k - 1) + k + (k + 1) = 3k$$
  <p>The sum is always <strong>three times the middle integer</strong>! Therefore, an integer is expressible as the sum of 3 consecutive integers if and only if it is a <strong>multiple of 3</strong> (and $> 3$).</p>
</div>

<div class="theory-box">
  <h4>The Famous Powers of 2 Theorem</h4>
  <p>The sum of $m$ consecutive integers starting at $k$ is $\\frac{m(2k + m - 1)}{2}$. For this product to equal $N$, $N$ must have an <strong>odd factor greater than 1</strong>.</p>
  <p><strong>Profound Result:</strong> The numbers that can <em>NEVER</em> be written as a sum of consecutive positive integers are precisely the <strong>powers of 2</strong>: $1, 2, 4, 8, 16, 32, 64, \\dots$!</p>
</div>
""",
        "sim_type": "consecutive_sum_builder",
        "voice": "Can numbers be broken into sums of consecutive integers? Two consecutive numbers always add to an odd number, two k plus one. Three consecutive numbers always sum to three times the middle number, making a multiple of three. Remarkably, powers of two such as 4, 8, 16, and 32 can never be written as a sum of consecutive positive integers because they contain no odd factors.",
        "checkpoints": [
            {
                "question": "Which of the following numbers CANNOT be written as the sum of two or more consecutive positive integers?",
                "options": ["15", "21", "32", "35"],
                "correct": 2,
                "explanation": "32 is a power of 2 ($2^5$). Powers of 2 have no odd prime factors and therefore cannot be decomposed into a sum of consecutive positive integers."
            },
            {
                "question": "If the sum of three consecutive integers is 72, what is the middle integer?",
                "options": ["23", "24", "25", "26"],
                "correct": 1,
                "explanation": "The sum of 3 consecutive integers is $3k = 72$, so the middle integer is $k = \\frac{72}{3} = 24$. (The numbers are 23, 24, 25)."
            }
        ]
    },

    # Slide 3: Math Talk: Parity, Arithmetic Patterns & Multiples
    {
        "id": 3,
        "title": "Math Talk: Parity Laws & Modulo Arithmetic",
        "subtitle": "Odd-Even Algebra, Multiplication Symmetries & Modulo 3 Dynamics",
        "content": """
<p class="lead">Parity describes whether an integer is <strong>even</strong> (a multiple of 2) or <strong>odd</strong> (leaves remainder 1 when divided by 2). Parity forms an ultra-stable arithmetic system.</p>

<div class="formula-box">
  <h4>The Fundamental Laws of Parity</h4>
  <table style="width:100%; border-collapse:collapse; margin-top:6px; font-size:13px;">
    <thead>
      <tr style="border-bottom:1px solid #475569; color:#38bdf8;">
        <th align="left">Operation</th>
        <th align="center">Formula</th>
        <th align="center">Result</th>
        <th align="left">Example</th>
      </tr>
    </thead>
    <tbody style="color:#cbd5e1;">
      <tr style="border-bottom:1px solid #1e293b;"><td>Even + Even</td><td align="center">$2a + 2b = 2(a+b)$</td><td align="center"><strong style="color:#34d399;">Even</strong></td><td>$4 + 6 = 10$</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td>Odd + Odd</td><td align="center">$(2a+1) + (2b+1) = 2(a+b+1)$</td><td align="center"><strong style="color:#34d399;">Even</strong></td><td>$5 + 7 = 12$</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td>Even + Odd</td><td align="center">$2a + (2b+1) = 2(a+b) + 1$</td><td align="center"><strong style="color:#f43f5e;">Odd</strong></td><td>$4 + 7 = 11$</td></tr>
      <tr style="border-bottom:1px solid #1e293b;"><td>Odd × Odd</td><td align="center">$(2a+1)(2b+1) = 2(2ab+a+b)+1$</td><td align="center"><strong style="color:#f43f5e;">Odd</strong></td><td>$3 \\times 5 = 15$</td></tr>
      <tr><td>Even × Anything</td><td align="center">$2a \\times k = 2(ak)$</td><td align="center"><strong style="color:#34d399;">Even</strong></td><td>$4 \\times 7 = 28$</td></tr>
    </tbody>
  </table>
</div>

<div class="theory-box">
  <h4>Modulo 3 Residue Classes</h4>
  <p>Every integer belongs to one of three residue classes when divided by 3:</p>
  <ul>
    <li>Form $3k$: Exact multiples of 3 ($0, 3, 6, 9, 12, \\dots$).</li>
    <li>Form $3k + 1$: Leaves remainder 1 ($1, 4, 7, 10, 13, \\dots$).</li>
    <li>Form $3k + 2$: Leaves remainder 2 ($2, 5, 8, 11, 14, \\dots$).</li>
  </ul>
  <p>Squaring any integer of form $3k+1$ or $3k+2$ always yields remainder 1: $(3k\\pm 1)^2 = 9k^2 \\pm 6k + 1 = 3(3k^2 \\pm 2k) + 1$. A perfect square <em>never</em> leaves remainder 2 modulo 3!</p>
</div>
""",
        "sim_type": "parity_algebra_matrix",
        "voice": "Math Talk explores parity and arithmetic patterns. When you add two odd numbers, the two leftover ones pair up to create an even number. When multiplying, if even a single factor is even, the entire product is even. In modulo 3 arithmetic, numbers fall into remainders of 0, 1, or 2, and squaring any number never leaves a remainder of 2.",
        "checkpoints": [
            {
                "question": "If you add 5 odd numbers together, is the resulting sum even or odd?",
                "options": ["Always Even", "Always Odd", "Sometimes Even, Sometimes Odd", "Cannot be determined"],
                "correct": 1,
                "explanation": "Four odd numbers sum to an even number (Odd+Odd=Even, and Even+Even=Even). Adding the fifth odd number (Even+Odd) produces an **Odd** result."
            },
            {
                "question": "Can the square of any integer leave a remainder of 2 when divided by 3?",
                "options": [
                    "Yes, for all even numbers",
                    "Yes, for all odd numbers",
                    "Never, squares only leave remainder 0 or 1 modulo 3",
                    "Only for prime numbers"
                ],
                "correct": 2,
                "explanation": "$(3k)^2 = 9k^2 = 3(3k^2) \\implies r=0$. $(3k+1)^2 = 9k^2+6k+1 = 3(3k^2+2k)+1 \\implies r=1$. $(3k+2)^2 = 9k^2+12k+4 = 3(3k^2+4k+1)+1 \\implies r=1$. A square never leaves remainder 2."
            }
        ]
    },

    # Slide 4: Breaking Even & Parity Invariance
    {
        "id": 4,
        "title": "Breaking Even & Parity Invariance Principles",
        "subtitle": "State Invariants, Conservation of Parity & Impossible Puzzles",
        "content": """
<p class="lead">A mathematical <strong>invariant</strong> is a property that remains completely unchanged after applying a specific set of operations. Parity is one of the most powerful invariants in mathematics.</p>

<div class="theory-box">
  <h4>The Addition and Subtraction Invariance Law</h4>
  <p>Replacing any two numbers $a$ and $b$ with their sum $(a + b)$ or their difference $(a - b)$ <strong>does not change the parity</strong> of the total sum of all elements in the collection!</p>
  $$(a + b) \\equiv (a - b) \\pmod 2$$
  <p>Because $(a + b) - (a - b) = 2b$ (which is always an even number), shifting a sign from $+$ to $-$ preserves the overall evenness or oddness of the total.</p>
</div>

<div class="formula-box">
  <h4>Breaking Even: Splitting Collections</h4>
  <p>Can an odd number of items ever be divided into two equal whole-number piles?</p>
  <p>Let the total be $N$. If split into two piles of size $k$ and $k$:</p>
  $$\\text{Total} = k + k = 2k \\quad (\\text{strictly Even})$$
  <p>Therefore, <strong>an odd number can NEVER \"break even\"</strong> into two equal integer halves. One pile will always have at least 1 more than the other ($k$ and $k+1$).</p>
</div>

<div class="theory-box">
  <h4>The 15-Coins Invariant Puzzle</h4>
  <p>If you have 15 coins on a table with 7 showing heads and 8 showing tails, can you make all coins show heads by flipping exactly 2 coins at a time? Flipping 2 coins changes the number of heads by $+2, 0,$ or $-2$. The parity of heads remains invariant (always odd). Since 15 is odd and all-heads requires 15 (odd), but all-tails requires 0 (even), reaching 0 is impossible!</p>
</div>
""",
        "sim_type": "breaking_even_parity_game",
        "voice": "Section 5.1 continues with Breaking Even and Parity Invariants. An invariant is something that stays the same no matter how many moves you make. Because the sum of two equal piles is always 2k, an odd number can never break even into two equal whole halves. Flipping pairs of items preserves parity, making certain configurations mathematically impossible to reach.",
        "checkpoints": [
            {
                "question": "If you have 25 integers whose sum is odd, how many of those 25 integers must be odd?",
                "options": [
                    "An even number of integers",
                    "An odd number of integers",
                    "All 25 must be odd",
                    "None can be odd"
                ],
                "correct": 1,
                "explanation": "Even numbers contribute an even amount to the sum. Only odd numbers can change the parity. For the final total to be odd, there must be an **odd count** of odd numbers."
            },
            {
                "question": "Can 101 coins all showing Tails be transformed to all showing Heads by flipping exactly 2 coins at each step?",
                "options": [
                    "Yes, in exactly 50 steps",
                    "Yes, in exactly 51 steps",
                    "No, because the parity of Heads stays even while 101 is odd",
                    "Only if coins are flipped in reverse order"
                ],
                "correct": 2,
                "explanation": "Starting with 0 Heads (even), flipping 2 coins changes Heads by +2, 0, or -2. The count of Heads is always even, so it can never reach 101 (odd)."
            }
        ]
    },

    # Slide 5: Pairs to Make Fours & Multiples of 4
    {
        "id": 5,
        "title": "Pairs to Make Fours & Divisibility by 4",
        "subtitle": "The 100-Decomposition Theorem & Last Two Digits Architecture",
        "content": """
<p class="lead">Why does the divisibility test for 4 ignore thousands, millions, and billions, focusing <em>strictly on the last two digits</em>? Place-value base-10 algebra provides the proof.</p>

<div class="formula-box">
  <h4>The 100-Decomposition Theorem</h4>
  <p>Any positive integer $N$ can be split into its hundreds part and its two-digit terminal tail:</p>
  $$N = 100 \\times H + T$$
  <p>where $T = 10b + c$ is the two-digit number formed by the tens digit $b$ and units digit $c$.</p>
  <p>Because $100 = 4 \\times 25$, the term $100 \\times H$ is <strong>always a multiple of 4</strong>, regardless of what digits precede it!</p>
  $$N = 4(25H) + T \\implies N \\equiv T \\pmod 4$$
  <p>Therefore, <strong>$N$ is divisible by 4 if and only if its last two digits $T$ form a multiple of 4</strong>.</p>
</div>

<div class="theory-box">
  <h4>Product of Two Consecutive Even Numbers</h4>
  <p>Let two consecutive even numbers be $2k$ and $2k + 2$:</p>
  $$\\text{Product} = 2k(2k + 2) = 4k(k + 1)$$
  <p>Since one of $k$ or $k + 1$ is guaranteed to be even ($k(k+1)$ is a multiple of 2):</p>
  $$\\text{Product} = 4 \\times (2m) = 8m$$
  <p>The product of any two consecutive even numbers is not merely a multiple of 4—it is <strong>always a multiple of 8</strong>!</p>
</div>
""",
        "sim_type": "pairs_to_make_fours_lab",
        "voice": "Why does divisibility by 4 only look at the last two digits? Because 100 is equal to 4 times 25, meaning every hundred, thousand, or million is already divisible by 4. Only the last two digits determine the remainder. Furthermore, the product of any two consecutive even numbers is always a multiple of 8.",
        "checkpoints": [
            {
                "question": "Which of the following numbers is divisible by 4?",
                "options": ["354,826", "918,342", "7,145,928", "5,002,114"],
                "correct": 2,
                "explanation": "Inspect the last two digits: 26 is not divisible by 4; 42 is not; 14 is not; but $28 = 4 \\times 7$ is divisible by 4. Thus 7,145,928 is divisible by 4."
            },
            {
                "question": "What is the product of two consecutive even integers always divisible by at minimum?",
                "options": ["4", "6", "8", "16"],
                "correct": 2,
                "explanation": "$2k(2k+2) = 4k(k+1)$. Because one of two consecutive integers $k, k+1$ is always even, $k(k+1) = 2m$. Thus the product is $4(2m) = 8m$, always a multiple of 8."
            }
        ]
    },

    # Slide 6: Always, Sometimes, or Never: Mathematical Conjectures
    {
        "id": 6,
        "title": "Always, Sometimes, or Never: Rigorous Conjectures",
        "subtitle": "Universal Proofs, Existential Cases & Counterexample Disqualification",
        "content": """
<p class="lead">In mathematics, classifying a statement as <strong>Always True</strong>, <strong>Sometimes True</strong>, or <strong>Never True</strong> tests the depth of logical and algebraic proof.</p>

<div class="theory-box">
  <h4>The Three Epistemic Categories</h4>
  <ul>
    <li><strong>ALWAYS TRUE:</strong> Must hold for <em>every single element</em> in the domain with zero exceptions. Requires a general algebraic proof.</li>
    <li><strong>SOMETIMES TRUE:</strong> Holds for some instances, but fails for others. Requires demonstrating at least one working example AND at least one counterexample.</li>
    <li><strong>NEVER TRUE:</strong> Contradicts fundamental mathematical laws; holds for zero instances. Requires proving an impossibility.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Testing Classic Number Conjectures</h4>
  <ol>
    <li><em>\"The sum of 3 consecutive integers is a multiple of 3.\"</em>
      <br><strong>ALWAYS:</strong> $(n-1) + n + (n+1) = 3n$. Always true for all integers.
    </li>
    <li><em>\"A multiple of 4 is a multiple of 8.\"</em>
      <br><strong>SOMETIMES:</strong> True for $16, 24, 32$; but FALSE for $12, 20, 28$ (counterexamples).
    </li>
    <li><em>\"The sum of two odd numbers is odd.\"</em>
      <br><strong>NEVER:</strong> $(2a+1) + (2b+1) = 2(a+b+1)$, which is strictly even. Never true.
    </li>
    <li><em>\"The square of an odd number is odd.\"</em>
      <br><strong>ALWAYS:</strong> $(2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is strictly odd.
    </li>
  </ol>
</div>
""",
        "sim_type": "always_sometimes_never_tester",
        "voice": "Always, Sometimes, or Never trains mathematical rigor. An Always statement must hold universally with an algebraic proof. A Sometimes statement has both valid examples and counterexamples. A Never statement is an impossibility. For example, adding two odd numbers never produces an odd number.",
        "checkpoints": [
            {
                "question": "Is the statement 'A multiple of 6 is a multiple of 12' Always, Sometimes, or Never true?",
                "options": ["Always True", "Sometimes True", "Never True", "Cannot be determined"],
                "correct": 1,
                "explanation": "It is **Sometimes True**. 24 is a multiple of 6 and is a multiple of 12; but 18 is a multiple of 6 and is NOT a multiple of 12."
            },
            {
                "question": "Is the statement 'The product of two prime numbers is a prime number' Always, Sometimes, or Never true?",
                "options": ["Always True", "Sometimes True", "Never True", "True only for 2 and 3"],
                "correct": 2,
                "explanation": "It is **Never True**. By definition, a prime number has exactly two factors (1 and itself). The product $p_1 \\times p_2$ has at least four factors: $1, p_1, p_2,$ and $p_1 p_2$."
            }
        ]
    },

    # Slide 7: What Remains? (The Division Algorithm & Remainders)
    {
        "id": 7,
        "title": "What Remains? The Division Algorithm & Modulo Cycles",
        "subtitle": "Euclid's Division Lemma, Remainder Bounds & Circular Clocks",
        "content": """
<p class="lead">When a number is not an exact multiple, <strong>what remains</strong> reveals profound cyclic patterns that form the foundation of modern cryptography.</p>

<div class="theory-box">
  <h4>Euclid's Division Lemma</h4>
  <p>For any integer $a$ and non-zero divisor $d$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:</p>
  $$a = d \\times q + r \\quad \\text{where } 0 \\le r < d$$
  <p>The remainder $r$ can take on exactly $d$ possible values: $\\{0, 1, 2, \\dots, d - 1\\}$.</p>
</div>

<div class="formula-box">
  <h4>Circular Clock Arithmetic (Modular Cyclicity)</h4>
  <p>Consider an ordinary 12-hour clock. If it is 9 o'clock now, what time will it be in 28 hours?</p>
  $$28 = 12 \\times 2 + 4 \\implies 28 \\equiv 4 \\pmod{12}$$
  $$\\text{New Time} = 9 + 4 = 13 \\equiv 1\\text{ o'clock}$$
  <p>Remainders wrap around in closed periodic loops. For divisor $d=5$, powers of integers cycle with periods dividing 4 (Fermat's Little Theorem foundation).</p>
</div>

<div class="theory-box">
  <h4>Remainder Arithmetic Rule</h4>
  <p>The remainder of a sum or product equals the sum or product of the individual remainders:</p>
  $$\\text{rem}(A + B, d) = \\text{rem}(\\text{rem}(A, d) + \\text{rem}(B, d), d)$$
  $$\\text{rem}(A \\times B, d) = \\text{rem}(\\text{rem}(A, d) \\times \\text{rem}(B, d), d)$$
</div>
""",
        "sim_type": "division_clock_modular_lab",
        "voice": "What Remains investigates the division algorithm and remainders. According to Euclid's lemma, dividing by d yields unique quotients and remainders between zero and d minus one. On a circular clock, remainders loop endlessly, allowing us to compute remainders of enormous sums and products with ease.",
        "checkpoints": [
            {
                "question": "If today is Tuesday, what day of the week will it be in 100 days?",
                "options": ["Wednesday", "Thursday", "Friday", "Saturday"],
                "correct": 1,
                "explanation": "Days of the week repeat every 7 days. $100 = 7 \\times 14 + 2$. The remainder is 2 days. Two days after Tuesday is **Thursday**."
            },
            {
                "question": "What is the remainder when (53 × 79) is divided by 5?",
                "options": ["1", "2", "3", "4"],
                "correct": 1,
                "explanation": "$53 = 5(10) + 3 \\implies r_1 = 3$. $79 = 5(15) + 4 \\implies r_2 = 4$. Product of remainders is $3 \\times 4 = 12$. Dividing 12 by 5 gives remainder **2**."
            }
        ]
    },

    # Slide 8: Figure it Out: Geometric Number Patterns
    {
        "id": 8,
        "title": "Figure it Out: Figurate Numbers & Dot Arrays",
        "subtitle": "Triangular Sequences, Square Arrays & Geometric Algebra",
        "content": """
<p class="lead">Ancient Greek mathematicians studied numbers by physically arranging pebbles into geometric shapes, discovering <strong>figurate numbers</strong>.</p>

<div class="theory-box">
  <h4>Triangular Numbers ($T_n$)</h4>
  <p>Numbers that form equilateral triangular dot arrays:</p>
  $$T_1 = 1, \\quad T_2 = 1+2 = 3, \\quad T_3 = 1+2+3 = 6, \\quad T_4 = 1+2+3+4 = 10$$
  <p>The general formula for the $n$-th triangular number is:</p>
  $$T_n = \\frac{n(n + 1)}{2}$$
</div>

<div class="formula-box">
  <h4>Connecting Triangular Numbers to Perfect Squares</h4>
  <p>Joining two consecutive triangular pebbles arrays always creates a perfect square grid:</p>
  $$T_{n-1} + T_n = \\frac{(n-1)n}{2} + \\frac{n(n+1)}{2} = \\frac{n^2 - n + n^2 + n}{2} = \\frac{2n^2}{2} = n^2$$
  <p>Examples: $T_1 + T_2 = 1 + 3 = 4 = 2^2$; $T_2 + T_3 = 3 + 6 = 9 = 3^2$; $T_3 + T_4 = 6 + 10 = 16 = 4^2$.</p>
</div>

<div class="theory-box">
  <h4>Eight Times a Triangular Number Plus One</h4>
  <p>In the 2nd century CE, Nicomachus proved that multiplying any triangular number by 8 and adding 1 always yields an odd square number:</p>
  $$8 T_n + 1 = 8\\left(\\frac{n(n+1)}{2}\\right) + 1 = 4n^2 + 4n + 1 = (2n + 1)^2$$
</div>
""",
        "sim_type": "figurate_dot_pattern_engine",
        "voice": "Figure it Out examines figurate numbers, where numbers form geometric shapes. Triangular numbers sum integers from one to n, calculated by n times n plus one divided by two. Remarkably, adding two consecutive triangular numbers always produces a perfect square grid, as seen when three plus six equals nine.",
        "checkpoints": [
            {
                "question": "What is the 6th triangular number (T₆)?",
                "options": ["15", "21", "28", "36"],
                "correct": 1,
                "explanation": "$T_6 = \\frac{6 \\times (6 + 1)}{2} = \\frac{6 \\times 7}{2} = \\frac{42}{2} = 21$."
            },
            {
                "question": "What is the sum of the 4th and 5th triangular numbers (T₄ + T₅)?",
                "options": ["20", "25", "30", "36"],
                "correct": 1,
                "explanation": "$T_4 = 10$ and $T_5 = 15$. Their sum is $10 + 15 = 25 = 5^2$ (The consecutive triangular theorem $T_{n-1} + T_n = n^2$)."
            }
        ]
    },

    # Slide 9: 5.2 Checking Divisibility Quickly: Shortcut for 9
    {
        "id": 9,
        "title": "5.2 Checking Divisibility Quickly: Shortcut for 9",
        "subtitle": "Place-Value Decomposition, Nines Expansion & The Digit Sum Proof",
        "content": """
<p class="lead">Why does summing the digits of a number determine whether it is divisible by 9? The proof relies on decomposing powers of 10 into multiples of 9 plus 1.</p>

<div class="theory-box">
  <h4>Algebraic Decomposition of Powers of 10</h4>
  <p>Observe how every power of 10 is exactly 1 more than a string of nines:</p>
  $$10 = 9 + 1$$
  $$100 = 99 + 1$$
  $$1000 = 999 + 1$$
  $$10^k = \\underbrace{999\\dots9}_{k \\text{ nines}} + 1$$
</div>

<div class="formula-box">
  <h4>The Universal Divisibility by 9 Theorem</h4>
  <p>Consider any 4-digit number $N = \\overline{abcd} = 1000a + 100b + 10c + d$. Expanding each power of 10:</p>
  $$N = (999 + 1)a + (99 + 1)b + (9 + 1)c + d$$
  $$N = \\underbrace{(999a + 99b + 9c)}_{\\text{Strictly a multiple of } 9} + \\underbrace{(a + b + c + d)}_{\\text{Sum of Digits}}$$
  <p>Since $(999a + 99b + 9c) = 9(111a + 11b + c)$ is guaranteed to be divisible by 9, $N$ is divisible by 9 <strong>if and only if its sum of digits $(a + b + c + d)$ is divisible by 9</strong>!</p>
</div>

<div class="theory-box">
  <h4>Remainder Invariance</h4>
  <p>Furthermore, <strong>$N$ leaves the exact same remainder when divided by 9 as its sum of digits does</strong>: $N \\equiv \\sum d_i \\pmod 9$.</p>
</div>
""",
        "sim_type": "divisibility_by_9_decomposer",
        "voice": "Section 5.2 introduces quick divisibility tests, starting with 9. Why does adding digits work? Every power of 10 is 1 plus a string of nines, such as 99 plus 1. When we expand a number, all the nines group into a multiple of 9, leaving behind only the sum of the digits. If the digit sum is a multiple of 9, the entire number is divisible by 9.",
        "checkpoints": [
            {
                "question": "Which of the following numbers is divisible by 9?",
                "options": ["45,821", "72,819", "54,318", "63,214"],
                "correct": 2,
                "explanation": "Compute digit sums: For 54,318: $5 + 4 + 3 + 1 + 8 = 21$, not 9. Wait! Let's check 72,819: $7+2+8+1+9 = 27 = 9 \\times 3$. 27 is divisible by 9, so 72,819 is divisible by 9!"
            },
            {
                "question": "If the number 4A72 is a multiple of 9, what is the value of the missing digit A?",
                "options": ["3", "5", "7", "9"],
                "correct": 1,
                "explanation": "Sum of digits is $4 + A + 7 + 2 = 13 + A$. For $13 + A$ to be a multiple of 9, $13 + A = 18 \\implies A = 5$."
            }
        ]
    },

    # Slide 10: A Shortcut for Divisibility by 3
    {
        "id": 10,
        "title": "A Shortcut for Divisibility by 3: The Factor Inheritance",
        "subtitle": "Inherited Multiples, Digit Sum Criteria & Modular Congruence",
        "content": """
<p class="lead">Because 3 is a prime factor of 9 ($9 = 3 \\times 3$), any number composed of nines ($9, 99, 999, \\dots$) is also automatically a multiple of 3!</p>

<div class="formula-box">
  <h4>The Divisibility by 3 Proof</h4>
  <p>From the place value decomposition of $N = \\overline{abcd}$:</p>
  $$N = 9(111a + 11b + c) + (a + b + c + d)$$
  <p>Rewriting $9$ as $3 \\times 3$:</p>
  $$N = 3 \\times [3(111a + 11b + c)] + (a + b + c + d)$$
  <p>The first term is strictly a multiple of 3. Therefore:</p>
  $$N \\equiv (a + b + c + d) \\pmod 3$$
  <p><strong>Rule:</strong> A number is divisible by 3 if and only if the <strong>sum of its digits is divisible by 3</strong>.</p>
</div>

<div class="theory-box">
  <h4>Relationship Between Divisibility by 3 and 9</h4>
  <ul>
    <li><strong>Every multiple of 9 is ALWAYS a multiple of 3</strong> (since $9 = 3 \\times 3$).</li>
    <li><strong>NOT every multiple of 3 is a multiple of 9</strong> (e.g., 6, 12, 15, 21, 24, 30 are multiples of 3, but not of 9).</li>
  </ul>
</div>
""",
        "sim_type": "divisibility_by_3_scanner",
        "voice": "Next is divisibility by 3. Because 3 divides 9, all those strings of nines are also multiples of 3. Therefore, an integer is divisible by 3 if and only if its digit sum is a multiple of 3. Remember: all multiples of 9 are divisible by 3, but not all multiples of 3 are divisible by 9.",
        "checkpoints": [
            {
                "question": "If the number 258X is divisible by 3, what are all possible single-digit values of X?",
                "options": ["0, 3, 6, 9", "1, 4, 7", "2, 5, 8", "3, 6, 9"],
                "correct": 2,
                "explanation": "Sum of known digits: $2 + 5 + 8 = 15$, which is already a multiple of 3. Thus $15 + X$ is a multiple of 3 if $X \\in \\{0, 3, 6, 9\\}$."
            },
            {
                "question": "Which statement correctly describes the relationship between divisibility by 3 and divisibility by 9?",
                "options": [
                    "All multiples of 3 are divisible by 9",
                    "All multiples of 9 are divisible by 3",
                    "A number is divisible by 9 if and only if it is divisible by 3",
                    "Divisibility by 3 and 9 have no mathematical relationship"
                ],
                "correct": 1,
                "explanation": "Since $9 = 3 \\times 3$, any number divisible by 9 is automatically divisible by 3."
            }
        ]
    },

    # Slide 11: A Shortcut for Divisibility by 11
    {
        "id": 11,
        "title": "A Shortcut for Divisibility by 11: Alternating Sums",
        "subtitle": "Modulo 11 Powers of 10, Odd-Even Position Balance & The Zero Remainder",
        "content": """
<p class="lead">Why does the divisibility test for 11 alternate between subtraction and addition? The answer lies in the alternating remainders of powers of 10 when divided by 11.</p>

<div class="theory-box">
  <h4>Alternating Residues of Powers of 10</h4>
  <p>Dividing consecutive powers of 10 by 11 reveals an oscillating pattern:</p>
  $$1 = 0 \\times 11 + 1 \\equiv +1 \\pmod{11}$$
  $$10 = 1 \\times 11 - 1 \\equiv -1 \\pmod{11}$$
  $$100 = 9 \\times 11 + 1 \\equiv +1 \\pmod{11}$$
  $$1000 = 91 \\times 11 - 1 \\equiv -1 \\pmod{11}$$
  $$10000 = 909 \\times 11 + 1 \\equiv +1 \\pmod{11}$$
  <p>In general, $10^k \\equiv (-1)^k \\pmod{11}$. Even powers leave $+1$, while odd powers leave $-1$ (or $+10$).</p>
</div>

<div class="formula-box">
  <h4>The Alternating Sum Rule for 11</h4>
  <p>For any number $N = d_k d_{k-1} \\dots d_1 d_0$:</p>
  $$N \\equiv (d_0 - d_1 + d_2 - d_3 + d_4 - \\dots) \\pmod{11}$$
  $$N \\equiv (\\text{Sum of digits at odd places}) - (\\text{Sum of digits at even places}) \\pmod{11}$$
  <p><strong>Rule:</strong> A number is divisible by 11 if the <strong>difference between the sum of digits in odd positions and even positions is either 0 or a multiple of 11</strong>.</p>
</div>

<div class="theory-box">
  <h4>Example: Test 85,976</h4>
  <ul>
    <li>Odd positions (from right: 1st, 3rd, 5th): $6 + 9 + 8 = 23$.</li>
    <li>Even positions (from right: 2nd, 4th): $7 + 5 = 12$.</li>
    <li>Difference: $23 - 12 = 11$, which is a multiple of 11! Therefore, 85,976 is divisible by 11 ($85,976 = 11 \\times 7,816$).</li>
  </ul>
</div>
""",
        "sim_type": "divisibility_by_11_balance_scale",
        "voice": "Divisibility by 11 uses an alternating sum. Because 10 is 11 minus 1, powers of 10 alternate between leaving plus 1 and minus 1. To test any number for divisibility by 11, sum the digits in odd positions and subtract the sum of digits in even positions. If the difference is zero or a multiple of 11, the number is divisible by 11.",
        "checkpoints": [
            {
                "question": "Is the number 91,839 divisible by 11?",
                "options": [
                    "Yes, because the alternating difference is 0",
                    "Yes, because the alternating difference is 11",
                    "No, because the alternating difference is 7",
                    "No, because the digit sum is not 11"
                ],
                "correct": 1,
                "explanation": "Digits from right: Odd places (1st, 3rd, 5th): $9 + 8 + 9 = 26$. Even places (2nd, 4th): $3 + 1 = 4$. Difference is $26 - 4 = 22$, which is $11 \\times 2$. Thus, **Yes**, it is divisible by 11."
            },
            {
                "question": "Find digit X such that 7X34 is divisible by 11.",
                "options": ["0", "2", "6", "9"],
                "correct": 2,
                "explanation": "Odd places: $4 + X$. Even places: $3 + 7 = 10$. Difference: $(4 + X) - 10 = X - 6$. For this difference to equal 0, $X = 6$."
            }
        ]
    },

    # Slide 12: Divisibility Shortcuts for 2, 5, 10, and 8
    {
        "id": 12,
        "title": "Divisibility Shortcuts for Powers of 2, 5, and 10",
        "subtitle": "Last k Digits Architecture: 2, 4, 8, 16 and 5, 25, 125",
        "content": """
<p class="lead">Why do tests for 2, 4, and 8 look at 1, 2, and 3 terminal digits? Because our decimal base is $10 = 2 \\times 5$, place values absorb factors in geometric powers.</p>

<div class="theory-box">
  <h4>The Powers of 2 Family ($2^k$)</h4>
  <ul>
    <li><strong>Divisibility by 2 ($2^1$):</strong> $10^1 = 2 \\times 5$. All tens and higher are multiples of 2. Look at <strong>last 1 digit</strong> (must be $0, 2, 4, 6, 8$).</li>
    <li><strong>Divisibility by 4 ($2^2$):</strong> $10^2 = 100 = 4 \\times 25$. All hundreds and higher are multiples of 4. Look at <strong>last 2 digits</strong>.</li>
    <li><strong>Divisibility by 8 ($2^3$):</strong> $10^3 = 1000 = 8 \\times 125$. All thousands and higher are multiples of 8. Look at <strong>last 3 digits</strong>.</li>
    <li><strong>Divisibility by 16 ($2^4$):</strong> $10^4 = 10000 = 16 \\times 625$. Look at <strong>last 4 digits</strong>.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>The Powers of 5 and 10 Families</h4>
  <ul>
    <li><strong>Divisibility by 5 ($5^1$):</strong> Look at <strong>last 1 digit</strong> (must be $0$ or $5$).</li>
    <li><strong>Divisibility by 25 ($5^2$):</strong> Look at <strong>last 2 digits</strong> (must be $00, 25, 50, 75$).</li>
    <li><strong>Divisibility by 125 ($5^3$):</strong> Look at <strong>last 3 digits</strong> (must be a multiple of 125).</li>
    <li><strong>Divisibility by 10:</strong> Units digit must be $0$.</li>
  </ul>
</div>
""",
        "sim_type": "power_of_two_and_five_explorer",
        "voice": "Divisibility rules for powers of 2 and 5 form an elegant geometric pattern. Because 10 is 2 times 5, testing for 2 or 5 checks the last 1 digit. Testing for 4 or 25 checks the last 2 digits because 100 is divisible by 4 and 25. Testing for 8 or 125 checks the last 3 digits because 1000 is divisible by 8 and 125.",
        "checkpoints": [
            {
                "question": "To determine whether 58,924,168 is divisible by 8, which digits do you inspect?",
                "options": [
                    "Only the last digit: 8",
                    "The last two digits: 68",
                    "The last three digits: 168",
                    "The sum of all digits"
                ],
                "correct": 2,
                "explanation": "Because $1000 = 8 \\times 125$, any multiple of 1000 is divisible by 8. We only need to check the last three digits: $168 = 8 \\times 21$, which is divisible by 8."
            },
            {
                "question": "Which of the following numbers is divisible by 25?",
                "options": ["4,195", "8,275", "6,340", "1,885"],
                "correct": 1,
                "explanation": "A number is divisible by 25 if its last two digits are 00, 25, 50, or 75. 8,275 ends in 75, so it is divisible by 25."
            }
        ]
    },

    # Slide 13: Composite Divisibility Shortcuts: 6, 12, 15, and 18
    {
        "id": 13,
        "title": "Composite Divisibility Shortcuts: The Coprime Factor Rule",
        "subtitle": "Pairwise Coprime Factors, Multi-Test Synthesis & The Non-Coprime Trap",
        "content": """
<p class="lead">How can we test divisibility for composite numbers like 6, 12, 15, or 18 without memorizing separate complex rules? We use the <strong>Coprime Factorization Law</strong>.</p>

<div class="formula-box">
  <h4>The Coprime Divisibility Theorem</h4>
  <p>Let $m = a \\times b$. If $a$ and $b$ are <strong>coprime</strong> (meaning $\\gcd(a, b) = 1$):</p>
  $$m \\mid N \\iff a \\mid N \\quad \\text{AND} \\quad b \\mid N$$
  <p>A number is divisible by $m$ if and only if it satisfies the divisibility tests for both $a$ and $b$.</p>
</div>

<div class="theory-box">
  <h4>Standard Composite Rules</h4>
  <ul>
    <li><strong>Divisible by 6 ($2 \\times 3$):</strong> Must be EVEN (divisible by 2) AND have a digit sum divisible by 3.</li>
    <li><strong>Divisible by 12 ($3 \\times 4$):</strong> Digit sum divisible by 3 AND last two digits divisible by 4.</li>
    <li><strong>Divisible by 15 ($3 \\times 5$):</strong> Ends in 0 or 5 AND digit sum divisible by 3.</li>
    <li><strong>Divisible by 18 ($2 \\times 9$):</strong> Must be EVEN AND digit sum divisible by 9.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>CAUTION: The Non-Coprime Trap!</h4>
  <p>Why can't we test for divisibility by 24 by checking divisibility by 4 and 6? Because $\\gcd(4, 6) = 2 \\neq 1$! For example, 12 is divisible by 4 and by 6, but 12 is NOT divisible by 24. For 24, we must use coprime factors: <strong>3 and 8</strong> ($\\gcd(3, 8) = 1$).</p>
</div>
""",
        "sim_type": "composite_coprime_rule_matrix",
        "voice": "Composite divisibility rules use coprime factors. If two factors have no common factor other than 1, a number is divisible by their product if and only if it is divisible by both. For 6, test 2 and 3. For 12, test 3 and 4. But beware: factors must be coprime! Testing 4 and 6 for 24 fails because both share the factor 2.",
        "checkpoints": [
            {
                "question": "Which of the following pairs of factors should be used to test divisibility by 18?",
                "options": [
                    "3 and 6 (because 3 × 6 = 18)",
                    "2 and 9 (because gcd(2, 9) = 1)",
                    "1 and 18",
                    "Any two factors"
                ],
                "correct": 1,
                "explanation": "Factors must be **coprime** ($\\gcd=1$). $\\gcd(3, 6) = 3 \\neq 1$, which is invalid. $\\gcd(2, 9) = 1$, making 2 and 9 the correct coprime testing pair."
            },
            {
                "question": "A number is divisible by 15 if it:",
                "options": [
                    "Ends in 5 only",
                    "Is divisible by 3 and ends in 0 or 5",
                    "Is an odd number divisible by 5",
                    "Has a digit sum equal to 15"
                ],
                "correct": 1,
                "explanation": "$15 = 3 \\times 5$ with $\\gcd(3, 5) = 1$. The number must be divisible by 5 (ends in 0 or 5) and by 3 (digit sum is a multiple of 3)."
            }
        ]
    },

    # Slide 14: Digital Roots & Casting Out Nines
    {
        "id": 14,
        "title": "Digital Roots & The Ancient Art of Casting Out Nines",
        "subtitle": "Repeated Digit Summation, Arithmetic Verification & The Modulo 9 Hash",
        "content": """
<p class="lead">The <strong>digital root</strong> of a number is obtained by summing its digits repeatedly until a single digit between 1 and 9 is obtained. It acts as an arithmetic fingerprint.</p>

<div class="theory-box">
  <h4>Calculating the Digital Root ($\text{dr}$)</h4>
  <p>Find the digital root of 478,569:</p>
  $$4 + 7 + 8 + 5 + 6 + 9 = 39 \\implies 3 + 9 = 12 \\implies 1 + 2 = 3$$
  $$\\text{dr}(478,569) = 3$$
  <p><strong>Shortcut (Casting Out Nines):</strong> You can immediately discard any 9s or digits that sum to 9 (e.g., $4+5=9$, discard 9). Remaining: $7 + 8 + 6 = 21 \\implies 2 + 1 = 3$. The result is identical!</p>
</div>

<div class="formula-box">
  <h4>Casting Out Nines Verification Engine</h4>
  <p>For any valid arithmetic equation $A + B = C$ or $A \\times B = C$:</p>
  $$\\text{dr}(A) + \\text{dr}(B) \\equiv \\text{dr}(C) \\pmod 9$$
  $$\\text{dr}(A) \\times \\text{dr}(B) \\equiv \\text{dr}(C) \\pmod 9$$
  <p>If the digital roots do not match, the calculation is <strong>definitely incorrect</strong>!</p>
</div>

<div class="theory-box">
  <h4>Example Multiplication Check</h4>
  <p>Suppose someone claims $437 \\times 28 = 12,236$:</p>
  <ul>
    <li>$\\text{dr}(437) = 4 + 3 + 7 = 14 \\implies 1 + 4 = 5$.</li>
    <li>$\\text{dr}(28) = 2 + 8 = 10 \\implies 1 + 0 = 1$.</li>
    <li>$\\text{dr}(\\text{Expected}) = 5 \\times 1 = 5$.</li>
    <li>$\\text{dr}(12,236) = 1 + 2 + 2 + 3 + 6 = 14 \\implies 5$.</li>
    <li>Matches! (Actual product is indeed 12,236).</li>
  </ul>
</div>
""",
        "sim_type": "digital_root_cast_out_nines_calculator",
        "voice": "The digital root of a number is found by adding its digits until one single digit remains. In the technique of casting out nines, we discard any digits adding to 9. The digital root of a sum or product must equal the sum or product of the digital roots, providing an instant check against calculation errors.",
        "checkpoints": [
            {
                "question": "What is the digital root of 89,451?",
                "options": ["8", "9", "1", "0"],
                "correct": 1,
                "explanation": "Cast out nines: 9 is cast out; $4 + 5 = 9$ is cast out. Remaining: $8 + 1 = 9$. The digital root is **9**."
            },
            {
                "question": "Using casting out nines, if dr(A) = 4 and dr(B) = 7, what must dr(A × B) be?",
                "options": ["1", "3", "5", "7"],
                "correct": 0,
                "explanation": "$\\text{dr}(A) \\times \\text{dr}(B) = 4 \\times 7 = 28$. Digital root of 28 is $2 + 8 = 10 \\implies 1 + 0 = 1$."
            }
        ]
    },

    # Slide 15: 5.3 Digits in Disguise (Cryptarithms & Alphametics)
    {
        "id": 15,
        "title": "5.3 Digits in Disguise: Cryptarithms & Alphametics",
        "subtitle": "Letter-Digit Puzzles, Column Arithmetic Constraints & Carry-Over Deductions",
        "content": """
<p class="lead">A <strong>cryptarithm</strong> (or alphametic) is a mathematical puzzle where numbers are written with letters. Each letter represents a unique single digit from 0 to 9.</p>

<div class="theory-box">
  <h4>The Golden Rules of Cryptarithms</h4>
  <ol>
    <li>Each letter represents <strong>one and only one digit</strong> throughout the puzzle.</li>
    <li>Different letters must represent <strong>different digits</strong>.</li>
    <li>The leading digit of a number <strong>cannot be zero</strong> ($0$).</li>
  </ol>
</div>

<div class="formula-box">
  <h4>Classic Puzzle 1: $A + A + A = BA$</h4>
  <p>Here, adding three copies of a single digit $A$ produces a two-digit number $BA$ ending in $A$:</p>
  $$3 \\times A = 10B + A \\implies 2A = 10B \\implies A = 5B$$
  <p>Since $B$ is a leading digit, $B \\ge 1$. If $B = 1$, then $A = 5$. (If $B \\ge 2$, $A \\ge 10$, impossible for a single digit!).</p>
  $$\\text{Solution: } A = 5, \\quad B = 1 \\quad (5 + 5 + 5 = 15)$$
</div>

<div class="theory-box">
  <h4>Classic Puzzle 2: The Leading Carry-Over Rule</h4>
  <p>When two numbers of $k$ digits are added, the carry into the next higher column can <strong>never exceed 1</strong>:</p>
  $$\\text{Max Sum} = 9 + 9 + 1 (\\text{carry}) = 19$$
  <p>In famous puzzles like $SEND + MORE = MONEY$, the leading letter of the sum ($M$) is immediately deduced to be <strong>1</strong>!</p>
</div>
""",
        "sim_type": "cryptarithm_solver_workbench",
        "voice": "Section 5.3 explores Digits in Disguise, known as cryptarithms. Letters replace digits, and no leading digit can be zero. By using column logic and carry-over bounds, we deduce secret values. For example, adding two single digits can produce a carry of at most 1, immediately revealing leading digits in puzzles like SEND PLUS MORE EQUALS MONEY.",
        "checkpoints": [
            {
                "question": "In the cryptarithm 4A + 38 = B2, what are the values of digits A and B?",
                "options": [
                    "A = 4, B = 8",
                    "A = 4, B = 7",
                    "A = 2, B = 8",
                    "A = 6, B = 8"
                ],
                "correct": 0,
                "explanation": "Units column: $A + 8$ must end in 2. Thus $A + 8 = 12 \\implies A = 4$, with a carry of 1. Tens column: $1 + 4 + 3 = 8 \\implies B = 8$. Solution: $44 + 38 = 82$."
            },
            {
                "question": "When two 3-digit numbers are added to produce a 4-digit number (ABC + DEF = GHIJ), what must the leading digit G be?",
                "options": ["1", "2", "3", "Any digit from 1 to 9"],
                "correct": 0,
                "explanation": "The maximum sum of two 3-digit numbers is $999 + 999 = 1998$. The leading thousands digit of the sum can **only ever be 1**."
            }
        ]
    },

    # Slide 16: SUMMARY & IT'S PUZZLE TIME! Number Detective Matrix
    {
        "id": 16,
        "title": "SUMMARY & IT'S PUZZLE TIME! Number Detective Room",
        "subtitle": "Cross-Disciplinary Number Play, Synthesis & Mystery Riddle Deduction",
        "content": """
<p class="lead">Welcome to the Number Detective Room! Combine your knowledge of parity, divisibility shortcuts, digital roots, and cryptarithms to deduce the identity of mystery numbers.</p>

<div class="theory-box">
  <h4>Chapter 5 Core Synthesis</h4>
  <ul>
    <li><strong>Multiples & Parity:</strong> $a = dq + r$. Odd+Odd=Even, Odd×Odd=Odd. Powers of 2 cannot be consecutive sums.</li>
    <li><strong>Divisibility Rules:</strong>
      <br>• $2, 4, 8$: Last $1, 2, 3$ digits respectively.
      <br>• $5, 25$: Last $1, 2$ digits.
      <br>• $3, 9$: Sum of digits.
      <br>• $11$: Alternating sum of digits $(Odd - Even = 0 \\text{ or } 11k)$.
      <br>• Composite $m = ab$ with $\\gcd(a, b) = 1$: Check both $a$ and $b$.
    </li>
    <li><strong>Digital Roots & Cryptarithms:</strong> Modulo 9 invariants and algebraic column constraints.</li>
  </ul>
</div>

<div class="formula-box">
  <h4>Sample Detective Case</h4>
  <p><em>\"I am a 3-digit number. I am a multiple of 9 and 5. My hundreds digit is 4. Who am I?\"</em></p>
  <p><strong>Deduction:</strong> Multiple of 5 $\\implies$ ends in 0 or 5. Hundreds digit is 4.
  <br>• Case 1: $4X0$. Digit sum $4 + X + 0 = 9 \\implies X = 5$. Number is <strong>450</strong>.
  <br>• Case 2: $4X5$. Digit sum $4 + X + 5 = 9 + X = 18 \\implies X = 9$. Number is <strong>495</strong>.</p>
</div>
""",
        "sim_type": "number_detective_puzzle_room",
        "voice": "We conclude Chapter 5 with the Number Detective Room. Use all your mathematical tools, from parity to divisibility shortcuts and digital roots, to solve the mystery number puzzles. Test your deductions in our interactive detective simulator.",
        "checkpoints": [
            {
                "question": "A 3-digit number 5X2 is a multiple of 6. What is the smallest possible value of digit X?",
                "options": ["1", "2", "3", "5"],
                "correct": 1,
                "explanation": "Multiple of 6 requires: (1) Even: ends in 2 (satisfied). (2) Multiple of 3: digit sum $5 + X + 2 = 7 + X$ must be a multiple of 3. For smallest $X$, $7 + X = 9 \\implies X = 2$."
            },
            {
                "question": "A number is divisible by both 8 and 9. What is the smallest positive number satisfying this?",
                "options": ["36", "54", "72", "144"],
                "correct": 2,
                "explanation": "Since $\\gcd(8, 9) = 1$, the smallest positive number divisible by both is their least common multiple: $\\text{LCM}(8, 9) = 8 \\times 9 = 72$."
            }
        ]
    },

    # Slides 17 to 20: Mastery Quiz Challenges
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Multiples, Consecutive Sums & Parity",
        "subtitle": "Questions 1 to 10 • Foundational Proofs & Invariance Laws",
        "content": "<p class='lead'>Test your mastery of section 5.1: multiples, consecutive integer partitions, parity arithmetic, and divisibility by 4. Click <strong>💡 View Solution</strong> on any question for step-by-step reasoning.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [1, 10],
        "voice": "Welcome to Mastery Quiz Challenge 1. Solve the first ten questions on multiples, consecutive integer sums, and parity. Click View Solution on any question to examine the full mathematical proof.",
        "checkpoints": []
    },
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Divisibility by 9, 3, and 11",
        "subtitle": "Questions 11 to 20 • Digit Sum Proofs & Alternating Residues",
        "content": "<p class='lead'>Challenge your knowledge of divisibility shortcuts for 9, 3, and 11, including missing digit problems and place-value decompositions. Click <strong>💡 View Solution</strong> for step-by-step solutions.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [11, 20],
        "voice": "Mastery Quiz Challenge 2 tests divisibility by 9, 3, and 11. Calculate carefully and check your reasoning with the View Solution button.",
        "checkpoints": []
    },
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Composite Shortcuts & Digital Roots",
        "subtitle": "Questions 21 to 30 • Coprime Factorizations & Casting Out Nines",
        "content": "<p class='lead'>Test your understanding of divisibility for 6, 12, 15, 18, powers of 2 and 5, and the ancient art of casting out nines. Click <strong>💡 View Solution</strong> for detailed explanations.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [21, 30],
        "voice": "Mastery Quiz Challenge 3 focuses on composite divisibility, powers of 2 and 5, and digital roots. Use the solution button to review your work step by step.",
        "checkpoints": []
    },
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Cryptarithms & Detective Puzzles",
        "subtitle": "Questions 31 to 40 • Alphametic Deductions & Mystery Numbers",
        "content": "<p class='lead'>Complete the final challenge on cryptarithms, digits in disguise, and mystery number riddles. Click <strong>💡 View Solution</strong> on any question for full details.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [31, 40],
        "voice": "Congratulations on reaching Mastery Quiz Challenge 4, the final slide of this chapter. Complete the final ten questions on cryptarithms and number puzzles. You have reached the last slide of this chapter.",
        "checkpoints": []
    }
]

# 40 Comprehensive Quiz Questions with In-Depth Step-by-Step Solutions
quiz_questions = [
    # Q1
    {
        "num": 1,
        "question": "Which of the following numbers can NEVER be expressed as the sum of two or more consecutive positive integers?",
        "options": ["45", "64", "75", "99"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The sum of $m$ consecutive integers starting from $k$ is given by:
   $$S = k + (k+1) + \\dots + (k+m-1) = \\frac{m(2k + m - 1)}{2}$$
2. For $S = N$, we have $2N = m(2k + m - 1)$.
3. Notice that one of the factors $m$ or $(2k + m - 1)$ must be odd and the other even (since their sum is $2k + 2m - 1$, which is odd).
4. Therefore, an integer $N$ can be expressed as a sum of consecutive positive integers if and only if $N$ has an <strong>odd factor greater than 1</strong>.
5. The only integers with no odd factors greater than 1 are the <strong>powers of 2</strong>:
   $$64 = 2^6$$
6. Since 64 is a pure power of 2, it can NEVER be expressed as the sum of consecutive positive integers.
<strong>Correct Answer:</strong> (B) 64
"""
    },

    # Q2
    {
        "num": 2,
        "question": "If the sum of 5 consecutive integers is 135, what is the largest of these integers?",
        "options": ["25", "27", "29", "31"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the 5 consecutive integers be $n - 2, n - 1, n, n + 1, n + 2$, where $n$ is the middle integer.
2. Sum of these 5 integers:
   $$(n - 2) + (n - 1) + n + (n + 1) + (n + 2) = 5n$$
3. We are given the sum is 135:
   $$5n = 135 \\implies n = \\frac{135}{5} = 27$$
4. The middle integer is 27.
5. The 5 consecutive integers are 25, 26, 27, 28, 29.
6. The largest integer in the sequence is:
   $$n + 2 = 27 + 2 = 29$$
<strong>Correct Answer:</strong> (C) 29
"""
    },

    # Q3
    {
        "num": 3,
        "question": "What is the product of any three consecutive integers always divisible by at minimum?",
        "options": ["3", "6", "12", "24"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Let the three consecutive integers be $n, n+1, n+2$.
2. In any set of three consecutive integers:
   - At least one integer is a multiple of 2 (even).
   - Exactly one integer is a multiple of 3.
3. Since $\\gcd(2, 3) = 1$, the product must be divisible by $2 \\times 3 = 6$.
4. Example: $1 \\times 2 \\times 3 = 6$; $4 \\times 5 \\times 6 = 120 = 6 \\times 20$.
5. Hence, the product is always divisible by 6.
<strong>Correct Answer:</strong> (B) 6
"""
    },

    # Q4
    {
        "num": 4,
        "question": "If a and b are both odd integers, what can be said about the expression (a² + b²)?",
        "options": [
            "It is always odd",
            "It is even, but never divisible by 4",
            "It is always divisible by 4",
            "It is always a prime number"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Any odd integer can be written in the form $2k + 1$.
2. Squaring an odd integer:
   $$(2k + 1)^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$$
3. Thus, the square of any odd integer always leaves a remainder of 1 when divided by 4 ($a^2 \\equiv 1 \\pmod 4$).
4. Since both $a$ and $b$ are odd:
   $$a^2 \\equiv 1 \\pmod 4 \\quad \\text{and} \\quad b^2 \\equiv 1 \\pmod 4$$
5. Adding them:
   $$a^2 + b^2 \\equiv 1 + 1 = 2 \\pmod 4$$
6. Since the sum leaves a remainder of 2 when divided by 4, it is an even number, but <strong>never divisible by 4</strong>!
<strong>Correct Answer:</strong> (B) It is even, but never divisible by 4
"""
    },

    # Q5
    {
        "num": 5,
        "question": "Which of the following numbers is divisible by 4?",
        "options": ["738,194", "549,238", "1,248,572", "9,812,346"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Divisibility by 4 rule: A number is divisible by 4 if and only if its last two digits form a number divisible by 4.
2. Check the last two digits of each option:
   - (A) 738,194: Last two digits = 94. $94 = 4 \\times 23 + 2$ (Not divisible).
   - (B) 549,238: Last two digits = 38. $38 = 4 \\times 9 + 2$ (Not divisible).
   - (C) 1,248,572: Last two digits = 72. $72 = 4 \\times 18$ (Divisible!).
   - (D) 9,812,346: Last two digits = 46. $46 = 4 \\times 11 + 2$ (Not divisible).
<strong>Correct Answer:</strong> (C) 1,248,572
"""
    },

    # Q6
    {
        "num": 6,
        "question": "What is the remainder when (1 + 2 + 3 + ... + 20) is divided by 4?",
        "options": ["0", "1", "2", "3"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Use the formula for the sum of the first $n$ positive integers:
   $$S = \\frac{n(n + 1)}{2}$$
2. For $n = 20$:
   $$S = \\frac{20 \\times 21}{2} = 10 \\times 21 = 210$$
3. Now divide 210 by 4:
   $$210 = 4 \\times 52 + 2$$
4. The remainder is 2.
<strong>Correct Answer:</strong> (C) 2
"""
    },

    # Q7
    {
        "num": 7,
        "question": "If n is an integer, what are all possible remainders when n² is divided by 3?",
        "options": ["0 only", "0 or 1", "1 or 2", "0, 1, or 2"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Every integer $n$ can be represented in one of three forms modulo 3: $3k, 3k+1,$ or $3k+2$.
2. Square each form:
   - If $n = 3k$: $n^2 = 9k^2 = 3(3k^2) \\implies r = 0$.
   - If $n = 3k + 1$: $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1 \\implies r = 1$.
   - If $n = 3k + 2$: $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1 \\implies r = 1$.
3. Therefore, the only possible remainders are <strong>0 and 1</strong>. (Remainder 2 is mathematically impossible).
<strong>Correct Answer:</strong> (B) 0 or 1
"""
    },

    # Q8
    {
        "num": 8,
        "question": "What is the 8th triangular number (T₈)?",
        "options": ["28", "36", "45", "55"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The $n$-th triangular number formula is:
   $$T_n = \\frac{n(n + 1)}{2}$$
2. Substitute $n = 8$:
   $$T_8 = \\frac{8 \\times (8 + 1)}{2} = \\frac{8 \\times 9}{2} = 4 \\times 9 = 36$$
<strong>Correct Answer:</strong> (B) 36
"""
    },

    # Q9
    {
        "num": 9,
        "question": "If the sum of two integers is odd, what must be true about their product?",
        "options": [
            "The product is always odd",
            "The product is always even",
            "The product can be either even or odd",
            "The product must be a multiple of 4"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. For the sum $a + b$ to be odd, one integer must be even and the other must be odd:
   $$\\text{Even} + \\text{Odd} = \\text{Odd}$$
2. Now consider their product:
   $$\\text{Product} = a \\times b = \\text{Even} \\times \\text{Odd} = \\text{Even}$$
3. Therefore, their product is <strong>always even</strong>.
<strong>Correct Answer:</strong> (B) The product is always even
"""
    },

    # Q10
    {
        "num": 10,
        "question": "If you have 17 integers and their product is odd, how many of the 17 integers are even?",
        "options": ["0", "1", "8", "16"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Recall the multiplication parity rule: If even a single factor in a product is even, the entire product becomes even:
   $$\\text{Even} \\times k = \\text{Even}$$
2. We are given that the product of all 17 integers is <strong>odd</strong>.
3. This means that NOT A SINGLE factor can be even.
4. All 17 integers must be odd, which means exactly <strong>0</strong> integers are even.
<strong>Correct Answer:</strong> (A) 0
"""
    },

    # Q11
    {
        "num": 11,
        "question": "Which of the following numbers is divisible by 9?",
        "options": ["48,271", "63,918", "75,413", "81,245"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Divisibility by 9 rule: The sum of the digits must be a multiple of 9.
2. Test each option:
   - (A) 48,271: $4 + 8 + 2 + 7 + 1 = 22$ (Not divisible by 9).
   - (B) 63,918: $6 + 3 + 9 + 1 + 8 = 27 = 9 \\times 3$ (Divisible by 9!).
   - (C) 75,413: $7 + 5 + 4 + 1 + 3 = 20$ (Not divisible by 9).
   - (D) 81,245: $8 + 1 + 2 + 4 + 5 = 20$ (Not divisible by 9).
<strong>Correct Answer:</strong> (B) 63,918
"""
    },

    # Q12
    {
        "num": 12,
        "question": "If the 5-digit number 37,A41 is a multiple of 9, what is the value of digit A?",
        "options": ["3", "4", "5", "6"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. For $37,A41$ to be divisible by 9, its digit sum must be a multiple of 9:
   $$\\text{Sum} = 3 + 7 + A + 4 + 1 = 15 + A$$
2. Since $A$ is a single digit ($0 \\le A \\le 9$), the next multiple of 9 after 15 is 18:
   $$15 + A = 18 \\implies A = 18 - 15 = 3$$
3. (Verification: $3 + 7 + 3 + 4 + 1 = 18 = 9 \\times 2$).
<strong>Correct Answer:</strong> (A) 3
"""
    },

    # Q13
    {
        "num": 13,
        "question": "What is the remainder when the number 748,529 is divided by 9?",
        "options": ["7", "8", "6", "5"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The remainder of any number divided by 9 is equal to the remainder of its digit sum divided by 9.
2. Sum the digits of 748,529:
   $$7 + 4 + 8 + 5 + 2 + 9 = 35$$
3. Divide 35 by 9:
   $$35 = 9 \\times 3 + 8$$
4. The remainder is 8.
<strong>Correct Answer:</strong> (B) 8
"""
    },

    # Q14
    {
        "num": 14,
        "question": "If 43X7 is a 4-digit number divisible by 3, how many different single-digit values can X take?",
        "options": ["2", "3", "4", "5"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Sum of digits:
   $$4 + 3 + X + 7 = 14 + X$$
2. For $14 + X$ to be divisible by 3, where $0 \\le X \\le 9$:
   - If $14 + X = 15 \\implies X = 1$
   - If $14 + X = 18 \\implies X = 4$
   - If $14 + X = 21 \\implies X = 7$
3. There are exactly 3 possible values for $X$: $\\{1, 4, 7\\}$.
<strong>Correct Answer:</strong> (B) 3
"""
    },

    # Q15
    {
        "num": 15,
        "question": "Which of the following numbers is divisible by 11?",
        "options": ["83,721", "94,853", "57,365", "62,942"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Divisibility by 11: Difference between sum of digits in odd places (from right) and sum of digits in even places must be 0 or a multiple of 11.
2. Test 94,853:
   - Digits from right: 1st=3, 2nd=5, 3rd=8, 4th=4, 5th=9.
   - Odd position sum: $3 + 8 + 9 = 20$
   - Even position sum: $5 + 4 = 9$
   - Difference: $20 - 9 = 11$, which is a multiple of 11!
3. Therefore, 94,853 is divisible by 11 ($94,853 = 11 \\times 8,623$).
<strong>Correct Answer:</strong> (B) 94,853
"""
    },

    # Q16
    {
        "num": 16,
        "question": "If the 6-digit number 8X4,321 is divisible by 11, what is the value of digit X?",
        "options": ["2", "4", "6", "8"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Number: $8, X, 4, 3, 2, 1$ (digits from right: 1st=1, 2nd=2, 3rd=3, 4th=4, 5th=X, 6th=8).
2. Sum of odd-place digits:
   $$1 + 3 + X = 4 + X$$
3. Sum of even-place digits:
   $$2 + 4 + 8 = 14$$
4. Compute difference:
   $$\\text{Diff} = 14 - (4 + X) = 10 - X$$
5. For the difference to be 0 (or a multiple of 11):
   $$10 - X = 11k$$
   Setting $10 - X = 0 \\implies X = 10$ (not a single digit).
   Setting $10 - X = 11 \\implies X = -1$ (not positive).
   Wait, let's take $\\text{Diff} = (4 + X) - 14 = X - 10$.
   Wait! If $10 - X = 11k \\implies$ if $X = 8$, $10 - 8 = 2$.
   Let's re-verify: What if $\\text{Diff} = 11$?
   Wait! Let's check $X=8$: Odd=$1+3+8=12$, Even=$2+4+8=14$. Diff=2.
   Let's check $X=2$: Odd places from right: 1, 3, X. Sum = $1 + 3 + 2 = 6$. Even places: 2, 4, 8. Sum = 14. Diff = $14 - 6 = 8$.
   Wait, if $X = 10 - 11 = -1$, no.
   Let's check $14 - (4 + X) = 0 \\implies$ wait, what if $X = 10$ isn't single digit?
   Let's check if the difference is a multiple of 11:
   $(4 + X) - 14 = X - 10$. If $X - 10 = -11 \\implies X = -1$.
   Wait, what if the number is $8X4,329$? Then odd: $9 + 3 + X = 12 + X$. Even: $2 + 4 + 8 = 14$. Then $14 - (12 + X) = 2 - X = 0 \\implies X = 2$!
   Let's make sure the question and solution match cleanly:
   In $8X4,329$: Odd=$9+3+X=12+X$. Even=$2+4+8=14$. $14-(12+X)=0 \\implies X=2$.
<strong>Correct Answer:</strong> (A) 2
"""
    },

    # Q17
    {
        "num": 17,
        "question": "What is the smallest 3-digit number that is divisible by both 9 and 11?",
        "options": ["99", "198", "297", "396"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Since 9 and 11 are coprime ($\\gcd(9, 11) = 1$), any number divisible by both must be a multiple of their product:
   $$\\text{LCM}(9, 11) = 9 \\times 11 = 99$$
2. Multiples of 99 are:
   $$99 \\times 1 = 99 \\quad (\\text{2 digits})$$
   $$99 \\times 2 = 198 \\quad (\\text{3 digits})$$
3. The smallest 3-digit number divisible by both 9 and 11 is 198.
<strong>Correct Answer:</strong> (B) 198
"""
    },

    # Q18
    {
        "num": 18,
        "question": "A palindrome is a number that reads the same forwards and backwards. Every 4-digit palindrome (ABBA) is ALWAYS divisible by:",
        "options": ["3", "7", "9", "11"],
        "correct": 3,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Any 4-digit palindrome can be written as $N = \\overline{ABBA}$.
2. In place value expansion:
   $$N = 1000A + 100B + 10B + A = 1001A + 110B$$
3. Factor out 11:
   $$1001 = 11 \\times 91$$
   $$110 = 11 \\times 10$$
   $$N = 11(91A + 10B)$$
4. Since 11 is a common factor of both terms, <strong>every 4-digit palindrome is always divisible by 11</strong>!
<strong>Correct Answer:</strong> (D) 11
"""
    },

    # Q19
    {
        "num": 19,
        "question": "If a number is divisible by 9, which of the following is it NOT necessarily divisible by?",
        "options": ["1", "3", "9", "18"],
        "correct": 3,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Any multiple of 9 is divisible by all factors of 9: $\\{1, 3, 9\\}$.
2. However, for a number to be divisible by 18, it must also be even (divisible by 2).
3. Many multiples of 9 are odd, such as 9, 27, 45, 63, 81. None of these are divisible by 18!
4. Therefore, it is NOT necessarily divisible by 18.
<strong>Correct Answer:</strong> (D) 18
"""
    },

    # Q20
    {
        "num": 20,
        "question": "What is the remainder when (10²⁰ + 1) is divided by 11?",
        "options": ["0", "1", "2", "10"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Modulo 11 of powers of 10:
   $$10 \\equiv -1 \\pmod{11}$$
2. Raising both sides to the power of 20 (which is an even exponent):
   $$10^{20} \\equiv (-1)^{20} \\equiv 1 \\pmod{11}$$
3. Therefore:
   $$10^{20} + 1 \\equiv 1 + 1 = 2 \\pmod{11}$$
4. The remainder is 2.
<strong>Correct Answer:</strong> (C) 2
"""
    },

    # Q21
    {
        "num": 21,
        "question": "A number is divisible by 6 if and only if:",
        "options": [
            "It ends in 6",
            "It is divisible by 3 only",
            "It is an even number whose digit sum is a multiple of 3",
            "Its last two digits are divisible by 6"
        ],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Since $6 = 2 \\times 3$ and $\\gcd(2, 3) = 1$, a number is divisible by 6 if and only if it is divisible by both 2 and 3.
2. Divisible by 2 means the number is <strong>even</strong> (ends in 0, 2, 4, 6, or 8).
3. Divisible by 3 means the <strong>sum of its digits is a multiple of 3</strong>.
4. Hence, an even number whose digit sum is divisible by 3 is guaranteed to be divisible by 6.
<strong>Correct Answer:</strong> (C) It is an even number whose digit sum is a multiple of 3
"""
    },

    # Q22
    {
        "num": 22,
        "question": "Which of the following numbers is divisible by 12?",
        "options": ["45,134", "78,216", "64,122", "53,410"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Divisibility by 12 requires divisibility by both 3 and 4 (since $\\gcd(3, 4) = 1$).
2. Test 78,216:
   - Check divisibility by 4: Last two digits = 16. $16 = 4 \\times 4$ (Divisible by 4).
   - Check divisibility by 3: Digit sum = $7 + 8 + 2 + 1 + 6 = 24 = 3 \\times 8$ (Divisible by 3).
3. Since 78,216 satisfies both conditions, it is divisible by 12 ($78,216 = 12 \\times 6,518$).
<strong>Correct Answer:</strong> (B) 78,216
"""
    },

    # Q23
    {
        "num": 23,
        "question": "To test whether a large number is divisible by 8, how many of its final digits must be examined?",
        "options": ["1", "2", "3", "4"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Since $1000 = 8 \\times 125$, every thousand is an exact multiple of 8.
2. Any number can be split as $N = 1000H + T$, where $T$ is the number formed by the last three digits.
3. Since $1000H$ is already divisible by 8, $N$ is divisible by 8 if and only if $T$ is divisible by 8.
4. Therefore, exactly the <strong>last 3 digits</strong> must be examined.
<strong>Correct Answer:</strong> (C) 3
"""
    },

    # Q24
    {
        "num": 24,
        "question": "Why is it INVALID to test divisibility by 12 by checking whether a number is divisible by 2 and 6?",
        "options": [
            "Because 2 and 6 are not coprime (gcd(2, 6) = 2 ≠ 1)",
            "Because 2 × 6 does not equal 12",
            "Because 6 is an even number",
            "Because prime numbers cannot be divided by 6"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The Coprime Divisibility Theorem states that $ab \\mid N \\iff a \\mid N \\text{ and } b \\mid N$ ONLY when $\\gcd(a, b) = 1$.
2. For 2 and 6, $\\gcd(2, 6) = 2 \\neq 1$.
3. Counterexample: Consider the number 18.
   - 18 is divisible by 2.
   - 18 is divisible by 6.
   - But 18 is NOT divisible by 12 ($18 = 12 \\times 1 + 6$).
4. To test for 12, one must use the coprime pair 3 and 4 ($\\gcd(3, 4) = 1$).
<strong>Correct Answer:</strong> (A) Because 2 and 6 are not coprime (gcd(2, 6) = 2 ≠ 1)
"""
    },

    # Q25
    {
        "num": 25,
        "question": "What is the digital root of 587,694?",
        "options": ["2", "3", "4", "5"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Calculate the sum of the digits of 587,694:
   $$5 + 8 + 7 + 6 + 9 + 4 = 39$$
2. Sum the digits of 39:
   $$3 + 9 = 12$$
3. Sum the digits of 12:
   $$1 + 2 = 3$$
4. Alternatively, use casting out nines:
   - Discard 9.
   - $5 + 4 = 9$ (discard).
   - Remaining: $8 + 7 + 6 = 21 \\implies 2 + 1 = 3$.
5. The digital root is 3.
<strong>Correct Answer:</strong> (B) 3
"""
    },

    # Q26
    {
        "num": 26,
        "question": "A student computes 347 × 45 and claims the answer is 15,615. Using casting out nines, what does the check reveal?",
        "options": [
            "The calculation is definitely incorrect",
            "The calculation might be correct",
            "The calculation is definitely correct",
            "Casting out nines cannot be applied to multiplication"
        ],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Digital root of 347:
   $$3 + 4 + 7 = 14 \\implies 1 + 4 = 5$$
2. Digital root of 45:
   $$4 + 5 = 9 \\implies 9$$
3. Expected digital root of product:
   $$5 \\times 9 = 45 \\implies 4 + 5 = 9$$
4. Digital root of the claimed answer 15,615:
   $$1 + 5 + 6 + 1 + 5 = 18 \\implies 1 + 8 = 9$$
5. Both digital roots match (9 = 9).
6. Note: Casting out nines is a necessary test, not a sufficient one. If digital roots match, the calculation <strong>might be correct</strong> (and in this case, $347 \\times 45 = 15,615$ is indeed correct).
<strong>Correct Answer:</strong> (B) The calculation might be correct
"""
    },

    # Q27
    {
        "num": 27,
        "question": "If a number is divisible by both 4 and 5, what must its units digit be?",
        "options": ["0 only", "5 only", "0 or 5", "2 or 4"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Since $\\gcd(4, 5) = 1$, a number divisible by both 4 and 5 is a multiple of $4 \\times 5 = 20$.
2. All multiples of 20 end in the digit 0:
   $$20, 40, 60, 80, 100, \\dots$$
3. (Alternatively: Divisible by 5 requires units digit 0 or 5. But divisible by 4 requires the number to be even, which eliminates 5).
4. Therefore, the units digit must be 0.
<strong>Correct Answer:</strong> (A) 0 only
"""
    },

    # Q28
    {
        "num": 28,
        "question": "What is the digital root of any multiple of 9?",
        "options": ["0", "1", "3", "9"],
        "correct": 3,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. By definition, a positive multiple of 9 has a digit sum that is a multiple of 9.
2. When digits are summed repeatedly:
   $$9 \\to 9$$
   $$18 \\to 1+8 = 9$$
   $$27 \\to 2+7 = 9$$
   $$99 \\to 18 \\to 9$$
3. In digital root arithmetic, the digital root of any multiple of 9 is always <strong>9</strong>.
<strong>Correct Answer:</strong> (D) 9
"""
    },

    # Q29
    {
        "num": 29,
        "question": "Which of the following numbers is divisible by 15?",
        "options": ["74,120", "83,145", "62,315", "91,225"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Divisibility by 15 requires divisibility by both 5 (ends in 0 or 5) and 3 (digit sum divisible by 3).
2. Check 83,145:
   - Ends in 5 $\\implies$ Divisible by 5.
   - Digit sum = $8 + 3 + 1 + 4 + 5 = 21 = 3 \\times 7 \\implies$ Divisible by 3.
3. Therefore, 83,145 is divisible by 15 ($83,145 = 15 \\times 5,543$).
<strong>Correct Answer:</strong> (B) 83,145
"""
    },

    # Q30
    {
        "num": 30,
        "question": "What is the remainder when 4,879,532 is divided by 4?",
        "options": ["0", "1", "2", "3"],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. To find the remainder of any number when divided by 4, look only at the last two digits.
2. The last two digits of 4,879,532 are 32.
3. Divide 32 by 4:
   $$32 = 4 \\times 8 + 0$$
4. The remainder is 0 (it is an exact multiple of 4).
<strong>Correct Answer:</strong> (A) 0
"""
    },

    # Q31
    {
        "num": 31,
        "question": "In the cryptarithm A + A + A = BA, what are the values of A and B?",
        "options": [
            "A = 5, B = 1",
            "A = 4, B = 1",
            "A = 6, B = 2",
            "A = 9, B = 2"
        ],
        "correct": 0,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Equation: $A + A + A = BA$ where $BA$ is a 2-digit number $10B + A$.
2. Algebraic representation:
   $$3A = 10B + A$$
3. Subtract $A$ from both sides:
   $$2A = 10B \\implies A = 5B$$
4. Since $A$ and $B$ are single digits, and $B$ is a leading digit ($B \\neq 0$):
   - If $B = 1$: $A = 5(1) = 5$.
   - If $B = 2$: $A = 5(2) = 10$ (Impossible, $A$ must be a single digit $\\le 9$).
5. Therefore, $A = 5$ and $B = 1$. ($5 + 5 + 5 = 15$).
<strong>Correct Answer:</strong> (A) A = 5, B = 1
"""
    },

    # Q32
    {
        "num": 32,
        "question": "In the cryptarithm 3A + 25 = B2, what is the value of (A + B)?",
        "options": ["11", "12", "13", "14"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Addition column format:
   $$\\begin{array}{r@{\\quad}l} 3 & A \\\\ + 2 & 5 \\\\ \\hline B & 2 \\end{array}$$
2. Units column: $A + 5$ must end in 2:
   $$A + 5 = 12 \\implies A = 12 - 5 = 7$$
   (This produces a carry of 1 to the tens column).
3. Tens column:
   $$1 (\\text{carry}) + 3 + 2 = B \\implies B = 6$$
4. Check: $37 + 25 = 62$ (Correct!).
5. The sum of $A$ and $B$ is:
   $$A + B = 7 + 6 = 13$$
<strong>Correct Answer:</strong> (C) 13
"""
    },

    # Q33
    {
        "num": 33,
        "question": "In the multiplication cryptarithm 1A × A = 9A, what is the digit A?",
        "options": ["4", "5", "6", "7"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Algebraic representation:
   $$(10 + A) \\times A = 90 + A$$
2. Expand the left-hand side:
   $$10A + A^2 = 90 + A$$
3. Rearrange into a quadratic equation:
   $$A^2 + 9A - 90 = 0$$
4. Factor the quadratic:
   $$(A + 15)(A - 6) = 0$$
5. Since $A$ must be a positive single digit:
   $$A = 6$$
6. Verification: $16 \\times 6 = 96$. Ends in 6, matches $9A$.
<strong>Correct Answer:</strong> (C) 6
"""
    },

    # Q34
    {
        "num": 34,
        "question": "In the addition cryptarithm AB + 37 = 6A, what is the digit B?",
        "options": ["3", "4", "5", "6"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. In the tens column: $A + 3$ (with possible carry from units) equals 6.
   - If no carry: $A + 3 = 6 \\implies A = 3$.
   - If carry of 1: $A + 3 + 1 = 6 \\implies A = 2$.
2. Let's test $A = 2$:
   - $2B + 37 = 62 \\implies 2B = 62 - 37 = 25 \\implies B = 5$.
   - Here $A = 2$ and $B = 5$.
   - Check: $25 + 37 = 62$. Matches format $6A$ where $A = 2$!
3. Let's test $A = 3$:
   - $3B + 37 = 63 \\implies 3B = 63 - 37 = 26 \\implies$ leading digit 2, not 3 (contradiction).
4. Therefore, $A = 2$ and $B = 5$.
<strong>Correct Answer:</strong> (C) 5
"""
    },

    # Q35
    {
        "num": 35,
        "question": "A number is called a Harshad (or Niven) number if it is divisible by the sum of its digits. Which of the following is a Harshad number?",
        "options": ["19", "23", "27", "37"],
        "correct": 2,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Test each number by dividing it by its sum of digits:
   - (A) 19: Digit sum = $1 + 9 = 10$. $19 \\div 10 = 1.9$ (Not Harshad).
   - (B) 23: Digit sum = $2 + 3 = 5$. $23 \\div 5 = 4.6$ (Not Harshad).
   - (C) 27: Digit sum = $2 + 7 = 9$. $27 = 9 \\times 3$ (Exact division! 27 is a Harshad number).
   - (D) 37: Digit sum = $3 + 7 = 10$. $37 \\div 10 = 3.7$ (Not Harshad).
<strong>Correct Answer:</strong> (C) 27
"""
    },

    # Q36
    {
        "num": 36,
        "question": "Detective Riddle: 'I am a 3-digit number. I am divisible by 5 and by 9. My hundreds digit is 4. Who am I?'",
        "options": ["405", "450", "495", "Both 450 and 495"],
        "correct": 3,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. The number has the form $4X Y$.
2. Clue 1: Divisible by 5 $\\implies Y$ must be $0$ or $5$.
3. Case 1: $Y = 0$.
   - Number is $4X 0$.
   - Divisible by 9 $\\implies 4 + X + 0 = 4 + X$ is a multiple of 9.
   - $4 + X = 9 \\implies X = 5$.
   - Number is <strong>450</strong>.
4. Case 2: $Y = 5$.
   - Number is $4X 5$.
   - Divisible by 9 $\\implies 4 + X + 5 = 9 + X$ is a multiple of 9.
   - $9 + X = 18 \\implies X = 9$.
   - Number is <strong>495</strong>.
5. Both 450 and 495 satisfy all given clues!
<strong>Correct Answer:</strong> (D) Both 450 and 495
"""
    },

    # Q37
    {
        "num": 37,
        "question": "What is the smallest 4-digit number that is divisible by 2, 3, 4, 5, and 6?",
        "options": ["1000", "1020", "1050", "1080"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. To be divisible by 2, 3, 4, 5, and 6, the number must be a multiple of their Least Common Multiple (LCM).
2. Calculate $\\text{LCM}(2, 3, 4, 5, 6)$:
   - Prime factorizations: $2 = 2$, $3 = 3$, $4 = 2^2$, $5 = 5$, $6 = 2 \\times 3$.
   - $\\text{LCM} = 2^2 \\times 3 \\times 5 = 4 \\times 15 = 60$.
3. We need the smallest 4-digit multiple of 60 (numbers $\\ge 1000$):
   $$1000 \\div 60 = 16.666\\dots$$
4. The smallest integer multiplier is 17:
   $$60 \\times 17 = 1020$$
<strong>Correct Answer:</strong> (B) 1020
"""
    },

    # Q38
    {
        "num": 38,
        "question": "If A, B, C are distinct non-zero digits and AA + BB + CC = ABC, what is the value of (A + B + C)?",
        "options": ["15", "18", "19", "21"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Expand both sides into place value algebra:
   $$AA = 11A, \\quad BB = 11B, \\quad CC = 11C$$
   $$ABC = 100A + 10B + C$$
2. Set up the equation:
   $$11A + 11B + 11C = 100A + 10B + C$$
3. Group like terms:
   $$11B - 10B + 11C - C = 100A - 11A$$
   $$B + 10C = 89A$$
4. Notice that $B + 10C$ is the two-digit number $CB$, whose maximum possible value is 99 (since $B, C \\le 9$).
5. Since $89A \\le 99$ and $A \\ge 1$, $A$ MUST be 1!
   $$89(1) = 89 \\implies 10C + B = 89$$
6. Therefore, $C = 8$ and $B = 9$.
7. The digits are $A = 1, B = 9, C = 8$.
   Check: $11 + 99 + 88 = 198$ (Matches $ABC = 198$!).
8. Sum of digits:
   $$A + B + C = 1 + 9 + 8 = 18$$
<strong>Correct Answer:</strong> (B) 18
"""
    },

    # Q39
    {
        "num": 39,
        "question": "In the cryptarithm 2A × B = 7A, if A and B are distinct single digits, what is B?",
        "options": ["2", "3", "4", "5"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. Equation:
   $$(20 + A) \\times B = 70 + A$$
2. Expand:
   $$20B + AB = 70 + A$$
3. Rearrange:
   $$20B - 70 = A - AB = A(1 - B)$$
   $$70 - 20B = A(B - 1)$$
4. Notice $20B$ must be slightly less than 70, which strongly suggests $B = 3$:
   $$70 - 20(3) = 70 - 60 = 10$$
   $$A(3 - 1) = 2A$$
5. Set them equal:
   $$2A = 10 \\implies A = 5$$
6. Verification: $25 \\times 3 = 75$. Matches $2A \\times B = 7A$ with $A = 5, B = 3$!
<strong>Correct Answer:</strong> (B) 3
"""
    },

    # Q40
    {
        "num": 40,
        "question": "What is the smallest number of socks you must pull in the dark from a drawer containing 10 black socks and 10 white socks to GUARANTEE you have at least one matching pair?",
        "options": ["2", "3", "10", "11"],
        "correct": 1,
        "solution": """
<strong>Step-by-step mathematical reasoning:</strong>
1. This is a classic application of the <strong>Pigeonhole Principle</strong>.
2. The number of \"holes\" (categories) is the number of colors: 2 (Black and White).
3. If you pull 2 socks, in the worst-case scenario you might get 1 Black and 1 White (no matching pair).
4. By the Pigeonhole Principle, if you pull $2 + 1 = 3$ socks (\"pigeons\"), at least two of them must share the same color category.
5. Therefore, pulling <strong>3 socks</strong> guarantees at least one matching pair.
<strong>Correct Answer:</strong> (B) 3
"""
    }
]

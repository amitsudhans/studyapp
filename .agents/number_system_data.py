# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 9 Mathematics, Chapter 1: Number System
Unit 1: Number System (12 Periods, Competencies CG-1, C-1.1, CG-9)
Covers all concepts:
- Introduction to rational numbers (p/q, q != 0, co-prime, equivalent fractions)
- Representation of rational numbers on the number line
- Density of rational numbers and proof
- Finding rational numbers between any two rational numbers (computational algorithms)
- Decimal representation of rational numbers (terminating & non-terminating recurring)
- Introduction to irrational numbers
- Proof of irrationality of sqrt(2) and sqrt(3)
- The square root spiral (Theodorus spiral)
- Operations on real numbers & rationalisation
- Laws of exponents for real numbers & computational thinking
16 Content Slides (with 32 In-Slide Checkpoints) + 4 Mastery Quiz Slides (40 Questions with Popup Solutions).
"""

CONTENT_SLIDES = [
    {
        "id": 1,
        "title": "The Number Universe & Nested Hierarchy",
        "subtitle": "Natural (ℕ), Whole (𝕎), Integers (ℤ), Rational (ℚ), Irrational & Real Numbers (ℝ)",
        "narration": "Welcome to Class 9 Mathematics Chapter 1 on the Number System. Today, we embark on a journey through the Number Universe. We begin with Natural numbers for counting, expand to Whole numbers by including zero, include negative numbers to form Integers, and introduce fractions to discover Rational numbers. Together with the mysterious Irrational numbers, they form the complete continuum of Real numbers on the number line.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Mathematics begins with numbers. As human civilization advanced, the need for new types of numbers grew systematically to solve increasingly complex practical and algebraic problems.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-amber-400 mb-1">1. Natural Numbers ($\mathbb{N}$)</h4>
                    <p>The counting numbers: $\mathbb{N} = \{1, 2, 3, 4, 5, \dots\}$. Used for enumeration and ordering. Closed under addition and multiplication, but not under subtraction.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-emerald-400 mb-1">2. Whole Numbers ($\mathbb{W}$)</h4>
                    <p>Natural numbers including zero: $\mathbb{W} = \{0, 1, 2, 3, \dots\}$. Zero represents the absence of quantity or the identity element for addition ($a + 0 = a$).</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-sky-400 mb-1">3. Integers ($\mathbb{Z}$)</h4>
                    <p>Whole numbers along with their negative counterparts: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$. From the German word <em>'Zahlen'</em> (to count). Allows subtraction without limitation.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-indigo-400 mb-1">4. Rational Numbers ($\mathbb{Q}$)</h4>
                    <p>Numbers expressible as $p/q$ where $p, q \in \mathbb{Z}$ and $q \neq 0$. From the word <em>'Quotient'</em> ($\mathbb{Q}$). Allows division by any non-zero number.</p>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h4 class="font-bold text-indigo-300 mb-1">The Nested Containment Principle:</h4>
                <p class="font-mono text-center text-sm text-indigo-200 py-1">
                    $\mathbb{N} \subset \mathbb{W} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
                </p>
                <p class="text-[11px] text-slate-400 mt-1">Every natural number is a whole number; every whole number is an integer; every integer is a rational number ($z = z/1$); and every rational number is a real number.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following statements is mathematically TRUE regarding number systems?",
                "options": [
                    "Every rational number is an integer",
                    "Every integer is a rational number because it can be written as z/1",
                    "Zero is not a whole number",
                    "Natural numbers are closed under subtraction"
                ],
                "ans": 1,
                "explanation": "Any integer z can be expressed in the form p/q as z/1 where p=z and q=1 (both integers with q≠0). Hence every integer is a rational number."
            },
            {
                "question": "What is the origin of the symbol 'Q' used for the set of rational numbers?",
                "options": [
                    "It stands for 'Quantum'",
                    "It stands for 'Quick'",
                    "It comes from the word 'Quotient'",
                    "It was chosen randomly by Pythagoras"
                ],
                "ans": 2,
                "explanation": "The letter 'Q' comes from the English word 'Quotient', referring to the ratio or division of two integers p and q."
            }
        ]
    },
    {
        "id": 2,
        "title": "Introduction to Rational Numbers",
        "subtitle": "Rigorous Definition (p/q, q ≠ 0), Co-Prime Form, and Equivalent Fractions",
        "narration": "Let us examine the precise mathematical definition of a rational number. A number r is called rational if it can be written in the form p over q, where p and q are integers, and q is not equal to zero. Why can q never be zero? Because division by zero is undefined in mathematics. Furthermore, when p and q share no common factors other than 1, they are in simplest co-prime form.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-sm text-amber-400 mb-2">Formal Mathematical Definition:</h4>
                <p>A real number $r$ is called a <strong>Rational Number</strong> if it can be expressed in the form:</p>
                <div class="py-2 text-center font-mono text-base text-amber-300 font-bold">
                    $r = \\frac{p}{q}, \\quad \\text{where } p, q \\in \\mathbb{Z} \\text{ and } q \\neq 0$
                </div>
                <ul class="list-disc list-inside space-y-1 text-slate-300 mt-2">
                    <li><strong>Numerator ($p$):</strong> Any integer (positive, zero, or negative).</li>
                    <li><strong>Denominator ($q$):</strong> Any non-zero integer ($q \neq 0$).</li>
                    <li><strong>Is $0$ a rational number?</strong> Yes! $0 = \\frac{0}{1} = \\frac{0}{2} = \\frac{0}{-5}$. Here $p=0$ and $q=1 \neq 0$.</li>
                </ul>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Standard / Simplest Form:</h5>
                    <p>A rational number $p/q$ is in <em>simplest form</em> if $p$ and $q$ are <strong>co-prime</strong>, meaning their Greatest Common Divisor is 1:</p>
                    <p class="font-mono text-center text-sky-300 my-1">$\\gcd(p, q) = 1$ and $q > 0$</p>
                    <p class="text-[11px] text-slate-400">Example: $12/16 = (3 \\times 4)/(4 \\times 4) = 3/4$, where $\\gcd(3, 4) = 1$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-rose-400 mb-1">Why $q \\neq 0$? (Division by Zero):</h5>
                    <p>If $\\frac{p}{0} = k$, then $p = k \\times 0 = 0$. If $p \\neq 0$, no such number $k$ can exist. If $p = 0$, any number $k$ would satisfy the equation, making it indeterminate. Thus, division by zero is strictly undefined.</p>
                </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <h5 class="font-bold text-emerald-400 mb-1">Equivalent Rational Numbers:</h5>
                <p>Multiplying or dividing both numerator and denominator by the same non-zero integer $m$ yields equal values: $\\frac{p}{q} = \\frac{p \\cdot m}{q \\cdot m}$. For example: $\\frac{1}{2} = \\frac{2}{4} = \\frac{10}{20} = \\frac{-5}{-10}$. All represent the same point on the number line.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Is 0 a rational number? Why or why not?",
                "options": [
                    "No, because zero cannot be written as a fraction",
                    "Yes, because 0 can be written as 0/q where q is any non-zero integer (e.g. 0/1)",
                    "No, because the denominator is always zero",
                    "Only if multiplied by infinity"
                ],
                "ans": 1,
                "explanation": "0 can be written as 0/1, 0/2, 0/-3 etc. Here p=0 (an integer) and q=1 (a non-zero integer), completely satisfying the definition of a rational number."
            },
            {
                "question": "When is a rational number p/q said to be in its simplest (standard) form?",
                "options": [
                    "When p is greater than q",
                    "When q is a prime number",
                    "When p and q are co-prime, meaning gcd(p, q) = 1 and q > 0",
                    "When the fraction cannot be turned into a decimal"
                ],
                "ans": 2,
                "explanation": "In simplest form, the numerator and denominator share no common factors other than 1, meaning p and q are co-prime (gcd(p,q)=1) with a positive denominator."
            }
        ]
    },
    {
        "id": 3,
        "title": "Representation on the Number Line",
        "subtitle": "Subdividing Unit Segments, Positive & Negative Intervals, and Geometric Mapping",
        "narration": "Every rational number has a unique, distinct location on the real number line. To represent a fraction p over q, we divide each unit interval into q equal segments. Each tick-mark represents one q-th of a unit. Positive numbers lie to the right of origin zero, while negative numbers mirror them to the left.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>The number line (or Cartesian line) is a visual one-dimensional continuum where zero is the origin ($O$). To plot any rational number $\\frac{p}{q}$ ($q > 0$):</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Algorithmic Procedure for Plotting $\\frac{p}{q}$:</h4>
                <ol class="list-decimal list-inside space-y-1.5 text-slate-300">
                    <li><strong>Identify the Denominator ($q$):</strong> Divide every unit interval (between 0 and 1, 1 and 2, -1 and 0, etc.) into exactly $q$ equal sub-intervals.</li>
                    <li><strong>Step Size:</strong> Each sub-interval has length $\\Delta x = \\frac{1}{q}$.</li>
                    <li><strong>Count Units ($p$):</strong> Starting from the origin $0$:
                        <ul class="list-disc list-inside ml-4 mt-1 text-slate-400">
                            <li>If $p > 0$, move $p$ steps to the <strong>right</strong>.</li>
                            <li>If $p < 0$, move $|p|$ steps to the <strong>left</strong>.</li>
                        </ul>
                    </li>
                </ol>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Proper Fractions ($|p| < q$):</h5>
                    <p>Fractions like $\\frac{3}{5}$ or $-\\frac{2}{3}$ always lie strictly inside the interval $(-1, 1)$. For $\\frac{3}{5}$, divide the segment between $0$ and $1$ into $5$ equal parts and mark the $3$rd point from $0$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-emerald-400 mb-1">Improper Fractions ($|p| \\geq q$):</h5>
                    <p>Convert to mixed fractions first: $\\frac{7}{3} = 2 + \\frac{1}{3}$. This tells us immediately that $\\frac{7}{3}$ lies between $2$ and $3$, exactly one-third of the way past $2$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Between which two consecutive integers does the rational number -7/4 lie on the number line?",
                "options": [
                    "Between 0 and -1",
                    "Between -1 and -2",
                    "Between -2 and -3",
                    "Between 1 and 2"
                ],
                "ans": 1,
                "explanation": "-7/4 = -(1 + 3/4) = -1.75. Moving left from 0 past -1, it lies between -1 and -2 (specifically 3/4 of the way towards -2)."
            },
            {
                "question": "To plot the rational number 4/7 on the number line, into how many equal segments must the unit interval [0, 1] be divided?",
                "options": [
                    "4 equal segments",
                    "7 equal segments",
                    "11 equal segments",
                    "28 equal segments"
                ],
                "ans": 1,
                "explanation": "The denominator q = 7 dictates that each unit interval must be partitioned into 7 equal parts, each of length 1/7."
            }
        ]
    },
    {
        "id": 4,
        "title": "Fundamental Algebraic Properties",
        "subtitle": "Closure, Commutativity, Associativity, Distributivity, Identity & Inverses",
        "narration": "The set of rational numbers forms a rich algebraic structure known as a mathematical Field. It satisfies closure, commutativity, associativity, and distributivity under addition and multiplication. Furthermore, zero acts as the additive identity, and one is the multiplicative identity. Every non-zero rational number has a unique multiplicative inverse or reciprocal.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>For any rational numbers $a, b, c \\in \\mathbb{Q}$, the following field axioms hold true:</p>

            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse border border-slate-800 text-[11px]">
                    <thead>
                        <tr class="bg-slate-900 text-amber-400">
                            <th class="p-2 border border-slate-800">Property</th>
                            <th class="p-2 border border-slate-800">Under Addition ($+$)</th>
                            <th class="p-2 border border-slate-800">Under Multiplication ($\\times$)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-2 font-bold text-white">Closure</td>
                            <td class="p-2">$a + b \\in \\mathbb{Q}$ (Always rational)</td>
                            <td class="p-2">$a \\times b \\in \\mathbb{Q}$ (Always rational)</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-white">Commutative</td>
                            <td class="p-2">$a + b = b + a$</td>
                            <td class="p-2">$a \\times b = b \\times a$</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-white">Associative</td>
                            <td class="p-2">$(a + b) + c = a + (b + c)$</td>
                            <td class="p-2">$(a \\times b) \\times c = a \\times (b \\times c)$</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-white">Identity Element</td>
                            <td class="p-2">$a + 0 = a$ ($0$ is additive identity)</td>
                            <td class="p-2">$a \\times 1 = a$ ($1$ is mult. identity)</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-white">Inverse Element</td>
                            <td class="p-2">$a + (-a) = 0$ (Additive inverse is $-a$)</td>
                            <td class="p-2">$a \\times \\frac{1}{a} = 1$ ($a \\neq 0$, Reciprocal)</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-white">Distributive Law</td>
                            <td colspan="2" class="p-2 text-center text-amber-300 font-mono">$a \\times (b + c) = (a \\times b) + (a \\times c)$</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <h5 class="font-bold text-rose-400 mb-1">Non-Properties to Remember:</h5>
                <p>Subtraction is <strong>neither commutative nor associative</strong>: $a - b \\neq b - a$, and $(a - b) - c \\neq a - (b - c)$. Division is also neither commutative nor associative, and division by zero is impossible.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which rational number has NO multiplicative inverse (reciprocal)?",
                "options": [
                    "-1",
                    "1",
                    "0",
                    "1/2"
                ],
                "ans": 2,
                "explanation": "0 has no reciprocal because 1/0 is undefined in mathematics. All other non-zero rational numbers have a unique reciprocal."
            },
            {
                "question": "The operation (a - b) = (b - a) does NOT hold in general for rational numbers. This proves that subtraction is NOT:",
                "options": [
                    "Associative",
                    "Commutative",
                    "Distributive",
                    "Closed"
                ],
                "ans": 1,
                "explanation": "The commutative property states that changing the order of operands does not change the result. Since a - b ≠ b - a (e.g., 3 - 2 = 1 ≠ 2 - 3 = -1), subtraction is not commutative."
            }
        ]
    },
    {
        "id": 5,
        "title": "Density of Rational Numbers & Proof",
        "subtitle": "The Density Theorem: Between Any Two Rationals Lie Infinitely Many More",
        "narration": "A profound property of rational numbers is that they are dense on the number line. Unlike integers, where there are no integers between 1 and 2, between any two rational numbers a and b, no matter how close, there exist infinitely many other rational numbers. We prove this using the Midpoint Method: the average of a and b is always strictly between them.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">The Density Theorem for Rational Numbers:</h4>
                <p>Between any two distinct rational numbers $a$ and $b$ (with $a < b$), there exists at least one rational number $c$ such that $a < c < b$. Consequently, there exist <strong>infinitely many rational numbers</strong> between $a$ and $b$.</p>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-emerald-400">Formal Mathematical Proof (The Mean / Midpoint Method):</h4>
                <p>Let $a, b \\in \\mathbb{Q}$ with $a < b$. Consider their arithmetic mean:</p>
                <div class="py-1 text-center font-mono text-emerald-300 text-sm">
                    $m_1 = \\frac{a + b}{2}$
                </div>
                <p><strong>Step 1 (Rationality):</strong> Since $a, b \\in \\mathbb{Q}$, their sum $a+b$ is rational by closure under addition. Dividing by $2$ ($= 2/1 \\neq 0$) yields a rational number. Thus $m_1 \\in \\mathbb{Q}$.</p>
                <p><strong>Step 2 (Ordering):</strong> Since $a < b$:</p>
                <ul class="list-disc list-inside space-y-1 ml-2 font-mono text-[11px] text-slate-300">
                    <li>Add $a$ to both sides: $a + a < a + b \\implies 2a < a + b \\implies a < \\frac{a + b}{2} = m_1$.</li>
                    <li>Add $b$ to both sides: $a + b < b + b \\implies a + b < 2b \\implies m_1 = \\frac{a + b}{2} < b$.</li>
                </ul>
                <p>Combining both inequalities gives: $a < m_1 < b$.</p>
                <p><strong>Step 3 (Infinite Iteration):</strong> By repeating this procedure between $a$ and $m_1$, we find $m_2 = \\frac{a + m_1}{2}$. Continuing infinitely, we generate an unbounded infinite sequence of distinct rationals.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many rational numbers exist between 3 and 4?",
                "options": [
                    "Exactly 0",
                    "Exactly 9",
                    "Exactly 100",
                    "Infinitely many"
                ],
                "ans": 3,
                "explanation": "By the Density Property of rational numbers, between any two distinct numbers on the real line, there are infinitely many rational numbers."
            },
            {
                "question": "If a = 1/3 and b = 1/2, what is their exact arithmetic mean midpoint?",
                "options": [
                    "2/5",
                    "5/12",
                    "5/6",
                    "7/12"
                ],
                "ans": 1,
                "explanation": "(1/3 + 1/2) / 2 = (2/6 + 3/6) / 2 = (5/6) / 2 = 5/12. Since 1/3 = 4/12 and 1/2 = 6/12, 5/12 lies precisely halfway between them."
            }
        ]
    },
    {
        "id": 6,
        "title": "Finding n Rational Numbers Between a and b",
        "subtitle": "The Common Denominator Algorithm & Step-Size Method (d = (b - a)/(n + 1))",
        "narration": "In school examinations, you will frequently be asked to find five, six, or more rational numbers between two given numbers. We can use two systematic algorithms: the Common Denominator Method where we multiply by n plus 1, or the Step-Size Formula d equals b minus a divided by n plus 1. Both produce distinct, equally spaced rational numbers.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>To find $n$ rational numbers between two given rational numbers $a$ and $b$ ($a < b$), mathematicians use two standard computational algorithms:</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-sky-400">Method 1: Equal Step-Size Algorithm ($d = \\frac{b - a}{n + 1}$)</h4>
                <p>This method spaces all $n$ numbers uniformly like markers on a ruler:</p>
                <div class="py-1 text-center font-mono text-sky-300 text-sm">
                    $d = \\frac{b - a}{n + 1}$
                </div>
                <p>The $n$ required rational numbers are generated sequentially by:</p>
                <div class="py-1 text-center font-mono text-slate-200">
                    $a + d, \\quad a + 2d, \\quad a + 3d, \\quad \\dots, \\quad a + nd$
                </div>
                <p class="text-[11px] text-slate-400">Example: Find $5$ rationals between $1$ and $2$. Here $n = 5$, $d = \\frac{2 - 1}{5 + 1} = \\frac{1}{6}$. The numbers are $1+\\frac{1}{6}=\\frac{7}{6}, \\frac{8}{6}, \\frac{9}{6}, \\frac{10}{6}, \\frac{11}{6}$.</p>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-emerald-400">Method 2: Common Denominator Scaler (Multiply by $(n + 1)$)</h4>
                <ol class="list-decimal list-inside space-y-1">
                    <li>Ensure both numbers have a common denominator $D$.</li>
                    <li>If the gap between numerators is smaller than $n$, multiply both numerator and denominator by $(n + 1)$ (or $10, 100$).</li>
                    <li>Pick the consecutive numerators in between.</li>
                </ol>
                <p class="text-[11px] text-slate-400">Example: Find $5$ rationals between $\\frac{3}{5}$ and $\\frac{4}{5}$. Multiply by $5 + 1 = 6$: $\\frac{3 \\times 6}{5 \\times 6} = \\frac{18}{30}$ and $\\frac{4 \\times 6}{5 \\times 6} = \\frac{24}{30}$. The numbers are $\\frac{19}{30}, \\frac{20}{30}, \\frac{21}{30}, \\frac{22}{30}, \\frac{23}{30}$.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "To find 5 rational numbers between 3/5 and 4/5 using the scaler method, by what factor should we multiply numerator and denominator?",
                "options": [
                    "By 2",
                    "By 3",
                    "By at least (5 + 1) = 6 (or any larger integer like 10)",
                    "By 5/5"
                ],
                "ans": 2,
                "explanation": "Multiplying by n+1 = 6 scales 3/5 to 18/30 and 4/5 to 24/30, creating a gap of exactly 5 integers (19, 20, 21, 22, 23) in the numerator."
            },
            {
                "question": "Using d = (b - a)/(n + 1), what is the step size d to insert 4 rational numbers between 2 and 3?",
                "options": [
                    "d = 1/4",
                    "d = 1/5 = 0.2",
                    "d = 1/6",
                    "d = 5"
                ],
                "ans": 1,
                "explanation": "Here a = 2, b = 3, and n = 4. Therefore, d = (3 - 2)/(4 + 1) = 1/5 = 0.2. The numbers are 2.2, 2.4, 2.6, 2.8."
            }
        ]
    },
    {
        "id": 7,
        "title": "Decimal Expansions: Terminating Decimals",
        "subtitle": "Long Division Remainder Analysis & The Prime Factorisation Theorem ($q = 2^m 5^n$)",
        "narration": "Every rational number has a decimal expansion that either terminates or repeats periodically. A decimal terminates when the remainder in long division becomes zero after a finite number of steps. There is a beautiful theorem in number theory: a rational number in simplest form terminates if and only if the prime factorisation of its denominator q contains only powers of 2, powers of 5, or both.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>When we divide the numerator $p$ by the denominator $q$ using standard long division, two distinct cases can occur with the sequence of remainders:</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Case 1: The Remainder Becomes Zero (Terminating Decimals)</h4>
                <p>After a finite number of division steps, the remainder becomes zero. The decimal expansion stops (terminates).</p>
                <div class="grid grid-cols-3 gap-2 my-2 text-center font-mono text-xs">
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{7}{8} = 0.875$</div>
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{1}{2} = 0.5$</div>
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{639}{250} = 2.556$</div>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-emerald-400">The Fundamental Denominator Factorisation Theorem:</h4>
                <p>Let $x = \\frac{p}{q}$ be a rational number in simplest form ($\\gcd(p, q) = 1$). Then $x$ has a <strong>terminating decimal expansion</strong> if and only if the prime factorisation of $q$ is of the form:</p>
                <div class="py-1 text-center font-mono text-emerald-300 text-base font-bold">
                    $q = 2^m \\times 5^n, \\quad \\text{where } m, n \\in \\mathbb{W} \\text{ (non-negative integers)}$
                </div>
                <p class="text-[11px] text-slate-400"><strong>Why?</strong> Because our number system is base 10, and $10 = 2 \\times 5$. Any terminating fraction can be converted into an equivalent fraction with a power of 10 in the denominator: $\\frac{p}{2^m 5^n} = \\frac{p \\cdot 2^{n} 5^m}{10^{\\max(m,n)}}$.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following rational numbers has a terminating decimal expansion?",
                "options": [
                    "7/75 (since 75 = 3 × 5²)",
                    "13/80 (since 80 = 2⁴ × 5)",
                    "5/14 (since 14 = 2 × 7)",
                    "1/6 (since 6 = 2 × 3)"
                ],
                "ans": 1,
                "explanation": "For 13/80, 80 = 2⁴ × 5¹. Its prime factors contain only 2 and 5. Hence, 13/80 = 0.1625, which terminates after 4 decimal places."
            },
            {
                "question": "How many decimal places will the expansion of 23 / (2³ × 5²) terminate after?",
                "options": [
                    "2 decimal places",
                    "3 decimal places",
                    "5 decimal places",
                    "It will not terminate"
                ],
                "ans": 1,
                "explanation": "The number of terminating decimal places equals max(m, n) = max(3, 2) = 3 decimal places. Indeed, 23/(8 × 25) = 23/200 = 0.115."
            }
        ]
    },
    {
        "id": 8,
        "title": "Non-Terminating Recurring Decimals",
        "subtitle": "Pigeonhole Principle in Division, Period Length, and Repetend Notation",
        "narration": "When the remainder never becomes zero, what happens? Because the divisor is q, the only possible remainders are 1, 2, up to q minus 1. By the Pigeonhole Principle, after at most q minus 1 steps, a remainder MUST repeat. Once a remainder repeats, the entire quotient cycle repeats forever! This produces a non-terminating recurring decimal.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-purple-500/30">
                <h4 class="font-bold text-purple-400 text-sm mb-1">Case 2: The Remainder Never Becomes Zero (Repeating Decimals)</h4>
                <p>If the remainder never reaches zero, a repeating pattern of remainders emerges. This yields a <strong>non-terminating recurring (repeating)</strong> decimal expansion.</p>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 my-2 text-center font-mono text-xs">
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{1}{3} = 0.333\\dots = 0.\\bar{3}$</div>
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{1}{7} = 0.\\overline{142857}$</div>
                    <div class="p-2 bg-slate-950 rounded border border-slate-800">$\\frac{7}{11} = 0.\\overline{63}$</div>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-sky-400">Mathematical Terminology:</h4>
                <ul class="list-disc list-inside space-y-1.5 text-slate-300">
                    <li><strong>Period:</strong> The repeating block of digits. For $0.\\overline{142857}$, the period is $142857$.</li>
                    <li><strong>Periodicity / Length of Period:</strong> The number of digits in the repeating block. For $1/7$, periodicity is $6$. For $1/3$, periodicity is $1$.</li>
                    <li><strong>Repetend / Vinculum Bar:</strong> A horizontal line drawn over the repeating block: $0.\\bar{6}$ means $0.6666\\dots$.</li>
                </ul>
            </div>

            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h5 class="font-bold text-indigo-300 mb-1">The Pigeonhole Principle Constraint:</h5>
                <p>When dividing by an integer $q$, the only possible non-zero remainders are $\{1, 2, 3, \\dots, q - 1\}$. There are at most $q - 1$ distinct remainders. Therefore, <em>the repeating block of digits in $\\frac{p}{q}$ can never have more than $(q - 1)$ digits!</em> For example, $1/7$ has a period of at most $7 - 1 = 6$ digits.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the maximum possible number of repeating digits in the period of 1/17?",
                "options": [
                    "17 digits",
                    "16 digits",
                    "8 digits",
                    "Infinite digits"
                ],
                "ans": 1,
                "explanation": "When dividing by q = 17, the only possible remainders are 1, 2, ..., 16 (16 distinct remainders). Thus, the period length can be at most q - 1 = 16 digits."
            },
            {
                "question": "What is the periodicity (length of the repeating cycle) of the fraction 1/7 = 0.142857142857...?",
                "options": [
                    "4",
                    "5",
                    "6",
                    "7"
                ],
                "ans": 2,
                "explanation": "The repeating block consists of the 6 digits '142857'. Hence, its periodicity is 6."
            }
        ]
    },
    {
        "id": 9,
        "title": "Converting Recurring Decimals to p/q Form",
        "subtitle": "Step-by-Step Algebraic Algorithm: The 10^k Scaling & Subtraction Technique",
        "narration": "Since all recurring decimals represent rational numbers, we must be able to convert any repeating decimal back into p over q form. We use an elegant algebraic algorithm. We define x as the recurring decimal, multiply x by ten to the power of k where k is the number of repeating digits, and subtract the original equation. The infinite repeating tails cancel out perfectly!",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Every recurring decimal can be converted back to an exact rational fraction $\\frac{p}{q}$. Here is the step-by-step universal algorithm:</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Universal Algebraic Conversion Algorithm:</h4>
                <ol class="list-decimal list-inside space-y-1.5 text-slate-300">
                    <li><strong>Step 1:</strong> Let $x$ equal the given decimal: $x = 0.\\overline{a_1 a_2 \\dots a_k} \\quad \\text{--- (Equation 1)}$.</li>
                    <li><strong>Step 2:</strong> Count the number of repeating digits ($k$).</li>
                    <li><strong>Step 3:</strong> Multiply Equation (1) by $10^k$ to shift one full period to the left of the decimal point:
                        <p class="font-mono text-center text-amber-300 my-1">$10^k x = a_1 a_2 \\dots a_k . \\overline{a_1 a_2 \\dots a_k} \\quad \\text{--- (Equation 2)}$</p>
                    </li>
                    <li><strong>Step 4:</strong> Subtract Equation (1) from Equation (2). The infinite tails cancel:
                        <p class="font-mono text-center text-emerald-300 my-1">$(10^k - 1) x = a_1 a_2 \\dots a_k$</p>
                    </li>
                    <li><strong>Step 5:</strong> Solve for $x$ and reduce to simplest co-prime form: $x = \\frac{a_1 a_2 \\dots a_k}{10^k - 1}$.</li>
                </ol>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Example A (Pure Recurring): $0.\\bar{3}$</h5>
                    <p>Let $x = 0.3333\\dots$<br>
                    $10x = 3.3333\\dots$<br>
                    Subtract: $10x - x = 3 \\implies 9x = 3 \\implies x = 3/9 = \\mathbf{1/3}$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-rose-400 mb-1">Example B (Mixed Recurring): $0.2\\bar{7}$</h5>
                    <p>Let $x = 0.2777\\dots$<br>
                    $10x = 2.777\\dots$ and $100x = 27.777\\dots$<br>
                    Subtract: $100x - 10x = 25 \\implies 90x = 25 \\implies x = 25/90 = \\mathbf{5/18}$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the rational p/q representation of 0.474747... (0.47 with bar over 47)?",
                "options": [
                    "47/100",
                    "47/99",
                    "47/90",
                    "43/90"
                ],
                "ans": 1,
                "explanation": "Let x = 0.4747... Since 2 digits repeat, 100x = 47.4747... Subtracting gives 99x = 47 => x = 47/99."
            },
            {
                "question": "Convert the mixed recurring decimal 0.235 (with bar over 35 only) into p/q form:",
                "options": [
                    "235/999",
                    "233/990",
                    "233/900",
                    "235/990"
                ],
                "ans": 1,
                "explanation": "Let x = 0.23535... Then 10x = 2.3535... and 1000x = 235.3535... Subtracting gives 1000x - 10x = 235 - 2 => 990x = 233 => x = 233/990."
            }
        ]
    },
    {
        "id": 10,
        "title": "Introduction to Irrational Numbers",
        "subtitle": "Non-Terminating Non-Recurring Decimals, Hippasus & The Pythagorean Crisis",
        "narration": "Around 400 BCE, the followers of Pythagoras believed that every quantity in nature could be expressed as a ratio of whole numbers. However, when a philosopher named Hippasus calculated the diagonal of a unit square, he discovered a number that CANNOT be written as p over q: the square root of two! This was the birth of Irrational numbers. In decimal form, irrational numbers are non-terminating and non-recurring.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-rose-500/30">
                <h4 class="font-bold text-rose-400 text-sm mb-1">Formal Definition of Irrational Numbers ($\mathbb{I}$ or $\mathbb{R} \setminus \mathbb{Q}$):</h4>
                <p>A real number $s$ is called <strong>Irrational</strong> if it <em>cannot</em> be written in the form $\\frac{p}{q}$, where $p$ and $q$ are integers and $q \\neq 0$.</p>
                <div class="py-1 text-center font-mono text-rose-300 text-xs">
                    Decimal Characterisation: <strong>Non-Terminating and Non-Recurring</strong>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-amber-400 mb-1">Famous Examples:</h5>
                    <ul class="list-disc list-inside space-y-1 text-slate-300">
                        <li>$\\sqrt{2} = 1.41421356237\\dots$ (Never repeats, never ends)</li>
                        <li>$\\sqrt{3} = 1.73205080756\\dots$</li>
                        <li>$\\pi = 3.141592653589793\\dots$</li>
                        <li>$0.101001000100001\\dots$ (Constructed pattern)</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">The $\\pi$ vs $\\frac{22}{7}$ Distinction:</h5>
                    <p>$\\pi$ is irrational because its exact circumference-to-diameter ratio cannot be expressed as a ratio of integers. The fraction $\\frac{22}{7} = 3.\\overline{142857}$ is a <em>rational approximation</em> used for practical arithmetic, but $\\pi \\neq \\frac{22}{7}$.</p>
                </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <h5 class="font-bold text-emerald-400 mb-1">The Real Number Continuum ($\mathbb{R}$):</h5>
                <p>The set of all Rational numbers and Irrational numbers taken together forms the complete set of <strong>Real Numbers ($\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$)</strong>. Every real number corresponds to a unique point on the number line, and every point represents a unique real number (The Cantor-Dedekind Axiom).</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following numbers is an IRRATIONAL number?",
                "options": [
                    "0.232323... (non-terminating recurring)",
                    "√25",
                    "0.101001000100001... (non-terminating non-recurring)",
                    "22/7"
                ],
                "ans": 2,
                "explanation": "0.1010010001... is non-terminating and non-recurring (the number of zeros increases each time, preventing any finite repeating cycle). Hence it is irrational. √25 = 5 (rational), 22/7 is rational, and 0.23... is rational."
            },
            {
                "question": "Is the number π equal to 22/7?",
                "options": [
                    "Yes, they are identical",
                    "No, π is irrational while 22/7 is a rational approximation",
                    "Yes, because both terminate after 2 decimal places",
                    "No, 22/7 is irrational while π is rational"
                ],
                "ans": 1,
                "explanation": "π is an irrational number (non-terminating, non-recurring), whereas 22/7 is a rational number (22/7 = 3.142857...). 22/7 is only an approximate value used for calculations."
            }
        ]
    },
    {
        "id": 11,
        "title": "Rigorous Proof of Irrationality of √2",
        "subtitle": "Proof by Contradiction, Euclid's Divisibility Lemma, and Parity Argument",
        "narration": "One of the crowned jewels of ancient mathematics is the proof that the square root of two is irrational. We use Proof by Contradiction. We assume the opposite: suppose root two is rational and can be written as a over b in simplest co-prime form. Through algebraic squaring, we discover that both a and b must be even numbers. But if both are even, they share a common factor of two! This contradicts our assumption that they are co-prime.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Theorem: $\\sqrt{2}$ is an Irrational Number.</h4>
                <p>We prove this using <strong>Reductio ad Absurdum (Proof by Contradiction)</strong>.</p>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2.5 font-mono text-[11px]">
                <p><strong class="text-sky-300">Assumption:</strong> Assume to the contrary that $\\sqrt{2}$ is rational. Then there exist integers $a$ and $b$ ($b \\neq 0$) such that:</p>
                <div class="text-center text-amber-300 font-bold text-xs py-1">
                    $\\sqrt{2} = \\frac{a}{b}, \\quad \\text{where } a, b \\in \\mathbb{Z} \\text{ and } \\gcd(a, b) = 1 \\text{ (co-prime)}$
                </div>

                <p><strong class="text-sky-300">Step 1:</strong> Square both sides:</p>
                <div class="text-center text-slate-200">
                    $2 = \\frac{a^2}{b^2} \\implies a^2 = 2b^2 \\quad \\text{--- (Equation 1)}$
                </div>
                <p class="text-slate-400">Since $2$ divides $2b^2$, it follows that $2$ divides $a^2$. By Euclid's Lemma, if a prime divides $a^2$, it must divide $a$. Thus, <strong>$a$ is an even integer</strong>.</p>

                <p><strong class="text-sky-300">Step 2:</strong> Since $a$ is even, we can write $a = 2k$ for some integer $k$. Substitute $a = 2k$ into Equation (1):</p>
                <div class="text-center text-slate-200">
                    $(2k)^2 = 2b^2 \\implies 4k^2 = 2b^2 \\implies b^2 = 2k^2 \\quad \\text{--- (Equation 2)}$
                </div>
                <p class="text-slate-400">This means $2$ divides $b^2$, which implies <strong>$b$ is also an even integer</strong>.</p>

                <p><strong class="text-rose-400 font-bold">Step 3 (The Contradiction):</strong></p>
                <p class="text-rose-300">Both $a$ and $b$ are even, which means they have at least $2$ as a common factor. This directly contradicts our foundational premise that $\\gcd(a, b) = 1$ (co-prime)!</p>

                <p><strong class="text-emerald-400 font-bold">Conclusion:</strong> Our initial assumption that $\\sqrt{2}$ is rational must be false. Therefore, $\\mathbf{\\sqrt{2}}$ <strong>is irrational</strong>. Q.E.D.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "In the proof of irrationality of √2, what critical contradiction is reached?",
                "options": [
                    "That 2 equals 4",
                    "That both a and b are even (sharing a factor of 2), contradicting that a and b are co-prime",
                    "That b is equal to zero",
                    "That square roots do not exist"
                ],
                "ans": 1,
                "explanation": "Starting from gcd(a,b)=1, we proved that 2 divides a and 2 divides b. This means 2 is a common factor, directly contradicting the assumption that a and b are co-prime."
            },
            {
                "question": "Which foundational theorem states: 'If a prime number p divides a², then p divides a'?",
                "options": [
                    "Pythagorean Theorem",
                    "Euclid's Lemma / Fundamental Theorem of Arithmetic",
                    "Newton's Binomial Theorem",
                    "Ramanujan's Partition Formula"
                ],
                "ans": 1,
                "explanation": "Euclid's Divisibility Lemma (corollary of Fundamental Theorem of Arithmetic) guarantees that if a prime p divides a², it must divide a."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rigorous Proof of Irrationality of √3",
        "subtitle": "Modulo Arithmetic, Divisibility by 3, and Generalisation to Non-Square Primes",
        "narration": "In the same manner, we can prove that root three is irrational. If root three were equal to a over b, then three times b squared equals a squared. This proves that three divides a. Substituting a equals three k shows that three also divides b. Once again, a and b share a common factor of three, violating co-primality. In fact, the square root of ANY positive integer that is not a perfect square is ALWAYS irrational!",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Theorem: $\\sqrt{3}$ is an Irrational Number.</h4>
                <p>We extend the method of contradiction to prime $p = 3$.</p>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2.5 font-mono text-[11px]">
                <p><strong class="text-sky-300">Assumption:</strong> Suppose $\\sqrt{3}$ is rational: $\\sqrt{3} = \\frac{a}{b}$, where $a, b \\in \\mathbb{Z}$, $b \\neq 0$, and $\\gcd(a, b) = 1$.</p>

                <p><strong class="text-sky-300">Step 1:</strong> Squaring both sides yields:</p>
                <div class="text-center text-slate-200">
                    $3 = \\frac{a^2}{b^2} \\implies a^2 = 3b^2 \\quad \\text{--- (Equation 1)}$
                </div>
                <p class="text-slate-400">Thus $3$ divides $a^2$. Since $3$ is prime, <strong>$3$ divides $a$</strong> ($a$ is a multiple of $3$).</p>

                <p><strong class="text-sky-300">Step 2:</strong> Substitute $a = 3m$ ($m \\in \\mathbb{Z}$) into Equation (1):</p>
                <div class="text-center text-slate-200">
                    $(3m)^2 = 3b^2 \\implies 9m^2 = 3b^2 \\implies b^2 = 3m^2 \\quad \\text{--- (Equation 2)}$
                </div>
                <p class="text-slate-400">Thus $3$ divides $b^2$, which implies <strong>$3$ divides $b$</strong>.</p>

                <p><strong class="text-rose-400 font-bold">Step 3 (Contradiction & Conclusion):</strong></p>
                <p class="text-rose-300">Both $a$ and $b$ are multiples of $3$, contradicting that $\\gcd(a, b) = 1$. Thus, $\\mathbf{\\sqrt{3}}$ <strong>is irrational</strong>.</p>
            </div>

            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h5 class="font-bold text-indigo-300 mb-1">Generalised Principle for Square Roots:</h5>
                <p>For any positive integer $n$:</p>
                <div class="py-1 text-center font-mono text-emerald-300 text-xs">
                    $\\sqrt{n} \\text{ is Rational } \\iff n \\text{ is a Perfect Square } (1, 4, 9, 16, 25, \\dots)
                </div>
                <p class="text-[11px] text-slate-400">If $n$ is not a perfect square (such as $2, 3, 5, 6, 7, 8, 10, 11$), then $\\sqrt{n}$ is <strong>strictly irrational</strong>.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following square roots is a RATIONAL number?",
                "options": [
                    "√7",
                    "√15",
                    "√81",
                    "√20"
                ],
                "ans": 2,
                "explanation": "81 is a perfect square: 81 = 9². Hence √81 = 9 = 9/1, which is a rational number. 7, 15, and 20 are not perfect squares, so their square roots are irrational."
            },
            {
                "question": "In the proof for √3, if a² = 3b², what substitution do we make for a?",
                "options": [
                    "a = 2k",
                    "a = 3m where m is an integer",
                    "a = b + 3",
                    "a = 9m"
                ],
                "ans": 1,
                "explanation": "Since 3 divides a², 3 must divide a. Therefore a is a multiple of 3, so we substitute a = 3m."
            }
        ]
    },
    {
        "id": 13,
        "title": "Plotting Irrational Numbers on the Number Line",
        "subtitle": "Pythagorean Theorem Construction: Locating √2, √3, and √5 with Compass & Ruler",
        "narration": "How can we pinpoint the exact position of an irrational number on a number line if its decimal never ends? We use geometry! By applying the Pythagorean Theorem, a right-angled triangle with base of 1 unit and perpendicular height of 1 unit has a hypotenuse of root 2. Using a compass with its needle at zero and pencil at the hypotenuse, we swing an arc down to the number line to plot the exact point root 2.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>The Pythagorean Theorem provides the bridge connecting irrational square roots to Euclidean geometry: in any right triangle with legs $a$ and $b$, the hypotenuse $c$ satisfies $c = \\sqrt{a^2 + b^2}$.</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Step-by-Step Construction for $\\sqrt{2}$:</h4>
                <ol class="list-decimal list-inside space-y-1.5 text-slate-300">
                    <li><strong>Step 1:</strong> On the number line, mark origin $O(0)$ and point $A(1)$. The length $OA = 1$ unit.</li>
                    <li><strong>Step 2:</strong> At $A$, construct a perpendicular segment $AB = 1$ unit, perpendicular to the number line ($AB \\perp OA$).</li>
                    <li><strong>Step 3:</strong> Join $OB$. By Pythagoras Theorem in right $\\triangle OAB$:
                        <p class="font-mono text-center text-amber-300 my-1">$OB = \\sqrt{OA^2 + AB^2} = \\sqrt{1^2 + 1^2} = \\sqrt{2} \\approx 1.414$</p>
                    </li>
                    <li><strong>Step 4:</strong> Using a compass centered at $O(0)$ with radius $OB = \\sqrt{2}$, draw an arc intersecting the number line at point $P$. The point $P$ represents $\\mathbf{\\sqrt{2}}$.</li>
                </ol>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Constructing $\\sqrt{3}$ from $\\sqrt{2}$:</h5>
                    <p>At point $B$ on hypotenuse $OB$ (length $\\sqrt{2}$), erect a perpendicular of length $1$ unit to point $C$. The new hypotenuse is $OC = \\sqrt{(\\sqrt{2})^2 + 1^2} = \\sqrt{2 + 1} = \\sqrt{3} \\approx 1.732$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-emerald-400 mb-1">Direct Construction for $\\sqrt{5}$:</h5>
                    <p>Take base $OA = 2$ units and vertical height $AB = 1$ unit. Then hypotenuse $OB = \\sqrt{2^2 + 1^2} = \\sqrt{4 + 1} = \\sqrt{5} \\approx 2.236$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "To construct √5 directly on the number line in a single right-angled triangle, what base and perpendicular lengths should be chosen?",
                "options": [
                    "Base = 1, Perpendicular = 1",
                    "Base = 2, Perpendicular = 1 (since 2² + 1² = 5)",
                    "Base = 3, Perpendicular = 2",
                    "Base = 5, Perpendicular = 5"
                ],
                "ans": 1,
                "explanation": "Using base = 2 and height = 1, hypotenuse = √(2² + 1²) = √(4 + 1) = √5."
            },
            {
                "question": "What is the role of the compass in plotting √2 on the number line?",
                "options": [
                    "To measure the temperature of the paper",
                    "To transfer the exact hypotenuse length from the triangle down onto the horizontal number line",
                    "To divide the number line into 10 equal parts",
                    "To draw a square of area 4"
                ],
                "ans": 1,
                "explanation": "The compass takes the radial distance OB = √2 from origin O and swings an arc to cut the horizontal number line at point P, transferring the distance accurately."
            }
        ]
    },
    {
        "id": 14,
        "title": "The Square Root Spiral (Theodorus Spiral)",
        "subtitle": "Algorithmic Iteration: Chaining Hypotenuse √n with Unit Perpendiculars",
        "narration": "The Greek philosopher Theodorus of Cyrene created a breathtaking geometric construction known as the Square Root Spiral. Starting with an isosceles right triangle of legs 1 and 1, the hypotenuse is root 2. At its tip, we attach another perpendicular of 1 unit to produce root 3, then root 4, root 5, and so on. As you continue, it coils like a nautilus seashell, visualizing all square roots sequentially.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-cyan-500/30">
                <h4 class="font-bold text-cyan-400 text-sm mb-1">The Theodorus Recursive Algorithm:</h4>
                <p>The Square Root Spiral is an algorithmic sequence of contiguous right-angled triangles sharing a common vertex at the origin $O$:</p>
                <div class="py-1 text-center font-mono text-cyan-300 text-xs font-bold">
                    $H_{n+1} = \\sqrt{(H_n)^2 + 1^2} = \\sqrt{n + 1}$
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Recursive Step-by-Step Construction:</h4>
                <ul class="list-disc list-inside space-y-1 text-slate-300 font-mono text-[11px]">
                    <li><strong>Triangle 1:</strong> Base $1$, Height $1 \\implies \\text{Hypotenuse } H_1 = \\sqrt{1^2 + 1^2} = \\mathbf{\\sqrt{2}}$.</li>
                    <li><strong>Triangle 2:</strong> Base $\\sqrt{2}$, Height $1 \\implies \\text{Hypotenuse } H_2 = \\sqrt{(\\sqrt{2})^2 + 1^2} = \\mathbf{\\sqrt{3}}$.</li>
                    <li><strong>Triangle 3:</strong> Base $\\sqrt{3}$, Height $1 \\implies \\text{Hypotenuse } H_3 = \\sqrt{(\\sqrt{3})^2 + 1^2} = \\sqrt{4} = \\mathbf{2}$.</li>
                    <li><strong>Triangle 4:</strong> Base $\\sqrt{4} = 2$, Height $1 \\implies \\text{Hypotenuse } H_4 = \\sqrt{2^2 + 1^2} = \\mathbf{\\sqrt{5}}$.</li>
                    <li><strong>Triangle $n$:</strong> Base $\\sqrt{n}$, Height $1 \\implies \\text{Hypotenuse } H_n = \\mathbf{\\sqrt{n + 1}}$.</li>
                </ul>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <h5 class="font-bold text-emerald-400 mb-1">Historical Milestone:</h5>
                <p>Theodorus constructed this spiral up to $\\sqrt{17}$, where the 16th triangle completes almost a full $360^\\circ$ rotation without overlapping the starting segment. It vividly proves that every square root $\\sqrt{n}$ is a constructible Euclidean segment!</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "In the square root spiral, if the base of a right triangle is √6 and the perpendicular is 1, what is the length of its hypotenuse?",
                "options": [
                    "√5",
                    "√7",
                    "7",
                    "√37"
                ],
                "ans": 1,
                "explanation": "Hypotenuse = √((√6)² + 1²) = √(6 + 1) = √7."
            },
            {
                "question": "At which square root did Theodorus historically halt his spiral construction because it completed nearly a full revolution?",
                "options": [
                    "√2",
                    "√10",
                    "√17",
                    "√100"
                ],
                "ans": 2,
                "explanation": "Plato recorded in his dialogue 'Theaetetus' that Theodorus constructed the spiral up to √17."
            }
        ]
    },
    {
        "id": 15,
        "title": "Operations on Real Numbers & Rationalisation",
        "subtitle": "Arithmetic Properties, Radical Identities & Conjugate Denominator Elimination",
        "narration": "What happens when you add, subtract, multiply, or divide rational and irrational numbers? The sum or product of a non-zero rational with an irrational is always irrational. However, operating on two irrational numbers can produce a rational result! When working with fractions containing square roots in the denominator, we perform Rationalisation using algebraic conjugates.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Rules of Mixed Arithmetic Operations:</h4>
                <ul class="list-disc list-inside space-y-1 text-slate-300">
                    <li><strong>Rational + Irrational = Irrational:</strong> $2 + \\sqrt{3}$ is irrational.</li>
                    <li><strong>Non-zero Rational $\\times$ Irrational = Irrational:</strong> $5\\sqrt{2}$ is irrational.</li>
                    <li><strong>Irrational $\\pm / \\times / \\div$ Irrational:</strong> Can be rational or irrational!
                        <p class="text-[11px] text-slate-400 ml-4 font-mono">$\\sqrt{2} \\times \\sqrt{2} = 2$ (Rational), but $\\sqrt{2} \\times \\sqrt{3} = \\sqrt{6}$ (Irrational).</p>
                    </li>
                </ul>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-emerald-500/30 space-y-2">
                <h4 class="font-bold text-emerald-400">Rationalising the Denominator:</h4>
                <p>Standard mathematical convention requires removing square roots from denominators because division by an irrational decimal is computationally inefficient.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2 mt-2">
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                        <span class="font-bold text-sky-300">Type 1 (Monomial): $\\frac{1}{\\sqrt{a}}$</span>
                        <p class="mt-1">Multiply numerator & denominator by $\\sqrt{a}$:</p>
                        <p class="font-mono text-center text-amber-300">$\\frac{1}{\\sqrt{a}} \\times \\frac{\\sqrt{a}}{\\sqrt{a}} = \\frac{\\sqrt{a}}{a}$</p>
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                        <span class="font-bold text-sky-300">Type 2 (Binomial Conjugate): $\\frac{1}{a + \\sqrt{b}}$</span>
                        <p class="mt-1">Multiply by the conjugate $(a - \\sqrt{b})$ using difference of squares $(x+y)(x-y) = x^2 - y^2$:</p>
                        <p class="font-mono text-center text-amber-300">$\\frac{1}{a + \\sqrt{b}} \\times \\frac{a - \\sqrt{b}}{a - \\sqrt{b}} = \\frac{a - \\sqrt{b}}{a^2 - b}$</p>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the rationalised form of the expression 1 / (√7 - 2)?",
                "options": [
                    "(√7 + 2) / 3",
                    "(√7 - 2) / 5",
                    "(√7 + 2) / 5",
                    "√7 / 2"
                ],
                "ans": 0,
                "explanation": "Multiply numerator and denominator by conjugate (√7 + 2): 1/(√7 - 2) × (√7 + 2)/(√7 + 2) = (√7 + 2)/((√7)² - 2²) = (√7 + 2)/(7 - 4) = (√7 + 2)/3."
            },
            {
                "question": "Which of the following operations on two irrational numbers results in a RATIONAL number?",
                "options": [
                    "√2 + √3",
                    "(3 + √5) + (3 - √5)",
                    "√2 × √5",
                    "√10 / √2"
                ],
                "ans": 1,
                "explanation": "(3 + √5) + (3 - √5) = 3 + 3 + (√5 - √5) = 6 = 6/1, which is a rational number!"
            }
        ]
    },
    {
        "id": 16,
        "title": "Laws of Exponents for Real Numbers",
        "subtitle": "Index Laws, Fractional Exponents (a^(p/q) = q√a^p), and Algorithmic Thinking",
        "narration": "In our final content slide, we consolidate the Laws of Exponents for positive real bases. Whether exponents are integers, fractions, or negative numbers, the fundamental laws of powers remain invariant. We also establish computational thinking skills: recognizing that calculating cube roots and fractional exponents follows deterministic algebraic algorithms.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Let $a, b > 0$ be real bases and $p, q, m, n \\in \\mathbb{Q}$ be rational exponents. The universal laws of exponents are:</p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="font-bold text-amber-400">1. Product with Same Base:</span>
                    <p class="font-mono text-center text-sm text-amber-300 my-1">$a^m \\cdot a^n = a^{m + n}$</p>
                    <p class="text-[10px] text-slate-400">Example: $2^{2/3} \\cdot 2^{1/3} = 2^{2/3 + 1/3} = 2^1 = 2$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="font-bold text-sky-400">2. Quotient with Same Base:</span>
                    <p class="font-mono text-center text-sm text-sky-300 my-1">$\\frac{a^m}{a^n} = a^{m - n}$</p>
                    <p class="text-[10px] text-slate-400">Example: $7^{1/5} / 7^{1/3} = 7^{1/5 - 1/3} = 7^{-2/15}$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="font-bold text-emerald-400">3. Power of a Power:</span>
                    <p class="font-mono text-center text-sm text-emerald-300 my-1">$(a^m)^n = a^{m \\cdot n}$</p>
                    <p class="text-[10px] text-slate-400">Example: $(3^{1/4})^4 = 3^{(1/4 \\times 4)} = 3^1 = 3$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="font-bold text-purple-400">4. Different Base, Same Exponent:</span>
                    <p class="font-mono text-center text-sm text-purple-300 my-1">$a^m \\cdot b^m = (ab)^m$</p>
                    <p class="text-[10px] text-slate-400">Example: $13^{1/5} \\cdot 17^{1/5} = (13 \\times 17)^{1/5} = 221^{1/5}$.</p>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Definition of Fractional Exponents (Radicals):</h4>
                <div class="py-1 text-center font-mono text-amber-300 text-sm">
                    $a^{m/n} = (\\sqrt[n]{a})^m = \\sqrt[n]{a^m}, \\quad a^{-m/n} = \\frac{1}{a^{m/n}}$
                </div>
                <p class="text-[11px] text-slate-400 mt-1">Example: Evaluate $64^{1/2} = \\sqrt{64} = 8$, and $32^{2/5} = (\\sqrt[5]{32})^2 = 2^2 = 4$.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the evaluated numerical value of 125^(-1/3)?",
                "options": [
                    "5",
                    "-5",
                    "1/5 = 0.2",
                    "1/25"
                ],
                "ans": 2,
                "explanation": "125 = 5³. Therefore 125^(-1/3) = (5³)^(-1/3) = 5^(3 × -1/3) = 5^(-1) = 1/5 = 0.2."
            },
            {
                "question": "Simplify: 11^(1/2) / 11^(1/4):",
                "options": [
                    "11^(1/2)",
                    "11^(1/4)",
                    "11^(3/4)",
                    "11^2"
                ],
                "ans": 1,
                "explanation": "Using quotient rule a^m / a^n = a^(m - n): 11^(1/2 - 1/4) = 11^(2/4 - 1/4) = 11^(1/4)."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Quiz Challenge • Part 1",
        "subtitle": "Rational Numbers, Number Line Representation & Density Concepts",
        "questions": [
            {
                "id": 1,
                "q": "Which of the following numbers can be expressed in the form p/q where p and q are integers and q ≠ 0?",
                "options": ["√2", "π", "0.75", "1.010010001..."],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> 0.75 is a terminating decimal and can be expressed as 75/100 = 3/4, where p = 3 and q = 4 are integers with q ≠ 0. Hence it is rational. √2, π, and 1.010010001... are all irrational."
            },
            {
                "id": 2,
                "q": "Which statement best describes the density of rational numbers?",
                "options": [
                    "There are no numbers between two consecutive integers",
                    "Between any two rational numbers, there are exactly 10 rational numbers",
                    "Between any two distinct rational numbers, there exist infinitely many rational numbers",
                    "Rational numbers are spaced exactly 1 unit apart"
                ],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> By the Density Theorem, between any two distinct rational numbers a and b, the mean (a+b)/2 produces another rational. Repeating this recursively generates an infinite count of rational numbers."
            },
            {
                "id": 3,
                "q": "Find a rational number lying exactly halfway between 1/4 and 1/3:",
                "options": ["7/24", "2/7", "7/12", "1/7"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Arithmetic mean = (1/4 + 1/3) / 2 = (3/12 + 4/12) / 2 = (7/12) / 2 = 7/24. Since 1/4 = 6/24 and 1/3 = 8/24, 7/24 is exactly halfway."
            },
            {
                "id": 4,
                "q": "What is the additive inverse of -5/9?",
                "options": ["-9/5", "5/9", "9/5", "0"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The additive inverse of a number x is -x such that x + (-x) = 0. For x = -5/9, -(-5/9) = +5/9."
            },
            {
                "id": 5,
                "q": "What is the multiplicative inverse (reciprocal) of -3/8?",
                "options": ["3/8", "-8/3", "8/3", "0"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The multiplicative inverse of a non-zero rational number a/b is b/a such that (a/b) × (b/a) = 1. Reciprocal of -3/8 is -8/3."
            },
            {
                "id": 6,
                "q": "Between which two integers does the improper fraction 17/5 lie on the number line?",
                "options": ["Between 1 and 2", "Between 2 and 3", "Between 3 and 4", "Between 4 and 5"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> 17/5 = 3 + 2/5 = 3.4. It lies between the consecutive integers 3 and 4, at 2/5 of the distance past 3."
            },
            {
                "id": 7,
                "q": "Using the formula d = (b - a)/(n + 1), what step size d inserts 3 rational numbers between 0 and 1?",
                "options": ["d = 1/2", "d = 1/3", "d = 1/4", "d = 1/5"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> Here a = 0, b = 1, and n = 3. d = (1 - 0)/(3 + 1) = 1/4 = 0.25. The numbers are 1/4, 2/4 = 1/2, and 3/4."
            },
            {
                "id": 8,
                "q": "Which property of rational numbers states that a × (b + c) = (a × b) + (a × c)?",
                "options": ["Closure property", "Commutative property", "Associative property", "Distributive property of multiplication over addition"],
                "ans": 3,
                "solution": "<strong>Detailed Solution:</strong> The identity a(b + c) = ab + ac defines the Distributive Property of multiplication over addition."
            },
            {
                "id": 9,
                "q": "Every whole number is a natural number. Is this statement true or false?",
                "options": ["True, because 0 is natural", "False, because 0 is a whole number but not a natural number", "True, because ℕ and 𝕎 are identical", "True for negative integers"],
                "ans": 1,
                "explanation": "",
                "solution": "<strong>Detailed Solution:</strong> False. The set of whole numbers is W = {0, 1, 2, 3, ...} and natural numbers N = {1, 2, 3, ...}. 0 is in W but not in N."
            },
            {
                "id": 10,
                "q": "Why is division by zero undefined in rational arithmetic?",
                "options": [
                    "Because ancient Greek mathematicians banned zero",
                    "Because if p/0 = k, then k × 0 must equal p; if p ≠ 0, no such k exists, and if p = 0, any k works (indeterminate)",
                    "Because zero is not a number",
                    "Because negative fractions cannot be inverted"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Division is inverse multiplication: p/q = k implies p = k × q. If q = 0, then p = k × 0 = 0. If p ≠ 0, this is impossible. If p = 0, k is indeterminate. Therefore, division by zero is strictly undefined."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Quiz Challenge • Part 2",
        "subtitle": "Decimal Expansions, Terminating vs Recurring & p/q Conversion",
        "questions": [
            {
                "id": 11,
                "q": "Under what condition does a simplest rational number p/q have a terminating decimal expansion?",
                "options": [
                    "q has only factors of 3 and 7",
                    "The prime factorisation of q contains only powers of 2 and/or 5 (q = 2^m × 5^n)",
                    "p must be a prime number",
                    "q must be greater than 100"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> A rational number p/q in simplest form terminates if and only if q = 2^m × 5^n for non-negative integers m and n, because our decimal base 10 = 2 × 5."
            },
            {
                "id": 12,
                "q": "Without actual division, determine which of the following fractions has a TERMINATING decimal:",
                "options": ["17/60", "29/343", "7/250", "15/14"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> For 7/250: 250 = 2¹ × 5³. Its prime factors are exclusively 2 and 5! Hence 7/250 terminates: 7/250 = (7 × 4)/(250 × 4) = 28/1000 = 0.028."
            },
            {
                "id": 13,
                "q": "Convert the recurring decimal 0.6666... (0.6 with bar) into its simplest p/q form:",
                "options": ["6/10", "2/3", "3/5", "6/99"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Let x = 0.6666... Multiply by 10: 10x = 6.6666... Subtract: 10x - x = 6 => 9x = 6 => x = 6/9 = 2/3."
            },
            {
                "id": 14,
                "q": "Convert the pure recurring decimal 0.121212... (0.12 with bar) into p/q form:",
                "options": ["12/100", "4/33", "12/90", "1/8"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Let x = 0.1212... Multiply by 10² = 100: 100x = 12.1212... Subtract: 100x - x = 12 => 99x = 12 => x = 12/99 = 4/33."
            },
            {
                "id": 15,
                "q": "Convert the mixed recurring decimal 0.12333... (0.123 with bar over 3 only) into p/q form:",
                "options": ["123/999", "111/900 = 37/300", "123/900", "111/990"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Let x = 0.12333... Multiply by 100: 100x = 12.333... and 1000x = 123.333... Subtract: 1000x - 100x = 123 - 12 => 900x = 111 => x = 111/900 = 37/300."
            },
            {
                "id": 16,
                "q": "What is the recurring decimal expansion of the rational number 1/9?",
                "options": ["0.9", "0.1111... = 0.1 bar", "0.01 bar", "0.0909..."],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> 1 ÷ 9: 1.000 / 9 = 0.1111... with constant remainder 1. In repetend notation, this is 0.1 with bar over 1."
            },
            {
                "id": 17,
                "q": "What is 0.9999... (0.9 with bar) equal to when converted to p/q form?",
                "options": ["0.9", "9/10", "1", "9.9"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> Let x = 0.999... Then 10x = 9.999... Subtracting gives 10x - x = 9 => 9x = 9 => x = 9/9 = 1. Mathematically, 0.999... and 1 are identical representations of the same real number!"
            },
            {
                "id": 18,
                "q": "Why does the fraction 1/7 repeat in cycles of at most 6 digits?",
                "options": [
                    "Because 6 is a perfect number",
                    "Because when dividing by 7, the only possible non-zero remainders are {1, 2, 3, 4, 5, 6} (6 remainders)",
                    "Because 7 is an odd number",
                    "Because base 10 has 10 - 7 = 3 cycles"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> In division by q, the remainders must be strictly less than q. For q = 7, the possible non-zero remainders are 1, 2, 3, 4, 5, 6. By the Pigeonhole Principle, after at most 6 steps, a remainder must recur."
            },
            {
                "id": 19,
                "q": "The decimal expansion of 329 / 400 is:",
                "options": [
                    "Non-terminating recurring",
                    "Terminating after 4 decimal places",
                    "Irrational",
                    "Non-terminating non-recurring"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> 400 = 2⁴ × 5². Since the prime factors are exclusively 2 and 5, it terminates. The number of decimal places is max(4, 2) = 4 places. Indeed, 329/400 = 0.8225."
            },
            {
                "id": 20,
                "q": "Which of the following decimal representations represents a RATIONAL number?",
                "options": [
                    "3.1415926535...",
                    "0.12012001200012...",
                    "2.345345345... (2.345 bar)",
                    "1.41421356..."
                ],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> 2.345345345... is non-terminating but RECURRING with period '345'. Any repeating decimal is rational. The others are non-terminating and non-recurring (irrational)."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Quiz Challenge • Part 3",
        "subtitle": "Irrational Numbers, Proofs of √2 and √3 & Number Line Constructions",
        "questions": [
            {
                "id": 21,
                "q": "Which ancient Greek mathematician is credited with discovering the irrationality of √2?",
                "options": ["Euclid", "Archimedes", "Hippasus of Metapontum", "Thales"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> Hippasus of Metapontum (a Pythagorean philosopher) showed that the diagonal of a unit square cannot be written as a ratio of whole numbers, proving √2 is irrational."
            },
            {
                "id": 22,
                "q": "In the proof by contradiction for the irrationality of √2, we start by assuming that:",
                "options": [
                    "√2 is irrational",
                    "√2 = a/b where a and b are integers with b ≠ 0 and gcd(a, b) = 1 (co-prime)",
                    "√2 is a whole number",
                    "2 is not a prime number"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Proof by contradiction begins by assuming the opposite: that √2 is rational, meaning it can be written as an irreducible fraction a/b where a and b are co-prime integers."
            },
            {
                "id": 23,
                "q": "If 3 divides a², why does 3 also divide a?",
                "options": [
                    "By Euclid's Lemma, because 3 is a prime number",
                    "Because 3 is an odd number",
                    "Because every integer divides its square",
                    "Only when a is a multiple of 9"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> By Euclid's Lemma: If p is a prime number and p divides a², then p must divide a. Since 3 is prime, 3 | a² implies 3 | a."
            },
            {
                "id": 24,
                "q": "What is the length of the hypotenuse of a right triangle with legs of 1 unit and 1 unit?",
                "options": ["1 unit", "2 units", "√2 units", "√3 units"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> By Pythagoras Theorem: c² = 1² + 1² = 1 + 1 = 2 => c = √2 units."
            },
            {
                "id": 25,
                "q": "To construct √3 on the number line using a right-angled triangle, what lengths should be chosen for the base and perpendicular?",
                "options": [
                    "Base = 1, Height = 1",
                    "Base = √2, Height = 1",
                    "Base = 2, Height = 1",
                    "Base = 3, Height = 3"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Hypotenuse = √((√2)² + 1²) = √(2 + 1) = √3. Thus taking base = √2 and height = 1 produces hypotenuse √3."
            },
            {
                "id": 26,
                "q": "Between which two integer marks does √2 ≈ 1.414 lie on the number line?",
                "options": ["Between 0 and 1", "Between 1 and 2", "Between 2 and 3", "Between -1 and 0"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Since 1² = 1 and 2² = 4, and 1 < 2 < 4, taking square roots gives 1 < √2 < 2. Thus √2 lies between 1 and 2."
            },
            {
                "id": 27,
                "q": "What is the 5th hypotenuse in the Theodorus Square Root Spiral if the 1st hypotenuse is √2?",
                "options": ["√4 = 2", "√5", "√6", "√7"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> The hypotenuses generated are: H1 = √2, H2 = √3, H3 = √4 = 2, H4 = √5, H5 = √6. The 5th hypotenuse is √6."
            },
            {
                "id": 28,
                "q": "Is the number 0.12345678910111213... rational or irrational?",
                "options": [
                    "Rational because it follows a pattern",
                    "Irrational because it is non-terminating and non-recurring (Champernowne constant)",
                    "An integer",
                    "Undetermined"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> This is Champernowne's constant (concatenation of natural numbers). Although generated by a systematic rule, it never repeats periodically and never terminates. Hence it is irrational."
            },
            {
                "id": 29,
                "q": "Why is √4 NOT an irrational number?",
                "options": [
                    "Because 4 is an even number",
                    "Because 4 is a perfect square (4 = 2²), so √4 = 2 = 2/1, which is a rational number",
                    "Because Pythagoras proved 4 is rational",
                    "Because it has a vinculum bar"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> 4 is a perfect square. √4 = 2 = 2/1, which satisfies the definition of a rational number p/q with p=2, q=1."
            },
            {
                "id": 30,
                "q": "Which property ensures that every real number has a unique point on the number line and vice versa?",
                "options": [
                    "The Closure Property",
                    "The Commutative Property",
                    "The Cantor-Dedekind Axiom / Completeness of Real Numbers",
                    "The Distributive Law"
                ],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> The Cantor-Dedekind Axiom asserts a one-to-one correspondence between the set of all real numbers and all geometric points on the continuous number line."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Quiz Challenge • Part 4",
        "subtitle": "Operations, Rationalisation & Laws of Exponents for Real Numbers",
        "questions": [
            {
                "id": 31,
                "q": "What is the sum of the rational number 3 and the irrational number √5?",
                "options": [
                    "3√5 (rational)",
                    "3 + √5 (irrational)",
                    "8 (rational)",
                    "√8 (irrational)"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The sum of a rational number and an irrational number is always irrational. Hence 3 + √5 is irrational."
            },
            {
                "id": 32,
                "q": "Rationalise the denominator of 1 / √3:",
                "options": ["√3 / 3", "3 / √3", "1 / 3", "3"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Multiply numerator and denominator by √3: 1/√3 × (√3/√3) = √3 / (√3 × √3) = √3 / 3."
            },
            {
                "id": 33,
                "q": "What is the algebraic conjugate of (5 + 2√3)?",
                "options": ["5 + 2√3", "5 - 2√3", "-5 - 2√3", "2√3 - 5"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The conjugate of a binomial (a + b√c) is obtained by changing the sign of the radical term: (a - b√c). The conjugate of 5 + 2√3 is 5 - 2√3."
            },
            {
                "id": 34,
                "q": "Rationalise the denominator of 1 / (√5 + √2):",
                "options": [
                    "(√5 - √2) / 3",
                    "(√5 + √2) / 3",
                    "(√5 - √2) / 7",
                    "√3 / 7"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Multiply by conjugate (√5 - √2): 1/(√5 + √2) × (√5 - √2)/(√5 - √2) = (√5 - √2)/((√5)² - (√2)²) = (√5 - √2)/(5 - 2) = (√5 - √2)/3."
            },
            {
                "id": 35,
                "q": "Simplify the radical expression: (3 + √3)(3 - √3):",
                "options": ["9", "6", "6 - √3", "12"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Using the identity (a + b)(a - b) = a² - b²: (3 + √3)(3 - √3) = 3² - (√3)² = 9 - 3 = 6."
            },
            {
                "id": 36,
                "q": "Evaluate: (16)^(3/4):",
                "options": ["4", "8", "12", "64"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> 16 = 2⁴. Therefore (16)^(3/4) = (2⁴)^(3/4) = 2^(4 × 3/4) = 2³ = 8."
            },
            {
                "id": 37,
                "q": "Evaluate: 64^(-1/2):",
                "options": ["-8", "8", "1/8", "-1/8"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> a^(-n) = 1 / a^n. 64^(1/2) = √64 = 8. Therefore 64^(-1/2) = 1 / 64^(1/2) = 1/8."
            },
            {
                "id": 38,
                "q": "Simplify: 2^(2/3) × 2^(1/5):",
                "options": [
                    "2^(2/15)",
                    "2^(13/15)",
                    "4^(3/8)",
                    "2^(3/8)"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Using product rule a^m × a^n = a^(m + n): 2^(2/3 + 1/5) = 2^(10/15 + 3/15) = 2^(13/15)."
            },
            {
                "id": 39,
                "q": "Simplify: (7^(1/2) × 8^(1/2)):",
                "options": [
                    "56^(1/2) = √56",
                    "15^(1/2)",
                    "56",
                    "7/8"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Using power rule a^m × b^m = (ab)^m: 7^(1/2) × 8^(1/2) = (7 × 8)^(1/2) = 56^(1/2) = √56 = 2√14."
            },
            {
                "id": 40,
                "q": "Find the value of a and b if: (√3 - 1) / (√3 + 1) = a + b√3:",
                "options": [
                    "a = 2, b = -1",
                    "a = -2, b = 1",
                    "a = 1, b = 2",
                    "a = 2, b = 1"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Rationalise LHS: (√3 - 1)² / ((√3)² - 1²) = (3 + 1 - 2√3) / (3 - 1) = (4 - 2√3)/2 = 2 - √3 = 2 + (-1)√3. Comparing with a + b√3 gives a = 2, b = -1."
            }
        ]
    }
]

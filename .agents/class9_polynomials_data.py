# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 9 Mathematics, Chapter 2
UNIT II: ALGEBRA (No. of periods: 66, Competencies CG-3, C-3.2, CG-9)
Introduction to Polynomials & Linear Functions
Covers:
- Algebraic expressions (terms, variables, constants, coefficients)
- Definition of a polynomial in one variable (P(x) = a_n x^n + ... + a_0, n in W)
- Degree of a polynomial (linear, quadratic, cubic, constant, zero polynomial)
- Introduction to linear polynomials P(x) = ax + b (a != 0) and applications
- Exploring linear patterns and arithmetic differences
- Modelling linear growth (positive slope) and linear decay (negative slope)
- Linear relationships in two variables (y = ax + b, Ax + By + C = 0)
- Visualising linear relationships on the Cartesian coordinate plane
- Slope (rate of change, rise/run) and y-intercept of y = ax + b
- Computational thinking to identify patterns, construct linear equations, and analyse graphs.
16 Content Slides (with 32 In-Slide Checkpoints) + 4 Mastery Quiz Slides (40 Questions with Popup Solutions).
"""

CONTENT_SLIDES = [
    {
        "id": 1,
        "title": "Algebraic Expressions & Anatomy of Terms",
        "subtitle": "Constants, Variables, Terms, Coefficients & Arithmetic Operations",
        "narration": "Welcome to Unit 2 on Algebra. In this chapter, we transition from arithmetic to generalized algebraic thinking. An algebraic expression is formed by combining constants and variables using addition, subtraction, multiplication, and division. Each part of an expression separated by a plus or minus sign is called a term. Every term has a numerical factor called its coefficient.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Algebra allows us to generalize mathematical relationships using symbols. Let us dissect the fundamental components of algebraic language:</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-amber-400 mb-1">1. Constants & Variables</h4>
                    <p><strong>Constant:</strong> A symbol having a fixed numerical value (e.g. $5, -3, 3/4, \pi$).<br>
                    <strong>Variable:</strong> A symbol (usually letters like $x, y, z, t$) that can take various real numerical values.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-sky-400 mb-1">2. Terms & Coefficients</h4>
                    <p>In the expression $5x^2 - 3x + 7$:</p>
                    <ul class="list-disc list-inside space-y-0.5 text-slate-400 text-[11px] mt-1">
                        <li>The terms are $5x^2$, $-3x$, and $+7$.</li>
                        <li>Coefficient of $x^2$ is $5$.</li>
                        <li>Coefficient of $x$ is $-3$ (note the negative sign!).</li>
                        <li>The constant term is $7$.</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h4 class="font-bold text-indigo-300 mb-1">Like Terms vs Unlike Terms:</h4>
                <p>Terms having the exact same variables raised to the same exponents are called <strong>like terms</strong> (e.g. $7x$ and $-2x$; $4x^2y$ and $9x^2y$). Only like terms can be combined through addition or subtraction: $7x - 2x = 5x$. Unlike terms cannot be combined: $3x + 4y$ cannot be simplified further.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the coefficient of x in the algebraic expression 7x² - 5x + 9?",
                "options": [
                    "7",
                    "-5",
                    "5",
                    "9"
                ],
                "ans": 1,
                "explanation": "The term containing x is -5x. Its numerical factor (coefficient) is -5, including its negative sign."
            },
            {
                "question": "Which of the following pairs represents LIKE terms?",
                "options": [
                    "3x and 3y",
                    "4x² and 4x",
                    "-2x²y and 5x²y",
                    "7 and 7x"
                ],
                "ans": 2,
                "explanation": "Like terms must have identical variable components with matching exponents. Both -2x²y and 5x²y have the variable factor x²y."
            }
        ]
    },
    {
        "id": 2,
        "title": "Formal Definition of a Polynomial",
        "subtitle": "Non-Negative Integer Powers (n ∈ 𝕎), Domain Restrictions & Disqualifiers",
        "narration": "What distinguishes a polynomial from a general algebraic expression? A polynomial in one variable x is an algebraic expression where the exponent of the variable x in every single term is strictly a Whole Number—meaning zero or a positive integer. If an expression contains negative powers, fractions in exponents, or variables in denominators, it is NOT a polynomial.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-sm text-amber-400 mb-2">Formal Mathematical Definition:</h4>
                <p>An algebraic expression of the form:</p>
                <div class="py-2 text-center font-mono text-xs sm:text-sm text-amber-300 font-bold">
                    $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$
                </div>
                <p>is called a <strong>Polynomial in one variable $x$</strong>, provided:</p>
                <ul class="list-disc list-inside space-y-1 text-slate-300 mt-2">
                    <li>The coefficients $a_n, a_{n-1}, \dots, a_0$ are <strong>Real Numbers</strong> ($\in \mathbb{R}$).</li>
                    <li>$a_n \neq 0$ (leading coefficient).</li>
                    <li>The exponents $n, n-1, \dots$ are strictly <strong>Whole Numbers</strong> ($n \in \mathbb{W} = \{0, 1, 2, 3, \dots\}$).</li>
                </ul>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/40">
                    <h5 class="font-bold text-emerald-400 mb-1">✓ Valid Polynomials:</h5>
                    <ul class="list-disc list-inside space-y-1 text-slate-300">
                        <li>$2x^3 - 5x + 7$ (Powers: $3, 1, 0 \in \mathbb{W}$)</li>
                        <li>$\sqrt{3} x^2 + 4$ (Coefficient can be irrational; power is $2$)</li>
                        <li>$y^4 - \frac{2}{3}y$ (Real coefficients, whole powers)</li>
                        <li>$8$ (Constant polynomial: $8x^0$)</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40">
                    <h5 class="font-bold text-rose-400 mb-1">✗ NOT Polynomials (Disqualified):</h5>
                    <ul class="list-disc list-inside space-y-1 text-slate-300">
                        <li>$\frac{1}{x} = x^{-1}$ (Negative exponent $-1 \notin \mathbb{W}$)</li>
                        <li>$\sqrt{x} = x^{1/2}$ (Fractional exponent $1/2 \notin \mathbb{W}$)</li>
                        <li>$x + \frac{2}{x^2} = x + 2x^{-2}$ (Variable in denominator)</li>
                        <li>$3x^{2/3} + 5$ (Fractional index)</li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following expressions is a POLYNOMIAL in one variable?",
                "options": [
                    "x² + 2/x + 3",
                    "3√x + x",
                    "x³ - 5x + √7",
                    "x^(3/2) - 1"
                ],
                "ans": 2,
                "explanation": "In x³ - 5x + √7, the exponents of x are 3 and 1 (both whole numbers), and √7 is simply a real constant coefficient. All other choices have negative or fractional powers of x."
            },
            {
                "question": "Why is the expression 1 / (x - 2) NOT a polynomial?",
                "options": [
                    "Because 2 is an even number",
                    "Because the variable x appears in the denominator, which equals (x - 2)^(-1) having a negative exponent",
                    "Because it has no constant term",
                    "Because x can only be positive"
                ],
                "ans": 1,
                "explanation": "A polynomial cannot have variables in denominators because rewriting them in the numerator introduces negative exponents (e.g. (x-2)^(-1)), which violates the whole-number power condition."
            }
        ]
    },
    {
        "id": 3,
        "title": "Degree & Classification of Polynomials",
        "subtitle": "Linear, Quadratic, Cubic, Constant & Zero Polynomials; Monomials & Binomials",
        "narration": "The degree of a polynomial is the highest power of the variable occurring with a non-zero coefficient. It determines the complexity and shape of the polynomial's graph. Degree 1 polynomials are linear, degree 2 are quadratic, and degree 3 are cubic. Constant non-zero polynomials have degree zero, while the zero polynomial has an undefined degree.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Polynomials are categorized in two complementary ways: by their <strong>Degree</strong> and by the <strong>Number of Terms</strong>.</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">1. Classification by Degree (Highest Power):</h4>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse border border-slate-800 text-[11px]">
                        <thead>
                            <tr class="bg-slate-900 text-amber-300">
                                <th class="p-2 border border-slate-800">Type</th>
                                <th class="p-2 border border-slate-800">Degree</th>
                                <th class="p-2 border border-slate-800">Standard Form</th>
                                <th class="p-2 border border-slate-800">Example</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr>
                                <td class="p-2 font-bold text-white">Zero Polynomial</td>
                                <td class="p-2 text-rose-400">Undefined ($-\infty$)</td>
                                <td class="p-2">$P(x) = 0$</td>
                                <td class="p-2">$0$</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-white">Constant</td>
                                <td class="p-2 text-sky-400">0</td>
                                <td class="p-2">$P(x) = c \quad (c \neq 0)$</td>
                                <td class="p-2">$5 = 5x^0$</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-white">Linear</td>
                                <td class="p-2 text-emerald-400">1</td>
                                <td class="p-2">$ax + b \quad (a \neq 0)$</td>
                                <td class="p-2">$3x - 4$</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-white">Quadratic</td>
                                <td class="p-2 text-purple-400">2</td>
                                <td class="p-2">$ax^2 + bx + c \quad (a \neq 0)$</td>
                                <td class="p-2">$2x^2 + 5x - 3$</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-bold text-white">Cubic</td>
                                <td class="p-2 text-indigo-400">3</td>
                                <td class="p-2">$ax^3 + bx^2 + cx + d$</td>
                                <td class="p-2">$4x^3 - x + 1$</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-2.5">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center">
                    <span class="font-bold text-amber-400">Monomial</span>
                    <p class="text-[11px] text-slate-300 mt-1">Exactly 1 term: $5x^3$, $-7$, $2x$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center">
                    <span class="font-bold text-sky-400">Binomial</span>
                    <p class="text-[11px] text-slate-300 mt-1">Exactly 2 terms: $x^2 - 4$, $3x + 1$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center">
                    <span class="font-bold text-emerald-400">Trinomial</span>
                    <p class="text-[11px] text-slate-300 mt-1">Exactly 3 terms: $x^2 + 5x + 6$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the degree of the non-zero constant polynomial P(x) = -9?",
                "options": [
                    "0",
                    "1",
                    "-9",
                    "Undefined"
                ],
                "ans": 0,
                "explanation": "-9 can be written as -9x^0. The highest power of the variable is 0. Hence, the degree of any non-zero constant polynomial is 0."
            },
            {
                "question": "What is the degree of the zero polynomial P(x) = 0?",
                "options": [
                    "0",
                    "1",
                    "Not defined",
                    "Infinity"
                ],
                "ans": 2,
                "explanation": "Because 0 can be written as 0x^1, 0x^2, 0x^100, etc., with any exponent, mathematicians define the degree of the zero polynomial to be Not Defined."
            }
        ]
    },
    {
        "id": 4,
        "title": "Introduction to Linear Polynomials",
        "subtitle": "Standard Form P(x) = ax + b (a ≠ 0), Zeroes & Root Geometry",
        "narration": "A linear polynomial is a polynomial of degree one. Its standard algebraic form is P of x equals ax plus b, where a and b are real numbers and a cannot be zero. The value of x for which P of x equals zero is called the zero or root of the polynomial. For any linear polynomial, there is always exactly one unique real zero: x equals minus b over a.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Standard Form of Linear Polynomial:</h4>
                <div class="py-1 text-center font-mono text-base text-amber-300 font-bold">
                    $P(x) = ax + b, \\quad \\text{where } a, b \\in \\mathbb{R} \\text{ and } a \\neq 0$
                </div>
                <p class="text-[11px] text-slate-400 mt-1">The term $ax$ is the linear term, $a$ is the leading coefficient (slope), and $b$ is the constant term.</p>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-sky-400">Finding the Zero (Root) of $P(x)$:</h4>
                <p>A real number $k$ is a <strong>zero</strong> of $P(x)$ if $P(k) = 0$. To find the zero algebraically, set $P(x) = 0$:</p>
                <div class="py-1 text-center font-mono text-sky-300 text-xs">
                    $ax + b = 0 \\implies ax = -b \\implies k = -\\frac{b}{a}$
                </div>
                <p><strong>Fundamental Geometric Theorem:</strong> Every linear polynomial has <em>exactly one unique real zero</em>. Graphically, this corresponds to the point where the line crosses the horizontal $x$-axis: $(-b/a, 0)$.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                    <span class="font-bold text-emerald-400">Example 1: $P(x) = 2x - 6$</span>
                    <p class="text-[11px] mt-1">$2x - 6 = 0 \\implies 2x = 6 \\implies x = 3$.<br>The unique zero is $x = 3$.</p>
                </div>
                <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                    <span class="font-bold text-emerald-400">Example 2: $P(x) = 5x + 4$</span>
                    <p class="text-[11px] mt-1">$5x + 4 = 0 \\implies 5x = -4 \\implies x = -4/5$.<br>The unique zero is $x = -0.8$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the zero of the linear polynomial P(x) = 3x - 15?",
                "options": [
                    "x = -5",
                    "x = 5",
                    "x = 15",
                    "x = 3"
                ],
                "ans": 1,
                "explanation": "Set P(x) = 0: 3x - 15 = 0 => 3x = 15 => x = 15/3 = 5."
            },
            {
                "question": "How many real zeroes can a linear polynomial P(x) = ax + b (a ≠ 0) have?",
                "options": [
                    "Zero zeroes",
                    "Exactly one zero",
                    "At most two zeroes",
                    "Infinitely many zeroes"
                ],
                "ans": 1,
                "explanation": "A non-zero polynomial of degree n can have at most n roots. For a linear polynomial (degree 1), there is always exactly one unique zero: x = -b/a."
            }
        ]
    },
    {
        "id": 5,
        "title": "Exploring Linear Patterns & First Differences",
        "subtitle": "Constant Rate of Change (Δy/Δx), Arithmetic Sequences & Function Tables",
        "narration": "How can you tell if a real-world pattern is linear? Look at the rate of change! In any linear relationship, when the input x increases by equal increments, the output y changes by a constant amount. This constant change is called the First Difference. If the first differences are identical, the relationship is guaranteed to be linear.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Linear relationships are governed by the principle of <strong>constant rate of change</strong>.</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">The First Differences Rule:</h4>
                <p>Consider an input-output table with evenly spaced inputs ($x$ values increasing by $\Delta x = 1$):</p>
                <div class="overflow-x-auto">
                    <table class="w-full text-center border-collapse border border-slate-800 text-[11px]">
                        <thead>
                            <tr class="bg-slate-900 text-sky-400">
                                <th class="p-1.5 border border-slate-800">Input ($x$)</th>
                                <th class="p-1.5 border border-slate-800">0</th>
                                <th class="p-1.5 border border-slate-800">1</th>
                                <th class="p-1.5 border border-slate-800">2</th>
                                <th class="p-1.5 border border-slate-800">3</th>
                                <th class="p-1.5 border border-slate-800">4</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr>
                                <td class="p-1.5 font-bold text-white">Output ($y$)</td>
                                <td class="p-1.5">2</td>
                                <td class="p-1.5">5</td>
                                <td class="p-1.5">8</td>
                                <td class="p-1.5">11</td>
                                <td class="p-1.5">14</td>
                            </tr>
                            <tr class="text-emerald-400 font-bold bg-slate-950">
                                <td class="p-1.5 text-white">First Diff ($\\Delta y$)</td>
                                <td class="p-1.5">-</td>
                                <td class="p-1.5">+3</td>
                                <td class="p-1.5">+3</td>
                                <td class="p-1.5">+3</td>
                                <td class="p-1.5">+3</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">Because $\Delta y = 3$ is constant for each $\Delta x = 1$, the slope is $a = \frac{\Delta y}{\Delta x} = 3$. At $x=0$, $y=2$, so $b=2$. The linear rule is: $\mathbf{y = 3x + 2}$.</p>
            </div>

            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h5 class="font-bold text-indigo-300 mb-1">Computational Pattern Test:</h5>
                <p>If $\Delta y$ is constant $\implies$ Linear ($y = ax + b$).<br>
                If the second differences $\Delta^2 y$ are constant $\implies$ Quadratic ($y = ax^2 + bx + c$).<br>
                If the ratio $y_{k+1}/y_k$ is constant $\implies$ Exponential ($y = a \cdot b^x$).</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "A table gives outputs y = 4, 9, 14, 19 for inputs x = 1, 2, 3, 4. What is the linear rule connecting x and y?",
                "options": [
                    "y = 4x",
                    "y = 5x - 1",
                    "y = 5x + 4",
                    "y = x + 5"
                ],
                "ans": 1,
                "explanation": "First differences: 9-4=5, 14-9=5, 19-14=5. The slope is 5. For x=1, y=4, so y = 5(1) + b = 4 => b = -1. Thus y = 5x - 1."
            },
            {
                "question": "Which of the following sequence of outputs (for x = 1, 2, 3, 4) represents a LINEAR relationship?",
                "options": [
                    "1, 4, 9, 16",
                    "2, 4, 8, 16",
                    "10, 7, 4, 1",
                    "1, 3, 7, 15"
                ],
                "ans": 2,
                "explanation": "For 10, 7, 4, 1: 7-10 = -3, 4-7 = -3, 1-4 = -3. The first difference is constantly -3. Thus it is a linear pattern with slope -3."
            }
        ]
    },
    {
        "id": 6,
        "title": "Modelling Linear Growth",
        "subtitle": "Positive Slope (a > 0), Real-World Accumulation & Direct Applications",
        "narration": "Linear growth describes any real-world phenomenon where a quantity increases by the same fixed amount over equal intervals of time or distance. Think of a taxi fare with a base charge plus a fixed fee per kilometer, or a savings account growing by a steady monthly deposit. In mathematical terms, linear growth is modeled by y equals ax plus b where the rate a is positive.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-emerald-500/30">
                <h4 class="font-bold text-emerald-400 text-sm mb-1">Mathematical Model of Linear Growth:</h4>
                <div class="py-1 text-center font-mono text-base text-emerald-300 font-bold">
                    $y = ax + b, \\quad \\text{with } a > 0$
                </div>
                <ul class="list-disc list-inside space-y-1 text-slate-300 text-[11px] mt-1">
                    <li>$y$: Total accumulated quantity (dependent variable).</li>
                    <li>$x$: Units elapsed (time, distance, hours, items) (independent variable).</li>
                    <li>$a$: Positive growth rate (slope, change per unit).</li>
                    <li>$b$: Initial value / base offset (value of $y$ when $x = 0$).</li>
                </ul>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-amber-400 mb-1">Application 1: Taxi Meter Fare</h5>
                    <p>A city taxi charges a base fare of $₹50$ plus $₹12$ for each kilometer traveled ($d$ km):</p>
                    <p class="font-mono text-amber-300 my-1 text-center font-bold">$F(d) = 12d + 50$</p>
                    <p class="text-[11px] text-slate-400">For a $10$ km trip: $F(10) = 12(10) + 50 = ₹170$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Application 2: Plant Height Growth</h5>
                    <p>A bamboo sapling starts at $15$ cm and grows steadily at $3$ cm per day ($t$ days):</p>
                    <p class="font-mono text-sky-300 my-1 text-center font-bold">$H(t) = 3t + 15$</p>
                    <p class="text-[11px] text-slate-400">After $20$ days: $H(20) = 3(20) + 15 = 75$ cm.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "A gym membership costs an enrollment fee of ₹500 plus ₹300 per month. What linear polynomial represents the total cost C(m) after m months?",
                "options": [
                    "C(m) = 500m + 300",
                    "C(m) = 300m + 500",
                    "C(m) = 800m",
                    "C(m) = 300m - 500"
                ],
                "ans": 1,
                "explanation": "The monthly fee is the recurring rate of change (slope a = 300), and the initial enrollment fee is the constant y-intercept (b = 500). Thus C(m) = 300m + 500."
            },
            {
                "question": "In the linear growth equation y = ax + b, what geometric feature indicates that the quantity is growing rather than shrinking?",
                "options": [
                    "b > 0",
                    "The slope a is strictly positive (a > 0)",
                    "x is always an integer",
                    "The line passes through origin"
                ],
                "ans": 1,
                "explanation": "A positive slope (a > 0) means that as x increases, y also increases, producing an upward-sloping line that models growth."
            }
        ]
    },
    {
        "id": 7,
        "title": "Modelling Linear Decay",
        "subtitle": "Negative Slope (a < 0), Depletion, Water Tank Drainage & Battery Drain",
        "narration": "Linear decay models the opposite process: a quantity that decreases at a constant rate over time. Examples include a water tank emptying at a constant drain rate, a smartphone battery discharging steadily during use, or a cooling engine. In mathematical equations, decay is characterized by a negative slope a less than zero.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-rose-500/30">
                <h4 class="font-bold text-rose-400 text-sm mb-1">Mathematical Model of Linear Decay:</h4>
                <div class="py-1 text-center font-mono text-base text-rose-300 font-bold">
                    $y = -|a|x + b \\quad \\text{or} \\quad y = ax + b, \\quad \\text{with } a < 0$
                </div>
                <p class="text-[11px] text-slate-400 mt-1">The line slopes downward from left to right. As $x$ increases, $y$ steadily decreases until it hits zero (the horizontal intercept).</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-amber-400 mb-1">Application 1: Water Tank Drainage</h5>
                    <p>A $1000$-liter water reservoir drains at a constant rate of $25$ liters per minute ($t$ min):</p>
                    <p class="font-mono text-amber-300 my-1 text-center font-bold">$V(t) = -25t + 1000$</p>
                    <p class="text-[11px] text-slate-400">When will it be completely empty ($V = 0$)?<br>
                    $0 = -25t + 1000 \\implies 25t = 1000 \\implies t = 40$ minutes.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Application 2: Smartphone Battery Drain</h5>
                    <p>A phone starts at $100\\%$ battery and discharges at $8\\%$ per hour of screen time ($h$):</p>
                    <p class="font-mono text-sky-300 my-1 text-center font-bold">$B(h) = -8h + 100$</p>
                    <p class="text-[11px] text-slate-400">Battery after $6$ hours: $B(6) = -8(6) + 100 = 52\\%$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "A 500-liter tank empties at 20 liters per minute. After how many minutes will the tank be completely dry?",
                "options": [
                    "20 minutes",
                    "25 minutes",
                    "50 minutes",
                    "10 minutes"
                ],
                "ans": 1,
                "explanation": "Model: V(t) = -20t + 500. Set V(t) = 0: 0 = -20t + 500 => 20t = 500 => t = 25 minutes."
            },
            {
                "question": "What is the slope of the line representing the fuel decay model F(d) = -0.08d + 50?",
                "options": [
                    "50",
                    "-0.08",
                    "0.08",
                    "-50"
                ],
                "ans": 1,
                "explanation": "In y = ax + b, the slope is the coefficient of the variable d, which is -0.08 (indicating fuel decreases by 0.08 liters per km)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Linear Relationships in Two Variables",
        "subtitle": "Connecting x and y: Implicit Form (Ax + By + C = 0) vs Slope-Intercept Form",
        "narration": "So far, we have studied polynomials in one variable. When we equate a linear polynomial to a second variable y, we obtain a Linear Equation in Two Variables: y equals ax plus b. We can also write it in the standard general form Ax plus By plus C equals zero. Every solution to this equation is an ordered pair of numbers (x, y) that satisfies the equality.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>An equation involving two variables with highest power 1 for each variable is called a <strong>Linear Equation in Two Variables</strong>.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-amber-400 mb-1">1. General (Standard) Form:</h4>
                    <p class="font-mono text-center text-amber-300 my-1 font-bold">$Ax + By + C = 0$</p>
                    <p class="text-[11px] text-slate-400">where $A, B, C$ are real numbers, and $A$ and $B$ are not both zero ($A^2 + B^2 \neq 0$). Example: $3x + 2y - 12 = 0$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h4 class="font-bold text-sky-400 mb-1">2. Slope-Intercept (Explicit) Form:</h4>
                    <p class="font-mono text-center text-sky-300 my-1 font-bold">$y = mx + c \quad \text{or} \quad y = ax + b$</p>
                    <p class="text-[11px] text-slate-400">Solving for $y$: $By = -Ax - C \implies y = \left(-\frac{A}{B}\right)x + \left(-\frac{C}{B}\right)$. Here slope $m = -A/B$ and $y$-intercept $c = -C/B$.</p>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 space-y-1">
                <h4 class="font-bold text-indigo-300">Infinitely Many Solutions:</h4>
                <p>Unlike a linear equation in one variable (which has exactly 1 solution), a linear equation in two variables has <strong>infinitely many solutions</strong>! For any chosen value of $x$, there exists a corresponding value of $y$ that satisfies the equation. Each solution is written as an ordered pair $(x, y)$.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many solutions does the linear equation 2x + 3y = 12 have in the real number system?",
                "options": [
                    "A unique solution",
                    "Exactly two solutions",
                    "Infinitely many solutions",
                    "No solution"
                ],
                "ans": 2,
                "explanation": "A linear equation in two variables represents a continuous straight line containing infinitely many points (x, y), each of which is a valid solution."
            },
            {
                "question": "Express the equation 4x - 2y = 8 in the slope-intercept form y = ax + b:",
                "options": [
                    "y = 2x - 4",
                    "y = 4x - 8",
                    "y = -2x + 4",
                    "y = 2x + 4"
                ],
                "ans": 0,
                "explanation": "4x - 2y = 8 => -2y = -4x + 8 => Divide by -2: y = 2x - 4."
            }
        ]
    },
    {
        "id": 9,
        "title": "Visualising Linear Relationships on the Plane",
        "subtitle": "Cartesian Coordinate System, Ordered Pairs & Geometric Straight Lines",
        "narration": "René Descartes revolutionized mathematics by uniting algebra and geometry through the Cartesian plane. When all the infinitely many ordered pairs (x, y) that satisfy a linear equation are plotted on the Cartesian plane, they align perfectly into a single continuous Straight Line! This is why such equations are called linear.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">The Geometric Fundamental Theorem of Linear Equations:</h4>
                <p>The graph of every linear equation in two variables $Ax + By + C = 0$ is a <strong>Straight Line</strong> on the Cartesian coordinate plane.</p>
                <ul class="list-disc list-inside space-y-1 text-slate-300 text-[11px]">
                    <li>Every point $(x_1, y_1)$ lying on the line is a solution to the equation.</li>
                    <li>Every solution $(x_1, y_1)$ to the equation corresponds to a point lying on the line.</li>
                    <li>Any point not on the line is NOT a solution.</li>
                </ul>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-sky-400 mb-1">Horizontal Lines ($y = c$):</h5>
                    <p>When $A = 0$, the equation becomes $By + C = 0 \implies y = c$. The line is parallel to the $x$-axis. Slope $m = 0$. Example: $y = 3$.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <h5 class="font-bold text-emerald-400 mb-1">Vertical Lines ($x = k$):</h5>
                    <p>When $B = 0$, the equation becomes $Ax + C = 0 \implies x = k$. The line is parallel to the $y$-axis. Slope is <strong>undefined</strong>. Example: $x = -2$.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the geometric representation of the equation x = 4 on the Cartesian plane?",
                "options": [
                    "A point at (4, 0)",
                    "A horizontal line parallel to the x-axis",
                    "A vertical line parallel to the y-axis passing through (4, 0)",
                    "A circle of radius 4"
                ],
                "ans": 2,
                "explanation": "In two dimensions, x = 4 means x is always 4 for any value of y, creating a vertical line parallel to the y-axis at x = 4."
            },
            {
                "question": "Does the point (2, 5) lie on the graph of the line 3x - y = 1?",
                "options": [
                    "Yes, because 3(2) - 5 = 6 - 5 = 1",
                    "No, because 2 + 5 = 7",
                    "Only if x is negative",
                    "Cannot be determined"
                ],
                "ans": 0,
                "explanation": "Substitute x = 2 and y = 5 into LHS: 3(2) - 5 = 6 - 5 = 1 = RHS. Since it satisfies the equation, the point lies on the line."
            }
        ]
    },
    {
        "id": 10,
        "title": "The Slope of a Line (m or a)",
        "subtitle": "Geometric Steepness, Rise Over Run, Rate of Change (Δy/Δx) & Angle of Inclination",
        "narration": "The slope of a line, denoted by m or a, measures its steepness and direction. It is defined as the vertical change, known as the rise, divided by the horizontal change, known as the run. Given any two distinct points on the line, the slope equals y2 minus y1 divided by x2 minus x1. A line going uphill has positive slope, while downhill has negative slope.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                <h4 class="font-bold text-amber-400 text-sm mb-1">Formal Definition of Slope ($m$):</h4>
                <div class="py-1 text-center font-mono text-base text-amber-300 font-bold">
                    $m = \frac{\text{Rise}}{\text{Run}} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}, \quad \text{for } x_2 \neq x_1$
                </div>
                <p class="text-[11px] text-slate-400 mt-1">The slope represents the constant rate at which $y$ increases for every $1$ unit increase in $x$.</p>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-[11px]">
                <div class="p-2.5 rounded-lg bg-emerald-950/50 border border-emerald-500/40">
                    <span class="font-bold text-emerald-300 block">Positive ($m > 0$)</span>
                    <span class="text-slate-400">Slopes upward to right (Growth)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-rose-950/50 border border-rose-500/40">
                    <span class="font-bold text-rose-300 block">Negative ($m < 0$)</span>
                    <span class="text-slate-400">Slopes downward to right (Decay)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-sky-950/50 border border-sky-500/40">
                    <span class="font-bold text-sky-300 block">Zero ($m = 0$)</span>
                    <span class="text-slate-400">Horizontal line ($\Delta y = 0$)</span>
                </div>
                <div class="p-2.5 rounded-lg bg-purple-950/50 border border-purple-500/40">
                    <span class="font-bold text-purple-300 block">Undefined</span>
                    <span class="text-slate-400">Vertical line ($\Delta x = 0$)</span>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the slope of the straight line passing through points (2, 3) and (6, 11)?",
                "options": [
                    "m = 2",
                    "m = 8/4 = 2",
                    "m = 4/8 = 1/2",
                    "m = -2"
                ],
                "ans": 1,
                "explanation": "m = (y2 - y1) / (x2 - x1) = (11 - 3) / (6 - 2) = 8 / 4 = 2."
            },
            {
                "question": "What is the slope of a horizontal line parallel to the x-axis?",
                "options": [
                    "m = 1",
                    "m = 0",
                    "m = Infinity",
                    "Undefined"
                ],
                "ans": 1,
                "explanation": "For any two points on a horizontal line, y2 = y1, so rise Δy = 0. Slope m = 0 / Δx = 0."
            }
        ]
    },
    {
        "id": 11,
        "title": "The y-Intercept and x-Intercept",
        "subtitle": "Axis Intersections: Starting Value (0, b) and Zero of Function (-b/a, 0)",
        "narration": "Where does a line cross the axes? The points where the line intersects the coordinate axes are called the intercepts. The y-intercept is the point where the line crosses the y-axis, found by setting x equal to zero. The x-intercept is where it crosses the x-axis, found by setting y equal to zero. Together, these two intercepts give us the easiest way to graph any line.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="font-bold text-amber-400 text-sm mb-1">1. The $y$-Intercept ($b$):</h4>
                    <p>The value of $y$ where the line crosses the vertical $y$-axis (where $x = 0$):</p>
                    <p class="font-mono text-center text-amber-300 my-1 font-bold">$(0, b)$</p>
                    <p class="text-[11px] text-slate-400">In real-world models, the $y$-intercept represents the <strong>initial state or starting value</strong> at time zero.</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-sky-500/30">
                    <h4 class="font-bold text-sky-400 text-sm mb-1">2. The $x$-Intercept:</h4>
                    <p>The value of $x$ where the line crosses the horizontal $x$-axis (where $y = 0$):</p>
                    <p class="font-mono text-center text-sky-300 my-1 font-bold">$\left(-\frac{b}{a}, 0\right)$</p>
                    <p class="text-[11px] text-slate-400">The $x$-intercept is precisely the <strong>zero of the linear polynomial</strong> $P(x) = ax + b$.</p>
                </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
                <h5 class="font-bold text-emerald-400 mb-1">Example: Find Intercepts of $2x + 3y = 6$</h5>
                <ul class="list-disc list-inside space-y-1 text-slate-300 text-[11px]">
                    <li><strong>$x$-intercept:</strong> Set $y = 0 \implies 2x + 3(0) = 6 \implies 2x = 6 \implies x = 3$. Point: $(3, 0)$.</li>
                    <li><strong>$y$-intercept:</strong> Set $x = 0 \implies 2(0) + 3y = 6 \implies 3y = 6 \implies y = 2$. Point: $(0, 2)$.</li>
                </ul>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the y-intercept of the line 3x - 4y = 12?",
                "options": [
                    "(0, 3)",
                    "(0, -3)",
                    "(4, 0)",
                    "(0, -4)"
                ],
                "ans": 1,
                "explanation": "Set x = 0: 3(0) - 4y = 12 => -4y = 12 => y = -3. The y-intercept is (0, -3)."
            },
            {
                "question": "What is the x-intercept of the line y = 2x - 8?",
                "options": [
                    "(4, 0)",
                    "(0, -8)",
                    "(-4, 0)",
                    "(8, 0)"
                ],
                "ans": 0,
                "explanation": "Set y = 0: 0 = 2x - 8 => 2x = 8 => x = 4. The x-intercept is (4, 0)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Algorithmic Graphing: The Intercept Method",
        "subtitle": "Step-by-Step Procedure: Two Defining Points & A Third Verification Point",
        "narration": "Euclid’s first postulate tells us that two distinct points determine a unique straight line. Therefore, to graph any linear equation, we only need to compute two points—ideally the x-intercept and the y-intercept. However, in good engineering practice, we always calculate a third test point. If all three points lie on the same straight line, our graph is guaranteed to be error-free.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <p>Here is the standard algorithmic procedure to graph any linear equation $Ax + By = C$:</p>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">The 3-Point Graphing Algorithm:</h4>
                <ol class="list-decimal list-inside space-y-1.5 text-slate-300">
                    <li><strong>Point 1 ($y$-intercept):</strong> Set $x = 0$, solve for $y \implies P_1(0, y_1)$.</li>
                    <li><strong>Point 2 ($x$-intercept):</strong> Set $y = 0$, solve for $x \implies P_2(x_2, 0)$.</li>
                    <li><strong>Point 3 (Verification Check):</strong> Pick an intermediate integer $x = x_3$, calculate $y_3 \implies P_3(x_3, y_3)$.</li>
                    <li><strong>Collinearity Test:</strong> Plot $P_1, P_2, P_3$. Lay a straightedge ruler across them. If they are collinear (all 3 fall on one line), draw the line through them and extend with arrows on both ends.</li>
                </ol>
            </div>

            <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h5 class="font-bold text-indigo-300 mb-1">What if the line passes through the origin $(0, 0)$?</h5>
                <p>If $C = 0$ (e.g. $y = 2x$), both intercepts coincide at $(0, 0)$. In this case, simply choose two other convenient non-zero inputs, such as $x = 1 \implies y = 2$ and $x = -1 \implies y = -2$, to obtain two distinct points.</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Why is it recommended to plot at least three points when graphing a linear equation by hand?",
                "options": [
                    "Because two points cannot define a line",
                    "To act as an error check: if the three points are not collinear, an arithmetic mistake occurred",
                    "Because three points form a triangle",
                    "It is mandatory under Euclid's laws"
                ],
                "ans": 1,
                "explanation": "While two points are mathematically sufficient to draw a line, computing a third point acts as an immediate check: if all three do not align on a single straight edge, you know one of your coordinates was miscalculated."
            },
            {
                "question": "Which of the following lines passes directly through the origin (0, 0)?",
                "options": [
                    "2x + 3y = 6",
                    "y = 5x",
                    "x + y = 1",
                    "y = 4"
                ],
                "ans": 1,
                "explanation": "For y = 5x, when x = 0, y = 5(0) = 0. Since (0, 0) satisfies the equation, it passes through the origin."
            }
        ]
    },
    {
        "id": 13,
        "title": "Direct Variation vs General Linear Models",
        "subtitle": "Proportional Models (y = kx) vs Affine Models (y = ax + b)",
        "narration": "In science and commerce, some relationships start at zero—such as cost proportional to weight of fruit, or distance traveled at constant speed. This is Direct Variation: y equals kx, which always passes through the origin. When a fixed starting cost or offset is added, it becomes a general linear model y equals ax plus b, shifting the line upward or downward by b units.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div class="p-3.5 rounded-xl bg-slate-900 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-400 text-sm mb-1">1. Direct Proportionality ($y = kx$):</h4>
                    <p>When the constant term is zero ($b = 0$):</p>
                    <div class="py-1 text-center font-mono text-cyan-300 font-bold">$y = kx \implies \frac{y}{x} = k = \text{constant}$</div>
                    <ul class="list-disc list-inside space-y-0.5 text-slate-400 text-[11px]">
                        <li>Always passes through the origin $(0, 0)$.</li>
                        <li>Doubling $x$ exactly doubles $y$.</li>
                        <li>$k$ is the constant of variation (slope).</li>
                    </ul>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/30">
                    <h4 class="font-bold text-amber-400 text-sm mb-1">2. General Linear (Affine) Model ($y = ax + b$):</h4>
                    <p>When an initial fixed offset $b \neq 0$ is present:</p>
                    <div class="py-1 text-center font-mono text-amber-300 font-bold">$y = ax + b$</div>
                    <ul class="list-disc list-inside space-y-0.5 text-slate-400 text-[11px]">
                        <li>Does NOT pass through $(0, 0)$; passes through $(0, b)$.</li>
                        <li>Doubling $x$ does NOT double $y$.</li>
                        <li>Example: Temperature $F = \frac{9}{5}C + 32$.</li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If y varies directly with x and y = 15 when x = 3, what is the constant of variation k?",
                "options": [
                    "k = 3",
                    "k = 5",
                    "k = 45",
                    "k = 1/5"
                ],
                "ans": 1,
                "explanation": "Direct variation: y = kx => k = y/x = 15/3 = 5."
            },
            {
                "question": "In the temperature conversion formula F = (9/5)C + 32, why is F NOT directly proportional to C?",
                "options": [
                    "Because 9/5 is a fraction",
                    "Because of the constant offset +32, which means (0, 0) is not on the line (when C=0, F=32)",
                    "Because temperature cannot be negative",
                    "Because Celsius is metric"
                ],
                "ans": 1,
                "explanation": "Because F/C is not constant (due to +32). At C = 0, F = 32 ≠ 0, so the line does not pass through the origin."
            }
        ]
    },
    {
        "id": 14,
        "title": "Computational Pattern Recognition & Extrapolation",
        "subtitle": "Algorithmic Discovery of Equations from Datasets & Future Predictions",
        "narration": "In data science and computational thinking, machines are given tables of inputs and outputs and must automatically discover the underlying formula. The algorithm is straightforward: first calculate the rate of change delta y over delta x to find slope a. Second, solve for intercept b using any known data point. Once the equation y equals ax plus b is found, we can extrapolate and predict any future output.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">The 4-Step Computational Discovery Algorithm:</h4>
                <ol class="list-decimal list-inside space-y-1.5 text-slate-300">
                    <li><strong>Step 1 (Compute Slope):</strong> Take any two distinct points $(x_1, y_1)$ and $(x_2, y_2)$ from the dataset:
                        <p class="font-mono text-center text-amber-300 my-1">$a = \frac{y_2 - y_1}{x_2 - x_1}$</p>
                    </li>
                    <li><strong>Step 2 (Compute Intercept):</strong> Substitute slope $a$ and point $(x_1, y_1)$ into $y = ax + b$:
                        <p class="font-mono text-center text-sky-300 my-1">$b = y_1 - a x_1$</p>
                    </li>
                    <li><strong>Step 3 (Synthesize Model):</strong> Assemble the predictive equation $y = ax + b$.</li>
                    <li><strong>Step 4 (Extrapolate & Predict):</strong> To find the output for any target input $x_{target}$, compute $y_{pred} = a x_{target} + b$.</li>
                </ol>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "A dataset contains points (2, 7) and (5, 16). Using the 4-step algorithm, what is the predictive equation?",
                "options": [
                    "y = 3x + 1",
                    "y = 2x + 3",
                    "y = 3x - 1",
                    "y = 4x - 1"
                ],
                "ans": 0,
                "explanation": "Step 1: a = (16 - 7)/(5 - 2) = 9/3 = 3. Step 2: b = 7 - 3(2) = 7 - 6 = 1. Model: y = 3x + 1."
            },
            {
                "question": "Using the model y = 3x + 1, what is the extrapolated prediction for x = 12?",
                "options": [
                    "36",
                    "37",
                    "35",
                    "38"
                ],
                "ans": 1,
                "explanation": "y = 3(12) + 1 = 36 + 1 = 37."
            }
        ]
    },
    {
        "id": 15,
        "title": "Systems of Linear Relationships: Break-Even Analysis",
        "subtitle": "Simultaneous Lines, Intersection Point (x*, y*) & Economic Break-Even",
        "narration": "What happens when two different linear relationships operate in the same scenario? In business, a company has a Cost function with a fixed overhead plus manufacturing cost, and a Revenue function from selling products. Where these two lines intersect is the Break-Even Point. Before this point, the business operates at a loss; after this point, it generates profit.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">The Break-Even Formulation:</h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                        <span class="font-bold text-rose-400">Total Cost Function: $C(x)$</span>
                        <p class="font-mono text-center text-rose-300 my-1">$C(x) = v x + F$</p>
                        <p class="text-[10px] text-slate-400">$F$ = Fixed overhead costs, $v$ = variable production cost per unit.</p>
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800">
                        <span class="font-bold text-emerald-400">Total Revenue Function: $R(x)$</span>
                        <p class="font-mono text-center text-emerald-300 my-1">$R(x) = p x$</p>
                        <p class="text-[10px] text-slate-400">$p$ = Selling price per unit ($p > v$).</p>
                    </div>
                </div>

                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <h5 class="font-bold text-amber-300 mb-1">Finding the Break-Even Point ($x^*$):</h5>
                    <p>Equate Cost and Revenue: $R(x^*) = C(x^*)$:</p>
                    <div class="py-1 text-center font-mono text-amber-300 font-bold">$p x^* = v x^* + F \implies (p - v) x^* = F \implies x^* = \frac{F}{p - v}$</div>
                    <p class="text-[11px] text-slate-400">Example: $F = ₹1000$, variable cost $v = ₹20$, selling price $p = ₹40$. Break-even quantity: $x^* = 1000 / (40 - 20) = 50$ units.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "A baker has fixed daily rent of ₹600. It costs ₹10 to bake each loaf of bread, which sells for ₹25. How many loaves must be sold to break even?",
                "options": [
                    "24 loaves",
                    "40 loaves",
                    "60 loaves",
                    "15 loaves"
                ],
                "ans": 1,
                "explanation": "Break-even condition: Revenue = Cost => 25x = 10x + 600 => 15x = 600 => x = 40 loaves."
            },
            {
                "question": "On a graph with Cost line C(x) and Revenue line R(x), what does the region to the RIGHT of the intersection point represent?",
                "options": [
                    "Net Loss region",
                    "Net Profit region (Revenue exceeds Cost)",
                    "Zero production",
                    "Undefined territory"
                ],
                "ans": 1,
                "explanation": "To the right of the break-even point, the Revenue line R(x) rises higher than the Cost line C(x), representing net financial profit."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking Synthesis: Linear Algebra",
        "subtitle": "Algorithmic Complexity, Interpolation, Extrapolation & Real-World Decision Systems",
        "narration": "In this final concept slide, we synthesize the power of linear polynomials in computational thinking. Linear models are the workhorses of artificial intelligence, machine learning, and data analytics. When an AI fits a linear regression line to massive data, it is executing the exact slope-intercept mathematics we have mastered today. Linear relationships empower us to reason logically, detect patterns, and make rigorous predictions.",
        "theory": r"""
        <div class="space-y-4 text-xs leading-relaxed text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <h4 class="font-bold text-amber-400">Core Competencies Mastery Checklist (CG-3, C-3.2, CG-9):</h4>
                <ul class="list-disc list-inside space-y-1.5 text-slate-300 text-[11px]">
                    <li><strong>Algebraic Fluency:</strong> Defining polynomials, verifying non-negative integer exponents, and categorizing degrees.</li>
                    <li><strong>Linear Modeling:</strong> Expressing physical growth ($a > 0$) and decay ($a < 0$) using $P(x) = ax + b$.</li>
                    <li><strong>Geometric Mapping:</strong> Translating equations into straight line Cartesian graphs via slopes and intercepts.</li>
                    <li><strong>Algorithmic Extraction:</strong> Computing rates of change, detecting patterns in tables, and calculating break-even solutions.</li>
                </ul>
            </div>

            <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
                <h5 class="font-bold text-indigo-300 mb-1">Bridge to Higher Mathematics:</h5>
                <p>Linear polynomials form the foundation for <strong>Linear Regression in Machine Learning</strong>, systems of linear equations in Class 10, and Linear Programming in Class 12. Every complex curved function in calculus can be approximated locally by a linear tangent line ($y = ax + b$)!</p>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the primary difference between interpolation and extrapolation?",
                "options": [
                    "Interpolation estimates values within known data bounds; extrapolation estimates values beyond known data bounds",
                    "Interpolation is for curves; extrapolation is for lines",
                    "Interpolation uses negative numbers",
                    "They are identical terms"
                ],
                "ans": 0,
                "explanation": "Interpolation predicts values inside the observed range of data points, whereas extrapolation extends the trend to predict values outside the observed domain."
            },
            {
                "question": "Which of the following describes the rate of change of any linear model y = ax + b?",
                "options": [
                    "It changes exponentially",
                    "It is strictly constant and equal to the slope a",
                    "It depends on the value of x",
                    "It is always zero"
                ],
                "ans": 1,
                "explanation": "The fundamental characteristic of any linear polynomial is that its rate of change (first derivative or slope) is strictly constant and equals a."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Quiz Challenge • Part 1",
        "subtitle": "Algebraic Expressions, Polynomial Definitions, Terms & Degrees",
        "questions": [
            {
                "id": 1,
                "q": "Which of the following is a polynomial in one variable?",
                "options": ["x² + 3/x + 2", "4x³ - 5x² + √2", "2√x + 7", "x^(2/3) + 1"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> In 4x³ - 5x² + √2, the powers of x are 3, 2, and 0 (all whole numbers), and √2 is a real constant. 3/x has power -1, 2√x has power 1/2, and x^(2/3) has power 2/3 (none of which are whole numbers)."
            },
            {
                "id": 2,
                "q": "What is the degree of the polynomial P(x) = 7x⁴ - 3x⁶ + 2x - 5?",
                "options": ["4", "6", "1", "7"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The degree is the highest exponent of the variable with non-zero coefficient. Here the term with the highest power is -3x⁶, which has power 6. Hence degree = 6."
            },
            {
                "id": 3,
                "q": "What is the coefficient of x² in the expression (2x - 3)(x + 5)?",
                "options": ["2", "7", "-15", "10"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Expand the product: (2x - 3)(x + 5) = 2x(x + 5) - 3(x + 5) = 2x² + 10x - 3x - 15 = 2x² + 7x - 15. The coefficient of x² is 2."
            },
            {
                "id": 4,
                "q": "A polynomial containing exactly two non-zero terms is called a:",
                "options": ["Monomial", "Binomial", "Trinomial", "Linear polynomial"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> A polynomial with exactly 1 term is a monomial, 2 terms is a binomial, and 3 terms is a trinomial."
            },
            {
                "id": 5,
                "q": "What is the degree of the zero polynomial 0?",
                "options": ["0", "1", "Not defined", "Infinity"],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> 0 can be written as 0x^n for any whole number n. Since no unique highest power can be assigned, its degree is defined as Not Defined."
            },
            {
                "id": 6,
                "q": "What is the degree of the constant polynomial P(x) = √5?",
                "options": ["1/2", "0", "1", "5"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> √5 is a non-zero real number: P(x) = √5 · x⁰. The power of x is 0, so any non-zero constant polynomial has degree 0."
            },
            {
                "id": 7,
                "q": "Which of the following is a LINEAR polynomial?",
                "options": ["x² + 1", "3x - 5", "5", "x³ - x"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> A linear polynomial has degree 1. 3x - 5 has highest power 1 on x."
            },
            {
                "id": 8,
                "q": "What is the value of the polynomial P(x) = 2x² - 3x + 4 at x = -2?",
                "options": ["6", "18", "10", "2"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> P(-2) = 2(-2)² - 3(-2) + 4 = 2(4) + 6 + 4 = 8 + 6 + 4 = 18."
            },
            {
                "id": 9,
                "q": "Which expression represents the perimeter of a rectangle with length (2x + 3) and width (x - 1)?",
                "options": ["3x + 2", "6x + 4", "2x² + x - 3", "6x + 8"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Perimeter = 2(length + width) = 2[(2x + 3) + (x - 1)] = 2[3x + 2] = 6x + 4."
            },
            {
                "id": 10,
                "q": "Why is √(2x) + 5 NOT a polynomial in x?",
                "options": [
                    "Because 5 is a constant",
                    "Because x is under the square root, meaning x has exponent 1/2 which is not a whole number",
                    "Because √2 is irrational",
                    "It is a polynomial"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> √(2x) = √2 · x^(1/2). Since the exponent of x is 1/2 (not a whole number), it cannot be a polynomial."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Quiz Challenge • Part 2",
        "subtitle": "Linear Polynomials, Zeroes, Patterns & First Differences",
        "questions": [
            {
                "id": 11,
                "q": "Find the zero of the linear polynomial P(x) = 5x - 20:",
                "options": ["x = -4", "x = 4", "x = 20", "x = 5"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Set P(x) = 0: 5x - 20 = 0 => 5x = 20 => x = 20/5 = 4."
            },
            {
                "id": 12,
                "q": "If x = -2 is a zero of P(x) = kx + 8, what is the value of k?",
                "options": ["k = 4", "k = -4", "k = 8", "k = 2"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Since x = -2 is a zero, P(-2) = 0: k(-2) + 8 = 0 => -2k = -8 => k = 4."
            },
            {
                "id": 13,
                "q": "The first differences of a table with x = 1, 2, 3, 4 are all equal to 7. What does this confirm?",
                "options": [
                    "The relationship is exponential",
                    "The relationship is linear with slope m = 7",
                    "The relationship is quadratic",
                    "The y-intercept is 7"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Constant first differences Δy = 7 indicate a constant rate of change, proving the relationship is linear with slope 7."
            },
            {
                "id": 14,
                "q": "A pattern has outputs 3, 7, 11, 15 for inputs n = 1, 2, 3, 4. What is the nth term formula?",
                "options": ["4n - 1", "4n + 3", "3n + 1", "4n + 1"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> First difference = 7 - 3 = 4. The slope is 4. For n = 1, output is 3: 4(1) + b = 3 => b = -1. Formula: 4n - 1."
            },
            {
                "id": 15,
                "q": "In the linear relationship y = ax, what happens to y when x is tripled?",
                "options": ["y is halved", "y is tripled", "y is squared", "y remains unchanged"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Direct proportionality: if x' = 3x, then y' = a(3x) = 3(ax) = 3y. The output is exactly tripled."
            },
            {
                "id": 16,
                "q": "What is the zero of P(x) = ax + b where a ≠ 0?",
                "options": ["x = b/a", "x = -b/a", "x = -a/b", "x = ab"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> ax + b = 0 => ax = -b => x = -b/a."
            },
            {
                "id": 17,
                "q": "Which table of (x, y) values represents a linear function?",
                "options": [
                    "(1, 2), (2, 4), (3, 8), (4, 16)",
                    "(1, 1), (2, 4), (3, 9), (4, 16)",
                    "(1, 5), (2, 8), (3, 11), (4, 14)",
                    "(1, 2), (2, 5), (3, 10), (4, 17)"
                ],
                "ans": 2,
                "solution": "<strong>Detailed Solution:</strong> For (1,5), (2,8), (3,11), (4,14): Δy = 8-5 = 3, 11-8 = 3, 14-11 = 3 (constant). Thus it is strictly linear."
            },
            {
                "id": 18,
                "q": "What is the zero of the polynomial P(x) = 2x?",
                "options": ["x = 2", "x = 0", "x = -2", "x = 1"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> 2x = 0 => x = 0/2 = 0."
            },
            {
                "id": 19,
                "q": "If P(x) = 3x + 5, what is P(2) + P(-2)?",
                "options": ["10", "22", "0", "16"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> P(2) = 3(2) + 5 = 11. P(-2) = 3(-2) + 5 = -1. Sum = 11 + (-1) = 10."
            },
            {
                "id": 20,
                "q": "The graph of a linear polynomial P(x) = ax + b intersects the x-axis at how many points?",
                "options": ["0 points", "Exactly 1 point", "2 points", "Infinite points"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Because a ≠ 0, it intersects the x-axis at exactly one point: (-b/a, 0)."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Quiz Challenge • Part 3",
        "subtitle": "Linear Growth & Decay Modelling & Word Problems",
        "questions": [
            {
                "id": 21,
                "q": "A plumber charges a ₹200 call-out fee plus ₹150 per hour. Which equation represents total cost C for h hours?",
                "options": [
                    "C = 200h + 150",
                    "C = 150h + 200",
                    "C = 350h",
                    "C = 150h - 200"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Fixed base fee = ₹200 (y-intercept), hourly rate = ₹150 (slope). C = 150h + 200."
            },
            {
                "id": 22,
                "q": "A candle is 30 cm tall and burns down at a rate of 2.5 cm per hour. What is its height H after t hours?",
                "options": [
                    "H = 2.5t + 30",
                    "H = -2.5t + 30",
                    "H = -2.5t - 30",
                    "H = 30t - 2.5"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Burning down represents decay (negative slope m = -2.5). Initial height = 30 cm. Equation: H = -2.5t + 30."
            },
            {
                "id": 23,
                "q": "For the candle in question 22 (H = -2.5t + 30), how many hours will it take to burn out completely?",
                "options": ["10 hours", "12 hours", "15 hours", "8 hours"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Set H = 0: 0 = -2.5t + 30 => 2.5t = 30 => t = 30 / 2.5 = 12 hours."
            },
            {
                "id": 24,
                "q": "A delivery vehicle starts with 60 liters of diesel and consumes 0.12 liters per kilometer. How much fuel remains after 250 km?",
                "options": ["30 liters", "35 liters", "25 liters", "40 liters"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Fuel model: F(d) = -0.12d + 60. For d = 250: F(250) = -0.12(250) + 60 = -30 + 60 = 30 liters."
            },
            {
                "id": 25,
                "q": "An investment account grows according to A(t) = 500t + 2000, where t is in years. What was the initial deposit?",
                "options": ["₹500", "₹2000", "₹2500", "₹1500"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> The initial deposit is the value at t = 0 (the y-intercept), which is ₹2000."
            },
            {
                "id": 26,
                "q": "In the investment model A(t) = 500t + 2000, how much interest is earned each year?",
                "options": ["₹500", "₹2000", "₹250", "₹1000"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> The annual growth rate is the slope a = ₹500 per year."
            },
            {
                "id": 27,
                "q": "A hot metal bar cools from 400°C at a rate of 15°C per minute. What is the temperature model T(m)?",
                "options": [
                    "T(m) = 15m + 400",
                    "T(m) = -15m + 400",
                    "T(m) = -400m + 15",
                    "T(m) = 400 - m"
                ],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Cooling means negative slope (-15°C/min) with initial temp 400°C: T(m) = -15m + 400."
            },
            {
                "id": 28,
                "q": "A factory produces 40 toys per hour with an initial inventory of 150 toys. How many toys are in stock after 8 hours?",
                "options": ["320", "470", "450", "500"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Model: N(h) = 40h + 150. For h = 8: N(8) = 40(8) + 150 = 320 + 150 = 470 toys."
            },
            {
                "id": 29,
                "q": "Which characteristic is common to BOTH linear growth and linear decay?",
                "options": [
                    "Both have positive slopes",
                    "Both have a strictly constant rate of change",
                    "Both pass through origin",
                    "Both have positive y-intercepts"
                ],
                "ans": 1,
                "explanation": "",
                "solution": "<strong>Detailed Solution:</strong> Both linear growth and decay are defined by straight lines having a constant rate of change (constant slope m)."
            },
            {
                "id": 30,
                "q": "A drone descends from 120 meters altitude at 4 meters per second. When will it land on the ground?",
                "options": ["25 seconds", "30 seconds", "40 seconds", "20 seconds"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Height H(t) = -4t + 120. At landing H = 0: -4t + 120 = 0 => 4t = 120 => t = 30 seconds."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Quiz Challenge • Part 4",
        "subtitle": "Slope, Intercepts, Graphing & Break-Even Analysis",
        "questions": [
            {
                "id": 31,
                "q": "What is the slope and y-intercept of the line 2x + 5y = 10?",
                "options": [
                    "Slope = -2/5, y-intercept = 2",
                    "Slope = 2/5, y-intercept = 10",
                    "Slope = -2, y-intercept = 5",
                    "Slope = 5/2, y-intercept = 2"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Solve for y: 5y = -2x + 10 => y = (-2/5)x + 2. Slope m = -2/5 and y-intercept b = 2."
            },
            {
                "id": 32,
                "q": "What is the x-intercept of the line 4x - 3y = 24?",
                "options": ["(0, -8)", "(6, 0)", "(-6, 0)", "(0, 6)"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Set y = 0: 4x - 3(0) = 24 => 4x = 24 => x = 6. Point: (6, 0)."
            },
            {
                "id": 33,
                "q": "What is the slope of the line passing through (1, -2) and (4, 7)?",
                "options": ["3", "1/3", "-3", "9"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> m = (7 - (-2)) / (4 - 1) = (7 + 2) / 3 = 9 / 3 = 3."
            },
            {
                "id": 34,
                "q": "Which line is PARALLEL to the line y = 4x - 5?",
                "options": ["y = -4x + 1", "y = 4x + 9", "y = (1/4)x - 5", "y = -1/4x"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Two lines are parallel if and only if they have the exact same slope. The slope of y = 4x - 5 is 4; y = 4x + 9 also has slope 4."
            },
            {
                "id": 35,
                "q": "What is the slope of a vertical line parallel to the y-axis?",
                "options": ["0", "1", "-1", "Undefined"],
                "ans": 3,
                "solution": "<strong>Detailed Solution:</strong> For a vertical line, x2 = x1, so run Δx = 0. Division by zero makes the slope undefined."
            },
            {
                "id": 36,
                "q": "A manufacturer has Cost C(x) = 20x + 800 and Revenue R(x) = 60x. What is the break-even quantity x*?",
                "options": ["15 units", "20 units", "25 units", "40 units"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> Set R(x) = C(x): 60x = 20x + 800 => 40x = 800 => x = 800/40 = 20 units."
            },
            {
                "id": 37,
                "q": "At the break-even point in question 36 (x = 20 units), what is the total revenue?",
                "options": ["₹800", "₹1200", "₹1000", "₹1600"],
                "ans": 1,
                "solution": "<strong>Detailed Solution:</strong> R(20) = 60 × 20 = ₹1200 (also C(20) = 20(20) + 800 = ₹1200)."
            },
            {
                "id": 38,
                "q": "If the graph of y = ax + b passes through (0, 3) and (2, 7), what are a and b?",
                "options": [
                    "a = 2, b = 3",
                    "a = 3, b = 2",
                    "a = 4, b = 3",
                    "a = 2, b = -3"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> y-intercept (0, 3) immediately gives b = 3. Using (2, 7): 7 = a(2) + 3 => 2a = 4 => a = 2."
            },
            {
                "id": 39,
                "q": "In which quadrant do the lines y = 2x and y = -x + 6 intersect?",
                "options": [
                    "First Quadrant (positive x, positive y)",
                    "Second Quadrant",
                    "Third Quadrant",
                    "Fourth Quadrant"
                ],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Equate: 2x = -x + 6 => 3x = 6 => x = 2. Then y = 2(2) = 4. The point (2, 4) has x > 0, y > 0, which lies in the First Quadrant."
            },
            {
                "id": 40,
                "q": "What is the equation of the line with slope -3 and passing through the origin (0, 0)?",
                "options": ["y = -3x", "y = -3x + 3", "3x + y = 3", "y = 3x"],
                "ans": 0,
                "solution": "<strong>Detailed Solution:</strong> Slope m = -3, y-intercept b = 0. Using y = mx + b yields y = -3x."
            }
        ]
    }
]


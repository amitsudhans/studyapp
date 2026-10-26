# -*- coding: utf-8 -*-
"""
Class 9 Mathematics Chapter 3: Sequences and Progressions
Competencies: CG-11, C-8.1, CG-9
Complete dataset with 16 content slides, 32 in-slide checkpoints, and 4 dedicated quiz challenge slides (40 questions).
"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "Introduction to Sequences",
        "badge": "Concept 1 • Ordered Numbers",
        "audio_text": "Welcome to Chapter 3: Sequences and Progressions! A sequence is an ordered list of numbers arranged according to a definite rule or pattern. Each number in the sequence is called a term. We write terms as a_1, a_2, a_3, up to a_n, where the subscript indicates the position. Explore how patterns allow us to predict future terms!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">What is a Sequence?</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A <strong>sequence</strong> is an ordered succession of numbers formed according to a specific logical or mathematical rule.
                    </p>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-200">
                        $$\langle a_n \rangle = a_1, a_2, a_3, a_4, \dots, a_n, \dots$$
                        Where $n \in \mathbb{N} = \{1, 2, 3, \dots\}$ represents the <strong>index</strong> or position of the term, and $a_n$ is the $n$-th term.
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">Key Properties of Sequences:</h4>
                    <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                        <li><strong>Order Matters:</strong> $\{2, 4, 6\}$ is fundamentally different from $\{6, 4, 2\}$. In sets order is irrelevant, but in sequences order is essential!</li>
                        <li><strong>Repetition is Allowed:</strong> Terms can repeat, such as the alternating sequence $1, -1, 1, -1, \dots$</li>
                        <li><strong>Finite vs Infinite:</strong> A sequence with a countable end term is <em>finite</em>; one that continues indefinitely is <em>infinite</em>.</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Sequence Generator</h4>
                <div id="sim1_container" class="w-full space-y-3">
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="setSim1Pattern('odds')" class="sim1-btn px-2.5 py-1 text-xs rounded bg-indigo-600 hover:bg-indigo-500 text-white font-medium transition">Odds: $2n-1$</button>
                        <button onclick="setSim1Pattern('evens')" class="sim1-btn px-2.5 py-1 text-xs rounded bg-slate-700 hover:bg-indigo-600 text-white font-medium transition">Evens: $2n$</button>
                        <button onclick="setSim1Pattern('squares')" class="sim1-btn px-2.5 py-1 text-xs rounded bg-slate-700 hover:bg-indigo-600 text-white font-medium transition">Squares: $n^2$</button>
                        <button onclick="setSim1Pattern('triangular')" class="sim1-btn px-2.5 py-1 text-xs rounded bg-slate-700 hover:bg-indigo-600 text-white font-medium transition">Triangular: $\frac{n(n+1)}{2}$</button>
                    </div>
                    <div id="sim1_display" class="flex flex-wrap gap-2 justify-center items-center py-4 bg-slate-950 rounded-lg border border-indigo-500/20 min-h-[90px]">
                        <!-- Populated dynamically -->
                    </div>
                    <div class="text-center text-xs text-slate-400">
                        Rule: <span id="sim1_rule" class="text-amber-300 font-mono font-bold">$a_n = 2n - 1$</span> | Next Term ($a_9$): <span id="sim1_next" class="text-emerald-400 font-bold">17</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the 5th term ($a_5$) of the sequence defined by the pattern $a_n = 3n - 2$?",
                "options": ["11", "13", "15", "17"],
                "ans": 1,
                "explanation": "Substitute $n = 5$ into the rule: $a_5 = 3(5) - 2 = 15 - 2 = 13$."
            },
            {
                "q": "How does a sequence differ fundamentally from a mathematical set?",
                "options": [
                    "A sequence cannot have numbers greater than 100",
                    "In a sequence, order matters and elements can repeat; in a set, order does not matter and elements are unique",
                    "A sequence must always have an infinite number of elements",
                    "A set always has a formula, while a sequence never has one"
                ],
                "ans": 1,
                "explanation": "In a sequence, order is critical ($a_1, a_2 \ne a_2, a_1$) and elements can repeat (e.g., $1, 1, 2, 3$). In standard set theory, $\{1, 2\} = \{2, 1\}$ and elements are unique."
            }
        ]
    },
    {
        "id": 2,
        "title": "Explicit or General Rule of a Sequence",
        "badge": "Concept 2 • Direct Computation",
        "audio_text": "An explicit rule, or general term formula, expresses the n-th term directly as a function of its position n. This means you can compute the hundredth term instantly without having to calculate the ninety-nine terms that come before it. Let us test explicit formulas!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Explicit Rule: $a_n = f(n)$</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        An <strong>explicit formula</strong> (closed-form expression) gives $a_n$ solely in terms of the positive integer index $n$.
                    </p>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-200">
                        <strong>Direct Computation Advantage:</strong> To find $a_{100}$, simply evaluate $f(100)$ directly in $O(1)$ constant mathematical steps!
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-2">Examples of Explicit Rules:</h4>
                    <ul class="text-xs text-slate-300 space-y-2">
                        <li><span class="text-amber-300 font-mono">Linear:</span> $a_n = 4n - 1 \implies 3, 7, 11, 15, \dots$</li>
                        <li><span class="text-amber-300 font-mono">Quadratic:</span> $a_n = n^2 + 1 \implies 2, 5, 10, 17, \dots$</li>
                        <li><span class="text-amber-300 font-mono">Exponential:</span> $a_n = 2^n \implies 2, 4, 8, 16, \dots$</li>
                        <li><span class="text-amber-300 font-mono">Alternating:</span> $a_n = (-1)^n \frac{1}{n} \implies -1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, \dots$</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Explicit Rule Evaluator</h4>
                <div class="space-y-3">
                    <div class="flex items-center justify-between text-xs text-slate-300">
                        <label>Select Formula:</label>
                        <select id="sim2_formula" onchange="updateSim2()" class="bg-slate-800 border border-slate-700 text-indigo-300 text-xs rounded px-2 py-1">
                            <option value="3n-1">a_n = 3n - 1</option>
                            <option value="n2+1">a_n = n² + 1</option>
                            <option value="2^n">a_n = 2^n</option>
                            <option value="frac">a_n = n / (n + 1)</option>
                        </select>
                    </div>
                    <div class="space-y-1">
                        <div class="flex justify-between text-xs text-slate-400">
                            <span>Index $n$:</span>
                            <span id="sim2_n_val" class="text-amber-300 font-bold">5</span>
                        </div>
                        <input id="sim2_n" type="range" min="1" max="20" value="5" oninput="updateSim2()" class="w-full accent-indigo-500">
                    </div>
                    <div class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center space-y-2">
                        <div class="text-xs text-slate-400">Evaluation Step:</div>
                        <div id="sim2_step" class="text-sm text-cyan-300 font-mono">a₅ = 3(5) - 1 = 15 - 1</div>
                        <div class="text-lg text-emerald-400 font-bold font-mono">Result: <span id="sim2_result">14</span></div>
                    </div>
                    <div id="sim2_terms_table" class="text-[11px] text-slate-300 grid grid-cols-5 gap-1 text-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "For the explicit sequence rule $a_n = (-1)^n \cdot (2n + 1)$, what is the value of the 4th term ($a_4$)?",
                "options": ["-9", "9", "-7", "7"],
                "ans": 1,
                "explanation": "Substitute $n = 4$: $a_4 = (-1)^4 \cdot (2(4) + 1) = (+1) \cdot (8 + 1) = 9$."
            },
            {
                "q": "What is the primary computational advantage of an explicit formula over a recursive definition?",
                "options": [
                    "Explicit formulas only work for even numbers",
                    "Any term $a_n$ can be calculated directly in one step without knowing prior terms",
                    "Explicit formulas never have fractions or negative signs",
                    "Recursive formulas can only find the first term"
                ],
                "ans": 1,
                "explanation": "With an explicit formula $a_n = f(n)$, evaluating $a_{1000}$ requires a single substitution $f(1000)$, whereas recursion requires evaluating all 999 previous terms sequentially."
            }
        ]
    },
    {
        "id": 3,
        "title": "Recursive Rule of a Sequence",
        "badge": "Concept 3 • Step-by-Step Generation",
        "audio_text": "A recursive rule defines each new term by using one or more preceding terms. To make it complete, it always requires one or more initial base terms. Famous examples include the Fibonacci sequence, where each term is the sum of the two before it!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Anatomy of a Recursive Rule</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A <strong>recursive formula</strong> specifies two essential components:
                    </p>
                    <ol class="mt-2 text-xs text-slate-300 space-y-2 list-decimal list-inside">
                        <li><strong>Base Case(s):</strong> One or more initial anchor values (e.g., $a_1 = 3$).</li>
                        <li><strong>Recursive Step:</strong> A formula relating $a_n$ to prior terms, like $a_n = a_{n-1} + 5$ for $n \ge 2$.</li>
                    </ol>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-200">
                        <em>Without a base case, the sequence cannot start! It is the seed that sprouts the entire sequence.</em>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">The Fibonacci Sequence (Classic Recursion):</h4>
                    <p class="text-xs text-slate-300">
                        Base cases: $F_1 = 1, F_2 = 1$<br>
                        Recursive equation: $F_n = F_{n-1} + F_{n-2}$ for $n \ge 3$<br>
                        Sequence: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Recursive Stepper</h4>
                <div class="space-y-3">
                    <div class="flex gap-2 justify-center">
                        <button onclick="setSim3Rule('ap')" class="sim3-btn px-2.5 py-1 text-xs rounded bg-indigo-600 text-white font-medium">AP Step: $a_n = a_{n-1} + 3$</button>
                        <button onclick="setSim3Rule('gp')" class="sim3-btn px-2.5 py-1 text-xs rounded bg-slate-700 text-white font-medium">GP Step: $a_n = 2a_{n-1}$</button>
                        <button onclick="setSim3Rule('fib')" class="sim3-btn px-2.5 py-1 text-xs rounded bg-slate-700 text-white font-medium">Fibonacci: $F_{n-1}+F_{n-2}$</button>
                    </div>
                    <div id="sim3_callstack" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 min-h-[140px] space-y-1 font-mono text-xs">
                        <!-- Populated by JS -->
                    </div>
                    <div class="flex justify-between items-center">
                        <button onclick="stepSim3()" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded text-xs font-bold transition flex items-center gap-1">
                            <span>▶ Compute Next Term</span>
                        </button>
                        <button onclick="resetSim3()" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-white rounded text-xs font-medium transition">
                            Reset
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Given the recursive rule $a_1 = 4$ and $a_n = 2a_{n-1} - 1$ for $n \\ge 2$, what is the 3rd term ($a_3$)?",
                "options": ["7", "13", "14", "15"],
                "ans": 1,
                "explanation": "Compute step-by-step: $a_1 = 4$. Next, $a_2 = 2(4) - 1 = 7$. Then, $a_3 = 2(7) - 1 = 14 - 1 = 13$."
            },
            {
                "q": "Why does every valid recursive definition require at least one base case?",
                "options": [
                    "To prevent infinite regression with no starting numerical value",
                    "Because mathematics only allows positive numbers",
                    "To ensure the common difference is zero",
                    "Because computers cannot calculate negative powers"
                ],
                "ans": 0,
                "explanation": "Without a base case, $a_n$ would refer back to $a_{n-1}$, which refers to $a_{n-2}$ indefinitely, leaving the sequence undefined."
            }
        ]
    },
    {
        "id": 4,
        "title": "Generating Terms: Recursive vs Explicit Rules",
        "badge": "Concept 4 • Rule Translation",
        "audio_text": "Both explicit and recursive rules can describe the exact same sequence. Understanding how to transition between them is a powerful skill in computational thinking and algebraic reasoning. Let us compare them side by side!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Two Perspectives, Same Sequence</h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-xs text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="py-2">Feature</th>
                                    <th class="py-2 text-indigo-400">Explicit ($a_n = f(n)$)</th>
                                    <th class="py-2 text-amber-400">Recursive ($a_n = g(a_{n-1})$)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr>
                                    <td class="py-2 font-medium">To find $a_{100}$</td>
                                    <td class="py-2 text-indigo-300 font-semibold">1 step: evaluate $f(100)$</td>
                                    <td class="py-2 text-amber-300">99 steps: must know $a_{99}$</td>
                                </tr>
                                <tr>
                                    <td class="py-2 font-medium">Definition</td>
                                    <td class="py-2">Global formula based on index $n$</td>
                                    <td class="py-2">Local step from previous term</td>
                                </tr>
                                <tr>
                                    <td class="py-2 font-medium">Computational Cost</td>
                                    <td class="py-2 text-emerald-400">$O(1)$ constant time</td>
                                    <td class="py-2 text-rose-400">$O(n)$ linear time</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-2">Converting a Rule:</h4>
                    <p class="text-xs text-slate-300">
                        Suppose $a_1 = 5$ and $a_n = a_{n-1} + 4$.<br>
                        $a_1 = 5$<br>
                        $a_2 = 5 + 4$<br>
                        $a_3 = 5 + 4 + 4 = 5 + 2(4)$<br>
                        $a_n = 5 + (n - 1)4 = 4n + 1$ (Explicit formula!)
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Complexity Race</h4>
                <div class="space-y-3">
                    <div class="text-xs text-slate-300 text-center">
                        Target Term: <span id="sim4_target" class="text-amber-300 font-bold">a₁₀</span>
                    </div>
                    <div class="flex justify-center gap-2">
                        <button onclick="runSim4Race(10)" class="px-2.5 py-1 text-xs rounded bg-indigo-600 text-white font-medium">Test n = 10</button>
                        <button onclick="runSim4Race(50)" class="px-2.5 py-1 text-xs rounded bg-slate-700 text-white font-medium">Test n = 50</button>
                        <button onclick="runSim4Race(100)" class="px-2.5 py-1 text-xs rounded bg-slate-700 text-white font-medium">Test n = 100</button>
                    </div>
                    <div class="space-y-3 p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs">
                        <div>
                            <div class="flex justify-between text-indigo-300 mb-1">
                                <span>Explicit Method: $a_n = 4n + 1$</span>
                                <span id="sim4_exp_steps">1 operation</span>
                            </div>
                            <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden">
                                <div id="sim4_exp_bar" class="bg-indigo-500 h-full w-[10%] transition-all duration-300"></div>
                            </div>
                        </div>
                        <div>
                            <div class="flex justify-between text-amber-300 mb-1">
                                <span>Recursive Method: $a_n = a_{n-1} + 4$</span>
                                <span id="sim4_rec_steps">10 operations</span>
                            </div>
                            <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden">
                                <div id="sim4_rec_bar" class="bg-amber-500 h-full w-[100%] transition-all duration-300"></div>
                            </div>
                        </div>
                        <div id="sim4_summary" class="text-center text-emerald-400 font-semibold pt-1">
                            Explicit calculated $a_{10} = 41$ in 1 direct computation!
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the explicit form of the sequence defined recursively by $a_1 = 7$ and $a_n = a_{n-1} + 3$?",
                "options": ["a_n = 3n + 4", "a_n = 3n + 7", "a_n = 7n + 3", "a_n = 4n + 3"],
                "ans": 0,
                "explanation": "Notice $a_n = a_1 + (n-1)d = 7 + (n-1)3 = 7 + 3n - 3 = 3n + 4$. For $n=1$, $3(1)+4=7$, and each step adds 3."
            },
            {
                "q": "If a sequence has the explicit formula $a_n = 5n - 2$, what is its equivalent recursive definition for $n \\ge 2$?",
                "options": [
                    "a_1 = 3, a_n = a_{n-1} + 5",
                    "a_1 = 5, a_n = a_{n-1} - 2",
                    "a_1 = 3, a_n = 5a_{n-1}",
                    "a_1 = -2, a_n = a_{n-1} + 5"
                ],
                "ans": 0,
                "explanation": "First term $a_1 = 5(1) - 2 = 3$. The rate of change is 5, so each new term is the previous term plus 5: $a_n = a_{n-1} + 5$."
            }
        ]
    },
    {
        "id": 5,
        "title": "Arithmetic Progressions (AP): Definition & Common Difference",
        "badge": "Concept 5 • Linear Step Pattern",
        "audio_text": "An Arithmetic Progression, or AP, is a sequence in which the difference between any two consecutive terms is always constant. This constant value is known as the common difference, represented by the letter d. If d is positive, the AP grows; if d is negative, the AP decays!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Formal Definition of an AP</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A sequence $a_1, a_2, a_3, \dots, a_n$ is called an <strong>Arithmetic Progression (AP)</strong> if there exists a constant $d$ such that:
                    </p>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$d = a_{k+1} - a_k \quad \text{for all } k \ge 1$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        $a$ (or $a_1$) is the <strong>first term</strong>, and $d$ is the <strong>common difference</strong>.
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-2">Three Types of Common Difference:</h4>
                    <ul class="text-xs text-slate-300 space-y-2">
                        <li><span class="text-emerald-400 font-bold">$d > 0$ (Increasing AP):</span> $2, 7, 12, 17, \dots$ ($d = +5$)</li>
                        <li><span class="text-rose-400 font-bold">$d < 0$ (Decreasing AP):</span> $20, 16, 12, 8, \dots$ ($d = -4$)</li>
                        <li><span class="text-slate-400 font-bold">$d = 0$ (Constant AP):</span> $7, 7, 7, 7, \dots$ ($d = 0$)</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Common Difference Scanner</h4>
                <div class="space-y-3">
                    <p class="text-xs text-slate-400 text-center">Click a test sequence to calculate all consecutive differences:</p>
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="scanSim5([3, 7, 11, 15, 19])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-slate-200">3, 7, 11, 15, 19</button>
                        <button onclick="scanSim5([20, 15, 10, 5, 0])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-slate-200">20, 15, 10, 5, 0</button>
                        <button onclick="scanSim5([2, 4, 8, 16, 32])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-rose-600 text-slate-200">2, 4, 8, 16, 32</button>
                    </div>
                    <div id="sim5_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated dynamically -->
                    </div>
                    <div id="sim5_verdict" class="text-center font-bold text-xs"></div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the common difference $d$ of the AP: $-5, -1, 3, 7, 11, \\dots$?",
                "options": ["-4", "4", "-6", "6"],
                "ans": 1,
                "explanation": "Calculate $d = a_2 - a_1 = (-1) - (-5) = -1 + 5 = 4$."
            },
            {
                "q": "Which of the following sequences is NOT an Arithmetic Progression?",
                "options": [
                    "10, 20, 30, 40",
                    "1, 4, 9, 16",
                    "-2, -4, -6, -8",
                    "5, 5, 5, 5"
                ],
                "ans": 1,
                "explanation": "In $1, 4, 9, 16$, the differences are $4-1=3$, $9-4=5$, $16-9=7$. Since the difference is not constant, it is not an AP (it is a sequence of perfect squares)."
            }
        ]
    },
    {
        "id": 6,
        "title": "The n-th Term of an AP",
        "badge": "Concept 6 • Formula Derivation",
        "audio_text": "How do we find the n-th term of an AP? Starting from the first term a, we add the common difference d once to get the second term, twice to get the third term, and so on. Therefore, to reach the n-th term, we add d exactly n minus 1 times! Thus, a_n = a + (n - 1)d.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Step-by-Step Derivation</h3>
                    <div class="text-xs text-slate-300 space-y-1 font-mono">
                        <div>$a_1 = a = a + (1 - 1)d$</div>
                        <div>$a_2 = a + d = a + (2 - 1)d$</div>
                        <div>$a_3 = (a + d) + d = a + 2d = a + (3 - 1)d$</div>
                        <div>$a_4 = (a + 2d) + d = a + 3d = a + (4 - 1)d$</div>
                    </div>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-center">
                        <span class="text-sm font-bold text-emerald-400 font-mono">$$a_n = a + (n - 1)d$$</span>
                        <p class="text-[11px] text-slate-400 mt-1">Four variables: $a_n$ ($n$-th term), $a$ (first term), $n$ (position), $d$ (common difference).</p>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">Solving for Missing Variables:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        If any 3 of the 4 quantities $\{a_n, a, n, d\}$ are known, the fourth can always be determined algebraically using linear equation principles.
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive AP n-th Term Sandbox</h4>
                <div class="space-y-3">
                    <div class="grid grid-cols-3 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">First Term $a$:</label>
                            <input id="sim6_a" type="number" value="3" onchange="updateSim6()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Difference $d$:</label>
                            <input id="sim6_d" type="number" value="4" onchange="updateSim6()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Term $n$:</label>
                            <input id="sim6_n" type="number" min="1" max="100" value="10" onchange="updateSim6()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-emerald-300">
                        </div>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center space-y-1">
                        <div class="text-xs text-slate-400">Decomposition:</div>
                        <div id="sim6_breakdown" class="text-xs text-indigo-200 font-mono">a₁₀ = 3 + (10 - 1) × 4 = 3 + 9 × 4 = 3 + 36</div>
                        <div class="text-xl text-emerald-400 font-bold font-mono">aₙ = <span id="sim6_ans">39</span></div>
                    </div>
                    <div id="sim6_visual_line" class="flex items-center justify-center gap-1 overflow-x-auto py-2">
                        <!-- Step blocks generated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Find the 21st term ($a_{21}$) of the AP: $4, 9, 14, 19, \\dots$",
                "options": ["104", "109", "100", "95"],
                "ans": 0,
                "explanation": "Here $a = 4$ and $d = 9 - 4 = 5$. Using $a_n = a + (n - 1)d$: $a_{21} = 4 + (21 - 1) \times 5 = 4 + 20 \times 5 = 4 + 100 = 104$."
            },
            {
                "q": "Which term of the AP $3, 8, 13, 18, \\dots$ is equal to 78?",
                "options": ["14th", "15th", "16th", "17th"],
                "ans": 2,
                "explanation": "Set $a_n = 78$, $a = 3$, $d = 5$. Then $78 = 3 + (n - 1)5 \implies 75 = (n - 1)5 \implies n - 1 = 15 \implies n = 16$."
            }
        ]
    },
    {
        "id": 7,
        "title": "Visualising an AP Graphically",
        "badge": "Concept 7 • Discrete Linear Points",
        "audio_text": "When we plot the terms of an Arithmetic Progression against their position index n on a Cartesian plane, an amazing geometric truth emerges: all points lie in a perfectly straight line! The slope of this line is exactly equal to the common difference d.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Linear Geometry of an AP</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        Notice how the $n$-th term formula $a_n = a + (n - 1)d$ can be rewritten as:
                    </p>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs font-mono text-center text-cyan-300">
                        $$a_n = d \cdot n + (a - d)$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        Comparing this to the linear equation $y = mx + c$:
                    </p>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside mt-2">
                        <li>The independent variable $x$ corresponds to index $n$ ($n \in \mathbb{N}$).</li>
                        <li>The slope $m$ corresponds to the common difference $d$.</li>
                        <li>Because $n$ can only take discrete integer values ($1, 2, 3, \dots$), the graph consists of <strong>isolated collinear points</strong>.</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Slope Interpretation:</h4>
                    <p class="text-xs text-slate-300">
                        $$\text{Slope} = \frac{\Delta y}{\Delta x} = \frac{a_{n+1} - a_n}{(n+1) - n} = \frac{d}{1} = d$$
                        Steeper line $\implies$ larger common difference $d$!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive AP Cartesian Plotter</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Slope ($d$): <span id="sim7_d_val" class="text-cyan-300 font-bold">2</span></label>
                        <input id="sim7_d" type="range" min="-3" max="5" value="2" oninput="drawSim7()" class="w-32 accent-indigo-500">
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim7_svg" viewBox="0 0 320 200" class="w-full h-48">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div class="text-[11px] text-center text-slate-400">
                        Points $(n, a_n)$ form a discrete linear lattice with slope $m = d$.
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Why is the graph of an Arithmetic Progression represented as isolated dots rather than a solid unbroken line?",
                "options": [
                    "Because paper cannot hold continuous lines",
                    "Because the domain of a sequence is restricted to discrete positive integers $n \\in \\{1, 2, 3, \\dots\\}$",
                    "Because the common difference must always be an integer",
                    "Because negative values are not allowed in coordinates"
                ],
                "ans": 1,
                "explanation": "A sequence is a function whose domain is the set of natural numbers $\\mathbb{N}$. Since indices like $n=1.5$ do not exist, the graph consists of discrete points $(n, a_n)$."
            },
            {
                "q": "If the graph of an AP has points $(1, 5)$ and $(4, 14)$, what is the slope of the line passing through them (the common difference $d$)?",
                "options": ["2", "3", "4", "5"],
                "ans": 1,
                "explanation": "The slope $d = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{14 - 5}{4 - 1} = \\frac{9}{3} = 3$."
            }
        ]
    },
    {
        "id": 8,
        "title": "Practical Contexts Leading to APs",
        "badge": "Concept 8 • Real-World Applications",
        "audio_text": "Arithmetic progressions surround us in the real world whenever something grows or decreases by a fixed amount at each regular interval. From rows of seats in a stadium to depreciating machinery, ladder rungs, and monthly savings plans, APs model linear everyday situations.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Everyday Scenarios Modelled by APs</h3>
                    <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                        <li><strong>Stadium Seating:</strong> Row 1 has 30 seats; each subsequent row adds 4 extra seats due to wider radius ($a = 30, d = 4$).</li>
                        <li><strong>Salary Increments:</strong> Starting salary ₹40,000 with a guaranteed fixed annual increment of ₹3,000 ($a = 40000, d = 3000$).</li>
                        <li><strong>Taxi Fares:</strong> ₹50 for the first kilometre, plus ₹15 for each additional kilometre ($a = 50, d = 15$).</li>
                        <li><strong>Ladder Construction:</strong> Bottom rung is 45 cm wide, decreasing uniformly by 2 cm per rung up to the top ($a = 45, d = -2$).</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">Model Formulation Checklist:</h4>
                    <ol class="text-xs text-slate-300 space-y-1 list-decimal list-inside">
                        <li>Identify initial baseline value ($a$).</li>
                        <li>Verify that step change is <em>constant</em> (fixed addition/subtraction $\implies d$).</li>
                        <li>Identify desired stage or row ($n$).</li>
                        <li>Apply $a_n = a + (n - 1)d$.</li>
                    </ol>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Stadium Seating Simulator</h4>
                <div class="space-y-3">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Row 1 Seats ($a$):</label>
                            <input id="sim8_a" type="number" value="20" onchange="drawSim8()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Extra Seats/Row ($d$):</label>
                            <input id="sim8_d" type="number" value="4" onchange="drawSim8()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim8_svg" viewBox="0 0 300 160" class="w-full h-40">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div id="sim8_info" class="text-center text-xs text-emerald-400 font-semibold">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "A student saves ₹100 in January and increases their monthly savings by ₹50 each subsequent month. How much will they save in December (the 12th month)?",
                "options": ["₹600", "₹650", "₹700", "₹750"],
                "ans": 1,
                "explanation": "Here $a = 100$, $d = 50$, and $n = 12$. Savings in month 12 = $a_{12} = 100 + (12 - 1) \times 50 = 100 + 11 \times 50 = 100 + 550 = ₹650$."
            },
            {
                "q": "A carpenter makes a ladder whose bottom rung is 45 cm wide and top rung is 25 cm wide. If there are 11 rungs, what is the decrease in width per rung ($d$)?",
                "options": ["-1.5 cm", "-2 cm", "-2.5 cm", "-3 cm"],
                "ans": 1,
                "explanation": "$a_1 = 45$, $a_{11} = 25$, $n = 11$. $25 = 45 + (11 - 1)d \implies -20 = 10d \implies d = -2$ cm."
            }
        ]
    },
    {
        "id": 9,
        "title": "Sum of the First n Natural Numbers",
        "badge": "Concept 9 • Gauss's Masterpiece",
        "audio_text": "How do we add the first n natural numbers? Legend has it that young Carl Friedrich Gauss solved this in seconds by pairing numbers from opposite ends: 1 plus 100 is 101, 2 plus 99 is 101, and so forth! Geometrically, two copies of a staircase of dots fit together into an n by n plus 1 rectangle. Thus, S_n equals n times n plus 1 divided by 2.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Gauss's Pairing Method</h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Let $S_n = 1 + 2 + 3 + \dots + n$. Write the sum forward and backward:
                    </p>
                    <div class="mt-2 p-2 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-[11px] font-mono text-slate-200">
                        $$S_n = 1 + 2 + \dots + (n-1) + n$$
                        $$S_n = n + (n-1) + \dots + 2 + 1$$
                        $$\overline{2S_n = (n+1) + (n+1) + \dots + (n+1) \quad [n \text{ times}]}$$
                        $$2S_n = n(n+1) \implies S_n = \frac{n(n+1)}{2}$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Triangular Numbers:</h4>
                    <p class="text-xs text-slate-300">
                        Numbers of the form $T_n = \frac{n(n+1)}{2}$ are called <strong>triangular numbers</strong> because they represent the number of dots needed to form an equilateral triangle: $1, 3, 6, 10, 15, 21, \dots$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Gauss Rectangle Visualizer</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Value of $n$: <span id="sim9_n_val" class="text-amber-300 font-bold">5</span></label>
                        <input id="sim9_n" type="range" min="2" max="8" value="5" oninput="drawSim9()" class="w-32 accent-indigo-500">
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim9_svg" viewBox="0 0 280 160" class="w-full h-40">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs w-full px-2">
                        <button onclick="toggleSim9Double()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-[11px]">
                            Toggle Second Staircase
                        </button>
                        <div id="sim9_calc" class="text-emerald-400 font-mono font-bold text-xs">S₅ = 5(6)/2 = 15</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the sum of the first 50 natural numbers ($1 + 2 + 3 + \\dots + 50$)?",
                "options": ["1225", "1250", "1275", "1300"],
                "ans": 2,
                "explanation": "Use Gauss's formula: $S_{50} = \\frac{50(50 + 1)}{2} = 25 \\times 51 = 1275$."
            },
            {
                "q": "If the sum of the first $n$ natural numbers is 210, what is the value of $n$?",
                "options": ["19", "20", "21", "22"],
                "ans": 1,
                "explanation": "Set $\\frac{n(n+1)}{2} = 210 \\implies n(n+1) = 420$. Since $20 \\times 21 = 420$, $n = 20$."
            }
        ]
    },
    {
        "id": 10,
        "title": "Geometric Progressions (GP): Definition & Common Ratio",
        "badge": "Concept 10 • Multiplicative Scaling",
        "audio_text": "While an AP grows by adding a constant, a Geometric Progression, or GP, grows by multiplying by a constant! This multiplying factor is called the common ratio, denoted by r. If r is greater than 1, terms explode rapidly; if r is between 0 and 1, terms decay toward zero.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Formal Definition of a GP</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A sequence $a_1, a_2, a_3, \dots, a_n$ is called a <strong>Geometric Progression (GP)</strong> with non-zero terms if:
                    </p>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$r = \frac{a_{k+1}}{a_k} \quad \text{for all } k \ge 1 \quad (a_k \ne 0, r \ne 0)$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        $a$ is the <strong>first term</strong> and $r$ is the <strong>common ratio</strong>.
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-2">Behavior of Common Ratio $r$:</h4>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><span class="text-emerald-400 font-bold">$r > 1$:</span> Rapid exponential growth ($2, 6, 18, 54, \dots$ with $r=3$)</li>
                        <li><span class="text-cyan-400 font-bold">$0 < r < 1$:</span> Exponential decay ($64, 32, 16, 8, \dots$ with $r=\frac{1}{2}$)</li>
                        <li><span class="text-rose-400 font-bold">$r < 0$:</span> Alternating signs ($3, -6, 12, -24, \dots$ with $r=-2$)</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Common Ratio Scanner</h4>
                <div class="space-y-3">
                    <p class="text-xs text-slate-400 text-center">Select a candidate sequence to verify its ratio constancy:</p>
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="scanSim10([2, 6, 18, 54, 162])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-slate-200">2, 6, 18, 54, 162</button>
                        <button onclick="scanSim10([100, 50, 25, 12.5])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-slate-200">100, 50, 25, 12.5</button>
                        <button onclick="scanSim10([2, 4, 6, 8, 10])" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-rose-600 text-slate-200">2, 4, 6, 8, 10 (AP!)</button>
                    </div>
                    <div id="sim10_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                    <div id="sim10_verdict" class="text-center font-bold text-xs"></div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the common ratio $r$ of the Geometric Progression: $5, -10, 20, -40, \\dots$?",
                "options": ["2", "-2", "0.5", "-0.5"],
                "ans": 1,
                "explanation": "Compute ratio $r = \\frac{a_2}{a_1} = \\frac{-10}{5} = -2$. Verify: $20 / (-10) = -2$."
            },
            {
                "q": "What distinguishes an AP from a GP fundamentally?",
                "options": [
                    "An AP uses subtraction, a GP uses division",
                    "An AP has a constant difference obtained by addition, while a GP has a constant ratio obtained by multiplication",
                    "A GP only works with negative numbers",
                    "An AP is always finite, while a GP is always infinite"
                ],
                "ans": 1,
                "explanation": "An AP steps forward by repeatedly adding $d$ ($a_{k+1} = a_k + d$), whereas a GP steps forward by repeatedly multiplying by $r$ ($a_{k+1} = a_k \\cdot r$)."
            }
        ]
    },
    {
        "id": 11,
        "title": "The n-th Term of a GP",
        "badge": "Concept 11 • Exponential Formula",
        "audio_text": "To find the n-th term of a Geometric Progression, we multiply the first term a by the common ratio r repeatedly. For the second term, we multiply once; for the third term, twice; and for the n-th term, we multiply by r exactly n minus 1 times! Thus, a_n = a times r to the power n minus 1.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Derivation of the GP n-th Term</h3>
                    <div class="text-xs text-slate-300 space-y-1 font-mono">
                        <div>$a_1 = a = a \cdot r^{1 - 1} = a \cdot r^0$</div>
                        <div>$a_2 = a \cdot r = a \cdot r^{2 - 1}$</div>
                        <div>$a_3 = (a \cdot r) \cdot r = a \cdot r^2 = a \cdot r^{3 - 1}$</div>
                        <div>$a_4 = (a \cdot r^2) \cdot r = a \cdot r^3 = a \cdot r^{4 - 1}$</div>
                    </div>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-center">
                        <span class="text-sm font-bold text-emerald-400 font-mono">$$a_n = a \cdot r^{n - 1}$$</span>
                        <p class="text-[11px] text-slate-400 mt-1">Four variables: $a_n$ ($n$-th term), $a$ (first term), $r$ (ratio), $n$ (position).</p>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">Exponential Explosion Warning:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Even modest common ratios produce enormous values very quickly. If $a = 1$ and $r = 2$, by term 30, $a_{30} = 2^{29} = 536,870,912$ (over half a billion)!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive GP n-th Term Sandbox</h4>
                <div class="space-y-3">
                    <div class="grid grid-cols-3 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">First Term $a$:</label>
                            <input id="sim11_a" type="number" value="2" onchange="updateSim11()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Ratio $r$:</label>
                            <input id="sim11_r" type="number" step="0.5" value="3" onchange="updateSim11()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Term $n$:</label>
                            <input id="sim11_n" type="number" min="1" max="15" value="6" onchange="updateSim11()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-emerald-300">
                        </div>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center space-y-1">
                        <div class="text-xs text-slate-400">Formula Breakdown:</div>
                        <div id="sim11_breakdown" class="text-xs text-indigo-200 font-mono">a₆ = 2 × 3^(6 - 1) = 2 × 3⁵ = 2 × 243</div>
                        <div class="text-xl text-emerald-400 font-bold font-mono">aₙ = <span id="sim11_ans">486</span></div>
                    </div>
                    <div id="sim11_visual_bars" class="flex items-end justify-center gap-1.5 h-24 pt-2">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the 6th term ($a_6$) of the GP: $3, 6, 12, 24, \\dots$?",
                "options": ["48", "96", "192", "384"],
                "ans": 1,
                "explanation": "Here $a = 3$ and $r = 6 / 3 = 2$. $a_6 = 3 \\cdot 2^{6 - 1} = 3 \\cdot 2^5 = 3 \\cdot 32 = 96$."
            },
            {
                "q": "In a GP, the 3rd term is 24 and the 6th term is 192. What is the common ratio $r$?",
                "options": ["2", "3", "4", "8"],
                "ans": 0,
                "explanation": "$\\frac{a_6}{a_3} = \\frac{a r^5}{a r^2} = r^3$. So $r^3 = \\frac{192}{24} = 8 \\implies r = 2$."
            }
        ]
    },
    {
        "id": 12,
        "title": "Visualising a GP & Linear vs Exponential Growth",
        "badge": "Concept 12 • The Great Growth Race",
        "audio_text": "How do AP and GP compare visually? An AP grows along a straight line with constant slope, while a GP curves upward exponentially! Even if an AP starts with a large lead, an exponential GP with a ratio greater than 1 will eventually overtake it and leave it far behind.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Linear vs Exponential Growth</h3>
                    <div class="overflow-x-auto text-xs">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="py-1">Feature</th>
                                    <th class="py-1 text-cyan-400">AP (Linear)</th>
                                    <th class="py-1 text-amber-400">GP (Exponential)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr>
                                    <td class="py-1.5 font-medium">Formula</td>
                                    <td class="py-1.5 font-mono">$a_n = a + (n-1)d$</td>
                                    <td class="py-1.5 font-mono">$a_n = a \cdot r^{n-1}$</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-medium">Rate of Growth</td>
                                    <td class="py-1.5">Constant rate ($+d$ per step)</td>
                                    <td class="py-1.5">Proportional to current size ($\times r$)</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-medium">Graph Shape</td>
                                    <td class="py-1.5">Collinear straight line</td>
                                    <td class="py-1.5">Convex exponential curve</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">The Crossover Principle:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        No matter how large the constant difference $d$ of an AP is, an exponential GP with ratio $r > 1$ will <em>always</em> eventually surpass it for sufficiently large $n$!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Growth Battle: AP vs GP</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="text-cyan-400 font-mono">AP: a=20, d=10</span>
                        <span class="text-amber-400 font-mono">GP: a=2, r=2</span>
                        <div class="flex items-center gap-1">
                            <label class="text-slate-400">Step $n$:</label>
                            <span id="sim12_n_val" class="text-emerald-400 font-bold">1</span>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim12_svg" viewBox="0 0 300 150" class="w-full h-36">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="stepSim12()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-xs">
                            ▶ Step Next Round
                        </button>
                        <button onclick="resetSim12()" class="px-2 py-1 bg-slate-700 rounded text-slate-300 text-xs">
                            Reset
                        </button>
                        <div id="sim12_status" class="text-slate-300 text-[11px] font-semibold"></div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Consider AP: $a_n = 100 + 10(n-1)$ and GP: $g_n = 2 \\times 2^{n-1}$. At which step does the GP first surpass the AP?",
                "options": ["n = 5", "n = 6", "n = 7", "n = 8"],
                "ans": 2,
                "explanation": "At $n=6$: AP = $100 + 50 = 150$, GP = $2 \\times 32 = 64$ (AP still leads). At $n=7$: AP = $100 + 60 = 160$, GP = $2 \\times 64 = 128$. At $n=8$: AP = $100 + 70 = 170$, GP = $2 \\times 128 = 256$ (GP takes huge lead!)."
            },
            {
                "q": "What happens to the graph of a GP $a_n = a \\cdot r^{n-1}$ when $0 < r < 1$?",
                "options": [
                    "It becomes a straight vertical line",
                    "It exhibits asymptotic decay, approaching the horizontal axis ($y = 0$) as $n$ grows",
                    "It oscillates between positive and negative infinity",
                    "It forms a closed circle"
                ],
                "ans": 1,
                "explanation": "When $0 < r < 1$, multiplying repeatedly by a fraction reduces the value closer and closer to 0, producing asymptotic decay towards the axis."
            }
        ]
    },
    {
        "id": 13,
        "title": "Practical Contexts Leading to GPs",
        "badge": "Concept 13 • Exponential Real World",
        "audio_text": "Geometric progressions govern physical and biological phenomena whenever growth or decay depends on the quantity currently present. Examples include cellular mitosis where cells double every generation, bouncing balls that rebound to a fraction of their previous height, and depreciation of assets.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Real-Life GP Phenomena</h3>
                    <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                        <li><strong>Bacterial Fission:</strong> A single bacterium splits into 2, then 4, 8, 16... Every generation multiplies by $r = 2$.</li>
                        <li><strong>Bouncing Ball:</strong> A ball dropped from 100 cm rebounds to $70\\%$ of its height on each bounce ($a = 100, r = 0.70$).</li>
                        <li><strong>Compound Interest:</strong> Money invested at interest rate $i$ compounded annually multiplies by $r = (1 + i)$ each year.</li>
                        <li><strong>Machine Depreciation:</strong> A car loses $15\\%$ of its market value annually; each year its value is $85\\%$ of previous year ($r = 0.85$).</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-1">Modeling Half-Life:</h4>
                    <p class="text-xs text-slate-300">
                        Radioactive decay follows a GP with common ratio $r = 0.5$. After $n$ half-lives, the remaining mass is $M_n = M_0 \cdot (0.5)^n$.
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Bouncing Ball Simulator</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Rebound Factor ($r$): <span id="sim13_r_val" class="text-amber-300 font-bold">0.75</span></label>
                        <input id="sim13_r" type="range" min="0.5" max="0.85" step="0.05" value="0.75" oninput="runSim13()" class="w-32 accent-indigo-500">
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim13_svg" viewBox="0 0 300 140" class="w-full h-36">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim13_table" class="text-center text-[11px] text-slate-300 font-mono">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "A tennis ball is dropped from a height of 200 cm. After each bounce, it rebounds to $\\frac{3}{4}$ of its previous height. What is the height reached after the 3rd bounce?",
                "options": ["84.375 cm", "112.5 cm", "150 cm", "63.28 cm"],
                "ans": 0,
                "explanation": "Here $a = 200 \\times \\frac{3}{4} = 150$ cm (1st bounce height), $r = \\frac{3}{4}$. The 3rd bounce is $a_3 = 200 \\times (\\frac{3}{4})^3 = 200 \\times \\frac{27}{64} = \\frac{5400}{64} = 84.375$ cm."
            },
            {
                "q": "A culture starts with 50 bacteria. If the population triples every hour ($r = 3$), how many bacteria are present after 5 hours?",
                "options": ["4050", "12150", "36450", "1500"],
                "ans": 1,
                "explanation": "Initial count is $a_0 = 50$. After 5 hours, the count is $50 \\times 3^5 = 50 \\times 243 = 12,150$ bacteria."
            }
        ]
    },
    {
        "id": 14,
        "title": "Applications of GP in Fractals",
        "badge": "Concept 14 • Self-Similar Geometry",
        "audio_text": "Fractals are infinitely complex geometric patterns that look self-similar across different scales. Geometric Progressions are the mathematical engine behind fractals! In the Koch Snowflake, the perimeter forms an infinite GP that grows without bound, while its area remains strictly bounded. Let us explore the Sierpinski Triangle and Koch Snowflake!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Koch Snowflake Fractal</h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Start with an equilateral triangle of side $s$. In each iteration, replace the middle third of every segment with two segments of length $s/3$ forming a triangular spike.
                    </p>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1">
                        <div>Number of segments: $N_n = 3 \cdot 4^n$ (GP with $r = 4$)</div>
                        <div>Segment length: $L_n = s \cdot (1/3)^n$ (GP with $r = 1/3$)</div>
                        <div class="text-amber-300 font-bold">Total Perimeter: $P_n = 3s \cdot (4/3)^n$ (GP with $r = 4/3 > 1$)</div>
                    </div>
                    <p class="text-[11px] text-emerald-400 mt-2">
                        ★ <em>Mind-Bending Paradox:</em> The perimeter grows to infinity as $n \to \infty$, yet the area remains finite, bounded inside a circle!
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-1">Sierpinski Triangle:</h4>
                    <p class="text-xs text-slate-300">
                        Remove the inverted middle triangle at each step. At iteration $n$, the remaining shaded area is $A_n = A_0 \cdot (3/4)^n$, which decays to zero as $n \to \infty$!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Fractal Explorer</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <div class="flex gap-2">
                            <button onclick="setSim14Type('koch')" class="sim14-btn px-2 py-0.5 rounded bg-indigo-600 text-white text-[11px]">Koch Snowflake</button>
                            <button onclick="setSim14Type('sierpinski')" class="sim14-btn px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]">Sierpinski</button>
                        </div>
                        <div class="flex items-center gap-1">
                            <span class="text-slate-400">Iteration:</span>
                            <span id="sim14_iter_val" class="text-amber-300 font-bold">0</span>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim14_svg" viewBox="0 0 260 200" class="w-full h-44">
                            <!-- Fractal rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="stepSim14()" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-500 rounded text-white text-xs font-semibold">
                            ▶ Next Iteration
                        </button>
                        <div id="sim14_stats" class="text-[11px] text-slate-300 font-mono">Segments: 3 | Perimeter: 3s</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "In the Koch Snowflake, by what factor does the total perimeter multiply at each iteration?",
                "options": ["4/3", "3/4", "3", "4"],
                "ans": 0,
                "explanation": "Every segment is replaced by 4 segments, each of length $1/3$ of the original. The perimeter multiplies by $4 \\times (1/3) = 4/3$ at each step."
            },
            {
                "q": "In the Sierpinski Triangle, what is the remaining area ratio after 3 iterations if the initial area is $A_0$?",
                "options": ["27/64", "9/16", "3/4", "81/256"],
                "ans": 0,
                "explanation": "At each step, $1/4$ of the area is removed, retaining $3/4$. After 3 iterations, remaining area is $A_3 = A_0 \\times (\\frac{3}{4})^3 = A_0 \\times \\frac{27}{64}$."
            }
        ]
    },
    {
        "id": 15,
        "title": "The Tower of Hanoi Puzzle",
        "badge": "Concept 15 • Recursive Masterpiece",
        "audio_text": "The Tower of Hanoi is a legendary mathematical puzzle invented by Edouard Lucas. You have three rods and n disks of different sizes. To move all disks from the source rod to the target rod without ever placing a larger disk onto a smaller disk requires a recursive strategy! The minimum number of moves needed forms a Geometric series whose sum is exactly 2 to the power n minus 1.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Rules of the Puzzle</h3>
                    <ul class="text-xs text-slate-300 space-y-1.5 list-disc list-inside">
                        <li>Only <strong>one disk</strong> may be moved at a time.</li>
                        <li>Each move consists of taking the upper disk from one rod and sliding it onto another rod.</li>
                        <li><strong>No larger disk may be placed on top of a smaller disk</strong> at any time.</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">The Recursive Equation:</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        To move $n$ disks from Peg A to Peg C:
                    </p>
                    <ol class="text-xs text-slate-300 list-decimal list-inside space-y-1 mt-1">
                        <li>Move top $n-1$ disks from A to B ($M_{n-1}$ moves).</li>
                        <li>Move largest disk from A to C ($1$ move).</li>
                        <li>Move $n-1$ disks from B to C ($M_{n-1}$ moves).</li>
                    </ol>
                    <div class="mt-2 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-emerald-300">
                        $$M_n = 2M_{n-1} + 1 \implies M_n = 2^n - 1$$
                        Notice $2^n - 1 = 1 + 2 + 4 + \dots + 2^{n-1}$ is the sum of a GP!
                    </div>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-1">Interactive Tower of Hanoi</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <div class="flex items-center gap-1">
                            <label class="text-slate-400">Disks ($n$):</label>
                            <select id="sim15_disks" onchange="initSim15()" class="bg-slate-800 border border-slate-700 text-xs rounded px-1.5 py-0.5 text-amber-300">
                                <option value="2">2 Disks (3 moves)</option>
                                <option value="3" selected>3 Disks (7 moves)</option>
                                <option value="4">4 Disks (15 moves)</option>
                            </select>
                        </div>
                        <div class="text-xs text-slate-300">
                            Moves: <span id="sim15_moves" class="text-emerald-400 font-bold">0</span> / <span id="sim15_min" class="text-amber-300 font-bold">7</span>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim15_svg" viewBox="0 0 300 130" class="w-full h-32">
                            <!-- Hanoi rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="autoSolveSim15()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-xs">
                            ▶ Auto-Solve Step
                        </button>
                        <button onclick="initSim15()" class="px-2 py-1 bg-slate-700 rounded text-slate-300 text-xs">
                            Reset
                        </button>
                        <div id="sim15_status" class="text-[11px] text-emerald-400">Ready</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the minimum number of moves required to solve the Tower of Hanoi puzzle with 5 disks?",
                "options": ["15", "25", "31", "32"],
                "ans": 2,
                "explanation": "Using formula $M_n = 2^n - 1$: for $n = 5$, $M_5 = 2^5 - 1 = 32 - 1 = 31$ moves."
            },
            {
                "q": "In the ancient legend of Hanoi with 64 golden disks, if priests make 1 move per second without error, roughly how long would it take to finish?",
                "options": [
                    "About 500 years",
                    "About 1,000,000 years",
                    "About 585 billion years (longer than the age of the Universe)",
                    "About 100 days"
                ],
                "ans": 2,
                "explanation": "$2^{64} - 1 \\approx 1.84 \\times 10^{19}$ seconds, which is approximately $5.85 \\times 10^{11}$ years (over 585 billion years!)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Patterns & Algorithms",
        "badge": "Concept 16 • Algorithmic Modeling",
        "audio_text": "Computational thinking connects mathematical patterns to algorithms and computer science. By decomposing sequences, identifying inductive loops, and formulating recursive functions with memoization, programmers and data scientists model everything from financial markets to artificial neural networks. Let us review the computational pipeline!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The 4 Pillars of Computational Thinking</h3>
                    <ul class="text-xs text-slate-300 space-y-2">
                        <li><strong>Decomposition:</strong> Breaking a complex sequence into differences ($\Delta a_k$) and quotients ($a_{k+1}/a_k$).</li>
                        <li><strong>Pattern Recognition:</strong> Testing whether $\Delta a_k = d$ (AP) or $a_{k+1}/a_k = r$ (GP) or higher-order differences.</li>
                        <li><strong>Abstraction:</strong> Generalizing numerical data into symbolic formulas ($a_n = a + (n-1)d$ or $a_n = a \cdot r^{n-1}$).</li>
                        <li><strong>Algorithm Design:</strong> Writing iterative and recursive code routines to generate, search, and sum terms efficiently.</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Algorithmic Complexity Summary:</h4>
                    <p class="text-xs text-slate-300">
                        • Explicit formula lookup: $\mathcal{O}(1)$ time, $\mathcal{O}(1)$ memory.<br>
                        • Loop-based generation: $\mathcal{O}(n)$ time, $\mathcal{O}(n)$ memory.<br>
                        • Naive Fibonacci recursion: $\mathcal{O}(2^n)$ exponential time (fixed with memoization to $\mathcal{O}(n)$!).
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col">
                <h4 class="text-sm font-bold text-indigo-300 mb-2 text-center">Interactive Algorithm Classifier</h4>
                <div class="space-y-3">
                    <p class="text-xs text-slate-400 text-center">Enter 4 comma-separated terms to test the algorithm:</p>
                    <div class="flex gap-2">
                        <input id="sim16_input" type="text" value="7, 14, 21, 28" class="flex-1 bg-slate-800 border border-slate-700 rounded px-2 py-1 text-xs text-amber-300 font-mono">
                        <button onclick="runSim16Classifier()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white text-xs font-semibold">
                            Run Pipeline
                        </button>
                    </div>
                    <div id="sim16_output" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Which computational thinking pillar involves determining whether consecutive differences in a sequence are constant?",
                "options": ["Abstraction", "Pattern Recognition", "Algorithm Design", "Decomposition"],
                "ans": 1,
                "explanation": "Pattern Recognition is identifying repeating trends or regularities (such as constant differences or constant ratios) in data."
            },
            {
                "q": "Why is computing $F_{50}$ in Fibonacci using an explicit Binet formula or memoized loop far superior to naive recursive function calls?",
                "options": [
                    "Naive recursion repeats identical subproblems exponentially, taking over 1 billion redundant steps",
                    "Naive recursion only works with negative numbers",
                    "Computers do not allow recursive calls greater than 10",
                    "Explicit formulas use less electricity"
                ],
                "ans": 0,
                "explanation": "Naive Fibonacci recursion has time complexity $O(2^n)$, recalculating $F_3, F_4, \\dots$ trillions of times redundantly. Memoization or loops reduce this to $O(n)$ linear steps."
            }
        ]
    }
]

# 4 Dedicated Quiz Slides (40 questions total: 10 per slide)
QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Quiz 1: Sequences, Explicit & Recursive Rules",
        "badge": "Quiz Challenge 1 • 10 Questions",
        "questions": [
            {
                "id": 1,
                "q": "What is the 8th term of the sequence defined by the explicit rule $a_n = n^2 - 3n$?",
                "options": ["40", "44", "48", "32"],
                "ans": 0,
                "solution": "Substitute $n = 8$: $a_8 = 8^2 - 3(8) = 64 - 24 = 40$."
            },
            {
                "id": 2,
                "q": "A sequence has explicit formula $a_n = (-1)^{n+1} \\cdot 2^n$. What is the 5th term ($a_5$)?",
                "options": ["-32", "32", "-16", "16"],
                "ans": 1,
                "solution": "Substitute $n = 5$: $a_5 = (-1)^{5+1} \\cdot 2^5 = (-1)^6 \\cdot 32 = (+1) \\cdot 32 = 32$."
            },
            {
                "id": 3,
                "q": "Given recursive rule $a_1 = 3$ and $a_n = 3a_{n-1} - 2$ for $n \\ge 2$, what is $a_4$?",
                "options": ["19", "45", "57", "61"],
                "ans": 3,
                "solution": "Step-by-step: $a_1 = 3$. $a_2 = 3(3) - 2 = 7$. $a_3 = 3(7) - 2 = 19$. $a_4 = 3(19) - 2 = 57 - 2 = 55$... wait: $3(19)-2 = 55$. Let's recheck: if $a_4 = 3(19)-2 = 55$. But options have 61? Let's check $a_1=3$: $a_2 = 3(3)-2=7$, $a_3=3(7)-2=19$, $3(19)-2=55$. If $a_1=5$: $a_2=13, a_3=37, a_4=109$. Let's adjust rule so an option matches exactly: if $a_n = 3a_{n-1} + 2$, then $a_1=3$, $a_2=11$, $a_3=35$. If $a_n = 2a_{n-1}+5$, $a_1=3, a_2=11, a_3=27, a_4=59$. For $a_1=3, a_n = 3a_{n-1}-2$, $a_4 = 55$. Let's fix option to 55."
            },
            {
                "id": 4,
                "q": "Which of the following is the recursive formula for the sequence $4, 9, 14, 19, 24, \\dots$?",
                "options": [
                    "a_1 = 4, a_n = a_{n-1} + 5",
                    "a_1 = 4, a_n = 5a_{n-1}",
                    "a_1 = 5, a_n = a_{n-1} + 4",
                    "a_1 = 4, a_n = 2a_{n-1} + 1"
                ],
                "ans": 0,
                "solution": "The first term is $a_1 = 4$. Each subsequent term increases by $9 - 4 = 5$. Thus $a_n = a_{n-1} + 5$ for $n \\ge 2$."
            },
            {
                "id": 5,
                "q": "What is the 50th term of the sequence with explicit formula $a_n = \\frac{n}{n+1}$?",
                "options": ["49/50", "50/51", "51/52", "1"],
                "ans": 1,
                "solution": "Substitute $n = 50$: $a_{50} = \\frac{50}{50 + 1} = \\frac{50}{51}$."
            },
            {
                "id": 6,
                "q": "If $a_n = 4n - 7$, what is the value of $a_{15} - a_{10}$?",
                "options": ["15", "20", "25", "30"],
                "ans": 1,
                "solution": "$a_{15} = 4(15) - 7 = 53$. $a_{10} = 4(10) - 7 = 33$. Difference = $53 - 33 = 20$. Alternatively, $(15 - 10) \\times 4 = 5 \\times 4 = 20$."
            },
            {
                "id": 7,
                "q": "The Fibonacci sequence is defined by $F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}$. What is $F_8$?",
                "options": ["13", "21", "34", "55"],
                "ans": 1,
                "solution": "Terms: $F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13, F_8=21$."
            },
            {
                "id": 8,
                "q": "Which term in the sequence $a_n = 2n^2 + 3$ is equal to 131?",
                "options": ["6th", "7th", "8th", "9th"],
                "ans": 2,
                "solution": "Set $2n^2 + 3 = 131 \\implies 2n^2 = 128 \\implies n^2 = 64 \\implies n = 8$ (since $n \\in \\mathbb{N}$, $n > 0$)."
            },
            {
                "id": 9,
                "q": "Convert the recursive definition $a_1 = 6, a_n = a_{n-1} + 7$ into an explicit formula.",
                "options": ["a_n = 7n - 1", "a_n = 7n + 6", "a_n = 6n + 1", "a_n = 7n + 1"],
                "ans": 0,
                "solution": "$a_n = a_1 + (n-1)d = 6 + (n-1)7 = 6 + 7n - 7 = 7n - 1$. Check $n=1$: $7(1)-1=6$."
            },
            {
                "id": 10,
                "q": "If a sequence satisfies $a_{n+1} = \\frac{a_n}{2}$ with $a_1 = 64$, what is $a_6$?",
                "options": ["1", "2", "4", "0.5"],
                "ans": 1,
                "solution": "$a_1 = 64, a_2 = 32, a_3 = 16, a_4 = 8, a_5 = 4, a_6 = 2$."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Quiz 2: Arithmetic Progressions & Sum of Natural Numbers",
        "badge": "Quiz Challenge 2 • 10 Questions",
        "questions": [
            {
                "id": 11,
                "q": "Find the 30th term of the AP: $7, 11, 15, 19, \\dots$",
                "options": ["120", "123", "127", "131"],
                "ans": 1,
                "solution": "Here $a = 7, d = 11 - 7 = 4$. $a_{30} = 7 + (30 - 1)4 = 7 + 29 \\times 4 = 7 + 116 = 123$."
            },
            {
                "id": 12,
                "q": "What is the common difference $d$ of an AP whose 10th term is 52 and 15th term is 77?",
                "options": ["3", "4", "5", "6"],
                "ans": 2,
                "solution": "$a_{15} - a_{10} = (15 - 10)d = 5d$. Thus $77 - 52 = 25 \\implies 5d = 25 \\implies d = 5$."
            },
            {
                "id": 13,
                "q": "Which term of the AP: $21, 18, 15, \\dots$ is equal to 0?",
                "options": ["7th", "8th", "9th", "10th"],
                "ans": 1,
                "solution": "$a = 21, d = 18 - 21 = -3$. Set $a_n = 0$: $0 = 21 + (n - 1)(-3) \\implies -21 = -3(n - 1) \\implies n - 1 = 7 \\implies n = 8$."
            },
            {
                "id": 14,
                "q": "Calculate the sum of the first 100 natural numbers ($1 + 2 + 3 + \\dots + 100$).",
                "options": ["5000", "5050", "5100", "5150"],
                "ans": 1,
                "solution": "Use Gauss's formula: $S_{100} = \\frac{100(101)}{2} = 50 \\times 101 = 5050$."
            },
            {
                "id": 15,
                "q": "How many two-digit positive integers are divisible by 3?",
                "options": ["29", "30", "31", "33"],
                "ans": 1,
                "solution": "The two-digit numbers divisible by 3 are $12, 15, 18, \\dots, 99$. This is an AP with $a = 12, d = 3, a_n = 99$. $99 = 12 + (n - 1)3 \\implies 87 = 3(n - 1) \\implies n - 1 = 29 \\implies n = 30$."
            },
            {
                "id": 16,
                "q": "If the sum of the first $n$ natural numbers is 78, what is $n$?",
                "options": ["11", "12", "13", "14"],
                "ans": 1,
                "solution": "$\\frac{n(n+1)}{2} = 78 \\implies n(n+1) = 156$. Testing $12 \\times 13 = 156$, so $n = 12$."
            },
            {
                "id": 17,
                "q": "In an AP, if $d = -4, n = 7, a_n = 4$, what is the first term $a$?",
                "options": ["24", "28", "20", "16"],
                "ans": 1,
                "solution": "$a_n = a + (n - 1)d \\implies 4 = a + (7 - 1)(-4) \\implies 4 = a - 24 \\implies a = 28$."
            },
            {
                "id": 18,
                "q": "A hall has 25 rows of chairs. Row 1 has 20 chairs, and each row has 2 more chairs than the previous. How many chairs are in the 25th row?",
                "options": ["66", "68", "70", "72"],
                "ans": 1,
                "solution": "$a = 20, d = 2, n = 25$. $a_{25} = 20 + (25 - 1)2 = 20 + 24 \\times 2 = 20 + 48 = 68$ chairs."
            },
            {
                "id": 19,
                "q": "If the 3rd and 9th terms of an AP are 4 and -8 respectively, which term of this AP is 0?",
                "options": ["5th", "6th", "7th", "8th"],
                "ans": 0,
                "solution": "$a_9 - a_3 = 6d \\implies -8 - 4 = -12 \\implies 6d = -12 \\implies d = -2$. Then $a_3 = a + 2d = 4 \\implies a + 2(-2) = 4 \\implies a = 8$. To find when $a_n = 0$: $0 = 8 + (n - 1)(-2) \\implies 2(n - 1) = 8 \\implies n - 1 = 4 \\implies n = 5$."
            },
            {
                "id": 20,
                "q": "What is the slope of the straight line formed when plotting the terms of the AP $12, 17, 22, 27, \\dots$ on a Cartesian plane?",
                "options": ["12", "5", "17", "1"],
                "ans": 1,
                "solution": "The slope of the line passing through points $(n, a_n)$ in an AP is equal to the common difference $d = 17 - 12 = 5$."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Quiz 3: Geometric Progressions & Exponential Modeling",
        "badge": "Quiz Challenge 3 • 10 Questions",
        "questions": [
            {
                "id": 21,
                "q": "What is the 7th term of the Geometric Progression: $2, 6, 18, 54, \\dots$?",
                "options": ["486", "729", "1458", "2187"],
                "ans": 2,
                "solution": "Here $a = 2$ and $r = 6 / 2 = 3$. $a_7 = a \\cdot r^{7-1} = 2 \\cdot 3^6 = 2 \\cdot 729 = 1458$."
            },
            {
                "id": 22,
                "q": "Find the common ratio $r$ of the GP whose first term is 5 and 4th term is 320.",
                "options": ["2", "4", "8", "16"],
                "ans": 1,
                "solution": "$a_4 = a \\cdot r^3 \\implies 320 = 5 \\cdot r^3 \\implies r^3 = 64 \\implies r = 4$."
            },
            {
                "id": 23,
                "q": "What is the 5th term of the alternating GP: $81, -27, 9, -3, \\dots$?",
                "options": ["1", "-1", "3", "-1/3"],
                "ans": 0,
                "solution": "$a = 81, r = -27 / 81 = -1/3$. $a_5 = 81 \\cdot (-1/3)^{5-1} = 81 \\cdot (-1/3)^4 = 81 \\cdot (1/81) = 1$."
            },
            {
                "id": 24,
                "q": "Which term of the GP $5, 10, 20, 40, \\dots$ is equal to 1280?",
                "options": ["7th", "8th", "9th", "10th"],
                "ans": 2,
                "solution": "$a = 5, r = 2$. $a_n = 5 \\cdot 2^{n-1} = 1280 \\implies 2^{n-1} = 256 = 2^8 \\implies n - 1 = 8 \\implies n = 9$."
            },
            {
                "id": 25,
                "q": "A machine purchased for ₹100,000 depreciates by $10\\%$ each year. What is its value after 3 years?",
                "options": ["₹70,000", "₹72,900", "₹81,000", "₹90,000"],
                "ans": 1,
                "solution": "Each year the value is multiplied by $r = 1 - 0.10 = 0.90$. Value after 3 years = $100,000 \\times (0.90)^3 = 100,000 \\times 0.729 = ₹72,900$."
            },
            {
                "id": 26,
                "q": "In a GP, if the 2nd term is 12 and the 5th term is 96, what is the first term $a$?",
                "options": ["3", "6", "4", "2"],
                "ans": 1,
                "solution": "$\\frac{a_5}{a_2} = \\frac{a r^4}{a r} = r^3 = \\frac{96}{12} = 8 \\implies r = 2$. Then $a_2 = a \\cdot 2 = 12 \\implies a = 6$."
            },
            {
                "id": 27,
                "q": "A ball rebounds to $80\\%$ of its height on each bounce. If dropped from 500 cm, what is the height on the 2nd bounce?",
                "options": ["400 cm", "320 cm", "256 cm", "200 cm"],
                "ans": 1,
                "solution": "1st bounce = $500 \\times 0.8 = 400$ cm. 2nd bounce = $400 \\times 0.8 = 320$ cm."
            },
            {
                "id": 28,
                "q": "If 3 numbers $k - 2, k + 1, k + 7$ are in GP, what is the value of $k$?",
                "options": ["3", "4", "5", "6"],
                "ans": 2,
                "solution": "For terms $x, y, z$ to be in GP, $y^2 = xz$. Thus $(k + 1)^2 = (k - 2)(k + 7) \\implies k^2 + 2k + 1 = k^2 + 5k - 14 \\implies 2k + 1 = 5k - 14 \\implies 3k = 15 \\implies k = 5$."
            },
            {
                "id": 29,
                "q": "What is the common ratio $r$ of the GP: $\\sqrt{2}, 2, 2\\sqrt{2}, 4, \\dots$?",
                "options": ["2", "\\sqrt{2}", "1/\\sqrt{2}", "4"],
                "ans": 1,
                "solution": "$r = \\frac{a_2}{a_1} = \\frac{2}{\\sqrt{2}} = \\sqrt{2}$."
            },
            {
                "id": 30,
                "q": "Why does an exponential GP eventually overtake any linear AP with constant difference $d$?",
                "options": [
                    "Because an AP stops after 20 terms",
                    "Because for $r > 1$, the growth increment in a GP is proportional to the current magnitude, which compounds superlinearly",
                    "Because AP common differences always decrease over time",
                    "Because negative numbers are not allowed in an AP"
                ],
                "ans": 1,
                "solution": "In an AP, each step adds a fixed constant $d$, whereas in a GP, each step multiplies by $r > 1$, creating an exponential rate of increase that outgrows any polynomial/linear rate."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Quiz 4: Fractals, Tower of Hanoi & Computational Algorithms",
        "badge": "Quiz Challenge 4 • 10 Questions",
        "questions": [
            {
                "id": 31,
                "q": "What is the minimum number of moves needed to solve the Tower of Hanoi puzzle with 4 disks?",
                "options": ["7", "15", "16", "31"],
                "ans": 1,
                "solution": "Use formula $M_n = 2^n - 1$: for $n = 4$, $M_4 = 2^4 - 1 = 16 - 1 = 15$ moves."
            },
            {
                "id": 32,
                "q": "If the side of the initial equilateral triangle of a Koch Snowflake is 9 cm, what is its perimeter at iteration 1?",
                "options": ["27 cm", "36 cm", "48 cm", "32 cm"],
                "ans": 1,
                "solution": "Initial perimeter $P_0 = 3 \\times 9 = 27$ cm. At iteration 1, perimeter multiplies by $4/3$: $P_1 = 27 \\times \\frac{4}{3} = 36$ cm."
            },
            {
                "id": 33,
                "q": "In the Sierpinski Triangle, if the initial shaded area is $64\\text{ cm}^2$, what is the shaded area after 2 iterations?",
                "options": ["48 cm²", "36 cm²", "27 cm²", "16 cm²"],
                "ans": 1,
                "solution": "At each iteration, area multiplies by $3/4$. After 2 iterations: $A_2 = 64 \\times (\\frac{3}{4})^2 = 64 \\times \\frac{9}{16} = 36\\text{ cm}^2$."
            },
            {
                "id": 34,
                "q": "What is the time complexity of looking up the $n$-th term of a sequence using an explicit closed-form formula $a_n = f(n)$?",
                "options": ["O(1) constant time", "O(n) linear time", "O(n²) quadratic time", "O(2ⁿ) exponential time"],
                "ans": 0,
                "solution": "Evaluating a direct formula involves arithmetic operations that run in $\\mathcal{O}(1)$ constant time, independent of $n$."
            },
            {
                "id": 35,
                "q": "In the Tower of Hanoi recurrence $M_n = 2M_{n-1} + 1$ with $M_1 = 1$, what is $M_6$?",
                "options": ["31", "63", "64", "127"],
                "ans": 1,
                "solution": "$M_6 = 2^6 - 1 = 64 - 1 = 63$ moves."
            },
            {
                "id": 36,
                "q": "Which of the following expressions represents the sum of the first $n$ terms of the sequence $1, 2, 4, 8, \\dots, 2^{n-1}$?",
                "options": ["2ⁿ", "2ⁿ - 1", "2ⁿ⁺¹ - 1", "n²"],
                "ans": 1,
                "solution": "This is a GP with $a = 1, r = 2$. $S_n = \\frac{a(r^n - 1)}{r - 1} = \\frac{1(2^n - 1)}{2 - 1} = 2^n - 1$."
            },
            {
                "id": 37,
                "q": "How many segments compose the Koch Snowflake boundary after 3 iterations?",
                "options": ["12", "48", "192", "768"],
                "ans": 2,
                "solution": "The number of segments is $N_n = 3 \\cdot 4^n$. For $n = 3$, $N_3 = 3 \\cdot 4^3 = 3 \\cdot 64 = 192$ segments."
            },
            {
                "id": 38,
                "q": "What technique in computational thinking allows recursive functions to avoid recalculating already-solved subproblems?",
                "options": ["Memoization / Caching", "Abstraction", "Binary Search", "Type Casting"],
                "ans": 0,
                "solution": "Memoization stores intermediate computation results in a table or hash map, turning exponential recursive algorithms into linear time."
            },
            {
                "id": 39,
                "q": "If a sequence algorithm inspects consecutive terms and finds $\\frac{a_2}{a_1} = 3$ and $\\frac{a_3}{a_2} = 3$, but $a_2 - a_1 = 6$ and $a_3 - a_2 = 18$, it classifies the sequence as:",
                "options": [
                    "An Arithmetic Progression with d = 6",
                    "A Geometric Progression with r = 3",
                    "Neither AP nor GP",
                    "A Fibonacci sequence"
                ],
                "ans": 1,
                "solution": "Because the ratios between consecutive terms are constant ($r = 3$) while differences are not constant, it is a Geometric Progression."
            },
            {
                "id": 40,
                "q": "A computational algorithm generates terms using: $a_1 = 1$, $a_n = a_{n-1} + n$ for $n \\ge 2$. What is the 6th term generated by this algorithm?",
                "options": ["15", "21", "28", "36"],
                "ans": 1,
                "solution": "This generates triangular numbers: $a_1 = 1$, $a_2 = 1+2 = 3$, $a_3 = 3+3 = 6$, $a_4 = 6+4 = 10$, $a_5 = 10+5 = 15$, $a_6 = 15+6 = 21$ (which is $T_6 = \\frac{6 \\times 7}{2} = 21$)."
            }
        ]
    }
]

# Quick fix for Quiz 1 Question 3: ensure option matches solution
QUIZ_SLIDES[0]["questions"][2]["options"] = ["19", "45", "55", "61"]
QUIZ_SLIDES[0]["questions"][2]["ans"] = 2
QUIZ_SLIDES[0]["questions"][2]["solution"] = "Step-by-step: $a_1 = 3$. Next, $a_2 = 3(3) - 2 = 7$. Then $a_3 = 3(7) - 2 = 19$. Finally, $a_4 = 3(19) - 2 = 57 - 2 = 55$."

print("Loaded class9_sequences_data: 16 content slides, 4 quiz slides, 40 quiz questions.")

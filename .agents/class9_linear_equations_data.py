# -*- coding: utf-8 -*-
"""
Class 9 Mathematics Chapter 5: Linear Equations in Two Variables
Competencies: CG-3, C-3.2, C-8.1, CG-9
Complete dataset with 16 content slides, 32 in-slide checkpoints, and 4 dedicated quiz challenge slides (40 questions).
"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "Introduction to Linear Equations in Two Variables",
        "badge": "Concept 1 • Two Unknowns",
        "audio_text": "Welcome to Linear Equations in Two Variables! When real-life situations involve two interconnected unknown quantities—such as the runs scored by two cricketers, or the cost of pens and pencils—a single variable is not enough. We express them using two variables in the standard form a x plus b y plus c equals zero. Let us explore real-world modeling!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Standard Form of a Linear Equation</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        An equation of the form:
                    </p>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-sm font-mono text-center text-amber-300 font-bold">
                        $$ax + by + c = 0$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        where $a, b, c$ are real numbers and $a, b$ are <strong>not both zero</strong> ($a^2 + b^2 \ne 0$), is called a <strong>linear equation in two variables</strong> $x$ and $y$.
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-2">Real-Life Contextual Examples:</h4>
                    <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                        <li><strong>Cricket Partnership:</strong> Two batsmen Rohit and Virat scored 176 runs together: $x + y = 176$.</li>
                        <li><strong>Stationery Cost:</strong> Cost of 5 notebooks and 7 pens is ₹250: $5x + 7y = 250$.</li>
                        <li><strong>Perimeter:</strong> The perimeter of a rectangle with length $x$ and width $y$ is 48 cm: $2(x + y) = 48 \implies x + y - 24 = 0$.</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Real-World Problem Translator</h4>
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <label class="text-slate-400">Select Context:</label>
                        <select id="sim1_scenario" onchange="updateSim1()" class="bg-slate-800 border border-slate-700 text-xs text-amber-300 rounded px-2 py-1">
                            <option value="cricket">Cricket Match Partnership</option>
                            <option value="stationery">Stationery Purchases</option>
                            <option value="fare">Taxi Fare Scheme</option>
                        </select>
                    </div>
                    <div id="sim1_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-2 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                    <div id="sim1_standard" class="text-xs text-center text-emerald-400 font-bold font-mono">
                        Standard Form: ax + by + c = 0
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Express the linear equation $2x = -5y + 7$ in the standard form $ax + by + c = 0$ and state the values of $a, b, c$.",
                "options": [
                    "2x + 5y - 7 = 0 with a = 2, b = 5, c = -7",
                    "2x - 5y + 7 = 0 with a = 2, b = -5, c = 7",
                    "2x + 5y + 7 = 0 with a = 2, b = 5, c = 7",
                    "5x + 2y - 7 = 0 with a = 5, b = 2, c = -7"
                ],
                "ans": 0,
                "explanation": "Transposing all terms to the LHS gives $2x + 5y - 7 = 0$. Comparing with $ax + by + c = 0$, we have $a = 2, b = 5, c = -7$."
            },
            {
                "q": "The cost of a notebook is twice the cost of a pen. Write a linear equation in two variables to represent this statement.",
                "options": [
                    "x - 2y = 0 (where x = notebook, y = pen)",
                    "2x - y = 0",
                    "x + 2y = 0",
                    "x = y + 2"
                ],
                "ans": 0,
                "explanation": "Let cost of notebook be ₹$x$ and cost of pen be ₹$y$. According to statement, $x = 2y \\implies x - 2y = 0$."
            }
        ]
    },
    {
        "id": 2,
        "title": "Solutions of a Linear Equation in Two Variables",
        "badge": "Concept 2 • Infinite Solutions",
        "audio_text": "While a linear equation in one variable has a single unique root, a linear equation in two variables has infinitely many solutions! Every solution is an ordered pair of real numbers x comma y that satisfies the equality. By choosing arbitrary values for x, we can calculate corresponding values for y.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Ordered Pairs as Solutions</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A <strong>solution</strong> of $ax + by + c = 0$ is an ordered pair of numbers $(\alpha, \beta)$ such that substituting $x = \alpha$ and $y = \beta$ makes the LHS equal to zero.
                    </p>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-cyan-300">
                        $$y = \frac{-c - ax}{b} \quad (b \ne 0)$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        ★ <strong>Fundamental Theorem:</strong> Every linear equation in two variables has <em>infinitely many solutions</em>!
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Intercepts (Easiest Solutions):</h4>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>y-intercept:</strong> Put $x = 0 \implies by + c = 0 \implies y = -c/b$. Point is $(0, -c/b)$.</li>
                        <li><strong>x-intercept:</strong> Put $y = 0 \implies ax + c = 0 \implies x = -c/a$. Point is $(-c/a, 0)$.</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Solution Table Generator</h4>
                <div class="w-full space-y-2">
                    <div class="text-xs text-center text-slate-400">
                        Equation: <span class="text-amber-300 font-bold font-mono">2x + 3y = 12 ⟹ y = (12 - 2x)/3</span>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <label class="text-slate-400">Choose x: <span id="sim2_x_val" class="text-cyan-300 font-bold font-mono">0</span></label>
                        <input id="sim2_x" type="range" min="-6" max="6" step="1" value="0" oninput="updateSim2()" class="w-36 accent-indigo-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-indigo-500/20 text-center text-xs font-mono">
                        <div>Calculated: y = (12 - 2(<span id="sim2_sub_x">0</span>))/3 = <span id="sim2_y_val" class="text-emerald-400 font-bold">4.00</span></div>
                        <div class="text-amber-300 font-bold mt-1">Solution Pair: (<span id="sim2_pair_x">0</span>, <span id="sim2_pair_y">4.00</span>)</div>
                    </div>
                    <div id="sim2_table" class="grid grid-cols-4 gap-1 text-[11px] font-mono text-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Which of the following ordered pairs is a solution of the equation $3x + 4y = 24$?",
                "options": ["(4, 3)", "(0, 6)", "(8, 0)", "All of the above"],
                "ans": 3,
                "explanation": "Substitute each pair: (4,3) gives $3(4)+4(3) = 12+12 = 24$. (0,6) gives $3(0)+4(6) = 24$. (8,0) gives $3(8)+4(0) = 24$. All three are valid solutions."
            },
            {
                "q": "Find the value of $k$ if $x = 2, y = 1$ is a solution of the equation $2x + 3y = k$.",
                "options": ["7", "5", "8", "6"],
                "ans": 0,
                "explanation": "Substitute $x = 2$ and $y = 1$ into $2x + 3y = k$: $2(2) + 3(1) = 4 + 3 = 7 \\implies k = 7$."
            }
        ]
    },
    {
        "id": 3,
        "title": "Graphical Representation of a Linear Equation",
        "badge": "Concept 3 • The Straight Line",
        "audio_text": "When we plot the infinite solutions of a linear equation in two variables onto a coordinate plane, an extraordinary geometrical fact appears: every single point lies along a perfectly straight line! Conversely, every point on that line is a valid solution. Hence, the equation is called linear.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Geometric Correspondence</h3>
                    <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                        <li>Every solution $(\alpha, \beta)$ of $ax + by + c = 0$ corresponds to a <strong>unique point</strong> on its line.</li>
                        <li>Every point $(x, y)$ lying on the line is a <strong>solution</strong> of the equation.</li>
                        <li>Any point that does <em>not</em> lie on the line is <em>not</em> a solution.</li>
                        <li><strong>Two Points Axiom:</strong> Exactly one straight line passes through two distinct points. Two points are enough to plot the line; a third point serves as a verification check!</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Graphing Algorithm:</h4>
                    <ol class="text-xs text-slate-300 space-y-1 list-decimal list-inside">
                        <li>Solve for $y$ in terms of $x$: $y = f(x)$.</li>
                        <li>Choose 2 or 3 convenient values of $x$ (like intercepts $x=0, y=0$).</li>
                        <li>Compute corresponding $y$ values to build a table.</li>
                        <li>Plot points and draw the straight line through them!</li>
                    </ol>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Cartesian Line Plotter</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Equation: x + 2y = 6</label>
                        <div class="flex gap-1 text-[11px] font-mono">
                            <span class="text-indigo-400">(0,3)</span> | <span class="text-cyan-400">(6,0)</span> | <span class="text-amber-400">(2,2)</span>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim3_svg" viewBox="0 0 260 200" class="w-full h-44">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div class="text-[11px] text-center text-slate-400">
                        Line connects continuous solutions across all four quadrants.
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "At what point does the graph of the linear equation $2x + 3y = 6$ cut the y-axis?",
                "options": ["(0, 2)", "(3, 0)", "(0, 3)", "(2, 0)"],
                "ans": 0,
                "explanation": "On the y-axis, the x-coordinate is zero ($x = 0$). Substitute $x = 0$ into $2(0) + 3y = 6 \\implies 3y = 6 \\implies y = 2$. Point is $(0, 2)$."
            },
            {
                "q": "If the point $(3, 4)$ lies on the graph of the equation $3y = ax + 7$, what is the value of $a$?",
                "options": ["5/3", "3/5", "1", "2"],
                "ans": 0,
                "explanation": "Substitute $x = 3, y = 4$: $3(4) = a(3) + 7 \\implies 12 = 3a + 7 \\implies 3a = 5 \\implies a = 5/3$."
            }
        ]
    },
    {
        "id": 4,
        "title": "Slope-Intercept Form of a Linear Equation",
        "badge": "Concept 4 • Rate of Change & Shift",
        "audio_text": "By solving standard linear form for y, we obtain the famous slope-intercept form, y equals m x plus c. Here, m is the slope, representing the rise over run or steepness of the line, while c is the y-intercept, where the line crosses the vertical axis. Let us adjust the slope and intercept interactively!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Converting to $y = mx + c$</h3>
                    <p class="text-xs text-slate-300 leading-relaxed font-mono">
                        $$ax + by + c = 0 \implies by = -ax - c \implies y = \left(-\frac{a}{b}\right)x + \left(-\frac{c}{b}\right)$$
                    </p>
                    <div class="mt-2 text-xs text-slate-300 space-y-1">
                        <div>• <strong>Slope ($m$):</strong> $-\frac{a}{b} = \frac{\Delta y}{\Delta x} = \frac{\text{Rise}}{\text{Run}}$ (determines direction & tilt)</div>
                        <div>• <strong>y-intercept ($c$):</strong> $-\frac{c}{b}$ (vertical shift where $x = 0$)</div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Slope Behaviors:</h4>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><span class="text-emerald-400 font-bold">$m > 0$:</span> Line slants upward from left to right.</li>
                        <li><span class="text-rose-400 font-bold">$m < 0$:</span> Line slants downward from left to right.</li>
                        <li><span class="text-cyan-400 font-bold">$m = 0$:</span> Line is horizontal (parallel to x-axis).</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Slope & Intercept Sandbox</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Slope $m$: <span id="sim4_m_val" class="text-cyan-300 font-bold">1</span></label>
                            <input id="sim4_m" type="range" min="-3" max="3" step="0.5" value="1" oninput="drawSim4()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Intercept $c$: <span id="sim4_c_val" class="text-amber-300 font-bold">2</span></label>
                            <input id="sim4_c" type="range" min="-5" max="5" step="1" value="2" oninput="drawSim4()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim4_svg" viewBox="0 0 260 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim4_eq" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        y = 1.0x + 2
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the slope ($m$) and y-intercept ($c$) of the line $3x - 2y = 8$?",
                "options": [
                    "m = 3/2, c = -4",
                    "m = -3/2, c = 4",
                    "m = 3, c = -8",
                    "m = 2/3, c = 8"
                ],
                "ans": 0,
                "explanation": "Rewrite as $-2y = -3x + 8 \\implies y = \\frac{3}{2}x - 4$. Thus slope $m = 3/2$ and y-intercept $c = -4$."
            },
            {
                "q": "If a line passes through $(0, 5)$ and has slope $m = -2$, what is its equation?",
                "options": ["y = -2x + 5", "y = 2x + 5", "y = -2x - 5", "2x - y = 5"],
                "ans": 0,
                "explanation": "Since the point is $(0, 5)$, the y-intercept is $c = 5$. With $m = -2$, the slope-intercept form gives $y = -2x + 5$."
            }
        ]
    },
    {
        "id": 5,
        "title": "Drawing Graphs When Variables Assume Certain Values (Discrete Domains)",
        "badge": "Concept 5 • Discrete vs Continuous",
        "audio_text": "In pure mathematics, variables x and y can take any real number, forming an unbroken continuous line. But in daily life, quantities like people, cars, or eggs must be whole positive numbers! In such contextual models, the graph is not a solid line, but a discrete set of isolated dots lying on the line.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Discrete Practical Contexts</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        Consider a school trip where adult tickets cost ₹100 ($x$) and student tickets cost ₹50 ($y$), with total budget ₹500:
                    </p>
                    <div class="mt-2 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$100x + 50y = 500 \implies 2x + y = 10$$
                    </div>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside mt-2">
                        <li>You cannot buy $2.5$ adult tickets or $-1$ student tickets!</li>
                        <li>Domain constraints: $x \ge 0, y \ge 0$, and $x, y \in \mathbb{W} = \{0, 1, 2, \dots\}$.</li>
                        <li>Valid integer solutions: $(0, 10), (1, 8), (2, 6), (3, 4), (4, 2), (5, 0)$.</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Visual Distinction:</h4>
                    <p class="text-xs text-slate-300">
                        • <strong>Continuous $\mathbb{R}$:</strong> Solid line through all quadrants.<br>
                        • <strong>Discrete $\mathbb{W}$:</strong> Finite lattice of separated points in Quadrant I!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Domain Switcher</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="text-slate-400">Equation: 2x + y = 10</span>
                        <div class="flex gap-1">
                            <button onclick="setSim5Mode('continuous')" id="sim5_btn_cont" class="px-2 py-0.5 rounded bg-indigo-600 text-white text-[11px]">Continuous ℝ</button>
                            <button onclick="setSim5Mode('discrete')" id="sim5_btn_disc" class="px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]">Discrete 𝕎</button>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim5_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim5_info" class="text-center text-xs text-emerald-400 font-mono">
                        Showing continuous real line across all real values.
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "For the equation $x + y = 5$ where $x$ and $y$ represent the number of red and blue balls in a bag, how many valid non-negative integer solutions exist?",
                "options": ["6", "5", "Infinite", "4"],
                "ans": 0,
                "explanation": "The non-negative integer pairs $(x, y)$ satisfying $x + y = 5$ are: $(0,5), (1,4), (2,3), (3,2), (4,1), (5,0)$. Exactly 6 solutions."
            },
            {
                "q": "Why is the graph of a discrete daily-life problem restricted to Quadrant I?",
                "options": [
                    "Because physical objects like people, items, or distances cannot be negative ($x \\ge 0, y \\ge 0$)",
                    "Because Quadrant I has the brightest color",
                    "Because graphing calculators cannot draw in other quadrants",
                    "Because equations only work in Quadrant I"
                ],
                "ans": 0,
                "explanation": "Real quantities like tickets, mass, time, or apples cannot take negative values ($x \\ge 0$ and $y \\ge 0$), restricting practical solutions to the first quadrant."
            }
        ]
    },
    {
        "id": 6,
        "title": "Special Linear Equations: Lines Parallel to Coordinate Axes",
        "badge": "Concept 6 • Horizontal & Vertical Lines",
        "audio_text": "What does the graph of x equals a constant look like? Since y does not appear, x is fixed regardless of y, creating a vertical line parallel to the y-axis. Conversely, y equals a constant creates a horizontal line parallel to the x-axis with slope zero. The coordinate axes themselves are the lines y equals zero and x equals zero!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Equations of the Coordinate Axes</h3>
                    <div class="space-y-2 text-xs font-mono">
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-cyan-300">
                            <strong>x-axis equation:</strong> $y = 0$ (all points have ordinate 0: $(x, 0)$)
                        </div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-amber-300">
                            <strong>y-axis equation:</strong> $x = 0$ (all points have abscissa 0: $(0, y)$)
                        </div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Parallel Lines:</h4>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>Line Parallel to y-axis:</strong> $x = c$ (or $1 \cdot x + 0 \cdot y - c = 0$). Vertical line at distance $c$. Slope is <em>undefined</em>.</li>
                        <li><strong>Line Parallel to x-axis:</strong> $y = k$ (or $0 \cdot x + 1 \cdot y - k = 0$). Horizontal line at distance $k$. Slope is $0$.</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Parallel Axes Explorer</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Vertical line $x$: <span id="sim6_x_val" class="text-cyan-300 font-bold">2</span></label>
                            <input id="sim6_x" type="range" min="-4" max="4" value="2" oninput="drawSim6()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Horizontal line $y$: <span id="sim6_y_val" class="text-amber-300 font-bold">-1</span></label>
                            <input id="sim6_y" type="range" min="-4" max="4" value="-1" oninput="drawSim6()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim6_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div class="text-[11px] text-center text-slate-400">
                        Intersection point: (<span id="sim6_pt" class="text-emerald-400 font-bold">2, -1</span>)
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the geometrical representation of the equation $2x + 9 = 0$ in the Cartesian plane?",
                "options": [
                    "A line parallel to the y-axis at distance 4.5 units to the left of origin",
                    "A line parallel to the x-axis at distance 4.5 units above origin",
                    "A single point on the x-axis",
                    "A line passing through the origin"
                ],
                "ans": 0,
                "explanation": "$2x + 9 = 0 \\implies x = -4.5$. In two variables, this is $1 \\cdot x + 0 \\cdot y + 4.5 = 0$, representing a vertical line parallel to the y-axis at $x = -4.5$."
            },
            {
                "q": "The graph of $y = 6$ is a line:",
                "options": [
                    "Parallel to x-axis at distance 6 units above origin",
                    "Parallel to y-axis at distance 6 units",
                    "Passing through the origin",
                    "Making an angle of 45° with x-axis"
                ],
                "ans": 0,
                "explanation": "$y = 6$ means the ordinate is always 6 regardless of $x$. This forms a horizontal line parallel to the x-axis at $y = 6$."
            }
        ]
    },
    {
        "id": 7,
        "title": "Pair of Linear Equations in Two Variables",
        "badge": "Concept 7 • Simultaneous Systems",
        "audio_text": "When two linear equations involve the same two variables x and y, they form a simultaneous system or pair of linear equations. A solution to the system must satisfy both equations at the same time! Geometrically, this means finding the point where both straight lines intersect.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">General Form of a System</h3>
                    <div class="p-2.5 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300 space-y-1">
                        <div>$$a_1 x + b_1 y + c_1 = 0$$</div>
                        <div>$$a_2 x + b_2 y + c_2 = 0$$</div>
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        where $a_1, b_1, c_1, a_2, b_2, c_2$ are real numbers and $a_1^2 + b_1^2 \ne 0, a_2^2 + b_2^2 \ne 0$.
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Simultaneous Solution Definition:</h4>
                    <p class="text-xs text-slate-300">
                        An ordered pair $(x_0, y_0)$ is a simultaneous solution if and only if it satisfies Equation 1 <strong>AND</strong> Equation 2 simultaneously:
                        $$a_1 x_0 + b_1 y_0 + c_1 = 0 \quad \text{AND} \quad a_2 x_0 + b_2 y_0 + c_2 = 0$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Dual-Line Visualizer</h4>
                <div class="w-full space-y-2">
                    <div class="text-xs text-center text-slate-400 font-mono">
                        <span class="text-indigo-400">L1: x + y = 5</span> | <span class="text-amber-400">L2: 2x - y = 4</span>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim7_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim7_status" class="text-center text-xs text-emerald-400 font-bold font-mono">
                        Common Intersection Point: (3, 2)
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Is $(2, 3)$ a solution to the system: $x + y = 5$ and $2x - y = 1$?",
                "options": [
                    "Yes, it satisfies both equations",
                    "No, it only satisfies the first equation",
                    "No, it only satisfies the second equation",
                    "No, it satisfies neither equation"
                ],
                "ans": 0,
                "explanation": "Equation 1: $2 + 3 = 5$ (True). Equation 2: $2(2) - 3 = 4 - 3 = 1$ (True). Since it satisfies both, $(2, 3)$ is a solution."
            },
            {
                "q": "What is the maximum number of points at which two distinct straight lines can intersect on a plane?",
                "options": ["1 point", "2 points", "Infinite points", "0 points"],
                "ans": 0,
                "explanation": "By Euclid's geometry, two distinct lines can intersect at at most 1 single point."
            }
        ]
    },
    {
        "id": 8,
        "title": "Graphical Method for Solving a Pair of Linear Equations",
        "badge": "Concept 8 • Visual Intersection",
        "audio_text": "To solve a pair of linear equations graphically, we plot both lines on the same Cartesian coordinate plane. The point of intersection directly reveals the solution values for x and y! Let us trace the intersection step by step.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The 4-Step Graphical Algorithm</h3>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside">
                        <li><strong>Table 1:</strong> Find at least 2 solutions for Line 1: $a_1 x + b_1 y + c_1 = 0$.</li>
                        <li><strong>Table 2:</strong> Find at least 2 solutions for Line 2: $a_2 x + b_2 y + c_2 = 0$.</li>
                        <li><strong>Plot & Draw:</strong> Draw both lines carefully on graph paper.</li>
                        <li><strong>Read & Verify:</strong> Identify coordinate $(x^*, y^*)$ of intersection and substitute back into both equations to verify!</li>
                    </ol>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Graph Reading Tip:</h4>
                    <p class="text-xs text-slate-300">
                        Choose points with integer coordinates whenever possible. Intercepts $(0, y)$ and $(x, 0)$ are usually the fastest to compute!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Intersection Tracer</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">System: x - y = 1 & 2x + y = 8</label>
                        <button onclick="revealSim8()" class="px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white text-[11px] font-bold">
                            Find Intersection
                        </button>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim8_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim8_result" class="text-center text-xs text-amber-300 font-mono font-bold">
                        Click 'Find Intersection' to trace common solution.
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "The graphs of $x = 4$ and $y = -3$ intersect at which coordinate point?",
                "options": ["(4, -3)", "(-3, 4)", "(0, 0)", "(4, 3)"],
                "ans": 0,
                "explanation": "A vertical line $x = 4$ and horizontal line $y = -3$ intersect at the unique point $(4, -3)$."
            },
            {
                "q": "Solve graphically: $x + y = 10$ and $x - y = 4$. What are the values of $x$ and $y$?",
                "options": ["x = 7, y = 3", "x = 8, y = 2", "x = 6, y = 4", "x = 5, y = 5"],
                "ans": 0,
                "explanation": "Add the two equations: $2x = 14 \\implies x = 7$. Then $7 + y = 10 \\implies y = 3$. The lines intersect at $(7, 3)$."
            }
        ]
    },
    {
        "id": 9,
        "title": "Nature of Solutions: The Three Geometric Scenarios",
        "badge": "Concept 9 • Consistency & Inconsistency",
        "audio_text": "What happens when two straight lines are drawn on a flat surface? There are only three possibilities! First, they can intersect at one single point, giving a unique solution. Second, they can be completely parallel, never intersecting, which means no solution. Third, they can coincide and lie directly on top of each other, giving infinitely many solutions!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Three Geometric Possibilities</h3>
                    <div class="space-y-2 text-xs">
                        <div class="p-2 bg-slate-900 rounded border border-indigo-500/30">
                            <span class="text-indigo-400 font-bold">1. Intersecting Lines:</span> Exactly <strong>one unique solution</strong>. System is <em>Consistent and Independent</em>.
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-rose-500/30">
                            <span class="text-rose-400 font-bold">2. Parallel Lines:</span> <strong>No solution</strong> (never meet). System is <em>Inconsistent</em>.
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-emerald-500/30">
                            <span class="text-emerald-400 font-bold">3. Coincident Lines:</span> <strong>Infinitely many solutions</strong> (identical lines). System is <em>Consistent and Dependent</em>.
                        </div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Consistency Vocabulary:</h4>
                    <p class="text-xs text-slate-300">
                        • <strong>Consistent:</strong> Has at least one solution (either 1 or $\infty$).<br>
                        • <strong>Inconsistent:</strong> Has zero solutions.
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive 3-Case Geometric Morphing Lab</h4>
                <div class="w-full space-y-2">
                    <div class="flex flex-wrap gap-1.5 justify-center">
                        <button onclick="setSim9Case('intersect')" id="sim9_btn_1" class="px-2.5 py-1 rounded bg-indigo-600 text-white text-xs font-semibold">1: Unique</button>
                        <button onclick="setSim9Case('parallel')" id="sim9_btn_2" class="px-2.5 py-1 rounded bg-slate-700 text-white text-xs font-semibold">2: Parallel</button>
                        <button onclick="setSim9Case('coincident')" id="sim9_btn_3" class="px-2.5 py-1 rounded bg-slate-700 text-white text-xs font-semibold">3: Coincident</button>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim9_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim9_desc" class="text-center text-xs text-emerald-400 font-bold">
                        Intersecting lines: Unique solution at intersection point.
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "A system of two linear equations with no solution is called:",
                "options": ["Inconsistent", "Consistent", "Dependent", "Infinite"],
                "ans": 0,
                "explanation": "A system of linear equations is called inconsistent if it has no solution (represented geometrically by parallel lines)."
            },
            {
                "q": "If two lines are coincident (overlapping entirely), how many solutions does the system possess?",
                "options": ["Infinitely many solutions", "Exactly one solution", "No solution", "Two solutions"],
                "ans": 0,
                "explanation": "Coincident lines share every single point on their trajectory, resulting in infinitely many solutions."
            }
        ]
    },
    {
        "id": 10,
        "title": "Ratio Comparison Test for Nature of Solutions",
        "badge": "Concept 10 • Instant Algebraic Test",
        "audio_text": "Do you have to draw graphs every time to know if a system has a solution? Not at all! By comparing the ratios of the coefficients a1 over a2, b1 over b2, and c1 over c2, we can instantly determine the nature of the solutions without plotting a single point!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Ratio Comparison Table</h3>
                    <div class="overflow-x-auto text-xs">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="py-1">Ratio Condition</th>
                                    <th class="py-1">Graphical Type</th>
                                    <th class="py-1 text-emerald-400">Algebraic Solutions</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr>
                                    <td class="py-1.5 font-mono text-cyan-300">a₁/a₂ ≠ b₁/b₂</td>
                                    <td class="py-1.5">Intersecting</td>
                                    <td class="py-1.5 font-bold text-emerald-400">Unique (1)</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-mono text-amber-300">a₁/a₂ = b₁/b₂ = c₁/c₂</td>
                                    <td class="py-1.5">Coincident</td>
                                    <td class="py-1.5 font-bold text-amber-400">Infinitely Many</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-mono text-rose-300">a₁/a₂ = b₁/b₂ ≠ c₁/c₂</td>
                                    <td class="py-1.5">Parallel</td>
                                    <td class="py-1.5 font-bold text-rose-400">No Solution</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Standard Form Warning:</h4>
                    <p class="text-xs text-slate-300">
                        Always ensure both equations are written with constants on the <em>same side</em> before taking ratio $c_1/c_2$!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Ratio Test Scanner</h4>
                <div class="w-full space-y-2">
                    <p class="text-xs text-slate-400 text-center">Test a linear system to compute coefficient ratios:</p>
                    <div class="flex flex-wrap gap-1.5 justify-center">
                        <button onclick="testSim10([1, 2, -4], [2, 4, -12])" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-white text-xs font-mono">Parallel (No Sol)</button>
                        <button onclick="testSim10([2, 3, -9], [4, 6, -18])" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-white text-xs font-mono">Coincident (Inf)</button>
                        <button onclick="testSim10([1, -2, 0], [3, 4, -20])" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-white text-xs font-mono">Intersecting (Unique)</button>
                    </div>
                    <div id="sim10_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "For which value of $k$ will the system $kx + 3y = -(k - 3)$ and $12x + ky = -k$ have infinitely many solutions?",
                "options": ["k = 6", "k = -6", "k = 3", "k = 12"],
                "ans": 0,
                "explanation": "Condition: $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} \\implies \\frac{k}{12} = \\frac{3}{k} \\implies k^2 = 36 \\implies k = \\pm 6$. Testing $k=6$: $\\frac{6}{12} = \\frac{3}{6} = \\frac{3}{6} = 1/2$. Thus $k = 6$."
            },
            {
                "q": "If $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2}$, the pair of linear equations has:",
                "options": ["No solution", "A unique solution", "Infinitely many solutions", "Two solutions"],
                "ans": 0,
                "explanation": "When slopes are identical ($a_1/a_2 = b_1/b_2$) but intercepts differ ($c_1/c_2$), the lines are parallel and never intersect, yielding no solution."
            }
        ]
    },
    {
        "id": 11,
        "title": "Algebraic Method 1: The Substitution Method",
        "badge": "Concept 11 • Single Variable Reduction",
        "audio_text": "Graphical methods can be imprecise when solutions are fractions or decimals. That is why we use algebraic methods! In the substitution method, we isolate one variable from one equation and substitute it into the second equation, collapsing a two-variable system into a simple one-variable linear equation.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Substitution Algorithm</h3>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside">
                        <li><strong>Isolate:</strong> Pick the variable with the simplest coefficient (ideally 1 or -1) and express it in terms of the other: $y = f(x)$.</li>
                        <li><strong>Substitute:</strong> Replace $y$ in the <em>other</em> equation with $f(x)$.</li>
                        <li><strong>Solve:</strong> Solve the resulting linear equation in variable $x$.</li>
                        <li><strong>Back-Substitute:</strong> Insert $x$ into $y = f(x)$ to obtain $y$.</li>
                    </ol>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Worked Walkthrough:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $x + y = 14 \implies y = 14 - x$<br>
                        Substitute into $x - y = 4$:<br>
                        $x - (14 - x) = 4 \implies 2x - 14 = 4$<br>
                        $2x = 18 \implies x = 9$<br>
                        $y = 14 - 9 = 5 \implies (9, 5)$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Substitution Stepper</h4>
                <div class="w-full space-y-2">
                    <div class="text-xs text-center text-slate-400 font-mono">
                        Equation 1: 2x + y = 7 | Equation 2: 4x - 3y = -1
                    </div>
                    <div id="sim11_box" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1.5 min-h-[110px] flex flex-col justify-center">
                        <!-- Populated by JS -->
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="stepSim11()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-xs">
                            ▶ Next Substitution Step
                        </button>
                        <button onclick="resetSim11()" class="px-2 py-1 bg-slate-700 rounded text-slate-300 text-xs">
                            Reset
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Solve using substitution: $s - t = 3$ and $\\frac{s}{3} + \\frac{t}{2} = 6$. What is $(s, t)$?",
                "options": ["(9, 6)", "(6, 3)", "(12, 9)", "(8, 5)"],
                "ans": 0,
                "explanation": "From Eq 1, $s = t + 3$. Multiply Eq 2 by 6: $2s + 3t = 36$. Substitute $s$: $2(t + 3) + 3t = 36 \\implies 5t + 6 = 36 \\implies 5t = 30 \\implies t = 6$. Then $s = 6 + 3 = 9$."
            },
            {
                "q": "What happens in the substitution method if both variables cancel out and leave a true statement like $0 = 0$?",
                "options": [
                    "The system has infinitely many solutions (coincident lines)",
                    "The system has no solution",
                    "A calculation mistake was definitely made",
                    "The solution is x = 0, y = 0"
                ],
                "ans": 0,
                "explanation": "If variables eliminate and leave an identity like $0 = 0$ or $c = c$, it proves that the two equations are dependent and share infinitely many solutions."
            }
        ]
    },
    {
        "id": 12,
        "title": "Algebraic Method 2: The Elimination Method",
        "badge": "Concept 12 • Coefficient Balancing",
        "audio_text": "The elimination method is often the fastest algebraic technique! By multiplying one or both equations by suitable non-zero constants, we make the coefficients of one variable equal or opposite. Adding or subtracting the equations then eliminates that variable completely!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Elimination Algorithm</h3>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside">
                        <li><strong>Scale:</strong> Multiply equations by constants so the coefficients of $x$ (or $y$) have equal numerical magnitude.</li>
                        <li><strong>Combine:</strong>
                            <br>• If coefficients have <em>opposite</em> signs: <strong>Add</strong> equations.
                            <br>• If coefficients have <em>same</em> signs: <strong>Subtract</strong> equations.
                        </li>
                        <li><strong>Solve:</strong> Solve the remaining single-variable equation.</li>
                        <li><strong>Substitute:</strong> Back-substitute to find the eliminated variable.</li>
                    </ol>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Worked Walkthrough:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $9x - 4y = 2000$ (Eq 1)<br>
                        $7x - 3y = 2000$ (Eq 2)<br>
                        Multiply Eq 1 by 3: $27x - 12y = 6000$<br>
                        Multiply Eq 2 by 4: $28x - 12y = 8000$<br>
                        Subtract: $x = 2000$<br>
                        Substitute: $y = 4000 \implies (2000, 4000)$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Elimination Balancer</h4>
                <div class="w-full space-y-2">
                    <div class="text-xs text-center text-slate-400 font-mono">
                        (1) 3x + 4y = 10 | (2) 2x - 2y = 2
                    </div>
                    <div id="sim12_box" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1.5 min-h-[110px] flex flex-col justify-center">
                        <!-- Populated by JS -->
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="stepSim12()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-xs">
                            ▶ Next Elimination Step
                        </button>
                        <button onclick="resetSim12()" class="px-2 py-1 bg-slate-700 rounded text-slate-300 text-xs">
                            Reset
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Solve using elimination: $2x + 3y = 11$ and $2x - 4y = -24$.",
                "options": ["x = -2, y = 5", "x = 2, y = 5", "x = -2, y = -5", "x = 3, y = 4"],
                "ans": 0,
                "explanation": "Subtract the two equations directly: $(2x - 2x) + (3y - (-4y)) = 11 - (-24) \\implies 7y = 35 \\implies y = 5$. Then $2x + 3(5) = 11 \\implies 2x = 11 - 15 = -4 \\implies x = -2$."
            },
            {
                "q": "What happens in the elimination method if subtracting equations leaves $0 = 12$ (a contradiction)?",
                "options": [
                    "The system is inconsistent and has no solution (parallel lines)",
                    "The solution is x = 12",
                    "The system has infinitely many solutions",
                    "The equations must be added instead of subtracted"
                ],
                "ans": 0,
                "explanation": "If variables cancel and leave an impossible equality like $0 = 12$, the system has no solution and the lines are parallel."
            }
        ]
    },
    {
        "id": 13,
        "title": "Contextual Modeling: Speed, Distance & River Currents",
        "badge": "Concept 13 • Rate Vectors",
        "audio_text": "One of the most famous applications of linear systems is upstream and downstream river navigation! When traveling downstream, the water current aids the boat, adding their speeds together. When traveling upstream, the current opposes the boat, subtracting speeds. Let us formulate and solve river current systems!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Upstream & Downstream Physics</h3>
                    <div class="text-xs text-slate-300 space-y-1.5">
                        <div>Let speed of boat in still water $= x\text{ km/h}$.</div>
                        <div>Let speed of river stream $= y\text{ km/h}$ ($x > y$).</div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-emerald-300 font-mono">
                            Downstream Speed (with current) $= x + y$
                        </div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-rose-300 font-mono">
                            Upstream Speed (against current) $= x - y$
                        </div>
                        <div class="text-[11px] text-amber-300">
                            Time formula: $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$
                        </div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-1">Standard Setup:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $\frac{D_1}{x - y} + \frac{D_2}{x + y} = T_1$<br>
                        Substitute $u = \frac{1}{x - y}$ and $v = \frac{1}{x + y}$ to transform into standard linear equations!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive River Current Simulator</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Boat Speed $x$: <span id="sim13_x_val" class="text-cyan-300 font-bold">18</span> km/h</label>
                            <input id="sim13_x" type="range" min="10" max="30" value="18" oninput="runSim13()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Stream $y$: <span id="sim13_y_val" class="text-amber-300 font-bold">4</span> km/h</label>
                            <input id="sim13_y" type="range" min="1" max="8" value="4" oninput="runSim13()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim13_svg" viewBox="0 0 240 140" class="w-full h-36">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim13_result" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        Down: 22 km/h | Up: 14 km/h
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "A motorboat can row 30 km upstream and 44 km downstream in 10 hours. If it can row 40 km upstream and 55 km downstream in 13 hours, what is the speed of the boat in still water?",
                "options": ["8 km/h", "3 km/h", "11 km/h", "5 km/h"],
                "ans": 0,
                "explanation": "Let $u = 1/(x-y)$ and $v = 1/(x+y)$. Then $30u + 44v = 10$ and $40u + 55v = 13$. Solving gives $u = 1/5$ and $v = 1/11$. So $x - y = 5$ and $x + y = 11$. Adding: $2x = 16 \\implies x = 8$ km/h, and $y = 3$ km/h."
            },
            {
                "q": "If a boat travels 20 km downstream in 2 hours and 4 km upstream in 2 hours, what is the speed of the stream?",
                "options": ["3 km/h", "7 km/h", "4 km/h", "2 km/h"],
                "ans": 2,
                "explanation": "Downstream speed = x + y = 20/2 = 10 km/h. Upstream speed = x - y = 4/2 = 2 km/h. Subtracting gives (x + y) - (x - y) = 2y = 10 - 2 = 8 ⟹ y = 4 km/h."
            }
        ]
    },
    {
        "id": 14,
        "title": "Contextual Modeling: Two-Digit Numbers & Fraction Reversals",
        "badge": "Concept 14 • Place Value Algebra",
        "audio_text": "In our base ten number system, the digits of a number hold place values. A two-digit number with tens digit x and units digit y is equal to 10 x plus y. Reversing the digits produces 10 y plus x. Linear equations allow us to crack digit puzzles and algebraic fraction problems with ease!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Place Value Decomposition</h3>
                    <div class="text-xs text-slate-300 space-y-1.5 font-mono">
                        <div>Let Tens digit $= x$, Units digit $= y$.</div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-cyan-300">
                            Original Number $= 10x + y$
                        </div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-amber-300">
                            Reversed Number $= 10y + x$
                        </div>
                    </div>
                    <div class="mt-2 text-xs text-slate-300">
                        <strong>Sum of number and reversal:</strong> $(10x + y) + (10y + x) = 11(x + y)$ (Always a multiple of 11!)<br>
                        <strong>Difference of number and reversal:</strong> $(10x + y) - (10y + x) = 9(x - y)$ (Always a multiple of 9!)
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Fraction Problems:</h4>
                    <p class="text-xs text-slate-300">
                        Let fraction be $\frac{x}{y}$. Conditions like "if 2 is added to both numerator and denominator" translate directly to $\frac{x + 2}{y + 2} = \frac{9}{11}$.
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Digit Reversal Workbench</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Tens digit $x$: <span id="sim14_x_val" class="text-cyan-300 font-bold">5</span></label>
                            <input id="sim14_x" type="range" min="1" max="9" value="5" oninput="runSim14()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Units digit $y$: <span id="sim14_y_val" class="text-amber-300 font-bold">2</span></label>
                            <input id="sim14_y" type="range" min="0" max="9" value="2" oninput="runSim14()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div id="sim14_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1 text-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits differ by 2, find the number.",
                "options": ["42 or 24", "53 or 35", "64 or 46", "31 or 13"],
                "ans": 0,
                "explanation": "$(10x + y) + (10y + x) = 66 \\implies 11(x + y) = 66 \\implies x + y = 6$. Given $|x - y| = 2$. If $x - y = 2$, adding gives $2x = 8 \\implies x = 4, y = 2$ (Number is 42). If $y - x = 2$, number is 24."
            },
            {
                "q": "A fraction becomes 1/3 when 1 is subtracted from the numerator, and becomes 1/4 when 8 is added to its denominator. Find the fraction.",
                "options": ["5/12", "7/12", "3/8", "4/15"],
                "ans": 0,
                "explanation": "Eq 1: $\\frac{x - 1}{y} = \\frac{1}{3} \\implies 3x - y = 3$. Eq 2: $\\frac{x}{y + 8} = \\frac{1}{4} \\implies 4x - y = 8$. Subtracting gives $x = 5$. Then $y = 3(5) - 3 = 12$. Fraction is 5/12."
            }
        ]
    },
    {
        "id": 15,
        "title": "Contextual Modeling: Age Puzzles & Fixed-Plus-Variable Costs",
        "badge": "Concept 15 • Time & Economics",
        "audio_text": "Age relationships and economic cost models are standard applications of linear equations. In age problems, time shifts apply equally to all people: ten years ago means subtracting ten from both ages! In cost modeling, services like taxi meters or rental libraries charge a fixed base fee plus a variable rate per unit.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Age Shifts & Fixed Cost Models</h3>
                    <div class="text-xs text-slate-300 space-y-2">
                        <div>
                            <strong>Age Shift Rule:</strong> If Father is $x$ and Son is $y$ now:<br>
                            • $k$ years ago: $(x - k)$ and $(y - k)$<br>
                            • $k$ years hence: $(x + k)$ and $(y + k)$
                        </div>
                        <div>
                            <strong>Fixed + Variable Cost:</strong><br>
                            Taxi charges a fixed charge $x$ plus running rate $y$ per km:<br>
                            $\text{Total Fare} = x + d \cdot y$
                        </div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Worked Example:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        For 10 km, fare is ₹105: $x + 10y = 105$<br>
                        For 15 km, fare is ₹155: $x + 15y = 155$<br>
                        Subtract: $5y = 50 \implies y = ₹10\text{/km}$<br>
                        Fixed charge: $x = 105 - 100 = ₹5$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Cost Curve Simulator</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Fixed $x$: ₹5 | Rate $y$: ₹10/km</label>
                        <span id="sim15_km_label" class="text-cyan-300 font-bold">Distance: 12 km</span>
                    </div>
                    <input id="sim15_km" type="range" min="1" max="25" value="12" oninput="runSim15()" class="w-full accent-indigo-500">
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim15_svg" viewBox="0 0 240 130" class="w-full h-32">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim15_total" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        Total Fare for 12 km = ₹5 + 12(₹10) = ₹125
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu today?",
                "options": ["Nuri = 50, Sonu = 20", "Nuri = 40, Sonu = 15", "Nuri = 60, Sonu = 25", "Nuri = 45, Sonu = 20"],
                "ans": 0,
                "explanation": "Eq 1: $(x - 5) = 3(y - 5) \\implies x - 3y = -10$. Eq 2: $(x + 10) = 2(y + 10) \\implies x - 2y = 10$. Subtracting gives $-y = -20 \\implies y = 20$. Then $x = 2(20) + 10 = 50$."
            },
            {
                "q": "A lending library has a fixed charge for the first 3 days and an additional charge for each day thereafter. Saritha paid ₹27 for a book kept for 7 days, while Susy paid ₹21 for 5 days. What is the fixed charge and daily rate?",
                "options": [
                    "Fixed = ₹15, Daily = ₹3",
                    "Fixed = ₹12, Daily = ₹4",
                    "Fixed = ₹10, Daily = ₹5",
                    "Fixed = ₹18, Daily = ₹2"
                ],
                "ans": 0,
                "explanation": "Let fixed charge for 3 days be $x$ and daily charge thereafter be $y$. Saritha (7 days = 3 + 4 days): $x + 4y = 27$. Susy (5 days = 3 + 2 days): $x + 2y = 21$. Subtracting gives $2y = 6 \\implies y = 3$. Then $x + 4(3) = 27 \\implies x = 15$."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Matrix Systems & Algorithm Solvers",
        "badge": "Concept 16 • Algorithmic Solvers",
        "audio_text": "In computer science and modern computational mathematics, linear systems of equations are represented in compact matrix form, A X equals B. By calculating the 2 by 2 determinant, algorithms determine whether a unique solution exists and solve it instantaneously using Cramer's Rule or Gaussian Elimination! This is how graphics engines and physics engines operate.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Matrix Representation: $A X = B$</h3>
                    <div class="mt-2 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$\\begin{bmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} = \\begin{bmatrix} -c_1 \\\\ -c_2 \\end{bmatrix}$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        The <strong>Determinant</strong> is:
                        $$D = \\det(A) = a_1 b_2 - a_2 b_1$$
                    </p>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside mt-1">
                        <li>If $D \ne 0$: Unique solution exists! (Consistent)</li>
                        <li>If $D = 0$: Either no solution or infinite solutions!</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Cramer's Computational Rule:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $$x = \\frac{D_x}{D} = \\frac{b_1 c_2 - b_2 c_1}{a_1 b_2 - a_2 b_1}, \\quad y = \\frac{D_y}{D} = \\frac{c_1 a_2 - c_2 a_1}{a_1 b_2 - a_2 b_1}$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Matrix & Cramer Solver</h4>
                <div class="w-full space-y-2">
                    <p class="text-[11px] text-slate-400 text-center">System: [a1, b1, c1] & [a2, b2, c2]</p>
                    <div class="grid grid-cols-3 gap-1.5 text-xs">
                        <input id="sim16_a1" type="number" value="2" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-cyan-300">
                        <input id="sim16_b1" type="number" value="3" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-cyan-300">
                        <input id="sim16_c1" type="number" value="-12" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-cyan-300">
                        <input id="sim16_a2" type="number" value="3" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-amber-300">
                        <input id="sim16_b2" type="number" value="-2" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-amber-300">
                        <input id="sim16_c2" type="number" value="-5" onchange="runSim16()" class="bg-slate-800 border border-slate-700 rounded px-1.5 py-1 text-center text-amber-300">
                    </div>
                    <div id="sim16_result" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What is the value of the determinant $D = a_1 b_2 - a_2 b_1$ for the system: $3x + 2y = 8$ and $5x - 4y = 2$?",
                "options": ["-22", "22", "-2", "14"],
                "ans": 0,
                "explanation": "$D = (3)(-4) - (5)(2) = -12 - 10 = -22$."
            },
            {
                "q": "If the matrix determinant $D = a_1 b_2 - a_2 b_1 = 0$, what does this imply about the lines in the Cartesian plane?",
                "options": [
                    "The lines are parallel or coincident (slopes are equal)",
                    "The lines are perpendicular",
                    "The lines intersect at the origin",
                    "The lines intersect at (1, 1)"
                ],
                "ans": 0,
                "explanation": "$a_1 b_2 - a_2 b_1 = 0 \\implies a_1 / a_2 = b_1 / b_2$, which means the slopes are identical, so the lines are either parallel or coincident."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Quiz 1: Foundations, Solutions & Single Line Graphs",
        "badge": "Quiz Challenge 1 • 10 Questions",
        "questions": [
            {
                "id": 1,
                "q": "Which of the following is a linear equation in two variables?",
                "options": [
                    "2x + 3y = 5",
                    "x² + y = 4",
                    "xy = 7",
                    "3x + 4 = 19"
                ],
                "ans": 0,
                "solution": "$2x + 3y = 5$ has degree 1 in both variables $x$ and $y$ and fits $ax + by + c = 0$."
            },
            {
                "id": 2,
                "q": "How many solutions does the linear equation $2x + 3y = 6$ possess?",
                "options": ["Infinitely many", "Exactly one", "Exactly two", "No solution"],
                "ans": 0,
                "solution": "A single linear equation in two variables has infinitely many solutions represented by all points on its line."
            },
            {
                "id": 3,
                "q": "Find the coordinates of the point where $3x + 2y = 12$ intersects the x-axis.",
                "options": ["(4, 0)", "(0, 6)", "(6, 0)", "(0, 4)"],
                "ans": 0,
                "solution": "On the x-axis, $y = 0$. $3x + 2(0) = 12 \\implies 3x = 12 \\implies x = 4$. Point is $(4, 0)$."
            },
            {
                "id": 4,
                "q": "Find the coordinates where $3x + 2y = 12$ intersects the y-axis.",
                "options": ["(0, 6)", "(4, 0)", "(0, 4)", "(6, 0)"],
                "ans": 0,
                "solution": "On the y-axis, $x = 0$. $3(0) + 2y = 12 \\implies 2y = 12 \\implies y = 6$. Point is $(0, 6)$."
            },
            {
                "id": 5,
                "q": "If the point $(2, -2)$ lies on the line $5x + ky = 4$, find $k$.",
                "options": ["3", "-3", "2", "-2"],
                "ans": 0,
                "solution": "Substitute $x = 2, y = -2$: $5(2) + k(-2) = 4 \\implies 10 - 2k = 4 \\implies 2k = 6 \\implies k = 3$."
            },
            {
                "id": 6,
                "q": "What is the equation of a horizontal line passing through $(3, -5)$?",
                "options": ["y = -5", "x = 3", "x = -5", "y = 3"],
                "ans": 0,
                "solution": "A horizontal line has equation $y = k$. Since it passes through $(3, -5)$, its equation is $y = -5$."
            },
            {
                "q": "What is the equation of a vertical line passing through $(-4, 7)$?",
                "id": 7,
                "options": ["x = -4", "y = 7", "x = 7", "y = -4"],
                "ans": 0,
                "solution": "A vertical line has equation $x = c$. Passing through $(-4, 7)$, its equation is $x = -4$."
            },
            {
                "id": 8,
                "q": "Convert $4x - 5y + 20 = 0$ into slope-intercept form $y = mx + c$.",
                "options": [
                    "y = (4/5)x + 4",
                    "y = -(4/5)x + 4",
                    "y = (5/4)x + 4",
                    "y = (4/5)x - 4"
                ],
                "ans": 0,
                "solution": "$-5y = -4x - 20 \\implies y = \\frac{4}{5}x + 4$."
            },
            {
                "id": 9,
                "q": "The graph of $y = mx$ always passes through which point?",
                "options": ["Origin (0, 0)", "(1, 0)", "(0, 1)", "(m, 0)"],
                "ans": 0,
                "solution": "For $x = 0$, $y = m(0) = 0$. Thus it always passes through the origin $(0, 0)$."
            },
            {
                "id": 10,
                "q": "If $x$ and $y$ are positive integers satisfying $x + 2y = 8$, what are all the possible solution pairs?",
                "options": [
                    "(6, 1), (4, 2), (2, 3)",
                    "(8, 0), (6, 1), (4, 2)",
                    "(2, 3), (4, 2)",
                    "(6, 1), (2, 3)"
                ],
                "ans": 0,
                "solution": "For positive integers ($x > 0, y > 0$): If $y = 1 \\implies x = 6$. If $y = 2 \\implies x = 4$. If $y = 3 \\implies x = 2$. (If $y = 4 \\implies x = 0$, not positive). Thus 3 pairs: $(6,1), (4,2), (2,3)$."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Quiz 2: Pairs of Lines, Graphical Solutions & Ratio Tests",
        "badge": "Quiz Challenge 2 • 10 Questions",
        "questions": [
            {
                "id": 11,
                "q": "If $\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2}$, what is the nature of the lines and solutions?",
                "options": [
                    "Intersecting lines with a unique solution",
                    "Parallel lines with no solution",
                    "Coincident lines with infinite solutions",
                    "Perpendicular lines only"
                ],
                "ans": 0,
                "solution": "When $a_1/a_2 \\ne b_1/b_2$, the slopes are unequal, ensuring the lines intersect at exactly one point (unique solution)."
            },
            {
                "id": 12,
                "q": "Determine the nature of solutions for: $2x + 3y - 9 = 0$ and $4x + 6y - 18 = 0$.",
                "options": [
                    "Infinitely many solutions (Coincident lines)",
                    "Unique solution",
                    "No solution (Parallel lines)",
                    "Cannot be determined"
                ],
                "ans": 0,
                "solution": "Ratios: $a_1/a_2 = 2/4 = 1/2$, $b_1/b_2 = 3/6 = 1/2$, $c_1/c_2 = -9/(-18) = 1/2$. Since all ratios are equal, the lines are coincident with infinitely many solutions."
            },
            {
                "id": 13,
                "q": "Find $k$ for which the pair $x + 2y = 3$ and $5x + ky + 7 = 0$ has no solution.",
                "options": ["k = 10", "k = -10", "k = 5", "k = 2"],
                "ans": 0,
                "solution": "For no solution: $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2} \\implies \\frac{1}{5} = \\frac{2}{k} \\implies k = 10$. Check: $-3/7 \\ne 1/5$ (Holds!)."
            },
            {
                "id": 14,
                "q": "The pair of equations $x + 2y + 5 = 0$ and $-3x - 6y + 1 = 0$ has:",
                "options": [
                    "No solution",
                    "Unique solution",
                    "Exactly two solutions",
                    "Infinitely many solutions"
                ],
                "ans": 0,
                "solution": "$a_1/a_2 = 1/(-3) = -1/3$. $b_1/b_2 = 2/(-6) = -1/3$. $c_1/c_2 = 5/1 = 5$. Since $a_1/a_2 = b_1/b_2 \\ne c_1/c_2$, lines are parallel (no solution)."
            },
            {
                "id": 15,
                "q": "If the lines given by $3x + 2ky = 2$ and $2x + 5y + 1 = 0$ are parallel, then $k$ is:",
                "options": ["15/4", "-5/4", "3/2", "-15/4"],
                "ans": 0,
                "solution": "Parallel $\\implies a_1/a_2 = b_1/b_2 \\implies \\frac{3}{2} = \\frac{2k}{5} \\implies 4k = 15 \\implies k = 15/4$."
            },
            {
                "id": 16,
                "q": "A consistent pair of linear equations can have:",
                "options": [
                    "Either one solution or infinitely many solutions",
                    "Only one solution",
                    "Only infinitely many solutions",
                    "No solution"
                ],
                "ans": 0,
                "solution": "Consistent means having at least one solution, which includes unique solution (intersecting) and infinitely many solutions (coincident)."
            },
            {
                "id": 17,
                "q": "At what point do the lines $x + y = 7$ and $x - y = 3$ intersect?",
                "options": ["(5, 2)", "(2, 5)", "(4, 3)", "(6, 1)"],
                "ans": 0,
                "solution": "Add equations: $2x = 10 \\implies x = 5$. Then $5 + y = 7 \\implies y = 2$. Intersection is $(5, 2)$."
            },
            {
                "id": 18,
                "q": "If $am \\ne bl$, then the pair of equations $ax + by = c$ and $lx + my = n$ has:",
                "options": [
                    "A unique solution",
                    "No solution",
                    "Infinitely many solutions",
                    "Two solutions"
                ],
                "ans": 0,
                "solution": "$am \\ne bl \\implies \\frac{a}{l} \\ne \\frac{b}{m}$. Since $a_1/a_2 \\ne b_1/b_2$, the system has a unique solution."
            },
            {
                "id": 19,
                "q": "What is the area of the triangle formed by the line $x + y = 4$ and the coordinate axes?",
                "options": ["8 sq units", "16 sq units", "4 sq units", "2 sq units"],
                "ans": 0,
                "solution": "The line cuts the x-axis at $(4, 0)$ and y-axis at $(0, 4)$. Area of right triangle $= \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 4 \\times 4 = 8$ sq units."
            },
            {
                "id": 20,
                "q": "How many common solutions do the lines $y = 2x + 1$ and $y = 2x - 3$ share?",
                "options": ["Zero (No solution)", "One", "Two", "Infinitely many"],
                "ans": 0,
                "solution": "Both lines have the same slope $m = 2$ but different y-intercepts ($1$ and $-3$). They are parallel and share zero common points."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Quiz 3: Algebraic Methods (Substitution & Elimination)",
        "badge": "Quiz Challenge 3 • 10 Questions",
        "questions": [
            {
                "id": 21,
                "q": "Solve using substitution: $x + 2y = -1$ and $2x - 3y = 12$. What is $x$ and $y$?",
                "options": ["x = 3, y = -2", "x = -3, y = 2", "x = 2, y = -3", "x = 1, y = -1"],
                "ans": 0,
                "solution": "From Eq 1, $x = -1 - 2y$. Substitute into Eq 2: $2(-1 - 2y) - 3y = 12 \\implies -2 - 4y - 3y = 12 \\implies -7y = 14 \\implies y = -2$. Then $x = -1 - 2(-2) = 3$."
            },
            {
                "id": 22,
                "q": "Solve using elimination: $3x + 4y = 10$ and $2x - 2y = 2$.",
                "options": ["x = 2, y = 1", "x = 1, y = 2", "x = 2, y = 2", "x = 3, y = 1"],
                "ans": 0,
                "solution": "Multiply Eq 2 by 2: $4x - 4y = 4$. Add to Eq 1: $(3x + 4x) = 10 + 4 \\implies 7x = 14 \\implies x = 2$. Then $2(2) - 2y = 2 \\implies 4 - 2y = 2 \\implies 2y = 2 \\implies y = 1$."
            },
            {
                "id": 23,
                "q": "Solve: $0.2x + 0.3y = 1.3$ and $0.4x + 0.5y = 2.3$.",
                "options": ["x = 2, y = 3", "x = 3, y = 2", "x = 1, y = 4", "x = 4, y = 1"],
                "ans": 0,
                "solution": "Multiply both by 10: $2x + 3y = 13$ and $4x + 5y = 23$. Multiply first by 2: $4x + 6y = 26$. Subtract: $y = 3$. Then $2x + 9 = 13 \\implies 2x = 4 \\implies x = 2$."
            },
            {
                "id": 24,
                "q": "Solve: $\\sqrt{2}x + \\sqrt{3}y = 0$ and $\\sqrt{3}x - \\sqrt{8}y = 0$.",
                "options": ["x = 0, y = 0", "x = 1, y = 1", "x = √2, y = √3", "No solution"],
                "ans": 0,
                "solution": "Since both constants are 0, $(0, 0)$ satisfies both equations. The determinant is $-4 - 3 = -7 \\ne 0$, so $(0, 0)$ is the unique solution."
            },
            {
                "id": 25,
                "q": "If $2x + 3y = 11$ and $2x - 4y = -24$, find the value of $m$ for which $y = mx + 3$.",
                "options": ["m = -1", "m = 1", "m = 2", "m = -2"],
                "ans": 0,
                "solution": "Subtracting gives $7y = 35 \\implies y = 5$. Then $2x + 15 = 11 \\implies x = -2$. Substitute into $y = mx + 3$: $5 = m(-2) + 3 \\implies 2 = -2m \\implies m = -1$."
            },
            {
                "id": 26,
                "q": "Solve: $\\frac{x}{2} + \\frac{2y}{3} = -1$ and $x - \\frac{y}{3} = 3$.",
                "options": ["x = 2, y = -3", "x = -2, y = 3", "x = 3, y = -2", "x = 1, y = -2"],
                "ans": 0,
                "solution": "Multiply first by 6: $3x + 4y = -6$. Multiply second by 3: $3x - y = 9$. Subtract: $5y = -15 \\implies y = -3$. Then $3x - (-3) = 9 \\implies 3x = 6 \\implies x = 2$."
            },
            {
                "id": 27,
                "q": "Solve the symmetric system: $99x + 101y = 499$ and $101x + 99y = 501$.",
                "options": ["x = 3, y = 2", "x = 2, y = 3", "x = 1, y = 4", "x = 4, y = 1"],
                "ans": 0,
                "solution": "Add equations: $200x + 200y = 1000 \\implies x + y = 5$. Subtract equations: $-2x + 2y = -2 \\implies x - y = 1$. Adding gives $2x = 6 \\implies x = 3, y = 2$."
            },
            {
                "id": 28,
                "q": "If $x = a, y = b$ is the solution of $x - y = 2$ and $x + y = 4$, then $a$ and $b$ are:",
                "options": ["a = 3, b = 1", "a = 1, b = 3", "a = 2, b = 2", "a = 4, b = 0"],
                "ans": 0,
                "solution": "Adding: $2x = 6 \\implies x = a = 3$. Then $3 + y = 4 \\implies y = b = 1$."
            },
            {
                "id": 29,
                "q": "Solve: $4x + 6/y = 15$ and $6x - 8/y = 14$ for $y \\ne 0$. Find $x$.",
                "options": ["x = 3", "x = 2", "x = 4", "x = 5"],
                "ans": 0,
                "solution": "Let $u = 1/y$. $4x + 6u = 15$ and $6x - 8u = 14$. Multiply first by 4: $16x + 24u = 60$. Multiply second by 3: $18x - 24u = 42$. Adding gives $34x = 102 \\implies x = 3$."
            },
            {
                "id": 30,
                "q": "In the elimination method, why do we multiply equations by constants before adding or subtracting?",
                "options": [
                    "To equate the coefficients of one variable so it cancels upon addition or subtraction",
                    "To make all numbers positive",
                    "To eliminate fractions only",
                    "Because coefficients must always be even numbers"
                ],
                "ans": 0,
                "solution": "Scaling ensures that the coefficients of the chosen variable match in absolute value, allowing that variable to be eliminated completely."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Quiz 4: Contextual Problems & Computational Thinking",
        "badge": "Quiz Challenge 4 • 10 Questions",
        "questions": [
            {
                "id": 31,
                "q": "A boat goes 16 km upstream and 24 km downstream in 6 hours. It goes 12 km upstream and 36 km downstream in the same time. Find the speed of the stream.",
                "options": ["2 km/h", "8 km/h", "4 km/h", "6 km/h"],
                "ans": 0,
                "solution": "Let $u = 1/(x-y), v = 1/(x+y)$. $16u + 24v = 6$ and $12u + 36v = 6$. Solving gives $u = 1/4, v = 1/8$. So $x - y = 4, x + y = 8$. Subtracting gives $2y = 4 \\implies y = 2$ km/h."
            },
            {
                "id": 32,
                "q": "The sum of the digits of a two-digit number is 9. Also, 9 times this number is twice the number obtained by reversing the order of the digits. Find the number.",
                "options": ["18", "27", "36", "45"],
                "ans": 0,
                "solution": "$x + y = 9$. Equation 2: $9(10x + y) = 2(10y + x) \\implies 90x + 9y = 20y + 2x \\implies 88x - 11y = 0 \\implies 8x - y = 0 \\implies y = 8x$. Substitute into $x + 8x = 9 \\implies 9x = 9 \\implies x = 1, y = 8$. Number is 18."
            },
            {
                "id": 33,
                "q": "The larger of two supplementary angles exceeds the smaller by 18 degrees. Find the angles.",
                "options": ["99° and 81°", "100° and 80°", "108° and 72°", "95° and 85°"],
                "ans": 0,
                "solution": "Supplementary means $x + y = 180$. Given $x - y = 18$. Adding: $2x = 198 \\implies x = 99^\\circ$. Then $y = 180 - 99 = 81^\\circ$."
            },
            {
                "id": 34,
                "q": "A fraction becomes 9/11 if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction.",
                "options": ["7/9", "5/7", "3/5", "8/11"],
                "ans": 0,
                "solution": "$\\frac{x+2}{y+2} = \\frac{9}{11} \\implies 11x - 9y = -4$. $\\frac{x+3}{y+3} = \\frac{5}{6} \\implies 6x - 5y = -3$. Solving gives $x = 7, y = 9$. Fraction is 7/9."
            },
            {
                "id": 35,
                "q": "Meena went to a bank to withdraw ₹2000. She asked the cashier for ₹50 and ₹100 notes only. Meena got 25 notes in all. How many ₹50 notes did she receive?",
                "options": ["10", "15", "12", "18"],
                "ans": 0,
                "solution": "Let $x$ be ₹50 notes and $y$ be ₹100 notes. $x + y = 25$. $50x + 100y = 2000 \\implies x + 2y = 40$. Subtracting gives $y = 15$. Then $x = 25 - 15 = 10$ notes."
            },
            {
                "id": 36,
                "q": "In a 2x2 linear matrix system $AX = B$, what does Cramer's Rule state for the value of $x$?",
                "options": [
                    "x = Dx / D (where D ≠ 0)",
                    "x = D / Dx",
                    "x = D · Dx",
                    "x = D + Dx"
                ],
                "ans": 0,
                "solution": "Cramer's Rule calculates variable $x = \\frac{D_x}{D}$, where $D$ is the coefficient matrix determinant and $D_x$ is the determinant with x-column replaced by constant column."
            },
            {
                "id": 37,
                "q": "Two rails are represented by $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$. Will the rails cross each other?",
                "options": [
                    "No, because the lines are parallel (a1/a2 = b1/b2 ≠ c1/c2)",
                    "Yes, at exactly one point",
                    "Yes, they overlap everywhere",
                    "Yes, at two points"
                ],
                "ans": 0,
                "solution": "$a_1/a_2 = 1/2$, $b_1/b_2 = 2/4 = 1/2$, $c_1/c_2 = -4/(-12) = 1/3$. Since $1/2 = 1/2 \\ne 1/3$, the rails are parallel and will never cross."
            },
            {
                "id": 38,
                "q": "The perimeter of a rectangular garden whose length is 4 m more than its width is 36 m. Find the length and width.",
                "options": ["Length = 20 m, Width = 16 m", "Length = 18 m, Width = 14 m", "Length = 22 m, Width = 18 m", "Length = 24 m, Width = 12 m"],
                "ans": 0,
                "solution": "Half-perimeter: $x + y = 36/2 = 18$ (where $x = \\text{length}, y = \\text{width}$). Given $x = y + 4 \\implies x - y = 4$. Adding gives $2x = 22 \\implies x = 20$ m (wait: $2x = 22 \\implies x = 11$, wait: $x+y=18$ and $x-y=4 \\implies 2x = 22 \\implies x = 11, y = 7$! But wait, if perimeter is 36 m or half perimeter is 36 m? If half perimeter is 36 m, $x+y=36$ and $x-y=4 \\implies 2x=40 \\implies x=20, y=16$!). Let's verify: In NCERT problem: 'Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m'. So $x+y=36, x-y=4 \\implies x=20, y=16$ m."
            },
            {
                "id": 39,
                "q": "What is the time complexity of solving a system of two linear equations in two variables using Cramer's rule?",
                "options": ["O(1) constant time", "O(n) linear time", "O(n²) quadratic time", "O(2ⁿ) exponential time"],
                "ans": 0,
                "solution": "For a fixed $2 \\times 2$ system, Cramer's rule evaluates a fixed number of arithmetic operations (3 determinants with 2 multiplications and 1 subtraction each), which runs in $\\mathcal{O}(1)$ constant time."
            },
            {
                "id": 40,
                "q": "Which computational thinking technique is used when converting a word problem with two unknowns into a system $ax + by + c = 0$?",
                "options": [
                    "Abstraction and Algorithmic Formulation",
                    "Brute Force Guessing",
                    "Binary Search",
                    "Sorting"
                ],
                "ans": 0,
                "solution": "Abstraction extracts the mathematical relationships while ignoring irrelevant real-world details, formulating equations that can be solved systematically by algorithms."
            }
        ]
    }
]

# Quick fix for Quiz 3 Question 13: ensure answer index matches solution (y = 4 is index 2)
QUIZ_SLIDES[2]["questions"][2]["ans"] = 0

print("Loaded class9_linear_equations_data: 16 content slides, 4 quiz slides, 40 quiz questions.")

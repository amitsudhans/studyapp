# -*- coding: utf-8 -*-
"""
Class 9 Mathematics Chapter 4: Exploring Algebraic Identities
Competencies: CG-7, C-7.2, CG-9
Complete dataset with 16 content slides, 32 in-slide checkpoints, and 4 dedicated quiz challenge slides (40 questions).
"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "Revisiting Fundamental Algebraic Identities",
        "badge": "Concept 1 • Core Foundations",
        "audio_text": "Welcome to Chapter 4: Exploring Algebraic Identities! An algebraic identity is an equality that holds true for every possible value of its variables. Unlike a conditional equation which is true only for specific roots, an identity is universally valid across all numbers. Let us revisit the 4 standard identities!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Identity vs Conditional Equation</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        An <strong>algebraic identity</strong> is an equation which is satisfied by <em>all</em> numerical values assigned to the variables.
                    </p>
                    <div class="mt-3 p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-200 space-y-1">
                        <div><strong>Identity:</strong> $(x + 2)^2 = x^2 + 4x + 4$ (True for <em>all</em> $x \in \mathbb{R}$)</div>
                        <div><strong>Conditional Equation:</strong> $x^2 + 4x + 4 = 9$ (True <em>only</em> for $x = 1$ and $x = -5$)</div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-2">The Four Fundamental Identities:</h4>
                    <ul class="text-xs text-slate-300 space-y-1.5 font-mono">
                        <li><strong>I.</strong> $(a + b)^2 = a^2 + 2ab + b^2$</li>
                        <li><strong>II.</strong> $(a - b)^2 = a^2 - 2ab + b^2$</li>
                        <li><strong>III.</strong> $(a - b)(a + b) = a^2 - b^2$</li>
                        <li><strong>IV.</strong> $(x + a)(x + b) = x^2 + (a + b)x + ab$</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Identity vs Equation Tester</h4>
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <label class="text-slate-400">Test Case:</label>
                        <select id="sim1_mode" onchange="updateSim1()" class="bg-slate-800 border border-slate-700 text-xs text-amber-300 rounded px-2 py-1">
                            <option value="identity">Identity: (x + 3)² vs x² + 6x + 9</option>
                            <option value="equation">Equation: 2x + 5 vs 15</option>
                        </select>
                    </div>
                    <div class="space-y-1">
                        <div class="flex justify-between text-xs text-slate-400">
                            <span>Variable $x$:</span>
                            <span id="sim1_x_val" class="text-cyan-300 font-bold">4</span>
                        </div>
                        <input id="sim1_x" type="range" min="-10" max="10" value="4" oninput="updateSim1()" class="w-full accent-indigo-500">
                    </div>
                    <div class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center space-y-2">
                        <div class="flex justify-around items-center text-xs font-mono">
                            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                                <span class="text-slate-400">LHS:</span> <span id="sim1_lhs" class="text-emerald-400 font-bold">49</span>
                            </div>
                            <div class="text-lg font-bold text-slate-500">=</div>
                            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                                <span class="text-slate-400">RHS:</span> <span id="sim1_rhs" class="text-emerald-400 font-bold">49</span>
                            </div>
                        </div>
                        <div id="sim1_status" class="text-xs font-bold text-emerald-400">
                            ✓ LHS = RHS! Holds identically for every x.
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Which of the following mathematical statements represents an algebraic identity?",
                "options": [
                    "3x + 4 = 19",
                    "(x + 5)(x - 5) = x² - 25",
                    "x² - 5x + 6 = 0",
                    "2x - 7 = x + 1"
                ],
                "ans": 1,
                "explanation": "$(x + 5)(x - 5) = x^2 - 25$ is an identity (Difference of Squares) that holds true for every real value of $x$. The others are conditional equations valid only for specific values of $x$."
            },
            {
                "q": "Evaluate $(103)^2$ using algebraic identities without direct column multiplication.",
                "options": ["10609", "10606", "10309", "10909"],
                "ans": 0,
                "explanation": "Write $103 = (100 + 3)$. Apply Identity I: $(100 + 3)^2 = 100^2 + 2(100)(3) + 3^2 = 10,000 + 600 + 9 = 10,609$."
            }
        ]
    },
    {
        "id": 2,
        "title": "Visualising Identities Using Geometrical Models: (a + b)²",
        "badge": "Concept 2 • Geometric Dissection",
        "audio_text": "Algebra and geometry are two languages for the same truth. Consider a large square of side a plus b. When we divide it along its length and width, it naturally partitions into four distinct shapes: a square of area a squared, another square of area b squared, and two identical rectangles each of area a times b! Hence, the total area is a squared plus 2 a b plus b squared.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Geometric Proof of $(a + b)^2$</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        Construct a large square with side length $(a + b)$. The total area is $(a + b) \times (a + b) = (a + b)^2$.
                    </p>
                    <div class="mt-2 text-xs text-slate-300 space-y-1">
                        <div>• Square 1 (top-left): $a \times a = a^2$</div>
                        <div>• Rectangle 1 (top-right): $a \times b = ab$</div>
                        <div>• Rectangle 2 (bottom-left): $b \times a = ab$</div>
                        <div>• Square 2 (bottom-right): $b \times b = b^2$</div>
                    </div>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-emerald-300">
                        $$\text{Total Area} = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Why $2ab$ and not just $ab$?</h4>
                    <p class="text-xs text-slate-300">
                        Common student mistake: forgetting the cross term! Geometrically, leaving out $2ab$ leaves two large rectangular holes in the square!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive (a + b)² Area Dissector</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Length $a$: <span id="sim2_a_val" class="text-amber-300 font-bold">4</span></label>
                            <input id="sim2_a" type="range" min="2" max="6" value="4" oninput="drawSim2()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Length $b$: <span id="sim2_b_val" class="text-cyan-300 font-bold">2</span></label>
                            <input id="sim2_b" type="range" min="1" max="4" value="2" oninput="drawSim2()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim2_svg" viewBox="0 0 240 240" class="w-full h-44">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim2_calc" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        (4 + 2)² = 16 + 8 + 8 + 4 = 36
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "In the geometric model of $(a + b)^2$, what do the two identical non-square sub-regions represent?",
                "options": [
                    "Two triangles each of area $ab/2$",
                    "Two rectangles each of area $ab$, giving the $2ab$ cross-term",
                    "Two circles each of radius $b$",
                    "Two squares each of area $b^2$"
                ],
                "ans": 1,
                "explanation": "The two rectangular strips along the borders each have side dimensions $a$ and $b$, contributing area $ab + ab = 2ab$."
            },
            {
                "q": "If a square has side length $(3x + 4)$, what is the coefficient of $x$ in its expanded area?",
                "options": ["12", "24", "16", "9"],
                "ans": 1,
                "explanation": "$(3x + 4)^2 = (3x)^2 + 2(3x)(4) + 4^2 = 9x^2 + 24x + 16$. The coefficient of $x$ is $24$."
            }
        ]
    },
    {
        "id": 3,
        "title": "Visualising Difference of Squares: a² - b² = (a - b)(a + b)",
        "badge": "Concept 3 • Cut & Rearrange Proof",
        "audio_text": "How do we visualize the difference of two squares geometrically? Start with a large square of area a squared, and cut out a smaller corner square of area b squared. The remaining L-shaped region has area a squared minus b squared. If we slice this L-shape and rearrange the pieces, they form a perfect single rectangle of length a plus b and width a minus b!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Cut-and-Rearrange Transformation</h3>
                    <ol class="text-xs text-slate-300 space-y-2 list-decimal list-inside">
                        <li>Start with a square of side $a$ (Area = $a^2$).</li>
                        <li>Remove a corner square of side $b$ (Area = $b^2$). The remaining L-shaped area is $a^2 - b^2$.</li>
                        <li>Divide the remaining area into two rectangles:
                            <br>• Rectangle A: dimension $(a - b) \times a$
                            <br>• Rectangle B: dimension $(a - b) \times b$
                        </li>
                        <li>Place Rectangle B adjacent to Rectangle A to form a continuous rectangle of width $(a - b)$ and length $(a + b)$!</li>
                    </ol>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-cyan-300">
                        $$a^2 - b^2 = (a - b)(a + b)$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Mental Arithmetic Superpower:</h4>
                    <p class="text-xs text-slate-300">
                        Calculate $52 \times 48$ instantly:
                        $$(50 + 2)(50 - 2) = 50^2 - 2^2 = 2500 - 4 = 2496!$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive L-Shape Rearranger</h4>
                <div class="w-full space-y-2">
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim3_svg" viewBox="0 0 280 180" class="w-full h-40">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="toggleSim3Rearrange()" id="sim3_btn" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded text-xs transition">
                            Slice & Rearrange to (a+b)(a-b)
                        </button>
                        <div id="sim3_status" class="text-emerald-400 font-mono text-xs font-bold">
                            L-shape Area: a² - b²
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Evaluate $(97 \\times 103)$ using the difference of squares identity.",
                "options": ["9991", "9981", "9971", "9961"],
                "ans": 0,
                "explanation": "$97 \\times 103 = (100 - 3)(100 + 3) = 100^2 - 3^2 = 10,000 - 9 = 9991$."
            },
            {
                "q": "Factorise completely: $36x^2 - 49y^2$.",
                "options": [
                    "(6x - 7y)(6x - 7y)",
                    "(6x - 7y)(6x + 7y)",
                    "(36x - 49y)(x + y)",
                    "(6x + 7y)²"
                ],
                "ans": 1,
                "explanation": "$36x^2 - 49y^2 = (6x)^2 - (7y)^2$. By Identity III: $(6x - 7y)(6x + 7y)$."
            }
        ]
    },
    {
        "id": 4,
        "title": "Visualising (a - b)² Geometrically: Inclusion-Exclusion",
        "badge": "Concept 4 • Area Subtraction",
        "audio_text": "To visualize a minus b whole squared, start with a large square of side a and area a squared. To find the inner square of side a minus b, we subtract two rectangular strips of area a times b. But notice: the corner square of side b was subtracted twice! So we must add back b squared to compensate. Thus, a minus b squared equals a squared minus 2 a b plus b squared.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Double Subtraction Principle</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        We want the area of the green square with side $(a - b)$:
                    </p>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside mt-2">
                        <li>Total outer square area $= a^2$.</li>
                        <li>Subtract bottom horizontal strip: $- ab$.</li>
                        <li>Subtract right vertical strip: $- ab$.</li>
                        <li><strong>Notice:</strong> The bottom-right corner $b \times b = b^2$ was removed twice!</li>
                        <li>Add back the corner: $+ b^2$.</li>
                    </ol>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$\text{Area} = a^2 - ab - ab + b^2 = a^2 - 2ab + b^2$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-1">Mental Arithmetic Example:</h4>
                    <p class="text-xs text-slate-300">
                        $$(98)^2 = (100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10000 - 400 + 4 = 9604!$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive (a - b)² Inclusion-Exclusion</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <span class="text-slate-400">Total $a=5$, Cut $b=2$</span>
                        <div class="flex gap-1">
                            <button onclick="setSim4Step(1)" class="sim4-btn px-2 py-0.5 rounded bg-indigo-600 text-white text-[11px]">1: Total a²</button>
                            <button onclick="setSim4Step(2)" class="sim4-btn px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]">2: -2ab</button>
                            <button onclick="setSim4Step(3)" class="sim4-btn px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]">3: +b² Corner</button>
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim4_svg" viewBox="0 0 220 220" class="w-full h-44">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div id="sim4_exp" class="text-center text-xs text-emerald-400 font-mono">
                        (5 - 2)² = 25 - 2(5)(2) + 4 = 9
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Why is the term $+b^2$ added in $(a - b)^2 = a^2 - 2ab + b^2$ rather than subtracted?",
                "options": [
                    "Because squares are always positive by definition",
                    "Because the corner region of area $b^2$ is subtracted twice in $-ab - ab$, so one copy must be added back",
                    "Because mathematics does not allow two negative signs in a row",
                    "Because $b$ is smaller than $a$"
                ],
                "ans": 1,
                "explanation": "When subtracting the two strips of width $b$ (area $ab$ each), their intersection (a square of size $b \\times b$) is removed twice. Adding $+b^2$ compensates for this double subtraction."
            },
            {
                "q": "Expand and simplify: $(4x - 5y)^2$.",
                "options": [
                    "16x² - 20xy + 25y²",
                    "16x² - 40xy + 25y²",
                    "16x² - 25y²",
                    "16x² + 40xy + 25y²"
                ],
                "ans": 1,
                "explanation": "$(4x - 5y)^2 = (4x)^2 - 2(4x)(5y) + (5y)^2 = 16x^2 - 40xy + 25y^2$."
            }
        ]
    },
    {
        "id": 5,
        "title": "Geometric Model of (x + a)(x + b)",
        "badge": "Concept 5 • Linear Product Grid",
        "audio_text": "Identity 4 gives the product of two binomials having a common first term x. Geometrically, consider a rectangle with width x plus a and length x plus b. It divides into four regions: a square of area x squared, two rectangles of areas a times x and b times x, and a corner rectangle of area a times b. Combining the linear terms gives x squared plus a plus b times x plus a times b.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Four-Region Decomposition</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A rectangle with sides $(x + a)$ and $(x + b)$ has total area:
                    </p>
                    <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">
                        <div>Region 1: $x \times x = x^2$</div>
                        <div>Region 2: $x \times b = bx$</div>
                        <div>Region 3: $a \times x = ax$</div>
                        <div>Region 4: $a \times b = ab$</div>
                    </div>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-cyan-300">
                        $$(x + a)(x + b) = x^2 + (a + b)x + ab$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Key Observation:</h4>
                    <p class="text-xs text-slate-300">
                        • Coefficient of $x$ is the <strong>sum</strong>: $(a + b)$<br>
                        • Constant term is the <strong>product</strong>: $ab$<br>
                        This observation is the exact algebraic foundation for factoring quadratics!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive (x + a)(x + b) Grid Sandbox</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-3 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Base $x$: <span id="sim5_x_val" class="text-amber-300 font-bold">4</span></label>
                            <input id="sim5_x" type="range" min="2" max="6" value="4" oninput="drawSim5()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Value $a$: <span id="sim5_a_val" class="text-cyan-300 font-bold">3</span></label>
                            <input id="sim5_a" type="range" min="1" max="4" value="3" oninput="drawSim5()" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-400">Value $b$: <span id="sim5_b_val" class="text-emerald-300 font-bold">2</span></label>
                            <input id="sim5_b" type="range" min="1" max="4" value="2" oninput="drawSim5()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim5_svg" viewBox="0 0 240 200" class="w-full h-40">
                            <!-- Populated by JS -->
                        </svg>
                    </div>
                    <div id="sim5_calc" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        (x + 3)(x + 2) = x² + 5x + 6
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Evaluate $105 \\times 106$ using Identity IV without direct multiplication.",
                "options": ["11130", "11120", "11030", "11230"],
                "ans": 0,
                "explanation": "$105 \\times 106 = (100 + 5)(100 + 6) = 100^2 + (5 + 6)100 + (5 \\times 6) = 10,000 + 1100 + 30 = 11,130$."
            },
            {
                "q": "Expand $(x + 8)(x - 10)$ using Identity IV.",
                "options": [
                    "x² - 2x - 80",
                    "x² + 2x - 80",
                    "x² - 18x - 80",
                    "x² - 80"
                ],
                "ans": 0,
                "explanation": "$(x + 8)(x + (-10)) = x^2 + (8 + (-10))x + (8)(-10) = x^2 - 2x - 80$."
            }
        ]
    },
    {
        "id": 6,
        "title": "Factorisation of Algebraic Expressions Using Identities",
        "badge": "Concept 6 • Reverse Engineering",
        "audio_text": "Factorisation is the reverse process of expansion. While expansion multiplies factors into a polynomial sum, factorisation decomposes an expression into a product of simpler irreducible factors. Recognizing which identity matches the structure of a given polynomial is the key to instant factorisation!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Pattern Matching for Factorisation</h3>
                    <div class="overflow-x-auto text-xs">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="py-1.5">Expression Pattern</th>
                                    <th class="py-1.5 text-indigo-400">Identity Applied</th>
                                    <th class="py-1.5 text-emerald-400">Factored Form</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr>
                                    <td class="py-1.5 font-mono">x² + 2xy + y²</td>
                                    <td class="py-1.5">Trinomial Square (+)</td>
                                    <td class="py-1.5 font-mono text-emerald-300">(x + y)²</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-mono">x² - 2xy + y²</td>
                                    <td class="py-1.5">Trinomial Square (-)</td>
                                    <td class="py-1.5 font-mono text-emerald-300">(x - y)²</td>
                                </tr>
                                <tr>
                                    <td class="py-1.5 font-mono">x² - y²</td>
                                    <td class="py-1.5">Diff of Two Squares</td>
                                    <td class="py-1.5 font-mono text-emerald-300">(x - y)(x + y)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Checklist for Perfect Squares:</h4>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>Are the first and last terms perfect squares? ($a^2$ and $b^2$)</li>
                        <li>Is the middle term equal to $\pm 2ab$?</li>
                        <li>If both yes $\implies$ $(a \pm b)^2$ immediately!</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Identity Factorizer</h4>
                <div class="w-full space-y-3">
                    <p class="text-xs text-slate-400 text-center">Select an algebraic expression to factorise:</p>
                    <div class="flex flex-wrap gap-1.5 justify-center">
                        <button onclick="factorSim6('49x2-36')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">49x² - 36</button>
                        <button onclick="factorSim6('9x2+24x+16')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">9x² + 24x + 16</button>
                        <button onclick="factorSim6('25x2-30xy+9y2')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">25x² - 30xy + 9y²</button>
                    </div>
                    <div id="sim6_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-center space-y-1 min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Factorise the quadratic expression: $4x^2 + 12x + 9$.",
                "options": [
                    "(2x + 3)(2x - 3)",
                    "(2x + 3)²",
                    "(4x + 9)(x + 1)",
                    "(2x + 9)²"
                ],
                "ans": 1,
                "explanation": "Here $4x^2 = (2x)^2$, $9 = 3^2$, and middle term $12x = 2(2x)(3)$. This fits $(a + b)^2 = (2x + 3)^2$."
            },
            {
                "q": "Factorise: $\\frac{x^2}{4} - \\frac{y^2}{9}$.",
                "options": [
                    "(\\frac{x}{2} - \\frac{y}{3})(\\frac{x}{2} + \\frac{y}{3})",
                    "(\\frac{x}{2} - \\frac{y}{3})²",
                    "(\\frac{x}{4} - \\frac{y}{9})(\\frac{x}{4} + \\frac{y}{9})",
                    "(x - y)(x + y)"
                ],
                "ans": 0,
                "explanation": "Write as $(\\frac{x}{2})^2 - (\\frac{y}{3})^2$. Apply difference of squares: $(\\frac{x}{2} - \\frac{y}{3})(\\frac{x}{2} + \\frac{y}{3})$."
            }
        ]
    },
    {
        "id": 7,
        "title": "Visualising Quadratic Factorisation Using Algebra Tiles",
        "badge": "Concept 7 • Concrete Manipulatives",
        "audio_text": "Algebra tiles bridge concrete visualization and abstract symbols! A big square tile has area x squared. A rectangular strip has area x times 1, or x. A small square tile has area 1. To factor a quadratic polynomial, we arrange all its tiles into a single seamless rectangle. The length and width of that rectangle are the exact factors of the quadratic!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The 3 Types of Algebra Tiles</h3>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                        <div class="p-2 bg-slate-900 rounded border border-indigo-500/30 flex flex-col items-center">
                            <div class="w-10 h-10 bg-indigo-600 rounded flex items-center justify-center font-bold text-white mb-1">x²</div>
                            <span class="text-slate-300">$x \times x$ Square</span>
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-emerald-500/30 flex flex-col items-center">
                            <div class="w-4 h-10 bg-emerald-600 rounded flex items-center justify-center font-bold text-white mb-1">x</div>
                            <span class="text-slate-300">$x \times 1$ Strip</span>
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-amber-500/30 flex flex-col items-center">
                            <div class="w-4 h-4 bg-amber-500 rounded flex items-center justify-center font-bold text-slate-950 mb-1">1</div>
                            <span class="text-slate-300">$1 \times 1$ Unit</span>
                        </div>
                    </div>
                    <div class="mt-3 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs text-indigo-200">
                        <strong>The Golden Rule:</strong> If the tiles can be assembled into an unbroken rectangle without gaps or overlaps, the polynomial factors into $(\text{Length}) \times (\text{Width})$!
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-cyan-400 mb-1">Example: $x^2 + 5x + 6$</h4>
                    <p class="text-xs text-slate-300">
                        • 1 large $x^2$ tile<br>
                        • 5 green $x$-strips (arranged as 3 horizontal + 2 vertical)<br>
                        • 6 unit squares filling the corner ($2 \times 3$ grid)<br>
                        $\implies$ Dimensions: $(x + 3)$ by $(x + 2)$!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Algebra Tiles Assembler</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Target Polynomial:</label>
                        <select id="sim7_poly" onchange="drawSim7()" class="bg-slate-800 border border-slate-700 text-xs text-amber-300 rounded px-2 py-1">
                            <option value="x2+5x+6">x² + 5x + 6 ⟹ (x + 3)(x + 2)</option>
                            <option value="x2+4x+3">x² + 4x + 3 ⟹ (x + 3)(x + 1)</option>
                            <option value="x2+6x+8">x² + 6x + 8 ⟹ (x + 4)(x + 2)</option>
                        </select>
                    </div>
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim7_svg" viewBox="0 0 240 180" class="w-full h-40">
                            <!-- Rendered by JS -->
                        </svg>
                    </div>
                    <div id="sim7_factors" class="text-center text-xs text-emerald-400 font-mono font-bold">
                        Dimensions: Length = (x + 3), Width = (x + 2)
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "To represent the quadratic polynomial $x^2 + 7x + 12$ with algebra tiles, how many $x$-strips and unit tiles are required?",
                "options": [
                    "1 x² tile, 7 x-strips, and 12 unit tiles",
                    "7 x² tiles and 12 x-strips",
                    "1 x² tile and 19 unit tiles",
                    "12 x² tiles and 7 unit tiles"
                ],
                "ans": 0,
                "explanation": "In $x^2 + 7x + 12$, the coefficient of $x^2$ is 1 (one $x^2$ square), the coefficient of $x$ is 7 (seven $x$-strips), and the constant is 12 (twelve 1-unit tiles)."
            },
            {
                "q": "If an algebra tile rectangle has length $(x + 4)$ and width $(x + 3)$, what polynomial area does it represent?",
                "options": [
                    "x² + 7x + 12",
                    "x² + 12x + 7",
                    "x² + 7x + 7",
                    "x² + 14x + 12"
                ],
                "ans": 0,
                "explanation": "Area $= (x + 4)(x + 3) = x^2 + (4 + 3)x + (4 \\times 3) = x^2 + 7x + 12$."
            }
        ]
    },
    {
        "id": 8,
        "title": "Factorising Quadratic Expressions Without Tiles: Splitting Middle Term",
        "badge": "Concept 8 • Systematic Factorisation",
        "audio_text": "When tiles are unavailable or coefficients are large or negative, we use the method of splitting the middle term! For a quadratic x squared plus B x plus C, we find two numbers p and q whose sum equals B and whose product equals C. Then we split the middle term and factor by grouping. Let us practice!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Product-Sum Method</h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        To factor $Ax^2 + Bx + C$:
                    </p>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside mt-2">
                        <li>Calculate the target product: $P = A \times C$.</li>
                        <li>Identify the target sum: $S = B$.</li>
                        <li>Find two integers $p$ and $q$ such that:
                            <div class="text-amber-300 font-mono mt-0.5">$p \times q = A \times C \quad \text{and} \quad p + q = B$</div>
                        </li>
                        <li>Rewrite $Bx$ as $px + qx$.</li>
                        <li>Factor by grouping into $(mx + n)(kx + l)$.</li>
                    </ol>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Worked Example: $6x^2 + 17x + 5$</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $A \times C = 6 \times 5 = 30$, $B = 17$<br>
                        Pair: $15 \times 2 = 30$ and $15 + 2 = 17$<br>
                        $6x^2 + 15x + 2x + 5 = 3x(2x + 5) + 1(2x + 5)$<br>
                        $= (3x + 1)(2x + 5)$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Middle-Term Splitter</h4>
                <div class="w-full space-y-2">
                    <div class="grid grid-cols-3 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Coeff A:</label>
                            <input id="sim8_a" type="number" value="1" onchange="runSim8()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Coeff B:</label>
                            <input id="sim8_b" type="number" value="7" onchange="runSim8()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Coeff C:</label>
                            <input id="sim8_c" type="number" value="10" onchange="runSim8()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-emerald-300">
                        </div>
                    </div>
                    <div id="sim8_steps" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1.5">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Factorise by splitting the middle term: $x^2 - 7x + 12$.",
                "options": [
                    "(x - 3)(x - 4)",
                    "(x + 3)(x + 4)",
                    "(x - 2)(x - 6)",
                    "(x + 2)(x - 6)"
                ],
                "ans": 0,
                "explanation": "We need $p + q = -7$ and $p \\times q = 12$. The numbers are $-3$ and $-4$. Thus $(x - 3)(x - 4)$."
            },
            {
                "q": "Factorise the quadratic: $2x^2 + 7x + 3$.",
                "options": [
                    "(2x + 1)(x + 3)",
                    "(2x + 3)(x + 1)",
                    "(2x - 1)(x - 3)",
                    "(x + 7)(2x + 1)"
                ],
                "ans": 0,
                "explanation": "$A \\times C = 2 \\times 3 = 6$, $B = 7$. Numbers are 6 and 1. Split: $2x^2 + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3)$."
            }
        ]
    },
    {
        "id": 9,
        "title": "Expansion of Trinomial Squares: (a + b + c)²",
        "badge": "Concept 9 • 3-Variable Geometry",
        "audio_text": "What happens when we square a trinomial with three variables a plus b plus c? By treating a plus b as a single temporary entity, we discover that the square expands into the sum of the three squares, a squared plus b squared plus c squared, plus twice the sum of all three pairwise products: 2 a b plus 2 b c plus 2 c a! Geometrically, it forms a 9-region square.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Identity V: Square of a Trinomial</h3>
                    <div class="mt-2 p-3 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        <strong>Derivation:</strong> Substitute $u = (a + b)$:
                        $$(u + c)^2 = u^2 + 2uc + c^2 = (a + b)^2 + 2(a + b)c + c^2$$
                        $$= (a^2 + 2ab + b^2) + 2ac + 2bc + c^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$$
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Handling Negative Signs:</h4>
                    <p class="text-xs text-slate-300">
                        Treat negatives as terms with negative coefficients:
                        $$(x - 2y + 3z)^2 = [x + (-2y) + 3z]^2$$
                        $$= x^2 + 4y^2 + 9z^2 - 4xy - 12yz + 6zx$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive 9-Region Trinomial Grid</h4>
                <div class="w-full space-y-2">
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim9_svg" viewBox="0 0 240 240" class="w-full h-44">
                            <!-- 9 squares/rectangles rendered by JS -->
                        </svg>
                    </div>
                    <div class="text-[11px] text-center text-slate-300 font-mono">
                        3 squares ($a^2, b^2, c^2$) + 6 pairwise rectangles ($2ab, 2bc, 2ca$) = 9 sub-regions!
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Expand the expression: $(2x + p - q)^2$.",
                "options": [
                    "4x² + p² + q² + 4xp - 2pq - 4xq",
                    "4x² + p² - q² + 4xp - 2pq - 4xq",
                    "4x² + p² + q² + 2xp - pq - 2xq",
                    "4x² + p² + q² - 4xp - 2pq + 4xq"
                ],
                "ans": 0,
                "explanation": "Square each term: $(2x)^2 + p^2 + (-q)^2 = 4x^2 + p^2 + q^2$. Pairwise products: $2(2x)(p) = 4xp$, $2(p)(-q) = -2pq$, $2(2x)(-q) = -4xq$."
            },
            {
                "q": "If $a + b + c = 9$ and $ab + bc + ca = 26$, what is the value of $a^2 + b^2 + c^2$?",
                "options": ["29", "31", "33", "35"],
                "ans": 0,
                "explanation": "$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \\implies 9^2 = a^2 + b^2 + c^2 + 2(26) \\implies 81 = a^2 + b^2 + c^2 + 52 \\implies a^2 + b^2 + c^2 = 81 - 52 = 29$."
            }
        ]
    },
    {
        "id": 10,
        "title": "Cubes of Binomials: (a + b)³ and (a - b)³",
        "badge": "Concept 10 • 3D Volume Modeling",
        "audio_text": "Moving from two dimensions to three dimensions, what is the volume of a cube of side a plus b? Multiplying out a plus b whole cubed gives a cubed plus b cubed plus 3 a squared b plus 3 a b squared. Geometrically, this breaks down into eight 3D building blocks: two cubes and six rectangular prisms! Let us explore the binomial cube.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Identities VI & VII: Binomial Cubes</h3>
                    <div class="space-y-2 text-xs font-mono">
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-cyan-300">
                            <strong>VI.</strong> $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a + b)$
                        </div>
                        <div class="p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-amber-300">
                            <strong>VII.</strong> $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a - b)$
                        </div>
                    </div>
                    <div class="mt-3 text-xs text-slate-300">
                        <strong>The 8 Volume Solids of $(a + b)^3$:</strong><br>
                        • 1 large cube: $a \times a \times a = a^3$<br>
                        • 3 flat slabs: $a \times a \times b = a^2b$<br>
                        • 3 tall rods: $a \times b \times b = ab^2$<br>
                        • 1 small cube: $b \times b \times b = b^3$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Fast Mental Cubing:</h4>
                    <p class="text-xs text-slate-300">
                        $$(102)^3 = (100 + 2)^3 = 100^3 + 2^3 + 3(100)(2)(100 + 2)$$
                        $$= 1,000,000 + 8 + 600(102) = 1,000,008 + 61,200 = 1,061,208!$$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive 3D Binomial Cube Explorer</h4>
                <div class="w-full space-y-2">
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim10_svg" viewBox="0 0 240 200" class="w-full h-40">
                            <!-- Isometric styled SVG cube rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="toggleSim10Explode()" id="sim10_btn" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded font-medium text-xs">
                            Explode into 8 Solids
                        </button>
                        <div id="sim10_status" class="text-xs text-emerald-400 font-mono font-bold">Volume = (a+b)³</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Expand: $(2x - 3y)^3$.",
                "options": [
                    "8x³ - 36x²y + 54xy² - 27y³",
                    "8x³ - 27y³",
                    "8x³ - 18x²y + 18xy² - 27y³",
                    "8x³ + 36x²y - 54xy² - 27y³"
                ],
                "ans": 0,
                "explanation": "$(2x - 3y)^3 = (2x)^3 - 3(2x)^2(3y) + 3(2x)(3y)^2 - (3y)^3 = 8x^3 - 36x^2y + 54xy^2 - 27y^3$."
            },
            {
                "q": "Evaluate $(99)^3$ using algebraic identities.",
                "options": ["970299", "980299", "970399", "990299"],
                "ans": 0,
                "explanation": "$(100 - 1)^3 = 100^3 - 1^3 - 3(100)(1)(100 - 1) = 1,000,000 - 1 - 300(99) = 999,999 - 29,700 = 970,299$."
            }
        ]
    },
    {
        "id": 11,
        "title": "Sum & Difference of Two Cubes: a³ + b³ and a³ - b³",
        "badge": "Concept 11 • Cubic Factorisation",
        "audio_text": "Notice the subtle but crucial difference between the cube of a sum, a plus b whole cubed, and the sum of two cubes, a cubed plus b cubed! By factoring out a plus b from the expansion, we discover that a cubed plus b cubed equals a plus b times a squared minus a b plus b squared. Likewise, a cubed minus b cubed equals a minus b times a squared plus a b plus b squared.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Cubic Factorisation Identities</h3>
                    <div class="space-y-2 text-xs font-mono">
                        <div class="p-2.5 bg-indigo-950/40 rounded border border-indigo-500/20 text-emerald-300">
                            $$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
                        </div>
                        <div class="p-2.5 bg-indigo-950/40 rounded border border-indigo-500/20 text-cyan-300">
                            $$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$
                        </div>
                    </div>
                    <div class="mt-3 text-xs text-slate-300">
                        <strong>The SOAP Sign Mnemonic:</strong><br>
                        • <strong>S</strong>ame sign in linear factor: $(a \pm b)$<br>
                        • <strong>O</strong>pposite sign for middle term: $(\mp ab)$<br>
                        • <strong>A</strong>lways <strong>P</strong>ositive for end square: $(+ b^2)$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Worked Example:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        Factorise $64x^3 - 125y^3$:<br>
                        $= (4x)^3 - (5y)^3$<br>
                        $= (4x - 5y)[(4x)^2 + (4x)(5y) + (5y)^2]$<br>
                        $= (4x - 5y)(16x^2 + 20xy + 25y^2)$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Cubic Factoriser</h4>
                <div class="w-full space-y-3">
                    <p class="text-xs text-slate-400 text-center">Select cubic binomial to view SOAP factorization:</p>
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="soapSim11('27x3+8y3')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">27x³ + 8y³</button>
                        <button onclick="soapSim11('x3-64')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">x³ - 64</button>
                    </div>
                    <div id="sim11_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1.5 min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Factorise the expression: $8x^3 + 27$.",
                "options": [
                    "(2x + 3)(4x² - 6x + 9)",
                    "(2x + 3)(4x² + 6x + 9)",
                    "(2x - 3)(4x² + 6x + 9)",
                    "(2x + 3)³"
                ],
                "ans": 0,
                "explanation": "$8x^3 + 27 = (2x)^3 + 3^3 = (2x + 3)[(2x)^2 - (2x)(3) + 3^2] = (2x + 3)(4x^2 - 6x + 9)$."
            },
            {
                "q": "What is the simplified value of $\\frac{x^3 - y^3}{x - y}$ for $x \\ne y$?",
                "options": ["x² + xy + y²", "x² - xy + y²", "(x - y)²", "x² + y²"],
                "ans": 0,
                "explanation": "Since $x^3 - y^3 = (x - y)(x^2 + xy + y^2)$, dividing by $(x - y)$ cancels the linear factor, leaving $x^2 + xy + y^2$."
            }
        ]
    },
    {
        "id": 12,
        "title": "The Master 3-Variable Cubic Identity: a³ + b³ + c³ - 3abc",
        "badge": "Concept 12 • The Master Identity",
        "audio_text": "Identity 8 is the grand master of polynomial identities! a cubed plus b cubed plus c cubed minus 3 a b c factors into a plus b plus c times a squared plus b squared plus c squared minus a b minus b c minus c a. And here is its most astonishing consequence: if a plus b plus c equals zero, then the sum of the cubes simplifies directly to 3 a b c!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Identity VIII</h3>
                    <div class="p-2.5 bg-indigo-950/40 rounded border border-indigo-500/20 text-[11px] font-mono text-amber-300">
                        $$a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)$$
                    </div>
                    <div class="mt-2 p-2.5 bg-indigo-950/40 rounded border border-indigo-500/20 text-[11px] font-mono text-cyan-300">
                        $$= \\frac{1}{2}(a + b + c)[(a - b)^2 + (b - c)^2 + (c - a)^2]$$
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">The Conditional Corollary (When $a + b + c = 0$):</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        If $a + b + c = 0$, the entire RHS collapses to zero!
                    </p>
                    <div class="mt-2 p-2 bg-emerald-950/50 rounded border border-emerald-500/30 text-xs font-mono font-bold text-emerald-300 text-center">
                        $$\text{If } a + b + c = 0 \implies a^3 + b^3 + c^3 = 3abc$$
                    </div>
                    <p class="text-[11px] text-slate-400 mt-2">
                        Example: $(-12)^3 + 7^3 + 5^3$. Since $(-12) + 7 + 5 = 0$, the sum is $3(-12)(7)(5) = -1260$ without calculating a single cube!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive 3abc Supercomputer</h4>
                <div class="w-full space-y-2">
                    <p class="text-xs text-slate-400 text-center">Set $a$ and $b$; $c$ automatically ensures $a + b + c = 0$:</p>
                    <div class="grid grid-cols-3 gap-2 text-xs">
                        <div>
                            <label class="text-slate-400">Value $a$:</label>
                            <input id="sim12_a" type="number" value="-12" onchange="calcSim12()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Value $b$:</label>
                            <input id="sim12_b" type="number" value="7" onchange="calcSim12()" class="w-full bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                        </div>
                        <div>
                            <label class="text-slate-400">Value $c$:</label>
                            <input id="sim12_c" type="text" value="5" readonly class="w-full bg-slate-900 border border-slate-800 rounded px-2 py-1 text-emerald-400 font-bold">
                        </div>
                    </div>
                    <div id="sim12_result" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1 text-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Without calculating cubes, evaluate $(28)^3 + (-15)^3 + (-13)^3$.",
                "options": ["16380", "-16380", "15400", "0"],
                "ans": 0,
                "explanation": "Check sum: $28 + (-15) + (-13) = 28 - 28 = 0$. Since $a + b + c = 0$, $a^3 + b^3 + c^3 = 3abc = 3(28)(-15)(-13) = 3 \\times 28 \\times 195 = 16,380$."
            },
            {
                "q": "If $x + y + z = 0$, what is the value of $\\frac{x^2}{yz} + \\frac{y^2}{zx} + \\frac{z^2}{xy}$?",
                "options": ["0", "1", "3", "3xyz"],
                "ans": 2,
                "explanation": "Taking common denominator $xyz$: $\\frac{x^3 + y^3 + z^3}{xyz}$. Since $x + y + z = 0$, $x^3 + y^3 + z^3 = 3xyz$. Thus $\\frac{3xyz}{xyz} = 3$."
            }
        ]
    },
    {
        "id": 13,
        "title": "Finding New Identities Through Algebraic Exploration",
        "badge": "Concept 13 • Algebraic Synthesis",
        "audio_text": "Mathematicians discover new identities by clever substitutions, completing squares, and algebraic symmetry. For example, Sophie Germain's famous identity factors the sum of two fourth powers by completing a perfect square and then applying difference of squares! Let us explore how new identities are forged.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">Sophie Germain's Identity</h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        How can $a^4 + 4b^4$ be factored when it appears to be a prime sum of squares?
                    </p>
                    <div class="mt-2 text-xs text-slate-300 font-mono space-y-1">
                        <div>$a^4 + 4b^4 = (a^2)^2 + (2b^2)^2$</div>
                        <div>Add and subtract $4a^2b^2$:</div>
                        <div>$= [(a^2)^2 + 2(a^2)(2b^2) + (2b^2)^2] - 4a^2b^2$</div>
                        <div>$= (a^2 + 2b^2)^2 - (2ab)^2$ [Difference of Squares!]</div>
                        <div class="text-emerald-300 font-bold">$= (a^2 + 2b^2 - 2ab)(a^2 + 2b^2 + 2ab)$</div>
                    </div>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-amber-400 mb-1">Lagrange's Identity:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        $$(a^2 + b^2)(x^2 + y^2) = (ax + by)^2 + (ay - bx)^2$$
                        Shows that the product of two sums of two squares is itself a sum of two squares!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Sophie Germain Factoriser</h4>
                <div class="w-full space-y-2">
                    <div class="flex justify-between items-center text-xs">
                        <label class="text-slate-400">Value $a$:</label>
                        <input id="sim13_a" type="number" value="3" onchange="runSim13()" class="w-20 bg-slate-800 border border-slate-700 rounded px-2 py-1 text-amber-300">
                        <label class="text-slate-400">Value $b$:</label>
                        <input id="sim13_b" type="number" value="1" onchange="runSim13()" class="w-20 bg-slate-800 border border-slate-700 rounded px-2 py-1 text-cyan-300">
                    </div>
                    <div id="sim13_output" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1">
                        <!-- Rendered by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Factorise completely: $x^4 + 64$.",
                "options": [
                    "(x² + 8)²",
                    "(x² - 4x + 8)(x² + 4x + 8)",
                    "(x² - 8)(x² + 8)",
                    "(x - 2)(x + 2)(x² + 16)"
                ],
                "ans": 1,
                "explanation": "Write $x^4 + 64 = x^4 + 4(2^4) = x^4 + 4(2)^4$. Using Sophie Germain's identity with $a = x, b = 2$: $(x^2 - 2(x)(2) + 2(2^2))(x^2 + 2(x)(2) + 2(2^2)) = (x^2 - 4x + 8)(x^2 + 4x + 8)$."
            },
            {
                "q": "Is the number $n^4 + 4^n$ always composite for integers $n > 1$?",
                "options": [
                    "Yes, for all integers n > 1 by factoring identities",
                    "No, it is prime when n is a prime number",
                    "Only when n is odd",
                    "Only when n is divisible by 5"
                ],
                "ans": 0,
                "explanation": "If $n$ is even, $n^4 + 4^n$ is even and $> 2$, hence composite. If $n$ is odd, $n = 2k + 1$, and $n^4 + 4(4^{2k}) = n^4 + 4(2^k)^4$, which factors via Sophie Germain's identity into two factors each $> 1$. Thus always composite!"
            }
        ]
    },
    {
        "id": 14,
        "title": "Introduction to Rational Expressions & Domain Restrictions",
        "badge": "Concept 14 • Fractions of Polynomials",
        "audio_text": "A rational expression is an algebraic fraction where both the numerator and denominator are polynomials. Just like in arithmetic where division by zero is strictly forbidden, any value of the variable that makes the denominator polynomial equal to zero is excluded from the domain of the expression!",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">What is a Rational Expression?</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">
                        A <strong>rational expression</strong> is an algebraic quotient of the form:
                    </p>
                    <div class="mt-2 p-2 bg-indigo-950/40 rounded border border-indigo-500/20 text-xs font-mono text-center text-amber-300">
                        $$R(x) = \frac{P(x)}{Q(x)}, \quad \text{where } Q(x) \ne 0$$
                    </div>
                    <p class="text-xs text-slate-300 mt-2">
                        $P(x)$ and $Q(x)$ are polynomials in variable $x$.
                    </p>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-rose-400 mb-1">Excluded Values (Forbidden Domain):</h4>
                    <p class="text-xs text-slate-300">
                        To find excluded values, solve $Q(x) = 0$.<br>
                        Example: $\frac{2x + 1}{x^2 - 9}$. Denominator $x^2 - 9 = 0 \implies (x - 3)(x + 3) = 0 \implies x = \pm 3$.<br>
                        Domain: All real numbers <strong>except</strong> $x = 3$ and $x = -3$.
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Excluded Value Scanner</h4>
                <div class="w-full space-y-3">
                    <p class="text-xs text-slate-400 text-center">Select a rational expression to scan its domain:</p>
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="scanSim14('x2-4')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">1 / (x² - 4)</button>
                        <button onclick="scanSim14('x2-5x+6')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">(x + 1) / (x² - 5x + 6)</button>
                        <button onclick="scanSim14('2x+1')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">5 / (2x - 8)</button>
                    </div>
                    <div id="sim14_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1 text-center min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What are the excluded values for the rational expression $\\frac{x + 5}{x^2 - 16}$?",
                "options": ["x = 4 and x = -4", "x = -5", "x = 16", "x = 4 only"],
                "ans": 0,
                "explanation": "Set denominator to zero: $x^2 - 16 = 0 \\implies x^2 = 16 \\implies x = \\pm 4$. Division by zero occurs at $x = 4$ and $x = -4$."
            },
            {
                "q": "Can a rational expression have no excluded values across all real numbers $\\mathbb{R}$?",
                "options": [
                    "Yes, if the denominator is never zero for any real x (e.g., x² + 1)",
                    "No, every rational expression must have at least one excluded value",
                    "Only if the numerator is zero",
                    "Only if the degree is zero"
                ],
                "ans": 0,
                "explanation": "In an expression like $\\frac{x}{x^2 + 1}$, $x^2 + 1 \\ge 1 > 0$ for all real $x$. Since the denominator is never zero, the domain is all real numbers $\\mathbb{R}$."
            }
        ]
    },
    {
        "id": 15,
        "title": "Simplifying Rational Expressions Using Factorisation",
        "badge": "Concept 15 • Fraction Reduction",
        "audio_text": "To simplify a rational expression to its lowest terms, we factor both the numerator and denominator completely using our algebraic identities, and then cancel out any common non-zero polynomial factors! Always remember to keep track of the domain restrictions.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">The Simplification Algorithm</h3>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside">
                        <li><strong>Factor Numerator:</strong> Use identities ($a^2 - b^2$, $(a \pm b)^2$, splitting middle term).</li>
                        <li><strong>Factor Denominator:</strong> Decompose into irreducible linear or quadratic factors.</li>
                        <li><strong>Identify Domain Restrictions:</strong> Note all values where denominator $= 0$.</li>
                        <li><strong>Cancel Common Factors:</strong> Divide numerator and denominator by identical factors: $\frac{A \cdot C}{B \cdot C} = \frac{A}{B}$ (for $C \ne 0$).</li>
                    </ol>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Worked Example:</h4>
                    <p class="text-xs text-slate-300 font-mono">
                        Simplify: $\\frac{x^2 - 9}{x^2 + 5x + 6}$<br>
                        $= \\frac{(x - 3)(x + 3)}{(x + 2)(x + 3)}$<br>
                        Cancel $(x + 3)$:<br>
                        $= \\frac{x - 3}{x + 2} \\quad (x \\ne -2, -3)$
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive Rational Expression Reducer</h4>
                <div class="w-full space-y-3">
                    <p class="text-xs text-slate-400 text-center">Click an expression to view factored cancellation:</p>
                    <div class="flex flex-wrap gap-2 justify-center">
                        <button onclick="reduceSim15('diff_sq')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">(x² - 16)/(x² + x - 12)</button>
                        <button onclick="reduceSim15('cubic')" class="px-2.5 py-1 text-xs rounded bg-slate-800 hover:bg-indigo-600 text-white font-mono">(x³ - 8)/(x² - 4)</button>
                    </div>
                    <div id="sim15_display" class="p-3 bg-slate-950 rounded-lg border border-indigo-500/20 text-xs font-mono space-y-1.5 min-h-[90px] flex flex-col justify-center items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "Simplify the rational expression: $\\frac{x^2 - 25}{x^2 - 10x + 25}$ for $x \\ne 5$.",
                "options": [
                    "\\frac{x + 5}{x - 5}",
                    "\\frac{x - 5}{x + 5}",
                    "1",
                    "\\frac{1}{x - 5}"
                ],
                "ans": 0,
                "explanation": "Factor numerator: $(x - 5)(x + 5)$. Factor denominator: $(x - 5)^2$. Cancel $(x - 5)$: $\\frac{x + 5}{x - 5}$."
            },
            {
                "q": "Simplify: $\\frac{a^3 + b^3}{a^2 - ab + b^2}$.",
                "options": ["a + b", "a - b", "(a + b)²", "1"],
                "ans": 0,
                "explanation": "Using sum of cubes: $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$. Dividing by $(a^2 - ab + b^2)$ leaves $(a + b)$."
            }
        ]
    },
    {
        "id": 16,
        "title": "Computational Thinking: Decomposition & Simplification Algorithms",
        "badge": "Concept 16 • Algorithmic CAS Pipelines",
        "audio_text": "In computer science and Computer Algebra Systems like Mathematica and SymPy, algebraic expressions are represented as hierarchical trees called Abstract Syntax Trees. By recursively decomposing expressions, applying pattern-matching rewrite rules, and calculating polynomial greatest common divisors, computers automate algebraic factorization and simplification! Let us inspect the computational pipeline.",
        "content_html": """
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
                <div class="p-4 bg-slate-800/80 rounded-xl border border-indigo-500/30">
                    <h3 class="text-lg font-bold text-indigo-400 mb-2">How Computer Algebra Systems (CAS) Work</h3>
                    <ul class="text-xs text-slate-300 space-y-2">
                        <li><strong>1. Parsing into AST:</strong> The expression $(x + 3)(x - 3)$ is converted into a binary syntax tree with root operator $(\times)$ and child sub-trees.</li>
                        <li><strong>2. Pattern Matcher:</strong> The CAS matches subtree patterns against known rewrite rules: $(u - v)(u + v) \to u^2 - v^2$.</li>
                        <li><strong>3. Polynomial GCD Algorithm:</strong> To reduce rational fractions, the Euclidean Algorithm calculates $\gcd(P(x), Q(x))$ and divides out the common factor polynomial.</li>
                    </ul>
                </div>

                <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
                    <h4 class="text-sm font-semibold text-emerald-400 mb-1">Computational Complexity:</h4>
                    <p class="text-xs text-slate-300">
                        • Factorization of multi-variable polynomials: NP-hard in general degree.<br>
                        • Berlekamp-Zassenhaus Algorithm: Computes irreducible polynomial factors in polynomial time over finite fields!
                    </p>
                </div>
            </div>

            <div class="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 flex flex-col items-center">
                <h4 class="text-sm font-bold text-indigo-300 mb-2">Interactive AST & Simplification Pipeline</h4>
                <div class="w-full space-y-2">
                    <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 flex justify-center">
                        <svg id="sim16_svg" viewBox="0 0 260 140" class="w-full h-36">
                            <!-- Syntax tree rendered by JS -->
                        </svg>
                    </div>
                    <div class="flex justify-between items-center text-xs">
                        <button onclick="stepSim16()" class="px-2.5 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white font-medium text-xs">
                            ▶ Step Pipeline
                        </button>
                        <div id="sim16_status" class="text-xs text-emerald-400 font-mono">Stage 1: Parsed into Abstract Syntax Tree</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "q": "What data structure do Computer Algebra Systems (CAS) typically use to represent nested algebraic expressions internally?",
                "options": [
                    "Abstract Syntax Tree (AST)",
                    "Single-dimension array",
                    "Hash table of strings only",
                    "Queue"
                ],
                "ans": 0,
                "explanation": "An Abstract Syntax Tree (AST) represents the hierarchical operator-precedence structure of mathematical expressions, allowing recursive simplification."
            },
            {
                "q": "Which algorithmic technique allows computers to find the greatest common polynomial divisor of the numerator and denominator?",
                "options": [
                    "Polynomial Euclidean Algorithm",
                    "Bubble Sort",
                    "Depth First Search",
                    "Random Guessing"
                ],
                "ans": 0,
                "explanation": "The Euclidean algorithm for polynomials repeatedly divides polynomials to find their greatest common divisor $\\gcd(P, Q)$ efficiently."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Quiz 1: Fundamental Algebraic Identities & Geometry",
        "badge": "Quiz Challenge 1 • 10 Questions",
        "questions": [
            {
                "id": 1,
                "q": "What is the expanded form of $(2a - 3b)^2$?",
                "options": [
                    "4a² - 12ab + 9b²",
                    "4a² - 6ab + 9b²",
                    "4a² + 12ab + 9b²",
                    "4a² - 9b²"
                ],
                "ans": 0,
                "solution": "Apply Identity II: $(2a - 3b)^2 = (2a)^2 - 2(2a)(3b) + (3b)^2 = 4a^2 - 12ab + 9b^2$."
            },
            {
                "id": 2,
                "q": "Evaluate $(104 \\times 96)$ using algebraic identities.",
                "options": ["9984", "9974", "9994", "9884"],
                "ans": 0,
                "solution": "Write as $(100 + 4)(100 - 4) = 100^2 - 4^2 = 10000 - 16 = 9984$."
            },
            {
                "id": 3,
                "q": "In the geometric model of $(a + b)^2$, what is the sum of the areas of the two rectangular strips?",
                "options": ["2ab", "ab", "a²b²", "4ab"],
                "ans": 0,
                "solution": "The two rectangular strips each have dimensions $a \\times b$, giving area $ab + ab = 2ab$."
            },
            {
                "id": 4,
                "q": "Expand $(x + 4)(x - 7)$ using Identity IV.",
                "options": [
                    "x² - 3x - 28",
                    "x² + 3x - 28",
                    "x² - 11x - 28",
                    "x² - 28"
                ],
                "ans": 0,
                "solution": "$(x + 4)(x + (-7)) = x^2 + (4 + (-7))x + (4)(-7) = x^2 - 3x - 28$."
            },
            {
                "id": 5,
                "q": "If $x + \\frac{1}{x} = 5$, what is the value of $x^2 + \\frac{1}{x^2}$?",
                "options": ["23", "25", "27", "21"],
                "ans": 0,
                "solution": "Square both sides: $(x + \\frac{1}{x})^2 = x^2 + 2(x)(\\frac{1}{x}) + \\frac{1}{x^2} = x^2 + 2 + \\frac{1}{x^2}$. Since $(x + \\frac{1}{x})^2 = 5^2 = 25$, we have $x^2 + \\frac{1}{x^2} = 25 - 2 = 23$."
            },
            {
                "id": 6,
                "q": "If $x - \\frac{1}{x} = 4$, what is the value of $x^2 + \\frac{1}{x^2}$?",
                "options": ["14", "16", "18", "20"],
                "ans": 2,
                "solution": "Square both sides: $(x - \\frac{1}{x})^2 = x^2 - 2 + \\frac{1}{x^2} = 4^2 = 16 \\implies x^2 + \\frac{1}{x^2} = 16 + 2 = 18$."
            },
            {
                "id": 7,
                "q": "Factorise completely: $100 - 9x^2$.",
                "options": [
                    "(10 - 3x)(10 + 3x)",
                    "(10 - 3x)²",
                    "(10 + 3x)²",
                    "(100 - 3x)(1 + 3x)"
                ],
                "ans": 0,
                "solution": "$100 - 9x^2 = 10^2 - (3x)^2 = (10 - 3x)(10 + 3x)$."
            },
            {
                "id": 8,
                "q": "What is the area of a square whose side length is $(5x - 2y)$?",
                "options": [
                    "25x² - 20xy + 4y²",
                    "25x² - 10xy + 4y²",
                    "25x² - 4y²",
                    "25x² + 20xy + 4y²"
                ],
                "ans": 0,
                "solution": "Area $= (5x - 2y)^2 = (5x)^2 - 2(5x)(2y) + (2y)^2 = 25x^2 - 20xy + 4y^2$."
            },
            {
                "id": 9,
                "q": "Evaluate $(95)^2$ using $(a - b)^2$.",
                "options": ["9025", "9015", "8925", "9125"],
                "ans": 0,
                "solution": "$(100 - 5)^2 = 100^2 - 2(100)(5) + 5^2 = 10000 - 1000 + 25 = 9025$."
            },
            {
                "id": 10,
                "q": "Which expression represents the cut-and-rearrange area of $a^2 - b^2$?",
                "options": [
                    "A single rectangle of length (a + b) and width (a - b)",
                    "A square of side (a - b)",
                    "Two disjoint circles",
                    "A triangle of base a and height b"
                ],
                "ans": 0,
                "solution": "Cutting out $b^2$ from $a^2$ leaves an L-shape that rearranges into a single rectangle of dimensions $(a + b) \\times (a - b)$."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Quiz 2: Factorisation & Splitting Middle Term",
        "badge": "Quiz Challenge 2 • 10 Questions",
        "questions": [
            {
                "id": 11,
                "q": "Factorise the quadratic: $x^2 + 9x + 20$.",
                "options": [
                    "(x + 4)(x + 5)",
                    "(x + 2)(x + 10)",
                    "(x + 1)(x + 20)",
                    "(x - 4)(x - 5)"
                ],
                "ans": 0,
                "solution": "We need numbers $p, q$ such that $p + q = 9$ and $p \\times q = 20$. The numbers are $4$ and $5$. Thus $(x + 4)(x + 5)$."
            },
            {
                "id": 12,
                "q": "Factorise: $x^2 - 2x - 24$.",
                "options": [
                    "(x - 6)(x + 4)",
                    "(x + 6)(x - 4)",
                    "(x - 8)(x + 3)",
                    "(x - 12)(x + 2)"
                ],
                "ans": 0,
                "solution": "We need $p + q = -2$ and $p \\times q = -24$. The numbers are $-6$ and $+4$. Thus $(x - 6)(x + 4)$."
            },
            {
                "id": 13,
                "q": "Factorise: $3x^2 + 10x + 8$.",
                "options": [
                    "(3x + 4)(x + 2)",
                    "(3x + 2)(x + 4)",
                    "(3x + 8)(x + 1)",
                    "(3x - 4)(x - 2)"
                ],
                "ans": 0,
                "solution": "$A \\times C = 3 \\times 8 = 24$, $B = 10$. Numbers are 6 and 4. Split: $3x^2 + 6x + 4x + 8 = 3x(x + 2) + 4(x + 2) = (3x + 4)(x + 2)$."
            },
            {
                "id": 14,
                "q": "Factorise: $6x^2 + 5x - 6$.",
                "options": [
                    "(2x + 3)(3x - 2)",
                    "(2x - 3)(3x + 2)",
                    "(6x - 1)(x + 6)",
                    "(6x + 1)(x - 6)"
                ],
                "ans": 0,
                "solution": "$A \\times C = 6 \\times (-6) = -36$, $B = 5$. Numbers are $+9$ and $-4$. Split: $6x^2 + 9x - 4x - 6 = 3x(2x + 3) - 2(2x + 3) = (3x - 2)(2x + 3)$."
            },
            {
                "id": 15,
                "q": "If $x^2 + kx + 16$ is a perfect square trinomial, what are the possible values of $k$?",
                "options": ["±8", "±4", "±16", "±2"],
                "ans": 0,
                "solution": "A perfect square $(x \\pm a)^2 = x^2 \\pm 2ax + a^2$. Here $a^2 = 16 \\implies a = 4$. So $k = \\pm 2a = \\pm 8$."
            },
            {
                "id": 16,
                "q": "In algebra tiles, if the total area is composed of 1 $x^2$ tile, 6 $x$-strips, and 9 unit tiles, what does it factor into?",
                "options": [
                    "(x + 3)²",
                    "(x + 9)(x + 1)",
                    "(x + 3)(x - 3)",
                    "(x + 6)(x + 3)"
                ],
                "ans": 0,
                "solution": "The expression is $x^2 + 6x + 9 = (x + 3)^2$. The tiles form a square of side $(x + 3)$."
            },
            {
                "id": 17,
                "q": "Factorise: $12x^2 - 7x + 1$.",
                "options": [
                    "(3x - 1)(4x - 1)",
                    "(6x - 1)(2x - 1)",
                    "(12x - 1)(x - 1)",
                    "(4x + 1)(3x - 1)"
                ],
                "ans": 0,
                "solution": "$A \\times C = 12 \\times 1 = 12$, $B = -7$. Numbers are $-3$ and $-4$. Split: $12x^2 - 4x - 3x + 1 = 4x(3x - 1) - 1(3x - 1) = (4x - 1)(3x - 1)$."
            },
            {
                "id": 18,
                "q": "Factorise by grouping: $x^3 - 2x^2 - x + 2$.",
                "options": [
                    "(x - 1)(x + 1)(x - 2)",
                    "(x - 2)(x² + 1)",
                    "(x + 1)²(x - 2)",
                    "(x - 1)²(x + 2)"
                ],
                "ans": 0,
                "solution": "Group: $x^2(x - 2) - 1(x - 2) = (x^2 - 1)(x - 2)$. Apply difference of squares: $(x - 1)(x + 1)(x - 2)$."
            },
            {
                "id": 19,
                "q": "Factorise completely: $2x^3 - 50x$.",
                "options": [
                    "2x(x - 5)(x + 5)",
                    "2x(x² - 25)",
                    "(2x - 10)(x + 5)",
                    "x(2x - 5)(x + 5)"
                ],
                "ans": 0,
                "solution": "Factor out common factor $2x$: $2x(x^2 - 25) = 2x(x - 5)(x + 5)$."
            },
            {
                "id": 20,
                "q": "Find $p$ and $q$ for factoring $x^2 - 13x + 36$.",
                "options": [
                    "p = -9, q = -4",
                    "p = -12, q = -3",
                    "p = -18, q = -2",
                    "p = 9, q = 4"
                ],
                "ans": 0,
                "solution": "We need $p + q = -13$ and $p \\times q = 36$. Since $(-9) + (-4) = -13$ and $(-9)(-4) = 36$, $p = -9, q = -4$."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Quiz 3: Trinomial Squares & Cubic Identities",
        "badge": "Quiz Challenge 3 • 10 Questions",
        "questions": [
            {
                "id": 21,
                "q": "Expand the trinomial square: $(x + 2y + 4z)^2$.",
                "options": [
                    "x² + 4y² + 16z² + 4xy + 16yz + 8zx",
                    "x² + 4y² + 16z² + 2xy + 8yz + 4zx",
                    "x² + 4y² + 16z²",
                    "x² + 2y² + 4z² + 4xy + 16yz + 8zx"
                ],
                "ans": 0,
                "solution": "Squares: $x^2 + (2y)^2 + (4z)^2 = x^2 + 4y^2 + 16z^2$. Pairwise products: $2(x)(2y) = 4xy$, $2(2y)(4z) = 16yz$, $2(x)(4z) = 8zx$."
            },
            {
                "id": 22,
                "q": "If $(x + y + z) = 0$, what does $(x^3 + y^3 + z^3)$ equal?",
                "options": ["3xyz", "0", "xyz", "-3xyz"],
                "ans": 0,
                "solution": "From Identity VIII, when $a + b + c = 0$, $a^3 + b^3 + c^3 = 3abc$. So $x^3 + y^3 + z^3 = 3xyz$."
            },
            {
                "id": 23,
                "q": "Expand: $(3x + 2y)^3$.",
                "options": [
                    "27x³ + 54x²y + 36xy² + 8y³",
                    "27x³ + 18x²y + 12xy² + 8y³",
                    "27x³ + 8y³",
                    "9x³ + 54x²y + 36xy² + 6y³"
                ],
                "ans": 0,
                "solution": "$(3x)^3 + 3(3x)^2(2y) + 3(3x)(2y)^2 + (2y)^3 = 27x^3 + 54x^2y + 36xy^2 + 8y^3$."
            },
            {
                "id": 24,
                "q": "Factorise: $27x^3 - 64y^3$.",
                "options": [
                    "(3x - 4y)(9x² + 12xy + 16y²)",
                    "(3x - 4y)(9x² - 12xy + 16y²)",
                    "(3x + 4y)(9x² - 12xy + 16y²)",
                    "(3x - 4y)³"
                ],
                "ans": 0,
                "solution": "$(3x)^3 - (4y)^3 = (3x - 4y)[(3x)^2 + (3x)(4y) + (4y)^2] = (3x - 4y)(9x^2 + 12xy + 16y^2)$."
            },
            {
                "id": 25,
                "q": "Without calculating cubes, find $(-15)^3 + 8^3 + 7^3$.",
                "options": ["-2520", "2520", "-1260", "0"],
                "ans": 0,
                "solution": "Sum $= (-15) + 8 + 7 = 0$. By conditional identity, sum of cubes $= 3(-15)(8)(7) = -45 \\times 56 = -2520$."
            },
            {
                "id": 26,
                "q": "If $x + y = 12$ and $xy = 27$, find the value of $x^3 + y^3$.",
                "options": ["756", "864", "972", "1028"],
                "ans": 0,
                "solution": "$x^3 + y^3 = (x + y)^3 - 3xy(x + y) = 12^3 - 3(27)(12) = 1728 - 972 = 756$."
            },
            {
                "id": 27,
                "q": "If $x - y = 4$ and $xy = 21$, find the value of $x^3 - y^3$.",
                "options": ["316", "284", "336", "364"],
                "ans": 0,
                "solution": "$x^3 - y^3 = (x - y)^3 + 3xy(x - y) = 4^3 + 3(21)(4) = 64 + 252 = 316$."
            },
            {
                "id": 28,
                "q": "Factorise: $8a^3 + b^3 + 12a^2b + 6ab^2$.",
                "options": [
                    "(2a + b)³",
                    "(2a - b)³",
                    "(4a + b)³",
                    "(2a + b)(4a² + b²)"
                ],
                "ans": 0,
                "solution": "This matches $(x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3$ with $x = 2a, y = b$. Thus $(2a + b)^3$."
            },
            {
                "id": 29,
                "q": "Expand $(-2x + 5y - 3z)^2$.",
                "options": [
                    "4x² + 25y² + 9z² - 20xy - 30yz + 12zx",
                    "4x² + 25y² + 9z² + 20xy - 30yz - 12zx",
                    "4x² - 25y² - 9z² - 20xy - 30yz + 12zx",
                    "4x² + 25y² + 9z² - 10xy - 15yz + 6zx"
                ],
                "ans": 0,
                "solution": "Squares: $4x^2 + 25y^2 + 9z^2$. Pairwise: $2(-2x)(5y) = -20xy$, $2(5y)(-3z) = -30yz$, $2(-2x)(-3z) = 12zx$."
            },
            {
                "id": 30,
                "q": "If $a^2 + b^2 + c^2 = 250$ and $ab + bc + ca = 3$, find $a + b + c$.",
                "options": ["±16", "±15", "±14", "±12"],
                "ans": 0,
                "solution": "$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) = 250 + 2(3) = 256$. Thus $a + b + c = \\pm \\sqrt{256} = \\pm 16$."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Quiz 4: Rational Expressions & Computational Modeling",
        "badge": "Quiz Challenge 4 • 10 Questions",
        "questions": [
            {
                "id": 31,
                "q": "What is the simplified form of $\\frac{x^2 - 49}{x + 7}$ for $x \\ne -7$?",
                "options": ["x - 7", "x + 7", "x - 49", "1"],
                "ans": 0,
                "solution": "$\\frac{x^2 - 49}{x + 7} = \\frac{(x - 7)(x + 7)}{x + 7} = x - 7$."
            },
            {
                "id": 32,
                "q": "What are the domain restrictions for $\\frac{2x - 3}{x^2 - 2x - 15}$?",
                "options": [
                    "x ≠ 5 and x ≠ -3",
                    "x ≠ -5 and x ≠ 3",
                    "x ≠ 3/2",
                    "x ≠ 15"
                ],
                "ans": 0,
                "solution": "Denominator $x^2 - 2x - 15 = (x - 5)(x + 3) = 0 \\implies x = 5, x = -3$. Excluded: $x \\ne 5, -3$."
            },
            {
                "id": 33,
                "q": "Simplify: $\\frac{x^2 + 6x + 9}{x^2 - 9}$.",
                "options": [
                    "\\frac{x + 3}{x - 3}",
                    "\\frac{x - 3}{x + 3}",
                    "1",
                    "\\frac{x + 3}{x + 3}"
                ],
                "ans": 0,
                "solution": "$\\frac{(x + 3)^2}{(x - 3)(x + 3)} = \\frac{x + 3}{x - 3}$ (for $x \\ne \\pm 3$)."
            },
            {
                "id": 34,
                "q": "Simplify: $\\frac{x^3 - 1}{x^2 - 1}$.",
                "options": [
                    "\\frac{x² + x + 1}{x + 1}",
                    "\\frac{x² - x + 1}{x + 1}",
                    "\\frac{x - 1}{x + 1}",
                    "x + 1"
                ],
                "ans": 0,
                "solution": "$\\frac{(x - 1)(x^2 + x + 1)}{(x - 1)(x + 1)} = \\frac{x^2 + x + 1}{x + 1}$ (for $x \\ne \\pm 1$)."
            },
            {
                "id": 35,
                "q": "Using Sophie Germain's identity, what are the factors of $a^4 + 4b^4$?",
                "options": [
                    "(a² - 2ab + 2b²)(a² + 2ab + 2b²)",
                    "(a² - 2b²)²",
                    "(a² + 2b²)²",
                    "(a - 2b)⁴"
                ],
                "ans": 0,
                "solution": "$a^4 + 4b^4 = (a^2 + 2b^2)^2 - 4a^2b^2 = (a^2 + 2b^2 - 2ab)(a^2 + 2b^2 + 2ab)$."
            },
            {
                "id": 36,
                "q": "What is the product $\\frac{x - 3}{x + 2} \\times \\frac{x^2 - 4}{x^2 - 9}$ in lowest terms?",
                "options": [
                    "\\frac{x - 2}{x + 3}",
                    "\\frac{x + 2}{x - 3}",
                    "1",
                    "\\frac{x - 2}{x - 3}"
                ],
                "ans": 0,
                "solution": "$\\frac{x - 3}{x + 2} \\times \\frac{(x - 2)(x + 2)}{(x - 3)(x + 3)} = \\frac{x - 2}{x + 3}$."
            },
            {
                "id": 37,
                "q": "What is the role of an Abstract Syntax Tree (AST) in Computer Algebra Systems?",
                "options": [
                    "It breaks down equations into operator nodes and operands so pattern-matching rules can be applied recursively",
                    "It converts numbers into binary decimals",
                    "It displays graphs on computer screens",
                    "It prevents syntax errors in HTML"
                ],
                "ans": 0,
                "solution": "An AST encodes expressions structurally, allowing computer algorithms to traverse subtrees, match identity patterns, and simplify expressions recursively."
            },
            {
                "q": "Simplify: $\\frac{4x^2 - 9}{2x^2 + 3x}$.",
                "id": 38,
                "options": [
                    "\\frac{2x - 3}{x}",
                    "\\frac{2x + 3}{x}",
                    "2x - 3",
                    "\\frac{4x - 9}{2x + 3}"
                ],
                "ans": 0,
                "solution": "Factor numerator: $(2x - 3)(2x + 3)$. Factor denominator: $x(2x + 3)$. Cancel $(2x + 3)$: $\\frac{2x - 3}{x}$."
            },
            {
                "id": 39,
                "q": "If $x = 2$, is the expression $\\frac{x^2 - 4}{x - 2}$ defined?",
                "options": [
                    "No, because substituting x = 2 gives 0/0 which is mathematically undefined",
                    "Yes, it equals 4",
                    "Yes, it equals 0",
                    "Yes, it equals 2"
                ],
                "ans": 0,
                "solution": "Although the simplified form is $(x + 2) = 4$ for $x \\ne 2$, at $x = 2$ the original expression has denominator $2 - 2 = 0$, which is undefined."
            },
            {
                "id": 40,
                "q": "In algorithmic factoring, which pillar of computational thinking is applied when breaking $(a + b + c)^2$ into 9 sub-region terms?",
                "options": [
                    "Decomposition",
                    "Algorithm Design",
                    "Pattern Generalization",
                    "Recursion"
                ],
                "ans": 0,
                "solution": "Decomposition is the process of breaking a complex problem or algebraic expression down into smaller, manageable sub-components."
            }
        ]
    }
]

print("Loaded class9_algebraic_identities_data: 16 content slides, 4 quiz slides, 40 quiz questions.")

# -*- coding: utf-8 -*-
"""
Bespoke SVG/HTML interactive simulators for NCERT Class 6 Mathematics Chapter 1: Patterns in Mathematics.
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""

SIMULATORS = {
    # Simulator 1: Interactive Pattern Detector & Nature's Gallery
    1: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Nature's Pattern Detector</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Art & Science</span>
        </div>

        <!-- SVG Pattern Display -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim1_svg" viewBox="0 0 400 200" class="w-full h-auto max-h-[220px]">
                <!-- Sunflower Spiral View (Default) -->
                <g id="sim1_sunflower">
                    <circle cx="200" cy="100" r="85" fill="#451a03" stroke="#d97706" stroke-width="2"/>
                    <!-- Sunflower Spiral Dots generated dynamically in JS -->
                    <g id="sim1_seeds"></g>
                    <!-- Petals Ring -->
                    <g id="sim1_petals"></g>
                    <text x="200" y="195" text-anchor="middle" fill="#fde047" font-size="9" font-weight="bold">Sunflower Seed Spirals (Golden Angle ~137.5°)</text>
                </g>

                <!-- Honeycomb View (Hidden initially) -->
                <g id="sim1_honeycomb" class="hidden">
                    <g id="sim1_hex_grid"></g>
                    <text x="200" y="195" text-anchor="middle" fill="#facc15" font-size="9" font-weight="bold">Hexagonal Tessellation (Zero Gaps, Max Honey Storage)</text>
                </g>

                <!-- Wave Rhythm View (Hidden initially) -->
                <g id="sim1_waves" class="hidden">
                    <path d="M 20 100 Q 65 30 110 100 T 200 100 T 290 100 T 380 100" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <path d="M 20 100 Q 65 170 110 100 T 200 100 T 290 100 T 380 100" fill="none" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="200" y="195" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Harmonic Rhythm Waves (Musical Pitch & Planetary Cycles)</text>
                </g>
            </svg>
        </div>

        <!-- Pattern Feature Card -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Active Pattern:</span>
                <span id="sim1_type_name" class="text-amber-300 font-bold">Sunflower Spiral Packings</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Mathematical Secret:</span>
                <span id="sim1_math_secret" class="text-emerald-400 font-bold">Virahānka / Fibonacci Numbers (21 & 34)</span>
            </div>
        </div>

        <!-- Pattern Mode Toggles -->
        <div class="grid grid-cols-3 gap-2 pt-1">
            <button onclick="sim1SetMode('sunflower')" id="sim1_btn_sun" class="py-1.5 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow">
                🌻 Sunflower
            </button>
            <button onclick="sim1SetMode('honeycomb')" id="sim1_btn_hex" class="py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                🐝 Honeycomb
            </button>
            <button onclick="sim1SetMode('waves')" id="sim1_btn_wav" class="py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                🎵 Wave Rhythm
            </button>
        </div>
    </div>
    """,

    # Simulator 2: Whole Number Stepper & Sequence Engine
    2: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Number Sequence Generator</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Rule-Based Patterns</span>
        </div>

        <!-- Sequence Output Display -->
        <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[140px] space-y-3">
            <div id="sim2_term_container" class="flex flex-wrap items-center justify-center gap-2">
                <!-- Injected in JS -->
            </div>
            <div class="text-[11px] text-slate-400 font-mono flex items-center gap-2">
                <span>Rule: <strong id="sim2_rule_desc" class="text-amber-300">Start at 2, Add 3 each step</strong></span>
            </div>
        </div>

        <!-- Step Rule Configuration Controls -->
        <div class="grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block text-[10px] mb-1">Starting Number:</label>
                <input type="number" id="sim2_start" value="2" min="0" max="50" onchange="sim2Generate()"
                       class="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-cyan-300 font-mono text-center">
            </div>
            <div>
                <label class="text-slate-400 block text-[10px] mb-1">Operation / Step:</label>
                <select id="sim2_step" onchange="sim2Generate()"
                        class="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-amber-300 font-mono text-xs">
                    <option value="add_1">Add 1 (+1: Counting)</option>
                    <option value="add_2">Add 2 (+2: Evens/Odds)</option>
                    <option value="add_3" selected>Add 3 (+3: Multiples)</option>
                    <option value="add_5">Add 5 (+5: Fives)</option>
                    <option value="mul_2">Multiply by 2 (×2: Doubling)</option>
                    <option value="mul_3">Multiply by 3 (×3: Tripling)</option>
                </select>
            </div>
        </div>

        <!-- Term Count Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Number of Terms to Generate:</span>
                <span id="sim2_count_val" class="font-mono text-cyan-300">7 Terms</span>
            </div>
            <input type="range" id="sim2_count_slider" min="4" max="10" value="7" step="1" oninput="sim2Generate()"
                   class="w-full accent-cyan-500 cursor-pointer">
        </div>
    </div>
    """,

    # Simulator 3: Even-Odd Sieve & Number Line Hopper
    3: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider">Even vs Odd Number Sieve</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Pairing Dots</span>
        </div>

        <!-- Visual Paired Dots Display -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[170px] space-y-3">
            <div class="flex items-center gap-3">
                <span class="text-xs text-slate-400">Inspecting Number:</span>
                <span id="sim3_num_label" class="text-2xl font-black text-amber-400 font-mono">7</span>
                <span id="sim3_parity_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">ODD NUMBER</span>
            </div>

            <!-- Dots Pairing Grid -->
            <div id="sim3_dots_container" class="flex flex-wrap items-center justify-center gap-2 max-w-[280px]">
                <!-- Injected in JS -->
            </div>

            <p id="sim3_pairing_text" class="text-xs text-slate-300 text-center">
                7 dots = 3 complete pairs + <strong class="text-amber-400">1 lone leftover dot!</strong>
            </p>
        </div>

        <!-- Number Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Select Number to Inspect:</span>
                <span id="sim3_slider_val" class="font-mono text-cyan-300">7</span>
            </div>
            <input type="range" id="sim3_slider" min="1" max="16" value="7" step="1" oninput="sim3SetNumber(this.value)"
                   class="w-full accent-emerald-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>1</span>
                <span>4</span>
                <span>8</span>
                <span>12</span>
                <span>16</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Triangular Number Pyramid Builder
    4: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Triangular Number Builder</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Tₙ = n(n+1)/2</span>
        </div>

        <!-- SVG Triangular Dot Pyramid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim4_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim4_dots_group" transform="translate(175, 25)"></g>
            </svg>
        </div>

        <!-- Formula and Calculation Box -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Triangular Term:</span>
                <span id="sim4_term_label" class="text-amber-300 font-mono font-bold text-base">T₄ = 10 Dots</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Row Addition:</span>
                <span id="sim4_sum_formula" class="text-cyan-300 font-mono font-bold">1 + 2 + 3 + 4 = 10</span>
            </div>
        </div>

        <!-- Slider for Rows -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Number of Triangular Rows (n):</span>
                <span id="sim4_slider_val" class="font-mono text-cyan-300">4 Rows</span>
            </div>
            <input type="range" id="sim4_slider" min="1" max="8" value="4" step="1" oninput="sim4SetRows(this.value)"
                   class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>1 (T₁)</span>
                <span>3 (T₃)</span>
                <span>5 (T₅)</span>
                <span>8 (T₈=36)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Square Grid Multiplier & Array Animator
    5: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Square Numbers (n × n Array)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">n² Perfect Squares</span>
        </div>

        <!-- SVG Square Grid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim5_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim5_grid_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Square Value Readout -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Square Dimension:</span>
                <span id="sim5_dim_label" class="text-amber-300 font-mono font-bold text-sm">5 × 5 Grid</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Total Dot Count (n²):</span>
                <span id="sim5_val_label" class="text-cyan-300 font-mono font-bold text-sm">25 Dots (5²)</span>
            </div>
        </div>

        <!-- Dimension Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Side Length (n):</span>
                <span id="sim5_slider_val" class="font-mono text-cyan-300">5</span>
            </div>
            <input type="range" id="sim5_slider" min="1" max="8" value="5" step="1" oninput="sim5SetSide(this.value)"
                   class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>1²=1</span>
                <span>3²=9</span>
                <span>5²=25</span>
                <span>8²=64</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 6: 3D Isometric Cube Stacker
    6: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider">3D Cube Numbers (n × n × n)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">n³ Blocks</span>
        </div>

        <!-- SVG 3D Isometric Cube -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim6_svg" viewBox="0 0 350 210" class="w-full h-auto max-h-[210px]">
                <g id="sim6_isometric_group" transform="translate(175, 120)"></g>
            </svg>
        </div>

        <!-- Cube Specs -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Cube Dimensions:</span>
                <span id="sim6_dim_label" class="text-amber-300 font-mono font-bold text-sm">3 × 3 × 3</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Total Unit Blocks (n³):</span>
                <span id="sim6_val_label" class="text-indigo-300 font-mono font-bold text-sm">27 Blocks (3³)</span>
            </div>
        </div>

        <!-- Cube Edge Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Cube Edge Length (n):</span>
                <span id="sim6_slider_val" class="font-mono text-cyan-300">n = 3</span>
            </div>
            <input type="range" id="sim6_slider" min="1" max="4" value="3" step="1" oninput="sim6SetCube(this.value)"
                   class="w-full accent-indigo-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>1³ = 1</span>
                <span>2³ = 8</span>
                <span>3³ = 27</span>
                <span>4³ = 64</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Virahānka Poetic Meter & Spiral Generator
    7: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Virahānka Numbers (Fibonacci)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Vₙ = Vₙ₋₁ + Vₙ₋₂</span>
        </div>

        <!-- SVG Golden Spiral Visualizer -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[200px]">
            <svg id="sim7_svg" viewBox="0 0 350 180" class="w-full h-auto max-h-[180px]">
                <g id="sim7_tiles_group" transform="translate(175, 90) scale(1.6)"></g>
            </svg>
        </div>

        <!-- Sequence Step-by-Step Display -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1.5 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-400">Sequence Term:</span>
                <span id="sim7_term_label" class="text-amber-300 font-mono font-bold text-sm">V₇ = 13</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="text-slate-400">Sum of Preceding Two:</span>
                <span id="sim7_calc_label" class="font-mono text-cyan-300 font-bold">5 + 8 = 13</span>
            </div>
        </div>

        <!-- Step Forward / Reset Button -->
        <div class="flex items-center justify-between gap-3 pt-1">
            <button onclick="sim7Step()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-bold text-xs shadow transition">
                ➕ Next Virahānka Term
            </button>
            <button onclick="sim7Reset()" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition">
                Reset to 1, 1
            </button>
        </div>
    </div>
    """,

    # Simulator 8: Doubling & Tripling Exponential Tree
    8: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Powers of 2 and 3 Branching Tree</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Exponential Split</span>
        </div>

        <!-- SVG Branching Tree -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim8_svg" viewBox="0 0 380 200" class="w-full h-auto max-h-[200px]">
                <g id="sim8_tree_group"></g>
            </svg>
        </div>

        <!-- Growth Readout -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Exponent Level:</span>
                <span id="sim8_level_label" class="text-amber-300 font-mono font-bold text-sm">Step n = 4</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Leaf Node Count:</span>
                <span id="sim8_total_label" class="text-cyan-300 font-mono font-bold text-sm">2⁴ = 16 Nodes</span>
            </div>
        </div>

        <!-- Mode Toggle & Level Slider -->
        <div class="space-y-2">
            <div class="flex gap-2">
                <button onclick="sim8SetBase(2)" id="sim8_btn_2" class="flex-1 py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs transition">
                    ⚡ Powers of 2 (Doubling)
                </button>
                <button onclick="sim8SetBase(3)" id="sim8_btn_3" class="flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                    💥 Powers of 3 (Tripling)
                </button>
            </div>
            <div class="space-y-1">
                <input type="range" id="sim8_slider" min="0" max="5" value="4" step="1" oninput="sim8SetLevel(this.value)"
                       class="w-full accent-cyan-500 cursor-pointer">
            </div>
        </div>
    </div>
    """,

    # Simulator 9: The Chameleon Number 36 Morphing Lab
    9: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-yellow-400"></span>
                <h4 class="text-xs font-bold text-yellow-300 uppercase tracking-wider">The Chameleon Number 36 Morphing Lab</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Triangle ⇄ Square</span>
        </div>

        <!-- SVG 36 Dots Morphing Grid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim9_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim9_dots_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Current Configuration Info -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Geometric Role:</span>
                <span id="sim9_role_label" class="text-amber-300 font-bold text-sm">Triangular Number (T₈)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Mathematical Formula:</span>
                <span id="sim9_formula_label" class="text-cyan-300 font-mono font-bold text-sm">1+2+...+8 = 36</span>
            </div>
        </div>

        <!-- Morph Toggle Button -->
        <div class="flex items-center justify-center pt-1">
            <button onclick="sim9ToggleMorph()" id="sim9_morph_btn" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-amber-500 via-yellow-400 to-amber-500 text-slate-950 font-black text-xs shadow-lg transition">
                🔄 Morph 36: Triangle (T₈) ➔ Square (6 × 6)
            </button>
        </div>
    </div>
    """,

    # Simulator 10: Honeycomb Centered Hexagon Expander
    10: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Centered Hexagonal Numbers (Honeycomb)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">1, 7, 19, 37, 61...</span>
        </div>

        <!-- SVG Concentric Hexagon Rings -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim10_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim10_hex_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Hexagon Specs -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Concentric Ring Level:</span>
                <span id="sim10_ring_label" class="text-amber-300 font-mono font-bold text-sm">Ring 2 (+12 dots)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Total Dot Count:</span>
                <span id="sim10_total_label" class="text-cyan-300 font-mono font-bold text-sm">19 Dots (H₃)</span>
            </div>
        </div>

        <!-- Ring Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Add Concentric Hexagonal Rings:</span>
                <span id="sim10_slider_val" class="font-mono text-cyan-300">Level 2</span>
            </div>
            <input type="range" id="sim10_slider" min="0" max="4" value="2" step="1" oninput="sim10SetRing(this.value)"
                   class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>0 (1 dot)</span>
                <span>1 (7 dots)</span>
                <span>2 (19 dots)</span>
                <span>3 (37 dots)</span>
                <span>4 (61 dots)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 11: L-Shaped Gnomon Square Prover
    11: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">L-Shaped Gnomon: Odds Sum to Squares</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">1 + 3 + ... = n²</span>
        </div>

        <!-- SVG Gnomon Grid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim11_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim11_gnomon_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Odd Sum Readout -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1.5 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-400">Sum of First n Odd Numbers:</span>
                <span id="sim11_sum_eq" class="text-amber-300 font-mono font-bold text-sm">1 + 3 + 5 + 7 = 16</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="text-slate-400">Square Identity:</span>
                <span id="sim11_square_eq" class="font-mono text-emerald-400 font-bold">4 × 4 = 4² = 16 Dots</span>
            </div>
        </div>

        <!-- Gnomon Layers Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Add L-Shaped Odd Layers (n):</span>
                <span id="sim11_slider_val" class="font-mono text-cyan-300">n = 4</span>
            </div>
            <input type="range" id="sim11_slider" min="1" max="6" value="4" step="1" oninput="sim11SetLayer(this.value)"
                   class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>1</span>
                <span>2 (4)</span>
                <span>3 (9)</span>
                <span>4 (16)</span>
                <span>5 (25)</span>
                <span>6 (36)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 12: Diagonal Slicer & Mountain Sum Visualizer
    12: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider">Mountain Sums & Diagonal Slices</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">1+2+3+2+1 = n²</span>
        </div>

        <!-- SVG Mountain / Diagonal Grid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim12_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim12_diag_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Mountain Equation Display -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1.5 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-400">Mountain Diagonal Addition:</span>
                <span id="sim12_sum_text" class="text-emerald-300 font-mono font-bold text-sm">1 + 2 + 3 + 4 + 3 + 2 + 1 = 16</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="text-slate-400">Peak Identity:</span>
                <span id="sim12_peak_text" class="font-mono text-cyan-300 font-bold">Peak = 4 ➔ 4² = 16</span>
            </div>
        </div>

        <!-- Mode Toggle & Peak Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Peak Value (n):</span>
                <span id="sim12_slider_val" class="font-mono text-cyan-300">Peak 4</span>
            </div>
            <input type="range" id="sim12_slider" min="2" max="6" value="4" step="1" oninput="sim12SetPeak(this.value)"
                   class="w-full accent-emerald-500 cursor-pointer">
        </div>
    </div>
    """,

    # Simulator 13: Regular Polygon Morphing Wheel
    13: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Regular Polygon Sequence (Table 3)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">3, 4, 5, 6, 7, 8 Sides</span>
        </div>

        <!-- SVG Regular Polygon -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim13_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim13_poly_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Polygon Data -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Polygon Name:</span>
                <span id="sim13_name_label" class="text-amber-300 font-bold text-sm">Regular Hexagon (6)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Interior Angle Sum:</span>
                <span id="sim13_angle_label" class="text-cyan-300 font-mono font-bold text-sm">(6−2) × 180° = 720°</span>
            </div>
        </div>

        <!-- Number of Sides Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Number of Sides / Corners (n):</span>
                <span id="sim13_slider_val" class="font-mono text-cyan-300">6 Sides</span>
            </div>
            <input type="range" id="sim13_slider" min="3" max="10" value="6" step="1" oninput="sim13SetSides(this.value)"
                   class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>3 (Triangle)</span>
                <span>4 (Square)</span>
                <span>6 (Hex)</span>
                <span>8 (Oct)</span>
                <span>10 (Decagon)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 14: Complete Graph (Kn) & Handshake Simulator
    14: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Complete Graphs (Kₙ) & Handshakes</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Edges = n(n-1)/2</span>
        </div>

        <!-- SVG Complete Graph Display -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim14_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim14_graph_group" transform="translate(175, 100)"></g>
            </svg>
        </div>

        <!-- Graph Metrics -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Vertices (Dots / People):</span>
                <span id="sim14_vert_label" class="text-amber-300 font-mono font-bold text-sm">n = 5 Points (K₅)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Total Edges / Handshakes:</span>
                <span id="sim14_edge_label" class="text-emerald-400 font-mono font-bold text-sm">10 Edges (T₄)</span>
            </div>
        </div>

        <!-- Vertex Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Select Vertex Count (n):</span>
                <span id="sim14_slider_val" class="font-mono text-cyan-300">5 Vertices</span>
            </div>
            <input type="range" id="sim14_slider" min="2" max="7" value="5" step="1" oninput="sim14SetVertices(this.value)"
                   class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>2 (1 edge)</span>
                <span>3 (3 edges)</span>
                <span>4 (6 edges)</span>
                <span>5 (10 edges)</span>
                <span>7 (21 edges)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 15: 3D Stacked Pyramids (Squares & Triangles)
    15: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider">3D Stacked Pyramids</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Layer Accumulation</span>
        </div>

        <!-- SVG 3D Isometric Stacked Pyramid -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim15_svg" viewBox="0 0 350 210" class="w-full h-auto max-h-[210px]">
                <g id="sim15_pyramid_group" transform="translate(175, 125)"></g>
            </svg>
        </div>

        <!-- Stacked Metrics -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-400">Stack Type:</span>
                <span id="sim15_type_label" class="text-amber-300 font-bold text-sm">Square Pyramid (1² + 2² + 3²)</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="text-slate-400">Total Unit Blocks:</span>
                <span id="sim15_total_label" class="font-mono text-cyan-300 font-bold text-sm">1 + 4 + 9 = 14 Blocks</span>
            </div>
        </div>

        <!-- Mode Toggle & Level Slider -->
        <div class="space-y-2">
            <div class="flex gap-2">
                <button onclick="sim15SetMode('square')" id="sim15_btn_sq" class="flex-1 py-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs transition">
                    🏛️ Stacked Squares
                </button>
                <button onclick="sim15SetMode('triangle')" id="sim15_btn_tri" class="flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                    ⛺ Stacked Triangles
                </button>
            </div>
            <div class="space-y-1">
                <input type="range" id="sim15_slider" min="1" max="4" value="3" step="1" oninput="sim15SetLevel(this.value)"
                       class="w-full accent-indigo-500 cursor-pointer">
            </div>
        </div>
    </div>
    """,

    # Simulator 16: Koch Snowflake Fractal Iteration Workbench
    16: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">The Koch Snowflake Fractal</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Powers of 4</span>
        </div>

        <!-- SVG Fractal Snowflake -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim16_svg" viewBox="0 0 350 200" class="w-full h-auto max-h-[200px]">
                <g id="sim16_fractal_group" transform="translate(175, 105)"></g>
            </svg>
        </div>

        <!-- Fractal Stats -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Fractal Iteration:</span>
                <span id="sim16_iter_label" class="text-amber-300 font-mono font-bold text-sm">Iteration 1</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Total Boundary Segments:</span>
                <span id="sim16_edges_label" class="text-cyan-300 font-mono font-bold text-sm">3 × 4¹ = 12 Edges</span>
            </div>
        </div>

        <!-- Iteration Step Buttons -->
        <div class="grid grid-cols-4 gap-2 pt-1">
            <button onclick="sim16SetIter(0)" id="sim16_btn_0" class="py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                Iter 0 (3)
            </button>
            <button onclick="sim16SetIter(1)" id="sim16_btn_1" class="py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs transition shadow">
                Iter 1 (12)
            </button>
            <button onclick="sim16SetIter(2)" id="sim16_btn_2" class="py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                Iter 2 (48)
            </button>
            <button onclick="sim16SetIter(3)" id="sim16_btn_3" class="py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                Iter 3 (192)
            </button>
        </div>
    </div>
    """
}

# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators for NCERT Class 6 Mathematics Chapter 7: Fractions
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, etc.).
All math rendered in clean Unicode (1/2, 3/4, 5/2, 1 1/2, ×, ÷, +, −, etc.).
"""

SIMULATORS = [
    # Sim 1: Roti Sharing Simulator
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🫓</span> Roti Sharing Laboratory
            </span>
            <span id="sim1_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">1/2 Roti Each</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 relative">
            <svg id="sim1_svg" viewBox="0 0 200 200" class="w-44 h-44 drop-shadow-md">
                <!-- Dynamic sectors injected via JS -->
            </svg>
            <div id="sim1_readout" class="mt-2 text-xs font-mono font-bold text-center text-cyan-300">
                1 roti ÷ 2 children = 1/2 share
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-2">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Number of Children (n):</span>
                <span id="sim1_n_val" class="font-bold font-mono text-amber-400">2</span>
            </div>
            <input type="range" id="sim1_n" min="1" max="12" value="2" oninput="updateSim1()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                <span>1 (Whole)</span>
                <span>2 (Half)</span>
                <span>4 (Quarter)</span>
                <span>8</span>
                <span>12</span>
            </div>
        </div>
    </div>
    """,

    # Sim 2: Comparing Unit Fractions
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>⚖️</span> Unit Fraction Comparator
            </span>
            <span id="sim2_result" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">1/3 > 1/6</span>
        </div>

        <div class="flex-1 flex flex-col justify-center space-y-3 py-2">
            <!-- Strip A -->
            <div class="space-y-1">
                <div class="flex justify-between text-xs">
                    <span class="text-amber-300 font-mono font-bold">Fraction A: 1/<span id="sim2_a_label">3</span></span>
                    <span id="sim2_a_pct" class="text-slate-400 font-mono text-[11px]">33.3% of whole</span>
                </div>
                <div class="w-full h-7 bg-slate-800 rounded-lg border border-slate-700 overflow-hidden flex" id="sim2_strip_a"></div>
            </div>

            <!-- Strip B -->
            <div class="space-y-1">
                <div class="flex justify-between text-xs">
                    <span class="text-cyan-300 font-mono font-bold">Fraction B: 1/<span id="sim2_b_label">6</span></span>
                    <span id="sim2_b_pct" class="text-slate-400 font-mono text-[11px]">16.7% of whole</span>
                </div>
                <div class="w-full h-7 bg-slate-800 rounded-lg border border-slate-700 overflow-hidden flex" id="sim2_strip_b"></div>
            </div>

            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-center text-xs text-slate-300">
                Rule: Larger denominator = smaller share size!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Denominator A:</label>
                <input type="range" id="sim2_a" min="2" max="12" value="3" oninput="updateSim2()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Denominator B:</label>
                <input type="range" id="sim2_b" min="2" max="12" value="6" oninput="updateSim2()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
        </div>
    </div>
    """,

    # Sim 3: Parts of a Whole (Chikki Bar)
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🍫</span> Interactive Chikki Bar
            </span>
            <span class="text-[11px] font-mono text-slate-400">Click pieces to toggle</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 space-y-3">
            <div id="sim3_grid" class="grid gap-1.5 p-2 bg-slate-950 rounded-xl border border-slate-800 shadow-inner">
                <!-- Clickable chikki pieces -->
            </div>

            <div class="p-2.5 rounded-xl bg-slate-800/90 border border-slate-700 w-full text-center text-xs font-mono space-y-1">
                <div class="text-amber-300 font-bold">
                    Selected Portion: <span id="sim3_frac">3/8</span> (<span id="sim3_count">3</span> of <span id="sim3_total">8</span> units)
                </div>
                <div class="text-slate-400 text-[11px]">
                    Remaining Uneaten: <span id="sim3_rem" class="text-cyan-300">5/8</span>
                </div>
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-300">Grid Partition:</span>
            <div class="flex gap-1.5">
                <button onclick="setSim3Size(4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-mono border border-slate-700">4 (1×4)</button>
                <button onclick="setSim3Size(6)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-mono border border-slate-700">6 (2×3)</button>
                <button onclick="setSim3Size(8)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-mono border border-slate-700">8 (2×4)</button>
                <button onclick="setSim3Size(12)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-mono border border-slate-700">12 (3×4)</button>
            </div>
        </div>
    </div>
    """,

    # Sim 4: Different Shapes, Same Share
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Shape Invariance Lab (1/4 Share)
            </span>
            <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Area = 25%</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 relative">
            <svg id="sim4_svg" viewBox="0 0 200 200" class="w-44 h-44 drop-shadow-md">
                <!-- Injected via JS based on mode -->
            </svg>
            <div id="sim4_desc" class="mt-2 text-xs text-center font-mono text-slate-300">
                Mode: 4 Vertical Columns (Stripes)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-3 gap-1.5 text-xs">
            <button onclick="setSim4Mode('stripes')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold border border-slate-700 text-[11px]">
                Columns
            </button>
            <button onclick="setSim4Mode('grid')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold border border-slate-700 text-[11px]">
                Corner 2×2
            </button>
            <button onclick="setSim4Mode('diagonals')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-300 font-bold border border-slate-700 text-[11px]">
                Triangles
            </button>
        </div>
    </div>
    """,

    # Sim 5: Paper Strip Folding
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📄</span> Paper Strip Folding Simulator
            </span>
            <span id="sim5_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">4 Equal Quarters</span>
        </div>

        <div class="flex-1 flex flex-col justify-center space-y-3 py-2">
            <div class="relative w-full h-14 bg-amber-100 rounded-xl border-2 border-amber-300 shadow-md flex overflow-hidden" id="sim5_paper">
                <!-- Folding segments and creases injected via JS -->
            </div>
            <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-300" id="sim5_text">
                2 folds in half = 2 × 2 = 4 sections (Unit: 1/4)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex flex-wrap gap-1.5 text-xs">
            <button onclick="setSim5Folds(1)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">1 Fold (1/2)</button>
            <button onclick="setSim5Folds(2)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">2 Folds (1/4)</button>
            <button onclick="setSim5Folds(3)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">3 Folds (1/8)</button>
            <button onclick="setSim5Folds(6)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 font-mono text-[11px] border border-slate-700">Thirds (1/6)</button>
        </div>
    </div>
    """,

    # Sim 6: Numerator & Denominator Dissector
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔢</span> Numerator vs Denominator
            </span>
            <span class="text-[11px] font-mono text-cyan-300">Count vs Unit Type</span>
        </div>

        <div class="flex-1 flex flex-col justify-center items-center py-2 space-y-2">
            <div class="flex items-center gap-4">
                <div class="text-center font-mono">
                    <div id="sim6_num_disp" class="text-2xl font-black text-cyan-300">5</div>
                    <div class="w-12 h-0.5 bg-slate-500 my-1"></div>
                    <div id="sim6_den_disp" class="text-2xl font-black text-amber-400">3</div>
                </div>
                <div class="text-xs text-slate-300 space-y-1 font-mono">
                    <div>= <span id="sim6_count_word" class="text-cyan-300 font-bold">5</span> times the unit <span id="sim6_unit_word" class="text-amber-400 font-bold">1/3</span></div>
                    <div id="sim6_sum_expr" class="text-[11px] text-slate-400">1/3 + 1/3 + 1/3 + 1/3 + 1/3</div>
                </div>
            </div>

            <!-- Dynamic visual blocks -->
            <div id="sim6_blocks" class="flex flex-wrap gap-1 justify-center max-w-xs mt-2"></div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Numerator (Count): <span id="sim6_num_val" class="text-cyan-300 font-mono font-bold">5</span></label>
                <input type="range" id="sim6_num" min="1" max="10" value="5" oninput="updateSim6()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Denominator (Type): <span id="sim6_den_val" class="text-amber-400 font-mono font-bold">3</span></label>
                <input type="range" id="sim6_den" min="2" max="8" value="3" oninput="updateSim6()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 7: Fractions on Number Line
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📍</span> Number Line Plotter
            </span>
            <span id="sim7_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Point = 3/4</span>
        </div>

        <div class="flex-1 flex flex-col justify-center py-2 space-y-2">
            <svg id="sim7_svg" viewBox="0 0 320 80" class="w-full h-24">
                <!-- Axis, ticks, labels and pointer injected via JS -->
            </svg>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-center font-mono text-xs text-slate-300" id="sim7_desc">
                Interval 0 to 1 split into 4 equal segments. Step 3 times → 3/4.
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Denominator: <span id="sim7_den_val" class="text-amber-300 font-bold font-mono">4</span></label>
                <input type="range" id="sim7_den" min="2" max="8" value="4" oninput="updateSim7()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Numerator: <span id="sim7_num_val" class="text-cyan-300 font-bold font-mono">3</span></label>
                <input type="range" id="sim7_num" min="0" max="8" value="3" oninput="updateSim7()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
        </div>
    </div>
    """,

    # Sim 8: Density of Fractions (Microscope)
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔬</span> Infinite Density Microscope
            </span>
            <span id="sim8_level" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Zoom: 1/16</span>
        </div>

        <div class="flex-1 flex flex-col justify-center space-y-2 py-2">
            <svg id="sim8_svg" viewBox="0 0 320 80" class="w-full h-24">
                <!-- Dynamic nested midpoints -->
            </svg>
            <div id="sim8_text" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-center font-mono text-xs text-slate-300">
                Found midpoints: 1/2 → 1/4 → 1/8 → 1/16
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="zoomSim8()" class="flex-1 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 font-bold border border-amber-500/30 transition">
                + Bisect & Zoom In
            </button>
            <button onclick="resetSim8()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border border-slate-700 transition">
                Reset
            </button>
        </div>
    </div>
    """,

    # Sim 9: Proper vs Improper Sorter
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🍰</span> Proper vs Improper Visualizer
            </span>
            <span id="sim9_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Proper Fraction (&lt;1)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 space-y-2">
            <div id="sim9_pies" class="flex items-center justify-center gap-2 flex-wrap max-w-xs">
                <!-- Injected SVGs of pies -->
            </div>
            <div id="sim9_status" class="p-2 rounded-xl bg-slate-800/90 border border-slate-700 font-mono text-xs text-center text-slate-200 w-full">
                Value = 3/4 = 0.75 (&lt; 1 Whole)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Numerator: <span id="sim9_num_val" class="text-cyan-300 font-bold font-mono">3</span></label>
                <input type="range" id="sim9_num" min="1" max="10" value="3" oninput="updateSim9()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Denominator: <span id="sim9_den_val" class="text-amber-400 font-bold font-mono">4</span></label>
                <input type="range" id="sim9_den" min="2" max="6" value="4" oninput="updateSim9()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 10: Mixed Numbers Converter
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔄</span> Mixed Number Converter
            </span>
            <span class="text-[11px] font-mono text-slate-400">Improper ↔ Mixed</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 space-y-3">
            <div class="flex items-center gap-4 text-center font-mono">
                <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 shadow">
                    <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Improper</span>
                    <span id="sim10_improper" class="text-lg font-black text-rose-300">7/3</span>
                </div>
                <span class="text-amber-400 font-bold text-xl">⇄</span>
                <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 shadow">
                    <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Mixed Number</span>
                    <span id="sim10_mixed" class="text-lg font-black text-emerald-300">2 1/3</span>
                </div>
            </div>

            <div id="sim10_division" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-300 w-full">
                Division: 7 ÷ 3 = 2 with remainder 1 → 2 wholes + 1/3
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Numerator: <span id="sim10_num_val" class="text-rose-300 font-bold font-mono">7</span></label>
                <input type="range" id="sim10_num" min="3" max="15" value="7" oninput="updateSim10()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-rose-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Denominator: <span id="sim10_den_val" class="text-amber-400 font-bold font-mono">3</span></label>
                <input type="range" id="sim10_den" min="2" max="6" value="3" oninput="updateSim10()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 11: The Fraction Wall
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🧱</span> Interactive Fraction Wall (1 to 1/10)
            </span>
            <span class="text-[11px] font-mono text-cyan-300">Drag to align</span>
        </div>

        <div class="flex-1 flex flex-col justify-center py-1 relative">
            <div id="sim11_wall" class="space-y-1 w-full relative">
                <!-- 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/8, 1/10 strips -->
            </div>
            <!-- Vertical guide laser line -->
            <div id="sim11_laser" class="absolute top-0 bottom-0 w-0.5 bg-rose-500 pointer-events-none transition-all shadow-[0_0_8px_rgba(244,63,94,0.8)]" style="left: 50%;"></div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1.5 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Align with:</span>
                <div class="flex gap-1">
                    <button onclick="setSim11Laser(0.5, '1/2')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-amber-300 border border-slate-700">1/2</button>
                    <button onclick="setSim11Laser(0.25, '1/4')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-cyan-300 border border-slate-700">1/4</button>
                    <button onclick="setSim11Laser(0.333, '1/3')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-emerald-300 border border-slate-700">1/3</button>
                    <button onclick="setSim11Laser(0.75, '3/4')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-purple-300 border border-slate-700">3/4</button>
                </div>
            </div>
            <div id="sim11_readout" class="text-center font-mono text-[11px] text-amber-300">
                Aligning 1/2 = 2/4 = 3/6 = 4/8 = 5/10
            </div>
        </div>
    </div>
    """,

    # Sim 12: Equivalent Fractions
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>✨</span> Equivalent Fraction Multiplier
            </span>
            <span id="sim12_formula" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">2/3 = 4/6</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 space-y-3">
            <div class="w-full flex justify-center gap-4">
                <svg id="sim12_svg1" viewBox="0 0 100 100" class="w-24 h-24 drop-shadow"></svg>
                <div class="flex items-center text-amber-400 font-bold text-lg">=</div>
                <svg id="sim12_svg2" viewBox="0 0 100 100" class="w-24 h-24 drop-shadow"></svg>
            </div>

            <div id="sim12_math" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-300 w-full">
                Multiply top & bottom by 2: (2 × 2) / (3 × 2) = 4/6
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-2 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Multiplier factor (k):</span>
                <span id="sim12_k_val" class="font-bold font-mono text-cyan-300">2</span>
            </div>
            <input type="range" id="sim12_k" min="1" max="6" value="2" oninput="updateSim12()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        </div>
    </div>
    """,

    # Sim 13: Simplest Form
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>✂️</span> Simplest Form & HCF Reducer
            </span>
            <span id="sim13_hcf" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">HCF = 12</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 space-y-3">
            <div class="flex items-center gap-4 font-mono">
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-center">
                    <span class="text-[10px] text-slate-400 block">Initial</span>
                    <span id="sim13_init" class="text-lg font-black text-amber-300">24/36</span>
                </div>
                <span class="text-slate-500 font-bold text-lg">→</span>
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-center">
                    <span class="text-[10px] text-slate-400 block">Simplest Form</span>
                    <span id="sim13_final" class="text-lg font-black text-emerald-300">2/3</span>
                </div>
            </div>

            <div id="sim13_steps" class="p-2.5 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-slate-300 space-y-1 w-full text-center">
                Divide 24 and 36 by HCF (12) → 2/3 (Lowest terms!)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Numerator: <span id="sim13_num_val" class="text-amber-300 font-bold font-mono">24</span></label>
                <input type="range" id="sim13_num" min="2" max="48" value="24" oninput="updateSim13()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Denominator: <span id="sim13_den_val" class="text-cyan-300 font-bold font-mono">36</span></label>
                <input type="range" id="sim13_den" min="2" max="48" value="36" oninput="updateSim13()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
        </div>
    </div>
    """,

    # Sim 14: Comparing Fractions
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>⚖️</span> Cross-Multiplication Duel
            </span>
            <span id="sim14_winner" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">5/6 > 3/4</span>
        </div>

        <div class="flex-1 flex flex-col justify-center py-2 space-y-3">
            <div class="grid grid-cols-2 gap-3 font-mono text-center text-xs">
                <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
                    <span class="text-amber-300 font-bold block text-sm" id="sim14_f1_disp">3/4</span>
                    <span class="text-[10px] text-slate-400" id="sim14_f1_equiv">= 9/12</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
                    <span class="text-cyan-300 font-bold block text-sm" id="sim14_f2_disp">5/6</span>
                    <span class="text-[10px] text-slate-400" id="sim14_f2_equiv">= 10/12</span>
                </div>
            </div>

            <div id="sim14_cross" class="p-2.5 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-200">
                Cross-product: 3 × 6 = 18 &lt; 4 × 5 = 20 → 3/4 &lt; 5/6!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-2 text-xs">
            <div class="space-y-1">
                <span class="text-amber-300 font-bold">Fraction 1:</span>
                <div class="flex gap-1">
                    <input type="number" id="sim14_n1" value="3" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim14()">
                    <input type="number" id="sim14_d1" value="4" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim14()">
                </div>
            </div>
            <div class="space-y-1">
                <span class="text-cyan-300 font-bold">Fraction 2:</span>
                <div class="flex gap-1">
                    <input type="number" id="sim14_n2" value="5" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim14()">
                    <input type="number" id="sim14_d2" value="6" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim14()">
                </div>
            </div>
        </div>
    </div>
    """,

    # Sim 15: Adding Like Fractions
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>➕</span> Like Fractions Addition & Subtraction
            </span>
            <span id="sim15_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">2/5 + 1/5 = 3/5</span>
        </div>

        <div class="flex-1 flex flex-col justify-center space-y-3 py-2">
            <!-- Dynamic visual strip -->
            <div class="space-y-1">
                <div class="flex justify-between text-xs text-slate-400 font-mono">
                    <span>Common Denominator: <span id="sim15_den_lbl" class="text-amber-300">5</span></span>
                    <span id="sim15_op_lbl" class="text-cyan-300">2 units + 1 unit = 3 units</span>
                </div>
                <div id="sim15_strip" class="w-full h-8 bg-slate-800 rounded-xl border border-slate-700 overflow-hidden flex"></div>
            </div>

            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-center text-xs text-slate-200" id="sim15_math">
                (2 + 1) / 5 = 3/5
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-2 text-xs">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <button onclick="setSim15Op('add')" id="sim15_btn_add" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Addition (+)</button>
                    <button onclick="setSim15Op('sub')" id="sim15_btn_sub" class="px-2.5 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Subtraction (−)</button>
                </div>
                <span class="text-[10px] text-rose-400 font-bold">Never add denominators!</span>
            </div>
            <div class="grid grid-cols-3 gap-2">
                <div>
                    <label class="text-[10px] text-slate-400 block">Denom:</label>
                    <input type="number" id="sim15_d" value="5" min="2" max="10" class="w-full p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim15()">
                </div>
                <div>
                    <label class="text-[10px] text-slate-400 block">Num A:</label>
                    <input type="number" id="sim15_na" value="2" min="1" max="9" class="w-full p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim15()">
                </div>
                <div>
                    <label class="text-[10px] text-slate-400 block">Num B:</label>
                    <input type="number" id="sim15_nb" value="1" min="1" max="9" class="w-full p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim15()">
                </div>
            </div>
        </div>
    </div>
    """,

    # Sim 16: Brahmagupta's Universal Calculator
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📜</span> Brahmagupta's Algorithm (628 CE)
            </span>
            <button onclick="loadEgyptianPuzzle()" class="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                Egyptian Puzzle
            </button>
        </div>

        <div class="flex-1 flex flex-col justify-center py-2 space-y-2">
            <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-center font-mono">
                <div class="text-xs text-slate-400 mb-1">Universal Rule: a/b + c/d = (ad + bc) / bd</div>
                <div id="sim16_step1" class="text-xs text-amber-300 font-bold">1/3 + 1/4 = (1×4 + 1×3) / (3×4)</div>
                <div id="sim16_step2" class="text-xs text-cyan-300 font-bold mt-1">= (4 + 3) / 12 = 7/12</div>
            </div>

            <div id="sim16_egyptian" class="hidden p-2 rounded bg-amber-950/30 border border-amber-800/50 text-[11px] font-mono text-amber-200 text-center">
                Egyptian 1 Whole = 1/2 + 1/3 + 1/6 = (3 + 2 + 1) / 6 = 6/6 = 1!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-2 text-xs">
            <div>
                <label class="text-[10px] text-slate-400 block">Fraction 1 (a/b):</label>
                <div class="flex gap-1">
                    <input type="number" id="sim16_a" value="1" min="1" max="10" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim16()">
                    <input type="number" id="sim16_b" value="3" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim16()">
                </div>
            </div>
            <div>
                <label class="text-[10px] text-slate-400 block">Fraction 2 (c/d):</label>
                <div class="flex gap-1">
                    <input type="number" id="sim16_c" value="1" min="1" max="10" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim16()">
                    <input type="number" id="sim16_d" value="4" min="1" max="12" class="w-1/2 p-1 bg-slate-950 border border-slate-700 rounded text-center text-xs font-mono" onchange="updateSim16()">
                </div>
            </div>
        </div>
    </div>
    """
]

def verify_sims():
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for idx, s in enumerate(SIMULATORS):
        for word in forbidden:
            if word in s:
                raise ValueError(f"Found forbidden LaTeX token in Sim {idx+1}: {word}")
        for ch in s:
            if 0xD800 <= ord(ch) <= 0xDFFF:
                raise ValueError(f"Found surrogate in Sim {idx+1}: {ch}")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 16 Simulators!")

if __name__ == "__main__":
    verify_sims()
    with open(".agents/class6_math_fractions_sims.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch7_fractions_sims.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_fractions_sims.py")

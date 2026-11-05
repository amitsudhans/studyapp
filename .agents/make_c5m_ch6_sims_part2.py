# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: Simulators 9 to 16
"""

SIMULATORS_PART2 = {
    "sim_slide_9": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-cyan-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">2×2 Box Method Grid Builder</span>
                <span class="text-xs text-slate-400 font-mono" id="sim9_summary_top">69 × 45 = 3,105</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                <div class="flex items-center gap-2">
                    <span>Factor 1:</span>
                    <input type="number" id="sim9_n1" value="69" min="11" max="99" onchange="updateSim9()" class="w-16 px-2 py-1 bg-slate-800 border border-slate-600 rounded text-center font-mono font-bold text-indigo-300">
                </div>
                <div class="flex items-center gap-2">
                    <span>Factor 2:</span>
                    <input type="number" id="sim9_n2" value="45" min="11" max="99" onchange="updateSim9()" class="w-16 px-2 py-1 bg-slate-800 border border-slate-600 rounded text-center font-mono font-bold text-emerald-300">
                </div>
                <div class="flex gap-1.5">
                    <button onclick="setSim9Preset(69, 45)" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[11px] font-mono">69 × 45</button>
                    <button onclick="setSim9Preset(48, 35)" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[11px] font-mono">48 × 35</button>
                    <button onclick="setSim9Preset(53, 27)" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[11px] font-mono">53 × 27</button>
                </div>
            </div>
            <!-- Grid Container -->
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
                <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono max-w-sm mx-auto">
                    <div class="p-2 bg-slate-900 rounded font-bold text-slate-500 flex items-center justify-center">×</div>
                    <div class="p-2 bg-indigo-950/60 rounded font-bold text-indigo-300 border border-indigo-500/30" id="sim9_t1">60</div>
                    <div class="p-2 bg-indigo-950/60 rounded font-bold text-indigo-300 border border-indigo-500/30" id="sim9_o1">9</div>

                    <div class="p-2 bg-emerald-950/60 rounded font-bold text-emerald-300 border border-emerald-500/30 flex items-center justify-center" id="sim9_t2">40</div>
                    <div class="p-2.5 bg-slate-900/90 rounded border border-slate-700">
                        <span class="text-[10px] text-slate-400 block" id="sim9_c1_lbl">60 × 40</span>
                        <span class="text-amber-300 font-bold text-sm" id="sim9_c1">2,400</span>
                    </div>
                    <div class="p-2.5 bg-slate-900/90 rounded border border-slate-700">
                        <span class="text-[10px] text-slate-400 block" id="sim9_c2_lbl">9 × 40</span>
                        <span class="text-amber-300 font-bold text-sm" id="sim9_c2">360</span>
                    </div>

                    <div class="p-2 bg-emerald-950/60 rounded font-bold text-emerald-300 border border-emerald-500/30 flex items-center justify-center" id="sim9_o2">5</div>
                    <div class="p-2.5 bg-slate-900/90 rounded border border-slate-700">
                        <span class="text-[10px] text-slate-400 block" id="sim9_c3_lbl">60 × 5</span>
                        <span class="text-amber-300 font-bold text-sm" id="sim9_c3">300</span>
                    </div>
                    <div class="p-2.5 bg-slate-900/90 rounded border border-slate-700">
                        <span class="text-[10px] text-slate-400 block" id="sim9_c4_lbl">9 × 5</span>
                        <span class="text-amber-300 font-bold text-sm" id="sim9_c4">45</span>
                    </div>
                </div>
                <div class="flex flex-wrap items-center justify-center gap-2 text-xs font-mono pt-3 border-t border-slate-800 mt-3">
                    <span id="sim9_row1_sum">Row 1: 2,760</span>
                    <span class="text-slate-500">+</span>
                    <span id="sim9_row2_sum">Row 2: 345</span>
                    <span class="text-slate-500">=</span>
                    <span class="text-emerald-400 font-bold text-sm bg-emerald-950 px-3 py-0.5 rounded border border-emerald-500/40" id="sim9_grand_total">3,105</span>
                </div>
            </div>
        </div>
    """,

    "sim_slide_10": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-amber-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Cricket Scoreboard & Procurement Tally</span>
                <span class="text-xs text-slate-400 font-mono" id="sim10_summary_stat">136 Total Runs</span>
            </div>
            <div class="space-y-2.5 text-xs bg-slate-800/80 p-3.5 rounded-xl border border-slate-700">
                <div class="flex justify-between items-center">
                    <span>Fours (4 runs): <strong id="sim10_f_val" class="text-amber-400">14</strong> (14 × 4 = <span id="sim10_f_runs" class="text-emerald-400 font-bold">56</span>)</span>
                    <input type="range" id="sim10_f" min="0" max="25" value="14" oninput="updateSim10()" class="w-32 accent-amber-400">
                </div>
                <div class="flex justify-between items-center">
                    <span>Sixes (6 runs): <strong id="sim10_s_val" class="text-rose-400">8</strong> (8 × 6 = <span id="sim10_s_runs" class="text-emerald-400 font-bold">48</span>)</span>
                    <input type="range" id="sim10_s" min="0" max="15" value="8" oninput="updateSim10()" class="w-32 accent-rose-400">
                </div>
                <div class="flex justify-between items-center">
                    <span>Singles (1 run): <strong id="sim10_1_val" class="text-cyan-400">32</strong> (32 × 1 = <span id="sim10_1_runs" class="text-emerald-400 font-bold">32</span>)</span>
                    <input type="range" id="sim10_1" min="0" max="60" value="32" oninput="updateSim10()" class="w-32 accent-cyan-400">
                </div>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-center font-mono space-y-1">
                <div class="text-sm text-slate-300">Total Score Breakdown: <span id="sim10_eq" class="text-slate-400">56 + 48 + 32</span></div>
                <div class="text-lg font-bold text-amber-300" id="sim10_total">136 Runs Scored!</div>
            </div>
        </div>
    """,

    "sim_slide_11": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Standard Column Algorithm Stepper</span>
                <span class="text-xs text-slate-400 font-mono" id="sim11_step_tag">Step 0 of 3</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                <div class="flex gap-2">
                    <button onclick="setSim11Problem(453, 13)" id="sim11_p1" class="px-2.5 py-1 bg-indigo-600 rounded font-mono font-bold">453 × 13 (Gir Milk)</button>
                    <button onclick="setSim11Problem(324, 26)" id="sim11_p2" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">324 × 26</button>
                    <button onclick="setSim11Problem(574, 125)" id="sim11_p3" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">574 × 125 (Ghee)</button>
                </div>
                <button onclick="nextSim11Step()" id="sim11_step_btn" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 rounded font-bold text-xs flex items-center gap-1">
                    <span>Next Step ➔</span>
                </button>
            </div>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <div id="sim11_calc_box" class="font-mono text-sm space-y-1 w-64 text-right"></div>
                <div id="sim11_explanation" class="text-xs text-slate-300 text-center mt-3 font-mono">
                    Click 'Next Step' to advance through the place-value partial products!
                </div>
            </div>
        </div>
    """,

    "sim_slide_12": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-rose-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Bug Hunter: Find the Error</span>
                <span class="text-xs text-slate-400 font-mono">Error Diagnostics</span>
            </div>
            <div class="flex gap-2 justify-center">
                <button onclick="setSim12Bug(1)" id="sim12_b1" class="px-3 py-1 bg-rose-600 rounded text-xs font-bold">Bug 1: Missing Zero</button>
                <button onclick="setSim12Bug(2)" id="sim12_b2" class="px-3 py-1 bg-slate-700 rounded text-xs font-bold">Bug 2: Premature Carry</button>
                <button onclick="setSim12Bug(3)" id="sim12_b3" class="px-3 py-1 bg-slate-700 rounded text-xs font-bold">Bug 3: Column Shift</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <!-- Flawed Solution -->
                <div class="p-3 bg-slate-950 rounded-xl border border-rose-500/40 space-y-2">
                    <span class="text-rose-400 font-bold block flex items-center gap-1">
                        <span>❌</span> Student Submission with Error
                    </span>
                    <div id="sim12_wrong_box" class="font-mono text-xs space-y-1 bg-slate-900/80 p-2.5 rounded"></div>
                    <p id="sim12_flaw_desc" class="text-[11px] text-slate-300"></p>
                </div>
                <!-- Correct Solution -->
                <div class="p-3 bg-slate-950 rounded-xl border border-emerald-500/40 space-y-2">
                    <span class="text-emerald-400 font-bold block flex items-center gap-1">
                        <span>✓</span> Mathematician's Verified Fix
                    </span>
                    <div id="sim12_right_box" class="font-mono text-xs space-y-1 bg-slate-900/80 p-2.5 rounded"></div>
                    <p id="sim12_fix_desc" class="text-[11px] text-emerald-300 font-semibold"></p>
                </div>
            </div>
        </div>
    """,

    "sim_slide_13": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-teal-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Derivative Fact Family Tree</span>
                <span class="text-xs text-slate-400 font-mono">Anchor: 17 × 23 = 391</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center">
                <button onclick="setSim13Deriv('double_b')" id="sim13_btn_db" class="px-2.5 py-1 bg-teal-600 rounded text-xs font-mono font-bold">17 × 46 (Double)</button>
                <button onclick="setSim13Deriv('double_a')" id="sim13_btn_da" class="px-2.5 py-1 bg-slate-700 rounded text-xs font-mono font-bold">34 × 23 (Double)</button>
                <button onclick="setSim13Deriv('plus_1')" id="sim13_btn_p1" class="px-2.5 py-1 bg-slate-700 rounded text-xs font-mono font-bold">17 × 24 (+17)</button>
                <button onclick="setSim13Deriv('minus_1')" id="sim13_btn_m1" class="px-2.5 py-1 bg-slate-700 rounded text-xs font-mono font-bold">17 × 22 (-17)</button>
                <button onclick="setSim13Deriv('times_10')" id="sim13_btn_t10" class="px-2.5 py-1 bg-slate-700 rounded text-xs font-mono font-bold">170 × 23 (×10)</button>
            </div>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center font-mono space-y-2">
                <div class="text-xs text-slate-400">Anchor Fact: <span class="text-amber-300 font-bold">17 × 23 = 391</span></div>
                <div id="sim13_derivation" class="text-sm text-cyan-300 font-bold">17 × 46 = 17 × (23 × 2) = 391 × 2</div>
                <div id="sim13_result" class="text-lg font-bold text-emerald-400">= 782</div>
            </div>
            <div class="text-[11px] text-center text-slate-400 font-mono">
                No column multiplication required! Algebraic structure yields related products instantly.
            </div>
        </div>
    """,

    "sim_slide_14": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-amber-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">King's Reward 7-Day Growth Race</span>
                <span class="text-xs text-slate-400 font-mono" id="sim14_day_lbl">Day 7 Comparison</span>
            </div>
            <div class="flex justify-between items-center text-xs">
                <span>Select Day (1 to 10): <strong id="sim14_d_val" class="text-amber-400">7</strong></span>
                <input type="range" id="sim14_day" min="1" max="10" value="7" oninput="updateSim14()" class="w-48 accent-amber-400">
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs font-mono text-center">
                <div class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30">
                    <span class="text-emerald-400 font-bold block text-[11px]">Choice A (₹ 100k Flat)</span>
                    <p class="text-slate-300 text-[10px]">Today: ₹ 100,000</p>
                    <p class="text-emerald-300 font-bold text-sm mt-1" id="sim14_tot_a">Total: ₹ 700,000</p>
                </div>
                <div class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30">
                    <span class="text-cyan-400 font-bold block text-[11px]">Choice B (Doubling ×2)</span>
                    <p class="text-slate-300 text-[10px]" id="sim14_day_b">Today: 128 coins</p>
                    <p class="text-cyan-300 font-bold text-sm mt-1" id="sim14_tot_b">Total: 254 coins</p>
                </div>
                <div class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30">
                    <span class="text-amber-400 font-bold block text-[11px]">Choice C (Quintupling ×5)</span>
                    <p class="text-slate-300 text-[10px]" id="sim14_day_c">Today: 15,625 coins</p>
                    <p class="text-amber-300 font-bold text-sm mt-1" id="sim14_tot_c">Total: 19,531 coins</p>
                </div>
            </div>
            <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                <svg id="sim14_svg" viewBox="0 0 380 70" class="w-full max-h-20"></svg>
            </div>
            <div id="sim14_verdict" class="text-xs text-center font-mono text-emerald-300 font-bold">
                At Day 7: Choice A wins with ₹ 700,000! (Slide to Day 10 to see Choice C overtake everything!)
            </div>
        </div>
    """,

    "sim_slide_15": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Palindromic Repunit & 9s Staircase</span>
                <span class="text-xs text-slate-400 font-mono">Numerical Harmony</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim15Mode('repunits')" id="sim15_m_rep" class="px-3 py-1 bg-indigo-600 rounded font-bold">Repunit Mountains</button>
                <button onclick="setSim15Mode('nines')" id="sim15_m_nine" class="px-3 py-1 bg-slate-700 rounded font-bold">9s Staircase</button>
            </div>
            <div id="sim15_content" class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 font-mono text-center space-y-1 text-xs"></div>
            <div class="text-[11px] text-center text-slate-400 font-mono">
                Observe the peak digit in each repunit product matching the number of 1s in the factor!
            </div>
        </div>
    """,

    "sim_slide_16": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-teal-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Algebraic Bridge & Tournament Ledger</span>
                <span class="text-xs text-slate-400 font-mono">n × (n + 1) = n² + n</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim16Tab('algebra')" id="sim16_t_alg" class="px-3 py-1 bg-teal-600 rounded font-bold">Adjacent Products</button>
                <button onclick="setSim16Tab('tournament')" id="sim16_t_tour" class="px-3 py-1 bg-slate-700 rounded font-bold">Tournament Ledger</button>
            </div>
            <div id="sim16_body" class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs font-mono"></div>
        </div>
    """
}


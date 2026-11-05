# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: Simulators 1 to 8
"""

SIMULATORS_PART1 = {
    "sim_slide_1": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-emerald-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Pouch Array & Shape Decrypter</span>
                <span class="text-xs text-slate-400 font-mono" id="sim1_tray_tally">4 Trays × (6 × 5) = 120 Pouches</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <!-- Shape decrypter panel -->
                <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700 space-y-2">
                    <span class="font-bold text-amber-300 block">Shape Puzzle Solver</span>
                    <div class="p-2 bg-slate-900/80 rounded border border-slate-700 space-y-1 font-mono text-[11px]">
                        <p>1. ◯ × ◯ = <span id="sim1_circ_sq">36</span> ➔ <strong>◯ = <span id="sim1_circ_val" class="text-emerald-400">6</span></strong></p>
                        <p>2. ◯ × △ = <span id="sim1_tri_prod">48</span> ➔ <strong>△ = <span id="sim1_tri_val" class="text-cyan-400">8</span></strong> (48 ÷ 6)</p>
                        <p>3. △ × ▢ = <span id="sim1_sq_prod">80</span> ➔ <strong>▢ = <span id="sim1_sq_val" class="text-purple-400">10</span></strong> (80 ÷ 8)</p>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="setSim1Puzzle(36, 48, 80)" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[10px] font-bold">Puzzle A (36, 48, 80)</button>
                        <button onclick="setSim1Puzzle(49, 63, 72)" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[10px] font-bold">Puzzle B (49, 63, 72)</button>
                    </div>
                </div>
                <!-- Array Controls -->
                <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700 space-y-2">
                    <span class="font-bold text-cyan-300 block">Pouch Tray Configurator</span>
                    <div class="space-y-1.5">
                        <div class="flex justify-between items-center text-[11px]">
                            <span>Rows per Tray: <strong id="sim1_rows_val" class="text-cyan-400">6</strong></span>
                            <input type="range" id="sim1_rows" min="2" max="8" value="6" oninput="updateSim1Array()" class="w-24 accent-cyan-400">
                        </div>
                        <div class="flex justify-between items-center text-[11px]">
                            <span>Cols per Tray: <strong id="sim1_cols_val" class="text-cyan-400">5</strong></span>
                            <input type="range" id="sim1_cols" min="2" max="8" value="5" oninput="updateSim1Array()" class="w-24 accent-cyan-400">
                        </div>
                        <div class="flex justify-between items-center text-[11px]">
                            <span>Trays Count: <strong id="sim1_trays_val" class="text-amber-400">4</strong></span>
                            <input type="range" id="sim1_trays" min="1" max="5" value="4" oninput="updateSim1Array()" class="w-24 accent-amber-400">
                        </div>
                    </div>
                </div>
            </div>
            <!-- SVG Pouch Grid Display -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim1_svg" viewBox="0 0 380 140" class="w-full max-h-36"></svg>
                <div id="sim1_summary" class="text-xs font-mono text-emerald-300 font-bold mt-2">1 Tray = 6 × 5 = 30 pouches | 4 Trays = 120 total pouches</div>
            </div>
        </div>
    """,

    "sim_slide_2": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Commutative Property & Zero Visualizer</span>
                <span class="text-xs text-slate-400 font-mono" id="sim2_formula">3 × 2 = 2 × 3 = 6</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center">
                <button id="sim2_btn_3x2" onclick="setSim2Mode('3x2')" class="px-3 py-1.5 bg-indigo-600 rounded-lg text-xs font-bold">Show 3 Groups of 2</button>
                <button id="sim2_btn_2x3" onclick="setSim2Mode('2x3')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded-lg text-xs font-bold">Show 2 Groups of 3</button>
                <button id="sim2_btn_zero" onclick="setSim2Mode('zero')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded-lg text-xs font-bold">Show 4 Groups of 0</button>
            </div>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[150px]">
                <div id="sim2_display" class="flex flex-wrap items-center justify-center gap-4"></div>
                <div id="sim2_explanation" class="text-xs font-mono text-amber-300 font-bold mt-3">3 crates with 2 bottles each = 3 × 2 = 6 bottles</div>
            </div>
            <div class="text-[11px] text-slate-400 text-center font-mono">
                Commutative Invariant: Rotating the crate grid 90° does not change the total bottle count!
            </div>
        </div>
    """,

    "sim_slide_3": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-cyan-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Place Value Shift Engine</span>
                <span class="text-xs text-slate-400 font-mono">Multiply by 10, 100, 1,000</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                <div class="flex items-center gap-2">
                    <span>Base Number:</span>
                    <input type="number" id="sim3_input" value="34" min="1" max="99" onchange="runSim3Shift()" class="w-16 px-2 py-1 bg-slate-800 border border-slate-600 rounded text-center font-mono font-bold text-amber-300">
                </div>
                <div class="flex gap-2">
                    <button onclick="setSim3Mult(1)" id="sim3_m1" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold text-xs">× 1</button>
                    <button onclick="setSim3Mult(10)" id="sim3_m10" class="px-2.5 py-1 bg-cyan-600 rounded font-mono font-bold text-xs">× 10</button>
                    <button onclick="setSim3Mult(100)" id="sim3_m100" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold text-xs">× 100</button>
                    <button onclick="setSim3Mult(1000)" id="sim3_m1000" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold text-xs">× 1,000</button>
                </div>
            </div>
            <!-- Place Value Grid -->
            <div class="overflow-x-auto">
                <table class="w-full text-center text-xs font-mono border border-slate-700 bg-slate-950 rounded-lg">
                    <thead class="bg-slate-800 text-slate-400 text-[11px]">
                        <tr>
                            <th class="p-2 border-r border-slate-700">Ten Thousands (TTh)</th>
                            <th class="p-2 border-r border-slate-700">Thousands (Th)</th>
                            <th class="p-2 border-r border-slate-700">Hundreds (H)</th>
                            <th class="p-2 border-r border-slate-700">Tens (T)</th>
                            <th class="p-2">Ones (O)</th>
                        </tr>
                    </thead>
                    <tbody class="text-base font-bold">
                        <tr id="sim3_row" class="h-12 text-slate-300">
                            <td class="p-2 border-r border-slate-800 text-slate-600" id="sim3_tth">-</td>
                            <td class="p-2 border-r border-slate-800 text-slate-600" id="sim3_th">-</td>
                            <td class="p-2 border-r border-slate-800 text-amber-300" id="sim3_h">-</td>
                            <td class="p-2 border-r border-slate-800 text-amber-300" id="sim3_t">3</td>
                            <td class="p-2 text-cyan-300" id="sim3_o">4</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div id="sim3_text" class="text-xs text-center font-mono text-emerald-400 font-bold bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
                34 × 10 = 340 (digits shifted 1 place left; one trailing zero appended)
            </div>
        </div>
    """,

    "sim_slide_4": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-teal-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">3-Way Strategy Comparator</span>
                <span class="text-xs text-slate-400 font-mono" id="sim4_target">Target: 18 × 5 = 90</span>
            </div>
            <div class="flex items-center justify-between gap-3 text-xs">
                <span>Select Factor:</span>
                <div class="flex gap-2">
                    <button onclick="setSim4Factor(18)" id="sim4_f18" class="px-2.5 py-1 bg-teal-600 rounded font-mono font-bold">18 × 5</button>
                    <button onclick="setSim4Factor(24)" id="sim4_f24" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">24 × 5</button>
                    <button onclick="setSim4Factor(36)" id="sim4_f36" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">36 × 5</button>
                </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3 bg-slate-950 rounded-xl border border-teal-500/40 space-y-1.5">
                    <span class="font-bold text-teal-300 block text-[11px]">Strategy 1: Halve & Double</span>
                    <p class="font-mono text-slate-300" id="sim4_hd_1">• 18 ÷ 2 = 9</p>
                    <p class="font-mono text-slate-300" id="sim4_hd_2">• 5 × 2 = 10</p>
                    <p class="font-mono text-emerald-400 font-bold text-sm" id="sim4_hd_res">➔ 9 × 10 = 90</p>
                </div>
                <div class="p-3 bg-slate-950 rounded-xl border border-cyan-500/40 space-y-1.5">
                    <span class="font-bold text-cyan-300 block text-[11px]">Strategy 2: Partitioning</span>
                    <p class="font-mono text-slate-300" id="sim4_pt_1">• 10 × 5 = 50</p>
                    <p class="font-mono text-slate-300" id="sim4_pt_2">• 8 × 5 = 40</p>
                    <p class="font-mono text-cyan-400 font-bold text-sm" id="sim4_pt_res">➔ 50 + 40 = 90</p>
                </div>
                <div class="p-3 bg-slate-950 rounded-xl border border-amber-500/40 space-y-1.5">
                    <span class="font-bold text-amber-300 block text-[11px]">Strategy 3: Compensation</span>
                    <p class="font-mono text-slate-300" id="sim4_cp_1">• 20 × 5 = 100</p>
                    <p class="font-mono text-slate-300" id="sim4_cp_2">• - (2 × 5) = -10</p>
                    <p class="font-mono text-amber-400 font-bold text-sm" id="sim4_cp_res">➔ 100 - 10 = 90</p>
                </div>
            </div>
            <div class="p-2.5 bg-slate-800/80 rounded-lg text-center font-mono text-xs text-slate-300 border border-slate-700">
                All 3 distinct pathways arrive at the exact same product of <strong id="sim4_final" class="text-emerald-400">90</strong>!
            </div>
        </div>
    """,

    "sim_slide_5": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-emerald-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Rectangle Slice & Paste Area Model</span>
                <span class="text-xs text-slate-400 font-mono" id="sim5_dim">16 × 25 = 400 m²</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                <div class="flex items-center gap-2">
                    <span>Problem:</span>
                    <button onclick="setSim5Preset(16, 25)" id="sim5_p1" class="px-2.5 py-1 bg-emerald-600 rounded font-mono font-bold">16 × 25</button>
                    <button onclick="setSim5Preset(24, 50)" id="sim5_p2" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">24 × 50</button>
                    <button onclick="setSim5Preset(28, 25)" id="sim5_p3" class="px-2.5 py-1 bg-slate-700 rounded font-mono font-bold">28 × 25</button>
                </div>
                <button onclick="toggleSim5Slice()" id="sim5_slice_btn" class="px-3 py-1 bg-amber-600 hover:bg-amber-500 rounded font-bold text-xs">
                    ✂️ Slice & Double Step
                </button>
            </div>
            <!-- SVG Rectangle Visualization -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim5_svg" viewBox="0 0 380 140" class="w-full max-h-36"></svg>
                <div id="sim5_step_text" class="text-xs font-mono text-cyan-300 font-bold mt-2">
                    Original Rectangle: Width 25 m × Height 16 m = 400 m²
                </div>
            </div>
        </div>
    """,

    "sim_slide_6": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-rose-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Nearest Friendly Ten Compensation Dial</span>
                <span class="text-xs text-slate-400 font-mono" id="sim6_preview">4 × 19 = 76</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span>Multiplier: <strong id="sim6_m_val" class="text-amber-400">4</strong></span>
                        <input type="range" id="sim6_m" min="2" max="9" value="4" oninput="updateSim6()" class="w-28 accent-amber-400">
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Target Number: <strong id="sim6_t_val" class="text-cyan-400">19</strong></span>
                        <select id="sim6_t" onchange="updateSim6()" class="bg-slate-800 border border-slate-600 rounded px-2 py-1 text-xs font-mono">
                            <option value="19">19 (20 - 1)</option>
                            <option value="29">29 (30 - 1)</option>
                            <option value="39">39 (40 - 1)</option>
                            <option value="48">48 (50 - 2)</option>
                            <option value="21">21 (20 + 1)</option>
                            <option value="31">31 (30 + 1)</option>
                            <option value="42">42 (40 + 2)</option>
                        </select>
                    </div>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono space-y-1 text-xs">
                    <p class="text-slate-400">Friendly Ten Round: <span id="sim6_round_calc" class="text-amber-300 font-bold">4 × 20 = 80</span></p>
                    <p class="text-slate-400">Adjustment: <span id="sim6_adjust_calc" class="text-rose-400 font-bold">- (4 × 1) = -4</span></p>
                    <p class="text-emerald-400 font-bold text-sm pt-1 border-t border-slate-800">Final Product: <span id="sim6_final_calc">80 - 4 = 76</span></p>
                </div>
            </div>
            <!-- Visual Bar -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim6_svg" viewBox="0 0 380 60" class="w-full max-h-16"></svg>
            </div>
        </div>
    """,

    "sim_slide_7": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Real-World Scenario Multiplier</span>
                <span class="text-xs text-slate-400 font-mono" id="sim7_mode_title">Auditorium Seating</span>
            </div>
            <div class="flex gap-2 justify-center">
                <button onclick="setSim7Mode('auditorium')" id="sim7_m_aud" class="px-3 py-1 bg-indigo-600 rounded text-xs font-bold">Auditorium</button>
                <button onclick="setSim7Mode('milk')" id="sim7_m_milk" class="px-3 py-1 bg-slate-700 rounded text-xs font-bold">Milk Herd</button>
                <button onclick="setSim7Mode('kurta')" id="sim7_m_kurta" class="px-3 py-1 bg-slate-700 rounded text-xs font-bold">Kurta Fabric</button>
            </div>
            <div id="sim7_controls" class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs bg-slate-800/80 p-3 rounded-xl border border-slate-700"></div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-center font-mono space-y-1">
                <div id="sim7_calculation" class="text-sm font-bold text-emerald-400">24 rows × 18 seats = 432 seats</div>
                <div id="sim7_subtext" class="text-xs text-slate-400">24 × (20 - 2) = 480 - 48 = 432</div>
            </div>
        </div>
    """,

    "sim_slide_8": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-emerald-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Compost Savings & Waste Analyzer</span>
                <span class="text-xs text-slate-400 font-mono">Ecological Arithmetic</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="space-y-3 bg-slate-800/80 p-3 rounded-xl border border-slate-700">
                    <div>
                        <div class="flex justify-between items-center mb-1">
                            <span>Daily Kitchen Waste: <strong id="sim8_waste_val" class="text-emerald-400">350 g</strong></span>
                        </div>
                        <input type="range" id="sim8_waste" min="100" max="800" step="25" value="350" oninput="updateSim8()" class="w-full accent-emerald-400">
                    </div>
                    <div>
                        <div class="flex justify-between items-center mb-1">
                            <span>Cost per 5kg Commercial Bag: <strong id="sim8_cost_val" class="text-amber-400">₹ 120</strong></span>
                        </div>
                        <input type="range" id="sim8_cost" min="60" max="250" step="10" value="120" oninput="updateSim8()" class="w-full accent-amber-400">
                    </div>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono space-y-1.5 text-xs">
                    <p class="text-slate-300">• 30-Day Waste: <strong id="sim8_m_waste" class="text-cyan-300">10.5 kg</strong></p>
                    <p class="text-slate-300">• 365-Day Annual Waste: <strong id="sim8_y_waste" class="text-cyan-300">127.75 kg</strong></p>
                    <p class="text-slate-300">• 5kg Compost Bags: <strong id="sim8_bags" class="text-emerald-400">25 bags</strong></p>
                    <div class="border-t border-slate-800 pt-1 text-sm font-bold text-amber-300">
                        Annual Savings: <span id="sim8_savings">₹ 3,000</span>
                    </div>
                </div>
            </div>
            <div class="text-[11px] text-center text-slate-400 font-mono">
                Converting organic waste preserves soil health and retains rupees in the family budget!
            </div>
        </div>
    """
}


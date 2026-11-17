# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 11: Simulators 1 to 8 HTML Templates
"""

import json

simulators_part1 = {
    1: {
        "title": "Electric Charge & Drift Velocity Studio",
        "description": "Visualize electron motion and conventional current in a copper conductor. Contrast random thermal motion against net drift velocity when an electric field is applied, and compute $I = Q/t$.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Electric Field:</span>
                        <button id="sim1_btn_toggle" onclick="sim1ToggleField()" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Field: ON</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Net Charge Q (C):</span>
                        <input type="range" id="sim1_charge_slider" min="1" max="10" value="5" step="0.5" oninput="sim1Update()" class="w-24 accent-amber-500">
                        <span id="sim1_charge_txt" class="text-amber-400 font-mono font-bold">5.0 C</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Time t (s):</span>
                        <input type="range" id="sim1_time_slider" min="1" max="10" value="2" step="0.5" oninput="sim1Update()" class="w-20 accent-amber-500">
                        <span id="sim1_time_txt" class="text-teal-400 font-mono font-bold">2.0 s</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim1_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Electric Current (I = Q/t)</div>
                        <div id="sim1_val_current" class="text-amber-400 font-bold text-sm">2.50 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Electrons Transferred</div>
                        <div id="sim1_val_electrons" class="text-teal-400 font-bold text-sm">3.12 × 10¹⁹</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Electron Drift Direction</div>
                        <div id="sim1_val_drift" class="text-cyan-400 font-bold text-sm">Right → Left (- to +)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Conventional Current</div>
                        <div id="sim1_val_conventional" class="text-emerald-400 font-bold text-sm">Left → Right (+ to -)</div>
                    </div>
                </div>
            </div>
        """
    },
    2: {
        "title": "Circuit & In-Line Ammeter Laboratory",
        "description": "Construct an electric loop with dry cell, torch bulb, plug key, and series ammeter. Toggle the plug key to observe electron flow, ammeter needle deflection, and filament glow.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Plug Key:</span>
                        <button id="sim2_btn_key" onclick="sim2ToggleKey()" class="px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold">Plug Inserted (Closed)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Cell Voltage:</span>
                        <select id="sim2_cell_select" onchange="sim2Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="1.5">1 Cell (1.5 V)</option>
                            <option value="3.0" selected>2 Cells (3.0 V)</option>
                            <option value="4.5">3 Cells (4.5 V)</option>
                            <option value="6.0">4 Cells (6.0 V)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Bulb Resistance:</span>
                        <input type="range" id="sim2_res_slider" min="5" max="25" value="10" step="1" oninput="sim2Update()" class="w-20 accent-amber-500">
                        <span id="sim2_res_txt" class="text-amber-400 font-mono font-bold">10 Ω</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim2_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Circuit State</div>
                        <div id="sim2_val_state" class="text-emerald-400 font-bold text-sm">Closed & Continuous</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ammeter Reading (Series)</div>
                        <div id="sim2_val_ammeter" class="text-amber-400 font-bold text-sm">0.300 A (300 mA)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Lamp Illuminance</div>
                        <div id="sim2_val_glow" class="text-yellow-400 font-bold text-sm">0.90 W (Bright)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ammeter Internal R</div>
                        <div id="sim2_val_rin" class="text-cyan-400 font-bold text-sm">≈ 0 Ω (Negligible)</div>
                    </div>
                </div>
            </div>
        """
    },
    3: {
        "title": "Electric Potential Difference & Voltmeter Studio",
        "description": "Simulate work done $W$ against electric fields to transport charge $Q$ between terminals. Connect a high-resistance voltmeter in parallel across circuit components to gauge $V = W/Q$.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Work Done W (J):</span>
                        <input type="range" id="sim3_work_slider" min="6" max="60" value="24" step="2" oninput="sim3Update()" class="w-24 accent-amber-500">
                        <span id="sim3_work_txt" class="text-amber-400 font-mono font-bold">24 J</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Charge Q (C):</span>
                        <input type="range" id="sim3_charge_slider" min="1" max="10" value="2" step="0.5" oninput="sim3Update()" class="w-20 accent-amber-500">
                        <span id="sim3_charge_txt" class="text-teal-400 font-mono font-bold">2.0 C</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Voltmeter Tap:</span>
                        <select id="sim3_tap_select" onchange="sim3Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="parallel">Parallel Across Component</option>
                            <option value="series">Erroneous Series Connection</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim3_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Potential Difference (V = W/Q)</div>
                        <div id="sim3_val_voltage" class="text-amber-400 font-bold text-sm">12.0 V</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Volt Definition</div>
                        <div id="sim3_val_unit" class="text-teal-400 font-bold text-sm">1 V = 1 Joule / 1 Coulomb</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Voltmeter Resistance</div>
                        <div id="sim3_val_voltr" class="text-cyan-400 font-bold text-sm">Very High (Draws zero I)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Connection Status</div>
                        <div id="sim3_val_status" class="text-emerald-400 font-bold text-sm">Correct Parallel Hookup</div>
                    </div>
                </div>
            </div>
        """
    },
    4: {
        "title": "Circuit Diagram Symbol Workbench",
        "description": "Inspect and assemble standard NCERT electrical schematic symbols. Click on components to examine their international engineering representations and test interactive switches.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Select Schematic Symbol:</span>
                        <select id="sim4_sym_select" onchange="sim4Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="cell">1. Electric Cell</option>
                            <option value="battery">2. Battery of Cells</option>
                            <option value="open_key">3. Plug Key (Open)</option>
                            <option value="closed_key">4. Plug Key (Closed)</option>
                            <option value="wire_joint">5. Wire Joint</option>
                            <option value="wire_cross">6. Wire Crossing without Joint</option>
                            <option value="bulb">7. Electric Bulb</option>
                            <option value="resistor">8. Fixed Resistor</option>
                            <option value="rheostat">9. Rheostat (Variable R)</option>
                            <option value="ammeter">10. Ammeter (Series)</option>
                            <option value="voltmeter">11. Voltmeter (Parallel)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim4CycleNext()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Next Symbol →</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim4_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">NCERT Standard Symbol</div>
                        <div id="sim4_val_name" class="text-amber-400 font-bold text-sm">Electric Cell</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Function & Role</div>
                        <div id="sim4_val_role" class="text-teal-400 font-bold text-sm">Maintains potential difference</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Polarity & Connection</div>
                        <div id="sim4_val_polarity" class="text-cyan-400 font-bold text-sm">Long line (+), Short thick line (-)</div>
                    </div>
                </div>
            </div>
        """
    },
    5: {
        "title": "Ohm's Law Activity 11.1 Verification",
        "description": "Replicate Georg Simon Ohm's seminal 1827 experiment. Add cells one by one (1.5 V, 3.0 V, 4.5 V, 6.0 V) across a nichrome wire and observe the constant proportionality $V/I = R$.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Number of 1.5 V Cells:</span>
                        <div class="inline-flex rounded-lg border border-slate-700 p-0.5 bg-slate-800">
                            <button id="sim5_btn_c1" onclick="sim5SetCells(1)" class="px-2.5 py-0.5 rounded text-xs bg-amber-600 text-slate-950 font-bold">1 Cell</button>
                            <button id="sim5_btn_c2" onclick="sim5SetCells(2)" class="px-2.5 py-0.5 rounded text-xs text-slate-300">2 Cells</button>
                            <button id="sim5_btn_c3" onclick="sim5SetCells(3)" class="px-2.5 py-0.5 rounded text-xs text-slate-300">3 Cells</button>
                            <button id="sim5_btn_c4" onclick="sim5SetCells(4)" class="px-2.5 py-0.5 rounded text-xs text-slate-300">4 Cells</button>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Nichrome Wire R:</span>
                        <input type="range" id="sim5_res_slider" min="5" max="20" value="10" step="1" oninput="sim5Update()" class="w-20 accent-amber-500">
                        <span id="sim5_res_txt" class="text-amber-400 font-mono font-bold">10 Ω</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim5_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Terminal Voltage V</div>
                        <div id="sim5_val_voltage" class="text-amber-400 font-bold text-sm">1.50 V</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Circuit Current I</div>
                        <div id="sim5_val_current" class="text-teal-400 font-bold text-sm">0.15 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ratio V / I</div>
                        <div id="sim5_val_ratio" class="text-cyan-400 font-bold text-sm">10.00 V/A (Ω)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ohmic Status</div>
                        <div id="sim5_val_status" class="text-emerald-400 font-bold text-sm">Linear Constant R</div>
                    </div>
                </div>
            </div>
        """
    },
    6: {
        "title": "V-I Characteristic Graph & Slope Studio",
        "description": "Plot experimental potential difference $V$ against electric current $I$. Compute the gradient/slope to determine resistance $R$, and compare ohmic metals with varying resistances.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Specimen Conductor:</span>
                        <select id="sim6_wire_select" onchange="sim6Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="copper">Sample A (Copper Wire - 2 Ω)</option>
                            <option value="iron" selected>Sample B (Nichrome Wire - 10 Ω)</option>
                            <option value="nichrome">Sample C (Thin Constantan - 25 Ω)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Sweep Potential V:</span>
                        <input type="range" id="sim6_v_slider" min="0" max="12" value="6" step="0.5" oninput="sim6Update()" class="w-24 accent-amber-500">
                        <span id="sim6_v_txt" class="text-amber-400 font-mono font-bold">6.0 V</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim6_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Applied Voltage V</div>
                        <div id="sim6_val_v" class="text-amber-400 font-bold text-sm">6.0 V</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Resulting Current I</div>
                        <div id="sim6_val_i" class="text-teal-400 font-bold text-sm">0.60 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Slope (ΔV / ΔI = R)</div>
                        <div id="sim6_val_slope" class="text-cyan-400 font-bold text-sm">10.0 Ω</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Graph Line Profile</div>
                        <div id="sim6_val_line" class="text-emerald-400 font-bold text-sm">Straight line through origin</div>
                    </div>
                </div>
            </div>
        """
    },
    7: {
        "title": "Resistance Geometric Factors (l, A, Material)",
        "description": "Experiment with Activity 11.3 by altering wire length $l$, cross-sectional area $A$ (thickness), and material to prove the governing formula $R = \\rho l / A$.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Material:</span>
                        <select id="sim7_mat_select" onchange="sim7Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="copper">Copper (ρ = 1.62 × 10⁻⁸ Ω·m)</option>
                            <option value="aluminium">Aluminium (ρ = 2.63 × 10⁻⁸ Ω·m)</option>
                            <option value="iron">Iron (ρ = 10.0 × 10⁻⁸ Ω·m)</option>
                            <option value="nichrome" selected>Nichrome (ρ = 100 × 10⁻⁸ Ω·m)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Length l (m):</span>
                        <input type="range" id="sim7_len_slider" min="0.5" max="5.0" value="1.0" step="0.5" oninput="sim7Update()" class="w-20 accent-amber-500">
                        <span id="sim7_len_txt" class="text-amber-400 font-mono font-bold">1.0 m</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Area A (mm²):</span>
                        <input type="range" id="sim7_area_slider" min="0.2" max="2.0" value="0.5" step="0.1" oninput="sim7Update()" class="w-20 accent-amber-500">
                        <span id="sim7_area_txt" class="text-teal-400 font-mono font-bold">0.5 mm²</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim7_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Wire Resistance R</div>
                        <div id="sim7_val_r" class="text-amber-400 font-bold text-sm">2.00 Ω</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Length Effect (R ∝ l)</div>
                        <div id="sim7_val_leffect" class="text-teal-400 font-bold text-sm">2× Length doubles R</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Area Effect (R ∝ 1/A)</div>
                        <div id="sim7_val_aeffect" class="text-cyan-400 font-bold text-sm">2× Area halves R</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Current (at 3 V)</div>
                        <div id="sim7_val_current" class="text-emerald-400 font-bold text-sm">1.50 A</div>
                    </div>
                </div>
            </div>
        """
    },
    8: {
        "title": "Electrical Resistivity Spectrum Analyzer",
        "description": "Examine the resistivity table across conductors, alloys, and insulators. Discover why nichrome alloy is chosen for toaster and iron heating elements over pure metals.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Category:</span>
                        <div class="inline-flex rounded-lg border border-slate-700 p-0.5 bg-slate-800">
                            <button id="sim8_btn_cat1" onclick="sim8SetCat('conductor')" class="px-2.5 py-0.5 rounded text-xs bg-amber-600 text-slate-950 font-bold">Conductors</button>
                            <button id="sim8_btn_cat2" onclick="sim8SetCat('alloy')" class="px-2.5 py-0.5 rounded text-xs text-slate-300">Alloys</button>
                            <button id="sim8_btn_cat3" onclick="sim8SetCat('insulator')" class="px-2.5 py-0.5 rounded text-xs text-slate-300">Insulators</button>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Heating Test:</span>
                        <button id="sim8_btn_heat" onclick="sim8ToggleHeat()" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold">Oxidation Stress: ON</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim8_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Resistivity ρ Range</div>
                        <div id="sim8_val_range" class="text-amber-400 font-bold text-sm">10⁻⁸ to 10⁻⁶ Ω·m</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">High-Temp Oxidation</div>
                        <div id="sim8_val_oxid" class="text-teal-400 font-bold text-sm">Alloy does NOT burn</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Typical Application</div>
                        <div id="sim8_val_app" class="text-cyan-400 font-bold text-sm">Transmission Cables</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Glass / Rubber ρ</div>
                        <div id="sim8_val_insul" class="text-emerald-400 font-bold text-sm">10¹² to 10¹⁷ Ω·m</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch11_sims_part1.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part1, f, indent=2)

print("Saved .agents/c10s_ch11_sims_part1.json successfully!")

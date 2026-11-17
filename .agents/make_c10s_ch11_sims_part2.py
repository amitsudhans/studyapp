# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 11: Simulators 9 to 16 HTML Templates
"""

import json

simulators_part2 = {
    9: {
        "title": "Series Resistors & Ammeter Position Lab",
        "description": "Examine Activity 11.4 with three resistors ($R_1, R_2, R_3$) in series. Shift the ammeter to different positions along the loop to verify that current is identical everywhere.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Ammeter Position:</span>
                        <select id="sim9_pos_select" onchange="sim9Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="before_r1">Position 1: Before R1</option>
                            <option value="between_r1_r2" selected>Position 2: Between R1 & R2</option>
                            <option value="between_r2_r3">Position 3: Between R2 & R3</option>
                            <option value="after_r3">Position 4: After R3 (Return)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Total Voltage:</span>
                        <input type="range" id="sim9_v_slider" min="3" max="12" value="6" step="1" oninput="sim9Update()" class="w-20 accent-amber-500">
                        <span id="sim9_v_txt" class="text-amber-400 font-mono font-bold">6 V</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim9_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ammeter Current Reading</div>
                        <div id="sim9_val_i" class="text-amber-400 font-bold text-sm">0.500 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Resistance (R_s)</div>
                        <div id="sim9_val_rtot" class="text-teal-400 font-bold text-sm">12.0 Ω (1+2+3)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Current Invariance</div>
                        <div id="sim9_val_invar" class="text-cyan-400 font-bold text-sm">Uniform at all points</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Individual Resistors</div>
                        <div id="sim9_val_res" class="text-emerald-400 font-bold text-sm">R1=2Ω, R2=4Ω, R3=6Ω</div>
                    </div>
                </div>
            </div>
        """
    },
    10: {
        "title": "Series Circuit Analysis & Voltage Drops",
        "description": "Analyze Activity 11.5 and Example 11.7. Measure individual potential drops across each series resistor with a voltmeter to confirm $V = V_1 + V_2 + V_3$ and $R_s = R_1 + R_2 + R_3$.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Preset Scenario:</span>
                        <select id="sim10_preset_select" onchange="sim10UpdatePreset()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="ex11_7">Example 11.7 (Lamp 20Ω + Wire 4Ω on 6V)</option>
                            <option value="three_r" selected>Activity 11.5 (R1=2Ω, R2=3Ω, R3=5Ω on 10V)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Voltmeter Probe:</span>
                        <select id="sim10_probe_select" onchange="sim10Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="total">Across Complete Combination (V)</option>
                            <option value="v1">Across Resistor R1 (V1)</option>
                            <option value="v2">Across Resistor R2 (V2)</option>
                            <option value="v3">Across Resistor R3 (V3)</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim10_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Equivalent R_s</div>
                        <div id="sim10_val_rs" class="text-amber-400 font-bold text-sm">10.0 Ω</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Loop Current I</div>
                        <div id="sim10_val_i" class="text-teal-400 font-bold text-sm">1.00 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Voltmeter Probe Reading</div>
                        <div id="sim10_val_vprobe" class="text-cyan-400 font-bold text-sm">V_total = 10.0 V</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Voltage Conservation</div>
                        <div id="sim10_val_sum" class="text-emerald-400 font-bold text-sm">V = V1 + V2 + V3</div>
                    </div>
                </div>
            </div>
        """
    },
    11: {
        "title": "Parallel Resistor Network & Current Branching",
        "description": "Simulate Activity 11.6 with three parallel resistors. Measure individual branch currents ($I_1, I_2, I_3$) and verify $1/R_p = 1/R_1 + 1/R_2 + 1/R_3$ with identical voltage across all branches.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Total Voltage:</span>
                        <input type="range" id="sim11_v_slider" min="6" max="24" value="12" step="2" oninput="sim11Update()" class="w-20 accent-amber-500">
                        <span id="sim11_v_txt" class="text-amber-400 font-mono font-bold">12 V</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Branch Switch:</span>
                        <button id="sim11_btn_b1" onclick="sim11ToggleBranch(1)" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">R1: ON</button>
                        <button id="sim11_btn_b2" onclick="sim11ToggleBranch(2)" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">R2: ON</button>
                        <button id="sim11_btn_b3" onclick="sim11ToggleBranch(3)" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">R3: ON</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim11_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Equivalent Resistance (R_p)</div>
                        <div id="sim11_val_rp" class="text-amber-400 font-bold text-sm">3.33 Ω</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Current (I = Σ I_k)</div>
                        <div id="sim11_val_itot" class="text-teal-400 font-bold text-sm">3.60 A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Branch Currents (I1, I2, I3)</div>
                        <div id="sim11_val_ibranches" class="text-cyan-400 font-bold text-sm">2.0A, 1.0A, 0.6A</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Voltage Across Each Branch</div>
                        <div id="sim11_val_vbranch" class="text-emerald-400 font-bold text-sm">Uniform 12.0 V</div>
                    </div>
                </div>
            </div>
        """
    },
    12: {
        "title": "Domestic Parallel vs Series Wiring Lab",
        "description": "Compare domestic parallel circuits with series wiring. Simulate appliance failure in both configurations to understand why home installations mandate parallel connections.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Wiring Topology:</span>
                        <button id="sim12_btn_parallel" onclick="sim12SetTopology('parallel')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Parallel (Domestic)</button>
                        <button id="sim12_btn_series" onclick="sim12SetTopology('series')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Series (Fairy Lights)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Fault Appliance 1:</span>
                        <button id="sim12_btn_fault" onclick="sim12ToggleFault()" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold">Blow Bulb 1</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim12_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Bulb 1 (50 W)</div>
                        <div id="sim12_val_app1" class="text-amber-400 font-bold text-sm">Operating Normal</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ceiling Fan (75 W)</div>
                        <div id="sim12_val_app2" class="text-teal-400 font-bold text-sm">Operating Normal</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Electric Heater (1500 W)</div>
                        <div id="sim12_val_app3" class="text-cyan-400 font-bold text-sm">Operating Normal</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Supply Voltage across Loads</div>
                        <div id="sim12_val_voltstatus" class="text-emerald-400 font-bold text-sm">Each gets full 220 V</div>
                    </div>
                </div>
            </div>
        """
    },
    13: {
        "title": "Joule's Heating Law Calorimeter Studio",
        "description": "Simulate Joule's heating effect ($H = I^2 R t$). Adjust electric current, resistance of heating coil, and duration to measure heat generated and thermal rise in water.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current I (A):</span>
                        <input type="range" id="sim13_i_slider" min="1" max="5" value="2" step="0.5" oninput="sim13Update()" class="w-20 accent-amber-500">
                        <span id="sim13_i_txt" class="text-amber-400 font-mono font-bold">2.0 A</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Resistance R (Ω):</span>
                        <input type="range" id="sim13_r_slider" min="5" max="25" value="10" step="5" oninput="sim13Update()" class="w-20 accent-amber-500">
                        <span id="sim13_r_txt" class="text-teal-400 font-mono font-bold">10 Ω</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Time t (s):</span>
                        <input type="range" id="sim13_t_slider" min="5" max="60" value="20" step="5" oninput="sim13Update()" class="w-20 accent-amber-500">
                        <span id="sim13_t_txt" class="text-cyan-400 font-mono font-bold">20 s</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim13_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Heat Produced (H = I²Rt)</div>
                        <div id="sim13_val_heat" class="text-amber-400 font-bold text-sm">800 J (0.8 kJ)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Thermal Rise (ΔT)</div>
                        <div id="sim13_val_temp" class="text-rose-400 font-bold text-sm">+3.8 °C</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">I² Dependency</div>
                        <div id="sim13_val_idep" class="text-cyan-400 font-bold text-sm">2× Current yields 4× Heat</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Power Dissipated (P)</div>
                        <div id="sim13_val_power" class="text-emerald-400 font-bold text-sm">40.0 W (J/s)</div>
                    </div>
                </div>
            </div>
        """
    },
    14: {
        "title": "Thermal Appliance & Bulb Filament Studio",
        "description": "Investigate incandescent lamps and electric irons. Observe why high-resistance tungsten filaments glow white-hot at $3380^\\circ\\text{C}$ while copper connecting leads remain cool.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Appliance:</span>
                        <select id="sim14_app_select" onchange="sim14Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="bulb" selected>Incandescent Bulb (Tungsten 3380°C)</option>
                            <option value="iron">Electric Laundry Iron (Nichrome Element)</option>
                            <option value="toaster">Bread Toaster (Nichrome Ribbon)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Operating Power:</span>
                        <input type="range" id="sim14_power_slider" min="20" max="100" value="80" step="10" oninput="sim14Update()" class="w-24 accent-amber-500">
                        <span id="sim14_power_txt" class="text-amber-400 font-mono font-bold">80%</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim14_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Filament Temperature</div>
                        <div id="sim14_val_temp" class="text-amber-400 font-bold text-sm">~2500 °C (Incandescent)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Gas Filling</div>
                        <div id="sim14_val_gas" class="text-teal-400 font-bold text-sm">Inactive Nitrogen & Argon</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Copper Connecting Cords</div>
                        <div id="sim14_val_cord" class="text-cyan-400 font-bold text-sm">Low R: Stays cool (~30°C)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Melting Point of Tungsten</div>
                        <div id="sim14_val_mp" class="text-rose-400 font-bold text-sm">3380 °C (Extremely high)</div>
                    </div>
                </div>
            </div>
        """
    },
    15: {
        "title": "Electric Fuse Safety & Meltdown Simulator",
        "description": "Test circuit protection using standard fuse ratings ($1\\text{ A}, 2\\text{ A}, 3\\text{ A}, 5\\text{ A}, 10\\text{ A}$). Simulate an overcurrent event where the fuse melts and saves costly appliances.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Fuse Rating:</span>
                        <select id="sim15_fuse_select" onchange="sim15Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="1">1 A Fuse</option>
                            <option value="2">2 A Fuse</option>
                            <option value="3">3 A Fuse</option>
                            <option value="5" selected>5 A Fuse (Standard 1 kW load)</option>
                            <option value="10">10 A Fuse</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Load Current:</span>
                        <input type="range" id="sim15_load_slider" min="1" max="12" value="4.5" step="0.5" oninput="sim15Update()" class="w-24 accent-amber-500">
                        <span id="sim15_load_txt" class="text-amber-400 font-mono font-bold">4.5 A</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim15TriggerSurge()" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold">Simulate Short Circuit</button>
                        <button onclick="sim15ResetFuse()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Replace Fuse</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim15_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Fuse Status</div>
                        <div id="sim15_val_status" class="text-emerald-400 font-bold text-sm">Intact & Conducting</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Load Appliance State</div>
                        <div id="sim15_val_app" class="text-amber-400 font-bold text-sm">Protected & Powered</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Fuse Composition</div>
                        <div id="sim15_val_alloy" class="text-cyan-400 font-bold text-sm">Lead-Tin Low Melting Alloy</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Installation Position</div>
                        <div id="sim15_val_pos" class="text-rose-400 font-bold text-sm">Series with Live Wire</div>
                    </div>
                </div>
            </div>
        """
    },
    16: {
        "title": "Electric Power & Commercial Energy Meter",
        "description": "Calculate electrical power ($P = VI = I^2 R = V^2 / R$) and commercial consumption in kilowatt-hours ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J} = 1\\text{ unit}$). Compute monthly electric bill.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Appliance Power:</span>
                        <input type="range" id="sim16_power_slider" min="100" max="2000" value="400" step="50" oninput="sim16Update()" class="w-24 accent-amber-500">
                        <span id="sim16_power_txt" class="text-amber-400 font-mono font-bold">400 W</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Hours / Day:</span>
                        <input type="range" id="sim16_hours_slider" min="1" max="24" value="8" step="1" oninput="sim16Update()" class="w-20 accent-amber-500">
                        <span id="sim16_hours_txt" class="text-teal-400 font-mono font-bold">8 hrs/day</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Tariff Rate (₹/unit):</span>
                        <input type="range" id="sim16_tariff_slider" min="2" max="10" value="5" step="0.5" oninput="sim16Update()" class="w-20 accent-amber-500">
                        <span id="sim16_tariff_txt" class="text-cyan-400 font-mono font-bold">₹5.0 / unit</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim16_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Daily Energy Consumed</div>
                        <div id="sim16_val_daily" class="text-amber-400 font-bold text-sm">3.20 kWh (Units)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Monthly Energy (30 Days)</div>
                        <div id="sim16_val_monthly" class="text-teal-400 font-bold text-sm">96.0 kWh (Units)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Monthly Bill Cost</div>
                        <div id="sim16_val_bill" class="text-emerald-400 font-bold text-sm">₹ 480.00</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">1 kWh in Joules</div>
                        <div id="sim16_val_joules" class="text-cyan-400 font-bold text-sm">3.6 × 10⁶ Joules</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch11_sims_part2.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part2, f, indent=2)

print("Saved .agents/c10s_ch11_sims_part2.json successfully!")

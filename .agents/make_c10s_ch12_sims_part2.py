# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 12: Simulators 9 to 16 HTML Templates
Magnetic Effects of Electric Current
"""

import json

simulators_part2 = {
    9: {
        "title": "Multi-Turn Coil Superposition Analyzer",
        "description": "Examine Activity 12.6. Adjust the number of tight turns n from 1 to 20 to verify that the magnetic field produced by a circular coil scales linearly as $B_{net} = n \\cdot B_1$ due to constructive vector addition.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Number of Turns (n):</span>
                        <input type="range" id="sim9_n_slider" min="1" max="20" value="5" step="1" oninput="sim9Update()" class="w-28 accent-amber-500">
                        <span id="sim9_n_txt" class="text-amber-400 font-mono font-bold">5 Turns</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current I (A):</span>
                        <input type="range" id="sim9_i_slider" min="0.5" max="4.0" value="2.0" step="0.5" oninput="sim9Update()" class="w-20 accent-amber-500">
                        <span id="sim9_i_txt" class="text-teal-400 font-mono font-bold">2.0 A</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim9_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Central Field B</div>
                        <div id="sim9_val_btot" class="text-amber-400 font-bold text-sm">6.28 × 10⁻⁵ T</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Single Turn Field B₁</div>
                        <div id="sim9_val_b1" class="text-teal-400 font-bold text-sm">1.26 × 10⁻⁵ T</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Turn Multiplier Factor</div>
                        <div id="sim9_val_mult" class="text-cyan-400 font-bold text-sm">5× Amplification</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Current In Each Turn</div>
                        <div id="sim9_val_sense" class="text-emerald-400 font-bold text-sm">Identical Circulation</div>
                    </div>
                </div>
            </div>
        """
    },
    10: {
        "title": "Solenoid Uniform Field Studio",
        "description": "Interact with Figure 12.10. Observe how the magnetic field of a cylindrical helical solenoid mimics a permanent bar magnet outside, while maintaining perfectly straight, parallel, uniform field lines inside.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current Sense:</span>
                        <button id="sim10_btn_toggle" onclick="sim10ToggleCurrent()" class="px-3 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Left: North / Right: South</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Turn Density (N/L):</span>
                        <input type="range" id="sim10_density_slider" min="6" max="18" value="12" step="2" oninput="sim10Update()" class="w-24 accent-amber-500">
                        <span id="sim10_density_txt" class="text-amber-400 font-mono font-bold">12 Turns</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim10_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Internal Core Field</div>
                        <div id="sim10_val_internal" class="text-amber-400 font-bold text-sm">Completely Uniform (Straight)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Internal Line Direction</div>
                        <div id="sim10_val_intdir" class="text-teal-400 font-bold text-sm">South → North (Right to Left)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">External Field Analogy</div>
                        <div id="sim10_val_analogy" class="text-cyan-400 font-bold text-sm">Permanent Bar Magnet</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Solenoid Formula</div>
                        <div id="sim10_val_formula" class="text-emerald-400 font-bold text-sm">B = μ₀ · n · I</div>
                    </div>
                </div>
            </div>
        """
    },
    11: {
        "title": "Electromagnet Soft Iron Core Inducer",
        "description": "Simulate Figure 12.11. Insert a soft iron rod into the solenoid to align ferromagnetic domains and amplify magnetic strength, demonstrating instant demagnetization upon opening the switch.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Core Material:</span>
                        <select id="sim11_core_select" onchange="sim11Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="soft_iron" selected>Soft Iron Core (High μ, Zero Retentivity)</option>
                            <option value="air">Air Core (Hollow Solenoid)</option>
                            <option value="steel">Hard Carbon Steel (Permanent Retentivity)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim11_btn_power" onclick="sim11TogglePower()" class="px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold">Power: ENERGIZED</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim11_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Magnetic Amplification</div>
                        <div id="sim11_val_amp" class="text-amber-400 font-bold text-sm">800× Core Boost</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Residual Magnetism</div>
                        <div id="sim11_val_resid" class="text-teal-400 font-bold text-sm">Zero (Instant Demagnetize)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Lifting Capacity</div>
                        <div id="sim11_val_lift" class="text-cyan-400 font-bold text-sm">45 Steel Pins Held</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Typical Applications</div>
                        <div id="sim11_val_app" class="text-emerald-400 font-bold text-sm">Cranes, Relays & Bells</div>
                    </div>
                </div>
            </div>
        """
    },
    12: {
        "title": "Kicking Aluminium Rod Experiment",
        "description": "Replicate Activity 12.7. Suspend a conducting aluminium rod between horseshoe magnet poles. Toggle current and magnetic field polarities to observe mechanical kick deflections.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current in Rod:</span>
                        <button id="sim12_btn_curr" onclick="sim12ToggleCurrent()" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">B → A (Forward)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Magnet Poles:</span>
                        <button id="sim12_btn_mag" onclick="sim12ToggleMagnet()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Bottom N / Top S (Upward B)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Angle θ:</span>
                        <input type="range" id="sim12_theta_slider" min="0" max="90" value="90" step="15" oninput="sim12Update()" class="w-16 accent-amber-500">
                        <span id="sim12_theta_txt" class="text-teal-400 font-mono font-bold">90°</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim12_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Mechanical Force Direction</div>
                        <div id="sim12_val_force" class="text-amber-400 font-bold text-sm">Displaces to the LEFT</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Force Scaling (sin θ)</div>
                        <div id="sim12_val_scaling" class="text-teal-400 font-bold text-sm">100% Maximum at 90°</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Governing Principle</div>
                        <div id="sim12_val_principle" class="text-cyan-400 font-bold text-sm">Ampere's Reciprocal Force</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Parallel Angle (0°) Force</div>
                        <div id="sim12_val_zero" class="text-emerald-400 font-bold text-sm">Exactly Zero Force</div>
                    </div>
                </div>
            </div>
        """
    },
    13: {
        "title": "Fleming's Left-Hand Rule Workbench",
        "description": "Master Figure 12.13 and solve Example 12.2. Align mutually perpendicular vectors: Forefinger (Field), Middle Finger (Current), and Thumb (Motion/Force) to predict charged particle deflections.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Scenario:</span>
                        <select id="sim13_scenario_select" onchange="sim13Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="ex12_2" selected>Example 12.2: Electron Beam (Velocity Right, Field Down)</option>
                            <option value="proton">Exercise Q2: Proton Beam (Velocity East, Deflected North)</option>
                            <option value="motor">Electric Motor Arm: Coil Current Forward, Field Right</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim13FireParticle()" class="px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Fire Particle Beam 🚀</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim13_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Forefinger (Magnetic Field)</div>
                        <div id="sim13_val_b" class="text-amber-400 font-bold text-sm">Vertically Downward (↓)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Middle Finger (Current)</div>
                        <div id="sim13_val_i" class="text-teal-400 font-bold text-sm">Horizontally Left (←)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Thumb (Resulting Force)</div>
                        <div id="sim13_val_f" class="text-cyan-400 font-bold text-sm">Into the Page (⊗)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Physical Devices</div>
                        <div id="sim13_val_device" class="text-emerald-400 font-bold text-sm">Electric Motors & Loudspeakers</div>
                    </div>
                </div>
            </div>
        """
    },
    14: {
        "title": "Biomagnetism & Diagnostic MRI Studio",
        "description": "Explore the medical science behind Section 12.3. Observe how microscopic ionic currents along heart and brain neurons generate biomagnetic fields ($10^{-9}$ Earth field) for MRI diagnostics.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Target Organ:</span>
                        <button id="sim14_btn_brain" onclick="sim14SetOrgan('brain')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Human Brain (Neural)</button>
                        <button id="sim14_btn_heart" onclick="sim14SetOrgan('heart')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Human Heart (Cardiac)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim14_btn_rf" onclick="sim14PulseRF()" class="px-2.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold">Apply RF Pulse (MRI Scan)</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim14_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Biomagnetic Field Magnitude</div>
                        <div id="sim14_val_mag" class="text-amber-400 font-bold text-sm">~10⁻¹³ T (10⁻⁹ of Earth)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Biochemical Source</div>
                        <div id="sim14_val_source" class="text-teal-400 font-bold text-sm">Na⁺ / K⁺ / Ca²⁺ Ionic Nerve Drift</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Target Nuclei in MRI</div>
                        <div id="sim14_val_nuclei" class="text-cyan-400 font-bold text-sm">Water Hydrogen Protons</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Radiation Safety</div>
                        <div id="sim14_val_safety" class="text-emerald-400 font-bold text-sm">Zero Ionizing Radiation</div>
                    </div>
                </div>
            </div>
        """
    },
    15: {
        "title": "Domestic 220V AC Electrical Installation",
        "description": "Inspect Figure 12.15. Trace Red Live (220V), Black Neutral (0V), and Green Earth wires supplying parallel 15A high-power and 5A lighting circuits with independent branch switches.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Toggle Appliances:</span>
                        <button id="sim15_btn_lamp" onclick="sim15ToggleLoad('lamp')" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">5A Lamp: ON</button>
                        <button id="sim15_btn_fan" onclick="sim15ToggleLoad('fan')" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">5A Fan: ON</button>
                        <button id="sim15_btn_geyser" onclick="sim15ToggleLoad('geyser')" class="px-2 py-0.5 rounded bg-emerald-700 text-white text-[11px] font-bold">15A Geyser: ON</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Main Switch:</span>
                        <button id="sim15_btn_main" onclick="sim15ToggleMain()" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold">Main: CLOSED</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim15_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Supply Voltage across Loads</div>
                        <div id="sim15_val_voltage" class="text-amber-400 font-bold text-sm">Uniform 220 V AC (50 Hz)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Current Drawn</div>
                        <div id="sim15_val_current" class="text-teal-400 font-bold text-sm">10.45 A (Normal Load)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Wire Color Code</div>
                        <div id="sim15_val_color" class="text-cyan-400 font-bold text-sm">Red Live / Black Neutral / Green Earth</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Wiring Topology</div>
                        <div id="sim15_val_top" class="text-emerald-400 font-bold text-sm">Independent Parallel Branches</div>
                    </div>
                </div>
            </div>
        """
    },
    16: {
        "title": "Earth Wire & Fuse Safety Meltdown Lab",
        "description": "Simulate domestic faults. Contrast shock prevention via the earth wire against hazardous live chassis exposure, and trigger a short-circuit current surge to watch the fuse melt.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Earth Wire Connection:</span>
                        <button id="sim16_btn_earth" onclick="sim16ToggleEarth()" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold">Earth Connected (Safe)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Simulate Fault:</span>
                        <button id="sim16_btn_leak" onclick="sim16SimulateInsulationLeak()" class="px-2.5 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Casing Leakage</button>
                        <button id="sim16_btn_short" onclick="sim16TriggerShortCircuit()" class="px-2.5 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold">Short-Circuit</button>
                        <button onclick="sim16ResetSystem()" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Reset</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim16_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Appliance Chassis Potential</div>
                        <div id="sim16_val_chassis" class="text-emerald-400 font-bold text-sm">0 V (Discharged into Earth)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Safety Fuse State</div>
                        <div id="sim16_val_fuse" class="text-amber-400 font-bold text-sm">Conducting Intact</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">User Shock Status</div>
                        <div id="sim16_val_shock" class="text-cyan-400 font-bold text-sm">Zero Shock Risk (Safe)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Protection Mechanism</div>
                        <div id="sim16_val_prot" class="text-emerald-400 font-bold text-sm">Low-R Earth Path + Joule Fuse</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch12_sims_part2.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part2, f, indent=2, ensure_ascii=False)

print("Saved .agents/c10s_ch12_sims_part2.json successfully!")

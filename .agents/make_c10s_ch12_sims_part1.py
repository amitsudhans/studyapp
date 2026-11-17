# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 12: Simulators 1 to 8 HTML Templates
Magnetic Effects of Electric Current
"""

import json

simulators_part1 = {
    1: {
        "title": "Oersted Compass Deflection Lab",
        "description": "Replicate Hans Christian Oersted's historic 1820 experiment (Activity 12.1). Toggle electric current through a straight thick copper wire and observe compass needle deflection caused by the magnetic field.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Circuit Switch:</span>
                        <button id="sim1_btn_switch" onclick="sim1ToggleSwitch()" class="px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold">Current: ON (Closed)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current I (A):</span>
                        <input type="range" id="sim1_i_slider" min="0.5" max="5.0" value="2.5" step="0.5" oninput="sim1Update()" class="w-24 accent-amber-500">
                        <span id="sim1_i_txt" class="text-amber-400 font-mono font-bold">2.5 A</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Wire Distance:</span>
                        <input type="range" id="sim1_d_slider" min="15" max="60" value="25" step="5" oninput="sim1Update()" class="w-20 accent-amber-500">
                        <span id="sim1_d_txt" class="text-teal-400 font-mono font-bold">25 mm</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim1_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Compass Deflection (θ)</div>
                        <div id="sim1_val_angle" class="text-amber-400 font-bold text-sm">38.5° East</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Magnetic Field at Needle</div>
                        <div id="sim1_val_b" class="text-teal-400 font-bold text-sm">2.00 × 10⁻⁵ T</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Discovered By</div>
                        <div id="sim1_val_scientist" class="text-cyan-400 font-bold text-sm">H. C. Oersted (1820)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Physical Deduction</div>
                        <div id="sim1_val_deduction" class="text-emerald-400 font-bold text-sm">Current generates B-field</div>
                    </div>
                </div>
            </div>
        """
    },
    2: {
        "title": "Bar Magnet & Iron Filings Pattern",
        "description": "Simulate Activity 12.2. Sprinkle iron filings over cardboard surrounding a bar magnet and tap the sheet to observe induced magnetic dipoles organizing into continuous curved lines.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <button id="sim2_btn_tap" onclick="sim2TapBoard()" class="px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Tap Cardboard 👆</button>
                        <button onclick="sim2ResetFilings()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Resprinkle Filings</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Magnet Pole Strength:</span>
                        <input type="range" id="sim2_str_slider" min="1" max="5" value="3" step="1" oninput="sim2Update()" class="w-24 accent-amber-500">
                        <span id="sim2_str_txt" class="text-amber-400 font-mono font-bold">Medium (3×)</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim2_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Alignment Order</div>
                        <div id="sim2_val_order" class="text-amber-400 font-bold text-sm">85% Aligned</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Line Density Peak</div>
                        <div id="sim2_val_peak" class="text-teal-400 font-bold text-sm">Maximum at N & S Poles</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Filing Mechanism</div>
                        <div id="sim2_val_mech" class="text-cyan-400 font-bold text-sm">Induced Dipole Alignment</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Field Representation</div>
                        <div id="sim2_val_rep" class="text-emerald-400 font-bold text-sm">Continuous Lines of Force</div>
                    </div>
                </div>
            </div>
        """
    },
    3: {
        "title": "Compass Step-by-Step Field Line Tracer",
        "description": "Step through Activity 12.3 with a plotting compass. Advance step-by-step from the North pole to mark pencil dots and trace continuous closed loops ending at the South pole.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <button onclick="sim3StepForward()" class="px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Step Compass Next →</button>
                        <button onclick="sim3ResetTracing()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Reset Tracer</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Select Starting Trajectory:</span>
                        <select id="sim3_line_select" onchange="sim3ChangeLine()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="1">Line 1 (Upper Tight Loop)</option>
                            <option value="2" selected>Line 2 (Central Wide Loop)</option>
                            <option value="3">Line 3 (Lower Tight Loop)</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim3_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Tracer Progress</div>
                        <div id="sim3_val_progress" class="text-amber-400 font-bold text-sm">Step 4 / 8</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">External Direction</div>
                        <div id="sim3_val_ext" class="text-teal-400 font-bold text-sm">North → South</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Internal Direction</div>
                        <div id="sim3_val_int" class="text-cyan-400 font-bold text-sm">South → North</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Loop Characteristic</div>
                        <div id="sim3_val_loop" class="text-emerald-400 font-bold text-sm">Continuous Closed Curve</div>
                    </div>
                </div>
            </div>
        """
    },
    4: {
        "title": "Magnetic Field Vector & Non-Intersection Proof",
        "description": "Inspect field line properties in real time. Drag an inspection probe across space to examine local field tangent vectors and test why two lines cannot cross.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Probe Position X:</span>
                        <input type="range" id="sim4_px_slider" min="50" max="550" value="280" step="10" oninput="sim4Update()" class="w-24 accent-amber-500">
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Probe Position Y:</span>
                        <input type="range" id="sim4_py_slider" min="30" max="230" value="65" step="10" oninput="sim4Update()" class="w-24 accent-amber-500">
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim4_btn_intersect" onclick="sim4TestIntersection()" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold">Simulate Intersection Paradox</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim4_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Field Magnitude (Crowding)</div>
                        <div id="sim4_val_mag" class="text-amber-400 font-bold text-sm">Moderate (0.35 T)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Tangent Direction Angle</div>
                        <div id="sim4_val_angle" class="text-teal-400 font-bold text-sm">142° (Unique Vector)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Non-Intersection Law</div>
                        <div id="sim4_val_intersect" class="text-cyan-400 font-bold text-sm">Strictly Separate Lines</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Physical Reason</div>
                        <div id="sim4_val_reason" class="text-emerald-400 font-bold text-sm">Needle cannot point twice</div>
                    </div>
                </div>
            </div>
        """
    },
    5: {
        "title": "Current Reversal & Polarity Deflection Lab",
        "subtitle": "Activity 12.4 Current Direction vs Magnetic Orientation",
        "description": "Simulate Activity 12.4. Flip battery polarity to reverse electric current between North-to-South and South-to-North, observing how compass needle deflection reverses between East and West.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current Direction:</span>
                        <button id="sim5_btn_n_s" onclick="sim5SetDirection('N_S')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">North → South</button>
                        <button id="sim5_btn_s_n" onclick="sim5SetDirection('S_N')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">South → North</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Circuit State:</span>
                        <button id="sim5_btn_key" onclick="sim5ToggleKey()" class="px-3 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold">Key Closed</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim5_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Current Flow Direction</div>
                        <div id="sim5_val_flow" class="text-amber-400 font-bold text-sm">North to South</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">North Pole Deflection</div>
                        <div id="sim5_val_deflect" class="text-teal-400 font-bold text-sm">Deflects toward EAST</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Governing Rule</div>
                        <div id="sim5_val_rule" class="text-cyan-400 font-bold text-sm">SNOW / Right-Hand Rule</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Polarity Relationship</div>
                        <div id="sim5_val_rel" class="text-emerald-400 font-bold text-sm">Field flips with Current</div>
                    </div>
                </div>
            </div>
        """
    },
    6: {
        "title": "Straight Wire Concentric Rings Field",
        "description": "Experiment with Activity 12.5. Adjust current magnitude I and compass radial distance r from a vertical wire to verify the fundamental law $B \\propto I / r$ with concentric circle patterns.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current I (A):</span>
                        <input type="range" id="sim6_i_slider" min="1" max="10" value="4" step="1" oninput="sim6Update()" class="w-24 accent-amber-500">
                        <span id="sim6_i_txt" class="text-amber-400 font-mono font-bold">4.0 A</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Radial Distance r (cm):</span>
                        <input type="range" id="sim6_r_slider" min="1" max="8" value="3" step="0.5" oninput="sim6Update()" class="w-24 accent-amber-500">
                        <span id="sim6_r_txt" class="text-teal-400 font-mono font-bold">3.0 cm</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim6_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Field Strength B</div>
                        <div id="sim6_val_b" class="text-amber-400 font-bold text-sm">2.67 × 10⁻⁵ T</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Current Proportionality</div>
                        <div id="sim6_val_iprop" class="text-teal-400 font-bold text-sm">B ∝ I (Direct)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Distance Proportionality</div>
                        <div id="sim6_val_rprop" class="text-cyan-400 font-bold text-sm">B ∝ 1/r (Inverse)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Line Geometry</div>
                        <div id="sim6_val_geom" class="text-emerald-400 font-bold text-sm">Concentric Circles</div>
                    </div>
                </div>
            </div>
        """
    },
    7: {
        "title": "Right-Hand Thumb Rule 3D Visualizer",
        "description": "Visualize the Right-Hand Thumb Rule and Maxwell's corkscrew rule. Test NCERT Example 12.1 for an East-to-West power line to view circulating field lines from East and West observer perspectives.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current Flow:</span>
                        <select id="sim7_dir_select" onchange="sim7Update()" class="bg-slate-800 text-slate-200 px-2 py-1 rounded border border-slate-700">
                            <option value="E_W" selected>Example 12.1: East → West</option>
                            <option value="W_E">West → East</option>
                            <option value="UP">Vertical UP (Out of page)</option>
                            <option value="DOWN">Vertical DOWN (Into page)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Observer Perspective:</span>
                        <button id="sim7_btn_east" onclick="sim7SetView('east')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">View from East</button>
                        <button id="sim7_btn_west" onclick="sim7SetView('west')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">View from West</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim7_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apparent Circulation</div>
                        <div id="sim7_val_circ" class="text-amber-400 font-bold text-sm">Clockwise</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Field Directly Below Wire</div>
                        <div id="sim7_val_below" class="text-teal-400 font-bold text-sm">Points toward NORTH</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Field Directly Above Wire</div>
                        <div id="sim7_val_above" class="text-cyan-400 font-bold text-sm">Points toward SOUTH</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Equivalent Analogy</div>
                        <div id="sim7_val_analogy" class="text-emerald-400 font-bold text-sm">Maxwell's Corkscrew</div>
                    </div>
                </div>
            </div>
        """
    },
    8: {
        "title": "Circular Loop Magnetic Field",
        "description": "Inspect Figures 12.8 & 12.9. Observe how concentric circular field lines around loop segments expand radially with distance and straighten into parallel lines at the center.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Loop Current Sense:</span>
                        <button id="sim8_btn_cw" onclick="sim8SetSense('cw')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Clockwise (South Face)</button>
                        <button id="sim8_btn_ccw" onclick="sim8SetSense('ccw')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Counter-Clockwise (North Face)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current I:</span>
                        <input type="range" id="sim8_i_slider" min="1" max="6" value="3" step="1" oninput="sim8Update()" class="w-20 accent-amber-500">
                        <span id="sim8_i_txt" class="text-amber-400 font-mono font-bold">3 A</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim8_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Center Field Geometry</div>
                        <div id="sim8_val_center" class="text-amber-400 font-bold text-sm">Straight & Parallel</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Center Field Direction</div>
                        <div id="sim8_val_dir" class="text-teal-400 font-bold text-sm">Into the Screen</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Magnetic Polarity of Face</div>
                        <div id="sim8_val_pole" class="text-cyan-400 font-bold text-sm">South Pole (Clock rule)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">All Segments Contribution</div>
                        <div id="sim8_val_contrib" class="text-emerald-400 font-bold text-sm">Constructive Superposition</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch12_sims_part1.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part1, f, indent=2, ensure_ascii=False)

print("Saved .agents/c10s_ch12_sims_part1.json successfully!")

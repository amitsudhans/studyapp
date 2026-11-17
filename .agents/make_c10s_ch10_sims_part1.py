# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 10: Simulators 1 to 8 HTML Templates
"""

import json

simulators_part1 = {
    1: {
        "title": "Eye vs Camera Optics Studio",
        "description": "Compare biological ocular vision with mechanical camera optics. Observe how light rays refract through the cornea and crystalline lens to form a real, inverted image on the retinal screen.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Mode:</span>
                        <button id="sim1_btn_eye" onclick="sim1SetMode('eye')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Human Eye</button>
                        <button id="sim1_btn_cam" onclick="sim1SetMode('camera')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Optical Camera</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Illumination:</span>
                        <input type="range" id="sim1_light_slider" min="20" max="100" value="70" oninput="sim1Update()" class="w-24 accent-amber-500">
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim1_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Front Refractor</div>
                        <div id="sim1_val_front" class="text-amber-400 font-bold">Cornea (n=1.376)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Aperture Control</div>
                        <div id="sim1_val_aperture" class="text-teal-400 font-bold">Iris & Pupil</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Focusing Element</div>
                        <div id="sim1_val_lens" class="text-cyan-400 font-bold">Crystalline Lens</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Image Screen</div>
                        <div id="sim1_val_screen" class="text-emerald-400 font-bold">Retina (Real, Inverted)</div>
                    </div>
                </div>
            </div>
        """
    },
    2: {
        "title": "Anatomy & Pupillary Light Reflex Studio",
        "description": "Interact with a cross-section of the human eyeball (diameter 2.3 cm). Adjust ambient ambient lighting to observe the pupillary reflex governed by the iris diaphragm.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Ambient Lighting:</span>
                        <input type="range" id="sim2_lux_slider" min="10" max="100" value="50" oninput="sim2Update()" class="w-32 accent-amber-500">
                        <span id="sim2_lux_txt" class="text-amber-400 font-mono font-bold">50% (Normal)</span>
                    </div>
                    <button onclick="sim2ToggleLabels()" id="sim2_btn_lbl" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Hide Anatomical Labels</button>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim2_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Pupil Diameter</div>
                        <div id="sim2_pupil_diam" class="text-amber-400 font-mono font-bold">4.0 mm</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Iris Muscle State</div>
                        <div id="sim2_muscle_state" class="text-teal-400 font-bold">Balanced Tone</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Retinal Flux</div>
                        <div id="sim2_flux_txt" class="text-cyan-400 font-mono font-bold">Optimal Safe</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Eyeball Metric</div>
                        <div class="text-emerald-400 font-bold">2.3 cm Spherical</div>
                    </div>
                </div>
            </div>
        """
    },
    3: {
        "title": "Retina Photoreceptor Transducer Studio",
        "description": "Explore the cellular architecture of the retina. Compare night-vision Rod cells (~120M) with daylight color-vision Cone cells (~6M) and observe signal transduction into the optic nerve.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-700 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Illumination Level:</span>
                        <button id="sim3_btn_dim" onclick="sim3SetMode('dim')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Dim Light (Rods)</button>
                        <button id="sim3_btn_bright" onclick="sim3SetMode('bright')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Bright Daylight (Cones)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Color Filter:</span>
                        <select id="sim3_color_select" onchange="sim3Update()" class="bg-slate-900 text-amber-400 px-2 py-0.5 rounded border border-slate-700">
                            <option value="white">White Sunlight</option>
                            <option value="red">Red (650 nm)</option>
                            <option value="green">Green (530 nm)</option>
                            <option value="blue">Blue (450 nm)</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim3_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Active Receptors</div>
                        <div id="sim3_active_type" class="text-amber-400 font-bold">Cone Photoreceptors</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Acuity & Color</div>
                        <div id="sim3_perception_txt" class="text-teal-400 font-bold">Trichromatic High Acuity</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Electrical Potential</div>
                        <div id="sim3_potential_txt" class="text-cyan-400 font-mono font-bold">-40 mV (Transduced)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Optic Nerve Output</div>
                        <div id="sim3_nerve_output" class="text-emerald-400 font-bold">Neural Spike Stream</div>
                    </div>
                </div>
            </div>
        """
    },
    4: {
        "title": "Power of Accommodation Studio",
        "description": "Adjust the target object distance from infinity down to 10 cm. Watch ciliary muscles contract to increase crystalline lens curvature, and detect the onset of eyestrain below 25 cm.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Object Distance (u):</span>
                        <input type="range" id="sim4_dist_slider" min="10" max="300" value="100" oninput="sim4Update()" class="w-36 accent-amber-500">
                        <span id="sim4_dist_txt" class="text-amber-400 font-mono font-bold">100 cm</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <button onclick="sim4SetDist(300)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:text-white">Infinity</button>
                        <button onclick="sim4SetDist(25)" class="px-2 py-0.5 rounded bg-slate-800 text-amber-400 font-bold hover:text-amber-300">Near Point (25 cm)</button>
                        <button onclick="sim4SetDist(12)" class="px-2 py-0.5 rounded bg-slate-800 text-rose-400 hover:text-rose-300">Strain (&lt;25 cm)</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim4_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ciliary Muscle State</div>
                        <div id="sim4_muscle_txt" class="text-amber-400 font-bold">Partially Contracted</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Lens Curvature</div>
                        <div id="sim4_lens_thick" class="text-teal-400 font-bold">Moderate Bulge</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Focal Length (f)</div>
                        <div id="sim4_focal_txt" class="text-cyan-400 font-mono font-bold">2.21 cm</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Retinal Focus Status</div>
                        <div id="sim4_focus_status" class="text-emerald-400 font-bold">Sharp Focus</div>
                    </div>
                </div>
            </div>
        """
    },
    5: {
        "title": "Myopia Optics & Concave Lens Correction Studio",
        "description": "Simulate near-sightedness caused by eyeball elongation or excessive corneal curvature. Observe rays focusing before the retina, and insert a corrective concave lens to restore sharp focus.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Myopic Far Point (d):</span>
                        <input type="range" id="sim5_fp_slider" min="50" max="250" value="100" oninput="sim5Update()" class="w-28 accent-amber-500">
                        <span id="sim5_fp_txt" class="text-amber-400 font-mono font-bold">100 cm</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim5_toggle_lens" onclick="sim5ToggleCorrection()" class="px-3 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Apply Concave Lens</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim5_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Convergence Point</div>
                        <div id="sim5_conv_txt" class="text-rose-400 font-bold">In Front of Retina</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Corrective Lens Type</div>
                        <div id="sim5_lens_type" class="text-teal-400 font-bold">Diverging Concave</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Required Power (P)</div>
                        <div id="sim5_power_txt" class="text-cyan-400 font-mono font-bold">-1.00 D</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Vision Acuity</div>
                        <div id="sim5_acuity_txt" class="text-amber-400 font-bold">Blurred Distance</div>
                    </div>
                </div>
            </div>
        """
    },
    6: {
        "title": "Hypermetropia Optics & Convex Lens Correction Studio",
        "description": "Simulate far-sightedness caused by a short eyeball or insufficient lens curvature. Rays converge behind the retina; insert a convex spectacle lens to bring the focal point forward onto the retina.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Receded Near Point (d'):</span>
                        <input type="range" id="sim6_np_slider" min="35" max="150" value="75" oninput="sim6Update()" class="w-28 accent-amber-500">
                        <span id="sim6_np_txt" class="text-amber-400 font-mono font-bold">75 cm</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim6_toggle_lens" onclick="sim6ToggleCorrection()" class="px-3 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Apply Convex Lens</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim6_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Uncorrected Focus</div>
                        <div id="sim6_conv_txt" class="text-rose-400 font-bold">Behind Retina</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Corrective Lens Type</div>
                        <div id="sim6_lens_type" class="text-teal-400 font-bold">Converging Convex</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Required Power (P)</div>
                        <div id="sim6_power_txt" class="text-cyan-400 font-mono font-bold">+2.67 D</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Reading Vision (25 cm)</div>
                        <div id="sim6_acuity_txt" class="text-amber-400 font-bold">Uncorrected Blurry</div>
                    </div>
                </div>
            </div>
        """
    },
    7: {
        "title": "Presbyopia & Bi-Focal Spectacle Studio",
        "description": "Examine age-related loss of accommodation and bi-focal lens optics. Switch between straight-ahead distant viewing (upper concave segment) and downward reading gaze (lower convex segment).",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Gaze Direction:</span>
                        <button id="sim7_btn_dist" onclick="sim7SetGaze('distance')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Straight Ahead (Distance)</button>
                        <button id="sim7_btn_near" onclick="sim7SetGaze('reading')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Downward (Reading)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Patient Age:</span>
                        <input type="range" id="sim7_age_slider" min="40" max="75" value="55" oninput="sim7Update()" class="w-24 accent-amber-500">
                        <span id="sim7_age_txt" class="text-amber-400 font-mono font-bold">55 yrs</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim7_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Active Bi-Focal Zone</div>
                        <div id="sim7_zone_txt" class="text-amber-400 font-bold">Upper Concave Segment</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ciliary Muscle Tone</div>
                        <div id="sim7_muscle_txt" class="text-teal-400 font-bold">Weakened Elasticity</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Lens Power Prescribed</div>
                        <div id="sim7_rx_txt" class="text-cyan-400 font-mono font-bold">-1.50 D / +2.00 D</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Corneal Graft Window</div>
                        <div class="text-emerald-400 font-bold">4 to 6 hrs post-mortem</div>
                    </div>
                </div>
            </div>
        """
    },
    8: {
        "title": "Prism Refraction & Deviation Goniometer",
        "description": "Trace monochromatic light through a triangular glass prism. Vary the prism angle (A) and angle of incidence (i) to measure angles of refraction, emergence (e), and deviation (D).",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Angle of Incidence (i):</span>
                        <input type="range" id="sim8_i_slider" min="25" max="75" value="48" oninput="sim8Update()" class="w-28 accent-amber-500">
                        <span id="sim8_i_txt" class="text-amber-400 font-mono font-bold">48°</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Prism Angle (A):</span>
                        <input type="range" id="sim8_a_slider" min="45" max="75" value="60" oninput="sim8Update()" class="w-24 accent-amber-500">
                        <span id="sim8_a_txt" class="text-cyan-400 font-mono font-bold">60°</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim8_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Angle of Emergence (e)</div>
                        <div id="sim8_e_txt" class="text-teal-400 font-mono font-bold">48.2°</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Angle of Deviation (D)</div>
                        <div id="sim8_d_txt" class="text-amber-400 font-mono font-bold">36.2°</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Sum Formula Check</div>
                        <div id="sim8_sum_txt" class="text-cyan-400 font-mono font-bold">i + e = A + D</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Refractive Index (n)</div>
                        <div class="text-emerald-400 font-mono font-bold">1.50 (Crown Glass)</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch10_sims_part1.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part1, f, indent=2)

print(f"Generated {len(simulators_part1)} simulator templates in Part 1.")

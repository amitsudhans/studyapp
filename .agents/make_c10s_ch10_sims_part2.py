# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 10: Simulators 9 to 16 HTML Templates
"""

import json

simulators_part2 = {
    9: {
        "title": "Prism Dispersion & VIBGYOR Spectrum Studio",
        "description": "Send a white sunlight beam through an optical prism (Activity 10.2). Observe how differential refractive indices fan out the beam into the 7 distinct spectral colors of VIBGYOR.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Light Source:</span>
                        <button id="sim9_btn_white" onclick="sim9SetSource('white')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">White Sunlight</button>
                        <button id="sim9_btn_mono" onclick="sim9SetSource('mono')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Monochromatic (Laser)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Beam Width:</span>
                        <input type="range" id="sim9_width_slider" min="2" max="15" value="6" oninput="sim9Update()" class="w-24 accent-amber-500">
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim9_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Least Deviated Color</div>
                        <div class="text-rose-400 font-bold">Red (λ ≈ 700 nm, v_max)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Most Deviated Color</div>
                        <div class="text-purple-400 font-bold">Violet (λ ≈ 400 nm, v_min)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Angular Dispersion</div>
                        <div id="sim9_disp_txt" class="text-cyan-400 font-mono font-bold">Δθ ≈ 1.85°</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-800/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Spectral Sequence</div>
                        <div class="text-amber-300 font-bold tracking-wider">V-I-B-G-Y-O-R</div>
                    </div>
                </div>
            </div>
        """
    },
    10: {
        "title": "Newton Recombination Apparatus Studio",
        "description": "Recreate Isaac Newton's two-prism experiment (Figure 10.6). Toggle the second inverted identical prism to observe dispersed VIBGYOR rays recombining into a beam of pure white light.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Second Prism (P2):</span>
                        <button id="sim10_toggle_p2" onclick="sim10ToggleP2()" class="px-3 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Inverted P2 Active</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Prism Separation:</span>
                        <input type="range" id="sim10_sep_slider" min="40" max="150" value="80" oninput="sim10Update()" class="w-28 accent-amber-500">
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim10_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Prism 1 Action</div>
                        <div class="text-teal-400 font-bold">Dispersion (White → VIBGYOR)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Prism 2 Action</div>
                        <div id="sim10_p2_action" class="text-amber-400 font-bold">Equal & Opposite Recombination</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Emergent Screen Beam</div>
                        <div id="sim10_screen_txt" class="text-cyan-400 font-bold">Pure White Sunlight</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Physical Proof</div>
                        <div class="text-emerald-400 font-bold">Sunlight is 7-Color Blend</div>
                    </div>
                </div>
            </div>
        """
    },
    11: {
        "title": "Rainbow Droplet Internal Optics Studio",
        "description": "Trace sunlight entering a spherical water droplet (Figure 10.8). Step through the three optical stages: front refraction/dispersion, back internal reflection, and emergence refraction at 40° to 42°.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Ray Tracing Stage:</span>
                        <button id="sim11_btn_all" onclick="sim11SetStage('all')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Full Sequence</button>
                        <button id="sim11_btn_1" onclick="sim11SetStage('1')" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">1. Refract/Disperse</button>
                        <button id="sim11_btn_2" onclick="sim11SetStage('2')" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">2. Internal Reflect</button>
                        <button id="sim11_btn_3" onclick="sim11SetStage('3')" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300">3. Emerge</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim11_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Red Light Emergence</div>
                        <div class="text-rose-400 font-mono font-bold">42.0° (Outer Arc)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Violet Emergence</div>
                        <div class="text-purple-400 font-mono font-bold">40.2° (Inner Arc)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Back Wall Physics</div>
                        <div class="text-cyan-400 font-bold">Total Internal Reflection (&gt;48.6°)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Observer Geometry</div>
                        <div class="text-emerald-400 font-bold">Sun at Back, Rain Ahead</div>
                    </div>
                </div>
            </div>
        """
    },
    12: {
        "title": "Atmospheric Refraction Gradient Studio",
        "description": "Visualize light propagating downward through atmospheric layers of increasing density. Observe how continuous refraction towards the normal curves light trajectories into downward-concave arcs.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Incident Angle (θ):</span>
                        <input type="range" id="sim12_angle_slider" min="15" max="75" value="45" oninput="sim12Update()" class="w-28 accent-amber-500">
                        <span id="sim12_angle_txt" class="text-amber-400 font-mono font-bold">45°</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Atmosphere:</span>
                        <button id="sim12_toggle_atm" onclick="sim12ToggleAtmosphere()" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Normal Atmosphere</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim12_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Upper Atmosphere (Vacuum)</div>
                        <div class="text-teal-400 font-mono font-bold">n = 1.00000</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Sea-Level Surface Air</div>
                        <div class="text-cyan-400 font-mono font-bold">n ≈ 1.00029</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ray Path Geometry</div>
                        <div id="sim12_path_txt" class="text-amber-400 font-bold">Curved Downward Arc</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apparent Shift</div>
                        <div class="text-emerald-400 font-bold">Shifted Toward Zenith</div>
                    </div>
                </div>
            </div>
        """
    },
    13: {
        "title": "Star Twinkling vs Planet Optics Studio",
        "description": "Simulate starlight from a point source traversing turbulent air eddies versus light from a nearby planet (extended source). See why stars twinkle while planetary brightness stays constant.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Source Selection:</span>
                        <button id="sim13_btn_star" onclick="sim13SetSource('star')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Distant Star (Point Source)</button>
                        <button id="sim13_btn_planet" onclick="sim13SetSource('planet')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Planet (Extended Disk)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Turbulence:</span>
                        <input type="range" id="sim13_turb_slider" min="1" max="10" value="5" oninput="sim13Update()" class="w-24 accent-amber-500">
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim13_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Source Geometry</div>
                        <div id="sim13_geo_txt" class="text-amber-400 font-bold">Sub-Microscopic Point</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apparent Position</div>
                        <div id="sim13_pos_txt" class="text-teal-400 font-bold">Slightly Elevated & Fluctuating</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Luminous Intensity</div>
                        <div id="sim13_lum_txt" class="text-cyan-400 font-mono font-bold">Twinkling Rapidly</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Averaging Effect</div>
                        <div id="sim13_avg_txt" class="text-emerald-400 font-bold">No Cancellation (Single Ray)</div>
                    </div>
                </div>
            </div>
        """
    },
    14: {
        "title": "Advanced Sunrise & Delayed Sunset Studio",
        "description": "Simulate solar rays grazing Earth's horizon (Figure 10.10). Atmospheric refraction bends rays when the Sun is 0.5° below the horizon, extending perceived daily daylight by ~4 minutes.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Actual Solar Elevation:</span>
                        <input type="range" id="sim14_elev_slider" min="-20" max="20" value="-5" oninput="sim14Update()" class="w-32 accent-amber-500">
                        <span id="sim14_elev_txt" class="text-amber-400 font-mono font-bold">-0.5° (Below Horizon)</span>
                    </div>
                    <button id="sim14_toggle_anim" onclick="sim14ToggleAnimation()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Animate Solar Cycle</button>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim14_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Physical Sun Position</div>
                        <div id="sim14_true_txt" class="text-rose-400 font-bold">0.5° Below Horizon</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apparent Virtual Sun</div>
                        <div id="sim14_app_txt" class="text-amber-400 font-bold">Visible Above Horizon</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Morning Time Shift</div>
                        <div class="text-cyan-400 font-mono font-bold">+2 Minutes Early</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Daily Daylight Bonus</div>
                        <div class="text-emerald-400 font-bold">~4 Full Minutes</div>
                    </div>
                </div>
            </div>
        """
    },
    15: {
        "title": "Tyndall Effect Colloidal Scattering Studio",
        "description": "Compare a true molecular solution (e.g., salt in water) with a colloidal suspension (e.g., milk/mist). Observe how colloidal particles scatter photons to render the light beam pathway clearly visible.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Medium Type:</span>
                        <button id="sim15_btn_colloid" onclick="sim15SetMedium('colloid')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold">Colloid (Milk/Mist)</button>
                        <button id="sim15_btn_true" onclick="sim15SetMedium('true')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">True Solution (Salt Water)</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Laser Intensity:</span>
                        <input type="range" id="sim15_laser_slider" min="20" max="100" value="70" oninput="sim15Update()" class="w-24 accent-amber-500">
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim15_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Particle Size Range</div>
                        <div id="sim15_size_txt" class="text-amber-400 font-mono font-bold">1 nm to 1000 nm</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Beam Path Visibility</div>
                        <div id="sim15_vis_txt" class="text-teal-400 font-bold">Luminous Illuminated Cone</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Scattering Mechanism</div>
                        <div class="text-cyan-400 font-bold">Diffuse Tyndall Scattering</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Natural Analogue</div>
                        <div class="text-emerald-400 font-bold">Sunlight in Dusty Room / Canopy</div>
                    </div>
                </div>
            </div>
        """
    },
    16: {
        "title": "Rayleigh Scattering & Sky Color Studio",
        "description": "Investigate Rayleigh's inverse-fourth-power law (I ∝ 1/λ⁴). Adjust the wavelength slider from violet (400 nm) to red (700 nm) to understand why the clear daytime sky is blue and danger signals are red.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Wavelength (λ):</span>
                        <input type="range" id="sim16_wave_slider" min="400" max="700" value="450" oninput="sim16Update()" class="w-32 accent-amber-500">
                        <span id="sim16_wave_txt" class="text-blue-400 font-mono font-bold">450 nm (Blue)</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim16SetPreset(400)" class="px-2 py-0.5 rounded bg-slate-800 text-purple-400 hover:text-purple-300">Violet</button>
                        <button onclick="sim16SetPreset(460)" class="px-2 py-0.5 rounded bg-slate-800 text-blue-400 font-bold hover:text-blue-300">Blue Sky</button>
                        <button onclick="sim16SetPreset(700)" class="px-2 py-0.5 rounded bg-slate-800 text-rose-400 font-bold hover:text-rose-300">Red Signal</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim16_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Relative Rayleigh Intensity</div>
                        <div id="sim16_intensity_txt" class="text-cyan-400 font-mono font-bold">5.85 × Baseline</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Blue vs Red Ratio</div>
                        <div class="text-amber-400 font-mono font-bold">(700/400)⁴ ≈ 9.4×</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Sky Color Mode</div>
                        <div id="sim16_sky_mode" class="text-teal-400 font-bold">Radiant Azure Dome</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Danger Signal Rationale</div>
                        <div class="text-rose-400 font-bold">Least Scattered by Fog/Smoke</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch10_sims_part2.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part2, f, indent=2)

print(f"Generated {len(simulators_part2)} simulator templates in Part 2.")

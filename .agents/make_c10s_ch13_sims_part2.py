# -*- coding: utf-8 -*-
"""
Generate Simulators 9 to 16 for Class 10 Science Chapter 13: Our Environment
"""

import json

simulators_part2 = {
    9: {
        "title": "Unidirectional Energy Flow vs Cyclic Nutrient Studio",
        "description": "Compare the strictly one-way dissipation of solar metabolic energy into degraded thermal heat with the perpetual cyclic biogeochemical recycling of mineral nutrients.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">View Mode:</span>
                        <select id="sim9_sel_mode" onchange="sim9Update()" class="bg-slate-800 text-emerald-400 rounded px-2 py-1 border border-slate-700">
                            <option value="energy">Energy Flow (One-Way Dissipation)</option>
                            <option value="nutrients">Mineral Nutrients (Closed Cyclic Recirculation)</option>
                            <option value="both">Integrated Comparison</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Solar Input:</span>
                        <input type="range" id="sim9_solar_slider" min="50" max="150" value="100" step="10" oninput="sim9Update()" class="w-24 accent-amber-500">
                        <span id="sim9_solar_txt" class="text-amber-400 font-mono font-bold">100%</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim9_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Thermodynamic Pathway</div>
                        <div id="sim9_val_flow" class="text-emerald-400 font-bold text-sm">Strictly One-Way</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Dissipated Heat Radiation</div>
                        <div id="sim9_val_heat" class="text-rose-400 font-bold text-sm">Continuous Thermal Loss</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Nutrient Biogeochemical Cycle</div>
                        <div id="sim9_val_nutrient" class="text-cyan-400 font-bold text-sm">100% Conserved via Soil</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">External Input Requirement</div>
                        <div id="sim9_val_solar_dep" class="text-amber-400 font-bold text-sm">Uninterrupted Solar Influx</div>
                    </div>
                </div>
            </div>
        """
    },
    10: {
        "title": "Biological Toxic Magnification Ladder",
        "description": "Observe non-biodegradable synthetic chemicals (like DDT and mercury) multiplying across aquatic trophic tiers to reach lethal concentrations in apex human tissues.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Water Initial Toxin:</span>
                        <input type="range" id="sim10_toxin_slider" min="1" max="10" value="2" step="1" oninput="sim10Update()" class="w-28 accent-rose-500">
                        <span id="sim10_toxin_txt" class="text-rose-400 font-mono font-bold">0.02 ppb</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Chemical Agent:</span>
                        <select id="sim10_sel_toxin" onchange="sim10Update()" class="bg-slate-800 text-amber-400 rounded px-2 py-1 border border-slate-700">
                            <option value="ddt">DDT Organochlorine Pesticide</option>
                            <option value="mercury">Methylmercury Heavy Metal</option>
                            <option value="lead">Lead Industrial Residue</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim10_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Phytoplankton Level</div>
                        <div id="sim10_val_plankton" class="text-emerald-400 font-bold text-sm">0.04 ppm (2,000×)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Small Fish Level</div>
                        <div id="sim10_val_smallfish" class="text-teal-400 font-bold text-sm">0.5 ppm (25,000×)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Large Predatory Fish</div>
                        <div id="sim10_val_bigfish" class="text-amber-400 font-bold text-sm">2.0 ppm (100,000×)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apex Consumer (Human)</div>
                        <div id="sim10_val_apex" class="text-rose-500 font-bold text-sm">25.0 ppm (1,250,000×)</div>
                    </div>
                </div>
            </div>
        """
    },
    11: {
        "title": "Pesticide Surface Wash vs Systemic Residue Lab",
        "description": "Experiment with Activity 13.3 by testing cold water, salt wash, and boiling on vegetables to discover why surface washing removes topical dust but leaves absorbed systemic pesticides intact.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Treatment:</span>
                        <select id="sim11_sel_treatment" onchange="sim11ApplyTreatment()" class="bg-slate-800 text-emerald-400 rounded px-2 py-1 border border-slate-700">
                            <option value="raw">Unwashed Harvest (100% Contaminated)</option>
                            <option value="tap_water">Running Tap Water Wash</option>
                            <option value="salt_soak">2% Salt Solution Soak (15 mins)</option>
                            <option value="peeled">Deep Skin Peeling</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim11Reset()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Reset Produce</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim11_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Surface Coating Toxin</div>
                        <div id="sim11_val_surface" class="text-rose-400 font-bold text-sm">100% Present</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Internal Vascular Residue</div>
                        <div id="sim11_val_systemic" class="text-amber-400 font-bold text-sm">100% Embedded</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Net Decontamination</div>
                        <div id="sim11_val_decon" class="text-cyan-400 font-bold text-sm">0% Cleared</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Safe Consumption Status</div>
                        <div id="sim11_val_safety" class="text-rose-500 font-bold text-sm">Hazardous Over-Limit</div>
                    </div>
                </div>
            </div>
        """
    },
    12: {
        "title": "Two-Step Photochemical Ozone Synthesis",
        "description": "Simulate stratospheric ozone synthesis: UV photons split diatomic oxygen into nascent oxygen atoms (O₂ -> O + O), which then collide with O₂ molecules to form protective triatomic ozone (O + O₂ -> O₃).",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Solar UV Intensity:</span>
                        <input type="range" id="sim12_uv_slider" min="20" max="100" value="70" step="5" oninput="sim12Update()" class="w-28 accent-cyan-500">
                        <span id="sim12_uv_txt" class="text-cyan-400 font-mono font-bold">70% UV</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Stratospheric Altitude:</span>
                        <input type="range" id="sim12_alt_slider" min="15" max="40" value="25" step="1" oninput="sim12Update()" class="w-24 accent-indigo-500">
                        <span id="sim12_alt_txt" class="text-indigo-400 font-mono font-bold">25 km</span>
                    </div>
                    <button onclick="sim12TriggerPhoton()" class="px-2.5 py-1 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold">Fire UV Photon ⚡</button>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim12_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Photolysis Step 1</div>
                        <div id="sim12_val_step1" class="text-cyan-400 font-bold text-sm">O₂ + UV -> O + O</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Synthesis Step 2</div>
                        <div id="sim12_val_step2" class="text-emerald-400 font-bold text-sm">O + O₂ -> O₃ (Ozone)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ozone Layer Thickness</div>
                        <div id="sim12_val_dobson" class="text-teal-400 font-bold text-sm">310 Dobson Units</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">UV-B Shielding Capacity</div>
                        <div id="sim12_val_shield" class="text-amber-400 font-bold text-sm">98.5% Absorbed</div>
                    </div>
                </div>
            </div>
        """
    },
    13: {
        "title": "CFC Catalytic Ozone Depletion & Montreal Protocol",
        "description": "Witness chlorine radical catalytic cycles destroying stratospheric ozone, and test the 1987 Montreal Protocol treaty timeline to track Antarctic ozone recovery.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Simulation Year:</span>
                        <input type="range" id="sim13_year_slider" min="1980" max="2060" value="1987" step="1" oninput="sim13Update()" class="w-32 accent-rose-500">
                        <span id="sim13_year_txt" class="text-rose-400 font-mono font-bold">1987</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim13_btn_protocol" onclick="sim13ToggleMontreal()" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold">Montreal Protocol: ACTIVE 📜</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim13_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">CFC Global Concentration</div>
                        <div id="sim13_val_cfc" class="text-rose-400 font-bold text-sm">Peak 550 ppt</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Catalytic Cl Destruction</div>
                        <div id="sim13_val_cl" class="text-amber-400 font-bold text-sm">Cl + O₃ -> ClO + O₂</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Antarctic Ozone Hole Area</div>
                        <div id="sim13_val_hole" class="text-cyan-400 font-bold text-sm">24.5 Million km²</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Stratospheric Healing Trend</div>
                        <div id="sim13_val_status" class="text-emerald-400 font-bold text-sm">Frozen at 1986 Level</div>
                    </div>
                </div>
            </div>
        """
    },
    14: {
        "title": "Substrate Enzyme Specificity Lock & Key Lab",
        "description": "Investigate Activities 13.5 and 13.6 by testing bacterial enzyme action on natural cellulose polymers (rapid decomposition) versus synthetic polyethylene plastics (0% fit, persistent for centuries).",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Test Material:</span>
                        <select id="sim14_sel_material" onchange="sim14Update()" class="bg-slate-800 text-emerald-400 rounded px-2 py-1 border border-slate-700">
                            <option value="cellulose">Cellulose (Paper / Cotton / Leaf)</option>
                            <option value="protein">Keratin / Protein (Leather / Wool)</option>
                            <option value="plastic">Polyethylene Plastic Carry Bag</option>
                            <option value="glass">Silica Glass Bottle</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim14BurySample()" class="px-2.5 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Soil Burial Test (60 Days) 🪱</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim14_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Polymer Bond Type</div>
                        <div id="sim14_val_bond" class="text-emerald-400 font-bold text-sm">β-1,4 Glycosidic Link</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Bacterial Enzyme Fit</div>
                        <div id="sim14_val_fit" class="text-teal-400 font-bold text-sm">Perfect Lock-and-Key</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Decomposition Half-Life</div>
                        <div id="sim14_val_halflife" class="text-cyan-400 font-bold text-sm">3 to 6 Weeks</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Classification</div>
                        <div id="sim14_val_class" class="text-emerald-400 font-bold text-sm">100% Biodegradable</div>
                    </div>
                </div>
            </div>
        """
    },
    15: {
        "title": "Municipal Source Segregation & 5 R Studio",
        "description": "Engage with Activities 13.7 and 13.8 by sorting urban refuse into Green (Wet/Compost) and Blue (Dry/Recycle) bins to maximize compost fertilizer and prevent toxic landfill leachate.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Current Waste Item:</span>
                        <span id="sim15_item_name" class="text-amber-400 font-bold font-mono">Banana Peel (Kitchen Waste)</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim15SortItem('green')" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold">🟢 Green Bin (Wet/Compost)</button>
                        <button onclick="sim15SortItem('blue')" class="px-3 py-1 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold">🔵 Blue Bin (Dry/Recycle)</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim15_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Sorting Accuracy</div>
                        <div id="sim15_val_accuracy" class="text-emerald-400 font-bold text-sm">100% (5/5 Sorted)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Vermicompost Produced</div>
                        <div id="sim15_val_compost" class="text-teal-400 font-bold text-sm">4.5 kg Organic Fertilizer</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Landfill Diversion Rate</div>
                        <div id="sim15_val_diversion" class="text-cyan-400 font-bold text-sm">88% Diverted</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Aquifer Leachate Risk</div>
                        <div id="sim15_val_risk" class="text-emerald-400 font-bold text-sm">Zero Contamination</div>
                    </div>
                </div>
            </div>
        """
    },
    16: {
        "title": "Railway Beverage Container Lifecycle Studio",
        "description": "Evaluate the environmental tradeoffs in passenger train beverage containers: Reusable Glass vs Disposable Plastic vs Clay Kulhad vs Modern Paper Cup across hygiene, topsoil loss, and biodegradability.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Select Container Era:</span>
                        <select id="sim16_sel_cup" onchange="sim16Update()" class="bg-slate-800 text-amber-400 rounded px-2 py-1 border border-slate-700">
                            <option value="glass">1. Reusable Glass Tumblers (Early Era)</option>
                            <option value="plastic">2. Disposable Plastic/Styrofoam Cups</option>
                            <option value="kulhad">3. Terracotta Clay Kulhads</option>
                            <option value="paper">4. Food-Grade Biodegradable Paper Cups</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Daily Demand:</span>
                        <input type="range" id="sim16_demand_slider" min="1" max="10" value="5" step="1" oninput="sim16Update()" class="w-24 accent-emerald-500">
                        <span id="sim16_demand_txt" class="text-emerald-400 font-mono font-bold">5 Million/day</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim16_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Sanitary Hygiene Rating</div>
                        <div id="sim16_val_hygiene" class="text-rose-400 font-bold text-sm">Poor (Washing Risk)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Fertile Topsoil Loss</div>
                        <div id="sim16_val_topsoil" class="text-emerald-400 font-bold text-sm">0 Tons Mined</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Decomposition Time</div>
                        <div id="sim16_val_decomp" class="text-amber-400 font-bold text-sm">1 Million Years (Glass)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Lifecycle Sustainability</div>
                        <div id="sim16_val_sustain" class="text-cyan-400 font-bold text-sm">Moderate (Washing Water)</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch13_sims_part2.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part2, f, indent=2, ensure_ascii=False)

print("Saved .agents/c10s_ch13_sims_part2.json successfully!")

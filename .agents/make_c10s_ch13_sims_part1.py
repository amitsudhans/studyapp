# -*- coding: utf-8 -*-
"""
Generate Simulators 1 to 8 for Class 10 Science Chapter 13: Our Environment
"""

import json

simulators_part1 = {
    1: {
        "title": "Ecosystem Biotic & Abiotic Balance Studio",
        "description": "Simulate interactions between climatic abiotic factors (temperature, rainfall) and living biotic communities (vegetation, herbivores, predators) to discover ecosystem equilibrium.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Annual Rainfall:</span>
                        <input type="range" id="sim1_rain_slider" min="20" max="200" value="100" step="10" oninput="sim1Update()" class="w-24 accent-emerald-500">
                        <span id="sim1_rain_txt" class="text-emerald-400 font-mono font-bold">100 cm</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Mean Temp:</span>
                        <input type="range" id="sim1_temp_slider" min="5" max="45" value="25" step="1" oninput="sim1Update()" class="w-24 accent-amber-500">
                        <span id="sim1_temp_txt" class="text-amber-400 font-mono font-bold">25°C</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim1Reset()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Reset Habitat</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim1_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Biome Classification</div>
                        <div id="sim1_val_biome" class="text-emerald-400 font-bold text-sm">Temperate Forest</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Producer Canopy Biomass</div>
                        <div id="sim1_val_biomass" class="text-teal-400 font-bold text-sm">7,800 kg/ha</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Herbivore Grazing Density</div>
                        <div id="sim1_val_herbivores" class="text-cyan-400 font-bold text-sm">45 deer/km²</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Equilibrium Index</div>
                        <div id="sim1_val_stability" class="text-amber-400 font-bold text-sm">Balanced (92%)</div>
                    </div>
                </div>
            </div>
        """
    },
    2: {
        "title": "Artificial Aquarium Life-Support Studio",
        "description": "Experiment with Activity 13.1 by adjusting aerator oxygenation, fish stocking density, and aquatic plants to observe oxygen levels and toxic waste accumulation in an artificial ecosystem.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <button id="sim2_btn_aerator" onclick="sim2ToggleAerator()" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold">Aerator: ON 🫧</button>
                        <button onclick="sim2FeedFish()" class="px-2.5 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">Feed Fish 🪱</button>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Fish Count:</span>
                        <input type="range" id="sim2_fish_slider" min="2" max="15" value="6" step="1" oninput="sim2Update()" class="w-24 accent-cyan-500">
                        <span id="sim2_fish_txt" class="text-cyan-400 font-mono font-bold">6 Fish</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="sim2CleanTank()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Clean Tank 🧼</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim2_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Dissolved O₂ Saturation</div>
                        <div id="sim2_val_o2" class="text-emerald-400 font-bold text-sm">8.2 mg/L (Optimal)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Toxic Ammonia / Waste</div>
                        <div id="sim2_val_waste" class="text-amber-400 font-bold text-sm">0.15 ppm (Safe)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Aquatic Plants (Hydrilla)</div>
                        <div id="sim2_val_plants" class="text-teal-400 font-bold text-sm">Photosynthesizing</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Ecosystem Status</div>
                        <div id="sim2_val_status" class="text-cyan-400 font-bold text-sm">Healthy Aquarium</div>
                    </div>
                </div>
            </div>
        """
    },
    3: {
        "title": "Ecological Trophic Roles Lab",
        "description": "Examine how producers, primary consumers, secondary consumers, and specialized parasites acquire nourishment and drive metabolic energy flow.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Select Organism:</span>
                        <select id="sim3_sel_organism" onchange="sim3Update()" class="bg-slate-800 text-emerald-400 rounded px-2 py-1 border border-slate-700">
                            <option value="producer">Green Plant (Autotroph)</option>
                            <option value="herbivore">Grasshopper (Primary Consumer)</option>
                            <option value="carnivore">Frog (Secondary Consumer)</option>
                            <option value="parasite">Cuscuta / Amarbel (Plant Parasite)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Sunlight Level:</span>
                        <input type="range" id="sim3_sun_slider" min="10" max="100" value="80" step="5" oninput="sim3Update()" class="w-24 accent-amber-500">
                        <span id="sim3_sun_txt" class="text-amber-400 font-mono font-bold">80%</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim3_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Nutritional Category</div>
                        <div id="sim3_val_mode" class="text-emerald-400 font-bold text-sm">Photoautotrophic</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Primary Energy Source</div>
                        <div id="sim3_val_source" class="text-teal-400 font-bold text-sm">Solar Photons + CO₂</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Chlorophyll Presence</div>
                        <div id="sim3_val_chloro" class="text-cyan-400 font-bold text-sm">Active Chloroplasts</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Trophic Rank</div>
                        <div id="sim3_val_rank" class="text-amber-400 font-bold text-sm">Trophic Level 1</div>
                    </div>
                </div>
            </div>
        """
    },
    4: {
        "title": "Decomposer Microbial Mineralization Engine",
        "description": "Observe saprophytic bacteria and fungi breaking down dead organic detritus, releasing essential nitrogen, phosphorus, and potassium ions to replenish soil fertility.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Dead Detritus Input:</span>
                        <input type="range" id="sim4_waste_slider" min="10" max="100" value="50" step="5" oninput="sim4Update()" class="w-24 accent-amber-500">
                        <span id="sim4_waste_txt" class="text-amber-400 font-mono font-bold">50 kg</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Microbial Density:</span>
                        <input type="range" id="sim4_micro_slider" min="1" max="5" value="3" step="1" oninput="sim4Update()" class="w-24 accent-emerald-500">
                        <span id="sim4_micro_txt" class="text-emerald-400 font-mono font-bold">Moderate (3×)</span>
                    </div>
                    <button onclick="sim4ToggleEnzymes()" id="sim4_btn_enz" class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold">Enzymes: ON</button>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim4_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Mineralization Rate</div>
                        <div id="sim4_val_rate" class="text-emerald-400 font-bold text-sm">4.8 kg/day</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Released Soil Nutrients (NPK)</div>
                        <div id="sim4_val_npk" class="text-teal-400 font-bold text-sm">340 mg/kg</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Humus Soil Organic Layer</div>
                        <div id="sim4_val_humus" class="text-cyan-400 font-bold text-sm">Rich Humus (6.2%)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Soil Recycling Status</div>
                        <div id="sim4_val_status" class="text-amber-400 font-bold text-sm">Actively Replenished</div>
                    </div>
                </div>
            </div>
        """
    },
    5: {
        "title": "4-Tier Food Chain Cascade Simulator",
        "description": "Construct linear terrestrial and aquatic food chains, and simulate trophic cascade disruptions when an intermediate consumer tier is removed.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Habitat Chain:</span>
                        <select id="sim5_sel_chain" onchange="sim5UpdateChain()" class="bg-slate-800 text-emerald-400 rounded px-2 py-1 border border-slate-700">
                            <option value="grassland">Grassland: Grass -> Insect -> Frog -> Snake -> Hawk</option>
                            <option value="forest">Forest: Tree -> Deer -> Tiger</option>
                            <option value="pond">Pond: Algae -> Zooplankton -> Small Fish -> Crane</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-2">
                        <button id="sim5_btn_disrupt" onclick="sim5ToggleDisruption()" class="px-3 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold">Remove Intermediate Tier ⚡</button>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim5_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Producer Level (T1)</div>
                        <div id="sim5_val_t1" class="text-emerald-400 font-bold text-sm">Healthy Abundance</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Primary Consumer (T2)</div>
                        <div id="sim5_val_t2" class="text-teal-400 font-bold text-sm">Regulated Herbivory</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Secondary Consumer (T3)</div>
                        <div id="sim5_val_t3" class="text-cyan-400 font-bold text-sm">Active Predation</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apex Predator (T4/T5)</div>
                        <div id="sim5_val_t4" class="text-amber-400 font-bold text-sm">Sustained Population</div>
                    </div>
                </div>
            </div>
        """
    },
    6: {
        "title": "Solar Energy 1% Photochemical Capture Studio",
        "description": "Quantify how terrestrial leaves intercept incident solar radiation, reflecting and dissipating 99% while capturing exactly 1% into synthesized carbohydrate chemical bond energy.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Incident Solar Energy:</span>
                        <input type="range" id="sim6_solar_slider" min="100000" max="2000000" value="1000000" step="100000" oninput="sim6Update()" class="w-32 accent-amber-500">
                        <span id="sim6_solar_txt" class="text-amber-400 font-mono font-bold">1,000,000 J</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Canopy Cover:</span>
                        <input type="range" id="sim6_canopy_slider" min="50" max="100" value="100" step="5" oninput="sim6Update()" class="w-24 accent-emerald-500">
                        <span id="sim6_canopy_txt" class="text-emerald-400 font-mono font-bold">100%</span>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim6_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Captured Plant Energy (1%)</div>
                        <div id="sim6_val_captured" class="text-emerald-400 font-bold text-sm">10,000 J</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Reflected & Transmitted (99%)</div>
                        <div id="sim6_val_lost" class="text-rose-400 font-bold text-sm">990,000 J</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Photosynthetic Efficiency</div>
                        <div id="sim6_val_eff" class="text-cyan-400 font-bold text-sm">Exactly 1.0%</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Gross Primary Output</div>
                        <div id="sim6_val_gpp" class="text-amber-400 font-bold text-sm">2.4 g Glucose/m²</div>
                    </div>
                </div>
            </div>
        """
    },
    7: {
        "title": "Lindeman 10% Trophic Energy Pyramid",
        "description": "Calculate and visualize step-by-step 90% metabolic energy dissipation and the remaining 10% trophic transfer across progressive ecological tiers.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Producer Energy (T1):</span>
                        <input type="range" id="sim7_energy_slider" min="1000" max="50000" value="10000" step="1000" oninput="sim7Update()" class="w-32 accent-emerald-500">
                        <span id="sim7_energy_txt" class="text-emerald-400 font-mono font-bold">10,000 J</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Trophic Levels:</span>
                        <select id="sim7_sel_tiers" onchange="sim7Update()" class="bg-slate-800 text-amber-400 rounded px-2 py-1 border border-slate-700">
                            <option value="4">4 Levels (Producers -> Apex)</option>
                            <option value="5">5 Levels (Extended Chain)</option>
                        </select>
                    </div>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim7_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Herbivore Energy (T2)</div>
                        <div id="sim7_val_t2" class="text-emerald-400 font-bold text-sm">1,000 J (10%)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Small Carnivore Energy (T3)</div>
                        <div id="sim7_val_t3" class="text-teal-400 font-bold text-sm">100 J (1%)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Apex Predator Energy (T4)</div>
                        <div id="sim7_val_t4" class="text-cyan-400 font-bold text-sm">10 J (0.1%)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Total Dissipated Heat</div>
                        <div id="sim7_val_heat" class="text-rose-400 font-bold text-sm">9,990 J Lost</div>
                    </div>
                </div>
            </div>
        """
    },
    8: {
        "title": "Interconnected Food Web Dynamic Graph",
        "description": "Interact with a multi-branching network of feeding links to explore how dietary flexibility and alternative prey pathways buffer biological communities against sudden species collapse.",
        "html": """
            <div class="space-y-4">
                <div class="flex flex-wrap items-center justify-between gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400">Trigger Environmental Shock:</span>
                        <select id="sim8_sel_shock" onchange="sim8ApplyShock()" class="bg-slate-800 text-amber-400 rounded px-2 py-1 border border-slate-700">
                            <option value="none">Normal Equilibrium</option>
                            <option value="insect_blight">Insect Crop Blight (-80% Insects)</option>
                            <option value="rodent_decline">Rodent Viral Outbreak (-80% Mice)</option>
                            <option value="frog_decline">Wetland Drainage (-80% Frogs)</option>
                        </select>
                    </div>
                    <button onclick="sim8ResetWeb()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium">Reset Web</button>
                </div>

                <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
                    <canvas id="sim8_canvas" width="600" height="260" class="w-full h-full"></canvas>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Predator Dietary Shift</div>
                        <div id="sim8_val_shift" class="text-emerald-400 font-bold text-sm">Balanced across prey</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Network Redundancy</div>
                        <div id="sim8_val_redundancy" class="text-teal-400 font-bold text-sm">8 Interconnected Links</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Community Homeostasis</div>
                        <div id="sim8_val_stability" class="text-cyan-400 font-bold text-sm">Highly Stable (95%)</div>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                        <div class="text-slate-400 text-[10px]">Trophic Cascade Impact</div>
                        <div id="sim8_val_cascade" class="text-amber-400 font-bold text-sm">Absorbed by Web</div>
                    </div>
                </div>
            </div>
        """
    }
}

with open(".agents/c10s_ch13_sims_part1.json", "w", encoding="utf-8") as f:
    json.dump(simulators_part1, f, indent=2, ensure_ascii=False)

print("Saved .agents/c10s_ch13_sims_part1.json successfully!")

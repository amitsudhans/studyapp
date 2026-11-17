#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Simulators 1 to 8 HTML markup for NCERT Class 10 Science Chapter 5: Life Processes.
"""

import json

sims_part1 = {
    1: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Molecular Movement & Structural Repair Simulator
                </h3>
                <p class="text-xs text-slate-400">Observe how continuous microscopic molecular repair counteracts environmental breakdown</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="toggleSlide1Repair()" id="s1RepairBtn" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all">
                    Enable Active Repair
                </button>
                <button onclick="resetSlide1Sim()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition-all">
                    Reset
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="md:col-span-2 bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center relative min-h-[220px]">
                <canvas id="s1Canvas" width="480" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
                <div id="s1StatusBadge" class="absolute top-5 right-5 px-2.5 py-1 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">
                    Degradation: Natural Wear
                </div>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <span class="font-bold text-white uppercase text-[10px] tracking-wider block text-amber-400">Structural Metrics</span>
                    <div class="flex justify-between border-b border-slate-800/60 pb-1.5">
                        <span class="text-slate-400">Cellular Order:</span>
                        <span id="s1OrderVal" class="font-mono text-emerald-400 font-bold">100%</span>
                    </div>
                    <div class="flex justify-between border-b border-slate-800/60 pb-1.5">
                        <span class="text-slate-400">Molecular Kinetic Energy:</span>
                        <span id="s1EnergyVal" class="font-mono text-cyan-400 font-bold">Active</span>
                    </div>
                    <div class="flex justify-between border-b border-slate-800/60 pb-1.5">
                        <span class="text-slate-400">Organism State:</span>
                        <span id="s1StateVal" class="font-bold text-emerald-400">Living & Maintained</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400 leading-relaxed">
                    💡 <strong class="text-slate-200">NCERT Principle:</strong> Environmental factors constantly degrade organized tissues. Without continuous invisible molecular movement, structural entropy causes biological death.
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    The 4 Life Processes & Multicellular Diffusion Trap
                </h3>
                <p class="text-xs text-slate-400">Explore essential life functions and compare single-cell vs multicellular diffusion rates</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide2Mode('unicellular')" id="s2BtnUni" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-slate-950 font-bold text-xs transition-all">Single-Celled (Amoeba)</button>
                <button onclick="setSlide2Mode('multicellular')" id="s2BtnMulti" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Multicellular Body</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s2Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s2Description" class="space-y-2">
                    <span class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Direct Diffusion (Amoeba)</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        In unicellular Amoeba, the entire plasma membrane touches the aquatic medium. Gases, nutrients, and wastes diffuse in fractions of a second across microscopic distances.
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                        <div class="flex justify-between text-[11px]"><span class="text-slate-400">Diffusion Distance:</span><span class="font-mono text-emerald-400">&lt; 50 μm</span></div>
                        <div class="flex justify-between text-[11px]"><span class="text-slate-400">Oxygen Transit Time:</span><span class="font-mono text-emerald-400">0.02 seconds</span></div>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[11px]">
                    <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800 text-center"><strong class="text-amber-400 block">1. Nutrition</strong>Carbon Energy</div>
                    <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800 text-center"><strong class="text-cyan-400 block">2. Respiration</strong>O2 ATP Release</div>
                    <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800 text-center"><strong class="text-emerald-400 block">3. Transport</strong>Vascular Delivery</div>
                    <div class="p-2 rounded-lg bg-slate-900/80 border border-slate-800 text-center"><strong class="text-rose-400 block">4. Excretion</strong>Toxic Waste Removal</div>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Photosynthesis Master Reaction & Three Major Events
                </h3>
                <p class="text-xs text-slate-400">6CO2 + 12H2O ➔ C6H12O6 + 6O2 + 6H2O in chlorophyll thylakoids</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="stepSlide3Event()" id="s3StepBtn" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs transition-all">
                    Step Event: Next Phase →
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="md:col-span-2 bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s3Canvas" width="480" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <span class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Current Reaction Phase</span>
                    <div id="s3PhaseTitle" class="font-bold text-white text-sm">1. Solar Photon Absorption</div>
                    <p id="s3PhaseDesc" class="text-xs text-slate-300 leading-relaxed">
                        Chlorophyll pigments inside leaf chloroplasts absorb solar photons, elevating electrons to a higher energy state.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-[11px]">
                    <div class="text-slate-400">Chemical Equation:</div>
                    <div class="font-mono text-emerald-300 font-bold text-[10.5px]">6CO2 + 12H2O ➔ C6H12O6 + 6O2 + 6H2O</div>
                    <div class="text-[10px] text-amber-300 mt-1">Desert plants absorb CO2 at night, processing intermediate malate by daylight!</div>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Activity 5.1: Variegated Leaf Chlorophyll & Starch Test
                </h3>
                <p class="text-xs text-slate-400">De-starching, alcohol bleaching in water bath, and iodine test on money plant / croton</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="stepSlide4Activity()" id="s4StepBtn" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold text-xs transition-all">
                    Next Activity Step →
                </button>
                <button onclick="resetSlide4Activity()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition-all">
                    Reset
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s4Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-amber-400 uppercase text-[10px] tracking-wider">Experimental Stage</span>
                        <span id="s4StepBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300">Stage 1 of 4</span>
                    </div>
                    <div id="s4StepTitle" class="font-bold text-white text-sm">Step 1: De-starching in Dark</div>
                    <p id="s4StepDesc" class="text-xs text-slate-300 leading-relaxed">
                        The variegated money plant is kept in complete darkness for 3 days to force cells to consume all pre-existing starch reserves through cellular respiration.
                    </p>
                </div>
                <div id="s4OutcomeBox" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <strong class="text-white block mb-0.5">Key Observation:</strong>
                    Iodine solution stains only the green chlorophyll zones blue-black, proving chlorophyll is indispensable for starch synthesis.
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    Stomatal Guard Cell Hydraulics & Activity 5.2 (KOH Bell Jar)
                </h3>
                <p class="text-xs text-slate-400">Adjust guard cell turgor pressure or toggle potassium hydroxide CO2 absorption</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide5Tab('stoma')" id="s5TabStoma" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-slate-950 font-bold text-xs transition-all">Guard Cell Hydraulics</button>
                <button onclick="setSlide5Tab('koh')" id="s5TabKOH" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Activity 5.2 Bell Jars</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s5Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s5Controls" class="space-y-3">
                    <div>
                        <div class="flex justify-between text-xs mb-1">
                            <span class="text-slate-400">Guard Cell Water Inflow (Turgor):</span>
                            <span id="s5TurgorVal" class="font-mono text-emerald-400 font-bold">Turgid (Open Pore)</span>
                        </div>
                        <input type="range" id="s5TurgorSlider" min="0" max="100" value="80" oninput="updateSlide5Stoma(this.value)" class="w-full accent-emerald-500">
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                        <strong class="text-amber-400">Hydraulic Mechanism:</strong> Water inflow swells guard cells; thin outer walls bow out, pulling thick inner concave walls apart to open the pore. Water loss collapses them closed.
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <strong class="text-white block mb-0.5">Activity 5.2 Insight:</strong>
                    Potassium hydroxide (KOH) absorbs CO2 completely. Potted plant under the KOH bell jar fails to produce starch, proving CO2 is mandatory.
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Heterotrophic Nutritional Strategies Simulator
                </h3>
                <p class="text-xs text-slate-400">Compare Saprophytic extracellular breakdown, Holozoic ingestion, and Parasitic haustoria</p>
            </div>
            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                <button onclick="setSlide6Mode('saprophyte')" id="s6BtnSapro" class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-bold text-xs transition-all">Saprophytic (Fungi)</button>
                <button onclick="setSlide6Mode('holozoic')" id="s6BtnHolo" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Holozoic (Animal)</button>
                <button onclick="setSlide6Mode('parasite')" id="s6BtnPara" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white font-semibold text-xs transition-all">Parasitic (Cuscuta)</button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s6Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div id="s6Details" class="space-y-2">
                    <span id="s6Title" class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Saprophytic Nutrition (Bread Mould / Mushrooms)</span>
                    <p id="s6Desc" class="text-xs text-slate-300 leading-relaxed">
                        Fungi secrete digestive enzymes externally onto dead organic matter, breaking polymers down into soluble molecules before absorbing them across hyphal walls.
                    </p>
                </div>
                <div class="grid grid-cols-3 gap-1.5 text-center text-[10.5px]">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Digestion:</strong><span id="s6DigVal" class="text-amber-400">External</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Host Fate:</strong><span id="s6HostVal" class="text-emerald-400">Dead Decay</span></div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><strong class="text-white block">Example:</strong><span id="s6ExVal" class="text-cyan-400">Rhizopus</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                    Unicellular Digestion: Amoeba vs Paramoecium
                </h3>
                <p class="text-xs text-slate-400">Pseudopodia phagocytosis & food vacuole diffusion vs ciliary cytostome current</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide7Engulf()" id="s7EngulfBtn" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold text-xs transition-all">
                    Feed Particle →
                </button>
                <button onclick="toggleSlide7Organism()" id="s7ToggleBtn" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition-all">
                    Switch to Paramoecium
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s7Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <span id="s7OrganismTitle" class="font-bold text-cyan-400 uppercase text-[10px] tracking-wider block">Amoeba Phagocytosis (Figure 5.5)</span>
                    <p id="s7OrganismDesc" class="text-xs text-slate-300 leading-relaxed">
                        Temporary finger-like pseudopodia extend and fuse around food, forming an internal food vacuole where hydrolytic enzymes digest polymers into soluble nutrients.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <div class="flex justify-between"><span class="text-slate-400">Feeding Apparatus:</span><span id="s7Apparatus" class="font-bold text-cyan-300">Pseudopodia (Any Site)</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Vacuole Action:</span><span class="font-bold text-emerald-400">Enzymatic Breakdown</span></div>
                    <div class="flex justify-between"><span class="text-slate-400">Egestion:</span><span class="font-bold text-amber-400">Surface Membrane Rupture</span></div>
                </div>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    Human Buccal Cavity, Salivary Amylase & Peristalsis
                </h3>
                <p class="text-xs text-slate-400">Activity 5.3 starch iodine test and involuntary oesophageal muscular peristaltic wave</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerSlide8Peristalsis()" id="s8PeristalsisBtn" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold text-xs transition-all">
                    Trigger Food Swallow Bolus
                </button>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-950 border border-slate-800/80 rounded-xl p-3 flex flex-col items-center justify-center min-h-[220px]">
                <canvas id="s8Canvas" width="360" height="200" class="w-full max-w-full rounded-lg bg-slate-950"></canvas>
            </div>
            <div class="space-y-3 bg-slate-950/60 border border-slate-800/80 rounded-xl p-3.5 text-xs text-slate-300 flex flex-col justify-between">
                <div class="space-y-2">
                    <span class="font-bold text-amber-400 uppercase text-[10px] tracking-wider block">Activity 5.3: Salivary Amylase Action</span>
                    <div class="grid grid-cols-2 gap-2 text-[11px]">
                        <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center">
                            <strong class="text-slate-300 block">Tube A (Starch only)</strong>
                            <span class="text-rose-400 font-bold">Deep Blue-Black</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center">
                            <strong class="text-slate-300 block">Tube B (Starch + Saliva)</strong>
                            <span class="text-emerald-400 font-bold">No Colour Change</span>
                        </div>
                    </div>
                    <p class="text-[11px] text-slate-400 leading-relaxed">
                        Salivary amylase breaks insoluble starch into simple maltose sugars. In the oesophagus, rhythmic contractions (peristalsis) propel food into the stomach.
                    </p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <strong class="text-white block mb-0.5">Dental Caries Note:</strong> Bacterial plaque on teeth ferments sugar to acid; brushing removes plaque before acids demineralize enamel.
                </div>
            </div>
        </div>
    </div>
    """
}

with open('.agents/c10s_ch5_sims_part1.json', 'w', encoding='utf-8') as f:
    json.dump(sims_part1, f, indent=2)

print("Simulators 1 to 8 successfully generated!")

# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 10 Science, Chapter 13: Our Environment.
Generates public/animations/our-environment.html with:
- 16 Rich Content Slides covering every line of the NCERT textbook (Pages 208-217).
- 32 In-Slide Checkpoint Questions with instant teacher feedback.
- 4 Dedicated Mastery Quiz Challenge Slides (40 questions total) with popup solution modals.
- 16 Bespoke Interactive SVG Laboratory Simulators.
- Animated Teacher Avatar (Dr. Sophia - Environmental Science Educator) with talking mouth synced to audio narration.
- Web Audio API sound synthesizer and Web Speech API narration.
- Last Slide Notice with strict unit test compatibility.
"""

import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from environment_data import CONTENT_SLIDES, QUIZ_SLIDES

def generate_interactive_simulator(s_idx):
    """Returns bespoke interactive SVG simulator HTML for each content slide (1-16)."""
    if s_idx == 1:
        # Lab 13.1: Ecosystem Biotic-Abiotic Balance Simulator
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">Interactive Lab 13.1: Ecosystem Biotic-Abiotic Dynamics</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim1Type('natural')" id="btn-sim1-nat" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition">Natural Forest</button>
                    <button onclick="toggleSim1Type('artificial')" id="btn-sim1-art" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Human-Made Garden</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-sky-950 via-slate-900 to-emerald-950/60 rounded-xl overflow-hidden border border-slate-800">
                <svg id="sim1-canvas" viewBox="0 0 500 280" class="w-full h-full">
                    <!-- Sky & Sun -->
                    <circle id="sim1-sun" cx="440" cy="50" r="30" fill="#facc15" opacity="0.9" filter="drop-shadow(0 0 15px #facc15)"/>
                    <!-- Clouds & Rain -->
                    <g id="sim1-clouds">
                        <path d="M60 50 Q80 30 110 40 Q130 25 160 45 Q180 50 170 70 Q140 85 90 75 Z" fill="#94a3b8" opacity="0.7"/>
                        <path d="M220 40 Q240 20 270 30 Q290 15 320 35 Q340 40 330 60 Q300 75 250 65 Z" fill="#cbd5e1" opacity="0.6"/>
                    </g>
                    <g id="sim1-rain" opacity="0">
                        <line x1="100" y1="80" x2="90" y2="120" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="130" y1="85" x2="120" y2="125" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="160" y1="80" x2="150" y2="120" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
                    </g>
                    <!-- Landscape Terrain -->
                    <path d="M0 200 Q150 160 300 190 T500 180 L500 280 L0 280 Z" fill="#14532d"/>
                    <path d="M0 220 Q200 190 350 215 T500 205 L500 280 L0 280 Z" fill="#0f3d21"/>

                    <!-- Plants / Trees -->
                    <g id="sim1-flora">
                        <!-- Forest Tree 1 -->
                        <rect x="70" y="140" width="16" height="60" fill="#78350f" rx="3"/>
                        <circle cx="78" cy="120" r="35" fill="#15803d"/>
                        <!-- Forest Tree 2 -->
                        <rect x="380" y="130" width="18" height="70" fill="#78350f" rx="3"/>
                        <polygon points="389,80 350,140 428,140" fill="#166534"/>
                        <polygon points="389,110 360,160 418,160" fill="#15803d"/>
                    </g>

                    <!-- Fauna Animals -->
                    <g id="sim1-fauna">
                        <!-- Deer / Herbivore -->
                        <g transform="translate(180, 175) scale(0.6)">
                            <ellipse cx="40" cy="30" rx="20" ry="12" fill="#d97706"/>
                            <rect x="25" y="38" width="4" height="22" fill="#b45309"/>
                            <rect x="35" y="38" width="4" height="22" fill="#b45309"/>
                            <rect x="45" y="38" width="4" height="22" fill="#b45309"/>
                            <rect x="55" y="38" width="4" height="22" fill="#b45309"/>
                            <circle cx="58" cy="18" r="8" fill="#d97706"/>
                            <polygon points="62,10 60,18 66,16" fill="#78350f"/>
                        </g>
                        <!-- Bird in Flight -->
                        <path d="M240 70 Q250 60 260 70 Q270 60 280 70" fill="none" stroke="#f8fafc" stroke-width="2"/>
                    </g>

                    <!-- Status Display HUD -->
                    <rect x="15" y="15" width="220" height="55" rx="8" fill="rgba(15,23,42,0.85)" stroke="#334155"/>
                    <text x="25" y="33" fill="#38bdf8" font-size="11" font-weight="bold" id="sim1-hud-mode">Ecosystem: Natural Forest</text>
                    <text x="25" y="48" fill="#94a3b8" font-size="9" id="sim1-hud-sub">Abiotic: Sunlight 85%, Rain 40% • Balanced</text>
                    <text x="25" y="60" fill="#4ade80" font-size="9" id="sim1-hud-bio">Biotic: Flora & Fauna in dynamic equilibrium</text>
                </svg>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-3">
                <div>
                    <div class="flex justify-between text-xs text-slate-300 mb-1">
                        <span>Solar Light Intensity:</span>
                        <span id="sim1-sun-val" class="font-bold text-amber-400">85%</span>
                    </div>
                    <input type="range" id="sim1-sun-slider" min="20" max="100" value="85" oninput="updateSim1Abiotic()" class="w-full accent-amber-500 cursor-pointer">
                </div>
                <div>
                    <div class="flex justify-between text-xs text-slate-300 mb-1">
                        <span>Rainfall Abiotic Level:</span>
                        <span id="sim1-rain-val" class="font-bold text-sky-400">Low (Drizzle)</span>
                    </div>
                    <input type="range" id="sim1-rain-slider" min="0" max="100" value="30" oninput="updateSim1Abiotic()" class="w-full accent-sky-500 cursor-pointer">
                </div>
            </div>
            <p id="sim1-desc" class="text-xs text-slate-400 mt-2 text-center">
                Abiotic components (temperature, sunlight, rainfall) directly govern biotic population growth and health!
            </p>
        </div>
        """

    elif s_idx == 2:
        # Lab 13.2: Aquarium Artificial Ecosystem Simulator (Activity 13.1)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-cyan-400">Interactive Lab 13.2: Activity 13.1 Aquarium Engineering</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim2Aerator()" id="btn-sim2-pump" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition">Aerator Pump: ON</button>
                    <button onclick="feedSim2Fish()" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">Feed Fish</button>
                    <button onclick="cleanSim2Tank()" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">Clean Aquarium</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border-2 border-cyan-500/40">
                <svg id="sim2-canvas" viewBox="0 0 500 280" class="w-full h-full">
                    <!-- Glass Tank Water -->
                    <rect id="sim2-water" x="20" y="30" width="460" height="230" rx="8" fill="#082f49" opacity="0.85"/>
                    <rect x="20" y="240" width="460" height="20" fill="#78350f" opacity="0.6"/> <!-- Gravel Bed -->

                    <!-- Aquatic Plants (Elodea) -->
                    <path d="M60 240 Q40 180 70 120 Q50 80 80 50" fill="none" stroke="#22c55e" stroke-width="4"/>
                    <path d="M90 240 Q110 170 80 110 Q110 70 90 40" fill="none" stroke="#16a34a" stroke-width="3"/>
                    <path d="M420 240 Q440 170 410 120 Q440 80 420 40" fill="none" stroke="#22c55e" stroke-width="4"/>

                    <!-- Aerator Tubing & Bubble Streams -->
                    <rect x="30" y="235" width="20" height="10" fill="#475569" rx="2"/>
                    <g id="sim2-bubbles">
                        <circle cx="40" cy="220" r="3" fill="#bae6fd" opacity="0.7"/>
                        <circle cx="45" cy="180" r="4" fill="#bae6fd" opacity="0.7"/>
                        <circle cx="38" cy="140" r="3.5" fill="#bae6fd" opacity="0.7"/>
                        <circle cx="42" cy="100" r="5" fill="#bae6fd" opacity="0.7"/>
                        <circle cx="40" cy="60" r="4" fill="#bae6fd" opacity="0.7"/>
                    </g>

                    <!-- Swimming Fish -->
                    <g id="sim2-fish1" transform="translate(200, 120)">
                        <ellipse cx="0" cy="0" rx="22" ry="12" fill="#f97316"/>
                        <polygon points="18,0 32,-10 32,10" fill="#ea580c"/>
                        <circle cx="-12" cy="-3" r="2.5" fill="#ffffff"/>
                        <circle cx="-12" cy="-3" r="1.2" fill="#0f172a"/>
                    </g>
                    <g id="sim2-fish2" transform="translate(320, 170)">
                        <ellipse cx="0" cy="0" rx="18" ry="10" fill="#38bdf8"/>
                        <polygon points="14,0 26,-8 26,8" fill="#0284c7"/>
                        <circle cx="-10" cy="-2" r="2" fill="#ffffff"/>
                        <circle cx="-10" cy="-2" r="1" fill="#0f172a"/>
                    </g>

                    <!-- Floating Food Flakes -->
                    <g id="sim2-flakes" opacity="0">
                        <circle cx="180" cy="45" r="2" fill="#fbbf24"/>
                        <circle cx="240" cy="50" r="2.5" fill="#f59e0b"/>
                        <circle cx="300" cy="45" r="2" fill="#d97706"/>
                    </g>

                    <!-- Water Quality Gauges HUD -->
                    <rect x="280" y="40" width="180" height="60" rx="8" fill="rgba(15,23,42,0.9)" stroke="#0284c7"/>
                    <text x="290" y="58" fill="#38bdf8" font-size="10" font-weight="bold">Dissolved Oxygen (DO):</text>
                    <text x="420" y="58" fill="#4ade80" font-size="10" font-weight="bold" id="sim2-do-val">8.2 mg/L</text>
                    <text x="290" y="76" fill="#94a3b8" font-size="9">Tank Cleanliness:</text>
                    <text x="420" y="76" fill="#38bdf8" font-size="9" font-weight="bold" id="sim2-clean-val">98% Clean</text>
                    <text x="290" y="92" fill="#f59e0b" font-size="8.5" id="sim2-status-note">Aquarium healthy & self-sustaining</text>
                </svg>
            </div>
            <p id="sim2-desc" class="text-xs text-slate-400 mt-2 text-center">
                An aquarium is a human-made artificial ecosystem. Without an aerator pump, dissolved oxygen depletes rapidly!
            </p>
        </div>
        """

    elif s_idx == 3:
        # Lab 13.3: Saprophytic Decomposers & Soil Mineralization Lab
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-violet-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-violet-400">Interactive Lab 13.3: Decomposers & Soil Replenishment</span>
                </div>
                <button onclick="toggleSim3Decomposers()" id="btn-sim3-toggle" class="px-2.5 py-1 rounded text-xs font-bold bg-violet-600 text-white transition">Decomposers: ACTIVE</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-violet-500/30">
                <svg id="sim3-canvas" viewBox="0 0 500 280" class="w-full h-full">
                    <!-- Surface Grass & Sky -->
                    <rect x="0" y="0" width="500" height="90" fill="#064e3b" opacity="0.4"/>
                    <line x1="0" y1="90" x2="500" y2="90" stroke="#10b981" stroke-width="3"/>

                    <!-- Plant on Surface -->
                    <rect x="360" y="30" width="8" height="60" fill="#15803d"/>
                    <path d="M360 40 Q320 20 330 50 Q350 55 360 50" fill="#22c55e"/>
                    <path d="M368 35 Q410 15 400 45 Q380 50 368 45" fill="#22c55e"/>

                    <!-- Plant Roots in Soil -->
                    <path d="M364 90 Q350 150 330 220 M364 120 Q390 170 410 230 M355 140 Q320 180 300 210" fill="none" stroke="#ca8a04" stroke-width="2.5"/>

                    <!-- Deep Soil Profile -->
                    <rect x="0" y="90" width="500" height="190" fill="#27180e"/>

                    <!-- Dead Leaf & Organic Remains on Soil Bed -->
                    <g id="sim3-dead-leaf" transform="translate(100, 100)">
                        <path d="M0 20 Q40 0 80 15 Q100 30 70 45 Q30 50 0 20 Z" fill="#92400e" stroke="#78350f" stroke-width="1.5"/>
                        <line x1="10" y1="20" x2="70" y2="30" stroke="#78350f" stroke-width="1"/>
                    </g>

                    <!-- Bacterial & Fungal Hyphae Networks -->
                    <g id="sim3-microbes">
                        <!-- Fungal Mycelium branching -->
                        <path d="M120 125 Q140 150 160 170 Q190 190 220 180" fill="none" stroke="#e9d5ff" stroke-width="1.5" stroke-dasharray="2,2"/>
                        <path d="M140 150 Q120 180 110 210" fill="none" stroke="#e9d5ff" stroke-width="1" stroke-dasharray="2,2"/>
                        <!-- Bacterial colonies (dots) -->
                        <circle cx="115" cy="120" r="3" fill="#a855f7"/>
                        <circle cx="130" cy="130" r="2.5" fill="#a855f7"/>
                        <circle cx="150" cy="125" r="3" fill="#c084fc"/>
                        <circle cx="165" cy="140" r="2.5" fill="#c084fc"/>
                    </g>

                    <!-- Released Mineral Ions Flowing to Roots -->
                    <g id="sim3-minerals">
                        <circle cx="200" cy="170" r="4" fill="#38bdf8"/>
                        <text x="208" y="174" fill="#38bdf8" font-size="8" font-family="monospace">NO₃⁻</text>
                        <circle cx="260" cy="190" r="4" fill="#facc15"/>
                        <text x="268" y="194" fill="#facc15" font-size="8" font-family="monospace">PO₄³⁻</text>
                        <circle cx="310" cy="160" r="4" fill="#4ade80"/>
                        <text x="318" y="164" fill="#4ade80" font-size="8" font-family="monospace">K⁺</text>
                    </g>

                    <!-- HUD Information Box -->
                    <rect x="20" y="190" width="200" height="70" rx="8" fill="rgba(15,23,42,0.92)" stroke="#7c3aed"/>
                    <text x="30" y="210" fill="#c084fc" font-size="10" font-weight="bold" id="sim3-title">Decomposers: Active Mineralization</text>
                    <text x="30" y="228" fill="#94a3b8" font-size="8.5" id="sim3-detail1">Bacteria/fungi break complex organic matter</text>
                    <text x="30" y="244" fill="#4ade80" font-size="8.5" id="sim3-detail2">Inorganic nutrients recycled to plant roots</text>
                </svg>
            </div>
            <p id="sim3-desc" class="text-xs text-slate-400 mt-2 text-center">
                Decomposers convert dead biomass into simple inorganic salts ($NO_3^-$, $PO_4^{3-}$). Without them, natural soil replenishment ceases completely!
            </p>
        </div>
        """

    elif s_idx == 4:
        # Lab 13.4: Terrestrial & Aquatic Food Chain Stepper (Fig 13.1)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">Interactive Lab 13.4: NCERT Food Chains (Figure 13.1)</span>
                </div>
                <div class="flex items-center gap-1.5">
                    <button onclick="selectSim4Chain('forest')" id="btn-chain-forest" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition">Forest</button>
                    <button onclick="selectSim4Chain('grassland')" id="btn-chain-grass" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Grassland</button>
                    <button onclick="selectSim4Chain('pond')" id="btn-chain-pond" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Pond</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-3">
                <div id="sim4-display" class="w-full flex items-center justify-between gap-2 overflow-x-auto py-4">
                    <!-- Dynamic Chain populated by JS -->
                </div>
            </div>

            <div id="sim4-info" class="mt-3 p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-xs text-slate-300">
                <span class="font-bold text-emerald-400" id="sim4-chain-title">Forest Food Chain (3 Trophic Tiers):</span>
                <p id="sim4-chain-desc" class="mt-1 text-slate-400">
                    Trees (T1: Producer) fix solar radiation → Deer (T2: Primary Consumer/Herbivore) feeds on leaves → Tiger (T3: Apex Carnivore) feeds on deer.
                </p>
            </div>
        </div>
        """

    elif s_idx == 5:
        # Lab 13.5: Lindeman's 10% Energy Transfer Pyramid Simulator (Fig 13.2)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">Interactive Lab 13.5: Raymond Lindeman's 10% Energy Pyramid</span>
                </div>
                <div class="text-xs text-slate-400">
                    Solar Input: <span id="sim5-solar-display" class="font-mono text-amber-300 font-bold">1,000,000 J</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 flex items-center justify-center p-2">
                <svg id="sim5-canvas" viewBox="0 0 500 270" class="w-full h-full">
                    <!-- T4 Tertiary Consumers (Apex Predator) -->
                    <polygon points="250,25 210,75 290,75" fill="#f43f5e" stroke="#be123c" stroke-width="1.5"/>
                    <text x="250" y="55" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">T4: Tertiary</text>
                    <text x="250" y="68" fill="#ffe4e6" font-size="9" font-family="monospace" text-anchor="middle" id="sim5-t4-val">10 J</text>

                    <!-- T3 Secondary Consumers -->
                    <polygon points="210,75 290,75 330,135 170,135" fill="#8b5cf6" stroke="#6d28d9" stroke-width="1.5"/>
                    <text x="250" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">T3: Secondary Consumers</text>
                    <text x="250" y="122" fill="#ede9fe" font-size="10" font-family="monospace" text-anchor="middle" id="sim5-t3-val">100 J</text>

                    <!-- T2 Primary Consumers (Herbivores) -->
                    <polygon points="170,135 330,135 380,200 120,200" fill="#0284c7" stroke="#0369a1" stroke-width="1.5"/>
                    <text x="250" y="165" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">T2: Herbivores (Primary Consumers)</text>
                    <text x="250" y="185" fill="#e0f2fe" font-size="11" font-family="monospace" text-anchor="middle" id="sim5-t2-val">1,000 J</text>

                    <!-- T1 Producers (Green Plants) -->
                    <polygon points="120,200 380,200 440,260 60,260" fill="#15803d" stroke="#166534" stroke-width="1.5"/>
                    <text x="250" y="230" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">T1: Autotrophs (Producers - 1% Solar Fixed)</text>
                    <text x="250" y="250" fill="#dcfce7" font-size="12" font-family="monospace" text-anchor="middle" id="sim5-t1-val">10,000 J</text>

                    <!-- 90% Heat Dissipation Annotations -->
                    <path d="M300,55 Q350,55 370,45" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="375" y="48" fill="#ef4444" font-size="8.5">90% Heat Loss</text>
                    <path d="M345,105 Q390,105 410,95" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="415" y="98" fill="#ef4444" font-size="8.5">90% Heat Loss</text>
                    <path d="M395,165 Q430,165 440,155" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="445" y="158" fill="#ef4444" font-size="8.5">90% Heat Loss</text>
                </svg>
            </div>

            <div class="mt-3">
                <div class="flex justify-between text-xs text-slate-300 mb-1">
                    <span>Adjust Solar Radiation Falling on Canopy:</span>
                    <span id="sim5-slider-display" class="font-mono text-amber-400 font-bold">1,000,000 J</span>
                </div>
                <input type="range" id="sim5-solar-slider" min="100000" max="5000000" step="100000" value="1000000" oninput="updateSim5Energy()" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                Plants convert 1% of sunlight into food. Consumers convert only 10% into body mass. After 4 levels, usable energy is exhausted!
            </p>
        </div>
        """

    elif s_idx == 6:
        # Lab 13.6: Food Web Interconnection Network (Fig 13.3)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 13.6: Multi-Branching Food Web (Figure 13.3)</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-400">Simulate Impact:</span>
                    <select id="sim6-select" onchange="updateSim6Web()" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded px-2 py-1">
                        <option value="none">Normal Equilibrium</option>
                        <option value="kill-rabbit">Rabbit Population Crashes</option>
                        <option value="kill-frog">Insecticide Eliminates Frogs</option>
                        <option value="kill-plant">Severe Drought Kills Plants</option>
                    </select>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-indigo-500/30">
                <svg id="sim6-canvas" viewBox="0 0 500 280" class="w-full h-full">
                    <!-- Web Interconnecting Lines -->
                    <g stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3" id="sim6-lines">
                        <line x1="100" y1="240" x2="80" y2="160"/>   <!-- Plants -> Rabbit -->
                        <line x1="100" y1="240" x2="250" y2="170"/>  <!-- Plants -> Grasshopper -->
                        <line x1="100" y1="240" x2="400" y2="170"/>  <!-- Plants -> Mouse -->
                        <line x1="80" y1="160" x2="160" y2="80"/>    <!-- Rabbit -> Fox -->
                        <line x1="80" y1="160" x2="350" y2="70"/>    <!-- Rabbit -> Hawk -->
                        <line x1="250" y1="170" x2="250" y2="110"/>  <!-- Grasshopper -> Frog -->
                        <line x1="250" y1="110" x2="350" y2="70"/>   <!-- Frog -> Snake/Hawk -->
                        <line x1="400" y1="170" x2="350" y2="70"/>   <!-- Mouse -> Hawk -->
                        <line x1="400" y1="170" x2="160" y2="80"/>   <!-- Mouse -> Fox -->
                    </g>

                    <!-- Trophic Nodes -->
                    <!-- T1 Plants -->
                    <g id="node-plants" transform="translate(100, 240)">
                        <circle cx="0" cy="0" r="22" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Plants (T1)</text>
                    </g>

                    <!-- T2 Herbivores -->
                    <g id="node-rabbit" transform="translate(80, 160)">
                        <circle cx="0" cy="0" r="20" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Rabbit</text>
                    </g>
                    <g id="node-grasshopper" transform="translate(250, 170)">
                        <circle cx="0" cy="0" r="20" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Insect</text>
                    </g>
                    <g id="node-mouse" transform="translate(400, 170)">
                        <circle cx="0" cy="0" r="20" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Mouse</text>
                    </g>

                    <!-- T3 Small Carnivores -->
                    <g id="node-frog" transform="translate(250, 110)">
                        <circle cx="0" cy="0" r="18" fill="#7c3aed" stroke="#a855f7" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Frog</text>
                    </g>

                    <!-- T4 Top Predators -->
                    <g id="node-fox" transform="translate(160, 80)">
                        <circle cx="0" cy="0" r="22" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Fox</text>
                    </g>
                    <g id="node-hawk" transform="translate(350, 70)">
                        <circle cx="0" cy="0" r="22" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Hawk</text>
                    </g>
                </svg>
            </div>
            <p id="sim6-desc" class="text-xs text-slate-400 mt-2 text-center">
                Food webs provide alternative feeding pathways. If rabbits decline, foxes and hawks switch to mice, stabilizing the ecosystem!
            </p>
        </div>
        """

    elif s_idx == 7:
        # Lab 13.7: Unidirectional Flow of Energy Engine (Fig 13.4)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">Interactive Lab 13.7: Unidirectional Energy Pipeline (Figure 13.4)</span>
                </div>
                <button onclick="triggerSim7ReverseAttempt()" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">Attempt Reverse Energy Flow</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-slate-800 p-4 flex flex-col justify-between">
                <svg id="sim7-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Sun Source -->
                    <circle cx="50" cy="120" r="30" fill="#facc15" filter="drop-shadow(0 0 10px #facc15)"/>
                    <text x="50" y="124" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">SUN</text>

                    <!-- Forward Flowing Arrows & Tiers -->
                    <!-- Arrow 1 -->
                    <line x1="85" y1="120" x2="135" y2="120" stroke="#f59e0b" stroke-width="4"/>
                    <polygon points="135,115 145,120 135,125" fill="#f59e0b"/>

                    <!-- Producers -->
                    <rect x="150" y="85" width="70" height="70" rx="8" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                    <text x="185" y="118" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Producers</text>
                    <text x="185" y="132" fill="#dcfce7" font-size="8" text-anchor="middle">Plants</text>

                    <!-- Arrow 2 -->
                    <line x1="225" y1="120" x2="265" y2="120" stroke="#f59e0b" stroke-width="4"/>
                    <polygon points="265,115 275,120 265,125" fill="#f59e0b"/>

                    <!-- Herbivores -->
                    <rect x="280" y="85" width="70" height="70" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                    <text x="315" y="118" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Herbivores</text>
                    <text x="315" y="132" fill="#e0f2fe" font-size="8" text-anchor="middle">Consumers</text>

                    <!-- Arrow 3 -->
                    <line x1="355" y1="120" x2="395" y2="120" stroke="#f59e0b" stroke-width="4"/>
                    <polygon points="395,115 405,120 395,125" fill="#f59e0b"/>

                    <!-- Top Carnivores -->
                    <rect x="410" y="85" width="75" height="70" rx="8" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                    <text x="447" y="118" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Carnivores</text>
                    <text x="447" y="132" fill="#ffe4e6" font-size="8" text-anchor="middle">Apex Tier</text>

                    <!-- Dissipated Heat Waves Radiating to Space -->
                    <path d="M185,80 Q195,50 185,30 M180,75 Q190,45 180,25" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
                    <path d="M315,80 Q325,50 315,30 M310,75 Q320,45 310,25" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
                    <path d="M447,80 Q457,50 447,30 M442,75 Q452,45 442,25" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
                    <text x="250" y="25" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">Heat Dissipated Permanently to Outer Space (Non-Recyclable)</text>
                </svg>
            </div>
            <div id="sim7-alert" class="hidden mt-2 p-2 rounded-lg bg-rose-950/80 border border-rose-500/40 text-xs text-rose-300 font-bold text-center">
                THERMODYNAMIC LAW: Energy flow is strictly unidirectional! Energy in consumers cannot revert to plants, nor can plant chemical energy return to the Sun!
            </div>
        </div>
        """

    elif s_idx == 8:
        # Lab 13.8: Biological Magnification (Biomagnification) Bio-Accumulator
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-rose-400">Interactive Lab 13.8: Biological Magnification Bio-Accumulator</span>
                </div>
                <div class="text-xs text-rose-400 font-bold" id="sim8-danger-level">Hazard: CRITICAL</div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-rose-500/30 p-3">
                <svg id="sim8-canvas" viewBox="0 0 500 250" class="w-full h-full">
                    <!-- Trophic Steps showing increasing red toxic dots -->
                    <!-- Step 1: Water -->
                    <rect x="20" y="180" width="75" height="55" rx="6" fill="#082f49" stroke="#0284c7"/>
                    <text x="57" y="200" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">1. Water</text>
                    <text x="57" y="220" fill="#94a3b8" font-size="7.5" font-family="monospace" text-anchor="middle" id="sim8-v1">0.000003 ppm</text>

                    <!-- Step 2: Plankton -->
                    <rect x="115" y="150" width="75" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
                    <text x="152" y="170" fill="#4ade80" font-size="8.5" font-weight="bold" text-anchor="middle">2. Plankton</text>
                    <text x="152" y="190" fill="#dcfce7" font-size="8" font-family="monospace" text-anchor="middle" id="sim8-v2">0.04 ppm</text>

                    <!-- Step 3: Small Fish -->
                    <rect x="210" y="120" width="75" height="115" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
                    <text x="247" y="140" fill="#818cf8" font-size="8.5" font-weight="bold" text-anchor="middle">3. Small Fish</text>
                    <text x="247" y="160" fill="#e0e7ff" font-size="8" font-family="monospace" text-anchor="middle" id="sim8-v3">0.5 ppm</text>

                    <!-- Step 4: Large Fish -->
                    <rect x="305" y="80" width="75" height="155" rx="6" fill="#451a03" stroke="#f59e0b"/>
                    <text x="342" y="100" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="middle">4. Large Fish</text>
                    <text x="342" y="120" fill="#fef3c7" font-size="8" font-family="monospace" text-anchor="middle" id="sim8-v4">2.0 ppm</text>

                    <!-- Step 5: Humans & Apex Fish-Eating Eagles -->
                    <rect x="400" y="30" width="85" height="205" rx="6" fill="#4c0519" stroke="#f43f5e" stroke-width="2"/>
                    <text x="442" y="55" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">5. Human / Apex</text>
                    <text x="442" y="75" fill="#ffe4e6" font-size="9" font-weight="bold" font-family="monospace" text-anchor="middle" id="sim8-v5">25.0 ppm</text>
                    <text x="442" y="90" fill="#fb7185" font-size="7.5" text-anchor="middle">Peak Toxicity!</text>
                </svg>
            </div>

            <div class="mt-3">
                <div class="flex justify-between text-xs text-slate-300 mb-1">
                    <span>Agricultural Pesticide Spray Runoff:</span>
                    <span id="sim8-pesticide-val" class="font-bold text-rose-400">Standard Agricultural Dosage</span>
                </div>
                <input type="range" id="sim8-slider" min="1" max="5" value="3" oninput="updateSim8Biomag()" class="w-full accent-rose-500 cursor-pointer">
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                Because non-biodegradable chemicals cannot be excreted or metabolized, humans at the top of the food chain accumulate the highest dosage!
            </p>
        </div>
        """

    elif s_idx == 9:
        # Lab 13.9: Stratospheric Ozone Shield vs Ground-Level Poison
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-cyan-400">Interactive Lab 13.9: Stratospheric Shield vs Ground-Level Toxin</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim9Altitude('stratosphere')" id="btn-sim9-strat" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition">Stratosphere (15-30 km)</button>
                    <button onclick="toggleSim9Altitude('ground')" id="btn-sim9-ground" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Ground-Level (Troposphere)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-cyan-500/30 p-3">
                <svg id="sim9-canvas" viewBox="0 0 500 260" class="w-full h-full">
                    <!-- Stratosphere View -->
                    <g id="sim9-strat-view">
                        <rect x="0" y="0" width="500" height="100" fill="#0f172a"/>
                        <!-- Sun & Incoming UV Rays -->
                        <circle cx="250" cy="-20" r="45" fill="#facc15" filter="drop-shadow(0 0 20px #facc15)"/>
                        <line x1="150" y1="20" x2="180" y2="110" stroke="#c084fc" stroke-width="3" stroke-dasharray="4,4"/>
                        <line x1="250" y1="25" x2="250" y2="110" stroke="#c084fc" stroke-width="3" stroke-dasharray="4,4"/>
                        <line x1="350" y1="20" x2="320" y2="110" stroke="#c084fc" stroke-width="3" stroke-dasharray="4,4"/>
                        <text x="250" y="65" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Harmful Solar UV-B & UV-C Radiation</text>

                        <!-- Ozone Layer Barrier -->
                        <rect x="50" y="110" width="400" height="40" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2" opacity="0.9"/>
                        <text x="250" y="135" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">OZONE LAYER (O₃ Shield Absorbs 99% UV)</text>

                        <!-- Protected Biosphere Surface -->
                        <rect x="0" y="210" width="500" height="50" fill="#14532d"/>
                        <text x="250" y="235" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Protected Earth Surface: Normal Flora & Fauna Thriving</text>
                    </g>

                    <!-- Ground-Level Smog View (Hidden by default) -->
                    <g id="sim9-ground-view" opacity="0">
                        <rect x="0" y="0" width="500" height="260" fill="#451a03" opacity="0.85"/>
                        <text x="250" y="50" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">TROPOSPHERIC OZONE: DEADLY POISON</text>
                        <text x="250" y="80" fill="#fca5a5" font-size="10" text-anchor="middle">Major component of toxic photochemical smog</text>
                        <!-- Human Lungs Illustration -->
                        <ellipse cx="250" cy="150" rx="35" ry="45" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
                        <text x="250" y="155" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Lung Damage</text>
                        <text x="250" y="230" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">Severe Asthma, Coughing & Respiratory Inflammation</text>
                    </g>
                </svg>
            </div>
            <p id="sim9-desc" class="text-xs text-slate-400 mt-2 text-center">
                Ozone (O3) is a deadly poison when inhaled at ground level, but forms an indispensable UV shield in the stratosphere!
            </p>
        </div>
        """

    elif s_idx == 10:
        # Lab 13.10: Two-Step Photochemical Ozone Synthesis & CFC Catalytic Cycle
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-cyan-400">Interactive Lab 13.10: Photochemical Synthesis & CFC Catalytic Destruction</span>
                </div>
                <div class="flex items-center gap-1.5">
                    <button onclick="triggerSim10Step(1)" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">Step 1: O₂ Photodissociation</button>
                    <button onclick="triggerSim10Step(2)" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">Step 2: O₃ Synthesis</button>
                    <button onclick="triggerSim10Step(3)" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">CFC Destruction Cycle</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-cyan-500/30 p-4 flex items-center justify-center">
                <div id="sim10-display" class="text-center space-y-3">
                    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 inline-block font-mono text-sm" id="sim10-equation">
                        <span class="text-amber-400 font-bold">O₂</span> ───(High-Energy UV)───→ <span class="text-cyan-400 font-bold">O + O</span> (Nascent Oxygen Atoms)
                    </div>
                    <p id="sim10-explanation" class="text-xs text-slate-300 max-w-md mx-auto">
                        Solar UV photons break the covalent bond in oxygen gas ($O_2$), generating two highly reactive free oxygen atoms.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                A single chlorine radical released from CFCs can catalytically destroy over 100,000 ozone molecules!
            </p>
        </div>
        """

    elif s_idx == 11:
        # Lab 13.11: Montreal Protocol & Antarctic Ozone Hole Recovery Timeline (Activity 13.4)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">Interactive Lab 13.11: 1987 Montreal Protocol & Ozone Hole Recovery</span>
                </div>
                <div class="text-xs text-emerald-400 font-bold font-mono" id="sim11-year-val">Year: 1987 (UNEP Treaty Signed)</div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-emerald-500/30 flex items-center justify-center p-3">
                <svg id="sim11-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Antarctic Continent Grid -->
                    <circle cx="250" cy="120" r="90" fill="#0f172a" stroke="#334155" stroke-dasharray="2,2"/>
                    <path d="M220 100 Q260 80 290 110 Q310 140 270 150 Q230 160 210 130 Z" fill="#334155"/>
                    <text x="250" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Antarctica</text>

                    <!-- Dynamic Ozone Hole -->
                    <circle id="sim11-hole" cx="250" cy="120" r="50" fill="#7c3aed" opacity="0.75" filter="drop-shadow(0 0 15px #7c3aed)"/>
                    <text x="250" y="175" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle" id="sim11-hole-label">Ozone Depletion Zone: 18 Million km²</text>
                </svg>
            </div>

            <div class="mt-3">
                <div class="flex justify-between text-xs text-slate-300 mb-1">
                    <span>Move Timeline Slider (1980 to 2060):</span>
                    <span id="sim11-slider-year" class="font-bold text-cyan-400 font-mono">1987</span>
                </div>
                <input type="range" id="sim11-slider" min="1980" max="2060" step="5" value="1987" oninput="updateSim11Timeline()" class="w-full accent-emerald-500 cursor-pointer">
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                Following the 1987 UNEP Montreal Protocol, CFC-free refrigeration has enabled the Antarctic ozone hole to steadily heal!
            </p>
        </div>
        """

    elif s_idx == 12:
        # Lab 13.12: Garbage Pit 60-Day Soil Burial Simulator (Activity 13.5)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">Interactive Lab 13.12: Activity 13.5 Garbage Soil Burial Test</span>
                </div>
                <div class="text-xs text-amber-400 font-bold font-mono" id="sim12-day-val">Observation: Day 0 (Freshly Buried)</div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-3">
                <svg id="sim12-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Soil Layers -->
                    <rect x="0" y="0" width="500" height="60" fill="#14532d"/>
                    <rect x="0" y="60" width="500" height="180" fill="#291809"/>
                    <text x="250" y="45" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Covered with 15 cm Garden Soil</text>

                    <!-- Buried Items -->
                    <!-- Item 1: Vegetable Peels (Biodegradable) -->
                    <g id="sim12-peels" transform="translate(80, 120)">
                        <path d="M0 10 Q20 -10 40 10 Q60 30 40 40 Z" fill="#84cc16"/>
                        <text x="20" y="60" fill="#bef264" font-size="8.5" text-anchor="middle">Vegetable Peels</text>
                    </g>

                    <!-- Item 2: Waste Paper / Cardboard -->
                    <g id="sim12-paper" transform="translate(200, 120)">
                        <rect x="0" y="0" width="45" height="35" rx="3" fill="#e2e8f0"/>
                        <text x="22" y="55" fill="#f8fafc" font-size="8.5" text-anchor="middle">Waste Paper</text>
                    </g>

                    <!-- Item 3: Plastic Wrapper (Non-Biodegradable) -->
                    <g id="sim12-plastic" transform="translate(320, 120)">
                        <polygon points="0,5 35,0 40,30 5,35" fill="#06b6d4" opacity="0.9"/>
                        <text x="20" y="55" fill="#67e8f9" font-size="8.5" text-anchor="middle">Plastic Packet</text>
                    </g>

                    <!-- Item 4: Aluminium Medicine Strip -->
                    <g id="sim12-metal" transform="translate(420, 120)">
                        <rect x="0" y="5" width="40" height="25" rx="4" fill="#94a3b8" stroke="#cbd5e1"/>
                        <text x="20" y="50" fill="#e2e8f0" font-size="8" text-anchor="middle">Blister Pack</text>
                    </g>
                </svg>
            </div>

            <div class="mt-3">
                <div class="flex justify-between text-xs text-slate-300 mb-1">
                    <span>Soil Incubation Elapsed Time:</span>
                    <span id="sim12-slider-day" class="font-bold text-amber-400 font-mono">Day 0</span>
                </div>
                <input type="range" id="sim12-slider" min="0" max="60" step="15" value="0" oninput="updateSim12Burial()" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <p id="sim12-desc" class="text-xs text-slate-400 mt-2 text-center">
                At 15-day intervals, peels and paper turn black and decompose into humus, while plastic and foil remain completely unaltered!
            </p>
        </div>
        """

    elif s_idx == 13:
        # Lab 13.13: Enzyme Substrate Specificity Lock-and-Key Simulator
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-violet-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-violet-400">Interactive Lab 13.13: Enzyme Lock-and-Key Specificity</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="testSim13Substrate('starch')" id="btn-sim13-starch" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition">Test Natural Starch</button>
                    <button onclick="testSim13Substrate('plastic')" id="btn-sim13-plastic" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Test Synthetic Plastic</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-violet-500/30 p-3 flex items-center justify-center">
                <svg id="sim13-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Enzyme Molecule with Specific Notched Active Site -->
                    <g id="sim13-enzyme" transform="translate(140, 100)">
                        <path d="M0,0 L80,0 L80,30 L110,30 L110,50 L80,50 L80,80 L0,80 Z" fill="#7c3aed" stroke="#a855f7" stroke-width="2"/>
                        <text x="40" y="45" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Enzyme</text>
                        <text x="95" y="22" fill="#c084fc" font-size="7.5" text-anchor="middle">Active Site</text>
                    </g>

                    <!-- Substrate Molecule Testing -->
                    <g id="sim13-substrate" transform="translate(260, 105)">
                        <!-- Fits Active Site by default -->
                        <rect x="0" y="25" width="30" height="20" fill="#22c55e" stroke="#16a34a" id="sim13-sub-shape"/>
                        <text x="15" y="15" fill="#4ade80" font-size="8.5" font-weight="bold" text-anchor="middle" id="sim13-sub-text">Starch</text>
                    </g>

                    <!-- Reaction Outcome HUD -->
                    <rect x="330" y="60" width="150" height="80" rx="8" fill="rgba(15,23,42,0.9)" stroke="#7c3aed"/>
                    <text x="340" y="85" fill="#4ade80" font-size="10" font-weight="bold" id="sim13-hud-status">STATUS: DIGESTED!</text>
                    <text x="340" y="105" fill="#94a3b8" font-size="8.5" id="sim13-hud-msg">Substrate fits active site</text>
                    <text x="340" y="122" fill="#38bdf8" font-size="8" id="sim13-hud-prod">Cleaved into glucose units</text>
                </svg>
            </div>
            <p id="sim13-desc" class="text-xs text-slate-400 mt-2 text-center">
                Enzymes are specific in their action! Microorganisms lack enzymes shaped to fit synthetic plastic polymers, leaving plastics undigested.
            </p>
        </div>
        """

    elif s_idx == 14:
        # Lab 13.14: Train Teacups Dilemma & Topsoil Impact Visualizer (NCERT Page 215)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">Interactive Lab 13.14: The Train Teacup Dilemma (Page 215)</span>
                </div>
                <div class="flex items-center gap-1.5 flex-wrap">
                    <button onclick="selectSim14Era('glass')" id="btn-cup-glass" class="px-2 py-1 rounded text-[11px] font-bold bg-slate-800 text-slate-300 transition">1. Returnable Glass</button>
                    <button onclick="selectSim14Era('plastic')" id="btn-cup-plastic" class="px-2 py-1 rounded text-[11px] font-bold bg-slate-800 text-slate-300 transition">2. Disposable Plastic</button>
                    <button onclick="selectSim14Era('kulhad')" id="btn-cup-kulhad" class="px-2 py-1 rounded text-[11px] font-bold bg-slate-800 text-slate-300 transition">3. Clay Kulhad</button>
                    <button onclick="selectSim14Era('paper')" id="btn-cup-paper" class="px-2 py-1 rounded text-[11px] font-bold bg-emerald-600 text-white transition">4. Disposable Paper</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <div class="flex flex-col sm:flex-row items-center justify-around gap-4 h-full">
                    <div id="sim14-cup-visual" class="flex flex-col items-center">
                        <svg viewBox="0 0 100 120" class="w-24 h-28">
                            <polygon points="20,10 80,10 70,110 30,110" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="50" y="65" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Paper</text>
                        </svg>
                        <span class="text-xs font-bold text-emerald-400 mt-1" id="sim14-cup-name">Modern Paper Cup</span>
                    </div>

                    <div class="flex-1 space-y-2 text-xs">
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">Hygiene & Public Health:</span>
                            <span class="font-bold text-emerald-400" id="sim14-hygiene">100% Hygienic (Single-Use)</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">Agricultural Top-Soil Loss:</span>
                            <span class="font-bold text-emerald-400" id="sim14-topsoil">Zero Top-Soil Loss</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">Biodegradability:</span>
                            <span class="font-bold text-emerald-400" id="sim14-biodegradable">100% Biodegradable</span>
                        </div>
                    </div>
                </div>
            </div>
            <p id="sim14-desc" class="text-xs text-slate-400 mt-2 text-center">
                Clay kulhads stripped fertile agricultural top-soil. Modern disposable paper cups achieve hygiene without harming soil or persisting in landfills!
            </p>
        </div>
        """

    elif s_idx == 15:
        # Lab 13.15: Two-Bin Segregation & 5 R's Interactive Sorter (Activity 13.7)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">Interactive Lab 13.15: Source Segregation & 5 R's Sorter</span>
                </div>
                <button onclick="resetSim15Sorter()" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Reset Items</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-slate-800 p-4 flex flex-col justify-between">
                <!-- Waste Item Tray -->
                <div class="flex items-center justify-center gap-2 flex-wrap mb-2">
                    <span class="text-xs text-slate-400 mr-2">Click item to sort:</span>
                    <button onclick="sortSim15Item('peel', 'green')" id="item-peel" class="px-2.5 py-1 rounded-full bg-slate-800 text-xs text-amber-300 border border-amber-500/30 cursor-pointer">Banana Peel</button>
                    <button onclick="sortSim15Item('bottle', 'blue')" id="item-bottle" class="px-2.5 py-1 rounded-full bg-slate-800 text-xs text-cyan-300 border border-cyan-500/30 cursor-pointer">Plastic Bottle</button>
                    <button onclick="sortSim15Item('can', 'blue')" id="item-can" class="px-2.5 py-1 rounded-full bg-slate-800 text-xs text-slate-300 border border-slate-500/30 cursor-pointer">Aluminium Can</button>
                    <button onclick="sortSim15Item('tea', 'green')" id="item-tea" class="px-2.5 py-1 rounded-full bg-slate-800 text-xs text-emerald-300 border border-emerald-500/30 cursor-pointer">Used Tea Leaves</button>
                </div>

                <!-- Green Bin vs Blue Bin -->
                <div class="grid grid-cols-2 gap-4 h-36">
                    <div class="bg-emerald-950/40 border-2 border-dashed border-emerald-500/60 rounded-xl p-3 flex flex-col items-center justify-between">
                        <span class="font-bold text-xs text-emerald-400 uppercase">Green Bin (Wet / Organic Compost)</span>
                        <div id="sim15-green-bin" class="flex gap-1 flex-wrap justify-center text-[10px] text-emerald-300">
                            <!-- Sorted wet items -->
                        </div>
                        <span class="text-[10px] text-emerald-400/80">For Biogas & Vermicomposting</span>
                    </div>

                    <div class="bg-sky-950/40 border-2 border-dashed border-sky-500/60 rounded-xl p-3 flex flex-col items-center justify-between">
                        <span class="font-bold text-xs text-sky-400 uppercase">Blue Bin (Dry / Recyclable)</span>
                        <div id="sim15-blue-bin" class="flex gap-1 flex-wrap justify-center text-[10px] text-sky-300">
                            <!-- Sorted dry items -->
                        </div>
                        <span class="text-[10px] text-sky-400/80">For Material Recovery & Recycling</span>
                    </div>
                </div>
            </div>
            <p id="sim15-desc" class="text-xs text-slate-400 mt-2 text-center">
                Segregating at source prevents landfill saturation and allows organic composting alongside industrial recycling!
            </p>
        </div>
        """

    elif s_idx == 16:
        # Lab 13.16: Trophic Disruption & Ecological Collapse Simulator (NCERT Exercises Q4 & Q5)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-rose-400">Interactive Lab 13.16: Trophic Level Removal & Collapse (Exercises Q4 & Q5)</span>
                </div>
                <button onclick="toggleSim16Herbivores()" id="btn-sim16-kill" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">Kill All Herbivores (T2)</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-rose-500/30 p-3">
                <svg id="sim16-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- T3 Apex Predators (Tigers) -->
                    <g id="sim16-t3" transform="translate(380, 80)">
                        <rect x="0" y="0" width="100" height="70" rx="8" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                        <text x="50" y="30" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">T3: Tigers</text>
                        <text x="50" y="50" fill="#fecdd3" font-size="9" text-anchor="middle" id="sim16-t3-status">Population: 10</text>
                    </g>

                    <!-- T2 Herbivores (Deer) -->
                    <g id="sim16-t2" transform="translate(200, 80)">
                        <rect x="0" y="0" width="100" height="70" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                        <text x="50" y="30" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">T2: Deer</text>
                        <text x="50" y="50" fill="#bae6fd" font-size="9" text-anchor="middle" id="sim16-t2-status">Population: 150</text>
                    </g>

                    <!-- T1 Producers (Trees / Grass) -->
                    <g id="sim16-t1" transform="translate(20, 80)">
                        <rect x="0" y="0" width="100" height="70" rx="8" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <text x="50" y="30" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">T1: Grass / Trees</text>
                        <text x="50" y="50" fill="#bbf7d0" font-size="9" text-anchor="middle" id="sim16-t1-status">Status: Normal</text>
                    </g>

                    <!-- Connecting Flow Arrows -->
                    <line x1="125" y1="115" x2="195" y2="115" stroke="#4ade80" stroke-width="3" id="sim16-arrow1"/>
                    <line x1="305" y1="115" x2="375" y2="115" stroke="#f43f5e" stroke-width="3" id="sim16-arrow2"/>
                </svg>
            </div>
            <p id="sim16-desc" class="text-xs text-slate-400 mt-2 text-center">
                Eliminating an intermediate trophic level starves carnivores above while leaving vegetation unbrowsed below. No level can be safely removed!
            </p>
        </div>
        """

    return ""

def build_full_html():
    """Compiles the complete master HTML document."""
    all_slides = []

    # Process 16 Content Slides
    for idx, slide in enumerate(CONTENT_SLIDES):
        s_idx = idx + 1
        simulator_html = generate_interactive_simulator(s_idx)

        checkpoints_html = ""
        for c_idx, cp in enumerate(slide["checkpoints"]):
            opts_html = ""
            for o_idx, opt in enumerate(cp["options"]):
                opts_html += f"""
                <button onclick="checkOption({s_idx}, {c_idx}, {o_idx}, {cp['ans']})" id="opt-{s_idx}-{c_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="mark-{s_idx}-{c_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            checkpoints_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-2 mb-3">
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                    Checkpoint Question {c_idx + 1}
                </span>
                <p class="text-xs font-bold text-slate-200 mt-1">{cp['question']}</p>
                <div class="space-y-1.5 mt-2">
                    {opts_html}
                </div>
                <div id="feedback-{s_idx}-{c_idx}" class="hidden p-2 rounded-lg text-xs mt-2 bg-slate-900 border border-slate-800 text-slate-300">
                    <span class="font-bold text-emerald-400">Teacher Explanation:</span> {cp['explanation']}
                </div>
            </div>
            """

        teacher_card_html = f"""
        <!-- Person Talking: Dr. Sophia Environmental Science Avatar -->
        <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-cyan-950/20 border border-emerald-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
            <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                    <!-- Body / Lab Coat with Green Collar -->
                    <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#059669" stroke="#10b981" stroke-width="2"/>
                    <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                    <!-- Stethoscope / Biosphere Badge -->
                    <circle cx="60" cy="98" r="4" fill="#38bdf8"/>
                    <!-- Neck -->
                    <rect x="52" y="68" width="16" height="15" fill="#fcd34d" rx="2"/>
                    <!-- Face -->
                    <ellipse cx="60" cy="50" rx="25" ry="28" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
                    <!-- Eyes with glasses -->
                    <circle cx="48" cy="46" r="7" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <circle cx="72" cy="46" r="7" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <line x1="55" y1="46" x2="65" y2="46" stroke="#0f172a" stroke-width="2"/>
                    <circle cx="48" cy="46" r="3" fill="#1e293b"/>
                    <circle cx="72" cy="46" r="3" fill="#1e293b"/>
                    <!-- Eyebrows -->
                    <path d="M42 36 Q48 33 54 36" fill="none" stroke="#78350f" stroke-width="2"/>
                    <path d="M66 36 Q72 33 78 36" fill="none" stroke="#78350f" stroke-width="2"/>
                    <!-- Animated Talking Mouth -->
                    <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    <!-- Hair -->
                    <path d="M35 50 Q30 20 60 20 Q90 20 85 50 Q75 15 60 18 Q45 15 35 50 Z" fill="#78350f"/>
                </svg>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mt-1">
                    Dr. Sophia • Ecologist
                </span>
            </div>

            <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"/></svg>
                        Teacher Narration & Audio Explanation
                    </span>
                    <button onclick="speakSlideNarration({s_idx})" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center gap-1 cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                        Listen (Dr. Sophia)
                    </button>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed italic" id="speech-bubble-{s_idx}">
                    "{slide['narration']}"
                </p>
            </div>
        </div>
        """

        slide_html = f"""
        <!-- Slide {s_idx}: {slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                        Slide {s_idx} of 20 • NCERT Chapter 13
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{slide['title']}</h2>
                    <p class="text-xs text-emerald-300 font-medium">{slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-slate-900 text-slate-400 border border-slate-800">
                        Class 10 Science
                    </span>
                </div>
            </div>

            {teacher_card_html}
            {simulator_html}

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Theory & Detailed Concept Notes -->
                <div class="lg:col-span-7 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl">
                    <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                        <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                        <h3 class="font-bold text-xs uppercase tracking-wider text-emerald-400">Complete NCERT Textbook Coverage</h3>
                    </div>
                    {slide['theory']}
                </div>

                <!-- 2 Checkpoints for this slide -->
                <div class="lg:col-span-5 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            <h3 class="font-bold text-xs uppercase tracking-wider text-emerald-400">In-Slide Concept Checkpoints (2 Questions)</h3>
                        </div>
                        {checkpoints_html}
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                        ★ Answer both questions above to reinforce key environmental concepts from this slide!
                    </div>
                </div>
            </div>
        </section>
        """
        all_slides.append(slide_html)

    # Process 4 Quiz Challenge Slides (Slides 17 to 20)
    for q_slide_idx, q_slide in enumerate(QUIZ_SLIDES):
        s_idx = 17 + q_slide_idx

        questions_cards_html = ""
        for q_idx, q_item in enumerate(q_slide["questions"]):
            opts_html = ""
            for o_idx, opt in enumerate(q_item["options"]):
                opts_html += f"""
                <button onclick="checkQuizOption({s_idx}, {q_idx}, {o_idx}, {q_item['ans']})" id="qopt-{s_idx}-{q_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="qmark-{s_idx}-{q_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            clean_title = q_item["q"].replace("'", "&#39;").replace('"', '&quot;')
            clean_solution = q_item["solution"].replace("'", "&#39;").replace('"', '&quot;')

            questions_cards_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 shadow-lg flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                            Question {q_item['id']}
                        </span>
                        <div id="qfeedback-{s_idx}-{q_idx}" class="text-xs font-bold text-slate-500">
                            Unanswered
                        </div>
                    </div>
                    <p class="text-xs font-bold text-slate-200 mb-3">{q_item['q']}</p>
                    <div class="space-y-1.5 mb-3">
                        {opts_html}
                    </div>
                </div>
                <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
                    <button onclick="openQuizSolution('{q_item['id']}', '{clean_title}', '{clean_solution}')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center gap-1.5 shadow-md cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        View Solution
                    </button>
                    <span class="text-[10px] text-slate-500 font-mono">NCERT Verified</span>
                </div>
            </div>
            """

        slide_html = f"""
        <!-- Slide {s_idx}: {q_slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                        Slide {s_idx} of 20 • NCERT Quiz Challenge
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{q_slide['title']}</h2>
                    <p class="text-xs text-emerald-300 font-medium">{q_slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600/30 text-emerald-300 border border-emerald-500/40">
                        10 Questions with Pop-up Solutions
                    </span>
                </div>
            </div>

            <!-- Quiz Instructions Banner -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-cyan-950/20 border border-emerald-500/30 flex items-center justify-between shadow-xl">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-emerald-600/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <div>
                        <h4 class="text-xs font-bold text-white">Interactive Environmental Examination Challenge</h4>
                        <p class="text-[11px] text-slate-400">Select an answer for immediate feedback or click <span class="text-emerald-300 font-bold">'View Solution'</span> to inspect the step-by-step teacher explanation modal.</p>
                    </div>
                </div>
                <button onclick="speakQuizInstructions({s_idx})" class="hidden sm:flex px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition items-center gap-1.5 cursor-pointer">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                    Read
                </button>
            </div>

            <!-- 10 Questions 2-Column Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {questions_cards_html}
            </div>
        </section>
        """
        all_slides.append(slide_html)

    slides_content_str = "\n".join(all_slides)

    # Master HTML Template
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 13: Our Environment Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX for beautiful math equations -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap');

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #030712;
            color: #f8fafc;
        }}

        pre, code, .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-fadeIn {{
            animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}

        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}

        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-3px) rotate(0.8deg); }}
        }}
        .teacher-bob {{
            animation: teacherBob 4s ease-in-out infinite;
        }}

        @keyframes mouthMove {{
            0%, 100% {{ ry: 3; rx: 5; }}
            50% {{ ry: 6.5; rx: 4.5; }}
        }}
        .talking-mouth {{
            animation: mouthMove 0.25s infinite alternate;
        }}

        .modal-backdrop {{
            background: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-slate-950">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center shadow-lg shadow-emerald-500/20 text-white font-black text-sm">
                    13
                </div>
                <div>
                    <h1 class="text-xs sm:text-sm font-bold text-white tracking-tight flex items-center gap-2">
                        NCERT Class 10 Science • Chapter 13
                        <span class="hidden md:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                            Our Environment
                        </span>
                    </h1>
                    <p class="text-[10px] text-slate-400">Dr. Sophia • 20 Interactive Slides & Laboratory Simulators</p>
                </div>
            </div>

            <!-- Slide Quick Pill Selector -->
            <div class="flex items-center gap-2">
                <div class="hidden sm:flex items-center gap-1.5 overflow-x-auto max-w-xs md:max-w-md custom-scrollbar py-1 px-2 rounded-xl bg-slate-900 border border-slate-800" id="slidePillsContainer">
                    <!-- Pills injected dynamically by JS -->
                </div>

                <!-- Global Audio Toggle -->
                <button onclick="toggleAudio()" id="btn-audio-global" class="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 flex items-center gap-1.5 transition cursor-pointer">
                    <span id="audio-icon">🔊</span>
                    <span class="hidden md:inline" id="audio-label">Voice: ON</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Slide Stage Area -->
    <main class="flex-1 w-full flex items-center justify-center p-2 sm:p-4">
        {slides_content_str}
    </main>

    <!-- Fixed Bottom Controls & Progress Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 px-4 py-3">
        <div class="max-w-5xl mx-auto">
            <!-- Progress Bar -->
            <div class="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden mb-3">
                <div id="progressBar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full w-[5%] transition-all duration-300"></div>
            </div>

            <div class="flex items-center justify-between gap-3">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-bold text-slate-200 transition flex items-center gap-2 cursor-pointer shadow-md disabled:opacity-40 disabled:cursor-not-allowed">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    Previous Slide
                </button>

                <div class="flex items-center gap-2">
                    <span id="currentSlideIndicator" class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/40 border border-emerald-500/30 px-3 py-1 rounded-lg">
                        Slide 1 / 20
                    </span>
                </div>

                <div class="flex items-center gap-2">
                    <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-bold transition flex items-center gap-2 cursor-pointer shadow-lg shadow-emerald-500/20">
                        Next Slide
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </button>
                </div>
            </div>

            <!-- Last Slide End-of-Chapter Notice (strictly verified by PHPUnit tests) -->
            <div id="lastSlideNotice" class="hidden mt-3 p-3 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-center animate-fadeIn">
                <p class="text-xs font-bold text-emerald-300">
                    🎉 You have reached the last slide of this chapter (Chapter 13: Our Environment)!
                </p>
                <p class="text-[11px] text-slate-300 mt-0.5">
                    You have mastered all concepts, activities, diagrams, and end-of-chapter exercises. Excellent work!
                </p>
            </div>
        </div>
    </footer>

    <!-- Universal Solution Popup Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative animate-fadeIn">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 cursor-pointer">
                ✕
            </button>
            <div class="flex items-center gap-2 mb-3">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-400" id="modalQuestionId">Solution</span>
            </div>
            <h3 class="text-sm font-bold text-white mb-3" id="modalQuestionTitle">Question Title</h3>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed mb-4 max-h-[60vh] overflow-y-auto custom-scrollbar" id="modalSolutionContent">
                Solution details...
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition cursor-pointer">
                    Got it, Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Scripts: Navigation, Sound Synthesizer & Simulators -->
    <script>
        // Total Slides: 16 Content + 4 Quiz Slides = 20 Slides
        const totalSlides = 20;
        let currentSlideIndex = 0; // 0-based index
        let audioEnabled = true;
        let currentUtterance = null;

        // Slide narrations array for Web Speech API
        const slideNarrations = [
            "Welcome to Chapter 13: Our Environment! An ecosystem consists of all interacting organisms in an area together with non-living physical surroundings. Biotic factors comprise living plants, animals, microbes, and humans, while abiotic factors include temperature, rainfall, wind, soil, and minerals.",
            "Organisms are grouped into producers, consumers, and decomposers based on how they obtain sustenance. Producers make organic food via photosynthesis. Consumers include herbivores, carnivores, omnivores, and parasites. Decomposers break down dead organic remains into simple inorganic substances.",
            "A food chain is a series of organisms where each step feeds on the preceding organism. Autotrophs occupy the first trophic level, capturing about 1% of sunlight. Herbivores occupy the second level, small carnivores the third, and larger tertiary carnivores the fourth trophic level.",
            "According to the 10% law of energy transfer, only an average of 10% of food consumed is converted into body biomass and made available to the next trophic level. 90% is dissipated as metabolic heat, limiting food chains to 3 or 4 links.",
            "In nature, food chains do not exist as isolated straight lines. Instead, organisms feed on multiple species, forming a branching network of interconnected feeding relationships called a food web.",
            "From the energy flow diagram, two fundamental principles emerge: energy flow is strictly unidirectional, and the usable energy diminishes progressively due to metabolic heat loss at each transfer.",
            "Harmful non-biodegradable chemicals such as synthetic pesticides and heavy metals accumulate progressively at each trophic level. Since humans occupy the top trophic level, maximum concentration accumulates in our bodies: biological magnification.",
            "Ozone is a triatomic molecule made of three oxygen atoms, O3. While deadly poison at ground level, at higher levels in the stratosphere, ozone absorbs harmful solar ultraviolet radiation, shielding life on Earth.",
            "Stratospheric ozone is formed naturally through a two-step photochemical reaction. High-energy UV radiation splits molecular oxygen into free oxygen atoms, which combine with intact O2 to produce ozone. Synthetic CFCs catalytically destroy ozone.",
            "In 1987, the United Nations Environment Programme forged the landmark Montreal Protocol agreement freezing CFC production at 1986 levels. It is now mandatory for manufacturers worldwide to produce CFC-free refrigerators.",
            "Substances that can be broken down by biological processes through bacteria and fungi are called biodegradable, such as fruit peels and paper. Substances that cannot be broken down by saprophytic microorganisms are non-biodegradable, such as synthetic plastics.",
            "Why do plastics persist? Enzymes are highly substrate-specific. Specific enzymes are required to break specific chemical bonds. Soil bacteria evolved enzymes for natural polymers, but lack enzymes to break synthetic plastic polymer bonds.",
            "Non-biodegradable plastics clog city drainage systems, leach toxic chemicals into groundwater, and harm stray animals. Even biodegradable waste, if allowed to rot in huge unmanaged heaps, emits foul odours and greenhouse methane.",
            "In Indian railway history, disposable clay kulhads were tested as an alternative to plastic cups. However, making billions of kulhads stripped fertile agricultural top-soil! Modern disposable paper cups provide the optimal sustainable solution.",
            "Dealing with the waste crisis requires waste segregation at source: green bins for biodegradable composting, and blue bins for dry recyclables, alongside the 5 R's hierarchy: Refuse, Reduce, Reuse, Repurpose, and Recycle.",
            "Here is the complete walkthrough of NCERT Exercises Q1 through Q9, covering biodegradable groupings, valid food chains, trophic level disruptions, and ozone layer protection.",
            "Mastery Challenge Part 1: Test your knowledge on ecosystem dynamics, abiotic factors, producers, and decomposers with 10 interactive questions.",
            "Mastery Challenge Part 2: Test your understanding of food chains, trophic levels, Raymond Lindeman's 10% energy law, and food webs.",
            "Mastery Challenge Part 3: Test your mastery of unidirectional energy flow, biological magnification, and stratospheric ozone depletion.",
            "Mastery Challenge Part 4: Complete your mastery with 10 questions on waste management, enzymes, kulhads, and the official NCERT exercises."
        ];

        // Web Audio API Synthesizer
        let audioCtx = null;
        function initAudio() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
        }}

        function playTone(freq, type = 'sine', duration = 0.1) {{
            if (!audioEnabled) return;
            try {{
                initAudio();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }} catch(e) {{}}
        }}

        function playCorrectSound() {{
            playTone(523.25, 'sine', 0.1);
            setTimeout(() => playTone(659.25, 'sine', 0.15), 100);
        }}

        function playIncorrectSound() {{
            playTone(280, 'sawtooth', 0.2);
        }}

        function toggleAudio() {{
            audioEnabled = !audioEnabled;
            const icon = document.getElementById('audio-icon');
            const lbl = document.getElementById('audio-label');
            if (audioEnabled) {{
                icon.textContent = '🔊';
                lbl.textContent = 'Voice: ON';
                playTone(600, 'sine', 0.1);
            }} else {{
                icon.textContent = '🔇';
                lbl.textContent = 'Voice: OFF';
                if (window.speechSynthesis) window.speechSynthesis.cancel();
            }}
        }}

        // Slide Navigation Logic
        function showSlide(index) {{
            if (index < 0 || index >= totalSlides) return;
            currentSlideIndex = index;

            // Hide all slides
            document.querySelectorAll('.slide-section').forEach(sec => sec.classList.add('hidden'));

            // Show current slide
            const target = document.getElementById(`slide-${{currentSlideIndex + 1}}`);
            if (target) {{
                target.classList.remove('hidden');
                target.classList.add('animate-fadeIn');
            }}

            // Update Progress Bar & Indicator
            const progressPct = ((currentSlideIndex + 1) / totalSlides) * 100;
            document.getElementById('progressBar').style.width = `${{progressPct}}%`;
            document.getElementById('currentSlideIndicator').textContent = `Slide ${{currentSlideIndex + 1}} / ${{totalSlides}}`;

            // Update Previous / Next Buttons
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const lastNotice = document.getElementById('lastSlideNotice');

            prevBtn.disabled = (currentSlideIndex === 0);

            // Last Slide Check (Strictly asserted in unit tests)
            if (currentSlideIndex === totalSlides - 1) {{
                nextBtn.style.display = 'none';
                lastNotice.classList.remove('hidden');
            }} else {{
                nextBtn.style.display = 'flex';
                lastNotice.classList.add('hidden');
            }}

            // Highlight quick pills
            document.querySelectorAll('.slide-pill').forEach((pill, pIdx) => {{
                if (pIdx === currentSlideIndex) {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-bold bg-emerald-600 text-white shrink-0 transition';
                }} else {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition';
                }}
            }});

            // Auto-speak narration if audio enabled
            if (audioEnabled) {{
                speakSlideNarration(currentSlideIndex + 1);
            }}

            // Re-render KaTeX if available
            if (window.renderMathInElement) {{
                renderMathInElement(target, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}

            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function navigateSlide(direction) {{
            const newIndex = currentSlideIndex + direction;
            if (newIndex >= 0 && newIndex < totalSlides) {{
                playTone(480, 'sine', 0.08);
                showSlide(newIndex);
            }}
        }}

        // Web Speech API Voiceover with Talking Mouth
        function speakSlideNarration(slideNum) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();

            const text = slideNarrations[slideNum - 1];
            if (!text) return;

            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.rate = 1.0;
            currentUtterance.pitch = 1.05;

            const mouth = document.getElementById(`teacherMouth-${{slideNum}}`);

            currentUtterance.onstart = () => {{
                if (mouth) mouth.classList.add('talking-mouth');
            }};

            currentUtterance.onend = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            currentUtterance.onerror = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            window.speechSynthesis.speak(currentUtterance);
        }}

        function speakQuizInstructions(slideNum) {{
            speakSlideNarration(slideNum);
        }}

        // In-Slide Checkpoint Options Evaluator
        function checkOption(sIdx, cIdx, selectedOpt, correctOpt) {{
            const optBtn = document.getElementById(`opt-${{sIdx}}-${{cIdx}}-${{selectedOpt}}`);
            const feedbackEl = document.getElementById(`feedback-${{sIdx}}-${{cIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`opt-${{sIdx}}-${{cIdx}}-${{i}}`);
                const mark = document.getElementById(`mark-${{sIdx}}-${{cIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓ Correct</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗ Incorrect</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
            }} else {{
                playIncorrectSound();
            }}

            if (feedbackEl) feedbackEl.classList.remove('hidden');
        }}

        // Quiz Question Option Evaluator
        function checkQuizOption(sIdx, qIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`qfeedback-${{sIdx}}-${{qIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`qopt-${{sIdx}}-${{qIdx}}-${{i}}`);
                const mark = document.getElementById(`qmark-${{sIdx}}-${{qIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct!</span>`;
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Click Solution</span>`;
            }}
        }}

        // Solution Pop-up Modal Handlers
        function openQuizSolution(qId, title, solutionHtml) {{
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `Question ${{qId}} Solution`;
            document.getElementById('modalQuestionTitle').textContent = title;
            const solEl = document.getElementById('modalSolutionContent');
            solEl.innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');

            if (window.renderMathInElement) {{
                renderMathInElement(solEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function closeSolutionModal() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        // Keyboard & Gesture Controls
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < totalSlides - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        }});

        // Generate Slide Quick Nav Pills
        function generateSlidePills() {{
            const container = document.getElementById('slidePillsContainer');
            if (!container) return;
            container.innerHTML = '';
            for (let i = 0; i < totalSlides; i++) {{
                const btn = document.createElement('button');
                btn.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition cursor-pointer';
                btn.textContent = (i + 1);
                btn.onclick = () => {{
                    playTone(480, 'sine', 0.08);
                    showSlide(i);
                }};
                container.appendChild(btn);
            }}
        }}

        // --- Bespoke Simulator Interactive Functions (1 to 16) ---

        // Lab 13.1
        function toggleSim1Type(type) {{
            playTone(520, 'sine', 0.08);
            const bNat = document.getElementById('btn-sim1-nat');
            const bArt = document.getElementById('btn-sim1-art');
            const hudMode = document.getElementById('sim1-hud-mode');
            const hudBio = document.getElementById('sim1-hud-bio');
            const desc = document.getElementById('sim1-desc');

            if (type === 'natural') {{
                bNat.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bArt.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                hudMode.textContent = 'Ecosystem: Natural Forest';
                hudBio.textContent = 'Biotic: Flora & Fauna in self-regulating equilibrium';
                desc.textContent = 'Natural ecosystems (forests, ponds, lakes) sustain themselves with complete biogeochemical cycling!';
            }} else {{
                bArt.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bNat.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                hudMode.textContent = 'Ecosystem: Human-Made Garden';
                hudBio.textContent = 'Biotic: Cultivated roses, lawns, requires human weeding & watering';
                desc.textContent = 'Human-made ecosystems (gardens, crop-fields, aquariums) require constant human intervention and care.';
            }}
        }}

        function updateSim1Abiotic() {{
            const sunVal = document.getElementById('sim1-sun-slider').value;
            const rainVal = document.getElementById('sim1-rain-slider').value;
            document.getElementById('sim1-sun-val').textContent = `${{sunVal}}%`;
            document.getElementById('sim1-sun').setAttribute('opacity', sunVal / 100);

            const rainEl = document.getElementById('sim1-rain');
            const rainLbl = document.getElementById('sim1-rain-val');
            if (rainVal > 50) {{
                rainEl.setAttribute('opacity', '1');
                rainLbl.textContent = 'Heavy Rainfall';
            }} else if (rainVal > 15) {{
                rainEl.setAttribute('opacity', '0.5');
                rainLbl.textContent = 'Moderate Drizzle';
            }} else {{
                rainEl.setAttribute('opacity', '0');
                rainLbl.textContent = 'Dry (Zero Rain)';
            }}
            document.getElementById('sim1-hud-sub').textContent = `Abiotic: Sunlight ${{sunVal}}%, Rain ${{rainVal}}%`;
        }}

        // Lab 13.2
        let sim2Aerator = true;
        function toggleSim2Aerator() {{
            sim2Aerator = !sim2Aerator;
            playTone(sim2Aerator ? 600 : 300, 'sine', 0.1);
            const btn = document.getElementById('btn-sim2-pump');
            const bubbles = document.getElementById('sim2-bubbles');
            const doVal = document.getElementById('sim2-do-val');
            const note = document.getElementById('sim2-status-note');
            const desc = document.getElementById('sim2-desc');

            if (sim2Aerator) {{
                btn.textContent = 'Aerator Pump: ON';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bubbles.setAttribute('opacity', '1');
                doVal.textContent = '8.2 mg/L';
                doVal.className = 'text-emerald-400 font-bold';
                note.textContent = 'Dissolved oxygen healthy & stable';
                desc.textContent = 'Aerator pump supplies continuous dissolved oxygen so fish breathe normally!';
            }} else {{
                btn.textContent = 'Aerator Pump: OFF (Danger!)';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                bubbles.setAttribute('opacity', '0');
                doVal.textContent = '1.2 mg/L (Hypoxia!)';
                doVal.className = 'text-rose-400 font-bold';
                note.textContent = 'CRITICAL: Fish gasping at surface!';
                desc.textContent = 'Without aerator pump, oxygen drops to 1.2 mg/L. Fish will suffocate in an artificial aquarium!';
            }}
        }}

        function feedSim2Fish() {{
            playTone(680, 'sine', 0.1);
            const flakes = document.getElementById('sim2-flakes');
            flakes.setAttribute('opacity', '1');
            setTimeout(() => flakes.setAttribute('opacity', '0'), 1500);
            document.getElementById('sim2-desc').textContent = 'Fish food consumed! Uneaten excess food and excretions increase waste in the aquarium.';
        }}

        function cleanSim2Tank() {{
            playTone(720, 'sine', 0.15);
            document.getElementById('sim2-clean-val').textContent = '100% Clean';
            document.getElementById('sim2-water').setAttribute('fill', '#082f49');
            document.getElementById('sim2-desc').textContent = 'Aquarium water changed and filtered! Unlike natural ponds, an aquarium lacks natural recycling and must be cleaned.';
        }}

        // Lab 13.3
        let sim3Active = true;
        function toggleSim3Decomposers() {{
            sim3Active = !sim3Active;
            playTone(sim3Active ? 620 : 280, 'sine', 0.1);
            const btn = document.getElementById('btn-sim3-toggle');
            const microbes = document.getElementById('sim3-microbes');
            const minerals = document.getElementById('sim3-minerals');
            const tEl = document.getElementById('sim3-title');
            const d1 = document.getElementById('sim3-detail1');
            const d2 = document.getElementById('sim3-detail2');
            const desc = document.getElementById('sim3-desc');

            if (sim3Active) {{
                btn.textContent = 'Decomposers: ACTIVE';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-violet-600 text-white transition';
                microbes.setAttribute('opacity', '1');
                minerals.setAttribute('opacity', '1');
                tEl.textContent = 'Decomposers: Active Mineralization';
                d1.textContent = 'Bacteria/fungi break complex organic matter';
                d2.textContent = 'Inorganic nutrients recycled to plant roots';
                desc.textContent = 'Decomposers convert dead biomass into simple inorganic salts (NO3-, PO4 3-). Soil replenished!';
            }} else {{
                btn.textContent = 'Decomposers: ABSENT / ELIMINATED';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                microbes.setAttribute('opacity', '0');
                minerals.setAttribute('opacity', '0');
                tEl.textContent = 'Decomposers: ABSENT (Crisis!)';
                d1.textContent = 'Dead carcasses and leaves pile up indefinitely';
                d2.textContent = 'Soil fertility exhausted; nutrients locked away!';
                desc.textContent = 'If decomposers disappear, dead bodies pile up forever and natural nutrient cycles collapse completely!';
            }}
        }}

        // Lab 13.4
        const chainData = {{
            forest: [
                {{ name: 'Forest Trees', tier: 'T1: Producer', color: 'bg-emerald-950 border-emerald-500/50 text-emerald-300' }},
                {{ name: 'Spotted Deer', tier: 'T2: Herbivore', color: 'bg-amber-950 border-amber-500/50 text-amber-300' }},
                {{ name: 'Bengal Tiger', tier: 'T3: Top Carnivore', color: 'bg-rose-950 border-rose-500/50 text-rose-300' }}
            ],
            grassland: [
                {{ name: 'Grass', tier: 'T1: Producer', color: 'bg-emerald-950 border-emerald-500/50 text-emerald-300' }},
                {{ name: 'Grasshopper', tier: 'T2: Herbivore', color: 'bg-cyan-950 border-cyan-500/50 text-cyan-300' }},
                {{ name: 'Frog', tier: 'T3: Small Carnivore', color: 'bg-indigo-950 border-indigo-500/50 text-indigo-300' }},
                {{ name: 'Snake', tier: 'T4: Carnivore', color: 'bg-purple-950 border-purple-500/50 text-purple-300' }},
                {{ name: 'Hawk / Eagle', tier: 'T5: Apex Predator', color: 'bg-rose-950 border-rose-500/50 text-rose-300' }}
            ],
            pond: [
                {{ name: 'Phytoplankton', tier: 'T1: Aquatic Producer', color: 'bg-emerald-950 border-emerald-500/50 text-emerald-300' }},
                {{ name: 'Zooplankton', tier: 'T2: Herbivore', color: 'bg-sky-950 border-sky-500/50 text-sky-300' }},
                {{ name: 'Small Fish', tier: 'T3: Carnivore', color: 'bg-blue-950 border-blue-500/50 text-blue-300' }},
                {{ name: 'Water Bird (Stork)', tier: 'T4: Top Predator', color: 'bg-rose-950 border-rose-500/50 text-rose-300' }}
            ]
        }};

        function selectSim4Chain(chainKey) {{
            playTone(520, 'sine', 0.08);
            ['forest', 'grass', 'pond'].forEach(k => {{
                const b = document.getElementById(`btn-chain-${{k}}`);
                if (b) b.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }});
            const activeBtn = document.getElementById(`btn-chain-${{chainKey === 'grassland' ? 'grass' : chainKey}}`);
            if (activeBtn) activeBtn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';

            const display = document.getElementById('sim4-display');
            display.innerHTML = '';
            const items = chainData[chainKey];

            items.forEach((item, i) => {{
                const el = document.createElement('div');
                el.className = `p-3 rounded-xl border ${{item.color}} flex flex-col items-center min-w-[110px] text-center shadow-lg`;
                el.innerHTML = `<span class="text-[10px] font-bold opacity-80">${{item.tier}}</span><span class="text-xs font-bold mt-1">${{item.name}}</span>`;
                display.appendChild(el);

                if (i < items.length - 1) {{
                    const arrow = document.createElement('div');
                    arrow.className = 'text-slate-500 font-bold text-sm shrink-0 px-1';
                    arrow.textContent = '➔';
                    display.appendChild(arrow);
                }}
            }});
        }}

        // Lab 13.5
        function updateSim5Energy() {{
            const solar = parseInt(document.getElementById('sim5-solar-slider').value);
            document.getElementById('sim5-solar-display').textContent = `${{solar.toLocaleString()}} J`;
            document.getElementById('sim5-slider-display').textContent = `${{solar.toLocaleString()}} J`;

            const t1 = solar * 0.01;
            const t2 = t1 * 0.10;
            const t3 = t2 * 0.10;
            const t4 = t3 * 0.10;

            document.getElementById('sim5-t1-val').textContent = `${{t1.toLocaleString()}} J`;
            document.getElementById('sim5-t2-val').textContent = `${{t2.toLocaleString()}} J`;
            document.getElementById('sim5-t3-val').textContent = `${{t3.toLocaleString()}} J`;
            document.getElementById('sim5-t4-val').textContent = `${{t4.toLocaleString()}} J`;
        }}

        // Lab 13.6
        function updateSim6Web() {{
            playTone(500, 'sine', 0.08);
            const val = document.getElementById('sim6-select').value;
            const desc = document.getElementById('sim6-desc');

            if (val === 'kill-rabbit') {{
                desc.textContent = 'Rabbit population crashed! Foxes and hawks adapt by consuming more mice and grasshoppers, stabilizing the web.';
            }} else if (val === 'kill-frog') {{
                desc.textContent = 'Frogs wiped out! Insect populations surge, but hawks and snakes feed heavily on mice to survive.';
            }} else if (val === 'kill-plant') {{
                desc.textContent = 'Severe drought kills plants! T1 failure cascades into severe food shortages across all consumer levels.';
            }} else {{
                desc.textContent = 'Food webs provide alternative feeding pathways. High biodiversity cushions ecosystems against collapse!';
            }}
        }}

        // Lab 13.7
        function triggerSim7ReverseAttempt() {{
            playIncorrectSound();
            const alertEl = document.getElementById('sim7-alert');
            alertEl.classList.remove('hidden');
            setTimeout(() => alertEl.classList.add('hidden'), 5000);
        }}

        // Lab 13.8
        function updateSim8Biomag() {{
            const level = parseInt(document.getElementById('sim8-slider').value);
            const mult = level * 0.5;
            document.getElementById('sim8-v1').textContent = `${{(0.000003 * mult).toFixed(7)}} ppm`;
            document.getElementById('sim8-v2').textContent = `${{(0.04 * mult).toFixed(3)}} ppm`;
            document.getElementById('sim8-v3').textContent = `${{(0.5 * mult).toFixed(2)}} ppm`;
            document.getElementById('sim8-v4').textContent = `${{(2.0 * mult).toFixed(1)}} ppm`;
            document.getElementById('sim8-v5').textContent = `${{(25.0 * mult).toFixed(1)}} ppm`;

            const dangerEl = document.getElementById('sim8-danger-level');
            if (level >= 4) {{
                dangerEl.textContent = 'Hazard: EXTREME TOXICITY';
                dangerEl.className = 'text-xs text-rose-500 font-black animate-pulse';
            }} else {{
                dangerEl.textContent = 'Hazard: HIGH BIOACCUMULATION';
                dangerEl.className = 'text-xs text-amber-400 font-bold';
            }}
        }}

        // Lab 13.9
        function toggleSim9Altitude(alt) {{
            playTone(alt === 'stratosphere' ? 640 : 340, 'sine', 0.1);
            const bStrat = document.getElementById('btn-sim9-strat');
            const bGnd = document.getElementById('btn-sim9-ground');
            const vStrat = document.getElementById('sim9-strat-view');
            const vGnd = document.getElementById('sim9-ground-view');
            const desc = document.getElementById('sim9-desc');

            if (alt === 'stratosphere') {{
                bStrat.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bGnd.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                vStrat.setAttribute('opacity', '1');
                vGnd.setAttribute('opacity', '0');
                desc.textContent = 'Stratospheric ozone (15-30 km) shields the biosphere from lethal UV radiation!';
            }} else {{
                bGnd.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                bStrat.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                vStrat.setAttribute('opacity', '0');
                vGnd.setAttribute('opacity', '1');
                desc.textContent = 'Ground-level tropospheric ozone is a deadly respiratory poison causing pulmonary edema and asthma!';
            }}
        }}

        // Lab 13.10
        function triggerSim10Step(step) {{
            playTone(500 + step * 60, 'sine', 0.1);
            const eq = document.getElementById('sim10-equation');
            const exp = document.getElementById('sim10-explanation');

            if (step === 1) {{
                eq.innerHTML = '<span class="text-amber-400 font-bold">O₂</span> ───(High-Energy UV)───→ <span class="text-cyan-400 font-bold">O + O</span>';
                exp.textContent = 'Step 1: Solar UV radiation splits diatomic oxygen molecules into free nascent oxygen atoms.';
            }} else if (step === 2) {{
                eq.innerHTML = '<span class="text-cyan-400 font-bold">O</span> + <span class="text-amber-400 font-bold">O₂</span> ──────→ <span class="text-emerald-400 font-bold">O₃ (Ozone Molecule)</span>';
                exp.textContent = 'Step 2: Reactive nascent oxygen (O) binds to intact oxygen gas (O2) to form protective stratospheric ozone (O3).';
            }} else {{
                eq.innerHTML = '<span class="text-rose-400 font-bold">Cl• + O₃ → ClO• + O₂</span> &nbsp;|&nbsp; <span class="text-rose-400 font-bold">ClO• + O → Cl• + O₂</span>';
                exp.textContent = 'CFC Catalysis: Chlorine radical destroys ozone and is regenerated unchanged, destroying over 100,000 O3 molecules per chlorine atom!';
            }}
        }}

        // Lab 13.11
        function updateSim11Timeline() {{
            const yr = parseInt(document.getElementById('sim11-slider').value);
            document.getElementById('sim11-slider-year').textContent = yr;
            document.getElementById('sim11-year-val').textContent = `Year: ${{yr}}`;

            const hole = document.getElementById('sim11-hole');
            const lbl = document.getElementById('sim11-hole-label');

            if (yr <= 1980) {{
                hole.setAttribute('r', '20');
                lbl.textContent = 'Ozone Hole Developing: 3 Million km²';
            }} else if (yr <= 2000) {{
                const r = 20 + (yr - 1980) * 3;
                hole.setAttribute('r', r);
                lbl.textContent = `Ozone Depletion Peaked: ${{Math.round(r * 0.4)}} Million km²`;
            }} else {{
                const r = Math.max(15, 80 - (yr - 2000) * 1.5);
                hole.setAttribute('r', r);
                lbl.textContent = `Healing Under Montreal Protocol: ${{Math.round(r * 0.3)}} Million km²`;
            }}
        }}

        // Lab 13.12
        function updateSim12Burial() {{
            const d = parseInt(document.getElementById('sim12-slider').value);
            document.getElementById('sim12-slider-day').textContent = `Day ${{d}}`;
            document.getElementById('sim12-day-val').textContent = `Observation: Day ${{d}}`;

            const peels = document.getElementById('sim12-peels');
            const paper = document.getElementById('sim12-paper');
            const desc = document.getElementById('sim12-desc');

            if (d === 0) {{
                peels.setAttribute('opacity', '1');
                paper.setAttribute('opacity', '1');
                desc.textContent = 'Day 0: All waste items freshly buried under 15 cm garden soil.';
            }} else if (d === 15) {{
                peels.setAttribute('opacity', '0.7');
                paper.setAttribute('opacity', '0.8');
                desc.textContent = 'Day 15: Peels start turning brown and softening; plastic remains unaltered.';
            }} else if (d === 30) {{
                peels.setAttribute('opacity', '0.35');
                paper.setAttribute('opacity', '0.5');
                desc.textContent = 'Day 30: Peels heavily digested into dark compost; plastic wrapper looks completely new.';
            }} else {{
                peels.setAttribute('opacity', '0.05');
                paper.setAttribute('opacity', '0.2');
                desc.textContent = 'Day 60: Organic waste completely vanished into rich soil humus. Plastic and aluminium persist 100% unaltered!';
            }}
        }}

        // Lab 13.13
        function testSim13Substrate(type) {{
            playTone(type === 'starch' ? 620 : 310, 'sine', 0.1);
            const bSt = document.getElementById('btn-sim13-starch');
            const bPl = document.getElementById('btn-sim13-plastic');
            const shape = document.getElementById('sim13-sub-shape');
            const txt = document.getElementById('sim13-sub-text');
            const st = document.getElementById('sim13-hud-status');
            const msg = document.getElementById('sim13-hud-msg');
            const prod = document.getElementById('sim13-hud-prod');
            const desc = document.getElementById('sim13-desc');

            if (type === 'starch') {{
                bSt.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bPl.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                shape.setAttribute('fill', '#22c55e');
                shape.setAttribute('width', '30');
                txt.textContent = 'Starch';
                st.textContent = 'STATUS: DIGESTED!';
                st.className = 'text-emerald-400 font-bold';
                msg.textContent = 'Substrate matches enzyme active site';
                prod.textContent = 'Cleaved into simple glucose units';
                desc.textContent = 'Natural starch matches bacterial amylase active sites, decomposing rapidly.';
            }} else {{
                bPl.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                bSt.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                shape.setAttribute('fill', '#06b6d4');
                shape.setAttribute('width', '50'); // Clashes geometrically
                txt.textContent = 'Synthetic Plastic';
                st.textContent = 'STATUS: REJECTED / NO REACTION!';
                st.className = 'text-rose-400 font-bold';
                msg.textContent = 'Molecular shape cannot fit enzyme site';
                prod.textContent = 'Persists unaltered in nature for centuries';
                desc.textContent = 'Enzymes are specific in action! Bacteria lack enzymes capable of breaking synthetic petroleum polymer bonds.';
            }}
        }}

        // Lab 13.14
        const teacupData = {{
            glass: {{ name: 'Returnable Glass Cup', hygiene: 'Unhygienic (Bucket Wash Risks)', topsoil: 'Zero Top-Soil Loss', bio: 'Reusable', desc: 'Washing cups in train stations posed severe disease transmission risks.' }},
            plastic: {{ name: 'Disposable Plastic Cup', hygiene: '100% Hygienic', topsoil: 'Zero Top-Soil Loss', bio: 'Non-Biodegradable (Landfill Crisis)', desc: 'Solved hygiene but created millions of non-biodegradable cups cluttering railway tracks.' }},
            kulhad: {{ name: 'Disposable Clay Kulhad', hygiene: 'Hygienic Single-Use', topsoil: 'Severe Loss of Fertile Top-Soil!', bio: '100% Biodegradable', desc: 'Clay was biodegradable, but extracting billions of kulhads stripped fertile agricultural top-soil!' }},
            paper: {{ name: 'Modern Paper Cup', hygiene: '100% Hygienic', topsoil: 'Zero Top-Soil Loss', bio: '100% Biodegradable & Compostable', desc: 'Paper cups are sanitary, fully biodegradable, and preserve fertile top-soil!' }}
        }};

        function selectSim14Era(era) {{
            playTone(540, 'sine', 0.08);
            ['glass', 'plastic', 'kulhad', 'paper'].forEach(e => {{
                const b = document.getElementById(`btn-cup-${{e}}`);
                if (b) b.className = 'px-2 py-1 rounded text-[11px] font-bold bg-slate-800 text-slate-300 transition';
            }});
            const activeB = document.getElementById(`btn-cup-${{era}}`);
            if (activeB) activeB.className = 'px-2 py-1 rounded text-[11px] font-bold bg-emerald-600 text-white transition';

            const d = teacupData[era];
            document.getElementById('sim14-cup-name').textContent = d.name;
            document.getElementById('sim14-hygiene').textContent = d.hygiene;
            document.getElementById('sim14-topsoil').textContent = d.topsoil;
            document.getElementById('sim14-biodegradable').textContent = d.bio;
            document.getElementById('sim14-desc').textContent = d.desc;
        }}

        // Lab 13.15
        function sortSim15Item(itemKey, expectedBin) {{
            playTone(580, 'sine', 0.1);
            const itemBtn = document.getElementById(`item-${{itemKey}}`);
            if (!itemBtn) return;
            itemBtn.classList.add('hidden');

            const targetBin = (expectedBin === 'green') ? document.getElementById('sim15-green-bin') : document.getElementById('sim15-blue-bin');
            const pill = document.createElement('span');
            pill.className = 'px-2 py-0.5 rounded-full bg-slate-900 border border-slate-700 m-0.5';
            pill.textContent = itemBtn.textContent;
            targetBin.appendChild(pill);
        }}

        function resetSim15Sorter() {{
            playTone(400, 'sine', 0.08);
            ['peel', 'bottle', 'can', 'tea'].forEach(k => {{
                const b = document.getElementById(`item-${{k}}`);
                if (b) b.classList.remove('hidden');
            }});
            document.getElementById('sim15-green-bin').innerHTML = '';
            document.getElementById('sim15-blue-bin').innerHTML = '';
        }}

        // Lab 13.16
        let sim16HerbivoresKilled = false;
        function toggleSim16Herbivores() {{
            sim16HerbivoresKilled = !sim16HerbivoresKilled;
            playTone(sim16HerbivoresKilled ? 280 : 540, 'sine', 0.12);
            const btn = document.getElementById('btn-sim16-kill');
            const t2Status = document.getElementById('sim16-t2-status');
            const t3Status = document.getElementById('sim16-t3-status');
            const t1Status = document.getElementById('sim16-t1-status');
            const desc = document.getElementById('sim16-desc');

            if (sim16HerbivoresKilled) {{
                btn.textContent = 'Restore Herbivores';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                t2Status.textContent = 'Population: 0 (EXTINCT!)';
                t2Status.className = 'text-rose-400 font-bold';
                t3Status.textContent = 'Starvation! Pop: 0';
                t3Status.className = 'text-rose-400 font-bold';
                t1Status.textContent = 'Overgrown & choked';
                t1Status.className = 'text-amber-400 font-bold';
                desc.textContent = 'Killing herbivores caused tiger starvation while grass grew unchecked. Every trophic tier is indispensable!';
            }} else {{
                btn.textContent = 'Kill All Herbivores (T2)';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                t2Status.textContent = 'Population: 150';
                t2Status.className = 'text-cyan-300';
                t3Status.textContent = 'Population: 10';
                t3Status.className = 'text-rose-300';
                t1Status.textContent = 'Status: Normal';
                t1Status.className = 'text-emerald-300';
                desc.textContent = 'Eliminating an intermediate trophic level starves carnivores above while leaving vegetation unbrowsed below.';
            }}
        }}

        // Initialize App on DOM Ready
        window.addEventListener('DOMContentLoaded', () => {{
            generateSlidePills();
            selectSim4Chain('forest');
            showSlide(0);
        }});
    </script>
</body>
</html>
"""
    return full_html

if __name__ == "__main__":
    html_output = build_full_html()
    target_path = "public/animations/our-environment.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output)} bytes)")


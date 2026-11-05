"""Simulators 1 to 8 for Chapter 6"""
import sys

SIMS = {}

# SIM 1
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Island Explorer & Indira Point Compass</span>
        <p class="text-[11px] text-slate-400">An island is land completely surrounded by water on all four sides. Locate India's southernmost tip!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-cyan-950/30 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <rect x="0" y="0" width="400" height="240" fill="#082f49"/>
            <path d="M 0,40 Q 50,35 100,40 T 200,40 T 300,40 T 400,40 L 400,240 L 0,240 Z" fill="#0c4a6e" opacity="0.6"/>
            <path d="M 0,120 Q 50,115 100,120 T 200,120 T 300,120 T 400,120 L 400,240 L 0,240 Z" fill="#075985" opacity="0.4"/>

            <!-- Mainland India Outline (Peninsula) -->
            <path d="M 40,0 L 40,60 Q 60,110 90,140 Q 110,160 120,180 L 100,190 Q 70,160 50,110 L 30,50 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
            <text x="50" y="40" fill="#94a3b8" font-size="9" font-weight="bold">Indian Mainland</text>
            <text x="55" y="52" fill="#64748b" font-size="8">(Peninsula: 3 sides water)</text>

            <!-- Andaman & Nicobar Chain -->
            <ellipse cx="250" cy="50" rx="14" ry="24" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="52" fill="#a7f3d0" font-size="8">North & Middle Andaman</text>

            <ellipse cx="254" cy="105" rx="12" ry="18" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <ellipse cx="256" cy="138" rx="9" ry="10" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <text x="272" y="108" fill="#a7f3d0" font-size="8">South Andaman (Port Blair)</text>

            <line x1="220" y1="156" x2="330" y2="156" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1"/>
            <text x="275" y="154" fill="#38bdf8" font-size="7">10° Channel</text>

            <ellipse cx="260" cy="172" rx="10" ry="8" fill="#047857" stroke="#10b981" stroke-width="1.5"/>
            <ellipse cx="265" cy="202" rx="14" ry="16" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
            <text x="284" y="196" fill="#6ee7b7" font-size="8" font-weight="bold">Great Nicobar</text>

            <!-- Indira Point Marker -->
            <g id="indiraMarker" class="cursor-pointer" transform="translate(268, 214)">
                <circle cx="0" cy="0" r="6" fill="#ef4444" opacity="0.8">
                    <animate attributeName="r" values="4;8;4" dur="2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="0" cy="0" r="3" fill="#ffffff"/>
                <polygon points="0,-14 -3,-3 3,-3" fill="#f59e0b"/>
                <rect x="-2" y="-18" width="4" height="4" fill="#ef4444"/>
            </g>
            <text x="280" y="222" fill="#f87171" font-size="9" font-weight="bold">Indira Point (6°45' N)</text>

            <!-- Water Surround Labels -->
            <g id="waterFlowArrows" class="opacity-0 transition-opacity duration-300">
                <circle cx="265" cy="100" r="45" fill="none" stroke="#38bdf8" stroke-dasharray="4,4" stroke-width="1.5"/>
                <text x="265" y="45" text-anchor="middle" fill="#7dd3fc" font-size="8">▲ North: Bay of Bengal</text>
                <text x="265" y="165" text-anchor="middle" fill="#7dd3fc" font-size="8">▼ South: Indian Ocean</text>
                <text x="325" y="105" fill="#7dd3fc" font-size="8">▶ East: Andaman Sea</text>
                <text x="180" y="105" fill="#7dd3fc" font-size="8">◀ West: Bay of Bengal</text>
            </g>

            <!-- Compass -->
            <g transform="translate(365, 35)">
                <circle cx="0" cy="0" r="16" fill="#0f172a" stroke="#475569" stroke-width="1"/>
                <line x1="0" y1="-14" x2="0" y2="14" stroke="#94a3b8" stroke-width="1"/>
                <line x1="-14" y1="0" x2="14" y2="0" stroke="#94a3b8" stroke-width="1"/>
                <polygon points="0,-13 -3,0 3,0" fill="#ef4444"/>
                <polygon points="0,13 -3,0 3,0" fill="#cbd5e1"/>
                <text x="0" y="-15" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="bold">N</text>
                <text x="0" y="23" text-anchor="middle" fill="#94a3b8" font-size="7">S</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleIslandWaterCheck()" id="sim1WaterBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition flex items-center justify-center space-x-1">
            <span>Verify Water Surround</span>
        </button>
        <button onclick="zoomIndiraPoint()" id="sim1IndiraBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center space-x-1">
            <span>Locate Indira Point (6°45' N)</span>
        </button>
    </div>
    <div id="sim1Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Island Fact:</span> An island has 360° water boundaries. India's mainland is a peninsula (water on 3 sides), while the Andaman & Nicobar group is a true island archipelago!
    </div>
</div>
"""

# SIM 2: Buttress Root Structural Physics Lab
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Buttress Root Structural Physics Lab</span>
        <p class="text-[11px] text-slate-400">Tropical rainforest trees grow 40m tall in thin topsoil. Compare how buttress roots resist cyclonic winds!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Soil Ground Line -->
            <rect x="0" y="190" width="400" height="50" fill="#3f2e1e"/>
            <line x1="0" y1="190" x2="400" y2="190" stroke="#78350f" stroke-width="2"/>
            <text x="200" y="210" text-anchor="middle" fill="#a16207" font-size="8">Shallow Tropical Topsoil Layer (Depth ~ 30-50 cm)</text>

            <!-- Wind Stream Lines -->
            <g id="windVectors" class="opacity-30">
                <path d="M 10,40 Q 100,30 200,45 T 390,40" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,4"/>
                <path d="M 10,70 Q 100,60 200,75 T 390,70" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="10,5"/>
                <path d="M 10,100 Q 100,90 200,105 T 390,100" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,4"/>
            </g>

            <!-- Tree Left: Standard Taproot / Shallow Root Tree -->
            <g id="standardTree" transform="translate(100, 190)">
                <!-- Canopy -->
                <circle cx="0" cy="-120" r="32" fill="#15803d" opacity="0.85"/>
                <circle cx="-15" cy="-110" r="24" fill="#166534" opacity="0.9"/>
                <circle cx="15" cy="-110" r="24" fill="#22c55e" opacity="0.8"/>
                <!-- Trunk -->
                <rect x="-8" y="-100" width="16" height="100" fill="#78350f"/>
                <!-- Shallow Roots underground -->
                <path d="M 0,0 L -18,20 M 0,0 L 18,20 M 0,0 L 0,25" stroke="#78350f" stroke-width="3"/>
                <text x="0" y="38" text-anchor="middle" fill="#94a3b8" font-size="8">Standard Roots (Shallow)</text>
            </g>

            <!-- Tree Right: Rainforest Giant with Buttress Roots -->
            <g id="buttressTree" transform="translate(280, 190)">
                <!-- Canopy -->
                <circle cx="0" cy="-125" r="36" fill="#15803d" opacity="0.9"/>
                <circle cx="-20" cy="-115" r="26" fill="#16a34a" opacity="0.9"/>
                <circle cx="20" cy="-115" r="26" fill="#22c55e" opacity="0.85"/>
                <!-- Trunk -->
                <rect x="-10" y="-105" width="20" height="105" fill="#78350f"/>
                <!-- Triangular Flanged Buttress Roots -->
                <!-- Left Buttress Fin -->
                <path d="M -10,-45 Q -25,-10 -55,0 L -10,0 Z" fill="#854d0e" stroke="#5c3809" stroke-width="1.5"/>
                <!-- Right Buttress Fin -->
                <path d="M 10,-45 Q 25,-10 55,0 L 10,0 Z" fill="#854d0e" stroke="#5c3809" stroke-width="1.5"/>
                <!-- Centre Flange -->
                <path d="M 0,-30 L -15,0 L 15,0 Z" fill="#9a3412" stroke="#5c3809" stroke-width="1"/>
                <text x="0" y="38" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">Wide Buttress Fins (Triangular Base)</text>
            </g>

            <!-- Wind Force Readout -->
            <g transform="translate(20, 25)">
                <rect x="0" y="0" width="130" height="24" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text id="windForceText" x="65" y="16" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Wind: Gentle Breeze (20 km/h)</text>
            </g>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Wind Velocity:</span>
            <span id="windSpeedLabel" class="font-bold text-cyan-400">20 km/h (Calm)</span>
        </div>
        <input type="range" id="windSlider" min="20" max="150" value="20" step="10" oninput="updateWindPhysics(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
    </div>
    <div id="sim2Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Biomechanical Principle:</span> Wide triangular buttress roots act like external cathedral flying buttresses, converting horizontal gale wind shear into tensile anchoring forces along the ground!
    </div>
</div>
"""

# SIM 3: Endemic Island Bird Sanctuary
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">Endemic Island Bird Observatory</span>
        <p class="text-[11px] text-slate-400">Endemic species occur naturally nowhere else on Earth! Spot Andaman's signature avian treasures.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-emerald-950/40 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Tropical Canopy Foliage -->
            <path d="M 0,0 L 400,0 L 400,110 Q 300,70 200,90 Q 100,70 0,110 Z" fill="#064e3b" opacity="0.8"/>
            <path d="M 0,0 L 400,0 L 400,80 Q 250,50 150,70 Q 50,40 0,80 Z" fill="#047857" opacity="0.9"/>

            <!-- Rainforest Tree Branches -->
            <path d="M 0,140 Q 60,130 130,145 T 220,135" fill="none" stroke="#451a03" stroke-width="8" stroke-linecap="round"/>
            <path d="M 230,110 Q 290,120 370,105 T 400,115" fill="none" stroke="#451a03" stroke-width="7" stroke-linecap="round"/>

            <!-- Hanging Figs & Berries (Bird Food) -->
            <circle cx="120" cy="155" r="4" fill="#a855f7"/>
            <circle cx="128" cy="158" r="3.5" fill="#a855f7"/>
            <circle cx="340" cy="120" r="4" fill="#ef4444"/>
            <circle cx="348" cy="124" r="3.5" fill="#f97316"/>

            <!-- Bird 1: Andaman Wood Pigeon (Columba palumboides) on Left Branch -->
            <g id="woodPigeon" class="cursor-pointer transition-transform hover:scale-105" transform="translate(110, 105)" onclick="selectBird('pigeon')">
                <!-- Highlight Aura -->
                <circle id="pigeonAura" cx="15" cy="15" r="35" fill="#c084fc" opacity="0.2" class="hidden"/>
                <!-- Body: Iridescent purple-grey -->
                <ellipse cx="15" cy="18" rx="20" ry="14" fill="#475569" stroke="#7e22ce" stroke-width="1.5"/>
                <!-- Head -->
                <circle cx="32" cy="10" r="10" fill="#94a3b8"/>
                <polygon points="40,9 48,11 40,13" fill="#fb923c"/>
                <circle cx="35" cy="8" r="2" fill="#0f172a"/>
                <!-- Wing -->
                <path d="M 5,14 Q 20,24 10,32 Q 0,26 5,14 Z" fill="#6b21a8"/>
                <!-- Tail -->
                <path d="M -2,22 L -14,30 L -10,20 Z" fill="#334155"/>
                <text x="15" y="-6" text-anchor="middle" fill="#e9d5ff" font-size="8" font-weight="bold">Andaman Wood Pigeon</text>
            </g>

            <!-- Bird 2: Andaman / Narcondam Hornbill on Right Branch -->
            <g id="hornbill" class="cursor-pointer transition-transform hover:scale-105" transform="translate(290, 80)" onclick="selectBird('hornbill')">
                <circle id="hornbillAura" cx="20" cy="15" r="40" fill="#f59e0b" opacity="0.2" class="hidden"/>
                <!-- Body -->
                <ellipse cx="15" cy="18" rx="22" ry="15" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
                <!-- White/rufous neck feathers -->
                <path d="M 28,12 Q 35,5 34,-5 L 24,-2 Z" fill="#fde68a"/>
                <!-- Head -->
                <circle cx="32" cy="-4" r="9" fill="#d97706"/>
                <!-- Huge Curved Bill with Casque -->
                <path d="M 38,-6 Q 52,-8 62,2 Q 48,6 38,2 Z" fill="#fbbf24" stroke="#b45309" stroke-width="1"/>
                <path d="M 39,-9 Q 48,-11 52,-6 Z" fill="#ea580c"/> <!-- Casque bump -->
                <circle cx="35" cy="-6" r="2" fill="#0f172a"/>
                <!-- Long Tail -->
                <path d="M -5,22 L -20,40 L -12,24 Z" fill="#f8fafc"/>
                <text x="25" y="-18" text-anchor="middle" fill="#fef08a" font-size="8" font-weight="bold">Andaman Hornbill</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="selectBird('pigeon')" id="pigeonBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-purple-900/60 hover:bg-purple-800 text-purple-200 border border-purple-500/40 transition">
            <span>Andaman Wood Pigeon</span>
        </button>
        <button onclick="selectBird('hornbill')" id="hornbillBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-900/60 hover:bg-amber-800 text-amber-200 border border-amber-500/40 transition">
            <span>Andaman Hornbill</span>
        </button>
    </div>
    <div id="sim3Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-purple-400 font-bold">Endemic Definition:</span> An endemic organism is geographically restricted to a specific localized habitat. Because islands are isolated by oceans, unique species evolved here over millions of years!
    </div>
</div>
"""

# SIM 4: Coral Polyp & Reef Ecosystem Builder
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Coral Polyp & Barrier Reef Physics</span>
        <p class="text-[11px] text-slate-400">Discover animal-algae symbiosis and how coral reefs absorb up to 97% of violent ocean wave energy!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-teal-950/40 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Ocean Storm Wave approaching from Left -->
            <path id="stormWavePath" d="M 0,80 Q 50,30 100,75 T 180,80 L 180,240 L 0,240 Z" fill="#0284c7" opacity="0.6"/>

            <!-- Coral Barrier Reef Wall in Center -->
            <g transform="translate(190, 120)">
                <!-- Limestone Cup (Calcium Carbonate skeleton) -->
                <path d="M 0,100 L 0,30 Q 20,40 40,30 L 40,100 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Individual Polyp Body (soft fleshy animal) -->
                <path d="M 5,30 Q 20,20 35,30 L 32,80 L 8,80 Z" fill="#f43f5e" opacity="0.9"/>
                <!-- Tentacles on rim -->
                <path d="M 5,28 Q -2,12 8,2 L 10,26" fill="none" stroke="#fb7185" stroke-width="2.5" stroke-linecap="round"/>
                <path d="M 14,26 Q 16,8 20,0 L 22,25" fill="none" stroke="#fb7185" stroke-width="2.5" stroke-linecap="round"/>
                <path d="M 28,26 Q 34,10 32,2 L 30,28" fill="none" stroke="#fb7185" stroke-width="2.5" stroke-linecap="round"/>
                <path d="M 35,28 Q 44,14 42,4 L 37,28" fill="none" stroke="#fb7185" stroke-width="2.5" stroke-linecap="round"/>

                <!-- Symbiotic Zooxanthellae (Green microalgae dots inside polyp tissues) -->
                <circle cx="15" cy="45" r="2" fill="#84cc16"/>
                <circle cx="25" cy="40" r="2.5" fill="#84cc16"/>
                <circle cx="18" cy="60" r="2" fill="#84cc16"/>
                <circle cx="28" cy="55" r="2" fill="#84cc16"/>
                <circle cx="22" cy="70" r="2" fill="#84cc16"/>

                <text x="20" y="112" text-anchor="middle" fill="#cbd5e1" font-size="8" font-weight="bold">Reef Structure</text>
            </g>

            <!-- Lagoon / Calm Coast on Right (Waves reduced to gentle ripples) -->
            <path d="M 230,135 Q 280,133 330,135 T 400,135 L 400,240 L 230,240 Z" fill="#0e7490" opacity="0.4"/>
            <text x="315" y="125" text-anchor="middle" fill="#38bdf8" font-size="8">Protected Calm Lagoon</text>

            <!-- Wave Energy Dissipation Percentage Gauge -->
            <g transform="translate(15, 20)">
                <rect x="0" y="0" width="130" height="42" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="65" y="15" text-anchor="middle" fill="#94a3b8" font-size="8">Wave Energy Reduction</text>
                <text id="waveReductionText" x="65" y="32" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">97% Absorbed</text>
            </g>

            <!-- Sunlight Beams powering photosynthesis -->
            <line x1="210" y1="0" x2="210" y2="100" stroke="#facc15" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
            <text x="235" y="25" fill="#facc15" font-size="8">Sunlight for Zooxanthellae</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleWaveStorm()" id="sim4StormBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
            <span>Simulate High Ocean Swell</span>
        </button>
        <button onclick="inspectPolypSymbiosis()" id="sim4SymbiosisBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
            <span>Inspect Polyp Symbiosis</span>
        </button>
    </div>
    <div id="sim4Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-rose-400 font-bold">Symbiosis Secret:</span> Coral polyps are tiny animals that secrete calcium carbonate cups. Microscopic algae (zooxanthellae) living inside provide 90% of their nutrients through sunlight photosynthesis!
    </div>
</div>
"""

# SIM 5: Sentinelese Indigenous Ecology & Tsunami Wisdom
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">North Sentinel Island & Tsunami Wisdom</span>
        <p class="text-[11px] text-slate-400">Discover how indigenous traditional knowledge warned of the 2004 tsunami before modern sensors!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Ocean Baseline -->
            <path id="sentinelOcean" d="M 0,160 L 150,160 Q 200,160 220,185 L 0,185 Z" fill="#0284c7" opacity="0.7"/>

            <!-- High Forested Ridge on Island (Right side) -->
            <path d="M 160,240 L 180,180 Q 240,110 320,130 Q 370,140 400,160 L 400,240 Z" fill="#14532d"/>
            <path d="M 220,130 Q 270,90 340,105 Q 380,120 400,140 L 400,240 L 220,240 Z" fill="#166534" opacity="0.8"/>

            <!-- Canopy Trees on Ridge -->
            <circle cx="280" cy="100" r="18" fill="#15803d"/>
            <circle cx="310" cy="95" r="20" fill="#22c55e" opacity="0.9"/>
            <circle cx="350" cy="110" r="22" fill="#166534"/>

            <!-- Sentinelese Tribe Figures on High Ridge -->
            <g id="tribeCamp" transform="translate(305, 88)">
                <circle cx="0" cy="0" r="4" fill="#92400e"/> <!-- Head -->
                <line x1="0" y1="4" x2="0" y2="16" stroke="#92400e" stroke-width="2"/> <!-- Torso -->
                <line x1="0" y1="16" x2="-4" y2="24" stroke="#92400e" stroke-width="1.5"/> <!-- Left Leg -->
                <line x1="0" y1="16" x2="4" y2="24" stroke="#92400e" stroke-width="1.5"/> <!-- Right Leg -->
                <!-- Long Bow -->
                <path d="M -6,-2 Q -10,10 -6,22" fill="none" stroke="#78350f" stroke-width="1.5"/>
                <line x1="-6" y1="-2" x2="-6" y2="22" stroke="#e2e8f0" stroke-width="0.8"/>
            </g>

            <!-- Shoreline Outrigger Canoe -->
            <g id="sentinelCanoe" transform="translate(130, 165)">
                <ellipse cx="0" cy="0" rx="18" ry="4" fill="#78350f"/>
                <line x1="-12" y1="0" x2="-22" y2="10" stroke="#92400e" stroke-width="1.5"/>
                <rect x="-24" y="9" width="16" height="3" rx="1" fill="#a16207"/>
            </g>

            <!-- Birds Alarm Signs -->
            <g id="birdAlarms" class="opacity-0 transition-opacity duration-300">
                <path d="M 230,50 Q 240,40 250,50 Q 260,40 270,50" fill="none" stroke="#ef4444" stroke-width="2"/>
                <path d="M 270,35 Q 280,25 290,35 Q 300,25 310,35" fill="none" stroke="#ef4444" stroke-width="2"/>
                <text x="270" y="20" text-anchor="middle" fill="#f87171" font-size="8" font-weight="bold">Alarm Screeches & Flock Upward Flight!</text>
            </g>

            <!-- Warning Status Box -->
            <g transform="translate(15, 20)">
                <rect x="0" y="0" width="155" height="42" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="77" y="15" text-anchor="middle" fill="#94a3b8" font-size="8">Condition & Elevation</text>
                <text id="sentinelModeText" x="77" y="32" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Calm Sea (Normal Tide)</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="setSentinelCondition('calm')" id="sentinelCalmBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
            <span>Calm Daily Life</span>
        </button>
        <button onclick="setSentinelCondition('tsunami')" id="sentinelTsunamiBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>2004 Tsunami Warning Signs</span>
        </button>
    </div>
    <div id="sim5Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Traditional Ecological Knowledge:</span> When ocean water rapidly receded and coastal birds shrieked, the Sentinelese recognized nature's warning and moved safely up to high forested hills!
    </div>
</div>
"""

# SIM 6: Sundarbans Tidal Delta Flow Engine
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Sundarbans Tidal Delta Flow Engine</span>
        <p class="text-[11px] text-slate-400">Where fresh Ganga-Brahmaputra waters meet Bay of Bengal tides, forming the world's largest mangrove forest!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-teal-950/30 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Mudflat Island Base -->
            <path d="M 50,130 Q 150,110 250,135 Q 350,120 400,140 L 400,240 L 0,240 L 0,140 Z" fill="#452a14"/>
            <text x="200" y="215" text-anchor="middle" fill="#a16207" font-size="9" font-weight="bold">Muddy Silt Delta Deposits (Rich Alluvial Soil)</text>

            <!-- Mangrove Stilt Roots & Tree Canopies -->
            <g transform="translate(160, 130)">
                <!-- Canopy -->
                <circle cx="0" cy="-60" r="30" fill="#15803d"/>
                <circle cx="-15" cy="-50" r="22" fill="#166534"/>
                <circle cx="15" cy="-50" r="22" fill="#22c55e" opacity="0.9"/>
                <!-- Trunk -->
                <rect x="-6" y="-35" width="12" height="35" fill="#582f0e"/>
                <!-- Entangled Stilt Roots -->
                <path d="M -5,-15 Q -20,10 -30,30" fill="none" stroke="#7f4f24" stroke-width="3"/>
                <path d="M 5,-15 Q 20,10 30,30" fill="none" stroke="#7f4f24" stroke-width="3"/>
                <path d="M -3,-5 Q -10,15 -15,30" fill="none" stroke="#936639" stroke-width="2.5"/>
                <path d="M 3,-5 Q 10,15 15,30" fill="none" stroke="#936639" stroke-width="2.5"/>
            </g>

            <!-- Tidal Water Layer (Animated Height) -->
            <rect id="tideWaterRect" x="0" y="160" width="400" height="80" fill="#0891b2" opacity="0.6"/>

            <!-- Mixing Flow Arrows -->
            <g transform="translate(40, 60)">
                <path d="M 0,0 L 60,0" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
                <text x="0" y="-8" fill="#7dd3fc" font-size="8">Fresh River Flow (Ganga)</text>
            </g>
            <g transform="translate(320, 60)">
                <path d="M 40,0 L -20,0" stroke="#0284c7" stroke-width="2"/>
                <text x="10" y="-8" text-anchor="middle" fill="#38bdf8" font-size="8">Salty Sea Inflow (Bay of Bengal)</text>
            </g>

            <!-- Brackish Water Salinity Meter -->
            <g transform="translate(15, 10)">
                <rect x="0" y="0" width="130" height="40" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="65" y="14" text-anchor="middle" fill="#94a3b8" font-size="8">Water Condition</text>
                <text id="salinityText" x="65" y="30" text-anchor="middle" fill="#2dd4bf" font-size="10" font-weight="bold">Brackish Water (Mixed)</text>
            </g>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Tidal Cycle:</span>
            <span id="tideLevelLabel" class="font-bold text-teal-400">Mid Tide</span>
        </div>
        <input type="range" id="tideSlider" min="0" max="100" value="50" oninput="updateTideLevel(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-teal-500">
    </div>
    <div id="sim6Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-teal-400 font-bold">Brackish Water:</span> Fresh river water mixing with salty ocean water creates brackish conditions that nourish unique mangrove species like the Sundari tree (Heritiera fomes)!
    </div>
</div>
"""

# SIM 7: Mangrove Pneumatophore Respiration Simulator
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Pneumatophore Respiration Simulator</span>
        <p class="text-[11px] text-slate-400">Mangrove soil is waterlogged with zero oxygen. See how breathing roots grow upward against gravity!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Muddy Waterlogged Soil Layer -->
            <rect x="0" y="140" width="400" height="100" fill="#3b2314"/>
            <text x="200" y="225" text-anchor="middle" fill="#78350f" font-size="8">Waterlogged Mud: Anoxic (Zero Dissolved O2)</text>

            <!-- Horizontal Underground Cable Root -->
            <path d="M 0,185 L 400,185" stroke="#713f12" stroke-width="10"/>

            <!-- Vertical Spike Roots (Pneumatophores) growing UPWARDS -->
            <!-- Root 1 -->
            <path d="M 70,185 L 70,85" stroke="#854d0e" stroke-width="6" stroke-linecap="round"/>
            <circle cx="70" cy="85" r="3" fill="#ca8a04"/>
            <!-- Lenticels (white breathing pores) -->
            <circle cx="68" cy="105" r="1.5" fill="#fef08a"/>
            <circle cx="72" cy="120" r="1.5" fill="#fef08a"/>

            <!-- Root 2 (Center - Featured Zoom) -->
            <path d="M 180,185 L 180,70" stroke="#854d0e" stroke-width="8" stroke-linecap="round"/>
            <circle cx="180" cy="70" r="4" fill="#ca8a04"/>
            <!-- Lenticels -->
            <circle cx="177" cy="85" r="2" fill="#fef08a"/>
            <circle cx="183" cy="100" r="2" fill="#fef08a"/>
            <circle cx="177" cy="118" r="2" fill="#fef08a"/>
            <circle cx="183" cy="132" r="2" fill="#fef08a"/>

            <!-- Root 3 -->
            <path d="M 280,185 L 280,90" stroke="#854d0e" stroke-width="6" stroke-linecap="round"/>
            <!-- Lenticels -->
            <circle cx="278" cy="110" r="1.5" fill="#fef08a"/>
            <circle cx="282" cy="125" r="1.5" fill="#fef08a"/>

            <!-- Oxygen Intake Bubbles / Arrows -->
            <g id="oxygenFlow" class="opacity-80">
                <path d="M 160,85 Q 170,85 174,85" stroke="#38bdf8" stroke-width="2"/>
                <text x="145" y="88" fill="#38bdf8" font-size="8">O2 in</text>
                <path d="M 200,100 Q 190,100 186,100" stroke="#38bdf8" stroke-width="2"/>
                <text x="205" y="103" fill="#38bdf8" font-size="8">O2 in</text>
            </g>

            <!-- Negative Geotropism Indicator -->
            <g transform="translate(305, 30)">
                <rect x="0" y="0" width="85" height="45" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="42" y="15" text-anchor="middle" fill="#94a3b8" font-size="7">Tropism</text>
                <text x="42" y="28" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">Negative</text>
                <text x="42" y="38" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">Geotropism (▲)</text>
            </g>

            <!-- Lenticel Zoom Callout -->
            <g id="lenticelZoom" class="opacity-0 transition-opacity duration-300" transform="translate(20, 25)">
                <rect x="0" y="0" width="130" height="50" rx="6" fill="#1e293b" stroke="#ca8a04" stroke-width="1.5"/>
                <text x="10" y="16" fill="#fef08a" font-size="8" font-weight="bold">Lenticel Microscopic Pore</text>
                <text x="10" y="30" fill="#cbd5e1" font-size="7">Porous spongy cork tissue</text>
                <text x="10" y="42" fill="#38bdf8" font-size="7">Channels O2 down to roots!</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleLenticelZoom()" id="lenticelBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">
            <span>Inspect Lenticels (Pores)</span>
        </button>
        <button onclick="simulateTideSubmersion()" id="tideSubmergeBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
            <span>Simulate High Tide Cover</span>
        </button>
    </div>
    <div id="sim7Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Negative Geotropism:</span> While regular roots grow downward with gravity (+geotropism), mangrove pneumatophores grow straight up into the air (-geotropism) to breathe atmospheric oxygen!
    </div>
</div>
"""

# SIM 8: Sundarbans Tiger Ambush & Mask Defense
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Sundarbans Tiger Ambush & Mask Defense Lab</span>
        <p class="text-[11px] text-slate-400">Honey collectors wear backward-facing human masks. Test how tiger ambush psychology works!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Mangrove Foliage & Swamp -->
            <rect x="0" y="170" width="400" height="70" fill="#2d1810"/>
            <!-- Mangrove roots background -->
            <path d="M 0,170 Q 50,140 100,170 T 200,170 T 300,170 T 400,170" fill="#14532d" opacity="0.6"/>

            <!-- Person (Honey Collector) Walking Forward (Facing Left) -->
            <g transform="translate(140, 140)">
                <!-- Body -->
                <rect x="-8" y="0" width="16" height="35" rx="3" fill="#0284c7"/>
                <line x1="-5" y1="35" x2="-8" y2="55" stroke="#0f172a" stroke-width="3"/>
                <line x1="5" y1="35" x2="8" y2="55" stroke="#0f172a" stroke-width="3"/>
                <!-- Head -->
                <circle cx="0" cy="-10" r="10" fill="#fcd34d"/>
                <!-- Front Face Profile (Facing Left) -->
                <circle cx="-6" cy="-10" r="1.5" fill="#0f172a"/>
                <path d="M -8,-6 L -4,-6" stroke="#0f172a" stroke-width="1"/>
                <text x="-15" y="-14" fill="#38bdf8" font-size="7">Walking ▶</text>

                <!-- Backward Facing Mask on Back of Head (Facing Right) -->
                <g id="rearMask" class="opacity-0 transition-opacity duration-300">
                    <circle cx="6" cy="-10" r="9" fill="#fef08a" stroke="#ea580c" stroke-width="1.5"/>
                    <!-- Painted wide eyes -->
                    <circle cx="7" cy="-12" r="2.5" fill="#ffffff" stroke="#000000" stroke-width="0.8"/>
                    <circle cx="7" cy="-12" r="1.2" fill="#000000"/>
                    <circle cx="7" cy="-8" r="2.5" fill="#ffffff" stroke="#000000" stroke-width="0.8"/>
                    <circle cx="7" cy="-8" r="1.2" fill="#000000"/>
                    <!-- Painted mustache / smile -->
                    <path d="M 10,-10 Q 12,-7 10,-4" fill="none" stroke="#dc2626" stroke-width="1"/>
                    <text x="22" y="-12" fill="#fde047" font-size="7" font-weight="bold">Rear Mask</text>
                </g>
            </g>

            <!-- Royal Bengal Tiger Stalking from Behind (Right Side) -->
            <g id="stalkingTiger" transform="translate(290, 150)" class="transition-transform duration-500">
                <!-- Tiger Body (Orange with Black Stripes) -->
                <ellipse cx="0" cy="0" rx="28" ry="16" fill="#ea580c"/>
                <!-- Stripes -->
                <path d="M -10,-12 L -5,0 L -12,10" stroke="#0f172a" stroke-width="2"/>
                <path d="M 2,-14 L 6,0 L 0,12" stroke="#0f172a" stroke-width="2"/>
                <path d="M 14,-10 L 16,0 L 12,8" stroke="#0f172a" stroke-width="2"/>
                <!-- Head -->
                <circle cx="-28" cy="-6" r="12" fill="#ea580c"/>
                <circle cx="-32" cy="-8" r="2" fill="#facc15"/>
                <circle cx="-32" cy="-8" r="1" fill="#0f172a"/>
                <polygon points="-24,-16 -20,-12 -26,-12" fill="#ea580c"/>
                <!-- Paws -->
                <rect x="-18" y="12" width="6" height="15" rx="2" fill="#c2410c"/>
                <rect x="12" y="12" width="6" height="15" rx="2" fill="#c2410c"/>
                <!-- Long Tail -->
                <path d="M 28,-2 Q 40,-15 35,-25" fill="none" stroke="#ea580c" stroke-width="4" stroke-linecap="round"/>
            </g>

            <!-- Tiger Thought Bubble / State Indicator -->
            <g transform="translate(260, 50)">
                <rect id="tigerStatusBox" x="0" y="0" width="125" height="38" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="1.5"/>
                <text id="tigerStatusTitle" x="62" y="14" text-anchor="middle" fill="#ea580c" font-size="8" font-weight="bold">Tiger Intent</text>
                <text id="tigerStatusDesc" x="62" y="28" text-anchor="middle" fill="#fef08a" font-size="8">Stalking from behind...</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleTigerMask(false)" id="maskOffBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
            <span>Mask: OFF (Back Bare)</span>
        </button>
        <button onclick="toggleTigerMask(true)" id="maskOnBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>Mask: ON (Face on Back)</span>
        </button>
    </div>
    <div id="sim8Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Ambush Predator Psychology:</span> Royal Bengal Tigers rely almost exclusively on stealth sneak attacks from the rear. When they see eyes looking straight at them, they feel spotted and lose the element of surprise, retreating into the mangrove brush!
    </div>
</div>
"""

print("Sims 1-8 defined successfully")

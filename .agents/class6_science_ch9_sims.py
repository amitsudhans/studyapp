"""
Interactive SVG/HTML Simulators for NCERT Class 6 Science - Chapter 9: Methods of Separation in Everyday Life
16 Bespoke interactive simulators. Zero raw LaTeX.
"""

SIMULATORS = {
    1: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 1: Separation Purpose Explorer</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300">Raw Mixture</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim1-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Outer Tray -->
                <rect x="30" y="20" width="340" height="120" rx="15" fill="#1e293b" stroke="#475569" stroke-width="2"/>
                <text x="200" y="40" fill="#94a3b8" font-size="12" text-anchor="middle" font-weight="bold">Harvest Grain Tray (Haryana Courtyard)</text>
                
                <!-- Grains (Golden) -->
                <g id="sim1-grains">
                    <ellipse cx="80" cy="80" rx="8" ry="4" fill="#facc15" transform="rotate(20 80 80)"/>
                    <ellipse cx="110" cy="95" rx="8" ry="4" fill="#facc15" transform="rotate(-15 110 95)"/>
                    <ellipse cx="140" cy="75" rx="8" ry="4" fill="#facc15" transform="rotate(45 140 75)"/>
                    <ellipse cx="170" cy="100" rx="8" ry="4" fill="#facc15" transform="rotate(10 170 100)"/>
                    <ellipse cx="200" cy="80" rx="8" ry="4" fill="#facc15" transform="rotate(-30 200 80)"/>
                    <ellipse cx="230" cy="95" rx="8" ry="4" fill="#facc15" transform="rotate(25 230 95)"/>
                    <ellipse cx="260" cy="75" rx="8" ry="4" fill="#facc15" transform="rotate(-10 260 75)"/>
                    <ellipse cx="290" cy="90" rx="8" ry="4" fill="#facc15" transform="rotate(35 290 90)"/>
                    <ellipse cx="320" cy="85" rx="8" ry="4" fill="#facc15" transform="rotate(-20 320 85)"/>
                </g>
                
                <!-- Stones (Dark Gray) -->
                <g id="sim1-stones">
                    <polygon points="95,65 105,62 108,72 98,75" fill="#64748b" stroke="#334155"/>
                    <polygon points="185,60 196,58 198,68 188,70" fill="#64748b" stroke="#334155"/>
                    <polygon points="275,60 286,63 283,73 273,70" fill="#64748b" stroke="#334155"/>
                </g>
                
                <!-- Husk (Papery Tan) -->
                <g id="sim1-husk">
                    <path d="M 125,115 Q 135,110 145,118" stroke="#d97706" stroke-width="2" fill="none"/>
                    <path d="M 215,110 Q 225,105 235,114" stroke="#d97706" stroke-width="2" fill="none"/>
                    <path d="M 305,112 Q 315,108 325,115" stroke="#d97706" stroke-width="2" fill="none"/>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="sim1RemoveStones()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 hover:bg-rose-500/30 transition">1. Remove Stones</button>
            <button onclick="sim1RemoveHusk()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30 transition">2. Blow Away Husk</button>
            <button onclick="sim1Reset()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Reset Tray</button>
        </div>
        <div id="sim1-status" class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300 text-center">
            Raw mixture contains wheat grains, dangerous gravel stones, and fibrous husk.
        </div>
    </div>
    """,

    2: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 2: Interactive Handpicking Lab</span>
            <span id="sim2-counter" class="text-xs font-bold text-emerald-400">Pebbles Left: 4 / 4</span>
        </div>
        <p class="text-xs text-slate-400">Click on each dark stone pebble among the polished rice grains to pick it out!</p>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim2-svg" viewBox="0 0 400 160" class="w-full h-full select-none cursor-pointer">
                <!-- Plate -->
                <ellipse cx="200" cy="80" rx="160" ry="70" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                <!-- Rice grains background -->
                <g fill="#f8fafc" opacity="0.85">
                    <ellipse cx="120" cy="65" rx="7" ry="3" transform="rotate(30 120 65)"/>
                    <ellipse cx="150" cy="85" rx="7" ry="3" transform="rotate(-40 150 85)"/>
                    <ellipse cx="180" cy="55" rx="7" ry="3" transform="rotate(15 180 55)"/>
                    <ellipse cx="210" cy="95" rx="7" ry="3" transform="rotate(60 210 95)"/>
                    <ellipse cx="240" cy="65" rx="7" ry="3" transform="rotate(-25 240 65)"/>
                    <ellipse cx="270" cy="85" rx="7" ry="3" transform="rotate(45 270 85)"/>
                    <ellipse cx="160" cy="110" rx="7" ry="3" transform="rotate(-10 160 110)"/>
                    <ellipse cx="230" cy="115" rx="7" ry="3" transform="rotate(35 230 115)"/>
                    <ellipse cx="190" cy="75" rx="7" ry="3" transform="rotate(-55 190 75)"/>
                </g>
                <!-- Clickable Stone Pebbles -->
                <g id="sim2-pebbles">
                    <polygon id="pebble-1" points="135,70 145,67 148,77 138,80" fill="#78716c" stroke="#44403c" stroke-width="1.5" onclick="sim2PickPebble(1)" class="hover:opacity-75 transition"/>
                    <polygon id="pebble-2" points="175,90 186,88 188,98 178,100" fill="#57534e" stroke="#292524" stroke-width="1.5" onclick="sim2PickPebble(2)" class="hover:opacity-75 transition"/>
                    <polygon id="pebble-3" points="220,60 231,63 228,73 218,70" fill="#78716c" stroke="#44403c" stroke-width="1.5" onclick="sim2PickPebble(3)" class="hover:opacity-75 transition"/>
                    <polygon id="pebble-4" points="255,95 265,92 268,102 258,105" fill="#57534e" stroke="#292524" stroke-width="1.5" onclick="sim2PickPebble(4)" class="hover:opacity-75 transition"/>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <span id="sim2-status" class="text-xs text-slate-300">Click individual stones to handpick them.</span>
            <button onclick="sim2Reset()" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 text-xs hover:bg-slate-700 transition">Reset Plate</button>
        </div>
    </div>
    """,

    3: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 3: Traditional Agricultural Threshing</span>
            <span id="sim3-strike-count" class="text-xs font-bold text-amber-400">Strikes: 0</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim3-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Ground & Wooden Log -->
                <line x1="20" y1="140" x2="380" y2="140" stroke="#334155" stroke-width="2"/>
                <rect x="180" y="110" width="80" height="30" rx="5" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                <text x="220" y="128" fill="#fde68a" font-size="10" text-anchor="middle" font-weight="bold">Hard Wooden Log</text>

                <!-- Farmer Arm & Wheat Sheaf Bundle -->
                <g id="sim3-sheaf" transform="rotate(-30 140 60)" style="transition: transform 0.25s ease-in-out;">
                    <!-- Stalk bundle -->
                    <line x1="140" y1="60" x2="190" y2="110" stroke="#ca8a04" stroke-width="8" stroke-linecap="round"/>
                    <!-- Grains on stalk -->
                    <circle cx="195" cy="115" r="4" fill="#facc15"/>
                    <circle cx="190" cy="120" r="3.5" fill="#facc15"/>
                    <circle cx="200" cy="110" r="3.5" fill="#facc15"/>
                </g>

                <!-- Released Grains Pile -->
                <g id="sim3-grain-pile" opacity="0">
                    <ellipse cx="220" cy="138" rx="25" ry="6" fill="#facc15"/>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim3Strike()" class="px-4 py-2 rounded-xl text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30 transition flex items-center gap-1.5">
                <span>💥</span>
                <span>Strike Stalks on Log</span>
            </button>
            <span id="sim3-msg" class="text-xs text-slate-300">Impact inertia snaps brittle grains free!</span>
        </div>
    </div>
    """,

    4: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 4: Motorized Combine Thresher</span>
            <span id="sim4-rpm-badge" class="text-xs font-bold text-cyan-400 font-mono">Drum: 800 RPM</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim4-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Combine Chassis -->
                <rect x="40" y="30" width="320" height="100" rx="10" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
                <!-- Spinning Threshing Cylinder -->
                <circle id="sim4-drum" cx="150" cy="80" r="30" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                <line id="sim4-spoke1" x1="125" y1="80" x2="175" y2="80" stroke="#38bdf8" stroke-width="2"/>
                <line id="sim4-spoke2" x1="150" y1="55" x2="150" y2="105" stroke="#38bdf8" stroke-width="2"/>
                <text x="150" y="84" fill="#bae6fd" font-size="8" text-anchor="middle" font-weight="bold">Drum</text>

                <!-- Crop Infeed -->
                <path d="M 10 70 L 40 75 L 40 85 L 10 90 Z" fill="#ca8a04"/>
                <text x="25" y="65" fill="#fde047" font-size="8" text-anchor="middle">Infeed</text>

                <!-- Blower Fan & Chaff Exhaust -->
                <path d="M 220 50 L 340 40" stroke="#f97316" stroke-width="4" stroke-dasharray="4,4"/>
                <text x="290" y="35" fill="#fdba74" font-size="9" font-weight="bold">Chaff Exhaust 💨</text>

                <!-- Clean Grain Chute -->
                <path d="M 220 110 L 290 130" stroke="#eab308" stroke-width="4"/>
                <text x="310" y="125" fill="#fef08a" font-size="9" font-weight="bold">Clean Grain 🌾</text>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-300">
                <span>Drum Throttle:</span>
                <span id="sim4-rate-val">Processing: 40 Quintals/hr</span>
            </div>
            <input type="range" id="sim4-slider" min="400" max="1400" step="100" value="800" oninput="sim4UpdateSpeed(this.value)" class="w-full accent-cyan-500">
        </div>
    </div>
    """,

    5: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 5: Aerodynamic Winnowing Lab</span>
            <span id="sim5-wind-badge" class="text-xs font-bold text-cyan-400">Wind: 18 km/h</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim5-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Ground -->
                <line x1="20" y1="140" x2="380" y2="140" stroke="#334155" stroke-width="2"/>
                <!-- Raised Stool -->
                <rect x="70" y="90" width="30" height="50" fill="#64748b"/>
                <!-- Worker Avatar -->
                <circle cx="85" cy="55" r="10" fill="#f87171"/>
                <line x1="85" y1="65" x2="85" y2="90" stroke="#f87171" stroke-width="3"/>
                <!-- Bamboo Soop -->
                <path d="M 85 65 L 115 55 L 130 62 L 95 72 Z" fill="#b45309" stroke="#78350f"/>
                
                <!-- Falling Trajectories -->
                <!-- Heavy Grains (Vertical Downward) -->
                <g id="sim5-grains-falling">
                    <circle cx="115" cy="85" r="2.5" fill="#facc15"/>
                    <circle cx="118" cy="105" r="2.5" fill="#facc15"/>
                    <circle cx="116" cy="125" r="2.5" fill="#facc15"/>
                    <ellipse cx="118" cy="139" rx="15" ry="4" fill="#facc15"/>
                    <text x="118" y="152" fill="#fef08a" font-size="8" text-anchor="middle">Heavy Grains</text>
                </g>

                <!-- Light Husk (Curved trajectory drifting right) -->
                <g id="sim5-husk-falling">
                    <path d="M 120 65 Q 180 80 250 138" fill="none" stroke="#d97706" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <ellipse cx="255" cy="139" rx="22" ry="4" fill="#d97706"/>
                    <text x="255" y="152" fill="#fdba74" font-size="8" text-anchor="middle">Blown Husk (Fodder)</text>
                </g>

                <!-- Wind Arrows -->
                <g opacity="0.6">
                    <path d="M 140 40 L 220 40 M 215 35 L 225 40 L 215 45" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="180" y="32" fill="#38bdf8" font-size="8">Wind Flow 💨</text>
                </g>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-300">
                <span>Crosswind Velocity:</span>
                <span id="sim5-wind-text">Moderate Breeze (18 km/h)</span>
            </div>
            <input type="range" min="5" max="35" value="18" oninput="sim5ChangeWind(this.value)" class="w-full accent-cyan-500">
        </div>
    </div>
    """,

    6: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 6: Dual-Mode Sieving Simulator</span>
            <div class="flex gap-1.5">
                <button onclick="sim6SetMode('flour')" id="sim6-btn-flour" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-600 text-white">Kitchen Flour</button>
                <button onclick="sim6SetMode('sand')" id="sim6-btn-sand" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">Construction Sand</button>
            </div>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim6-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Sieve Frame -->
                <g id="sim6-sieve" style="transition: transform 0.1s linear;">
                    <rect x="120" y="55" width="160" height="20" rx="3" fill="#334155" stroke="#64748b"/>
                    <!-- Mesh Line -->
                    <line x1="120" y1="70" x2="280" y2="70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>
                    <!-- Trapped Large Particles (Bran or Pebbles) -->
                    <circle cx="150" cy="65" r="4" fill="#b45309"/>
                    <circle cx="180" cy="64" r="5" fill="#78350f"/>
                    <circle cx="210" cy="66" r="4.5" fill="#b45309"/>
                    <circle cx="240" cy="65" r="4" fill="#78350f"/>
                    <text id="sim6-top-label" x="200" y="48" fill="#fdba74" font-size="8" text-anchor="middle" font-weight="bold">Retained: Wheat Bran (Choker)</text>
                </g>

                <!-- Passing Fine Particles -->
                <g id="sim6-falling">
                    <circle cx="160" cy="95" r="1.5" fill="#f8fafc"/>
                    <circle cx="190" cy="110" r="1.5" fill="#f8fafc"/>
                    <circle cx="220" cy="100" r="1.5" fill="#f8fafc"/>
                    <circle cx="250" cy="115" r="1.5" fill="#f8fafc"/>
                </g>

                <!-- Collection Tray -->
                <path d="M 130 135 L 270 135 L 260 145 L 140 145 Z" fill="#1e293b" stroke="#475569"/>
                <text id="sim6-bottom-label" x="200" y="152" fill="#bae6fd" font-size="8" text-anchor="middle">Passed: Fine Flour Powder</text>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim6Shake()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 hover:bg-indigo-500/30 transition">👋 Shake Sieve</button>
            <span id="sim6-desc" class="text-xs text-slate-300">Pores allow smaller particles to pass while blocking larger ones.</span>
        </div>
    </div>
    """,

    7: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 7: Coastal Salt Pan Evaporator</span>
            <span id="sim7-salinity-badge" class="text-xs font-bold text-amber-400">Salinity: 3.5% (Seawater)</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim7-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Sun with animated rays -->
                <circle cx="60" cy="40" r="18" fill="#f59e0b"/>
                <g stroke="#f59e0b" stroke-width="2" opacity="0.6">
                    <line x1="60" y1="15" x2="60" y2="5"/>
                    <line x1="60" y1="65" x2="60" y2="75"/>
                    <line x1="35" y1="40" x2="25" y2="40"/>
                    <line x1="85" y1="40" x2="95" y2="40"/>
                </g>
                <text x="60" y="90" fill="#fcd34d" font-size="8" text-anchor="middle">Solar Insolation</text>

                <!-- Shallow Salt Pan Reservoir -->
                <rect x="130" y="60" width="240" height="70" rx="4" fill="#334155" stroke="#64748b" stroke-width="2"/>
                
                <!-- Liquid Seawater Layer (Height decreases with evaporation) -->
                <rect id="sim7-water-layer" x="132" y="65" width="236" height="55" fill="#0284c7" opacity="0.75"/>

                <!-- Salt Crust Crystals at Bottom (Grows as water vanishes) -->
                <rect id="sim7-salt-crust" x="132" y="115" width="236" height="12" fill="#ffffff" opacity="0.2"/>
                <text id="sim7-salt-label" x="250" y="125" fill="#0f172a" font-size="8" text-anchor="middle" font-weight="bold" opacity="0">Pure Common Salt (NaCl)</text>

                <!-- Rising Vapour squiggles -->
                <g id="sim7-vapour" opacity="0.5">
                    <path d="M 180 55 Q 185 45 180 35" stroke="#93c5fd" fill="none" stroke-width="1.5"/>
                    <path d="M 240 55 Q 245 45 240 35" stroke="#93c5fd" fill="none" stroke-width="1.5"/>
                    <path d="M 300 55 Q 305 45 300 35" stroke="#93c5fd" fill="none" stroke-width="1.5"/>
                </g>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-300">
                <span>Solar Exposure Days:</span>
                <span id="sim7-days-val" class="font-bold text-cyan-300">Day 1 (Fresh Seawater Intake)</span>
            </div>
            <input type="range" min="1" max="5" value="1" oninput="sim7SetDay(this.value)" class="w-full accent-amber-500">
        </div>
    </div>
    """,

    8: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 8: China Dish Evaporation Lab</span>
            <span id="sim8-burner-state" class="text-xs font-bold text-slate-400">Burner: OFF</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim8-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Tripod Stand -->
                <line x1="160" y1="80" x2="140" y2="145" stroke="#64748b" stroke-width="3"/>
                <line x1="240" y1="80" x2="260" y2="145" stroke="#64748b" stroke-width="3"/>
                <line x1="150" y1="80" x2="250" y2="80" stroke="#94a3b8" stroke-width="2"/> <!-- Wire Gauze -->

                <!-- Spirit Lamp Burner -->
                <rect x="185" y="115" width="30" height="25" rx="3" fill="#475569"/>
                <!-- Flame -->
                <path id="sim8-flame" d="M 200 115 Q 192 100 200 90 Q 208 100 200 115 Z" fill="#f59e0b" opacity="0"/>

                <!-- China Dish -->
                <path d="M 170 80 Q 200 95 230 80 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                <!-- Solution in Dish -->
                <path id="sim8-liquid" d="M 175 82 Q 200 92 225 82 Z" fill="#38bdf8"/>
                <!-- White Salt Residue -->
                <path id="sim8-residue" d="M 178 86 Q 200 92 222 86 Z" fill="#ffffff" opacity="0"/>

                <!-- Steam Waves -->
                <g id="sim8-steam" opacity="0">
                    <path d="M 195 75 Q 190 65 195 55" stroke="#cbd5e1" stroke-width="1.5" fill="none"/>
                    <path d="M 205 75 Q 210 65 205 55" stroke="#cbd5e1" stroke-width="1.5" fill="none"/>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim8ToggleBurner()" id="sim8-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30 transition">🔥 Ignite Burner</button>
            <span id="sim8-info" class="text-xs text-slate-300">Click to boil water and crystallize white salt.</span>
        </div>
    </div>
    """,

    9: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 9: Sedimentation Settling Clock</span>
            <span id="sim9-time-badge" class="text-xs font-bold text-amber-400">Time: 0 mins (Murky)</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim9-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Beaker -->
                <rect x="150" y="30" width="100" height="110" rx="4" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
                
                <!-- Murky Water -->
                <rect id="sim9-water" x="152" y="45" width="96" height="93" fill="#78350f" opacity="0.8"/>

                <!-- Settling Sediment Cake -->
                <rect id="sim9-sediment" x="152" y="125" width="96" height="13" fill="#451a03" opacity="0.3"/>
                <text id="sim9-sed-label" x="200" y="135" fill="#fde68a" font-size="8" text-anchor="middle" opacity="0">Sediment</text>

                <!-- Floating Chaff -->
                <g id="sim9-floating">
                    <line x1="165" y1="48" x2="175" y2="47" stroke="#fbbf24" stroke-width="2"/>
                    <line x1="210" y1="46" x2="225" y2="48" stroke="#fbbf24" stroke-width="2"/>
                </g>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-300">
                <span>Undisturbed Settling Time:</span>
                <span id="sim9-clarity-val" class="font-bold text-cyan-300">0% Clarified</span>
            </div>
            <input type="range" min="0" max="20" value="0" oninput="sim9SetTime(this.value)" class="w-full accent-amber-500">
        </div>
    </div>
    """,

    10: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 10: Careful Decantation Angle</span>
            <span id="sim10-angle-badge" class="text-xs font-bold text-cyan-400 font-mono">Tilt: 0°</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim10-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Receiver Beaker on Right -->
                <rect x="260" y="70" width="70" height="70" rx="3" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                <rect id="sim10-recv-liquid" x="262" y="130" width="66" height="8" fill="#38bdf8" opacity="0.6"/>

                <!-- Tilting Beaker on Left -->
                <g id="sim10-tilt-beaker" transform="rotate(0 160 110)" style="transition: transform 0.15s ease-out;">
                    <rect x="110" y="40" width="60" height="80" rx="3" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
                    <rect x="112" y="60" width="56" height="58" fill="#38bdf8" opacity="0.5"/>
                    <rect x="112" y="105" width="56" height="13" fill="#451a03"/> <!-- Sediment -->
                </g>

                <!-- Liquid Stream into Receiver -->
                <path id="sim10-stream" d="M 175 60 Q 220 80 270 120" stroke="#38bdf8" stroke-width="3" fill="none" opacity="0"/>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-300">
                <span>Vessel Tilt Angle:</span>
                <span id="sim10-status-msg" class="text-emerald-400 font-bold">Stable</span>
            </div>
            <input type="range" min="0" max="60" value="0" oninput="sim10SetTilt(this.value)" class="w-full accent-indigo-500">
        </div>
    </div>
    """,

    11: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 11: 4-Step Filter Cone Folding</span>
            <span id="sim11-step-badge" class="text-xs font-bold text-cyan-400">Step 1: Circle</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim11-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Folding Visual Transformations -->
                <g id="sim11-stage">
                    <circle id="sim11-shape" cx="200" cy="80" r="50" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
                </g>
                <text id="sim11-caption" x="200" y="148" fill="#cbd5e1" font-size="10" text-anchor="middle" font-weight="bold">Flat Circular Filter Paper (110 mm)</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="sim11Step(1)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold">1. Circle</button>
            <button onclick="sim11Step(2)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold">2. Semi</button>
            <button onclick="sim11Step(3)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold">3. Quadrant</button>
            <button onclick="sim11Step(4)" class="px-2 py-1.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold">4. 60° Cone</button>
        </div>
    </div>
    """,

    12: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 12: Funnel Filtration Laboratory</span>
            <span id="sim12-filtrate-badge" class="text-xs font-bold text-emerald-400">Filtrate: 0 mL</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim12-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Glass Funnel -->
                <polygon points="170,20 230,20 205,65 205,95 195,95 195,65" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Filter Paper Cone inside Funnel -->
                <polygon points="174,22 226,22 200,63" fill="#f8fafc" stroke="#cbd5e1"/>
                <!-- Muddy Residue trapped inside Paper -->
                <polygon id="sim12-residue" points="180,26 220,26 200,60" fill="#78350f" opacity="0"/>
                <text id="sim12-res-label" x="250" y="35" fill="#f59e0b" font-size="8" opacity="0">Residue (Mud)</text>

                <!-- Conical Receiver Flask Below -->
                <path d="M 185 95 L 215 95 L 235 145 L 165 145 Z" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
                <!-- Clear Filtrate Accumulation -->
                <path id="sim12-filtrate" d="M 172 135 L 228 135 L 233 144 L 167 144 Z" fill="#0284c7" opacity="0"/>
                <text id="sim12-fil-label" x="250" y="135" fill="#38bdf8" font-size="8" opacity="0">Filtrate (Clear Water)</text>

                <!-- Dripping Droplet -->
                <circle id="sim12-drop" cx="200" cy="105" r="2.5" fill="#38bdf8" opacity="0"/>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim12StartFilter()" id="sim12-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 hover:bg-cyan-500/30 transition">💧 Pour Muddy Water</button>
            <span id="sim12-info" class="text-xs text-slate-300">Traps solid residue while clear filtrate drops below.</span>
        </div>
    </div>
    """,

    13: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 13: Traditional Curd Churning (Mathni)</span>
            <span id="sim13-butter-badge" class="text-xs font-bold text-amber-400">Butter: 0 g</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim13-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Earthen Matka Pot -->
                <ellipse cx="200" cy="140" rx="40" ry="10" fill="#451a03"/>
                <path d="M 160 50 Q 130 90 160 135 L 240 135 Q 270 90 240 50 Z" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                <ellipse cx="200" cy="50" rx="40" ry="8" fill="#9a3412"/>

                <!-- Curd & Buttermilk Liquid -->
                <path d="M 165 70 Q 140 100 165 130 L 235 130 Q 260 100 235 70 Z" fill="#f8fafc" opacity="0.9"/>

                <!-- Floating Butter Blobs (Appear as churned) -->
                <g id="sim13-butter-blobs" opacity="0">
                    <circle cx="185" cy="73" r="7" fill="#fde047"/>
                    <circle cx="215" cy="72" r="8" fill="#facc15"/>
                    <circle cx="200" cy="76" r="6" fill="#fde047"/>
                    <text x="200" y="66" fill="#713f12" font-size="7" text-anchor="middle" font-weight="bold">Butter (Makhan)</text>
                </g>

                <!-- Wooden Mathni Churner Rod & Blades -->
                <g id="sim13-mathni" style="transition: transform 0.1s linear;">
                    <rect x="197" y="10" width="6" height="110" fill="#d97706"/>
                    <line x1="180" y1="110" x2="220" y2="110" stroke="#b45309" stroke-width="4"/>
                    <line x1="185" y1="118" x2="215" y2="118" stroke="#b45309" stroke-width="4"/>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim13Churn()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30 transition">🌀 Pull Mathni Ropes</button>
            <span id="sim13-status" class="text-xs text-slate-300">Continuous spinning separates light butter from dense buttermilk.</span>
        </div>
    </div>
    """,

    14: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 14: Magnetic Wand Extraction</span>
            <span id="sim14-pins-badge" class="text-xs font-bold text-emerald-400">Iron Nails Retrieved: 0 / 5</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim14-svg" viewBox="0 0 400 160" class="w-full h-full select-none cursor-pointer">
                <!-- Wooden Sawdust Tray -->
                <rect x="50" y="90" width="300" height="50" rx="5" fill="#ca8a04" opacity="0.3" stroke="#ca8a04" stroke-width="1.5"/>
                <text x="200" y="130" fill="#fef08a" font-size="9" text-anchor="middle">Non-Magnetic Sawdust Bed</text>

                <!-- Iron Nails Scattered -->
                <g id="sim14-nails">
                    <line id="nail-1" x1="90" y1="105" x2="105" y2="115" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                    <line id="nail-2" x1="140" y1="110" x2="155" y2="100" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                    <line id="nail-3" x1="195" y1="112" x2="210" y2="112" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                    <line id="nail-4" x1="250" y1="105" x2="265" y2="115" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                    <line id="nail-5" x1="300" y1="110" x2="315" y2="105" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                </g>

                <!-- Magnetic Bar (Moves down on hover/click) -->
                <g id="sim14-magnet" transform="translate(160, 25)" style="transition: transform 0.3s ease-out;">
                    <rect x="0" y="0" width="40" height="20" fill="#ef4444"/> <!-- North -->
                    <text x="20" y="14" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">N</text>
                    <rect x="40" y="0" width="40" height="20" fill="#3b82f6"/> <!-- South -->
                    <text x="60" y="14" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">S</text>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim14HoverMagnet()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 hover:bg-indigo-500/30 transition">🧲 Sweep Magnet</button>
            <button onclick="sim14Reset()" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 text-xs hover:bg-slate-700 transition">Reset</button>
        </div>
    </div>
    """,

    15: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 15: Scrap Yard Electromagnet Crane</span>
            <span id="sim15-power-badge" class="text-xs font-bold text-rose-400 font-mono">Current: OFF</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <svg id="sim15-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- Crane Arm & Cable -->
                <line x1="200" y1="10" x2="200" y2="50" stroke="#475569" stroke-width="3"/>
                
                <!-- Circular Electromagnetic Disc -->
                <ellipse id="sim15-disc" cx="200" cy="55" rx="45" ry="12" fill="#334155" stroke="#64748b" stroke-width="2"/>
                <text x="200" y="58" fill="#e2e8f0" font-size="8" text-anchor="middle" font-weight="bold">Electromagnet</text>

                <!-- Magnetic Field Glow (When ON) -->
                <ellipse id="sim15-glow" cx="200" cy="55" rx="52" ry="16" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" opacity="0"/>

                <!-- Scrap Iron Clinging to Magnet -->
                <g id="sim15-clinging-iron" opacity="0">
                    <rect x="180" y="65" width="40" height="8" fill="#64748b"/>
                    <polygon points="170,72 190,72 180,82" fill="#475569"/>
                    <rect x="205" y="66" width="25" height="10" fill="#64748b"/>
                </g>

                <!-- Recycling Truck Bin on Right -->
                <rect x="290" y="90" width="80" height="50" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
                <text x="330" y="120" fill="#bae6fd" font-size="8" text-anchor="middle">Scrap Truck</text>

                <!-- Ground Junk Pile on Left -->
                <path d="M 50 140 Q 90 110 130 140 Z" fill="#475569"/>
                <text x="90" y="152" fill="#94a3b8" font-size="8" text-anchor="middle">Mixed Waste</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="sim15PowerOn()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/30 transition">⚡ Power ON (Magnetize)</button>
            <button onclick="sim15PowerOff()" class="px-2.5 py-1.5 rounded-lg text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 hover:bg-rose-500/30 transition">🔌 Power OFF (Release)</button>
        </div>
    </div>
    """,

    16: """
    <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Sim 16: Multi-Step Separation Pipeline</span>
            <span id="sim16-stage-badge" class="text-xs font-bold text-amber-400">Stage: 1 / 3</span>
        </div>
        <div class="relative w-full h-44 bg-slate-900 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim16-svg" viewBox="0 0 400 160" class="w-full h-full">
                <!-- 3 Pipeline Stages Boxes -->
                <!-- Step 1: Dissolution -->
                <g id="sim16-box1" opacity="1">
                    <rect x="30" y="40" width="90" height="80" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
                    <text x="75" y="60" fill="#a5b4fc" font-size="9" text-anchor="middle" font-weight="bold">1. Dissolve</text>
                    <text x="75" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Salt dissolves</text>
                    <text x="75" y="95" fill="#facc15" font-size="8" text-anchor="middle">Sand stays solid</text>
                </g>

                <path d="M 125 80 L 150 80" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>

                <!-- Step 2: Filtration -->
                <g id="sim16-box2" opacity="0.4">
                    <rect x="155" y="40" width="90" height="80" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                    <text x="200" y="60" fill="#fcd34d" font-size="9" text-anchor="middle" font-weight="bold">2. Filter</text>
                    <text x="200" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Sand: Residue</text>
                    <text x="200" y="95" fill="#38bdf8" font-size="8" text-anchor="middle">Salt-water: Filtrate</text>
                </g>

                <path d="M 250 80 L 275 80" stroke="#64748b" stroke-width="2"/>

                <!-- Step 3: Evaporation -->
                <g id="sim16-box3" opacity="0.4">
                    <rect x="280" y="40" width="90" height="80" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                    <text x="325" y="60" fill="#6ee7b7" font-size="9" text-anchor="middle" font-weight="bold">3. Evaporate</text>
                    <text x="325" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Steam condenses</text>
                    <text x="325" y="95" fill="#ffffff" font-size="8" text-anchor="middle">Pure salt crystals</text>
                </g>
            </svg>
        </div>
        <div class="flex items-center justify-between">
            <button onclick="sim16Advance()" id="sim16-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/30 transition">Next Separation Stage ➔</button>
            <span id="sim16-status" class="text-xs text-slate-300 font-medium">Stage 1: Adding water dissolves soluble salt.</span>
        </div>
    </div>
    """
}


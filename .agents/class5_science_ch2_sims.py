"""
Class 5 Science Chapter 2: Journey of a River
16 Bespoke Interactive SVG/HTML Simulators
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Godavari Source & Eastward Journey</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Course: Origin to Bay of Bengal (1,465 km)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Western Ghats Mountain Peaks (Left / West) -->
                <polygon points="10,170 45,60 85,170" fill="#334155" />
                <polygon points="35,85 45,60 55,85" fill="#64748b" />
                <text x="45" y="50" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Brahmagiri Hills</text>
                <text x="45" y="180" fill="#cbd5e1" font-size="7" text-anchor="middle">Trimbakeshwar (1,067m)</text>

                <!-- Spring Origin Sparkle -->
                <circle cx="45" cy="85" r="5" fill="#38bdf8" filter="drop-shadow(0 0 5px #0284c7)" />
                <circle cx="45" cy="85" r="2" fill="#ffffff" />

                <!-- Deccan Plateau Landscape (Center) -->
                <rect x="85" y="140" width="165" height="60" fill="#78350f" opacity="0.6" />
                <text x="165" y="160" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">Deccan Plateau (Eastward Slope)</text>

                <!-- Flowing Godavari River Ribbon -->
                <path id="sim1-river" d="M 45,85 Q 90,110 130,120 T 210,135 T 280,150 L 320,165 L 320,185 L 280,170 Q 210,155 130,135 T 45,95 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />

                <!-- Bay of Bengal Coast (Right / East) -->
                <path d="M 270,30 Q 285,100 320,130 L 320,0 L 270,0 Z" fill="#0369a1" opacity="0.8" />
                <text x="300" y="55" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Bay of</text>
                <text x="300" y="68" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Bengal</text>

                <!-- Distance Marker Flag -->
                <g id="sim1-boat" transform="translate(140, 115)">
                    <polygon points="0,0 12,0 8,6 0,6" fill="#f59e0b" />
                    <line x1="6" y1="0" x2="6" y2="-8" stroke="#f8fafc" stroke-width="1" />
                    <polygon points="6,-8 14,-4 6,0" fill="#ef4444" />
                </g>

                <rect x="90" y="15" width="140" height="26" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim1-distance-text" x="160" y="32" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Length: 1,465 km (Dakshin Ganga)</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="navigateGodavariCourse('source')" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🏔️ Inspect Mountain Source (Trimbakeshwar)
            </button>
            <button onclick="navigateGodavariCourse('delta')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌊 Inspect Mouth & Delta (Bay of Bengal)
            </button>
        </div>
        <div id="sim1-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            The Godavari originates as a clear mountain spring in the Brahmagiri Hills at Trimbakeshwar, flowing 1,465 km eastward across Maharashtra, Telangana, and Andhra Pradesh into the Bay of Bengal.
        </div>
    </div>
    """,

    2: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Tributaries & River Confluence (Sangam)</span>
            <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Active Feeder: Manjira River</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Landscape Bed -->
                <rect x="0" y="0" width="320" height="200" fill="#1e293b" opacity="0.3" />

                <!-- Main Godavari Trunk Channel (Widening from Left to Right) -->
                <path id="sim2-trunk" d="M 0,95 Q 80,95 130,90 T 220,80 T 320,70 L 320,130 Q 220,120 130,115 T 80,105 L 0,105 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <text x="40" y="103" fill="#ffffff" font-size="8" font-weight="bold">Godavari Trunk</text>

                <!-- Tributary 1: Manjira (Right Bank, from Bottom-Left) -->
                <g id="sim2-trib-manjira">
                    <path d="M 60,200 Q 80,150 110,110" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round" />
                    <text x="65" y="170" fill="#fde047" font-size="7.5" font-weight="bold" transform="rotate(-45 65 170)">Manjira ➔</text>
                </g>

                <!-- Tributary 2: Indravati (Left Bank, from Top-Center) -->
                <g id="sim2-trib-indravati">
                    <path d="M 180,0 Q 185,50 200,80" stroke="#10b981" stroke-width="4.5" fill="none" stroke-linecap="round" />
                    <text x="185" y="30" fill="#86efac" font-size="7.5" font-weight="bold" transform="rotate(45 185 30)">Indravati ➔</text>
                </g>

                <!-- Tributary 3: Sabari (Left Bank, from Top-Right) -->
                <g id="sim2-trib-sabari">
                    <path d="M 270,0 Q 265,45 260,75" stroke="#38bdf8" stroke-width="4" fill="none" stroke-linecap="round" />
                    <text x="272" y="35" fill="#bae6fd" font-size="7.5" font-weight="bold" transform="rotate(60 272 35)">Sabari ➔</text>
                </g>

                <!-- Sangam / Confluence Marker -->
                <circle cx="200" cy="80" r="6" fill="#f43f5e" filter="drop-shadow(0 0 6px #ef4444)" />
                <circle cx="200" cy="80" r="2.5" fill="#ffffff" />
                <text x="200" y="100" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Sangam (Confluence)</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="toggleTributary('manjira')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🌾 Manjira River
            </button>
            <button onclick="toggleTributary('indravati')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🌲 Indravati River
            </button>
            <button onclick="toggleTributary('sabari')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-300 border border-slate-700">
                🏔️ Sabari River
            </button>
        </div>
        <div id="sim2-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Tributaries like the Manjira, Indravati, and Sabari drain rainfall from surrounding states and pour into the Godavari, making the main river channel wider, deeper, and more powerful.
        </div>
    </div>
    """,

    3: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Perennial vs Seasonal River Flow</span>
            <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Season: Peak Summer (May)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#050814" />

                <!-- Left Half: Perennial River (Godavari) -->
                <rect x="10" y="20" width="145" height="160" rx="6" fill="#0f172a" stroke="#0284c7" />
                <text x="82" y="38" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Perennial River (Year-Round)</text>
                <!-- River channel flowing constantly -->
                <path d="M 20,70 Q 82,60 145,75 L 145,130 Q 82,140 20,125 Z" fill="#15803d" />
                <path id="sim3-perennial-water" d="M 20,85 Q 82,75 145,90 L 145,115 Q 82,125 20,110 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                <text x="82" y="103" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Continuous Flow</text>
                <text x="82" y="155" fill="#a5f3fc" font-size="7.5" text-anchor="middle">Fed by deep springs & aquifers</text>

                <!-- Right Half: Seasonal Rain-Fed River -->
                <rect x="165" y="20" width="145" height="160" rx="6" fill="#0f172a" stroke="#d97706" />
                <text x="237" y="38" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Seasonal River (Rain-Fed)</text>
                <!-- Riverbed banks -->
                <path d="M 175,70 Q 237,60 300,75 L 300,130 Q 237,140 175,125 Z" fill="#57534e" />
                <!-- Water or Dry Sand -->
                <path id="sim3-seasonal-bed" d="M 175,85 Q 237,75 300,90 L 300,115 Q 237,125 175,110 Z" fill="#ca8a04" stroke="#eab308" stroke-width="1" />
                <text id="sim3-seasonal-status" x="237" y="103" fill="#fef08a" font-size="7.5" font-weight="bold" text-anchor="middle">Dry Cracked Sandbed</text>
                <text x="237" y="155" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Flows only during monsoon rains</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setRiverSeason('summer')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ☀️ Scorching Summer (May Heat)
            </button>
            <button onclick="setRiverSeason('monsoon')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌧️ Monsoon Downpour (July Rain)
            </button>
        </div>
        <div id="sim3-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Perennial rivers like the Godavari flow year-round because deep groundwater aquifers sustain baseflow even during hot summers. Seasonal rivers flow only in the monsoon and dry up into sand.
        </div>
    </div>
    """,

    4: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Riparian Wildlife & Forest Corridor</span>
            <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Creature: Royal Bengal Tiger</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Riverside Forest (Dense Teak & Red Sandalwood) -->
                <path d="M 0,140 Q 60,110 120,130 T 240,115 T 320,135 L 320,0 L 0,0 Z" fill="#14532d" />
                <rect x="0" y="140" width="320" height="60" fill="#0284c7" />
                <text x="160" y="175" fill="#bae6fd" font-size="8" font-weight="bold" text-anchor="middle">Flowing Godavari River Current</text>

                <!-- Clickable Wildlife Nodes along Riverbank -->
                <!-- Tiger Node -->
                <g onclick="selectRiverCreature('tiger')" class="cursor-pointer" transform="translate(60, 95)">
                    <circle id="sim4-btn-tiger" cx="0" cy="0" r="22" fill="#ea580c" stroke="#fde047" stroke-width="2.5" />
                    <text x="0" y="5" font-size="14" text-anchor="middle">🐅</text>
                    <text x="0" y="32" fill="#fdba74" font-size="7.5" font-weight="bold" text-anchor="middle">Bengal Tiger</text>
                </g>

                <!-- Barking Deer Node -->
                <g onclick="selectRiverCreature('deer')" class="cursor-pointer" transform="translate(130, 85)">
                    <circle id="sim4-btn-deer" cx="0" cy="0" r="20" fill="#ca8a04" stroke="#fef08a" stroke-width="1.5" />
                    <text x="0" y="5" font-size="13" text-anchor="middle">🦌</text>
                    <text x="0" y="30" fill="#fef08a" font-size="7.5" font-weight="bold" text-anchor="middle">Barking Deer</text>
                </g>

                <!-- Indian Golden Gecko Node -->
                <g onclick="selectRiverCreature('gecko')" class="cursor-pointer" transform="translate(200, 80)">
                    <circle id="sim4-btn-gecko" cx="0" cy="0" r="20" fill="#15803d" stroke="#86efac" stroke-width="1.5" />
                    <text x="0" y="5" font-size="13" text-anchor="middle">🦎</text>
                    <text x="0" y="30" fill="#86efac" font-size="7.5" font-weight="bold" text-anchor="middle">Golden Gecko</text>
                </g>

                <!-- Red Sandalwood Tree Node -->
                <g onclick="selectRiverCreature('sandalwood')" class="cursor-pointer" transform="translate(270, 75)">
                    <circle id="sim4-btn-tree" cx="0" cy="0" r="20" fill="#7f1d1d" stroke="#fca5a5" stroke-width="1.5" />
                    <text x="0" y="5" font-size="13" text-anchor="middle">🌲</text>
                    <text x="0" y="30" fill="#fca5a5" font-size="7.5" font-weight="bold" text-anchor="middle">Red Sandal</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="selectRiverCreature('tiger')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-orange-300 border border-slate-700">
                🐅 Tiger
            </button>
            <button onclick="selectRiverCreature('deer')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🦌 Deer
            </button>
            <button onclick="selectRiverCreature('gecko')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🦎 Gecko
            </button>
            <button onclick="selectRiverCreature('sandalwood')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                🌲 Sandalwood
            </button>
        </div>
        <div id="sim4-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Riverside forest corridors sustain tigers, barking deer, and rare nocturnal Indian golden geckos, alongside fragrant native red sandalwood trees that thrive in fertile river valleys.
        </div>
    </div>
    """,

    5: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Coringa Mangrove Estuary & Tidal Roots</span>
            <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Tide Level: Low Tide (Roots Exposed)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040d1a" />

                <!-- Waterlogged Estuary Mud Bed -->
                <rect x="0" y="130" width="320" height="70" fill="#292524" />
                <text x="160" y="190" fill="#a8a29e" font-size="7.5" font-weight="bold" text-anchor="middle">Anaerobic Estuary Mud (Freshwater + Saltwater)</text>

                <!-- Mangrove Tree Center -->
                <g transform="translate(160, 80)">
                    <!-- Mangrove Canopy -->
                    <circle cx="0" cy="-35" r="32" fill="#15803d" stroke="#22c55e" stroke-width="1.5" />
                    <!-- Trunk -->
                    <rect x="-8" y="-15" width="16" height="40" fill="#78350f" />
                    
                    <!-- Arching Stilt Roots (Anchor against tides) -->
                    <path d="M -8,15 Q -30,35 -50,55" stroke="#78350f" stroke-width="4" fill="none" />
                    <path d="M 8,15 Q 30,35 50,55" stroke="#78350f" stroke-width="4" fill="none" />
                    <path d="M -4,20 Q -15,40 -25,55" stroke="#78350f" stroke-width="3" fill="none" />
                    <path d="M 4,20 Q 15,40 25,55" stroke="#78350f" stroke-width="3" fill="none" />
                </g>

                <!-- Vertical Breathing Roots (Pneumatophores) growing upward from mud -->
                <g id="sim5-pneumatophores" stroke="#ca8a04" stroke-width="2.5" stroke-linecap="round">
                    <line x1="40" y1="135" x2="40" y2="105" />
                    <line x1="55" y1="135" x2="55" y2="110" />
                    <line x1="70" y1="135" x2="70" y2="102" />
                    <line x1="90" y1="135" x2="90" y2="108" />
                    <line x1="230" y1="135" x2="230" y2="105" />
                    <line x1="250" y1="135" x2="250" y2="102" />
                    <line x1="270" y1="135" x2="270" y2="110" />
                    <line x1="285" y1="135" x2="285" y2="107" />
                </g>
                <text x="65" y="98" fill="#fde047" font-size="7.5" font-weight="bold">Pneumatophores</text>
                <text x="65" y="108" fill="#fef08a" font-size="6.5">(Breathing Roots)</text>

                <!-- Tidal Water Layer -->
                <rect id="sim5-tide-water" x="0" y="125" width="320" height="25" fill="#0284c7" opacity="0.45" />
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setMangroveTide('low')" class="p-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-xs font-bold text-white shadow transition">
                ⬇️ Low Tide (Pneumatophores Breathe Air)
            </button>
            <button onclick="setMangroveTide('high')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                ⬆️ High Tide (Brackish Ocean Surge)
            </button>
        </div>
        <div id="sim5-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In the Coringa delta, river freshwater mixes with seawater. Because waterlogged coastal mud lacks oxygen, mangrove trees send upward breathing roots (pneumatophores) like snorkels into the air!
        </div>
    </div>
    """,

    6: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Civilization Lifeline: River Water Uses</span>
            <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Selected: Agricultural Irrigation</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Central Flowing River -->
                <path d="M 0,70 Q 160,50 320,70 L 320,130 Q 160,150 0,130 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <text x="160" y="105" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">The Godavari Lifeline Current</text>

                <!-- Sector 1: Domestic Drinking Supply (Top-Left) -->
                <g onclick="selectWaterService('domestic')" class="cursor-pointer" transform="translate(60, 35)">
                    <rect id="sim6-card-domestic" x="-45" y="-18" width="90" height="36" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
                    <text x="0" y="-2" fill="#38bdf8" font-size="7.5" font-weight="bold" text-anchor="middle">🚰 Municipal Drinking</text>
                    <text x="0" y="10" fill="#94a3b8" font-size="6.5" text-anchor="middle">Filtered City Supply</text>
                </g>

                <!-- Sector 2: Agricultural Canal Irrigation (Bottom-Left) -->
                <g onclick="selectWaterService('farming')" class="cursor-pointer" transform="translate(60, 165)">
                    <rect id="sim6-card-farming" x="-45" y="-18" width="90" height="36" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" />
                    <text x="0" y="-2" fill="#4ade80" font-size="7.5" font-weight="bold" text-anchor="middle">🌾 Crop Irrigation</text>
                    <text x="0" y="10" fill="#94a3b8" font-size="6.5" text-anchor="middle">Rice & Sugarcane Canals</text>
                </g>

                <!-- Sector 3: Industrial Cooling & Power (Bottom-Right) -->
                <g onclick="selectWaterService('industry')" class="cursor-pointer" transform="translate(260, 165)">
                    <rect id="sim6-card-industry" x="-45" y="-18" width="90" height="36" rx="6" fill="#0f172a" stroke="#ca8a04" stroke-width="1" />
                    <text x="0" y="-2" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">🏭 Factory & Power</text>
                    <text x="0" y="10" fill="#94a3b8" font-size="6.5" text-anchor="middle">Turbines & Cooling</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="selectWaterService('domestic')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-300 border border-slate-700">
                🚰 Domestic Drinking
            </button>
            <button onclick="selectWaterService('farming')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🌾 Farm Irrigation
            </button>
            <button onclick="selectWaterService('industry')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🏭 Industry & Power
            </button>
        </div>
        <div id="sim6-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Canals divert river water to irrigate sprawling fields of paddy rice, sugarcane, and cotton, providing food security and rural livelihoods across the Deccan Plateau.
        </div>
    </div>
    """,

    7: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Livelihoods & Ecotourism at Papi Hills</span>
            <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Mode: Sustainable Ecotourism Cruise</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Papi Hills Gorge Cliffs on Both Sides -->
                <polygon points="0,170 30,30 90,120 120,160 0,160" fill="#14532d" />
                <polygon points="320,170 290,25 230,110 200,160 320,160" fill="#14532d" />
                <text x="60" y="45" fill="#86efac" font-size="8" font-weight="bold">Papi Hills Cliff</text>
                <text x="260" y="45" fill="#86efac" font-size="8" font-weight="bold">Papi Hills Cliff</text>

                <!-- Narrow Deep River Channel -->
                <rect x="0" y="140" width="320" height="60" fill="#0284c7" />

                <!-- Ecotourist Cruise Boat (Center) -->
                <g id="sim7-eco-boat" style="display: block;" transform="translate(160, 135)">
                    <path d="M -30,10 L 30,10 L 25,24 L -25,24 Z" fill="#f8fafc" stroke="#475569" stroke-width="1.5" />
                    <!-- Canopy Cover -->
                    <rect x="-22" y="-5" width="44" height="15" fill="#0284c7" rx="2" />
                    <text x="0" y="5" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Eco Cruise</text>
                    <text x="0" y="32" fill="#a5f3fc" font-size="7.5" font-weight="bold" text-anchor="middle">Zero Litter • Nature Observation</text>
                </g>

                <!-- Traditional Fisherman Boat -->
                <g id="sim7-fish-boat" style="display: none;" transform="translate(160, 135)">
                    <path d="M -25,12 L 25,12 L 20,22 L -20,22 Z" fill="#ca8a04" stroke="#78350f" stroke-width="1.5" />
                    <!-- Fisherman with Cast Net -->
                    <circle cx="5" cy="5" r="3" fill="#fde047" />
                    <line x1="5" y1="8" x2="5" y2="14" stroke="#fde047" stroke-width="1.5" />
                    <!-- Thrown Cast Net Arc -->
                    <path d="M 10,8 Q 35,0 45,15" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2,2" fill="none" />
                    <text x="0" y="32" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">Traditional Cast-Net Fishery</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setLivelihoodMode('tour')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚤 Ecotourism (Zero Pollution Sightseeing)
            </button>
            <button onclick="setLivelihoodMode('fish')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🎣 Traditional Fisherfolk (Cast Nets)
            </button>
        </div>
        <div id="sim7-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Ecotourism enables travelers to experience the natural grandeur of the Papi Hills gorge without littering, while traditional fishing provides sustainable protein and livelihoods for riverbank families.
        </div>
    </div>
    """,

    8: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Hydroelectric Dam & Reservoir Engineering</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Status: Turbines Generating Electricity</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Reservoir Behind Dam Wall (Left) -->
                <rect x="0" y="45" width="130" height="155" fill="#0284c7" />
                <text x="65" y="70" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Reservoir Lake</text>
                <text x="65" y="82" fill="#bae6fd" font-size="7" text-anchor="middle">Stored Monsoon Surplus</text>

                <!-- Massive Concrete Dam Wall (Center) -->
                <polygon points="130,45 155,45 185,200 130,200" fill="#475569" stroke="#94a3b8" stroke-width="1.5" />
                <text x="145" y="35" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle">Dam Wall</text>

                <!-- Penstock Pipe through Dam Base -->
                <line x1="120" y1="160" x2="190" y2="160" stroke="#0f172a" stroke-width="12" />
                <line x1="120" y1="160" x2="190" y2="160" stroke="#38bdf8" stroke-width="8" stroke-dasharray="4,2" />

                <!-- Powerhouse & Generator Turbine -->
                <rect x="190" y="130" width="45" height="50" rx="3" fill="#1e293b" stroke="#cbd5e1" />
                <!-- Turbine Spinning Blades -->
                <circle id="sim8-turbine" cx="212" cy="155" r="10" fill="#ca8a04" stroke="#facc15" stroke-width="1.5" />
                <line x1="202" y1="155" x2="222" y2="155" stroke="#ffffff" stroke-width="1.5" />
                <line x1="212" y1="145" x2="212" y2="165" stroke="#ffffff" stroke-width="1.5" />
                <text x="212" y="122" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">⚡ Turbine</text>

                <!-- Downstream Controlled River (Right) -->
                <rect x="235" y="150" width="85" height="50" fill="#0284c7" opacity="0.6" />
                <text x="277" y="180" fill="#bae6fd" font-size="7" font-weight="bold" text-anchor="middle">Downstream Flow</text>

                <!-- Power Grid Transmission Lines -->
                <line x1="212" y1="130" x2="212" y2="60" stroke="#f59e0b" stroke-width="2" />
                <line x1="212" y1="60" x2="270" y2="40" stroke="#f59e0b" stroke-width="2" />
                <polygon points="265,35 275,35 270,55" fill="#eab308" />
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleDamTurbines(true)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ⚡ Spin Turbines (Generate Electricity)
            </button>
            <button onclick="toggleDamTurbines(false)" class="p-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow transition">
                🌊 Open Floodgates (Release Excess Water)
            </button>
        </div>
        <div id="sim8-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Dams act as giant valley barricades that store seasonal rain in reservoirs. Water plunging through penstock pipes spins massive turbines to generate clean electricity without burning fossil fuels.
        </div>
    </div>
    """,

    9: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Dam Trade-Offs & Forest Submergence</span>
            <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Reservoir: Full Submergence Level</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Valley Bed with Ancient Forest & Village Settlements -->
                <polygon points="0,180 80,100 160,140 240,90 320,180 320,200 0,200" fill="#14532d" />
                
                <!-- Trees submerged or exposed -->
                <g id="sim9-forest">
                    <rect x="60" y="115" width="4" height="15" fill="#78350f" />
                    <circle cx="62" cy="110" r="10" fill="#16a34a" />
                    <rect x="180" y="115" width="4" height="15" fill="#78350f" />
                    <circle cx="182" cy="110" r="12" fill="#16a34a" />
                </g>

                <!-- Village Hut -->
                <g id="sim9-village" transform="translate(120, 120)">
                    <rect x="0" y="5" width="22" height="15" fill="#ca8a04" />
                    <polygon points="-3,5 11,-4 25,5" fill="#b91c1c" />
                    <text x="11" y="27" fill="#fde047" font-size="6.5" font-weight="bold" text-anchor="middle">Tribal Village</text>
                </g>

                <!-- Rising Reservoir Water Level -->
                <rect id="sim9-reservoir-water" x="0" y="90" width="320" height="110" fill="#0284c7" opacity="0.65" />
                
                <!-- Submergence Warning Line -->
                <line x1="0" y1="90" x2="320" y2="90" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" />
                <text x="160" y="82" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Full Reservoir Submergence Mark</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setReservoirLevel('high')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🌊 Full Reservoir Level (Submerge Valley)
            </button>
            <button onclick="setReservoirLevel('low')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌲 Natural River Valley (Original Forest)
            </button>
        </div>
        <div id="sim9-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            While reservoirs store water, filling them permanently drowns fertile valleys and ancient forests, severing wildlife migration corridors and displacing indigenous human settlements.
        </div>
    </div>
    """,

    10: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">River Pollution Sources & Water Health</span>
            <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">River Health: Severely Contaminated</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- River Current with Dynamic Color -->
                <rect id="sim10-water" x="0" y="80" width="320" height="85" fill="#451a03" opacity="0.8" />
                <text id="sim10-water-status" x="160" y="125" fill="#fca5a5" font-size="8.5" font-weight="bold" text-anchor="middle">Toxic Effluents & Sewage Discharged</text>

                <!-- City Drainage Pipe (Top Left) -->
                <g transform="translate(50, 45)">
                    <rect x="-15" y="0" width="30" height="35" fill="#475569" stroke="#94a3b8" />
                    <!-- Sludge outflow -->
                    <path d="M -10,35 Q 0,55 10,75" stroke="#78350f" stroke-width="6" fill="none" />
                    <text x="0" y="-5" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">City Sewage</text>
                </g>

                <!-- Factory Pipe (Top Center) -->
                <g transform="translate(160, 45)">
                    <rect x="-15" y="0" width="30" height="35" fill="#334155" stroke="#94a3b8" />
                    <!-- Chemical dye outflow -->
                    <path d="M -10,35 Q 0,55 10,75" stroke="#9333ea" stroke-width="5" fill="none" />
                    <text x="0" y="-5" fill="#c084fc" font-size="7.5" font-weight="bold" text-anchor="middle">Factory Dyes</text>
                </g>

                <!-- Floating Plastic Debris -->
                <g id="sim10-plastic-trash" transform="translate(240, 110)">
                    <rect x="0" y="0" width="14" height="6" rx="2" fill="#f43f5e" />
                    <circle cx="20" cy="5" r="4" fill="#38bdf8" />
                    <text x="10" y="-6" fill="#f87171" font-size="7" font-weight="bold" text-anchor="middle">Plastic Trash</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="cleanseRiver(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌿 Operate Sewage Treatment (Clean River)
            </button>
            <button onclick="cleanseRiver(false)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                ☣️ Dump Untreated Sewage & Chemicals
            </button>
        </div>
        <div id="sim10-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Dumping untreated domestic sewage, non-biodegradable plastics, and industrial chemical effluents turns living rivers into toxic health hazards. Installing Sewage Treatment Plants (STPs) is vital.
        </div>
    </div>
    """,

    11: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Fertilizer Runoff & The Green Blanket</span>
            <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Ecosystem: Eutrophication Bloom</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Water Column in Pond/River -->
                <rect x="0" y="60" width="320" height="140" fill="#0284c7" fill-opacity="0.5" />

                <!-- Green Blanket (Dense Algal Bloom Mat on Surface) -->
                <rect id="sim11-green-mat" x="0" y="55" width="320" height="20" fill="#15803d" stroke="#22c55e" stroke-width="1.5" />
                <text x="160" y="68" fill="#fef08a" font-size="8.5" font-weight="bold" text-anchor="middle">Dense Algal Bloom & Weed Mat</text>

                <!-- Blocked Sunlight Rays -->
                <line x1="80" y1="20" x2="80" y2="55" stroke="#facc15" stroke-width="2" stroke-dasharray="2,2" />
                <line x1="160" y1="20" x2="160" y2="55" stroke="#facc15" stroke-width="2" stroke-dasharray="2,2" />
                <line x1="240" y1="20" x2="240" y2="55" stroke="#facc15" stroke-width="2" stroke-dasharray="2,2" />
                <text x="160" y="35" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Sunlight Blocked by Green Blanket!</text>

                <!-- Fish Suffering from Oxygen Starvation -->
                <g id="sim11-dead-fish" transform="translate(160, 130)">
                    <ellipse cx="0" cy="0" rx="14" ry="7" fill="#94a3b8" />
                    <polygon points="-14,0 -22,-6 -22,6" fill="#64748b" />
                    <!-- Dead eye (X) -->
                    <text x="8" y="2" fill="#ef4444" font-size="8" font-weight="bold">×</text>
                    <text x="0" y="24" fill="#fca5a5" font-size="7.5" font-weight="bold" text-anchor="middle">Dissolved Oxygen Depleted (Suffocation)</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleEutrophication(true)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🌾 Spray Chemical Fertilizer (Trigger Bloom)
            </button>
            <button onclick="toggleEutrophication(false)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌿 Natural Organic Farming (Clean Water)
            </button>
        </div>
        <div id="sim11-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Excess fertilizers washed into rivers feed explosive algal blooms. This green blanket blocks sunlight, and decaying algae consumes all dissolved oxygen, suffocating fish in aquatic dead zones.
        </div>
    </div>
    """,

    12: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Monsoon River Flood Dynamics</span>
            <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Stage: Normal River Flow</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Floodplain Ground (Settlements & Fields on banks) -->
                <rect x="0" y="90" width="70" height="110" fill="#15803d" />
                <rect x="250" y="90" width="70" height="110" fill="#15803d" />
                <!-- Houses on Floodplain -->
                <g transform="translate(25, 68)">
                    <rect x="0" y="7" width="16" height="15" fill="#ca8a04" />
                    <polygon points="-2,7 8,-2 18,7" fill="#b91c1c" />
                </g>
                <g transform="translate(275, 68)">
                    <rect x="0" y="7" width="16" height="15" fill="#ca8a04" />
                    <polygon points="-2,7 8,-2 18,7" fill="#b91c1c" />
                </g>

                <!-- River Channel -->
                <path d="M 70,200 L 70,120 Q 160,110 250,120 L 250,200 Z" fill="#0f172a" stroke="#334155" />
                
                <!-- Dynamic Flood Water -->
                <rect id="sim12-flood-water" x="70" y="130" width="180" height="70" fill="#0284c7" opacity="0.8" />
                <text id="sim12-flood-label" x="160" y="165" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Within Normal Banks</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="triggerFloodStage('normal')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                💧 Normal Seasonal Flow
            </button>
            <button onclick="triggerFloodStage('deluge')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🌊 Heavy Monsoon Cloudburst (Flood Over Bank)
            </button>
        </div>
        <div id="sim12-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            When continuous cloudbursts dump massive rainfall over river catchments, volume overwhelms the channel. The river bursts its banks, inundating houses and crops built on natural floodplains.
        </div>
    </div>
    """,

    13: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Forest Shield vs Deforested Runoff</span>
            <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Catchment: Forest Shield Active</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040714" />

                <!-- Left Slope: Pristine Forest (Absorbs Rain) -->
                <polygon points="10,180 80,40 150,180" fill="#14532d" />
                <g id="sim13-forest-trees">
                    <circle cx="65" cy="80" r="12" fill="#22c55e" />
                    <circle cx="95" cy="70" r="14" fill="#16a34a" />
                    <circle cx="80" cy="115" r="15" fill="#15803d" />
                </g>
                <text x="80" y="32" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Forested Slope</text>
                <text x="80" y="165" fill="#a7f3d0" font-size="7" text-anchor="middle">Spongy Humus Absorbs Rain</text>

                <!-- Right Slope: Deforested Bare Rocks (Flash Runoff) -->
                <polygon points="170,180 240,40 310,180" fill="#78350f" />
                <!-- Mud runoff streaks -->
                <line x1="240" y1="65" x2="280" y2="150" stroke="#ca8a04" stroke-width="4" stroke-dasharray="3,3" />
                <line x1="225" y1="85" x2="200" y2="150" stroke="#ca8a04" stroke-width="4" stroke-dasharray="3,3" />
                <text x="240" y="32" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Deforested Slope</text>
                <text x="240" y="165" fill="#fde047" font-size="7" text-anchor="middle">Rapid Muddy Flash Flood Runoff!</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="compareCatchment('forest')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌲 Forest Shield (Infiltration & Soil Anchor)
            </button>
            <button onclick="compareCatchment('bare')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ⛰️ Deforested Hills (Erosion & Flash Flood)
            </button>
        </div>
        <div id="sim13-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Tree canopies cushion falling rain, spongy humus absorbs moisture, and root systems anchor riverbanks. Clear-cutting forests strips away this sponge, causing violent flash floods and river siltation.
        </div>
    </div>
    """,

    14: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Flood Safety Protocol Station</span>
            <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Protocol: Before the Flood</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Action Card Display -->
                <rect x="25" y="20" width="270" height="155" rx="8" fill="#0f172a" stroke="#334155" />

                <!-- Content Area -->
                <g id="sim14-content" transform="translate(160, 45)">
                    <text id="sim14-step-title" x="0" y="0" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Phase 1: Before the Flood (Preparedness)</text>
                    
                    <g id="sim14-step-icons" transform="translate(0, 30)">
                        <rect x="-80" y="-15" width="30" height="30" rx="4" fill="#1e293b" />
                        <text x="-65" y="5" font-size="14" text-anchor="middle">🎒</text>
                        <rect x="-20" y="-15" width="30" height="30" rx="4" fill="#1e293b" />
                        <text x="-5" y="5" font-size="14" text-anchor="middle">🔦</text>
                        <rect x="40" y="-15" width="30" height="30" rx="4" fill="#1e293b" />
                        <text x="55" y="5" font-size="14" text-anchor="middle">📻</text>
                    </g>
                    
                    <text id="sim14-step-p1" x="0" y="65" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle">Prepare an Emergency Kit with Torch, Batteries & Medicines</text>
                    <text id="sim14-step-p2" x="0" y="80" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Keep battery radio tuned to meteorological storm alerts</text>
                    <text id="sim14-step-p3" x="0" y="95" fill="#94a3b8" font-size="7.5" text-anchor="middle">Move family documents, dry food, and livestock to elevated ground</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="setFloodSafetyPhase('before')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🎒 Before Flood
            </button>
            <button onclick="setFloodSafetyPhase('during')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                🚫 During Flood
            </button>
            <button onclick="setFloodSafetyPhase('after')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                💧 After Flood
            </button>
        </div>
        <div id="sim14-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Never attempt to walk, swim, or drive through moving floodwaters—just 15 cm can sweep an adult away! After floods recede, always boil drinking water to prevent waterborne epidemics.
        </div>
    </div>
    """,

    15: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Chennai 2019 Day Zero: Jaldoot Water Train</span>
            <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Crisis: 4 City Reservoirs Dried Up</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Dried Up Cracked Reservoir Basin (Top Half) -->
                <rect x="20" y="15" width="280" height="70" rx="6" fill="#78350f" />
                <path d="M 40,35 L 70,55 L 110,40 L 150,65 L 200,45 L 250,60" stroke="#ca8a04" stroke-width="2" fill="none" />
                <text x="160" y="35" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Chennai Day Zero: Parched Reservoir Bed</text>

                <!-- Railway Track (Bottom Half) -->
                <line x1="0" y1="140" x2="320" y2="140" stroke="#64748b" stroke-width="3" />
                <line x1="0" y1="150" x2="320" y2="150" stroke="#64748b" stroke-width="3" />
                <!-- Ties -->
                <g stroke="#94a3b8" stroke-width="2">
                    <line x1="30" y1="135" x2="30" y2="155" />
                    <line x1="70" y1="135" x2="70" y2="155" />
                    <line x1="110" y1="135" x2="110" y2="155" />
                    <line x1="150" y1="135" x2="150" y2="155" />
                    <line x1="190" y1="135" x2="190" y2="155" />
                    <line x1="230" y1="135" x2="230" y2="155" />
                    <line x1="270" y1="135" x2="270" y2="155" />
                </g>

                <!-- Jaldoot Water Train Tanker Wagons -->
                <g id="sim15-water-train" transform="translate(60, 115)">
                    <!-- Tanker 1 -->
                    <rect x="0" y="0" width="55" height="25" rx="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="27" y="15" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">WATER</text>
                    <!-- Tanker 2 -->
                    <rect x="65" y="0" width="55" height="25" rx="5" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="92" y="15" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">WATER</text>
                    <!-- Engine -->
                    <rect x="130" y="-5" width="45" height="30" rx="3" fill="#ea580c" />
                    <text x="152" y="15" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">IR</text>
                </g>

                <rect x="25" y="165" width="270" height="26" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim15-train-status" x="160" y="181" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Jaldoot Train Delivering 2.5 Million Liters from Jolarpettai</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="dispatchWaterTrain()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🚂 Dispatch Jaldoot Water Train (200 km)
            </button>
            <button onclick="inspectDayZero()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🏜️ Inspect Dried Up Reservoir Basin
            </button>
        </div>
        <div id="sim15-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In summer 2019, Chennai's reservoirs dried up completely. Indian Railways operated special Jaldoot trains carrying 2.5 million liters of drinking water per trip from Jolarpettai to save the city.
        </div>
    </div>
    """,

    16: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Automated Water ATM & Conservation Meter</span>
            <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Action: Dispensing Clean RO Water</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Water ATM Kiosk Structure (Center) -->
                <rect x="110" y="25" width="100" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
                <rect x="120" y="35" width="80" height="22" rx="4" fill="#0284c7" />
                <text x="160" y="50" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">WATER ATM</text>

                <!-- Digital Display Screen -->
                <rect x="125" y="65" width="70" height="25" rx="3" fill="#022c22" stroke="#10b981" />
                <text id="sim16-atm-screen" x="160" y="81" fill="#34d399" font-size="8.5" font-weight="bold" text-anchor="middle">INSERT COIN / CARD</text>

                <!-- Coin / Card Slot -->
                <rect x="135" y="100" width="20" height="4" fill="#e2e8f0" />
                <circle cx="175" cy="102" r="5" fill="#facc15" />

                <!-- Water Dispensing Tap & Vessel -->
                <rect x="155" y="115" width="10" height="15" fill="#64748b" />
                <!-- Water stream -->
                <line id="sim16-atm-stream" x1="160" y1="130" x2="160" y2="155" stroke="#38bdf8" stroke-width="4" opacity="0" />
                <!-- Reusable Steel Jug (Zero plastic bottle waste) -->
                <rect x="150" y="150" width="20" height="22" rx="3" fill="#94a3b8" stroke="#e2e8f0" />

                <!-- National Water Mission Banner (Bottom) -->
                <text x="160" y="192" fill="#a5f3fc" font-size="7.5" font-weight="bold" text-anchor="middle">"Catch the Rain, Where it Falls, When it Falls"</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="operateWaterATM()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                💳 Insert Card / Coin (Dispense Water)
            </button>
            <button onclick="calculatePledgeSavings()" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚰 Turn Off Tap While Brushing (Save 15 L)
            </button>
        </div>
        <div id="sim16-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Water ATMs dispense pure, affordable RO drinking water into reusable jugs, eliminating plastic bottle pollution. Practicing daily conservation protects our rivers and water security.
        </div>
    </div>
    """
}


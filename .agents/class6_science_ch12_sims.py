"""
Class 6 Science Chapter 12: Beyond Earth
16 Bespoke Interactive SVG/HTML Simulators
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Nubra Valley Caravan Stargazer</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Heading: True North (000°)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <defs>
                    <linearGradient id="sim1-sky" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stop-color="#020617" />
                        <stop offset="60%" stop-color="#0f172a" />
                        <stop offset="100%" stop-color="#1e1b4b" />
                    </linearGradient>
                </defs>
                <rect x="0" y="0" width="320" height="200" fill="url(#sim1-sky)" />
                <!-- Ladakh Mountain Peaks -->
                <polygon points="0,170 45,120 90,165 140,110 210,160 270,105 320,155 320,200 0,200" fill="#0f172a" opacity="0.9" />
                <polygon points="20,175 70,135 120,170 170,125 240,170 300,120 320,150 320,200 0,200" fill="#020617" />
                
                <!-- Stars in Nubra Sky -->
                <g id="sim1-stars" fill="#ffffff">
                    <circle cx="30" cy="30" r="1" opacity="0.8" />
                    <circle cx="80" cy="45" r="1.5" opacity="0.9" />
                    <circle cx="120" cy="25" r="1.2" opacity="0.7" />
                    <circle cx="190" cy="40" r="1.8" opacity="0.95" />
                    <circle cx="230" cy="20" r="1.2" opacity="0.8" />
                    <circle cx="280" cy="50" r="1.5" opacity="0.85" />
                    <circle cx="60" cy="80" r="1.3" opacity="0.75" />
                    <circle cx="150" cy="70" r="1.6" opacity="0.9" />
                    <circle cx="250" cy="85" r="1.4" opacity="0.8" />
                </g>

                <!-- Pole Star (Dhruva Tara) High in North -->
                <g id="sim1-polestar" transform="translate(160, 35)">
                    <circle cx="0" cy="0" r="4" fill="#67e8f9" filter="drop-shadow(0 0 4px #22d3ee)" />
                    <circle cx="0" cy="0" r="1.5" fill="#ffffff" />
                    <line x1="-8" y1="0" x2="8" y2="0" stroke="#67e8f9" stroke-width="0.8" />
                    <line x1="0" y1="-8" x2="0" y2="8" stroke="#67e8f9" stroke-width="0.8" />
                    <text x="8" y="-4" fill="#a5f3fc" font-size="9" font-weight="bold">Dhruva Tārā (North)</text>
                </g>

                <!-- Navigation Guidance Ray -->
                <line id="sim1-nav-line" x1="160" y1="35" x2="160" y2="175" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.8" />

                <!-- Caravan Camel Silhouette and Traveler -->
                <g id="sim1-caravan" transform="translate(140, 165)">
                    <ellipse cx="20" cy="10" rx="14" ry="7" fill="#ca8a04" opacity="0.9" />
                    <circle cx="34" cy="5" r="5" fill="#ca8a04" opacity="0.9" />
                    <line x1="12" y1="16" x2="10" y2="28" stroke="#ca8a04" stroke-width="2.5" />
                    <line x1="26" y1="16" x2="28" y2="28" stroke="#ca8a04" stroke-width="2.5" />
                    <!-- Lantern Glow -->
                    <circle cx="6" cy="12" r="3" fill="#fde047" filter="drop-shadow(0 0 5px #facc15)" />
                </g>

                <!-- Compass Heading Display -->
                <rect x="10" y="10" width="105" height="26" rx="5" fill="#0f172a" fill-opacity="0.85" stroke="#334155" />
                <text id="sim1-heading-text" x="16" y="27" fill="#38bdf8" font-size="10" font-weight="bold">Compass: 000° N</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="navigateCaravan('north')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🧭 March North
            </button>
            <button onclick="navigateCaravan('east')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🌅 Turn East
            </button>
            <button onclick="navigateCaravan('west')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🌄 Turn West
            </button>
        </div>
        <div id="sim1-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Ancient Silk Route caravans traversing Ladakh used the unwavering position of the Pole Star (Dhruva Tārā) as their celestial compass long before magnetic compasses existed.
        </div>
    </div>
    """,

    2: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Constellation Sky Map & IAU Boundaries</span>
            <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Mode: 88 IAU Official Boundaries</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#050814" />
                
                <!-- Celestial Grid Coordinates -->
                <circle cx="160" cy="100" r="90" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="2,2" />
                <circle cx="160" cy="100" r="50" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="2,2" />
                <line x1="70" y1="100" x2="250" y2="100" stroke="#1e293b" stroke-width="1" />
                <line x1="160" y1="10" x2="160" y2="190" stroke="#1e293b" stroke-width="1" />

                <!-- IAU Official Patch Boundaries -->
                <g id="sim2-iau-boundaries" stroke="#6366f1" stroke-width="1" fill="#4338ca" fill-opacity="0.12">
                    <!-- Ursa Major Sector -->
                    <polygon points="50,30 140,25 150,90 40,80" />
                    <!-- Orion Sector -->
                    <polygon points="170,95 270,85 285,175 160,165" />
                    <!-- Cassiopeia Sector -->
                    <polygon points="160,20 260,20 250,75 165,70" />
                </g>

                <!-- Ursa Major Stars & Stick Lines -->
                <g id="sim2-stars">
                    <!-- Saptarshi / Big Dipper Stars -->
                    <circle cx="60" cy="45" r="2.5" fill="#f8fafc" />
                    <circle cx="80" cy="40" r="2.5" fill="#f8fafc" />
                    <circle cx="95" cy="50" r="2.5" fill="#f8fafc" />
                    <circle cx="105" cy="65" r="2.5" fill="#f8fafc" />
                    <circle cx="130" cy="62" r="2.5" fill="#f8fafc" />
                    <circle cx="132" cy="78" r="2.5" fill="#38bdf8" />
                    <circle cx="110" cy="80" r="2.5" fill="#38bdf8" />
                    <!-- Orion Stars -->
                    <circle cx="195" cy="115" r="3.2" fill="#f97316" /> <!-- Betelgeuse -->
                    <circle cx="245" cy="110" r="2.8" fill="#bae6fd" /> <!-- Bellatrix -->
                    <circle cx="210" cy="135" r="2.2" fill="#ffffff" /> <!-- Belt 1 -->
                    <circle cx="220" cy="137" r="2.2" fill="#ffffff" /> <!-- Belt 2 -->
                    <circle cx="230" cy="139" r="2.2" fill="#ffffff" /> <!-- Belt 3 -->
                    <circle cx="205" cy="160" r="2.8" fill="#e2e8f0" /> <!-- Saiph -->
                    <circle cx="248" cy="158" r="3.5" fill="#38bdf8" /> <!-- Rigel -->
                </g>

                <!-- Constellation Stick Connectors -->
                <g id="sim2-lines" stroke="#38bdf8" stroke-width="1.2" opacity="0.8">
                    <polyline points="60,45 80,40 95,50 105,65 130,62 132,78 110,80 105,65" fill="none" />
                    <polygon points="195,115 245,110 248,158 205,160" fill="none" stroke="#f43f5e" stroke-dasharray="2,2" />
                    <line x1="210" y1="135" x2="230" y2="139" stroke="#facc15" stroke-width="2" />
                </g>

                <!-- Labels -->
                <text x="85" y="32" fill="#93c5fd" font-size="9" font-weight="bold">Ursa Major</text>
                <text x="210" y="105" fill="#fca5a5" font-size="9" font-weight="bold">Orion</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="toggleConstellationView('all')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🌐 All 88 Sectors
            </button>
            <button onclick="toggleConstellationView('figures')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                ✨ Stick Figures
            </button>
            <button onclick="toggleConstellationView('stars')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                ⭐ Star Field Only
            </button>
        </div>
        <div id="sim2-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In 1922, the International Astronomical Union (IAU) formally mapped the entire celestial sphere into 88 precise border regions so every star belongs to one unique constellation.
        </div>
    </div>
    """,

    3: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Orion the Hunter & Sirius Pointer</span>
            <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Target: Sirius (Canis Major)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Orion Outline Figure Background -->
                <path d="M 120,40 L 175,35 L 180,115 L 125,120 Z" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="0.8" stroke-dasharray="2,2" />
                
                <!-- Orion Key Stars -->
                <!-- Betelgeuse (Red Supergiant, Ardra) -->
                <g transform="translate(120, 40)">
                    <circle cx="0" cy="0" r="5" fill="#ea580c" filter="drop-shadow(0 0 5px #f97316)" />
                    <text x="-6" y="-8" fill="#fdba74" font-size="8.5" font-weight="bold">Betelgeuse (Ārdrā)</text>
                </g>
                <!-- Bellatrix -->
                <circle cx="175" cy="35" r="3" fill="#bae6fd" />
                <text x="180" y="38" fill="#93c5fd" font-size="8">Bellatrix</text>
                <!-- Rigel (Blue Supergiant) -->
                <g transform="translate(180, 115)">
                    <circle cx="0" cy="0" r="4.5" fill="#38bdf8" filter="drop-shadow(0 0 5px #0284c7)" />
                    <text x="6" y="12" fill="#7dd3fc" font-size="8.5" font-weight="bold">Rigel</text>
                </g>
                <!-- Saiph -->
                <circle cx="125" cy="120" r="2.8" fill="#e2e8f0" />
                <text x="96" y="128" fill="#94a3b8" font-size="8">Saiph</text>

                <!-- Orion's Belt (3 Stars in a straight row) -->
                <circle cx="145" cy="74" r="2.8" fill="#ffffff" />
                <circle cx="152" cy="77" r="2.8" fill="#ffffff" />
                <circle cx="159" cy="80" r="2.8" fill="#ffffff" />
                <rect x="135" y="66" width="35" height="22" rx="4" fill="none" stroke="#facc15" stroke-width="1" stroke-dasharray="2,2" />
                <text x="135" y="62" fill="#fde047" font-size="8" font-weight="bold">Belt Stars</text>

                <!-- Pointer Line down-left to Sirius -->
                <line id="sim3-sirius-ray" x1="145" y1="74" x2="260" y2="120" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" />

                <!-- Sirius in Canis Major (Brightest Star in Night Sky) -->
                <g id="sim3-sirius" transform="translate(260, 120)">
                    <circle cx="0" cy="0" r="6" fill="#ffffff" filter="drop-shadow(0 0 8px #38bdf8)" />
                    <line x1="-10" y1="0" x2="10" y2="0" stroke="#38bdf8" stroke-width="1.2" />
                    <line x1="0" y1="-10" x2="0" y2="10" stroke="#38bdf8" stroke-width="1.2" />
                    <text x="-16" y="18" fill="#67e8f9" font-size="9" font-weight="bold">Sirius (Brightest)</text>
                </g>

                <!-- Pointer Line up-right to Aldebaran in Taurus -->
                <line id="sim3-taurus-ray" x1="159" y1="80" x2="45" y2="35" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6" />
                <g transform="translate(45, 35)">
                    <circle cx="0" cy="0" r="3.8" fill="#f97316" />
                    <text x="-25" y="14" fill="#fbbf24" font-size="8">Aldebaran (Rohiṇī)</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="highlightTarget('sirius')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌟 Trace Belt ➔ Sirius (Canis Major)
            </button>
            <button onclick="highlightTarget('taurus')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🐂 Trace Belt ➔ Aldebaran (Taurus)
            </button>
        </div>
        <div id="sim3-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Drawing an imaginary line through the three prominent stars of Orion's Belt down towards the south-east points directly to Sirius, the brightest star in the entire night sky.
        </div>
    </div>
    """,

    4: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Pole Star Compass & Pointer Stars</span>
            <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Ratio: 5x Distance Rule</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Earth Curvature at Bottom -->
                <path d="M 0,195 Q 160,180 320,195 L 320,200 L 0,200 Z" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
                <text x="160" y="196" fill="#64748b" font-size="8" text-anchor="middle">Northern Horizon</text>

                <!-- Ursa Major (Saptarshi / Big Dipper) -->
                <!-- Handle Stars: Kratu, Pulaha, Pulastya, Atri, Angiras, Vasishtha, Marichi -->
                <g id="sim4-dipper" stroke="#38bdf8" stroke-width="1.2">
                    <line x1="30" y1="125" x2="55" y2="128" />
                    <line x1="55" y1="128" x2="80" y2="138" />
                    <line x1="80" y1="138" x2="105" y2="148" />
                    <line x1="105" y1="148" x2="135" y2="145" />
                    <line x1="135" y1="145" x2="140" y2="170" />
                    <line x1="140" y1="170" x2="110" y2="173" />
                    <line x1="110" y1="173" x2="105" y2="148" />

                    <!-- Dipper Stars -->
                    <circle cx="30" cy="125" r="2.2" fill="#ffffff" />
                    <circle cx="55" cy="128" r="2.2" fill="#ffffff" />
                    <circle cx="80" cy="138" r="2.2" fill="#ffffff" />
                    <circle cx="105" cy="148" r="2.2" fill="#ffffff" />
                    <circle cx="135" cy="145" r="2.2" fill="#ffffff" />
                    <circle cx="140" cy="170" r="3.2" fill="#facc15" /> <!-- Merak / Pulaha -->
                    <circle cx="135" cy="145" r="3.2" fill="#facc15" /> <!-- Dubhe / Kratu -->
                </g>

                <!-- Pointer Gap Indicator -->
                <line x1="140" y1="170" x2="135" y2="145" stroke="#f43f5e" stroke-width="2.5" />
                <text x="146" y="160" fill="#f87171" font-size="8" font-weight="bold">Gap (d)</text>

                <!-- 5x Extrapolated Pointer Line -->
                <line id="sim4-ray" x1="140" y1="170" x2="120" y2="35" stroke="#22d3ee" stroke-width="2" stroke-dasharray="3,3" />

                <!-- Five Incremental Markers along the line -->
                <circle cx="135" cy="145" r="1.5" fill="#22d3ee" />
                <circle cx="131" cy="118" r="1.5" fill="#22d3ee" />
                <circle cx="127" cy="90" r="1.5" fill="#22d3ee" />
                <circle cx="124" cy="63" r="1.5" fill="#22d3ee" />
                <circle cx="120" cy="35" r="2" fill="#22d3ee" />

                <!-- Pole Star (Polaris / Dhruva Tara) -->
                <g id="sim4-polaris" transform="translate(120, 35)">
                    <circle cx="0" cy="0" r="5" fill="#38bdf8" filter="drop-shadow(0 0 6px #06b6d4)" />
                    <circle cx="0" cy="0" r="2" fill="#ffffff" />
                    <line x1="-8" y1="0" x2="8" y2="0" stroke="#67e8f9" stroke-width="1" />
                    <line x1="0" y1="-8" x2="0" y2="8" stroke="#67e8f9" stroke-width="1" />
                    <text x="10" y="4" fill="#a5f3fc" font-size="9" font-weight="bold">Dhruva Tārā (North Pole Star)</text>
                </g>
                <text x="120" y="20" fill="#94a3b8" font-size="8" text-anchor="middle">Distance ≈ 5 × Gap</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="measurePoleStar('extend')" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                📏 Measure 5× Pointer Gap
            </button>
            <button onclick="measurePoleStar('rotate')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-cyan-300 border border-slate-700 shadow transition">
                🔄 Rotate Sky Around Polaris
            </button>
        </div>
        <div id="sim4-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Locate the two end stars of the Big Dipper bowl (Merak and Dubhe). Extend an imaginary line through them upward by 5 times their distance to reach the stationary Pole Star.
        </div>
    </div>
    """,

    5: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Urban Light Pollution vs Hanle Dark Sky</span>
            <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Skyglow: Urban (Bortle 8)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Sky Background with Dynamic Skyglow Filter -->
                <rect id="sim5-sky" x="0" y="0" width="320" height="150" fill="#334155" />
                
                <!-- Milky Way Ribbon (Hidden in city, revealed in dark sky) -->
                <path id="sim5-milkyway" d="M 0,20 Q 100,60 200,30 T 320,80 L 320,130 Q 200,90 100,120 T 0,90 Z" fill="#e0e7ff" opacity="0.05" />

                <!-- Star Field (Dim stars hidden in city) -->
                <g id="sim5-stars">
                    <!-- Bright stars always visible -->
                    <circle cx="80" cy="40" r="2.5" fill="#ffffff" />
                    <circle cx="230" cy="30" r="2.8" fill="#ffffff" />
                    <circle cx="160" cy="60" r="2.2" fill="#ffffff" />
                </g>
                <!-- Faint Stars (Controlled by opacity) -->
                <g id="sim5-faint-stars" opacity="0.1" fill="#cbd5e1">
                    <circle cx="40" cy="20" r="1" />
                    <circle cx="110" cy="25" r="1.2" />
                    <circle cx="140" cy="35" r="0.8" />
                    <circle cx="190" cy="20" r="1.3" />
                    <circle cx="270" cy="55" r="1.1" />
                    <circle cx="290" cy="25" r="1" />
                    <circle cx="65" cy="80" r="0.9" />
                    <circle cx="125" cy="95" r="1.2" />
                    <circle cx="210" cy="80" r="1.4" />
                    <circle cx="250" cy="90" r="0.8" />
                </g>

                <!-- Cityscape vs Hanle Observatory Silhouette -->
                <g id="sim5-ground">
                    <!-- City Buildings -->
                    <rect id="sim5-bldg1" x="30" y="120" width="25" height="35" fill="#1e293b" />
                    <rect id="sim5-bldg2" x="60" y="105" width="30" height="50" fill="#0f172a" />
                    <rect id="sim5-bldg3" x="95" y="130" width="20" height="25" fill="#1e293b" />
                    <rect id="sim5-bldg4" x="220" y="115" width="28" height="40" fill="#0f172a" />
                    <!-- Streetlamp with glaring light cone -->
                    <g id="sim5-lamp" transform="translate(160, 125)">
                        <line x1="0" y1="0" x2="0" y2="30" stroke="#94a3b8" stroke-width="2" />
                        <path d="M -15,30 L 15,30 L 2,0 L -2,0 Z" fill="#fef08a" opacity="0.6" />
                        <circle cx="0" cy="0" r="4" fill="#facc15" />
                    </g>
                    <!-- Hanle Telescope Dome (Initially Hidden) -->
                    <g id="sim5-hanle" transform="translate(250, 120)" opacity="0">
                        <path d="M 0,30 L 0,15 A 15,15 0 0 1 30,15 L 30,30 Z" fill="#f8fafc" stroke="#475569" stroke-width="1.5" />
                        <rect x="12" y="5" width="6" height="25" fill="#0284c7" />
                        <text x="15" y="-4" fill="#38bdf8" font-size="7.5" font-weight="bold" text-anchor="middle">Hanle 4,500m</text>
                    </g>
                </g>
                <rect x="0" y="155" width="320" height="45" fill="#020617" />
                <text id="sim5-visibility-text" x="160" y="180" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">Visible Stars: ~20 to 50</text>
            </svg>
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-[11px] text-slate-400">
                <span>🏙️ High Pollution (City)</span>
                <span>🏞️ Hanle Dark Sky Reserve (Ladakh)</span>
            </div>
            <input type="range" id="sim5-slider" min="1" max="100" value="15" oninput="updateLightPollution(this.value)" class="w-full accent-indigo-500 bg-slate-800 rounded-lg cursor-pointer">
        </div>
        <div id="sim5-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Excess artificial outdoor lighting creates skyglow that drowns out faint stars. Hanle in Ladakh was designated India's first Dark Sky Reserve due to its pristine, cloudless, low-humidity air.
        </div>
    </div>
    """,

    6: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Stargazing Field Tool & Night Vision Mode</span>
            <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Light: Red Cellophane (Preserves Vision)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Night Sky Window -->
                <rect id="sim6-sky-bg" x="0" y="0" width="320" height="200" fill="#030712" />
                
                <!-- Star Field -->
                <g id="sim6-starfield" fill="#ffffff">
                    <circle cx="50" cy="50" r="1.5" />
                    <circle cx="100" cy="30" r="2.2" />
                    <circle cx="170" cy="70" r="1.8" />
                    <circle cx="240" cy="40" r="2.5" />
                    <circle cx="280" cy="90" r="1.2" />
                    <circle cx="80" cy="120" r="2" />
                    <circle cx="190" cy="140" r="1.6" />
                </g>

                <!-- Stargazer's Chart Paper -->
                <rect x="70" y="30" width="180" height="130" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
                <text x="160" y="55" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">Sky Map & Star Chart</text>
                
                <!-- Constellation Chart Drawing on Paper -->
                <polyline points="100,110 130,85 160,115 190,85 220,110" fill="none" stroke="#64748b" stroke-width="1.2" />
                <circle cx="100" cy="110" r="2.5" fill="#94a3b8" />
                <circle cx="130" cy="85" r="2.5" fill="#94a3b8" />
                <circle cx="160" cy="115" r="2.5" fill="#94a3b8" />
                <circle cx="190" cy="85" r="2.5" fill="#94a3b8" />
                <circle cx="220" cy="110" r="2.5" fill="#94a3b8" />
                <text x="160" y="140" fill="#64748b" font-size="8.5" text-anchor="middle">Cassiopeia ("W" Shape)</text>

                <!-- Torch Flashlight Beam Overlay -->
                <polygon id="sim6-beam" points="20,180 80,40 240,40 280,180" fill="#ef4444" fill-opacity="0.25" />
                <!-- Torch Body -->
                <g transform="translate(145, 175)">
                    <rect x="0" y="0" width="30" height="15" rx="3" fill="#475569" />
                    <rect x="5" y="-4" width="20" height="4" fill="#94a3b8" />
                    <circle id="sim6-filter" cx="15" cy="-2" r="5" fill="#ef4444" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setTorchMode('red')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🔴 Red Flashlight (Protects Rod Cells)
            </button>
            <button onclick="setTorchMode('white')" class="p-2 rounded-xl bg-slate-200 hover:bg-white text-xs font-bold text-slate-900 shadow transition">
                ⚪ White Light (Blinds Night Vision)
            </button>
        </div>
        <div id="sim6-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Human eyes take 20 to 30 minutes to adapt to darkness. Astronomers cover torches with red cellophane paper because red wavelength light does not break down rhodopsin pigment in eye rod cells.
        </div>
    </div>
    """,

    7: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Solar Powerhouse & 1 AU Photon Transit</span>
            <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Distance: 1 AU (149.6 Million km)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- The Sun (Center-Left) -->
                <g id="sim7-sun" transform="translate(50, 100)">
                    <!-- Corona Rays -->
                    <circle cx="0" cy="0" r="38" fill="#f59e0b" opacity="0.2" filter="blur(4px)" />
                    <circle cx="0" cy="0" r="30" fill="#fbbf24" opacity="0.4" />
                    <!-- Core -->
                    <circle cx="0" cy="0" r="22" fill="#fef08a" stroke="#f59e0b" stroke-width="2" />
                    <text x="0" y="3" fill="#78350f" font-size="8.5" font-weight="bold" text-anchor="middle">Sun Core</text>
                    <text x="0" y="12" fill="#92400e" font-size="6.5" text-anchor="middle">15,000,000 K</text>
                </g>

                <!-- Earth Orbit Path -->
                <path d="M 270,30 A 230,160 0 0 1 270,170" fill="none" stroke="#334155" stroke-width="1.2" stroke-dasharray="3,3" />

                <!-- Earth (Right) -->
                <g id="sim7-earth" transform="translate(265, 100)">
                    <circle cx="0" cy="0" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                    <!-- Green Continents -->
                    <circle cx="-2" cy="-2" r="3" fill="#22c55e" />
                    <circle cx="3" cy="2" r="2.5" fill="#16a34a" />
                    <text x="0" y="19" fill="#93c5fd" font-size="8.5" font-weight="bold" text-anchor="middle">Earth</text>
                </g>

                <!-- Photon Packet Moving along Light Path -->
                <line x1="75" y1="100" x2="255" y2="100" stroke="#fef08a" stroke-width="1" stroke-dasharray="2,2" opacity="0.4" />
                <circle id="sim7-photon" cx="75" cy="100" r="4" fill="#ffffff" filter="drop-shadow(0 0 5px #fde047)" />

                <!-- Distance Banner -->
                <rect x="90" y="25" width="140" height="26" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim7-timer-text" x="160" y="42" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Travel Time: 8 min 20 sec</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="firePhotonAnimation()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ⚡ Transmit Photon to Earth (1 AU)
            </button>
            <button onclick="compareProxima()" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🌌 Compare Proxima Centauri (4.24 yr)
            </button>
        </div>
        <div id="sim7-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Light travels at 300,000 km per second, yet takes 8 minutes and 20 seconds to traverse 1 AU (149.6 million km) from the Sun to Earth. By contrast, light from Proxima Centauri takes 4.24 years!
        </div>
    </div>
    """,

    8: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">The Four Inner Rocky Terrestrial Planets</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Planet: Earth (Blue Oasis)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#050816" />

                <!-- 4 Terrestrial Planets aligned with scale indicators -->
                <!-- Mercury -->
                <g onclick="selectRockyPlanet('mercury')" class="cursor-pointer" transform="translate(45, 90)">
                    <circle id="sim8-p-mercury" cx="0" cy="0" r="10" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5" />
                    <!-- Crater marks -->
                    <circle cx="-3" cy="-2" r="2" fill="#64748b" />
                    <circle cx="2" cy="3" r="1.5" fill="#64748b" />
                    <text x="0" y="24" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Mercury</text>
                    <text x="0" y="34" fill="#64748b" font-size="7" text-anchor="middle">0.39 AU</text>
                </g>

                <!-- Venus -->
                <g onclick="selectRockyPlanet('venus')" class="cursor-pointer" transform="translate(115, 90)">
                    <circle id="sim8-p-venus" cx="0" cy="0" r="18" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5" />
                    <!-- Dense CO2 clouds -->
                    <path d="M -12,-5 Q 0,-10 12,-4" stroke="#d97706" stroke-width="2" fill="none" />
                    <path d="M -14,4 Q 0,8 14,3" stroke="#d97706" stroke-width="2" fill="none" />
                    <text x="0" y="30" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle">Venus</text>
                    <text x="0" y="40" fill="#64748b" font-size="7" text-anchor="middle">0.72 AU</text>
                </g>

                <!-- Earth -->
                <g onclick="selectRockyPlanet('earth')" class="cursor-pointer" transform="translate(195, 90)">
                    <circle id="sim8-p-earth" cx="0" cy="0" r="19" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5" />
                    <circle cx="-4" cy="-4" r="5" fill="#22c55e" />
                    <circle cx="5" cy="4" r="6" fill="#16a34a" />
                    <text x="0" y="32" fill="#93c5fd" font-size="8.5" font-weight="bold" text-anchor="middle">Earth</text>
                    <text x="0" y="42" fill="#38bdf8" font-size="7" text-anchor="middle">1.00 AU</text>
                </g>

                <!-- Mars -->
                <g onclick="selectRockyPlanet('mars')" class="cursor-pointer" transform="translate(270, 90)">
                    <circle id="sim8-p-mars" cx="0" cy="0" r="12" fill="#dc2626" stroke="#f87171" stroke-width="1.5" />
                    <!-- Polar Ice Cap & Olympus Mons -->
                    <ellipse cx="0" cy="-10" rx="4" ry="2" fill="#ffffff" />
                    <circle cx="2" cy="1" r="2.5" fill="#991b1b" />
                    <text x="0" y="26" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Mars</text>
                    <text x="0" y="36" fill="#64748b" font-size="7" text-anchor="middle">1.52 AU</text>
                </g>

                <!-- Comparative Data Banner -->
                <rect x="20" y="145" width="280" height="42" rx="6" fill="#0f172a" stroke="#334155" />
                <text id="sim8-data-line1" x="160" y="162" fill="#e2e8f0" font-size="9" font-weight="bold" text-anchor="middle">Earth: Surface Temp 15°C | Nitrogen-Oxygen Life Blanket</text>
                <text id="sim8-data-line2" x="160" y="177" fill="#94a3b8" font-size="8" text-anchor="middle">Liquid water oceans cover 71% of surface; single natural moon.</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="selectRockyPlanet('mercury')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🌑 Mercury
            </button>
            <button onclick="selectRockyPlanet('venus')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🔥 Venus
            </button>
            <button onclick="selectRockyPlanet('earth')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                🌍 Earth
            </button>
            <button onclick="selectRockyPlanet('mars')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                🔴 Mars
            </button>
        </div>
        <div id="sim8-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click any inner planet to explore its physical diameter, atmospheric greenhouse conditions, surface geology, and orbital characteristics.
        </div>
    </div>
    """,

    9: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Outer Giants: Gas & Ice Worlds</span>
            <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Jupiter: Great Red Spot</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Jupiter (Largest Planet) -->
                <g onclick="selectGiant('jupiter')" class="cursor-pointer" transform="translate(55, 95)">
                    <circle cx="0" cy="0" r="32" fill="#d97706" />
                    <!-- Cloud bands -->
                    <ellipse cx="0" cy="-12" rx="30" ry="4" fill="#b45309" />
                    <ellipse cx="0" cy="0" rx="31" ry="5" fill="#fef3c7" opacity="0.6" />
                    <ellipse cx="0" cy="14" rx="28" ry="4" fill="#92400e" />
                    <!-- Great Red Spot Storm -->
                    <ellipse cx="14" cy="8" rx="7" ry="4.5" fill="#dc2626" />
                    <text x="0" y="45" fill="#fde68a" font-size="8.5" font-weight="bold" text-anchor="middle">Jupiter</text>
                </g>

                <!-- Saturn (Ringed Jewel) -->
                <g onclick="selectGiant('saturn')" class="cursor-pointer" transform="translate(150, 95)">
                    <!-- Saturn Rings Behind -->
                    <ellipse cx="0" cy="0" rx="42" ry="12" fill="none" stroke="#fde047" stroke-width="4" opacity="0.8" />
                    <ellipse cx="0" cy="0" rx="46" ry="14" fill="none" stroke="#ca8a04" stroke-width="2" opacity="0.5" />
                    <!-- Ball -->
                    <circle cx="0" cy="0" r="23" fill="#eab308" />
                    <!-- Rings in front -->
                    <path d="M -42,0 A 42,12 0 0 0 42,0" stroke="#fde047" stroke-width="4" fill="none" />
                    <text x="0" y="45" fill="#fef08a" font-size="8.5" font-weight="bold" text-anchor="middle">Saturn</text>
                </g>

                <!-- Uranus (Tilted Ice Giant) -->
                <g onclick="selectGiant('uranus')" class="cursor-pointer" transform="translate(235, 95)">
                    <!-- Uranus Vertical Ring -->
                    <ellipse cx="0" cy="0" rx="6" ry="24" fill="none" stroke="#67e8f9" stroke-width="1.5" opacity="0.7" />
                    <circle cx="0" cy="0" r="14" fill="#06b6d4" />
                    <text x="0" y="45" fill="#a5f3fc" font-size="8.5" font-weight="bold" text-anchor="middle">Uranus</text>
                </g>

                <!-- Neptune (Windswept Deep Blue) -->
                <g onclick="selectGiant('neptune')" class="cursor-pointer" transform="translate(290, 95)">
                    <circle cx="0" cy="0" r="13" fill="#1d4ed8" stroke="#3b82f6" stroke-width="1.5" />
                    <!-- White cirrus clouds -->
                    <path d="M -7,-2 Q 0,-4 7,-1" stroke="#93c5fd" stroke-width="1.5" fill="none" />
                    <text x="0" y="45" fill="#93c5fd" font-size="8.5" font-weight="bold" text-anchor="middle">Neptune</text>
                </g>

                <!-- Data Banner -->
                <rect x="20" y="150" width="280" height="42" rx="6" fill="#0f172a" stroke="#334155" />
                <text id="sim9-data-title" x="160" y="167" fill="#cbd5e1" font-size="9" font-weight="bold" text-anchor="middle">Jupiter: Gas Giant of Hydrogen & Helium</text>
                <text id="sim9-data-detail" x="160" y="181" fill="#94a3b8" font-size="8" text-anchor="middle">Mass greater than all other 7 planets combined; Great Red Spot anticyclone raging 300+ yrs.</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="selectGiant('jupiter')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🌀 Jupiter
            </button>
            <button onclick="selectGiant('saturn')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-yellow-300 border border-slate-700">
                🪐 Saturn
            </button>
            <button onclick="selectGiant('uranus')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                ❄️ Uranus
            </button>
            <button onclick="selectGiant('neptune')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-blue-300 border border-slate-700">
                💨 Neptune
            </button>
        </div>
        <div id="sim9-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Outer planets lack solid surfaces. Jupiter and Saturn are gas giants made of hydrogen and helium, while Uranus and Neptune are ice giants containing frozen water, ammonia, and methane.
        </div>
    </div>
    """,

    10: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">2006 IAU Planetary Criteria Checker</span>
            <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Classification: Dwarf Planet (Pluto)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Left Column: Planet Graphic -->
                <g id="sim10-planet-art" transform="translate(60, 90)">
                    <circle id="sim10-target-body" cx="0" cy="0" r="30" fill="#a8a29e" stroke="#e7e5e4" stroke-width="2" />
                    <!-- Nitrogen Ice Plains -->
                    <path id="sim10-heart" d="M -10,0 C -15,-10 0,-15 0,0 C 0,-15 15,-10 10,0 C 5,10 0,15 0,15 C 0,15 -5,10 -10,0 Z" fill="#f5f5f4" opacity="0.8" />
                    <text id="sim10-name-label" x="0" y="46" fill="#f5f5f4" font-size="10" font-weight="bold" text-anchor="middle">Pluto</text>
                </g>

                <!-- Right Column: 3 IAU Conditions -->
                <g transform="translate(140, 25)">
                    <!-- Criterion 1: Orbits the Sun -->
                    <rect x="0" y="0" width="165" height="38" rx="5" fill="#0f172a" stroke="#334155" />
                    <circle id="sim10-chk1" cx="18" cy="19" r="8" fill="#10b981" />
                    <text id="sim10-chk1-icon" x="18" y="22" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">✓</text>
                    <text x="32" y="16" fill="#cbd5e1" font-size="8" font-weight="bold">1. Orbits the Sun</text>
                    <text x="32" y="28" fill="#94a3b8" font-size="7">Direct heliocentic orbit</text>

                    <!-- Criterion 2: Hydrostatic Shape -->
                    <rect x="0" y="44" width="165" height="38" rx="5" fill="#0f172a" stroke="#334155" />
                    <circle id="sim10-chk2" cx="18" cy="63" r="8" fill="#10b981" />
                    <text id="sim10-chk2-icon" x="18" y="66" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">✓</text>
                    <text x="32" y="60" fill="#cbd5e1" font-size="8" font-weight="bold">2. Round Spherical Shape</text>
                    <text x="32" y="72" fill="#94a3b8" font-size="7">Self-gravity overcomes rigid forces</text>

                    <!-- Criterion 3: Cleared Neighborhood -->
                    <rect x="0" y="88" width="165" height="38" rx="5" fill="#0f172a" stroke="#334155" />
                    <circle id="sim10-chk3" cx="18" cy="107" r="8" fill="#ef4444" />
                    <text id="sim10-chk3-icon" x="18" y="110" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">✗</text>
                    <text x="32" y="104" fill="#fca5a5" font-size="8" font-weight="bold">3. Cleared Neighborhood</text>
                    <text id="sim10-c3-sub" x="32" y="116" fill="#f87171" font-size="7">Shares orbit with Kuiper belt</text>
                </g>

                <rect x="20" y="155" width="280" height="35" rx="6" fill="#1e1b4b" stroke="#4338ca" />
                <text id="sim10-verdict" x="160" y="177" fill="#a5b4fc" font-size="9.5" font-weight="bold" text-anchor="middle">Pluto meets 2 of 3 criteria ➔ Classified as Dwarf Planet</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="testIAUObject('earth')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌍 Test Earth (Major Planet)
            </button>
            <button onclick="testIAUObject('pluto')" class="p-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white shadow transition">
                🪐 Test Pluto (Dwarf Planet)
            </button>
        </div>
        <div id="sim10-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In 2006, the IAU defined a true planet as an object that orbits the Sun, has sufficient mass for a nearly round shape, and has gravitationally cleared its orbital neighborhood of debris.
        </div>
    </div>
    """,

    11: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Point Star vs Extended Planet Disk</span>
            <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Target: Distant Star (Point Source)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Atmosphere Boundary Band -->
                <rect x="120" y="0" width="80" height="200" fill="#0284c7" fill-opacity="0.1" stroke="#0369a1" stroke-dasharray="2,2" />
                <text x="160" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Turbulent Air Layers</text>

                <!-- Source Object (Left) -->
                <g id="sim11-source" transform="translate(40, 100)">
                    <circle id="sim11-src-dot" cx="0" cy="0" r="3" fill="#ffffff" filter="drop-shadow(0 0 4px #facc15)" />
                    <text id="sim11-src-name" x="0" y="22" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Single Point Source</text>
                    <text x="0" y="32" fill="#64748b" font-size="7" text-anchor="middle">Trillions of km away</text>
                </g>

                <!-- Light Rays passing through air turbulence -->
                <g id="sim11-rays">
                    <path id="sim11-beam-path" d="M 40,100 L 120,95 Q 160,115 200,90 L 270,100" stroke="#fef08a" stroke-width="1.8" fill="none" />
                </g>

                <!-- Observer Eye (Right) -->
                <g transform="translate(270, 100)">
                    <path d="M 0,-15 Q 20,0 0,15 Q -20,0 0,-15 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5" />
                    <circle cx="0" cy="0" r="7" fill="#0284c7" />
                    <circle cx="0" cy="0" r="3.5" fill="#020617" />
                    <text x="0" y="28" fill="#94a3b8" font-size="8" text-anchor="middle">Eye Retina</text>
                </g>

                <!-- Signal Intensity Wave Graph -->
                <rect x="15" y="150" width="290" height="42" rx="6" fill="#0f172a" stroke="#334155" />
                <path id="sim11-signal" d="M 30,175 Q 45,155 60,180 T 90,160 T 120,182 T 150,158 T 180,180 T 210,160 T 240,180 T 270,165" stroke="#f59e0b" stroke-width="2" fill="none" />
                <text id="sim11-status-text" x="160" y="162" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="middle">Light Rapidly Deviates ➔ Perceived as Twinkling</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="inspectLightSource('star')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ✨ Distant Star (Point Source Twinkles)
            </button>
            <button onclick="inspectLightSource('planet')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🪐 Nearby Planet (Disk Averages Steady)
            </button>
        </div>
        <div id="sim11-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Stars are so distant they act as single pinpoint light sources easily refracted by atmospheric air pockets. Planets are close enough to act as extended disks of millions of points whose fluctuations cancel out.
        </div>
    </div>
    """,

    12: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Lunar Synchronous Orbit & Impact Craters</span>
            <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Period: 27.3 Days (Tidally Locked)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Earth Center -->
                <circle cx="160" cy="100" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <circle cx="156" cy="96" r="6" fill="#22c55e" />
                <text x="160" y="103" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Earth</text>

                <!-- Moon Orbit Track -->
                <ellipse cx="160" cy="100" rx="100" ry="60" fill="none" stroke="#334155" stroke-width="1.2" stroke-dasharray="3,3" />

                <!-- Moon Body at Position with Near Side Marker -->
                <g id="sim12-moon-node" transform="translate(260, 100)">
                    <circle cx="0" cy="0" r="14" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5" />
                    <!-- Impact Craters (Preserved forever without atmosphere) -->
                    <circle cx="-3" cy="-3" r="3" fill="#64748b" />
                    <circle cx="4" cy="4" r="2.5" fill="#475569" />
                    <circle cx="-5" cy="5" r="2" fill="#64748b" />
                    <!-- Near-Side Flag / Indicator always pointing toward Earth -->
                    <line id="sim12-face-arrow" x1="0" y1="0" x2="-14" y2="0" stroke="#f43f5e" stroke-width="2.5" />
                    <text x="0" y="24" fill="#e2e8f0" font-size="8" font-weight="bold" text-anchor="middle">Moon</text>
                </g>

                <!-- Crater Preservation Explanation Banner -->
                <rect x="25" y="150" width="270" height="42" rx="6" fill="#0f172a" stroke="#334155" />
                <text id="sim12-crater-title" x="160" y="166" fill="#cbd5e1" font-size="9" font-weight="bold" text-anchor="middle">No Air or Water Erosion = Pristine Craters</text>
                <text id="sim12-crater-sub" x="160" y="180" fill="#94a3b8" font-size="8" text-anchor="middle">Rotational period equals orbital period (~27.3 d): same face always faces Earth.</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="simulateOrbitStep()" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🔄 Orbit Step (Demonstrate Tidal Lock)
            </button>
            <button onclick="impactMeteorite()" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                ☄️ Meteorite Impact (Create Crater)
            </button>
        </div>
        <div id="sim12-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Because the Moon rotates on its axis at the exact same rate it orbits Earth (27.3 days), we always see the exact same hemisphere (near side). Without wind or rain, craters endure billions of years.
        </div>
    </div>
    """,

    13: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Chandrayaan-3 South Pole Touchdown</span>
            <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">August 23, 2023: Shiv Shakti Point</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Lunar South Pole Rough Terrain -->
                <path d="M 0,165 Q 40,150 90,162 T 180,155 T 260,168 T 320,158 L 320,200 L 0,200 Z" fill="#475569" />
                <path d="M 20,175 Q 80,165 140,172 T 240,168 T 320,175 L 320,200 L 0,200 Z" fill="#334155" />

                <!-- Vikram Lander on Lunar Surface -->
                <g id="sim13-vikram" transform="translate(100, 115)">
                    <!-- Thruster Blast Glow -->
                    <polygon id="sim13-flame" points="10,40 20,40 15,50" fill="#f59e0b" opacity="0" />
                    <!-- Lander Body -->
                    <rect x="0" y="10" width="30" height="25" rx="3" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5" />
                    <rect x="5" y="0" width="20" height="10" fill="#cbd5e1" />
                    <!-- Solar Panels -->
                    <rect x="-8" y="12" width="8" height="20" fill="#0284c7" stroke="#38bdf8" stroke-width="0.8" />
                    <rect x="30" y="12" width="8" height="20" fill="#0284c7" stroke="#38bdf8" stroke-width="0.8" />
                    <!-- Landing Legs -->
                    <line x1="2" y1="35" x2="-6" y2="48" stroke="#64748b" stroke-width="2.5" />
                    <line x1="28" y1="35" x2="36" y2="48" stroke="#64748b" stroke-width="2.5" />
                    <!-- Tricolor on Lander -->
                    <rect x="8" y="16" width="14" height="3" fill="#f97316" />
                    <rect x="8" y="19" width="14" height="3" fill="#ffffff" />
                    <rect x="8" y="22" width="14" height="3" fill="#16a34a" />
                    <text x="15" y="8" fill="#e2e8f0" font-size="7.5" font-weight="bold" text-anchor="middle">Vikram</text>
                </g>

                <!-- Ramp and Pragyan Rover -->
                <line id="sim13-ramp" x1="130" y1="150" x2="160" y2="165" stroke="#94a3b8" stroke-width="2" />
                <g id="sim13-pragyan" transform="translate(170, 150)">
                    <rect x="0" y="0" width="22" height="11" rx="2" fill="#ca8a04" stroke="#facc15" stroke-width="1" />
                    <!-- Solar Mast -->
                    <line x1="4" y1="0" x2="4" y2="-6" stroke="#94a3b8" stroke-width="1.5" />
                    <rect x="2" y="-10" width="12" height="4" fill="#0284c7" />
                    <!-- 6 Wheels -->
                    <circle cx="3" cy="13" r="2.5" fill="#1e293b" />
                    <circle cx="11" cy="13" r="2.5" fill="#1e293b" />
                    <circle cx="19" cy="13" r="2.5" fill="#1e293b" />
                    <!-- Ashoka Chakra imprint behind rover -->
                    <circle id="sim13-imprint" cx="-8" cy="13" r="2" fill="none" stroke="#38bdf8" stroke-width="0.8" opacity="0.8" />
                    <text x="11" y="22" fill="#fde047" font-size="7.5" font-weight="bold" text-anchor="middle">Pragyan</text>
                </g>

                <!-- National Space Day Plaque -->
                <rect x="200" y="25" width="105" height="40" rx="5" fill="#0f172a" stroke="#334155" />
                <text x="252" y="42" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">National Space Day</text>
                <text x="252" y="55" fill="#38bdf8" font-size="7.5" text-anchor="middle">23 August (India's Triumph)</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="drivePragyanRover()" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚜 Deploy & Drive Pragyan Rover
            </button>
            <button onclick="scanWaterIce()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                💧 Scan Lunar South Pole Water Ice
            </button>
        </div>
        <div id="sim13-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            India became the first nation in history to land near the lunar south pole when Chandrayaan-3 touched down at Shiv Shakti Point on August 23, 2023, celebrated annually as National Space Day.
        </div>
    </div>
    """,

    14: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Asteroid Belt & Gravitational Dynamics</span>
            <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Zone: Between Mars & Jupiter</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- The Sun (Center) -->
                <circle cx="160" cy="100" r="14" fill="#fbbf24" stroke="#f59e0b" stroke-width="2" />
                <text x="160" y="103" fill="#78350f" font-size="7" font-weight="bold" text-anchor="middle">Sun</text>

                <!-- Mars Orbit (Inner) -->
                <ellipse cx="160" cy="100" rx="45" ry="30" fill="none" stroke="#ef4444" stroke-width="1" stroke-dasharray="2,2" />
                <circle cx="205" cy="100" r="4" fill="#ef4444" />
                <text x="205" y="112" fill="#fca5a5" font-size="6.5" text-anchor="middle">Mars</text>

                <!-- Asteroid Belt Swarm Ring (Between 2.2 and 3.2 AU) -->
                <ellipse cx="160" cy="100" rx="80" ry="50" fill="none" stroke="#ca8a04" stroke-width="12" stroke-opacity="0.15" />
                <g id="sim14-debris" fill="#d97706">
                    <circle cx="240" cy="100" r="1.5" />
                    <circle cx="235" cy="115" r="2" />
                    <circle cx="225" cy="130" r="1.8" />
                    <circle cx="200" cy="142" r="1.2" />
                    <circle cx="160" cy="150" r="2.2" />
                    <circle cx="120" cy="142" r="1.4" />
                    <circle cx="95" cy="130" r="1.7" />
                    <circle cx="85" cy="115" r="2" />
                    <circle cx="80" cy="100" r="1.5" />
                    <circle cx="85" cy="85" r="1.8" />
                    <circle cx="95" cy="70" r="1.3" />
                    <circle cx="120" cy="58" r="2" />
                    <circle cx="160" cy="50" r="1.5" />
                    <circle cx="200" cy="58" r="1.8" />
                    <circle cx="225" cy="70" r="1.4" />
                    <circle cx="235" cy="85" r="2.2" />
                    <!-- Ceres (Largest Asteroid & Dwarf Planet) -->
                    <circle cx="240" cy="95" r="3.2" fill="#fef08a" stroke="#ca8a04" stroke-width="0.8" />
                    <text x="255" y="92" fill="#fde047" font-size="7" font-weight="bold">Ceres</text>
                </g>

                <!-- Jupiter Orbit (Outer Perturber) -->
                <ellipse cx="160" cy="100" rx="120" ry="75" fill="none" stroke="#eab308" stroke-width="1.2" stroke-dasharray="3,3" />
                <circle cx="280" cy="100" r="9" fill="#d97706" stroke="#fbbf24" stroke-width="1.5" />
                <text x="280" y="117" fill="#fde68a" font-size="7.5" font-weight="bold" text-anchor="middle">Jupiter</text>

                <!-- Gravitational Disruption Banner -->
                <rect x="25" y="160" width="270" height="30" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim14-status-line" x="160" y="179" fill="#fef08a" font-size="8.5" font-weight="bold" text-anchor="middle">Jupiter's gravity stirred debris, preventing planet formation</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="highlightCeres()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🪐 Inspect Ceres (Dwarf Planet)
            </button>
            <button onclick="stirJupiterGravity()" class="p-2 rounded-xl bg-yellow-600 hover:bg-yellow-500 text-xs font-bold text-white shadow transition">
                🌀 Simulate Jupiter's Gravitational Pull
            </button>
        </div>
        <div id="sim14-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Millions of rocky fragments orbit between Mars and Jupiter. Giant Jupiter's immense gravity prevented these primitive planetary building blocks from accreting into a single planet.
        </div>
    </div>
    """,

    15: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Comet Anatomy & Sublimation Tails</span>
            <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Anatomy: Nucleus + Coma + Dual Tails</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- The Sun (Emitting Radiation & Solar Wind) -->
                <g transform="translate(45, 100)">
                    <circle cx="0" cy="0" r="20" fill="#fbbf24" stroke="#f59e0b" stroke-width="2" />
                    <!-- Solar wind arrows pushing outward -->
                    <line x1="25" y1="0" x2="60" y2="0" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2" />
                    <line x1="22" y1="-12" x2="55" y2="-25" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2" />
                    <line x1="22" y1="12" x2="55" y2="25" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2" />
                    <text x="0" y="30" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Sun</text>
                    <text x="45" y="-30" fill="#eab308" font-size="7">Solar Wind ➔</text>
                </g>

                <!-- Comet Structure (Middle-Right) -->
                <g id="sim15-comet" transform="translate(180, 100)">
                    <!-- Ion Gas Tail (Straight, Blue, points directly opposite Sun) -->
                    <polygon id="sim15-ion-tail" points="0,0 120,-18 115,-8" fill="#38bdf8" opacity="0.75" />
                    <text x="110" y="-22" fill="#7dd3fc" font-size="7.5" font-weight="bold">Ion Gas Tail</text>

                    <!-- Dust Tail (Curved, Yellowish, follows orbital trail) -->
                    <path id="sim15-dust-tail" d="M 0,0 Q 60,15 110,35 L 105,45 Q 50,20 0,0 Z" fill="#fef08a" opacity="0.65" />
                    <text x="95" y="52" fill="#fef08a" font-size="7.5" font-weight="bold">Dust Tail</text>

                    <!-- Coma (Glowing Gas Envelope) -->
                    <circle cx="0" cy="0" r="14" fill="#67e8f9" opacity="0.4" filter="blur(2px)" />
                    <circle cx="0" cy="0" r="8" fill="#a5f3fc" opacity="0.6" />

                    <!-- Icy Nucleus (Dirty Snowball) -->
                    <circle cx="0" cy="0" r="4" fill="#334155" stroke="#94a3b8" stroke-width="1" />
                    <text x="-5" y="-12" fill="#e2e8f0" font-size="7.5" font-weight="bold">Icy Nucleus</text>
                </g>

                <!-- Orbital Cycle Banner -->
                <rect x="25" y="160" width="270" height="30" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim15-halley-text" x="160" y="179" fill="#67e8f9" font-size="8.5" font-weight="bold" text-anchor="middle">Tails always point AWAY from the Sun due to solar wind pressure</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="orbitCometNearSun()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                ☄️ Approach Sun (Sublimate & Grow Tails)
            </button>
            <button onclick="showHalleyPeriod()" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                📅 Halley's Comet (76-Year Cycle)
            </button>
        </div>
        <div id="sim15-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Comets are balls of frozen ice, dust, and rock. As they approach the Sun, heat sublimes ice directly into gas, forming a glowing coma and two massive tails that always point away from the Sun.
        </div>
    </div>
    """,

    16: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Milky Way (Ākāśha Gangā) & Cosmic Address</span>
            <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Galaxy: Barred Spiral (~100,000 ly)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Spiral Galaxy Core & Arms -->
                <g id="sim16-galaxy" transform="translate(160, 95)">
                    <!-- Central Supermassive Black Hole & Bulge Glow -->
                    <circle cx="0" cy="0" r="28" fill="#fef08a" opacity="0.3" filter="blur(6px)" />
                    <circle cx="0" cy="0" r="15" fill="#fef08a" stroke="#f59e0b" stroke-width="1.5" />
                    <circle cx="0" cy="0" r="5" fill="#000000" /> <!-- Sagittarius A* -->

                    <!-- Spiral Arms -->
                    <path d="M 0,0 Q 40,-20 80,0 T 130,-40" fill="none" stroke="#818cf8" stroke-width="12" opacity="0.25" stroke-linecap="round" />
                    <path d="M 0,0 Q -40,20 -80,0 T -130,40" fill="none" stroke="#818cf8" stroke-width="12" opacity="0.25" stroke-linecap="round" />
                    <path d="M 0,0 Q 20,40 0,80 T -50,110" fill="none" stroke="#c084fc" stroke-width="10" opacity="0.2" stroke-linecap="round" />
                    <path d="M 0,0 Q -20,-40 0,-80 T 50,-110" fill="none" stroke="#c084fc" stroke-width="10" opacity="0.2" stroke-linecap="round" />

                    <!-- Star Clusters throughout arms -->
                    <circle cx="50" cy="20" r="1.5" fill="#ffffff" />
                    <circle cx="-60" cy="-25" r="1.5" fill="#ffffff" />
                    <circle cx="30" cy="-60" r="1.5" fill="#ffffff" />
                    <circle cx="-40" cy="65" r="1.5" fill="#ffffff" />

                    <!-- Our Sun's Location in Orion-Cygnus Arm (26,000 ly from core) -->
                    <g id="sim16-sun-location" transform="translate(65, 30)">
                        <circle cx="0" cy="0" r="3.5" fill="#facc15" filter="drop-shadow(0 0 5px #fde047)" />
                        <!-- Target Reticle -->
                        <circle cx="0" cy="0" r="8" fill="none" stroke="#22d3ee" stroke-width="1" stroke-dasharray="2,2" />
                        <line x1="-12" y1="0" x2="12" y2="0" stroke="#22d3ee" stroke-width="0.8" />
                        <line x1="0" y1="-12" x2="0" y2="12" stroke="#22d3ee" stroke-width="0.8" />
                        <text x="14" y="3" fill="#fde047" font-size="8" font-weight="bold">Our Solar System</text>
                    </g>
                </g>

                <!-- Cosmic Hierarchy Banner -->
                <rect x="15" y="155" width="290" height="36" rx="6" fill="#0f172a" stroke="#334155" />
                <text id="sim16-address" x="160" y="177" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">Earth ➔ Solar System ➔ Orion Arm ➔ Milky Way ➔ Universe</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="pinpointSunLocation()" class="p-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white shadow transition">
                📍 Pinpoint Our Sun (~26,000 ly)
            </button>
            <button onclick="scanExoplanets()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🪐 Scan Habitable Goldilocks Zones
            </button>
        </div>
        <div id="sim16-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Our Sun is just one of over 100 billion stars in the Milky Way (Ākāśha Gangā) spiral galaxy. Modern telescopes have detected thousands of exoplanets orbiting distant stars across the cosmos.
        </div>
    </div>
    """
}


# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 9 to 16
Class 4 Science Chapter 9: Different Lands, Different Lives
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part2 = {
    # Simulator 9: Puri Coastal Seashore
    "sim_puri_coast": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Puri Seashore: Wave Dynamics & Coastal Palm Roots</h3>
                <p class="text-xs text-slate-400">Trigger ocean high-tide waves and observe how palm root networks anchor sand dunes against erosion.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="triggerPuriTide('high')" class="px-3 py-1 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition">🌊 High Tide Wave</button>
                <button onclick="triggerPuriTide('low')" class="px-3 py-1 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">🏖️ Calm Low Tide</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Coastal Seashore Animation SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Sky & Morning Sun -->
                    <rect x="0" y="0" width="500" height="90" fill="#0f172a"/>
                    <circle cx="80" cy="50" r="22" fill="#fbbf24" opacity="0.9"/>

                    <!-- Ocean Waters -->
                    <path id="puriOceanPath" d="M0,90 Q125,75 250,90 T500,85 L500,160 Q350,175 180,165 L0,170 Z" fill="#0284c7" opacity="0.8"/>
                    
                    <!-- Sandy Shoreline / Beach Dunes -->
                    <path d="M0,150 Q180,140 320,155 T500,145 L500,230 L0,230 Z" fill="#d97706"/>
                    <text x="380" y="210" fill="#fef3c7" font-size="10" font-weight="bold">Golden Sandy Shore</text>

                    <!-- Coconut Palm on Dune -->
                    <g transform="translate(380, 50)">
                        <!-- Curved flexible trunk -->
                        <path d="M50,110 Q35,50 60,10" stroke="#78350f" stroke-width="8" fill="none"/>
                        <!-- Green fronds -->
                        <path d="M60,10 Q30,-15 10,-10" stroke="#15803d" stroke-width="4" fill="none"/>
                        <path d="M60,10 Q80,-20 110,-10" stroke="#15803d" stroke-width="4" fill="none"/>
                        <path d="M60,10 Q95,15 120,30" stroke="#15803d" stroke-width="4" fill="none"/>
                        <path d="M60,10 Q30,20 15,35" stroke="#15803d" stroke-width="4" fill="none"/>
                        <!-- Subterranean Root Network -->
                        <path id="palmRootNetwork" d="M50,110 Q30,130 15,155 M50,110 Q65,135 80,160 M50,110 Q50,140 50,170" stroke="#451a03" stroke-width="3" fill="none"/>
                        <text x="45" y="145" fill="#fef3c7" font-size="8">Fibrous Roots</text>
                    </g>

                    <!-- Artisanal Fishing Boat -->
                    <g id="puriFishingBoat" transform="translate(140, 95)" class="cursor-pointer transition-transform duration-500">
                        <path d="M0,15 Q30,30 60,15 L50,0 L10,0 Z" fill="#b45309" stroke="#78350f"/>
                        <line x1="30" y1="0" x2="30" y2="-20" stroke="#334155" stroke-width="2"/>
                        <polygon points="30,-20 50,-5 30,-5" fill="#f8fafc" opacity="0.9"/>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="puriWaveStatus">🌊 Wave State: Calm Gentle Breakers</span>
                    <span class="text-cyan-400">Roots bind 95% of beach sand against wave wash</span>
                </div>
            </div>

            <!-- Coastal Science Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Shoreline Ecosystem</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">TIDAL RANGE</span>
                        <span class="font-bold text-cyan-300">Semi-diurnal (2 High, 2 Low Daily)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">COASTAL FLORA</span>
                        <span class="font-semibold text-slate-200">Coconut Palms, Palmyra, Casuarina</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">COMMUNITY TRADE</span>
                        <span class="font-semibold text-emerald-400">Artisanal Net Fishing & Sand Art</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 10: Marine Coastal Biodiversity
    "sim_marine_life": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Olive Ridley Turtle Arribada & Dolphin Sonar</h3>
                <p class="text-xs text-slate-400">Follow the mother turtle digging her nest cavity and see how hatchlings navigate by moonlight.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="animateTurtleNesting()" class="px-2.5 py-1 text-xs rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">🐢 Turtle Nesting</button>
                <button onclick="toggleBeachLights()" id="btnLightToggle" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 text-yellow-300 font-semibold transition">💡 Toggle Beach Lights</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Sea Turtle Nesting Box -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wide">Olive Ridley Arribada</span>
                    <span id="turtleEggCount" class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">Eggs: 110 buried</span>
                </div>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 relative flex flex-col justify-end p-3 overflow-hidden">
                    <!-- Sand pit -->
                    <div class="w-full h-16 bg-amber-800/80 rounded-t-xl relative flex items-center justify-center">
                        <div id="turtleEggsGroup" class="flex gap-1 flex-wrap justify-center w-28">
                            <span class="w-2.5 h-2.5 rounded-full bg-white shadow-sm inline-block"></span>
                            <span class="w-2.5 h-2.5 rounded-full bg-white shadow-sm inline-block"></span>
                            <span class="w-2.5 h-2.5 rounded-full bg-white shadow-sm inline-block"></span>
                            <span class="w-2.5 h-2.5 rounded-full bg-white shadow-sm inline-block"></span>
                            <span class="w-2.5 h-2.5 rounded-full bg-white shadow-sm inline-block"></span>
                        </div>
                    </div>
                    <!-- Mother Turtle -->
                    <div id="turtleMotherSvg" class="absolute top-2 left-1/2 -translate-x-1/2 flex flex-col items-center">
                        <span class="text-3xl">🐢</span>
                    </div>
                </div>
                <p id="turtleStatusText" class="text-[11px] text-slate-300">Mother turtle digs a 50 cm flask cavity with hind flippers, deposits soft-shelled eggs, and covers them with sand.</p>
            </div>

            <!-- Hatchling Orientation & Dolphin Sonar -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Marine Navigation & Sonar</span>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 relative flex items-center justify-around p-2">
                    <!-- Dolphin -->
                    <div class="text-center">
                        <span class="text-2xl animate-pulse">🐬</span>
                        <span class="text-[9px] text-cyan-300 block font-bold">Echolocation</span>
                    </div>
                    <!-- Sound waves -->
                    <div class="flex gap-1">
                        <span class="w-1 h-6 bg-cyan-400/80 rounded-full animate-ping"></span>
                        <span class="w-1 h-10 bg-cyan-400/60 rounded-full"></span>
                        <span class="w-1 h-14 bg-cyan-400/40 rounded-full"></span>
                    </div>
                    <!-- Ghost Crab -->
                    <div class="text-center">
                        <span class="text-xl">🦀</span>
                        <span class="text-[9px] text-amber-300 block font-bold">Intertidal Crab</span>
                    </div>
                </div>
                <div id="lightWarningBox" class="p-2 rounded bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    Natural Moon Horizon: Safe navigation into the open sea. Keep beach lights OFF!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 11: Coastal Chariot Heritage
    "sim_rath_yatra": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Puri Rath Yatra: Giant Timber Chariot Engineering</h3>
                <p class="text-xs text-slate-400">Examine the 45-foot wooden chariot, crafted each year without iron nails using mortise and tenon joinery.</p>
            </div>
            <button onclick="pullChariotRopes()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition flex items-center gap-1.5">
                <span>🪢</span> Pull Sacred Ropes
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Chariot SVG Diagram -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[240px]">
                <svg viewBox="0 0 500 240" class="w-full h-auto">
                    <!-- Grand Road Avenue -->
                    <rect x="0" y="190" width="500" height="50" fill="#334155"/>
                    <line x1="0" y1="215" x2="500" y2="215" stroke="#475569" stroke-dasharray="8,8"/>

                    <!-- Chariot Structure -->
                    <g id="chariotGroup" transform="translate(180, 20)" class="transition-transform duration-700">
                        <!-- Pinnacle / Shikhara canopy -->
                        <polygon points="70,0 20,60 120,60" fill="#dc2626" stroke="#b91c1c" stroke-width="2"/>
                        <circle cx="70" cy="-5" r="5" fill="#facc15"/> <!-- Kalasha -->
                        <!-- Central Pavilion Room -->
                        <rect x="25" y="60" width="90" height="70" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
                        <!-- Wooden carved Pillars -->
                        <line x1="35" y1="60" x2="35" y2="130" stroke="#78350f" stroke-width="5"/>
                        <line x1="105" y1="60" x2="105" y2="130" stroke="#78350f" stroke-width="5"/>
                        <!-- Lower Chassis Frame -->
                        <rect x="10" y="130" width="120" height="25" fill="#78350f" rx="3"/>
                        <text x="70" y="146" fill="#fef3c7" font-size="8" text-anchor="middle" font-weight="bold">Wooden Joinery (No Nails)</text>
                        <!-- Massive Multi-spoke Wheels (16 spokes) -->
                        <circle cx="35" cy="175" r="22" fill="#451a03" stroke="#b45309" stroke-width="3"/>
                        <circle cx="35" cy="175" r="7" fill="#facc15"/>
                        <circle cx="105" cy="175" r="22" fill="#451a03" stroke="#b45309" stroke-width="3"/>
                        <circle cx="105" cy="175" r="7" fill="#facc15"/>
                    </g>

                    <!-- Coir Pulling Ropes -->
                    <path id="chariotRopePath" d="M190,165 Q100,175 10,185" stroke="#ca8a04" stroke-width="5" fill="none"/>
                    <text x="90" y="165" fill="#ca8a04" font-size="9" font-weight="bold">Heavy Coir Ropes</text>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="chariotMoveStatus">Chariot Stationary at Bada Danda (Grand Road)</span>
                    <span class="text-amber-400 font-bold">45 Feet Tall • 16 Massive Wheels</span>
                </div>
            </div>

            <!-- Architectural Heritage Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wide">Heritage Architecture</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">MATERIAL ENGINEERING</span>
                        <span class="font-bold text-amber-300">Seasoned Timber + Coir Fiber (No Metal Nails)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">PULLING PARTICIPATION</span>
                        <span class="font-bold text-cyan-300">Over 1,000,000 Devotees Together</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">PERFORMING ART</span>
                        <span class="font-semibold text-slate-200">Odissi Dance (Tribhanga Wave Movements)</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 12: Cyclone Early Warning
    "sim_cyclone_warning": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Coastal Disaster Management & Cyclone Radar</h3>
                <p class="text-xs text-slate-400">Track a tropical cyclone trajectory on the Doppler radar screen and execute zero-casualty village evacuations.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="triggerCycloneRadarSweep()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">🔄 Radar Sweep</button>
                <button onclick="evacuateToShelter()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition">🛡️ Evacuate Villages</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Doppler Radar Screen -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Doppler Weather Radar (Bay of Bengal)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded bg-red-500/20 text-red-300 border border-red-500/30 animate-pulse">Category 3 Cyclone</span>
                </div>
                <div class="h-36 bg-slate-900 rounded-lg border border-slate-800 relative flex items-center justify-center overflow-hidden">
                    <!-- Concentric Range Rings -->
                    <circle cx="50%" cy="50%" r="55" fill="none" stroke="#334155" stroke-dasharray="2,2"/>
                    <circle cx="50%" cy="50%" r="35" fill="none" stroke="#334155" stroke-dasharray="2,2"/>
                    <!-- Radar Sweep Line -->
                    <div id="radarSweepLine" class="absolute w-36 h-0.5 bg-cyan-400 origin-left animate-spin" style="animation-duration: 3s;"></div>
                    <!-- Cyclone Eye -->
                    <div id="cycloneEyeIcon" class="text-2xl text-red-500 absolute top-6 right-10 animate-spin" style="animation-duration: 4s;">🌀</div>
                    <span class="text-[10px] text-slate-400 absolute bottom-2 left-2">Odisha Shoreline (Distance: 180 km)</span>
                </div>
                <div class="flex justify-between text-xs text-slate-300">
                    <span>Wind Speed: <b class="text-red-400">165 km/h</b></span>
                    <span>Landfall Forecast: <b class="text-amber-400">28 Hours</b></span>
                </div>
            </div>

            <!-- Elevated Multi-Purpose Cyclone Shelter -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wide">Elevated Concrete Refuge Shelter</span>
                    <span id="evacStatusBadge" class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">Safe: 2,400 People</span>
                </div>
                <!-- Shelter Graphic -->
                <div class="h-36 bg-slate-900 rounded-lg border border-slate-800 p-3 flex flex-col justify-between">
                    <div class="flex justify-between items-start">
                        <span class="text-xs font-bold text-emerald-300">Reinforced Concrete Upper Floor</span>
                        <span class="text-xs">☀️ Solar Power</span>
                    </div>
                    <!-- Wave level vs Concrete Stilts -->
                    <div class="space-y-1">
                        <div class="w-full bg-slate-800 h-10 rounded border border-slate-700 flex items-center justify-center text-xs font-bold text-emerald-200">
                            Safe Living Quarters + Potable Water + First Aid
                        </div>
                        <div class="flex justify-around">
                            <div class="w-4 h-8 bg-slate-600"></div>
                            <div class="w-4 h-8 bg-slate-600"></div>
                            <div class="w-4 h-8 bg-slate-600"></div>
                        </div>
                    </div>
                    <div class="text-[10px] text-cyan-400 font-semibold text-center">
                        Built 5 metres above ground to allow storm surge waves to pass underneath safely.
                    </div>
                </div>
                <p id="evacLogText" class="text-[11px] text-slate-400">Warning sirens activated across 48 coastal towers; zero-casualty protocol in action.</p>
            </div>
        </div>
    </div>
    """,

    # Simulator 13: Himalayan Mountain Landforms
    "sim_sikkim_mountains": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-indigo-300">Sikkim Alpine Relief: Mount Kangchenjunga & Terraces</h3>
                <p class="text-xs text-slate-400">Simulate sunrise alpenglow over Mount Kangchenjunga (8,586 m) and inspect hillside terrace farming.</p>
            </div>
            <button onclick="toggleKangchenjungaSun()" id="btnSunToggle" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                🌅 Sunrise Alpenglow
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Mountain Relief SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Sky Gradient -->
                    <rect id="alpineSkyRect" x="0" y="0" width="500" height="230" fill="#0f172a"/>

                    <!-- Mount Kangchenjunga (Third Highest Peak - 8,586 m) -->
                    <polygon id="peakKanchenjunga" points="250,20 180,120 320,120" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
                    <!-- Golden/Pink Sunrise Glaciers -->
                    <polygon id="peakSnowGlacier" points="250,20 215,80 285,80" fill="#ffffff" opacity="0.95"/>
                    <text x="250" y="15" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Mount Kangchenjunga (8,586 m)</text>

                    <!-- Flanking Himalayan Ridges -->
                    <polygon points="100,60 20,160 180,160" fill="#334155" opacity="0.8"/>
                    <polygon points="400,60 320,160 480,160" fill="#334155" opacity="0.8"/>

                    <!-- Steep River Gorge with Teesta River -->
                    <path d="M220,140 Q250,170 230,230 L270,230 Q290,170 260,140 Z" fill="#38bdf8"/>
                    <text x="250" y="215" fill="#0c4a6e" font-size="9" font-weight="bold" text-anchor="middle">Teesta River</text>

                    <!-- Stepped Hillside Terraces (Left Slope) -->
                    <g transform="translate(40, 130)">
                        <polygon points="0,0 80,0 70,15 0,15" fill="#15803d"/>
                        <polygon points="0,15 90,15 80,30 0,30" fill="#166534"/>
                        <polygon points="0,30 100,30 90,45 0,45" fill="#15803d"/>
                        <text x="20" y="25" fill="#fef3c7" font-size="7" font-weight="bold">Stepped Terraces</text>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="mountainSunStatus">Current Time: Dawn (First Light Striking Glaciers)</span>
                    <span class="text-indigo-400 font-bold">Altitude: 8,586 m • Glacial Water</span>
                </div>
            </div>

            <!-- Alpine Science Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-indigo-400 uppercase tracking-wide">Highland Geography</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">ELEVATION EXTREMES</span>
                        <span class="font-bold text-indigo-300">280 m (Valleys) to 8,586 m (Summit)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SOIL EROSION CONTROL</span>
                        <span class="font-bold text-emerald-400">Terraced Benches Slow Rainwater Runoff</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">CASH CROPS</span>
                        <span class="font-semibold text-slate-200">Large Black Cardamom, Ginger, Maize</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 14: Mountain Lifestyle Warmth
    "sim_mountain_lifestyle": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Highland Thermal Adaptations: Bakhu, Thukpa & Yak</h3>
                <p class="text-xs text-slate-400">Explore woollen bakhu coat insulation, prepare hot thukpa noodle soup, and test yak high-altitude biology.</p>
            </div>
            <button onclick="feedHotThukpa()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition">🍲 Serve Hot Thukpa</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <!-- 1. Woollen Bakhu Layering -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wide">1. Woollen Bakhu Coat</span>
                <p class="text-[11px] text-slate-300">Full-length wool coat wrapped securely with a broad belt over a silk honju blouse.</p>
                <div class="p-2 rounded bg-slate-900 border border-slate-800 space-y-1 text-xs">
                    <div class="flex justify-between">
                        <span class="text-slate-400">Air Temperature:</span>
                        <span class="text-blue-400 font-bold">-4°C</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">Skin Surface:</span>
                        <span class="text-emerald-400 font-bold">35°C (Warm!)</span>
                    </div>
                </div>
            </div>

            <!-- 2. High-Calorie Steaming Thukpa -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">2. Warming Thukpa & Sel Roti</span>
                <p class="text-[11px] text-slate-300">Piping-hot noodle soup with ginger, garlic, vegetables, and crispy ring-shaped rice flatbreads.</p>
                <div class="h-16 bg-slate-900 rounded flex items-center justify-center gap-3">
                    <span class="text-2xl animate-bounce">🍲</span>
                    <span class="text-xl">🥯</span>
                </div>
                <div id="thukpaEnergyMeter" class="text-[10px] text-amber-300 font-semibold text-center">
                    Instant metabolic thermal energy for chilly evenings
                </div>
            </div>

            <!-- 3. Himalayan Yak Biology -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">3. Domestic Yak Biology</span>
                <p class="text-[11px] text-slate-300">Double-layered wool coat, sure-footed hooves, and expanded lungs for thin high-altitude air.</p>
                <div class="p-2 rounded bg-slate-900 border border-slate-800 text-[11px] space-y-1">
                    <span class="text-cyan-300 block font-bold">● High Lung Capacity: Thrives in thin air</span>
                    <span class="text-amber-300 block font-bold">● Rich Milk: Churned into Chhurpi cheese</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 15: Mountain Flora Festivals
    "sim_mountain_festivals": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Pitched Wooden Roofs & Sacred Chaam Mask Dance</h3>
                <p class="text-xs text-slate-400">Slide snowfall off the steep pitched wooden roof and trigger the traditional chaam mask dance.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="triggerRoofSnow()" class="px-2.5 py-1 text-xs rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold transition">❄️ Shed Roof Snow</button>
                <button onclick="spinChaamDancer()" class="px-2.5 py-1 text-xs rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">🎭 Spin Chaam Dance</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Pitched Roof Simulation -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-blue-400 uppercase tracking-wide">Steep Sloping Roof Engineering</span>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 relative flex items-center justify-center p-2">
                    <svg viewBox="0 0 200 120" class="w-40 h-auto">
                        <!-- House Body -->
                        <rect x="50" y="60" width="100" height="50" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                        <!-- Steep Pitched Roof (50 degree slope) -->
                        <polygon points="100,10 40,60 160,60" fill="#334155" stroke="#64748b" stroke-width="2"/>
                        <!-- Snow Layer on Roof -->
                        <polygon id="roofSnowPolygon" points="100,6 36,60 44,60 100,14 156,60 164,60" fill="#ffffff" opacity="0.95"/>
                    </svg>
                </div>
                <p id="roofSnowStatus" class="text-[11px] text-slate-300">Steep angles allow heavy winter snow and monsoon downpours to slide off immediately, preventing ceiling collapse.</p>
            </div>

            <!-- Sacred Chaam Mask Dance -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">Loosong Monastic Chaam Dance</span>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-around p-2">
                    <!-- Rotating Chaam Mask -->
                    <div id="chaamMaskIcon" class="text-4xl transition-transform duration-700">
                        🎭
                    </div>
                    <!-- Musical Instruments -->
                    <div class="text-center space-y-1">
                        <span class="text-xs font-bold text-cyan-300 block">Dungchen Horns</span>
                        <span class="text-[11px] text-slate-400 block">Long copper trumpets echoing across valleys</span>
                        <span class="text-xs font-bold text-amber-300 block">Rhythmic Cymbals</span>
                    </div>
                </div>
                <p class="text-[11px] text-slate-300">Performed during Loosong (Sikkimese New Year) to destroy negative energies and welcome abundant seasonal harvests.</p>
            </div>
        </div>
    </div>
    """,

    # Simulator 16: Landform Comparison Matrix
    "sim_comparison_matrix": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Master Synthesis: Four Indian Landforms Comparison Matrix</h3>
                <p class="text-xs text-slate-400">Compare physical features, primary crops, wildlife, shelters, and water systems across all four environments.</p>
            </div>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-slate-300 border-collapse">
                <thead>
                    <tr class="border-b border-slate-800 text-[11px] text-slate-400 uppercase bg-slate-950">
                        <th class="p-2.5">Feature</th>
                        <th class="p-2.5 text-emerald-400">🌾 Plains (Punjab)</th>
                        <th class="p-2.5 text-amber-400">🏜️ Desert (Thar)</th>
                        <th class="p-2.5 text-cyan-400">🏖️ Coast (Puri)</th>
                        <th class="p-2.5 text-indigo-400">🏔️ Mountains (Sikkim)</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/60">
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-slate-200">Soil Type</td>
                        <td class="p-2.5">Fertile river alluvium</td>
                        <td class="p-2.5">Coarse sandy dunes</td>
                        <td class="p-2.5">Saline sandy shoreline</td>
                        <td class="p-2.5">Rocky gravel hill soil</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-slate-200">Signature Foods</td>
                        <td class="p-2.5">Makki roti, Sarson saag</td>
                        <td class="p-2.5">Dal-bati, Ker sangri</td>
                        <td class="p-2.5">Fresh fish, Crab curry</td>
                        <td class="p-2.5">Thukpa soup, Sel roti</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-slate-200">Traditional Shelter</td>
                        <td class="p-2.5">Brick/mud farm houses</td>
                        <td class="p-2.5">Thick mud walls + thatch</td>
                        <td class="p-2.5">Palm thatch & shelters</td>
                        <td class="p-2.5">Pitched wooden roofs</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-slate-200">Water Adaptation</td>
                        <td class="p-2.5">Canals & tube wells</td>
                        <td class="p-2.5">Underground tankas</td>
                        <td class="p-2.5">Cyclone storm shelters</td>
                        <td class="p-2.5">Glacial streams & springs</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-slate-200">Key Fauna</td>
                        <td class="p-2.5">Cattle, buffaloes</td>
                        <td class="p-2.5">Camels, desert lizards</td>
                        <td class="p-2.5">Sea turtles, dolphins</td>
                        <td class="p-2.5">Domestic yaks, red pandas</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """
}


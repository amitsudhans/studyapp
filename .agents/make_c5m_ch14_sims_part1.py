# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Chapter 14: Maps and Locations"""

sims_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">🕊️ Siberian Crane Migration Route</span>
                <span id="sim1_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Total: 5,200 km</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Animate the migratory flight from Arctic Siberia southward to Bharatpur, Rajasthan:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim1AnimateFlight()" id="sim1_fly_btn" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">Start Southward Flight ➔</button>
                <button onclick="sim1Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim1_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Compass Rose -->
                    <circle cx="170" cy="30" r="14" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                    <line x1="170" y1="18" x2="170" y2="42" stroke="#38bdf8" stroke-width="1.5"/>
                    <line x1="158" y1="30" x2="182" y2="30" stroke="#94a3b8" stroke-width="1"/>
                    <text x="170" y="16" text-anchor="middle" font-size="7" fill="#38bdf8" font-weight="bold">N</text>
                    <!-- Flight Path Line -->
                    <path d="M 50 25 Q 120 70 100 135" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="4,2"/>
                    <!-- Siberia Landmark -->
                    <circle cx="50" cy="25" r="5" fill="#38bdf8"/>
                    <text x="50" y="18" text-anchor="middle" font-size="8" fill="#38bdf8" font-weight="bold">Siberia (North)</text>
                    <!-- Bharatpur Landmark -->
                    <circle cx="100" cy="135" r="5" fill="#f59e0b"/>
                    <text x="100" y="150" text-anchor="middle" font-size="8" fill="#f59e0b" font-weight="bold">Bharatpur (South)</text>
                    <!-- Crane Marker -->
                    <g id="sim1_crane" transform="translate(50, 25)">
                        <circle cx="0" cy="0" r="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
                        <polygon points="-6,-2 0,4 6,-2" fill="#38bdf8" opacity="0.8"/>
                    </g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold block mb-1">Directional Vector:</span>
                    <div id="sim1_dir_txt" class="text-amber-300 font-bold">Heading: Southwards (S)</div>
                    <div class="text-[10px] text-slate-400 mt-0.5">Navigating via celestial landmarks and Earth's magnetic field.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Distance Flown:</span>
                    <span id="sim1_dist" class="text-emerald-400 font-bold text-sm">0 km / 5,200 km</span>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧭 Cardinal Compass & Sun Explorer</span>
                <span id="sim2_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Facing East</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Face the rising sun or select a direction to establish left, right, and opposite bearings:</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 mb-2">
                <button onclick="sim2Face('east')" id="sim2_btn_east" class="px-2 py-1 rounded bg-amber-600 text-white font-bold">Face East (Sun)</button>
                <button onclick="sim2Face('north')" id="sim2_btn_north" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Face North</button>
                <button onclick="sim2Face('west')" id="sim2_btn_west" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Face West</button>
                <button onclick="sim2Face('south')" id="sim2_btn_south" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Face South</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim2_svg" viewBox="0 0 180 140" class="w-44 h-32">
                    <!-- Compass Axes -->
                    <line x1="90" y1="20" x2="90" y2="120" stroke="#475569" stroke-width="1.5"/>
                    <line x1="30" y1="70" x2="150" y2="70" stroke="#475569" stroke-width="1.5"/>
                    <text x="90" y="15" text-anchor="middle" font-size="9" fill="#38bdf8" font-weight="bold">North (N)</text>
                    <text x="90" y="132" text-anchor="middle" font-size="9" fill="#10b981" font-weight="bold">South (S)</text>
                    <text x="165" y="73" text-anchor="middle" font-size="9" fill="#f59e0b" font-weight="bold">East (E)</text>
                    <text x="15" y="73" text-anchor="middle" font-size="9" fill="#f43f5e" font-weight="bold">West (W)</text>
                    <!-- Rising Sun -->
                    <circle cx="140" cy="40" r="10" fill="#f59e0b" opacity="0.8"/>
                    <text x="140" y="58" text-anchor="middle" font-size="6" fill="#facc15 font-bold">Rising Sun</text>
                    <!-- Pointer Arrow -->
                    <g id="sim2_pointer" transform="rotate(90, 90, 70)">
                        <polygon points="90,40 95,75 85,75" fill="#f59e0b"/>
                        <circle cx="90" cy="70" r="4" fill="#ffffff"/>
                    </g>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold">Front:</span> <span id="sim2_front" class="text-white">East (Facing Sun)</span>
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold">Left Hand:</span> <span id="sim2_left" class="text-white">North</span>
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold">Right Hand:</span> <span id="sim2_right" class="text-white">South</span>
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-rose-400 font-bold">Behind Back:</span> <span id="sim2_back" class="text-white">West (Setting Sun)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-purple-400">🐣 Four Chicks Flight Trajectory</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Perpendicular 90° Axes</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Animate the four chicks flying out from their nest along the four cardinal directions:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim3FlyChicks()" id="sim3_btn_fly" class="flex-1 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-bold transition">Fly All 4 Chicks Out ➔</button>
                <button onclick="sim3Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim3_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Axes -->
                    <line x1="80" y1="15" x2="80" y2="125" stroke="#475569" stroke-width="1.5"/>
                    <line x1="20" y1="70" x2="140" y2="70" stroke="#475569" stroke-width="1.5"/>
                    <!-- Central Nest -->
                    <circle cx="80" cy="70" r="10" fill="#78350f" stroke="#d97706" stroke-width="1.5"/>
                    <text x="80" y="73" text-anchor="middle" font-size="7" fill="#fef3c7" font-weight="bold">Nest</text>
                    <!-- Chick 1 (N) -->
                    <circle id="sim3_c1" cx="80" cy="70" r="5" fill="#38bdf8"/>
                    <!-- Chick 2 (S) -->
                    <circle id="sim3_c2" cx="80" cy="70" r="5" fill="#10b981"/>
                    <!-- Chick 3 (E) -->
                    <circle id="sim3_c3" cx="80" cy="70" r="5" fill="#f59e0b"/>
                    <!-- Chick 4 (W) -->
                    <circle id="sim3_c4" cx="80" cy="70" r="5" fill="#f43f5e"/>
                    <!-- Labels -->
                    <text x="80" y="10" text-anchor="middle" font-size="7" fill="#38bdf8" font-weight="bold">North (Chick 1)</text>
                    <text x="80" y="135" text-anchor="middle" font-size="7" fill="#10b981" font-weight="bold">South (Chick 2)</text>
                    <text x="145" y="73" font-size="7" fill="#f59e0b" font-weight="bold">East (3)</text>
                    <text x="15" y="73" text-anchor="end" font-size="7" fill="#f43f5e" font-weight="bold">West (4)</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-purple-300 font-bold block mb-1">Perpendicular Geometry:</span>
                    <div class="text-slate-300 text-[10px]">North ↔ South: Vertical Axis (180°)</div>
                    <div class="text-slate-300 text-[10px]">East ↔ West: Horizontal Axis (180°)</div>
                    <div class="text-amber-300 font-bold mt-1">Cross Angle: 90° Right Angle</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold">Opposite Pairs:</span>
                    <span class="text-slate-400 block text-[10px]">North is opposite South; East is opposite West.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">⛺ Campsite Map & Legend Studio</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Bird Watching Camp</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click to apply directional color clues to the tents around the road and lake:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim4ColorTents()" id="sim4_btn_color" class="px-2.5 py-1 rounded bg-emerald-600 text-white font-bold">Apply Color Clues ➔</button>
                <button onclick="sim4AddEastTent()" id="sim4_btn_east" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Draw Tent East of Lake</button>
                <button onclick="sim4Reset()" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Reset</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim4_svg" viewBox="0 0 180 140" class="w-44 h-32">
                    <!-- Central Road -->
                    <line x1="70" y1="10" x2="70" y2="130" stroke="#64748b" stroke-width="6"/>
                    <line x1="70" y1="10" x2="70" y2="130" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="3,3"/>
                    <text x="65" y="15" text-anchor="end" font-size="6" fill="#94a3b8">Road</text>
                    <!-- Lake in East -->
                    <ellipse cx="125" cy="70" rx="22" ry="16" fill="#0284c7" opacity="0.6" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="125" y="72" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Lake</text>
                    <!-- Tent West of Road (Blue) -->
                    <polygon id="sim4_t_west" points="30,55 42,75 18,75" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
                    <text x="30" y="83" text-anchor="middle" font-size="6" fill="#94a3b8" id="sim4_lbl_west">West Tent</text>
                    <!-- Tent Closest to Lake (Green) -->
                    <polygon id="sim4_t_lake" points="100,55 108,70 92,70" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
                    <!-- Tent North of Green (Purple) -->
                    <polygon id="sim4_t_north" points="100,20 108,35 92,35" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
                    <!-- Tent South of Lake (Yellow) -->
                    <polygon id="sim4_t_south" points="125,100 133,115 117,115" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
                    <!-- Dynamic East Tent -->
                    <polygon id="sim4_t_east" points="160,60 168,75 152,75" fill="#475569" opacity="0"/>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[10px]">
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-blue-400 font-bold">1. West of Road:</span> Blue Tent
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold">2. Near Lake:</span> Green Tent
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-purple-400 font-bold">3. North of Green:</span> Purple Tent
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-yellow-400 font-bold">4. South of Lake:</span> Yellow Tent
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-blue-400">🛏️ Room Layout & Relative Directions</span>
                <span id="sim5_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Observer at Center</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click furniture to see its cardinal and relative directions from the student at the center:</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 mb-2">
                <button onclick="sim5Inspect('window')" id="sim5_btn_window" class="px-2 py-1 rounded bg-cyan-600 text-white font-bold">Window (N)</button>
                <button onclick="sim5Inspect('bed')" id="sim5_btn_bed" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Bed (E)</button>
                <button onclick="sim5Inspect('door')" id="sim5_btn_door" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Door (S)</button>
                <button onclick="sim5Inspect('cupboard')" id="sim5_btn_cupboard" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Cupboard (W)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim5_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Room Walls -->
                    <rect x="20" y="15" width="120" height="110" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                    <!-- Window on North Wall -->
                    <rect id="sim5_rect_window" x="60" y="13" width="40" height="4" fill="#38bdf8"/>
                    <text x="80" y="25" text-anchor="middle" font-size="7" fill="#38bdf8" font-weight="bold">Window (N)</text>
                    <!-- Door on South Wall -->
                    <rect id="sim5_rect_door" x="65" y="123" width="30" height="4" fill="#f43f5e"/>
                    <text x="80" y="120" text-anchor="middle" font-size="7" fill="#f43f5e" font-weight="bold">Door (S)</text>
                    <!-- Bed on East Wall -->
                    <rect id="sim5_rect_bed" x="115" y="45" width="23" height="50" rx="3" fill="#10b981" stroke="#34d399" stroke-width="1"/>
                    <text x="126" y="73" text-anchor="middle" font-size="6" fill="#ffffff" font-weight="bold">Bed</text>
                    <!-- Cupboard on West Wall -->
                    <rect id="sim5_rect_cupboard" x="22" y="45" width="18" height="50" rx="2" fill="#f59e0b" stroke="#fbbf24" stroke-width="1"/>
                    <text x="31" y="73" text-anchor="middle" font-size="5" fill="#ffffff" font-weight="bold">Wardrobe</text>
                    <!-- Center Figure -->
                    <circle cx="80" cy="70" r="6" fill="#a855f7" stroke="#ffffff" stroke-width="1.5"/>
                    <!-- Sight arrow facing North -->
                    <polygon points="80,58 83,63 77,63" fill="#a855f7"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-blue-300 font-bold block mb-1" id="sim5_item_title">Window on Northern Wall</span>
                    <div id="sim5_cardinal" class="text-emerald-400 font-bold">Cardinal Direction: North</div>
                    <div id="sim5_relative" class="text-slate-300 text-[10px] mt-1">Relative to Observer: Directly in Front</div>
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">🔄 Dynamic Observer Heading Simulator</span>
                <span id="sim6_heading_txt" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Facing: North (0°)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Rotate the observer to see how relative left/right directions change while cardinal axes stay fixed:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim6Turn(-90)" class="flex-1 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">↶ Turn 90° Left</button>
                <button onclick="sim6Turn(90)" class="flex-1 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-bold transition">↷ Turn 90° Right</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim6_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <line x1="80" y1="15" x2="80" y2="125" stroke="#475569" stroke-width="1.5"/>
                    <line x1="20" y1="70" x2="140" y2="70" stroke="#475569" stroke-width="1.5"/>
                    <text x="80" y="12" text-anchor="middle" font-size="8" fill="#38bdf8" font-weight="bold">N</text>
                    <text x="80" y="135" text-anchor="middle" font-size="8" fill="#10b981" font-weight="bold">S</text>
                    <text x="148" y="73" font-size="8" fill="#f59e0b" font-weight="bold">E</text>
                    <text x="12" y="73" text-anchor="end" font-size="8" fill="#f43f5e" font-weight="bold">W</text>
                    <!-- Observer Body and Gaze Arrow -->
                    <g id="sim6_avatar" transform="rotate(0, 80, 70)">
                        <circle cx="80" cy="70" r="10" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
                        <polygon points="80,50 85,62 75,62" fill="#facc15"/>
                        <!-- Left arm indicator (pink) -->
                        <line x1="70" y1="70" x2="62" y2="70" stroke="#f43f5e" stroke-width="2.5"/>
                        <!-- Right arm indicator (cyan) -->
                        <line x1="90" y1="70" x2="98" y2="70" stroke="#38bdf8" stroke-width="2.5"/>
                    </g>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[10px]">
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-300 font-bold">Front Heading:</span> <span id="sim6_facing">North</span>
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold">Right Hand Points:</span> <span id="sim6_right">East</span>
                </div>
                <div class="p-1.5 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-rose-300 font-bold">Left Hand Points:</span> <span id="sim6_left">West</span>
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚌 School Bus Field Trip Route</span>
                <span id="sim7_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">At Depot</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Advance the school bus along the street grid to pick up students at each designated stop:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim7Step()" id="sim7_btn_step" class="flex-1 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Drive to Next Stop ➔</button>
                <button onclick="sim7Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
            <svg id="sim7_svg" viewBox="0 0 320 110" class="w-full h-28">
                <!-- Grid Roads -->
                <line x1="20" y1="85" x2="300" y2="85" stroke="#334155" stroke-width="6"/>
                <line x1="20" y1="25" x2="300" y2="25" stroke="#334155" stroke-width="6"/>
                <line x1="90" y1="15" x2="90" y2="95" stroke="#334155" stroke-width="6"/>
                <line x1="190" y1="15" x2="190" y2="95" stroke="#334155" stroke-width="6"/>
                <line x1="270" y1="15" x2="270" y2="95" stroke="#334155" stroke-width="6"/>
                <!-- Road Names -->
                <text x="30" y="80" font-size="6" fill="#64748b">Park Ave</text>
                <text x="95" y="55" font-size="6" fill="#64748b">Rose St</text>
                <text x="120" y="20" font-size="6" fill="#64748b">Market Rd</text>
                <!-- Stops -->
                <circle cx="20" cy="85" r="4" fill="#64748b"/>
                <text x="20" y="97" text-anchor="middle" font-size="6" fill="#94a3b8">Depot</text>
                <circle cx="90" cy="25" r="4" fill="#38bdf8"/>
                <text x="90" y="15" text-anchor="middle" font-size="6" fill="#38bdf8" font-weight="bold">Stop 1</text>
                <circle cx="190" cy="25" r="4" fill="#10b981"/>
                <text x="190" y="15" text-anchor="middle" font-size="6" fill="#10b981" font-weight="bold">Stop 2</text>
                <circle cx="190" cy="85" r="4" fill="#f59e0b"/>
                <text x="190" y="97" text-anchor="middle" font-size="6" fill="#f59e0b" font-weight="bold">Stop 3</text>
                <circle cx="290" cy="85" r="4" fill="#f43f5e"/>
                <text x="290" y="97" text-anchor="middle" font-size="6" fill="#f43f5e" font-weight="bold">Zoo Highway</text>
                <!-- Bus Avatar -->
                <g id="sim7_bus" transform="translate(20, 85)">
                    <rect x="-8" y="-5" width="16" height="10" rx="2" fill="#eab308" stroke="#ffffff" stroke-width="1"/>
                </g>
            </svg>
            <div id="sim7_log" class="text-center font-mono text-[10px] text-amber-300 mt-1">Bus ready at Depot. Click Next to depart!</div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">📏 Manhattan Grid Distance Optimizer</span>
                <span id="sim8_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Minimal: 7 Blocks</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select alternative routes between corner A (Home) and corner B (School):</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim8SelectRoute('r1')" id="sim8_btn_r1" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold">Route 1 (L-Shape)</button>
                <button onclick="sim8SelectRoute('r2')" id="sim8_btn_r2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Route 2 (Inverted L)</button>
                <button onclick="sim8SelectRoute('r3')" id="sim8_btn_r3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Route 3 (Zig-Zag)</button>
                <button onclick="sim8SelectRoute('r4')" id="sim8_btn_r4" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Route 4 (Detour)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim8_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- 3x4 Grid Blocks -->
                    <g stroke="#334155" stroke-width="1">
                        <line x1="20" y1="20" x2="140" y2="20"/>
                        <line x1="20" y1="50" x2="140" y2="50"/>
                        <line x1="20" y1="80" x2="140" y2="80"/>
                        <line x1="20" y1="110" x2="140" y2="110"/>
                        <line x1="20" y1="20" x2="20" y2="110"/>
                        <line x1="60" y1="20" x2="60" y2="110"/>
                        <line x1="100" y1="20" x2="100" y2="110"/>
                        <line x1="140" y1="20" x2="140" y2="110"/>
                    </g>
                    <!-- Home & School Markers -->
                    <circle cx="20" cy="110" r="4" fill="#10b981"/>
                    <text x="20" y="122" text-anchor="middle" font-size="6" fill="#10b981" font-weight="bold">Home (A)</text>
                    <circle cx="140" cy="20" r="4" fill="#f59e0b"/>
                    <text x="140" y="14" text-anchor="middle" font-size="6" fill="#f59e0b" font-weight="bold">School (B)</text>
                    <!-- Dynamic Path Overlay -->
                    <path id="sim8_path" d="M 20 110 L 140 110 L 140 20" fill="none" stroke="#6366f1" stroke-width="3" stroke-linecap="round"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-indigo-300 font-bold block mb-1" id="sim8_route_title">Route 1: 3 East + 4 North</span>
                    <div id="sim8_dist_calc" class="text-emerald-400 font-bold">Total Distance = 7 Blocks</div>
                    <div id="sim8_efficiency" class="text-[10px] text-slate-400 mt-1">Minimal Manhattan grid distance.</div>
                </div>
            </div>
        </div>
    </div>
    """
}

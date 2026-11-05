# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Chapter 14: Maps and Locations"""

sims_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚇 Delhi Metro Schematic Transit Map</span>
                <span id="sim9_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Network Overview</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Explore color-coded transit lines and interchange transfer hubs across the capital:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim9FilterLine('all')" id="sim9_btn_all" class="px-2.5 py-1 rounded bg-amber-600 text-white font-bold transition">All Lines</button>
                <button onclick="sim9FilterLine('yellow')" id="sim9_btn_yellow" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-yellow-300 transition">Yellow (N-S)</button>
                <button onclick="sim9FilterLine('blue')" id="sim9_btn_blue" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-blue-300 transition">Blue (E-W)</button>
                <button onclick="sim9FilterLine('red')" id="sim9_btn_red" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 transition">Red Line</button>
                <button onclick="sim9FilterLine('hubs')" id="sim9_btn_hubs" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 transition">Interchanges 🔄</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim9_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Grid background -->
                    <defs>
                        <pattern id="sim9_grid" width="20" height="20" patternUnits="userSpaceOnUse">
                            <line x1="0" y1="0" x2="20" y2="0" stroke="#334155" stroke-width="0.5" stroke-opacity="0.3"/>
                            <line x1="0" y1="0" x2="0" y2="20" stroke="#334155" stroke-width="0.5" stroke-opacity="0.3"/>
                        </pattern>
                    </defs>
                    <rect width="200" height="160" fill="url(#sim9_grid)"/>

                    <!-- Compass -->
                    <g transform="translate(180, 20)">
                        <circle cx="0" cy="0" r="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                        <line x1="0" y1="-8" x2="0" y2="8" stroke="#38bdf8" stroke-width="1.5"/>
                        <line x1="-8" y1="0" x2="8" y2="0" stroke="#64748b" stroke-width="1"/>
                        <text x="0" y="-9" text-anchor="middle" font-size="6" fill="#38bdf8" font-weight="bold">N</text>
                    </g>

                    <!-- Red Line (East-West North) -->
                    <path id="sim9_line_red" d="M 20 40 L 80 40 L 160 30 L 185 30" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
                    <!-- Yellow Line (North-South) -->
                    <path id="sim9_line_yellow" d="M 80 20 L 80 40 L 95 80 L 95 145" fill="none" stroke="#eab308" stroke-width="3" stroke-linecap="round"/>
                    <!-- Blue Line (East-West Center) -->
                    <path id="sim9_line_blue" d="M 20 95 L 60 95 L 95 80 L 140 80 L 185 95" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
                    <!-- Violet Line -->
                    <path id="sim9_line_violet" d="M 80 40 L 115 65 L 140 80 L 140 145" fill="none" stroke="#8b5cf6" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="3,1"/>

                    <!-- Interchange Hub: Kashmere Gate (Red + Yellow) -->
                    <g id="sim9_hub_kg">
                        <circle cx="80" cy="40" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
                        <text x="80" y="34" text-anchor="middle" font-size="6.5" fill="#f8fafc" font-weight="bold">Kashmere Gate</text>
                    </g>

                    <!-- Interchange Hub: Rajiv Chowk (Yellow + Blue) -->
                    <g id="sim9_hub_rc">
                        <circle cx="95" cy="80" r="6" fill="#ffffff" stroke="#e11d48" stroke-width="2"/>
                        <circle cx="95" cy="80" r="3" fill="#e11d48"/>
                        <text x="95" y="72" text-anchor="middle" font-size="7" fill="#facc15" font-weight="bold">Rajiv Chowk</text>
                    </g>

                    <!-- Interchange Hub: Mandi House (Blue + Violet) -->
                    <g id="sim9_hub_mh">
                        <circle cx="140" cy="80" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
                        <text x="140" y="73" text-anchor="middle" font-size="6" fill="#f8fafc" font-weight="bold">Mandi House</text>
                    </g>

                    <!-- Station: Qutb Minar (South Yellow) -->
                    <circle cx="95" cy="135" r="3.5" fill="#eab308" stroke="#ffffff" stroke-width="1"/>
                    <text x="102" y="138" font-size="6" fill="#fef08a">Qutb Minar</text>

                    <!-- Station: Supreme Court (Blue Line) -->
                    <circle cx="160" cy="86" r="3.5" fill="#3b82f6" stroke="#ffffff" stroke-width="1"/>
                    <text x="160" y="98" text-anchor="middle" font-size="6" fill="#93c5fd">Supreme Court</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim9_info_title" class="text-amber-400 font-bold block mb-1">Delhi Metro Network Map</span>
                    <div id="sim9_info_desc" class="text-slate-300 text-[10.5px]">Schematic maps use straight 90° and 45° angle lines rather than realistic curved geography for instant readability.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between items-center text-[10px]">
                        <span class="text-slate-400">Selected Line / Hub:</span>
                        <span id="sim9_status" class="text-emerald-400 font-bold">All 4 Lines Visible</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-sky-400">⚡ Metro Route Optimizer: Qutb Minar ➔ Supreme Court</span>
                <span id="sim10_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Select Route</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare Route A (direct via Rajiv Chowk) versus Route B (multiple transfers):</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim10SelectRoute('A')" id="sim10_btn_a" class="flex-1 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold transition">Route A (Rajiv Chowk)</button>
                <button onclick="sim10SelectRoute('B')" id="sim10_btn_b" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Route B (Double Transfer)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim10_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Metro Route Path Background -->
                    <path d="M 60 140 L 60 40 L 160 40" fill="none" stroke="#334155" stroke-width="4" stroke-linecap="round"/>
                    
                    <!-- Route A Highlight -->
                    <path id="sim10_path_a" d="M 60 140 L 60 40 L 160 40" fill="none" stroke="#eab308" stroke-width="3" stroke-linecap="round" opacity="0.2"/>
                    <path id="sim10_path_a2" d="M 60 40 L 160 40" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round" opacity="0.2"/>
                    
                    <!-- Route B Path Alternate (via Hauz Khas + Mandi House) -->
                    <path id="sim10_path_b" d="M 60 140 L 60 100 L 120 100 L 140 50 L 160 40" fill="none" stroke="#ec4899" stroke-width="3" stroke-linecap="round" opacity="0.2"/>

                    <!-- Start: Qutb Minar -->
                    <circle cx="60" cy="140" r="5" fill="#eab308" stroke="#ffffff" stroke-width="1.5"/>
                    <text x="60" y="153" text-anchor="middle" font-size="7" fill="#fef08a" font-weight="bold">Qutb Minar</text>

                    <!-- Rajiv Chowk Transfer -->
                    <circle cx="60" cy="40" r="6" fill="#ffffff" stroke="#e11d48" stroke-width="2"/>
                    <text x="60" y="30" text-anchor="middle" font-size="7" fill="#f8fafc" font-weight="bold">Rajiv Chowk (Transfer)</text>

                    <!-- Destination: Supreme Court -->
                    <circle cx="160" cy="40" r="5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5"/>
                    <text x="160" y="30" text-anchor="middle" font-size="7" fill="#93c5fd" font-weight="bold">Supreme Court</text>

                    <!-- Moving Train Marker -->
                    <circle id="sim10_train" cx="60" cy="140" r="4.5" fill="#22c55e" stroke="#ffffff" stroke-width="1"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim10_route_title" class="text-sky-300 font-bold block mb-1">Route A: Optimal 1-Interchange</span>
                    <div id="sim10_breakdown" class="text-[10px] text-slate-300 space-y-1">
                        <div>• Yellow Line: Qutb Minar ➔ Rajiv Chowk (14 stops)</div>
                        <div>• Interchange 1: Switch at Rajiv Chowk to Blue Line</div>
                        <div>• Blue Line: Rajiv Chowk ➔ Supreme Court (2 stops)</div>
                    </div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center text-[10.5px]">
                    <span class="text-slate-400">Stops & Transfers:</span>
                    <span id="sim10_metrics" class="text-emerald-400 font-bold">16 Stops | 1 Transfer</span>
                </div>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🏫 School Map Symbols & Standard Legend</span>
                <span id="sim11_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Click Legend Item</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click any symbol in the legend palette to highlight and inspect its map location:</p>
            <div class="flex flex-wrap gap-1 mb-2">
                <button onclick="sim11Highlight('building')" id="sim11_btn_building" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold">🏢 School</button>
                <button onclick="sim11Highlight('gate')" id="sim11_btn_gate" class="px-2 py-1 rounded bg-slate-800 text-amber-300">🚪 Main Gate</button>
                <button onclick="sim11Highlight('tank')" id="sim11_btn_tank" class="px-2 py-1 rounded bg-slate-800 text-cyan-300">💧 Water Tank</button>
                <button onclick="sim11Highlight('garden')" id="sim11_btn_garden" class="px-2 py-1 rounded bg-slate-800 text-emerald-300">🌳 Garden</button>
                <button onclick="sim11Highlight('bench')" id="sim11_btn_bench" class="px-2 py-1 rounded bg-slate-800 text-purple-300">🪑 Benches</button>
                <button onclick="sim11Highlight('all')" id="sim11_btn_all" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Show All</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim11_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Boundary Wall -->
                    <rect x="15" y="15" width="170" height="130" fill="#0f172a" stroke="#64748b" stroke-width="2" stroke-dasharray="3,2"/>
                    <text x="100" y="12" text-anchor="middle" font-size="6" fill="#94a3b8">Outer Boundary Wall</text>

                    <!-- School Main Building -->
                    <rect id="sim11_sym_building" x="30" y="30" width="75" height="45" rx="3" fill="#6366f1" stroke="#818cf8" stroke-width="1.5"/>
                    <text x="67" y="55" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Main Building</text>

                    <!-- Main Gate (South) -->
                    <g id="sim11_sym_gate" transform="translate(100, 145)">
                        <rect x="-15" y="-5" width="30" height="10" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                        <text x="0" y="2" text-anchor="middle" font-size="6" fill="#0f172a" font-weight="bold">GATE</text>
                    </g>

                    <!-- Water Tank (North-East) -->
                    <g id="sim11_sym_tank" transform="translate(150, 45)">
                        <circle cx="0" cy="0" r="12" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                        <text x="0" y="2" text-anchor="middle" font-size="6" fill="#ffffff" font-weight="bold">TANK</text>
                    </g>

                    <!-- School Garden (South-West) -->
                    <g id="sim11_sym_garden" transform="translate(45, 110)">
                        <rect x="-20" y="-18" width="40" height="36" rx="4" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
                        <text x="0" y="-3" text-anchor="middle" font-size="6.5" fill="#ffffff" font-weight="bold">Garden</text>
                        <circle cx="-8" cy="8" r="4" fill="#22c55e"/>
                        <circle cx="8" cy="8" r="4" fill="#22c55e"/>
                    </g>

                    <!-- Park Benches -->
                    <g id="sim11_sym_bench" transform="translate(150, 110)">
                        <rect x="-15" y="-6" width="30" height="6" fill="#a855f7" stroke="#c084fc" stroke-width="1"/>
                        <rect x="-15" y="4" width="30" height="6" fill="#a855f7" stroke="#c084fc" stroke-width="1"/>
                        <text x="0" y="1" text-anchor="middle" font-size="5" fill="#ffffff">Benches</text>
                    </g>

                    <!-- Walkway Path -->
                    <path d="M 100 140 L 100 95 L 67 75" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="2,2"/>
                    <path d="M 100 95 L 140 95 L 150 60" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="2,2"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim11_legend_name" class="text-emerald-400 font-bold block mb-1">Standardized Map Legend</span>
                    <div id="sim11_legend_desc" class="text-[10px] text-slate-300">A map key / legend gives fixed, universally understood symbols so any visitor can read the layout immediately.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px]">
                    <span class="text-slate-400">Selected Feature:</span>
                    <span id="sim11_feat_stat" class="text-amber-300 font-bold ml-1">Main School Building (Purple)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧭 Island Treasure Hunt Navigation</span>
                <span id="sim12_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Step 0 of 3</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Follow the parchment bearings and pace counts to discover the buried treasure:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim12NextStep()" id="sim12_step_btn" class="flex-1 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Walk Step 1 (East 30 Paces) ➔</button>
                <button onclick="sim12Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim12_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Compass Rose -->
                    <g transform="translate(175, 25)">
                        <circle cx="0" cy="0" r="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                        <line x1="0" y1="-10" x2="0" y2="10" stroke="#ef4444" stroke-width="1.5"/>
                        <line x1="-10" y1="0" x2="10" y2="0" stroke="#64748b" stroke-width="1"/>
                        <text x="0" y="-11" text-anchor="middle" font-size="6" fill="#ef4444" font-weight="bold">N</text>
                    </g>

                    <!-- Trail Lines -->
                    <line id="sim12_line1" x1="40" y1="130" x2="130" y2="130" stroke="#eab308" stroke-width="2.5" stroke-dasharray="3,2" opacity="0.2"/>
                    <line id="sim12_line2" x1="130" y1="130" x2="130" y2="50" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,2" opacity="0.2"/>
                    <line id="sim12_line3" x1="130" y1="50" x2="70" y2="50" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="3,2" opacity="0.2"/>

                    <!-- Start: Banyan Tree -->
                    <circle cx="40" cy="130" r="5" fill="#15803d" stroke="#ffffff" stroke-width="1.5"/>
                    <text x="40" y="145" text-anchor="middle" font-size="6.5" fill="#86efac" font-weight="bold">Banyan Tree</text>

                    <!-- Landmark 1: Stone Well -->
                    <circle cx="130" cy="130" r="4.5" fill="#64748b" stroke="#ffffff" stroke-width="1"/>
                    <text x="130" y="145" text-anchor="middle" font-size="6" fill="#cbd5e1">Old Well</text>

                    <!-- Landmark 2: Sun Dial -->
                    <circle cx="130" cy="50" r="4.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                    <text x="130" y="42" text-anchor="middle" font-size="6" fill="#fde68a">Sun Dial</text>

                    <!-- Landmark 3: Buried Chest -->
                    <g id="sim12_chest" transform="translate(70, 50)" opacity="0.3">
                        <rect x="-7" y="-5" width="14" height="10" rx="1.5" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
                        <circle cx="0" cy="0" r="1.5" fill="#fef08a"/>
                        <text x="0" y="14" text-anchor="middle" font-size="6" fill="#fbbf24" font-weight="bold">Treasure!</text>
                    </g>

                    <!-- Explorer Marker -->
                    <circle id="sim12_marker" cx="40" cy="130" r="4" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim12_clue_title" class="text-amber-400 font-bold block mb-1">Clue 1: Departure</span>
                    <div id="sim12_clue_desc" class="text-[10px] text-slate-300">Face the rising Sun and walk 30 paces East from the Great Banyan Tree to reach the Old Stone Well.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center text-[10.5px]">
                    <span class="text-slate-400">Total Paces Walked:</span>
                    <span id="sim12_paces" class="text-emerald-400 font-bold">0 Paces</span>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-orange-400">🐜 Anthill Grid Crawling Lab (1 cm Grid)</span>
                <span id="sim13_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500/20 text-orange-300 border border-orange-500/30">Target: Laddoo</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Send the worker ant crawling along the 1 cm grid lines to gather food items:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim13SelectFood('laddoo')" id="sim13_btn_laddoo" class="px-2.5 py-1 rounded bg-orange-600 text-white font-bold transition">Laddoo (2, 3)</button>
                <button onclick="sim13SelectFood('bread')" id="sim13_btn_bread" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 transition">Bread (5, 4)</button>
                <button onclick="sim13SelectFood('sugar')" id="sim13_btn_sugar" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 transition">Sugar (6, 5)</button>
                <button onclick="sim13SelectFood('apple')" id="sim13_btn_apple" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 transition">Apple (1, 5)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim13_svg" viewBox="0 0 180 160" class="w-48 h-40">
                    <!-- 1 cm Grid (each unit = 20px) Origin at (20, 140) -->
                    <defs>
                        <pattern id="sim13_cmgrid" width="20" height="20" patternUnits="userSpaceOnUse">
                            <rect width="20" height="20" fill="none" stroke="#334155" stroke-width="0.8"/>
                        </pattern>
                    </defs>
                    <rect x="20" y="20" width="140" height="120" fill="url(#sim13_cmgrid)"/>
                    
                    <!-- Axes -->
                    <line x1="20" y1="140" x2="165" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="20" y1="140" x2="20" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                    <text x="165" y="148" font-size="7" fill="#94a3b8">East (cm)</text>
                    <text x="20" y="12" font-size="7" fill="#94a3b8">North (cm)</text>

                    <!-- Axis tick labels -->
                    <text x="20" y="150" font-size="6" fill="#64748b" text-anchor="middle">0</text>
                    <text x="40" y="150" font-size="6" fill="#64748b" text-anchor="middle">1</text>
                    <text x="60" y="150" font-size="6" fill="#64748b" text-anchor="middle">2</text>
                    <text x="80" y="150" font-size="6" fill="#64748b" text-anchor="middle">3</text>
                    <text x="100" y="150" font-size="6" fill="#64748b" text-anchor="middle">4</text>
                    <text x="120" y="150" font-size="6" fill="#64748b" text-anchor="middle">5</text>
                    <text x="140" y="150" font-size="6" fill="#64748b" text-anchor="middle">6</text>

                    <text x="12" y="123" font-size="6" fill="#64748b" text-anchor="middle">1</text>
                    <text x="12" y="103" font-size="6" fill="#64748b" text-anchor="middle">2</text>
                    <text x="12" y="83" font-size="6" fill="#64748b" text-anchor="middle">3</text>
                    <text x="12" y="63" font-size="6" fill="#64748b" text-anchor="middle">4</text>
                    <text x="12" y="43" font-size="6" fill="#64748b" text-anchor="middle">5</text>
                    <text x="12" y="23" font-size="6" fill="#64748b" text-anchor="middle">6</text>

                    <!-- Anthill Origin (0,0) -> SVG (20, 140) -->
                    <circle cx="20" cy="140" r="5" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
                    <text x="32" y="136" font-size="6.5" fill="#fcd34d" font-weight="bold">Anthill (0,0)</text>

                    <!-- Food Items -->
                    <!-- Laddoo at (2, 3) -> (60, 80) -->
                    <circle cx="60" cy="80" r="4" fill="#f59e0b"/>
                    <!-- Bread at (5, 4) -> (120, 60) -->
                    <rect x="116" y="56" width="8" height="8" rx="1.5" fill="#d97706"/>
                    <!-- Sugar at (6, 5) -> (140, 40) -->
                    <rect x="136" y="36" width="8" height="8" fill="#e2e8f0"/>
                    <!-- Apple at (1, 5) -> (40, 40) -->
                    <circle cx="40" cy="40" r="4" fill="#ef4444"/>

                    <!-- Crawling Path Active -->
                    <path id="sim13_path" d="M 20 140 L 60 140 L 60 80" fill="none" stroke="#f97316" stroke-width="2.5" stroke-linecap="round"/>

                    <!-- Ant Marker -->
                    <circle id="sim13_ant" cx="60" cy="80" r="3.5" fill="#f97316" stroke="#ffffff" stroke-width="1"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim13_target_title" class="text-orange-400 font-bold block mb-1">Target: Sweet Laddoo</span>
                    <div id="sim13_calc_steps" class="text-[10px] text-slate-300 space-y-1">
                        <div>• Horizontal East: 2 grid units = 2 cm</div>
                        <div>• Vertical North: 3 grid units = 3 cm</div>
                        <div>• Coordinates: (2, 3)</div>
                    </div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center text-[10.5px]">
                    <span class="text-slate-400">Total Crawl Distance:</span>
                    <span id="sim13_total_dist" class="text-emerald-400 font-bold">2 + 3 = 5 cm</span>
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">🔍 Shortest Grid Path & Backtracking Avoidance</span>
                <span id="sim14_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Target: Bread (5, 4)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare minimal monotonic paths versus wasteful backtracking routes on grid lines:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim14ShowRoute('EN')" id="sim14_btn_en" class="px-2.5 py-1 rounded bg-teal-600 text-white font-bold transition">East ➔ North (9 cm)</button>
                <button onclick="sim14ShowRoute('NE')" id="sim14_btn_ne" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-sky-300 transition">North ➔ East (9 cm)</button>
                <button onclick="sim14ShowRoute('stair')" id="sim14_btn_stair" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 transition">Staircase (9 cm)</button>
                <button onclick="sim14ShowRoute('back')" id="sim14_btn_back" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 transition">Backtracking ⚠️ (13 cm)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim14_svg" viewBox="0 0 180 160" class="w-48 h-40">
                    <!-- Grid background -->
                    <defs>
                        <pattern id="sim14_cmgrid" width="20" height="20" patternUnits="userSpaceOnUse">
                            <rect width="20" height="20" fill="none" stroke="#334155" stroke-width="0.8"/>
                        </pattern>
                    </defs>
                    <rect x="20" y="20" width="140" height="120" fill="url(#sim14_cmgrid)"/>
                    <line x1="20" y1="140" x2="165" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="20" y1="140" x2="20" y2="15" stroke="#94a3b8" stroke-width="1.5"/>

                    <!-- Start & Destination Markers -->
                    <circle cx="20" cy="140" r="4.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                    <text x="25" y="152" font-size="6.5" fill="#fcd34d" font-weight="bold">Start (0,0)</text>

                    <!-- Bread Destination at (5, 4) -> SVG (120, 60) -->
                    <rect x="115" y="55" width="10" height="10" rx="2" fill="#d97706" stroke="#ffffff" stroke-width="1"/>
                    <text x="120" y="50" text-anchor="middle" font-size="6.5" fill="#fed7aa" font-weight="bold">Bread (5,4)</text>

                    <!-- Route Paths -->
                    <path id="sim14_route_en" d="M 20 140 L 120 140 L 120 60" fill="none" stroke="#14b8a6" stroke-width="3" stroke-linecap="round"/>
                    <path id="sim14_route_ne" d="M 20 140 L 20 60 L 120 60" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" opacity="0.2"/>
                    <path id="sim14_route_stair" d="M 20 140 L 60 140 L 60 100 L 100 100 L 100 60 L 120 60" fill="none" stroke="#818cf8" stroke-width="3" stroke-linecap="round" opacity="0.2"/>
                    <path id="sim14_route_back" d="M 20 140 L 80 140 L 80 80 L 40 80 L 40 60 L 120 60" fill="none" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" opacity="0.2"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim14_route_name" class="text-teal-400 font-bold block mb-1">Route 1: 5 East + 4 North</span>
                    <div id="sim14_formula" class="text-[10px] text-slate-300">Total distance = 5 cm (East) + 4 cm (North) = 9 cm. Minimal shortest path.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center text-[10.5px]">
                    <span class="text-slate-400">Shortest Possible Distance:</span>
                    <span id="sim14_len_badge" class="text-emerald-400 font-bold">9 cm (Optimal)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-violet-400">📊 2D Coordinate Grid System Studio (12 × 12)</span>
                <span id="sim15_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-violet-500/20 text-violet-300 border border-violet-500/30">Active: (4, 7)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust sliders to observe the universal standard rule: <b>Horizontal (X) FIRST, Vertical (Y) SECOND</b>:</p>
            <div class="grid grid-cols-2 gap-3 mb-2">
                <div>
                    <label class="text-[10px] text-indigo-300 flex justify-between">
                        <span>Horizontal X (Columns / East):</span>
                        <span id="sim15_x_val" class="font-bold text-white">4</span>
                    </label>
                    <input type="range" id="sim15_slider_x" min="0" max="12" value="4" oninput="sim15Update()" class="w-full accent-indigo-500 cursor-pointer">
                </div>
                <div>
                    <label class="text-[10px] text-emerald-300 flex justify-between">
                        <span>Vertical Y (Rows / North):</span>
                        <span id="sim15_y_val" class="font-bold text-white">7</span>
                    </label>
                    <input type="range" id="sim15_slider_y" min="0" max="12" value="7" oninput="sim15Update()" class="w-full accent-emerald-500 cursor-pointer">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim15_svg" viewBox="0 0 160 160" class="w-44 h-40">
                    <!-- 12x12 Grid: 10px per unit, origin at (20, 140) -->
                    <defs>
                        <pattern id="sim15_grid12" width="10" height="10" patternUnits="userSpaceOnUse">
                            <rect width="10" height="10" fill="none" stroke="#334155" stroke-width="0.5"/>
                        </pattern>
                    </defs>
                    <rect x="20" y="20" width="120" height="120" fill="url(#sim15_grid12)"/>
                    <!-- Axes -->
                    <line x1="20" y1="140" x2="150" y2="140" stroke="#818cf8" stroke-width="1.5"/>
                    <line x1="20" y1="140" x2="20" y2="10" stroke="#34d399" stroke-width="1.5"/>
                    <text x="148" y="148" font-size="6" fill="#818cf8" font-weight="bold">X</text>
                    <text x="15" y="12" font-size="6" fill="#34d399" font-weight="bold">Y</text>

                    <!-- Dynamic Coordinate Projections -->
                    <!-- Vertical projection up from X axis -->
                    <line id="sim15_proj_x" x1="60" y1="140" x2="60" y2="70" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="2,2"/>
                    <!-- Horizontal projection right from Y axis -->
                    <line id="sim15_proj_y" x1="20" y1="70" x2="60" y2="70" stroke="#34d399" stroke-width="1.5" stroke-dasharray="2,2"/>

                    <!-- Coordinate Point -->
                    <circle id="sim15_pt" cx="60" cy="70" r="4.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-violet-300 font-bold block mb-1">Ordered Pair: (X, Y)</span>
                    <div id="sim15_pair_display" class="text-amber-300 font-bold text-base mb-1">(4, 7)</div>
                    <div id="sim15_pair_desc" class="text-[10px] text-slate-300">Walk 4 units right along the horizontal X-axis, then 7 units up along the vertical Y-axis.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px]">
                    <span class="text-slate-400">Coordinate Rule:</span>
                    <span class="text-emerald-400 font-bold ml-1">Always (Horizontal, Vertical)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🦁 Zoo Animal Coordinate Plotting Master</span>
                <span id="sim16_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Click Animal</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select an animal to plot its exact (X, Y) coordinate coordinates on the 12 × 12 zoo grid:</p>
            <div class="flex flex-wrap gap-1 mb-2">
                <button onclick="sim16Plot('panda')" id="sim16_btn_panda" class="px-2 py-1 rounded bg-emerald-600 text-white font-bold">🐼 Panda (1,1)</button>
                <button onclick="sim16Plot('tortoise')" id="sim16_btn_tortoise" class="px-2 py-1 rounded bg-slate-800 text-emerald-300">🐢 Tortoise (4,1)</button>
                <button onclick="sim16Plot('deer')" id="sim16_btn_deer" class="px-2 py-1 rounded bg-slate-800 text-amber-300">🦌 Deer (8,3)</button>
                <button onclick="sim16Plot('croc')" id="sim16_btn_croc" class="px-2 py-1 rounded bg-slate-800 text-cyan-300">🐊 Crocodile (7,6)</button>
                <button onclick="sim16Plot('lion')" id="sim16_btn_lion" class="px-2 py-1 rounded bg-slate-800 text-rose-300">🦁 Lion (3,10)</button>
                <button onclick="sim16Plot('elephant')" id="sim16_btn_elephant" class="px-2 py-1 rounded bg-slate-800 text-indigo-300">🐘 Elephant (11,11)</button>
                <button onclick="sim16Plot('all')" id="sim16_btn_all" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Show All</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim16_svg" viewBox="0 0 160 160" class="w-44 h-40">
                    <!-- 12x12 Grid: 10px per unit, origin at (20, 140) -->
                    <defs>
                        <pattern id="sim16_grid12" width="10" height="10" patternUnits="userSpaceOnUse">
                            <rect width="10" height="10" fill="none" stroke="#334155" stroke-width="0.5"/>
                        </pattern>
                    </defs>
                    <rect x="20" y="20" width="120" height="120" fill="url(#sim16_grid12)"/>
                    <line x1="20" y1="140" x2="150" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="20" y1="140" x2="20" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
                    <text x="145" y="148" font-size="6" fill="#94a3b8">East (X)</text>
                    <text x="12" y="12" font-size="6" fill="#94a3b8">North (Y)</text>

                    <!-- Guide Lines -->
                    <line id="sim16_line_x" x1="30" y1="140" x2="30" y2="130" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
                    <line id="sim16_line_y" x1="20" y1="130" x2="30" y2="130" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>

                    <!-- Animal Enclosures: 
                        Panda (1, 1) -> (30, 130)
                        Tortoise (4, 1) -> (60, 130)
                        Deer (8, 3) -> (100, 110)
                        Crocodile (7, 6) -> (90, 80)
                        Lion (3, 10) -> (50, 40)
                        Elephant (11, 11) -> (130, 30)
                    -->
                    <circle id="sim16_encl_panda" cx="30" cy="130" r="4.5" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
                    <circle id="sim16_encl_tortoise" cx="60" cy="130" r="4.5" fill="#10b981" stroke="#ffffff" stroke-width="1"/>
                    <circle id="sim16_encl_deer" cx="100" cy="110" r="4.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                    <circle id="sim16_encl_croc" cx="90" cy="80" r="4.5" fill="#06b6d4" stroke="#ffffff" stroke-width="1"/>
                    <circle id="sim16_encl_lion" cx="50" cy="40" r="4.5" fill="#f43f5e" stroke="#ffffff" stroke-width="1"/>
                    <circle id="sim16_encl_elephant" cx="130" cy="30" r="4.5" fill="#6366f1" stroke="#ffffff" stroke-width="1"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim16_animal_name" class="text-emerald-400 font-bold block mb-1">🐼 Panda Enclosure</span>
                    <div id="sim16_coord_display" class="text-amber-300 font-bold text-sm mb-1">Coordinates: (1, 1)</div>
                    <div id="sim16_plot_desc" class="text-[10px] text-slate-300">Located 1 unit East along the horizontal column and 1 unit North along the vertical row from the entrance.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px]">
                    <span class="text-slate-400">Position Status:</span>
                    <span id="sim16_status_text" class="text-emerald-400 font-bold ml-1">Panda Plotted at (1, 1)</span>
                </div>
            </div>
        </div>
    </div>
    """
}


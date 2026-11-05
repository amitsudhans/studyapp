"""
Class 6 Science Chapter 11: Nature's Treasures
16 Bespoke Interactive SVG/HTML Simulators
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Western Ghats Nature Treasury</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Bounty: Pristine Forest</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg id="sim1-svg" class="w-full h-full" viewBox="0 0 320 200">
                <defs>
                    <linearGradient id="sim1-sky" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stop-color="#0284c7" />
                        <stop offset="60%" stop-color="#38bdf8" />
                        <stop offset="100%" stop-color="#bae6fd" />
                    </linearGradient>
                </defs>
                <!-- Mountain Sky -->
                <rect x="0" y="0" width="320" height="130" fill="url(#sim1-sky)" />
                <!-- Sun -->
                <circle cx="260" cy="40" r="18" fill="#fbbf24" stroke="#f59e0b" stroke-width="2" />
                <!-- Western Ghats Mountain Silhouette -->
                <path d="M 0,130 Q 80,60 160,110 T 320,80 L 320,150 L 0,150 Z" fill="#15803d" opacity="0.8" />
                <path d="M 40,140 Q 140,80 240,130 L 320,120 L 320,170 L 0,170 Z" fill="#166534" />
                <!-- Crystal Stream -->
                <path d="M 120,150 Q 140,165 160,180 T 180,200 L 140,200 Q 130,185 110,165 Z" fill="#0284c7" />
                <!-- Soil Valley Floor -->
                <rect x="0" y="165" width="115" height="35" fill="#57534e" />
                <rect x="175" y="165" width="145" height="35" fill="#57534e" />
                <!-- Trees & Wildlife -->
                <path d="M 50,165 L 50,140 M 40,145 L 50,130 L 60,145 Z" stroke="#78350f" stroke-width="3" fill="#22c55e" />
                <path d="M 75,170 L 75,145 M 65,150 L 75,135 L 85,150 Z" stroke="#78350f" stroke-width="3" fill="#16a34a" />
                <path d="M 230,165 L 230,135 M 220,140 L 230,120 L 240,140 Z" stroke="#78350f" stroke-width="3" fill="#15803d" />

                <!-- Highlight Box Indicator -->
                <rect id="sim1-focus" x="10" y="10" width="150" height="30" rx="6" fill="#0f172a" fill-opacity="0.85" stroke="#334155" />
                <text id="sim1-focus-text" x="20" y="29" fill="#94a3b8" font-size="11" font-weight="bold">Gift: Pure Clean Air</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="inspectGift('air')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                💨 Air
            </button>
            <button onclick="inspectGift('water')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                💧 Water
            </button>
            <button onclick="inspectGift('soil')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🌱 Soil
            </button>
            <button onclick="inspectGift('sun')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                ☀️ Sun
            </button>
        </div>
        <div id="sim1-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click any gift to discover how the Western Ghats ecosystem naturally generates, purifies, and sustains that vital treasure.
        </div>
    </div>
    """,

    2: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 11.1: Breath Hold & Oxygen Saturation</span>
            <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Breathing Normal</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Human Torso & Lungs Silhouette -->
                <path d="M 120,40 Q 160,25 200,40 L 210,180 L 110,180 Z" fill="#1e293b" stroke="#334155" stroke-width="2" />
                <!-- Trachea (Windpipe) -->
                <line x1="160" y1="40" x2="160" y2="85" stroke="#94a3b8" stroke-width="4" stroke-linecap="round" />
                <!-- Left & Right Lungs -->
                <path id="sim2-lung-l" d="M 155,85 C 130,85 125,145 150,150 C 158,150 158,95 155,85 Z" fill="#f43f5e" opacity="0.8" style="transition: all 0.4s ease;" />
                <path id="sim2-lung-r" d="M 165,85 C 190,85 195,145 170,150 C 162,150 162,95 165,85 Z" fill="#f43f5e" opacity="0.8" style="transition: all 0.4s ease;" />

                <!-- O2 Gauge Meter -->
                <g transform="translate(250, 95)">
                    <rect x="-35" y="-55" width="70" height="110" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
                    <text x="0" y="-38" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">Blood O₂</text>
                    <!-- Mercury level bar -->
                    <rect x="-15" y="-25" width="30" height="70" rx="4" fill="#1e293b" />
                    <rect id="sim2-o2-bar" x="-15" y="-25" width="30" height="70" rx="4" fill="#38bdf8" style="transition: all 0.5s ease; transform-origin: 0 45px;" />
                    <text id="sim2-o2-val" x="0" y="35" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">99%</text>
                </g>

                <!-- Timer Indicator -->
                <text x="50" y="80" fill="#94a3b8" font-size="10" font-weight="bold">Hold Timer:</text>
                <text id="sim2-timer" x="50" y="110" fill="#f8fafc" font-size="22" font-weight="extrabold">0s</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button id="sim2-btn" onclick="toggleHoldBreath()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🫁 Hold Breath (Pinch Nostrils)
            </button>
            <button onclick="resetBreathing()" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                💨 Inhale Fresh Oxygen
            </button>
        </div>
        <div id="sim2-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click <strong>Hold Breath</strong>: blood oxygen saturation rapidly drops, triggering an overwhelming biological urge to breathe within 30-40 seconds!
        </div>
    </div>
    """,

    3: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Atmospheric Gas Mixture Chamber</span>
            <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Total Mixture (100%)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />
                
                <!-- Donut Pie Chart of Atmosphere -->
                <g transform="translate(110, 100)">
                    <!-- Nitrogen Slice (78% -> 280.8 deg) -->
                    <circle cx="0" cy="0" r="60" fill="none" stroke="#0284c7" stroke-width="26" stroke-dasharray="294 377" stroke-dashoffset="0" />
                    <!-- Oxygen Slice (21% -> 75.6 deg) -->
                    <circle cx="0" cy="0" r="60" fill="none" stroke="#22c55e" stroke-width="26" stroke-dasharray="79 377" stroke-dashoffset="-294" />
                    <!-- Argon & CO2 Slice (1% -> 3.6 deg) -->
                    <circle cx="0" cy="0" r="60" fill="none" stroke="#f59e0b" stroke-width="26" stroke-dasharray="4 377" stroke-dashoffset="-373" />
                    <text x="0" y="4" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Air</text>
                </g>

                <!-- Legend Cards -->
                <g transform="translate(210, 45)">
                    <!-- Nitrogen -->
                    <circle cx="5" cy="15" r="5" fill="#0284c7" />
                    <text x="16" y="19" fill="#38bdf8" font-size="11" font-weight="bold">Nitrogen 78%</text>
                    
                    <!-- Oxygen -->
                    <circle cx="5" cy="45" r="5" fill="#22c55e" />
                    <text x="16" y="49" fill="#4ade80" font-size="11" font-weight="bold">Oxygen 21%</text>
                    
                    <!-- Argon & CO2 -->
                    <circle cx="5" cy="75" r="5" fill="#f59e0b" />
                    <text x="16" y="79" fill="#fbbf24" font-size="11" font-weight="bold">Argon+CO₂ 1%</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="isolateGas('nitrogen')" class="p-1.5 rounded-lg bg-sky-950 border border-sky-500/50 text-[11px] font-bold text-sky-300">
                💨 N₂ (78%)
            </button>
            <button onclick="isolateGas('oxygen')" class="p-1.5 rounded-lg bg-emerald-950 border border-emerald-500/50 text-[11px] font-bold text-emerald-300">
                🫁 O₂ (21%)
            </button>
            <button onclick="isolateGas('co2')" class="p-1.5 rounded-lg bg-amber-950 border border-amber-500/50 text-[11px] font-bold text-amber-300">
                🌱 CO₂ (0.04%)
            </button>
        </div>
        <div id="sim3-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Nitrogen dilutes oxygen to prevent runaway fires and builds plant proteins; oxygen sustains respiration; carbon dioxide drives photosynthesis.
        </div>
    </div>
    """,

    4: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Windmill Turbine & Firki Kinetic Lab</span>
            <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Wind Speed: 15 km/h</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Wind Turbine Tower -->
                <path d="M 100,180 L 108,60 L 112,60 L 120,180 Z" fill="#64748b" />
                <circle cx="110" cy="60" r="7" fill="#cbd5e1" />
                
                <!-- Rotating Turbine Blades -->
                <g id="sim4-blades" style="transform-origin: 110px 60px; animation: spinTurbine 2s linear infinite;">
                    <path d="M 110,60 L 110,5 L 114,35 Z" fill="#f8fafc" />
                    <path d="M 110,60 L 158,88 L 132,74 Z" fill="#f8fafc" />
                    <path d="M 110,60 L 62,88 L 88,74 Z" fill="#f8fafc" />
                </g>

                <!-- Paper Firki (Pinwheel) Handheld -->
                <g transform="translate(230, 110)">
                    <line x1="0" y1="20" x2="0" y2="70" stroke="#b45309" stroke-width="3" />
                    <circle cx="0" cy="20" r="4" fill="#ef4444" />
                    <!-- Rotating Firki Blades -->
                    <g id="sim4-firki" style="transform-origin: 0px 20px; animation: spinTurbine 1s linear infinite;">
                        <path d="M 0,20 Q -15,-5 0,-15 Q 15,-5 0,20" fill="#ec4899" />
                        <path d="M 0,20 Q 25,5 35,20 Q 25,35 0,20" fill="#3b82f6" />
                        <path d="M 0,20 Q 15,45 0,55 Q -15,45 0,20" fill="#eab308" />
                        <path d="M 0,20 Q -25,35 -35,20 Q -25,5 0,20" fill="#10b981" />
                    </g>
                </g>

                <!-- Wattage Display -->
                <rect x="15" y="15" width="130" height="26" rx="6" fill="#0f172a" stroke="#334155" />
                <text id="sim4-power" x="25" y="32" fill="#4ade80" font-size="11" font-weight="bold">Output: 450 kW</text>
            </svg>
        </div>
        <div class="flex items-center space-x-3">
            <span class="text-xs text-slate-400 font-bold shrink-0">Breeze Speed:</span>
            <input id="sim4-slider" type="range" min="0" max="60" value="15" oninput="setWindSpeed(this.value)" class="w-full accent-indigo-500" />
            <span id="sim4-speed-val" class="text-xs font-bold text-indigo-400 shrink-0">15 km/h</span>
        </div>
        <div id="sim4-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Moving air pushes against angled aerodynamic blades, converting kinetic energy into rotational motion to generate clean electricity.
        </div>
    </div>
    <style>
        @keyframes spinTurbine {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
    """,

    5: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">The 10-Liter Global Water Bucket</span>
            <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Total Planetary Water</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030d1a" />
                
                <!-- 1. The 10-Liter Bucket (Saline Oceans: 97.5%) -->
                <g id="sim5-bucket" transform="translate(60, 40)">
                    <path d="M 0,20 L 10,130 Q 10,140 20,140 L 70,140 Q 80,140 80,130 L 90,20 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                    <text x="45" y="80" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">10 Liters</text>
                    <text x="45" y="95" fill="#bae6fd" font-size="9" text-anchor="middle">Oceans (97.5%)</text>
                    <text x="45" y="160" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">All Earth Water</text>
                </g>

                <!-- Flow Arrow -->
                <path d="M 155,100 L 180,100 M 174,95 L 180,100 L 174,105" stroke="#64748b" stroke-width="2.5" />

                <!-- 2. The Tea Cup (Total Freshwater: 2.5% = 250 mL) -->
                <g id="sim5-cup" transform="translate(195, 75)">
                    <path d="M 5,20 L 10,65 Q 10,75 20,75 L 45,75 Q 55,75 55,65 L 60,20 Z" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
                    <!-- Handle -->
                    <path d="M 60,30 Q 75,45 60,60" fill="none" stroke="#38bdf8" stroke-width="2" />
                    <text x="32" y="45" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">250 mL</text>
                    <text x="32" y="95" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Freshwater (2.5%)</text>
                </g>

                <!-- 3. The Accessible Drop (< 1 mL) -->
                <g id="sim5-drop" transform="translate(280, 105)">
                    <path d="M 12,0 C 0,16 0,26 12,26 C 24,26 24,16 12,0 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <text x="12" y="45" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">1 Drop!</text>
                    <text x="12" y="58" fill="#94a3b8" font-size="8" text-anchor="middle">Rivers & Lakes</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="highlightWaterFraction('all')" class="p-1.5 rounded-lg bg-sky-950 border border-sky-500/50 text-[11px] font-bold text-sky-300">
                🌊 10L Bucket (Ocean)
            </button>
            <button onclick="highlightWaterFraction('fresh')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                ☕ 250mL Cup (Fresh)
            </button>
            <button onclick="highlightWaterFraction('drop')" class="p-1.5 rounded-lg bg-amber-950 border border-amber-500/50 text-[11px] font-bold text-amber-300">
                💧 1 Drop (Usable)
            </button>
        </div>
        <div id="sim5-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            If all Earth's water filled a 10L bucket, accessible freshwater in lakes and rivers would equal barely a single drop!
        </div>
    </div>
    """,

    6: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 11.3: Water Waste & Conservation Audit</span>
            <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Tap Leaking: Wasting Water</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Water Pipe & Tap -->
                <rect x="40" y="60" width="80" height="18" fill="#64748b" />
                <path d="M 120,60 L 150,60 L 150,90 L 135,90 L 135,78 L 120,78 Z" fill="#94a3b8" />
                <!-- Tap Knob Valve -->
                <rect id="sim6-valve" x="138" y="42" width="9" height="18" fill="#ef4444" rx="2" style="transition: transform 0.4s ease; transform-origin: 142px 51px;" />
                <rect x="130" y="38" width="25" height="6" fill="#ef4444" rx="2" />

                <!-- Water Stream or Drops -->
                <g id="sim6-water-stream">
                    <!-- Falling Droplets -->
                    <circle id="sim6-d1" cx="142" cy="110" r="4" fill="#38bdf8" />
                    <circle id="sim6-d2" cx="142" cy="135" r="4" fill="#38bdf8" />
                    <circle id="sim6-d3" cx="142" cy="160" r="4" fill="#38bdf8" />
                </g>

                <!-- Wash Basin / Bucket -->
                <path d="M 110,165 L 120,195 L 165,195 L 175,165 Z" fill="#334155" stroke="#475569" stroke-width="2" />

                <!-- Wastage Statistics Panel -->
                <g transform="translate(195, 45)">
                    <rect x="0" y="0" width="115" height="100" rx="8" fill="#0f172a" stroke="#334155" />
                    <text x="10" y="22" fill="#94a3b8" font-size="9" font-weight="bold">Water Wasted:</text>
                    <text id="sim6-liters" x="10" y="48" fill="#f43f5e" font-size="20" font-weight="extrabold">30 L/day</text>
                    <text id="sim6-cost" x="10" y="70" fill="#cbd5e1" font-size="10">10,950 L / year</text>
                    <text id="sim6-action" x="10" y="88" fill="#f59e0b" font-size="9" font-weight="bold">Fix washer now!</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="repairTap(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🔧 Repair Leaky Washer (Save Water)
            </button>
            <button onclick="repairTap(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🚰 Loosen Tap (Leak Active)
            </button>
        </div>
        <div id="sim6-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            A faucet dripping once per second squanders over 30 liters daily. Fixing leaky washers saves over 10,000 liters every year!
        </div>
    </div>
    """,

    7: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Traditional Stepwell (Bawadi / Vav) Reservoir</span>
            <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Season: Monsoon Refill</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Ground Surface -->
                <rect x="0" y="0" width="320" height="30" fill="#78350f" />
                
                <!-- Subterranean Excavation Cavity -->
                <path d="M 40,30 L 100,180 L 220,180 L 280,30 Z" fill="#1c1917" stroke="#44403c" stroke-width="2" />
                
                <!-- Left Descending Steps -->
                <path d="M 40,30 L 70,30 L 70,60 L 95,60 L 95,90 L 115,90 L 115,120 L 130,120 L 130,150 L 140,150 L 140,180" stroke="#78716c" stroke-width="2" fill="none" />
                <!-- Right Descending Steps -->
                <path d="M 280,30 L 250,30 L 250,60 L 225,60 L 225,90 L 205,90 L 205,120 L 190,120 L 190,150 L 180,150 L 180,180" stroke="#78716c" stroke-width="2" fill="none" />

                <!-- Water Reservoir Level inside Stepwell -->
                <rect id="sim7-water" x="100" y="100" width="120" height="80" fill="#0284c7" opacity="0.8" style="transition: all 0.6s ease;" />

                <!-- Raindrops Falling (Monsoon) -->
                <g id="sim7-rain" style="transition: opacity 0.5s ease; opacity: 1;">
                    <line x1="80" y1="5" x2="75" y2="25" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,4" />
                    <line x1="160" y1="5" x2="155" y2="25" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,4" />
                    <line x1="240" y1="5" x2="235" y2="25" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,4" />
                </g>

                <text x="160" y="195" fill="#cbd5e1" font-size="9" text-anchor="middle" font-weight="bold">Aquifer Recharge Base</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setStepwellSeason('monsoon')" class="p-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white shadow transition">
                🌧️ Monsoon Season (Full Recharge)
            </button>
            <button onclick="setStepwellSeason('summer')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ☀️ Peak Summer (Deep Storage)
            </button>
        </div>
        <div id="sim7-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Intricate stepwells (Bawadi & Vav) capture monsoon runoff, recharging groundwater and maintaining cool potable water throughout scorching dry summers.
        </div>
    </div>
    """,

    8: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">The Solar Engine Biosphere Driver</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Solar Drive: Maximum</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Sun Powerhouse -->
                <circle id="sim8-sun" cx="160" cy="40" r="26" fill="#f59e0b" stroke="#fde047" stroke-width="3" style="transition: all 0.5s ease;" />
                
                <!-- Solar Radiant Beams -->
                <g id="sim8-rays" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.8">
                    <line x1="135" y1="40" x2="60" y2="120" />
                    <line x1="160" y1="68" x2="160" y2="130" />
                    <line x1="185" y1="40" x2="260" y2="120" />
                </g>

                <!-- 1. Photosynthesis Zone Left -->
                <g transform="translate(30, 130)">
                    <path d="M 30,50 L 30,15 M 15,25 L 30,5 L 45,25 Z" fill="#22c55e" stroke="#15803d" stroke-width="1.5" />
                    <text x="30" y="62" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Photosynthesis</text>
                </g>

                <!-- 2. Water Evaporation Center -->
                <g transform="translate(130, 130)">
                    <path d="M 0,40 Q 30,30 60,40 L 60,55 L 0,55 Z" fill="#0284c7" />
                    <!-- Rising Vapour -->
                    <path d="M 15,35 Q 20,20 15,10 M 30,35 Q 35,20 30,10 M 45,35 Q 50,20 45,10" stroke="#38bdf8" stroke-width="1.5" fill="none" />
                    <text x="30" y="62" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Water Cycle</text>
                </g>

                <!-- 3. Wind Currents Right -->
                <g transform="translate(230, 130)">
                    <path d="M 0,25 Q 25,10 50,25 Q 25,40 0,25" fill="none" stroke="#a78bfa" stroke-width="2.5" />
                    <path d="M 10,35 Q 35,20 60,35" fill="none" stroke="#a78bfa" stroke-width="1.5" />
                    <text x="30" y="62" fill="#c4b5fd" font-size="9" font-weight="bold" text-anchor="middle">Wind & Weather</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleSolarEngine(true)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ☀️ Solar Engine Active (Life Thrives)
            </button>
            <button onclick="toggleSolarEngine(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🌑 Block Sun (Planetary Freeze)
            </button>
        </div>
        <div id="sim8-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            The Sun is Earth's primary thermodynamic engine, evaporating oceans for rain, driving atmospheric winds, and powering green photosynthesis.
        </div>
    </div>
    """,

    9: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Solar Photovoltaic Panel & Cooker Lab</span>
            <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Mode: Solar PV Panel</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Sun Light Source Top Left -->
                <circle cx="40" cy="35" r="16" fill="#f59e0b" />
                <path d="M 40,35 L 120,70" stroke="#fde047" stroke-width="1" stroke-dasharray="3,3" />

                <!-- 1. Photovoltaic Panel Assembly -->
                <g id="sim9-pv-group" style="transition: opacity 0.4s ease; opacity: 1;">
                    <!-- Angled Solar Panel Frame -->
                    <polygon points="90,110 200,60 220,130 110,180" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2" />
                    <!-- Grid Lines on Silicon -->
                    <line x1="145" y1="85" x2="165" y2="155" stroke="#93c5fd" stroke-width="1.5" />
                    <line x1="100" y1="145" x2="210" y2="95" stroke="#93c5fd" stroke-width="1.5" />
                    
                    <!-- Output Meter -->
                    <rect x="235" y="80" width="75" height="50" rx="6" fill="#0f172a" stroke="#334155" />
                    <text x="272" y="100" fill="#94a3b8" font-size="9" text-anchor="middle">Power Output</text>
                    <text id="sim9-watt" x="272" y="120" fill="#4ade80" font-size="14" font-weight="bold" text-anchor="middle">320 W</text>
                </g>

                <!-- 2. Solar Box Cooker (Hidden initially) -->
                <g id="sim9-cooker-group" style="transition: opacity 0.4s ease; opacity: 0;" transform="translate(100, 60)">
                    <rect x="0" y="20" width="120" height="80" fill="#1e293b" stroke="#475569" stroke-width="2" rx="4" />
                    <!-- Black Interior -->
                    <rect x="10" y="30" width="100" height="60" fill="#020617" />
                    <!-- Cooking Pots -->
                    <circle cx="35" cy="60" r="14" fill="#334155" stroke="#64748b" stroke-width="1.5" />
                    <circle cx="85" cy="60" r="14" fill="#334155" stroke="#64748b" stroke-width="1.5" />
                    <!-- Glass Lid -->
                    <rect x="5" y="25" width="110" height="70" fill="#38bdf8" opacity="0.25" stroke="#7dd3fc" stroke-width="1" />
                    <text x="60" y="15" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Internal Temp: 125°C</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setSolarTech('pv')" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                ⚡ Solar PV Panel (Electricity)
            </button>
            <button onclick="setSolarTech('cooker')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🍲 Solar Box Cooker (Thermal)
            </button>
        </div>
        <div id="sim9-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Solar panels generate clean electrical watts directly from photons; solar cookers trap thermal infrared heat under glass to cook meals with zero fuel.
        </div>
    </div>
    """,

    10: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Forest Canopy & Humus Recycling Lab</span>
            <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Zero-Waste Recycling Active</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Forest Canopy Background -->
                <rect x="0" y="0" width="320" height="130" fill="#052e16" />
                <path d="M 0,60 Q 60,20 120,50 T 240,30 T 320,60 L 320,130 L 0,130 Z" fill="#14532d" />
                <path d="M 0,90 Q 70,60 150,85 T 320,70 L 320,130 L 0,130 Z" fill="#166534" />
                
                <!-- Tree Trunks -->
                <rect x="50" y="110" width="20" height="50" fill="#78350f" />
                <rect x="180" y="100" width="24" height="60" fill="#78350f" />

                <!-- Forest Floor Soil Layer (Humus) -->
                <rect x="0" y="150" width="320" height="50" fill="#292524" />
                <rect x="0" y="150" width="320" height="8" fill="#1c1917" /> <!-- Dark Humus layer -->

                <!-- Falling Leaves (Decaying Litter) -->
                <g id="sim10-leaf-litter" style="transition: all 0.5s ease;">
                    <path d="M 70,148 Q 78,142 86,148 Q 78,154 70,148 Z" fill="#b45309" />
                    <path d="M 120,152 Q 130,145 140,152 Q 130,159 120,152 Z" fill="#d97706" />
                    <path d="M 220,149 Q 228,143 236,149 Q 228,155 220,149 Z" fill="#b45309" />
                </g>

                <!-- Decomposer Microbe Activity Arrows -->
                <g id="sim10-recycling-arrows" style="transition: opacity 0.5s ease; opacity: 1;">
                    <path d="M 80,165 Q 85,185 105,175 M 100,170 L 105,175 L 102,180" stroke="#4ade80" stroke-width="1.5" fill="none" />
                    <text x="135" y="178" fill="#4ade80" font-size="9" font-weight="bold">Nutrient Return</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="triggerLeafFall()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🍂 Autumn Leaf Litter (Humus Genesis)
            </button>
            <button onclick="toggleDeforestation(true)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🪓 Clear Cut Trees (Soil Erosion Hazard)
            </button>
        </div>
        <div id="sim10-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Fallen foliage is broken down by saprophytic fungi and earthworms into dark, nutrient-dense humus that feeds tree roots with zero chemical additives.
        </div>
    </div>
    """,

    11: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Chipko Movement & Van Mahotsav Lab</span>
            <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Action: Hugging the Ash Tree</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Himalayan Mountain Backdrop -->
                <polygon points="0,120 70,50 140,120" fill="#1e293b" />
                <polygon points="120,120 200,40 280,120" fill="#334155" />
                <rect x="0" y="150" width="320" height="50" fill="#14532d" />

                <!-- The Mighty Forest Tree -->
                <rect x="145" y="60" width="30" height="100" fill="#78350f" />
                <circle cx="160" cy="50" r="45" fill="#16a34a" />

                <!-- Villager Hugging the Tree (Chipko) -->
                <g id="sim11-protester" transform="translate(135, 100)" style="transition: all 0.5s ease;">
                    <!-- Head -->
                    <circle cx="0" cy="0" r="8" fill="#fde047" stroke="#ca8a04" stroke-width="1.5" />
                    <!-- Body Clinging to Tree -->
                    <rect x="-4" y="8" width="12" height="30" fill="#f43f5e" rx="4" />
                    <!-- Arms Wrapped around Trunk -->
                    <path d="M 8,16 Q 28,16 38,16" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" fill="none" />
                </g>

                <!-- Logger with Axe (Stopped / Blocked) -->
                <g id="sim11-logger" transform="translate(70, 110)" style="transition: all 0.5s ease;">
                    <circle cx="0" cy="0" r="8" fill="#94a3b8" />
                    <rect x="-4" y="8" width="10" height="28" fill="#475569" rx="2" />
                    <!-- Lowered Axe -->
                    <line x1="6" y1="20" x2="18" y2="35" stroke="#b45309" stroke-width="3" />
                    <polygon points="18,35 25,32 23,40" fill="#94a3b8" />
                </g>

                <text x="160" y="185" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Gaura Devi & Villagers Shielding Forest</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setChipkoMode('hug')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌳 Chipko Resistance (Protect Trees)
            </button>
            <button onclick="setChipkoMode('plant')" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🌱 Van Mahotsav (Plant Saplings)
            </button>
        </div>
        <div id="sim11-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In 1974, Gaura Devi and Uttarakhand women hugged forest trees to block commercial axes, pioneering non-violent ecological defense.
        </div>
    </div>
    """,

    12: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Soil Horizon & Earthworm Aeration Lab</span>
            <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Aeration: Active Burrowing</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Topsoil Layer (A Horizon: Rich Humus & Roots) -->
                <rect x="0" y="0" width="320" height="70" fill="#292524" />
                <text x="10" y="20" fill="#a8a29e" font-size="9" font-weight="bold">Topsoil (Humus + Minerals)</text>
                
                <!-- Subsoil Layer (B Horizon: Clay & Minerals) -->
                <rect x="0" y="70" width="320" height="70" fill="#44403c" />
                <text x="10" y="90" fill="#a8a29e" font-size="9" font-weight="bold">Subsoil (Clay + Oxides)</text>

                <!-- Weathered Bedrock Layer (C Horizon) -->
                <rect x="0" y="140" width="320" height="60" fill="#78716c" />
                <text x="10" y="160" fill="#e7e5e4" font-size="9" font-weight="bold">Weathered Bedrock</text>

                <!-- Plant Roots Penetrating Soil -->
                <path d="M 80,0 Q 85,35 75,65 Q 70,85 85,115" stroke="#fef08a" stroke-width="2.5" fill="none" />
                <path d="M 240,0 Q 235,40 245,75 Q 250,100 240,125" stroke="#fef08a" stroke-width="2.5" fill="none" />

                <!-- Earthworm Burrowing & Tunnel -->
                <g id="sim12-worm-group" style="transition: all 0.5s ease;" transform="translate(140, 45)">
                    <!-- Aeration Tunnel -->
                    <path d="M 0,0 Q 20,20 10,50 Q 0,70 15,90" stroke="#1c1917" stroke-width="8" stroke-linecap="round" fill="none" />
                    <!-- Segmented Earthworm Body -->
                    <path d="M 0,0 Q 20,20 10,50" stroke="#f43f5e" stroke-width="5" stroke-linecap="round" fill="none" />
                    <circle cx="0" cy="0" r="3.5" fill="#e11d48" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleEarthworm(true)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🪱 Earthworm Aeration (Pores & Casts)
            </button>
            <button onclick="toggleEarthworm(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🧱 Compacted Soil (Zero Burrowing)
            </button>
        </div>
        <div id="sim12-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Earthworms tunnel subterranean macropores that aerate root zones, improve drainage, and convert organic matter into fertile vermicompost.
        </div>
    </div>
    """,

    13: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Lithosphere: Rocks to Extracted Metals</span>
            <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Display: Mineral to Metal</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- 1. Mineral Ore Rock Left -->
                <g id="sim13-ore-card" transform="translate(60, 95)">
                    <polygon id="sim13-ore-poly" points="-30,-20 0,-35 35,-15 25,25 -20,30" fill="#b45309" stroke="#d97706" stroke-width="2" />
                    <text id="sim13-ore-label" x="0" y="45" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Bauxite Ore</text>
                </g>

                <!-- Blast Furnace Smelting Arrow -->
                <g transform="translate(160, 95)">
                    <circle cx="0" cy="0" r="20" fill="#1e293b" stroke="#6366f1" stroke-width="2" />
                    <text x="0" y="4" font-size="16" text-anchor="middle">🔥</text>
                    <text x="0" y="32" fill="#94a3b8" font-size="9" text-anchor="middle">Refining</text>
                </g>

                <!-- 2. Refined Metal Ingot Right -->
                <g id="sim13-metal-card" transform="translate(260, 95)">
                    <rect id="sim13-ingot-rect" x="-28" y="-15" width="56" height="30" rx="3" fill="#cbd5e1" stroke="#f8fafc" stroke-width="2" />
                    <text id="sim13-metal-label" x="0" y="45" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Aluminium Ingot</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="setMetalSample('aluminium')" class="p-1.5 rounded-lg bg-sky-950 border border-sky-500/50 text-[11px] font-bold text-sky-300">
                ✈️ Bauxite ➔ Aluminium
            </button>
            <button onclick="setMetalSample('iron')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                🏗️ Haematite ➔ Iron
            </button>
            <button onclick="setMetalSample('copper')" class="p-1.5 rounded-lg bg-amber-950 border border-amber-500/50 text-[11px] font-bold text-amber-300">
                ⚡ Chalcopyrite ➔ Copper
            </button>
        </div>
        <div id="sim13-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Mineral ores mined from rock strata are refined in industrial metallurgical furnaces to extract pure structural and electrical metals.
        </div>
    </div>
    """,

    14: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Fossil Fuel Million-Year Geological Chamber</span>
            <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Era: 300 Million Years Ago</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Prehistoric Swamp Surface vs Modern Sedimentary Crust -->
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Strata Layers -->
                <rect x="0" y="30" width="320" height="40" fill="#78350f" />
                <text x="15" y="55" fill="#fde047" font-size="9" font-weight="bold">Sandstone & Mudstone</text>

                <rect x="0" y="70" width="320" height="45" fill="#57534e" />
                <text x="15" y="95" fill="#d6d3d1" font-size="9" font-weight="bold">Shale Caprock (Airtight Trap)</text>

                <!-- Natural Gas Pocket -->
                <rect id="sim14-gas-layer" x="0" y="115" width="320" height="25" fill="#38bdf8" opacity="0.3" />
                <text x="15" y="132" fill="#38bdf8" font-size="9" font-weight="bold">Natural Gas (CNG/Methane)</text>

                <!-- Crude Petroleum Layer -->
                <rect id="sim14-oil-layer" x="0" y="140" width="320" height="30" fill="#1e1b4b" stroke="#312e81" stroke-width="1.5" />
                <text x="15" y="160" fill="#a5b4fc" font-size="9" font-weight="bold">Crude Petroleum Reservoir</text>

                <!-- Coal Seam Base -->
                <rect id="sim14-coal-layer" x="0" y="170" width="320" height="30" fill="#020617" />
                <text x="15" y="190" fill="#94a3b8" font-size="9" font-weight="bold">Compressed Coal Seam</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setFossilEra('prehistoric')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌿 Prehistoric Swamp Biomass
            </button>
            <button onclick="setFossilEra('modern')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🛢️ Modern Buried Hydrocarbon Trap
            </button>
        </div>
        <div id="sim14-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Over 300 million years, heat and immense geological pressure metamorphosed ancient organic swamp vegetation into coal, crude oil, and natural gas.
        </div>
    </div>
    """,

    15: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Renewable vs. Non-Renewable Resource Sorter</span>
            <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Select an Item to Classify</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Left Bin: Renewable -->
                <rect x="20" y="20" width="130" height="160" rx="10" fill="#064e3b" opacity="0.6" stroke="#10b981" stroke-width="2" />
                <text x="85" y="45" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Renewable</text>
                <text x="85" y="60" fill="#a7f3d0" font-size="8" text-anchor="middle">Naturally Replenished</text>
                <g id="sim15-renewable-items" transform="translate(85, 110)">
                    <text x="0" y="0" font-size="28" text-anchor="middle">☀️ 💨 🌲</text>
                </g>

                <!-- Right Bin: Non-Renewable -->
                <rect x="170" y="20" width="130" height="160" rx="10" fill="#4c0519" opacity="0.6" stroke="#f43f5e" stroke-width="2" />
                <text x="235" y="45" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Non-Renewable</text>
                <text x="235" y="60" fill="#fecdd3" font-size="8" text-anchor="middle">Finite Exhaustible</text>
                <g id="sim15-nonrenewable-items" transform="translate(235, 110)">
                    <text x="0" y="0" font-size="28" text-anchor="middle">🛢️ ⛏️ 🪨</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="testResource('sun')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                ☀️ Sunlight
            </button>
            <button onclick="testResource('petrol')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                🛢️ Petroleum
            </button>
            <button onclick="testResource('forest')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🌲 Forests
            </button>
        </div>
        <div id="sim15-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click any resource to classify it based on whether nature regenerates it within human timeframes or whether it will permanently deplete.
        </div>
    </div>
    """,

    16: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Gandhian Ecological Balance Meter</span>
            <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Mode: Sustainable Need</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Two-Pan Balance Scale of Justice & Ecology -->
                <!-- Central Fulcrum Pillar -->
                <line x1="160" y1="50" x2="160" y2="170" stroke="#64748b" stroke-width="4" stroke-linecap="round" />
                <polygon points="140,175 180,175 160,165" fill="#475569" />
                
                <!-- Tilting Beam -->
                <g id="sim16-beam" style="transform-origin: 160px 60px; transition: transform 0.5s ease; transform: rotate(0deg);">
                    <line x1="60" y1="60" x2="260" y2="60" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />
                    <!-- Left Pan Strings & Pan (Need) -->
                    <line x1="80" y1="60" x2="60" y2="110" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="80" y1="60" x2="100" y2="110" stroke="#94a3b8" stroke-width="1.5" />
                    <path d="M 50,110 Q 80,125 110,110 Z" fill="#15803d" stroke="#22c55e" stroke-width="1.5" />
                    <text x="80" y="140" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Every Man's Need</text>

                    <!-- Right Pan Strings & Pan (Greed) -->
                    <line x1="240" y1="60" x2="220" y2="110" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="240" y1="60" x2="260" y2="110" stroke="#94a3b8" stroke-width="1.5" />
                    <path d="M 210,110 Q 240,125 270,110 Z" fill="#991b1b" stroke="#f43f5e" stroke-width="1.5" />
                    <text x="240" y="140" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Limitless Greed</text>
                </g>

                <!-- Gandhi Quote Banner -->
                <rect x="25" y="170" width="270" height="24" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="160" y="186" fill="#fde047" font-size="9.5" font-style="italic" text-anchor="middle">"Earth provides enough for need, not for greed."</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setBalanceState('need')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚲 Moderate Need (Ecological Harmony)
            </button>
            <button onclick="setBalanceState('greed')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🚗 Wasteful Greed (Resource Depletion)
            </button>
        </div>
        <div id="sim16-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Sustainable living balances resource consumption within Earth's regenerative boundaries, preserving treasures for posterity.
        </div>
    </div>
    """
}


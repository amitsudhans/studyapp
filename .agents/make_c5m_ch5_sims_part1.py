#!/usr/bin/env python3
"""
Generate Simulators 1 to 8 for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""

sims_1_to_8 = {}

# Simulator 1: Choosing Units (Real-World Quantity Sorter)
sims_1_to_8[1] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Sensible Unit Selector
        </span>
        <span id="s1UnitReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            India Gate: Metres (42 m)
        </span>
    </div>

    <!-- Object Selection Grid -->
    <div class="w-full grid grid-cols-4 gap-1.5 mb-2">
        <button id="s1Obj1" onclick="s1SelectObject(1)" class="px-2 py-1 bg-amber-500/30 text-amber-200 border border-amber-500/40 rounded text-xs font-bold transition">
            🏛️ India Gate
        </button>
        <button id="s1Obj2" onclick="s1SelectObject(2)" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🧣 Hanky
        </button>
        <button id="s1Obj3" onclick="s1SelectObject(3)" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🕳️ Well Depth
        </button>
        <button id="s1Obj4" onclick="s1SelectObject(4)" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🛣️ Highway
        </button>
    </div>

    <!-- Visual Card Display -->
    <div class="w-full max-w-[340px] aspect-[4/3] bg-slate-950 rounded-xl border border-slate-800 p-4 my-2 flex flex-col items-center justify-center text-center">
        <div id="s1Icon" class="text-4xl mb-2">🏛️</div>
        <div id="s1Title" class="text-base font-bold text-white">India Gate (New Delhi)</div>
        <div id="s1Desc" class="text-xs text-slate-400 mt-1">Majestic memorial archway in central Delhi.</div>
        <div id="s1BestUnit" class="mt-3 px-3 py-1 bg-amber-950/70 border border-amber-500/40 rounded-lg text-amber-300 font-mono text-xs font-extrabold">
            Best Unit: Metres (m) • ~42 m tall
        </div>
    </div>

    <!-- Unit Buttons to Test -->
    <div class="w-full grid grid-cols-4 gap-2 mt-2">
        <button onclick="s1TestUnit('mm')" class="py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-bold transition">
            Millimetres
        </button>
        <button onclick="s1TestUnit('cm')" class="py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-bold transition">
            Centimetres
        </button>
        <button onclick="s1TestUnit('m')" class="py-1.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            Metres
        </button>
        <button onclick="s1TestUnit('km')" class="py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-bold transition">
            Kilometres
        </button>
    </div>
</div>
"""

# Simulator 2: Unit Equivalence (Double Number Line Fabric Converter)
sims_1_to_8[2] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Double Number Line Fabric Scale
        </span>
        <span id="s2DualReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            2.4 m = 240 cm (2 m 40 cm)
        </span>
    </div>

    <!-- Double Number Line SVG -->
    <div class="relative w-full max-w-[340px] aspect-[5/3] flex items-center justify-center my-2">
        <svg id="s2Svg" viewBox="-20 -60 300 120" class="w-full h-full drop-shadow-md">
            <!-- Top Line (Metres) -->
            <line x1="0" y1="-25" x2="260" y2="-25" stroke="#3b82f6" stroke-width="3"/>
            <text x="270" y="-22" font-size="10" font-weight="bold" fill="#60a5fa">Metres (m)</text>

            <!-- Bottom Line (Centimetres) -->
            <line x1="0" y1="25" x2="260" y2="25" stroke="#10b981" stroke-width="3"/>
            <text x="270" y="28" font-size="10" font-weight="bold" fill="#34d399">Centimetres (cm)</text>

            <!-- Scale Ticks 0 to 5m / 0 to 500cm -->
            <!-- 0 -->
            <line x1="0" y1="-30" x2="0" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="0" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">0</text>
            <text x="0" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">0</text>
            <!-- 1m = 100cm (x=52) -->
            <line x1="52" y1="-30" x2="52" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="52" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">1m</text>
            <text x="52" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">100</text>
            <!-- 2m = 200cm (x=104) -->
            <line x1="104" y1="-30" x2="104" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="104" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">2m</text>
            <text x="104" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">200</text>
            <!-- 3m = 300cm (x=156) -->
            <line x1="156" y1="-30" x2="156" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="156" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">3m</text>
            <text x="156" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">300</text>
            <!-- 4m = 400cm (x=208) -->
            <line x1="208" y1="-30" x2="208" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="208" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">4m</text>
            <text x="208" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">400</text>
            <!-- 5m = 500cm (x=260) -->
            <line x1="260" y1="-30" x2="260" y2="30" stroke="#64748b" stroke-width="1.5"/>
            <text x="260" y="-35" text-anchor="middle" font-size="9" fill="#93c5fd">5m</text>
            <text x="260" y="42" text-anchor="middle" font-size="9" fill="#6ee7b7">500</text>

            <!-- Dynamic Indicator Cursor -->
            <g id="s2Cursor" transform="translate(124.8, 0)">
                <line x1="0" y1="-40" x2="0" y2="40" stroke="#f59e0b" stroke-width="3"/>
                <polygon points="0,-42 -4,-48 4,-48" fill="#f59e0b"/>
                <polygon points="0,42 -4,48 4,48" fill="#f59e0b"/>
            </g>
        </svg>
    </div>

    <!-- Fabric Presets -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s2SetCm(240)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Stole: 240 cm (2m 40cm)
        </button>
        <button onclick="s2SetCm(350)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Curtain: 350 cm (3m 50cm)
        </button>
        <button onclick="s2SetCm(550)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Sari: 550 cm (5m 50cm)
        </button>
    </div>

    <!-- Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-3 px-2">
        <span class="text-xs text-slate-400">Length (cm):</span>
        <input type="range" id="s2Slider" min="0" max="500" value="240" step="10" oninput="s2SetCm(this.value)" class="flex-1 accent-blue-400 cursor-pointer">
        <span id="s2SliderVal" class="font-mono text-blue-300 font-bold text-xs w-16 text-right">240 cm</span>
    </div>
</div>
"""

# Simulator 3: Comparing Lengths (Balance & Inequality Comparator)
sims_1_to_8[3] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Mixed Length Inequality Balance
        </span>
        <span id="s3CompReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            456 cm &lt; 5 m (500 cm)
        </span>
    </div>

    <!-- Comparison Cards -->
    <div class="w-full grid grid-cols-3 gap-2 items-center my-3 text-center">
        <!-- Item 1 -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Length A</div>
            <div id="s3ValA" class="text-base font-extrabold text-white mt-1">456 cm</div>
            <div id="s3EquivA" class="text-xs text-teal-400 font-mono mt-0.5">= 456 cm</div>
        </div>

        <!-- Big Inequality Symbol -->
        <div class="flex items-center justify-center">
            <div id="s3SymbolBox" class="w-12 h-12 rounded-full bg-teal-950 border-2 border-teal-400 flex items-center justify-center text-2xl font-extrabold text-teal-300 shadow">
                &lt;
            </div>
        </div>

        <!-- Item 2 -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Length B</div>
            <div id="s3ValB" class="text-base font-extrabold text-white mt-1">5 m</div>
            <div id="s3EquivB" class="text-xs text-teal-400 font-mono mt-0.5">= 500 cm</div>
        </div>
    </div>

    <!-- Rule Explanation -->
    <div id="s3Explanation" class="w-full p-2.5 bg-slate-850 rounded-xl border border-slate-700 text-xs font-medium text-center text-slate-300 mb-2">
        Convert 5 m to 500 cm first! Since 456 cm &lt; 500 cm, 456 cm &lt; 5 m.
    </div>

    <!-- Comparison Presets -->
    <div class="w-full grid grid-cols-3 gap-2">
        <button onclick="s3Compare('456 cm', 456, '5 m', 500)" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded-lg text-xs font-bold transition">
            456 cm vs 5 m
        </button>
        <button onclick="s3Compare('3 m 25 cm', 325, '350 cm', 350)" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded-lg text-xs font-bold transition">
            3 m 25 cm vs 350 cm
        </button>
        <button onclick="s3Compare('6 m', 600, '600 cm', 600)" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded-lg text-xs font-bold transition">
            6 m vs 600 cm (=)
        </button>
    </div>
</div>
"""

# Simulator 4: Tallest Statues (Monument Height Barometer)
sims_1_to_8[4] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            World's Tallest Statues Height Barometer
        </span>
        <span id="s4StatueDiff" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            Unity (182m) - Buddha (128m) = 54 m
        </span>
    </div>

    <!-- SVG Statue Height Comparison Chart -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s4Svg" viewBox="-20 -100 280 140" class="w-full h-full drop-shadow-md">
            <!-- Ground Line -->
            <line x1="0" y1="25" x2="260" y2="25" stroke="#475569" stroke-width="2"/>

            <!-- Statue of Unity: 182 m (bar height 91) -->
            <rect x="20" y="-66" width="35" height="91" fill="#f59e0b" rx="2"/>
            <text x="37.5" y="-71" text-anchor="middle" font-size="10" font-weight="bold" fill="#fde047">182 m</text>
            <text x="37.5" y="38" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#cbd5e1">Unity (IND)</text>

            <!-- Spring Temple Buddha: 128 m (bar height 64) -->
            <rect x="100" y="-39" width="35" height="64" fill="#3b82f6" rx="2"/>
            <text x="117.5" y="-44" text-anchor="middle" font-size="10" font-weight="bold" fill="#93c5fd">128 m</text>
            <text x="117.5" y="38" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#cbd5e1">Buddha (CHN)</text>

            <!-- Statue of Liberty: 93 m (bar height 46.5) -->
            <rect x="180" y="-21.5" width="35" height="46.5" fill="#10b981" rx="2"/>
            <text x="197.5" y="-26.5" text-anchor="middle" font-size="10" font-weight="bold" fill="#6ee7b7">93 m</text>
            <text x="197.5" y="38" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#cbd5e1">Liberty (USA)</text>
        </svg>
    </div>

    <!-- Quick Compare Buttons -->
    <div class="w-full grid grid-cols-2 gap-2 mt-2">
        <button onclick="s4Compare(182, 128, 'Statue of Unity', 'Spring Temple Buddha')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-200 border border-emerald-500/30 rounded-lg text-xs font-bold transition">
            Unity vs Buddha (54 m)
        </button>
        <button onclick="s4Compare(182, 93, 'Statue of Unity', 'Statue of Liberty')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-200 border border-emerald-500/30 rounded-lg text-xs font-bold transition">
            Unity vs Liberty (89 m)
        </button>
    </div>
</div>
"""

# Simulator 5: Measuring Tools (Interactive Rodometer Wheel)
sims_1_to_8[5] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Surveyor Measuring Wheel (Rodometer)
        </span>
        <span id="s5WheelReadout" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            Distance: 0 Metres (0 Revs)
        </span>
    </div>

    <!-- SVG Rolling Wheel -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s5Svg" viewBox="-120 -80 240 160" class="w-full h-full drop-shadow-md">
            <!-- Ground Line -->
            <line x1="-110" y1="50" x2="110" y2="50" stroke="#475569" stroke-width="4" stroke-linecap="round"/>

            <!-- Handle Frame -->
            <line x1="-15" y1="20" x2="-60" y2="-60" stroke="#94a3b8" stroke-width="5" stroke-linecap="round"/>
            <circle cx="-60" cy="-60" r="7" fill="#64748b"/>

            <!-- Digital Counter on Handle -->
            <rect x="-48" y="-30" width="36" height="20" fill="#0f172a" stroke="#a855f7" stroke-width="2" rx="3"/>
            <text id="s5CounterText" x="-30" y="-16" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#d8b4fe">0 m</text>

            <!-- Rolling Wheel Group -->
            <g id="s5Wheel" transform="translate(-15, 20) rotate(0)">
                <circle cx="0" cy="0" r="30" fill="none" stroke="#a855f7" stroke-width="4"/>
                <line x1="0" y1="-30" x2="0" y2="30" stroke="#c084fc" stroke-width="2"/>
                <line x1="-30" y1="0" x2="30" y2="0" stroke="#c084fc" stroke-width="2"/>
                <!-- Wheel Marker Dot -->
                <circle cx="0" cy="-25" r="4" fill="#f59e0b"/>
                <circle cx="0" cy="0" r="5" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
            </g>
        </svg>
    </div>

    <!-- Roll Controls -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s5Roll(1)" class="px-2 py-1.5 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded-lg text-xs font-bold transition">
            Roll 1 Metre 🔄
        </button>
        <button onclick="s5Roll(5)" class="px-2 py-1.5 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded-lg text-xs font-bold transition">
            Roll 5 Metres ⏩
        </button>
        <button onclick="s5Reset()" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Reset
        </button>
    </div>
</div>
"""

# Simulator 6: The Kilometre (200m Track & Footstep Counter)
sims_1_to_8[6] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-rose-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-rose-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-rose-400 animate-pulse"></span>
            1 Kilometre Track Lap Counter
        </span>
        <span id="s6KmReadout" class="font-mono bg-rose-950/80 px-2.5 py-1 rounded-md text-rose-300 border border-rose-500/30 font-bold">
            0 Laps = 0 Metres (0 km)
        </span>
    </div>

    <!-- SVG Track & Runner -->
    <div class="relative w-full max-w-[340px] aspect-[5/3] flex items-center justify-center my-2">
        <svg id="s6Svg" viewBox="-120 -70 240 140" class="w-full h-full drop-shadow-md">
            <!-- 200m Oval Running Track -->
            <rect x="-80" y="-40" width="160" height="80" rx="40" fill="#1e293b" stroke="#f43f5e" stroke-width="4"/>
            <rect x="-65" y="-25" width="130" height="50" rx="25" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="0" y="5" text-anchor="middle" font-size="11" font-weight="bold" fill="#fda4af">200m Lap</text>

            <!-- Runner Marker -->
            <circle id="s6Runner" cx="-80" cy="0" r="7" fill="#fbbf24" stroke="#ffffff" stroke-width="2"/>
        </svg>
    </div>

    <!-- Metrics Bar -->
    <div class="w-full grid grid-cols-3 gap-2 my-2 text-center text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Laps (200m each)</div>
            <div id="s6LapsVal" class="text-sm font-extrabold text-white mt-0.5">0 / 5</div>
        </div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Metres</div>
            <div id="s6MetresVal" class="text-sm font-extrabold text-rose-400 mt-0.5">0 m</div>
        </div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Footsteps (~0.5m)</div>
            <div id="s6StepsVal" class="text-sm font-extrabold text-amber-400 mt-0.5">0 steps</div>
        </div>
    </div>

    <!-- Lap Stepper Button -->
    <div class="w-full flex items-center justify-between gap-3 mt-1">
        <button onclick="s6AddLap()" class="flex-1 py-2 bg-gradient-to-r from-rose-500 to-pink-500 hover:from-rose-600 hover:to-pink-600 text-slate-950 font-extrabold rounded-xl text-xs transition shadow">
            Run 1 Lap (+200 m, 400 steps) 🏃
        </button>
        <button onclick="s6Reset()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-bold transition">
            Reset
        </button>
    </div>
</div>
"""

# Simulator 7: Race Track (3-Kilometre Marathon Course Planner)
sims_1_to_8[7] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            3-km Marathon Route Planner
        </span>
        <span id="s7CourseStatus" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            5 Water Stations (Every 500m)
        </span>
    </div>

    <!-- Linear Course Route SVG -->
    <div class="relative w-full max-w-[340px] aspect-[5/2] flex items-center justify-center my-2">
        <svg id="s7Svg" viewBox="-10 -30 320 60" class="w-full h-full drop-shadow-md">
            <!-- Main Highway Track (3,000 m) -->
            <line x1="10" y1="0" x2="290" y2="0" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>

            <!-- Start (0m) -->
            <circle cx="10" cy="0" r="6" fill="#10b981"/>
            <text x="10" y="20" text-anchor="middle" font-size="9" font-weight="bold" fill="#6ee7b7">Start (0m)</text>

            <!-- 500m Intervals Dots Group -->
            <g id="s7StationMarkers"></g>

            <!-- Finish (3,000m) -->
            <circle cx="290" cy="0" r="6" fill="#ef4444"/>
            <text x="290" y="20" text-anchor="middle" font-size="9" font-weight="bold" fill="#fca5a5">Finish (3km)</text>
        </svg>
    </div>

    <!-- Interval Controls -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s7SetInterval(500)" class="px-2 py-1.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            Water Every 500m (5 Stations)
        </button>
        <button onclick="s7SetInterval(250)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Marshals Every 250m
        </button>
        <button onclick="s7SetInterval(1000)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Milestones Every 1km
        </button>
    </div>
</div>
"""

# Simulator 8: Train Journey (Vivek Express 4,189 km Explorer)
sims_1_to_8[8] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Vivek Express 4,189 km Explorer
        </span>
        <span id="s8TrainReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            Total Journey: 4,189 km (75 Hours)
        </span>
    </div>

    <!-- Schematic Route SVG -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s8Svg" viewBox="-120 -80 240 160" class="w-full h-full drop-shadow-md">
            <!-- Train Track Path -->
            <path d="M 80,-60 L 40,-40 L -20,0 L -10,30 L -30,60" fill="none" stroke="#3b82f6" stroke-width="4" stroke-dasharray="6 3"/>

            <!-- Stations -->
            <!-- Dibrugarh -->
            <circle cx="80" cy="-60" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
            <text x="88" y="-56" font-size="9" font-weight="bold" fill="#fca5a5">Dibrugarh (Assam)</text>

            <!-- Guwahati -->
            <circle cx="40" cy="-40" r="6" fill="#fbbf24"/>
            <text x="48" y="-36" font-size="9" fill="#fde047">Guwahati (560km)</text>

            <!-- Malda Town -->
            <circle cx="-20" cy="0" r="6" fill="#10b981"/>
            <text x="-15" y="-5" font-size="8.5" fill="#6ee7b7">Malda Town (1,200km)</text>

            <!-- Visakhapatnam -->
            <circle cx="-10" cy="30" r="6" fill="#38bdf8"/>
            <text x="0" y="34" font-size="8.5" fill="#7dd3fc">Vizag (2,300km)</text>

            <!-- Kanniyakumari -->
            <circle cx="-30" cy="60" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
            <text x="-20" y="64" font-size="9" font-weight="bold" fill="#fca5a5">Kanniyakumari (4,189km)</text>
        </svg>
    </div>

    <!-- Route Stats -->
    <div class="w-full p-2.5 bg-slate-950 rounded-xl border border-slate-800 text-center font-mono text-xs text-slate-300">
        4,189 km • 9 States Traversed • 55+ Major Stops • Longest Rail Route in India
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 1 to 8. Count: {len(sims_1_to_8)}")


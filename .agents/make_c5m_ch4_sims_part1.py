#!/usr/bin/env python3
"""
Generate Simulators 1 to 8 for NCERT Class 5 Mathematics - Chapter 4: We the Travellers - II
"""

sims_1_to_8 = {}

# Simulator 1: Equal Sums (Two-Pan Balance & Number Swapper)
sims_1_to_8[1] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Two-Pan Number Balance
        </span>
        <span id="s1BalanceStatus" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            Group A: 48 | Group B: 40 (Diff: 8)
        </span>
    </div>

    <!-- SVG Balance Scale -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s1Svg" viewBox="-160 -120 320 200" class="w-full h-full drop-shadow-md">
            <!-- Stand & Fulcrum -->
            <polygon points="-15,80 15,80 0,0" fill="#475569"/>
            <rect x="-60" y="80" width="120" height="12" fill="#334155" rx="3"/>
            <circle cx="0" cy="0" r="8" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>

            <!-- Tilting Beam -->
            <g id="s1BeamGroup" transform="rotate(-6)">
                <line x1="-130" y1="0" x2="130" y2="0" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
                
                <!-- Left Pan (Group A) -->
                <g transform="translate(-120, 0)">
                    <line x1="0" y1="0" x2="-25" y2="45" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="0" y1="0" x2="25" y2="45" stroke="#94a3b8" stroke-width="1.5"/>
                    <path d="M -35,45 Q 0,65 35,45 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                    <text id="s1LeftText" x="0" y="38" text-anchor="middle" font-size="12" font-weight="bold" fill="#fde047">Sum: 48</text>
                </g>

                <!-- Right Pan (Group B) -->
                <g transform="translate(120, 0)">
                    <line x1="0" y1="0" x2="-25" y2="45" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="0" y1="0" x2="25" y2="45" stroke="#94a3b8" stroke-width="1.5"/>
                    <path d="M -35,45 Q 0,65 35,45 Z" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
                    <text id="s1RightText" x="0" y="38" text-anchor="middle" font-size="12" font-weight="bold" fill="#93c5fd">Sum: 40</text>
                </g>
            </g>
        </svg>
    </div>

    <!-- Cards Layout -->
    <div class="w-full grid grid-cols-2 gap-3 mt-2 text-xs">
        <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl">
            <div class="font-bold text-amber-300 mb-1.5 flex justify-between">
                <span>Group A</span>
                <span id="s1SumA">Sum = 48</span>
            </div>
            <div class="flex gap-1.5" id="s1CardsA">
                <span class="px-2 py-1 bg-amber-500/20 text-amber-200 border border-amber-500/40 rounded font-mono font-bold">12</span>
                <span class="px-2 py-1 bg-amber-500/20 text-amber-200 border border-amber-500/40 rounded font-mono font-bold">16</span>
                <span class="px-2 py-1 bg-amber-400 text-slate-950 border border-amber-300 rounded font-mono font-extrabold shadow">20</span>
            </div>
        </div>
        <div class="p-3 bg-blue-950/40 border border-blue-500/30 rounded-xl">
            <div class="font-bold text-blue-300 mb-1.5 flex justify-between">
                <span>Group B</span>
                <span id="s1SumB">Sum = 40</span>
            </div>
            <div class="flex gap-1.5" id="s1CardsB">
                <span class="px-2 py-1 bg-blue-500/20 text-blue-200 border border-blue-500/40 rounded font-mono font-bold">10</span>
                <span class="px-2 py-1 bg-blue-500/20 text-blue-200 border border-blue-500/40 rounded font-mono font-bold">14</span>
                <span class="px-2 py-1 bg-blue-400 text-slate-950 border border-blue-300 rounded font-mono font-extrabold shadow">16</span>
            </div>
        </div>
    </div>

    <!-- Swap Action Button -->
    <div class="w-full flex items-center justify-between gap-3 mt-3">
        <button id="s1SwapBtn" onclick="s1Swap()" class="flex-1 py-2 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-slate-950 font-extrabold rounded-xl text-xs transition shadow">
            Swap 20 (Group A) with 16 (Group B) [Diff = 4 = 8/2]
        </button>
        <button onclick="s1Reset()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-bold transition">
            Reset
        </button>
    </div>
</div>
"""

# Simulator 2: Fuel Mileage (Vehicle Fuel Consumption & Passenger Efficiency)
sims_1_to_8[2] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            Vehicle Fuel & Efficiency Barometer
        </span>
        <span id="s2EfficiencyReadout" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            Car: 15 km/L (20 L for 300 km)
        </span>
    </div>

    <!-- Vehicle Select Tabs -->
    <div class="w-full grid grid-cols-4 gap-1.5 mb-2">
        <button id="s2TabBike" onclick="s2SelectVehicle('bike')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🏍️ Bike (50 km/L)
        </button>
        <button id="s2TabCar" onclick="s2SelectVehicle('car')" class="px-2 py-1 bg-emerald-500/30 text-emerald-200 border border-emerald-500/40 rounded text-xs font-bold transition">
            🚗 Car (15 km/L)
        </button>
        <button id="s2TabMinibus" onclick="s2SelectVehicle('minibus')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🚐 Minibus (8 km/L)
        </button>
        <button id="s2TabBus" onclick="s2SelectVehicle('bus')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🚌 Bus (4 km/L)
        </button>
    </div>

    <!-- Visual Dashboard -->
    <div class="w-full p-4 bg-slate-850 rounded-xl border border-slate-700 my-2 grid grid-cols-3 gap-3 text-center">
        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Journey Distance</div>
            <div id="s2DistDisplay" class="text-base font-extrabold text-white mt-1">300 km</div>
        </div>
        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Fuel Consumed</div>
            <div id="s2FuelDisplay" class="text-base font-extrabold text-amber-400 mt-1">20.0 L</div>
        </div>
        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Per Passenger Fuel</div>
            <div id="s2PerPaxDisplay" class="text-base font-extrabold text-emerald-400 mt-1">5.0 L / pax</div>
        </div>
    </div>

    <!-- Distance Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Trip Distance:</span>
        <input type="range" id="s2DistSlider" min="50" max="600" value="300" step="25" oninput="s2Update(this.value)" class="flex-1 accent-emerald-400 cursor-pointer">
        <span id="s2SliderVal" class="font-mono text-emerald-300 font-bold text-xs w-14 text-right">300 km</span>
    </div>
</div>
"""

# Simulator 3: Place Value (Addition with Regrouping Machine)
sims_1_to_8[3] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            3-Digit Addition Regrouping Machine
        </span>
        <span id="s3StepReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            Problem: 258 + 175
        </span>
    </div>

    <!-- Column Place Value Table -->
    <div class="w-full max-w-[320px] bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-sm shadow-inner my-2">
        <!-- Carry Row -->
        <div class="grid grid-cols-4 text-center text-amber-400 font-bold text-xs pb-1 border-b border-slate-800">
            <span class="text-slate-500">Carry:</span>
            <span id="s3CarryH">-</span>
            <span id="s3CarryT" class="text-amber-400">-</span>
            <span id="s3CarryO" class="text-amber-400">-</span>
        </div>
        <!-- Headers -->
        <div class="grid grid-cols-4 text-center text-slate-400 font-bold text-xs py-1 border-b border-slate-800">
            <span></span>
            <span>H</span>
            <span>T</span>
            <span>O</span>
        </div>
        <!-- Row 1: 258 -->
        <div class="grid grid-cols-4 text-center text-white py-1">
            <span class="text-slate-500 text-xs"></span>
            <span>2</span>
            <span>5</span>
            <span>8</span>
        </div>
        <!-- Row 2: + 175 -->
        <div class="grid grid-cols-4 text-center text-white py-1 border-b-2 border-slate-700">
            <span class="text-amber-400 font-bold">+</span>
            <span>1</span>
            <span>7</span>
            <span>5</span>
        </div>
        <!-- Result Row: 433 -->
        <div class="grid grid-cols-4 text-center text-emerald-400 font-extrabold text-base pt-1">
            <span>=</span>
            <span id="s3ResH">?</span>
            <span id="s3ResT">?</span>
            <span id="s3ResO">?</span>
        </div>
    </div>

    <!-- Step Controls -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button id="s3StepBtn1" onclick="s3DoStep(1)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Step 1: Add Ones
        </button>
        <button id="s3StepBtn2" onclick="s3DoStep(2)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Step 2: Add Tens
        </button>
        <button id="s3StepBtn3" onclick="s3DoStep(3)" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-200 border border-blue-500/30 rounded-lg text-xs font-bold transition">
            Step 3: Add Hundreds
        </button>
    </div>

    <!-- Explanation Box -->
    <div id="s3Explanation" class="w-full mt-2 p-2.5 bg-slate-800/80 rounded-lg text-xs text-slate-300 border border-slate-700 text-center font-medium">
        Click 'Step 1: Add Ones' to begin adding 8 + 5.
    </div>
</div>
"""

# Simulator 4: Inverse Operations (Fact Family Triangle)
sims_1_to_8[4] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Inverse Fact Family Triangle
        </span>
        <span id="s4FamilyReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            Fact Family: [125, 75, 200]
        </span>
    </div>

    <!-- SVG Fact Family Triangle -->
    <div class="relative w-full max-w-[320px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s4Svg" viewBox="-120 -100 240 180" class="w-full h-full drop-shadow-md">
            <!-- Triangle Outline -->
            <polygon points="0,-70 -90,60 90,60" fill="#0f172a" stroke="#14b8a6" stroke-width="4" stroke-linejoin="round"/>
            
            <!-- Nodes -->
            <!-- Apex: Whole (200) -->
            <circle cx="0" cy="-70" r="22" fill="#0f766e" stroke="#2dd4bf" stroke-width="3"/>
            <text x="0" y="-64" text-anchor="middle" font-size="13" font-weight="bold" fill="#ffffff">200</text>
            <text x="0" y="-96" text-anchor="middle" font-size="10" font-weight="bold" fill="#5eead4">WHOLE</text>

            <!-- Bottom Left: Part 1 (125) -->
            <circle cx="-90" cy="60" r="20" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
            <text x="-90" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">125</text>
            <text x="-90" y="92" text-anchor="middle" font-size="10" font-weight="bold" fill="#7dd3fc">PART 1</text>

            <!-- Bottom Right: Part 2 (75) -->
            <circle cx="90" cy="60" r="20" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
            <text x="90" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">75</text>
            <text x="90" y="92" text-anchor="middle" font-size="10" font-weight="bold" fill="#fde047">PART 2</text>

            <!-- Operator Signs inside Triangle -->
            <text x="0" y="10" text-anchor="middle" font-size="18" font-weight="bold" fill="#94a3b8">⇄</text>
            <text x="-50" y="-10" text-anchor="middle" font-size="14" font-weight="bold" fill="#f43f5e">−</text>
            <text x="50" y="-10" text-anchor="middle" font-size="14" font-weight="bold" fill="#f43f5e">−</text>
            <text x="0" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#10b981">+</text>
        </svg>
    </div>

    <!-- 4 Equations Grid -->
    <div class="w-full grid grid-cols-2 gap-2 mt-2 font-mono text-xs">
        <button onclick="s4Highlight(1)" class="p-2 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-emerald-200 text-left hover:bg-emerald-900/40 transition">
            125 + 75 = 200
        </button>
        <button onclick="s4Highlight(2)" class="p-2 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-emerald-200 text-left hover:bg-emerald-900/40 transition">
            75 + 125 = 200
        </button>
        <button onclick="s4Highlight(3)" class="p-2 bg-rose-950/40 border border-rose-500/30 rounded-lg text-rose-200 text-left hover:bg-rose-900/40 transition">
            200 - 75 = 125
        </button>
        <button onclick="s4Highlight(4)" class="p-2 bg-rose-950/40 border border-rose-500/30 rounded-lg text-rose-200 text-left hover:bg-rose-900/40 transition">
            200 - 125 = 75
        </button>
    </div>
</div>
"""

# Simulator 5: Fuel Problems (Minibus Fuel Gauge & Subtraction Solver)
sims_1_to_8[5] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Minibus Fuel Tank Refill Solver
        </span>
        <span id="s5FuelReadout" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            Tank: 38 L / 65 L
        </span>
    </div>

    <!-- Fuel Gauge / Tank Visual -->
    <div class="w-full max-w-[320px] bg-slate-950 p-4 rounded-xl border border-slate-800 my-2">
        <div class="flex justify-between text-xs text-slate-400 mb-1">
            <span>Empty (0 L)</span>
            <span class="text-amber-400 font-bold">Current: <span id="s5CurrentL">38</span> L</span>
            <span>Full (65 L)</span>
        </div>
        <!-- Progress Bar -->
        <div class="w-full h-7 bg-slate-800 rounded-lg overflow-hidden border border-slate-700 relative">
            <div id="s5TankFill" class="h-full bg-gradient-to-r from-amber-500 to-emerald-500 transition-all duration-300" style="width: 58.5%;"></div>
            <div class="absolute inset-0 flex items-center justify-center text-xs font-bold text-white drop-shadow">
                <span id="s5AddedText">Fuel Added: 27 Litres (65 - 38)</span>
            </div>
        </div>
    </div>

    <!-- Subtraction with Regrouping Column -->
    <div class="w-full max-w-[280px] p-3 bg-slate-850 rounded-xl border border-slate-700 font-mono text-xs my-2 text-center">
        <div class="text-slate-400 pb-1 border-b border-slate-700">65 L (Final) - 38 L (Initial)</div>
        <div class="py-1 text-slate-200">
            Regroup 6 Tens into 5 Tens + 15 Ones<br>
            Ones: 15 - 8 = 7 Ones<br>
            Tens: 5 - 3 = 2 Tens
        </div>
        <div class="pt-1 text-emerald-400 font-bold border-t border-slate-700">
            Result = 27 Litres Added | Check: 38 + 27 = 65 L
        </div>
    </div>

    <!-- Interactive Refill Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Fill Tank To:</span>
        <input type="range" id="s5Slider" min="38" max="65" value="65" oninput="s5Update(this.value)" class="flex-1 accent-purple-400 cursor-pointer">
        <span id="s5SliderVal" class="font-mono text-purple-300 font-bold text-xs w-10 text-right">65 L</span>
    </div>
</div>
"""

# Simulator 6: Consecutive Numbers (3 & 4 Consecutive Number Sum Analyzer)
sims_1_to_8[6] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-rose-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-rose-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-rose-400 animate-pulse"></span>
            Consecutive Number Sum Analyzer
        </span>
        <span id="s6SumReadout" class="font-mono bg-rose-950/80 px-2.5 py-1 rounded-md text-rose-300 border border-rose-500/30 font-bold">
            3 Numbers: 4 + 5 + 6 = 15
        </span>
    </div>

    <!-- Mode Selector -->
    <div class="w-full grid grid-cols-2 gap-2 mb-2">
        <button id="s6Mode3" onclick="s6SetMode(3)" class="py-1.5 bg-rose-500/30 text-rose-200 border border-rose-500/40 rounded-lg text-xs font-bold transition">
            3 Consecutive Numbers (Sum = 3 × Middle)
        </button>
        <button id="s6Mode4" onclick="s6SetMode(4)" class="py-1.5 bg-slate-800 text-slate-300 border border-slate-700 rounded-lg text-xs font-bold transition">
            4 Consecutive Numbers (Always Even)
        </button>
    </div>

    <!-- Visual Blocks -->
    <div id="s6BlocksContainer" class="w-full flex items-center justify-center gap-2 my-3">
        <!-- Injected via JS -->
    </div>

    <!-- Formula Display -->
    <div id="s6FormulaBox" class="w-full p-2.5 bg-slate-850 rounded-xl border border-slate-700 text-center font-mono text-xs text-rose-300">
        4 + 5 + 6 = 15 | Notice: 3 × Middle (5) = 15!
    </div>

    <!-- Slider for Starting Number -->
    <div class="w-full flex items-center justify-between gap-3 mt-3 px-2">
        <span class="text-xs text-slate-400">Start Number:</span>
        <input type="range" id="s6StartSlider" min="1" max="25" value="4" oninput="s6UpdateStart(this.value)" class="flex-1 accent-rose-400 cursor-pointer">
        <span id="s6StartVal" class="font-mono text-rose-300 font-bold text-xs w-8 text-right">4</span>
    </div>
</div>
"""

# Simulator 7: Longest Route (North-South Corridor Map & Leg Adder)
sims_1_to_8[7] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            North-South Corridor Leg Adder
        </span>
        <span id="s7RouteReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            Total Distance: 3,740 km
        </span>
    </div>

    <!-- Route Schematic SVG -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s7Svg" viewBox="-120 -80 240 160" class="w-full h-full drop-shadow-md">
            <!-- Corridor Vertical Path -->
            <line x1="0" y1="-60" x2="0" y2="60" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>

            <!-- Stations -->
            <!-- Srinagar (Top) -->
            <circle cx="0" cy="-60" r="8" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
            <text x="14" y="-56" font-size="11" font-weight="bold" fill="#fca5a5">Srinagar (J&K)</text>

            <!-- Delhi -->
            <circle cx="0" cy="-20" r="7" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
            <text x="14" y="-16" font-size="10" font-weight="bold" fill="#93c5fd">Delhi (810 km)</text>

            <!-- Nagpur -->
            <circle cx="0" cy="20" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
            <text x="14" y="24" font-size="10" font-weight="bold" fill="#6ee7b7">Nagpur (1,080 km)</text>

            <!-- Kanyakumari (Bottom) -->
            <circle cx="0" cy="60" r="8" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
            <text x="14" y="64" font-size="11" font-weight="bold" fill="#fde047">Kanyakumari (1,850 km)</text>
        </svg>
    </div>

    <!-- 4-Digit Column Addition Display -->
    <div class="w-full max-w-[300px] p-2.5 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs text-center my-1">
        <div class="text-slate-400">Leg 1 (Srinagar → Delhi): 810 km</div>
        <div class="text-slate-400">Leg 2 (Delhi → Nagpur): 1,080 km</div>
        <div class="text-slate-400 border-b border-slate-800 pb-1">+ Leg 3 (Nagpur → Kanyakumari): 1,850 km</div>
        <div class="text-amber-300 font-bold pt-1">Total Expedition = 3,740 km</div>
    </div>

    <div class="w-full flex justify-center mt-2">
        <button onclick="s7AnimateRoute()" class="px-4 py-1.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            Trace Complete Corridor Journey 🚗
        </button>
    </div>
</div>
"""

# Simulator 8: Route Distances (Sea & Coastal Route Subtraction)
sims_1_to_8[8] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Maritime Port Distance Subtractor
        </span>
        <span id="s8SavingReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            Saved: 1,075 Nautical Miles
        </span>
    </div>

    <!-- Port Schematic SVG -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s8Svg" viewBox="-130 -80 260 160" class="w-full h-full drop-shadow-md">
            <!-- Peninsular Outline Hint -->
            <path d="M -80,-50 L 0,60 L 80,-50" fill="none" stroke="#334155" stroke-width="12" stroke-linejoin="round"/>
            
            <!-- Longer Outer Route (Red Dashed) -->
            <path d="M -80,-50 Q -110,70 0,75 Q 110,70 80,-50" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6 3"/>
            <text x="0" y="95" text-anchor="middle" font-size="10" fill="#fca5a5">Long Route: 3,240 nm</text>

            <!-- Shorter Direct Coastal Route (Green Solid) -->
            <path d="M -80,-50 L 0,55 L 80,-50" fill="none" stroke="#10b981" stroke-width="4"/>
            <text x="0" y="40" text-anchor="middle" font-size="10" font-weight="bold" fill="#6ee7b7">Direct Route: 2,165 nm</text>

            <!-- Port Markers -->
            <!-- Mumbai -->
            <circle cx="-80" cy="-50" r="7" fill="#38bdf8"/>
            <text x="-85" y="-62" font-size="10" font-weight="bold" fill="#7dd3fc">Mumbai</text>

            <!-- Cochin -->
            <circle cx="0" cy="55" r="7" fill="#fbbf24"/>
            <text x="12" y="58" font-size="10" font-weight="bold" fill="#fde047">Cochin</text>

            <!-- Chennai -->
            <circle cx="80" cy="-50" r="7" fill="#38bdf8"/>
            <text x="50" y="-62" font-size="10" font-weight="bold" fill="#7dd3fc">Chennai</text>
        </svg>
    </div>

    <!-- Subtraction Breakdown -->
    <div class="w-full max-w-[300px] p-2.5 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs text-center my-1">
        <div class="text-slate-400">Outer Route: 3,240 nautical miles</div>
        <div class="text-slate-400 border-b border-slate-800 pb-1">- Direct Route: 2,165 nautical miles</div>
        <div class="text-emerald-400 font-bold pt-1">Distance Saved = 1,075 nautical miles!</div>
    </div>

    <div class="w-full flex justify-center mt-2">
        <button onclick="s8ToggleRoutes()" class="px-4 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/40 rounded-lg text-xs font-bold transition">
            Compare Sea Route Efficiency ⚓
        </button>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 1 to 8. Count: {len(sims_1_to_8)}")


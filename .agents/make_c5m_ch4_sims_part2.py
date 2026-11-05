#!/usr/bin/env python3
"""
Generate Simulators 9 to 16 for NCERT Class 5 Mathematics - Chapter 4: We the Travellers - II
"""

sims_9_to_16 = {}

# Simulator 9: Mental Math (Shortcut Engine)
sims_9_to_16[9] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Mental Shortcut Engine
        </span>
        <span id="s9ShortcutReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            345 + 99 = 444 (+100 - 1)
        </span>
    </div>

    <!-- Strategy Tabs -->
    <div class="w-full grid grid-cols-3 gap-1.5 mb-2">
        <button id="s9TabAdd99" onclick="s9SetStrategy('add99')" class="px-2 py-1 bg-teal-500/30 text-teal-200 border border-teal-500/40 rounded text-xs font-bold transition">
            + 99 (+100 - 1)
        </button>
        <button id="s9TabSub99" onclick="s9SetStrategy('sub99')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            - 99 (-100 + 1)
        </button>
        <button id="s9TabAdd999" onclick="s9SetStrategy('add999')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            + 999 (+1000 - 1)
        </button>
    </div>

    <!-- Visual Stepper Cards -->
    <div class="w-full p-4 bg-slate-850 rounded-xl border border-slate-700 my-2 text-center">
        <div id="s9OriginalExpr" class="text-lg font-mono font-bold text-white mb-2">345 + 99 = ?</div>
        <div class="flex items-center justify-center gap-2 text-xs font-mono">
            <span id="s9Step1Box" class="px-3 py-1.5 bg-slate-900 border border-slate-700 rounded-lg text-slate-300">
                Step 1: 345 + 100 = 445
            </span>
            <span class="text-teal-400 font-bold">➔</span>
            <span id="s9Step2Box" class="px-3 py-1.5 bg-emerald-950/60 border border-emerald-500/40 rounded-lg text-emerald-300 font-bold">
                Step 2: 445 - 1 = 444!
            </span>
        </div>
    </div>

    <!-- Number Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Starting Number:</span>
        <input type="range" id="s9Slider" min="150" max="850" value="345" oninput="s9UpdateNumber(this.value)" class="flex-1 accent-teal-400 cursor-pointer">
        <span id="s9NumVal" class="font-mono text-teal-300 font-bold text-xs w-10 text-right">345</span>
    </div>
</div>
"""

# Simulator 10: Palindrome Numbers (Symmetry Detector & Reverse-and-Add)
sims_9_to_16[10] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Palindrome Symmetry Inspector
        </span>
        <span id="s10PalinBadge" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            484 is a PALINDROME!
        </span>
    </div>

    <!-- Odometer Digits Display -->
    <div class="w-full max-w-[300px] flex items-center justify-center gap-2 p-4 bg-slate-950 rounded-xl border border-slate-800 my-2">
        <div id="s10D1" class="w-12 h-14 bg-slate-800 border-2 border-purple-400 rounded-lg flex items-center justify-center font-mono font-extrabold text-2xl text-purple-300 shadow">4</div>
        <div id="s10D2" class="w-12 h-14 bg-slate-800 border-2 border-purple-400 rounded-lg flex items-center justify-center font-mono font-extrabold text-2xl text-purple-300 shadow">8</div>
        <div id="s10D3" class="w-12 h-14 bg-slate-800 border-2 border-purple-400 rounded-lg flex items-center justify-center font-mono font-extrabold text-2xl text-purple-300 shadow">4</div>
    </div>

    <!-- Reverse-and-Add Demonstration Box -->
    <div class="w-full max-w-[320px] p-3 bg-slate-850 rounded-xl border border-slate-700 text-xs font-mono my-2 text-center">
        <div class="text-slate-400">Reverse-and-Add Engine:</div>
        <div id="s10ReverseCalc" class="text-emerald-300 font-bold mt-1">
            52 + 25 = 77 (Instant Palindrome!)
        </div>
    </div>

    <!-- Palindrome Presets -->
    <div class="w-full grid grid-cols-4 gap-1.5 mt-2">
        <button onclick="s10CheckNum('484')" class="px-2 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            484
        </button>
        <button onclick="s10CheckNum('363')" class="px-2 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            363
        </button>
        <button onclick="s10CheckNum('8558')" class="px-2 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            8,558
        </button>
        <button onclick="s10CheckNum('348')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold">
            348 (Not)
        </button>
    </div>
</div>
"""

# Simulator 11: Grid Puzzles (3×3 Monotonic Increasing Grid)
sims_9_to_16[11] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-indigo-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-indigo-400 animate-pulse"></span>
            3×3 Monotonic Grid Solver
        </span>
        <span id="s11GridStatus" class="font-mono bg-indigo-950/80 px-2.5 py-1 rounded-md text-indigo-300 border border-indigo-500/30 font-bold">
            Standard Order: VALID
        </span>
    </div>

    <!-- 3x3 Grid Display -->
    <div class="grid grid-cols-3 gap-2 p-3 bg-slate-950 rounded-xl border border-slate-800 my-2">
        <div id="s11Cell1" class="w-14 h-14 bg-emerald-950/60 border-2 border-emerald-400 rounded-lg flex items-center justify-center font-mono font-extrabold text-xl text-emerald-300">1</div>
        <div id="s11Cell2" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">2</div>
        <div id="s11Cell3" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">3</div>
        <div id="s11Cell4" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">4</div>
        <div id="s11Cell5" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">5</div>
        <div id="s11Cell6" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">6</div>
        <div id="s11Cell7" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">7</div>
        <div id="s11Cell8" class="w-14 h-14 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center font-mono font-bold text-xl text-white">8</div>
        <div id="s11Cell9" class="w-14 h-14 bg-emerald-950/60 border-2 border-emerald-400 rounded-lg flex items-center justify-center font-mono font-extrabold text-xl text-emerald-300">9</div>
    </div>

    <!-- Preset Solution Switcher -->
    <div class="w-full grid grid-cols-2 gap-2 mt-2">
        <button onclick="s11SetLayout('standard')" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded-lg text-xs font-bold transition">
            Solution A: Standard [1-9]
        </button>
        <button onclick="s11SetLayout('alternate')" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded-lg text-xs font-bold transition">
            Solution B: Diagonal [1,2,4...]
        </button>
    </div>
</div>
"""

# Simulator 12: Even and Odd (Paired Dots & Addition Parity Workbench)
sims_9_to_16[12] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-cyan-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
            Paired Dots Parity Workbench
        </span>
        <span id="s12ParityStatus" class="font-mono bg-cyan-950/80 px-2.5 py-1 rounded-md text-cyan-300 border border-cyan-500/30 font-bold">
            Odd (5) + Odd (7) = Even (12)
        </span>
    </div>

    <!-- Visual Dot Array Container -->
    <div class="w-full max-w-[320px] p-4 bg-slate-950 rounded-xl border border-slate-800 my-2 flex flex-col gap-3">
        <!-- Number 1 Dots -->
        <div>
            <div class="text-[10px] text-cyan-400 font-bold uppercase mb-1">Number A: <span id="s12NumALabel">5 (Odd - 1 Leftover)</span></div>
            <div id="s12DotsA" class="flex flex-wrap gap-1.5"></div>
        </div>
        <!-- Number 2 Dots -->
        <div>
            <div class="text-[10px] text-amber-400 font-bold uppercase mb-1">Number B: <span id="s12NumBLabel">7 (Odd - 1 Leftover)</span></div>
            <div id="s12DotsB" class="flex flex-wrap gap-1.5"></div>
        </div>
    </div>

    <!-- Parity Laws Rule Bar -->
    <div id="s12RuleExplanation" class="w-full p-2.5 bg-slate-850 rounded-xl border border-slate-700 text-xs font-medium text-center text-slate-300">
        Both numbers have 1 leftover dot. When added together, the 2 leftover dots form a pair, making the total sum strictly EVEN!
    </div>

    <!-- Quick Buttons for Parity Pairs -->
    <div class="w-full grid grid-cols-3 gap-1.5 mt-2">
        <button onclick="s12SetNumbers(5, 7)" class="px-2 py-1.5 bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-200 border border-cyan-500/30 rounded text-xs font-bold">
            Odd + Odd (5+7)
        </button>
        <button onclick="s12SetNumbers(4, 6)" class="px-2 py-1.5 bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-200 border border-cyan-500/30 rounded text-xs font-bold">
            Even + Even (4+6)
        </button>
        <button onclick="s12SetNumbers(4, 5)" class="px-2 py-1.5 bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-200 border border-cyan-500/30 rounded text-xs font-bold">
            Even + Odd (4+5)
        </button>
    </div>
</div>
"""

# Simulator 13: Logic Puzzles (Coin Combinations & Torch Switch)
sims_9_to_16[13] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            Logic Puzzles: Coins & Switches
        </span>
        <span id="s13PuzzleReadout" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            ₹ 25 = 10×₹2 + 1×₹5
        </span>
    </div>

    <!-- Two-Panel Puzzle Grid -->
    <div class="w-full grid grid-cols-2 gap-3 my-2">
        <!-- Coin Combinator -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
            <div class="text-[10px] font-bold text-amber-400 uppercase mb-1">🪙 Make ₹ 25</div>
            <div id="s13CoinsDisplay" class="font-mono text-xs text-slate-300 my-2">
                10 × ₹ 2 + 1 × ₹ 5 = ₹ 25
            </div>
            <button onclick="s13CycleCoins()" class="px-2.5 py-1 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 rounded text-xs font-bold">
                Next Combo 🔄
            </button>
        </div>

        <!-- Torch Switch -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center flex flex-col items-center justify-between">
            <div class="text-[10px] font-bold text-cyan-400 uppercase mb-1">🔦 Torch Switch</div>
            <div id="s13TorchBeam" class="w-8 h-8 rounded-full bg-slate-800 border-2 border-slate-700 flex items-center justify-center font-bold text-xs text-slate-500 my-1">
                OFF
            </div>
            <div class="text-[10px] text-slate-400">Presses: <span id="s13PressCount" class="font-bold text-white">0</span></div>
            <button onclick="s13PressTorch()" class="px-2.5 py-1 bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 border border-cyan-500/30 rounded text-xs font-bold mt-1">
                Press Button 🔘
            </button>
        </div>
    </div>
</div>
"""

# Simulator 14: Mountain Peaks (Priyanka Mohite Himalayan Elevation Chart)
sims_9_to_16[14] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Priyanka Mohite Peaks Elevation Chart
        </span>
        <span id="s14DiffBadge" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            Everest - Annapurna = 758 m
        </span>
    </div>

    <!-- Altitude Bar Chart SVG -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s14Svg" viewBox="-20 -100 280 140" class="w-full h-full drop-shadow-md">
            <!-- Ground Baseline at 8,000m -->
            <line x1="0" y1="20" x2="260" y2="20" stroke="#475569" stroke-width="2"/>
            <text x="260" y="24" font-size="8" fill="#64748b">8,000m Base</text>

            <!-- Everest: 8,849m (height 85) -->
            <rect x="15" y="-65" width="30" height="85" fill="#f59e0b" rx="2"/>
            <text x="30" y="-70" text-anchor="middle" font-size="9" font-weight="bold" fill="#fde047">8,849</text>
            <text x="30" y="32" text-anchor="middle" font-size="8" fill="#cbd5e1">Everest</text>

            <!-- Kanchenjunga: 8,586m (height 58) -->
            <rect x="65" y="-38" width="30" height="58" fill="#3b82f6" rx="2"/>
            <text x="80" y="-43" text-anchor="middle" font-size="9" font-weight="bold" fill="#93c5fd">8,586</text>
            <text x="80" y="32" text-anchor="middle" font-size="8" fill="#cbd5e1">Kanchen</text>

            <!-- Lhotse: 8,516m (height 51) -->
            <rect x="115" y="-31" width="30" height="51" fill="#10b981" rx="2"/>
            <text x="130" y="-36" text-anchor="middle" font-size="9" font-weight="bold" fill="#6ee7b7">8,516</text>
            <text x="130" y="32" text-anchor="middle" font-size="8" fill="#cbd5e1">Lhotse</text>

            <!-- Makalu: 8,485m (height 48) -->
            <rect x="165" y="-28" width="30" height="48" fill="#8b5cf6" rx="2"/>
            <text x="180" y="-33" text-anchor="middle" font-size="9" font-weight="bold" fill="#c4b5fd">8,485</text>
            <text x="180" y="32" text-anchor="middle" font-size="8" fill="#cbd5e1">Makalu</text>

            <!-- Annapurna: 8,091m (height 9) -->
            <rect x="215" y="11" width="30" height="9" fill="#ef4444" rx="2"/>
            <text x="230" y="6" text-anchor="middle" font-size="9" font-weight="bold" fill="#fca5a5">8,091</text>
            <text x="230" y="32" text-anchor="middle" font-size="8" fill="#cbd5e1">Anna</text>
        </svg>
    </div>

    <!-- Quick Compare Buttons -->
    <div class="w-full grid grid-cols-3 gap-1.5 mt-2">
        <button onclick="s14Compare(8849, 8091, 'Everest', 'Annapurna')" class="px-2 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold">
            Everest - Anna (758m)
        </button>
        <button onclick="s14Compare(8849, 8586, 'Everest', 'Kanchenjunga')" class="px-2 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold">
            Everest - Kanchen (263m)
        </button>
        <button onclick="s14Compare(8516, 8091, 'Lhotse', 'Annapurna')" class="px-2 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold">
            Lhotse - Anna (425m)
        </button>
    </div>
</div>
"""

# Simulator 15: Math Mela (Event Review Dashboard)
sims_9_to_16[15] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Math Metric Mela Dashboard
        </span>
        <span id="s15MelaBadge" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            Certificates: 625 Remaining
        </span>
    </div>

    <!-- Event Cards Grid -->
    <div class="w-full grid grid-cols-3 gap-2 my-2 text-center text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Certificates</div>
            <div class="text-sm font-bold text-white mt-1">2,500 - 1,875</div>
            <div class="text-xs font-extrabold text-teal-400 mt-1">= 625 Left</div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Cricket Score</div>
            <div class="text-sm font-bold text-white mt-1">348 + 295</div>
            <div class="text-xs font-extrabold text-amber-400 mt-1">= 643 Runs</div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-[10px] text-slate-400 font-bold uppercase">Weekly Savings</div>
            <div class="text-sm font-bold text-white mt-1">45 + 60 + 75</div>
            <div class="text-xs font-extrabold text-emerald-400 mt-1">= ₹ 180</div>
        </div>
    </div>
</div>
"""

# Simulator 16: Travel Lab (Integrated Multi-Leg Expedition Sandbox)
sims_9_to_16[16] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Travel Arithmetic Expedition Sandbox
        </span>
        <span id="s16ExpeditionCost" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            Total Fuel Cost: ₹ 2,700
        </span>
    </div>

    <!-- Route Selector -->
    <div class="w-full grid grid-cols-3 gap-1.5 mb-2">
        <button id="s16R1" onclick="s16SelectRoute(450, 'Delhi → Jaipur')" class="px-2 py-1 bg-blue-500/30 text-blue-200 border border-blue-500/40 rounded text-xs font-bold transition">
            Delhi → Jaipur (450 km)
        </button>
        <button id="s16R2" onclick="s16SelectRoute(1200, 'Mumbai → Goa')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            Mumbai → Goa (1,200 km)
        </button>
        <button id="s16R3" onclick="s16SelectRoute(2400, 'Kolkata → Chennai')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            Kolkata → Chennai (2,400 km)
        </button>
    </div>

    <!-- Expedition Metrics Grid -->
    <div class="w-full p-3 bg-slate-950 rounded-xl border border-slate-800 my-2 grid grid-cols-3 gap-2 text-center text-xs">
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Distance</div>
            <div id="s16DistVal" class="text-sm font-extrabold text-white mt-0.5">450 km</div>
        </div>
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Fuel Used (15 km/L)</div>
            <div id="s16FuelVal" class="text-sm font-extrabold text-amber-400 mt-0.5">30 Litres</div>
        </div>
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Cost (@ ₹90/L)</div>
            <div id="s16CostVal" class="text-sm font-extrabold text-emerald-400 mt-0.5">₹ 2,700</div>
        </div>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 9 to 16. Count: {len(sims_9_to_16)}")


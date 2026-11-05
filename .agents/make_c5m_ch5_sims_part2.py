#!/usr/bin/env python3
"""
Generate Simulators 9 to 16 for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""

sims_9_to_16 = {}

# Simulator 9: Millimetre Scale (Magnifying Glass Ruler Zoomer)
sims_9_to_16[9] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Millimetre Precision Ruler Zoomer
        </span>
        <span id="s9MmReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            1 cm = 10 mm (Tick: 6 mm)
        </span>
    </div>

    <!-- SVG Ruler with Zoom Lens -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s9Svg" viewBox="-20 -60 280 140" class="w-full h-full drop-shadow-md">
            <!-- Ruler Base (0 to 3 cm) -->
            <rect x="0" y="0" width="240" height="40" fill="#1e293b" stroke="#0d9488" stroke-width="2" rx="4"/>
            
            <!-- Ticks for 0 to 3 cm (80px per cm) -->
            <!-- 0 cm -->
            <line x1="0" y1="0" x2="0" y2="25" stroke="#2dd4bf" stroke-width="2.5"/>
            <text x="0" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#2dd4bf">0</text>
            <!-- 1 cm (x=80) -->
            <line x1="80" y1="0" x2="80" y2="25" stroke="#2dd4bf" stroke-width="2.5"/>
            <text x="80" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#2dd4bf">1 cm</text>
            <!-- 2 cm (x=160) -->
            <line x1="160" y1="0" x2="160" y2="25" stroke="#2dd4bf" stroke-width="2.5"/>
            <text x="160" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#2dd4bf">2 cm</text>
            <!-- 3 cm (x=240) -->
            <line x1="240" y1="0" x2="240" y2="25" stroke="#2dd4bf" stroke-width="2.5"/>
            <text x="240" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#2dd4bf">3 cm</text>

            <!-- 10 mm ticks inside 0 to 1 cm -->
            <g id="s9MmTicks"></g>

            <!-- Interactive Arrow Pointer -->
            <g id="s9ArrowGroup" transform="translate(48, 0)">
                <line x1="0" y1="-25" x2="0" y2="-2" stroke="#f59e0b" stroke-width="3"/>
                <polygon points="0,0 -4,-8 4,-8" fill="#f59e0b"/>
                <text id="s9ArrowText" x="0" y="-30" text-anchor="middle" font-size="10" font-weight="bold" fill="#fbbf24">6 mm</text>
            </g>
        </svg>
    </div>

    <!-- Mm Stepper Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Position (mm):</span>
        <input type="range" id="s9Slider" min="1" max="29" value="6" oninput="s9SetMm(this.value)" class="flex-1 accent-teal-400 cursor-pointer">
        <span id="s9SliderVal" class="font-mono text-teal-300 font-bold text-xs w-16 text-right">6 mm</span>
    </div>
</div>
"""

# Simulator 10: Seed Growth (4-Day Sprout Growth Lab)
sims_9_to_16[10] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            4-Day Sprout Growth Tracker
        </span>
        <span id="s10DayReadout" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            Day 3: 15 mm (1 cm 5 mm)
        </span>
    </div>

    <!-- SVG Sprout & Ruler -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s10Svg" viewBox="-30 -80 260 140" class="w-full h-full drop-shadow-md">
            <!-- Calibrated Vertical Millimetre Ruler -->
            <rect x="0" y="-60" width="30" height="110" fill="#1e293b" stroke="#334155" rx="3"/>
            <!-- 0 mark at y=30 -->
            <line x1="0" y1="30" x2="25" y2="30" stroke="#cbd5e1" stroke-width="2"/>
            <text x="28" y="33" font-size="8" fill="#94a3b8">0</text>
            <!-- 10mm (1cm) at y=0 -->
            <line x1="0" y1="0" x2="25" y2="0" stroke="#cbd5e1" stroke-width="2"/>
            <text x="28" y="3" font-size="8" fill="#94a3b8">1cm</text>
            <!-- 20mm (2cm) at y=-30 -->
            <line x1="0" y1="-30" x2="25" y2="-30" stroke="#cbd5e1" stroke-width="2"/>
            <text x="28" y="-27" font-size="8" fill="#94a3b8">2cm</text>

            <!-- Chana / Moong Seed Body at (90, 30) -->
            <ellipse cx="90" cy="30" rx="14" ry="10" fill="#92400e" stroke="#78350f" stroke-width="2"/>
            <circle cx="85" cy="27" r="2" fill="#ffffff" opacity="0.6"/>

            <!-- Extending Sprout Radicle -->
            <path id="s10Radicle" d="M 85,24 Q 75,10 75,-15" fill="none" stroke="#84cc16" stroke-width="4" stroke-linecap="round"/>
            <!-- Sprout Tip -->
            <circle id="s10Tip" cx="75" cy="-15" r="3.5" fill="#a3e635"/>

            <!-- Dimension Line -->
            <line x1="50" y1="30" x2="50" y2="-15" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 2"/>
            <text id="s10DimText" x="45" y="10" text-anchor="end" font-size="10" font-weight="bold" fill="#fde047">15 mm</text>
        </svg>
    </div>

    <!-- 4 Day Buttons -->
    <div class="w-full grid grid-cols-4 gap-1.5 mt-2">
        <button onclick="s10SetDay(1, 3)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold transition">
            Day 1 (3 mm)
        </button>
        <button onclick="s10SetDay(2, 8)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold transition">
            Day 2 (8 mm)
        </button>
        <button onclick="s10SetDay(3, 15)" class="px-2 py-1.5 bg-emerald-500/30 text-emerald-200 border border-emerald-500/40 rounded text-xs font-bold transition">
            Day 3 (15 mm)
        </button>
        <button onclick="s10SetDay(4, 24)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold transition">
            Day 4 (24 mm)
        </button>
    </div>
</div>
"""

# Simulator 11: Precision Lines (Virtual Drafting Table)
sims_9_to_16[11] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-indigo-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-indigo-400 animate-pulse"></span>
            Virtual Drafting Table Line Drawer
        </span>
        <span id="s11LineReadout" class="font-mono bg-indigo-950/80 px-2.5 py-1 rounded-md text-indigo-300 border border-indigo-500/30 font-bold">
            Drawn Line: 5 cm 5 mm (55 mm)
        </span>
    </div>

    <!-- Drawing Board SVG -->
    <div class="relative w-full max-w-[340px] aspect-[5/3] flex items-center justify-center my-2">
        <svg id="s11Svg" viewBox="-20 -40 280 100" class="w-full h-full drop-shadow-md">
            <!-- Background Grid paper -->
            <rect x="0" y="-30" width="240" height="80" fill="#0f172a" stroke="#334155" stroke-dasharray="4 4"/>

            <!-- Drawn Line Segment -->
            <line id="s11DrawnLine" x1="10" y1="10" x2="175" y2="10" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
            <!-- End tick marks -->
            <line x1="10" y1="2" x2="10" y2="18" stroke="#f43f5e" stroke-width="2"/>
            <line id="s11EndTick" x1="175" y1="2" x2="175" y2="18" stroke="#f43f5e" stroke-width="2"/>

            <!-- Pencil Graphic Tip -->
            <polygon id="s11Pencil" points="175,10 185,-5 195,5" fill="#f59e0b"/>

            <text x="10" y="30" font-size="9" fill="#94a3b8">Start (0)</text>
            <text id="s11EndText" x="175" y="30" font-size="9" font-weight="bold" fill="#fda4af">5 cm 5 mm</text>
        </svg>
    </div>

    <!-- Line Length Presets -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s11Draw(36, '3 cm 6 mm')" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            36 mm (3 cm 6 mm)
        </button>
        <button onclick="s11Draw(55, '5 cm 5 mm')" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            55 mm (5 cm 5 mm)
        </button>
        <button onclick="s11Draw(72, '7 cm 2 mm')" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            72 mm (7 cm 2 mm)
        </button>
    </div>
</div>
"""

# Simulator 12: Adding Lengths (Column Addition with Metric Regrouping)
sims_9_to_16[12] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Mixed Unit Column Addition
        </span>
        <span id="s12AddReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            4 m 65 cm + 3 m 55 cm
        </span>
    </div>

    <!-- Column Addition Table -->
    <div class="w-full max-w-[300px] p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs my-2">
        <div class="grid grid-cols-3 text-center text-amber-400 font-bold pb-1 border-b border-slate-800">
            <span>Carry:</span>
            <span id="s12CarryM">+1 m</span>
            <span>-</span>
        </div>
        <div class="grid grid-cols-3 text-center text-slate-400 font-bold py-1 border-b border-slate-800">
            <span></span>
            <span>Metres (m)</span>
            <span>Centimetres (cm)</span>
        </div>
        <div class="grid grid-cols-3 text-center text-white py-1">
            <span></span>
            <span>4</span>
            <span>65</span>
        </div>
        <div class="grid grid-cols-3 text-center text-white py-1 border-b-2 border-slate-700">
            <span class="text-amber-400 font-bold">+</span>
            <span>3</span>
            <span>55</span>
        </div>
        <div class="grid grid-cols-3 text-center text-emerald-400 font-extrabold text-sm pt-1">
            <span>=</span>
            <span id="s12ResM">8 m</span>
            <span id="s12ResCm">20 cm</span>
        </div>
    </div>

    <!-- Regrouping Note -->
    <div class="w-full p-2 bg-slate-850 rounded-lg border border-slate-700 text-center font-mono text-[11px] text-slate-300">
        65 cm + 55 cm = 120 cm = 1 m 20 cm. (Write 20 cm, carry 1 m to metres column!)
    </div>
</div>
"""

# Simulator 13: Subtracting Lengths (Ribbon Subtraction with Borrowing)
sims_9_to_16[13] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-rose-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-rose-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-rose-400 animate-pulse"></span>
            Ribbon Cutting Subtraction with Borrowing
        </span>
        <span id="s13SubReadout" class="font-mono bg-rose-950/80 px-2.5 py-1 rounded-md text-rose-300 border border-rose-500/30 font-bold">
            6 m 00 cm - 2 m 45 cm = 3 m 55 cm
        </span>
    </div>

    <!-- Column Subtraction Box -->
    <div class="w-full max-w-[300px] p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs my-2 text-center">
        <div class="text-amber-400 pb-1 border-b border-slate-800">
            Borrow 1 m as 100 cm: 6 m becomes 5 m, 0 cm becomes 100 cm
        </div>
        <div class="py-1 text-slate-200">
            Centimetres: 100 cm - 45 cm = 55 cm<br>
            Metres: 5 m - 2 m = 3 m
        </div>
        <div class="pt-1 text-emerald-400 font-bold border-t border-slate-800">
            Remaining Ribbon = 3 m 55 cm | Check: 3m 55cm + 2m 45cm = 6m
        </div>
    </div>
</div>
"""

# Simulator 14: Scaling Lengths (Shirt Fabric Multiplier)
sims_9_to_16[14] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Shirt Fabric Scaling Calculator
        </span>
        <span id="s14ScaleReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            4 Shirts × (2 m 25 cm) = 9 Metres
        </span>
    </div>

    <!-- Visual Dashboard -->
    <div class="w-full p-3 bg-slate-950 rounded-xl border border-slate-800 my-2 grid grid-cols-3 gap-2 text-center text-xs">
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Shirts</div>
            <div id="s14ShirtsCount" class="text-base font-extrabold text-white mt-0.5">4 Shirts</div>
        </div>
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Per Shirt</div>
            <div class="text-base font-extrabold text-amber-400 mt-0.5">2 m 25 cm</div>
        </div>
        <div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Total Fabric</div>
            <div id="s14TotalCloth" class="text-base font-extrabold text-emerald-400 mt-0.5">9 m 00 cm</div>
        </div>
    </div>

    <!-- Shirts Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Number of Shirts:</span>
        <input type="range" id="s14Slider" min="1" max="8" value="4" oninput="s14Update(this.value)" class="flex-1 accent-amber-400 cursor-pointer">
        <span id="s14SliderVal" class="font-mono text-amber-300 font-bold text-xs w-14 text-right">4 shirts</span>
    </div>
</div>
"""

# Simulator 15: Height Estimation (Urban Benchmark Stacker)
sims_9_to_16[15] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Urban Height Benchmark Stacker
        </span>
        <span id="s15EstReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            3-Storey School ≈ 9 to 10 m
        </span>
    </div>

    <!-- Benchmark Cards -->
    <div class="w-full grid grid-cols-3 gap-2 my-2 text-center text-xs">
        <div class="p-2.5 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-lg mb-1">🚪</div>
            <div class="font-bold text-white">Classroom Door</div>
            <div class="text-teal-400 font-bold mt-1">~2 Metres</div>
        </div>
        <div class="p-2.5 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-lg mb-1">🏢</div>
            <div class="font-bold text-white">Building Storey</div>
            <div class="text-teal-400 font-bold mt-1">~3 Metres</div>
        </div>
        <div class="p-2.5 bg-slate-950 rounded-xl border border-slate-800">
            <div class="text-lg mb-1">💡</div>
            <div class="font-bold text-white">Streetlight Pole</div>
            <div class="text-teal-400 font-bold mt-1">~6 Metres</div>
        </div>
    </div>
</div>
"""

# Simulator 16: Feet and Inches (Dual Imperial-Metric Wall Chart)
sims_9_to_16[16] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Wall Height Chart: Feet & Inches vs Centimetres
        </span>
        <span id="s16DualHeightReadout" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            4 ft 4 in ≈ 132 cm
        </span>
    </div>

    <!-- SVG Wall Chart -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s16Svg" viewBox="-40 -80 280 140" class="w-full h-full drop-shadow-md">
            <!-- Wall Background -->
            <rect x="0" y="-70" width="120" height="120" fill="#1e293b" stroke="#475569" stroke-width="2"/>

            <!-- Left Scale: Feet -->
            <line x1="0" y1="50" x2="0" y2="-70" stroke="#a855f7" stroke-width="3"/>
            <!-- 3ft (y=30), 4ft (y=-10), 5ft (y=-50) -->
            <line x1="0" y1="30" x2="10" y2="30" stroke="#a855f7" stroke-width="2"/>
            <text x="-6" y="34" text-anchor="end" font-size="9" fill="#c084fc">3 ft</text>
            <line x1="0" y1="-10" x2="10" y2="-10" stroke="#a855f7" stroke-width="2"/>
            <text x="-6" y="-6" text-anchor="end" font-size="9" fill="#c084fc">4 ft</text>
            <line x1="0" y1="-50" x2="10" y2="-50" stroke="#a855f7" stroke-width="2"/>
            <text x="-6" y="-46" text-anchor="end" font-size="9" fill="#c084fc">5 ft</text>

            <!-- Right Scale: cm -->
            <line x1="120" y1="50" x2="120" y2="-70" stroke="#10b981" stroke-width="3"/>
            <text x="126" y="34" font-size="9" fill="#6ee7b7">90 cm</text>
            <text x="126" y="-6" font-size="9" fill="#6ee7b7">120 cm</text>
            <text x="126" y="-46" font-size="9" fill="#6ee7b7">150 cm</text>

            <!-- Height Bar Cursor -->
            <line id="s16Cursor" x1="0" y1="-23" x2="120" y2="-23" stroke="#f59e0b" stroke-width="3"/>
            <polygon points="120,-23 126,-28 126,-18" fill="#f59e0b"/>
            <text id="s16HeightText" x="60" y="-30" text-anchor="middle" font-size="11" font-weight="bold" fill="#fde047">4 ft 4 in (132 cm)</text>
        </svg>
    </div>

    <!-- Height Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Student Height:</span>
        <input type="range" id="s16Slider" min="36" max="68" value="52" oninput="s16SetInches(this.value)" class="flex-1 accent-purple-400 cursor-pointer">
        <span id="s16InchesVal" class="font-mono text-purple-300 font-bold text-xs w-16 text-right">4 ft 4 in</span>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 9 to 16. Count: {len(sims_9_to_16)}")


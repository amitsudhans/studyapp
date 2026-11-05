#!/usr/bin/env python3
"""
Generate Simulators 9 to 16 for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""

sims_9_to_16 = {}

# Simulator 9: Angles Around (Everyday Object Classifier)
sims_9_to_16[9] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Everyday Object Angle Classifier
        </span>
        <span id="s9CategoryBadge" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            Acute Angle (50°)
        </span>
    </div>

    <!-- Object Tabs -->
    <div class="w-full grid grid-cols-4 gap-1.5 mb-2">
        <button id="s9TabDoor" onclick="s9SelectObject('door')" class="px-2 py-1 bg-teal-500/30 text-teal-200 border border-teal-500/40 rounded text-xs font-bold transition">
            🚪 Door
        </button>
        <button id="s9TabRoof" onclick="s9SelectObject('roof')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            ⛺ Tent
        </button>
        <button id="s9TabLaptop" onclick="s9SelectObject('laptop')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            💻 Laptop
        </button>
        <button id="s9TabSplit" onclick="s9SelectObject('split')" class="px-2 py-1 bg-slate-800 text-slate-300 border border-slate-700 rounded text-xs font-bold transition">
            🤸 Splits
        </button>
    </div>

    <!-- SVG Display -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s9Svg" viewBox="-120 -120 240 160" class="w-full h-full drop-shadow-md">
            <g id="s9ObjectArt"></g>
            <path id="s9AngleArc" d="" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
            <text id="s9AngleText" x="30" y="-15" font-size="11" font-weight="bold" fill="#fbbf24">50°</text>
        </svg>
    </div>

    <!-- Angle Control -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Object Opening:</span>
        <input type="range" id="s9Slider" min="20" max="180" value="50" oninput="s9UpdateAngle(this.value)" class="flex-1 accent-teal-400 cursor-pointer">
        <span id="s9Val" class="font-mono text-teal-300 font-bold text-xs w-10 text-right">50°</span>
    </div>
</div>
"""

# Simulator 10: Folded Tester (8-Part Circular Tracing Paper Tester)
sims_9_to_16[10] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            8-Part Folded Paper Tester
        </span>
        <span id="s10WedgesReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            Unfolded: 8 Wedges (45° Each)
        </span>
    </div>

    <!-- SVG Folded Tester -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s10Svg" viewBox="-130 -130 260 260" class="w-full h-full drop-shadow-md">
            <!-- Full Unfolded Disc with 8 Sectors -->
            <g id="s10FullDisc">
                <circle cx="0" cy="0" r="100" fill="#1e293b" stroke="#3b82f6" stroke-width="3"/>
                <!-- 8 Spoke Fold Creases -->
                <line x1="0" y1="-100" x2="0" y2="100" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 3"/>
                <line x1="-100" y1="0" x2="100" y2="0" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 3"/>
                <line x1="-70.7" y1="-70.7" x2="70.7" y2="70.7" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 3"/>
                <line x1="-70.7" y1="70.7" x2="70.7" y2="-70.7" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3 3"/>
                <!-- Sector Numbers -->
                <text x="25" y="-60" font-size="11" font-weight="bold" fill="#93c5fd">1 (45°)</text>
                <text x="60" y="-25" font-size="11" font-weight="bold" fill="#93c5fd">2</text>
                <text x="60" y="35" font-size="11" font-weight="bold" fill="#93c5fd">3</text>
                <text x="25" y="70" font-size="11" font-weight="bold" fill="#93c5fd">4</text>
                <text x="-35" y="70" font-size="11" font-weight="bold" fill="#93c5fd">5</text>
                <text x="-70" y="35" font-size="11" font-weight="bold" fill="#93c5fd">6</text>
                <text x="-70" y="-25" font-size="11" font-weight="bold" fill="#93c5fd">7</text>
                <text x="-35" y="-60" font-size="11" font-weight="bold" fill="#93c5fd">8</text>
            </g>

            <!-- Highlighted Wedges Arc -->
            <path id="s10WedgeHighlight" d="" fill="#3b82f6" fill-opacity="0.35"/>

            <!-- Center Pivot -->
            <circle cx="0" cy="0" r="6" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
        </svg>
    </div>

    <!-- Folding Step Buttons -->
    <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-1.5 mt-2">
        <button onclick="s10ShowStep(1)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-xs font-bold transition">
            Fold 1 (1/2 Turn)
        </button>
        <button onclick="s10ShowStep(2)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-xs font-bold transition">
            Fold 2 (1/4 Turn)
        </button>
        <button onclick="s10ShowStep(3)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-xs font-bold transition">
            Fold 3 (1/8 Turn)
        </button>
        <button onclick="s10ShowStep(0)" class="px-2 py-1.5 bg-blue-600/30 hover:bg-blue-600/40 text-blue-200 border border-blue-500/40 rounded text-xs font-bold transition">
            Unfold (8 Parts)
        </button>
    </div>

    <!-- Wedge Count Selector -->
    <div class="w-full flex items-center justify-between gap-3 mt-3 px-2">
        <span class="text-xs text-slate-400">Highlight Wedges:</span>
        <input type="range" id="s10WedgeSlider" min="1" max="8" value="2" oninput="s10SetWedges(this.value)" class="flex-1 accent-blue-400 cursor-pointer">
        <span id="s10WedgeCount" class="font-mono text-blue-300 font-bold text-xs w-16 text-right">2 (90°)</span>
    </div>
</div>
"""

# Simulator 11: Six-Part Tester (6 Equal Sectors & Straw Pointer)
sims_9_to_16[11] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Six-Part Tester with Straw Pointer
        </span>
        <span id="s11SectorReadout" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            1/6 Turn (60°)
        </span>
    </div>

    <!-- SVG Six-Part Disc -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s11Svg" viewBox="-130 -130 260 260" class="w-full h-full drop-shadow-md">
            <!-- 6 Colored Sectors of 60° each -->
            <!-- Sector 1: 0 to 60° -->
            <path d="M 0,0 L 0,-100 A 100,100 0 0,1 86.6,-50 Z" fill="#8b5cf6" fill-opacity="0.25" stroke="#a78bfa" stroke-width="1.5"/>
            <!-- Sector 2: 60 to 120° -->
            <path d="M 0,0 L 86.6,-50 A 100,100 0 0,1 86.6,50 Z" fill="#3b82f6" fill-opacity="0.25" stroke="#60a5fa" stroke-width="1.5"/>
            <!-- Sector 3: 120 to 180° -->
            <path d="M 0,0 L 86.6,50 A 100,100 0 0,1 0,100 Z" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="1.5"/>
            <!-- Sector 4: 180 to 240° -->
            <path d="M 0,0 L 0,100 A 100,100 0 0,1 -86.6,50 Z" fill="#f59e0b" fill-opacity="0.25" stroke="#fbbf24" stroke-width="1.5"/>
            <!-- Sector 5: 240 to 300° -->
            <path d="M 0,0 L -86.6,50 A 100,100 0 0,1 -86.6,-50 Z" fill="#ef4444" fill-opacity="0.25" stroke="#f87171" stroke-width="1.5"/>
            <!-- Sector 6: 300 to 360° -->
            <path d="M 0,0 L -86.6,-50 A 100,100 0 0,1 0,-100 Z" fill="#ec4899" fill-opacity="0.25" stroke="#f472b6" stroke-width="1.5"/>
            
            <!-- Sector Labels -->
            <text x="35" y="-60" font-size="10" font-weight="bold" fill="#c4b5fd">60° (1/6)</text>
            <text x="70" y="0" font-size="10" font-weight="bold" fill="#93c5fd">60°</text>
            <text x="35" y="65" font-size="10" font-weight="bold" fill="#6ee7b7">60°</text>
            <text x="-45" y="65" font-size="10" font-weight="bold" fill="#fde047">60°</text>
            <text x="-75" y="0" font-size="10" font-weight="bold" fill="#fca5a5">60°</text>
            <text x="-45" y="-60" font-size="10" font-weight="bold" fill="#fbcfe8">60°</text>

            <!-- Fixed Baseline Straw (Pointing up) -->
            <line x1="0" y1="0" x2="0" y2="-100" stroke="#94a3b8" stroke-width="5" stroke-linecap="round" stroke-dasharray="4 3"/>

            <!-- Movable Straw Pointer -->
            <g id="s11StrawPointer" transform="rotate(60)">
                <line x1="0" y1="0" x2="0" y2="-105" stroke="#fbbf24" stroke-width="6" stroke-linecap="round"/>
                <polygon points="0,-112 -6,-100 6,-100" fill="#fbbf24"/>
                <circle cx="0" cy="-90" r="3" fill="#78350f"/>
            </g>

            <!-- Split Pin Centre -->
            <circle cx="0" cy="0" r="10" fill="#0f172a" stroke="#fbbf24" stroke-width="3"/>
            <circle cx="0" cy="0" r="4" fill="#fbbf24"/>
        </svg>
    </div>

    <!-- Stepper Buttons -->
    <div class="w-full grid grid-cols-3 sm:grid-cols-6 gap-1.5 mt-2">
        <button onclick="s11SetSector(1)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            1/6 (60°)
        </button>
        <button onclick="s11SetSector(2)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            2/6 (120°)
        </button>
        <button onclick="s11SetSector(3)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            3/6 (180°)
        </button>
        <button onclick="s11SetSector(4)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            4/6 (240°)
        </button>
        <button onclick="s11SetSector(5)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            5/6 (300°)
        </button>
        <button onclick="s11SetSector(6)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 border border-purple-500/30 rounded text-xs font-bold">
            6/6 (360°)
        </button>
    </div>
</div>
"""

# Simulator 12: Combining Turns (Fraction Turn Calculator)
sims_9_to_16[12] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-indigo-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-indigo-400 animate-pulse"></span>
            Combining Fractional Turns
        </span>
        <span id="s12TotalReadout" class="font-mono bg-indigo-950/80 px-2.5 py-1 rounded-md text-indigo-300 border border-indigo-500/30 font-bold">
            Total Turn: 3/8 (135°)
        </span>
    </div>

    <!-- SVG Fraction Circle -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s12Svg" viewBox="-130 -130 260 260" class="w-full h-full drop-shadow-md">
            <!-- 8 Eighths Background Wedges -->
            <circle cx="0" cy="0" r="100" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <g id="s12EighthsLines">
                <line x1="0" y1="-100" x2="0" y2="100" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 2"/>
                <line x1="-100" y1="0" x2="100" y2="0" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 2"/>
                <line x1="-70.7" y1="-70.7" x2="70.7" y2="70.7" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 2"/>
                <line x1="-70.7" y1="70.7" x2="70.7" y2="-70.7" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 2"/>
            </g>

            <!-- Dynamic Swept Combined Arc -->
            <path id="s12CombinedWedge" d="" fill="#6366f1" fill-opacity="0.4" stroke="#818cf8" stroke-width="2"/>

            <!-- Baseline (0°) -->
            <line x1="0" y1="0" x2="0" y2="-100" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="4 3"/>

            <!-- Moving Angle Pointer -->
            <g id="s12PointerGroup" transform="rotate(135)">
                <line x1="0" y1="0" x2="0" y2="-100" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
                <polygon points="0,-106 -5,-96 5,-96" fill="#f43f5e"/>
            </g>

            <!-- Center Pivot -->
            <circle cx="0" cy="0" r="7" fill="#0f172a" stroke="#818cf8" stroke-width="3"/>
            <circle cx="0" cy="0" r="2.5" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Equation Box -->
    <div id="s12Equation" class="w-full text-center py-1.5 px-3 bg-slate-800/80 rounded-lg text-xs font-mono text-indigo-200 border border-indigo-500/30 mb-2">
        1/4 Turn + 1/8 Turn = 2/8 + 1/8 = 3/8 Turn (135° Obtuse Angle)
    </div>

    <!-- Combination Buttons -->
    <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-1.5">
        <button onclick="s12SetFormula('1/4 + 1/8', 135)" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            1/4 + 1/8 (3/8)
        </button>
        <button onclick="s12SetFormula('1/2 - 1/8', 135)" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            1/2 - 1/8 (3/8)
        </button>
        <button onclick="s12SetFormula('1/4 + 1/4', 180)" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            1/4 + 1/4 (1/2)
        </button>
        <button onclick="s12SetFormula('1/8 + 1/8', 90)" class="px-2 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-200 border border-indigo-500/30 rounded text-xs font-bold">
            1/8 + 1/8 (1/4)
        </button>
    </div>
</div>
"""

# Simulator 13: Clock Turns (Minute-Hand Rotations)
sims_9_to_16[13] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Minute-Hand Turn Clock
        </span>
        <span id="s13ClockReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            15 Min = 1/4 Turn (90°)
        </span>
    </div>

    <!-- SVG Clock Dial -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s13Svg" viewBox="-130 -130 260 260" class="w-full h-full drop-shadow-md">
            <!-- Clock Face Outer & Inner -->
            <circle cx="0" cy="0" r="110" fill="#0f172a" stroke="#d97706" stroke-width="4"/>
            <circle cx="0" cy="0" r="105" fill="#1e293b"/>

            <!-- Swept Angle Arc -->
            <path id="s13SweptWedge" d="M 0,0 L 0,-90 A 90,90 0 0,1 90,0 Z" fill="#f59e0b" fill-opacity="0.25"/>

            <!-- 12 Hour Marks & Numbers -->
            <g id="s13HourMarks"></g>

            <!-- Hour Hand (Points to 12 fixed) -->
            <line x1="0" y1="0" x2="0" y2="-55" stroke="#94a3b8" stroke-width="5" stroke-linecap="round"/>

            <!-- Minute Hand (Dynamic Rotation) -->
            <g id="s13MinuteHand" transform="rotate(90)">
                <line x1="0" y1="0" x2="0" y2="-90" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                <polygon points="0,-95 -4,-85 4,-85" fill="#f59e0b"/>
            </g>

            <!-- Center Cap -->
            <circle cx="0" cy="0" r="7" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
            <circle cx="0" cy="0" r="2.5" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Minute Presets -->
    <div class="w-full grid grid-cols-4 gap-1.5 mt-2">
        <button onclick="s13SetMinutes(15)" class="px-1.5 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold transition">
            15m (1/4 Turn)
        </button>
        <button onclick="s13SetMinutes(30)" class="px-1.5 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold transition">
            30m (1/2 Turn)
        </button>
        <button onclick="s13SetMinutes(45)" class="px-1.5 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold transition">
            45m (3/4 Turn)
        </button>
        <button onclick="s13SetMinutes(60)" class="px-1.5 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-200 border border-amber-500/30 rounded text-xs font-bold transition">
            60m (1 Turn)
        </button>
    </div>
</div>
"""

# Simulator 14: Clockwise Motion (Righty-Tighty Tap/Screw)
sims_9_to_16[14] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            Clockwise Direction: 'Righty-Tighty'
        </span>
        <span id="s14TapStatus" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            Valve Sealed Tight (Closed)
        </span>
    </div>

    <!-- SVG Tap / Screw Simulator -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s14Svg" viewBox="-120 -100 240 160" class="w-full h-full drop-shadow-md">
            <!-- Curved Clockwise Arrows (Top -> Right -> Bottom) -->
            <path d="M -50,-60 A 70,70 0 0,1 60,-30" fill="none" stroke="#10b981" stroke-width="4" stroke-dasharray="6 3"/>
            <polygon points="65,-25 58,-38 50,-30" fill="#10b981"/>
            <text x="50" y="-55" font-size="11" font-weight="bold" fill="#34d399">Clockwise (CW)</text>

            <!-- Tap Body -->
            <rect x="-20" y="0" width="40" height="50" fill="#475569" rx="4"/>
            <path d="M 20,20 L 50,20 L 50,45 L 35,45" fill="none" stroke="#475569" stroke-width="12" stroke-linejoin="round"/>
            
            <!-- Rotating Tap Handle Group -->
            <g id="s14HandleGroup" transform="rotate(0)">
                <rect x="-45" y="-14" width="90" height="14" fill="#059669" rx="4" stroke="#34d399" stroke-width="2"/>
                <circle cx="0" cy="-7" r="8" fill="#10b981"/>
            </g>

            <!-- Water Drips (hidden when tightened) -->
            <g id="s14WaterDrips" opacity="0">
                <circle cx="42" cy="55" r="4" fill="#38bdf8"/>
                <circle cx="42" cy="70" r="3" fill="#38bdf8"/>
            </g>
        </svg>
    </div>

    <!-- Tighten Actions -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s14Rotate(45)" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-200 border border-emerald-500/30 rounded-lg text-xs font-bold transition">
            Turn CW +45°
        </button>
        <button onclick="s14Rotate(90)" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-200 border border-emerald-500/30 rounded-lg text-xs font-bold transition">
            Turn CW +90°
        </button>
        <button onclick="s14Reset()" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Reset Valve
        </button>
    </div>
</div>
"""

# Simulator 15: Anti-Clockwise (Lefty-Loosey Cap/Tap Opener)
sims_9_to_16[15] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-pink-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-pink-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-pink-400 animate-pulse"></span>
            Anti-Clockwise: 'Lefty-Loosey'
        </span>
        <span id="s15Status" class="font-mono bg-pink-950/80 px-2.5 py-1 rounded-md text-pink-300 border border-pink-500/30 font-bold">
            Cap Loosened & Water Flowing!
        </span>
    </div>

    <!-- SVG Anti-Clockwise Simulator -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s15Svg" viewBox="-120 -100 240 160" class="w-full h-full drop-shadow-md">
            <!-- Curved Anti-Clockwise Arrow (Top -> Left -> Bottom) -->
            <path d="M 50,-60 A 70,70 0 0,0 -60,-30" fill="none" stroke="#ec4899" stroke-width="4" stroke-dasharray="6 3"/>
            <polygon points="-65,-25 -50,-30 -58,-38" fill="#ec4899"/>
            <text x="-95" y="-55" font-size="11" font-weight="bold" fill="#f472b6">Anti-Clockwise (ACW)</text>

            <!-- Bottle Neck & Cap -->
            <rect x="-35" y="10" width="70" height="60" fill="#334155" rx="6"/>
            <line x1="-30" y1="20" x2="30" y2="20" stroke="#64748b" stroke-width="2"/>
            <line x1="-30" y1="30" x2="30" y2="30" stroke="#64748b" stroke-width="2"/>

            <!-- Movable Cap Group -->
            <g id="s15CapGroup" transform="translate(0, 0)">
                <rect x="-40" y="-12" width="80" height="20" fill="#db2777" rx="4" stroke="#f472b6" stroke-width="2"/>
                <text x="0" y="2" text-anchor="middle" font-size="9" fill="#ffffff" font-weight="bold">BOTTLE CAP</text>
            </g>

            <!-- Flowing Splash -->
            <g id="s15Splash" opacity="1">
                <path d="M -15,70 Q 0,90 15,70" stroke="#38bdf8" stroke-width="3" fill="none"/>
                <circle cx="0" cy="78" r="4" fill="#38bdf8"/>
            </g>
        </svg>
    </div>

    <!-- Unloosen Actions -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s15Rotate(-45)" class="px-2 py-1.5 bg-pink-600/20 hover:bg-pink-600/30 text-pink-200 border border-pink-500/30 rounded-lg text-xs font-bold transition">
            Turn ACW -45°
        </button>
        <button onclick="s15Rotate(-90)" class="px-2 py-1.5 bg-pink-600/20 hover:bg-pink-600/30 text-pink-200 border border-pink-500/30 rounded-lg text-xs font-bold transition">
            Turn ACW -90°
        </button>
        <button onclick="s15Reset()" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Screw On Cap
        </button>
    </div>
</div>
"""

# Simulator 16: Compass Turns (Directional Navigation Game)
sims_9_to_16[16] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Cardinal Compass Navigation Game
        </span>
        <span id="s16HeadingReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            Facing: North (0°)
        </span>
    </div>

    <!-- SVG Compass Rose -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s16Svg" viewBox="-130 -130 260 260" class="w-full h-full drop-shadow-md">
            <!-- Compass Ring -->
            <circle cx="0" cy="0" r="105" fill="#0f172a" stroke="#0d9488" stroke-width="3"/>
            <circle cx="0" cy="0" r="98" fill="#134e4a" fill-opacity="0.2"/>

            <!-- 8 Compass Points Guidelines -->
            <line x1="0" y1="-95" x2="0" y2="95" stroke="#115e59" stroke-width="1.5"/>
            <line x1="-95" y1="0" x2="95" y2="0" stroke="#115e59" stroke-width="1.5"/>
            <line x1="-67" y1="-67" x2="67" y2="67" stroke="#115e59" stroke-width="1" stroke-dasharray="3 2"/>
            <line x1="-67" y1="67" x2="67" y2="-67" stroke="#115e59" stroke-width="1" stroke-dasharray="3 2"/>

            <!-- Cardinal Labels -->
            <text x="0" y="-108" text-anchor="middle" font-size="14" font-weight="bold" fill="#2dd4bf">N</text>
            <text x="115" y="5" text-anchor="start" font-size="14" font-weight="bold" fill="#2dd4bf">E</text>
            <text x="0" y="122" text-anchor="middle" font-size="14" font-weight="bold" fill="#2dd4bf">S</text>
            <text x="-115" y="5" text-anchor="end" font-size="14" font-weight="bold" fill="#2dd4bf">W</text>

            <text x="75" y="-75" font-size="9" fill="#5eead4">NE</text>
            <text x="75" y="80" font-size="9" fill="#5eead4">SE</text>
            <text x="-85" y="80" font-size="9" fill="#5eead4">SW</text>
            <text x="-85" y="-75" font-size="9" fill="#5eead4">NW</text>

            <!-- Rotatable Compass Needle -->
            <g id="s16Needle" transform="rotate(0)">
                <!-- North Needle (Red) -->
                <polygon points="0,-85 -10,-10 0,0" fill="#ef4444"/>
                <polygon points="0,-85 10,-10 0,0" fill="#dc2626"/>
                <!-- South Needle (Silver) -->
                <polygon points="0,85 -10,10 0,0" fill="#94a3b8"/>
                <polygon points="0,85 10,10 0,0" fill="#cbd5e1"/>
            </g>

            <!-- Center Pivot Pin -->
            <circle cx="0" cy="0" r="9" fill="#0f172a" stroke="#2dd4bf" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Direction Navigation Buttons -->
    <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-1.5 mt-2">
        <button onclick="s16Turn(90, 'CW')" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded text-xs font-bold transition">
            1/4 Turn CW (→)
        </button>
        <button onclick="s16Turn(-90, 'ACW')" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded text-xs font-bold transition">
            1/4 Turn ACW (←)
        </button>
        <button onclick="s16Turn(180, 'Half')" class="px-2 py-1.5 bg-teal-600/20 hover:bg-teal-600/30 text-teal-200 border border-teal-500/30 rounded text-xs font-bold transition">
            1/2 Turn (Opposite)
        </button>
        <button onclick="s16Reset()" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold transition">
            Reset (North)
        </button>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 9 to 16. Count: {len(sims_9_to_16)}")


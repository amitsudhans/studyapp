#!/usr/bin/env python3
"""
Generate Simulators 1 to 8 for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""

sims_1_to_8 = {}

# Simulator 1: Turning Around (Giant Wheel / Rotation Hub)
sims_1_to_8[1] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Giant Wheel Rotation Hub
        </span>
        <span id="s1TurnReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            0° (0 Turns)
        </span>
    </div>

    <!-- SVG Giant Wheel -->
    <div class="relative w-full max-w-[340px] aspect-square flex items-center justify-center my-2">
        <svg id="s1Svg" viewBox="-160 -160 320 320" class="w-full h-full drop-shadow-lg">
            <!-- Ground Base / Legs -->
            <polygon points="-50,150 0,0 50,150" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
            <line x1="-80" y1="150" x2="80" y2="150" stroke="#475569" stroke-width="6" stroke-linecap="round"/>
            
            <!-- Rotating Wheel Group -->
            <g id="s1WheelGroup">
                <!-- Outer Rim -->
                <circle cx="0" cy="0" r="110" fill="none" stroke="#f59e0b" stroke-width="5" stroke-dasharray="6 4"/>
                <circle cx="0" cy="0" r="70" fill="none" stroke="#fbbf24" stroke-width="2" opacity="0.4"/>
                
                <!-- 8 Spokes -->
                <line x1="0" y1="-110" x2="0" y2="110" stroke="#f59e0b" stroke-width="3"/>
                <line x1="-110" y1="0" x2="110" y2="0" stroke="#f59e0b" stroke-width="3"/>
                <line x1="-77.8" y1="-77.8" x2="77.8" y2="77.8" stroke="#f59e0b" stroke-width="2"/>
                <line x1="-77.8" y1="77.8" x2="77.8" y2="-77.8" stroke="#f59e0b" stroke-width="2"/>
                
                <!-- 8 Cabins -->
                <!-- Top cabin (highlighted red/gold) -->
                <g transform="translate(0, -110)">
                    <circle cx="0" cy="0" r="14" fill="#ef4444" stroke="#fef08a" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#ffffff">1</text>
                </g>
                <g transform="translate(77.8, -77.8)">
                    <circle cx="0" cy="0" r="12" fill="#3b82f6" stroke="#93c5fd" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">2</text>
                </g>
                <g transform="translate(110, 0)">
                    <circle cx="0" cy="0" r="12" fill="#10b981" stroke="#a7f3d0" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">3</text>
                </g>
                <g transform="translate(77.8, 77.8)">
                    <circle cx="0" cy="0" r="12" fill="#8b5cf6" stroke="#ddd6fe" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">4</text>
                </g>
                <g transform="translate(0, 110)">
                    <circle cx="0" cy="0" r="12" fill="#ec4899" stroke="#fbcfe8" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">5</text>
                </g>
                <g transform="translate(-77.8, 77.8)">
                    <circle cx="0" cy="0" r="12" fill="#14b8a6" stroke="#99f6e4" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">6</text>
                </g>
                <g transform="translate(-110, 0)">
                    <circle cx="0" cy="0" r="12" fill="#f97316" stroke="#fed7aa" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">7</text>
                </g>
                <g transform="translate(-77.8, -77.8)">
                    <circle cx="0" cy="0" r="12" fill="#eab308" stroke="#fef08a" stroke-width="2"/>
                    <text y="4" text-anchor="middle" font-size="9" fill="#ffffff">8</text>
                </g>
            </g>
            
            <!-- Central Pivot Axle -->
            <circle cx="0" cy="0" r="12" fill="#0f172a" stroke="#fbbf24" stroke-width="3"/>
            <circle cx="0" cy="0" r="4" fill="#fbbf24"/>
        </svg>
    </div>

    <!-- Controls -->
    <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-2 mt-2">
        <button onclick="s1SetTurn(90, '1/4 Turn')" class="px-2.5 py-1.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            1/4 Turn (90°)
        </button>
        <button onclick="s1SetTurn(180, '1/2 Turn')" class="px-2.5 py-1.5 bg-blue-500/20 hover:bg-blue-500/30 text-blue-300 border border-blue-500/40 rounded-lg text-xs font-bold transition">
            1/2 Turn (180°)
        </button>
        <button onclick="s1SetTurn(270, '3/4 Turn')" class="px-2.5 py-1.5 bg-purple-500/20 hover:bg-purple-500/30 text-purple-300 border border-purple-500/40 rounded-lg text-xs font-bold transition">
            3/4 Turn (270°)
        </button>
        <button onclick="s1SetTurn(360, '1 Full Turn')" class="px-2.5 py-1.5 bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 rounded-lg text-xs font-bold transition">
            1 Full Turn (360°)
        </button>
    </div>
    
    <div class="w-full flex items-center justify-between gap-3 mt-3 px-2">
        <span class="text-xs text-slate-400 font-medium">Free Rotation:</span>
        <input type="range" id="s1Slider" min="0" max="360" value="0" step="5" oninput="s1OnSlider(this.value)" class="flex-1 accent-amber-400 cursor-pointer">
        <button onclick="s1Reset()" class="text-xs text-slate-400 hover:text-white px-2 py-1 bg-slate-800 rounded border border-slate-700">Reset</button>
    </div>
</div>
"""

# Simulator 2: Turn Types (Quadrant Wheel & Pointer)
sims_1_to_8[2] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-blue-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
            Rotational Fractions Quadrant
        </span>
        <span id="s2FractionReadout" class="font-mono bg-blue-950/80 px-2.5 py-1 rounded-md text-blue-300 border border-blue-500/30 font-bold">
            0/4 Turn (0°)
        </span>
    </div>

    <!-- SVG Quadrant Circle -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s2Svg" viewBox="-150 -150 300 300" class="w-full h-full drop-shadow-md">
            <!-- 4 Quadrants Background -->
            <path id="s2Sector1" d="M 0,0 L 0,-120 A 120,120 0 0,1 120,0 Z" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="1.5"/>
            <path id="s2Sector2" d="M 0,0 L 120,0 A 120,120 0 0,1 0,120 Z" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="1.5"/>
            <path id="s2Sector3" d="M 0,0 L 0,120 A 120,120 0 0,1 -120,0 Z" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="1.5"/>
            <path id="s2Sector4" d="M 0,0 L -120,0 A 120,120 0 0,1 0,-120 Z" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="1.5"/>
            
            <!-- Outer Ring -->
            <circle cx="0" cy="0" r="120" fill="none" stroke="#475569" stroke-width="2"/>
            
            <!-- Cardinal Labels -->
            <text x="0" y="-128" text-anchor="middle" font-size="11" font-weight="bold" fill="#93c5fd">Start (0° / 360°)</text>
            <text x="135" y="4" text-anchor="start" font-size="11" font-weight="bold" fill="#6ee7b7">1/4 Turn (90°)</text>
            <text x="0" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#c4b5fd">1/2 Turn (180°)</text>
            <text x="-135" y="4" text-anchor="end" font-size="11" font-weight="bold" fill="#fde047">3/4 Turn (270°)</text>

            <!-- Dynamic Swept Wedge Arc -->
            <path id="s2WedgeArc" d="" fill="#ef4444" fill-opacity="0.35"/>

            <!-- Baseline Ray (Pointing Up) -->
            <line x1="0" y1="0" x2="0" y2="-120" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="4 3"/>

            <!-- Movable Pointer Ray -->
            <g id="s2PointerGroup" transform="rotate(0)">
                <line x1="0" y1="0" x2="0" y2="-120" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
                <polygon points="0,-128 -7,-112 7,-112" fill="#ef4444"/>
            </g>

            <!-- Centre Pivot -->
            <circle cx="0" cy="0" r="8" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Interactive Buttons -->
    <div class="w-full grid grid-cols-2 sm:grid-cols-4 gap-2 mt-2">
        <button onclick="s2SetTurn(90, '1/4 Turn (90°)')" class="px-2 py-1.5 bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/40 rounded-lg text-xs font-bold transition">
            1/4 Turn (90°)
        </button>
        <button onclick="s2SetTurn(180, '1/2 Turn (180°)')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 rounded-lg text-xs font-bold transition">
            1/2 Turn (180°)
        </button>
        <button onclick="s2SetTurn(270, '3/4 Turn (270°)')" class="px-2 py-1.5 bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/40 rounded-lg text-xs font-bold transition">
            3/4 Turn (270°)
        </button>
        <button onclick="s2SetTurn(360, '1 Full Turn (360°)')" class="px-2 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            1 Full Turn (360°)
        </button>
    </div>
</div>
"""

# Simulator 3: What Is Angle (Dynamic Two-Ray Angle Builder)
sims_1_to_8[3] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-teal-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-400 animate-pulse"></span>
            Two-Ray Angle Anatomy
        </span>
        <span id="s3AngleReadout" class="font-mono bg-teal-950/80 px-2.5 py-1 rounded-md text-teal-300 border border-teal-500/30 font-bold">
            Angle: 45°
        </span>
    </div>

    <!-- SVG Canvas -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s3Svg" viewBox="-40 -160 320 200" class="w-full h-full drop-shadow-md">
            <!-- Vertex marker -->
            <circle cx="0" cy="0" r="10" fill="#0f172a" stroke="#14b8a6" stroke-width="3"/>
            <text x="-15" y="24" font-size="12" font-weight="bold" fill="#14b8a6">Vertex</text>

            <!-- Angle Arc -->
            <path id="s3Arc" d="" fill="none" stroke="#f59e0b" stroke-width="3"/>
            <text id="s3ArcText" x="50" y="-20" font-size="11" font-weight="bold" fill="#fbbf24">45°</text>

            <!-- Arm 1 (Baseline, horizontal) -->
            <line id="s3Arm1" x1="0" y1="0" x2="160" y2="0" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
            <polygon id="s3Arm1Arrow" points="166,0 156,-5 156,5" fill="#38bdf8"/>
            <text x="110" y="20" font-size="11" fill="#7dd3fc" font-weight="bold">Base Arm</text>

            <!-- Arm 2 (Rotating) -->
            <g id="s3Arm2Group">
                <line id="s3Arm2" x1="0" y1="0" x2="113" y2="-113" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
                <polygon id="s3Arm2Arrow" points="117,-117 106,-110 110,-106" fill="#f43f5e"/>
                <text id="s3Arm2Label" x="90" y="-125" font-size="11" fill="#fda4af" font-weight="bold">Rotated Arm</text>
            </g>
        </svg>
    </div>

    <!-- Slider & Toggles -->
    <div class="w-full flex flex-col gap-2 mt-2">
        <div class="flex items-center justify-between text-xs">
            <span class="text-slate-400">Rotate Angle:</span>
            <input type="range" id="s3AngleSlider" min="0" max="180" value="45" oninput="s3UpdateAngle(this.value)" class="w-3/5 accent-teal-400 cursor-pointer">
            <span id="s3SliderVal" class="font-mono text-teal-300 font-bold w-12 text-right">45°</span>
        </div>
        <div class="flex items-center justify-between text-xs pt-1 border-t border-slate-800">
            <span class="text-slate-400">Arm Length:</span>
            <input type="range" id="s3LenSlider" min="80" max="180" value="160" oninput="s3UpdateLength(this.value)" class="w-3/5 accent-blue-400 cursor-pointer">
            <span class="text-slate-400 text-[10px] w-12 text-right">(No Angle Change)</span>
        </div>
    </div>
</div>
"""

# Simulator 4: Right Angle (Quarter Turn & Square Corner)
sims_1_to_8[4] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-emerald-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            1/4 Turn Right Angle Inspector
        </span>
        <span id="s4StatusReadout" class="font-mono bg-emerald-950/80 px-2.5 py-1 rounded-md text-emerald-300 border border-emerald-500/30 font-bold">
            Exact Right Angle (90°)
        </span>
    </div>

    <!-- SVG Right Angle Display -->
    <div class="relative w-full max-w-[320px] aspect-square flex items-center justify-center my-2">
        <svg id="s4Svg" viewBox="-30 -160 260 200" class="w-full h-full drop-shadow-md">
            <!-- Background Grid Corner -->
            <rect x="0" y="-140" width="140" height="140" fill="#10b981" fill-opacity="0.05" stroke="#334155" stroke-dasharray="3 3"/>

            <!-- Square Corner Symbol (Appears at 90°) -->
            <rect id="s4SquareCorner" x="0" y="-24" width="24" height="24" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2.5"/>

            <!-- Base Arm (Horizontal) -->
            <line x1="0" y1="0" x2="160" y2="0" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>
            <polygon points="166,0 156,-5 156,5" fill="#64748b"/>

            <!-- Upright / Movable Arm -->
            <g id="s4ArmGroup">
                <line x1="0" y1="0" x2="0" y2="-150" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                <polygon points="0,-156 -5,-146 5,-146" fill="#10b981"/>
            </g>

            <!-- Vertex -->
            <circle cx="0" cy="0" r="9" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
            <text x="-15" y="24" font-size="11" font-weight="bold" fill="#64748b">Vertex</text>
            <text x="110" y="20" font-size="11" font-weight="bold" fill="#64748b">Arm 1</text>
            <text x="-4" y="-160" font-size="11" font-weight="bold" fill="#10b981">Arm 2</text>
        </svg>
    </div>

    <!-- Real-World Presets -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s4SetPreset(90, 'Clock at 3:00')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 rounded-lg text-xs font-bold transition">
            🕒 Clock 3:00
        </button>
        <button onclick="s4SetPreset(90, 'Textbook Corner')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 rounded-lg text-xs font-bold transition">
            📖 Book Corner
        </button>
        <button onclick="s4SetPreset(90, 'Perpendicular Door')" class="px-2 py-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 rounded-lg text-xs font-bold transition">
            🚪 Doorway 90°
        </button>
    </div>
</div>
"""

# Simulator 5: Acute Angle (Sharp Scissors / Beak)
sims_1_to_8[5] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-cyan-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
            Sharp Turn Acute Angle Lab
        </span>
        <span id="s5Readout" class="font-mono bg-cyan-950/80 px-2.5 py-1 rounded-md text-cyan-300 border border-cyan-500/30 font-bold">
            Acute Angle: 35° (&lt; 90°)
        </span>
    </div>

    <!-- SVG Scissor / Sharp Angle -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s5Svg" viewBox="-30 -140 280 180" class="w-full h-full drop-shadow-md">
            <!-- Dashed 90° reference line -->
            <line x1="0" y1="0" x2="0" y2="-120" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
            <text x="6" y="-115" font-size="10" fill="#64748b">90° Right Angle Reference</text>

            <!-- Acute Angle Arc -->
            <path id="s5Arc" d="" fill="#06b6d4" fill-opacity="0.2" stroke="#06b6d4" stroke-width="2.5"/>
            <text id="s5ArcLabel" x="50" y="-15" font-size="11" font-weight="bold" fill="#22d3ee">35°</text>

            <!-- Blade 1 (Fixed) -->
            <line x1="0" y1="0" x2="160" y2="0" stroke="#0ea5e9" stroke-width="5" stroke-linecap="round"/>
            <circle cx="160" cy="0" r="3" fill="#0ea5e9"/>

            <!-- Blade 2 (Rotatable Acute) -->
            <g id="s5Blade2Group">
                <line x1="0" y1="0" x2="131" y2="-91" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
                <circle cx="131" cy="-91" r="3" fill="#f43f5e"/>
            </g>

            <!-- Pivot Screw -->
            <circle cx="0" cy="0" r="8" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Angle Slider -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Sharp Opening:</span>
        <input type="range" id="s5Slider" min="10" max="85" value="35" oninput="s5Update(this.value)" class="flex-1 accent-cyan-400 cursor-pointer">
        <span id="s5Val" class="font-mono text-cyan-300 font-bold text-xs w-10 text-right">35°</span>
    </div>
</div>
"""

# Simulator 6: Obtuse Angle (Wide Turn & Reclining Chair / Laptop)
sims_1_to_8[6] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-purple-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse"></span>
            Wide Turn Obtuse Angle Lab
        </span>
        <span id="s6Readout" class="font-mono bg-purple-950/80 px-2.5 py-1 rounded-md text-purple-300 border border-purple-500/30 font-bold">
            Obtuse Angle: 125° (&gt; 90°, &lt; 180°)
        </span>
    </div>

    <!-- SVG Obtuse Display -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s6Svg" viewBox="-130 -140 280 180" class="w-full h-full drop-shadow-md">
            <!-- 90° right angle reference line -->
            <line x1="0" y1="0" x2="0" y2="-120" stroke="#475569" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="6" y="-115" font-size="9" fill="#64748b">90° Right Angle</text>

            <!-- 180° straight angle reference line -->
            <line x1="0" y1="0" x2="-120" y2="0" stroke="#475569" stroke-width="1.5" stroke-dasharray="2 2"/>
            <text x="-115" y="-6" font-size="9" fill="#64748b">180°</text>

            <!-- Obtuse Angle Swept Arc -->
            <path id="s6Arc" d="" fill="#a855f7" fill-opacity="0.25" stroke="#a855f7" stroke-width="2.5"/>
            <text id="s6ArcLabel" x="25" y="-50" font-size="11" font-weight="bold" fill="#d8b4fe">125°</text>

            <!-- Base Arm (Horizontal) -->
            <line x1="0" y1="0" x2="130" y2="0" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>

            <!-- Obtuse Rotating Arm -->
            <g id="s6ArmGroup">
                <line x1="0" y1="0" x2="-74" y2="-106" stroke="#c084fc" stroke-width="5" stroke-linecap="round"/>
                <circle cx="-74" cy="-106" r="4" fill="#e9d5ff"/>
            </g>

            <!-- Center Pivot -->
            <circle cx="0" cy="0" r="8" fill="#0f172a" stroke="#a855f7" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
        </svg>
    </div>

    <!-- Controls -->
    <div class="w-full flex items-center justify-between gap-3 mt-2 px-2">
        <span class="text-xs text-slate-400">Wide Opening:</span>
        <input type="range" id="s6Slider" min="95" max="175" value="125" oninput="s6Update(this.value)" class="flex-1 accent-purple-400 cursor-pointer">
        <span id="s6Val" class="font-mono text-purple-300 font-bold text-xs w-10 text-right">125°</span>
    </div>
</div>
"""

# Simulator 7: Straight Angle (Two Quarter Turns / 180° Line)
sims_1_to_8[7] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-rose-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-rose-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-rose-400 animate-pulse"></span>
            1/2 Turn Straight Angle Transformer
        </span>
        <span id="s7Readout" class="font-mono bg-rose-950/80 px-2.5 py-1 rounded-md text-rose-300 border border-rose-500/30 font-bold">
            Two 1/4 Turns = 180° Flat Line
        </span>
    </div>

    <!-- SVG Straight Angle Display -->
    <div class="relative w-full max-w-[340px] aspect-[5/3] flex items-center justify-center my-2">
        <svg id="s7Svg" viewBox="-150 -100 300 140" class="w-full h-full drop-shadow-md">
            <!-- Semicircle Arc (180°) -->
            <path id="s7Semicircle" d="M 120,0 A 120,120 0 0,0 -120,0" fill="#f43f5e" fill-opacity="0.15" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3"/>

            <!-- Right Angle Step Indicator (90°) -->
            <line x1="0" y1="0" x2="0" y2="-90" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="5" y="-75" font-size="9" fill="#fde047">1st 1/4 Turn (90°)</text>

            <!-- Flat Straight Line Arms -->
            <line x1="0" y1="0" x2="130" y2="0" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
            <polygon points="136,0 126,-5 126,5" fill="#f43f5e"/>

            <g id="s7ArmLeftGroup">
                <line x1="0" y1="0" x2="-130" y2="0" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
                <polygon points="-136,0 -126,-5 -126,5" fill="#38bdf8"/>
            </g>

            <!-- Center Pivot -->
            <circle cx="0" cy="0" r="8" fill="#0f172a" stroke="#f43f5e" stroke-width="3"/>
            <circle cx="0" cy="0" r="3" fill="#ffffff"/>
            <text x="0" y="24" text-anchor="middle" font-size="11" font-weight="bold" fill="#fda4af">Shared Vertex (180°)</text>
        </svg>
    </div>

    <!-- Step Buttons -->
    <div class="w-full grid grid-cols-3 gap-2 mt-2">
        <button onclick="s7Step(0)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-bold transition">
            Reset (0°)
        </button>
        <button onclick="s7Step(90)" class="px-2 py-1.5 bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-bold transition">
            1st 1/4 Turn (90°)
        </button>
        <button onclick="s7Step(180)" class="px-2 py-1.5 bg-rose-600/20 hover:bg-rose-600/30 text-rose-300 border border-rose-500/40 rounded-lg text-xs font-bold transition">
            2nd 1/4 Turn (180°)
        </button>
    </div>
</div>
"""

# Simulator 8: Paper Fan (Accordion Pleated Paper Fan)
sims_1_to_8[8] = """
<div class="bg-slate-900/90 rounded-2xl p-5 border border-amber-500/30 flex flex-col items-center">
    <div class="w-full flex justify-between items-center mb-3 text-xs">
        <span class="font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            Accordion Paper Fan Laboratory
        </span>
        <span id="s8FanReadout" class="font-mono bg-amber-950/80 px-2.5 py-1 rounded-md text-amber-300 border border-amber-500/30 font-bold">
            Fan Spread: 90° (Right Angle)
        </span>
    </div>

    <!-- SVG Accordion Fan -->
    <div class="relative w-full max-w-[340px] aspect-[4/3] flex items-center justify-center my-2">
        <svg id="s8Svg" viewBox="-140 -130 280 160" class="w-full h-full drop-shadow-md">
            <!-- Pleated Fan Blades Group -->
            <g id="s8FanBlades"></g>
            
            <!-- Pinched Vertex Base -->
            <polygon points="-8,10 8,10 4,22 -4,22" fill="#d97706"/>
            <circle cx="0" cy="10" r="5" fill="#f59e0b" stroke="#78350f" stroke-width="2"/>
            <text x="0" y="32" text-anchor="middle" font-size="10" fill="#fcd34d" font-weight="bold">Pinched Vertex</text>
        </svg>
    </div>

    <!-- Fan Presets & Slider -->
    <div class="w-full grid grid-cols-4 gap-1.5 mt-2">
        <button onclick="s8SetAngle(30)" class="px-1.5 py-1 bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-300 border border-cyan-500/30 rounded text-[11px] font-bold">
            Acute (30°)
        </button>
        <button onclick="s8SetAngle(90)" class="px-1.5 py-1 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 rounded text-[11px] font-bold">
            Right (90°)
        </button>
        <button onclick="s8SetAngle(135)" class="px-1.5 py-1 bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 rounded text-[11px] font-bold">
            Obtuse (135°)
        </button>
        <button onclick="s8SetAngle(180)" class="px-1.5 py-1 bg-rose-600/20 hover:bg-rose-600/30 text-rose-300 border border-rose-500/30 rounded text-[11px] font-bold">
            Straight (180°)
        </button>
    </div>
    
    <div class="w-full flex items-center justify-between gap-3 mt-3 px-2">
        <span class="text-xs text-slate-400">Fan Spread:</span>
        <input type="range" id="s8Slider" min="15" max="180" value="90" oninput="s8SetAngle(this.value)" class="flex-1 accent-amber-400 cursor-pointer">
        <span id="s8SliderVal" class="font-mono text-amber-300 font-bold text-xs w-10 text-right">90°</span>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Authored Simulators 1 to 8. Count: {len(sims_1_to_8)}")


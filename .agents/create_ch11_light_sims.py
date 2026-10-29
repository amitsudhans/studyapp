# -*- coding: utf-8 -*-
"""
Generates the 16 bespoke SVG/HTML interactive simulators for Chapter 11: Light: Shadows and Reflections.
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""

def generate_sims():
    sims = {}

    # Simulator 1: Luminous vs Non-Luminous Optical Stage
    sims[1] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.1 Luminous vs Non-Luminous Optical Stage</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Emission vs Reflection</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim1_svg" viewBox="0 0 560 240" class="w-full h-full select-none">
            <!-- Room Background -->
            <rect id="sim1_roomBg" x="0" y="0" width="560" height="240" fill="#020617" />
            
            <!-- Ceiling Light Bulb -->
            <g id="sim1_ceilingLamp" transform="translate(100, 30)">
                <line x1="0" y1="-30" x2="0" y2="10" stroke="#64748b" stroke-width="2" />
                <circle id="sim1_lampBulb" cx="0" cy="18" r="14" fill="#fef08a" filter="drop-shadow(0 0 10px #f59e0b)" />
                <path d="M -8 18 L 8 18" stroke="#f59e0b" stroke-width="1.5" />
                <text x="0" y="42" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Luminous Bulb</text>
            </g>

            <!-- Table Stage in Center -->
            <rect x="200" y="140" width="160" height="15" fill="#78350f" rx="3" />
            <line x1="220" y1="155" x2="220" y2="210" stroke="#451a03" stroke-width="4" />
            <line x1="340" y1="155" x2="340" y2="210" stroke="#451a03" stroke-width="4" />

            <!-- Test Object on Table (Changes dynamically) -->
            <g id="sim1_objectGroup" transform="translate(280, 115)">
                <!-- Default: Non-Luminous Book -->
                <rect id="sim1_objShape" x="-25" y="-15" width="50" height="30" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" />
                <text id="sim1_objLabel" x="0" y="5" font-size="9" font-weight="bold" fill="#f8fafc" text-anchor="middle">Book</text>
            </g>

            <!-- Human Observer Eye on Right -->
            <g transform="translate(480, 100)">
                <!-- Eye Outline -->
                <path d="M -30 0 Q 0 -20 30 0 Q 0 20 -30 0 Z" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" />
                <circle id="sim1_iris" cx="0" cy="0" r="10" fill="#0284c7" />
                <circle cx="0" cy="0" r="4" fill="#020617" />
                <text x="0" y="32" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Observer Eye</text>
            </g>

            <!-- Animated Photon Ray Lines -->
            <g id="sim1_rayLines" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4">
                <!-- Source to Object -->
                <line id="sim1_ray1" x1="100" y1="48" x2="280" y2="115" />
                <!-- Object to Eye (Reflection) -->
                <line id="sim1_ray2" x1="280" y1="115" x2="450" y2="100" />
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <span class="text-xs text-slate-300 font-medium block mb-1.5">Select Test Object:</span>
            <div class="grid grid-cols-2 gap-2">
                <button id="sim1_btnBook" class="px-2.5 py-1.5 rounded bg-cyan-800 text-white text-xs font-semibold hover:bg-cyan-700 transition">Book (Reflector)</button>
                <button id="sim1_btnMirror" class="px-2.5 py-1.5 rounded bg-slate-700 text-slate-200 text-xs font-semibold hover:bg-slate-600 transition">Mirror (Reflector)</button>
                <button id="sim1_btnCandle" class="px-2.5 py-1.5 rounded bg-amber-700 text-white text-xs font-semibold hover:bg-amber-600 transition">Candle (Luminous)</button>
                <button id="sim1_btnFirefly" class="px-2.5 py-1.5 rounded bg-emerald-700 text-white text-xs font-semibold hover:bg-emerald-600 transition">Firefly (Luminous)</button>
            </div>
        </div>
        <div class="flex flex-col justify-between">
            <span class="text-xs text-slate-300 font-medium mb-1">Room Lighting Switch:</span>
            <button id="sim1_btnToggleLight" class="w-full py-2 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition">💡 Room Light: ON (Lit)</button>
            <span id="sim1_visibilityTag" class="text-[11px] text-emerald-400 font-mono mt-1 text-center font-bold">Status: Visible to Eye (Photons Received)</span>
        </div>
    </div>

    <div id="sim1_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Non-luminous objects (like books and mirrors) produce zero light. When room light strikes them, photons reflect into your eye, making them visible. In a dark room, they become completely invisible!
    </div>
</div>
"""

    # Simulator 2: Sun-Earth-Moon Cosmic Reflector Orbit
    sims[2] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">11.1 The Moon Paradox: Reflected Moonlight Orbit</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Aryabhata's Solar Reflection Principle</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
        <!-- Space Orbital View (8 cols) -->
        <div class="md:col-span-8 h-64 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim2_orbit_svg" viewBox="0 0 360 220" class="w-full h-full select-none">
                <!-- Distant Sun on Far Left -->
                <rect x="0" y="0" width="30" height="220" fill="#fef08a" opacity="0.3" />
                <path d="M 0 0 L 25 110 L 0 220 Z" fill="#f59e0b" />
                <text x="12" y="115" font-size="9" font-weight="bold" fill="#020617" text-anchor="middle" transform="rotate(-90 12 115)">SUNLIGHT</text>

                <!-- Parallel Sunlight Rays -->
                <g stroke="#fef08a" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6">
                    <line x1="30" y1="50" x2="340" y2="50" />
                    <line x1="30" y1="110" x2="340" y2="110" />
                    <line x1="30" y1="170" x2="340" y2="170" />
                </g>

                <!-- Central Earth -->
                <circle cx="180" cy="110" r="28" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <!-- Earth Continents -->
                <ellipse cx="170" cy="105" rx="10" ry="14" fill="#10b981" />
                <ellipse cx="192" cy="115" rx="8" ry="10" fill="#10b981" />
                <text x="180" y="114" font-size="8" font-weight="bold" fill="#f8fafc" text-anchor="middle">EARTH</text>

                <!-- Moon Orbit Circle -->
                <circle cx="180" cy="110" r="75" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3,3" />

                <!-- Orbiting Moon Body -->
                <!-- Center: (180 + 75*cos(angle), 110 + 75*sin(angle)) -->
                <g id="sim2_moonBody" transform="translate(255, 110)">
                    <circle cx="0" cy="0" r="14" fill="#1e293b" stroke="#64748b" />
                    <!-- Sunlit Half (Always left hemisphere facing Sun) -->
                    <path d="M 0 -14 A 14 14 0 0 0 0 14 Z" fill="#f8fafc" />
                </g>
            </svg>
        </div>

        <!-- Earth Viewfinder: What Observer on Earth Sees (4 cols) -->
        <div class="md:col-span-4 h-64 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-amber-300">Telescopic View from Earth</span>
            <div class="w-28 h-28 rounded-full bg-slate-950 border-2 border-slate-700 flex items-center justify-center overflow-hidden relative shadow-inner">
                <!-- Moon Phase Silhouette -->
                <svg id="sim2_phase_svg" viewBox="0 0 60 60" class="w-full h-full">
                    <circle cx="30" cy="30" r="26" fill="#090d16" />
                    <path id="sim2_phaseShape" d="M 30 4 A 26 26 0 0 1 30 56 A 26 26 0 0 0 30 4 Z" fill="#f8fafc" />
                </svg>
            </div>
            <div>
                <span id="sim2_phaseName" class="text-sm font-bold text-emerald-400 block">Full Moon</span>
                <span class="text-[10px] text-slate-400">Sunlit half directly faces Earth</span>
            </div>
        </div>
    </div>

    <!-- Orbit Slider -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Moon Orbital Position Angle (29.5-Day Month)</span>
            <span id="sim2_angleVal" class="text-cyan-400 font-mono font-bold">180° (Full Moon)</span>
        </div>
        <input type="range" id="sim2_angleSlider" min="0" max="360" value="180" class="w-full accent-cyan-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>0° (New Moon)</span>
            <span>90° (1st Quarter)</span>
            <span>180° (Full Moon)</span>
            <span>270° (3rd Quarter)</span>
            <span>360° (New Moon)</span>
        </div>
    </div>

    <div id="sim2_feedback" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Exactly 50% of the Moon is always lit by the Sun. As the Moon orbits Earth, our viewing angle shifts, creating the cyclic lunar phases from New Moon to Full Moon.
    </div>
</div>
"""

    # Simulator 3: The Three Cardboard Pinholes Alignment Rig
    sims[3] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">11.2 The Three-Cardboard Pinhole Rig</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Collinear Rectilinear Propagation</span>
    </div>

    <div class="relative w-full h-60 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim3_svg" viewBox="0 0 540 220" class="w-full h-full select-none">
            <!-- Optical Track Rail -->
            <line x1="30" y1="180" x2="510" y2="180" stroke="#475569" stroke-width="4" />
            <line x1="30" y1="184" x2="510" y2="184" stroke="#1e293b" stroke-width="2" />

            <!-- Candle Source on Left -->
            <g transform="translate(60, 110)">
                <rect x="-8" y="20" width="16" height="50" fill="#fef3c7" stroke="#d97706" />
                <polygon points="-5,20 5,20 0,0" fill="#f59e0b" />
                <polygon points="-3,20 3,20 0,5" fill="#ef4444" />
                <circle cx="0" cy="5" r="10" fill="#fef08a" opacity="0.3" />
                <text x="0" y="85" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Candle Flame</text>
            </g>

            <!-- Cardboard A (Fixed at x=160, pinhole at y=115) -->
            <g transform="translate(160, 80)">
                <rect x="-10" y="0" width="20" height="100" fill="#b45309" stroke="#78350f" stroke-width="2" rx="2" />
                <circle cx="0" cy="35" r="4" fill="#020617" />
                <text x="0" y="115" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Card A</text>
            </g>

            <!-- Cardboard B (Displaceable vertically via slider at x=280) -->
            <g id="sim3_cardB" transform="translate(280, 80)">
                <rect x="-10" y="0" width="20" height="100" fill="#b45309" stroke="#78350f" stroke-width="2" rx="2" />
                <circle id="sim3_pinB" cx="0" cy="35" r="4" fill="#020617" />
                <text x="0" y="115" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Card B</text>
            </g>

            <!-- Cardboard C (Fixed at x=400, pinhole at y=115) -->
            <g transform="translate(400, 80)">
                <rect x="-10" y="0" width="20" height="100" fill="#b45309" stroke="#78350f" stroke-width="2" rx="2" />
                <circle cx="0" cy="35" r="4" fill="#020617" />
                <text x="0" y="115" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Card C</text>
            </g>

            <!-- Target Screen / Eye on Right at x=490 -->
            <g transform="translate(490, 80)">
                <rect x="-5" y="0" width="10" height="100" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="2" />
                <!-- Projected Light Spot on Screen -->
                <circle id="sim3_screenSpot" cx="0" cy="35" r="7" fill="#fef08a" filter="drop-shadow(0 0 6px #f59e0b)" />
                <text x="0" y="115" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Screen</text>
            </g>

            <!-- Straight Laser Beam Path -->
            <line id="sim3_beam1" x1="60" y1="115" x2="280" y2="115" stroke="#fde047" stroke-width="3" opacity="0.9" />
            <line id="sim3_beam2" x1="280" y1="115" x2="490" y2="115" stroke="#fde047" stroke-width="3" opacity="0.9" />
        </svg>
    </div>

    <!-- Controls -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Cardboard B Vertical Alignment Offset</span>
            <span id="sim3_offsetVal" class="text-emerald-400 font-mono font-bold">0 mm (Collinear Perfect)</span>
        </div>
        <input type="range" id="sim3_offsetSlider" min="-30" max="30" value="0" class="w-full accent-emerald-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>-30 mm (Displaced Low)</span>
            <span>0 mm (Strictly Aligned)</span>
            <span>+30 mm (Displaced High)</span>
        </div>
    </div>

    <div id="sim3_status" class="text-xs p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-center font-medium">
        Collinear alignment achieved! Light travels in a straight line through all three pinholes, forming a bright golden spot on the screen.
    </div>
</div>
"""

    # Simulator 4: Straight vs Bent Rubber Pipe Visualizer
    sims[4] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.2 Straight vs Bent Pipe Optical Experiment</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Light Cannot Bend Around Corners</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
        <!-- Pipe Diagram View (8 cols) -->
        <div class="md:col-span-8 h-64 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim4_pipe_svg" viewBox="0 0 360 220" class="w-full h-full select-none">
                <!-- Candle on Left -->
                <g transform="translate(50, 110)">
                    <rect x="-8" y="20" width="16" height="50" fill="#fef3c7" stroke="#d97706" />
                    <polygon points="-5,20 5,20 0,0" fill="#f59e0b" />
                    <polygon points="-3,20 3,20 0,5" fill="#ef4444" />
                    <circle cx="0" cy="5" r="10" fill="#fef08a" opacity="0.3" />
                    <text x="0" y="85" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Candle</text>
                </g>

                <!-- Pipe Tube (Straight vs Bent) -->
                <!-- Path d changes dynamically via JS -->
                <path id="sim4_pipeBody" d="M 100 110 L 260 110" stroke="#475569" stroke-width="26" stroke-linecap="round" fill="none" />
                <path id="sim4_pipeLumen" d="M 100 110 L 260 110" stroke="#090d16" stroke-width="16" stroke-linecap="round" fill="none" />

                <!-- Straight Light Beam through Lumen -->
                <line id="sim4_beam" x1="50" y1="110" x2="310" y2="110" stroke="#fde047" stroke-width="4" />

                <!-- Observer Eye on Right -->
                <g transform="translate(320, 110)">
                    <path d="M -15 0 Q 0 -12 15 0 Q 0 12 -15 0 Z" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" />
                    <circle cx="0" cy="0" r="5" fill="#0284c7" />
                    <circle cx="0" cy="0" r="2" fill="#020617" />
                    <text x="0" y="24" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Observer</text>
                </g>
            </svg>
        </div>

        <!-- Inset Pupil Perspective (4 cols) -->
        <div class="md:col-span-4 h-64 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-cyan-300">Observer Eye View</span>
            <div class="w-28 h-28 rounded-full bg-slate-950 border-2 border-slate-700 flex items-center justify-center overflow-hidden relative shadow-inner">
                <!-- Pupil interior: either shows flame or pitch dark -->
                <div id="sim4_pupilView" class="w-full h-full flex items-center justify-center">
                    <span id="sim4_flameIcon" class="text-4xl animate-bounce">🔥</span>
                </div>
            </div>
            <div>
                <span id="sim4_viewText" class="text-xs font-bold text-emerald-400 block">Flame Clearly Visible!</span>
                <span class="text-[10px] text-slate-400">Direct straight-line ray</span>
            </div>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <button id="sim4_btnStraight" class="px-4 py-2 rounded bg-emerald-600 text-white text-xs font-bold hover:bg-emerald-500 transition">Test Straight Pipe (0° Bend)</button>
        <button id="sim4_btnBent" class="px-4 py-2 rounded bg-rose-600 text-white text-xs font-bold hover:bg-rose-500 transition">Test Bent Pipe (60° Bend)</button>
    </div>

    <div id="sim4_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        When the rubber pipe is straight, light rays travel unobstructed through the lumen into your eye. When bent, light cannot curve around the angle, rendering the flame completely invisible.
    </div>
</div>
"""

    # Simulator 5: 3-Material Optical Beam Transmissometer (11.3)
    sims[5] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">11.3 Material Optical Transmissometer</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Transparent • Translucent • Opaque</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim5_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Flashlight Source on Left -->
            <g transform="translate(60, 110)">
                <rect x="-30" y="-15" width="30" height="30" fill="#475569" rx="3" />
                <path d="M 0 -22 L 25 -32 L 25 32 L 0 22 Z" fill="#f59e0b" />
                <text x="-15" y="32" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Flashlight</text>
            </g>

            <!-- Light Beam 1 (Source to Material) -->
            <polygon points="85,78 240,40 240,180 85,142" fill="#fef08a" opacity="0.4" />

            <!-- Test Material Slab (x=240, width=40) -->
            <rect id="sim5_slab" x="240" y="30" width="40" height="160" rx="4" fill="#38bdf8" opacity="0.3" stroke="#0ea5e9" stroke-width="2" />
            <text id="sim5_slabName" x="260" y="210" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Clear Optical Glass</text>

            <!-- Light Beam 2 (Transmitted Past Material) -->
            <polygon id="sim5_transBeam" points="280,40 450,15 450,205 280,180" fill="#fef08a" opacity="0.38" />

            <!-- Target Screen on Right -->
            <rect x="450" y="10" width="16" height="200" fill="#f8fafc" stroke="#64748b" rx="2" />
            <text x="458" y="225" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Screen</text>

            <!-- Transmitted Light Spot / Shadow on Screen -->
            <rect id="sim5_screenLight" x="451" y="25" width="14" height="170" fill="#fef08a" opacity="0.8" />
            <!-- Shadow Overlay (Darkness) -->
            <rect id="sim5_screenShadow" x="451" y="25" width="14" height="170" fill="#020617" opacity="0.05" />
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-3 gap-2">
        <button id="sim5_btnTransp" class="py-2 rounded bg-emerald-700 text-white text-xs font-bold hover:bg-emerald-600 transition">1. Transparent (Glass)</button>
        <button id="sim5_btnTransl" class="py-2 rounded bg-cyan-700 text-white text-xs font-bold hover:bg-cyan-600 transition">2. Translucent (Butter Paper)</button>
        <button id="sim5_btnOpaque" class="py-2 rounded bg-rose-700 text-white text-xs font-bold hover:bg-rose-600 transition">3. Opaque (Wood / Metal)</button>
    </div>

    <div id="sim5_desc" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        <strong class="text-emerald-400">Transparent:</strong> Transmits 98% of incident photons without deviation. Objects behind are seen with crisp clarity; virtually zero shadow is cast.
    </div>
</div>
"""

    # Simulator 6: 3-Component Shadow Physics Bench (11.4)
    sims[6] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.4 The 3-Component Shadow Bench</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Source • Obstacle • Screen</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim6_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Floor Grid -->
            <line x1="20" y1="200" x2="520" y2="200" stroke="#475569" stroke-width="2" />

            <!-- 1. Flashlight on Left -->
            <g id="sim6_lightGroup" transform="translate(60, 110)">
                <rect x="-25" y="-12" width="25" height="24" fill="#475569" rx="2" />
                <path d="M 0 -18 L 20 -26 L 20 26 L 0 18 Z" fill="#f59e0b" />
                <text x="-12" y="28" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Torch</text>
            </g>

            <!-- Light Cone Rays -->
            <polygon id="sim6_beamPoly" points="80,84 460,20 460,200 80,136" fill="#fef08a" opacity="0.35" />

            <!-- 2. Opaque Obstacle Object in Center (x position adjustable) -->
            <g id="sim6_obstacle" transform="translate(240, 110)">
                <circle cx="0" cy="0" r="24" fill="#334155" stroke="#64748b" stroke-width="2" />
                <text x="0" y="38" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Opaque Sphere</text>
            </g>

            <!-- 3. Screen on Right (Toggleable) -->
            <g id="sim6_screenGroup" transform="translate(460, 110)">
                <rect x="0" y="-95" width="16" height="190" fill="#f8fafc" stroke="#64748b" rx="2" />
                <text x="8" y="112" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Screen</text>

                <!-- Shadow Cast on Screen -->
                <ellipse id="sim6_shadowDisc" cx="8" cy="0" rx="6" ry="42" fill="#020617" />
            </g>

            <!-- Status Indicator if screen removed -->
            <text id="sim6_noScreenMsg" x="460" y="115" font-size="10" font-weight="bold" fill="#f43f5e" text-anchor="middle" style="display:none;">NO SCREEN (No Shadow!)</text>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Obstacle Distance from Torch</span>
                <span id="sim6_distVal" class="text-amber-400 font-mono font-bold">Medium (240 mm)</span>
            </div>
            <input type="range" id="sim6_distSlider" min="140" max="360" value="240" class="w-full accent-amber-500 cursor-pointer">
        </div>
        <div class="flex items-center justify-between gap-2">
            <button id="sim6_toggleLight" class="flex-1 py-2 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition">💡 Torch: ON</button>
            <button id="sim6_toggleScreen" class="flex-1 py-2 rounded bg-cyan-700 text-white text-xs font-bold hover:bg-cyan-600 transition">🖥️ Screen: PRESENT</button>
        </div>
    </div>

    <div id="sim6_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Shadow formation demands all three prerequisites. Toggle off the screen or the light to prove that shadows cannot exist in empty air without a surface to receive them!
    </div>
</div>
"""

    # Simulator 7: Extended Light Source Umbra-Penumbra Ray Tracer (11.4)
    sims[7] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">11.4 Umbra vs Penumbra Ray Tracer</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Point vs Broad Light Source</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim7_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Light Source on Left (Radius adjustable: 4 to 35) -->
            <circle id="sim7_source" cx="60" cy="120" r="28" fill="#fef08a" stroke="#f59e0b" stroke-width="2" filter="drop-shadow(0 0 8px #f59e0b)" />
            <text id="sim7_sourceLabel" x="60" y="165" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Extended Source</text>

            <!-- Opaque Obstacle Ball in Center -->
            <circle cx="260" cy="120" r="22" fill="#334155" stroke="#64748b" stroke-width="2" />
            <text x="260" y="155" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Obstacle</text>

            <!-- Ray Lines: Outer (Penumbra boundary) and Inner (Umbra boundary) -->
            <!-- Top ray to top, bottom to bottom (Umbra) -->
            <line id="sim7_rayU1" x1="60" y1="92" x2="470" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" />
            <line id="sim7_rayU2" x1="60" y1="148" x2="470" y2="140" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" />
            <!-- Cross rays (Penumbra) -->
            <line id="sim7_rayP1" x1="60" y1="92" x2="470" y2="180" stroke="#0ea5e9" stroke-width="1.5" opacity="0.7" />
            <line id="sim7_rayP2" x1="60" y1="148" x2="470" y2="60" stroke="#0ea5e9" stroke-width="1.5" opacity="0.7" />

            <!-- Screen on Right at x=470 -->
            <rect x="470" y="20" width="16" height="200" fill="#f8fafc" stroke="#64748b" rx="2" />
            
            <!-- Penumbra Region (Gray) on Screen -->
            <rect id="sim7_penumbraZone" x="471" y="60" width="14" height="120" fill="#475569" opacity="0.8" />
            <!-- Umbra Region (Jet Black) on Screen -->
            <rect id="sim7_umbraZone" x="471" y="100" width="14" height="40" fill="#020617" />

            <!-- Labels on Screen -->
            <text x="500" y="75" font-size="8" font-weight="bold" fill="#94a3b8">Penumbra</text>
            <text x="500" y="123" font-size="8" font-weight="bold" fill="#f87171">Umbra (Total)</text>
            <text x="500" y="170" font-size="8" font-weight="bold" fill="#94a3b8">Penumbra</text>
        </svg>
    </div>

    <!-- Controls -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Light Source Radius (Point vs Broad Disc)</span>
            <span id="sim7_radiusVal" class="text-amber-400 font-mono font-bold">Broad Source (R = 28 mm)</span>
        </div>
        <input type="range" id="sim7_radiusSlider" min="4" max="36" value="28" class="w-full accent-amber-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>Point Source (0 Penumbra)</span>
            <span>Intermediate Bulb</span>
            <span>Broad Extended Source</span>
        </div>
    </div>

    <div id="sim7_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Broad light sources create two distinct shadow zones: a completely dark central umbra surrounded by a softer, partial penumbra. Moving the slider to 'Point Source' eliminates the penumbra entirely!
    </div>
</div>
"""

    # Simulator 8: 3D Object Rotation & Distance Shadow Projector (11.4)
    sims[8] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">11.4 3D Shape Rotation & Distance Shadow Projector</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Geometric Silhouette Transformation</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
        <!-- 3D Object Stage (7 cols) -->
        <div class="md:col-span-7 h-60 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center p-2 relative">
            <svg id="sim8_obj_svg" viewBox="0 0 300 200" class="w-full h-full select-none">
                <!-- Torch Light Left -->
                <polygon points="10,60 70,30 70,170 10,140" fill="#fef08a" opacity="0.3" />
                <circle cx="20" cy="100" r="14" fill="#f59e0b" />
                <text x="20" y="130" font-size="8" fill="#fde047" text-anchor="middle">Torch</text>

                <!-- Central 3D Object (Rotatable Cylinder) -->
                <g id="sim8_rotGroup" transform="translate(180, 100)">
                    <!-- Cylinder Face -->
                    <rect id="sim8_cylBody" x="-20" y="-35" width="40" height="70" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" />
                    <ellipse id="sim8_cylTop" cx="0" cy="-35" rx="20" ry="8" fill="#60a5fa" stroke="#1d4ed8" />
                </g>
                <text id="sim8_angleLabel" x="180" y="175" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Orientation: 0° (Side View)</text>
            </svg>
        </div>

        <!-- 2D Shadow Screen (5 cols) -->
        <div class="md:col-span-5 h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-amber-300">2D Shadow on Screen</span>
            <div class="w-32 h-36 bg-slate-950 border-2 border-slate-700 rounded-lg flex items-center justify-center p-2 shadow-inner">
                <svg id="sim8_screen_svg" viewBox="0 0 100 120" class="w-full h-full">
                    <!-- Dynamic Shadow Silhouette -->
                    <rect id="sim8_shadowShape" x="25" y="25" width="50" height="70" rx="2" fill="#020617" filter="drop-shadow(0 0 4px #020617)" />
                </svg>
            </div>
            <div>
                <span id="sim8_shapeName" class="text-xs font-bold text-emerald-400 block">Rectangular Silhouette</span>
                <span class="text-[10px] text-slate-400">Projects profile perpendicular to beam</span>
            </div>
        </div>
    </div>

    <!-- Controls -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Rotate Cylinder (0° Profile to 90° End-On)</span>
            <span id="sim8_rotVal" class="text-cyan-400 font-mono font-bold">0° (Side Profile)</span>
        </div>
        <input type="range" id="sim8_rotSlider" min="0" max="90" value="0" class="w-full accent-cyan-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>0° (Rectangle Shadow)</span>
            <span>45° (Rounded Oblong)</span>
            <span>90° (Circular Shadow)</span>
        </div>
    </div>

    <div id="sim8_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        A single 3D cylinder casts completely different 2D shadows depending on orientation: a sharp rectangle when illuminated from the side, and a perfect circle when illuminated from the base!
    </div>
</div>
"""

    # Simulator 9: Celestial Eclipse Simulator (11.4)
    sims[9] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.4 Celestial Eclipse Mechanics Simulator</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Cosmic Umbra & Penumbra</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim9_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Space Background with Stars -->
            <rect x="0" y="0" width="540" height="240" fill="#020617" />
            <circle cx="40" cy="30" r="1" fill="#f8fafc" />
            <circle cx="120" cy="200" r="1.5" fill="#f8fafc" />
            <circle cx="490" cy="40" r="1" fill="#f8fafc" />

            <!-- The Sun on Left (Massive Luminous Sphere) -->
            <circle cx="40" cy="120" r="38" fill="#fef08a" stroke="#f59e0b" stroke-width="2" filter="drop-shadow(0 0 16px #f59e0b)" />
            <text x="40" y="124" font-size="9" font-weight="bold" fill="#020617" text-anchor="middle">SUN</text>

            <!-- Mode 1: Solar Eclipse (Moon in middle, Earth on right) -->
            <g id="sim9_solarGroup">
                <!-- Moon in Middle -->
                <circle cx="240" cy="120" r="10" fill="#94a3b8" stroke="#cbd5e1" />
                <text x="240" y="145" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Moon</text>

                <!-- Moon's Umbra Shadow Cone to Earth -->
                <polygon points="240,110 440,118 440,122 240,130" fill="#020617" opacity="0.9" />
                <!-- Moon's Penumbra Shadow Cone to Earth -->
                <polygon points="240,110 440,85 440,155 240,130" fill="#475569" opacity="0.3" />

                <!-- Earth on Right receiving shadow -->
                <circle cx="440" cy="120" r="28" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <!-- Totality Spot on Earth -->
                <circle cx="414" cy="120" r="4" fill="#020617" />
                <text x="440" y="160" font-size="8" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Earth</text>
            </g>

            <!-- Mode 2: Lunar Eclipse (Earth in middle, Moon on right - toggled via JS) -->
            <g id="sim9_lunarGroup" style="display:none;">
                <!-- Earth in Middle -->
                <circle cx="260" cy="120" r="28" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                <text x="260" y="160" font-size="8" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Earth</text>

                <!-- Earth's Giant Umbra Shadow Cone -->
                <polygon points="260,92 480,105 480,135 260,148" fill="#020617" opacity="0.9" />

                <!-- Moon Plunging into Earth's Shadow on Right -->
                <circle cx="460" cy="120" r="10" fill="#dc2626" stroke="#b91c1c" />
                <text x="460" y="145" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">Blood Moon</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div class="flex gap-2">
            <button id="sim9_btnSolar" class="px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition">Solar Eclipse (Sun-Moon-Earth)</button>
            <button id="sim9_btnLunar" class="px-3 py-1.5 rounded bg-slate-700 text-slate-200 text-xs font-semibold hover:bg-slate-600 transition">Lunar Eclipse (Sun-Earth-Moon)</button>
        </div>
        <span id="sim9_phaseNotice" class="text-xs font-mono text-amber-300 font-bold">Phase: New Moon (Daytime Totality)</span>
    </div>

    <div id="sim9_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        <strong class="text-amber-400">Solar Eclipse:</strong> The Moon passes directly between the Sun and Earth during a New Moon, casting its small umbra shadow onto Earth's surface, turning day into night along the path of totality.
    </div>
</div>
"""

    # Simulator 10: Interactive Optical Bench: Law of Reflection (11.5)
    sims[10] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">11.5 The Universal Law of Reflection (∠i = ∠r)</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Precision Laser Bench</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim10_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Horizontal Plane Mirror at y=180 -->
            <rect x="60" y="180" width="420" height="12" fill="#38bdf8" opacity="0.8" stroke="#0284c7" stroke-width="2" rx="1" />
            <!-- Mirror Hatching (Silver backing) -->
            <g stroke="#64748b" stroke-width="1.5">
                <line x1="80" y1="192" x2="70" y2="202" />
                <line x1="120" y1="192" x2="110" y2="202" />
                <line x1="160" y1="192" x2="150" y2="202" />
                <line x1="200" y1="192" x2="190" y2="202" />
                <line x1="240" y1="192" x2="230" y2="202" />
                <line x1="280" y1="192" x2="270" y2="202" />
                <line x1="320" y1="192" x2="310" y2="202" />
                <line x1="360" y1="192" x2="350" y2="202" />
                <line x1="400" y1="192" x2="390" y2="202" />
                <line x1="440" y1="192" x2="430" y2="202" />
            </g>
            <text x="270" y="218" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">Flat Plane Mirror Surface</text>

            <!-- Normal Line (Perpendicular at Point of Incidence x=270, y=180) -->
            <line x1="270" y1="40" x2="270" y2="180" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,4" />
            <text x="270" y="30" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Normal Line (90°)</text>

            <!-- Protractor Angle Arc Overlays -->
            <path id="sim10_arcI" d="M 270 140 A 40 40 0 0 0 240 145" stroke="#38bdf8" stroke-width="2" fill="none" />
            <path id="sim10_arcR" d="M 270 140 A 40 40 0 0 1 300 145" stroke="#f43f5e" stroke-width="2" fill="none" />

            <!-- Point of Incidence O -->
            <circle cx="270" cy="180" r="4" fill="#f59e0b" />
            <text x="270" y="172" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">O</text>

            <!-- Incident Laser Beam -->
            <line id="sim10_incBeam" x1="120" y1="60" x2="270" y2="180" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" />
            <text id="sim10_angleIText" x="225" y="130" font-size="11" font-weight="bold" fill="#38bdf8">∠i = 40°</text>

            <!-- Reflected Laser Beam -->
            <line id="sim10_refBeam" x1="270" y1="180" x2="420" y2="60" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" />
            <text id="sim10_angleRText" x="290" y="130" font-size="11" font-weight="bold" fill="#f43f5e">∠r = 40°</text>
        </svg>
    </div>

    <!-- Controls -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Angle of Incidence (∠i) Slider</span>
            <span id="sim10_readout" class="text-emerald-400 font-mono font-bold">∠i = 40° | ∠r = 40° (Exact Match)</span>
        </div>
        <input type="range" id="sim10_angleSlider" min="0" max="75" value="40" class="w-full accent-emerald-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>0° (Normal Incidence)</span>
            <span>30°</span>
            <span>45°</span>
            <span>60°</span>
            <span>75° (Grazing Angle)</span>
        </div>
    </div>

    <div id="sim10_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Universal Law: The angle of incidence always strictly equals the angle of reflection (∠i = ∠r). At 0° (normal), light bounces straight back along its own path!
    </div>
</div>
"""

    # Simulator 11: Plane Mirror Virtual Image Ray Constructor (11.6)
    sims[11] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">11.6 Plane Mirror Virtual Image Geometry</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">d_i = d_o | h_i = h_o</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim11_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Floor / Principal Axis at y=190 -->
            <line x1="30" y1="190" x2="510" y2="190" stroke="#475569" stroke-width="2" />

            <!-- Vertical Plane Mirror in Center (x=270) -->
            <rect x="267" y="30" width="6" height="160" fill="#38bdf8" stroke="#0ea5e9" stroke-width="2" />
            <!-- Mirror Hatching (Right side is behind mirror) -->
            <g stroke="#64748b" stroke-width="1.5">
                <line x1="273" y1="40" x2="280" y2="45" />
                <line x1="273" y1="70" x2="280" y2="75" />
                <line x1="273" y1="100" x2="280" y2="105" />
                <line x1="273" y1="130" x2="280" y2="135" />
                <line x1="273" y1="160" x2="280" y2="165" />
            </g>
            <text x="270" y="22" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mirror Plane</text>

            <!-- Real Candle Object on Left (x adjustable) -->
            <g id="sim11_objCandle" transform="translate(150, 190)">
                <rect x="-8" y="-60" width="16" height="60" fill="#fef3c7" stroke="#d97706" />
                <polygon points="-5,-60 5,-60 0,-80" fill="#f59e0b" />
                <polygon points="-3,-60 3,-60 0,-75" fill="#ef4444" />
                <circle cx="0" cy="-75" r="10" fill="#fef08a" opacity="0.3" />
                <text x="0" y="16" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Object</text>
            </g>

            <!-- Virtual Candle Image on Right (Behind Mirror at equal distance) -->
            <g id="sim11_imgCandle" transform="translate(390, 190)">
                <rect x="-8" y="-60" width="16" height="60" fill="#fef3c7" stroke="#d97706" opacity="0.6" stroke-dasharray="2,2" />
                <polygon points="-5,-60 5,-60 0,-80" fill="#f59e0b" opacity="0.6" />
                <polygon points="-3,-60 3,-60 0,-75" fill="#ef4444" opacity="0.6" />
                <circle cx="0" cy="-75" r="10" fill="#fef08a" opacity="0.2" />
                <text x="0" y="16" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Virtual Image</text>
            </g>

            <!-- Distance Dimension Indicators -->
            <!-- Object Distance d_o -->
            <line id="sim11_lineDo" x1="150" y1="210" x2="270" y2="210" stroke="#fde047" stroke-width="1.5" />
            <text id="sim11_textDo" x="210" y="224" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">d_o = 120 cm</text>
            <!-- Image Distance d_i -->
            <line id="sim11_lineDi" x1="270" y1="210" x2="390" y2="210" stroke="#67e8f9" stroke-width="1.5" />
            <text id="sim11_textDi" x="330" y="224" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">d_i = 120 cm</text>
        </svg>
    </div>

    <!-- Controls -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Candle Object Distance in Front of Mirror (d_o)</span>
            <span id="sim11_distReadout" class="text-amber-400 font-mono font-bold">d_o = 120 cm | d_i = 120 cm</span>
        </div>
        <input type="range" id="sim11_objSlider" min="50" max="200" value="120" class="w-full accent-amber-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>50 cm (Close to Glass)</span>
            <span>120 cm (Mid-Range)</span>
            <span>200 cm (Far Standoff)</span>
        </div>
    </div>

    <div id="sim11_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        In a flat plane mirror, the virtual image is always erect, identical in height (magnification = 1), and formed as far behind the mirror glass as the object is placed in front (d_i = d_o).
    </div>
</div>
"""

    # Simulator 12: Ambulance Text & Lateral Inversion Mirror Box (11.6)
    sims[12] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
            <span class="font-bold text-sm text-rose-300">11.6 Lateral Inversion & The AMBULANCE Effect</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-rose-950 text-rose-200 border border-rose-500/30 font-mono">Left-Right Optical Reversal</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <!-- Direct Real Object View (Left) -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-rose-400">1. Real World Object (Ambulance Front)</span>
            <div class="w-full h-32 bg-slate-950 border border-slate-800 rounded flex flex-col items-center justify-center p-2">
                <span class="text-3xl mb-1">🚑</span>
                <span id="sim12_realText" class="text-xl sm:text-2xl font-mono font-black text-rose-400 tracking-widest">ƎƆИA⅃UБMA</span>
            </div>
            <span class="text-[11px] text-slate-400">Lettering is painted intentionally reversed</span>
        </div>

        <!-- Rearview Mirror Reflection (Right) -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-emerald-400">2. Driver Rear-View Mirror Reflection</span>
            <div class="w-full h-32 bg-slate-950 border-2 border-slate-600 rounded-xl flex flex-col items-center justify-center p-2 shadow-inner">
                <span class="text-xs text-slate-400 mb-1">Car Mirror Frame</span>
                <span id="sim12_mirrorText" class="text-xl sm:text-2xl font-mono font-black text-emerald-300 tracking-widest">AMBULANCE</span>
            </div>
            <span class="text-[11px] text-emerald-300 font-semibold">Lateral inversion restores normal readable text!</span>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <span class="text-xs text-slate-300 font-medium">Test Different Letter Inversions:</span>
        <div class="flex gap-2">
            <button id="sim12_btnAmb" class="px-3 py-1.5 rounded bg-rose-700 text-white text-xs font-bold hover:bg-rose-600 transition">AMBULANCE</button>
            <button id="sim12_btnHand" class="px-3 py-1.5 rounded bg-cyan-700 text-white text-xs font-bold hover:bg-cyan-600 transition">Right Hand Wave</button>
            <button id="sim12_btnLetters" class="px-3 py-1.5 rounded bg-amber-700 text-white text-xs font-bold hover:bg-amber-600 transition">Letters (A, B, C)</button>
        </div>
    </div>

    <div id="sim12_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Lateral inversion swaps bilateral symmetry (left becomes right, right becomes left). Drivers glancing in their rear-view mirrors instantly read 'AMBULANCE' correctly and yield the road.
    </div>
</div>
"""

    # Simulator 13: Virtual Pinhole Camera Optical Box (11.7)
    sims[13] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">11.7 The Pinhole Camera (Camera Obscura)</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Lensless Inverted Real Projection</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim13_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Distant Object on Left: A Colorful Tree -->
            <g id="sim13_object" transform="translate(60, 120)">
                <!-- Trunk -->
                <rect x="-6" y="10" width="12" height="60" fill="#78350f" />
                <!-- Foliage -->
                <circle cx="0" cy="-20" r="32" fill="#10b981" stroke="#059669" stroke-width="2" />
                <!-- Red Apple Top Marker -->
                <circle cx="0" cy="-45" r="5" fill="#ef4444" />
                <text x="0" y="85" font-size="9" font-weight="bold" fill="#f8fafc" text-anchor="middle">Real Tree Object</text>
            </g>

            <!-- Pinhole Camera Box Body (x=240 to 480) -->
            <rect x="240" y="40" width="240" height="150" fill="#020617" stroke="#475569" stroke-width="3" rx="4" />
            <text x="360" y="30" font-size="9" font-weight="bold" fill="#94a3b8" text-anchor="middle">Light-Tight Box</text>

            <!-- Pinhole Aperture on Front Face (x=240, y=115) -->
            <line x1="240" y1="40" x2="240" y2="112" stroke="#e2e8f0" stroke-width="4" />
            <line x1="240" y1="118" x2="240" y2="190" stroke="#e2e8f0" stroke-width="4" />
            <circle cx="240" cy="115" r="3" fill="#fef08a" />
            <text x="240" y="205" font-size="8" font-weight="bold" fill="#fef08a" text-anchor="middle">Pinhole</text>

            <!-- Translucent Screen at Back (x=460) -->
            <rect x="460" y="42" width="6" height="146" fill="#38bdf8" opacity="0.6" stroke="#0ea5e9" />
            <text x="460" y="205" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">Screen</text>

            <!-- Ray Lines Crossing at Pinhole -->
            <!-- Ray 1 from Top of Tree (Red Apple y=-45 => absolute y=75) down through pinhole to screen -->
            <line x1="60" y1="75" x2="240" y2="115" stroke="#ef4444" stroke-width="2" />
            <line x1="240" y1="115" x2="460" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2" />

            <!-- Ray 2 from Bottom of Tree Trunk (y=70 => absolute y=190) up through pinhole to screen -->
            <line x1="60" y1="190" x2="240" y2="115" stroke="#10b981" stroke-width="2" />
            <line x1="240" y1="115" x2="460" y2="70" stroke="#10b981" stroke-width="2" stroke-dasharray="2,2" />

            <!-- Inverted Image on Translucent Screen -->
            <g id="sim13_invImage" transform="translate(460, 115) scale(0.65, -0.65)">
                <rect x="-6" y="10" width="12" height="60" fill="#78350f" opacity="0.8" />
                <circle cx="0" cy="-20" r="32" fill="#10b981" opacity="0.8" />
                <circle cx="0" cy="-45" r="5" fill="#ef4444" opacity="0.9" />
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Camera Box Length (Screen Distance)</span>
                <span id="sim13_lenVal" class="text-cyan-400 font-mono font-bold">Medium (220 mm)</span>
            </div>
            <input type="range" id="sim13_lenSlider" min="140" max="300" value="220" class="w-full accent-cyan-500 cursor-pointer">
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Pinhole Aperture Size</span>
                <span id="sim13_holeVal" class="text-emerald-400 font-mono font-bold">Tiny (Sharp Image)</span>
            </div>
            <input type="range" id="sim13_holeSlider" min="1" max="5" value="1" class="w-full accent-emerald-500 cursor-pointer">
        </div>
    </div>

    <div id="sim13_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Because light travels strictly in straight lines, rays from the top and bottom of the tree cross at the tiny pinhole, projecting an upside-down (inverted), real, and colored image on the translucent screen.
    </div>
</div>
"""

    # Simulator 14: Tree Canopy Solar Projection Simulator (11.7)
    sims[14] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.7 Natural Canopy Pinhole Projections</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Dappled Sunlight & Solar Eclipse Proof</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <!-- Tree Canopy Model (Left) -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-amber-300">Dappled Sunlight on Ground</span>
            <div class="w-full h-36 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-center p-2 relative overflow-hidden">
                <!-- Ground with Dappled Solar Spots -->
                <svg id="sim14_spots_svg" viewBox="0 0 200 120" class="w-full h-full">
                    <rect x="0" y="0" width="200" height="120" fill="#1e1b4b" opacity="0.6" />
                    <!-- Normal Round Spots (transmuted dynamically into crescents) -->
                    <g id="sim14_spotsGroup" fill="#fef08a" opacity="0.9">
                        <circle cx="40" cy="30" r="12" />
                        <circle cx="95" cy="45" r="15" />
                        <circle cx="150" cy="35" r="11" />
                        <circle cx="65" cy="80" r="14" />
                        <circle cx="130" cy="85" r="16" />
                        <circle cx="170" cy="95" r="10" />
                    </g>
                </svg>
            </div>
            <span id="sim14_spotLabel" class="text-[11px] text-emerald-300 font-semibold">Normal Sun: Circular solar disc images</span>
        </div>

        <!-- Celestial Sun State (Right) -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center text-center">
            <span class="text-xs font-bold text-cyan-300">Celestial Sun Shape</span>
            <div class="w-28 h-28 rounded-full bg-slate-950 border-2 border-slate-700 flex items-center justify-center overflow-hidden relative shadow-inner">
                <svg viewBox="0 0 60 60" class="w-full h-full">
                    <circle id="sim14_skySun" cx="30" cy="30" r="22" fill="#fef08a" stroke="#f59e0b" stroke-width="2" />
                    <!-- Moon Disc (Slid across Sun during eclipse) -->
                    <circle id="sim14_eclMoon" cx="44" cy="30" r="22" fill="#020617" style="display:none;" />
                </svg>
            </div>
            <div>
                <span id="sim14_sunStateName" class="text-xs font-bold text-amber-400 block">Full Solar Disc (Round)</span>
                <span class="text-[10px] text-slate-400">Light source geometry dictates spot shape</span>
            </div>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <button id="sim14_btnToggleEclipse" class="px-4 py-2 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition">Trigger Partial Solar Eclipse</button>
        <button id="sim14_btnReset" class="px-3 py-2 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold transition">Reset to Normal Sun</button>
    </div>

    <div id="sim14_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Gaps between leaves act as pinholes. During an eclipse, as the Moon covers part of the Sun, every single round spot on the ground transforms into a luminous crescent!
    </div>
</div>
"""

    # Simulator 15: Submarine Trench Periscope Ray Simulator (11.8.1)
    sims[15] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">11.8.1 The Dual-Mirror Periscope (Z-Path Optics)</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Two 45° Plane Mirrors (2 × 90° = 180° Bypass)</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim15_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Obstacle Brick Wall in Center -->
            <rect x="230" y="80" width="80" height="160" fill="#7f1d1d" stroke="#450a0a" stroke-width="2" />
            <text x="270" y="160" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Opaque Wall</text>

            <!-- Target Object (Ship / Apple) on Far Left over Wall -->
            <g transform="translate(60, 45)">
                <!-- Sailing Ship -->
                <path d="M -20 15 L 20 15 L 12 25 L -12 25 Z" fill="#b45309" />
                <line x1="0" y1="15" x2="0" y2="-15" stroke="#78350f" stroke-width="2" />
                <polygon points="0,-15 15,-5 0,5" fill="#f8fafc" />
                <text x="0" y="36" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Surface Ship</text>
            </g>

            <!-- Z-Shaped Periscope Tube -->
            <path d="M 120 45 L 200 45 L 200 195 L 360 195" stroke="#334155" stroke-width="28" stroke-linecap="square" stroke-linejoin="miter" fill="none" />
            <path d="M 120 45 L 200 45 L 200 195 L 360 195" stroke="#090d16" stroke-width="18" stroke-linecap="square" stroke-linejoin="miter" fill="none" />

            <!-- Mirror 1 (Top at x=200, y=45 inclined at 45°) -->
            <line x1="188" y1="33" x2="212" y2="57" stroke="#38bdf8" stroke-width="4" />
            <text x="215" y="30" font-size="8" font-weight="bold" fill="#38bdf8">M₁ (45°)</text>

            <!-- Mirror 2 (Bottom at x=200, y=195 inclined at 45°) -->
            <line x1="188" y1="183" x2="212" y2="207" stroke="#38bdf8" stroke-width="4" />
            <text x="175" y="215" font-size="8" font-weight="bold" fill="#38bdf8">M₂ (45°)</text>

            <!-- Ray Path: Horizontal -> 90° Down -> 90° Forward to Eye -->
            <polyline id="sim15_ray" points="60,45 200,45 200,195 380,195" stroke="#fde047" stroke-width="3" fill="none" stroke-linecap="round" />

            <!-- Observer Eye Behind Wall on Right at x=390, y=195 -->
            <g transform="translate(390, 195)">
                <path d="M -15 0 Q 0 -12 15 0 Q 0 12 -15 0 Z" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" />
                <circle cx="0" cy="0" r="5" fill="#0284c7" />
                <text x="0" y="22" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Commander Eye</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <button id="sim15_btnAnimate" class="px-4 py-2 rounded bg-cyan-700 text-white text-xs font-bold hover:bg-cyan-600 transition">Animate Photon Transit (2 × 90° Turns)</button>
        <span class="text-xs text-slate-300 font-mono">Bypasses high wall completely</span>
    </div>

    <div id="sim15_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Horizontal rays from the distant ship strike top mirror M₁ at 45°, turning 90° down the tube. Striking bottom mirror M₂ at 45°, they turn 90° into the observer's eye, producing an erect, clear view over the wall!
    </div>
</div>
"""

    # Simulator 16: Interactive 60° Kaleidoscope Mandala & Heritage Chamber (11.8.2)
    sims[16] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">11.8.2 The 60° Kaleidoscope & Optical Heritage</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">6-Fold Radial Symmetrical Mandalas</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
        <!-- Kaleidoscope Eyepiece Mandala (7 cols) -->
        <div class="md:col-span-7 h-64 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center p-2">
            <svg id="sim16_mandala_svg" viewBox="0 0 240 240" class="w-full h-full select-none">
                <!-- Circular Brass Eyepiece Frame -->
                <circle cx="120" cy="120" r="110" fill="#020617" stroke="#d97706" stroke-width="4" />
                
                <!-- Equilateral Triangular Mirror Aperture (60° per angle) -->
                <polygon points="120,30 200,165 40,165" fill="#090d16" stroke="#38bdf8" stroke-width="1.5" />
                
                <!-- 6-Fold Symmetric Mandala Petals -->
                <g id="sim16_mandalaGroup" transform="translate(120, 120)">
                    <g transform="rotate(0)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <g transform="rotate(60)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <g transform="rotate(120)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <g transform="rotate(180)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <g transform="rotate(240)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <g transform="rotate(300)"><circle cx="25" cy="0" r="10" fill="#ec4899" opacity="0.8" /><ellipse cx="45" cy="0" rx="14" ry="6" fill="#8b5cf6" /><circle cx="55" cy="0" r="4" fill="#fef08a" /></g>
                    <circle cx="0" cy="0" r="8" fill="#fde047" />
                </g>
            </svg>
        </div>

        <!-- Optical Heritage Scroll (5 cols) -->
        <div class="md:col-span-5 h-64 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between text-xs">
            <span class="font-bold text-amber-300 block mb-1">Our Optical Heritage</span>
            <div class="space-y-2 text-slate-300">
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <strong class="text-emerald-400 block">Maharishi Kanada (6th C. BCE)</strong>
                    Vaisheshika Sutras: Light is composed of fast-moving corpuscular particles of <em>Tejas</em> travelling along straight lines.
                </div>
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <strong class="text-cyan-400 block">Ibn al-Haytham (965–1040 CE)</strong>
                    Kitab al-Manazir: Father of Modern Optics. Proved vision is caused by rays entering the eye; systematized pinhole optics.
                </div>
            </div>
            <span class="text-[10px] text-slate-400">Formula: N = (360° / 60°) − 1 = 5 images per pair</span>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <button id="sim16_btnRotate" class="px-4 py-2 rounded bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xs font-bold hover:from-purple-500 hover:to-pink-500 transition shadow-lg">Rotate Kaleidoscope (Randomize Mandala)</button>
        <span class="text-xs text-amber-300 font-mono font-bold">Infinite non-repeating symmetrical forms!</span>
    </div>

    <div id="sim16_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Three rectangular mirrors inclined at 60° generate infinite 6-fold radial symmetric mandalas. Every shake rearranges the colored glass beads into a unique, never-before-seen design!
    </div>
</div>
"""

    with open(".agents/class7_science_light_sims.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-generated simulators file for Class 7 Science Chapter 11: Light: Shadows and Reflections."""\n\n')
        f.write("SIMULATORS = " + repr(sims) + "\n")

    print(f"Successfully generated class7_science_light_sims.py with {len(sims)} simulators.")

if __name__ == "__main__":
    generate_sims()


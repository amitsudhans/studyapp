# -*- coding: utf-8 -*-
"""
Generates the 16 bespoke SVG/HTML interactive simulators for:
NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun.
Output: .agents/class7_science_earth_moon_sun_sims.py
Strictly zero raw LaTeX. Clean Unicode everywhere.
"""

def create_sims_file():
    print("Generating class7_science_earth_moon_sun_sims.py...")

    code = '''# -*- coding: utf-8 -*-
"""
Bespoke SVG/HTML interactive simulators for NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun.
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""

SIMULATORS = {
    # Simulator 1: Scale & Distance Explorer
    1: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Cosmic Scale & Distance Lab</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Sun • Earth • Moon Trio</span>
        </div>

        <!-- SVG Visualizer -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim1_svg" viewBox="0 0 500 200" class="w-full h-auto max-h-[220px]">
                <!-- Background Stars -->
                <circle cx="30" cy="25" r="1" fill="#cbd5e1" opacity="0.6"/>
                <circle cx="120" cy="80" r="1.5" fill="#f8fafc" opacity="0.8"/>
                <circle cx="210" cy="30" r="1" fill="#cbd5e1" opacity="0.5"/>
                <circle cx="380" cy="40" r="1.5" fill="#fef08a" opacity="0.7"/>
                <circle cx="460" cy="160" r="1" fill="#cbd5e1" opacity="0.6"/>

                <!-- Sun -->
                <g transform="translate(60, 100)">
                    <circle r="45" fill="url(#sunGlowGrad)" opacity="0.4"/>
                    <circle r="36" fill="url(#sunBodyGrad)"/>
                    <text x="0" y="4" text-anchor="middle" fill="#030712" font-size="11" font-weight="bold">SUN</text>
                    <text x="0" y="55" text-anchor="middle" fill="#fde047" font-size="9" font-family="monospace">1,392,700 km</text>
                </g>

                <!-- Light Pulse Photon -->
                <circle id="sim1_photon" cx="100" cy="100" r="4" fill="#38bdf8" filter="drop-shadow(0 0 6px #38bdf8)"/>
                <line x1="100" y1="100" x2="350" y2="100" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.4"/>

                <!-- Earth & Orbit -->
                <g id="sim1_earth_group" transform="translate(350, 100)">
                    <!-- Lunar Orbit -->
                    <circle r="38" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2"/>
                    <!-- Earth -->
                    <circle r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <circle cx="-3" cy="-3" r="5" fill="#22c55e" opacity="0.7"/>
                    <text x="0" y="24" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">EARTH</text>
                    <text x="0" y="34" text-anchor="middle" fill="#94a3b8" font-size="8" font-family="monospace">12,742 km</text>

                    <!-- Moon -->
                    <g id="sim1_moon" transform="translate(38, 0)">
                        <circle r="4.5" fill="#cbd5e1" stroke="#94a3b8" stroke-width="0.8"/>
                        <text x="0" y="-8" text-anchor="middle" fill="#e2e8f0" font-size="7">MOON</text>
                    </g>
                </g>

                <!-- Defs for Gradients -->
                <defs>
                    <radialGradient id="sunGlowGrad" cx="50%" cy="50%" r="50%">
                        <stop offset="0%" stop-color="#f59e0b" stop-opacity="1"/>
                        <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
                    </radialGradient>
                    <radialGradient id="sunBodyGrad" cx="40%" cy="40%" r="60%">
                        <stop offset="0%" stop-color="#fef08a"/>
                        <stop offset="60%" stop-color="#f59e0b"/>
                        <stop offset="100%" stop-color="#ea580c"/>
                    </radialGradient>
                </defs>
            </svg>
        </div>

        <!-- Readout & Transit Metrics -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Sun-to-Earth Distance:</span>
                <span class="text-amber-300 font-mono font-bold text-sm">~150,000,000 km</span>
                <span class="text-slate-400 block text-[10px] mt-1">Light Transit: <strong class="text-emerald-400">8m 20s (500s)</strong></span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Earth-to-Moon Distance:</span>
                <span class="text-cyan-300 font-mono font-bold text-sm">~384,400 km</span>
                <span class="text-slate-400 block text-[10px] mt-1">Light Transit: <strong class="text-emerald-400">1.28 seconds</strong></span>
            </div>
        </div>

        <!-- Interactive Controls -->
        <div class="flex items-center justify-between gap-3 pt-1">
            <button onclick="sim1AnimatePhoton()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-bold text-xs shadow-md transition flex items-center gap-1.5">
                <span>🚀</span> Launch Photon Beam
            </button>
            <button onclick="sim1ToggleOrbit()" id="sim1_orbit_btn" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition">
                Toggle Lunar Orbit
            </button>
        </div>
    </div>
    """,

    # Simulator 2: 3D Earth Globe Rotation Workbench
    2: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Earth Axial Rotation (West to East)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">24-Hour Cycle</span>
        </div>

        <!-- SVG Rotating Globe -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim2_svg" viewBox="0 0 400 200" class="w-full h-auto max-h-[220px]">
                <!-- Distant Sun Rays -->
                <g stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6">
                    <line x1="20" y1="40" x2="130" y2="40"/>
                    <line x1="20" y1="80" x2="130" y2="80"/>
                    <line x1="20" y1="120" x2="130" y2="120"/>
                    <line x1="20" y1="160" x2="130" y2="160"/>
                </g>
                <text x="30" y="25" fill="#fde047" font-size="10" font-weight="bold">☀️ Incoming Sunlight</text>

                <!-- Earth Globe -->
                <g transform="translate(250, 100)">
                    <!-- Rotational Axis Rod -->
                    <line x1="-30" y1="-80" x2="30" y2="80" stroke="#94a3b8" stroke-width="2.5" stroke-linecap="round"/>
                    <circle cx="-30" cy="-80" r="3" fill="#38bdf8"/>
                    <text x="-35" y="-85" text-anchor="end" fill="#38bdf8" font-size="9" font-weight="bold">North Pole</text>
                    <text x="35" y="95" text-anchor="start" fill="#94a3b8" font-size="9">South Pole</text>

                    <!-- Globe Body -->
                    <circle r="60" fill="#0369a1" stroke="#0284c7" stroke-width="2"/>
                    
                    <!-- Dynamic Rotating Continents (clipping circle) -->
                    <clipPath id="sim2_clip">
                        <circle r="59"/>
                    </clipPath>
                    <g clip-path="url(#sim2_clip)">
                        <!-- Day/Night Shadow Overlay -->
                        <!-- Left half lit, right half night -->
                        <path d="M 0 -60 A 60 60 0 0 1 0 60 L 60 60 L 60 -60 Z" fill="#020617" opacity="0.75"/>
                        <!-- Continents moving with angle -->
                        <g id="sim2_continents">
                            <!-- Continents repeated across 2 cycles for infinite wrap -->
                            <path d="M -90 -20 Q -60 -40 -30 -10 Q 0 -30 30 0 Q 10 30 -40 20 Z" fill="#22c55e" opacity="0.8"/>
                            <circle cx="-40" cy="5" r="8" fill="#16a34a"/>
                            <path d="M 70 -30 Q 110 -50 140 -20 Q 160 10 120 30 Q 90 20 70 -30 Z" fill="#22c55e" opacity="0.8"/>
                            <path d="M 230 -20 Q 260 -40 290 -10 Q 320 -30 350 0 Z" fill="#22c55e" opacity="0.8"/>
                        </g>
                        <!-- Delhi Marker -->
                        <circle id="sim2_delhi_dot" cx="0" cy="-10" r="3.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                    </g>

                    <!-- West-to-East Arrow -->
                    <path d="M -40 45 Q 0 55 40 45" fill="none" stroke="#facc15" stroke-width="2.5" marker-end="url(#arrow)"/>
                    <text x="0" y="68" text-anchor="middle" fill="#facc15" font-size="8" font-weight="bold">West ➔ East Spin</text>
                </g>
            </svg>
        </div>

        <!-- City Status Indicator -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Location: <strong class="text-amber-300">New Delhi (28°N)</strong></span>
                <span id="sim2_phase_text" class="text-emerald-400 font-bold">Status: Mid-Day (Sunlight)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Local Hour:</span>
                <span id="sim2_time_text" class="text-cyan-300 font-mono font-bold text-sm">12:00 PM</span>
            </div>
        </div>

        <!-- Slider & Spin Controls -->
        <div class="space-y-2">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Axial Rotation Angle:</span>
                <span id="sim2_angle_val" class="font-mono text-cyan-300">0° (12:00 PM)</span>
            </div>
            <input type="range" id="sim2_slider" min="0" max="360" value="0" step="5" oninput="sim2UpdateAngle(this.value)"
                   class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex items-center justify-between pt-1">
                <button onclick="sim2ToggleAutoSpin()" id="sim2_spin_btn" class="px-4 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">
                    ▶ Auto Spin Globe
                </button>
                <span class="text-[11px] text-slate-400 font-mono">1 Rotation = ~24 Hours</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 3: Day-Night & Circle of Illumination (Terminator)
    3: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider">The Circle of Illumination (Terminator)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Day vs Night</span>
        </div>

        <!-- SVG Terminator Box -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg viewBox="0 0 420 200" class="w-full h-auto max-h-[220px]">
                <!-- Sun Light Source -->
                <circle cx="20" cy="100" r="30" fill="#f59e0b" filter="drop-shadow(0 0 15px #f59e0b)"/>
                <text x="20" y="104" text-anchor="middle" fill="#020617" font-size="10" font-weight="bold">SUN</text>

                <!-- Parallel Rays -->
                <g stroke="#fef08a" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7">
                    <line x1="55" y1="50" x2="200" y2="50"/>
                    <line x1="55" y1="80" x2="200" y2="80"/>
                    <line x1="55" y1="120" x2="200" y2="120"/>
                    <line x1="55" y1="150" x2="200" y2="150"/>
                </g>

                <!-- Earth Spherical Body -->
                <g transform="translate(230, 100)">
                    <!-- Day Hemisphere -->
                    <path d="M 0 -65 A 65 65 0 0 0 0 65 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
                    <text x="-35" y="5" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">DAY</text>
                    <text x="-35" y="20" text-anchor="middle" fill="#bae6fd" font-size="8">Illuminated</text>

                    <!-- Night Hemisphere -->
                    <path d="M 0 -65 A 65 65 0 0 1 0 65 Z" fill="#020617" stroke="#334155" stroke-width="1"/>
                    <text x="35" y="5" text-anchor="middle" fill="#64748b" font-size="11" font-weight="bold">NIGHT</text>
                    <text x="35" y="20" text-anchor="middle" fill="#475569" font-size="8">Shadow</text>

                    <!-- Terminator Line (Vertical Boundary) -->
                    <line x1="0" y1="-75" x2="0" y2="75" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3,3"/>
                    <circle cx="0" cy="-75" r="3" fill="#f43f5e"/>
                    <circle cx="0" cy="75" r="3" fill="#f43f5e"/>
                    
                    <!-- Observer Pin -->
                    <g id="sim3_pin" transform="rotate(0)">
                        <line x1="0" y1="0" x2="0" y2="-65" stroke="#facc15" stroke-width="2"/>
                        <circle cx="0" cy="-65" r="4.5" fill="#facc15" stroke="#000000" stroke-width="1"/>
                    </g>
                </g>

                <!-- Terminator Label -->
                <text x="230" y="20" text-anchor="middle" fill="#f43f5e" font-size="9" font-weight="bold">Terminator Line (Boundary)</text>
                <text x="230" y="192" text-anchor="middle" fill="#94a3b8" font-size="8">Circle of Illumination</text>
            </svg>
        </div>

        <!-- Observer State Readout -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Observer Position:</span>
                <span id="sim3_pos_name" class="text-amber-300 font-bold">Solar Noon (Sub-solar point)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Shadow Length:</span>
                <span id="sim3_shadow_text" class="text-cyan-300 font-mono font-bold">Zero / Minimal</span>
            </div>
        </div>

        <!-- Observer Angle Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Move Observer Around Globe:</span>
                <span id="sim3_slider_val" class="font-mono text-cyan-300">Noon (0°)</span>
            </div>
            <input type="range" id="sim3_slider" min="-180" max="180" value="0" step="15" oninput="sim3SetPin(this.value)"
                   class="w-full accent-emerald-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Midnight (-180°)</span>
                <span>Dawn (-90°)</span>
                <span>Noon (0°)</span>
                <span>Dusk (+90°)</span>
                <span>Midnight (+180°)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Apparent Sky Motion Simulator (East to West)
    4: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Apparent Diurnal Motion (East to West)</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Horizon Simulator</span>
        </div>

        <!-- Dual Mode View: Sky Horizon -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex flex-col items-center justify-center min-h-[220px]">
            <svg id="sim4_svg" viewBox="0 0 450 180" class="w-full h-auto max-h-[180px]">
                <!-- Sky Background Dome -->
                <path d="M 25 150 A 200 130 0 0 1 425 150 Z" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
                
                <!-- Sun's Celestial Arc -->
                <path d="M 50 150 Q 225 20 400 150" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>

                <!-- Horizon Ground -->
                <rect x="20" y="150" width="410" height="25" fill="#1e293b" rx="4"/>
                <text x="50" y="166" fill="#38bdf8" font-size="11" font-weight="bold">EAST</text>
                <text x="225" y="166" text-anchor="middle" fill="#94a3b8" font-size="10">SOUTH (Noon Zenith)</text>
                <text x="400" y="166" text-anchor="end" fill="#f87171" font-size="11" font-weight="bold">WEST</text>

                <!-- Moving Sun on Horizon Arc -->
                <g id="sim4_sun" transform="translate(50, 150)">
                    <circle r="14" fill="#f59e0b" filter="drop-shadow(0 0 8px #f59e0b)"/>
                    <circle r="10" fill="#fef08a"/>
                </g>

                <!-- Stick Shadow Indicator in Ground -->
                <line x1="225" y1="150" x2="225" y2="135" stroke="#ffffff" stroke-width="2.5"/>
                <line id="sim4_shadow" x1="225" y1="150" x2="280" y2="150" stroke="#000000" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
            </svg>
        </div>

        <!-- Horizon Readout -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Time of Day:</span>
                <span id="sim4_time_label" class="text-amber-300 font-mono font-bold text-sm">6:00 AM (Sunrise)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Apparent Sun Motion:</span>
                <span id="sim4_motion_desc" class="text-cyan-300 font-bold">Rising in East ➔ Climbing</span>
            </div>
        </div>

        <!-- Time Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Scrub Sun Across Daytime Sky:</span>
                <span id="sim4_slider_val" class="font-mono text-cyan-300">Sunrise (6:00 AM)</span>
            </div>
            <input type="range" id="sim4_slider" min="6" max="18" value="6" step="0.5" oninput="sim4SetTime(this.value)"
                   class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>6 AM (East Rise)</span>
                <span>12 PM (Solar Noon)</span>
                <span>6 PM (West Set)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Acharya Aryabhata's Boat Analogy
    5: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Aryabhata's Relative Motion Analogy</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">499 CE Discovery</span>
        </div>

        <!-- SVG Boat & River Scene -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim5_svg" viewBox="0 0 450 190" class="w-full h-auto max-h-[190px]">
                <!-- River Water -->
                <rect x="0" y="100" width="450" height="90" fill="#0369a1"/>
                <path d="M 0 115 Q 110 110 220 115 T 450 115" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.6"/>
                <path d="M 0 145 Q 110 140 220 145 T 450 145" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.4"/>

                <!-- Riverbank (Stationary Land) -->
                <rect x="0" y="20" width="450" height="80" fill="#15803d"/>
                
                <!-- Stationary Riverbank Trees (moving apparent vector) -->
                <g id="sim5_trees" transform="translate(0, 0)">
                    <!-- Tree 1 -->
                    <rect x="60" y="55" width="8" height="25" fill="#78350f"/>
                    <circle cx="64" cy="45" r="16" fill="#16a34a"/>
                    <!-- Ancient Temple -->
                    <polygon points="170,40 185,15 200,40" fill="#d97706"/>
                    <rect x="175" y="40" width="20" height="35" fill="#f59e0b"/>
                    <!-- Tree 2 -->
                    <rect x="310" y="55" width="8" height="25" fill="#78350f"/>
                    <circle cx="314" cy="45" r="16" fill="#16a34a"/>
                    <!-- Tree 3 -->
                    <rect x="420" y="55" width="8" height="25" fill="#78350f"/>
                    <circle cx="424" cy="45" r="16" fill="#16a34a"/>
                </g>

                <!-- The Moving Boat -->
                <g id="sim5_boat" transform="translate(180, 120)">
                    <path d="M -35 0 L 35 0 L 25 18 L -25 18 Z" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
                    <polygon points="0,-25 0,0 20,0" fill="#f8fafc"/>
                    <circle cx="-5" cy="-8" r="4" fill="#fbbf24"/>
                    <!-- Boat Direction Arrow (Forward / East) -->
                    <path d="M 40 10 L 70 10" stroke="#22c55e" stroke-width="3" marker-end="url(#arrow)"/>
                    <text x="55" y="24" text-anchor="middle" fill="#22c55e" font-size="8" font-weight="bold">Boat Moves East ➔</text>
                </g>

                <!-- Apparent Motion Arrow on Bank -->
                <path d="M 280 25 L 230 25" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="255" y="16" text-anchor="middle" fill="#f43f5e" font-size="8" font-weight="bold">⬅ Trees Appear to Move West</text>
            </svg>
        </div>

        <!-- Parallel Scientific Truth -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-emerald-400 font-bold block mb-1">Boat Passenger:</span>
                <span class="text-slate-300">Boat moves <strong class="text-emerald-300">Forward</strong>; stationary trees appear to drift <strong class="text-rose-400">Backward</strong>.</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-amber-400 font-bold block mb-1">Observer on Earth:</span>
                <span class="text-slate-300">Earth spins <strong class="text-emerald-300">West to East</strong>; stationary stars appear to drift <strong class="text-amber-300">East to West</strong>.</span>
            </div>
        </div>

        <!-- Interactive Animate Button -->
        <div class="flex items-center justify-between pt-1">
            <button onclick="sim5ToggleAnimation()" id="sim5_btn" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs shadow-md transition">
                ▶ Row Aryabhata's Boat
            </button>
            <span class="text-[11px] text-slate-400 italic">Aryabhatiya Golapada Verse 9</span>
        </div>
    </div>
    """,

    # Simulator 6: Orbital Revolution & Leap Year Calculator
    6: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Earth Revolution & Leap Year Engine</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">365¼ Days Orbit</span>
        </div>

        <!-- SVG Orbit Visualizer -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim6_svg" viewBox="0 0 450 210" class="w-full h-auto max-h-[210px]">
                <!-- Sun at Focus -->
                <circle cx="225" cy="105" r="24" fill="#f59e0b" filter="drop-shadow(0 0 12px #f59e0b)"/>
                <text x="225" y="109" text-anchor="middle" fill="#030712" font-size="9" font-weight="bold">SUN</text>

                <!-- Nearly Circular Orbital Ellipse -->
                <ellipse cx="225" cy="105" rx="170" ry="75" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4"/>

                <!-- 4 Season Month Markers -->
                <text x="225" y="24" text-anchor="middle" fill="#94a3b8" font-size="9">JUNE (Solstice)</text>
                <text x="405" y="108" fill="#94a3b8" font-size="9">SEPT (Equinox)</text>
                <text x="225" y="196" text-anchor="middle" fill="#94a3b8" font-size="9">DEC (Solstice)</text>
                <text x="12" y="108" fill="#94a3b8" font-size="9">MARCH (Equinox)</text>

                <!-- Revolving Earth -->
                <g id="sim6_earth" transform="translate(55, 105)">
                    <circle r="11" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="0" y="-16" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">EARTH</text>
                </g>
            </svg>
        </div>

        <!-- 4-Year Accumulated Hours Bar -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-300">Accumulated Fractional Day:</span>
                <span id="sim6_accum_hours" class="font-mono text-amber-300 font-bold">+6 Hours (Year 1)</span>
            </div>
            <div class="w-full bg-slate-900 h-2 rounded-full overflow-hidden">
                <div id="sim6_hours_bar" class="bg-gradient-to-r from-cyan-500 to-amber-500 h-full w-[25%] transition-all duration-300"></div>
            </div>
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Yr 1 (+6h)</span>
                <span>Yr 2 (+12h)</span>
                <span>Yr 3 (+18h)</span>
                <span class="text-emerald-400 font-bold">Yr 4 (+24h = LEAP DAY!)</span>
            </div>
        </div>

        <!-- Cycle Step Button & Orbit Slider -->
        <div class="flex items-center justify-between gap-3 pt-1">
            <button onclick="sim6StepYear()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold text-xs shadow-md transition">
                📅 Advance Calendar Year
            </button>
            <div class="text-right text-xs">
                <span class="text-slate-400 block text-[10px]">February Days:</span>
                <span id="sim6_feb_days" class="text-emerald-300 font-mono font-bold text-sm">28 Days (Common)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Seasonal Night Sky & Constellation Viewer
    7: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider">Seasonal Constellations & Night Gaze</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">12.2.1 Night Sky</span>
        </div>

        <!-- SVG Deep Sky Ring -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim7_svg" viewBox="0 0 450 220" class="w-full h-auto max-h-[220px]">
                <!-- Central Sun -->
                <circle cx="225" cy="110" r="18" fill="#f59e0b"/>
                <text x="225" y="114" text-anchor="middle" fill="#030712" font-size="8" font-weight="bold">SUN</text>

                <!-- Earth Orbit -->
                <circle cx="225" cy="110" r="65" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3,3"/>

                <!-- Deep Space Constellations Ring -->
                <!-- Winter Constellations (Top) -->
                <g transform="translate(225, 25)">
                    <circle cx="-10" cy="0" r="2" fill="#fde047"/>
                    <circle cx="0" cy="0" r="2" fill="#fde047"/>
                    <circle cx="10" cy="0" r="2" fill="#fde047"/>
                    <text x="0" y="-8" text-anchor="middle" fill="#fde047" font-size="8" font-weight="bold">ORION (Winter)</text>
                </g>
                <!-- Spring (Right) -->
                <g transform="translate(390, 110)">
                    <circle cx="0" cy="-5" r="2" fill="#38bdf8"/>
                    <circle cx="5" cy="5" r="2" fill="#38bdf8"/>
                    <text x="0" y="20" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">LEO (Spring)</text>
                </g>
                <!-- Summer (Bottom) -->
                <g transform="translate(225, 195)">
                    <circle cx="-8" cy="0" r="2" fill="#f43f5e"/>
                    <circle cx="8" cy="0" r="2" fill="#f43f5e"/>
                    <text x="0" y="16" text-anchor="middle" fill="#f43f5e" font-size="8" font-weight="bold">SCORPIUS (Summer)</text>
                </g>
                <!-- Autumn (Left) -->
                <g transform="translate(55, 110)">
                    <circle cx="0" cy="0" r="2" fill="#a855f7"/>
                    <text x="0" y="20" text-anchor="middle" fill="#a855f7" font-size="8" font-weight="bold">PEGASUS (Autumn)</text>
                </g>

                <!-- Earth & Night Sight Cone -->
                <g id="sim7_earth_group" transform="translate(225, 175)">
                    <circle r="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
                    <!-- Night Gaze Cone pointing AWAY from Sun -->
                    <polygon id="sim7_gaze" points="0,0 -35,50 35,50" fill="#6366f1" opacity="0.25"/>
                    <line x1="0" y1="0" x2="0" y2="45" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="2,2"/>
                    <text x="0" y="-10" text-anchor="middle" fill="#94a3b8" font-size="7">Earth</text>
                </g>
            </svg>
        </div>

        <!-- Constellation Visibility Box -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Season / Month:</span>
                <span id="sim7_month_label" class="text-amber-300 font-bold text-sm">December (Winter)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Visible at Midnight:</span>
                <span id="sim7_visible_stars" class="text-emerald-400 font-bold text-sm">Orion, Taurus, Sirius</span>
            </div>
        </div>

        <!-- Month Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Select Month of Year:</span>
                <span id="sim7_slider_val" class="font-mono text-cyan-300">December</span>
            </div>
            <input type="range" id="sim7_slider" min="0" max="11" value="0" step="1" oninput="sim7SetMonth(this.value)"
                   class="w-full accent-indigo-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Dec</span>
                <span>Mar</span>
                <span>Jun</span>
                <span>Sep</span>
                <span>Dec</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 8: Axial Tilt & Polaris Alignment Inspector
    8: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Earth 23.5° Axial Tilt & Polaris Alignment</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Axial Parallelism</span>
        </div>

        <!-- SVG Axial Tilt Geometry -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim8_svg" viewBox="0 0 450 200" class="w-full h-auto max-h-[200px]">
                <!-- Polaris North Star in Distant Space -->
                <g transform="translate(380, 25)">
                    <circle r="4" fill="#ffffff" filter="drop-shadow(0 0 6px #ffffff)"/>
                    <text x="0" y="16" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">POLARIS (North Star)</text>
                </g>

                <!-- Central Sun -->
                <circle cx="225" cy="115" r="16" fill="#f59e0b"/>
                <text x="225" y="119" text-anchor="middle" fill="#030712" font-size="8" font-weight="bold">SUN</text>

                <!-- Orbital Track -->
                <ellipse cx="225" cy="115" rx="170" ry="55" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3"/>

                <!-- Earth 1 (Left - June) -->
                <g id="sim8_earth_left" transform="translate(90, 115)">
                    <!-- Axis Line Tilted 23.5° to Right -->
                    <line x1="-15" y1="35" x2="15" y2="-35" stroke="#f43f5e" stroke-width="2"/>
                    <circle r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="18" y="-38" fill="#f43f5e" font-size="8" font-weight="bold">N (Tilts TOWARD Sun)</text>
                    <text x="0" y="48" text-anchor="middle" fill="#fde047" font-size="8">June Solstice</text>
                </g>

                <!-- Earth 2 (Right - Dec) -->
                <g id="sim8_earth_right" transform="translate(360, 115)">
                    <!-- Axis Line Parallel Tilted 23.5° to Right -->
                    <line x1="-15" y1="35" x2="15" y2="-35" stroke="#f43f5e" stroke-width="2"/>
                    <circle r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="18" y="-38" fill="#f43f5e" font-size="8" font-weight="bold">N (Tilts AWAY)</text>
                    <text x="0" y="48" text-anchor="middle" fill="#38bdf8" font-size="8">Dec Solstice</text>
                </g>

                <!-- Parallel Pointer Rays to Polaris -->
                <line x1="105" y1="80" x2="380" y2="25" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2" opacity="0.6"/>
                <line x1="375" y1="80" x2="380" y2="25" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2" opacity="0.6"/>
            </svg>
        </div>

        <!-- Tilt Specs -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Tilt from Perpendicular:</span>
                <span class="text-amber-300 font-mono font-bold text-sm">23.5°</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Angle to Orbital Plane:</span>
                <span class="text-cyan-300 font-mono font-bold text-sm">66.5°</span>
            </div>
        </div>

        <p class="text-[11px] text-slate-300 bg-slate-950/40 p-2.5 rounded-xl border border-slate-800">
            Notice how both axes point in the exact same direction (towards Polaris) regardless of where Earth travels on its orbit! This parallelism is what exposes alternate hemispheres to direct sunlight.
        </p>
    </div>
    """,

    # Simulator 9: Direct vs Slanted Sunlight (Insolation Angle)
    9: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-yellow-400"></span>
                <h4 class="text-xs font-bold text-yellow-300 uppercase tracking-wider">Direct vs Slanted Sunlight Bench</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Heat Flux Physics</span>
        </div>

        <!-- SVG Flashlight / Solar Beam -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim9_svg" viewBox="0 0 420 190" class="w-full h-auto max-h-[190px]">
                <!-- Ground Surface -->
                <line x1="20" y1="160" x2="400" y2="160" stroke="#64748b" stroke-width="3"/>
                <text x="30" y="180" fill="#94a3b8" font-size="9">Ground Surface</text>

                <!-- Sunlight Beam Polygon -->
                <polygon id="sim9_beam" points="210,20 180,160 240,160" fill="#facc15" opacity="0.35"/>

                <!-- Beam Boundaries -->
                <line id="sim9_ray_left" x1="210" y1="20" x2="180" y2="160" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
                <line id="sim9_ray_right" x1="210" y1="20" x2="240" y2="160" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>

                <!-- Flashlight Source -->
                <circle id="sim9_source" cx="210" cy="20" r="14" fill="#f59e0b"/>
                <text x="210" y="24" text-anchor="middle" fill="#020617" font-size="8" font-weight="bold">SUN</text>

                <!-- Ground Footprint Highlight -->
                <line id="sim9_footprint" x1="180" y1="160" x2="240" y2="160" stroke="#f43f5e" stroke-width="6" stroke-linecap="round"/>
                <text id="sim9_area_label" x="210" y="148" text-anchor="middle" fill="#f43f5e" font-size="9" font-weight="bold">Footprint: 60 mm</text>
            </svg>
        </div>

        <!-- Solar Heat Concentration Readout -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Sunlight Elevation Angle:</span>
                <span id="sim9_angle_readout" class="text-amber-300 font-mono font-bold text-sm">90° (Direct / Summer)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Heating Intensity:</span>
                <span id="sim9_intensity_text" class="text-rose-400 font-bold text-sm">MAXIMUM (Intense Summer Heat)</span>
            </div>
        </div>

        <!-- Angle Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Adjust Sun Elevation Angle:</span>
                <span id="sim9_slider_val" class="font-mono text-cyan-300">90°</span>
            </div>
            <input type="range" id="sim9_slider" min="25" max="90" value="90" step="5" oninput="sim9SetAngle(this.value)"
                   class="w-full accent-yellow-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>25° (Slanted / Winter)</span>
                <span>60° (Spring / Autumn)</span>
                <span>90° (Perpendicular / Summer)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 10: Solstices & Hemispheric Opposition
    10: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Solstices & Hemispheric Opposition</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">June 21 vs Dec 22</span>
        </div>

        <!-- SVG Solstice Globe -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim10_svg" viewBox="0 0 450 200" class="w-full h-auto max-h-[200px]">
                <!-- Sun Light Rays from Left -->
                <g stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6">
                    <line x1="20" y1="40" x2="160" y2="40"/>
                    <line x1="20" y1="80" x2="160" y2="80"/>
                    <line x1="20" y1="120" x2="160" y2="120"/>
                    <line x1="20" y1="160" x2="160" y2="160"/>
                </g>
                <text x="30" y="25" fill="#fde047" font-size="10" font-weight="bold">☀️ Sunlight</text>

                <!-- Earth Globe -->
                <g transform="translate(280, 100)">
                    <!-- Axis Tilted 23.5° -->
                    <line id="sim10_axis" x1="-25" y1="-85" x2="25" y2="85" stroke="#f43f5e" stroke-width="2.5"/>
                    <circle cx="-25" cy="-85" r="3" fill="#f43f5e"/>
                    <text id="sim10_np_text" x="-30" y="-90" text-anchor="end" fill="#f43f5e" font-size="9" font-weight="bold">North Pole (23.5°)</text>

                    <!-- Globe -->
                    <circle r="65" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>

                    <!-- Equator Line -->
                    <line x1="-65" y1="0" x2="65" y2="0" stroke="#facc15" stroke-width="1" stroke-dasharray="2,2"/>
                    <text x="70" y="4" fill="#facc15" font-size="8">Equator (0°)</text>

                    <!-- Tropic of Cancer (23.5°N) -->
                    <line x1="-58" y1="-26" x2="58" y2="-26" stroke="#ffffff" stroke-width="0.8" stroke-dasharray="2,2" opacity="0.8"/>
                    <text x="65" y="-23" fill="#ffffff" font-size="7">Tropic of Cancer (23.5°N)</text>

                    <!-- Shadow Overlay (Right half dark) -->
                    <path d="M 0 -65 A 65 65 0 0 1 0 65 Z" fill="#020617" opacity="0.75"/>
                </g>
            </svg>
        </div>

        <!-- Solstice Comparison Data -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-amber-400 font-bold block mb-1">Northern Hemisphere:</span>
                <span id="sim10_north_status" class="text-slate-200">Peak Summer (14h Daylight in Delhi)</span>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-cyan-400 font-bold block mb-1">Southern Hemisphere:</span>
                <span id="sim10_south_status" class="text-slate-200">Peak Winter (Short days in Sydney)</span>
            </div>
        </div>

        <!-- Toggle Buttons -->
        <div class="flex items-center justify-center gap-3 pt-1">
            <button onclick="sim10SetSolstice('june')" id="sim10_june_btn" class="flex-1 py-2 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow-md">
                ☀️ June 21 (Summer Solstice)
            </button>
            <button onclick="sim10SetSolstice('dec')" id="sim10_dec_btn" class="flex-1 py-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                ❄️ Dec 22 (Winter Solstice)
            </button>
        </div>
    </div>
    """,

    # Simulator 11: Equinox Worldwide 12h/12h Balancer
    11: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                <h4 class="text-xs font-bold text-emerald-300 uppercase tracking-wider">Equinox Worldwide Day/Night Balancer</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">March 21 & Sept 23</span>
        </div>

        <!-- SVG Equinox Geometry -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg viewBox="0 0 420 190" class="w-full h-auto max-h-[190px]">
                <!-- Sun Light Rays -->
                <g stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6">
                    <line x1="20" y1="45" x2="150" y2="45"/>
                    <line x1="20" y1="95" x2="150" y2="95"/>
                    <line x1="20" y1="145" x2="150" y2="145"/>
                </g>
                <text x="30" y="25" fill="#fde047" font-size="10" font-weight="bold">☀️ Direct Equator Rays</text>

                <!-- Earth at Equinox -->
                <g transform="translate(250, 95)">
                    <!-- Upright Terminator running directly Pole-to-Pole -->
                    <circle r="65" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <!-- Right Half Night Shadow -->
                    <path d="M 0 -65 A 65 65 0 0 1 0 65 Z" fill="#020617" opacity="0.75"/>

                    <!-- Geographic Poles -->
                    <circle cx="0" cy="-65" r="3" fill="#ffffff"/>
                    <text x="0" y="-72" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">North Pole</text>
                    <circle cx="0" cy="65" r="3" fill="#ffffff"/>
                    <text x="0" y="78" text-anchor="middle" fill="#ffffff" font-size="8">South Pole</text>

                    <!-- Latitude Marker Pins -->
                    <circle id="sim11_pin_eq" cx="-45" cy="0" r="3.5" fill="#facc15"/>
                    <text x="-52" y="3" text-anchor="end" fill="#facc15" font-size="7">Equator: 12h / 12h</text>
                    <circle id="sim11_pin_delhi" cx="-35" cy="-28" r="3.5" fill="#38bdf8"/>
                    <text x="-42" y="-25" text-anchor="end" fill="#38bdf8" font-size="7">Delhi (28°N): 12h / 12h</text>
                    <circle id="sim11_pin_pole" cx="-10" cy="-58" r="3.5" fill="#a855f7"/>
                    <text x="-16" y="-55" text-anchor="end" fill="#a855f7" font-size="7">Arctic: 12h / 12h</text>
                </g>
            </svg>
        </div>

        <!-- Equinox Global Balance Specs -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs">
            <div class="flex items-center justify-between text-slate-300">
                <span class="font-bold text-emerald-400">Equator (0°):</span>
                <span class="font-mono text-cyan-300 font-bold">12h 00m Day • 12h 00m Night</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="font-bold text-emerald-400">New Delhi (28°N):</span>
                <span class="font-mono text-cyan-300 font-bold">12h 00m Day • 12h 00m Night</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
                <span class="font-bold text-emerald-400">London (51°N):</span>
                <span class="font-mono text-cyan-300 font-bold">12h 00m Day • 12h 00m Night</span>
            </div>
        </div>

        <!-- Season Toggle -->
        <div class="flex items-center justify-between gap-3 pt-1">
            <button onclick="sim11SetEquinox('spring')" id="sim11_spring_btn" class="flex-1 py-1.5 rounded-lg bg-emerald-600 text-white font-bold text-xs transition">
                🌱 March 21 (Vernal Equinox)
            </button>
            <button onclick="sim11SetEquinox('autumn')" id="sim11_autumn_btn" class="flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                🍂 Sept 23 (Autumnal Equinox)
            </button>
        </div>
    </div>
    """,

    # Simulator 12: Celestial Shadow Optics: Umbra & Penumbra
    12: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Celestial Shadow Optics: Umbra & Penumbra</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Ray Tracing</span>
        </div>

        <!-- SVG Umbra & Penumbra Diagram -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim12_svg" viewBox="0 0 460 200" class="w-full h-auto max-h-[200px]">
                <!-- Large Extended Light Source: The Sun -->
                <circle cx="45" cy="100" r="35" fill="#f59e0b" filter="drop-shadow(0 0 10px #f59e0b)"/>
                <text x="45" y="104" text-anchor="middle" fill="#030712" font-size="9" font-weight="bold">SUN</text>

                <!-- Opaque Obstacle: The Moon -->
                <circle cx="210" cy="100" r="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
                <text x="210" y="80" text-anchor="middle" fill="#94a3b8" font-size="8">Obstacle</text>

                <!-- Umbra (Dark Inner Cone) -->
                <polygon points="210,86 360,100 210,114" fill="#000000" stroke="#334155" stroke-width="0.8"/>
                <text x="270" y="103" fill="#ffffff" font-size="8" font-weight="bold">UMBRA</text>

                <!-- Penumbra Upper -->
                <polygon points="210,86 450,40 450,90 360,100" fill="#475569" opacity="0.35"/>
                <!-- Penumbra Lower -->
                <polygon points="210,114 360,100 450,110 450,160" fill="#475569" opacity="0.35"/>
                <text x="390" y="65" fill="#cbd5e1" font-size="8">PENUMBRA</text>
                <text x="390" y="145" fill="#cbd5e1" font-size="8">PENUMBRA</text>

                <!-- Ray Tracing Lines -->
                <g stroke="#facc15" stroke-width="1" opacity="0.5">
                    <line x1="45" y1="65" x2="360" y2="100"/>
                    <line x1="45" y1="135" x2="360" y2="100"/>
                    <line x1="45" y1="65" x2="450" y2="160"/>
                    <line x1="45" y1="135" x2="450" y2="40"/>
                </g>

                <!-- Draggable Observer Sensor -->
                <g id="sim12_probe" transform="translate(360, 100)">
                    <circle r="6" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" class="cursor-pointer"/>
                    <text x="0" y="-10" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">Probe</text>
                </g>
            </svg>
        </div>

        <!-- Shadow Probe Readout -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Probe Location:</span>
                <span id="sim12_zone_text" class="text-amber-300 font-bold">Umbra Tip (Total Eclipse)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">What Observer Sees:</span>
                <span id="sim12_view_text" class="text-emerald-400 font-bold">100% Sun Blocked (Corona Visible)</span>
            </div>
        </div>

        <!-- Probe Position Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Move Observer Vertically Across Shadow:</span>
                <span id="sim12_y_val" class="font-mono text-cyan-300">Center (Y = 100)</span>
            </div>
            <input type="range" id="sim12_slider" min="50" max="150" value="100" step="5" oninput="sim12SetProbeY(this.value)"
                   class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Full Sunlight</span>
                <span>Upper Penumbra</span>
                <span>Umbra Core</span>
                <span>Lower Penumbra</span>
                <span>Full Sunlight</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 13: Solar Eclipse Geometry & Path of Totality
    13: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider">Solar Eclipse & Path of Totality</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Sun • Moon • Earth</span>
        </div>

        <!-- SVG Solar Eclipse Diagram -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim13_svg" viewBox="0 0 460 200" class="w-full h-auto max-h-[200px]">
                <!-- Sun on Left -->
                <circle cx="40" cy="100" r="30" fill="#f59e0b" filter="drop-shadow(0 0 10px #f59e0b)"/>
                <text x="40" y="104" text-anchor="middle" fill="#020617" font-size="9" font-weight="bold">SUN</text>

                <!-- New Moon in Middle -->
                <g id="sim13_moon" transform="translate(230, 100)">
                    <circle r="9" fill="#0f172a" stroke="#475569" stroke-width="1"/>
                    <text x="0" y="-14" text-anchor="middle" fill="#cbd5e1" font-size="8">New Moon</text>
                </g>

                <!-- Earth on Right -->
                <g id="sim13_earth" transform="translate(390, 100)">
                    <circle r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="0" y="4" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">EARTH</text>
                    <!-- Umbra Shadow Spot on Earth -->
                    <circle id="sim13_totality_dot" cx="-35" cy="0" r="3" fill="#000000"/>
                </g>

                <!-- Shadow Cones -->
                <g id="sim13_shadows">
                    <!-- Umbra Cone -->
                    <polygon id="sim13_umbra_cone" points="230,91 355,100 230,109" fill="#000000" opacity="0.9"/>
                    <!-- Penumbra Cone -->
                    <polygon id="sim13_penumbra_cone" points="230,91 370,75 370,125 230,109" fill="#64748b" opacity="0.3"/>
                </g>
            </svg>
        </div>

        <!-- Observer Viewport Preview -->
        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center gap-4">
            <!-- Mini Solar View Circle -->
            <div class="w-14 h-14 rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center shrink-0 relative overflow-hidden">
                <circle id="sim13_sky_sun" cx="28" cy="28" r="20" fill="#f59e0b"/>
                <circle id="sim13_sky_moon" cx="28" cy="28" r="20" fill="#020617"/>
            </div>
            <div class="text-xs">
                <span class="text-slate-400 block text-[10px]">What Observers See on Ground:</span>
                <span id="sim13_status_label" class="text-amber-300 font-bold text-sm block">Total Solar Eclipse (Totality)</span>
                <span class="text-slate-300 text-[11px]">Solar corona visible; stars appear in daytime sky!</span>
            </div>
        </div>

        <!-- Moon Alignment Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Moon Orbital Alignment:</span>
                <span id="sim13_slider_val" class="font-mono text-cyan-300">Exact Syzygy (0)</span>
            </div>
            <input type="range" id="sim13_slider" min="-20" max="20" value="0" step="2" oninput="sim13SetMoonOffset(this.value)"
                   class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Misses Above (No Eclipse)</span>
                <span>Totality</span>
                <span>Misses Below (No Eclipse)</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 14: 400:1 Cosmic Ratio & Pinhole Projection Box
    14: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider">The 400:1 Ratio & Pinhole Projection</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Angular Size: ~0.5°</span>
        </div>

        <!-- SVG Pinhole Projection Demonstration -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim14_svg" viewBox="0 0 450 190" class="w-full h-auto max-h-[190px]">
                <!-- Partial Eclipsed Sun in Sky -->
                <g transform="translate(60, 95)">
                    <circle cx="0" cy="0" r="26" fill="#f59e0b"/>
                    <circle cx="10" cy="-6" r="24" fill="#020617"/>
                    <text x="0" y="42" text-anchor="middle" fill="#fde047" font-size="8">Crescent Sun in Sky</text>
                </g>

                <!-- Straight Rays Passing Through Pinhole -->
                <line x1="86" y1="75" x2="250" y2="95" stroke="#facc15" stroke-width="1.2" stroke-dasharray="2,2"/>
                <line x1="86" y1="115" x2="250" y2="95" stroke="#facc15" stroke-width="1.2" stroke-dasharray="2,2"/>
                <line x1="250" y1="95" x2="380" y2="115" stroke="#facc15" stroke-width="1.2" stroke-dasharray="2,2"/>
                <line x1="250" y1="95" x2="380" y2="75" stroke="#facc15" stroke-width="1.2" stroke-dasharray="2,2"/>

                <!-- Pinhole Cardboard Barrier -->
                <rect x="248" y="30" width="4" height="55" fill="#475569"/>
                <rect x="248" y="105" width="4" height="55" fill="#475569"/>
                <text x="250" y="22" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="bold">Pinhole Foil</text>

                <!-- Projection Screen Cardboard -->
                <rect x="380" y="35" width="6" height="120" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
                <text x="383" y="25" text-anchor="middle" fill="#f8fafc" font-size="8">White Screen</text>

                <!-- Inverted Real Image of Crescent Sun on Screen -->
                <g transform="translate(378, 95)">
                    <circle cx="-6" cy="0" r="14" fill="#f59e0b"/>
                    <circle cx="-12" cy="4" r="13" fill="#ffffff"/>
                    <text x="-25" y="28" text-anchor="end" fill="#38bdf8" font-size="7">Inverted Safe Image</text>
                </g>
            </svg>
        </div>

        <!-- 400:1 Math Proof -->
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-amber-400 font-bold block">Sun vs Moon Diameter:</span>
                <span class="text-slate-300 font-mono text-[11px]">1,392,700 ÷ 3,474 ≈ <strong>400.9×</strong></span>
            </div>
            <div class="p-2 rounded-xl bg-slate-950/70 border border-slate-800">
                <span class="text-cyan-400 font-bold block">Sun vs Moon Distance:</span>
                <span class="text-slate-300 font-mono text-[11px]">149,600,000 ÷ 384,400 ≈ <strong>389.2×</strong></span>
            </div>
        </div>

        <p class="text-[11px] text-emerald-300 bg-emerald-950/30 p-2.5 rounded-xl border border-emerald-500/30">
            ✅ <strong>Safe Observation:</strong> A pinhole projector projects a real, inverted image of the solar eclipse onto white cardboard with zero danger to human eyes!
        </p>
    </div>
    """,

    # Simulator 15: Lunar Eclipse Orbital Stages
    15: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider">Lunar Eclipse: Earth's Shadow Cone</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Sun • Earth • Moon</span>
        </div>

        <!-- SVG Lunar Eclipse Geometry -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim15_svg" viewBox="0 0 460 200" class="w-full h-auto max-h-[200px]">
                <!-- Sun Light Rays from Left -->
                <circle cx="20" cy="100" r="25" fill="#f59e0b"/>
                <text x="20" y="104" text-anchor="middle" fill="#030712" font-size="8" font-weight="bold">SUN</text>

                <!-- Earth in Middle -->
                <circle cx="160" cy="100" r="26" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="160" y="104" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">EARTH</text>

                <!-- Earth's Giant Shadow Cones -->
                <!-- Umbra Cone -->
                <polygon points="160,76 360,100 160,124" fill="#000000" stroke="#334155" stroke-width="0.8"/>
                <text x="250" y="103" fill="#ef4444" font-size="8" font-weight="bold">UMBRA (Dark Red)</text>

                <!-- Penumbra Cones -->
                <polygon points="160,76 450,45 450,85 360,100" fill="#475569" opacity="0.3"/>
                <polygon points="160,124 360,100 450,115 450,155" fill="#475569" opacity="0.3"/>
                <text x="390" y="70" fill="#cbd5e1" font-size="7">PENUMBRA</text>

                <!-- Orbiting Moon -->
                <g id="sim15_moon" transform="translate(300, 100)">
                    <circle r="9" fill="#f87171" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="0" y="-14" text-anchor="middle" fill="#f87171" font-size="8" font-weight="bold">Full Moon</text>
                </g>
            </svg>
        </div>

        <!-- Lunar Stage Readout -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Eclipse Phase:</span>
                <span id="sim15_phase_text" class="text-rose-400 font-bold text-sm">Total Lunar Eclipse (Totality)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Lunar Appearance:</span>
                <span id="sim15_color_text" class="text-rose-300 font-bold text-sm">Glowing Copper-Red (Blood Moon)</span>
            </div>
        </div>

        <!-- Moon Position Slider -->
        <div class="space-y-1">
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span>Advance Moon Across Earth's Shadow:</span>
                <span id="sim15_slider_val" class="font-mono text-cyan-300">Center Umbra</span>
            </div>
            <input type="range" id="sim15_slider" min="50" max="150" value="100" step="5" oninput="sim15SetMoonY(this.value)"
                   class="w-full accent-rose-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                <span>Normal Full Moon</span>
                <span>Partial Umbra</span>
                <span>Totality</span>
                <span>Partial Umbra</span>
                <span>Normal Full Moon</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 16: The Blood Moon & 5° Orbital Tilt
    16: """
    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700/80 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-500 animate-pulse"></span>
                <h4 class="text-xs font-bold text-rose-300 uppercase tracking-wider">The 5.14° Orbital Tilt & Node Alignment</h4>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">Why Eclipses Are Rare</span>
        </div>

        <!-- SVG 3D-Tilt Orbital Ring -->
        <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 overflow-hidden flex items-center justify-center min-h-[220px]">
            <svg id="sim16_svg" viewBox="0 0 460 200" class="w-full h-auto max-h-[200px]">
                <!-- Earth Orbital Plane (Flat Ecliptic) -->
                <ellipse cx="230" cy="100" rx="190" ry="25" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3"/>
                <text x="430" y="104" text-anchor="end" fill="#94a3b8" font-size="8">Ecliptic Plane (Earth Orbit)</text>

                <!-- Central Earth -->
                <circle cx="230" cy="100" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="230" y="104" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">EARTH</text>

                <!-- Tilted Moon Orbit (Angle variable) -->
                <g id="sim16_tilted_orbit" transform="rotate(5.14, 230, 100)">
                    <ellipse cx="230" cy="100" rx="140" ry="40" fill="none" stroke="#f43f5e" stroke-width="1.8"/>
                    <text x="350" y="70" fill="#f43f5e" font-size="8" font-weight="bold">Moon's 5.14° Tilted Orbit</text>

                    <!-- Moon at High Point -->
                    <circle id="sim16_moon" cx="370" cy="100" r="7" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
                </g>

                <!-- Nodes (Intersection Points) -->
                <circle cx="90" cy="100" r="3" fill="#22c55e"/>
                <text x="90" y="115" text-anchor="middle" fill="#22c55e" font-size="8">Node (Rahu)</text>
                <circle cx="370" cy="100" r="3" fill="#22c55e"/>
                <text x="370" y="115" text-anchor="middle" fill="#22c55e" font-size="8">Node (Ketu)</text>
            </svg>
        </div>

        <!-- Orbital Status Box -->
        <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 flex items-center justify-between text-xs">
            <div>
                <span class="text-slate-400 block text-[10px]">Orbital Plane Tilt:</span>
                <span id="sim16_tilt_label" class="text-amber-300 font-mono font-bold text-sm">5.14° (Real Moon Orbit)</span>
            </div>
            <div class="text-right">
                <span class="text-slate-400 block text-[10px]">Eclipse Feasibility:</span>
                <span id="sim16_feasibility" class="text-cyan-300 font-bold">Misses Shadow (No Eclipse)</span>
            </div>
        </div>

        <!-- Tilt Toggle Controls -->
        <div class="flex items-center justify-between gap-3 pt-1">
            <button onclick="sim16SetTilt(5.14)" id="sim16_real_btn" class="flex-1 py-1.5 rounded-lg bg-rose-600 text-white font-bold text-xs transition shadow-md">
                5.14° Real Tilt (Eclipses Rare)
            </button>
            <button onclick="sim16SetTilt(0)" id="sim16_zero_btn" class="flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition">
                0° Flat Orbit (Eclipse Every Month!)
            </button>
        </div>
    </div>
    """
}
'''
    with open(".agents/class7_science_earth_moon_sun_sims.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully generated .agents/class7_science_earth_moon_sun_sims.py with 16 bespoke simulators.")

if __name__ == "__main__":
    create_sims_file()


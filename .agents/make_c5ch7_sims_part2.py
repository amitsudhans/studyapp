"""
Simulators 9 to 16 for NCERT Class 5 Science Chapter 7: Energy - How Things Work
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMS = {}

# SIM 9: Filament Bulb vs Solid-State LED Energy Efficiency Duel
SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Energy Efficiency: Filament vs Modern LED</span>
        <p class="text-[11px] text-slate-400">See how old filament bulbs waste 90% as heat while cool LEDs save power!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Left Side: Incandescent Bulb -->
            <g transform="translate(100, 110)">
                <rect x="-70" y="-75" width="140" height="150" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" opacity="0.6"/>
                <text x="0" y="-55" text-anchor="middle" fill="#f87171" font-size="8" font-weight="bold">Traditional 60W Bulb</text>
                <!-- Bulb Outline -->
                <circle cx="0" cy="-10" r="22" fill="#fef08a" opacity="0.4"/>
                <circle cx="0" cy="-10" r="16" fill="#facc15" opacity="0.8"/>
                <!-- Tungsten Filament wire -->
                <path d="M -6,0 L -3,-18 L 0,-10 L 3,-18 L 6,0" stroke="#ea580c" stroke-width="1.5" fill="none"/>
                <!-- Base -->
                <rect x="-8" y="10" width="16" height="12" fill="#64748b"/>

                <!-- Heat Wave Radiation lines (90% wasted heat!) -->
                <path d="M -30,-25 Q -40,-35 -30,-45" stroke="#ef4444" stroke-width="1.5" fill="none"/>
                <path d="M 30,-25 Q 40,-35 30,-45" stroke="#ef4444" stroke-width="1.5" fill="none"/>
                <text x="0" y="42" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="bold">90% Wasted Heat 🔥</text>
                <text x="0" y="55" text-anchor="middle" fill="#fca5a5" font-size="7">Only 10% Light</text>
            </g>

            <!-- Right Side: Solid-State LED -->
            <g transform="translate(300, 110)">
                <rect x="-70" y="-75" width="140" height="150" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5" opacity="0.6"/>
                <text x="0" y="-55" text-anchor="middle" fill="#6ee7b7" font-size="8" font-weight="bold">Modern 9W LED Bulb</text>
                <!-- LED Dome -->
                <ellipse cx="0" cy="-12" rx="20" ry="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
                <!-- Semiconductor Chip Grid -->
                <rect x="-6" y="-14" width="12" height="6" fill="#facc15"/>
                <rect x="-10" y="4" width="20" height="18" fill="#64748b"/>

                <!-- Clean Light Beams (85% useful light, cool body) -->
                <line x1="-28" y1="-28" x2="-38" y2="-38" stroke="#34d399" stroke-width="1.5"/>
                <line x1="28" y1="-28" x2="38" y2="-38" stroke="#34d399" stroke-width="1.5"/>
                <line x1="0" y1="-34" x2="0" y2="-44" stroke="#34d399" stroke-width="1.5"/>
                <text x="0" y="42" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">85% Useful Light 🌟</text>
                <text x="0" y="55" text-anchor="middle" fill="#a7f3d0" font-size="7">Stays Cool & Saves Bills</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleBulbComparison('filament')" id="btnFilament" class="py-2 px-3 rounded-xl text-xs font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200 transition">
            <span>Inspect 60W Filament (Hot)</span>
        </button>
        <button onclick="toggleBulbComparison('led')" id="btnLED" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200 transition">
            <span>Inspect 9W LED (Efficient)</span>
        </button>
    </div>
    <div id="sim9Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Lumen Efficiency:</span> A 9W LED produces the exact same brightness as an old 60W bulb, cutting electricity consumption by 85%!
    </div>
</div>
"""

# SIM 10: Electric Safety Simulator & MCB Circuit Breaker
SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Electric Safety & Circuit Breaker (MCB) Lab</span>
        <p class="text-[11px] text-slate-400">Never touch switches with wet hands! Test how safety breakers trip during overloads.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Distribution Box Board -->
            <rect x="50" y="30" width="300" height="175" rx="10" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            <text x="200" y="50" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="bold">Home Electrical Protection Panel</text>

            <!-- MCB Switch in Center -->
            <g transform="translate(160, 70)">
                <rect x="0" y="0" width="80" height="95" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
                <!-- MCB Toggle Lever -->
                <rect id="mcbLever" x="30" y="20" width="20" height="35" rx="4" fill="#22c55e" stroke="#16a34a" stroke-width="1"/>
                <text id="mcbStateText" x="40" y="75" text-anchor="middle" fill="#4ade80" font-size="8" font-weight="bold">MCB: ON</text>
            </g>

            <!-- Hand Moisture Condition Display (Left) -->
            <g transform="translate(70, 75)">
                <rect x="0" y="0" width="75" height="85" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
                <text x="37" y="16" text-anchor="middle" fill="#94a3b8" font-size="7">Skin State</text>
                <text id="skinStateIcon" x="37" y="42" text-anchor="middle" font-size="20">✋</text>
                <text id="skinStateText" x="37" y="62" text-anchor="middle" fill="#34d399" font-size="7" font-weight="bold">Dry (Safe)</text>
                <text id="skinResistanceText" x="37" y="74" text-anchor="middle" fill="#94a3b8" font-size="6">100,000 Ω</text>
            </g>

            <!-- Overload Load Station (Right) -->
            <g transform="translate(255, 75)">
                <rect x="0" y="0" width="75" height="85" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
                <text x="37" y="16" text-anchor="middle" fill="#94a3b8" font-size="7">Circuit Current</text>
                <text id="currentLoadText" x="37" y="42" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">4 A</text>
                <text id="loadStatusText" x="37" y="62" text-anchor="middle" fill="#38bdf8" font-size="7">Normal Load</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="setHandMoisture(false)" class="py-1.5 px-2 rounded-xl font-bold bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200">Dry Hands (Safe)</button>
        <button onclick="setHandMoisture(true)" class="py-1.5 px-2 rounded-xl font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200">Wet Hands (DANGER!)</button>
        <button onclick="simulateCircuitOverload()" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Trip MCB Overload</button>
    </div>
    <div id="sim10Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Safety Rule:</span> Wet hands contain mineral salts that drop electrical resistance from 100,000 ohms to under 1,000 ohms, allowing dangerous current into the body!
    </div>
</div>
"""

# SIM 11: Clean Energy vs Coal Emission Monitor
SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Clean Energy vs Coal Emission Monitor</span>
        <p class="text-[11px] text-slate-400">Compare polluting fossil fuel smoke against zero-emission solar and wind energy!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Left Half: Coal Thermal Power Plant -->
            <rect x="10" y="30" width="185" height="180" rx="8" fill="#1e1b18" stroke="#78350f" stroke-width="1.5"/>
            <text x="102" y="50" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="bold">Coal Thermal Power (Fossil Fuel)</text>

            <!-- Factory & Chimney -->
            <rect x="70" y="120" width="65" height="70" fill="#451a03"/>
            <rect x="85" y="70" width="20" height="50" fill="#292524"/>

            <!-- Smoke Plumes billowing out -->
            <circle cx="95" cy="55" r="14" fill="#52525b" opacity="0.8"/>
            <circle cx="85" cy="42" r="18" fill="#3f3f46" opacity="0.9"/>
            <circle cx="110" cy="38" r="16" fill="#27272a" opacity="0.9"/>
            <text x="102" y="175" text-anchor="middle" fill="#ef4444" font-size="7" font-weight="bold">PM2.5, SO2 & CO2 Smoke</text>

            <!-- Right Half: Solar & Wind Clean Generation -->
            <rect x="205" y="30" width="185" height="180" rx="8" fill="#042f2e" stroke="#059669" stroke-width="1.5"/>
            <text x="297" y="50" text-anchor="middle" fill="#6ee7b7" font-size="8" font-weight="bold">Renewable Solar & Wind Farm</text>

            <!-- Sun in Sky -->
            <circle cx="250" cy="75" r="12" fill="#facc15"/>
            <!-- Solar PV Panel -->
            <polygon points="230,150 270,150 280,180 220,180" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <!-- Wind Turbine Tower & Blades -->
            <line x1="335" y1="180" x2="335" y2="105" stroke="#cbd5e1" stroke-width="3"/>
            <circle cx="335" cy="105" r="4" fill="#94a3b8"/>
            <!-- 3 Blades -->
            <line x1="335" y1="105" x2="335" y2="75" stroke="#f8fafc" stroke-width="2"/>
            <line x1="335" y1="105" x2="310" y2="120" stroke="#f8fafc" stroke-width="2"/>
            <line x1="335" y1="105" x2="360" y2="120" stroke="#f8fafc" stroke-width="2"/>

            <text x="297" y="175" text-anchor="middle" fill="#34d399" font-size="7" font-weight="bold">Zero Emissions (100% Clean)</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="inspectPowerType('coal')" class="py-2 px-3 rounded-xl text-xs font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200 transition">
            <span>Analyze Coal Emissions</span>
        </button>
        <button onclick="inspectPowerType('clean')" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200 transition">
            <span>Analyze Renewable Clean Power</span>
        </button>
    </div>
    <div id="sim11Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Clean Energy Truth:</span> Solar panels and wind turbines produce zero smoke, zero soot, and zero carbon emissions, keeping our atmosphere clean and healthy!
    </div>
</div>
"""

# SIM 12: Aerodynamic Pinwheel & Wind Velocity Tunnel (Activity 6)
SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Aerodynamic Pinwheel Wind Tunnel</span>
        <p class="text-[11px] text-slate-400">Activity 6: Adjust wind velocity to see the paper pinwheel convert air into rotation!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Wind Stream Vectors -->
            <g id="pinwheelWindLines" class="opacity-40">
                <line x1="20" y1="70" x2="160" y2="70" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,4"/>
                <line x1="10" y1="110" x2="160" y2="110" stroke="#38bdf8" stroke-width="3" stroke-dasharray="10,5"/>
                <line x1="20" y1="150" x2="160" y2="150" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,4"/>
            </g>

            <!-- Support Stick & Pencil -->
            <rect x="220" y="115" width="8" height="110" fill="#a16207" rx="2"/>

            <!-- Pinwheel Rotor Assembly (Rotates with JS) -->
            <g id="pinwheelRotor" transform="translate(224, 115)">
                <!-- 4 Colored Curved Paper Vanes -->
                <!-- Vane 1: Red -->
                <path d="M 0,0 L 0,-45 Q 25,-45 0,0 Z" fill="#ef4444"/>
                <!-- Vane 2: Yellow -->
                <path d="M 0,0 L 45,0 Q 45,25 0,0 Z" fill="#facc15"/>
                <!-- Vane 3: Blue -->
                <path d="M 0,0 L 0,45 Q -25,45 0,0 Z" fill="#3b82f6"/>
                <!-- Vane 4: Green -->
                <path d="M 0,0 L -45,0 Q -45,-25 0,0 Z" fill="#22c55e"/>

                <!-- Central Pushpin -->
                <circle cx="0" cy="0" r="5" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
            </g>

            <!-- Wind Gauge -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="130" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="65" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Wind Speed & RPM</text>
                <text id="pinwheelRpmText" x="65" y="28" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">120 RPM (Breeze)</text>
                <text id="pinwheelSpeedText" x="65" y="38" text-anchor="middle" fill="#7dd3fc" font-size="7">Wind: 25 km/h</text>
            </g>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Blowing Wind Speed:</span>
            <span id="pinwheelSliderLabel" class="font-bold text-cyan-400">25 km/h (Moderate)</span>
        </div>
        <input type="range" id="pinwheelSlider" min="0" max="60" value="25" oninput="updatePinwheelSpeed(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
    </div>
    <div id="sim12Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Kinetic Conversion:</span> Rushing air molecules strike the cupped curved blades, converting straight-line wind force into continuous rotary torque!
    </div>
</div>
"""

# SIM 13: Convex Sun Lens Focal Ignition Lab (Activity 7)
SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Convex Lens Solar Focal Ignition Lab</span>
        <p class="text-[11px] text-slate-400">Activity 7: Adjust lens distance to focus sunlight rays into a scorching focal point!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/20 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Parallel Sunlight Rays Incoming from Sky -->
            <line x1="160" y1="20" x2="160" y2="80" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2"/>
            <line x1="180" y1="20" x2="180" y2="80" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2"/>
            <line x1="200" y1="20" x2="200" y2="80" stroke="#facc15" stroke-width="2"/>
            <line x1="220" y1="20" x2="220" y2="80" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2"/>
            <line x1="240" y1="20" x2="240" y2="80" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2"/>
            <text x="200" y="16" text-anchor="middle" fill="#fde047" font-size="8">Parallel Sunlight Rays</text>

            <!-- Magnifying Glass Lens (Movable with slider) -->
            <g id="magnifyingLensGroup" transform="translate(200, 80)">
                <!-- Glass Lens Rim -->
                <ellipse cx="0" cy="0" rx="45" ry="10" fill="#38bdf8" opacity="0.3" stroke="#94a3b8" stroke-width="2"/>
                <!-- Wooden Handle -->
                <line x1="45" y1="0" x2="90" y2="0" stroke="#a16207" stroke-width="6" stroke-linecap="round"/>
            </g>

            <!-- Refracted Converging Light Rays -->
            <path id="focalRays" d="M 160,80 L 200,185 L 240,80" fill="none" stroke="#fde047" stroke-width="2" opacity="0.8"/>

            <!-- Dry Leaf on Stone Slab at Bottom -->
            <rect x="130" y="195" width="140" height="20" rx="3" fill="#475569"/>
            <path d="M 170,192 C 180,180 220,180 230,192 C 210,198 190,198 170,192 Z" fill="#854d0e" stroke="#713f12" stroke-width="1"/>

            <!-- Burning Focal Spot & Smoke (Active at exact focus) -->
            <circle id="focalHotSpot" cx="200" cy="186" r="3" fill="#ffffff" stroke="#ef4444" stroke-width="2">
                <animate attributeName="r" values="2;4;2" dur="0.8s" repeatCount="indefinite"/>
            </circle>
            <!-- Smoke Particles -->
            <g id="leafSmoke" class="opacity-80">
                <circle cx="200" cy="175" r="4" fill="#cbd5e1" opacity="0.5"/>
                <circle cx="198" cy="162" r="6" fill="#cbd5e1" opacity="0.4"/>
                <circle cx="203" cy="148" r="8" fill="#cbd5e1" opacity="0.3"/>
            </g>

            <!-- Temperature Callout -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="130" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="65" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Focal Spot Temperature</text>
                <text id="focalTempText" x="65" y="28" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="bold">265°C (Ignition!)</text>
                <text id="focalStatusText" x="65" y="38" text-anchor="middle" fill="#fde047" font-size="7">Leaf Smouldering</text>
            </g>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Lens Focal Distance:</span>
            <span id="lensHeightLabel" class="font-bold text-amber-400">Optimal Focus (Hotspot)</span>
        </div>
        <input type="range" id="lensSlider" min="40" max="120" value="80" oninput="updateLensFocus(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
    </div>
    <div id="sim13Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Refraction Focus:</span> Convex lenses refract parallel sunlight rays to a microscopic focal spot, concentrating radiant energy to surpass 250°C!
    </div>
</div>
"""

# SIM 14: Homemade Water Wheel & Mechanical Hoist (Activity 8)
SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Homemade Water Wheel & Hoist Lab</span>
        <p class="text-[11px] text-slate-400">Activity 8: Falling water spins spoon paddles to lift a suspended weight!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Water Pitcher Pouring at Top -->
            <g transform="translate(140, 20)">
                <ellipse cx="0" cy="0" rx="14" ry="8" fill="#0284c7"/>
                <path d="M -14,0 L -8,25 L 8,25 L 14,0 Z" fill="#0369a1"/>
            </g>
            <!-- Water Stream Falling onto Left Spoons -->
            <path id="fallingStream" d="M 135,45 Q 145,80 155,100" stroke="#38bdf8" stroke-width="4" fill="none" stroke-dasharray="6,2"/>

            <!-- Water Wheel Assembly (Spins with JS) -->
            <g id="waterWheelGroup" transform="translate(190, 115)">
                <!-- Central Cork Disc -->
                <circle cx="0" cy="0" r="22" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                <!-- Axle Spoke -->
                <circle cx="0" cy="0" r="5" fill="#f8fafc"/>

                <!-- 6 Radial Spoon Blades -->
                <!-- Blade 1: Top -->
                <line x1="0" y1="-22" x2="0" y2="-50" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="0" cy="-50" r="7" fill="#cbd5e1"/>
                <!-- Blade 2: Top-Right -->
                <line x1="19" y1="-11" x2="43" y2="-25" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="43" cy="-25" r="7" fill="#cbd5e1"/>
                <!-- Blade 3: Bottom-Right -->
                <line x1="19" y1="11" x2="43" y2="25" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="43" cy="25" r="7" fill="#cbd5e1"/>
                <!-- Blade 4: Bottom -->
                <line x1="0" y1="22" x2="0" y2="50" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="0" cy="50" r="7" fill="#cbd5e1"/>
                <!-- Blade 5: Bottom-Left -->
                <line x1="-19" y1="11" x2="-43" y2="25" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="-43" cy="25" r="7" fill="#cbd5e1"/>
                <!-- Blade 6: Top-Left (Receiving Water Impact) -->
                <line x1="-19" y1="-11" x2="-43" y2="-25" stroke="#94a3b8" stroke-width="3"/>
                <circle cx="-43" cy="-25" r="7" fill="#cbd5e1"/>
            </g>

            <!-- Suspended Thread & Weight on Right -->
            <line x1="190" y1="115" x2="280" y2="115" stroke="#cbd5e1" stroke-width="2"/>
            <line id="hoistThread" x1="280" y1="115" x2="280" y2="185" stroke="#cbd5e1" stroke-width="1.5"/>
            <!-- Suspended Weight (Moves up when rotating) -->
            <rect id="hoistWeight" x="272" y="185" width="16" height="18" rx="2" fill="#eab308" stroke="#ca8a04" stroke-width="1"/>
            <text x="280" y="215" text-anchor="middle" fill="#fde047" font-size="7">Weight Lifted</text>

            <!-- Hydro Power Gauge -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="120" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="60" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Water Flow Rate</text>
                <text id="waterFlowRateText" x="60" y="28" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="bold">Medium Stream</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleWaterStream(true)" id="btnWaterStart" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
            <span>Pour Water (Spin Wheel)</span>
        </button>
        <button onclick="toggleWaterStream(false)" id="btnWaterStop" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
            <span>Stop Water (Rest)</span>
        </button>
    </div>
    <div id="sim14Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Mechanical Work:</span> Gravitational potential energy of falling water converts into rotational kinetic power, effortlessly hoisting the weight!
    </div>
</div>
"""

# SIM 15: Himalayan Gharaat Watermill (Traditional Hydro Power)
SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Traditional Himalayan Gharaat (Watermill)</span>
        <p class="text-[11px] text-slate-400">Discover zero-carbon engineering: mountain stream power grinding whole grain into flour!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-emerald-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Mountain Slope & Cottage Outline -->
            <path d="M 0,160 L 80,110 L 400,110 L 400,240 L 0,240 Z" fill="#1e293b"/>
            <!-- Upper Milling Floor -->
            <rect x="180" y="55" width="160" height="55" fill="#334155" stroke="#475569" stroke-width="1.5"/>
            <text x="260" y="72" text-anchor="middle" fill="#e2e8f0" font-size="8" font-weight="bold">Upper Milling Room</text>

            <!-- Circular Grinding Stones in Upper Room -->
            <ellipse cx="260" cy="95" rx="30" ry="10" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
            <!-- Grain Hopper Funnel above stone -->
            <polygon points="250,75 270,75 262,85 258,85" fill="#eab308"/>
            <text x="260" y="82" text-anchor="middle" fill="#0f172a" font-size="6">Wheat</text>

            <!-- Vertical Wooden Drive Spindle connecting upstairs stone to downstairs turbine -->
            <line x1="260" y1="95" x2="260" y2="185" stroke="#a16207" stroke-width="6"/>

            <!-- High-Speed Water Chute (Flume / Penstock) -->
            <path d="M 50,80 L 120,130 L 220,185" fill="none" stroke="#78350f" stroke-width="12" stroke-linecap="round"/>
            <!-- Mountain Torrent Water rushing down chute -->
            <path d="M 50,80 L 120,130 L 220,185" fill="none" stroke="#38bdf8" stroke-width="6" stroke-dasharray="8,4"/>

            <!-- Submerged Wooden Turbine Runner (Panchakkari) downstairs -->
            <g id="gharaatRunner" transform="translate(260, 185)">
                <circle cx="0" cy="0" r="14" fill="#78350f"/>
                <line x1="-25" y1="0" x2="25" y2="0" stroke="#ca8a04" stroke-width="4"/>
                <line x1="0" y1="-25" x2="0" y2="25" stroke="#ca8a04" stroke-width="4"/>
            </g>

            <!-- Discharge Tailrace Water Flow -->
            <path d="M 270,195 Q 330,205 400,200" stroke="#0284c7" stroke-width="8" fill="none"/>
            <text x="350" y="195" fill="#7dd3fc" font-size="7">Tailrace Outflow</text>

            <!-- Status Indicator -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="135" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="67" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Milling Status</text>
                <text id="gharaatStatusText" x="67" y="28" text-anchor="middle" fill="#34d399" font-size="9" font-weight="bold">Water Mill Grinding</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleGharaatFlow(true)" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">
            <span>Divert Stream (Grind Wheat)</span>
        </button>
        <button onclick="toggleGharaatFlow(false)" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
            <span>Close Sluice Gate (Halt)</span>
        </button>
    </div>
    <div id="sim15Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Traditional Clean Tech:</span> Operating for centuries with zero fuel and zero smoke, Gharaats produce fresh nutritious flour while preserving cold-milling vitamins!
    </div>
</div>
"""

# SIM 16: Green Energy Grid & Home Conservation Dashboard
SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Eco-Smart Home & Renewable Grid Dashboard</span>
        <p class="text-[11px] text-slate-400">Combine solar rooftop generation with smart daily conservation habits!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Modern Eco House -->
            <rect x="70" y="90" width="160" height="110" rx="4" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <!-- Slanted Rooftop with Solar PV Array -->
            <polygon points="50,90 150,45 250,90" fill="#334155"/>
            <!-- Solar Panels on Roof -->
            <polygon points="75,85 145,50 175,70 105,85" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="130" y="68" fill="#ffffff" font-size="7" font-weight="bold">Rooftop Solar</text>

            <!-- House Windows & Room Appliances -->
            <!-- Room 1 Light -->
            <rect id="houseWindow1" x="90" y="110" width="30" height="30" fill="#fde047" stroke="#ca8a04" stroke-width="1.5"/>
            <text x="105" y="128" text-anchor="middle" font-size="10">💡</text>
            <!-- Room 2 Fan -->
            <rect id="houseWindow2" x="175" y="110" width="30" height="30" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
            <text x="190" y="128" text-anchor="middle" font-size="10">🌀</text>

            <!-- Outdoor Natural Sun Clothesline -->
            <line x1="260" y1="130" x2="360" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="260" y1="130" x2="260" y2="190" stroke="#64748b" stroke-width="3"/>
            <line x1="360" y1="130" x2="360" y2="190" stroke="#64748b" stroke-width="3"/>
            <!-- Clothes on line drying in sun -->
            <rect x="280" y="132" width="22" height="28" rx="2" fill="#f43f5e"/>
            <rect x="315" y="132" width="25" height="25" rx="2" fill="#38bdf8"/>
            <text x="310" y="175" text-anchor="middle" fill="#a7f3d0" font-size="7">Solar Drying</text>

            <!-- Net Zero Energy Meter (Right Top) -->
            <g transform="translate(265, 30)">
                <rect x="0" y="0" width="120" height="75" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                <text x="60" y="18" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">ECO STAR RATING</text>
                <text id="ecoStarScore" x="60" y="44" text-anchor="middle" fill="#fde047" font-size="18" font-weight="bold">★★★★★</text>
                <text id="netEnergyText" x="60" y="62" text-anchor="middle" fill="#34d399" font-size="7">Net Zero Green Home</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="toggleEcoAction('lights')" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Switch Off Empty Room</button>
        <button onclick="toggleEcoAction('unplug')" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Unplug Vampire Charger</button>
        <button onclick="toggleEcoAction('clothes')" class="py-1.5 px-2 rounded-xl font-bold bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200">Sun-Dry Clothes</button>
    </div>
    <div id="sim16Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Earth Guardian:</span> The cleanest kilowatt of energy is the one you never waste! Every simple habit protects our atmosphere.
    </div>
</div>
"""

print("Sims 9-16 defined successfully")


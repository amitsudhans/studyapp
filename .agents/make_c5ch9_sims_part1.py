"""
Simulators 1 to 8 for NCERT Class 5 Science Chapter 9: Rhythms of Nature
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMS = {}

# SIM 1: Nature's Clock (Time Scales of Change)
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Time Scales of Change Laboratory</span>
        <p class="text-[11px] text-slate-400">Discover how nature changes across different paces: seconds, hours, and years!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Central Display Stage Canvas -->
            <g id="sim1StageCanvas">
                <!-- Mode 1 (Default): Seconds (Bouncing Ball & Blinking Eye) -->
                <circle cx="200" cy="120" r="28" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
                <ellipse cx="200" cy="120" rx="18" ry="12" fill="#0f172a"/>
                <circle cx="200" cy="120" r="5" fill="#38bdf8"/>
                <!-- Speed shockwave rings -->
                <circle cx="200" cy="120" r="45" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6">
                    <animate attributeName="r" values="35;65;35" dur="1.5s" repeatCount="indefinite"/>
                </circle>
                <text x="200" y="185" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Rapid Change: Blinking Eye (0.3 Seconds)</text>
            </g>

            <!-- Time Scale Indicator Card -->
            <rect x="25" y="20" width="130" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="34" fill="#94a3b8" font-size="8">CURRENT TIME SCALE</text>
            <text id="sim1ScaleTitle" x="35" y="50" fill="#38bdf8" font-size="11" font-weight="bold">Seconds Scale</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setSim1Scale('seconds')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-sky-500/50 text-xs font-semibold text-sky-300">
            1. Seconds (Blink/Bounce)
        </button>
        <button onclick="setSim1Scale('hours')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">
            2. Hours (Sun & Shadow)
        </button>
        <button onclick="setSim1Scale('years')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-emerald-500/50 text-xs font-semibold text-emerald-300">
            3. Years (Sapling to Tree)
        </button>
    </div>
    <div id="sim1Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Seconds Scale:</strong> Quick physical actions like blinking an eye or catching a dropped cricket ball happen in fractions of a second.
    </div>
</div>
"""

# SIM 2: Day and Night (Torch & Globe Illumination Model)
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Torch & Globe Day-Night Simulator</span>
        <p class="text-[11px] text-slate-400">Model Activity 1: See how a stationary Sun lights up half the spinning Earth at a time.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Stationary Torch (Left - Sun Model) -->
            <g id="torchSource" transform="translate(40, 95)">
                <rect x="0" y="10" width="50" height="30" rx="4" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
                <polygon points="50,5 75,-5 75,55 50,45" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Bulb beam -->
                <circle cx="75" cy="25" r="8" fill="#facc15"/>
                <!-- Yellow Light Cone Beam expanding across canvas -->
                <polygon points="75,25 240,40 240,200" fill="#fef08a" opacity="0.25"/>
                <line x1="75" y1="25" x2="240" y2="40" stroke="#fef08a" stroke-width="1" stroke-dasharray="3,2" opacity="0.6"/>
                <line x1="75" y1="25" x2="240" y2="200" stroke="#fef08a" stroke-width="1" stroke-dasharray="3,2" opacity="0.6"/>
                <text x="35" y="60" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Torch (Sun)</text>
            </g>

            <!-- Spinning Globe (Right - Earth Model) -->
            <g id="globeModel" transform="translate(250, 120)">
                <!-- Tilted Axis Rod -->
                <line x1="-30" y1="-75" x2="30" y2="75" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                <!-- Globe Sphere (Radius 50) -->
                <!-- Dark Hemisphere (Facing away, Right) -->
                <circle cx="0" cy="0" r="50" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                <!-- Lit Hemisphere (Facing torch, Left) -->
                <path d="M 0,-50 A 50 50 0 0 0 0,50 Z" fill="#0284c7" opacity="0.9"/>
                <!-- Continents on Lit Side -->
                <ellipse cx="-20" cy="-10" rx="14" ry="18" fill="#22c55e" opacity="0.8"/>
                <ellipse cx="-25" cy="20" rx="10" ry="12" fill="#15803d" opacity="0.8"/>
                <!-- Country Pin (India) -->
                <g id="sim2CountryPin" transform="translate(-18, -12)">
                    <circle cx="0" cy="0" r="4" fill="#f97316" stroke="#ffffff" stroke-width="1"/>
                    <text x="6" y="3" fill="#ffffff" font-size="7" font-weight="bold">Town A</text>
                </g>
                <!-- Central Terminator Line -->
                <line x1="0" y1="-50" x2="0" y2="50" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,3"/>
                <text x="-25" y="-55" fill="#38bdf8" font-size="9" font-weight="bold">DAY</text>
                <text x="25" y="-55" fill="#94a3b8" font-size="9" font-weight="bold">NIGHT</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="rotateGlobeSim2()" class="flex-1 p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white transition">
            Rotate Earth (Spin Halfway)
        </button>
        <button onclick="resetGlobeSim2()" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300">
            Reset Globe
        </button>
    </div>
    <div id="sim2Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        Town A is on the illuminated side facing the stationary torch, experiencing <strong>Daytime</strong>! Click 'Rotate Earth' to turn it into shadow.
    </div>
</div>
"""

# SIM 3: Earth's Spin (Axial Spin & Sun Tracker)
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Axial Spin & Solar Tracker</span>
        <p class="text-[11px] text-slate-400">Track how Earth's eastward spin creates sunrise in the East, solar noon overhead, and sunset in the West.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Sky Dome Arc -->
            <path d="M 60,190 A 140 140 0 0 1 340,190" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>

            <!-- Horizon Ground -->
            <rect x="30" y="190" width="340" height="25" rx="4" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
            <text x="65" y="206" fill="#38bdf8" font-size="9" font-weight="bold">EAST (Sunrise)</text>
            <text x="200" y="206" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">SOUTH</text>
            <text x="335" y="206" fill="#f97316" font-size="9" font-weight="bold" text-anchor="end">WEST (Sunset)</text>

            <!-- Flagpole in center -->
            <line x1="200" y1="190" x2="200" y2="135" stroke="#cbd5e1" stroke-width="3"/>
            <polygon points="200,135 220,145 200,155" fill="#f59e0b"/>

            <!-- Ground Shadow of Flagpole -->
            <line id="flagpoleShadow" x1="200" y1="190" x2="270" y2="190" stroke="#020617" stroke-width="5" stroke-linecap="round"/>

            <!-- Animated Sun Orb -->
            <g id="solarOrb" transform="translate(60, 190)">
                <circle cx="0" cy="0" r="14" fill="#facc15" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="0" cy="0" r="18" fill="none" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3,3">
                    <animate attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite"/>
                </circle>
            </g>

            <!-- Solar Time Card -->
            <rect x="25" y="20" width="130" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="34" fill="#94a3b8" font-size="8">SOLAR TIME</text>
            <text id="solarTimeText" x="35" y="50" fill="#facc15" font-size="12" font-weight="bold">06:00 AM (Sunrise)</text>
        </svg>
    </div>
    <div class="flex items-center gap-3">
        <label class="text-xs text-slate-300 font-semibold whitespace-nowrap">Time of Day:</label>
        <input type="range" id="solarTimeSlider" min="6" max="18" value="6" oninput="updateSolarHour(this.value)" class="w-full accent-amber-500">
        <span id="sliderHourDisplay" class="text-xs font-bold text-amber-400 w-16 text-right">06:00 AM</span>
    </div>
    <div id="sim3Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        At 6:00 AM, the Sun rises on the Eastern horizon. Because the Sun is low, light strikes at a shallow angle, casting a long shadow toward the West!
    </div>
</div>
"""

# SIM 4: Seasons' Journal (Interactive Wall Chart Explorer)
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Classroom Seasons' Journal Explorer</span>
        <p class="text-[11px] text-slate-400">Step through the 4 quarters of the year and observe shifts in trees, animals, and weather.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <g id="journalCanvas">
                <!-- Landscape Backdrop -->
                <rect x="50" y="25" width="300" height="190" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>

                <!-- Central Tree (Changes per quarter) -->
                <!-- Trunk -->
                <path d="M 185,185 L 195,120 L 205,120 L 215,185 Z" fill="#78350f"/>
                <!-- Foliage / Blossom (Q1 default: Summer Mangoes) -->
                <circle cx="200" cy="95" r="45" fill="#15803d" stroke="#16a34a" stroke-width="2"/>
                <!-- Golden ripe mangoes -->
                <ellipse cx="180" cy="90" rx="6" ry="9" fill="#facc15"/>
                <ellipse cx="215" cy="85" rx="6" ry="9" fill="#facc15"/>
                <ellipse cx="195" cy="115" rx="6" ry="9" fill="#facc15"/>

                <!-- Sun / Weather Icon -->
                <circle cx="100" cy="65" r="20" fill="#f59e0b"/>
                <line x1="100" y1="35" x2="100" y2="42" stroke="#facc15" stroke-width="2"/>
                <line x1="100" y1="88" x2="100" y2="95" stroke="#facc15" stroke-width="2"/>
                <line x1="70" y1="65" x2="77" y2="65" stroke="#facc15" stroke-width="2"/>
                <line x1="123" y1="65" x2="130" y2="65" stroke="#facc15" stroke-width="2"/>

                <!-- Readout label -->
                <text x="200" y="175" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Q1: April to June (Summer Heat & Mangoes)</text>
            </g>

            <!-- Quarter Tag -->
            <rect x="250" y="35" width="90" height="28" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="journalQuarterTag" x="295" y="53" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">QUARTER 1</text>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="setJournalQuarter(1)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-xs font-semibold text-amber-300">Q1: Apr-Jun</button>
        <button onclick="setJournalQuarter(2)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-cyan-500/50 text-xs font-semibold text-cyan-300">Q2: Jul-Sep</button>
        <button onclick="setJournalQuarter(3)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-pink-500/50 text-xs font-semibold text-pink-300">Q3: Oct-Dec</button>
        <button onclick="setJournalQuarter(4)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-xs font-semibold text-emerald-300">Q4: Jan-Mar</button>
    </div>
    <div id="sim4Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Quarter 1 (April to June):</strong> Blazing sunshine, long school summer vacations, hot dry winds, and the golden harvest of ripe mangoes.
    </div>
</div>
"""

# SIM 5: Yearly Rhythms (Five Ecological Themes Dashboard)
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Five Ecological Themes Dashboard</span>
        <p class="text-[11px] text-slate-400">Analyze annual patterns across Plant Life, Animals, Air, Heat & Light, and Water & Humans.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <g id="sim5Canvas">
                <!-- Theme Card 1 (Default: Plant Life) -->
                <rect x="50" y="25" width="300" height="190" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                <text x="200" y="55" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">THEME 1: PLANT LIFE CYCLES</text>

                <!-- Tree Seasonal States Progression -->
                <circle cx="100" cy="120" r="22" fill="#15803d"/>
                <text x="100" y="155" fill="#cbd5e1" font-size="8" text-anchor="middle">Spring Blooms</text>

                <circle cx="165" cy="120" r="22" fill="#ca8a04"/>
                <text x="165" y="155" fill="#cbd5e1" font-size="8" text-anchor="middle">Summer Fruits</text>

                <circle cx="235" cy="120" r="22" fill="#047857"/>
                <text x="235" y="155" fill="#cbd5e1" font-size="8" text-anchor="middle">Monsoon Growth</text>

                <!-- Deciduous bare tree in winter -->
                <circle cx="300" cy="120" r="22" fill="#334155"/>
                <path d="M 295,120 L 290,105 M 305,120 L 310,105" stroke="#cbd5e1" stroke-width="2"/>
                <text x="300" y="155" fill="#cbd5e1" font-size="8" text-anchor="middle">Winter Rest</text>

                <text x="200" y="195" fill="#a7f3d0" font-size="9" text-anchor="middle">Deciduous trees shed leaves to conserve moisture, then burst into new shoots!</text>
            </g>

            <rect x="25" y="20" width="90" height="28" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="sim5ThemeTag" x="70" y="38" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">PLANTS</text>
        </svg>
    </div>
    <div class="grid grid-cols-5 gap-1">
        <button onclick="setSim5Theme('plants')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-semibold text-emerald-300">1. Plants</button>
        <button onclick="setSim5Theme('animals')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-cyan-500/50 text-[10px] font-semibold text-cyan-300">2. Animals</button>
        <button onclick="setSim5Theme('air')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-semibold text-sky-300">3. Air</button>
        <button onclick="setSim5Theme('heat')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-semibold text-amber-300">4. Light</button>
        <button onclick="setSim5Theme('humans')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-pink-500/50 text-[10px] font-semibold text-pink-300">5. Humans</button>
    </div>
    <div id="sim5Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Plant Life Theme:</strong> Trees undergo rhythmic transformations: budding in spring, bearing fruit in summer, growing lush in monsoon, and shedding leaves in dry months.
    </div>
</div>
"""

# SIM 6: Vasanta Spring (Vasanta Blossom Garden & Koel Song)
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Vasanta Spring Garden & Koel Song</span>
        <p class="text-[11px] text-slate-400">Experience the King of Seasons (Rituraj) with flaming Palash blooms and sweet Koel calls.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Gentle Spring Sky -->
            <rect x="50" y="25" width="300" height="190" rx="8" fill="#064e3b" stroke="#059669" stroke-width="2"/>

            <!-- Flowering Palash / Gulmohar Tree -->
            <path d="M 190,195 L 196,120 L 204,120 L 210,195 Z" fill="#78350f"/>
            <!-- Fiery Orange Blooms (Flame of the Forest) -->
            <circle cx="200" cy="90" r="45" fill="#ea580c" opacity="0.85"/>
            <circle cx="175" cy="80" r="20" fill="#f97316"/>
            <circle cx="225" cy="80" r="20" fill="#f97316"/>
            <circle cx="200" cy="65" r="22" fill="#fb923c"/>
            <circle cx="190" cy="105" r="18" fill="#f97316"/>
            <circle cx="215" cy="105" r="18" fill="#f97316"/>

            <!-- Asian Koel Bird on branch -->
            <g id="koelBird" transform="translate(130, 95)">
                <ellipse cx="20" cy="15" rx="16" ry="10" fill="#0f172a" stroke="#334155"/>
                <circle cx="32" cy="10" r="6" fill="#020617"/>
                <circle cx="34" cy="9" r="1.5" fill="#ef4444"/>
                <polygon points="36,10 44,11 36,13" fill="#ca8a04"/>
                <!-- Sound waves radiating from beak -->
                <path d="M 45,6 Q 52,11 45,16 M 49,3 Q 58,11 49,19" fill="none" stroke="#fef08a" stroke-width="1.5">
                    <animate attributeName="opacity" values="0.2;1;0.2" dur="1.5s" repeatCount="indefinite"/>
                </path>
                <text x="60" y="14" fill="#fef08a" font-size="8" font-weight="bold">"Ku-oo!"</text>
            </g>

            <!-- Temperature Comfort Gauge (Center-Left) -->
            <rect x="65" y="35" width="95" height="42" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="75" y="48" fill="#94a3b8" font-size="7.5">SPRING CLIMATE</text>
            <text x="75" y="66" fill="#34d399" font-size="11" font-weight="bold">24°C • Pleasant</text>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="triggerKoelSong()" class="flex-1 p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Listen to Koel Bird Call
        </button>
        <button onclick="bloomPalash()" class="flex-1 p-2 bg-orange-600 hover:bg-orange-500 rounded-lg text-xs font-bold text-white">
            Burst Palash Flowers (Flame of Forest)
        </button>
    </div>
    <div id="sim6Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Vasanta (Spring):</strong> Moderate temperatures bring nature's rebirth. Fragrant mango blossoms (Manjari) and blazing Palash flowers fill the air with beauty.
    </div>
</div>
"""

# SIM 7: Grishma Summer (Summer Heatwave & Hydration Station)
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Grishma Heatwave & Hydration Station</span>
        <p class="text-[11px] text-slate-400">Discover the high-heat physics of summer and rehydrate with seasonal natural fruits!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Scorching Reddish-Yellow Sky Backdrop -->
            <rect x="50" y="25" width="300" height="190" rx="8" fill="#451a03" stroke="#b45309" stroke-width="2"/>

            <!-- High Overhead Blazing Sun -->
            <circle cx="200" cy="60" r="28" fill="#f59e0b">
                <animate attributeName="r" values="26;30;26" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="200" cy="60" r="35" fill="none" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="4,4"/>

            <!-- Cracked Earth Ground -->
            <rect x="50" y="160" width="300" height="55" fill="#78350f"/>
            <!-- Mud cracks lines -->
            <path d="M 80,180 L 110,195 L 140,185 M 170,175 L 200,195 L 230,175 M 260,185 L 290,195 L 320,180" stroke="#451a03" stroke-width="2.5" fill="none"/>

            <!-- Temperature & Loo Wind Alert -->
            <rect x="65" y="35" width="95" height="42" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="75" y="48" fill="#f87171" font-size="7.5">PEAK HEATWAVE</text>
            <text x="75" y="66" fill="#ef4444" font-size="12" font-weight="bold">44°C • Loo Wind</text>

            <!-- Hydration Station (Right) -->
            <g id="hydrationStation" transform="translate(260, 40)">
                <rect x="0" y="0" width="80" height="110" rx="6" fill="#020617" stroke="#ca8a04" stroke-width="1.5"/>
                <text x="40" y="16" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">SEASONAL FOOD</text>
                <!-- Watermelon wedge -->
                <path d="M 25,45 A 25 25 0 0 0 65,45 Z" fill="#dc2626" stroke="#15803d" stroke-width="2.5"/>
                <circle cx="35" cy="40" r="1.5" fill="#020617"/>
                <circle cx="45" cy="42" r="1.5" fill="#020617"/>
                <circle cx="55" cy="40" r="1.5" fill="#020617"/>
                <!-- Mango -->
                <ellipse cx="45" cy="72" rx="12" ry="16" fill="#facc15" stroke="#eab308"/>
                <text x="40" y="100" fill="#4ade80" font-size="7.5" font-weight="bold" text-anchor="middle">92% Hydration</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="sipAamPanna()" class="flex-1 p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Drink Aam Panna (Replenish Electrolytes)
        </button>
        <button onclick="eatWatermelon()" class="flex-1 p-2 bg-rose-600 hover:bg-rose-500 rounded-lg text-xs font-bold text-white">
            Eat Cold Watermelon (92% Water)
        </button>
    </div>
    <div id="sim7Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Grishma (Summer):</strong> Blazing solar rays cause ponds to dry and ground to crack. Nature provides water-rich melons and mangoes to sustain animal and human hydration.
    </div>
</div>
"""

# SIM 8: Varsha Monsoon (Monsoon Cloud & Rain Simulator)
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Varsha Monsoon Rain Simulator</span>
        <p class="text-[11px] text-slate-400">Trigger life-giving monsoon clouds, petrichor aroma, and celebrate with singing frogs!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Sky Background -->
            <rect x="50" y="25" width="300" height="190" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>

            <!-- Heavy Monsoon Clouds (Top) -->
            <g id="monsoonCloudGroup" transform="translate(100, 35)">
                <ellipse cx="60" cy="25" rx="35" ry="18" fill="#334155"/>
                <ellipse cx="95" cy="20" rx="30" ry="20" fill="#475569"/>
                <ellipse cx="130" cy="25" rx="35" ry="18" fill="#334155"/>
            </g>

            <!-- Falling Rain Streams -->
            <g id="rainStreamGroup" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="6,4">
                <line x1="130" y1="65" x2="120" y2="175"/>
                <line x1="160" y1="65" x2="150" y2="175"/>
                <line x1="190" y1="65" x2="180" y2="175"/>
                <line x1="220" y1="65" x2="210" y2="175"/>
                <line x1="250" y1="65" x2="240" y2="175"/>
            </g>

            <!-- Lush Emerald Ground & Pond -->
            <rect x="50" y="170" width="300" height="45" fill="#15803d"/>
            <ellipse cx="200" cy="195" rx="60" ry="15" fill="#0284c7"/>

            <!-- Croaking Bullfrog in pond -->
            <g id="monsoonFrog" transform="translate(180, 180)">
                <ellipse cx="20" cy="12" rx="14" ry="9" fill="#65a30d" stroke="#365314" stroke-width="1.5"/>
                <circle cx="14" cy="5" r="4" fill="#a3e635"/>
                <circle cx="26" cy="5" r="4" fill="#a3e635"/>
                <circle cx="14" cy="5" r="1.5" fill="#020617"/>
                <circle cx="26" cy="5" r="1.5" fill="#020617"/>
                <text x="40" y="10" fill="#fef08a" font-size="8" font-weight="bold">"Croak!"</text>
            </g>

            <!-- Petrichor Badge -->
            <rect x="65" y="35" width="95" height="32" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="75" y="47" fill="#94a3b8" font-size="7">RAIN AROMA</text>
            <text x="75" y="59" fill="#38bdf8" font-size="9" font-weight="bold">Sweet Petrichor</text>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="toggleMonsoonRain()" class="flex-1 p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Toggle Rain Downpour
        </button>
        <button onclick="triggerFrogCroak()" class="flex-1 p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Sing with Bullfrog
        </button>
    </div>
    <div id="sim8Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Varsha (Monsoon):</strong> Rains drench the soil, filling ponds and aquifers. Earthworms aerate the mud, bullfrogs sing in puddles, and farmers plant Kharif rice!
    </div>
</div>
"""

print("Simulators 1 to 8 defined.")


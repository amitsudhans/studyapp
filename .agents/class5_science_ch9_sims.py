"""
Simulators 1 to 16 for NCERT Class 5 Science Chapter 9: Rhythms of Nature
Zero raw LaTeX! Clean Unicode symbols.
"""
SIMS = {}
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

SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Sharad Autumn Riverbank & Fragrance Lab</span>
        <p class="text-[11px] text-slate-400">Experience crystal-clear sapphire skies, waving white Kaash reeds, and nocturnal Shiuli blooms!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-indigo-950 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Full Moon (Sharad Purnima) -->
            <circle id="sharadMoon" cx="330" cy="50" r="22" fill="#fef08a" opacity="0.9"/>
            <circle cx="330" cy="50" r="30" fill="none" stroke="#fef08a" stroke-width="1" opacity="0.4">
                <animate attributeName="r" values="26;34;26" dur="3s" repeatCount="indefinite"/>
            </circle>

            <!-- Calm Autumn River Surface -->
            <path d="M0,160 Q100,150 200,160 T400,160 L400,240 L0,240 Z" fill="#0369a1" opacity="0.4"/>
            <path d="M0,175 Q100,170 200,175 T400,175 L400,240 L0,240 Z" fill="#075985" opacity="0.6"/>

            <!-- Kaash Reed Cluster 1 (Left Riverbank) -->
            <g id="kaashReedsLeft">
                <!-- Stems -->
                <path d="M50,220 Q55,140 45,90" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <path d="M70,225 Q75,130 65,80" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <path d="M90,230 Q85,150 95,95" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <!-- White Fluffy Plumes -->
                <ellipse cx="45" cy="85" rx="8" ry="25" fill="#f8fafc" opacity="0.95" transform="rotate(-10 45 85)"/>
                <ellipse cx="65" cy="75" rx="9" ry="28" fill="#ffffff" opacity="0.95" transform="rotate(-5 65 75)"/>
                <ellipse cx="95" cy="90" rx="8" ry="24" fill="#f8fafc" opacity="0.95" transform="rotate(10 95 90)"/>
            </g>

            <!-- Fragrant Shiuli / Parijat Tree (Right Bank) -->
            <g id="shiuliTree">
                <!-- Trunk & Leaves -->
                <path d="M220,220 Q225,160 215,130 Q210,110 195,95" stroke="#78350f" stroke-width="7" fill="none"/>
                <path d="M215,130 Q240,115 250,90" stroke="#78350f" stroke-width="4.5" fill="none"/>
                <circle cx="190" cy="85" r="32" fill="#15803d" opacity="0.85"/>
                <circle cx="240" cy="80" r="26" fill="#16a34a" opacity="0.85"/>
                <!-- Shiuli Flowers (White petals with fiery orange stalks) -->
                <circle cx="180" cy="80" r="3" fill="#f97316"/>
                <circle cx="180" cy="80" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
                <circle cx="205" cy="90" r="3" fill="#f97316"/>
                <circle cx="205" cy="90" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
                <circle cx="235" cy="75" r="3" fill="#f97316"/>
                <circle cx="235" cy="75" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
            </g>

            <!-- Floating Fallen Flowers on Ground -->
            <g id="fallenFlowers">
                <circle cx="170" cy="215" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
                <circle cx="190" cy="222" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
                <circle cx="240" cy="218" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
            </g>

            <!-- Info Floating Pill -->
            <rect x="20" y="20" width="130" height="40" rx="6" fill="#020617" stroke="#334155" opacity="0.92"/>
            <text x="30" y="34" fill="#94a3b8" font-size="7">SHARAD ATMOSPHERE</text>
            <text id="sharadPillText" x="30" y="48" fill="#38bdf8" font-size="10" font-weight="bold">Sapphire Skies & Moon</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="swayKaashGrass()" class="p-2 bg-emerald-700 hover:bg-emerald-600 rounded-lg text-xs font-bold text-white">
            Wavering Kaash Plumes
        </button>
        <button onclick="bloomShiuliFlowers()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Release Shiuli Perfume
        </button>
    </div>
    <div id="sim9Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Sharad (Autumn):</strong> Ashvina–Kartika marks calm water, white Kaash grass swaying by riverbanks, nocturnal orange-stemmed Shiuli blossoms, and bright moonlight.
    </div>
</div>
"""

SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Hemant Pre-Winter Dew & Harvest Laboratory</span>
        <p class="text-[11px] text-slate-400">Witness morning mist, glittering dewdrops on blades of grass, and golden ripe paddy fields!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Gentle Morning Sun through Mist -->
            <circle cx="80" cy="60" r="30" fill="#fde047" opacity="0.4"/>
            <circle cx="80" cy="60" r="20" fill="#fef08a" opacity="0.8"/>
            <!-- Morning Mist Layers -->
            <ellipse id="mistLayer" cx="200" cy="90" rx="190" ry="25" fill="#f1f5f9" opacity="0.25"/>

            <!-- Golden Ripened Paddy Field -->
            <rect x="0" y="140" width="400" height="100" fill="#78350f" opacity="0.8"/>
            <g id="paddyStalks">
                <path d="M30,230 Q35,160 25,130" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M50,230 Q60,155 45,125" stroke="#eab308" stroke-width="3" fill="none"/>
                <path d="M70,230 Q75,150 65,120" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M90,230 Q105,155 90,125" stroke="#fbbf24" stroke-width="3" fill="none"/>
                <path d="M120,230 Q130,150 115,120" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M150,230 Q155,150 145,120" stroke="#eab308" stroke-width="3" fill="none"/>
                <path d="M180,230 Q190,155 175,125" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <!-- Heavy Golden Grain Heads Bending Down -->
                <ellipse cx="23" cy="130" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 23 130)"/>
                <ellipse cx="43" cy="125" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 43 125)"/>
                <ellipse cx="63" cy="120" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 63 120)"/>
                <ellipse cx="88" cy="125" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 88 125)"/>
                <ellipse cx="113" cy="120" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 113 120)"/>
                <ellipse cx="143" cy="120" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 143 120)"/>
            </g>

            <!-- Large Grass Blade with Condensing Dewdrop (Right Stage) -->
            <g id="dewDropFeature" transform="translate(250, 80)">
                <path d="M10,140 Q40,60 120,30 Q80,90 20,150 Z" fill="#22c55e" opacity="0.9"/>
                <!-- Sparkling Dewdrop on Grass Tip -->
                <ellipse id="condensingDew" cx="118" cy="32" rx="10" ry="12" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" opacity="0.95"/>
                <circle cx="115" cy="28" r="3" fill="#ffffff" opacity="0.9"/>
                <!-- Drip effect trail -->
                <line x1="118" y1="44" x2="118" y2="70" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>
            </g>

            <!-- Til-Gur Sweet Plate Icon -->
            <g transform="translate(300, 160)">
                <ellipse cx="40" cy="30" rx="36" ry="16" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Sesame Ladoos (Til-Gur) -->
                <circle cx="25" cy="25" r="9" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                <circle cx="42" cy="22" r="10" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                <circle cx="55" cy="26" r="8" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                <text x="40" y="42" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">Til-Gur Sweet</text>
            </g>

            <!-- Status Indicator Card -->
            <rect x="20" y="20" width="130" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="30" y="32" fill="#94a3b8" font-size="7">PRE-WINTER PHENOMENON</text>
            <text id="hemantCardText" x="30" y="46" fill="#fbbf24" font-size="10" font-weight="bold">Dew & Golden Fields</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="sparkleDewdrops()" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Condense Morning Dew
        </button>
        <button onclick="tasteTilGurSweet()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Sample Til-Gur Treat
        </button>
    </div>
    <div id="sim10Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Hemant (Pre-Winter):</strong> Margashirsha–Pausha brings pleasant morning chills, glistening dewdrops on grass tips, golden paddy harvesting, and warm nourishing sesame-jaggery sweets.
    </div>
</div>
"""

SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Shishir Winter Chill & Immunity Laboratory</span>
        <p class="text-[11px] text-slate-400">Explore crisp chilly winds, bare trees, warming evening bonfires, and immunity foods!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-cyan-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Cold Frosty Sky & Distant Snowy Peaks -->
            <polygon points="40,120 100,50 160,120" fill="#334155" opacity="0.5"/>
            <polygon points="75,70 100,50 125,70" fill="#f8fafc" opacity="0.9"/>
            <polygon points="120,130 190,40 260,130" fill="#1e293b" opacity="0.6"/>
            <polygon points="165,65 190,40 215,65" fill="#ffffff" opacity="0.95"/>

            <!-- Bare Deciduous Tree (Shedding leaves to conserve water) -->
            <g id="bareWinterTree" transform="translate(60, 90)">
                <path d="M40,110 Q42,60 38,30 Q35,15 20,0" stroke="#64748b" stroke-width="5" fill="none"/>
                <path d="M38,30 Q55,20 65,5" stroke="#64748b" stroke-width="3" fill="none"/>
                <path d="M40,55 Q20,40 10,25" stroke="#64748b" stroke-width="2.5" fill="none"/>
                <path d="M40,75 Q60,60 75,45" stroke="#64748b" stroke-width="2" fill="none"/>
                <text x="40" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">Bare Tree (Leaf Shedding)</text>
            </g>

            <!-- Bonfire with Flickering Flames -->
            <g id="bonfire" transform="translate(180, 150)">
                <!-- Cross Logs -->
                <line x1="5" y1="35" x2="45" y2="25" stroke="#78350f" stroke-width="6"/>
                <line x1="5" y1="25" x2="45" y2="35" stroke="#78350f" stroke-width="6"/>
                <!-- Flame Elements -->
                <path d="M25,30 Q15,10 25,-5 Q35,10 25,30 Z" fill="#f97316">
                    <animate attributeName="d" values="M25,30 Q15,10 25,-5 Q35,10 25,30 Z; M25,30 Q20,5 25,-12 Q30,5 25,30 Z; M25,30 Q15,10 25,-5 Q35,10 25,30 Z" dur="0.8s" repeatCount="indefinite"/>
                </path>
                <path d="M25,28 Q18,12 25,5 Q32,12 25,28 Z" fill="#fef08a"/>
                <text x="25" y="48" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Warm Bonfire</text>
            </g>

            <!-- Immunity Pantry Showcase (Right Stage) -->
            <g id="immunityPantry" transform="translate(270, 70)">
                <rect x="0" y="0" width="115" height="130" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="57" y="16" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">WINTER PANTRY</text>
                
                <!-- Sarson ka Saag Bowl -->
                <circle cx="30" cy="40" r="14" fill="#14532d" stroke="#16a34a" stroke-width="1.5"/>
                <circle cx="30" cy="40" r="4" fill="#fef08a"/>
                <text x="50" y="43" fill="#f8fafc" font-size="8">Sarson Saag</text>

                <!-- Vitamin-C Oranges -->
                <circle cx="30" cy="70" r="12" fill="#ea580c"/>
                <circle cx="30" cy="70" r="4" fill="#fb923c"/>
                <text x="50" y="73" fill="#f8fafc" font-size="8">Citrus Orange</text>

                <!-- Nutrient-Dense Amla -->
                <circle cx="30" cy="98" r="10" fill="#65a30d"/>
                <path d="M26,90 Q30,98 34,90" stroke="#365314" stroke-width="1" fill="none"/>
                <text x="50" y="101" fill="#f8fafc" font-size="8">Amla (Gooseberry)</text>
            </g>

            <!-- Thermometer Display -->
            <rect x="15" y="15" width="85" height="35" rx="5" fill="#020617" stroke="#334155" opacity="0.92"/>
            <text x="22" y="27" fill="#94a3b8" font-size="7">TEMPERATURE</text>
            <text id="shishirTemp" x="22" y="41" fill="#38bdf8" font-size="11" font-weight="bold">8°C (Chilly)</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="stokeWinterBonfire()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Stoke Fire & Warm Up
        </button>
        <button onclick="inspectImmunityFoods()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Inspect Immunity Foods
        </button>
    </div>
    <div id="sim11Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Shishir (Winter):</strong> Magha–Phalguna brings freezing winds from the Himalayas. Trees drop leaves to preserve moisture, while citrus fruits, amla, and leafy greens boost human immunity.
    </div>
</div>
"""

SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider block mb-1">Pan-India Regional Climatic Contrasts</span>
        <p class="text-[11px] text-slate-400">Click regions to explore diverse climates: Himalayan snow, Thar desert, tropical coast, & monsoon rain!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Interactive Map Graphic with Highlight Pins -->
            <!-- Simplified India Map Silhouette Outline -->
            <path d="M160,20 L180,45 L200,30 L220,50 L205,75 L230,105 L260,105 L280,120 L270,140 L240,135 L220,160 L185,225 L160,180 L140,165 L130,120 L145,95 L150,55 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5" opacity="0.6"/>

            <!-- Region Hotspots (Clickable Pins) -->
            <!-- 1. Kashmir / Ladakh (North) -->
            <g onclick="selectRegion('kashmir')" class="cursor-pointer" id="pinKashmir">
                <circle cx="180" cy="38" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                <text x="180" y="41" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">1</text>
                <text x="195" y="38" fill="#bae6fd" font-size="8" font-weight="bold">Kashmir</text>
            </g>

            <!-- 2. Rajasthan Thar Desert (West) -->
            <g onclick="selectRegion('rajasthan')" class="cursor-pointer" id="pinRajasthan">
                <circle cx="140" cy="100" r="10" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
                <text x="140" y="103" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">2</text>
                <text x="95" y="103" fill="#fde68a" font-size="8" font-weight="bold">Rajasthan</text>
            </g>

            <!-- 3. Meghalaya Mawsynram (East) -->
            <g onclick="selectRegion('meghalaya')" class="cursor-pointer" id="pinMeghalaya">
                <circle cx="270" cy="115" r="10" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
                <text x="270" y="118" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">3</text>
                <text x="285" y="118" fill="#93c5fd" font-size="8" font-weight="bold">Meghalaya</text>
            </g>

            <!-- 4. Kerala Coastal Tropics (South) -->
            <g onclick="selectRegion('kerala')" class="cursor-pointer" id="pinKerala">
                <circle cx="170" cy="195" r="10" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
                <text x="170" y="198" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">4</text>
                <text x="185" y="198" fill="#a7f3d0" font-size="8" font-weight="bold">Kerala</text>
            </g>

            <!-- Dynamic Regional Feature Preview Card (Right Box) -->
            <g id="regionFeatureCard" transform="translate(25, 140)">
                <rect x="0" y="0" width="120" height="75" rx="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text id="regCardTitle" x="10" y="18" fill="#38bdf8" font-size="9" font-weight="bold">Kashmir Himalayas</text>
                <text id="regCardDesc1" x="10" y="32" fill="#e2e8f0" font-size="7.5">• Sub-zero snow & ice</text>
                <text id="regCardDesc2" x="10" y="46" fill="#e2e8f0" font-size="7.5">• Pheran & Kangri pot</text>
                <text id="regCardDesc3" x="10" y="60" fill="#e2e8f0" font-size="7.5">• Wooden insulated roofs</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="selectRegion('kashmir')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            1. Kashmir (Snow)
        </button>
        <button onclick="selectRegion('rajasthan')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            2. Desert (Heat)
        </button>
        <button onclick="selectRegion('meghalaya')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            3. Rain (Mawsynram)
        </button>
        <button onclick="selectRegion('kerala')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            4. Kerala (Coast)
        </button>
    </div>
    <div id="sim12Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Regional Contrasts:</strong> While Kashmir shivers at −5°C requiring Kangri fire pots under pherans, Kerala stays warm and humid at 28°C with coconut breezes!
    </div>
</div>
"""

SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-lime-400 uppercase tracking-wider block mb-1">Agricultural Cropping Triad (Kharif, Rabi, Zaid)</span>
        <p class="text-[11px] text-slate-400">Discover which crops grow in which season: monsoon rice, winter wheat, and summer melons!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Soil and Weather Backdrops -->
            <rect x="0" y="150" width="400" height="90" fill="#3f2e1a" opacity="0.8"/>
            <line x1="0" y1="150" x2="400" y2="150" stroke="#78350f" stroke-width="2"/>

            <!-- Dynamic Crop Visual Stage -->
            <g id="cropStageGraphic">
                <!-- Default: Kharif Paddy Field -->
                <!-- Rain Clouds above -->
                <circle cx="200" cy="40" r="22" fill="#475569"/>
                <circle cx="225" cy="35" r="26" fill="#64748b"/>
                <circle cx="175" cy="40" r="20" fill="#475569"/>
                <!-- Rain streaks -->
                <line x1="180" y1="65" x2="175" y2="85" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="205" y1="68" x2="200" y2="88" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="225" y1="65" x2="220" y2="85" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>

                <!-- Rice Paddy Shoots in Watery Soil -->
                <rect x="50" y="150" width="300" height="20" fill="#0284c7" opacity="0.4"/>
                <path d="M120,165 Q110,120 95,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M120,165 Q130,115 145,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M200,165 Q190,115 175,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M200,165 Q210,110 225,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M280,165 Q270,120 255,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M280,165 Q290,115 305,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <text x="200" y="195" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Kharif: Water-Hungry Paddy & Cotton</text>
            </g>

            <!-- Sowing & Harvesting Metadata Card -->
            <rect x="20" y="15" width="135" height="46" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="28" y="28" fill="#94a3b8" font-size="7">SEASON & CROPPING CYCLE</text>
            <text id="cropTitle" x="28" y="42" fill="#4ade80" font-size="11" font-weight="bold">Kharif Season</text>
            <text id="cropTiming" x="28" y="54" fill="#cbd5e1" font-size="7.5">Sown: June | Harvest: Oct</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="selectCropPattern('kharif')" class="p-2 bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            1. Kharif (Monsoon)
        </button>
        <button onclick="selectCropPattern('rabi')" class="p-2 bg-amber-950/80 hover:bg-amber-900 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            2. Rabi (Winter)
        </button>
        <button onclick="selectCropPattern('zaid')" class="p-2 bg-red-950/80 hover:bg-red-900 border border-red-500 rounded-lg text-xs font-bold text-red-300">
            3. Zaid (Summer)
        </button>
    </div>
    <div id="sim13Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Kharif Crops:</strong> Planted at the onset of monsoon rains (June–July) and harvested in autumn (September–October). Examples: Rice (paddy), maize, cotton, and groundnut.
    </div>
</div>
"""

SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider block mb-1">Pan-Indian Harvest Festival Wheel</span>
        <p class="text-[11px] text-slate-400">Spin the wheel to explore how farmers across India thank nature for bountiful crops!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Rotary Festival Hub -->
            <g id="festivalWheelGroup" transform="translate(140, 120)">
                <circle cx="0" cy="0" r="80" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                <!-- Segments -->
                <path d="M0,0 L0,-80 A80,80 0 0,1 76,-25 Z" fill="#b45309" opacity="0.7"/>
                <path d="M0,0 L76,-25 A80,80 0 0,1 47,65 Z" fill="#065f46" opacity="0.7"/>
                <path d="M0,0 L47,65 A80,80 0 0,1 -47,65 Z" fill="#1e40af" opacity="0.7"/>
                <path d="M0,0 L-47,65 A80,80 0 0,1 -76,-25 Z" fill="#86198f" opacity="0.7"/>
                <path d="M0,0 L-76,-25 A80,80 0 0,1 0,-80 Z" fill="#991b1b" opacity="0.7"/>
                <!-- Hub -->
                <circle cx="0" cy="0" r="28" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
                <text x="0" y="4" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">HARVEST</text>
            </g>

            <!-- Dynamic Selected Festival Visual (Right Side Stage) -->
            <g id="festivalDisplayStage" transform="translate(250, 40)">
                <rect x="0" y="0" width="135" height="160" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5" opacity="0.95"/>
                <!-- Festival Icon Graphic (Default: Makar Sankranti Kites) -->
                <g id="festGraphic">
                    <polygon points="67,25 90,50 67,75 44,50" fill="#ef4444" stroke="#fbbf24" stroke-width="1.5"/>
                    <line x1="67" y1="25" x2="67" y2="75" stroke="#ffffff" stroke-width="1"/>
                    <line x1="44" y1="50" x2="90" y2="50" stroke="#ffffff" stroke-width="1"/>
                    <path d="M67,75 Q75,90 67,100" stroke="#fbbf24" stroke-width="1" fill="none"/>
                </g>
                <text id="festName" x="67" y="115" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Makar Sankranti</text>
                <text id="festRegion" x="67" y="130" fill="#38bdf8" font-size="8" text-anchor="middle">Across India (January)</text>
                <text id="festCustom" x="67" y="145" fill="#cbd5e1" font-size="7" text-anchor="middle">Flying Kites & Til-Gur</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="displayFestival('sankranti')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Makar Sankranti
        </button>
        <button onclick="displayFestival('pongal')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Pongal (Tamil Nadu)
        </button>
        <button onclick="displayFestival('lohri')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-orange-500/50 text-[10px] font-bold text-orange-300">
            Lohri (Punjab)
        </button>
        <button onclick="displayFestival('bihu')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-indigo-500/50 text-[10px] font-bold text-indigo-300">
            Magh Bihu (Assam)
        </button>
    </div>
    <div id="sim14Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Makar Sankranti:</strong> Marks the Sun's northward journey (*Uttarayana*) and the winter harvest. Families celebrate with soaring colorful kites, sesame *chikki*, and festive prayers!
    </div>
</div>
"""

SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Ritucharya Seasonal Lifestyle Simulator</span>
        <p class="text-[11px] text-slate-400">Toggle between Summer and Winter to adapt clothing, hydration, and nutritional diet!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Split Environment Backdrop -->
            <g id="lifestyleBackdrop">
                <rect x="0" y="0" width="200" height="240" fill="#451a03" opacity="0.3"/>
                <rect x="200" y="0" width="200" height="240" fill="#082f49" opacity="0.3"/>
                <line x1="200" y1="0" x2="200" y2="240" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
            </g>

            <!-- Character Model (Center) -->
            <g id="characterModel" transform="translate(170, 70)">
                <!-- Head -->
                <circle cx="30" cy="20" r="14" fill="#fed7aa"/>
                <path d="M16,16 Q30,6 44,16 Z" fill="#1e293b"/>
                <!-- Torso Clothing (Dynamic) -->
                <rect id="charTorso" x="16" y="34" width="28" height="45" rx="4" fill="#ffffff" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Legs -->
                <line x1="23" y1="79" x2="23" y2="120" stroke="#1e293b" stroke-width="4"/>
                <line x1="37" y1="79" x2="37" y2="120" stroke="#1e293b" stroke-width="4"/>
            </g>

            <!-- Summer Adaptation Gear (Left) -->
            <g id="summerGear" transform="translate(25, 40)">
                <rect x="0" y="0" width="125" height="160" rx="8" fill="#020617" stroke="#f59e0b" stroke-width="1.5" opacity="0.95"/>
                <text x="62" y="20" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">SUMMER (Grishma)</text>
                <!-- Light Cotton Shirt Icon -->
                <rect x="42" y="32" width="40" height="30" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
                <text x="62" y="52" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">Airy Cotton</text>
                <!-- Hydrating Buttermilk / Aam Panna -->
                <rect x="48" y="72" width="28" height="35" rx="3" fill="#bae6fd" stroke="#0284c7" stroke-width="1"/>
                <text x="62" y="93" fill="#0369a1" font-size="7" font-weight="bold" text-anchor="middle">Chhaachh</text>
                <text x="62" y="125" fill="#fde68a" font-size="7.5" text-anchor="middle">Cooling hydration</text>
                <text x="62" y="140" fill="#cbd5e1" font-size="7" text-anchor="middle">Rest during noon peak</text>
            </g>

            <!-- Winter Adaptation Gear (Right) -->
            <g id="winterGear" transform="translate(250, 40)">
                <rect x="0" y="0" width="125" height="160" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="62" y="20" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">WINTER (Shishir)</text>
                <!-- Heavy Woollen Sweater Icon -->
                <rect x="42" y="32" width="40" height="30" rx="3" fill="#dc2626" stroke="#991b1b" stroke-width="1"/>
                <text x="62" y="52" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Woollen Layers</text>
                <!-- Warming Bajra Roti & Ghee -->
                <circle cx="62" cy="90" r="16" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                <circle cx="62" cy="90" r="5" fill="#fef08a"/>
                <text x="62" y="125" fill="#bae6fd" font-size="7.5" text-anchor="middle">Warming bajra & ghee</text>
                <text x="62" y="140" fill="#cbd5e1" font-size="7" text-anchor="middle">Warm sunshine in day</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="setLifestyleMode('summer')" class="flex-1 p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Switch to Summer Mode (Grishma)
        </button>
        <button onclick="setLifestyleMode('winter')" class="flex-1 p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Switch to Winter Mode (Shishir)
        </button>
    </div>
    <div id="sim15Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Ritucharya Concept:</strong> Living in rhythm with nature means wearing breathable cottons and drinking buttermilk in summer, while dressing in layered woollens and eating warm bajra roti in winter.
    </div>
</div>
"""

SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">The Eternal Six-Season Cosmic Wheel</span>
        <p class="text-[11px] text-slate-400">Step through the endless cyclic loop of nature's Shad Ritu and witness the harmony of change!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Rotating Mandala Wheel -->
            <g id="cosmicMandala" transform="translate(200, 120)">
                <!-- Outer Wheel Ring -->
                <circle cx="0" cy="0" r="95" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
                
                <!-- 6 Season Nodes around the circle (Radius = 75) -->
                <!-- 1. Vasanta (0 deg: 75, 0) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(1)">
                    <circle cx="75" cy="0" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                    <text x="75" y="4" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Vasanta</text>
                </g>
                <!-- 2. Grishma (60 deg: 37.5, 65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(2)">
                    <circle cx="37.5" cy="65" r="16" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
                    <text x="37.5" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Grishma</text>
                </g>
                <!-- 3. Varsha (120 deg: -37.5, 65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(3)">
                    <circle cx="-37.5" cy="65" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                    <text x="-37.5" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Varsha</text>
                </g>
                <!-- 4. Sharad (180 deg: -75, 0) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(4)">
                    <circle cx="-75" cy="0" r="16" fill="#4338ca" stroke="#818cf8" stroke-width="2"/>
                    <text x="-75" y="4" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Sharad</text>
                </g>
                <!-- 5. Hemant (240 deg: -37.5, -65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(5)">
                    <circle cx="-37.5" cy="-65" r="16" fill="#d97706" stroke="#fcd34d" stroke-width="2"/>
                    <text x="-37.5" y="-61" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Hemant</text>
                </g>
                <!-- 6. Shishir (300 deg: 37.5, -65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(6)">
                    <circle cx="37.5" cy="-65" r="16" fill="#0e7490" stroke="#67e8f9" stroke-width="2"/>
                    <text x="37.5" y="-61" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Shishir</text>
                </g>

                <!-- Center Golden Sun Core -->
                <circle cx="0" cy="0" r="28" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
                <text x="0" y="3" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">HARMONY</text>
            </g>

            <!-- Flow Indicator Tag -->
            <rect x="25" y="20" width="135" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="32" fill="#94a3b8" font-size="7">THE CYCLIC HARMONY</text>
            <text id="seasonCycleName" x="35" y="46" fill="#c084fc" font-size="10" font-weight="bold">Continuous 6-Season Loop</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="stepNextSeasonCycle()" class="p-2 bg-purple-600 hover:bg-purple-500 rounded-lg text-xs font-bold text-white">
            Step to Next Season
        </button>
        <button onclick="toggleSeasonalAutoSpin()" class="p-2 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-xs font-bold text-white">
            Auto-Spin Cosmic Wheel
        </button>
    </div>
    <div id="sim16Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Eternal Rhythm:</strong> Change is not a one-way path, but an eternal revolving cycle. Winter cold prepares seeds, Spring wakes flowers, Summer builds heat, Monsoon brings rain, and Autumn brings clarity.
    </div>
</div>
"""


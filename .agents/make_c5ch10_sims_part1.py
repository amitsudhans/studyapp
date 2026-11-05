"""
Simulators 1 to 8 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Zero raw LaTeX! Clean Unicode symbols.
"""

SIMS = {}

# SIM 1: One Shared Home (ISS Orbit Simulator)
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">ISS Orbit & Borderless Earth Laboratory</span>
        <p class="text-[11px] text-slate-400">Glide 400 km above Earth aboard the space station. Notice how all artificial borders disappear!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Deep Space Stars -->
            <circle cx="30" cy="25" r="1" fill="#ffffff" opacity="0.8"/>
            <circle cx="85" cy="40" r="1.5" fill="#ffffff" opacity="0.9"/>
            <circle cx="370" cy="30" r="1" fill="#ffffff" opacity="0.7"/>
            <circle cx="320" cy="70" r="1.5" fill="#ffffff" opacity="0.9"/>
            <circle cx="45" cy="190" r="1" fill="#ffffff" opacity="0.6"/>

            <!-- Curved Horizon of Earth Below -->
            <path id="sim1EarthCurve" d="M-50,260 Q200,80 450,260 Z" fill="#0284c7" opacity="0.9"/>
            <!-- Landmass Outline on Earth (No Borders) -->
            <path id="sim1Landmass" d="M80,180 Q130,120 180,150 Q210,130 250,160 Q280,130 320,180 Q250,220 150,210 Z" fill="#15803d" opacity="0.85"/>
            <!-- Swirling White Atmosphere & Clouds -->
            <path d="M50,160 Q120,130 200,140 Q280,150 350,170" stroke="#ffffff" stroke-width="6" fill="none" opacity="0.45" stroke-linecap="round"/>
            <path d="M100,180 Q170,160 260,175" stroke="#ffffff" stroke-width="4" fill="none" opacity="0.35" stroke-linecap="round"/>

            <!-- Atmospheric Glowing Limb (Thin Blue Line) -->
            <path d="M-50,260 Q200,80 450,260" stroke="#38bdf8" stroke-width="3" fill="none" opacity="0.8"/>

            <!-- International Space Station (ISS) in Orbit -->
            <g id="issStationGraphic" transform="translate(160, 45)">
                <!-- Main Truss -->
                <line x1="0" y1="20" x2="80" y2="20" stroke="#94a3b8" stroke-width="3"/>
                <!-- Central Modules -->
                <rect x="32" y="14" width="16" height="12" rx="2" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
                <circle cx="40" cy="20" r="3" fill="#38bdf8"/>
                <!-- Solar Array Wings Left -->
                <rect x="4" y="2" width="12" height="36" rx="1" fill="#0284c7" stroke="#38bdf8" stroke-width="1" opacity="0.9"/>
                <rect x="18" y="2" width="12" height="36" rx="1" fill="#0284c7" stroke="#38bdf8" stroke-width="1" opacity="0.9"/>
                <!-- Solar Array Wings Right -->
                <rect x="50" y="2" width="12" height="36" rx="1" fill="#0284c7" stroke="#38bdf8" stroke-width="1" opacity="0.9"/>
                <rect x="64" y="2" width="12" height="36" rx="1" fill="#0284c7" stroke="#38bdf8" stroke-width="1" opacity="0.9"/>
            </g>

            <!-- Altitude & Velocity Badge -->
            <rect x="20" y="15" width="125" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="28" y="28" fill="#94a3b8" font-size="7">ORBITAL OBSERVATION</text>
            <text id="orbitModeText" x="28" y="42" fill="#38bdf8" font-size="10" font-weight="bold">Altitude: 400 km | ISS</text>
            <text x="28" y="52" fill="#cbd5e1" font-size="7">Speed: 28,000 km/h (No Borders)</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleDayNightOrbit()" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Switch Day / Night Orbit
        </button>
        <button onclick="zoomISSView()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Inspect 'Overview Effect'
        </button>
    </div>
    <div id="sim1Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Cosmic View:</strong> From the International Space Station, countries, walls, and boundary lines are completely absent. All you see is one radiant blue oasis wrapped in a thin atmospheric veil.
    </div>
</div>
"""

# SIM 2: The Blue Planet (Planetary Surface Analyzer)
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-blue-400 uppercase tracking-wider block mb-1">The Blue Planet Surface Analyzer</span>
        <p class="text-[11px] text-slate-400">Discover why Earth shines like a blue marble in the solar system: 71% oceans & 29% landmasses!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Rotating Earth Globe -->
            <g id="bluePlanetGlobe" transform="translate(150, 120)">
                <!-- Ocean Base Sphere -->
                <circle cx="0" cy="0" r="75" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Atmospheric Glow Ring -->
                <circle cx="0" cy="0" r="79" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.4"/>
                
                <!-- Continents on Globe -->
                <path id="globeContinents" d="M-25,-55 Q0,-35 25,-40 Q40,-15 20,15 Q5,45 -20,35 Q-45,15 -35,-25 Z" fill="#15803d" opacity="0.9"/>
                <path d="M-55,5 Q-35,-15 -20,-5 Q-15,30 -40,40 Z" fill="#16a34a" opacity="0.8"/>
                
                <!-- Swirling Cloud Layers -->
                <path d="M-60,-20 Q0,-45 50,-15" stroke="#ffffff" stroke-width="4" fill="none" opacity="0.5" stroke-linecap="round"/>
                <path d="M-40,25 Q15,40 60,10" stroke="#ffffff" stroke-width="3" fill="none" opacity="0.4" stroke-linecap="round"/>
            </g>

            <!-- Surface Ratio Infographic Card (Right Side) -->
            <g transform="translate(260, 45)">
                <rect x="0" y="0" width="125" height="150" rx="8" fill="#020617" stroke="#334155" opacity="0.95"/>
                <text x="62" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">SURFACE PROPORTION</text>
                
                <!-- Water Gauge -->
                <rect x="12" y="32" width="100" height="24" rx="4" fill="#0284c7"/>
                <text x="62" y="47" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">71% Liquid Oceans</text>

                <!-- Land Gauge -->
                <rect x="12" y="64" width="41" height="24" rx="4" fill="#16a34a"/>
                <text x="62" y="79" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">29% Continents</text>

                <text id="featureAnalyzed" x="62" y="112" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Oceans Absorb Red</text>
                <text x="62" y="126" fill="#cbd5e1" font-size="7" text-anchor="middle">Scatters Blue Light</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="analyzeEarthSurface('oceans')" class="p-2 bg-sky-950 hover:bg-sky-900 border border-sky-500 rounded-lg text-xs font-bold text-sky-300">
            1. Oceans (71%)
        </button>
        <button onclick="analyzeEarthSurface('continents')" class="p-2 bg-emerald-950 hover:bg-emerald-900 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            2. Continents (29%)
        </button>
        <button onclick="analyzeEarthSurface('atmosphere')" class="p-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 rounded-lg text-xs font-bold text-slate-200">
            3. Atmosphere
        </button>
    </div>
    <div id="sim2Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Blue Marble:</strong> Earth's vast liquid oceans absorb the longer red wavelengths of sunlight, reflecting shorter blue light into space and making our home shine like a jewel.
    </div>
</div>
"""

# SIM 3: Boundless Nature (Atmospheric Circulation & Seed Dispersion)
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Boundless Nature Circulation Simulator</span>
        <p class="text-[11px] text-slate-400">Watch air streams, rainclouds, floating dandelion seeds, and ocean currents cross the globe freely!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Continuous Wind Jet Streams -->
            <g id="windStreamGroup">
                <path d="M0,60 Q100,30 200,60 T400,60" stroke="#38bdf8" stroke-width="2" fill="none" stroke-dasharray="6,6" opacity="0.7">
                    <animate attributeName="stroke-dashoffset" values="0;-100" dur="4s" repeatCount="indefinite"/>
                </path>
                <path d="M0,120 Q100,150 200,120 T400,120" stroke="#2dd4bf" stroke-width="2.5" fill="none" stroke-dasharray="8,8" opacity="0.7">
                    <animate attributeName="stroke-dashoffset" values="0;-100" dur="3s" repeatCount="indefinite"/>
                </path>
                <path d="M0,180 Q100,160 200,180 T400,180" stroke="#38bdf8" stroke-width="2" fill="none" stroke-dasharray="6,6" opacity="0.7">
                    <animate attributeName="stroke-dashoffset" values="0;-100" dur="5s" repeatCount="indefinite"/>
                </path>
            </g>

            <!-- Drifting Raincloud with Showers -->
            <g id="driftingRaincloud" transform="translate(140, 70)">
                <ellipse cx="25" cy="15" rx="20" ry="12" fill="#64748b" opacity="0.9"/>
                <ellipse cx="45" cy="10" rx="25" ry="16" fill="#94a3b8" opacity="0.95"/>
                <ellipse cx="65" cy="15" rx="18" ry="12" fill="#64748b" opacity="0.9"/>
                <!-- Rain Streaks -->
                <line x1="25" y1="32" x2="20" y2="48" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="45" y1="35" x2="40" y2="52" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="65" y1="32" x2="60" y2="48" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
            </g>

            <!-- Floating Seeds on Breeze (Dandelion & Coconut) -->
            <g id="floatingSeed" transform="translate(60, 130)">
                <!-- Dandelion Parachute -->
                <circle cx="15" cy="15" r="2.5" fill="#fef08a"/>
                <line x1="15" y1="15" x2="15" y2="28" stroke="#cbd5e1" stroke-width="1"/>
                <circle cx="15" cy="28" r="1.5" fill="#78350f"/>
                <!-- Fluff filaments -->
                <line x1="15" y1="15" x2="8" y2="6" stroke="#f1f5f9" stroke-width="0.8"/>
                <line x1="15" y1="15" x2="22" y2="6" stroke="#f1f5f9" stroke-width="0.8"/>
                <line x1="15" y1="15" x2="15" y2="4" stroke="#f1f5f9" stroke-width="0.8"/>
                <text x="15" y="42" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Airborne Seed</text>
            </g>

            <!-- Status Indicator Card -->
            <rect x="25" y="15" width="135" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="28" fill="#94a3b8" font-size="7">PLANETARY TRANSIT</text>
            <text id="natureTransitText" x="35" y="42" fill="#2dd4bf" font-size="10" font-weight="bold">Boundless Air & Water</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="accelerateWinds()" class="p-2 bg-teal-600 hover:bg-teal-500 rounded-lg text-xs font-bold text-white">
            Accelerate Trade Winds
        </button>
        <button onclick="disperseSeeds()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Disperse Global Seeds
        </button>
    </div>
    <div id="sim3Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Free Transits:</strong> Rainclouds form over the Indian Ocean, blow across the subcontinent, and drop moisture that nourishes crops. No passport or visa is required!
    </div>
</div>
"""

# SIM 4: Travelling Birds (Rosy Starling Migration Corridor)
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-pink-400 uppercase tracking-wider block mb-1">Rosy Starling 5,000 km Migration Flight</span>
        <p class="text-[11px] text-slate-400">Track the pink-and-black rosy starlings flying from freezing Russia and Mongolia to sunny India!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Simplified Migration Corridor Map -->
            <!-- Northern Breeding Grounds (Russia/Mongolia) -->
            <rect x="50" y="25" width="140" height="40" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
            <text x="120" y="42" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">Russia & Mongolia</text>
            <text x="120" y="55" fill="#f472b6" font-size="7" text-anchor="middle">Summer Breeding Grounds</text>

            <!-- Southern Winter Haven (India) -->
            <rect x="210" y="165" width="140" height="40" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1"/>
            <text x="280" y="182" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">India (Gujarat & Peninsular)</text>
            <text x="280" y="195" fill="#86efac" font-size="7" text-anchor="middle">Winter Haven & Pest Control</text>

            <!-- Curved Transcontinental Migration Flight Path -->
            <path id="migrationFlightPath" d="M120,65 Q180,100 280,165" stroke="#ec4899" stroke-width="2.5" fill="none" stroke-dasharray="6,4">
                <animate attributeName="stroke-dashoffset" values="0;-50" dur="2s" repeatCount="indefinite"/>
            </path>

            <!-- Rosy Starling Bird Model -->
            <g id="starlingBird" transform="translate(180, 105)">
                <!-- Pink Body -->
                <ellipse cx="20" cy="15" rx="14" ry="9" fill="#f472b6" stroke="#db2777" stroke-width="1"/>
                <!-- Glossy Black Head & Crest -->
                <circle cx="10" cy="11" r="6" fill="#0f172a"/>
                <polygon points="5,11 0,13 5,14" fill="#f59e0b"/>
                <!-- Black Wings & Tail -->
                <polygon points="26,10 38,18 25,18" fill="#1e293b"/>
                <polygon points="28,15 36,15 28,19" fill="#0f172a"/>
            </g>

            <!-- Locust Swarm / Pest Target -->
            <g id="locustPestGroup" transform="translate(290, 130)">
                <ellipse cx="10" cy="10" rx="6" ry="3" fill="#854d0e"/>
                <line x1="8" y1="7" x2="4" y2="4" stroke="#a16207" stroke-width="1"/>
                <ellipse cx="25" cy="15" rx="6" ry="3" fill="#854d0e"/>
                <text x="20" y="28" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">Locust Swarm</text>
            </g>

            <!-- Flight Distance Pill -->
            <rect x="25" y="175" width="115" height="34" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="32" y="188" fill="#94a3b8" font-size="7">MIGRATION ROUTE</text>
            <text x="32" y="200" fill="#ec4899" font-size="9" font-weight="bold">5,000 km Non-Stop</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="flyStarlingFlock()" class="p-2 bg-pink-600 hover:bg-pink-500 rounded-lg text-xs font-bold text-white">
            Trigger Starling Murmuration
        </button>
        <button onclick="feedOnLocusts()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Devour Crop Locusts
        </button>
    </div>
    <div id="sim4Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Travelling Ally:</strong> Rosy starlings fly 5,000 km across mountains and deserts to escape freezing winters, consuming millions of destructive grasshoppers and locusts for Indian farmers!
    </div>
</div>
"""

# SIM 5: Yoga's Gift (Global Harmony & Asana Explorer)
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Yoga: India's Gift to the World</span>
        <p class="text-[11px] text-slate-400">Explore ancient Surya Namaskar, mindful pranayama breathing, and the June 21 UN International Day of Yoga!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Radiant Golden Sun (Solstice Symbol) -->
            <circle cx="200" cy="70" r="32" fill="#f59e0b" opacity="0.3"/>
            <circle cx="200" cy="70" r="22" fill="#fde047" opacity="0.8"/>

            <!-- Yoga Asana Silhouette (Centered) -->
            <g id="yogaAsanaGraphic" transform="translate(185, 110)">
                <!-- Head -->
                <circle cx="15" cy="10" r="8" fill="#fed7aa"/>
                <!-- Torso in Prayer / Lotus Pose -->
                <path d="M7,22 Q15,18 23,22 L27,45 Q15,48 3,45 Z" fill="#f97316"/>
                <!-- Crossed Legs -->
                <ellipse cx="15" cy="52" rx="20" ry="6" fill="#ea580c"/>
                <!-- Hands in Namaste -->
                <path d="M12,24 L18,24 L15,32 Z" fill="#fed7aa"/>
            </g>

            <!-- Breathing Expansion Aura -->
            <circle id="breathAura" cx="200" cy="135" r="35" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.6">
                <animate attributeName="r" values="30;50;30" dur="4s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="0.7;0.2;0.7" dur="4s" repeatCount="indefinite"/>
            </circle>

            <!-- World Clock Cities Celebrating June 21 -->
            <g transform="translate(25, 40)">
                <rect x="0" y="0" width="105" height="130" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
                <text x="52" y="16" fill="#f59e0b" font-size="7.5" font-weight="bold" text-anchor="middle">JUNE 21 SOLSTICE</text>
                <text x="12" y="36" fill="#e2e8f0" font-size="7.5">🇮🇳 New Delhi</text>
                <text x="12" y="56" fill="#e2e8f0" font-size="7.5">🇯🇵 Tokyo</text>
                <text x="12" y="76" fill="#e2e8f0" font-size="7.5">🇫🇷 Paris</text>
                <text x="12" y="96" fill="#e2e8f0" font-size="7.5">🇺🇸 New York</text>
                <text x="52" y="118" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">177 UN Nations</text>
            </g>

            <!-- Harmony Tag -->
            <rect x="270" y="40" width="105" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="278" y="54" fill="#94a3b8" font-size="7">ANCIENT MEANING</text>
            <text x="278" y="68" fill="#fde047" font-size="9" font-weight="bold">Yuj: To Unite</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="cycleYogaPose()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Cycle Asanas (Poses)
        </button>
        <button onclick="guidePranayamaBreath()" class="p-2 bg-teal-600 hover:bg-teal-500 rounded-lg text-xs font-bold text-white">
            Mindful Breath (Pranayama)
        </button>
    </div>
    <div id="sim5Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Universal Science of Wellness:</strong> Practiced in India for over 3,000 years, Yoga unites body, breath, and mind. In 2014, the UN declared June 21 as International Day of Yoga.
    </div>
</div>
"""

# SIM 6: Chilli's Journey (Trans-Atlantic Spice Route)
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Chilli's Journey: From South America to Goa</span>
        <p class="text-[11px] text-slate-400">Discover how red chillies crossed the Atlantic to replace black pepper in Indian curries!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Ocean Waves Background -->
            <path d="M0,160 Q100,150 200,160 T400,160 L400,240 L0,240 Z" fill="#0369a1" opacity="0.3"/>

            <!-- Left Stage: South America Origin (Chilli Pod) -->
            <g id="southAmericaStage" transform="translate(60, 50)">
                <rect x="0" y="0" width="105" height="120" rx="8" fill="#020617" stroke="#e11d48" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#f43f5e" font-size="8" font-weight="bold" text-anchor="middle">SOUTH AMERICA</text>
                <!-- Red Chilli Graphic -->
                <path d="M52,35 Q65,45 62,75 Q60,95 48,105 Q52,90 48,70 Q45,50 52,35 Z" fill="#e11d48"/>
                <path d="M52,35 Q50,25 45,22" stroke="#15803d" stroke-width="2.5" fill="none"/>
                <text x="52" y="114" fill="#fecdd3" font-size="7" font-weight="bold" text-anchor="middle">Capsicum Native</text>
            </g>

            <!-- Center: Sailing Caravel Ship -->
            <g id="traderShip" transform="translate(180, 85)">
                <path d="M5,40 L35,40 L40,28 L0,28 Z" fill="#78350f"/>
                <!-- White Sails -->
                <polygon points="12,25 24,5 24,25" fill="#f8fafc"/>
                <polygon points="26,25 36,8 36,25" fill="#e2e8f0"/>
                <line x1="24" y1="5" x2="24" y2="28" stroke="#475569" stroke-width="1.5"/>
                <text x="20" y="52" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">1500s Trade</text>
            </g>

            <!-- Right Stage: India (Goa & Western Ghats) -->
            <g id="indiaStage" transform="translate(245, 50)">
                <rect x="0" y="0" width="105" height="120" rx="8" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">INDIA (GOA)</text>
                <!-- Black Pepper Berries (Indigenous) -->
                <circle cx="38" cy="50" r="5" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <circle cx="48" cy="45" r="5" fill="#0f172a" stroke="#475569" stroke-width="1"/>
                <circle cx="58" cy="52" r="5" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <circle cx="46" cy="58" r="5" fill="#0f172a" stroke="#475569" stroke-width="1"/>
                <!-- Green Chilli Adaptation -->
                <path d="M52,70 Q62,80 58,95 Q54,105 48,110 Q50,98 48,85 Z" fill="#16a34a"/>
                <text x="52" y="32" fill="#94a3b8" font-size="6.5" text-anchor="middle">Old: Black Pepper</text>
                <text x="52" y="116" fill="#86efac" font-size="6.5" font-weight="bold" text-anchor="middle">New: Green Chilli</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="sailChilliShip()" class="p-2 bg-rose-600 hover:bg-rose-500 rounded-lg text-xs font-bold text-white">
            Sail Portuguese Ship to Goa
        </button>
        <button onclick="comparePepperChilli()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Compare Pepper vs Chilli
        </button>
    </div>
    <div id="sim6Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Global Spice Swap:</strong> 500 years ago, Indian cooking relied on black pepper from Kerala. Portuguese sailors carried fiery red chillies from South America to Goa, permanently transforming Indian food!
    </div>
</div>
"""

# SIM 7: Sweet Sugar (Ancient Indian Sugarcane Press)
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Sweet Sugar: India's Gift of Gur & Sarkara</span>
        <p class="text-[11px] text-slate-400">Discover how ancient Indian artisans crushed sugarcane to invent jaggery and crystalline sugar!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/40 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Sugarcane Stalks (Left) -->
            <g id="sugarcaneStalks" transform="translate(50, 40)">
                <rect x="0" y="0" width="10" height="140" rx="3" fill="#65a30d" stroke="#365314" stroke-width="1"/>
                <line x1="0" y1="35" x2="10" y2="35" stroke="#365314" stroke-width="1.5"/>
                <line x1="0" y1="70" x2="10" y2="70" stroke="#365314" stroke-width="1.5"/>
                <line x1="0" y1="105" x2="10" y2="105" stroke="#365314" stroke-width="1.5"/>
                
                <rect x="18" y="10" width="10" height="130" rx="3" fill="#84cc16" stroke="#365314" stroke-width="1"/>
                <line x1="18" y1="45" x2="28" y2="45" stroke="#365314" stroke-width="1.5"/>
                <line x1="18" y1="80" x2="28" y2="80" stroke="#365314" stroke-width="1.5"/>
                <line x1="18" y1="115" x2="28" y2="115" stroke="#365314" stroke-width="1.5"/>
                <text x="14" y="155" fill="#a3e635" font-size="8" font-weight="bold" text-anchor="middle">Sugarcane</text>
            </g>

            <!-- Boiling Kadai (Pan) for Jaggery -->
            <g id="boilingKadai" transform="translate(150, 90)">
                <!-- Clay Furnace Bottom with Fire -->
                <polygon points="10,80 70,80 60,60 20,60" fill="#78350f"/>
                <path d="M30,75 Q40,55 50,75 Z" fill="#f97316"/>
                <circle cx="40" cy="68" r="4" fill="#fde047"/>
                <!-- Iron Kadai -->
                <ellipse cx="40" cy="55" rx="35" ry="12" fill="#334155" stroke="#1e293b" stroke-width="2"/>
                <!-- Golden Boiling Juice / Jaggery -->
                <ellipse id="boilingLiquid" cx="40" cy="53" rx="30" ry="9" fill="#d97706"/>
                <!-- Steam Vapor -->
                <path d="M30,42 Q33,25 28,15" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.4"/>
                <path d="M45,42 Q48,25 43,15" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.4"/>
                <text x="40" y="95" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Boiling Gur (Jaggery)</text>
            </g>

            <!-- Crystalline Sugar Crystals (Right) -->
            <g id="sugarCrystalsGroup" transform="translate(280, 50)">
                <rect x="0" y="0" width="95" height="110" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5" opacity="0.95"/>
                <text x="47" y="18" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">SARKARA</text>
                <!-- White Crystals -->
                <polygon points="47,35 60,48 47,60 34,48" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
                <polygon points="28,65 38,75 28,85 18,75" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
                <polygon points="62,68 72,78 62,88 52,78" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
                <text x="47" y="100" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Sugar & Candy</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="crushSugarcaneJuice()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Boil Cane into Golden Jaggery
        </button>
        <button onclick="crystallizeSugar()" class="p-2 bg-yellow-600 hover:bg-yellow-500 rounded-lg text-xs font-bold text-white">
            Refine into Sarkara Crystals
        </button>
    </div>
    <div id="sim7Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Sweet Story:</strong> India pioneered sugarcane processing into gur and sparkling crystalline sugar (Sarkara). Persian and Arab merchants spread this sweet invention across the globe!
    </div>
</div>
"""

# SIM 8: Mexican Marigold (Aztec Bloom to Indian Garland)
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-orange-400 uppercase tracking-wider block mb-1">Mexican Marigold: Aztec Bloom to Indian Garland</span>
        <p class="text-[11px] text-slate-400">Trace the Genda Phool from ancient Aztec festivals to Indian wedding garlands and pest defense!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Aztec Temple Pyramid Silhouette (Left) -->
            <polygon points="10,130 50,50 90,130" fill="#334155" opacity="0.4"/>
            <polygon points="35,70 65,70 60,50 40,50" fill="#475569" opacity="0.6"/>
            <text x="50" y="145" fill="#94a3b8" font-size="7" text-anchor="middle">Aztec Mexico</text>

            <!-- Center: Giant Vibrant Marigold Flower (Genda Phool) -->
            <g id="marigoldBloom" transform="translate(190, 85)">
                <!-- Petal Layers -->
                <circle cx="10" cy="10" r="32" fill="#ea580c"/>
                <circle cx="10" cy="10" r="24" fill="#f97316"/>
                <circle cx="10" cy="10" r="16" fill="#f59e0b"/>
                <circle cx="10" cy="10" r="8" fill="#fde047"/>
                <path d="M10,42 Q8,75 10,95" stroke="#15803d" stroke-width="4" fill="none"/>
            </g>

            <!-- Right Stage: Indian Festive Garland & Soil Defense -->
            <g id="indianFestiveGarland" transform="translate(280, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#ea580c" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="16" fill="#fb923c" font-size="8" font-weight="bold" text-anchor="middle">INDIAN FESTIVALS</text>
                
                <!-- Garland Arc with 5 Miniature Marigolds -->
                <circle cx="30" cy="38" r="8" fill="#f97316"/>
                <circle cx="45" cy="46" r="9" fill="#f59e0b"/>
                <circle cx="60" cy="46" r="9" fill="#ea580c"/>
                <circle cx="75" cy="38" r="8" fill="#fde047"/>
                <text x="52" y="68" fill="#fde68a" font-size="7" text-anchor="middle">Diwali Garlands</text>

                <!-- Natural Garden Soil Nematode Defense -->
                <rect x="12" y="80" width="80" height="42" rx="4" fill="#14532d"/>
                <text x="52" y="95" fill="#86efac" font-size="7" font-weight="bold" text-anchor="middle">Root Bio-Defense</text>
                <text x="52" y="112" fill="#bbf7d0" font-size="6.5" text-anchor="middle">Repels Nematodes</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="stringMarigoldGarland()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            String Festive Diwali Garland
        </button>
        <button onclick="testNematodeDefense()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Test Soil Pest Protection
        </button>
    </div>
    <div id="sim8Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Aztec Immigrant:</strong> Marigolds travelled from Aztec ceremonies in Mexico to Indian soil 500 years ago, becoming an essential blossom for temple prayers, weddings, and organic garden pest control!
    </div>
</div>
"""

print("Simulators 1 to 8 defined.")


"""
Simulators 1 to 16 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Zero raw LaTeX! Clean Unicode symbols.
"""
SIMS = {}
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

SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Indian Cattle in Brazil (Zebu Adaptation Lab)</span>
        <p class="text-[11px] text-slate-400">Discover why Gir, Kankrej, and Ongole cattle from India thrive under Brazil's tropical sun!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Tropical Blistering Sun Overhead -->
            <circle cx="200" cy="40" r="24" fill="#f59e0b" opacity="0.9"/>
            <circle cx="200" cy="40" r="32" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.5"/>

            <!-- Center Stage: Indian Zebu Cow Model (Gir / Ongole) -->
            <g id="zebuCattleGraphic" transform="translate(130, 80)">
                <!-- Body with Prominent Hump -->
                <path d="M40,65 Q35,30 55,25 Q70,40 100,45 Q120,45 125,75 Q125,95 110,95 L40,95 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Prominent Hump -->
                <ellipse cx="60" cy="28" rx="14" ry="10" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
                <!-- Neck & Dewlap (Loose Skin for Heat Dissipation) -->
                <path d="M40,65 Q30,85 45,95" stroke="#94a3b8" stroke-width="4" fill="none"/>
                <!-- Head & Sweeping Horns -->
                <circle cx="30" cy="50" r="12" fill="#e2e8f0"/>
                <path d="M28,40 Q25,25 35,20" stroke="#475569" stroke-width="2.5" fill="none"/>
                <!-- Legs -->
                <line x1="48" y1="95" x2="48" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="65" y1="95" x2="65" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="95" y1="95" x2="95" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="112" y1="95" x2="112" y2="135" stroke="#94a3b8" stroke-width="4"/>
            </g>

            <!-- Adaptation Advantage Card (Left) -->
            <g transform="translate(20, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">SUPER ADAPTATIONS</text>
                <text x="10" y="38" fill="#e2e8f0" font-size="7.5">• Prominent Hump</text>
                <text x="10" y="58" fill="#e2e8f0" font-size="7.5">• Large Cool Dewlap</text>
                <text x="10" y="78" fill="#e2e8f0" font-size="7.5">• Abundant Sweat Glands</text>
                <text x="10" y="98" fill="#e2e8f0" font-size="7.5">• Tick & Heat Immunity</text>
                <text x="52" y="122" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Thrives at 42°C</text>
            </g>

            <!-- Brazilian Dairy Share Badge (Right) -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">BRAZIL LIVESTOCK</text>
                <circle cx="52" cy="60" r="30" fill="#14532d"/>
                <text x="52" y="58" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">>75%</text>
                <text x="52" y="72" fill="#86efac" font-size="7" text-anchor="middle">Indian Lineage</text>
                <text x="52" y="105" fill="#e2e8f0" font-size="7" text-anchor="middle">Nelore (Ongole)</text>
                <text x="52" y="120" fill="#e2e8f0" font-size="7" text-anchor="middle">Gir Leiteiro</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="testHeatTolerance()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Test Tropical Heat Resistance
        </button>
        <button onclick="inspectBrazilianStamp()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            View Brazil Postage Stamp
        </button>
    </div>
    <div id="sim9Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Indian Lineage in Brazil:</strong> Over three-quarters of Brazil's cattle carry Indian Zebu genetics. Their sweat glands, loose dewlap, and natural tick resistance made them the kings of South American pasturelands!
    </div>
</div>
"""

SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Web of Life: The Planetary Interconnectedness Network</span>
        <p class="text-[11px] text-slate-400">Trace how solar energy, green plants, pollinators, birds, animals, and humans are bound in one web!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Interconnecting Radiant Web Strands -->
            <line x1="200" y1="40" x2="100" y2="100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="200" y1="40" x2="300" y2="100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="100" y1="100" x2="140" y2="180" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="300" y1="100" x2="260" y2="180" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="140" y1="180" x2="260" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="200" y1="40" x2="200" y2="120" stroke="#fde047" stroke-width="2" opacity="0.7"/>

            <!-- Node 1: Sun Energy (Top) -->
            <g class="cursor-pointer" onclick="selectWebNode('sun')">
                <circle cx="200" cy="40" r="22" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
                <text x="200" y="44" fill="#020617" font-size="7.5" font-weight="bold" text-anchor="middle">Sun Energy</text>
            </g>

            <!-- Node 2: Producers (Green Plants & Trees) -->
            <g class="cursor-pointer" onclick="selectWebNode('plants')">
                <circle cx="100" cy="100" r="22" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                <text x="100" y="104" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Producers</text>
            </g>

            <!-- Node 3: Pollinators & Birds -->
            <g class="cursor-pointer" onclick="selectWebNode('pollinators')">
                <circle cx="300" cy="100" r="22" fill="#ea580c" stroke="#fbbf24" stroke-width="2"/>
                <text x="300" y="104" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Pollinators</text>
            </g>

            <!-- Node 4: Humans & Animals -->
            <g class="cursor-pointer" onclick="selectWebNode('herbivores')">
                <circle cx="140" cy="180" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="140" y="184" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Humans & Herd</text>
            </g>

            <!-- Node 5: Soil Decomposers & Microbes -->
            <g class="cursor-pointer" onclick="selectWebNode('decomposers')">
                <circle cx="260" cy="180" r="22" fill="#78350f" stroke="#d97706" stroke-width="2"/>
                <text x="260" y="184" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Decomposers</text>
            </g>

            <!-- Center Core: Harmony of the Web -->
            <circle cx="200" cy="120" r="16" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="200" y="123" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">WEB</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="selectWebNode('plants')" class="p-2 bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            Plants (Producers)
        </button>
        <button onclick="selectWebNode('pollinators')" class="p-2 bg-amber-950/80 hover:bg-amber-900 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            Birds & Bees
        </button>
        <button onclick="selectWebNode('decomposers')" class="p-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 rounded-lg text-xs font-bold text-slate-200">
            Soil Decomposers
        </button>
    </div>
    <div id="sim10Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Web of Life:</strong> Every organism plays an irreplaceable role. Green plants capture sunlight, pollinators fertilize crops, starlings eat pests, and soil microbes recycle vital nutrients!
    </div>
</div>
"""

SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">Vasudhaiva Kutumbakam: Planetary Family Wheel</span>
        <p class="text-[11px] text-slate-400">Celebrate the timeless Sanskrit philosophy: humans, animals, plants, rivers, & sky form one family!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-purple-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Outer Rotary Family Ring -->
            <g id="familyMandalaGroup" transform="translate(200, 120)">
                <circle cx="0" cy="0" r="88" fill="none" stroke="#6b21a8" stroke-width="2" stroke-dasharray="4,4"/>
                
                <!-- 5 Family Segments around the circle -->
                <!-- 1. All Humanity (0 deg: 70, 0) -->
                <circle cx="70" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="70" y="4" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Humanity</text>

                <!-- 2. Animal Kingdom (72 deg: 21.6, 66.5) -->
                <circle cx="21.6" cy="66.5" r="16" fill="#ea580c" stroke="#fbbf24" stroke-width="2"/>
                <text x="21.6" y="70" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Animals</text>

                <!-- 3. Trees & Forests (144 deg: -56.6, 41.1) -->
                <circle cx="-56.6" cy="41.1" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                <text x="-56.6" y="45" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Forests</text>

                <!-- 4. Rivers & Oceans (216 deg: -56.6, -41.1) -->
                <circle cx="-56.6" cy="-41.1" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                <text x="-56.6" y="-37" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Rivers</text>

                <!-- 5. Atmosphere & Sky (288 deg: 21.6, -66.5) -->
                <circle cx="21.6" cy="-66.5" r="16" fill="#7c3aed" stroke="#c084fc" stroke-width="2"/>
                <text x="21.6" y="-62.5" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Atmosphere</text>

                <!-- Center Core: Vasudhaiva Kutumbakam -->
                <circle cx="0" cy="0" r="32" fill="#f59e0b" stroke="#fde047" stroke-width="2"/>
                <text x="0" y="-3" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">ONE EARTH</text>
                <text x="0" y="9" fill="#020617" font-size="6.5" font-weight="bold" text-anchor="middle">ONE FAMILY</text>
            </g>

            <!-- Sanskrit Wisdom Pill -->
            <rect x="25" y="15" width="135" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="28" fill="#94a3b8" font-size="7">MAHA UPANISHAD</text>
            <text x="35" y="42" fill="#c084fc" font-size="9" font-weight="bold">वसुधैव कुटुम्बकम्</text>
            <text x="35" y="52" fill="#cbd5e1" font-size="7">The World is One Family</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="rotateFamilyWheel()" class="p-2 bg-purple-600 hover:bg-purple-500 rounded-lg text-xs font-bold text-white">
            Spin Planetary Family Wheel
        </button>
        <button onclick="reciteUniversalMotto()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Recite Sanskrit Shloka
        </button>
    </div>
    <div id="sim11Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Universal Kinship:</strong> To a noble mind, the entire Earth is one single household. We share one sky, one water cycle, and one destiny with all living beings!
    </div>
</div>
"""

SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Prakriti Rakshati Rakshita (Reciprocal Bio-Shield)</span>
        <p class="text-[11px] text-slate-400">Discover how protecting mangrove forests shields coastal villages from cyclonic sea surges!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Fierce Ocean Wave Surge (Left) -->
            <path id="cycloneSurgeWave" d="M0,180 Q60,110 110,140 Q130,160 160,180 L0,240 Z" fill="#0284c7" opacity="0.8"/>
            <path d="M0,195 Q70,140 130,170 L0,240 Z" fill="#0369a1" opacity="0.6"/>

            <!-- Mangrove Bio-Shield Buffer (Center: Stilt Roots & Dense Foliage) -->
            <g id="mangroveShieldGroup" transform="translate(170, 100)">
                <!-- Interlocking Stilt Roots -->
                <path d="M25,50 Q10,75 0,90" stroke="#78350f" stroke-width="4" fill="none"/>
                <path d="M25,50 Q40,75 50,90" stroke="#78350f" stroke-width="4" fill="none"/>
                <path d="M25,50 Q30,70 25,90" stroke="#78350f" stroke-width="3.5" fill="none"/>
                <!-- Dense Green Canopy -->
                <circle cx="25" cy="35" r="28" fill="#15803d" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <circle cx="10" cy="30" r="18" fill="#16a34a" opacity="0.9"/>
                <circle cx="40" cy="30" r="18" fill="#16a34a" opacity="0.9"/>
                <text x="25" y="105" fill="#86efac" font-size="7.5" font-weight="bold" text-anchor="middle">Mangrove Shield</text>
            </g>

            <!-- Protected Coastal Village (Right) -->
            <g id="safeVillage" transform="translate(290, 120)">
                <!-- House 1 -->
                <polygon points="25,20 5,40 45,40" fill="#b45309"/>
                <rect x="10" y="40" width="30" height="25" fill="#fed7aa" stroke="#78350f" stroke-width="1"/>
                <!-- Green Tree -->
                <circle cx="65" cy="35" r="16" fill="#15803d"/>
                <rect x="62" y="50" width="6" height="15" fill="#78350f"/>
                <text x="35" y="80" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Safe Coastal Village</text>
            </g>

            <!-- MoEFCC Motto Banner -->
            <rect x="25" y="20" width="150" height="40" rx="6" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
            <text x="35" y="34" fill="#4ade80" font-size="8.5" font-weight="bold">प्रकृतिः रक्षति रक्षिता</text>
            <text x="35" y="48" fill="#e2e8f0" font-size="7">Nature Protects if Protected</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="launchCycloneSurge()" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Simulate Cyclone Storm Surge
        </button>
        <button onclick="reinforceMangroves()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Nurture Mangrove Buffer
        </button>
    </div>
    <div id="sim12Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Reciprocal Guardianship:</strong> When coastal communities protect mangrove forests, the tangled roots break high waves, safeguarding homes and human lives during tropical cyclones.
    </div>
</div>
"""

SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Global Travelers: The World Inside Your Lunchbox</span>
        <p class="text-[11px] text-slate-400">Click everyday foods and stationery to uncover their incredible geographic birthplaces!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Lunchbox Graphic -->
            <g id="lunchboxContainer" transform="translate(130, 45)">
                <rect x="0" y="0" width="140" height="110" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <line x1="0" y1="55" x2="140" y2="55" stroke="#334155" stroke-width="1.5"/>
                <line x1="70" y1="55" x2="70" y2="110" stroke="#334155" stroke-width="1.5"/>

                <!-- Compartment 1: Aloo Paratha (Potatoes) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('potato')">
                    <circle cx="35" cy="28" r="16" fill="#d97706"/>
                    <text x="35" y="31" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Potato</text>
                </g>

                <!-- Compartment 2: Tomato & Chilli Salad -->
                <g class="cursor-pointer" onclick="inspectLunchItem('tomato')">
                    <circle cx="105" cy="28" r="16" fill="#dc2626"/>
                    <text x="105" y="31" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Tomato</text>
                </g>

                <!-- Compartment 3: Sweet Rice Kheer (Rice & Sugar) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('rice')">
                    <ellipse cx="35" cy="82" rx="20" ry="14" fill="#f8fafc"/>
                    <text x="35" y="85" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">Rice/Sugar</text>
                </g>

                <!-- Compartment 4: Notebook & Pen (Paper) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('paper')">
                    <rect x="85" y="68" width="35" height="28" rx="2" fill="#3b82f6"/>
                    <text x="102" y="85" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Paper</text>
                </g>
            </g>

            <!-- Dynamic Origin Card (Right Stage) -->
            <g id="itemOriginCard" transform="translate(290, 35)">
                <rect x="0" y="0" width="100" height="130" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5" opacity="0.95"/>
                <text id="lunchItemTitle" x="50" y="18" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Potato Origin</text>
                <text id="lunchItemRegion" x="50" y="36" fill="#38bdf8" font-size="7.5" text-anchor="middle">Andes Mountains</text>
                <text id="lunchItemCountry" x="50" y="52" fill="#cbd5e1" font-size="7" text-anchor="middle">(Peru / Bolivia)</text>
                <text id="lunchItemDate" x="50" y="75" fill="#e2e8f0" font-size="7" text-anchor="middle">Arrived in India:</text>
                <text id="lunchItemAge" x="50" y="90" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">~400 Years Ago</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="inspectLunchItem('potato')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Potato
        </button>
        <button onclick="inspectLunchItem('tomato')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-rose-500/50 text-[10px] font-bold text-rose-300">
            Tomato/Chilli
        </button>
        <button onclick="inspectLunchItem('rice')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Rice/Sugar
        </button>
        <button onclick="inspectLunchItem('paper')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            Paper
        </button>
    </div>
    <div id="sim13Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Global Meal:</strong> Potatoes and tomatoes originated in the South American Andes; rice and sugarcane sugar came from ancient India; and paper was invented in China!
    </div>
</div>
"""

SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Earth Guardians: Daily Environmental Impact Dashboard</span>
        <p class="text-[11px] text-slate-400">Toggle daily mindful actions to see your real-time environmental score and water/energy savings!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Central Eco-Badge Gauge -->
            <g id="ecoGaugeGroup" transform="translate(200, 100)">
                <circle cx="0" cy="0" r="60" fill="#0f172a" stroke="#334155" stroke-width="4"/>
                <circle id="ecoMeterArc" cx="0" cy="0" r="60" fill="none" stroke="#22c55e" stroke-width="5" stroke-dasharray="377" stroke-dashoffset="180"/>
                <text x="0" y="-8" fill="#94a3b8" font-size="8" text-anchor="middle">PLANET IMPACT</text>
                <text id="ecoScoreText" x="0" y="16" fill="#4ade80" font-size="20" font-weight="bold" text-anchor="middle">75%</text>
                <text x="0" y="32" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Guardian Level</text>
            </g>

            <!-- Metrics Panel Left -->
            <g transform="translate(25, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">WATER SAVED</text>
                <text id="waterSavedMetric" x="52" y="45" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">24 Litres</text>
                <text x="52" y="60" fill="#94a3b8" font-size="7" text-anchor="middle">per day</text>
                <line x1="10" y1="72" x2="95" y2="72" stroke="#334155" stroke-width="1"/>
                <text x="52" y="90" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">COAL SAVED</text>
                <text id="energySavedMetric" x="52" y="112" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">1.2 kWh</text>
            </g>

            <!-- Metrics Panel Right -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">PLASTIC AVOIDED</text>
                <text id="plasticAvoidedMetric" x="52" y="45" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">4 Bags</text>
                <text x="52" y="60" fill="#94a3b8" font-size="7" text-anchor="middle">cloth upcycled</text>
                <line x1="10" y1="72" x2="95" y2="72" stroke="#334155" stroke-width="1"/>
                <text x="52" y="90" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">TREES NURTURED</text>
                <text id="treesPlantedMetric" x="52" y="112" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">1 Neem Sapling</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="toggleAction('tap')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            Fix Leaking Tap
        </button>
        <button onclick="toggleAction('power')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Turn Off Fan/Light
        </button>
        <button onclick="toggleAction('plastic')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Refuse Plastic Bag
        </button>
        <button onclick="toggleAction('tree')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-purple-500/50 text-[10px] font-bold text-purple-300">
            Plant Neem Tree
        </button>
    </div>
    <div id="sim14Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Daily Stewardship:</strong> Closing taps while brushing saves up to 10 litres of water daily. Turning off unused fans cuts coal burning. Small daily choices protect our shared planet!
    </div>
</div>
"""

SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider block mb-1">Seasons Across Borders: Hemispheric Clock</span>
        <p class="text-[11px] text-slate-400">Discover how Earth's 23.5° axial tilt creates opposite seasons across Northern & Southern Hemispheres!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Sun Rays Coming from Left -->
            <circle cx="20" cy="120" r="35" fill="#f59e0b" opacity="0.8"/>
            <line x1="55" y1="80" x2="130" y2="80" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>
            <line x1="55" y1="120" x2="130" y2="120" stroke="#fde047" stroke-width="2"/>
            <line x1="55" y1="160" x2="130" y2="160" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>

            <!-- Tilted Earth Globe (Center) -->
            <g id="tiltedEarthGlobe" transform="translate(190, 120)">
                <!-- Earth Sphere -->
                <circle cx="0" cy="0" r="60" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Tilted Axis Line (23.5 deg) -->
                <line x1="-25" y1="-75" x2="25" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="4,3"/>
                <!-- Equator Line -->
                <line x1="-60" y1="20" x2="60" y2="-20" stroke="#fbbf24" stroke-width="1.5"/>

                <!-- Northern Hemisphere (India - Tilted Toward Sun) -->
                <circle cx="-15" cy="-25" r="7" fill="#15803d"/>
                <text x="-15" y="-12" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">India</text>

                <!-- Southern Hemisphere (Australia - Tilted Away) -->
                <circle cx="25" cy="30" r="7" fill="#b45309"/>
                <text x="25" y="44" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Australia</text>
            </g>

            <!-- Hemisphere Contrast Cards (Right Side) -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="110" height="135" rx="8" fill="#020617" stroke="#334155" opacity="0.95"/>
                <text x="55" y="18" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">JUNE SOLSTICE</text>
                
                <!-- North Status -->
                <rect x="8" y="30" width="94" height="42" rx="4" fill="#14532d"/>
                <text x="55" y="44" fill="#4ade80" font-size="7.5" font-weight="bold" text-anchor="middle">Northern Hemisphere</text>
                <text x="55" y="58" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">SUMMER (India)</text>

                <!-- South Status -->
                <rect x="8" y="80" width="94" height="42" rx="4" fill="#082f49"/>
                <text x="55" y="94" fill="#38bdf8" font-size="7.5" font-weight="bold" text-anchor="middle">Southern Hemisphere</text>
                <text x="55" y="108" fill="#bae6fd" font-size="9" font-weight="bold" text-anchor="middle">WINTER (Australia)</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="setSolsticeSeason('june')" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            June: Summer (North) / Winter (South)
        </button>
        <button onclick="setSolsticeSeason('december')" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            December: Winter (North) / Summer (South)
        </button>
    </div>
    <div id="sim15Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Hemispheric Harmony:</strong> When children in India celebrate summer vacation in June, children in Australia and Argentina are wearing woollens during winter! Migrating animals use these opposite cycles to travel and thrive.
    </div>
</div>
"""

SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Our Living Earth: Four Planetary Spheres Laboratory</span>
        <p class="text-[11px] text-slate-400">Interact with the four interconnected spheres: Atmosphere, Hydrosphere, Biosphere, and Geosphere!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Earth with 4 Concentric Spheres -->
            <g id="planetarySpheresGraphic" transform="translate(160, 120)">
                <!-- 1. Geosphere (Solid Core/Crust) -->
                <circle cx="0" cy="0" r="40" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                <text x="0" y="4" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Geosphere</text>

                <!-- 2. Hydrosphere (Water Layer) -->
                <circle id="hydroRing" cx="0" cy="0" r="56" fill="none" stroke="#0284c7" stroke-width="3" opacity="0.8"/>

                <!-- 3. Biosphere (Life Layer) -->
                <circle id="bioRing" cx="0" cy="0" r="70" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,4" opacity="0.9"/>

                <!-- 4. Atmosphere (Air Shield) -->
                <circle id="atmoRing" cx="0" cy="0" r="84" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>
            </g>

            <!-- Layer Information Card (Right Stage) -->
            <g transform="translate(265, 40)">
                <rect x="0" y="0" width="120" height="145" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text id="sphereTitle" x="60" y="18" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Atmosphere (Air)</text>
                <text id="sphereDesc1" x="10" y="40" fill="#e2e8f0" font-size="7">• 78% Nitrogen, 21% O₂</text>
                <text id="sphereDesc2" x="10" y="60" fill="#e2e8f0" font-size="7">• Shields UV with Ozone</text>
                <text id="sphereDesc3" x="10" y="80" fill="#e2e8f0" font-size="7">• Circulates rainclouds</text>
                <text id="sphereDesc4" x="10" y="100" fill="#e2e8f0" font-size="7">• Traps warmth (Greenhouse)</text>
                <rect x="10" y="115" width="100" height="20" rx="3" fill="#0369a1"/>
                <text x="60" y="128" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Common Heritage</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="inspectSphere('atmosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            Atmosphere
        </button>
        <button onclick="inspectSphere('hydrosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            Hydrosphere
        </button>
        <button onclick="inspectSphere('biosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Biosphere
        </button>
        <button onclick="inspectSphere('geosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Geosphere
        </button>
    </div>
    <div id="sim16Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Our Living Earth:</strong> All four spheres—air, water, living creatures, and soil—interact seamlessly. We are proud custodians of this miracle planet. Vasudhaiva Kutumbakam!
    </div>
</div>
"""


# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 1 to 8
Class 4 Science Chapter 10: Our Sky
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part1 = {
    # Simulator 1: Changing Daily Sky
    "sim_daily_sky_cycle": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">24-Hour Diurnal Sky & Solar Arc Simulator</h3>
                <p class="text-xs text-slate-400">Slide the time of day to observe atmospheric light, color gradients, and solar position shifts.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Time: <b id="timeDisplayVal" class="text-amber-400">06:00 AM (Dawn)</b></span>
                <input type="range" id="dailyTimeSlider" min="0" max="24" value="6" step="1" oninput="updateDailySkyTime(this.value)" class="w-28 sm:w-36 accent-amber-500">
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Sky Canvas / SVG View -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 500 220" class="w-full h-auto">
                    <!-- Sky Background with dynamic gradient fill -->
                    <rect id="skyBackgroundRect" x="0" y="0" width="500" height="170" fill="#f97316" opacity="0.85"/>
                    
                    <!-- Celestial Sun -->
                    <g id="celestialSunGroup" transform="translate(60, 140)">
                        <circle cx="0" cy="0" r="18" fill="#fbbf24" filter="drop-shadow(0 0 8px #f59e0b)"/>
                        <circle cx="0" cy="0" r="24" fill="#fef08a" opacity="0.3"/>
                    </g>

                    <!-- Celestial Moon & Stars (Night) -->
                    <g id="celestialMoonGroup" transform="translate(250, 60)" class="hidden">
                        <circle cx="0" cy="0" r="14" fill="#e2e8f0" filter="drop-shadow(0 0 6px #cbd5e1)"/>
                        <!-- Little stars -->
                        <circle cx="-80" cy="-30" r="1.5" fill="#ffffff" class="animate-ping"/>
                        <circle cx="80" cy="-20" r="1.5" fill="#ffffff"/>
                        <circle cx="-140" cy="10" r="1.5" fill="#ffffff"/>
                        <circle cx="140" cy="20" r="1.5" fill="#ffffff"/>
                    </g>

                    <!-- Terrestrial Horizon / Silhouette Trees -->
                    <rect x="0" y="170" width="500" height="50" fill="#1e293b"/>
                    <!-- Hills -->
                    <path d="M0,170 Q120,135 240,170 T500,165 L500,220 L0,220 Z" fill="#0f172a"/>
                    <!-- Tree silhouette -->
                    <polygon points="120,170 135,130 150,170" fill="#1e293b"/>
                    <polygon points="380,170 395,125 410,170" fill="#1e293b"/>
                    
                    <!-- Cardinal Directions -->
                    <text x="30" y="195" fill="#94a3b8" font-size="10" font-weight="bold">EAST (Sunrise)</text>
                    <text x="470" y="195" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="end">WEST (Sunset)</text>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="skyPhaseDesc">🌅 Morning Dawn: Golden-orange horizon; birds awake and take flight.</span>
                </div>
            </div>

            <!-- Diurnal Status Card -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wide">Atmospheric Condition</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SOLAR ELEVATION</span>
                        <span id="solarElevVal" class="font-bold text-amber-300">Low Slanted Angle (15°)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">ATMOSPHERIC COLOR</span>
                        <span id="skyColorVal" class="font-semibold text-orange-400">Golden Amber & Soft Rose</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">NATURE BEHAVIOR</span>
                        <span id="natureActVal" class="font-semibold text-emerald-400">Songbirds singing, flowers opening</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 2: The Radiant Sun
    "sim_solar_radiance": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">The Sun: Planetary Powerhouse & Core Fusion</h3>
                <p class="text-xs text-slate-400">Explore solar energy generation, nuclear fusion in the core, and radiation reaching planet Earth.</p>
            </div>
            <button onclick="triggerSolarFlare()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition flex items-center gap-1">
                <span>⚡</span> Release Solar Flare
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Cutaway Solar Core Diagram -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[220px] relative">
                <div class="relative w-44 h-44 rounded-full bg-gradient-to-br from-amber-500 via-orange-600 to-red-700 flex items-center justify-center shadow-2xl border-2 border-yellow-400/80">
                    <!-- Core Glow -->
                    <div id="solarCoreGlow" class="w-20 h-20 rounded-full bg-yellow-200 flex flex-col items-center justify-center shadow-inner animate-pulse">
                        <span class="text-[9px] font-bold text-amber-950">CORE</span>
                        <span class="text-[8px] text-amber-900">15,000,000°C</span>
                    </div>
                    <!-- Radiation Streamers -->
                    <div class="absolute -top-3 w-2 h-6 bg-yellow-300 rounded-full blur-[1px]"></div>
                    <div class="absolute -bottom-3 w-2 h-6 bg-yellow-300 rounded-full blur-[1px]"></div>
                    <div class="absolute -left-3 w-6 h-2 bg-yellow-300 rounded-full blur-[1px]"></div>
                    <div class="absolute -right-3 w-6 h-2 bg-yellow-300 rounded-full blur-[1px]"></div>
                </div>
                <span class="text-[11px] text-amber-300 font-bold mt-3">Hydrogen Fusion into Helium Gas</span>
            </div>

            <!-- Solar Power Functions -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5 text-xs">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">Earth Life Support Engines</span>
                
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex items-start gap-2">
                    <span class="text-base">🌱</span>
                    <div>
                        <span class="font-bold text-emerald-300">Photosynthesis Engine</span>
                        <p class="text-[11px] text-slate-300">Provides light photons for green plants to manufacture carbohydrates and produce oxygen.</p>
                    </div>
                </div>

                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex items-start gap-2">
                    <span class="text-base">💧</span>
                    <div>
                        <span class="font-bold text-cyan-300">Hydrological Water Cycle</span>
                        <p class="text-[11px] text-slate-300">Evaporates ocean water into vapor, driving global rainfall and freshwater replenishment.</p>
                    </div>
                </div>

                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex items-start gap-2">
                    <span class="text-base">💨</span>
                    <div>
                        <span class="font-bold text-yellow-300">Atmospheric Winds</span>
                        <p class="text-[11px] text-slate-300">Unequal solar heating creates pressure differentials, generating planetary wind currents.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 3: Daytime Biological Rhythms
    "sim_biological_rhythms": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Circadian Rhythms: Diurnal vs Nocturnal Behaviors</h3>
                <p class="text-xs text-slate-400">Toggle between Daytime and Nighttime to observe physiological and behavioral shifts in nature.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="setCircadianMode('day')" id="btnCircDay" class="px-3 py-1 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition">☀️ Daytime (Diurnal)</button>
                <button onclick="setCircadianMode('night')" id="btnCircNight" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition">🌙 Nighttime (Nocturnal)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <!-- Card 1: Flora (Sunflower / Jasmine) -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">1. Plant Responses</span>
                <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex flex-col items-center justify-center">
                    <span id="circFloraIcon" class="text-4xl transition-transform duration-500">🌻</span>
                    <span id="circFloraTitle" class="text-xs font-bold text-amber-300 mt-1">Sunflower Heliotropism</span>
                </div>
                <p id="circFloraDesc" class="text-[11px] text-slate-300 leading-snug">Petals wide open, actively facing the Sun to maximize photon absorption.</p>
            </div>

            <!-- Card 2: Aviary / Birds (Sparrow vs Owl) -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-2">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">2. Bird Behaviors</span>
                <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex flex-col items-center justify-center">
                    <span id="circBirdIcon" class="text-4xl transition-transform duration-500">🐦</span>
                    <span id="circBirdTitle" class="text-xs font-bold text-cyan-300 mt-1">Songbirds & Honeybees</span>
                </div>
                <p id="circBirdDesc" class="text-[11px] text-slate-300 leading-snug">Actively flying between trees, foraging for seeds and collecting nectar.</p>
            </div>

            <!-- Card 3: Mammals (Human/Cattle vs Bat) -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-2">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wide">3. Animal Activity</span>
                <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex flex-col items-center justify-center">
                    <span id="circMammalIcon" class="text-4xl transition-transform duration-500">🐄</span>
                    <span id="circMammalTitle" class="text-xs font-bold text-emerald-300 mt-1">Farm Cattle & Humans</span>
                </div>
                <p id="circMammalDesc" class="text-[11px] text-slate-300 leading-snug">Grazing in pasture, farming, schooling, and outdoor agricultural tasks.</p>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Forming Light Shadows
    "sim_shadow_formation": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Optical Shadow Formation: Material Transparency Tester</h3>
                <p class="text-xs text-slate-400">Select different barrier materials to observe how straight light rays interact with obstacles.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="setShadowMaterial('opaque')" id="btnMatOpaque" class="px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition">🪵 Opaque Wood</button>
                <button onclick="setShadowMaterial('translucent')" id="btnMatTranslucent" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">📜 Butter Paper</button>
                <button onclick="setShadowMaterial('transparent')" id="btnMatTransparent" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🪟 Clear Glass</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Ray Diagram SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 500 200" class="w-full h-auto">
                    <!-- Light Source (Lamp / Torch) -->
                    <g transform="translate(30, 80)">
                        <rect x="0" y="10" width="35" height="20" rx="3" fill="#475569"/>
                        <polygon points="35,5 50,0 50,40 35,35" fill="#facc15"/>
                        <circle cx="55" cy="20" r="12" fill="#fef08a" opacity="0.6"/>
                    </g>

                    <!-- Incident Straight Rays -->
                    <line x1="85" y1="95" x2="220" y2="60" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,4"/>
                    <line x1="85" y1="100" x2="220" y2="100" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,4"/>
                    <line x1="85" y1="105" x2="220" y2="140" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,4"/>

                    <!-- Material Obstacle Barrier -->
                    <g id="materialBarrierGroup" transform="translate(220, 50)">
                        <rect id="barrierRect" x="0" y="0" width="25" height="100" rx="4" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                        <text id="barrierLabel" x="12" y="55" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 12 55)">Opaque Wood</text>
                    </g>

                    <!-- Transmitted Rays (Dynamic) -->
                    <g id="transmittedRaysGroup">
                        <!-- Blocked by default -->
                    </g>

                    <!-- Projection Screen -->
                    <rect x="440" y="20" width="10" height="160" rx="2" fill="#cbd5e1" stroke="#94a3b8"/>
                    <text x="445" y="15" fill="#94a3b8" font-size="9" text-anchor="middle">Screen</text>

                    <!-- Cast Shadow on Screen -->
                    <rect id="castShadowRect" x="438" y="45" width="6" height="110" rx="2" fill="#0f172a" opacity="0.95"/>
                    <text id="shadowLabel" x="420" y="105" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="end">Dark Shadow</text>
                </svg>
            </div>

            <!-- Optical Physics Explanation -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Optical Law</h4>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs space-y-1">
                    <span class="text-amber-300 font-bold block">Rectilinear Propagation:</span>
                    <span id="opticsLawText" class="text-slate-300 leading-snug">
                        Light rays travel in straight lines. Opaque wood blocks rays completely, leaving a sharp, dark shadow on the screen.
                    </span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                    <span>Shadow Density: </span>
                    <span id="shadowDensityVal" class="text-emerald-400 font-bold">100% Solid Black</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Daylong Shadow Shifts
    "sim_daylong_shadows": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Gnomon Post: Sun Elevation & Shadow Length Simulator</h3>
                <p class="text-xs text-slate-400">Drag the solar position across the sky to observe shadow length, orientation, and noon shrinkage.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Solar Position:</span>
                <input type="range" id="gnomonSunSlider" min="1" max="5" value="1" oninput="updateGnomonShadow(this.value)" class="w-28 sm:w-36 accent-amber-500">
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Shadow Plane SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Ground surface -->
                    <rect x="0" y="150" width="500" height="80" fill="#334155"/>
                    <line x1="0" y1="150" x2="500" y2="150" stroke="#64748b" stroke-width="2"/>

                    <!-- East and West Labels -->
                    <text x="30" y="170" fill="#f8fafc" font-size="10" font-weight="bold">WEST (Shadow side)</text>
                    <text x="470" y="170" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">EAST (Sun side)</text>

                    <!-- Vertical Gnomon Post -->
                    <g transform="translate(250, 70)">
                        <rect x="-4" y="0" width="8" height="80" rx="2" fill="#dc2626" stroke="#991b1b" stroke-width="2"/>
                        <circle cx="0" cy="0" r="6" fill="#facc15"/>
                        <text x="0" y="-10" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">Vertical Post</text>
                    </g>

                    <!-- Moving Cast Shadow -->
                    <ellipse id="gnomonCastShadow" cx="170" cy="152" rx="75" ry="6" fill="#0f172a" opacity="0.9"/>

                    <!-- Solar Body positioned dynamically -->
                    <g id="gnomonSunOrb" transform="translate(420, 90)">
                        <circle cx="0" cy="0" r="16" fill="#fbbf24" filter="drop-shadow(0 0 8px #f59e0b)"/>
                        <line x1="0" y1="0" x2="-166" y2="58" stroke="#fde047" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="gnomonStatusText">🌅 Morning (08:00 AM): Low eastern Sun casts very long shadow toward the West.</span>
                </div>
            </div>

            <!-- Quantitative Metrics -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wide">Shadow Metrics</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SHADOW LENGTH</span>
                        <span id="shadowLengthVal" class="font-bold text-amber-300 text-sm">Long (2.8 × Post Height)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SHADOW DIRECTION</span>
                        <span id="shadowDirVal" class="font-semibold text-cyan-300">Pointing West (Opposite Sun)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SOLAR ZENITH ANGLE</span>
                        <span id="solarZenithVal" class="font-semibold text-emerald-400">25° Elevation</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 6: Torchlight Shadow Lab
    "sim_torch_shadow_lab": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Indoor Optics Lab: Torch Distance & Beam Angle</h3>
                <p class="text-xs text-slate-400">Adjust the torch distance slider to test shadow magnification on the wall screen.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Torch Distance:</span>
                <input type="range" id="torchDistSlider" min="20" max="100" value="50" oninput="updateTorchLab(this.value)" class="w-28 sm:w-36 accent-cyan-500">
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Torch Beam View -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 350 200" class="w-full h-auto">
                    <!-- Light Beam Cone -->
                    <polygon id="torchBeamCone" points="80,100 320,30 320,170" fill="#fef08a" opacity="0.25"/>

                    <!-- Torch Icon -->
                    <g id="torchSvgGroup" transform="translate(40, 85)">
                        <rect x="0" y="8" width="30" height="14" rx="2" fill="#64748b"/>
                        <polygon points="30,3 42,0 42,30 30,27" fill="#38bdf8"/>
                        <circle cx="45" cy="15" r="8" fill="#fef08a" opacity="0.8"/>
                    </g>

                    <!-- Figurine Obstacle -->
                    <g transform="translate(180, 70)">
                        <circle cx="0" cy="10" r="8" fill="#dc2626"/>
                        <rect x="-4" y="18" width="8" height="40" fill="#dc2626" rx="2"/>
                        <rect x="-10" y="58" width="20" height="4" fill="#991b1b"/>
                    </g>

                    <!-- Wall Screen -->
                    <rect x="320" y="10" width="8" height="180" fill="#cbd5e1"/>

                    <!-- Projected Shadow on Wall -->
                    <rect id="wallShadowRect" x="317" y="60" width="5" height="80" rx="2" fill="#0f172a" opacity="0.95"/>
                </svg>
                <div class="text-[11px] text-slate-400 text-center mt-1">
                    <span id="torchLabStatus">Distance: 50 cm • Shadow Height: 80 mm</span>
                </div>
            </div>

            <!-- Experimental Insights -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Experimental Observations</span>
                
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-amber-300 font-bold block">1. Distance vs Magnification</span>
                        <p class="text-[11px] text-slate-300">Moving torch closer intercepts wider cone angle → larger magnified shadow.</p>
                    </div>

                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-cyan-300 font-bold block">2. Sharpness vs Diffusion</span>
                        <p class="text-[11px] text-slate-300">Point light sources cast razor-sharp umbra; broad torches create soft penumbra borders.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Historical Shadow Sundials
    "sim_sundial_astronomy": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Jantar Mantar: Brihat Samrat Yantra (Jaipur)</h3>
                <p class="text-xs text-slate-400">Step the solar hour to see the 27-metre stone gnomon cast shadows across calibrated marble quadrants.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="stepSundialHour(-1)" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 font-bold transition">◀ -1 Hr</button>
                <span id="sundialTimeText" class="px-3 py-1 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold text-xs">12:00 PM (Noon)</span>
                <button onclick="stepSundialHour(1)" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 font-bold transition">+1 Hr ▶</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Sundial SVG Graphic -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Ground base -->
                    <rect x="0" y="190" width="500" height="40" fill="#334155"/>

                    <!-- Massive Triangular Gnomon (Jaipur Samrat Yantra: 27 m tall) -->
                    <polygon points="250,30 250,190 120,190" fill="#b45309" stroke="#78350f" stroke-width="2"/>
                    <text x="180" y="160" fill="#fef3c7" font-size="9" font-weight="bold">Triangular Gnomon (27 m)</text>

                    <!-- Curved Marble Quadrant Scale (Left & Right) -->
                    <path d="M120,190 Q180,110 250,105" stroke="#cbd5e1" stroke-width="8" fill="none"/>
                    <path d="M250,105 Q320,110 380,190" stroke="#cbd5e1" stroke-width="8" fill="none"/>
                    <text x="350" y="180" fill="#94a3b8" font-size="8">Marble Scale</text>

                    <!-- Moving Shadow Line on Quadrant -->
                    <line id="sundialShadowLine" x1="250" y1="30" x2="250" y2="105" stroke="#0f172a" stroke-width="4"/>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="sundialAccuracyText">Precision: Local solar time measured to within 2 seconds accuracy.</span>
                    <span class="text-amber-400 font-bold">UNESCO World Heritage Site</span>
                </div>
            </div>

            <!-- Archaeoastronomy Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wide">Observatory Facts</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">FIVE OBSERVATORY CITIES</span>
                        <span class="font-bold text-slate-200">Jaipur, Delhi, Ujjain, Varanasi, Mathura</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">GNOMON ALIGNMENT</span>
                        <span class="font-bold text-cyan-300">Parallel to Earth's axis (Points to Pole Star)</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 8: Creative Shadow Puppetry
    "sim_shadow_puppetry": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Indian Shadow Theatre & Hand Silhouettes</h3>
                <p class="text-xs text-slate-400">Select hand silhouettes or traditional leather puppets to project stories on the glowing screen.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="setShadowPuppet('deer')" id="btnPupDeer" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition">🦌 Deer Silhouette</button>
                <button onclick="setShadowPuppet('bird')" id="btnPupBird" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🦅 Flying Eagle</button>
                <button onclick="setShadowPuppet('dog')" id="btnPupDog" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🐕 Barking Dog</button>
                <button onclick="setShadowPuppet('tholu')" id="btnPupTholu" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🎭 Leather Puppet</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Illuminated Cloth Screen Projection -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div class="w-64 h-40 bg-gradient-to-r from-amber-100 via-yellow-50 to-amber-100 rounded-xl border-4 border-amber-700 shadow-2xl relative flex items-center justify-center overflow-hidden">
                    <!-- Projector Backlight Glow -->
                    <div class="absolute inset-0 bg-yellow-400/20 animate-pulse pointer-events-none"></div>

                    <!-- Shadow Figure Projected -->
                    <div id="puppetFigureDisplay" class="text-6xl text-slate-950 filter drop-shadow-md select-none transition-transform duration-300">
                        🦌
                    </div>
                </div>
                <span class="text-[11px] text-slate-400 mt-2">Backlit Translucent Cotton Screen</span>
            </div>

            <!-- Folk Art Context -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span id="puppetTraditionTitle" class="text-xs font-bold text-amber-400 uppercase tracking-wide">Hand Shadow: Leaping Deer</span>
                <p id="puppetTraditionDesc" class="text-xs text-slate-300 leading-relaxed">
                    Created by joining wrists together with fingers extended upwards like antlers. The thumb forms the deer's muzzle, demonstrating hand optics.
                </p>

                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-xs">
                    <span class="text-cyan-400 font-bold block">Heritage Shadow Traditions:</span>
                    <span class="text-slate-300 block">● <b>Togalu Gombeyaata</b> (Karnataka)</span>
                    <span class="text-slate-300 block">● <b>Tholu Bommalata</b> (Andhra Pradesh)</span>
                    <span class="text-slate-300 block">● <b>Ravanachhaya</b> (Odisha)</span>
                </div>
            </div>
        </div>
    </div>
    """
}


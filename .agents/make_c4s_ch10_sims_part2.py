# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 9 to 16
Class 4 Science Chapter 10: Our Sky
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part2 = {
    # Simulator 9: Dazzling Night Sky
    "sim_night_stargazing": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-indigo-300">Constellation Astronomy: Saptarishi & Polaris (Pole Star)</h3>
                <p class="text-xs text-slate-400">Identify the seven stars of Saptarishi (Ursa Major) and trace the pointer stars directly to Polaris.</p>
            </div>
            <button onclick="toggleConstellationLines()" id="btnConstLines" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                ✨ Connect Saptarishi Stars
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Starlight SVG Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Deep Velvet Night Sky with Ambient Stars -->
                    <rect x="0" y="0" width="500" height="230" fill="#030712"/>
                    
                    <!-- Random Twinkling Background Stars -->
                    <circle cx="40" cy="50" r="1.5" fill="#ffffff" opacity="0.6"/>
                    <circle cx="90" cy="180" r="1" fill="#ffffff" opacity="0.4"/>
                    <circle cx="160" cy="30" r="1.5" fill="#ffffff" opacity="0.5"/>
                    <circle cx="280" cy="40" r="1" fill="#ffffff" opacity="0.4"/>
                    <circle cx="440" cy="70" r="1.5" fill="#ffffff" opacity="0.6"/>
                    <circle cx="470" cy="190" r="1" fill="#ffffff" opacity="0.5"/>

                    <!-- Saptarishi (7 Stars of the Ladle) -->
                    <!-- Handle: 1, 2, 3 -->
                    <circle id="star1" cx="80" cy="150" r="3.5" fill="#67e8f9" filter="drop-shadow(0 0 4px #06b6d4)"/>
                    <circle id="star2" cx="130" cy="130" r="3.5" fill="#67e8f9" filter="drop-shadow(0 0 4px #06b6d4)"/>
                    <circle id="star3" cx="180" cy="135" r="3.5" fill="#67e8f9" filter="drop-shadow(0 0 4px #06b6d4)"/>
                    <!-- Bowl: 4, 5, 6, 7 -->
                    <circle id="star4" cx="220" cy="160" r="3.5" fill="#67e8f9" filter="drop-shadow(0 0 4px #06b6d4)"/>
                    <circle id="star5" cx="280" cy="165" r="4" fill="#a5f3fc" filter="drop-shadow(0 0 6px #22d3ee)"/>
                    <circle id="star6" cx="290" cy="115" r="4" fill="#a5f3fc" filter="drop-shadow(0 0 6px #22d3ee)"/>
                    <circle id="star7" cx="225" cy="110" r="3.5" fill="#67e8f9" filter="drop-shadow(0 0 4px #06b6d4)"/>

                    <!-- Polaris (North Pole Star) -->
                    <circle id="starPolaris" cx="305" cy="35" r="5" fill="#facc15" filter="drop-shadow(0 0 8px #eab308)"/>
                    <text x="320" y="38" fill="#fef08a" font-size="10" font-weight="bold">Polaris (Dhruva Tara)</text>

                    <!-- Constellation Stick Lines (Dynamic) -->
                    <g id="constellationLinesGroup" class="hidden">
                        <line x1="80" y1="150" x2="130" y2="130" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="130" y1="130" x2="180" y2="135" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="180" y1="135" x2="220" y2="160" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="220" y1="160" x2="280" y2="165" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="280" y1="165" x2="290" y2="115" stroke="#06b6d4" stroke-width="2"/>
                        <line x1="290" y1="115" x2="225" y2="110" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="225" y1="110" x2="220" y2="160" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <!-- Pointer Line from Star 5 & 6 to Polaris -->
                        <line x1="290" y1="115" x2="305" y2="35" stroke="#facc15" stroke-width="2" stroke-dasharray="4,4"/>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="stargazingStatusText">Saptarishi (7 Sage Stars) pointing directly to the northern celestial pole.</span>
                </div>
            </div>

            <!-- Stargazing Guide -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-indigo-400 uppercase tracking-wide">Navigational Science</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">POINTER STARS (Merak & Dubhe)</span>
                        <span class="font-bold text-cyan-300">Outer two bowl stars align with North Pole Star</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">ATMOSPHERIC TWINKLING</span>
                        <span class="font-semibold text-slate-200">Refraction through shifting air densities</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 10: Moon Surface Glow
    "sim_moon_surface": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-slate-200">The Moon: Cosmic Mirror & Lunar Geology</h3>
                <p class="text-xs text-slate-400">Discover how sunlight reflects off the airless lunar surface, revealing ancient maria plains and impact craters.</p>
            </div>
            <button onclick="toggleSunbeamReflection()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">
                ☀️ Shine Sunbeam on Moon
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Moon Close-up Surface Graphic -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div class="relative w-40 h-40 rounded-full bg-slate-300 border-4 border-slate-400 shadow-2xl overflow-hidden flex items-center justify-center">
                    <!-- Maria (Dark Basalt Plains) -->
                    <circle cx="35" cy="50" r="18" fill="#64748b" opacity="0.6"/>
                    <circle cx="80" cy="90" r="28" fill="#475569" opacity="0.7"/>
                    <circle cx="115" cy="45" r="15" fill="#64748b" opacity="0.6"/>

                    <!-- Impact Craters -->
                    <circle cx="60" cy="35" r="6" fill="#94a3b8" stroke="#334155" stroke-width="1.5"/>
                    <circle cx="120" cy="110" r="8" fill="#94a3b8" stroke="#334155" stroke-width="1.5"/>
                    <circle cx="45" cy="120" r="5" fill="#94a3b8" stroke="#334155" stroke-width="1.5"/>

                    <!-- Reflected Ray Overlay -->
                    <div id="moonReflectOverlay" class="absolute inset-0 bg-yellow-200/20 opacity-0 transition-opacity duration-700 pointer-events-none"></div>
                </div>
                <span class="text-[11px] text-slate-400 mt-2">Distance from Earth: 384,400 km</span>
            </div>

            <!-- Geology Facts -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5 text-xs">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Lunar Characteristics</span>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">NON-LUMINOUS REFLECTOR</span>
                    <span class="font-bold text-yellow-300">Emits 0% own light; reflects ~12% incident sunlight</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">ZERO WEATHER EROSION</span>
                    <span class="font-semibold text-slate-200">No air or water; impact craters preserved billions of years</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">LUNAR MARIA</span>
                    <span class="font-semibold text-slate-200">Ancient solidified basaltic volcanic lava flows</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 11: Phases Of Moon
    "sim_lunar_phases": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">29.5-Day Lunar Phase Cycle: Amavasya to Poornima</h3>
                <p class="text-xs text-slate-400">Step through the 8 distinct phases to see how orbital alignment creates changing visible shapes.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="stepMoonPhase(-1)" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 font-bold transition">◀ Prev</button>
                <span id="phaseDisplayBadge" class="px-3 py-1 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-bold text-xs">1. New Moon (Amavasya)</span>
                <button onclick="stepMoonPhase(1)" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 font-bold transition">Next ▶</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Earth View Display -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div id="lunarPhaseVisual" class="text-7xl select-none filter drop-shadow-lg transition-transform duration-300">
                    🌑
                </div>
                <span id="lunarPhaseName" class="text-sm font-bold text-cyan-300 mt-3">🌑 New Moon (Amavasya)</span>
                <span id="lunarPhaseDay" class="text-[11px] text-slate-400">Day 1 of 29.5-day cycle</span>
            </div>

            <!-- Orbital Alignment Explanation -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Orbital Geometry</span>
                <p id="lunarPhaseDesc" class="text-xs text-slate-300 leading-relaxed">
                    The Moon lies directly between the Earth and the Sun. Its illuminated hemisphere faces away into space, rendering the Moon completely invisible from Earth.
                </p>

                <div class="space-y-1.5 text-xs pt-1 border-t border-slate-800">
                    <div class="flex justify-between">
                        <span class="text-slate-400">Visible Illumination:</span>
                        <span id="lunarIllumVal" class="text-emerald-400 font-bold">0% (Completely Dark)</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">Lunar Month Progress:</span>
                        <span id="lunarProgressVal" class="text-cyan-400 font-bold">Beginning of Cycle</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 12: Lunar Calendar Festivals
    "sim_lunar_festivals": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Lunar Calendar Chronometry & Indian Festivals</h3>
                <p class="text-xs text-slate-400">Select a national festival to reveal its corresponding Moon phase and cultural significance.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="selectFestival('diwali')" id="btnFestDiwali" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition">🪔 Diwali</button>
                <button onclick="selectFestival('eid')" id="btnFestEid" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🌙 Eid</button>
                <button onclick="selectFestival('buddha')" id="btnFestBuddha" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🌕 Buddha Poornima</button>
                <button onclick="selectFestival('karva')" id="btnFestKarva" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">✨ Karva Chauth</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Festival Visual Box -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[200px]">
                <div id="festEmojiIcon" class="text-6xl mb-2">🪔</div>
                <span id="festNameHeading" class="text-base font-bold text-amber-300">Diwali (Festival of Lights)</span>
                <span id="festPhaseTag" class="text-xs px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 mt-1">Kartik Amavasya (New Moon)</span>
            </div>

            <!-- Cultural Chronometry Details -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">Calendar Alignment</span>
                <p id="festDescText" class="text-xs text-slate-300 leading-relaxed">
                    Celebrated on the darkest night of the autumn month of Kartik. The complete absence of moonlight is countered by lighting millions of earthen diyas, celebrating light over darkness.
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs">
                    <span class="text-cyan-400 font-bold block">Astronomical Link:</span>
                    <span id="festAstroLink" class="text-slate-300">Nocturnal illumination is zero; maximum contrast for oil lamps and fireworks.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 13: Chandrayaan Lunar Landing
    "sim_chandrayaan_landing": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Chandrayaan-3: Vikram Lander Touchdown (Aug 23, 2023)</h3>
                <p class="text-xs text-slate-400">Fire the liquid retro-rockets to counteract lunar gravity and execute a soft touchdown on 4 shock-absorbing legs.</p>
            </div>
            <button onclick="executeVikramLanding()" id="btnLandVikram" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition flex items-center gap-1.5">
                <span>🚀</span> Fire Retro-Rockets
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Lunar Descent Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[240px]">
                <svg viewBox="0 0 500 240" class="w-full h-auto">
                    <!-- Black Lunar Sky -->
                    <rect x="0" y="0" width="500" height="240" fill="#030712"/>

                    <!-- Distant Earth in sky -->
                    <circle cx="430" cy="40" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                    <text x="430" y="65" fill="#94a3b8" font-size="8" text-anchor="middle">Earth</text>

                    <!-- Lunar South Pole Surface with Craters -->
                    <path d="M0,190 Q120,175 250,195 T500,185 L500,240 L0,240 Z" fill="#475569"/>
                    <circle cx="120" cy="210" r="14" fill="#334155"/>
                    <circle cx="380" cy="215" r="18" fill="#334155"/>
                    <text x="250" y="230" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Shiv Shakti Point (Lunar South Pole)</text>

                    <!-- Vikram Lander Module -->
                    <g id="vikramLanderGroup" transform="translate(225, 30)" class="transition-transform duration-1000">
                        <!-- Gold insulated body -->
                        <rect x="0" y="10" width="50" height="35" rx="3" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
                        <!-- Solar panels on sides -->
                        <polygon points="-8,15 0,15 0,40 -8,40" fill="#2563eb"/>
                        <polygon points="50,15 58,15 58,40 50,40" fill="#2563eb"/>
                        <!-- Top Antenna -->
                        <line x1="25" y1="10" x2="25" y2="0" stroke="#cbd5e1" stroke-width="2"/>
                        <circle cx="25" cy="0" r="3" fill="#cbd5e1"/>
                        <!-- 4 Shock-absorbing landing legs -->
                        <line x1="5" y1="45" x2="-5" y2="65" stroke="#94a3b8" stroke-width="3"/>
                        <circle cx="-5" cy="65" r="4" fill="#64748b"/>
                        <line x1="45" y1="45" x2="55" y2="65" stroke="#94a3b8" stroke-width="3"/>
                        <circle cx="55" cy="65" r="4" fill="#64748b"/>
                        <!-- Retro-rocket plume (dynamic) -->
                        <polygon id="retroRocketPlume" points="20,45 25,68 30,45" fill="#f97316" class="hidden animate-ping"/>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="vikramStatusText">Altitude: 800 m • Descent Velocity: 45 m/s</span>
                    <span class="text-emerald-400 font-bold">National Space Day (August 23)</span>
                </div>
            </div>

            <!-- Touchdown Metrics -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wide">Touchdown Telemetry</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">HISTORIC GLOBAL RANK</span>
                        <span class="font-bold text-yellow-300">1st at Lunar South Pole (4th on Moon)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">BRAKING SYSTEM</span>
                        <span class="font-bold text-cyan-300">4 Throttleable Liquid Engines (No Parachutes)</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 14: Pragyan Surface Exploration
    "sim_pragyan_rover": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Pragyan Rover: Surface Exploration & Laser Spectroscopy</h3>
                <p class="text-xs text-slate-400">Drive the 6-wheeled robotic rover, emboss wheel emblems into regolith, and fire the LIBS laser to detect sulfur.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="drivePragyanRover()" class="px-2.5 py-1 text-xs rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">🚜 Drive Rover</button>
                <button onclick="fireLaserSpectroscope()" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold transition">⚡ Fire LIBS Laser</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Rover Driving SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px]">
                <svg viewBox="0 0 500 230" class="w-full h-auto">
                    <!-- Lunar Ground Surface -->
                    <rect x="0" y="160" width="500" height="70" fill="#475569"/>
                    
                    <!-- Wheel Track Marks with Embossed Emblems -->
                    <g id="pragyanTracksGroup">
                        <line x1="0" y1="185" x2="160" y2="185" stroke="#334155" stroke-width="6" stroke-dasharray="8,6"/>
                        <text x="80" y="180" fill="#94a3b8" font-size="7">ISRO Emblem Tracks</text>
                    </g>

                    <!-- Laser Pulse Line (Dynamic) -->
                    <line id="roverLaserBeam" x1="220" y1="140" x2="350" y2="165" stroke="#ef4444" stroke-width="2" class="hidden"/>
                    <circle id="laserSparkDot" cx="350" cy="165" r="4" fill="#facc15" class="hidden animate-ping"/>

                    <!-- Pragyan Rover Assembly -->
                    <g id="pragyanRoverGroup" transform="translate(160, 120)" class="transition-transform duration-500">
                        <!-- Chassis -->
                        <rect x="0" y="10" width="50" height="22" rx="3" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                        <!-- Solar Panel (Upright) -->
                        <polygon points="10,-5 45,-5 40,10 5,10" fill="#2563eb" stroke="#1d4ed8" stroke-width="1"/>
                        <!-- 6 Rocker-Bogie Wheels -->
                        <circle cx="5" cy="38" r="6" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                        <circle cx="25" cy="38" r="6" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                        <circle cx="45" cy="38" r="6" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                    </g>

                    <!-- Nearby Lunar Rock -->
                    <polygon points="340,175 355,155 375,175" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
                    <text x="360" y="190" fill="#cbd5e1" font-size="8">Basalt Rock</text>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="pragyanStatusText">Pragyan Rover: Stationary • Ready for in-situ soil analysis.</span>
                </div>
            </div>

            <!-- Mineral Analysis Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Chemical Spectroscopy</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">CONFIRMED ELEMENT</span>
                        <span id="spectralResultVal" class="font-bold text-yellow-300 text-sm">Sulfur (S) Detected!</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">OTHER MINERALS</span>
                        <span class="font-semibold text-slate-200">Aluminum, Calcium, Iron, Chromium</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 15: Apparent Solar Motion
    "sim_earth_rotation": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Earth Axial Rotation: The Science of Day & Night</h3>
                <p class="text-xs text-slate-400">Rotate planet Earth counter-clockwise (West to East) to see why the Sun appears to transit East to West.</p>
            </div>
            <button onclick="rotateEarthPlanet()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition">
                🔄 Spin Earth (West ➔ East)
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Rotating Earth & Sunlight -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div class="relative w-40 h-40 flex items-center justify-center">
                    <!-- Stationary Sunbeam Rays from Left -->
                    <div class="absolute -left-12 flex flex-col gap-3">
                        <div class="w-10 h-0.5 bg-yellow-400 animate-pulse"></div>
                        <div class="w-10 h-0.5 bg-yellow-400 animate-pulse"></div>
                        <div class="w-10 h-0.5 bg-yellow-400 animate-pulse"></div>
                    </div>

                    <!-- Earth Globe (Split Day/Night) -->
                    <div id="earthGlobeVisual" class="w-36 h-36 rounded-full border-2 border-cyan-400/80 shadow-2xl overflow-hidden relative transition-transform duration-700 flex">
                        <!-- Day side (Left) -->
                        <div class="w-1/2 h-full bg-blue-500 relative flex items-center justify-center">
                            <span class="text-xs font-bold text-yellow-200">DAY</span>
                        </div>
                        <!-- Night side (Right) -->
                        <div class="w-1/2 h-full bg-slate-950 relative flex items-center justify-center">
                            <span class="text-xs font-bold text-slate-400">NIGHT</span>
                        </div>
                    </div>
                </div>
                <span class="text-[11px] text-cyan-300 font-bold mt-2">1 Full Rotation = 24 Hours</span>
            </div>

            <!-- Train Analogy Explanation -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">The Moving Train Analogy</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    When your train pulls forward out of a station, the trees and platform appear to rush backwards in reverse. Similarly, because Earth spins smoothly from <b>West to East</b>, the stationary Sun appears to move from <b>East to West</b>!
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs">
                    <span class="text-amber-300 font-bold block">Scientific Truth:</span>
                    <span class="text-slate-300">The Sun is stationary at the solar system center; Earth's spin creates the day-night cycle.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 16: Sky Observations Synthesis
    "sim_sky_tracker_matrix": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Master Sky Tracker: Diurnal & Nocturnal Synthesis Matrix</h3>
                <p class="text-xs text-slate-400">Consolidated scientific reference comparing sky color, solar altitude, shadow behavior, and living activities.</p>
            </div>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-slate-300 border-collapse">
                <thead>
                    <tr class="border-b border-slate-800 text-[11px] text-slate-400 uppercase bg-slate-950">
                        <th class="p-2.5">Time Period</th>
                        <th class="p-2.5 text-amber-400">Sky Appearance</th>
                        <th class="p-2.5 text-yellow-400">Solar Position</th>
                        <th class="p-2.5 text-cyan-400">Shadow Length & Direction</th>
                        <th class="p-2.5 text-emerald-400">Nature Activities</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/60">
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-amber-300">🌅 Morning (Dawn)</td>
                        <td class="p-2.5">Golden amber, soft rose</td>
                        <td class="p-2.5">Low on Eastern horizon</td>
                        <td class="p-2.5">Very Long • Pointing West</td>
                        <td class="p-2.5">Roosters crow, sparrows fly, flowers open</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-yellow-300">☀️ Midday (Noon)</td>
                        <td class="p-2.5">Brilliant azure blue</td>
                        <td class="p-2.5">Highest point (Zenith overhead)</td>
                        <td class="p-2.5 font-bold text-emerald-400">Shortest of the Day</td>
                        <td class="p-2.5">Maximum photosynthesis; animals seek shade</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-orange-300">🌇 Evening (Dusk)</td>
                        <td class="p-2.5">Crimson, purple, orange</td>
                        <td class="p-2.5">Low on Western horizon</td>
                        <td class="p-2.5">Very Long • Pointing East</td>
                        <td class="p-2.5">Birds return to roost; daytime blossoms close</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-bold text-indigo-300">🌌 Night (Midnight)</td>
                        <td class="p-2.5">Velvet black with twinkling stars</td>
                        <td class="p-2.5">Below horizon (Opposite side)</td>
                        <td class="p-2.5">No solar shadow (Moonlight shadows)</td>
                        <td class="p-2.5">Owls, bats hunt; nocturnal jasmine blooms</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """
}


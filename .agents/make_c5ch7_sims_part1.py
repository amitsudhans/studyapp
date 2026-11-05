"""
Simulators 1 to 8 for NCERT Class 5 Science Chapter 7: Energy - How Things Work
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMS = {}

# SIM 1: What Energy Does (Energy Transformer Matrix)
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Energy Transformer Matrix</span>
        <p class="text-[11px] text-slate-400">Energy is what makes things move, shine, sound, warm up, and do work!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Central Energy Core -->
            <circle cx="200" cy="120" r="35" fill="#f59e0b" opacity="0.2">
                <animate attributeName="r" values="32;38;32" dur="3s" repeatCount="indefinite"/>
            </circle>
            <circle cx="200" cy="120" r="25" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
            <text x="200" y="117" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">ENERGY</text>
            <text x="200" y="128" text-anchor="middle" fill="#fef3c7" font-size="7">Source Core</text>

            <!-- 4 Output Channels -->
            <!-- Top: Light (Sun/Bulb) -->
            <g id="channelLight" class="cursor-pointer" onclick="activateSim1Mode('light')">
                <line x1="200" y1="95" x2="200" y2="45" stroke="#facc15" stroke-width="2" stroke-dasharray="3,2"/>
                <circle id="nodeLight" cx="200" cy="35" r="18" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
                <text x="200" y="32" text-anchor="middle" font-size="12">💡</text>
                <text x="200" y="44" text-anchor="middle" fill="#fde047" font-size="7" font-weight="bold">Light</text>
            </g>

            <!-- Right: Movement (Cart/Wheel) -->
            <g id="channelMotion" class="cursor-pointer" onclick="activateSim1Mode('motion')">
                <line x1="225" y1="120" x2="310" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,2"/>
                <circle id="nodeMotion" cx="325" cy="120" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="325" y="117" text-anchor="middle" font-size="12">🏃</text>
                <text x="325" y="129" text-anchor="middle" fill="#7dd3fc" font-size="7" font-weight="bold">Motion</text>
            </g>

            <!-- Bottom: Heat/Thermal -->
            <g id="channelHeat" class="cursor-pointer" onclick="activateSim1Mode('heat')">
                <line x1="200" y1="145" x2="200" y2="195" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,2"/>
                <circle id="nodeHeat" cx="200" cy="205" r="18" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
                <text x="200" y="202" text-anchor="middle" font-size="12">🔥</text>
                <text x="200" y="214" text-anchor="middle" fill="#fda4af" font-size="7" font-weight="bold">Heat</text>
            </g>

            <!-- Left: Sound (Acoustic Wave) -->
            <g id="channelSound" class="cursor-pointer" onclick="activateSim1Mode('sound')">
                <line x1="175" y1="120" x2="90" y2="120" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,2"/>
                <circle id="nodeSound" cx="75" cy="120" r="18" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
                <text x="75" y="117" text-anchor="middle" font-size="12">🔔</text>
                <text x="75" y="129" text-anchor="middle" fill="#e9d5ff" font-size="7" font-weight="bold">Sound</text>
            </g>

            <!-- Floating Effect Readout Box -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="130" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text id="sim1EffectTitle" x="65" y="14" text-anchor="middle" fill="#facc15" font-size="8" font-weight="bold">Active Manifestation</text>
                <text id="sim1EffectDesc" x="65" y="28" text-anchor="middle" fill="#cbd5e1" font-size="7">Click any node to test</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5 text-xs">
        <button onclick="activateSim1Mode('motion')" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Motion</button>
        <button onclick="activateSim1Mode('light')" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Light</button>
        <button onclick="activateSim1Mode('sound')" class="py-1.5 px-2 rounded-xl font-bold bg-purple-950/60 hover:bg-purple-900 border border-purple-500/40 text-purple-200">Sound</button>
        <button onclick="activateSim1Mode('heat')" class="py-1.5 px-2 rounded-xl font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200">Heat</button>
    </div>
    <div id="sim1Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Scientific Concept:</span> Energy is invisible, but we see and feel its work whenever objects move, lamps glow, instruments chime, or temperatures rise!
    </div>
</div>
"""

# SIM 2: Balloon Air Rocket Launcher (Activity 1)
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Balloon Air Rocket Launcher</span>
        <p class="text-[11px] text-slate-400">Activity 1: Stored compressed air exhausts backward, rocketing the straw forward!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Taut Guide String spanning across room -->
            <line x1="20" y1="120" x2="380" y2="120" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,2"/>
            <circle cx="20" cy="120" r="4" fill="#64748b"/>
            <circle cx="380" cy="120" r="4" fill="#64748b"/>
            <text x="40" y="110" fill="#64748b" font-size="7">Anchor Point A</text>
            <text x="320" y="110" fill="#64748b" font-size="7">Anchor Point B</text>

            <!-- Balloon Rocket Assembly (Straw + Inflated Balloon) -->
            <g id="balloonRocketAssembly" transform="translate(50, 120)">
                <!-- Drinking Straw threaded on string -->
                <rect x="-25" y="-4" width="50" height="8" rx="2" fill="#facc15" stroke="#ca8a04" stroke-width="1"/>
                <!-- Tape Strips securing balloon -->
                <rect x="-15" y="-7" width="8" height="14" fill="#94a3b8" opacity="0.7"/>
                <rect x="7" y="-7" width="8" height="14" fill="#94a3b8" opacity="0.7"/>

                <!-- Rubber Balloon hanging under straw -->
                <!-- Balloon Body: Expands when inflated -->
                <ellipse id="balloonBody" cx="0" cy="35" rx="35" ry="25" fill="#f43f5e" stroke="#e11d48" stroke-width="1.5"/>
                <!-- Balloon Neck facing Left (Backward exhaust) -->
                <polygon id="balloonNeck" points="-35,32 -48,27 -48,43 -35,38" fill="#f43f5e"/>

                <!-- Backward Air Jet Vectors (Hidden until launch) -->
                <g id="airJetStream" class="opacity-0 transition-opacity duration-200">
                    <line x1="-50" y1="35" x2="-80" y2="35" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,3"/>
                    <line x1="-50" y1="30" x2="-75" y2="25" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
                    <line x1="-50" y1="40" x2="-75" y2="45" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
                    <text x="-95" y="38" fill="#7dd3fc" font-size="7" font-weight="bold">Air Jet ◀</text>
                </g>
                <text x="15" y="5" fill="#fde047" font-size="7" font-weight="bold">Thrust ▶</text>
            </g>

            <!-- Speedometer / Distance Gauge -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="135" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="67" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Rocket Velocity</text>
                <text id="rocketSpeedText" x="67" y="28" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">0 m/s (Rest)</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="inflateBalloon()" id="btnInflate" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>1. Inflate Stored Air</span>
        </button>
        <button onclick="launchBalloonRocket()" id="btnLaunch" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
            <span>2. Release & Launch Rocket!</span>
        </button>
    </div>
    <div id="sim2Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Action and Reaction:</span> The backward exhaust of compressed air pushes the balloon forward with equal momentum, the exact physics of rocket space launches!
    </div>
</div>
"""

# SIM 3: Rubber Band Guitar Frequency & Pitch Lab (Activity 2)
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">Rubber Band Guitar & Acoustic Waves</span>
        <p class="text-[11px] text-slate-400">Activity 2: Pluck stretched bands to observe vibration frequency and acoustic pitch!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-purple-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Shoebox Soundbox Resonator -->
            <rect x="50" y="40" width="300" height="160" rx="10" fill="#3f2e1e" stroke="#78350f" stroke-width="2"/>
            <!-- Sound Hole in Box Center -->
            <ellipse cx="200" cy="120" rx="35" ry="35" fill="#1c1917" stroke="#292524" stroke-width="2"/>
            <text x="200" y="123" text-anchor="middle" fill="#78716c" font-size="8">Resonance Soundhole</text>

            <!-- Bridges / Pencils Supporting Strings -->
            <rect x="90" y="50" width="10" height="140" rx="2" fill="#ca8a04"/>
            <rect x="300" y="50" width="10" height="140" rx="2" fill="#ca8a04"/>

            <!-- String 1: Thin Rubber Band (High Pitch) -->
            <g id="strGroup1" class="cursor-pointer" onclick="pluckString(1)">
                <path id="rubberStr1" d="M 95,75 L 305,75" stroke="#f43f5e" stroke-width="1.8"/>
                <text x="75" y="78" fill="#fda4af" font-size="7">Thin</text>
            </g>

            <!-- String 2: Medium Rubber Band (Medium Pitch) -->
            <g id="strGroup2" class="cursor-pointer" onclick="pluckString(2)">
                <path id="rubberStr2" d="M 95,120 L 305,120" stroke="#facc15" stroke-width="3.5"/>
                <text x="65" y="123" fill="#fef08a" font-size="7">Medium</text>
            </g>

            <!-- String 3: Thick Rubber Band (Deep Bass Pitch) -->
            <g id="strGroup3" class="cursor-pointer" onclick="pluckString(3)">
                <path id="rubberStr3" d="M 95,165 L 305,165" stroke="#38bdf8" stroke-width="6"/>
                <text x="72" y="168" fill="#bae6fd" font-size="7">Thick</text>
            </g>

            <!-- Acoustic Frequency & Wave Meter -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="135" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="67" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Vibration Frequency</text>
                <text id="freqMeterText" x="67" y="28" text-anchor="middle" fill="#c084fc" font-size="10" font-weight="bold">Ready to Pluck</text>
                <text id="pitchDescText" x="67" y="38" text-anchor="middle" fill="#cbd5e1" font-size="7">Click any band below</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="pluckString(1)" class="py-1.5 px-2 rounded-xl font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200">Pluck Thin (High)</button>
        <button onclick="pluckString(2)" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Pluck Medium</button>
        <button onclick="pluckString(3)" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Pluck Thick (Bass)</button>
    </div>
    <div id="sim3Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-purple-400 font-bold">Vibrational Physics:</span> Thinner and tighter bands oscillate at a higher frequency (more vibrations per second), creating higher musical pitch!
    </div>
</div>
"""

# SIM 4: Solar Water Heating & Molecular Thermometer (Activity 3)
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Solar Thermal Water Heating Lab</span>
        <p class="text-[11px] text-slate-400">Activity 3: Compare a bowl in the shade versus radiant solar heating outdoors!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950/40 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Left Side: Shaded Cupboard -->
            <rect x="25" y="45" width="160" height="175" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
            <text x="105" y="65" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="bold">Shaded Cupboard</text>
            <!-- Bowl A -->
            <ellipse cx="105" cy="170" rx="40" ry="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <path d="M 65,170 Q 105,200 145,170 Z" fill="#0369a1"/>
            <text x="105" y="174" text-anchor="middle" fill="#ffffff" font-size="8">Bowl A (Water)</text>
            <!-- Thermometer A -->
            <rect x="98" y="90" width="14" height="65" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
            <rect x="102" y="115" width="6" height="35" rx="2" fill="#38bdf8"/>
            <circle cx="105" cy="155" r="7" fill="#38bdf8"/>
            <text id="tempTextA" x="105" y="82" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">24°C</text>

            <!-- Right Side: Open Sun Terrace -->
            <rect x="215" y="45" width="160" height="175" rx="8" fill="#451a03" stroke="#b45309" stroke-width="1.5" opacity="0.6"/>
            <!-- Radiant Sun Icon with Rays -->
            <circle cx="295" cy="70" r="16" fill="#facc15" stroke="#f59e0b" stroke-width="2"/>
            <line x1="295" y1="90" x2="295" y2="120" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,2"/>
            <line x1="280" y1="85" x2="265" y2="115" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,2"/>
            <line x1="310" y1="85" x2="325" y2="115" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,2"/>
            <text x="295" y="50" text-anchor="middle" fill="#fde047" font-size="8" font-weight="bold">Direct Sunshine</text>
            <!-- Bowl B -->
            <ellipse cx="295" cy="170" rx="40" ry="14" fill="#0284c7" stroke="#fbbf24" stroke-width="1.5"/>
            <path d="M 255,170 Q 295,200 335,170 Z" fill="#0369a1"/>
            <text x="295" y="174" text-anchor="middle" fill="#ffffff" font-size="8">Bowl B (Water)</text>
            <!-- Thermometer B -->
            <rect x="288" y="90" width="14" height="65" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
            <rect id="thermoLiquidB" x="292" y="105" width="6" height="45" rx="2" fill="#ef4444"/>
            <circle cx="295" cy="155" r="7" fill="#ef4444"/>
            <text id="tempTextB" x="295" y="82" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="bold">38°C</text>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Sunshine Exposure Time:</span>
            <span id="sunTimeLabel" class="font-bold text-amber-400">2 Hours (Full Exposure)</span>
        </div>
        <input type="range" id="sunTimeSlider" min="0" max="120" value="120" step="10" oninput="updateSolarHeating(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
    </div>
    <div id="sim4Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Radiant Heat Transfer:</span> Water absorbs infrared radiant energy from sunlight, speeding up molecular vibrations and raising its temperature!
    </div>
</div>
"""

# SIM 5: The Food Battery & Metabolic Energy Gauge
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Human Food Battery & Metabolism Lab</span>
        <p class="text-[11px] text-slate-400">Food provides stored chemical fuel that our body uses and stores like a battery!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-emerald-950/20 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Plate of Food Items on Left -->
            <ellipse cx="110" cy="150" rx="65" ry="30" fill="#334155" stroke="#64748b" stroke-width="2"/>
            <!-- Roti (Carbohydrates) -->
            <circle cx="85" cy="145" r="22" fill="#ca8a04" stroke="#a16207" stroke-width="1.5"/>
            <text x="85" y="148" text-anchor="middle" fill="#fef08a" font-size="7" font-weight="bold">Roti</text>
            <!-- Dal Bowl (Proteins) -->
            <ellipse cx="135" cy="140" rx="18" ry="12" fill="#d97706" stroke="#b45309" stroke-width="1"/>
            <text x="135" y="143" text-anchor="middle" fill="#ffffff" font-size="7" font-weight="bold">Dal</text>
            <!-- Apple / Fruit (Vitamins & Glucose) -->
            <circle cx="115" cy="160" r="10" fill="#ef4444"/>
            <text x="115" y="163" text-anchor="middle" fill="#ffffff" font-size="6">Fruit</text>

            <text x="110" y="195" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="bold">Nutrient Chemical Energy</text>

            <!-- Energy Battery Gauge on Right -->
            <g transform="translate(260, 60)">
                <!-- Battery Shell -->
                <rect x="0" y="10" width="70" height="120" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="2.5"/>
                <!-- Battery Terminal Cap -->
                <rect x="25" y="0" width="20" height="10" rx="2" fill="#94a3b8"/>
                <!-- Battery Liquid Level (Dynamic) -->
                <rect id="batteryFill" x="6" y="25" width="58" height="98" rx="4" fill="#22c55e"/>
                <text id="batteryPctText" x="35" y="75" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">85%</text>
                <text x="35" y="145" text-anchor="middle" fill="#a7f3d0" font-size="8" font-weight="bold">Body Reserve</text>
            </g>

            <!-- Connecting Arrow -->
            <path d="M 175,130 Q 215,110 250,110" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,2"/>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="performActivity('eat')" class="py-1.5 px-2 rounded-xl font-bold bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200">Eat Meal (+Charge)</button>
        <button onclick="performActivity('run')" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Run Sprint (-Fast)</button>
        <button onclick="performActivity('study')" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Study (-Steady)</button>
    </div>
    <div id="sim5Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Metabolic Reserve:</span> Muscles and liver store excess glucose as glycogen, sustaining your heartbeat, lungs, and thinking brain all day and night!
    </div>
</div>
"""

# SIM 6: Combustion Engine Piston Chamber (Fuel Power)
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Combustion Engine Cylinder Lab</span>
        <p class="text-[11px] text-slate-400">Discover how burning fuel creates high-pressure gas that pushes pistons to turn wheels!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Cylinder Block -->
            <rect x="140" y="30" width="120" height="150" fill="#1e293b" stroke="#475569" stroke-width="3"/>
            <!-- Spark Plug at Top -->
            <rect x="193" y="15" width="14" height="20" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
            <polygon id="sparkIgnition" points="200,32 195,42 205,42" fill="#facc15" class="opacity-0 transition-opacity duration-200"/>

            <!-- Piston Assembly (Moves Down on Ignition) -->
            <g id="pistonGroup" transform="translate(150, 70)" class="transition-transform duration-300">
                <!-- Piston Crown -->
                <rect x="0" y="0" width="100" height="35" rx="3" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
                <!-- Connecting Rod -->
                <line x1="50" y1="35" x2="50" y2="105" stroke="#94a3b8" stroke-width="8" stroke-linecap="round"/>
                <!-- Wrist Pin -->
                <circle cx="50" cy="18" r="6" fill="#0f172a"/>
            </g>

            <!-- Expanding Fire Gas in Chamber -->
            <rect id="fireChamber" x="145" y="35" width="110" height="35" fill="#ea580c" opacity="0" class="transition-opacity duration-300"/>

            <!-- Crankshaft Rotating Wheel -->
            <circle cx="200" cy="195" r="28" fill="#334155" stroke="#64748b" stroke-width="3"/>
            <circle id="crankPin" cx="200" cy="175" r="5" fill="#facc15"/>

            <!-- Status Gauge -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="115" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="57" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Engine Cycle</text>
                <text id="engineCycleText" x="57" y="28" text-anchor="middle" fill="#f59e0b" font-size="9" font-weight="bold">Ready to Ignite</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="injectFuel()" id="btnInject" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
            <span>1. Inject Fuel & Air Mist</span>
        </button>
        <button onclick="sparkIgnite()" id="btnIgnite" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>2. Spark & Power Stroke!</span>
        </button>
    </div>
    <div id="sim6Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Fuel Combustion:</span> Burning petrol generates expanding gases that exert thousands of newtons of force, driving pistons to turn vehicle axles!
    </div>
</div>
"""

# SIM 7: Diya Capillary Siphon & Oil Flame Chemistry (Activity 4)
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Diya Capillary Siphon & Flame Chemistry</span>
        <p class="text-[11px] text-slate-400">Activity 4: Oil climbs through microscopic pores by capillary action to feed the flame!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/20 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Clay Diya Dish -->
            <path d="M 60,170 Q 200,225 340,170 Q 300,195 200,200 Q 100,195 60,170 Z" fill="#b45309" stroke="#78350f" stroke-width="2"/>
            <!-- Liquid Oil Reservoir (Adjustable Height) -->
            <ellipse id="diyaOilReservoir" cx="200" cy="175" rx="100" ry="20" fill="#eab308" opacity="0.8"/>
            <text x="200" y="188" text-anchor="middle" fill="#713f12" font-size="8" font-weight="bold">Mustard Oil Fuel</text>

            <!-- Twisted Cotton Wick Emerging from Oil -->
            <path d="M 160,175 Q 190,165 200,130" stroke="#f8fafc" stroke-width="6" stroke-linecap="round" fill="none"/>
            <path d="M 160,175 Q 190,165 200,130" stroke="#fef08a" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.6"/>

            <!-- Microscopic Capillary Inflow Arrows -->
            <g id="capillaryArrows" class="opacity-80">
                <path d="M 175,170 Q 185,160 193,145" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2" fill="none"/>
                <text x="145" y="150" fill="#fde047" font-size="7">Capillary Rise ▲</text>
            </g>

            <!-- Luminous Flame on Wick Tip -->
            <g id="diyaFlame" transform="translate(200, 125)">
                <!-- Outer Yellow Corona -->
                <path d="M 0,0 C -12,-15 -14,-35 0,-50 C 14,-35 12,-15 0,0 Z" fill="#facc15" opacity="0.9"/>
                <!-- Inner Blue/Orange Core -->
                <path d="M 0,0 C -6,-10 -6,-25 0,-35 C 6,-25 6,-10 0,0 Z" fill="#ea580c"/>
                <circle cx="0" cy="-5" r="4" fill="#38bdf8" opacity="0.8"/> <!-- Blue base: complete combustion -->
            </g>

            <!-- Fuel Status Card -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="130" height="38" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="65" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Fuel Reservoir</text>
                <text id="oilStatusText" x="65" y="28" text-anchor="middle" fill="#eab308" font-size="10" font-weight="bold">Oil Level: Full</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleOilLevel('full')" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>Refill Oil (Steady Flame)</span>
        </button>
        <button onclick="toggleOilLevel('empty')" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
            <span>Deplete Oil (Flame Dies)</span>
        </button>
    </div>
    <div id="sim7Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Vapor Combustion:</span> Heat vaporizes rising liquid oil into gas at the tip; it is the oil vapor that burns with oxygen, not the cotton wick itself!
    </div>
</div>
"""

# SIM 8: Universal Electric Circuit & Appliance Hub
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Universal Electric Circuit & Appliance Hub</span>
        <p class="text-[11px] text-slate-400">Electricity easily converts into rotational motion, heating, or bright light!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950/20 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Closed Circuit Copper Loop -->
            <rect x="60" y="50" width="280" height="140" rx="15" fill="none" stroke="#ea580c" stroke-width="3"/>

            <!-- Battery (Power Source on Left) -->
            <g transform="translate(60, 100)">
                <rect x="-15" y="0" width="30" height="40" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
                <rect x="-6" y="-6" width="12" height="6" fill="#94a3b8"/>
                <text x="0" y="24" text-anchor="middle" fill="#facc15" font-size="8" font-weight="bold">BATTERY</text>
            </g>

            <!-- Switch on Bottom Wire -->
            <g id="switchAssembly" class="cursor-pointer" transform="translate(180, 190)" onclick="toggleCircuitSwitch()">
                <circle cx="0" cy="0" r="4" fill="#94a3b8"/>
                <circle cx="40" cy="0" r="4" fill="#94a3b8"/>
                <line id="switchKnife" x1="0" y1="0" x2="35" y2="-18" stroke="#facc15" stroke-width="3" stroke-linecap="round"/>
                <text id="switchText" x="20" y="20" text-anchor="middle" fill="#94a3b8" font-size="8">Switch: OPEN</text>
            </g>

            <!-- Appliance Station at Top Wire -->
            <g id="applianceStation" transform="translate(200, 50)">
                <!-- Appliance Display Box -->
                <circle id="applianceAura" cx="0" cy="0" r="32" fill="#38bdf8" opacity="0.1"/>
                <circle cx="0" cy="0" r="24" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                <text id="applianceIcon" x="0" y="6" text-anchor="middle" font-size="18">🌀</text>
                <text id="applianceName" x="0" y="38" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">Electric Motor</text>
            </g>

            <!-- Electron Flow Dots (Animated when switch closed) -->
            <g id="electronDots" class="opacity-0 transition-opacity duration-300">
                <circle cx="100" cy="50" r="2.5" fill="#38bdf8"/>
                <circle cx="150" cy="50" r="2.5" fill="#38bdf8"/>
                <circle cx="260" cy="50" r="2.5" fill="#38bdf8"/>
                <circle cx="310" cy="50" r="2.5" fill="#38bdf8"/>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="setAppliance('motor')" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Motor (Motion)</button>
        <button onclick="setAppliance('heater')" class="py-1.5 px-2 rounded-xl font-bold bg-rose-950/60 hover:bg-rose-900 border border-rose-500/40 text-rose-200">Coil (Heat)</button>
        <button onclick="setAppliance('bulb')" class="py-1.5 px-2 rounded-xl font-bold bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">LED (Light)</button>
    </div>
    <div id="sim8Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Closed Circuit:</span> Electrons only flow when the circuit loop is continuous. Opening the switch stops current instantly!
    </div>
</div>
"""

print("Sims 1-8 defined successfully")


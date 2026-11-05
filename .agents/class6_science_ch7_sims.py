"""
Interactive HTML/SVG Simulators for Class 6 Science Chapter 7: Temperature and its Measurement
16 Bespoke interactive simulators (Slide 1 to 16).
Zero raw LaTeX. Pure Unicode.
"""

SIMULATORS = {
    1: """
        <!-- Simulator 1: Touch vs Digital Probe Comparator -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🩺</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Touch vs Digital Thermometer Probe</h3>
                        <p class="text-[11px] text-slate-400">Compare subjective hand touch against objective digital measurement</p>
                    </div>
                </div>
                <span id="sim1ModeBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">Objective Tool</span>
            </div>

            <div class="grid grid-cols-2 gap-3">
                <!-- Method A: Hand Touch -->
                <div onclick="testSim1Method('hand')" id="sim1Card-hand" class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 hover:border-amber-500/50 cursor-pointer transition space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-xs text-amber-400 flex items-center space-x-1.5">
                            <span>✋</span><span>Method A: Hand Touch</span>
                        </span>
                        <span class="text-[10px] text-slate-400">Subjective</span>
                    </div>
                    <div class="h-20 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-center p-2">
                        <span id="sim1HandGraphic" class="text-3xl">✋ ➡️ 🧒</span>
                    </div>
                    <div id="sim1HandReading" class="text-[11px] text-slate-300 bg-slate-900 p-2 rounded border border-slate-800">
                        Result: <em>"Feels slightly warm... or maybe normal?" (Uncertain Guess)</em>
                    </div>
                </div>

                <!-- Method B: Digital Clinical Thermometer -->
                <div onclick="testSim1Method('tool')" id="sim1Card-tool" class="p-3.5 rounded-xl bg-slate-800/60 border border-indigo-500/50 hover:border-indigo-400 cursor-pointer transition space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-xs text-indigo-300 flex items-center space-x-1.5">
                            <span>🌡️</span><span>Method B: Digital Thermometer</span>
                        </span>
                        <span class="text-[10px] text-emerald-400 font-bold">Scientific</span>
                    </div>
                    <div class="h-20 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-center p-2">
                        <div class="flex items-center space-x-2">
                            <span class="text-2xl">⚡</span>
                            <div class="font-mono text-xl font-extrabold text-emerald-400 bg-slate-900 px-3 py-1 rounded border border-slate-700" id="sim1ToolDisplay">
                                37.0 °C
                            </div>
                        </div>
                    </div>
                    <div id="sim1ToolReading" class="text-[11px] text-emerald-300 bg-slate-900 p-2 rounded border border-slate-800">
                        Result: <strong>Exact Normal Baseline (37.0°C / 98.6°F)</strong>
                    </div>
                </div>
            </div>

            <div id="sim1Summary" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Click either card above to test. Skin senses heat transfer rate; only calibrated thermometers provide an unambiguous quantitative number.
            </div>
        </div>
    """,

    2: """
        <!-- Simulator 2: The Three-Bowl Paradox (Activity 7.1) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🥣</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Three-Bowl Sensory Paradox (Activity 7.1)</h3>
                        <p class="text-[11px] text-slate-400">Experience how human thermal adaptation tricks the brain</p>
                    </div>
                </div>
                <span id="sim2StateBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">Step 1: Dip Hands in A & C</span>
            </div>

            <!-- Three Bowls Visual Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800/80 p-3 flex items-center justify-around relative">
                <!-- Bowl A: Warm -->
                <div class="flex flex-col items-center">
                    <div id="sim2BowlA" class="w-20 h-20 rounded-full border-2 border-rose-500/60 bg-rose-500/20 flex flex-col items-center justify-center shadow-lg shadow-rose-500/10 transition-all">
                        <span class="text-lg">♨️</span>
                        <span class="text-[10px] text-rose-300 font-bold">Bowl A</span>
                        <span class="text-[9px] text-rose-400 font-mono">Warm (40°C)</span>
                    </div>
                    <span id="sim2LeftHandLabel" class="text-[10px] text-slate-400 mt-1 font-semibold">Left Hand</span>
                </div>

                <!-- Bowl B: Middle Tap Water -->
                <div class="flex flex-col items-center">
                    <div id="sim2BowlB" class="w-24 h-24 rounded-full border-2 border-amber-400/60 bg-amber-500/20 flex flex-col items-center justify-center shadow-lg transition-all">
                        <span class="text-xl">💧</span>
                        <span class="text-[11px] text-amber-300 font-bold">Bowl B</span>
                        <span class="text-[10px] text-slate-300 font-mono">Tap Water (22°C)</span>
                    </div>
                    <span class="text-[10px] text-amber-400 mt-1 font-bold">Test Container</span>
                </div>

                <!-- Bowl C: Ice Cold -->
                <div class="flex flex-col items-center">
                    <div id="sim2BowlC" class="w-20 h-20 rounded-full border-2 border-cyan-500/60 bg-cyan-500/20 flex flex-col items-center justify-center shadow-lg shadow-cyan-500/10 transition-all">
                        <span class="text-lg">🧊</span>
                        <span class="text-[10px] text-cyan-300 font-bold">Bowl C</span>
                        <span class="text-[9px] text-cyan-400 font-mono">Ice Cold (5°C)</span>
                    </div>
                    <span id="sim2RightHandLabel" class="text-[10px] text-slate-400 mt-1 font-semibold">Right Hand</span>
                </div>
            </div>

            <!-- Interactive Action Controls -->
            <div class="grid grid-cols-2 gap-2">
                <button onclick="runSim2Step1()" id="sim2Btn1" class="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-lg transition">
                    1. Dip Hands into Bowl A & Bowl C 👐
                </button>
                <button onclick="runSim2Step2()" id="sim2Btn2" disabled class="p-2.5 rounded-xl bg-slate-800 text-slate-500 font-bold text-xs cursor-not-allowed transition">
                    2. Plunge BOTH Hands into Bowl B ⚡
                </button>
            </div>
            <div id="sim2Feedback" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Click Step 1 to immerse Left Hand in warm water (Bowl A) and Right Hand in ice water (Bowl C).
            </div>
        </div>
    """,

    3: """
        <!-- Simulator 3: Molecular Kinetic Speed & Thermal Motion -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">⚛️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Molecular Kinetic Energy Simulator</h3>
                        <p class="text-[11px] text-slate-400">See how microscopic particle collisions define macroscopic temperature</p>
                    </div>
                </div>
                <span id="sim3TempBadge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">25 °C</span>
            </div>

            <!-- Molecular Motion Chamber -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-2 relative overflow-hidden flex items-center justify-center">
                <svg id="sim3ParticleBox" width="340" height="150" viewBox="0 0 340 150">
                    <!-- Particles rendered by JS -->
                </svg>
            </div>

            <!-- Temperature Slider -->
            <div class="space-y-1.5">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Adjust Temperature:</span>
                    <span id="sim3SliderLabel" class="text-cyan-400 font-mono font-bold">25 °C (Room Temperature)</span>
                </div>
                <input type="range" id="sim3Slider" min="0" max="100" value="25" oninput="updateSim3Temp(this.value)" class="w-full accent-cyan-500 cursor-pointer">
                <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                    <span>0°C (Ice Point)</span>
                    <span>37°C (Human Body)</span>
                    <span>100°C (Boiling Steam)</span>
                </div>
            </div>
            <div id="sim3Insight" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                At higher temperatures, constituent molecules vibrate and collide with higher kinetic velocities.
            </div>
        </div>
    """,

    4: """
        <!-- Simulator 4: Digital Clinical Thermometer Inspector -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔬</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Digital Clinical Thermometer Anatomy</h3>
                        <p class="text-[11px] text-slate-400">Explore the thermistor probe, battery cell, and LCD logic</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Mercury-Free</span>
            </div>

            <!-- Thermometer Diagram Graphic -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex flex-col items-center justify-center relative">
                <svg width="320" height="90" viewBox="0 0 320 90">
                    <!-- Metal Probe Tip -->
                    <rect x="20" y="38" width="30" height="14" rx="2" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5" onclick="inspectSim4Part('tip')" class="cursor-pointer hover:opacity-80"/>
                    <text x="35" y="30" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Thermistor Tip</text>
                    <!-- Body Casing -->
                    <rect x="50" y="30" width="220" height="30" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
                    <!-- LCD Screen -->
                    <rect x="110" y="35" width="70" height="20" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5" onclick="inspectSim4Part('lcd')" class="cursor-pointer"/>
                    <text x="145" y="49" fill="#10b981" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle" id="sim4SvgLcd">37.0 °C</text>
                    <!-- Power Button -->
                    <circle cx="205" cy="45" r="7" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" onclick="inspectSim4Part('btn')" class="cursor-pointer"/>
                    <text x="205" y="48" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">⏻</text>
                    <!-- Battery Cap -->
                    <rect x="270" y="32" width="25" height="26" rx="3" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5" onclick="inspectSim4Part('battery')" class="cursor-pointer"/>
                    <text x="282" y="47" fill="#64748b" font-size="7" font-weight="bold" text-anchor="middle">Bat</text>
                </svg>
                <span class="text-[10px] text-slate-500 italic mt-1">Click any labeled component above to inspect its engineering</span>
            </div>

            <!-- Dynamic Part Details -->
            <div id="sim4Details" class="p-3 rounded-xl bg-slate-800/50 border border-slate-700/60 text-xs space-y-1">
                <span class="font-bold text-cyan-300 block">Probe Tip (Thermistor):</span>
                <p class="text-slate-300 leading-relaxed">Encases a temperature-sensitive resistor whose electrical conductivity shifts predictably with body warmth.</p>
            </div>
        </div>
    """,

    5: """
        <!-- Simulator 5: Non-Contact Infrared Scanner -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">📡</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Infrared Non-Contact Scanner</h3>
                        <p class="text-[11px] text-slate-400">Aim infrared sensor at forehead from safe distance (COVID-19 screening)</p>
                    </div>
                </div>
                <span id="sim5DistBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">Distance: 3 cm</span>
            </div>

            <!-- Scanning Chamber -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-between relative overflow-hidden">
                <!-- Forehead Model -->
                <div class="flex flex-col items-center z-10">
                    <div class="w-16 h-28 rounded-2xl bg-gradient-to-b from-amber-200 to-amber-400 border border-amber-500 flex flex-col items-center justify-center shadow-lg relative">
                        <span class="text-xs font-bold text-slate-900">Forehead</span>
                        <div id="sim5HeatGlow" class="absolute inset-0 bg-red-500/20 rounded-2xl opacity-40 transition-opacity"></div>
                    </div>
                    <span class="text-[10px] text-slate-400 mt-1">Subject</span>
                </div>

                <!-- Infrared Invisible Beam SVG -->
                <div class="flex-1 flex flex-col items-center justify-center relative">
                    <svg id="sim5BeamSvg" width="160" height="40" viewBox="0 0 160 40">
                        <line x1="20" y1="20" x2="140" y2="20" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4" id="sim5BeamLine" opacity="0"/>
                        <polygon points="20,20 30,15 30,25" fill="#f43f5e" id="sim5BeamArrow" opacity="0"/>
                    </svg>
                    <span id="sim5ScanText" class="text-[10px] font-mono font-bold text-rose-400 opacity-0 transition-opacity">IR Thermal Radiation Detected</span>
                </div>

                <!-- Handheld IR Gun -->
                <div class="flex flex-col items-center z-10">
                    <div class="p-2 rounded-xl bg-slate-800 border-2 border-cyan-500 shadow-xl flex flex-col items-center">
                        <span class="text-xl">🔫</span>
                        <div class="p-1 rounded bg-slate-900 font-mono text-xs font-bold text-emerald-400 mt-1 border border-slate-700" id="sim5GunDisplay">
                            --.- °C
                        </div>
                    </div>
                    <span class="text-[10px] text-cyan-300 mt-1 font-bold">IR Scanner</span>
                </div>
            </div>

            <!-- Trigger Button -->
            <button onclick="triggerSim5Scan()" id="sim5ScanBtn" class="w-full py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-bold text-xs shadow-lg transition">
                ⚡ Pull Trigger (Scan Forehead Thermal Radiation)
            </button>
            <div id="sim5Status" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Click the trigger to focus invisible infrared thermal waves onto the thermopile sensor. Reading completes in 0.5 seconds!
            </div>
        </div>
    """,

    6: """
        <!-- Simulator 6: Clinical Measuring Step Simulator (Activity 7.2) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">📋</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Clinical Measurement Protocol (Activity 7.2)</h3>
                        <p class="text-[11px] text-slate-400">Step through the 5 standardized medical steps for fever measurement</p>
                    </div>
                </div>
                <span id="sim6StepBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">Step 1 of 5</span>
            </div>

            <!-- Step Display Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex flex-col items-center justify-center relative overflow-hidden">
                <div id="sim6StepGraphic" class="flex flex-col items-center text-center space-y-2">
                    <!-- Graphic updated by JS -->
                </div>
            </div>

            <!-- Navigation Buttons -->
            <div class="flex items-center justify-between">
                <button onclick="prevSim6Step()" id="sim6PrevBtn" disabled class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-500 text-xs font-bold transition cursor-not-allowed">
                    ← Previous Step
                </button>
                <div class="flex space-x-1.5" id="sim6Dots">
                    <!-- Dots generated by JS -->
                </div>
                <button onclick="nextSim6Step()" id="sim6NextBtn" class="px-4 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition shadow-md">
                    Next Step →
                </button>
            </div>
        </div>
    """,

    7: """
        <!-- Simulator 7: Circadian Body Temperature Rhythm -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">📈</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">24-Hour Circadian Temperature Curve</h3>
                        <p class="text-[11px] text-slate-400">Slide through a full day to observe normal healthy fluctuations</p>
                    </div>
                </div>
                <span id="sim7TimeBadge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">06:00 AM (Dawn)</span>
            </div>

            <!-- Visual Graph & Thermometer Readout -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <svg width="240" height="130" viewBox="0 0 240 130">
                    <!-- Baseline 37.0 Line -->
                    <line x1="20" y1="65" x2="220" y2="65" stroke="#475569" stroke-width="1" stroke-dasharray="3,3"/>
                    <text x="225" y="68" fill="#64748b" font-size="7">37.0°C</text>
                    <!-- Circadian Sine Wave -->
                    <path d="M 20,95 Q 70,110 120,65 T 220,35" fill="none" stroke="#818cf8" stroke-width="2.5"/>
                    <!-- Time Marker Indicator -->
                    <circle id="sim7Point" cx="20" cy="95" r="5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center w-28">
                    <span class="text-[10px] text-slate-400 block">Temperature:</span>
                    <span id="sim7TempDisplay" class="text-xl font-bold font-mono text-emerald-400">36.4 °C</span>
                    <span id="sim7PhaseLabel" class="text-[9px] text-indigo-300 block mt-1">Morning Low</span>
                </div>
            </div>

            <!-- Time Slider -->
            <div class="space-y-1">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Time of Day:</span>
                    <span id="sim7SliderTime" class="text-amber-400 font-bold">06:00 AM</span>
                </div>
                <input type="range" id="sim7Slider" min="0" max="24" value="6" oninput="updateSim7Time(this.value)" class="w-full accent-indigo-500 cursor-pointer">
            </div>
            <div id="sim7Insight" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Body temperature dips to its lowest at dawn (~36.4°C) and peaks in late afternoon (~37.3°C).
            </div>
        </div>
    """,

    8: """
        <!-- Simulator 8: Triple Scale Converter (Celsius, Fahrenheit, Kelvin) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔄</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Triple Scale Synchronizer</h3>
                        <p class="text-[11px] text-slate-400">Celsius (°C), Fahrenheit (°F), and Kelvin (SI: K)</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Real-Time Sync</span>
            </div>

            <!-- Triple Display Gauges -->
            <div class="grid grid-cols-3 gap-2 text-center">
                <div class="p-3 rounded-xl bg-slate-800/80 border border-cyan-500/40">
                    <span class="text-[10px] text-cyan-300 font-bold block mb-1">Celsius (°C)</span>
                    <span id="sim8ValC" class="text-xl font-mono font-extrabold text-white">37.0 °C</span>
                    <span class="text-[9px] text-slate-400 block mt-1">Metric Standard</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-800/80 border border-amber-500/40">
                    <span class="text-[10px] text-amber-300 font-bold block mb-1">Fahrenheit (°F)</span>
                    <span id="sim8ValF" class="text-xl font-mono font-extrabold text-amber-300">98.6 °F</span>
                    <span class="text-[9px] text-slate-400 block mt-1">Customary Scale</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-800/80 border border-emerald-500/40">
                    <span class="text-[10px] text-emerald-300 font-bold block mb-1">Kelvin (K)</span>
                    <span id="sim8ValK" class="text-xl font-mono font-extrabold text-emerald-400">310.15 K</span>
                    <span class="text-[9px] text-slate-400 block mt-1">SI Base Unit</span>
                </div>
            </div>

            <!-- Master Slider -->
            <div class="space-y-1.5">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Adjust Temperature:</span>
                    <span id="sim8PresetLabel" class="text-emerald-400 font-bold">Normal Body Temperature</span>
                </div>
                <input type="range" id="sim8Slider" min="0" max="100" value="37" oninput="updateSim8Scales(this.value)" class="w-full accent-cyan-500 cursor-pointer">
            </div>

            <!-- Quick Preset Buttons -->
            <div class="flex items-center space-x-2">
                <button onclick="setSim8Preset(0)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-bold text-cyan-300 border border-slate-700">0°C (Ice)</button>
                <button onclick="setSim8Preset(37)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-bold text-emerald-300 border border-slate-700">37°C (Body)</button>
                <button onclick="setSim8Preset(100)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-bold text-rose-300 border border-slate-700">100°C (Boiling)</button>
            </div>
        </div>
    """,

    9: """
        <!-- Simulator 9: Laboratory Thermometer Anatomy & Stem Explorer -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🧪</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Laboratory Stem Explorer</h3>
                        <p class="text-[11px] text-slate-400">Inspect the -10°C to 110°C capillary bore and absence of constriction</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20">Wide Range: -10°C to 110°C</span>
            </div>

            <!-- Lab Thermometer Graphic -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-center relative">
                <svg width="320" height="90" viewBox="0 0 320 90">
                    <!-- Thin-walled Bulb -->
                    <circle cx="35" cy="45" r="14" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
                    <text x="35" y="75" fill="#f87171" font-size="7" font-weight="bold" text-anchor="middle">Red Alcohol Bulb</text>
                    <!-- Thick Glass Stem -->
                    <rect x="45" y="38" width="250" height="14" rx="2" fill="rgba(241, 245, 249, 0.1)" stroke="#64748b" stroke-width="1.5"/>
                    <!-- Open Capillary Bore -->
                    <line x1="45" y1="45" x2="280" y2="45" stroke="#334155" stroke-width="2"/>
                    <!-- Liquid Column (up to 60°C) -->
                    <line x1="45" y1="45" x2="190" y2="45" stroke="#ef4444" stroke-width="2" id="sim9LiquidCol"/>
                    <!-- NO Constriction Callout -->
                    <circle cx="55" cy="45" r="8" fill="none" stroke="#eab308" stroke-width="1" stroke-dasharray="2,2"/>
                    <text x="65" y="25" fill="#facc15" font-size="7" font-weight="bold">NO KINK!</text>
                    <!-- Scale Markings -->
                    <text x="45" y="58" fill="#94a3b8" font-size="6">-10</text>
                    <text x="80" y="58" fill="#94a3b8" font-size="6">0</text>
                    <text x="140" y="58" fill="#94a3b8" font-size="6">37</text>
                    <text x="190" y="58" fill="#94a3b8" font-size="6">60</text>
                    <text x="270" y="58" fill="#94a3b8" font-size="6">110°C</text>
                </svg>
            </div>

            <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 rounded bg-slate-800/60 border border-slate-700">
                    <span class="font-bold text-amber-300 block mb-1">Uniform Capillary Bore</span>
                    <span class="text-slate-300 text-[11px]">Straight glass bore allows instantaneous fluid expansion and contraction.</span>
                </div>
                <div class="p-2.5 rounded bg-slate-800/60 border border-slate-700">
                    <span class="font-bold text-rose-300 block mb-1">Direct Immersion Required</span>
                    <span class="text-slate-300 text-[11px]">Because it lacks a constriction, it must be read while immersed in the liquid.</span>
                </div>
            </div>
        </div>
    """,

    10: """
        <!-- Simulator 10: Least Count Calculator (Activities 7.3 & 7.4) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">📐</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Least Count Calculator (Activity 7.4)</h3>
                        <p class="text-[11px] text-slate-400">Calculate the value of one smallest division on different thermometer scales</p>
                    </div>
                </div>
                <span id="sim10LcBadge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Least Count: 1.0 °C</span>
            </div>

            <!-- Zoomed Scale Display -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex flex-col items-center justify-center relative">
                <svg id="sim10SvgScale" width="300" height="90" viewBox="0 0 300 90">
                    <!-- Scale ticks rendered by JS -->
                </svg>
            </div>

            <!-- Division Configuration Buttons -->
            <div class="grid grid-cols-3 gap-2">
                <button onclick="setSim10Divisions(10)" id="sim10Btn-10" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">10 Divisions (1.0°C)</button>
                <button onclick="setSim10Divisions(5)" id="sim10Btn-5" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">5 Divisions (2.0°C)</button>
                <button onclick="setSim10Divisions(50)" id="sim10Btn-50" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">50 Divisions (0.2°C)</button>
            </div>
            <div id="sim10Calculation" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed font-mono">
                Calculation: 10°C span ÷ 10 subdivisions = 1.0 °C per division mark.
            </div>
        </div>
    """,

    11: """
        <!-- Simulator 11: Parallax Alignment Gauge -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">👁️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Parallax Error Eliminator</h3>
                        <p class="text-[11px] text-slate-400">Position the eye at exact 90° horizontal alignment to prevent false readings</p>
                    </div>
                </div>
                <span id="sim11AccuracyBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Position B: 90° Perpendicular</span>
            </div>

            <!-- Alignment Bench -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <!-- Eye View Positions -->
                <div class="flex flex-col space-y-2 text-xs">
                    <button onclick="setSim11Pos('A')" id="sim11Btn-A" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 font-semibold transition text-left">
                        Position A (Looking Down 45°)
                    </button>
                    <button onclick="setSim11Pos('B')" id="sim11Btn-B" class="px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-bold transition text-left shadow-lg">
                        Position B (Direct 90° Eye Level) ✓
                    </button>
                    <button onclick="setSim11Pos('C')" id="sim11Btn-C" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 font-semibold transition text-left">
                        Position C (Looking Up 45°)
                    </button>
                </div>

                <!-- Thermometer Tube Graphic -->
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center w-36">
                    <span class="text-[10px] text-slate-400 block">Apparent Reading:</span>
                    <span id="sim11Reading" class="text-2xl font-mono font-bold text-emerald-400">40.0 °C</span>
                    <span id="sim11Status" class="text-[10px] font-bold text-emerald-400 block mt-1">True Temperature</span>
                </div>
            </div>

            <div id="sim11Explanation" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Looking down from above (Position A) projects the meniscus higher (42°C). Looking up from below (Position C) projects it lower (38°C). Only Position B is true!
            </div>
        </div>
    """,

    12: """
        <!-- Simulator 12: In-Liquid vs Out-of-Liquid Drop -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">⬇️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">The Inviolable Immersion Rule</h3>
                        <p class="text-[11px] text-slate-400">Observe how the open capillary column falls instantly upon removal from liquid</p>
                    </div>
                </div>
                <span id="sim12Badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Immersed in Hot Water</span>
            </div>

            <!-- Immersion Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <!-- Beaker Graphic -->
                <div class="flex flex-col items-center">
                    <div class="w-24 h-28 border-2 border-slate-600 rounded-b-xl bg-rose-500/20 flex flex-col justify-end p-2 relative overflow-hidden">
                        <div class="h-16 bg-rose-500/30 rounded-b-lg border-t border-rose-400 flex items-center justify-center text-[9px] font-bold text-rose-300">
                            Hot Water (80°C)
                        </div>
                    </div>
                </div>

                <!-- Thermometer Animated Position -->
                <div id="sim12ThermoUnit" class="flex flex-col items-center transition-all duration-700">
                    <div class="w-4 h-32 bg-slate-200 rounded-t border border-slate-400 relative overflow-hidden flex flex-col justify-end">
                        <div id="sim12Column" class="w-full bg-red-600 transition-all duration-700" style="height: 75%;"></div>
                    </div>
                    <div class="w-8 h-8 rounded-full bg-red-600 border border-red-700 -mt-2"></div>
                </div>

                <!-- Temperature Readout -->
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center w-32">
                    <span class="text-[10px] text-slate-400 block">Current Reading:</span>
                    <span id="sim12Readout" class="text-2xl font-mono font-bold text-rose-400">80.0 °C</span>
                    <span id="sim12State" class="text-[10px] text-emerald-400 font-bold block mt-1">In-Liquid Reading</span>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="grid grid-cols-2 gap-2">
                <button onclick="liftSim12Thermometer()" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-lg transition">
                    🚫 Lift Thermometer Out into Air!
                </button>
                <button onclick="immerseSim12Thermometer()" class="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-lg transition">
                    ✓ Re-Immerse in Hot Water
                </button>
            </div>
        </div>
    """,

    13: """
        <!-- Simulator 13: Ice Melting Phase Plateau (Activity 7.5) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🧊</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">0°C Melting Ice Plateau (Activity 7.5)</h3>
                        <p class="text-[11px] text-slate-400">Watch temperature lock at 0°C as latent heat melts the ice crystals</p>
                    </div>
                </div>
                <span id="sim13PhaseBadge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">0.0 °C (Melting Plateau)</span>
            </div>

            <!-- Thermal Chamber & Graph -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <svg width="220" height="120" viewBox="0 0 220 120">
                    <!-- Graph Axes -->
                    <line x1="20" y1="100" x2="200" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <line x1="20" y1="100" x2="20" y2="20" stroke="#475569" stroke-width="1.5"/>
                    <text x="180" y="112" fill="#64748b" font-size="7">Time (min)</text>
                    <text x="5" y="25" fill="#64748b" font-size="7">Temp (°C)</text>
                    <!-- Latent Plateau Line -->
                    <line x1="20" y1="80" x2="130" y2="80" stroke="#38bdf8" stroke-width="3" id="sim13PlateauLine"/>
                    <text x="75" y="74" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Flat 0.0°C Plateau</text>
                    <!-- Post-Melt Warming Line -->
                    <line x1="130" y1="80" x2="190" y2="40" stroke="#818cf8" stroke-width="2" stroke-dasharray="3,3" id="sim13WarmLine" opacity="0.3"/>
                    <text x="165" y="45" fill="#818cf8" font-size="7">Liquid Warms</text>
                </svg>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center w-28">
                    <span class="text-[10px] text-slate-400 block">Current Temp:</span>
                    <span class="text-2xl font-mono font-bold text-cyan-400" id="sim13Temp">0.0 °C</span>
                    <span class="text-[9px] text-slate-400 block mt-1" id="sim13StateLabel">Ice Slush</span>
                </div>
            </div>

            <!-- Heat Supply Toggle -->
            <button onclick="toggleSim13Heating()" id="sim13HeatBtn" class="w-full py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-lg transition">
                🔥 Apply Continuous Room Heat
            </button>
            <div id="sim13Text" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Heat from the room is absorbed as latent heat of fusion. Temperature remains locked at 0°C until the final ice crystal liquefies.
            </div>
        </div>
    """,

    14: """
        <!-- Simulator 14: Boiling Water Phase Plateau (Activity 7.6) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">♨️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">100°C Boiling Water Plateau (Activity 7.6)</h3>
                        <p class="text-[11px] text-slate-400">Open beaker boiling temperature flatlines at 100°C</p>
                    </div>
                </div>
                <span id="sim14Badge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">100.0 °C (Boiling Flatline)</span>
            </div>

            <!-- Boiling Beaker & Graph -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <svg width="220" height="120" viewBox="0 0 220 120">
                    <line x1="20" y1="100" x2="200" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <line x1="20" y1="100" x2="20" y2="20" stroke="#475569" stroke-width="1.5"/>
                    <text x="180" y="112" fill="#64748b" font-size="7">Time</text>
                    <text x="5" y="25" fill="#64748b" font-size="7">100°C</text>
                    <!-- Warming up line -->
                    <line x1="20" y1="90" x2="90" y2="35" stroke="#f59e0b" stroke-width="2"/>
                    <!-- 100°C Plateau -->
                    <line x1="90" y1="35" x2="200" y2="35" stroke="#ef4444" stroke-width="3"/>
                    <text x="145" y="30" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Locked at 100.0°C</text>
                </svg>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center w-28">
                    <span class="text-[10px] text-slate-400 block">Water Temp:</span>
                    <span class="text-2xl font-mono font-bold text-rose-400" id="sim14Temp">100.0 °C</span>
                    <span class="text-[9px] text-amber-300 font-bold block mt-1 animate-pulse">Vigorous Steam!</span>
                </div>
            </div>

            <div class="flex items-center space-x-2">
                <button onclick="boostSim14Flame()" id="sim14BoostBtn" class="flex-1 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-lg transition">
                    🔥 Turn Gas Flame to Maximum!
                </button>
                <button onclick="resetSim14()" class="px-3 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs">Reset</button>
            </div>
            <div id="sim14Insight" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Even with maximum burner power, open water cannot exceed 100°C. Extra heat becomes latent heat of vaporization.
            </div>
        </div>
    """,

    15: """
        <!-- Simulator 15: Maximum-Minimum Weather Station -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🌤️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Maximum-Minimum Weather Station</h3>
                        <p class="text-[11px] text-slate-400">Six's U-tube thermometer tracking 24-hour daily extremes</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">Diurnal Cycle</span>
            </div>

            <!-- U-Tube Graphic -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <svg width="240" height="130" viewBox="0 0 240 130">
                    <!-- U-Tube Stem -->
                    <path d="M 80,20 L 80,90 A 20,20 0 0,0 120,90 L 120,20" fill="none" stroke="#475569" stroke-width="8"/>
                    <!-- Liquid Mercury thread -->
                    <path d="M 80,60 L 80,90 A 20,20 0 0,0 120,90 L 120,45" fill="none" stroke="#cbd5e1" stroke-width="4"/>
                    <!-- Left Dumbbell Index (Minimum) -->
                    <rect x="78" y="55" width="4" height="6" fill="#38bdf8"/>
                    <text x="50" y="58" fill="#38bdf8" font-size="8" font-weight="bold">Min: 14°C</text>
                    <!-- Right Dumbbell Index (Maximum) -->
                    <rect x="118" y="40" width="4" height="6" fill="#f43f5e"/>
                    <text x="145" y="44" fill="#f43f5e" font-size="8" font-weight="bold">Max: 32°C</text>
                </svg>
                <div class="space-y-2 text-xs w-32">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-[9px] text-cyan-400 block font-bold">Daily Minimum:</span>
                        <span class="font-mono text-sm font-bold text-white">14.2 °C (05:30 AM)</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-[9px] text-rose-400 block font-bold">Daily Maximum:</span>
                        <span class="font-mono text-sm font-bold text-white">32.6 °C (02:45 PM)</span>
                    </div>
                </div>
            </div>

            <div class="p-2.5 rounded-lg bg-slate-800/50 border border-slate-700/60 text-xs text-slate-300">
                Steel index markers are pushed by expanding mercury and remain locked at the highest and lowest daily points until reset with a magnet.
            </div>
        </div>
    """,

    16: """
        <!-- Simulator 16: Anna Mani Meteorological Instrumentation Station -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🎈</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Anna Mani Meteorological Station</h3>
                        <p class="text-[11px] text-slate-400">Explore instruments engineered by the Weather Woman of India</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">National Pioneer</span>
            </div>

            <!-- Instrument Selector -->
            <div class="grid grid-cols-3 gap-2">
                <button onclick="selectSim16Tool('ozone')" id="sim16Btn-ozone" class="p-2 rounded-xl bg-indigo-600 text-white font-bold text-xs">Ozonesonde</button>
                <button onclick="selectSim16Tool('solar')" id="sim16Btn-solar" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">Pyranometer ☀️</button>
                <button onclick="selectSim16Tool('wind')" id="sim16Btn-wind" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">Wind Anemometer 💨</button>
            </div>

            <!-- Display Area -->
            <div id="sim16Display" class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <!-- Rendered by JS -->
            </div>

            <div id="sim16Notes" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                The Indian Ozonesonde was designed by Anna Mani at IMD Pune to measure vertical ozone distribution up to 35 km altitude.
            </div>
        </div>
    """
}


# make_c4s_ch6_sims_part2.py
# Generates interactive simulators 9 to 16 for Chapter 6: Happy and Healthy Living

simulators_part2 = {}

# SIM 9: Heart Rate & Stamina Meter
simulators_part2["sim-9"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-red-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-red-300">Cardiovascular Stamina & Play Meter</h4>
            </div>
            <span class="text-xs bg-red-500/20 text-red-300 px-2.5 py-1 rounded-full font-medium border border-red-500/30">Aerobic Biomechanics</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.selectActivity('sitting')" class="activity-btn active p-2.5 rounded-xl border border-red-500/50 bg-red-950/40 hover:bg-red-900/50 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🪑</span>
                <div>
                    <div class="text-xs font-bold text-white">Sitting (Rest)</div>
                    <div class="text-[10px] text-slate-400">Basal metabolic rate</div>
                </div>
            </button>
            <button onclick="window.selectActivity('walking')" class="activity-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🚶</span>
                <div>
                    <div class="text-xs font-bold text-white">Brisk Walking</div>
                    <div class="text-[10px] text-emerald-400">Light aerobic activity</div>
                </div>
            </button>
            <button onclick="window.selectActivity('skipping')" class="activity-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🏃</span>
                <div>
                    <div class="text-xs font-bold text-white">Skipping Rope</div>
                    <div class="text-[10px] text-amber-400">Moderate cardio burn</div>
                </div>
            </button>
            <button onclick="window.selectActivity('khokho')" class="activity-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">⚡</span>
                <div>
                    <div class="text-xs font-bold text-white">Kho-Kho Sprint</div>
                    <div class="text-[10px] text-rose-400">High-intensity play</div>
                </div>
            </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Heart Pulse Rate</span>
                <div class="text-xl font-extrabold text-red-400 flex items-center gap-2">
                    <span class="animate-ping text-xs">💓</span>
                    <span id="actBpm">75 BPM</span>
                </div>
                <span class="text-[10px] text-slate-400 block" id="actHeartDesc">Calm steady resting rhythm</span>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Lung Oxygen Intake</span>
                <div class="text-xl font-extrabold text-sky-400 flex items-center gap-2">
                    <span>🫁</span>
                    <span id="actO2">14 Breaths/min</span>
                </div>
                <span class="text-[10px] text-slate-400 block" id="actLungDesc">Standard tidal volume</span>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Brain Endorphin Level</span>
                <div class="text-xl font-extrabold text-amber-300 flex items-center gap-2">
                    <span>🧠</span>
                    <span id="actEndorphin">Baseline 20%</span>
                </div>
                <span class="text-[10px] text-slate-400 block" id="actBrainDesc">Normal neural state</span>
            </div>
        </div>

        <div class="flex items-center justify-between text-xs text-slate-300 bg-slate-950 p-3 rounded-lg border border-slate-800">
            <span>WHO & NEP Standard: <strong>Minimum 60 minutes of vigorous daily physical play</strong> for growing children!</span>
            <span class="text-emerald-400 font-semibold">Builds Strong Bones & Happiness</span>
        </div>
    </div>
"""

# SIM 10: Spinal Alignment & Yoga Posture Chamber
simulators_part2["sim-10"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Spinal Alignment & Yoga Asana Chamber</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Postural Ergonomics</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.selectAsana('vrikshasana')" class="asana-btn active p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 hover:bg-emerald-900/50 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🧘</span>
                <div>
                    <div class="text-xs font-bold text-white">Vrikshasana</div>
                    <div class="text-[10px] text-emerald-300">Tree Pose (Balance)</div>
                </div>
            </button>
            <button onclick="window.selectAsana('bhujangasana')" class="asana-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🐍</span>
                <div>
                    <div class="text-xs font-bold text-white">Bhujangasana</div>
                    <div class="text-[10px] text-amber-300">Cobra Pose (Spine)</div>
                </div>
            </button>
            <button onclick="window.selectAsana('tadasana')" class="asana-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">⛰️</span>
                <div>
                    <div class="text-xs font-bold text-white">Tadasana</div>
                    <div class="text-[10px] text-cyan-300">Mountain Pose (Erect)</div>
                </div>
            </button>
            <button onclick="window.selectAsana('balasana')" class="asana-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🌱</span>
                <div>
                    <div class="text-xs font-bold text-white">Balasana</div>
                    <div class="text-[10px] text-purple-300">Child Pose (Relax)</div>
                </div>
            </button>
        </div>

        <div id="asanaDetails" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
            <div class="w-20 h-20 rounded-2xl bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-center text-4xl shrink-0" id="asanaIcon">
                🧘
            </div>
            <div class="flex-1 space-y-1.5 text-center sm:text-left">
                <div class="flex items-center gap-2 justify-center sm:justify-start">
                    <span id="asanaBadge" class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950 px-2 py-0.5 rounded">Balance & Stability</span>
                    <h5 id="asanaName" class="text-sm font-bold text-white">Vrikshasana (Tree Pose)</h5>
                </div>
                <p id="asanaDesc" class="text-xs text-slate-300 leading-relaxed">
                    Stand firmly on one foot, place the sole of the opposite foot on the inner thigh, and join palms in Namaste overhead. Trains cerebellar balance, strengthens ankles, and promotes single-pointed mental concentration.
                </p>
                <div class="flex flex-wrap gap-2 pt-1 justify-center sm:justify-start text-[11px]">
                    <span class="bg-slate-800 text-slate-300 px-2 py-0.5 rounded" id="asanaSpine">Spine Effect: Aligns 33 vertebrae vertically</span>
                    <span class="bg-emerald-900/40 text-emerald-300 px-2 py-0.5 rounded border border-emerald-700/50" id="asanaCorrection">Counteracts: Forward desk slouching and poor posture</span>
                </div>
            </div>
        </div>
    </div>
"""

# SIM 11: Brain Glymphatic Cleansing Simulator
simulators_part2["sim-11"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-violet-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-violet-300">Brain Glymphatic Rinse & Memory Lab</h4>
            </div>
            <span class="text-xs bg-violet-500/20 text-violet-300 px-2.5 py-1 rounded-full font-medium border border-violet-500/30">Neurobiology of Sleep</span>
        </div>

        <div class="flex items-center justify-center gap-3">
            <button onclick="window.setSleepState('wake')" class="sleep-toggle-btn p-3 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 text-xs font-bold flex items-center gap-2 text-slate-300">
                <span>☀️</span> Daytime Awake (Learning & Toxin Buildup)
            </button>
            <button onclick="window.setSleepState('sleep')" class="sleep-toggle-btn active p-3 rounded-xl border border-violet-500/50 bg-violet-950/40 hover:bg-violet-900/50 text-xs font-bold flex items-center gap-2 text-white">
                <span>🌙</span> Deep Sleep (Glymphatic Wash & Memory Save)
            </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Fluid Wash Flow</span>
                <div class="text-sm font-bold text-sky-400 flex items-center gap-2" id="glymphFlow">
                    <span>🌊</span> +60% Cerebrospinal Surge
                </div>
                <p class="text-[11px] text-slate-400" id="glymphFlowDesc">Brain interstitial space expands, allowing fluid to flush out metabolic waste.</p>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Memory Processing</span>
                <div class="text-sm font-bold text-violet-300 flex items-center gap-2" id="glymphMemory">
                    <span>💾</span> Long-Term Consolidation
                </div>
                <p class="text-[11px] text-slate-400" id="glymphMemoryDesc">Hippocampus transfers school facts into stable cerebral cortex storage.</p>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Pituitary Growth Hormone</span>
                <div class="text-sm font-bold text-emerald-400 flex items-center gap-2" id="glymphHormone">
                    <span>📈</span> Peak Secretion Active
                </div>
                <p class="text-[11px] text-slate-400" id="glymphHormoneDesc">Stimulates bone lengthening, cell regeneration, and muscle tissue repair.</p>
            </div>
        </div>

        <div class="bg-violet-950/30 rounded-lg p-2.5 border border-violet-800/40 flex items-center justify-between text-xs">
            <span class="text-slate-300">Target for 9-10 year olds: <strong>9 to 10 hours</strong> of uninterrupted nighttime slumber.</span>
            <span class="text-violet-300 font-semibold">Sleep Recharges Body & Mind</span>
        </div>
    </div>
"""

# SIM 12: Circadian Melatonin Clock Cycle
simulators_part2["sim-12"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-indigo-300">Circadian Melatonin Clock & Screen Hygiene</h4>
            </div>
            <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-full font-medium border border-indigo-500/30">24-Hour Rhythm</span>
        </div>

        <div class="space-y-2">
            <div class="flex items-center justify-between">
                <label for="circadianSlider" class="text-xs font-bold text-slate-300 flex items-center gap-2">
                    <span>🕒 Time of Day:</span>
                    <span id="circadianTimeVal" class="text-indigo-300 text-base font-extrabold bg-slate-800 px-2.5 py-0.5 rounded border border-slate-700">9:00 PM (Bedtime Preparation)</span>
                </label>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-400">Blue Screen Exposure:</span>
                    <button id="screenToggleBtn" onclick="window.toggleBlueScreen()" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-700">Screen OFF (Healthy)</button>
                </div>
            </div>
            <input type="range" id="circadianSlider" min="0" max="23" value="21" oninput="window.updateCircadianSim(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500">
            <div class="flex justify-between text-[10px] text-slate-500">
                <span>12 AM (Midnight)</span>
                <span>6 AM (Sunrise)</span>
                <span>12 PM (Noon)</span>
                <span>6 PM (Sunset)</span>
                <span>11 PM (Night)</span>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 bg-slate-950/80 rounded-xl p-3 border border-slate-800">
            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Natural Melatonin Level</span>
                <div class="text-sm font-bold text-indigo-300 flex items-center gap-2" id="circadianMelatonin">
                    <span>🧪</span> High (65 pg/mL)
                </div>
                <p class="text-[11px] text-slate-400" id="circadianMelatoninDesc">Pineal gland detects darkness and signals drowsiness.</p>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Body Core Temperature</span>
                <div class="text-sm font-bold text-cyan-300 flex items-center gap-2" id="circadianTemp">
                    <span>🌡️</span> 36.4°C (Cooling)
                </div>
                <p class="text-[11px] text-slate-400" id="circadianTempDesc">Blood flows to extremities, cooling the core for deep rest.</p>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Alertness & Readiness</span>
                <div class="text-sm font-bold text-amber-300 flex items-center gap-2" id="circadianAlert">
                    <span>😴</span> Ready for Slumber
                </div>
                <p class="text-[11px] text-slate-400" id="circadianAlertDesc">Cortisol is lowest; brainwaves transition into relaxing alpha states.</p>
            </div>
        </div>
    </div>
"""

# SIM 13: Safe vs Unsafe Boundary Radar
simulators_part2["sim-13"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-teal-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-teal-300">Safe vs Unsafe Boundary Radar</h4>
            </div>
            <span class="text-xs bg-teal-500/20 text-teal-300 px-2.5 py-1 rounded-full font-medium border border-teal-500/30">Body Boundary Evaluation</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
            <button onclick="window.evaluateTouchScenario(0)" class="touch-scene-btn active p-2.5 rounded-xl border border-teal-500/50 bg-teal-950/40 text-left hover:bg-teal-900/50 transition-all">
                <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>🤗</span> Loving Parent Hug
                </div>
                <div class="text-[10px] text-teal-300">Comforting & warm</div>
            </button>
            <button onclick="window.evaluateTouchScenario(1)" class="touch-scene-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 text-left hover:bg-slate-800 transition-all">
                <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>✋</span> Sports High-Five
                </div>
                <div class="text-[10px] text-emerald-300">Open celebratory gesture</div>
            </button>
            <button onclick="window.evaluateTouchScenario(2)" class="touch-scene-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 text-left hover:bg-slate-800 transition-all">
                <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>⚠️</span> Secret Uncomfortable Touch
                </div>
                <div class="text-[10px] text-rose-400">Boundary violation</div>
            </button>
        </div>

        <div id="touchRadarCard" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <span id="touchRadarIcon" class="text-3xl">🛡️</span>
                    <div>
                        <h5 id="touchRadarTitle" class="text-sm font-bold text-teal-300">SAFE TOUCH: Warm, Open & Caring</h5>
                        <span id="touchRadarType" class="text-[11px] text-slate-400">Consensual, respectful interaction from family</span>
                    </div>
                </div>
                <span id="touchRadarBadge" class="text-xs font-extrabold px-2.5 py-1 rounded bg-teal-950 text-teal-300 border border-teal-700">SAFE & HEALTHY</span>
            </div>
            <p id="touchRadarDesc" class="text-xs text-slate-300 leading-relaxed">
                A warm hug from parents or caregivers makes a child feel loved, secure, and respected. It is done openly without secrecy or fear.
            </p>
            <div class="flex items-center justify-between pt-1 text-[11px]">
                <span class="text-slate-400" id="touchRadarAction">Action: Enjoy and reciprocate affection with family members</span>
                <span class="text-teal-400 font-medium" id="touchRadarGut">Internal Gut Check: Feels calm and happy</span>
            </div>
        </div>
    </div>
"""

# SIM 14: Swimsuit Boundary Defense Shield
simulators_part2["sim-14"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Universal Swimsuit Boundary Shield</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Personal Body Safety</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center space-y-3">
                <div class="relative w-36 h-48 bg-slate-900 rounded-2xl border-2 border-slate-700 flex flex-col items-center justify-around p-2">
                    <button onclick="window.inspectZone('mouth')" class="zone-btn w-12 py-1 rounded bg-amber-500/30 border border-amber-400 text-[10px] font-bold text-amber-200 hover:bg-amber-500/50 transition-all">Mouth 👄</button>
                    <button onclick="window.inspectZone('chest')" class="zone-btn w-24 py-1.5 rounded bg-cyan-500/30 border border-cyan-400 text-[10px] font-bold text-cyan-200 hover:bg-cyan-500/50 transition-all">Chest Zone 🎽</button>
                    <button onclick="window.inspectZone('groin')" class="zone-btn w-20 py-1.5 rounded bg-cyan-500/30 border border-cyan-400 text-[10px] font-bold text-cyan-200 hover:bg-cyan-500/50 transition-all">Groin Zone 🩳</button>
                    <button onclick="window.inspectZone('buttocks')" class="zone-btn w-20 py-1 rounded bg-cyan-500/30 border border-cyan-400 text-[10px] font-bold text-cyan-200 hover:bg-cyan-500/50 transition-all">Back Zone 🛡️</button>
                </div>
                <span class="text-[11px] text-slate-400 text-center">Click any zone to inspect safety rules</span>
            </div>

            <div class="space-y-3 flex flex-col justify-between">
                <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="text-2xl" id="zoneIcon">🎽</span>
                        <div>
                            <h5 class="text-sm font-bold text-cyan-300" id="zoneTitle">Chest & Torso Zone</h5>
                            <span class="text-[10px] text-slate-400">Swimsuit Protected Area</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed" id="zoneRule">
                        Covered completely by swimsuits. No one has any right to touch this area, look at it, photograph it, or ask you to touch theirs.
                    </p>
                    <div class="bg-amber-950/40 text-amber-300 p-2 rounded border border-amber-800/40 text-[11px]" id="zoneDoctorRule">
                        Doctor Checkup Rule: Allowed ONLY for medical reasons when a parent or guardian is standing right beside you inside the room!
                    </div>
                </div>

                <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800 text-[11px] text-slate-300 flex items-center justify-between">
                    <span>Golden Rule: <strong>Your body belongs strictly to YOU!</strong></span>
                    <span class="text-rose-400 font-semibold">Never Keep Secrets About Touches</span>
                </div>
            </div>
        </div>
    </div>
"""

# SIM 15: Three-Step Safety Action Hero
simulators_part2["sim-15"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-rose-300">Three-Step Safety Action Hero: NO - RUN - TELL</h4>
            </div>
            <span class="text-xs bg-rose-500/20 text-rose-300 px-2.5 py-1 rounded-full font-medium border border-rose-500/30">Action Protocol</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <button onclick="window.selectActionStep(1)" class="action-step-btn active p-3 rounded-xl border border-rose-500/50 bg-rose-950/40 hover:bg-rose-900/50 transition-all text-left space-y-1">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-rose-400">STEP 1</span>
                    <span class="text-2xl">🗣️</span>
                </div>
                <div class="text-sm font-bold text-white">SAY "NO!"</div>
                <p class="text-[11px] text-slate-300">Speak in a loud, firm, commanding voice.</p>
            </button>

            <button onclick="window.selectActionStep(2)" class="action-step-btn p-3 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left space-y-1">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-amber-400">STEP 2</span>
                    <span class="text-2xl">🏃</span>
                </div>
                <div class="text-sm font-bold text-white">RUN AWAY</div>
                <p class="text-[11px] text-slate-300">Dash to a bright, crowded, safe space.</p>
            </button>

            <button onclick="window.selectActionStep(3)" class="action-step-btn p-3 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left space-y-1">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-emerald-400">STEP 3</span>
                    <span class="text-2xl">📢</span>
                </div>
                <div class="text-sm font-bold text-white">TELL AN ADULT</div>
                <p class="text-[11px] text-slate-300">Confide in your trusted Safety Circle.</p>
            </button>
        </div>

        <div id="actionStepDetail" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center gap-2">
                <span id="actionStepIcon" class="text-3xl">🗣️</span>
                <div>
                    <h5 id="actionStepTitle" class="text-sm font-bold text-rose-300">Step 1: Use Your Bold Voice — Say "NO!"</h5>
                    <span id="actionStepSubtitle" class="text-[11px] text-slate-400">Stand tall, look them directly in the eye</span>
                </div>
            </div>
            <p id="actionStepDesc" class="text-xs text-slate-300 leading-relaxed">
                Say clearly and loudly: "NO! Stop this! I do not like this!" You never have to be polite to anyone who is crossing your body boundaries.
            </p>
            <div class="flex flex-wrap gap-2 pt-1 text-[11px]">
                <span class="bg-slate-800 text-slate-300 px-2.5 py-1 rounded" id="actionStepFact">Voice power stops unwanted behavior in its tracks</span>
                <span class="bg-rose-950/60 text-rose-300 px-2.5 py-1 rounded border border-rose-800/50">Core Truth: You are NEVER at fault</span>
            </div>
        </div>
    </div>
"""

# SIM 16: 24-Hour Holistic Health Planner
simulators_part2["sim-16"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-teal-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-teal-300">24-Hour Holistic Health Daily Planner</h4>
            </div>
            <span class="text-xs bg-teal-500/20 text-teal-300 px-2.5 py-1 rounded-full font-medium border border-teal-500/30">Integrated Routine</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.selectRoutinePhase('morning')" class="routine-btn active p-2.5 rounded-xl border border-teal-500/50 bg-teal-950/40 hover:bg-teal-900/50 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🌅</span>
                <div>
                    <div class="text-xs font-bold text-white">Morning (6-8 AM)</div>
                    <div class="text-[10px] text-amber-300">Hydration & Yoga</div>
                </div>
            </button>
            <button onclick="window.selectRoutinePhase('school')" class="routine-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🎒</span>
                <div>
                    <div class="text-xs font-bold text-white">School (8 AM-3 PM)</div>
                    <div class="text-[10px] text-cyan-300">Learning & Mindful Lunch</div>
                </div>
            </button>
            <button onclick="window.selectRoutinePhase('afternoon')" class="routine-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">⚽</span>
                <div>
                    <div class="text-xs font-bold text-white">Play (4-6 PM)</div>
                    <div class="text-[10px] text-emerald-300">60m Active Sports</div>
                </div>
            </button>
            <button onclick="window.selectRoutinePhase('night')" class="routine-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🌙</span>
                <div>
                    <div class="text-xs font-bold text-white">Night (8 PM-6 AM)</div>
                    <div class="text-[10px] text-indigo-300">Screens Off & 9-10h Sleep</div>
                </div>
            </button>
        </div>

        <div id="routineCard" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center gap-2">
                <span id="routineIcon" class="text-3xl">🌅</span>
                <div>
                    <h5 id="routineTitle" class="text-sm font-bold text-teal-300">Morning Awakening: 6:00 AM - 8:00 AM</h5>
                    <span id="routineSubtitle" class="text-[11px] text-slate-400">Foundation for physical energy & mental clarity</span>
                </div>
            </div>
            <p id="routineDesc" class="text-xs text-slate-300 leading-relaxed">
                Wake up at a consistent time. Drink a glass of warm water, stretch the spine with Tadasana and Vrikshasana, and enjoy a nutritious breakfast of millets and fruits for sustained glucose energy.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-1 text-[11px]">
                <div class="bg-slate-900 p-2 rounded border border-slate-800" id="routineGoal1">💧 Hydration: Warm water kickstarts metabolism</div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800" id="routineGoal2">🧘 Movement: 10 mins gentle spinal alignment</div>
                <div class="bg-slate-900 p-2 rounded border border-slate-800" id="routineGoal3">🥗 Fuel: Whole grain millet breakfast</div>
            </div>
        </div>
    </div>
"""

print(f"Part 2 simulators written: {len(simulators_part2)}")


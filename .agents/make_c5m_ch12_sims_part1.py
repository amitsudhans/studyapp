# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
Simulators 1 to 8 (HTML & SVG interactive components)
"""

simulators_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧘 Yoga Elapsed Time Calculator</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Morning Practice Session</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust start and finish times to see the elapsed duration calculated via timeline milestones:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Start Minute (06:xx):</span>
                        <span id="sim1_start_val" class="text-cyan-400 font-mono font-bold">06:15 a.m.</span>
                    </div>
                    <input type="range" id="sim1_start" min="0" max="30" step="5" value="15" oninput="sim1Update()" class="w-full accent-cyan-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>End Minute (07:xx):</span>
                        <span id="sim1_end_val" class="text-emerald-400 font-mono font-bold">07:05 a.m.</span>
                    </div>
                    <input type="range" id="sim1_end" min="0" max="30" step="5" value="5" oninput="sim1Update()" class="w-full accent-emerald-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim1_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Dial -->
                    <circle cx="100" cy="80" r="60" fill="#0f172a" stroke="#475569" stroke-width="3"/>
                    <!-- Hour numbers -->
                    <text x="100" y="32" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">12</text>
                    <text x="150" y="84" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">3</text>
                    <text x="100" y="134" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">6</text>
                    <text x="50" y="84" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">9</text>
                    <!-- Hands -->
                    <line id="sim1_hour_hand" x1="100" y1="80" x2="100" y2="52" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round"/>
                    <line id="sim1_min_hand" x1="100" y1="80" x2="135" y2="80" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
                    <circle cx="100" cy="80" r="4" fill="#f8fafc"/>
                    <!-- Start-to-End arc highlight -->
                    <path id="sim1_arc" d="" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round" opacity="0.75"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Timeline Milestone Jumps:</span>
                    <div id="sim1_step1" class="text-cyan-300">Step 1: 06:15 ➔ 07:00 = 45 min</div>
                    <div id="sim1_step2" class="text-emerald-300">Step 2: 07:00 ➔ 07:05 = 5 min</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Total Elapsed Time:</span>
                    <span id="sim1_res_tot" class="text-amber-300 font-bold text-sm">50 minutes</span>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">⏱️ Interval Duration Studio</span>
                <span id="sim2_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Select Preset</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Explore the 3 core time-interval scenarios from the syllabus:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim2Select(1)" id="sim2_btn_1" class="px-2 py-1 rounded bg-cyan-600 text-white font-semibold">01:15 to 01:42 p.m.</button>
                <button onclick="sim2Select(2)" id="sim2_btn_2" class="px-2 py-1 rounded bg-slate-800 text-slate-200">03:18 to 08:18 p.m.</button>
                <button onclick="sim2Select(3)" id="sim2_btn_3" class="px-2 py-1 rounded bg-slate-800 text-slate-200">09:15 to 11:30 a.m.</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim2_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Linear timeline arc visualization -->
                    <line x1="20" y1="90" x2="180" y2="90" stroke="#475569" stroke-width="3"/>
                    <circle cx="30" cy="90" r="5" fill="#38bdf8"/>
                    <circle cx="170" cy="90" r="5" fill="#10b981"/>
                    <text id="sim2_lbl_start" x="30" y="112" text-anchor="middle" font-size="9" fill="#38bdf8" font-weight="bold">01:15 p.m.</text>
                    <text id="sim2_lbl_end" x="170" y="112" text-anchor="middle" font-size="9" fill="#10b981" font-weight="bold">01:42 p.m.</text>
                    <!-- Jump arc -->
                    <path id="sim2_jump_arc" d="M 30,85 Q 100,30 170,85" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
                    <text id="sim2_jump_txt" x="100" y="48" text-anchor="middle" font-size="11" fill="#f59e0b" font-weight="bold">+27 min</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1" id="sim2_type">Category: Same Hour Gap</span>
                    <div id="sim2_math" class="text-slate-300">Subtract minutes: 42 − 15 = 27 min</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Elapsed Duration:</span>
                    <span id="sim2_res" class="text-emerald-400 font-bold text-sm">27 minutes</span>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">🎨 Painting Duration Ranker</span>
                <span id="sim3_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Art Studio Contest</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a student painter to highlight their duration and view comparative rankings:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim3Highlight('all')" id="sim3_btn_all" class="px-2 py-1 rounded bg-indigo-600 text-white font-semibold">All 4 Painters</button>
                <button onclick="sim3Highlight('student3')" id="sim3_btn_student3" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Student 3 (90m)</button>
                <button onclick="sim3Highlight('student1')" id="sim3_btn_student1" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Student 1 (75m)</button>
                <button onclick="sim3Highlight('student2')" id="sim3_btn_student2" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Student 2 (50m)</button>
                <button onclick="sim3Highlight('student4')" id="sim3_btn_student4" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Student 4 (40m)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim3_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Bar Chart of Durations -->
                    <g id="sim3_bars">
                        <!-- Student 3 (90) -->
                        <text x="25" y="30" font-size="8" fill="#818cf8">Student 3</text>
                        <rect x="60" y="22" width="120" height="11" rx="2" fill="#6366f1"/>
                        <text x="185" y="31" font-size="8" fill="#c7d2fe">90m</text>

                        <!-- Student 1 (75) -->
                        <text x="25" y="60" font-size="8" fill="#38bdf8">Student 1</text>
                        <rect x="60" y="52" width="100" height="11" rx="2" fill="#0284c7"/>
                        <text x="165" y="61" font-size="8" fill="#bae6fd">75m</text>

                        <!-- Student 2 (50) -->
                        <text x="25" y="90" font-size="8" fill="#fbbf24">Student 2</text>
                        <rect x="60" y="82" width="67" height="11" rx="2" fill="#d97706"/>
                        <text x="132" y="91" font-size="8" fill="#fde68a">50m</text>

                        <!-- Student 4 (40) -->
                        <text x="25" y="120" font-size="8" fill="#34d399">Student 4</text>
                        <rect x="60" y="112" width="53" height="11" rx="2" fill="#059669"/>
                        <text x="118" y="121" font-size="8" fill="#a7f3d0">40m</text>
                    </g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-indigo-400 font-bold block mb-1">Rank Analysis:</span>
                    <div id="sim3_desc">Longest: Student 3 (90 min) • Shortest: Student 4 (40 min)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Spread / Difference:</span>
                    <span id="sim3_diff" class="text-amber-400 font-bold">90 − 40 = 50 minutes</span>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🚉 12-Hour vs 24-Hour Railway Clock</span>
                <span id="sim4_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Daylight Time</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Slide the 24-hour master clock to observe automatic conversion between 12-hour and railway time:</p>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>24-Hour Master Slider:</span>
                    <span id="sim4_hr_val" class="text-emerald-400 font-mono font-bold">16:30 Hours</span>
                </div>
                <input type="range" id="sim4_hr" min="0" max="23" step="1" value="16" oninput="sim4Update()" class="w-full accent-emerald-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Electronic Station Display</span>
                <div id="sim4_disp_24" class="text-2xl font-black font-mono text-emerald-400 bg-slate-900 px-4 py-1.5 rounded-lg border border-emerald-500/40 shadow-inner">
                    16:30
                </div>
                <span class="text-[10px] text-emerald-300 mt-1 font-mono">Railway / Military Time</span>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1">12-Hour Format:</span>
                    <div id="sim4_disp_12" class="text-white font-bold text-sm">04:30 p.m.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Conversion Rule:</span>
                    <div id="sim4_rule" class="text-slate-300">P.M. time ➔ 4 + 12 = 16:30 hours</div>
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">🏃 200m School Race Stopwatch</span>
                <span id="sim5_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Ready at Starting Line</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Simulate the 200m walking race to see why seconds are necessary to separate the three competitors:</p>
            <div class="flex gap-2 mb-1">
                <button onclick="sim5StartRace()" id="sim5_race_btn" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow flex items-center gap-1">
                    <span>▶️</span> Start 200m Race
                </button>
                <button onclick="sim5ResetRace()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs">
                    Reset Track
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim5_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- 3 Track Lanes -->
                    <rect x="20" y="20" width="160" height="35" rx="3" fill="#1e293b" stroke="#334155"/>
                    <rect x="20" y="62" width="160" height="35" rx="3" fill="#1e293b" stroke="#334155"/>
                    <rect x="20" y="105" width="160" height="35" rx="3" fill="#1e293b" stroke="#334155"/>
                    <!-- Finish Line Ribbon -->
                    <line x1="165" y1="15" x2="165" y2="145" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3,3"/>
                    <!-- Racers -->
                    <circle id="sim5_racer1" cx="30" cy="37" r="7" fill="#10b981"/>
                    <text x="42" y="40" font-size="8" fill="#6ee7b7">Runner A</text>
                    <circle id="sim5_racer2" cx="30" cy="79" r="7" fill="#38bdf8"/>
                    <text x="42" y="82" font-size="8" fill="#7dd3fc">Runner C</text>
                    <circle id="sim5_racer3" cx="30" cy="122" r="7" fill="#f59e0b"/>
                    <text x="42" y="125" font-size="8" fill="#fcd34d">Runner B</text>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between text-emerald-400 font-bold"><span>Runner A (Gold):</span><span>2 min 14 sec</span></div>
                    <div class="flex justify-between text-cyan-400 font-bold mt-1"><span>Runner C (Silver):</span><span>2 min 18 sec</span></div>
                    <div class="flex justify-between text-amber-400 font-bold mt-1"><span>Runner B (Bronze):</span><span>2 min 22 sec</span></div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-rose-400 font-bold">Precision Lesson:</span>
                    <span class="text-slate-300 block text-[10px] mt-0.5">Without seconds, all 3 racers would appear tied at 2 minutes!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⏱️ Seconds Precision & Sweep Studio</span>
                <span id="sim6_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">1 min = 60 sec</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Trigger seconds hand rotations to observe how seconds accumulate to advance the minute hand:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim6Sweep(10)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">+10 Sec</button>
                <button onclick="sim6Sweep(30)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">30 Sec (1/2 Turn)</button>
                <button onclick="sim6Sweep(45)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">45 Sec (3/4 Turn)</button>
                <button onclick="sim6Sweep(60)" class="px-2 py-1 rounded bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">60 Sec (Full Circuit!)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim6_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <circle cx="100" cy="80" r="60" fill="#0f172a" stroke="#64748b" stroke-width="2.5"/>
                    <!-- 60 Hash marks -->
                    <g id="sim6_hashes"></g>
                    <!-- Minute Hand -->
                    <line id="sim6_min_hand" x1="100" y1="80" x2="100" y2="40" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                    <!-- Red Seconds Hand -->
                    <line id="sim6_sec_hand" x1="100" y1="80" x2="100" y2="30" stroke="#ef4444" stroke-width="1.5" stroke-linecap="round"/>
                    <circle cx="100" cy="80" r="3.5" fill="#ef4444"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between"><span>Current Seconds:</span><span id="sim6_sec_val" class="text-rose-400 font-bold">0 sec</span></div>
                    <div class="flex justify-between mt-1"><span>Angle Turned:</span><span id="sim6_deg_val" class="text-cyan-400 font-bold">0°</span></div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-300 font-bold block mb-1">Equivalence Rule:</span>
                    <span id="sim6_desc" class="text-slate-300">60 seconds of rotation advances the minute hand by exactly 1 minute mark.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">⚖️ Time Unit Estimation Classifier</span>
                <span id="sim7_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Interactive Sorting</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click an activity to test whether it belongs to seconds or minutes:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim7Test('blink')" id="sim7_btn_blink" class="px-2 py-1 rounded bg-teal-600 text-white font-semibold">👀 Eye Blink</button>
                <button onclick="sim7Test('switch')" id="sim7_btn_switch" class="px-2 py-1 rounded bg-slate-800 text-slate-200">💡 Light Switch</button>
                <button onclick="sim7Test('teeth')" id="sim7_btn_teeth" class="px-2 py-1 rounded bg-slate-800 text-slate-200">🪥 Brush Teeth</button>
                <button onclick="sim7Test('count')" id="sim7_btn_count" class="px-2 py-1 rounded bg-slate-800 text-slate-200">🔢 Count 1 to 20</button>
                <button onclick="sim7Test('lunch')" id="sim7_btn_lunch" class="px-2 py-1 rounded bg-slate-800 text-slate-200">🍲 Eat Lunch</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 space-y-2 text-center">
                <div class="text-3xl" id="sim7_icon">👀</div>
                <div class="text-sm font-bold text-white" id="sim7_title">Blinking Eyelids</div>
                <span id="sim7_badge" class="inline-block px-2 py-0.5 rounded text-xs font-bold font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                    Takes Seconds (~0.3 sec)
                </span>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-teal-400 font-bold block mb-1">Reasoning & Duration:</span>
                    <span id="sim7_reason">Occurs almost instantaneously in a single split second!</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Rule: Instant actions ➔ Seconds; Multi-step actions ➔ Minutes.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-rose-400">⏱️ One-Minute Challenge Simulator</span>
                <span id="sim8_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">60-Second Benchmark</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a physical feat and run a live 60-second timer to test your estimation vs actual rhythm:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim8SelectFeat('pushups')" id="sim8_btn_pushups" class="px-2 py-1 rounded bg-rose-600 text-white font-semibold">Push-Ups</button>
                <button onclick="sim8SelectFeat('balloons')" id="sim8_btn_balloons" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Blow Balloons</button>
                <button onclick="sim8SelectFeat('breaths')" id="sim8_btn_breaths" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Breaths</button>
                <button onclick="sim8SelectFeat('hops')" id="sim8_btn_hops" class="px-2 py-1 rounded bg-slate-800 text-slate-200">One-Leg Hops</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Live 60s Countdown</span>
                <div id="sim8_timer" class="text-3xl font-black font-mono text-rose-400 bg-slate-900 px-4 py-1.5 rounded-lg border border-rose-500/40">
                    60s
                </div>
                <div class="flex gap-2 mt-2">
                    <button onclick="sim8StartTimer()" id="sim8_timer_btn" class="px-2.5 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs">Start Timer</button>
                    <button onclick="sim8ResetTimer()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs">Reset</button>
                </div>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between text-slate-400"><span>Pre-Estimate:</span><span id="sim8_est">30 reps</span></div>
                    <div class="flex justify-between text-emerald-400 font-bold mt-1"><span>Actual Verified:</span><span id="sim8_act">15 to 22 reps</span></div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px]">
                    <span id="sim8_obs">Muscular fatigue slows repetition pace over 60 seconds.</span>
                </div>
            </div>
        </div>
    </div>
    """
}

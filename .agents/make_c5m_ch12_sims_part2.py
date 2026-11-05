# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
Simulators 9 to 16 (HTML & SVG interactive components)
"""

simulators_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-blue-400">⚡ Micro-Interval Stopwatch</span>
                <span id="sim9_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Sub-Minute Lab</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a short-duration activity to simulate high-precision timing:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim9Select('skip')" id="sim9_btn_skip" class="px-2 py-1 rounded bg-blue-600 text-white font-semibold">🪢 10s Skipping</button>
                <button onclick="sim9Select('word')" id="sim9_btn_word" class="px-2 py-1 rounded bg-slate-800 text-slate-200">✍️ Writing "FRIEND"</button>
                <button onclick="sim9Select('sprint')" id="sim9_btn_sprint" class="px-2 py-1 rounded bg-slate-800 text-slate-200">🏃 100m Sprint</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">High-Precision Timer</span>
                <div id="sim9_disp" class="text-3xl font-black font-mono text-cyan-400 bg-slate-900 px-4 py-1.5 rounded-lg border border-cyan-500/40">
                    10.0s
                </div>
                <div class="text-[10px] text-slate-400 mt-1 font-mono" id="sim9_frac">1/6th of a Minute</div>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1" id="sim9_title">10-Second Rope Skipping</span>
                    <div id="sim9_perf" class="text-slate-300">Achieved: 18 rapid rope skips!</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Why Seconds Count:</span>
                    <span id="sim9_why" class="text-slate-400">Whole minutes would round 10 seconds down to 0 minutes!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-purple-400">🕒 Analog Seconds Hand Reader</span>
                <span id="sim10_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Task 1: Walking to Kitchen</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a daily chore to observe the starting and ending position of the seconds hand:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim10Select('kitchen')" id="sim10_btn_kitchen" class="px-2 py-1 rounded bg-purple-600 text-white font-semibold">Walk to Kitchen</button>
                <button onclick="sim10Select('paper')" id="sim10_btn_paper" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Pick Up Paper</button>
                <button onclick="sim10Select('dish')" id="sim10_btn_dish" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Wash Plate</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800 gap-2">
                <!-- Clock A: Start -->
                <svg viewBox="0 0 100 100" class="w-20 h-20">
                    <circle cx="50" cy="50" r="45" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                    <text x="50" y="15" text-anchor="middle" font-size="8" fill="#94a3b8">12</text>
                    <text x="85" y="53" text-anchor="middle" font-size="8" fill="#94a3b8">3</text>
                    <text x="50" y="90" text-anchor="middle" font-size="8" fill="#94a3b8">6</text>
                    <text x="15" y="53" text-anchor="middle" font-size="8" fill="#94a3b8">9</text>
                    <line id="sim10_hand_a" x1="50" y1="50" x2="50" y2="15" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                    <circle cx="50" cy="50" r="3" fill="#ef4444"/>
                    <text x="50" y="98" text-anchor="middle" font-size="7" fill="#38bdf8">Start Clock</text>
                </svg>
                <span class="text-slate-400 font-bold">➔</span>
                <!-- Clock B: End -->
                <svg viewBox="0 0 100 100" class="w-20 h-20">
                    <circle cx="50" cy="50" r="45" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                    <text x="50" y="15" text-anchor="middle" font-size="8" fill="#94a3b8">12</text>
                    <text x="85" y="53" text-anchor="middle" font-size="8" fill="#94a3b8">3</text>
                    <text x="50" y="90" text-anchor="middle" font-size="8" fill="#94a3b8">6</text>
                    <text x="15" y="53" text-anchor="middle" font-size="8" fill="#94a3b8">9</text>
                    <line id="sim10_hand_b" x1="50" y1="50" x2="80" y2="68" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                    <circle cx="50" cy="50" r="3" fill="#ef4444"/>
                    <text x="50" y="98" text-anchor="middle" font-size="7" fill="#10b981">End Clock</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div id="sim10_gap" class="text-cyan-300 font-bold">Hand moved: 12 ➔ 4 (4 gaps)</div>
                    <div class="text-slate-400 mt-1">Each numeral gap = 5 seconds</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Elapsed Seconds:</span>
                    <span id="sim10_res" class="text-emerald-400 font-bold text-sm">20 seconds</span>
                </div>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">✏️ Seconds Hand Drawing Studio</span>
                <span id="sim11_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Target: 30 Seconds</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select target elapsed seconds starting from 12 to observe where to draw the red seconds hand:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim11Set(20)" id="sim11_btn_20" class="px-2 py-1 rounded bg-slate-800 text-slate-200">20 sec (➔ 4)</button>
                <button onclick="sim11Set(30)" id="sim11_btn_30" class="px-2 py-1 rounded bg-emerald-600 text-white font-semibold">30 sec (➔ 6)</button>
                <button onclick="sim11Set(40)" id="sim11_btn_40" class="px-2 py-1 rounded bg-slate-800 text-slate-200">40 sec (➔ 8)</button>
                <button onclick="sim11Set(60)" id="sim11_btn_60" class="px-2 py-1 rounded bg-slate-800 text-slate-200">60 sec (➔ 12)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim11_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <circle cx="100" cy="80" r="60" fill="#0f172a" stroke="#64748b" stroke-width="2.5"/>
                    <!-- Numerals -->
                    <text x="100" y="32" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">12</text>
                    <text x="150" y="84" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">3</text>
                    <text x="100" y="134" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">6</text>
                    <text x="50" y="84" text-anchor="middle" font-size="10" fill="#94a3b8" font-weight="bold">9</text>
                    <!-- Red Drawn Seconds Hand -->
                    <line id="sim11_hand" x1="100" y1="80" x2="100" y2="130" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round"/>
                    <circle cx="100" cy="80" r="4" fill="#ef4444"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold block mb-1">Drawing Formula:</span>
                    <div id="sim11_calc">Target Numeral = 30 ÷ 5 = 6</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Hand Orientation:</span>
                    <span id="sim11_orient" class="text-amber-300 font-bold">Points straight down at 6 (Half Turn)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔢 Hours To Minutes Multiplier</span>
                <span id="sim12_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">1 hr = 60 min</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust hours and extra minutes to calculate total minutes and verify the inverse division:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Hours:</span>
                        <span id="sim12_hr_val" class="text-amber-400 font-mono font-bold">2 hr</span>
                    </div>
                    <input type="range" id="sim12_hr" min="1" max="8" step="1" value="2" oninput="sim12Update()" class="w-full accent-amber-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Extra Minutes:</span>
                        <span id="sim12_min_val" class="text-cyan-400 font-mono font-bold">25 min</span>
                    </div>
                    <input type="range" id="sim12_min" min="0" max="55" step="5" value="25" oninput="sim12Update()" class="w-full accent-cyan-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Calculated Total</span>
                <div id="sim12_res_tot" class="text-3xl font-black font-mono text-amber-300 bg-slate-900 px-4 py-1.5 rounded-lg border border-amber-500/40">
                    145 min
                </div>
                <div class="text-[10px] text-slate-400 mt-1 font-mono" id="sim12_sub">2 × 60 + 25 = 145 min</div>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1">Inverse Verification:</span>
                    <div id="sim12_inv" class="text-slate-300">145 ÷ 60 = 2 hr remainder 25 min</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold">Base-60 Arithmetic:</span>
                    <span class="text-slate-400 block text-[10px]">Multiply by 60 to convert down; divide by 60 to convert up.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">📏 Double Number Line (Hours & Minutes)</span>
                <span id="sim13_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Proportional Dual Scale</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Slide along the dual scale to view hours directly aligned with their equivalent minutes:</p>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>Time Cursor:</span>
                    <span id="sim13_cur_val" class="text-teal-400 font-mono font-bold">2.5 Hours (150 min)</span>
                </div>
                <input type="range" id="sim13_cursor" min="0" max="300" step="15" value="150" oninput="sim13Update()" class="w-full accent-teal-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim13_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Top Axis (Hours) -->
                    <line x1="20" y1="45" x2="180" y2="45" stroke="#38bdf8" stroke-width="2"/>
                    <text x="20" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">0h</text>
                    <text x="52" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">1h</text>
                    <text x="84" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">2h</text>
                    <text x="116" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">3h</text>
                    <text x="148" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">4h</text>
                    <text x="180" y="35" text-anchor="middle" font-size="8" fill="#38bdf8">5h</text>

                    <!-- Bottom Axis (Minutes) -->
                    <line x1="20" y1="115" x2="180" y2="115" stroke="#fbbf24" stroke-width="2"/>
                    <text x="20" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">0m</text>
                    <text x="52" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">60m</text>
                    <text x="84" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">120m</text>
                    <text x="116" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">180m</text>
                    <text x="148" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">240m</text>
                    <text x="180" y="132" text-anchor="middle" font-size="8" fill="#fbbf24">300m</text>

                    <!-- Draggable Alignment Cursor -->
                    <line id="sim13_cursor_line" x1="100" y1="20" x2="100" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
                    <circle id="sim13_pt_top" cx="100" cy="45" r="4" fill="#38bdf8"/>
                    <circle id="sim13_pt_bot" cx="100" cy="115" r="4" fill="#fbbf24"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1">Aligned Values:</span>
                    <div id="sim13_res_top" class="text-cyan-300">Top Scale: 2 hr 30 min</div>
                    <div id="sim13_res_bot" class="text-amber-300 mt-1">Bottom Scale: 150 minutes</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Notice: 1 hour mark on top always aligns with 60 on bottom.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">📏 Double Number Line (Minutes & Seconds)</span>
                <span id="sim14_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Target: 320 Seconds</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Explore the famous 320 seconds and 10 min 13 sec conversions on the proportional scale:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim14Preset(320)" id="sim14_btn_320" class="px-2.5 py-1 rounded bg-cyan-600 text-white font-semibold">320 Seconds (5m 20s)</button>
                <button onclick="sim14Preset(150)" id="sim14_btn_150" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">150 Seconds (2m 30s)</button>
                <button onclick="sim14Preset(250)" id="sim14_btn_250" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">250 Seconds (4m 10s)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Dual Readout</span>
                <div id="sim14_disp_sec" class="text-2xl font-black font-mono text-cyan-400">320 Seconds</div>
                <div class="text-sm font-bold text-emerald-400 mt-1 font-mono" id="sim14_disp_min">5 min 20 sec</div>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Calculation Breakdown:</span>
                    <div id="sim14_math" class="text-slate-300">320 ÷ 60 = 5 with remainder 20</div>
                    <div class="text-cyan-300 font-bold mt-1">300s (5m) + 20s = 5 min 20 sec</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Reverse: 10 min 13 sec = (10 × 60) + 13 = 613 seconds!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📖 Elapsed Time Word Problem Solver</span>
                <span id="sim15_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">School Bus Picnic</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a real-world story scenario to see the timeline jump calculation unfold:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim15Select('picnic')" id="sim15_btn_picnic" class="px-2 py-1 rounded bg-amber-600 text-white font-semibold">🚌 School Picnic Trip</button>
                <button onclick="sim15Select('homework')" id="sim15_btn_homework" class="px-2 py-1 rounded bg-slate-800 text-slate-200">📚 Homework Time</button>
                <button onclick="sim15Select('movie')" id="sim15_btn_movie" class="px-2 py-1 rounded bg-slate-800 text-slate-200">🎬 Movie Schedule</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim15_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <line x1="20" y1="100" x2="180" y2="100" stroke="#475569" stroke-width="3"/>
                    <circle cx="30" cy="100" r="5" fill="#38bdf8"/>
                    <circle cx="100" cy="100" r="4" fill="#f59e0b"/>
                    <circle cx="170" cy="100" r="5" fill="#10b981"/>
                    <text id="sim15_lbl_1" x="30" y="122" text-anchor="middle" font-size="8" fill="#38bdf8" font-weight="bold">08:30 a.m.</text>
                    <text id="sim15_lbl_2" x="100" y="122" text-anchor="middle" font-size="8" fill="#f59e0b">09:30 a.m.</text>
                    <text id="sim15_lbl_3" x="170" y="122" text-anchor="middle" font-size="8" fill="#10b981" font-weight="bold">10:15 a.m.</text>
                    <!-- Arcs -->
                    <path d="M 30,95 Q 65,55 100,95" fill="none" stroke="#38bdf8" stroke-width="2"/>
                    <text x="65" y="65" text-anchor="middle" font-size="8" fill="#38bdf8">+1 hr</text>
                    <path d="M 100,95 Q 135,55 170,95" fill="none" stroke="#f59e0b" stroke-width="2"/>
                    <text x="135" y="65" text-anchor="middle" font-size="8" fill="#f59e0b">+45 min</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1" id="sim15_title">Bus Journey (1 hr 45 min)</span>
                    <div id="sim15_steps" class="text-slate-300">08:30 + 1 hr = 09:30 ➔ + 45 min = 10:15 a.m.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Final Calculated Time:</span>
                    <span id="sim15_res" class="text-emerald-400 font-bold text-sm">10:15 a.m.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">📅 Daily Time Schedules Planner</span>
                <span id="sim16_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Active School Day</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Inspect the master timeline of a 5th grade school day integrating hours, minutes, and seconds:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim16Highlight('assembly')" id="sim16_btn_assembly" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Assembly (25m)</button>
                <button onclick="sim16Highlight('lunch')" id="sim16_btn_lunch" class="px-2 py-1 rounded bg-emerald-600 text-white font-semibold">Lunch Break (40m)</button>
                <button onclick="sim16Highlight('sports')" id="sim16_btn_sports" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Sports Sprint (20.4s)</button>
                <button onclick="sim16Highlight('all')" id="sim16_btn_all" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Full Day View</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim16_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Day Schedule Blocks -->
                    <rect x="25" y="25" width="40" height="25" rx="3" fill="#0284c7"/>
                    <text x="45" y="41" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Assembly</text>

                    <rect x="70" y="25" width="105" height="25" rx="3" fill="#4338ca"/>
                    <text x="122" y="41" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Morning Lessons (3h 50m)</text>

                    <rect id="sim16_lunch_rect" x="25" y="65" width="70" height="25" rx="3" fill="#059669" stroke="#34d399" stroke-width="2"/>
                    <text x="60" y="81" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Lunch (40m)</text>

                    <rect x="100" y="65" width="75" height="25" rx="3" fill="#4338ca"/>
                    <text x="137" y="81" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Afternoon Classes</text>

                    <rect x="25" y="105" width="150" height="25" rx="3" fill="#b45309"/>
                    <text x="100" y="121" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="bold">Evening Sports & Sprints (Seconds!)</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold block mb-1" id="sim16_title">Lunch Recess Duration</span>
                    <div id="sim16_time" class="text-slate-300">12:15 p.m. + 40 min = 12:55 p.m.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold">Continuum Lesson:</span>
                    <span class="text-slate-400 block text-[10px]">Hours partition the day; minutes divide classes; seconds time athletic sprints.</span>
                </div>
            </div>
        </div>
    </div>
    """
}

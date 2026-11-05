# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Chapter 15: Data Through Pictures"""

sims_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📊 Vertical Daily Routine Bar Graph</span>
                <span id="sim9_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Total: 24 Hours</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click any activity bar to inspect its exact vertical height and duration:</p>
            <div class="flex flex-wrap gap-1 mb-2">
                <button onclick="sim9Highlight('sleep')" id="sim9_btn_sleep" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold transition">Sleep (8h)</button>
                <button onclick="sim9Highlight('school')" id="sim9_btn_school" class="px-2 py-1 rounded bg-slate-800 text-amber-300 transition">School (6h)</button>
                <button onclick="sim9Highlight('study')" id="sim9_btn_study" class="px-2 py-1 rounded bg-slate-800 text-cyan-300 transition">Study (2h)</button>
                <button onclick="sim9Highlight('play')" id="sim9_btn_play" class="px-2 py-1 rounded bg-slate-800 text-emerald-300 transition">Play (4h)</button>
                <button onclick="sim9Highlight('other')" id="sim9_btn_other" class="px-2 py-1 rounded bg-slate-800 text-rose-300 transition">Other (4h)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim9_svg" viewBox="0 0 200 150" class="w-48 h-36">
                    <!-- Axes -->
                    <line x1="30" y1="130" x2="190" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="30" y1="130" x2="30" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                    <text x="185" y="140" font-size="6" fill="#94a3b8">Activity</text>
                    <text x="25" y="12" font-size="6" fill="#94a3b8">Hours</text>

                    <!-- Y-axis ticks (0, 2, 4, 6, 8, 10) Scale: 1 hr = 10px, Base = 130 -->
                    <text x="22" y="133" font-size="6" fill="#64748b" text-anchor="end">0</text>
                    <text x="22" y="113" font-size="6" fill="#64748b" text-anchor="end">2</text>
                    <text x="22" y="93" font-size="6" fill="#64748b" text-anchor="end">4</text>
                    <text x="22" y="73" font-size="6" fill="#64748b" text-anchor="end">6</text>
                    <text x="22" y="53" font-size="6" fill="#64748b" text-anchor="end">8</text>
                    <text x="22" y="33" font-size="6" fill="#64748b" text-anchor="end">10</text>

                    <!-- Horizontal Gridlines -->
                    <line x1="30" y1="110" x2="190" y2="110" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>
                    <line x1="30" y1="90" x2="190" y2="90" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>
                    <line x1="30" y1="70" x2="190" y2="70" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>
                    <line x1="30" y1="50" x2="190" y2="50" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>

                    <!-- Bars (Width = 20px) -->
                    <!-- Sleep: 8h -> Height = 80px, Y = 50 -->
                    <rect id="sim9_bar_sleep" x="40" y="50" width="22" height="80" rx="2" fill="#6366f1"/>
                    <text x="51" y="142" font-size="6" fill="#818cf8" text-anchor="middle">Sleep</text>

                    <!-- School: 6h -> Height = 60px, Y = 70 -->
                    <rect id="sim9_bar_school" x="70" y="70" width="22" height="60" rx="2" fill="#f59e0b"/>
                    <text x="81" y="142" font-size="6" fill="#fbbf24" text-anchor="middle">School</text>

                    <!-- Study: 2h -> Height = 20px, Y = 110 -->
                    <rect id="sim9_bar_study" x="100" y="110" width="22" height="20" rx="2" fill="#06b6d4"/>
                    <text x="111" y="142" font-size="6" fill="#22d3ee" text-anchor="middle">Study</text>

                    <!-- Play: 4h -> Height = 40px, Y = 90 -->
                    <rect id="sim9_bar_play" x="130" y="90" width="22" height="40" rx="2" fill="#10b981"/>
                    <text x="141" y="142" font-size="6" fill="#34d399" text-anchor="middle">Play</text>

                    <!-- Other: 4h -> Height = 40px, Y = 90 -->
                    <rect id="sim9_bar_other" x="160" y="90" width="22" height="40" rx="2" fill="#f43f5e"/>
                    <text x="171" y="142" font-size="6" fill="#fb7185" text-anchor="middle">Other</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim9_act_title" class="text-indigo-400 font-bold block mb-1">🛏️ Restful Sleep</span>
                    <div id="sim9_act_hours" class="text-white font-bold text-sm mb-1">Height: 8 Hours</div>
                    <div id="sim9_act_desc" class="text-[10px] text-slate-300">Occupies 8 out of 24 daily hours (exactly 1/3 of the full day). Tallest bar in the graph.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10px] text-slate-300 flex justify-between items-center">
                    <span>Graph Rule:</span>
                    <span class="text-emerald-400 font-bold">Bar Height ∝ Quantity</span>
                </div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-sky-400">⚖️ Schedule Balance & Equity Analyzer</span>
                <span id="sim10_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Total: 24h</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust sleeping and study sliders to see the automatic impact on daily lifestyle balance:</p>
            <div class="grid grid-cols-2 gap-3 mb-2">
                <div>
                    <label class="text-[10px] text-indigo-300 flex justify-between">
                        <span>Sleep Hours:</span>
                        <span id="sim10_sleep_txt" class="font-bold text-white">8h</span>
                    </label>
                    <input type="range" id="sim10_slider_sleep" min="6" max="10" value="8" oninput="sim10Update()" class="w-full accent-indigo-500 cursor-pointer">
                </div>
                <div>
                    <label class="text-[10px] text-cyan-300 flex justify-between">
                        <span>Self-Study Hours:</span>
                        <span id="sim10_study_txt" class="font-bold text-white">2h</span>
                    </label>
                    <input type="range" id="sim10_slider_study" min="1" max="4" value="2" oninput="sim10Update()" class="w-full accent-cyan-500 cursor-pointer">
                </div>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="grid grid-cols-3 gap-2 text-center text-[10.5px]">
                <div class="p-2 rounded bg-indigo-950/60 border border-indigo-500/30 text-indigo-300">
                    <span class="block text-slate-400 text-[10px]">Sleep:</span>
                    <span id="sim10_disp_sleep" class="font-bold text-sm">8 Hours</span>
                </div>
                <div class="p-2 rounded bg-amber-950/60 border border-amber-500/30 text-amber-300">
                    <span class="block text-slate-400 text-[10px]">Education:</span>
                    <span id="sim10_disp_edu" class="font-bold text-sm">8 Hours</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/60 border border-emerald-500/30 text-emerald-300">
                    <span class="block text-slate-400 text-[10px]">Play & Food:</span>
                    <span id="sim10_disp_play" class="font-bold text-sm">8 Hours</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10.5px]">
                <span id="sim10_balance_status" class="text-emerald-400 font-bold block mb-0.5">✓ Perfectly Balanced Three-Part Day (8-8-8)</span>
                <span id="sim10_balance_desc" class="text-slate-400 text-[10px]">1/3 of the day is allocated to sleep, 1/3 to education, and 1/3 to recreation and living.</span>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">✂️ Paper Strip Finger Measuring Lab</span>
                <span id="sim11_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Select Student</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Simulate measuring index fingers with paper strips and cutting off excess length:</p>
            <div class="flex gap-1.5 mb-2">
                <button onclick="sim11Measure('A')" id="sim11_btn_a" class="flex-1 py-1 rounded bg-teal-600 text-white font-bold transition">Friend A</button>
                <button onclick="sim11Measure('B')" id="sim11_btn_b" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Friend B</button>
                <button onclick="sim11Measure('C')" id="sim11_btn_c" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Friend C</button>
                <button onclick="sim11Measure('D')" id="sim11_btn_d" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Friend D</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim11_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Centimeter Ruler on Left -->
                    <rect x="20" y="10" width="18" height="120" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                    <line x1="38" y1="130" x2="30" y2="130" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="132" font-size="6" fill="#94a3b8" text-anchor="end">0</text>
                    <line x1="38" y1="110" x2="32" y2="110" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="112" font-size="6" fill="#94a3b8" text-anchor="end">1</text>
                    <line x1="38" y1="90" x2="32" y2="90" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="92" font-size="6" fill="#94a3b8" text-anchor="end">2</text>
                    <line x1="38" y1="70" x2="32" y2="70" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="72" font-size="6" fill="#94a3b8" text-anchor="end">3</text>
                    <line x1="38" y1="50" x2="32" y2="50" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="52" font-size="6" fill="#94a3b8" text-anchor="end">4</text>
                    <line x1="38" y1="30" x2="32" y2="30" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="32" font-size="6" fill="#94a3b8" text-anchor="end">5</text>
                    <line x1="38" y1="10" x2="30" y2="10" stroke="#f8fafc" stroke-width="1"/>
                    <text x="26" y="12" font-size="6" fill="#94a3b8" text-anchor="end">6</text>

                    <!-- Base Line -->
                    <line x1="15" y1="130" x2="145" y2="130" stroke="#94a3b8" stroke-width="1.5"/>

                    <!-- Paper Strip (Friend A default: 4.5 cm -> height = 90px (20px/cm), Y = 40) -->
                    <rect id="sim11_strip" x="65" y="40" width="20" height="90" rx="1" fill="#facc15" stroke="#ca8a04" stroke-width="1"/>
                    
                    <!-- Cut line indicator -->
                    <line id="sim11_cut_line" x1="60" y1="40" x2="90" y2="40" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,1"/>
                    <text id="sim11_label" x="75" y="35" text-anchor="middle" font-size="7" fill="#facc15" font-weight="bold">4.5 cm</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim11_friend_name" class="text-teal-400 font-bold block mb-1">Friend A Measurement</span>
                    <div id="sim11_len_disp" class="text-amber-300 font-bold text-sm mb-1">Index Finger: 4.5 cm</div>
                    <div id="sim11_detail_txt" class="text-[10px] text-slate-300">Paper strip aligned with base crease joint; marked at tip and excess paper trimmed away.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10px] text-slate-300 flex justify-between items-center">
                    <span>Protocol:</span>
                    <span class="text-emerald-400 font-bold">Accurate to ±1 mm</span>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">📏 Physical Strip Bar Graph Canvas</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Common Zero Baseline</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Examine all four student strips pasted side by side on a vertical centimeter grid:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim12Compare('max_min')" id="sim12_btn_diff" class="flex-1 py-1 rounded bg-emerald-600 text-white font-bold transition">Longest vs Shortest Spread</button>
                <button onclick="sim12Compare('all')" id="sim12_btn_all" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Show All Strips</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim12_svg" viewBox="0 0 180 140" class="w-44 h-32">
                    <!-- Baseline -->
                    <line x1="20" y1="125" x2="165" y2="125" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="25" y1="125" x2="25" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                    <text x="20" y="14" font-size="6" fill="#94a3b8">cm</text>

                    <!-- Strips (20px per cm, Base = 125) -->
                    <!-- Friend D: 4.2 cm -> height 84px, Y = 41 -->
                    <rect id="sim12_strip_d" x="40" y="41" width="18" height="84" rx="1" fill="#f43f5e"/>
                    <text x="49" y="135" font-size="6" fill="#fb7185" text-anchor="middle">D (4.2)</text>

                    <!-- Friend A: 4.5 cm -> height 90px, Y = 35 -->
                    <rect id="sim12_strip_a" x="70" y="35" width="18" height="90" rx="1" fill="#facc15"/>
                    <text x="79" y="135" font-size="6" fill="#fde047" text-anchor="middle">A (4.5)</text>

                    <!-- Friend B: 5.0 cm -> height 100px, Y = 25 -->
                    <rect id="sim12_strip_b" x="100" y="25" width="18" height="100" rx="1" fill="#06b6d4"/>
                    <text x="109" y="135" font-size="6" fill="#67e8f9" text-anchor="middle">B (5.0)</text>

                    <!-- Friend C: 5.8 cm -> height 116px, Y = 9 -->
                    <rect id="sim12_strip_c" x="130" y="9" width="18" height="116" rx="1" fill="#10b981"/>
                    <text x="139" y="135" font-size="6" fill="#6ee7b7" text-anchor="middle">C (5.8)</text>

                    <!-- Range Indicator Line -->
                    <line id="sim12_range_line" x1="49" y1="9" x2="139" y2="9" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim12_comp_title" class="text-emerald-400 font-bold block mb-1">Spread Across Measured Cohort</span>
                    <div id="sim12_comp_math" class="text-amber-300 font-bold text-sm mb-1">Range = 5.8 - 4.2 = 1.6 cm</div>
                    <div id="sim12_comp_desc" class="text-[10px] text-slate-300">Friend C possesses the longest finger (5.8 cm), while Friend D has the shortest (4.2 cm).</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10px] text-slate-300 flex justify-between items-center">
                    <span>Variation Spread:</span>
                    <span class="text-emerald-400 font-bold">1.6 cm (16 mm)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-rose-400">🍲 Canteen Food Waste Notice Board</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Total: 27 kg</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a menu day to inspect cafeteria plate waste measured by kitchen staff:</p>
            <div class="flex flex-wrap gap-1 mb-2">
                <button onclick="sim13SelectDay('mon')" id="sim13_btn_mon" class="px-2 py-1 rounded bg-slate-800 text-slate-200 transition">Mon (4kg)</button>
                <button onclick="sim13SelectDay('tue')" id="sim13_btn_tue" class="px-2 py-1 rounded bg-slate-800 text-slate-200 transition">Tue (7kg)</button>
                <button onclick="sim13SelectDay('wed')" id="sim13_btn_wed" class="px-2 py-1 rounded bg-slate-800 text-emerald-300 transition">Wed (3kg)</button>
                <button onclick="sim13SelectDay('thu')" id="sim13_btn_thu" class="px-2 py-1 rounded bg-rose-600 text-white font-bold transition">Thu (8kg)</button>
                <button onclick="sim13SelectDay('fri')" id="sim13_btn_fri" class="px-2 py-1 rounded bg-slate-800 text-slate-200 transition">Fri (5kg)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim13_svg" viewBox="0 0 180 140" class="w-44 h-32">
                    <line x1="25" y1="125" x2="170" y2="125" stroke="#94a3b8" stroke-width="1.5"/>
                    <line x1="25" y1="125" x2="25" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                    <text x="18" y="15" font-size="6" fill="#94a3b8">kg</text>

                    <!-- Gridlines: 10px per kg, Base = 125 -->
                    <line x1="25" y1="95" x2="170" y2="95" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>
                    <line x1="25" y1="65" x2="170" y2="65" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>
                    <line x1="25" y1="35" x2="170" y2="35" stroke="#334155" stroke-width="0.5" stroke-dasharray="2,2"/>

                    <!-- Mon: 4kg (40px, Y=85) -->
                    <rect id="sim13_bar_mon" x="35" y="85" width="18" height="40" rx="1" fill="#f59e0b"/>
                    <text x="44" y="135" font-size="5.5" fill="#fcd34d" text-anchor="middle">Mon</text>

                    <!-- Tue: 7kg (70px, Y=55) -->
                    <rect id="sim13_bar_tue" x="62" y="55" width="18" height="70" rx="1" fill="#f59e0b"/>
                    <text x="71" y="135" font-size="5.5" fill="#fcd34d" text-anchor="middle">Tue</text>

                    <!-- Wed: 3kg (30px, Y=95) -->
                    <rect id="sim13_bar_wed" x="89" y="95" width="18" height="30" rx="1" fill="#10b981"/>
                    <text x="98" y="135" font-size="5.5" fill="#6ee7b7" text-anchor="middle">Wed</text>

                    <!-- Thu: 8kg (80px, Y=45) -->
                    <rect id="sim13_bar_thu" x="116" y="45" width="18" height="80" rx="1" fill="#ef4444"/>
                    <text x="125" y="135" font-size="5.5" fill="#fca5a5" text-anchor="middle">Thu</text>

                    <!-- Fri: 5kg (50px, Y=75) -->
                    <rect id="sim13_bar_fri" x="143" y="75" width="18" height="50" rx="1" fill="#f59e0b"/>
                    <text x="152" y="135" font-size="5.5" fill="#fcd34d" text-anchor="middle">Fri</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim13_day_name" class="text-rose-400 font-bold block mb-1">Thursday: Puri-Sabzi</span>
                    <div id="sim13_day_waste" class="text-white font-bold text-sm mb-1">Plate Waste: 8 kg (Peak)</div>
                    <div id="sim13_day_desc" class="text-[10px] text-slate-300">Highest waste of the week. Suggests that fixed portions of puri-sabzi were larger than student appetite.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10px] text-slate-300 flex justify-between items-center">
                    <span>Lowest Day:</span>
                    <span class="text-emerald-400 font-bold">Wed Khichdi (3 kg)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">💡 Food Waste Meal Saver Calculator</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">1 kg = 3 Meals</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Simulate canteen waste reduction strategies to calculate child meals saved:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim14SetReduction(0)" id="sim14_btn_0" class="flex-1 py-1 rounded bg-rose-600 text-white font-bold transition">No Change (27kg)</button>
                <button onclick="sim14SetReduction(25)" id="sim14_btn_25" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 transition">-25% Waste</button>
                <button onclick="sim14SetReduction(50)" id="sim14_btn_50" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 transition">-50% Waste</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="grid grid-cols-2 gap-2 text-center text-[11px]">
                <div class="p-2 rounded bg-slate-950/80 border border-slate-800">
                    <span class="block text-slate-400 text-[10px]">Weekly Waste Mass:</span>
                    <span id="sim14_waste_kg" class="font-bold text-rose-400 text-sm">27.0 kg</span>
                </div>
                <div class="p-2 rounded bg-slate-950/80 border border-slate-800">
                    <span class="block text-slate-400 text-[10px]">Potential Meals Wasted:</span>
                    <span id="sim14_meals_wasted" class="font-bold text-amber-400 text-sm">81 Child Meals</span>
                </div>
            </div>
            <div class="p-2 rounded bg-emerald-950/60 border border-emerald-500/30 text-emerald-300 text-[10.5px]">
                <span class="font-bold block mb-1">🌱 Impact of Conservation Plan:</span>
                <span id="sim14_impact_txt">At baseline, 27 kg of discarded food equals 81 meals that could have fed children. Reducing waste saves resources and protects the environment.</span>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">🔎 Courtyard Picture Logic Checker</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">12 Students</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Evaluate logical claims against visual counts in the courtyard illustration:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim15CheckStatement(1)" id="sim15_btn_s1" class="flex-1 py-1 rounded bg-cyan-600 text-white font-bold transition">Claim 1: Caps</button>
                <button onclick="sim15CheckStatement(2)" id="sim15_btn_s2" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Claim 2: Glasses</button>
                <button onclick="sim15CheckStatement(3)" id="sim15_btn_s3" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Claim 3: Overlap</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                <span id="sim15_claim_txt" class="text-amber-300 font-bold block mb-1">Claim 1: "Exactly 5 children are wearing caps."</span>
                <div id="sim15_verdict" class="text-emerald-400 font-bold text-sm mb-1">Verdict: TRUE ✓ (Visual Count = 5)</div>
                <div id="sim15_proof" class="text-[10px] text-slate-300">Careful scanning reveals 5 cap wearers among the 12 children in the courtyard.</div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Summary Counts:</span>
                <span class="text-cyan-300 font-bold">5 Caps | 4 Glasses | 6 Bags | 7 Books</span>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-violet-400">🔷 Regular Polyhedral Nets Explorer</span>
                <span id="sim16_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-violet-500/20 text-violet-300 border border-violet-500/30">Icosahedron (20)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Toggle between the flat 2D nets and 3D folded geometry of regular polyhedra:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim16SelectSolid('icosa')" id="sim16_btn_icosa" class="flex-1 py-1 rounded bg-violet-600 text-white font-bold transition">Icosahedron (20 Triangles)</button>
                <button onclick="sim16SelectSolid('dodeca')" id="sim16_btn_dodeca" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 transition">Dodecahedron (12 Pentagons)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim16_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Net schematic representation -->
                    <g id="sim16_net_graphic">
                        <!-- Default: Icosahedron net cluster of 20 triangles -->
                        <polygon points="40,30 60,30 50,47" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="60,30 80,30 70,47" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="80,30 100,30 90,47" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="100,30 120,30 110,47" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="50,47 70,47 60,30" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="70,47 90,47 80,30" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="90,47 110,47 100,30" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <!-- Row 2 -->
                        <polygon points="30,47 50,47 40,64" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="50,47 70,47 60,64" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="70,47 90,47 80,64" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="90,47 110,47 100,64" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="110,47 130,47 120,64" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="40,64 60,64 50,47" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="60,64 80,64 70,47" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="80,64 100,64 90,47" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="100,64 120,64 110,47" fill="#4f46e5" stroke="#ffffff" stroke-width="0.8"/>
                        <!-- Row 3 -->
                        <polygon points="40,64 60,64 50,81" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="60,64 80,64 70,81" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="80,64 100,64 90,81" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                        <polygon points="100,64 120,64 110,81" fill="#6366f1" stroke="#ffffff" stroke-width="0.8"/>
                    </g>
                    <text x="80" y="125" text-anchor="middle" font-size="7" fill="#a78bfa" font-weight="bold" id="sim16_net_caption">20 Equilateral Triangles</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim16_solid_name" class="text-violet-400 font-bold block mb-1">🔷 Regular Icosahedron</span>
                    <div id="sim16_props" class="text-[10.5px] text-slate-300 space-y-0.5">
                        <div>• Faces (F): 20 Equilateral Triangles</div>
                        <div>• Vertices (V): 12 Corners</div>
                        <div>• Edges (E): 30 Creased Lines</div>
                    </div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10px] text-slate-300 flex justify-between items-center">
                    <span>Euler Characteristic:</span>
                    <span class="text-emerald-400 font-bold">V - E + F = 2</span>
                </div>
            </div>
        </div>
    </div>
    """
}


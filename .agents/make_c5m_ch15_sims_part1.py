# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Chapter 15: Data Through Pictures"""

sims_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📝 Raw Survey Field Notebook</span>
                <span id="sim1_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Total: 35 Friends</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Inspect raw survey notes collected directly from thirty-five classmates:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim1Filter('all')" id="sim1_btn_all" class="px-2.5 py-1 rounded bg-amber-600 text-white font-bold transition">All 35 Notes</button>
                <button onclick="sim1Filter('half')" id="sim1_btn_half" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">½ hr (5)</button>
                <button onclick="sim1Filter('one')" id="sim1_btn_one" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">1 hr (12)</button>
                <button onclick="sim1Filter('one_half')" id="sim1_btn_one_half" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">1½ hrs (8)</button>
                <button onclick="sim1Filter('two')" id="sim1_btn_two" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">2 hrs (6)</button>
                <button onclick="sim1Filter('more')" id="sim1_btn_more" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">> 2 hrs (4)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="flex justify-between items-center bg-slate-800/80 p-2 rounded-lg border border-slate-700 text-[11px]">
                <span class="text-amber-300 font-bold">Unorganized Field Responses:</span>
                <span id="sim1_count" class="text-emerald-400 font-bold">35 Recorded Entries</span>
            </div>
            <div id="sim1_grid" class="flex flex-wrap gap-1 max-h-32 overflow-y-auto p-2 bg-slate-950/80 rounded-lg border border-slate-800 text-[10px]">
                <!-- Dynamically populated raw tags -->
            </div>
            <div class="text-[10px] text-slate-400 text-center" id="sim1_desc">
                Raw data reflects initial unorganized survey notes before mathematical tallying or grouping.
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">📊 Tally Marks & Frequency Table Builder</span>
                <span id="sim2_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">5 Intervals</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Group scattered observations into standardized 5-mark bundles (<s>||||</s>) and frequencies:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim2ShowAll()" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">Complete Table ➔</button>
                <button onclick="sim2StepTally()" id="sim2_btn_step" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Step Bundle (+5)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] text-slate-300 border-collapse">
                    <thead>
                        <tr class="border-b border-slate-700 text-amber-300">
                            <th class="py-1">TV Duration</th>
                            <th class="py-1">Tally Marks (5s)</th>
                            <th class="py-1 text-right">Frequency</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800" id="sim2_table_body">
                        <tr><td>½ hour</td><td id="sim2_tally_0" class="text-amber-400 font-bold"><s>||||</s></td><td id="sim2_freq_0" class="text-right text-white font-bold">5</td></tr>
                        <tr><td>1 hour</td><td id="sim2_tally_1" class="text-amber-400 font-bold"><s>||||</s> <s>||||</s> ||</td><td id="sim2_freq_1" class="text-right text-white font-bold">12</td></tr>
                        <tr><td>1½ hours</td><td id="sim2_tally_2" class="text-amber-400 font-bold"><s>||||</s> |||</td><td id="sim2_freq_2" class="text-right text-white font-bold">8</td></tr>
                        <tr><td>2 hours</td><td id="sim2_tally_3" class="text-amber-400 font-bold"><s>||||</s> |</td><td id="sim2_freq_3" class="text-right text-white font-bold">6</td></tr>
                        <tr><td>> 2 hours</td><td id="sim2_tally_4" class="text-amber-400 font-bold">||||</td><td id="sim2_freq_4" class="text-right text-white font-bold">4</td></tr>
                    </tbody>
                    <tfoot>
                        <tr class="border-t border-slate-600 font-bold text-emerald-400">
                            <td>Total Cohort</td>
                            <td id="sim2_tally_total">35 Tallies</td>
                            <td class="text-right" id="sim2_freq_total">35</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Check Sum Verification:</span>
                <span class="text-emerald-400 font-bold">5 + 12 + 8 + 6 + 4 = 35 Children</span>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-sky-400">🔍 TV Survey Subgroup Calculator</span>
                <span id="sim3_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Cohort Split</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Evaluate cumulative viewing habits against health guidelines (1 hr maximum):</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim3Subgroup('le1')" id="sim3_btn_le1" class="flex-1 py-1.5 rounded-lg bg-sky-600 text-white font-bold transition">≤ 1 Hour (Healthy)</button>
                <button onclick="sim3Subgroup('gt1')" id="sim3_btn_gt1" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">> 1 Hour (Excess)</button>
                <button onclick="sim3Subgroup('gt2')" id="sim3_btn_gt2" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">> 2 Hours (Extreme)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                <span id="sim3_calc_title" class="text-sky-300 font-bold block mb-1">Subgroup: 1 Hour or Less</span>
                <div id="sim3_calc_math" class="text-[11px] text-emerald-400 font-bold mb-1">5 (½ hr) + 12 (1 hr) = 17 Children</div>
                <div id="sim3_calc_desc" class="text-[10px] text-slate-300">17 out of 35 children (48.6%) adhere to healthy daily screen time recommendations.</div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                <div class="flex justify-between text-[10.5px] text-slate-400 mb-1">
                    <span>≤ 1 Hour: 17 Children</span>
                    <span>> 1 Hour: 18 Children</span>
                </div>
                <!-- Dual-color split progress bar -->
                <div class="w-full bg-slate-950 h-3 rounded-full overflow-hidden flex border border-slate-700">
                    <div id="sim3_bar_le" class="bg-emerald-500 h-full transition-all duration-300" style="width: 48.6%;"></div>
                    <div id="sim3_bar_gt" class="bg-rose-500 h-full transition-all duration-300" style="width: 51.4%;"></div>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧸 Toy Shop Inventory Pictograph</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Key: 1 ⭐ = 5 Items</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click an inventory row to reveal how symbols multiply by the scale factor of 5:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim4Inspect('toys')" id="sim4_btn_toys" class="flex-1 py-1 rounded bg-amber-600 text-white font-bold transition">Toys (4 ⭐)</button>
                <button onclick="sim4Inspect('games')" id="sim4_btn_games" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 transition">Games (6 ⭐)</button>
                <button onclick="sim4Inspect('sports')" id="sim4_btn_sports" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 transition">Sports (8 ⭐)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="space-y-1.5" id="sim4_rows">
                <div id="sim4_row_toys" class="p-2 rounded bg-slate-800/80 border border-amber-500/50 flex justify-between items-center">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">🧸 Stuffed Toys</span>
                        <span class="text-amber-400 text-sm">⭐⭐⭐⭐</span>
                    </div>
                    <span class="text-white font-bold text-xs">4 × 5 = 20 Items</span>
                </div>
                <div id="sim4_row_games" class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center opacity-60">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">🎲 Board Games</span>
                        <span class="text-cyan-400 text-sm">⭐⭐⭐⭐⭐⭐</span>
                    </div>
                    <span class="text-white font-bold text-xs">6 × 5 = 30 Items</span>
                </div>
                <div id="sim4_row_sports" class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center opacity-60">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">⚽ Sports Gear</span>
                        <span class="text-emerald-400 text-sm">⭐⭐⭐⭐⭐⭐⭐⭐</span>
                    </div>
                    <span class="text-white font-bold text-xs">8 × 5 = 40 Items</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Total Shop Stock:</span>
                <span class="text-amber-300 font-bold">20 + 30 + 40 = 90 Items (18 Icons)</span>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">🔄 Custom Scale Transformer</span>
                <span id="sim5_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Scale: 1 = 10</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Switch the scale factor to observe how icon counts change while inventory remains fixed:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim5SetScale(5)" id="sim5_btn_5" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Scale 1 = 5</button>
                <button onclick="sim5SetScale(10)" id="sim5_btn_10" class="flex-1 py-1 rounded bg-teal-600 text-white font-bold transition">Scale 1 = 10</button>
                <button onclick="sim5SetScale(2)" id="sim5_btn_2" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Scale 1 = 2</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="space-y-1.5">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <span>🧸 Toys (20 Items):</span>
                    <span id="sim5_disp_toys" class="text-teal-300 font-bold text-sm">⭐⭐ (2 Icons)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <span>🎲 Games (30 Items):</span>
                    <span id="sim5_disp_games" class="text-teal-300 font-bold text-sm">⭐⭐⭐ (3 Icons)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <span>⚽ Sports (40 Items):</span>
                    <span id="sim5_disp_sports" class="text-teal-300 font-bold text-sm">⭐⭐⭐⭐ (4 Icons)</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Total Icons Required:</span>
                <span id="sim5_total_icons" class="text-emerald-400 font-bold">2 + 3 + 4 = 9 Icons</span>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">🛵 Two-Wheeler Roadside Traffic Tally</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Key: 1 🛵 = 3 Vehicles</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Inspect vehicle counts observed during morning rush hours across three days:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim6Inspect('mon')" id="sim6_btn_mon" class="flex-1 py-1 rounded bg-indigo-600 text-white font-bold transition">Monday (5 🛵)</button>
                <button onclick="sim6Inspect('wed')" id="sim6_btn_wed" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Wed (3 🛵)</button>
                <button onclick="sim6Inspect('fri')" id="sim6_btn_fri" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Friday (8 🛵)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="space-y-1.5" id="sim6_traffic_rows">
                <div id="sim6_row_mon" class="p-2 rounded bg-slate-800/80 border border-indigo-500/50 flex justify-between items-center">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Monday: 5 Icons</span>
                        <span class="text-amber-400 text-sm">🛵🛵🛵🛵🛵</span>
                    </div>
                    <span class="text-white font-bold text-xs">5 × 3 = 15 Vehicles</span>
                </div>
                <div id="sim6_row_wed" class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center opacity-60">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Wednesday: 3 Icons</span>
                        <span class="text-cyan-400 text-sm">🛵🛵🛵</span>
                    </div>
                    <span class="text-white font-bold text-xs">3 × 3 = 9 Vehicles</span>
                </div>
                <div id="sim6_row_fri" class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center opacity-60">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Friday: 8 Icons (Peak)</span>
                        <span class="text-emerald-400 text-sm">🛵🛵🛵🛵🛵🛵🛵🛵</span>
                    </div>
                    <span class="text-white font-bold text-xs">8 × 3 = 24 Vehicles</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>3-Day Combined Total:</span>
                <span class="text-emerald-400 font-bold">15 + 9 + 24 = 48 Vehicles</span>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-sky-400">🛺 Fractional Pictograph Re-scaling (Scale = 6)</span>
                <span id="sim7_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Full = 6 | Half = 3</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Observe how remainder quantities (3 vehicles) are encoded as fractional half-icons:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim7ToggleScale(6)" id="sim7_btn_scale6" class="flex-1 py-1 rounded bg-sky-600 text-white font-bold transition">Scale 1 = 6 (With Halves)</button>
                <button onclick="sim7ToggleScale(3)" id="sim7_btn_scale3" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Scale 1 = 3 (Original)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="space-y-1.5" id="sim7_display_area">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Monday (15 Vehicles):</span>
                        <span id="sim7_mon_icons" class="text-amber-300 text-sm font-bold">🛵🛵 🛺 (2½ Icons)</span>
                    </div>
                    <span id="sim7_mon_math" class="text-white text-xs">6 + 6 + 3 = 15</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Wednesday (9 Vehicles):</span>
                        <span id="sim7_wed_icons" class="text-cyan-300 text-sm font-bold">🛵 🛺 (1½ Icons)</span>
                    </div>
                    <span id="sim7_wed_math" class="text-white text-xs">6 + 3 = 9</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex justify-between items-center">
                    <div>
                        <span class="font-bold text-slate-200 block text-[11px]">Friday (24 Vehicles):</span>
                        <span id="sim7_fri_icons" class="text-emerald-300 text-sm font-bold">🛵🛵🛵🛵 (4 Icons)</span>
                    </div>
                    <span id="sim7_fri_math" class="text-white text-xs">6 × 4 = 24</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Peak vs Quietest Difference:</span>
                <span class="text-amber-400 font-bold">Friday - Wed = 24 - 9 = 15 Vehicles</span>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-purple-400">⏰ 24-Hour Icon Daily Schedule</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">1 Icon = 1 Hour</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click an activity category to highlight its dedicated hourly blocks across the day:</p>
            <div class="flex flex-wrap gap-1 mb-2">
                <button onclick="sim8Select('sleep')" id="sim8_btn_sleep" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold transition">Sleep (8h)</button>
                <button onclick="sim8Select('school')" id="sim8_btn_school" class="px-2 py-1 rounded bg-slate-800 text-amber-300 transition">School (6h)</button>
                <button onclick="sim8Select('study')" id="sim8_btn_study" class="px-2 py-1 rounded bg-slate-800 text-cyan-300 transition">Study (2h)</button>
                <button onclick="sim8Select('play')" id="sim8_btn_play" class="px-2 py-1 rounded bg-slate-800 text-emerald-300 transition">Play/Food (4h)</button>
                <button onclick="sim8Select('other')" id="sim8_btn_other" class="px-2 py-1 rounded bg-slate-800 text-rose-300 transition">Other (4h)</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="flex justify-between items-center text-[11px] mb-1">
                <span id="sim8_active_name" class="font-bold text-indigo-400">🛏️ Restful Sleep (8 Hours)</span>
                <span id="sim8_fraction" class="text-amber-300 font-bold">8 / 24 = 1/3 of Day</span>
            </div>
            <!-- 24 hourly icon blocks -->
            <div id="sim8_blocks_grid" class="grid grid-cols-6 sm:grid-cols-8 gap-1 p-2 bg-slate-950/80 rounded-lg border border-slate-800 text-center">
                <!-- Dynamically populated 24 hourly boxes -->
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-[10.5px] text-slate-300 flex justify-between items-center">
                <span>Total Budget Sum:</span>
                <span class="text-emerald-400 font-bold">8 + 6 + 2 + 4 + 4 = 24 Hours</span>
            </div>
        </div>
    </div>
    """
}


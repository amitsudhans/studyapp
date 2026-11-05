# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Chapter 13: Animal Jumps"""

sims_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-purple-400">⚙️ Multiplier Magic Box</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Multiplier: ×4</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select an input number to drop into the brass machine and see the product emerge:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim1SetInput(7)" id="sim1_btn_7" class="px-2.5 py-1 rounded bg-purple-600 text-white font-bold">7</button>
                <button onclick="sim1SetInput(9)" id="sim1_btn_9" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">9</button>
                <button onclick="sim1SetInput(12)" id="sim1_btn_12" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">12</button>
                <button onclick="sim1SetInput(15)" id="sim1_btn_15" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">15</button>
                <button onclick="sim1SetInput(18)" id="sim1_btn_18" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">18</button>
            </div>
            <button onclick="sim1DropToken()" id="sim1_drop_btn" class="w-full py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">Drop Token Into Machine ➔</button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim1_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Funnel Top -->
                    <polygon points="70,10 130,10 115,40 85,40" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                    <!-- Machine Body -->
                    <rect x="50" y="40" width="100" height="75" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
                    <!-- Gears -->
                    <circle cx="80" cy="75" r="14" fill="#312e81" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4,2"/>
                    <circle cx="120" cy="75" r="14" fill="#312e81" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4,2"/>
                    <text x="100" y="80" text-anchor="middle" font-size="12" font-weight="bold" fill="#facc15">× 4</text>
                    <!-- Output Chute -->
                    <polygon points="85,115 115,115 125,145 75,145" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                    <!-- Animated Token -->
                    <circle id="sim1_token" cx="100" cy="25" r="11" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
                    <text id="sim1_token_txt" x="100" y="29" text-anchor="middle" font-size="9" font-weight="bold" fill="#ffffff">7</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-purple-300 font-bold block mb-1">Mathematical Transformation:</span>
                    <div id="sim1_calc" class="text-amber-300 font-bold text-sm">7 × 4 = 28</div>
                    <div id="sim1_rel" class="text-[10px] text-slate-400 mt-1">28 is a multiple of 7 and 4.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Machine Output:</span>
                    <span id="sim1_out_val" class="text-emerald-400 font-bold text-base">28</span>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">📐 Factor Rectangle Studio</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Total Tiles: 12</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click a factor pair to reconfigure the 12 square tiles into different complete rectangles:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim2SetArray(1, 12)" id="sim2_btn_1_12" class="px-2.5 py-1 rounded bg-cyan-600 text-white font-bold">1 × 12</button>
                <button onclick="sim2SetArray(2, 6)" id="sim2_btn_2_6" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">2 × 6</button>
                <button onclick="sim2SetArray(3, 4)" id="sim2_btn_3_4" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">3 × 4</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800 h-36 overflow-auto">
                <svg id="sim2_svg" viewBox="0 0 200 120" class="w-48 h-28">
                    <!-- Dynamic Grid Tiles -->
                    <g id="sim2_grid"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold block mb-1">Dimensions & Divisors:</span>
                    <div id="sim2_desc" class="text-amber-300 font-bold">1 Row of 12 Tiles (1 × 12 = 12)</div>
                    <div class="text-[10px] text-slate-400 mt-1">Both 1 and 12 divide 12 with remainder 0.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold">All Factors of 12:</span>
                    <div class="text-slate-200 text-xs font-bold mt-0.5">{1, 2, 3, 4, 6, 12}</div>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🧱 Array Configurations Lab</span>
                <span id="sim3_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Square Array!</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Test different numbers of tiles to see if they form multiple rectangles, squares, or only primes:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim3SetNumber(10)" id="sim3_btn_10" class="px-2 py-1 rounded bg-slate-800 text-slate-200">10</button>
                <button onclick="sim3SetNumber(16)" id="sim3_btn_16" class="px-2 py-1 rounded bg-emerald-600 text-white font-bold">16 (Square)</button>
                <button onclick="sim3SetNumber(25)" id="sim3_btn_25" class="px-2 py-1 rounded bg-slate-800 text-slate-200">25 (Square)</button>
                <button onclick="sim3SetNumber(13)" id="sim3_btn_13" class="px-2 py-1 rounded bg-slate-800 text-slate-200">13 (Prime)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800 h-36">
                <svg id="sim3_svg" viewBox="0 0 160 120" class="w-40 h-28">
                    <g id="sim3_tiles"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-300 font-bold block mb-1" id="sim3_title">16 Tiles: 4 × 4 Square</span>
                    <div id="sim3_pairs" class="text-slate-300 text-[10px]">Pairs: 1×16, 2×8, 4×4</div>
                    <div id="sim3_nature" class="text-emerald-400 font-bold mt-1">Factors: {1, 2, 4, 8, 16} (5 Factors)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold">Geometric Insight:</span>
                    <span id="sim3_insight" class="text-slate-400 block text-[10px]">Identical factor (4×4) yields a perfect square!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔍 Prime & Composite Sieve</span>
                <span id="sim4_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">PRIME NUMBER</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a number to test all whole divisors and determine prime or composite status:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim4TestNumber(2)" id="sim4_btn_2" class="px-2 py-1 rounded bg-slate-800 text-slate-200">2</button>
                <button onclick="sim4TestNumber(9)" id="sim4_btn_9" class="px-2 py-1 rounded bg-slate-800 text-slate-200">9</button>
                <button onclick="sim4TestNumber(13)" id="sim4_btn_13" class="px-2 py-1 rounded bg-emerald-600 text-white font-bold">13</button>
                <button onclick="sim4TestNumber(14)" id="sim4_btn_14" class="px-2 py-1 rounded bg-slate-800 text-slate-200">14</button>
                <button onclick="sim4TestNumber(24)" id="sim4_btn_24" class="px-2 py-1 rounded bg-slate-800 text-slate-200">24</button>
                <button onclick="sim4TestNumber(37)" id="sim4_btn_37" class="px-2 py-1 rounded bg-slate-800 text-slate-200">37</button>
                <button onclick="sim4TestNumber(1)" id="sim4_btn_1" class="px-2 py-1 rounded bg-slate-800 text-slate-200">1</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 font-mono text-center">
                <div class="text-3xl font-extrabold text-amber-300 mb-1" id="sim4_num">13</div>
                <div class="text-[10px] text-slate-400">Total Factors Count: <span id="sim4_count" class="text-emerald-400 font-bold">2</span></div>
                <div class="mt-2 text-xs text-slate-300 font-bold" id="sim4_factor_list">Factors: {1, 13}</div>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Mathematical Classification:</span>
                    <div id="sim4_desc" class="text-emerald-300 font-bold">Prime Number (Exactly 2 Factors)</div>
                    <div id="sim4_sub" class="text-[10px] text-slate-400 mt-1">Divisible only by 1 and 13.</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold">Geometric Array:</span>
                    <span id="sim4_geom" class="text-slate-400 block text-[10px]">Forms only a 1 × 13 line strip.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🐰 Rabbit & 🐸 Frog Jumps</span>
                <span id="sim5_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Shared Landing: 12</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Animate animal leaps along the number line to find where both footprints overlap:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim5NextStep()" id="sim5_step_btn" class="flex-1 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition">Leap Next Step ➔</button>
                <button onclick="sim5Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
            <svg id="sim5_svg" viewBox="0 0 320 110" class="w-full h-28">
                <!-- Number line axis -->
                <line x1="10" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2"/>
                <!-- Ticks and labels (0 to 24) -->
                <g id="sim5_ticks"></g>
                <!-- Rabbit arcs (orange) -->
                <g id="sim5_rabbit_arcs"></g>
                <!-- Frog arcs (green) -->
                <g id="sim5_frog_arcs"></g>
                <!-- Positions -->
                <circle id="sim5_rabbit_pos" cx="10" cy="80" r="5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>
                <circle id="sim5_frog_pos" cx="10" cy="80" r="5" fill="#10b981" stroke="#ffffff" stroke-width="1.5"/>
            </svg>
            <div class="flex justify-between text-[11px] font-mono mt-1 pt-1 border-t border-slate-800 text-slate-300">
                <span class="text-amber-400">🐰 Rabbit (Step 4): Pos <strong id="sim5_r_pos">0</strong></span>
                <span class="text-emerald-400">🐸 Frog (Step 3): Pos <strong id="sim5_f_pos">0</strong></span>
                <span class="text-cyan-300">Overlap: <strong id="sim5_overlap">0</strong></span>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">🕷️ Spider & 🦗 Grasshopper Jumps</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">LCM = 6</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare Spider (3-step) and Grasshopper (6-step) to see why one jump size divides another:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim6Step()" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition">Advance Jumps ➔</button>
                <button onclick="sim6Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
            <svg id="sim6_svg" viewBox="0 0 320 110" class="w-full h-28">
                <line x1="10" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2"/>
                <g id="sim6_ticks"></g>
                <g id="sim6_spider_arcs"></g>
                <g id="sim6_grass_arcs"></g>
                <circle id="sim6_spider_pos" cx="10" cy="80" r="5" fill="#a855f7" stroke="#ffffff" stroke-width="1.5"/>
                <circle id="sim6_grass_pos" cx="10" cy="80" r="5" fill="#06b6d4" stroke="#ffffff" stroke-width="1.5"/>
            </svg>
            <div class="flex justify-between text-[11px] font-mono mt-1 pt-1 border-t border-slate-800 text-slate-300">
                <span class="text-purple-400">🕷️ Spider (3): Pos <strong id="sim6_s_pos">0</strong></span>
                <span class="text-cyan-400">🦗 Grasshopper (6): Pos <strong id="sim6_g_pos">0</strong></span>
                <span class="text-emerald-400">Shared: <strong id="sim6_shared">6, 12, 18, 24</strong></span>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">📊 Multiples Practice Explorer</span>
                <span id="sim7_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">LCM: 12</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a number pair to compute their multiples lists and locate common meeting points:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim7SelectPair(4, 6)" id="sim7_btn_4_6" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold">4 & 6</button>
                <button onclick="sim7SelectPair(8, 12)" id="sim7_btn_8_12" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">8 & 12</button>
                <button onclick="sim7SelectPair(6, 8)" id="sim7_btn_6_8" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">6 & 8</button>
                <button onclick="sim7SelectPair(9, 12)" id="sim7_btn_9_12" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">9 & 12</button>
            </div>
        </div>

        <div class="space-y-2 font-mono text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
                <span id="sim7_m1_label" class="text-amber-400 font-bold block mb-1">Multiples of 4:</span>
                <div id="sim7_m1_list" class="text-slate-300 text-[11px]">4, 8, 12, 16, 20, 24, 28, 32, 36...</div>
            </div>
            <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
                <span id="sim7_m2_label" class="text-cyan-400 font-bold block mb-1">Multiples of 6:</span>
                <div id="sim7_m2_list" class="text-slate-300 text-[11px]">6, 12, 18, 24, 30, 36, 42...</div>
            </div>
            <div class="bg-emerald-950/60 p-2 rounded-lg border border-emerald-500/40 text-emerald-300 flex justify-between items-center">
                <span>Least Common Multiple (LCM):</span>
                <span id="sim7_lcm" class="font-bold text-base text-amber-300">12</span>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🏁 Cobbled Road Race to Tile 64</span>
                <span id="sim8_winner" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Target: Tile 64</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Watch Racer A (step 4) and Racer B (step 6) sprint to tile 64. Who lands exactly on 64?</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim8RunRace()" id="sim8_btn_race" class="flex-1 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">Start Race to 64! ➔</button>
                <button onclick="sim8Reset()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Reset</button>
            </div>
        </div>

        <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
            <svg id="sim8_svg" viewBox="0 0 320 110" class="w-full h-28">
                <!-- Track 1: Racer A (4) -->
                <line x1="20" y1="40" x2="300" y2="40" stroke="#475569" stroke-width="2"/>
                <text x="15" y="25" font-size="8" fill="#f59e0b" font-weight="bold">🐰 Racer A (Step 4)</text>
                <circle id="sim8_r1" cx="20" cy="40" r="5" fill="#f59e0b"/>
                <!-- Target flag at 64 -->
                <line x1="280" y1="15" x2="280" y2="95" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
                <text x="280" y="12" text-anchor="middle" font-size="8" fill="#ef4444" font-weight="bold">🏁 64</text>
                <!-- Track 2: Racer B (6) -->
                <line x1="20" y1="80" x2="300" y2="80" stroke="#475569" stroke-width="2"/>
                <text x="15" y="65" font-size="8" fill="#38bdf8" font-weight="bold">🦌 Racer B (Step 6)</text>
                <circle id="sim8_r2" cx="20" cy="80" r="5" fill="#38bdf8"/>
            </svg>
            <div class="grid grid-cols-2 gap-2 text-[11px] font-mono mt-1 pt-1 border-t border-slate-800">
                <div class="text-amber-400">Racer A: <span id="sim8_t1_txt">Tile 0 (0 leaps)</span></div>
                <div class="text-cyan-400">Racer B: <span id="sim8_t2_txt">Tile 0 (0 leaps)</span></div>
            </div>
            <div id="sim8_result" class="text-center text-xs font-bold text-emerald-400 mt-1">Click Start to see who reaches tile 64!</div>
        </div>
    </div>
    """
}

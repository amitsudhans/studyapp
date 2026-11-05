# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
Simulators 1 to 8 (HTML & SVG interactive components)
"""

simulators_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥥 Coconut Orchard Grid & Fact Generator</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">N = D × Q</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust rows and columns of coconut crates to discover dual division facts from multiplication:</p>
            <div class="grid grid-cols-2 gap-3 mb-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Rows (Divisor D):</span>
                        <span id="sim1_rows_val" class="text-amber-400 font-mono font-bold">6</span>
                    </label>
                    <input id="sim1_rows_input" type="range" min="2" max="8" value="6" step="1" oninput="sim1Update()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Columns (Quotient Q):</span>
                        <span id="sim1_cols_val" class="text-cyan-400 font-mono font-bold">8</span>
                    </label>
                    <input id="sim1_cols_input" type="range" min="2" max="10" value="8" step="1" oninput="sim1Update()" class="w-full accent-cyan-400">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col items-center justify-center p-2 bg-slate-950/60 rounded-lg border border-slate-800 min-h-[140px] overflow-hidden">
                <div id="sim1_grid" class="grid gap-1 max-h-[130px] overflow-auto p-1"></div>
            </div>
            <div class="space-y-2">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                    <div class="text-slate-300">Total Coconuts (Dividend <span class="text-amber-300 font-bold">N</span>): <span id="sim1_n" class="text-emerald-400 font-bold text-sm">48</span></div>
                    <div class="text-cyan-300">Multiplication: <span id="sim1_mult">6 × 8 = 48</span></div>
                    <div class="text-amber-300">Division Fact 1: <span id="sim1_div1">48 ÷ 6 = 8</span></div>
                    <div class="text-indigo-300">Division Fact 2: <span id="sim1_div2">48 ÷ 8 = 6</span></div>
                </div>
                <div class="text-[10px] text-slate-400 bg-emerald-950/30 p-1.5 rounded border border-emerald-800/40">
                    💡 <strong>Inverse Relationship:</strong> Partitioning 48 into 6 rows gives 8 per row, while partitioning into 8 columns gives 6 per column!
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔺 Number Fact Triangle Studio</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Fact Families</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Pick a fact triangle or input your own factors to see the 1 multiplication and 2 division statements:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim2Set(9, 8)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">9 × 8 = 72</button>
                <button onclick="sim2Set(12, 7)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">12 × 7 = 84</button>
                <button onclick="sim2Set(15, 6)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">15 × 6 = 90</button>
                <button onclick="sim2Set(25, 4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">25 × 4 = 100</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center">
                <svg viewBox="0 0 180 150" class="w-44 h-36">
                    <!-- Triangle Outline -->
                    <polygon points="90,18 20,132 160,132" fill="#1e293b" stroke="#3b82f6" stroke-width="3" stroke-linejoin="round"/>
                    <!-- Top Peak Node (Product) -->
                    <circle cx="90" cy="22" r="18" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
                    <text id="sim2_peak" x="90" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">72</text>
                    <!-- Bottom Left Node -->
                    <circle cx="24" cy="130" r="16" fill="#06b6d4" stroke="#22d3ee" stroke-width="2"/>
                    <text id="sim2_left" x="24" y="134" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">9</text>
                    <!-- Bottom Right Node -->
                    <circle cx="156" cy="130" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
                    <text id="sim2_right" x="156" y="134" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">8</text>
                    <!-- Triangle center label -->
                    <text x="90" y="90" text-anchor="middle" font-size="16" font-weight="bold" fill="#64748b">×</text>
                    <!-- Side division symbols -->
                    <text x="50" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#94a3b8">÷</text>
                    <text x="130" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#94a3b8">÷</text>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-1.5 rounded bg-amber-950/40 border border-amber-800/40 text-amber-300">
                    <strong>Product at Apex:</strong> <span id="sim2_stat_prod">9 × 8 = 72</span>
                </div>
                <div class="p-1.5 rounded bg-cyan-950/40 border border-cyan-800/40 text-cyan-300">
                    <strong>Division Fact Left:</strong> <span id="sim2_stat_div1">72 ÷ 9 = 8</span>
                </div>
                <div class="p-1.5 rounded bg-emerald-950/40 border border-emerald-800/40 text-emerald-300">
                    <strong>Division Fact Right:</strong> <span id="sim2_stat_div2">72 ÷ 8 = 9</span>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">✂️ Trailing Zero Cancellation Station</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Zero Striking</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a division problem to watch equal trailing zeros get struck from Dividend and Divisor:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim3Set(150, 30)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">150 ÷ 30</button>
                <button onclick="sim3Set(4200, 70)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">4,200 ÷ 70</button>
                <button onclick="sim3Set(24000, 600)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">24,000 ÷ 600</button>
                <button onclick="sim3Set(75000, 750)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">75,000 ÷ 750</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="flex items-center justify-center gap-3 p-3 bg-slate-950/80 rounded-lg font-mono text-base">
                <div id="sim3_display" class="flex items-center gap-2">
                    <span id="sim3_num" class="text-amber-400 font-bold">4,200</span>
                    <span class="text-slate-400">÷</span>
                    <span id="sim3_den" class="text-cyan-400 font-bold">70</span>
                    <span class="text-slate-400">=</span>
                    <span id="sim3_ans" class="text-emerald-400 font-bold font-mono">60</span>
                </div>
            </div>
            <div id="sim3_explanation" class="p-2 rounded bg-slate-800/70 border border-slate-700 text-[11px] text-slate-300">
                Cancel 1 zero from each: 420 ÷ 7 = 60.
            </div>
            <div class="flex justify-center">
                <button onclick="sim3Animate()" class="px-4 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow">
                    ▶️ Animate Zero Cancellation
                </button>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚴 Rate & Bonus Distribution Calculator</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Uniform Partition</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Explore everyday rate division: Cyclist Tour Distance vs Farm Bonus Sharing:</p>
            <div class="flex gap-2 mb-2">
                <button id="sim4_mode_cycle" onclick="sim4SetMode('cycle')" class="px-3 py-1 rounded bg-amber-600 text-white font-bold">🚴 Cyclist Rally</button>
                <button id="sim4_mode_bonus" onclick="sim4SetMode('bonus')" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold">💰 Bonus Sharing</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-3">
            <div id="sim4_controls" class="space-y-2">
                <!-- Dynamic slider controls inserted by JS -->
            </div>
            <div class="p-2.5 rounded bg-slate-950/80 border border-slate-800 font-mono text-[11px] space-y-1">
                <div id="sim4_formula" class="text-cyan-300 font-bold">Daily Rate = Total Distance ÷ Number of Days</div>
                <div id="sim4_calculation" class="text-emerald-400 text-sm font-bold">400 km ÷ 5 days = 80 km/day</div>
                <div id="sim4_detail" class="text-slate-400 text-[10px]">The cyclist travels an equal distance of 80 km each day.</div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧩 Convenient Splitting Workshop</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Mental Decomposition</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Split difficult dividends into friendly multiples using addition or subtraction:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim5Set(1248, 6, 'add', 1200, 48)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1,248 ÷ 6 (Add)</button>
                <button onclick="sim5Set(1992, 4, 'sub', 2000, 8)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1,992 ÷ 4 (Sub)</button>
                <button onclick="sim5Set(3570, 7, 'add', 3500, 70)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">3,570 ÷ 7 (Add)</button>
                <button onclick="sim5Set(2970, 3, 'sub', 3000, 30)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">2,970 ÷ 3 (Sub)</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-3 gap-2 text-center font-mono">
                <div class="p-2 rounded bg-amber-950/40 border border-amber-800/40">
                    <span class="text-[10px] text-slate-400 block">Original Problem</span>
                    <span id="sim5_orig" class="text-amber-300 font-bold text-sm">1,248 ÷ 6</span>
                </div>
                <div class="p-2 rounded bg-indigo-950/40 border border-indigo-800/40">
                    <span class="text-[10px] text-slate-400 block">Friendly Parts</span>
                    <span id="sim5_split" class="text-indigo-300 font-bold text-sm">(1200 + 48) ÷ 6</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-[10px] text-slate-400 block">Combined Quotient</span>
                    <span id="sim5_result" class="text-emerald-300 font-bold text-sm">200 + 8 = 208</span>
                </div>
            </div>
            <div id="sim5_steps" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-[11px] text-slate-300 space-y-1">
                <div>Step 1: 1,200 ÷ 6 = 200</div>
                <div>Step 2: 48 ÷ 6 = 8</div>
                <div>Sum: 200 + 8 = 208</div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⚙️ Repeated Halving Machine</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Powers of 2</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Dividing by 4 is halving twice. Dividing by 8 is halving thrice. Test with numbers:</p>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold">Choose Divisor:</label>
                    <select id="sim6_divisor" onchange="sim6Update()" class="w-full mt-1 p-1.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-mono">
                        <option value="4">÷ 4 (Halve 2 times)</option>
                        <option value="8">÷ 8 (Halve 3 times)</option>
                    </select>
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold">Choose Number:</label>
                    <select id="sim6_number" onchange="sim6Update()" class="w-full mt-1 p-1.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-mono">
                        <option value="256">256</option>
                        <option value="512">512</option>
                        <option value="1024">1,024</option>
                        <option value="848">848</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div id="sim6_stages" class="flex items-center justify-around gap-1 font-mono text-[11px]">
                <!-- Populated dynamically: Start -> Halve 1 -> Halve 2 -> (Halve 3) -->
            </div>
            <div id="sim6_summary" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-center text-emerald-400 font-bold">
                256 ÷ 4 = 64 (Half: 128 ➔ Half: 64)
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🌴 Susie vs Sunitha: Partial Quotients Race</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">582 ÷ 6 = 97</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare Susie's cautious chunks (10s, 20s) with Sunitha's optimized leaps (90s) in Kerala:</p>
            <div class="flex gap-2 mb-2">
                <button id="sim7_tab_susie" onclick="sim7SetMethod('susie')" class="px-3 py-1 rounded bg-amber-600 text-white font-bold">🐢 Susie's Chunks (5 steps)</button>
                <button id="sim7_tab_sunitha" onclick="sim7SetMethod('sunitha')" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold">⚡ Sunitha's Leap (2 steps)</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Step</th>
                            <th class="p-1.5 border-b border-slate-700">Partial Quotient Chunk</th>
                            <th class="p-1.5 border-b border-slate-700">Subtracted</th>
                            <th class="p-1.5 border-b border-slate-700">Remaining Balance</th>
                        </tr>
                    </thead>
                    <tbody id="sim7_table_body" class="divide-y divide-slate-800">
                        <!-- Populated by JS -->
                    </tbody>
                </table>
            </div>
            <div id="sim7_total" class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40 font-mono text-center text-emerald-300 font-bold">
                Total Quotient = 97 coconuts per sack!
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⚖️ Fundamental Division Algorithm Balance</span>
                <span id="sim8_validity" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">R &lt; D Verified</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Verify the theorem: <strong>Dividend (N) = Divisor (D) × Quotient (Q) + Remainder (R)</strong>, with <strong>0 ≤ R &lt; D</strong>:</p>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Dividend (N):</span>
                        <span id="sim8_n_val" class="text-amber-400 font-mono font-bold">47</span>
                    </label>
                    <input id="sim8_n_input" type="range" min="10" max="99" value="47" step="1" oninput="sim8Update()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Divisor (D):</span>
                        <span id="sim8_d_val" class="text-cyan-400 font-mono font-bold">6</span>
                    </label>
                    <input id="sim8_d_input" type="range" min="2" max="12" value="6" step="1" oninput="sim8Update()" class="w-full accent-cyan-400">
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-3 gap-2 text-center font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Quotient (Q)</span>
                    <span id="sim8_q" class="text-cyan-300 font-bold text-base">7</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Remainder (R)</span>
                    <span id="sim8_r" class="text-amber-300 font-bold text-base">5</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Condition R &lt; D</span>
                    <span id="sim8_cond" class="text-emerald-400 font-bold text-base">5 &lt; 6 (Pass)</span>
                </div>
            </div>
            <div class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-center text-xs text-emerald-400">
                <span id="sim8_eqn">47 = 6 × 7 + 5</span>
            </div>
        </div>
    </div>
    """
}


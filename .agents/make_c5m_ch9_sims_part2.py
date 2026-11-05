# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
Simulators 9 to 16 (HTML & SVG interactive components)
"""

simulators_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚌 School Bus Excursion Fleet Allocator</span>
                <span id="sim9_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Ceiling Rounding</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Calculate buses needed when students exceed an exact multiple. Every child must have a seat:</p>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Total Students:</span>
                        <span id="sim9_students_val" class="text-amber-400 font-mono font-bold">248</span>
                    </label>
                    <input id="sim9_students_input" type="range" min="50" max="400" value="248" step="1" oninput="sim9Update()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Bus Capacity:</span>
                        <span id="sim9_capacity_val" class="text-cyan-400 font-mono font-bold">50</span>
                    </label>
                    <input id="sim9_capacity_input" type="range" min="20" max="60" value="50" step="5" oninput="sim9Update()" class="w-full accent-cyan-400">
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-3 gap-2 text-center font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Full Buses</span>
                    <span id="sim9_full" class="text-cyan-300 font-bold text-base">4</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Leftover Kids</span>
                    <span id="sim9_rem" class="text-amber-300 font-bold text-base">48</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-slate-400 block text-[10px]">Buses to Hire</span>
                    <span id="sim9_total_buses" class="text-emerald-300 font-bold text-base">5</span>
                </div>
            </div>
            <div id="sim9_explanation" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-center text-xs text-slate-300">
                248 ÷ 50 = 4 remainder 48. Because 48 children cannot be left behind, you must hire 5 buses!
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥥 Kalpavruksha Coconut Oil Mill & Revenue Ledger</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Commercial Math</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">In Kerala, 8 coconuts yield 1 litre of pure virgin coconut oil. Trace the conversion and income:</p>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Harvested Coconuts:</span>
                        <span id="sim10_nuts_val" class="text-amber-400 font-mono font-bold">4,376</span>
                    </label>
                    <input id="sim10_nuts_input" type="range" min="800" max="8000" value="4376" step="8" oninput="sim10Update()" class="w-full accent-amber-400">
                </div>
                <div>
                    <label class="text-[11px] text-slate-400 font-semibold flex justify-between">
                        <span>Selling Price per Litre:</span>
                        <span id="sim10_price_val" class="text-emerald-400 font-mono font-bold">₹240</span>
                    </label>
                    <input id="sim10_price_input" type="range" min="150" max="350" value="240" step="10" oninput="sim10Update()" class="w-full accent-emerald-400">
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-3 gap-2 text-center font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Ratio</span>
                    <span class="text-cyan-300 font-bold text-base">8 : 1 L</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Oil Extracted</span>
                    <span id="sim10_litres" class="text-amber-300 font-bold text-base">547 L</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-slate-400 block text-[10px]">Total Revenue</span>
                    <span id="sim10_revenue" class="text-emerald-300 font-bold text-base">₹1,31,280</span>
                </div>
            </div>
            <div id="sim10_breakdown" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-center text-xs text-slate-300">
                4,376 ÷ 8 = 547 Litres. 547 L × ₹240 = ₹1,31,280!
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📦 Two-Digit Divisor Estimator</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Trial Multiplier</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Round the 2-digit divisor to the nearest 10 to estimate trial quotient digits cleanly:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim11Set(9913, 23)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Husk Bales: 9,913 ÷ 23</button>
                <button onclick="sim11Set(8890, 35)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Tender Crates: 8,890 ÷ 35</button>
                <button onclick="sim11Set(7488, 48)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Farm Seedlings: 7,488 ÷ 48</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-2 gap-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Exact Division</span>
                    <span id="sim11_exact" class="text-cyan-300 font-bold text-sm">9,913 ÷ 23</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Rounded Estimate</span>
                    <span id="sim11_est" class="text-amber-300 font-bold text-sm">10,000 ÷ 20 ≈ 500</span>
                </div>
            </div>
            <div id="sim11_steps" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-xs text-slate-300 space-y-1">
                <div>99 ÷ 23: 23 × 4 = 92 (Remainder 7)</div>
                <div>Bring down 1 ➔ 71 ÷ 23: 23 × 3 = 69 (Remainder 2)</div>
                <div>Bring down 3 ➔ 23 ÷ 23 = 1</div>
                <div class="text-emerald-400 font-bold">Exact Quotient: 431 bales (Remainder: 0)</div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🪜 4-Step Long Division Cycle Animator</span>
                <span id="sim12_step_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Step 1: Divide</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Walk through the eternal 4-step rhythm: <strong>Divide ➔ Multiply ➔ Subtract ➔ Bring down</strong>:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim12Prev()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold">◀ Step Back</button>
                <button onclick="sim12Next()" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow">Next Step ▶</button>
                <button onclick="sim12Reset()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700">Reset</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center font-mono text-base p-2 bg-slate-950/80 rounded-lg border border-slate-800">
                <div id="sim12_bracket" class="text-slate-200 leading-relaxed text-sm">
                    <!-- Dynamic vertical long division bracket -->
                </div>
            </div>
            <div class="space-y-2">
                <div class="p-2 rounded bg-indigo-950/40 border border-indigo-800/40 font-mono text-[11px]">
                    <div id="sim12_action_title" class="text-indigo-300 font-bold mb-1">Step 1: Divide</div>
                    <div id="sim12_action_desc" class="text-slate-300">Divide 7 into 43. 7 × 6 = 42. Write 6 on top.</div>
                </div>
                <div class="flex items-center justify-around text-center text-[10px] font-bold">
                    <span id="sim12_badge_d" class="p-1 px-2 rounded bg-cyan-600 text-white">1. Divide</span>
                    <span id="sim12_badge_m" class="p-1 px-2 rounded bg-slate-800 text-slate-400">2. Multiply</span>
                    <span id="sim12_badge_s" class="p-1 px-2 rounded bg-slate-800 text-slate-400">3. Subtract</span>
                    <span id="sim12_badge_b" class="p-1 px-2 rounded bg-slate-800 text-slate-400">4. Bring Down</span>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🕵️ Zero Quotient Trap Detective</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Never Skip 0!</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">When a brought-down digit is smaller than the divisor, you MUST write 0 in the quotient:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim13Set(3005, 5)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">3,005 ÷ 5 = 601 (Not 61!)</button>
                <button onclick="sim13Set(4016, 4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">4,016 ÷ 4 = 1,004 (Not 14!)</button>
                <button onclick="sim13Set(6024, 6)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">6,024 ÷ 6 = 1,004 (Not 14!)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700">
            <div class="p-2.5 rounded bg-rose-950/30 border border-rose-800/40 font-mono text-[11px] space-y-1">
                <div class="text-rose-400 font-bold flex items-center gap-1">
                    <span>❌ The Fatal Trap:</span>
                </div>
                <div id="sim13_wrong" class="text-slate-300">
                    Skipping 0 in 3,005 ÷ 5 gives 61.<br>
                    Check: 61 × 5 = 305 (Off by 2,700!)
                </div>
            </div>
            <div class="p-2.5 rounded bg-emerald-950/30 border border-emerald-800/40 font-mono text-[11px] space-y-1">
                <div class="text-emerald-400 font-bold flex items-center gap-1">
                    <span>✅ Correct Place Value:</span>
                </div>
                <div id="sim13_right" class="text-slate-300">
                    3,005 ÷ 5 = 601.<br>
                    Check: 601 × 5 = 3,005 (Exact match!)
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔨 Carpenter Workshop Bottleneck Analyzer</span>
                <span id="sim14_bottleneck" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Bottleneck: Clips</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Each wooden packing crate requires 4 panels, 8 clips, and 16 screws. What limits output?</p>
            <div class="grid grid-cols-3 gap-2 mb-2 font-mono">
                <div>
                    <label class="text-[10px] text-slate-400">Panels (÷4):</label>
                    <input id="sim14_panels" type="number" value="120" min="20" max="500" step="10" oninput="sim14Update()" class="w-full p-1 rounded bg-slate-800 border border-slate-700 text-amber-300 text-center">
                </div>
                <div>
                    <label class="text-[10px] text-slate-400">Clips (÷8):</label>
                    <input id="sim14_clips" type="number" value="200" min="20" max="800" step="10" oninput="sim14Update()" class="w-full p-1 rounded bg-slate-800 border border-slate-700 text-cyan-300 text-center">
                </div>
                <div>
                    <label class="text-[10px] text-slate-400">Screws (÷16):</label>
                    <input id="sim14_screws" type="number" value="480" min="50" max="1500" step="20" oninput="sim14Update()" class="w-full p-1 rounded bg-slate-800 border border-slate-700 text-emerald-300 text-center">
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-3 gap-2 text-center font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Panels Limit</span>
                    <span id="sim14_cap_panels" class="text-amber-300 font-bold text-sm">30 Crates</span>
                </div>
                <div class="p-2 rounded bg-rose-950/40 border border-rose-800/50">
                    <span class="text-rose-300 block text-[10px]">Clips Limit</span>
                    <span id="sim14_cap_clips" class="text-rose-300 font-bold text-sm">25 Crates</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <span class="text-slate-400 block text-[10px]">Screws Limit</span>
                    <span id="sim14_cap_screws" class="text-emerald-300 font-bold text-sm">30 Crates</span>
                </div>
            </div>
            <div id="sim14_summary" class="p-2 rounded bg-slate-950/80 border border-slate-800 font-mono text-center text-xs text-amber-300 font-bold">
                Maximum finished crates possible = 25 crates (limited by Clips).
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧾 Sabzi Mandi Vegetable Market Invoice Auditor</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Rate = Total ÷ Quantity</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Verify mandi wholesale invoices using division to find unit price per kilogram:</p>
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Produce</th>
                            <th class="p-1.5 border-b border-slate-700">Total Billed</th>
                            <th class="p-1.5 border-b border-slate-700">Quantity (kg)</th>
                            <th class="p-1.5 border-b border-slate-700">Calculated Rate/kg</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300">🥔 Potatoes</td>
                            <td class="p-1.5">₹720</td>
                            <td class="p-1.5">40 kg</td>
                            <td class="p-1.5 text-emerald-400 font-bold">₹720 ÷ 40 = ₹18/kg</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-red-400">🍅 Tomatoes</td>
                            <td class="p-1.5">₹1,125</td>
                            <td class="p-1.5">25 kg</td>
                            <td class="p-1.5 text-emerald-400 font-bold">₹1,125 ÷ 25 = ₹45/kg</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-emerald-300">🧅 Onions</td>
                            <td class="p-1.5">₹1,440</td>
                            <td class="p-1.5">48 kg</td>
                            <td class="p-1.5 text-emerald-400 font-bold">₹1,440 ÷ 48 = ₹30/kg</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="bg-slate-900/60 p-2.5 rounded-xl border border-slate-700 font-mono text-[11px] space-y-1 text-slate-300">
            <div class="text-cyan-300 font-bold">💡 Core Mandi Formulas:</div>
            <div>• Unit Rate (₹/kg) = Total Cost (₹) ÷ Quantity (kg)</div>
            <div>• Quantity Bought (kg) = Total Cost (₹) ÷ Unit Rate (₹/kg)</div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⚖️ Mathematical Truth & Statement Classifier</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Logic & Truth</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Test algebraic statements to classify them as <strong>Always True</strong>, <strong>Sometimes True</strong>, or <strong>Never True</strong>:</p>
            <div class="space-y-2">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex items-center justify-between">
                    <span class="font-mono text-slate-200">1. a ÷ b = b ÷ a (Commutativity)</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Sometimes True (only if a=b)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex items-center justify-between">
                    <span class="font-mono text-slate-200">2. In N = D × Q + R, R &lt; D</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Always True</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex items-center justify-between">
                    <span class="font-mono text-slate-200">3. A number divided by 0 equals 0</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400 border border-red-500/30">Never True (Undefined)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 flex items-center justify-between">
                    <span class="font-mono text-slate-200">4. 0 divided by any non-zero number is 0</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Always True</span>
                </div>
            </div>
        </div>
    </div>
    """
}


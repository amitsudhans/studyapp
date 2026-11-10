# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Coach Allocation Remainders</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">324 Children ÷ 15 Seats = 21 R 9</span>
    </div>

    <!-- Long Division Step-by-Step Visualization -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 font-mono text-xs">
        <div class="flex justify-between items-center text-slate-400">
            <span>Total Visiting Students: <strong class="text-white text-sm">324</strong></span>
            <span>Coach Capacity: <strong class="text-orange-400 text-sm">15</strong></span>
        </div>

        <!-- Long Division Box -->
        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 flex flex-col items-center">
            <div class="w-64 space-y-1">
                <div class="text-right text-emerald-400 font-bold text-sm">Quotient: 21 Coaches</div>
                <div class="flex items-center border-t-2 border-slate-700 pt-1">
                    <span class="w-12 text-orange-400 font-bold">15 )</span>
                    <span class="font-bold text-white text-sm">324</span>
                </div>
                <div class="text-right text-slate-400">- 300 <span class="text-[10px] text-slate-500">(15 × 20)</span></div>
                <div class="border-t border-slate-700 text-right text-white">24</div>
                <div class="text-right text-slate-400">- 15 <span class="text-[10px] text-slate-500">(15 × 1)</span></div>
                <div class="border-t border-slate-700 text-right text-amber-400 font-bold">Remainder: 9 Children</div>
            </div>
        </div>

        <!-- Practical Real-World Verdict -->
        <div class="bg-orange-950/40 border border-orange-800/60 p-3 rounded-lg space-y-1 text-slate-200">
            <div class="flex items-center justify-between text-xs font-bold">
                <span class="text-orange-300">Station Master Allocation Rule:</span>
                <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Total: 22 Coaches</span>
            </div>
            <p class="text-[11px] text-slate-300 leading-relaxed font-sans">
                21 full coaches hold 315 children. The remaining 9 children cannot be left behind on the platform! Exactly <strong>22 coaches</strong> must be ordered so everyone gets a seat.
            </p>
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Multiplication & Division Drill</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Standard Algorithms & Verification</span>
    </div>

    <!-- Toggle Drill Mode -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setDrillMode('mult')" id="drill-btn-mult" class="px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition">
            ✖ 2-Digit Multiplication (24 × 36)
        </button>
        <button onclick="setDrillMode('div')" id="drill-btn-div" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition">
            ➗ Long Division (478 ÷ 8)
        </button>
    </div>

    <!-- Algorithm Stepper View -->
    <div id="drill-container" class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs flex justify-center">
        <!-- Injected via setDrillMode -->
    </div>

    <div id="drill-verification-box" class="bg-slate-800/40 p-3 rounded-xl border border-slate-800 text-xs font-mono text-slate-300">
        Verification Formula: <strong>Dividend = (Divisor × Quotient) + Remainder</strong>
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Hundreds Scaling Patterns</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Multiples of 100 & Trailing Zeroes</span>
    </div>

    <!-- Interactive Problem Presets -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setHundredsProblem(2, 100)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">2 × 100</button>
        <button onclick="setHundredsProblem(11, 200)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">11 × 200</button>
        <button onclick="setHundredsProblem(80, 50)" class="px-2.5 py-1 rounded bg-purple-600 text-white font-bold">80 × 50</button>
        <button onclick="setHundredsProblem(15, 300)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">15 × 300</button>
    </div>

    <!-- Decomposition Visualizer -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 font-mono text-xs">
        <div class="flex justify-between items-center text-slate-300">
            <span>Expression: <strong id="h-prob-str" class="text-white text-base font-bold">80 × 50</strong></span>
            <span id="h-zero-count-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">2 Decade Zeroes</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Step 1: Single-Digit Multiplication</span>
                <div id="h-step1-res" class="text-sm font-bold text-amber-400 mt-1">8 × 5 = 40</div>
                <div class="text-[10px] text-slate-400">Notice 40 already has a zero!</div>
            </div>
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Step 2: Append Trailing Zeroes</span>
                <div id="h-step2-res" class="text-sm font-bold text-purple-300 mt-1">40 × 100 = 4,000</div>
                <div class="text-[10px] text-emerald-400 font-bold">Final Product: 4,000</div>
            </div>
        </div>
    </div>

    <div class="text-center text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-xl border border-slate-800">
        Common Student Trap: 8 × 5 makes 40. Appending two zeroes produces <strong>4,000</strong> (not 400)!
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Dividing Tens & Hundreds</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Grain Depot Packaging Logistics</span>
    </div>

    <!-- Depot Packaging Selector -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs font-mono">
        <button onclick="setPackCase(1)" id="pack-btn-1" class="p-2.5 rounded-xl border bg-teal-600/20 border-teal-500 text-teal-300 font-bold text-left transition">
            Case 1: 750 kg in 10 kg sacks
        </button>
        <button onclick="setPackCase(2)" id="pack-btn-2" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white">
            Case 2: 2,400 kg in 100 kg crates
        </button>
        <button onclick="setPackCase(3)" id="pack-btn-3" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white">
            Case 3: 846 kg in 100 kg crates
        </button>
    </div>

    <!-- Packaging Breakdown Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="flex justify-between items-center text-slate-400">
            <span>Division Calculation: <strong id="pack-eq-str" class="text-white">750 ÷ 10</strong></span>
            <span id="pack-status-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Exact Packaging (R 0)</span>
        </div>
        <div class="grid grid-cols-2 gap-3 pt-1">
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Quotient (Full Bags)</span>
                <div id="pack-quot-res" class="text-lg font-bold text-teal-300 mt-1">75 Sacks</div>
            </div>
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400 uppercase">Remainder (Leftover)</span>
                <div id="pack-rem-res" class="text-lg font-bold text-amber-300 mt-1">0 kg Leftover</div>
            </div>
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Currency Denomination Puzzles</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Museum Ticket Payment: ₹685</span>
    </div>

    <!-- Target Amount Display -->
    <div class="flex justify-between items-center bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono">
        <span class="text-slate-400">Target Ticket Cost: <strong class="text-amber-400 text-base font-bold">₹685</strong></span>
        <span class="text-emerald-300 font-bold">5 Notes/Coins Total</span>
    </div>

    <!-- Denominations Breakdown Stack -->
    <div class="space-y-1.5 text-xs font-mono">
        <div class="flex items-center justify-between p-2 rounded-lg bg-amber-950/40 border border-amber-800/40">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-amber-600 text-white font-bold text-[10px]">₹200 Note</span>
                <span class="text-slate-200">3 Notes</span>
            </div>
            <span class="text-amber-300 font-bold">3 × ₹200 = ₹600</span>
        </div>
        <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950 border border-slate-800">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-emerald-700 text-white font-bold text-[10px]">₹50 Note</span>
                <span class="text-slate-200">1 Note</span>
            </div>
            <span class="text-emerald-300 font-bold">1 × ₹50 = ₹50</span>
        </div>
        <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950 border border-slate-800">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-red-700 text-white font-bold text-[10px]">₹20 Note</span>
                <span class="text-slate-200">1 Note</span>
            </div>
            <span class="text-red-300 font-bold">1 × ₹20 = ₹20</span>
        </div>
        <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950 border border-slate-800">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-indigo-700 text-white font-bold text-[10px]">₹10 Note</span>
                <span class="text-slate-200">1 Note</span>
            </div>
            <span class="text-indigo-300 font-bold">1 × ₹10 = ₹10</span>
        </div>
        <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950 border border-slate-800">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-yellow-600 text-white font-bold text-[10px]">₹5 Coin</span>
                <span class="text-slate-200">1 Coin</span>
            </div>
            <span class="text-yellow-300 font-bold">1 × ₹5 = ₹5</span>
        </div>
    </div>

    <div class="text-center text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 font-mono">
        Sum: <strong>₹600 + ₹50 + ₹20 + ₹10 + ₹5 = ₹685</strong> (Paid using exact minimal currency units)
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Multiplication Pattern Discovery</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Digital Roots & The 11s Trick</span>
    </div>

    <!-- Pattern Explorer Tabs -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setPatternMode('nines')" id="pat-btn-nines" class="px-3.5 py-1.5 rounded-xl bg-rose-600 text-white font-bold transition">
            The Magic of 9s (Digit Sum = 9)
        </button>
        <button onclick="setPatternMode('elevens')" id="pat-btn-elevens" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition">
            The 11s Split-Sum Trick
        </button>
    </div>

    <!-- Dynamic Pattern Demonstration Card -->
    <div id="pat-demo-card" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
        <!-- Injected via setPatternMode -->
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fleet Capacity Matching</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Multi-Modal Passenger Matching</span>
    </div>

    <!-- Interactive Vehicle Capacity Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-center text-xs font-mono border-collapse">
            <thead>
                <tr class="border-b border-slate-800 text-[10px] uppercase text-slate-400">
                    <th class="py-1.5 px-2 text-left">Vehicle Type</th>
                    <th class="py-1.5 px-2">Unit Rate</th>
                    <th class="py-1.5 px-2">Fleet Size</th>
                    <th class="py-1.5 px-2 text-cyan-400 font-bold">Total Capacity</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60">
                <tr>
                    <td class="py-2 px-2 text-left text-white">🚲 Bicycle</td>
                    <td class="py-2 px-2 text-slate-400">1 person</td>
                    <td class="py-2 px-2"><input type="number" id="fl-bike-n" value="10" min="0" max="50" onchange="recalcFleetCapacity()" class="w-12 bg-slate-800 border border-slate-700 text-white rounded text-center"></td>
                    <td id="fl-bike-tot" class="py-2 px-2 text-cyan-300 font-bold">10</td>
                </tr>
                <tr>
                    <td class="py-2 px-2 text-left text-white">🛺 Auto-Rickshaw</td>
                    <td class="py-2 px-2 text-slate-400">3 persons</td>
                    <td class="py-2 px-2"><input type="number" id="fl-auto-n" value="6" min="0" max="50" onchange="recalcFleetCapacity()" class="w-12 bg-slate-800 border border-slate-700 text-white rounded text-center"></td>
                    <td id="fl-auto-tot" class="py-2 px-2 text-cyan-300 font-bold">18</td>
                </tr>
                <tr>
                    <td class="py-2 px-2 text-left text-white">🚗 Passenger Car</td>
                    <td class="py-2 px-2 text-slate-400">5 persons</td>
                    <td class="py-2 px-2"><input type="number" id="fl-car-n" value="4" min="0" max="50" onchange="recalcFleetCapacity()" class="w-12 bg-slate-800 border border-slate-700 text-white rounded text-center"></td>
                    <td id="fl-car-tot" class="py-2 px-2 text-cyan-300 font-bold">20</td>
                </tr>
                <tr>
                    <td class="py-2 px-2 text-left text-white">🚐 Minibus</td>
                    <td class="py-2 px-2 text-slate-400">20 persons</td>
                    <td class="py-2 px-2"><input type="number" id="fl-bus-n" value="8" min="0" max="50" onchange="recalcFleetCapacity()" class="w-12 bg-slate-800 border border-slate-700 text-white rounded text-center"></td>
                    <td id="fl-bus-tot" class="py-2 px-2 text-cyan-300 font-bold">160</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Grand Fleet Total -->
    <div class="flex justify-between items-center bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono">
        <span class="text-slate-400">Combined Transit Fleet Capacity:</span>
        <strong id="fl-grand-total" class="text-base text-cyan-300 font-bold">208 Passengers</strong>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Transport Fleet Arithmetic</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">500 Visitors Transport Logistics</span>
    </div>

    <!-- Problem Breakdown Pipeline -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 font-mono text-xs">
        <div class="flex justify-between items-center text-slate-300">
            <span>Target Group: <strong class="text-white text-base">500 Visitors</strong></span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Mixed Fleet Coordination</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <!-- Phase 1: Minibuses -->
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-1">
                <span class="text-[10px] text-amber-400 uppercase font-bold">Step 1: 4 Minibuses (25 seats each)</span>
                <div class="text-sm font-bold text-white">4 × 25 = 100 Passengers</div>
                <div class="text-[10px] text-slate-400">Remaining: 500 - 100 = 400</div>
            </div>
            <!-- Phase 2: Electric Buses -->
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-1">
                <span class="text-[10px] text-cyan-400 uppercase font-bold">Step 2: 50-Seater Electric Buses</span>
                <div class="text-sm font-bold text-cyan-300">400 ÷ 50 = 8 Buses</div>
                <div class="text-[10px] text-emerald-400">Exactly 8 Electric Buses needed</div>
            </div>
        </div>

        <!-- Integrated Solution Summary -->
        <div class="bg-emerald-950/40 p-3 rounded-lg border border-emerald-800/60 text-slate-200">
            <strong>Optimal Fleet Deployment:</strong> 4 Minibuses (100 seats) + 8 Large Electric Buses (400 seats) = <strong>500 Total Seats</strong>.
        </div>
    </div>
</div>
"""

simulators_part2 = {9: sim9, 10: sim10, 11: sim11, 12: sim12, 13: sim13, 14: sim14, 15: sim15, 16: sim16}


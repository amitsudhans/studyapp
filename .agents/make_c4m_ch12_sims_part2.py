# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fractions Of Time</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Quarter, Half & Three-Quarter Hours</span>
    </div>

    <!-- Clock Face with Dynamic Sector Shading -->
    <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
        <div class="relative w-44 h-44">
            <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
                <!-- Clock Dial -->
                <circle cx="50" cy="50" r="46" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
                <!-- Dynamic Shaded Fraction Wedge -->
                <path id="frac-wedge-path" d="M 50 50 L 50 8 A 42 42 0 0 1 92 50 Z" fill="#ec4899" fill-opacity="0.35"/>
                <!-- Hour Markers -->
                <g font-size="6" font-weight="bold" fill="#cbd5e1" text-anchor="middle" dominant-baseline="central">
                    <text x="50" y="14">12</text>
                    <text x="86" y="50">3</text>
                    <text x="50" y="86">6</text>
                    <text x="14" y="50">9</text>
                </g>
                <!-- Center point -->
                <circle cx="50" cy="50" r="3" fill="#ffffff"/>
                <!-- Minute Hand pointing to current fraction -->
                <line id="frac-min-hand" x1="50" y1="50" x2="88" y2="50" stroke="#f472b6" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
        </div>

        <!-- Fraction Details Display -->
        <div class="space-y-2 text-xs w-full max-w-xs text-center sm:text-left">
            <span id="frac-badge" class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">
                1/4 Hour (Quarter Past)
            </span>
            <div id="frac-title" class="text-xl font-bold text-white">15 Minutes</div>
            <div class="space-y-1 font-mono text-[11px] text-slate-300 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
                <div id="frac-eq-str">Equation: 1/4 × 60 min = 15 min</div>
                <div id="frac-deg-str" class="text-pink-400">Angle: 90° arc on dial</div>
            </div>
        </div>
    </div>

    <!-- Fraction Toggles -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button onclick="setFractionSim(0.25, '1/4 Hour (Quarter Past)', 15, '1/4 × 60 min = 15 min', '90° arc on dial', 90)" class="p-2 rounded-xl bg-pink-600 text-white font-bold text-center">
            1/4 Hour (15m)
        </button>
        <button onclick="setFractionSim(0.5, '1/2 Hour (Half Past)', 30, '1/2 × 60 min = 30 min', '180° straight angle', 180)" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-center">
            1/2 Hour (30m)
        </button>
        <button onclick="setFractionSim(0.75, '3/4 Hour (Quarter To)', 45, '3/4 × 60 min = 45 min', '270° major arc', 270)" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-center">
            3/4 Hour (45m)
        </button>
        <button onclick="setFractionSim(1.0, 'Full Hour (Complete Turn)', 60, '1 × 60 min = 60 min', '360° full circle', 360)" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-center">
            1 Full Hour (60m)
        </button>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Clock Reading Errors</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Diagnostic Lab & Misconception Spotter</span>
    </div>

    <!-- Interactive Misconception Case Selector -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
        <button onclick="selectDiagCase(1)" id="diag-btn-1" class="p-2.5 rounded-xl border bg-red-600/20 border-red-500 text-red-300 font-bold text-left transition">
            Mistake 1: Hand on 7
        </button>
        <button onclick="selectDiagCase(2)" id="diag-btn-2" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white">
            Mistake 2: Approaching 6
        </button>
        <button onclick="selectDiagCase(3)" id="diag-btn-3" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-left transition hover:text-white">
            Mistake 3: Zero Confusion
        </button>
    </div>

    <!-- Diagnostic Comparison View -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <!-- The Common Mistake -->
        <div class="bg-red-950/30 border border-red-800/60 p-3.5 rounded-xl space-y-1.5">
            <div class="flex items-center gap-1.5 text-red-400 font-bold text-xs uppercase font-mono">
                <span>❌</span> Common Misconception
            </div>
            <div id="diag-wrong-text" class="text-sm font-bold text-red-200">"The minute hand points to 7, so it is 3:07."</div>
            <p id="diag-wrong-reason" class="text-[11px] text-slate-300 leading-relaxed">
                Reading the clock face digit literally as minutes instead of multiplying by 5.
            </p>
        </div>

        <!-- The Correct Mathematical Interpretation -->
        <div class="bg-emerald-950/30 border border-emerald-800/60 p-3.5 rounded-xl space-y-1.5">
            <div class="flex items-center gap-1.5 text-emerald-400 font-bold text-xs uppercase font-mono">
                <span>✅</span> Correct Mathematical Reading
            </div>
            <div id="diag-right-text" class="text-sm font-bold text-emerald-200">"Actual Time: 3:35 (7 × 5 = 35 minutes)"</div>
            <p id="diag-right-reason" class="text-[11px] text-slate-300 leading-relaxed">
                Each number from 1 to 12 represents a 5-minute interval: 7 × 5 = 35 minutes.
            </p>
        </div>
    </div>

    <div id="diag-tip-box" class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 text-xs text-slate-400 leading-relaxed">
        <strong>Teacher Diagnostic Tip:</strong> The minute hand traces sixty 1-minute steps. Always multiply the pointed digit by 5 to find elapsed minutes!
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Time Duration Tracking</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Study Log & Cumulative Duration</span>
    </div>

    <!-- Daily Study & Activity Schedule -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center pb-2 border-b border-slate-800 text-[11px] font-mono uppercase text-slate-400">
            <span>Subject / Activity</span>
            <span>Duration (Minutes)</span>
        </div>
        <div class="flex justify-between items-center">
            <span class="text-slate-200">📐 Joyful Mathematics</span>
            <span class="font-mono text-amber-400 font-bold">45 min</span>
        </div>
        <div class="flex justify-between items-center">
            <span class="text-slate-200">🔬 Environmental Studies</span>
            <span class="font-mono text-cyan-400 font-bold">50 min</span>
        </div>
        <div class="flex justify-between items-center">
            <span class="text-slate-200">📖 Story Reading & English</span>
            <span class="font-mono text-pink-400 font-bold">35 min</span>
        </div>
        <div class="flex justify-between items-center">
            <span class="text-slate-200">⚽ Physical Exercise & Play</span>
            <span class="font-mono text-emerald-400 font-bold">40 min</span>
        </div>
    </div>

    <!-- Regrouping Calculation Display -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 space-y-1">
            <span class="text-[10px] uppercase font-mono text-slate-400">Step 1: Total Raw Minutes</span>
            <div class="text-sm font-bold text-white font-mono">45 + 50 + 35 + 40 = 170 min</div>
            <div class="text-[11px] text-slate-400">Sum all durations directly.</div>
        </div>
        <div class="bg-amber-950/40 p-3 rounded-xl border border-amber-800/60 space-y-1">
            <span class="text-[10px] uppercase font-mono text-amber-400">Step 2: Base-60 Regrouping</span>
            <div class="text-base font-bold text-amber-200 font-mono">2 Hours 50 Minutes</div>
            <div class="text-[11px] text-slate-300">170 ÷ 60 = 2 hours remainder 50 min.</div>
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Railway Time Schedules</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Overnight Train Timetable & Midnight Reset</span>
    </div>

    <!-- Train Selector Tabs -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
        <button onclick="selectTrainSchedule('rajdhani')" id="train-btn-rajdhani" class="p-2 rounded-xl border bg-blue-600/20 border-blue-500 text-blue-300 font-bold text-center transition">
            🚆 Rajdhani Express
        </button>
        <button onclick="selectTrainSchedule('vande')" id="train-btn-vande" class="p-2 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-center transition hover:text-white">
            ⚡ Vande Bharat
        </button>
        <button onclick="selectTrainSchedule('mail')" id="train-btn-mail" class="p-2 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-center transition hover:text-white">
            🚂 Superfast Mail
        </button>
    </div>

    <!-- Timetable Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span id="train-name-tag" class="font-bold text-white text-sm">New Delhi - Mumbai Central Rajdhani</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-blue-500/20 text-blue-300">Overnight Express</span>
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400">Departure</span>
                <div id="train-dep-str" class="text-emerald-400 font-bold text-base mt-0.5">20:15</div>
                <span class="text-[10px] text-slate-500">(8:15 PM)</span>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400">Midnight Jump</span>
                <div class="text-amber-400 font-bold text-base mt-0.5">24:00 / 00:00</div>
                <span class="text-[10px] text-slate-500">Day Reset</span>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-[10px] text-slate-400">Arrival Next Day</span>
                <div id="train-arr-str" class="text-cyan-400 font-bold text-base mt-0.5">08:45</div>
                <span class="text-[10px] text-slate-500">(8:45 AM)</span>
            </div>
        </div>

        <!-- Overnight Calculation Breakdown -->
        <div id="train-calc-steps" class="text-xs bg-slate-900/60 p-3 rounded-lg border border-slate-800 text-slate-300 leading-relaxed font-mono">
            Phase 1: 20:15 to 24:00 = 3h 45m. Phase 2: 00:00 to 08:45 = 8h 45m.<br>
            Total Duration: 3h 45m + 8h 45m = 11h 90m = <strong class="text-white">12 Hours 30 Minutes</strong>.
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Shelf Life Inspection</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Grocery Inventory Quality Control Audit</span>
    </div>

    <!-- Audit Date Setting -->
    <div class="flex items-center justify-between bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-400 font-medium">Store Audit Date:</span>
        <input type="date" id="audit-date-input" value="2025-04-10" onchange="runShelfLifeAudit()" class="bg-slate-800 text-white px-2.5 py-1 rounded-lg border border-slate-700 font-mono text-xs focus:ring-1 focus:ring-orange-500">
    </div>

    <!-- Inventory Inspection Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
            <thead>
                <tr class="border-b border-slate-800 text-slate-400 font-mono uppercase text-[10px]">
                    <th class="py-2 px-2">Item</th>
                    <th class="py-2 px-2">MFG Date</th>
                    <th class="py-2 px-2">Shelf Life</th>
                    <th class="py-2 px-2">EXP Date</th>
                    <th class="py-2 px-2">Audit Verdict</th>
                </tr>
            </thead>
            <tbody id="shelf-audit-tbody" class="divide-y divide-slate-800 font-mono">
                <!-- Rows injected dynamically by JS -->
            </tbody>
        </table>
    </div>

    <div class="text-center text-xs text-slate-400 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
        Food safety rule: If Audit Date is beyond Expiry Date, the item must be immediately discarded.
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Days And Weeks</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Modular 7-Day Cycle & Calendar Jumps</span>
    </div>

    <!-- Interactive Calendar Jump Solver -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex flex-col sm:flex-row justify-between items-center gap-2 text-xs">
            <span class="text-slate-300">If the <strong class="text-cyan-400 font-bold">3rd</strong> of the month is a <strong class="text-emerald-400 font-bold">Sunday</strong>...</span>
            <button onclick="runCalendarJumps()" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs">Highlight All Sundays</button>
        </div>

        <!-- Mini Calendar Grid -->
        <div class="grid grid-cols-7 gap-1 text-center text-xs font-mono pt-2">
            <div class="text-red-400 font-bold text-[10px]">SUN</div>
            <div class="text-slate-400 font-bold text-[10px]">MON</div>
            <div class="text-slate-400 font-bold text-[10px]">TUE</div>
            <div class="text-slate-400 font-bold text-[10px]">WED</div>
            <div class="text-slate-400 font-bold text-[10px]">THU</div>
            <div class="text-slate-400 font-bold text-[10px]">FRI</div>
            <div class="text-slate-400 font-bold text-[10px]">SAT</div>
            <!-- Days 1 to 31 injected dynamically with Sundays highlighted -->
            <div id="cal-grid-cells" class="contents"></div>
        </div>

        <!-- 7-Day Arithmetic Formula -->
        <div class="bg-slate-900/60 p-3 rounded-lg border border-slate-800 text-xs font-mono space-y-1">
            <span class="text-slate-400 uppercase text-[10px]">7-Day Modulo Leap Pattern:</span>
            <div class="text-cyan-300 font-bold">3 + 7 = 10, 10 + 7 = 17, 17 + 7 = 24, 24 + 7 = 31</div>
            <div class="text-[11px] text-slate-400">All dates with difference of multiple of 7 share the exact same weekday!</div>
        </div>
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-violet-500/20 text-violet-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Century Leap Rules</h3>
        </div>
        <span class="text-xs text-violet-400 font-medium">The 400-Year Century Exception Rule</span>
    </div>

    <!-- Century Year Selection Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="testCenturyYear(1600)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">1600</button>
        <button onclick="testCenturyYear(1700)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">1700</button>
        <button onclick="testCenturyYear(1800)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">1800</button>
        <button onclick="testCenturyYear(1900)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">1900</button>
        <button onclick="testCenturyYear(2000)" class="px-2.5 py-1 rounded bg-violet-600 text-white font-bold font-mono">2000</button>
        <button onclick="testCenturyYear(2100)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">2100</button>
        <button onclick="testCenturyYear(2400)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono">2400</button>
    </div>

    <!-- Century Year Two-Step Verification Card -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 text-xs">
        <div class="flex justify-between items-center">
            <span class="text-slate-400 font-medium">Testing Century Year: <strong id="cent-val" class="text-white text-base font-mono">2000</strong></span>
            <span id="cent-status-pill" class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                LEAP CENTURY (366 Days)
            </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 font-mono">
            <!-- Step 1: Divisible by 4 -->
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-1">
                <span class="text-[10px] text-slate-400 uppercase">Check 1: Divisible by 4?</span>
                <div id="cent-chk1-math" class="text-indigo-300 font-bold">2000 ÷ 4 = 500 (R 0)</div>
                <div class="text-[11px] text-emerald-400">Passes standard leap rule</div>
            </div>

            <!-- Step 2: Century 400 Rule -->
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-1">
                <span class="text-[10px] text-slate-400 uppercase">Check 2: Divisible by 400?</span>
                <div id="cent-chk2-math" class="text-violet-300 font-bold">2000 ÷ 400 = 5 (R 0)</div>
                <div id="cent-chk2-res" class="text-[11px] text-emerald-400">Divisible by 400! February has 29 days.</div>
            </div>
        </div>

        <div id="cent-expl-note" class="text-[11px] text-slate-400 bg-slate-900/50 p-2.5 rounded-lg border border-slate-800/80 leading-relaxed">
            Because a solar year is slightly less than 365.25 days (approx 365.2422 days), 3 leap days must be eliminated every 400 years. Only century years divisible by 400 keep February 29!
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Time Arithmetic Logic</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Base-60 Regrouping & Column Arithmetic</span>
    </div>

    <!-- Mode Selector: Addition vs Subtraction -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setTimeArithMode('add')" id="arith-mode-add" class="px-4 py-1.5 rounded-xl bg-emerald-600 text-white font-bold transition">
            ➕ Time Addition (Carry 60 min as 1 hr)
        </button>
        <button onclick="setTimeArithMode('sub')" id="arith-mode-sub" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition">
            ➖ Time Subtraction (Borrow 1 hr as 60 min)
        </button>
    </div>

    <!-- Column Arithmetic Visualizer -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-center">
        <div class="w-72 font-mono text-sm space-y-2">
            <!-- Headers -->
            <div class="grid grid-cols-2 text-center text-xs text-slate-400 uppercase font-bold border-b border-slate-800 pb-1">
                <span>Hours</span>
                <span>Minutes</span>
            </div>

            <!-- Row 1 -->
            <div class="grid grid-cols-2 text-center text-white font-bold py-1">
                <span id="arith-r1-h">3 hr</span>
                <span id="arith-r1-m">45 min</span>
            </div>

            <!-- Row 2 with Operator -->
            <div class="grid grid-cols-2 text-center text-white font-bold py-1 relative">
                <span id="arith-op" class="absolute -left-4 text-emerald-400 font-black text-base">+</span>
                <span id="arith-r2-h">2 hr</span>
                <span id="arith-r2-m">35 min</span>
            </div>

            <!-- Total Bar -->
            <div class="border-t-2 border-slate-700 pt-2 grid grid-cols-2 text-center">
                <div>
                    <span id="arith-res-h" class="text-base font-black text-emerald-300">6 hr</span>
                    <div id="arith-sub-h" class="text-[10px] text-slate-400">(3 + 2 + 1)</div>
                </div>
                <div>
                    <span id="arith-res-m" class="text-base font-black text-emerald-300">20 min</span>
                    <div id="arith-sub-m" class="text-[10px] text-amber-400">(80m - 60m)</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Regrouping Explanation Step -->
    <div id="arith-step-expl" class="text-xs bg-slate-950/60 p-3 rounded-xl border border-slate-800 text-slate-300 leading-relaxed font-mono">
        Minutes: 45 + 35 = 80 min. Since 80 ≥ 60, we regroup 60 min into +1 hour. Remaining minutes = 80 - 60 = 20 min. Hours: 3 + 2 + 1 = 6 hours. Final Result = <strong>6 Hours 20 Minutes</strong>.
    </div>
</div>
"""

simulators_part2 = {9: sim9, 10: sim10, 11: sim11, 12: sim12, 13: sim13, 14: sim14, 15: sim15, 16: sim16}

# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 7: The Cleanest Village
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Snack Bill & Piggy Bank Savings</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Addition with Regrouping</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setSnackExpenseMode('pusaw')" id="btn-snack-pusaw" class="snack-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition">Pusaw & Tea (₹38 + ₹16)</button>
        <button onclick="setSnackExpenseMode('piggy')" id="btn-snack-piggy" class="snack-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Piggy Bank (₹185 + ₹125)</button>
    </div>

    <!-- Snack & Savings SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="snackExpenseSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Left Visual Container (Pusaw / Coin jar) -->
            <rect x="40" y="25" width="120" height="120" rx="8" fill="#14532d" fill-opacity="0.3" stroke="#22c55e" stroke-width="2"/>
            <text id="snackIcon" x="100" y="75" font-size="34" text-anchor="middle">🥮</text>
            <text id="snackLabel" x="100" y="110" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Khasi Red Rice Cake</text>
            <text id="snackSubLabel" x="100" y="128" fill="#fef08a" font-size="10" text-anchor="middle">₹38 Cake + ₹16 Tea</text>

            <!-- Right Calculation Container -->
            <rect x="180" y="25" width="140" height="120" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            <g id="snackMathGroup">
                <text x="250" y="50" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">¹ (carry)</text>
                <text x="225" y="75" fill="#ffffff" font-size="16" font-weight="bold">38</text>
                <text x="200" y="98" fill="#38bdf8" font-size="16" font-weight="black">+</text>
                <text x="225" y="98" fill="#ffffff" font-size="16" font-weight="bold">16</text>
                <line x1="200" y1="108" x2="270" y2="108" stroke="#64748b" stroke-width="2"/>
                <text x="225" y="132" fill="#34d399" font-size="19" font-weight="black">₹54</text>
            </g>
        </svg>

        <div id="snackExpenseDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            8 + 6 = 14 (write 4, carry 1 Ten); 1 + 3 + 1 = 5 Tens. Total bill: <span class="text-emerald-400 font-bold">₹54</span>.
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Snack Choice Differences</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">83 Pusaw vs 46 Fruit Plates</span>
    </div>

    <!-- Borrowing Step Buttons -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setSnackDiffStep('problem')" id="btn-diff-1" class="diff-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Step 1: 83 - 46 Setup</button>
        <button onclick="setSnackDiffStep('borrowed')" id="btn-diff-2" class="diff-btn px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition">Step 2: Borrow 1 Ten (13 - 6)</button>
    </div>

    <!-- Subtraction with Borrowing SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="snackDiffSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Left Comparison Bars -->
            <text x="30" y="40" fill="#86efac" font-size="10" font-weight="bold">83 Pusaw Cakes</text>
            <rect x="30" y="48" width="166" height="20" rx="3" fill="#16a34a"/>

            <text x="30" y="90" fill="#fbcfe8" font-size="10" font-weight="bold">46 Fruit Plates</text>
            <rect x="30" y="98" width="92" height="20" rx="3" fill="#ec4899"/>

            <!-- Difference bracket -->
            <line x1="122" y1="125" x2="196" y2="125" stroke="#fbbf24" stroke-width="2"/>
            <text x="159" y="142" fill="#fde047" font-size="11" font-weight="extrabold" text-anchor="middle">Diff: 37</text>

            <!-- Right Column Subtraction Box -->
            <rect x="220" y="20" width="110" height="135" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            <g id="snackDiffColGroup">
                <!-- Regrouped numbers on top -->
                <text x="250" y="42" fill="#f59e0b" font-size="11" font-weight="extrabold">⁷</text>
                <text x="280" y="42" fill="#f59e0b" font-size="11" font-weight="extrabold">¹³</text>
                
                <text x="250" y="68" fill="#ffffff" font-size="18" font-weight="bold">8</text>
                <text x="280" y="68" fill="#ffffff" font-size="18" font-weight="bold">3</text>

                <text x="232" y="92" fill="#ef4444" font-size="18" font-weight="black">-</text>
                <text x="250" y="92" fill="#ffffff" font-size="18" font-weight="bold">4</text>
                <text x="280" y="92" fill="#ffffff" font-size="18" font-weight="bold">6</text>

                <line x1="230" y1="104" x2="310" y2="104" stroke="#64748b" stroke-width="2"/>

                <text x="250" y="130" fill="#34d399" font-size="20" font-weight="black">3</text>
                <text x="280" y="130" fill="#34d399" font-size="20" font-weight="black">7</text>
            </g>
        </svg>

        <div id="snackDiffDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Cannot take 6 from 3. Borrow 1 Ten: 13 - 6 = 7 Ones; 7 - 4 = 3 Tens. Difference = <span class="text-amber-400 font-bold">37 students</span>.
        </div>
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Regrouping In Subtraction</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Double Borrowing (324 - 176)</span>
    </div>

    <!-- Step Controls -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="setSubStep(1)" id="btn-substep-1" class="substep-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Step 1: Borrow to Ones</button>
        <button onclick="setSubStep(2)" id="btn-substep-2" class="substep-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Step 2: Borrow to Tens</button>
        <button onclick="setSubStep(3)" id="btn-substep-3" class="substep-btn px-2.5 py-1.5 rounded-xl bg-red-500 text-white font-bold text-xs shadow transition">Step 3: Complete (148)</button>
    </div>

    <!-- Column Subtraction SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="columnSubSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <rect x="90" y="15" width="180" height="140" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            
            <g id="colSubTextGroup">
                <!-- Place Value Labels -->
                <text x="135" y="38" fill="#64748b" font-size="11" font-weight="bold">H</text>
                <text x="175" y="38" fill="#64748b" font-size="11" font-weight="bold">T</text>
                <text x="215" y="38" fill="#64748b" font-size="11" font-weight="bold">O</text>

                <!-- Borrow Marks -->
                <text x="135" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">²</text>
                <text x="175" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹¹</text>
                <text x="215" y="55" fill="#f59e0b" font-size="11" font-weight="extrabold">¹⁴</text>

                <!-- Row 1: 324 -->
                <text x="135" y="80" fill="#ffffff" font-size="18" font-weight="bold">3</text>
                <text x="175" y="80" fill="#ffffff" font-size="18" font-weight="bold">2</text>
                <text x="215" y="80" fill="#ffffff" font-size="18" font-weight="bold">4</text>

                <!-- Row 2: - 176 -->
                <text x="105" y="105" fill="#ef4444" font-size="18" font-weight="black">-</text>
                <text x="135" y="105" fill="#ffffff" font-size="18" font-weight="bold">1</text>
                <text x="175" y="105" fill="#ffffff" font-size="18" font-weight="bold">7</text>
                <text x="215" y="105" fill="#ffffff" font-size="18" font-weight="bold">6</text>

                <line x1="105" y1="116" x2="245" y2="116" stroke="#64748b" stroke-width="2"/>

                <!-- Difference: 148 -->
                <text x="135" y="142" fill="#34d399" font-size="20" font-weight="black">1</text>
                <text x="175" y="142" fill="#34d399" font-size="20" font-weight="black">4</text>
                <text x="215" y="142" fill="#34d399" font-size="20" font-weight="black">8</text>
            </g>
        </svg>

        <div id="colSubDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Ones: 14 - 6 = 8. Tens: 11 - 7 = 4. Hundreds: 2 - 1 = 1. Difference = <span class="text-red-400 font-bold">148</span>.
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Travel Spend & Harvest Difference</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Real-World Spend-Down Math</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setSpendMode('wallet')" id="btn-spend-wallet" class="spend-btn px-3 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow transition">Wallet: ₹310 - ₹179</button>
        <button onclick="setSpendMode('mango')" id="btn-spend-mango" class="spend-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Harvest: 520kg - 415kg</button>
    </div>

    <!-- Visual Accounting SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="spendTrackerSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Starting Value Card -->
            <rect x="30" y="35" width="90" height="90" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="75" y="60" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">Initial Cash</text>
            <text id="spendInitVal" x="75" y="90" fill="#ffffff" font-size="18" font-weight="black" text-anchor="middle">₹310</text>

            <!-- Minus Sign -->
            <text x="140" y="85" fill="#ef4444" font-size="22" font-weight="black" text-anchor="middle">-</text>

            <!-- Remaining Card -->
            <rect x="160" y="35" width="90" height="90" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="205" y="60" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Remaining</text>
            <text id="spendRemVal" x="205" y="90" fill="#ffffff" font-size="18" font-weight="black" text-anchor="middle">₹179</text>

            <!-- Equal Sign -->
            <text x="270" y="85" fill="#38bdf8" font-size="22" font-weight="black" text-anchor="middle">=</text>

            <!-- Spent / Difference Result -->
            <rect x="285" y="45" width="65" height="70" rx="8" fill="#831843" stroke="#f472b6" stroke-width="2"/>
            <text x="317" y="68" fill="#fbcfe8" font-size="9" font-weight="bold" text-anchor="middle">SPENT</text>
            <text id="spendResultVal" x="317" y="95" fill="#ffffff" font-size="16" font-weight="black" text-anchor="middle">₹131</text>
        </svg>

        <div id="spendDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Initial ₹310 - Remaining ₹179 = <span class="text-purple-400 font-bold">₹131 Total Money Spent</span>.
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Train Passenger Tracking</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Multi-Station Route Simulator</span>
    </div>

    <!-- Station Step Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setTrainStation(1)" id="btn-st-delhi" class="st-btn px-2.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition">New Delhi (642)</button>
        <button onclick="setTrainStation(2)" id="btn-st-dadri" class="st-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Dadri (671)</button>
        <button onclick="setTrainStation(3)" id="btn-st-ghazi" class="st-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Ghaziabad (637)</button>
        <button onclick="setTrainStation(4)" id="btn-st-aligarh" class="st-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Aligarh (592)</button>
    </div>

    <!-- Train Track & Passenger SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="trainTrackSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Railway Track -->
            <line x1="20" y1="120" x2="340" y2="120" stroke="#475569" stroke-width="4"/>
            <!-- Ties -->
            <g stroke="#334155" stroke-width="2">
                <line x1="40" y1="115" x2="40" y2="125"/><line x1="80" y1="115" x2="80" y2="125"/>
                <line x1="120" y1="115" x2="120" y2="125"/><line x1="160" y1="115" x2="160" y2="125"/>
                <line x1="200" y1="115" x2="200" y2="125"/><line x1="240" y1="115" x2="240" y2="125"/>
                <line x1="280" y1="115" x2="280" y2="125"/><line x1="320" y1="115" x2="320" y2="125"/>
            </g>

            <!-- Train Engine Graphic -->
            <g id="trainGraphic" transform="translate(30, 0)">
                <rect x="0" y="70" width="80" height="40" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <rect x="55" y="75" width="20" height="18" rx="2" fill="#bae6fd"/>
                <!-- Wheels -->
                <circle cx="20" cy="115" r="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
                <circle cx="60" cy="115" r="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="2"/>
            </g>

            <!-- Live Passenger Readout -->
            <rect x="180" y="25" width="150" height="75" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <text id="trainStationName" x="255" y="48" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Departure: New Delhi</text>
            <text id="trainOccupancyVal" x="255" y="75" fill="#f8fafc" font-size="17" font-weight="black" text-anchor="middle">642 Passengers</text>
            <text id="trainFlowDetail" x="255" y="92" fill="#a7f3d0" font-size="9" text-anchor="middle">Starting full train</text>
        </svg>

        <div id="trainTrackDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Departing New Delhi: <span class="text-cyan-400 font-bold">642 passengers</span> on board.
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Mental Math Shortcuts</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Near-Tens Compensation</span>
    </div>

    <!-- Shortcut Strategy Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setMentalShortcut('add99')" id="btn-shortcut-add99" class="short-btn px-3 py-1.5 rounded-xl bg-yellow-500 text-slate-950 font-bold text-xs shadow transition">Add 99 (356 + 99)</button>
        <button onclick="setMentalShortcut('sub49')" id="btn-shortcut-sub49" class="short-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Sub 49 (280 - 49)</button>
        <button onclick="setMentalShortcut('expand')" id="btn-shortcut-expand" class="short-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Expanded (45 + 32)</button>
    </div>

    <!-- Mental Compensation SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="mentalShortcutSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Problem Statement -->
            <rect x="40" y="25" width="280" height="35" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
            <text id="mentalOriginalText" x="180" y="47" fill="#f8fafc" font-size="13" font-weight="extrabold" text-anchor="middle">Problem: 356 + 99</text>

            <!-- Shortcut Transformation -->
            <path d="M 180 62 L 180 80" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>

            <rect x="30" y="85" width="300" height="60" rx="8" fill="#422006" fill-opacity="0.4" stroke="#d97706" stroke-width="2"/>
            <text id="mentalStep1" x="180" y="108" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Step 1: 356 + 100 = 456</text>
            <text id="mentalStep2" x="180" y="130" fill="#34d399" font-size="13" font-weight="black" text-anchor="middle">Step 2: 456 - 1 = 455!</text>
        </svg>

        <div id="mentalDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            99 is (100 - 1). Add 100 to get 456, then subtract 1 = <span class="text-yellow-400 font-bold">455</span> instantly without paper!
        </div>
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Target Number Decompositions</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Sum 856 & Difference 563</span>
    </div>

    <!-- Target Selector -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="setTargetDecomp('sum856_a')" id="btn-decomp-1" class="decomp-btn px-2.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow transition">500 + 356</button>
        <button onclick="setTargetDecomp('sum856_b')" id="btn-decomp-2" class="decomp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">700 + 156</button>
        <button onclick="setTargetDecomp('diff563_a')" id="btn-decomp-3" class="decomp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">763 - 200</button>
        <button onclick="setTargetDecomp('diff563_b')" id="btn-decomp-4" class="decomp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">863 - 300</button>
    </div>

    <!-- Equation Visualization SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="targetDecompSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Target Circle (Center) -->
            <circle cx="180" cy="85" r="45" fill="#1e1b4b" stroke="#6366f1" stroke-width="2.5"/>
            <text x="180" y="78" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">TARGET</text>
            <text id="targetCentralNum" x="180" y="100" fill="#ffffff" font-size="18" font-weight="black" text-anchor="middle">856</text>

            <!-- Left Addend / Minuend -->
            <rect id="partARect" x="30" y="65" width="80" height="40" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text id="partAVal" x="70" y="90" fill="#38bdf8" font-size="15" font-weight="black" text-anchor="middle">500</text>

            <!-- Operator Symbol -->
            <text id="decompOp" x="123" y="91" fill="#fbbf24" font-size="20" font-weight="black" text-anchor="middle">+</text>

            <!-- Right Addend / Subtrahend -->
            <rect id="partBRect" x="250" y="65" width="80" height="40" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text id="partBVal" x="290" y="90" fill="#38bdf8" font-size="15" font-weight="black" text-anchor="middle">356</text>
            
            <text id="decompEquals" x="237" y="91" fill="#fbbf24" font-size="20" font-weight="black" text-anchor="middle">=</text>
        </svg>

        <div id="targetDecompDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            500 + 356 = <span class="text-blue-400 font-bold">856</span>. Decomposing by place value creates clean target equations!
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Number Pair Hunt Grid</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Adjacent Matrix Calculations</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="setGridHunt('max_sum')" id="btn-hunt-maxsum" class="hunt-btn px-2.5 py-1.5 rounded-xl bg-green-500 text-slate-950 font-bold text-xs shadow transition">Greatest Sum (87+94)</button>
        <button onclick="setGridHunt('min_diff')" id="btn-hunt-mindiff" class="hunt-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Smallest Diff (55-52)</button>
        <button onclick="setGridHunt('missing')" id="btn-hunt-missing" class="hunt-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Missing Digit (3_5)</button>
    </div>

    <!-- 4x4 Grid Matrix SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="numberGridSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- 4x4 Table Container (Left) -->
            <g id="gridCellsGroup">
                <!-- Row 1 -->
                <rect x="30" y="25" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="49" y="43" fill="#ffffff" font-size="11" text-anchor="middle">24</text>
                <rect x="70" y="25" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="89" y="43" fill="#ffffff" font-size="11" text-anchor="middle">38</text>
                <rect id="cell87" x="110" y="25" width="38" height="28" fill="#15803d" stroke="#22c55e" stroke-width="2"/><text x="129" y="43" fill="#ffffff" font-size="11" font-weight="black" text-anchor="middle">87</text>
                <rect id="cell94" x="150" y="25" width="38" height="28" fill="#15803d" stroke="#22c55e" stroke-width="2"/><text x="169" y="43" fill="#ffffff" font-size="11" font-weight="black" text-anchor="middle">94</text>

                <!-- Row 2 -->
                <rect x="30" y="55" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="49" y="73" fill="#ffffff" font-size="11" text-anchor="middle">45</text>
                <rect id="cell52" x="70" y="55" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="89" y="73" fill="#ffffff" font-size="11" text-anchor="middle">52</text>
                <rect id="cell55" x="110" y="55" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="129" y="73" fill="#ffffff" font-size="11" text-anchor="middle">55</text>
                <rect x="150" y="55" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="169" y="73" fill="#ffffff" font-size="11" text-anchor="middle">63</text>

                <!-- Row 3 -->
                <rect x="30" y="85" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="49" y="103" fill="#ffffff" font-size="11" text-anchor="middle">71</text>
                <rect x="70" y="85" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="89" y="103" fill="#ffffff" font-size="11" text-anchor="middle">19</text>
                <rect x="110" y="85" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="129" y="103" fill="#ffffff" font-size="11" text-anchor="middle">33</text>
                <rect x="150" y="85" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="169" y="103" fill="#ffffff" font-size="11" text-anchor="middle">48</text>

                <!-- Row 4 -->
                <rect x="30" y="115" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="49" y="133" fill="#ffffff" font-size="11" text-anchor="middle">12</text>
                <rect x="70" y="115" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="89" y="133" fill="#ffffff" font-size="11" text-anchor="middle">67</text>
                <rect x="110" y="115" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="129" y="133" fill="#ffffff" font-size="11" text-anchor="middle">81</text>
                <rect x="150" y="115" width="38" height="28" fill="#1e293b" stroke="#334155"/><text x="169" y="133" fill="#ffffff" font-size="11" text-anchor="middle">29</text>
            </g>

            <!-- Analysis Readout Box (Right) -->
            <rect x="205" y="30" width="130" height="110" rx="8" fill="#052e16" stroke="#22c55e" stroke-width="1.5"/>
            <text id="gridReadoutTitle" x="270" y="55" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Adjacent Pair</text>
            <text id="gridReadoutNums" x="270" y="80" fill="#ffffff" font-size="14" font-weight="black" text-anchor="middle">87 + 94</text>
            <text id="gridReadoutResult" x="270" y="105" fill="#fde047" font-size="16" font-weight="black" text-anchor="middle">= 181</text>
            <text id="gridReadoutTag" x="270" y="125" fill="#86efac" font-size="9" text-anchor="middle">Greatest Adjacent Sum</text>
        </svg>

        <div id="gridHuntDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Neighboring cells 87 and 94 yield the <span class="text-green-400 font-bold">greatest sum = 181</span>!
        </div>
    </div>
</div>
"""

simulators_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16,
}


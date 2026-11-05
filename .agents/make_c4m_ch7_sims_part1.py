# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 7: The Cleanest Village
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Village Field Trip Logistics</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Timetable & Poster Data</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setTripMetric('time')" id="btn-trip-time" class="trip-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition">Travel Time (9h)</button>
        <button onclick="setTripMetric('pop')" id="btn-trip-pop" class="trip-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Village Population</button>
        <button onclick="setTripMetric('ticket')" id="btn-trip-ticket" class="trip-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Ticket Budget</button>
    </div>

    <!-- Interactive Poster SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="tripLogisticsSvg" viewBox="0 0 360 190" class="w-full max-w-[340px] h-auto">
            <!-- Background Poster Board -->
            <rect x="20" y="20" width="320" height="150" rx="8" fill="#064e3b" fill-opacity="0.25" stroke="#10b981" stroke-width="2"/>
            
            <!-- Dynamic Content Container -->
            <g id="tripDisplayGroup">
                <!-- Clock / Time Graphic (Default) -->
                <circle cx="110" cy="85" r="45" fill="#022c22" stroke="#34d399" stroke-width="2"/>
                <!-- Clock hands for 7:00 AM -->
                <line x1="110" y1="85" x2="110" y2="52" stroke="#34d399" stroke-width="3" stroke-linecap="round"/>
                <line x1="110" y1="85" x2="85" y2="105" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
                <circle cx="110" cy="85" r="4" fill="#fbbf24"/>
                <text x="110" y="145" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">Departure: 7:00 AM</text>

                <!-- Arrow to Arrival -->
                <path d="M 175 85 L 210 85" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)" stroke-dasharray="3 3"/>
                <text x="195" y="75" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">9 Hours</text>

                <circle cx="260" cy="85" r="35" fill="#022c22" stroke="#f59e0b" stroke-width="2"/>
                <!-- Clock hands for 4:00 PM -->
                <line x1="260" y1="85" x2="260" y2="60" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
                <line x1="260" y1="85" x2="285" y2="100" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="260" cy="85" r="3" fill="#ffffff"/>
                <text x="260" y="135" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Arrival: 4:00 PM</text>
            </g>
        </svg>

        <div id="tripDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            From 7:00 AM to 12:00 noon (5h) + 12:00 noon to 4:00 PM (4h) = <span class="text-emerald-400 font-bold">9 Hours Travel Time</span>.
        </div>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Market Cart Unit Pricing</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Per-Kg Produce Rates</span>
    </div>

    <!-- Produce Selection -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectCartItem('beans')" id="btn-item-beans" class="cart-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition">Beans (₹95/kg)</button>
        <button onclick="selectCartItem('potato')" id="btn-item-potato" class="cart-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Potato (₹37/kg)</button>
        <button onclick="selectCartItem('onion')" id="btn-item-onion" class="cart-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Onion (₹32/kg)</button>
        <button onclick="selectCartItem('radish')" id="btn-item-radish" class="cart-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Radish (₹23/kg)</button>
    </div>

    <!-- Weight Selector & Scale SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <div class="flex items-center gap-2 mb-3">
            <span class="text-xs text-slate-400 font-bold">Select Quantity:</span>
            <button onclick="setCartQty(1)" class="qty-btn px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700">1 kg</button>
            <button onclick="setCartQty(2)" class="qty-btn px-2.5 py-1 rounded bg-amber-500 text-slate-950 text-xs font-bold shadow">2 kg</button>
            <button onclick="setCartQty(3)" class="qty-btn px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700">3 kg</button>
        </div>

        <svg id="marketCartSvg" viewBox="0 0 360 160" class="w-full max-w-[340px] h-auto">
            <!-- Produce Icon / Basket -->
            <rect x="50" y="30" width="110" height="90" rx="8" fill="#166534" fill-opacity="0.3" stroke="#22c55e" stroke-width="2"/>
            <text id="cartProduceIcon" x="105" y="75" font-size="32" text-anchor="middle">🫘</text>
            <text id="cartProduceLabel" x="105" y="105" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Green Beans</text>

            <!-- Price & Weight Calculation Box -->
            <rect x="180" y="30" width="140" height="90" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
            <text x="250" y="55" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">Cost Calculation</text>
            <text id="cartMathText" x="250" y="78" fill="#fef08a" font-size="13" font-weight="extrabold" text-anchor="middle">2 kg × ₹95</text>
            <text id="cartTotalText" x="250" y="105" fill="#38bdf8" font-size="15" font-weight="black" text-anchor="middle">= ₹190</text>
        </svg>

        <div id="cartDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            2 kilograms of green beans at ₹95/kg: <span class="text-amber-400 font-bold">95 + 95 = ₹190</span>.
        </div>
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Total Cost Combinations</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Multi-Item Grocery Basket</span>
    </div>

    <!-- Combination Preset Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setBasketCombo('standard')" id="btn-combo-std" class="combo-btn px-3 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition">1kg Onion + 2kg Potato</button>
        <button onclick="setBasketCombo('target163')" id="btn-combo-target" class="combo-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Target ₹163 Combo</button>
        <button onclick="setBasketCombo('fruits')" id="btn-combo-fruits" class="combo-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Banana + Papaya</button>
    </div>

    <!-- Shopping Basket Receipt SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="basketComboSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Receipt Bill Paper -->
            <rect x="40" y="20" width="280" height="130" rx="6" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            
            <!-- Dynamic Receipt Rows -->
            <g id="receiptRowsGroup">
                <text x="60" y="45" fill="#94a3b8" font-size="10" font-weight="bold">ITEM DESCRIPTION</text>
                <text x="300" y="45" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="end">PRICE</text>
                <line x1="60" y1="52" x2="300" y2="52" stroke="#475569" stroke-width="1"/>

                <!-- Row 1 -->
                <text x="60" y="70" fill="#f8fafc" font-size="11">1 kg Onions</text>
                <text x="300" y="70" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹32</text>

                <!-- Row 2 -->
                <text x="60" y="90" fill="#f8fafc" font-size="11">2 kg Potatoes (2 × ₹37)</text>
                <text x="300" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="end">₹74</text>

                <line x1="60" y1="102" x2="300" y2="102" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3"/>

                <!-- Total Row -->
                <text x="60" y="125" fill="#38bdf8" font-size="13" font-weight="extrabold">TOTAL AMOUNT</text>
                <text x="300" y="125" fill="#38bdf8" font-size="15" font-weight="black" text-anchor="end">₹106</text>
            </g>
        </svg>

        <div id="basketComboDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Subtotal for potatoes: 37 + 37 = ₹74. Adding onions: 74 + 32 = <span class="text-cyan-400 font-bold">₹106</span>.
        </div>
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Grocery Balance & Change</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Open Number Line Math</span>
    </div>

    <!-- Bill vs Paid Controls -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setBalanceScenario(64, 100)" id="btn-bal-64" class="bal-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs shadow transition">Bill ₹64 (Paid ₹100)</button>
        <button onclick="setBalanceScenario(125, 200)" id="btn-bal-125" class="bal-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Bill ₹125 (Paid ₹200)</button>
        <button onclick="setBalanceScenario(340, 500)" id="btn-bal-340" class="bal-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Bill ₹340 (Paid ₹500)</button>
    </div>

    <!-- Number Line SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="balanceLineSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Number Line Horizontal -->
            <line x1="30" y1="110" x2="330" y2="110" stroke="#64748b" stroke-width="2"/>
            
            <!-- Start Mark (Bill = 64) -->
            <circle cx="50" cy="110" r="5" fill="#ef4444"/>
            <text x="50" y="130" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">₹64 (Bill)</text>

            <!-- Jump 1: +6 to 70 -->
            <path d="M 50 110 Q 95 65 140 110" fill="none" stroke="#fbbf24" stroke-width="2"/>
            <text x="95" y="80" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">+₹6</text>
            <circle cx="140" cy="110" r="4" fill="#fbbf24"/>
            <text x="140" y="130" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">₹70</text>

            <!-- Jump 2: +30 to 100 -->
            <path d="M 140 110 Q 225 45 310 110" fill="none" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="65" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">+₹30</text>
            <circle cx="310" cy="110" r="5" fill="#10b981"/>
            <text x="310" y="130" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">₹100 (Paid)</text>

            <!-- Summary Text -->
            <text id="balanceMathSummary" x="180" y="30" fill="#c7d2fe" font-size="12" font-weight="extrabold" text-anchor="middle">Change = ₹6 + ₹30 = ₹36</text>
        </svg>

        <div id="balanceDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Counting up: 64 to 70 (+₹6), then 70 to 100 (+₹30). Total balance returned: <span class="text-indigo-400 font-bold">₹36</span> (₹20 + ₹10 + ₹5 + ₹1).
        </div>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Orange Purchase Tenders</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Fixed ₹42 Bill with Varied Notes</span>
    </div>

    <!-- Currency Note Tenders -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setOrangeTender(50)" id="btn-tender-50" class="tender-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow transition">₹50 Note</button>
        <button onclick="setOrangeTender(100)" id="btn-tender-100" class="tender-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">₹100 Note</button>
        <button onclick="setOrangeTender(200)" id="btn-tender-200" class="tender-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">₹200 Note</button>
        <button onclick="setOrangeTender(500)" id="btn-tender-500" class="tender-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">₹500 Note</button>
    </div>

    <!-- Visual Orange Stall SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="orangeTenderSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <!-- Two Oranges -->
            <circle cx="70" cy="75" r="24" fill="#f97316"/>
            <circle cx="70" cy="75" r="20" fill="#ea580c"/>
            <text x="70" y="80" font-size="20" text-anchor="middle">🍊</text>

            <circle cx="115" cy="75" r="24" fill="#f97316"/>
            <circle cx="115" cy="75" r="20" fill="#ea580c"/>
            <text x="115" y="80" font-size="20" text-anchor="middle">🍊</text>

            <text x="92" y="125" fill="#fdba74" font-size="11" font-weight="bold" text-anchor="middle">2 Oranges = ₹42</text>

            <!-- Banknote Paid Display -->
            <rect id="tenderNoteRect" x="180" y="35" width="140" height="75" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
            <text x="250" y="58" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Currency Tendered</text>
            <text id="tenderNoteVal" x="250" y="82" fill="#ffffff" font-size="16" font-weight="black" text-anchor="middle">₹50 Note</text>
            <text id="tenderChangeVal" x="250" y="100" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Change: ₹8</text>

            <line x1="180" y1="125" x2="320" y2="125" stroke="#475569" stroke-width="1"/>
            <text id="tenderEquationText" x="250" y="145" fill="#38bdf8" font-size="11" font-weight="extrabold" text-anchor="middle">₹50 - ₹42 = ₹8</text>
        </svg>

        <div id="orangeTenderDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Paying with ₹50: <span class="text-orange-400 font-bold">₹50 - ₹42 = ₹8</span> balance returned.
        </div>
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Triangle Magic Sums</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Combinatorial Puzzle (1 to 6)</span>
    </div>

    <!-- Target Sum Selection -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="setMagicTriangle(9)" id="btn-magic-9" class="magic-btn px-3 py-1.5 rounded-xl bg-pink-600 text-white font-bold text-xs shadow transition">Target Sum: 9</button>
        <button onclick="setMagicTriangle(10)" id="btn-magic-10" class="magic-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Target Sum: 10</button>
        <button onclick="setMagicTriangle(12)" id="btn-magic-12" class="magic-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Target Sum: 12</button>
    </div>

    <!-- Magic Triangle SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="magicTriangleSvg" viewBox="0 0 360 190" class="w-full max-w-[340px] h-auto">
            <!-- Triangle Outline -->
            <polygon points="180,30 60,160 300,160" fill="none" stroke="#475569" stroke-width="3"/>
            
            <!-- Top Vertex Circle (Node 1) -->
            <circle cx="180" cy="30" r="16" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
            <text id="nodeTop" x="180" y="35" fill="#ffffff" font-size="12" font-weight="black" text-anchor="middle">1</text>

            <!-- Bottom Left Vertex Circle (Node 2) -->
            <circle cx="60" cy="160" r="16" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
            <text id="nodeLeft" x="60" y="165" fill="#ffffff" font-size="12" font-weight="black" text-anchor="middle">2</text>

            <!-- Bottom Right Vertex Circle (Node 3) -->
            <circle cx="300" cy="160" r="16" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
            <text id="nodeRight" x="300" y="165" fill="#ffffff" font-size="12" font-weight="black" text-anchor="middle">3</text>

            <!-- Left Middle Circle (Node 4) -->
            <circle cx="120" cy="95" r="14" fill="#831843" stroke="#f472b6" stroke-width="2"/>
            <text id="nodeMidLeft" x="120" y="100" fill="#fdf2f8" font-size="11" font-weight="bold" text-anchor="middle">6</text>

            <!-- Right Middle Circle (Node 5) -->
            <circle cx="240" cy="95" r="14" fill="#831843" stroke="#f472b6" stroke-width="2"/>
            <text id="nodeMidRight" x="240" y="100" fill="#fdf2f8" font-size="11" font-weight="bold" text-anchor="middle">5</text>

            <!-- Bottom Middle Circle (Node 6) -->
            <circle cx="180" cy="160" r="14" fill="#831843" stroke="#f472b6" stroke-width="2"/>
            <text id="nodeMidBottom" x="180" y="165" fill="#fdf2f8" font-size="11" font-weight="bold" text-anchor="middle">4</text>
        </svg>

        <div id="magicTriangleDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Side 1: 1 + 6 + 2 = 9. Side 2: 1 + 5 + 3 = 9. Side 3: 2 + 4 + 3 = <span class="text-pink-400 font-bold">9</span>!
        </div>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Base Ten Regrouping Addition</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Dienes Blocks Model</span>
    </div>

    <!-- Regrouping Trigger -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setBaseTenStep('unbundled')" id="btn-dienes-1" class="dienes-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Step 1: 48 + 26 (14 Ones)</button>
        <button onclick="setBaseTenStep('bundled')" id="btn-dienes-2" class="dienes-btn px-3.5 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs shadow transition">Step 2: Bundle 10 Ones -> 1 Ten</button>
    </div>

    <!-- Visual Dienes Blocks SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="baseTenSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Tens Column (Left) -->
            <rect x="30" y="25" width="140" height="135" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="100" y="42" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Tens Column (Rods)</text>

            <!-- Ones Column (Right) -->
            <rect x="190" y="25" width="140" height="135" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="260" y="42" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Ones Column (Cubes)</text>

            <!-- Dynamic Blocks -->
            <g id="dienesBlocksGroup">
                <!-- Bundled View: 7 Tens rods in Tens column, 4 single cubes in Ones -->
                <!-- 7 Ten Rods -->
                <rect x="42" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="57" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
                <rect x="72" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="87" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
                <rect x="102" y="55" width="10" height="85" fill="#0284c7" rx="2"/><rect x="117" y="55" width="10" height="85" fill="#0284c7" rx="2"/>
                <rect x="132" y="55" width="10" height="85" fill="#10b981" rx="2" stroke="#34d399" stroke-width="1"/> <!-- Carried Rod -->
                <text x="100" y="152" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">7 Tens = 70</text>

                <!-- 4 Remaining Ones Cubes -->
                <rect x="225" y="65" width="14" height="14" fill="#f59e0b" rx="2"/>
                <rect x="250" y="65" width="14" height="14" fill="#f59e0b" rx="2"/>
                <rect x="225" y="90" width="14" height="14" fill="#f59e0b" rx="2"/>
                <rect x="250" y="90" width="14" height="14" fill="#f59e0b" rx="2"/>
                <text x="260" y="152" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">4 Ones = 4</text>
            </g>
        </svg>

        <div id="baseTenDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            10 of the 14 single cubes bundle into <span class="text-emerald-400 font-bold">1 new Ten rod</span>, leaving 4 single cubes. Total = <span class="text-teal-400 font-bold">74</span>.
        </div>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Field Trip Attendance Addition</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Vertical Column Regrouping</span>
    </div>

    <!-- Problem Selector -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setAdditionProblem('teachers')" id="btn-add-teach" class="add-prob-btn px-3 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow transition">Teachers (24 + 28)</button>
        <button onclick="setAdditionProblem('students')" id="btn-add-stud" class="add-prob-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Students (438 + 476)</button>
    </div>

    <!-- Vertical Column Addition SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="columnAdditionSvg" viewBox="0 0 360 170" class="w-full max-w-[340px] h-auto">
            <rect x="80" y="15" width="200" height="140" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            
            <g id="colAddTextGroup">
                <!-- Teachers: 24 + 28 = 52 Default -->
                <!-- Carries -->
                <text x="175" y="40" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">¹</text>

                <!-- Row 1 -->
                <text x="145" y="65" fill="#94a3b8" font-size="16" font-weight="bold">T</text>
                <text x="185" y="65" fill="#94a3b8" font-size="16" font-weight="bold">O</text>
                
                <text x="145" y="90" fill="#ffffff" font-size="18" font-weight="bold">2</text>
                <text x="185" y="90" fill="#ffffff" font-size="18" font-weight="bold">4</text>

                <!-- Row 2 -->
                <text x="115" y="115" fill="#38bdf8" font-size="18" font-weight="black">+</text>
                <text x="145" y="115" fill="#ffffff" font-size="18" font-weight="bold">2</text>
                <text x="185" y="115" fill="#ffffff" font-size="18" font-weight="bold">8</text>

                <line x1="110" y1="125" x2="210" y2="125" stroke="#64748b" stroke-width="2"/>

                <!-- Answer Row -->
                <text x="145" y="148" fill="#34d399" font-size="20" font-weight="black">5</text>
                <text x="185" y="148" fill="#34d399" font-size="20" font-weight="black">2</text>
            </g>
        </svg>

        <div id="colAddDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Ones: 4 + 8 = 12 (write 2, carry 1). Tens: 1 + 2 + 2 = <span class="text-blue-400 font-bold">5 Tens</span>. Total = <span class="text-emerald-400 font-bold">52 Staff</span>.
        </div>
    </div>
</div>
"""

simulators_part1 = {
    1: sim1,
    2: sim2,
    3: sim3,
    4: sim4,
    5: sim5,
    6: sim6,
    7: sim7,
    8: sim8,
}


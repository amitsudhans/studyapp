"""
Simulators 1 to 8 for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I
Joyful Mathematics curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols.
"""

SIMS = {}

# SIM 1: We the Travellers (Transport Timeline Explorer)
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Transport Evolution & Speed Explorer</span>
        <p class="text-[11px] text-slate-400">Step through human travel history: from walking at 4 km/h to orbital spacecraft at 28,000 km/h!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Road / Horizon Track -->
            <line x1="20" y1="180" x2="380" y2="180" stroke="#334155" stroke-width="3"/>
            <line x1="20" y1="180" x2="380" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6,6"/>

            <!-- Dynamic Vehicle Visual Stage -->
            <g id="transportVehicleGraphic">
                <!-- Mode 1 (Default): Walking Traveller -->
                <circle cx="200" cy="115" r="14" fill="#fed7aa"/>
                <path d="M190,130 L210,130 L205,160 L195,160 Z" fill="#0284c7"/>
                <line x1="195" y1="160" x2="190" y2="180" stroke="#1e293b" stroke-width="3"/>
                <line x1="205" y1="160" x2="215" y2="180" stroke="#1e293b" stroke-width="3"/>
                <!-- Walking Stick -->
                <line x1="214" y1="135" x2="218" y2="180" stroke="#78350f" stroke-width="2"/>
                <text x="200" y="90" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Ancient Walking on Foot</text>
            </g>

            <!-- Speedometer Display Card -->
            <rect x="25" y="20" width="135" height="46" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="33" fill="#94a3b8" font-size="7">AVERAGE SPEED</text>
            <text id="sim1SpeedText" x="35" y="48" fill="#38bdf8" font-size="11" font-weight="bold">4 km/h (Walking)</text>
            <text id="sim1Distance10h" x="35" y="59" fill="#cbd5e1" font-size="7">Distance in 10h: 40 km</text>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="setTransportMode('walk')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Walking (4 km/h)
        </button>
        <button onclick="setTransportMode('cart')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Cart (5 km/h)
        </button>
        <button onclick="setTransportMode('train')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            Train (120 km/h)
        </button>
        <button onclick="setTransportMode('rocket')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-purple-500/50 text-[10px] font-bold text-purple-300">
            Rocket (28,000 km/h)
        </button>
    </div>
    <div id="sim1Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Walking (Ancient Era):</strong> Travellers walked at 3–5 km/h. To journey across India from Varanasi to Kanyakumari took over 6 months of steady walking!
    </div>
</div>
"""

# SIM 2: Ten Thousand (Base-10 Visual Counter)
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Ten Thousand: Bundling Base-10 Units</span>
        <p class="text-[11px] text-slate-400">Add thousands one by one. Watch 9,000 + 1,000 bundle into Ten Thousand (10,000)!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- 10 Thousand Cube Bundles Container (2 rows of 5) -->
            <g id="thousandBlocksGroup" transform="translate(45, 55)">
                <!-- Blocks rendered dynamically by JS -->
            </g>

            <!-- Counter Readout Box -->
            <rect x="255" y="45" width="125" height="135" rx="8" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="317" y="65" fill="#94a3b8" font-size="8" font-weight="bold" text-anchor="middle">TOTAL COUNT</text>
            <text id="sim2BundleTotal" x="317" y="98" fill="#4ade80" font-size="20" font-weight="bold" text-anchor="middle">1,000</text>
            <text id="sim2BundleWords" x="317" y="118" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">One Thousand</text>
            <text id="sim2BundleMath" x="317" y="145" fill="#38bdf8" font-size="7.5" text-anchor="middle">1 × 1,000 = 1,000</text>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="addThousandBlock()" class="flex-1 p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            + Add 1,000 Block
        </button>
        <button onclick="resetThousandBlocks()" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-bold text-slate-300">
            Reset (1,000)
        </button>
        <button onclick="jumpToTenThousand()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Bundle to 10,000
        </button>
    </div>
    <div id="sim2Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Base-10 Bundling:</strong> 10 Ones = 1 Ten | 10 Tens = 1 Hundred | 10 Hundreds = 1 Thousand | <strong>10 Thousands = 1 Ten Thousand (10,000)</strong>!
    </div>
</div>
"""

# SIM 3: Place Value (Indian Place Value Abacus / Spike Board)
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Indian Place Value Spike Abacus (TTh, Th, H, T, O)</span>
        <p class="text-[11px] text-slate-400">Add beads to each spike and see how each position scales by powers of 10!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Abacus Wooden Base -->
            <rect x="30" y="180" width="340" height="22" rx="4" fill="#78350f" stroke="#451a03" stroke-width="1.5"/>

            <!-- 5 Spikes (TTh: 70, Th: 135, H: 200, T: 265, O: 330) -->
            <!-- TTh Spike -->
            <line x1="70" y1="50" x2="70" y2="180" stroke="#94a3b8" stroke-width="2.5"/>
            <text x="70" y="196" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">TTh</text>
            <text x="70" y="210" fill="#94a3b8" font-size="7" text-anchor="middle">(10,000)</text>

            <!-- Th Spike -->
            <line x1="135" y1="50" x2="135" y2="180" stroke="#94a3b8" stroke-width="2.5"/>
            <text x="135" y="196" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Th</text>
            <text x="135" y="210" fill="#94a3b8" font-size="7" text-anchor="middle">(1,000)</text>

            <!-- H Spike -->
            <line x1="200" y1="50" x2="200" y2="180" stroke="#94a3b8" stroke-width="2.5"/>
            <text x="200" y="196" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">H</text>
            <text x="200" y="210" fill="#94a3b8" font-size="7" text-anchor="middle">(100)</text>

            <!-- T Spike -->
            <line x1="265" y1="50" x2="265" y2="180" stroke="#94a3b8" stroke-width="2.5"/>
            <text x="265" y="196" fill="#fb923c" font-size="8" font-weight="bold" text-anchor="middle">T</text>
            <text x="265" y="210" fill="#94a3b8" font-size="7" text-anchor="middle">(10)</text>

            <!-- O Spike -->
            <line x1="330" y1="50" x2="330" y2="180" stroke="#94a3b8" stroke-width="2.5"/>
            <text x="330" y="196" fill="#f472b6" font-size="8" font-weight="bold" text-anchor="middle">O</text>
            <text x="330" y="210" fill="#94a3b8" font-size="7" text-anchor="middle">(1)</text>

            <!-- Beads Container -->
            <g id="abacusBeadsLayer"></g>

            <!-- Top Value Pill -->
            <rect x="120" y="12" width="160" height="30" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="abacusTotalText" x="200" y="32" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Value: 35,427</text>
        </svg>
    </div>
    <div class="grid grid-cols-5 gap-1.5">
        <button onclick="incrementAbacusSpike('tth')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-yellow-500/50 text-[10px] font-bold text-yellow-300">
            +1 TTh
        </button>
        <button onclick="incrementAbacusSpike('th')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            +1 Th
        </button>
        <button onclick="incrementAbacusSpike('h')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            +1 H
        </button>
        <button onclick="incrementAbacusSpike('t')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-orange-500/50 text-[10px] font-bold text-orange-300">
            +1 T
        </button>
        <button onclick="incrementAbacusSpike('o')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-pink-500/50 text-[10px] font-bold text-pink-300">
            +1 O
        </button>
    </div>
    <div id="sim3Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Expanded Form:</strong> 30,000 + 5,000 + 400 + 20 + 7 = <strong>35,427</strong> (Thirty-five thousand, four hundred twenty-seven).
    </div>
</div>
"""

# SIM 4: Writing Numbers (Indian Comma Formatter)
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Indian Comma System & Period Formatter</span>
        <p class="text-[11px] text-slate-400">See how commas group digits into Thousands Period and Ones Period (XX,XXX)!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Period Groups Container Card -->
            <g transform="translate(50, 40)">
                <!-- Thousands Period Box (2 digits) -->
                <rect x="0" y="0" width="125" height="100" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
                <text x="62" y="24" fill="#bae6fd" font-size="8" font-weight="bold" text-anchor="middle">THOUSANDS PERIOD</text>
                <text id="commaPeriodTTh" x="62" y="68" fill="#ffffff" font-size="28" font-weight="bold" text-anchor="middle">48</text>
                <text x="62" y="88" fill="#7dd3fc" font-size="7.5" text-anchor="middle">TTh & Th Columns</text>

                <!-- Comma Divider Bead -->
                <circle cx="140" cy="65" r="4" fill="#f59e0b"/>
                <path d="M140,65 Q136,75 142,78" stroke="#f59e0b" stroke-width="2" fill="none"/>
                <text x="140" y="95" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">,</text>

                <!-- Ones Period Box (3 digits) -->
                <rect x="155" y="0" width="145" height="100" rx="8" fill="#064e3b" stroke="#4ade80" stroke-width="2"/>
                <text x="227" y="24" fill="#bbf7d0" font-size="8" font-weight="bold" text-anchor="middle">ONES PERIOD</text>
                <text id="commaPeriodOnes" x="227" y="68" fill="#ffffff" font-size="28" font-weight="bold" text-anchor="middle">215</text>
                <text x="227" y="88" fill="#86efac" font-size="7.5" text-anchor="middle">H, T, O Columns</text>
            </g>

            <!-- Combined Full Numeral Banner -->
            <rect x="50" y="160" width="300" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="fullNumeralWithComma" x="200" y="180" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Numeral: 48,215</text>
            <text id="fullWordNameText" x="200" y="194" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Forty-eight thousand, two hundred fifteen</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setExampleNumber('48215')" class="p-2 bg-sky-900 hover:bg-sky-800 border border-sky-500 rounded-lg text-xs font-bold text-sky-200">
            Example 1: 48,215
        </button>
        <button onclick="setExampleNumber('70008')" class="p-2 bg-emerald-900 hover:bg-emerald-800 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-200">
            Example 2: 70,008
        </button>
        <button onclick="setExampleNumber('99999')" class="p-2 bg-amber-900 hover:bg-amber-800 border border-amber-500 rounded-lg text-xs font-bold text-amber-200">
            Example 3: 99,999
        </button>
    </div>
    <div id="sim4Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Indian Rule:</strong> First comma after 3 digits from right (Ones, Tens, Hundreds). The next period has 2 digits (Thousands). So 5 digits are written as <strong>48,215</strong>!
    </div>
</div>
"""

# SIM 5: Ordering Numbers (Vehicle Odometer Sorter)
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Vehicle Odometer Sorter (Ascending vs Descending)</span>
        <p class="text-[11px] text-slate-400">Compare 4 vehicle travel distances. Sort them in ascending or descending order!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- 4 Odometer Distance Cards -->
            <g id="odometerBarsGroup" transform="translate(30, 30)">
                <!-- Vehicle A: Car (24,150 km) -->
                <rect id="barA" x="0" y="10" width="180" height="28" rx="4" fill="#0284c7" opacity="0.85"/>
                <text x="10" y="28" fill="#ffffff" font-size="8" font-weight="bold">Car A: 24,150 km</text>

                <!-- Vehicle B: Bus (18,900 km) -->
                <rect id="barB" x="0" y="48" width="140" height="28" rx="4" fill="#15803d" opacity="0.85"/>
                <text x="10" y="66" fill="#ffffff" font-size="8" font-weight="bold">Bus B: 18,900 km</text>

                <!-- Vehicle C: Train (45,300 km) -->
                <rect id="barC" x="0" y="86" width="300" height="28" rx="4" fill="#d97706" opacity="0.85"/>
                <text x="10" y="104" fill="#ffffff" font-size="8" font-weight="bold">Train C: 45,300 km</text>

                <!-- Vehicle D: Truck (32,800 km) -->
                <rect id="barD" x="0" y="124" width="225" height="28" rx="4" fill="#7c3aed" opacity="0.85"/>
                <text x="10" y="142" fill="#ffffff" font-size="8" font-weight="bold">Truck D: 32,800 km</text>
            </g>

            <!-- Order Indicator Label -->
            <rect x="25" y="195" width="350" height="30" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="orderSequenceText" x="200" y="214" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Unsorted: Compare Ten Thousands (TTh) digits first!</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="sortOdometers('ascending')" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Ascending Order (Smallest to Largest)
        </button>
        <button onclick="sortOdometers('descending')" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Descending Order (Largest to Smallest)
        </button>
    </div>
    <div id="sim5Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Comparison Rule:</strong> Look at the Ten Thousands digit first: 1 in 18,900 < 2 in 24,150 < 3 in 32,800 < 4 in 45,300.
    </div>
</div>
"""

# SIM 6: Digit Swap (Number Shifter Lab)
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Digit Swap Lab (The Power of Position)</span>
        <p class="text-[11px] text-slate-400">Swap digits in 25,480 to discover how position massively changes a number's value!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- 5 Clickable Digit Tiles -->
            <g id="digitTilesGroup" transform="translate(65, 50)">
                <!-- Tile 1 (TTh) -->
                <rect id="tile0" x="0" y="0" width="45" height="60" rx="6" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
                <text id="digitVal0" x="22" y="38" fill="#ffffff" font-size="24" font-weight="bold" text-anchor="middle">2</text>
                <text x="22" y="54" fill="#7dd3fc" font-size="7" text-anchor="middle">TTh</text>

                <!-- Tile 2 (Th) -->
                <rect id="tile1" x="55" y="0" width="45" height="60" rx="6" fill="#064e3b" stroke="#4ade80" stroke-width="2"/>
                <text id="digitVal1" x="77" y="38" fill="#ffffff" font-size="24" font-weight="bold" text-anchor="middle">5</text>
                <text x="77" y="54" fill="#86efac" font-size="7" text-anchor="middle">Th</text>

                <!-- Tile 3 (H) -->
                <rect id="tile2" x="110" y="0" width="45" height="60" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="2"/>
                <text id="digitVal2" x="132" y="38" fill="#ffffff" font-size="24" font-weight="bold" text-anchor="middle">4</text>
                <text x="132" y="54" fill="#fde68a" font-size="7" text-anchor="middle">H</text>

                <!-- Tile 4 (T) -->
                <rect id="tile3" x="165" y="0" width="45" height="60" rx="6" fill="#581c87" stroke="#c084fc" stroke-width="2"/>
                <text id="digitVal3" x="187" y="38" fill="#ffffff" font-size="24" font-weight="bold" text-anchor="middle">8</text>
                <text x="187" y="54" fill="#e9d5ff" font-size="7" text-anchor="middle">T</text>

                <!-- Tile 5 (O) -->
                <rect id="tile4" x="220" y="0" width="45" height="60" rx="6" fill="#881337" stroke="#fb7185" stroke-width="2"/>
                <text id="digitVal4" x="242" y="38" fill="#ffffff" font-size="24" font-weight="bold" text-anchor="middle">0</text>
                <text x="242" y="54" fill="#fecdd3" font-size="7" text-anchor="middle">O</text>
            </g>

            <!-- Difference Comparison Panel -->
            <rect x="50" y="135" width="300" height="75" rx="8" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="200" y="154" fill="#94a3b8" font-size="8" text-anchor="middle">ORIGINAL VS NEW VALUE</text>
            <text id="swapCompareText" x="200" y="174" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Original Number: 25,480</text>
            <text id="swapDiffText" x="200" y="196" fill="#38bdf8" font-size="9" text-anchor="middle">Click below to swap digits</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="swapDigits(0, 1)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-sky-500 rounded-lg text-xs font-bold text-sky-300">
            Swap TTh & Th (2 ↔ 5)
        </button>
        <button onclick="swapDigits(1, 3)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-purple-500 rounded-lg text-xs font-bold text-purple-300">
            Swap Th & T (5 ↔ 8)
        </button>
        <button onclick="resetSwapDigits()" class="p-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 rounded-lg text-xs font-bold text-slate-300">
            Reset (25,480)
        </button>
    </div>
    <div id="sim6Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Position Matters:</strong> Moving digit 5 from Thousands (5,000) to Ten Thousands (50,000) increases its value by 45,000!
    </div>
</div>
"""

# SIM 7: Nearest Tens (Rabbit & Carrot Number Line)
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Nearest Tens: The Rabbit & Carrot Number Line</span>
        <p class="text-[11px] text-slate-400">Watch the hungry rabbit hop to the nearest multiple of 10. Halfway (5) always hops UP!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Number Line from 40 to 50 -->
            <line x1="50" y1="140" x2="350" y2="140" stroke="#94a3b8" stroke-width="2.5"/>

            <!-- Tick Marks 40 to 50 -->
            <!-- 40 (Left Carrot) -->
            <line x1="50" y1="130" x2="50" y2="150" stroke="#f59e0b" stroke-width="3"/>
            <text x="50" y="165" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">40</text>
            <!-- Carrot Icon at 40 -->
            <polygon points="50,115 45,100 55,100" fill="#ea580c"/>
            <line x1="50" y1="100" x2="48" y2="92" stroke="#16a34a" stroke-width="2"/>

            <!-- 45 (Midpoint) -->
            <line x1="200" y1="132" x2="200" y2="148" stroke="#38bdf8" stroke-width="2"/>
            <text x="200" y="165" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">45 (Midway)</text>

            <!-- 50 (Right Carrot) -->
            <line x1="350" y1="130" x2="350" y2="150" stroke="#f59e0b" stroke-width="3"/>
            <text x="350" y="165" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">50</text>
            <!-- Carrot Icon at 50 -->
            <polygon points="350,115 345,100 355,100" fill="#ea580c"/>
            <line x1="350" y1="100" x2="348" y2="92" stroke="#16a34a" stroke-width="2"/>

            <!-- Rabbit Marker Graphic -->
            <g id="rabbitMarker" transform="translate(140, 110)">
                <!-- Rabbit Body -->
                <ellipse cx="0" cy="0" rx="10" ry="7" fill="#f8fafc"/>
                <circle cx="-7" cy="-4" r="5" fill="#f8fafc"/>
                <!-- Long Ears -->
                <line x1="-8" y1="-8" x2="-10" y2="-18" stroke="#f8fafc" stroke-width="2"/>
                <line x1="-6" y1="-8" x2="-6" y2="-18" stroke="#f8fafc" stroke-width="2"/>
                <circle cx="-8" cy="-5" r="1" fill="#020617"/>
                <text x="0" y="24" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">43</text>
            </g>

            <!-- Status Decision Box -->
            <rect x="50" y="20" width="300" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="rabbitDecisionText" x="200" y="38" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Position: 43 | Distance to 40 = 3, Distance to 50 = 7</text>
            <text id="rabbitVerdictText" x="200" y="52" fill="#38bdf8" font-size="8" text-anchor="middle">Closer to 40 → Rounds down to 40</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setRabbitPosition(43)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            Test 43 (Hops to 40)
        </button>
        <button onclick="setRabbitPosition(45)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-sky-500 rounded-lg text-xs font-bold text-sky-300">
            Test 45 (Halfway → 50)
        </button>
        <button onclick="setRabbitPosition(48)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            Test 48 (Hops to 50)
        </button>
    </div>
    <div id="sim7Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Rule:</strong> Check the Ones digit! 1, 2, 3, 4 round down. 5, 6, 7, 8, 9 round up to the next ten.
    </div>
</div>
"""

# SIM 8: Nearest Hundreds (Highway Milestone Marker)
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Nearest Hundreds: Highway Milestone Marker</span>
        <p class="text-[11px] text-slate-400">Position the highway car between 300 km and 400 km. Check which hundred is closer!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Highway Road Surface -->
            <rect x="20" y="120" width="360" height="50" fill="#1e293b"/>
            <line x1="20" y1="145" x2="380" y2="145" stroke="#fde047" stroke-width="2" stroke-dasharray="8,8"/>

            <!-- Milestones at 300, 350, 400 -->
            <!-- 300 km Milestone -->
            <g transform="translate(45, 80)">
                <path d="M0,40 L0,15 A15,15 0 0,1 30,15 L30,40 Z" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <path d="M0,15 A15,15 0 0,1 30,15 Z" fill="#0284c7"/>
                <text x="15" y="32" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">300</text>
            </g>

            <!-- 350 km Midpoint Marker -->
            <line x1="200" y1="120" x2="200" y2="170" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
            <text x="200" y="112" fill="#38bdf8" font-size="7.5" font-weight="bold" text-anchor="middle">Midpoint (350)</text>

            <!-- 400 km Milestone -->
            <g transform="translate(325, 80)">
                <path d="M0,40 L0,15 A15,15 0 0,1 30,15 L30,40 Z" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <path d="M0,15 A15,15 0 0,1 30,15 Z" fill="#16a34a"/>
                <text x="15" y="32" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">400</text>
            </g>

            <!-- Highway Car Graphic -->
            <g id="highwayCarMarker" transform="translate(130, 130)">
                <rect x="0" y="6" width="36" height="14" rx="3" fill="#ea580c"/>
                <polygon points="8,6 14,0 26,0 30,6" fill="#fde047"/>
                <circle cx="8" cy="20" r="4" fill="#020617"/>
                <circle cx="28" cy="20" r="4" fill="#020617"/>
                <text id="carDistanceLabel" x="18" y="-4" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">328 km</text>
            </g>

            <!-- Result Readout Banner -->
            <rect x="50" y="20" width="300" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="milestoneResultText" x="200" y="38" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">328 km: Tens digit is 2 (< 5)</text>
            <text id="milestoneVerdictText" x="200" y="52" fill="#38bdf8" font-size="8" text-anchor="middle">Rounds DOWN to 300 km</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setHighwayDistance(328)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-sky-500 rounded-lg text-xs font-bold text-sky-300">
            Test 328 km (→ 300)
        </button>
        <button onclick="setHighwayDistance(350)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            Test 350 km (→ 400)
        </button>
        <button onclick="setHighwayDistance(372)" class="p-2 bg-slate-900 hover:bg-slate-800 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            Test 372 km (→ 400)
        </button>
    </div>
    <div id="sim8Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Nearest 100 Rule:</strong> Look at the Tens digit! If tens digit is 5 or more (50 to 99), round up to the next hundred.
    </div>
</div>
"""

print("Simulators 1 to 8 defined.")


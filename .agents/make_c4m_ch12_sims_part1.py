# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leap Year Timeline Explorer</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Divisibility by 4 & February 29</span>
    </div>

    <!-- Interactive Year Slider -->
    <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400 font-medium">Select Year: <strong id="leap-year-val" class="text-indigo-400 text-base font-bold">2024</strong></span>
            <span id="leap-badge" class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">LEAP YEAR (366 Days)</span>
        </div>
        <input type="range" id="leap-slider" min="2016" max="2036" step="1" value="2024" oninput="updateLeapSim(this.value)" class="w-full accent-indigo-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-500 font-mono">
            <span>2016</span>
            <span>2020</span>
            <span>2024</span>
            <span>2028</span>
            <span>2032</span>
            <span>2036</span>
        </div>
    </div>

    <!-- Mathematical Breakdown Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50">
            <div class="text-[10px] text-slate-400 uppercase">Divisibility</div>
            <div id="leap-div-math" class="text-indigo-300 font-bold mt-0.5">2024 ÷ 4 = 506</div>
            <div id="leap-rem-text" class="text-[10px] text-emerald-400 font-medium">Remainder 0</div>
        </div>
        <div class="bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50">
            <div class="text-[10px] text-slate-400 uppercase">Days in Feb</div>
            <div id="leap-feb-days" class="text-white font-bold text-base mt-0.5">29 Days</div>
            <div id="leap-feb-sub" class="text-[10px] text-indigo-300 font-medium">+1 Leap Day</div>
        </div>
        <div class="bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50">
            <div class="text-[10px] text-slate-400 uppercase">Total Days</div>
            <div id="leap-total-days" class="text-white font-bold text-base mt-0.5">366 Days</div>
            <div class="text-[10px] text-slate-400 font-medium">52 wks + 2 days</div>
        </div>
        <div class="bg-slate-800/60 p-2.5 rounded-lg border border-slate-700/50">
            <div class="text-[10px] text-slate-400 uppercase">Feb 29 Birthday</div>
            <div id="leap-bday-status" class="text-emerald-300 font-bold text-xs mt-1">Official Date!</div>
            <div class="text-[10px] text-slate-400">Leapling Day</div>
        </div>
    </div>

    <!-- Quick Presets -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <span class="text-slate-400 text-[11px]">Jump to:</span>
        <button onclick="updateLeapSim(2020)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">2020 (Leap)</button>
        <button onclick="updateLeapSim(2023)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">2023 (Ordinary)</button>
        <button onclick="updateLeapSim(2024)" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold">2024 (Leap)</button>
        <button onclick="updateLeapSim(2025)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">2025 (Ordinary)</button>
        <button onclick="updateLeapSim(2028)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">2028 (Leap)</button>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Universal Date Formats Math</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">DD/MM/YYYY vs Written Words</span>
    </div>

    <!-- Interactive Date Builder -->
    <div class="grid grid-cols-3 gap-2 bg-slate-950/60 p-3 rounded-xl border border-slate-800">
        <div>
            <label class="block text-[10px] text-slate-400 font-medium mb-1">Day (DD)</label>
            <select id="date-dd" onchange="renderDateFormatSim()" class="w-full bg-slate-800 border border-slate-700 rounded-lg text-white text-xs p-1.5 focus:ring-1 focus:ring-blue-500">
                <!-- 01 to 31 populated by JS -->
            </select>
        </div>
        <div>
            <label class="block text-[10px] text-slate-400 font-medium mb-1">Month (MM)</label>
            <select id="date-mm" onchange="renderDateFormatSim()" class="w-full bg-slate-800 border border-slate-700 rounded-lg text-white text-xs p-1.5 focus:ring-1 focus:ring-blue-500">
                <option value="1">01 - January</option>
                <option value="2">02 - February</option>
                <option value="3">03 - March</option>
                <option value="4">04 - April</option>
                <option value="5">05 - May</option>
                <option value="6">06 - June</option>
                <option value="7">07 - July</option>
                <option value="8" selected>08 - August</option>
                <option value="9">09 - September</option>
                <option value="10">10 - October</option>
                <option value="11">11 - November</option>
                <option value="12">12 - December</option>
            </select>
        </div>
        <div>
            <label class="block text-[10px] text-slate-400 font-medium mb-1">Year (YYYY)</label>
            <input type="number" id="date-yyyy" value="1947" min="1900" max="2099" onchange="renderDateFormatSim()" class="w-full bg-slate-800 border border-slate-700 rounded-lg text-white text-xs p-1.5 focus:ring-1 focus:ring-blue-500 font-mono">
        </div>
    </div>

    <!-- Output Display Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-blue-950/40 border border-blue-800/60 p-3 rounded-xl space-y-1">
            <span class="text-[10px] text-blue-400 font-mono uppercase">Standard Format (DD/MM/YYYY)</span>
            <div id="date-out-num" class="text-lg font-bold text-white font-mono tracking-wider">15/08/1947</div>
            <div class="text-[11px] text-slate-400">Day: <span id="out-dd" class="text-blue-300">15</span> | Month: <span id="out-mm" class="text-blue-300">08</span> | Year: <span id="out-yy" class="text-blue-300">1947</span></div>
        </div>
        <div class="bg-emerald-950/40 border border-emerald-800/60 p-3 rounded-xl space-y-1">
            <span class="text-[10px] text-emerald-400 font-mono uppercase">Expanded Written Form</span>
            <div id="date-out-words" class="text-base font-bold text-emerald-200">15 August 1947</div>
            <div id="date-context-note" class="text-[11px] text-slate-300">Indian Independence Day</div>
        </div>
    </div>

    <!-- Historical & Festival Presets -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 text-[11px] mr-1">Presets:</span>
        <button onclick="setDatePreset(15, 8, 1947, 'Independence Day')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">15 Aug 1947</button>
        <button onclick="setDatePreset(26, 1, 1950, 'Republic Day')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">26 Jan 1950</button>
        <button onclick="setDatePreset(2, 10, 1869, 'Gandhi Jayanti')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">02 Oct 1869</button>
        <button onclick="setDatePreset(14, 11, 2025, 'Children\'s Day')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">14 Nov 2025</button>
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Packaging Expiry Dates Inspector</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">MFG Date + Shelf Life = Expiry</span>
    </div>

    <!-- Product Selection Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button onclick="selectExpiryProduct('biscuit')" id="exp-tab-biscuit" class="p-2 rounded-xl border bg-amber-600/20 border-amber-500 text-amber-300 font-bold text-center transition">
            🍪 Biscuit Pack
        </button>
        <button onclick="selectExpiryProduct('milk')" id="exp-tab-milk" class="p-2 rounded-xl border border-slate-800 bg-slate-950/60 text-slate-400 text-center transition hover:text-white">
            🥛 Milk Pouch
        </button>
        <button onclick="selectExpiryProduct('jam')" id="exp-tab-jam" class="p-2 rounded-xl border border-slate-800 bg-slate-950/60 text-slate-400 text-center transition hover:text-white">
            🍓 Fruit Jam
        </button>
        <button onclick="selectExpiryProduct('syrup')" id="exp-tab-syrup" class="p-2 rounded-xl border border-slate-800 bg-slate-950/60 text-slate-400 text-center transition hover:text-white">
            💊 Cough Syrup
        </button>
    </div>

    <!-- Label Visual Mockup -->
    <div class="bg-slate-950 p-4 rounded-xl border border-dashed border-slate-700 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="space-y-1 text-center sm:text-left">
            <span id="exp-prod-name" class="font-bold text-white text-sm">Nutri-Bake Digestive Biscuits</span>
            <div class="text-xs font-mono text-slate-400">MFG: <span id="exp-mfg-str" class="text-amber-400 font-bold">10/01/2024</span></div>
            <div class="text-xs font-mono text-slate-400">BEST BEFORE: <span id="exp-life-str" class="text-indigo-300 font-bold">6 Months from MFG</span></div>
            <div class="text-xs font-mono text-slate-400">EXP DATE: <span id="exp-target-str" class="text-red-400 font-bold">10/07/2024</span></div>
        </div>

        <!-- Inspection Date Checker -->
        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 text-center space-y-1.5">
            <div class="text-[10px] text-slate-400 uppercase font-mono">Today's Inspection Date</div>
            <input type="date" id="exp-inspect-date" value="2024-05-15" onchange="auditExpiryProduct()" class="bg-slate-800 text-white text-xs px-2 py-1 rounded border border-slate-700 focus:ring-1 focus:ring-amber-500 font-mono">
            <div id="exp-status-pill" class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                SAFE TO EAT (Fresh)
            </div>
        </div>
    </div>

    <!-- Step by Step Calculation Breakdown -->
    <div id="exp-calc-expl" class="text-xs bg-slate-800/40 p-3 rounded-xl border border-slate-800 text-slate-300 leading-relaxed">
        Manufacturing Month: <strong>January (01)</strong>. Adding 6 months shelf life: 01 + 6 = <strong>July (07)</strong>. Expiry Date = 10 July 2024. Inspection date 15 May 2024 is before July 10, so the product is completely safe.
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Community Lunar Calendars</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Shukla & Krishna Paksha Moon Phases</span>
    </div>

    <!-- Moon Visual Rendering & Phase Name -->
    <div class="flex flex-col sm:flex-row items-center justify-center gap-6 bg-slate-950 p-4 rounded-xl border border-slate-800">
        <!-- Dynamic SVG Moon -->
        <div class="relative w-28 h-28 flex items-center justify-center">
            <svg viewBox="0 0 100 100" class="w-24 h-24 drop-shadow-[0_0_15px_rgba(230,230,250,0.3)]">
                <circle cx="50" cy="50" r="45" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                <path id="moon-phase-path" d="M 50 5 A 45 45 0 0 1 50 95 A 45 45 0 0 1 50 5" fill="#fef08a"/>
            </svg>
        </div>

        <!-- Phase Info Box -->
        <div class="text-center sm:text-left space-y-1">
            <span id="lunar-paksha-tag" class="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Shukla Paksha (Waxing)</span>
            <h4 id="lunar-tithi-title" class="text-base font-bold text-white">Tithi 15: Purnima (Full Moon)</h4>
            <p id="lunar-desc-text" class="text-xs text-slate-400 max-w-xs leading-relaxed">The bright glowing moon fully illuminates the night sky. Celebrated across India with festivals like Raksha Bandhan and Guru Purnima.</p>
        </div>
    </div>

    <!-- Tithi Slider (1 to 30) -->
    <div class="space-y-1 bg-slate-950/60 p-3 rounded-xl border border-slate-800">
        <div class="flex justify-between text-xs text-slate-400">
            <span>Tithi Day: <strong id="lunar-day-val" class="text-purple-300">15</strong> of 30</span>
            <span id="lunar-cycle-pct" class="font-mono text-purple-400">100% Illuminated</span>
        </div>
        <input type="range" id="lunar-slider" min="1" max="30" step="1" value="15" oninput="updateLunarSim(this.value)" class="w-full accent-purple-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-500 font-mono">
            <span>Amavasya (Day 1)</span>
            <span>Waxing Crescent</span>
            <span>Purnima (Day 15)</span>
            <span>Waning Gibbous</span>
            <span>Amavasya (Day 30)</span>
        </div>
    </div>

    <!-- Quick Jump Phase Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <button onclick="updateLunarSim(1)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300">Amavasya (New Moon)</button>
        <button onclick="updateLunarSim(8)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300">Half Moon (Waxing)</button>
        <button onclick="updateLunarSim(15)" class="px-2.5 py-1 rounded bg-purple-600 text-white font-bold">Purnima (Full Moon)</button>
        <button onclick="updateLunarSim(22)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300">Half Moon (Waning)</button>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Daily Routine Wheel</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">24-Hour Circular Schedule Balance</span>
    </div>

    <!-- Interactive Circular SVG 24-Hour Wheel -->
    <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
        <div class="relative w-48 h-48">
            <svg id="routine-svg" viewBox="0 0 200 200" class="w-full h-full transform -rotate-90">
                <!-- SVG sectors dynamically drawn -->
            </svg>
            <div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none text-center">
                <span class="text-lg font-black text-white font-mono">24h</span>
                <span class="text-[9px] uppercase tracking-wider text-slate-400">Total Day</span>
            </div>
        </div>

        <!-- Schedule Breakdown List -->
        <div class="space-y-2 text-xs w-full max-w-xs">
            <div class="flex items-center justify-between p-2 rounded-lg bg-indigo-950/40 border border-indigo-800/40">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500"></span>
                    <span class="text-slate-200 font-medium">Rest & Sleep</span>
                </div>
                <span class="font-mono text-indigo-300 font-bold">8 Hours (1/3 day)</span>
            </div>
            <div class="flex items-center justify-between p-2 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
                    <span class="text-slate-200 font-medium">School & Study</span>
                </div>
                <span class="font-mono text-emerald-300 font-bold">6 Hours (1/4 day)</span>
            </div>
            <div class="flex items-center justify-between p-2 rounded-lg bg-amber-950/40 border border-amber-800/40">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500"></span>
                    <span class="text-slate-200 font-medium">Play & Outdoor Exercise</span>
                </div>
                <span class="font-mono text-amber-300 font-bold">3 Hours (1/8 day)</span>
            </div>
            <div class="flex items-center justify-between p-2 rounded-lg bg-rose-950/40 border border-rose-800/40">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500"></span>
                    <span class="text-slate-200 font-medium">Meals, Family & Hobbies</span>
                </div>
                <span class="font-mono text-rose-300 font-bold">7 Hours</span>
            </div>
        </div>
    </div>

    <div class="text-center text-xs text-slate-400 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
        The circular clock spans all 24 hours of Earth's rotation: <strong>8h + 6h + 3h + 7h = 24 Hours</strong>.
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Twelve Hour Clocks</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">AM vs PM & Day-Night Transition</span>
    </div>

    <!-- Sky Background & Clock Container -->
    <div id="sky-box" class="relative rounded-xl p-5 border border-slate-700 overflow-hidden transition-colors duration-700 bg-gradient-to-b from-sky-900 to-indigo-950 flex flex-col sm:flex-row items-center justify-around gap-4">
        <!-- SVG Analog Clock Face -->
        <div class="relative w-40 h-40">
            <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
                <!-- Dial Outer Ring -->
                <circle cx="50" cy="50" r="46" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
                <!-- Hour Ticks & Numbers -->
                <g font-size="7" font-weight="bold" fill="#94a3b8" text-anchor="middle" dominant-baseline="central">
                    <text x="50" y="14">12</text>
                    <text x="70" y="19">1</text>
                    <text x="83" y="32">2</text>
                    <text x="88" y="50">3</text>
                    <text x="83" y="68">4</text>
                    <text x="70" y="81">5</text>
                    <text x="50" y="86">6</text>
                    <text x="30" y="81">7</text>
                    <text x="17" y="68">8</text>
                    <text x="12" y="50">9</text>
                    <text x="17" y="32">10</text>
                    <text x="30" y="19">11</text>
                </g>
                <!-- Hands -->
                <line id="sim6-hour-hand" x1="50" y1="50" x2="50" y2="28" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                <line id="sim6-min-hand" x1="50" y1="50" x2="50" y2="18" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
                <circle cx="50" cy="50" r="3" fill="#ffffff"/>
            </svg>
        </div>

        <!-- Time Readout & Meridian Info -->
        <div class="text-center sm:text-left space-y-2">
            <div class="space-y-0.5">
                <div class="text-[10px] uppercase font-mono tracking-wider text-slate-300">Current Time Display</div>
                <div id="sim6-digital-time" class="text-3xl font-black text-white font-mono">07:00 AM</div>
            </div>
            <div id="sim6-meridian-badge" class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                AM (Ante Meridiem — Morning)
            </div>
            <p id="sim6-desc-note" class="text-xs text-slate-200 max-w-xs leading-relaxed">
                The morning sun is rising. Morning activities occur between midnight and 12:00 noon.
            </p>
        </div>
    </div>

    <!-- Quick Time Switchers -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setTwelveHourSim(7, 0, 'AM', 'Morning Sun')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">07:00 AM (Morning)</button>
        <button onclick="setTwelveHourSim(12, 0, 'PM', 'Midday Noon')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">12:00 PM (Noon)</button>
        <button onclick="setTwelveHourSim(3, 30, 'PM', 'Afternoon Study')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">03:30 PM (Afternoon)</button>
        <button onclick="setTwelveHourSim(7, 0, 'PM', 'Sunset Dusk')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">07:00 PM (Evening)</button>
        <button onclick="setTwelveHourSim(12, 0, 'AM', 'Midnight Stars')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">12:00 AM (Midnight)</button>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Digital Clock Formats</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">12-Hour vs 24-Hour Railway Time</span>
    </div>

    <!-- Interactive Converter Box -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <!-- 12-Hour Side -->
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center space-y-3">
            <span class="text-xs uppercase font-mono text-emerald-400 font-semibold">12-Hour Standard Clock</span>
            <div class="flex items-center justify-center gap-2 font-mono">
                <input type="number" id="conv-hh" min="1" max="12" value="8" onchange="runClockConverter()" class="w-16 bg-slate-800 text-white text-center text-xl font-bold py-1.5 rounded-lg border border-slate-700">
                <span class="text-xl font-bold text-slate-400">:</span>
                <input type="number" id="conv-mm" min="0" max="59" value="30" onchange="runClockConverter()" class="w-16 bg-slate-800 text-white text-center text-xl font-bold py-1.5 rounded-lg border border-slate-700">
                <button id="conv-meridiem-btn" onclick="toggleConverterMeridiem()" class="px-3 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm">PM</button>
            </div>
            <div id="conv-12h-str" class="text-lg font-black text-white font-mono">08:30 PM</div>
        </div>

        <!-- 24-Hour Railway Side -->
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center space-y-3">
            <span class="text-xs uppercase font-mono text-cyan-400 font-semibold">24-Hour Railway Clock</span>
            <div class="text-xs text-slate-400 font-mono" id="conv-math-rule">Calculation: 8 + 12 = 20</div>
            <div id="conv-24h-str" class="text-3xl font-black text-cyan-300 font-mono tracking-widest mt-2">20:30 Hours</div>
            <div class="text-[11px] text-slate-400">Zero ambiguity; no AM or PM required.</div>
        </div>
    </div>

    <!-- Preset Trains & Flights -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <span class="text-slate-400 text-[11px]">Schedules:</span>
        <button onclick="setConvPreset(6, 15, 'AM')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">06:15 AM → 06:15</button>
        <button onclick="setConvPreset(12, 0, 'PM')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">12:00 PM → 12:00</button>
        <button onclick="setConvPreset(8, 30, 'PM')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">08:30 PM → 20:30</button>
        <button onclick="setConvPreset(11, 45, 'PM')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">11:45 PM → 23:45</button>
        <button onclick="setConvPreset(12, 0, 'AM')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">12:00 AM → 00:00</button>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Elapsed Time Intervals</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Milestone Jumps & Duration Calculation</span>
    </div>

    <!-- Benchmark Jump Diagram -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs font-mono text-slate-400">
            <span>Start: <strong class="text-emerald-400 text-sm">06:15 AM</strong></span>
            <span class="text-amber-300 font-bold">Milestone: 07:00 AM</span>
            <span>Arrival: <strong class="text-rose-400 text-sm">07:40 AM</strong></span>
        </div>

        <!-- Visual Milestone Bar -->
        <div class="relative h-10 bg-slate-900 rounded-xl overflow-hidden flex border border-slate-700 text-xs font-mono font-bold">
            <!-- Jump 1: 06:15 to 07:00 (45m) -->
            <div class="w-[53%] bg-emerald-600/30 border-r-2 border-dashed border-amber-400 flex items-center justify-center text-emerald-300">
                +45 min (to 07:00)
            </div>
            <!-- Jump 2: 07:00 to 07:40 (40m) -->
            <div class="w-[47%] bg-rose-600/30 flex items-center justify-center text-rose-300">
                +40 min (to 07:40)
            </div>
        </div>

        <div class="flex justify-between text-[11px] text-slate-400 font-mono">
            <span>06:15</span>
            <span class="text-amber-400 font-bold">07:00 (Next Full Hour)</span>
            <span>07:40</span>
        </div>
    </div>

    <!-- Total Duration Result Card -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 space-y-1">
            <span class="text-[10px] uppercase font-mono text-slate-400">Additive Equation</span>
            <div class="text-sm font-bold text-white font-mono">45 min + 40 min = 85 minutes</div>
            <div class="text-[11px] text-slate-400">Break down across the nearest hour boundary.</div>
        </div>
        <div class="bg-indigo-950/40 p-3 rounded-xl border border-indigo-800/60 space-y-1">
            <span class="text-[10px] uppercase font-mono text-indigo-400">Simplified Duration</span>
            <div class="text-base font-bold text-indigo-200 font-mono">1 Hour 25 Minutes</div>
            <div class="text-[11px] text-slate-300">85 min = 60 min (1 hr) + 25 min</div>
        </div>
    </div>
</div>
"""

simulators_part1 = {1: sim1, 2: sim2, 3: sim3, 4: sim4, 5: sim5, 6: sim6, 7: sim7, 8: sim8}

# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 12 Simulators Dictionary"""

SIMULATORS = {
    1: '''
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
''',
    2: '''
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
        <button onclick="setDatePreset(14, 11, 2025, 'Children's Day')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">14 Nov 2025</button>
    </div>
</div>
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}

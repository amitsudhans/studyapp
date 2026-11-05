# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 6: Measuring Length
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Health Checkup Stadiometer</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Height & Scale Meter</span>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3">
        <button onclick="setStudentHeight(115)" class="h-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700">115 cm</button>
        <button onclick="setStudentHeight(128)" class="h-btn px-3 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs transition shadow">128 cm</button>
        <button onclick="setStudentHeight(135)" class="h-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700">135 cm</button>
        <button onclick="setStudentHeight(142)" class="h-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700">142 cm</button>
    </div>

    <!-- Interactive Stadiometer SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="stadiometerSvg" viewBox="0 0 360 200" class="w-full max-w-[340px] h-auto">
            <!-- Floor -->
            <rect x="20" y="180" width="320" height="10" fill="#334155" rx="3"/>
            <!-- Stadiometer Back Bar -->
            <rect x="80" y="20" width="24" height="160" fill="#1e293b" stroke="#475569" stroke-width="2" rx="4"/>
            <!-- Tick marks on ruler bar -->
            <line x1="84" y1="30" x2="100" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="106" y="34" fill="#94a3b8" font-size="8">150</text>
            <line x1="84" y1="65" x2="98" y2="65" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="106" y="69" fill="#94a3b8" font-size="8">135</text>
            <line x1="84" y1="100" x2="100" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="106" y="104" fill="#94a3b8" font-size="8">120</text>
            <line x1="84" y1="135" x2="98" y2="135" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="106" y="139" fill="#94a3b8" font-size="8">105</text>
            <line x1="84" y1="170" x2="100" y2="170" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="106" y="174" fill="#94a3b8" font-size="8">90</text>

            <!-- Student Silhouette -->
            <g id="studentSilhouette">
                <circle id="studentHead" cx="180" cy="85" r="18" fill="#38bdf8"/>
                <rect id="studentBody" x="165" y="103" width="30" height="77" rx="6" fill="#0284c7"/>
            </g>

            <!-- Movable Headpiece Cursor -->
            <g id="stadiometerHeadpiece" transform="translate(0, 0)">
                <polygon points="76,67 195,67 195,73 104,73 104,80 76,80" fill="#f59e0b" stroke="#d97706" stroke-width="1"/>
                <line x1="76" y1="67" x2="220" y2="67" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3 3"/>
            </g>

            <!-- Dimension callout -->
            <rect x="230" y="45" width="115" height="55" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="287" y="66" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Recorded Height</text>
            <text id="stadiometerText" x="287" y="88" fill="#f8fafc" font-size="14" font-weight="extrabold" text-anchor="middle">128 cm</text>
        </svg>

        <div id="stadiometerDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Recorded height: <span class="text-teal-400 font-bold">128 cm</span> = <span class="text-amber-400 font-bold">1 metre 28 centimetres</span>
        </div>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">1-Metre Classroom Benchmark</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Compare with 1 Metre</span>
    </div>

    <!-- Item selection -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="compareMetre('door')" id="btn-bench-door" class="bench-btn px-2.5 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs transition">Door Height</button>
        <button onclick="compareMetre('board')" id="btn-bench-board" class="bench-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">Blackboard</button>
        <button onclick="compareMetre('table')" id="btn-bench-table" class="bench-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">Study Desk</button>
        <button onclick="compareMetre('duster')" id="btn-bench-duster" class="bench-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">Felt Duster</button>
    </div>

    <!-- Visual Benchmarking SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="benchmarkSvg" viewBox="0 0 360 200" class="w-full max-w-[340px] h-auto">
            <!-- Floor line -->
            <line x1="20" y1="180" x2="340" y2="180" stroke="#475569" stroke-width="2"/>

            <!-- 1 Metre Standard Reference Rod -->
            <g id="standard1mRod" transform="translate(60, 0)">
                <rect x="0" y="80" width="16" height="100" fill="#f59e0b" rx="3" stroke="#b45309" stroke-width="1.5"/>
                <text x="8" y="135" fill="#1e293b" font-size="10" font-weight="extrabold" text-anchor="middle" transform="rotate(-90 8 135)">1 METRE</text>
            </g>

            <!-- Dynamic Comparison Object Container -->
            <g id="benchObjectGroup">
                <!-- Door Default (Height 200 cm = 2m) -->
                <rect x="180" y="30" width="70" height="150" fill="#818cf8" fill-opacity="0.25" stroke="#818cf8" stroke-width="2" rx="4"/>
                <circle cx="235" cy="110" r="4" fill="#fbbf24"/>
                <line x1="160" y1="30" x2="160" y2="180" stroke="#a5b4fc" stroke-width="1.5" stroke-dasharray="3 3"/>
                <text x="215" y="20" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Door Height: ~2 Metres</text>
            </g>

            <!-- Comparison Verdict Badge -->
            <rect x="220" y="130" width="125" height="40" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text id="benchVerdict" x="282" y="155" fill="#c7d2fe" font-size="12" font-weight="bold" text-anchor="middle">Greater than 1 m</text>
        </svg>

        <div id="benchDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            A classroom door measures about 2 metres, which is <span class="text-emerald-400 font-bold">longer than 1 metre</span>.
        </div>
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Modular Fraction Ropes</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">1m, 1/2m, 1/4m Combiner</span>
    </div>

    <!-- Rope Fraction Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setRopeMode('half_half')" id="btn-rope-1" class="rope-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs transition shadow">1/2 m + 1/2 m</button>
        <button onclick="setRopeMode('quarter_quarter')" id="btn-rope-2" class="rope-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">1/4 m + 1/4 m</button>
        <button onclick="setRopeMode('four_quarters')" id="btn-rope-3" class="rope-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">4 × 1/4 m</button>
        <button onclick="setRopeMode('half_quarter')" id="btn-rope-4" class="rope-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">1/2 m + 1/4 m</button>
    </div>

    <!-- Rope Visual SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="ropeFractionSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Reference 1-Metre Rope at Top -->
            <text x="20" y="25" fill="#94a3b8" font-size="10" font-weight="bold">Standard 1 Metre Reference (100 cm):</text>
            <rect x="20" y="32" width="320" height="14" rx="4" fill="#3b82f6" fill-opacity="0.3" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="180" y="43" fill="#bfdbfe" font-size="9" font-weight="bold" text-anchor="middle">1 Metre = 100 cm</text>

            <!-- Knot markers at 1/4, 1/2, 3/4 -->
            <circle cx="100" cy="39" r="3" fill="#fbbf24"/>
            <circle cx="180" cy="39" r="3" fill="#fbbf24"/>
            <circle cx="260" cy="39" r="3" fill="#fbbf24"/>

            <!-- Modular Segments Display -->
            <g id="ropeSegmentsGroup" transform="translate(0, 40)">
                <!-- Default 1/2 + 1/2 -->
                <text x="20" y="45" fill="#34d399" font-size="10" font-weight="bold">Active Combined Rope:</text>
                <rect x="20" y="55" width="160" height="22" rx="4" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
                <text x="100" y="70" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">1/2 m (50 cm)</text>

                <rect x="180" y="55" width="160" height="22" rx="4" fill="#059669" fill-opacity="0.35" stroke="#059669" stroke-width="2"/>
                <text x="260" y="70" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">1/2 m (50 cm)</text>
                <!-- Joining knot -->
                <circle cx="180" cy="66" r="5" fill="#f59e0b"/>
            </g>
        </svg>

        <div id="ropeFractionDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            <span class="text-emerald-400 font-bold">50 cm + 50 cm = 100 cm</span> = Exactly <span class="text-amber-400 font-bold">1 Metre</span>!
        </div>
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Walking & Jumping Track</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Paces vs Metre Lines</span>
    </div>

    <!-- Distance Options -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setWalkDistance(1)" id="btn-walk-1m" class="walk-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">1 Metre</button>
        <button onclick="setWalkDistance(5)" id="btn-walk-5m" class="walk-btn px-3.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition">5 Metres</button>
        <button onclick="setWalkDistance(10)" id="btn-walk-10m" class="walk-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">10 Metres</button>
    </div>

    <!-- Visual Track SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="walkTrackSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Starting Mark -->
            <rect x="25" y="30" width="6" height="110" fill="#22c55e" rx="2"/>
            <text x="28" y="22" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">START</text>

            <!-- Finish Mark -->
            <rect x="330" y="30" width="6" height="110" fill="#ef4444" rx="2"/>
            <text x="333" y="22" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">END</text>

            <!-- Track Lane -->
            <rect x="30" y="60" width="300" height="50" fill="#0f172a" stroke="#334155" stroke-width="2"/>
            <line x1="30" y1="85" x2="330" y2="85" stroke="#475569" stroke-width="1.5" stroke-dasharray="6 6"/>

            <!-- Step Footprints Group -->
            <g id="footprintsGroup">
                <!-- 5 Steps along the 5m line -->
                <circle cx="90" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/>
                <text x="90" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">1</text>
                <circle cx="150" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/>
                <text x="150" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">2</text>
                <circle cx="210" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/>
                <text x="210" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">3</text>
                <circle cx="270" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/>
                <text x="270" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">4</text>
                <circle cx="330" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/>
                <text x="330" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">5</text>
            </g>

            <!-- Dimension Tape -->
            <line x1="30" y1="135" x2="330" y2="135" stroke="#f59e0b" stroke-width="2"/>
            <line x1="30" y1="128" x2="30" y2="142" stroke="#f59e0b" stroke-width="2"/>
            <line x1="330" y1="128" x2="330" y2="142" stroke="#f59e0b" stroke-width="2"/>
            <text id="walkTrackDimText" x="180" y="152" fill="#fbbf24" font-size="12" font-weight="extrabold" text-anchor="middle">Total Distance: 5 Metres</text>
        </svg>

        <div id="walkTrackDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Covering 5 metres requires about <span class="text-cyan-400 font-bold">5 large steps (1m each)</span> or <span class="text-amber-400 font-bold">10 normal paces (50cm each)</span>.
        </div>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Long Jump Sand Pit</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Jump & Tape Measure</span>
    </div>

    <!-- Jump Power Buttons -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="triggerJump(120)" class="jump-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">1 m 20 cm</button>
        <button onclick="triggerJump(165)" class="jump-btn px-3 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow transition">1 m 65 cm</button>
        <button onclick="triggerJump(210)" class="jump-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">2 m 10 cm</button>
    </div>

    <!-- Long Jump SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="longJumpSvg" viewBox="0 0 360 190" class="w-full max-w-[340px] h-auto">
            <!-- Takeoff Board -->
            <rect x="30" y="60" width="18" height="80" fill="#f59e0b" rx="2" stroke="#d97706" stroke-width="1.5"/>
            <text x="39" y="155" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Board</text>

            <!-- Sand Pit Area -->
            <rect x="52" y="60" width="290" height="80" fill="#d97706" fill-opacity="0.2" stroke="#b45309" stroke-width="2" rx="4"/>
            <!-- Sand texture dots -->
            <circle cx="80" cy="85" r="1.5" fill="#f59e0b" opacity="0.4"/>
            <circle cx="140" cy="110" r="1.5" fill="#f59e0b" opacity="0.4"/>
            <circle cx="200" cy="75" r="1.5" fill="#f59e0b" opacity="0.4"/>
            <circle cx="270" cy="120" r="1.5" fill="#f59e0b" opacity="0.4"/>

            <!-- Jump Arc Path -->
            <path id="jumpTrajectory" d="M 48 95 Q 140 20 220 100" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4"/>

            <!-- Landing Mark in Sand -->
            <g id="landingMarkGroup" transform="translate(0, 0)">
                <ellipse id="sandDent" cx="220" cy="100" rx="16" ry="8" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
                <text x="220" y="85" fill="#fef08a" font-size="10" font-weight="extrabold" text-anchor="middle">Landing</text>
            </g>

            <!-- Stretched Tape Measure -->
            <line id="jumpTape" x1="48" y1="125" x2="220" y2="125" stroke="#ef4444" stroke-width="2.5"/>
            <circle cx="48" cy="125" r="4" fill="#ef4444"/>
            <circle id="jumpTapeEnd" cx="220" cy="125" r="4" fill="#ef4444"/>
            <text id="jumpTapeText" x="134" y="142" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">1 m 65 cm</text>
        </svg>

        <div id="longJumpDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Recorded jump: <span class="text-orange-400 font-bold">1 m 65 cm</span> = <span class="text-yellow-300 font-bold">165 centimetres</span> total distance!
        </div>
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Animal Length Scales</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Comparative Scale Runway</span>
    </div>

    <!-- Animal Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectAnimalScale('whale')" id="btn-scale-whale" class="scale-btn px-2.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs transition">Blue Whale (30m)</button>
        <button onclick="selectAnimalScale('bus')" id="btn-scale-bus" class="scale-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Bus (10m)</button>
        <button onclick="selectAnimalScale('croc')" id="btn-scale-croc" class="scale-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Crocodile (4m)</button>
        <button onclick="selectAnimalScale('ostrich')" id="btn-scale-ostrich" class="scale-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Ostrich (2.5m)</button>
    </div>

    <!-- Comparative Scale SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="animalScaleSvg" viewBox="0 0 360 190" class="w-full max-w-[340px] h-auto">
            <!-- 35 Metre Scale Ruler Line at bottom -->
            <line x1="20" y1="150" x2="340" y2="150" stroke="#64748b" stroke-width="2"/>
            <text x="20" y="166" fill="#94a3b8" font-size="9">0m</text>
            <text x="127" y="166" fill="#94a3b8" font-size="9">10m</text>
            <text x="233" y="166" fill="#94a3b8" font-size="9">20m</text>
            <text x="340" y="166" fill="#94a3b8" font-size="9">30m</text>

            <!-- Major tick marks -->
            <line x1="20" y1="145" x2="20" y2="155" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="127" y1="145" x2="127" y2="155" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="233" y1="145" x2="233" y2="155" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="340" y1="145" x2="340" y2="155" stroke="#94a3b8" stroke-width="1.5"/>

            <!-- Animal Graphic / Bar container -->
            <g id="animalGraphicGroup">
                <!-- Blue Whale (Default 30m = width 320) -->
                <rect x="20" y="60" width="320" height="50" rx="25" fill="#3b82f6" fill-opacity="0.35" stroke="#3b82f6" stroke-width="2"/>
                <circle cx="315" cy="80" r="3" fill="#ffffff"/>
                <path d="M 20 85 L 10 70 L 10 100 Z" fill="#3b82f6"/>
                <text x="180" y="90" fill="#bfdbfe" font-size="13" font-weight="bold" text-anchor="middle">Blue Whale: 30 Metres Long</text>
            </g>
        </svg>

        <div id="animalScaleDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            A gigantic Blue Whale spans <span class="text-blue-400 font-bold">30 metres</span>, equivalent to three 10-metre buses parked end-to-end!
        </div>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Length Ratio Puzzle</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Multiplier Comparison</span>
    </div>

    <!-- Puzzle Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button onclick="setRatioPuzzle('whale_bus')" id="btn-ratio-1" class="ratio-btn px-2.5 py-1.5 rounded-xl bg-pink-600 text-white font-bold text-xs transition">Whale vs Bus</button>
        <button onclick="setRatioPuzzle('bus_croc')" id="btn-ratio-2" class="ratio-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Bus vs Desk (2m)</button>
        <button onclick="setRatioPuzzle('croc_cat')" id="btn-ratio-3" class="ratio-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Desk vs Ruler</button>
    </div>

    <!-- Visual Ratio Breakdown SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="ratioPuzzleSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Target Object (e.g. 30m Whale) -->
            <rect x="20" y="30" width="320" height="35" rx="6" fill="#ec4899" fill-opacity="0.25" stroke="#ec4899" stroke-width="2"/>
            <text x="180" y="52" fill="#fbcfe8" font-size="12" font-weight="bold" text-anchor="middle">Total Target: 30 Metres (Whale)</text>

            <!-- Unit Blocks (e.g. 3 Buses of 10m each) -->
            <g id="ratioBlocksGroup">
                <rect x="20" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/>
                <text x="70" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 1 (10m)</text>

                <rect x="130" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/>
                <text x="180" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 2 (10m)</text>

                <rect x="240" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/>
                <text x="290" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 3 (10m)</text>
            </g>

            <!-- Mathematical Equation -->
            <text id="ratioMathText" x="180" y="155" fill="#f472b6" font-size="12" font-weight="extrabold" text-anchor="middle">30 m ÷ 10 m = 3 Times</text>
        </svg>

        <div id="ratioPuzzleDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            A 30-metre blue whale is exactly <span class="text-pink-400 font-bold">3 times as long</span> as a 10-metre school bus!
        </div>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Centimetre Ruler Explorer</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Measuring Classroom Items</span>
    </div>

    <!-- Object Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="measureSmallItem('eraser')" id="btn-item-eraser" class="item-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">Eraser (4 cm)</button>
        <button onclick="measureSmallItem('sharpener')" id="btn-item-sharpener" class="item-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Sharpener (3 cm)</button>
        <button onclick="measureSmallItem('pencil')" id="btn-item-pencil" class="item-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Pencil (12 cm)</button>
        <button onclick="measureSmallItem('clip')" id="btn-item-clip" class="item-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Paperclip (5 cm)</button>
    </div>

    <!-- Ruler and Object SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="rulerMeasureSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- 15-cm Ruler Body -->
            <rect x="20" y="90" width="320" height="55" rx="4" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
            
            <!-- Ruler centimeter tick marks from 0 to 15 (width=300px, 20px per cm) -->
            <!-- 0 cm at x=30, 15 cm at x=330 -->
            <g stroke="#78350f" stroke-width="1.5">
                <line x1="30" y1="90" x2="30" y2="110"/>
                <line x1="50" y1="90" x2="50" y2="104"/>
                <line x1="70" y1="90" x2="70" y2="104"/>
                <line x1="90" y1="90" x2="90" y2="104"/>
                <line x1="110" y1="90" x2="110" y2="110"/>
                <line x1="130" y1="90" x2="130" y2="104"/>
                <line x1="150" y1="90" x2="150" y2="104"/>
                <line x1="170" y1="90" x2="170" y2="104"/>
                <line x1="190" y1="90" x2="190" y2="110"/>
                <line x1="210" y1="90" x2="210" y2="104"/>
                <line x1="230" y1="90" x2="230" y2="104"/>
                <line x1="250" y1="90" x2="250" y2="104"/>
                <line x1="270" y1="90" x2="270" y2="110"/>
                <line x1="290" y1="90" x2="290" y2="104"/>
                <line x1="310" y1="90" x2="310" y2="104"/>
                <line x1="330" y1="90" x2="330" y2="110"/>
            </g>

            <!-- Numbers on ruler -->
            <text x="30" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">0</text>
            <text x="70" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">2</text>
            <text x="110" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">4</text>
            <text x="150" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">6</text>
            <text x="190" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">8</text>
            <text x="230" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">10</text>
            <text x="270" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">12</text>
            <text x="330" y="125" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">15</text>
            <text x="320" y="138" fill="#78350f" font-size="8" font-style="italic">cm</text>

            <!-- Active Object (Default Eraser = 4cm = 80px) -->
            <g id="activeSmallItem" transform="translate(0, 0)">
                <rect x="30" y="45" width="80" height="35" rx="5" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
                <text x="70" y="67" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Eraser</text>
                <!-- Guideline from 0 to 4 -->
                <line x1="30" y1="45" x2="30" y2="90" stroke="#0284c7" stroke-dasharray="2 2"/>
                <line x1="110" y1="45" x2="110" y2="90" stroke="#0284c7" stroke-dasharray="2 2"/>
            </g>
        </svg>

        <div id="rulerMeasureDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Aligned from mark 0 to mark 4: <span class="text-amber-400 font-bold">Length = 4 centimetres (4 cm)</span>
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


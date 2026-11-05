# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 6 Simulators"""

simulators = {
    1: '''
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
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Metre Scale Division</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">100 Centimetre Breakdown</span>
    </div>

    <!-- Division Breakdown Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setMetreDivision('full')" id="btn-div-full" class="div-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition">1 Whole Metre</button>
        <button onclick="setMetreDivision('half')" id="btn-div-half" class="div-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">1/2 Metre (50 cm)</button>
        <button onclick="setMetreDivision('quarter')" id="btn-div-quarter" class="div-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">1/4 Metre (25 cm)</button>
        <button onclick="setMetreDivision('three_quarter')" id="btn-div-three" class="div-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">3/4 Metre (75 cm)</button>
    </div>

    <!-- Scale Division SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="metreDivisionSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- 100 cm Wooden Metre Stick -->
            <rect x="20" y="55" width="320" height="40" rx="4" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
            
            <!-- 10-cm division marks (320px width = 3.2px per cm; 10cm = 32px) -->
            <g stroke="#713f12" stroke-width="1.5">
                <line x1="20" y1="55" x2="20" y2="95"/>
                <line x1="52" y1="55" x2="52" y2="85"/><text x="52" y="77" fill="#fef08a" font-size="8" text-anchor="middle">10</text>
                <line x1="84" y1="55" x2="84" y2="85"/><text x="84" y="77" fill="#fef08a" font-size="8" text-anchor="middle">20</text>
                <line x1="100" y1="55" x2="100" y2="95" stroke-width="2"/><text x="100" y="80" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">25</text>
                <line x1="116" y1="55" x2="116" y2="85"/><text x="116" y="77" fill="#fef08a" font-size="8" text-anchor="middle">30</text>
                <line x1="148" y1="55" x2="148" y2="85"/><text x="148" y="77" fill="#fef08a" font-size="8" text-anchor="middle">40</text>
                <line x1="180" y1="55" x2="180" y2="95" stroke-width="2.5"/><text x="180" y="80" fill="#ffffff" font-size="9" font-weight="extrabold" text-anchor="middle">50</text>
                <line x1="212" y1="55" x2="212" y2="85"/><text x="212" y="77" fill="#fef08a" font-size="8" text-anchor="middle">60</text>
                <line x1="244" y1="55" x2="244" y2="85"/><text x="244" y="77" fill="#fef08a" font-size="8" text-anchor="middle">70</text>
                <line x1="260" y1="55" x2="260" y2="95" stroke-width="2"/><text x="260" y="80" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">75</text>
                <line x1="276" y1="55" x2="276" y2="85"/><text x="276" y="77" fill="#fef08a" font-size="8" text-anchor="middle">80</text>
                <line x1="308" y1="55" x2="308" y2="85"/><text x="308" y="77" fill="#fef08a" font-size="8" text-anchor="middle">90</text>
                <line x1="340" y1="55" x2="340" y2="95"/>
            </g>

            <!-- Highlight Overlay Box -->
            <rect id="metreHighlightBox" x="20" y="55" width="320" height="40" rx="4" fill="#22c55e" fill-opacity="0.3" stroke="#16a34a" stroke-width="2"/>

            <!-- Dimension Bracket / Callout -->
            <path id="metreBracket" d="M 20 115 L 20 125 L 180 125 L 180 135 L 180 125 L 340 125 L 340 115" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="metreDivisionText" x="180" y="152" fill="#38bdf8" font-size="12" font-weight="extrabold" text-anchor="middle">100 cm = 1 Metre</text>
        </svg>

        <div id="metreDivisionDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            A standard metre stick contains exactly <span class="text-emerald-400 font-bold">100 centimetres</span>.
        </div>
    </div>
</div>
''',
    10: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Estimation vs Measurement</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Guess, Measure & Compare</span>
    </div>

    <!-- Object Selection -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setEstItem('book')" id="btn-est-book" class="est-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">Math Book</button>
        <button onclick="setEstItem('bottle')" id="btn-est-bottle" class="est-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Water Bottle</button>
        <button onclick="setEstItem('box')" id="btn-est-box" class="est-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Pencil Box</button>
        <button onclick="setEstItem('handspan')" id="btn-est-handspan" class="est-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Hand Span</button>
    </div>

    <!-- Interactive Comparison SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="estMeasureSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Estimated Length Bar -->
            <text x="30" y="38" fill="#fbbf24" font-size="11" font-weight="bold">Estimated Length (Eye Guess):</text>
            <rect id="estBar" x="30" y="48" width="180" height="25" rx="4" fill="#f59e0b" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
            <text id="estValText" x="220" y="65" fill="#fef08a" font-size="11" font-weight="bold">25 cm</text>

            <!-- Actual Measured Length Bar -->
            <text x="30" y="105" fill="#38bdf8" font-size="11" font-weight="bold">Actual Measured Length (Ruler):</text>
            <rect id="actBar" x="30" y="115" width="200" height="25" rx="4" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="2"/>
            <text id="actValText" x="240" y="132" fill="#bae6fd" font-size="11" font-weight="bold">28 cm</text>

            <!-- Difference Callout -->
            <text id="diffCalloutText" x="180" y="165" fill="#a7f3d0" font-size="11" font-weight="extrabold" text-anchor="middle">Difference: 3 cm (Close Estimation!)</text>
        </svg>

        <div id="estMeasureDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Estimating develops spatial sense, while precise ruler verification confirms accuracy.
        </div>
    </div>
</div>
''',
    11: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Toy Car Ramp Distance</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Roll Distance Analyzer</span>
    </div>

    <!-- Surface / Ramp Controls -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="launchCar('smooth')" id="btn-car-smooth" class="car-btn px-3 py-1.5 rounded-xl bg-red-500 text-white font-bold text-xs shadow transition">Smooth Tile (95 cm)</button>
        <button onclick="launchCar('wood')" id="btn-car-wood" class="car-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Wood Board (65 cm)</button>
        <button onclick="launchCar('carpet')" id="btn-car-carpet" class="car-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Carpet (35 cm)</button>
    </div>

    <!-- Ramp & Roll Runway SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="carRampSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Ramp Triangle -->
            <polygon points="20,130 80,130 80,70" fill="#475569" stroke="#64748b" stroke-width="2"/>
            <line x1="20" y1="130" x2="80" y2="70" stroke="#f87171" stroke-width="3"/>

            <!-- Floor Tape Measure -->
            <rect x="80" y="130" width="260" height="15" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
            <!-- Ticks on tape -->
            <line x1="80" y1="130" x2="80" y2="140" stroke="#854d0e"/>
            <text x="80" y="143" fill="#854d0e" font-size="7">0</text>
            <line x1="160" y1="130" x2="160" y2="140" stroke="#854d0e"/>
            <text x="160" y="143" fill="#854d0e" font-size="7">50cm</text>
            <line x1="240" y1="130" x2="240" y2="140" stroke="#854d0e"/>
            <text x="240" y="143" fill="#854d0e" font-size="7">100cm</text>
            <line x1="320" y1="130" x2="320" y2="140" stroke="#854d0e"/>
            <text x="320" y="143" fill="#854d0e" font-size="7">150cm</text>

            <!-- Toy Car Graphic -->
            <g id="toyCarGraphic" transform="translate(152, 0)">
                <!-- Car body -->
                <rect x="75" y="108" width="28" height="15" rx="3" fill="#ef4444"/>
                <rect x="81" y="102" width="16" height="8" rx="2" fill="#fee2e2"/>
                <!-- Wheels -->
                <circle cx="81" cy="125" r="4.5" fill="#1e293b"/>
                <circle cx="97" cy="125" r="4.5" fill="#1e293b"/>
            </g>

            <!-- Distance Dimension line -->
            <line id="carDistanceLine" x1="80" y1="95" x2="232" y2="95" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="80" cy="95" r="3" fill="#38bdf8"/>
            <circle id="carDistanceLineEnd" cx="232" cy="95" r="3" fill="#38bdf8"/>
            <text id="carDistanceText" x="156" y="88" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Distance: 95 cm</text>
        </svg>

        <div id="carRampDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            On smooth tiles with low friction, the toy car rolled <span class="text-red-400 font-bold">95 cm</span>!
        </div>
    </div>
</div>
''',
    12: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Treasure Grid Routes</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">1 cm Grid Pathfinder</span>
    </div>

    <!-- Route Selector -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="selectGridRoute('routeA')" id="btn-grid-a" class="grid-btn px-3 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow transition">Route A (Direct: 8 cm)</button>
        <button onclick="selectGridRoute('routeB')" id="btn-grid-b" class="grid-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Route B (Detour: 12 cm)</button>
        <button onclick="selectGridRoute('routeC')" id="btn-grid-c" class="grid-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Route C (Scenic: 16 cm)</button>
    </div>

    <!-- 1cm Grid SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="treasureGridSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Grid Lines (12 x 5 squares, each 25px) -->
            <g stroke="#334155" stroke-width="1" opacity="0.6">
                <!-- Horizontals -->
                <line x1="30" y1="25" x2="330" y2="25"/>
                <line x1="30" y1="55" x2="330" y2="55"/>
                <line x1="30" y1="85" x2="330" y2="85"/>
                <line x1="30" y1="115" x2="330" y2="115"/>
                <line x1="30" y1="145" x2="330" y2="145"/>
                <!-- Verticals -->
                <line x1="30" y1="25" x2="30" y2="145"/>
                <line x1="60" y1="25" x2="60" y2="145"/>
                <line x1="90" y1="25" x2="90" y2="145"/>
                <line x1="120" y1="25" x2="120" y2="145"/>
                <line x1="150" y1="25" x2="150" y2="145"/>
                <line x1="180" y1="25" x2="180" y2="145"/>
                <line x1="210" y1="25" x2="210" y2="145"/>
                <line x1="240" y1="25" x2="240" y2="145"/>
                <line x1="270" y1="25" x2="270" y2="145"/>
                <line x1="300" y1="25" x2="300" y2="145"/>
                <line x1="330" y1="25" x2="330" y2="145"/>
            </g>

            <!-- Start Point (Classroom) -->
            <circle cx="60" cy="115" r="9" fill="#10b981"/>
            <text x="60" y="119" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">S</text>

            <!-- Treasure Chest Point -->
            <rect x="290" y="45" width="20" height="18" rx="3" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <text x="300" y="58" fill="#1e293b" font-size="10" font-weight="extrabold" text-anchor="middle">★</text>

            <!-- Dynamic Route Polyline -->
            <polyline id="gridRoutePath" points="60,115 150,115 150,55 300,55" fill="none" stroke="#a855f7" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>

        <div id="treasureGridDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Route A: <span class="text-purple-400 font-bold">8 grid cm on map</span> = <span class="text-amber-400 font-bold">16 metres on actual school ground</span> (Scale: 1 cm = 2 m).
        </div>
    </div>
</div>
''',
    13: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Broken Ruler Challenge</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Subtract Initial Coordinate</span>
    </div>

    <!-- Broken Case Buttons -->
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setBrokenCase('caseA')" id="btn-broken-a" class="broken-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs transition shadow">Starts at 3 cm</button>
        <button onclick="setBrokenCase('caseB')" id="btn-broken-b" class="broken-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Starts at 5 cm</button>
        <button onclick="setBrokenCase('caseC')" id="btn-broken-c" class="broken-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Starts at 7 cm</button>
    </div>

    <!-- Broken Ruler SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="brokenRulerSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Jagged broken left edge -->
            <path d="M 60 70 L 68 80 L 58 90 L 70 100 L 60 110 L 68 125 L 330 125 L 330 70 Z" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
            
            <!-- Ticks from 3 cm to 15 cm -->
            <!-- 20px per cm: mark 3 at x=80, 4 at 100, 5 at 120, etc. -->
            <g stroke="#78350f" stroke-width="1.5">
                <line x1="80" y1="70" x2="80" y2="88"/><text x="80" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">3</text>
                <line x1="120" y1="70" x2="120" y2="88"/><text x="120" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">5</text>
                <line x1="160" y1="70" x2="160" y2="88"/><text x="160" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">7</text>
                <line x1="200" y1="70" x2="200" y2="88"/><text x="200" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">9</text>
                <line x1="240" y1="70" x2="240" y2="88"/><text x="240" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">11</text>
                <line x1="280" y1="70" x2="280" y2="88"/><text x="280" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">13</text>
                <line x1="320" y1="70" x2="320" y2="88"/><text x="320" y="105" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">15</text>
            </g>

            <!-- Measured Object above ruler -->
            <g id="brokenObjectGroup">
                <!-- Placed from mark 3 (x=80) to mark 11 (x=240) -> 8 cm -->
                <rect x="80" y="32" width="160" height="28" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
                <text x="160" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Blue Crayon</text>
                <!-- Guideline drops -->
                <line x1="80" y1="32" x2="80" y2="70" stroke="#0284c7" stroke-dasharray="2 2"/>
                <line x1="240" y1="32" x2="240" y2="70" stroke="#0284c7" stroke-dasharray="2 2"/>
            </g>

            <!-- Subtraction Formula Text -->
            <text id="brokenFormulaText" x="180" y="155" fill="#fbbf24" font-size="12" font-weight="extrabold" text-anchor="middle">Length = 11 cm - 3 cm = 8 cm</text>
        </svg>

        <div id="brokenRulerDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Never read only the end point! Subtract: <span class="text-orange-400 font-bold">11 cm - 3 cm = 8 cm</span>.
        </div>
    </div>
</div>
''',
    14: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Sticker Border Math</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Perimeter Ribbon / Border</span>
    </div>

    <!-- Dimension Controls -->
    <div class="flex items-center justify-center gap-2">
        <button onclick="setCardBorder(12, 8)" id="btn-card-1" class="card-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs shadow transition">12 cm × 8 cm Card</button>
        <button onclick="setCardBorder(15, 10)" id="btn-card-2" class="card-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">15 cm × 10 cm Photo</button>
        <button onclick="setCardBorder(20, 10)" id="btn-card-3" class="card-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">20 cm × 10 cm Chart</button>
    </div>

    <!-- Greeting Card SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="stickerBorderSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Card Body -->
            <rect id="cardRect" x="90" y="35" width="180" height="100" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
            <text x="180" y="85" fill="#c7d2fe" font-size="12" font-weight="bold" text-anchor="middle">Greeting Card</text>
            <text id="cardDimLabel" x="180" y="103" fill="#a5b4fc" font-size="10" text-anchor="middle">12 cm × 8 cm</text>

            <!-- Decorative Border Ribbon -->
            <rect id="cardBorderRibbon" x="87" y="32" width="186" height="106" rx="8" fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="8 6"/>

            <!-- Top Dimension -->
            <text id="cardTopLen" x="180" y="24" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">12 cm</text>
            <!-- Bottom Dimension -->
            <text id="cardBotLen" x="180" y="152" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">12 cm</text>
            <!-- Left Dimension -->
            <text id="cardLeftLen" x="72" y="90" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">8 cm</text>
            <!-- Right Dimension -->
            <text id="cardRightLen" x="290" y="90" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">8 cm</text>
        </svg>

        <div id="stickerBorderDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Total border tape: 12 + 8 + 12 + 8 = <span class="text-indigo-400 font-bold">40 cm of lace / ribbon needed</span>.
        </div>
    </div>
</div>
''',
    15: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Metre-Centimetre Converter</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Deep Well Rope Meter</span>
    </div>

    <!-- Depth Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setWellDepth(2, 45)" id="btn-depth-1" class="depth-btn px-2.5 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs transition shadow">2m 45cm</button>
        <button onclick="setWellDepth(4, 10)" id="btn-depth-2" class="depth-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">4m 10cm</button>
        <button onclick="setWellDepth(6, 80)" id="btn-depth-3" class="depth-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">6m 80cm</button>
        <button onclick="setWellDepth(8, 05)" id="btn-depth-4" class="depth-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">8m 5cm</button>
    </div>

    <!-- Well & Bucket Depth SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="wellDepthSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Well Shaft -->
            <rect x="50" y="25" width="100" height="135" fill="#0f172a" stroke="#475569" stroke-width="2"/>
            <!-- Water Level at bottom -->
            <rect x="52" y="130" width="96" height="28" fill="#0284c7" fill-opacity="0.5"/>

            <!-- Pulley at top -->
            <circle cx="100" cy="20" r="10" fill="#64748b"/>
            <!-- Rope lowering bucket -->
            <line id="wellRopeLine" x1="100" y1="20" x2="100" y2="85" stroke="#f59e0b" stroke-width="2.5"/>
            <!-- Bucket -->
            <polygon id="wellBucket" points="93,85 107,85 104,102 96,102" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>

            <!-- Dual Conversion Panel -->
            <rect x="180" y="30" width="160" height="110" rx="8" fill="#134e4a" fill-opacity="0.3" stroke="#14b8a6" stroke-width="1.5"/>
            <text x="260" y="55" fill="#5eead4" font-size="11" font-weight="bold" text-anchor="middle">Dual Unit Conversion</text>
            <text id="convMetrePart" x="260" y="80" fill="#f0fdfa" font-size="13" font-weight="extrabold" text-anchor="middle">2 m 45 cm</text>
            <text x="260" y="98" fill="#99f6e4" font-size="10" text-anchor="middle">equals</text>
            <text id="convCmPart" x="260" y="122" fill="#2dd4bf" font-size="15" font-weight="black" text-anchor="middle">245 cm</text>
        </svg>

        <div id="wellDepthDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Rule: Multiply metres by 100 and add centimetres: <span class="text-teal-400 font-bold">(2 × 100) + 45 = 245 cm</span>.
        </div>
    </div>
</div>
''',
    16: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fencing Garden Perimeter</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Fixed 20-Metre Wire Fence</span>
    </div>

    <!-- Garden Dimension Buttons (Fixed Perimeter = 20m) -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setGardenShape(6, 4)" id="btn-garden-1" class="garden-btn px-2.5 py-1.5 rounded-xl bg-green-500 text-slate-950 font-bold text-xs transition shadow">6m × 4m</button>
        <button onclick="setGardenShape(7, 3)" id="btn-garden-2" class="garden-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">7m × 3m</button>
        <button onclick="setGardenShape(8, 2)" id="btn-garden-3" class="garden-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">8m × 2m</button>
        <button onclick="setGardenShape(5, 5)" id="btn-garden-4" class="garden-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">5m × 5m (Square)</button>
    </div>

    <!-- Garden Visual SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="gardenFenceSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Vegetable Bed Fill -->
            <rect id="gardenBedRect" x="90" y="35" width="180" height="90" rx="6" fill="#14532d" fill-opacity="0.4" stroke="#22c55e" stroke-width="2.5"/>
            <!-- Plant icons inside bed -->
            <text x="180" y="85" fill="#86efac" font-size="12" font-weight="bold" text-anchor="middle">Vegetable Bed</text>

            <!-- Dimension labels -->
            <text id="gardenTopLabel" x="180" y="24" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">Length: 6 Metres</text>
            <text id="gardenSideLabel" x="55" y="85" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">Width: 4m</text>

            <!-- Perimeter Equation Summary -->
            <rect x="70" y="140" width="220" height="30" rx="6" fill="#052e16" stroke="#16a34a" stroke-width="1"/>
            <text id="gardenPerimeterText" x="180" y="160" fill="#bbf7d0" font-size="11" font-weight="bold" text-anchor="middle">Perimeter = 6 + 4 + 6 + 4 = 20 Metres</text>
        </svg>

        <div id="gardenFenceDesc" class="mt-2 text-center text-xs font-semibold text-slate-300">
            Every shape uses exactly <span class="text-green-400 font-bold">20 metres of fence wire</span>! Notice how area changes while perimeter stays fixed.
        </div>
    </div>
</div>
''',
}

# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Class 3 Mathematics Chapter 3: Double Century."""

simulators_part2 = {}

# 9. Flower Petal Puzzles
simulators_part2['sim_flower_petal_puzzles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-pink-400">Interactive Lab 9</span>
            <h3 class="text-lg font-bold text-slate-100">Complementary Petal Pairs</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-pink-500/20 text-pink-300 font-semibold border border-pink-500/30">Target Sum = 100</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        In the center of this flower sits <strong>100</strong>. Match two petals whose values add up to make exactly 100!
    </p>

    <!-- Flower Puzzle Canvas/SVG -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <div class="relative w-72 h-72 sm:w-80 sm:h-80 flex items-center justify-center">
            <!-- Center Circle -->
            <div class="absolute z-10 w-24 h-24 rounded-full bg-amber-500 border-4 border-amber-300 shadow-lg flex flex-col items-center justify-center text-slate-950">
                <span class="text-xs font-black uppercase tracking-wider">TARGET</span>
                <span class="text-3xl font-black font-mono">100</span>
            </div>

            <!-- Petal Elements around the circle -->
            <div id="flowerPetalsContainer" class="absolute inset-0">
                <!-- Rendered dynamically: 8 petals placed radially -->
            </div>
        </div>

        <!-- Match Status Feedback -->
        <div id="petalPairStatus" class="mt-2 text-xs font-semibold text-center text-slate-300 bg-slate-900 px-4 py-2 rounded-lg border border-slate-800 w-full max-w-sm">
            Click any first petal to start pairing!
        </div>
    </div>

    <!-- Controls -->
    <div class="flex justify-center gap-2">
        <button onclick="resetFlowerPuzzle()" class="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold">
            🔄 New Petal Puzzle
        </button>
    </div>
</div>
"""

# 10. Counting Beyond Hundred
simulators_part2['sim_counting_beyond_hundred'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Interactive Lab 10</span>
            <h3 class="text-lg font-bold text-slate-100">Stepping Past 100 (101 to 124)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/20 text-sky-300 font-semibold border border-sky-500/30">Consecutive Hundreds Sequence</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        After 100, the counting cycle restarts from one: 101, 102, 103... Step through consecutive numbers and observe the place value structure and number words.
    </p>

    <!-- Visual Stepper Display -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <!-- Number & Word Card -->
        <div class="text-center my-2">
            <div class="text-xs text-sky-400 font-bold uppercase tracking-wide">Current Number</div>
            <div id="seqNumberDisplay" class="text-5xl font-black font-mono text-white tracking-wider my-1">108</div>
            <div id="seqWordDisplay" class="text-sm font-semibold text-amber-300">"One Hundred Eight"</div>
        </div>

        <!-- Bundle Decomposition Visual -->
        <div class="grid grid-cols-3 gap-2 w-full max-w-md my-3 text-center text-xs">
            <div class="bg-indigo-950/60 p-2.5 rounded-lg border border-indigo-700/50">
                <span class="text-indigo-300 block font-bold">1 HUNDRED</span>
                <span class="text-lg font-mono font-black text-indigo-200">100</span>
                <span class="text-[10px] text-slate-400 block">1 big bundle</span>
            </div>
            <div class="bg-emerald-950/60 p-2.5 rounded-lg border border-emerald-700/50">
                <span class="text-emerald-300 block font-bold">TENS</span>
                <span id="seqTensVal" class="text-lg font-mono font-black text-emerald-200">0</span>
                <span id="seqTensTxt" class="text-[10px] text-slate-400 block">0 tens (0)</span>
            </div>
            <div class="bg-amber-950/60 p-2.5 rounded-lg border border-amber-700/50">
                <span class="text-amber-300 block font-bold">ONES</span>
                <span id="seqOnesVal" class="text-lg font-mono font-black text-amber-200">8</span>
                <span id="seqOnesTxt" class="text-[10px] text-slate-400 block">8 loose</span>
            </div>
        </div>

        <!-- Expansion Equation -->
        <div id="seqEquation" class="text-xs font-mono bg-slate-900 px-3 py-1.5 rounded border border-slate-800 text-slate-300">
            100 + 0 + 8 = 108
        </div>
    </div>

    <!-- Stepping Controls -->
    <div class="flex flex-wrap gap-2 justify-center">
        <button onclick="stepSeq(-1)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-bold text-slate-200">◀ Previous (-1)</button>
        <button onclick="stepSeq(1)" class="px-4 py-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white shadow">Next Number (+1) ▶</button>
        <button onclick="setSeqNum(101)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 rounded text-xs text-slate-300">101</button>
        <button onclick="setSeqNum(110)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 rounded text-xs text-slate-300">110</button>
        <button onclick="setSeqNum(119)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 rounded text-xs text-slate-300">119</button>
        <button onclick="setSeqNum(124)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 rounded text-xs text-slate-300">124</button>
    </div>
</div>
"""

# 11. Hundred Matchstick Bundles
simulators_part2['sim_matchstick_bundles_150'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 11</span>
            <h3 class="text-lg font-bold text-slate-100">Matchstick Bundles to 150</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Concrete Representation</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Build any number using three concrete units: a giant bundle of <strong>100</strong>, bundles of <strong>10</strong>, and <strong>loose</strong> matchsticks!
    </p>

    <!-- Bundle Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="flex justify-between items-center mb-3">
            <span class="text-xs text-slate-400 font-semibold">Active Matchstick Collection:</span>
            <span id="matchstickTotalBadge" class="text-base font-black font-mono text-amber-400">136 Matchsticks</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <!-- 100 Bundle Box -->
            <div class="bg-slate-900/90 border border-indigo-700/50 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold text-indigo-300">100-Bundle</span>
                <div id="matchHundredDisplay" class="h-16 flex items-center justify-center my-1">
                    <!-- SVG Hundred Bundle -->
                    <div class="w-14 h-14 rounded-lg bg-indigo-900/80 border-2 border-indigo-400 flex flex-col items-center justify-center shadow">
                        <span class="text-xs font-black text-indigo-200">100</span>
                        <span class="text-[9px] text-indigo-400">STICKS</span>
                    </div>
                </div>
                <div class="flex gap-1 mt-1">
                    <button onclick="adjustMatchUnit('h', 1)" class="w-7 h-7 bg-indigo-800 hover:bg-indigo-700 rounded text-xs font-bold">+</button>
                    <button onclick="adjustMatchUnit('h', -1)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 rounded text-xs font-bold">-</button>
                </div>
                <span id="matchCountH" class="text-xs font-mono text-indigo-300 mt-1">1 bundle = 100</span>
            </div>

            <!-- 10 Bundles Box -->
            <div class="bg-slate-900/90 border border-emerald-700/50 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold text-emerald-300">10-Bundles</span>
                <div id="matchTensDisplay" class="h-16 flex flex-wrap items-center justify-center gap-1.5 overflow-hidden my-1">
                    <!-- Dynamic small bundles -->
                </div>
                <div class="flex gap-1 mt-1">
                    <button onclick="adjustMatchUnit('t', 1)" class="w-7 h-7 bg-emerald-800 hover:bg-emerald-700 rounded text-xs font-bold">+</button>
                    <button onclick="adjustMatchUnit('t', -1)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 rounded text-xs font-bold">-</button>
                </div>
                <span id="matchCountT" class="text-xs font-mono text-emerald-300 mt-1">3 bundles = 30</span>
            </div>

            <!-- Loose Sticks Box -->
            <div class="bg-slate-900/90 border border-amber-700/50 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold text-amber-300">Loose Matchsticks</span>
                <div id="matchOnesDisplay" class="h-16 flex flex-wrap items-center justify-center gap-1 overflow-hidden my-1">
                    <!-- Dynamic single matchsticks -->
                </div>
                <div class="flex gap-1 mt-1">
                    <button onclick="adjustMatchUnit('o', 1)" class="w-7 h-7 bg-amber-800 hover:bg-amber-700 rounded text-xs font-bold">+</button>
                    <button onclick="adjustMatchUnit('o', -1)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 rounded text-xs font-bold">-</button>
                </div>
                <span id="matchCountO" class="text-xs font-mono text-amber-300 mt-1">6 singles = 6</span>
            </div>
        </div>

        <div id="matchSummaryEquation" class="mt-3 p-2 bg-slate-900 rounded-lg text-center text-xs font-mono text-amber-200 border border-slate-800">
            Total: 100 + 30 + 6 = 136 Matchsticks
        </div>
    </div>

    <!-- Quick Presets -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setMatchPreset(1, 1, 5)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">115</button>
        <button onclick="setMatchPreset(1, 2, 8)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">128</button>
        <button onclick="setMatchPreset(1, 4, 2)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">142</button>
        <button onclick="setMatchPreset(1, 5, 0)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-amber-400 font-mono font-bold">150</button>
    </div>
</div>
"""

# 12. Counting to One-Fifty
simulators_part2['sim_counting_to_150'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-green-400">Interactive Lab 12</span>
            <h3 class="text-lg font-bold text-slate-100">100-to-150 Range Explorer</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-green-500/20 text-green-300 font-semibold border border-green-500/30">The First Half-Century</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Explore numbers from 100 to 150 along an interactive continuum. Note key milestones like the exact midpoint <strong>125</strong> and decade markers!
    </p>

    <!-- Slider & Track -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <!-- Big Number Callout -->
        <div class="flex justify-between items-center mb-4">
            <div>
                <span class="text-xs text-slate-400 block">Position on Continuum:</span>
                <span id="range150Word" class="text-sm font-semibold text-green-300">"One Hundred Twenty-Five"</span>
            </div>
            <div id="range150Number" class="text-4xl font-black font-mono text-white">125</div>
        </div>

        <!-- Custom Track with Milestones -->
        <div class="relative py-4 select-none">
            <input type="range" id="sliderRange150" min="100" max="150" value="125" oninput="updateRange150(this.value)" class="w-full accent-green-400 cursor-pointer">
            <div class="flex justify-between text-[11px] font-mono text-slate-400 mt-2">
                <span>100</span>
                <span>110</span>
                <span>120</span>
                <span class="text-amber-400 font-bold">125 (Mid)</span>
                <span>130</span>
                <span>140</span>
                <span>150</span>
            </div>
        </div>

        <!-- Relationship Badges -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-3 text-xs text-center">
            <div class="bg-slate-900 p-2 rounded border border-slate-800">
                <span class="text-slate-400 block">Distance from 100:</span>
                <span id="rangeDist100" class="font-bold text-green-300 font-mono">+25</span>
            </div>
            <div class="bg-slate-900 p-2 rounded border border-slate-800">
                <span class="text-slate-400 block">Distance to 150:</span>
                <span id="rangeDist150" class="font-bold text-sky-300 font-mono">25 to go</span>
            </div>
            <div class="bg-slate-900 p-2 rounded border border-slate-800 col-span-2 sm:col-span-1">
                <span class="text-slate-400 block">Nearest Ten:</span>
                <span id="rangeNearestTen" class="font-bold text-amber-300 font-mono">130</span>
            </div>
        </div>
    </div>

    <!-- Milestone Quick Buttons -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setRange150Val(100)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">100</button>
        <button onclick="setRange150Val(115)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">115</button>
        <button onclick="setRange150Val(125)" class="px-2.5 py-1 bg-green-900 hover:bg-green-800 rounded text-green-200 font-mono font-bold">125 (Mid)</button>
        <button onclick="setRange150Val(138)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">138</button>
        <button onclick="setRange150Val(150)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">150</button>
    </div>
</div>
"""

# 13. Clap Snap Pat
simulators_part2['sim_clap_snap_pat'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-violet-400">Interactive Lab 13</span>
            <h3 class="text-lg font-bold text-slate-100">Clap, Snap & Pat Rhythm Game</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-violet-500/20 text-violet-300 font-semibold border border-violet-500/30">Multi-Sensory Place Value</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Turn numbers into rhythm! 👏 <strong>Clap = 100</strong>, 🫰 <strong>Snap = 10</strong>, 🦵 <strong>Pat Thigh = 1</strong>. Tap the action buttons to build sound codes!
    </p>

    <!-- Rhythm Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <!-- Rhythm History Sequence -->
        <div class="text-xs text-slate-400 mb-2">Current Rhythm Pattern:</div>
        <div id="rhythmSoundLog" class="min-h-[50px] bg-slate-900 rounded-lg p-2.5 border border-slate-800 flex flex-wrap items-center justify-center gap-1.5 text-lg">
            <!-- Dynamic gesture badges -->
        </div>

        <!-- Calculated Sound Total -->
        <div class="mt-3">
            <span class="text-xs text-slate-400 block">Total Number Encoded:</span>
            <span id="rhythmTotalNumber" class="text-4xl font-black font-mono text-violet-300">0</span>
            <div id="rhythmBreakdownTxt" class="text-xs text-slate-400 mt-1 font-mono">0 Claps + 0 Snaps + 0 Pats = 0</div>
        </div>
    </div>

    <!-- Action Buttons with Sound Triggers -->
    <div class="grid grid-cols-3 gap-2">
        <button onclick="triggerRhythm('clap')" class="py-3 px-2 bg-indigo-700 hover:bg-indigo-600 active:scale-95 text-white rounded-xl font-bold flex flex-col items-center gap-1 shadow transition">
            <span class="text-2xl">👏</span>
            <span class="text-xs">CLAP (+100)</span>
            <span class="text-[10px] text-indigo-200">Hundreds</span>
        </button>
        <button onclick="triggerRhythm('snap')" class="py-3 px-2 bg-emerald-700 hover:bg-emerald-600 active:scale-95 text-white rounded-xl font-bold flex flex-col items-center gap-1 shadow transition">
            <span class="text-2xl">🫰</span>
            <span class="text-xs">SNAP (+10)</span>
            <span class="text-[10px] text-emerald-200">Tens</span>
        </button>
        <button onclick="triggerRhythm('pat')" class="py-3 px-2 bg-amber-700 hover:bg-amber-600 active:scale-95 text-white rounded-xl font-bold flex flex-col items-center gap-1 shadow transition">
            <span class="text-2xl">🦵</span>
            <span class="text-xs">PAT (+1)</span>
            <span class="text-[10px] text-amber-200">Ones</span>
        </button>
    </div>

    <!-- Utility Controls -->
    <div class="flex justify-between items-center pt-1 text-xs">
        <button onclick="clearRhythm()" class="px-3 py-1.5 bg-rose-900/60 hover:bg-rose-800 text-rose-200 rounded-lg">Clear Rhythm</button>
        <div class="flex gap-1.5">
            <button onclick="playRhythmTarget(123)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300">Encode 123</button>
            <button onclick="playRhythmTarget(145)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300">Encode 145</button>
        </div>
    </div>
</div>
"""

# 14. Place Value Breakdowns
simulators_part2['sim_place_value_breakdowns'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Interactive Lab 14</span>
            <h3 class="text-lg font-bold text-slate-100">Expanded Form Chart (150 to 159)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">H-T-O Table & Expanded Form</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Examine how numbers in the fifties decade (150–159) keep hundreds and tens steady while ones increment step by step!
    </p>

    <!-- Interactive Table & Form -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <!-- Current Number Header -->
        <div class="flex justify-between items-center mb-3">
            <span class="text-xs text-slate-400">Target Number in 150s:</span>
            <span id="chartTargetNum" class="text-2xl font-black font-mono text-emerald-400">154</span>
        </div>

        <!-- 3-Column Place Value Breakdown -->
        <div class="grid grid-cols-3 gap-2 text-center mb-3">
            <div class="bg-indigo-950/50 p-2.5 rounded-lg border border-indigo-700/50">
                <span class="text-[10px] font-bold text-indigo-300 block">HUNDREDS</span>
                <span class="text-2xl font-black font-mono text-indigo-200">1</span>
                <span class="text-xs text-indigo-400 font-mono block">= 100</span>
            </div>
            <div class="bg-emerald-950/50 p-2.5 rounded-lg border border-emerald-700/50">
                <span class="text-[10px] font-bold text-emerald-300 block">TENS</span>
                <span class="text-2xl font-black font-mono text-emerald-200">5</span>
                <span class="text-xs text-emerald-400 font-mono block">= 50</span>
            </div>
            <div class="bg-amber-950/50 p-2.5 rounded-lg border border-amber-700/50">
                <span class="text-[10px] font-bold text-amber-300 block">ONES</span>
                <span id="chartOnesDigit" class="text-2xl font-black font-mono text-amber-200">4</span>
                <span id="chartOnesValue" class="text-xs text-amber-400 font-mono block">= 4</span>
            </div>
        </div>

        <!-- Expanded Equation -->
        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 text-center">
            <div id="chartExpandedForm" class="text-lg sm:text-xl font-bold font-mono text-emerald-300">
                100 + 50 + 4 = 154
            </div>
            <div id="chartWordName" class="text-xs font-semibold text-slate-300 mt-1">
                "One Hundred Fifty-Four"
            </div>
        </div>
    </div>

    <!-- Stepper Buttons for 150 to 159 -->
    <div class="flex flex-wrap gap-1.5 justify-center text-xs">
        <button onclick="setChart150(150)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">150</button>
        <button onclick="setChart150(151)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">151</button>
        <button onclick="setChart150(152)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">152</button>
        <button onclick="setChart150(153)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">153</button>
        <button onclick="setChart150(154)" class="px-2 py-1 bg-emerald-900 hover:bg-emerald-800 rounded text-emerald-300 font-mono font-bold">154</button>
        <button onclick="setChart150(155)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">155</button>
        <button onclick="setChart150(156)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">156</button>
        <button onclick="setChart150(157)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">157</button>
        <button onclick="setChart150(158)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">158</button>
        <button onclick="setChart150(159)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">159</button>
    </div>
</div>
"""

# 15. Number Line Jumps
simulators_part2['sim_number_line_jumps'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-blue-400">Interactive Lab 15</span>
            <h3 class="text-lg font-bold text-slate-100">Number Line Leaps (100 to 200)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-500/20 text-blue-300 font-semibold border border-blue-500/30">Jump Mechanics</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Jump across the second century in controlled strides of <strong>+5, +10, or +20</strong>! Watch how your position leaps forward toward the summit of 200.
    </p>

    <!-- Number Line SVG Canvas -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <div class="flex justify-between items-center w-full mb-3 text-xs">
            <span class="text-slate-400">Start: <strong class="text-blue-300">100</strong></span>
            <span class="text-slate-400">Current Spot: <strong id="jumpCurrentPos" class="text-blue-400 text-lg font-mono">140</strong></span>
            <span class="text-slate-400">Goal: <strong class="text-amber-400">200</strong></span>
        </div>

        <!-- SVG Track -->
        <div class="w-full overflow-x-auto py-2">
            <svg id="jumpLineSvg" viewBox="0 0 600 90" class="w-full min-w-[500px] h-24">
                <!-- Base track line -->
                <line x1="30" y1="50" x2="570" y2="50" stroke="#475569" stroke-width="3"/>
                <!-- Milestone ticks -->
                <line x1="30" y1="40" x2="30" y2="60" stroke="#38bdf8" stroke-width="3"/>
                <text x="30" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="monospace">100</text>

                <line x1="165" y1="45" x2="165" y2="55" stroke="#64748b" stroke-width="2"/>
                <text x="165" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="monospace">125</text>

                <line x1="300" y1="40" x2="300" y2="60" stroke="#38bdf8" stroke-width="3"/>
                <text x="300" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="monospace">150</text>

                <line x1="435" y1="45" x2="435" y2="55" stroke="#64748b" stroke-width="2"/>
                <text x="435" y="75" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="monospace">175</text>

                <line x1="570" y1="40" x2="570" y2="60" stroke="#f59e0b" stroke-width="3"/>
                <text x="570" y="75" text-anchor="middle" fill="#f59e0b" font-size="11" font-family="monospace">200</text>

                <!-- Jumper Token -->
                <circle id="jumperToken" cx="246" cy="50" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2" class="transition-all duration-300"/>
            </svg>
        </div>

        <div id="jumpActionLog" class="text-xs font-mono text-blue-200 mt-2 bg-slate-900 px-3 py-1 rounded border border-slate-800">
            Current jump status: 140 is 40 steps past 100, 60 steps to 200
        </div>
    </div>

    <!-- Leap Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="leapStep(5)" class="px-3 py-2 bg-sky-700 hover:bg-sky-600 rounded-lg text-xs font-bold text-white shadow">
            🐰 Hop +5
        </button>
        <button onclick="leapStep(10)" class="px-3 py-2 bg-blue-700 hover:bg-blue-600 rounded-lg text-xs font-bold text-white shadow">
            🦌 Leap +10
        </button>
        <button onclick="leapStep(20)" class="px-3 py-2 bg-indigo-700 hover:bg-indigo-600 rounded-lg text-xs font-bold text-white shadow">
            🦘 Giant Leap +20
        </button>
        <button onclick="resetJumper()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-bold text-slate-300">
            Reset (100)
        </button>
    </div>
</div>
"""

# 16. Double Century Goal
simulators_part2['sim_double_century_goal'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 16</span>
            <h3 class="text-lg font-bold text-slate-100">The Double Century Summit (200)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Grand Finale Milestone</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        You have arrived at the summit of <strong>200</strong>! Explore the three grand equivalences of a Double Century and celebrate this monumental achievement!
    </p>

    <!-- 200 Summit Display -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <!-- Trophy & Fireworks Milestone Header -->
        <div class="flex items-center justify-center gap-3 my-2">
            <span class="text-4xl">🏏</span>
            <div>
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block">DOUBLE CENTURY</span>
                <span class="text-5xl font-black font-mono text-white">200</span>
            </div>
            <span class="text-4xl">🏆</span>
        </div>

        <!-- 3 Equivalent Views -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs">
            <div class="bg-indigo-950/60 p-3 rounded-xl border border-indigo-700/50 flex flex-col items-center">
                <span class="text-indigo-300 font-bold">2 Master Bundles</span>
                <div class="flex gap-2 my-2">
                    <div class="w-10 h-10 rounded bg-indigo-800 border border-indigo-400 flex items-center justify-center text-xs font-black">100</div>
                    <div class="w-10 h-10 rounded bg-indigo-800 border border-indigo-400 flex items-center justify-center text-xs font-black">100</div>
                </div>
                <span class="text-slate-300 font-mono">100 + 100 = 200</span>
            </div>

            <div class="bg-emerald-950/60 p-3 rounded-xl border border-emerald-700/50 flex flex-col items-center">
                <span class="text-emerald-300 font-bold">20 Bundles of Ten</span>
                <div class="text-lg font-mono font-bold text-emerald-300 my-2">20 × 10</div>
                <span class="text-slate-300 font-mono">20 Tens = 200</span>
            </div>

            <div class="bg-amber-950/60 p-3 rounded-xl border border-amber-700/50 flex flex-col items-center">
                <span class="text-amber-300 font-bold">200 Loose Units</span>
                <div class="text-lg font-mono font-bold text-amber-300 my-2">200 × 1</div>
                <span class="text-slate-300 font-mono">200 Single Items</span>
            </div>
        </div>

        <!-- Celebration Sparkle Banner -->
        <div id="doubleCenturyCelebration" class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2.5 text-xs text-amber-300 font-semibold">
            🎉 "Sensational mastery! You have conquered the journey from 1 to 200 with complete place value understanding!"
        </div>
    </div>

    <!-- Interactive Celebration Trigger -->
    <div class="flex justify-center gap-2">
        <button onclick="triggerDoubleCenturyCheer()" class="px-5 py-2.5 bg-amber-600 hover:bg-amber-500 active:scale-95 text-slate-950 font-black rounded-xl text-xs shadow-lg transition flex items-center gap-2">
            <span>🎆 Launch Double Century Celebration</span>
        </button>
    </div>
</div>
"""

print(f"Successfully created {len(simulators_part2)} simulators for Part 2")


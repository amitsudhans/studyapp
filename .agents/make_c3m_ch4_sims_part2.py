# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Class 3 Mathematics Chapter 4: Vacation with My Nani Maa."""

simulators_part2 = {}

# 9. Decade Hop Jumps
simulators_part2['sim_decade_hop_jumps'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-green-400">Interactive Lab 9</span>
            <h3 class="text-lg font-bold text-slate-100">Leaping Garden Creature Hops (+10 / -10)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-green-500/20 text-green-300 font-semibold border border-green-500/30">Decade Leaps</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Frogs leap forward by <strong>+10</strong> and grasshoppers hop backward by <strong>-10</strong>! Watch how the ones digit stays steady while tens shift smoothly.
    </p>

    <!-- Leaping Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <div class="flex justify-between items-center mb-3 text-xs">
            <span class="text-slate-400">Current Creature Position:</span>
            <span id="creaturePosBadge" class="text-3xl font-black font-mono text-green-400">34</span>
            <span class="text-slate-400 font-mono">Ones digit: <strong id="creatureOnesFix" class="text-amber-300">4</strong> (Steady)</span>
        </div>

        <!-- Visual Jumping Trail -->
        <div id="creatureJumpTrail" class="min-h-[60px] bg-slate-900 rounded-lg p-2.5 border border-slate-800 flex items-center justify-center gap-2 font-mono text-sm">
            <!-- Dynamic hop trail -->
        </div>

        <div id="creatureActionStatus" class="mt-2 text-xs font-semibold text-slate-300">
            Click Leap Forward (+10) or Hop Backward (-10)!
        </div>
    </div>

    <!-- Action Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="creatureHop(10)" class="px-3 py-2 bg-green-700 hover:bg-green-600 text-white rounded-lg text-xs font-bold shadow flex items-center justify-center gap-1">
            <span>🐸 Frog Leap (+10)</span>
        </button>
        <button onclick="creatureHop(-10)" class="px-3 py-2 bg-emerald-800 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold shadow flex items-center justify-center gap-1">
            <span>🦗 Grasshopper (-10)</span>
        </button>
        <button onclick="setCreatureStart(24)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-mono">
            Start at 24
        </button>
        <button onclick="setCreatureStart(78)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-mono">
            Start at 78
        </button>
    </div>
</div>
"""

# 10. Hidden Leaf Puzzles
simulators_part2['sim_hidden_leaf_puzzles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-lime-400">Interactive Lab 10</span>
            <h3 class="text-lg font-bold text-slate-100">Ant Colony Under the Leaf</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-lime-500/20 text-lime-300 font-semibold border border-lime-500/30">Total 50 - Visible 35 = 15</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        A total foraging team of <strong>50 ants</strong> is active. You observe 35 marching outside. How many are hidden under the broad mango leaf?
    </p>

    <!-- Garden Leaf Scene -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <!-- Open Marching Ants Area -->
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-slate-300 uppercase block mb-1">Visible Marching Ants</span>
                <span id="antVisibleBadge" class="text-2xl font-black font-mono text-lime-400">35 Ants</span>
                <div class="text-[11px] text-slate-400 mt-1">Marching in disciplined order along path</div>
            </div>

            <!-- Broad Mango Leaf -->
            <div class="bg-emerald-950/40 p-3 rounded-xl border border-emerald-600/40 text-center relative overflow-hidden flex flex-col items-center">
                <div class="flex justify-between items-center w-full mb-1">
                    <span class="text-xs font-bold text-emerald-300 uppercase">Under Broad Leaf</span>
                    <button onclick="toggleLeaf()" id="leafToggleBtn" class="text-[10px] px-2 py-0.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white font-bold">Lift Leaf</button>
                </div>
                <!-- Leaf graphic / container -->
                <div id="leafCoverGraphic" class="w-full h-16 bg-gradient-to-r from-emerald-800 to-green-900 rounded-xl flex items-center justify-center border-2 border-emerald-400/50 shadow-md">
                    <span class="text-2xl">🍃</span>
                    <span id="leafStatusTxt" class="text-xs font-bold text-emerald-200 ml-1">Leaf Sheltering Colony</span>
                </div>
                <div id="hiddenAntsRevealed" class="hidden mt-2 text-xs font-mono font-bold text-amber-300">
                    🐜 15 Ants Revealed Resting Here!
                </div>
                <span id="leafCountTxt" class="text-xs font-mono text-emerald-300 font-bold mt-2">Hidden: 15 Ants (50 - 35 = 15)</span>
            </div>
        </div>

        <div class="mt-3 p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-center text-xs font-mono text-lime-200">
            Estimation Check: 35 is more than half of 50, so hidden ants must be less than 25 (Exact: 15).
        </div>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setAntPreset(50, 35)" class="px-3 py-1.5 bg-lime-700 text-white rounded font-mono font-bold">50 Total (35 Vis ➜ 15 Hidden)</button>
        <button onclick="setAntPreset(40, 24)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">40 Total (24 Vis ➜ 16 Hidden)</button>
        <button onclick="setAntPreset(60, 42)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">60 Total (42 Vis ➜ 18 Hidden)</button>
    </div>
</div>
"""

# 11. Hundred Grid Navigation
simulators_part2['sim_hundred_grid_navigation'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Interactive Lab 11</span>
            <h3 class="text-lg font-bold text-slate-100">100-Grid Arrow Navigator</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/20 text-sky-300 font-semibold border border-sky-500/30">Spatial Operations</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Navigate the 1-100 chart! ⬇️ Down adds 10, ⬆️ Up subtracts 10, ➡️ Right adds 1, ⬅️ Left subtracts 1. Tap arrows to journey!
    </p>

    <!-- 100 Grid Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="flex justify-between items-center w-full mb-2 text-xs">
            <span class="text-slate-400">Current Position: <strong id="navGridPos" class="text-sky-400 text-sm font-mono font-bold">45</strong></span>
            <span id="navArrowHistory" class="text-amber-300 font-mono">Path: Start 45</span>
        </div>

        <!-- 10x10 Mini Grid -->
        <div id="navMiniGrid" class="grid grid-cols-10 gap-1 w-full max-w-sm aspect-square bg-slate-900 p-2 rounded-lg border border-slate-800 select-none">
            <!-- 100 cells dynamically generated -->
        </div>

        <!-- Directional D-Pad Controls -->
        <div class="flex flex-col items-center gap-1.5 mt-3">
            <button onclick="navGridStep('up')" class="w-12 h-9 rounded-lg bg-sky-800 hover:bg-sky-700 font-bold text-white text-xs shadow flex items-center justify-center">⬆️ -10</button>
            <div class="flex gap-2">
                <button onclick="navGridStep('left')" class="w-12 h-9 rounded-lg bg-sky-800 hover:bg-sky-700 font-bold text-white text-xs shadow flex items-center justify-center">⬅️ -1</button>
                <button onclick="navGridReset()" class="px-2 h-9 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px]">Reset</button>
                <button onclick="navGridStep('right')" class="w-12 h-9 rounded-lg bg-sky-800 hover:bg-sky-700 font-bold text-white text-xs shadow flex items-center justify-center">➡️ +1</button>
            </div>
            <button onclick="navGridStep('down')" class="w-12 h-9 rounded-lg bg-sky-800 hover:bg-sky-700 font-bold text-white text-xs shadow flex items-center justify-center">⬇️ +10</button>
        </div>
    </div>
</div>
"""

# 12. Grid Race Game
simulators_part2['sim_grid_race_game'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-yellow-400">Interactive Lab 12</span>
            <h3 class="text-lg font-bold text-slate-100">1-to-100 Grid Race Arena</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-yellow-500/20 text-yellow-300 font-semibold border border-yellow-500/30">Target: 91-100</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Roll two dice, combine digits into a 2-digit number (e.g. 3 & 5 ➜ 35 or 53), then choose to Add or Subtract to race toward the 91-100 goal!
    </p>

    <!-- Race Arena Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <!-- Status Bar -->
        <div class="flex justify-between items-center mb-3 text-xs">
            <span class="text-slate-400">Current Cell: <strong id="racePlayerPos" class="text-yellow-400 font-mono text-base">42</strong></span>
            <span id="raceStatusBadge" class="text-emerald-400 font-bold font-mono">Racing Forward!</span>
        </div>

        <!-- Dice Roll Outcome Box -->
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl max-w-sm mx-auto mb-3">
            <div class="flex items-center justify-center gap-3">
                <div id="diceA" class="w-10 h-10 rounded-lg bg-amber-600 text-white font-black text-xl flex items-center justify-center shadow">3</div>
                <div id="diceB" class="w-10 h-10 rounded-lg bg-amber-600 text-white font-black text-xl flex items-center justify-center shadow">5</div>
            </div>
            <div class="text-xs text-slate-300 mt-2">
                Available Moves: <span id="raceMoveChoicesTxt" class="font-mono text-yellow-300 font-bold">35 or 53</span>
            </div>
        </div>

        <!-- Action Choice Buttons -->
        <div class="flex flex-wrap gap-2 justify-center text-xs">
            <button onclick="applyRaceMove('add', false)" id="btnRaceAddLow" class="px-3 py-1.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white font-bold">Add 35 (+35)</button>
            <button onclick="applyRaceMove('add', true)" id="btnRaceAddHigh" class="px-3 py-1.5 rounded bg-emerald-800 hover:bg-emerald-700 text-white font-bold">Add 53 (+53)</button>
            <button onclick="applyRaceMove('sub', false)" id="btnRaceSubLow" class="px-3 py-1.5 rounded bg-rose-800 hover:bg-rose-700 text-white font-bold">Sub 35 (-35)</button>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex justify-between items-center pt-1 text-xs">
        <button onclick="rollRaceDice()" class="px-4 py-2 bg-yellow-600 hover:bg-yellow-500 text-slate-950 font-bold rounded-lg shadow">
            🎲 Roll Dice
        </button>
        <button onclick="resetRaceGame()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg">
            Reset to Cell 1
        </button>
    </div>
</div>
"""

# 13. Magic Square Matrix
simulators_part2['sim_magic_square_matrix'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Interactive Lab 13</span>
            <h3 class="text-lg font-bold text-slate-100">Classic 3×3 Magic Square (Sum = 15)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30">Constant Sum 15</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        In this 3×3 grid using digits 1 through 9, every horizontal row, vertical column, and diagonal adds up to <strong>15</strong>!
    </p>

    <!-- Magic Square Grid -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <div class="grid grid-cols-3 gap-2 w-48 sm:w-56 aspect-square p-2 bg-slate-900 rounded-xl border border-slate-800 shadow-inner">
            <!-- Row 1 -->
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">8</div>
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">1</div>
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">6</div>
            <!-- Row 2 -->
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">3</div>
            <div class="bg-amber-600 border-2 border-amber-300 rounded-lg flex items-center justify-center text-2xl font-mono font-black text-slate-950 shadow">5</div>
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">7</div>
            <!-- Row 3 -->
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">4</div>
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">9</div>
            <div class="bg-purple-950/60 border border-purple-500/50 rounded-lg flex items-center justify-center text-xl font-mono font-bold text-purple-200">2</div>
        </div>

        <!-- Verification Line Chooser -->
        <div class="mt-3 p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center text-xs font-mono text-purple-300 w-full max-w-sm">
            <span id="magicSumEquation">Top Row: 8 + 1 + 6 = 15</span>
        </div>
    </div>

    <!-- Line Checking Buttons -->
    <div class="flex flex-wrap gap-1.5 justify-center text-xs">
        <button onclick="checkMagicLine('r1')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Row 1 (8+1+6)</button>
        <button onclick="checkMagicLine('r2')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Row 2 (3+5+7)</button>
        <button onclick="checkMagicLine('r3')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Row 3 (4+9+2)</button>
        <button onclick="checkMagicLine('c1')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Col 1 (8+3+4)</button>
        <button onclick="checkMagicLine('diag')" class="px-2.5 py-1 bg-purple-800 hover:bg-purple-700 text-white rounded font-mono font-bold">Diag (8+5+2)</button>
    </div>
</div>
"""

# 14. Radish Harvest Bundles
simulators_part2['sim_radish_harvest_bundles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Interactive Lab 14</span>
            <h3 class="text-lg font-bold text-slate-100">Radish Harvest (25 + 36 = 61)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-semibold border border-rose-500/30">Regrouping 10 Ones into 1 Ten</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Combine 25 red radishes and 36 white radishes. 5 ones + 6 ones = 11 ones, which regroups into <strong>1 new ten</strong> and 1 loose radish!
    </p>

    <!-- Harvest Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- 25 Red Radishes -->
            <div class="bg-slate-900 p-3 rounded-xl border border-rose-700/50 flex flex-col items-center">
                <span class="text-xs font-bold text-rose-300 mb-1">Red Radishes: 25</span>
                <span class="text-xs text-slate-400 font-mono">2 bundles of 10 + 5 loose</span>
                <div class="flex gap-2 my-2 items-center">
                    <div class="w-7 h-10 bg-rose-900 border border-rose-400 rounded flex items-center justify-center text-[10px] text-rose-200 font-bold">10</div>
                    <div class="w-7 h-10 bg-rose-900 border border-rose-400 rounded flex items-center justify-center text-[10px] text-rose-200 font-bold">10</div>
                    <span class="text-xs text-slate-400">+ 5 singles</span>
                </div>
            </div>

            <!-- 36 White Radishes -->
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-600/50 flex flex-col items-center">
                <span class="text-xs font-bold text-slate-200 mb-1">White Radishes: 36</span>
                <span class="text-xs text-slate-400 font-mono">3 bundles of 10 + 6 loose</span>
                <div class="flex gap-2 my-2 items-center">
                    <div class="w-7 h-10 bg-slate-800 border border-slate-400 rounded flex items-center justify-center text-[10px] text-slate-200 font-bold">10</div>
                    <div class="w-7 h-10 bg-slate-800 border border-slate-400 rounded flex items-center justify-center text-[10px] text-slate-200 font-bold">10</div>
                    <div class="w-7 h-10 bg-slate-800 border border-slate-400 rounded flex items-center justify-center text-[10px] text-slate-200 font-bold">10</div>
                    <span class="text-xs text-slate-400">+ 6 singles</span>
                </div>
            </div>
        </div>

        <!-- Combined Total with Regrouping -->
        <div class="mt-3 p-3 bg-slate-900 rounded-lg border border-slate-800 text-center font-mono">
            <div class="text-xs text-slate-400">Step 1: Tens = 20 + 30 = 50. Step 2: Ones = 5 + 6 = 11 (10 + 1).</div>
            <div class="text-xl font-black text-rose-300 mt-1">Total: 50 + 11 = 61 Radishes</div>
            <div class="text-xs text-emerald-400 mt-1">Result: 6 bundles of 10 + 1 single radish = 61!</div>
        </div>
    </div>
</div>
"""

# 15. Vegetable Crate Complements
simulators_part2['sim_vegetable_crate_complements'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Interactive Lab 15</span>
            <h3 class="text-lg font-bold text-slate-100">100-Capacity Storage Crate (65 + ? = 100)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-orange-500/20 text-orange-300 font-semibold border border-orange-500/30">Target 100 Complement</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        A vegetable crate holds 100 items. Adjust the tomato count to see how many carrots are needed to fill the crate completely to 100!
    </p>

    <!-- Crate Visual -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <!-- 10x10 Grid representation -->
        <div class="flex justify-between items-center mb-2 text-xs">
            <span class="text-rose-400 font-bold">🍅 Tomatoes: <span id="crateTomatoesVal">65</span></span>
            <span class="text-orange-400 font-bold">🥕 Carrots: <span id="crateCarrotsVal">35</span></span>
            <span class="text-amber-300 font-mono font-bold">Total: 100</span>
        </div>

        <!-- 10-bar multi visual -->
        <div class="w-full h-8 bg-slate-900 rounded-lg border border-slate-800 flex overflow-hidden my-2">
            <div id="crateTomatoesBar" style="width: 65%;" class="bg-rose-600 flex items-center justify-center text-xs font-bold font-mono text-white transition-all duration-300">
                65 Tomatoes
            </div>
            <div id="crateCarrotsBar" style="width: 35%;" class="bg-orange-500 flex items-center justify-center text-xs font-bold font-mono text-slate-950 transition-all duration-300">
                35 Carrots
            </div>
        </div>

        <div id="crateComplementEquation" class="p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-xs font-mono text-amber-200 mt-2">
            Complement: 100 - 65 = <strong>35 Carrots</strong> (65 + 35 = 100)
        </div>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setCrateTomatoes(65)" class="px-3 py-1.5 bg-orange-700 text-white rounded font-mono font-bold">65 Tomatoes ➜ 35 Carrots</button>
        <button onclick="setCrateTomatoes(40)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">40 Tomatoes ➜ 60 Carrots</button>
        <button onclick="setCrateTomatoes(75)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">75 Tomatoes ➜ 25 Carrots</button>
        <button onclick="setCrateTomatoes(82)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">82 Tomatoes ➜ 18 Carrots</button>
    </div>
</div>
"""

# 16. Apple Harvest Comparison
simulators_part2['sim_apple_harvest_comparison'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-red-400">Interactive Lab 16</span>
            <h3 class="text-lg font-bold text-slate-100">Apple Harvest Comparison (85 vs 67)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-red-500/20 text-red-300 font-semibold border border-red-500/30">Total 152 | Difference 18</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Basket A holds <strong>85 apples</strong> and Basket B holds <strong>67 apples</strong>. Explore the combined total sum and the exact comparative difference margin!
    </p>

    <!-- Comparison Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <div class="grid grid-cols-2 gap-3 max-w-sm mx-auto mb-3">
            <div class="bg-red-950/50 border border-red-600/50 p-3 rounded-xl flex flex-col items-center">
                <span class="text-xs font-bold text-red-300">Basket A</span>
                <span class="text-3xl font-black font-mono text-white my-1">85</span>
                <span class="text-[10px] text-slate-400">Apples</span>
            </div>
            <div class="bg-amber-950/50 border border-amber-600/50 p-3 rounded-xl flex flex-col items-center">
                <span class="text-xs font-bold text-amber-300">Basket B</span>
                <span class="text-3xl font-black font-mono text-white my-1">67</span>
                <span class="text-[10px] text-slate-400">Apples</span>
            </div>
        </div>

        <!-- Comparative Output Box -->
        <div id="appleComparisonDisplay" class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs font-mono space-y-1">
            <div class="text-emerald-400 font-bold text-sm">Combined Total: 85 + 67 = 152 Apples</div>
            <div class="text-amber-300 font-bold">Difference Margin: 85 - 67 = 18 More Apples in Basket A!</div>
        </div>
    </div>

    <!-- Toggle Buttons -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setAppleMode('total')" class="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white rounded font-bold">View Addition Total (152)</button>
        <button onclick="setAppleMode('diff')" class="px-3 py-1.5 bg-amber-700 hover:bg-amber-600 text-white rounded font-bold">View Difference (18)</button>
    </div>
</div>
"""

print(f"Successfully generated {len(simulators_part2)} simulators for Part 2")


# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Class 3 Mathematics Chapter 4: Vacation with My Nani Maa."""

simulators_part1 = {}

# 1. Hidden Marble Trick
simulators_part1['sim_hidden_marble_trick'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 1</span>
            <h3 class="text-lg font-bold text-slate-100">Handkerchief Marble Hide-and-Seek</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Total - Visible = Hidden</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Observe the wooden tabletop. A total of <strong id="marbleTotalDisp">15</strong> marbles were placed here. Some marbles are hidden beneath the cloth, while others remain visible in the open!
    </p>

    <!-- Tabletop Stage -->
    <div class="bg-amber-950/20 border border-amber-800/40 rounded-xl p-4 min-h-[170px] relative overflow-hidden flex flex-col justify-between">
        <div class="flex justify-between items-center text-xs text-amber-300 mb-2 border-b border-amber-800/30 pb-1">
            <span>Wooden Tabletop Stage</span>
            <span class="font-mono font-bold" id="marbleVisibleCountBadge">Visible: 9 | Hidden: 6</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <!-- Open Visible Marbles Area -->
            <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
                <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wide mb-2">Visible Marbles</span>
                <div id="visibleMarblesContainer" class="flex flex-wrap gap-2 justify-center min-h-[48px] py-1">
                    <!-- Dynamic marble spheres -->
                </div>
                <span id="visibleMarblesCountTxt" class="text-xs font-mono text-emerald-400 font-bold mt-1">9 Visible</span>
            </div>

            <!-- Cloth / Handkerchief Covered Area -->
            <div class="bg-rose-950/40 border border-rose-700/50 rounded-xl p-3 flex flex-col items-center relative">
                <div class="flex justify-between items-center w-full mb-1">
                    <span class="text-[11px] font-bold text-rose-300 uppercase tracking-wide">Under Handkerchief</span>
                    <button onclick="toggleCloth()" id="clothToggleBtn" class="text-[10px] px-2 py-0.5 rounded bg-rose-800 hover:bg-rose-700 text-white font-semibold">Peeking: Off</button>
                </div>
                <div id="clothCover" class="w-full h-14 bg-gradient-to-r from-rose-700 to-pink-800 rounded-lg flex items-center justify-center border-2 border-rose-400/60 shadow-inner transition-all duration-300">
                    <span id="clothCoverLabel" class="text-xs font-bold text-white tracking-wider">❓ Hidden Under Cloth</span>
                </div>
                <div id="hiddenMarblesContainer" class="hidden flex flex-wrap gap-2 justify-center min-h-[48px] py-1 mt-1">
                    <!-- Revealed marbles when peeked -->
                </div>
                <span id="hiddenMarblesCountTxt" class="text-xs font-mono text-amber-300 font-bold mt-1">6 Hidden (15 - 9 = 6)</span>
            </div>
        </div>

        <div id="marbleEquationSummary" class="mt-3 p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center text-xs font-mono text-amber-200">
            Total 15 - Visible 9 = <strong>6 Hidden Marbles</strong> (Verified by 9 + 6 = 15)
        </div>
    </div>

    <!-- Preset Selection Controls -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <span class="text-slate-400 self-center">Try Total:</span>
        <button onclick="setMarblePreset(15, 9)" class="px-2.5 py-1.5 bg-amber-600 text-white rounded font-bold font-mono">15 (9 vis)</button>
        <button onclick="setMarblePreset(17, 11)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">17 (11 vis)</button>
        <button onclick="setMarblePreset(20, 13)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">20 (13 vis)</button>
        <button onclick="setMarblePreset(23, 15)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">23 (15 vis)</button>
        <button onclick="setMarblePreset(27, 18)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">27 (18 vis)</button>
    </div>
</div>
"""

# 2. Balushahi Sweet Counts
simulators_part1['sim_balushahi_sweet_counts'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Interactive Lab 2</span>
            <h3 class="text-lg font-bold text-slate-100">Balushahi Serving Platter</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-orange-500/20 text-orange-300 font-semibold border border-orange-500/30">Addition & Consumption</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Combine fresh balushahi sweets from two boxes ($7 + 5 = 12$), then simulate afternoon teatime by eating some to see the remaining quantity!
    </p>

    <!-- Platter Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <div class="flex justify-between items-center mb-3">
            <span class="text-xs text-slate-400 font-semibold">Active Serving Platter</span>
            <span id="balushahiCountBadge" class="text-base font-black font-mono text-amber-400">12 Sweets on Platter</span>
        </div>

        <!-- Sweet Platter Display -->
        <div id="balushahiPlatter" class="min-h-[100px] bg-amber-950/30 border-2 border-amber-600/40 rounded-2xl p-3 flex flex-wrap gap-2.5 items-center justify-center">
            <!-- Dynamic sweet icons -->
        </div>

        <!-- Operation Readout -->
        <div class="mt-3 p-3 bg-slate-900 rounded-lg border border-slate-800">
            <div id="balushahiEquation" class="text-xl font-black font-mono text-amber-300">
                Box A (7) + Box B (5) = 12 Sweets
            </div>
            <div id="balushahiStatusTxt" class="text-xs text-slate-400 mt-1">
                Click "Eat 1 Sweet" to observe subtraction in action!
            </div>
        </div>
    </div>

    <!-- Interactive Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="addSweet()" class="px-3 py-2 bg-emerald-700 hover:bg-emerald-600 rounded-lg text-xs font-bold text-white shadow">
            ➕ Add 1 Sweet
        </button>
        <button onclick="eatSweet()" class="px-3 py-2 bg-amber-700 hover:bg-amber-600 rounded-lg text-xs font-bold text-white shadow">
            🍪 Eat 1 Sweet
        </button>
        <button onclick="eatMultipleSweets(4)" class="px-3 py-2 bg-rose-800 hover:bg-rose-700 rounded-lg text-xs font-bold text-white shadow">
            Teatime (-4 Sweets)
        </button>
        <button onclick="resetSweets()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300">
            Reset (7 + 5 = 12)
        </button>
    </div>
</div>
"""

# 3. Story Books Total
simulators_part1['sim_story_books_total'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Interactive Lab 3</span>
            <h3 class="text-lg font-bold text-slate-100">Ten-Frame Book Bridging</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-500/20 text-indigo-300 font-semibold border border-indigo-500/30">9 + 7 = 10 + 6 = 16</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Combine <strong>9 storybooks</strong> and <strong>7 puzzle books</strong> using two ten-frames. Click the button to move 1 book into the ten-frame to make a friendly ten!
    </p>

    <!-- Ten-Frames Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Ten-Frame 1 (Storybooks) -->
            <div class="bg-slate-900 p-3 rounded-xl border border-indigo-700/50 flex flex-col items-center">
                <div class="flex justify-between items-center w-full mb-2">
                    <span class="text-xs font-bold text-indigo-300">Ten-Frame 1: Storybooks</span>
                    <span id="frame1CountBadge" class="text-xs font-mono font-bold text-indigo-400">9 Books</span>
                </div>
                <!-- 2x5 Grid -->
                <div id="tenFrame1" class="grid grid-cols-5 gap-1.5 p-2 bg-slate-950 rounded-lg border border-slate-800 w-full max-w-xs">
                    <!-- 10 cells generated dynamically -->
                </div>
            </div>

            <!-- Ten-Frame 2 (Puzzle Books) -->
            <div class="bg-slate-900 p-3 rounded-xl border border-emerald-700/50 flex flex-col items-center">
                <div class="flex justify-between items-center w-full mb-2">
                    <span class="text-xs font-bold text-emerald-300">Ten-Frame 2: Puzzle Books</span>
                    <span id="frame2CountBadge" class="text-xs font-mono font-bold text-emerald-400">7 Books</span>
                </div>
                <!-- 2x5 Grid -->
                <div id="tenFrame2" class="grid grid-cols-5 gap-1.5 p-2 bg-slate-950 rounded-lg border border-slate-800 w-full max-w-xs">
                    <!-- 10 cells generated dynamically -->
                </div>
            </div>
        </div>

        <!-- Strategy Outcome Equation -->
        <div class="mt-4 p-3 bg-slate-900 rounded-lg border border-slate-800 text-center">
            <div id="bookTenFrameEquation" class="text-xl sm:text-2xl font-black font-mono text-indigo-300">
                9 + 7 = 16 Books
            </div>
            <div id="bookTenFrameStepTxt" class="text-xs text-slate-300 mt-1">
                Initial state: 9 storybooks need 1 more to complete a full decade.
            </div>
        </div>
    </div>

    <!-- Bridging Controls -->
    <div class="flex flex-wrap gap-2 justify-center">
        <button onclick="executeMakeTen()" id="btnMakeTen" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-bold shadow transition">
            ✨ Move 1 Book to Make 10
        </button>
        <button onclick="resetTenFrames()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold">
            Reset (9 + 7)
        </button>
        <button onclick="setBookCustom(8, 5)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-mono">
            Try 8 + 5
        </button>
    </div>
</div>
"""

# 4. Card Equation Triplets
simulators_part1['sim_card_equation_triplets'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-pink-400">Interactive Lab 4</span>
            <h3 class="text-lg font-bold text-slate-100">Fact Family Triplet Cards</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-pink-500/20 text-pink-300 font-semibold border border-pink-500/30">4 Equations in 1 Triplet</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Three number cards form an inseparable fact family. Explore the four related addition and subtraction equations unlocked by these numbers!
    </p>

    <!-- Triplet Cards Display -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <!-- 3 Cards Visual -->
        <div class="flex items-center justify-center gap-3 sm:gap-6 my-2">
            <div class="w-16 h-24 sm:w-20 sm:h-28 rounded-xl bg-pink-950/60 border-2 border-pink-500 flex flex-col items-center justify-center shadow-lg">
                <span class="text-[10px] text-pink-300 font-bold">PART</span>
                <span id="tripletCardA" class="text-3xl sm:text-4xl font-black font-mono text-white">7</span>
            </div>
            <span class="text-2xl font-bold text-slate-500">+</span>
            <div class="w-16 h-24 sm:w-20 sm:h-28 rounded-xl bg-purple-950/60 border-2 border-purple-500 flex flex-col items-center justify-center shadow-lg">
                <span class="text-[10px] text-purple-300 font-bold">PART</span>
                <span id="tripletCardB" class="text-3xl sm:text-4xl font-black font-mono text-white">8</span>
            </div>
            <span class="text-2xl font-bold text-slate-500">=</span>
            <div class="w-16 h-24 sm:w-20 sm:h-28 rounded-xl bg-amber-950/60 border-2 border-amber-500 flex flex-col items-center justify-center shadow-lg">
                <span class="text-[10px] text-amber-300 font-bold">TOTAL</span>
                <span id="tripletCardTotal" class="text-3xl sm:text-4xl font-black font-mono text-amber-300">15</span>
            </div>
        </div>

        <!-- 4 Equations Matrix -->
        <div class="grid grid-cols-2 gap-2 w-full max-w-md mt-3 text-xs font-mono">
            <div id="eqBox1" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-center font-bold text-emerald-300">
                7 + 8 = 15
            </div>
            <div id="eqBox2" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-center font-bold text-emerald-300">
                8 + 7 = 15
            </div>
            <div id="eqBox3" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-center font-bold text-amber-300">
                15 - 7 = 8
            </div>
            <div id="eqBox4" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-center font-bold text-amber-300">
                15 - 8 = 7
            </div>
        </div>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setTripletPreset(7, 8, 15)" class="px-3 py-1.5 bg-pink-700 text-white rounded font-mono font-bold">Triplet {7, 8, 15}</button>
        <button onclick="setTripletPreset(6, 8, 14)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Triplet {6, 8, 14}</button>
        <button onclick="setTripletPreset(9, 7, 16)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Triplet {9, 7, 16}</button>
        <button onclick="setTripletPreset(5, 9, 14)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Triplet {5, 9, 14}</button>
    </div>
</div>
"""

# 5. Bead String Strategies
simulators_part1['sim_bead_string_strategies'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Interactive Lab 5</span>
            <h3 class="text-lg font-bold text-slate-100">Ginladi Bead String Addition</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-teal-500/20 text-teal-300 font-semibold border border-teal-500/30">Three Paths to 15 + 7</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Solve <strong>15 + 7 = 22</strong> along a 100-bead string using three distinct mental pathways: single units, friendly bridging, or compensation leap!
    </p>

    <!-- Strategy Selector Tabs -->
    <div class="grid grid-cols-3 gap-1.5 border-b border-slate-800 pb-2 text-xs">
        <button onclick="setBeadStrategy('bridge')" id="tabStratBridge" class="px-2 py-1.5 rounded-lg font-bold bg-teal-600 text-white">🌉 Friendly Bridge (+5, +2)</button>
        <button onclick="setBeadStrategy('comp')" id="tabStratComp" class="px-2 py-1.5 rounded-lg font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">⚡ Compensation (+10, -3)</button>
        <button onclick="setBeadStrategy('ones')" id="tabStratOnes" class="px-2 py-1.5 rounded-lg font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">🐢 Step by Ones (+1 × 7)</button>
    </div>

    <!-- Ginladi Display -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <!-- Bead Track -->
        <div id="ginladiStrategyTrack" class="flex flex-wrap gap-1 justify-center max-w-lg p-2.5 bg-slate-900 rounded-lg border border-slate-800 select-none">
            <!-- 30 beads displayed for focus -->
        </div>

        <!-- Strategy Visual Explanation Box -->
        <div id="beadStrategyExplanation" class="mt-3 p-3 rounded-lg bg-teal-950/40 border border-teal-800/40 text-center w-full max-w-md">
            <div class="text-lg font-bold font-mono text-teal-300">15 + 5 = 20, then 20 + 2 = 22</div>
            <div class="text-xs text-slate-300 mt-1">Jump 5 beads to hit clean decade 20, then jump remaining 2 to reach 22!</div>
        </div>
    </div>
</div>
"""

# 6. Adding Larger Bundles
simulators_part1['sim_adding_larger_bundles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Interactive Lab 6</span>
            <h3 class="text-lg font-bold text-slate-100">Stamp Album Decade Leaps</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">22 + 30 = 52</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        You have <strong>22 stamps</strong> in an album. A gift packet adds <strong>30 stamps</strong> (3 full tens). Watch how decade additions modify only the tens place!
    </p>

    <!-- Visual Album Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <!-- Tens Bundles Visual -->
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col items-center">
                <span class="text-xs font-bold text-cyan-300 mb-2">Stamp Tens Bundles</span>
                <div id="stampBundlesDisplay" class="flex flex-wrap gap-2 justify-center my-1">
                    <!-- Dynamic bundles -->
                </div>
                <span id="stampBundlesTotalTxt" class="text-xs font-mono text-slate-300 mt-2">5 Tens Bundles (50) + 2 Loose = 52</span>
            </div>

            <!-- Number Line Decade Step Display -->
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col items-center">
                <span class="text-xs font-bold text-cyan-300 mb-2">Number Line Leaps of 10</span>
                <div class="w-full py-2 flex items-center justify-center font-mono text-xs">
                    <span class="px-2 py-1 rounded bg-slate-800 text-slate-300">22</span>
                    <span class="text-cyan-400 font-bold mx-1">➜ (+10) ➜</span>
                    <span class="px-2 py-1 rounded bg-slate-800 text-slate-300">32</span>
                    <span class="text-cyan-400 font-bold mx-1">➜ (+10) ➜</span>
                    <span class="px-2 py-1 rounded bg-slate-800 text-slate-300">42</span>
                    <span class="text-cyan-400 font-bold mx-1">➜ (+10) ➜</span>
                    <span class="px-2 py-1 rounded bg-cyan-600 text-white font-bold">52</span>
                </div>
                <div class="text-[11px] text-slate-400 mt-2 text-center">Three clean forward hops of 10!</div>
            </div>
        </div>

        <div id="stampAddingEquation" class="mt-3 p-2.5 rounded bg-cyan-950/40 border border-cyan-800/40 text-center font-mono font-bold text-cyan-300 text-base">
            22 + 30 = 52 Stamps
        </div>
    </div>

    <!-- Quick Jump Controls -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setStampAddition(22, 10)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Add +10 (32)</button>
        <button onclick="setStampAddition(22, 20)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Add +20 (42)</button>
        <button onclick="setStampAddition(22, 30)" class="px-3 py-1.5 bg-cyan-700 text-white rounded font-mono font-bold">Add +30 (52)</button>
        <button onclick="setStampAddition(22, 40)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Add +40 (62)</button>
    </div>
</div>
"""

# 7. Backward Line Jumps
simulators_part1['sim_backward_line_jumps'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Interactive Lab 7</span>
            <h3 class="text-lg font-bold text-slate-100">Backward Leaps (52 - 37)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-semibold border border-rose-500/30">52 - 37 = 15</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Out of <strong>52 stamps</strong>, 37 are portrait stamps. Find the remaining monument stamps by taking strategic backward leaps on an open number line!
    </p>

    <!-- Number Line Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center">
        <!-- SVG Step Animation -->
        <div class="w-full overflow-x-auto py-2">
            <svg id="backJumpSvg" viewBox="0 0 550 100" class="w-full min-w-[480px] h-24">
                <line x1="30" y1="60" x2="520" y2="60" stroke="#475569" stroke-width="3"/>
                <!-- Ticks -->
                <circle cx="500" cy="60" r="5" fill="#f43f5e"/>
                <text x="500" y="82" fill="#f43f5e" font-size="11" text-anchor="middle" font-family="monospace">52 (Start)</text>

                <!-- Hop 1 (-10) -->
                <path d="M500,55 Q450,20 400,55" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <text x="450" y="25" fill="#fda4af" font-size="10" text-anchor="middle">-10</text>
                <circle cx="400" cy="60" r="4" fill="#cbd5e1"/>
                <text x="400" y="82" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="monospace">42</text>

                <!-- Hop 2 (-10) -->
                <path d="M400,55 Q350,20 300,55" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <text x="350" y="25" fill="#fda4af" font-size="10" text-anchor="middle">-10</text>
                <circle cx="300" cy="60" r="4" fill="#cbd5e1"/>
                <text x="300" y="82" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="monospace">32</text>

                <!-- Hop 3 (-10) -->
                <path d="M300,55 Q250,20 200,55" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <text x="250" y="25" fill="#fda4af" font-size="10" text-anchor="middle">-10</text>
                <circle cx="200" cy="60" r="4" fill="#cbd5e1"/>
                <text x="200" y="82" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="monospace">22</text>

                <!-- Hop 4 (-7: split -2 to 20, -5 to 15) -->
                <path d="M200,55 Q165,30 130,55" fill="none" stroke="#f59e0b" stroke-width="2"/>
                <text x="165" y="32" fill="#fde68a" font-size="10" text-anchor="middle">-7</text>
                <circle cx="130" cy="60" r="6" fill="#10b981"/>
                <text x="130" y="82" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle" font-family="monospace">15 (Ans)</text>
            </svg>
        </div>

        <div id="backJumpResultTxt" class="mt-2 p-2.5 bg-slate-900 rounded-lg text-xs font-mono text-center text-slate-300 border border-slate-800">
            52 - 30 = 22, then 22 - 7 = <strong>15 Monument Stamps</strong>!
        </div>
    </div>

    <!-- Stepper Buttons -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setBackJumpDemo(52, 37)" class="px-3 py-1.5 bg-rose-700 text-white rounded font-mono font-bold">52 - 37 = 15</button>
        <button onclick="setBackJumpDemo(64, 28)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">64 - 28 = 36</button>
        <button onclick="setBackJumpDemo(75, 42)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">75 - 42 = 33</button>
    </div>
</div>
"""

# 8. Target Jump Projections
simulators_part1['sim_target_jump_projections'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 8</span>
            <h3 class="text-lg font-bold text-slate-100">Distance to Target (52 + ? = 75)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Forward Gap = 23</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        You have <strong>52 stamps</strong> and aim for <strong>75 stamps</strong>. Journey forward from 52 to 75 in structured leaps!
    </p>

    <!-- Target Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <div class="grid grid-cols-3 gap-2 max-w-sm mx-auto mb-3 text-xs">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-slate-400 block">Current</span>
                <span class="text-xl font-bold font-mono text-cyan-300">52</span>
            </div>
            <div class="bg-amber-950/40 p-2 rounded-lg border border-amber-600/50 flex flex-col items-center justify-center">
                <span class="text-[10px] text-amber-300 font-bold block">GAP NEEDED</span>
                <span id="targetGapDisplay" class="text-2xl font-black font-mono text-amber-400">23</span>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-slate-400 block">Goal Target</span>
                <span class="text-xl font-bold font-mono text-emerald-300">75</span>
            </div>
        </div>

        <!-- 2-Step Leap Diagram -->
        <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs font-mono text-slate-200">
            <div class="text-amber-300 font-bold text-sm mb-1">Two-Step Journey:</div>
            <div>Step 1: Jump +20 from 52 ➜ <strong class="text-cyan-300">72</strong></div>
            <div>Step 2: Jump +3 from 72 ➜ <strong class="text-emerald-300">75</strong></div>
            <div class="mt-2 text-emerald-400 font-bold">Total Stamps Needed: 20 + 3 = 23 Stamps!</div>
        </div>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setTargetDemo(52, 75)" class="px-3 py-1.5 bg-amber-600 text-white rounded font-mono font-bold">Target 75 from 52 (23)</button>
        <button onclick="setTargetDemo(40, 68)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Target 68 from 40 (28)</button>
        <button onclick="setTargetDemo(35, 80)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">Target 80 from 35 (45)</button>
    </div>
</div>
"""

print(f"Successfully generated {len(simulators_part1)} simulators for Part 1")


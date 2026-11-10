# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Class 3 Mathematics Chapter 3: Double Century."""

simulators_part1 = {}

# 1. Prehistoric Tallying
simulators_part1['sim_prehistoric_tally'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 1</span>
            <h3 class="text-lg font-bold text-slate-100">Cave Wall & Bone Notch Tallying</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Ancient Systems</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Before numerals were invented, humans scratched marks on rocks, bones, and bark to count cattle and moon cycles. Explore how grouping tally marks makes counting large numbers easy!
    </p>

    <!-- Visual Display -->
    <div class="bg-stone-950 border border-stone-800 rounded-xl p-4 min-h-[180px] flex flex-col justify-between relative overflow-hidden">
        <div class="flex items-center justify-between text-xs text-stone-400 mb-2 border-b border-stone-800 pb-1">
            <span>Rock Surface & Ancient Bone Simulator</span>
            <span id="tallyCountBadge" class="font-bold text-amber-400 text-sm">Total Marks: 17</span>
        </div>
        
        <!-- Bone & Scratches SVG Area -->
        <div id="tallyDisplayArea" class="flex flex-wrap gap-3 items-center min-h-[90px] py-2">
            <!-- Rendered dynamically by JS -->
        </div>

        <div id="tallyGroupingSummary" class="text-xs bg-stone-900/80 p-2.5 rounded-lg border border-stone-800 text-amber-200 font-mono mt-2">
            Grouping: 3 bundles of 5 + 2 single scratches = 17 marks
        </div>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="addTally(1)" class="px-3 py-2 bg-amber-600 hover:bg-amber-500 text-white rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 shadow">
            <span>+1 Scratch</span>
        </button>
        <button onclick="addTally(5)" class="px-3 py-2 bg-amber-700 hover:bg-amber-600 text-white rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 shadow">
            <span>+5 Bundle</span>
        </button>
        <button onclick="setTallyGroup(5)" id="btnGroup5" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 rounded-lg text-xs font-semibold transition">
            Group by 5s
        </button>
        <button onclick="setTallyGroup(10)" id="btnGroup10" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold transition">
            Group by 10s
        </button>
        <button onclick="setTallyGroup(20)" id="btnGroup20" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold transition">
            Group by 20s
        </button>
        <button onclick="resetTally()" class="px-3 py-2 bg-rose-900/60 hover:bg-rose-800 text-rose-200 border border-rose-700/50 rounded-lg text-xs font-bold transition col-span-2 sm:col-span-1">
            Reset (0)
        </button>
    </div>
</div>
"""

# 2. Indian Base Ten
simulators_part1['sim_base_ten_system'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Interactive Lab 2</span>
            <h3 class="text-lg font-bold text-slate-100">The Power of Ten Symbols</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">Ancient Indian Genius</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Ancient Indian mathematicians realized that using only ten symbols (<span class="font-mono text-emerald-300 font-bold">0, 1, 2, 3, 4, 5, 6, 7, 8, 9</span>) and place value, any number up to infinity can be written!
    </p>

    <!-- Digit Place Value Reels -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 text-center">
        <div class="grid grid-cols-3 gap-3 max-w-sm mx-auto mb-3">
            <!-- Hundreds Column -->
            <div class="bg-indigo-950/60 border border-indigo-700/50 rounded-xl p-2.5 flex flex-col items-center">
                <span class="text-[11px] font-bold uppercase tracking-wide text-indigo-300">Hundreds (H)</span>
                <div class="flex items-center justify-center gap-1 my-2">
                    <button onclick="changeDigit('h', -1)" class="w-7 h-7 rounded bg-indigo-900 hover:bg-indigo-800 text-white font-bold text-sm">-</button>
                    <span id="digitH" class="text-3xl font-black font-mono text-indigo-200 w-10 text-center">1</span>
                    <button onclick="changeDigit('h', 1)" class="w-7 h-7 rounded bg-indigo-900 hover:bg-indigo-800 text-white font-bold text-sm">+</button>
                </div>
                <span id="valH" class="text-xs font-mono text-indigo-400">100</span>
            </div>

            <!-- Tens Column -->
            <div class="bg-emerald-950/60 border border-emerald-700/50 rounded-xl p-2.5 flex flex-col items-center">
                <span class="text-[11px] font-bold uppercase tracking-wide text-emerald-300">Tens (T)</span>
                <div class="flex items-center justify-center gap-1 my-2">
                    <button onclick="changeDigit('t', -1)" class="w-7 h-7 rounded bg-emerald-900 hover:bg-emerald-800 text-white font-bold text-sm">-</button>
                    <span id="digitT" class="text-3xl font-black font-mono text-emerald-200 w-10 text-center">4</span>
                    <button onclick="changeDigit('t', 1)" class="w-7 h-7 rounded bg-emerald-900 hover:bg-emerald-800 text-white font-bold text-sm">+</button>
                </div>
                <span id="valT" class="text-xs font-mono text-emerald-400">40</span>
            </div>

            <!-- Ones Column -->
            <div class="bg-amber-950/60 border border-amber-700/50 rounded-xl p-2.5 flex flex-col items-center">
                <span class="text-[11px] font-bold uppercase tracking-wide text-amber-300">Ones (O)</span>
                <div class="flex items-center justify-center gap-1 my-2">
                    <button onclick="changeDigit('o', -1)" class="w-7 h-7 rounded bg-amber-900 hover:bg-amber-800 text-white font-bold text-sm">-</button>
                    <span id="digitO" class="text-3xl font-black font-mono text-amber-200 w-10 text-center">6</span>
                    <button onclick="changeDigit('o', 1)" class="w-7 h-7 rounded bg-amber-900 hover:bg-amber-800 text-white font-bold text-sm">+</button>
                </div>
                <span id="valO" class="text-xs font-mono text-amber-400">6</span>
            </div>
        </div>

        <!-- Place Value Expansion Equation -->
        <div class="bg-slate-900 rounded-lg p-3 border border-slate-800 inline-block w-full">
            <div class="text-xs text-slate-400 mb-1">Standard Expanded Form:</div>
            <div id="baseTenEquation" class="text-lg sm:text-xl font-bold font-mono text-amber-300">
                100 + 40 + 6 = 146
            </div>
            <div id="baseTenWordName" class="text-xs font-semibold text-slate-300 mt-1">
                "One Hundred Forty-Six"
            </div>
        </div>
    </div>

    <!-- Quick Preset Buttons -->
    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="setBaseTenPreset(1, 0, 0)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-mono">100 (Century)</button>
        <button onclick="setBaseTenPreset(1, 2, 5)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-mono">125 (Quarter)</button>
        <button onclick="setBaseTenPreset(1, 7, 2)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-mono">172</button>
        <button onclick="setBaseTenPreset(2, 0, 0)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-mono">200 (Double)</button>
    </div>
</div>
"""

# 3. Power of Zero
simulators_part1['sim_zero_placeholder'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Interactive Lab 3</span>
            <h3 class="text-lg font-bold text-slate-100">Zero as the Essential Placeholder</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">The Empty Place Guardian</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        What happens when a place has nothing in it? Without zero holding the tens column, <strong>105</strong> collapses into <strong>15</strong>! Try toggling zero to witness its crucial role.
    </p>

    <!-- Comparative Column Visual -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- WITH ZERO -->
            <div id="withZeroBox" class="bg-slate-900 border-2 border-cyan-500/60 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">With Zero Placeholder (105)</span>
                <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                    <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40">
                        <span class="text-[10px] text-indigo-300 block">HUNDREDS</span>
                        <span class="text-2xl font-black font-mono text-indigo-300">1</span>
                        <span class="text-[10px] text-slate-400 block">1 bundle (100)</span>
                    </div>
                    <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40">
                        <span class="text-[10px] text-cyan-300 block">TENS</span>
                        <span class="text-2xl font-black font-mono text-cyan-300">0</span>
                        <span class="text-[10px] text-cyan-400 block font-bold">Empty space</span>
                    </div>
                    <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                        <span class="text-[10px] text-amber-300 block">ONES</span>
                        <span class="text-2xl font-black font-mono text-amber-300">5</span>
                        <span class="text-[10px] text-slate-400 block">5 singles</span>
                    </div>
                </div>
                <div class="text-xs text-center text-slate-300 font-mono">Value: 100 + 0 + 5 = <strong class="text-cyan-300 text-sm">105</strong></div>
            </div>

            <!-- WITHOUT ZERO (COLLAPSED) -->
            <div id="withoutZeroBox" class="bg-rose-950/20 border border-rose-500/40 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Zero (Collapsed: 15)</span>
                <div class="grid grid-cols-2 gap-2 w-3/4 my-3 text-center">
                    <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40">
                        <span class="text-[10px] text-rose-300 block">TENS</span>
                        <span class="text-2xl font-black font-mono text-rose-300">1</span>
                        <span class="text-[10px] text-slate-400 block">1 ten (10)</span>
                    </div>
                    <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                        <span class="text-[10px] text-amber-300 block">ONES</span>
                        <span class="text-2xl font-black font-mono text-amber-300">5</span>
                        <span class="text-[10px] text-slate-400 block">5 singles</span>
                    </div>
                </div>
                <div class="text-xs text-center text-rose-300 font-mono">Value: 10 + 5 = <strong class="text-rose-400 text-sm">15 (Disaster! Lost 90!)</strong></div>
            </div>
        </div>

        <div class="mt-3 p-2.5 rounded bg-slate-900 border border-slate-800 text-xs text-slate-300 text-center">
            💡 <strong>Crucial Rule:</strong> Zero tells us there are <span class="text-cyan-300 font-semibold">no tens</span>, while holding the hundreds in the third spot!
        </div>
    </div>

    <!-- Exploration Options -->
    <div class="flex flex-wrap gap-2 justify-center">
        <button onclick="setZeroDemo(105)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold">Explore 105 (0 Tens)</button>
        <button onclick="setZeroDemo(150)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold">Explore 150 (0 Ones)</button>
        <button onclick="setZeroDemo(200)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold">Explore 200 (0 Tens, 0 Ones)</button>
    </div>
</div>
"""

# 4. Marketplace Estimation Counting
simulators_part1['sim_marketplace_counting'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Interactive Lab 4</span>
            <h3 class="text-lg font-bold text-slate-100">Marketplace Vendor Counting</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-orange-500/20 text-orange-300 font-semibold border border-orange-500/30">Estimation vs Tens Bundles</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        At the weekly village bazaar, vendors organize items in groups of 10 for fast counting. Select a market stall to estimate, then count packed boxes and loose items!
    </p>

    <!-- Stall Selector -->
    <div class="flex gap-2 border-b border-slate-800 pb-2">
        <button onclick="selectMarketStall('laddoos')" id="stallBtnLaddoos" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-orange-600 text-white">Sweet Stall (Laddoos)</button>
        <button onclick="selectMarketStall('bangles')" id="stallBtnBangles" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Bangle Stall</button>
        <button onclick="selectMarketStall('bananas')" id="stallBtnBananas" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">Fruit Vendor</button>
    </div>

    <!-- Stall Display Area -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="flex justify-between items-center mb-3">
            <span id="stallItemTitle" class="text-xs font-bold text-orange-300 uppercase">Laddoo Stall: Boxes of 10 & Single Laddoos</span>
            <span id="stallTotalBadge" class="text-sm font-black font-mono text-amber-400">Total: 47</span>
        </div>

        <!-- Visual representation -->
        <div id="stallVisualContainer" class="min-h-[110px] bg-slate-900/60 rounded-lg p-3 border border-slate-800 flex flex-wrap items-center gap-3">
            <!-- Dynamic Boxes of 10 & Loose items -->
        </div>

        <div class="grid grid-cols-2 gap-2 mt-3 text-xs">
            <div class="bg-slate-900 p-2 rounded border border-slate-800 text-center">
                <span class="text-slate-400 block">Packed Tens:</span>
                <span id="stallTensCount" class="font-bold text-orange-400 text-base">4 boxes (40)</span>
            </div>
            <div class="bg-slate-900 p-2 rounded border border-slate-800 text-center">
                <span class="text-slate-400 block">Loose Singles:</span>
                <span id="stallOnesCount" class="font-bold text-amber-300 text-base">7 single sweets (7)</span>
            </div>
        </div>
    </div>

    <!-- Adjuster Controls -->
    <div class="flex items-center justify-between text-xs">
        <div class="flex gap-2">
            <button onclick="adjustMarketItem('box', 1)" class="px-3 py-1.5 rounded bg-orange-700 hover:bg-orange-600 font-bold">+1 Box (10)</button>
            <button onclick="adjustMarketItem('box', -1)" class="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 font-bold">-1 Box</button>
        </div>
        <div class="flex gap-2">
            <button onclick="adjustMarketItem('loose', 1)" class="px-3 py-1.5 rounded bg-amber-700 hover:bg-amber-600 font-bold">+1 Single</button>
            <button onclick="adjustMarketItem('loose', -1)" class="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 font-bold">-1 Single</button>
        </div>
    </div>
</div>
"""

# 5. Snakes Ladders Grid
simulators_part1['sim_snakes_ladders_grid'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Interactive Lab 5</span>
            <h3 class="text-lg font-bold text-slate-100">100-Grid Snakes & Ladders</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-semibold border border-rose-500/30">Row Tens & Navigation</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        In a 10×10 grid, moving one row straight up adds exactly <strong>+10</strong>! Test your piece on the board, climb ladders, and see how matchstick bundles match board numbers.
    </p>

    <!-- Mini Board Display -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="flex justify-between items-center w-full mb-2 text-xs">
            <span class="text-slate-400">Current Position: <strong id="gridPlayerPos" class="text-rose-400 text-sm font-mono">24</strong></span>
            <span id="gridBundleNotation" class="text-amber-300 font-mono">2 bundles of 10 + 4 loose</span>
        </div>

        <!-- 10x10 Interactive Mini Grid -->
        <div id="snakesMiniGrid" class="grid grid-cols-10 gap-1 w-full max-w-md aspect-square bg-slate-900 p-2 rounded-lg border border-slate-800 select-none">
            <!-- 100 cells generated dynamically -->
        </div>

        <div id="gridActionStatus" class="mt-2 text-xs font-semibold text-center text-slate-300">
            Click any cell or roll the dice to navigate!
        </div>
    </div>

    <!-- Navigation Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="rollSnakesDice()" class="px-3 py-2 bg-rose-600 hover:bg-rose-500 text-white rounded-lg text-xs font-bold shadow">
            🎲 Roll Dice
        </button>
        <button onclick="stepGridPos(10)" class="px-3 py-2 bg-indigo-700 hover:bg-indigo-600 text-white rounded-lg text-xs font-bold shadow">
            ⬆️ Jump Row (+10)
        </button>
        <button onclick="stepGridPos(-10)" class="px-3 py-2 bg-indigo-900 hover:bg-indigo-800 text-slate-200 rounded-lg text-xs font-bold">
            ⬇️ Down Row (-10)
        </button>
        <button onclick="resetGridPos()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold">
            Reset to 1
        </button>
    </div>
</div>
"""

# 6. The Talking Pot
simulators_part1['sim_talking_pot_increment'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Interactive Lab 6</span>
            <h3 class="text-lg font-bold text-slate-100">The Magical Talking Pot</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30">Consecutive Successors (N + 1)</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Whenever a number enters the magical clay pot, it chimes and speaks the immediate next number! Type any number or click presets to see the pot glow and announce the successor.
    </p>

    <!-- Pot Visual Scene -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col items-center relative overflow-hidden">
        <!-- SVG Talking Pot -->
        <div class="relative w-48 h-44 flex items-center justify-center my-2">
            <svg id="potSvg" viewBox="0 0 200 180" class="w-full h-full transition-transform duration-300">
                <!-- Pot Base & Rim -->
                <ellipse cx="100" cy="35" rx="55" ry="12" fill="#7c2d12" stroke="#ea580c" stroke-width="3"/>
                <ellipse cx="100" cy="35" rx="42" ry="7" fill="#431407"/>
                <!-- Pot Body -->
                <path d="M55,35 C30,70 20,130 60,165 C85,178 115,178 140,165 C180,130 170,70 145,35 Z" fill="#9a3412" stroke="#ea580c" stroke-width="4"/>
                <!-- Clay Decorative bands -->
                <path d="M38,95 Q100,120 162,95" fill="none" stroke="#fed7aa" stroke-width="3" stroke-dasharray="6,4"/>
                <path d="M42,120 Q100,145 158,120" fill="none" stroke="#f97316" stroke-width="2"/>
                <!-- Pot Eyes / Face -->
                <circle cx="82" cy="85" r="5" fill="#fef08a"/>
                <circle cx="118" cy="85" r="5" fill="#fef08a"/>
                <circle cx="82" cy="85" r="2" fill="#1e293b"/>
                <circle cx="118" cy="85" r="2" fill="#1e293b"/>
                <!-- Smile -->
                <path id="potMouth" d="M85,105 Q100,120 115,105" fill="none" stroke="#fef08a" stroke-width="3" stroke-linecap="round"/>
            </svg>
            
            <!-- Floating Bubble Output -->
            <div id="potBubble" class="absolute -top-1 bg-purple-600 text-white font-mono font-black text-xl px-4 py-1.5 rounded-full shadow-lg border-2 border-purple-300 transform scale-0 transition-transform duration-300">
                100!
            </div>
        </div>

        <!-- Pot Output Message -->
        <div id="potSpeechOutput" class="text-sm font-bold text-purple-300 bg-purple-950/40 border border-purple-800/40 rounded-lg px-4 py-2 mt-1 text-center w-full max-w-sm">
            "Feed me a number to hear its next successor!"
        </div>
    </div>

    <!-- Input Controls -->
    <div class="flex flex-col sm:flex-row gap-2 items-center justify-center pt-1">
        <div class="flex items-center gap-2">
            <span class="text-xs text-slate-300">Enter Number:</span>
            <input type="number" id="potInputNumber" value="99" min="0" max="999" class="w-20 px-2.5 py-1.5 bg-slate-800 border border-slate-700 rounded-lg text-amber-300 font-mono font-bold text-center text-sm focus:outline-none focus:border-purple-500">
        </div>
        <button onclick="activateTalkingPot()" class="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white font-bold rounded-lg text-xs shadow-md transition">
            ✨ Drop Into Talking Pot
        </button>
    </div>

    <div class="flex flex-wrap gap-2 justify-center text-xs">
        <button onclick="quickFeedPot(9)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">Feed 9</button>
        <button onclick="quickFeedPot(49)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">Feed 49</button>
        <button onclick="quickFeedPot(99)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-purple-300 font-mono font-bold">Feed 99</button>
        <button onclick="quickFeedPot(149)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-300 font-mono">Feed 149</button>
        <button onclick="quickFeedPot(199)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 rounded text-amber-300 font-mono font-bold">Feed 199</button>
    </div>
</div>
"""

# 7. Defining One Hundred
simulators_part1['sim_defining_hundred'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-yellow-400">Interactive Lab 7</span>
            <h3 class="text-lg font-bold text-slate-100">Multiple Faces of 100</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-yellow-500/20 text-yellow-300 font-semibold border border-yellow-500/30">The Grand Century</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        100 is a monumental milestone in mathematics! Explore four real-world perspectives on what makes a complete hundred.
    </p>

    <!-- Representation Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 border-b border-slate-800 pb-2 text-xs">
        <button onclick="setHundredView('cricket')" id="hViewTabCricket" class="px-2.5 py-2 rounded-lg font-bold bg-yellow-600 text-white">🏏 Cricket Century</button>
        <button onclick="setHundredView('bundles')" id="hViewTabBundles" class="px-2.5 py-2 rounded-lg font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">🪵 10 Tens Bundles</button>
        <button onclick="setHundredView('successor')" id="hViewTabSuccessor" class="px-2.5 py-2 rounded-lg font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">➕ 99 + 1 Step</button>
        <button onclick="setHundredView('bindis')" id="hViewTabBindis" class="px-2.5 py-2 rounded-lg font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">🔴 10 Bindi Cards</button>
    </div>

    <!-- Active View Display -->
    <div id="hundredViewPanel" class="bg-slate-950 border border-slate-800 rounded-xl p-4 min-h-[160px] flex flex-col justify-center items-center text-center">
        <!-- Rendered dynamically -->
    </div>

    <!-- Summary Box -->
    <div class="bg-slate-900 border border-slate-800 rounded-lg p-3 text-xs text-center text-slate-300 font-mono">
        <span class="text-yellow-400 font-bold">Mathematical Identity:</span> 1 Hundred = 10 Tens = 100 Ones = 99 + 1
    </div>
</div>
"""

# 8. Making One Hundred
simulators_part1['sim_making_hundred_pairs'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Interactive Lab 8</span>
            <h3 class="text-lg font-bold text-slate-100">Ginladi 100-Bead String Pairs</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-teal-500/20 text-teal-300 font-semibold border border-teal-500/30">Complementary Pairs</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        A Ginladi is a traditional 100-bead string with alternating groups of 10 red and 10 white beads. Move the divider clip to find friendly pairs that add up to 100!
    </p>

    <!-- Bead String Container -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
        <div class="flex justify-between items-center mb-2 text-xs">
            <span class="text-slate-400">Divider Position: <strong id="beadSplitValue" class="text-teal-300 font-mono text-sm">60</strong></span>
            <span class="text-teal-400 font-bold font-mono">Total = 100 Beads</span>
        </div>

        <!-- 100 Beads Visualization -->
        <div id="ginladiBeadTrack" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 flex flex-wrap gap-1 items-center justify-center select-none py-3">
            <!-- 10 groups of 10 beads -->
        </div>

        <!-- Complementary Equation Display -->
        <div class="mt-4 p-3 rounded-lg bg-teal-950/40 border border-teal-800/40 text-center">
            <div id="hundredPairEquation" class="text-xl sm:text-2xl font-black font-mono text-teal-300">
                60 + 40 = 100
            </div>
            <div id="hundredPairExplanation" class="text-xs text-slate-300 mt-1">
                Part A: 6 tens (60) + Part B: 4 tens (40) = 10 tens (100)
            </div>
        </div>
    </div>

    <!-- Slider & Presets -->
    <div class="space-y-2">
        <div class="flex items-center gap-3">
            <span class="text-xs text-slate-400 w-16">Split at:</span>
            <input type="range" id="ginladiSlider" min="0" max="100" step="5" value="60" oninput="updateGinladi(this.value)" class="w-full accent-teal-400 cursor-pointer">
            <span id="sliderValDisplay" class="text-xs font-mono font-bold text-teal-300 w-10 text-right">60</span>
        </div>

        <div class="flex flex-wrap gap-2 justify-center text-xs pt-1">
            <button onclick="setGinladiVal(50)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">50 + 50</button>
            <button onclick="setGinladiVal(70)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">70 + 30</button>
            <button onclick="setGinladiVal(85)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">85 + 15</button>
            <button onclick="setGinladiVal(95)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono">95 + 5</button>
        </div>
    </div>
</div>
"""

print(f"Successfully created {len(simulators_part1)} simulators for Part 1")


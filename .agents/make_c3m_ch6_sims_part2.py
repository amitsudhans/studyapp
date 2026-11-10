# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

simulators_part2 = {}

# 9. Advancing Four Hundred
simulators_part2['sim_advancing_four_hundred'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 9</span>
            <h3 class="text-lg font-bold text-slate-100">Advancing Toward Four Hundred</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-500/20 text-blue-300 font-semibold border border-blue-500/30">Distance to Next Century</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Plot numbers approaching 400 and calculate the two-step mental jump distance to reach the fourth century milestone!
    </p>

    <!-- Distance Gauge Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="fourHundSvg" viewBox="0 0 360 140" class="w-full max-w-[420px] h-36 bg-slate-900 rounded-lg shadow-inner">
            <!-- Axis 300 to 400 -->
            <line x1="40" y1="70" x2="320" y2="70" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>

            <!-- 300 Mark -->
            <line x1="40" y1="55" x2="40" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="40" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">300</text>

            <!-- 350 Midpoint -->
            <line x1="180" y1="60" x2="180" y2="80" stroke="#94a3b8" stroke-width="2"/>
            <text x="180" y="102" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">350</text>

            <!-- 400 Landmark Milestone -->
            <line x1="320" y1="50" x2="320" y2="90" stroke="#f59e0b" stroke-width="4"/>
            <text x="320" y="105" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">400 ⭐</text>

            <!-- Current Target Pin (Default 387 -> x=283) -->
            <g id="fourHundPin" transform="translate(283, 0)">
                <circle cx="0" cy="70" r="6" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
                <polygon points="0,58 -5,48 5,48" fill="#38bdf8"/>
                <text id="fourHundPinTxt" x="0" y="42" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">387</text>
            </g>

            <!-- Jump Arc Representation -->
            <path id="jumpArc" d="M 283 70 Q 301 35 320 70" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3 3"/>
        </svg>

        <div id="fourHundCalcBanner" class="mt-2 text-xs text-blue-300 font-semibold bg-blue-950/40 px-3 py-1.5 rounded-lg border border-blue-800/40 text-center w-full font-mono">
            📏 387 is 13 units away from 400! (Step 1: 387 + 3 = 390; Step 2: 390 + 10 = 400).
        </div>
    </div>

    <!-- Target Selector Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setFourHundTarget(387)" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            1. Target 387 (13 to 400)
        </button>
        <button onclick="setFourHundTarget(329)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. Target 329 (71 to 400)
        </button>
        <button onclick="setFourHundTarget(350)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            3. Target 350 (50 to 400)
        </button>
    </div>
</div>

<script>
window.setFourHundTarget = function(val) {
    const pin = document.getElementById('fourHundPin');
    const txt = document.getElementById('fourHundPinTxt');
    const banner = document.getElementById('fourHundCalcBanner');
    const arc = document.getElementById('jumpArc');

    if (!pin || !txt || !banner) return;

    // x mapping: 300->40, 400->320 (width = 280)
    const x = 40 + ((val - 300) / 100) * 280;
    pin.setAttribute('transform', 'translate(' + x.toFixed(1) + ', 0)');
    txt.innerText = val.toString();

    const dist = 400 - val;
    if (arc) {
        arc.setAttribute('d', 'M ' + x.toFixed(1) + ' 70 Q ' + ((x + 320)/2).toFixed(1) + ' 35 320 70');
    }

    banner.innerText = "📏 " + val + " is " + dist + " units away from 400! (400 - " + val + " = " + dist + ")";
};
</script>
"""

# 10. Sweet Shop Inventory
simulators_part2['sim_sweet_shop_inventory'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 10</span>
            <h3 class="text-lg font-bold text-slate-100">Bakery Sweet Inventory (Past 400 to 500)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Hundreds Trays</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Pack sweet treats into hundred trays, ten boxes, and loose singles to count past 400 up to the 500 threshold!
    </p>

    <!-- Inventory Display Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="grid grid-cols-3 gap-3 w-full text-center">
            <!-- 100 Trays -->
            <div class="bg-slate-900/90 border border-amber-500/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-amber-400 block mb-1">Trays of 100</span>
                <span id="invTraysTxt" class="text-2xl font-black text-amber-300 font-mono">4</span>
                <span class="text-[11px] text-slate-400 block">🍱🍱🍱🍱 (400)</span>
            </div>

            <!-- 10 Boxes -->
            <div class="bg-slate-900/90 border border-cyan-500/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-cyan-400 block mb-1">Boxes of 10</span>
                <span id="invBoxesTxt" class="text-2xl font-black text-cyan-300 font-mono">8</span>
                <span class="text-[11px] text-slate-400 block">📦 (80)</span>
            </div>

            <!-- Singles -->
            <div class="bg-slate-900/90 border border-emerald-500/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-emerald-400 block mb-1">Single Sweets</span>
                <span id="invSinglesTxt" class="text-2xl font-black text-emerald-300 font-mono">7</span>
                <span class="text-[11px] text-slate-400 block">🍬 (7)</span>
            </div>
        </div>

        <div id="invMathBanner" class="mt-3 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            🧁 Dhokla Inventory: 4 Trays (400) + 8 Boxes (80) + 7 Singles (7) = 487 Sweets!
        </div>
    </div>

    <!-- Presets -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setSweetInventory(4, 2, 3, 'Mysore Pak')" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            423 Mysore Pak
        </button>
        <button onclick="setSweetInventory(4, 8, 7, 'Dhoklas')" class="px-2.5 py-1.5 bg-amber-600 hover:bg-amber-500 text-white rounded-lg text-xs font-bold transition">
            487 Dhoklas
        </button>
        <button onclick="setSweetInventory(5, 0, 0, 'Besan Laddoos')" class="px-2.5 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition">
            500 Laddoos (Max)
        </button>
    </div>
</div>

<script>
window.setSweetInventory = function(trays, boxes, singles, item) {
    const t = document.getElementById('invTraysTxt');
    const b = document.getElementById('invBoxesTxt');
    const s = document.getElementById('invSinglesTxt');
    const banner = document.getElementById('invMathBanner');

    if (!t || !b || !s || !banner) return;

    t.innerText = trays;
    b.innerText = boxes;
    s.innerText = singles;

    const total = trays * 100 + boxes * 10 + singles;
    banner.innerText = "🧁 " + item + " Inventory: " + trays + " Trays (" + (trays*100) + ") + " + boxes + " Boxes (" + (boxes*10) + ") + " + singles + " Singles = " + total + " Sweets!";
};
</script>
"""

# 11. Apartment Grid Navigation
simulators_part2['sim_apartment_grid_navigation'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 11</span>
            <h3 class="text-lg font-bold text-slate-100">Hop Hundreds Home Apartment Grid</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">Floor ±10, Door ±1</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Click any apartment door on this 10-column multi-floor residential building grid to discover neighbor coordinate rules!
    </p>

    <!-- Apartment Matrix Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <!-- 3 sample floors: Floor 3 (121-130), Floor 2 (111-120), Floor 1 (101-110) -->
        <div class="space-y-1.5 w-full max-w-[420px]">
            <!-- Floor 3 (120s) -->
            <div class="flex items-center gap-1">
                <span class="text-[10px] font-bold text-slate-500 w-12 text-right">Floor 3:</span>
                <div class="grid grid-cols-10 gap-1 flex-1">
                    <button onclick="selectApt(121)" id="apt-121" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">121</button>
                    <button onclick="selectApt(122)" id="apt-122" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">122</button>
                    <button onclick="selectApt(123)" id="apt-123" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">123</button>
                    <button onclick="selectApt(124)" id="apt-124" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">124</button>
                    <button onclick="selectApt(125)" id="apt-125" class="apt-btn p-1 text-[10px] font-mono bg-cyan-600 font-bold text-white rounded text-center">125</button>
                    <button onclick="selectApt(126)" id="apt-126" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">126</button>
                    <button onclick="selectApt(127)" id="apt-127" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">127</button>
                    <button onclick="selectApt(128)" id="apt-128" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">128</button>
                    <button onclick="selectApt(129)" id="apt-129" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">129</button>
                    <button onclick="selectApt(130)" id="apt-130" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">130</button>
                </div>
            </div>

            <!-- Floor 2 (110s) -->
            <div class="flex items-center gap-1">
                <span class="text-[10px] font-bold text-slate-500 w-12 text-right">Floor 2:</span>
                <div class="grid grid-cols-10 gap-1 flex-1">
                    <button onclick="selectApt(111)" id="apt-111" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">111</button>
                    <button onclick="selectApt(112)" id="apt-112" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">112</button>
                    <button onclick="selectApt(113)" id="apt-113" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">113</button>
                    <button onclick="selectApt(114)" id="apt-114" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">114</button>
                    <button onclick="selectApt(115)" id="apt-115" class="apt-btn p-1 text-[10px] font-mono bg-amber-500 font-bold text-slate-950 rounded text-center shadow-md">115</button>
                    <button onclick="selectApt(116)" id="apt-116" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">116</button>
                    <button onclick="selectApt(117)" id="apt-117" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">117</button>
                    <button onclick="selectApt(118)" id="apt-118" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">118</button>
                    <button onclick="selectApt(119)" id="apt-119" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">119</button>
                    <button onclick="selectApt(120)" id="apt-120" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">120</button>
                </div>
            </div>

            <!-- Floor 1 (100s) -->
            <div class="flex items-center gap-1">
                <span class="text-[10px] font-bold text-slate-500 w-12 text-right">Floor 1:</span>
                <div class="grid grid-cols-10 gap-1 flex-1">
                    <button onclick="selectApt(101)" id="apt-101" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">101</button>
                    <button onclick="selectApt(102)" id="apt-102" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">102</button>
                    <button onclick="selectApt(103)" id="apt-103" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">103</button>
                    <button onclick="selectApt(104)" id="apt-104" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">104</button>
                    <button onclick="selectApt(105)" id="apt-105" class="apt-btn p-1 text-[10px] font-mono bg-emerald-600 font-bold text-white rounded text-center">105</button>
                    <button onclick="selectApt(106)" id="apt-106" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">106</button>
                    <button onclick="selectApt(107)" id="apt-107" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">107</button>
                    <button onclick="selectApt(108)" id="apt-108" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">108</button>
                    <button onclick="selectApt(109)" id="apt-109" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">109</button>
                    <button onclick="selectApt(110)" id="apt-110" class="apt-btn p-1 text-[10px] font-mono bg-slate-800 hover:bg-slate-700 rounded text-center">110</button>
                </div>
            </div>
        </div>

        <div id="aptRulesNotice" class="mt-3 text-xs text-cyan-300 font-semibold bg-cyan-950/40 px-3 py-1.5 rounded-lg border border-cyan-800/40 text-center w-full font-mono">
            🏢 Selected Apt 115: One floor up is 125 (+10). One floor down is 105 (-10)!
        </div>
    </div>
</div>

<script>
window.selectApt = function(num) {
    const notice = document.getElementById('aptRulesNotice');
    if (!notice) return;

    const up = num + 10;
    const down = num - 10;
    const left = num - 1;
    const right = num + 1;

    notice.innerText = "🏢 Selected Apt " + num + ": Floor Above = " + up + " (+10) | Floor Below = " + down + " (-10) | Right Door = " + right + " (+1)";
};
</script>
"""

# 12. Mystery House Clues
simulators_part2['sim_mystery_house_clues'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 12</span>
            <h3 class="text-lg font-bold text-slate-100">Mystery House Detective Deduction</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-violet-500/20 text-violet-300 font-semibold border border-violet-500/30">Coordinate Riddles</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Solve spatial architectural riddles to deduce secret apartment numbers from floor numbers and column digits!
    </p>

    <!-- Riddle Box Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 w-full max-w-[420px] space-y-3">
            <div class="flex items-center gap-2 text-xs font-bold text-violet-400 uppercase tracking-wider">
                <span>🕵️ Detective Case File</span>
            </div>
            <p id="riddleTextPrompt" class="text-xs sm:text-sm text-slate-200 font-medium">
                "I am located on Floor 4 (40s decade) of Jump Joy Residency. My column ends in the digit 7. What apartment am I?"
            </p>
            <div class="flex justify-between items-center pt-2 border-t border-slate-800">
                <span id="riddleDeductionAnswer" class="text-xs font-mono font-bold text-amber-300">Deduction: 200 + 40 + 7 = ?</span>
                <button onclick="revealMysteryApt('247')" class="px-3 py-1.5 bg-violet-600 hover:bg-violet-500 rounded-lg text-xs font-bold transition">
                    🔍 Solve Riddle
                </button>
            </div>
        </div>

        <div id="riddleSolutionNotice" class="mt-3 text-xs text-violet-300 font-semibold bg-violet-950/40 px-3 py-1.5 rounded-lg border border-violet-800/40 text-center w-full font-mono">
            🚪 Click "Solve Riddle" to reveal the mystery resident apartment!
        </div>
    </div>

    <!-- Riddle Selectors -->
    <div class="grid grid-cols-2 gap-2 pt-1">
        <button onclick="loadRiddle(1)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            Case 1: Floor 4, Col 7
        </button>
        <button onclick="loadRiddle(2)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            Case 2: Between 231 & 233
        </button>
    </div>
</div>

<script>
window.currRiddleCase = 1;

window.loadRiddle = function(c) {
    window.currRiddleCase = c;
    const p = document.getElementById('riddleTextPrompt');
    const a = document.getElementById('riddleDeductionAnswer');
    const n = document.getElementById('riddleSolutionNotice');

    if (c === 1) {
        p.innerText = '"I am located on Floor 4 (40s decade) of Jump Joy Residency. My column ends in the digit 7. What apartment am I?"';
        a.innerText = "Deduction: 200 + 40 + 7 = ?";
        n.innerText = '🚪 Click "Solve Riddle" to reveal the mystery resident apartment!';
    } else {
        p.innerText = '"I am situated directly between apartment 231 and 233, and directly below apartment 242. Who am I?"';
        a.innerText = "Deduction: Between 231 & 233, or 242 - 10 = ?";
        n.innerText = '🚪 Click "Solve Riddle" to reveal the mystery resident apartment!';
    }
};

window.revealMysteryApt = function() {
    const a = document.getElementById('riddleDeductionAnswer');
    const n = document.getElementById('riddleSolutionNotice');

    if (window.currRiddleCase === 1) {
        a.innerText = "Deduction: 200 + 40 + 7 = 247!";
        n.innerText = "🎉 Case Solved: Apartment 247! (Floor 4 gives 40s decade, Column 7 gives 7 ones).";
    } else {
        a.innerText = "Deduction: 231 < 232 < 233 and 242 - 10 = 232!";
        n.innerText = "🎉 Case Solved: Apartment 232! (Both horizontal neighbor and vertical column clues match).";
    }
};
</script>
"""

# 13. Dienes Block Models
simulators_part2['sim_dienes_block_models'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 13</span>
            <h3 class="text-lg font-bold text-slate-100">Dienes Base-10 Block Modeler</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">Flats, Rods, Cubes</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Construct 3-digit numbers using 100-flats (squares), 10-rods (sticks), and 1-cubes (units) across H-T-O columns!
    </p>

    <!-- Block Workspace Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="grid grid-cols-3 gap-3 w-full text-center">
            <!-- Hundreds Flat Column -->
            <div class="bg-slate-900/90 border border-emerald-500/40 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold uppercase text-emerald-400 mb-1">Hundreds Flats</span>
                <span id="flatsCount" class="text-3xl font-black text-emerald-300 font-mono">3</span>
                <span class="text-[10px] text-slate-400 mt-1">🟩🟩🟩 (300)</span>
            </div>

            <!-- Tens Rod Column -->
            <div class="bg-slate-900/90 border border-blue-500/40 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold uppercase text-blue-400 mb-1">Tens Rods</span>
                <span id="rodsCount" class="text-3xl font-black text-blue-300 font-mono">4</span>
                <span class="text-[10px] text-slate-400 mt-1">🪵🪵🪵🪵 (40)</span>
            </div>

            <!-- Ones Cube Column -->
            <div class="bg-slate-900/90 border border-amber-500/40 rounded-xl p-3 flex flex-col items-center">
                <span class="text-xs font-bold uppercase text-amber-400 mb-1">Unit Cubes</span>
                <span id="cubesCount" class="text-3xl font-black text-amber-300 font-mono">2</span>
                <span class="text-[10px] text-slate-400 mt-1">🟨🟨 (2)</span>
            </div>
        </div>

        <div id="dienesExpBanner" class="mt-3 text-xs text-emerald-300 font-semibold bg-emerald-950/40 px-3 py-1.5 rounded-lg border border-emerald-800/40 text-center w-full font-mono">
            🧮 Model Value: 3 Flats (300) + 4 Rods (40) + 2 Cubes (2) = 342!
        </div>
    </div>

    <!-- Stepper Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setDienesModel(3, 4, 2)" class="px-3 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-xl text-xs font-bold transition">
            1. 342 (3F + 4R + 2C)
        </button>
        <button onclick="setDienesModel(4, 4, 2)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. 442 (+1 Flat)
        </button>
        <button onclick="setDienesModel(4, 2, 2)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            3. 422 (-2 Rods)
        </button>
    </div>
</div>

<script>
window.setDienesModel = function(f, r, c) {
    const fc = document.getElementById('flatsCount');
    const rc = document.getElementById('rodsCount');
    const cc = document.getElementById('cubesCount');
    const banner = document.getElementById('dienesExpBanner');

    if (!fc || !rc || !cc || !banner) return;

    fc.innerText = f;
    rc.innerText = r;
    cc.innerText = c;

    const total = f * 100 + r * 10 + c;
    banner.innerText = "🧮 Model Value: " + f + " Flats (" + (f*100) + ") + " + r + " Rods (" + (r*10) + ") + " + c + " Cubes (" + c + ") = " + total + "!";
};
</script>
"""

# 14. Number Hunt Patterns
simulators_part2['sim_number_hunt_patterns'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 14</span>
            <h3 class="text-lg font-bold text-slate-100">Number Hunt Digit Filter (200-300)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-pink-500/20 text-pink-300 font-semibold border border-pink-500/30">Digit Position Rules</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Filter numbers between 200 and 300 to discover which numbers contain the digit 5 in ones, tens, or both places!
    </p>

    <!-- Filter Output Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div id="huntResultsContainer" class="flex flex-wrap gap-2 justify-center py-2 min-h-[90px] w-full max-w-[420px]">
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">205</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">215</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">225</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">235</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">245</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">255 ⭐</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">265</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">275</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">285</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">295</span>
        </div>

        <div id="huntFilterNotice" class="mt-2 text-xs text-pink-300 font-semibold bg-pink-950/40 px-3 py-1.5 rounded-lg border border-pink-800/40 text-center w-full font-mono">
            🎯 Filter: 10 numbers have 5 in the ONES column (ending in 5).
        </div>
    </div>

    <!-- Filter Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setHuntFilter('ones')" class="px-3 py-2 bg-pink-600 hover:bg-pink-500 rounded-xl text-xs font-bold transition">
            1. 5 in Ones Place
        </button>
        <button onclick="setHuntFilter('tens')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. 5 in Tens Place
        </button>
        <button onclick="setHuntFilter('both')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            3. 5 in Both Places
        </button>
    </div>
</div>

<script>
window.setHuntFilter = function(mode) {
    const box = document.getElementById('huntResultsContainer');
    const notice = document.getElementById('huntFilterNotice');
    if (!box || !notice) return;

    if (mode === 'ones') {
        box.innerHTML = `
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">205</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">215</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">225</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">235</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">245</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">255 ⭐</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">265</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">275</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">285</span>
            <span class="px-2.5 py-1 bg-pink-950/80 border border-pink-700 text-pink-300 font-mono text-xs rounded-lg font-bold">295</span>
        `;
        notice.innerText = "🎯 Filter: 10 numbers have 5 in the ONES column (205, 215, 225, 235, 245, 255, 265, 275, 285, 295).";
    } else if (mode === 'tens') {
        box.innerHTML = `
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">250</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">251</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">252</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">253</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">254</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">255 ⭐</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">256</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">257</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">258</span>
            <span class="px-2.5 py-1 bg-blue-950/80 border border-blue-700 text-blue-300 font-mono text-xs rounded-lg font-bold">259</span>
        `;
        notice.innerText = "🎯 Filter: 10 numbers have 5 in the TENS column (entire 250s decade from 250 to 259).";
    } else {
        box.innerHTML = `
            <span class="px-4 py-2 bg-emerald-600 border border-emerald-400 text-white font-mono text-sm rounded-xl font-black shadow-lg animate-bounce">255 ⭐</span>
        `;
        notice.innerText = "⭐ Unique Intersection: 255 is the ONLY number having 5 in BOTH tens and ones places!";
    }
};
</script>
"""

# 15. Place Value Comparisons
simulators_part2['sim_place_value_comparisons'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 15</span>
            <h3 class="text-lg font-bold text-slate-100">Place Value Comparison Balance Scale</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">H-T-O Hierarchy &gt;, &lt;</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Compare two 3-digit numbers using the greater than (&gt;) and less than (&lt;) balance scale!
    </p>

    <!-- Balance Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="flex items-center justify-center gap-4 py-2 w-full max-w-[380px]">
            <!-- Left Pan -->
            <div class="bg-slate-900 border-2 border-emerald-500/60 rounded-xl p-3 flex flex-col items-center w-36 shadow-lg">
                <span class="text-[10px] font-bold text-slate-400 uppercase">Left Number</span>
                <span id="cmpLeftVal" class="text-3xl font-black text-emerald-400 font-mono my-1">487</span>
                <span class="text-[10px] text-slate-400">4 Hundreds, 8 Tens</span>
            </div>

            <!-- Inequality Sign Badge -->
            <div id="cmpSignBadge" class="w-12 h-12 rounded-full bg-amber-500/20 border-2 border-amber-500 flex items-center justify-center font-black text-2xl text-amber-400 shadow-md">
                &gt;
            </div>

            <!-- Right Pan -->
            <div class="bg-slate-900 border-2 border-blue-500/60 rounded-xl p-3 flex flex-col items-center w-36 shadow-lg">
                <span class="text-[10px] font-bold text-slate-400 uppercase">Right Number</span>
                <span id="cmpRightVal" class="text-3xl font-black text-blue-400 font-mono my-1">423</span>
                <span class="text-[10px] text-slate-400">4 Hundreds, 2 Tens</span>
            </div>
        </div>

        <div id="cmpReasoningNotice" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            ⚖️ Place Value Reason: Hundreds are equal (4 = 4), but 8 tens &gt; 2 tens. Therefore, 487 &gt; 423!
        </div>
    </div>

    <!-- Comparison Presets -->
    <div class="grid grid-cols-2 gap-2 pt-1">
        <button onclick="setComparisonPair(487, 423, '&gt;', 'Hundreds equal (4 = 4), but 8 tens &gt; 2 tens. So 487 &gt; 423.')" class="px-3 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-xl text-xs font-bold transition">
            1. 487 vs 423 (487 &gt; 423)
        </button>
        <button onclick="setComparisonPair(209, 290, '&lt;', 'Hundreds equal (2 = 2), but 0 tens &lt; 9 tens. So 209 &lt; 290.')" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            2. 209 vs 290 (209 &lt; 290)
        </button>
    </div>
</div>

<script>
window.setComparisonPair = function(left, right, sign, reason) {
    const lEl = document.getElementById('cmpLeftVal');
    const rEl = document.getElementById('cmpRightVal');
    const sEl = document.getElementById('cmpSignBadge');
    const nEl = document.getElementById('cmpReasoningNotice');

    if (!lEl || !rEl || !sEl || !nEl) return;

    lEl.innerText = left;
    rEl.innerText = right;
    sEl.innerHTML = sign;
    nEl.innerText = "⚖️ Place Value Reason: " + reason;
};
</script>
"""

# 16. Ordering Three Digits
simulators_part2['sim_ordering_three_digits'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 16</span>
            <h3 class="text-lg font-bold text-slate-100">3-Digit Permutation & Ordering Machine</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">Min / Max Ordering</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Given digit cards 3, 7, and 5, view all 6 combinations, discover minimum and maximum values, and sort in order!
    </p>

    <!-- Ordering Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <!-- 3 Given Digit Cards -->
        <div class="flex items-center gap-3 mb-2">
            <span class="text-xs text-slate-400 font-bold uppercase">Given Digits:</span>
            <div class="flex gap-2">
                <span class="w-8 h-10 rounded-lg bg-amber-500/20 border border-amber-500 text-amber-300 flex items-center justify-center font-mono font-black text-base shadow">3</span>
                <span class="w-8 h-10 rounded-lg bg-cyan-500/20 border border-cyan-500 text-cyan-300 flex items-center justify-center font-mono font-black text-base shadow">7</span>
                <span class="w-8 h-10 rounded-lg bg-emerald-500/20 border border-emerald-500 text-emerald-300 flex items-center justify-center font-mono font-black text-base shadow">5</span>
            </div>
        </div>

        <!-- 6 Permutations Container -->
        <div id="permutationsBox" class="flex flex-wrap gap-2 justify-center py-2 max-w-[420px]">
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">357</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">375</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">537</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">573</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">735</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">753</span>
        </div>

        <div id="permOrderingNotice" class="mt-2 text-xs text-emerald-300 font-semibold bg-emerald-950/40 px-3 py-1.5 rounded-lg border border-emerald-800/40 text-center w-full font-mono">
            ⭐ 6 Permutations: Smallest = 357 (lowest digit in hundreds) | Greatest = 753 (highest digit in hundreds).
        </div>
    </div>

    <!-- Action Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setPermSort('all')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            1. All 6 Numbers
        </button>
        <button onclick="setPermSort('asc')" class="px-3 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-xl text-xs font-bold transition">
            2. Ascending Order (Smallest ➔ Greatest)
        </button>
        <button onclick="setPermSort('desc')" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            3. Descending Order (Greatest ➔ Smallest)
        </button>
    </div>
</div>

<script>
window.setPermSort = function(mode) {
    const box = document.getElementById('permutationsBox');
    const notice = document.getElementById('permOrderingNotice');
    if (!box || !notice) return;

    if (mode === 'asc') {
        box.innerHTML = `
            <span class="px-2 py-1 bg-emerald-950/80 border border-emerald-600 text-emerald-300 font-mono text-xs rounded-lg font-bold">357 (Min)</span>
            <span class="text-slate-500 text-xs flex items-center">&lt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">375</span>
            <span class="text-slate-500 text-xs flex items-center">&lt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">537</span>
            <span class="text-slate-500 text-xs flex items-center">&lt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">573</span>
            <span class="text-slate-500 text-xs flex items-center">&lt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">735</span>
            <span class="text-slate-500 text-xs flex items-center">&lt;</span>
            <span class="px-2 py-1 bg-emerald-950/80 border border-emerald-600 text-emerald-300 font-mono text-xs rounded-lg font-bold">753 (Max)</span>
        `;
        notice.innerText = "📈 Ascending Order: 357 < 375 < 537 < 573 < 735 < 753 (from lowest to highest value).";
    } else if (mode === 'desc') {
        box.innerHTML = `
            <span class="px-2 py-1 bg-blue-950/80 border border-blue-600 text-blue-300 font-mono text-xs rounded-lg font-bold">753 (Max)</span>
            <span class="text-slate-500 text-xs flex items-center">&gt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">735</span>
            <span class="text-slate-500 text-xs flex items-center">&gt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">573</span>
            <span class="text-slate-500 text-xs flex items-center">&gt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">537</span>
            <span class="text-slate-500 text-xs flex items-center">&gt;</span>
            <span class="px-2 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">375</span>
            <span class="text-slate-500 text-xs flex items-center">&gt;</span>
            <span class="px-2 py-1 bg-blue-950/80 border border-blue-600 text-blue-300 font-mono text-xs rounded-lg font-bold">357 (Min)</span>
        `;
        notice.innerText = "📉 Descending Order: 753 > 735 > 573 > 537 > 375 > 357 (from highest to lowest value).";
    } else {
        box.innerHTML = `
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">357</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">375</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">537</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">573</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">735</span>
            <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 text-slate-200 font-mono text-xs rounded-lg font-bold">753</span>
        `;
        notice.innerText = "⭐ 6 Permutations: Smallest = 357 (lowest digit in hundreds) | Greatest = 753 (highest digit in hundreds).";
    }
};
</script>
"""

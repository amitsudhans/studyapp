# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

simulators_part1 = {}

# 1. Counting Festival Torans
simulators_part1['sim_counting_festival_torans'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 1</span>
            <h3 class="text-lg font-bold text-slate-100">Festival Toran String Counter</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Tens Decade Counting</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Click to hang festive toran strings (10 flags each) across fairground stalls to count smoothly past two hundred up to 250!
    </p>

    <!-- Toran Visualizer Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="toranSvg" viewBox="0 0 360 170" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- Stall Canopy -->
            <path d="M 20 40 Q 90 20 180 40 Q 270 20 340 40" fill="none" stroke="#f59e0b" stroke-width="4"/>
            <line x1="20" y1="40" x2="20" y2="160" stroke="#78350f" stroke-width="4"/>
            <line x1="340" y1="40" x2="340" y2="160" stroke="#78350f" stroke-width="4"/>

            <!-- Dynamic Toran Strings Group -->
            <g id="toranStringsGroup">
                <!-- 20 baseline strings = 200 flags (represented as background bunting) -->
                <text x="180" y="70" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">Baseline: 20 Strings of 10 = 200 Flags</text>
            </g>

            <!-- Active Additional Decade Flags -->
            <g id="activeToranFlags">
                <!-- Dynamically rendered flags -->
            </g>
        </svg>

        <div id="toranMathBanner" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            🚩 Current Count: 200 + 0 = 200 Triangular Torans (20 Tens Strings)
        </div>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 pt-1">
        <button onclick="setToranCount(200)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            200 Flags
        </button>
        <button onclick="setToranCount(210)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            210 Flags (+10)
        </button>
        <button onclick="setToranCount(230)" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            230 Flags (+30)
        </button>
        <button onclick="setToranCount(250)" class="px-2.5 py-1.5 bg-amber-600 hover:bg-amber-500 text-white rounded-lg text-xs font-bold transition">
            250 Flags (Max)
        </button>
        <button onclick="addOneToranString()" class="col-span-2 sm:col-span-1 px-2.5 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition">
            ➕ Add 10
        </button>
    </div>
</div>

<script>
window.currTorans = 200;

window.setToranCount = function(val) {
    window.currTorans = val;
    renderTorans();
};

window.addOneToranString = function() {
    if (window.currTorans < 250) {
        window.currTorans += 10;
        renderTorans();
    }
};

function renderTorans() {
    const banner = document.getElementById('toranMathBanner');
    const grp = document.getElementById('activeToranFlags');
    if (!banner || !grp) return;

    const extra = window.currTorans - 200;
    const extraStrings = extra / 10;
    const totalStrings = 20 + extraStrings;

    banner.innerText = "🚩 Current Count: 200 + " + extra + " = " + window.currTorans + " Triangular Torans (" + totalStrings + " Tens Strings)";

    grp.innerHTML = "";
    const colors = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#a855f7"];
    for (let s = 0; s < extraStrings; s++) {
        const y = 90 + s * 14;
        const color = colors[s % colors.length];
        let flags = `<line x1="40" y1="${y}" x2="320" y2="${y}" stroke="#64748b" stroke-width="1.5"/>`;
        for (let f = 0; f < 10; f++) {
            const x = 50 + f * 27;
            flags += `<polygon points="${x},${y} ${x+12},${y} ${x+6},${y+10}" fill="${color}"/>`;
        }
        grp.innerHTML += flags;
    }
}
</script>
"""

# 2. Reaching Three Hundred
simulators_part1['sim_reaching_three_hundred'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 2</span>
            <h3 class="text-lg font-bold text-slate-100">Crossing the 300 Century Threshold</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-pink-500/20 text-pink-300 font-semibold border border-pink-500/30">298 + 1 + 1 = 300</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Observe the crate of fruit toffees. Click the button to add single toffees and watch how 299 regroups into exactly 300!
    </p>

    <!-- Stage Container -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full">
            <!-- Bangle Stall Display -->
            <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3 flex flex-col items-center justify-between">
                <span class="text-xs font-bold uppercase text-amber-400 tracking-wide mb-1">Bangle Stall Display</span>
                <div class="flex flex-wrap gap-1.5 justify-center py-2 max-w-[200px]">
                    <div class="text-2xl">⭕⭕⭕⭕</div>
                    <div class="text-2xl">⭕⭕⭕⭕</div>
                </div>
                <span class="text-xs font-mono text-slate-300 font-bold bg-slate-800 px-2 py-0.5 rounded">28 Rods × 10 = 280 Bangles</span>
            </div>

            <!-- Sweet Toffee Crate -->
            <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3 flex flex-col items-center justify-between">
                <span class="text-xs font-bold uppercase text-pink-400 tracking-wide mb-1">Toffee Crate Counter</span>
                <div id="toffeeBoxVisual" class="py-2 flex flex-col items-center">
                    <span id="toffeeNumDisplay" class="text-4xl font-extrabold text-pink-400 font-mono tracking-wider transition-all duration-300">298</span>
                    <span id="toffeeLabel" class="text-xs text-slate-400 mt-1">Starting Count: 298 Toffees</span>
                </div>
                <div class="flex gap-2">
                    <button onclick="addToffeeOne()" id="addToffeeBtn" class="px-3 py-1.5 bg-pink-600 hover:bg-pink-500 text-white rounded-lg text-xs font-bold transition">
                        🍬 Add 1 Toffee
                    </button>
                    <button onclick="resetToffees()" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold transition">
                        🔄 Reset
                    </button>
                </div>
            </div>
        </div>

        <div id="toffeeMathNotice" class="mt-3 text-xs text-pink-300 font-semibold bg-pink-950/40 px-3 py-1.5 rounded-lg border border-pink-800/40 text-center w-full font-mono">
            🍬 Starting with 298 toffees. Click "Add 1 Toffee" to step forward!
        </div>
    </div>
</div>

<script>
window.currToffees = 298;

window.addToffeeOne = function() {
    const disp = document.getElementById('toffeeNumDisplay');
    const lbl = document.getElementById('toffeeLabel');
    const notice = document.getElementById('toffeeMathNotice');
    const btn = document.getElementById('addToffeeBtn');

    if (window.currToffees === 298) {
        window.currToffees = 299;
        disp.innerText = "299";
        disp.className = "text-4xl font-extrabold text-amber-400 font-mono tracking-wider transition-all duration-300";
        lbl.innerText = "298 + 1 = 299 (1 away from 300!)";
        notice.innerText = "🍬 298 + 1 = 299. Just one more toffee to reach the milestone!";
    } else if (window.currToffees === 299) {
        window.currToffees = 300;
        disp.innerText = "300";
        disp.className = "text-5xl font-black text-emerald-400 font-mono tracking-wider animate-bounce transition-all duration-300";
        lbl.innerText = "🎉 299 + 1 = 300 (Milestone Reached!)";
        notice.innerText = "🎉 MILESTONE REACHED: 299 + 1 = 300! Exactly 3 Hundreds (30 Bundles of 10).";
        if (btn) btn.disabled = true;
    }
};

window.resetToffees = function() {
    window.currToffees = 298;
    const disp = document.getElementById('toffeeNumDisplay');
    const lbl = document.getElementById('toffeeLabel');
    const notice = document.getElementById('toffeeMathNotice');
    const btn = document.getElementById('addToffeeBtn');

    disp.innerText = "298";
    disp.className = "text-4xl font-extrabold text-pink-400 font-mono tracking-wider transition-all duration-300";
    lbl.innerText = "Starting Count: 298 Toffees";
    notice.innerText = "🍬 Starting with 298 toffees. Click 'Add 1 Toffee' to step forward!";
    if (btn) btn.disabled = false;
};
</script>
"""

# 3. Tiled Number Paths
simulators_part1['sim_tiled_number_paths'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 3</span>
            <h3 class="text-lg font-bold text-slate-100">Garden Tiled Number Pathway</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">Sequence Navigation</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Click the obscured stone tiles to restore missing consecutive numerals along the fairground garden path!
    </p>

    <!-- Stepping Stones Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="space-y-4 w-full">
            <!-- Path A: 211 to 216 -->
            <div class="space-y-1">
                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Path A: 210s Decade Stones</span>
                <div class="flex flex-wrap gap-2 justify-center">
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">211</div>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">212</div>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">213</div>
                    <!-- Hidden Stone 214 -->
                    <button id="stone214" onclick="revealStone('stone214', '214')" class="w-12 h-12 rounded-xl bg-amber-500/20 border-2 border-dashed border-amber-500 flex items-center justify-center font-mono font-bold text-amber-300 text-xs hover:bg-amber-500/30 transition">
                        ❓
                    </button>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">215</div>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">216</div>
                </div>
            </div>

            <!-- Path B: 298 to 304 -->
            <div class="space-y-1">
                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Path B: Crossing 300 Milestone</span>
                <div class="flex flex-wrap gap-2 justify-center">
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">298</div>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">299</div>
                    <!-- Milestone Stone 300 -->
                    <div class="w-12 h-12 rounded-xl bg-emerald-950/80 border-2 border-emerald-500 flex items-center justify-center font-mono font-bold text-emerald-400 text-xs shadow-md">300</div>
                    <!-- Hidden Stone 301 -->
                    <button id="stone301" onclick="revealStone('stone301', '301')" class="w-12 h-12 rounded-xl bg-amber-500/20 border-2 border-dashed border-amber-500 flex items-center justify-center font-mono font-bold text-amber-300 text-xs hover:bg-amber-500/30 transition">
                        ❓
                    </button>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">302</div>
                    <div class="w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-slate-200 text-xs">303</div>
                </div>
            </div>
        </div>

        <div id="pathNotice" class="mt-3 text-xs text-emerald-300 font-semibold bg-emerald-950/40 px-3 py-1.5 rounded-lg border border-emerald-800/40 text-center w-full font-mono">
            👣 Click the question mark stones (❓) to uncover the hidden numerals!
        </div>
    </div>
</div>

<script>
window.revealStone = function(btnId, val) {
    const btn = document.getElementById(btnId);
    const notice = document.getElementById(pathNotice);
    if (!btn) return;

    btn.innerText = val;
    btn.className = "w-12 h-12 rounded-xl bg-emerald-600 border border-emerald-500 flex items-center justify-center font-mono font-bold text-white text-xs shadow-lg transition-all scale-105";
    btn.disabled = true;

    const noticeEl = document.getElementById('pathNotice');
    if (noticeEl) {
        noticeEl.innerText = "✨ Stone restored! Number " + val + " fits perfectly into the consecutive sequence.";
    }
};
</script>
"""

# 4. Matchstick Bundle Sentences
simulators_part1['sim_matchstick_bundle_sentences'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 4</span>
            <h3 class="text-lg font-bold text-slate-100">Matchstick Sentence Translator</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">Concrete to Verbal</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Adjust hundreds bundles, tens bundles, and loose sticks to generate expressive mathematical sentences!
    </p>

    <!-- Bundles Display Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="grid grid-cols-3 gap-3 w-full text-center">
            <!-- Hundreds Column -->
            <div class="bg-slate-900/80 border border-amber-600/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-amber-400 block mb-1">Hundreds Bundles (100)</span>
                <span id="hCountTxt" class="text-2xl font-black text-amber-300 font-mono">2</span>
                <span class="text-[11px] text-slate-400 block">📦📦 (200)</span>
            </div>

            <!-- Tens Column -->
            <div class="bg-slate-900/80 border border-cyan-600/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-cyan-400 block mb-1">Tens Bundles (10)</span>
                <span id="tCountTxt" class="text-2xl font-black text-cyan-300 font-mono">3</span>
                <span class="text-[11px] text-slate-400 block">🪵🪵🪵 (30)</span>
            </div>

            <!-- Ones Column -->
            <div class="bg-slate-900/80 border border-emerald-600/40 rounded-xl p-2.5">
                <span class="text-[10px] font-bold uppercase text-emerald-400 block mb-1">Loose Sticks (1)</span>
                <span id="oCountTxt" class="text-2xl font-black text-emerald-300 font-mono">5</span>
                <span class="text-[11px] text-slate-400 block">🥢🥢🥢🥢🥢 (5)</span>
            </div>
        </div>

        <div id="matchstickSentenceBox" class="mt-3 text-xs text-cyan-300 font-semibold bg-cyan-950/40 px-3 py-2 rounded-lg border border-cyan-800/40 text-center w-full space-y-1">
            <div class="text-sm font-bold text-white font-mono">Total Value: 235</div>
            <div class="text-slate-300">📝 Verbal Sentence: "200 and 35 more"</div>
            <div class="text-amber-400">🎯 Relative Landmark: "15 less than 250"</div>
        </div>
    </div>

    <!-- Preset Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setMatchstickSentence(2, 3, 5)" class="px-3 py-2 bg-cyan-600 hover:bg-cyan-500 rounded-xl text-xs font-bold transition">
            1. 235 (200 + 35)
        </button>
        <button onclick="setMatchstickSentence(2, 5, 0)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. 250 (200 + 50)
        </button>
        <button onclick="setMatchstickSentence(2, 9, 5)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            3. 295 (5 less than 300)
        </button>
    </div>
</div>

<script>
window.setMatchstickSentence = function(h, t, o) {
    const hc = document.getElementById('hCountTxt');
    const tc = document.getElementById('tCountTxt');
    const oc = document.getElementById('oCountTxt');
    const box = document.getElementById('matchstickSentenceBox');

    if (!hc || !tc || !oc || !box) return;

    hc.innerText = h;
    tc.innerText = t;
    oc.innerText = o;

    const total = h * 100 + t * 10 + o;
    const moreThan200 = total - 200;
    const diffTo250 = 250 - total;
    const diffTo300 = 300 - total;

    let relLandmark = "";
    if (diffTo250 === 0) {
        relLandmark = "🎯 Exact Landmark: 250 (Twenty-five bundles of 10)";
    } else if (diffTo250 > 0) {
        relLandmark = "🎯 Relative Landmark: " + diffTo250 + " less than 250";
    } else {
        relLandmark = "🎯 Relative Landmark: " + diffTo300 + " less than 300";
    }

    box.innerHTML = `
        <div class="text-sm font-bold text-white font-mono">Total Value: ${total}</div>
        <div class="text-slate-300">📝 Verbal Sentence: "200 and ${moreThan200} more"</div>
        <div class="text-amber-400">${relLandmark}</div>
    `;
};
</script>
"""

# 5. Extended Number Line
simulators_part1['sim_extended_number_line'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 5</span>
            <h3 class="text-lg font-bold text-slate-100">Extended Number Line (0 to 350)</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-500/20 text-indigo-300 font-semibold border border-indigo-500/30">Geometric Spacing</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Drag the interactive slider along this calibrated highway from 0 to 350 to inspect landmark towers and relative distances!
    </p>

    <!-- Number Line SVG Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="extLineSvg" viewBox="0 0 360 140" class="w-full max-w-[420px] h-36 bg-slate-900 rounded-lg shadow-inner">
            <!-- Main Highway Axis -->
            <line x1="30" y1="70" x2="330" y2="70" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>

            <!-- Major Landmark Ticks (0, 100, 200, 300, 350) -->
            <!-- 0 (x=30) -->
            <line x1="30" y1="55" x2="30" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="30" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">0</text>

            <!-- 100 (x=115) -->
            <line x1="115" y1="55" x2="115" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="115" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">100</text>

            <!-- 200 (x=200) -->
            <line x1="200" y1="55" x2="200" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="200" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">200</text>

            <!-- 250 Midpoint (x=243) -->
            <line x1="243" y1="60" x2="243" y2="80" stroke="#f59e0b" stroke-width="2"/>
            <text x="243" y="50" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">250</text>

            <!-- 300 (x=286) -->
            <line x1="286" y1="55" x2="286" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="286" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">300</text>

            <!-- 350 (x=330) -->
            <line x1="330" y1="55" x2="330" y2="85" stroke="#94a3b8" stroke-width="3"/>
            <text x="330" y="102" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">350</text>

            <!-- Dynamic Pin Indicator -->
            <g id="extPinGroup" transform="translate(260, 0)">
                <circle cx="0" cy="70" r="7" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
                <polygon points="0,55 -6,45 6,45" fill="#38bdf8"/>
                <text id="extPinText" x="0" y="40" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">275</text>
            </g>
        </svg>

        <div id="extLineBanner" class="mt-2 text-xs text-indigo-300 font-semibold bg-indigo-950/40 px-3 py-1.5 rounded-lg border border-indigo-800/40 text-center w-full font-mono">
            📍 Value: 275 | Exactly midway between 250 and 300!
        </div>
    </div>

    <!-- Slider -->
    <div class="space-y-1 pt-1">
        <div class="flex justify-between text-xs font-mono">
            <span class="text-slate-400">Position on Number Line:</span>
            <span id="extSliderLabel" class="text-sky-400 font-bold">275 Units</span>
        </div>
        <input type="range" min="0" max="350" value="275" id="extLineRange" oninput="updateExtLine(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-sky-500">
    </div>
</div>

<script>
window.updateExtLine = function(val) {
    const n = parseInt(val);
    const pin = document.getElementById('extPinGroup');
    const txt = document.getElementById('extPinText');
    const banner = document.getElementById('extLineBanner');
    const lbl = document.getElementById('extSliderLabel');

    if (!pin || !txt || !banner) return;

    lbl.innerText = n + " Units";
    txt.innerText = n.toString();

    // Mapping 0..350 to x: 30..330 (span = 300)
    const x = 30 + (n / 350) * 300;
    pin.setAttribute('transform', 'translate(' + x.toFixed(1) + ', 0)');

    let rel = "";
    if (n === 250) rel = "Exact Midpoint between 200 and 300!";
    else if (n === 275) rel = "Midway between 250 and 300!";
    else if (n === 290) rel = "Much closer to 300 (only 10 away!) than to 200.";
    else if (n >= 200 && n <= 300) rel = "In the third century (200s block).";
    else if (n > 300) rel = "In the fourth century (300s block).";
    else rel = "Earlier century benchmark.";

    banner.innerText = "📍 Value: " + n + " | " + rel;
};
</script>
"""

# 6. Number Slider Hops
simulators_part1['sim_number_slider_hops'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 6</span>
            <h3 class="text-lg font-bold text-slate-100">Number Slider Rapid Hops</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-teal-500/20 text-teal-300 font-semibold border border-teal-500/30">±1, ±10, ±20 Strides</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Execute controlled mental arithmetic jumps from 240 by ones, tens, and twenties along the track!
    </p>

    <!-- Hop Track Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div class="text-center py-2">
            <span class="text-xs text-slate-400 uppercase tracking-widest block mb-1">Current Slider Position</span>
            <span id="sliderHopDisplay" class="text-5xl font-black text-teal-400 font-mono tracking-wider transition-all duration-200">240</span>
        </div>

        <div id="hopHistoryLog" class="text-[11px] font-mono text-slate-400 mt-1">
            Baseline: 240
        </div>

        <div id="hopMathNotice" class="mt-3 text-xs text-teal-300 font-semibold bg-teal-950/40 px-3 py-1.5 rounded-lg border border-teal-800/40 text-center w-full font-mono">
            🦘 Standing at 240. Click any hop button below to leap forward or backward!
        </div>
    </div>

    <!-- Hop Buttons -->
    <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 pt-1">
        <button onclick="applyHop(-20)" class="px-2 py-1.5 bg-rose-950 hover:bg-rose-900 text-rose-300 border border-rose-800 rounded-lg text-xs font-bold transition">
            -20
        </button>
        <button onclick="applyHop(-10)" class="px-2 py-1.5 bg-rose-950 hover:bg-rose-900 text-rose-300 border border-rose-800 rounded-lg text-xs font-bold transition">
            -10
        </button>
        <button onclick="applyHop(-1)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg text-xs font-bold transition">
            -1
        </button>
        <button onclick="applyHop(1)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg text-xs font-bold transition">
            +1
        </button>
        <button onclick="applyHop(10)" class="px-2 py-1.5 bg-emerald-950 hover:bg-emerald-900 text-emerald-300 border border-emerald-800 rounded-lg text-xs font-bold transition">
            +10
        </button>
        <button onclick="applyHop(20)" class="px-2 py-1.5 bg-emerald-950 hover:bg-emerald-900 text-emerald-300 border border-emerald-800 rounded-lg text-xs font-bold transition">
            +20
        </button>
    </div>
</div>

<script>
window.hopVal = 240;

window.applyHop = function(delta) {
    const prev = window.hopVal;
    window.hopVal += delta;

    const disp = document.getElementById('sliderHopDisplay');
    const log = document.getElementById('hopHistoryLog');
    const notice = document.getElementById('hopMathNotice');

    if (!disp || !log || !notice) return;

    disp.innerText = window.hopVal;
    const sign = delta > 0 ? "+" + delta : delta.toString();
    log.innerText = prev + " " + sign + " = " + window.hopVal;

    notice.innerText = "🦘 Jumped by " + sign + ": moved from " + prev + " to " + window.hopVal + "!";
};
</script>
"""

# 7. The Flag Game
simulators_part1['sim_the_flag_game'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 7</span>
            <h3 class="text-lg font-bold text-slate-100">The Number Line Flag Game</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Binary Deduction (200-210)</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        A secret mystery number is hidden between 200 and 210. Click numbers to receive Higher/Lower flags and find it!
    </p>

    <!-- Flag Arena Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <!-- Target Number Secret Box -->
        <div class="flex items-center gap-3 mb-2">
            <span class="text-xs text-slate-400">Mystery Target:</span>
            <span id="targetSecretBox" class="px-3 py-1 bg-slate-800 border border-slate-700 rounded-lg font-mono font-bold text-amber-300 text-sm">❓ Hidden</span>
            <button onclick="newFlagGame()" class="text-[11px] px-2 py-0.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-300">New Secret</button>
        </div>

        <!-- 200-210 Interactive Number Bar -->
        <div class="flex flex-wrap gap-1.5 justify-center py-2 w-full max-w-[420px]">
            <button onclick="guessFlagNumber(200)" id="fb-200" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">200</button>
            <button onclick="guessFlagNumber(201)" id="fb-201" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">201</button>
            <button onclick="guessFlagNumber(202)" id="fb-202" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">202</button>
            <button onclick="guessFlagNumber(203)" id="fb-203" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">203</button>
            <button onclick="guessFlagNumber(204)" id="fb-204" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">204</button>
            <button onclick="guessFlagNumber(205)" id="fb-205" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">205</button>
            <button onclick="guessFlagNumber(206)" id="fb-206" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">206</button>
            <button onclick="guessFlagNumber(207)" id="fb-207" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">207</button>
            <button onclick="guessFlagNumber(208)" id="fb-208" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">208</button>
            <button onclick="guessFlagNumber(209)" id="fb-209" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">209</button>
            <button onclick="guessFlagNumber(210)" id="fb-210" class="flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition">210</button>
        </div>

        <div id="flagClueNotice" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            🚩 Make your first guess! (Hint: Try the midpoint 205).
        </div>
    </div>
</div>

<script>
window.secretTarget = 207;

window.newFlagGame = function() {
    window.secretTarget = 200 + Math.floor(Math.random() * 11);
    const box = document.getElementById('targetSecretBox');
    const notice = document.getElementById('flagClueNotice');
    if (box) box.innerText = "❓ Hidden";
    if (notice) notice.innerText = "🚩 New mystery number generated between 200 and 210! Make your guess.";

    const allBtns = document.querySelectorAll('.flag-num-btn');
    allBtns.forEach(b => {
        b.className = "flag-num-btn w-9 h-10 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono text-xs font-bold transition";
        b.disabled = false;
    });
};

window.guessFlagNumber = function(n) {
    const btn = document.getElementById('fb-' + n);
    const notice = document.getElementById('flagClueNotice');
    const box = document.getElementById('targetSecretBox');

    if (n === window.secretTarget) {
        if (btn) btn.className = "flag-num-btn w-9 h-10 rounded-lg bg-emerald-600 font-mono text-xs font-bold text-white shadow-lg animate-bounce";
        if (box) box.innerText = "🎯 " + window.secretTarget;
        if (notice) notice.innerText = "🎉 BINGO! Exactly " + n + "! You found the secret number.";
    } else if (n < window.secretTarget) {
        if (btn) btn.className = "flag-num-btn w-9 h-10 rounded-lg bg-amber-600/50 text-amber-300 border border-amber-500 font-mono text-xs font-bold";
        if (notice) notice.innerText = "🚩 GOLDEN FLAG: HIGHER than " + n + "! (Eliminating numbers ≤ " + n + ").";
    } else {
        if (btn) btn.className = "flag-num-btn w-9 h-10 rounded-lg bg-rose-600/50 text-rose-300 border border-rose-500 font-mono text-xs font-bold";
        if (notice) notice.innerText = "🚩 CRIMSON FLAG: LOWER than " + n + "! (Eliminating numbers ≥ " + n + ").";
    }
};
</script>
"""

# 8. Four Convergence Chain
simulators_part1['sim_four_convergence_chain'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 8</span>
            <h3 class="text-lg font-bold text-slate-100">The Magical Four Convergence Chain</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30">Attractive Fixed Point</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Spell any number, count its letters, and repeat. Watch how every single number in English spirals invariably into FOUR!
    </p>

    <!-- Chain Visualizer Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div id="chainStepsDisplay" class="flex flex-wrap items-center justify-center gap-2 py-3 min-h-[90px] w-full">
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">
                TWO HUNDRED FIFTY (16)
            </div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">
                SIXTEEN (7)
            </div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">
                SEVEN (5)
            </div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">
                FIVE (4)
            </div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-purple-600 border border-purple-400 font-mono text-xs font-bold text-white shadow-lg animate-pulse">
                FOUR (4) 🔄
            </div>
        </div>

        <div id="chainNotice" class="mt-2 text-xs text-purple-300 font-semibold bg-purple-950/40 px-3 py-1.5 rounded-lg border border-purple-800/40 text-center w-full font-mono">
            ✨ Converged! "FOUR" has 4 letters, locking into an unbreakable mathematical loop.
        </div>
    </div>

    <!-- Presets -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="runWordChain('250')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            1. Try 250
        </button>
        <button onclick="runWordChain('300')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. Try 300
        </button>
        <button onclick="runWordChain('45')" class="px-3 py-2 bg-purple-600 hover:bg-purple-500 rounded-xl text-xs font-bold transition">
            3. Try 45
        </button>
    </div>
</div>

<script>
window.runWordChain = function(num) {
    const disp = document.getElementById('chainStepsDisplay');
    const notice = document.getElementById('chainNotice');
    if (!disp) return;

    if (num === '250') {
        disp.innerHTML = `
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">TWO HUNDRED FIFTY (16)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">SIXTEEN (7)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">SEVEN (5)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">FIVE (4)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-purple-600 border border-purple-400 font-mono text-xs font-bold text-white shadow-lg animate-pulse">FOUR (4) 🔄</div>
        `;
        notice.innerText = "✨ Starting at 250: 16 -> 7 -> 5 -> 4 -> 4. Converged to FOUR!";
    } else if (num === '300') {
        disp.innerHTML = `
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">THREE HUNDRED (12)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">TWELVE (6)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">SIX (3)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">THREE (5)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">FIVE (4)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-purple-600 border border-purple-400 font-mono text-xs font-bold text-white shadow-lg animate-pulse">FOUR (4) 🔄</div>
        `;
        notice.innerText = "✨ Starting at 300: 12 -> 6 -> 3 -> 5 -> 4 -> 4. Converged to FOUR!";
    } else if (num === '45') {
        disp.innerHTML = `
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">FORTY FIVE (9)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200">NINE (4)</div>
            <span class="text-slate-500">➔</span>
            <div class="px-3 py-1.5 rounded-lg bg-purple-600 border border-purple-400 font-mono text-xs font-bold text-white shadow-lg animate-pulse">FOUR (4) 🔄</div>
        `;
        notice.innerText = "✨ Starting at 45: 9 -> 4 -> 4. Converged directly to FOUR!";
    }
};
</script>
"""

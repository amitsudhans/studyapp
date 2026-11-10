#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 14: Probability
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: 5 Diamond Cards Without Replacement (Ex 14.1 Q15: Queen Put Aside)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♦️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Cards Without Replacement Lab (Ex 14.1 Q15: 5 → 4)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c14s9-badge">5 Diamonds</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC14S9(0)" id="btn-149-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">1. Start: All 5 Diamonds</button>
        <button onclick="pickC14S9(1)" id="btn-149-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Put Q♦ Aside (4 Left!)</button>
    </div>

    <div class="flex justify-center gap-2 py-1 font-mono text-xs" id="c14s9-cards"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1 text-center" id="c14s9-info"></div>
</div>

<script>
function pickC14S9(step) {
    document.getElementById("btn-149-0").className = step === 0
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-149-1").className = step === 1
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const list = ["10♦", "J♦", "Q♦", "K♦", "A♦"];
    let html = "";
    list.forEach(c => {
        const gone = (step === 1 && c === "Q♦");
        html += `<div class="px-3 py-2 rounded-xl border font-bold ${gone ? "bg-slate-950 border-slate-800 text-slate-600 line-through" : "bg-rose-950/40 border-rose-400 text-rose-200"}">${c}</div>`;
    });
    document.getElementById("c14s9-cards").innerHTML = html;
    document.getElementById("c14s9-badge").textContent = step === 0 ? "5 Cards" : "4 Cards Left";
    document.getElementById("c14s9-info").innerHTML = step === 0
        ? `<div class="text-cyan-300 font-bold">Total = 5 Diamond Cards  ⇒  P(Queen Q♦) = 1 / 5</div>`
        : `<div class="text-emerald-300 font-bold">Total shrank to 4 {10♦, J♦, K♦, A♦}!</div><div class="text-amber-300 font-bold">(a) P(Ace) = 1 / 4   |   (b) P(Queen) = 0 (Impossible!)</div>`;
}
pickC14S9(1);
</script>
"""

# Simulator 10: Marbles (Q9), Piggy Bank Coins (Q10) & Lettered Die (Q19)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏺</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Ex 14.1 Counting Solver: Piggy Bank, Marbles & Lettered Die</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Sum All First!</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC14S10(10)" id="btn-1410-10" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Q10: Piggy Bank</button>
        <button onclick="pickC14S10(9)" id="btn-1410-9" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q9: 17 Marbles</button>
        <button onclick="pickC14S10(19)" id="btn-1410-19" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q19: Letter Die</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c14s10-box"></div>
</div>

<script>
function pickC14S10(q) {
    for (const k of [10, 9, 19]) {
        document.getElementById("btn-1410-" + k).className = k === q
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c14s10-box");
    if (q === 10) {
        box.innerHTML = `<div class="text-amber-300 font-bold">Ex 14.1 Q10: 100 (50p) + 50 (₹1) + 20 (₹2) + 10 (₹5) = 180 Total Coins</div>
            <div class="text-emerald-300 font-bold">• P(50p coin) = 100/180 = 5/9   |   P(Not ₹5 coin) = (180−10)/180 = 17/18!</div>`;
    } else if (q === 9) {
        box.innerHTML = `<div class="text-amber-300 font-bold">Ex 14.1 Q9: 5 Red + 8 White + 4 Green = 17 Marbles</div>
            <div class="text-emerald-300 font-bold">P(Red) = 5/17   |   P(White) = 8/17   |   P(NOT Green) = (5+8)/17 = 13/17!</div>`;
    } else {
        box.innerHTML = `<div class="text-amber-300 font-bold">Ex 14.1 Q19: Six Faces Showing { A, B, C, D, E, A }</div>
            <div class="text-emerald-300 font-bold">Notice A repeats twice! P(A) = 2/6 = 1/3   |   P(D) = 1/6!</div>`;
    }
}
pickC14S10(10);
</script>
"""

# Simulator 11: Interactive Spinner Wheel (1–8) & Defective Lot Shrinking (Q12, Q16, Q17)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎡</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">1–8 Number Spinner & Defective Lot Lab (Ex 14.1 Q12, Q16, Q17)</h3>
        </div>
        <button onclick="spinArrowS11()" class="text-xs bg-cyan-600 hover:bg-cyan-500 text-white font-bold px-3 py-1 rounded-full">Spin Arrow!</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 space-y-1">
            <div class="text-cyan-300 font-bold" id="c14s11-spin">Click Spin Arrow! (Equally likely {1..8})</div>
            <div class="text-slate-300">• P(=8) = 1/8   • P(Odd) = 4/8 = 1/2</div>
            <div class="text-emerald-300 font-bold">• P(&gt;2) = 6/8 = 3/4   • P(&lt;9) = 8/8 = 1!</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-amber-800 space-y-1">
            <div class="text-amber-300 font-bold">Defective Inspection (Q16 & Q17):</div>
            <div class="text-slate-300">• Q16 Pens: 132 good / (132+12) = 11/12</div>
            <div class="text-emerald-300 font-bold">• Q17 Bulbs (1 good removed): 15/19!</div>
        </div>
    </div>
</div>

<script>
function spinArrowS11() {
    const val = Math.floor(Math.random() * 8) + 1;
    document.getElementById("c14s11-spin").textContent = `Arrow stopped on: [ ${val} ]  (${val % 2 === 1 ? "Odd" : "Even"}, ${val > 2 ? "> 2" : "≤ 2"})`;
}
</script>
"""

# Simulator 12: Box Discs (1–90, Q18) & 53 Sundays Leap vs Non-Leap Year Switcher
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📅</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">90 Numbered Discs (Q18) & 53 Sundays Calendar Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">HOTS Classic</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC14S12(0)" id="btn-1412-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Ex 14.1 Q18: 90 Discs</button>
        <button onclick="pickC14S12(1)" id="btn-1412-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Calendar: 53 Sundays</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c14s12-box"></div>
</div>

<script>
function pickC14S12(m) {
    document.getElementById("btn-1412-0").className = m === 0
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1412-1").className = m === 1
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c14s12-box");
    if (m === 0) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">90 Discs Numbered 1 to 90 (Watch 1..9 are Single-Digit!)</div>
            <div class="text-slate-200">(i) Two-digit (10..90): (90 − 9) / 90 = 81/90 = 9/10</div>
            <div class="text-amber-300">(ii) Perfect Squares {1,4,9,16,25,36,49,64,81}: 9/90 = 1/10</div>
            <div class="text-emerald-300 font-bold">(iii) Divisible by 5 (90 ÷ 5 = 18): 18/90 = 1/5!</div>`;
    } else {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ordinary Year (365 days = 52 weeks + 1 extra day):</div>
            <div class="text-amber-300">P(53 Sundays in Ordinary Year) = 1 / 7</div>
            <div class="text-cyan-300 font-bold mt-1">Leap Year (366 days = 52 weeks + 2 consecutive days):</div>
            <div class="text-emerald-300 font-bold">Pairs {(Sat,Sun), (Sun,Mon)} out of 7 pairs ⇒ P(53 Sundays in Leap Year) = 2 / 7!</div>`;
    }
}
pickC14S12(0);
</script>
"""

# Simulator 13: Continuous Geometric Probability SVG Lab (Ex 14.1 Q20 & Ex 11)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Continuous Geometric Probability Lab (Area Ratio)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Favourable Area / Total Area</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC14S13(0)" id="btn-1413-0" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs">Q20: Circle in 3×2 Rect (π/24)</button>
        <button onclick="pickC14S13(1)" id="btn-1413-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Ex 11: Lake Forest (5/27)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 180 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c14s13-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c14s13-info"></div>
    </div>
</div>

<script>
function pickC14S13(m) {
    document.getElementById("btn-1413-0").className = m === 0
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1413-1").className = m === 1
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const svg = document.getElementById("c14s13-svg");
    const info = document.getElementById("c14s13-info");
    if (m === 0) {
        svg.innerHTML = `<rect x="20" y="20" width="140" height="80" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="90" cy="60" r="20" fill="rgba(16,185,129,0.55)" stroke="#34d399" stroke-width="2"/>
            <text x="90" y="112" fill="#cbd5e1" font-size="9" text-anchor="middle">3 m × 2 m, Circle d = 1 m (r = 0.5 m)</text>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Rectangle = 3 × 2 = 6 m²</div>
            <div class="text-slate-200">Circle = π(0.5)² = π/4 m²</div>
            <div class="text-emerald-300 font-bold text-sm">P(Inside Circle) = (π/4)/6 = π/24!</div>`;
    } else {
        svg.innerHTML = `<rect x="20" y="18" width="140" height="80" fill="rgba(22,163,74,0.22)" stroke="#4ade80" stroke-width="2"/>
            <rect x="113" y="18" width="47" height="44" fill="rgba(56,189,248,0.55)" stroke="#38bdf8" stroke-width="2"/>
            <text x="136" y="43" fill="#e0f2fe" font-size="9" text-anchor="middle">Lake</text>`;
        info.innerHTML = `<div class="text-emerald-300 font-bold">Forest = 9 × 4.5 = 40.5 km²</div>
            <div class="text-cyan-300">Lake = 3 × 2.5 = 7.5 km²</div>
            <div class="text-amber-300 font-bold text-sm">P(Lake) = 7.5 / 40.5 = 5 / 27!</div>`;
    }
}
pickC14S13(0);
</script>
"""

# Simulator 14: Algebraic Missing Balls Slider (x Black in 12 + 6 More Doubles Odds!)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔮</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Algebraic Missing Balls Solver (Box of 12 → Add 6 Black!)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c14s14-badge">x = 3 Match!</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Test Initial Black Balls x (Box holds 12 total; adding 6 more makes 18):</span><span class="font-bold text-amber-300" id="c14s14-xv">x = 3</span></div>
        <input type="range" min="1" max="8" step="1" value="3" id="c14s14-x" oninput="updC14S14()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300" id="c14s14-p1"></div>
        <div class="text-amber-300" id="c14s14-p2"></div>
        <div class="text-emerald-300 font-bold" id="c14s14-res"></div>
    </div>
</div>

<script>
function updC14S14() {
    const x = parseInt(document.getElementById("c14s14-x").value, 10);
    const p1 = x / 12;
    const p2 = (x + 6) / 18;
    const ratio = p2 / p1;
    document.getElementById("c14s14-xv").textContent = "x = " + x;
    document.getElementById("c14s14-badge").textContent = x === 3 ? "x = 3 DOUBLED!" : `Ratio = ${ratio.toFixed(2)}×`;
    document.getElementById("c14s14-p1").textContent = `Initial P(Black) = ${x} / 12 = ${p1.toFixed(3)}`;
    document.getElementById("c14s14-p2").textContent = `After +6 Black P(Black) = (${x}+6) / 18 = ${x+6}/18 = ${p2.toFixed(3)}  [= ${ratio.toFixed(2)}× initial!]`;
    document.getElementById("c14s14-res").textContent = x === 3
        ? "✓ EXACT DOUBLING! 0.500 = 2 × 0.250 ⇒ Initial x = 3 black balls!"
        : "Slide to find x where New Probability equals EXACTLY 2× Initial!";
}
updC14S14();
</script>
"""

# Simulator 15: Fallacies & Arguments Auditor (Ex 14.1 Q25 & Gambler's Fallacy)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕵️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Argument Auditor: Ex 14.1 Q25 & Gambler's Fallacy</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Myth Buster</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="pickC14S15(0)" id="btn-1415-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">Myth 1: 2-Coin 1/3</button>
        <button onclick="pickC14S15(1)" id="btn-1415-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Fact 2: Die Odd 1/2</button>
        <button onclick="pickC14S15(2)" id="btn-1415-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Myth 3: Coin Memory</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c14s15-box"></div>
</div>

<script>
function pickC14S15(m) {
    for (let k = 0; k < 3; k++) {
        const bg = k === 1 ? "bg-emerald-600" : "bg-rose-600";
        document.getElementById("btn-1415-" + k).className = k === m
            ? `p-2 rounded-xl ${bg} text-white font-bold text-xs`
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c14s15-box");
    if (m === 0) {
        box.innerHTML = `<div class="text-rose-300 font-bold">✗ INCORRECT ARGUMENT (Ex 14.1 Q25 i):</div>
            <div class="text-slate-200">"2 coins give 2H, 2T, or 1 each ⇒ each = 1/3" ignores that "1 of each" occurs in TWO ways (HT & TH)!</div>
            <div class="text-amber-300 font-bold">True values: P(HH) = 1/4, P(HT/TH) = 2/4 = 1/2, P(TT) = 1/4.</div>`;
    } else if (m === 1) {
        box.innerHTML = `<div class="text-emerald-300 font-bold">✓ TRUE ARGUMENT (Ex 14.1 Q25 ii):</div>
            <div class="text-slate-200">On a fair die, Odd {1,3,5} and Even {2,4,6} are disjoint, equally likely, and hold 3 faces each!</div>
            <div class="text-cyan-300 font-bold">Hence P(Odd) = 3/6 = 1/2 and P(Even) = 3/6 = 1/2 cleanly!</div>`;
    } else {
        box.innerHTML = `<div class="text-rose-300 font-bold">✗ GAMBLER'S FALLACY: "5 Heads in a row means Tail is due!"</div>
            <div class="text-emerald-300 font-bold">Truth: A fair coin has ZERO memory! Next toss ALWAYS keeps P(Tail) = 1/2!</div>`;
    }
}
pickC14S15(0);
</script>
"""

# Simulator 16: Section 14.2 Custom Event Probability & Complement Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Section 14.2 Master Laplace Probability & Complement Calculator</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">0 ≤ P(E) ≤ 1</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Favourable Outcomes m:</span><span class="font-bold text-emerald-300" id="c14s16-mv">12</span></div>
            <input type="range" min="0" max="52" step="1" value="12" id="c14s16-m" oninput="updC14S16()" class="w-full accent-emerald-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Total Outcomes n:</span><span class="font-bold text-cyan-300" id="c14s16-nv">52</span></div>
            <input type="range" min="1" max="52" step="1" value="52" id="c14s16-n" oninput="updC14S16()" class="w-full accent-cyan-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-emerald-800 text-emerald-200 font-bold" id="c14s16-pe"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-amber-800 text-amber-200 font-bold" id="c14s16-pne"></div>
    </div>
</div>

<script>
function updC14S16() {
    let m = parseInt(document.getElementById("c14s16-m").value, 10);
    const n = parseInt(document.getElementById("c14s16-n").value, 10);
    if (m > n) { m = n; document.getElementById("c14s16-m").value = m; }
    document.getElementById("c14s16-mv").textContent = m;
    document.getElementById("c14s16-nv").textContent = n;
    const p = m / n;
    const q = 1 - p;
    const tag = m === 0 ? " (IMPOSSIBLE!)" : (m === n ? " (SURE EVENT!)" : "");
    document.getElementById("c14s16-pe").textContent = `P(E) = ${m}/${n} = ${p.toFixed(4)} (${(p*100).toFixed(1)}%)${tag}`;
    document.getElementById("c14s16-pne").textContent = `P(not E) = 1 − P(E) = ${n-m}/${n} = ${q.toFixed(4)} (${(q*100).toFixed(1)}%)`;
}
updC14S16();
</script>
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 1: Real Numbers
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Real Numbers Intro
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏛️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Real Numbers Roadmap &amp; Positive Integer Pillars</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Chapter 1 Overview</span>
    </div>

    <p class="text-xs text-slate-300">Inspect all four core mathematical tools powered by positive integer properties inside NCERT Class 10 Chapter 1!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectIntroPillar('euclid')" id="btn-ip-euclid" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Euclid HCF</button>
        <button onclick="selectIntroPillar('fta')" id="btn-ip-fta" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Prime Uniqueness</button>
        <button onclick="selectIntroPillar('irrat')" id="btn-ip-irrat" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Irrational Roots</button>
        <button onclick="selectIntroPillar('dec')" id="btn-ip-dec" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Decimal p/q Test</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-sm" id="ip-title">1. Euclid's Division Algorithm (Computing HCF)</h4>
            <span class="px-2 py-0.5 rounded bg-slate-900 text-amber-300 border border-slate-700 font-mono text-[11px]" id="ip-eq">a = bq + r</span>
        </div>
        <p class="text-slate-300 leading-relaxed" id="ip-desc">Uses step-by-step integer division with non-negative remainders (0 ≤ r &lt; b) to lock onto the exact Highest Common Factor (HCF) of any two positive integers swiftly!</p>
    </div>
</div>

<script>
function selectIntroPillar(p) {
    const map = {
        euclid: { t: "1. Euclid's Division Algorithm (Computing HCF)", eq: 'a = bq + r', d: 'Uses step-by-step integer division with non-negative remainders (0 ≤ r < b) to lock onto the exact Highest Common Factor (HCF) of any two positive integers swiftly!' },
        fta: { t: '2. Fundamental Theorem of Arithmetic (Theorem 1.1)', eq: 'N = p₁ᵃ × p₂ᵇ ...', d: 'Every composite number splits into one completely unique multiset of prime factors (apart from order)—governing HCF, LCM, and digit-ending proofs!' },
        irrat: { t: '3. Proving Irrationality (√2, √3, √5)', eq: 'p | a² ⟹ p | a', d: 'Combining unique prime divisibility (Theorem 1.2) with coprime contradiction (Theorem 1.3) proves square roots of primes can never equal p/q!' },
        dec: { t: '4. Decimal Expansion Predictor of Rational p/q', eq: 'q = 2ⁿ × 5ᵐ', d: 'Once p/q is reduced to lowest form, inspecting prime factors of denominator q reveals instantly whether its decimal terminates or repeats periodically!' }
    };
    const d = map[p];
    if (!d) return;
    ['euclid', 'fta', 'irrat', 'dec'].forEach(k => {
        const b = document.getElementById('btn-ip-' + k);
        if (b) {
            b.className = (k === p)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ip-title').textContent = d.t;
    document.getElementById('ip-eq').textContent = d.eq;
    document.getElementById('ip-desc').textContent = d.d;
}
</script>
"""

# Simulator 2: Euclid Division Method
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚙️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Live Euclid's Division HCF Stepper</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Divisibility Chain</span>
    </div>

    <p class="text-xs text-slate-300">Pick an integer pair to watch repeated remainders (a = bq + r) slide cleanly downward until r = 0 reveals the exact HCF!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="runEuclidPair('p1')" id="btn-euc-p1" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">(455, 42)</button>
        <button onclick="runEuclidPair('p2')" id="btn-euc-p2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(225, 135)</button>
        <button onclick="runEuclidPair('p3')" id="btn-euc-p3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(867, 255)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs" id="euc-steps-box">
        <div class="text-slate-300">Step 1: 455 = <span class="text-amber-300 font-bold">42</span> × 10 + <span class="text-cyan-300 font-bold">35</span> (r ≠ 0)</div>
        <div class="text-slate-300">Step 2: 42 = <span class="text-amber-300 font-bold">35</span> × 1 + <span class="text-cyan-300 font-bold">7</span> (r ≠ 0)</div>
        <div class="text-slate-300">Step 3: 35 = <span class="text-emerald-400 font-bold">7</span> × 5 + <span class="text-emerald-400 font-bold">0</span> (r = 0 STOP!)</div>
        <div class="pt-2 border-t border-slate-800 text-emerald-300 font-bold font-sans">Final Non-Zero Divisor: HCF(455, 42) = 7</div>
    </div>
</div>

<script>
function runEuclidPair(key) {
    const data = {
        p1: {
            steps: [
                'Step 1: 455 = <span class="text-amber-300 font-bold">42</span> × 10 + <span class="text-cyan-300 font-bold">35</span> (r ≠ 0)',
                'Step 2: 42 = <span class="text-amber-300 font-bold">35</span> × 1 + <span class="text-cyan-300 font-bold">7</span> (r ≠ 0)',
                'Step 3: 35 = <span class="text-emerald-400 font-bold">7</span> × 5 + <span class="text-emerald-400 font-bold">0</span> (r = 0 STOP!)'
            ],
            res: 'Final Non-Zero Divisor: HCF(455, 42) = 7'
        },
        p2: {
            steps: [
                'Step 1: 225 = <span class="text-amber-300 font-bold">135</span> × 1 + <span class="text-cyan-300 font-bold">90</span> (r ≠ 0)',
                'Step 2: 135 = <span class="text-amber-300 font-bold">90</span> × 1 + <span class="text-cyan-300 font-bold">45</span> (r ≠ 0)',
                'Step 3: 90 = <span class="text-emerald-400 font-bold">45</span> × 2 + <span class="text-emerald-400 font-bold">0</span> (r = 0 STOP!)'
            ],
            res: 'Final Non-Zero Divisor: HCF(225, 135) = 45'
        },
        p3: {
            steps: [
                'Step 1: 867 = <span class="text-amber-300 font-bold">255</span> × 3 + <span class="text-cyan-300 font-bold">102</span> (r ≠ 0)',
                'Step 2: 255 = <span class="text-amber-300 font-bold">102</span> × 2 + <span class="text-cyan-300 font-bold">51</span> (r ≠ 0)',
                'Step 3: 102 = <span class="text-emerald-400 font-bold">51</span> × 2 + <span class="text-emerald-400 font-bold">0</span> (r = 0 STOP!)'
            ],
            res: 'Final Non-Zero Divisor: HCF(867, 255) = 51'
        }
    };
    const item = data[key];
    if (!item) return;
    ['p1', 'p2', 'p3'].forEach(k => {
        const b = document.getElementById('btn-euc-' + k);
        if (b) {
            b.className = (k === key)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const box = document.getElementById('euc-steps-box');
    box.innerHTML = item.steps.map(s => `<div class="text-slate-300">${s}</div>`).join('') +
        `<div class="pt-2 border-t border-slate-800 text-emerald-300 font-bold font-sans">${item.res}</div>`;
}
</script>
"""

# Simulator 3: Decimal Expansion Test
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Rational p/q Decimal Expansion Predictor</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Denominator Test</span>
    </div>

    <p class="text-xs text-slate-300">Click any fraction below to simplify first, inspect denominator q's prime factorization, and predict whether its decimal stops or repeats forever!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectDecFrac('f1')" id="btn-df-f1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">3 / 8</button>
        <button onclick="inspectDecFrac('f2')" id="btn-df-f2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">6 / 15 (Trap!)</button>
        <button onclick="inspectDecFrac('f3')" id="btn-df-f3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">7 / 80</button>
        <button onclick="inspectDecFrac('f4')" id="btn-df-f4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">13 / 21</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="font-mono font-bold text-cyan-300 text-sm" id="df-simp">Simplified Coprime Form: 3 / 8</span>
            <span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-900/70 text-emerald-300 border border-emerald-700" id="df-verdict">TERMINATING (0.375)</span>
        </div>
        <div class="font-mono text-amber-300" id="df-q">Denominator Factoring: q = 8 = 2³ × 5⁰</div>
        <p class="text-slate-300 leading-relaxed" id="df-desc">Because reduced denominator 8 splits strictly into power of 2 (multiply top/bottom by 5³ = 125 -> 375/1000), its decimal terminates cleanly at 0.375!</p>
    </div>
</div>

<script>
function inspectDecFrac(key) {
    const map = {
        f1: { simp: 'Simplified Coprime Form: 3 / 8', verd: 'TERMINATING (0.375)', ok: true, q: 'Denominator Factoring: q = 8 = 2³ × 5⁰', desc: 'Because reduced denominator 8 splits strictly into power of 2 (multiply top/bottom by 5³ = 125 -> 375/1000), its decimal terminates cleanly at 0.375!' },
        f2: { simp: 'Simplified Coprime Form: 6/15 -> 2/5 (Cancel HCF 3!)', verd: 'TERMINATING (0.4)', ok: true, q: 'Denominator Factoring: q = 5 = 2⁰ × 5¹', desc: 'Watch out for unsimplified traps! Although 15 = 3×5 initially had a 3, canceling common 3 yields coprime 2/5 where q = 5 alone, so it terminates cleanly at 0.4!' },
        f3: { simp: 'Simplified Coprime Form: 7 / 80', verd: 'TERMINATING (0.0875)', ok: true, q: 'Denominator Factoring: q = 80 = 2⁴ × 5¹', desc: 'Only primes 2 and 5 divide denominator 80! Maximum exponent 4 gives exact 4 decimal places: (7 × 5³) / 10⁴ = 875 / 10000 = 0.0875.' },
        f4: { simp: 'Simplified Coprime Form: 13 / 21', verd: 'NON-TERMINATING REPEATING', ok: false, q: 'Denominator Factoring: q = 21 = 3¹ × 7¹', desc: 'Reduced denominator 21 contains primes 3 and 7 besides 2 and 5! Therefore no power of 10 can absorb 21, guaranteeing infinite periodic repeating digits: 0.619047...' }
    };
    const d = map[key];
    if (!d) return;
    ['f1', 'f2', 'f3', 'f4'].forEach(k => {
        const b = document.getElementById('btn-df-' + k);
        if (b) {
            b.className = (k === key)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('df-simp').textContent = d.simp;
    const vb = document.getElementById('df-verdict');
    vb.textContent = d.verd;
    vb.className = d.ok
        ? 'px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-900/70 text-emerald-300 border border-emerald-700'
        : 'px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-rose-900/70 text-rose-300 border border-rose-700';
    document.getElementById('df-q').textContent = d.q;
    document.getElementById('df-desc').textContent = d.desc;
}
</script>
"""

# Simulator 4: Factor Tree Explorer
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌳</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Prime Factor Tree &amp; Gauss Explorer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Carl Friedrich Gauss</span>
    </div>

    <p class="text-xs text-slate-300">Choose a composite integer to split into glowing prime leaves, or read Carl Friedrich Gauss's historic theorem origin!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="showFactorTree('32760')" id="btn-ft-32760" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">32,760</button>
        <button onclick="showFactorTree('140')" id="btn-ft-140" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">140</button>
        <button onclick="showFactorTree('3825')" id="btn-ft-3825" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3,825</button>
        <button onclick="showFactorTree('gauss')" id="btn-ft-gauss" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-amber-700 hover:bg-slate-800">📜 Gauss</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 space-y-2 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="ft-title">Factor Tree of 32,760 (Textbook Showcase)</h4>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-emerald-300 leading-relaxed" id="ft-chain">
            32,760 -> 2 × 16,380 -> 2 × 2 × 8,190 -> 2³ × 4,095 -> 2³ × 3 × 1,365 -> 2³ × 3² × 455 -> 2³ × 3² × 5 × 91 -> 2³ × 3² × 5 × 7 × 13
        </div>
        <p class="text-slate-300" id="ft-note">Every bottom leaf (2, 3, 5, 7, 13) is strictly PRIME and cannot split further!</p>
    </div>
</div>

<script>
function showFactorTree(k) {
    const map = {
        '32760': { t: 'Factor Tree of 32,760 (Textbook Showcase)', c: '32,760 -> 2 × 16,380 -> 2 × 2 × 8,190 -> 2³ × 4,095 -> 2³ × 3 × 1,365 -> 2³ × 3² × 455 -> 2³ × 3² × 5 × 91 -> 2³ × 3² × 5 × 7 × 13', n: 'Every bottom leaf (2, 3, 5, 7, 13) is strictly PRIME and cannot split further!' },
        '140': { t: 'Factor Tree of 140 (Exercise 1.1 Q1)', c: '140 -> 2 × 70 -> 2 × 2 × 35 -> 2² × 5 × 7', n: 'Final prime leaves: {2, 2, 5, 7} -> exponential product 2² × 5 × 7.' },
        '3825': { t: 'Factor Tree of 3,825 (Exercise 1.1 Q1)', c: '3,825 -> 3 × 1,275 -> 3² × 425 -> 3² × 5 × 85 -> 3² × 5² × 17', n: 'Divisibility by 3 and 5 cleanly reveals final prime factors 3² × 5² × 17.' },
        'gauss': { t: "Carl Friedrich Gauss (1777–1855): 'Prince of Mathematicians'", c: 'Masterwork: Disquisitiones Arithmeticae (1801, written at age 21)', n: 'Often ranked beside Archimedes and Newton, Carl Friedrich Gauss published the first rigorous proof of unique prime factorization—now known as the Fundamental Theorem of Arithmetic!' }
    };
    const d = map[k];
    if (!d) return;
    ['32760', '140', '3825', 'gauss'].forEach(x => {
        const b = document.getElementById('btn-ft-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ft-title').textContent = d.t;
    document.getElementById('ft-chain').textContent = d.c;
    document.getElementById('ft-note').textContent = d.n;
}
</script>
"""

# Simulator 5: Fundamental Arithmetic Theorem
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧬</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Theorem 1.1: Order-Independent Prime Uniqueness</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Unique Fingerprint</span>
    </div>

    <p class="text-xs text-slate-300">Test two completely different starting split paths for 60 or 210 to verify Theorem 1.1: identical prime atoms always emerge!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="comparePaths('60')" id="btn-cp-60" class="p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Compare Trees of 60</button>
        <button onclick="comparePaths('210')" id="btn-cp-210" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Compare Trees of 210</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-1">
            <div class="font-bold text-cyan-300">Branching Route A (Smallest First)</div>
            <div class="font-mono text-slate-200" id="cp-route-a">60 = 2 × 30 = 2 × 2 × 15 = 2 × 2 × 3 × 5</div>
        </div>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-1">
            <div class="font-bold text-amber-300">Branching Route B (Random Split)</div>
            <div class="font-mono text-slate-200" id="cp-route-b">60 = 6 × 10 = (3 × 2) × (5 × 2) = 3 × 5 × 2 × 2</div>
        </div>
    </div>

    <div class="bg-emerald-950/50 p-3 rounded-xl border border-emerald-700/60 text-xs text-emerald-300 font-bold text-center" id="cp-summary">
        Ascending Canonical Fingerprint: 60 = 2² × 3 × 5 (100% Identical Multiset!)
    </div>
</div>

<script>
function comparePaths(num) {
    const map = {
        '60': { a: '60 = 2 × 30 = 2 × 2 × 15 = 2 × 2 × 3 × 5', b: '60 = 6 × 10 = (3 × 2) × (5 × 2) = 3 × 5 × 2 × 2', s: 'Ascending Canonical Fingerprint: 60 = 2² × 3 × 5 (100% Identical Multiset!)' },
        '210': { a: '210 = 2 × 105 = 2 × 3 × 35 = 2 × 3 × 5 × 7', b: '210 = 10 × 21 = (5 × 2) × (7 × 3) = 5 × 7 × 2 × 3', s: 'Ascending Canonical Fingerprint: 210 = 2 × 3 × 5 × 7 (100% Identical Multiset!)' }
    };
    const d = map[num];
    if (!d) return;
    ['60', '210'].forEach(k => {
        const b = document.getElementById('btn-cp-' + k);
        if (b) {
            b.className = (k === num)
                ? 'p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('cp-route-a').textContent = d.a;
    document.getElementById('cp-route-b').textContent = d.b;
    document.getElementById('cp-summary').textContent = d.s;
}
</script>
"""

# Simulator 6: Zero Ending Check
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">0️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Can 4ⁿ or 6ⁿ End With Zero? Live Power Checker</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Uniqueness Proof</span>
    </div>

    <p class="text-xs text-slate-300">Pick base (4ⁿ, 6ⁿ, or 10ⁿ) and exponent n to inspect values, trailing digits, and prime factors needed for digit 0!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="checkZeroEnd('four')" id="btn-ze-four" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Test 4ⁿ = 2²ⁿ</button>
        <button onclick="checkZeroEnd('six')" id="btn-ze-six" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test 6ⁿ = 2ⁿ·3ⁿ</button>
        <button onclick="checkZeroEnd('ten')" id="btn-ze-ten" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test 10ⁿ = 2ⁿ·5ⁿ</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold" id="ze-vals">n=1: 4 | n=2: 16 | n=3: 64 | n=4: 256 | n=5: 1024</div>
        <div class="font-mono text-cyan-300" id="ze-primes">Unique Prime Factors Present: { 2 } ONLY — Missing Prime: 5!</div>
        <p class="text-slate-300 leading-relaxed" id="ze-why">Ending in 0 requires divisibility by 10 = 2 × 5. Since uniqueness guarantees ONLY prime 2 divides 4ⁿ = 2²ⁿ, prime 5 can never occur—so 4ⁿ NEVER ends in 0!</p>
    </div>
</div>

<script>
function checkZeroEnd(base) {
    const map = {
        four: { v: 'n=1: 4 | n=2: 16 | n=3: 64 | n=4: 256 | n=5: 1,024', p: 'Unique Prime Factors Present: { 2 } ONLY — Missing Prime: 5!', w: 'Ending in 0 requires divisibility by 10 = 2 × 5. Since uniqueness guarantees ONLY prime 2 divides 4ⁿ = 2²ⁿ, prime 5 can never occur—so 4ⁿ NEVER ends in 0!' },
        six: { v: 'n=1: 6 | n=2: 36 | n=3: 216 | n=4: 1,296 | n=5: 7,776', p: 'Unique Prime Factors Present: { 2, 3 } ONLY — Missing Prime: 5!', w: 'Notice 6ⁿ always ends in 6! By Theorem 1.1 uniqueness, only primes 2 and 3 divide 6ⁿ = 2ⁿ × 3ⁿ, proving prime 5 is strictly absent—never ending with 0!' },
        ten: { v: 'n=1: 10 | n=2: 100 | n=3: 1,000 | n=4: 10,000', p: 'Unique Prime Factors Present: { 2, 5 } — Both 2 and 5 Present!', w: 'Because both prime 2 AND prime 5 exist inside 10ⁿ = (2 × 5)ⁿ, 10ⁿ ends cleanly with n trailing zeroes for every natural number n!' }
    };
    const d = map[base];
    if (!d) return;
    ['four', 'six', 'ten'].forEach(k => {
        const b = document.getElementById('btn-ze-' + k);
        if (b) {
            b.className = (k === base)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ze-vals').textContent = d.v;
    document.getElementById('ze-primes').textContent = d.p;
    document.getElementById('ze-why').textContent = d.w;
}
</script>
"""

# Simulator 7: HCF And LCM
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Prime HCF &amp; LCM Identity Verifier</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">HCF × LCM = a × b</span>
    </div>

    <p class="text-xs text-slate-300">Select any NCERT pair to compute HCF (smallest common prime powers), LCM (greatest prime powers), and check their exact product balance!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="calcHcfLcm('96_404')" id="btn-hl-96_404" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">(96, 404)</button>
        <button onclick="calcHcfLcm('26_91')" id="btn-hl-26_91" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(26, 91)</button>
        <button onclick="calcHcfLcm('510_92')" id="btn-hl-510_92" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(510, 92)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="hl-fact">96 = 2⁵ × 3¹  |  404 = 2² × 101¹</div>
        <div class="text-amber-300" id="hl-res">HCF (min common) = 2² = 4  |  LCM (max all) = 2⁵ × 3 × 101 = 9,696</div>
        <div class="pt-2 border-t border-slate-800 text-emerald-400 font-bold" id="hl-check">Verify: 4 × 9,696 = 38,784  ≡  96 × 404 = 38,784 ✅</div>
    </div>
</div>

<script>
function calcHcfLcm(k) {
    const map = {
        '96_404': { f: '96 = 2⁵ × 3¹  |  404 = 2² × 101¹', r: 'HCF (min common) = 2² = 4  |  LCM (max all) = 2⁵ × 3 × 101 = 9,696', c: 'Verify: 4 × 9,696 = 38,784  ≡  96 × 404 = 38,784 ✅' },
        '26_91': { f: '26 = 2¹ × 13¹  |  91 = 7¹ × 13¹', r: 'HCF (min common) = 13¹ = 13  |  LCM (max all) = 2 × 7 × 13 = 182', c: 'Verify: 13 × 182 = 2,366  ≡  26 × 91 = 2,366 ✅' },
        '510_92': { f: '510 = 2 × 3 × 5 × 17  |  92 = 2² × 23', r: 'HCF (min common) = 2¹ = 2  |  LCM (max all) = 2² × 3 × 5 × 17 × 23 = 23,460', c: 'Verify: 2 × 23,460 = 46,920  ≡  510 × 92 = 46,920 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['96_404', '26_91', '510_92'].forEach(x => {
        const b = document.getElementById('btn-hl-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('hl-fact').textContent = d.f;
    document.getElementById('hl-res').textContent = d.r;
    document.getElementById('hl-check').textContent = d.c;
}
</script>
"""

# Simulator 8: Composite Number Proof
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧩</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Exercise 1.1 Composite Proof Factor Extractor</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Factoring Proof</span>
    </div>

    <p class="text-xs text-slate-300">Watch both Exercise 1.1 composite sums reveal hidden divisors instantly without heavy long multiplication!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showCompositeProof('ex1')" id="btn-cpex-ex1" class="p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">7×11×13 + 13</button>
        <button onclick="showCompositeProof('ex2')" id="btn-cpex-ex2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">7×6×5×4×3×2×1 + 5</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold" id="cpex-step1">Step 1 (Spot Shared Factor 13): (7 × 11 × 13) + (1 × 13)</div>
        <div class="font-mono text-cyan-300 font-bold" id="cpex-step2">Step 2 (Factor Out Common 13): = 13 × (7 × 11 + 1) = 13 × 78 = 2 × 3 × 13²</div>
        <p class="text-emerald-300 font-semibold" id="cpex-why">Conclusion: Because it writes cleanly as a product of multiple integers &gt; 1 (factors 13, 2, 3, 78 besides 1 and itself), it is strictly COMPOSITE!</p>
    </div>
</div>

<script>
function showCompositeProof(k) {
    const map = {
        ex1: { s1: 'Step 1 (Spot Shared Factor 13): (7 × 11 × 13) + (1 × 13)', s2: 'Step 2 (Factor Out Common 13): = 13 × (7 × 11 + 1) = 13 × 78 = 2 × 3 × 13²', w: 'Conclusion: Because it writes cleanly as a product of multiple integers > 1 (factors 13, 2, 3, 78 besides 1 and itself), it is strictly COMPOSITE!' },
        ex2: { s1: 'Step 1 (Spot Shared Factor 5): (7 × 6 × 5 × 4 × 3 × 2 × 1) + (1 × 5)', s2: 'Step 2 (Factor Out Common 5): = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1) = 5 × 1,009', w: 'Conclusion: Expressed directly as product 5 × 1,009 where both factors > 1! Having divisors 5 and 1,009 besides 1 and itself proves it is COMPOSITE!' }
    };
    const d = map[k];
    if (!d) return;
    ['ex1', 'ex2'].forEach(x => {
        const b = document.getElementById('btn-cpex-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('cpex-step1').textContent = d.s1;
    document.getElementById('cpex-step2').textContent = d.s2;
    document.getElementById('cpex-why').textContent = d.w;
}
</script>
"""

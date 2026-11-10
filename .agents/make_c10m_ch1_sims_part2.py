#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 1: Real Numbers
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Circular Track Meeting
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏃</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Circular Sports Track Simulator (LCM Meeting Time)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="trk-time-badge">t = 0 min</span>
    </div>

    <p class="text-xs text-slate-300">Runner A (cyan, 18 min/lap) and Runner B (amber, 12 min/lap) start together! Advance time by 6-minute steps to catch their exact reunion!</p>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="setTrackTime(0)" id="btn-tk-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">t = 0m</button>
        <button onclick="setTrackTime(12)" id="btn-tk-12" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">t = 12m</button>
        <button onclick="setTrackTime(18)" id="btn-tk-18" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">t = 18m</button>
        <button onclick="setTrackTime(36)" id="btn-tk-36" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-amber-700 hover:bg-slate-800">t = 36m (LCM!)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 175" class="w-full h-auto max-h-[175px] rounded-xl bg-slate-950 border border-slate-800">
            <circle cx="110" cy="88" r="56" fill="none" stroke="#334155" stroke-width="14" />
            <circle cx="110" cy="88" r="56" fill="none" stroke="#64748b" stroke-dasharray="4,4" stroke-width="1.5" />
            <!-- Start Line at Top (110, 32) -->
            <line x1="110" y1="22" x2="110" y2="42" stroke="#22c55e" stroke-width="4" />
            <text x="110" y="16" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">START LINE</text>
            <!-- Runner A (outer r=60) -->
            <circle id="dot-runner-a" cx="110" cy="28" r="7" fill="#38bdf8" stroke="#fff" stroke-width="1.5" />
            <!-- Runner B (inner r=50) -->
            <circle id="dot-runner-b" cx="110" cy="38" r="7" fill="#fbbf24" stroke="#fff" stroke-width="1.5" />
            <text x="110" y="164" fill="#cbd5e1" font-size="9" font-weight="bold" text-anchor="middle" id="trk-svg-lbl">Both poised at START LINE (t = 0 min)!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <div class="font-mono text-cyan-300" id="trk-laps-a">Runner A (18 min/lap): 0.00 laps</div>
            <div class="font-mono text-amber-300" id="trk-laps-b">Runner B (12 min/lap): 0.00 laps</div>
            <p class="text-slate-300 leading-relaxed pt-1" id="trk-desc">Reuniting right on the starting line requires WHOLE integer lap counts for both runners simultaneously—occurring at LCM(18, 12) = 36 minutes!</p>
        </div>
    </div>
</div>

<script>
function setTrackTime(t) {
    const radA = -Math.PI/2 + 2*Math.PI*(t/18);
    const radB = -Math.PI/2 + 2*Math.PI*(t/12);
    const ax = 110 + 61 * Math.cos(radA), ay = 88 + 61 * Math.sin(radA);
    const bx = 110 + 49 * Math.cos(radB), by = 88 + 49 * Math.sin(radB);
    const da = document.getElementById('dot-runner-a');
    const db = document.getElementById('dot-runner-b');
    if (da) { da.setAttribute('cx', ax.toFixed(1)); da.setAttribute('cy', ay.toFixed(1)); }
    if (db) { db.setAttribute('cx', bx.toFixed(1)); db.setAttribute('cy', by.toFixed(1)); }

    [0, 12, 18, 36].forEach(k => {
        const b = document.getElementById('btn-tk-' + k);
        if (b) {
            b.className = (k === t)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('trk-time-badge').textContent = `t = ${t} min`;
    document.getElementById('trk-laps-a').textContent = `Runner A (18 min/lap): ${(t/18).toFixed(2)} laps`;
    document.getElementById('trk-laps-b').textContent = `Runner B (12 min/lap): ${(t/12).toFixed(2)} laps`;
    const msg = {
        0: 'Both poised at START LINE (t = 0 min)!',
        12: 'Runner B finishes Lap 1, yet Runner A sits only 2/3 around!',
        18: 'Runner A finishes Lap 1, yet Runner B sits halfway through Lap 2!',
        36: 'REUNION! Runner A = 2.00 laps & Runner B = 3.00 laps at START!'
    };
    document.getElementById('trk-svg-lbl').textContent = msg[t];
}
</script>
"""

# Simulator 10: Theorem One Two
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔑</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Theorem 1.2 Tester: Prime vs. Composite Divisors</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">p | a² ⟹ p | a</span>
    </div>

    <p class="text-xs text-slate-300">Test prime divisors vs. the famous composite trap (p = 4 dividing 6² = 36) to see why primality is essential in Theorem 1.2!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testThm12('p2')" id="btn-t12-p2" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Prime p=2 (a=6)</button>
        <button onclick="testThm12('p3')" id="btn-t12-p3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Prime p=3 (a=12)</button>
        <button onclick="testThm12('c4')" id="btn-t12-c4" class="p-2.5 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">Trap: 4 | 6²</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold" id="t12-math">a = 6 = 2 × 3  ⟹  a² = 36 = 2² × 3²</div>
        <p class="text-slate-300 leading-relaxed" id="t12-why">Since prime 2 divides a² = 36 cleanly, uniqueness forbids brand-new primes from appearing in a²—so 2 MUST appear inside a = 6 itself (2 | 6 ✅)!</p>
    </div>
</div>

<script>
function testThm12(k) {
    const map = {
        p2: { m: 'a = 6 = 2 × 3  ⟹  a² = 36 = 2² × 3²', w: 'Since prime 2 divides a² = 36 cleanly, uniqueness forbids brand-new primes from appearing in a²—so 2 MUST appear inside a = 6 itself (2 | 6 ✅)!' },
        p3: { m: 'a = 12 = 2² × 3  ⟹  a² = 144 = 2⁴ × 3²', w: 'Prime 3 divides 144 evenly; squaring merely doubles existing prime powers of a, guaranteeing prime 3 divides a = 12 as well (3 | 12 ✅)!' },
        c4: { m: 'TRAP! Composite p = 4 divides 6² = 36 (36 ÷ 4 = 9)... YET 4 ∤ 6!', w: 'Why? Composite 4 = 2 × 2 grabs ONE factor 2 from the first copy of 6 and the SECOND 2 from the other copy of 6! Hence Theorem 1.2 holds strictly for PRIME divisors p!' }
    };
    const d = map[k];
    if (!d) return;
    ['p2', 'p3', 'c4'].forEach(x => {
        const b = document.getElementById('btn-t12-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('t12-math').textContent = d.m;
    document.getElementById('t12-why').textContent = d.w;
}
</script>
"""

# Simulator 11: Proving Root Two
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💥</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Theorem 1.3 Stepper: Contradiction Proof of √2</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">4 Logic Steps</span>
    </div>

    <p class="text-xs text-slate-300">Walk step by step through Euclid's classic 4-line logical contradiction proving √2 can NEVER equal any integer ratio a/b!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="stepRoot2(1)" id="btn-r2-1" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">1. Coprime Setup</button>
        <button onclick="stepRoot2(2)" id="btn-r2-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. 2 Divides a</button>
        <button onclick="stepRoot2(3)" id="btn-r2-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. 2 Divides b</button>
        <button onclick="stepRoot2(4)" id="btn-r2-4" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">4. Contradiction!</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold" id="r2-eq">Assume √2 = a / b  where HCF(a, b) = 1 (coprime), b ≠ 0</div>
        <p class="text-slate-300 leading-relaxed" id="r2-note">First suppose √2 IS rational. By dividing top and bottom by common factors, write √2 = a/b cleanly in lowest coprime form so a and b share NO common factor > 1!</p>
    </div>
</div>

<script>
function stepRoot2(n) {
    const map = {
        1: { e: 'Assume √2 = a / b  where HCF(a, b) = 1 (coprime), b ≠ 0', n: 'First suppose √2 IS rational. By dividing top and bottom by common factors, write √2 = a/b cleanly in lowest coprime form so a and b share NO common factor > 1!' },
        2: { e: 'b√2 = a  ⟹  2b² = a²  ⟹  2 divides a²  ⟹  2 divides a (Thm 1.2)', n: 'Squaring both sides gives 2b² = a². Thus prime 2 divides a²; by Theorem 1.2, prime 2 MUST divide a! So we write a = 2c for some integer c.' },
        3: { e: '2b² = (2c)² = 4c²  ⟹  b² = 2c²  ⟹  2 divides b²  ⟹  2 divides b', n: 'Substituting a = 2c yields 2b² = 4c², which simplifies to b² = 2c². Immediately prime 2 divides b²—and by Theorem 1.2, prime 2 MUST divide b as well!' },
        4: { e: 'CLASH! Both 2 | a AND 2 | b  ⟹  HCF(a, b) ≥ 2  ≠  1!  ∴ √2 is IRRATIONAL!', n: 'Because 2 divides BOTH a and b, they cannot be coprime! Our false assumption that √2 is rational collapses—proving √2 is irrational forever!' }
    };
    const d = map[n];
    if (!d) return;
    [1, 2, 3, 4].forEach(k => {
        const b = document.getElementById('btn-r2-' + k);
        if (b) {
            b.className = (k === n)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('r2-eq').textContent = d.e;
    document.getElementById('r2-note').textContent = d.n;
}
</script>
"""

# Simulator 12: Roots Three Five
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌱</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">General Prime √p Blueprint Explorer (√3, √5 &amp; √9 Trap)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Generalized Proof</span>
    </div>

    <p class="text-xs text-slate-300">Swap prime p inside Theorem 1.3 to prove √3 and √5 irrational—and spot why composite √9 fails the contradiction!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="genRootProof('p3')" id="btn-rp-p3" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Prove √3</button>
        <button onclick="genRootProof('p5')" id="btn-rp-p5" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Prove √5</button>
        <button onclick="genRootProof('p9')" id="btn-rp-p9" class="p-2.5 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">Test √9 (Trap!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-cyan-300 font-bold" id="rp-chain">3b² = a²  ⟹  3 | a (set a = 3c)  ⟹  3b² = 9c²  ⟹  b² = 3c²  ⟹  3 | b</div>
        <p class="text-slate-300 leading-relaxed" id="rp-verdict">Prime 3 divides BOTH coprime integers a and b—impossible! Therefore √3 is strictly irrational.</p>
    </div>
</div>

<script>
function genRootProof(k) {
    const map = {
        p3: { c: '3b² = a²  ⟹  3 | a (set a = 3c)  ⟹  3b² = 9c²  ⟹  b² = 3c²  ⟹  3 | b', v: 'Prime 3 divides BOTH coprime integers a and b—impossible! Therefore √3 is strictly irrational.' },
        p5: { c: '5b² = a²  ⟹  5 | a (set a = 5c)  ⟹  5b² = 25c²  ⟹  b² = 5c²  ⟹  5 | b', v: 'Prime 5 divides BOTH coprime integers a and b—contradiction! Therefore √5 is strictly irrational (Exercise 1.2 Q1).' },
        p9: { c: '9b² = a²  ⟹  9 | a² DOES NOT force 9 | a! (Check a = 3, b = 1: 9·1² = 3² ✅)', v: 'TRAP CAUGHT! 9 = 3² is composite, so Theorem 1.2 fails! Indeed √9 = 3/1 is cleanly RATIONAL! √p is guaranteed irrational only when p is prime (or non-square).' }
    };
    const d = map[k];
    if (!d) return;
    ['p3', 'p5', 'p9'].forEach(x => {
        const b = document.getElementById('btn-rp-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('rp-chain').textContent = d.c;
    document.getElementById('rp-verdict').textContent = d.v;
}
</script>
"""

# Simulator 13: Combined Irrational Proofs
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚗️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Rational Closure Isolation Lab (5 − √3 &amp; 3√2)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">4-Line Proof</span>
    </div>

    <p class="text-xs text-slate-300">Inspect how isolating the radical cleanly onto one side proves Textbook Examples 10 &amp; 11 in four algebraic lines!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showCombProof('sub')" id="btn-cm-sub" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Prove 5 − √3 Irrational</button>
        <button onclick="showCombProof('mul')" id="btn-cm-mul" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Prove 3√2 Irrational</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-slate-300" id="cm-l1">1. Assume rational: 5 − √3 = a / b  (a, b ∈ ℤ, b ≠ 0)</div>
        <div class="text-cyan-300" id="cm-l2">2. Isolate radical: 5 − a / b = √3  ⟹  (5b − a) / b = √3</div>
        <div class="text-rose-300 font-bold" id="cm-l3">3. Contradiction: (5b − a)/b is RATIONAL, yet √3 is IRRATIONAL!</div>
        <div class="text-emerald-300 font-bold font-sans pt-1" id="cm-l4">4. Conclude: Assumption fails ⟹ 5 − √3 is strictly IRRATIONAL!</div>
    </div>
</div>

<script>
function showCombProof(mode) {
    const map = {
        sub: { l1: '1. Assume rational: 5 − √3 = a / b  (a, b ∈ ℤ, b ≠ 0)', l2: '2. Isolate radical: 5 − a / b = √3  ⟹  (5b − a) / b = √3', l3: '3. Contradiction: (5b − a)/b is RATIONAL, yet √3 is IRRATIONAL!', l4: '4. Conclude: Assumption fails ⟹ 5 − √3 is strictly IRRATIONAL!' },
        mul: { l1: '1. Assume rational: 3√2 = a / b  (a, b ∈ ℤ, b ≠ 0)', l2: '2. Isolate radical: Divide both sides by 3  ⟹  √2 = a / (3b)', l3: '3. Contradiction: a/(3b) is RATIONAL (since a, 3b ∈ ℤ), yet √2 is IRRATIONAL!', l4: '4. Conclude: Assumption fails ⟹ 3√2 is strictly IRRATIONAL!' }
    };
    const d = map[mode];
    if (!d) return;
    ['sub', 'mul'].forEach(k => {
        const b = document.getElementById('btn-cm-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('cm-l1').textContent = d.l1;
    document.getElementById('cm-l2').textContent = d.l2;
    document.getElementById('cm-l3').textContent = d.l3;
    document.getElementById('cm-l4').textContent = d.l4;
}
</script>
"""

# Simulator 14: Mixed Exercise Proofs
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Exercise 1.2 Instant Radical Isolation Deck</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">All 4 Questions</span>
    </div>

    <p class="text-xs text-slate-300">Click each Exercise 1.2 number to reveal the exact algebraic isolation line producing the rational-vs-irrational contradiction!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectEx12('q1')" id="btn-e12-q1" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">3 + 2√5</button>
        <button onclick="inspectEx12('q2')" id="btn-e12-q2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">1 / √2</button>
        <button onclick="inspectEx12('q3')" id="btn-e12-q3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">7√5</button>
        <button onclick="inspectEx12('q4')" id="btn-e12-q4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">6 + √2</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="e12-iso">Isolate √5:  3 + 2√5 = a/b  ⟹  2√5 = (a − 3b)/b  ⟹  √5 = (a − 3b) / (2b)</div>
        <div class="text-emerald-300 font-sans" id="e12-msg">Contradiction: (a − 3b)/(2b) is strictly rational (a, b, 2, 3 ∈ ℤ, 2b ≠ 0), yet √5 is irrational!</div>
    </div>
</div>

<script>
function inspectEx12(q) {
    const map = {
        q1: { iso: 'Isolate √5:  3 + 2√5 = a/b  ⟹  2√5 = (a − 3b)/b  ⟹  √5 = (a − 3b) / (2b)', msg: 'Contradiction: (a − 3b)/(2b) is strictly rational (a, b, 2, 3 ∈ ℤ, 2b ≠ 0), yet √5 is irrational!' },
        q2: { iso: 'Flip Reciprocal:  1 / √2 = a / b  (a ≠ 0, b ≠ 0)  ⟹  √2 = b / a', msg: 'Contradiction: b / a is strictly rational (integers b, a ≠ 0), yet √2 is irrational (Theorem 1.3)!' },
        q3: { iso: 'Divide by 7:  7√5 = a / b  ⟹  √5 = a / (7b)', msg: 'Contradiction: a / (7b) is strictly rational (integers a, 7b ≠ 0), yet √5 is irrational!' },
        q4: { iso: 'Subtract 6:  6 + √2 = a / b  ⟹  √2 = (a − 6b) / b', msg: 'Contradiction: (a − 6b) / b is strictly rational (integers a−6b, b ≠ 0), yet √2 is irrational!' }
    };
    const d = map[q];
    if (!d) return;
    ['q1', 'q2', 'q3', 'q4'].forEach(k => {
        const b = document.getElementById('btn-e12-' + k);
        if (b) {
            b.className = (k === q)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('e12-iso').textContent = d.iso;
    document.getElementById('e12-msg').textContent = d.msg;
}
</script>
"""

# Simulator 15: Three Number Formulas
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Note to Reader: Why HCF×LCM ≠ p·q·r &amp; True 3-Number Formula</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Section 1.4 Note</span>
    </div>

    <p class="text-xs text-slate-300">Verify numerically why 2-number rule fails on triples (6, 72, 120) and (12, 15, 21), and inspect NCERT's exact pairwise formula!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="inspectTriple('t1')" id="btn-tr-t1" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Triple (6, 72, 120)</button>
        <button onclick="inspectTriple('t2')" id="btn-tr-t2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Triple (12, 15, 21)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="text-cyan-300" id="tr-basic">HCF(6, 72, 120) = 6  |  LCM(6, 72, 120) = 360</div>
        <div class="text-rose-300 font-bold" id="tr-clash">❌ HCF × LCM = 6 × 360 = 2,160  ≠  p × q × r = 51,840</div>
        <div class="text-emerald-300" id="tr-exact">✅ True Formula: LCM = [p·q·r·HCF(p,q,r)] / [HCF(6,72)·HCF(72,120)·HCF(6,120)] = (51840 × 6) / (6 × 24 × 6) = 360!</div>
    </div>
</div>

<script>
function inspectTriple(key) {
    const map = {
        t1: {
            b: 'HCF(6, 72, 120) = 6  |  LCM(6, 72, 120) = 360',
            c: '❌ HCF × LCM = 6 × 360 = 2,160  ≠  p × q × r = 51,840',
            e: '✅ True Formula: LCM = [p·q·r·HCF(p,q,r)] / [HCF(6,72)·HCF(72,120)·HCF(6,120)] = (51840 × 6) / (6 × 24 × 6) = 360!'
        },
        t2: {
            b: 'HCF(12, 15, 21) = 3  |  LCM(12, 15, 21) = 420',
            c: '❌ HCF × LCM = 3 × 420 = 1,260  ≠  p × q × r = 3,780',
            e: '✅ True Formula: LCM = (3,780 × 3) / [HCF(12,15)·HCF(15,21)·HCF(12,21)] = 11,340 / (3 × 3 × 3) = 420!'
        }
    };
    const d = map[key];
    if (!d) return;
    ['t1', 't2'].forEach(x => {
        const b = document.getElementById('btn-tr-' + x);
        if (b) {
            b.className = (x === key)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('tr-basic').textContent = d.b;
    document.getElementById('tr-clash').textContent = d.c;
    document.getElementById('tr-exact').textContent = d.e;
}
</script>
"""

# Simulator 16: Chapter One Summary
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎓</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Chapter 1 Master Formula &amp; Theorem Reference Hub</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Revision Sheet</span>
    </div>

    <p class="text-xs text-slate-300">Click any core theorem or law below to review its exact NCERT Chapter 1 statement before tackling Exercises 1.1 &amp; 1.2!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectSummary('t11')" id="btn-sum-t11" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Theorem 1.1</button>
        <button onclick="inspectSummary('t12')" id="btn-sum-t12" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Theorem 1.2</button>
        <button onclick="inspectSummary('t13')" id="btn-sum-t13" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Theorem 1.3</button>
        <button onclick="inspectSummary('note')" id="btn-sum-note" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Note (3 Nums)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="sum-title">Theorem 1.1: Fundamental Theorem of Arithmetic (Gauss)</h4>
        <p class="text-slate-300 leading-relaxed" id="sum-desc">Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur. Anchors 4ⁿ/6ⁿ digit tests &amp; HCF × LCM = a × b.</p>
    </div>
</div>

<script>
function inspectSummary(k) {
    const map = {
        t11: { t: 'Theorem 1.1: Fundamental Theorem of Arithmetic (Gauss)', d: 'Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur. Anchors 4ⁿ/6ⁿ digit tests & HCF × LCM = a × b.' },
        t12: { t: 'Theorem 1.2: Prime Divisibility Lemma', d: 'Let p be a prime number. If p divides a², then p divides a, where a is a positive integer. Strictly fails if p is composite (e.g., 4 | 6² yet 4 ∤ 6).' },
        t13: { t: 'Theorem 1.3: Irrationality of Prime Square Roots (√2, √3, √5)', d: 'Proved via contradiction by writing √p = a/b in lowest coprime form, applying Theorem 1.2 twice to force common factor p dividing both a and b.' },
        note: { t: 'Section 1.4 Note to Reader: Three-Integer Formulas', d: 'Warning: HCF(p, q, r) × LCM(p, q, r) ≠ p · q · r! Exact formulas require dividing by all three pairwise HCFs (or LCMs) respectively.' }
    };
    const d = map[k];
    if (!d) return;
    ['t11', 't12', 't13', 'note'].forEach(x => {
        const b = document.getElementById('btn-sum-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sum-title').textContent = d.t;
    document.getElementById('sum-desc').textContent = d.d;
}
</script>
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 2: Power Play
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Paper Folding Power (0 to 46 folds thickness explorer)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Paper Folding Doubling Simulator (0.001 cm Start)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c2s1-badge">0 Folds</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Number of Folds (a):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c2s1-av">a = 10 folds (2¹⁰ = 1,024×)</span>
        </div>
        <input type="range" min="0" max="46" step="1" value="10" id="c8c2s1-a" oninput="updC8C2S1()" class="w-full accent-amber-400">
        <div class="flex flex-wrap gap-1.5 pt-1">
            <button onclick="setFoldS1(10)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-[11px] font-bold border border-slate-700">10 Folds (1.024 cm)</button>
            <button onclick="setFoldS1(26)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-300 text-[11px] font-bold border border-slate-700">26 Folds (~Burj Khalifa)</button>
            <button onclick="setFoldS1(30)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 text-[11px] font-bold border border-slate-700">30 Folds (10.7 km Jet)</button>
            <button onclick="setFoldS1(46)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-rose-300 text-[11px] font-bold border border-slate-700">46 Folds (Past Moon!)</button>
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8c2s1-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 text-cyan-300 font-bold" id="c8c2s1-layers">Layers: 2¹⁰ = 1,024</div>
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s1-thick">Thickness: 1.024 cm</div>
            <div class="bg-amber-950/30 p-2 rounded-lg border border-amber-700/50 text-amber-200 font-bold" id="c8c2s1-bench">Landmark: Thick Notebook!</div>
        </div>
    </div>
</div>

<script>
function setFoldS1(v) {
    document.getElementById("c8c2s1-a").value = v;
    updC8C2S1();
}
function updC8C2S1() {
    const a = parseInt(document.getElementById("c8c2s1-a").value);
    const factor = Math.pow(2, a);
    const cm = 0.001 * factor;
    let disp = "";
    if (cm < 100) disp = cm.toFixed(3) + " cm";
    else if (cm < 100000) disp = (cm / 100).toFixed(2) + " m";
    else disp = Math.round(cm / 100000).toLocaleString("en-IN") + " km";

    let bench = "Human hair / paper edge";
    if (a >= 46) bench = "Past Moon (~3,84,000 km)!";
    else if (a === 45) bench = "Nearly Moon distance (~3.52 lakh km)!";
    else if (a >= 35) bench = "Deep Earth orbit / Space!";
    else if (a >= 30) bench = "Airplane cruising (~10.7 km)!";
    else if (a >= 26) bench = "Burj Khalifa height (~670+ m)!";
    else if (a >= 20) bench = "10.5 m (3-storey house)!";
    else if (a >= 10) bench = "Book thickness (~1.024 cm)";
    else if (a >= 7) bench = "1.28 mm fingernail";

    document.getElementById("c8c2s1-badge").textContent = a + " Folds";
    document.getElementById("c8c2s1-av").textContent = "a = " + a + " (2^" + a + " layers)";
    document.getElementById("c8c2s1-layers").textContent = "Layers: 2^" + a + " = " + (factor <= 1e12 ? Math.round(factor).toLocaleString("en-IN") : factor.toExponential(2));
    document.getElementById("c8c2s1-thick").textContent = "Thickness: " + disp;
    document.getElementById("c8c2s1-bench").textContent = "Scale: " + bench;

    const pct = Math.max(4, Math.round((a / 46) * 92));
    document.getElementById("c8c2s1-svg").innerHTML = `
        <line x1="20" y1="104" x2="200" y2="104" stroke="#475569" stroke-width="2"/>
        <rect x="35" y="${104 - pct}" width="44" height="${pct}" rx="3" fill="#f59e0b" fill-opacity="0.75" stroke="#fcd34d" stroke-width="1.5"/>
        <text x="57" y="${Math.max(14, 98 - pct)}" text-anchor="middle" fill="#fef3c7" font-size="9" font-weight="bold">2^${a}</text>
        <text x="148" y="34" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Every 10 Folds</text>
        <text x="148" y="48" text-anchor="middle" fill="#22d3ee" font-size="10" font-weight="bold">× 1,024 (2¹⁰)</text>
        <text x="148" y="74" text-anchor="middle" fill="#a7f3d0" font-size="9">${disp}</text>
        <circle cx="195" cy="18" r="9" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
        <text x="195" y="35" text-anchor="middle" fill="#94a3b8" font-size="7">Moon</text>
    `;
}
updC8C2S1();
</script>
"""

# Simulator 2: Base And Exponent (n^a Expander + 2^5 vs 5^2 + Prime Power Factorizer)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔢</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Base vs Exponent Lab &amp; 32,400 Prime Power Breakdown</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c2s2-badge">2⁵ = 32</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base (n):</span><span class="font-bold text-cyan-300" id="c8c2s2-nv">2</span></div>
            <input type="range" min="1" max="9" step="1" value="2" id="c8c2s2-n" oninput="updC8C2S2()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exponent (a):</span><span class="font-bold text-amber-300" id="c8c2s2-av">5</span></div>
            <input type="range" min="1" max="7" step="1" value="5" id="c8c2s2-a" oninput="updC8C2S2()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-300 font-bold" id="c8c2s2-exp">2⁵ = 2 × 2 × 2 × 2 × 2 = 32</div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-300 font-bold" id="c8c2s2-swap">Compare swapped aⁿ: 5² = 25 (2⁵ &gt; 5²!)</div>
        <div class="flex items-center justify-between bg-emerald-950/30 p-2 rounded-lg border border-emerald-700/50">
            <span class="text-emerald-200 font-bold">NCERT Prime Form: 32,400 = 2⁴ × 3⁴ × 5²</span>
            <button onclick="setSwapS2()" class="px-2 py-1 rounded bg-cyan-700 hover:bg-cyan-600 text-white text-[10px] font-bold">Test 2⁵ vs 5²</button>
        </div>
    </div>
</div>

<script>
function setSwapS2() {
    document.getElementById("c8c2s2-n").value = 2;
    document.getElementById("c8c2s2-a").value = 5;
    updC8C2S2();
}
function updC8C2S2() {
    const n = parseInt(document.getElementById("c8c2s2-n").value);
    const a = parseInt(document.getElementById("c8c2s2-a").value);
    const val = Math.pow(n, a);
    const swapVal = Math.pow(a, n);
    const factors = Array(a).fill(n).join(" × ");
    const cmp = val === swapVal ? "=" : (val > swapVal ? ">" : "<");

    document.getElementById("c8c2s2-nv").textContent = n;
    document.getElementById("c8c2s2-av").textContent = a;
    document.getElementById("c8c2s2-badge").textContent = n + "^" + a + " = " + val.toLocaleString("en-IN");
    document.getElementById("c8c2s2-exp").textContent = n + "^" + a + " = " + factors + " = " + val.toLocaleString("en-IN");
    document.getElementById("c8c2s2-swap").textContent = "Swapped check: " + n + "^" + a + " (" + val.toLocaleString("en-IN") + ") " + cmp + " " + a + "^" + n + " (" + swapVal.toLocaleString("en-IN") + ")";
}
updC8C2S2();
</script>
"""

# Simulator 3: Product Base Rule (n^a × n^b = n^(a+b) & Trap Checker)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💎</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Product Rule Lab: nᵃ × nᵇ = nᵃ⁺ᵇ (Stones that Shine)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c2s3-badge">2³ × 2⁴ = 2⁷</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base (n):</span><span class="font-bold text-cyan-300" id="c8c2s3-nv">2</span></div>
            <input type="range" min="2" max="7" step="1" value="2" id="c8c2s3-n" oninput="updC8C2S3()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exp (a):</span><span class="font-bold text-amber-300" id="c8c2s3-av">3</span></div>
            <input type="range" min="1" max="5" step="1" value="3" id="c8c2s3-a" oninput="updC8C2S3()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exp (b):</span><span class="font-bold text-emerald-300" id="c8c2s3-bv">4</span></div>
            <input type="range" min="1" max="5" step="1" value="4" id="c8c2s3-b" oninput="updC8C2S3()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s3-res"></div>
        <div class="p-2 bg-rose-950/30 rounded-lg border border-rose-700/50 text-rose-200 font-bold" id="c8c2s3-trap"></div>
    </div>
</div>

<script>
function updC8C2S3() {
    const n = parseInt(document.getElementById("c8c2s3-n").value);
    const a = parseInt(document.getElementById("c8c2s3-a").value);
    const b = parseInt(document.getElementById("c8c2s3-b").value);
    const p1 = Math.pow(n, a), p2 = Math.pow(n, b);
    const prod = p1 * p2;
    const sumExp = a + b;
    const addVal = p1 + p2;

    document.getElementById("c8c2s3-nv").textContent = n;
    document.getElementById("c8c2s3-av").textContent = a;
    document.getElementById("c8c2s3-bv").textContent = b;
    document.getElementById("c8c2s3-badge").textContent = n + "^" + a + " × " + n + "^" + b + " = " + n + "^" + sumExp;
    document.getElementById("c8c2s3-res").textContent = "Law 1: " + n + "^" + a + " × " + n + "^" + b + " = " + n + "^(" + a + "+" + b + ") = " + n + "^" + sumExp + " = " + prod.toLocaleString("en-IN");
    document.getElementById("c8c2s3-trap").textContent = "Addition Trap Alert: " + n + "^" + a + " + " + n + "^" + b + " = " + p1 + " + " + p2 + " = " + addVal.toLocaleString("en-IN") + " (NOT " + n + "^" + sumExp + "!)";
}
updC8C2S3();
</script>
"""

# Simulator 4: Power Of Power ((n^a)^b = n^(a*b) vs stacked n^(a^b))
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪷</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Power of Power Lab: (nᵃ)ᵇ vs Stacked n^(aᵇ)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c2s4-badge">(2³)² = 2⁶</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base (n):</span><span class="font-bold text-cyan-300" id="c8c2s4-nv">2</span></div>
            <input type="range" min="2" max="5" step="1" value="2" id="c8c2s4-n" oninput="updC8C2S4()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Inner (a):</span><span class="font-bold text-amber-300" id="c8c2s4-av">3</span></div>
            <input type="range" min="2" max="4" step="1" value="3" id="c8c2s4-a" oninput="updC8C2S4()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Outer (b):</span><span class="font-bold text-emerald-300" id="c8c2s4-bv">2</span></div>
            <input type="range" min="2" max="4" step="1" value="2" id="c8c2s4-b" oninput="updC8C2S4()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/50 space-y-1">
            <div class="text-[10px] uppercase text-emerald-400 font-bold">With Parentheses: (nᵃ)ᵇ = n^(a×b)</div>
            <div class="text-emerald-200 font-bold" id="c8c2s4-paren"></div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-amber-700/50 space-y-1">
            <div class="text-[10px] uppercase text-amber-400 font-bold">Stacked Tower: n^(aᵇ) [Top First!]</div>
            <div class="text-amber-200 font-bold" id="c8c2s4-tower"></div>
        </div>
    </div>
</div>

<script>
function updC8C2S4() {
    const n = parseInt(document.getElementById("c8c2s4-n").value);
    const a = parseInt(document.getElementById("c8c2s4-a").value);
    const b = parseInt(document.getElementById("c8c2s4-b").value);
    const multExp = a * b;
    const towerExp = Math.pow(a, b);
    const vParen = Math.pow(n, multExp);
    const vTower = Math.pow(n, towerExp);

    document.getElementById("c8c2s4-nv").textContent = n;
    document.getElementById("c8c2s4-av").textContent = a;
    document.getElementById("c8c2s4-bv").textContent = b;
    document.getElementById("c8c2s4-badge").textContent = "(" + n + "^" + a + ")^" + b + " = " + n + "^" + multExp;
    document.getElementById("c8c2s4-paren").textContent = "(" + n + "^" + a + ")^" + b + " = " + n + "^(" + a + "×" + b + ") = " + n + "^" + multExp + " = " + vParen.toLocaleString("en-IN");
    document.getElementById("c8c2s4-tower").textContent = n + "^(" + a + "^" + b + ") = " + n + "^" + towerExp + " = " + (vTower <= 1e10 ? vTower.toLocaleString("en-IN") : vTower.toExponential(2));
}
updC8C2S4();
</script>
"""

# Simulator 5: Same Exponent Laws (m^a * n^a = (mn)^a & m^a / n^a = (m/n)^a)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Same Exponent Laws: 2ᵃ × 5ᵃ = 10ᵃ Mental Shortcut</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c2s5-badge">a = 4</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">m:</span><span class="font-bold text-cyan-300" id="c8c2s5-mv">2</span></div>
            <input type="range" min="2" max="9" step="1" value="2" id="c8c2s5-m" oninput="updC8C2S5()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">n:</span><span class="font-bold text-amber-300" id="c8c2s5-nv">5</span></div>
            <input type="range" min="2" max="9" step="1" value="5" id="c8c2s5-n" oninput="updC8C2S5()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exp (a):</span><span class="font-bold text-emerald-300" id="c8c2s5-av">4</span></div>
            <input type="range" min="1" max="6" step="1" value="4" id="c8c2s5-a" oninput="updC8C2S5()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-300 font-bold" id="c8c2s5-prod"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s5-quot"></div>
        <div class="flex gap-2">
            <button onclick="setTenS5()" class="px-2.5 py-1 rounded bg-emerald-700 hover:bg-emerald-600 text-white text-[11px] font-bold">2ᵃ × 5ᵃ = 10ᵃ Shortcut</button>
            <button onclick="setOutfitsS5()" class="px-2.5 py-1 rounded bg-indigo-700 hover:bg-indigo-600 text-white text-[11px] font-bold">Shirt-Cap Outfits (2⁴ × 3⁴)</button>
        </div>
    </div>
</div>

<script>
function setTenS5() {
    document.getElementById("c8c2s5-m").value = 2;
    document.getElementById("c8c2s5-n").value = 5;
    document.getElementById("c8c2s5-a").value = 4;
    updC8C2S5();
}
function setOutfitsS5() {
    document.getElementById("c8c2s5-m").value = 2;
    document.getElementById("c8c2s5-n").value = 3;
    document.getElementById("c8c2s5-a").value = 4;
    updC8C2S5();
}
function updC8C2S5() {
    const m = parseInt(document.getElementById("c8c2s5-m").value);
    const n = parseInt(document.getElementById("c8c2s5-n").value);
    const a = parseInt(document.getElementById("c8c2s5-a").value);
    const mn = m * n;
    const pVal = Math.pow(mn, a);
    const qVal = Math.pow(m / n, a);

    document.getElementById("c8c2s5-mv").textContent = m;
    document.getElementById("c8c2s5-nv").textContent = n;
    document.getElementById("c8c2s5-av").textContent = a;
    document.getElementById("c8c2s5-badge").textContent = "a = " + a;
    document.getElementById("c8c2s5-prod").textContent = "Law 3: " + m + "^" + a + " × " + n + "^" + a + " = (" + m + "×" + n + ")^" + a + " = " + mn + "^" + a + " = " + pVal.toLocaleString("en-IN");
    document.getElementById("c8c2s5-quot").textContent = "Law 4: " + m + "^" + a + " ÷ " + n + "^" + a + " = (" + m + "/" + n + ")^" + a + " = " + qVal.toFixed(4);
}
updC8C2S5();
</script>
"""

# Simulator 6: Division Base Rule (n^a / n^b = n^(a-b))
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➗</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Quotient Cancellation Lab: nᵃ ÷ nᵇ = nᵃ⁻ᵇ</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c2s6-badge">5⁷ ÷ 5³ = 5⁴</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base (n):</span><span class="font-bold text-cyan-300" id="c8c2s6-nv">5</span></div>
            <input type="range" min="2" max="9" step="1" value="5" id="c8c2s6-n" oninput="updC8C2S6()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Top (a):</span><span class="font-bold text-amber-300" id="c8c2s6-av">7</span></div>
            <input type="range" min="1" max="8" step="1" value="7" id="c8c2s6-a" oninput="updC8C2S6()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Bot (b):</span><span class="font-bold text-emerald-300" id="c8c2s6-bv">3</span></div>
            <input type="range" min="1" max="8" step="1" value="3" id="c8c2s6-b" oninput="updC8C2S6()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-200" id="c8c2s6-cancel"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s6-res"></div>
        <div class="p-2 bg-cyan-950/30 rounded-lg border border-cyan-700/50 text-cyan-200 font-bold">Multi-Base Challenge: (2⁸ × 3⁵) ÷ (2⁵ × 3²) = 2³ × 3³ = 6³ = 216</div>
    </div>
</div>

<script>
function updC8C2S6() {
    const n = parseInt(document.getElementById("c8c2s6-n").value);
    const a = parseInt(document.getElementById("c8c2s6-a").value);
    const b = parseInt(document.getElementById("c8c2s6-b").value);
    const diff = a - b;
    const cancelCount = Math.min(a, b);
    const val = Math.pow(n, diff);

    document.getElementById("c8c2s6-nv").textContent = n;
    document.getElementById("c8c2s6-av").textContent = a;
    document.getElementById("c8c2s6-bv").textContent = b;
    document.getElementById("c8c2s6-badge").textContent = n + "^" + a + " ÷ " + n + "^" + b + " = " + n + "^(" + diff + ")";
    document.getElementById("c8c2s6-cancel").textContent = "Matching factors canceled top & bottom: " + cancelCount + " pairs of " + n;
    document.getElementById("c8c2s6-res").textContent = n + "^" + a + " ÷ " + n + "^" + b + " = " + n + "^(" + a + " − " + b + ") = " + n + "^(" + diff + ") = " + (diff >= 0 ? Math.round(val).toLocaleString("en-IN") : "1 / " + Math.round(Math.pow(n, -diff)).toLocaleString("en-IN"));
}
updC8C2S6();
</script>
"""

# Simulator 7: Zero Power Law (Step-down Pattern & x^a / x^a = x^0 = 1)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">0️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Zero Power Proof Lab: Why x⁰ = 1 (x ≠ 0)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c2s7-badge">Base: 2</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Any Non-Zero Base (x):</span>
            <span class="font-bold text-cyan-300" id="c8c2s7-xv">x = 2</span>
        </div>
        <input type="range" min="2" max="9" step="1" value="2" id="c8c2s7-x" oninput="updC8C2S7()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-4 gap-2 font-mono text-xs text-center" id="c8c2s7-cards"></div>

    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
        <div class="text-emerald-300 font-bold" id="c8c2s7-proof"></div>
        <div class="text-amber-300 font-bold">Exam Trap Check: (5⁰ + 7⁰) × 9⁰ = (1 + 1) × 1 = 2 (NEVER 0!)</div>
    </div>
</div>

<script>
function updC8C2S7() {
    const x = parseInt(document.getElementById("c8c2s7-x").value);
    document.getElementById("c8c2s7-xv").textContent = "x = " + x;
    document.getElementById("c8c2s7-badge").textContent = "Base: " + x;

    let html = "";
    for (let e = 3; e >= 0; e--) {
        const val = Math.pow(x, e);
        const isZero = e === 0;
        html += `<div class="p-2 rounded-xl border ${isZero ? "bg-emerald-500/25 border-emerald-400 text-emerald-100" : "bg-slate-900 border-slate-800 text-cyan-200"}">
            <div class="font-bold">${x}^${e}</div>
            <div class="text-sm font-black mt-0.5">${val}</div>
            <div class="text-[9px] text-slate-400">${e > 0 ? "÷" + x + " next →" : "Exact 1!"}</div>
        </div>`;
    }
    document.getElementById("c8c2s7-cards").innerHTML = html;
    document.getElementById("c8c2s7-proof").textContent = "Quotient Proof: " + x + "³ ÷ " + x + "³ = (" + Math.pow(x, 3) + "÷" + Math.pow(x, 3) + ") = 1   AND   " + x + "^(3−3) = " + x + "⁰  ⇒  " + x + "⁰ = 1";
}
updC8C2S7();
</script>
"""

# Simulator 8: Negative Exponent Reciprocals (Step Left Past Zero + Fraction Flip)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Negative Exponent Reciprocal Lab: n⁻ᵃ = 1 / nᵃ</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c2s8-badge">Exp: -2</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base (n):</span><span class="font-bold text-cyan-300" id="c8c2s8-nv">10</span></div>
            <input type="range" min="2" max="10" step="1" value="10" id="c8c2s8-n" oninput="updC8C2S8()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exponent (k):</span><span class="font-bold text-rose-300" id="c8c2s8-kv">-2</span></div>
            <input type="range" min="-4" max="3" step="1" value="-2" id="c8c2s8-k" oninput="updC8C2S8()" class="w-full accent-rose-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-300 font-bold" id="c8c2s8-recip"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s8-dec"></div>
        <div class="p-2 bg-amber-950/30 rounded-lg border border-amber-700/50 text-amber-200 font-bold">Fraction Flip Rule: (3/5)⁻² = (5/3)² = 25/9 (NEVER becomes negative!)</div>
    </div>
</div>

<script>
function updC8C2S8() {
    const n = parseInt(document.getElementById("c8c2s8-n").value);
    const k = parseInt(document.getElementById("c8c2s8-k").value);
    const val = Math.pow(n, k);

    document.getElementById("c8c2s8-nv").textContent = n;
    document.getElementById("c8c2s8-kv").textContent = k;
    document.getElementById("c8c2s8-badge").textContent = "Exp: " + k;

    if (k < 0) {
        const pos = Math.pow(n, -k);
        document.getElementById("c8c2s8-recip").textContent = "Reciprocal Form: " + n + "^(" + k + ") = 1 / " + n + "^" + (-k) + " = 1 / " + pos.toLocaleString("en-IN");
        document.getElementById("c8c2s8-dec").textContent = "Decimal Value: " + val + "  (Always POSITIVE because " + n + " > 0!)";
    } else {
        document.getElementById("c8c2s8-recip").textContent = "Standard Power: " + n + "^" + k + " = " + val.toLocaleString("en-IN");
        document.getElementById("c8c2s8-dec").textContent = "Notice: Stepping left divides by " + n + " cleanly across zero!";
    }
}
updC8C2S8();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 7: Proportional Reasoning-1
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Image Scaling Similarity (Tiger Photo Resizing A-E Explorer)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐯</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Digital Tiger Image Resizing: Proportional vs Distorted</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c7s1-badge">Orig: 6×4 cm</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-2.5 rounded-xl border border-slate-800 text-xs">
        <button onclick="setImgS1(0)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Image A (6×4 Orig)</button>
        <button onclick="setImgS1(1)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Image B (12×8 ×2)</button>
        <button onclick="setImgS1(2)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Image C (9×6 ×1.5)</button>
        <button onclick="setImgS1(3)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Image D (12×4 Stretched)</button>
        <button onclick="setImgS1(4)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Image E (8×6 +2 Added)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c7s1-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 font-bold" id="c8c7s1-verdict"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c7s1-ratio"></div>
        </div>
    </div>
</div>

<script>
const tigerImgs = [
    { b: "Orig: 6×4", w: 72, h: 48, ok: true, v: "Original Reference (6 cm × 4 cm)", r: "Aspect W:H = 6 : 4 = 3 : 2" },
    { b: "12×8 (×2 ✓)", w: 120, h: 80, ok: true, v: "PROPORTIONAL ✓ (Scaled both ×2!)", r: "Aspect W:H = 12 : 8 = 3 : 2 (Identical Shape!)" },
    { b: "9×6 (×1.5 ✓)", w: 90, h: 60, ok: true, v: "PROPORTIONAL ✓ (Scaled both ×1.5!)", r: "Aspect W:H = 9 : 6 = 3 : 2 (Identical Shape!)" },
    { b: "12×4 (✗)", w: 130, h: 44, ok: false, v: "DISTORTED ✗ (Elongated horizontally!)", r: "Aspect 12 : 4 = 3 : 1 ≠ 3 : 2 (Height stayed flat!)" },
    { b: "8×6 (+2 ✗)", w: 96, h: 72, ok: false, v: "DISTORTED ✗ (+2 cm added to both!)", r: "Aspect 8 : 6 = 4 : 3 ≠ 3 : 2 (Addition breaks similarity!)" }
];
function setImgS1(i) {
    const t = tigerImgs[i];
    document.getElementById("c8c7s1-badge").textContent = t.b;
    const vEl = document.getElementById("c8c7s1-verdict");
    vEl.className = "p-2 bg-slate-950 rounded-lg border border-slate-800 font-bold " + (t.ok ? "text-emerald-300" : "text-rose-300");
    vEl.textContent = t.v;
    document.getElementById("c8c7s1-ratio").textContent = t.r;
    const x = 110 - t.w / 2, y = 55 - t.h / 2;
    document.getElementById("c8c7s1-svg").innerHTML = `
        <rect x="${x}" y="${y}" width="${t.w}" height="${t.h}" rx="6" fill="${t.ok ? "#f59e0b" : "#f43f5e"}" fill-opacity="0.25" stroke="${t.ok ? "#fbbf24" : "#fb7185"}" stroke-width="2.5"/>
        <ellipse cx="110" cy="55" rx="${(t.w * 0.25).toFixed(1)}" ry="${(t.h * 0.35).toFixed(1)}" fill="${t.ok ? "#fbbf24" : "#fb7185"}" fill-opacity="0.7"/>
    `;
}
setImgS1(1);
</script>
"""

# Simulator 2: Multiplicative vs Additive Change (4×2 Rectangle Comparison)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Multiplicative (×k) vs Additive (+k) Comparison on 4 × 2</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c7s2-badge">k = 3</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Parameter k (2 to 6):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c7s2-kv">k = 3</span>
        </div>
        <input type="range" min="2" max="6" step="1" value="3" id="c8c7s2-k" oninput="updC8C7S2()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/60 space-y-1">
            <div class="text-emerald-400 font-bold">Multiplicative: (4×k) by (2×k)</div>
            <div class="text-emerald-200 font-bold" id="c8c7s2-mul"></div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-rose-700/60 space-y-1">
            <div class="text-rose-400 font-bold">Additive: (4+k) by (2+k)</div>
            <div class="text-rose-200 font-bold" id="c8c7s2-add"></div>
        </div>
    </div>
</div>

<script>
function updC8C7S2() {
    const k = parseInt(document.getElementById("c8c7s2-k").value);
    const mw = 4 * k, mh = 2 * k;
    const aw = 4 + k, ah = 2 + k;
    document.getElementById("c8c7s2-kv").textContent = "k = " + k;
    document.getElementById("c8c7s2-badge").textContent = "k = " + k;
    document.getElementById("c8c7s2-mul").textContent = mw + " × " + mh + " → Ratio = " + (mw / mh).toFixed(2) + " : 1 (Preserved! ✓)";
    document.getElementById("c8c7s2-add").textContent = aw + " × " + ah + " → Ratio = " + (aw / ah).toFixed(2) + " : 1 (Distorted! ✗)";
}
updC8C7S2();
</script>
"""

# Simulator 3: Ratios And Terms (Factor-Based Ratio Scaler a:b)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Factor-Based Proportional Ratio Generator (5 : 8 × Factor k)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c7s3-badge">k = 3 → 15 : 24</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Multiply BOTH Terms (First = 5, Second = 8) by Factor k:</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s3-kv">k = 3</span>
        </div>
        <input type="range" min="1" max="12" step="1" value="3" id="c8c7s3-k" oninput="updC8C7S3()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s3-eq"></div>
        <div class="text-cyan-200" id="c8c7s3-terms"></div>
    </div>
</div>

<script>
function updC8C7S3() {
    const k = parseInt(document.getElementById("c8c7s3-k").value);
    const t1 = 5 * k, t2 = 8 * k;
    document.getElementById("c8c7s3-kv").textContent = "k = " + k;
    document.getElementById("c8c7s3-badge").textContent = "k = " + k + " → " + t1 + " : " + t2;
    document.getElementById("c8c7s3-eq").textContent = "Proportional Ratio: 5 : 8  ::  " + t1 + " : " + t2 + "   (Dividing both by " + k + " returns 5 : 8!)";
    document.getElementById("c8c7s3-terms").textContent = "First Term = " + t1 + ",   Second Term = " + t2 + " (Order strictly matters: 8 : 5 ≠ 5 : 8)";
}
updC8C7S3();
</script>
"""

# Simulator 4: Simplest Form Proportion (HCF Reducer & :: Verifier)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">HCF Ratio Simplifier &amp; (::) Proportion Comparator</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c7s4-badge">18:24 :: 12:16</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Scale Ratio A (3:4 × m):</span><span class="font-bold text-cyan-300" id="c8c7s4-mv">m = 6 (18:24)</span></div>
            <input type="range" min="1" max="10" step="1" value="6" id="c8c7s4-m" oninput="updC8C7S4()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Scale Ratio B (3:4 × n):</span><span class="font-bold text-amber-300" id="c8c7s4-nv">n = 4 (12:16)</span></div>
            <input type="range" min="1" max="10" step="1" value="4" id="c8c7s4-n" oninput="updC8C7S4()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c7s4-hcf"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s4-prop"></div>
    </div>
</div>

<script>
function updC8C7S4() {
    const m = parseInt(document.getElementById("c8c7s4-m").value);
    const n = parseInt(document.getElementById("c8c7s4-n").value);
    const a1 = 3 * m, b1 = 4 * m;
    const a2 = 3 * n, b2 = 4 * n;
    document.getElementById("c8c7s4-mv").textContent = "m = " + m + " (" + a1 + ":" + b1 + ")";
    document.getElementById("c8c7s4-nv").textContent = "n = " + n + " (" + a2 + ":" + b2 + ")";
    document.getElementById("c8c7s4-badge").textContent = a1 + ":" + b1 + " :: " + a2 + ":" + b2;
    document.getElementById("c8c7s4-hcf").textContent = a1 + ":" + b1 + " ÷ HCF(" + m + ") = 3:4   |   " + a2 + ":" + b2 + " ÷ HCF(" + n + ") = 3:4";
    document.getElementById("c8c7s4-prop").textContent = "Identical Simplest Form (3 : 4) ⇒ TRUE PROPORTION: " + a1 + " : " + b1 + " :: " + a2 + " : " + b2;
}
updC8C7S4();
</script>
"""

# Simulator 5: Lemonade Cement Mixtures (Scaling Sweetness & Structural Strength)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍋</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Lemonade Sweetness &amp; Cement Wall Scaler (2 : 3 Ratio)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c7s5-badge">15 Glasses</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Lemonade Batch Glasses (Multiples of 3):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s5-gv">15 Glasses</span>
        </div>
        <input type="range" min="3" max="30" step="3" value="15" id="c8c7s5-g" oninput="updC8C7S5()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s5-sug"></div>
        <div class="text-cyan-200 font-bold">Civil Cement Check: 4 bags : 6 m :: 6 bags : 9 m (both 2 : 3 equal wall strength!)</div>
    </div>
</div>

<script>
function updC8C7S5() {
    const glasses = parseInt(document.getElementById("c8c7s5-g").value);
    const spoons = (2 * glasses) / 3;
    document.getElementById("c8c7s5-gv").textContent = glasses + " Glasses";
    document.getElementById("c8c7s5-badge").textContent = spoons + " Spoons : " + glasses + " Glasses";
    document.getElementById("c8c7s5-sug").textContent = "Exact Proportional Sugar = " + spoons + " Spoons  (2 : 3 :: " + spoons + " : " + glasses + " — Identical Sweetness!)";
}
updC8C7S5();
</script>
"""

# Simulator 6: Age Additive Fallacy (Time Slider Breaking Parent-Child Age Ratio)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏳</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Additive Non-Proportionality: Parent (30) &amp; Child (10) Ages</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c7s6-badge">+0 Yrs → 3.00 : 1</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Years Passed (+y added identically to BOTH ages!):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s6-yv">+10 Years</span>
        </div>
        <input type="range" min="0" max="50" step="5" value="10" id="c8c7s6-y" oninput="updC8C7S6()" class="w-full accent-rose-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200 font-bold" id="c8c7s6-ages"></div>
        <div class="font-bold text-sm" id="c8c7s6-rat"></div>
    </div>
</div>

<script>
function updC8C7S6() {
    const y = parseInt(document.getElementById("c8c7s6-y").value);
    const p = 30 + y, c = 10 + y;
    const dec = (p / c).toFixed(2);
    document.getElementById("c8c7s6-yv").textContent = "+" + y + " Years";
    document.getElementById("c8c7s6-badge").textContent = "+" + y + " Yrs → " + dec + ":1";
    document.getElementById("c8c7s6-ages").textContent = "Ages After " + y + " Yrs: Parent = " + p + ",   Child = " + c;
    const el = document.getElementById("c8c7s6-rat");
    el.className = "font-bold text-sm " + (y === 0 ? "text-emerald-300" : "text-rose-300");
    el.textContent = y === 0
        ? "Initial Ratio = 30 : 10 = 3 : 1 (3.00× older)"
        : "New Ratio = " + p + " : " + c + " ≈ " + dec + " : 1 (BROKE 3:1! Drifting steadily toward 1:1!)";
}
updC8C7S6();
</script>
"""

# Simulator 7: Filter Coffee Strength (Decoction vs Milk Concentration)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">☕</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Filter Coffee Strength Lab (Decoction : Milk)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c7s7-badge">Compare Cups</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-amber-300 font-bold">Cup A: 20 mL Decoction + 80 mL Milk</div>
            <div class="text-cyan-200">Ratio 1 : 4  |  Decoction % = 20% (Lighter!)</div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/60 space-y-1">
            <div class="text-emerald-300 font-bold">Cup B: 30 mL Decoction + 90 mL Milk</div>
            <div class="text-emerald-200 font-bold">Ratio 1 : 3  |  Decoction % = 25% (STRONGER! ✓)</div>
        </div>
    </div>

    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-amber-200 text-center">
        Interactive Custom Cup: <input type="range" min="10" max="60" step="10" value="30" id="c8c7s7-d" oninput="updC8C7S7()" class="w-28 align-middle accent-amber-400">
        <span class="font-bold text-amber-300" id="c8c7s7-out">30 mL Decoction + 90 mL Milk → 25.0% Strength</span>
    </div>
</div>

<script>
function updC8C7S7() {
    const d = parseInt(document.getElementById("c8c7s7-d").value);
    const m = 90;
    const pct = ((d / (d + m)) * 100).toFixed(1);
    document.getElementById("c8c7s7-out").textContent = d + " mL Decoction + " + m + " mL Milk → " + pct + "% (" + (d >= 30 ? "Rich / Strong" : "Light / Milky") + ")";
}
updC8C7S7();
</script>
"""

# Simulator 8: Trairasika Cross Rule (Āryabhaṭa 499 CE Solver d = (b * c) / a)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Āryabhaṭa's Trairāśika (Rule of Three) Interactive Solver</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c7s8-badge">d = 192</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Pramāṇa (a):</span><span class="font-bold text-cyan-300" id="c8c7s8-av">5</span></div>
            <input type="range" min="1" max="12" step="1" value="5" id="c8c7s8-a" oninput="updC8C7S8()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Phala (b):</span><span class="font-bold text-amber-300" id="c8c7s8-bv">120</span></div>
            <input type="range" min="20" max="200" step="20" value="120" id="c8c7s8-b" oninput="updC8C7S8()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Ichchhā (c):</span><span class="font-bold text-emerald-300" id="c8c7s8-cv">8</span></div>
            <input type="range" min="1" max="20" step="1" value="8" id="c8c7s8-c" oninput="updC8C7S8()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s8-ans"></div>
        <div class="text-cyan-200" id="c8c7s8-prop"></div>
    </div>
</div>

<script>
function updC8C7S8() {
    const a = parseInt(document.getElementById("c8c7s8-a").value);
    const b = parseInt(document.getElementById("c8c7s8-b").value);
    const c = parseInt(document.getElementById("c8c7s8-c").value);
    const d = ((b * c) / a).toFixed(2).replace(/\\.00$/, "");
    document.getElementById("c8c7s8-av").textContent = a;
    document.getElementById("c8c7s8-bv").textContent = b;
    document.getElementById("c8c7s8-cv").textContent = c;
    document.getElementById("c8c7s8-badge").textContent = "Ichchhāphala d = " + d;
    document.getElementById("c8c7s8-ans").textContent = "ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa = (" + b + " × " + c + ") ÷ " + a + " = " + d;
    document.getElementById("c8c7s8-prop").textContent = "Proportion: " + a + " : " + b + " :: " + c + " : " + d + "  (Cross check ad = bc!)";
}
updC8C7S8();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")

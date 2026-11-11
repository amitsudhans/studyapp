#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 3: A Story of Numbers
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Indian Number Roots (Yajurveda Powers of 10 + Bakhshali Dot Zero)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Yajurveda Samhita Powers of 10 (10⁰ to 10¹²) &amp; Bakhshali Zero</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c3s1-badge">10⁴ : Ayuta</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Select Sanskrit Vedic Power of 10 (k):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c3s1-kv">k = 4 (10⁴)</span>
        </div>
        <input type="range" min="0" max="12" step="1" value="4" id="c8c3s1-k" oninput="updC8C3S1()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1.5">
            <div class="text-cyan-300 font-bold text-sm" id="c8c3s1-name"></div>
            <div class="text-emerald-300 font-bold" id="c8c3s1-val"></div>
            <div class="text-slate-400" id="c8c3s1-note"></div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-amber-700/50 space-y-1.5">
            <div class="text-amber-300 font-bold">Bakhshali Dot Zero (c. 3rd CE) &amp; Aryabhata (499 CE)</div>
            <div class="text-slate-200 flex items-center gap-2 pt-1">
                <span class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-amber-300 font-black">3 • 5</span>
                <span>→ Dot marks empty tens place (= 305)!</span>
            </div>
        </div>
    </div>
</div>

<script>
const vedicPowers = [
    ["Eka", "1", "10⁰ — Unity foundation"],
    ["Dasha", "10", "10¹ — Ten fingers"],
    ["Shata", "100", "10² — One hundred"],
    ["Sahasra", "1,000", "10³ — One thousand"],
    ["Ayuta", "10,000", "10⁴ — Ten thousand"],
    ["Niyuta", "1,00,000", "10⁵ — One lakh"],
    ["Prayuta", "10,00,000", "10⁶ — One million"],
    ["Arbuda", "1,00,00,000", "10⁷ — One crore"],
    ["Nyarbuda", "10,00,00,000", "10⁸ — Hundred million"],
    ["Samudra", "1,00,00,00,000", "10⁹ — One Arab / Billion"],
    ["Madhya", "10,00,00,00,000", "10¹⁰ — Ten billion"],
    ["Anta", "1,00,00,00,00,000", "10¹¹ — Kharab"],
    ["Parardha", "10,00,00,00,00,000", "10¹² — Trillion (Yajurveda max!)"]
];
function updC8C3S1() {
    const k = parseInt(document.getElementById("c8c3s1-k").value);
    const p = vedicPowers[k];
    document.getElementById("c8c3s1-kv").textContent = "k = " + k + " (10^" + k + ")";
    document.getElementById("c8c3s1-badge").textContent = "10^" + k + " : " + p[0];
    document.getElementById("c8c3s1-name").textContent = "Sanskrit Name: " + p[0];
    document.getElementById("c8c3s1-val").textContent = "Value: " + p[1] + " (10^" + k + ")";
    document.getElementById("c8c3s1-note").textContent = p[2];
}
updC8C3S1();
</script>
"""

# Simulator 2: Global Numeral Journey (Brahmi -> Devanagari -> Arabic -> European Digits)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌍</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Brahmi to Modern Numeral Evolution Timeline</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c3s2-badge">Digit: 3</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Inspect Digit Evolution (1 to 9):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c3s2-dv">Digit 3</span>
        </div>
        <input type="range" min="1" max="9" step="1" value="3" id="c8c3s2-d" oninput="updC8C3S2()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
            <div class="text-[10px] text-slate-400">Brahmi (3rd BCE)</div>
            <div class="text-lg font-black text-amber-300 mt-1" id="c8c3s2-br"></div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
            <div class="text-[10px] text-slate-400">Devanagari (India)</div>
            <div class="text-lg font-black text-emerald-300 mt-1" id="c8c3s2-dev"></div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
            <div class="text-[10px] text-slate-400">Al-Khwarizmi (820 CE)</div>
            <div class="text-lg font-black text-cyan-300 mt-1" id="c8c3s2-ar"></div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-cyan-600/60">
            <div class="text-[10px] text-cyan-300 font-bold">Fibonacci / Modern</div>
            <div class="text-lg font-black text-white mt-1" id="c8c3s2-mod"></div>
        </div>
    </div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-amber-200 font-mono text-center">
        Route: India (Brahmi &amp; Aryabhata) → Baghdad (Al-Khwarizmi, Al-Kindi c.800–830 CE) → Europe (Fibonacci c.1200 CE &amp; Renaissance)
    </div>
</div>

<script>
const digitMorph = {
    1: ["𑁒 (I)", "१", "١", "1"],
    2: ["𑁓 (=)", "२", "٢", "2"],
    3: ["𑁔 (≡)", "३", "٣", "3"],
    4: ["𑁕 (+)", "४", "٤", "4"],
    5: ["𑁖", "५", "٥", "5"],
    6: ["𑁗", "६", "٦", "6"],
    7: ["𑁘", "७", "٧", "7"],
    8: ["𑁙", "८", "٨", "8"],
    9: ["𑁚", "९", "٩", "9"]
};
function updC8C3S2() {
    const d = parseInt(document.getElementById("c8c3s2-d").value);
    const row = digitMorph[d];
    document.getElementById("c8c3s2-dv").textContent = "Digit " + d;
    document.getElementById("c8c3s2-badge").textContent = "Digit: " + d;
    document.getElementById("c8c3s2-br").textContent = row[0];
    document.getElementById("c8c3s2-dev").textContent = row[1];
    document.getElementById("c8c3s2-ar").textContent = row[2];
    document.getElementById("c8c3s2-mod").textContent = row[3];
}
updC8C3S2();
</script>
"""

# Simulator 3: Early Counting Logic (Sticks/Pebbles 1-to-1, Phonetic Sequence, Symbols)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪨</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Stone Age 3-Method Herd Tracker (No Modern Digits!)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c3s3-badge">Morning: 8 | Returned: 6</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Morning Sheep Out:</span><span class="font-bold text-amber-300" id="c8c3s3-mv">8</span></div>
            <input type="range" min="1" max="15" step="1" value="8" id="c8c3s3-m" oninput="updC8C3S3()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Evening Returned:</span><span class="font-bold text-emerald-300" id="c8c3s3-ev">6</span></div>
            <input type="range" min="0" max="15" step="1" value="6" id="c8c3s3-e" oninput="updC8C3S3()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-200" id="c8c3s3-peb"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c3s3-let"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c3s3-diff"></div>
    </div>
</div>

<script>
const alphaSeq = "abcdefghijklmno";
function updC8C3S3() {
    const m = parseInt(document.getElementById("c8c3s3-m").value);
    const eSlider = document.getElementById("c8c3s3-e");
    let e = parseInt(eSlider.value);
    if (e > m) { e = m; eSlider.value = m; }
    const miss = m - e;

    document.getElementById("c8c3s3-mv").textContent = m;
    document.getElementById("c8c3s3-ev").textContent = e;
    document.getElementById("c8c3s3-badge").textContent = "Out: " + m + " | Back: " + e;

    const matched = Array(e).fill("🟢").join("");
    const leftover = Array(miss).fill("🪨").join("");
    document.getElementById("c8c3s3-peb").textContent = "Method 1 (1-to-1 Pebbles): Matched=" + (matched || "none") + " | Leftover=" + (leftover || "ZERO missing!");
    document.getElementById("c8c3s3-let").textContent = "Method 2 (Phonetic Sequence): Morning reached '" + alphaSeq[m - 1] + "', Evening reached '" + (e > 0 ? alphaSeq[e - 1] : "none") + "'";
    document.getElementById("c8c3s3-diff").textContent = miss === 0
        ? "All sheep returned safely! Leftover sticks/pebbles: 0"
        : "Missing count (Method 3 Sticks): " + Array(miss).fill("|").join(" ") + " (" + miss + " left in pouch!)";
}
updC8C3S3();
</script>
"""

# Simulator 4: Body Part Counting (Papua New Guinea 27-Landmark Anatomical Sequence)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧍</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Papua New Guinea 27-Point Body Sequence Explorer</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c3s4-badge">#14: Nose Bridge</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Touch Sequence Step (1 to 27):</span>
            <span class="font-bold text-indigo-300 font-mono" id="c8c3s4-pv">Step #14</span>
        </div>
        <input type="range" min="1" max="27" step="1" value="14" id="c8c3s4-p" oninput="updC8C3S4()" class="w-full accent-indigo-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c3s4-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-amber-300 font-bold" id="c8c3s4-land"></div>
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c3s4-rule"></div>
        </div>
    </div>
</div>

<script>
const bodyMap = [
    "L. Little Finger", "L. Ring Finger", "L. Middle Finger", "L. Index Finger", "L. Thumb",
    "L. Wrist", "L. Forearm", "L. Elbow", "L. Upper Arm", "L. Shoulder",
    "L. Collarbone", "L. Ear", "L. Eye", "Nose Bridge (Center)",
    "R. Eye", "R. Ear", "R. Collarbone", "R. Shoulder", "R. Upper Arm",
    "R. Elbow", "R. Forearm", "R. Wrist", "R. Thumb", "R. Index Finger",
    "R. Middle Finger", "R. Ring Finger", "R. Little Finger"
];
function updC8C3S4() {
    const p = parseInt(document.getElementById("c8c3s4-p").value);
    const name = bodyMap[p - 1];
    document.getElementById("c8c3s4-pv").textContent = "Step #" + p;
    document.getElementById("c8c3s4-badge").textContent = "#" + p + ": " + name;
    document.getElementById("c8c3s4-land").textContent = "Landmark #" + p + " = " + name;
    document.getElementById("c8c3s4-rule").textContent = p === 14
        ? "Exact symmetric midpoint (#14 of 27)!"
        : (p < 14 ? "Ascending Left Side (Step " + p + " → 14)" : "Descending Right Side (Step " + p + " → 27)");

    let dots = `<line x1="20" y1="60" x2="110" y2="25" stroke="#475569" stroke-width="2"/><line x1="110" y1="25" x2="200" y2="60" stroke="#475569" stroke-width="2"/>`;
    for (let i = 1; i <= 27; i++) {
        const x = 18 + (i - 1) * 7.1;
        const y = i <= 14 ? 65 - (i - 1) * 3 : 26 + (i - 14) * 3;
        const cur = i === p;
        dots += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${cur ? 5.5 : 2.2}" fill="${cur ? "#fbbf24" : (i < p ? "#34d399" : "#334155")}"/>`;
    }
    dots += `<text x="110" y="96" text-anchor="middle" fill="#a5b4fc" font-size="9" font-weight="bold">Fixed Order = Shared Cardinal Meaning</text>`;
    document.getElementById("c8c3s4-svg").innerHTML = dots;
}
updC8C3S4();
</script>
"""

# Simulator 5: Bone Tally Marks (Lebombo 29 Notches vs Ishango Primes & 5-Bundle Tally)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🦴</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Ancient Bone Notches: Lebombo (44,000 yrs) &amp; Ishango Bone</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c3s5-badge">Lebombo Bone</span>
    </div>

    <div class="flex flex-wrap gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setBoneS5(0)" class="px-3 py-1 rounded-lg bg-amber-600 text-white font-bold">Lebombo Bone (~44,000 yrs)</button>
        <button onclick="setBoneS5(1)" class="px-3 py-1 rounded-lg bg-cyan-700 text-white font-bold">Ishango Bone (~20–35k yrs)</button>
        <button onclick="setBoneS5(2)" class="px-3 py-1 rounded-lg bg-emerald-700 text-white font-bold">5-Bundle Cross Tally (23)</button>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2">
        <svg viewBox="0 0 360 72" class="w-full h-20 bg-slate-950 rounded-xl border border-slate-800" id="c8c3s5-svg"></svg>
        <div class="font-mono text-xs bg-slate-950 p-2.5 rounded-lg border border-slate-800 text-emerald-300 font-bold text-center" id="c8c3s5-info"></div>
    </div>
</div>

<script>
function setBoneS5(mode) {
    let svg = `<rect x="18" y="20" width="324" height="32" rx="14" fill="#3f3626" stroke="#b49a6c" stroke-width="2"/>`;
    if (mode === 0) {
        for (let i = 0; i < 29; i++) {
            const x = 32 + i * 10.2;
            svg += `<line x1="${x}" y1="22" x2="${x}" y2="48" stroke="#fde68a" stroke-width="2"/>`;
        }
        document.getElementById("c8c3s5-badge").textContent = "Lebombo (29 Notches)";
        document.getElementById("c8c3s5-info").textContent = "South Africa (~44,000 yrs old): 29 parallel carved notches — matches a ~29-day lunar cycle!";
    } else if (mode === 1) {
        const groups = [11, 13, 17, 19];
        let x = 30;
        groups.forEach(g => {
            for (let k = 0; k < g; k++) {
                svg += `<line x1="${x}" y1="23" x2="${x}" y2="47" stroke="#38bdf8" stroke-width="1.6"/>`;
                x += 4.2;
            }
            x += 18;
        });
        document.getElementById("c8c3s5-badge").textContent = "Ishango (Primes 11,13,17,19)";
        document.getElementById("c8c3s5-info").textContent = "DR Congo (~20,000–35,000 yrs old): Structured columns showing prime sequences (11,13,17,19) & doublings!";
    } else {
        for (let b = 0; b < 4; b++) {
            const bx = 35 + b * 68;
            for (let s = 0; s < 4; s++) {
                svg += `<line x1="${bx + s * 9}" y1="23" x2="${bx + s * 9}" y2="49" stroke="#34d399" stroke-width="2.2"/>`;
            }
            svg += `<line x1="${bx - 3}" y1="46" x2="${bx + 30}" y2="25" stroke="#fbbf24" stroke-width="2.5"/>`;
        }
        for (let r = 0; r < 3; r++) {
            svg += `<line x1="${307 + r * 9}" y1="23" x2="${307 + r * 9}" y2="49" stroke="#34d399" stroke-width="2.2"/>`;
        }
        document.getElementById("c8c3s5-badge").textContent = "Grouped Fives = 23";
        document.getElementById("c8c3s5-info").textContent = "Four 5-bundles (4×5 = 20) + 3 loose strokes = 23 — instantly subitized without recounting 1-by-1!";
    }
    document.getElementById("c8c3s5-svg").innerHTML = svg;
}
setBoneS5(0);
</script>
"""

# Simulator 6: Counting In Twos (Gumulgal Pairs + Visual Subitizing Limit)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✌️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Gumulgal Counting-in-Twos &amp; Visual Subitizing Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c3s6-badge">n = 5</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Quantity (1 to 8):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c3s6-nv">n = 5</span>
        </div>
        <input type="range" min="1" max="8" step="1" value="5" id="c8c3s6-n" oninput="updC8C3S6()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-2.5 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-amber-300 font-bold" id="c8c3s6-word"></div>
            <div class="text-slate-300" id="c8c3s6-parts"></div>
        </div>
        <div class="p-2.5 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-base tracking-widest" id="c8c3s6-dots"></div>
            <div class="font-bold" id="c8c3s6-sub"></div>
        </div>
    </div>
</div>

<script>
function updC8C3S6() {
    const n = parseInt(document.getElementById("c8c3s6-n").value);
    const pairs = Math.floor(n / 2);
    const rem = n % 2;
    let words = [];
    for (let i = 0; i < pairs; i++) words.push("ukasar");
    if (rem === 1) words.push("urapon");

    document.getElementById("c8c3s6-nv").textContent = "n = " + n;
    document.getElementById("c8c3s6-badge").textContent = "n = " + n;
    document.getElementById("c8c3s6-word").textContent = "Gumulgal: " + words.join("-");
    document.getElementById("c8c3s6-parts").textContent = "Expanded: " + Array(pairs).fill("2").concat(rem ? ["1"] : []).join(" + ") + " = " + n;
    document.getElementById("c8c3s6-dots").textContent = Array(n).fill("🟡").join(" ");
    const subEl = document.getElementById("c8c3s6-sub");
    if (n <= 4) {
        subEl.className = "font-bold text-emerald-300";
        subEl.textContent = "Within Subitizing Limit (≤ 4): recognized in 1 glance!";
    } else {
        subEl.className = "font-bold text-rose-300";
        subEl.textContent = "Above Subitizing Limit (> 4): needs pair/group bundling!";
    }
}
updC8C3S6();
</script>
"""

# Simulator 7: Roman Numeral System (Live Encoder + Subtractive Highlighter)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏛️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Roman Numeral Builder (I, V, X, L, C, D, M)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c3s7-badge">MMCCCLXVII</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Slide Decimal Value (1 to 3,999):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c3s7-nv">2,367</span>
        </div>
        <input type="range" min="1" max="3999" step="1" value="2367" id="c8c3s7-n" oninput="updC8C3S7()" class="w-full accent-amber-400">
        <div class="flex flex-wrap gap-1.5">
            <button onclick="setRomS7(1994)" class="px-2 py-1 rounded bg-slate-800 text-cyan-300 text-[11px] font-bold border border-slate-700">Test 1994 (MCMXCIV)</button>
            <button onclick="setRomS7(449)" class="px-2 py-1 rounded bg-slate-800 text-emerald-300 text-[11px] font-bold border border-slate-700">Test 449 (CDXLIX)</button>
            <button onclick="setRomS7(2367)" class="px-2 py-1 rounded bg-slate-800 text-amber-300 text-[11px] font-bold border border-slate-700">Test 2367</button>
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-lg font-black tracking-wider text-amber-300" id="c8c3s7-rom"></div>
        <div class="text-emerald-300 font-bold" id="c8c3s7-brk"></div>
    </div>
</div>

<script>
const romPairs = [
    [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
    [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
    [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
];
function setRomS7(v) {
    document.getElementById("c8c3s7-n").value = v;
    updC8C3S7();
}
function updC8C3S7() {
    let rem = parseInt(document.getElementById("c8c3s7-n").value);
    const orig = rem;
    let rom = "";
    let parts = [];
    for (const [val, sym] of romPairs) {
        let count = 0;
        while (rem >= val) {
            rom += sym;
            rem -= val;
            count++;
        }
        if (count > 0) parts.push(sym.repeat(count) + "=" + (count * val));
    }
    document.getElementById("c8c3s7-nv").textContent = orig.toLocaleString("en-IN");
    document.getElementById("c8c3s7-badge").textContent = rom;
    document.getElementById("c8c3s7-rom").textContent = rom;
    document.getElementById("c8c3s7-brk").textContent = "Breakdown: " + parts.join(" + ") + " = " + orig;
}
updC8C3S7();
</script>
"""

# Simulator 8: Egyptian Hieroglyphic Base (c. 3000 BCE Powers of 10 Landmarks)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪷</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Egyptian Hieroglyphic Converter (c. 3000 BCE Landmarks)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c3s8-badge">3,425</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Test Any Value (1 to 25,000):</span>
            <span class="font-bold text-emerald-300 font-mono" id="c8c3s8-nv">3,425</span>
        </div>
        <input type="range" min="1" max="25000" step="1" value="3425" id="c8c3s8-n" oninput="updC8C3S8()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="text-base leading-relaxed text-amber-200 text-center" id="c8c3s8-glyphs"></div>
        <div class="text-cyan-300 font-bold text-center" id="c8c3s8-count"></div>
        <div class="grid grid-cols-7 gap-1 text-[10px] text-center text-slate-400 pt-1 border-t border-slate-800">
            <div>𓏺<br>Staff<br>10⁰</div>
            <div>𓎆<br>Heel<br>10¹</div>
            <div>𓍢<br>Coil<br>10²</div>
            <div>𓆼<br>Lotus<br>10³</div>
            <div>𓂭<br>Finger<br>10⁴</div>
            <div>🐸<br>Frog<br>10⁵</div>
            <div>🙌<br>Man<br>10⁶</div>
        </div>
    </div>
</div>

<script>
const egyWeights = [
    [10000, "☝️ Finger"],
    [1000, "🪷 Lotus"],
    [100, "🌀 Coil"],
    [10, "🧲 Heel"],
    [1, "| Staff"]
];
function updC8C3S8() {
    let rem = parseInt(document.getElementById("c8c3s8-n").value);
    const orig = rem;
    let out = [];
    let totalGlyphs = 0;
    for (const [w, lbl] of egyWeights) {
        const c = Math.floor(rem / w);
        rem %= w;
        totalGlyphs += c;
        if (c > 0) out.push(c + "×" + lbl);
    }
    document.getElementById("c8c3s8-nv").textContent = orig.toLocaleString("en-IN");
    document.getElementById("c8c3s8-badge").textContent = orig.toLocaleString("en-IN");
    document.getElementById("c8c3s8-glyphs").textContent = out.join("  +  ");
    document.getElementById("c8c3s8-count").textContent = "Total Carved Hieroglyphs: " + totalGlyphs + " (Purely Additive — Any Order Reads " + orig.toLocaleString("en-IN") + ")";
}
updC8C3S8();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 9: The Baudhāyana-Pythagoras Theorem
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>📐</span> Śulba-Sūtra Verse 1.9: Doubling a Square
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c9s1Mode('orig')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Original (2Δ)</button>
      <button type="button" onclick="c9s1Mode('diag')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">On Diagonal (4Δ = 2×)</button>
      <button type="button" onclick="c9s1Mode('doubleSide')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Side × 2 (8Δ = 4× Trap!)</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c9s1Svg" viewBox="0 0 220 220" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9s1Info" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  window.c9s1Mode = function(mode){
    const svg = document.getElementById('c9s1Svg');
    const info = document.getElementById('c9s1Info');
    if(!svg || !info) return;
    if(mode === 'orig'){
      svg.innerHTML = `
        <rect x="65" y="65" width="90" height="90" fill="#0e7490" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2.5"/>
        <line x1="65" y1="65" x2="155" y2="155" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="110" y="55" text-anchor="middle" fill="#22d3ee" font-size="11">Side = s (Area = 1×)</text>`;
      info.innerHTML = `<b class="text-cyan-300">Original Square (Area = s²):</b><br>Drawing one diagonal slices the square into <b>2 congruent right isosceles triangles</b>.`;
    } else if(mode === 'diag'){
      svg.innerHTML = `
        <polygon points="110,40 180,110 110,180 40,110" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="2.5"/>
        <line x1="110" y1="40" x2="110" y2="180" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
        <line x1="40" y1="110" x2="180" y2="110" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="110" y="25" text-anchor="middle" fill="#34d399" font-size="11">Diagonal Square = 2× Area!</text>`;
      info.innerHTML = `<b class="text-emerald-300">Baudhāyana's Diagonal Square (2× Area):</b><br>Horizontal & vertical grid lines reveal <b>4 congruent triangles</b> (4 ÷ 2 = EXACT 2× area)!`;
    } else {
      svg.innerHTML = `
        <rect x="20" y="20" width="180" height="180" fill="#be123c" fill-opacity="0.25" stroke="#fb7185" stroke-width="2.5"/>
        <line x1="110" y1="20" x2="110" y2="200" stroke="#64748b" stroke-width="1.5"/>
        <line x1="20" y1="110" x2="200" y2="110" stroke="#64748b" stroke-width="1.5"/>
        <text x="110" y="14" text-anchor="middle" fill="#fb7185" font-size="11">Side = 2s → 4× Area (TRAP!)</text>`;
      info.innerHTML = `<b class="text-rose-300">Doubling Side Length = 4× Area!</b><br>(2s) × (2s) = 4s² = <b>8 triangles</b>! Side doubling overshoots double area by 2×.`;
    }
  };
  window.c9s1Mode('diag');
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📄</span> Section 2.2: Midpoint Paper Folding (PQRS = ½ Area)
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c9s2Svg" viewBox="0 0 220 220" class="w-full max-w-[220px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div class="space-y-3 text-xs">
      <label class="block text-slate-300">Fold Corners Inward to Center (0% → 100%)
        <input id="c9s2Fold" type="range" min="0" max="100" value="60" oninput="c9s2Draw()" class="mt-2 w-full accent-cyan-400">
      </label>
      <div id="c9s2Txt" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-slate-300 space-y-1"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c9s2Draw = function(){
    const pct = parseFloat(document.getElementById('c9s2Fold').value) || 0;
    const t = pct / 100;
    const svg = document.getElementById('c9s2Svg');
    if(!svg) return;
    const x0 = 30, y0 = 30, s = 160, cx = 110, cy = 110;
    const p = {x:110, y:30}, q = {x:190, y:110}, r = {x:110, y:190}, sPt = {x:30, y:110};
    const flap = (ox, oy, m1, m2) => {
      const fx = ox + (cx - ox) * t;
      const fy = oy + (cy - oy) * t;
      return `<polygon points="${m1.x},${m1.y} ${m2.x},${m2.y} ${fx.toFixed(1)},${fy.toFixed(1)}" fill="#fbbf24" fill-opacity="0.45" stroke="#fbbf24" stroke-width="1.5"/>`;
    };
    svg.innerHTML = `
      <rect x="${x0}" y="${y0}" width="${s}" height="${s}" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <polygon points="${p.x},${p.y} ${q.x},${q.y} ${r.x},${r.y} ${sPt.x},${sPt.y}" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/>
      ${flap(30,30,sPt,p)} ${flap(190,30,p,q)} ${flap(190,190,q,r)} ${flap(30,190,r,sPt)}
      <text x="110" y="23" text-anchor="middle" fill="#cbd5e1" font-size="10">P</text>
      <text x="200" y="114" fill="#cbd5e1" font-size="10">Q</text>
      <text x="110" y="206" text-anchor="middle" fill="#cbd5e1" font-size="10">R</text>
      <text x="20" y="114" fill="#cbd5e1" font-size="10">S</text>`;
    document.getElementById('c9s2Txt').innerHTML = `Fold progress: <b class="text-cyan-300">${pct}%</b><br>Outer 4 triangular corners fold cleanly onto center to cover all of inscribed square <b>PQRS</b> → Area(PQRS) = <b class="text-emerald-300">exact 50% (½)</b>!`;
  };
  window.c9s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📏</span> Isosceles Right Triangle Explorer (c = a√2)
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg viewBox="0 0 220 180" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800">
      <polygon points="50,140 160,140 50,30" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="2.5"/>
      <rect x="50" y="126" width="14" height="14" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
      <text id="c9s3LegA" x="35" y="90" text-anchor="middle" fill="#38bdf8" font-size="11">a = 1</text>
      <text id="c9s3LegB" x="105" y="158" text-anchor="middle" fill="#38bdf8" font-size="11">a = 1</text>
      <text id="c9s3Hyp" x="128" y="80" fill="#fbbf24" font-size="11" font-weight="bold">c = √2</text>
    </svg>
    <div class="space-y-3 text-xs">
      <label class="block text-slate-300">Equal Leg Length (a):
        <input id="c9s3A" type="range" min="1" max="12" value="1" oninput="c9s3Calc()" class="mt-1 w-full accent-emerald-400">
      </label>
      <div id="c9s3Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1 text-slate-300"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c9s3Calc = function(){
    const a = parseInt(document.getElementById('c9s3A').value, 10) || 1;
    const c2 = 2 * a * a;
    const cDec = (a * Math.SQRT2).toFixed(3);
    document.getElementById('c9s3LegA').textContent = 'a = ' + a;
    document.getElementById('c9s3LegB').textContent = 'a = ' + a;
    document.getElementById('c9s3Hyp').textContent = `c = ${a === 1 ? '' : a}√2`;
    document.getElementById('c9s3Out').innerHTML = `
      <div>Leg Square Area (a²): <b class="text-cyan-300">${a*a}</b> each</div>
      <div>Hypotenuse Square (c² = 2a²): <b class="text-emerald-300">${c2}</b></div>
      <div>Exact Hypotenuse c: <b class="text-amber-300">${a===1?'':a}√2 ≈ ${cDec}</b></div>`;
  };
  window.c9s3Calc();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🔍</span> Nested √2 Bounds & Last-Digit Non-Terminating Proof
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c9s4Zoom(0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">1–2</button>
      <button type="button" onclick="c9s4Zoom(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">1.4–1.5</button>
      <button type="button" onclick="c9s4Zoom(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">1.414–1.415</button>
    </div>
  </div>
  <div id="c9s4Bound" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1.5 text-xs">
    <div class="font-bold text-rose-300">Last Non-Zero Digit Squaring Test (Click any digit d = 1..9):</div>
    <div id="c9s4Digits" class="flex flex-wrap gap-1.5"></div>
    <div id="c9s4DigitRes" class="text-slate-300 pt-1"></div>
  </div>
</div>
<script>
(function(){
  const levels = [
    '<b>Integer Bounds:</b> 1² = 1 (&lt; 2) and 2² = 4 (&gt; 2) → <span class="text-cyan-300 font-bold">1 &lt; √2 &lt; 2</span>',
    '<b>Tenths Bounds:</b> 1.4² = 1.96 (&lt; 2) and 1.5² = 2.25 (&gt; 2) → <span class="text-emerald-300 font-bold">1.4 &lt; √2 &lt; 1.5</span>',
    '<b>Thousandths Bounds:</b> 1.414² = 1.999396 (&lt; 2) and 1.415² = 2.002225 (&gt; 2) → <span class="text-amber-300 font-bold">1.414 &lt; √2 &lt; 1.415</span>'
  ];
  window.c9s4Zoom = function(idx){
    const el = document.getElementById('c9s4Bound');
    if(el) el.innerHTML = levels[idx] || levels[0];
  };
  const dBox = document.getElementById('c9s4Digits');
  if(dBox){
    for(let d = 1; d <= 9; d++){
      const b = document.createElement('button');
      b.type = 'button';
      b.textContent = d;
      b.className = 'w-7 h-7 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold border border-slate-700';
      b.onclick = () => {
        document.getElementById('c9s4DigitRes').innerHTML = `Last digit <b>${d}</b> → ${d}² = <b>${d*d}</b> (ends in <b>${(d*d)%10} ≠ 0</b>)! Never hits 2.000...!`;
      };
      dBox.appendChild(b);
    }
    document.getElementById('c9s4DigitRes').textContent = 'No digit 1–9 squared ends in 0 → NO terminating decimal squared can ever equal 2!';
  }
  window.c9s4Zoom(2);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧮</span> Euclid's Proof (Elements): 2n² = m² Factor-of-2 Parity Clash
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Test Integer n: <input id="c9s5N" type="number" value="12" min="1" max="500" oninput="c9s5Test()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Test Integer m: <input id="c9s5M" type="number" value="17" min="1" max="500" oninput="c9s5Test()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c9s5Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  function count2(x){
    let c = 0, v = Math.abs(Math.floor(x));
    if(v === 0) return 0;
    while(v % 2 === 0){ c++; v /= 2; }
    return c;
  }
  window.c9s5Test = function(){
    const n = Math.max(1, parseInt(document.getElementById('c9s5N').value, 10) || 1);
    const m = Math.max(1, parseInt(document.getElementById('c9s5M').value, 10) || 1);
    const cN = count2(n), cM = count2(m);
    const lhsTwos = 1 + 2 * cN;
    const rhsTwos = 2 * cM;
    const lhs = 2 * n * n, rhs = m * m;
    document.getElementById('c9s5Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2 text-center">
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
          <div class="text-slate-400">LHS = 2n² = ${lhs}</div>
          <div class="text-amber-300 font-bold text-sm">2s count = 1 + ${2*cN} = ${lhsTwos} (ALWAYS ODD!)</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
          <div class="text-slate-400">RHS = m² = ${rhs}</div>
          <div class="text-cyan-300 font-bold text-sm">2s count = 2×${cM} = ${rhsTwos} (ALWAYS EVEN!)</div>
        </div>
      </div>
      <div class="text-rose-300 font-semibold">Parity Clash! ${lhsTwos} (Odd) ≠ ${rhsTwos} (Even) → 2n² can NEVER equal m², so √2 ≠ m/n!</div>`;
  };
  window.c9s5Test();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>➕</span> Verse 1.12 Combining Two Squares: a² + b² = c²
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Leg a: <span id="c9s6ALbl" class="text-cyan-300 font-bold">3</span>
      <input id="c9s6A" type="range" min="1" max="15" value="3" oninput="c9s6Calc()" class="w-full accent-cyan-400">
    </label>
    <label class="text-slate-300">Leg b: <span id="c9s6BLbl" class="text-amber-300 font-bold">4</span>
      <input id="c9s6B" type="range" min="1" max="15" value="4" oninput="c9s6Calc()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9s6Boxes" class="grid grid-cols-3 gap-2 text-center text-xs"></div>
</div>
<script>
(function(){
  window.c9s6Calc = function(){
    const a = parseInt(document.getElementById('c9s6A').value, 10) || 3;
    const b = parseInt(document.getElementById('c9s6B').value, 10) || 4;
    document.getElementById('c9s6ALbl').textContent = a;
    document.getElementById('c9s6BLbl').textContent = b;
    const c2 = a*a + b*b;
    const c = Math.sqrt(c2);
    const cStr = Number.isInteger(c) ? c.toString() : '√' + c2 + ' ≈ ' + c.toFixed(2);
    document.getElementById('c9s6Boxes').innerHTML = `
      <div class="p-3 rounded-xl bg-slate-950 border border-cyan-500/40"><div class="text-slate-400">Square on Leg a</div><div class="text-lg font-bold text-cyan-300">${a*a}</div><div class="text-[10px] text-slate-400">${a} × ${a}</div></div>
      <div class="p-3 rounded-xl bg-slate-950 border border-amber-500/40"><div class="text-slate-400">Square on Leg b</div><div class="text-lg font-bold text-amber-300">${b*b}</div><div class="text-[10px] text-slate-400">${b} × ${b}</div></div>
      <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/40"><div class="text-slate-400">Combined c² = a²+b²</div><div class="text-lg font-bold text-emerald-300">${c2}</div><div class="text-[10px] text-emerald-200">c = ${cStr}</div></div>`;
  };
  window.c9s6Calc();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>✂️</span> Baudhāyana Verse 2.1 Dissection Proof
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c9s7Step(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">1. Join a²+b²</button>
      <button type="button" onclick="c9s7Step(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">2. Slice 2Δ</button>
      <button type="button" onclick="c9s7Step(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">3. Unified c²</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c9s7Svg" viewBox="0 0 220 200" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9s7Desc" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c9s7Step = function(s){
    const svg = document.getElementById('c9s7Svg');
    const desc = document.getElementById('c9s7Desc');
    if(!svg || !desc) return;
    if(s === 1){
      svg.innerHTML = `
        <rect x="40" y="100" width="50" height="50" fill="#0891b2" fill-opacity="0.4" stroke="#22d3ee" stroke-width="2"/>
        <rect x="90" y="65" width="85" height="85" fill="#d97706" fill-opacity="0.4" stroke="#fbbf24" stroke-width="2"/>
        <text x="65" y="128" text-anchor="middle" fill="#22d3ee" font-size="11">a²</text>
        <text x="132" y="110" text-anchor="middle" fill="#fbbf24" font-size="12">b²</text>`;
      desc.innerHTML = `<b class="text-cyan-300">Step 1: Place Two Unequal Squares Side by Side</b><br>Smaller square <b>a²</b> sits flush next to larger square <b>b²</b> along a shared base.`;
    } else if(s === 2){
      svg.innerHTML = `
        <rect x="40" y="100" width="50" height="50" fill="#0891b2" fill-opacity="0.25" stroke="#22d3ee" stroke-width="1.5"/>
        <rect x="90" y="65" width="85" height="85" fill="#d97706" fill-opacity="0.25" stroke="#fbbf24" stroke-width="1.5"/>
        <polygon points="40,150 125,150 125,100" fill="#f43f5e" fill-opacity="0.35" stroke="#fb7185" stroke-width="2" stroke-dasharray="4,2"/>
        <polygon points="125,150 175,150 175,65" fill="#10b981" fill-opacity="0.35" stroke="#34d399" stroke-width="2" stroke-dasharray="4,2"/>`;
      desc.innerHTML = `<b class="text-amber-300">Step 2: Verse 2.1 Marking & Dissection</b><br>Measure width <b>a</b> along the base and slice two congruent right-angled triangles having legs <b>a, b</b> and hypotenuse <b>c</b>.`;
    } else {
      svg.innerHTML = `
        <polygon points="125,100 175,65 140,15 90,50" fill="#059669" fill-opacity="0.45" stroke="#34d399" stroke-width="2.5"/>
        <text x="133" y="62" text-anchor="middle" fill="#ecfdf5" font-size="13" font-weight="bold">c²</text>`;
      desc.innerHTML = `<b class="text-emerald-300">Step 3: Rigid Rotation Assembles Exact Square c²!</b><br>Sliding and rotating the two sliced right triangles covers all edges of length <b>c</b> with 90° corners (α + β = 90°), proving <b>a² + b² = c²</b>!`;
    }
  };
  window.c9s7Step(1);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🔢</span> Verse 1.13 Baudhāyana Triples & Scaling (ka, kb, kc)
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c9s8Set(3,4,5)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">(3,4,5)</button>
      <button type="button" onclick="c9s8Set(5,12,13)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">(5,12,13)</button>
      <button type="button" onclick="c9s8Set(8,15,17)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">(8,15,17)</button>
      <button type="button" onclick="c9s8Set(7,24,25)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">(7,24,25)</button>
    </div>
  </div>
  <label class="block text-xs text-slate-300">Scale Multiplier k: <span id="c9s8KVal" class="font-bold text-amber-300">1</span>
    <input id="c9s8K" type="range" min="1" max="6" value="1" oninput="c9s8Calc()" class="mt-1 w-full accent-amber-400">
  </label>
  <div id="c9s8Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  let base = [3, 4, 5];
  window.c9s8Set = function(a, b, c){ base = [a, b, c]; window.c9s8Calc(); };
  window.c9s8Calc = function(){
    const k = parseInt(document.getElementById('c9s8K').value, 10) || 1;
    document.getElementById('c9s8KVal').textContent = k;
    const sa = k*base[0], sb = k*base[1], sc = k*base[2];
    const kind = k === 1 ? '<span class="text-emerald-300 font-bold">PRIMITIVE Triple (HCF = 1)</span>' : `<span class="text-amber-300 font-bold">SCALED Triple (HCF = ${k})</span>`;
    document.getElementById('c9s8Out').innerHTML = `
      <div>Resulting Triple: <b class="text-cyan-300 text-sm">(${sa}, ${sb}, ${sc})</b> — ${kind}</div>
      <div>Verification: ${sa}² + ${sb}² = ${sa*sa} + ${sb*sb} = <b class="text-emerald-300">${sc*sc} = ${sc}²</b> ✓</div>`;
  };
  window.c9s8Calc();
})();
</script>
"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 2: Introduction to Linear Polynomials
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪴</span> Real-World Garden Fencing &amp; Grass Seed Expression Builder
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Variable Length l (metres): <strong id="c9c2s1LVal" class="text-cyan-300">8 m</strong></span>
      <input type="range" id="c9c2s1L" min="2" max="20" value="8" oninput="c9c2s1Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
      <span class="text-slate-300">Fixed Width w = <strong>5 m</strong></span>
      <span class="text-amber-300 font-semibold">Fence ₹40/m | Seed ₹15/m²</span>
    </div>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s1Svg" viewBox="0 0 220 140" class="w-56 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s1Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s1Draw = function(){
    const l = parseInt(document.getElementById('c9c2s1L').value);
    document.getElementById('c9c2s1LVal').textContent = `${l} m`;
    const perim = 2*l + 10, area = 5*l;
    const fCost = 40 * perim, sCost = 15 * area, total = fCost + sCost;
    const rw = 20 + l * 8;
    const svg = `<rect x="20" y="32" width="${rw}" height="65" fill="#059669" fill-opacity="0.28" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5 2"/>` +
                `<text x="${20 + rw/2}" y="24" fill="#22d3ee" font-size="9" text-anchor="middle" font-weight="bold">Length l = ${l} m</text>` +
                `<text x="${20 + rw/2}" y="68" fill="#6ee7b7" font-size="9" text-anchor="middle">Area = 5l = ${area} m²</text>` +
                `<text x="${25 + rw}" y="68" fill="#fbbf24" font-size="8.5">w=5m</text>`;
    document.getElementById('c9c2s1Svg').innerHTML = svg;
    document.getElementById('c9c2s1Out').innerHTML = `
      <div class="font-bold text-cyan-300">Combined Cost Formula: 40(2l + 10) + 15(5l) = 155l + 400</div>
      <p>Perimeter = 2(${l}) + 10 = <strong>${perim} m</strong> → Fencing = ₹${fCost}</p>
      <p>Area = 5(${l}) = <strong>${area} m²</strong> → Grass Seed = ₹${sCost}</p>
      <p class="text-emerald-300 font-bold">Total Cost at l = ${l}: ₹${total} (= 155×${l} + 400)</p>
    `;
  };
  c9c2s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🔬</span> Univariate Algebraic Expression Dissector
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s2Pick(0)" id="c9c2s2b0" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">3z + 7</button>
    <button type="button" onclick="c9c2s2Pick(1)" id="c9c2s2b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">x² + 5x + 1</button>
    <button type="button" onclick="c9c2s2Pick(2)" id="c9c2s2b2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">5y³ + y² + 2y - 1</button>
    <button type="button" onclick="c9c2s2Pick(3)" id="c9c2s2b3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">-4t + 9</button>
  </div>
  <div id="c9c2s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const ex = [
    { expr:'3z + 7', varName:'z', terms:['3z', '+7'], coeffs:'z → 3', constant:'+7', note:'2 terms in single variable z; linear expression.' },
    { expr:'x² + 5x + 1', varName:'x', terms:['1x²', '+5x', '+1'], coeffs:'x² → 1, x → 5', constant:'+1', note:'3 terms in x; note hidden leading coefficient 1 on x².' },
    { expr:'5y³ + y² + 2y - 1', varName:'y', terms:['5y³', '+1y²', '+2y', '-1'], coeffs:'y³ → 5, y² → 1, y → 2', constant:'-1', note:'4 terms in y; keep negative sign attached to constant term -1!' },
    { expr:'-4t + 9', varName:'t', terms:['-4t', '+9'], coeffs:'t → -4', constant:'+9', note:'2 terms in t; negative coefficient -4 on variable t.' }
  ];
  window.c9c2s2Pick = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c9c2s2b'+k);
      if(b) b.className = k===i ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const d = ex[i];
    document.getElementById('c9c2s2Out').innerHTML = `
      <div class="text-base font-extrabold text-white">${d.expr}</div>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400 block">Variable</span><strong class="text-cyan-300">${d.varName} (Univariate)</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400 block">Terms (${d.terms.length})</span><strong class="text-amber-300">${d.terms.join(', ')}</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400 block">Coefficients</span><strong class="text-emerald-300">${d.coeffs}</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400 block">Constant</span><strong class="text-purple-300">${d.constant}</strong></div>
      </div>
      <p class="text-[11px] text-slate-400">${d.note}</p>
    `;
  };
  c9c2s2Pick(0);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🏷️</span> Univariate Polynomial Degree Classifier (0, 1, 2, 3)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s3Cls(0)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-500/40">8x⁰ (Constant)</button>
    <button type="button" onclick="c9c2s3Cls(1)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40">3z + 7 (Linear)</button>
    <button type="button" onclick="c9c2s3Cls(2)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 border border-purple-500/40">x² + 5x + 1 (Quadratic)</button>
    <button type="button" onclick="c9c2s3Cls(3)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-emerald-500/40">5y³ + y² + 2y - 1 (Cubic)</button>
    <button type="button" onclick="c9c2s3Cls(4)" class="px-2.5 py-1 rounded bg-rose-950/70 hover:bg-rose-900 text-rose-300 border border-rose-500/40">4/x + 3 (Non-Polynomial)</button>
  </div>
  <div id="c9c2s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    ['8x⁰ (= 8)', 'Degree 0 — Constant Polynomial', 'Highest exponent is 0. Value remains constant regardless of x.', 'text-cyan-300'],
    ['3z + 7', 'Degree 1 — Linear Polynomial', 'Highest exponent of z is 1 (z¹). Graph is a straight line with constant first difference 3.', 'text-amber-300'],
    ['x² + 5x + 1', 'Degree 2 — Quadratic Polynomial', 'Highest exponent of x is 2. Consecutive differences change linearly; graph forms a parabola.', 'text-purple-300'],
    ['5y³ + y² + 2y - 1', 'Degree 3 — Cubic Polynomial', 'Highest exponent of y is 3. All exponents (3, 2, 1, 0) are whole numbers.', 'text-emerald-300'],
    ['4/x + 3 (= 4x⁻¹ + 3)', 'NOT a Polynomial!', 'Exponent -1 is negative (not a whole number {0, 1, 2, 3...}), so division by variable disqualifies it.', 'text-rose-400']
  ];
  window.c9c2s3Cls = function(idx){
    const [e, cls, msg, color] = items[idx];
    document.getElementById('c9c2s3Out').innerHTML = `<div class="text-base font-bold text-white">${e}</div><div class="font-bold ${color}">${cls}</div><p>${msg}</p>`;
  };
  c9c2s3Cls(1);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚙️</span> Linear Input-Output Machine: y = ax + b (Perimeter &amp; Club Fees)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s4Mode(4,0,'Square Side (cm)','Perimeter (cm)')" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">Square Perimeter (y = 4x)</button>
    <button type="button" onclick="c9c2s4Mode(50,200,'Matches Played','Total Club Fee (₹)')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Joining ₹200 + Match ₹50x</button>
  </div>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span id="c9c2s4InLbl" class="text-slate-300 font-semibold">Input x:</span> <strong id="c9c2s4XVal" class="text-amber-300">5</strong>
      <input type="range" id="c9c2s4X" min="0" max="15" value="5" oninput="c9c2s4Run()" class="w-full accent-cyan-400 mt-1">
    </label>
    <div id="c9c2s4Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1"></div>
  </div>
</div>
<script>
(function(){
  let ca = 4, cb = 0, inTxt = 'Square Side (cm)', outTxt = 'Perimeter (cm)';
  window.c9c2s4Mode = function(a,b,iL,oL){ ca=a; cb=b; inTxt=iL; outTxt=oL; c9c2s4Run(); };
  window.c9c2s4Run = function(){
    const x = parseInt(document.getElementById('c9c2s4X').value);
    document.getElementById('c9c2s4InLbl').textContent = `${inTxt} (x):`;
    document.getElementById('c9c2s4XVal').textContent = x;
    const y = ca*x + cb;
    document.getElementById('c9c2s4Out').innerHTML = `
      <div class="font-bold text-cyan-300">Function Rule: y = ${ca}x ${cb>=0?'+ '+cb:'- '+Math.abs(cb)}</div>
      <div>${inTxt} = <strong>${x}</strong> → Rate ${ca} × ${x} + Fixed ${cb}</div>
      <div class="text-emerald-300 font-bold text-sm">${outTxt} (y) = ${y}</div>
    `;
  };
  c9c2s4Run();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📊</span> Successive Integer Differences Table (Linear vs Quadratic)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s5Type('lin1')" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Linear: 4x + 3</button>
    <button type="button" onclick="c9c2s5Type('lin2')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Linear: -3x + 20</button>
    <button type="button" onclick="c9c2s5Type('quad')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Quadratic: x² + 1 (Non-Linear)</button>
  </div>
  <div id="c9c2s5Out" class="overflow-x-auto bg-slate-950 rounded-xl border border-slate-800 p-3 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c2s5Type = function(t){
    const xs = [0,1,2,3,4,5];
    const fn = t==='lin1' ? x=>4*x+3 : (t==='lin2' ? x=>-3*x+20 : x=>x*x+1);
    const ys = xs.map(fn);
    const diffs = ys.slice(1).map((v,i)=>v - ys[i]);
    const isLin = t!=='quad';
    const cells = (arr, cls='') => arr.map(v=>`<td class="px-2.5 py-1 border border-slate-800 text-center ${cls}">${v}</td>`).join('');
    document.getElementById('c9c2s5Out').innerHTML = `
      <table class="w-full border-collapse mb-2">
        <tr><th class="px-2 py-1 border border-slate-800 text-left text-slate-400">Input x</th>${cells(xs,'text-cyan-300 font-bold')}</tr>
        <tr><th class="px-2 py-1 border border-slate-800 text-left text-slate-400">Output P(x)</th>${cells(ys,'text-white font-bold')}</tr>
        <tr><th class="px-2 py-1 border border-slate-800 text-left text-amber-300">Difference Δy</th><td class="px-2 py-1 border border-slate-800 text-center text-slate-600">—</td>${cells(diffs, isLin?'text-emerald-300 font-bold':'text-rose-400 font-bold')}</tr>
      </table>
      <div class="${isLin?'text-emerald-300':'text-rose-400'} font-semibold">${isLin ? 'Exact constant successive difference! Confirms degree-1 linear polynomial.' : 'Changing successive differences (+1, +3, +5, +7, +9)! Confirms non-linear quadratic.'}</div>
    `;
  };
  c9c2s5Type('lin1');
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧱</span> Geometric Square Tile Pattern Generalizer (2n − 1)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Step Number n: <strong id="c9c2s6NVal" class="text-emerald-300">4</strong></span>
    <input type="range" id="c9c2s6N" min="1" max="7" value="4" oninput="c9c2s6Draw()" class="w-full accent-emerald-400 mt-1">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s6Svg" viewBox="0 0 180 180" class="w-44 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s6Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s6Draw = function(){
    const n = parseInt(document.getElementById('c9c2s6N').value);
    document.getElementById('c9c2s6NVal').textContent = n;
    const total = 2*n - 1;
    let s = '';
    const sz = 20;
    for(let k=0; k<n; k++){
      s += `<rect x="${18 + k*sz}" y="142" width="${sz-2}" height="${sz-2}" rx="3" fill="${k===0?'#fbbf24':'#22d3ee'}" fill-opacity="0.75" stroke="#fff" stroke-width="1"/>`;
      if(k>0){
        s += `<rect x="18" y="${142 - k*sz}" width="${sz-2}" height="${sz-2}" rx="3" fill="#34d399" fill-opacity="0.75" stroke="#fff" stroke-width="1"/>`;
      }
    }
    document.getElementById('c9c2s6Svg').innerHTML = s;
    document.getElementById('c9c2s6Out').innerHTML = `
      <div class="font-bold text-emerald-300">Step n = ${n} → Total Tiles = 2(${n}) − 1 = ${total}</div>
      <p>Yellow corner tile = <strong>1</strong>; Right arm = <strong>${n-1}</strong> cyan tiles; Top arm = <strong>${n-1}</strong> green tiles.</p>
      <p class="text-cyan-300">Sequence: 1, 3, 5, 7, 9, 11, 13 (constant step +2 per stage!)</p>
    `;
  };
  c9c2s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚕</span> Applied Linear Sequence Switcher
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s7Pick(0)" id="c9c2s7b0" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">Daily Allowance</button>
    <button type="button" onclick="c9c2s7Pick(1)" id="c9c2s7b1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Tiered Taxi Fare</button>
    <button type="button" onclick="c9c2s7Pick(2)" id="c9c2s7b2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Savings Plan</button>
    <button type="button" onclick="c9c2s7Pick(3)" id="c9c2s7b3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Reading Rate</button>
  </div>
  <div id="c9c2s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const probs = [
    ['Daily Allowance Budget: A(d) = 500 − 30d', 'Start with ₹500 and spend ₹30 daily.', 'Term sequence: 500, 470, 440, 410... (step -30/day; hits ₹200 on Day 10).'],
    ['Tiered Taxi Fare (d ≥ 1 km): F(d) = 35 + 12(d − 1) = 12d + 23', '₹35 for first km + ₹12 for every extra km.', 'Sequence for 1, 2, 3, 4 km: ₹35, ₹47, ₹59, ₹71 (constant step +₹12/km).'],
    ['Weekly Savings Accumulation: S(w) = 600 + 150w', 'Open with ₹600 and add ₹150 every week.', 'Sequence: ₹600, ₹750, ₹900, ₹1050... (constant growth +₹150/week).'],
    ['Reading Completion Rate: U(n) = 270 − 18n', '270-page book read at 18 pages/evening.', 'Unread pages: 270, 252, 234... reaching 0 cleanly after n = 15 evenings.']
  ];
  window.c9c2s7Pick = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c9c2s7b'+k);
      if(b) b.className = k===i ? 'px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const [t, desc, seq] = probs[i];
    document.getElementById('c9c2s7Out').innerHTML = `<div class="font-bold text-cyan-300 text-sm">${t}</div><p>${desc}</p><p class="text-emerald-300 font-semibold">${seq}</p>`;
  };
  c9c2s7Pick(0);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📈</span> Linear Growth Simulator: C(d) = 100 + 60d (Positive Rate a &gt; 0)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Day d: <strong id="c9c2s8DVal" class="text-emerald-300">5</strong></span>
    <input type="range" id="c9c2s8D" min="0" max="10" value="5" oninput="c9c2s8Plot()" class="w-full accent-emerald-400 mt-1">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s8Svg" viewBox="0 0 210 150" class="w-56 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s8Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s8Plot = function(){
    const d = parseInt(document.getElementById('c9c2s8D').value);
    document.getElementById('c9c2s8DVal').textContent = d;
    const val = 100 + 60*d;
    const px = 25 + d*16, py = 132 - (val/700)*110;
    let s = `<line x1="25" y1="132" x2="195" y2="132" stroke="#64748b" stroke-width="1.4"/><line x1="25" y1="15" x2="25" y2="132" stroke="#64748b" stroke-width="1.4"/>`;
    s += `<line x1="25" y1="${132-(100/700)*110}" x2="185" y2="${132-(700/700)*110}" stroke="#34d399" stroke-width="2.2"/>`;
    s += `<circle cx="25" cy="${132-(100/700)*110}" r="3.5" fill="#fbbf24"/>`;
    s += `<circle cx="${px}" cy="${py}" r="5" fill="#22d3ee" stroke="#fff" stroke-width="1.2"/>`;
    document.getElementById('c9c2s8Svg').innerHTML = s;
    document.getElementById('c9c2s8Out').innerHTML = `<div class="font-bold text-emerald-300">C(${d}) = 100 + 60(${d}) = ${val}</div><p>Baseline C(0) = <strong>100</strong>; Growth Rate a = <strong>+60 per day</strong> (&gt; 0).</p><p class="text-[11px] text-amber-300">Note: C(2) = 220 while C(4) = 340 ≠ 2×220, because non-zero baseline b = 100 shifts the starting height!</p>`;
  };
  c9c2s8Plot();
})();
</script>
"""
}

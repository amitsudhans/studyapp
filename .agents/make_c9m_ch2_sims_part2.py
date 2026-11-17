#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 2: Introduction to Linear Polynomials
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>📉</span> Linear Decay Explorer (h(t) = 3 − 0.5t, Depreciation, Population &amp; Phone Balance)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s9Pick(0)" id="c9c2s9b0" class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-semibold">Candle h(t)=3-0.5t</button>
    <button type="button" onclick="c9c2s9Pick(1)" id="c9c2s9b1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Vehicle Depreciation</button>
    <button type="button" onclick="c9c2s9Pick(2)" id="c9c2s9b2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Village Population</button>
    <button type="button" onclick="c9c2s9Pick(3)" id="c9c2s9b3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Prepaid Balance</button>
  </div>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span id="c9c2s9TLbl" class="text-slate-300 font-semibold">Time t:</span> <strong id="c9c2s9TVal" class="text-rose-300">2</strong>
    <input type="range" id="c9c2s9T" min="0" max="8" value="2" oninput="c9c2s9Draw()" class="w-full accent-rose-400 mt-1">
  </label>
  <div id="c9c2s9Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  let cur = 0;
  const models = [
    { name:'Candle Height h(t) = 3 − 0.5t dm', lbl:'Hours Burned (t)', fn:t=>Math.max(0, 3-0.5*t).toFixed(1)+' dm', zero:'Melts completely at t = 6 hours' },
    { name:'Vehicle Value V(t) = 80,000 − 6,000t', lbl:'Years Owned (t)', fn:t=>'₹'+(80000-6000*t).toLocaleString(), zero:'Drops ₹6,000 steadily each year' },
    { name:'Village Population P(t) = 4,000 − 40t', lbl:'Years Elapsed (t)', fn:t=>(4000-40*t).toLocaleString()+' people', zero:'Declines by 40 residents per year' },
    { name:'Prepaid Phone B(m) = 200 − 5m (×5 min)', lbl:'5-Min Blocks (m/5)', fn:t=>'₹'+Math.max(0, 200-25*t), zero:'Hits ₹0 after 40 total minutes (8 blocks)' }
  ];
  window.c9c2s9Pick = function(i){
    cur = i;
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c9c2s9b'+k);
      if(b) b.className = k===i ? 'px-2 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    c9c2s9Draw();
  };
  window.c9c2s9Draw = function(){
    const t = parseInt(document.getElementById('c9c2s9T').value);
    const m = models[cur];
    document.getElementById('c9c2s9TLbl').textContent = m.lbl + ':';
    document.getElementById('c9c2s9TVal').textContent = t;
    document.getElementById('c9c2s9Out').innerHTML = `<div class="font-bold text-rose-300">${m.name}</div><p>At t = ${t} → Value = <strong class="text-white text-sm">${m.fn(t)}</strong></p><p class="text-[11px] text-amber-300">${m.zero} (Negative slope a &lt; 0 drives linear decay!)</p>`;
  };
  c9c2s9Pick(0);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧮</span> Simultaneous Equation Solver for y = ax + b from Two Data Points
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">x₁: <input type="number" id="c9c2s10x1" value="2" oninput="c9c2s10Solve()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 text-cyan-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">y₁: <input type="number" id="c9c2s10y1" value="11" oninput="c9c2s10Solve()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 text-cyan-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">x₂: <input type="number" id="c9c2s10x2" value="5" oninput="c9c2s10Solve()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 text-amber-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">y₂: <input type="number" id="c9c2s10y2" value="23" oninput="c9c2s10Solve()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 text-amber-300 font-bold"></label>
  </div>
  <div id="c9c2s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c2s10Solve = function(){
    const x1 = parseFloat(document.getElementById('c9c2s10x1').value) || 0;
    const y1 = parseFloat(document.getElementById('c9c2s10y1').value) || 0;
    const x2 = parseFloat(document.getElementById('c9c2s10x2').value) || 0;
    const y2 = parseFloat(document.getElementById('c9c2s10y2').value) || 0;
    if(x1===x2){
      document.getElementById('c9c2s10Out').innerHTML = `<span class="text-rose-400 font-bold">Choose x₁ ≠ x₂ so Δx ≠ 0!</span>`;
      return;
    }
    const a = (y2 - y1) / (x2 - x1);
    const b = y1 - a * x1;
    const aStr = Number.isInteger(a) ? a : a.toFixed(2);
    const bStr = Number.isInteger(b) ? b : b.toFixed(2);
    document.getElementById('c9c2s10Out').innerHTML = `
      <div>System: (1) ${x1}a + b = ${y1} and (2) ${x2}a + b = ${y2}</div>
      <div>Subtract (2) − (1) to eliminate b: (${x2} − ${x1})a = ${y2} − ${y1} ⇒ <strong>a = ${aStr}</strong></div>
      <div>Substitute back into (1): b = ${y1} − (${aStr})(${x1}) = <strong>${bStr}</strong></div>
      <div class="text-emerald-300 font-bold text-sm">Linear Relationship: y = ${aStr}x ${b>=0?'+ '+bStr:'− '+Math.abs(bStr)}</div>
    `;
  };
  c9c2s10Solve();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🌡️</span> Pricing Solvers &amp; Temperature Conversion (°C ↔ °F)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s11Show('telecom')" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Telecom Data Plan</button>
    <button type="button" onclick="c9c2s11Show('gym')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Gym Court Rental</button>
    <button type="button" onclick="c9c2s11Show('modules')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Learning Modules</button>
    <button type="button" onclick="c9c2s11Show('temp')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">°C to °F Converter</button>
  </div>
  <div id="c9c2s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c2s11Show = function(k){
    const box = document.getElementById('c9c2s11Out');
    if(k==='telecom'){
      box.innerHTML = `<div class="font-bold text-cyan-300">Telecom Data Plan: (10 GB, ₹450) and (18 GB, ₹690)</div><p>a = (690 − 450) / (18 − 10) = 240 / 8 = <strong>₹30/GB</strong>; b = 450 − 10(30) = <strong>₹150 fixed fee</strong>.</p><p class="text-emerald-300 font-bold">Model: Cost(g) = 30g + 150</p>`;
    } else if(k==='gym'){
      box.innerHTML = `<div class="font-bold text-cyan-300">Gym Court Rental: (3 hr, ₹600) and (7 hr, ₹1200)</div><p>a = (1200 − 600) / (7 − 3) = 600 / 4 = <strong>₹150/hr</strong>; b = 600 − 3(150) = <strong>₹150 booking deposit</strong>.</p><p class="text-emerald-300 font-bold">Model: Rent(h) = 150h + 150</p>`;
    } else if(k==='modules'){
      box.innerHTML = `<div class="font-bold text-cyan-300">Online Learning Modules: (4 mod, ₹1100) and (9 mod, ₹2100)</div><p>a = (2100 − 1100) / (9 − 4) = 1000 / 5 = <strong>₹200/module</strong>; b = 1100 − 800 = <strong>₹300 registration</strong>.</p><p class="text-emerald-300 font-bold">Model: Fee(m) = 200m + 300</p>`;
    } else {
      box.innerHTML = `<div class="font-bold text-amber-300">Interactive Celsius to Fahrenheit: F = (9/5)C + 32</div><label class="block">Celsius (°C): <input type="number" id="c9c2s11C" value="35" oninput="document.getElementById('c9c2s11F').textContent = ((9/5)*parseFloat(this.value||0)+32).toFixed(1) + ' °F'" class="w-16 bg-slate-900 border border-slate-700 rounded px-1.5 text-cyan-300 font-bold"> → <strong id="c9c2s11F" class="text-emerald-300 text-sm">95.0 °F</strong></label><p class="text-[11px] text-slate-400">Solved from boiling (100, 212) and freezing (0, 32): a = 180/100 = 9/5, b = 32.</p>`;
    }
  };
  c9c2s11Show('telecom');
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Coordinate Plotting &amp; Straight-Line Fit: y = 2x − 1
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s12Test(0,-1)" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Test (0, -1)</button>
    <button type="button" onclick="c9c2s12Test(2,3)" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Test (2, 3)</button>
    <button type="button" onclick="c9c2s12Test(-1,-3)" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Test (-1, -3)</button>
    <button type="button" onclick="c9c2s12Test(2,4)" class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">Test Off-Line (2, 4)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s12Svg" viewBox="0 0 180 180" class="w-44 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s12Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s12Test = function(tx, ty){
    const sc = 15, ox = 90, oy = 90;
    const onLine = ty === 2*tx - 1;
    let s = `<line x1="15" y1="${oy}" x2="165" y2="${oy}" stroke="#64748b" stroke-width="1.3"/><line x1="${ox}" y1="15" x2="${ox}" y2="165" stroke="#64748b" stroke-width="1.3"/>`;
    s += `<line x1="${ox-3*sc}" y1="${oy-(-7)*sc}" x2="${ox+4*sc}" y2="${oy-(7)*sc}" stroke="#22d3ee" stroke-width="2.2"/>`;
    [[0,-1],[2,3],[-1,-3]].forEach(([x,y])=>{ s += `<circle cx="${ox+x*sc}" cy="${oy-y*sc}" r="3.5" fill="#fbbf24"/>`; });
    s += `<circle cx="${ox+tx*sc}" cy="${oy-ty*sc}" r="5.5" fill="${onLine?'#34d399':'#fb7185'}" stroke="#fff" stroke-width="1.5"/>`;
    document.getElementById('c9c2s12Svg').innerHTML = s;
    document.getElementById('c9c2s12Out').innerHTML = `<div class="font-bold text-cyan-300">Testing Point (${tx}, ${ty}) in y = 2x − 1</div><p>Evaluate 2(${tx}) − 1 = <strong>${2*tx-1}</strong> vs given y = <strong>${ty}</strong>.</p><p class="font-bold ${onLine?'text-emerald-300':'text-rose-400'}">${onLine?'EXACT MATCH! Point lies directly on the straight line!':'MISMATCH! Point does NOT lie on the line.'}</p>`;
  };
  c9c2s12Test(2,3);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>📐</span> Origin-Passing Lines y = ax: Steepness |a| &amp; Sign (Growth vs Decay)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s13Set(3)" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">a = 3 (Steep Growth)</button>
    <button type="button" onclick="c9c2s13Set(1)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">a = 1 (45° Diagonal)</button>
    <button type="button" onclick="c9c2s13Set(0.25)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">a = 0.25 (Flat Growth)</button>
    <button type="button" onclick="c9c2s13Set(-2)" class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">a = -2 (Linear Decay)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s13Svg" viewBox="0 0 180 180" class="w-44 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s13Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s13Set = function(a){
    const ox=90, oy=90, sc=16;
    const x1=-4, y1=a*x1, x2=4, y2=a*x2;
    let s = `<line x1="15" y1="${oy}" x2="165" y2="${oy}" stroke="#64748b" stroke-width="1.3"/><line x1="${ox}" y1="15" x2="${ox}" y2="165" stroke="#64748b" stroke-width="1.3"/>`;
    s += `<line x1="${ox-4*sc}" y1="${oy+4*sc}" x2="${ox+4*sc}" y2="${oy-4*sc}" stroke="#334155" stroke-width="1" stroke-dasharray="3 3"/>`;
    s += `<line x1="${ox+x1*sc}" y1="${oy-y1*sc}" x2="${ox+x2*sc}" y2="${oy-y2*sc}" stroke="${a>0?'#34d399':'#fb7185'}" stroke-width="2.6"/>`;
    s += `<circle cx="${ox}" cy="${oy}" r="4" fill="#fbbf24"/>`;
    document.getElementById('c9c2s13Svg').innerHTML = s;
    const mag = Math.abs(a)>1 ? 'Steeper than y = x (|a| > 1)' : (Math.abs(a)<1 ? 'Flatter than y = x (|a| < 1)' : 'Exact 45° diagonal (|a| = 1)');
    document.getElementById('c9c2s13Out').innerHTML = `<div class="font-bold text-purple-300">Line y = ${a}x through Origin (0, 0)</div><p>Magnitude: <strong>${mag}</strong></p><p class="${a>0?'text-emerald-300':'text-rose-400'} font-semibold">${a>0?'Positive slope (a > 0) → Linear Growth (rises left-to-right)':'Negative slope (a < 0) → Linear Decay (falls left-to-right)'}</p>`;
  };
  c9c2s13Set(3);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪜</span> Slope (a) &amp; y-Intercept (b): Parallel Lines with Equal Slope
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Shared Slope (a): <strong id="c9c2s14AVal" class="text-cyan-300">1.5</strong></span>
      <input type="range" id="c9c2s14A" min="-2" max="2" step="0.5" value="1.5" oninput="c9c2s14Plot()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Line 2 y-Intercept (b₂): <strong id="c9c2s14BVal" class="text-amber-300">3</strong></span>
      <input type="range" id="c9c2s14B" min="-4" max="4" step="1" value="3" oninput="c9c2s14Plot()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c2s14Svg" viewBox="0 0 180 180" class="w-44 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c2s14Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c2s14Plot = function(){
    const a = parseFloat(document.getElementById('c9c2s14A').value);
    const b = parseInt(document.getElementById('c9c2s14B').value);
    document.getElementById('c9c2s14AVal').textContent = a;
    document.getElementById('c9c2s14BVal').textContent = b;
    const ox=90, oy=90, sc=14;
    let s = `<line x1="15" y1="${oy}" x2="165" y2="${oy}" stroke="#64748b" stroke-width="1.3"/><line x1="${ox}" y1="15" x2="${ox}" y2="165" stroke="#64748b" stroke-width="1.3"/>`;
    s += `<line x1="${ox-5*sc}" y1="${oy-(-5*a)*sc}" x2="${ox+5*sc}" y2="${oy-(5*a)*sc}" stroke="#22d3ee" stroke-width="2.2"/>`;
    s += `<line x1="${ox-5*sc}" y1="${oy-(-5*a+b)*sc}" x2="${ox+5*sc}" y2="${oy-(5*a+b)*sc}" stroke="#fbbf24" stroke-width="2.2"/>`;
    s += `<circle cx="${ox}" cy="${oy-b*sc}" r="4.5" fill="#fbbf24" stroke="#fff"/>`;
    document.getElementById('c9c2s14Svg').innerHTML = s;
    document.getElementById('c9c2s14Out').innerHTML = `<div class="font-bold text-cyan-300">Line 1: y = ${a}x (through (0,0))</div><div class="font-bold text-amber-300">Line 2: y = ${a}x ${b>=0?'+ '+b:'− '+Math.abs(b)} (crosses y-axis at (0, ${b}))</div><p class="text-emerald-300 font-semibold">${b===0?'b = 0: Both lines coincide!':'Identical slope a = '+a+' with b ≠ 0 → Parallel lines never intersecting!'}</p>`;
  };
  c9c2s14Plot();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⬡</span> Matchstick Hexagon Chain (5n + 1) &amp; Applied Exercise Lab
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Joined Hexagons (n): <strong id="c9c2s15NVal" class="text-amber-300">4</strong></span>
    <input type="range" id="c9c2s15N" min="1" max="8" value="4" oninput="c9c2s15Draw()" class="w-full accent-amber-400 mt-1">
  </label>
  <div id="c9c2s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c2s15Draw = function(){
    const n = parseInt(document.getElementById('c9c2s15N').value);
    document.getElementById('c9c2s15NVal').textContent = n;
    const sticks = 5*n + 1;
    document.getElementById('c9c2s15Out').innerHTML = `
      <div class="font-bold text-amber-300 text-sm">Joined Matchstick Hexagons (n = ${n}) → ${sticks} Matchsticks</div>
      <p>1st hexagon = <strong>6</strong> sticks; each of the remaining (${n-1}) joined hexagons shares 1 edge and adds <strong>5</strong> sticks.</p>
      <p class="text-cyan-300 font-semibold">Linear Rule: 6 + 5(n − 1) = 5n + 1 → At n = ${n}, 5(${n}) + 1 = ${sticks} sticks!</p>
      <p class="text-[11px] text-emerald-300">Also verify Kelvin→Fahrenheit slope: F = (9/5)(K − 273.15) + 32 rises 1.8 °F per 1 K.</p>
    `;
  };
  c9c2s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🗂️</span> Chapter 2 Complete Synthesis Matrix
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c2s16Tab(0)" id="c9c2s16t0" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">1. Degree &amp; Terms</button>
    <button type="button" onclick="c9c2s16Tab(1)" id="c9c2s16t1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2. Patterns &amp; Differences</button>
    <button type="button" onclick="c9c2s16Tab(2)" id="c9c2s16t2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">3. Growth, Decay &amp; Solvers</button>
    <button type="button" onclick="c9c2s16Tab(3)" id="c9c2s16t3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">4. Slope &amp; Parallel Lines</button>
  </div>
  <div id="c9c2s16Body" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const tabs = [
    ['Univariate Polynomial Classification', [
      '• Components: variable letter, terms separated by +/−, numeric coefficients, constant term',
      '• Constant (Degree 0): e.g., 8x⁰ | Linear (Degree 1): e.g., 3z + 7',
      '• Quadratic (Degree 2): e.g., x² + 5x + 1 | Cubic (Degree 3): e.g., 5y³ + y² + 2y − 1',
      '• Exponents must be whole numbers {0, 1, 2, 3...} — never negative or fractional'
    ]],
    ['Linear Polynomials & Pattern Sequences', [
      '• Standard form: y = ax + b with a ≠ 0 (Perimeter 4x; Joining Fee + Match Fee)',
      '• Constant Successive Difference: P(x + 1) − P(x) = a for all consecutive integers',
      '• Growing Square Tiles: 2n − 1 | Matchstick Hexagons: 5n + 1',
      '• Models daily allowance, tiered taxi fare, weekly savings, and reading rates'
    ]],
    ['Linear Growth, Decay & Equation Solvers', [
      '• Linear Growth (a > 0): e.g., C(d) = 100 + 60d, plant growth, bank deposits',
      '• Linear Decay (a < 0): e.g., h(t) = 3 − 0.5t, vehicle depreciation, village population, phone balance',
      '• Two-Point Solver: a = (y₂ − y₁)/(x₂ − x₁), then b = y₁ − ax₁ eliminates b first',
      '• Applications: telecom plans, learning modules, gym rentals, °C↔°F, Kelvin↔°F'
    ]],
    ['Visualising y = ax + b on Cartesian Plane', [
      '• Every degree-1 solution set (x, ax + b) plots as a continuous straight line',
      '• Origin lines y = ax pass through (0, 0): steeper if |a| > 1, flatter if |a| < 1',
      '• Positive slope (a > 0) rises left-to-right; negative slope (a < 0) drops left-to-right',
      '• y-intercept (0, b) shifts line vertically; equal slopes (a₁ = a₂, b₁ ≠ b₂) stay parallel'
    ]]
  ];
  window.c9c2s16Tab = function(idx){
    [0,1,2,3].forEach(i => {
      const b = document.getElementById('c9c2s16t'+i);
      if(b) b.className = i===idx ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const [head, lines] = tabs[idx];
    document.getElementById('c9c2s16Body').innerHTML = `<div class="font-bold text-cyan-300 text-sm">${head}</div>` + lines.map(l => `<div>${l}</div>`).join('');
  };
  c9c2s16Tab(0);
})();
</script>
"""
}

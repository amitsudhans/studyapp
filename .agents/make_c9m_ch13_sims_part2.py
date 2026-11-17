#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 13: Two Variables, One Line
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Elimination Method Step-by-Step Walkthrough
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>System: 3x + 2y = 19 &amp; 5x − 3y = 19</span>
      <span id="c9c13s9Lbl" class="text-amber-300 font-bold">Step 1 / 4</span>
    </div>
    <input id="c9c13s9Step" type="range" min="1" max="4" value="1" oninput="c9c13s9Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c13s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const steps = [
    '<span class="text-cyan-300 font-bold">Step 1 (Scale to Match y):</span> Multiply Eq 1 by 3 → 9x + 6y = 57; Eq 2 by 2 → 10x − 6y = 38.',
    '<span class="text-amber-300 font-bold">Step 2 (Add Vertically):</span> (+6y) and (−6y) cancel! 19x = 95.',
    '<span class="text-emerald-300 font-bold">Step 3 (Solve x):</span> x = 95 / 19 = 5.',
    '<span class="text-emerald-400 font-bold">Step 4 (Find y):</span> 3(5) + 2y = 19 ⇒ 2y = 4 ⇒ y = 2. Solution: (5, 2)!'
  ];
  window.c9c13s9Draw = function(){
    const s = parseInt(document.getElementById('c9c13s9Step').value, 10);
    document.getElementById('c9c13s9Lbl').textContent = 'Step ' + s + ' / 4';
    document.getElementById('c9c13s9Out').innerHTML = steps.slice(0, s).map(x => `<div class="p-2 rounded bg-slate-900 border border-slate-800">${x}</div>`).join('');
  };
  c9c13s9Draw();
})();
</script>""",

    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔍</span> Coefficient Ratio Classifier: 2x + 3y = 6 vs a₂x + b₂y = c₂
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>a₂:</span><span id="c9c13s10AL" class="text-cyan-300 font-bold">4</span></div>
      <input id="c9c13s10A" type="range" min="1" max="8" value="4" oninput="c9c13s10Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>b₂:</span><span id="c9c13s10BL" class="text-emerald-300 font-bold">6</span></div>
      <input id="c9c13s10B" type="range" min="1" max="9" value="6" oninput="c9c13s10Draw()" class="w-full accent-emerald-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>c₂:</span><span id="c9c13s10CL" class="text-amber-300 font-bold">12</span></div>
      <input id="c9c13s10C" type="range" min="4" max="18" value="12" oninput="c9c13s10Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c13s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c13s10Draw = function(){
    const a2 = parseInt(document.getElementById('c9c13s10A').value, 10);
    const b2 = parseInt(document.getElementById('c9c13s10B').value, 10);
    const c2 = parseInt(document.getElementById('c9c13s10C').value, 10);
    document.getElementById('c9c13s10AL').textContent = a2;
    document.getElementById('c9c13s10BL').textContent = b2;
    document.getElementById('c9c13s10CL').textContent = c2;
    const rA = 2/a2, rB = 3/b2, rC = 6/c2;
    const eqAB = Math.abs(rA - rB) < 1e-9;
    const eqBC = Math.abs(rB - rC) < 1e-9;
    let verdict = '';
    if (!eqAB) verdict = '<span class="text-emerald-400 font-bold">UNIQUE SOLUTION (Intersecting Lines):</span> a₁/a₂ ≠ b₁/b₂';
    else if (eqBC) verdict = '<span class="text-cyan-300 font-bold">INFINITELY MANY SOLUTIONS (Coincident Lines):</span> a₁/a₂ = b₁/b₂ = c₁/c₂';
    else verdict = '<span class="text-rose-400 font-bold">NO SOLUTION (Parallel Lines):</span> a₁/a₂ = b₁/b₂ ≠ c₁/c₂';
    document.getElementById('c9c13s10Out').innerHTML = `
      <div>System: <span class="font-bold text-white">2x + 3y = 6</span> and <span class="font-bold text-white">${a2}x + ${b2}y = ${c2}</span></div>
      <div class="flex gap-4 text-slate-300"><span>a₁/a₂ = ${rA.toFixed(2)}</span><span>b₁/b₂ = ${rB.toFixed(2)}</span><span>c₁/c₂ = ${rC.toFixed(2)}</span></div>
      <div class="p-2.5 rounded bg-slate-900 border border-slate-800">${verdict}</div>`;
  };
  c9c13s10Draw();
})();
</script>""",

    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📜</span> History of Linear Systems Across Civilisations
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c13s11Set(0)" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Babylon (c. 2000 BCE)</button>
    <button onclick="c9c13s11Set(1)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">China: Fangcheng</button>
    <button onclick="c9c13s11Set(2)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">India: Āryabhaṭa &amp; Brahmagupta</button>
  </div>
  <div id="c9c13s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const eras = [
    '<div class="text-amber-300 font-bold">Old Babylonian Clay Tablets (c. 2000 BCE)</div><div>Scribe tablets posed two-unknown field and silver weight puzzles (such as length + width = S, length − width = D) solved via systematic verbal balancing recipes.</div>',
    '<div class="text-emerald-400 font-bold">Han Dynasty China: The Nine Chapters (Fangcheng)</div><div>Arranged linear coefficients as counting rods in rectangular arrays and eliminated columns step by step—inventing matrix row reduction and negative numbers ~1,800 years before Gauss.</div>',
    '<div class="text-cyan-300 font-bold">Classical India: Āryabhaṭa (499 CE) &amp; Brahmagupta (628 CE)</div><div>Developed systematic rules for multi-unknown linear equations (avyakta-ganita) and integer linear equations (kuttaka) for astronomy and commerce.</div>'
  ];
  window.c9c13s11Set = function(i){
    document.getElementById('c9c13s11Out').innerHTML = eras[i];
  };
  c9c13s11Set(0);
})();
</script>""",

    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Graphical Intersection Configurations
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c13s12Set('inter')" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Intersecting (Unique)</button>
    <button onclick="c9c13s12Set('par')" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Parallel (None)</button>
    <button onclick="c9c13s12Set('coin')" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Coincident (Infinite)</button>
  </div>
  <svg id="c9c13s12Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c13s12Set = function(m){
    const svg = document.getElementById('c9c13s12Svg');
    let content = '<line x1="30" y1="95" x2="330" y2="95" stroke="#334155" stroke-width="1"/><line x1="180" y1="15" x2="180" y2="160" stroke="#334155" stroke-width="1"/>';
    if (m === 'inter') {
      content += '<line x1="70" y1="145" x2="290" y2="35" stroke="#38bdf8" stroke-width="3"/><line x1="70" y1="45" x2="290" y2="145" stroke="#34d399" stroke-width="3"/><circle cx="190" cy="90" r="6" fill="#fbbf24"/><text x="180" y="175" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Intersecting Lines ⇒ 1 Unique Solution (Consistent)</text>';
    } else if (m === 'par') {
      content += '<line x1="70" y1="125" x2="290" y2="35" stroke="#38bdf8" stroke-width="3"/><line x1="70" y1="155" x2="290" y2="65" stroke="#fb7185" stroke-width="3"/><text x="180" y="175" text-anchor="middle" fill="#fb7185" font-size="11" font-weight="bold">Parallel Lines ⇒ 0 Solutions (Inconsistent)</text>';
    } else {
      content += '<line x1="70" y1="140" x2="290" y2="40" stroke="#38bdf8" stroke-width="6"/><line x1="70" y1="140" x2="290" y2="40" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6,4"/><text x="180" y="175" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Coincident Lines ⇒ Infinitely Many Solutions (Dependent)</text>';
    }
    svg.innerHTML = content;
  };
  c9c13s12Set('inter');
})();
</script>""",

    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>♿</span> Ramp Gradient (1:12) &amp; Celsius–Fahrenheit Converter
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Ramp Rise (m):</span><span id="c9c13s13RL" class="text-cyan-300 font-bold">0.6 m</span></div>
      <input id="c9c13s13R" type="range" min="0.2" max="1.2" step="0.1" value="0.6" oninput="c9c13s13Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Celsius (°C):</span><span id="c9c13s13CL" class="text-amber-300 font-bold">-40°C</span></div>
      <input id="c9c13s13C" type="range" min="-50" max="100" step="5" value="-40" oninput="c9c13s13Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c13s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 grid grid-cols-1 sm:grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9c13s13Draw = function(){
    const rise = parseFloat(document.getElementById('c9c13s13R').value);
    const c = parseFloat(document.getElementById('c9c13s13C').value);
    const run = (rise * 12).toFixed(1);
    const f = ((9/5)*c + 32).toFixed(1);
    document.getElementById('c9c13s13RL').textContent = rise.toFixed(1) + ' m';
    document.getElementById('c9c13s13CL').textContent = c + '°C';
    document.getElementById('c9c13s13Out').innerHTML = `
      <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
        <div class="text-slate-400">Wheelchair Ramp (m = 1/12)</div>
        <div class="text-base font-bold text-cyan-300">Min Run = ${run} m</div>
      </div>
      <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
        <div class="text-slate-400">F = (9/5)C + 32</div>
        <div class="text-base font-bold text-amber-300">${c}°C = ${f}°F ${c===-40?'(Equal!)':''}</div>
      </div>`;
  };
  c9c13s13Draw();
})();
</script>""",

    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📱</span> Mobile Data Plan Crossover Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Monthly Data Usage x (GB):</span>
      <span id="c9c13s14Lbl" class="text-amber-300 font-bold">50 GB (Break-Even!)</span>
    </div>
    <input id="c9c13s14X" type="range" min="10" max="100" step="5" value="50" oninput="c9c13s14Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c13s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c13s14Draw = function(){
    const x = parseInt(document.getElementById('c9c13s14X').value, 10);
    const pA = 200 + 2*x, pB = 100 + 4*x;
    document.getElementById('c9c13s14Lbl').textContent = x + ' GB' + (x===50?' (Exact Crossover!)':'');
    const best = pA < pB ? 'Plan A is cheaper!' : (pB < pA ? 'Plan B is cheaper!' : 'Both plans cost ₹300!');
    document.getElementById('c9c13s14Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2">
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800"><span class="text-cyan-300 font-bold">Plan A (2x + 200):</span> ₹${pA}</div>
        <div class="p-2.5 rounded bg-slate-900 border border-slate-800"><span class="text-emerald-300 font-bold">Plan B (4x + 100):</span> ₹${pB}</div>
      </div>
      <div class="text-amber-300 font-bold">${best}</div>`;
  };
  c9c13s14Draw();
})();
</script>""",

    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚆</span> Train Speed-Distance Relative Motion Solver
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Sum u + v (km/h):</span><span id="c9c13s15SL" class="text-cyan-300 font-bold">100</span></div>
      <input id="c9c13s15S" type="range" min="60" max="160" step="10" value="100" oninput="c9c13s15Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Diff u − v (km/h):</span><span id="c9c13s15DL" class="text-amber-300 font-bold">20</span></div>
      <input id="c9c13s15D" type="range" min="10" max="50" step="10" value="20" oninput="c9c13s15Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c13s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c13s15Draw = function(){
    const s = parseInt(document.getElementById('c9c13s15S').value, 10);
    const d = parseInt(document.getElementById('c9c13s15D').value, 10);
    document.getElementById('c9c13s15SL').textContent = s;
    document.getElementById('c9c13s15DL').textContent = d;
    const u = (s+d)/2, v = (s-d)/2;
    document.getElementById('c9c13s15Out').innerHTML =
      'Adding (u + v = ' + s + ') and (u − v = ' + d + ') gives 2u = ' + (s+d) + ' ⇒ <span class="text-emerald-400 font-bold">Train 1 u = ' + u + ' km/h</span>, <span class="text-cyan-300 font-bold">Train 2 v = ' + v + ' km/h</span>.';
  };
  c9c13s15Draw();
})();
</script>""",

    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏆</span> Chapter 13 Quick-Reference Formula Verifier
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9c13s16Set(0)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">1. Standard Form</button>
    <button onclick="c9c13s16Set(1)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">2. Slope-Intercept</button>
    <button onclick="c9c13s16Set(2)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">3. Unique Solution</button>
    <button onclick="c9c13s16Set(3)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">4. Infinite vs None</button>
  </div>
  <div id="c9c13s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const notes = [
    '<span class="text-cyan-300 font-bold">Standard Form:</span> ax + by + c = 0 (a, b not both 0). Single-variable x = k becomes 1x + 0y − k = 0.',
    '<span class="text-emerald-400 font-bold">Slope-Intercept Form:</span> y = mx + d, where slope m = (y₂ − y₁)/(x₂ − x₁) = −a/b and y-intercept d = −c/b.',
    '<span class="text-amber-300 font-bold">Unique Solution:</span> a₁/a₂ ≠ b₁/b₂ ⇒ Intersecting lines meeting at one shared point (consistent).',
    '<span class="text-rose-400 font-bold">Infinite vs No Solution:</span> All three ratios equal (a₁/a₂ = b₁/b₂ = c₁/c₂) ⇒ Coincident (infinite); a₁/a₂ = b₁/b₂ ≠ c₁/c₂ ⇒ Parallel (none).'
  ];
  window.c9c13s16Set = function(i){
    document.getElementById('c9c13s16Out').innerHTML = notes[i];
  };
  c9c13s16Set(0);
})();
</script>""",
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 10: Proportional Reasoning-2
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🚗</span> Fixed Distance Speed vs Time Simulator (s·t = 90 km)
  </h3>
  <label class="block text-xs text-slate-300">Driving Speed s (km/h): <span id="c10s9SVal" class="font-bold text-cyan-300">30 km/h</span>
    <input id="c10s9S" type="range" min="15" max="90" step="5" value="30" oninput="c10s9Calc()" class="mt-1 w-full accent-cyan-400">
  </label>
  <div id="c10s9Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  window.c10s9Calc = function(){
    const s = parseFloat(document.getElementById('c10s9S').value) || 30;
    const t = 90 / s;
    document.getElementById('c10s9SVal').textContent = s + ' km/h';
    document.getElementById('c10s9Out').innerHTML = `
      <div>Constant Distance = <b>90 km</b> | Travel Time t = 90 ÷ ${s} = <b class="text-emerald-300 text-sm">${t.toFixed(2).replace(/\\.00$/,'')} hours</b></div>
      <div class="h-3 bg-slate-800 rounded-full overflow-hidden"><div class="h-full bg-amber-400 transition-all" style="width:${Math.min(100, (t/6)*100)}%"></div></div>
      <div class="text-slate-400">Check product: ${s} × ${t.toFixed(2).replace(/\\.00$/,'')} = 90 km (double speed to 60 km/h → halves time to 1.5 hrs!)</div>`;
  };
  window.c10s9Calc();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>🏕️</span> Workforce & Food Provisions Inverse Solver
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c10s10Set(12,10,15,'Workers / Road Days')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Road Crew</button>
      <button type="button" onclick="c10s10Set(40,18,60,'Hikers / Food Days')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Food Provisions</button>
    </div>
  </div>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Initial Headcount<input id="c10s10W1" type="number" value="40" min="1" oninput="c10s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Initial Days<input id="c10s10T1" type="number" value="18" min="1" oninput="c10s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">New Headcount<input id="c10s10W2" type="number" value="60" min="1" oninput="c10s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c10s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs"></div>
</div>
<script>
(function(){
  let lbl = 'Hikers / Food Days';
  window.c10s10Set = function(w1, t1, w2, title){
    lbl = title;
    document.getElementById('c10s10W1').value = w1;
    document.getElementById('c10s10T1').value = t1;
    document.getElementById('c10s10W2').value = w2;
    window.c10s10Calc();
  };
  window.c10s10Calc = function(){
    const w1 = Math.max(1, parseFloat(document.getElementById('c10s10W1').value) || 1);
    const t1 = Math.max(1, parseFloat(document.getElementById('c10s10T1').value) || 1);
    const w2 = Math.max(1, parseFloat(document.getElementById('c10s10W2').value) || 1);
    const total = w1 * t1;
    const t2 = total / w2;
    document.getElementById('c10s10Out').innerHTML = `<span class="text-slate-400">${lbl}:</span> Total Person-Days = <b>${total}</b> → With <b>${w2}</b> people: Duration = <b class="text-emerald-300">${t2.toFixed(2).replace(/\\.00$/,'')} days</b>`;
  };
  window.c10s10Calc();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🖌️</span> Combined Unequal Work Rates (1/A + 1/B = 1/T)
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Painter A Solo Time (hrs): <input id="c10s11A" type="number" value="6" min="1" max="50" oninput="c10s11Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Painter B Solo Time (hrs): <input id="c10s11B" type="number" value="3" min="1" max="50" oninput="c10s11Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c10s11Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c10s11Calc = function(){
    const a = Math.max(1, parseFloat(document.getElementById('c10s11A').value) || 6);
    const b = Math.max(1, parseFloat(document.getElementById('c10s11B').value) || 3);
    const rate = 1/a + 1/b;
    const t = 1 / rate;
    document.getElementById('c10s11Out').innerHTML = `
      <div>1-Hour Output: Painter A = <b>1/${a}</b> + Painter B = <b>1/${b}</b> → Combined = <b>${(rate*100).toFixed(1)}%</b>/hr</div>
      <div>Together Time = 1 ÷ (1/${a} + 1/${b}) = <b class="text-emerald-300 text-sm">${t.toFixed(2).replace(/\\.00$/,'')} hours</b> (faster than either solo!)</div>`;
  };
  window.c10s11Calc();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🚰</span> Pump Flow Rates & Multi-Pipe Cistern Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">600 L Tank: Single Pump Flow Rate</div>
      <label class="text-slate-400">Flow (L/min): <input id="c10s12F" type="range" min="10" max="60" step="5" value="20" oninput="c10s12Flow()" class="mt-1 w-full accent-cyan-400"></label>
      <div id="c10s12FlowOut" class="text-emerald-300 font-bold"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Combined Different Pipes (hrs)</div>
      <div class="grid grid-cols-2 gap-2">
        <label class="text-slate-400">Pipe 1 (h)<input id="c10s12P1" type="number" value="4" min="1" oninput="c10s12Dual()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">Pipe 2 (h)<input id="c10s12P2" type="number" value="6" min="1" oninput="c10s12Dual()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c10s12DualOut" class="text-amber-200 font-bold"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c10s12Flow = function(){
    const f = parseFloat(document.getElementById('c10s12F').value) || 20;
    document.getElementById('c10s12FlowOut').textContent = `${f} L/min → Fills 600 L in ${(600/f).toFixed(1).replace(/\\.0$/,'')} min`;
  };
  window.c10s12Dual = function(){
    const p1 = Math.max(1, parseFloat(document.getElementById('c10s12P1').value) || 4);
    const p2 = Math.max(1, parseFloat(document.getElementById('c10s12P2').value) || 6);
    const t = 1 / (1/p1 + 1/p2);
    document.getElementById('c10s12DualOut').textContent = `Together = ${t.toFixed(2).replace(/\\.00$/,'')} hours`;
  };
  window.c10s12Flow();
  window.c10s12Dual();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📊</span> Inverse Table Solver (x·y = 36) & Sleep/Transport Pie Reader
  </h3>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
    <div class="font-bold text-cyan-300">Inverse Proportion Data Table (Click missing ? slots)</div>
    <div class="grid grid-cols-5 gap-1.5 text-center">
      <div class="p-1.5 bg-slate-900 rounded">x = 2<br><b class="text-amber-300">y = 18</b></div>
      <div class="p-1.5 bg-slate-900 rounded">x = 4<br><b class="text-amber-300">y = 9</b></div>
      <button type="button" onclick="this.innerHTML='x = 8<br><b class=text-emerald-300>y = 4.5</b>'" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-cyan-500/40">x = 8<br><b>y = ?</b></button>
      <div class="p-1.5 bg-slate-900 rounded">x = 9<br><b class="text-amber-300">y = 4</b></div>
      <button type="button" onclick="this.innerHTML='<b class=text-emerald-300>x = 12</b><br>y = 3'" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-cyan-500/40"><b>x = ?</b><br>y = 3</button>
    </div>
  </div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs flex flex-wrap justify-between gap-2">
    <span>24-Hr Sleep (8 hrs): <b class="text-cyan-300">(8/24)×360° = 120° (33.3%)</b></span>
    <span>360-Pupil Transport Pie: <b class="text-emerald-300">1° = exactly 1 pupil!</b></span>
  </div>
</div>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏭</span> Factory Machine Schedule Planner
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Machines<input id="c10s14M" type="number" value="5" min="1" max="50" oninput="c10s14Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Target Bottles<input id="c10s14B" type="number" value="1000" min="100" step="500" oninput="c10s14Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <div class="p-2 rounded bg-slate-950 border border-slate-800 flex flex-col justify-center">
      <div class="text-[10px] text-slate-400">Baseline Rate</div>
      <div class="text-cyan-300 font-bold">30 mach-hr / 1k</div>
    </div>
  </div>
  <div id="c10s14Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs"></div>
</div>
<script>
(function(){
  window.c10s14Calc = function(){
    const m = Math.max(1, parseFloat(document.getElementById('c10s14M').value) || 5);
    const b = Math.max(100, parseFloat(document.getElementById('c10s14B').value) || 1000);
    const reqMachHrs = (b / 1000) * 30;
    const hrs = reqMachHrs / m;
    document.getElementById('c10s14Out').innerHTML = `Needed Machine-Hours = <b>${reqMachHrs.toFixed(1).replace(/\\.0$/,'')}</b> → With <b>${m}</b> machines: Time = <b class="text-emerald-300 text-sm">${hrs.toFixed(2).replace(/\\.00$/,'')} hours</b>!`;
  };
  window.c10s14Calc();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🔎</span> 3-Row Proportion Classifier (Direct vs Inverse vs Neither)
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c10s15Set([100,300,500])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Fuel (Direct)</button>
      <button type="button" onclick="c10s15Set([600,200,120])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Prize Split (Inverse)</button>
      <button type="button" onclick="c10s15Set([45,75,105])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Taxi+Base (Neither)</button>
    </div>
  </div>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">y at x=1<input id="c10s15Y1" type="number" value="600" oninput="c10s15Test()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">y at x=3<input id="c10s15Y2" type="number" value="200" oninput="c10s15Test()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">y at x=5<input id="c10s15Y3" type="number" value="120" oninput="c10s15Test()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c10s15Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c10s15Set = function([a,b,c]){
    document.getElementById('c10s15Y1').value = a;
    document.getElementById('c10s15Y2').value = b;
    document.getElementById('c10s15Y3').value = c;
    window.c10s15Test();
  };
  window.c10s15Test = function(){
    const ys = [1, 3, 5].map((x, i) => ({ x, y: parseFloat(document.getElementById('c10s15Y' + (i+1)).value) || 0 }));
    const qs = ys.map(p => (p.y / p.x).toFixed(1));
    const ps = ys.map(p => (p.x * p.y).toFixed(1));
    const isDir = qs[0] === qs[1] && qs[1] === qs[2];
    const isInv = ps[0] === ps[1] && ps[1] === ps[2];
    const badge = isDir ? '<b class="text-emerald-300">DIRECT PROPORTION (Constant y/x!)</b>' : isInv ? '<b class="text-cyan-300">INVERSE PROPORTION (Constant x·y!)</b>' : '<b class="text-rose-300">NEITHER Direct nor Inverse!</b>';
    document.getElementById('c10s15Out').innerHTML = `
      <div>Quotients (y/x): ${qs.join(' , ')} | Products (x·y): ${ps.join(' , ')}</div>
      <div>Verdict: ${badge}</div>`;
  };
  window.c10s15Test();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📚</span> Chapter 10 Master Proportionality Matrix
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-cyan-300 mb-1">1. Recap, RF Maps & Multi-Term</div>
      <div class="text-slate-300">ad = bc; Map RF = Map ÷ Ground; a:b:c:d :: p:q:r:s ⟺ a/p = b/q = c/r = d/s.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-emerald-300 mb-1">2. Whole Share Partitioning & Pie Charts</div>
      <div class="text-slate-300">Share = x × (Term ÷ Sum); Central Angle = (Freq ÷ Total) × 360° (via HCF).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-amber-300 mb-1">3. Direct vs Inverse Proportions</div>
      <div class="text-slate-300">Direct: x/y = k (constant quotient); Inverse: x · y = k or x₁y₁ = x₂y₂ (n ↔ 1/n).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-rose-300 mb-1">4. Combined Rates & Pumps</div>
      <div class="text-slate-300">Unequal workers/pipes add 1-hour fractions cleanly: 1/T = 1/T₁ + 1/T₂.</div>
    </div>
  </div>
</div>
"""
}

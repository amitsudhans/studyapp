#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 8: Fractions in Disguise
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🎭</span> Per Centum 100-Square Grid Explorer
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s1Set(25)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">25% (1/4)</button>
      <button type="button" onclick="c8s1Set(50)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">50% (1/2)</button>
      <button type="button" onclick="c8s1Set(35)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">35%</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <div>
      <div id="c8s1Grid" class="grid grid-cols-10 gap-1 p-2.5 bg-slate-950 rounded-xl border border-slate-800 w-full max-w-[260px] mx-auto"></div>
      <p class="text-[11px] text-slate-400 text-center mt-2">Slide or click squares to toggle shading out of 100</p>
    </div>
    <div class="space-y-3">
      <div>
        <div class="flex justify-between text-xs text-slate-300 mb-1">
          <span>Shaded Units (z out of 100)</span>
          <span id="c8s1PctLabel" class="font-bold text-amber-300">35%</span>
        </div>
        <input id="c8s1Range" type="range" min="0" max="100" value="35" oninput="c8s1Set(this.value)" class="w-full accent-amber-400">
      </div>
      <div class="grid grid-cols-2 gap-2 text-center">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="text-[10px] uppercase text-slate-400">Per Centum Fraction</div>
          <div id="c8s1Frac" class="text-base font-bold text-cyan-300">35 / 100</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="text-[10px] uppercase text-slate-400">Simplest Disguise</div>
          <div id="c8s1Simp" class="text-base font-bold text-emerald-300">7 / 20</div>
        </div>
      </div>
      <div id="c8s1Note" class="text-xs text-slate-300 bg-slate-950/70 border border-slate-800 rounded-xl p-2.5">
        z% = z/100: 35 shaded squares out of 100 equal squares wear the disguise 7/20.
      </div>
    </div>
  </div>
</div>
<script>
(function(){
  let cells = Array(100).fill(false);
  function gcd(a,b){ return b === 0 ? a : gcd(b, a % b); }
  function render(){
    const grid = document.getElementById('c8s1Grid');
    if(!grid) return;
    grid.innerHTML = '';
    let count = 0;
    cells.forEach((on, i) => {
      if(on) count++;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'aspect-square rounded-[3px] transition-colors ' + (on ? 'bg-amber-400 border border-amber-200' : 'bg-slate-800 hover:bg-slate-700 border border-slate-700');
      btn.onclick = () => { cells[i] = !cells[i]; render(); };
      grid.appendChild(btn);
    });
    const g = gcd(count, 100);
    document.getElementById('c8s1Range').value = count;
    document.getElementById('c8s1PctLabel').textContent = count + '%';
    document.getElementById('c8s1Frac').textContent = count + ' / 100';
    document.getElementById('c8s1Simp').textContent = (count/g) + ' / ' + (100/g);
    document.getElementById('c8s1Note').textContent = `z% = z/100: ${count} shaded squares out of 100 equal squares = ${count}% (reduced ${count/g}/${100/g}).`;
  }
  window.c8s1Set = function(val){
    const n = Math.max(0, Math.min(100, parseInt(val, 10) || 0));
    cells = cells.map((_, i) => i < n);
    render();
  };
  window.c8s1Set(35);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🔄</span> Fraction-to-Percent & Base-10 Converter
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c8s2Preset(3,4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">3/4</button>
      <button type="button" onclick="c8s2Preset(7,20)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">7/20</button>
      <button type="button" onclick="c8s2Preset(3,8)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">3/8</button>
      <button type="button" onclick="c8s2Preset(2,3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">2/3</button>
    </div>
  </div>
  <div class="grid grid-cols-2 gap-3">
    <label class="block text-xs text-slate-300">Numerator
      <input id="c8s2Num" type="number" value="3" min="0" max="200" oninput="c8s2Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-sm">
    </label>
    <label class="block text-xs text-slate-300">Denominator
      <input id="c8s2Den" type="number" value="4" min="1" max="200" oninput="c8s2Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-sm">
    </label>
  </div>
  <div id="c8s2Steps" class="space-y-2 text-xs"></div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
    <div class="text-[11px] font-semibold text-amber-300 mb-1">Base-10 Decimal Shift Advantage (100 = 10²)</div>
    <div id="c8s2Dec" class="text-xs text-slate-300">75% ÷ 100 = 0.75 (shift decimal point 2 places left!)</div>
  </div>
</div>
<script>
(function(){
  window.c8s2Preset = function(n, d){
    document.getElementById('c8s2Num').value = n;
    document.getElementById('c8s2Den').value = d;
    window.c8s2Calc();
  };
  window.c8s2Calc = function(){
    const n = parseFloat(document.getElementById('c8s2Num').value) || 0;
    const d = Math.max(1, parseFloat(document.getElementById('c8s2Den').value) || 1);
    const pct = (n / d) * 100;
    const pctStr = Number.isInteger(pct) ? pct.toString() : pct.toFixed(2).replace(/\\.00$/, '');
    const decStr = (n / d).toFixed(4).replace(/0+$/, '').replace(/\\.$/, '');
    const exact100 = Number.isInteger(100 / d);
    const stepsEl = document.getElementById('c8s2Steps');
    const decEl = document.getElementById('c8s2Dec');
    if(!stepsEl || !decEl) return;
    stepsEl.innerHTML = `
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
        <span class="font-bold text-emerald-300">Method 1 (Scale Denominator to 100):</span>
        ${exact100 ? `${n}/${d} = (${n}×${100/d}) / (${d}×${100/d}) = <b>${n*(100/d)}/100 = ${pctStr}%</b>` : `<span class="text-slate-400">Since ${d} does not divide 100 evenly into a whole integer, use Method 2!</span>`}
      </div>
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
        <span class="font-bold text-cyan-300">Method 2 (Multiply by 100%):</span>
        (${n}/${d}) × 100% = ${n*100}/${d}% = <b class="text-amber-300">${pctStr}%</b>
      </div>`;
    decEl.innerHTML = `<span class="text-cyan-300 font-bold">${pctStr}%</span> ÷ 100 = <span class="text-emerald-300 font-bold">${decStr || '0'}</span> — base-10 aligns hundredths straight to two decimal columns!`;
  };
  window.c8s2Calc();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>🏁</span> Global Stats & Track Position Visualizer
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s3Stat('water')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Body Water</button>
      <button type="button" onclick="c8s3Stat('sun')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Solar Mass</button>
      <button type="button" onclick="c8s3Stat('soil')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Soil Impact</button>
    </div>
  </div>
  <div id="c8s3StatBox" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    💧 <b class="text-cyan-300">Human Body Water (~60%):</b> Roughly 60/100 of adult body weight consists of water! (Rooted in Arthashastra-style per-hundred ratios!)
  </div>
  <div class="space-y-3 pt-1">
    <div class="text-xs font-semibold text-amber-300">0%–100% Race Track Fraction Comparison</div>
    <div class="grid grid-cols-2 gap-3 text-xs">
      <label class="text-slate-300">Runner P Fraction:
        <select id="c8s3P" onchange="c8s3Track()" class="mt-1 w-full px-2 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white">
          <option value="0.5">1/2 (50%)</option>
          <option value="0.7" selected>7/10 (70%)</option>
          <option value="0.6">3/5 (60%)</option>
          <option value="0.625">5/8 (62.5%)</option>
        </select>
      </label>
      <label class="text-slate-300">Runner Q Fraction:
        <select id="c8s3Q" onchange="c8s3Track()" class="mt-1 w-full px-2 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white">
          <option value="0.75" selected>3/4 (75%)</option>
          <option value="0.8">4/5 (80%)</option>
          <option value="0.65">13/20 (65%)</option>
          <option value="0.45">9/20 (45%)</option>
        </select>
      </label>
    </div>
    <div class="space-y-2 bg-slate-950 p-3 rounded-xl border border-slate-800">
      <div class="text-[11px] flex justify-between text-cyan-300"><span>Runner P</span><span id="c8s3PLbl">70%</span></div>
      <div class="h-3 bg-slate-800 rounded-full overflow-hidden"><div id="c8s3PBar" class="h-full bg-cyan-400 transition-all" style="width:70%"></div></div>
      <div class="text-[11px] flex justify-between text-amber-300"><span>Runner Q</span><span id="c8s3QLbl">75%</span></div>
      <div class="h-3 bg-slate-800 rounded-full overflow-hidden"><div id="c8s3QBar" class="h-full bg-amber-400 transition-all" style="width:75%"></div></div>
      <div id="c8s3Res" class="text-xs font-semibold text-emerald-300 pt-1"></div>
    </div>
  </div>
</div>
<script>
(function(){
  const msgs = {
    water: '💧 <b class="text-cyan-300">Human Body Water (~60%):</b> Roughly 60 parts out of 100 of adult body mass consists of water!',
    sun: '☀️ <b class="text-amber-300">Solar System Mass (>99.8%):</b> Over 99.8% sits inside the Sun, leaving < 0.2% for all planets!',
    soil: '🌱 <b class="text-emerald-300">Global Soil Degradation (~33%):</b> Roughly one-third of productive Earth soil faces degradation.'
  };
  window.c8s3Stat = function(k){
    const box = document.getElementById('c8s3StatBox');
    if(box) box.innerHTML = msgs[k] || '';
  };
  window.c8s3Track = function(){
    const p = parseFloat(document.getElementById('c8s3P').value) * 100;
    const q = parseFloat(document.getElementById('c8s3Q').value) * 100;
    document.getElementById('c8s3PLbl').textContent = p.toFixed(1).replace(/\\.0$/, '') + '%';
    document.getElementById('c8s3QLbl').textContent = q.toFixed(1).replace(/\\.0$/, '') + '%';
    document.getElementById('c8s3PBar').style.width = p + '%';
    document.getElementById('c8s3QBar').style.width = q + '%';
    const diff = Math.abs(p - q).toFixed(1).replace(/\\.0$/, '');
    const res = document.getElementById('c8s3Res');
    if(p > q) res.textContent = `Runner P (${p}%) > Runner Q (${q}%) by ${diff} percentage points!`;
    else if(q > p) res.textContent = `Runner Q (${q}%) > Runner P (${p}%) by ${diff} percentage points!`;
    else res.textContent = `Equal track position: both stand at ${p}%!`;
  };
  window.c8s3Track();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⚖️</span> Contextual Whole Base Comparator
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Group A Whole</div>
      <label class="block text-slate-400">Total Units A: <input id="c8s4BaseA" type="number" value="10" min="1" max="5000" oninput="c8s4Calc()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <label class="block text-slate-400">Percent A (%): <input id="c8s4PctA" type="number" value="50" min="0" max="100" oninput="c8s4Calc()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <div id="c8s4ValA" class="text-sm font-bold text-cyan-300 pt-1">Actual = 5 units</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-emerald-300">Group B Whole</div>
      <label class="block text-slate-400">Total Units B: <input id="c8s4BaseB" type="number" value="100" min="1" max="5000" oninput="c8s4Calc()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <label class="block text-slate-400">Percent B (%): <input id="c8s4PctB" type="number" value="20" min="0" max="100" oninput="c8s4Calc()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <div id="c8s4ValB" class="text-sm font-bold text-emerald-300 pt-1">Actual = 20 units</div>
    </div>
  </div>
  <div id="c8s4Visual" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs"></div>
</div>
<script>
(function(){
  window.c8s4Calc = function(){
    const bA = Math.max(1, parseFloat(document.getElementById('c8s4BaseA').value) || 1);
    const pA = Math.max(0, parseFloat(document.getElementById('c8s4PctA').value) || 0);
    const bB = Math.max(1, parseFloat(document.getElementById('c8s4BaseB').value) || 1);
    const pB = Math.max(0, parseFloat(document.getElementById('c8s4PctB').value) || 0);
    const vA = (pA / 100) * bA;
    const vB = (pB / 100) * bB;
    document.getElementById('c8s4ValA').textContent = 'Actual = ' + vA.toFixed(1).replace(/\\.0$/, '') + ' units';
    document.getElementById('c8s4ValB').textContent = 'Actual = ' + vB.toFixed(1).replace(/\\.0$/, '') + ' units';
    const maxV = Math.max(vA, vB, 1);
    const warn = (pA > pB && vA < vB) || (pB > pA && vB < vA)
      ? '⚠️ Notice! The smaller percentage yields a LARGER quantity because its reference whole is bigger!'
      : 'Comparing raw % directly is meaningful ONLY when both whole bases match!';
    document.getElementById('c8s4Visual').innerHTML = `
      <div class="flex items-center gap-2"><span class="w-14 text-cyan-300">Qty A</span><div class="flex-1 h-3 bg-slate-800 rounded-full overflow-hidden"><div class="h-full bg-cyan-400" style="width:${(vA/maxV)*100}%"></div></div><span class="w-12 text-right font-bold">${vA.toFixed(1).replace(/\\.0$/,'')}</span></div>
      <div class="flex items-center gap-2"><span class="w-14 text-emerald-300">Qty B</span><div class="flex-1 h-3 bg-slate-800 rounded-full overflow-hidden"><div class="h-full bg-emerald-400" style="width:${(vB/maxV)*100}%"></div></div><span class="w-12 text-right font-bold">${vB.toFixed(1).replace(/\\.0$/,'')}</span></div>
      <p class="text-amber-300 font-medium pt-1">${warn}</p>`;
  };
  window.c8s4Calc();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Bar Model, Proportion & Unit-Rate Solver
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Target Percent (a%):
      <input id="c8s5Pct" type="range" min="5" max="100" step="5" value="35" oninput="c8s5Update()" class="w-full mt-2 accent-cyan-400">
      <div id="c8s5PctOut" class="font-bold text-cyan-300 mt-1">35%</div>
    </label>
    <label class="text-slate-300">Total Whole (total):
      <input id="c8s5Tot" type="number" value="400" min="10" max="10000" oninput="c8s5Update()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-sm">
    </label>
  </div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
    <div class="text-[11px] text-slate-400">10-Segment Visual Bar Model (each full block = 10% of whole)</div>
    <div id="c8s5Bars" class="grid grid-cols-10 gap-1 h-8"></div>
    <div id="c8s5Methods" class="text-xs text-slate-300 space-y-1 pt-2"></div>
  </div>
</div>
<script>
(function(){
  window.c8s5Update = function(){
    const pct = parseFloat(document.getElementById('c8s5Pct').value) || 0;
    const tot = Math.max(1, parseFloat(document.getElementById('c8s5Tot').value) || 400);
    document.getElementById('c8s5PctOut').textContent = pct + '%';
    const bars = document.getElementById('c8s5Bars');
    if(!bars) return;
    bars.innerHTML = '';
    for(let i = 0; i < 10; i++){
      const segStart = i * 10;
      const fill = Math.max(0, Math.min(10, pct - segStart)) * 10;
      const cell = document.createElement('div');
      cell.className = 'relative bg-slate-800 rounded border border-slate-700 overflow-hidden flex items-center justify-center text-[10px] font-bold text-white';
      cell.innerHTML = `<div class="absolute inset-y-0 left-0 bg-cyan-500/70" style="width:${fill}%"></div><span class="relative z-10">${(tot/10).toFixed(0)}</span>`;
      bars.appendChild(cell);
    }
    const share = (pct / 100) * tot;
    const onePct = tot / 100;
    document.getElementById('c8s5Methods').innerHTML = `
      <div>• <b class="text-emerald-300">Proportion (a/100 = s/total):</b> ${pct}/100 = s/${tot} → s = <b class="text-amber-300">${share.toFixed(1).replace(/\\.0$/,'')}</b></div>
      <div>• <b class="text-cyan-300">Unit Rate (1% scaling):</b> 1% = ${tot}÷100 = ${onePct.toFixed(2).replace(/\\.00$/,'')} → ${pct} × ${onePct.toFixed(2).replace(/\\.00$/,'')} = <b class="text-amber-300">${share.toFixed(1).replace(/\\.0$/,'')}</b></div>`;
  };
  window.c8s5Update();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>⚡</span> Mental Benchmark Decomposer
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s6Preset(360,25)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">25% of 360</button>
      <button type="button" onclick="c8s6Preset(480,15)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">15% of 480</button>
      <button type="button" onclick="c8s6Preset(600,75)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">75% of 600</button>
    </div>
  </div>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Base Amount: <input id="c8s6Base" type="number" value="480" min="1" max="50000" oninput="c8s6Solve()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Mental Percent (%): <input id="c8s6Pct" type="number" value="15" min="1" max="100" oninput="c8s6Solve()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c8s6Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  window.c8s6Preset = function(b, p){
    document.getElementById('c8s6Base').value = b;
    document.getElementById('c8s6Pct').value = p;
    window.c8s6Solve();
  };
  window.c8s6Solve = function(){
    const base = Math.max(1, parseFloat(document.getElementById('c8s6Base').value) || 480);
    let rem = Math.max(0, Math.min(100, Math.round(parseFloat(document.getElementById('c8s6Pct').value) || 0)));
    const orig = rem;
    const chunks = [];
    [[50,'half ÷2'],[25,'quarter ÷4'],[10,'tenth ÷10'],[5,'half of 10%'],[1,'hundredth ÷100']].forEach(([val, hint]) => {
      const cnt = Math.floor(rem / val);
      if(cnt > 0){
        const partVal = cnt * (val / 100) * base;
        chunks.push({ val, cnt, hint, partVal });
        rem -= cnt * val;
      }
    });
    const chips = chunks.map(c => `<span class="inline-block px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700 text-cyan-300">${c.cnt > 1 ? c.cnt + '×' : ''}${c.val}% (${c.hint}) = <b class="text-amber-300">${c.partVal.toFixed(1).replace(/\\.0$/,'')}</b></span>`).join(' <span class="text-slate-500">+</span> ');
    const ans = (orig / 100) * base;
    document.getElementById('c8s6Out').innerHTML = `
      <div class="text-slate-400">Decomposing ${orig}% of ${base} into friendly mental anchors:</div>
      <div class="flex flex-wrap items-center gap-1.5 pt-1">${chips || '<span>0% = 0</span>'}</div>
      <div class="text-sm font-bold text-emerald-300 pt-1">Mental Sum = ${ans.toFixed(2).replace(/\\.00$/,'')}</div>`;
  };
  window.c8s6Solve();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🎯</span> FDP Trio & Sales Targets Above 100%
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s7Set(60)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">60%</button>
      <button type="button" onclick="c8s7Set(150)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">150% Target</button>
      <button type="button" onclick="c8s7Set(225)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">225%</button>
    </div>
  </div>
  <div>
    <div class="flex justify-between text-xs text-slate-300 mb-1">
      <span>Target Achievement (0% to 250%)</span>
      <span id="c8s7PctTxt" class="font-bold text-amber-300">150%</span>
    </div>
    <input id="c8s7Slider" type="range" min="0" max="250" step="5" value="150" oninput="c8s7Set(this.value)" class="w-full accent-amber-400">
  </div>
  <div class="grid grid-cols-3 gap-2 text-center">
    <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-[10px] text-slate-400">Fraction (F)</div><div id="c8s7F" class="text-base font-bold text-cyan-300">3 / 2</div></div>
    <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-[10px] text-slate-400">Decimal (D)</div><div id="c8s7D" class="text-base font-bold text-emerald-300">1.50</div></div>
    <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-[10px] text-slate-400">Percent (P)</div><div id="c8s7P" class="text-base font-bold text-amber-300">150%</div></div>
  </div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
    <div class="flex justify-between text-slate-400"><span>Daily Target = 40 units (100% Baseline Bar)</span><span id="c8s7Units" class="text-emerald-300 font-bold">60 units sold</span></div>
    <div id="c8s7TargetBars" class="space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  function gcd(a,b){ return b === 0 ? a : gcd(b, a % b); }
  window.c8s7Set = function(val){
    const p = Math.max(0, Math.min(250, parseInt(val, 10) || 0));
    document.getElementById('c8s7Slider').value = p;
    document.getElementById('c8s7PctTxt').textContent = p + '%';
    const g = gcd(p, 100);
    document.getElementById('c8s7F').textContent = (p/g) + ' / ' + (100/g);
    document.getElementById('c8s7D').textContent = (p/100).toFixed(2);
    document.getElementById('c8s7P').textContent = p + '%';
    const units = (p / 100) * 40;
    document.getElementById('c8s7Units').textContent = units.toFixed(0) + ' units vs 40 target';
    const barsEl = document.getElementById('c8s7TargetBars');
    let html = '';
    const labels = ['Target 1 (0–100%)', 'Target 2 (100–200%)', 'Target 3 (200–250%)'];
    [0, 100, 200].forEach((start, idx) => {
      const cap = idx === 2 ? 50 : 100;
      const w = Math.max(0, Math.min(cap, p - start)) / cap * 100;
      html += `<div><div class="text-[10px] text-slate-400">${labels[idx]}</div><div class="h-2.5 bg-slate-800 rounded-full overflow-hidden"><div class="h-full ${idx===0?'bg-cyan-400':idx===1?'bg-emerald-400':'bg-amber-400'}" style="width:${w}%"></div></div></div>`;
    });
    barsEl.innerHTML = html;
  };
  window.c8s7Set(150);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🧪</span> Unequal Totals & Content Standardizer
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s8Mode(21,25,32,40,'Test Scores')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Test Scores</button>
      <button type="button" onclick="c8s8Mode(30,120,44,200,'Food Sugar Content')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Know Your Contents</button>
    </div>
  </div>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Item / Test A</div>
      <label class="block text-slate-400">Part / Marks A: <input id="c8s8PartA" type="number" value="21" min="0" oninput="c8s8Update()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <label class="block text-slate-400">Total Base A: <input id="c8s8TotA" type="number" value="25" min="1" oninput="c8s8Update()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Item / Test B</div>
      <label class="block text-slate-400">Part / Marks B: <input id="c8s8PartB" type="number" value="32" min="0" oninput="c8s8Update()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <label class="block text-slate-400">Total Base B: <input id="c8s8TotB" type="number" value="40" min="1" oninput="c8s8Update()" class="w-full mt-1 px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
    </div>
  </div>
  <div id="c8s8Result" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs"></div>
</div>
<script>
(function(){
  let modeLabel = 'Test Scores';
  window.c8s8Mode = function(pa, ta, pb, tb, label){
    modeLabel = label;
    document.getElementById('c8s8PartA').value = pa;
    document.getElementById('c8s8TotA').value = ta;
    document.getElementById('c8s8PartB').value = pb;
    document.getElementById('c8s8TotB').value = tb;
    window.c8s8Update();
  };
  window.c8s8Update = function(){
    const pa = parseFloat(document.getElementById('c8s8PartA').value) || 0;
    const ta = Math.max(1, parseFloat(document.getElementById('c8s8TotA').value) || 1);
    const pb = parseFloat(document.getElementById('c8s8PartB').value) || 0;
    const tb = Math.max(1, parseFloat(document.getElementById('c8s8TotB').value) || 1);
    const pctA = (pa / ta) * 100;
    const pctB = (pb / tb) * 100;
    const winner = pctA > pctB ? `A (${pctA.toFixed(1)}%) > B (${pctB.toFixed(1)}%)` : pctB > pctA ? `B (${pctB.toFixed(1)}%) > A (${pctA.toFixed(1)}%)` : `Equal at ${pctA.toFixed(1)}%`;
    document.getElementById('c8s8Result').innerHTML = `
      <div class="text-slate-400 font-semibold">${modeLabel} Normalized to 100-Scale</div>
      <div class="flex items-center gap-2"><span class="w-10 text-cyan-300 font-bold">A</span><div class="flex-1 h-3 bg-slate-800 rounded-full overflow-hidden"><div class="h-full bg-cyan-400" style="width:${Math.min(100,pctA)}%"></div></div><span class="w-14 text-right font-bold text-cyan-300">${pctA.toFixed(1)}%</span></div>
      <div class="flex items-center gap-2"><span class="w-10 text-amber-300 font-bold">B</span><div class="flex-1 h-3 bg-slate-800 rounded-full overflow-hidden"><div class="h-full bg-amber-400" style="width:${Math.min(100,pctB)}%"></div></div><span class="w-14 text-right font-bold text-amber-300">${pctB.toFixed(1)}%</span></div>
      <div class="text-emerald-300 font-bold pt-1">Fair Verdict: ${winner}</div>`;
  };
  window.c8s8Update();
})();
</script>
"""
}

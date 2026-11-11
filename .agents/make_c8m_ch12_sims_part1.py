#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 12: Tales by Dots and Lines
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⚖️</span> Mean as a Physical Fulcrum Balance Beam
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Dots fixed at: <b>2, 4, 8, 10</b> (True Mean = 6)</span><span>Fulcrum Position: <b id="c12s1Pos" class="text-cyan-300">6.0</b></span></div>
    <svg id="c12s1Svg" viewBox="0 0 320 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <input id="c12s1Sl" type="range" min="2" max="10" step="0.5" value="6" oninput="c12s1Draw()" class="w-full accent-amber-400">
    <div id="c12s1Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  const dots = [2, 4, 8, 10];
  window.c12s1Draw = function(){
    const f = parseFloat(document.getElementById('c12s1Sl').value) || 6;
    document.getElementById('c12s1Pos').textContent = f.toFixed(1);
    let lhs = 0, rhs = 0;
    dots.forEach(d => { if(d < f) lhs += (f - d); else rhs += (d - f); });
    const diff = rhs - lhs;
    const tilt = Math.max(-12, Math.min(12, diff * 1.4));
    const toX = v => 35 + ((v - 1) / 10) * 250;
    const fx = toX(f);
    const svg = document.getElementById('c12s1Svg');
    if(!svg) return;
    svg.innerHTML = `
      <g transform="rotate(${tilt.toFixed(1)}, ${fx.toFixed(1)}, 68)">
        <line x1="35" y1="68" x2="285" y2="68" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
        ${dots.map(d => `<circle cx="${toX(d).toFixed(1)}" cy="56" r="7" fill="#22d3ee"/><text x="${toX(d).toFixed(1)}" y="44" text-anchor="middle" fill="#cbd5e1" font-size="10">${d}</text>`).join('')}
      </g>
      <polygon points="${fx.toFixed(1)},70 ${(fx-10).toFixed(1)},92 ${(fx+10).toFixed(1)},92" fill="#fbbf24"/>`;
    const eq = Math.abs(lhs - rhs) < 0.01;
    document.getElementById('c12s1Out').innerHTML = `LHS Total Distance = <b class="text-cyan-300">${lhs.toFixed(1)}</b> vs RHS Total Distance = <b class="text-amber-300">${rhs.toFixed(1)}</b> → ${eq ? '<b class="text-emerald-300">BALANCED AT MEAN = 6!</b>' : `<b class="text-rose-300">Tilts ${diff>0?'Right':'Left'}! Slide fulcrum to 6!</b>`}`;
  };
  window.c12s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>➕</span> Insert / Balance Data Points Tracker
    </h3>
    <button type="button" onclick="c12s2Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs border border-slate-700">Reset [14,18,22,26]</button>
  </div>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c12s2Add([28])" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">+ Insert 28 (Above 20)</button>
    <button type="button" onclick="c12s2Add([12])" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">+ Insert 12 (Below 20)</button>
    <button type="button" onclick="c12s2Add([14,26])" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">+ Symmetric Pair (14 & 26)</button>
  </div>
  <div id="c12s2Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  let arr = [14, 18, 22, 26];
  function render(){
    const sum = arr.reduce((a,b) => a + b, 0);
    const mean = sum / arr.length;
    document.getElementById('c12s2Out').innerHTML = `
      <div>Current Data (${arr.length} dots): <b class="text-slate-200">[${arr.join(', ')}]</b></div>
      <div class="text-sm font-bold ${Math.abs(mean-20)<0.01?'text-amber-300':mean>20?'text-emerald-300':'text-cyan-300'}">Current Mean = ${mean.toFixed(2).replace(/\\.00$/,'')}</div>`;
  }
  window.c12s2Add = function(vals){ arr = arr.concat(vals); render(); };
  window.c12s2Reset = function(){ arr = [14, 18, 22, 26]; render(); };
  render();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📐</span> Linear Operations on Dot Plots (±c Shift & ×k Scale)
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Multiply by Factor k: <span id="c12s3KOut" class="font-bold text-cyan-300">2×</span>
      <input id="c12s3K" type="range" min="1" max="4" step="0.5" value="2" oninput="c12s3Calc()" class="mt-1 w-full accent-cyan-400">
    </label>
    <label class="text-slate-300">Add Constant c: <span id="c12s3COut" class="font-bold text-amber-300">+5</span>
      <input id="c12s3C" type="range" min="-10" max="15" step="1" value="5" oninput="c12s3Calc()" class="mt-1 w-full accent-amber-400">
    </label>
  </div>
  <div id="c12s3Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const base = [4, 6, 8, 10];
  window.c12s3Calc = function(){
    const k = parseFloat(document.getElementById('c12s3K').value) || 1;
    const c = parseFloat(document.getElementById('c12s3C').value) || 0;
    document.getElementById('c12s3KOut').textContent = k + '×';
    document.getElementById('c12s3COut').textContent = (c >= 0 ? '+' : '') + c;
    const oldMean = 7;
    const transformed = base.map(v => v * k + c);
    const newMean = oldMean * k + c;
    document.getElementById('c12s3Out').innerHTML = `
      <div>Original [4, 6, 8, 10] → Mean = <b>7</b></div>
      <div>Transformed (x×${k} ${c>=0?'+':'−'} ${Math.abs(c)}): <b class="text-cyan-300">[${transformed.join(', ')}]</b></div>
      <div class="text-emerald-300 font-bold">Instant Formula Mean = 7 × ${k} ${c>=0?'+':'−'} ${Math.abs(c)} = ${newMean.toFixed(1).replace(/\\.0$/,'')}!</div>`;
  };
  window.c12s3Calc();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🎯</span> Tinkering with Median Explorer
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c12s4Set([10,12,15,20,25])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">Original (5)</button>
      <button type="button" onclick="c12s4Set([2,10,12,15,20,25,900])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Insert 2 & 900</button>
      <button type="button" onclick="c12s4Set([10,12,15,18,20,25])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Insert +18 Only</button>
    </div>
  </div>
  <div id="c12s4Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  window.c12s4Set = function(arr){
    const s = [...arr].sort((a,b) => a - b);
    const n = s.length;
    const med = n % 2 === 1 ? s[(n-1)/2] : (s[n/2 - 1] + s[n/2]) / 2;
    const mean = s.reduce((a,b) => a + b, 0) / n;
    document.getElementById('c12s4Out').innerHTML = `
      <div>Sorted Values (${n}): <b>[${s.join(', ')}]</b></div>
      <div class="grid grid-cols-2 gap-2 text-center">
        <div class="p-2 rounded-xl bg-slate-900 border border-emerald-500/40"><div class="text-slate-400">Median</div><div class="text-base font-bold text-emerald-300">${med}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-cyan-500/40"><div class="text-slate-400">Mean</div><div class="text-base font-bold text-cyan-300">${mean.toFixed(1).replace(/\\.0$/,'')}</div></div>
      </div>
      <div class="text-slate-400">Inserting one low & one extreme high value (2 & 900) keeps Median locked at 15 while Mean jumps to 140.6!</div>`;
  };
  window.c12s4Set([10,12,15,20,25]);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🕵️</span> Missing Wrestler Weight & Overstated Coconut Corrector
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Missing Wrestler Solver (Team of 5)</div>
      <label class="text-slate-400">Target Mean (kg): <input id="c12s5M" type="number" value="72" oninput="c12s5W()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <div class="text-[11px] text-slate-400">Known 4 weights: 68, 70, 74, 75 (Sum = 287 kg)</div>
      <div id="c12s5WOut" class="text-emerald-300 font-bold"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">10-Tree Coconut Harvest Fixer</div>
      <div class="grid grid-cols-2 gap-1.5">
        <label class="text-slate-400">Wrong<input id="c12s5Wr" type="number" value="65" oninput="c12s5C()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">True<input id="c12s5Tr" type="number" value="35" oninput="c12s5C()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c12s5COut" class="text-cyan-200 font-bold"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c12s5W = function(){
    const m = parseFloat(document.getElementById('c12s5M').value) || 72;
    const reqSum = m * 5;
    document.getElementById('c12s5WOut').textContent = `Missing Weight = ${reqSum} − 287 = ${reqSum - 287} kg`;
  };
  window.c12s5C = function(){
    const wr = parseFloat(document.getElementById('c12s5Wr').value) || 0;
    const tr = parseFloat(document.getElementById('c12s5Tr').value) || 0;
    const newSum = 420 - wr + tr;
    document.getElementById('c12s5COut').textContent = `(420 − ${wr} + ${tr}) ÷ 10 = ${(newSum/10).toFixed(1).replace(/\\.0$/,'')} coconuts`;
  };
  window.c12s5W();
  window.c12s5C();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📋</span> Family-Size Frequency Table: Weighted Mean & Cumulative Median
  </h3>
  <div class="grid grid-cols-4 gap-2 text-xs text-center">
    <label class="p-2 rounded bg-slate-950 border border-slate-800 text-slate-300">Size 3 Freq<input id="c12s6F3" type="number" value="4" min="0" oninput="c12s6Calc()" class="mt-1 w-full px-1 py-1 rounded bg-slate-900 border border-slate-700 text-white text-center"></label>
    <label class="p-2 rounded bg-slate-950 border border-slate-800 text-slate-300">Size 4 Freq<input id="c12s6F4" type="number" value="8" min="0" oninput="c12s6Calc()" class="mt-1 w-full px-1 py-1 rounded bg-slate-900 border border-slate-700 text-white text-center"></label>
    <label class="p-2 rounded bg-slate-950 border border-slate-800 text-slate-300">Size 5 Freq<input id="c12s6F5" type="number" value="6" min="0" oninput="c12s6Calc()" class="mt-1 w-full px-1 py-1 rounded bg-slate-900 border border-slate-700 text-white text-center"></label>
    <label class="p-2 rounded bg-slate-950 border border-slate-800 text-slate-300">Size 6 Freq<input id="c12s6F6" type="number" value="2" min="0" oninput="c12s6Calc()" class="mt-1 w-full px-1 py-1 rounded bg-slate-900 border border-slate-700 text-white text-center"></label>
  </div>
  <div id="c12s6Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c12s6Calc = function(){
    const fs = [3,4,5,6].map(sz => ({ x: sz, f: Math.max(0, parseInt(document.getElementById('c12s6F'+sz).value, 10) || 0) }));
    const n = fs.reduce((s, r) => s + r.f, 0);
    if(n === 0){ document.getElementById('c12s6Out').textContent = 'Enter at least 1 family.'; return; }
    const sumFX = fs.reduce((s, r) => s + r.x * r.f, 0);
    const wMean = sumFX / n;
    const expanded = [];
    fs.forEach(r => { for(let i = 0; i < r.f; i++) expanded.push(r.x); });
    const med = n % 2 === 1 ? expanded[(n-1)/2] : (expanded[n/2 - 1] + expanded[n/2]) / 2;
    document.getElementById('c12s6Out').innerHTML = `
      <div>Σfᵢxᵢ = <b>${sumFX}</b> across Σfᵢ = <b>${n}</b> families</div>
      <div>Weighted Mean = <b class="text-cyan-300">${wMean.toFixed(2).replace(/\\.00$/,'')}</b> | Cumulative Median = <b class="text-emerald-300">${med}</b></div>`;
  };
  window.c12s6Calc();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Live Spreadsheet Grid: Range B3:G3, =SUM() & =AVERAGE()
  </h3>
  <div class="grid grid-cols-6 gap-1.5 text-center text-xs">
    <div class="text-[10px] text-slate-400">B3</div><div class="text-[10px] text-slate-400">C3</div><div class="text-[10px] text-slate-400">D3</div><div class="text-[10px] text-slate-400">E3</div><div class="text-[10px] text-slate-400">F3</div><div class="text-[10px] text-slate-400">G3</div>
    <input id="c12s7_0" type="number" value="12" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
    <input id="c12s7_1" type="number" value="18" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
    <input id="c12s7_2" type="number" value="15" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
    <input id="c12s7_3" type="number" value="24" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
    <input id="c12s7_4" type="number" value="21" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
    <input id="c12s7_5" type="number" value="30" oninput="c12s7Calc()" class="px-1 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-center">
  </div>
  <div id="c12s7Out" class="grid grid-cols-3 gap-2 text-center text-xs"></div>
</div>
<script>
(function(){
  window.c12s7Calc = function(){
    const vals = [0,1,2,3,4,5].map(i => parseFloat(document.getElementById('c12s7_'+i).value) || 0);
    const sum = vals.reduce((a,b) => a + b, 0);
    const avg = sum / vals.length;
    const sorted = [...vals].sort((a,b) => a - b);
    const med = (sorted[2] + sorted[3]) / 2;
    document.getElementById('c12s7Out').innerHTML = `
      <div class="p-2.5 rounded-xl bg-slate-950 border border-cyan-500/40"><div class="text-[10px] text-slate-400">H3: =SUM(B3:G3)</div><div class="text-base font-bold text-cyan-300">${sum}</div></div>
      <div class="p-2.5 rounded-xl bg-slate-950 border border-emerald-500/40"><div class="text-[10px] text-slate-400">I3: =AVERAGE(B3:G3)</div><div class="text-base font-bold text-emerald-300">${avg.toFixed(2).replace(/\\.00$/,'')}</div></div>
      <div class="p-2.5 rounded-xl bg-slate-950 border border-amber-500/40"><div class="text-[10px] text-slate-400">J3: =MEDIAN(B3:G3)</div><div class="text-base font-bold text-amber-300">${med}</div></div>`;
  };
  window.c12s7Calc();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🌡️</span> Line Graph: Kerala vs Punjab Monthly Max Temperatures
  </h3>
  <svg id="c12s8Svg" viewBox="0 0 360 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div class="flex flex-wrap justify-between text-xs text-slate-300 px-1">
    <span class="text-cyan-300">● <b>Kerala (Coastal):</b> Steady 29°C–33°C all year</span>
    <span class="text-amber-300">● <b>Punjab (Inland):</b> Steep swing ~18°C winter ↔ >40°C summer</span>
  </div>
</div>
<script>
(function(){
  const kerala = [31,32,33,33,32,30,29,29,30,30,31,31];
  const punjab = [18,22,28,36,41,40,36,34,34,31,26,20];
  const svg = document.getElementById('c12s8Svg');
  if(!svg) return;
  const toX = i => 26 + (i / 11) * 314;
  const toY = t => 130 - ((t - 10) / 35) * 108;
  const path = arr => arr.map((t, i) => (i===0?'M':'L') + toX(i).toFixed(1) + ',' + toY(t).toFixed(1)).join(' ');
  const months = ['J','F','M','A','M','J','J','A','S','O','N','D'];
  svg.innerHTML = `
    <line x1="26" y1="130" x2="345" y2="130" stroke="#334155"/>
    <path d="${path(kerala)}" fill="none" stroke="#22d3ee" stroke-width="2.5"/>
    <path d="${path(punjab)}" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
    ${months.map((m,i) => `<text x="${toX(i).toFixed(1)}" y="143" text-anchor="middle" fill="#94a3b8" font-size="9">${m}</text>`).join('')}
    <text x="160" y="20" fill="#fbbf24" font-size="10">Punjab Peak (~41°C May)</text>`;
})();
</script>
"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 10: Proportional Reasoning-2
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🥞</span> Idli Batter Scaler & Cross-Multiplication Checker
  </h3>
  <div class="grid grid-cols-4 gap-2 text-xs">
    <label class="text-slate-300">a (Rice 1)<input id="c10s1A" type="number" value="3" min="1" oninput="c10s1Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">b (Dal 1)<input id="c10s1B" type="number" value="1" min="1" oninput="c10s1Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">c (Rice 2)<input id="c10s1C" type="number" value="12" min="1" oninput="c10s1Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">d (Dal 2)<input id="c10s1D" type="number" value="4" min="1" oninput="c10s1Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c10s1Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c10s1Check = function(){
    const a = parseFloat(document.getElementById('c10s1A').value) || 1;
    const b = parseFloat(document.getElementById('c10s1B').value) || 1;
    const c = parseFloat(document.getElementById('c10s1C').value) || 1;
    const d = parseFloat(document.getElementById('c10s1D').value) || 1;
    const ad = a * d, bc = b * c;
    const ok = Math.abs(ad - bc) < 1e-9;
    document.getElementById('c10s1Out').innerHTML = `
      <div>Cross Products: a×d = <b>${a}×${d} = ${ad}</b> vs b×c = <b>${b}×${c} = ${bc}</b></div>
      <div class="${ok ? 'text-emerald-300' : 'text-rose-300'} font-bold">${ok ? `Exact Proportion! (${a}:${b} :: ${c}:${d}) — identical scaling factor ${(c/a).toFixed(2).replace(/\\.00$/,'')}×!` : 'Not Proportional! Cross-products differ.'}</div>`;
  };
  window.c10s1Check();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🗺️</span> Representative Fraction (RF) & Map Distance Lab
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c10s2Mode(6000000,5,'Bengaluru–Chennai (1:60,00,000)')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Atlas 1:60L</button>
      <button type="button" onclick="c10s2Mode(50,12,'Classroom Wall (1:50 Plan)')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">1:50 Floor Plan</button>
    </div>
  </div>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">RF Scale Denominator (1 : N)<input id="c10s2Den" type="number" value="6000000" min="1" oninput="c10s2Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Map Length (cm)<input id="c10s2Cm" type="number" value="5" min="0.1" step="0.5" oninput="c10s2Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c10s2Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  let lbl = 'Atlas Map (1:60,00,000)';
  window.c10s2Mode = function(den, cm, title){
    lbl = title;
    document.getElementById('c10s2Den').value = den;
    document.getElementById('c10s2Cm').value = cm;
    window.c10s2Calc();
  };
  window.c10s2Calc = function(){
    const den = Math.max(1, parseFloat(document.getElementById('c10s2Den').value) || 1);
    const cm = Math.max(0, parseFloat(document.getElementById('c10s2Cm').value) || 0);
    const groundCm = cm * den;
    const groundM = groundCm / 100;
    const groundKm = groundM / 1000;
    document.getElementById('c10s2Out').innerHTML = `
      <div class="text-slate-400">${lbl}</div>
      <div>Ground Distance = ${cm} cm × ${den.toLocaleString()} = <b>${groundM.toLocaleString()} m</b> (${groundKm >= 0.1 ? `<b class="text-emerald-300">${groundKm.toFixed(2).replace(/\\.00$/,'')} km</b>` : `<b class="text-emerald-300">${groundM} m</b>`})</div>`;
  };
  window.c10s2Calc();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>🧪</span> Multi-Term Ratio Scaler (>2 Terms)
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c10s3Set('Spice Mix',[8,4,2,1],['Coriander','Cumin','Pepper','Cloves'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Spice 8:4:2:1</button>
      <button type="button" onclick="c10s3Set('Paint Shade',[2,3,5],['Red','Blue','White'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Paint 2:3:5</button>
      <button type="button" onclick="c10s3Set('Concrete',[1,1.5,3],['Cement','Sand','Gravel'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Concrete 1:1.5:3</button>
    </div>
  </div>
  <label class="block text-xs text-slate-300">Common Batch Multiplier: <span id="c10s3KOut" class="font-bold text-amber-300">4×</span>
    <input id="c10s3K" type="range" min="1" max="12" value="4" oninput="c10s3Draw()" class="mt-1 w-full accent-emerald-400">
  </label>
  <div id="c10s3Out" class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs"></div>
</div>
<script>
(function(){
  let cur = { name: 'Concrete', terms: [1, 1.5, 3], names: ['Cement', 'Sand', 'Gravel'] };
  window.c10s3Set = function(name, terms, names){ cur = { name, terms, names }; window.c10s3Draw(); };
  window.c10s3Draw = function(){
    const k = parseInt(document.getElementById('c10s3K').value, 10) || 1;
    document.getElementById('c10s3KOut').textContent = k + '×';
    const box = document.getElementById('c10s3Out');
    if(!box) return;
    box.style.gridTemplateColumns = `repeat(${cur.terms.length}, minmax(0, 1fr))`;
    box.innerHTML = cur.terms.map((t, i) => `
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
        <div class="text-[10px] text-slate-400">${cur.names[i]} (base ${t})</div>
        <div class="text-base font-bold text-cyan-300">${(t * k).toFixed(1).replace(/\\.0$/,'')}</div>
      </div>`).join('');
  };
  window.c10s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🍰</span> Whole Quantity Partitioning Calculator
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c10s4Preset(110,[1,1.5,3],['Cement','Sand','Gravel'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">110 Concrete</button>
      <button type="button" onclick="c10s4Preset(50,[2,3,5],['Red','Blue','White'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">50 mL Paint</button>
      <button type="button" onclick="c10s4Preset(180,[1,3,5],['Angle 1','Angle 2','Angle 3'])" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">180° Triangle (1:3:5)</button>
    </div>
  </div>
  <label class="block text-xs text-slate-300">Total Whole (x):
    <input id="c10s4Tot" type="number" value="180" min="1" oninput="c10s4Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-sm">
  </label>
  <div id="c10s4Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  let ratio = [1, 3, 5], labels = ['Angle 1', 'Angle 2', 'Angle 3'];
  window.c10s4Preset = function(tot, r, l){
    ratio = r; labels = l;
    document.getElementById('c10s4Tot').value = tot;
    window.c10s4Calc();
  };
  window.c10s4Calc = function(){
    const tot = Math.max(0.1, parseFloat(document.getElementById('c10s4Tot').value) || 180);
    const sum = ratio.reduce((a,b) => a + b, 0);
    const shares = ratio.map((t, i) => `<div>• <b>${labels[i]}</b> (term ${t}/${sum}): ${tot} × (${t}/${sum}) = <b class="text-emerald-300">${((tot*t)/sum).toFixed(1).replace(/\\.0$/,'')}</b></div>`).join('');
    document.getElementById('c10s4Out').innerHTML = `<div class="text-slate-400">Sum of All Terms = <b>${sum}</b> | Unit Size = ${(tot/sum).toFixed(2).replace(/\\.00$/,'')}</div>${shares}`;
  };
  window.c10s4Calc();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪙</span> Coin Value Ratios & Triangle Inequality Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Coin Counts Ratio (₹1 : ₹2 : ₹5 = 3 : 2 : 1)</div>
      <label class="text-slate-400">Total Bag Value (₹): <input id="c10s5Val" type="number" value="120" min="12" step="12" oninput="c10s5Coins()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <div id="c10s5CoinOut" class="text-emerald-300 font-semibold"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Triangle Side Ratio Viability (a : b : c)</div>
      <div class="grid grid-cols-3 gap-1.5">
        <input id="c10s5A" type="number" value="2" min="1" oninput="c10s5Tri()" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white">
        <input id="c10s5B" type="number" value="3" min="1" oninput="c10s5Tri()" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white">
        <input id="c10s5C" type="number" value="6" min="1" oninput="c10s5Tri()" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white">
      </div>
      <div id="c10s5TriOut" class="font-semibold"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c10s5Coins = function(){
    const tot = Math.max(12, parseFloat(document.getElementById('c10s5Val').value) || 120);
    const k = tot / 12;
    document.getElementById('c10s5CoinOut').textContent = `1(3k)+2(2k)+5(1k) = 12k = ₹${tot} → k=${k.toFixed(1).replace(/\\.0$/,'')} → Counts: ${3*k} (₹1), ${2*k} (₹2), ${k} (₹5)`;
  };
  window.c10s5Tri = function(){
    const sides = [
      parseFloat(document.getElementById('c10s5A').value) || 1,
      parseFloat(document.getElementById('c10s5B').value) || 1,
      parseFloat(document.getElementById('c10s5C').value) || 1
    ].sort((x,y) => x - y);
    const ok = sides[0] + sides[1] > sides[2];
    const el = document.getElementById('c10s5TriOut');
    el.className = (ok ? 'text-emerald-300' : 'text-rose-400') + ' font-semibold';
    el.textContent = ok ? `Valid Triangle! (${sides[0]} + ${sides[1]} > ${sides[2]})` : `Invalid! (${sides[0]} + ${sides[1]} ≤ ${sides[2]} fails triangle inequality)`;
  };
  window.c10s5Coins();
  window.c10s5Tri();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🥧</span> Pie Chart Builder: Assessment Grades A–E (40 Students)
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c10s6Pie" viewBox="-110 -110 220 220" class="w-full max-w-[200px] mx-auto"></svg>
    <div id="c10s6List" class="space-y-1.5 text-xs"></div>
  </div>
</div>
<script>
(function(){
  const grades = [
    { name: 'Grade A', freq: 12, color: '#34d399' },
    { name: 'Grade B', freq: 10, color: '#38bdf8' },
    { name: 'Grade C', freq: 8,  color: '#fbbf24' },
    { name: 'Grade D', freq: 6,  color: '#a78bfa' },
    { name: 'Grade E', freq: 4,  color: '#fb7185' }
  ];
  const tot = grades.reduce((s, g) => s + g.freq, 0);
  const svg = document.getElementById('c10s6Pie');
  const list = document.getElementById('c10s6List');
  if(!svg || !list) return;
  let angle = -Math.PI / 2;
  let paths = '';
  let rows = '';
  grades.forEach(g => {
    const deg = (g.freq / tot) * 360;
    const rad = (deg * Math.PI) / 180;
    const x1 = 90 * Math.cos(angle), y1 = 90 * Math.sin(angle);
    const x2 = 90 * Math.cos(angle + rad), y2 = 90 * Math.sin(angle + rad);
    const large = deg > 180 ? 1 : 0;
    paths += `<path d="M 0 0 L ${x1.toFixed(1)} ${y1.toFixed(1)} A 90 90 0 ${large} 1 ${x2.toFixed(1)} ${y2.toFixed(1)} Z" fill="${g.color}" stroke="#0f172a" stroke-width="2"/>`;
    rows += `<div class="flex items-center justify-between p-1.5 rounded bg-slate-950 border border-slate-800"><span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full" style="background:${g.color}"></span><b>${g.name}</b> (${g.freq}/40)</span><span class="font-bold text-amber-300">${deg}°</span></div>`;
    angle += rad;
  });
  svg.innerHTML = paths;
  list.innerHTML = rows + `<div class="text-[11px] text-slate-400 pt-1">HCF = 2 simplifies ratio to 6:5:4:3:2 (1 unit = 18° → Sum = 360°)</div>`;
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📺</span> Percentage-to-Degree & Reverse Pie Converter
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Survey % → Pie Angle (1% = 3.6°)</div>
      <label class="text-slate-400">Category Share (%): <input id="c10s7Pct" type="range" min="5" max="90" value="35" oninput="c10s7Fwd()" class="mt-1 w-full accent-cyan-400"></label>
      <div id="c10s7FwdOut" class="text-amber-300 font-bold"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-emerald-300">Reverse Reader: Angle → Count</div>
      <div class="grid grid-cols-2 gap-2">
        <label class="text-slate-400">Angle (°)<input id="c10s7Ang" type="number" value="108" min="1" max="360" oninput="c10s7Rev()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">Total People<input id="c10s7Tot" type="number" value="120" min="1" oninput="c10s7Rev()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c10s7RevOut" class="text-emerald-300 font-bold"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c10s7Fwd = function(){
    const p = parseFloat(document.getElementById('c10s7Pct').value) || 0;
    document.getElementById('c10s7FwdOut').textContent = `${p}% × 3.6° = ${(p * 3.6).toFixed(1).replace(/\\.0$/,'')}° central sector`;
  };
  window.c10s7Rev = function(){
    const ang = parseFloat(document.getElementById('c10s7Ang').value) || 0;
    const tot = Math.max(1, parseFloat(document.getElementById('c10s7Tot').value) || 120);
    const cnt = (ang / 360) * tot;
    document.getElementById('c10s7RevOut').textContent = `(${ang}° / 360°) × ${tot} = ${cnt.toFixed(1).replace(/\\.0$/,'')} students`;
  };
  window.c10s7Fwd();
  window.c10s7Rev();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Direct (x/y = k) vs Inverse (x·y = k) Reciprocal Lab
  </h3>
  <label class="block text-xs text-slate-300">Scale Variable x by Factor n: <span id="c10s8NVal" class="font-bold text-amber-300">2×</span>
    <input id="c10s8N" type="range" min="1" max="5" step="0.5" value="2" oninput="c10s8Calc()" class="mt-1 w-full accent-amber-400">
  </label>
  <div id="c10s8Out" class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs"></div>
</div>
<script>
(function(){
  window.c10s8Calc = function(){
    const n = parseFloat(document.getElementById('c10s8N').value) || 2;
    document.getElementById('c10s8NVal').textContent = n + '×';
    const baseX = 12, baseY = 6;
    const newX = baseX * n;
    const dirY = baseY * n;
    const invY = baseY / n;
    document.getElementById('c10s8Out').innerHTML = `
      <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/40 space-y-1">
        <div class="font-bold text-emerald-300">Direct Proportion (x / y = 2 constant)</div>
        <div>Start (12, 6) → x×${n} = <b>${newX}</b>, y×${n} = <b class="text-emerald-300">${dirY.toFixed(1).replace(/\\.0$/,'')}</b></div>
        <div class="text-slate-400">Quotient: ${newX}/${dirY.toFixed(1).replace(/\\.0$/,'')} = 2</div>
      </div>
      <div class="p-3 rounded-xl bg-slate-950 border border-cyan-500/40 space-y-1">
        <div class="font-bold text-cyan-300">Inverse Proportion (x · y = 72 constant)</div>
        <div>Start (12, 6) → x×${n} = <b>${newX}</b>, y÷${n} = <b class="text-amber-300">${invY.toFixed(2).replace(/\\.00$/,'')}</b></div>
        <div class="text-slate-400">Product: ${newX} × ${invY.toFixed(2).replace(/\\.00$/,'')} = 72</div>
      </div>`;
  };
  window.c10s8Calc();
})();
</script>
"""
}

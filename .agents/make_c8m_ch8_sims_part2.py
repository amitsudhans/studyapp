#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 8: Fractions in Disguise
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Relative Change vs % of Base Analyzer
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Original Starting Base:
      <input id="c8s9Orig" type="number" value="4000" min="1" oninput="c8s9Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white">
    </label>
    <label class="text-slate-300">New Ending Value:
      <input id="c8s9New" type="number" value="4600" min="0" oninput="c8s9Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white">
    </label>
  </div>
  <div id="c8s9Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs"></div>
</div>
<script>
(function(){
  window.c8s9Calc = function(){
    const orig = Math.max(1, parseFloat(document.getElementById('c8s9Orig').value) || 1);
    const valNew = Math.max(0, parseFloat(document.getElementById('c8s9New').value) || 0);
    const diff = valNew - orig;
    const pctChange = (diff / orig) * 100;
    const pctOfOrig = (valNew / orig) * 100;
    const isUp = diff >= 0;
    document.getElementById('c8s9Out').innerHTML = `
      <div class="flex flex-wrap justify-between gap-2">
        <span>Amount of Change: <b class="text-white">${diff >= 0 ? '+' : ''}${diff.toFixed(1).replace(/\\.0$/,'')}</b></span>
        <span>Divided by Original Base: <b class="text-cyan-300">${orig}</b></span>
      </div>
      <div class="grid grid-cols-2 gap-2 pt-1 text-center">
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-400">Percentage ${isUp ? 'Increase' : 'Decrease'}</div>
          <div class="text-base font-bold ${isUp ? 'text-emerald-300' : 'text-rose-300'}">${Math.abs(pctChange).toFixed(1).replace(/\\.0$/,'')}% ${isUp ? '↑' : '↓'}</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
          <div class="text-[10px] text-slate-400">New Value as % OF Original</div>
          <div class="text-base font-bold text-amber-300">${pctOfOrig.toFixed(1).replace(/\\.0$/,'')}%</div>
        </div>
      </div>`;
  };
  window.c8s9Calc();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🧾</span> Supply Chain, Gross/Net Profit & GST Bill Lab
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <label class="text-slate-300">Cost Price (₹)<input id="c8s10Cp" type="number" value="800" min="1" oninput="c8s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Selling Price (₹)<input id="c8s10Sp" type="number" value="1000" min="1" oninput="c8s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Operating Exp (₹)<input id="c8s10Op" type="number" value="80" min="0" oninput="c8s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">GST Slab (%)
      <select id="c8s10Gst" onchange="c8s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white">
        <option value="5">5% (2.5+2.5)</option>
        <option value="12">12% (6+6)</option>
        <option value="18" selected>18% (9+9)</option>
      </select>
    </label>
  </div>
  <div id="c8s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c8s10Calc = function(){
    const cp = Math.max(1, parseFloat(document.getElementById('c8s10Cp').value) || 1);
    const sp = Math.max(0, parseFloat(document.getElementById('c8s10Sp').value) || 0);
    const op = Math.max(0, parseFloat(document.getElementById('c8s10Op').value) || 0);
    const gst = parseFloat(document.getElementById('c8s10Gst').value) || 0;
    const gross = sp - cp;
    const net = gross - op;
    const grossPct = (gross / cp) * 100;
    const halfTax = (gst / 200) * sp;
    const totalBill = sp + 2 * halfTax;
    document.getElementById('c8s10Out').innerHTML = `
      <div class="flex flex-wrap justify-between gap-2">
        <span>Gross ${gross >= 0 ? 'Profit' : 'Loss'}: <b class="${gross>=0?'text-emerald-300':'text-rose-300'}">₹${gross.toFixed(0)} (${grossPct.toFixed(1)}%)</b></span>
        <span>Net Profit (−Expenses): <b class="${net>=0?'text-cyan-300':'text-rose-300'}">₹${net.toFixed(0)}</b></span>
      </div>
      <div class="border-t border-slate-800 pt-1.5 flex flex-wrap justify-between gap-2 text-slate-300">
        <span>CGST (${gst/2}%): ₹${halfTax.toFixed(2)}</span>
        <span>SGST (${gst/2}%): ₹${halfTax.toFixed(2)}</span>
        <span class="text-amber-300 font-bold">Customer Bill: ₹${totalBill.toFixed(2)}</span>
      </div>`;
  };
  window.c8s10Calc();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌱</span> Linear p(1+rt) vs Compound p(1+r)^t Growth Curve
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Principal (p) ₹<input id="c8s11P" type="number" value="1000" min="100" oninput="c8s11Draw()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Rate (%)<input id="c8s11R" type="number" value="15" min="1" max="50" oninput="c8s11Draw()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Years (t)<input id="c8s11T" type="range" min="1" max="10" value="6" oninput="c8s11Draw()" class="mt-2 w-full accent-emerald-400"><span id="c8s11TLbl" class="text-cyan-300 font-bold">6 yrs</span></label>
  </div>
  <svg id="c8s11Svg" viewBox="0 0 360 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c8s11Stats" class="flex flex-wrap justify-between gap-2 text-xs px-1"></div>
</div>
<script>
(function(){
  window.c8s11Draw = function(){
    const p = Math.max(100, parseFloat(document.getElementById('c8s11P').value) || 1000);
    const r = (parseFloat(document.getElementById('c8s11R').value) || 10) / 100;
    const tMax = parseInt(document.getElementById('c8s11T').value, 10) || 6;
    document.getElementById('c8s11TLbl').textContent = tMax + ' yrs';
    const simpPts = [], compPts = [];
    for(let i = 0; i <= tMax; i++){
      simpPts.push(p * (1 + r * i));
      compPts.push(p * Math.pow(1 + r, i));
    }
    const maxY = Math.max(...compPts, p * 1.1);
    const toX = (i) => 24 + (i / tMax) * 316;
    const toY = (v) => 132 - ((v - p * 0.8) / (maxY - p * 0.8)) * 112;
    const dSimp = simpPts.map((v, i) => (i===0?'M':'L') + toX(i).toFixed(1) + ',' + toY(v).toFixed(1)).join(' ');
    const dComp = compPts.map((v, i) => (i===0?'M':'L') + toX(i).toFixed(1) + ',' + toY(v).toFixed(1)).join(' ');
    const svg = document.getElementById('c8s11Svg');
    if(!svg) return;
    svg.innerHTML = `
      <line x1="24" y1="132" x2="345" y2="132" stroke="#334155" stroke-width="1"/>
      <path d="${dSimp}" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4"/>
      <path d="${dComp}" fill="none" stroke="#34d399" stroke-width="3"/>
      <text x="30" y="20" fill="#34d399" font-size="10">Compound p(1+r)^t</text>
      <text x="160" y="20" fill="#38bdf8" font-size="10">Simple p(1+rt)</text>`;
    const sEnd = simpPts[tMax], cEnd = compPts[tMax];
    document.getElementById('c8s11Stats').innerHTML = `
      <span class="text-cyan-300">Simple: <b>₹${sEnd.toFixed(0)}</b></span>
      <span class="text-emerald-300">Compound: <b>₹${cEnd.toFixed(0)}</b></span>
      <span class="text-amber-300">Snowball Extra: <b>+₹${(cEnd-sEnd).toFixed(0)}</b></span>`;
  };
  window.c8s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>📉</span> Depreciation & Exponential Decay Curve p(1−r)^t
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Initial Value (p) ₹<input id="c8s12P" type="number" value="50000" min="100" oninput="c8s12Draw()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Decay Rate (%)<input id="c8s12R" type="number" value="20" min="1" max="60" oninput="c8s12Draw()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Years (t)<input id="c8s12T" type="range" min="1" max="8" value="4" oninput="c8s12Draw()" class="mt-2 w-full accent-rose-400"><span id="c8s12TLbl" class="text-rose-300 font-bold">4 yrs</span></label>
  </div>
  <div id="c8s12Bars" class="grid grid-cols-5 gap-2 items-end h-28 bg-slate-950 rounded-xl border border-slate-800 p-3"></div>
  <div id="c8s12Summary" class="text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c8s12Draw = function(){
    const p = Math.max(100, parseFloat(document.getElementById('c8s12P').value) || 50000);
    const r = Math.min(0.6, (parseFloat(document.getElementById('c8s12R').value) || 20) / 100);
    const tMax = parseInt(document.getElementById('c8s12T').value, 10) || 4;
    document.getElementById('c8s12TLbl').textContent = tMax + ' yrs';
    const barsEl = document.getElementById('c8s12Bars');
    if(!barsEl) return;
    barsEl.className = `grid gap-2 items-end h-28 bg-slate-950 rounded-xl border border-slate-800 p-3`;
    barsEl.style.gridTemplateColumns = `repeat(${tMax + 1}, minmax(0, 1fr))`;
    let html = '';
    let finalV = p;
    for(let i = 0; i <= tMax; i++){
      const v = p * Math.pow(1 - r, i);
      finalV = v;
      const hPct = Math.max(6, (v / p) * 100);
      html += `<div class="flex flex-col items-center justify-end h-full"><div class="text-[9px] text-amber-300 mb-0.5">${(v/1000).toFixed(1)}k</div><div class="w-full rounded-t bg-rose-500/80" style="height:${hPct*0.75}%"></div><div class="text-[9px] text-slate-400 mt-0.5">Y${i}</div></div>`;
    }
    barsEl.innerHTML = html;
    document.getElementById('c8s12Summary').innerHTML = `After <b>${tMax} years</b> at ${(r*100).toFixed(0)}% exponential decay: Remaining Value = <b class="text-rose-300">₹${finalV.toFixed(0)}</b> (shrinks by smaller ₹ steps each year!).`;
  };
  window.c8s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>⚠️</span> Successive Discounts & Asymmetry Trap Tester
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c8s13Set(-30,-20)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">30% + 20% Off</button>
      <button type="button" onclick="c8s13Set(50,-50)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">+50% then −50%</button>
    </div>
  </div>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Step 1 Change (%): <input id="c8s13A" type="number" value="-30" min="-90" max="200" oninput="c8s13Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Step 2 Change (%): <input id="c8s13B" type="number" value="-20" min="-90" max="200" oninput="c8s13Calc()" class="mt-1 w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c8s13Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c8s13Set = function(a, b){
    document.getElementById('c8s13A').value = a;
    document.getElementById('c8s13B').value = b;
    window.c8s13Calc();
  };
  window.c8s13Calc = function(){
    const a = parseFloat(document.getElementById('c8s13A').value) || 0;
    const b = parseFloat(document.getElementById('c8s13B').value) || 0;
    const after1 = 100 * (1 + a / 100);
    const after2 = after1 * (1 + b / 100);
    const netPct = after2 - 100;
    const naive = a + b;
    document.getElementById('c8s13Out').innerHTML = `
      <div>Starting ₹100 → Step 1 (${a >= 0 ? '+' : ''}${a}%): <b class="text-cyan-300">₹${after1.toFixed(1)}</b> → Step 2 (${b >= 0 ? '+' : ''}${b}%): <b class="text-amber-300">₹${after2.toFixed(2)}</b></div>
      <div class="flex flex-wrap justify-between gap-2 pt-1">
        <span>True Net Effect: <b class="${netPct>=0?'text-emerald-300':'text-rose-300'}">${netPct>=0?'+':''}${netPct.toFixed(2)}%</b></span>
        <span class="text-slate-400">Naive Sum (${a} + ${b}) = <b>${naive}% (TRAP!)</b></span>
      </div>`;
  };
  window.c8s13Calc();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-4">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏷️</span> Promotional Deals & Rectangle Area % Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Promotional Deal: "Buy X, Get Y Free"</div>
      <div class="grid grid-cols-2 gap-2">
        <label class="text-slate-400">Buy (X)<input id="c8s14Buy" type="number" value="2" min="1" max="20" oninput="c8s14Deals()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">Free (Y)<input id="c8s14Free" type="number" value="1" min="1" max="10" oninput="c8s14Deals()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c8s14DealOut" class="text-emerald-300 font-semibold pt-1"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Rectangle Area Change Tester</div>
      <div class="grid grid-cols-2 gap-2">
        <label class="text-slate-400">Length Δ%<input id="c8s14L" type="number" value="20" min="-80" max="200" oninput="c8s14Area()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">Width Δ%<input id="c8s14W" type="number" value="-20" min="-80" max="200" oninput="c8s14Area()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c8s14AreaOut" class="text-rose-300 font-semibold pt-1"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c8s14Deals = function(){
    const x = Math.max(1, parseInt(document.getElementById('c8s14Buy').value, 10) || 1);
    const y = Math.max(0, parseInt(document.getElementById('c8s14Free').value, 10) || 0);
    const disc = (y / (x + y)) * 100;
    document.getElementById('c8s14DealOut').textContent = `${y} free out of ${x+y} carried = ${disc.toFixed(2)}% true discount!`;
  };
  window.c8s14Area = function(){
    const l = parseFloat(document.getElementById('c8s14L').value) || 0;
    const w = parseFloat(document.getElementById('c8s14W').value) || 0;
    const factor = (1 + l / 100) * (1 + w / 100);
    const areaPct = (factor - 1) * 100;
    const el = document.getElementById('c8s14AreaOut');
    el.className = (areaPct >= 0 ? 'text-emerald-300' : 'text-rose-300') + ' font-semibold pt-1';
    el.textContent = `Area factor = ${factor.toFixed(2)} → ${areaPct >= 0 ? '+' : ''}${areaPct.toFixed(1)}% Area change!`;
  };
  window.c8s14Deals();
  window.c8s14Area();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📚</span> Chapter 8 Master Formula Matrix
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-cyan-300 mb-1">1. Per Cent & FDP Conversions</div>
      <div class="text-slate-300">z% = z/100; Fraction → %: × 100%; % → Decimal: ÷ 100 (2 shifts left).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-amber-300 mb-1">2. Part of a Contextual Whole</div>
      <div class="text-slate-300">a/100 = s/total; Benchmarks: 50%(÷2), 25%(÷4), 10%(÷10), 5%, 1%.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-emerald-300 mb-1">3. Relative % Change & Commerce</div>
      <div class="text-slate-300">% Change = (Change ÷ Original Base) × 100; Profit/Loss% based on CP; GST = CGST + SGST.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-rose-300 mb-1">4. Growth, Decay & Successive Multipliers</div>
      <div class="text-slate-300">Linear: p(1 + rt); Compound: p(1 + r)^t; Decay: p(1 − r)^t; Chain: (1 ± r₁)(1 ± r₂).</div>
    </div>
  </div>
</div>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>♞</span> Peaceful Knights 8×8 Chessboard Lab
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c8s16Preset('col')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">8 Peaceful Knights</button>
      <button type="button" onclick="c8s16Preset('dark')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">32 Dark-Square Max (50%)</button>
      <button type="button" onclick="c8s16Preset('clear')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Clear</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <div id="c8s16Board" class="grid grid-cols-8 gap-0.5 p-2 bg-slate-950 rounded-xl border border-slate-800 w-full max-w-[260px] mx-auto"></div>
    <div class="space-y-2.5 text-xs">
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
        <div>Placed Knights: <b id="c8s16Cnt" class="text-cyan-300">0</b> (<span id="c8s16Pct">0%</span> of 64 squares)</div>
        <div>Attacks Detected: <b id="c8s16Atk" class="text-emerald-300">0 (Peaceful!)</b></div>
      </div>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-slate-300">
        <b>L-Move Parity Rule:</b> Every (±2, ±1) jump reverses square color! Placing knights ONLY on dark squares ensures 0 attacks up to 32 knights (50%)!
      </div>
    </div>
  </div>
</div>
<script>
(function(){
  let knights = new Set();
  const key = (r,c) => r + ',' + c;
  function attacksBetween(r1, c1, r2, c2){
    const dr = Math.abs(r1 - r2), dc = Math.abs(c1 - c2);
    return (dr === 2 && dc === 1) || (dr === 1 && dc === 2);
  }
  function render(){
    const board = document.getElementById('c8s16Board');
    if(!board) return;
    board.innerHTML = '';
    const coords = [...knights].map(s => s.split(',').map(Number));
    const threatened = new Set();
    let conflicts = 0;
    coords.forEach(([r1, c1], i) => {
      [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]].forEach(([dr, dc]) => {
        const nr = r1 + dr, nc = c1 + dc;
        if(nr >= 0 && nr < 8 && nc >= 0 && nc < 8) threatened.add(key(nr, nc));
      });
      for(let j = i + 1; j < coords.length; j++){
        if(attacksBetween(r1, c1, coords[j][0], coords[j][1])) conflicts++;
      }
    });
    for(let r = 0; r < 8; r++){
      for(let c = 0; c < 8; c++){
        const k = key(r, c);
        const hasK = knights.has(k);
        const isDark = (r + c) % 2 === 1;
        const isHit = threatened.has(k);
        const btn = document.createElement('button');
        btn.type = 'button';
        let bg = isDark ? 'bg-slate-800' : 'bg-slate-600/70';
        if(hasK && isHit) bg = 'bg-rose-600';
        else if(hasK) bg = 'bg-emerald-600';
        else if(isHit) bg = isDark ? 'bg-rose-950/80 border-rose-500/40' : 'bg-rose-900/50 border-rose-400/40';
        btn.className = `aspect-square flex items-center justify-center text-sm sm:text-base rounded-[2px] border border-slate-700/50 ${bg}`;
        btn.textContent = hasK ? '♞' : (isHit ? '•' : '');
        btn.onclick = () => {
          if(knights.has(k)) knights.delete(k); else knights.add(k);
          render();
        };
        board.appendChild(btn);
      }
    }
    const cnt = knights.size;
    document.getElementById('c8s16Cnt').textContent = cnt;
    document.getElementById('c8s16Pct').textContent = ((cnt / 64) * 100).toFixed(1).replace(/\\.0$/, '') + '%';
    const atkEl = document.getElementById('c8s16Atk');
    atkEl.textContent = conflicts === 0 ? '0 (Peaceful!)' : conflicts + ' attack pairs!';
    atkEl.className = conflicts === 0 ? 'text-emerald-300 font-bold' : 'text-rose-400 font-bold';
  }
  window.c8s16Preset = function(mode){
    knights.clear();
    if(mode === 'col'){
      for(let r = 0; r < 8; r++) knights.add(key(r, 0));
    } else if(mode === 'dark'){
      for(let r = 0; r < 8; r++) for(let c = 0; c < 8; c++) if((r + c) % 2 === 1) knights.add(key(r, c));
    }
    render();
  };
  window.c8s16Preset('col');
})();
</script>
"""
}

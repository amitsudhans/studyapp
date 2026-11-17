#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 10: How Quantities Combine: Understanding Data
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Interactive Cluster vs Stacked Column SVG Toggle
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c10s9Set('stacked')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">Stacked Columns (Totals + Parts)</button>
    <button onclick="c9c10s9Set('cluster')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">Cluster Columns (Baseline-Zero)</button>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c10s9Svg" viewBox="0 0 260 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c10s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  const yrs = [
    {lbl: '2023', a: 30, b: 25, c: 20},
    {lbl: '2024', a: 35, b: 30, c: 30},
    {lbl: '2025', a: 40, b: 35, c: 45}
  ];
  window.c9c10s9Set = function(mode){
    const base = 130, sc = 0.85;
    let svg = `<line x1="20" y1="${base}" x2="245" y2="${base}" stroke="#475569" stroke-width="1.5"/>`;
    yrs.forEach((d, idx) => {
      const gx = 45 + idx * 72;
      if(mode === 'stacked'){
        const ha = d.a*sc, hb = d.b*sc, hc = d.c*sc;
        svg += `<rect x="${gx}" y="${base-ha}" width="30" height="${ha}" fill="#22d3ee"/>`;
        svg += `<rect x="${gx}" y="${base-ha-hb}" width="30" height="${hb}" fill="#fbbf24"/>`;
        svg += `<rect x="${gx}" y="${base-ha-hb-hc}" width="30" height="${hc}" fill="#34d399"/>`;
        svg += `<text x="${gx+15}" y="${base-ha-hb-hc-5}" text-anchor="middle" fill="#e2e8f0" font-size="9">${d.a+d.b+d.c}</text>`;
        svg += `<text x="${gx+15}" y="${base+12}" text-anchor="middle" fill="#94a3b8" font-size="9">${d.lbl}</text>`;
      } else {
        svg += `<rect x="${gx-10}" y="${base-d.a*sc}" width="13" height="${d.a*sc}" fill="#22d3ee"/>`;
        svg += `<rect x="${gx+5}" y="${base-d.b*sc}" width="13" height="${d.b*sc}" fill="#fbbf24"/>`;
        svg += `<rect x="${gx+20}" y="${base-d.c*sc}" width="13" height="${d.c*sc}" fill="#34d399"/>`;
        svg += `<text x="${gx+12}" y="${base+12}" text-anchor="middle" fill="#94a3b8" font-size="9">${d.lbl}</text>`;
      }
    });
    document.getElementById('c9c10s9Svg').innerHTML = svg;
    document.getElementById('c9c10s9Out').innerHTML = mode === 'stacked'
      ? `<div class="font-bold text-cyan-300">Stacked Column View</div><div>Top edge immediately reveals totals (75 → 95 → 120) while showing Arts, Commerce &amp; Science bands!</div>`
      : `<div class="font-bold text-amber-300">Cluster Column View</div><div>Every stream starts at baseline 0 for easy side-by-side comparison, though overall totals must be added manually.</div>`;
  };
  setTimeout(function(){ window.c9c10s9Set('stacked'); }, 40);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Stacked Bar Component Height Inspector
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Band A Top (from 0):</span><input id="c9c10s10A" type="number" min="5" max="80" value="40" oninput="c9c10s10Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Band B Top (Cumulative):</span><input id="c9c10s10B" type="number" min="10" max="150" value="95" oninput="c9c10s10Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Band C Top (Total):</span><input id="c9c10s10C" type="number" min="15" max="250" value="130" oninput="c9c10s10Draw()" class="w-full mt-1 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s10Draw = function(){
    const a = parseFloat(document.getElementById('c9c10s10A').value || '40');
    const b = Math.max(a, parseFloat(document.getElementById('c9c10s10B').value || '95'));
    const c = Math.max(b, parseFloat(document.getElementById('c9c10s10C').value || '130'));
    document.getElementById('c9c10s10Out').innerHTML = `
      <div>Band A = ${a} − 0 = <strong class="text-cyan-300">${a}</strong> &nbsp;|&nbsp; Band B = ${b} − ${a} = <strong class="text-amber-300">${b - a}</strong> &nbsp;|&nbsp; Band C = ${c} − ${b} = <strong class="text-emerald-300">${c - b}</strong></div>
      <div class="text-slate-400">Verification: ${a} + ${b - a} + ${c - b} = ${c} (Matches Overall Stack Height!)</div>
    `;
  };
  setTimeout(window.c9c10s10Draw, 40);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Absolute Stacked vs 100% Proportional Stacked Switcher
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c10s11Set('abs')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">Absolute Stacked Bars</button>
    <button onclick="c9c10s11Set('pct')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">100% Stacked Bars</button>
  </div>
  <div id="c9c10s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2.5"></div>
</div>
<script>
(function(){
  const cities = [
    {name: 'City A (Total 100)', solar: 20, wind: 30, coal: 50},
    {name: 'City B (Total 400)', solar: 120, wind: 80, coal: 200}
  ];
  window.c9c10s11Set = function(mode){
    const rows = cities.map(c => {
      const tot = c.solar + c.wind + c.coal;
      const scale = mode === 'pct' ? 100 / tot : 100 / 400;
      const w1 = (c.solar * scale).toFixed(1), w2 = (c.wind * scale).toFixed(1), w3 = (c.coal * scale).toFixed(1);
      return `<div>
        <div class="flex justify-between mb-1"><strong>${c.name}</strong><span>Solar ${Math.round(c.solar*100/tot)}% | Wind ${Math.round(c.wind*100/tot)}% | Coal ${Math.round(c.coal*100/tot)}%</span></div>
        <div class="w-full h-5 bg-slate-900 rounded overflow-hidden flex border border-slate-800">
          <div style="width:${w1}%" class="bg-amber-400 h-full"></div>
          <div style="width:${w2}%" class="bg-cyan-400 h-full"></div>
          <div style="width:${w3}%" class="bg-slate-600 h-full"></div>
        </div>
      </div>`;
    }).join('');
    document.getElementById('c9c10s11Out').innerHTML = rows + `<div class="text-cyan-300 pt-1">${mode === 'pct' ? '100% View: Both bars have equal length 100%, showing City B uses a higher solar share (30% vs 20%)!' : 'Absolute View: City B is 4× taller/wider in total energy (400 vs 100).'}</div>`;
  };
  setTimeout(function(){ window.c9c10s11Set('pct'); }, 40);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Household Energy Share &amp; Scale Trap Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Total Household Energy Multiplier (2020 vs 1990):</span>
      <span id="c9c10s12MLbl" class="text-amber-300 font-bold">2.0× Total Energy</span>
    </div>
    <input id="c9c10s12M" type="range" min="1" max="3" step="0.5" value="2" oninput="c9c10s12Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c10s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c10s12Draw = function(){
    const m = parseFloat(document.getElementById('c9c10s12M').value);
    document.getElementById('c9c10s12MLbl').textContent = m.toFixed(1) + '× Total Energy';
    const bio1990 = 60;
    const bio2020 = +(0.30 * (100 * m)).toFixed(1);
    document.getElementById('c9c10s12Out').innerHTML = `
      <div>1990: Biomass = 60% of 100 units = <strong class="text-cyan-300">60 units</strong></div>
      <div>2020: Biomass = 30% of ${100*m} units = <strong class="text-amber-300">${bio2020} units</strong></div>
      <div class="text-emerald-300 font-semibold">${bio2020 === bio1990 ? 'Notice! Even though biomass share halved (60% → 30%), absolute biomass stayed at 60 units!' : (bio2020 > bio1990 ? 'Absolute biomass actually INCREASED despite a smaller percentage!' : 'Absolute biomass decreased.')}</div>
    `;
  };
  setTimeout(window.c9c10s12Draw, 40);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🕒</span> 24-Hour Time Use Survey (2024) Stacked Bar Breakdown
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Demographic Profile:</span>
    <select id="c9c10s13Sel" onchange="c9c10s13Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="stu">Class 9 Student (24h Budget)</option>
      <option value="paid">Full-Time Worker (24h Budget)</option>
      <option value="care">Caregiver &amp; Homemaker (24h Budget)</option>
    </select>
  </label>
  <div id="c9c10s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const prof = {
    stu: {sleep: 8.5, work: 0, care: 1.5, learn: 8.0, leis: 6.0},
    paid: {sleep: 7.5, work: 8.5, care: 2.0, learn: 0.5, leis: 5.5},
    care: {sleep: 7.5, work: 1.5, care: 9.5, learn: 0.5, leis: 5.0}
  };
  window.c9c10s13Draw = function(){
    const d = prof[document.getElementById('c9c10s13Sel').value];
    const pct = h => ((h / 24) * 100).toFixed(1) + '%';
    document.getElementById('c9c10s13Out').innerHTML = `
      <div class="w-full h-6 rounded overflow-hidden flex border border-slate-700">
        <div style="width:${pct(d.sleep)}" class="bg-indigo-500 h-full" title="Sleep"></div>
        <div style="width:${pct(d.work)}" class="bg-cyan-400 h-full" title="Paid Work"></div>
        <div style="width:${pct(d.care)}" class="bg-amber-400 h-full" title="Unpaid Care"></div>
        <div style="width:${pct(d.learn)}" class="bg-emerald-400 h-full" title="Learning"></div>
        <div style="width:${pct(d.leis)}" class="bg-rose-400 h-full" title="Leisure"></div>
      </div>
      <div class="flex flex-wrap gap-2 text-[11px]">
        <span class="text-indigo-300">Sleep: ${d.sleep}h</span> •
        <span class="text-cyan-300">Paid Work: ${d.work}h</span> •
        <span class="text-amber-300">Unpaid Care: ${d.care}h</span> •
        <span class="text-emerald-300">Learning: ${d.learn}h</span> •
        <span class="text-rose-300">Leisure: ${d.leis}h</span>
      </div>
    `;
  };
  setTimeout(window.c9c10s13Draw, 40);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏏</span> Cricket Run Rate &amp; Share Portfolio Average Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Phase 1 (10 overs) Run Rate:</span><input id="c9c10s14R1" type="number" step="0.5" value="6.0" oninput="c9c10s14Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Death Overs (5 overs) Run Rate:</span><input id="c9c10s14R2" type="number" step="0.5" value="12.0" oninput="c9c10s14Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s14Draw = function(){
    const r1 = parseFloat(document.getElementById('c9c10s14R1').value || '6');
    const r2 = parseFloat(document.getElementById('c9c10s14R2').value || '12');
    const runs = 10*r1 + 5*9 + 5*r2;
    const rr = runs / 20;
    document.getElementById('c9c10s14Out').innerHTML = `
      <div>Middle Overs (5 overs) fixed at 9.0 runs/over = 45 runs.</div>
      <div class="font-bold text-emerald-300 text-sm">20-Over Total = ${runs.toFixed(1)} runs ⇒ Overall Run Rate = ${rr.toFixed(2)} runs/over</div>
    `;
  };
  setTimeout(window.c9c10s14Draw, 40);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🛰️</span> State Infrastructure &amp; Space Debris Stacked Data Analyzer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Dataset View:</span>
    <select id="c9c10s15Sel" onchange="c9c10s15Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="debris">Orbital Space Debris Growth (Absolute Stacked)</option>
      <option value="school">State School Playgrounds (100% Proportional Stacked)</option>
      <option value="census">Disability Census Distribution (100% Stacked)</option>
    </select>
  </label>
  <div id="c9c10s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const views = {
    debris: ['Active Satellites: 8,000 | Dead Spacecraft: 3,000 | Rocket Bodies: 2,000 | Fragmentation Debris: 23,000', 'Total Tracked Orbital Objects = 36,000. Fragmentation debris drives over 63% of total clutter!'],
    school: ['Large State (50,000 schools): 70% Playground (35,000) vs Small State (2,000 schools): 85% Playground (1,700)', '100% stacked bars compare equity fairly; absolute charts show 35,000 vs 1,700 raw count!'],
    census: ['Locomotor 40% | Visual 20% | Hearing 15% | Speech &amp; Other 25%', 'Out of 10,000 persons, 25% = 2,500 persons belong to Speech &amp; Other categories.']
  };
  window.c9c10s15Draw = function(){
    const [top, bot] = views[document.getElementById('c9c10s15Sel').value];
    document.getElementById('c9c10s15Out').innerHTML = `
      <div class="font-bold text-cyan-300">${top}</div>
      <div class="text-emerald-300">${bot}</div>
    `;
  };
  setTimeout(window.c9c10s15Draw, 40);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📚</span> Chapter 10 Complete Weighted Mean &amp; Chart Reference Matrix
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c10s16Show('wmean')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">Weighted Mean &amp; Alloys</button>
    <button onclick="c9c10s16Show('charts')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">Stacked vs 100% Charts</button>
  </div>
  <div id="c9c10s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cards = {
    wmean: `<div class="font-bold text-cyan-300 text-sm">Weighted Mean &amp; Mixture Formulas</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Combined Average:</strong> (an + bm)/(n + m); simple (a+b)/2 holds only if n = m or a = b</li>
        <li><strong>General Weighted Mean:</strong> x̄ = (W₁x₁ + ... + Wₙxₙ) / (W₁ + ... + Wₙ)</li>
        <li><strong>Gold Alloy Purity (Brahmagupta &amp; Śrīdharācārya):</strong> (Σ Wᵢkᵢ) / (Σ Wᵢ)</li>
        <li><strong>Custom Weights:</strong> Course rubrics, restaurant ratings, review recency, cricket run rates</li>
      </ul>`,
    charts: `<div class="font-bold text-emerald-300 text-sm">Visualising &amp; Interpreting Data</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Cluster Columns:</strong> Best for baseline-zero comparison of individual sub-categories</li>
        <li><strong>Stacked Columns/Bars:</strong> Show overall totals AND component parts (subtract bottom from top!)</li>
        <li><strong>100% Stacked Bars:</strong> Compare relative proportions across fixed lengths (replaces multi-pie charts)</li>
        <li><strong>Scale Caution:</strong> Always check total magnitude alongside percentage shares!</li>
      </ul>`
  };
  window.c9c10s16Show = function(k){
    document.getElementById('c9c10s16Out').innerHTML = cards[k] || cards.wmean;
  };
  setTimeout(function(){ window.c9c10s16Show('wmean'); }, 40);
})();
</script>
"""
}

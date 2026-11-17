#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 3: The World of Numbers
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏺</span> One-to-One Pebble Pot &amp; Bone Tally Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
      <div class="flex items-center justify-between">
        <span class="text-amber-300 font-semibold">Pastoral Clay Pot (ℕ)</span>
        <span id="c9c3s1Count" class="text-cyan-300 font-bold">5 sheep out</span>
      </div>
      <div class="flex gap-1.5 flex-wrap">
        <button type="button" onclick="c9c3s1Step(1)" class="px-2.5 py-1 rounded bg-emerald-600/30 border border-emerald-500/50 text-emerald-200 font-semibold">+1 Sheep Leaves</button>
        <button type="button" onclick="c9c3s1Step(-1)" class="px-2.5 py-1 rounded bg-rose-600/30 border border-rose-500/50 text-rose-200 font-semibold">-1 Sheep Returns</button>
        <button type="button" onclick="c9c3s1Reset()" class="px-2 py-1 rounded bg-slate-800 border border-slate-700 text-slate-300">Reset (5)</button>
      </div>
    </div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1.5">
      <div class="text-amber-300 font-semibold">Select Bone Tally Artifact</div>
      <div class="flex gap-1.5">
        <button type="button" onclick="c9c3s1Bone('lebombo')" id="c9c3s1bLeb" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">Lebombo (~35k BP)</button>
        <button type="button" onclick="c9c3s1Bone('ishango')" id="c9c3s1bIsh" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Ishango (~20k BCE)</button>
      </div>
    </div>
  </div>
  <svg id="c9c3s1Svg" viewBox="0 0 420 135" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c3s1Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  let pebbles = 5;
  let bone = 'lebombo';
  window.c9c3s1Step = function(delta){
    pebbles = Math.max(0, Math.min(12, pebbles + delta));
    c9c3s1Draw();
  };
  window.c9c3s1Reset = function(){ pebbles = 5; c9c3s1Draw(); };
  window.c9c3s1Bone = function(b){
    bone = b;
    const leb = document.getElementById('c9c3s1bLeb');
    const ish = document.getElementById('c9c3s1bIsh');
    if(leb && ish){
      leb.className = b==='lebombo' ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
      ish.className = b==='ishango' ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    }
    c9c3s1Draw();
  };
  window.c9c3s1Draw = function(){
    document.getElementById('c9c3s1Count').textContent = `${pebbles} pebbles in pot`;
    let potSvg = `<path d="M35 55 Q25 95 45 115 L115 115 Q135 95 125 55 Z" fill="#78350f" fill-opacity="0.45" stroke="#f59e0b" stroke-width="2"/>` +
                 `<ellipse cx="80" cy="55" rx="45" ry="9" fill="#451a03" stroke="#fbbf24" stroke-width="1.5"/>`;
    for(let i=0;i<pebbles;i++){
      const px = 48 + (i % 4) * 20;
      const py = 102 - Math.floor(i / 4) * 14;
      potSvg += `<circle cx="${px}" cy="${py}" r="6" fill="#38bdf8" stroke="#bae6fd" stroke-width="1"/>`;
    }
    potSvg += `<text x="80" y="25" fill="#cbd5e1" font-size="10" text-anchor="middle" font-weight="bold">ℕ Correspondence: ${pebbles}</text>`;
    let boneSvg = '';
    if(bone === 'lebombo'){
      boneSvg += `<rect x="175" y="45" width="225" height="36" rx="14" fill="#fef3c7" fill-opacity="0.16" stroke="#fde68a" stroke-width="2"/>`;
      for(let i=0;i<29;i++){
        const x = 190 + i * 7.1;
        boneSvg += `<line x1="${x}" y1="49" x2="${x}" y2="77" stroke="#facc15" stroke-width="1.8"/>`;
      }
      boneSvg += `<text x="287" y="30" fill="#fde047" font-size="10" text-anchor="middle" font-weight="bold">Lebombo Bone: 29 Lunar Cycle Notches</text>`;
      boneSvg += `<text x="287" y="106" fill="#94a3b8" font-size="9.5" text-anchor="middle">~35,000 BP • Southern Africa • 1-to-1 Day Tracking</text>`;
    } else {
      boneSvg += `<rect x="175" y="40" width="225" height="44" rx="14" fill="#e0f2fe" fill-opacity="0.12" stroke="#38bdf8" stroke-width="2"/>`;
      const primes = [11, 13, 17, 19];
      primes.forEach((p, idx) => {
        const gx = 190 + idx * 52;
        boneSvg += `<text x="${gx + 16}" y="67" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">${p}</text>`;
        boneSvg += `<rect x="${gx}" y="47" width="34" height="30" rx="5" fill="none" stroke="#34d399" stroke-opacity="0.5"/>`;
      });
      boneSvg += `<text x="287" y="28" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">Ishango Bone: Grouped Primes (11, 13, 17, 19) &amp; ×2</text>`;
      boneSvg += `<text x="287" y="106" fill="#94a3b8" font-size="9.5" text-anchor="middle">~20,000 BCE • Central Africa • Earliest Prime &amp; Doubling Tallies</text>`;
    }
    document.getElementById('c9c3s1Svg').innerHTML = potSvg + boneSvg;
    document.getElementById('c9c3s1Out').innerHTML = pebbles === 0
      ? `<strong class="text-emerald-300">Pot Empty!</strong> All sheep safely returned — 1-to-1 correspondence matches cleanly without written digits.`
      : `<strong class="text-cyan-300">${pebbles} pebble${pebbles>1?'s':''} inside pot</strong> — representing counting number ${pebbles} ∈ ℕ = {1, 2, 3, 4, ...}.`;
  };
  c9c3s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⚖️</span> Harappan Weights &amp; Ancient Indian Powers of 10
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Select Sanskrit Decimal Power Scale: <strong id="c9c3s2Name" class="text-amber-300">Parārdha (10¹²)</strong></span>
      <input type="range" id="c9c3s2Idx" min="0" max="6" value="5" oninput="c9c3s2Draw()" class="w-full accent-amber-400 mt-1.5">
    </label>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
      <div class="text-cyan-300 font-semibold">Indus Valley Ratio Family (Lothal &amp; Harappa)</div>
      <div class="text-slate-300">Binary: <span class="text-emerald-300 font-mono">1, 2, 4, 8, 16, 32, 64</span> → Decimal: <span class="text-amber-300 font-mono">160, 320, 640</span></div>
    </div>
  </div>
  <svg id="c9c3s2Svg" viewBox="0 0 420 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c3s2Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const scales = [
    { name:'Eka', pow:0, src:'Yajurveda', desc:'Unit base (10⁰ = 1)' },
    { name:'Śata', pow:2, src:'Yajurveda', desc:'Hundred (10² = 100)' },
    { name:'Sahasra', pow:3, src:'Yajurveda', desc:'Thousand (10³ = 1,000)' },
    { name:'Lakṣa', pow:5, src:'Yajurveda', desc:'One Hundred Thousand / Lakh (10⁵)' },
    { name:'Koṭi', pow:7, src:'Yajurveda', desc:'Ten Million / Crore (10⁷)' },
    { name:'Parārdha', pow:12, src:'Vedic Texts (Yajurveda)', desc:'One Trillion (10¹² = 1,000,000,000,000)' },
    { name:'Tallakṣaṇa', pow:53, src:'Lalitavistara', desc:'Cosmic Decimal Power 10⁵³ (stepping by 10² past Koṭi)' }
  ];
  window.c9c3s2Draw = function(){
    const idx = parseInt(document.getElementById('c9c3s2Idx').value);
    const sc = scales[idx];
    document.getElementById('c9c3s2Name').textContent = `${sc.name} (10^${sc.pow})`;
    const weights = [1,2,4,8,16,32,64,160,320];
    let svg = `<text x="14" y="20" fill="#22d3ee" font-size="9.5" font-weight="bold">Harappan Chert Cubical Weights Progression:</text>`;
    weights.forEach((w, i) => {
      const sz = 10 + i * 3.4;
      const x = 14 + i * 44;
      const y = 70 - sz / 2;
      svg += `<rect x="${x}" y="${y}" width="${sz}" height="${sz}" rx="2" fill="${i<7?'#10b981':'#f59e0b'}" fill-opacity="0.32" stroke="${i<7?'#34d399':'#fbbf24'}" stroke-width="1.5"/>`;
      svg += `<text x="${x + sz/2}" y="106" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${w}</text>`;
    });
    document.getElementById('c9c3s2Svg').innerHTML = svg;
    document.getElementById('c9c3s2Out').innerHTML = `
      <div class="flex justify-between items-center"><strong class="text-amber-300 text-sm">${sc.name} = 10<sup>${sc.pow}</sup></strong><span class="px-2 py-0.5 rounded bg-slate-800 text-cyan-300">${sc.src}</span></div>
      <p class="mt-1">${sc.desc}</p>
    `;
  };
  c9c3s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>🟣</span> Bakhśhālī Bindu &amp; Brahmagupta's Zero Laws Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Test Number a: <strong id="c9c3s3AVal" class="text-cyan-300">7</strong></span>
      <input type="range" id="c9c3s3A" min="-9" max="12" value="7" oninput="c9c3s3Draw()" class="w-full accent-purple-400 mt-1.5">
    </label>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-between">
      <div>
        <div class="text-purple-300 font-semibold">Bakhśhālī Manuscript Place Value</div>
        <div class="text-slate-400">Bindu dot (●) marks empty tens place</div>
      </div>
      <div class="px-3 py-1 rounded-lg bg-purple-950/60 border border-purple-500/40 font-mono text-base text-amber-300">3●5 → 305</div>
    </div>
  </div>
  <div id="c9c3s3Out" class="grid grid-cols-2 gap-2.5 text-xs"></div>
</div>
<script>
(function(){
  window.c9c3s3Draw = function(){
    const a = parseInt(document.getElementById('c9c3s3A').value);
    document.getElementById('c9c3s3AVal').textContent = a;
    const cards = [
      { title:'Additive Inverse', eq:`(${a}) − (${a}) = 0`, rule:'a − a = 0 (zero as exact balance)', col:'cyan' },
      { title:'Additive Identity (+)', eq:`(${a}) + 0 = ${a}`, rule:'a + 0 = a (adding zero leaves unchanged)', col:'emerald' },
      { title:'Zero Subtraction (−)', eq:`(${a}) − 0 = ${a}`, rule:'a − 0 = a (subtracting zero leaves unchanged)', col:'amber' },
      { title:'Zero Multiplication (×)', eq:`(${a}) × 0 = 0`, rule:'a × 0 = 0 (collapses product to zero)', col:'purple' }
    ];
    document.getElementById('c9c3s3Out').innerHTML = cards.map(c => `
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
        <div class="text-${c.col}-300 font-bold">${c.title}</div>
        <div class="text-base font-mono text-white mt-1">${c.eq}</div>
        <div class="text-slate-400 mt-1">${c.rule}</div>
      </div>
    `).join('');
  };
  c9c3s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>💰</span> Dhana (Fortune +) &amp; Riṇa (Debt −) Integer Balance Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Factor a (Action / Sign): <strong id="c9c3s4AVal" class="text-rose-300">-3</strong></span>
      <input type="range" id="c9c3s4A" min="-5" max="5" value="-3" oninput="c9c3s4Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Factor b (Fortune/Debt Item): <strong id="c9c3s4BVal" class="text-rose-300">-4</strong></span>
      <input type="range" id="c9c3s4B" min="-6" max="6" value="-4" oninput="c9c3s4Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <svg id="c9c3s4Svg" viewBox="0 0 420 85" class="w-full h-24 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c3s4Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1"></div>
</div>
<script>
(function(){
  window.c9c3s4Draw = function(){
    const a = parseInt(document.getElementById('c9c3s4A').value);
    const b = parseInt(document.getElementById('c9c3s4B').value);
    const prod = a * b;
    document.getElementById('c9c3s4AVal').textContent = a > 0 ? `+${a}` : a;
    document.getElementById('c9c3s4BVal').textContent = b > 0 ? `+${b}` : b;
    let svg = `<line x1="20" y1="45" x2="400" y2="45" stroke="#475569" stroke-width="2"/>`;
    for(let x=-10;x<=10;x+=2){
      const px = 210 + x * 17;
      svg += `<line x1="${px}" y1="40" x2="${px}" y2="50" stroke="#94a3b8" stroke-width="1.2"/>`;
      svg += `<text x="${px}" y="65" fill="${x<0?'#fb7185':(x>0?'#34d399':'#fbbf24')}" font-size="8.5" text-anchor="middle">${x}</text>`;
    }
    const cx = Math.max(25, Math.min(395, 210 + Math.max(-10, Math.min(10, prod/3)) * 17));
    svg += `<text x="70" y="20" fill="#fb7185" font-size="9.5" font-weight="bold">← Riṇa (Debts −)</text>`;
    svg += `<text x="345" y="20" fill="#34d399" font-size="9.5" font-weight="bold" text-anchor="end">Dhana (Fortunes +) →</text>`;
    svg += `<circle cx="210" cy="45" r="4" fill="#fbbf24"/>`;
    document.getElementById('c9c3s4Svg').innerHTML = svg;
    let logic = '';
    if(a < 0 && b < 0) logic = `Removing (× negative) ${Math.abs(a)} debts of (${b}) wipes debt away → net FORTUNE GAIN +${prod}!`;
    else if(a < 0 && b > 0) logic = `Losing ${Math.abs(a)} fortunes of +${b} creates a DEBT of ${prod}!`;
    else if(a > 0 && b < 0) logic = `Taking on ${a} debts of (${b}) builds a DEBT of ${prod}!`;
    else if(a > 0 && b > 0) logic = `Adding ${a} fortunes of +${b} creates a FORTUNE of +${prod}!`;
    else logic = `Multiplying by 0 yields 0 (Brahmagupta's zero product law).`;
    document.getElementById('c9c3s4Out').innerHTML = `
      <div class="text-sm font-bold ${prod>=0?'text-emerald-300':'text-rose-300'}">(${a}) × (${b}) = ${prod > 0 ? '+'+prod : prod} ∈ ℤ</div>
      <p>${logic}</p>
    `;
  };
  c9c3s4Draw();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>➗</span> Rational Equivalence (ad = bc) &amp; Co-Prime Reducer (ℚ)
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">p (num 1)<input type="number" id="c9c3s5p" value="-6" oninput="c9c3s5Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold px-2 py-1 rounded border border-slate-700"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">q (den 1 ≠ 0)<input type="number" id="c9c3s5q" value="15" oninput="c9c3s5Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold px-2 py-1 rounded border border-slate-700"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">r (num 2)<input type="number" id="c9c3s5r" value="14" oninput="c9c3s5Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold px-2 py-1 rounded border border-slate-700"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">s (den 2 ≠ 0)<input type="number" id="c9c3s5s" value="-35" oninput="c9c3s5Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold px-2 py-1 rounded border border-slate-700"></label>
  </div>
  <div id="c9c3s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  function gcd(a, b){ a=Math.abs(a); b=Math.abs(b); while(b){ const t=a%b; a=b; b=t; } return a || 1; }
  function reduceStd(n, d){
    if(d < 0){ n = -n; d = -d; }
    const g = gcd(n, d);
    return `${n/g}/${d/g}`;
  }
  window.c9c3s5Draw = function(){
    const p = parseInt(document.getElementById('c9c3s5p').value)||0;
    const q = parseInt(document.getElementById('c9c3s5q').value)||0;
    const r = parseInt(document.getElementById('c9c3s5r').value)||0;
    const s = parseInt(document.getElementById('c9c3s5s').value)||0;
    const out = document.getElementById('c9c3s5Out');
    if(q===0 || s===0){
      out.innerHTML = `<div class="text-rose-400 font-bold">Undefined Rational! Denominator strictly requires q ≠ 0 and s ≠ 0.</div>`;
      return;
    }
    const lhs = p * s, rhs = q * r, eq = lhs === rhs;
    out.innerHTML = `
      <div class="flex flex-wrap gap-3 items-center justify-between">
        <div>Cross-Product Test: <span class="font-mono text-cyan-300">(${p})×(${s}) = ${lhs}</span> vs <span class="font-mono text-amber-300">(${q})×(${r}) = ${rhs}</span></div>
        <span class="px-2.5 py-1 rounded font-bold ${eq?'bg-emerald-500/20 text-emerald-300':'bg-rose-500/20 text-rose-300'}">${eq ? 'EQUIVALENT RATIONALS' : 'NOT EQUIVALENT'}</span>
      </div>
      <div class="grid grid-cols-2 gap-2 pt-1">
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Co-Prime Form 1: <strong class="text-cyan-300">${reduceStd(p,q)}</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Co-Prime Form 2: <strong class="text-amber-300">${reduceStd(r,s)}</strong></div>
      </div>
    `;
  };
  c9c3s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-indigo-300 flex items-center gap-2">
    <span>📏</span> Number Line Segment Distance |a − b| &amp; Midpoint Density
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Point a = p₁/4: <strong id="c9c3s6AVal" class="text-cyan-300">-3/4</strong></span>
      <input type="range" id="c9c3s6A" min="-8" max="8" value="-3" oninput="c9c3s6Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Point b = p₂/4: <strong id="c9c3s6BVal" class="text-amber-300">5/4</strong></span>
      <input type="range" id="c9c3s6B" min="-8" max="8" value="5" oninput="c9c3s6Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <svg id="c9c3s6Svg" viewBox="0 0 420 90" class="w-full h-24 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c3s6Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c3s6Draw = function(){
    const n1 = parseInt(document.getElementById('c9c3s6A').value);
    const n2 = parseInt(document.getElementById('c9c3s6B').value);
    document.getElementById('c9c3s6AVal').textContent = `${n1}/4 (${(n1/4).toFixed(2)})`;
    document.getElementById('c9c3s6BVal').textContent = `${n2}/4 (${(n2/4).toFixed(2)})`;
    const toX = v => 210 + v * 22;
    const ax = toX(n1), bx = toX(n2), mx = (ax + bx)/2;
    let svg = `<line x1="20" y1="50" x2="400" y2="50" stroke="#475569" stroke-width="2"/>`;
    for(let q=-8;q<=8;q++){
      const x = toX(q), isInt = q%4===0;
      svg += `<line x1="${x}" y1="${isInt?41:45}" x2="${x}" y2="${isInt?59:55}" stroke="${isInt?'#cbd5e1':'#64748b'}" stroke-width="${isInt?2:1}"/>`;
      if(isInt) svg += `<text x="${x}" y="74" fill="#cbd5e1" font-size="9" text-anchor="middle">${q/4}</text>`;
    }
    svg += `<line x1="${ax}" y1="30" x2="${bx}" y2="30" stroke="#818cf8" stroke-width="2.5"/>`;
    svg += `<circle cx="${ax}" cy="50" r="5" fill="#22d3ee"/><text x="${ax}" y="22" fill="#22d3ee" font-size="9" text-anchor="middle">a</text>`;
    svg += `<circle cx="${bx}" cy="50" r="5" fill="#fbbf24"/><text x="${bx}" y="22" fill="#fbbf24" font-size="9" text-anchor="middle">b</text>`;
    if(n1 !== n2) svg += `<circle cx="${mx}" cy="50" r="4.5" fill="#34d399"/><text x="${mx}" y="14" fill="#34d399" font-size="8.5" text-anchor="middle">midpoint</text>`;
    document.getElementById('c9c3s6Svg').innerHTML = svg;
    const distNum = Math.abs(n1 - n2);
    const midNum = n1 + n2;
    document.getElementById('c9c3s6Out').innerHTML = `
      <div>Distance |a − b| = |(${n1}/4) − (${n2}/4)| = <strong class="text-indigo-300">${distNum}/4 = ${(distNum/4).toFixed(2)} units</strong></div>
      <div class="mt-1">Midpoint (a + b)/2 = <strong class="text-emerald-300">${midNum}/8 = ${(midNum/8).toFixed(3)}</strong> ${n1!==n2?'(strictly between a & b — infinitely repeatable density!)':'(choose a ≠ b to observe density midpoint)'}</div>
    `;
  };
  c9c3s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>📐</span> Baudhāyana's √2 Square Diagonal &amp; Contradiction Proof Stepper
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s7Step(0)" id="c9c3s7b0" class="px-2.5 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-semibold">1. Unit Square</button>
    <button type="button" onclick="c9c3s7Step(1)" id="c9c3s7b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2. Assume Co-Prime</button>
    <button type="button" onclick="c9c3s7Step(2)" id="c9c3s7b2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">3. p Is Even</button>
    <button type="button" onclick="c9c3s7Step(3)" id="c9c3s7b3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">4. Contradiction!</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg viewBox="0 0 150 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800 shrink-0">
      <rect x="30" y="25" width="75" height="75" fill="#0f766e" fill-opacity="0.25" stroke="#2dd4bf" stroke-width="2"/>
      <line x1="30" y1="100" x2="105" y2="25" stroke="#fb7185" stroke-width="2.5"/>
      <text x="67" y="114" fill="#5eead4" font-size="9.5" text-anchor="middle">side = 1</text>
      <text x="115" y="65" fill="#5eead4" font-size="9.5">1</text>
      <text x="65" y="57" fill="#fb7185" font-size="10.5" font-weight="bold" transform="rotate(-45 65 57)">d = √2</text>
    </svg>
    <div id="c9c3s7Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const steps = [
    { t:'Step 1: Baudhāyana Śulbasūtras (~800 BCE)', m:'Unit square with side 1 has diagonal d² = 1² + 1² = 2 ⇒ d = √2 ≈ 1.4142135...' },
    { t:'Step 2: Hippasus Contradiction Assumption', m:'Suppose √2 = p/q is rational in lowest co-prime terms: HCF(p, q) = 1. Squaring gives 2q² = p².' },
    { t:'Step 3: Even Parity Transfer', m:'Since p² = 2q² is even, p must be even (p = 2k). Substituting gives 2q² = 4k² ⇒ q² = 2k², forcing q ALSO even!' },
    { t:'Step 4: Fatal Contradiction (2 divides both p & q)', m:'Both p and q divisible by 2 contradicts HCF(p, q) = 1! Therefore √2 CANNOT be expressed as any rational p/q.' }
  ];
  window.c9c3s7Step = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c9c3s7b'+k);
      if(b) b.className = k===i ? 'px-2.5 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const d = steps[i];
    document.getElementById('c9c3s7Out').innerHTML = `<div class="text-rose-300 font-bold text-sm">${d.t}</div><p class="leading-relaxed">${d.m}</p>`;
  };
  c9c3s7Step(0);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧭</span> Compass &amp; Straightedge Construction of √n (Spiral &amp; Line Drop)
  </h3>
  <div class="flex items-center justify-between text-xs bg-slate-950 p-2.5 rounded-xl border border-slate-800">
    <span>Target Irrational Radical: <strong id="c9c3s8Lbl" class="text-emerald-300 text-sm">√2 ≈ 1.414</strong></span>
    <div class="flex gap-1.5">
      <button type="button" onclick="c9c3s8Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-emerald-600/30 border border-slate-700">√2</button>
      <button type="button" onclick="c9c3s8Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-emerald-600/30 border border-slate-700">√3</button>
      <button type="button" onclick="c9c3s8Pick(5)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-emerald-600/30 border border-slate-700">√5</button>
      <button type="button" onclick="c9c3s8Pick(6)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-emerald-600/30 border border-slate-700">√6</button>
    </div>
  </div>
  <svg id="c9c3s8Svg" viewBox="0 0 420 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c3s8Out" class="text-xs text-slate-300 px-1"></div>
</div>
<script>
(function(){
  window.c9c3s8Pick = function(n){
    const val = Math.sqrt(n);
    document.getElementById('c9c3s8Lbl').textContent = `√${n} ≈ ${val.toFixed(4)}`;
    const base = n === 5 ? 2 : Math.sqrt(n - 1);
    const scale = 72;
    const ox = 55, oy = 112;
    const ax = ox + base * scale, ay = oy;
    const bx = ax, by = oy - scale;
    const r = Math.hypot(ax - ox, by - oy);
    const dx = ox + r;
    let svg = `<line x1="25" y1="${oy}" x2="395" y2="${oy}" stroke="#475569" stroke-width="2"/>`;
    for(let k=0;k<=3;k++){
      const tx = ox + k * scale;
      svg += `<line x1="${tx}" y1="${oy-4}" x2="${tx}" y2="${oy+4}" stroke="#94a3b8"/><text x="${tx}" y="${oy+15}" fill="#94a3b8" font-size="9" text-anchor="middle">${k}</text>`;
    }
    svg += `<line x1="${ox}" y1="${oy}" x2="${ax}" y2="${ay}" stroke="#38bdf8" stroke-width="2.5"/>`;
    svg += `<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#fbbf24" stroke-width="2.5"/>`;
    svg += `<line x1="${ox}" y1="${oy}" x2="${bx}" y2="${by}" stroke="#34d399" stroke-width="2.5"/>`;
    svg += `<path d="M ${bx} ${by} A ${r} ${r} 0 0 1 ${dx} ${oy}" fill="none" stroke="#f472b6" stroke-width="1.8" stroke-dasharray="4 3"/>`;
    svg += `<circle cx="${dx}" cy="${oy}" r="4.5" fill="#f472b6"/><text x="${dx}" y="${oy-8}" fill="#f472b6" font-size="10" font-weight="bold" text-anchor="middle">√${n}</text>`;
    svg += `<text x="${(ox+ax)/2}" y="${oy+14}" fill="#38bdf8" font-size="9" text-anchor="middle">${n===5?'2':'√'+(n-1)}</text>`;
    svg += `<text x="${ax+8}" y="${(ay+by)/2}" fill="#fbbf24" font-size="9">1</text>`;
    document.getElementById('c9c3s8Svg').innerHTML = svg;
    document.getElementById('c9c3s8Out').innerHTML = `Base leg <strong class="text-cyan-300">${n===5?'2':'√'+(n-1)}</strong> + perpendicular <strong class="text-amber-300">1</strong> → Hypotenuse = <strong class="text-emerald-300">√(${n-1}+1) = √${n}</strong> → Compass arc drops point cleanly onto axis!`;
  };
  c9c3s8Pick(2);
})();
</script>
"""
}

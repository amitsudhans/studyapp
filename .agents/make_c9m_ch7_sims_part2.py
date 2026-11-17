#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 7: The Mathematics of Maybe: Introduction to Probability
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Law of Large Numbers Convergence &amp; Gambler's Fallacy Check
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c7s9Sim(10)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">Run 10 Flips</button>
    <button onclick="c9c7s9Sim(100)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">100 Flips</button>
    <button onclick="c9c7s9Sim(1000)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">1,000 Flips</button>
    <button onclick="c9c7s9Sim(10000)" class="px-2.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold">10,000 Flips</button>
  </div>
  <div id="c9c7s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c7s9Sim = function(N){
    let h = 0;
    for(let i=0; i<N; i++) if(Math.random() < 0.5) h++;
    const freq = h / N;
    const diff = Math.abs(freq - 0.5).toFixed(4);
    document.getElementById('c9c7s9Out').innerHTML = `
      <div class="font-bold text-cyan-300">Trials N = ${N.toLocaleString()} | Heads Observed = ${h.toLocaleString()}</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">Empirical P(H) = ${freq.toFixed(4)} (Distance from 0.5000 = ${diff})</div>
      <div class="text-[11px] text-amber-300 font-semibold">Gambler's Fallacy Check: Even after 6 Heads in a row, the very next flip STILL has P(Head) = 0.5000 because coins have zero memory!</div>
    `;
  };
  c9c7s9Sim(1000);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🗂️</span> Sample Space Set Builder: S &amp; Sample Size n(S)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Choose Random Experiment:</span>
    <select id="c9c7s10Exp" onchange="c9c7s10Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
      <option value="c1">Tossing 1 Coin</option>
      <option value="d1">Rolling 1 Fair Die</option>
      <option value="c2" selected>Tossing 2 Fair Coins</option>
      <option value="c3">Tossing 3 Fair Coins</option>
    </select>
  </label>
  <div id="c9c7s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const map = {
    c1: {s:'{H, T}', n:2, note:'Two distinct faces on a single coin.'},
    d1: {s:'{1, 2, 3, 4, 5, 6}', n:6, note:'Six distinct numbered faces on a cubic die.'},
    c2: {s:'{HH, HT, TH, TT}', n:4, note:'HT (Coin 1 H, Coin 2 T) differs from TH (Coin 1 T, Coin 2 H) ⇒ n(S) = 4, NOT 3!'},
    c3: {s:'{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}', n:8, note:'2 × 2 × 2 = 8 distinct equally likely 3-toss sequences.'}
  };
  window.c9c7s10Draw = function(){
    const d = map[document.getElementById('c9c7s10Exp').value];
    document.getElementById('c9c7s10Out').innerHTML = `
      <div class="font-mono text-cyan-300 font-bold text-sm">Sample Space S = ${d.s}</div>
      <div class="font-bold text-emerald-300">Sample Size n(S) = ${d.n}</div>
      <div class="text-[11px] text-slate-400">${d.note}</div>
    `;
  };
  c9c7s10Draw();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎲🎲</span> Two-Dice 36-Outcome Matrix &amp; Target Sum Explorer
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Highlight Pairs with Sum = <strong id="c9c7s11SumVal" class="text-amber-300">7</strong></span>
    <input type="range" id="c9c7s11Sum" min="2" max="12" value="7" oninput="c9c7s11Draw()" class="w-full accent-amber-400 mt-1">
  </label>
  <div id="c9c7s11Grid" class="grid grid-cols-6 gap-1 p-2 bg-slate-950 rounded-xl border border-slate-800 text-[10px] font-mono text-center"></div>
  <div id="c9c7s11Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c7s11Draw = function(){
    const target = parseInt(document.getElementById('c9c7s11Sum').value);
    document.getElementById('c9c7s11SumVal').textContent = target;
    let html = '', hits = 0;
    for(let r=1; r<=6; r++){
      for(let c=1; c<=6; c++){
        const ok = (r + c === target);
        if(ok) hits++;
        html += `<div class="py-1 rounded border ${ok ? 'bg-amber-500/30 border-amber-400 text-amber-200 font-bold' : 'bg-slate-900 border-slate-800 text-slate-500'}">(${r},${c})</div>`;
      }
    }
    document.getElementById('c9c7s11Grid').innerHTML = html;
    document.getElementById('c9c7s11Out').innerHTML = `
      <span class="font-bold text-cyan-300">n(S) = 6 × 6 = 36 | Favourable Pairs Summing to ${target} = ${hits} ⇒ P(Sum = ${target}) = ${hits}/36 = ${(hits/36).toFixed(3)}</span>
    `;
  };
  c9c7s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧩</span> Events as Subsets (E ⊆ S) &amp; Complement P(not E) = 1 − P(E)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Event E on Fair Die S = {1, 2, 3, 4, 5, 6}:</span>
    <select id="c9c7s12Evt" onchange="c9c7s12Draw()" class="w-full mt-1 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
      <option value="gt4">Number strictly greater than 4</option>
      <option value="even">Even number</option>
      <option value="prime">Prime number</option>
      <option value="imp">Number equal to 7 (Impossible ∅)</option>
      <option value="sure">Integer from 1 to 6 (Sure Event S)</option>
    </select>
  </label>
  <div id="c9c7s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const evts = {
    gt4: {e:'{5, 6}', ne:'{1, 2, 3, 4}', k:2},
    even: {e:'{2, 4, 6}', ne:'{1, 3, 5}', k:3},
    prime: {e:'{2, 3, 5}', ne:'{1, 4, 6}', k:3},
    imp: {e:'∅ (Empty)', ne:'{1, 2, 3, 4, 5, 6}', k:0},
    sure: {e:'{1, 2, 3, 4, 5, 6}', ne:'∅ (Empty)', k:6}
  };
  window.c9c7s12Draw = function(){
    const d = evts[document.getElementById('c9c7s12Evt').value];
    document.getElementById('c9c7s12Out').innerHTML = `
      <div class="font-mono text-emerald-300 font-bold">Subset E = ${d.e} ⇒ P(E) = ${d.k}/6 = ${(d.k/6).toFixed(3)}</div>
      <div class="font-mono text-amber-300 font-bold">Complement not-E = ${d.ne} ⇒ P(not E) = 1 − ${d.k}/6 = ${6-d.k}/6 = ${((6-d.k)/6).toFixed(3)}</div>
      <div class="text-[11px] text-cyan-300">Verify Sum: P(E) + P(not E) = ${d.k}/6 + ${6-d.k}/6 = 1!</div>
    `;
  };
  c9c7s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-violet-300 flex items-center gap-2">
    <span>🌿</span> Multi-Step Tree Diagram Visualizer
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Two-Stage Experiment:</span>
    <select id="c9c7s13Scen" onchange="c9c7s13Draw()" class="w-full mt-1 bg-slate-900 text-violet-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
      <option value="coins">Tossing 2 Fair Coins (2 × 2 = 4 Paths)</option>
      <option value="fruit">Fruit Baskets: {Apple, Banana} × {Orange, Mango, Guava} (6 Paths)</option>
    </select>
  </label>
  <svg id="c9c7s13Svg" viewBox="0 0 280 125" class="w-full max-w-md mx-auto h-32 bg-slate-950 rounded-xl border border-slate-800 block"></svg>
</div>
<script>
(function(){
  window.c9c7s13Draw = function(){
    const sc = document.getElementById('c9c7s13Scen').value;
    const svg = document.getElementById('c9c7s13Svg');
    if(sc === 'coins'){
      svg.innerHTML = `
        <circle cx="20" cy="62" r="4" fill="#fbbf24"/>
        <line x1="20" y1="62" x2="110" y2="32" stroke="#38bdf8" stroke-width="2"/>
        <line x1="20" y1="62" x2="110" y2="92" stroke="#34d399" stroke-width="2"/>
        <text x="65" y="42" fill="#38bdf8" font-size="9" font-weight="bold">H</text>
        <text x="65" y="88" fill="#34d399" font-size="9" font-weight="bold">T</text>
        <line x1="110" y1="32" x2="210" y2="18" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="110" y1="32" x2="210" y2="46" stroke="#34d399" stroke-width="1.5"/>
        <line x1="110" y1="92" x2="210" y2="78" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="110" y1="92" x2="210" y2="106" stroke="#34d399" stroke-width="1.5"/>
        <text x="220" y="21" fill="#e2e8f0" font-size="9" font-weight="bold">HH (1/4)</text>
        <text x="220" y="49" fill="#e2e8f0" font-size="9" font-weight="bold">HT (1/4)</text>
        <text x="220" y="81" fill="#e2e8f0" font-size="9" font-weight="bold">TH (1/4)</text>
        <text x="220" y="109" fill="#e2e8f0" font-size="9" font-weight="bold">TT (1/4)</text>
      `;
    } else {
      const ys = [16, 36, 54, 74, 92, 112];
      const lbls = ['(Apple, Orange)', '(Apple, Mango)', '(Apple, Guava)', '(Banana, Orange)', '(Banana, Mango)', '(Banana, Guava)'];
      let lines = '';
      ys.forEach((y, i) => {
        const py = i < 3 ? 36 : 92;
        lines += `<line x1="100" y1="${py}" x2="180" y2="${y}" stroke="#a78bfa" stroke-width="1.4"/>
                  <text x="186" y="${y+3}" fill="#e2e8f0" font-size="8.5" font-weight="bold">${lbls[i]}</text>`;
      });
      svg.innerHTML = `
        <circle cx="20" cy="64" r="4" fill="#fbbf24"/>
        <line x1="20" y1="64" x2="100" y2="36" stroke="#22d3ee" stroke-width="2"/>
        <line x1="20" y1="64" x2="100" y2="92" stroke="#34d399" stroke-width="2"/>
        <text x="55" y="45" fill="#22d3ee" font-size="9" font-weight="bold">Apple</text>
        <text x="50" y="88" fill="#34d399" font-size="9" font-weight="bold">Banana</text>
        ${lines}
      `;
    }
  };
  c9c7s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✖️</span> Weighted Tree Branch Probability Multiplier
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Box 1 Red Pens (out of 3 total): <strong id="c9c7s14R1Val" class="text-rose-300">2 / 3</strong></span>
      <input type="range" id="c9c7s14R1" min="1" max="2" value="2" oninput="c9c7s14Draw()" class="w-full accent-rose-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Box 2 Red Pens (out of 4 total): <strong id="c9c7s14R2Val" class="text-cyan-300">1 / 4</strong></span>
      <input type="range" id="c9c7s14R2" min="1" max="3" value="1" oninput="c9c7s14Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
  </div>
  <div id="c9c7s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c7s14Draw = function(){
    const r1 = parseInt(document.getElementById('c9c7s14R1').value);
    const r2 = parseInt(document.getElementById('c9c7s14R2').value);
    document.getElementById('c9c7s14R1Val').textContent = `${r1} / 3`;
    document.getElementById('c9c7s14R2Val').textContent = `${r2} / 4`;
    const b1 = 3 - r1, b2 = 4 - r2;
    const rr = r1*r2, rb = r1*b2, br = b1*r2, bb = b1*b2;
    document.getElementById('c9c7s14Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2 font-mono text-xs">
        <div class="p-2 rounded bg-slate-900 border border-slate-800 text-rose-300">P(Red, Red) = (${r1}/3)(${r2}/4) = ${rr}/12</div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800 text-amber-300">P(Red, Blue) = (${r1}/3)(${b2}/4) = ${rb}/12</div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800 text-cyan-300">P(Blue, Red) = (${b1}/3)(${r2}/4) = ${br}/12</div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800 text-indigo-300">P(Blue, Blue) = (${b1}/3)(${b2}/4) = ${bb}/12</div>
      </div>
      <div class="text-emerald-300 font-bold">Total Sum of All 4 Leaves = (${rr}+${rb}+${br}+${bb})/12 = 12/12 = 1.00 ✓</div>
    `;
  };
  c9c7s14Draw();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🎯</span> Geometric Area Drop Probability Simulator (Favourable Area / Total Area)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Inner Fountain Circle Radius r (inside 10 m × 6 m Courtyard): <strong id="c9c7s15RVal" class="text-cyan-300">2.0 m</strong></span>
    <input type="range" id="c9c7s15R" min="0.5" max="2.8" step="0.1" value="2.0" oninput="c9c7s15Draw()" class="w-full accent-cyan-400 mt-1">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c7s15Svg" viewBox="0 0 180 110" class="w-44 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c7s15Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c7s15Draw = function(){
    const r = parseFloat(document.getElementById('c9c7s15R').value);
    document.getElementById('c9c7s15RVal').textContent = `${r.toFixed(1)} m`;
    const totalA = 60;
    const circA = Math.PI * r * r;
    const p = circA / totalA;
    document.getElementById('c9c7s15Svg').innerHTML = `
      <rect x="15" y="10" width="150" height="90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="90" cy="55" r="${(r*15).toFixed(1)}" fill="#06b6d4" fill-opacity="0.45" stroke="#22d3ee" stroke-width="2"/>
      <text x="90" y="58" fill="#fff" font-size="8.5" font-weight="bold" text-anchor="middle">r=${r.toFixed(1)}m</text>
    `;
    document.getElementById('c9c7s15Out').innerHTML = `
      <div class="font-bold text-cyan-300">Circle Area = πr² ≈ ${circA.toFixed(2)} m² | Courtyard Area = 10 × 6 = 60 m²</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">P(Random Drop Hits Circle) = ${circA.toFixed(2)} / 60 = ${p.toFixed(3)} (${(p*100).toFixed(1)}%)</div>
    `;
  };
  c9c7s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏆</span> Chapter 7 Complete Probability Reference Matrix
  </h3>
  <select id="c9c7s16Filter" onchange="c9c7s16Draw()" class="w-full sm:w-72 bg-slate-950 text-cyan-300 font-bold border border-slate-700 rounded-xl px-3 py-1.5 text-xs">
    <option value="all">All Chapter 7 Pillars (7.1–7.4)</option>
    <option value="scale">Scale, Randomness &amp; Jñān-Chaupad (7.1–7.2.1)</option>
    <option value="theory">Theoretical, Sampling &amp; Fallacy (7.2.2–7.2.3)</option>
    <option value="sets">Sample Spaces &amp; Subset Events (7.3)</option>
    <option value="trees">Tree Diagrams &amp; Geometric Area (7.4)</option>
  </select>
  <div id="c9c7s16Out" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs"></div>
</div>
<script>
(function(){
  const cards = [
    {g:'scale', title:'0–1 Probability Scale', body:'0 ≤ P(E) ≤ 1 always. 0 = Impossible, 0.5 = Even Chance, 1 = Certain. Random experiments have known S yet unpredictable single trials.'},
    {g:'scale', title:'Experimental Relative Frequency', body:'P(E) = Occurrences / Total Trials. Highlighted historically by ancient Indian Jñān-Chaupad (Snakes &amp; Ladders ancestor).'},
    {g:'theory', title:'Theoretical Ratio &amp; Equal Likelihood', body:'P(E) = Favourable / Total ONLY when outcomes are equally likely! Check unequal spinner angles θ°/360° carefully.'},
    {g:'theory', title:'Sampling, LLN &amp; Gambler’s Fallacy', body:'Scale representative samples (50 → 1,500). Law of Large Numbers stabilizes long runs; coins have zero memory (no Fallacy!).'},
    {g:'sets', title:'Sample Space S &amp; Events E', body:'S lists all distinct outcomes cleanly (n(S) = 4 for 2 coins, 36 for 2 dice). Event E ⊆ S; Complement P(not E) = 1 − P(E).'},
    {g:'trees', title:'Tree Diagrams &amp; Geometric Drops', body:'Multiply branch probabilities along paths, sum matching leaves (all leaves sum to 1). Geometric P = Favourable Area / Total Area.'}
  ];
  window.c9c7s16Draw = function(){
    const f = document.getElementById('c9c7s16Filter').value;
    const shown = f === 'all' ? cards : cards.filter(c => c.g === f);
    document.getElementById('c9c7s16Out').innerHTML = shown.map(c => `
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
        <div class="font-bold text-amber-300">${c.title}</div>
        <div class="text-slate-300 leading-relaxed">${c.body}</div>
      </div>
    `).join('');
  };
  c9c7s16Draw();
})();
</script>
"""
}

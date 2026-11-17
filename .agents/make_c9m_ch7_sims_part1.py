#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 7: The Mathematics of Maybe: Introduction to Probability
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎯</span> Objective Likelihood Gauge: Turning "Maybe" into Numbers
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Everyday Event:</span>
    <select id="c9c7s1Evt" onchange="c9c7s1Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="0">Rolling a 7 on a standard 6-sided die (Impossible)</option>
      <option value="0.1">Winning a 10-ticket lucky draw with 1 ticket (Unlikely)</option>
      <option value="0.5" selected>Fair coin toss landing Heads (Even Chance 50-50)</option>
      <option value="0.8">Dark monsoon clouds bringing evening rain (Likely)</option>
      <option value="1">Sun rising in the east tomorrow morning (Certain)</option>
    </select>
  </label>
  <div id="c9c7s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c7s1Draw = function(){
    const p = parseFloat(document.getElementById('c9c7s1Evt').value);
    const pct = Math.round(p * 100);
    const lbl = p === 0 ? 'IMPOSSIBLE (0%)' : p < 0.5 ? 'UNLIKELY' : p === 0.5 ? 'EVEN CHANCE (50%)' : p < 1 ? 'LIKELY' : 'CERTAIN (100%)';
    const col = p === 0 ? 'bg-rose-500' : p < 0.5 ? 'bg-amber-500' : p === 0.5 ? 'bg-cyan-400' : p < 1 ? 'bg-emerald-400' : 'bg-indigo-400';
    document.getElementById('c9c7s1Out').innerHTML = `
      <div class="flex justify-between font-bold text-sm">
        <span class="text-cyan-300">Probability P(E) = ${p.toFixed(2)} (${pct}%)</span>
        <span class="text-amber-300">${lbl}</span>
      </div>
      <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden">
        <div class="${col} h-3 transition-all duration-300" style="width:${pct}%"></div>
      </div>
      <div class="text-[11px] text-slate-400">Probability replaces vague guesses with a precise numerical measure between 0 and 1!</div>
    `;
  };
  c9c7s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🎲</span> Random Experiment Live Tester: Known Pool vs Unpredictable Single Trial
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c7s2Run('coin')" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold">🪙 Toss Fair Coin</button>
    <button onclick="c9c7s2Run('die')" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">🎲 Roll 6-Sided Die</button>
    <button onclick="c9c7s2Run('rain')" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold">🌧️ Simulate Weather Factor</button>
  </div>
  <div id="c9c7s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  let hist = [];
  window.c9c7s2Run = function(mode){
    let pool = '', res = '', note = '';
    if(mode === 'coin'){
      pool = '{Heads, Tails}';
      res = Math.random() < 0.5 ? 'Heads (H)' : 'Tails (T)';
      note = 'Known outcome pool, yet individual flip result cannot be predicted beforehand!';
    } else if(mode === 'die'){
      pool = '{1, 2, 3, 4, 5, 6}';
      res = 'Face ' + (Math.floor(Math.random()*6) + 1);
      note = 'All 6 faces are known before rolling, yet each next single roll stays uncertain!';
    } else {
      pool = '{Clear, Drizzle, Heavy Rain}';
      const opts = ['Clear Sky', 'Light Drizzle', 'Heavy Rain'];
      res = opts[Math.floor(Math.random()*3)];
      note = 'Rainfall is mathematically random due to extreme sensitivity to wind, pressure, temperature & humidity!';
    }
    hist.unshift(res);
    hist = hist.slice(0, 6);
    document.getElementById('c9c7s2Out').innerHTML = `
      <div class="font-bold text-cyan-300">Known Possible Outcomes Pool: ${pool}</div>
      <div class="font-mono text-emerald-300 text-sm font-bold">This Trial Outcome: ${res}</div>
      <div class="text-amber-300">Recent Sequence: ${hist.join(' → ')}</div>
      <div class="text-[11px] text-slate-400">${note}</div>
    `;
  };
  c9c7s2Run('die');
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-violet-300 flex items-center gap-2">
    <span>🃏</span> 6-Card Deck Visual Model on the 0-to-1 Probability Scale
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Number of Purple Cards (out of 6 total): <strong id="c9c7s3KVal" class="text-violet-300">3 Purple / 3 Green</strong></span>
    <input type="range" id="c9c7s3K" min="0" max="6" value="3" oninput="c9c7s3Draw()" class="w-full accent-violet-400 mt-1">
  </label>
  <div id="c9c7s3Cards" class="flex gap-2 justify-center flex-wrap p-2.5 bg-slate-950 rounded-xl border border-slate-800"></div>
  <div id="c9c7s3Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c7s3Draw = function(){
    const k = parseInt(document.getElementById('c9c7s3K').value);
    document.getElementById('c9c7s3KVal').textContent = `${k} Purple / ${6-k} Green`;
    let cards = '';
    for(let i=0; i<6; i++){
      const isP = i < k;
      cards += `<div class="w-10 h-14 rounded-lg border-2 flex items-center justify-center font-bold text-xs ${isP ? 'bg-violet-600/40 border-violet-400 text-violet-200' : 'bg-emerald-600/30 border-emerald-400 text-emerald-200'}">${isP ? 'P' : 'G'}</div>`;
    }
    const p = k / 6;
    const tag = k === 0 ? 'IMPOSSIBLE (0)' : k === 3 ? 'EVEN CHANCE (0.5)' : k === 6 ? 'CERTAIN (1)' : k < 3 ? 'Unlikely (< 0.5)' : 'Likely (> 0.5)';
    document.getElementById('c9c7s3Cards').innerHTML = cards;
    document.getElementById('c9c7s3Out').innerHTML = `
      <div class="flex justify-between font-bold">
        <span class="text-violet-300">P(Purple) = ${k}/6 = ${p.toFixed(3)}</span>
        <span class="text-amber-300">${tag}</span>
      </div>
      <div class="relative w-full h-3 bg-slate-800 rounded-full">
        <div class="absolute top-0 left-0 h-3 bg-gradient-to-r from-rose-500 via-amber-400 to-emerald-400 rounded-full" style="width:${(p*100).toFixed(1)}%"></div>
      </div>
      <div class="flex justify-between text-[10px] text-slate-400 font-mono"><span>0 (Impossible)</span><span>0.5 (Even)</span><span>1 (Certain)</span></div>
    `;
  };
  c9c7s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>⚖️</span> Dual Approach Comparator: Experimental Data vs Theoretical Symmetry
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c7s4Mode('fair')" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold">🎲 Symmetric Fair Die (Theory = 1/6)</button>
    <button onclick="c9c7s4Mode('cap')" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">🍾 Asymmetric Bottle Cap (Need Trials!)</button>
  </div>
  <div id="c9c7s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c7s4Mode = function(m){
    const out = document.getElementById('c9c7s4Out');
    if(m === 'fair'){
      out.innerHTML = `
        <div class="font-bold text-cyan-300">Approach: THEORETICAL PROBABILITY (Symmetry Reasoning)</div>
        <div class="text-slate-200">A balanced cube has 6 congruent faces ⇒ Zero trials needed to know P(rolling 6) = 1/6 ≈ 0.167!</div>
        <div class="text-[11px] text-emerald-300">Works whenever physical symmetry guarantees equally likely outcomes.</div>
      `;
    } else {
      let up = 0, N = 50;
      for(let i=0; i<N; i++) if(Math.random() < 0.62) up++;
      out.innerHTML = `
        <div class="font-bold text-amber-300">Approach: EXPERIMENTAL PROBABILITY (Physical Observation)</div>
        <div class="text-slate-200">Bottle caps are asymmetric! Running ${N} simulated tosses gave ${up} open-up landings ⇒ Empirical P ≈ ${(up/N).toFixed(2)}.</div>
        <div class="text-[11px] text-pink-300">Click again to see empirical frequency vary slightly across repeated experiments!</div>
      `;
    }
  };
  c9c7s4Mode('fair');
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🐍</span> Jñān-Chaupad Experimental Trials &amp; Relative Frequency Tracker
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c7s5Roll(1)" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold">+1 Die Throw</button>
    <button onclick="c9c7s5Roll(20)" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold">+20 Throws</button>
    <button onclick="c9c7s5Reset()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border border-slate-700">Reset</button>
  </div>
  <div id="c9c7s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  let total = 0, sixes = 0;
  window.c9c7s5Roll = function(k){
    for(let i=0; i<k; i++){
      total++;
      if(Math.floor(Math.random()*6)+1 === 6) sixes++;
    }
    const rel = total ? (sixes/total).toFixed(3) : '0.000';
    document.getElementById('c9c7s5Out').innerHTML = `
      <div class="font-bold text-cyan-300">Observed Event (Rolling a 6 on Jñān-Chaupad Die): ${sixes} times out of ${total} trials</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">Experimental P(6) = ${sixes} / ${total} = ${rel}</div>
      <div class="text-[11px] text-amber-200">Historical Spotlight: Ancient Indian Jñān-Chaupad ("Board of Knowledge") inspired modern Snakes and Ladders!</div>
    `;
  };
  window.c9c7s5Reset = function(){ total = 0; sixes = 0; c9c7s5Roll(10); };
  c9c7s5Roll(10);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔤</span> Theoretical Ratio Explorer: Picking Letters from "PROBABILITY"
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Target Letter Event:</span>
    <select id="c9c7s6Sel" onchange="c9c7s6Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
      <option value="B">Letter 'B' (2 slips)</option>
      <option value="I">Letter 'I' (2 slips)</option>
      <option value="V">Any Vowel: O, A, I, I (4 slips)</option>
      <option value="C">Any Consonant (7 slips)</option>
      <option value="P">Letter 'P' (1 slip)</option>
    </select>
  </label>
  <div id="c9c7s6Tiles" class="flex flex-wrap gap-1.5 justify-center p-2.5 bg-slate-950 rounded-xl border border-slate-800"></div>
  <div id="c9c7s6Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const word = 'PROBABILITY'.split('');
  const vowels = new Set(['A','E','I','O','U']);
  window.c9c7s6Draw = function(){
    const sel = document.getElementById('c9c7s6Sel').value;
    let count = 0, html = '';
    word.forEach(ch => {
      const hit = (sel === 'V' && vowels.has(ch)) || (sel === 'C' && !vowels.has(ch)) || (ch === sel);
      if(hit) count++;
      html += `<span class="w-7 h-8 rounded-lg flex items-center justify-center font-bold text-xs border ${hit ? 'bg-emerald-500/30 border-emerald-400 text-emerald-200' : 'bg-slate-900 border-slate-700 text-slate-400'}">${ch}</span>`;
    });
    document.getElementById('c9c7s6Tiles').innerHTML = html;
    document.getElementById('c9c7s6Out').innerHTML = `
      <span class="font-bold text-cyan-300">Theoretical P = Favourable / Total = ${count} / 11 ≈ ${(count/11).toFixed(3)}</span>
    `;
  };
  c9c7s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-pink-300 flex items-center gap-2">
    <span>🎡</span> Fair vs Unequal Spinner: Testing the Equally Likely Condition
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c7s7Mode('fair')" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold">Fair Spinner (90° each)</button>
    <button onclick="c9c7s7Mode('unfair')" class="px-3 py-1.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold">Unequal Spinner (180° Red!)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c7s7Svg" viewBox="0 0 120 120" class="w-28 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c7s7Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c7s7Mode = function(m){
    const svg = document.getElementById('c9c7s7Svg');
    const out = document.getElementById('c9c7s7Out');
    if(m === 'fair'){
      svg.innerHTML = `
        <path d="M60,60 L60,12 A48,48 0 0,1 108,60 Z" fill="#ef4444" fill-opacity="0.75"/>
        <path d="M60,60 L108,60 A48,48 0 0,1 60,108 Z" fill="#3b82f6" fill-opacity="0.75"/>
        <path d="M60,60 L60,108 A48,48 0 0,1 12,60 Z" fill="#10b981" fill-opacity="0.75"/>
        <path d="M60,60 L12,60 A48,48 0 0,1 60,12 Z" fill="#fbbf24" fill-opacity="0.75"/>
        <circle cx="60" cy="60" r="4" fill="#fff"/>
      `;
      out.innerHTML = `
        <div class="font-bold text-emerald-300">EQUALLY LIKELY: All 4 sectors span 90° each!</div>
        <div class="font-mono text-cyan-300">P(Red) = 90°/360° = 1/4 = 0.25</div>
        <div class="text-[11px] text-slate-400">Simple counting 1/4 works ONLY because all 4 sectors have equal area!</div>
      `;
    } else {
      svg.innerHTML = `
        <path d="M60,60 L60,12 A48,48 0 1,1 60,108 Z" fill="#ef4444" fill-opacity="0.8"/>
        <path d="M60,60 L60,108 A48,48 0 0,1 12,60 Z" fill="#3b82f6" fill-opacity="0.75"/>
        <path d="M60,60 L12,60 A48,48 0 0,1 26,26 Z" fill="#10b981" fill-opacity="0.75"/>
        <path d="M60,60 L26,26 A48,48 0 0,1 60,12 Z" fill="#fbbf24" fill-opacity="0.75"/>
        <circle cx="60" cy="60" r="4" fill="#fff"/>
      `;
      out.innerHTML = `
        <div class="font-bold text-pink-300">TRAP ALERT: 4 colors, yet NOT equally likely!</div>
        <div class="font-mono text-amber-300">Red = 180°/360° = 1/2 (NOT 1/4!) | Green = 45°/360° = 1/8</div>
        <div class="text-[11px] text-slate-400">Always check central angles/areas before dividing by outcome count!</div>
      `;
    }
  };
  c9c7s7Mode('unfair');
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🍌</span> Campus Sampling &amp; Population Forecasting Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Students Preferring Bananas (out of 50 surveyed): <strong id="c9c7s8BVal" class="text-amber-300">20 / 50</strong></span>
      <input type="range" id="c9c7s8B" min="5" max="40" value="20" oninput="c9c7s8Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Total School Population: <strong id="c9c7s8PopVal" class="text-cyan-300">1,500</strong></span>
      <input type="range" id="c9c7s8Pop" min="500" max="2500" step="100" value="1500" oninput="c9c7s8Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
  </div>
  <div id="c9c7s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c7s8Draw = function(){
    const b = parseInt(document.getElementById('c9c7s8B').value);
    const pop = parseInt(document.getElementById('c9c7s8Pop').value);
    document.getElementById('c9c7s8BVal').textContent = `${b} / 50`;
    document.getElementById('c9c7s8PopVal').textContent = pop.toLocaleString();
    const p = b / 50;
    const est = Math.round(p * pop);
    document.getElementById('c9c7s8Out').innerHTML = `
      <div class="font-bold text-amber-300">Sample Empirical Probability = ${b} / 50 = ${(p*100).toFixed(0)}% (${p.toFixed(2)})</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">Projected Canteen Order = ${p.toFixed(2)} × ${pop.toLocaleString()} = ${est.toLocaleString()} bananas</div>
      <div class="text-[11px] text-slate-400">Random representative sampling prevents bias and forecasts full-population demand accurately!</div>
    `;
  };
  c9c7s8Draw();
})();
</script>
"""
}

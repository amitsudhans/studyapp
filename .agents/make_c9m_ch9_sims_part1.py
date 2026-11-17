#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 9: Propositions and their Converses
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Statement vs Non-Proposition Classifier
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Sentence to Evaluate:</span>
    <select id="c9c9s1Sel" onchange="c9c9s1Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="p_true">"Every prime number greater than 2 is odd."</option>
      <option value="p_false">"Every rectangle has five sides."</option>
      <option value="np_q">"Is 91 a prime number?"</option>
      <option value="np_cmd">"Close the classroom door immediately!"</option>
      <option value="np_op">"Vanilla ice cream tastes better than chocolate."</option>
      <option value="np_open">"x + 3 = 7" (with x unspecified)</option>
    </select>
  </label>
  <div id="c9c9s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const info = {
    p_true: ['VALID PROPOSITION (TRUE)', 'text-emerald-300', 'Unambiguously True in all cases — declarative and objectively verifiable.'],
    p_false: ['VALID PROPOSITION (FALSE)', 'text-amber-300', 'Unambiguously False — still a valid proposition because its truth value is strictly definite!'],
    np_q: ['NOT A PROPOSITION (Question)', 'text-rose-400', 'Questions ask for information and cannot be judged True or False.'],
    np_cmd: ['NOT A PROPOSITION (Command)', 'text-rose-400', 'Imperative instructions carry no True/False truth value.'],
    np_op: ['NOT A PROPOSITION (Opinion)', 'text-rose-400', 'Personal taste varies by observer and is not objectively True or False.'],
    np_open: ['NOT A PROPOSITION (Open Sentence)', 'text-rose-400', 'Truth depends on free variable x (True if x = 4; False if x = 5).']
  };
  window.c9c9s1Draw = function(){
    const k = document.getElementById('c9c9s1Sel').value;
    const [badge, cls, desc] = info[k];
    document.getElementById('c9c9s1Out').innerHTML = `
      <div class="font-bold text-sm ${cls}">${badge}</div>
      <div>${desc}</div>
    `;
  };
  setTimeout(window.c9c9s1Draw, 40);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>➡️</span> If-Then Premise &amp; Conclusion Deconstructor
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Conditional Proposition (X ⇒ Y):</span>
    <select id="c9c9s2Sel" onchange="c9c9s2Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="sq">If a polygon is a square, then it has four equal sides.</option>
      <option value="div5">If a whole number ends in 0, then it is divisible by 5.</option>
      <option value="tri">If a triangle is equilateral, then all three angles equal 60°.</option>
    </select>
  </label>
  <div id="c9c9s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const map = {
    sq: ['A polygon is a square', 'It has four equal sides', 'A rhombus has 4 equal sides (X false, Y true) without making X ⇒ Y false!'],
    div5: ['A whole number ends in 0', 'It is divisible by 5', 'Numbers ending in 5 are also divisible by 5 (X false, Y true), yet X ⇒ Y holds!'],
    tri: ['A triangle is equilateral', 'All three angles equal 60°', 'Here both X ⇒ Y and Y ⇒ X happen to be true!']
  };
  window.c9c9s2Draw = function(){
    const [x, y, note] = map[document.getElementById('c9c9s2Sel').value];
    document.getElementById('c9c9s2Out').innerHTML = `
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div class="p-2.5 rounded-lg bg-cyan-500/10 border border-cyan-500/30"><span class="text-[10px] uppercase text-cyan-300 font-bold block">Premise (X)</span><strong class="text-white">${x}</strong></div>
        <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30"><span class="text-[10px] uppercase text-emerald-300 font-bold block">Conclusion (Y)</span><strong class="text-white">${y}</strong></div>
      </div>
      <div class="text-amber-300 pt-1">Key Insight: ${note}</div>
    `;
  };
  setTimeout(window.c9c9s2Draw, 40);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔄</span> Interactive Statement-to-Converse Flipper
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Statement Pair:</span>
    <select id="c9c9s3Sel" onchange="c9c9s3Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="mul10">If a whole number is a multiple of 10, then its units digit is 0.</option>
      <option value="tiger">If an animal is a Bengal tiger, then it is a mammal.</option>
      <option value="even">If an integer is odd, then it is prime.</option>
    </select>
  </label>
  <div id="c9c9s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const pairs = {
    mul10: ["If a whole number's units digit is 0, then it is a multiple of 10.", 'TRUE', 'TRUE', 'Both directions hold!'],
    tiger: ['If an animal is a mammal, then it is a Bengal tiger.', 'TRUE', 'FALSE (Counterexample: elephant, whale)', 'Truth of X ⇒ Y does NOT guarantee Y ⇒ X.'],
    even: ['If an integer is prime, then it is odd.', 'FALSE (Counterexample: 9)', 'FALSE (Counterexample: 2)', 'Both proposition and converse can be False!']
  };
  window.c9c9s3Draw = function(){
    const [conv, t1, t2, msg] = pairs[document.getElementById('c9c9s3Sel').value];
    document.getElementById('c9c9s3Out').innerHTML = `
      <div><strong class="text-amber-300">Converse (Y ⇒ X):</strong> <span class="text-white">${conv}</span></div>
      <div class="flex flex-wrap gap-3 pt-1">
        <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700">Original: <strong>${t1}</strong></span>
        <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700">Converse: <strong>${t2}</strong></span>
      </div>
      <div class="text-cyan-300">${msg}</div>
    `;
  };
  setTimeout(window.c9c9s3Draw, 40);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>💥</span> Euler's Counterexample Tester: Fermat Numbers F<sub>n</sub> = 2<sup>2<sup>n</sup></sup> + 1
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Select Index (n = 0 to 5):</span>
      <span id="c9c9s4NLbl" class="text-amber-300 font-bold">n = 5</span>
    </div>
    <input id="c9c9s4N" type="range" min="0" max="5" value="5" oninput="c9c9s4Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c9s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const fermat = [
    ['3', true, 'Prime (2¹ + 1 = 3)'],
    ['5', true, 'Prime (2² + 1 = 5)'],
    ['17', true, 'Prime (2⁴ + 1 = 17)'],
    ['257', true, 'Prime (2⁸ + 1 = 257)'],
    ['65,537', true, 'Prime (2¹⁶ + 1 = 65,537)'],
    ['4,294,967,297', false, 'COMPOSITE! Euler (1732) factored F₅ = 641 × 6,700,417 — one counterexample disproved Fermat!']
  ];
  window.c9c9s4Draw = function(){
    const n = parseInt(document.getElementById('c9c9s4N').value, 10);
    document.getElementById('c9c9s4NLbl').textContent = 'n = ' + n;
    const [val, isPrime, note] = fermat[n];
    document.getElementById('c9c9s4Out').innerHTML = `
      <div class="text-sm font-bold text-cyan-300">F<sub>${n}</sub> = 2<sup>${Math.pow(2,n)}</sup> + 1 = ${val}</div>
      <div class="font-bold ${isPrime ? 'text-emerald-300' : 'text-rose-400'}">${note}</div>
    `;
  };
  setTimeout(window.c9c9s4Draw, 40);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌧️</span> Causal Logic Explorer: Rain vs Wet Road
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c9s5Set('rain')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">Case 1: Heavy Rain</button>
    <button onclick="c9c9s5Set('tanker')" class="px-3 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-200 font-bold">Case 2: Water Tanker Spill</button>
    <button onclick="c9c9s5Set('dry')" class="px-3 py-1.5 rounded-lg bg-slate-700/60 hover:bg-slate-700 border border-slate-600 text-slate-200 font-bold">Case 3: Sunny Dry Day</button>
  </div>
  <div id="c9c9s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cases = {
    rain: ['Rain = TRUE, Road Wet = TRUE', 'Supports both "Rain ⇒ Wet" and "Wet ⇒ Rain" (no counterexample here).'],
    tanker: ['Rain = FALSE, Road Wet = TRUE', '<strong class="text-rose-400">COUNTEREXAMPLE TO CONVERSE!</strong> Road is wet, yet it did NOT rain! Proves "Wet ⇒ Rain" is FALSE.'],
    dry: ['Rain = FALSE, Road Wet = FALSE', 'Premises are False; does not falsify either direction.']
  };
  window.c9c9s5Set = function(k){
    const [st, msg] = cases[k];
    document.getElementById('c9c9s5Out').innerHTML = `
      <div class="font-bold text-amber-300">${st}</div>
      <div>${msg}</div>
    `;
  };
  setTimeout(function(){ window.c9c9s5Set('tanker'); }, 40);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔢</span> Multiples of 6 vs Multiples of 3 Counterexample Finder
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Test Any Positive Integer (1 to 36):</span>
    <input id="c9c9s6N" type="number" min="1" max="36" value="9" oninput="c9c9s6Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
  </label>
  <div id="c9c9s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c9s6Draw = function(){
    const n = Math.max(1, parseInt(document.getElementById('c9c9s6N').value || '1', 10));
    const m3 = n % 3 === 0;
    const m6 = n % 6 === 0;
    let verdict = '';
    if(m6) verdict = `<span class="text-emerald-300 font-bold">${n} is a multiple of BOTH 6 and 3</span> (6k = 3·2k).`;
    else if(m3) verdict = `<span class="text-rose-400 font-bold">COUNTEREXAMPLE FOUND!</span> ${n} is a multiple of 3, yet NOT a multiple of 6 — disproving the converse!`;
    else verdict = `<span class="text-slate-400">${n} is neither a multiple of 3 nor a multiple of 6.</span>`;
    document.getElementById('c9c9s6Out').innerHTML = `
      <div>Divisible by 3? <strong>${m3 ? 'YES' : 'NO'}</strong> &nbsp;|&nbsp; Divisible by 6? <strong>${m6 ? 'YES' : 'NO'}</strong></div>
      <div>${verdict}</div>
    `;
  };
  setTimeout(window.c9c9s6Draw, 40);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧩</span> Factor-Partner Pairing Grid: Perfect Squares vs Odd Factor Counts
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Enter Positive Integer N (1 to 100):</span>
    <input id="c9c9s7N" type="number" min="1" max="100" value="36" oninput="c9c9s7Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
  </label>
  <div id="c9c9s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c9s7Draw = function(){
    const N = Math.max(1, Math.min(100, parseInt(document.getElementById('c9c9s7N').value || '1', 10)));
    const pairs = [];
    let count = 0;
    for(let d = 1; d * d <= N; d++){
      if(N % d === 0){
        const partner = N / d;
        if(d === partner){
          pairs.push(`<span class="px-2 py-1 rounded bg-amber-500/20 border border-amber-400 text-amber-200 font-bold">{${d} ↔ self}</span>`);
          count += 1;
        } else {
          pairs.push(`<span class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-cyan-200">{${d}, ${partner}}</span>`);
          count += 2;
        }
      }
    }
    const isSq = Number.isInteger(Math.sqrt(N));
    document.getElementById('c9c9s7Out').innerHTML = `
      <div class="flex flex-wrap gap-2">${pairs.join('')}</div>
      <div class="pt-1 border-t border-slate-800 font-bold ${isSq ? 'text-emerald-300' : 'text-cyan-300'}">
        Total Factors of ${N}: ${count} (${count % 2 === 1 ? 'ODD' : 'EVEN'}) &nbsp;•&nbsp; ${isSq ? `${N} = ${Math.sqrt(N)}² IS a Perfect Square!` : `${N} is NOT a Perfect Square.`}
      </div>
    `;
  };
  setTimeout(window.c9c9s7Draw, 40);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Equal-Area Non-Congruent Triangle SVG Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Slide Top Vertex Horizontally (Fixed Base = 10, Fixed Height = 6):</span>
      <span id="c9c9s8XLbl" class="text-amber-300 font-bold">Shear x = 6</span>
    </div>
    <input id="c9c9s8X" type="range" min="0" max="14" value="6" oninput="c9c9s8Draw()" class="w-full accent-amber-400">
  </label>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c9s8Svg" viewBox="0 0 260 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c9s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  window.c9c9s8Draw = function(){
    const sh = parseInt(document.getElementById('c9c9s8X').value, 10);
    document.getElementById('c9c9s8XLbl').textContent = 'Shear x = ' + sh;
    const ax = 40, ay = 125, bx = 180, by = 125;
    const cx = 40 + sh * 14, cy = 35;
    const s1 = +(Math.hypot(cx - ax, ay - cy) / 14).toFixed(2);
    const s2 = +(Math.hypot(bx - cx, by - cy) / 14).toFixed(2);
    document.getElementById('c9c9s8Svg').innerHTML = `
      <line x1="15" y1="${cy}" x2="245" y2="${cy}" stroke="#334155" stroke-dasharray="4 3"/>
      <polygon points="${ax},${ay} ${bx},${by} ${cx},${cy}" fill="rgba(34,211,238,0.18)" stroke="#22d3ee" stroke-width="2"/>
      <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${ay}" stroke="#fbbf24" stroke-dasharray="3 3" stroke-width="1.5"/>
      <circle cx="${cx}" cy="${cy}" r="4.5" fill="#fbbf24"/>
    `;
    document.getElementById('c9c9s8Out').innerHTML = `
      <div class="font-bold text-emerald-300">Area = ½ × 10 × 6 = 30 units² (ALWAYS Constant!)</div>
      <div>Side lengths: base = 10, left = ${s1}, right = ${s2}</div>
      <div class="text-rose-400 font-semibold">Different side lengths prove equal-area triangles need NOT be congruent!</div>
    `;
  };
  setTimeout(window.c9c9s8Draw, 40);
})();
</script>
"""
}

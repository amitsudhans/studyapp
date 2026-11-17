#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 13: Two Variables, One Line
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🍎</span> Budget Line Explorer: 60x + 50y = 280
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Apples x (kg at ₹60/kg):</span>
      <span id="c9c13s1Lbl" class="text-amber-300 font-bold">x = 3.0 kg, y = 2.0 kg</span>
    </div>
    <input id="c9c13s1X" type="range" min="0" max="4.5" step="0.5" value="3" oninput="c9c13s1Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c13s1Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c13s1Draw = function(){
    const x = parseFloat(document.getElementById('c9c13s1X').value);
    const y = (280 - 60*x) / 50;
    document.getElementById('c9c13s1Lbl').textContent = 'x = ' + x.toFixed(1) + ' kg, y = ' + y.toFixed(2) + ' kg';
    const px = v => 50 + v * 52;
    const py = v => 155 - v * 22;
    document.getElementById('c9c13s1Svg').innerHTML = `
      <line x1="50" y1="20" x2="50" y2="155" stroke="#475569" stroke-width="1.5"/>
      <line x1="50" y1="155" x2="330" y2="155" stroke="#475569" stroke-width="1.5"/>
      <line x1="${px(0)}" y1="${py(5.6)}" x2="${px(4.67)}" y2="${py(0)}" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="${px(x)}" cy="${py(y)}" r="6" fill="#fbbf24"/>
      <text x="${px(x)+10}" y="${py(y)-6}" fill="#fbbf24" font-size="11" font-weight="bold">(${x.toFixed(1)}, ${y.toFixed(2)})</text>
      <text x="190" y="175" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">60(${x.toFixed(1)}) + 50(${y.toFixed(2)}) = ₹280</text>`;
  };
  c9c13s1Draw();
})();
</script>""",

    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📝</span> Standard Form Converter: ax + by + c = 0
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c13s2Set(0)" class="px-2.5 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">60x + 50y = 280</button>
    <button onclick="c9c13s2Set(1)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">x/2 − y/3 = 5</button>
    <button onclick="c9c13s2Set(2)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">x = 4</button>
    <button onclick="c9c13s2Set(3)" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">y = −7</button>
  </div>
  <div id="c9c13s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cases = [
    { eq: '60x + 50y = 280', step: 'Subtract 280 from both sides', std: '60x + 50y − 280 = 0', a: 60, b: 50, c: -280 },
    { eq: 'x/2 − y/3 = 5', step: 'Multiply by LCM(2, 3) = 6 to clear fractions: 3x − 2y = 30', std: '3x − 2y − 30 = 0', a: 3, b: -2, c: -30 },
    { eq: 'x = 4', step: 'Insert 0·y for the missing variable and subtract 4', std: '1x + 0y − 4 = 0', a: 1, b: 0, c: -4 },
    { eq: 'y = −7', step: 'Insert 0·x for the missing variable and add 7', std: '0x + 1y + 7 = 0', a: 0, b: 1, c: 7 }
  ];
  window.c9c13s2Set = function(i){
    const d = cases[i];
    document.getElementById('c9c13s2Out').innerHTML = `
      <div><span class="text-slate-400">Original:</span> <span class="text-amber-300 font-bold">${d.eq}</span></div>
      <div><span class="text-slate-400">Rule:</span> ${d.step}</div>
      <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-sm font-bold text-emerald-300">${d.std}</div>
      <div class="flex gap-3 font-semibold text-cyan-300"><span>a = ${d.a}</span><span>b = ${d.b}</span><span>c = ${d.c}</span></div>`;
  };
  c9c13s2Set(0);
})();
</script>""",

    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📍</span> Ordered Pair Solution Generator: 2x + y = 8
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Pick Any Real x:</span>
      <span id="c9c13s3Lbl" class="text-amber-300 font-bold">x = 2 ⇒ y = 4</span>
    </div>
    <input id="c9c13s3X" type="range" min="-1" max="5" step="0.5" value="2" oninput="c9c13s3Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c13s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c13s3Draw = function(){
    const x = parseFloat(document.getElementById('c9c13s3X').value);
    const y = 8 - 2*x;
    const swapVal = 2*y + x;
    document.getElementById('c9c13s3Lbl').textContent = 'x = ' + x + ' ⇒ y = ' + y;
    document.getElementById('c9c13s3Out').innerHTML = `
      <div><span class="text-emerald-400 font-bold">Ordered Pair (${x}, ${y}):</span> 2(${x}) + (${y}) = <span class="text-emerald-300 font-bold">8 (TRUE!)</span></div>
      <div><span class="text-rose-400 font-bold">Swapped Pair (${y}, ${x}):</span> 2(${y}) + (${x}) = <span class="text-amber-300 font-bold">${swapVal} (${swapVal===8?'Equal only when x=y':'≠ 8, FALSE!'})</span></div>
      <div class="text-cyan-300">Every choice of x yields a unique y ⇒ Infinitely many solutions!</div>`;
  };
  c9c13s3Draw();
})();
</script>""",

    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Two-Intercept Line Grapher: ax + by = 12
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Coeff a:</span><span id="c9c13s4AL" class="text-cyan-300 font-bold">2</span></div>
      <input id="c9c13s4A" type="range" min="1" max="6" value="2" oninput="c9c13s4Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Coeff b:</span><span id="c9c13s4BL" class="text-emerald-300 font-bold">3</span></div>
      <input id="c9c13s4B" type="range" min="1" max="6" value="3" oninput="c9c13s4Draw()" class="w-full accent-emerald-400">
    </label>
  </div>
  <svg id="c9c13s4Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c13s4Draw = function(){
    const a = parseInt(document.getElementById('c9c13s4A').value, 10);
    const b = parseInt(document.getElementById('c9c13s4B').value, 10);
    document.getElementById('c9c13s4AL').textContent = a;
    document.getElementById('c9c13s4BL').textContent = b;
    const xi = 12/a, yi = 12/b;
    const px = v => 55 + v * 20;
    const py = v => 150 - v * 10;
    document.getElementById('c9c13s4Svg').innerHTML = `
      <line x1="55" y1="15" x2="55" y2="155" stroke="#475569" stroke-width="1.5"/>
      <line x1="45" y1="150" x2="325" y2="150" stroke="#475569" stroke-width="1.5"/>
      <line x1="${px(0)}" y1="${py(yi)}" x2="${px(xi)}" y2="${py(0)}" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="${px(xi)}" cy="${py(0)}" r="5.5" fill="#fbbf24"/>
      <circle cx="${px(0)}" cy="${py(yi)}" r="5.5" fill="#34d399"/>
      <text x="${px(xi)}" y="168" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">(${xi.toFixed(1)}, 0)</text>
      <text x="64" y="${py(yi)+4}" fill="#34d399" font-size="11" font-weight="bold">(0, ${yi.toFixed(1)})</text>
      <text x="220" y="26" fill="#cbd5e1" font-size="11" font-weight="bold">${a}x + ${b}y = 12</text>`;
  };
  c9c13s4Draw();
})();
</script>""",

    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Rise Over Run &amp; 4 Slope Types
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c13s5Set('pos')" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-white font-semibold">Positive (m &gt; 0)</button>
    <button onclick="c9c13s5Set('neg')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Negative (m &lt; 0)</button>
    <button onclick="c9c13s5Set('zero')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Zero (Horizontal)</button>
    <button onclick="c9c13s5Set('undef')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Undefined (Vertical)</button>
  </div>
  <svg id="c9c13s5Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  const cfg = {
    pos:   { p1:[80,140], p2:[270,45], col:'#34d399', txt:'Rise = +95, Run = +190 ⇒ m = +0.5 (Rises left→right)' },
    neg:   { p1:[80,45],  p2:[270,140], col:'#fb7185', txt:'Rise = −95, Run = +190 ⇒ m = −0.5 (Falls left→right)' },
    zero:  { p1:[70,95],  p2:[290,95], col:'#fbbf24', txt:'Rise = 0, Run = 220 ⇒ m = 0 (Horizontal Line)' },
    undef: { p1:[180,35], p2:[180,150], col:'#c084fc', txt:'Run = 0 ⇒ Division by zero ⇒ Undefined Slope (Vertical)' }
  };
  window.c9c13s5Set = function(k){
    const c = cfg[k];
    document.getElementById('c9c13s5Svg').innerHTML = `
      <line x1="30" y1="95" x2="330" y2="95" stroke="#334155" stroke-width="1"/>
      <line x1="180" y1="15" x2="180" y2="160" stroke="#334155" stroke-width="1"/>
      <line x1="${c.p1[0]}" y1="${c.p1[1]}" x2="${c.p2[0]}" y2="${c.p2[1]}" stroke="${c.col}" stroke-width="3.5"/>
      <circle cx="${c.p1[0]}" cy="${c.p1[1]}" r="5" fill="#f8fafc"/><circle cx="${c.p2[0]}" cy="${c.p2[1]}" r="5" fill="#f8fafc"/>
      <text x="180" y="174" text-anchor="middle" fill="${c.col}" font-size="11" font-weight="bold">${c.txt}</text>`;
  };
  c9c13s5Set('pos');
})();
</script>""",

    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔄</span> Slope-Intercept Transformer: ax + by + c = 0 → y = mx + d
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Slope m:</span><span id="c9c13s6ML" class="text-cyan-300 font-bold">1.0</span></div>
      <input id="c9c13s6M" type="range" min="-2.5" max="2.5" step="0.5" value="1" oninput="c9c13s6Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>y-intercept d:</span><span id="c9c13s6DL" class="text-amber-300 font-bold">1</span></div>
      <input id="c9c13s6D" type="range" min="-3" max="3" step="1" value="1" oninput="c9c13s6Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <svg id="c9c13s6Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c13s6Draw = function(){
    const m = parseFloat(document.getElementById('c9c13s6M').value);
    const d = parseFloat(document.getElementById('c9c13s6D').value);
    document.getElementById('c9c13s6ML').textContent = m.toFixed(1);
    document.getElementById('c9c13s6DL').textContent = d;
    const px = x => 180 + x * 25;
    const py = y => 95 - y * 15;
    const x1 = -5, y1 = m*x1 + d, x2 = 5, y2 = m*x2 + d;
    document.getElementById('c9c13s6Svg').innerHTML = `
      <line x1="30" y1="95" x2="330" y2="95" stroke="#475569" stroke-width="1.2"/>
      <line x1="180" y1="15" x2="180" y2="165" stroke="#475569" stroke-width="1.2"/>
      <line x1="${px(x1)}" y1="${py(y1)}" x2="${px(x2)}" y2="${py(y2)}" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="${px(0)}" cy="${py(d)}" r="5.5" fill="#fbbf24"/>
      <text x="180" y="176" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">y = ${m}x ${d>=0?'+ '+d:'− '+Math.abs(d)}   (m = −a/b, d = −c/b)</text>`;
  };
  c9c13s6Draw();
})();
</script>""",

    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏛️</span> Real-World System Formulator
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c13s7Set(0)" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Ticket Sales</button>
    <button onclick="c9c13s7Set(1)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Taxi Fares</button>
    <button onclick="c9c13s7Set(2)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Number Puzzle</button>
  </div>
  <div id="c9c13s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const items = [
    { title:'Ticket Sales', e1:'3x + 2y = 500 (3 adult + 2 child tickets)', e2:'2x + 5y = 480 (2 adult + 5 child tickets)', sol:'Adult x = ₹140, Child y = ₹40' },
    { title:'Taxi Fare Structure', e1:'F + 10r = 105 (Fixed fee + 10 km)', e2:'F + 15r = 155 (Fixed fee + 15 km)', sol:'Fixed fee F = ₹5, Rate r = ₹10/km' },
    { title:'Two-Number Puzzle', e1:'x + y = 36 (Sum is 36)', e2:'x − y = 12 (Difference is 12)', sol:'Larger x = 24, Smaller y = 12' }
  ];
  window.c9c13s7Set = function(i){
    const d = items[i];
    document.getElementById('c9c13s7Out').innerHTML = `
      <div class="text-amber-300 font-bold">${d.title}</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800">Eq 1: <span class="text-cyan-300 font-semibold">${d.e1}</span></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800">Eq 2: <span class="text-cyan-300 font-semibold">${d.e2}</span></div>
      <div class="text-emerald-400 font-bold">Shared Solution: ${d.sol}</div>`;
  };
  c9c13s7Set(0);
})();
</script>""",

    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪜</span> Substitution Method Step-by-Step Walkthrough
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>System: x + y = 14 &amp; 3x − 2y = 12</span>
      <span id="c9c13s8Lbl" class="text-amber-300 font-bold">Step 1 / 4</span>
    </div>
    <input id="c9c13s8Step" type="range" min="1" max="4" value="1" oninput="c9c13s8Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c13s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const steps = [
    '<span class="text-cyan-300 font-bold">Step 1 (Isolate):</span> From x + y = 14, isolate x = 14 − y.',
    '<span class="text-amber-300 font-bold">Step 2 (Substitute):</span> Plug x = 14 − y into Eq 2: 3(14 − y) − 2y = 12.',
    '<span class="text-emerald-300 font-bold">Step 3 (Solve y):</span> 42 − 3y − 2y = 12 ⇒ 42 − 5y = 12 ⇒ 5y = 30 ⇒ y = 6.',
    '<span class="text-emerald-400 font-bold">Step 4 (Back-Substitute &amp; Check):</span> x = 14 − 6 = 8. Check: 8+6=14 and 3(8)−2(6)=12. Solution: (8, 6)!'
  ];
  window.c9c13s8Draw = function(){
    const s = parseInt(document.getElementById('c9c13s8Step').value, 10);
    document.getElementById('c9c13s8Lbl').textContent = 'Step ' + s + ' / 4';
    document.getElementById('c9c13s8Out').innerHTML = steps.slice(0, s).map(x => `<div class="p-2 rounded bg-slate-900 border border-slate-800">${x}</div>`).join('');
  };
  c9c13s8Draw();
})();
</script>""",
}

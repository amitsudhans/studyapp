#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 5: I'm Up and Down, and Round and Round
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🌈</span> Minor Arc, Semicircle &amp; Major Reflex Central Angle Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Minor Arc Central Angle θ: <strong id="c9c5s9AngVal" class="text-cyan-300">70°</strong></span>
    <input type="range" id="c9c5s9Ang" min="20" max="180" value="70" oninput="c9c5s9Draw()" class="w-full accent-amber-400 mt-1.5">
  </label>
  <div id="c9c5s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s9Draw = function(){
    const th = parseInt(document.getElementById('c9c5s9Ang').value);
    const maj = 360 - th;
    document.getElementById('c9c5s9AngVal').textContent = `${th}°${th===180?' (Semicircle!)':''}`;
    document.getElementById('c9c5s9Out').innerHTML = `
      <div class="text-cyan-300">Arc Type 1: ${th===180?'Exact Semicircle':'Minor Arc'} → Central Angle = <strong>${th}°</strong></div>
      <div class="text-amber-300">Arc Type 2: ${maj===180?'Exact Semicircle':'Major Arc'} → Reflex Central Angle = 360° − ${th}° = <strong>${maj}°</strong></div>
      <div class="text-emerald-300 font-sans">Full revolution check: ${th}° + ${maj}° = 360°. Congruent arcs always subtend identical central angles!</div>
    `;
  };
  c9c5s9Draw();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Theorem 9 Live Protractor: Central Angle ∠AOB = 2 × Inscribed Angle ∠APB
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Central Angle ∠AOB: <strong id="c9c5s10AngVal" class="text-cyan-300">136°</strong></span>
    <input type="range" id="c9c5s10Ang" min="40" max="240" value="136" oninput="c9c5s10Draw()" class="w-full accent-cyan-400 mt-1.5">
  </label>
  <div id="c9c5s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s10Draw = function(){
    const c = parseInt(document.getElementById('c9c5s10Ang').value);
    const ins = c / 2;
    document.getElementById('c9c5s10AngVal').textContent = `${c}°`;
    document.getElementById('c9c5s10Out').innerHTML = `
      <div class="text-cyan-300 font-bold text-sm">Central ∠AOB = ${c}°  ⇒  Inscribed ∠APB = ${c}° / 2 = ${ins}°</div>
      <div class="text-amber-300">Exterior Angle Decomposition: 2α + 2β = 2(α + β) = 2 ∠APB = ∠AOB!</div>
      <div class="text-emerald-300 font-sans">${c===180 ? 'SEMICIRCLE CASE: 180° / 2 = 90°!' : (c > 180 ? 'REFLEX MAJOR ARC CASE: obtuse inscribed angle > 90°!' : 'MINOR ARC CASE: acute inscribed angle < 90°!')}</div>
    `;
  };
  c9c5s10Draw();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🔺</span> Theorem 9 Corollaries: Semicircle 90° &amp; Same-Segment Equal Angles
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c5s11Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Semicircle Diameter (180° → 90°)</button>
    <button type="button" onclick="c9c5s11Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Same Segment (∠APB = ∠AQB = 42°)</button>
    <button type="button" onclick="c9c5s11Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Right Triangle Converse</button>
  </div>
  <div id="c9c5s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t:'Corollary 1: Angle in a Semicircle = 90°', e:'Diameter AB forms a 180° straight angle at Centre O. Every inscribed angle ∠APB = ½(180°) = 90° — guaranteed right corner anywhere on the semicircle!' },
    { t:'Corollary 2: Angles in the Same Segment Are Equal', e:'Points P, Q, R on the same arc segment all see central angle ∠AOB = 84°, so ∠APB = ∠AQB = ∠ARB = ½(84°) = 42° identically!' },
    { t:'Right-Triangle Converse Property', e:'Whenever ∠ACB = 90° on circle vertices A, B, C, chord AB MUST subtend 180° at O — making hypotenuse AB an exact diameter!' }
  ];
  window.c9c5s11Pick = function(i){
    const d = items[i];
    document.getElementById('c9c5s11Out').innerHTML = `<div class="text-emerald-300 font-bold text-sm">${d.t}</div><p class="mt-1">${d.e}</p>`;
  };
  c9c5s11Pick(0);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>🔍</span> Theorem 10: Concyclic Points Tester (∠ACB = ∠ADB on Same Side of AB)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Compare Vertex Angle ∠ADB (against fixed ∠ACB = 50°): <strong id="c9c5s12Val" class="text-cyan-300">50°</strong></span>
    <input type="range" id="c9c5s12Ang" min="35" max="65" value="50" oninput="c9c5s12Draw()" class="w-full accent-purple-400 mt-1.5">
  </label>
  <div id="c9c5s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c5s12Draw = function(){
    const adb = parseInt(document.getElementById('c9c5s12Ang').value);
    document.getElementById('c9c5s12Val').textContent = `${adb}°`;
    const conc = adb === 50;
    document.getElementById('c9c5s12Out').innerHTML = `
      <div class="font-mono">Fixed ∠ACB = <strong class="text-cyan-300">50°</strong> | Tested ∠ADB = <strong class="text-amber-300">${adb}°</strong> (both same side of AB)</div>
      <div class="px-2.5 py-1 rounded font-bold inline-block mt-1 ${conc?'bg-emerald-500/20 text-emerald-300':'bg-rose-500/20 text-rose-300'}">${conc ? 'CONCYCLIC! All 4 points A, B, C, D lie on ONE circle (Theorem 10)!' : (adb > 50 ? 'NOT CONCYCLIC: D sits STRICTLY INSIDE circle ABC!' : 'NOT CONCYCLIC: D sits STRICTLY OUTSIDE circle ABC!')}</div>
    `;
  };
  c9c5s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>💠</span> Theorems 11 &amp; 12: Cyclic Quadrilateral Opposite Angles Sum (∠A + ∠C = 180°)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Adjust Vertex Angle ∠A: <strong id="c9c5s13AVal" class="text-cyan-300">112°</strong></span>
    <input type="range" id="c9c5s13A" min="30" max="150" value="112" oninput="c9c5s13Draw()" class="w-full accent-cyan-400 mt-1.5">
  </label>
  <div id="c9c5s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s13Draw = function(){
    const a = parseInt(document.getElementById('c9c5s13A').value);
    const c = 180 - a;
    document.getElementById('c9c5s13AVal').textContent = `${a}°`;
    document.getElementById('c9c5s13Out').innerHTML = `
      <div class="text-cyan-300">Central Angle BOD = 2(${a}°) = ${2*a}° | Reflex BOD = 2(${c}°) = ${2*c}°</div>
      <div class="text-emerald-300 font-bold text-sm">Opposite Angle Sum: ∠A + ∠C = ${a}° + ${c}° = 180° (Theorem 11)!</div>
      <div class="text-amber-300">Exterior angle at C = 180° − ${c}° = ${a}° = ∠A (Converse Thm 12: sum 180° ⇒ concyclic!).</div>
    `;
  };
  c9c5s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🚧</span> Parallel Chords Gap Simulator: Same Side (|d₁−d₂|) vs Opposite Sides (d₁+d₂)
  </h3>
  <div class="flex gap-2 text-xs">
    <button type="button" onclick="c9c5s14Side('opp')" id="c9c5s14bO" class="px-3 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Opposite Sides of O</button>
    <button type="button" onclick="c9c5s14Side('same')" id="c9c5s14bS" class="px-3 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Same Side of O</button>
  </div>
  <div id="c9c5s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s14Side = function(mode){
    const bo = document.getElementById('c9c5s14bO'), bs = document.getElementById('c9c5s14bS');
    if(bo && bs){
      bo.className = mode==='opp' ? 'px-3 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-3 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
      bs.className = mode==='same' ? 'px-3 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-3 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    }
    const gap = mode==='opp' ? '6 + 8 = 14 cm' : '8 − 6 = 2 cm';
    document.getElementById('c9c5s14Out').innerHTML = `
      <div class="text-cyan-300">Circle r = 10 cm | Chord 1 = 16 cm (d₁ = √(10²−8²) = 6 cm) | Chord 2 = 12 cm (d₂ = √(10²−6²) = 8 cm)</div>
      <div class="text-emerald-300 font-bold text-sm">Separation Distance (${mode==='opp'?'Opposite Sides':'Same Side'}): ${gap}</div>
      <div class="text-slate-400 font-sans">Exam Alert: Always check whether the problem specifies opposite sides or same side of Centre O!</div>
    `;
  };
  c9c5s14Side('opp');
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🛡️</span> Classic Circle Exercise Proof Chain Inspector
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c5s15Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Cyclic Parallelogram = Rectangle</button>
    <button type="button" onclick="c9c5s15Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Cyclic Trapezium = Isosceles</button>
    <button type="button" onclick="c9c5s15Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Concentric Line AB = CD</button>
  </div>
  <div id="c9c5s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  const proofs = [
    { t:'Cyclic Parallelogram ABCD is ALWAYS a Rectangle', s1:'Parallelogram opposite angles equal: ∠A = ∠C.', s2:'Cyclic quad opposite angles supplementary (Thm 11): ∠A + ∠C = 180°.', s3:'2∠A = 180° ⇒ ∠A = ∠B = ∠C = ∠D = 90° ⇒ Rectangle!' },
    { t:'Isosceles Trapezium ABCD (AD = BC, AB ∥ DC) is Cyclic', s1:'Co-interior parallel sum: ∠A + ∠D = 180°.', s2:'Equal non-parallel legs AD = BC forces base angles ∠A = ∠B.', s3:'Substitute: ∠B + ∠D = 180° ⇒ Concyclic by Theorem 12!' },
    { t:'Line Crossing Concentric Circles at A, B, C, D has AB = CD', s1:'Drop shared perpendicular OM ⊥ AD from concentric Centre O.', s2:'Thm 5 on outer circle: AM = MD; Thm 5 on inner circle: BM = MC.', s3:'Subtract inner halves: AM − BM = MD − MC ⇒ AB = CD!' }
  ];
  window.c9c5s15Pick = function(i){
    const p = proofs[i];
    document.getElementById('c9c5s15Out').innerHTML = `
      <div class="text-emerald-300 font-bold text-sm font-sans">${p.t}</div>
      <div class="text-cyan-300">Step 1: ${p.s1}</div>
      <div class="text-amber-300">Step 2: ${p.s2}</div>
      <div class="text-purple-300 font-bold">Step 3: ${p.s3}</div>
    `;
  };
  c9c5s15Pick(0);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🏆</span> Chapter 5 Complete Theorems 1–12 &amp; Corollaries Reference Matrix
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c5s16Filter('all')" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">All 12 Theorems</button>
    <button type="button" onclick="c9c5s16Filter('chords')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Points &amp; Chords (1–8)</button>
    <button type="button" onclick="c9c5s16Filter('angles')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Arcs &amp; Cyclic (9–12)</button>
  </div>
  <div id="c9c5s16Out" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] max-h-56 overflow-y-auto custom-scrollbar pr-1"></div>
</div>
<script>
(function(){
  const thms = [
    { id:'Thm 1', cat:'chords', txt:'Unique circle passes through 3 non-collinear points (Circumcentre).' },
    { id:'Thm 2–3', cat:'chords', txt:'Equal chords ⇔ equal central angles (SSS / SAS congruence).' },
    { id:'Thm 4–5', cat:'chords', txt:'Centre-to-midpoint ⊥ chord ⇔ perpendicular from centre bisects chord.' },
    { id:'Thm 6–7', cat:'chords', txt:'Equal chords ⇔ equidistant from Centre O (r² = (L/2)² + d²).' },
    { id:'Thm 8', cat:'chords', txt:'Longer chord sits closer to O; diameter (d = 0) is longest chord.' },
    { id:'Thm 9', cat:'angles', txt:'Central angle = 2 × inscribed angle; semicircle = 90°; same segment equal.' },
    { id:'Thm 10', cat:'angles', txt:'Equal angles subtended on same side of segment ⇒ 4 points concyclic.' },
    { id:'Thm 11–12', cat:'angles', txt:'Cyclic quad opposite angles sum = 180° ⇔ 4 vertices concyclic.' }
  ];
  window.c9c5s16Filter = function(cat){
    const list = cat==='all' ? thms : thms.filter(d => d.cat===cat);
    document.getElementById('c9c5s16Out').innerHTML = list.map(d => `
      <div class="p-2 rounded bg-slate-950 border border-slate-800"><strong class="text-cyan-300">${d.id}:</strong> <span class="text-slate-300">${d.txt}</span></div>
    `).join('');
  };
  c9c5s16Filter('all');
})();
</script>
"""
}

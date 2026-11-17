#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 5: I'm Up and Down, and Round and Round
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⭕</span> Circle Locus, Chord, Diameter &amp; Central Angle Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Central Angle Subtended by Chord PQ: <strong id="c9c5s1AngVal" class="text-cyan-300">90°</strong></span>
    <input type="range" id="c9c5s1Ang" min="30" max="180" value="90" oninput="c9c5s1Draw()" class="w-full accent-cyan-400 mt-1.5">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c5s1Svg" viewBox="0 0 160 150" class="w-40 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c5s1Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c5s1Draw = function(){
    const deg = parseInt(document.getElementById('c9c5s1Ang').value);
    document.getElementById('c9c5s1AngVal').textContent = `${deg}°${deg===180?' (DIAMETER!)':''}`;
    const cx = 80, cy = 75, r = 52;
    const half = (deg * Math.PI / 180) / 2;
    const px = cx - r * Math.sin(half), py = cy - r * Math.cos(half);
    const qx = cx + r * Math.sin(half), qy = cy - r * Math.cos(half);
    const chord = (2 * r * Math.sin(half) / r * 10).toFixed(2);
    const svg = `
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="#0891b2" fill-opacity="0.12" stroke="#22d3ee" stroke-width="2"/>
      <line x1="${cx}" y1="${cy}" x2="${px}" y2="${py}" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="3 2"/>
      <line x1="${cx}" y1="${cy}" x2="${qx}" y2="${qy}" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="3 2"/>
      <line x1="${px}" y1="${py}" x2="${qx}" y2="${qy}" stroke="#34d399" stroke-width="2.8"/>
      <circle cx="${cx}" cy="${cy}" r="3.5" fill="#fbbf24"/><text x="${cx}" y="${cy+14}" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">O</text>
      <circle cx="${px}" cy="${py}" r="4" fill="#34d399"/><text x="${px-8}" y="${py}" fill="#6ee7b7" font-size="9">P</text>
      <circle cx="${qx}" cy="${qy}" r="4" fill="#34d399"/><text x="${qx+6}" y="${qy}" fill="#6ee7b7" font-size="9">Q</text>
    `;
    document.getElementById('c9c5s1Svg').innerHTML = svg;
    document.getElementById('c9c5s1Out').innerHTML = `
      <div class="font-bold text-cyan-300">Radius r = OP = OQ = 10 cm (Fixed Locus Distance)</div>
      <div class="font-mono text-emerald-300">Chord PQ Length = ${chord} cm | Central Angle ∠POQ = ${deg}°</div>
      <div class="text-amber-300 font-semibold">${deg===180 ? 'SPECIAL CASE: PQ passes straight through Centre O ⇒ PQ is a DIAMETER (2r = 20 cm)!' : 'Slide to 180° to see chord PQ pass through Centre O as a Diameter!'}</div>
    `;
  };
  c9c5s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🔄</span> Complete Circle Symmetry: Angle Rotation &amp; Diameter Reflection Axis
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Rotation Angle θ (about O): <strong id="c9c5s2RotVal" class="text-cyan-300">37°</strong></span>
      <input type="range" id="c9c5s2Rot" min="0" max="360" value="37" oninput="c9c5s2Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Mirror Diameter Tilt φ: <strong id="c9c5s2MirVal" class="text-amber-300">45°</strong></span>
      <input type="range" id="c9c5s2Mir" min="0" max="180" value="45" oninput="c9c5s2Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c5s2Svg" viewBox="0 0 150 150" class="w-36 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c5s2Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c5s2Draw = function(){
    const rot = parseInt(document.getElementById('c9c5s2Rot').value);
    const mir = parseInt(document.getElementById('c9c5s2Mir').value);
    document.getElementById('c9c5s2RotVal').textContent = `${rot}°`;
    document.getElementById('c9c5s2MirVal').textContent = `${mir}°`;
    const cx = 75, cy = 75, r = 50;
    const radR = rot * Math.PI / 180;
    const radM = mir * Math.PI / 180;
    const mx1 = cx - (r+14)*Math.cos(radM), my1 = cy - (r+14)*Math.sin(radM);
    const mx2 = cx + (r+14)*Math.cos(radM), my2 = cy + (r+14)*Math.sin(radM);
    const px = cx + r*Math.cos(radR), py = cy + r*Math.sin(radR);
    document.getElementById('c9c5s2Svg').innerHTML = `
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="#10b981" fill-opacity="0.12" stroke="#34d399" stroke-width="2.5"/>
      <line x1="${mx1}" y1="${my1}" x2="${mx2}" y2="${my2}" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="4 3"/>
      <line x1="${cx}" y1="${cy}" x2="${px}" y2="${py}" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="${px}" cy="${py}" r="4.5" fill="#38bdf8"/>
      <circle cx="${cx}" cy="${cy}" r="3.5" fill="#fbbf24"/>
    `;
    document.getElementById('c9c5s2Out').innerHTML = `
      <div class="font-bold text-emerald-300">100% Overlap Under Every Angle!</div>
      <p>Rotating by <strong>${rot}°</strong> maps the circle identically onto itself (complete rotational symmetry).</p>
      <p class="text-amber-300">Folding across diameter at <strong>${mir}°</strong> leaves identical halves (infinitely many reflection axes!).</p>
    `;
  };
  c9c5s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-indigo-300 flex items-center gap-2">
    <span>🎯</span> Two-Point Circle Generator (Centres Along Perpendicular Bisector)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Slide Centre O Along Perpendicular Bisector (Offset h): <strong id="c9c5s3HVal" class="text-cyan-300">h = 0 (Smallest Circle!)</strong></span>
    <input type="range" id="c9c5s3H" min="-35" max="35" value="0" oninput="c9c5s3Draw()" class="w-full accent-indigo-400 mt-1.5">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c5s3Svg" viewBox="0 0 180 150" class="w-44 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c5s3Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c5s3Draw = function(){
    const h = parseInt(document.getElementById('c9c5s3H').value);
    document.getElementById('c9c5s3HVal').textContent = h===0 ? 'h = 0 (Minimum Diameter Circle)' : `h = ${h}`;
    const ax = 62, bx = 118, ay = 75, mx = 90;
    const cy = 75 - h;
    const r = Math.hypot(mx - ax, h);
    document.getElementById('c9c5s3Svg').innerHTML = `
      <line x1="${mx}" y1="10" x2="${mx}" y2="140" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${ay}" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="${mx}" cy="${cy}" r="${r}" fill="#22d3ee" fill-opacity="0.1" stroke="#22d3ee" stroke-width="2"/>
      <circle cx="${ax}" cy="${ay}" r="4.5" fill="#fbbf24"/><text x="${ax-10}" y="${ay+4}" fill="#fbbf24" font-size="9" font-weight="bold">A</text>
      <circle cx="${bx}" cy="${ay}" r="4.5" fill="#fbbf24"/><text x="${bx+6}" y="${ay+4}" fill="#fbbf24" font-size="9" font-weight="bold">B</text>
      <circle cx="${mx}" cy="${cy}" r="3.5" fill="#34d399"/><text x="${mx+6}" y="${cy-4}" fill="#34d399" font-size="9" font-weight="bold">O</text>
    `;
    document.getElementById('c9c5s3Out').innerHTML = `
      <div class="font-bold text-cyan-300">OA = OB = Radius = ${r.toFixed(1)} units</div>
      <p>Every position of Centre O along the vertical perpendicular bisector keeps OA = OB seamlessly!</p>
      <div class="text-emerald-300 font-semibold">${h===0 ? 'At midpoint (h = 0), AB is diameter: smallest possible circle!' : 'Infinitely many points along the bisector ⇒ infinitely many circles through A & B!'}</div>
    `;
  };
  c9c5s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📐</span> Theorem 1: Unique Three-Point Circumcircle &amp; Triangle Circumcentre Finder
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c5s4Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Acute Δ (O Inside)</button>
    <button type="button" onclick="c9c5s4Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Right Δ (O on Hypotenuse)</button>
    <button type="button" onclick="c9c5s4Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Obtuse Δ (O Outside)</button>
    <button type="button" onclick="c9c5s4Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">3 Collinear Points (No Circle!)</button>
  </div>
  <div id="c9c5s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const cases = [
    { name:'Acute-Angled Triangle ABC', loc:'Strictly INSIDE ΔABC', why:'Perpendicular bisectors of AB and BC cross inside the triangle at unique circumcentre O.' },
    { name:'Right-Angled Triangle ABC (∠B = 90°)', loc:'Exact MIDPOINT of Hypotenuse AC', why:'Hypotenuse AC acts as a diameter, so circumcentre O sits right at midpoint M of AC (MA=MB=MC).' },
    { name:'Obtuse-Angled Triangle ABC (∠B > 90°)', loc:'Strictly OUTSIDE ΔABC (opposite ∠B)', why:'Obtuse angle forces long side AC closer to opposite side while circumcentre O moves outside past AC.' },
    { name:'Three Collinear Points P–Q–R', loc:'IMPOSSIBLE (Parallel Perpendicular Bisectors!)', why:'Perpendicular bisectors of PQ and QR run strictly parallel and never meet — proving 3 collinear points never share a circle.' }
  ];
  window.c9c5s4Pick = function(i){
    const d = cases[i];
    document.getElementById('c9c5s4Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">${d.name}</div>
      <div>Circumcentre Location: <strong class="text-amber-300">${d.loc}</strong></div>
      <p class="text-slate-300">${d.why}</p>
    `;
  };
  c9c5s4Pick(0);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>⚖️</span> Theorems 2 &amp; 3: Equal Chords ⇔ Equal Central Angles (SSS &amp; SAS)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Twin Chord Angle θ (∠AOB = ∠COD): <strong id="c9c5s5AngVal" class="text-cyan-300">72°</strong></span>
    <input type="range" id="c9c5s5Ang" min="35" max="130" value="72" oninput="c9c5s5Draw()" class="w-full accent-purple-400 mt-1.5">
  </label>
  <div id="c9c5s5Out" class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs"></div>
</div>
<script>
(function(){
  window.c9c5s5Draw = function(){
    const th = parseInt(document.getElementById('c9c5s5Ang').value);
    document.getElementById('c9c5s5AngVal').textContent = `${th}°`;
    const chord = (2 * 10 * Math.sin((th * Math.PI / 180)/2)).toFixed(2);
    document.getElementById('c9c5s5Out').innerHTML = `
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
        <div class="text-cyan-300 font-bold">Theorem 2 (Chords ⇒ Angles)</div>
        <div>Given AB = CD = <strong>${chord} cm</strong> (r = 10 cm)</div>
        <div class="text-emerald-300 font-semibold">SSS Congruence ⇒ ∠AOB = ∠COD = ${th}°</div>
      </div>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
        <div class="text-amber-300 font-bold">Theorem 3 Converse (Angles ⇒ Chords)</div>
        <div>Given ∠AOB = ∠COD = <strong>${th}°</strong> (r = 10 cm)</div>
        <div class="text-emerald-300 font-semibold">SAS Congruence ⇒ Chord AB = CD = ${chord} cm</div>
      </div>
    `;
  };
  c9c5s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Theorems 4 &amp; 5: Chord Bisector &amp; Right-Triangle Distance Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Radius r (OA): <strong id="c9c5s6RVal" class="text-cyan-300">13 cm</strong></span>
      <input type="range" id="c9c5s6R" min="5" max="20" value="13" oninput="c9c5s6Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Perpendicular Distance d (OM): <strong id="c9c5s6DVal" class="text-amber-300">5 cm</strong></span>
      <input type="range" id="c9c5s6D" min="0" max="15" value="5" oninput="c9c5s6Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c5s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s6Draw = function(){
    const r = parseInt(document.getElementById('c9c5s6R').value);
    const d = Math.min(r - 1, parseInt(document.getElementById('c9c5s6D').value));
    document.getElementById('c9c5s6RVal').textContent = `${r} cm`;
    document.getElementById('c9c5s6DVal').textContent = `${d} cm`;
    const half = Math.sqrt(r*r - d*d), full = 2*half;
    document.getElementById('c9c5s6Out').innerHTML = `
      <div class="text-cyan-300">Right ΔOMA: ∠OMA = 90° (Thm 4) &amp; AM = MB (Thm 5)</div>
      <div class="text-amber-300">Half-Chord AM = √(${r}² − ${d}²) = √(${r*r - d*d}) = ${half.toFixed(2)} cm</div>
      <div class="text-emerald-300 font-bold text-sm">Full Chord AB = 2 × AM = ${full.toFixed(2)} cm</div>
    `;
  };
  c9c5s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📏</span> Theorems 6 &amp; 7: Equidistant Chords Have Equal Length (OM = ON ⇔ AB = CD)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Shared Perpendicular Distance d = OM = ON (radius = 10 cm): <strong id="c9c5s7DVal" class="text-amber-300">6 cm</strong></span>
    <input type="range" id="c9c5s7D" min="0" max="9" value="6" oninput="c9c5s7Draw()" class="w-full accent-emerald-400 mt-1.5">
  </label>
  <div id="c9c5s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s7Draw = function(){
    const d = parseInt(document.getElementById('c9c5s7D').value);
    document.getElementById('c9c5s7DVal').textContent = `${d} cm`;
    const half = Math.sqrt(100 - d*d), L = 2 * half;
    document.getElementById('c9c5s7Out').innerHTML = `
      <div class="text-cyan-300">By RHS: ΔOAM ≅ ΔOCN (hypotenuse r = 10 cm, distance d = ${d} cm)</div>
      <div class="text-emerald-300 font-bold text-sm">Chord AB = Chord CD = 2√(10² − ${d}²) = ${L.toFixed(2)} cm!</div>
      <div class="text-slate-400 font-sans">Equal chords sit at identical distance from O (Thm 6), and equal distance forces equal chords (Thm 7).</div>
    `;
  };
  c9c5s7Draw();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>🔭</span> Theorem 8: Unequal Chords — Longer Chord Lies Closer to Centre O (r = 10 cm)
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Chord 1 Distance d₁: <strong id="c9c5s8D1Val" class="text-cyan-300">4 cm</strong></span>
      <input type="range" id="c9c5s8D1" min="0" max="9" value="4" oninput="c9c5s8Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Chord 2 Distance d₂: <strong id="c9c5s8D2Val" class="text-rose-300">8 cm</strong></span>
      <input type="range" id="c9c5s8D2" min="0" max="9" value="8" oninput="c9c5s8Draw()" class="w-full accent-rose-400 mt-1">
    </label>
  </div>
  <div id="c9c5s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c5s8Draw = function(){
    const d1 = parseInt(document.getElementById('c9c5s8D1').value);
    const d2 = parseInt(document.getElementById('c9c5s8D2').value);
    document.getElementById('c9c5s8D1Val').textContent = `${d1} cm`;
    document.getElementById('c9c5s8D2Val').textContent = `${d2} cm`;
    const L1 = 2 * Math.sqrt(100 - d1*d1), L2 = 2 * Math.sqrt(100 - d2*d2);
    const msg = d1 === d2 ? 'Equal distance ⇒ EQUAL chords!' : (d1 < d2 ? 'Chord 1 is CLOSER (d₁ < d₂) ⇒ Chord 1 is LONGER!' : 'Chord 2 is CLOSER (d₂ < d₁) ⇒ Chord 2 is LONGER!');
    document.getElementById('c9c5s8Out').innerHTML = `
      <div>Chord 1 (d₁=${d1}): Length = <strong class="text-cyan-300">${L1.toFixed(2)} cm</strong>${d1===0?' (DIAMETER!)':''}</div>
      <div>Chord 2 (d₂=${d2}): Length = <strong class="text-rose-300">${L2.toFixed(2)} cm</strong>${d2===0?' (DIAMETER!)':''}</div>
      <div class="text-emerald-300 font-bold pt-1">${msg}</div>
    `;
  };
  c9c5s8Draw();
})();
</script>
"""
}

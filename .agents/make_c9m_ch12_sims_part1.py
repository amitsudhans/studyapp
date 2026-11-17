#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 12: Quadrilaterals
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Planar Quadrilateral Guardrail Inspector
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c12s1Mode('valid')" id="c9c12s1Btn_valid" class="px-2.5 py-1.5 rounded-lg bg-emerald-600 text-white font-semibold">Valid Planar 4-Gon</button>
    <button onclick="c9c12s1Mode('collinear')" id="c9c12s1Btn_collinear" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Collinear Triple</button>
    <button onclick="c9c12s1Mode('skew')" id="c9c12s1Btn_skew" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Non-Planar (Skew)</button>
    <button onclick="c9c12s1Mode('bowtie')" id="c9c12s1Btn_bowtie" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Bowtie Crossing</button>
    <button onclick="c9c12s1Mode('open')" id="c9c12s1Btn_open" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Open Chain</button>
  </div>
  <svg id="c9c12s1Svg" viewBox="0 0 360 190" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s1Info" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c12s1Mode = function(mode){
    const modes = ['valid','collinear','skew','bowtie','open'];
    modes.forEach(m => {
      const b = document.getElementById('c9c12s1Btn_' + m);
      if (b) b.className = m === mode
        ? 'px-2.5 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold'
        : 'px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    });
    const svg = document.getElementById('c9c12s1Svg');
    const info = document.getElementById('c9c12s1Info');
    if (mode === 'valid') {
      svg.innerHTML = `
        <polygon points="70,150 280,155 255,40 105,55" fill="rgba(16,185,129,0.18)" stroke="#34d399" stroke-width="3"/>
        <circle cx="70" cy="150" r="5" fill="#fbbf24"/><text x="54" y="165" fill="#fbbf24" font-size="12" font-weight="bold">A</text>
        <circle cx="280" cy="155" r="5" fill="#fbbf24"/><text x="288" y="165" fill="#fbbf24" font-size="12" font-weight="bold">B</text>
        <circle cx="255" cy="40" r="5" fill="#fbbf24"/><text x="263" y="38" fill="#fbbf24" font-size="12" font-weight="bold">C</text>
        <circle cx="105" cy="55" r="5" fill="#fbbf24"/><text x="88" y="50" fill="#fbbf24" font-size="12" font-weight="bold">D</text>
        <text x="180" y="102" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">Angle Sum = 360°</text>`;
      info.innerHTML = '<span class="text-emerald-400 font-bold">VALID PLANAR QUADRILATERAL:</span> All 4 vertices are coplanar, no 3 are collinear, edges do not self-intersect, and DA closes back to A.';
    } else if (mode === 'collinear') {
      svg.innerHTML = `
        <line x1="60" y1="145" x2="300" y2="145" stroke="#ef4444" stroke-width="3" stroke-dasharray="5,4"/>
        <polygon points="60,145 180,145 300,145 175,45" fill="rgba(239,68,68,0.16)" stroke="#f87171" stroke-width="3"/>
        <circle cx="60" cy="145" r="5" fill="#fbbf24"/><text x="48" y="165" fill="#fbbf24" font-size="12">A</text>
        <circle cx="180" cy="145" r="5" fill="#ef4444"/><text x="176" y="165" fill="#f87171" font-size="12">B</text>
        <circle cx="300" cy="145" r="5" fill="#fbbf24"/><text x="298" y="165" fill="#fbbf24" font-size="12">C</text>
        <circle cx="175" cy="45" r="5" fill="#fbbf24"/><text x="172" y="34" fill="#fbbf24" font-size="12">D</text>`;
      info.innerHTML = '<span class="text-rose-400 font-bold">REJECTED (COLLINEAR TRIPLE):</span> Vertices A, B, and C lie on one straight line. Sides AB and BC merge, collapsing the figure into triangle ACD.';
    } else if (mode === 'skew') {
      svg.innerHTML = `
        <polygon points="65,135 205,155 285,95 145,75" fill="rgba(100,116,139,0.12)" stroke="#475569" stroke-dasharray="4,4"/>
        <polygon points="65,135 205,155 255,35" fill="rgba(245,158,11,0.18)" stroke="#fbbf24" stroke-width="2.5"/>
        <polygon points="65,135 145,75 255,35" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="65" y1="135" x2="255" y2="35" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="180" y="176" text-anchor="middle" fill="#fbbf24" font-size="11">Folded out of plane (3D Skew) ⇒ Σ∠ &lt; 360°</text>`;
      info.innerHTML = '<span class="text-amber-400 font-bold">REJECTED (NON-PLANAR / SKEW):</span> Vertex C is lifted out of the flat plane ABD. In 3D space, the interior angle sum drops strictly below 360°.';
    } else if (mode === 'bowtie') {
      svg.innerHTML = `
        <line x1="75" y1="45" x2="285" y2="145" stroke="#ef4444" stroke-width="3"/>
        <line x1="285" y1="45" x2="75" y2="145" stroke="#ef4444" stroke-width="3"/>
        <line x1="75" y1="45" x2="75" y2="145" stroke="#38bdf8" stroke-width="3"/>
        <line x1="285" y1="45" x2="285" y2="145" stroke="#38bdf8" stroke-width="3"/>
        <circle cx="180" cy="95" r="7" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
        <text x="180" y="172" text-anchor="middle" fill="#f87171" font-size="11">Self-intersection at non-vertex point!</text>`;
      info.innerHTML = '<span class="text-rose-400 font-bold">REJECTED (SELF-INTERSECTING BOWTIE):</span> Opposite segments cross at an interior point, breaking simple inside/outside separation.';
    } else {
      svg.innerHTML = `
        <polyline points="70,145 275,150 250,45 105,60" fill="none" stroke="#fbbf24" stroke-width="3"/>
        <line x1="105" y1="60" x2="70" y2="145" stroke="#ef4444" stroke-width="2" stroke-dasharray="5,5"/>
        <circle cx="70" cy="145" r="5" fill="#34d399"/><circle cx="105" cy="60" r="5" fill="#ef4444"/>
        <text x="180" y="175" text-anchor="middle" fill="#fbbf24" font-size="11">Missing closing edge DA (Open 3-segment path)</text>`;
      info.innerHTML = '<span class="text-amber-400 font-bold">REJECTED (OPEN PATH):</span> Without closing segment DA back to A, there is no enclosed 2D region or interior angles.';
    }
  };
  c9c12s1Mode('valid');
})();
</script>""",

    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪁</span> Convex vs Non-Convex Dent Simulator
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Push Vertex C Inward Toward A:</span>
      <span id="c9c12s2Lbl" class="text-amber-300 font-bold">Convex</span>
    </div>
    <input id="c9c12s2Slider" type="range" min="35" max="155" value="48" oninput="c9c12s2Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s2Svg" viewBox="0 0 360 190" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s2Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  function ang(p1, p, p2){
    const v1 = [p1[0]-p[0], p1[1]-p[1]], v2 = [p2[0]-p[0], p2[1]-p[1]];
    const dot = v1[0]*v2[0] + v1[1]*v2[1];
    const det = v1[0]*v2[1] - v1[1]*v2[0];
    let deg = Math.atan2(det, dot) * 180 / Math.PI;
    if (deg < 0) deg += 360;
    return deg;
  }
  window.c9c12s2Draw = function(){
    const t = parseFloat(document.getElementById('c9c12s2Slider').value);
    const A = [180, 165], B = [65, 65], D = [295, 65];
    const C = [180, t];
    const aA = ang(D, A, B), aB = ang(A, B, C), aC = ang(B, C, D), aD = ang(C, D, A);
    const reflex = aC > 180;
    document.getElementById('c9c12s2Lbl').textContent = reflex ? 'NON-CONVEX (Dent > 180°)' : 'CONVEX (All < 180°)';
    document.getElementById('c9c12s2Lbl').className = reflex ? 'text-rose-400 font-bold' : 'text-emerald-400 font-bold';
    document.getElementById('c9c12s2Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]} ${D[0]},${D[1]}" fill="${reflex ? 'rgba(244,63,94,0.18)' : 'rgba(16,185,129,0.18)'}" stroke="${reflex ? '#fb7185' : '#34d399'}" stroke-width="2.5"/>
      <line x1="${A[0]}" y1="${A[1]}" x2="${C[0]}" y2="${C[1]}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
      <line x1="${B[0]}" y1="${B[1]}" x2="${D[0]}" y2="${D[1]}" stroke="${reflex ? '#f59e0b' : '#38bdf8'}" stroke-width="2" stroke-dasharray="4,3"/>
      <text x="180" y="182" text-anchor="middle" fill="#cbd5e1" font-size="11">A (${aA.toFixed(0)}°)</text>
      <text x="48" y="68" fill="#cbd5e1" font-size="11">B (${aB.toFixed(0)}°)</text>
      <text x="180" y="${C[1]-10}" text-anchor="middle" fill="${reflex ? '#fb7185' : '#34d399'}" font-size="11" font-weight="bold">C (${aC.toFixed(0)}°)</text>
      <text x="303" y="68" fill="#cbd5e1" font-size="11">D (${aD.toFixed(0)}°)</text>`;
    document.getElementById('c9c12s2Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2">
        <div><span class="text-slate-400">Angle Sum:</span> <span class="text-cyan-300 font-bold">${(aA+aB+aC+aD).toFixed(0)}°</span> (always 360°)</div>
        <div><span class="text-slate-400">Diagonals Intersect?</span> <span class="${reflex ? 'text-rose-400' : 'text-emerald-400'} font-bold">${reflex ? 'NO (BD outside)' : 'YES (inside)'}</span></div>
      </div>`;
  };
  c9c12s2Draw();
})();
</script>""",

    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Theorem 2: Opposite Sides Equal ⇒ Parallelogram (SSS)
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between mb-1"><span>Base a = AB = CD:</span><span id="c9c12s3ALbl" class="text-cyan-300 font-bold">140</span></div>
      <input id="c9c12s3A" type="range" min="90" max="170" value="140" oninput="c9c12s3Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between mb-1"><span>Tilt Angle θ:</span><span id="c9c12s3TLbl" class="text-amber-300 font-bold">62°</span></div>
      <input id="c9c12s3T" type="range" min="35" max="135" value="62" oninput="c9c12s3Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <svg id="c9c12s3Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s3Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c12s3Draw = function(){
    const a = parseFloat(document.getElementById('c9c12s3A').value);
    const th = parseFloat(document.getElementById('c9c12s3T').value);
    document.getElementById('c9c12s3ALbl').textContent = (a/10).toFixed(1) + ' cm';
    document.getElementById('c9c12s3TLbl').textContent = th + '°';
    const b = 95, rad = th * Math.PI / 180;
    const A = [85, 148], B = [85 + a, 148];
    const D = [A[0] + b*Math.cos(rad), A[1] - b*Math.sin(rad)];
    const C = [B[0] + b*Math.cos(rad), B[1] - b*Math.sin(rad)];
    document.getElementById('c9c12s3Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]}" fill="rgba(56,189,248,0.16)" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="${A[0]},${A[1]} ${C[0]},${C[1]} ${D[0]},${D[1]}" fill="rgba(16,185,129,0.16)" stroke="#34d399" stroke-width="2.5"/>
      <line x1="${A[0]}" y1="${A[1]}" x2="${C[0]}" y2="${C[1]}" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5,3"/>
      <text x="${A[0]-12}" y="${A[1]+14}" fill="#f8fafc" font-size="11" font-weight="bold">A</text>
      <text x="${B[0]+6}" y="${B[1]+14}" fill="#f8fafc" font-size="11" font-weight="bold">B</text>
      <text x="${C[0]+6}" y="${C[1]-6}" fill="#f8fafc" font-size="11" font-weight="bold">C</text>
      <text x="${D[0]-14}" y="${D[1]-6}" fill="#f8fafc" font-size="11" font-weight="bold">D</text>
      <text x="180" y="22" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">ΔABC ≅ ΔCDA by SSS ⇒ AB ∥ CD &amp; BC ∥ DA</text>`;
    document.getElementById('c9c12s3Out').innerHTML =
      'SSS Proof: <span class="text-cyan-300 font-semibold">AB = CD = ' + (a/10).toFixed(1) + ' cm</span>, <span class="text-emerald-300 font-semibold">BC = DA = 9.5 cm</span>, and <span class="text-amber-300 font-semibold">AC = CA</span>. CPCTC gives equal alternate interior angles ⇒ Parallelogram!';
  };
  c9c12s3Draw();
})();
</script>""",

    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Theorem 3: Opposite Angles Equal ⇒ Parallelogram
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Set Opposite Angles ∠A = ∠C:</span>
      <span id="c9c12s4Lbl" class="text-amber-300 font-bold">∠A = ∠C = 65°, ∠B = ∠D = 115°</span>
    </div>
    <input id="c9c12s4A" type="range" min="40" max="140" value="65" oninput="c9c12s4Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s4Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s4Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c12s4Draw = function(){
    const a = parseInt(document.getElementById('c9c12s4A').value, 10);
    const b = 180 - a;
    document.getElementById('c9c12s4Lbl').textContent = '∠A = ∠C = ' + a + '°, ∠B = ∠D = ' + b + '°';
    const rad = a * Math.PI / 180, L = 140, H = 95;
    const A = [85, 145], B = [85 + L, 145];
    const D = [A[0] + H*Math.cos(rad), A[1] - H*Math.sin(rad)];
    const C = [B[0] + H*Math.cos(rad), B[1] - H*Math.sin(rad)];
    document.getElementById('c9c12s4Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]} ${D[0]},${D[1]}" fill="rgba(99,102,241,0.18)" stroke="#818cf8" stroke-width="2.5"/>
      <text x="${A[0]+14}" y="${A[1]-10}" fill="#fbbf24" font-size="11" font-weight="bold">A=${a}°</text>
      <text x="${B[0]-42}" y="${B[1]-10}" fill="#34d399" font-size="11" font-weight="bold">B=${b}°</text>
      <text x="${C[0]-42}" y="${C[1]+18}" fill="#fbbf24" font-size="11" font-weight="bold">C=${a}°</text>
      <text x="${D[0]+10}" y="${D[1]+18}" fill="#34d399" font-size="11" font-weight="bold">D=${b}°</text>
      <text x="180" y="22" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">∠A + ∠B = ${a}° + ${b}° = 180° ⇒ AD ∥ BC</text>`;
    document.getElementById('c9c12s4Out').innerHTML =
      'Algebraic Proof: <span class="text-amber-300 font-semibold">2(' + a + '°) + 2(' + b + '°) = 360°</span> ⇒ <span class="text-cyan-300 font-semibold">∠A + ∠B = 180°</span> (co-interior supplementary ⇒ AD ∥ BC) and <span class="text-emerald-300 font-semibold">∠A + ∠D = 180°</span> (⇒ AB ∥ DC).';
  };
  c9c12s4Draw();
})();
</script>""",

    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✖️</span> Theorems 4 &amp; 5: Bisecting Diagonals vs Single-Pair Test
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c12s5Tab('thm4')" id="c9c12s5B_thm4" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Thm 4: Bisecting Diagonals</button>
    <button onclick="c9c12s5Tab('thm5')" id="c9c12s5B_thm5" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Thm 5: AB = CD &amp; AB ∥ CD</button>
    <button onclick="c9c12s5Tab('trap')" id="c9c12s5B_trap" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Trap: AB ∥ CD &amp; BC = DA</button>
  </div>
  <svg id="c9c12s5Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s5Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c12s5Tab = function(t){
    ['thm4','thm5','trap'].forEach(k => {
      document.getElementById('c9c12s5B_' + k).className = k === t
        ? 'px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold'
        : 'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    });
    const svg = document.getElementById('c9c12s5Svg');
    const out = document.getElementById('c9c12s5Out');
    if (t === 'thm4') {
      svg.innerHTML = `
        <polygon points="75,145 235,145 285,45 125,45" fill="rgba(16,185,129,0.14)" stroke="#34d399" stroke-width="2.5"/>
        <line x1="75" y1="145" x2="285" y2="45" stroke="#fbbf24" stroke-width="2"/>
        <line x1="235" y1="145" x2="125" y2="45" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="180" cy="95" r="4.5" fill="#f43f5e"/><text x="180" y="83" text-anchor="middle" fill="#f43f5e" font-size="11" font-weight="bold">O</text>
        <text x="180" y="22" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">OA = OC, OB = OD ⇒ ΔAOB ≅ ΔCOD (SAS)</text>`;
      out.innerHTML = '<span class="text-emerald-400 font-bold">THEOREM 4 (PARALLELOGRAM):</span> Vertically opposite angles at O plus equal half-diagonals give SAS congruence, forcing opposite sides parallel.';
    } else if (t === 'thm5') {
      svg.innerHTML = `
        <polygon points="80,145 240,145 285,45 125,45" fill="rgba(56,189,248,0.14)" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="80" y1="145" x2="240" y2="145" stroke="#fbbf24" stroke-width="4"/>
        <line x1="125" y1="45" x2="285" y2="45" stroke="#fbbf24" stroke-width="4"/>
        <line x1="80" y1="145" x2="285" y2="45" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="180" y="22" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Same Pair AB = CD &amp; AB ∥ CD ⇒ ΔABC ≅ ΔCDA (SAS)</text>`;
      out.innerHTML = '<span class="text-cyan-300 font-bold">THEOREM 5 (PARALLELOGRAM):</span> One pair both equal AND parallel gives equal alternate angles along AC, proving BC = DA and BC ∥ DA.';
    } else {
      svg.innerHTML = `
        <polygon points="65,145 295,145 245,45 115,45" fill="rgba(244,63,94,0.15)" stroke="#fb7185" stroke-width="2.5"/>
        <line x1="115" y1="45" x2="245" y2="45" stroke="#38bdf8" stroke-width="3"/>
        <line x1="65" y1="145" x2="295" y2="145" stroke="#38bdf8" stroke-width="3"/>
        <text x="180" y="22" text-anchor="middle" fill="#fb7185" font-size="11" font-weight="bold">Counterexample: Isosceles Trapezium (NOT a Parallelogram!)</text>`;
      out.innerHTML = '<span class="text-rose-400 font-bold">TRAP AVOIDED:</span> If one pair is parallel (AB ∥ CD) and the OTHER pair is equal (BC = DA), you can get an isosceles trapezium instead of a parallelogram!';
    }
  };
  c9c12s5Tab('thm4');
})();
</script>""",

    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚙️</span> Parallelogram Applications: Watt Linkage &amp; Force Vectors
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c12s6Mode('watt')" id="c9c12s6B_watt" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Watt Straight-Line Linkage</button>
    <button onclick="c9c12s6Mode('force')" id="c9c12s6B_force" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Physics Force Parallelogram</button>
  </div>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between mb-1"><span id="c9c12s6ParamName">Linkage Rocker Angle:</span><span id="c9c12s6Val" class="text-amber-300 font-bold">0°</span></div>
    <input id="c9c12s6Slider" type="range" min="-35" max="35" value="0" oninput="c9c12s6Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s6Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  let cur = 'watt';
  window.c9c12s6Mode = function(m){
    cur = m;
    document.getElementById('c9c12s6B_watt').className = m === 'watt' ? 'px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold' : 'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    document.getElementById('c9c12s6B_force').className = m === 'force' ? 'px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold' : 'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    const sl = document.getElementById('c9c12s6Slider');
    if (m === 'watt') { sl.min = -35; sl.max = 35; sl.value = 0; document.getElementById('c9c12s6ParamName').textContent = 'Rocker Tilt Angle:'; }
    else { sl.min = 25; sl.max = 135; sl.value = 60; document.getElementById('c9c12s6ParamName').textContent = 'Angle Between F₁ & F₂:'; }
    c9c12s6Draw();
  };
  window.c9c12s6Draw = function(){
    const v = parseFloat(document.getElementById('c9c12s6Slider').value);
    document.getElementById('c9c12s6Val').textContent = v + '°';
    const svg = document.getElementById('c9c12s6Svg');
    if (cur === 'watt') {
      const r = v * Math.PI / 180;
      const P1 = [80, 70], P2 = [280, 115], L = 85;
      const A = [P1[0] + L*Math.cos(r), P1[1] + L*Math.sin(r)];
      const B = [P2[0] - L*Math.cos(r), P2[1] + L*Math.sin(r)];
      const M = [(A[0]+B[0])/2, (A[1]+B[1])/2];
      svg.innerHTML = `
        <line x1="180" y1="30" x2="180" y2="165" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
        <line x1="${P1[0]}" y1="${P1[1]}" x2="${A[0]}" y2="${A[1]}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
        <line x1="${P2[0]}" y1="${P2[1]}" x2="${B[0]}" y2="${B[1]}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
        <line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="#fbbf24" stroke-width="4" stroke-linecap="round"/>
        <circle cx="${P1[0]}" cy="${P1[1]}" r="5" fill="#94a3b8"/><circle cx="${P2[0]}" cy="${P2[1]}" r="5" fill="#94a3b8"/>
        <circle cx="${M[0]}" cy="${M[1]}" r="6" fill="#34d399"/>
        <text x="180" y="22" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Midpoint Tracer M x = ${M[0].toFixed(1)} (nearly vertical line!)</text>`;
    } else {
      const r = v * Math.PI / 180, O = [90, 145], f1 = 130, f2 = 90;
      const A = [O[0]+f1, O[1]], B = [O[0]+f2*Math.cos(r), O[1]-f2*Math.sin(r)];
      const C = [A[0]+f2*Math.cos(r), A[1]-f2*Math.sin(r)];
      const mag = Math.sqrt(13*13 + 9*9 + 2*13*9*Math.cos(r)).toFixed(1);
      svg.innerHTML = `
        <polygon points="${O[0]},${O[1]} ${A[0]},${A[1]} ${C[0]},${C[1]} ${B[0]},${B[1]}" fill="rgba(56,189,248,0.12)" stroke="#475569" stroke-dasharray="4,3"/>
        <line x1="${O[0]}" y1="${O[1]}" x2="${A[0]}" y2="${A[1]}" stroke="#38bdf8" stroke-width="3.5"/>
        <line x1="${O[0]}" y1="${O[1]}" x2="${B[0]}" y2="${B[1]}" stroke="#34d399" stroke-width="3.5"/>
        <line x1="${O[0]}" y1="${O[1]}" x2="${C[0]}" y2="${C[1]}" stroke="#fbbf24" stroke-width="4"/>
        <text x="${(O[0]+A[0])/2}" y="${O[1]+16}" fill="#38bdf8" font-size="11" font-weight="bold">F₁ = 13 N</text>
        <text x="${B[0]-35}" y="${B[1]-6}" fill="#34d399" font-size="11" font-weight="bold">F₂ = 9 N</text>
        <text x="${C[0]+6}" y="${C[1]}" fill="#fbbf24" font-size="11" font-weight="bold">R = ${mag} N</text>`;
    }
  };
  c9c12s6Mode('watt');
})();
</script>""",

    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔺</span> Theorem 6: Midpoint Theorem &amp; Auxiliary Parallelogram
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Shift Apex A Horizontally:</span>
      <span id="c9c12s7Lbl" class="text-amber-300 font-bold">BC = 18.0 cm, DE = 9.0 cm</span>
    </div>
    <input id="c9c12s7Ax" type="range" min="70" max="240" value="135" oninput="c9c12s7Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s7Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c12s7Draw = function(){
    const ax = parseFloat(document.getElementById('c9c12s7Ax').value);
    const A = [ax, 35], B = [55, 155], C = [235, 155];
    const D = [(A[0]+B[0])/2, (A[1]+B[1])/2];
    const E = [(A[0]+C[0])/2, (A[1]+C[1])/2];
    const F = [2*E[0]-D[0], 2*E[1]-D[1]];
    document.getElementById('c9c12s7Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]}" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="${C[0]},${C[1]} ${E[0]},${E[1]} ${F[0]},${F[1]}" fill="rgba(245,158,11,0.16)" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/>
      <line x1="${D[0]}" y1="${D[1]}" x2="${E[0]}" y2="${E[1]}" stroke="#34d399" stroke-width="3.5"/>
      <line x1="${E[0]}" y1="${E[1]}" x2="${F[0]}" y2="${F[1]}" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4,3"/>
      <text x="${A[0]}" y="${A[1]-8}" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">A</text>
      <text x="${B[0]-10}" y="${B[1]+14}" fill="#f8fafc" font-size="11" font-weight="bold">B</text>
      <text x="${C[0]+6}" y="${C[1]+14}" fill="#f8fafc" font-size="11" font-weight="bold">C</text>
      <text x="${D[0]-14}" y="${D[1]}" fill="#34d399" font-size="11" font-weight="bold">D</text>
      <text x="${E[0]+5}" y="${E[1]-8}" fill="#34d399" font-size="11" font-weight="bold">E</text>
      <text x="${F[0]+6}" y="${F[1]}" fill="#fbbf24" font-size="11" font-weight="bold">F</text>
      <text x="180" y="177" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">DE ∥ BC  &amp;  DE = ½DF = ½BC  (BCFD is a Parallelogram)</text>`;
  };
  c9c12s7Draw();
})();
</script>""",

    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Theorem 7: Converse Midpoint &amp; Segment Trisection
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Equal Subdivisions (n):</span>
      <span id="c9c12s8Lbl" class="text-amber-300 font-bold">n = 3 (Trisection)</span>
    </div>
    <input id="c9c12s8N" type="range" min="2" max="5" value="3" oninput="c9c12s8Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s8Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c12s8Draw = function(){
    const n = parseInt(document.getElementById('c9c12s8N').value, 10);
    const names = {2:'Bisection',3:'Trisection',4:'Quadrisection',5:'5 Equal Parts'};
    document.getElementById('c9c12s8Lbl').textContent = 'n = ' + n + ' (' + names[n] + ')';
    const A = [55, 140], B = [305, 140], RayEnd = [265, 35];
    let html = `<line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="#38bdf8" stroke-width="3.5"/>`;
    html += `<line x1="${A[0]}" y1="${A[1]}" x2="${RayEnd[0]}" y2="${RayEnd[1]}" stroke="#94a3b8" stroke-width="2"/>`;
    for (let i = 1; i <= n; i++) {
      const f = i / n;
      const px = A[0] + f*(RayEnd[0]-A[0]), py = A[1] + f*(RayEnd[1]-A[1]);
      const qx = A[0] + f*(B[0]-A[0]), qy = A[1];
      html += `<line x1="${px}" y1="${py}" x2="${qx}" y2="${qy}" stroke="${i===n ? '#fbbf24' : '#34d399'}" stroke-width="2" stroke-dasharray="${i===n ? '' : '4,3'}"/>`;
      html += `<circle cx="${px}" cy="${py}" r="4" fill="#fbbf24"/><circle cx="${qx}" cy="${qy}" r="4.5" fill="#34d399"/>`;
    }
    html += `<text x="45" y="158" fill="#f8fafc" font-size="11" font-weight="bold">A</text><text x="305" y="158" fill="#f8fafc" font-size="11" font-weight="bold">B</text>`;
    html += `<text x="180" y="174" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Parallel lines transfer ${n} equal ray marks onto AB</text>`;
    document.getElementById('c9c12s8Svg').innerHTML = html;
  };
  c9c12s8Draw();
})();
</script>""",
}

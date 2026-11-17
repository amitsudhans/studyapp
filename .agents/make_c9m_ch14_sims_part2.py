#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 14: Math of Space: Surface Area and Volume
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌍</span> Archimedes Sphere-in-Cylinder &amp; Map Distortion
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Sphere Radius r (cm):</span>
      <span id="c9c14s9RL" class="text-amber-300 font-bold">r = 7 cm (h = 14 cm)</span>
    </div>
    <input id="c9c14s9R" type="range" min="3" max="14" value="7" oninput="c9c14s9Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c14s9Draw = function(){
    const r = parseInt(document.getElementById('c9c14s9R').value, 10);
    document.getElementById('c9c14s9RL').textContent = 'r = ' + r + ' cm (Cylinder h = ' + (2*r) + ' cm)';
    const sa = (4*Math.PI*r*r).toFixed(1);
    const vs = ((4/3)*Math.PI*r*r*r).toFixed(1);
    const vc = (2*Math.PI*r*r*r).toFixed(1);
    document.getElementById('c9c14s9Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2">
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Sphere SA = Cyl CSA = <span class="text-cyan-300 font-bold">${sa} cm²</span></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800">V_sphere / V_cyl = <span class="text-amber-300 font-bold">${vs} / ${vc} = 2/3</span></div>
      </div>
      <div class="text-emerald-300">Equirectangular Map Note: Stretching polar latitude circles onto the cylinder wall enlarges Greenland visually!</div>`;
  };
  c9c14s9Draw();
})();
</script>""",

    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧶</span> String-Wrapping Verification: 1 Sphere = 4 Circles
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Unwind String onto Flat Circles of Radius r:</span>
      <span id="c9c14s10Lbl" class="text-amber-300 font-bold">4 / 4 Circles Filled (4πr²)</span>
    </div>
    <input id="c9c14s10C" type="range" min="0" max="4" value="4" oninput="c9c14s10Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c14s10Svg" viewBox="0 0 360 130" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c14s10Draw = function(){
    const k = parseInt(document.getElementById('c9c14s10C').value, 10);
    document.getElementById('c9c14s10Lbl').textContent = k + ' / 4 Circles Filled (' + k + 'πr²)';
    let html = '';
    for (let i=0; i<4; i++){
      const cx = 55 + i*83;
      html += `<circle cx="${cx}" cy="60" r="32" fill="${i<k?'rgba(245,158,11,0.35)':'none'}" stroke="${i<k?'#fbbf24':'#475569'}" stroke-width="2.5"/>`;
      html += `<text x="${cx}" y="64" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">πr²</text>`;
    }
    html += `<text x="180" y="118" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Sphere String Covers Exactly 4 Circles ⇒ SA = 4πr²</text>`;
    document.getElementById('c9c14s10Svg').innerHTML = html;
  };
  c9c14s10Draw();
})();
</script>""",

    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🍉</span> Hemisphere CSA (2πr²), Solid TSA (3πr²) &amp; Volume (⅔πr³)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Hemisphere Radius r (cm):</span>
      <span id="c9c14s11RL" class="text-amber-300 font-bold">r = 7 cm</span>
    </div>
    <input id="c9c14s11R" type="range" min="3.5" max="14" step="3.5" value="7" oninput="c9c14s11Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 grid grid-cols-3 gap-2"></div>
</div>
<script>
(function(){
  window.c9c14s11Draw = function(){
    const r = parseFloat(document.getElementById('c9c14s11R').value);
    document.getElementById('c9c14s11RL').textContent = 'r = ' + r + ' cm';
    const pi = 22/7;
    document.getElementById('c9c14s11Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">CSA (2πr²)</div><div class="font-bold text-cyan-300">${(2*pi*r*r).toFixed(1)} cm²</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Solid TSA (3πr²)</div><div class="font-bold text-emerald-300">${(3*pi*r*r).toFixed(1)} cm²</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Volume (⅔πr³)</div><div class="font-bold text-amber-300">${((2/3)*pi*r*r*r).toFixed(1)} cm³</div></div>`;
  };
  c9c14s11Draw();
})();
</script>""",

    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚰</span> Rooftop Water Tank Capacity &amp; Unit Converter (1 m³ = 1000 L)
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Tank Radius (m):</span><span id="c9c14s12RL" class="text-cyan-300 font-bold">0.7 m</span></div>
      <input id="c9c14s12R" type="range" min="0.5" max="2.0" step="0.1" value="0.7" oninput="c9c14s12Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Tank Height (m):</span><span id="c9c14s12HL" class="text-amber-300 font-bold">1.5 m</span></div>
      <input id="c9c14s12H" type="range" min="1.0" max="4.0" step="0.5" value="1.5" oninput="c9c14s12Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c14s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c14s12Draw = function(){
    const r = parseFloat(document.getElementById('c9c14s12R').value);
    const h = parseFloat(document.getElementById('c9c14s12H').value);
    document.getElementById('c9c14s12RL').textContent = r.toFixed(1) + ' m';
    document.getElementById('c9c14s12HL').textContent = h.toFixed(1) + ' m';
    const v = Math.PI * r * r * h;
    document.getElementById('c9c14s12Out').innerHTML =
      'Volume = <span class="text-cyan-300 font-bold">' + v.toFixed(2) + ' m³</span> = <span class="text-emerald-400 font-bold">' + Math.round(v*1000).toLocaleString() + ' Litres</span>.';
  };
  c9c14s12Draw();
})();
</script>""",

    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎾</span> Guesstimate Lab: Golgappas &amp; Sphere Packing Efficiency
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Sphere Packing Efficiency (%):</span>
      <span id="c9c14s13EL" class="text-amber-300 font-bold">74% (Tightest 3D Packing)</span>
    </div>
    <input id="c9c14s13E" type="range" min="52" max="74" value="74" oninput="c9c14s13Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c14s13Draw = function(){
    const eff = parseInt(document.getElementById('c9c14s13E').value, 10);
    document.getElementById('c9c14s13EL').textContent = eff + '% (' + (100-eff) + '% Void Air Gaps)';
    const roomVol = 150000000; // 150 m^3 in cm^3
    const ballVol = 143; // ~r=3.25 cm tennis ball
    const count = Math.round((roomVol * (eff/100)) / ballVol);
    document.getElementById('c9c14s13Out').innerHTML =
      'In a 150 m³ classroom, tennis balls (~143 cm³ each) at <span class="text-cyan-300 font-bold">' + eff + '% packing efficiency</span> fit roughly <span class="text-amber-300 font-bold">' + count.toLocaleString() + ' balls</span> (never 100% due to void gaps)!';
  };
  c9c14s13Draw();
})();
</script>""",

    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎨</span> Painted n×n×n Cut-Cube Face Counter
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Cube Grid Size n:</span>
      <span id="c9c14s14NL" class="text-amber-300 font-bold">4 × 4 × 4 (64 unit cubes)</span>
    </div>
    <input id="c9c14s14N" type="range" min="2" max="7" value="4" oninput="c9c14s14Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 grid grid-cols-2 sm:grid-cols-4 gap-2"></div>
</div>
<script>
(function(){
  window.c9c14s14Draw = function(){
    const n = parseInt(document.getElementById('c9c14s14N').value, 10);
    document.getElementById('c9c14s14NL').textContent = n + ' × ' + n + ' × ' + n + ' (' + (n*n*n) + ' unit cubes)';
    const f3 = 8, f2 = 12*(n-2), f1 = 6*(n-2)*(n-2), f0 = (n-2)*(n-2)*(n-2);
    document.getElementById('c9c14s14Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">3 Faces</div><div class="font-bold text-rose-300">${f3}</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">2 Faces</div><div class="font-bold text-amber-300">${f2}</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">1 Face</div><div class="font-bold text-cyan-300">${f1}</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">0 Faces</div><div class="font-bold text-emerald-300">${f0}</div></div>`;
  };
  c9c14s14Draw();
})();
</script>""",

    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🐦</span> Archimedes Crow-and-Pitcher Marble Displacement
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Spherical Marbles Dropped (r = 1 cm):</span>
      <span id="c9c14s15ML" class="text-amber-300 font-bold">75 Marbles (Water at Rim!)</span>
    </div>
    <input id="c9c14s15M" type="range" min="0" max="75" step="5" value="75" oninput="c9c14s15Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c14s15Draw = function(){
    const m = parseInt(document.getElementById('c9c14s15M').value, 10);
    const rise = (m * (4/3) / 25).toFixed(2);
    document.getElementById('c9c14s15ML').textContent = m + ' Marbles (Water +{rise} cm)'.replace('{rise}', rise);
    document.getElementById('c9c14s15Out').innerHTML =
      'Each marble displaces (4/3)π cm³ in a pitcher of base area 25π cm². Dropping <span class="text-amber-300 font-bold">' + m + ' marbles</span> raises water by <span class="text-cyan-300 font-bold">' + rise + ' cm</span> (75 marbles = full 4.00 cm rise to rim)!';
  };
  c9c14s15Draw();
})();
</script>""",

    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏆</span> Chapter 14 Formula Table &amp; Fold-Out 2D Nets
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c14s16Set(0)" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-white font-semibold">Cuboid</button>
    <button onclick="c9c14s16Set(1)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Cylinder</button>
    <button onclick="c9c14s16Set(2)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Cone</button>
    <button onclick="c9c14s16Set(3)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Sphere</button>
    <button onclick="c9c14s16Set(4)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Hemisphere</button>
  </div>
  <div id="c9c14s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const tbl = [
    '<div class="text-amber-300 font-bold">Cuboid (l, w, h) &amp; Cube (a)</div><div>TSA = 2(wl + hl + hw) [Cube: 6a²] | Volume = lwh [Cube: a³] | Net: 6 rectangles</div>',
    '<div class="text-cyan-300 font-bold">Right Circular Cylinder (r, h)</div><div>CSA = 2πrh | Closed TSA = 2πr(h + r) | Volume = πr²h | Net: 1 rectangle (2πr × h) + 2 circles</div>',
    '<div class="text-emerald-300 font-bold">Right Circular Cone (r, h, l)</div><div>l² = h² + r² | CSA = πrl | TSA = πr(l + r) | Volume = ⅓πr²h | Net: 1 circular sector + 1 circle</div>',
    '<div class="text-rose-300 font-bold">Sphere (radius r)</div><div>Surface Area = 4πr² (4 great-circle discs) | Volume = (4/3)πr³ (2/3 of circumscribed cylinder)</div>',
    '<div class="text-indigo-300 font-bold">Solid Hemisphere (radius r)</div><div>CSA = 2πr² | Solid TSA = 3πr² | Volume = (2/3)πr³</div>'
  ];
  window.c9c14s16Set = function(i){
    document.getElementById('c9c14s16Out').innerHTML = tbl[i];
  };
  c9c14s16Set(0);
})();
</script>""",
}

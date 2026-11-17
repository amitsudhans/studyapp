#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 1: Orienting Yourself: The Use of Coordinates
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏛️</span> Sindhu-Sarasvatī ~10 m Urban Grid &amp; Baudhāyana Orthogonal Cords
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s1Mode(0)" id="c9s1b0" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">~10 m Grid Streets</button>
    <button type="button" onclick="c9s1Mode(1)" id="c9s1b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Block Addressing (E, N)</button>
    <button type="button" onclick="c9s1Mode(2)" id="c9s1b2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Baudhāyana Prācī Cord</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s1Svg" viewBox="0 0 220 170" class="w-56 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s1Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const info = [
    ['Sindhu-Sarasvatī ~10 m Orthogonal Grid', 'Main north-south avenues and east-west cross-streets met cleanly at 90°, organizing Mohenjo-daro and Kalibangan into rectangular house blocks.'],
    ['City Block Coordinate Addressing', 'Locating the Great Bath or Granary at (Avenue 3 East, Street 2 North) anticipates modern ordered pairs (x, y) on an urban grid!'],
    ['Baudhāyana Śulba-Sūtra Orthogonal Cords (c. 800 BCE)', 'Using a taut east-west reference line (prācī) and stretched peg-and-cord triplets (3-4-5, 5-12-13), builders generated exact perpendicular north-south axes on ground.']
  ];
  window.c9s1Mode = function(m){
    [0,1,2].forEach(i => {
      const b = document.getElementById('c9s1b'+i);
      if(b) b.className = i===m ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const svg = document.getElementById('c9s1Svg');
    let h = '';
    if(m===0 || m===1){
      for(let x=25; x<=195; x+=34){ h += `<line x1="${x}" y1="15" x2="${x}" y2="155" stroke="${x===93?'#22d3ee':'#334155'}" stroke-width="${x===93?4:2.5}"/>`; }
      for(let y=20; y<=150; y+=32){ h += `<line x1="20" y1="${y}" x2="200" y2="${y}" stroke="${y===84?'#fbbf24':'#334155'}" stroke-width="${y===84?4:2.5}"/>`; }
      for(let gx=30; gx<190; gx+=34){
        for(let gy=25; gy<145; gy+=32){
          h += `<rect x="${gx}" y="${gy}" width="24" height="22" rx="2" fill="#0f172a" stroke="#475569" stroke-width="1"/>`;
        }
      }
      if(m===0){
        h += `<text x="110" y="12" fill="#22d3ee" font-size="8" text-anchor="middle">N-S Main Avenue (~10 m wide)</text>`;
        h += `<text x="15" y="87" fill="#fbbf24" font-size="8">E-W</text>`;
      } else {
        h += `<circle cx="127" cy="52" r="5" fill="#34d399"/><text x="134" y="49" fill="#34d399" font-size="8.5" font-weight="bold">Block (3, 2)</text>`;
        h += `<circle cx="59" cy="116" r="5" fill="#f472b6"/><text x="34" y="130" fill="#f472b6" font-size="8.5" font-weight="bold">Well (1, 1)</text>`;
      }
    } else {
      h += `<line x1="25" y1="125" x2="195" y2="125" stroke="#fbbf24" stroke-width="2.5"/>`;
      h += `<line x1="75" y1="25" x2="75" y2="145" stroke="#22d3ee" stroke-width="2.5"/>`;
      h += `<line x1="75" y1="53" x2="171" y2="125" stroke="#34d399" stroke-width="2" stroke-dasharray="4 2"/>`;
      h += `<rect x="75" y="113" width="12" height="12" fill="none" stroke="#22d3ee" stroke-width="1.2"/>`;
      h += `<circle cx="75" cy="125" r="4" fill="#fff"/><circle cx="171" cy="125" r="4" fill="#fbbf24"/><circle cx="75" cy="53" r="4" fill="#22d3ee"/>`;
      h += `<text x="145" y="138" fill="#fbbf24" font-size="8.5">Prācī (East-West) = 4</text>`;
      h += `<text x="20" y="75" fill="#22d3ee" font-size="8.5">Orthogonal = 3</text>`;
      h += `<text x="128" y="82" fill="#34d399" font-size="8.5">Cord = 5</text>`;
    }
    svg.innerHTML = h;
    document.getElementById('c9s1Out').innerHTML = `<div class="font-bold text-cyan-300">${info[m][0]}</div><p class="leading-relaxed">${info[m][1]}</p><div class="text-[11px] text-amber-300">Perpendicular reference lines turn ground layout into unambiguous location numbers.</div>`;
  };
  c9s1Mode(0);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🧭</span> Ujjayinī Zero-Longitude Meridian Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">East / West from Ujjayinī (0°): <strong id="c9s2LonVal" class="text-amber-300">0°</strong></span>
      <input type="range" id="c9s2Lon" min="-15" max="15" value="0" oninput="c9s2Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">North Latitude from Equator (0°): <strong id="c9s2LatVal" class="text-cyan-300">23° N</strong></span>
      <input type="range" id="c9s2Lat" min="0" max="35" value="23" oninput="c9s2Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s2Svg" viewBox="0 0 220 165" class="w-56 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s2Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s2Draw = function(){
    const lon = parseInt(document.getElementById('c9s2Lon').value);
    const lat = parseInt(document.getElementById('c9s2Lat').value);
    document.getElementById('c9s2LonVal').textContent = lon===0 ? '0° (On Ujjayinī Meridian)' : (lon>0 ? `${lon}° East` : `${Math.abs(lon)}° West`);
    document.getElementById('c9s2LatVal').textContent = `${lat}° North`;
    const cx = 110 + lon * 5;
    const cy = 140 - lat * 3.4;
    let svg = '';
    svg += `<line x1="20" y1="140" x2="200" y2="140" stroke="#34d399" stroke-width="2"/>`;
    svg += `<line x1="110" y1="12" x2="110" y2="152" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2"/>`;
    for(let x=35; x<=185; x+=25){ svg += `<line x1="${x}" y1="18" x2="${x}" y2="140" stroke="#1e293b" stroke-width="1"/>`; }
    for(let y=21; y<=140; y+=17){ svg += `<line x1="20" y1="${y}" x2="200" y2="${y}" stroke="#1e293b" stroke-width="1"/>`; }
    svg += `<circle cx="110" cy="61.8" r="4" fill="#fbbf24"/><text x="115" y="59" fill="#fbbf24" font-size="8">Ujjayinī (0°, 23°N)</text>`;
    svg += `<line x1="110" y1="${cy}" x2="${cx}" y2="${cy}" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="3 2"/>`;
    svg += `<line x1="${cx}" y1="140" x2="${cx}" y2="${cy}" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 2"/>`;
    svg += `<circle cx="${cx}" cy="${cy}" r="5" fill="#22d3ee" stroke="#fff" stroke-width="1.2"/>`;
    svg += `<text x="114" y="152" fill="#34d399" font-size="8" text-anchor="middle">Equator (0° Lat) &amp; Ujjayinī Zero Meridian</text>`;
    document.getElementById('c9s2Svg').innerHTML = svg;
    const dir = lon===0 ? 'exactly on the Ujjayinī Prime Meridian' : (lon>0 ? `${lon}° East of Ujjayinī` : `${Math.abs(lon)}° West of Ujjayinī`);
    document.getElementById('c9s2Out').innerHTML = `<div class="font-bold text-amber-300">Astronomical Position Pair: (${lon}°, ${lat}° N)</div><p>Measured <strong>${dir}</strong> and <strong>${lat}° North</strong> of the Equator.</p><p class="text-[11px] text-cyan-300">Just like modern Origin (0,0), Ujjayinī locked down a universal 0° longitudinal baseline for ancient Indian astronomers.</p>`;
  };
  c9s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌍</span> Global Mathematical Pioneers Timeline
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s3Pick(0)" id="c9s3b0" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-semibold">Hipparchus</button>
    <button type="button" onclick="c9s3Pick(1)" id="c9s3b1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Ptolemy</button>
    <button type="button" onclick="c9s3Pick(2)" id="c9s3b2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Āryabhaṭa</button>
    <button type="button" onclick="c9s3Pick(3)" id="c9s3b3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Al-Bīrūnī</button>
    <button type="button" onclick="c9s3Pick(4)" id="c9s3b4" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Omar Khayyām</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s3Svg" viewBox="0 0 210 155" class="w-52 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s3Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const scholars = [
    ['Hipparchus (c. 190–120 BCE)', 'Celestial & Terrestrial Grids', 'Pioneered cataloging stars and Earth regions using intersecting angular grids of latitude and longitude.', '★ Grid: (λ, φ)'],
    ['Ptolemy (c. 100–170 CE)', 'Geographia Gridded World Atlas', 'Indexed ~8,000 cities with numerical latitude and longitude pairs across conic and spherical projections.', 'Map Table (lon, lat)'],
    ['Āryabhaṭa (476–550 CE)', 'Celestial Coordinates & Sine Tables', 'Computed planetary coordinates, Earth rotation, and ardha-jyā (sine) projections in Āryabhaṭīya (499 CE).', 'sin θ & Celestial Arcs'],
    ['Al-Bīrūnī (973–1048 CE)', 'Geodesy & City Coordinate Triangulation', 'Refined city coordinates across Ghazni–India and calculated Earth’s radius trigonometrically using mountain angles.', 'R ≈ 6,339 km'],
    ['Omar Khayyām (1048–1131 CE)', 'Geometric Solutions via Intersecting Curves', 'Solved cubic algebraic equations geometrically by intersecting parabolas and circles along orthogonal axes.', 'y = x² ∩ Circle']
  ];
  window.c9s3Pick = function(idx){
    [0,1,2,3,4].forEach(i => {
      const b = document.getElementById('c9s3b'+i);
      if(b) b.className = i===idx ? 'px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const svg = document.getElementById('c9s3Svg');
    let d = '';
    if(idx<=1){
      d = `<circle cx="105" cy="78" r="56" fill="none" stroke="#334155" stroke-width="1.5"/>` +
          `<ellipse cx="105" cy="78" rx="56" ry="18" fill="none" stroke="#22d3ee" stroke-width="1.4"/>` +
          `<ellipse cx="105" cy="78" rx="22" ry="56" fill="none" stroke="#34d399" stroke-width="1.4"/>` +
          `<circle cx="123" cy="64" r="4" fill="#fbbf24"/><text x="105" y="147" fill="#34d399" font-size="8.5" text-anchor="middle">${scholars[idx][3]}</text>`;
    } else if(idx===2 || idx===3){
      d = `<circle cx="105" cy="82" r="52" fill="#0f172a" stroke="#22d3ee" stroke-width="1.8"/>` +
          `<line x1="105" y1="82" x2="145" y2="50" stroke="#fbbf24" stroke-width="2"/>` +
          `<line x1="145" y1="50" x2="145" y2="82" stroke="#34d399" stroke-width="2"/>` +
          `<line x1="53" y1="82" x2="157" y2="82" stroke="#475569" stroke-width="1.2"/>` +
          `<text x="105" y="147" fill="#fbbf24" font-size="8.5" text-anchor="middle">${scholars[idx][3]}</text>`;
    } else {
      d = `<line x1="25" y1="120" x2="185" y2="120" stroke="#475569" stroke-width="1.5"/>` +
          `<line x1="65" y1="20" x2="65" y2="135" stroke="#475569" stroke-width="1.5"/>` +
          `<path d="M 35 35 Q 65 160 145 35" fill="none" stroke="#22d3ee" stroke-width="2"/>` +
          `<circle cx="115" cy="90" r="32" fill="none" stroke="#fbbf24" stroke-width="2"/>` +
          `<circle cx="131" cy="62" r="4.5" fill="#34d399"/><text x="105" y="147" fill="#34d399" font-size="8.5" text-anchor="middle">${scholars[idx][3]}</text>`;
    }
    svg.innerHTML = d;
    document.getElementById('c9s3Out').innerHTML = `<div class="font-bold text-emerald-300">${scholars[idx][0]}</div><div class="text-[11px] font-semibold text-cyan-300">${scholars[idx][1]}</div><p class="leading-relaxed">${scholars[idx][2]}</p>`;
  };
  c9s3Pick(0);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>➗</span> Brahmagupta Zero &amp; Negatives → Descartes 4-Quadrant Plane
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s4Stage(0)" id="c9s4b0" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">1. Positive-Only View</button>
    <button type="button" onclick="c9s4Stage(1)" id="c9s4b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2. Brahmagupta Zero &amp; Negatives</button>
    <button type="button" onclick="c9s4Stage(2)" id="c9s4b2" class="px-2.5 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40 font-semibold">3. Fermat &amp; Descartes Plane</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s4Svg" viewBox="0 0 210 160" class="w-52 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s4Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const txt = [
    ['Before Zero & Negative Arithmetic', 'Ancient lengths were strictly positive magnitudes (> 0), trapping geometric coordinates inside a single upper-right positive corner.'],
    ['Brahmagupta (628 CE, Brāhmasphuṭasiddhānta)', 'Defined zero as a full number and codified operations with negative numbers ("debts"), unlocking negative left and downward directions on axes!'],
    ['Pierre de Fermat & René Descartes (17th Century)', 'Combined two perpendicular signed axes meeting at Origin (0,0), encoding all 4 quadrants and turning curves into algebraic equations!']
  ];
  window.c9s4Stage = function(s){
    [0,1,2].forEach(i => {
      const b = document.getElementById('c9s4b'+i);
      if(b) b.className = i===s ? 'px-2.5 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    let g = '';
    if(s===0){
      g += `<rect x="105" y="15" width="85" height="65" fill="#0891b2" fill-opacity="0.22" stroke="#22d3ee"/>`;
      g += `<line x1="105" y1="80" x2="195" y2="80" stroke="#22d3ee" stroke-width="2"/><line x1="105" y1="80" x2="105" y2="10" stroke="#22d3ee" stroke-width="2"/>`;
      g += `<text x="148" y="48" fill="#22d3ee" font-size="9" text-anchor="middle" font-weight="bold">Only (+, +)</text>`;
    } else if(s===1){
      g += `<line x1="20" y1="80" x2="190" y2="80" stroke="#fbbf24" stroke-width="2"/>`;
      g += `<line x1="105" y1="15" x2="105" y2="145" stroke="#fbbf24" stroke-width="2"/>`;
      g += `<circle cx="105" cy="80" r="5" fill="#fbbf24"/><text x="112" y="75" fill="#fbbf24" font-size="8.5" font-weight="bold">Zero 0</text>`;
      g += `<text x="35" y="73" fill="#fb7185" font-size="8.5">-x (Negatives)</text><text x="110" y="135" fill="#fb7185" font-size="8.5">-y (Negatives)</text>`;
    } else {
      g += `<rect x="105" y="15" width="85" height="65" fill="#0891b2" fill-opacity="0.18"/>`;
      g += `<rect x="20" y="15" width="85" height="65" fill="#d97706" fill-opacity="0.18"/>`;
      g += `<rect x="20" y="80" width="85" height="65" fill="#e11d48" fill-opacity="0.18"/>`;
      g += `<rect x="105" y="80" width="85" height="65" fill="#059669" fill-opacity="0.18"/>`;
      g += `<line x1="20" y1="80" x2="190" y2="80" stroke="#e2e8f0" stroke-width="1.8"/><line x1="105" y1="15" x2="105" y2="145" stroke="#e2e8f0" stroke-width="1.8"/>`;
      g += `<text x="147" y="48" fill="#22d3ee" font-size="9" text-anchor="middle">QI (+,+)</text><text x="62" y="48" fill="#fbbf24" font-size="9" text-anchor="middle">QII (-,+)</text>`;
      g += `<text x="62" y="118" fill="#fb7185" font-size="9" text-anchor="middle">QIII (-,-)</text><text x="147" y="118" fill="#34d399" font-size="9" text-anchor="middle">QIV (+,-)</text>`;
    }
    document.getElementById('c9s4Svg').innerHTML = g;
    document.getElementById('c9s4Out').innerHTML = `<div class="font-bold text-purple-300">${txt[s][0]}</div><p class="leading-relaxed">${txt[s][1]}</p>`;
  };
  c9s4Stage(2);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧶</span> Tactile Pin-and-Thread Home Map (Scale 1 cm : 1 foot)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s5Pick('bedroom')" id="c9s5_bedroom" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">Bedroom Pin</button>
    <button type="button" onclick="c9s5Pick('bathroom')" id="c9s5_bathroom" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Bathroom Pin</button>
    <button type="button" onclick="c9s5Pick('wardrobe')" id="c9s5_wardrobe" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Wardrobe Pin</button>
    <button type="button" onclick="c9s5Pick('door')" id="c9s5_door" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Main Door Pin</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s5Svg" viewBox="0 0 240 165" class="w-60 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s5Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const items = {
    bedroom: { name:'Bedroom Centre', x:6, y:9, dims:'10 cm × 8 cm board → 10 ft × 8 ft real room' },
    bathroom: { name:'Bathroom Corner', x:14, y:10, dims:'6 cm × 5 cm board → 6 ft × 5 ft real room' },
    wardrobe: { name:'Wardrobe Edge', x:3, y:11, dims:'4 cm × 2 cm board → 4 ft × 2 ft real fixture' },
    door: { name:'Main Entrance Door', x:10, y:0, dims:'On bottom wall (y = 0 cm), 10 ft east from corner (0,0)' }
  };
  window.c9s5Pick = function(key){
    ['bedroom','bathroom','wardrobe','door'].forEach(k => {
      const b = document.getElementById('c9s5_'+k);
      if(b) b.className = k===key ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const it = items[key];
    const px = 25 + it.x * 11;
    const py = 145 - it.y * 10;
    let svg = '';
    for(let i=0;i<=18;i+=2){ svg += `<line x1="${25+i*11}" y1="15" x2="${25+i*11}" y2="145" stroke="#1e293b" stroke-width="1"/>`; }
    for(let j=0;j<=12;j+=2){ svg += `<line x1="25" y1="${145-j*10}" x2="223" y2="${145-j*10}" stroke="#1e293b" stroke-width="1"/>`; }
    svg += `<rect x="25" y="25" width="110" height="80" fill="#0891b2" fill-opacity="0.18" stroke="#38bdf8" stroke-width="1.5"/>`;
    svg += `<text x="72" y="65" fill="#7dd3fc" font-size="8">Bedroom</text>`;
    svg += `<rect x="135" y="25" width="66" height="50" fill="#059669" fill-opacity="0.18" stroke="#34d399" stroke-width="1.5"/>`;
    svg += `<text x="147" y="53" fill="#6ee7b7" font-size="8">Bath</text>`;
    svg += `<rect x="36" y="25" width="44" height="20" fill="#d97706" fill-opacity="0.28" stroke="#fbbf24" stroke-width="1.2"/>`;
    svg += `<line x1="25" y1="145" x2="225" y2="145" stroke="#94a3b8" stroke-width="1.5"/>`;
    svg += `<line x1="25" y1="15" x2="25" y2="145" stroke="#94a3b8" stroke-width="1.5"/>`;
    svg += `<line x1="25" y1="${py}" x2="${px}" y2="${py}" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2"/>`;
    svg += `<line x1="${px}" y1="145" x2="${px}" y2="${py}" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2"/>`;
    svg += `<circle cx="${px}" cy="${py}" r="5.5" fill="#fbbf24" stroke="#fff" stroke-width="1.5"/>`;
    svg += `<text x="125" y="158" fill="#94a3b8" font-size="8" text-anchor="middle">Tactile Thread Grid: 1 cm board = 1 foot room</text>`;
    document.getElementById('c9s5Svg').innerHTML = svg;
    document.getElementById('c9s5Out').innerHTML = `<div class="font-bold text-cyan-300">${it.name} → Pin (${it.x} cm, ${it.y} cm)</div><p>Actual Walk Distance from Origin (0,0): <strong>${it.x} feet east, ${it.y} feet north</strong>.</p><p class="text-amber-300">${it.dims}</p>`;
  };
  c9s5Pick('bedroom');
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📍</span> Interactive (x, y) Ordered Pair &amp; Origin Plotter
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Abscissa (x): <strong id="c9s6XVal" class="text-cyan-300">3</strong></span>
      <input type="range" id="c9s6X" min="-5" max="5" value="3" oninput="c9s6Plot()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Ordinate (y): <strong id="c9s6YVal" class="text-amber-300">4</strong></span>
      <input type="range" id="c9s6Y" min="-5" max="5" value="4" oninput="c9s6Plot()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s6Svg" viewBox="0 0 200 200" class="w-48 h-48 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s6Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s6Plot = function(){
    const x = parseInt(document.getElementById('c9s6X').value);
    const y = parseInt(document.getElementById('c9s6Y').value);
    document.getElementById('c9s6XVal').textContent = x;
    document.getElementById('c9s6YVal').textContent = y;
    const cx = 100 + x * 15, cy = 100 - y * 15;
    let s = '';
    for(let k=-5; k<=5; k++){
      const p = 100 + k * 15;
      s += `<line x1="${p}" y1="15" x2="${p}" y2="185" stroke="#1e293b" stroke-width="1"/>`;
      s += `<line x1="15" y1="${p}" x2="185" y2="${p}" stroke="#1e293b" stroke-width="1"/>`;
    }
    s += `<line x1="12" y1="100" x2="188" y2="100" stroke="#94a3b8" stroke-width="1.8"/>`;
    s += `<line x1="100" y1="12" x2="100" y2="188" stroke="#94a3b8" stroke-width="1.8"/>`;
    s += `<line x1="100" y1="100" x2="${cx}" y2="100" stroke="#22d3ee" stroke-width="2.5"/>`;
    s += `<line x1="${cx}" y1="100" x2="${cx}" y2="${cy}" stroke="#fbbf24" stroke-width="2.5"/>`;
    s += `<circle cx="100" cy="100" r="3.5" fill="#fff"/><text x="104" y="111" fill="#cbd5e1" font-size="8">O(0,0)</text>`;
    s += `<circle cx="${cx}" cy="${cy}" r="5" fill="#34d399" stroke="#fff" stroke-width="1.2"/>`;
    s += `<text x="${cx + (x>=0?6:-38)}" y="${cy - 6}" fill="#34d399" font-size="9" font-weight="bold">P(${x}, ${y})</text>`;
    document.getElementById('c9s6Svg').innerHTML = s;
    const hdir = x===0?'0 units horizontally':(x>0?`${x} units right along +x`:`${Math.abs(x)} units left along -x`);
    const vdir = y===0?'0 units vertically':(y>0?`${y} units up parallel to +y`:`${Math.abs(y)} units down parallel to -y`);
    document.getElementById('c9s6Out').innerHTML = `<div class="font-bold text-emerald-300">Ordered Pair P(${x}, ${y})</div><p>Step 1 (x = ${x}): Move <strong>${hdir}</strong>.</p><p>Step 2 (y = ${y}): Move <strong>${vdir}</strong>.</p><p class="text-[11px] text-amber-300">Compare with swapped (${y}, ${x}): ${x===y?'Identical point!':'Different location because order matters!'}</p>`;
  };
  c9s6Plot();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🧭</span> Four-Quadrant Sign Classifier &amp; Boundary Tester
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s7Test(3,4)" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">(3, 4) → QI</button>
    <button type="button" onclick="c9s7Test(-4,3)" class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40">(-4, 3) → QII</button>
    <button type="button" onclick="c9s7Test(-3,-4)" class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">(-3, -4) → QIII</button>
    <button type="button" onclick="c9s7Test(4,-2)" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">(4, -2) → QIV</button>
    <button type="button" onclick="c9s7Test(0,-4)" class="px-2 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40">(0, -4) → y-axis</button>
    <button type="button" onclick="c9s7Test(5,0)" class="px-2 py-1 rounded bg-slate-700 text-slate-200 border border-slate-600">(5, 0) → x-axis</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s7Svg" viewBox="0 0 200 200" class="w-48 h-48 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s7Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s7Test = function(x, y){
    const cx = 100 + x * 15, cy = 100 - y * 15;
    let loc = '';
    if(x>0 && y>0) loc = 'Quadrant I (+, +)';
    else if(x<0 && y>0) loc = 'Quadrant II (-, +)';
    else if(x<0 && y<0) loc = 'Quadrant III (-, -)';
    else if(x>0 && y<0) loc = 'Quadrant IV (+, -)';
    else if(x===0 && y===0) loc = 'Origin (0, 0)';
    else if(y===0) loc = 'Directly ON the x-axis (not in any quadrant!)';
    else loc = 'Directly ON the y-axis (not in any quadrant!)';
    let s = '';
    s += `<rect x="100" y="15" width="85" height="85" fill="#0891b2" fill-opacity="0.14"/>`;
    s += `<rect x="15" y="15" width="85" height="85" fill="#d97706" fill-opacity="0.14"/>`;
    s += `<rect x="15" y="100" width="85" height="85" fill="#e11d48" fill-opacity="0.14"/>`;
    s += `<rect x="100" y="100" width="85" height="85" fill="#059669" fill-opacity="0.14"/>`;
    s += `<line x1="15" y1="100" x2="185" y2="100" stroke="#e2e8f0" stroke-width="1.6"/>`;
    s += `<line x1="100" y1="15" x2="100" y2="185" stroke="#e2e8f0" stroke-width="1.6"/>`;
    s += `<text x="142" y="34" fill="#22d3ee" font-size="8.5" text-anchor="middle">QI (+,+)</text>`;
    s += `<text x="58" y="34" fill="#fbbf24" font-size="8.5" text-anchor="middle">QII (-,+)</text>`;
    s += `<text x="58" y="176" fill="#fb7185" font-size="8.5" text-anchor="middle">QIII (-,-)</text>`;
    s += `<text x="142" y="176" fill="#34d399" font-size="8.5" text-anchor="middle">QIV (+,-)</text>`;
    s += `<circle cx="${cx}" cy="${cy}" r="5.5" fill="#fff" stroke="#22d3ee" stroke-width="2"/>`;
    s += `<text x="${cx}" y="${cy-9}" fill="#fff" font-size="9" text-anchor="middle" font-weight="bold">(${x}, ${y})</text>`;
    document.getElementById('c9s7Svg').innerHTML = s;
    document.getElementById('c9s7Out').innerHTML = `<div class="font-bold text-amber-300">Point (${x}, ${y}) → ${loc}</div><p>Sign Check: x = ${x>0?'positive (+)':(x<0?'negative (-)':'zero (0)')}, y = ${y>0?'positive (+)':(y<0?'negative (-)':'zero (0)')}.</p><p class="text-[11px] text-cyan-300">Quadrants rotate counter-clockwise starting from top-right QI (+,+).</p>`;
  };
  c9s7Test(-4, 3);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📏</span> Perpendicular Axis Distance &amp; (x, y) vs (y, x) Checker
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">x-coordinate: <strong id="c9s8XVal" class="text-cyan-300">2</strong></span>
      <input type="range" id="c9s8X" min="-5" max="5" value="2" oninput="c9s8Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">y-coordinate: <strong id="c9s8YVal" class="text-amber-300">4</strong></span>
      <input type="range" id="c9s8Y" min="-5" max="5" value="4" oninput="c9s8Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s8Svg" viewBox="0 0 200 200" class="w-48 h-48 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s8Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s8Draw = function(){
    const x = parseInt(document.getElementById('c9s8X').value);
    const y = parseInt(document.getElementById('c9s8Y').value);
    document.getElementById('c9s8XVal').textContent = x;
    document.getElementById('c9s8YVal').textContent = y;
    const px = 100 + x * 15, py = 100 - y * 15;
    const qx = 100 + y * 15, qy = 100 - x * 15;
    let s = '';
    s += `<line x1="15" y1="185" x2="185" y2="15" stroke="#334155" stroke-width="1.2" stroke-dasharray="4 3"/>`;
    s += `<line x1="15" y1="100" x2="185" y2="100" stroke="#94a3b8" stroke-width="1.6"/>`;
    s += `<line x1="100" y1="15" x2="100" y2="185" stroke="#94a3b8" stroke-width="1.6"/>`;
    s += `<line x1="100" y1="${py}" x2="${px}" y2="${py}" stroke="#22d3ee" stroke-width="2" stroke-dasharray="3 2"/>`;
    s += `<line x1="${px}" y1="100" x2="${px}" y2="${py}" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3 2"/>`;
    if(x!==y){
      s += `<circle cx="${qx}" cy="${qy}" r="4.5" fill="#fb7185"/><text x="${qx+6}" y="${qy+3}" fill="#fb7185" font-size="8.5">Q(${y},${x})</text>`;
    }
    s += `<circle cx="${px}" cy="${py}" r="5" fill="#34d399" stroke="#fff" stroke-width="1.2"/><text x="${px+6}" y="${py-5}" fill="#34d399" font-size="8.5" font-weight="bold">P(${x},${y})</text>`;
    document.getElementById('c9s8Svg').innerHTML = s;
    const eqMsg = x===y ? `<span class="text-emerald-300 font-bold">x = y = ${x} → P(${x},${y}) = Q(${y},${x}) on diagonal y = x!</span>` : `<span class="text-rose-300 font-bold">x ≠ y → P(${x},${y}) ≠ Q(${y},${x}) (different points!)</span>`;
    document.getElementById('c9s8Out').innerHTML = `<div class="font-bold text-cyan-300">Distances from Axes for P(${x}, ${y})</div><p>Perpendicular distance from <strong>y-axis</strong> = |x| = <strong>${Math.abs(x)} units</strong></p><p>Perpendicular distance from <strong>x-axis</strong> = |y| = <strong>${Math.abs(y)} units</strong></p><p>${eqMsg}</p>`;
  };
  c9s8Draw();
})();
</script>
"""
}

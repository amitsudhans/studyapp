#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Matter Hierarchy: All Roads Lead to Atoms</span>
    <div class="flex gap-2">
      <button onclick="setC8S1('nonliving')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Non-Living Matter</button>
      <button onclick="setC8S1('living')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Living Organisms</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c8s1_nl">
      <rect x="45" y="75" width="95" height="55" rx="8" fill="#b45309" stroke="#fde68a"/><text x="92" y="107" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">House</text>
      <line x1="145" y1="102" x2="175" y2="102" stroke="#94a3b8" stroke-width="3"/>
      <rect x="180" y="75" width="95" height="55" rx="8" fill="#d97706" stroke="#fde68a"/><text x="227" y="107" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">Bricks</text>
      <line x1="280" y1="102" x2="310" y2="102" stroke="#94a3b8" stroke-width="3"/>
      <rect x="315" y="75" width="95" height="55" rx="8" fill="#0284c7" stroke="#bae6fd"/><text x="362" y="107" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">Silicates</text>
      <line x1="415" y1="102" x2="445" y2="102" stroke="#94a3b8" stroke-width="3"/>
      <circle cx="495" cy="102" r="38" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="495" cy="102" r="8" fill="#fbbf24"/>
      <text x="495" y="156" text-anchor="middle" fill="#7dd3fc" font-size="12" font-weight="bold">ATOMS</text>
      <text x="300" y="205" text-anchor="middle" fill="#cbd5e1" font-size="12">Non-living structures break down from macroscopic bricks to silicate molecules and atoms</text>
    </g>
    <g id="c8s1_liv" style="display:none">
      <rect x="35" y="75" width="85" height="55" rx="8" fill="#059669" stroke="#a7f3d0"/><text x="77" y="107" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Organs</text>
      <line x1="122" y1="102" x2="140" y2="102" stroke="#94a3b8" stroke-width="2"/>
      <rect x="142" y="75" width="85" height="55" rx="8" fill="#0d9488" stroke="#99f6e4"/><text x="184" y="107" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Tissues</text>
      <line x1="229" y1="102" x2="247" y2="102" stroke="#94a3b8" stroke-width="2"/>
      <rect x="249" y="75" width="85" height="55" rx="8" fill="#0284c7" stroke="#bae6fd"/><text x="291" y="107" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Cells</text>
      <line x1="336" y1="102" x2="354" y2="102" stroke="#94a3b8" stroke-width="2"/>
      <rect x="356" y="75" width="85" height="55" rx="8" fill="#6366f1" stroke="#c7d2fe"/><text x="398" y="107" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Proteins</text>
      <line x1="443" y1="102" x2="462" y2="102" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="505" cy="102" r="36" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="2"/>
      <circle cx="505" cy="102" r="8" fill="#fbbf24"/>
      <text x="505" y="156" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">ATOMS</text>
      <text x="300" y="205" text-anchor="middle" fill="#cbd5e1" font-size="12">Living organisms also reduce to proteins and fundamental atoms!</text>
    </g>
  </svg>
</div>
<script>
window.setC8S1 = function(m){
  document.getElementById('c8s1_nl').style.display = (m==='nonliving'?'block':'none');
  document.getElementById('c8s1_liv').style.display = (m==='living'?'block':'none');
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">Ancient &amp; 1808 Atomic Roots</span>
    <div class="flex gap-1.5">
      <button onclick="setC8S2('kanada')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Acharya Kanada</button>
      <button onclick="setC8S2('greek')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Democritus</button>
      <button onclick="setC8S2('dalton')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Dalton (1808)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="150" cy="120" r="20" fill="#fbbf24"/>
    <circle cx="290" cy="120" r="20" fill="#fbbf24"/><circle cx="330" cy="120" r="20" fill="#38bdf8"/>
    <circle cx="450" cy="108" r="20" fill="#fbbf24"/><circle cx="490" cy="108" r="20" fill="#38bdf8"/><circle cx="470" cy="142" r="20" fill="#34d399"/>
    <text x="150" y="165" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">Parmanu (Single)</text>
    <text x="310" y="165" text-anchor="middle" fill="#7dd3fc" font-size="12" font-weight="bold">Dyad (Pair)</text>
    <text x="470" y="182" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Triad (Three)</text>
    <text id="c8s2_title" x="300" y="42" text-anchor="middle" fill="#fbbf24" font-size="16" font-weight="bold">Acharya Kanada (Vaisesika Sutras): Dravya &rarr; Parmanu</text>
    <text id="c8s2_sub" x="300" y="216" text-anchor="middle" fill="#cbd5e1" font-size="12">Proposed indivisible parmanus combine into dyads and triads to form matter</text>
  </svg>
</div>
<script>
window.setC8S2 = function(k){
  const t = document.getElementById('c8s2_title');
  const s = document.getElementById('c8s2_sub');
  if(k==='kanada'){
    t.textContent = 'Acharya Kanada (Vaisesika Sutras): Dravya -> Parmanu';
    s.textContent = 'Proposed indivisible parmanus combine into dyads and triads to form matter';
  } else if(k==='greek'){
    t.textContent = 'Leucippus & Democritus (5th Century BCE): Atomos';
    s.textContent = 'Coined the Greek term atomos meaning uncuttable or indivisible';
  } else {
    t.textContent = 'John Dalton (1808): Scientific Atomic Theory';
    s.textContent = 'All matter consists of indivisible atoms combining in simple whole-number ratios';
  }
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">J. J. Thomson (1897) Cathode Ray Tube</span>
    <div class="flex gap-2">
      <button onclick="setC8S3(false)" class="px-2.5 py-1 rounded bg-slate-700 text-xs text-slate-200 border border-slate-500">E-Field Off</button>
      <button onclick="setC8S3(true)" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Turn On + Plate</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="60" y="65" width="480" height="110" rx="22" fill="#0f172a" stroke="#64748b" stroke-width="3"/>
    <rect x="85" y="100" width="14" height="40" fill="#38bdf8"/>
    <text x="92" y="156" text-anchor="middle" fill="#7dd3fc" font-size="11">Cathode (-)</text>
    <rect x="240" y="55" width="130" height="12" fill="#f43f5e"/>
    <text x="305" y="48" text-anchor="middle" fill="#fda4af" font-size="11">+ Positive Plate</text>
    <rect x="240" y="173" width="130" height="12" fill="#38bdf8"/>
    <text x="305" y="198" text-anchor="middle" fill="#7dd3fc" font-size="11">- Negative Plate</text>
    <path id="c8s3_beam" d="M 100 120 L 520 120" fill="none" stroke="#34d399" stroke-width="4" stroke-dasharray="7,4"/>
    <text id="c8s3_lbl" x="300" y="222" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Electron (e-): Charge = -1.602 x 10^-19 C | Relative Charge = -1</text>
  </svg>
</div>
<script>
window.setC8S3 = function(on){
  const b = document.getElementById('c8s3_beam');
  const l = document.getElementById('c8s3_lbl');
  if(on){
    b.setAttribute('d','M 100 120 L 240 120 Q 350 116 515 80');
    l.textContent = 'Deflected toward + Plate! Proves cathode rays are negative electrons (all atoms)';
  } else {
    b.setAttribute('d','M 100 120 L 520 120');
    l.textContent = 'Electron (e-): Charge = -1.602 x 10^-19 C | Relative Charge = -1';
  }
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Thomson's Watermelon Model (Neutrality Balance)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Electrons (Seeds): <b id="c8s4_e" class="text-cyan-300">6</b> / +6 Pulp</label>
      <input type="range" min="4" max="8" step="1" value="6" id="c8s4_sl" oninput="updC8S4()" class="w-24 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="230" cy="120" r="82" fill="#e11d48" stroke="#15803d" stroke-width="8"/>
    <g id="c8s4_seeds">
      <circle cx="200" cy="95" r="7" fill="#0f172a"/><circle cx="255" cy="90" r="7" fill="#0f172a"/>
      <circle cx="185" cy="130" r="7" fill="#0f172a"/><circle cx="230" cy="125" r="7" fill="#0f172a"/>
      <circle cx="270" cy="135" r="7" fill="#0f172a"/><circle cx="220" cy="160" r="7" fill="#0f172a"/>
    </g>
    <text x="445" y="75" text-anchor="middle" fill="#fda4af" font-size="14" font-weight="bold">Red Pulp = +6 Charge</text>
    <text id="c8s4_neg" x="445" y="105" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Black Seeds = -6 Charge</text>
    <text id="c8s4_net" x="445" y="145" text-anchor="middle" fill="#6ee7b7" font-size="17" font-weight="bold">Net Charge = 0 (Neutral)</text>
  </svg>
</div>
<script>
window.updC8S4 = function(){
  const n = parseInt(document.getElementById('c8s4_sl').value,10);
  document.getElementById('c8s4_e').textContent = n;
  document.getElementById('c8s4_neg').textContent = 'Black Seeds = -' + n + ' Charge';
  const net = 6 - n;
  const el = document.getElementById('c8s4_net');
  el.textContent = 'Net Charge = ' + (net>0?'+'+net:net) + (net===0?' (Neutral Atom)':' (Charged!)');
  el.setAttribute('fill', net===0 ? '#6ee7b7' : '#fbbf24');
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">1911 Gold Foil Experiment (Geiger &amp; Marsden)</span>
    <div class="flex gap-1.5">
      <button onclick="setC8S5('pass')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Most Pass Straight</button>
      <button onclick="setC8S5('defl')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Large Deflection</button>
      <button onclick="setC8S5('back')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">1 in 20,000 Rebound</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="330" y="35" width="8" height="170" fill="#fbbf24"/>
    <circle cx="334" cy="120" r="10" fill="#ef4444" stroke="#fecaca" stroke-width="2"/>
    <text x="334" y="220" text-anchor="middle" fill="#fde047" font-size="11">Gold Foil (~1000 atoms thick)</text>
    <path id="c8s5_ray" d="M 70 80 L 530 80" fill="none" stroke="#34d399" stroke-width="4" stroke-dasharray="6,3"/>
    <text id="c8s5_txt" x="300" y="30" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Most &alpha;-particles pass straight through &rArr; Atom is mostly empty space!</text>
  </svg>
</div>
<script>
window.setC8S5 = function(mode){
  const r = document.getElementById('c8s5_ray');
  const t = document.getElementById('c8s5_txt');
  if(mode==='pass'){
    r.setAttribute('d','M 70 80 L 530 80'); r.setAttribute('stroke','#34d399');
    t.textContent = 'Most alpha-particles pass straight through -> Atom is mostly empty space!';
  } else if(mode==='defl'){
    r.setAttribute('d','M 70 108 L 325 108 L 460 40'); r.setAttribute('stroke','#fbbf24');
    t.textContent = 'Small fraction deflect at large angles -> Positive charge is concentrated!';
  } else {
    r.setAttribute('d','M 70 120 L 320 120 L 85 130'); r.setAttribute('stroke','#f43f5e');
    t.textContent = '~1 in 20,000 bounce back sharply -> Tiny, dense positive Nucleus!';
  }
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Rutherford Planetary Model &amp; Stability Flaw</span>
    <div class="flex gap-2">
      <button onclick="setC8S6('scale')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Nucleus vs Atom Scale</button>
      <button onclick="setC8S6('flaw')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Classical EM Spiral</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c8s6_scale">
      <circle cx="300" cy="115" r="78" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,4"/>
      <circle cx="300" cy="115" r="5" fill="#ef4444"/>
      <circle cx="378" cy="115" r="6" fill="#34d399"/>
      <text x="300" y="25" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Atom (~10^-10 m) is 100,000x wider than Nucleus (~10^-15 m)</text>
      <text x="300" y="218" text-anchor="middle" fill="#cbd5e1" font-size="12">1,000,000 (10^6) stacked atoms = 0.1 mm paper | Nucleus holds protons (+1)</text>
    </g>
    <g id="c8s6_flaw" style="display:none">
      <circle cx="300" cy="115" r="8" fill="#ef4444"/>
      <path d="M 380 115 A 80 80 0 1 1 300 35 A 60 60 0 1 1 240 115 A 40 40 0 1 1 300 75 A 20 20 0 1 1 312 115" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="5,3"/>
      <text x="300" y="25" text-anchor="middle" fill="#fda4af" font-size="14" font-weight="bold">Limitation: Accelerating e- radiates energy &amp; spirals into Nucleus!</text>
      <text x="300" y="218" text-anchor="middle" fill="#cbd5e1" font-size="12">Classical electromagnetism predicts collapse, yet real atoms are stable!</text>
    </g>
  </svg>
</div>
<script>
window.setC8S6 = function(m){
  document.getElementById('c8s6_scale').style.display = (m==='scale'?'block':'none');
  document.getElementById('c8s6_flaw').style.display = (m==='flaw'?'block':'none');
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">Niels Bohr (1913) Stationary Orbits (K, L, M, N)</span>
    <div class="flex gap-1.5">
      <button onclick="setC8S7(1)" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">K (n=1)</button>
      <button onclick="setC8S7(2)" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">L (n=2)</button>
      <button onclick="setC8S7(3)" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">M (n=3)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="240" cy="120" r="14" fill="#ef4444"/><text x="240" y="124" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">+</text>
    <circle cx="240" cy="120" r="36" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="240" cy="120" r="62" fill="none" stroke="#34d399" stroke-width="2"/>
    <circle cx="240" cy="120" r="88" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <circle id="c8s7_el" cx="276" cy="120" r="7" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
    <text x="445" y="75" text-anchor="middle" fill="#fde047" font-size="14" font-weight="bold">E_K &lt; E_L &lt; E_M &lt; E_N</text>
    <text id="c8s7_msg" x="445" y="115" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">In K shell (n=1): Zero energy loss!</text>
    <text x="445" y="155" text-anchor="middle" fill="#cbd5e1" font-size="11">Jump out = Absorb | Drop in = Emit light</text>
    <text x="445" y="180" text-anchor="middle" fill="#94a3b8" font-size="10">(Barkla named X-ray lines starting at K)</text>
  </svg>
</div>
<script>
window.setC8S7 = function(n){
  const r = n===1 ? 36 : (n===2 ? 62 : 88);
  const lbl = n===1 ? 'K (n=1, lowest energy)' : (n===2 ? 'L (n=2, higher energy)' : 'M (n=3, highest shown)');
  document.getElementById('c8s7_el').setAttribute('cx', 240 + r);
  document.getElementById('c8s7_msg').textContent = 'Stationary ' + lbl + ': No radiation!';
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">James Chadwick (1932) Neutron &amp; BARC India</span>
    <div class="flex gap-2">
      <button onclick="setC8S8('he')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Helium 4:1 Mass Anomaly</button>
      <button onclick="setC8S8('barc')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">BARC Dhruva &amp; Bhabha</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c8s8_he">
      <circle cx="150" cy="110" r="16" fill="#ef4444"/><text x="150" y="114" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">p+</text>
      <text x="150" y="155" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Hydrogen = 1 u</text>
      <circle cx="400" cy="95" r="16" fill="#ef4444"/><text x="400" y="99" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">p+</text>
      <circle cx="436" cy="95" r="16" fill="#ef4444"/><text x="436" y="99" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">p+</text>
      <circle cx="400" cy="130" r="16" fill="#94a3b8"/><text x="400" y="134" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="bold">n0</text>
      <circle cx="436" cy="130" r="16" fill="#94a3b8"/><text x="436" y="134" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="bold">n0</text>
      <text x="418" y="170" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">Helium = 4 u (2 p+ + 2 n0)</text>
      <text x="300" y="212" text-anchor="middle" fill="#6ee7b7" font-size="12">Table 8.1: e- (-1) | p+ (+1) | n0 (0) &mdash; Neutrons stabilize nuclei via Strong Force</text>
    </g>
    <g id="c8s8_barc" style="display:none">
      <rect x="90" y="55" width="420" height="125" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
      <text x="300" y="95" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">Bhabha Atomic Research Centre (BARC), Mumbai</text>
      <text x="300" y="125" text-anchor="middle" fill="#cbd5e1" font-size="13">Homi Jehangir Bhabha (Father of Indian Nuclear Programme)</text>
      <text x="300" y="155" text-anchor="middle" fill="#fde047" font-size="12">Dhruva Reactor: Peaceful neutron research for medicine, crops &amp; energy</text>
    </g>
  </svg>
</div>
<script>
window.setC8S8 = function(m){
  document.getElementById('c8s8_he').style.display = (m==='he'?'block':'none');
  document.getElementById('c8s8_barc').style.display = (m==='barc'?'block':'none');
};
</script>"""
}

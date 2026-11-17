#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Ionic Bond: Na &rarr; Na&#8314; + e&#8315; &amp; Cl + e&#8315; &rarr; Cl&#8315;</span>
    <div class="flex gap-2">
      <button onclick="setC9S9('xfer')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Electron Transfer</button>
      <button onclick="setC9S9('lat')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">3D Crystal Lattice</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c9s9_xfer">
      <circle cx="165" cy="115" r="38" fill="#0284c7" stroke="#bae6fd" stroke-width="2"/>
      <text x="165" y="112" text-anchor="middle" fill="#fff" font-size="16" font-weight="bold">Na&#8314;</text>
      <text x="165" y="130" text-anchor="middle" fill="#bae6fd" font-size="11">(2, 8)</text>
      <line x1="210" y1="115" x2="375" y2="115" stroke="#fbbf24" stroke-width="3" stroke-dasharray="5,3"/>
      <polygon points="385,115 370,108 370,122" fill="#fbbf24"/>
      <text x="297" y="102" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">1 e&#8315; transferred</text>
      <circle cx="435" cy="115" r="42" fill="#059669" stroke="#a7f3d0" stroke-width="2"/>
      <text x="435" y="112" text-anchor="middle" fill="#fff" font-size="16" font-weight="bold">Cl&#8315;</text>
      <text x="435" y="130" text-anchor="middle" fill="#a7f3d0" font-size="11">(2, 8, 8)</text>
      <text x="300" y="200" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Opposite charges attract electrostatically &rarr; Ionic Bond (NaCl)</text>
    </g>
    <g id="c9s9_lat" style="display:none">
      <circle cx="250" cy="80" r="14" fill="#38bdf8"/><circle cx="300" cy="80" r="18" fill="#34d399"/><circle cx="350" cy="80" r="14" fill="#38bdf8"/>
      <circle cx="250" cy="130" r="18" fill="#34d399"/><circle cx="300" cy="130" r="14" fill="#38bdf8"/><circle cx="350" cy="130" r="18" fill="#34d399"/>
      <text x="300" y="185" text-anchor="middle" fill="#fde047" font-size="14" font-weight="bold">3D Crystal Lattice: Each Na&#8314; surrounded by 6 Cl&#8315; ions (and vice versa)</text>
    </g>
  </svg>
</div>
<script>
window.setC9S9 = function(m){
  document.getElementById('c9s9_xfer').style.display = (m==='xfer'?'block':'none');
  document.getElementById('c9s9_lat').style.display = (m==='lat'?'block':'none');
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Tables 9.1(a) &amp; 9.1(b): Ion Reference</span>
    <div class="flex gap-1.5">
      <button onclick="setC9S10('mono')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">9.1(a) Monoatomic</button>
      <button onclick="setC9S10('poly')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">9.1(b) Polyatomic</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c9s10_mono">
      <text x="300" y="45" text-anchor="middle" fill="#fbbf24" font-size="16" font-weight="bold">Table 9.1(a): Monoatomic Cations &amp; Anions (-ide)</text>
      <text x="300" y="88" text-anchor="middle" fill="#7dd3fc" font-size="14">Cations (+): Na&#8314;, K&#8314;, Cu&#8314; (1) | Ca&sup2;&#8314;, Fe&sup2;&#8314;, Cu&sup2;&#8314; (2) | Al&sup3;&#8314;, Fe&sup3;&#8314; (3)</text>
      <text x="300" y="130" text-anchor="middle" fill="#6ee7b7" font-size="14">Anions (-): F&#8315; (fluoride), Cl&#8315; (chloride) | O&sup2;&#8315; (oxide), S&sup2;&#8315; (sulfide)</text>
      <text x="300" y="178" text-anchor="middle" fill="#cbd5e1" font-size="12">Rule: Cation name FIRST, then monoatomic anion ending in -ide</text>
    </g>
    <g id="c9s10_poly" style="display:none">
      <text x="300" y="45" text-anchor="middle" fill="#34d399" font-size="16" font-weight="bold">Table 9.1(b): Polyatomic Ions</text>
      <text x="300" y="88" text-anchor="middle" fill="#fde047" font-size="14">1- Charge: Hydroxide (OH&#8315;), Nitrate (NO&#8323;&#8315;), Hydrogencarbonate (HCO&#8323;&#8315;)</text>
      <text x="300" y="130" text-anchor="middle" fill="#7dd3fc" font-size="14">2- Charge: Carbonate (CO&#8323;&sup2;&#8315;), Sulfate (SO&#8324;&sup2;&#8315;)</text>
      <text x="300" y="172" text-anchor="middle" fill="#fda4af" font-size="14">1+ Cation: Ammonium (NH&#8324;&#8314;)</text>
    </g>
  </svg>
</div>
<script>
window.setC9S10 = function(m){
  document.getElementById('c9s10_mono').style.display = (m==='mono'?'block':'none');
  document.getElementById('c9s10_poly').style.display = (m==='poly'?'block':'none');
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">Section 9.5 Criss-Cross Formula Builder</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S11('ccl4')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">CCl&#8324;</button>
      <button onclick="setC9S11('mgo')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">MgO</button>
      <button onclick="setC9S11('mgoh')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Mg(OH)&#8322;</button>
      <button onclick="setC9S11('al2so4')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Al&#8322;(SO&#8324;)&#8323;</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c9s11_s1" x="300" y="60" text-anchor="middle" fill="#7dd3fc" font-size="18" font-weight="bold">Al (3+)   &times;   SO&#8324; (2-)</text>
    <text id="c9s11_s2" x="300" y="105" text-anchor="middle" fill="#fde047" font-size="15">Criss-Cross magnitudes: 2 goes to Al, 3 goes to (SO&#8324;)</text>
    <text id="c9s11_res" x="300" y="160" text-anchor="middle" fill="#6ee7b7" font-size="28" font-weight="bold">Al&#8322;(SO&#8324;)&#8323;</text>
    <text x="300" y="205" text-anchor="middle" fill="#cbd5e1" font-size="12">Always simplify ratios (Mg&#8322;O&#8322; &rarr; MgO) and bracket polyatomic ions when subscript &gt; 1</text>
  </svg>
</div>
<script>
window.setC9S11 = function(k){
  const m = {
    ccl4: ['C (valency 4)   x   Cl (valency 1)', 'Criss-Cross: 1 goes to C, 4 goes to Cl', 'CCl4'],
    mgo:  ['Mg (2+)   x   O (2-)', 'Criss-Cross gives Mg2O2 -> Divide by 2 to simplify!', 'MgO'],
    mgoh: ['Mg (2+)   x   OH (1-)', 'Criss-Cross: 1 to Mg, 2 to (OH) in brackets', 'Mg(OH)2'],
    al2so4: ['Al (3+)   x   SO4 (2-)', 'Criss-Cross: 2 goes to Al, 3 goes to (SO4)', 'Al2(SO4)3']
  };
  document.getElementById('c9s11_s1').textContent = m[k][0];
  document.getElementById('c9s11_s2').textContent = m[k][1];
  document.getElementById('c9s11_res').textContent = m[k][2];
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 9.4: 9V Circuit Conductivity &amp; Solubility</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S12('solid')" class="px-2 py-1 rounded bg-slate-700 text-xs text-slate-200 border border-slate-500">Solid NaCl</button>
      <button onclick="setC9S12('aq')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Aqueous NaCl</button>
      <button onclick="setC9S12('sugar')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Sugar Water</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="210" y="95" width="180" height="80" rx="8" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="2"/>
    <circle id="c9s12_bulb" cx="300" cy="48" r="20" fill="#334155" stroke="#94a3b8" stroke-width="3"/>
    <text id="c9s12_lbl" x="300" y="140" text-anchor="middle" fill="#cbd5e1" font-size="14" font-weight="bold">Solid NaCl: Ions Locked &rarr; Bulb OFF</text>
    <text id="c9s12_sub" x="300" y="206" text-anchor="middle" fill="#fde047" font-size="12">Ionic: High MP, water-soluble | Covalent (Camphor): Lower MP, kerosene-soluble</text>
  </svg>
</div>
<script>
window.setC9S12 = function(m){
  const b = document.getElementById('c9s12_bulb');
  const l = document.getElementById('c9s12_lbl');
  if(m==='aq'){
    b.setAttribute('fill','#fbbf24'); b.setAttribute('stroke','#fef08a');
    l.textContent = 'Aqueous NaCl: Mobile Na+ & Cl- Ions -> Bulb GLOWS!';
  } else if(m==='sugar'){
    b.setAttribute('fill','#334155'); b.setAttribute('stroke','#94a3b8');
    l.textContent = 'Sugar Water (Covalent): Zero Free Ions -> Bulb OFF';
  } else {
    b.setAttribute('fill','#334155'); b.setAttribute('stroke','#94a3b8');
    l.textContent = 'Solid NaCl: Ions Locked in Lattice -> Bulb OFF';
  }
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Section 9.7 Molecular Mass Calculator (u)</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S13('h2o')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">H&#8322;O (18 u)</button>
      <button onclick="setC9S13('co2')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">CO&#8322; (44 u)</button>
      <button onclick="setC9S13('hno3')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">HNO&#8323; (63 u)</button>
      <button onclick="setC9S13('ch4')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">CH&#8324; (16 u)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c9s13_f" x="300" y="92" text-anchor="middle" fill="#fbbf24" font-size="24" font-weight="bold">H&#8322;O = (1 &times; 2) + 16 = 18 u</text>
    <text id="c9s13_d" x="300" y="135" text-anchor="middle" fill="#cbd5e1" font-size="13">Example 9.4: Sum of atomic masses of all atoms in one covalent molecule</text>
    <text x="300" y="165" text-anchor="middle" fill="#6ee7b7" font-size="12">Atomic Masses: H = 1 u, C = 12 u, N = 14 u, O = 16 u</text>
  </svg>
</div>
<script>
window.setC9S13 = function(k){
  const m = {
    h2o: ['H2O = (1 x 2) + 16 = 18 u', 'Example 9.4: 2 Hydrogen atoms + 1 Oxygen atom'],
    co2: ['CO2 = 12 + (16 x 2) = 44 u', 'Example 9.5: 12 + 32 = 44 u'],
    hno3: ['HNO3 = 1 + 14 + (16 x 3) = 63 u', 'Pause & Ponder 21: 1 + 14 + 48 = 63 u'],
    ch4: ['CH4 = 12 + (1 x 4) = 16 u', 'Pause & Ponder 22: Methane molecular mass = 16 u']
  };
  document.getElementById('c9s13_f').textContent = m[k][0];
  document.getElementById('c9s13_d').textContent = m[k][1];
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">Section 9.8 Formula Unit Mass Calculator (u)</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S14('na2o')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Na&#8322;O (62 u)</button>
      <button onclick="setC9S14('cano3')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Ca(NO&#8323;)&#8322; (164 u)</button>
      <button onclick="setC9S14('kcl')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">KCl (74.5 u)</button>
      <button onclick="setC9S14('mgoh')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Mg(OH)&#8322; (58 u)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text id="c9s14_f" x="300" y="92" text-anchor="middle" fill="#6ee7b7" font-size="22" font-weight="bold">Ca(NO&#8323;)&#8322; = 40 + 2&times;[14 + 48] = 164 u</text>
    <text id="c9s14_d" x="300" y="135" text-anchor="middle" fill="#cbd5e1" font-size="13">Example 9.7: Multiply polyatomic bracket contents by outer subscript 2</text>
    <text x="300" y="165" text-anchor="middle" fill="#fde047" font-size="12">Used for ionic crystals (simplest empirical formula unit)</text>
  </svg>
</div>
<script>
window.setC9S14 = function(k){
  const m = {
    na2o: ['Na2O = (23 x 2) + 16 = 62 u', 'Example 9.6: 46 + 16 = 62 u'],
    cano3: ['Ca(NO3)2 = 40 + 2 x [14 + 48] = 164 u', 'Example 9.7: 40 + 124 = 164 u'],
    kcl: ['KCl = 39 + 35.5 = 74.5 u', 'Pause & Ponder 23: Potassium Chloride'],
    mgoh: ['Mg(OH)2 = 24 + 2 x (16 + 1) = 58 u', 'Pause & Ponder 24: 24 + 34 = 58 u']
  };
  document.getElementById('c9s14_f').textContent = m[k][0];
  document.getElementById('c9s14_d').textContent = m[k][1];
};
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-purple-300 uppercase">Ion Subatomic Particle Inspector</span>
    <div class="flex gap-1.5">
      <button onclick="setC9S15('al')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">&sup2;&#8311;Al&sup3;&#8314;</button>
      <button onclick="setC9S15('br')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">&sup8;&sup0;Br&#8315;</button>
      <button onclick="setC9S15('hg')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">&sup2;&sup0;&sup1;Hg&sup2;&#8314;</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text id="c9s15_h" x="300" y="92" text-anchor="middle" fill="#d8b4fe" font-size="22" font-weight="bold">27-13-Al 3+ : 13 p+, 14 n0, 10 e-</text>
    <text id="c9s15_b1" x="300" y="130" text-anchor="middle" fill="#cbd5e1" font-size="13">Lost 3 electrons (13 - 3 = 10 e-) | Neutrons = 27 - 13 = 14</text>
    <text x="300" y="160" text-anchor="middle" fill="#6ee7b7" font-size="12">Charge balance: +6 (2 Al3+) neutralizes -6 (3 SO4 2-)</text>
  </svg>
</div>
<script>
window.setC9S15 = function(k){
  const m = {
    al: ['27-13-Al 3+ : 13 p+, 14 n0, 10 e-', 'Lost 3 electrons (13 - 3 = 10 e-) | Neutrons = 27 - 13 = 14'],
    br: ['80-35-Br - : 35 p+, 45 n0, 36 e-', 'Gained 1 electron (35 + 1 = 36 e-) | Neutrons = 80 - 35 = 45'],
    hg: ['201-80-Hg 2+ : 80 p+, 121 n0, 78 e-', 'Lost 2 electrons (80 - 2 = 78 e-) | Neutrons = 201 - 80 = 121']
  };
  document.getElementById('c9s15_h').textContent = m[k][0];
  document.getElementById('c9s15_b1').textContent = m[k][1];
};
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">At a Glance: Chapter 9 Master Map</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S16('laws')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Mass Laws</button>
      <button onclick="setC9S16('bonds')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Bonds</button>
      <button onclick="setC9S16('form')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Formulae</button>
      <button onclick="setC9S16('mass')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Masses</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c9s16_h" x="300" y="90" text-anchor="middle" fill="#fbbf24" font-size="18" font-weight="bold">Lavoisier (1789) &amp; Proust &rarr; Dalton (1808)</text>
    <text id="c9s16_b1" x="300" y="126" text-anchor="middle" fill="#cbd5e1" font-size="13">Conservation: Mass Reactants = Mass Products (Closed System)</text>
    <text id="c9s16_b2" x="300" y="156" text-anchor="middle" fill="#6ee7b7" font-size="13">Constant Proportions: Fixed Mass Ratios (H2O = 1:8)</text>
  </svg>
</div>
<script>
window.setC9S16 = function(k){
  const m = {
    laws: ['Lavoisier (1789) & Proust -> Dalton (1808)', 'Conservation: Mass Reactants = Mass Products (Closed System)', 'Constant Proportions: Fixed Mass Ratios (H2O = 1:8)'],
    bonds: ['Covalent (Sharing: H2, O2, N2) vs Ionic (Transfer: NaCl)', 'Ionic compounds form 3D crystal lattices (6 neighbours)', 'Ionic conducts when aqueous/molten; Covalent does not'],
    form: ['Criss-Cross Method: Cross valencies or ion charges', 'Simplify ratios (Mg2O2 -> MgO) & bracket polyatomics Mg(OH)2', 'Prefixes: mono, di, tri, tetra, penta, hexa (H2O/NH3 exceptions)'],
    mass: ['Molecular Mass (Covalent): H2O=18u, CO2=44u, HNO3=63u, CH4=16u', 'Formula Unit Mass (Ionic): Na2O=62u, Ca(NO3)2=164u, KCl=74.5u', 'All masses summed in unified atomic mass units (u)']
  };
  document.getElementById('c9s16_h').textContent = m[k][0];
  document.getElementById('c9s16_b1').textContent = m[k][1];
  document.getElementById('c9s16_b2').textContent = m[k][2];
};
</script>"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Chemical Transformation: 2H&#8322; + O&#8322; &rarr; 2H&#8322;O</span>
    <div class="flex gap-2">
      <button onclick="setC9S1('react')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Before: H&#8322; &amp; O&#8322; Gases</button>
      <button onclick="setC9S1('prod')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">After: Liquid Water</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c9s1_react">
      <circle cx="170" cy="110" r="36" fill="rgba(244,63,94,0.25)" stroke="#f43f5e" stroke-width="2"/>
      <text x="170" y="106" text-anchor="middle" fill="#fda4af" font-size="15" font-weight="bold">H&#8322; Gas</text>
      <text x="170" y="126" text-anchor="middle" fill="#cbd5e1" font-size="11">Combustible!</text>
      <text x="295" y="116" text-anchor="middle" fill="#94a3b8" font-size="22" font-weight="bold">+</text>
      <circle cx="420" cy="110" r="36" fill="rgba(251,191,36,0.25)" stroke="#fbbf24" stroke-width="2"/>
      <text x="420" y="106" text-anchor="middle" fill="#fde047" font-size="15" font-weight="bold">O&#8322; Gas</text>
      <text x="420" y="126" text-anchor="middle" fill="#cbd5e1" font-size="11">Supports Fire!</text>
      <text x="300" y="195" text-anchor="middle" fill="#cbd5e1" font-size="12">Reactants have fiery properties, yet bonding transforms them completely!</text>
    </g>
    <g id="c9s1_prod" style="display:none">
      <ellipse cx="300" cy="115" rx="95" ry="48" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="3"/>
      <text x="300" y="110" text-anchor="middle" fill="#7dd3fc" font-size="18" font-weight="bold">Liquid H&#8322;O (Water)</text>
      <text x="300" y="135" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Extinguishes Fire!</text>
      <text x="300" y="200" text-anchor="middle" fill="#cbd5e1" font-size="12">Chemical reactions create new compounds with completely new properties</text>
    </g>
  </svg>
</div>
<script>
window.setC9S1 = function(m){
  document.getElementById('c9s1_react').style.display = (m==='react'?'block':'none');
  document.getElementById('c9s1_prod').style.display = (m==='prod'?'block':'none');
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 9.2: Baking Soda + Vinegar Mass Test</span>
    <div class="flex gap-2">
      <button onclick="setC9S2('open')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Set-up 1: Open Flask</button>
      <button onclick="setC9S2('closed')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Set-up 2: Balloon Sealed</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon points="260,155 340,155 315,90 285,90" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
    <rect x="285" y="75" width="30" height="15" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <ellipse id="c9s2_bal" cx="300" cy="48" rx="22" ry="26" fill="rgba(52,211,153,0.35)" stroke="#34d399" stroke-width="2" style="display:none"/>
    <text id="c9s2_gas" x="300" y="52" text-anchor="middle" fill="#fda4af" font-size="13" font-weight="bold">CO&#8322; Gas Escapes!</text>
    <rect x="220" y="160" width="160" height="28" rx="6" fill="#1e293b" stroke="#94a3b8"/>
    <text id="c9s2_wt" x="300" y="179" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="bold">Scale: 150.0 g &rarr; 146.5 g</text>
    <text id="c9s2_msg" x="300" y="216" text-anchor="middle" fill="#cbd5e1" font-size="12">Open System: Escaping CO&#8322; lowers scale reading (Antoine Lavoisier 1789)</text>
  </svg>
</div>
<script>
window.setC9S2 = function(m){
  const bal = document.getElementById('c9s2_bal');
  const gas = document.getElementById('c9s2_gas');
  const wt = document.getElementById('c9s2_wt');
  const msg = document.getElementById('c9s2_msg');
  if(m==='open'){
    bal.style.display='none'; gas.textContent='CO2 Gas Escapes!'; gas.setAttribute('fill','#fda4af');
    wt.textContent='Scale: 150.0 g -> 146.5 g';
    msg.textContent='Open System: Escaping CO2 lowers scale reading';
  } else {
    bal.style.display='block'; gas.textContent='CO2 Trapped!'; gas.setAttribute('fill','#6ee7b7');
    wt.textContent='Scale: 150.0 g -> 150.0 g (EQUAL!)';
    msg.textContent='Closed System: Mass of Reactants = Mass of Products (Lavoisier 1789)';
  }
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 9.3 Precipitation: Na&#8322;SO&#8324; + BaCl&#8322;</span>
    <div class="flex gap-2">
      <button onclick="setC9S3('before')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Before Tilting</button>
      <button onclick="setC9S3('after')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">After Mixing (BaSO&#8324;&darr;)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon points="245,160 355,160 322,70 278,70" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2"/>
    <rect x="282" y="54" width="36" height="16" fill="#d97706"/>
    <rect id="c9s3_ppt" x="255" y="142" width="90" height="16" rx="4" fill="#f8fafc" style="display:none"/>
    <text id="c9s3_st" x="300" y="38" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Two Clear Solutions Separated Inside Corked Flask</text>
    <text x="300" y="192" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Balance Mass: Unchanged! (Reactants = Products)</text>
    <text x="300" y="218" text-anchor="middle" fill="#cbd5e1" font-size="11">Ex 9.1: 6.92 g = 6.92 g | Ex 9.2: 2.4 g C &rarr; 8.8 g CO&#8322; | 20 g H&#8322; + 160 g O&#8322; = 180 g H&#8322;O</text>
  </svg>
</div>
<script>
window.setC9S3 = function(m){
  const ppt = document.getElementById('c9s3_ppt');
  const st = document.getElementById('c9s3_st');
  if(m==='before'){
    ppt.style.display='none';
    st.textContent='Two Clear Solutions Separated Inside Corked Flask';
  } else {
    ppt.style.display='block';
    st.textContent='White BaSO4 Precipitate Formed — Total Mass Identical!';
  }
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">Proust's Law of Constant Proportions</span>
    <div class="flex gap-1.5">
      <button onclick="setC9S4('h2o')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">H&#8322;O (1 : 8)</button>
      <button onclick="setC9S4('hgs')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Cinnabar (Hingula)</button>
      <button onclick="setC9S4('nacl')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Ex 9.3 NaCl</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <text id="c9s4_h" x="300" y="90" text-anchor="middle" fill="#fde047" font-size="20" font-weight="bold">Pure Water (H&#8322;O): Always 1 : 8 by Mass</text>
    <text id="c9s4_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">1 g Hydrogen + 8 g Oxygen = 9 g Pure Water (any source!)</text>
    <text id="c9s4_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Joseph Louis Proust: Pure compounds have invariant mass ratios</text>
  </svg>
</div>
<script>
window.setC9S4 = function(k){
  const m = {
    h2o: ['Pure Water (H2O): Always 1 : 8 by Mass', '1 g Hydrogen + 8 g Oxygen = 9 g Pure Water (any source!)', 'Joseph Louis Proust: Pure compounds have invariant mass ratios'],
    hgs: ['Red Cinnabar (Hingula, HgS): Fixed Composition', '86.22% Mercury (Hg) + 13.78% Sulfur (S) by mass', 'Ancient Indian pigment extraction confirmed constant ratios'],
    nacl: ['Ex 9.3 Sodium Chloride (NaCl): 23 : 35.5 Ratio', '46 g Sodium reacts with exactly 71 g Chlorine', 'Mixtures vary freely, but pure compounds never vary ratios!']
  };
  document.getElementById('c9s4_h').textContent = m[k][0];
  document.getElementById('c9s4_b1').textContent = m[k][1];
  document.getElementById('c9s4_b2').textContent = m[k][2];
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">John Dalton's 1808 Atomic Theory</span>
    <div class="flex gap-1.5">
      <button onclick="setC9S5('cons')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Explains Conservation</button>
      <button onclick="setC9S5('prop')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Explains Proportions</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="150" cy="110" r="22" fill="#38bdf8"/><circle cx="205" cy="110" r="22" fill="#f43f5e"/>
    <text x="275" y="116" text-anchor="middle" fill="#94a3b8" font-size="22" font-weight="bold">&rarr;</text>
    <circle cx="365" cy="110" r="22" fill="#38bdf8"/><circle cx="408" cy="110" r="22" fill="#f43f5e"/>
    <text id="c9s5_h" x="300" y="42" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">Postulate 2: Atoms neither created nor destroyed (Rearrangement!)</text>
    <text id="c9s5_sub" x="300" y="185" text-anchor="middle" fill="#cbd5e1" font-size="13">Total atoms before = Total atoms after &rArr; Explains Lavoisier's Law!</text>
  </svg>
</div>
<script>
window.setC9S5 = function(m){
  if(m==='cons'){
    document.getElementById('c9s5_h').textContent = 'Postulate 2: Atoms neither created nor destroyed (Rearrangement!)';
    document.getElementById('c9s5_sub').textContent = 'Total atoms before = Total atoms after => Explains Lavoisier Law!';
  } else {
    document.getElementById('c9s5_h').textContent = 'Postulates 5 & 6: Simple Whole-Number & Constant Atom Ratios';
    document.getElementById('c9s5_sub').textContent = 'Fixed atom counts per molecule => Explains Proust Constant Proportions!';
  }
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Why Atoms Combine: Lower Potential Energy &amp; Octet</span>
    <div class="flex gap-2">
      <button onclick="setC9S6('cov')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Path 1: Covalent Share</button>
      <button onclick="setC9S6('ion')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Path 2: Ionic Transfer</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <path d="M 80 65 Q 190 65 250 140 Q 300 185 350 140 Q 410 65 520 65" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="110" cy="65" r="8" fill="#f43f5e"/>
    <text x="110" y="48" text-anchor="middle" fill="#fda4af" font-size="11">Free O atom (6 e-)</text>
    <circle cx="300" cy="162" r="10" fill="#34d399"/>
    <text x="300" y="142" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Bonded Molecule (Low Energy!)</text>
    <text id="c9s6_msg" x="300" y="212" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">Covalent Bond: Non-metals share valence electron pairs to reach Octet (8)</text>
  </svg>
</div>
<script>
window.setC9S6 = function(m){
  document.getElementById('c9s6_msg').textContent = m==='cov'
    ? 'Covalent Bond: Non-metals share valence electron pairs to reach Octet (8)'
    : 'Ionic Bond: Metals transfer electrons to Non-metals forming + and - ions';
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Covalent Bonds in Elements: Single, Double, Triple</span>
    <div class="flex gap-1.5">
      <button onclick="setC9S7(1)" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">H&#8322; / Cl&#8322; (Single)</button>
      <button onclick="setC9S7(2)" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">O&#8322; (Double)</button>
      <button onclick="setC9S7(3)" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">N&#8322; (Triple)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="205" cy="115" r="46" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="395" cy="115" r="46" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="3"/>
    <text id="c9s7_a1" x="205" y="122" text-anchor="middle" fill="#fff" font-size="22" font-weight="bold">H</text>
    <text id="c9s7_a2" x="395" y="122" text-anchor="middle" fill="#fff" font-size="22" font-weight="bold">H</text>
    <line id="c9s7_l1" x1="255" y1="115" x2="345" y2="115" stroke="#fbbf24" stroke-width="5"/>
    <line id="c9s7_l2" x1="255" y1="103" x2="345" y2="103" stroke="#fbbf24" stroke-width="5" style="display:none"/>
    <line id="c9s7_l3" x1="255" y1="127" x2="345" y2="127" stroke="#fbbf24" stroke-width="5" style="display:none"/>
    <text id="c9s7_desc" x="300" y="200" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Single Covalent Bond (H-H): 1 shared pair (2 electrons) &rarr; Duplet!</text>
  </svg>
</div>
<script>
window.setC9S7 = function(n){
  const l1=document.getElementById('c9s7_l1'), l2=document.getElementById('c9s7_l2'), l3=document.getElementById('c9s7_l3');
  const a1=document.getElementById('c9s7_a1'), a2=document.getElementById('c9s7_a2'), d=document.getElementById('c9s7_desc');
  if(n===1){
    a1.textContent='H'; a2.textContent='H'; l1.style.display='block'; l2.style.display='none'; l3.style.display='none';
    d.textContent='Single Covalent Bond (H-H, Cl-Cl, F-F): 1 shared electron pair';
  } else if(n===2){
    a1.textContent='O'; a2.textContent='O'; l1.style.display='none'; l2.style.display='block'; l3.style.display='block';
    d.textContent='Double Covalent Bond (O=O): 2 shared electron pairs (4 electrons)';
  } else {
    a1.textContent='N'; a2.textContent='N'; l1.style.display='block'; l2.style.display='block'; l3.style.display='block';
    d.textContent='Triple Covalent Bond (N=N): 3 shared electron pairs (6 electrons)';
  }
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">Covalent Compounds &amp; Prefix Naming</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC9S8('co')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">CO</button>
      <button onclick="setC9S8('n2o5')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">N&#8322;O&#8325;</button>
      <button onclick="setC9S8('ccl4')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">CCl&#8324;</button>
      <button onclick="setC9S8('exc')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">H&#8322;O / NH&#8323;</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c9s8_h" x="300" y="92" text-anchor="middle" fill="#fbbf24" font-size="22" font-weight="bold">CO &rarr; Carbon Monoxide</text>
    <text id="c9s8_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">Prefixes: mono (1), di (2), tri (3), tetra (4), penta (5), hexa (6)</text>
    <text id="c9s8_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="12">Vowel dropped before oxide: mono + oxide &rarr; monoxide!</text>
  </svg>
</div>
<script>
window.setC9S8 = function(k){
  const m = {
    co: ['CO -> Carbon Monoxide', 'Prefixes: mono (1), di (2), tri (3), tetra (4), penta (5), hexa (6)', 'Vowel dropped before oxide: mono + oxide -> monoxide!'],
    n2o5: ['N2O5 -> Dinitrogen Pentoxide', 'di- (2 nitrogens) + penta- (5 oxygens, drop a)', 'Raja Ramanna also advanced India nuclear energy & isotopes'],
    ccl4: ['CCl4 -> Carbon Tetrachloride', '1 Carbon + 4 Chlorines (tetra-)', 'Covalent sharing builds HCl, H2O, and CCl4'],
    exc: ['Exceptions: H2O = Water | NH3 = Ammonia', 'Common names retained instead of systematic prefixes', 'H2O has 2 single covalent O-H bonds']
  };
  document.getElementById('c9s8_h').textContent = m[k][0];
  document.getElementById('c9s8_b1').textContent = m[k][1];
  document.getElementById('c9s8_b2').textContent = m[k][2];
};
</script>"""
}

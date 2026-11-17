#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Table 8.2 IUPAC Symbols &amp; Latin Roots</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC8S9('Fe')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Iron (Fe)</button>
      <button onclick="setC8S9('Au')" class="px-2 py-1 rounded bg-yellow-600/30 text-xs text-yellow-200 border border-yellow-500/40">Gold (Au)</button>
      <button onclick="setC8S9('Na')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Sodium (Na)</button>
      <button onclick="setC8S9('W')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Tungsten (W)</button>
      <button onclick="setC8S9('Co')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Co vs CO</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="85" y="42" width="430" height="150" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c8s9_sym" x="300" y="95" text-anchor="middle" fill="#fbbf24" font-size="34" font-weight="bold">Fe</text>
    <text id="c8s9_name" x="300" y="132" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">Iron &larr; Latin: ferrum</text>
    <text id="c8s9_rule" x="300" y="165" text-anchor="middle" fill="#cbd5e1" font-size="12">IUPAC Rule: 1st letter UPPERCASE, 2nd letter lowercase (Berzelius 1813)</text>
  </svg>
</div>
<script>
window.setC8S9 = function(k){
  const map = {
    Fe: ['Fe', 'Iron <- Latin: ferrum', '1st letter UPPERCASE, 2nd letter lowercase'],
    Au: ['Au', 'Gold <- Latin: aurum', 'Berzelius alphabetic abbreviation (1813)'],
    Na: ['Na', 'Sodium <- Latin: natrium', 'Never write NA; always Na'],
    W:  ['W', 'Tungsten <- German: wolfram', 'Single-letter symbol is always UPPERCASE'],
    Co: ['Co vs CO', 'Co = Cobalt element | CO = Carbon Monoxide gas', 'Capitalization changes chemical meaning completely!']
  };
  const d = map[k];
  document.getElementById('c8s9_sym').textContent = d[0];
  document.getElementById('c8s9_name').textContent = d[1];
  document.getElementById('c8s9_rule').textContent = d[2];
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Nuclide Builder: Z &amp; A = Z + n</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Protons Z: <b id="c8s10_z" class="text-rose-300">6</b></label>
      <input type="range" min="1" max="11" step="1" value="6" id="c8s10_pz" oninput="updC8S10()" class="w-20 accent-rose-400">
      <label class="text-xs text-slate-300">Neutrons n: <b id="c8s10_n" class="text-cyan-300">6</b></label>
      <input type="range" min="0" max="12" step="1" value="6" id="c8s10_pn" oninput="updC8S10()" class="w-20 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c8s10_a" x="235" y="90" text-anchor="end" fill="#fbbf24" font-size="24" font-weight="bold">12</text>
    <text id="c8s10_zb" x="235" y="145" text-anchor="end" fill="#f43f5e" font-size="24" font-weight="bold">6</text>
    <text id="c8s10_el" x="245" y="132" fill="#38bdf8" font-size="56" font-weight="bold">C</text>
    <text id="c8s10_info" x="300" y="188" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Carbon: Z = 6 (6 p+, 6 e-) | Mass Number A = 6 + 6 = 12</text>
    <text x="300" y="216" text-anchor="middle" fill="#94a3b8" font-size="11">Nucleons = Protons + Neutrons | Z uniquely defines the element</text>
  </svg>
</div>
<script>
window.updC8S10 = function(){
  const syms = ['','H','He','Li','Be','B','C','N','O','F','Ne','Na'];
  const names = ['','Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Fluorine','Neon','Sodium'];
  const z = parseInt(document.getElementById('c8s10_pz').value,10);
  const n = parseInt(document.getElementById('c8s10_pn').value,10);
  const A = z + n;
  document.getElementById('c8s10_z').textContent = z;
  document.getElementById('c8s10_n').textContent = n;
  document.getElementById('c8s10_a').textContent = A;
  document.getElementById('c8s10_zb').textContent = z;
  document.getElementById('c8s10_el').textContent = syms[z];
  document.getElementById('c8s10_info').textContent = names[z] + ': Z = ' + z + ' (' + z + ' p+, ' + z + ' e-) | Mass Number A = ' + z + ' + ' + n + ' = ' + A;
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Bohr-Bury 2n&sup2; Shells (Fig 8.11: Z = 1 to 18)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Atomic No Z: <b id="c8s11_z" class="text-amber-300">11 (Na)</b></label>
      <input type="range" min="1" max="18" step="1" value="11" id="c8s11_sl" oninput="updC8S11()" class="w-28 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="200" cy="120" r="14" fill="#ef4444"/><text id="c8s11_nuc" x="200" y="124" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Na</text>
    <circle cx="200" cy="120" r="34" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="200" cy="120" r="58" fill="none" stroke="#34d399" stroke-width="2"/>
    <circle cx="200" cy="120" r="82" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <text id="c8s11_cfg" x="445" y="78" text-anchor="middle" fill="#fde047" font-size="22" font-weight="bold">K=2, L=8, M=1</text>
    <text x="445" y="118" text-anchor="middle" fill="#7dd3fc" font-size="12">Max 2n&sup2;: K=2, L=8, M=18, N=32</text>
    <text x="445" y="145" text-anchor="middle" fill="#6ee7b7" font-size="12">Outermost shell max = 8 electrons</text>
    <text x="445" y="172" text-anchor="middle" fill="#cbd5e1" font-size="11">Fill stepwise from inside out (K &rarr; L &rarr; M)</text>
  </svg>
</div>
<script>
window.updC8S11 = function(){
  const syms = ['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar'];
  const z = parseInt(document.getElementById('c8s11_sl').value,10);
  const k = Math.min(2, z);
  const l = Math.min(8, Math.max(0, z - 2));
  const m = Math.max(0, z - 10);
  document.getElementById('c8s11_z').textContent = z + ' (' + syms[z] + ')';
  document.getElementById('c8s11_nuc').textContent = syms[z];
  let txt = 'K=' + k;
  if(l>0) txt += ', L=' + l;
  if(m>0) txt += ', M=' + m;
  document.getElementById('c8s11_cfg').textContent = txt;
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Valency &amp; Octet Rule Calculator</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Valence e-: <b id="c8s12_v" class="text-cyan-300">6</b></label>
      <input type="range" min="1" max="8" step="1" value="6" id="c8s12_sl" oninput="updC8S12()" class="w-28 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c8s12_val" x="300" y="75" text-anchor="middle" fill="#6ee7b7" font-size="26" font-weight="bold">Valency = 8 - 6 = 2</text>
    <text id="c8s12_ex" x="300" y="118" text-anchor="middle" fill="#fde047" font-size="15">Example: Oxygen (2, 6) gains/shares 2 e- to complete Octet (8)</text>
    <text x="300" y="162" text-anchor="middle" fill="#cbd5e1" font-size="13">1 to 4 valence e- &rArr; Valency = v  |  5 to 7 valence e- &rArr; Valency = 8 - v</text>
    <text x="300" y="192" text-anchor="middle" fill="#7dd3fc" font-size="12">Full Octet (8) or Helium Duplet (2) &rArr; Valency = 0 (Inert Noble Gas)</text>
  </svg>
</div>
<script>
window.updC8S12 = function(){
  const v = parseInt(document.getElementById('c8s12_sl').value,10);
  document.getElementById('c8s12_v').textContent = v;
  const ex = ['','Na (2,8,1)','Mg (2,8,2)','Al (2,8,3)','C (2,4)','N (2,5)','O (2,6)','F (2,7)','Ne (2,8)'];
  const valEl = document.getElementById('c8s12_val');
  const exEl = document.getElementById('c8s12_ex');
  if(v <= 4){
    valEl.textContent = 'Valency = ' + v + ' (1-4 valence e- rule)';
    exEl.textContent = 'Example: ' + ex[v] + ' has ' + v + ' valence electrons -> Valency ' + v;
  } else if(v < 8){
    valEl.textContent = 'Valency = 8 - ' + v + ' = ' + (8-v);
    exEl.textContent = 'Example: ' + ex[v] + ' needs ' + (8-v) + ' e- to reach stable Octet (8)';
  } else {
    valEl.textContent = 'Valency = 0 (Full Octet!)';
    exEl.textContent = 'Example: Neon (2, 8) is chemically inert with 8 valence electrons';
  }
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">Isotopes &amp; Societal Applications</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC8S13('H')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">H Isotopes</button>
      <button onclick="setC8S13('U')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">U-235 Fuel</button>
      <button onclick="setC8S13('Co')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Co-60 Cancer</button>
      <button onclick="setC8S13('I')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">I-131 Thyroid</button>
      <button onclick="setC8S13('C')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">C-14 Dating</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text id="c8s13_h" x="300" y="92" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Hydrogen: Protium (1H), Deuterium (2H), Tritium (3H)</text>
    <text id="c8s13_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">All have Z = 1 proton, with 0, 1, and 2 neutrons respectively</text>
    <text id="c8s13_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Same Z &rArr; Identical chemical properties, different physical mass!</text>
  </svg>
</div>
<script>
window.setC8S13 = function(k){
  const m = {
    H: ['Hydrogen: Protium (1H), Deuterium (2H), Tritium (3H)', 'All have Z = 1 proton, with 0, 1, and 2 neutrons respectively', 'Same Z => Identical chemical properties, different physical mass!'],
    U: ['Uranium-235 (235-92-U): Nuclear Power Fuel', 'Fission of U-235 releases immense clean thermal energy', 'Powers nuclear electricity plants across India & the world'],
    Co: ['Cobalt-60 (60-27-Co): Cancer Radiation Therapy', 'Emits controlled gamma rays to destroy malignant tumour cells', 'Key medical radioisotope application in modern hospitals'],
    I: ['Iodine-131 (131-53-I): Goitre & Thyroid Treatment', 'Selectively absorbed by the thyroid gland to treat disorders', 'Essential diagnostic & therapeutic medical isotope'],
    C: ['Carbon-14 (14-6-C): Radiocarbon Fossil Dating', 'Measures decay of C-14 in ancient wood, bone & fossils', 'Also note Carbon-12 and Carbon-13 are stable carbon isotopes']
  };
  document.getElementById('c8s13_h').textContent = m[k][0];
  document.getElementById('c8s13_b1').textContent = m[k][1];
  document.getElementById('c8s13_b2').textContent = m[k][2];
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Average Atomic Mass &amp; Isobars</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">% 35-Cl: <b id="c8s14_p" class="text-amber-300">75%</b></label>
      <input type="range" min="0" max="100" step="5" value="75" id="c8s14_sl" oninput="updC8S14()" class="w-28 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c8s14_avg" x="300" y="65" text-anchor="middle" fill="#6ee7b7" font-size="20" font-weight="bold">Avg Mass = 35(0.75) + 37(0.25) = 35.50 u</text>
    <rect x="90" y="105" width="420" height="75" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="300" y="135" text-anchor="middle" fill="#d8b4fe" font-size="15" font-weight="bold">Isobars (Different Z, Same A = 40): 40-20-Ca | 40-19-K | 40-18-Ar</text>
    <text x="300" y="162" text-anchor="middle" fill="#cbd5e1" font-size="12">Modern Quantum Model replaces flat Bohr rings with 3D electron clouds</text>
  </svg>
</div>
<script>
window.updC8S14 = function(){
  const p35 = parseInt(document.getElementById('c8s14_sl').value,10);
  const p37 = 100 - p35;
  const avg = 35*(p35/100) + 37*(p37/100);
  document.getElementById('c8s14_p').textContent = p35 + '% (37-Cl: ' + p37 + '%)';
  document.getElementById('c8s14_avg').textContent = 'Avg Mass = 35(' + (p35/100).toFixed(2) + ') + 37(' + (p37/100).toFixed(2) + ') = ' + avg.toFixed(2) + ' u';
};
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Revise, Reflect, Refine: Thought Experiments</span>
    <div class="flex gap-2">
      <button onclick="setC8S15('foil')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Thicker Gold Foil</button>
      <button onclick="setC8S15('heavy')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Heavy Electron Shift</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <text id="c8s15_h" x="300" y="92" text-anchor="middle" fill="#fde047" font-size="18" font-weight="bold">Thicker Gold Foil (1000 &rarr; 10,000 atoms)</text>
    <text id="c8s15_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">Alpha beam encounters 10x more gold nuclei along its path</text>
    <text id="c8s15_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Result: Large-angle scattering and 180-deg rebounds increase!</text>
  </svg>
</div>
<script>
window.setC8S15 = function(m){
  if(m==='foil'){
    document.getElementById('c8s15_h').textContent = 'Thicker Gold Foil (1000 -> 10,000 atoms)';
    document.getElementById('c8s15_b1').textContent = 'Alpha beam encounters 10x more gold nuclei along its path';
    document.getElementById('c8s15_b2').textContent = 'Result: Large-angle scattering and 180-deg rebounds increase!';
  } else {
    document.getElementById('c8s15_h').textContent = 'Hypothetical Heavy Electrons (1 u each)';
    document.getElementById('c8s15_b1').textContent = 'Normally 6 electrons in 12-6-C have negligible mass (~0 u)';
    document.getElementById('c8s15_b2').textContent = 'If each electron weighed 1 u, total 12-6-C mass rises to ~18 u!';
  }
};
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">At a Glance: Chapter 8 Master Map</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC8S16('models')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Models</button>
      <button onclick="setC8S16('particles')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Particles</button>
      <button onclick="setC8S16('shells')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Shells &amp; Valency</button>
      <button onclick="setC8S16('iso')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Isotopes &amp; Isobars</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c8s16_h" x="300" y="90" text-anchor="middle" fill="#fbbf24" font-size="18" font-weight="bold">Dalton &rarr; Thomson &rarr; Rutherford &rarr; Bohr &rarr; Quantum Cloud</text>
    <text id="c8s16_b1" x="300" y="126" text-anchor="middle" fill="#cbd5e1" font-size="13">Kanada (Parmanu) &amp; Democritus (Atomos) began atomic philosophy</text>
    <text id="c8s16_b2" x="300" y="156" text-anchor="middle" fill="#6ee7b7" font-size="13">Each experiment refined our model of the atom's interior!</text>
  </svg>
</div>
<script>
window.setC8S16 = function(k){
  const m = {
    models: ['Dalton -> Thomson -> Rutherford -> Bohr -> Quantum Cloud', 'Kanada (Parmanu) & Democritus (Atomos) began atomic philosophy', 'Each experiment refined our model of the atoms interior!'],
    particles: ['e- (-1, Thomson) | p+ (+1, Rutherford) | n0 (0, Chadwick)', 'Atomic Number Z = protons | Mass Number A = Z + n', 'IUPAC symbols: 1st letter Capital, 2nd lowercase (Fe, Au, Na, W)'],
    shells: ['Bohr-Bury 2n^2: K=2, L=8, M=18, N=32 (Outermost max = 8)', 'Valency = v (for 1-4 valence e-) or 8 - v (for 5-7 valence e-)', 'Stable Octet (8) or Helium Duplet (2) => Valency = 0'],
    iso: ['Isotopes: Same Z, Different A (1H/2H/3H; Cl avg = 35.5 u)', 'Isobars: Different Z, Same A (40-Ca, 40-K, 40-Ar)', 'Applications: U-235, Co-60 (cancer), I-131 (thyroid), C-14 (dating)']
  };
  document.getElementById('c8s16_h').textContent = m[k][0];
  document.getElementById('c8s16_b1').textContent = m[k][1];
  document.getElementById('c8s16_b2').textContent = m[k][2];
};
</script>"""
}

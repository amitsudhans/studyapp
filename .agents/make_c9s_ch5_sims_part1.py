#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Everyday Mixtures & Separation</span>
    <div class="flex gap-1.5">
      <button onclick="setMix1('sugar')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-600/30 text-amber-200 border border-amber-500/40">Sugarcane → Sugar</button>
      <button onclick="setMix1('blood')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-rose-600/30 text-rose-200 border border-rose-500/40">Blood Drop → Malaria</button>
    </div>
  </div>
  <svg viewBox="0 0 600 245" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="sim1_sugar">
      <rect x="65" y="65" width="120" height="110" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <text x="125" y="105" text-anchor="middle" fill="#fde68a" font-size="13" font-weight="bold">Sugarcane Juice</text>
      <text x="125" y="128" text-anchor="middle" fill="#94a3b8" font-size="11">Water + Sugar + Pulp</text>
      <line x1="195" y1="120" x2="255" y2="120" stroke="#fbbf24" stroke-width="3"/>
      <polygon points="260,120 248,113 248,127" fill="#fbbf24"/>
      <rect x="268" y="65" width="125" height="110" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <text x="330" y="105" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Clarify & Boil</text>
      <text x="330" y="128" text-anchor="middle" fill="#94a3b8" font-size="11">Crystallization</text>
      <line x1="403" y1="120" x2="455" y2="120" stroke="#34d399" stroke-width="3"/>
      <polygon points="460,120 448,113 448,127" fill="#34d399"/>
      <rect x="466" y="65" width="100" height="110" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
      <text x="516" y="105" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Pure Sugar</text>
      <text x="516" y="128" text-anchor="middle" fill="#cbd5e1" font-size="11">White Crystals</text>
    </g>
    <g id="sim1_blood" style="display:none">
      <circle cx="150" cy="125" r="55" fill="#450a0a" stroke="#f43f5e" stroke-width="2.5"/>
      <text x="150" y="122" text-anchor="middle" fill="#fda4af" font-size="13" font-weight="bold">Blood Drop</text>
      <text x="150" y="140" text-anchor="middle" fill="#cbd5e1" font-size="10">Plasma + RBCs + WBCs</text>
      <line x1="220" y1="125" x2="320" y2="125" stroke="#38bdf8" stroke-width="3"/>
      <polygon points="325,125 313,118 313,132" fill="#38bdf8"/>
      <text x="272" y="112" text-anchor="middle" fill="#7dd3fc" font-size="11">Smear / Spin</text>
      <rect x="335" y="70" width="210" height="110" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
      <text x="440" y="108" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Malaria Detection</text>
      <text x="440" y="132" text-anchor="middle" fill="#cbd5e1" font-size="11">Isolate RBCs / Parasites</text>
      <text x="440" y="152" text-anchor="middle" fill="#94a3b8" font-size="10">Microscopy & Paperfuge</text>
    </g>
  </svg>
</div>
<script>
window.setMix1 = function(k){
  document.getElementById('sim1_sugar').style.display = (k==='sugar'?'block':'none');
  document.getElementById('sim1_blood').style.display = (k==='blood'?'block':'none');
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Activity 5.1: Group A, B & C Laser Test</span>
    <div class="flex gap-1.5">
      <button onclick="setGrp2('A')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Group A: Salt</button>
      <button onclick="setGrp2('B')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Group B: Chalk</button>
      <button onclick="setGrp2('C')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Group C: Milk</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="40" y="110" width="75" height="26" rx="5" fill="#334155" stroke="#94a3b8"/>
    <text x="77" y="127" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">LASER</text>
    <rect x="200" y="55" width="160" height="145" rx="10" fill="#082f49" fill-opacity="0.55" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="115" y1="123" x2="200" y2="123" stroke="#ef4444" stroke-width="3"/>
    <line id="sim2_beam" x1="200" y1="123" x2="360" y2="123" stroke="#ef4444" stroke-width="2" stroke-opacity="0.1"/>
    <line x1="360" y1="123" x2="430" y2="123" stroke="#ef4444" stroke-width="3"/>
    <g id="sim2_sed" style="display:none" fill="#e2e8f0">
      <circle cx="230" cy="188" r="4"/><circle cx="255" cy="190" r="4"/><circle cx="280" cy="187" r="4"/><circle cx="310" cy="189" r="4"/><circle cx="335" cy="188" r="4"/>
    </g>
    <rect x="390" y="50" width="190" height="150" rx="10" fill="#0f172a" stroke="#334155"/>
    <text id="sim2_t" x="405" y="78" fill="#67e8f9" font-size="13" font-weight="bold">Group A: Salt Solution</text>
    <text id="sim2_v" x="405" y="106" fill="#cbd5e1" font-size="11">Visible particles: No</text>
    <text id="sim2_l" x="405" y="130" fill="#cbd5e1" font-size="11">Laser scattering: No</text>
    <text id="sim2_s" x="405" y="154" fill="#cbd5e1" font-size="11">Settles on standing: No</text>
    <text id="sim2_f" x="405" y="178" fill="#34d399" font-size="11">Filter residue: None</text>
  </svg>
</div>
<script>
window.setGrp2 = function(g){
  const map = {
    A: {op:'0.1', w:2, sed:'none', t:'Group A: Salt Solution', v:'Visible particles: No (<1 nm)', l:'Laser scattering: No', s:'Settles on standing: No', f:'Filter residue: None'},
    B: {op:'0.95', w:7, sed:'block', t:'Group B: Chalk Suspension', v:'Visible particles: Yes (>1000 nm)', l:'Laser scattering: Yes (while stirred)', s:'Settles on standing: Yes', f:'Filter residue: Chalk trapped'},
    C: {op:'0.95', w:6, sed:'none', t:'Group C: Milk Colloid', v:'Visible particles: No (1-1000 nm)', l:'Laser scattering: Yes (Tyndall)', s:'Settles on standing: No', f:'Filter residue: None'}
  }[g];
  const b = document.getElementById('sim2_beam');
  b.setAttribute('stroke-opacity', map.op); b.setAttribute('stroke-width', map.w);
  document.getElementById('sim2_sed').style.display = map.sed;
  document.getElementById('sim2_t').textContent = map.t;
  document.getElementById('sim2_v').textContent = map.v;
  document.getElementById('sim2_l').textContent = map.l;
  document.getElementById('sim2_s').textContent = map.s;
  document.getElementById('sim2_f').textContent = map.f;
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Concentration % Calculator</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Solute (g): <b id="sim3_sol" class="text-amber-300">20</b></label>
      <input type="range" min="5" max="50" step="5" value="20" oninput="updSim3(this.value)" class="w-32 accent-emerald-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="45" y="40" width="160" height="160" rx="12" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="125" y="68" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">% m/m (Mass/Mass)</text>
    <text id="sim3_mm_d" x="125" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">20 g solute + 80 g water</text>
    <text x="125" y="122" text-anchor="middle" fill="#94a3b8" font-size="10">Total Solution = 100 g</text>
    <text id="sim3_mm" x="125" y="162" text-anchor="middle" fill="#34d399" font-size="22" font-weight="bold">20.0%</text>

    <rect x="220" y="40" width="160" height="160" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="300" y="68" text-anchor="middle" fill="#fcd34d" font-size="13" font-weight="bold">% m/v (Medical IV)</text>
    <text id="sim3_mv_d" x="300" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">20 g in 200 mL soln</text>
    <text x="300" y="122" text-anchor="middle" fill="#94a3b8" font-size="10">e.g. 5% glucose / 0.9% saline</text>
    <text id="sim3_mv" x="300" y="162" text-anchor="middle" fill="#fbbf24" font-size="22" font-weight="bold">10.0%</text>

    <rect x="395" y="40" width="160" height="160" rx="12" fill="#0f172a" stroke="#a78bfa" stroke-width="2"/>
    <text x="475" y="68" text-anchor="middle" fill="#ddd6fe" font-size="13" font-weight="bold">% v/v (Liquids)</text>
    <text id="sim3_vv_d" x="475" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">20 mL in 250 mL soln</text>
    <text x="475" y="122" text-anchor="middle" fill="#94a3b8" font-size="10">Perfumes & Vinegar</text>
    <text id="sim3_vv" x="475" y="162" text-anchor="middle" fill="#c4b5fd" font-size="22" font-weight="bold">8.0%</text>
  </svg>
</div>
<script>
window.updSim3 = function(v){
  v = parseInt(v,10);
  document.getElementById('sim3_sol').textContent = v;
  document.getElementById('sim3_mm_d').textContent = v+' g solute + '+(100-v)+' g water';
  document.getElementById('sim3_mm').textContent = v.toFixed(1)+'%';
  document.getElementById('sim3_mv_d').textContent = v+' g in 200 mL soln';
  document.getElementById('sim3_mv').textContent = ((v/200)*100).toFixed(1)+'%';
  document.getElementById('sim3_vv_d').textContent = v+' mL in 250 mL soln';
  document.getElementById('sim3_vv').textContent = ((v/250)*100).toFixed(1)+'%';
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 5.2: Solubility vs Temperature</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Temp: <b id="sim4_t" class="text-cyan-300">40 °C</b></label>
      <input type="range" min="20" max="80" step="20" value="40" oninput="updSim4(this.value)" class="w-32 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="80" y1="200" x2="530" y2="200" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="200" x2="80" y2="30" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 100 175 L 230 140 L 360 95 L 490 45" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <text x="495" y="48" fill="#67e8f9" font-size="12" font-weight="bold">Solid A (↑)</text>
    <path d="M 100 155 L 230 148 L 360 142 L 490 135" fill="none" stroke="#34d399" stroke-width="3"/>
    <text x="495" y="138" fill="#6ee7b7" font-size="12" font-weight="bold">Solid B</text>
    <path d="M 100 80 L 230 115 L 360 145 L 490 172" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="495" y="176" fill="#fda4af" font-size="12" font-weight="bold">Gas (↓)</text>
    <line id="sim4_vl" x1="230" y1="35" x2="230" y2="200" stroke="#fbbf24" stroke-dasharray="4,4"/>
    <text id="sim4_read" x="300" y="32" text-anchor="middle" fill="#fde68a" font-size="12" font-weight="bold">At 40°C: Solid A = 45 g/100g | Gas solubility drops as T rises</text>
  </svg>
</div>
<script>
window.updSim4 = function(t){
  t = parseInt(t,10);
  document.getElementById('sim4_t').textContent = t + ' °C';
  const xMap = {20:100, 40:230, 60:360, 80:490};
  const aMap = {20:20, 40:45, 60:80, 80:115};
  document.getElementById('sim4_vl').setAttribute('x1', xMap[t]);
  document.getElementById('sim4_vl').setAttribute('x2', xMap[t]);
  document.getElementById('sim4_read').textContent = 'At '+t+'°C: Solid A = '+aMap[t]+' g/100g | Solid ↑ vs Gas ↓';
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Activity 5.3: Copper Sulfate Crystallization</span>
    <div class="flex gap-1.5">
      <button onclick="setCry5(1)" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200">1. Hot Water Bath</button>
      <button onclick="setCry5(2)" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">2. Filter Dirt</button>
      <button onclick="setCry5(3)" class="px-2 py-1 rounded bg-blue-600/30 text-xs text-blue-200">3. Cool Crystals</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="210" y="65" width="180" height="120" rx="12" fill="#082f49" stroke="#38bdf8" stroke-width="2.5"/>
    <g id="sim5_crys" style="display:none" fill="#3b82f6" stroke="#93c5fd" stroke-width="1.5">
      <polygon points="245,165 265,145 285,165 265,178"/>
      <polygon points="295,160 320,138 345,160 320,178"/>
      <polygon points="348,166 365,150 380,166 365,178"/>
    </g>
    <text id="sim5_title" x="300" y="42" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="bold">Step 1: Dissolve CuSO₄ + Drop of Dil. H₂SO₄ in Water Bath</text>
    <text id="sim5_sub" x="300" y="212" text-anchor="middle" fill="#cbd5e1" font-size="12">Natural Crystals: Rock Salt, Snowflakes, Quartz, Mawsmai Cave | Panga & Karkatch Salts</text>
  </svg>
</div>
<script>
window.setCry5 = function(step){
  const t = document.getElementById('sim5_title');
  const c = document.getElementById('sim5_crys');
  if(step===1){ t.textContent='Step 1: Dissolve CuSO₄ + Drop of Dil. H₂SO₄ in Water Bath'; c.style.display='none'; }
  else if(step===2){ t.textContent='Step 2: Filter Hot Saturated Solution to Remove Insoluble Dirt'; c.style.display='none'; }
  else { t.textContent='Step 3: Slow Undisturbed Cooling Yields Pure Blue Geometric Crystals!'; c.style.display='block'; }
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Distillation: Simple, Kannauj & Petroleum</span>
    <div class="flex gap-1.5">
      <button onclick="setDist6('simple')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">Simple (ΔT ≥ 25°C)</button>
      <button onclick="setDist6('ittar')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200">Kannauj Deg-Bhapka</button>
      <button onclick="setDist6('oil')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">Petroleum Tower</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="sim6_simple">
      <circle cx="150" cy="145" r="45" fill="#083344" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="150" y="150" text-anchor="middle" fill="#e2e8f0" font-size="11">Boiling Flask</text>
      <line x1="185" y1="115" x2="380" y2="145" stroke="#67e8f9" stroke-width="10" stroke-opacity="0.35"/>
      <line x1="185" y1="115" x2="380" y2="145" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="285" y="110" text-anchor="middle" fill="#7dd3fc" font-size="11">Liebig Condenser</text>
      <rect x="405" y="130" width="75" height="65" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
      <text x="442" y="167" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="bold">Distillate</text>
    </g>
    <g id="sim6_ittar" style="display:none">
      <rect x="75" y="65" width="450" height="125" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <text x="300" y="108" text-anchor="middle" fill="#fcd34d" font-size="16" font-weight="bold">Kannauj Traditional Deg-Bhapka Method</text>
      <text x="300" y="136" text-anchor="middle" fill="#cbd5e1" font-size="12">Copper Deg + Bamboo Condenser → Captures Mitti ka Ittar in Sandalwood Oil</text>
    </g>
    <g id="sim6_oil" style="display:none">
      <rect x="190" y="25" width="220" height="195" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
      <text x="300" y="50" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Top (Cool): LPG</text>
      <text x="300" y="80" text-anchor="middle" fill="#cbd5e1" font-size="12">Petrol (Gasoline)</text>
      <text x="300" y="110" text-anchor="middle" fill="#cbd5e1" font-size="12">Kerosene</text>
      <text x="300" y="140" text-anchor="middle" fill="#cbd5e1" font-size="12">Diesel</text>
      <text x="300" y="170" text-anchor="middle" fill="#cbd5e1" font-size="12">Lubricating Oil</text>
      <text x="300" y="200" text-anchor="middle" fill="#fda4af" font-size="12" font-weight="bold">Bottom (Hot): Bitumen</text>
    </g>
  </svg>
</div>
<script>
window.setDist6 = function(m){
  ['simple','ittar','oil'].forEach(k=>{
    document.getElementById('sim6_'+k).style.display=(k===m?'block':'none');
  });
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Paper Chromatography Strip</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Solvent Rise: <b id="sim7_p" class="text-amber-300">0%</b></label>
      <input type="range" min="0" max="100" value="0" oninput="updSim7(this.value)" class="w-36 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="240" y="25" width="120" height="190" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
    <rect x="200" y="185" width="200" height="35" fill="#0ea5e9" fill-opacity="0.35"/>
    <line x1="245" y1="172" x2="355" y2="172" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="372" y="176" fill="#cbd5e1" font-size="10">Pencil Baseline</text>
    <circle id="sim7_b1" cx="300" cy="172" r="7" fill="#ef4444"/>
    <circle id="sim7_b2" cx="300" cy="172" r="7" fill="#eab308"/>
    <circle id="sim7_b3" cx="300" cy="172" r="7" fill="#2563eb"/>
    <text x="115" y="105" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="bold">Water / 2% Salt</text>
    <text x="115" y="125" text-anchor="middle" fill="#94a3b8" font-size="11">Capillary Rise</text>
    <text x="485" y="105" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Different Speeds</text>
    <text x="485" y="125" text-anchor="middle" fill="#94a3b8" font-size="11">Separates Ink / Spinach</text>
  </svg>
</div>
<script>
window.updSim7 = function(pct){
  pct = parseInt(pct,10);
  document.getElementById('sim7_p').textContent = pct + '%';
  document.getElementById('sim7_b1').setAttribute('cy', 172 - pct*0.55);
  document.getElementById('sim7_b2').setAttribute('cy', 172 - pct*0.90);
  document.getElementById('sim7_b3').setAttribute('cy', 172 - pct*1.25);
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Separating Funnel: Mustard Oil & Water</span>
    <button onclick="drainSim8()" class="px-3 py-1 rounded-lg bg-cyan-600/30 text-cyan-200 border border-cyan-500/40 text-xs font-bold">Open / Reset Stopcock</button>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon points="220,40 380,40 315,145 285,145" fill="#0f172a" stroke="#94a3b8" stroke-width="2.5"/>
    <rect x="292" y="145" width="16" height="40" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
    <rect id="sim8_oil" x="242" y="55" width="116" height="42" rx="4" fill="#eab308" fill-opacity="0.8"/>
    <rect id="sim8_wat" x="268" y="97" width="64" height="45" rx="4" fill="#0ea5e9" fill-opacity="0.8"/>
    <text x="145" y="78" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">Mustard Oil (Top)</text>
    <text x="145" y="122" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Water (Bottom)</text>
    <rect x="260" y="190" width="80" height="40" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect id="sim8_beak" x="264" y="226" width="72" height="0" fill="#0ea5e9" fill-opacity="0.8"/>
    <text id="sim8_msg" x="470" y="120" text-anchor="middle" fill="#cbd5e1" font-size="12">Stopcock Closed</text>
  </svg>
</div>
<script>
(function(){
  let drained = false;
  window.drainSim8 = function(){
    drained = !drained;
    document.getElementById('sim8_wat').setAttribute('height', drained ? '0' : '45');
    document.getElementById('sim8_beak').setAttribute('y', drained ? '198' : '226');
    document.getElementById('sim8_beak').setAttribute('height', drained ? '28' : '0');
    document.getElementById('sim8_oil').setAttribute('y', drained ? '85' : '55');
    document.getElementById('sim8_msg').textContent = drained ? 'Water Drained! Oil Stays.' : 'Stopcock Closed';
  };
})();
</script>"""
}

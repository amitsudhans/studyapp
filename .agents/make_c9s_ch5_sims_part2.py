#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Sublimation & Alloys</span>
    <div class="flex gap-1.5">
      <button onclick="setSub9('heat')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Heat Camphor + Sand</button>
      <button onclick="setSub9('alloy')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Alloys (Solid Solns)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="sim9_sub">
      <polygon points="210,165 390,165 315,50 285,50" fill="#0f172a" stroke="#94a3b8" stroke-width="2.5"/>
      <ellipse cx="300" cy="175" rx="95" ry="18" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
      <text x="300" y="180" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="bold">Sand Remains in Dish</text>
      <circle cx="275" cy="95" r="5" fill="#f8fafc"/><circle cx="325" cy="95" r="5" fill="#f8fafc"/>
      <circle cx="262" cy="120" r="5" fill="#f8fafc"/><circle cx="338" cy="120" r="5" fill="#f8fafc"/>
      <text x="485" y="105" text-anchor="middle" fill="#7dd3fc" font-size="12" font-weight="bold">Camphor Deposits</text>
      <text x="485" y="123" text-anchor="middle" fill="#cbd5e1" font-size="11">Solid → Vapour → Solid</text>
    </g>
    <g id="sim9_alloy" style="display:none">
      <rect x="65" y="65" width="470" height="115" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <text x="300" y="102" text-anchor="middle" fill="#fcd34d" font-size="15" font-weight="bold">Alloys: Brass, Bronze & Stainless Steel</text>
      <text x="300" y="132" text-anchor="middle" fill="#cbd5e1" font-size="12">Melted & cooled into uniform solid solutions — NOT separable by physical methods!</text>
    </g>
  </svg>
</div>
<script>
window.setSub9 = function(m){
  document.getElementById('sim9_sub').style.display=(m==='heat'?'block':'none');
  document.getElementById('sim9_alloy').style.display=(m==='alloy'?'block':'none');
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Centrifugation & Paperfuge</span>
    <button onclick="spinSim10()" class="px-3 py-1 rounded-lg bg-rose-600/30 text-rose-200 border border-rose-500/40 text-xs font-bold">Spin Blood Sample</button>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="130" y="45" width="60" height="150" rx="14" fill="#450a0a" stroke="#94a3b8" stroke-width="2"/>
    <text x="160" y="215" text-anchor="middle" fill="#cbd5e1" font-size="11">Before Spin</text>
    <line x1="215" y1="120" x2="310" y2="120" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="315,120 303,113 303,127" fill="#38bdf8"/>
    <text x="262" y="106" text-anchor="middle" fill="#7dd3fc" font-size="11">Centrifuge / Paperfuge</text>
    <rect x="340" y="45" width="60" height="150" rx="14" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
    <rect id="sim10_pl" x="342" y="47" width="56" height="92" rx="10" fill="#fef08a" fill-opacity="0.85"/>
    <rect id="sim10_rbc" x="342" y="139" width="56" height="54" rx="10" fill="#dc2626"/>
    <text x="485" y="95" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="bold">Lighter Plasma (Top)</text>
    <text x="485" y="168" text-anchor="middle" fill="#fca5a5" font-size="12" font-weight="bold">Denser Cells (Bottom)</text>
  </svg>
</div>
<script>
window.spinSim10 = function(){
  const pl = document.getElementById('sim10_pl');
  const rbc = document.getElementById('sim10_rbc');
  const cur = pl.getAttribute('fill-opacity') === '0.85';
  pl.setAttribute('fill', cur ? '#450a0a' : '#fef08a');
  pl.setAttribute('fill-opacity', cur ? '0.9' : '0.85');
  rbc.setAttribute('fill', cur ? '#450a0a' : '#dc2626');
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Coagulation: Alum (Fitkari) & Paneer</span>
    <div class="flex gap-1.5">
      <button onclick="setCoag11(false)" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200">Muddy Water</button>
      <button onclick="setCoag11(true)" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">Add Alum (Fitkari)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect id="sim11_tank" x="180" y="45" width="240" height="150" rx="12" fill="#78350f" fill-opacity="0.7" stroke="#94a3b8" stroke-width="2.5"/>
    <g id="sim11_flocs" style="display:none" fill="#92400e">
      <circle cx="220" cy="180" r="8"/><circle cx="260" cy="182" r="9"/><circle cx="300" cy="181" r="10"/><circle cx="340" cy="182" r="8"/><circle cx="380" cy="180" r="9"/>
    </g>
    <text id="sim11_lbl" x="300" y="30" text-anchor="middle" fill="#fde68a" font-size="13" font-weight="bold">Fine Suspended Clay Stays Cloudy</text>
    <text x="300" y="220" text-anchor="middle" fill="#cbd5e1" font-size="11">Similar to Acid Curdling Milk Proteins to Make Paneer!</text>
  </svg>
</div>
<script>
window.setCoag11 = function(added){
  const t = document.getElementById('sim11_tank');
  const f = document.getElementById('sim11_flocs');
  const l = document.getElementById('sim11_lbl');
  t.setAttribute('fill', added ? '#082f49' : '#78350f');
  f.style.display = added ? 'block' : 'none';
  l.textContent = added ? 'Alum Clumps Fine Dirt → Rapid Sedimentation!' : 'Fine Suspended Clay Stays Cloudy';
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Colloids & Emulsions (1–1000 nm)</span>
    <span class="text-xs text-slate-400">Dispersed Phase + Dispersion Medium</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="40" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="162" y="70" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Colloid Properties</text>
    <text x="162" y="100" text-anchor="middle" fill="#cbd5e1" font-size="12">• Size: 1 nm to 1000 nm</text>
    <text x="162" y="126" text-anchor="middle" fill="#cbd5e1" font-size="12">• Does NOT settle on standing</text>
    <text x="162" y="152" text-anchor="middle" fill="#cbd5e1" font-size="12">• Passes through filter paper</text>
    <text x="162" y="178" text-anchor="middle" fill="#38bdf8" font-size="12">• Scatters light (Tyndall Effect)</text>

    <rect x="315" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="437" y="70" text-anchor="middle" fill="#fcd34d" font-size="14" font-weight="bold">Emulsions (Liquid-in-Liquid)</text>
    <text x="437" y="102" text-anchor="middle" fill="#cbd5e1" font-size="12">Milk, Butter & Vanishing Cream</text>
    <text x="437" y="132" text-anchor="middle" fill="#94a3b8" font-size="11">Other Colloids:</text>
    <text x="437" y="156" text-anchor="middle" fill="#cbd5e1" font-size="12">Blood, Ice Cream, Fog, Smoke</text>
  </svg>
</div>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Tyndall Effect & Table 5.1</span>
    <span class="text-xs text-slate-400">John Tyndall Light Scattering</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="30" y="25" width="540" height="190" rx="10" fill="#0f172a" stroke="#334155"/>
    <g font-size="11" font-weight="bold" fill="#7dd3fc">
      <text x="50" y="55">Mixture Type</text><text x="175" y="55">Size</text><text x="275" y="55">Filter?</text><text x="360" y="55">Settles?</text><text x="445" y="55">Tyndall?</text>
    </g>
    <line x1="40" y1="68" x2="560" y2="68" stroke="#334155"/>
    <g font-size="12" fill="#e2e8f0">
      <text x="50" y="100" fill="#38bdf8" font-weight="bold">True Solution</text><text x="175" y="100">&lt; 1 nm</text><text x="275" y="100">Passes</text><text x="360" y="100">No</text><text x="445" y="100" fill="#f43f5e">No</text>
      <text x="50" y="140" fill="#34d399" font-weight="bold">Colloid</text><text x="175" y="140">1–1000 nm</text><text x="275" y="140">Passes</text><text x="360" y="140">No</text><text x="445" y="140" fill="#34d399">Yes</text>
      <text x="50" y="180" fill="#fbbf24" font-weight="bold">Suspension</text><text x="175" y="180">&gt; 1000 nm</text><text x="275" y="180">Residue</text><text x="360" y="180">Yes</text><text x="445" y="180" fill="#34d399">Yes*</text>
    </g>
  </svg>
</div>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Applications in Nature & Society</span>
    <span class="text-xs text-slate-400">Body, Water & Circular Economy</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="35" y="30" width="165" height="82" rx="10" fill="#0f172a" stroke="#f43f5e"/>
    <text x="117" y="62" text-anchor="middle" fill="#fda4af" font-size="13" font-weight="bold">Kidney Filtration</text>
    <text x="117" y="84" text-anchor="middle" fill="#cbd5e1" font-size="10">Removes urea, keeps cells</text>

    <rect x="217" y="30" width="165" height="82" rx="10" fill="#0f172a" stroke="#38bdf8"/>
    <text x="300" y="62" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Sewage & Rivers</text>
    <text x="300" y="84" text-anchor="middle" fill="#cbd5e1" font-size="10">Screen, coagulate & filter</text>

    <rect x="400" y="30" width="165" height="82" rx="10" fill="#0f172a" stroke="#10b981"/>
    <text x="482" y="62" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Waste Segregation</text>
    <text x="482" y="84" text-anchor="middle" fill="#cbd5e1" font-size="10">Wet compost vs dry recycle</text>

    <rect x="115" y="132" width="370" height="78" rx="10" fill="#1e293b" stroke="#fbbf24"/>
    <text x="300" y="164" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="bold">Lithium-Ion Battery Recycling</text>
    <text x="300" y="188" text-anchor="middle" fill="#cbd5e1" font-size="11">Recovers Li, Co & Ni — cuts toxic e-waste & mining</text>
  </svg>
</div>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">The Journey Beyond & Artificial Blood</span>
    <span class="text-xs text-slate-400">Mini-Labs & Frontier</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="40" y="35" width="245" height="170" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="162" y="65" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Hands-On Mini-Labs</text>
    <text x="162" y="96" text-anchor="middle" fill="#cbd5e1" font-size="12">• Torchlight Tyndall Demo</text>
    <text x="162" y="122" text-anchor="middle" fill="#cbd5e1" font-size="12">• Hanging Thread Crystals</text>
    <text x="162" y="148" text-anchor="middle" fill="#cbd5e1" font-size="12">• Leaf & Candy Chromatography</text>
    <text x="162" y="174" text-anchor="middle" fill="#cbd5e1" font-size="12">• Outdoor Solar Still</text>

    <rect x="315" y="35" width="245" height="170" rx="12" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <text x="437" y="65" text-anchor="middle" fill="#fda4af" font-size="14" font-weight="bold">Artificial Blood Quest</text>
    <text x="437" y="98" text-anchor="middle" fill="#cbd5e1" font-size="12">PFC Emulsions & HBOCs</text>
    <text x="437" y="126" text-anchor="middle" fill="#94a3b8" font-size="11">Universal compatibility,</text>
    <text x="437" y="146" text-anchor="middle" fill="#94a3b8" font-size="11">no blood-group matching,</text>
    <text x="437" y="166" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Colloid Engineering!</text>
  </svg>
</div>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Chapter 5 At a Glance: Separation Map</span>
    <span class="text-xs text-slate-400">Ready for Quizzes 17–20</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="30" y="25" width="260" height="92" rx="10" fill="#0f172a" stroke="#06b6d4"/>
    <text x="160" y="50" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">Homogeneous (Solutions)</text>
    <text x="160" y="72" text-anchor="middle" fill="#cbd5e1" font-size="11">Crystallization • Distillation</text>
    <text x="160" y="92" text-anchor="middle" fill="#cbd5e1" font-size="11">Paper Chromatography • Alloys</text>

    <rect x="310" y="25" width="260" height="92" rx="10" fill="#0f172a" stroke="#10b981"/>
    <text x="440" y="50" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Heterogeneous Mixtures</text>
    <text x="440" y="72" text-anchor="middle" fill="#cbd5e1" font-size="11">Separating Funnel • Sublimation</text>
    <text x="440" y="92" text-anchor="middle" fill="#cbd5e1" font-size="11">Centrifugation • Coagulation</text>

    <rect x="55" y="134" width="490" height="84" rx="12" fill="#1e293b" stroke="#f59e0b"/>
    <text x="300" y="162" text-anchor="middle" fill="#fcd34d" font-size="13" font-weight="bold">Concentration & Light Scattering</text>
    <text x="300" y="188" text-anchor="middle" fill="#ffffff" font-size="12">% m/m, % m/v, % v/v  |  Colloids (1–1000 nm) = Tyndall Effect</text>
  </svg>
</div>"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 11 Simulators (Part 2: Slides 9-16)
High-fidelity responsive SVG interactive laboratory widgets.
"""

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Mode:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S9('external')" id="c11s9_btn_ext" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">External (Aquatic Frogs/Fish)</button>
        <button onclick="setC11S9('internal')" id="c11s9_btn_int" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Internal (Terrestrial Animals)</button>
        <button onclick="setC11S9('compare')" id="c11s9_btn_cmp" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Survival Analytics</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s9_tag">Pond Spawning &bull; High Gamete Mortality</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s9_display" class="w-full max-w-lg flex flex-col items-center">
      <svg id="c11s9_svg" viewBox="0 0 420 150" class="w-full h-36"></svg>
      <div id="c11s9_desc" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full"></div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>External: 10,000s of exposed eggs &bull; Internal: Few protected eggs inside maternal body.</span>
  </div>
</div>
<script>
window.setC11S9 = function(m){
  const btns = ['ext','int','cmp'];
  btns.forEach(b => { document.getElementById('c11s9_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s9_svg');
  const desc = document.getElementById('c11s9_desc');
  const tag = document.getElementById('c11s9_tag');

  if(m === 'external'){
    document.getElementById('c11s9_btn_ext').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Pond Spawning • High Gamete Mortality";
    svg.innerHTML = `
      <!-- Open pond water -->
      <rect x="50" y="20" width="320" height="110" rx="8" fill="#0369a1" opacity="0.3"/>
      <!-- Water waves -->
      <path d="M50,45 Q130,35 210,45 Q290,55 370,45" stroke="#38bdf8" stroke-width="2" fill="none"/>
      <!-- Gelatinous frog spawn egg mass -->
      <g transform="translate(100, 75)">
        <circle cx="0" cy="0" r="14" fill="#e0f2fe" opacity="0.6"/>
        <circle cx="0" cy="0" r="4" fill="#0f172a"/>
        <circle cx="20" cy="-5" r="14" fill="#e0f2fe" opacity="0.6"/>
        <circle cx="20" cy="-5" r="4" fill="#0f172a"/>
        <circle cx="10" cy="15" r="14" fill="#e0f2fe" opacity="0.6"/>
        <circle cx="10" cy="15" r="4" fill="#0f172a"/>
        <text x="-25" y="35" fill="#fde047" font-size="10">Spawn: 10,000+ Jelly Eggs</text>
      </g>
      <!-- Sperm cloud in water -->
      <g transform="translate(260, 65)">
        <circle cx="0" cy="0" r="2" fill="#fff"/><circle cx="15" cy="-8" r="2" fill="#fff"/><circle cx="-10" cy="15" r="2" fill="#fff"/>
        <path d="M0,0 Q-10,-5 -15,-2 M15,-8 Q25,-12 30,-8 M-10,15 Q-20,18 -25,12" stroke="#fff" stroke-width="1.2" fill="none"/>
        <text x="-30" y="35" fill="#bae6fd" font-size="10">Swimming Sperm Cloud</text>
      </g>
      <!-- Predator fish lurking -->
      <path d="M330,105 Q310,95 290,105 Q310,115 330,105 Z" fill="#ef4444"/>
      <text x="280" y="125" fill="#ef4444" font-size="9">Predator Hazard</text>
    `;
    desc.innerHTML = "<strong>External Fertilisation:</strong> Female frogs and bony fish shed thousands of soft, unfertilized eggs in open water. Males discharge sperm clouds externally. Water currents and predators cause heavy mortality (&lt;5% survive), necessitating massive gamete quantities.";
  } else if(m === 'internal'){
    document.getElementById('c11s9_btn_int').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Terrestrial Adaptation • Shielded Gestation";
    svg.innerHTML = `
      <!-- Protective egg / maternal womb shield -->
      <ellipse cx="210" cy="75" rx="80" ry="55" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
      <!-- Inner warm moist chamber -->
      <ellipse cx="210" cy="75" rx="65" ry="42" fill="#064e3b" opacity="0.5"/>
      <!-- Embryo safely developing inside -->
      <ellipse cx="210" cy="75" rx="25" ry="18" fill="#a7f3d0" stroke="#059669" stroke-width="1.5"/>
      <circle cx="200" cy="70" r="4" fill="#047857"/>
      <text x="180" y="78" fill="#047857" font-size="9">Embryo</text>
      <text x="160" y="25" fill="#10b981" font-size="11" font-weight="bold">Internal Maternal Chamber</text>
      <text x="145" y="125" fill="#6ee7b7" font-size="10">Sheltered from desiccation &amp; predators</text>
    `;
    desc.innerHTML = "<strong>Internal Fertilisation:</strong> Reptiles, birds, and mammals transfer sperm internally into the moist female tract. Sheltered from desiccation and external predators, embryos enjoy high survival rates (&gt;80%), allowing animals to produce far fewer eggs.";
  } else {
    document.getElementById('c11s9_btn_cmp').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Survival Probability &amp; Resource Investment";
    svg.innerHTML = `
      <!-- Bar comparison -->
      <text x="60" y="45" fill="#38bdf8" font-size="11" font-weight="bold">External (Frog)</text>
      <rect x="160" y="32" width="200" height="16" rx="3" fill="#0284c7"/>
      <text x="170" y="44" fill="#fff" font-size="10 font-weight="bold">Gamete Count: 20,000 | Survival: 2%</text>

      <text x="60" y="95" fill="#10b981" font-size="11" font-weight="bold">Internal (Bird/Mammal)</text>
      <rect x="160" y="82" width="60" height="16" rx="3" fill="#059669"/>
      <text x="230" y="94" fill="#a7f3d0" font-size="10 font-weight="bold">Gamete Count: 1-5 | Survival: 85%</text>
    `;
    desc.innerHTML = "<strong>Evolutionary Trade-off:</strong> External aquatic breeders spend energy making thousands of cheap eggs. Terrestrial internal breeders make very few eggs but invest heavily in shells, placental nutrition, and maternal protection.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S9('external'));
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Strategy:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S10('table')" id="c11s10_btn_tab" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Table 11.4 Spectrum</button>
        <button onclick="setC11S10('meta')" id="c11s10_btn_meta" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Tadpole Metamorphosis</button>
        <button onclick="setC11S10('viviparity')" id="c11s10_btn_vivi" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Mammalian Viviparity</button>
      </div>
    </div>
    <span class="text-xs text-cyan-300 font-semibold" id="c11s10_tag">Comparative Animal Strategies</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s10_content" class="w-full max-w-xl"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Yolk-limited eggs require feeding larvae; yolk-rich cleidoic eggs support direct development.</span>
  </div>
</div>
<script>
window.setC11S10 = function(mode){
  const btns = ['tab','meta','vivi'];
  btns.forEach(b => { document.getElementById('c11s10_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const c = document.getElementById('c11s10_content');
  const tag = document.getElementById('c11s10_tag');

  if(mode === 'table'){
    document.getElementById('c11s10_btn_tab').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Textbook Table 11.4 Animal Comparison";
    c.innerHTML = `
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border border-slate-800 rounded-lg">
          <thead class="bg-slate-900 text-slate-300">
            <tr>
              <th class="p-2 border-b border-slate-800">Animal</th>
              <th class="p-2 border-b border-slate-800">Fertilisation</th>
              <th class="p-2 border-b border-slate-800">Egg Count</th>
              <th class="p-2 border-b border-slate-800">Survival / Strategy</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 text-slate-400">
            <tr><td class="p-2 font-semibold text-cyan-300">Fish</td><td class="p-2">External (Water)</td><td class="p-2">100s – 1,000s</td><td class="p-2 text-rose-400">Low (Predator losses)</td></tr>
            <tr><td class="p-2 font-semibold text-emerald-300">Frog</td><td class="p-2">External (Water)</td><td class="p-2">5,000 – 50,000</td><td class="p-2 text-amber-400">Low (Larval metamorphosis)</td></tr>
            <tr><td class="p-2 font-semibold text-amber-300">Lizard</td><td class="p-2">Internal (Land)</td><td class="p-2">2 – 20</td><td class="p-2 text-yellow-300">Moderate (Leathery cleidoic eggs)</td></tr>
            <tr><td class="p-2 font-semibold text-purple-300">Bird</td><td class="p-2">Internal (Land)</td><td class="p-2">1 – 15</td><td class="p-2 text-emerald-400">High (Hard shell, incubation)</td></tr>
          </tbody>
        </table>
      </div>
    `;
  } else if(mode === 'meta'){
    document.getElementById('c11s10_btn_meta').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Frog Larval Metamorphosis";
    c.innerHTML = `
      <div class="flex items-center justify-around w-full py-2">
        <div class="flex flex-col items-center">
          <circle cx="20" cy="20" r="12" fill="#0369a1"/>
          <span class="text-xs font-bold text-sky-400">1. Egg</span>
          <span class="text-[10px] text-slate-400">Yolk-limited</span>
        </div>
        <span class="text-amber-400 font-bold">&rarr;</span>
        <div class="flex flex-col items-center">
          <span class="text-lg">🐟</span>
          <span class="text-xs font-bold text-emerald-400">2. Tadpole</span>
          <span class="text-[10px] text-slate-400">Gills, tail, grazes algae</span>
        </div>
        <span class="text-amber-400 font-bold">&rarr;</span>
        <div class="flex flex-col items-center">
          <span class="text-lg">🐸</span>
          <span class="text-xs font-bold text-lime-400">3. Adult Frog</span>
          <span class="text-[10px] text-slate-400">Lungs, legs, carnivorous</span>
        </div>
      </div>
      <div class="p-2 mt-2 rounded-lg bg-slate-900 border border-slate-800 text-center text-xs text-emerald-300">
        Thyroxine hormone triggers metamorphosis: tail resorbs, lungs develop, limbs emerge for terrestrial life.
      </div>
    `;
  } else {
    document.getElementById('c11s10_btn_vivi').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Placental Viviparity & Parental Care";
    c.innerHTML = `
      <div class="space-y-2 text-xs">
        <div class="p-2 rounded-lg bg-purple-950/40 border border-purple-800/60 flex items-center justify-between">
          <span class="font-bold text-purple-300">Internal Gestation (Womb):</span>
          <span class="text-slate-300">Placental nourishment shields foetus from all external hazards</span>
        </div>
        <div class="p-2 rounded-lg bg-purple-950/40 border border-purple-800/60 flex items-center justify-between">
          <span class="font-bold text-purple-300">Mammary Lactation:</span>
          <span class="text-slate-300">Breast milk delivers ideal nutrition, antibodies, and enzymes</span>
        </div>
        <div class="p-2 rounded-lg bg-purple-950/40 border border-purple-800/60 flex items-center justify-between">
          <span class="font-bold text-purple-300">Extended Parental Care:</span>
          <span class="text-slate-300">Guarantees highest infant survival rate in animal kingdom</span>
        </div>
      </div>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S10('table'));
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Scrotum Temp:</span>
      <input type="range" id="c11s11_slider" min="32" max="38" step="0.5" value="34.5" oninput="updateC11S11(this.value)" class="w-24 accent-cyan-400">
      <span class="text-xs font-mono font-bold text-white px-2 py-0.5 rounded bg-slate-800" id="c11s11_t_disp">34.5°C</span>
    </div>
    <span class="text-xs font-semibold" id="c11s11_status_tag">Optimal Spermatogenesis (2.5°C below core)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg viewBox="0 0 420 150" class="w-full h-36">
      <!-- Body core boundary -->
      <line x1="80" y1="90" x2="340" y2="90" stroke="#475569" stroke-dasharray="4,4" stroke-width="1.5"/>
      <text x="90" y="80" fill="#94a3b8" font-size="10">Core Body Cavity (37.0°C)</text>
      <!-- Extra-abdominal Scrotum Pouch -->
      <path d="M170,90 Q170,140 210,140 Q250,140 250,90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <!-- Paired Testes inside Scrotum -->
      <ellipse id="c11s11_testis" cx="210" cy="115" rx="20" ry="15" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
      <text x="195" y="118" fill="#fff" font-size="9" font-weight="bold">Testis</text>
      <!-- Vas Deferens loop ascending into abdomen -->
      <path d="M210,100 Q210,40 260,35 Q300,35 300,70" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="220" y="30" fill="#f59e0b" font-size="10">Vas Deferens</text>
      <!-- Accessory Gland: Prostate & Seminal Vesicle -->
      <circle cx="300" cy="70" r="10" fill="#a855f7" stroke="#c084fc" stroke-width="1.5"/>
      <text x="315" y="73" fill="#c084fc" font-size="9">Prostate &amp; Seminal Vesicles</text>
      <!-- Sperm morphology callout -->
      <g transform="translate(60, 20)">
        <ellipse cx="20" cy="15" rx="8" ry="5" fill="#38bdf8"/>
        <line x1="28" y1="15" x2="36" y2="15" stroke="#f59e0b" stroke-width="3"/>
        <path d="M36,15 Q46,10 56,20" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
        <text x="0" y="35" fill="#38bdf8" font-size="9">Head (DNA)</text>
        <text x="32" y="35" fill="#f59e0b" font-size="9">Mid (ATP)</text>
        <text x="60" y="35" fill="#93c5fd" font-size="9">Tail</text>
      </g>
    </svg>
    <div id="c11s11_desc" class="p-2 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Leydig cells in testes secrete testosterone; Seminal vesicle fructose fuels sperm tail motility.</span>
  </div>
</div>
<script>
window.updateC11S11 = function(t){
  t = parseFloat(t);
  document.getElementById('c11s11_t_disp').textContent = t.toFixed(1) + '°C';
  const tag = document.getElementById('c11s11_status_tag');
  const testis = document.getElementById('c11s11_testis');
  const desc = document.getElementById('c11s11_desc');

  if(t >= 34.0 && t <= 35.0){
    tag.className = 'text-xs font-semibold text-emerald-400';
    tag.textContent = 'Optimal Spermatogenesis (2.0–2.5°C below core 37°C)';
    testis.setAttribute('fill', '#059669');
    desc.innerHTML = "<strong>Normal Scrotal Physiology:</strong> At 34.5°C, the scrotal pouch provides the cool environment required by germ cells to synthesize hundreds of millions of healthy, motile sperm.";
  } else if(t > 35.5){
    tag.className = 'text-xs font-semibold text-rose-400';
    tag.textContent = 'Too Warm: Thermal Inhibition of Sperm Synthesis';
    testis.setAttribute('fill', '#dc2626');
    desc.innerHTML = "<strong>Heat Stress Alert:</strong> If testes are exposed to normal core body temperature (37°C) or higher, sperm synthesis drops precipitously, demonstrating why testes must be extra-abdominal.";
  } else {
    tag.className = 'text-xs font-semibold text-sky-400';
    tag.textContent = 'Cool Temperature: Scrotal muscles contract to warm testes';
    testis.setAttribute('fill', '#0284c7');
    desc.innerHTML = "<strong>Thermoregulation:</strong> Dartos and cremaster muscles contract, pulling testes closer to the pelvic body wall to conserve warmth.";
  }
};
window.addEventListener('DOMContentLoaded', () => updateC11S11(34.5));
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Inspect:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S12('organs')" id="c11s12_btn_org" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Female Anatomy</button>
        <button onclick="setC11S12('asymmetry')" id="c11s12_btn_asym" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Gamete Asymmetry (Table 11.5)</button>
      </div>
    </div>
    <span class="text-xs text-rose-300 font-semibold" id="c11s12_tag">Ovaries, Oviducts &amp; Muscular Uterus</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s12_view_org" class="w-full max-w-lg flex flex-col items-center">
      <svg viewBox="0 0 420 150" class="w-full h-36">
        <!-- Muscular Uterus -->
        <path d="M170,50 Q210,35 250,50 L240,110 Q210,120 180,110 Z" fill="#881337" stroke="#e11d48" stroke-width="2"/>
        <text x="195" y="80" fill="#fecdd3" font-size="10" font-weight="bold">Uterus</text>
        <!-- Endometrium lining -->
        <path d="M185,55 Q210,48 235,55 L230,95 Q210,102 190,95 Z" fill="#fda4af" opacity="0.3"/>
        <!-- Cervix & Vagina -->
        <rect x="198" y="112" width="24" height="25" fill="#4c0519" stroke="#e11d48"/>
        <text x="228" y="125" fill="#fda4af" font-size="9">Cervix/Vagina</text>
        <!-- Left Fallopian Tube -->
        <path d="M170,55 Q130,30 90,55" fill="none" stroke="#fb7185" stroke-width="4"/>
        <ellipse cx="85" cy="60" rx="10" ry="7" fill="#f43f5e"/>
        <!-- Left Ovary -->
        <ellipse cx="85" cy="78" rx="15" ry="11" fill="#be123c" stroke="#fb7185" stroke-width="1.5"/>
        <text x="45" y="82" fill="#f43f5e" font-size="10">Ovary (Left)</text>
        <!-- Right Fallopian Tube -->
        <path d="M250,55 Q290,30 330,55" fill="none" stroke="#fb7185" stroke-width="4"/>
        <ellipse cx="335" cy="60" rx="10" ry="7" fill="#f43f5e"/>
        <!-- Right Ovary -->
        <ellipse cx="335" cy="78" rx="15" ry="11" fill="#be123c" stroke="#fb7185" stroke-width="1.5"/>
        <text x="355" y="82" fill="#f43f5e" font-size="10">Ovary (Right)</text>
      </svg>
      <div class="p-2 mt-1 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full">
        <strong>Ovaries:</strong> Release 1 ovum/month and synthesize estrogen &amp; progesterone. <strong>Fallopian Tube:</strong> Site of fertilisation. <strong>Uterus:</strong> Muscular womb where blastocyst implants.
      </div>
    </div>

    <div id="c11s12_view_asym" class="hidden w-full max-w-xl">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border border-slate-800 rounded-lg">
          <thead class="bg-slate-900 text-slate-300">
            <tr>
              <th class="p-2 border-b border-slate-800">Parameter</th>
              <th class="p-2 border-b border-slate-800 text-cyan-400">Male Sperm</th>
              <th class="p-2 border-b border-slate-800 text-rose-400">Female Ovum (Egg)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 text-slate-400">
            <tr><td class="p-2 font-semibold text-slate-300">Size</td><td class="p-2">Microscopic (~60 &mu;m)</td><td class="p-2 text-rose-300">Macroscopic (~120 &mu;m diameter)</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Motility</td><td class="p-2 text-cyan-300">Highly motile (flagellar tail)</td><td class="p-2 text-slate-400">Non-motile (swept by tube cilia)</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Quantity</td><td class="p-2 text-amber-300">100–300 million per ejaculate</td><td class="p-2 text-emerald-400">1 single egg per 28-day cycle</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Nutrients</td><td class="p-2">Minimal (streamlined for speed)</td><td class="p-2 text-yellow-300">Abundant yolk &amp; mitochondria</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Human ovum contains thousands of maternal mitochondria that fuel all early embryonic cell divisions.</span>
  </div>
</div>
<script>
window.setC11S12 = function(v){
  const vo = document.getElementById('c11s12_view_org');
  const va = document.getElementById('c11s12_view_asym');
  const bo = document.getElementById('c11s12_btn_org');
  const ba = document.getElementById('c11s12_btn_asym');
  const tag = document.getElementById('c11s12_tag');

  if(v === 'organs'){
    vo.classList.remove('hidden'); va.classList.add('hidden');
    bo.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    ba.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    tag.textContent = "Ovaries, Oviducts & Muscular Uterus";
  } else {
    vo.classList.add('hidden'); va.classList.remove('hidden');
    ba.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
    bo.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    tag.textContent = "Table 11.5 Gamete Asymmetry Comparison";
  }
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Timeline:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S13(0)" id="c11s13_btn_0" class="px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Day 0: Ovulation</button>
        <button onclick="setC11S13(1)" id="c11s13_btn_1" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Day 1: Fertilisation</button>
        <button onclick="setC11S13(3)" id="c11s13_btn_3" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Day 3: Cleavage</button>
        <button onclick="setC11S13(6)" id="c11s13_btn_6" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Day 6: Implantation</button>
        <button onclick="setC11S13('ivf')" id="c11s13_btn_ivf" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">IVF Landmark</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s13_tag">Day 0: Follicle Rupture &amp; Ovulation</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg id="c11s13_svg" viewBox="0 0 420 150" class="w-full h-36"></svg>
    <div id="c11s13_details" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>India's first IVF baby, Durga (Kanupriya Agarwal), was created by Subhash Mukhopadhyay in Kolkata in October 1978!</span>
  </div>
</div>
<script>
window.setC11S13 = function(d){
  const btns = ['0','1','3','6','ivf'];
  btns.forEach(b => { document.getElementById('c11s13_btn_' + b).className = 'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s13_svg');
  const det = document.getElementById('c11s13_details');
  const tag = document.getElementById('c11s13_tag');

  if(d === 0){
    document.getElementById('c11s13_btn_0').className = 'px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Day 0: Follicle Rupture & Ovulation";
    svg.innerHTML = `
      <!-- Ovary & released egg entering oviduct -->
      <ellipse cx="100" cy="80" rx="30" ry="20" fill="#be123c"/>
      <circle cx="140" cy="70" r="8" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>
      <path d="M150,70 L200,65" stroke="#fb7185" stroke-width="3" stroke-dasharray="3,3"/>
      <path d="M190,40 Q250,30 320,60" stroke="#f43f5e" stroke-width="6" fill="none"/>
      <text x="60" y="50" fill="#fda4af" font-size="10">Ovary</text>
      <text x="120" y="95" fill="#fde047" font-size="10 font-weight="bold">Ovulated Egg (n)</text>
    `;
    det.innerHTML = "<strong>Day 0 - Ovulation:</strong> Mid-cycle LH surge triggers rupture of the mature ovarian follicle, releasing a secondary oocyte into the fallopian tube.";
  } else if(d === 1){
    document.getElementById('c11s13_btn_1').className = 'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Day 1: Syngamy (Fertilisation) in Fallopian Tube";
    svg.innerHTML = `
      <!-- Egg in ampulla surrounded by swimming sperm -->
      <circle cx="210" cy="70" r="22" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>
      <text x="195" y="74" fill="#78350f" font-size="10" font-weight="bold">Zygote (2n)</text>
      <!-- Penetrating sperm -->
      <path d="M160,70 L188,70" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="188" cy="70" r="3" fill="#38bdf8"/>
      <!-- Other sperm bouncing off block -->
      <path d="M245,50 L233,60" stroke="#94a3b8" stroke-width="1.5"/><circle cx="233" cy="60" r="2" fill="#94a3b8"/>
      <text x="130" y="40" fill="#38bdf8" font-size="10 font-weight="bold">Sperm Nucleus Enters</text>
      <text x="220" y="115" fill="#ca8a04" font-size="10">Cortical Reaction blocks polyspermy</text>
    `;
    det.innerHTML = "<strong>Day 1 - Fertilisation:</strong> A single sperm fuses with the egg membrane. Nuclear fusion restores the diploid count (46 chromosomes), forming the single-cell zygote.";
  } else if(d === 3){
    document.getElementById('c11s13_btn_3').className = 'px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Day 3–4: Mitotic Cleavage (2 &rarr; 4 &rarr; 8 Cells)";
    svg.innerHTML = `
      <!-- Cleavage dividing cells -->
      <circle cx="210" cy="70" r="24" fill="none" stroke="#ca8a04" stroke-width="2"/>
      <circle cx="200" cy="60" r="10" fill="#4ade80" stroke="#16a34a"/>
      <circle cx="220" cy="60" r="10" fill="#4ade80" stroke="#16a34a"/>
      <circle cx="200" cy="80" r="10" fill="#4ade80" stroke="#16a34a"/>
      <circle cx="220" cy="80" r="10" fill="#4ade80" stroke="#16a34a"/>
      <text x="150" y="115" fill="#4ade80" font-size="11" font-weight="bold">Morula (Solid Ball of Dividing Cells)</text>
    `;
    det.innerHTML = "<strong>Day 3–4 - Mitotic Cleavage:</strong> Zygote divides rapidly into 2, 4, 8, and 16 cells without increasing in overall volume, propelled toward the uterus by oviduct cilia.";
  } else if(d === 6){
    document.getElementById('c11s13_btn_6').className = 'px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Day 6–7: Blastocyst Implantation in Endometrium";
    svg.innerHTML = `
      <!-- Uterine endometrial wall -->
      <rect x="50" y="30" width="100" height="90" fill="#881337" opacity="0.6" stroke="#e11d48" stroke-width="2"/>
      <text x="60" y="75" fill="#fecdd3" font-size="10">Uterine Endometrium</text>
      <!-- Blastocyst embedding -->
      <circle cx="160" cy="75" r="22" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
      <!-- Inner cell mass -->
      <circle cx="150" cy="75" r="8" fill="#c084fc"/>
      <!-- Trophoblast invading wall -->
      <path d="M140,65 L135,62 M140,75 L130,75 M140,85 L135,88" stroke="#e11d48" stroke-width="2"/>
      <text x="190" y="70" fill="#c084fc" font-size="11" font-weight="bold">Blastocyst Embedding</text>
      <text x="190" y="90" fill="#a855f7" font-size="10">Initiates Clinical Pregnancy</text>
    `;
    det.innerHTML = "<strong>Day 6–7 - Implantation:</strong> The hollow blastocyst embeds into the vascular endometrial wall. Trophoblast cells initiate placental formation and secrete hCG hormone.";
  } else {
    document.getElementById('c11s13_btn_ivf').className = 'px-2 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
    tag.textContent = "In-Vitro Fertilisation & Subhash Mukhopadhyay";
    svg.innerHTML = `
      <!-- Petri dish illustration -->
      <ellipse cx="210" cy="75" rx="90" ry="35" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <ellipse cx="210" cy="75" rx="80" ry="30" fill="#0284c7" opacity="0.2"/>
      <circle cx="210" cy="75" r="10" fill="#fde047"/>
      <text x="120" y="45" fill="#38bdf8" font-size="11" font-weight="bold">IVF: In-Vitro Petri Dish Fertilisation</text>
      <text x="135" y="125" fill="#fde047" font-size="10 font-weight="bold">Kanupriya Agarwal ('Durga') &bull; Kolkata 1978</text>
    `;
    det.innerHTML = "<strong>IVF Tribute:</strong> In cases of infertility, ova and sperm are fertilized outside the body in sterile dishes. Subhash Mukhopadhyay created India's first test-tube baby, Kanupriya Agarwal (Durga), in October 1978!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S13(0));
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Focus:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S14('cycle')" id="c11s14_btn_cyc" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">28-Day Menstrual Cycle</button>
        <button onclick="setC11S14('sex')" id="c11s14_btn_sex" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Sex Determination (XX vs XY)</button>
      </div>
    </div>
    <span class="text-xs text-rose-300 font-semibold" id="c11s14_tag">Phases of 28-Day Cycle</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s14_view_cyc" class="w-full max-w-lg flex flex-col items-center">
      <div class="grid grid-cols-4 gap-2 w-full text-center text-xs">
        <div class="p-2.5 rounded-xl bg-rose-950/50 border border-rose-800/60">
          <span class="text-xs font-bold text-rose-300 block">Days 1–5</span>
          <span class="text-[11px] font-semibold text-rose-400">Menstruation</span>
          <p class="text-[9px] text-slate-400 mt-1">Endometrial lining breaks down &amp; sheds</p>
        </div>
        <div class="p-2.5 rounded-xl bg-sky-950/50 border border-sky-800/60">
          <span class="text-xs font-bold text-sky-300 block">Days 6–13</span>
          <span class="text-[11px] font-semibold text-sky-400">Follicular</span>
          <p class="text-[9px] text-slate-400 mt-1">Estrogen rebuilds vascular uterine wall</p>
        </div>
        <div class="p-2.5 rounded-xl bg-amber-950/50 border border-amber-800/60">
          <span class="text-xs font-bold text-amber-300 block">Day 14</span>
          <span class="text-[11px] font-semibold text-amber-400">Ovulation</span>
          <p class="text-[9px] text-slate-400 mt-1">LH surge causes egg release from ovary</p>
        </div>
        <div class="p-2.5 rounded-xl bg-purple-950/50 border border-purple-800/60">
          <span class="text-xs font-bold text-purple-300 block">Days 15–28</span>
          <span class="text-[11px] font-semibold text-purple-400">Luteal</span>
          <p class="text-[9px] text-slate-400 mt-1">Progesterone maintains lining for embryo</p>
        </div>
      </div>
      <div class="p-2.5 mt-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 text-center w-full">
        If fertilisation does not occur within 24 hours, the ovum degenerates and progesterone plunges, triggering menstruation again on Day 28!
      </div>
    </div>

    <div id="c11s14_view_sex" class="hidden w-full max-w-lg flex flex-col items-center space-y-3">
      <div class="flex items-center justify-around w-full">
        <div class="p-2 rounded-xl bg-rose-950/40 border border-rose-800 text-center">
          <span class="text-xs font-bold text-rose-300">Mother (XX)</span>
          <span class="text-[10px] block text-slate-400 mt-1">Only produces:</span>
          <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 text-xs font-bold">X Eggs (100%)</span>
        </div>
        <div class="text-xl font-bold text-slate-400">&times;</div>
        <div class="p-2 rounded-xl bg-blue-950/40 border border-blue-800 text-center">
          <span class="text-xs font-bold text-blue-300">Father (XY)</span>
          <span class="text-[10px] block text-slate-400 mt-1">Produces:</span>
          <div class="flex gap-1 mt-1">
            <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 text-xs font-bold">50% X Sperm</span>
            <span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 text-xs font-bold">50% Y Sperm</span>
          </div>
        </div>
      </div>
      <div class="grid grid-cols-2 gap-3 w-full">
        <div class="p-2.5 rounded-xl bg-slate-900 border border-rose-900 text-center">
          <span class="text-xs font-bold text-rose-400">X (Mother) + X (Father)</span>
          <span class="text-sm font-bold text-white block mt-1">XX &rarr; Female Girl (50%)</span>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-blue-900 text-center">
          <span class="text-xs font-bold text-blue-400">X (Mother) + Y (Father)</span>
          <span class="text-sm font-bold text-white block mt-1">XY &rarr; Male Boy (50%)</span>
        </div>
      </div>
      <p class="text-xs text-amber-300 font-semibold text-center">The father's sperm scientifically determines biological sex, dispelling false social superstitions!</p>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Menstrual Hygiene: Use sanitary pads/tampons/cups, change every 4–6 hours, and dispose responsibly.</span>
  </div>
</div>
<script>
window.setC11S14 = function(m){
  const vc = document.getElementById('c11s14_view_cyc');
  const vs = document.getElementById('c11s14_view_sex');
  const bc = document.getElementById('c11s14_btn_cyc');
  const bs = document.getElementById('c11s14_btn_sex');
  const tag = document.getElementById('c11s14_tag');

  if(m === 'cycle'){
    vc.classList.remove('hidden'); vs.classList.add('hidden');
    bc.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    bs.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    tag.textContent = "Phases of 28-Day Cycle";
  } else {
    vc.classList.add('hidden'); vs.classList.remove('hidden');
    bs.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    bc.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    tag.textContent = "Chromosomal Sex Determination (XX vs XY)";
  }
};
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Trimester:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S15(1)" id="c11s15_btn_1" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">1st (Months 1–3)</button>
        <button onclick="setC11S15(2)" id="c11s15_btn_2" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2nd (Months 4–6)</button>
        <button onclick="setC11S15(3)" id="c11s15_btn_3" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3rd (Months 7–9)</button>
        <button onclick="setC11S15('asha')" id="c11s15_btn_ash" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">ASHA Health Care</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s15_tag">1st Trimester: Organogenesis &bull; Foetus at Wk 9</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg id="c11s15_svg" viewBox="0 0 420 150" class="w-full h-36"></svg>
    <div id="c11s15_desc" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>National Health Mission: 10+ lakh ASHA workers promote safe hospital deliveries and infant vaccination.</span>
  </div>
</div>
<script>
window.setC11S15 = function(t){
  const btns = ['1','2','3','ash'];
  btns.forEach(b => { document.getElementById('c11s15_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s15_svg');
  const desc = document.getElementById('c11s15_desc');
  const tag = document.getElementById('c11s15_tag');

  if(t === 1){
    document.getElementById('c11s15_btn_1').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "1st Trimester: Organogenesis • Foetus at Week 9";
    svg.innerHTML = `
      <!-- Disc placenta & early embryo -->
      <path d="M120,40 Q150,20 180,40" stroke="#ef4444" stroke-width="6"/>
      <line x1="150" y1="35" x2="200" y2="75" stroke="#f59e0b" stroke-width="3"/>
      <!-- Small embryo -->
      <circle cx="210" cy="80" r="14" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
      <circle cx="206" cy="76" r="3" fill="#047857"/>
      <text x="110" y="20" fill="#ef4444" font-size="10 font-weight="bold">Placental Disc</text>
      <text x="235" y="80" fill="#34d399" font-size="11" font-weight="bold">Embryo &rarr; Foetus (Week 9)</text>
      <text x="235" y="98" fill="#94a3b8" font-size="9">Heart beats, limbs bud, organs form</text>
    `;
    desc.innerHTML = "<strong>1st Trimester (Months 1–3):</strong> Intensive organogenesis! The placenta forms, delivering O2 and nutrients without mixing maternal-foetal blood. By week 9, all major organs exist, designating it a foetus.";
  } else if(t === 2){
    document.getElementById('c11s15_btn_2').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "2nd Trimester: Rapid Growth & Quickening";
    svg.innerHTML = `
      <!-- Developing foetus -->
      <ellipse cx="210" cy="75" rx="35" ry="25" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
      <circle cx="190" cy="65" r="12" fill="#6ee7b7"/>
      <path d="M225,85 Q245,100 240,110" stroke="#059669" stroke-width="3"/>
      <text x="140" y="30" fill="#10b981" font-size="11" font-weight="bold">Rapid Skeletal Growth &amp; Movements</text>
      <text x="160" y="125" fill="#fde047" font-size="10">Mother feels 'quickening' movements</text>
    `;
    desc.innerHTML = "<strong>2nd Trimester (Months 4–6):</strong> Bones ossify, eyebrows and eyelashes appear, and the mother actively detects foetal limb movements ('quickening').";
  } else if(t === 3){
    document.getElementById('c11s15_btn_3').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "3rd Trimester & Parturition (Birth)";
    svg.innerHTML = `
      <!-- Full-term baby upside down towards cervix -->
      <ellipse cx="210" cy="75" rx="45" ry="32" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
      <circle cx="210" cy="115" r="16" fill="#6ee7b7"/>
      <text x="140" y="25" fill="#f59e0b" font-size="11" font-weight="bold">Lung &amp; Brain Maturation</text>
      <text x="150" y="145" fill="#fbbf24" font-size="10">Uterine contractions initiate childbirth</text>
    `;
    desc.innerHTML = "<strong>3rd Trimester (Months 7–9):</strong> Lungs manufacture surfactant and the brain expands rapidly. Rhythmic oxytocin contractions of the uterine muscle push the baby through the cervix and birth canal.";
  } else {
    document.getElementById('c11s15_btn_ash').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "ASHA Community Health Workers (NHM)";
    svg.innerHTML = `
      <!-- ASHA healthcare icon -->
      <rect x="130" y="30" width="160" height="90" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
      <text x="150" y="55" fill="#c084fc" font-size="11" font-weight="bold">ASHA Worker Support</text>
      <text x="145" y="75" fill="#e0e7ff" font-size="9">&bull; Iron &amp; Folic Acid nutrition</text>
      <text x="145" y="90" fill="#e0e7ff" font-size="9">&bull; Institutional hospital birth</text>
      <text x="145" y="105" fill="#e0e7ff" font-size="9">&bull; Mandatory infant vaccinations</text>
    `;
    desc.innerHTML = "<strong>Community Healthcare:</strong> Over 10 lakh Accredited Social Health Activists (ASHA) under the National Health Mission counsel rural mothers, guide nutrition, accompany hospital births, and oversee vaccination.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S15(1));
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Method:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S16('barrier')" id="c11s16_btn_bar" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">1. Barrier (Condoms)</button>
        <button onclick="setC11S16('saheli')" id="c11s16_btn_sah" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Hormonal &amp; Saheli</button>
        <button onclick="setC11S16('iud')" id="c11s16_btn_iud" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. IUD (Copper-T)</button>
        <button onclick="setC11S16('surgery')" id="c11s16_btn_sur" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">4. Surgical Sterilisation</button>
      </div>
    </div>
    <span class="text-xs text-emerald-300 font-semibold" id="c11s16_tag">Mechanical Barrier &bull; STI + Pregnancy Protection</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s16_content" class="w-full max-w-lg"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-300">
    <span>Strict legal ban on prenatal sex determination in India protects female children and maintains demographic balance.</span>
  </div>
</div>
<script>
window.setC11S16 = function(cat){
  const btns = ['bar','sah','iud','sur'];
  btns.forEach(b => { document.getElementById('c11s16_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const c = document.getElementById('c11s16_content');
  const tag = document.getElementById('c11s16_tag');

  if(cat === 'barrier'){
    document.getElementById('c11s16_btn_bar').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Mechanical Barrier • STI + Pregnancy Protection";
    c.innerHTML = `
      <div class="p-3 rounded-xl bg-slate-900 border border-cyan-800/60 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-cyan-300">Latex Condoms &amp; Diaphragms</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300">Dual Shield</span>
        </div>
        <p class="text-xs text-slate-300">Mechanically prevents sperm from entering the female genital tract.</p>
        <div class="p-2 rounded-lg bg-cyan-950/40 border border-cyan-800 text-xs text-cyan-200">
          <strong>Crucial Public Health Advantage:</strong> Condoms are the ONLY contraceptive method that shields against both unwanted pregnancy and Sexually Transmitted Infections (STIs like HIV, gonorrhoea, and syphilis).
        </div>
      </div>
    `;
  } else if(cat === 'saheli'){
    document.getElementById('c11s16_btn_sah').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Hormonal & CDRI Saheli (Centchroman)";
    c.innerHTML = `
      <div class="p-3 rounded-xl bg-slate-900 border border-amber-800/60 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-amber-300">Indian Scientific Triumph: Saheli</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300">Once-a-Week</span>
        </div>
        <p class="text-xs text-slate-300">Developed by scientists at the Central Drug Research Institute (CDRI) in Lucknow, Uttar Pradesh.</p>
        <div class="p-2 rounded-lg bg-amber-950/40 border border-amber-800 text-xs text-amber-200">
          <strong>Non-Steroidal Advantage:</strong> World's first non-hormonal, non-steroidal oral contraceptive pill. It prevents implantation with negligible side effects compared to daily hormonal pills.
        </div>
      </div>
    `;
  } else if(cat === 'iud'){
    document.getElementById('c11s16_btn_iud').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Intra-Uterine Devices (Copper-T)";
    c.innerHTML = `
      <div class="p-3 rounded-xl bg-slate-900 border border-emerald-800/60 space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-sm font-bold text-emerald-300">Copper-T (IUD)</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300">Long-Acting Reversible</span>
        </div>
        <p class="text-xs text-slate-300">A small T-shaped device inserted into the uterine cavity by a trained medical professional.</p>
        <div class="p-2 rounded-lg bg-emerald-950/40 border border-emerald-800 text-xs text-emerald-200">
          <strong>Mode of Action:</strong> Slowly releases copper ions that suppress sperm motility and fertilising capacity, while preventing blastocyst implantation.
        </div>
      </div>
    `;
  } else {
    document.getElementById('c11s16_btn_sur').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Permanent Surgical Sterilisation";
    c.innerHTML = `
      <div class="grid grid-cols-2 gap-3">
        <div class="p-2.5 rounded-xl bg-slate-900 border border-purple-800/60">
          <span class="text-xs font-bold text-purple-300 block">Vasectomy (Male)</span>
          <p class="text-[11px] text-slate-300 mt-1">A small segment of the vas deferens is cut and tied off. Sperm cannot enter semen; ejaculation remains normal.</p>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-purple-800/60">
          <span class="text-xs font-bold text-purple-300 block">Tubectomy (Female)</span>
          <p class="text-[11px] text-slate-300 mt-1">A small segment of each fallopian tube is ligated and severed. Blocks sperm from reaching the ovum.</p>
        </div>
      </div>
      <p class="text-[11px] text-slate-400 mt-2 text-center">Highly effective permanent methods with zero interference to sexual libido or hormone production.</p>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S16('barrier'));
</script>"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 3: Tissues in Action
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧬</span> Biological Hierarchy &amp; Division of Labour Explorer
  </h3>
  <div class="grid grid-cols-5 gap-1 text-xs">
    <button onclick="c9s3s1Lvl(0)" class="py-1.5 rounded-lg bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">1. Cells</button>
    <button onclick="c9s3s1Lvl(1)" class="py-1.5 rounded-lg bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">2. Tissues</button>
    <button onclick="c9s3s1Lvl(2)" class="py-1.5 rounded-lg bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">3. Organs</button>
    <button onclick="c9s3s1Lvl(3)" class="py-1.5 rounded-lg bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">4. Systems</button>
    <button onclick="c9s3s1Lvl(4)" class="py-1.5 rounded-lg bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">5. Organism</button>
  </div>
  <div id="c9s3s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const lvls = [
    { t: '1. Specialized Cells (Division of Labour)', c: 'text-cyan-300', d: 'A single cell divides and differentiates into skin (protection), muscle (movement), bone (support), and nerve (coordination) cells—far more efficient than a unicellular Amoeba!' },
    { t: '2. Tissues (Coordinated Cell Teams)', c: 'text-emerald-300', d: 'A group of similar cells specialized for a shared function (e.g., muscular tissue or xylem).' },
    { t: '3. Organs (Multi-Tissue Structures)', c: 'text-amber-300', d: 'Different tissues combine to form functional organs such as the heart, stomach, or leaf.' },
    { t: '4. Organ Systems (Integrated Partnerships)', c: 'text-violet-300', d: 'Organs cooperate in systems such as the digestive, circulatory, or musculoskeletal system.' },
    { t: '5. Complete Multicellular Organism', c: 'text-rose-300', d: 'All organ systems coordinate smoothly to sustain life in plants and animals.' }
  ];
  window.c9s3s1Lvl = function(i){
    const l = lvls[i];
    document.getElementById('c9s3s1Out').innerHTML = `<div class="font-bold text-sm ${l.c}">${l.t}</div><p class="text-slate-300 leading-relaxed">${l.d}</p>`;
  };
  c9s3s1Lvl(0);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌿</span> Plant vs. Animal Tissue Architecture Comparator
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s3s2Mode(0)" class="py-2 rounded-xl bg-emerald-500/20 border border-emerald-400/50 text-emerald-200 font-bold">Stationary Plants</button>
    <button onclick="c9s3s2Mode(1)" class="py-2 rounded-xl bg-amber-500/20 border border-amber-400/50 text-amber-200 font-bold">Mobile Animals</button>
  </div>
  <div id="c9s3s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const modes = [
    `<div class="font-bold text-sm text-emerald-300">Plants: Stationary &amp; Autotrophic</div>
     <div class="text-slate-300"><b>Support:</b> Rigid cell walls and abundant dead mechanical cells for uprightness.</div>
     <div class="text-slate-300"><b>Nutrition &amp; Growth:</b> Autotrophic photosynthesis; continuous localized growth at meristems.</div>`,
    `<div class="font-bold text-sm text-amber-300">Animals: Mobile &amp; Heterotrophic</div>
     <div class="text-slate-300"><b>Support:</b> Flexible living cells adapted for active locomotion and higher energy demand.</div>
     <div class="text-slate-300"><b>Nutrition &amp; Growth:</b> Heterotrophic digestive tissues; uniform growth up to definite adult size.</div>`
  ];
  window.c9s3s2Mode = function(i){
    document.getElementById('c9s3s2Out').innerHTML = modes[i];
  };
  c9s3s2Mode(0);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌱</span> Meristematic Cell Traits &amp; B. G. L. Swamy
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s3s3Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">5 Meristem Traits</button>
    <button onclick="c9s3s3Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">B. G. L. Swamy</button>
  </div>
  <div id="c9s3s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const views = [
    `<div class="font-bold text-sm text-emerald-300">Optimized for Rapid Mitosis</div>
     <ul class="list-disc pl-4 text-slate-300 space-y-0.5">
       <li>Small size &amp; thin cell walls</li>
       <li>Dense cytoplasm &amp; prominent nuclei</li>
       <li>Tightly packed with zero intercellular spaces</li>
       <li>Generally lacking vacuoles</li>
     </ul>`,
    `<div class="font-bold text-sm text-amber-300">Meet a Scientist: B. G. L. Swamy</div>
     <p class="text-slate-300 leading-relaxed">Renowned Indian botanist and plant anatomist who authored the award-winning Kannada botanical book <b>Hasuru Honnu (Green Gold)</b>.</p>`
  ];
  window.c9s3s3Pick = function(i){
    document.getElementById('c9s3s3Out').innerHTML = views[i];
  };
  c9s3s3Pick(0);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪴</span> Activity 3.1: Apical, Lateral &amp; Intercalary Meristems
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s4Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Apical (Jar A vs B)</button>
    <button onclick="c9s3s4Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Lateral (Girth/Rings)</button>
    <button onclick="c9s3s4Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Intercalary (Regrowth)</button>
  </div>
  <div id="c9s3s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Apical Meristem &amp; Activity 3.1 (Onion Root Tips)', c: 'text-cyan-300', d: 'Jar A (intact tips) keeps elongating; Jar B (cut root tips) stops growing, proving apical meristems at tips drive length growth.' },
    { t: 'Lateral Meristem (Secondary Girth &amp; Annual Rings)', c: 'text-amber-300', d: 'Cylindrical meristematic rings widen dicot stems and produce annual growth rings revealing tree age and past climate.' },
    { t: 'Intercalary Meristem &amp; Cell Differentiation', c: 'text-emerald-300', d: 'Located at nodes/internode bases so grasses and hedges regrow after cutting. Mature cells then differentiate permanently.' }
  ];
  window.c9s3s4Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s4Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s4Pick(0);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🛡️</span> Protective Epidermis &amp; Suberin Bark Explorer
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s5Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Cutin Cuticle</button>
    <button onclick="c9s3s5Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Stomata &amp; Roots</button>
    <button onclick="c9s3s5Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Cork &amp; Bark</button>
  </div>
  <div id="c9s3s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Waxy Cutin Cuticle (Aerial Epidermis)', c: 'text-emerald-300', d: 'Single tightly packed layer coated with waxy cutin prevents water loss, mechanical injury, and parasite invasion.' },
    { t: 'Root Hairs &amp; Leaf Stomata', c: 'text-cyan-300', d: 'Root hairs boost water/mineral absorption; leaf stomata regulate CO₂/O₂ exchange and transpiration pull.' },
    { t: 'Bark Formation (Cork Cambium + Suberin)', c: 'text-amber-300', d: 'Cork cambium generates dead, suberin-coated cork cells forming waterproof, insulating protective tree bark.' }
  ];
  window.c9s3s5Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s5Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s5Pick(0);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎋</span> Simple Permanent Supporting Tissues Lab
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s6Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Parenchyma</button>
    <button onclick="c9s3s6Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Collenchyma</button>
    <button onclick="c9s3s6Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Sclerenchyma</button>
  </div>
  <div id="c9s3s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Parenchyma (Living, Thin-Walled, Intercellular Spaces)', c: 'text-emerald-300', d: 'Stores food, performs photosynthesis, and forms buoyant air cavities (aerenchyma) in aquatic plants.' },
    { t: 'Collenchyma (Living, Pectin Corner Thickenings)', c: 'text-cyan-300', d: 'Unevenly thickened corners with pectin give tensile flexibility to bending stems and climbing tendrils.' },
    { t: 'Sclerenchyma (Dead, Thick Lignified Walls)', c: 'text-amber-300', d: 'Heavy lignin walls deliver extreme hardness and strength in coconut husk fibres and walnut shells.' }
  ];
  window.c9s3s6Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s6Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s6Pick(0);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚰</span> Xylem, Phloem &amp; Anther Culture Pioneers
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s7Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Xylem (Upward)</button>
    <button onclick="c9s3s7Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Phloem (Two-Way)</button>
    <button onclick="c9s3s7Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Guha &amp; Maheshwari</button>
  </div>
  <div id="c9s3s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Xylem: Unidirectional Water &amp; Mineral Transport', c: 'text-cyan-300', d: 'Components: tracheids, vessels, xylem fibres (all dead), and xylem parenchyma (ONLY living component). Part of Vascular Tissue System.' },
    { t: 'Phloem: Bidirectional Food Transport', c: 'text-emerald-300', d: 'Components: sieve tubes, companion cells (regulate sieve tubes), phloem parenchyma, and phloem fibres. Plant systems: Dermal, Ground, Vascular.' },
    { t: 'Sipra Guha Mukherjee &amp; S. C. Maheshwari', c: 'text-amber-300', d: 'Indian pioneers who discovered anther culture to regenerate whole haploid plants in tissue culture.' }
  ];
  window.c9s3s7Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s7Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s7Pick(0);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧱</span> Table 3.2: Animal Epithelial Tissues Explorer
  </h3>
  <div class="grid grid-cols-5 gap-1 text-xs">
    <button onclick="c9s3s8Pick(0)" class="py-1.5 rounded-lg bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Simple</button>
    <button onclick="c9s3s8Pick(1)" class="py-1.5 rounded-lg bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Stratified</button>
    <button onclick="c9s3s8Pick(2)" class="py-1.5 rounded-lg bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Glandular</button>
    <button onclick="c9s3s8Pick(3)" class="py-1.5 rounded-lg bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">Sensory</button>
    <button onclick="c9s3s8Pick(4)" class="py-1.5 rounded-lg bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Ciliated</button>
  </div>
  <div id="c9s3s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Simple Squamous Epithelium (Diffusion)', c: 'text-cyan-300', d: 'Ultra-thin single flat layer enabling rapid gas/nutrient diffusion (e.g., lung alveoli, capillaries).' },
    { t: 'Stratified Squamous Epithelium (Protection)', c: 'text-amber-300', d: 'Multiple stacked layers protecting outer skin and mouth lining against friction and wear.' },
    { t: 'Glandular Epithelium (Secretion)', c: 'text-emerald-300', d: 'Specialized secretory cells producing sweat, saliva, mucus, or digestive enzymes.' },
    { t: 'Sensory Epithelium (Reception)', c: 'text-violet-300', d: 'Detects stimuli such as taste, smell, light, or sound.' },
    { t: 'Columnar &amp; Ciliated Epithelium (Absorption &amp; Movement)', c: 'text-rose-300', d: 'Tall intestinal cells absorb nutrients; beating cilia in airways sweep mucus and dust outward.' }
  ];
  window.c9s3s8Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s8Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s8Pick(0);
})();
</script>
"""
}

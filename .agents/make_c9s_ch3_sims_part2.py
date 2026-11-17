#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 3: Tissues in Action
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🩸</span> Blood &amp; Structural Connective Tissues Lab
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s9Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Blood (Plasma/Cells)</button>
    <button onclick="c9s3s9Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Bone &amp; Cartilage</button>
    <button onclick="c9s3s9Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Tendon vs Ligament</button>
  </div>
  <div id="c9s3s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Blood Components (Activity 3.2 &amp; 3.3)', c: 'text-rose-300', d: 'Liquid Plasma matrix carries RBCs (hemoglobin oxygen transport), WBCs (immune defense/pus), and Platelets (blood clotting).' },
    { t: 'Bone &amp; Cartilage Framework', c: 'text-amber-300', d: 'Bones have a rigid calcium/phosphorus matrix; Cartilage offers soft, flexible cushioning at joints, ears, and nose.' },
    { t: 'Tendons vs. Ligaments', c: 'text-cyan-300', d: 'Tendons connect MUSCLE TO BONE; elastic Ligaments connect BONE TO BONE across joints.' }
  ];
  window.c9s3s9Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s9Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s9Pick(0);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>💪</span> Muscular Triad &amp; Neuron Signal Explorer
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <button onclick="c9s3s10Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Skeletal</button>
    <button onclick="c9s3s10Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Smooth</button>
    <button onclick="c9s3s10Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Cardiac</button>
    <button onclick="c9s3s10Pick(3)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Neuron</button>
  </div>
  <div id="c9s3s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Skeletal Muscle (Voluntary)', c: 'text-cyan-300', d: 'Striated, multinucleate, cylindrical fibres attached to bones for conscious movement.' },
    { t: 'Smooth Muscle (Involuntary)', c: 'text-emerald-300', d: 'Unstriated, spindle-shaped cells in internal organ walls driving slow continuous movement.' },
    { t: 'Cardiac Muscle (Heart Only)', c: 'text-rose-300', d: 'Involuntary, branched, striated fibres working rhythmically without fatigue.' },
    { t: 'Nervous Tissue &amp; Neuron', c: 'text-amber-300', d: 'Cell body + Dendrites (receive signals) + Axon &amp; Axon Terminals (transmit electrical/chemical impulses).' }
  ];
  window.c9s3s10Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s10Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s10Pick(0);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Activity 3.4 &amp; 3.5: Bone vs. Muscle Weight Share
  </h3>
  <label class="block bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
    <div class="flex justify-between"><span>Adult Body Weight:</span><span id="c9s3s11WL" class="text-cyan-300 font-bold">60 kg</span></div>
    <input id="c9s3s11W" type="range" min="40" max="100" step="5" value="60" oninput="c9s3s11Up()" class="w-full accent-cyan-400">
  </label>
  <div id="c9s3s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9s3s11Up = function(){
    const w = parseInt(document.getElementById('c9s3s11W').value, 10);
    document.getElementById('c9s3s11WL').textContent = w + ' kg';
    const bLow = (w * 0.12).toFixed(1), bHigh = (w * 0.15).toFixed(1);
    const mLow = (w * 0.35).toFixed(1), mHigh = (w * 0.45).toFixed(1);
    document.getElementById('c9s3s11Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Bones (~12–15%)</div><div class="text-base font-bold text-amber-300">${bLow}–${bHigh} kg</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Skeletal Muscle (~35–45%)</div><div class="text-base font-bold text-cyan-300">${mLow}–${mHigh} kg</div></div>
      <div class="col-span-2 text-slate-400">Bones, muscles, joints, cartilage, tendons &amp; ligaments coordinate under nervous control!</div>`;
  };
  c9s3s11Up();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🦴</span> Joint Types &amp; Bone Marrow Stem Cells
  </h3>
  <div class="grid grid-cols-5 gap-1 text-xs">
    <button onclick="c9s3s12Pick(0)" class="py-1.5 rounded-lg bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Ball-Socket</button>
    <button onclick="c9s3s12Pick(1)" class="py-1.5 rounded-lg bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Hinge</button>
    <button onclick="c9s3s12Pick(2)" class="py-1.5 rounded-lg bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Pivot</button>
    <button onclick="c9s3s12Pick(3)" class="py-1.5 rounded-lg bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">Fixed</button>
    <button onclick="c9s3s12Pick(4)" class="py-1.5 rounded-lg bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Marrow</button>
  </div>
  <div id="c9s3s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  const items = [
    { t: '3.5.1 Ball and Socket Joint', c: 'text-cyan-300', d: 'Multi-directional circular rotation in shoulder and hip joints.' },
    { t: '3.5.2 Hinge Joint', c: 'text-emerald-300', d: 'Single-plane back-and-forth movement like a door hinge (elbow, knee).' },
    { t: '3.5.3 Pivot Joint', c: 'text-amber-300', d: 'Rotational side-to-side turning at the skull–vertebral column junction.' },
    { t: '3.5.4 Fixed Joints', c: 'text-violet-300', d: 'Immovable fused bones protecting delicate organs (e.g., cranium around the brain).' },
    { t: 'Bone Marrow Stem Cells', c: 'text-rose-300', d: 'Regenerate RBCs, WBCs, and platelets; bone marrow transplants treat leukemia and thalassemia.' }
  ];
  window.c9s3s12Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s12Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s12Pick(0);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧘</span> Axial Skeleton (Spine &amp; Rib Cage) &amp; Yoga
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s13Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Vertebral Column</button>
    <button onclick="c9s3s13Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">12-Pair Rib Cage</button>
    <button onclick="c9s3s13Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Yoga &amp; Health</button>
  </div>
  <div id="c9s3s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Vertebral Column (Backbone)', c: 'text-cyan-300', d: 'Vertebrae separated by flexible cartilage discs support posture, allow bending, and protect the spinal cord.' },
    { t: 'Rib Cage (12 Pairs of Ribs)', c: 'text-emerald-300', d: 'Connected by flexible costal cartilage so the chest expands and contracts smoothly during breathing while shielding heart and lungs.' },
    { t: 'Bridging Science &amp; Society: Yoga &amp; Health', c: 'text-amber-300', d: 'Regular yoga postures (Surya Namaskar), proper posture, and daily exercise maintain bone strength, joint flexibility, and muscle fitness.' }
  ];
  window.c9s3s13Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s13Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s13Pick(0);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🥕</span> F. C. Steward Totipotency &amp; Crown Gall Biotech
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s3s14Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Steward (1958 Carrot)</button>
    <button onclick="c9s3s14Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Crown Gall Vector</button>
  </div>
  <div id="c9s3s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'F. C. Steward (1958): Carrot Phloem Totipotency', c: 'text-amber-300', d: 'Mature carrot root phloem cells placed in nutrient medium underwent dedifferentiation (regained division) and redifferentiation into whole flowering carrot plants!' },
    { t: 'Crown Gall Disease → Crop Genetic Engineering', c: 'text-emerald-300', d: 'Agrobacterium tumefaciens naturally inserts DNA causing crown gall swellings; scientists disarmed its tumor genes to deliver beneficial traits into crops.' }
  ];
  window.c9s3s14Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s14Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s14Pick(0);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪵</span> Applied Puzzles: Teak Rings &amp; Elephant Debarking
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s3s15Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Teak Annual Rings</button>
    <button onclick="c9s3s15Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Elephant Debarking</button>
    <button onclick="c9s3s15Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Tendon &amp; Cloning</button>
  </div>
  <div id="c9s3s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Teak Tree Annual Rings (Lateral Meristem)', c: 'text-amber-300', d: 'Counting rings estimates tree age; wide rings record wet monsoon years while narrow rings record dry drought years.' },
    { t: 'Elephant Debarking (Girdling / Ring-Barking)', c: 'text-rose-300', d: 'Stripping a full ring of bark removes outer phloem, blocking downward food flow so roots starve and the tree eventually dies!' },
    { t: 'Ankle Tendon, Dance Joints &amp; Cloning vs Totipotency', c: 'text-cyan-300', d: 'Palpate your Achilles tendon (muscle-to-bone); compare joint ranges in tribal dance; reflect on natural plant totipotency vs animal cloning.' }
  ];
  window.c9s3s15Pick = function(i){
    const d = items[i];
    document.getElementById('c9s3s15Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s3s15Pick(0);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📋</span> Chapter 3 At a Glance: Tissue Master Map
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/30 space-y-1">
      <div class="font-bold text-emerald-300">Plant Tissues</div>
      <div class="text-slate-300"><b>Meristems:</b> Apical, Lateral, Intercalary</div>
      <div class="text-slate-300"><b>Simple:</b> Parenchyma, Collenchyma, Sclerenchyma</div>
      <div class="text-slate-300"><b>Complex:</b> Xylem (water ↑) &amp; Phloem (food ↕)</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-amber-500/30 space-y-1">
      <div class="font-bold text-amber-300">Animal Tissues</div>
      <div class="text-slate-300"><b>Epithelial:</b> Squamous, Glandular, Ciliated</div>
      <div class="text-slate-300"><b>Connective:</b> Blood, Bone, Cartilage, Tendon, Ligament</div>
      <div class="text-slate-300"><b>Muscle &amp; Nerve:</b> Skeletal, Smooth, Cardiac + Neuron</div>
    </div>
  </div>
</div>
"""
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 11 Simulators (Part 1: Slides 1-8)
High-fidelity responsive SVG interactive laboratory widgets.
"""

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Mode:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S1('asexual')" id="c11s1_btn_asex" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Asexual (Cloning)</button>
        <button onclick="setC11S1('sexual')" id="c11s1_btn_sex" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Sexual (Variation)</button>
        <button onclick="setC11S1('compare')" id="c11s1_btn_comp" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Comparison Matrix</button>
      </div>
    </div>
    <span class="text-xs text-slate-400" id="c11s1_status">Single Parent &bull; Mitotic Clones</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div id="c11s1_view_asex" class="w-full flex flex-col items-center justify-center space-y-4">
      <div class="flex items-center justify-around w-full max-w-md">
        <div class="flex flex-col items-center p-3 rounded-xl bg-cyan-950/40 border border-cyan-800/60">
          <span class="text-xs font-bold text-cyan-300">Single Parent (2n)</span>
          <div class="w-12 h-12 rounded-full border-2 border-cyan-400 flex items-center justify-center mt-2 bg-cyan-500/10">
            <span class="text-xs font-mono text-cyan-200">DNA</span>
          </div>
          <span class="text-[10px] text-slate-400 mt-1">Amoeba / Yeast / Hydra</span>
        </div>
        <div class="flex flex-col items-center">
          <span class="text-xs text-amber-400 font-bold">Mitosis</span>
          <span class="text-lg text-amber-400">&rarr;</span>
          <span class="text-[10px] text-slate-400">Zero Meiosis</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="flex flex-col items-center p-2.5 rounded-xl bg-cyan-950/30 border border-cyan-800/40">
            <span class="text-[11px] font-bold text-emerald-300">Clone A (2n)</span>
            <div class="w-10 h-10 rounded-full border border-emerald-400 flex items-center justify-center mt-1 bg-emerald-500/10">
              <span class="text-[10px] font-mono text-emerald-200">DNA</span>
            </div>
            <span class="text-[9px] text-emerald-400 mt-1">Identical</span>
          </div>
          <div class="flex flex-col items-center p-2.5 rounded-xl bg-cyan-950/30 border border-cyan-800/40">
            <span class="text-[11px] font-bold text-emerald-300">Clone B (2n)</span>
            <div class="w-10 h-10 rounded-full border border-emerald-400 flex items-center justify-center mt-1 bg-emerald-500/10">
              <span class="text-[10px] font-mono text-emerald-200">DNA</span>
            </div>
            <span class="text-[9px] text-emerald-400 mt-1">Identical</span>
          </div>
        </div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center max-w-lg">
        <p class="text-xs text-cyan-300 font-semibold">Fast, energy-efficient reproduction producing exact genetic clones. Ideal in stable environments!</p>
      </div>
    </div>

    <div id="c11s1_view_sex" class="hidden w-full flex flex-col items-center justify-center space-y-3">
      <div class="flex items-center justify-around w-full max-w-lg">
        <div class="flex flex-col items-center gap-2">
          <div class="p-2 rounded-lg bg-blue-950/50 border border-blue-700/60 text-center">
            <span class="text-[11px] font-bold text-blue-300">Parent 1 (2n)</span>
            <span class="text-[10px] block text-blue-400">&darr; Meiosis</span>
            <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 text-[10px] font-bold">Gamete (n)</span>
          </div>
          <div class="p-2 rounded-lg bg-rose-950/50 border border-rose-700/60 text-center">
            <span class="text-[11px] font-bold text-rose-300">Parent 2 (2n)</span>
            <span class="text-[10px] block text-rose-400">&darr; Meiosis</span>
            <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 text-[10px] font-bold">Gamete (n)</span>
          </div>
        </div>
        <div class="flex flex-col items-center">
          <span class="text-xs text-amber-400 font-bold">Fertilisation</span>
          <span class="text-lg text-amber-400">&rarr;</span>
          <span class="text-[10px] text-slate-400">n + n = 2n</span>
        </div>
        <div class="flex flex-col items-center p-3 rounded-xl bg-purple-950/40 border border-purple-800/60 text-center">
          <span class="text-xs font-bold text-purple-300">Zygote (2n)</span>
          <div class="w-12 h-12 rounded-full border-2 border-dashed border-purple-400 flex items-center justify-center mt-1 bg-purple-500/10">
            <span class="text-[10px] font-mono text-purple-200">Recombined</span>
          </div>
          <span class="text-[10px] text-amber-300 font-semibold mt-1">&star; Genetic Variation</span>
        </div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center max-w-lg">
        <p class="text-xs text-purple-300 font-semibold">Mixes two parental genomes generating rich biological variation essential for survival and adaptation.</p>
      </div>
    </div>

    <div id="c11s1_view_comp" class="hidden w-full max-w-xl">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border border-slate-800 rounded-lg">
          <thead class="bg-slate-900 text-slate-300">
            <tr>
              <th class="p-2 border-b border-slate-800">Feature</th>
              <th class="p-2 border-b border-slate-800 text-cyan-400">Asexual Reproduction</th>
              <th class="p-2 border-b border-slate-800 text-purple-400">Sexual Reproduction</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 text-slate-400">
            <tr><td class="p-2 font-semibold text-slate-300">Parents</td><td class="p-2 text-cyan-300">1 parent</td><td class="p-2 text-purple-300">2 parents</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Gametes</td><td class="p-2">No gametes formed</td><td class="p-2">Haploid sperm/pollen &amp; egg (n)</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Offspring</td><td class="p-2 text-emerald-400">Clones (100% identical)</td><td class="p-2 text-amber-400">Genetically diverse variants</td></tr>
            <tr><td class="p-2 font-semibold text-slate-300">Speed / Cost</td><td class="p-2">Rapid &amp; low energy</td><td class="p-2">Slower, high parental energy</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-300">
    <span id="c11s1_info">Asexual: Mitosis preserving parental traits | Sexual: Meiosis generating evolutionary variation</span>
  </div>
</div>
<script>
window.setC11S1 = function(mode){
  const va = document.getElementById('c11s1_view_asex');
  const vs = document.getElementById('c11s1_view_sex');
  const vc = document.getElementById('c11s1_view_comp');
  const ba = document.getElementById('c11s1_btn_asex');
  const bs = document.getElementById('c11s1_btn_sex');
  const bc = document.getElementById('c11s1_btn_comp');
  const st = document.getElementById('c11s1_status');
  [ba,bs,bc].forEach(b => { b.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  va.classList.add('hidden'); vs.classList.add('hidden'); vc.classList.add('hidden');
  if(mode === 'asexual'){
    va.classList.remove('hidden'); ba.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    st.textContent = 'Single Parent • Mitotic Clones';
  } else if(mode === 'sexual'){
    vs.classList.remove('hidden'); bs.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    st.textContent = 'Two Parents • Meiotic Recombination';
  } else {
    vc.classList.remove('hidden'); bc.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    st.textContent = 'Comparison: Clonal Stability vs Evolutionary Plasticity';
  }
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Plant Organ:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S2('potato')" id="c11s2_btn_pot" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Potato Tuber</button>
        <button onclick="setC11S2('bryo')" id="c11s2_btn_bry" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Bryophyllum Leaf</button>
        <button onclick="setC11S2('ginger')" id="c11s2_btn_gin" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ginger Rhizome</button>
        <button onclick="setC11S2('cane')" id="c11s2_btn_can" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Sugarcane Stem</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s2_tag">Underground Stem Tuber &bull; Buds ('Eyes')</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s2_diagram" class="w-full max-w-md flex flex-col items-center">
      <svg viewBox="0 0 400 160" class="w-full h-36">
        <!-- SVG will dynamically render selected plant -->
        <g id="c11s2_svg_content"></g>
      </svg>
      <div id="c11s2_desc" class="p-3 mt-2 rounded-xl bg-slate-900/90 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg">
        <strong>Potato Tuber:</strong> Modified underground storage stem possessing nodes known as 'eyes'. Each eye contains a dormant vegetative bud that sprouts into an independent leafy plant when placed in damp soil.
      </div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Vegetative propagation bypasses flowers and seeds, retaining 100% of parental crop traits.</span>
  </div>
</div>
<script>
window.setC11S2 = function(type){
  const btns = ['pot','bry','gin','can'];
  btns.forEach(b => { document.getElementById('c11s2_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const g = document.getElementById('c11s2_svg_content');
  const desc = document.getElementById('c11s2_desc');
  const tag = document.getElementById('c11s2_tag');

  if(type === 'potato'){
    document.getElementById('c11s2_btn_pot').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Underground Stem Tuber • Buds ('Eyes')";
    g.innerHTML = `
      <ellipse cx="200" cy="90" rx="90" ry="50" fill="#78350f" opacity="0.6" stroke="#b45309" stroke-width="2"/>
      <!-- Eyes / Buds -->
      <circle cx="160" cy="70" r="5" fill="#fde68a"/>
      <circle cx="230" cy="85" r="5" fill="#fde68a"/>
      <circle cx="190" cy="115" r="5" fill="#fde68a"/>
      <!-- Sprouting green shoot -->
      <path d="M160,65 Q150,35 140,20 Q145,28 160,30" fill="#22c55e"/>
      <path d="M160,65 Q170,40 180,25 Q175,32 165,35" fill="#4ade80"/>
      <!-- Adventitious roots -->
      <path d="M160,75 Q155,95 150,110 M160,75 Q165,95 170,115" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
      <text x="210" y="50" fill="#38bdf8" font-size="11" font-weight="bold">Sprouting Eye (Bud)</text>
      <text x="250" y="105" fill="#fde68a" font-size="10">Dormant Eye</text>
    `;
    desc.innerHTML = "<strong>Potato Tuber:</strong> Modified underground storage stem possessing nodes known as 'eyes'. Each eye contains a dormant vegetative bud that sprouts into an independent leafy plant when placed in damp soil.";
  } else if(type === 'bryo'){
    document.getElementById('c11s2_btn_bry').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Foliar Propagation • Leaf Margin Notches";
    g.innerHTML = `
      <!-- Big Fleshy Serrated Leaf -->
      <path d="M100,80 C120,20 280,20 300,80 C280,140 120,140 100,80 Z" fill="#14532d" opacity="0.7" stroke="#22c55e" stroke-width="2"/>
      <path d="M100,80 L300,80" stroke="#16a34a" stroke-width="2"/>
      <!-- Notches with plantlets -->
      <g transform="translate(140,40)">
        <circle cx="0" cy="0" r="3" fill="#eab308"/>
        <path d="M0,0 Q-5,-15 -10,-20 Q-2,-14 0,-8 Q5,-15 10,-20 Q3,-14 0,0" fill="#4ade80"/>
        <path d="M0,0 Q-4,10 -8,15 M0,0 Q4,10 8,15" stroke="#fef08a" stroke-width="1.2" fill="none"/>
      </g>
      <g transform="translate(220,38)">
        <circle cx="0" cy="0" r="3" fill="#eab308"/>
        <path d="M0,0 Q-5,-15 -10,-20 Q-2,-14 0,-8 Q5,-15 10,-20 Q3,-14 0,0" fill="#4ade80"/>
        <path d="M0,0 Q-4,10 -8,15 M0,0 Q4,10 8,15" stroke="#fef08a" stroke-width="1.2" fill="none"/>
      </g>
      <g transform="translate(180,120)">
        <circle cx="0" cy="0" r="3" fill="#eab308"/>
        <path d="M0,0 Q-5,15 -10,20 Q-2,14 0,8 Q5,15 10,20 Q3,14 0,0" fill="#4ade80"/>
        <path d="M0,0 Q-4,-10 -8,-15" stroke="#fef08a" stroke-width="1.2" fill="none"/>
      </g>
      <text x="240" y="25" fill="#fde047" font-size="11" font-weight="bold">Plantlet in Leaf Notch</text>
      <text x="200" y="145" fill="#86efac" font-size="10">Detaches onto moist soil</text>
    `;
    desc.innerHTML = "<strong>Bryophyllum Leaf:</strong> Fleshy succulent leaves with notches along their margins containing adventitious buds. In moist conditions, these buds sprout miniature plantlets complete with roots and shoots that drop off to form new plants!";
  } else if(type === 'ginger'){
    document.getElementById('c11s2_btn_gin').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Underground Horizontal Stem • Rhizome";
    g.innerHTML = `
      <path d="M120,90 Q150,60 200,80 Q250,60 280,95 Q250,120 190,110 Q140,120 120,90 Z" fill="#854d0e" opacity="0.7" stroke="#ca8a04" stroke-width="2"/>
      <!-- Nodes / scale leaves lines -->
      <line x1="160" y1="70" x2="155" y2="115" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="210" y1="75" x2="205" y2="110" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="250" y1="75" x2="245" y2="110" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>
      <!-- Upright shoot from node -->
      <path d="M210,75 Q215,40 220,15 Q210,30 205,45" fill="#22c55e"/>
      <path d="M210,75 Q230,45 240,25 Q225,40 215,55" fill="#4ade80"/>
      <!-- Adventitious roots from base -->
      <path d="M140,115 Q135,140 130,150 M180,112 Q180,140 185,150 M240,110 Q245,135 250,150" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
      <text x="245" y="35" fill="#4ade80" font-size="11" font-weight="bold">Aerial Green Shoot</text>
      <text x="130" y="60" fill="#fde047" font-size="10">Rhizome Node &amp; Scale Leaves</text>
    `;
    desc.innerHTML = "<strong>Ginger Rhizome:</strong> An underground modified stem growing horizontally. Possesses distinct nodes and internodes with scaly leaves. Buds at the nodes produce vigorous aerial green shoots and adventitious roots.";
  } else {
    document.getElementById('c11s2_btn_can').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Stem Cutting • Sugarcane Nodes";
    g.innerHTML = `
      <!-- Sugarcane stem pieces -->
      <rect x="120" y="65" width="160" height="30" rx="4" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
      <line x1="170" y1="65" x2="170" y2="95" stroke="#fde047" stroke-width="3"/>
      <line x1="230" y1="65" x2="230" y2="95" stroke="#fde047" stroke-width="3"/>
      <!-- Node bud sprouting -->
      <circle cx="170" cy="65" r="4" fill="#fbbf24"/>
      <path d="M170,65 Q165,35 155,15 Q165,28 175,35" fill="#4ade80"/>
      <!-- Roots from node -->
      <path d="M170,95 Q165,125 155,145 M170,95 Q175,125 180,145" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
      <text x="190" y="45" fill="#4ade80" font-size="11" font-weight="bold">Sprouting Node Bud</text>
      <text x="130" y="115" fill="#fde047" font-size="10">Stem Node with Cambium</text>
    `;
    desc.innerHTML = "<strong>Sugarcane Stem Propagation:</strong> Farmers slice mature sugarcane into stem setts containing at least one healthy node. When buried in moist soil, the node bud sprouts into a leafy shoot while adventitious roots establish firm anchorage.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S2('potato'));
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Method:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S3('grafting')" id="c11s3_btn_graft" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Grafting</button>
        <button onclick="setC11S3('cutting')" id="c11s3_btn_cut" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Cutting (45° Slant)</button>
        <button onclick="setC11S3('layering')" id="c11s3_btn_lay" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Layering</button>
        <button onclick="setC11S3('tissue')" id="c11s3_btn_tiss" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Meristem Tissue Culture</button>
      </div>
    </div>
    <span class="text-xs text-cyan-300 font-semibold" id="c11s3_tag">Scion (Fruiting Shoot) + Stock (Root Base)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c11s3_display" class="w-full max-w-lg flex flex-col items-center">
      <svg id="c11s3_svg" viewBox="0 0 420 150" class="w-full h-36">
        <!-- Dynamic content injected -->
      </svg>
      <div id="c11s3_details" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full"></div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Krishi Vigyan Kendras (KVKs under ICAR) train Indian farmers in modern vegetative propagation to maximize crop yields.</span>
  </div>
</div>
<script>
window.setC11S3 = function(mode){
  const btns = ['graft','cut','lay','tiss'];
  btns.forEach(b => { document.getElementById('c11s3_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s3_svg');
  const det = document.getElementById('c11s3_details');
  const tag = document.getElementById('c11s3_tag');

  if(mode === 'grafting'){
    document.getElementById('c11s3_btn_graft').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Scion (Fruiting Shoot) + Stock (Root Base)";
    svg.innerHTML = `
      <!-- Stock (lower rooted stem) -->
      <rect x="180" y="80" width="40" height="50" rx="3" fill="#78350f" stroke="#b45309" stroke-width="2"/>
      <path d="M180,80 L200,60 L220,80" fill="#92400e"/>
      <path d="M190,130 Q180,145 170,150 M200,130 Q200,148 205,150 M210,130 Q220,145 230,150" stroke="#f59e0b" stroke-width="2" fill="none"/>
      <!-- Scion (upper shoot) with wedge -->
      <rect x="180" y="20" width="40" height="40" rx="3" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
      <path d="M180,60 L200,80 L220,60" fill="#16a34a"/>
      <!-- Leaves on scion -->
      <path d="M180,30 Q150,15 140,25 Q160,35 180,35" fill="#4ade80"/>
      <path d="M220,30 Q250,15 260,25 Q240,35 220,35" fill="#4ade80"/>
      <!-- Tape wrap overlay -->
      <rect x="175" y="55" width="50" height="30" rx="2" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-dasharray="3,3"/>
      <text x="240" y="45" fill="#4ade80" font-size="11" font-weight="bold">Scion (High-Yield Variety)</text>
      <text x="240" y="75" fill="#38bdf8" font-size="10">Aligned Cambium &amp; Polythene Tape</text>
      <text x="240" y="105" fill="#f59e0b" font-size="11" font-weight="bold">Stock (Rooted Hardy Base)</text>
    `;
    det.innerHTML = "<strong>Grafting Protocol:</strong> Joining a rooted, hardy host plant (<strong>Stock</strong>) with a cut stem from a desired superior fruiting variety (<strong>Scion</strong>). Securely wrapping aligned vascular cambium layers enables them to heal into a single composite plant (e.g., premium mangoes and roses).";
  } else if(mode === 'cutting'){
    document.getElementById('c11s3_btn_cut').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "45°–60° Slanted Cut • Adventitious Rooting";
    svg.innerHTML = `
      <!-- Soil line -->
      <line x1="50" y1="100" x2="370" y2="100" stroke="#78350f" stroke-width="3"/>
      <rect x="50" y="100" width="320" height="40" fill="#451a03" opacity="0.4"/>
      <!-- Cut stem tilted at 45-60 deg -->
      <g transform="translate(180,95) rotate(-30)">
        <rect x="-10" y="-70" width="20" height="90" rx="2" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
        <!-- Slanted base cut -->
        <path d="M-10,20 L10,5 L10,20 Z" fill="#92400e"/>
        <!-- Node with leaf -->
        <circle cx="0" cy="-30" r="4" fill="#fbbf24"/>
        <path d="M10,-30 Q35,-45 45,-35 Q30,-25 10,-28" fill="#4ade80"/>
        <!-- Adventitious roots emerging -->
        <path d="M-5,15 Q-20,30 -25,45 M5,10 Q20,30 25,45" stroke="#f59e0b" stroke-width="2" fill="none"/>
      </g>
      <text x="230" y="40" fill="#4ade80" font-size="11" font-weight="bold">Trimmed Upper Shoot</text>
      <text x="230" y="75" fill="#fbbf24" font-size="10">Node planted at 45°–60° in moist soil</text>
      <text x="230" y="125" fill="#38bdf8" font-size="11" font-weight="bold">Adventitious Roots Sprout</text>
    `;
    det.innerHTML = "<strong>Stem Cutting (Activity 11.1):</strong> Slicing a shoot with intact nodes at a 45°–60° angle. Trimming lower leaves reduces transpiration while the submerged node rapidly produces adventitious roots in damp earth (e.g., rose, sugarcane).";
  } else if(mode === 'layering'){
    document.getElementById('c11s3_btn_lay').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Branch Bending • Rooting Before Severing";
    svg.innerHTML = `
      <!-- Parent tree trunk -->
      <rect x="80" y="40" width="30" height="90" fill="#78350f" stroke="#b45309" stroke-width="2"/>
      <!-- Soil line -->
      <line x1="50" y1="120" x2="380" y2="120" stroke="#92400e" stroke-width="3"/>
      <rect x="50" y="120" width="330" height="25" fill="#451a03" opacity="0.4"/>
      <!-- Flexible branch bent down into soil -->
      <path d="M110,60 C150,70 180,135 220,135 C260,135 280,70 300,50" fill="none" stroke="#22c55e" stroke-width="5"/>
      <!-- Roots in soil loop -->
      <path d="M210,135 Q205,145 200,150 M220,135 Q220,148 225,150 M230,135 Q235,145 240,150" stroke="#f59e0b" stroke-width="2" fill="none"/>
      <!-- Peg holding branch down -->
      <path d="M215,115 L225,130" stroke="#ef4444" stroke-width="3"/>
      <text x="130" y="30" fill="#fde047" font-size="11" font-weight="bold">Parent Shrub (Lemon / Jasmine)</text>
      <text x="180" y="110" fill="#ef4444" font-size="10">Pegged in Soil</text>
      <text x="270" y="40" fill="#4ade80" font-size="11" font-weight="bold">Severed Once Rooted!</text>
    `;
    det.innerHTML = "<strong>Layering:</strong> A flexible lower branch is bent downwards, pegged in moist soil, and kept nourished by the parent plant until strong roots emerge, after which it is severed to grow independently.";
  } else {
    document.getElementById('c11s3_btn_tiss').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Apical Meristem • Sterile Virus-Free Clones";
    svg.innerHTML = `
      <!-- Laboratory Flask with Agar -->
      <path d="M170,40 L190,40 L190,70 L140,120 C130,130 140,140 160,140 L260,140 C280,140 290,130 280,120 L230,70 L230,40 L250,40" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <!-- Nutrient Agar base -->
      <path d="M145,118 L275,118 L260,138 L160,138 Z" fill="#e0e7ff" opacity="0.3"/>
      <!-- Micro-plantlets growing in agar -->
      <path d="M180,125 Q180,105 175,95 Q185,100 185,125" fill="#22c55e"/>
      <path d="M210,125 Q210,100 205,90 Q215,95 215,125" fill="#4ade80"/>
      <path d="M240,125 Q240,105 245,95 Q235,100 235,125" fill="#22c55e"/>
      <text x="290" y="60" fill="#38bdf8" font-size="11" font-weight="bold">Sterile Nutrient Agar</text>
      <text x="290" y="85" fill="#4ade80" font-size="10">Excised Meristem Shoot Tip</text>
      <text x="290" y="110" fill="#fde047" font-size="10">100% Virus-Free Clones (Banana)</text>
    `;
    det.innerHTML = "<strong>Apical Meristem Tissue Culture:</strong> Actively dividing cells from shoot tips lack vascular tissue and viral pathogens. Cultured in sterile nutrient media, thousands of identical, virus-free banana plantlets are mass-produced!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S3('grafting'));
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Organism:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S4('yeast')" id="c11s4_btn_yeast" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Yeast Budding</button>
        <button onclick="setC11S4('hydra')" id="c11s4_btn_hydra" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Hydra Budding</button>
        <button onclick="setC11S4('rhizopus')" id="c11s4_btn_rhiz" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Rhizopus Spores</button>
        <button onclick="setC11S4('pasteur')" id="c11s4_btn_past" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Pasteur &amp; Cooling</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s4_tag">Unicellular Fungus &bull; Asymmetrical Budding</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg id="c11s4_svg" viewBox="0 0 420 150" class="w-full h-36">
      <!-- Dynamic SVG animation -->
    </svg>
    <div id="c11s4_info" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg"></div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Fungal spores possess durable dehydrated walls, resisting cold and drought until moisture arrives.</span>
  </div>
</div>
<script>
window.setC11S4 = function(m){
  const btns = ['yeast','hydra','rhiz','past'];
  btns.forEach(b => { document.getElementById('c11s4_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s4_svg');
  const inf = document.getElementById('c11s4_info');
  const tag = document.getElementById('c11s4_tag');

  if(m === 'yeast'){
    document.getElementById('c11s4_btn_yeast').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Unicellular Fungus • Asymmetrical Budding";
    svg.innerHTML = `
      <!-- Yeast cell 1: Parent with budding bump -->
      <ellipse cx="100" cy="80" rx="35" ry="30" fill="#3b82f6" opacity="0.4" stroke="#60a5fa" stroke-width="2"/>
      <circle cx="100" cy="80" r="10" fill="#1e40af"/>
      <path d="M130,70 Q145,65 145,80 Q145,95 130,90" fill="#3b82f6" opacity="0.5" stroke="#60a5fa" stroke-width="2"/>
      <circle cx="138" cy="80" r="4" fill="#1e40af"/>
      <text x="80" y="125" fill="#93c5fd" font-size="10">1. Emerging Bud</text>

      <!-- Yeast cell 2: Replicating nucleus -->
      <ellipse cx="220" cy="80" rx="35" ry="30" fill="#3b82f6" opacity="0.4" stroke="#60a5fa" stroke-width="2"/>
      <ellipse cx="265" cy="75" rx="20" ry="18" fill="#3b82f6" opacity="0.5" stroke="#60a5fa" stroke-width="2"/>
      <path d="M220,80 Q240,78 265,75" stroke="#f59e0b" stroke-width="3" stroke-dasharray="2,2"/>
      <circle cx="220" cy="80" r="8" fill="#1e40af"/>
      <circle cx="265" cy="75" r="7" fill="#1e40af"/>
      <text x="210" y="125" fill="#93c5fd" font-size="10">2. Mitotic Migration</text>

      <!-- Yeast cell 3: Chain of budding cells -->
      <ellipse cx="330" cy="80" rx="25" ry="22" fill="#3b82f6" opacity="0.4" stroke="#60a5fa" stroke-width="2"/>
      <ellipse cx="370" cy="65" rx="18" ry="16" fill="#3b82f6" opacity="0.5" stroke="#60a5fa" stroke-width="2"/>
      <ellipse cx="395" cy="45" rx="12" ry="10" fill="#3b82f6" opacity="0.6" stroke="#60a5fa" stroke-width="2"/>
      <text x="325" y="125" fill="#fde047" font-size="10">3. Bud Chain</text>
    `;
    inf.innerHTML = "<strong>Yeast Budding (Activity 11.2):</strong> Baker's yeast metabolizes glucose in warm water, forming a localized mitotic protuberance (bud). The nucleus divides mitotically, sending a copy into the bud, which may detach or form chains.";
  } else if(m === 'hydra'){
    document.getElementById('c11s4_btn_hydra').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Multicellular Cnidarian • Outgrowth & Detachment";
    svg.innerHTML = `
      <!-- Hydra Parent Body -->
      <path d="M150,140 Q150,50 170,40 Q190,50 190,140 Z" fill="#14532d" opacity="0.6" stroke="#22c55e" stroke-width="2"/>
      <!-- Tentacles on parent -->
      <path d="M170,40 Q140,15 130,5 M170,40 Q160,10 165,0 M170,40 Q180,10 185,0 M170,40 Q200,15 210,5" stroke="#4ade80" stroke-width="2" fill="none"/>
      <!-- Bud outgrowth on side of parent -->
      <path d="M190,95 Q230,90 235,75 Q240,95 190,115 Z" fill="#166534" stroke="#4ade80" stroke-width="2"/>
      <!-- Mini tentacles on bud -->
      <path d="M235,75 Q245,65 255,60 M235,75 Q250,75 260,78 M235,75 Q245,85 255,90" stroke="#86efac" stroke-width="1.5" fill="none"/>
      <!-- Arrow and detached baby hydra -->
      <text x="240" y="125" fill="#fbbf24" font-size="14">&rarr;</text>
      <g transform="translate(140, 20)">
        <path d="M150,120 Q150,80 160,75 Q170,80 170,120 Z" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
        <path d="M160,75 Q145,60 140,55 M160,75 Q160,55 160,50 M160,75 Q175,60 180,55" stroke="#86efac" stroke-width="1.5" fill="none"/>
        <text x="135" y="135" fill="#86efac" font-size="9">Independent Hydra</text>
      </g>
    `;
    inf.innerHTML = "<strong>Hydra Budding:</strong> Repeated cell divisions at a specific body site produce a lateral bud. As it develops tentacles and a mouth, it constricts at the base and cleanly detaches to live as an autonomous clone!";
  } else if(m === 'rhizopus'){
    document.getElementById('c11s4_btn_rhiz').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Bread Mould (Rhizopus) • Sporangium & Spores";
    svg.innerHTML = `
      <!-- Bread surface -->
      <rect x="50" y="120" width="320" height="25" fill="#78350f" opacity="0.5"/>
      <text x="60" y="137" fill="#fbbf24" font-size="10">Moist Bread Substrate</text>
      <!-- Hyphae meshwork -->
      <path d="M80,120 Q120,115 160,120 Q200,112 240,120 Q280,115 320,120" stroke="#fef08a" stroke-width="2" fill="none"/>
      <!-- Upright Sporangiophore 1 (Intact) -->
      <line x1="140" y1="120" x2="140" y2="55" stroke="#fef08a" stroke-width="2"/>
      <circle cx="140" cy="50" r="18" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
      <text x="110" y="25" fill="#cbd5e1" font-size="10">Sporangium</text>
      <!-- Upright Sporangiophore 2 (Bursting) -->
      <line x1="250" y1="120" x2="250" y2="60" stroke="#fef08a" stroke-width="2"/>
      <path d="M235,55 Q245,45 250,55 Q255,45 265,55" fill="none" stroke="#64748b" stroke-width="2"/>
      <!-- Airborne spores dispersing -->
      <circle cx="270" cy="40" r="3" fill="#38bdf8"/>
      <circle cx="285" cy="30" r="3" fill="#38bdf8"/>
      <circle cx="300" cy="45" r="3" fill="#38bdf8"/>
      <circle cx="315" cy="25" r="3" fill="#38bdf8"/>
      <circle cx="290" cy="65" r="3" fill="#38bdf8"/>
      <text x="270" y="80" fill="#38bdf8" font-size="10 font-weight="bold">Airborne Spores Dispersing</text>
    `;
    inf.innerHTML = "<strong>Fungal Spore Formation (Activity 11.3):</strong> Rhizopus develops upright hyphae topped by dark sporangia packed with thousands of microscopic spores. When the sac bursts, lightweight spores float on air currents to colonize new organic food.";
  } else {
    document.getElementById('c11s4_btn_past').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Pasteur's Germ Theory • Food Refrigeration";
    svg.innerHTML = `
      <!-- Swan-neck flask of Pasteur -->
      <path d="M80,120 C60,110 70,80 90,80 L110,80 L110,50 Q130,20 160,20 Q190,20 170,50 L180,60" fill="none" stroke="#e0e7ff" stroke-width="2"/>
      <ellipse cx="90" cy="115" rx="30" ry="10" fill="#fde047" opacity="0.4"/>
      <text x="50" y="140" fill="#e0e7ff" font-size="10">Pasteur's Swan-Neck Flask</text>
      <!-- Refrigerator block -->
      <rect x="250" y="30" width="120" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <line x1="250" y1="65" x2="370" y2="65" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="260" y="40" width="10" height="2" fill="#38bdf8"/>
      <rect x="260" y="75" width="10" height="2" fill="#38bdf8"/>
      <text x="270" y="55" fill="#38bdf8" font-size="11" font-weight="bold">Freezer (&lt; 0°C)</text>
      <text x="270" y="95" fill="#38bdf8" font-size="11" font-weight="bold">Cooler (4°C)</text>
      <text x="260" y="120" fill="#fde047" font-size="9">Halts Spore Germination</text>
    `;
    inf.innerHTML = "<strong>Germ Theory &amp; Food Preservation:</strong> Louis Pasteur disproved spontaneous generation by proving microbes come from airborne spores. Refrigerators chill food below 4°C, halting spore enzyme activity and preventing mould growth!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S4('yeast'));
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Chromosome Pairs (n):</span>
      <input type="range" id="c11s5_n_slider" min="1" max="6" value="3" oninput="updateC11S5(this.value)" class="w-28 accent-cyan-400">
      <span class="text-xs font-mono font-bold text-white px-2 py-0.5 rounded bg-slate-800" id="c11s5_n_disp">n = 3</span>
    </div>
    <span class="text-xs text-amber-300 font-bold" id="c11s5_comb_disp">2^3 = 8 Combinations</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <!-- Bead representation of Activity 11.4 -->
    <div class="w-full max-w-lg space-y-3">
      <div class="flex items-center justify-between p-2 rounded-lg bg-slate-900 border border-slate-800">
        <span class="text-xs font-bold text-slate-300">Activity 11.4 Chromosome Pairs (Beads):</span>
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1"><span class="w-3.5 h-3.5 rounded-full bg-rose-500"></span><span class="w-3.5 h-3.5 rounded-full bg-blue-500"></span><span class="text-[10px] text-slate-400">Pair 1</span></div>
          <div class="flex items-center gap-1"><span class="w-3.5 h-3.5 rounded-full bg-emerald-500"></span><span class="w-3.5 h-3.5 rounded-full bg-yellow-500"></span><span class="text-[10px] text-slate-400">Pair 2</span></div>
          <div class="flex items-center gap-1"><span class="w-3.5 h-3.5 rounded-full bg-purple-500"></span><span class="w-3.5 h-3.5 rounded-full bg-orange-500"></span><span class="text-[10px] text-slate-400">Pair 3</span></div>
        </div>
      </div>

      <div id="c11s5_bead_grid" class="grid grid-cols-4 gap-2 text-center text-xs">
        <!-- Injected combinations -->
      </div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-300">
    <span>Human beings: 23 pairs &rarr; 2^23 = <strong>8,388,608</strong> possible gamete combinations per parent!</span>
  </div>
</div>
<script>
window.updateC11S5 = function(n){
  n = parseInt(n);
  document.getElementById('c11s5_n_disp').textContent = 'n = ' + n;
  const total = Math.pow(2, n);
  document.getElementById('c11s5_comb_disp').textContent = '2^' + n + ' = ' + total + ' Gamete Types';
  const grid = document.getElementById('c11s5_bead_grid');
  grid.innerHTML = '';
  const limit = Math.min(total, 16);
  for(let i=0; i<limit; i++){
    let dots = '';
    const colors = [['#f43f5e','#3b82f6'], ['#10b981','#eab308'], ['#a855f7','#f97316'], ['#06b6d4','#ec4899'], ['#84cc16','#6366f1'], ['#14b8a6','#d946ef']];
    for(let b=0; b<n; b++){
      const bit = (i >> b) & 1;
      const c = colors[b % colors.length][bit];
      dots += `<span class="inline-block w-2.5 h-2.5 rounded-full mr-1" style="background:${c}"></span>`;
    }
    const card = document.createElement('div');
    card.className = 'p-2 rounded-lg bg-slate-900 border border-slate-800 flex flex-col items-center';
    card.innerHTML = `<span class="text-[10px] text-slate-400 mb-1">Gamete ${i+1}</span><div>${dots}</div>`;
    grid.appendChild(card);
  }
};
window.addEventListener('DOMContentLoaded', () => updateC11S5(3));
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Floral Whorl:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S6('all')" id="c11s6_btn_all" class="px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Complete Flower</button>
        <button onclick="setC11S6('calyx')" id="c11s6_btn_cal" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">1. Calyx (Sepals)</button>
        <button onclick="setC11S6('corolla')" id="c11s6_btn_cor" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Corolla (Petals)</button>
        <button onclick="setC11S6('stamen')" id="c11s6_btn_sta" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Stamen (Male)</button>
        <button onclick="setC11S6('pistil')" id="c11s6_btn_pis" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">4. Pistil (Female)</button>
      </div>
    </div>
    <span class="text-xs text-emerald-300 font-semibold" id="c11s6_tag">All 4 Concentric Floral Whorls</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg id="c11s6_svg" viewBox="0 0 420 160" class="w-full h-36">
      <!-- Receptacle & Pedicel -->
      <path d="M195,150 L205,150 L205,130 Q220,125 220,115 L180,115 Q180,125 195,130 Z" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
      <!-- Whorl 1: Sepals (Calyx) -->
      <path id="c11s6_w_calyx" d="M180,115 Q140,115 130,95 Q155,100 180,115 M220,115 Q260,115 270,95 Q245,100 220,115" fill="#16a34a" stroke="#22c55e" stroke-width="2"/>
      <!-- Whorl 2: Petals (Corolla) -->
      <path id="c11s6_w_corolla" d="M180,115 Q110,90 90,40 Q140,50 170,80 M220,115 Q290,90 310,40 Q260,50 230,80 M180,115 Q200,60 200,30 Q200,60 220,115" fill="#f43f5e" opacity="0.8" stroke="#fb7185" stroke-width="2"/>
      <!-- Whorl 3: Stamens (Filament + Anther) -->
      <g id="c11s6_w_stamen">
        <path d="M190,110 Q160,70 155,45" stroke="#fde047" stroke-width="2" fill="none"/>
        <ellipse cx="155" cy="42" rx="6" ry="4" fill="#eab308" stroke="#ca8a04"/>
        <path d="M210,110 Q240,70 245,45" stroke="#fde047" stroke-width="2" fill="none"/>
        <ellipse cx="245" cy="42" rx="6" ry="4" fill="#eab308" stroke="#ca8a04"/>
      </g>
      <!-- Whorl 4: Pistil (Ovary, Style, Stigma) -->
      <g id="c11s6_w_pistil">
        <!-- Swollen Ovary -->
        <ellipse cx="200" cy="100" rx="16" ry="15" fill="#14532d" stroke="#16a34a" stroke-width="2"/>
        <!-- Ovules inside ovary -->
        <circle cx="195" cy="98" r="3" fill="#fef08a"/>
        <circle cx="205" cy="98" r="3" fill="#fef08a"/>
        <!-- Style -->
        <line x1="200" y1="85" x2="200" y2="40" stroke="#22c55e" stroke-width="4"/>
        <!-- Sticky Stigma tip -->
        <ellipse cx="200" cy="38" rx="8" ry="4" fill="#86efac" stroke="#15803d" stroke-width="2"/>
      </g>
    </svg>
    <div id="c11s6_desc" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg">
      Click the tabs above to isolate each floral whorl: <strong>Calyx (Sepals)</strong>, <strong>Corolla (Petals)</strong>, <strong>Stamen (Male)</strong>, and <strong>Pistil/Carpel (Female)</strong>.
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Bisexual flowers (hibiscus) have both stamens and pistil; unisexual flowers (papaya) have only one.</span>
  </div>
</div>
<script>
window.setC11S6 = function(w){
  const btns = ['all','cal','cor','sta','pis'];
  btns.forEach(b => { document.getElementById('c11s6_btn_' + b).className = 'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const c = document.getElementById('c11s6_w_calyx');
  const r = document.getElementById('c11s6_w_corolla');
  const s = document.getElementById('c11s6_w_stamen');
  const p = document.getElementById('c11s6_w_pistil');
  const desc = document.getElementById('c11s6_desc');
  const tag = document.getElementById('c11s6_tag');

  [c,r,s,p].forEach(el => el.style.opacity = '1');
  if(w === 'all'){
    document.getElementById('c11s6_btn_all').className = 'px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "All 4 Concentric Floral Whorls";
    desc.innerHTML = "<strong>Complete Bisexual Flower:</strong> Calyx protects in bud, Corolla attracts pollinators, Stamens synthesize male pollen, and Pistil houses ovules inside the basal ovary.";
  } else if(w === 'calyx'){
    document.getElementById('c11s6_btn_cal').className = 'px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    tag.textContent = "Whorl 1: Calyx (Green Sepals)";
    r.style.opacity = '0.15'; s.style.opacity = '0.15'; p.style.opacity = '0.15';
    desc.innerHTML = "<strong>Calyx (Sepals):</strong> The outermost vegetative whorl. Green and leafy, its primary function is shielding and protecting delicate inner reproductive organs during the bud stage.";
  } else if(w === 'corolla'){
    document.getElementById('c11s6_btn_cor').className = 'px-2 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
    tag.textContent = "Whorl 2: Corolla (Bright Petals)";
    c.style.opacity = '0.15'; s.style.opacity = '0.15'; p.style.opacity = '0.15';
    desc.innerHTML = "<strong>Corolla (Petals):</strong> The second floral whorl. Often brightly colored, fragrant, and possessing nectaries to lure insect and avian pollinators for cross-pollination.";
  } else if(w === 'stamen'){
    document.getElementById('c11s6_btn_sta').className = 'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Whorl 3: Androecium (Male Stamens)";
    c.style.opacity = '0.15'; r.style.opacity = '0.15'; p.style.opacity = '0.15';
    desc.innerHTML = "<strong>Stamen (Male Reproductive Organ):</strong> Consists of a slender supporting <strong>filament</strong> and a terminal bilobed <strong>anther</strong> whose pollen sacs synthesize microscopic pollen grains carrying male gametes.";
  } else {
    document.getElementById('c11s6_btn_pis').className = 'px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition';
    tag.textContent = "Whorl 4: Gynoecium (Female Pistil / Carpel)";
    c.style.opacity = '0.15'; r.style.opacity = '0.15'; s.style.opacity = '0.15';
    desc.innerHTML = "<strong>Pistil / Carpel (Female Organ):</strong> Features a sticky landing <strong>stigma</strong>, an elongated <strong>style</strong>, and a swollen basal <strong>ovary</strong> containing protective <strong>ovules</strong> with female egg cells.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S6('all'));
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Vector:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S7('wind')" id="c11s7_btn_wind" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Wind (Wheat/Maize)</button>
        <button onclick="setC11S7('insect')" id="c11s7_btn_ins" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Insect (Sunflower/Bee)</button>
        <button onclick="setC11S7('water')" id="c11s7_btn_wat" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Water (Vallisneria)</button>
        <button onclick="setC11S7('bird')" id="c11s7_btn_bir" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Bird (Coral Tree)</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-semibold" id="c11s7_tag">Lightweight Pollen &bull; Feathery Stigma</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div class="w-full max-w-lg flex flex-col items-center">
      <svg id="c11s7_svg" viewBox="0 0 420 150" class="w-full h-36">
        <!-- Dynamic illustration of vector pollination -->
      </svg>
      <div id="c11s7_details" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full"></div>
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Activity 11.7: Wind grasses expend ~1,000,000 pollens for 50-200 seeds; insect flowers use far fewer!</span>
  </div>
</div>
<script>
window.setC11S7 = function(vec){
  const btns = ['wind','ins','wat','bir'];
  btns.forEach(b => { document.getElementById('c11s7_btn_' + b).className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition'; });
  const svg = document.getElementById('c11s7_svg');
  const det = document.getElementById('c11s7_details');
  const tag = document.getElementById('c11s7_tag');

  if(vec === 'wind'){
    document.getElementById('c11s7_btn_wind').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition';
    tag.textContent = "Lightweight Pollen • Feathery Stigma";
    svg.innerHTML = `
      <!-- Grass stem with feathery stigma -->
      <line x1="280" y1="140" x2="280" y2="70" stroke="#65a30d" stroke-width="3"/>
      <!-- Feathery branched stigma -->
      <path d="M280,70 Q250,50 240,30 M280,70 Q270,40 265,20 M280,70 Q290,40 295,20 M280,70 Q310,50 320,30" stroke="#fde047" stroke-width="2" fill="none"/>
      <!-- Wind breeze lines & millions of micro-pollens -->
      <path d="M60,60 Q120,45 180,60 Q240,75 300,60" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" fill="none"/>
      <circle cx="100" cy="55" r="2" fill="#fef08a"/><circle cx="140" cy="65" r="2" fill="#fef08a"/>
      <circle cx="180" cy="50" r="2" fill="#fef08a"/><circle cx="220" cy="68" r="2" fill="#fef08a"/>
      <circle cx="260" cy="45" r="2" fill="#fef08a"/><circle cx="280" cy="35" r="2" fill="#fef08a"/>
      <text x="60" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Airborne Wind Current</text>
      <text x="240" y="95" fill="#fde047" font-size="10">Protruding Feathery Stigma</text>
    `;
    det.innerHTML = "<strong>Wind Pollination (Anemophily):</strong> Seen in cereal crops (wheat, rice, maize). Flowers lack petals and scent but generate millions of dry, ultra-lightweight pollen grains caught by prominent, feathery stigmas.";
  } else if(vec === 'insect'){
    document.getElementById('c11s7_btn_ins').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    tag.textContent = "Bright Petals • Nectar & Spiny Pollen";
    svg.innerHTML = `
      <!-- Big bright Sunflower center & petals -->
      <circle cx="150" cy="90" r="30" fill="#78350f" stroke="#b45309" stroke-width="3"/>
      <path d="M150,55 L150,35 M150,125 L150,145 M115,90 L95,90 M185,90 L205,90" stroke="#eab308" stroke-width="6"/>
      <!-- Honeybee flying towards flower -->
      <g transform="translate(260, 60)">
        <ellipse cx="0" cy="0" rx="14" ry="10" fill="#fde047" stroke="#000" stroke-width="1.5"/>
        <line x1="-5" y1="-10" x2="-5" y2="10" stroke="#000" stroke-width="2"/>
        <line x1="3" y1="-10" x2="3" y2="10" stroke="#000" stroke-width="2"/>
        <!-- Translucent wings -->
        <ellipse cx="-2" cy="-14" rx="10" ry="6" fill="#e0f2fe" opacity="0.7"/>
        <text x="20" y="5" fill="#fde047" font-size="11" font-weight="bold">Honeybee</text>
      </g>
      <!-- Spiny pollen on bee legs -->
      <circle cx="258" cy="72" r="3" fill="#ea580c"/>
      <circle cx="262" cy="73" r="3" fill="#ea580c"/>
      <text x="220" y="105" fill="#ea580c" font-size="10">Sticky, Spiny Pollen Grains</text>
    `;
    det.innerHTML = "<strong>Insect Pollination (Entomophily):</strong> Sunflower, hibiscus, and marigold produce colorful petals, fragrant scents, and sweet nectar. Rough, spiny pollen clings firmly to visiting honeybees for targeted transfer.";
  } else if(vec === 'water'){
    document.getElementById('c11s7_btn_wat').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-blue-600 text-white transition';
    tag.textContent = "Aquatic Medium • Vallisneria & Hydrilla";
    svg.innerHTML = `
      <!-- Water surface waves -->
      <path d="M50,70 Q100,60 150,70 Q200,80 250,70 Q300,60 350,70" stroke="#0284c7" stroke-width="3" fill="none"/>
      <rect x="50" y="70" width="320" height="70" fill="#0369a1" opacity="0.2"/>
      <!-- Submerged plant Vallisneria -->
      <path d="M120,140 Q130,100 140,75" stroke="#15803d" stroke-width="2.5" fill="none"/>
      <circle cx="140" cy="72" r="4" fill="#fde047"/>
      <!-- Floating pollen on water surface -->
      <circle cx="200" cy="68" r="3" fill="#fef08a"/><circle cx="240" cy="70" r="3" fill="#fef08a"/>
      <text x="70" y="50" fill="#38bdf8" font-size="11" font-weight="bold">Water Surface Film Currents</text>
      <text x="160" y="110" fill="#86efac" font-size="10">Floating Male Flowers / Pollen in Vallisneria</text>
    `;
    det.innerHTML = "<strong>Water Pollination (Hydrophily):</strong> In aquatic plants like Vallisneria and Hydrilla, pollen grains or male flowers detach and float on the water surface until drifting into receptive female stigmas.";
  } else {
    document.getElementById('c11s7_btn_bir').className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
    tag.textContent = "Bird Vectors (Ornithophily) • Sunbirds";
    svg.innerHTML = `
      <!-- Sturdy tubular flower -->
      <path d="M140,110 L190,80 Q220,70 240,60 L240,85 Q210,90 170,120 Z" fill="#e11d48" stroke="#be123c" stroke-width="2"/>
      <!-- Sunbird with long slender curved beak -->
      <path d="M300,50 Q280,45 260,65 Q250,68 235,72" stroke="#f59e0b" stroke-width="2" fill="none"/>
      <ellipse cx="305" cy="50" rx="15" ry="12" fill="#047857"/>
      <circle cx="295" cy="46" r="2" fill="#000"/>
      <text x="240" y="35" fill="#f43f5e" font-size="11" font-weight="bold">Sunbird Visiting Coral Tree</text>
      <text x="140" y="140" fill="#fda4af" font-size="10">Dilute Nectar inside Sturdy Floral Tube</text>
    `;
    det.innerHTML = "<strong>Bird Pollination (Ornithophily):</strong> Large, sturdy flowers like the Indian coral tree visited by sunbirds and white-eyes. Flowers produce abundant dilute nectar inside robust floral cups that withstand avian visits.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S7('wind'));
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Stage:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC11S8(1)" id="c11s8_btn_1" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">1. Germination</button>
        <button onclick="setC11S8(2)" id="c11s8_btn_2" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Tube Growth</button>
        <button onclick="setC11S8(3)" id="c11s8_btn_3" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Fertilisation</button>
        <button onclick="setC11S8(4)" id="c11s8_btn_4" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">4. Seed &amp; Fruit</button>
      </div>
    </div>
    <span class="text-xs text-emerald-300 font-semibold" id="c11s8_tag">Pollen Adherence to Sticky Stigma</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <svg viewBox="0 0 420 150" class="w-full h-36">
      <!-- Pistil Outline -->
      <ellipse cx="200" cy="25" rx="14" ry="6" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
      <path d="M192,28 L192,80 Q160,90 160,120 Q160,145 200,145 Q240,145 240,120 Q240,90 208,28 Z" fill="#14532d" opacity="0.4" stroke="#16a34a" stroke-width="2"/>
      <!-- Ovule with egg inside -->
      <ellipse cx="200" cy="115" rx="16" ry="14" fill="#047857" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="200" cy="118" r="4" fill="#fde047" id="c11s8_egg"/>
      <text x="225" y="122" fill="#fde047" font-size="10">Egg Cell (n)</text>
      <!-- Pollen Grain on Stigma -->
      <circle cx="200" cy="22" r="5" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
      <!-- Dynamic Pollen Tube -->
      <path id="c11s8_tube" d="M200,26 L200,35" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
      <!-- Male Gametes -->
      <circle id="c11s8_gam1" cx="200" cy="32" r="2.5" fill="#ef4444"/>
    </svg>
    <div id="c11s8_desc" class="p-2.5 mt-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 text-center w-full max-w-lg">
      Compatible pollen lands on sticky stigma and absorbs sugary fluid, initiating germination.
    </div>
  </div>

  <div class="flex items-center justify-between text-[11px] bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-lg text-slate-400">
    <span>Father of Indian Embryology: Panchanan Maheshwari pioneered in-vitro fertilisation and test-tube plant embryo culturing!</span>
  </div>
</div>
<script>
window.setC11S8 = function(stg){
  for(let i=1; i<=4; i++){
    document.getElementById('c11s8_btn_' + i).className = (i === stg) ?
      'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition' :
      'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  }
  const tube = document.getElementById('c11s8_tube');
  const gam = document.getElementById('c11s8_gam1');
  const desc = document.getElementById('c11s8_desc');
  const tag = document.getElementById('c11s8_tag');

  if(stg === 1){
    tag.textContent = "1. Pollen Germination on Stigma";
    tube.setAttribute('d', 'M200,26 L200,35');
    gam.setAttribute('cy', '32');
    desc.innerHTML = "<strong>Stage 1 - Germination:</strong> Stigma secretes sugary moisture. Compatible pollen grain hydrates, and a slender pollen tube emerges through a germ pore.";
  } else if(stg === 2){
    tag.textContent = "2. Chemotropic Tube Growth Down Style";
    tube.setAttribute('d', 'M200,26 L200,85');
    gam.setAttribute('cy', '75');
    desc.innerHTML = "<strong>Stage 2 - Tube Elongation:</strong> Pollen tube grows downward through the style via chemotropism, carrying two haploid male gametes toward the ovary.";
  } else if(stg === 3){
    tag.textContent = "3. Micropyle Entry & Syngamy (Fertilisation)";
    tube.setAttribute('d', 'M200,26 L200,90 Q200,118 196,118');
    gam.setAttribute('cy', '118');
    desc.innerHTML = "<strong>Stage 3 - Fertilisation (Syngamy):</strong> Pollen tube penetrates ovule through micropyle. One male gamete fuses with the egg cell forming a diploid zygote (2n)!";
  } else {
    tag.textContent = "4. Ovule &rarr; Seed | Ovary &rarr; Fruit";
    tube.setAttribute('d', 'M200,26 L200,120');
    gam.setAttribute('cy', '118');
    desc.innerHTML = "<strong>Stage 4 - Post-Fertilisation Changes:</strong> Zygote becomes an embryo. The ovule develops a tough seed coat, maturing into a seed. The surrounding ovary wall ripens into a fruit!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC11S8(1));
</script>"""
}

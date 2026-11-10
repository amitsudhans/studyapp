#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 4: Getting to Know Plants
Simulators Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌿 Plant Growth Forms Explorer</h3>
    <span id="formTag1" style="background: #0284c7; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Selected: Tree (15 m)</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: linear-gradient(180deg, #1e293b 0%, #0f172a 75%, #3f2e21 75%, #292017 100%); border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Ground line -->
      <line x1="0" y1="158" x2="500" y2="158" stroke="#15803d" stroke-width="4" />
      
      <!-- Scale Ruler (meters) on left -->
      <line x1="25" y1="20" x2="25" y2="158" stroke="#64748b" stroke-width="1.5" />
      <text x="5" y="30" fill="#94a3b8" font-size="8">15 m</text>
      <text x="5" y="80" fill="#94a3b8" font-size="8">8 m</text>
      <text x="5" y="125" fill="#94a3b8" font-size="8">2 m</text>
      <text x="5" y="155" fill="#94a3b8" font-size="8">0 m</text>

      <!-- 1. Tree Display -->
      <g id="figTree" style="transition: opacity 0.3s;">
        <rect x="180" y="60" width="22" height="98" fill="#78350f" stroke="#451a03" stroke-width="2"/>
        <!-- Spreading Canopy -->
        <circle cx="191" cy="55" r="45" fill="#15803d" />
        <circle cx="165" cy="65" r="30" fill="#16a34a" />
        <circle cx="215" cy="65" r="30" fill="#16a34a" />
        <!-- Underground Taproot -->
        <path d="M 191,158 L 191,195 M 191,175 L 175,190 M 191,180 L 205,192" stroke="#92400e" stroke-width="2.5" fill="none"/>
      </g>

      <!-- 2. Shrub Display (Bushy multistem) -->
      <g id="figShrub" opacity="0.2" style="transition: opacity 0.3s;">
        <!-- Multiple woody stems from base -->
        <path d="M 300,158 Q 285,130 280,105 M 300,158 Q 295,120 295,95 M 300,158 Q 305,120 310,95 M 300,158 Q 315,130 325,108" stroke="#92400e" stroke-width="2.5" fill="none"/>
        <circle cx="280" cy="100" r="14" fill="#16a34a" />
        <circle cx="295" cy="90" r="16" fill="#15803d" />
        <circle cx="310" cy="90" r="16" fill="#15803d" />
        <circle cx="325" cy="105" r="14" fill="#16a34a" />
      </g>

      <!-- 3. Herb Display (Soft green) -->
      <g id="figHerb" opacity="0.2" style="transition: opacity 0.3s;">
        <path d="M 390,158 Q 388,140 390,125" stroke="#22c55e" stroke-width="2" fill="none"/>
        <ellipse cx="384" cy="135" rx="6" ry="3" fill="#4ade80" />
        <ellipse cx="396" cy="130" rx="6" ry="3" fill="#4ade80" />
        <ellipse cx="390" cy="120" rx="5" ry="4" fill="#4ade80" />
      </g>

      <!-- 4. Tiny Moss (Carpet) -->
      <g id="figMoss" opacity="0.2" style="transition: opacity 0.3s;">
        <ellipse cx="440" cy="157" rx="16" ry="4" fill="#84cc16" />
        <circle cx="435" cy="154" r="2" fill="#a3e635" />
        <circle cx="445" cy="154" r="2" fill="#a3e635" />
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim1Select(0)" id="fBtn0" style="background: #0284c7; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌳 Tree</button>
    <button onclick="sim1Select(1)" id="fBtn1" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌺 Shrub</button>
    <button onclick="sim1Select(2)" id="fBtn2" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌱 Herb</button>
    <button onclick="sim1Select(3)" id="fBtn3" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🟩 Moss</button>
  </div>

  <div id="sim1Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🌳 <strong>Tree:</strong> Defined by a single stout woody trunk covered in bark, elevated spreading branches, and deep anchoring taproots reaching up to 15-30 meters high.
  </div>
</div>

<script>
const sim1Data = [
  {name: "Selected: Tree (15 m)", desc: "🌳 <strong>Tree:</strong> Defined by a single stout woody trunk covered in bark, elevated spreading branches, and deep anchoring taproots reaching up to 15-30 meters high.", id: "figTree"},
  {name: "Selected: Shrub (2 m)", desc: "🌺 <strong>Shrub:</strong> Medium-sized bushy plant with multiple slender woody stems arising near ground level rather than a single trunk. Examples: Rose, Hibiscus, Tulsi.", id: "figShrub"},
  {name: "Selected: Herb (40 cm)", desc: "🌱 <strong>Herb:</strong> Small plant with soft, green, non-woody flexible stems rich in chlorophyll. Lives for one or two seasons. Examples: Mint, Coriander, Tomato.", id: "figHerb"},
  {name: "Selected: Moss (1 cm)", desc: "🟩 <strong>Moss:</strong> Tiny, carpet-like non-vascular green plants that hug damp stones and tree bark, absorbing water directly without true roots.", id: "figMoss"}
];

function sim1Select(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`fBtn${i}`).style.background = (i === idx) ? '#0284c7' : '#334155';
    document.getElementById(sim1Data[i].id).setAttribute('opacity', (i === idx) ? '1' : '0.2');
  }
  document.getElementById('formTag1').innerText = sim1Data[idx].name;
  document.getElementById('sim1Info').innerHTML = sim1Data[idx].desc;
}
</script>
""",

    2: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌳 Indigenous Tree Arboretum</h3>
    <span id="treeSpeciesBadge" style="background: #15803d; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Banyan Tree (Ficus benghalensis)</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Sky & Ground -->
      <rect x="0" y="160" width="500" height="50" fill="#3f2e21" />
      <line x1="0" y1="160" x2="500" y2="160" stroke="#15803d" stroke-width="3" />

      <!-- Center Tree Trunk -->
      <g id="arboretumTree">
        <!-- Main Trunk -->
        <path d="M 230,160 Q 235,110 230,70 L 270,70 Q 265,110 270,160 Z" fill="#78350f" stroke="#451a03" stroke-width="2"/>
        
        <!-- Hanging Aerial Prop Roots (Banyan specific, toggleable) -->
        <g id="propRootsGroup">
          <line x1="180" y1="70" x2="180" y2="160" stroke="#92400e" stroke-width="3"/>
          <line x1="320" y1="70" x2="320" y2="160" stroke="#92400e" stroke-width="3"/>
          <text x="180" y="150" fill="#fbbf24" font-size="8">Prop Root</text>
        </g>

        <!-- Wide Spreading Leafy Canopy -->
        <circle id="treeCanopy" cx="250" cy="55" r="55" fill="#15803d" stroke="#166534" stroke-width="2"/>
        <circle cx="210" cy="65" r="35" fill="#16a34a" opacity="0.8"/>
        <circle cx="290" cy="65" r="35" fill="#16a34a" opacity="0.8"/>

        <!-- Underground Taproots -->
        <path d="M 250,160 L 250,205 M 250,180 L 225,200 M 250,185 L 275,200" stroke="#92400e" stroke-width="3" fill="none"/>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim2ShowTree(0)" id="tBtn0" style="background: #0284c7; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌳 Banyan</button>
    <button onclick="sim2ShowTree(1)" id="tBtn1" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🍃 Peepal</button>
    <button onclick="sim2ShowTree(2)" id="tBtn2" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🥭 Mango</button>
    <button onclick="sim2ShowTree(3)" id="tBtn3" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🏜️ Khejri</button>
  </div>

  <div id="sim2Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🌳 <strong>Banyan Tree:</strong> India's national tree, famous for massive aerial prop roots that grow downwards from horizontal branches to anchor in the soil like secondary supporting pillars!
  </div>
</div>

<script>
const sim2Data = [
  {name: "Banyan Tree (Ficus benghalensis)", desc: "🌳 <strong>Banyan Tree:</strong> India's national tree, famous for massive aerial prop roots that grow downwards from horizontal branches to anchor in the soil like secondary supporting pillars!", props: true, color: "#15803d"},
  {name: "Peepal Tree (Ficus religiosa)", desc: "🍃 <strong>Peepal Tree:</strong> Revered for heart-shaped glossy leaves with extended drip-tips that flutter in the slightest breeze, releasing oxygen round the clock.", props: false, color: "#16a34a"},
  {name: "Mango Tree (Mangifera indica)", desc: "🥭 <strong>Mango Tree:</strong> Evergreen fruit giant producing fragrant spring inflorescences that develop into the king of tropical summer fruits.", props: false, color: "#047857"},
  {name: "Khejri Tree (Prosopis cineraria)", desc: "🏜️ <strong>Desert Khejri:</strong> Thar desert lifesaver with deep taproots reaching 35 meters down to find subterranean water, surviving severe droughts.", props: false, color: "#65a30d"}
];

function sim2ShowTree(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`tBtn${i}`).style.background = (i === idx) ? '#0284c7' : '#334155';
  }
  const item = sim2Data[idx];
  document.getElementById('treeSpeciesBadge').innerText = item.name;
  document.getElementById('sim2Info').innerHTML = item.desc;
  document.getElementById('propRootsGroup').style.display = item.props ? 'block' : 'none';
  document.getElementById('treeCanopy').setAttribute('fill', item.color);
}
</script>
""",

    3: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🔬 Tactile Leaf Texture Lab</h3>
    <button onclick="sim3PourWater()" id="waterDropBtn3" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">💧 Pour Raindrop</button>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <!-- Leaf A: Smooth Waxy Cuticle (Mango/Peepal) -->
    <div style="background: #1e293b; border-radius: 8px; padding: 10px; border: 1px solid #334155; text-align: center;">
      <div style="font-weight: bold; color: #4ade80; font-size: 0.85rem; margin-bottom: 4px;">Smooth & Glossy Cuticle (Mango)</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <!-- Smooth Mango Leaf Blade -->
        <path d="M 20,60 Q 80,25 140,60 Q 80,95 20,60 Z" fill="#15803d" stroke="#16a34a" stroke-width="2"/>
        <line x1="20" y1="60" x2="140" y2="60" stroke="#facc15" stroke-width="1.5" />
        <!-- Shiny highlight -->
        <path d="M 35,55 Q 80,35 125,55" stroke="#ffffff" stroke-width="1.5" opacity="0.6" fill="none"/>
        <!-- Water drop rolling off -->
        <circle id="dropSmooth" cx="50" cy="50" r="5" fill="#38bdf8" style="transition: transform 1s ease-in;"/>
      </svg>
      <div style="font-size: 0.75rem; color: #94a3b8;">Water glides off instantly</div>
    </div>

    <!-- Leaf B: Rough Hairy Surface (Teak) -->
    <div style="background: #1e293b; border-radius: 8px; padding: 10px; border: 1px solid #334155; text-align: center;">
      <div style="font-weight: bold; color: #facc15; font-size: 0.85rem; margin-bottom: 4px;">Rough & Leathery (Teak)</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <!-- Rough Teak Leaf with Trichome hairs -->
        <path d="M 20,60 Q 80,15 140,60 Q 80,105 20,60 Z" fill="#166534" stroke="#14532d" stroke-width="2"/>
        <line x1="20" y1="60" x2="140" y2="60" stroke="#ca8a04" stroke-width="1.5" />
        <!-- Microscopic hairs (dots & small dashes) -->
        <g stroke="#86efac" stroke-width="1">
          <line x1="50" y1="45" x2="50" y2="40" /><line x1="70" y1="40" x2="70" y2="35" />
          <line x1="90" y1="42" x2="90" y2="37" /><line x1="110" y1="50" x2="110" y2="45" />
          <line x1="60" y1="75" x2="60" y2="80" /><line x1="80" y1="80" x2="80" y2="85" />
          <line x1="100" y1="78" x2="100" y2="83" />
        </g>
        <!-- Water drop caught on hairs -->
        <circle id="dropRough" cx="80" cy="55" r="5" fill="#38bdf8" />
      </svg>
      <div style="font-size: 0.75rem; color: #94a3b8;">Hairs trap moisture & deter pests</div>
    </div>
  </div>

  <div id="sim3Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "Pour Raindrop" to observe how surface cuticles allow water to roll off smooth mango leaves!
  </div>
</div>

<script>
let sim3DropRolled = false;
function sim3PourWater() {
  sim3DropRolled = !sim3DropRolled;
  const ds = document.getElementById('dropSmooth');
  if(sim3DropRolled) {
    ds.setAttribute('transform', 'translate(85, 10)');
    document.getElementById('sim3Info').innerHTML = '💧 <strong>Waterproof Cuticle Action:</strong> Raindrops roll effortlessly off the smooth waxy cuticle of the mango leaf, keeping stomata clear for gas exchange!';
  } else {
    ds.setAttribute('transform', 'translate(0, 0)');
    document.getElementById('sim3Info').innerText = 'Raindrop reset to leaf base. Click to pour again!';
  }
}
</script>
""",

    4: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🍇 Jamun Ripening Stages</h3>
    <span id="jamunStageBadge" style="background: #15803d; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Stage 1: Unripe Green Berry</span>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155; display: flex; align-items: center; justify-content: center;">
    <svg viewBox="0 0 400 180" style="width: 100%; height: 100%;">
      <!-- Twig and Leaves -->
      <path d="M 50,40 Q 150,70 350,50" stroke="#78350f" stroke-width="5" fill="none"/>
      <!-- Green Leaf 1 -->
      <path d="M 120,58 Q 160,20 220,50 Q 160,75 120,58 Z" fill="#15803d" />
      <!-- Green Leaf 2 -->
      <path d="M 230,55 Q 270,15 320,40 Q 280,70 230,55 Z" fill="#16a34a" />

      <!-- Hanging Jamun Berry Cluster (Centerpiece) -->
      <g id="jamunCluster">
        <line x1="200" y1="65" x2="200" y2="95" stroke="#78350f" stroke-width="2"/>
        <!-- Berry 1 (Center) -->
        <ellipse id="berry1" cx="200" cy="115" rx="20" ry="26" fill="#84cc16" stroke="#4d7c0f" stroke-width="2"/>
        <!-- Berry 2 (Left) -->
        <ellipse id="berry2" cx="175" cy="108" rx="16" ry="22" fill="#84cc16" stroke="#4d7c0f" stroke-width="2"/>
        <!-- Berry 3 (Right) -->
        <ellipse id="berry3" cx="225" cy="110" rx="17" ry="23" fill="#84cc16" stroke="#4d7c0f" stroke-width="2"/>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;">
    <button onclick="sim4SetStage(1)" id="jBtn1" style="background: #15803d; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🟢 1. Sour Green</button>
    <button onclick="sim4SetStage(2)" id="jBtn2" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🔴 2. Turning Pink</button>
    <button onclick="sim4SetStage(3)" id="jBtn3" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🟣 3. Sweet Purple</button>
  </div>

  <div id="sim4Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🟢 <strong>Stage 1 (Unripe):</strong> Packed with sour acids and green chlorophyll pigments, camouflaging the hard fruit among foliage so animals do not eat immature seeds.
  </div>
</div>

<script>
const sim4Stages = [
  {name: "Stage 1: Unripe Green Berry", desc: "🟢 <strong>Stage 1 (Unripe):</strong> Packed with sour acids and green chlorophyll pigments, camouflaging the hard fruit among foliage so animals do not eat immature seeds.", color: "#84cc16", stroke: "#4d7c0f", badgeBg: "#15803d"},
  {name: "Stage 2: Turning Reddish-Pink", desc: "🔴 <strong>Stage 2 (Ripening):</strong> Chlorophyll breaks down as natural fruit sugars develop, accumulating bright red anthocyanin pigments.", color: "#e11d48", stroke: "#9f1239", badgeBg: "#be123c"},
  {name: "Stage 3: Deep Purple-Black Ripe", desc: "🟣 <strong>Stage 3 (Fully Ripe):</strong> Soft, juicy, sweet-astringent, and rich in dark purple antioxidants. Attracts birds that eat the fruit and disperse healthy seeds far away!", color: "#3b0764", stroke: "#581c87", badgeBg: "#581c87"}
];

function sim4SetStage(stage) {
  const s = sim4Stages[stage-1];
  for(let i=1; i<=3; i++) {
    document.getElementById(`jBtn${i}`).style.background = (i === stage) ? '#0284c7' : '#334155';
  }
  document.getElementById('berry1').setAttribute('fill', s.color);
  document.getElementById('berry1').setAttribute('stroke', s.stroke);
  document.getElementById('berry2').setAttribute('fill', s.color);
  document.getElementById('berry2').setAttribute('stroke', s.stroke);
  document.getElementById('berry3').setAttribute('fill', s.color);
  document.getElementById('berry3').setAttribute('stroke', s.stroke);

  const badge = document.getElementById('jamunStageBadge');
  badge.innerText = s.name;
  badge.style.background = s.badgeBg;
  document.getElementById('sim4Info').innerHTML = s.desc;
}
</script>
""",

    5: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌺 Bushy Garden Shrub Explorer</h3>
    <span id="shrubBadge" style="background: #be123c; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Scarlet Hibiscus (China Rose)</span>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Soil ground level -->
      <rect x="0" y="160" width="500" height="40" fill="#3f2e21" />
      <line x1="0" y1="160" x2="500" y2="160" stroke="#15803d" stroke-width="3" />

      <!-- Multiple woody stems emerging near ground (Shrub hallmark) -->
      <g stroke="#78350f" stroke-width="3" stroke-linecap="round" fill="none">
        <path d="M 250,160 Q 220,120 190,80" />
        <path d="M 250,160 Q 235,110 220,60" />
        <path d="M 250,160 Q 255,100 250,50" />
        <path d="M 250,160 Q 270,110 285,65" />
        <path d="M 250,160 Q 285,120 315,85" />
      </g>

      <!-- Shrub Foliage & Flowers -->
      <!-- Dense rounded foliage -->
      <circle cx="210" cy="80" r="28" fill="#15803d" opacity="0.9"/>
      <circle cx="250" cy="65" r="32" fill="#16a34a" opacity="0.9"/>
      <circle cx="290" cy="80" r="28" fill="#15803d" opacity="0.9"/>

      <!-- Flowers (Interactive Color changes) -->
      <g id="shrubFlowers">
        <!-- Center Flower -->
        <circle id="shrubFlw1" cx="250" cy="50" r="12" fill="#e11d48" />
        <circle cx="250" cy="50" r="4" fill="#fde047" />
        <!-- Left Flower -->
        <circle id="shrubFlw2" cx="190" cy="75" r="10" fill="#e11d48" />
        <circle cx="190" cy="75" r="3" fill="#fde047" />
        <!-- Right Flower -->
        <circle id="shrubFlw3" cx="310" cy="75" r="10" fill="#e11d48" />
        <circle cx="310" cy="75" r="3" fill="#fde047" />
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim5SelectShrub(0)" id="sBtn0" style="background: #0284c7; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌺 Hibiscus</button>
    <button onclick="sim5SelectShrub(1)" id="sBtn1" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌹 Rose</button>
    <button onclick="sim5SelectShrub(2)" id="sBtn2" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌿 Tulsi</button>
    <button onclick="sim5SelectShrub(3)" id="sBtn3" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🍃 Curry Leaf</button>
  </div>

  <div id="sim5Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🌺 <strong>Hibiscus:</strong> Classic garden shrub displaying 5 vibrant scarlet petals and a long projecting yellow stamen column, supported by multiple woody branches from ground level.
  </div>
</div>

<script>
const sim5Data = [
  {name: "Scarlet Hibiscus (China Rose)", desc: "🌺 <strong>Hibiscus:</strong> Classic garden shrub displaying 5 vibrant scarlet petals and a long projecting yellow stamen column, supported by multiple woody branches from ground level.", color: "#e11d48", badge: "#be123c"},
  {name: "Fragrant Rose (Rosa)", desc: "🌹 <strong>Rose Shrub:</strong> Woody prickly shrub with multi-layered petals rich in fragrant rose oil, cultivated worldwide for beauty and perfume.", color: "#f43f5e", badge: "#e11d48"},
  {name: "Holy Basil (Tulsi)", desc: "🌿 <strong>Tulsi Shrub:</strong> Revered medicinal shrub with aromatic leaves and purple flower spikes packed with antimicrobial essential oils like eugenol.", color: "#a855f7", badge: "#7e22ce"},
  {name: "Curry Leaf (Murraya koenigii)", desc: "🍃 <strong>Curry Leaf Shrub:</strong> Aromatic culinary shrub whose glossy pinnate leaves provide essential savory seasoning across traditional dishes.", color: "#84cc16", badge: "#4d7c0f"}
];

function sim5SelectShrub(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`sBtn${i}`).style.background = (i === idx) ? '#0284c7' : '#334155';
  }
  const item = sim5Data[idx];
  document.getElementById('shrubBadge').innerText = item.name;
  document.getElementById('shrubBadge').style.background = item.badge;
  document.getElementById('shrubFlw1').setAttribute('fill', item.color);
  document.getElementById('shrubFlw2').setAttribute('fill', item.color);
  document.getElementById('shrubFlw3').setAttribute('fill', item.color);
  document.getElementById('sim5Info').innerHTML = item.desc;
}
</script>
""",

    6: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🫘 Legume Shrub Pulses & Root Nodules</h3>
    <button onclick="sim6ToggleNodules()" id="noduleBtn6" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🔬 Zoom into Root Nodules</button>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Ground line -->
      <rect x="0" y="110" width="500" height="90" fill="#3f2e21" />
      <line x1="0" y1="110" x2="500" y2="110" stroke="#15803d" stroke-width="3" />

      <!-- Upper Legume Shrub (Above Ground) -->
      <path d="M 250,110 Q 230,70 210,40 M 250,110 Q 250,60 250,30 M 250,110 Q 270,70 290,40" stroke="#78350f" stroke-width="2.5" fill="none"/>
      <!-- Hanging Pulse Pods (Toor / Moong) -->
      <g fill="#ca8a04" stroke="#854d0e" stroke-width="1.5">
        <path d="M 210,50 Q 200,65 205,80 Q 212,65 210,50 Z" />
        <path d="M 250,45 Q 242,60 246,75 Q 254,60 250,45 Z" />
        <path d="M 290,50 Q 300,65 295,80 Q 288,65 290,50 Z" />
      </g>
      <text x="215" y="70" fill="#fef08a" font-size="9" font-weight="bold">Pods</text>

      <!-- Underground Root System with Nodules -->
      <g stroke="#d97706" stroke-width="2" fill="none">
        <path d="M 250,110 L 250,185" />
        <path d="M 250,130 L 210,165" />
        <path d="M 250,145 L 290,175" />
        <path d="M 250,160 L 230,190" />
      </g>

      <!-- Symbiotic Root Nodules (Nitrogen Factories) -->
      <g id="noduleGroup" fill="#fbbf24">
        <circle cx="215" cy="160" r="4" />
        <circle cx="225" cy="150" r="3.5" />
        <circle cx="250" cy="140" r="4.5" />
        <circle cx="270" cy="155" r="4" />
        <circle cx="285" cy="170" r="3.5" />
        <circle cx="235" cy="185" r="3" />
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim6ShowPulse('toor')" style="background: #eab308; color: #1e293b; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">Toor Dal</button>
    <button onclick="sim6ShowPulse('masoor')" style="background: #f97316; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">Masoor Dal</button>
    <button onclick="sim6ShowPulse('moong')" style="background: #22c55e; color: #1e293b; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">Moong Dal</button>
    <button onclick="sim6ShowPulse('urad')" style="background: #64748b; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">Urad Dal</button>
  </div>

  <div id="sim6Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🫘 <strong>Legume Superpower:</strong> Pulses (toor, masoor, moong, urad) are high-protein seeds harvested from legume shrubs whose roots naturally fertilize the soil with nitrogen!
  </div>
</div>

<script>
let sim6NodulesHighlighted = false;
function sim6ToggleNodules() {
  sim6NodulesHighlighted = !sim6NodulesHighlighted;
  const ng = document.getElementById('noduleGroup');
  const btn = document.getElementById('noduleBtn6');
  if(sim6NodulesHighlighted) {
    ng.setAttribute('fill', '#ef4444');
    btn.innerText = '🔍 Normal View';
    document.getElementById('sim6Info').innerHTML = '🔬 <strong>Rhizobium Bacteria at Work:</strong> Inside these round nodules, millions of microscopic bacteria capture nitrogen directly from atmospheric air, converting it into natural plant fertilizer without chemicals!';
  } else {
    ng.setAttribute('fill', '#fbbf24');
    btn.innerText = '🔬 Zoom into Root Nodules';
    document.getElementById('sim6Info').innerText = 'Root nodules returned to normal view. Click pulse buttons below to inspect specific crops!';
  }
}

function sim6ShowPulse(type) {
  if(type === 'toor') {
    document.getElementById('sim6Info').innerHTML = '🟡 <strong>Toor Dal (Pigeon Pea):</strong> Harvested from tall woody legume shrubs. Rich in dietary protein, essential for building strong muscles in children.';
  } else if(type === 'masoor') {
    document.getElementById('sim6Info').innerHTML = '🟠 <strong>Masoor Dal (Red Lentil):</strong> Fast-cooking nutritious pulse high in iron and fiber, harvested from delicate bushy legume plants.';
  } else if(type === 'moong') {
    document.getElementById('sim6Info').innerHTML = '🟢 <strong>Moong Dal (Green Gram):</strong> Easily digestible pulse rich in antioxidants, commonly sprouted to multiply vitamin C content!';
  } else if(type === 'urad') {
    document.getElementById('sim6Info').innerHTML = '⚪ <strong>Urad Dal (Black Gram):</strong> Dense in calcium and magnesium, traditionally ground with rice to prepare fermented idli and dosa batters.';
  }
}
</script>
""",

    7: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌱 Herb Stem Flexibility & Kitchen Garden</h3>
    <button onclick="sim7BendStem()" id="bendBtn7" style="background: #16a34a; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🔄 Test Stem Flexibility</button>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155; display: flex; align-items: center; justify-content: center;">
    <svg viewBox="0 0 400 180" style="width: 100%; height: 100%;">
      <!-- Clay Flower Pot -->
      <polygon points="160,130 240,130 230,175 170,175" fill="#b45309" stroke="#78350f" stroke-width="2"/>
      <rect x="155" y="120" width="90" height="12" rx="2" fill="#d97706" />

      <!-- Flexible Green Herb Stem (Mint / Coriander) -->
      <g id="herbStemGroup" style="transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1); transform-origin: 200px 120px;">
        <path id="herbStemPath" d="M 200,120 Q 200,80 200,40" stroke="#22c55e" stroke-width="4" stroke-linecap="round" fill="none"/>
        <!-- Soft green leaves along stem -->
        <ellipse cx="190" cy="95" rx="10" ry="5" fill="#4ade80" transform="rotate(-30 190 95)"/>
        <ellipse cx="210" cy="90" rx="10" ry="5" fill="#4ade80" transform="rotate(30 210 90)"/>
        <ellipse cx="190" cy="65" rx="9" ry="4" fill="#4ade80" transform="rotate(-30 190 65)"/>
        <ellipse cx="210" cy="60" rx="9" ry="4" fill="#4ade80" transform="rotate(30 210 60)"/>
        <!-- Top tender leaf tip -->
        <ellipse cx="200" cy="38" rx="8" ry="5" fill="#86efac" />
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim7SelectHerb('mint')" style="background: #15803d; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌱 Mint (Pudina)</button>
    <button onclick="sim7SelectHerb('coriander')" style="background: #16a34a; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌿 Coriander</button>
    <button onclick="sim7SelectHerb('tomato')" style="background: #dc2626; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🍅 Tomato</button>
    <button onclick="sim7SelectHerb('mustard')" style="background: #ca8a04; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌼 Mustard</button>
  </div>

  <div id="sim7Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "Test Stem Flexibility" to see how soft, green herbaceous stems bend under wind without snapping!
  </div>
</div>

<script>
let sim7Bending = false;
function sim7BendStem() {
  sim7Bending = !sim7Bending;
  const sg = document.getElementById('herbStemGroup');
  if(sim7Bending) {
    sg.style.transform = 'rotate(35deg)';
    document.getElementById('sim7Info').innerHTML = '🌿 <strong>Flexible Non-Woody Stem:</strong> Notice how the tender green stem bends gracefully under wind pressure without breaking! High water turgor pressure keeps herbs upright.';
  } else {
    sg.style.transform = 'rotate(0deg)';
    document.getElementById('sim7Info').innerText = 'Stem returned upright. Herbs lack hard wood, relying on cellular turgidity to stand tall.';
  }
}

function sim7SelectHerb(type) {
  if(type === 'mint') {
    document.getElementById('sim7Info').innerHTML = '🌱 <strong>Mint (Pudina):</strong> Aromatic herbaceous plant with square green stems and refreshing menthol aroma used in digestive chutneys and cool teas.';
  } else if(type === 'coriander') {
    document.getElementById('sim7Info').innerHTML = '🌿 <strong>Coriander (Dhaniya):</strong> Delicate culinary herb with feathery compound leaves rich in vitamin A, widely used for fragrant garnishing.';
  } else if(type === 'tomato') {
    document.getElementById('sim7Info').innerHTML = '🍅 <strong>Tomato Herb:</strong> Herbaceous plant with hairy green stems producing succulent red culinary fruits packed with lycopene.';
  } else if(type === 'mustard') {
    document.getElementById('sim7Info').innerHTML = '🌼 <strong>Mustard Herb:</strong> Fast-growing winter herb with edible green leaves (sarson ka saag) and bright golden blossoms that yield mustard seeds.';
  }
}
</script>
""",

    8: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌾 Staple Grain Grasses & Basal Regrowth</h3>
    <button onclick="sim8Graze()" id="grazeBtn8" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">✂️ Graze / Mow Tops</button>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Soil level -->
      <rect x="0" y="160" width="500" height="40" fill="#3f2e21" />
      <line x1="0" y1="160" x2="500" y2="160" stroke="#15803d" stroke-width="3" />

      <!-- Basal Meristem Growth Crown (Ground level) -->
      <ellipse cx="250" cy="160" rx="40" ry="6" fill="#84cc16" opacity="0.6"/>
      <text x="250" y="175" text-anchor="middle" fill="#fef08a" font-size="9" font-weight="bold">Basal Growth Zone (Meristem)</text>

      <!-- Grass Blades / Cereal Stems (Wheat / Paddy) -->
      <g id="grassBladesGroup" style="transition: all 0.6s ease-out;">
        <!-- Stem 1 with Grain Head -->
        <line x1="220" y1="160" x2="210" y2="60" stroke="#22c55e" stroke-width="3" />
        <ellipse cx="208" cy="50" rx="5" ry="12" fill="#facc15" stroke="#ca8a04" />
        <!-- Stem 2 (Center) -->
        <line x1="250" y1="160" x2="250" y2="40" stroke="#22c55e" stroke-width="3" />
        <ellipse cx="250" cy="30" rx="6" ry="14" fill="#facc15" stroke="#ca8a04" />
        <!-- Stem 3 -->
        <line x1="280" y1="160" x2="290" y2="55" stroke="#22c55e" stroke-width="3" />
        <ellipse cx="292" cy="45" rx="5" ry="12" fill="#facc15" stroke="#ca8a04" />
        <!-- Narrow blade leaves with parallel venation -->
        <path d="M 220,130 Q 180,100 160,110" stroke="#4ade80" stroke-width="3" fill="none"/>
        <path d="M 280,130 Q 320,100 340,110" stroke="#4ade80" stroke-width="3" fill="none"/>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim8SelectGrain('paddy')" style="background: #15803d; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌾 Paddy (Rice)</button>
    <button onclick="sim8SelectGrain('wheat')" style="background: #b45309; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🍞 Wheat</button>
    <button onclick="sim8SelectGrain('bajra')" style="background: #475569; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🫓 Bajra</button>
    <button onclick="sim8SelectGrain('ragi')" style="background: #78350f; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🥣 Ragi</button>
  </div>

  <div id="sim8Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🌾 <strong>Cereal Grasses:</strong> Grains like rice, wheat, and millets are seeds of large grasses whose basal meristem allows them to survive grazing and trampling!
  </div>
</div>

<script>
let sim8Grazed = false;
function sim8Graze() {
  sim8Grazed = !sim8Grazed;
  const gb = document.getElementById('grassBladesGroup');
  const btn = document.getElementById('grazeBtn8');
  if(sim8Grazed) {
    gb.style.transform = 'scaleY(0.35)';
    gb.style.transformOrigin = '250px 160px';
    btn.innerText = '🌱 Regrow from Base';
    document.getElementById('sim8Info').innerHTML = '✂️ <strong>Tops Grazed!</strong> Even though the upper blades are eaten, the living basal meristem at the soil level remains safe and unharmed.';
  } else {
    gb.style.transform = 'scaleY(1)';
    btn.innerText = '✂️ Graze / Mow Tops';
    document.getElementById('sim8Info').innerHTML = '🌱 <strong>Rapid Basal Regrowth:</strong> Within days, the basal meristem pushes up fresh green leaves, showcasing the grass family\'s remarkable survival superpower!';
  }
}

function sim8SelectGrain(grain) {
  if(grain === 'paddy') {
    document.getElementById('sim8Info').innerHTML = '🌾 <strong>Paddy (Rice):</strong> Semi-aquatic cultivated grass grown in flooded paddy fields, feeding more than half of humanity as our primary staple grain.';
  } else if(grain === 'wheat') {
    document.getElementById('sim8Info').innerHTML = '🍞 <strong>Wheat Grass:</strong> Winter rabi cereal grass with golden ears containing gluten-rich grains milled into flour for rotis and bread.';
  } else if(grain === 'bajra') {
    document.getElementById('sim8Info').innerHTML = '🫓 <strong>Bajra (Pearl Millet):</strong> Drought-resilient grass thriving in sandy dry soils, producing iron-rich grains for hearty winter flatbreads.';
  } else if(grain === 'ragi') {
    document.getElementById('sim8Info').innerHTML = '🥣 <strong>Ragi (Finger Millet):</strong> Superfood grass rich in dietary calcium and amino acids, excellent for strong bones and traditional porridges.';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part1)} simulators for Part 1.")

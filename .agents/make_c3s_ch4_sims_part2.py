#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 4: Getting to Know Plants
Simulators Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🎋 Giant Grasses: Bamboo & Sugarcane</h3>
    <button onclick="sim9GrowBamboo()" id="growBambooBtn" style="background: #16a34a; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">⚡ 24-Hour Bamboo Growth (+90 cm)</button>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Ground line -->
      <rect x="0" y="170" width="500" height="40" fill="#3f2e21" />
      <line x1="0" y1="170" x2="500" y2="170" stroke="#15803d" stroke-width="3" />

      <!-- Giant Bamboo Culm with Jointed Nodes -->
      <g id="bambooShoot" style="transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1); transform-origin: 180px 170px;">
        <!-- Hollow Culm Cylinder -->
        <rect x="165" y="40" width="30" height="130" fill="#22c55e" stroke="#15803d" stroke-width="2"/>
        <!-- Ring Nodes -->
        <line x1="165" y1="70" x2="195" y2="70" stroke="#14532d" stroke-width="3"/>
        <line x1="165" y1="105" x2="195" y2="105" stroke="#14532d" stroke-width="3"/>
        <line x1="165" y1="140" x2="195" y2="140" stroke="#14532d" stroke-width="3"/>
        <!-- Bamboo Foliage at Nodes -->
        <path d="M 195,70 Q 230,50 240,65" stroke="#4ade80" stroke-width="3" fill="none"/>
        <path d="M 165,105 Q 130,85 120,100" stroke="#4ade80" stroke-width="3" fill="none"/>
        <text x="180" y="30" text-anchor="middle" fill="#86efac" font-size="9" font-weight="bold">Giant Bamboo</text>
      </g>

      <!-- Sugarcane Stalk (Right) -->
      <g id="sugarcanePlant">
        <rect x="330" y="60" width="22" height="110" fill="#ca8a04" stroke="#854d0e" stroke-width="2"/>
        <!-- Nodes -->
        <line x1="330" y1="85" x2="352" y2="85" stroke="#713f12" stroke-width="2"/>
        <line x1="330" y1="115" x2="352" y2="115" stroke="#713f12" stroke-width="2"/>
        <line x1="330" y1="145" x2="352" y2="145" stroke="#713f12" stroke-width="2"/>
        <!-- Arching Sugarcane Leaves -->
        <path d="M 340,60 Q 380,30 400,50" stroke="#84cc16" stroke-width="2.5" fill="none"/>
        <path d="M 340,60 Q 300,30 280,50" stroke="#84cc16" stroke-width="2.5" fill="none"/>
        <text x="341" y="50" text-anchor="middle" fill="#fef08a" font-size="9" font-weight="bold">Sugarcane</text>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim9SqueezeSugarcane()" style="background: #d97706; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🥤 Squeeze Sugarcane Juice</button>
    <button onclick="sim9EcoTimber()" style="background: #475569; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🏠 Bamboo Green Timber</button>
  </div>

  <div id="sim9Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "24-Hour Bamboo Growth" to observe how the world's tallest grass can surge 90 cm in a single day!
  </div>
</div>

<script>
let sim9Grown = false;
function sim9GrowBamboo() {
  sim9Grown = !sim9Grown;
  const bb = document.getElementById('bambooShoot');
  const btn = document.getElementById('growBambooBtn');
  if(sim9Grown) {
    bb.style.transform = 'scaleY(1.4)';
    btn.innerText = '🔄 Reset Bamboo Height';
    document.getElementById('sim9Info').innerHTML = '⚡ <strong>90 cm Daily Velocity!</strong> In warm monsoon climates, tropical bamboo species can elongate up to 90 cm in 24 hours through rapid cell elongation at its nodes!';
  } else {
    bb.style.transform = 'scaleY(1)';
    btn.innerText = '⚡ 24-Hour Bamboo Growth (+90 cm)';
    document.getElementById('sim9Info').innerText = 'Bamboo returned to normal stature. Giant grasses demonstrate nature\'s most efficient structural engineering!';
  }
}

function sim9SqueezeSugarcane() {
  document.getElementById('sim9Info').innerHTML = '🥤 <strong>Sweet Sucrose Sap:</strong> Sugarcane stalks store energy-rich sweet juice in fibrous internal cells, harvested to produce unrefined jaggery (gur) and pure cane sugar!';
}

function sim9EcoTimber() {
  document.getElementById('sim9Info').innerHTML = '🏠 <strong>Green Steel of Nature:</strong> Hollow yet circular-reinforced bamboo culms provide lightweight strength superior to structural steel, building earthquake-safe homes without cutting down slow-growing forest trees.';
}
</script>
""",

    10: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🧗 Climbers & Tendril Coiling</h3>
    <button onclick="sim10TouchSupport()" id="tendrilBtn10" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🖐️ Touch Trellis Support</button>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Wooden Garden Trellis Stake (Vertical Support) -->
      <rect x="300" y="20" width="16" height="170" fill="#78350f" stroke="#451a03" stroke-width="2"/>
      <text x="325" y="40" fill="#cbd5e1" font-size="9" font-weight="bold">Wooden Trellis Stake</text>

      <!-- Slender Climbing Vine Stem (Green Pea / Money Plant) -->
      <path d="M 120,190 Q 160,150 200,120 Q 240,90 270,70" stroke="#22c55e" stroke-width="4" stroke-linecap="round" fill="none"/>
      <!-- Leaves -->
      <ellipse cx="170" cy="140" rx="14" ry="8" fill="#4ade80" transform="rotate(-20 170 140)"/>
      <ellipse cx="230" cy="100" rx="14" ry="8" fill="#4ade80" transform="rotate(-35 230 100)"/>

      <!-- Sensitive Tendril Tip -->
      <path id="coilingTendril" d="M 270,70 Q 285,65 300,70" stroke="#86efac" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <circle cx="270" cy="70" r="3" fill="#facc15" />
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
    <button onclick="sim10SelectClimber('pea')" style="background: #15803d; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌱 Green Pea Tendril</button>
    <button onclick="sim10SelectClimber('money')" style="background: #0369a1; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌿 Money Plant Roots</button>
    <button onclick="sim10SelectClimber('jasmine')" style="background: #475569; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌸 Sweet Jasmine</button>
  </div>

  <div id="sim10Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "Touch Trellis Support" to witness touch-sensitive thigmotropism coiling the tendril tightly around the wooden stake!
  </div>
</div>

<script>
let sim10Coiled = false;
function sim10TouchSupport() {
  sim10Coiled = !sim10Coiled;
  const ct = document.getElementById('coilingTendril');
  const btn = document.getElementById('tendrilBtn10');
  if(sim10Coiled) {
    // Spiral wrap around stake at x=300
    ct.setAttribute('d', 'M 270,70 L 300,70 Q 316,65 316,75 Q 316,85 300,85 Q 284,85 284,95 Q 284,105 308,105');
    btn.innerText = '🔄 Release Tendril';
    document.getElementById('sim10Info').innerHTML = '🌀 <strong>Thigmotropism Spiral:</strong> Upon physical contact, cells on the outer side grow faster, coiling the tendril into a spring-like anchor that pulls the vine up to sunlight!';
  } else {
    ct.setAttribute('d', 'M 270,70 Q 285,65 300,70');
    btn.innerText = '🖐️ Touch Trellis Support';
    document.getElementById('sim10Info').innerText = 'Tendril returned to relaxed scanning state. Click to trigger touch response!';
  }
}

function sim10SelectClimber(type) {
  if(type === 'pea') {
    document.getElementById('sim10Info').innerHTML = '🌱 <strong>Green Pea:</strong> Uses thread-like leaf tendrils that coil like telephone cords around fences, lifting delicate sweet pea pods toward sunlight.';
  } else if(type === 'money') {
    document.getElementById('sim10Info').innerHTML = '🌿 <strong>Money Plant:</strong> Uses specialized aerial adventitious clasping roots that sprout from stem nodes to glue itself to damp walls and tree trunks.';
  } else if(type === 'jasmine') {
    document.getElementById('sim10Info').innerHTML = '🌸 <strong>Jasmine Climber:</strong> Flexible woody twiners that wrap clockwise around garden arches, filling evening air with intoxicating floral perfume.';
  }
}
</script>
""",

    11: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🍉 Creepers & Heavy Fruit Biomechanics</h3>
    <button onclick="sim11TestLoad()" id="loadTestBtn11" style="background: #dc2626; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">⚖️ Test Suspended Load</button>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Solid Ground Earth (Safe Cradle) -->
      <rect x="0" y="160" width="500" height="50" fill="#3f2e21" />
      <line x1="0" y1="160" x2="500" y2="160" stroke="#15803d" stroke-width="3" />

      <!-- High Tree Branch (Unsafe suspended scenario on left) -->
      <rect x="40" y="30" width="160" height="12" fill="#78350f" />
      <path id="suspendedVine" d="M 120,42 L 120,100" stroke="#22c55e" stroke-width="2.5" fill="none"/>
      <!-- Heavy Suspended Watermelon (10 kg) -->
      <g id="suspendedMelon" transform="translate(120, 115)">
        <ellipse cx="0" cy="0" rx="20" ry="16" fill="#15803d" stroke="#166534" stroke-width="2"/>
        <text x="0" y="4" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">10 kg</text>
      </g>
      <text id="snapWarning" x="120" y="145" text-anchor="middle" fill="#f87171" font-size="9" font-weight="bold" opacity="0">⚠️ STEM SNAPS!</text>

      <!-- Ground Trailing Creeper (Safe Natural Design on right) -->
      <path d="M 240,160 Q 300,155 360,160 Q 420,158 480,160" stroke="#22c55e" stroke-width="3.5" fill="none"/>
      <!-- Broad green mulch leaves -->
      <ellipse cx="300" cy="155" rx="14" ry="8" fill="#4ade80" />
      <ellipse cx="420" cy="155" rx="14" ry="8" fill="#4ade80" />
      
      <!-- Massive Pumpkin resting securely on solid ground -->
      <g transform="translate(360, 150)">
        <ellipse cx="0" cy="0" rx="26" ry="18" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>
        <line x1="-15" y1="0" x2="15" y2="0" stroke="#9a3412" stroke-dasharray="2,2"/>
        <text x="0" y="3" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">Pumpkin (Solid Ground)</text>
      </g>
    </svg>
  </div>

  <div id="sim11Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "Test Suspended Load" to see why heavy fruits cannot hang from climbing vines, requiring the solid earth to cradle them!
  </div>
</div>

<script>
let sim11Snapped = false;
function sim11TestLoad() {
  sim11Snapped = !sim11Snapped;
  const vine = document.getElementById('suspendedVine');
  const melon = document.getElementById('suspendedMelon');
  const warn = document.getElementById('snapWarning');
  const btn = document.getElementById('loadTestBtn11');
  if(sim11Snapped) {
    vine.setAttribute('d', 'M 120,42 L 120,65 M 120,75 L 120,140');
    melon.setAttribute('transform', 'translate(120, 150)');
    warn.setAttribute('opacity', '1');
    btn.innerText = '🔄 Reset Load Test';
    document.getElementById('sim11Info').innerHTML = '💥 <strong>Biomechanics in Action:</strong> The thin vine cannot bear 10 kg against gravity! Creepers evolved to trail on the ground so the earth comfortably supports massive pumpkins and watermelons.';
  } else {
    vine.setAttribute('d', 'M 120,42 L 120,100');
    melon.setAttribute('transform', 'translate(120, 115)');
    warn.setAttribute('opacity', '0');
    btn.innerText = '⚖️ Test Suspended Load';
    document.getElementById('sim11Info').innerText = 'Vine reconnected. Notice how the ground-resting pumpkin on the right stays completely safe and stable!';
  }
}
</script>
""",

    12: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🍅 Tomato Plant Organ Anatomy</h3>
    <span id="organBadge12" style="background: #0284c7; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Click Any Organ Below</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Ground line -->
      <rect x="0" y="150" width="500" height="60" fill="#3f2e21" />
      <line x1="0" y1="150" x2="500" y2="150" stroke="#15803d" stroke-width="3" />

      <!-- 1. Roots (Subterranean) -->
      <g onclick="sim12Select('roots')" style="cursor: pointer;">
        <path d="M 250,150 L 250,200 M 250,165 L 210,190 M 250,175 L 290,195 M 250,185 L 235,205" stroke="#d97706" stroke-width="3" fill="none"/>
        <rect x="180" y="165" width="40" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="185" y="177" fill="#facc15" font-size="9" font-weight="bold">Roots</text>
      </g>

      <!-- 2. Central Stem -->
      <g onclick="sim12Select('stem')" style="cursor: pointer;">
        <line x1="250" y1="150" x2="250" y2="40" stroke="#22c55e" stroke-width="5" stroke-linecap="round"/>
        <rect x="258" y="100" width="36" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="263" y="112" fill="#4ade80" font-size="9" font-weight="bold">Stem</text>
      </g>

      <!-- 3. Leaves (Photosynthesis) -->
      <g onclick="sim12Select('leaves')" style="cursor: pointer;">
        <path d="M 250,110 Q 210,90 190,105 Q 220,125 250,110 Z" fill="#15803d" />
        <path d="M 250,80 Q 290,60 310,75 Q 280,95 250,80 Z" fill="#15803d" />
        <rect x="155" y="85" width="42" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="160" y="97" fill="#86efac" font-size="9" font-weight="bold">Leaves</text>
      </g>

      <!-- 4. Flowers (Yellow petals) -->
      <g onclick="sim12Select('flowers')" style="cursor: pointer;">
        <circle cx="270" cy="50" r="8" fill="#facc15" />
        <circle cx="270" cy="50" r="3" fill="#ca8a04" />
        <rect x="285" y="42" width="48" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="290" y="54" fill="#fef08a" font-size="9" font-weight="bold">Flowers</text>
      </g>

      <!-- 5. Fruit (Plump Red Tomato) -->
      <g onclick="sim12Select('fruit')" style="cursor: pointer;">
        <circle cx="215" cy="70" r="14" fill="#dc2626" stroke="#991b1b" stroke-width="1.5"/>
        <circle cx="215" cy="62" r="3" fill="#15803d" />
        <rect x="145" y="55" width="38" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="150" y="67" fill="#f87171" font-size="9" font-weight="bold">Fruit</text>
      </g>

      <!-- 6. Seeds (Inside tomato cross-section) -->
      <g onclick="sim12Select('seeds')" style="cursor: pointer;">
        <rect x="360" y="85" width="42" height="16" rx="4" fill="#0f172a" opacity="0.8"/>
        <text x="365" y="97" fill="#fbbf24" font-size="9" font-weight="bold">Seeds</text>
        <circle cx="380" cy="115" r="3" fill="#fef08a" /><circle cx="386" cy="120" r="3" fill="#fef08a" />
      </g>
    </svg>
  </div>

  <div id="sim12Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click on any labeled organ in the tomato diagram to inspect its physiological function!
  </div>
</div>

<script>
const sim12Organs = {
  roots: {name: "Root System", desc: "🪵 <strong>Roots:</strong> Anchor the plant firmly against wind while microscopic root hairs absorb essential water and dissolved minerals from deep soil."},
  stem: {name: "Stem (Vascular Backbone)", desc: "🌿 <strong>Stem:</strong> Holds leaves toward sunlight and houses internal xylem tubes (carrying water up) and phloem tubes (distributing food down)."},
  leaves: {name: "Photosynthetic Leaves", desc: "🍃 <strong>Leaves:</strong> The plant's food factories! Packed with green chlorophyll to capture solar energy, converting water and CO2 into nourishing sugars."},
  flowers: {name: "Reproductive Flowers", desc: "🌼 <strong>Flowers:</strong> Reproductive organs displaying bright yellow petals that invite pollinating bees, leading to seed and fruit formation."},
  fruit: {name: "Protective Tomato Fruit", desc: "🍅 <strong>Fruit:</strong> Develops from the fertilized flower ovary. Plump and juicy to protect delicate seeds inside while attracting seed dispersers."},
  seeds: {name: "Embryonic Seeds", desc: "🌰 <strong>Seeds:</strong> Nature's time capsules! Each seed contains a dormant baby plant embryo and stored food, awaiting moisture to sprout."}
};

function sim12Select(organ) {
  const item = sim12Organs[organ];
  document.getElementById('organBadge12').innerText = item.name;
  document.getElementById('sim12Info').innerHTML = item.desc;
}
</script>
""",

    13: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">📋 Adopt a Plant Friend & Log Girth</h3>
    <span id="girthTag13" style="background: #15803d; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Measured Girth: 110 cm</span>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Tree Trunk of Adopted Friend -->
      <rect x="220" y="20" width="60" height="160" fill="#78350f" stroke="#451a03" stroke-width="2"/>
      <!-- Bark furrow lines -->
      <line x1="235" y1="30" x2="235" y2="170" stroke="#451a03" stroke-width="1.5" />
      <line x1="250" y1="20" x2="250" y2="180" stroke="#451a03" stroke-width="1.5" />
      <line x1="265" y1="35" x2="265" y2="165" stroke="#451a03" stroke-width="1.5" />

      <!-- Measuring Tape / String wrapped around trunk (Chest Height) -->
      <g id="measuringString" style="transition: all 0.4s;">
        <ellipse cx="250" cy="100" rx="36" ry="10" fill="none" stroke="#facc15" stroke-width="4" stroke-dasharray="6,4"/>
        <!-- Tag with string measurement -->
        <rect x="290" y="88" width="85" height="22" rx="4" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
        <text id="stringText" x="295" y="103" fill="#fef08a" font-size="9" font-weight="bold">String = 110 cm</text>
      </g>

      <!-- Adopted Tree Nameplate -->
      <g transform="translate(140, 130)">
        <rect x="0" y="0" width="70" height="24" rx="4" fill="#0284c7" />
        <text x="35" y="15" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">Friend: Gulmohar</text>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
    <button onclick="sim13LogSeason('spring')" style="background: #16a34a; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌸 Spring Blooms</button>
    <button onclick="sim13LogSeason('autumn')" style="background: #d97706; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🍂 Autumn Shedding</button>
    <button onclick="sim13LogSeason('birds')" style="background: #0369a1; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🐦 Wildlife Visitors</button>
  </div>

  <div id="sim13Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Wrapping a flexible string around the trunk at chest height gives accurate trunk girth (circumference) to track annual growth!
  </div>
</div>

<script>
function sim13LogSeason(event) {
  if(event === 'spring') {
    document.getElementById('sim13Info').innerHTML = '🌸 <strong>Phenology Diary (Spring):</strong> Fresh scarlet flower clusters burst open! Bees, sunbirds, and butterflies arrive in dozens to sip sweet nectar.';
  } else if(event === 'autumn') {
    document.getElementById('sim13Info').innerHTML = '🍂 <strong>Phenology Diary (Autumn):</strong> Older leaves turn golden yellow and gently fall to the ground, creating natural mulch that replenishes soil organic nutrients.';
  } else if(event === 'birds') {
    document.getElementById('sim13Info').innerHTML = '🐦 <strong>Biodiversity Observation:</strong> Spotted three squirrels chasing along upper branches and a family of tailorbirds nesting beneath broad leaves.';
  }
}
</script>
""",

    14: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🖍️ Tree Bark Impressions & Lenticels</h3>
    <button onclick="sim14RubCrayon()" id="rubCrayonBtn" style="background: #ea580c; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🖍️ Rub Wax Crayon</button>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <!-- Trunk with Paper sheet -->
    <div style="background: #1e293b; border-radius: 8px; padding: 8px; border: 1px solid #334155; text-align: center;">
      <div style="font-size: 0.8rem; font-weight: bold; color: #94a3b8; margin-bottom: 4px;">Paper Pressed Against Trunk</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <!-- Woody Tree Bark -->
        <rect x="20" y="10" width="120" height="100" fill="#78350f" />
        <!-- Bark Fissures -->
        <line x1="45" y1="10" x2="45" y2="110" stroke="#451a03" stroke-width="3"/>
        <line x1="80" y1="10" x2="80" y2="110" stroke="#451a03" stroke-width="4"/>
        <line x1="115" y1="10" x2="115" y2="110" stroke="#451a03" stroke-width="3"/>
        <!-- White Paper Sheet Overlay -->
        <rect x="35" y="20" width="90" height="80" fill="#f8fafc" opacity="0.85" stroke="#94a3b8" />
        <!-- Crayon rubbing impression (initially hidden) -->
        <g id="crayonImpression" opacity="0" style="transition: opacity 0.5s;">
          <line x1="45" y1="20" x2="45" y2="100" stroke="#c2410c" stroke-width="3" stroke-dasharray="4,2"/>
          <line x1="80" y1="20" x2="80" y2="100" stroke="#c2410c" stroke-width="4" stroke-dasharray="6,3"/>
          <line x1="115" y1="20" x2="115" y2="100" stroke="#c2410c" stroke-width="3" stroke-dasharray="4,2"/>
        </g>
      </svg>
    </div>

    <!-- Microscopic Lenticel Breathing Pores -->
    <div style="background: #1e293b; border-radius: 8px; padding: 8px; border: 1px solid #334155; text-align: center;">
      <div style="font-size: 0.8rem; font-weight: bold; color: #38bdf8; margin-bottom: 4px;">Lenticel (Bark Breathing Pore)</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <ellipse cx="80" cy="60" rx="60" ry="40" fill="#92400e" stroke="#451a03" stroke-width="2"/>
        <!-- Lenticel raised slit pore -->
        <ellipse cx="80" cy="60" rx="30" ry="10" fill="#ca8a04" />
        <ellipse cx="80" cy="60" rx="20" ry="4" fill="#0f172a" />
        <!-- Oxygen gas exchange arrows -->
        <path d="M 80,35 L 80,50 M 75,45 L 80,50 L 85,45" stroke="#38bdf8" stroke-width="2" fill="none"/>
        <text x="80" y="25" text-anchor="middle" fill="#7dd3fc" font-size="8" font-weight="bold">O2 Inflow</text>
      </svg>
    </div>
  </div>

  <div id="sim14Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    Click "Rub Wax Crayon" to capture the tree's unique textured bark fingerprint on paper!
  </div>
</div>

<script>
let sim14Rubbed = false;
function sim14RubCrayon() {
  sim14Rubbed = !sim14Rubbed;
  const imp = document.getElementById('crayonImpression');
  const btn = document.getElementById('rubCrayonBtn');
  if(sim14Rubbed) {
    imp.setAttribute('opacity', '1');
    btn.innerText = '🔄 Fresh Paper Sheet';
    document.getElementById('sim14Info').innerHTML = '🖍️ <strong>Bark Impression Created!</strong> Raised ridges and deep fissures transfer wax, recording the tree\'s distinctive bark fingerprint for your nature journal!';
  } else {
    imp.setAttribute('opacity', '0');
    btn.innerText = '🖍️ Rub Wax Crayon';
    document.getElementById('sim14Info').innerText = 'New paper placed on trunk. Click to create a rubbing!';
  }
}
</script>
""",

    15: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">👃 Blindfolded Leaf Fragrance Game</h3>
    <span id="scentBadge15" style="background: #0284c7; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Mystery Aroma #1</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 10px;">
    <button onclick="sim15Scratch(0)" id="scBtn0" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🌱 Leaf A
    </button>
    <button onclick="sim15Scratch(1)" id="scBtn1" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🌿 Leaf B
    </button>
    <button onclick="sim15Scratch(2)" id="scBtn2" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🍃 Leaf C
    </button>
    <button onclick="sim15Scratch(3)" id="scBtn3" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🍋 Leaf D
    </button>
  </div>

  <div id="sim15Box" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #38bdf8; min-height: 70px;">
    <div id="sim15Title" style="font-weight: bold; color: #38bdf8; font-size: 0.95rem;">Select a mystery leaf above</div>
    <div id="sim15Desc" style="font-size: 0.85rem; color: #cbd5e1; margin-top: 4px; line-height: 1.4;">
      Close your eyes and test your olfactory senses! Crushing leaves ruptures microscopic essential oil glands, releasing distinct airborne scent molecules.
    </div>
  </div>
</div>

<script>
const sim15Scents = [
  {title: "🌱 Mystery Leaf A: Mint (Pudina)", desc: "❄️ <strong>Cool Menthol Aroma:</strong> Instantly releases refreshing, icy-cool menthol vapor that clears nasal passages and soothes digestion.", badge: "Aroma: Mint (Menthol)"},
  {title: "🌿 Mystery Leaf B: Holy Basil (Tulsi)", desc: "🫚 <strong>Warm Spicy Eugenol:</strong> Emits a rich, clove-like medicinal fragrance loaded with antimicrobial and immune-supporting essential oils.", badge: "Aroma: Tulsi (Eugenol)"},
  {title: "🍃 Mystery Leaf C: Curry Leaf (Kadi Patta)", desc: "🥘 <strong>Savory Herbal Fragrance:</strong> Rich in pinene and caryophyllene, releasing the unmistakable savory aroma of South Indian tempering.", badge: "Aroma: Curry Leaf (Herbal)"},
  {title: "🍋 Mystery Leaf D: Lemon Leaf (Citrus)", desc: "✨ <strong>Zesty Fresh Limonene:</strong> Bright citrus scent that deters insect herbivores while energizing our sensory nervous system.", badge: "Aroma: Lemon (Limonene)"}
];

function sim15Scratch(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`scBtn${i}`).style.borderColor = (i === idx) ? '#38bdf8' : '#475569';
  }
  const item = sim15Scents[idx];
  document.getElementById('sim15Title').innerText = item.title;
  document.getElementById('sim15Desc').innerHTML = item.desc;
  document.getElementById('scentBadge15').innerText = item.badge;
}
</script>
""",

    16: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌺 Rafflesia Gigantism & Leaf Rangoli</h3>
    <span id="wonderBadge16" style="background: #dc2626; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Rafflesia (100 cm Diameter!)</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <!-- Rafflesia Giant Blossom -->
    <div style="background: #1e293b; border-radius: 8px; padding: 8px; border: 1px solid #334155; text-align: center;">
      <div style="font-size: 0.8rem; font-weight: bold; color: #f87171; margin-bottom: 4px;">World's Largest Flower (1 Meter)</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <!-- 5 Giant Red Petals with white warts -->
        <g fill="#dc2626" stroke="#991b1b" stroke-width="2">
          <circle cx="80" cy="30" r="22" /><circle cx="80" cy="30" r="4" fill="#fecaca" />
          <circle cx="45" cy="55" r="22" /><circle cx="45" cy="55" r="4" fill="#fecaca" />
          <circle cx="115" cy="55" r="22" /><circle cx="115" cy="55" r="4" fill="#fecaca" />
          <circle cx="55" cy="90" r="22" /><circle cx="55" cy="90" r="4" fill="#fecaca" />
          <circle cx="105" cy="90" r="22" /><circle cx="105" cy="90" r="4" fill="#fecaca" />
        </g>
        <!-- Center bowl cavity -->
        <circle cx="80" cy="65" r="20" fill="#7f1d1d" stroke="#450a0a" stroke-width="2"/>
        <circle cx="80" cy="65" r="8" fill="#facc15" />
      </svg>
    </div>

    <!-- Eco-Friendly Fallen Leaf Rangoli -->
    <div style="background: #1e293b; border-radius: 8px; padding: 8px; border: 1px solid #334155; text-align: center;">
      <div style="font-size: 0.8rem; font-weight: bold; color: #4ade80; margin-bottom: 4px;">Fallen Leaf Rangoli Art</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 95px;">
        <!-- Center circle -->
        <circle cx="80" cy="60" r="10" fill="#facc15" />
        <!-- Symmetrical leaf petals (shed foliage) -->
        <g fill="#15803d">
          <ellipse cx="80" cy="35" rx="8" ry="15" fill="#eab308" />
          <ellipse cx="80" cy="85" rx="8" ry="15" fill="#eab308" />
          <ellipse cx="55" cy="60" rx="15" ry="8" fill="#ca8a04" />
          <ellipse cx="105" cy="60" rx="15" ry="8" fill="#ca8a04" />
          <!-- Diagonal leaves -->
          <ellipse cx="62" cy="42" rx="7" ry="12" fill="#15803d" transform="rotate(-45 62 42)"/>
          <ellipse cx="98" cy="42" rx="7" ry="12" fill="#15803d" transform="rotate(45 98 42)"/>
          <ellipse cx="62" cy="78" rx="7" ry="12" fill="#15803d" transform="rotate(45 62 78)"/>
          <ellipse cx="98" cy="78" rx="7" ry="12" fill="#15803d" transform="rotate(-45 98 78)"/>
        </g>
      </svg>
    </div>
  </div>

  <div id="sim16Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 38px; line-height: 1.4;">
    🌺 <strong>Rafflesia:</strong> Reaching 1 meter across and 10 kg in weight, this umbrella-sized giant flower has no roots or leaves! Alongside it, fallen-leaf rangoli honors nature sustainably without plucking living blossoms.
  </div>
</div>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part2)} simulators for Part 2.")

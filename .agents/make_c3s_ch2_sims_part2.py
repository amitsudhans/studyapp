#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Science (Our Wondrous World)
Chapter 2: Going to the Mela
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🎎 Indigenous Folk Toy Workshop</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Toy('phirki')">Paper Phirki (Pinwheel)</button>
      <button class="sim-btn" onclick="sim9Toy('top')">Wooden Spinning Top</button>
      <button class="sim-btn" onclick="sim9Toy('puppet')">Terracotta Doll</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim9Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim9Icon" style="font-size:38px;">🏵️ 💨</div>
      <div id="sim9Name" style="font-size:14px; font-weight:bold; color:#fbbf24; margin-top:4px;">Paper Phirki (Wind Pinwheel)</div>
    </div>
    <div id="sim9Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      💨 <b>Wind Energy:</b> Running forward pushes air against curved paper blades, converting kinetic air motion into rapid spinning!
    </div>
  </div>
</div>
<script>
function sim9Toy(t) {
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(t)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim9Icon');
  const name = document.getElementById('sim9Name');
  const fb = document.getElementById('sim9Feedback');

  if (t === 'phirki') {
    icon.innerHTML = '🏵️ 💨';
    name.innerHTML = 'Paper Phirki (Pinwheel)';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '💨 <b>Aerodynamic Rotation:</b> Moving air strikes angled paper vanes, generating rotational torque without any batteries!';
  } else if (t === 'top') {
    icon.innerHTML = '🌀 🪵';
    name.innerHTML = 'Carved Wooden Top (Lattoo)';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🌀 <b>Gyroscopic Stability:</b> Rapid spinning produces angular momentum, keeping the wooden top balanced upright on its narrow tip.';
  } else if (t === 'puppet') {
    icon.innerHTML = '🎎 🏺';
    name.innerHTML = 'Painted Terracotta Clay Doll';
    fb.style.color = '#34d399';
    fb.innerHTML = '🏺 <b>Eco-Friendly Craft:</b> Baked from natural riverbed clay and painted with non-toxic botanical dyes by village potters.';
  }
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🎡 Fairground Amusement Physics Console</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Ride('wheel')">Giant Ferris Wheel</button>
      <button class="sim-btn" onclick="sim10Ride('round')">Merry-Go-Round</button>
      <button class="sim-btn" onclick="sim10Ride('safety')">Safety Restraint Check</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim10Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central Wheel / Ride Group -->
      <g id="sim10Graphic" transform="translate(120, 70)">
        <!-- Giant Wheel Spokes -->
        <circle cx="0" cy="0" r="45" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <line x1="-45" y1="0" x2="45" y2="0" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="0" y1="-45" x2="0" y2="45" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="-32" y1="-32" x2="32" y2="32" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="-32" y1="32" x2="32" y2="-32" stroke="#38bdf8" stroke-width="1.5"/>
        <!-- Center Hub -->
        <circle cx="0" cy="0" r="8" fill="#f59e0b"/>
        <!-- Cabins -->
        <circle cx="0" cy="-45" r="7" fill="#ef4444"/>
        <circle cx="45" cy="0" r="7" fill="#22c55e"/>
        <circle cx="0" cy="45" r="7" fill="#ef4444"/>
        <circle cx="-45" cy="0" r="7" fill="#22c55e"/>
      </g>
    </svg>
    <div id="sim10Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎡 <b>Giant Wheel:</b> Vertical circular rotation provides breathtaking panoramic views and sensations of apparent lightness at the top!
    </div>
  </div>
</div>
<script>
function sim10Ride(r) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(r)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const g = document.getElementById('sim10Graphic');
  const fb = document.getElementById('sim10Feedback');

  if (r === 'wheel') {
    g.innerHTML = `
      <circle cx="0" cy="0" r="45" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <line x1="-45" y1="0" x2="45" y2="0" stroke="#38bdf8" stroke-width="1.5"/>
      <line x1="0" y1="-45" x2="0" y2="45" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="8" fill="#f59e0b"/>
      <circle cx="0" cy="-45" r="7" fill="#ef4444"/>
      <circle cx="45" cy="0" r="7" fill="#22c55e"/>
      <circle cx="0" cy="45" r="7" fill="#ef4444"/>
      <circle cx="-45" cy="0" r="7" fill="#22c55e"/>
    `;
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🎡 <b>Vertical Circular Motion:</b> At the apex, riders experience a gentle floating sensation as downward acceleration offsets seat push.';
  } else if (r === 'round') {
    g.innerHTML = `
      <ellipse cx="0" cy="15" rx="50" ry="20" fill="none" stroke="#f59e0b" stroke-width="3"/>
      <line x1="0" y1="-30" x2="0" y2="30" stroke="#94a3b8" stroke-width="4"/>
      <polygon points="-50,-30 0,-45 50,-30" fill="#dc2626"/>
      <circle cx="-25" cy="15" r="8" fill="#3b82f6"/>
      <circle cx="25" cy="15" r="8" fill="#10b981"/>
    `;
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🎠 <b>Centripetal Acceleration:</b> The spinning carousel constantly pulls riders inward, keeping horses moving safely in a smooth circle.';
  } else if (r === 'safety') {
    g.innerHTML = `
      <rect x="-30" y="-20" width="60" height="40" rx="6" fill="#334155" stroke="#22c55e" stroke-width="2"/>
      <line x1="-30" y1="0" x2="30" y2="0" stroke="#22c55e" stroke-width="4"/>
      <text x="0" y="5" fill="#f8fafc" font-size="8" text-anchor="middle" font-weight="bold">LOCKED BAR</text>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '🔒 <b>Safety Lap Bar:</b> Firmly locked waist restraint prevents accidental slip-outs during dynamic fairground ride motion.';
  }
}
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🎭 Traditional Puppet Theater (Kathputli)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Move('bow')">Bow Respectfully</button>
      <button class="sim-btn" onclick="sim11Move('dance')">Dance & Spin</button>
      <button class="sim-btn" onclick="sim11Move('music')">Play Dholak Beat</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim11Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Stage Curtains -->
      <polygon points="0,0 50,0 35,140 0,140" fill="#881337"/>
      <polygon points="240,0 190,0 205,140 240,140" fill="#881337"/>
      <rect x="0" y="0" width="240" height="15" fill="#4c0519"/>

      <!-- Puppet Marionette Group -->
      <g id="sim11Marionette" transform="translate(120, 50)">
        <!-- Strings -->
        <line x1="-15" y1="-40" x2="-8" y2="10" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2 2"/>
        <line x1="15" y1="-40" x2="8" y2="10" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2 2"/>
        <line x1="0" y1="-40" x2="0" y2="-12" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2 2"/>

        <!-- Puppet Head & Turban -->
        <circle cx="0" cy="-6" r="7" fill="#f59e0b"/>
        <ellipse cx="0" cy="-11" rx="8" ry="4" fill="#dc2626"/>

        <!-- Puppet Dress & Skirt -->
        <polygon points="-8,2 8,2 14,35 -14,35" fill="#e11d48"/>
        <!-- Hands -->
        <line x1="-8" y1="10" x2="-14" y2="20" stroke="#f59e0b" stroke-width="2"/>
        <line x1="8" y1="10" x2="14" y2="20" stroke="#f59e0b" stroke-width="2"/>
      </g>
    </svg>
    <div id="sim11Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#f472b6; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎎 <b>Folk Marionette:</b> Master puppeteers pull fine cotton strings to make carved wooden figures dance and tell moral fables!
    </div>
  </div>
</div>
<script>
function sim11Move(m) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(m)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const p = document.getElementById('sim11Marionette');
  const fb = document.getElementById('sim11Feedback');

  if (m === 'bow') {
    p.setAttribute('transform', 'translate(120, 60) rotate(20)');
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🙏 <b>Respectful Bow:</b> Releasing string tension tilts the wooden head and torso forward in traditional festive greeting.';
  } else if (m === 'dance') {
    p.setAttribute('transform', 'translate(120, 45) rotate(-15)');
    fb.style.color = '#f472b6';
    fb.innerHTML = '💃 <b>Rhythmic Folk Dance:</b> Alternating string twitches create swirling leaps, bringing the sequined character to vibrant life!';
  } else if (m === 'music') {
    p.setAttribute('transform', 'translate(120, 50)');
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🥁 <b>Dholak Beats & Whistle:</b> Two-headed folk drums and shrill reed whistles punctuate the drama, accentuating moral storytelling.';
  }
}
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🧼 Food Hygiene & Handwashing Station</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Wash()">1. Wash Hands with Soap</button>
      <button class="sim-btn" onclick="sim12Cover()">2. Inspect Food Glass Covers</button>
      <button class="sim-btn" onclick="sim12Eat()">3. Safe Wholesome Dining</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim12Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim12Icon" style="font-size:38px;">🧼 🚰 💧</div>
      <div id="sim12Step" style="font-size:14px; font-weight:bold; color:#38bdf8; margin-top:4px;">20-Second Soap Wash</div>
    </div>
    <div id="sim12Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🧼 <b>Germ Destruction:</b> Soap dissolves fatty bacterial membranes picked up from public railings, preventing digestive infections!
    </div>
  </div>
</div>
<script>
function sim12Wash() {
  const icon = document.getElementById('sim12Icon');
  const step = document.getElementById('sim12Step');
  const fb = document.getElementById('sim12Feedback');
  icon.innerHTML = '🧼 🚰 💧';
  step.innerHTML = 'Lathering Soap for 20 Seconds';
  fb.style.color = '#34d399';
  fb.innerHTML = '🧼 <b>Hand Hygiene:</b> Washing hands with soap removes invisible pathogens before eating delicious festival treats.';
}

function sim12Cover() {
  const icon = document.getElementById('sim12Icon');
  const step = document.getElementById('sim12Step');
  const fb = document.getElementById('sim12Feedback');
  icon.innerHTML = '🛡️ 🍲 🪰🚫';
  step.innerHTML = 'Protective Sneeze Guards';
  fb.style.color = '#38bdf8';
  fb.innerHTML = '🛡️ <b>Clean Preparation:</b> Glass food shields prevent airborne dust and flies from contaminating street delicacies like chhole and chaat.';
}

function sim12Eat() {
  const icon = document.getElementById('sim12Icon');
  const step = document.getElementById('sim12Step');
  const fb = document.getElementById('sim12Feedback');
  icon.innerHTML = '😋 🧆 🍧';
  step.innerHTML = 'Wholesome Festival Feasting';
  fb.style.color = '#fbbf24';
  fb.innerHTML = '🍧 <b>Safe Dining:</b> Enjoying crispy gol gappas, golden jalebis, and chilled kulfi without risk of stomach illness!';
}
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">♻️ Fairground Dual-Bin Waste Sorting</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim13Sort('leaf')">Leaf Plate (Organic)</button>
      <button class="sim-btn" onclick="sim13Sort('cup')">Clean Paper Cup (Dry)</button>
      <button class="sim-btn" onclick="sim13Sort('peel')">Fruit Peels (Organic)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Two Bins Side by Side -->
    <div style="display:flex; gap:20px; align-items:center; justify-content:center;">
      <!-- Green Bin -->
      <div style="width:90px; height:100px; background:#15803d; border-radius:10px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#f8fafc; font-weight:bold; font-size:11px; border:2px solid #22c55e;">
        <span style="font-size:24px;">🟢 🍂</span>
        GREEN BIN
        <span style="font-size:9px; font-weight:normal;">Wet Organic</span>
      </div>
      <!-- Blue Bin -->
      <div style="width:90px; height:100px; background:#1d4ed8; border-radius:10px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#f8fafc; font-weight:bold; font-size:11px; border:2px solid #60a5fa;">
        <span style="font-size:24px;">🔵 📄</span>
        BLUE BIN
        <span style="font-size:9px; font-weight:normal;">Dry Recyclable</span>
      </div>
    </div>
    <div id="sim13Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ♻️ Click an item above to practice source waste segregation!
    </div>
  </div>
</div>
<script>
function sim13Sort(item) {
  const fb = document.getElementById('sim13Feedback');
  if (item === 'leaf') {
    fb.style.color = '#a3e635';
    fb.innerHTML = '🟢 <b>Green Bin Match:</b> Banana leaf plates and food scraps are biodegradable organic waste that decompose into garden compost!';
  } else if (item === 'cup') {
    fb.style.color = '#60a5fa';
    fb.innerHTML = '🔵 <b>Blue Bin Match:</b> Clean paper cups and cardboard packaging belong in the dry bin to be recycled into new paper products.';
  } else if (item === 'peel') {
    fb.style.color = '#a3e635';
    fb.innerHTML = '🟢 <b>Green Bin Match:</b> Orange and banana peels are rich organic wet waste, providing valuable nutrients for municipal compost.';
  }
}
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🐕 Security Service Sniffer Dog Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Action('sniff')">Olfactory Scent Tracking</button>
      <button class="sim-btn" onclick="sim14Action('harness')">On-Duty Harness Protocol</button>
      <button class="sim-btn" onclick="sim14Action('distract')">No-Distraction Rule</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim14Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim14Icon" style="font-size:38px;">🐕‍🦺 👮 🔍</div>
      <div id="sim14Text" style="font-size:13px; font-weight:bold; color:#38bdf8; margin-top:4px;">Canine Scent Tracking</div>
    </div>
    <div id="sim14Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🔍 <b>300 Million Scent Receptors:</b> Police dogs detect microscopic scent particles in air, locating lost persons and security threats.
    </div>
  </div>
</div>
<script>
function sim14Action(act) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(act)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim14Icon');
  const text = document.getElementById('sim14Text');
  const fb = document.getElementById('sim14Feedback');

  if (act === 'sniff') {
    icon.innerHTML = '🐕‍🦺 👮 🔍';
    text.innerHTML = 'Olfactory Scent Detection';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🔍 <b>Canine Superpowers:</b> A dog\'s sense of smell is up to 100,000 times more acute than human smell, tracking scent trails through crowds.';
  } else if (act === 'harness') {
    icon.innerHTML = '🐕‍🦺 🦺 🎖️';
    text.innerHTML = 'Official Service Harness';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🦺 <b>Working Dog Status:</b> The official harness indicates the dog is actively working alongside law enforcement to protect the community.';
  } else if (act === 'distract') {
    icon.innerHTML = '✋ 🐕‍🦺 🚫';
    text.innerHTML = 'Observe Respectfully';
    fb.style.color = '#f87171';
    fb.innerHTML = '🚫 <b>Do Not Pet:</b> Never pet, whistle at, or feed a working service dog on duty so its sensory concentration is never broken.';
  }
}
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🗺️ Neighborhood Landmark & Route Map</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Route('home')">1. Home & Neighborhood</button>
      <button class="sim-btn" onclick="sim15Route('bus')">2. Bus Stop & Library</button>
      <button class="sim-btn" onclick="sim15Route('parade')">3. Parade Ground (Mela)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim15Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Compass Rose Top Right -->
      <g transform="translate(215, 25)">
        <circle cx="0" cy="0" r="14" fill="rgba(0,0,0,0.5)" stroke="#94a3b8" stroke-width="1"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#f43f5e" stroke-width="2"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#94a3b8" stroke-width="2"/>
        <text x="0" y="-14" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">N</text>
        <text x="0" y="20" fill="#94a3b8" font-size="7" text-anchor="middle">S</text>
        <text x="18" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">E</text>
        <text x="-18" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">W</text>
      </g>

      <!-- Road Path -->
      <path d="M 35 110 L 80 110 L 80 60 L 170 60 L 170 30" fill="none" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>

      <!-- Home (South-West) -->
      <rect x="15" y="95" width="35" height="25" rx="3" fill="#3b82f6"/>
      <text x="32" y="111" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">🏠 Home</text>

      <!-- Bus Stop & Library (Center) -->
      <rect x="65" y="45" width="40" height="22" rx="3" fill="#10b981"/>
      <text x="85" y="59" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">📚 Library</text>

      <!-- Parade Ground (North-East) -->
      <rect x="145" y="15" width="50" height="25" rx="3" fill="#f59e0b"/>
      <text x="170" y="31" fill="#000000" font-size="8" text-anchor="middle" font-weight="bold">🎪 Mela</text>

      <!-- Active Marker -->
      <circle id="sim15Marker" cx="35" cy="110" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" style="transition:all 0.4s ease;"/>
    </svg>
    <div id="sim15Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🏠 <b>Start Point:</b> Walking east from home toward the bus stop along the pedestrian footpath.
    </div>
  </div>
</div>
<script>
function sim15Route(step) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(step)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const m = document.getElementById('sim15Marker');
  const fb = document.getElementById('sim15Feedback');

  if (step === 'home') {
    m.setAttribute('cx', '35');
    m.setAttribute('cy', '110');
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🏠 <b>Home (South-West):</b> Journey begins by walking safely along the footpath to the main road.';
  } else if (step === 'bus') {
    m.setAttribute('cx', '80');
    m.setAttribute('cy', '60');
    fb.style.color = '#34d399';
    fb.innerHTML = '📚 <b>Bus Stop & Library:</b> Boarding Bus 401 across from the public library to travel northeast across town.';
  } else if (step === 'parade') {
    m.setAttribute('cx', '170');
    m.setAttribute('cy', '30');
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🎪 <b>Parade Ground (North-East):</b> Destination reached! Vast open fairground with rides, stalls, and amenities.';
  }
}
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🤝 Community Helpers & Mock Mela Roles</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16Role('halwai')">Halwai (Sweetmaker)</button>
      <button class="sim-btn" onclick="sim16Role('puppeteer')">Puppeteer Artist</button>
      <button class="sim-btn" onclick="sim16Role('driver')">Bus Driver & Conductor</button>
      <button class="sim-btn" onclick="sim16Role('cleaner')">Sanitation Worker</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim16Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim16Icon" style="font-size:38px;">👨‍🍳 🍲 🍯</div>
      <div id="sim16Title" style="font-size:14px; font-weight:bold; color:#fbbf24; margin-top:4px;">Master Halwai (Confectioner)</div>
    </div>
    <div id="sim16Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      👨‍🍳 <b>Culinary Artisan:</b> Cooks golden jalebis, laddoos, and spicy chhole over iron woks, bringing festive joy to hungry crowds!
    </div>
  </div>
</div>
<script>
function sim16Role(role) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(role)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim16Icon');
  const title = document.getElementById('sim16Title');
  const fb = document.getElementById('sim16Feedback');

  if (role === 'halwai') {
    icon.innerHTML = '👨‍🍳 🍲 🍯';
    title.innerHTML = 'Master Halwai (Confectioner)';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '👨‍🍳 <b>Culinary Helper:</b> Prepares traditional sweets and savory snacks with skill, providing nourishment for fairgoers.';
  } else if (role === 'puppeteer') {
    icon.innerHTML = '🎭 🎎 🥁';
    title.innerHTML = 'Puppeteer (Cultural Storyteller)';
    fb.style.color = '#f472b6';
    fb.innerHTML = '🎭 <b>Cultural Artist:</b> Entertains audiences with string marionettes and dholak beats, teaching moral fables to children.';
  } else if (role === 'driver') {
    icon.innerHTML = '🚌 🎫 🛣️';
    title.innerHTML = 'Bus Driver & Ticket Conductor';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🚌 <b>Transit Lifeline:</b> Safely navigates urban roadways and issues tickets, connecting citizens across town affordably.';
  } else if (role === 'cleaner') {
    icon.innerHTML = '🧹 🧤 ♻️';
    title.innerHTML = 'Municipal Sanitation Worker';
    fb.style.color = '#34d399';
    fb.innerHTML = '🧹 <b>Environmental Guardian:</b> Empties dustbins and clears grounds, keeping public spaces hygienic, clean, and disease-free.';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9 to 16).")
    for k in sorted(sims_part2.keys()):
        print(f"Sim {k}: length {len(sims_part2[k])} chars")

#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Science (Our Wondrous World)
Chapter 1: Family and Friends
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🧹 Shared Domestic Chores Organizer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Task('plates')">Dinner Plate Setting</button>
      <button class="sim-btn" onclick="sim9Task('plants')">Watering Plants</button>
      <button class="sim-btn" onclick="sim9Task('hair')">Hair Oiling & Braiding</button>
      <button class="sim-btn" onclick="sim9Task('fold')">Folding Clean Laundry</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim9Visual" style="width:200px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <div id="sim9Icon" style="font-size:38px;">🍽️ 🥣 🥄</div>
      <div id="sim9Label" style="font-size:14px; font-weight:bold; color:#fbbf24; margin-top:6px;">Setting Dining Table</div>
    </div>
    <div id="sim9Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🍽️ <b>Plate Setting:</b> Children help lay stainless steel thalis and cups, building responsibility and preparing for family dinner.
    </div>
  </div>
</div>
<script>
function sim9Task(task) {
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(task)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim9Icon');
  const label = document.getElementById('sim9Label');
  const fb = document.getElementById('sim9Feedback');

  if (task === 'plates') {
    icon.innerHTML = '🍽️ 🥣 🥄';
    label.innerHTML = 'Setting Dining Table';
    fb.style.color = '#34d399';
    fb.innerHTML = '🍽️ <b>Dinner Preparation:</b> Setting clean plates, spoons, and drinking water cups teaches table manners and helpful cooperation.';
  } else if (task === 'plants') {
    icon.innerHTML = '🪴 🚿 🌿';
    label.innerHTML = 'Watering Courtyard Plants';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🪴 <b>Botanical Care:</b> Watering potted herbs in the morning prevents wilting and connects children with living nature.';
  } else if (task === 'hair') {
    icon.innerHTML = '💆 🪮 🎵';
    label.innerHTML = 'Oiling & Braiding Hair';
    fb.style.color = '#f472b6';
    fb.innerHTML = '🪮 <b>Loving Bonding Ritual:</b> Family elders gently massage fragrant coconut oil and braid hair while humming traditional folk tunes.';
  } else if (task === 'fold') {
    icon.innerHTML = '👕 👖 🧺';
    label.innerHTML = 'Folding Dry Laundry';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🧺 <b>Neat Organization:</b> Folding dry cotton clothes and organizing wardrobes cultivates tidy habits and self-reliance.';
  }
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🏘️ Neighborhood Solidarity & Harmony Map</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Action('sweets')">Share Festival Sweets</button>
      <button class="sim-btn" onclick="sim10Action('emergency')">Emergency First Help</button>
      <button class="sim-btn" onclick="sim10Action('quiet')">Respect Quiet Hours</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim10Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Street Road -->
      <rect x="0" y="55" width="240" height="30" fill="#334155"/>
      <line x1="0" y1="70" x2="240" y2="70" stroke="#f8fafc" stroke-width="2" stroke-dasharray="8 6"/>

      <!-- House 1 (Our Family) -->
      <rect x="25" y="15" width="55" height="40" fill="#3b82f6" rx="3"/>
      <polygon points="15,15 52,0 90,15" fill="#1d4ed8"/>
      <text x="52" y="38" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">Our Home</text>

      <!-- House 2 (Friendly Neighbors) -->
      <rect x="160" y="15" width="55" height="40" fill="#10b981" rx="3"/>
      <polygon points="150,15 187,0 225,15" fill="#047857"/>
      <text x="187" y="38" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">Neighbors</text>

      <!-- Animated Bridge / Interaction -->
      <g id="sim10Interaction" transform="translate(120, 65)">
        <circle cx="0" cy="0" r="12" fill="#f59e0b" opacity="0.9"/>
        <text x="0" y="4" font-size="12" text-anchor="middle">🎁</text>
      </g>
    </svg>
    <div id="sim10Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎁 <b>Festive Sharing:</b> Exchanging homemade laddoos and festival delicacies across the street builds lifelong community bonds!
    </div>
  </div>
</div>
<script>
function sim10Action(act) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(act)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const inter = document.getElementById('sim10Interaction');
  const fb = document.getElementById('sim10Feedback');

  if (act === 'sweets') {
    inter.innerHTML = `
      <circle cx="0" cy="0" r="12" fill="#f59e0b" opacity="0.9"/>
      <text x="0" y="4" font-size="12" text-anchor="middle">🎁</text>
    `;
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🎁 <b>Festive Delicacies:</b> Neighbors visit with plates of sweets and greetings during Diwali, Eid, Christmas, and Pongal.';
  } else if (act === 'emergency') {
    inter.innerHTML = `
      <circle cx="0" cy="0" r="12" fill="#ef4444" opacity="0.9"/>
      <text x="0" y="4" font-size="12" text-anchor="middle">🚑</text>
    `;
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🚑 <b>First Responders:</b> In sudden crises like sudden power cuts or medical illness, helpful neighbors arrive with immediate aid.';
  } else if (act === 'quiet') {
    inter.innerHTML = `
      <circle cx="0" cy="0" r="12" fill="#8b5cf6" opacity="0.9"/>
      <text x="0" y="4" font-size="12" text-anchor="middle">🤫</text>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '🤫 <b>Quiet Hours Etiquette:</b> Refraining from loud television or shouting after 9 PM respects elders and sleeping infants.';
  }
}
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🍂 Eco-Friendly Fallen Leaf Rangoli Lab</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Pattern('marigold')">Fallen Marigold Petals</button>
      <button class="sim-btn" onclick="sim11Pattern('leaves')">Fallen Dry Neem Leaves</button>
      <button class="sim-btn" onclick="sim11Pattern('compost')">Recycle into Compost</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim11Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Concentric rangoli guide rings -->
      <circle cx="120" cy="70" r="50" fill="none" stroke="rgba(255,255,255,0.15)" stroke-dasharray="3 3"/>
      <circle cx="120" cy="70" r="30" fill="none" stroke="rgba(255,255,255,0.15)" stroke-dasharray="3 3"/>
      <circle cx="120" cy="70" r="10" fill="none" stroke="rgba(255,255,255,0.2)"/>

      <!-- Botanical Elements -->
      <g id="sim11Elements"></g>
    </svg>
    <div id="sim11Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🌼 <b>Natural Materials:</b> Using fallen flowers avoids ripping live blooms from plants, protecting garden pollinators!
    </div>
  </div>
</div>
<script>
function sim11Pattern(pat) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(pat)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const el = document.getElementById('sim11Elements');
  const fb = document.getElementById('sim11Feedback');

  if (pat === 'marigold') {
    let p = '<circle cx="120" cy="70" r="8" fill="#f59e0b"/>';
    for (let i = 0; i < 8; i++) {
      const a = i * Math.PI / 4;
      const x = 120 + 30 * Math.cos(a);
      const y = 70 + 30 * Math.sin(a);
      p += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="7" fill="#d97706"/>`;
    }
    for (let i = 0; i < 16; i++) {
      const a = i * Math.PI / 8;
      const x = 120 + 50 * Math.cos(a);
      const y = 70 + 50 * Math.sin(a);
      p += `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="5" ry="3" fill="#ea580c"/>`;
    }
    el.innerHTML = p;
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🌼 <b>Fallen Marigold Petals:</b> Gathered gently from courtyard floor stones to form brilliant golden concentric circles.';
  } else if (pat === 'leaves') {
    let p = '<circle cx="120" cy="70" r="8" fill="#15803d"/>';
    for (let i = 0; i < 8; i++) {
      const a = i * Math.PI / 4;
      const x = 120 + 32 * Math.cos(a);
      const y = 70 + 32 * Math.sin(a);
      p += `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="8" ry="4" transform="rotate(${i*45} ${x.toFixed(1)} ${y.toFixed(1)})" fill="#16a34a"/>`;
    }
    for (let i = 0; i < 12; i++) {
      const a = i * Math.PI / 6;
      const x = 120 + 50 * Math.cos(a);
      const y = 70 + 50 * Math.sin(a);
      p += `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="7" ry="3" transform="rotate(${i*30} ${x.toFixed(1)} ${y.toFixed(1)})" fill="#854d0e"/>`;
    }
    el.innerHTML = p;
    fb.style.color = '#34d399';
    fb.innerHTML = '🍃 <b>Shed Neem & Mango Leaves:</b> Natural green and golden-brown foliage creates symmetrical geometric starbursts without plucking.';
  } else if (pat === 'compost') {
    el.innerHTML = `
      <rect x="70" y="40" width="100" height="60" rx="8" fill="#451a03" stroke="#78350f" stroke-width="2"/>
      <text x="120" y="65" fill="#f8fafc" font-size="10" text-anchor="middle" font-weight="bold">♻️ Compost Pit</text>
      <text x="120" y="85" fill="#a3e635" font-size="9" text-anchor="middle">Rich Organic Humus</text>
    `;
    fb.style.color = '#a3e635';
    fb.innerHTML = '♻️ <b>Zero Chemical Waste:</b> Swept into the garden compost pit after the festival, turning into nutrient-rich soil humus!';
  }
}
setTimeout(() => sim11Pattern('marigold'), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🦯 Special Care & Inclusivity Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Scenario('walkway')">Clear Tripping Hazards</button>
      <button class="sim-btn" onclick="sim12Scenario('hearing')">Gentle Clear Speech</button>
      <button class="sim-btn" onclick="sim12Scenario('reading')">Reading Aloud</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim12Card" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim12Icon" style="font-size:36px;">🧹 👟 🧸</div>
      <div id="sim12Text" style="font-size:13px; font-weight:bold; color:#38bdf8; margin-top:4px; text-align:center;">Unobstructed Hallways</div>
    </div>
    <div id="sim12Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🧹 <b>Fall Prevention:</b> Keeping corridors free of loose shoes and toys protects elderly grandparents from severe fall injuries.
    </div>
  </div>
</div>
<script>
function sim12Scenario(scen) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(scen)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim12Icon');
  const text = document.getElementById('sim12Text');
  const fb = document.getElementById('sim12Feedback');

  if (scen === 'walkway') {
    icon.innerHTML = '✨ 🚶‍♂️ 🦯';
    text.innerHTML = 'Clear & Dry Walking Path';
    fb.style.color = '#34d399';
    fb.innerHTML = '🦯 <b>Safe Movement:</b> Removing loose rugs, shoes, and water spills ensures elders walk securely with confidence.';
  } else if (scen === 'hearing') {
    icon.innerHTML = '👂 🗣️ 💖';
    text.innerHTML = 'Face Directly & Speak Patiently';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '👂 <b>Patient Communication:</b> Facing hard-of-hearing relatives directly and speaking with calm, unhurried clarity without shouting.';
  } else if (scen === 'reading') {
    icon.innerHTML = '👓 📰 📖';
    text.innerHTML = 'Reading News & Labels Aloud';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '👓 <b>Visual Assistance:</b> Reading medicine dosage instructions and daily newspaper articles aloud for relatives with frail vision.';
  }
}
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🌳 Interactive Family Tree Explorer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Gen('grand')">1. Grandparents (Roots)</button>
      <button class="sim-btn" onclick="sim13Gen('parents')">2. Parents & Aunts/Uncles</button>
      <button class="sim-btn" onclick="sim13Gen('children')">3. Children & Cousins (Leaves)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim13Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Tree Structure Lines -->
      <line x1="120" y1="35" x2="60" y2="75" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="120" y1="35" x2="180" y2="75" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="60" y1="90" x2="35" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="60" y1="90" x2="85" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="180" y1="90" x2="180" y2="120" stroke="#94a3b8" stroke-width="1.5"/>

      <!-- Node 1: Grandparents (Top) -->
      <g id="sim13_n1" transform="translate(120, 25)">
        <rect x="-35" y="-12" width="70" height="22" rx="4" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
        <text x="0" y="3" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">Grandparents</text>
      </g>

      <!-- Node 2: Parents (Middle Left) -->
      <g id="sim13_n2" transform="translate(60, 80)">
        <rect x="-30" y="-10" width="60" height="20" rx="4" fill="#2563eb" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="0" y="3" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">Parents</text>
      </g>

      <!-- Node 3: Aunts/Uncles (Middle Right) -->
      <g id="sim13_n3" transform="translate(180, 80)">
        <rect x="-32" y="-10" width="64" height="20" rx="4" fill="#059669" stroke="#34d399" stroke-width="1.5"/>
        <text x="0" y="3" fill="#ffffff" font-size="7.5" text-anchor="middle" font-weight="bold">Aunt & Uncle</text>
      </g>

      <!-- Node 4: Siblings & Self (Bottom Left) -->
      <g id="sim13_n4" transform="translate(60, 125)">
        <rect x="-35" y="-8" width="70" height="16" rx="3" fill="#7c3aed" stroke="#a78bfa" stroke-width="1.5"/>
        <text x="0" y="3" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">Self & Siblings</text>
      </g>

      <!-- Node 5: Cousins (Bottom Right) -->
      <g id="sim13_n5" transform="translate(180, 125)">
        <rect x="-25" y="-8" width="50" height="16" rx="3" fill="#db2777" stroke="#f472b6" stroke-width="1.5"/>
        <text x="0" y="3" fill="#ffffff" font-size="7.5" text-anchor="middle" font-weight="bold">Cousins</text>
      </g>
    </svg>
    <div id="sim13Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      👴👵 <b>Generation 1 (Roots):</b> Grandparents form the ancestral foundation, connecting maternal and paternal lines.
    </div>
  </div>
</div>
<script>
function sim13Gen(g) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(g)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const fb = document.getElementById('sim13Feedback');

  if (g === 'grand') {
    fb.style.color = '#fbbf24';
    fb.innerHTML = '👴👵 <b>Generation 1 (Roots):</b> Grandparents provide cultural traditions, wisdom, and ancestral family history.';
  } else if (g === 'parents') {
    fb.style.color = '#38bdf8';
    fb.innerHTML = '👨👩 <b>Generation 2 (Branches):</b> Parents, aunts, and uncles who nurture the home, provide livelihoods, and care for elders.';
  } else if (g === 'children') {
    fb.style.color = '#a78bfa';
    fb.innerHTML = '👧👦 <b>Generation 3 (Leaves):</b> Siblings and cousins who grow, learn, play, and carry family values into the bright future.';
  }
}
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🎯 Traditional Pitthoo (Seven Stones) Field Game</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Action('throw')">1. Throw Tennis Ball</button>
      <button class="sim-btn" onclick="sim14Action('scatter')">2. Tower Collapses</button>
      <button class="sim-btn" onclick="sim14Action('dodge')">3. Dodge & Rebuild!</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim14Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Green Park Grass -->
      <rect x="0" y="105" width="240" height="35" fill="#15803d"/>
      <!-- Pitch Circle -->
      <ellipse cx="120" cy="115" rx="35" ry="10" fill="none" stroke="#f8fafc" stroke-width="1.5" stroke-dasharray="3 3"/>

      <!-- Pitthoo 7 Stones -->
      <g id="sim14Stones">
        <rect x="106" y="102" width="28" height="6" rx="2" fill="#d97706" stroke="#1e293b"/>
        <rect x="108" y="96" width="24" height="6" rx="2" fill="#f59e0b" stroke="#1e293b"/>
        <rect x="110" y="90" width="20" height="6" rx="2" fill="#fbbf24" stroke="#1e293b"/>
        <rect x="112" y="84" width="16" height="6" rx="2" fill="#d97706" stroke="#1e293b"/>
        <rect x="114" y="78" width="12" height="6" rx="2" fill="#f59e0b" stroke="#1e293b"/>
        <rect x="116" y="72" width="8" height="6" rx="2" fill="#fbbf24" stroke="#1e293b"/>
        <rect x="117" y="66" width="6" height="6" rx="2" fill="#ea580c" stroke="#1e293b"/>
      </g>

      <!-- Striker with Ball -->
      <g id="sim14Striker" transform="translate(30, 95)">
        <circle cx="0" cy="-14" r="7" fill="#38bdf8"/>
        <line x1="0" y1="-7" x2="0" y2="12" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="0" y1="2" x2="10" y2="-4" stroke="#38bdf8" stroke-width="2.5"/>
        <circle id="sim14Ball" cx="14" cy="-5" r="4" fill="#a3e635"/>
      </g>
    </svg>
    <div id="sim14Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#a3e635; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎾 <b>Step 1:</b> Striker throws a soft rubber tennis ball toward the 7-stone tower from behind the crease.
    </div>
  </div>
</div>
<script>
function sim14Action(act) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(act)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const stones = document.getElementById('sim14Stones');
  const ball = document.getElementById('sim14Ball');
  const fb = document.getElementById('sim14Feedback');

  if (act === 'throw') {
    stones.innerHTML = `
      <rect x="106" y="102" width="28" height="6" rx="2" fill="#d97706" stroke="#1e293b"/>
      <rect x="108" y="96" width="24" height="6" rx="2" fill="#f59e0b" stroke="#1e293b"/>
      <rect x="110" y="90" width="20" height="6" rx="2" fill="#fbbf24" stroke="#1e293b"/>
      <rect x="112" y="84" width="16" height="6" rx="2" fill="#d97706" stroke="#1e293b"/>
      <rect x="114" y="78" width="12" height="6" rx="2" fill="#f59e0b" stroke="#1e293b"/>
      <rect x="116" y="72" width="8" height="6" rx="2" fill="#fbbf24" stroke="#1e293b"/>
      <rect x="117" y="66" width="6" height="6" rx="2" fill="#ea580c" stroke="#1e293b"/>
    `;
    ball.setAttribute('cx', '14');
    ball.setAttribute('cy', '-5');
    fb.style.color = '#a3e635';
    fb.innerHTML = '🎾 <b>Throwing Accuracy:</b> Striker aims carefully to topple the seven stacked stones!';
  } else if (act === 'scatter') {
    stones.innerHTML = `
      <rect x="95" y="108" width="18" height="5" rx="1" fill="#d97706"/>
      <rect x="118" y="106" width="14" height="5" rx="1" fill="#f59e0b"/>
      <rect x="135" y="110" width="12" height="5" rx="1" fill="#fbbf24"/>
      <rect x="105" y="112" width="10" height="5" rx="1" fill="#d97706"/>
      <rect x="125" y="112" width="8" height="4" rx="1" fill="#f59e0b"/>
    `;
    ball.setAttribute('cx', '120');
    ball.setAttribute('cy', '100');
    fb.style.color = '#f87171';
    fb.innerHTML = '💥 <b>Tower Toppled!</b> Stones scatter across the circle. Fielders rush to retrieve the ball while strikers sprint to rebuild!';
  } else if (act === 'dodge') {
    stones.innerHTML = `
      <rect x="108" y="104" width="24" height="6" rx="2" fill="#d97706"/>
      <rect x="110" y="98" width="20" height="6" rx="2" fill="#f59e0b"/>
      <rect x="112" y="92" width="16" height="6" rx="2" fill="#fbbf24"/>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '🏃 <b>Dodge & Rebuild:</b> Strikers duck and weave to avoid the ball while quickly restacking all 7 stones to win the round!';
  }
}
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">⏱️ Sportsmanship & Hydration Station</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Station('water')">Clean Hydration</button>
      <button class="sim-btn" onclick="sim15Station('rest')">20-Min Shade Rest</button>
      <button class="sim-btn" onclick="sim15Station('dusk')">Return Before Dusk</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim15Display" style="width:200px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <div id="sim15Icon" style="font-size:38px;">💧 🧊 🥤</div>
      <div id="sim15Label" style="font-size:13px; font-weight:bold; color:#38bdf8; margin-top:4px;">Replenish Fluids</div>
    </div>
    <div id="sim15Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      💧 <b>Hydration:</b> Sweating cools the body but depletes fluids. Drinking clean water prevents cramps and heat fatigue.
    </div>
  </div>
</div>
<script>
function sim15Station(st) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(st)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim15Icon');
  const label = document.getElementById('sim15Label');
  const fb = document.getElementById('sim15Feedback');

  if (st === 'water') {
    icon.innerHTML = '💧 🧊 🥤';
    label.innerHTML = 'Replenish Body Fluids';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '💧 <b>Hydration:</b> Drink small sips of water during match breaks to keep muscles functioning efficiently.';
  } else if (st === 'rest') {
    icon.innerHTML = '🌳 🧘 🍉';
    label.innerHTML = '20-Minute Tree Shade Pause';
    fb.style.color = '#34d399';
    fb.innerHTML = '🌳 <b>Cooling Down:</b> Resting under shady branches lowers heart rate and body temperature after vigorous running.';
  } else if (st === 'dusk') {
    icon.innerHTML = '🌅 🎒 🏠';
    label.innerHTML = 'Safe Sunset Departure';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🌅 <b>Safe Departure:</b> Pack all sports gear, pick up any litter, and walk home safely before nightfall with playmates.';
  }
}
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🧩 Family Values & Social Bond Matrix</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16Value('empathy')">Empathy</button>
      <button class="sim-btn" onclick="sim16Value('inclusivity')">Inclusivity</button>
      <button class="sim-btn" onclick="sim16Value('cooperation')">Cooperation</button>
      <button class="sim-btn" onclick="sim16Value('respect')">Respect</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim16Card" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim16Icon" style="font-size:38px;">💖 🤝 👂</div>
      <div id="sim16Word" style="font-size:16px; font-weight:bold; color:#f472b6; margin-top:4px;">EMPATHY</div>
    </div>
    <div id="sim16Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#f472b6; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      💖 <b>Empathy:</b> Feeling and understanding another person's emotions, offering a comforting hand whenever someone is hurting.
    </div>
  </div>
</div>
<script>
function sim16Value(val) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(val)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim16Icon');
  const word = document.getElementById('sim16Word');
  const fb = document.getElementById('sim16Feedback');

  if (val === 'empathy') {
    icon.innerHTML = '💖 🤝 👂';
    word.innerHTML = 'EMPATHY';
    fb.style.color = '#f472b6';
    fb.innerHTML = '💖 <b>Empathy:</b> Putting yourself in another person\'s place and offering compassionate comfort when they need help.';
  } else if (val === 'inclusivity') {
    icon.innerHTML = '🌈 👧 👦 🧒';
    word.innerHTML = 'INCLUSIVITY';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🌈 <b>Inclusivity:</b> Welcoming every single playmate into the group, ensuring no child feels left out or lonely.';
  } else if (val === 'cooperation') {
    icon.innerHTML = '🐝 🏗️ 🧺';
    word.innerHTML = 'COOPERATION';
    fb.style.color = '#34d399';
    fb.innerHTML = '🐝 <b>Cooperation:</b> Working harmoniously together toward common domestic and community goals, dividing tasks fairly.';
  } else if (val === 'respect') {
    icon.innerHTML = '🙏 👵 👴';
    word.innerHTML = 'RESPECT';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🙏 <b>Respect:</b> Valuing the dignity of elders, parents, neighbors, companion animals, and the natural living environment.';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9 to 16).")
    for k in sorted(sims_part2.keys()):
        print(f"Sim {k}: length {len(sims_part2[k])} chars")

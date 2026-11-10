#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Science (Our Wondrous World)
Chapter 1: Family and Friends
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🏃 Courtyard Playtime & Games Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Select('hide')">Hide & Seek</button>
      <button class="sim-btn" onclick="sim1Select('tag')">Active Tag</button>
      <button class="sim-btn" onclick="sim1Select('peek')">Peek-a-Boo</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim1Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Tree for hiding -->
      <rect x="35" y="60" width="14" height="60" fill="#78350f" rx="2"/>
      <circle cx="42" cy="50" r="32" fill="#15803d" opacity="0.9"/>
      <!-- Veranda watching area -->
      <rect x="170" y="30" width="60" height="90" fill="#334155" rx="4"/>
      <polygon points="160,30 200,8 240,30" fill="#b91c1c"/>
      <text x="200" y="70" fill="#f8fafc" font-size="8" text-anchor="middle">Veranda</text>
      <!-- Seeker / Player 1 -->
      <g id="sim1Player1" transform="translate(110, 85)">
        <circle cx="0" cy="-14" r="8" fill="#f59e0b"/>
        <line x1="0" y1="-6" x2="0" y2="15" stroke="#f59e0b" stroke-width="3"/>
        <line x1="-8" y1="2" x2="8" y2="2" stroke="#f59e0b" stroke-width="2.5"/>
        <line x1="0" y1="15" x2="-6" y2="28" stroke="#f59e0b" stroke-width="2.5"/>
        <line x1="0" y1="15" x2="6" y2="28" stroke="#f59e0b" stroke-width="2.5"/>
      </g>
      <!-- Hider / Player 2 -->
      <g id="sim1Player2" transform="translate(48, 85)">
        <circle cx="0" cy="-14" r="7" fill="#38bdf8"/>
        <line x1="0" y1="-7" x2="0" y2="14" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="0" y1="14" x2="-5" y2="26" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="14" x2="5" y2="26" stroke="#38bdf8" stroke-width="2"/>
      </g>
    </svg>
    <div id="sim1Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🌳 <b>Hide-and-Seek:</b> Player hides behind the courtyard tree while seeker counts. Builds observation and spatial memory!
    </div>
  </div>
</div>
<script>
function sim1Select(game) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(game)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const p1 = document.getElementById('sim1Player1');
  const p2 = document.getElementById('sim1Player2');
  const fb = document.getElementById('sim1Feedback');

  if (game === 'hide') {
    p1.setAttribute('transform', 'translate(110, 85)');
    p2.setAttribute('transform', 'translate(48, 85)');
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🌳 <b>Hide-and-Seek:</b> Counting player uses listening skills while companions hide safely in open courtyard spots.';
  } else if (game === 'tag') {
    p1.setAttribute('transform', 'translate(80, 85)');
    p2.setAttribute('transform', 'translate(140, 85)');
    fb.style.color = '#34d399';
    fb.innerHTML = '🏃 <b>Active Tag Sprint:</b> Chasing and dodging builds strong heart health, stamina, and bone strength in fresh evening air.';
  } else if (game === 'peek') {
    p1.setAttribute('transform', 'translate(100, 85)');
    p2.setAttribute('transform', 'translate(125, 95)');
    fb.style.color = '#fbbf24';
    fb.innerHTML = '👶 <b>Gentle Peek-a-Boo:</b> Toddler laughs joyfully as elders cover and reveal their eyes, reinforcing object permanence.';
  }
}
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">🌿 Courtyard Garden Ecosystem Explorer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2Plant('jasmine')">Jasmine Bush</button>
      <button class="sim-btn" onclick="sim2Plant('marigold')">Marigold Flowers</button>
      <button class="sim-btn" onclick="sim2Plant('tulsi')">Sacred Tulsi</button>
      <button class="sim-btn" onclick="sim2Action('relax')">Family Gathering</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim2Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Soil Ground -->
      <rect x="0" y="110" width="240" height="30" fill="#451a03"/>
      <!-- Wooden Bench -->
      <rect x="140" y="80" width="80" height="8" rx="2" fill="#92400e"/>
      <rect x="148" y="88" width="6" height="25" fill="#78350f"/>
      <rect x="206" y="88" width="6" height="25" fill="#78350f"/>
      <!-- Selected Plant Center -->
      <g id="sim2PlantGroup" transform="translate(60, 110)">
        <!-- Default Jasmine -->
        <path d="M 0 0 Q -10 -40 -5 -70 Q 10 -40 0 0" fill="#15803d"/>
        <circle cx="-12" cy="-60" r="6" fill="#ffffff" stroke="#e2e8f0"/>
        <circle cx="8" cy="-55" r="6" fill="#ffffff" stroke="#e2e8f0"/>
        <circle cx="0" cy="-75" r="7" fill="#ffffff" stroke="#e2e8f0"/>
      </g>
      <!-- Butterflies / Pollinators -->
      <g id="sim2Insects" transform="translate(75, 45)">
        <polygon points="0,0 6,-6 4,-1" fill="#ec4899"/>
        <polygon points="0,0 6,6 4,1" fill="#ec4899"/>
      </g>
    </svg>
    <div id="sim2Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🌸 <b>Jasmine (Chameli):</b> Releases sweet, calming fragrance that relieves stress after a busy workday.
    </div>
  </div>
</div>
<script>
function sim2Plant(type) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(type)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const pg = document.getElementById('sim2PlantGroup');
  const fb = document.getElementById('sim2Feedback');

  if (type === 'jasmine') {
    pg.innerHTML = `
      <path d="M 0 0 Q -10 -40 -5 -70 Q 10 -40 0 0" fill="#15803d"/>
      <circle cx="-12" cy="-60" r="6" fill="#ffffff" stroke="#e2e8f0"/>
      <circle cx="8" cy="-55" r="6" fill="#ffffff" stroke="#e2e8f0"/>
      <circle cx="0" cy="-75" r="7" fill="#ffffff" stroke="#e2e8f0"/>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '🌸 <b>Jasmine (Chameli):</b> Produces fragrant white flowers whose natural aromatic oils calm the senses.';
  } else if (type === 'marigold') {
    pg.innerHTML = `
      <path d="M 0 0 Q -15 -35 -10 -65 Q 15 -35 0 0" fill="#166534"/>
      <circle cx="-12" cy="-55" r="9" fill="#f59e0b"/>
      <circle cx="10" cy="-50" r="9" fill="#d97706"/>
      <circle cx="-2" cy="-70" r="10" fill="#f59e0b"/>
    `;
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🌼 <b>Marigold (Genda):</b> Vibrant golden blooms attract pollinators and are used for traditional festive garlands.';
  } else if (type === 'tulsi') {
    pg.innerHTML = `
      <path d="M 0 0 Q -8 -30 -4 -60 Q 8 -30 0 0" fill="#14532d"/>
      <ellipse cx="-8" cy="-45" rx="5" ry="3" fill="#22c55e"/>
      <ellipse cx="8" cy="-42" rx="5" ry="3" fill="#22c55e"/>
      <ellipse cx="-2" cy="-58" rx="6" ry="4" fill="#22c55e"/>
    `;
    fb.style.color = '#10b981';
    fb.innerHTML = '🌿 <b>Sacred Tulsi (Holy Basil):</b> Medicinal courtyard plant that purifies air and is prized for immune-boosting herbal teas.';
  }
}

function sim2Action(act) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes('gathering')) b.classList.add('active');
    else b.classList.remove('active');
  });
  const fb = document.getElementById('sim2Feedback');
  fb.style.color = '#38bdf8';
  fb.innerHTML = '👨‍👩‍👧‍👦 <b>Evening Family Gathering:</b> Parents and elders sit on wooden benches, sharing laughter, tea, and warm conversations amidst nature.';
}
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🎲 Monsoon Indoor Games Center</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Play('dice')">Roll Dice</button>
      <button class="sim-btn" onclick="sim3Play('antakshari')">Antakshari Song Chain</button>
      <button class="sim-btn" onclick="sim3Play('snacks')">Hot Pakodas & Tea</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Mini Board Display -->
    <div id="sim3Display" style="width:200px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <div id="sim3Visual" style="font-size:38px;">🎲</div>
      <div id="sim3Text" style="font-size:14px; font-weight:bold; color:#fbbf24; margin-top:4px;">Roll = 4</div>
    </div>
    <div id="sim3Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎲 <b>Snakes & Ladders:</b> Advancing along the board teaches patience, turn-taking, and graceful acceptance of surprises!
    </div>
  </div>
</div>
<script>
let sim3RollCount = 0;
const sim3Songs = [
    { letter: 'M', song: '🎵 Megha re megha re...', team: 'Team A sings letter M' },
    { letter: 'R', song: '🎵 Rimjhim gire saawan...', team: 'Team B responds with R' },
    { letter: 'N', song: '🎵 Nani teri morni ko mor...', team: 'Team A answers with N' }
];

function sim3Play(mode) {
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(mode)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const vis = document.getElementById('sim3Visual');
  const txt = document.getElementById('sim3Text');
  const fb = document.getElementById('sim3Feedback');

  if (mode === 'dice') {
    const r = Math.floor(Math.random() * 6) + 1;
    const icons = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
    vis.innerHTML = icons[r - 1];
    txt.innerHTML = `Rolled: ${r}`;
    fb.style.color = '#38bdf8';
    fb.innerHTML = `🎲 <b>Dice Roll ${r}:</b> Move counter forward ${r} steps on the board. Climb ladders or slide down snakes with a smile!`;
  } else if (mode === 'antakshari') {
    sim3RollCount = (sim3RollCount + 1) % sim3Songs.length;
    const s = sim3Songs[sim3RollCount];
    vis.innerHTML = '🎤';
    txt.innerHTML = s.letter;
    fb.style.color = '#f472b6';
    fb.innerHTML = `🎶 <b>${s.team}:</b> "${s.song}" — Family singing games exercise musical memory and joyful togetherness!`;
  } else if (mode === 'snacks') {
    vis.innerHTML = '🫖 🍘';
    txt.innerHTML = 'Hot Snacks';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '☕ <b>Warm Hospitality:</b> Sharing fresh, crispy gram-flour pakodas and spiced tea while rain taps on the roof!';
  }
}
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">🌧️ Monsoon Physics & Nature Lab</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4Select('boat')">Paper Boat Buoyancy</button>
      <button class="sim-btn" onclick="sim4Select('peacock')">Dancing Peacock</button>
      <button class="sim-btn" onclick="sim4Select('bird')">Feather Insulation</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim4Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Rain Stream Surface -->
      <path d="M 0 100 Q 60 95 120 100 Q 180 105 240 100 L 240 140 L 0 140 Z" fill="#0284c7" opacity="0.6"/>
      <!-- Rain Streaks -->
      <line x1="40" y1="10" x2="35" y2="35" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="2 4"/>
      <line x1="90" y1="15" x2="85" y2="40" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="2 4"/>
      <line x1="160" y1="5" x2="155" y2="30" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="2 4"/>
      <line x1="210" y1="12" x2="205" y2="37" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="2 4"/>

      <!-- Subject Graphics Group -->
      <g id="sim4Graphic" transform="translate(100, 80)">
        <!-- Default Paper Boat -->
        <polygon points="0,15 40,15 32,25 8,25" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="12,15 20,0 20,15" fill="#ef4444"/>
        <polygon points="20,15 28,5 20,5" fill="#3b82f6"/>
      </g>
    </svg>
    <div id="sim4Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ⛵ <b>Buoyancy:</b> Hollow paper shape displaces water equal to its weight, floating safely until water saturates the fibers.
    </div>
  </div>
</div>
<script>
function sim4Select(phenomenon) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(phenomenon)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const g = document.getElementById('sim4Graphic');
  const fb = document.getElementById('sim4Feedback');

  if (phenomenon === 'boat') {
    g.innerHTML = `
      <polygon points="0,15 40,15 32,25 8,25" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
      <polygon points="12,15 20,0 20,15" fill="#ef4444"/>
      <polygon points="20,15 28,5 20,5" fill="#3b82f6"/>
    `;
    fb.style.color = '#38bdf8';
    fb.innerHTML = '⛵ <b>Archimedes Principle:</b> Lightweight folded paper boat stays afloat as water pushes upwards against its hollow base.';
  } else if (phenomenon === 'peacock') {
    g.innerHTML = `
      <!-- Peacock body and fan -->
      <path d="M 20 -20 C -20 -40 60 -40 20 -20" stroke="#047857" stroke-width="12" fill="none"/>
      <circle cx="20" cy="-25" r="14" fill="#0284c7" opacity="0.8"/>
      <ellipse cx="20" cy="5" rx="8" ry="14" fill="#0369a1"/>
      <circle cx="20" cy="-12" r="6" fill="#0284c7"/>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '🦚 <b>Courtship Display:</b> Male peacock spreads iridescent tail coverts in a magnificent fan to celebrate monsoon rains!';
  } else if (phenomenon === 'bird') {
    g.innerHTML = `
      <!-- Fluffed small bird on perch -->
      <line x1="-15" y1="20" x2="55" y2="20" stroke="#78350f" stroke-width="4"/>
      <circle cx="20" cy="8" r="16" fill="#b45309"/>
      <circle cx="30" cy="-2" r="8" fill="#d97706"/>
      <polygon points="36,-2 44,0 36,3" fill="#ea580c"/>
    `;
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🐦 <b>Thermal Insulation:</b> Small birds fluff their feathers to trap warm air pockets, preventing chilly rainwater from touching skin.';
  }
}
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">👵 Grandparent Heritage Games Console</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5Select('gitte')">Gitte (5 Pebbles)</button>
      <button class="sim-btn" onclick="sim5Select('top')">Lattoo (Spinning Top)</button>
      <button class="sim-btn" onclick="sim5Select('seeds')">Tamarind Seed Mancala</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim5Canvas" style="width:200px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <div id="sim5Icon" style="font-size:36px;">🪨 🪨 🪨 🪨 🪨</div>
      <div id="sim5Name" style="font-size:14px; font-weight:bold; color:#fbbf24; margin-top:6px;">Gitte Hand Toss</div>
    </div>
    <div id="sim5Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🪨 <b>Gitte (Five Pebbles):</b> Toss one pebble up while snatching another from the floor! Develops lightning-fast reflexes and focus.
    </div>
  </div>
</div>
<script>
function sim5Select(game) {
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(game)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim5Icon');
  const name = document.getElementById('sim5Name');
  const fb = document.getElementById('sim5Feedback');

  if (game === 'gitte') {
    icon.innerHTML = '🪨 🪨 🪨 🪨 🪨';
    name.innerHTML = 'Gitte (5 Smooth Pebbles)';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🪨 <b>Dexterity Training:</b> Taught by grandparents, tossing and scooping smooth stones builds hand-eye coordination!';
  } else if (game === 'top') {
    icon.innerHTML = '🌀 🪵';
    name.innerHTML = 'Lattoo Spinning Top';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🌀 <b>Angular Momentum:</b> Wrapping string around a carved wooden top and flicking it spins smoothly on its metal tip!';
  } else if (game === 'seeds') {
    icon.innerHTML = '🌰 🌰 🌰 🌰';
    name.innerHTML = 'Tamarind Seed Strategy';
    fb.style.color = '#34d399';
    fb.innerHTML = '🌰 <b>Traditional Counting:</b> Moving smooth tamarind seeds between wooden cups sharpens mental arithmetic and strategic thinking.';
  }
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🐕 Companion Animal Kindness Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Care('feed')">Provide Food Bowl</button>
      <button class="sim-btn" onclick="sim6Care('water')">Fresh Water Dish</button>
      <button class="sim-btn" onclick="sim6Care('brush')">Gentle Fur Brushing</button>
      <button class="sim-btn" onclick="sim6Care('stray')">Care for Stray Animals</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim6Display" style="width:200px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <div id="sim6Dog" style="font-size:42px;">🐕</div>
      <div id="sim6Status" style="font-size:13px; font-weight:bold; color:#34d399; margin-top:4px;">Happy & Well Fed!</div>
    </div>
    <div id="sim6Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🍲 <b>Nutritious Food:</b> Sharing wholesome food with companion animals satisfies hunger and builds unconditional love and loyalty.
    </div>
  </div>
</div>
<script>
function sim6Care(action) {
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(action)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const dog = document.getElementById('sim6Dog');
  const stat = document.getElementById('sim6Status');
  const fb = document.getElementById('sim6Feedback');

  if (action === 'feed') {
    dog.innerHTML = '🐕 🥣';
    stat.innerHTML = 'Nourished & Content';
    fb.style.color = '#34d399';
    fb.innerHTML = '🥣 <b>Wholesome Food:</b> Pets need regular, nutritious food. We never feed animals harmful spicy or toxic scraps.';
  } else if (action === 'water') {
    dog.innerHTML = '🐕 💧';
    stat.innerHTML = 'Hydrated & Refreshed';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '💧 <b>Potable Water:</b> A shallow clay bowl with clean water protects animals from summer heat dehydration.';
  } else if (action === 'brush') {
    dog.innerHTML = '🐕 🧼';
    stat.innerHTML = 'Clean & Pampered';
    fb.style.color = '#f472b6';
    fb.innerHTML = '🧼 <b>Hygiene & Affection:</b> Brushing pet fur gently removes dirt and loose hair while strengthening emotional attachment.';
  } else if (action === 'stray') {
    dog.innerHTML = '🐕‍🦺 🕊️';
    stat.innerHTML = 'Neighborhood Harmony';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🕊️ <b>Stray Kindness:</b> Leaving clean water and dry chapatis outside the gate sustains community animals without teasing or cruelty.';
  }
}
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🏠 Diverse Family Structure Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Type('nuclear')">Nuclear Family</button>
      <button class="sim-btn" onclick="sim7Type('joint')">Joint Family</button>
      <button class="sim-btn" onclick="sim7Type('single')">Single-Parent Home</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim7Members" style="font-size:36px; margin-bottom:8px;">👨 👩 👧 👦</div>
    <div id="sim7Desc" style="font-size:14px; font-weight:bold; color:#fbbf24;">Parents + Children (4 Members)</div>
    <div id="sim7Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🏡 <b>Nuclear Family:</b> A compact home where parents and children share domestic responsibilities through close teamwork.
    </div>
  </div>
</div>
<script>
function sim7Type(t) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(t)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const mem = document.getElementById('sim7Members');
  const desc = document.getElementById('sim7Desc');
  const fb = document.getElementById('sim7Feedback');

  if (t === 'nuclear') {
    mem.innerHTML = '👨 👩 👧 👦';
    desc.innerHTML = 'Parents + Children (Nuclear Household)';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🏡 <b>Nuclear Family:</b> Parents and siblings living together, sharing daily chores and cultivating self-reliance.';
  } else if (t === 'joint') {
    mem.innerHTML = '👴 👵 👨 👩 👨‍🦱 👩‍🦱 👦 👧 👶';
    desc.innerHTML = 'Grandparents + Parents + Aunts/Uncles + Cousins';
    fb.style.color = '#34d399';
    fb.innerHTML = '🏰 <b>Joint Family:</b> Multiple generations sharing one roof and kitchen. Constant elder guidance and cousin camaraderie!';
  } else if (t === 'single') {
    mem.innerHTML = '👩 👧 👦 (or 👨 👧 👦)';
    desc.innerHTML = 'Single Parent + Children';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '❤️ <b>Dedicated Parenting:</b> Bound by deep love and resilience, often supported by caring relatives and friendly neighbors.';
  }
}
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🤝 Family Roles & Mutual Support Matrix</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Role('grandparents')">Grandparents' Role</button>
      <button class="sim-btn" onclick="sim8Role('parents')">Parents' Role</button>
      <button class="sim-btn" onclick="sim8Role('children')">Children's Role</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim8Icon" style="font-size:38px; margin-bottom:8px;">👵 📖 👴</div>
    <div id="sim8Duty" style="font-size:14px; font-weight:bold; color:#fbbf24;">Wisdom, Supervision & Storytelling</div>
    <div id="sim8Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      📜 <b>Moral Anchors:</b> Grandparents teach ethical values, supervise daily play, and provide emotional security to youngsters.
    </div>
  </div>
</div>
<script>
function sim8Role(role) {
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(role)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim8Icon');
  const duty = document.getElementById('sim8Duty');
  const fb = document.getElementById('sim8Feedback');

  if (role === 'grandparents') {
    icon.innerHTML = '👵 📖 👴';
    duty.innerHTML = 'Wisdom, Moral Stories & Loving Supervision';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '📜 <b>Elders:</b> Transmit cultural traditions, resolve family disputes with calm patience, and guide the younger generations.';
  } else if (role === 'parents') {
    icon.innerHTML = '👨‍🍳 💼 👩‍🏫 🛒';
    duty.innerHTML = 'Nourishment, Education & Domestic Care';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '💼 <b>Parents:</b> Work diligently to earn livelihoods, cook wholesome meals, guide school studies, and ensure healthcare.';
  } else if (role === 'children') {
    icon.innerHTML = '📚 🧹 🪴 👧 👦';
    duty.innerHTML = 'Helpful Chores, Diligent Study & Elder Care';
    fb.style.color = '#34d399';
    fb.innerHTML = '🪴 <b>Children:</b> Study faithfully, organize their belongings, run errands, water garden plants, and care for aging elders.';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1 to 8).")
    for k in sorted(sims_part1.keys()):
        print(f"Sim {k}: length {len(sims_part1[k])} chars")

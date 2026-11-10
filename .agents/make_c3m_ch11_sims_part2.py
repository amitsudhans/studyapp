#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">💪 Muscular Weight Sensing & Gravity Test</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Hold(true)">Hold Items for 30 Seconds</button>
      <button class="sim-btn" onclick="sim9Hold(false)">Lower Hands (Rest)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-around; width:100%; max-width:550px; margin-bottom:12px;">
      <!-- Left Hand: 3 Textbooks -->
      <div style="flex:1; background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:12px; padding:12px; text-align:center; margin:0 6px;">
        <div style="font-size:12px; color:#fca5a5; font-weight:bold;">Left Hand (Dense Stack)</div>
        <div style="font-size:30px; margin:4px 0;">📚📚📚</div>
        <div style="font-size:14px; font-weight:bold; color:#fff;">3 Math Textbooks</div>
        <div id="sim9LeftStrain" style="font-size:12px; color:#f87171; font-weight:bold; margin-top:6px;">Muscles: Heavy Downward Pull! ⬇️</div>
      </div>
      <!-- Right Hand: Empty Pencil Box -->
      <div style="flex:1; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center; margin:0 6px;">
        <div style="font-size:12px; color:#6ee7b7; font-weight:bold;">Right Hand (Hollow Box)</div>
        <div style="font-size:30px; margin:4px 0;">✏️📦</div>
        <div style="font-size:14px; font-weight:bold; color:#fff;">Empty Pencil Box</div>
        <div id="sim9RightStrain" style="font-size:12px; color:#34d399; font-weight:bold; margin-top:6px;">Muscles: Light & Relaxed 🟢</div>
      </div>
    </div>
    <div id="sim9Feedback" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Earth's gravity pulls harder on the dense textbooks, creating muscular tension and fatigue!
    </div>
  </div>
</div>
<script>
function sim9Hold(holding) {
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(holding ? 'Hold' : 'Lower'));
  });

  const left = document.getElementById('sim9LeftStrain');
  const fb = document.getElementById('sim9Feedback');

  if (holding) {
    left.innerHTML = 'Muscles: Strong Fatigue & Strain! ⬇️⬇️';
    left.style.color = '#ef4444';
    fb.innerHTML = '💥 <span style="color:#f87171;">Gravity at work!</span> The left arm feels heavy strain, while the right arm holds the light pencil box effortlessly.';
  } else {
    left.innerHTML = 'Muscles: Arms Lowered & Resting 🟢';
    left.style.color = '#34d399';
    fb.innerHTML = '🟢 <span style="color:#34d399;">Resting state:</span> Zero muscular resistance needed when arms rest at your sides.';
  }
}
setTimeout(() => sim9Hold(true), 100);
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">⚖️ Two-Pan Balance Beam Equilibrium Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Weigh('melon')">Watermelon vs Apple</button>
      <button class="sim-btn" onclick="sim10Weigh('bottles')">Lunchbox vs Bottle</button>
      <button class="sim-btn" onclick="sim10Weigh('equal')">2 Apples vs Lunchbox (Equal)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <svg width="400" height="130" viewBox="0 0 400 130" style="background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); margin-bottom:12px;">
      <!-- Central stand & fulcrum -->
      <polygon points="200,50 185,115 215,115" fill="#475569" />
      <circle cx="200" cy="50" r="6" fill="#f59e0b" />

      <!-- Tilting Beam Group -->
      <g id="sim10Beam" style="transform-origin:200px 50px; transition:transform 0.5s ease;">
        <line x1="60" y1="50" x2="340" y2="50" stroke="#fbbf24" stroke-width="4" stroke-linecap="round" />
        <!-- Left Pan Strings & Pan -->
        <line x1="80" y1="50" x2="60" y2="90" stroke="#94a3b8" stroke-width="1.5" />
        <line x1="80" y1="50" x2="100" y2="90" stroke="#94a3b8" stroke-width="1.5" />
        <ellipse cx="80" cy="90" rx="30" ry="6" fill="#334155" stroke="#64748b" stroke-width="2" />
        <text id="sim10LeftText" x="80" y="82" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">🍉 Melon</text>

        <!-- Right Pan Strings & Pan -->
        <line x1="320" y1="50" x2="300" y2="90" stroke="#94a3b8" stroke-width="1.5" />
        <line x1="320" y1="50" x2="340" y2="90" stroke="#94a3b8" stroke-width="1.5" />
        <ellipse cx="320" cy="90" rx="30" ry="6" fill="#334155" stroke="#64748b" stroke-width="2" />
        <text id="sim10RightText" x="320" y="82" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">🍎 Apple</text>
      </g>
    </svg>
    <div id="sim10Verdict" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Watermelon (2,000 g) is heavier than Apple (200 g): Left pan sinks!
    </div>
  </div>
</div>
<script>
function sim10Weigh(mode) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });

  const beam = document.getElementById('sim10Beam');
  const leftT = document.getElementById('sim10LeftText');
  const rightT = document.getElementById('sim10RightText');
  const fb = document.getElementById('sim10Verdict');

  if (mode === 'melon') {
    beam.style.transform = 'rotate(-10deg)';
    leftT.textContent = '🍉 Melon';
    rightT.textContent = '🍎 Apple';
    fb.innerHTML = '🍉 <span style="color:#f87171;">Watermelon (2,000 g) &gt; Apple (200 g):</span> Left pan sinks downward!';
  } else if (mode === 'bottles') {
    beam.style.transform = 'rotate(8deg)';
    leftT.textContent = '🍱 Lunchbox';
    rightT.textContent = '🧴 Bottle';
    fb.innerHTML = '🧴 <span style="color:#38bdf8;">Water Bottle (600 g) &gt; Lunchbox (400 g):</span> Right pan sinks downward!';
  } else {
    beam.style.transform = 'rotate(0deg)';
    leftT.textContent = '🍎🍎 2 Apples';
    rightT.textContent = '🍱 Lunchbox';
    fb.innerHTML = '⚖️ <span style="color:#34d399;">PERFECT EQUILIBRIUM!</span> 2 Apples (400 g) = 1 Lunchbox (400 g). Beam is level!';
  }
}
setTimeout(() => sim10Weigh('melon'), 100);
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🪙 Non-Standard Unit Coin Weighing Balance</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11WeighItem('apple', 12)">Weigh Apple (12 Coins)</button>
      <button class="sim-btn" onclick="sim11WeighItem('eraser', 8)">Weigh Eraser (8 Coins)</button>
      <button class="sim-btn" onclick="sim11WeighItem('pencil', 3)">Weigh Pencil (3 Coins)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; max-width:550px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:16px; margin-bottom:12px;">
      <div style="flex:1; text-align:center; border-right:1px solid rgba(255,255,255,0.1); padding-right:10px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Left Pan Object</div>
        <div id="sim11ItemIcon" style="font-size:36px; margin:4px 0;">🍎</div>
        <div id="sim11ItemName" style="font-size:16px; font-weight:bold; color:#fff;">Apple</div>
      </div>
      <div style="font-size:24px; font-weight:bold; color:#fbbf24; padding:0 12px;">⚖️ =</div>
      <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.1); padding-left:10px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Right Pan (Counterweight)</div>
        <div id="sim11CoinsIcon" style="font-size:24px; margin:4px 0; color:#fbbf24;">🪙🪙🪙🪙</div>
        <div id="sim11CoinCount" style="font-size:20px; font-weight:bold; color:#38bdf8;">12 Five-Rupee Coins</div>
      </div>
    </div>
    <div id="sim11Summary" style="font-size:15px; font-weight:bold; color:#34d399; text-align:center;">
      The apple is counterbalanced by exactly 12 uniform coins!
    </div>
  </div>
</div>
<script>
function sim11WeighItem(type, coins) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(type));
  });

  const icon = type === 'apple' ? '🍎' : (type === 'eraser' ? '🧽' : '✏️');
  const name = type === 'apple' ? 'Fresh Apple' : (type === 'eraser' ? 'Chalkboard Eraser' : 'Writing Pencil');

  document.getElementById('sim11ItemIcon').innerText = icon;
  document.getElementById('sim11ItemName').innerText = name;
  document.getElementById('sim11CoinCount').innerText = coins + ' Five-Rupee Coins';

  let coinsStr = '';
  for (let i = 0; i < Math.min(8, coins); i++) coinsStr += '🪙';
  document.getElementById('sim11CoinsIcon').innerText = coinsStr + (coins > 8 ? '...' : '');

  document.getElementById('sim11Summary').innerHTML = 'Weight Measurement: <span style="color:#fbbf24;">1 ' + name + ' = ' + coins + ' Coins</span>';
}
setTimeout(() => sim11WeighItem('apple', 12), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">📊 Ascending Weight Ordering Ladder</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Step(1)">1. Sharpener vs Spoon</button>
      <button class="sim-btn" onclick="sim12Step(2)">2. Spoon vs Pencil Box</button>
      <button class="sim-btn" onclick="sim12Step(3)">3. Pencil Box vs Apple</button>
      <button class="sim-btn" onclick="sim12Step(4)">View Full Ascending Order</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim12Ladder" style="display:flex; justify-content:center; gap:10px; width:100%; max-width:580px; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim12Feedback" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Step 1: Sharpener (15 g) &lt; Spoon (45 g). Spoon sinks!
    </div>
  </div>
</div>
<script>
const sim12Items = [
  { name: 'Sharpener', icon: '🪒', weight: '15 g (Lightest)' },
  { name: 'Metal Spoon', icon: '🥄', weight: '45 g' },
  { name: 'Pencil Box', icon: '📦', weight: '120 g' },
  { name: 'Apple', icon: '🍎', weight: '200 g (Heaviest)' }
];

function sim12Step(st) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + st) || (st === 4 && b.innerText.includes('Full')));
  });

  const ladder = document.getElementById('sim12Ladder');
  ladder.innerHTML = '';
  const fb = document.getElementById('sim12Feedback');

  if (st < 4) {
    const pair = st === 1 ? [0, 1] : (st === 2 ? [1, 2] : [2, 3]);
    ladder.innerHTML = `
      <div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:10px; padding:10px 20px; text-align:center;">
        <div style="font-size:28px;">${sim12Items[pair[0]].icon}</div>
        <div style="font-size:13px; font-weight:bold; color:#fff;">${sim12Items[pair[0]].name}</div>
      </div>
      <div style="font-size:24px; font-weight:bold; color:#f87171; align-self:center;">&lt;</div>
      <div style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:10px; padding:10px 20px; text-align:center;">
        <div style="font-size:28px;">${sim12Items[pair[1]].icon}</div>
        <div style="font-size:13px; font-weight:bold; color:#fff;">${sim12Items[pair[1]].name}</div>
      </div>
    `;
    fb.innerHTML = `Comparison: <span style="color:#fbbf24;">${sim12Items[pair[0]].name} &lt; ${sim12Items[pair[1]].name}</span> (${sim12Items[pair[1]].name} tilts downward)`;
  } else {
    sim12Items.forEach((it, i) => {
      ladder.innerHTML += `
        <div style="flex:1; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:8px 4px; text-align:center;">
          <div style="font-size:10px; color:#6ee7b7; font-weight:bold;">#${i + 1}</div>
          <div style="font-size:22px;">${it.icon}</div>
          <div style="font-size:11px; font-weight:bold; color:#fff;">${it.name}</div>
        </div>
      `;
    });
    fb.innerHTML = '🎉 <span style="color:#34d399;">Ascending Order Complete:</span> Sharpener &lt; Spoon &lt; Pencil Box &lt; Apple!';
  }
}
setTimeout(() => sim12Step(1), 100);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🧂 Standard Kilogram (1 kg = 1,000 g) Reference</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Inspect('salt')">1 kg Cooking Salt</button>
      <button class="sim-btn" onclick="sim13Inspect('iron')">1 kg Iron Market Weight</button>
      <button class="sim-btn" onclick="sim13Inspect('clips')">1,000 Paperclips Equivalence</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim13Icon" style="font-size:40px; margin-bottom:6px;">🧂</div>
      <div id="sim13Title" style="font-size:18px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">1 kg Salt Packet</div>
      <div id="sim13Equation" style="font-size:26px; font-weight:bold; color:#38bdf8; margin-bottom:6px;">1 Kilogram (kg) = 1,000 Grams (g)</div>
      <div id="sim13Desc" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        A standard sealed grocery packet of cooking salt provides a reliable physical benchmark for 1 kg of mass.
      </div>
    </div>
    <div style="font-size:12px; color:#94a3b8; font-style:italic;">
      One standard kilogram ensures honest, accurate trade across food markets and science labs worldwide!
    </div>
  </div>
</div>
<script>
const sim13Data = {
  salt: { icon: '🧂', title: '1 kg Cooking Salt Packet', eq: '1 Kilogram (kg) = 1,000 Grams (g)', desc: 'Grocery salt packages provide a tangible classroom benchmark for holding 1 standard kilogram in your hand.' },
  iron: { icon: '⚖️', title: '1 kg Solid Cast-Iron Weight', eq: '1 kg Iron Weight = 1,000 g', desc: 'Vegetable merchants place heavy cast-iron 1 kg weights on pan balances to weigh potatoes and onions accurately.' },
  clips: { icon: '📎', title: '1,000 Small Paperclips', eq: '1,000 Paperclips ≈ 1,000 g = 1 kg', desc: 'A single metal paperclip weighs about 1 gram. One thousand paperclips together equal the weight of 1 full kilogram!' }
};

function sim13Inspect(key) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });
  const d = sim13Data[key];
  document.getElementById('sim13Icon').innerText = d.icon;
  document.getElementById('sim13Title').innerText = d.title;
  document.getElementById('sim13Equation').innerText = d.eq;
  document.getElementById('sim13Desc').innerText = d.desc;
}
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🎒 Everyday Kilogram Sorter & Backpack Equalizer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Item(0)">Orange</button>
      <button class="sim-btn" onclick="sim14Item(1)">School Backpack</button>
      <button class="sim-btn" onclick="sim14Item(2)">Pineapple</button>
      <button class="sim-btn" onclick="sim14Equalize()">Equalize Bags (5 kg & 3 kg)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim14Content" style="width:100%; max-width:580px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:14px; text-align:center; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim14Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; text-align:center;">
      An orange weighs about 150 grams, which is significantly less than 1 kilogram!
    </div>
  </div>
</div>
<script>
const sim14Items = [
  { name: '🍊 Juicy Fresh Orange', weight: '~150 g', cat: '< 1 kg', desc: 'An orange is a snack that fits in your hand, weighing much less than 1 kg (1,000 g).' },
  { name: '🎒 Loaded School Backpack', weight: '~4-6 kg', cat: '> 1 kg', desc: 'A school backpack filled with books and water weighs significantly more than 1 kg.' },
  { name: '🍍 Whole Pineapple', weight: '~1 kg', cat: '≈ 1 kg', desc: 'A ripe pineapple closely approximates the weight of a standard 1 kg salt packet.' }
];

function sim14Item(idx) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  const it = sim14Items[idx];
  document.getElementById('sim14Content').innerHTML = `
    <div style="font-size:18px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">${it.name} (${it.weight})</div>
    <div style="font-size:22px; font-weight:bold; color:#34d399; margin:6px 0;">Category: ${it.cat}</div>
    <div style="font-size:13px; color:#cbd5e1;">${it.desc}</div>
  `;
  document.getElementById('sim14Feedback').innerText = it.name + ' belongs to the ' + it.cat + ' group!';
}

function sim14Equalize() {
  document.querySelectorAll('#sim14 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === 3);
  });
  document.getElementById('sim14Content').innerHTML = `
    <div style="font-size:16px; font-weight:bold; color:#fbbf24; margin-bottom:6px;">Backpack Weight Equalization Puzzle:</div>
    <div style="display:flex; justify-content:space-around; align-items:center; margin:10px 0;">
      <div style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:8px; padding:10px 20px;">
        <div style="font-size:11px; color:#fca5a5;">Bag A</div>
        <div style="font-size:20px; font-weight:bold; color:#fff;">5 kg - 1 kg = 4 kg</div>
      </div>
      <div style="font-size:20px; color:#fbbf24;">➡️ Shift 1 kg ➡️</div>
      <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px 20px;">
        <div style="font-size:11px; color:#6ee7b7;">Bag B</div>
        <div style="font-size:20px; font-weight:bold; color:#fff;">3 kg + 1 kg = 4 kg</div>
      </div>
    </div>
  `;
  document.getElementById('sim14Feedback').innerHTML = '⚖️ <span style="color:#34d399;">Equalized!</span> Shifting 1 kg from Bag A to Bag B makes both bags equal at 4 kg each!';
}
setTimeout(() => sim14Item(0), 100);
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🌾 Fractional Kilogram Daal & Tea Balance</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Mode('half')">2 Daal Packs (1/2 kg each)</button>
      <button class="sim-btn" onclick="sim15Mode('quarter')">4 Tea Boxes (1/4 kg each)</button>
      <button class="sim-btn" onclick="sim15Mode('mixed')">1 Daal (500g) + 2 Tea (250g)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; max-width:580px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:14px; margin-bottom:12px;">
      <div id="sim15LeftPacks" style="flex:1; text-align:center; border-right:1px solid rgba(255,255,255,0.1); padding-right:10px;">
        <!-- Injected packs -->
      </div>
      <div style="font-size:24px; font-weight:bold; color:#34d399; padding:0 12px;">⚖️ =</div>
      <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.1); padding-left:10px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Right Pan Standard Weight</div>
        <div style="font-size:32px; margin:4px 0;">⚖️</div>
        <div style="font-size:18px; font-weight:bold; color:#fbbf24;">1 kg Iron Weight (1,000 g)</div>
      </div>
    </div>
    <div id="sim15Equation" style="font-size:16px; font-weight:bold; color:#38bdf8; text-align:center;">
      500 g + 500 g = 1,000 g = 1 kg
    </div>
  </div>
</div>
<script>
function sim15Mode(mode) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });

  const left = document.getElementById('sim15LeftPacks');
  const eq = document.getElementById('sim15Equation');

  if (mode === 'half') {
    left.innerHTML = `
      <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Left Pan Grocery Packs</div>
      <div style="font-size:26px; margin:4px 0;">🟡 🟡</div>
      <div style="font-size:15px; font-weight:bold; color:#fff;">2 Half-Kg Daal Packs</div>
      <div style="font-size:11px; color:#fbbf24;">(500 g + 500 g)</div>
    `;
    eq.innerHTML = '✨ Two Halves Make Whole: <span style="color:#fbbf24;">500 g + 500 g = 1,000 g = 1 kg</span>';
  } else if (mode === 'quarter') {
    left.innerHTML = `
      <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Left Pan Grocery Packs</div>
      <div style="font-size:24px; margin:4px 0;">🍵 🍵 🍵 🍵</div>
      <div style="font-size:15px; font-weight:bold; color:#fff;">4 Quarter-Kg Tea Boxes</div>
      <div style="font-size:11px; color:#fbbf24;">(4 × 250 g)</div>
    `;
    eq.innerHTML = '✨ Four Quarters Make Whole: <span style="color:#fbbf24;">4 × 250 g = 1,000 g = 1 kg</span>';
  } else {
    left.innerHTML = `
      <div style="font-size:12px; color:#94a3b8; font-weight:bold;">Left Pan Grocery Packs</div>
      <div style="font-size:24px; margin:4px 0;">🟡 + 🍵 🍵</div>
      <div style="font-size:15px; font-weight:bold; color:#fff;">1 Daal (500g) + 2 Tea (250g)</div>
      <div style="font-size:11px; color:#fbbf24;">(500 g + 500 g)</div>
    `;
    eq.innerHTML = '✨ Mixed Combination: <span style="color:#fbbf24;">500 g + (2 × 250 g) = 1,000 g = 1 kg</span>';
  }
}
setTimeout(() => sim15Mode('half'), 100);
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🧩 Tricky Balls Pan-Balance Logic Riddles</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16Riddle(1)">Riddle 1: Odd Heavy Ball (Scale Level)</button>
      <button class="sim-btn" onclick="sim16Riddle(2)">Riddle 1: Odd Heavy Ball (Scale Tilts)</button>
      <button class="sim-btn" onclick="sim16Riddle(3)">Riddle 2: Color Ranking (Red, Orange, Green)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim16Board" style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:600px; width:100%; text-align:center; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim16Reasoning" style="font-size:15px; font-weight:bold; color:#34d399; text-align:center;">
      Deductive logic solves balance puzzles with mathematical certainty!
    </div>
  </div>
</div>
<script>
function sim16Riddle(type) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes('' + type));
  });

  const board = document.getElementById('sim16Board');
  const rz = document.getElementById('sim16Reasoning');

  if (type === 1) {
    board.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">Weighing Ball A vs Ball B: Beam is LEVEL</div>
      <div style="display:flex; justify-content:center; gap:20px; align-items:center; margin:10px 0;">
        <div style="width:40px; height:40px; border-radius:50%; background:#38bdf8; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold;">A</div>
        <div style="font-size:24px; color:#fbbf24;">⚖️ =</div>
        <div style="width:40px; height:40px; border-radius:50%; background:#38bdf8; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold;">B</div>
        <div style="margin-left:20px; padding:6px 14px; background:rgba(239,68,68,0.2); border:2px solid #ef4444; border-radius:8px;">
          <div style="font-size:10px; color:#fca5a5;">On Table:</div>
          <div style="font-size:18px; font-weight:bold; color:#f87171;">Ball C ⭐</div>
        </div>
      </div>
    `;
    rz.innerHTML = '🎯 <span style="color:#34d399;">Deduction:</span> Since A equals B, neither is heavy. Therefore, <span style="color:#fbbf24;">Ball C</span> left on the table is the heavy one!';
  } else if (type === 2) {
    board.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">Weighing Ball A vs Ball B: LEFT Pan Sinks Down</div>
      <div style="display:flex; justify-content:center; gap:20px; align-items:center; margin:10px 0;">
        <div style="width:44px; height:44px; border-radius:50%; background:#ef4444; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; transform:translateY(6px); border:2px solid #fff;">A ⭐</div>
        <div style="font-size:24px; color:#fbbf24;">↘️ &gt;</div>
        <div style="width:36px; height:36px; border-radius:50%; background:#38bdf8; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; transform:translateY(-6px);">B</div>
        <div style="margin-left:20px; padding:6px 14px; background:rgba(255,255,255,0.05); border-radius:8px;">
          <div style="font-size:10px; color:#94a3b8;">On Table:</div>
          <div style="font-size:14px; color:#cbd5e1;">Ball C</div>
        </div>
      </div>
    `;
    rz.innerHTML = '🎯 <span style="color:#34d399;">Deduction:</span> Because the left pan sank, <span style="color:#f87171;">Ball A</span> is immediately identified as the heavy ball in just 1 weighing!';
  } else {
    board.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">Color Weight Transitivity: Red &gt; Orange and Orange &gt; Green</div>
      <div style="display:flex; justify-content:center; gap:16px; align-items:center; margin:10px 0;">
        <div style="padding:6px 12px; background:rgba(34,197,94,0.2); border:1px solid #22c55e; border-radius:8px; font-weight:bold; color:#4ade80;">Green (Lightest)</div>
        <div style="color:#fbbf24; font-weight:bold;">&lt;</div>
        <div style="padding:6px 12px; background:rgba(249,115,22,0.2); border:1px solid #f97316; border-radius:8px; font-weight:bold; color:#fb923c;">Orange</div>
        <div style="color:#fbbf24; font-weight:bold;">&lt;</div>
        <div style="padding:6px 12px; background:rgba(239,68,68,0.2); border:1px solid #ef4444; border-radius:8px; font-weight:bold; color:#f87171;">Red (Heaviest)</div>
      </div>
    `;
    rz.innerHTML = '🎯 <span style="color:#34d399;">Complete Order:</span> Green &lt; Orange &lt; Red (Lightest to Heaviest)!';
  }
}
setTimeout(() => sim16Riddle(1), 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Slides 9-16.")
    for k in sorted(sims_part2.keys()):
        print(f"  Slide {k}: {len(sims_part2[k])} chars")

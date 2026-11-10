#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🥤 Sugarcane Juice Stall Glass Capacity Comparator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Select('small')">6 Small Glasses (100 mL)</button>
      <button class="sim-btn" onclick="sim1Select('medium')">3 Medium Glasses (200 mL)</button>
      <button class="sim-btn" onclick="sim1Select('large')">2 Large Tumblers (300 mL)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#cbd5e1; font-weight:bold; margin-bottom:8px;">
      Total Juice Volume Challenge: <span style="color:#fbbf24; font-size:16px;">600 mL</span>
    </div>
    <!-- Visual container display -->
    <div id="sim1GlassesWrap" style="display:flex; justify-content:center; align-items:flex-end; gap:12px; width:100%; max-width:550px; height:100px; margin-bottom:12px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:10px;">
      <!-- Injected glasses -->
    </div>
    <div id="sim1Feedback" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      6 × 100 mL = 600 mL (More glasses, smaller capacity each)
    </div>
  </div>
</div>
<script>
function sim1Select(mode) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });

  const wrap = document.getElementById('sim1GlassesWrap');
  wrap.innerHTML = '';
  const fb = document.getElementById('sim1Feedback');

  if (mode === 'small') {
    for (let i = 0; i < 6; i++) {
      wrap.innerHTML += '<div style=\"width:32px; height:50px; background:#f59e0b; border:2px solid #fbbf24; border-radius:4px 4px 6px 6px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px; font-weight:bold;\">100</div>';
    }
    fb.innerHTML = '✨ 6 Small Glasses: <span style=\"color:#fbbf24;\">6 × 100 mL = 600 mL</span> (Fewer mL per glass, higher glass count!)';
  } else if (mode === 'medium') {
    for (let i = 0; i < 3; i++) {
      wrap.innerHTML += '<div style=\"width:50px; height:70px; background:#f59e0b; border:2px solid #fbbf24; border-radius:6px 6px 8px 8px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:12px; font-weight:bold;\">200</div>';
    }
    fb.innerHTML = '✨ 3 Medium Glasses: <span style=\"color:#38bdf8;\">3 × 200 mL = 600 mL</span> (Balanced glass size and count!)';
  } else {
    for (let i = 0; i < 2; i++) {
      wrap.innerHTML += '<div style=\"width:68px; height:85px; background:#f59e0b; border:2px solid #fbbf24; border-radius:8px 8px 10px 10px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:14px; font-weight:bold;\">300</div>';
    }
    fb.innerHTML = '✨ 2 Large Tumblers: <span style=\"color:#34d399;\">2 × 300 mL = 600 mL</span> (Fewer glasses, larger capacity each!)';
  }
}
setTimeout(() => sim1Select('small'), 100);
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">🧪 Equalizing Container Pouring Test</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2ShowOriginal()">View Original Glasses (Deceptive)</button>
      <button class="sim-btn" onclick="sim2PourEqual()">Pour into Identical Jars (Truthful)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim2Stage" style="display:flex; justify-content:space-around; align-items:flex-end; width:100%; max-width:550px; height:120px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:10px 20px; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim2Verdict" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Glass shapes deceive our eyes! Click 'Pour into Identical Jars' to reveal the true volume.
    </div>
  </div>
</div>
<script>
function sim2ShowOriginal() {
  document.querySelectorAll('#sim2 .sim-controls button')[0].classList.add('active');
  document.querySelectorAll('#sim2 .sim-controls button')[1].classList.remove('active');

  const stage = document.getElementById('sim2Stage');
  stage.innerHTML = `
    <div style="text-align:center;">
      <div style="width:30px; height:90px; background:linear-gradient(180deg, transparent 20%, #38bdf8 20%); border:2px solid #fff; border-radius:4px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Glass A (Tall/Thin)</div>
    </div>
    <div style="text-align:center;">
      <div style="width:70px; height:50px; background:linear-gradient(180deg, transparent 15%, #38bdf8 15%); border:2px solid #fff; border-radius:6px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Glass B (Short/Wide)</div>
    </div>
    <div style="text-align:center;">
      <div style="width:50px; height:65px; background:linear-gradient(180deg, transparent 40%, #38bdf8 40%); border:2px solid #fff; border-radius:6px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Glass C (Medium)</div>
    </div>
  `;
  document.getElementById('sim2Verdict').innerHTML = 'Glass A looks tallest, but Glass B has a much wider base! Who has the most?';
}

function sim2PourEqual() {
  document.querySelectorAll('#sim2 .sim-controls button')[0].classList.remove('active');
  document.querySelectorAll('#sim2 .sim-controls button')[1].classList.add('active');

  const stage = document.getElementById('sim2Stage');
  stage.innerHTML = `
    <div style="text-align:center;">
      <div style="width:50px; height:80px; background:linear-gradient(180deg, transparent 50%, #10b981 50%); border:2px solid #34d399; border-radius:4px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Jar A: 200 mL</div>
    </div>
    <div style="text-align:center;">
      <div style="width:50px; height:80px; background:linear-gradient(180deg, transparent 20%, #10b981 20%); border:2px solid #34d399; border-radius:4px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Jar B: 350 mL (Most!)</div>
    </div>
    <div style="text-align:center;">
      <div style="width:50px; height:80px; background:linear-gradient(180deg, transparent 65%, #10b981 65%); border:2px solid #34d399; border-radius:4px; margin:0 auto;"></div>
      <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Jar C: 150 mL (Least)</div>
    </div>
  `;
  document.getElementById('sim2Verdict').innerHTML = '🎉 <span style="color:#34d399;">Truth Revealed!</span> Glass B had the MOST milk (350 mL), while Glass C had the LEAST (150 mL)!';
}
setTimeout(() => sim2ShowOriginal(), 100);
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🥣 Vessel Filling Ratio & Capacity Estimator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3SetVessel('glass')">Fill Glass (3 Bowls)</button>
      <button class="sim-btn" onclick="sim3SetVessel('bottle')">Fill Bottle (4 Glasses)</button>
      <button class="sim-btn" onclick="sim3SetVessel('bucket')">Fill Bucket (5 Bottles)</button>
      <button class="sim-btn" onclick="sim3AddUnit()">Pour 1 Unit (+)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:120px; height:120px; background:rgba(0,0,0,0.3); border:3px solid #38bdf8; border-radius:10px; overflow:hidden; margin-bottom:12px; display:flex; align-items:flex-end;">
      <div id="sim3Liquid" style="width:100%; height:0%; background:linear-gradient(180deg, #38bdf8, #0284c7); transition:height 0.4s ease;"></div>
      <div id="sim3WaterLevelText" style="position:absolute; width:100%; text-align:center; top:45%; font-size:14px; font-weight:bold; color:#fff; text-shadow:0 1px 3px rgba(0,0,0,0.8);">0 / 3 Bowls</div>
    </div>
    <div id="sim3Status" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Click 'Pour 1 Unit (+)' to fill the vessel step-by-step!
    </div>
  </div>
</div>
<script>
let sim3CurVessel = 'glass';
let sim3Count = 0;
const sim3Data = {
  glass: { max: 3, unit: 'Bowls', name: 'Drinking Glass' },
  bottle: { max: 4, unit: 'Glasses', name: 'Water Bottle' },
  bucket: { max: 5, unit: 'Bottles', name: 'Washing Bucket' }
};

function sim3SetVessel(type) {
  sim3CurVessel = type;
  sim3Count = 0;
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(type));
  });
  sim3Update();
}

function sim3AddUnit() {
  const d = sim3Data[sim3CurVessel];
  if (sim3Count < d.max) {
    sim3Count++;
    sim3Update();
  }
}

function sim3Update() {
  const d = sim3Data[sim3CurVessel];
  const pct = Math.round((sim3Count / d.max) * 100);
  document.getElementById('sim3Liquid').style.height = pct + '%';
  document.getElementById('sim3WaterLevelText').innerText = sim3Count + ' / ' + d.max + ' ' + d.unit;

  const st = document.getElementById('sim3Status');
  if (sim3Count === d.max) {
    st.innerHTML = '🎉 <span style="color:#34d399;">Vessel Completely Full!</span> Exactly ' + d.max + ' ' + d.unit + ' fill 1 ' + d.name + '!';
  } else {
    st.innerHTML = 'Filled: ' + sim3Count + ' ' + d.unit + ' poured into ' + d.name + ' (' + (d.max - sim3Count) + ' more needed)';
  }
}
setTimeout(() => sim3SetVessel('glass'), 100);
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">🍋 Lemonade Stall Utensil Calculator</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim4Mod(-1)">- 1 Glass</button>
      <button class="sim-btn active" id="sim4CountBtn">Serve 4 Glasses</button>
      <button class="sim-btn" onclick="sim4Mod(1)">+ 1 Glass</button>
      <button class="sim-btn" onclick="sim4Preset(10)">Full Jug (10 Glasses)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-around; gap:16px; width:100%; max-width:580px; margin-bottom:12px;">
      <div style="flex:1; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; color:#fbbf24; font-weight:bold;">Customer Glasses</div>
        <div id="sim4GlassesDisplay" style="font-size:32px; font-weight:bold; color:#fff; margin-top:4px;">4</div>
      </div>
      <div style="flex:1; background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; color:#60a5fa; font-weight:bold;">Ladles Needed (×3)</div>
        <div id="sim4LadlesDisplay" style="font-size:32px; font-weight:bold; color:#fff; margin-top:4px;">12</div>
      </div>
      <div style="flex:1; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; color:#34d399; font-weight:bold;">Jugs Required (÷10)</div>
        <div id="sim4JugsDisplay" style="font-size:26px; font-weight:bold; color:#fff; margin-top:8px;">1 Jug</div>
      </div>
    </div>
    <div id="sim4Formula" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Rule: 1 Glass = 3 Ladles | 1 Jug = 10 Glasses (4 × 3 = 12 ladles)
    </div>
  </div>
</div>
<script>
let sim4Glasses = 4;
function sim4Mod(delta) {
  sim4Glasses = Math.max(1, Math.min(30, sim4Glasses + delta));
  sim4Render();
}

function sim4Preset(val) {
  sim4Glasses = val;
  sim4Render();
}

function sim4Render() {
  document.getElementById('sim4CountBtn').innerText = 'Serve ' + sim4Glasses + ' Glasses';
  document.getElementById('sim4GlassesDisplay').innerText = sim4Glasses;
  const ladles = sim4Glasses * 3;
  document.getElementById('sim4LadlesDisplay').innerText = ladles;
  const jugs = Math.ceil(sim4Glasses / 10);
  document.getElementById('sim4JugsDisplay').innerText = jugs + (jugs === 1 ? ' Jug' : ' Jugs');

  document.getElementById('sim4Formula').innerHTML = `Formula: <span style="color:#fbbf24;">${sim4Glasses} Glasses × 3 = ${ladles} Ladles</span> (${jugs} Jug needed)`;
}
setTimeout(() => sim4Render(), 100);
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🥛 Standard Litre (1 L = 1,000 mL) Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5Inspect('bottle')">1-Litre Bottle</button>
      <button class="sim-btn" onclick="sim5Inspect('milkCan')">Milkman 1 L Measure Can</button>
      <button class="sim-btn" onclick="sim5Inspect('oilPouch')">1-Litre Cooking Oil Pouch</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim5Icon" style="font-size:36px; margin-bottom:6px;">🍾</div>
      <div id="sim5Title" style="font-size:18px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">1-Litre Water Bottle</div>
      <div id="sim5Metric" style="font-size:26px; font-weight:bold; color:#38bdf8; margin-bottom:6px;">1 Litre (L) = 1,000 Millilitres (mL)</div>
      <div id="sim5Desc" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        Standard 1-litre drinking water bottles are sold in shops worldwide. They hold exactly 1,000 mL of pure liquid.
      </div>
    </div>
    <div style="font-size:12px; color:#94a3b8; font-style:italic;">
      Standard litre units ensure fair, trusted commerce across towns, dairies, and international trade!
    </div>
  </div>
</div>
<script>
const sim5Data = {
  bottle: { icon: '🍾', title: '1-Litre Drinking Water Bottle', desc: 'Standard water bottles found in stores hold exactly 1 litre (1,000 mL) of drinking water.' },
  milkCan: { icon: '🥛', title: 'Milkman 1-Litre Metal Can', desc: 'Every morning, dairy milkmen use standardized cylindrical metal measures holding exactly 1 litre.' },
  oilPouch: { icon: '🌻', title: '1-Litre Cooking Oil Pouch', desc: 'Sealed cooking oil packages are filled to 1 standard litre to ensure fair trade in kitchens.' }
};

function sim5Inspect(key) {
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });
  const it = sim5Data[key];
  document.getElementById('sim5Icon').innerText = it.icon;
  document.getElementById('sim5Title').innerText = it.title;
  document.getElementById('sim5Desc').innerText = it.desc;
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🍶 Household Container 1-Litre Sorter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Pick(0)">Teacup</button>
      <button class="sim-btn" onclick="sim6Pick(1)">Bathing Bucket</button>
      <button class="sim-btn" onclick="sim6Pick(2)">Thermal Flask</button>
      <button class="sim-btn" onclick="sim6Pick(3)">Eye Dropper</button>
      <button class="sim-btn" onclick="sim6Pick(4)">Watering Can</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim6Prompt" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 20px; text-align:center;">
      Container: ☕ Porcelain Teacup (~180 mL)
    </div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; width:100%; max-width:600px; margin-bottom:12px;">
      <button class="sim-btn" id="sim6Bin0" onclick="sim6Guess(0)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#60a5fa;">&lt; 1 Litre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Less than 1,000 mL</div>
      </button>
      <button class="sim-btn" id="sim6Bin1" onclick="sim6Guess(1)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#34d399;">≈ 1 Litre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Around 1,000 mL</div>
      </button>
      <button class="sim-btn" id="sim6Bin2" onclick="sim6Guess(2)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#f59e0b;">&gt; 1 Litre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">More than 1,000 mL</div>
      </button>
    </div>
    <div id="sim6Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; text-align:center;">
      Click a category bin above to classify this vessel!
    </div>
  </div>
</div>
<script>
let sim6Cur = 0;
const sim6Items = [
  { name: '☕ Porcelain Teacup', size: '~180 mL', bin: 0, reason: 'A teacup holds small sips, far less than 1 full litre (1,000 mL)!' },
  { name: '🪣 Bathroom Bathing Bucket', size: '~15-20 Litres', bin: 2, reason: 'A bathing bucket holds many litres of water for bathing or mopping floors!' },
  { name: '🧴 Personal Thermal Flask', size: '~1 Litre', bin: 1, reason: 'A standard personal thermal flask holds approximately 1 litre of warm water!' },
  { name: '💧 Medicine Eye Dropper', size: '~2 mL', bin: 0, reason: 'An eye dropper holds only tiny droplets, measuring far less than 1 litre!' },
  { name: '🪴 Garden Watering Can', size: '~5 Litres', bin: 2, reason: 'A garden watering can carries several litres to hydrate outdoor plants!' }
];

function sim6Pick(idx) {
  sim6Cur = idx;
  document.querySelectorAll('#sim6 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  const it = sim6Items[idx];
  document.getElementById('sim6Prompt').innerText = 'Container: ' + it.name + ' (' + it.size + ')';
  document.getElementById('sim6Feedback').innerText = 'Click a category bin above to classify this vessel!';
  document.querySelectorAll('#sim6 [id^=sim6Bin]').forEach(b => {
    b.style.borderColor = '';
    b.style.background = '';
  });
}

function sim6Guess(binIdx) {
  const it = sim6Items[sim6Cur];
  const fb = document.getElementById('sim6Feedback');
  const btn = document.getElementById('sim6Bin' + binIdx);

  if (binIdx === it.bin) {
    btn.style.borderColor = '#10b981';
    btn.style.background = 'rgba(16,185,129,0.2)';
    fb.innerHTML = '🎉 <span style="color:#34d399;">Correct!</span> ' + it.reason;
  } else {
    btn.style.borderColor = '#ef4444';
    btn.style.background = 'rgba(239,68,68,0.2)';
    fb.innerHTML = '❌ <span style="color:#f87171;">Try again!</span> Think about whether ' + it.size + ' is smaller, around, or larger than 1,000 mL.';
  }
}
setTimeout(() => sim6Pick(0), 100);
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🥛 Half-Litre (1/2 L = 500 mL) Explorer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7SetState('split')">Split into 2 Half-Litres</button>
      <button class="sim-btn" onclick="sim7SetState('combine')">Combine to 1 Whole Litre</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim7Display" style="display:flex; justify-content:center; align-items:flex-end; gap:20px; width:100%; max-width:550px; height:120px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:10px; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim7Equation" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 24px; text-align:center;">
      1/2 Litre + 1/2 Litre = 1 Whole Litre (500 mL + 500 mL = 1,000 mL)
    </div>
  </div>
</div>
<script>
function sim7SetState(state) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(state));
  });

  const disp = document.getElementById('sim7Display');
  const eq = document.getElementById('sim7Equation');

  if (state === 'split') {
    disp.innerHTML = `
      <div style="text-align:center;">
        <div style="width:65px; height:70px; background:linear-gradient(180deg, #38bdf8, #0284c7); border:2px solid #fff; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">500 mL</div>
        <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">1/2 Litre Mug A</div>
      </div>
      <div style="font-size:24px; font-weight:bold; color:#fbbf24; padding-bottom:30px;">+</div>
      <div style="text-align:center;">
        <div style="width:65px; height:70px; background:linear-gradient(180deg, #38bdf8, #0284c7); border:2px solid #fff; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">500 mL</div>
        <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">1/2 Litre Mug B</div>
      </div>
    `;
    eq.innerHTML = 'Split State: <span style="color:#38bdf8;">Two Half-Litres</span> (500 mL + 500 mL = 1,000 mL = 1 L)';
  } else {
    disp.innerHTML = `
      <div style="text-align:center;">
        <div style="width:90px; height:100px; background:linear-gradient(180deg, #10b981, #047857); border:2px solid #34d399; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:bold; color:#fff;">1,000 mL</div>
        <div style="font-size:11px; color:#cbd5e1; font-weight:bold; margin-top:4px;">1 Whole Litre Vessel</div>
      </div>
    `;
    eq.innerHTML = 'Combined State: <span style="color:#34d399;">1 Complete Litre = 1,000 mL</span>';
  }
}
setTimeout(() => sim7SetState('split'), 100);
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🍹 Quarter-Litre (1/4 L = 250 mL) Partitioning</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Select(1)">1 Glass (250 mL)</button>
      <button class="sim-btn" onclick="sim8Select(2)">2 Glasses (500 mL)</button>
      <button class="sim-btn" onclick="sim8Select(3)">3 Glasses (750 mL)</button>
      <button class="sim-btn" onclick="sim8Select(4)">4 Glasses (1,000 mL)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim8Glasses" style="display:flex; justify-content:center; gap:12px; width:100%; max-width:550px; margin-bottom:12px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim8Readout" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 24px; text-align:center;">
      Active: 1/4 Litre = 250 mL
    </div>
  </div>
</div>
<script>
function sim8Select(count) {
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + count));
  });

  const container = document.getElementById('sim8Glasses');
  container.innerHTML = '';
  const labels = ['1/4 Litre (250 mL)', '2/4 = 1/2 Litre (500 mL)', '3/4 Litre (750 mL)', '4/4 = 1 Whole Litre (1,000 mL)'];

  for (let i = 1; i <= 4; i++) {
    const active = i <= count;
    container.innerHTML += `
      <div style="flex:1; max-width:90px; text-align:center;">
        <div style="height:70px; background:${active ? 'linear-gradient(180deg, #38bdf8, #0284c7)' : 'rgba(255,255,255,0.1)'}; border:2px solid ${active ? '#fff' : '#64748b'}; border-radius:4px 4px 6px 6px; display:flex; align-items:center; justify-content:center; color:${active ? '#fff' : '#94a3b8'}; font-size:11px; font-weight:bold;">
          250 mL
        </div>
        <div style="font-size:10px; color:#cbd5e1; font-weight:bold; margin-top:4px;">Glass #${i}</div>
      </div>
    `;
  }

  document.getElementById('sim8Readout').innerHTML = 'Selected: <span style="color:#fbbf24;">' + labels[count - 1] + '</span>';
}
setTimeout(() => sim8Select(1), 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Slides 1-8.")
    for k in sorted(sims_part1.keys()):
        print(f"  Slide {k}: {len(sims_part1[k])} chars")

#!/usr/bin/env python3
"""NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting Simulators"""

simulators = {
    1: '''
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
      wrap.innerHTML += '<div style="width:32px; height:50px; background:#f59e0b; border:2px solid #fbbf24; border-radius:4px 4px 6px 6px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px; font-weight:bold;">100</div>';
    }
    fb.innerHTML = '✨ 6 Small Glasses: <span style="color:#fbbf24;">6 × 100 mL = 600 mL</span> (Fewer mL per glass, higher glass count!)';
  } else if (mode === 'medium') {
    for (let i = 0; i < 3; i++) {
      wrap.innerHTML += '<div style="width:50px; height:70px; background:#f59e0b; border:2px solid #fbbf24; border-radius:6px 6px 8px 8px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:12px; font-weight:bold;">200</div>';
    }
    fb.innerHTML = '✨ 3 Medium Glasses: <span style="color:#38bdf8;">3 × 200 mL = 600 mL</span> (Balanced glass size and count!)';
  } else {
    for (let i = 0; i < 2; i++) {
      wrap.innerHTML += '<div style="width:68px; height:85px; background:#f59e0b; border:2px solid #fbbf24; border-radius:8px 8px 10px 10px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:14px; font-weight:bold;">300</div>';
    }
    fb.innerHTML = '✨ 2 Large Tumblers: <span style="color:#34d399;">2 × 300 mL = 600 mL</span> (Fewer glasses, larger capacity each!)';
  }
}
setTimeout(() => sim1Select('small'), 100);
</script>
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}

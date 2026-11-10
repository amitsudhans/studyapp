#!/usr/bin/env python3
"""NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan Simulators"""

simulators = {
    1: '''
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🌸 Festival Courtyard Item Counter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Filter('all')">All Items</button>
      <button class="sim-btn" onclick="sim1Filter('leaves')">🍃 Mango Leaves (Pairs of 2)</button>
      <button class="sim-btn" onclick="sim1Filter('glasses')">🥛 Glasses (Rows of 3)</button>
      <button class="sim-btn" onclick="sim1Filter('poms')">🍎 Pomegranates (Baskets of 4)</button>
      <button class="sim-btn" onclick="sim1Filter('flowers')">🌼 Marigolds (Garlands of 5)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim1Display" style="display:flex; flex-wrap:wrap; justify-content:center; gap:16px; width:100%; max-width:650px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim1Equation" style="margin-top:16px; font-size:18px; font-weight:bold; color:#f59e0b; background:rgba(0,0,0,0.3); padding:8px 20px; border-radius:20px; border:1px solid rgba(245,158,11,0.4);">
      Equal Grouping Formula: 4 groups of 5 = 20 items
    </div>
  </div>
</div>
<script>
function sim1Filter(type) {
  const btnGroup = document.querySelectorAll('#sim1 .sim-controls .sim-btn');
  btnGroup.forEach(b => b.classList.remove('active'));
  if (event && event.target) event.target.classList.add('active');

  const container = document.getElementById('sim1Display');
  const eq = document.getElementById('sim1Equation');
  container.innerHTML = '';

  if (type === 'leaves' || type === 'all') {
    let html = '<div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:10px 14px; text-align:center;">';
    html += '<div style="font-size:12px; font-weight:bold; color:#10b981; margin-bottom:6px;">🍃 Mango Leaves: 5 Pairs of 2</div><div style="display:flex; gap:8px;">';
    for (let g = 0; g < 5; g++) {
      html += '<div style="background:rgba(16,185,129,0.3); border-radius:8px; padding:6px 8px; font-size:20px;" title="Pair ' + (g+1) + '">🍃🍃</div>';
    }
    html += '</div><div style="margin-top:6px; font-size:13px; color:#a7f3d0; font-weight:bold;">5 × 2 = 10 Leaves</div></div>';
    container.innerHTML += html;
  }

  if (type === 'glasses' || type === 'all') {
    let html = '<div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:10px 14px; text-align:center;">';
    html += '<div style="font-size:12px; font-weight:bold; color:#60a5fa; margin-bottom:6px;">🥛 Drinking Glasses: 3 Rows of 3</div><div style="display:flex; gap:8px;">';
    for (let g = 0; g < 3; g++) {
      html += '<div style="background:rgba(59,130,246,0.3); border-radius:8px; padding:6px 8px; font-size:20px;" title="Row ' + (g+1) + '">🥛🥛🥛</div>';
    }
    html += '</div><div style="margin-top:6px; font-size:13px; color:#bfdbfe; font-weight:bold;">3 × 3 = 9 Glasses</div></div>';
    container.innerHTML += html;
  }

  if (type === 'poms' || type === 'all') {
    let html = '<div style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:12px; padding:10px 14px; text-align:center;">';
    html += '<div style="font-size:12px; font-weight:bold; color:#f87171; margin-bottom:6px;">🍎 Pomegranates: 3 Baskets of 4</div><div style="display:flex; gap:8px;">';
    for (let g = 0; g < 3; g++) {
      html += '<div style="background:rgba(239,68,68,0.3); border-radius:8px; padding:6px 8px; font-size:20px;" title="Basket ' + (g+1) + '">🍎🍎🍎🍎</div>';
    }
    html += '</div><div style="margin-top:6px; font-size:13px; color:#fecaca; font-weight:bold;">3 × 4 = 12 Fruits</div></div>';
    container.innerHTML += html;
  }

  if (type === 'flowers' || type === 'all') {
    let html = '<div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:10px 14px; text-align:center;">';
    html += '<div style="font-size:12px; font-weight:bold; color:#fbbf24; margin-bottom:6px;">🌼 Marigold Garlands: 4 Garlands of 5</div><div style="display:flex; gap:8px;">';
    for (let g = 0; g < 4; g++) {
      html += '<div style="background:rgba(245,158,11,0.3); border-radius:8px; padding:6px 8px; font-size:20px;" title="Garland ' + (g+1) + '">🌼🌼🌼🌼🌼</div>';
    }
    html += '</div><div style="margin-top:6px; font-size:13px; color:#fef3c7; font-weight:bold;">4 × 5 = 20 Flowers</div></div>';
    container.innerHTML += html;
  }

  if (type === 'leaves') eq.innerText = "🍃 5 Pairs of Leaves = 5 × 2 = 10 Mango Leaves";
  else if (type === 'glasses') eq.innerText = "🥛 3 Rows of Glasses = 3 × 3 = 9 Glasses";
  else if (type === 'poms') eq.innerText = "🍎 3 Baskets of Pomegranates = 3 × 4 = 12 Fruits";
  else if (type === 'flowers') eq.innerText = "🌼 4 Garlands of Marigolds = 4 × 5 = 20 Flowers";
  else eq.innerText = "Festive Decor Groups: Fast counting via equal grouping (Multiplication)!";
}
setTimeout(() => sim1Filter('all'), 100);
</script>
''',
    2: '''
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">🎀 Craft Material Scaling Workbench</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1; font-weight:600;">Wristbands to craft:</span>
      <button class="sim-btn" onclick="sim2Adjust(-1)">➖ Less</button>
      <span id="sim2Count" style="font-size:16px; font-weight:bold; color:#f59e0b; min-width:24px; text-align:center;">5</span>
      <button class="sim-btn" onclick="sim2Adjust(1)">➕ More</button>
      <button class="sim-btn" onclick="sim2Set(10)">Preset 10</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:14px; width:100%; max-width:680px; margin-bottom:14px;">
      <div style="flex:1; min-width:140px; background:rgba(236,72,153,0.15); border:1px solid #ec4899; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:24px;">🌸</div>
        <div style="font-size:13px; font-weight:bold; color:#f472b6;">Central Flowers</div>
        <div style="font-size:11px; color:#fbcfe8;">1 per wristband</div>
        <div id="sim2Flowers" style="font-size:20px; font-weight:bold; color:#fff; margin-top:6px;">5 × 1 = 5</div>
      </div>
      <div style="flex:1; min-width:140px; background:rgba(99,102,241,0.15); border:1px solid #6366f1; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:24px;">🧵</div>
        <div style="font-size:13px; font-weight:bold; color:#818cf8;">Satin Threads</div>
        <div style="font-size:11px; color:#c7d2fe;">2 per wristband</div>
        <div id="sim2Threads" style="font-size:20px; font-weight:bold; color:#fff; margin-top:6px;">5 × 2 = 10</div>
      </div>
      <div style="flex:1; min-width:140px; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:24px;">✨</div>
        <div style="font-size:13px; font-weight:bold; color:#fbbf24;">Golden Beads</div>
        <div style="font-size:11px; color:#fef3c7;">4 per wristband</div>
        <div id="sim2Beads" style="font-size:20px; font-weight:bold; color:#fff; margin-top:6px;">5 × 4 = 20</div>
      </div>
      <div style="flex:1; min-width:140px; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:24px;">📦</div>
        <div style="font-size:13px; font-weight:bold; color:#34d399;">Total Materials</div>
        <div style="font-size:11px; color:#a7f3d0;">7 items per wristband</div>
        <div id="sim2Total" style="font-size:20px; font-weight:bold; color:#fff; margin-top:6px;">5 × 7 = 35</div>
      </div>
    </div>
    <div id="sim2Preview" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px; max-width:650px;">
      <!-- Wristband preview chips -->
    </div>
  </div>
</div>
<script>
let sim2Val = 5;
function sim2Adjust(delta) {
  sim2Val = Math.max(1, Math.min(10, sim2Val + delta));
  sim2Render();
}
function sim2Set(val) {
  sim2Val = val;
  sim2Render();
}
function sim2Render() {
  document.getElementById('sim2Count').innerText = sim2Val;
  document.getElementById('sim2Flowers').innerText = sim2Val + ' × 1 = ' + (sim2Val * 1);
  document.getElementById('sim2Threads').innerText = sim2Val + ' × 2 = ' + (sim2Val * 2);
  document.getElementById('sim2Beads').innerText = sim2Val + ' × 4 = ' + (sim2Val * 4);
  document.getElementById('sim2Total').innerText = sim2Val + ' × 7 = ' + (sim2Val * 7);

  const prev = document.getElementById('sim2Preview');
  prev.innerHTML = '';
  for (let i = 0; i < sim2Val; i++) {
    prev.innerHTML += '<div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.2); border-radius:16px; padding:6px 12px; display:flex; align-items:center; gap:6px; font-size:13px; font-weight:600; color:#cbd5e1;"><span style="color:#f472b6;">🌸1</span><span style="color:#818cf8;">🧵2</span><span style="color:#fbbf24;">✨4</span><span style="color:#64748b; font-size:10px;">(# ' + (i+1) + ')</span></div>';
  }
}
setTimeout(sim2Render, 100);
</script>
''',
    3: '''
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🔄 Repeated Addition to Multiplication Converter</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Group Size:</span>
      <button class="sim-btn" onclick="sim3SetSize(2)">2s</button>
      <button class="sim-btn" onclick="sim3SetSize(3)">3s</button>
      <button class="sim-btn active" onclick="sim3SetSize(4)">4s</button>
      <button class="sim-btn" onclick="sim3SetSize(5)">5s</button>
      <span style="margin-left:8px; font-size:13px; color:#cbd5e1;">Groups:</span>
      <button class="sim-btn" onclick="sim3SetCount(3)">3</button>
      <button class="sim-btn" onclick="sim3SetCount(4)">4</button>
      <button class="sim-btn active" onclick="sim3SetCount(5)">5</button>
      <button class="sim-btn" onclick="sim3SetCount(6)">6</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim3Boxes" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-bottom:18px;">
      <!-- Rendered groups -->
    </div>
    <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(255,255,255,0.15); border-radius:14px; padding:12px 24px; text-align:center; max-width:600px; width:100%;">
      <div id="sim3AddChain" style="font-size:16px; color:#94a3b8; font-weight:600; margin-bottom:6px;">4 + 4 + 4 + 4 + 4 = 20</div>
      <div id="sim3MultEq" style="font-size:22px; color:#38bdf8; font-weight:bold;">5 groups of 4  ➔  5 × 4 = 20</div>
    </div>
  </div>
</div>
<script>
let sim3Size = 4;
let sim3Count = 5;

function sim3SetSize(sz) {
  sim3Size = sz;
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    if (b.innerText === sz + 's') b.classList.add('active');
    else if (b.innerText.endsWith('s')) b.classList.remove('active');
  });
  sim3Render();
}

function sim3SetCount(cnt) {
  sim3Count = cnt;
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    if (b.innerText === '' + cnt) b.classList.add('active');
    else if (!b.innerText.endsWith('s')) b.classList.remove('active');
  });
  sim3Render();
}

function sim3Render() {
  const container = document.getElementById('sim3Boxes');
  container.innerHTML = '';
  const total = sim3Size * sim3Count;

  for (let i = 0; i < sim3Count; i++) {
    let box = '<div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; border-radius:10px; padding:8px 12px; text-align:center;">';
    box += '<div style="font-size:11px; font-weight:bold; color:#7dd3fc; margin-bottom:4px;">Group ' + (i+1) + '</div>';
    box += '<div style="display:flex; gap:4px; justify-content:center;">';
    for (let j = 0; j < sim3Size; j++) {
      box += '<div style="width:16px; height:16px; background:#f59e0b; border-radius:50%; box-shadow:0 0 6px rgba(245,158,11,0.6);"></div>';
    }
    box += '</div><div style="font-size:12px; color:#cbd5e1; margin-top:4px; font-weight:600;">' + sim3Size + '</div></div>';
    container.innerHTML += box;
  }

  const addTerms = Array(sim3Count).fill(sim3Size).join(' + ');
  document.getElementById('sim3AddChain').innerText = addTerms + ' = ' + total;
  document.getElementById('sim3MultEq').innerHTML = sim3Count + ' groups of ' + sim3Size + ' &nbsp;➔&nbsp; <span style="color:#f59e0b;">' + sim3Count + ' × ' + sim3Size + ' = ' + total + '</span>';
}
setTimeout(sim3Render, 100);
</script>
''',
    4: '''
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">⚖️ Forward Scaling & Reverse Bead Division Solver</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4Mode('forward')">Forward: Scale Wristbands</button>
      <button class="sim-btn" onclick="sim4Mode('reverse')">Reverse: Bead Division</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim4ForwardPanel" style="width:100%; max-width:600px; text-align:center;">
      <div style="margin-bottom:12px; display:flex; justify-content:center; align-items:center; gap:12px;">
        <span style="font-weight:600; color:#cbd5e1;">Target Wristbands:</span>
        <input type="range" id="sim4Range" min="1" max="12" value="6" oninput="sim4UpdateForward(this.value)" style="width:200px;">
        <span id="sim4FwdVal" style="font-size:18px; font-weight:bold; color:#f59e0b; min-width:30px;">6</span>
      </div>
      <div style="display:flex; justify-content:space-around; background:rgba(0,0,0,0.3); border-radius:12px; padding:14px; border:1px solid rgba(255,255,255,0.1);">
        <div><div style="color:#f472b6; font-size:12px; font-weight:bold;">🌸 Flowers (×1)</div><div id="sim4FwdFlw" style="font-size:22px; font-weight:bold; color:#fff;">6</div></div>
        <div><div style="color:#818cf8; font-size:12px; font-weight:bold;">🧵 Threads (×2)</div><div id="sim4FwdThr" style="font-size:22px; font-weight:bold; color:#fff;">12</div></div>
        <div><div style="color:#fbbf24; font-size:12px; font-weight:bold;">✨ Beads (×4)</div><div id="sim4FwdBd" style="font-size:22px; font-weight:bold; color:#fff;">24</div></div>
      </div>
    </div>
    <div id="sim4ReversePanel" style="width:100%; max-width:600px; text-align:center; display:none;">
      <div style="margin-bottom:12px; font-size:14px; color:#cbd5e1; font-weight:600;">Choose available golden beads in box:</div>
      <div style="display:flex; justify-content:center; gap:8px; margin-bottom:14px;">
        <button class="sim-btn" onclick="sim4RevBeads(20)">20 Beads</button>
        <button class="sim-btn active" onclick="sim4RevBeads(24)">24 Beads</button>
        <button class="sim-btn" onclick="sim4RevBeads(32)">32 Beads</button>
        <button class="sim-btn" onclick="sim4RevBeads(40)">40 Beads</button>
      </div>
      <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:14px; border:1px solid rgba(255,255,255,0.1);">
        <div id="sim4RevMath" style="font-size:20px; font-weight:bold; color:#38bdf8;">24 Beads ÷ 4 per wristband = 6 Complete Wristbands</div>
        <div style="font-size:12px; color:#94a3b8; margin-top:6px;">Check: 6 wristbands × 4 beads = 24 beads total (Zero leftover)</div>
      </div>
    </div>
  </div>
</div>
<script>
function sim4Mode(m) {
  const btns = document.querySelectorAll('#sim4 .sim-controls button');
  btns.forEach(b => b.classList.remove('active'));
  if (m === 'forward') {
    btns[0].classList.add('active');
    document.getElementById('sim4ForwardPanel').style.display = 'block';
    document.getElementById('sim4ReversePanel').style.display = 'none';
  } else {
    btns[1].classList.add('active');
    document.getElementById('sim4ForwardPanel').style.display = 'none';
    document.getElementById('sim4ReversePanel').style.display = 'block';
  }
}
function sim4UpdateForward(v) {
  document.getElementById('sim4FwdVal').innerText = v;
  document.getElementById('sim4FwdFlw').innerText = v * 1;
  document.getElementById('sim4FwdThr').innerText = v * 2;
  document.getElementById('sim4FwdBd').innerText = v * 4;
}
function sim4RevBeads(b) {
  document.querySelectorAll('#sim4ReversePanel .sim-btn').forEach(btn => {
    btn.classList.toggle('active', btn.innerText.startsWith(b));
  });
  const wristbands = Math.floor(b / 4);
  document.getElementById('sim4RevMath').innerText = b + ' Beads ÷ 4 per wristband = ' + wristbands + ' Complete Wristbands';
}
</script>
''',
    5: '''
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🍬 Rectangular Sweet Box Array Matrix</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Presets for 18 Sweets:</span>
      <button class="sim-btn" onclick="sim5Set(2, 9)">2 × 9</button>
      <button class="sim-btn active" onclick="sim5Set(3, 6)">3 × 6</button>
      <button class="sim-btn" onclick="sim5Set(6, 3)">6 × 3</button>
      <button class="sim-btn" onclick="sim5Set(3, 3)">Square 3 × 3</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="margin-bottom:10px; display:flex; gap:16px; align-items:center; font-size:13px; color:#cbd5e1;">
      <div>Rows: <button class="sim-btn" onclick="sim5Row(-1)">➖</button> <span id="sim5RText" style="font-weight:bold; color:#f59e0b;">3</span> <button class="sim-btn" onclick="sim5Row(1)">➕</button></div>
      <div>Columns: <button class="sim-btn" onclick="sim5Col(-1)">➖</button> <span id="sim5CText" style="font-weight:bold; color:#38bdf8;">6</span> <button class="sim-btn" onclick="sim5Col(1)">➕</button></div>
    </div>
    <div id="sim5BoxGrid" style="background:#451a03; border:3px solid #d97706; border-radius:12px; padding:10px; display:inline-grid; gap:6px; box-shadow:0 8px 20px rgba(0,0,0,0.5);">
      <!-- Sweet grid -->
    </div>
    <div id="sim5Formula" style="margin-top:12px; font-size:18px; font-weight:bold; color:#fbbf24;">
      3 Rows × 6 Columns = 18 Laddoos
    </div>
  </div>
</div>
<script>
let sim5R = 3;
let sim5C = 6;

function sim5Set(r, c) {
  sim5R = r;
  sim5C = c;
  sim5Render();
}
function sim5Row(delta) {
  sim5R = Math.max(1, Math.min(8, sim5R + delta));
  sim5Render();
}
function sim5Col(delta) {
  sim5C = Math.max(1, Math.min(10, sim5C + delta));
  sim5Render();
}
function sim5Render() {
  document.getElementById('sim5RText').innerText = sim5R;
  document.getElementById('sim5CText').innerText = sim5C;
  const grid = document.getElementById('sim5BoxGrid');
  grid.style.gridTemplateRows = 'repeat(' + sim5R + ', 24px)';
  grid.style.gridTemplateColumns = 'repeat(' + sim5C + ', 24px)';
  grid.innerHTML = '';
  const total = sim5R * sim5C;

  for (let i = 0; i < total; i++) {
    grid.innerHTML += '<div style="width:24px; height:24px; background:radial-gradient(circle at 35% 35%, #fbbf24, #d97706); border-radius:50%; box-shadow:inset -1px -1px 3px rgba(0,0,0,0.4), 0 2px 4px rgba(0,0,0,0.3);" title="Laddoo"></div>';
  }
  document.getElementById('sim5Formula').innerText = sim5R + ' Rows × ' + sim5C + ' Columns = ' + total + ' Laddoos';
}
setTimeout(sim5Render, 100);
</script>
''',
    6: '''
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🍽️ Fair Sharing Equal Division Simulator</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Plates:</span>
      <button class="sim-btn" onclick="sim6SetPlates(3)">3 Plates</button>
      <button class="sim-btn" onclick="sim6SetPlates(6)">6 Plates</button>
      <button class="sim-btn active" onclick="sim6SetPlates(9)">9 Plates</button>
      <button class="sim-btn" onclick="sim6DealRound()">Deal 1 Round</button>
      <button class="sim-btn" onclick="sim6Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; width:100%; max-width:620px; margin-bottom:12px; align-items:center;">
      <div style="font-size:14px; font-weight:600; color:#cbd5e1;">Platter Sweets Left: <span id="sim6Left" style="font-size:18px; font-weight:bold; color:#f59e0b;">18</span> / 18</div>
      <div style="font-size:14px; font-weight:600; color:#cbd5e1;">Rounds Dealt: <span id="sim6Rounds" style="font-size:18px; font-weight:bold; color:#38bdf8;">0</span></div>
    </div>
    <div id="sim6PlatesContainer" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; width:100%; max-width:650px; margin-bottom:14px;">
      <!-- Plates -->
    </div>
    <div id="sim6DivSummary" style="font-size:18px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:8px 20px;">
      Click 'Deal 1 Round' to distribute laddoos equally!
    </div>
  </div>
</div>
<script>
let sim6Total = 18;
let sim6PlatesCount = 9;
let sim6DealtPerPlate = 0;

function sim6SetPlates(n) {
  sim6PlatesCount = n;
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === n + ' Plates');
  });
  sim6Reset();
}
function sim6Reset() {
  sim6DealtPerPlate = 0;
  sim6Render();
}
function sim6DealRound() {
  const left = sim6Total - (sim6DealtPerPlate * sim6PlatesCount);
  if (left >= sim6PlatesCount) {
    sim6DealtPerPlate++;
    sim6Render();
  }
}
function sim6Render() {
  const left = sim6Total - (sim6DealtPerPlate * sim6PlatesCount);
  document.getElementById('sim6Left').innerText = left;
  document.getElementById('sim6Rounds').innerText = sim6DealtPerPlate;

  const container = document.getElementById('sim6PlatesContainer');
  container.innerHTML = '';
  for (let i = 0; i < sim6PlatesCount; i++) {
    let p = '<div style="background:rgba(255,255,255,0.1); border:2px solid rgba(255,255,255,0.3); border-radius:50%; width:56px; height:56px; display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:3px; padding:4px;" title="Plate ' + (i+1) + '">';
    for (let s = 0; s < sim6DealtPerPlate; s++) {
      p += '<div style="width:14px; height:14px; background:#fbbf24; border-radius:50%; box-shadow:0 0 3px #f59e0b;"></div>';
    }
    p += '</div>';
    container.innerHTML += p;
  }

  const summary = document.getElementById('sim6DivSummary');
  if (left === 0) {
    summary.innerHTML = '🎉 Fair Sharing Complete: ' + sim6Total + ' ÷ ' + sim6PlatesCount + ' = <span style="color:#fbbf24;">' + sim6DealtPerPlate + ' sweets per plate</span> (0 leftover)';
  } else {
    summary.innerHTML = '18 Total Sweets ÷ ' + sim6PlatesCount + ' Plates ➔ Current share: ' + sim6DealtPerPlate + ' each (' + left + ' remaining on platter)';
  }
}
setTimeout(sim6Reset, 100);
</script>
''',
    7: '''
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🥟 Step-by-Step Subtraction Sharing</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Select('kaju')">💎 Diamond Kaju Katli (20 ÷ 5)</button>
      <button class="sim-btn" onclick="sim7Select('peda')">⚪ Milk Pedas (15 ÷ 5)</button>
      <button class="sim-btn" onclick="sim7Step()">Next Subtraction Round (-5)</button>
      <button class="sim-btn" onclick="sim7Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim7Plates" style="display:flex; justify-content:center; gap:14px; margin-bottom:14px; width:100%; max-width:620px;">
      <!-- 5 Plates -->
    </div>
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:12px 20px; max-width:600px; width:100%; text-align:center; border:1px solid rgba(255,255,255,0.1);">
      <div id="sim7SubChain" style="font-size:15px; color:#cbd5e1; font-weight:600; margin-bottom:6px;">Initial Total: 20 Sweets</div>
      <div id="sim7Equation" style="font-size:20px; font-weight:bold; color:#f59e0b;">20 ÷ 5 = 4 Sweets per Plate</div>
    </div>
  </div>
</div>
<script>
let sim7Type = 'kaju';
let sim7Total = 20;
let sim7Round = 0;
const sim7MaxRounds = { 'kaju': 4, 'peda': 3 };

function sim7Select(t) {
  sim7Type = t;
  sim7Total = (t === 'kaju') ? 20 : 15;
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    if (t === 'kaju') b.classList.toggle('active', b.innerText.includes('Kaju'));
    else b.classList.toggle('active', b.innerText.includes('Pedas'));
  });
  sim7Reset();
}
function sim7Reset() {
  sim7Round = 0;
  sim7Render();
}
function sim7Step() {
  if (sim7Round < sim7MaxRounds[sim7Type]) {
    sim7Round++;
    sim7Render();
  }
}
function sim7Render() {
  const platesCont = document.getElementById('sim7Plates');
  platesCont.innerHTML = '';
  const sweetEmoji = (sim7Type === 'kaju') ? '💎' : '⚪';

  for (let p = 0; p < 5; p++) {
    let html = '<div style="background:rgba(255,255,255,0.08); border:2px solid rgba(255,255,255,0.25); border-radius:14px; padding:8px; text-align:center; flex:1; min-width:70px;">';
    html += '<div style="font-size:11px; font-weight:bold; color:#94a3b8; margin-bottom:4px;">Plate ' + (p+1) + '</div>';
    html += '<div style="font-size:18px; min-height:28px;">';
    for (let r = 0; r < sim7Round; r++) {
      html += sweetEmoji;
    }
    html += '</div><div style="font-size:12px; font-weight:bold; color:#fbbf24; margin-top:2px;">' + sim7Round + '</div></div>';
    platesCont.innerHTML += html;
  }

  const left = sim7Total - (sim7Round * 5);
  let chain = 'Repeated Subtraction: ';
  for (let r = 1; r <= sim7Round; r++) {
    chain += (sim7Total - (r-1)*5) + ' - 5 = ' + (sim7Total - r*5) + (r < sim7Round ? ' ➔ ' : '');
  }
  if (sim7Round === 0) chain = 'Platter holds ' + sim7Total + ' sweets ready for 5 plates.';
  document.getElementById('sim7SubChain').innerText = chain;

  const eq = document.getElementById('sim7Equation');
  if (left === 0) {
    eq.innerHTML = '🎉 ' + sim7Total + ' ÷ 5 = <span style="color:#34d399;">' + sim7Round + ' Sweets per Plate</span> (' + sim7Round + ' rounds of 5 subtracted)';
  } else {
    eq.innerText = sim7Total + ' Sweets on 5 Plates ➔ Current: ' + sim7Round + ' each (' + left + ' remaining)';
  }
}
setTimeout(sim7Reset, 100);
</script>
''',
    8: '''
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🚲 Bicycle Wheel & Jalebi Coil Pairing Lab</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8SetMode('bike')">🚲 Bicycle Wheels (Groups of 2)</button>
      <button class="sim-btn" onclick="sim8SetMode('jalebi')">🍥 Sweet Jalebis (Groups of 4)</button>
      <button class="sim-btn" onclick="sim8ChangeTotal(-1)">➖ Less Total</button>
      <button class="sim-btn" onclick="sim8ChangeTotal(1)">➕ More Total</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim8ItemsGrid" style="display:flex; flex-wrap:wrap; justify-content:center; gap:10px; width:100%; max-width:650px; margin-bottom:14px;">
      <!-- Grouped sets -->
    </div>
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:10px 24px; border:1px solid rgba(255,255,255,0.15); text-align:center;">
      <div id="sim8Formula" style="font-size:20px; font-weight:bold; color:#38bdf8;">12 Wheels ÷ 2 wheels per bike = 6 Complete Bicycles</div>
      <div id="sim8Check" style="font-size:12px; color:#cbd5e1; margin-top:4px;">Multiplication Check: 6 bicycles × 2 wheels = 12 wheels</div>
    </div>
  </div>
</div>
<script>
let sim8Mode = 'bike';
let sim8BikeWheels = 12;
let sim8JalebiCount = 24;

function sim8SetMode(m) {
  sim8Mode = m;
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    if (m === 'bike') b.classList.toggle('active', b.innerText.includes('Bicycle'));
    else b.classList.toggle('active', b.innerText.includes('Jalebis'));
  });
  sim8Render();
}
function sim8ChangeTotal(delta) {
  if (sim8Mode === 'bike') {
    sim8BikeWheels = Math.max(4, Math.min(20, sim8BikeWheels + delta * 2));
  } else {
    sim8JalebiCount = Math.max(8, Math.min(36, sim8JalebiCount + delta * 4));
  }
  sim8Render();
}
function sim8Render() {
  const container = document.getElementById('sim8ItemsGrid');
  container.innerHTML = '';

  if (sim8Mode === 'bike') {
    const bikes = sim8BikeWheels / 2;
    for (let b = 0; b < bikes; b++) {
      container.innerHTML += '<div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:8px 12px; text-align:center;"><div style="font-size:24px;">🚲</div><div style="font-size:12px; font-weight:bold; color:#93c5fd;">Bike ' + (b+1) + '</div><div style="font-size:11px; color:#bfdbfe;">⚙️⚙️ (2 Wheels)</div></div>';
    }
    document.getElementById('sim8Formula').innerText = sim8BikeWheels + ' Wheels ÷ 2 wheels per bike = ' + bikes + ' Complete Bicycles';
    document.getElementById('sim8Check').innerText = 'Multiplication Check: ' + bikes + ' bicycles × 2 wheels = ' + sim8BikeWheels + ' wheels';
  } else {
    const plates = sim8JalebiCount / 4;
    for (let p = 0; p < plates; p++) {
      container.innerHTML += '<div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:8px 12px; text-align:center;"><div style="font-size:22px;">🍥🍥<br>🍥🍥</div><div style="font-size:12px; font-weight:bold; color:#fbbf24; margin-top:4px;">Plate ' + (p+1) + '</div><div style="font-size:11px; color:#fef3c7;">(4 Jalebis)</div></div>';
    }
    document.getElementById('sim8Formula').innerText = sim8JalebiCount + ' Jalebis ÷ 4 per plate = ' + plates + ' Complete Plates';
    document.getElementById('sim8Check').innerText = 'Multiplication Check: ' + plates + ' plates × 4 jalebis = ' + sim8JalebiCount + ' jalebis';
  }
}
setTimeout(sim8Render, 100);
</script>
''',
    9: '''
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🌻 Botanical Array Commutative Symmetry</div>
    <div class="sim-controls">
      <button class="sim-btn active" id="sim9ViewBtn" onclick="sim9Rotate()">🔄 Rotate View: Front (8 × 6) vs Side (6 × 8)</button>
      <button class="sim-btn" onclick="sim9Preset(4, 7)">Test 4 × 7</button>
      <button class="sim-btn" onclick="sim9Preset(8, 6)">Reset 8 × 6</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim9GridWrapper" style="transition:transform 0.4s ease; display:inline-grid; gap:4px; padding:12px; background:rgba(6,78,59,0.3); border:2px solid #10b981; border-radius:12px;">
      <!-- Flower Grid -->
    </div>
    <div style="margin-top:12px; background:rgba(0,0,0,0.3); padding:8px 20px; border-radius:12px; border:1px solid rgba(255,255,255,0.15); text-align:center;">
      <div id="sim9Formula" style="font-size:20px; font-weight:bold; color:#34d399;">8 Rows × 6 Columns = 48 Plants</div>
      <div id="sim9Commutative" style="font-size:13px; color:#a7f3d0; margin-top:2px;">Commutative Law: 8 × 6 = 6 × 8 = 48 (Total remains identical!)</div>
    </div>
  </div>
</div>
<script>
let sim9R = 8;
let sim9C = 6;
let sim9Flipped = false;

function sim9Rotate() {
  sim9Flipped = !sim9Flipped;
  const temp = sim9R;
  sim9R = sim9C;
  sim9C = temp;
  sim9Render();
}
function sim9Preset(r, c) {
  sim9R = r;
  sim9C = c;
  sim9Flipped = false;
  sim9Render();
}
function sim9Render() {
  const grid = document.getElementById('sim9GridWrapper');
  grid.style.gridTemplateRows = 'repeat(' + sim9R + ', 22px)';
  grid.style.gridTemplateColumns = 'repeat(' + sim9C + ', 22px)';
  grid.innerHTML = '';
  const total = sim9R * sim9C;

  for (let i = 0; i < total; i++) {
    grid.innerHTML += '<div style="width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:15px;" title="Marigold">🌼</div>';
  }

  document.getElementById('sim9Formula').innerText = sim9R + ' Rows × ' + sim9C + ' Columns = ' + total + ' Plants';
  document.getElementById('sim9Commutative').innerHTML = 'Commutative Law: <span style="color:#fbbf24;">' + sim9R + ' × ' + sim9C + ' = ' + sim9C + ' × ' + sim9R + ' = ' + total + '</span> (Product unchanged!)';
}
setTimeout(sim9Render, 100);
</script>
''',
    10: '''
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🐥 Farmyard Chicks Times-Two Table Builder</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Pairs of Chicks:</span>
      <button class="sim-btn" onclick="sim10Adjust(-1)">➖ Less</button>
      <span id="sim10PairNum" style="font-size:16px; font-weight:bold; color:#fbbf24; min-width:24px; text-align:center;">5</span>
      <button class="sim-btn" onclick="sim10Adjust(1)">➕ More</button>
      <button class="sim-btn" onclick="sim10Set(10)">Full Table (10)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim10ChicksGrid" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px; width:100%; max-width:640px; margin-bottom:14px;">
      <!-- Chicks in pairs -->
    </div>
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:10px 24px; border:1px solid rgba(255,255,255,0.15); text-align:center;">
      <div id="sim10Equation" style="font-size:22px; font-weight:bold; color:#f59e0b;">5 Pairs of Chicks ➔ 5 × 2 = 10 Chicks</div>
      <div style="font-size:12px; color:#cbd5e1; margin-top:4px;">Even Number Rule: Every product in 2-times table ends in 0, 2, 4, 6, or 8!</div>
    </div>
  </div>
</div>
<script>
let sim10Pairs = 5;

function sim10Adjust(delta) {
  sim10Pairs = Math.max(1, Math.min(10, sim10Pairs + delta));
  sim10Render();
}
function sim10Set(val) {
  sim10Pairs = val;
  sim10Render();
}
function sim10Render() {
  document.getElementById('sim10PairNum').innerText = sim10Pairs;
  const grid = document.getElementById('sim10ChicksGrid');
  grid.innerHTML = '';
  const total = sim10Pairs * 2;

  for (let i = 0; i < sim10Pairs; i++) {
    grid.innerHTML += '<div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:6px 10px; display:flex; align-items:center; gap:4px;"><span style="font-size:20px;">🐥🐥</span><span style="font-size:11px; font-weight:bold; color:#fbbf24;">Pair ' + (i+1) + '</span></div>';
  }

  document.getElementById('sim10Equation').innerHTML = sim10Pairs + ' Pairs of Chicks &nbsp;➔&nbsp; <span style="color:#fbbf24;">' + sim10Pairs + ' × 2 = ' + total + ' Chicks</span>';
}
setTimeout(sim10Render, 100);
</script>
''',
    11: '''
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🏃 Skip Jump Number Track (Multiples of 3)</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim11Hop()">Jump Next (+3)</button>
      <button class="sim-btn" onclick="sim11Reset()">Reset to 0</button>
      <button class="sim-btn" onclick="sim11AutoJump()">Complete Track (10 Jumps)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim11Track" style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center; max-width:680px; margin-bottom:14px;">
      <!-- Stones 0 to 30 -->
    </div>
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:10px 24px; border:1px solid rgba(255,255,255,0.15); text-align:center;">
      <div id="sim11Stat" style="font-size:20px; font-weight:bold; color:#38bdf8;">0 Jumps taken ➔ Landing Stone: 0</div>
      <div id="sim11Formula" style="font-size:13px; color:#94a3b8; margin-top:4px;">Multiplication Sentence: 0 × 3 = 0</div>
    </div>
  </div>
</div>
<script>
let sim11Jumps = 0;

function sim11Hop() {
  if (sim11Jumps < 10) {
    sim11Jumps++;
    sim11Render();
  }
}
function sim11Reset() {
  sim11Jumps = 0;
  sim11Render();
}
function sim11AutoJump() {
  sim11Jumps = 10;
  sim11Render();
}
function sim11Render() {
  const track = document.getElementById('sim11Track');
  track.innerHTML = '';
  const currentPos = sim11Jumps * 3;

  for (let s = 0; s <= 30; s++) {
    const isLanded = (s % 3 === 0 && s <= currentPos && s > 0);
    const isCurrent = (s === currentPos);
    let bg = 'rgba(255,255,255,0.06)';
    let border = 'rgba(255,255,255,0.15)';
    let color = '#94a3b8';

    if (isCurrent) {
      bg = '#0284c7'; border = '#38bdf8'; color = '#fff';
    } else if (isLanded) {
      bg = 'rgba(56,189,248,0.2)'; border = '#0284c7'; color = '#7dd3fc';
    }

    let stone = '<div style="width:34px; height:34px; border-radius:50%; background:' + bg + '; border:2px solid ' + border + '; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:' + color + '; position:relative;" title="Stone ' + s + '">';
    stone += s;
    if (isCurrent) stone += '<div style="position:absolute; top:-16px; font-size:14px;">🚩</div>';
    stone += '</div>';
    track.innerHTML += stone;
  }

  document.getElementById('sim11Stat').innerHTML = sim11Jumps + ' Jumps of 3 taken &nbsp;➔&nbsp; Landing Stone: <span style="color:#38bdf8;">' + currentPos + '</span>';
  document.getElementById('sim11Formula').innerText = 'Multiplication Sentence: ' + sim11Jumps + ' × 3 = ' + currentPos;
}
setTimeout(sim11Reset, 100);
</script>
''',
    12: '''
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🎯 Dual-Track Multiples Race: 4-Step vs 6-Step</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Target Stone:</span>
      <button class="sim-btn" onclick="sim12Target(12)">12</button>
      <button class="sim-btn active" onclick="sim12Target(24)">24</button>
      <button class="sim-btn" onclick="sim12Target(36)">36</button>
      <button class="sim-btn" onclick="sim12Target(48)">48</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="width:100%; max-width:640px; margin-bottom:14px;">
      <div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:10px 16px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between;">
        <div style="font-size:14px; font-weight:bold; color:#60a5fa;">🔵 4-Step Hopper (Jumps by 4):</div>
        <div id="sim12Jumper4" style="font-size:16px; font-weight:bold; color:#fff;">6 Jumps to reach 24 (6 × 4 = 24)</div>
      </div>
      <div style="background:rgba(168,85,247,0.15); border:1px solid #a855f7; border-radius:12px; padding:10px 16px; display:flex; align-items:center; justify-content:space-between;">
        <div style="font-size:14px; font-weight:bold; color:#c084fc;">🟣 6-Step Hopper (Jumps by 6):</div>
        <div id="sim12Jumper6" style="font-size:16px; font-weight:bold; color:#fff;">4 Jumps to reach 24 (4 × 6 = 24)</div>
      </div>
    </div>
    <div id="sim12CommonBanner" style="font-size:16px; font-weight:bold; color:#fbbf24; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:8px 20px;">
      ⭐ 24 is a Common Multiple of 4 and 6! Both jumpers land squarely on 24.
    </div>
  </div>
</div>
<script>
let sim12T = 24;

function sim12Target(t) {
  sim12T = t;
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === '' + t);
  });
  sim12Render();
}
function sim12Render() {
  const j4 = sim12T / 4;
  const j6 = sim12T / 6;

  document.getElementById('sim12Jumper4').innerText = j4 + ' Jumps to reach ' + sim12T + ' (' + j4 + ' × 4 = ' + sim12T + ')';
  document.getElementById('sim12Jumper6').innerText = j6 + ' Jumps to reach ' + sim12T + ' (' + j6 + ' × 6 = ' + sim12T + ')';
  document.getElementById('sim12CommonBanner').innerHTML = '⭐ <span style="color:#fff;">' + sim12T + '</span> is a Common Multiple of 4 and 6! (6-hopper uses fewer leaps: ' + j6 + ' vs ' + j4 + ')';
}
setTimeout(sim12Render, 100);
</script>
''',
    13: '''
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🥢 Stick Cross Intersection Dot Builder</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Horizontal Sticks:</span>
      <button class="sim-btn" onclick="sim13SetH(3)">3</button>
      <button class="sim-btn" onclick="sim13SetH(4)">4</button>
      <button class="sim-btn active" onclick="sim13SetH(5)">5</button>
      <span style="margin-left:8px; font-size:13px; color:#cbd5e1;">Vertical Sticks:</span>
      <button class="sim-btn" onclick="sim13SetV(3)">3</button>
      <button class="sim-btn active" onclick="sim13SetV(4)">4</button>
      <button class="sim-btn" onclick="sim13SetV(5)">5</button>
      <button class="sim-btn" onclick="sim13SetV(6)">6</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim13SticksCanvas" style="position:relative; width:260px; height:180px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.1); margin-bottom:12px;">
      <!-- Horizontal and vertical sticks SVG -->
    </div>
    <div id="sim13Equation" style="font-size:20px; font-weight:bold; color:#f87171; background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:12px; padding:8px 24px;">
      5 Horizontal × 4 Vertical = 20 Intersection Dots
    </div>
  </div>
</div>
<script>
let sim13H = 5;
let sim13V = 4;

function sim13SetH(h) {
  sim13H = h;
  sim13Render();
}
function sim13SetV(v) {
  sim13V = v;
  sim13Render();
}
function sim13Render() {
  const container = document.getElementById('sim13SticksCanvas');
  const w = 260;
  const h = 180;
  let svg = '<svg width="' + w + '" height="' + h + '" style="position:absolute; top:0; left:0;">';

  const hGap = h / (sim13H + 1);
  const vGap = w / (sim13V + 1);

  // Horizontal sticks
  for (let i = 1; i <= sim13H; i++) {
    const y = i * hGap;
    svg += '<line x1="15" y1="' + y + '" x2="' + (w-15) + '" y2="' + y + '" stroke="#d97706" stroke-width="5" stroke-linecap="round" />';
  }

  // Vertical sticks
  for (let j = 1; j <= sim13V; j++) {
    const x = j * vGap;
    svg += '<line x1="' + x + '" y1="15" x2="' + x + '" y2="' + (h-15) + '" stroke="#3b82f6" stroke-width="5" stroke-linecap="round" />';
  }

  // Intersection dots
  for (let i = 1; i <= sim13H; i++) {
    const y = i * hGap;
    for (let j = 1; j <= sim13V; j++) {
      const x = j * vGap;
      svg += '<circle cx="' + x + '" cy="' + y + '" r="5" fill="#ef4444" stroke="#fff" stroke-width="1.5" />';
    }
  }

  svg += '</svg>';
  container.innerHTML = svg;
  const total = sim13H * sim13V;
  document.getElementById('sim13Equation').innerText = sim13H + ' Horizontal × ' + sim13V + ' Vertical = ' + total + ' Red Intersection Dots';
}
setTimeout(sim13Render, 100);
</script>
''',
    14: '''
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🔢 Table Additive Synthesis & 5s Digit Rhythm</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Mode('five')">5-Times Digit Rhythm (0 vs 5)</button>
      <button class="sim-btn" onclick="sim14Mode('addition')">Synthesize: 2× + 3× = 5× Table</button>
      <button class="sim-btn" onclick="sim14Mode('seven')">Synthesize: 4× + 3× = 7× Table</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim14Content" style="width:100%; max-width:640px; text-align:center;">
      <!-- Dynamic table content -->
    </div>
  </div>
</div>
<script>
let sim14Current = 'five';

function sim14Mode(m) {
  sim14Current = m;
  const btns = document.querySelectorAll('#sim14 .sim-controls button');
  btns.forEach(b => b.classList.remove('active'));
  if (m === 'five') btns[0].classList.add('active');
  else if (m === 'addition') btns[1].classList.add('active');
  else btns[2].classList.add('active');
  sim14Render();
}

function sim14Render() {
  const container = document.getElementById('sim14Content');
  if (sim14Current === 'five') {
    let html = '<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px; margin-bottom:12px;">';
    for (let i = 1; i <= 10; i++) {
      const prod = i * 5;
      const endsInFive = (prod % 10 === 5);
      const bg = endsInFive ? 'rgba(236,72,153,0.2)' : 'rgba(16,185,129,0.2)';
      const border = endsInFive ? '#ec4899' : '#10b981';
      const badge = endsInFive ? 'Ends in 5' : 'Ends in 0';
      html += '<div style="background:' + bg + '; border:1px solid ' + border + '; border-radius:10px; padding:6px 10px; min-width:80px;">';
      html += '<div style="font-size:11px; color:#cbd5e1;">5 × ' + i + '</div>';
      html += '<div style="font-size:18px; font-weight:bold; color:#fff;">' + prod + '</div>';
      html += '<div style="font-size:10px; font-weight:bold; color:' + border + ';">' + badge + '</div></div>';
    }
    html += '</div><div style="font-size:14px; color:#38bdf8; font-weight:600;">Units digits alternate forever: 5, 0, 5, 0, 5, 0, 5, 0, 5, 0!</div>';
    container.innerHTML = html;
  } else if (sim14Current === 'addition') {
    let html = '<div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px; font-size:12px; margin-bottom:12px; background:rgba(0,0,0,0.2); padding:10px; border-radius:12px;">';
    html += '<div style="font-weight:bold; color:#60a5fa;">2-Times Table</div><div style="font-weight:bold; color:#cbd5e1;">+</div><div style="font-weight:bold; color:#c084fc;">3-Times Table</div><div style="font-weight:bold; color:#cbd5e1;">=</div><div style="font-weight:bold; color:#34d399;">5-Times Table</div>';
    for (let i = 1; i <= 5; i++) {
      html += '<div style="color:#93c5fd;">2 × ' + i + ' = ' + (2*i) + '</div><div>+</div><div style="color:#d8b4fe;">3 × ' + i + ' = ' + (3*i) + '</div><div>=</div><div style="font-weight:bold; color:#6ee7b7;">5 × ' + i + ' = ' + (5*i) + '</div>';
    }
    html += '</div><div style="font-size:14px; color:#fbbf24; font-weight:bold;">(2 × n) + (3 × n) = (2 + 3) × n = 5 × n!</div>';
    container.innerHTML = html;
  } else {
    let html = '<div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px; font-size:12px; margin-bottom:12px; background:rgba(0,0,0,0.2); padding:10px; border-radius:12px;">';
    html += '<div style="font-weight:bold; color:#f59e0b;">4-Times Table</div><div style="font-weight:bold; color:#cbd5e1;">+</div><div style="font-weight:bold; color:#c084fc;">3-Times Table</div><div style="font-weight:bold; color:#cbd5e1;">=</div><div style="font-weight:bold; color:#ec4899;">7-Times Table</div>';
    for (let i = 1; i <= 5; i++) {
      html += '<div style="color:#fcd34d;">4 × ' + i + ' = ' + (4*i) + '</div><div>+</div><div style="color:#d8b4fe;">3 × ' + i + ' = ' + (3*i) + '</div><div>=</div><div style="font-weight:bold; color:#f472b6;">7 × ' + i + ' = ' + (7*i) + '</div>';
    }
    html += '</div><div style="font-size:14px; color:#fbbf24; font-weight:bold;">(4 × n) + (3 × n) = (4 + 3) × n = 7 × n!</div>';
    container.innerHTML = html;
  }
}
setTimeout(sim14Render, 100);
</script>
''',
    15: '''
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🐚 Sea-Shell Repeated Subtraction & Currency Changer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Mode('shell')">🐚 Sea-Shell Necklaces (112 ÷ 28)</button>
      <button class="sim-btn" onclick="sim15Mode('rupee')">💵 Currency Exchange (500 ÷ 50)</button>
      <button class="sim-btn" onclick="sim15Step()">Subtract Next Group</button>
      <button class="sim-btn" onclick="sim15Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim15Display" style="width:100%; max-width:640px; text-align:center;">
      <!-- Dynamic subtraction chain -->
    </div>
    <div id="sim15Equation" style="margin-top:12px; font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px;">
      112 Shells ready for necklace crafting.
    </div>
  </div>
</div>
<script>
let sim15Type = 'shell';
let sim15StepCount = 0;

function sim15Mode(m) {
  sim15Type = m;
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    if (m === 'shell') b.classList.toggle('active', b.innerText.includes('Sea-Shell'));
    else b.classList.toggle('active', b.innerText.includes('Currency'));
  });
  sim15Reset();
}
function sim15Reset() {
  sim15StepCount = 0;
  sim15Render();
}
function sim15Step() {
  const maxSteps = (sim15Type === 'shell') ? 4 : 10;
  if (sim15StepCount < maxSteps) {
    sim15StepCount++;
    sim15Render();
  }
}
function sim15Render() {
  const container = document.getElementById('sim15Display');
  const eq = document.getElementById('sim15Equation');

  if (sim15Type === 'shell') {
    const total = 112;
    const sub = 28;
    const left = total - (sim15StepCount * sub);

    let html = '<div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-bottom:12px;">';
    for (let i = 0; i < 4; i++) {
      const active = (i < sim15StepCount);
      html += '<div style="background:' + (active ? 'rgba(16,185,129,0.2)' : 'rgba(255,255,255,0.06)') + '; border:1px solid ' + (active ? '#10b981' : 'rgba(255,255,255,0.2)') + '; border-radius:12px; padding:10px 14px; min-width:110px;">';
      html += '<div style="font-size:24px;">' + (active ? '📿' : '🐚') + '</div>';
      html += '<div style="font-size:12px; font-weight:bold; color:' + (active ? '#34d399' : '#94a3b8') + ';">Necklace ' + (i+1) + '</div>';
      html += '<div style="font-size:11px; color:#cbd5e1;">(28 Shells)</div></div>';
    }
    html += '</div>';
    container.innerHTML = html;

    if (left === 0) {
      eq.innerHTML = '🎉 Repeated Subtraction Complete: 112 - 28 - 28 - 28 - 28 = 0 &nbsp;➔&nbsp; <span style="color:#34d399;">112 ÷ 28 = 4 Necklaces</span>';
    } else {
      eq.innerText = 'Shells remaining: ' + left + ' (Subtracted ' + sim15StepCount + ' rounds of 28)';
    }
  } else {
    const total = 500;
    const sub = 50;
    const left = total - (sim15StepCount * sub);

    let html = '<div style="display:flex; justify-content:center; gap:6px; flex-wrap:wrap; margin-bottom:12px;">';
    for (let i = 0; i < 10; i++) {
      const active = (i < sim15StepCount);
      html += '<div style="background:' + (active ? 'rgba(59,130,246,0.2)' : 'rgba(255,255,255,0.06)') + '; border:1px solid ' + (active ? '#3b82f6' : 'rgba(255,255,255,0.2)') + '; border-radius:8px; padding:6px 8px; font-size:11px; font-weight:bold; color:' + (active ? '#93c5fd' : '#64748b') + ';">💵 ₹50 (#' + (i+1) + ')</div>';
    }
    html += '</div>';
    container.innerHTML = html;

    if (left === 0) {
      eq.innerHTML = '🎉 Exchanged ₹500 Note: Subtracted 10 notes of ₹50 &nbsp;➔&nbsp; <span style="color:#38bdf8;">500 ÷ 50 = 10 Notes of ₹50</span>';
    } else {
      eq.innerText = 'Rupees remaining: ₹' + left + ' (Exchanged ' + sim15StepCount + ' notes of ₹50)';
    }
  }
}
setTimeout(sim15Reset, 100);
</script>
''',
    16: '''
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">✉️ Mystery Factor Envelope Unlocker</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Target Envelope:</span>
      <button class="sim-btn active" onclick="sim16Select(32, 4, 8)">Envelope 32</button>
      <button class="sim-btn" onclick="sim16Select(45, 5, 9)">Envelope 45</button>
      <button class="sim-btn" onclick="sim16Select(28, 4, 7)">Envelope 28</button>
      <button class="sim-btn" onclick="sim16Select(56, 7, 8)">Envelope 56</button>
      <button class="sim-btn" onclick="sim16ResetCards()">Reset Slots</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
      <div id="sim16SlotA" style="width:48px; height:60px; background:rgba(255,255,255,0.1); border:2px dashed #38bdf8; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#38bdf8;">?</div>
      <div style="font-size:24px; font-weight:bold; color:#cbd5e1;">×</div>
      <div id="sim16SlotB" style="width:48px; height:60px; background:rgba(255,255,255,0.1); border:2px dashed #38bdf8; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:bold; color:#38bdf8;">?</div>
      <div style="font-size:24px; font-weight:bold; color:#cbd5e1;">=</div>
      <div id="sim16Envelope" style="background:radial-gradient(circle, #f59e0b, #b45309); border:2px solid #fbbf24; border-radius:12px; padding:10px 20px; font-size:24px; font-weight:bold; color:#fff; box-shadow:0 4px 12px rgba(245,158,11,0.4);">
        ✉️ 32
      </div>
    </div>
    <div style="font-size:12px; color:#cbd5e1; margin-bottom:6px; font-weight:600;">Click two number cards from deck (1 to 10) to fill slots:</div>
    <div id="sim16Deck" style="display:flex; gap:6px; flex-wrap:wrap; justify-content:center; max-width:620px; margin-bottom:10px;">
      <!-- Cards 1 to 10 -->
    </div>
    <div id="sim16Status" style="font-size:16px; font-weight:bold; color:#fbbf24;">
      Choose two cards whose product equals the envelope!
    </div>
  </div>
</div>
<script>
let sim16Target = 32;
let sim16A = null;
let sim16B = null;

function sim16Select(t) {
  sim16Target = t;
  document.getElementById('sim16Envelope').innerHTML = '✉️ ' + t;
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === 'Envelope ' + t);
  });
  sim16ResetCards();
}

function sim16ResetCards() {
  sim16A = null;
  sim16B = null;
  document.getElementById('sim16SlotA').innerText = '?';
  document.getElementById('sim16SlotB').innerText = '?';
  document.getElementById('sim16Status').innerHTML = 'Choose two cards from the deck whose product equals ' + sim16Target + '!';
  sim16RenderDeck();
}

function sim16PickCard(num) {
  if (sim16A === null) {
    sim16A = num;
    document.getElementById('sim16SlotA').innerText = num;
  } else if (sim16B === null) {
    sim16B = num;
    document.getElementById('sim16SlotB').innerText = num;
    sim16Check();
  }
}

function sim16Check() {
  const prod = sim16A * sim16B;
  const status = document.getElementById('sim16Status');
  if (prod === sim16Target) {
    status.innerHTML = '🎉 <span style="color:#34d399;">UNLOCKED! ' + sim16A + ' × ' + sim16B + ' = ' + sim16Target + ' correctly opens the envelope!</span>';
  } else {
    status.innerHTML = '❌ <span style="color:#f87171;">' + sim16A + ' × ' + sim16B + ' = ' + prod + ' (Not ' + sim16Target + '). Click Reset Slots and try again!</span>';
  }
}

function sim16RenderDeck() {
  const deck = document.getElementById('sim16Deck');
  deck.innerHTML = '';
  for (let n = 1; n <= 10; n++) {
    deck.innerHTML += '<button onclick="sim16PickCard(' + n + ')" style="width:36px; height:48px; background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.3); border-radius:6px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer;" onmouseover="this.style.background='#38bdf8'" onmouseout="this.style.background='rgba(255,255,255,0.12)'">' + n + '</button>';
  }
}
setTimeout(sim16ResetCards, 100);
</script>
''',
}

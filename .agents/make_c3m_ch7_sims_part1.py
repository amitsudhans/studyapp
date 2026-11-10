#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
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
""",

    2: """
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
""",

    3: """
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
""",

    4: """
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
""",

    5: """
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
""",

    6: """
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
""",

    7: """
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
""",

    8: """
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
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Sims 1-8).")

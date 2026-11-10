#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 8: Fair Share
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🥞 Paratha & Chocolate Bar Half Folding Lab</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Select('paratha')">Round Paratha (Circle)</button>
      <button class="sim-btn" onclick="sim1Select('chocolate')">Chocolate Bar (8 Blocks)</button>
      <button class="sim-btn" onclick="sim1Fold()">Cut / Fold Down Middle</button>
      <button class="sim-btn" onclick="sim1Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim1Visual" style="margin-bottom:14px; min-height:120px; display:flex; align-items:center; justify-content:center; gap:16px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim1Equation" style="font-size:18px; font-weight:bold; color:#f59e0b; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 20px;">
      1 Whole Object ready to be shared equally between 2 friends.
    </div>
  </div>
</div>
<script>
let sim1Type = 'paratha';
let sim1IsFolded = false;

function sim1Select(t) {
  sim1Type = t;
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    if (t === 'paratha') b.classList.toggle('active', b.innerText.includes('Paratha'));
    else b.classList.toggle('active', b.innerText.includes('Chocolate'));
  });
  sim1Reset();
}
function sim1Reset() {
  sim1IsFolded = false;
  sim1Render();
}
function sim1Fold() {
  sim1IsFolded = true;
  sim1Render();
}
function sim1Render() {
  const vis = document.getElementById('sim1Visual');
  const eq = document.getElementById('sim1Equation');

  if (sim1Type === 'paratha') {
    if (!sim1IsFolded) {
      vis.innerHTML = '<div style="width:110px; height:110px; background:radial-gradient(circle at 35% 35%, #fbbf24, #d97706); border-radius:50%; border:3px solid #b45309; box-shadow:0 6px 14px rgba(0,0,0,0.4); display:flex; align-items:center; justify-content:center; font-weight:bold; color:#78350f;">1 Whole</div>';
      eq.innerText = '1 Whole Round Paratha ready to fold.';
    } else {
      vis.innerHTML = '<div style="display:flex; gap:14px;"><div style="width:55px; height:110px; background:radial-gradient(circle at 70% 35%, #fbbf24, #d97706); border-radius:110px 0 0 110px; border:3px solid #b45309; border-right:2px dashed #fff; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#78350f;">1/2</div><div style="width:55px; height:110px; background:radial-gradient(circle at 30% 35%, #fbbf24, #d97706); border-radius:0 110px 110px 0; border:3px solid #b45309; border-left:2px dashed #fff; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#78350f;">1/2</div></div>';
      eq.innerHTML = '🎉 <span style="color:#34d399;">Equal Halves: 1 Whole Paratha = 1/2 + 1/2 (Two identical semicircles!)</span>';
    }
  } else {
    if (!sim1IsFolded) {
      let html = '<div style="display:grid; grid-template-columns:repeat(4, 28px); gap:3px; background:#451a03; padding:6px; border-radius:8px; border:2px solid #78350f;">';
      for (let i = 0; i < 8; i++) html += '<div style="width:28px; height:28px; background:#78350f; border:1px solid #92400e; border-radius:4px;"></div>';
      html += '</div>';
      vis.innerHTML = html;
      eq.innerText = '1 Whole Chocolate Bar (8 equal blocks total).';
    } else {
      let html = '<div style="display:flex; gap:12px;">';
      html += '<div style="background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:8px; padding:6px; text-align:center;"><div style="display:grid; grid-template-columns:repeat(2, 28px); gap:3px; margin-bottom:4px;"><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div></div><div style="font-size:11px; font-weight:bold; color:#34d399;">4 Blocks (1/2)</div></div>';
      html += '<div style="background:rgba(59,130,246,0.2); border:1px solid #3b82f6; border-radius:8px; padding:6px; text-align:center;"><div style="display:grid; grid-template-columns:repeat(2, 28px); gap:3px; margin-bottom:4px;"><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div><div style="width:28px; height:28px; background:#78350f; border-radius:4px;"></div></div><div style="font-size:11px; font-weight:bold; color:#60a5fa;">4 Blocks (1/2)</div></div>';
      html += '</div>';
      vis.innerHTML = html;
      eq.innerHTML = '🎉 <span style="color:#38bdf8;">8 Blocks ÷ 2 = 4 Blocks each (Exactly one half each!)</span>';
    }
  }
}
setTimeout(sim1Reset, 100);
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">📐 Slicing Alignment & Equal Half Inspector</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Cut Position:</span>
      <button class="sim-btn" onclick="sim2SetPos(-30)">Offset Cut (-30%)</button>
      <button class="sim-btn active" onclick="sim2SetPos(0)">Exact Center (0% Offset)</button>
      <button class="sim-btn" onclick="sim2SetPos(30)">Offset Cut (+30%)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim2ShapeBox" style="position:relative; width:220px; height:110px; background:#1e293b; border-radius:12px; border:2px solid #475569; overflow:hidden; margin-bottom:14px;">
      <!-- Sliced sections -->
      <div id="sim2LeftArea" style="position:absolute; left:0; top:0; bottom:0; background:rgba(59,130,246,0.3); width:50%; border-right:2px dashed #f59e0b; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#60a5fa; font-size:14px;">50%</div>
      <div id="sim2RightArea" style="position:absolute; right:0; top:0; bottom:0; background:rgba(16,185,129,0.3); width:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#34d399; font-size:14px;">50%</div>
    </div>
    <div id="sim2Status" style="font-size:18px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:8px 24px;">
      ✓ Valid Halves: Both pieces have equal 50% area!
    </div>
  </div>
</div>
<script>
let sim2Offset = 0;

function sim2SetPos(pos) {
  sim2Offset = pos;
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (pos === 0 && b.innerText.includes('Exact Center')) || (pos === -30 && b.innerText.includes('-30%')) || (pos === 30 && b.innerText.includes('+30%')));
  });
  sim2Render();
}

function sim2Render() {
  const leftPct = 50 + sim2Offset;
  const rightPct = 50 - sim2Offset;

  const leftEl = document.getElementById('sim2LeftArea');
  const rightEl = document.getElementById('sim2RightArea');
  leftEl.style.width = leftPct + '%';
  rightEl.style.width = rightPct + '%';
  leftEl.innerText = leftPct + '%';
  rightEl.innerText = rightPct + '%';

  const status = document.getElementById('sim2Status');
  if (sim2Offset === 0) {
    status.className = 'font-bold text-lg text-emerald-400 bg-emerald-950/40 border border-emerald-600 rounded-xl px-5 py-2';
    status.innerHTML = '✓ <span style="color:#34d399;">Valid Halves: Cut passes directly through center (50% / 50%)!</span>';
  } else {
    status.className = 'font-bold text-lg text-rose-400 bg-rose-950/40 border border-rose-600 rounded-xl px-5 py-2';
    status.innerHTML = '✕ <span style="color:#f87171;">Unequal Slices: ' + leftPct + '% vs ' + rightPct + '% (Not equal halves!)</span>';
  }
}
setTimeout(sim2Render, 100);
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🦋 Mirror Reflection Symmetry & Chikki Snack Counter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Mode('butterfly')">🦋 Symmetrical Butterfly</button>
      <button class="sim-btn" onclick="sim3Mode('chikki')">🍫 Chikki Nibble (2 out of 4)</button>
      <button class="sim-btn" onclick="sim3Action()">Interact Step</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim3Display" style="min-height:130px; display:flex; align-items:center; justify-content:center; margin-bottom:12px;">
      <!-- Dynamic SVG -->
    </div>
    <div id="sim3Equation" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Click 'Interact Step' to see symmetry in action!
    </div>
  </div>
</div>
<script>
let sim3CurrentMode = 'butterfly';
let sim3Step = false;

function sim3Mode(m) {
  sim3CurrentMode = m;
  sim3Step = false;
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    if (m === 'butterfly') b.classList.toggle('active', b.innerText.includes('Butterfly'));
    else b.classList.toggle('active', b.innerText.includes('Chikki'));
  });
  sim3Render();
}
function sim3Action() {
  sim3Step = !sim3Step;
  sim3Render();
}
function sim3Render() {
  const disp = document.getElementById('sim3Display');
  const eq = document.getElementById('sim3Equation');

  if (sim3CurrentMode === 'butterfly') {
    if (!sim3Step) {
      disp.innerHTML = '<div style="display:flex; align-items:center; gap:0; border:2px dashed #64748b; border-radius:12px; padding:10px;"><div style="font-size:48px; background:rgba(236,72,153,0.2); border-radius:8px 0 0 8px; padding:10px;">🦋</div><div style="width:70px; height:70px; background:rgba(255,255,255,0.05); border-left:2px solid #ec4899; display:flex; align-items:center; justify-content:center; color:#64748b; font-size:12px;">Missing Half</div></div>';
      eq.innerText = 'Only the left half is drawn. Click \'Interact Step\' to reflect the right half!';
    } else {
      disp.innerHTML = '<div style="display:flex; align-items:center; gap:0; border:2px solid #ec4899; border-radius:12px; padding:10px;"><div style="font-size:48px; background:rgba(236,72,153,0.2); border-radius:8px 0 0 8px; padding:10px;">🦋</div><div style="font-size:48px; background:rgba(236,72,153,0.2); border-radius:0 8px 8px 0; padding:10px; transform:scaleX(-1); border-left:2px solid #ec4899;">🦋</div></div>';
      eq.innerHTML = '🎉 <span style="color:#f472b6;">Mirror Symmetry Complete: Right half mirrors left half to make 1 whole!</span>';
    }
  } else {
    if (!sim3Step) {
      disp.innerHTML = '<div style="display:flex; gap:4px; background:#451a03; padding:8px; border-radius:8px; border:2px solid #78350f;"><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div></div>';
      eq.innerText = 'Chikki snack has 4 equal strips. Click \'Interact Step\' to nibble 2 strips!';
    } else {
      disp.innerHTML = '<div style="display:flex; gap:4px; background:#451a03; padding:8px; border-radius:8px; border:2px solid #78350f;"><div style="width:26px; height:60px; background:transparent; border:1px dashed #64748b; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:10px; color:#64748b;">Eaten</div><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div><div style="width:26px; height:60px; background:#d97706; border-radius:4px;"></div><div style="width:26px; height:60px; background:transparent; border:1px dashed #64748b; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:10px; color:#64748b;">Eaten</div></div>';
      eq.innerHTML = '🎉 <span style="color:#38bdf8;">2 Strips eaten out of 4 = 2/4 = 1/2 Eaten (Exactly one half remains!)</span>';
    }
  }
}
setTimeout(sim3Render, 100);
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">📄 Origami Square Multiple Folding Paths</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4Fold('horiz')">Horizontal Fold</button>
      <button class="sim-btn" onclick="sim4Fold('vert')">Vertical Fold</button>
      <button class="sim-btn" onclick="sim4Fold('diag1')">Main Diagonal</button>
      <button class="sim-btn" onclick="sim4Fold('diag2')">Opposite Diagonal</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim4PaperCanvas" style="position:relative; width:130px; height:130px; background:#1e293b; border:2px solid #94a3b8; border-radius:6px; overflow:hidden; margin-bottom:14px;">
      <!-- Crease overlay -->
    </div>
    <div id="sim4FoldNote" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Horizontal fold creates two identical rectangles (50% area each).
    </div>
  </div>
</div>
<script>
function sim4Fold(type) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (type === 'horiz' && b.innerText.includes('Horizontal')) ||
      (type === 'vert' && b.innerText.includes('Vertical')) ||
      (type === 'diag1' && b.innerText.includes('Main')) ||
      (type === 'diag2' && b.innerText.includes('Opposite')));
  });

  const canvas = document.getElementById('sim4PaperCanvas');
  const note = document.getElementById('sim4FoldNote');
  const sz = 130;

  if (type === 'horiz') {
    canvas.innerHTML = '<div style="position:absolute; top:0; left:0; width:100%; height:50%; background:rgba(59,130,246,0.3); border-bottom:2px dashed #f59e0b; display:flex; align-items:center; justify-content:center; color:#93c5fd; font-weight:bold; font-size:13px;">Top 1/2</div><div style="position:absolute; bottom:0; left:0; width:100%; height:50%; background:rgba(16,185,129,0.3); display:flex; align-items:center; justify-content:center; color:#6ee7b7; font-weight:bold; font-size:13px;">Bottom 1/2</div>';
    note.innerHTML = 'Horizontal Fold: Produces 2 equal rectangular halves (Area = 50% each)!';
  } else if (type === 'vert') {
    canvas.innerHTML = '<div style="position:absolute; top:0; left:0; width:50%; height:100%; background:rgba(59,130,246,0.3); border-right:2px dashed #f59e0b; display:flex; align-items:center; justify-content:center; color:#93c5fd; font-weight:bold; font-size:13px;">Left 1/2</div><div style="position:absolute; top:0; right:0; width:50%; height:100%; background:rgba(16,185,129,0.3); display:flex; align-items:center; justify-content:center; color:#6ee7b7; font-weight:bold; font-size:13px;">Right 1/2</div>';
    note.innerHTML = 'Vertical Fold: Produces 2 tall rectangular halves (Area = 50% each)!';
  } else if (type === 'diag1') {
    canvas.innerHTML = '<svg width="' + sz + '" height="' + sz + '" style="position:absolute; top:0; left:0;"><polygon points="0,0 ' + sz + ',0 ' + sz + ',' + sz + '" fill="rgba(59,130,246,0.35)"/><polygon points="0,0 0,' + sz + ' ' + sz + ',' + sz + '" fill="rgba(16,185,129,0.35)"/><line x1="0" y1="0" x2="' + sz + '" y2="' + sz + '" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4"/><text x="75" y="35" fill="#93c5fd" font-size="12" font-weight="bold">1/2</text><text x="35" y="95" fill="#6ee7b7" font-size="12" font-weight="bold">1/2</text></svg>';
    note.innerHTML = 'Diagonal Fold: Produces 2 congruent triangular halves (Area = 50% each)!';
  } else {
    canvas.innerHTML = '<svg width="' + sz + '" height="' + sz + '" style="position:absolute; top:0; left:0;"><polygon points="0,0 ' + sz + ',0 0,' + sz + '" fill="rgba(245,158,11,0.35)"/><polygon points="' + sz + ',0 ' + sz + ',' + sz + ' 0,' + sz + '" fill="rgba(236,72,153,0.35)"/><line x1="' + sz + '" y1="0" x2="0" y2="' + sz + '" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4"/><text x="35" y="35" fill="#fde68a" font-size="12" font-weight="bold">1/2</text><text x="75" y="95" fill="#fbcfe8" font-size="12" font-weight="bold">1/2</text></svg>';
    note.innerHTML = 'Opposite Diagonal: Produces 2 matching triangular halves (Area = 50% each)!';
  }
}
setTimeout(() => sim4Fold('horiz'), 100);
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">⚖️ Resource Fairness Dilemma Evaluator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5Inspect('blanket')">Woolen Blanket</button>
      <button class="sim-btn" onclick="sim5Inspect('tree')">Mango Tree</button>
      <button class="sim-btn" onclick="sim5Inspect('lamp')">Solar Lantern</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim5DilemmaCards" style="display:flex; gap:12px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- Populated by JS -->
    </div>
    <div id="sim5Verdict" style="font-size:16px; font-weight:bold; color:#f87171; background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:12px; padding:8px 24px; text-align:center;">
      Unfair Distribution: Daytime warmth is useless compared to cold night protection!
    </div>
  </div>
</div>
<script>
function sim5Inspect(item) {
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (item === 'blanket' && b.innerText.includes('Blanket')) ||
      (item === 'tree' && b.innerText.includes('Tree')) ||
      (item === 'lamp' && b.innerText.includes('Lantern')));
  });

  const cards = document.getElementById('sim5DilemmaCards');
  const verdict = document.getElementById('sim5Verdict');

  if (item === 'blanket') {
    cards.innerHTML = '<div style="flex:1; background:rgba(239,68,68,0.2); border:1px solid #ef4444; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">☀️</div><div style="font-size:13px; font-weight:bold; color:#f87171;">Share A: Day Blanket</div><div style="font-size:11px; color:#fecaca;">Blanket in hot daytime (Zero warmth utility)</div></div><div style="flex:1; background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">🌙</div><div style="font-size:13px; font-weight:bold; color:#34d399;">Share B: Night Blanket</div><div style="font-size:11px; color:#a7f3d0;">Blanket in freezing night (Vital essential utility)</div></div>';
    verdict.innerHTML = '❌ <span style="color:#f87171;">Unfair Time Share! True Fair Share: Alternate nights (Brother 1 on Mon/Wed, Brother 2 on Tue/Thu).</span>';
  } else if (item === 'tree') {
    cards.innerHTML = '<div style="flex:1; background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">🥭</div><div style="font-size:13px; font-weight:bold; color:#34d399;">Share A: Tree Top Canopy</div><div style="font-size:11px; color:#a7f3d0;">Harvests all ripe sweet mangoes</div></div><div style="flex:1; background:rgba(239,68,68,0.2); border:1px solid #ef4444; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">🪴</div><div style="font-size:13px; font-weight:bold; color:#f87171;">Share B: Tree Underground Roots</div><div style="font-size:11px; color:#fecaca;">Must water roots daily with zero fruit harvest</div></div>';
    verdict.innerHTML = '❌ <span style="color:#f87171;">Unfair Part Share! True Fair Share: Share both watering duty and mango harvest equally 50/50!</span>';
  } else {
    cards.innerHTML = '<div style="flex:1; background:rgba(239,68,68,0.2); border:1px solid #ef4444; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">☀️</div><div style="font-size:13px; font-weight:bold; color:#f87171;">Share A: Noon Sun Lantern</div><div style="font-size:11px; color:#fecaca;">Light is invisible during bright daytime</div></div><div style="flex:1; background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;"><div style="font-size:24px;">💡</div><div style="font-size:13px; font-weight:bold; color:#34d399;">Share B: Dark Night Lantern</div><div style="font-size:11px; color:#a7f3d0;">Illuminates dark home for reading & studying</div></div>';
    verdict.innerHTML = '❌ <span style="color:#f87171;">Unfair Utility! True Fair Share: Charge by day, place in shared study room by night!</span>';
  }
}
setTimeout(() => sim5Inspect('blanket'), 100);
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🥭 Discrete Object Fair Sharing Bowls</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Total Mangoes:</span>
      <button class="sim-btn" onclick="sim6Set(8)">8 Mangoes</button>
      <button class="sim-btn active" onclick="sim6Set(10)">10 Mangoes</button>
      <button class="sim-btn" onclick="sim6Set(14)">14 Mangoes</button>
      <button class="sim-btn" onclick="sim6DealStep()">Deal 1 Each</button>
      <button class="sim-btn" onclick="sim6Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; width:100%; max-width:620px; margin-bottom:12px;">
      <div style="font-size:13px; font-weight:bold; color:#cbd5e1;">Basket Stock: <span id="sim6Stock" style="color:#fbbf24; font-size:16px;">10</span> Mangoes Left</div>
      <div style="font-size:13px; font-weight:bold; color:#cbd5e1;">Dealt: <span id="sim6Dealt" style="color:#38bdf8; font-size:16px;">0</span> each</div>
    </div>
    <div style="display:flex; gap:20px; width:100%; max-width:620px; margin-bottom:14px;">
      <div style="flex:1; background:rgba(59,130,246,0.15); border:2px solid #3b82f6; border-radius:16px; padding:12px; text-align:center;">
        <div style="font-size:13px; font-weight:bold; color:#60a5fa;">Bowl A (Friend 1)</div>
        <div id="sim6BowlA" style="font-size:22px; min-height:36px; margin-top:6px;"></div>
      </div>
      <div style="flex:1; background:rgba(16,185,129,0.15); border:2px solid #10b981; border-radius:16px; padding:12px; text-align:center;">
        <div style="font-size:13px; font-weight:bold; color:#34d399;">Bowl B (Friend 2)</div>
        <div id="sim6BowlB" style="font-size:22px; min-height:36px; margin-top:6px;"></div>
      </div>
    </div>
    <div id="sim6Equation" style="font-size:18px; font-weight:bold; color:#f59e0b; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 20px;">
      Click 'Deal 1 Each' to share mangoes into equal halves!
    </div>
  </div>
</div>
<script>
let sim6Total = 10;
let sim6PerBowl = 0;

function sim6Set(n) {
  sim6Total = n;
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === n + ' Mangoes');
  });
  sim6Reset();
}
function sim6Reset() {
  sim6PerBowl = 0;
  sim6Render();
}
function sim6DealStep() {
  const left = sim6Total - (sim6PerBowl * 2);
  if (left >= 2) {
    sim6PerBowl++;
    sim6Render();
  }
}
function sim6Render() {
  const left = sim6Total - (sim6PerBowl * 2);
  document.getElementById('sim6Stock').innerText = left;
  document.getElementById('sim6Dealt').innerText = sim6PerBowl;

  let mangoes = '';
  for (let i = 0; i < sim6PerBowl; i++) mangoes += '🥭';
  document.getElementById('sim6BowlA').innerText = mangoes;
  document.getElementById('sim6BowlB').innerText = mangoes;

  const eq = document.getElementById('sim6Equation');
  if (left === 0) {
    eq.innerHTML = '🎉 Fair Sharing Complete: ' + sim6Total + ' ÷ 2 = <span style="color:#34d399;">' + sim6PerBowl + ' Mangoes Each (Half of ' + sim6Total + ')</span>';
  } else {
    eq.innerText = sim6Total + ' Total Mangoes ➔ Current: ' + sim6PerBowl + ' in each bowl (' + left + ' left in basket)';
  }
}
setTimeout(sim6Reset, 100);
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">⚖️ Reciprocal Halves & Doubles Balancer</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Base Number:</span>
      <button class="sim-btn" onclick="sim7Set(3)">3</button>
      <button class="sim-btn" onclick="sim7Set(4)">4</button>
      <button class="sim-btn active" onclick="sim7Set(5)">5</button>
      <button class="sim-btn" onclick="sim7Set(6)">6</button>
      <button class="sim-btn" onclick="sim7Set(7)">7</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-around; width:100%; max-width:620px; margin-bottom:14px; gap:12px;">
      <div style="flex:1; background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#60a5fa;">🔵 Doubling Operation</div>
        <div id="sim7DoubleMath" style="font-size:22px; font-weight:bold; color:#fff; margin-top:6px;">5 × 2 = 10</div>
        <div style="font-size:11px; color:#93c5fd; margin-top:2px;">(10 is double of 5)</div>
      </div>
      <div style="flex:1; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#34d399;">🟢 Halving Operation</div>
        <div id="sim7HalfMath" style="font-size:22px; font-weight:bold; color:#fff; margin-top:6px;">10 ÷ 2 = 5</div>
        <div style="font-size:11px; color:#a7f3d0; margin-top:2px;">(5 is half of 10)</div>
      </div>
    </div>
    <div id="sim7ReciprocalRule" style="font-size:16px; font-weight:bold; color:#fbbf24; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:8px 24px; text-align:center;">
      Reciprocal Law: 5 is half of 10, and 10 is double of 5!
    </div>
  </div>
</div>
<script>
let sim7Val = 5;

function sim7Set(n) {
  sim7Val = n;
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === '' + n);
  });
  sim7Render();
}
function sim7Render() {
  const dbl = sim7Val * 2;
  document.getElementById('sim7DoubleMath').innerText = sim7Val + ' × 2 = ' + dbl;
  document.getElementById('sim7HalfMath').innerText = dbl + ' ÷ 2 = ' + sim7Val;
  document.getElementById('sim7ReciprocalRule').innerHTML = 'Reciprocal Law: <span style="color:#fff;">' + sim7Val + ' is half of ' + dbl + '</span>, and <span style="color:#fff;">' + dbl + ' is double of ' + sim7Val + '</span>!';
}
setTimeout(sim7Render, 100);
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">📍 Number Line Midpoint & Double Distance Marker</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Target Landmark:</span>
      <button class="sim-btn" onclick="sim8Set(8)">8 Units</button>
      <button class="sim-btn" onclick="sim8Set(12)">12 Units</button>
      <button class="sim-btn active" onclick="sim8Set(16)">16 Units</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim8Line" style="display:flex; flex-wrap:wrap; gap:4px; justify-content:center; max-width:650px; margin-bottom:14px;">
      <!-- Stones 0 to 18 -->
    </div>
    <div id="sim8Equation" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Halfway landmark: 8 is half of 16 (16 ÷ 2 = 8).
    </div>
  </div>
</div>
<script>
let sim8Target = 16;

function sim8Set(t) {
  sim8Target = t;
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === t + ' Units');
  });
  sim8Render();
}
function sim8Render() {
  const line = document.getElementById('sim8Line');
  line.innerHTML = '';
  const mid = sim8Target / 2;

  for (let i = 0; i <= 18; i++) {
    let bg = 'rgba(255,255,255,0.06)';
    let border = 'rgba(255,255,255,0.15)';
    let color = '#94a3b8';
    let label = '';

    if (i === 0) {
      bg = '#334155'; border = '#64748b'; color = '#fff'; label = 'Start';
    } else if (i === mid) {
      bg = '#0284c7'; border = '#38bdf8'; color = '#fff'; label = 'Half';
    } else if (i === sim8Target) {
      bg = '#059669'; border = '#34d399'; color = '#fff'; label = 'Whole';
    }

    let box = '<div style="width:30px; height:36px; border-radius:6px; background:' + bg + '; border:1.5px solid ' + border + '; display:flex; flex-direction:column; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:' + color + ';">';
    box += '<span>' + i + '</span>';
    if (label) box += '<span style="font-size:8px; line-height:1; color:#f59e0b;">' + label + '</span>';
    box += '</div>';
    line.innerHTML += box;
  }

  document.getElementById('sim8Equation').innerHTML = 'Distance 0 to ' + sim8Target + ': Exact Halfway Midpoint is <span style="color:#38bdf8;">' + mid + '</span> (Half of ' + sim8Target + ' is ' + mid + ')';
}
setTimeout(sim8Render, 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Sims 1-8).")

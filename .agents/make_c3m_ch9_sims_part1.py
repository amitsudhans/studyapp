#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">👑 Royal Courtyard Crow Flock Place Value Counter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Preset(963)">963 (Royal Count)</button>
      <button class="sim-btn" onclick="sim1Preset(845)">845 Crows</button>
      <button class="sim-btn" onclick="sim1Preset(720)">720 Crows</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:center; gap:16px; width:100%; max-width:640px; margin-bottom:14px;">
      <div style="flex:1; background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#60a5fa;">Hundreds (×100)</div>
        <div id="sim1H" style="font-size:26px; font-weight:bold; color:#fff; margin-top:4px;">9</div>
        <div id="sim1HVal" style="font-size:12px; color:#93c5fd; font-weight:600;">900 Units</div>
      </div>
      <div style="flex:1; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#fbbf24;">Tens (×10)</div>
        <div id="sim1T" style="font-size:26px; font-weight:bold; color:#fff; margin-top:4px;">6</div>
        <div id="sim1TVal" style="font-size:12px; color:#fde68a; font-weight:600;">60 Units</div>
      </div>
      <div style="flex:1; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#34d399;">Ones (×1)</div>
        <div id="sim1O" style="font-size:26px; font-weight:bold; color:#fff; margin-top:4px;">3</div>
        <div id="sim1OVal" style="font-size:12px; color:#a7f3d0; font-weight:600;">3 Units</div>
      </div>
    </div>
    <div id="sim1Expanded" style="font-size:20px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Expanded Form: 900 + 60 + 3 = 963 Crows
    </div>
  </div>
</div>
<script>
function sim1Preset(val) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + val));
  });

  const h = Math.floor(val / 100);
  const t = Math.floor((val % 100) / 10);
  const o = val % 10;

  document.getElementById('sim1H').innerText = h;
  document.getElementById('sim1HVal').innerText = (h * 100) + ' Units';
  document.getElementById('sim1T').innerText = t;
  document.getElementById('sim1TVal').innerText = (t * 10) + ' Units';
  document.getElementById('sim1O').innerText = o;
  document.getElementById('sim1OVal').innerText = o + ' Units';

  document.getElementById('sim1Expanded').innerHTML = 'Expanded Form: <span style="color:#fbbf24;">' + (h * 100) + ' + ' + (t * 10) + ' + ' + o + ' = ' + val + ' Crows</span>';
}
setTimeout(() => sim1Preset(963), 100);
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">📦 Rice Sack Inventory Place Value Tiles</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2Show(832)">832 Sacks</button>
      <button class="sim-btn" onclick="sim2Show(504)">504 (Zero Tens)</button>
      <button class="sim-btn" onclick="sim2Show(726)">726 Sacks</button>
      <button class="sim-btn" onclick="sim2Show(620)">620 (Zero Ones)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim2TileDisplay" style="display:flex; justify-content:center; gap:20px; width:100%; max-width:650px; margin-bottom:14px; min-height:100px; align-items:center;">
      <!-- Tiles -->
    </div>
    <div id="sim2Equation" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      8 Hundred Flats + 3 Ten Rods + 2 Unit Tiles = 832 Rice Sacks
    </div>
  </div>
</div>
<script>
function sim2Show(val) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + val));
  });

  const h = Math.floor(val / 100);
  const t = Math.floor((val % 100) / 10);
  const o = val % 10;

  const disp = document.getElementById('sim2TileDisplay');
  disp.innerHTML = '';

  // Hundreds Flats
  let hHtml = '<div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:10px; padding:8px; text-align:center;"><div style="font-size:11px; font-weight:bold; color:#60a5fa; margin-bottom:4px;">' + h + ' Hundred Flats</div><div style="display:flex; flex-wrap:wrap; gap:3px; max-width:140px; justify-content:center;">';
  for (let i = 0; i < h; i++) hHtml += '<div style="width:26px; height:26px; background:#3b82f6; border:1px solid #fff; border-radius:3px;" title="100"></div>';
  hHtml += '</div></div>';
  disp.innerHTML += hHtml;

  // Tens Rods
  let tHtml = '<div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:10px; padding:8px; text-align:center;"><div style="font-size:11px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">' + t + ' Ten Rods</div><div style="display:flex; gap:3px; justify-content:center;">';
  if (t === 0) tHtml += '<div style="font-size:11px; color:#94a3b8; font-style:italic; padding:10px;">None (0)</div>';
  else {
    for (let i = 0; i < t; i++) tHtml += '<div style="width:8px; height:36px; background:#f59e0b; border:1px solid #fff; border-radius:2px;" title="10"></div>';
  }
  tHtml += '</div></div>';
  disp.innerHTML += tHtml;

  // Unit Tiles
  let oHtml = '<div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:8px; text-align:center;"><div style="font-size:11px; font-weight:bold; color:#34d399; margin-bottom:4px;">' + o + ' Unit Tiles</div><div style="display:flex; flex-wrap:wrap; gap:3px; max-width:60px; justify-content:center;">';
  if (o === 0) oHtml += '<div style="font-size:11px; color:#94a3b8; font-style:italic; padding:10px;">None (0)</div>';
  else {
    for (let i = 0; i < o; i++) oHtml += '<div style="width:8px; height:8px; background:#10b981; border:1px solid #fff; border-radius:1px;" title="1"></div>';
  }
  oHtml += '</div></div>';
  disp.innerHTML += oHtml;

  document.getElementById('sim2Equation').innerHTML = h + ' Hundreds (' + (h*100) + ') + ' + t + ' Tens (' + (t*10) + ') + ' + o + ' Units (' + o + ') = <span style="color:#fbbf24;">' + val + ' Sacks</span>';
}
setTimeout(() => sim2Show(832), 100);
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">📍 Extended Number Line Benchmark Navigator (500–900)</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Target Pin:</span>
      <button class="sim-btn" onclick="sim3Pin(530)">530</button>
      <button class="sim-btn active" onclick="sim3Pin(628)">628</button>
      <button class="sim-btn" onclick="sim3Pin(703)">703</button>
      <button class="sim-btn" onclick="sim3Pin(855)">855</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim3Track" style="position:relative; width:100%; max-width:620px; height:80px; margin-bottom:14px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); display:flex; align-items:center; padding:0 30px;">
      <!-- Coordinate line with pins -->
      <div style="position:absolute; left:30px; right:30px; height:4px; background:#475569; border-radius:2px;"></div>
      <div id="sim3PinMarker" style="position:absolute; top:12px; transform:translateX(-50%); display:flex; flex-direction:column; align-items:center; transition:left 0.4s ease;">
        <span style="font-size:18px;">🚩</span>
        <span id="sim3PinText" style="font-size:11px; font-weight:bold; color:#fbbf24; background:#1e293b; padding:1px 6px; border-radius:4px; border:1px solid #f59e0b;">628</span>
      </div>
      <!-- Milestones -->
      <div style="position:absolute; left:30px; bottom:14px; transform:translateX(-50%); font-size:11px; font-weight:bold; color:#94a3b8;">500</div>
      <div style="position:absolute; left:25%; bottom:14px; transform:translateX(-50%); font-size:11px; font-weight:bold; color:#94a3b8;">600</div>
      <div style="position:absolute; left:50%; bottom:14px; transform:translateX(-50%); font-size:11px; font-weight:bold; color:#94a3b8;">700</div>
      <div style="position:absolute; left:75%; bottom:14px; transform:translateX(-50%); font-size:11px; font-weight:bold; color:#94a3b8;">800</div>
      <div style="position:absolute; right:30px; bottom:14px; transform:translateX(50%); font-size:11px; font-weight:bold; color:#94a3b8;">900</div>
    </div>
    <div id="sim3Analysis" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      628 sits between 600 and 700 (Closer to 600 than 700).
    </div>
  </div>
</div>
<script>
function sim3Pin(val) {
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === '' + val);
  });

  // Scale: 500 = 0% of inner track, 900 = 100%
  const pct = ((val - 500) / 400) * 100;
  const pin = document.getElementById('sim3PinMarker');
  pin.style.left = 'calc(30px + ' + pct + ' * (100% - 60px) / 100)';
  document.getElementById('sim3PinText').innerText = val;

  const lowerH = Math.floor(val / 100) * 100;
  const upperH = lowerH + 100;
  const mid = lowerH + 50;
  const closer = (val < mid) ? lowerH : upperH;

  document.getElementById('sim3Analysis').innerHTML = val + ' lies between <span style="color:#fbbf24;">' + lowerH + ' and ' + upperH + '</span> (Midpoint ' + mid + ', closer to ' + closer + ')';
}
setTimeout(() => sim3Pin(628), 100);
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">📊 Multi-Scale Rounding Boundary Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4Inspect(468)">468</button>
      <button class="sim-btn" onclick="sim4Inspect(183)">183</button>
      <button class="sim-btn" onclick="sim4Inspect(899)">899</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; flex-direction:column; gap:10px; width:100%; max-width:620px; margin-bottom:12px;">
      <div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; border-radius:10px; padding:10px 16px; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-weight:bold; color:#60a5fa; font-size:13px;">Neighboring Tens (±10):</span>
        <span id="sim4Tens" style="font-weight:bold; color:#fff; font-size:16px;">460 &lt; 468 &lt; 470</span>
      </div>
      <div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:10px; padding:10px 16px; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-weight:bold; color:#fbbf24; font-size:13px;">Neighboring Fifties (±50):</span>
        <span id="sim4Fifties" style="font-weight:bold; color:#fff; font-size:16px;">450 &lt; 468 &lt; 500</span>
      </div>
      <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:10px 16px; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-weight:bold; color:#34d399; font-size:13px;">Neighboring Hundreds (±100):</span>
        <span id="sim4Hundreds" style="font-weight:bold; color:#fff; font-size:16px;">400 &lt; 468 &lt; 500</span>
      </div>
    </div>
    <div id="sim4RoundingVerdict" style="font-size:16px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Closest Hundred: 500 (Since 68 ≥ 50, it rounds UP toward 500!)
    </div>
  </div>
</div>
<script>
function sim4Inspect(val) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === '' + val);
  });

  const lowT = Math.floor(val / 10) * 10;
  const upT = lowT + 10;
  const lowF = Math.floor(val / 50) * 50;
  const upF = lowF + 50;
  const lowH = Math.floor(val / 100) * 100;
  const upH = lowH + 100;

  document.getElementById('sim4Tens').innerText = lowT + ' < ' + val + ' < ' + upT;
  document.getElementById('sim4Fifties').innerText = lowF + ' < ' + val + ' < ' + upF;
  document.getElementById('sim4Hundreds').innerText = lowH + ' < ' + val + ' < ' + upH;

  const closestH = (val - lowH >= 50) ? upH : lowH;
  document.getElementById('sim4RoundingVerdict').innerHTML = 'Closest Hundred: <span style="color:#fff;">' + closestH + '</span> (Difference = ' + Math.abs(val - closestH) + ' units)';
}
setTimeout(() => sim4Inspect(468), 100);
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🦩 Riverbank Crane Food Hunt Step Puzzle</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5Select('crane1')">Crane 1: 650 to 700 (Step 10)</button>
      <button class="sim-btn" onclick="sim5Select('crane2')">Crane 2: 750 to 800 (Step 25)</button>
      <button class="sim-btn" onclick="sim5Hop()">Hop Next Step</button>
      <button class="sim-btn" onclick="sim5Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim5Stones" style="display:flex; gap:8px; justify-content:center; max-width:620px; margin-bottom:14px; flex-wrap:wrap;">
      <!-- Stepping stones -->
    </div>
    <div id="sim5Progress" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Click 'Hop Next Step' to guide the crane toward food!
    </div>
  </div>
</div>
<script>
let sim5Mode = 'crane1';
let sim5CurrentHop = 0;

function sim5Select(m) {
  sim5Mode = m;
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (m === 'crane1' && b.innerText.includes('Crane 1')) ||
      (m === 'crane2' && b.innerText.includes('Crane 2')));
  });
  sim5Reset();
}
function sim5Reset() {
  sim5CurrentHop = 0;
  sim5Render();
}
function sim5Hop() {
  const maxHops = (sim5Mode === 'crane1') ? 5 : 2;
  if (sim5CurrentHop < maxHops) {
    sim5CurrentHop++;
    sim5Render();
  }
}
function sim5Render() {
  const container = document.getElementById('sim5Stones');
  container.innerHTML = '';
  const isCrane1 = (sim5Mode === 'crane1');
  const start = isCrane1 ? 650 : 750;
  const step = isCrane1 ? 10 : 25;
  const totalHops = isCrane1 ? 5 : 2;
  const target = start + (totalHops * step);

  for (let h = 0; h <= totalHops; h++) {
    const val = start + (h * step);
    const isCraneHere = (h === sim5CurrentHop);
    const isTarget = (h === totalHops);

    let bg = 'rgba(255,255,255,0.08)';
    let border = 'rgba(255,255,255,0.2)';
    let color = '#cbd5e1';

    if (isCraneHere) {
      bg = '#0284c7'; border = '#38bdf8'; color = '#fff';
    } else if (h < sim5CurrentHop) {
      bg = 'rgba(16,185,129,0.2)'; border = '#10b981'; color = '#6ee7b7';
    }

    let stone = '<div style="background:' + bg + '; border:2px solid ' + border + '; border-radius:12px; padding:8px 12px; text-align:center; min-width:64px; position:relative;">';
    if (isCraneHere) stone += '<div style="position:absolute; top:-20px; left:50%; transform:translateX(-50%); font-size:18px;">🦩</div>';
    else if (isTarget) stone += '<div style="position:absolute; top:-20px; left:50%; transform:translateX(-50%); font-size:16px;">🐟</div>';
    stone += '<div style="font-size:13px; font-weight:bold; color:' + color + ';">' + val + '</div>';
    stone += '</div>';
    container.innerHTML += stone;
  }

  const prog = document.getElementById('sim5Progress');
  const currentPos = start + (sim5CurrentHop * step);
  if (sim5CurrentHop === totalHops) {
    prog.innerHTML = '🎉 <span style="color:#34d399;">Target Reached! ' + totalHops + ' hops of ' + step + ' units bridged ' + start + ' to ' + target + '!</span>';
  } else {
    prog.innerText = 'Current Position: ' + currentPos + ' (' + sim5CurrentHop + ' / ' + totalHops + ' hops completed)';
  }
}
setTimeout(sim5Reset, 100);
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🎟️ Tambola Grid Math Clue Game (570–630)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Clue(1)">Clue 1: 6H 0T 5O</button>
      <button class="sim-btn" onclick="sim6Clue(2)">Clue 2: 5 more than 590</button>
      <button class="sim-btn" onclick="sim6Clue(3)">Clue 3: 10 less than 620</button>
      <button class="sim-btn" onclick="sim6Solve()">Strike Out Number</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim6ClueBanner" style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 18px;">
      Caller Clue: "I have 6 hundreds, 0 tens, and 5 loose ones. Who am I?"
    </div>
    <div id="sim6Grid" style="display:grid; grid-template-columns:repeat(6, 44px); gap:6px; margin-bottom:12px;">
      <!-- Grid numbers -->
    </div>
    <div id="sim6Feedback" style="font-size:16px; font-weight:bold; color:#34d399;">
      Click 'Strike Out Number' to claim the winning cell!
    </div>
  </div>
</div>
<script>
let sim6Current = 1;
const sim6Numbers = [570, 580, 590, 595, 600, 605, 610, 615, 620, 625, 630];
const sim6Answers = { 1: 605, 2: 595, 3: 610 };
const sim6ClueTexts = {
  1: 'Caller Clue: "I have 6 hundreds, 0 tens, and 5 loose ones. Who am I?"',
  2: 'Caller Clue: "I am exactly 5 more than 590. Who am I?"',
  3: 'Caller Clue: "I am exactly 10 less than 620. Who am I?"'
};

function sim6Clue(idx) {
  sim6Current = idx;
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('Clue ' + idx));
  });
  document.getElementById('sim6ClueBanner').innerText = sim6ClueTexts[idx];
  document.getElementById('sim6Feedback').innerText = 'Click \'Strike Out Number\' to claim the winning cell!';
  sim6RenderGrid(false);
}

function sim6Solve() {
  const ans = sim6Answers[sim6Current];
  document.getElementById('sim6Feedback').innerHTML = '🎉 Strike Out! Winning cell: <span style="color:#fbbf24;">' + ans + '</span>';
  sim6RenderGrid(true);
}

function sim6RenderGrid(highlight) {
  const grid = document.getElementById('sim6Grid');
  grid.innerHTML = '';
  const target = sim6Answers[sim6Current];

  sim6Numbers.forEach(n => {
    const isTarget = (n === target && highlight);
    let bg = isTarget ? '#f59e0b' : 'rgba(255,255,255,0.08)';
    let color = isTarget ? '#0f172a' : '#cbd5e1';
    let border = isTarget ? '#fbbf24' : 'rgba(255,255,255,0.15)';
    grid.innerHTML += '<div style="background:' + bg + '; border:1.5px solid ' + border + '; border-radius:6px; height:34px; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:' + color + ';">' + n + '</div>';
  });
}
setTimeout(() => sim6Clue(1), 100);
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🎭 Multiple Representation Equation Costume Studio</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Select(368)">368</button>
      <button class="sim-btn" onclick="sim7Select(905)">905</button>
      <button class="sim-btn" onclick="sim7Select(555)">555</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim7CardGrid" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px; width:100%; max-width:620px; margin-bottom:12px;">
      <!-- 4 expressions -->
    </div>
    <div style="font-size:14px; font-weight:bold; color:#a7f3d0; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 20px;">
      Additive & Subtractive Invariance: A number stays identical across all representations!
    </div>
  </div>
</div>
<script>
const sim7Data = {
  368: [
    { title: 'Standard Expanded', eq: '300 + 60 + 8 = 368' },
    { title: 'Decade Bundle Split', eq: '350 + 18 = 368' },
    { title: 'Hundreds Separation', eq: '200 + 168 = 368' },
    { title: 'Subtractive Form', eq: '400 - 32 = 368' }
  ],
  905: [
    { title: 'Standard Expanded', eq: '900 + 0 + 5 = 905' },
    { title: 'Tens & Ones Mix', eq: '850 + 55 = 905' },
    { title: 'Half-Century Base', eq: '800 + 105 = 905' },
    { title: 'Subtractive Form', eq: '1000 - 95 = 905' }
  ],
  555: [
    { title: 'Triplet Expanded', eq: '500 + 50 + 5 = 555' },
    { title: 'Two-Piece Split', eq: '500 + 55 = 555' },
    { title: 'Century Offset', eq: '400 + 155 = 555' },
    { title: 'Subtractive Form', eq: '600 - 45 = 555' }
  ]
};

function sim7Select(num) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText === '' + num);
  });

  const grid = document.getElementById('sim7CardGrid');
  grid.innerHTML = '';
  sim7Data[num].forEach(item => {
    grid.innerHTML += '<div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 12px; text-align:center;"><div style="font-size:11px; font-weight:bold; color:#94a3b8; margin-bottom:2px;">' + item.title + '</div><div style="font-size:15px; font-weight:bold; color:#38bdf8;">' + item.eq + '</div></div>';
  });
}
setTimeout(() => sim7Select(368), 100);
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🏃 Stepping Stone Pattern Trail Solver</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Pattern('p25')">Skip +25 Trail</button>
      <button class="sim-btn" onclick="sim8Pattern('p10')">Skip +10 Trail</button>
      <button class="sim-btn" onclick="sim8Pattern('p15')">Skip +15 Trail</button>
      <button class="sim-btn" onclick="sim8Reveal()">Fill Blank Stone</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim8Stones" style="display:flex; gap:8px; justify-content:center; max-width:620px; margin-bottom:14px; flex-wrap:wrap;">
      <!-- Trail stones -->
    </div>
    <div id="sim8Rule" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Pattern Rule: Add +25 at each step!
    </div>
  </div>
</div>
<script>
let sim8Type = 'p25';
let sim8Revealed = false;
const sim8Data = {
  p25: { stones: [600, 625, 650, 675, 700], blankIdx: 3, rule: 'Pattern Rule: Constant step of +25 (650 + 25 = 675)' },
  p10: { stones: [510, 520, 530, 540, 550], blankIdx: 3, rule: 'Pattern Rule: Constant step of +10 (530 + 10 = 540)' },
  p15: { stones: [700, 715, 730, 745, 760], blankIdx: 3, rule: 'Pattern Rule: Constant step of +15 (730 + 15 = 745)' }
};

function sim8Pattern(type) {
  sim8Type = type;
  sim8Revealed = false;
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (type === 'p25' && b.innerText.includes('+25')) ||
      (type === 'p10' && b.innerText.includes('+10')) ||
      (type === 'p15' && b.innerText.includes('+15')));
  });
  sim8Render();
}
function sim8Reveal() {
  sim8Revealed = true;
  sim8Render();
}
function sim8Render() {
  const d = sim8Data[sim8Type];
  const container = document.getElementById('sim8Stones');
  container.innerHTML = '';

  d.stones.forEach((s, idx) => {
    const isBlank = (idx === d.blankIdx);
    let text = s;
    let bg = 'rgba(255,255,255,0.08)';
    let border = 'rgba(255,255,255,0.2)';
    let color = '#fff';

    if (isBlank && !sim8Revealed) {
      text = '?';
      bg = '#d97706'; border = '#fbbf24'; color = '#fff';
    } else if (isBlank && sim8Revealed) {
      bg = '#059669'; border = '#34d399'; color = '#fff';
    }

    container.innerHTML += '<div style="background:' + bg + '; border:2px solid ' + border + '; border-radius:10px; width:56px; height:48px; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:bold; color:' + color + ';">' + text + '</div>';
  });

  const ruleEl = document.getElementById('sim8Rule');
  if (sim8Revealed) {
    ruleEl.innerHTML = '🎉 <span style="color:#34d399;">' + d.rule + '</span>';
  } else {
    ruleEl.innerText = 'Determine step interval and click \'Fill Blank Stone\'!';
  }
}
setTimeout(() => sim8Pattern('p25'), 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Sims 1-8).")

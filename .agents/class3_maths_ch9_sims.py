#!/usr/bin/env python3
"""NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II Simulators"""

simulators = {
    1: '''
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
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
  document.getElementById('sim6Feedback').innerText = 'Click 'Strike Out Number' to claim the winning cell!';
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
''',
    7: '''
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
''',
    8: '''
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
    ruleEl.innerText = 'Determine step interval and click 'Fill Blank Stone'!';
  }
}
setTimeout(() => sim8Pattern('p25'), 100);
</script>
''',
    9: '''
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">⚖️ Visual Balance Scale Equation Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Target(400)">Target 400</button>
      <button class="sim-btn" onclick="sim9Target(775)">Target 775</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; max-width:620px; margin-bottom:14px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:14px; padding:16px;">
      <div style="flex:1; text-align:center; border-right:1px solid rgba(255,255,255,0.1); padding-right:12px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold; text-transform:uppercase;">Left Pan (Fixed Target)</div>
        <div id="sim9TargetVal" style="font-size:32px; font-weight:bold; color:#38bdf8; margin-top:4px;">400</div>
      </div>
      <div style="padding:0 12px; font-size:24px; font-weight:bold; color:#f59e0b;" id="sim9BalanceIcon">⚖️</div>
      <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.1); padding-left:12px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold; text-transform:uppercase;">Right Pan (Expression)</div>
        <div id="sim9ExprVal" style="font-size:24px; font-weight:bold; color:#a7f3d0; margin-top:4px;">200 + 200</div>
      </div>
    </div>
    <div id="sim9Options" style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; max-width:620px; margin-bottom:12px;">
      <!-- Buttons dynamically populated -->
    </div>
    <div id="sim9Verdict" style="font-size:16px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 18px; text-align:center;">
      Perfect Balance! 200 + 200 = 400
    </div>
  </div>
</div>
<script>
let sim9CurrentTarget = 400;
const sim9Data = {
  400: [
    { expr: '200 + 200', val: 400, correct: true },
    { expr: '500 - 100', val: 400, correct: true },
    { expr: '350 + 50', val: 400, correct: true },
    { expr: '450 - 50', val: 400, correct: true },
    { expr: '300 + 80', val: 380, correct: false },
    { expr: '600 - 150', val: 450, correct: false }
  ],
  775: [
    { expr: '700 + 75', val: 775, correct: true },
    { expr: '800 - 25', val: 775, correct: true },
    { expr: '750 + 25', val: 775, correct: true },
    { expr: '1000 - 225', val: 775, correct: true },
    { expr: '700 + 85', val: 785, correct: false },
    { expr: '800 - 35', val: 765, correct: false }
  ]
};

function sim9Target(target) {
  sim9CurrentTarget = target;
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('' + target));
  });
  document.getElementById('sim9TargetVal').innerText = target;

  const container = document.getElementById('sim9Options');
  container.innerHTML = '';
  sim9Data[target].forEach((item, idx) => {
    const btn = document.createElement('button');
    btn.className = 'sim-btn' + (idx === 0 ? ' active' : '');
    btn.innerText = item.expr;
    btn.onclick = () => sim9SelectExpr(item, btn);
    container.appendChild(btn);
  });
  sim9SelectExpr(sim9Data[target][0], container.firstChild);
}

function sim9SelectExpr(item, btn) {
  document.querySelectorAll('#sim9Options button').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  document.getElementById('sim9ExprVal').innerText = item.expr;
  const verdict = document.getElementById('sim9Verdict');
  const icon = document.getElementById('sim9BalanceIcon');

  if (item.val === sim9CurrentTarget) {
    icon.innerText = '⚖️ (Balanced)';
    verdict.style.color = '#34d399';
    verdict.style.background = 'rgba(16,185,129,0.15)';
    verdict.style.borderColor = '#10b981';
    verdict.innerText = '✨ Perfect Balance! ' + item.expr + ' = ' + item.val;
  } else if (item.val < sim9CurrentTarget) {
    icon.innerText = '↙️ (Right Under)';
    verdict.style.color = '#fbbf24';
    verdict.style.background = 'rgba(245,158,11,0.15)';
    verdict.style.borderColor = '#f59e0b';
    verdict.innerText = '⚠️ Unbalanced! ' + item.expr + ' = ' + item.val + ' (Too Low by ' + (sim9CurrentTarget - item.val) + ')';
  } else {
    icon.innerText = '↘️ (Right Over)';
    verdict.style.color = '#f87171';
    verdict.style.background = 'rgba(239,68,68,0.15)';
    verdict.style.borderColor = '#ef4444';
    verdict.innerText = '⚠️ Unbalanced! ' + item.expr + ' = ' + item.val + ' (Too High by ' + (item.val - sim9CurrentTarget) + ')';
  }
}
setTimeout(() => sim9Target(400), 100);
</script>
''',
    10: '''
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">📊 Real-World Magnitude Estimation Sorter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Pick(0)">Classroom Kids</button>
      <button class="sim-btn" onclick="sim10Pick(1)">Fingers & Toes</button>
      <button class="sim-btn" onclick="sim10Pick(2)">Truck Rice Sacks</button>
      <button class="sim-btn" onclick="sim10Pick(3)">Night Sky Stars</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim10Prompt" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 20px; text-align:center;">
      Item: "Number of students in a typical school classroom"
    </div>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; width:100%; max-width:620px; margin-bottom:12px;">
      <button class="sim-btn" id="sim10Bin0" onclick="sim10Guess(0)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#60a5fa;">&lt; 10</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Single Digits</div>
      </button>
      <button class="sim-btn" id="sim10Bin1" onclick="sim10Guess(1)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#34d399;">10 – 100</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Tens Range</div>
      </button>
      <button class="sim-btn" id="sim10Bin2" onclick="sim10Guess(2)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#fbbf24;">100 – 1,000</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Hundreds Range</div>
      </button>
      <button class="sim-btn" id="sim10Bin3" onclick="sim10Guess(3)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#f87171;">&gt; 1,000</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Thousands+</div>
      </button>
    </div>
    <div id="sim10Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; text-align:center;">
      Click a magnitude bin above to categorize this real-world quantity!
    </div>
  </div>
</div>
<script>
let sim10Cur = 0;
const sim10Items = [
  { name: 'Number of students in a typical school classroom', bin: 1, explanation: 'A classroom usually has 30 to 45 students, which falls between 10 and 100!' },
  { name: 'Total fingers and toes on one human person', bin: 1, explanation: 'A person has 10 fingers and 10 toes, totaling 20 (between 10 and 100)!' },
  { name: 'Sacks of grains loaded into a large cargo transport truck', bin: 2, explanation: 'A large cargo truck carries hundreds of sacks (typically 200 to 800 sacks)!' },
  { name: 'Visible stars twinkling in a clear midnight sky', bin: 3, explanation: 'Stars visible on a clear night stretch into many thousands and millions!' }
];

function sim10Pick(idx) {
  sim10Cur = idx;
  document.querySelectorAll('#sim10 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  document.getElementById('sim10Prompt').innerText = 'Item: "' + sim10Items[idx].name + '"';
  document.getElementById('sim10Feedback').innerText = 'Click a magnitude bin above to categorize this real-world quantity!';
  document.querySelectorAll('#sim10 [id^=sim10Bin]').forEach(b => {
    b.style.borderColor = '';
    b.style.background = '';
  });
}

function sim10Guess(binIdx) {
  const item = sim10Items[sim10Cur];
  const fb = document.getElementById('sim10Feedback');
  const clickedBtn = document.getElementById('sim10Bin' + binIdx);

  if (binIdx === item.bin) {
    clickedBtn.style.borderColor = '#10b981';
    clickedBtn.style.background = 'rgba(16,185,129,0.2)';
    fb.innerHTML = '🎉 <span style="color:#34d399;">Correct!</span> ' + item.explanation;
  } else {
    clickedBtn.style.borderColor = '#ef4444';
    clickedBtn.style.background = 'rgba(239,68,68,0.2)';
    fb.innerHTML = '❌ <span style="color:#f87171;">Try again!</span> Think about whether this is less than 10, in tens, in hundreds, or thousands.';
  }
}
setTimeout(() => sim10Pick(0), 100);
</script>
''',
    11: '''
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🧩 Century & Half-Century Riddle Solver</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Select(1)">Century + Half</button>
      <button class="sim-btn" onclick="sim11Select(2)">Double Century - 10</button>
      <button class="sim-btn" onclick="sim11Select(3)">Triple + 25</button>
      <button class="sim-btn" onclick="sim11Select(4)">Mid 400 & 500</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim11Clue" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:8px;">
        "I am a century plus a half century. Who am I?"
      </div>
      <div id="sim11AnswerBox" style="font-size:26px; font-weight:bold; color:#38bdf8;">
        ?
      </div>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="sim-btn active" onclick="sim11Reveal()" style="padding:8px 20px;">💡 Reveal Step-by-Step Breakdown</button>
    </div>
    <div id="sim11Reasoning" style="font-size:14px; color:#a7f3d0; font-weight:600; margin-top:10px; text-align:center;">
      Click the button above to unpack the riddle's number terms!
    </div>
  </div>
</div>
<script>
let sim11Cur = 1;
const sim11Data = {
  1: { clue: '"I am a century plus a half century. Who am I?"', ans: '150', reason: 'Term Breakdown: Century = 100. Half Century = 50. Total = 100 + 50 = 150!' },
  2: { clue: '"I am double century minus 10. Who am I?"', ans: '190', reason: 'Term Breakdown: Double Century = 2 × 100 = 200. Minus 10 = 200 - 10 = 190!' },
  3: { clue: '"I am triple century plus twenty-five. Who am I?"', ans: '325', reason: 'Term Breakdown: Triple Century = 300. Add 25 = 300 + 25 = 325!' },
  4: { clue: '"I am the exact middle number between 400 and 500. Who am I?"', ans: '450', reason: 'Term Breakdown: Distance between 400 and 500 is 100. Halfway point = 400 + 50 = 450!' }
};

function sim11Select(idx) {
  sim11Cur = idx;
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(idx === 1 ? 'Century + Half' : idx === 2 ? 'Double Century' : idx === 3 ? 'Triple' : 'Mid'));
  });
  document.getElementById('sim11Clue').innerText = sim11Data[idx].clue;
  document.getElementById('sim11AnswerBox').innerText = '?';
  document.getElementById('sim11Reasoning').innerText = 'Click the button above to unpack the riddle's number terms!';
}

function sim11Reveal() {
  const item = sim11Data[sim11Cur];
  document.getElementById('sim11AnswerBox').innerHTML = '<span style="color:#34d399;">' + item.ans + '</span>';
  document.getElementById('sim11Reasoning').innerHTML = '🎯 ' + item.reason;
}
setTimeout(() => sim11Select(1), 100);
</script>
''',
    12: '''
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🔍 Special Sequence & Pattern Detector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Select('stepUp')">Step-Up</button>
      <button class="sim-btn" onclick="sim12Select('stepDown')">Step-Down</button>
      <button class="sim-btn" onclick="sim12Select('triplets')">Triplets</button>
      <button class="sim-btn" onclick="sim12Select('mirrors')">Palindromes</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim12Display" style="display:flex; gap:10px; justify-content:center; max-width:620px; margin-bottom:14px; flex-wrap:wrap;">
      <!-- Populated by JS -->
    </div>
    <div id="sim12RuleCard" style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:12px 20px; width:100%; max-width:620px; text-align:center;">
      <div id="sim12RuleTitle" style="font-size:16px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">Consecutive Step-Up Pattern</div>
      <div id="sim12RuleDesc" style="font-size:13px; color:#cbd5e1;">Each consecutive digit increases by exactly 1: 2→3→4, 3→4→5, 4→5→6!</div>
    </div>
  </div>
</div>
<script>
const sim12Patterns = {
  stepUp: {
    title: 'Consecutive Step-Up Pattern',
    desc: 'Each digit steps up by 1 (+1 each place): 234, 345, 456, 567, 678!',
    nums: ['234', '345', '456', '567', '678']
  },
  stepDown: {
    title: 'Consecutive Step-Down Pattern',
    desc: 'Each digit steps down by 1 (-1 each place): 765, 654, 543, 432, 321!',
    nums: ['765', '654', '543', '432', '321']
  },
  triplets: {
    title: 'Repeating Identical Triplet Digits',
    desc: 'All three digits (Hundreds, Tens, Ones) are completely identical!',
    nums: ['111', '222', '333', '444', '555']
  },
  mirrors: {
    title: 'Mirrored Palindromic Numbers',
    desc: 'The number reads exactly the same forwards and backwards! (First digit = Last digit)',
    nums: ['121', '343', '565', '787', '909']
  }
};

function sim12Select(key) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });

  const pat = sim12Patterns[key];
  document.getElementById('sim12RuleTitle').innerText = pat.title;
  document.getElementById('sim12RuleDesc').innerText = pat.desc;

  const disp = document.getElementById('sim12Display');
  disp.innerHTML = '';
  pat.nums.forEach(num => {
    const card = document.createElement('div');
    card.style.background = 'rgba(59,130,246,0.15)';
    card.style.border = '1px solid #3b82f6';
    card.style.borderRadius = '10px';
    card.style.padding = '10px 18px';
    card.style.fontSize = '22px';
    card.style.fontWeight = 'bold';
    card.style.color = '#fff';
    card.innerText = num;
    disp.appendChild(card);
  });
}
setTimeout(() => sim12Select('stepUp'), 100);
</script>
''',
    13: '''
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🎟️ 6 Place Value Slips Number Maker</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim13Preset('max')">Max (600)</button>
      <button class="sim-btn" onclick="sim13Preset('min')">Min (6)</button>
      <button class="sim-btn" onclick="sim13Preset('target321')">Make 321</button>
      <button class="sim-btn" onclick="sim13Reset()">Reset Slips</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#94a3b8; font-weight:bold; margin-bottom:10px;">
      Total Available Slips: <span id="sim13Remaining" style="color:#fbbf24; font-size:16px;">6 / 6 Available</span>
    </div>
    <div style="display:flex; justify-content:center; gap:16px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- Hundreds Slip Column -->
      <div style="flex:1; background:rgba(59,130,246,0.12); border:1px solid #3b82f6; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#60a5fa;">[100] Slips</div>
        <div id="sim13CountH" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('H', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('H', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValH" style="font-size:11px; color:#93c5fd; margin-top:4px;">0 Units</div>
      </div>
      <!-- Tens Slip Column -->
      <div style="flex:1; background:rgba(245,158,11,0.12); border:1px solid #f59e0b; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#fbbf24;">[10] Slips</div>
        <div id="sim13CountT" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('T', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('T', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValT" style="font-size:11px; color:#fde68a; margin-top:4px;">0 Units</div>
      </div>
      <!-- Ones Slip Column -->
      <div style="flex:1; background:rgba(16,185,129,0.12); border:1px solid #10b981; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#34d399;">[1] Slips</div>
        <div id="sim13CountO" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('O', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('O', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValO" style="font-size:11px; color:#a7f3d0; margin-top:4px;">0 Units</div>
      </div>
    </div>
    <div id="sim13TotalBox" style="font-size:20px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Constructed Number: 0
    </div>
  </div>
</div>
<script>
let sim13Counts = { H: 0, T: 0, O: 0 };
const sim13MaxSlips = 6;

function sim13Update() {
  const used = sim13Counts.H + sim13Counts.T + sim13Counts.O;
  const rem = sim13MaxSlips - used;
  document.getElementById('sim13Remaining').innerText = rem + ' / ' + sim13MaxSlips + ' Available';

  document.getElementById('sim13CountH').innerText = sim13Counts.H;
  document.getElementById('sim13ValH').innerText = (sim13Counts.H * 100) + ' Units';

  document.getElementById('sim13CountT').innerText = sim13Counts.T;
  document.getElementById('sim13ValT').innerText = (sim13Counts.T * 10) + ' Units';

  document.getElementById('sim13CountO').innerText = sim13Counts.O;
  document.getElementById('sim13ValO').innerText = sim13Counts.O + ' Units';

  const sum = sim13Counts.H * 100 + sim13Counts.T * 10 + sim13Counts.O;
  document.getElementById('sim13TotalBox').innerHTML = 'Constructed Total: <span style="color:#fbbf24;">' + sum + '</span> (' + used + ' slips used)';
}

function sim13Mod(type, delta) {
  const used = sim13Counts.H + sim13Counts.T + sim13Counts.O;
  if (delta > 0 && used >= sim13MaxSlips) return;
  if (delta < 0 && sim13Counts[type] <= 0) return;
  sim13Counts[type] += delta;
  sim13Update();
}

function sim13Preset(type) {
  if (type === 'max') {
    sim13Counts = { H: 6, T: 0, O: 0 };
  } else if (type === 'min') {
    sim13Counts = { H: 0, T: 0, O: 6 };
  } else if (type === 'target321') {
    sim13Counts = { H: 3, T: 2, O: 1 };
  }
  sim13Update();
}

function sim13Reset() {
  sim13Counts = { H: 0, T: 0, O: 0 };
  sim13Update();
}
setTimeout(() => sim13Preset('target321'), 100);
</script>
''',
    14: '''
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🔢 Digit Combination & Permutation Explorer (Digits 3 & 8)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Mode(2)">2-Digit Permutations</button>
      <button class="sim-btn" onclick="sim14Mode(3)">3-Digit Permutations</button>
      <button class="sim-btn" onclick="sim14Sort()">Toggle Sort Order</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim14Summary" style="font-size:14px; color:#cbd5e1; font-weight:bold; margin-bottom:12px; text-align:center;">
      Showing all combinations using digits 3 and 8:
    </div>
    <div id="sim14Cards" style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center; max-width:620px; margin-bottom:14px;">
      <!-- Injected by JS -->
    </div>
    <div id="sim14MinMax" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Smallest: 33 | Largest: 88
    </div>
  </div>
</div>
<script>
let sim14Digits = 2;
let sim14Asc = true;
const sim14Data = {
  2: [33, 38, 83, 88],
  3: [333, 338, 383, 388, 833, 838, 883, 888]
};

function sim14Mode(digits) {
  sim14Digits = digits;
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(digits + '-Digit'));
  });
  sim14Render();
}

function sim14Sort() {
  sim14Asc = !sim14Asc;
  sim14Render();
}

function sim14Render() {
  const list = [...sim14Data[sim14Digits]];
  list.sort((a, b) => sim14Asc ? a - b : b - a);

  document.getElementById('sim14Summary').innerText = 'Showing ' + list.length + ' distinct ' + sim14Digits + '-digit combinations (Ordered ' + (sim14Asc ? 'Ascending' : 'Descending') + '):';

  const cardsContainer = document.getElementById('sim14Cards');
  cardsContainer.innerHTML = '';
  list.forEach(num => {
    const d = document.createElement('div');
    d.style.background = 'rgba(245,158,11,0.15)';
    d.style.border = '1px solid #f59e0b';
    d.style.borderRadius = '10px';
    d.style.padding = '8px 16px';
    d.style.fontSize = '20px';
    d.style.fontWeight = 'bold';
    d.style.color = '#fff';
    d.innerText = num;
    cardsContainer.appendChild(d);
  });

  const min = Math.min(...list);
  const max = Math.max(...list);
  document.getElementById('sim14MinMax').innerHTML = 'Smallest: <span style="color:#34d399;">' + min + '</span> | Largest: <span style="color:#f87171;">' + max + '</span>';
}
setTimeout(() => sim14Mode(2), 100);
</script>
''',
    15: '''
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">📜 Bhutasankhya Cultural Symbol Decoder</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Select(0)">Moon (1)</button>
      <button class="sim-btn" onclick="sim15Select(1)">Eyes (2)</button>
      <button class="sim-btn" onclick="sim15Select(2)">Times (3)</button>
      <button class="sim-btn" onclick="sim15Select(3)">Directions (4)</button>
      <button class="sim-btn" onclick="sim15Select(4)">Hand/Palm (5)</button>
      <button class="sim-btn" onclick="sim15Select(5)">Notes (7)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim15Icon" style="font-size:40px; margin-bottom:6px;">🌙</div>
      <div id="sim15Sanskrit" style="font-size:22px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">Chandra / Shashi (Moon)</div>
      <div id="sim15Digit" style="font-size:32px; font-weight:bold; color:#38bdf8; margin-bottom:6px;">Numeral: 1</div>
      <div id="sim15Meaning" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        Represents 1 because in our observable natural world, there is exactly one moon orbiting Earth!
      </div>
    </div>
    <div style="font-size:12px; color:#94a3b8; font-style:italic;">
      Ancient Indian mathematicians used poetry & nature words to record numbers effortlessly in verse!
    </div>
  </div>
</div>
<script>
const sim15Symbols = [
  { icon: '🌙', name: 'Chandra / Shashi (Moon)', num: 1, desc: 'Represents 1 because in our natural world, there is only one moon orbiting Earth!' },
  { icon: '👀', name: 'Netra / Lochana (Eyes)', num: 2, desc: 'Represents 2 because humans and animals see through a pair of two eyes!' },
  { icon: '⏳', name: 'Trikala (Three Times)', num: 3, desc: 'Represents 3 because time flows through three states: Past, Present, and Future!' },
  { icon: '🧭', name: 'Disha (Cardinal Directions)', num: 4, desc: 'Represents 4 because geography is framed by four directions: North, South, East, West!' },
  { icon: '✋', name: 'Pani / Kara (Palm Fingers)', num: 5, desc: 'Represents 5 because a single human hand holds five fingers!' },
  { icon: '🎵', name: 'Saptasvara (Musical Notes)', num: 7, desc: 'Represents 7 because classical Indian music is built on seven sacred notes: Sa, Re, Ga, Ma, Pa, Dha, Ni!' }
];

function sim15Select(idx) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });

  const item = sim15Symbols[idx];
  document.getElementById('sim15Icon').innerText = item.icon;
  document.getElementById('sim15Sanskrit').innerText = item.name;
  document.getElementById('sim15Digit').innerText = 'Numeral: ' + item.num;
  document.getElementById('sim15Meaning').innerText = item.desc;
}
setTimeout(() => sim15Select(0), 100);
</script>
''',
    16: '''
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🔄 Right-to-Left Word Numeral Decoder (*Ankanam Vamato Gatih*)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16Preset(0)">Netra-Agni-Shashi</button>
      <button class="sim-btn" onclick="sim16Preset(1)">Kha-Bana-Chandra</button>
      <button class="sim-btn" onclick="sim16Preset(2)">Veda-Netra-Ritu</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#fbbf24; font-weight:bold; margin-bottom:8px;">
      Rule: 'Ankanam Vamato Gatih' (Words are spoken left-to-right, but digits fill Units → Tens → Hundreds!)
    </div>
    <!-- Card sequence container -->
    <div id="sim16Cards" style="display:flex; justify-content:center; gap:12px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- Injected by JS -->
    </div>
    <!-- Final decoded standard number -->
    <div id="sim16Decoded" style="font-size:22px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 24px; text-align:center;">
      Decoded Number: 132
    </div>
  </div>
</div>
<script>
const sim16Data = [
  {
    name: 'Netra-Agni-Shashi',
    cards: [
      { word: 'Netra (Eyes)', digit: 2, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Agni (Fires)', digit: 3, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Shashi (Moon)', digit: 1, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 132
  },
  {
    name: 'Kha-Bana-Chandra',
    cards: [
      { word: 'Kha (Void/Sky)', digit: 0, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Bana (Arrows)', digit: 5, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Chandra (Moon)', digit: 1, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 150
  },
  {
    name: 'Veda-Netra-Ritu',
    cards: [
      { word: 'Veda (Vedas)', digit: 4, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Netra (Eyes)', digit: 2, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Ritu (Seasons)', digit: 6, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 624
  }
];

function sim16Preset(idx) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });

  const item = sim16Data[idx];
  const container = document.getElementById('sim16Cards');
  container.innerHTML = '';

  item.cards.forEach((card, i) => {
    const col = document.createElement('div');
    col.style.flex = '1';
    col.style.background = 'rgba(255,255,255,0.05)';
    col.style.border = '1px solid ' + card.color;
    col.style.borderRadius = '12px';
    col.style.padding = '10px';
    col.style.textAlign = 'center';

    col.innerHTML = `
      <div style="font-size:11px; color:#94a3b8; font-weight:bold;">Word ${i + 1}</div>
      <div style="font-size:14px; font-weight:bold; color:${card.color}; margin:4px 0;">${card.word}</div>
      <div style="font-size:24px; font-weight:bold; color:#fff;">${card.digit}</div>
      <div style="font-size:11px; color:#cbd5e1; margin-top:4px;">➡️ Fills ${card.place}</div>
    `;
    container.appendChild(col);
  });

  document.getElementById('sim16Decoded').innerHTML = 'Decoded 3-Digit Numeral: <span style="color:#fbbf24; font-size:26px;">' + item.num + '</span> <span style="font-size:14px; color:#94a3b8;">(' + item.cards[2].digit + '00 + ' + item.cards[1].digit + '0 + ' + item.cards[0].digit + ')</span>';
}
setTimeout(() => sim16Preset(0), 100);
</script>
''',
}

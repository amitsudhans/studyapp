#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
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
""",

    10: """
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
""",

    11: """
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
""",

    12: """
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
""",

    13: """
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
""",

    14: """
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
""",

    15: """
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
""",

    16: """
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
    deck.innerHTML += '<button onclick="sim16PickCard(' + n + ')" style="width:36px; height:48px; background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.3); border-radius:6px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer;" onmouseover="this.style.background=\'#38bdf8\'" onmouseout="this.style.background=\'rgba(255,255,255,0.12)\'">' + n + '</button>';
  }
}
setTimeout(sim16ResetCards, 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Sims 9-16).")

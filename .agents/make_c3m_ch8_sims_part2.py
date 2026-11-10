#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 8: Fair Share
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🕵️ 'Guess Who Am I' Number Riddle Detective</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Select(1)">Riddle 1: Double is 10</button>
      <button class="sim-btn" onclick="sim9Select(2)">Riddle 2: Double of 4</button>
      <button class="sim-btn" onclick="sim9Select(3)">Riddle 3: Half is 6, Add 2</button>
      <button class="sim-btn" onclick="sim9Solve()">Reveal Solution</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim9Clue" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:8px;">
        "I am a mystery number. If you double me, you get the number 10. Who am I?"
      </div>
      <div id="sim9AnswerBox" style="font-size:24px; font-weight:bold; color:#38bdf8;">
        ?
      </div>
    </div>
    <div id="sim9Reasoning" style="font-size:14px; color:#a7f3d0; font-weight:600;">
      Click 'Reveal Solution' to see the inverse deductive reasoning!
    </div>
  </div>
</div>
<script>
let sim9Riddle = 1;
const sim9Data = {
  1: { clue: '"I am a mystery number. If you double me, you get the number 10. Who am I?"', ans: '5', reason: 'Reverse Logic: If doubling gives 10, the number is half of 10. 10 ÷ 2 = 5!' },
  2: { clue: '"I am greater than 6 but less than 10. I am the double of 4. Who am I?"', ans: '8', reason: 'Deductive Logic: Double of 4 is 4 × 2 = 8. 8 is between 6 and 10!' },
  3: { clue: '"My half is 6. If you add 2 to me, what number do you reach?"', ans: '14', reason: 'Two-Step Logic: If half is 6, the whole is 6 × 2 = 12. Then 12 + 2 = 14!' }
};

function sim9Select(idx) {
  sim9Riddle = idx;
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('Riddle ' + idx));
  });
  document.getElementById('sim9Clue').innerText = sim9Data[idx].clue;
  document.getElementById('sim9AnswerBox').innerText = '?';
  document.getElementById('sim9Reasoning').innerText = 'Click \'Reveal Solution\' to see the inverse deductive reasoning!';
}
function sim9Solve() {
  const d = sim9Data[sim9Riddle];
  document.getElementById('sim9AnswerBox').innerHTML = '🎉 Secret Number: <span style="color:#fbbf24;">' + d.ans + '</span>';
  document.getElementById('sim9Reasoning').innerHTML = '💡 ' + d.reason;
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🍉 Watermelon Quarter Partitioning Workbench</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Step(1)">1 Whole</button>
      <button class="sim-btn" onclick="sim10Step(2)">2 Halves (1/2 each)</button>
      <button class="sim-btn" onclick="sim10Step(3)">4 Quarters (1/4 each)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim10Visual" style="min-height:120px; display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:14px;">
      <!-- Watermelon segments -->
    </div>
    <div id="sim10Formula" style="font-size:18px; font-weight:bold; color:#f59e0b; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      1 Complete Whole Watermelon ready to share among 4 people.
    </div>
  </div>
</div>
<script>
function sim10Step(s) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (s === 1 && b.innerText.includes('1 Whole')) ||
      (s === 2 && b.innerText.includes('2 Halves')) ||
      (s === 3 && b.innerText.includes('4 Quarters')));
  });

  const vis = document.getElementById('sim10Visual');
  const f = document.getElementById('sim10Formula');

  if (s === 1) {
    vis.innerHTML = '<div style="width:110px; height:110px; background:radial-gradient(circle at 35% 35%, #10b981, #065f46); border-radius:50%; border:3px solid #047857; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#fff; font-size:16px;">1 Whole</div>';
    f.innerText = '1 Complete Whole Watermelon.';
  } else if (s === 2) {
    vis.innerHTML = '<div style="display:flex; gap:12px;"><div style="width:55px; height:110px; background:radial-gradient(circle at 70% 35%, #ef4444, #991b1b); border-radius:110px 0 0 110px; border:3px solid #059669; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#fff;">1/2</div><div style="width:55px; height:110px; background:radial-gradient(circle at 30% 35%, #ef4444, #991b1b); border-radius:0 110px 110px 0; border:3px solid #059669; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#fff;">1/2</div></div>';
    f.innerHTML = 'Cut into 2 Halves: 1 Whole = 1/2 + 1/2 (Shared between 2 people)';
  } else {
    vis.innerHTML = '<div style="display:grid; grid-template-columns:repeat(2, 55px); gap:6px;"><div style="width:55px; height:55px; background:#ef4444; border-radius:55px 0 0 0; border:2px solid #059669; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">1/4</div><div style="width:55px; height:55px; background:#ef4444; border-radius:0 55px 0 0; border:2px solid #059669; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">1/4</div><div style="width:55px; height:55px; background:#ef4444; border-radius:0 0 0 55px; border:2px solid #059669; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">1/4</div><div style="width:55px; height:55px; background:#ef4444; border-radius:0 0 55px 0; border:2px solid #059669; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#fff;">1/4</div></div>';
    f.innerHTML = '🎉 <span style="color:#34d399;">Cut into 4 Quarters: Each piece = 1/4 (Notice: 2 Quarters = 1/2 Half!)</span>';
  }
}
setTimeout(() => sim10Step(1), 100);
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">📐 Geometric Shape Quarter Partitions</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Shape('circle')">Circle (4 Quadrants)</button>
      <button class="sim-btn" onclick="sim11Shape('square')">Square (4 Small Squares)</button>
      <button class="sim-btn" onclick="sim11Shape('diagonal')">Square (4 Triangles)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim11Canvas" style="position:relative; width:130px; height:130px; margin-bottom:14px;">
      <!-- Shape partitions -->
    </div>
    <div id="sim11Equation" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Circle divided into 4 identical quadrants (25% area each).
    </div>
  </div>
</div>
<script>
function sim11Shape(type) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', (type === 'circle' && b.innerText.includes('Circle')) ||
      (type === 'square' && b.innerText.includes('Small Squares')) ||
      (type === 'diagonal' && b.innerText.includes('Triangles')));
  });

  const c = document.getElementById('sim11Canvas');
  const eq = document.getElementById('sim11Equation');
  const sz = 130;

  if (type === 'circle') {
    c.innerHTML = '<svg width="' + sz + '" height="' + sz + '" style="border-radius:50%; overflow:hidden;"><circle cx="65" cy="65" r="64" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/><line x1="65" y1="0" x2="65" y2="130" stroke="#f59e0b" stroke-width="2.5"/><line x1="0" y1="65" x2="130" y2="65" stroke="#f59e0b" stroke-width="2.5"/><text x="25" y="45" fill="#38bdf8" font-size="12" font-weight="bold">1/4</text><text x="85" y="45" fill="#38bdf8" font-size="12" font-weight="bold">1/4</text><text x="25" y="100" fill="#38bdf8" font-size="12" font-weight="bold">1/4</text><text x="85" y="100" fill="#38bdf8" font-size="12" font-weight="bold">1/4</text></svg>';
    eq.innerHTML = 'Circle: 4 identical circular quadrants (Area = 25% each)!';
  } else if (type === 'square') {
    c.innerHTML = '<div style="display:grid; grid-template-columns:repeat(2, 63px); gap:4px; width:130px; height:130px;"><div style="background:rgba(59,130,246,0.3); border:1px solid #3b82f6; display:flex; align-items:center; justify-content:center; color:#93c5fd; font-weight:bold; font-size:12px;">1/4</div><div style="background:rgba(16,185,129,0.3); border:1px solid #10b981; display:flex; align-items:center; justify-content:center; color:#6ee7b7; font-weight:bold; font-size:12px;">1/4</div><div style="background:rgba(245,158,11,0.3); border:1px solid #f59e0b; display:flex; align-items:center; justify-content:center; color:#fde68a; font-weight:bold; font-size:12px;">1/4</div><div style="background:rgba(236,72,153,0.3); border:1px solid #ec4899; display:flex; align-items:center; justify-content:center; color:#fbcfe8; font-weight:bold; font-size:12px;">1/4</div></div>';
    eq.innerHTML = 'Square: 4 smaller congruent squares (Area = 25% each)!';
  } else {
    c.innerHTML = '<svg width="' + sz + '" height="' + sz + '" style="background:#1e293b; border:2px solid #475569; border-radius:6px;"><polygon points="0,0 130,0 65,65" fill="rgba(59,130,246,0.35)"/><polygon points="130,0 130,130 65,65" fill="rgba(16,185,129,0.35)"/><polygon points="130,130 0,130 65,65" fill="rgba(245,158,11,0.35)"/><polygon points="0,130 0,0 65,65" fill="rgba(236,72,153,0.35)"/><line x1="0" y1="0" x2="130" y2="130" stroke="#fff" stroke-width="2"/><line x1="130" y1="0" x2="0" y2="130" stroke="#fff" stroke-width="2"/><text x="58" y="28" fill="#fff" font-size="11" font-weight="bold">1/4</text><text x="95" y="70" fill="#fff" font-size="11" font-weight="bold">1/4</text><text x="58" y="115" fill="#fff" font-size="11" font-weight="bold">1/4</text><text x="18" y="70" fill="#fff" font-size="11" font-weight="bold">1/4</text></svg>';
    eq.innerHTML = 'Diagonal Folds: 4 congruent triangular quarters (Area = 25% each)!';
  }
}
setTimeout(() => sim11Shape('circle'), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🐦 Bird Flock & Marigold Collection Fractions</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Fraction of 12 Birds:</span>
      <button class="sim-btn" onclick="sim12Set(3, '1/4')">1/4 (3 Birds)</button>
      <button class="sim-btn active" onclick="sim12Set(6, '1/2')">1/2 (6 Birds)</button>
      <button class="sim-btn" onclick="sim12Set(9, '3/4')">3/4 (9 Birds)</button>
      <button class="sim-btn" onclick="sim12Set(12, 'Whole')">Whole (12 Birds)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim12Flock" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- 12 Birds -->
    </div>
    <div id="sim12Equation" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      1/2 of 12 Birds = 6 Birds (12 ÷ 2 = 6)
    </div>
  </div>
</div>
<script>
let sim12Count = 6;
let sim12Label = '1/2';

function sim12Set(cnt, lbl) {
  sim12Count = cnt;
  sim12Label = lbl;
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith(lbl));
  });
  sim12Render();
}

function sim12Render() {
  const flock = document.getElementById('sim12Flock');
  flock.innerHTML = '';
  for (let i = 0; i < 12; i++) {
    const isHighlighted = (i < sim12Count);
    const bg = isHighlighted ? 'rgba(56,189,248,0.25)' : 'rgba(255,255,255,0.06)';
    const border = isHighlighted ? '#38bdf8' : 'rgba(255,255,255,0.15)';
    const shadow = isHighlighted ? 'box-shadow:0 0 10px rgba(56,189,248,0.5);' : '';
    flock.innerHTML += '<div style="background:' + bg + '; border:1px solid ' + border + '; border-radius:10px; padding:8px 10px; font-size:22px; text-align:center; ' + shadow + '" title="Bird ' + (i+1) + '">🐦</div>';
  }

  const eq = document.getElementById('sim12Equation');
  if (sim12Label === '1/4') eq.innerHTML = '1/4 of 12 Birds = <span style="color:#38bdf8;">3 Birds (12 ÷ 4 = 3)</span>';
  else if (sim12Label === '1/2') eq.innerHTML = '1/2 of 12 Birds = <span style="color:#34d399;">6 Birds (12 ÷ 2 = 6)</span>';
  else if (sim12Label === '3/4') eq.innerHTML = '3/4 of 12 Birds = <span style="color:#fbbf24;">9 Birds (3 × 3 = 9)</span>';
  else eq.innerHTML = 'Complete Whole Flock = <span style="color:#f472b6;">12 Birds (4/4 = 1)</span>';
}
setTimeout(sim12Render, 100);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">⏱️ Progressive Fraction Circle Dial</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim13Step(1)">1 Quarter (1/4)</button>
      <button class="sim-btn active" onclick="sim13Step(2)">2 Quarters (1/2)</button>
      <button class="sim-btn" onclick="sim13Step(3)">3 Quarters (3/4)</button>
      <button class="sim-btn" onclick="sim13Step(4)">4 Quarters (1 Whole)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim13Circle" style="position:relative; width:130px; height:130px; margin-bottom:14px;">
      <!-- Dynamic SVG Disc -->
    </div>
    <div id="sim13Equation" style="font-size:20px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      2 Quarters = 1/2 of Circle (Exactly half shaded!)
    </div>
  </div>
</div>
<script>
function sim13Step(q) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith(q + ' '));
  });

  const c = document.getElementById('sim13Circle');
  const eq = document.getElementById('sim13Equation');
  const sz = 130;

  let svg = '<svg width="' + sz + '" height="' + sz + '" style="border-radius:50%; overflow:hidden;">';
  svg += '<circle cx="65" cy="65" r="64" fill="#0f172a" stroke="#475569" stroke-width="2"/>';

  // Quadrant 1 (top-right): 0 to 90 deg
  if (q >= 1) svg += '<path d="M65,65 L65,0 A65,65 0 0,1 130,65 Z" fill="#38bdf8" />';
  // Quadrant 2 (bottom-right): 90 to 180 deg
  if (q >= 2) svg += '<path d="M65,65 L130,65 A65,65 0 0,1 65,130 Z" fill="#38bdf8" />';
  // Quadrant 3 (bottom-left): 180 to 270 deg
  if (q >= 3) svg += '<path d="M65,65 L65,130 A65,65 0 0,1 0,65 Z" fill="#38bdf8" />';
  // Quadrant 4 (top-left): 270 to 360 deg
  if (q >= 4) svg += '<path d="M65,65 L0,65 A65,65 0 0,1 65,0 Z" fill="#38bdf8" />';

  svg += '<line x1="65" y1="0" x2="65" y2="130" stroke="#fff" stroke-width="1.5"/>';
  svg += '<line x1="0" y1="65" x2="130" y2="65" stroke="#fff" stroke-width="1.5"/>';
  svg += '</svg>';
  c.innerHTML = svg;

  if (q === 1) eq.innerHTML = '1 Quarter = <span style="color:#38bdf8;">1/4 of Circle (25%)</span>';
  else if (q === 2) eq.innerHTML = '2 Quarters = <span style="color:#34d399;">1/2 of Circle (50% - Exactly one half!)</span>';
  else if (q === 3) eq.innerHTML = '3 Quarters = <span style="color:#fbbf24;">3/4 of Circle (75% - 1 quarter left to whole!)</span>';
  else eq.innerHTML = '4 Quarters = <span style="color:#f472b6;">1 Complete Whole Circle (4/4 = 100%)</span>';
}
setTimeout(() => sim13Step(2), 100);
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🥤 Three-Quarters Cup & Complementary Fraction Lab</div>
    <div class="sim-controls">
      <span style="font-size:13px; color:#cbd5e1;">Fill Levels:</span>
      <button class="sim-btn" onclick="sim14Fill(1)">1/4 Level</button>
      <button class="sim-btn" onclick="sim14Fill(2)">2/4 (Half)</button>
      <button class="sim-btn active" onclick="sim14Fill(3)">3/4 Level</button>
      <button class="sim-btn" onclick="sim14Fill(4)">4/4 Full</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; align-items:center; gap:20px; margin-bottom:14px;">
      <!-- Measuring cup visual -->
      <div style="position:relative; width:80px; height:120px; background:rgba(255,255,255,0.06); border:3px solid #94a3b8; border-top:none; border-radius:0 0 16px 16px; overflow:hidden;">
        <div id="sim14Liquid" style="position:absolute; bottom:0; left:0; right:0; height:75%; background:linear-gradient(to top, #d97706, #fbbf24); transition:height 0.3s ease;"></div>
        <div style="position:absolute; bottom:25%; left:0; right:0; border-bottom:1px dashed rgba(255,255,255,0.4);"></div>
        <div style="position:absolute; bottom:50%; left:0; right:0; border-bottom:1px dashed rgba(255,255,255,0.4);"></div>
        <div style="position:absolute; bottom:75%; left:0; right:0; border-bottom:1px dashed rgba(255,255,255,0.4);"></div>
      </div>
      <div style="text-align:left;">
        <div id="sim14FullStat" style="font-size:16px; font-weight:bold; color:#fbbf24;">Full: 3/4 (Three Quarters)</div>
        <div id="sim14EmptyStat" style="font-size:16px; font-weight:bold; color:#94a3b8; margin-top:4px;">Empty: 1/4 (One Quarter)</div>
        <div style="font-size:12px; color:#cbd5e1; margin-top:8px;">Complementary Law: 3/4 + 1/4 = 4/4 = 1 Whole</div>
      </div>
    </div>
  </div>
</div>
<script>
function sim14Fill(level) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith(level + '/'));
  });

  const liquid = document.getElementById('sim14Liquid');
  liquid.style.height = (level * 25) + '%';

  const full = level + '/4';
  const empty = (4 - level) + '/4';

  document.getElementById('sim14FullStat').innerHTML = 'Full: <span style="color:#fbbf24;">' + full + '</span>';
  document.getElementById('sim14EmptyStat').innerHTML = 'Empty: <span style="color:#38bdf8;">' + empty + '</span>';
}
setTimeout(() => sim14Fill(3), 100);
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🎨 16-Cell Grid Fraction Painter</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim15Preset(4)">Preset 1/4 (4 Cells)</button>
      <button class="sim-btn active" onclick="sim15Preset(8)">Preset 1/2 (8 Cells)</button>
      <button class="sim-btn" onclick="sim15Preset(12)">Preset 3/4 (12 Cells)</button>
      <button class="sim-btn" onclick="sim15Clear()">Clear</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim15Grid" style="display:grid; grid-template-columns:repeat(4, 30px); gap:4px; margin-bottom:14px; background:rgba(0,0,0,0.3); padding:8px; border-radius:10px; border:1px solid rgba(255,255,255,0.15);">
      <!-- 16 Cells -->
    </div>
    <div id="sim15Status" style="font-size:18px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      8 / 16 Cells Shaded = Exactly 1/2 (One Half)!
    </div>
  </div>
</div>
<script>
let sim15Cells = Array(16).fill(false);

function sim15Preset(cnt) {
  sim15Cells = Array(16).fill(false);
  for (let i = 0; i < cnt; i++) sim15Cells[i] = true;
  sim15Render();
}
function sim15Clear() {
  sim15Cells = Array(16).fill(false);
  sim15Render();
}
function sim15Toggle(idx) {
  sim15Cells[idx] = !sim15Cells[idx];
  sim15Render();
}
function sim15Render() {
  const grid = document.getElementById('sim15Grid');
  grid.innerHTML = '';
  let shadedCount = 0;

  for (let i = 0; i < 16; i++) {
    const isShaded = sim15Cells[i];
    if (isShaded) shadedCount++;
    const bg = isShaded ? '#38bdf8' : 'rgba(255,255,255,0.08)';
    grid.innerHTML += '<div onclick="sim15Toggle(' + i + ')" style="width:30px; height:30px; background:' + bg + '; border-radius:4px; cursor:pointer; border:1px solid rgba(255,255,255,0.2);"></div>';
  }

  const stat = document.getElementById('sim15Status');
  if (shadedCount === 4) stat.innerHTML = '🎉 4 / 16 Cells Shaded = <span style="color:#38bdf8;">Exactly 1/4 (One Quarter)!</span>';
  else if (shadedCount === 8) stat.innerHTML = '🎉 8 / 16 Cells Shaded = <span style="color:#34d399;">Exactly 1/2 (One Half)!</span>';
  else if (shadedCount === 12) stat.innerHTML = '🎉 12 / 16 Cells Shaded = <span style="color:#fbbf24;">Exactly 3/4 (Three Quarters)!</span>';
  else if (shadedCount === 16) stat.innerHTML = '🎉 16 / 16 Cells Shaded = <span style="color:#f472b6;">Complete Whole (4/4)!</span>';
  else stat.innerText = shadedCount + ' / 16 Cells Shaded. (Click cells to reach 4 for 1/4, 8 for 1/2, or 12 for 3/4!)';
}
setTimeout(() => sim15Preset(8), 100);
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🧩 Fractional Puzzle Whole Reconstruction Workbench</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16SetMode('quarters')">Rebuild from 4 Quarters (1/4)</button>
      <button class="sim-btn" onclick="sim16SetMode('halves')">Rebuild from 2 Halves (1/2)</button>
      <button class="sim-btn" onclick="sim16Snap()">Snap Pieces Together</button>
      <button class="sim-btn" onclick="sim16Reset()">Disassemble</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim16Visual" style="min-height:130px; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
      <!-- Dynamic puzzle pieces -->
    </div>
    <div id="sim16Equation" style="font-size:18px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Click 'Snap Pieces Together' to reconstruct the complete whole!
    </div>
  </div>
</div>
<script>
let sim16Mode = 'quarters';
let sim16Snapped = false;

function sim16SetMode(m) {
  sim16Mode = m;
  sim16Snapped = false;
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    if (m === 'quarters') b.classList.toggle('active', b.innerText.includes('Quarters'));
    else b.classList.toggle('active', b.innerText.includes('Halves'));
  });
  sim16Render();
}
function sim16Snap() {
  sim16Snapped = true;
  sim16Render();
}
function sim16Reset() {
  sim16Snapped = false;
  sim16Render();
}
function sim16Render() {
  const vis = document.getElementById('sim16Visual');
  const eq = document.getElementById('sim16Equation');

  if (sim16Mode === 'quarters') {
    if (!sim16Snapped) {
      vis.innerHTML = '<div style="display:flex; gap:10px;"><div style="width:40px; height:40px; background:#38bdf8; border-radius:4px; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:11px; color:#0f172a;">1/4</div><div style="width:40px; height:40px; background:#38bdf8; border-radius:4px; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:11px; color:#0f172a;">1/4</div><div style="width:40px; height:40px; background:#38bdf8; border-radius:4px; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:11px; color:#0f172a;">1/4</div><div style="width:40px; height:40px; background:#38bdf8; border-radius:4px; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:11px; color:#0f172a;">1/4</div></div>';
      eq.innerText = '4 Separate 1/4 Pieces ready. Click \'Snap Pieces Together\'!';
    } else {
      vis.innerHTML = '<div style="display:grid; grid-template-columns:repeat(2, 50px); gap:2px; border:2px solid #38bdf8; padding:2px; border-radius:6px; background:#0284c7;"><div style="width:50px; height:50px; background:#38bdf8; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:12px; color:#0f172a;">1/4</div><div style="width:50px; height:50px; background:#38bdf8; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:12px; color:#0f172a;">1/4</div><div style="width:50px; height:50px; background:#38bdf8; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:12px; color:#0f172a;">1/4</div><div style="width:50px; height:50px; background:#38bdf8; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:12px; color:#0f172a;">1/4</div></div>';
      eq.innerHTML = '🎉 <span style="color:#34d399;">Reconstructed Whole Square: 4 × 1/4 = 4/4 = 1 Whole!</span>';
    }
  } else {
    if (!sim16Snapped) {
      vis.innerHTML = '<div style="display:flex; gap:16px;"><div style="width:50px; height:100px; background:#10b981; border-radius:100px 0 0 100px; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#0f172a;">1/2</div><div style="width:50px; height:100px; background:#10b981; border-radius:0 100px 100px 0; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#0f172a;">1/2</div></div>';
      eq.innerText = '2 Separate Half Semicircles. Click \'Snap Pieces Together\'!';
    } else {
      vis.innerHTML = '<div style="width:100px; height:100px; background:#10b981; border-radius:50%; border:2px solid #059669; display:flex; align-items:center; justify-content:center; font-weight:bold; color:#0f172a; font-size:16px;">1 Whole</div>';
      eq.innerHTML = '🎉 <span style="color:#34d399;">Reconstructed Whole Circle: 2 × 1/2 = 2/2 = 1 Whole!</span>';
    }
  }
}
setTimeout(sim16Render, 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Sims 9-16).")

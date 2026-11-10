#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🪞 Capital Letter Symmetry Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Select('A')">Letter A</button>
      <button class="sim-btn" onclick="sim9Select('B')">Letter B</button>
      <button class="sim-btn" onclick="sim9Select('H')">Letter H</button>
      <button class="sim-btn" onclick="sim9Select('F')">Letter F</button>
      <button class="sim-btn" onclick="sim9ToggleAxis()">Toggle Axis: <span id="sim9AxisLabel">Vertical</span></button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div style="position:relative; width:160px; height:140px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center;">
      <!-- Letter display -->
      <span id="sim9LetterChar" style="font-size:84px; font-weight:900; color:#fbbf24; font-family:sans-serif; user-select:none;">A</span>
      <!-- Mirror Line -->
      <div id="sim9MirrorLine" style="position:absolute; width:2px; height:130px; background:#f43f5e; box-shadow:0 0 8px #f43f5e; transition:all 0.3s ease;"></div>
    </div>
    <div id="sim9Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ✔️ <b>Vertical Symmetry:</b> Folding letter A along the red vertical line matches left and right halves perfectly!
    </div>
  </div>
</div>
<script>
let sim9CurrentLetter = 'A';
let sim9IsVertical = true;

const sim9Data = {
  'A': { vert: true, horiz: false, vNote: '✔️ Vertical Symmetry: Left and right sides of A are identical mirror reflections.', hNote: '❌ No Horizontal Symmetry: Top point does not match open bottom legs.' },
  'B': { vert: false, horiz: true, vNote: '❌ No Vertical Symmetry: Left vertical spine does not match curved right loops.', hNote: '✔️ Horizontal Symmetry: Top loop matches bottom loop when folded across horizontal axis.' },
  'H': { vert: true, horiz: true, vNote: '✔️ Vertical Symmetry: Left vertical bar reflects right vertical bar across the center.', hNote: '✔️ Horizontal Symmetry: Top half reflects bottom half across the horizontal crossbar.' },
  'F': { vert: false, horiz: false, vNote: '❌ No Vertical Symmetry: Right horizontal arms have no reflection on left.', hNote: '❌ No Horizontal Symmetry: Top arms have no reflection at the bottom.' }
};

function sim9Select(letter) {
  sim9CurrentLetter = letter;
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    if (b.textContent.includes('Letter ' + letter)) b.classList.add('active');
    else if (b.textContent.startsWith('Letter ')) b.classList.remove('active');
  });
  document.getElementById('sim9LetterChar').textContent = letter;
  sim9Update();
}

function sim9ToggleAxis() {
  sim9IsVertical = !sim9IsVertical;
  document.getElementById('sim9AxisLabel').textContent = sim9IsVertical ? 'Vertical' : 'Horizontal';
  const line = document.getElementById('sim9MirrorLine');
  if (sim9IsVertical) {
    line.style.width = '2px';
    line.style.height = '130px';
  } else {
    line.style.width = '150px';
    line.style.height = '2px';
  }
  sim9Update();
}

function sim9Update() {
  const d = sim9Data[sim9CurrentLetter];
  const fb = document.getElementById('sim9Feedback');
  const isSym = sim9IsVertical ? d.vert : d.horiz;
  const msg = sim9IsVertical ? d.vNote : d.hNote;

  fb.style.color = isSym ? '#34d399' : '#f87171';
  fb.innerHTML = msg;
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🎯 Grid Counter Symmetry Board</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim10Preset('wings')">Pattern: Butterfly</button>
      <button class="sim-btn" onclick="sim10Preset('diamond')">Pattern: Diamond</button>
      <button class="sim-btn" onclick="sim10Clear()">Clear Board</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <p style="font-size:13px; color:#cbd5e1; margin-bottom:8px;">Click any square on the left side (columns 0-2). Its mirror counterpart automatically lights up on the right (columns 3-5)!</p>
    <div id="sim10Grid" style="display:grid; grid-template-columns:repeat(6, 32px); grid-template-rows:repeat(5, 32px); gap:4px; position:relative; background:rgba(0,0,0,0.3); padding:8px; border-radius:10px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central divider line -->
      <div style="position:absolute; left:107px; top:6px; bottom:6px; width:3px; background:#f43f5e; box-shadow:0 0 6px #f43f5e; pointer-events:none; z-index:5;"></div>
    </div>
    <div id="sim10Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:4px 16px; text-align:center;">
      Active Counter Pairs: <span id="sim10Count">0</span> pairs (Symmetry verified across red mirror axis)
    </div>
  </div>
</div>
<script>
const sim10Rows = 5;
const sim10Cols = 6;
let sim10GridState = Array(sim10Rows).fill().map(() => Array(sim10Cols).fill(false));

function sim10Init() {
  const container = document.getElementById('sim10Grid');
  // clear old cells except mirror line
  container.querySelectorAll('.sim10-cell').forEach(c => c.remove());
  
  for (let r = 0; r < sim10Rows; r++) {
    for (let c = 0; c < sim10Cols; c++) {
      const cell = document.createElement('div');
      cell.className = 'sim10-cell';
      cell.id = `sim10_${r}_${c}`;
      cell.style.width = '32px';
      cell.style.height = '32px';
      cell.style.borderRadius = '6px';
      cell.style.background = 'rgba(255,255,255,0.08)';
      cell.style.border = '1px solid rgba(255,255,255,0.12)';
      cell.style.cursor = c < 3 ? 'pointer' : 'default';
      cell.style.display = 'flex';
      cell.style.alignItems = 'center';
      cell.style.justifyContent = 'center';
      cell.style.fontSize = '16px';
      cell.style.transition = 'all 0.2s ease';

      if (c < 3) {
        cell.onclick = () => sim10ToggleLeft(r, c);
      }
      container.appendChild(cell);
    }
  }
  sim10Preset('diamond');
}

function sim10ToggleLeft(r, c) {
  const mirrorC = 5 - c;
  const newState = !sim10GridState[r][c];
  sim10GridState[r][c] = newState;
  sim10GridState[r][mirrorC] = newState;
  sim10Render();
}

function sim10Render() {
  let count = 0;
  for (let r = 0; r < sim10Rows; r++) {
    for (let c = 0; c < sim10Cols; c++) {
      const cell = document.getElementById(`sim10_${r}_${c}`);
      if (!cell) continue;
      if (sim10GridState[r][c]) {
        cell.style.background = c < 3 ? '#3b82f6' : '#10b981';
        cell.textContent = c < 3 ? '🔵' : '🟢';
        if (c < 3) count++;
      } else {
        cell.style.background = 'rgba(255,255,255,0.08)';
        cell.textContent = '';
      }
    }
  }
  document.getElementById('sim10Count').textContent = count;
}

function sim10Clear() {
  for (let r = 0; r < sim10Rows; r++) {
    for (let c = 0; c < sim10Cols; c++) {
      sim10GridState[r][c] = false;
    }
  }
  sim10Render();
}

function sim10Preset(type) {
  sim10Clear();
  if (type === 'diamond') {
    sim10ToggleLeft(0, 2);
    sim10ToggleLeft(1, 1);
    sim10ToggleLeft(2, 0);
    sim10ToggleLeft(3, 1);
    sim10ToggleLeft(4, 2);
  } else if (type === 'wings') {
    sim10ToggleLeft(0, 0);
    sim10ToggleLeft(1, 0);
    sim10ToggleLeft(1, 1);
    sim10ToggleLeft(2, 2);
    sim10ToggleLeft(3, 1);
    sim10ToggleLeft(4, 0);
  }
}

// Initialise on load
setTimeout(sim10Init, 100);
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🧱 Floor Path Tessellation Lab</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Select('square')">Square Tiles</button>
      <button class="sim-btn" onclick="sim11Select('hexagon')">Hexagon Tiles</button>
      <button class="sim-btn" onclick="sim11Select('circle')">Circle Stones (Gaps!)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim11Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);"></svg>
    <div id="sim11Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ✔️ <b>Perfect Tessellation:</b> Square tiles meet edge-to-edge with ZERO gaps and ZERO overlaps! Smooth for fair walking.
    </div>
  </div>
</div>
<script>
function sim11Select(shape) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(shape)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const svg = document.getElementById('sim11Svg');
  const fb = document.getElementById('sim11Feedback');

  if (shape === 'square') {
    let html = '';
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 7; c++) {
        const color = (r + c) % 2 === 0 ? '#d97706' : '#f59e0b';
        html += `<rect x="${c * 34 + 3}" y="${r * 34 + 3}" width="32" height="32" rx="2" fill="${color}" stroke="#1e293b" stroke-width="1.5"/>`;
      }
    }
    svg.innerHTML = html;
    fb.style.color = '#34d399';
    fb.innerHTML = '✔️ <b>Square Tessellation:</b> 4 right angles meet at each corner (4 × 90° = 360°). Leaves 0 gaps, preventing tripping.';
  } else if (shape === 'hexagon') {
    let html = '';
    const r = 18;
    const dx = 1.5 * r;
    const dy = Math.sqrt(3) * r;
    for (let row = 0; row < 5; row++) {
      for (let col = 0; col < 6; col++) {
        const cx = col * dx + 20;
        const cy = row * dy + (col % 2 === 1 ? dy / 2 : 0) + 14;
        let pts = '';
        for (let a = 0; a < 6; a++) {
          const angle = a * Math.PI / 3;
          const px = cx + r * Math.cos(angle);
          const py = cy + r * Math.sin(angle);
          pts += `${px.toFixed(1)},${py.toFixed(1)} `;
        }
        const colVal = (row + col) % 3 === 0 ? '#0284c7' : (row + col) % 3 === 1 ? '#0ea5e9' : '#38bdf8';
        html += `<polygon points="${pts}" fill="${colVal}" stroke="#0f172a" stroke-width="1.5"/>`;
      }
    }
    svg.innerHTML = html;
    fb.style.color = '#34d399';
    fb.innerHTML = '✔️ <b>Hexagon Honeycomb:</b> 3 hexagon angles meet at every vertex (3 × 120° = 360°). Locks tightly like bee comb!';
  } else if (shape === 'circle') {
    let html = '';
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 7; c++) {
        html += `<circle cx="${c * 34 + 18}" cy="${r * 34 + 18}" r="15" fill="#ec4899" stroke="#be185d" stroke-width="2"/>`;
        // Gap markers in between
        if (r < 3 && c < 6) {
          html += `<polygon points="${c * 34 + 35},${r * 34 + 26} ${c * 34 + 43},${r * 34 + 35} ${c * 34 + 35},${r * 34 + 44} ${c * 34 + 27},${r * 34 + 35}" fill="#ef4444" opacity="0.6"/>`;
        }
      }
    }
    svg.innerHTML = html;
    fb.style.color = '#f87171';
    fb.innerHTML = '❌ <b>Tessellation Failure:</b> Round circles leave triangular empty gaps (red marks). Unsuitable for fair footpaths!';
  }
}
setTimeout(() => sim11Select('square'), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">📐 Vertex Angle Sum Checker</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Select('square')">4 Squares (90°×4)</button>
      <button class="sim-btn" onclick="sim12Select('triangle')">6 Triangles (60°×6)</button>
      <button class="sim-btn" onclick="sim12Select('hexagon')">3 Hexagons (120°×3)</button>
      <button class="sim-btn" onclick="sim12Select('pentagon')">3 Pentagons (108°×3)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim12Svg" viewBox="0 0 200 140" style="width:190px; height:133px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central vertex marker -->
      <circle cx="100" cy="70" r="4" fill="#f43f5e"/>
    </svg>
    <div id="sim12Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Total Vertex Angle: <b>360°</b> — Perfect Closure (Tiles the surface!)
    </div>
  </div>
</div>
<script>
function sim12Select(type) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(type)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const svg = document.getElementById('sim12Svg');
  const fb = document.getElementById('sim12Feedback');

  if (type === 'square') {
    svg.innerHTML = `
      <rect x="50" y="20" width="50" height="50" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
      <rect x="100" y="20" width="50" height="50" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/>
      <rect x="50" y="70" width="50" height="50" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>
      <rect x="100" y="70" width="50" height="50" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/>
      <circle cx="100" cy="70" r="5" fill="#f43f5e"/>
      <text x="100" y="132" fill="#e2e8f0" font-size="12" text-anchor="middle" font-weight="bold">90° + 90° + 90° + 90° = 360°</text>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '✔️ <b>Four Right Angles = 360°:</b> Exactly fills the full turn around the vertex without gap or overlap!';
  } else if (type === 'triangle') {
    let p = '';
    const colors = ['#f59e0b', '#fbbf24', '#d97706', '#b45309', '#fde68a', '#78350f'];
    for (let i = 0; i < 6; i++) {
      const a1 = i * Math.PI / 3;
      const a2 = (i + 1) * Math.PI / 3;
      const x1 = 100 + 50 * Math.cos(a1);
      const y1 = 70 + 50 * Math.sin(a1);
      const x2 = 100 + 50 * Math.cos(a2);
      const y2 = 70 + 50 * Math.sin(a2);
      p += `<polygon points="100,70 ${x1.toFixed(1)},${y1.toFixed(1)} ${x2.toFixed(1)},${y2.toFixed(1)}" fill="${colors[i]}" stroke="#1e293b" stroke-width="1.5"/>`;
    }
    p += `<circle cx="100" cy="70" r="5" fill="#f43f5e"/>`;
    p += `<text x="100" y="132" fill="#e2e8f0" font-size="12" text-anchor="middle" font-weight="bold">6 × 60° = 360°</text>`;
    svg.innerHTML = p;
    fb.style.color = '#34d399';
    fb.innerHTML = '✔️ <b>Six Triangles = 360°:</b> Six 60° equilateral angles cluster tightly around the central point!';
  } else if (type === 'hexagon') {
    svg.innerHTML = `
      <polygon points="100,70 100,20 57,45 57,95 100,70" fill="#10b981" stroke="#047857" stroke-width="2"/>
      <polygon points="100,70 100,20 143,45 143,95 100,70" fill="#34d399" stroke="#047857" stroke-width="2"/>
      <polygon points="100,70 57,95 100,120 143,95 100,70" fill="#059669" stroke="#047857" stroke-width="2"/>
      <circle cx="100" cy="70" r="5" fill="#f43f5e"/>
      <text x="100" y="134" fill="#e2e8f0" font-size="12" text-anchor="middle" font-weight="bold">3 × 120° = 360°</text>
    `;
    fb.style.color = '#34d399';
    fb.innerHTML = '✔️ <b>Three Hexagons = 360°:</b> Three 120° angles wrap around the center with zero gap!';
  } else if (type === 'pentagon') {
    svg.innerHTML = `
      <g transform="translate(100, 70)">
        <polygon points="0,0 45,0 59,42 22,69 -14,43" fill="#8b5cf6" stroke="#6d28d9" stroke-width="2"/>
        <polygon points="0,0 -14,43 -51,16 -36,-27 0,0" fill="#a78bfa" stroke="#6d28d9" stroke-width="2"/>
        <polygon points="0,0 -36,-27 -14,-70 32,-70 45,0" fill="#c4b5fd" stroke="#6d28d9" stroke-width="2"/>
        <!-- Gap indicator wedge -->
        <path d="M 0 0 L 45 0 A 45 45 0 0 1 32 -31 Z" fill="#ef4444" opacity="0.8"/>
        <circle cx="0" cy="0" r="5" fill="#f43f5e"/>
        <text x="0" y="60" fill="#f87171" font-size="12" text-anchor="middle" font-weight="bold">3 × 108° = 324° (36° GAP!)</text>
      </g>
    `;
    fb.style.color = '#f87171';
    fb.innerHTML = '❌ <b>Pentagons Fail to Tile:</b> 3 regular pentagons total only 324°, leaving an unfilled 36° wedge!';
  }
}
setTimeout(() => sim12Select('square'), 100);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">✂️ Cut & Paste Repeating Tile Maker</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Step(1)">Step 1: Base Square</button>
      <button class="sim-btn" onclick="sim13Step(2)">Step 2: Cut Triangular Notch</button>
      <button class="sim-btn" onclick="sim13Step(3)">Step 3: Paste on Right</button>
      <button class="sim-btn" onclick="sim13Step(4)">Step 4: Tessellate Floor!</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim13Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);"></svg>
    <div id="sim13Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Step 1: Begin with a regular square tile.
    </div>
  </div>
</div>
<script>
function sim13Step(s) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach((b, idx) => {
    if (idx + 1 === s) b.classList.add('active');
    else b.classList.remove('active');
  });

  const svg = document.getElementById('sim13Svg');
  const fb = document.getElementById('sim13Feedback');

  if (s === 1) {
    svg.innerHTML = `
      <rect x="85" y="35" width="70" height="70" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
      <text x="120" y="75" fill="#ffffff" font-size="13" text-anchor="middle" font-weight="bold">Base Square Tile</text>
    `;
    fb.innerHTML = '<b>Step 1:</b> Start with a standard square tile. Area = 70 × 70 units.';
  } else if (s === 2) {
    svg.innerHTML = `
      <!-- Base with notch missing -->
      <path d="M 85 35 L 155 35 L 155 105 L 85 105 L 85 80 L 105 70 L 85 60 Z" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
      <!-- Cut piece floating -->
      <polygon points="50,60 70,70 50,80" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
      <text x="60" y="50" fill="#ef4444" font-size="11" text-anchor="middle" font-weight="bold">✂️ Cut notch</text>
      <path d="M 72 70 L 82 70" stroke="#f43f5e" stroke-width="2" stroke-dasharray="2 2"/>
    `;
    fb.innerHTML = '<b>Step 2:</b> Cut a triangle out from the left edge. The tile now has a hollow indentation.';
  } else if (s === 3) {
    svg.innerHTML = `
      <!-- Full modified tile with notch on left and protrusion on right -->
      <path d="M 85 35 L 155 35 L 155 60 L 175 70 L 155 80 L 155 105 L 85 105 L 85 80 L 105 70 L 85 60 Z" fill="#10b981" stroke="#34d399" stroke-width="2"/>
      <!-- Slide arrow -->
      <path d="M 95 120 L 145 120" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="120" y="134" fill="#fbbf24" font-size="11" text-anchor="middle" font-weight="bold">Slide across & paste on right</text>
    `;
    fb.innerHTML = '<b>Step 3:</b> Paste the exact triangle onto the right edge! <b>Area is strictly conserved.</b>';
  } else if (s === 4) {
    // Show 3 interlocking tiles
    let html = '';
    const offsets = [20, 90, 160];
    const colors = ['#0284c7', '#0d9488', '#0284c7'];
    offsets.forEach((ox, idx) => {
      html += `<path d="M ${ox} 35 L ${ox + 70} 35 L ${ox + 70} 60 L ${ox + 90} 70 L ${ox + 70} 80 L ${ox + 70} 105 L ${ox} 105 L ${ox} 80 L ${ox + 20} 70 L ${ox} 60 Z" fill="${colors[idx]}" stroke="#ffffff" stroke-width="1.5" opacity="0.9"/>`;
    });
    svg.innerHTML = html;
    fb.innerHTML = '✔️ <b>Step 4: Perfect Tessellation!</b> The right protrusion slots exactly into the left notch of the next tile!';
  }
}
setTimeout(() => sim13Step(1), 100);
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🗺️ Fairground Map & Legend Reader</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Select('chaupal')">Chaupal (Crafts)</button>
      <button class="sim-btn" onclick="sim14Select('lake')">Kund Lake</button>
      <button class="sim-btn" onclick="sim14Select('food')">Food Court</button>
      <button class="sim-btn" onclick="sim14Select('gate1')">Gate 1 & Parking</button>
      <button class="sim-btn" onclick="sim14Select('wheel')">Giant Wheel</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim14Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Compass Rose -->
      <g transform="translate(215, 25)">
        <circle cx="0" cy="0" r="14" fill="rgba(0,0,0,0.5)" stroke="#94a3b8" stroke-width="1"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#f43f5e" stroke-width="2"/>
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#94a3b8" stroke-width="2"/>
        <text x="0" y="-14" fill="#f43f5e" font-size="9" text-anchor="middle" font-weight="bold">N</text>
        <text x="0" y="21" fill="#94a3b8" font-size="8" text-anchor="middle">S</text>
        <text x="18" y="3" fill="#94a3b8" font-size="8" text-anchor="middle">E</text>
        <text x="-18" y="3" fill="#94a3b8" font-size="8" text-anchor="middle">W</text>
      </g>
      <!-- Paths -->
      <line x1="40" y1="110" x2="120" y2="70" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
      <line x1="120" y1="70" x2="120" y2="25" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
      <line x1="120" y1="70" x2="180" y2="85" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>

      <!-- Gate 1 (SW) -->
      <rect id="sim14_gate1" x="20" y="100" width="36" height="24" rx="4" fill="#3b82f6" stroke="#60a5fa" stroke-width="1.5"/>
      <text x="38" y="116" fill="#ffffff" font-size="9" text-anchor="middle" font-weight="bold">🚪 Gate 1</text>

      <!-- Chaupal (Center) -->
      <circle id="sim14_chaupal" cx="120" cy="70" r="20" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
      <text x="120" y="74" fill="#000000" font-size="9" text-anchor="middle" font-weight="bold">🎪 Chaupal</text>

      <!-- Kund Lake (North) -->
      <ellipse id="sim14_lake" cx="120" cy="22" rx="30" ry="14" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <text x="120" y="25" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">🌊 Kund Lake</text>

      <!-- Food Court (East) -->
      <rect id="sim14_food" x="165" y="75" width="34" height="22" rx="4" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
      <text x="182" y="89" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">🍲 Food</text>

      <!-- Giant Wheel (SE) -->
      <circle id="sim14_wheel" cx="180" cy="115" r="14" fill="#ec4899" stroke="#f472b6" stroke-width="1.5"/>
      <text x="180" y="119" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">🎡 Wheel</text>
    </svg>
    <div id="sim14Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🎪 <b>Central Chaupal:</b> Located at the fair hub. Walk North to reach the ancient Kund Lake, or East for Food Court.
    </div>
  </div>
</div>
<script>
function sim14Select(place) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(place)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const ids = ['gate1', 'chaupal', 'lake', 'food', 'wheel'];
  ids.forEach(id => {
    const el = document.getElementById('sim14_' + id);
    if (el) el.setAttribute('stroke-width', id === place ? '3.5' : '1.5');
  });

  const fb = document.getElementById('sim14Feedback');
  if (place === 'chaupal') {
    fb.innerHTML = '🎪 <b>Chaupal (Center):</b> Crafts exhibition stage. Direct North leads to Kund Lake; East leads to Food Court.';
  } else if (place === 'lake') {
    fb.innerHTML = '🌊 <b>Kund Lake (North):</b> Sits directly North of the central Chaupal stage along the main avenue.';
  } else if (place === 'food') {
    fb.innerHTML = '🍲 <b>Food Court (East):</b> Located East of Chaupal. Smells of hot jalebis and parathas!';
  } else if (place === 'gate1') {
    fb.innerHTML = '🚪 <b>Gate 1 & Parking (South-West):</b> Main ticket entry terminal and shuttle bus drop-off.';
  } else if (place === 'wheel') {
    fb.innerHTML = '🎡 <b>Giant Wheel (South-East):</b> Amusement zone located South-East of the central Chaupal.';
  }
}
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🧭 Colored Pathway Navigator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Route('golden')">Golden Lane (Crafts)</button>
      <button class="sim-btn" onclick="sim15Route('red')">Red Lane (Terracotta)</button>
      <button class="sim-btn" onclick="sim15Route('blue')">Blue Lane (Textiles)</button>
      <button class="sim-btn" onclick="sim15Route('green')">Green Lane (Food)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim15Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central Hub -->
      <circle cx="120" cy="70" r="16" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
      <text x="120" y="74" fill="#f8fafc" font-size="8" text-anchor="middle" font-weight="bold">START HUB</text>
      <!-- Golden Path (Straight Up / North) -->
      <path id="sim15_p_golden" d="M 120 54 L 120 18" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
      <text x="120" y="12" fill="#fbbf24" font-size="8" text-anchor="middle" font-weight="bold">Crafts (North)</text>

      <!-- Red Path (East) -->
      <path id="sim15_p_red" d="M 136 70 L 210 70" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
      <text x="210" y="62" fill="#f87171" font-size="8" text-anchor="middle" font-weight="bold">Terracotta (East)</text>

      <!-- Blue Path (South) -->
      <path id="sim15_p_blue" d="M 120 86 L 120 125" stroke="#3b82f6" stroke-width="6" stroke-linecap="round"/>
      <text x="120" y="136" fill="#60a5fa" font-size="8" text-anchor="middle" font-weight="bold">Textiles (South)</text>

      <!-- Green Path (West) -->
      <path id="sim15_p_green" d="M 104 70 L 30 70" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
      <text x="30" y="62" fill="#34d399" font-size="8" text-anchor="middle" font-weight="bold">Food (West)</text>

      <!-- Animated Walker Marker -->
      <circle id="sim15Marker" cx="120" cy="35" r="7" fill="#ffffff" stroke="#f43f5e" stroke-width="2" style="transition:all 0.4s ease;"/>
    </svg>
    <div id="sim15Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🟡 <b>Golden Lane:</b> Head straight North 50 paces to visit brass metal workers and woodcarvers.
    </div>
  </div>
</div>
<script>
function sim15Route(route) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(route)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const marker = document.getElementById('sim15Marker');
  const fb = document.getElementById('sim15Feedback');

  if (route === 'golden') {
    marker.setAttribute('cx', '120');
    marker.setAttribute('cy', '25');
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🟡 <b>Golden Lane:</b> Walk straight North from Central Hub. Leads directly to master woodcraftsmen.';
  } else if (route === 'red') {
    marker.setAttribute('cx', '190');
    marker.setAttribute('cy', '70');
    fb.style.color = '#f87171';
    fb.innerHTML = '🔴 <b>Red Lane:</b> Turn 90° East from Central Hub. Leads to terracotta clay pots and clay horse artisans.';
  } else if (route === 'blue') {
    marker.setAttribute('cx', '120');
    marker.setAttribute('cy', '115');
    fb.style.color = '#60a5fa';
    fb.innerHTML = '🔵 <b>Blue Lane:</b> Head South from Central Hub. Leads directly to handloom silk sarees and printed dupattas.';
  } else if (route === 'green') {
    marker.setAttribute('cx', '50');
    marker.setAttribute('cy', '70');
    fb.style.color = '#34d399';
    fb.innerHTML = '🟢 <b>Green Lane:</b> Turn 90° West from Central Hub. Follow the aroma to hot regional food stalls!';
  }
}
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🏁 Fair Hedge Maze Pathfinder</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim16Move(0, -1)">⬆️ Up</button>
      <button class="sim-btn" onclick="sim16Move(0, 1)">⬇️ Down</button>
      <button class="sim-btn" onclick="sim16Move(-1, 0)">⬅️ Left</button>
      <button class="sim-btn" onclick="sim16Move(1, 0)">➡️ Right</button>
      <button class="sim-btn" onclick="sim16Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <div id="sim16Board" style="display:grid; grid-template-columns:repeat(5, 34px); grid-template-rows:repeat(5, 34px); gap:3px; background:rgba(0,0,0,0.3); padding:8px; border-radius:10px; border:1px solid rgba(255,255,255,0.15);"></div>
    <div id="sim16Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:4px 16px; text-align:center;">
      Navigate from 🟢 Start (0,0) to 🏁 Exit (4,4) through open green pathways! Avoid hedge walls.
    </div>
  </div>
</div>
<script>
// 5x5 Maze: 0=open, 1=wall
const sim16Maze = [
  [0, 0, 1, 0, 0],
  [1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 1, 0]
];
let sim16Pos = { r: 0, c: 0 };

function sim16Init() {
  const b = document.getElementById('sim16Board');
  b.innerHTML = '';
  for (let r = 0; r < 5; r++) {
    for (let c = 0; c < 5; c++) {
      const cell = document.createElement('div');
      cell.id = `sim16_${r}_${c}`;
      cell.style.width = '34px';
      cell.style.height = '34px';
      cell.style.borderRadius = '5px';
      cell.style.display = 'flex';
      cell.style.alignItems = 'center';
      cell.style.justifyContent = 'center';
      cell.style.fontSize = '16px';
      cell.style.fontWeight = 'bold';

      if (sim16Maze[r][c] === 1) {
        cell.style.background = '#334155';
        cell.textContent = '🌿';
      } else {
        cell.style.background = 'rgba(255,255,255,0.06)';
      }
      b.appendChild(cell);
    }
  }
  sim16Render();
}

function sim16Render() {
  for (let r = 0; r < 5; r++) {
    for (let c = 0; c < 5; c++) {
      const cell = document.getElementById(`sim16_${r}_${c}`);
      if (sim16Maze[r][c] === 1) continue;
      cell.textContent = '';
      cell.style.background = 'rgba(255,255,255,0.06)';

      if (r === 0 && c === 0) cell.textContent = '🟢';
      if (r === 4 && c === 4) cell.textContent = '🏁';
      if (r === sim16Pos.r && c === sim16Pos.c) {
        cell.textContent = '🚶';
        cell.style.background = '#0284c7';
      }
    }
  }

  const fb = document.getElementById('sim16Feedback');
  if (sim16Pos.r === 4 && sim16Pos.c === 4) {
    fb.style.color = '#34d399';
    fb.innerHTML = '🎉 <b>Congratulations!</b> You navigated the hedge maze to the Exit Gate without getting lost!';
  } else {
    fb.style.color = '#38bdf8';
    fb.innerHTML = `Current Position: (${sim16Pos.r}, ${sim16Pos.c}) — Follow open pathways toward 🏁 (4,4).`;
  }
}

function sim16Move(dc, dr) {
  const nr = sim16Pos.r + dr;
  const nc = sim16Pos.c + dc;
  if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5) {
    if (sim16Maze[nr][nc] === 0) {
      sim16Pos = { r: nr, c: nc };
      sim16Render();
    } else {
      const fb = document.getElementById('sim16Feedback');
      fb.style.color = '#f87171';
      fb.innerHTML = '⛔ Hedge Wall! Backtrack and find an open lane.';
    }
  }
}

function sim16Reset() {
  sim16Pos = { r: 0, c: 0 };
  sim16Render();
}

setTimeout(sim16Init, 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9 to 16).")
    for k in sorted(sims_part2.keys()):
        print(f"Sim {k}: length {len(sims_part2[k])} chars")

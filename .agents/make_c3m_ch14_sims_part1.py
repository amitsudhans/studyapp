#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🏺 Craft Fair Symmetry Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Select('lamp')">Brass Lamp (Symmetrical)</button>
      <button class="sim-btn" onclick="sim1Select('pot')">Clay Pot (Symmetrical)</button>
      <button class="sim-btn" onclick="sim1Select('kettle')">Tea Kettle (Asymmetrical)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Visual Object with Mirror Axis -->
    <svg id="sim1Svg" viewBox="0 0 200 140" style="width:180px; height:126px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central Line of Symmetry -->
      <line x1="100" y1="10" x2="100" y2="130" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3"/>
      <!-- Symmetrical Lamp Default -->
      <g id="sim1Object">
        <!-- Base -->
        <path d="M 60 120 L 140 120 L 125 105 L 75 105 Z" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
        <!-- Stem -->
        <rect x="95" y="45" width="10" height="60" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
        <!-- Bowl -->
        <path d="M 50 45 C 50 70 150 70 150 45 Z" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
        <!-- Flame -->
        <path d="M 100 20 Q 92 38 100 45 Q 108 38 100 20 Z" fill="#ef4444"/>
      </g>
    </svg>
    <div id="sim1Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ✔️ Symmetrical: The dashed red line divides the brass lamp into identical left and right halves!
    </div>
  </div>
</div>
<script>
function sim1Select(obj) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(obj));
  });
  const g = document.getElementById('sim1Object');
  const fb = document.getElementById('sim1Feedback');

  if (obj === 'lamp') {
    g.innerHTML = `
      <path d="M 60 120 L 140 120 L 125 105 L 75 105 Z" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
      <rect x="95" y="45" width="10" height="60" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
      <path d="M 50 45 C 50 70 150 70 150 45 Z" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
      <path d="M 100 20 Q 92 38 100 45 Q 108 38 100 20 Z" fill="#ef4444"/>
    `;
    fb.innerHTML = '✔️ <b style="color:#34d399;">Symmetrical</b>: Both halves of the ceremonial brass lamp match identically!';
  } else if (obj === 'pot') {
    g.innerHTML = `
      <ellipse cx="100" cy="80" rx="45" ry="35" fill="#b45309" stroke="#d97706" stroke-width="2"/>
      <ellipse cx="100" cy="45" rx="25" ry="8" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
      <rect x="85" y="45" width="30" height="15" fill="#b45309"/>
    `;
    fb.innerHTML = '✔️ <b style="color:#34d399;">Symmetrical</b>: Terracotta pot has bilateral symmetry across the vertical center line.';
  } else if (obj === 'kettle') {
    g.innerHTML = `
      <!-- Body -->
      <circle cx="100" cy="80" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <!-- Spout on right -->
      <path d="M 125 70 L 165 50 L 160 45 L 125 60 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <!-- Handle on left -->
      <path d="M 75 60 C 45 60 45 100 75 100" fill="none" stroke="#38bdf8" stroke-width="6"/>
      <!-- Lid -->
      <path d="M 85 45 L 115 45 L 100 35 Z" fill="#0369a1"/>
    `;
    fb.innerHTML = '❌ <b style="color:#f43f5e;">Asymmetrical</b>: Handle is on the left, spout on the right. Halves do NOT match!';
  }
}
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">📿 Bead Mala Bilateral Symmetry Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2Set('sym1')">Symmetrical Pattern A</button>
      <button class="sim-btn" onclick="sim2Set('sym2')">Symmetrical Pattern B</button>
      <button class="sim-btn" onclick="sim2Set('asym')">Asymmetrical Pattern</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Bead Strand Container -->
    <div style="display:flex; align-items:center; justify-content:center; gap:8px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:16px 24px; max-width:540px; position:relative;" id="sim2BeadsWrap">
      <!-- Injected 8 beads -->
    </div>
    <!-- Central dividing line label -->
    <div style="font-size:11px; color:#f43f5e; font-weight:bold; margin-top:6px;">
      ▲ Midpoint Line of Symmetry (Fold Here) ▲
    </div>
    <div id="sim2Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Pattern reads identical from left and right: Red-Yellow-Yellow-Red | Red-Yellow-Yellow-Red!
    </div>
  </div>
</div>
<script>
function sim2Set(mode) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  const wrap = document.getElementById('sim2BeadsWrap');
  wrap.innerHTML = '';
  const fb = document.getElementById('sim2Feedback');

  let beads = [];
  if (mode === 'sym1') {
    document.querySelectorAll('#sim2 .sim-controls button')[0].classList.add('active');
    beads = ['#ef4444', '#fbbf24', '#fbbf24', '#ef4444', '#ef4444', '#fbbf24', '#fbbf24', '#ef4444'];
    fb.innerHTML = '✔️ <b style="color:#34d399;">Symmetrical</b>: R-Y-Y-R | R-Y-Y-R. Folding at midpoint aligns matching colors!';
  } else if (mode === 'sym2') {
    document.querySelectorAll('#sim2 .sim-controls button')[1].classList.add('active');
    beads = ['#fbbf24', '#ef4444', '#ef4444', '#fbbf24', '#fbbf24', '#ef4444', '#ef4444', '#fbbf24'];
    fb.innerHTML = '✔️ <b style="color:#34d399;">Symmetrical</b>: Y-R-R-Y | Y-R-R-Y. Left half mirrors right half perfectly!';
  } else if (mode === 'asym') {
    document.querySelectorAll('#sim2 .sim-controls button')[2].classList.add('active');
    beads = ['#ef4444', '#ef4444', '#ef4444', '#ef4444', '#fbbf24', '#fbbf24', '#fbbf24', '#fbbf24'];
    fb.innerHTML = '❌ <b style="color:#f43f5e;">Asymmetrical</b>: 4 Reds followed by 4 Yellows. Folding lands Red on Yellow!';
  }

  beads.forEach((color, idx) => {
    // Add central separator after 4th bead
    if (idx === 4) {
      wrap.innerHTML += '<div style="width:2px; height:40px; background:#f43f5e; margin:0 4px;"></div>';
    }
    wrap.innerHTML += '<div style="width:36px; height:36px; border-radius:50%; background:' + color + '; border:2px solid #fff; box-shadow:0 2px 6px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#000;">' + (color === '#ef4444' ? 'R' : 'Y') + '</div>';
  });
}
sim2Set('sym1');
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🎨 Tamil Nadu Kolam Dot-Grid Symmetrical Builder</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Stage(1)">Stage 1: 5×5 Dot Grid (Pulli)</button>
      <button class="sim-btn" onclick="sim3Stage(2)">Stage 2: Symmetrical Curves</button>
      <button class="sim-btn" onclick="sim3Stage(3)">Stage 3: 4-Way Symmetrical Masterpiece</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- 5x5 Dot Canvas SVG -->
    <svg viewBox="0 0 200 160" style="width:180px; height:144px; background:rgba(0,0,0,0.4); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Symmetry Axes -->
      <line x1="100" y1="10" x2="100" y2="150" stroke="rgba(244,63,94,0.4)" stroke-dasharray="3 3"/>
      <line x1="20" y1="80" x2="180" y2="80" stroke="rgba(244,63,94,0.4)" stroke-dasharray="3 3"/>
      
      <!-- Injected Kolam Curves -->
      <g id="sim3Curves"></g>
      
      <!-- 5x5 Dots Grid -->
      <g id="sim3Dots">
        <!-- Render 25 dots -->
      </g>
    </svg>
    <div id="sim3Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Stage 1: A 5×5 regular dot grid (pulli) laid out with equal spacing.
    </div>
  </div>
</div>
<script>
function sim3RenderDots() {
  const dotsG = document.getElementById('sim3Dots');
  let s = '';
  for (let r = 0; r < 5; r++) {
    for (let c = 0; c < 5; c++) {
      const cx = 40 + c * 30;
      const cy = 20 + r * 30;
      s += '<circle cx="' + cx + '" cy="' + cy + '" r="3" fill="#cbd5e1"/>';
    }
  }
  dotsG.innerHTML = s;
}

function sim3Stage(stg) {
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes('(' + stg + ')'));
  });
  const curvesG = document.getElementById('sim3Curves');
  const fb = document.getElementById('sim3Feedback');

  if (stg === 1) {
    curvesG.innerHTML = '';
    fb.innerHTML = 'Stage 1: <b>5×5 Dot Grid (Pulli)</b> provides the geometric reference points.';
  } else if (stg === 2) {
    curvesG.innerHTML = `
      <path d="M 100 20 Q 130 50 100 80 Q 70 50 100 20 Z" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 40 80 Q 70 50 100 80 Q 70 110 40 80 Z" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 160 80 Q 130 50 100 80 Q 130 110 160 80 Z" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 100 140 Q 130 110 100 80 Q 70 110 100 140 Z" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    `;
    fb.innerHTML = 'Stage 2: Symmetrical loops connect the dots across horizontal and vertical mirror axes.';
  } else if (stg === 3) {
    curvesG.innerHTML = `
      <path d="M 100 20 Q 130 50 100 80 Q 70 50 100 20 Z" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 40 80 Q 70 50 100 80 Q 70 110 40 80 Z" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 160 80 Q 130 50 100 80 Q 130 110 160 80 Z" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 100 140 Q 130 110 100 80 Q 70 110 100 140 Z" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="100" cy="80" r="18" fill="rgba(251,191,36,0.3)" stroke="#fbbf24" stroke-width="2"/>
    `;
    fb.innerHTML = 'Stage 3: <b>4-Way Symmetrical Kolam</b>: Perfectly balanced top-to-bottom and left-to-right!';
  }
}
sim3RenderDots();
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">📐 Fold Line Symmetry Tester & Crease Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4SetShape('square')">Square (4 Lines)</button>
      <button class="sim-btn" onclick="sim4SetShape('rect')">Rectangle (2 Lines)</button>
      <button class="sim-btn" onclick="sim4SetShape('eqtri')">Equilateral Triangle (3 Lines)</button>
      <button class="sim-btn" onclick="sim4SetShape('scalene')">Scalene Triangle (0 Lines)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- Shape Display with Crease Lines -->
    <svg id="sim4Svg" viewBox="0 0 200 150" style="width:180px; height:135px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <g id="sim4ShapeGroup"></g>
    </svg>
    <div id="sim4Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      A square has 4 lines of symmetry: vertical, horizontal, and 2 diagonals!
    </div>
  </div>
</div>
<script>
function sim4SetShape(shape) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(shape));
  });
  const g = document.getElementById('sim4ShapeGroup');
  const fb = document.getElementById('sim4Feedback');

  if (shape === 'square') {
    g.innerHTML = `
      <rect x="50" y="25" width="100" height="100" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- 4 Lines of symmetry -->
      <line x1="100" y1="10" x2="100" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <line x1="35" y1="75" x2="165" y2="75" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <line x1="35" y1="10" x2="165" y2="140" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 3"/>
      <line x1="35" y1="140" x2="165" y2="10" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 3"/>
    `;
    fb.innerHTML = 'Square: <b style="color:#34d399;">4 lines of symmetry</b> (Vertical, Horizontal, and Both Diagonals).';
  } else if (shape === 'rect') {
    g.innerHTML = `
      <rect x="35" y="45" width="130" height="60" fill="rgba(245,158,11,0.2)" stroke="#fbbf24" stroke-width="2.5"/>
      <!-- 2 Lines of symmetry -->
      <line x1="100" y1="25" x2="100" y2="125" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <line x1="15" y1="75" x2="185" y2="75" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
    `;
    fb.innerHTML = 'Rectangle: <b style="color:#fbbf24;">2 lines of symmetry</b> (Vertical & Horizontal only; diagonals do NOT match!).';
  } else if (shape === 'eqtri') {
    g.innerHTML = `
      <polygon points="100,20 40,125 160,125" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="2.5"/>
      <!-- 3 Lines of symmetry -->
      <line x1="100" y1="10" x2="100" y2="135" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <line x1="30" y1="130" x2="135" y2="65" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
      <line x1="170" y1="130" x2="65" y2="65" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
    `;
    fb.innerHTML = 'Equilateral Triangle: <b style="color:#34d399;">3 lines of symmetry</b> from each vertex to opposite side.';
  } else if (shape === 'scalene') {
    g.innerHTML = `
      <polygon points="60,25 30,125 175,100" fill="rgba(244,63,94,0.2)" stroke="#f43f5e" stroke-width="2.5"/>
    `;
    fb.innerHTML = 'Scalene Triangle: <b style="color:#f43f5e;">0 lines of symmetry</b>! Unequal sides prevent any matching fold.';
  }
}
sim4SetShape('square');
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🌸 Regional Rangoli Symmetry (Pookalam vs Aipan)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5Select('pookalam')">Pookalam (Kerala Radial)</button>
      <button class="sim-btn" onclick="sim5Select('aipan')">Aipan (Uttarakhand Linear)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Art Showcase Display -->
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:12px 20px; max-width:500px; width:100%; display:flex; align-items:center; gap:16px;">
      <svg id="sim5ArtSvg" viewBox="0 0 120 120" style="width:100px; height:100px; flex-shrink:0;">
        <!-- Injected Art -->
      </svg>
      <div>
        <div id="sim5Title" style="font-size:16px; font-weight:bold; color:#fbbf24;">Pookalam Floral Rangoli</div>
        <div id="sim5Desc" style="font-size:12px; color:#cbd5e1; margin-top:4px; line-height:1.4;">
          Concentric floral rings celebrating Onam harvest in Kerala. Boasts infinite radial symmetry lines!
        </div>
      </div>
    </div>
    <div id="sim5Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Pookalam petals radiate outward in circular concentric symmetry.
    </div>
  </div>
</div>
<script>
function sim5Select(art) {
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(art));
  });
  const svg = document.getElementById('sim5ArtSvg');
  const title = document.getElementById('sim5Title');
  const desc = document.getElementById('sim5Desc');
  const fb = document.getElementById('sim5Feedback');

  if (art === 'pookalam') {
    title.innerText = 'Pookalam Floral Carpet';
    desc.innerHTML = 'Crafted during Onam in Kerala using multi-colored flower petals. Circular design has multiple radial lines of symmetry radiating from the center.';
    fb.innerHTML = '<b>Pookalam (Kerala)</b>: Concentric circular flower petals create magnificent radial symmetry.';
    svg.innerHTML = `
      <circle cx="60" cy="60" r="50" fill="#f59e0b"/>
      <circle cx="60" cy="60" r="38" fill="#ef4444"/>
      <circle cx="60" cy="60" r="26" fill="#10b981"/>
      <circle cx="60" cy="60" r="14" fill="#fbbf24"/>
      <circle cx="60" cy="60" r="5" fill="#fff"/>
      <line x1="60" y1="10" x2="60" y2="110" stroke="rgba(255,255,255,0.4)" stroke-dasharray="2 2"/>
      <line x1="10" y1="60" x2="110" y2="60" stroke="rgba(255,255,255,0.4)" stroke-dasharray="2 2"/>
    `;
  } else if (art === 'aipan') {
    title.innerText = 'Aipan Folk Art of Uttarakhand';
    desc.innerHTML = 'Painted on red ochre clay courtyards using white rice flour paste (biswar). Features central sacred lotus motifs and symmetrical border chowkis.';
    fb.innerHTML = '<b>Aipan (Uttarakhand)</b>: White rice paste on red clay highlights strict vertical & horizontal mirror axes.';
    svg.innerHTML = `
      <rect x="10" y="10" width="100" height="100" fill="#991b1b" stroke="#7f1d1d" stroke-width="2"/>
      <rect x="25" y="25" width="70" height="70" fill="none" stroke="#fff" stroke-width="2"/>
      <polygon points="60,30 90,60 60,90 30,60" fill="none" stroke="#fff" stroke-width="2"/>
      <circle cx="60" cy="60" r="10" fill="#fff"/>
      <line x1="60" y1="10" x2="60" y2="110" stroke="rgba(251,191,36,0.6)" stroke-dasharray="2 2"/>
    `;
  }
}
sim5Select('pookalam');
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🦋 Symmetrical Grid Pattern Completer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6ToggleHalf(true)">Left Half Only</button>
      <button class="sim-btn" onclick="sim6ToggleHalf(false)">Complete Symmetrical Diya</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- Grid Canvas with Diya Outline -->
    <svg viewBox="0 0 200 140" style="width:180px; height:126px; background:rgba(0,0,0,0.4); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Central Mirror Line -->
      <line x1="100" y1="10" x2="100" y2="130" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3 3"/>
      <!-- Left Half Diya (Always visible) -->
      <path d="M 100 80 Q 50 80 50 110 L 100 110 Z" fill="rgba(217,119,6,0.4)" stroke="#fbbf24" stroke-width="2"/>
      <path d="M 100 40 Q 80 65 100 80 Z" fill="rgba(239,68,68,0.5)" stroke="#ef4444" stroke-width="2"/>
      <!-- Right Half Diya (Toggled) -->
      <g id="sim6RightHalf" style="display:none;">
        <path d="M 100 80 Q 150 80 150 110 L 100 110 Z" fill="rgba(217,119,6,0.4)" stroke="#fbbf24" stroke-width="2"/>
        <path d="M 100 40 Q 120 65 100 80 Z" fill="rgba(239,68,68,0.5)" stroke="#ef4444" stroke-width="2"/>
      </g>
    </svg>
    <div id="sim6Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Left half shown. Click "Complete Symmetrical Diya" to reflect across the dashed red line!
    </div>
  </div>
</div>
<script>
function sim6ToggleHalf(onlyLeft) {
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  const rh = document.getElementById('sim6RightHalf');
  const fb = document.getElementById('sim6Feedback');

  if (onlyLeft) {
    document.querySelectorAll('#sim6 .sim-controls button')[0].classList.add('active');
    rh.style.display = 'none';
    fb.innerHTML = 'Left half drawn: Corner points sit at distances 20px and 50px from the center line.';
  } else {
    document.querySelectorAll('#sim6 .sim-controls button')[1].classList.add('active');
    rh.style.display = 'block';
    fb.innerHTML = '🎉 <b>Reflected Successfully!</b> Each point on the right mirrors the exact horizontal distance.';
  }
}
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🐱 Folded Paper Animal Mask Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Step(1)">1: Fold Paper in Half</button>
      <button class="sim-btn" onclick="sim7Step(2)">2: Draw & Cut Half Face</button>
      <button class="sim-btn" onclick="sim7Step(3)">3: Unfold Symmetrical Mask</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- Mask SVG Container -->
    <svg viewBox="0 0 200 140" style="width:180px; height:126px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <g id="sim7Graphic"></g>
    </svg>
    <div id="sim7Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Step 1: Fold square card paper in half along central vertical crease line.
    </div>
  </div>
</div>
<script>
function sim7Step(stg) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes('(' + stg + ')'));
  });
  const g = document.getElementById('sim7Graphic');
  const fb = document.getElementById('sim7Feedback');

  if (stg === 1) {
    g.innerHTML = `
      <!-- Folded half sheet -->
      <rect x="50" y="20" width="50" height="100" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
      <line x1="100" y1="15" x2="100" y2="125" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <text x="100" y="135" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">Crease</text>
    `;
    fb.innerHTML = 'Step 1: Square card paper folded in half along the central vertical crease line.';
  } else if (stg === 2) {
    g.innerHTML = `
      <rect x="50" y="20" width="50" height="100" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="1"/>
      <line x1="100" y1="15" x2="100" y2="125" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
      <!-- Cutout half of cat face -->
      <path d="M 100 30 L 60 20 L 75 60 C 60 80 60 100 100 110 Z" fill="rgba(245,158,11,0.3)" stroke="#fbbf24" stroke-width="2"/>
      <circle cx="85" cy="65" r="7" fill="#ef4444"/>
    `;
    fb.innerHTML = 'Step 2: Draw half face along crease. One cut slices through both layers simultaneously!';
  } else if (stg === 3) {
    g.innerHTML = `
      <!-- Complete unfolded symmetrical cat mask -->
      <path d="M 100 30 L 60 20 L 75 60 C 60 80 60 100 100 110 C 140 100 140 80 125 60 L 140 20 Z" fill="rgba(245,158,11,0.4)" stroke="#fbbf24" stroke-width="2.5"/>
      <!-- Symmetrical Eyeholes -->
      <circle cx="85" cy="65" r="7" fill="#1e293b" stroke="#fff" stroke-width="1.5"/>
      <circle cx="115" cy="65" r="7" fill="#1e293b" stroke="#fff" stroke-width="1.5"/>
      <polygon points="100,80 95,88 105,88" fill="#ef4444"/>
    `;
    fb.innerHTML = '🎉 <b>Unfolded Mask:</b> Flawless bilateral symmetry! Eyeholes sit at identical heights for easy vision.';
  }
}
sim7Step(1);
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🎭 The Painter's Mirror Trick Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Test('face')">Face Portrait (Symmetrical)</button>
      <button class="sim-btn" onclick="sim8Test('rupee')">50-Rupee Note (Clever Payment)</button>
      <button class="sim-btn" onclick="sim8Test('kettle')">Teapot (Asymmetrical)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Mirror Reflection Split Box -->
    <div style="display:flex; justify-content:center; align-items:center; gap:0; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:10px; max-width:480px; width:100%;">
      <!-- Real Object Half -->
      <div id="sim8Real" style="width:48%; background:rgba(56,189,248,0.1); border-right:2px dashed #f43f5e; padding:10px; text-align:center;">
        <span style="font-size:10px; color:#38bdf8; font-weight:bold; display:block;">REAL HALF CANVAS</span>
        <div id="sim8RealContent" style="font-size:32px; margin-top:4px;">👤</div>
      </div>
      <!-- Mirror Reflection Half -->
      <div id="sim8Mirror" style="width:48%; background:rgba(251,191,36,0.1); padding:10px; text-align:center;">
        <span style="font-size:10px; color:#fbbf24; font-weight:bold; display:block;">MIRROR REFLECTION</span>
        <div id="sim8MirrorContent" style="font-size:32px; margin-top:4px; transform:scaleX(-1);">👤</div>
      </div>
    </div>
    <div id="sim8Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Face has bilateral symmetry: The mirror reflection successfully completes the full portrait!
    </div>
  </div>
</div>
<script>
function sim8Test(item) {
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(item));
  });
  const rc = document.getElementById('sim8RealContent');
  const mc = document.getElementById('sim8MirrorContent');
  const fb = document.getElementById('sim8Feedback');

  if (item === 'face') {
    rc.innerHTML = 'Half Face 🌓';
    mc.innerHTML = '🌗 Reflected Half';
    mc.style.transform = 'scaleX(1)';
    fb.innerHTML = '✔️ Symmetrical Face: The mirror reflection produces a believable full portrait.';
  } else if (item === 'rupee') {
    rc.innerHTML = '💵 ₹50 Note';
    mc.innerHTML = '💵 ₹50 Reflection';
    mc.style.transform = 'scaleX(-1)';
    fb.innerHTML = '🪙 <b>Clever Child Trick:</b> "You gave me half a portrait; I give you 50 rupees by a mirror to make 100!"';
  } else if (item === 'kettle') {
    rc.innerHTML = '🫖 Handle Side';
    mc.innerHTML = '🫖 Handle Side';
    mc.style.transform = 'scaleX(-1)';
    fb.innerHTML = '❌ <b>Asymmetrical Failure:</b> Mirroring the handle side gives a kettle with 2 handles and NO spout!';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1 to 8).")
    for k in sorted(sims_part1.keys()):
        print(f"Sim {k}: length {len(sims_part1[k])} chars")

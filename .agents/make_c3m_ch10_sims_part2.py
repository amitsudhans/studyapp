#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party!
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🪢 Knotted Metre Rope Workshop</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Step(1)">1. Tie Start Knot (0 cm)</button>
      <button class="sim-btn" onclick="sim9Step(2)">2. Stretch to 100 cm</button>
      <button class="sim-btn" onclick="sim9Step(3)">3. Tie End Knot (1 m)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:580px; height:60px; background:#1e293b; border:2px solid #475569; border-radius:8px; display:flex; align-items:center; padding:0 30px; margin-bottom:12px;">
      <!-- Metre ruler ticks -->
      <div style="position:absolute; left:30px; top:4px; font-size:10px; color:#94a3b8; font-weight:bold;">0 cm</div>
      <div style="position:absolute; left:50%; transform:translateX(-50%); top:4px; font-size:10px; color:#94a3b8; font-weight:bold;">50 cm</div>
      <div style="position:absolute; right:30px; top:4px; font-size:10px; color:#94a3b8; font-weight:bold;">100 cm (1 Metre)</div>

      <!-- Rope cord -->
      <div id="sim9Rope" style="position:absolute; left:30px; height:6px; width:0; background:#f59e0b; border-radius:3px; transition:width 0.5s ease;"></div>

      <!-- Knots -->
      <div id="sim9Knot1" style="position:absolute; left:22px; width:16px; height:16px; background:#b45309; border:2px solid #fbbf24; border-radius:50%; opacity:0; transition:opacity 0.3s ease;"></div>
      <div id="sim9Knot2" style="position:absolute; right:22px; width:16px; height:16px; background:#b45309; border:2px solid #fbbf24; border-radius:50%; opacity:0; transition:opacity 0.3s ease;"></div>
    </div>
    <div id="sim9Feedback" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Step 1: Tie a secure knot at the zero mark of the measuring rod.
    </div>
  </div>
</div>
<script>
function sim9Step(st) {
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + st));
  });

  const rope = document.getElementById('sim9Rope');
  const k1 = document.getElementById('sim9Knot1');
  const k2 = document.getElementById('sim9Knot2');
  const fb = document.getElementById('sim9Feedback');

  if (st === 1) {
    k1.style.opacity = '1';
    k2.style.opacity = '0';
    rope.style.width = '0px';
    fb.innerHTML = '🪢 <span style="color:#fbbf24;">Start Knot Tied at 0 cm!</span> Ready to stretch along ruler.';
  } else if (st === 2) {
    k1.style.opacity = '1';
    k2.style.opacity = '0';
    rope.style.width = 'calc(100% - 60px)';
    fb.innerHTML = '📏 <span style="color:#38bdf8;">Rope Stretched Straight!</span> No slack or bends, reaching 100 cm.';
  } else if (st === 3) {
    k1.style.opacity = '1';
    k2.style.opacity = '1';
    rope.style.width = 'calc(100% - 60px)';
    fb.innerHTML = '🎉 <span style="color:#34d399;">End Knot Tied at 100 cm!</span> Distance between knots is precisely 1 Metre!';
  }
}
setTimeout(() => sim9Step(1), 100);
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🧍 Wall Height 1-Metre Benchmark Sorter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Check(115)">Child A (115 cm)</button>
      <button class="sim-btn" onclick="sim10Check(92)">Child B (92 cm)</button>
      <button class="sim-btn" onclick="sim10Check(120)">Child C (120 cm)</button>
      <button class="sim-btn" onclick="sim10Check(100)">Child D (100 cm)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:550px; height:120px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); display:flex; align-items:flex-end; padding:0 30px; margin-bottom:12px;">
      <!-- 1 Metre Wall Chalk Line -->
      <div style="position:absolute; left:0; right:0; bottom:80px; height:2px; background:#fbbf24; border-top:2px dashed #f59e0b; z-index:2;">
        <span style="position:absolute; right:10px; top:-16px; font-size:10px; font-weight:bold; color:#fbbf24;">1-Metre Wall Line (100 cm)</span>
      </div>

      <!-- Child Height Figure -->
      <div id="sim10Figure" style="position:relative; width:45px; background:linear-gradient(180deg, #38bdf8, #1e40af); border-radius:8px 8px 0 0; margin-left:80px; transition:height 0.4s ease; display:flex; flex-direction:column; align-items:center; justify-content:flex-start; padding-top:4px; z-index:1;">
        <span style="font-size:16px;">🧒</span>
      </div>
      <div id="sim10HeightBadge" style="margin-left:14px; margin-bottom:20px; font-size:14px; font-weight:bold; color:#fff;">
        Height: 115 cm
      </div>
    </div>
    <div id="sim10Verdict" style="font-size:15px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 20px; text-align:center;">
      Category: TALLER than 1 Metre (+15 cm above line)
    </div>
  </div>
</div>
<script>
function sim10Check(cm) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('' + cm));
  });

  const fig = document.getElementById('sim10Figure');
  const badge = document.getElementById('sim10HeightBadge');
  const verdict = document.getElementById('sim10Verdict');

  // 100 cm is mapped to 80px
  const hPx = Math.round((cm / 100) * 80);
  fig.style.height = hPx + 'px';
  badge.innerText = 'Height: ' + cm + ' cm';

  if (cm > 100) {
    verdict.style.color = '#34d399';
    verdict.style.background = 'rgba(16,185,129,0.15)';
    verdict.style.borderColor = '#10b981';
    verdict.innerHTML = '✨ Category: <span style="color:#34d399;">MORE than 1 Metre</span> (' + (cm - 100) + ' cm taller than line)';
  } else if (cm < 100) {
    verdict.style.color = '#fbbf24';
    verdict.style.background = 'rgba(245,158,11,0.15)';
    verdict.style.borderColor = '#f59e0b';
    verdict.innerHTML = '📏 Category: <span style="color:#fbbf24;">LESS than 1 Metre</span> (' + (100 - cm) + ' cm below line)';
  } else {
    verdict.style.color = '#38bdf8';
    verdict.style.background = 'rgba(56,189,248,0.15)';
    verdict.style.borderColor = '#38bdf8';
    verdict.innerHTML = '🎯 Category: <span style="color:#38bdf8;">EXACTLY 1 Metre</span> (Right on the line!)';
  }
}
setTimeout(() => sim10Check(115), 100);
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">📦 Real-World Metre Benchmark Classifier</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Pick(0)">Pencil</button>
      <button class="sim-btn" onclick="sim11Pick(1)">School Bus</button>
      <button class="sim-btn" onclick="sim11Pick(2)">Study Desk</button>
      <button class="sim-btn" onclick="sim11Pick(3)">Door Height</button>
      <button class="sim-btn" onclick="sim11Pick(4)">Guitar</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim11Prompt" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 20px; text-align:center;">
      Object: ✏️ Wooden Writing Pencil (approx 18 cm)
    </div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; width:100%; max-width:600px; margin-bottom:12px;">
      <button class="sim-btn" id="sim11Bin0" onclick="sim11Guess(0)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#60a5fa;">&lt; 1 Metre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Shorter than 100 cm</div>
      </button>
      <button class="sim-btn" id="sim11Bin1" onclick="sim11Guess(1)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#34d399;">≈ 1 Metre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Close to 100 cm</div>
      </button>
      <button class="sim-btn" id="sim11Bin2" onclick="sim11Guess(2)" style="padding:12px 8px; text-align:center;">
        <div style="font-size:16px; font-weight:bold; color:#f59e0b;">&gt; 1 Metre</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px;">Longer than 100 cm</div>
      </button>
    </div>
    <div id="sim11Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; text-align:center;">
      Click a size benchmark bin above to classify this object!
    </div>
  </div>
</div>
<script>
let sim11Cur = 0;
const sim11Items = [
  { name: '✏️ Wooden Writing Pencil', size: '~18 cm', bin: 0, reason: 'A pencil fits inside a pouch, measuring far less than 1 metre (100 cm)!' },
  { name: '🚌 Passenger School Bus', size: '~8 metres', bin: 2, reason: 'A large school bus carries dozens of children, measuring many metres long!' },
  { name: '🪑 School Study Desk', size: '~75-100 cm', bin: 1, reason: 'A desk reaches roughly waist level on an adult, closely matching 1 metre!' },
  { name: '🚪 Classroom Door Height', size: '~200 cm', bin: 2, reason: 'A doorway is built for tall adults to walk through, measuring about 2 metres!' },
  { name: '🎸 Acoustic Music Guitar', size: '~100 cm', bin: 1, reason: 'A standard guitar is approximately 1 metre long from base to peghead!' }
];

function sim11Pick(idx) {
  sim11Cur = idx;
  document.querySelectorAll('#sim11 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  const it = sim11Items[idx];
  document.getElementById('sim11Prompt').innerText = 'Object: ' + it.name + ' (' + it.size + ')';
  document.getElementById('sim11Feedback').innerText = 'Click a size benchmark bin above to classify this object!';
  document.querySelectorAll('#sim11 [id^=sim11Bin]').forEach(b => {
    b.style.borderColor = '';
    b.style.background = '';
  });
}

function sim11Guess(binIdx) {
  const it = sim11Items[sim11Cur];
  const fb = document.getElementById('sim11Feedback');
  const btn = document.getElementById('sim11Bin' + binIdx);

  if (binIdx === it.bin) {
    btn.style.borderColor = '#10b981';
    btn.style.background = 'rgba(16,185,129,0.2)';
    fb.innerHTML = '🎉 <span style="color:#34d399;">Correct!</span> ' + it.reason;
  } else {
    btn.style.borderColor = '#ef4444';
    btn.style.background = 'rgba(239,68,68,0.2)';
    fb.innerHTML = '❌ <span style="color:#f87171;">Try again!</span> Consider whether ' + it.size + ' is smaller, roughly equal, or larger than 100 cm.';
  }
}
setTimeout(() => sim11Pick(0), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">✂️ Folding Half-Metre (50 cm) Explorer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Fold(false)">Unfolded (1 Metre = 100 cm)</button>
      <button class="sim-btn" onclick="sim12Fold(true)">Fold in Half (1/2 Metre)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:560px; height:70px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; align-items:center; justify-content:center; margin-bottom:12px;">
      <!-- Whole rope representation -->
      <div id="sim12RopeWrap" style="display:flex; width:80%; height:12px; background:#475569; border-radius:6px; overflow:hidden; transition:width 0.5s ease;">
        <div id="sim12Part1" style="flex:1; background:#3b82f6; border-right:2px dashed #fff;"></div>
        <div id="sim12Part2" style="flex:1; background:#10b981;"></div>
      </div>
    </div>
    <div id="sim12Labels" style="display:flex; justify-content:space-between; width:80%; max-width:450px; font-size:12px; font-weight:bold; margin-bottom:10px;">
      <span style="color:#60a5fa;">Left Half: 50 cm</span>
      <span style="color:#34d399;">Right Half: 50 cm</span>
    </div>
    <div id="sim12Equation" style="font-size:18px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Whole Metre: 100 cm (50 cm + 50 cm = 100 cm = 1 m)
    </div>
  </div>
</div>
<script>
function sim12Fold(folded) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(folded ? 'Fold in Half' : 'Unfolded'));
  });

  const wrap = document.getElementById('sim12RopeWrap');
  const eq = document.getElementById('sim12Equation');

  if (folded) {
    wrap.style.width = '40%';
    eq.innerHTML = 'Folded State: <span style="color:#38bdf8;">1/2 Metre = 50 cm</span> (Half of 100 cm)';
  } else {
    wrap.style.width = '80%';
    eq.innerHTML = 'Unfolded State: <span style="color:#fbbf24;">1 Whole Metre = 100 cm</span> (50 cm + 50 cm)';
  }
}
setTimeout(() => sim12Fold(false), 100);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">📐 Quarter-Metre (25 cm) Crease Partitioning</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Highlight(1)">1 Quarter (25 cm)</button>
      <button class="sim-btn" onclick="sim13Highlight(2)">2 Quarters (50 cm)</button>
      <button class="sim-btn" onclick="sim13Highlight(3)">3 Quarters (75 cm)</button>
      <button class="sim-btn" onclick="sim13Highlight(4)">4 Quarters (100 cm)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; width:100%; max-width:560px; height:50px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px; gap:4px; margin-bottom:12px;">
      <div id="sim13Seg1" style="flex:1; border-radius:6px; background:#3b82f6; display:flex; align-items:center; justify-content:center; color:#fff; font-size:12px; font-weight:bold;">25 cm (1/4)</div>
      <div id="sim13Seg2" style="flex:1; border-radius:6px; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:#94a3b8; font-size:12px; font-weight:bold;">25 cm (1/4)</div>
      <div id="sim13Seg3" style="flex:1; border-radius:6px; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:#94a3b8; font-size:12px; font-weight:bold;">25 cm (1/4)</div>
      <div id="sim13Seg4" style="flex:1; border-radius:6px; background:rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; color:#94a3b8; font-size:12px; font-weight:bold;">25 cm (1/4)</div>
    </div>
    <div id="sim13Readout" style="font-size:18px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 24px; text-align:center;">
      Active Length: 1/4 Metre = 25 cm
    </div>
  </div>
</div>
<script>
function sim13Highlight(quarters) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + quarters));
  });

  const cm = quarters * 25;
  const labels = ['1/4 Metre', '2/4 = 1/2 Metre', '3/4 Metre', '4/4 = 1 Whole Metre'];

  for (let i = 1; i <= 4; i++) {
    const el = document.getElementById('sim13Seg' + i);
    if (i <= quarters) {
      el.style.background = '#3b82f6';
      el.style.color = '#fff';
    } else {
      el.style.background = 'rgba(255,255,255,0.1)';
      el.style.color = '#94a3b8';
    }
  }

  document.getElementById('sim13Readout').innerHTML = 'Selected: <span style="color:#fbbf24;">' + labels[quarters - 1] + ' = ' + cm + ' cm</span>';
}
setTimeout(() => sim13Highlight(1), 100);
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">📋 Fractional Metre Object Survey Checklist</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Test('pencilBox')">Pencil Box (25 cm)</button>
      <button class="sim-btn" onclick="sim14Test('schoolBag')">School Bag (50 cm)</button>
      <button class="sim-btn" onclick="sim14Test('windowPane')">Window Pane (75 cm)</button>
      <button class="sim-btn" onclick="sim14Test('readingDesk')">Reading Desk (100 cm)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="width:100%; max-width:600px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); overflow:hidden; margin-bottom:12px;">
      <table style="width:100%; border-collapse:collapse; font-size:12px; text-align:center;">
        <thead style="background:rgba(255,255,255,0.08); color:#fbbf24; font-weight:bold;">
          <tr>
            <th style="padding:8px; border-bottom:1px solid rgba(255,255,255,0.1);">Item</th>
            <th style="padding:8px; border-bottom:1px solid rgba(255,255,255,0.1);">1/4 m (25 cm)</th>
            <th style="padding:8px; border-bottom:1px solid rgba(255,255,255,0.1);">1/2 m (50 cm)</th>
            <th style="padding:8px; border-bottom:1px solid rgba(255,255,255,0.1);">3/4 m (75 cm)</th>
            <th style="padding:8px; border-bottom:1px solid rgba(255,255,255,0.1);">1 m (100 cm)</th>
          </tr>
        </thead>
        <tbody style="color:#cbd5e1;" id="sim14TableBody">
          <!-- Populated by JS -->
        </tbody>
      </table>
    </div>
    <div id="sim14Note" style="font-size:14px; font-weight:bold; color:#34d399; text-align:center;">
      Testing classroom furniture with fractional rope knots!
    </div>
  </div>
</div>
<script>
const sim14Items = {
  pencilBox: { name: 'Pencil Box', cm: 25, match: '1/4 m', note: '✨ Pencil Box aligns cleanly with the 1/4 m (25 cm) mark!' },
  schoolBag: { name: 'School Bag Height', cm: 50, match: '1/2 m', note: '✨ School Bag aligns perfectly with the 1/2 m (50 cm) mark!' },
  windowPane: { name: 'Window Pane Width', cm: 75, match: '3/4 m', note: '✨ Window Pane matches the three-quarters mark: 3/4 m (75 cm)!' },
  readingDesk: { name: 'Reading Desk Width', cm: 100, match: '1 m', note: '✨ Reading Desk spans the complete length of 1 whole metre (100 cm)!' }
};

function sim14Test(key) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });

  const it = sim14Items[key];
  const body = document.getElementById('sim14TableBody');
  body.innerHTML = `
    <tr>
      <td style="padding:8px; font-weight:bold; color:#fff;">${it.name}</td>
      <td style="padding:8px;">${it.match === '1/4 m' ? '✅' : '—'}</td>
      <td style="padding:8px;">${it.match === '1/2 m' ? '✅' : '—'}</td>
      <td style="padding:8px;">${it.match === '3/4 m' ? '✅' : '—'}</td>
      <td style="padding:8px;">${it.match === '1 m' ? '✅' : '—'}</td>
    </tr>
  `;
  document.getElementById('sim14Note').innerText = it.note;
}
setTimeout(() => sim14Test('pencilBox'), 100);
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🏃 Playground Standing Broad Jump Tracker</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Jump(85)">Jump A (85 cm)</button>
      <button class="sim-btn" onclick="sim15Jump(135)">Jump B (135 cm)</button>
      <button class="sim-btn" onclick="sim15Jump(180)">Jump C (180 cm)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:580px; height:80px; background:#1e293b; border:2px solid #475569; border-radius:8px; display:flex; align-items:center; padding:0 30px; margin-bottom:12px;">
      <!-- Track milestones -->
      <div style="position:absolute; left:30px; top:4px; font-size:10px; color:#f87171; font-weight:bold;">Takeoff (0m)</div>
      <div style="position:absolute; left:35%; top:4px; font-size:10px; color:#94a3b8;">1.0 m (100 cm)</div>
      <div style="position:absolute; left:60%; top:4px; font-size:10px; color:#94a3b8;">1.5 m (150 cm)</div>
      <div style="position:absolute; right:30px; top:4px; font-size:10px; color:#94a3b8;">2.0 m (200 cm)</div>

      <!-- Landing Jumper -->
      <div id="sim15Jumper" style="position:absolute; left:30px; transform:translateX(-50%); display:flex; flex-direction:column; align-items:center; transition:left 0.5s ease;">
        <span style="font-size:22px;">👟</span>
        <span id="sim15Badge" style="font-size:10px; font-weight:bold; color:#fbbf24; background:#0f172a; padding:1px 6px; border-radius:4px; border:1px solid #f59e0b;">85 cm</span>
      </div>
    </div>
    <div id="sim15Interval" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Landed at 85 cm: Less than 1 metre (&lt; 1.0 m)
    </div>
  </div>
</div>
<script>
function sim15Jump(cm) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('' + cm));
  });

  // Scale: 0 cm = 30px, 200 cm = calc(100% - 30px)
  const pct = (cm / 200) * 85 + 5;
  const jumper = document.getElementById('sim15Jumper');
  jumper.style.left = pct + '%';
  document.getElementById('sim15Badge').innerText = cm + ' cm';

  const fb = document.getElementById('sim15Interval');
  if (cm < 100) {
    fb.innerHTML = 'Landed at ' + cm + ' cm: <span style="color:#fbbf24;">Less than 1 metre (&lt; 1.0 m)</span>';
  } else if (cm <= 150) {
    fb.innerHTML = 'Landed at ' + cm + ' cm: <span style="color:#34d399;">Between 1.0 m and 1.5 m (Great jump!)</span>';
  } else {
    fb.innerHTML = 'Landed at ' + cm + ' cm: <span style="color:#38bdf8;">Between 1.5 m and 2.0 m (Super leap!)</span>';
  }
}
setTimeout(() => sim15Jump(85), 100);
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">✂️ Rope Cuts & Walking Paces Calculator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16SetMode('cuts')">Rope Cuts Logic</button>
      <button class="sim-btn" onclick="sim16SetMode('paces')">Footstep Paces</button>
      <button class="sim-btn" onclick="sim16SetMode('perimeter')">Room Perimeter</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim16Card" style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <!-- Dynamic interactive content -->
    </div>
    <div id="sim16Summary" style="font-size:15px; font-weight:bold; color:#a7f3d0; text-align:center;">
      Rule: n pieces require n - 1 scissor cuts!
    </div>
  </div>
</div>
<script>
function sim16SetMode(mode) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });

  const card = document.getElementById('sim16Card');
  const sum = document.getElementById('sim16Summary');

  if (mode === 'cuts') {
    card.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">How many cuts to make 4 equal pieces of rope?</div>
      <div style="font-size:28px; font-weight:bold; color:#38bdf8; margin:8px 0;">3 Cuts</div>
      <div style="font-size:12px; color:#cbd5e1;">Cut 1 makes 2 pieces. Cut 2 makes 3 pieces. Cut 3 makes 4 pieces!</div>
    `;
    sum.innerText = 'Mathematical Principle: Cuts = Pieces - 1 (4 - 1 = 3 cuts)';
  } else if (mode === 'paces') {
    card.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">Pacing a 6-metre hallway (50 cm per footstep):</div>
      <div style="font-size:28px; font-weight:bold; color:#34d399; margin:8px 0;">12 Footsteps</div>
      <div style="font-size:12px; color:#cbd5e1;">Each metre = 2 footsteps (50 cm + 50 cm). 6 metres × 2 footsteps = 12 footsteps!</div>
    `;
    sum.innerText = 'Pacing Formula: Hallway Metres × 2 = Total Footsteps';
  } else {
    card.innerHTML = `
      <div style="font-size:15px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">Classroom Room Perimeter (8m long × 6m wide):</div>
      <div style="font-size:28px; font-weight:bold; color:#f59e0b; margin:8px 0;">28 Metres</div>
      <div style="font-size:12px; color:#cbd5e1;">Perimeter = 8 m + 8 m + 6 m + 6 m = 16 m + 12 m = 28 m total!</div>
    `;
    sum.innerText = 'Perimeter Formula: 2 × (Length + Width) = 2 × (8 + 6) = 28 m';
  }
}
setTimeout(() => sim16SetMode('cuts'), 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Slides 9-16.")
    for k in sorted(sims_part2.keys()):
        print(f"  Slide {k}: {len(sims_part2[k])} chars")

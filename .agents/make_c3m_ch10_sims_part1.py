#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party!
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🎉 Classroom Party Decoration Length Comparator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Inspect('door')">Door Height</button>
      <button class="sim-btn" onclick="sim1Inspect('window')">Window Width</button>
      <button class="sim-btn" onclick="sim1Inspect('table')">Activity Desk</button>
      <button class="sim-btn" onclick="sim1Inspect('bunting')">Wall Bunting</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; margin-bottom:12px;">
      <div id="sim1TargetTitle" style="font-size:16px; font-weight:bold; color:#fbbf24; margin-bottom:6px;">Target: Classroom Entrance Door</div>
      <div id="sim1Desc" style="font-size:13px; color:#cbd5e1; margin-bottom:10px;">
        Comparing vertical door height against informal paper strings and ribbon tools.
      </div>
      <div style="background:rgba(255,255,255,0.05); border-radius:8px; height:24px; width:100%; position:relative; overflow:hidden;">
        <div id="sim1Bar" style="height:100%; width:85%; background:linear-gradient(90deg, #3b82f6, #38bdf8); border-radius:8px; transition:width 0.4s ease;"></div>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8; margin-top:4px;">
        <span>0 cm</span>
        <span id="sim1MeasureVal" style="color:#38bdf8; font-weight:bold; font-size:13px;">200 cm (Very Tall)</span>
        <span>250 cm</span>
      </div>
    </div>
    <div id="sim1Verdict" style="font-size:15px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 18px; text-align:center;">
      ✨ The doorway is significantly taller than all furniture, requiring 2 long paper strings!
    </div>
  </div>
</div>
<script>
const sim1Items = {
  door: { title: 'Classroom Entrance Door', desc: 'Door height requires 2 long paper strings joined end-to-end.', widthPct: '85%', val: '200 cm (Tallest)', verdict: '✨ The doorway is significantly taller than all furniture, requiring 2 long paper strings!' },
  window: { title: 'Classroom Window Frame', desc: 'Window width matches approximately 1 long paper ribbon.', widthPct: '50%', val: '120 cm (Medium)', verdict: '✨ The window width matches roughly 1 long streamer ribbon across the glass pane!' },
  table: { title: 'Student Activity Desk', desc: 'Desk height is roughly waist level, measured with a short string.', widthPct: '32%', val: '75 cm (Waist Level)', verdict: '✨ Desk height is convenient for sitting and matches waist-level string cords!' },
  bunting: { title: 'Wall-to-Wall Party Bunting', desc: 'Stretched between opposite classroom walls across the room.', widthPct: '98%', val: '600 cm (Longest)', verdict: '✨ Wall-to-wall party bunting spans the entire room, requiring multiple footsteps to pace!' }
};

function sim1Inspect(key) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });
  const it = sim1Items[key];
  document.getElementById('sim1TargetTitle').innerText = 'Target: ' + it.title;
  document.getElementById('sim1Desc').innerText = it.desc;
  document.getElementById('sim1Bar').style.width = it.widthPct;
  document.getElementById('sim1MeasureVal').innerText = it.val;
  document.getElementById('sim1Verdict').innerText = it.verdict;
}
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">✋ Handspan Size Variation Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2SetHand('large')">Large Handspan (15 cm)</button>
      <button class="sim-btn" onclick="sim2SetHand('small')">Small Handspan (10 cm)</button>
      <button class="sim-btn" onclick="sim2Animate()">Walk Spans Across Table</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#cbd5e1; font-weight:bold; margin-bottom:8px;">
      Measuring a fixed 90 cm Study Tabletop:
    </div>
    <div id="sim2Table" style="position:relative; width:100%; max-width:600px; height:70px; background:#451a03; border:3px solid #78350f; border-radius:10px; display:flex; align-items:center; padding:0 8px; margin-bottom:12px; overflow:hidden;">
      <div id="sim2SpansContainer" style="display:flex; width:100%; height:100%; align-items:center;">
        <!-- Injected span hands -->
      </div>
    </div>
    <div id="sim2Feedback" style="font-size:16px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Count: 6 Large Handspans (6 × 15 cm = 90 cm)
    </div>
  </div>
</div>
<script>
let sim2Mode = 'large';
function sim2SetHand(mode) {
  sim2Mode = mode;
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.toLowerCase().includes(mode));
  });
  sim2Render();
}

function sim2Render() {
  const container = document.getElementById('sim2SpansContainer');
  container.innerHTML = '';
  const count = sim2Mode === 'large' ? 6 : 9;
  const spanSize = sim2Mode === 'large' ? 15 : 10;

  for (let i = 0; i < count; i++) {
    const hand = document.createElement('div');
    hand.style.flex = '1';
    hand.style.height = '80%';
    hand.style.margin = '2px';
    hand.style.background = sim2Mode === 'large' ? 'rgba(59,130,246,0.3)' : 'rgba(245,158,11,0.3)';
    hand.style.border = '1px dashed ' + (sim2Mode === 'large' ? '#60a5fa' : '#fbbf24');
    hand.style.borderRadius = '6px';
    hand.style.display = 'flex';
    hand.style.alignItems = 'center';
    hand.style.justifyContent = 'center';
    hand.style.fontSize = '18px';
    hand.innerHTML = '✋<span style="font-size:10px; color:#fff; font-weight:bold; margin-left:2px;">#' + (i + 1) + '</span>';
    container.appendChild(hand);
  }

  document.getElementById('sim2Feedback').innerHTML = sim2Mode === 'large' 
    ? 'Count: <span style="color:#60a5fa;">6 Large Handspans</span> (6 × 15 cm = 90 cm table)'
    : 'Count: <span style="color:#fbbf24;">9 Small Handspans</span> (9 × 10 cm = 90 cm table)';
}

function sim2Animate() {
  const hands = document.querySelectorAll('#sim2SpansContainer > div');
  hands.forEach((h, i) => {
    h.style.opacity = '0';
    setTimeout(() => {
      h.style.transition = 'opacity 0.3s ease';
      h.style.opacity = '1';
    }, i * 150);
  });
}
setTimeout(() => sim2SetHand('large'), 100);
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🖼️ Display Board Border Ribbon Perimeter Calculator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3SetBoard(6, 4)">Medium Board (6 × 4)</button>
      <button class="sim-btn" onclick="sim3SetBoard(8, 5)">Large Board (8 × 5)</button>
      <button class="sim-btn" onclick="sim3SetBoard(5, 3)">Small Board (5 × 3)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:280px; height:140px; background:#064e3b; border:8px solid #b45309; border-radius:8px; display:flex; flex-direction:column; justify-content:space-between; padding:4px; margin-bottom:12px;">
      <!-- Top edge strings -->
      <div id="sim3Top" style="display:flex; justify-content:space-around; color:#fbbf24; font-size:11px; font-weight:bold; border-bottom:2px dashed #f59e0b; padding-bottom:2px;">
        Top: 6 Strings
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; height:100%;">
        <div id="sim3Left" style="color:#34d399; font-size:11px; font-weight:bold; transform:rotate(-90deg);">4 Strings</div>
        <div style="font-size:14px; font-weight:bold; color:#a7f3d0; text-align:center;">Class Display Board</div>
        <div id="sim3Right" style="color:#34d399; font-size:11px; font-weight:bold; transform:rotate(90deg);">4 Strings</div>
      </div>
      <!-- Bottom edge strings -->
      <div id="sim3Bottom" style="display:flex; justify-content:space-around; color:#fbbf24; font-size:11px; font-weight:bold; border-top:2px dashed #f59e0b; padding-top:2px;">
        Bottom: 6 Strings
      </div>
    </div>
    <div id="sim3Equation" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Perimeter = 6 + 6 + 4 + 4 = 20 Paper Ribbons
    </div>
  </div>
</div>
<script>
function sim3SetBoard(h, v) {
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(h + ' × ' + v));
  });
  document.getElementById('sim3Top').innerText = 'Top: ' + h + ' Strings';
  document.getElementById('sim3Bottom').innerText = 'Bottom: ' + h + ' Strings';
  document.getElementById('sim3Left').innerText = v + ' Strings';
  document.getElementById('sim3Right').innerText = v + ' Strings';

  const total = h + h + v + v;
  document.getElementById('sim3Equation').innerHTML = 'Total Border Perimeter: <span style="color:#fbbf24;">' + h + ' + ' + h + ' + ' + v + ' + ' + v + ' = ' + total + ' Strings</span>';
}
setTimeout(() => sim3SetBoard(6, 4), 100);
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">🎭 Bilateral Moustache Symmetry Canvas</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4SetLength(8)">8 cm Curl</button>
      <button class="sim-btn" onclick="sim4SetLength(12)">12 cm Curl</button>
      <button class="sim-btn" onclick="sim4SetLength(15)">15 cm Grand Curl</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <svg width="340" height="120" viewBox="0 0 340 120" style="background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); margin-bottom:12px;">
      <!-- Central line of symmetry -->
      <line x1="170" y1="10" x2="170" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4" />
      <text x="175" y="24" fill="#fbbf24" font-size="10" font-weight="bold">Line of Symmetry</text>
      <!-- Nose indicator -->
      <circle cx="170" cy="50" r="10" fill="#f87171" opacity="0.8" />
      <!-- Left moustache curl -->
      <path id="sim4LeftPath" d="M 170 60 Q 120 75 90 40" fill="none" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" />
      <!-- Right moustache curl (symmetrical) -->
      <path id="sim4RightPath" d="M 170 60 Q 220 75 250 40" fill="none" stroke="#34d399" stroke-width="6" stroke-linecap="round" />
    </svg>
    <div id="sim4Status" style="font-size:15px; font-weight:bold; color:#a7f3d0; text-align:center;">
      Left Curl = 8 cm | Right Curl = 8 cm (Perfect Balance)
    </div>
  </div>
</div>
<script>
function sim4SetLength(cm) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('' + cm));
  });

  const span = cm * 10;
  const leftX = 170 - span;
  const rightX = 170 + span;

  document.getElementById('sim4LeftPath').setAttribute('d', `M 170 60 Q ${170 - span/2} ${60 + cm} ${leftX} ${60 - cm/2}`);
  document.getElementById('sim4RightPath').setAttribute('d', `M 170 60 Q ${170 + span/2} ${60 + cm} ${rightX} ${60 - cm/2}`);

  document.getElementById('sim4Status').innerHTML = `Left Curl = <span style="color:#38bdf8;">${cm} cm</span> | Right Curl = <span style="color:#34d399;">${cm} cm</span> (Identical Bilateral Length!)`;
}
setTimeout(() => sim4SetLength(8), 100);
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🚪 Doorway Spatial Clearance Navigator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5SetOrientation('flat')">Try Flat (120 cm length)</button>
      <button class="sim-btn" onclick="sim5SetOrientation('sideways')">Turn Sideways (65 cm width)</button>
      <button class="sim-btn" onclick="sim5Push()">Push Through Door (80 cm opening)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:550px; height:90px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center; overflow:hidden; margin-bottom:12px;">
      <!-- Door posts -->
      <div style="position:absolute; top:0; bottom:0; left:300px; width:12px; background:#ef4444; border-radius:2px;"></div>
      <div style="position:absolute; top:0; bottom:0; left:420px; width:12px; background:#ef4444; border-radius:2px;"></div>
      <div style="position:absolute; top:4px; left:330px; font-size:10px; font-weight:bold; color:#fca5a5;">Door Opening (80 cm)</div>

      <!-- Animated Table -->
      <div id="sim5Table" style="position:absolute; left:60px; height:50px; width:120px; background:#b45309; border:2px solid #f59e0b; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#fff; transition:all 0.5s ease;">
        Table (120 cm)
      </div>
    </div>
    <div id="sim5Feedback" style="font-size:15px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Table is flat (120 cm wide). Door is 80 cm wide. Click 'Push Through'!
    </div>
  </div>
</div>
<script>
let sim5Mode = 'flat';
function sim5SetOrientation(mode) {
  sim5Mode = mode;
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.toLowerCase().includes(mode));
  });

  const tbl = document.getElementById('sim5Table');
  tbl.style.left = '60px';
  if (mode === 'flat') {
    tbl.style.width = '120px';
    tbl.style.height = '46px';
    tbl.innerText = 'Table (120 cm)';
    document.getElementById('sim5Feedback').innerText = 'Table is flat (120 cm wide). Door is 80 cm wide. Click \'Push Through\'!';
  } else {
    tbl.style.width = '65px';
    tbl.style.height = '46px';
    tbl.innerText = 'Table (65 cm)';
    document.getElementById('sim5Feedback').innerText = 'Table turned sideways! Width is now 65 cm (less than 80 cm door). Ready to push!';
  }
}

function sim5Push() {
  const tbl = document.getElementById('sim5Table');
  const fb = document.getElementById('sim5Feedback');

  if (sim5Mode === 'flat') {
    tbl.style.left = '180px';
    setTimeout(() => {
      fb.innerHTML = '💥 <span style="color:#f87171;">STUCK! 120 cm is wider than the 80 cm door. Rotate sideways!</span>';
    }, 400);
  } else {
    tbl.style.left = '450px';
    setTimeout(() => {
      fb.innerHTML = '🎉 <span style="color:#34d399;">PASSED EASILY! 65 cm &lt; 80 cm doorway clearance!</span>';
    }, 400);
  }
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🌉 Toy Bridge Vertical Clearance Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Test(4, 'Sports Car')">Car (4 cm)</button>
      <button class="sim-btn" onclick="sim6Test(11, 'Delivery Van')">Van (11 cm)</button>
      <button class="sim-btn" onclick="sim6Test(16, 'Double-Decker')">Bus (16 cm)</button>
      <button class="sim-btn" onclick="sim6Test(22, 'Tall Giraffe')">Giraffe (22 cm)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="position:relative; width:100%; max-width:550px; height:110px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); display:flex; align-items:flex-end; padding:0 20px; margin-bottom:12px; overflow:hidden;">
      <!-- Bridge Span -->
      <div style="position:absolute; left:220px; bottom:65px; width:120px; height:16px; background:#475569; border:2px solid #94a3b8; border-radius:4px; z-index:2;">
        <span style="font-size:9px; color:#cbd5e1; font-weight:bold; display:block; text-align:center;">Clearance 14 cm</span>
      </div>
      <!-- Bridge Pillars -->
      <div style="position:absolute; left:220px; bottom:0; width:14px; height:65px; background:#334155; z-index:2;"></div>
      <div style="position:absolute; left:326px; bottom:0; width:14px; height:65px; background:#334155; z-index:2;"></div>

      <!-- Toy Vehicle -->
      <div id="sim6Vehicle" style="position:absolute; left:30px; bottom:0; background:#3b82f6; border:2px solid #60a5fa; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:bold; color:#fff; transition:left 0.6s ease; z-index:1;">
        Car (4 cm)
      </div>
    </div>
    <div id="sim6Verdict" style="font-size:15px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 20px; text-align:center;">
      ✨ Safe Clearance! 4 cm vehicle is less than 14 cm bridge height.
    </div>
  </div>
</div>
<script>
function sim6Test(h, name) {
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(name));
  });

  const veh = document.getElementById('sim6Vehicle');
  const fb = document.getElementById('sim6Verdict');
  veh.style.left = '30px';
  veh.style.height = (h * 4) + 'px';
  veh.style.width = '60px';
  veh.innerText = name;

  setTimeout(() => {
    if (h <= 14) {
      veh.style.left = '420px';
      fb.style.color = '#34d399';
      fb.style.background = 'rgba(16,185,129,0.15)';
      fb.style.borderColor = '#10b981';
      fb.innerHTML = '✨ <span style="color:#34d399;">Safe Passage!</span> ' + name + ' (' + h + ' cm) fits under the 14 cm clearance!';
    } else {
      veh.style.left = '165px';
      fb.style.color = '#f87171';
      fb.style.background = 'rgba(239,68,68,0.15)';
      fb.style.borderColor = '#ef4444';
      fb.innerHTML = '💥 <span style="color:#f87171;">CRASH!</span> ' + name + ' (' + h + ' cm) exceeds the 14 cm clearance limit!';
    }
  }, 200);
}
setTimeout(() => sim6Test(4, 'Sports Car'), 100);
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🧍 Body Proportion Truth Verifier</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Inspect('forearm')">Forearm = Foot</button>
      <button class="sim-btn" onclick="sim7Inspect('armspan')">Arm Span = Height</button>
      <button class="sim-btn" onclick="sim7Inspect('head')">Head = 3 Handspans</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim7Graphic" style="font-size:36px; margin-bottom:6px;">💪 🦶</div>
      <div id="sim7Title" style="font-size:18px; font-weight:bold; color:#fbbf24; margin-bottom:6px;">Rule: Forearm Length = Foot Length</div>
      <div id="sim7Explanation" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        Place the sole of your shoe along your inner forearm from elbow crease to wrist. They match almost identically!
      </div>
    </div>
    <div id="sim7Note" style="font-size:12px; color:#94a3b8; font-style:italic;">
      Ancient craftspeople used body parts as portable proportional rulers for clothing and architecture!
    </div>
  </div>
</div>
<script>
const sim7Data = {
  forearm: {
    icon: '💪 🦶',
    title: 'Rule: Forearm Length ≈ Foot Length',
    desc: 'Place the sole of your shoe along the inside of your forearm from elbow crease to wrist. They match with incredible consistency across almost all humans!'
  },
  armspan: {
    icon: '👐 🧍',
    title: 'Rule: Outstretched Arm Span ≈ Standing Height',
    desc: 'Stretch both arms wide to the sides. The horizontal span from fingertip to fingertip is roughly equal to your total standing height from floor to head crown!'
  },
  head: {
    icon: '👑 ✋✋✋',
    title: 'Rule: Head Circumference ≈ 3 Handspans',
    desc: 'Wrap a paper strip around your forehead. Laying your handspan along that strip demonstrates that your head circumference is approximately 3 handspans around!'
  }
};

function sim7Inspect(key) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });
  const d = sim7Data[key];
  document.getElementById('sim7Graphic').innerText = d.icon;
  document.getElementById('sim7Title').innerText = d.title;
  document.getElementById('sim7Explanation').innerText = d.desc;
}
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">📏 Evolution of Measurement: Informal to Standard Metre</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Step(1)">1. Body Units</button>
      <button class="sim-btn" onclick="sim8Step(2)">2. Sticks & Paper</button>
      <button class="sim-btn" onclick="sim8Step(3)">3. Universal Metre Rod</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim8Icon" style="font-size:36px; margin-bottom:6px;">✋ 🦶</div>
      <div id="sim8StageTitle" style="font-size:18px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">Stage 1: Informal Body Spans</div>
      <div id="sim8Problem" style="font-size:12px; font-weight:bold; color:#f87171; margin-bottom:8px;">Problem: Varied from person to person, creating trade disputes!</div>
      <div id="sim8Desc" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        Early humans measured cloth using arm-lengths (cubits) and paces. Different arm lengths meant unfair transactions.
      </div>
    </div>
    <div id="sim8Benefit" style="font-size:14px; font-weight:bold; color:#38bdf8;">
      The journey toward 1 metre = 100 centimetres brought fairness and precision to the world!
    </div>
  </div>
</div>
<script>
const sim8Stages = {
  1: { icon: '✋ 🦶', title: 'Stage 1: Informal Body Spans', prob: 'Problem: Different arm sizes caused constant disputes in trade!', desc: 'Measuring with fingers, handspans, and arm-lengths meant customers with shorter merchants received less cloth.' },
  2: { icon: '🪵 📜', title: 'Stage 2: Agreed Sticks & Strips', prob: 'Improvement: Local agreement within a single village or market.', desc: 'Communities cut uniform wooden sticks and marked cords to use locally in village markets.' },
  3: { icon: '📏 🌍', title: 'Stage 3: Universal Standard Metre (100 cm)', prob: 'Solution: Exactly identical length worldwide!', desc: 'International science established the metre (m = 100 cm). Sturdy metal rods ensure identical, trusted measurements everywhere.' }
};

function sim8Step(step) {
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.startsWith('' + step));
  });
  const st = sim8Stages[step];
  document.getElementById('sim8Icon').innerText = st.icon;
  document.getElementById('sim8StageTitle').innerText = st.title;
  document.getElementById('sim8Problem').innerText = st.prob;
  document.getElementById('sim8Problem').style.color = step === 3 ? '#34d399' : '#f87171';
  document.getElementById('sim8Desc').innerText = st.desc;
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Slides 1-8.")
    for k in sorted(sims_part1.keys()):
        print(f"  Slide {k}: {len(sims_part1[k])} chars")

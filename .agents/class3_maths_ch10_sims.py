#!/usr/bin/env python3
"""NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party! Simulators"""

simulators = {
    1: '''
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
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
    document.getElementById('sim5Feedback').innerText = 'Table is flat (120 cm wide). Door is 80 cm wide. Click 'Push Through'!';
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}

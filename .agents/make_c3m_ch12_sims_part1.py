#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 12: Give and Take
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🐛 Animal Track Jump Navigator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1SetRule(2)">+2 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(5)">+5 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(-5)">-5 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(6)">+6 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(-6)">-6 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(9)">+9 Jump</button>
      <button class="sim-btn" onclick="sim1SetRule(-9)">-9 Jump</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim1Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div style="font-size:13px; color:#cbd5e1; margin-bottom:10px;">
      Follow the caterpillar segment trail from start to finish!
    </div>
    <!-- Track segments display -->
    <div id="sim1Track" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px; max-width:620px; padding:12px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Injected track circles -->
    </div>
    <div id="sim1Feedback" style="margin-top:12px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Rule: Add 2. Click Next Jump to leap forward!
    </div>
    <div style="margin-top:10px;">
      <button class="sim-btn" style="background:#10b981; font-weight:bold; font-size:14px; padding:6px 24px;" onclick="sim1NextStep()">Leap to Next Segment 🐾</button>
    </div>
  </div>
</div>
<script>
let sim1CurrentVal = 20;
let sim1Step = 2;
let sim1History = [20];

function sim1Init() {
  const track = document.getElementById('sim1Track');
  track.innerHTML = '';
  sim1History.forEach((v, idx) => {
    const isCurrent = idx === sim1History.length - 1;
    const bg = isCurrent ? '#10b981' : '#334155';
    const border = isCurrent ? '#34d399' : '#64748b';
    track.innerHTML += '<div style=\"width:44px; height:44px; border-radius:50%; background:' + bg + '; border:2px solid ' + border + '; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px; box-shadow:0 2px 6px rgba(0,0,0,0.3);\">' + v + '</div>';
  });
}

function sim1SetRule(step) {
  sim1Step = step;
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.remove('active');
    if (b.innerText.includes((step > 0 ? '+' : '') + step)) b.classList.add('active');
  });
  sim1Reset();
  document.getElementById('sim1Feedback').innerHTML = 'Rule selected: <b>' + (step > 0 ? 'Add ' + step : 'Subtract ' + Math.abs(step)) + '</b>. Current number: ' + sim1CurrentVal;
}

function sim1Reset() {
  sim1CurrentVal = (sim1Step < 0) ? 60 : 20;
  sim1History = [sim1CurrentVal];
  sim1Init();
  document.getElementById('sim1Feedback').innerHTML = 'Track reset to <b>' + sim1CurrentVal + '</b>. Ready to jump!';
}

function sim1NextStep() {
  if (sim1History.length >= 8) {
    document.getElementById('sim1Feedback').innerHTML = '🎉 Track completed 8 leaps! Hit Reset or choose another jump rule.';
    return;
  }
  const nextVal = sim1CurrentVal + sim1Step;
  sim1History.push(nextVal);
  const oldVal = sim1CurrentVal;
  sim1CurrentVal = nextVal;
  sim1Init();
  const sign = sim1Step > 0 ? '+' : '-';
  document.getElementById('sim1Feedback').innerHTML = '🐾 Jumped: ' + oldVal + ' ' + sign + ' ' + Math.abs(sim1Step) + ' = <span style=\"color:#34d399; font-size:16px;\">' + nextVal + '</span>!';
}
sim1Init();
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">📦 Part-Part-Whole Addition Bar Model</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2SetData(364, 52)">364 + 52 (Saplings)</button>
      <button class="sim-btn" onclick="sim2SetData(248, 75)">248 + 75</button>
      <button class="sim-btn" onclick="sim2SetData(415, 130)">415 + 130</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:16px;">
    <!-- Whole Bar -->
    <div style="width:100%; max-width:540px; margin-bottom:12px;">
      <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:4px;">
        <span>WHOLE (TOTAL QUANTITY)</span>
        <span id="sim2WholeLabel" style="color:#38bdf8; font-size:15px;">? = 416</span>
      </div>
      <div style="height:44px; width:100%; background:linear-gradient(90deg, #0284c7, #38bdf8); border-radius:8px; border:2px solid #7dd3fc; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:16px; box-shadow:0 4px 10px rgba(0,0,0,0.3);">
        <span id="sim2WholeText">Total = 416</span>
      </div>
    </div>
    <!-- Parts Split Bar -->
    <div style="width:100%; max-width:540px; margin-bottom:16px;">
      <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:4px;">
        <span>PART 1 (EXISTING)</span>
        <span>PART 2 (INCOMING)</span>
      </div>
      <div id="sim2BarParts" style="display:flex; height:44px; width:100%; gap:4px;">
        <div id="sim2Part1" style="width:85%; background:linear-gradient(90deg, #10b981, #34d399); border-radius:8px 0 0 8px; border:2px solid #6ee7b7; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">
          364
        </div>
        <div id="sim2Part2" style="width:15%; background:linear-gradient(90deg, #f59e0b, #fbbf24); border-radius:0 8px 8px 0; border:2px solid #fde68a; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">
          52
        </div>
      </div>
    </div>
    <!-- Dynamic Feedback Equation -->
    <div id="sim2Feedback" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 24px; text-align:center;">
      Part 1 (364) + Part 2 (52) = <span style="color:#34d399;">Whole (416)</span>
    </div>
  </div>
</div>
<script>
function sim2SetData(p1, p2) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.remove('active');
    if (b.innerText.includes(p1 + ' + ' + p2)) b.classList.add('active');
  });
  const whole = p1 + p2;
  const pct1 = Math.round((p1 / whole) * 100);
  const pct2 = 100 - pct1;
  document.getElementById('sim2Part1').style.width = pct1 + '%';
  document.getElementById('sim2Part1').innerText = p1;
  document.getElementById('sim2Part2').style.width = pct2 + '%';
  document.getElementById('sim2Part2').innerText = p2;
  document.getElementById('sim2WholeLabel').innerText = 'Whole = ' + whole;
  document.getElementById('sim2WholeText').innerText = 'Total = ' + whole;
  document.getElementById('sim2Feedback').innerHTML = 'Part 1 (' + p1 + ') + Part 2 (' + p2 + ') = <span style=\"color:#34d399;\">Whole (' + whole + ')</span>';
}
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🏛️ Place Value Column Addition Regrouper</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Reset()">Start: 364 + 52</button>
      <button class="sim-btn" id="sim3NextBtn" onclick="sim3StepForward()">Next Step ⏩</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Column Place Value Table -->
    <div style="background:rgba(0,0,0,0.4); border-radius:12px; border:1px solid rgba(255,255,255,0.2); padding:12px 20px; width:100%; max-width:380px;">
      <!-- Header Row: H T O -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-weight:bold; border-bottom:2px solid rgba(255,255,255,0.2); padding-bottom:6px; margin-bottom:8px;">
        <span style="color:#cbd5e1;">Op</span>
        <span style="color:#f87171;">H (100)</span>
        <span style="color:#fbbf24;">T (10)</span>
        <span style="color:#34d399;">O (1)</span>
      </div>
      <!-- Carry Row -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:12px; height:20px; color:#cbd5e1;">
        <span>Carry:</span>
        <span id="sim3CarryH" style="color:#f87171; font-weight:bold;"></span>
        <span id="sim3CarryT" style="color:#fbbf24; font-weight:bold;"></span>
        <span></span>
      </div>
      <!-- Number 1 Row: 3 6 4 -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:18px; font-weight:bold; color:#fff; padding:4px 0;">
        <span></span>
        <span style="color:#fca5a5;">3</span>
        <span style="color:#fde047;">6</span>
        <span style="color:#86efac;">4</span>
      </div>
      <!-- Number 2 Row: + 0 5 2 -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:18px; font-weight:bold; color:#fff; padding:4px 0; border-bottom:2px solid #38bdf8;">
        <span style="color:#38bdf8;">+</span>
        <span style="color:#64748b;">0</span>
        <span style="color:#fde047;">5</span>
        <span style="color:#86efac;">2</span>
      </div>
      <!-- Result Row -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:22px; font-weight:bold; padding-top:6px;">
        <span style="color:#38bdf8;">=</span>
        <span id="sim3ResH" style="color:#f87171;">-</span>
        <span id="sim3ResT" style="color:#fbbf24;">-</span>
        <span id="sim3ResO" style="color:#34d399;">-</span>
      </div>
    </div>
    <!-- Step explanation text -->
    <div id="sim3Feedback" style="margin-top:12px; font-size:14px; color:#e2e8f0; text-align:center; background:rgba(0,0,0,0.3); border-radius:8px; padding:6px 16px; border:1px solid rgba(255,255,255,0.15);">
      Step 0: Ready to calculate 364 + 52. Click "Next Step" to begin with Ones column!
    </div>
  </div>
</div>
<script>
let sim3CurrentStep = 0;

function sim3Reset() {
  sim3CurrentStep = 0;
  document.getElementById('sim3CarryH').innerText = '';
  document.getElementById('sim3CarryT').innerText = '';
  document.getElementById('sim3ResH').innerText = '-';
  document.getElementById('sim3ResT').innerText = '-';
  document.getElementById('sim3ResO').innerText = '-';
  document.getElementById('sim3Feedback').innerHTML = 'Step 0: Ready to add 364 + 52. Click "Next Step" to add Ones column.';
  document.getElementById('sim3NextBtn').disabled = false;
  document.getElementById('sim3NextBtn').innerText = 'Next Step ⏩';
}

function sim3StepForward() {
  sim3CurrentStep++;
  if (sim3CurrentStep === 1) {
    document.getElementById('sim3ResO').innerText = '6';
    document.getElementById('sim3Feedback').innerHTML = 'Step 1 (Ones): 4 + 2 = <b style=\"color:#34d399;\">6 Ones</b>. No regrouping needed.';
  } else if (sim3CurrentStep === 2) {
    document.getElementById('sim3ResT').innerText = '1';
    document.getElementById('sim3CarryH').innerText = '1';
    document.getElementById('sim3Feedback').innerHTML = 'Step 2 (Tens): 6 tens + 5 tens = 11 tens. Regroup 10 tens into <b style=\"color:#f87171;\">1 Hundred</b> carried over, leaving <b style=\"color:#fbbf24;\">1 Ten</b>!';
  } else if (sim3CurrentStep === 3) {
    document.getElementById('sim3ResH').innerText = '4';
    document.getElementById('sim3Feedback').innerHTML = 'Step 3 (Hundreds): 1 carried + 3 existing = <b style=\"color:#f87171;\">4 Hundreds</b>. Final sum is <b style=\"color:#38bdf8; font-size:17px;\">416</b>! 🎉';
    document.getElementById('sim3NextBtn').disabled = true;
    document.getElementById('sim3NextBtn').innerText = 'Completed! ✅';
  }
}
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">📏 Number Line Leap Explorer (364 + 52)</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim4JumpTens()">Jump +10 Tens (5 times)</button>
      <button class="sim-btn" onclick="sim4JumpOnes()">Jump +1 Ones (2 times)</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim4Reset()">Reset</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- SVG Number Line with Jump Arcs -->
    <svg id="sim4Svg" viewBox="0 0 600 120" style="width:100%; max-width:600px; height:120px; background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Base Axis -->
      <line x1="40" y1="90" x2="560" y2="90" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
      <!-- Axis Ticks & Labels -->
      <line x1="50" y1="85" x2="50" y2="95" stroke="#fff" stroke-width="2"/>
      <text x="50" y="110" fill="#cbd5e1" font-size="11" text-anchor="middle">364</text>
      
      <line x1="120" y1="85" x2="120" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="120" y="110" fill="#94a3b8" font-size="10" text-anchor="middle">374</text>
      
      <line x1="190" y1="85" x2="190" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="190" y="110" fill="#94a3b8" font-size="10" text-anchor="middle">384</text>
      
      <line x1="260" y1="85" x2="260" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="260" y="110" fill="#94a3b8" font-size="10" text-anchor="middle">394</text>
      
      <line x1="330" y1="85" x2="330" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="330" y="110" fill="#94a3b8" font-size="10" text-anchor="middle">404</text>
      
      <line x1="400" y1="85" x2="400" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="400" y="110" fill="#94a3b8" font-size="10" text-anchor="middle">414</text>
      
      <line x1="500" y1="85" x2="500" y2="95" stroke="#34d399" stroke-width="2"/>
      <text x="500" y="110" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">416</text>
      
      <!-- Interactive Arcs Group -->
      <g id="sim4Arcs"></g>
    </svg>
    <div id="sim4Feedback" style="margin-top:10px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Current Position: 364. Click "Jump +10 Tens" to take 5 strides of 10!
    </div>
  </div>
</div>
<script>
let sim4Stage = 0; // 0=start, 1=tens done (414), 2=ones done (416)

function sim4Reset() {
  sim4Stage = 0;
  document.getElementById('sim4Arcs').innerHTML = '';
  document.getElementById('sim4Feedback').innerHTML = 'Current Position: <b>364</b>. Ready to make jumps!';
}

function sim4JumpTens() {
  if (sim4Stage >= 1) return;
  sim4Stage = 1;
  const arcs = document.getElementById('sim4Arcs');
  let str = '';
  const xCoords = [50, 120, 190, 260, 330, 400];
  for (let i = 0; i < 5; i++) {
    const x1 = xCoords[i];
    const x2 = xCoords[i+1];
    const midX = (x1 + x2) / 2;
    str += '<path d=\"M ' + x1 + ' 85 Q ' + midX + ' 40 ' + x2 + ' 85\" stroke=\"#fbbf24\" stroke-width=\"2.5\" fill=\"none\"/>';
    str += '<text x=\"' + midX + '\" y=\"50\" fill=\"#fde047\" font-size=\"10\" font-weight=\"bold\" text-anchor=\"middle\">+10</text>';
  }
  arcs.innerHTML = str;
  document.getElementById('sim4Feedback').innerHTML = '5 Jumps of +10: 364 → 374 → 384 → 394 → 404 → <b style=\"color:#fbbf24;\">414</b>! Now click "Jump +1 Ones".';
}

function sim4JumpOnes() {
  if (sim4Stage === 0) {
    sim4JumpTens();
  }
  if (sim4Stage >= 2) return;
  sim4Stage = 2;
  const arcs = document.getElementById('sim4Arcs');
  // Two small jumps from 400 to 500
  arcs.innerHTML += '<path d=\"M 400 85 Q 450 65 500 85\" stroke=\"#34d399\" stroke-width=\"3\" fill=\"none\"/>';
  arcs.innerHTML += '<text x=\"450\" y=\"70\" fill=\"#34d399\" font-size=\"11\" font-weight=\"bold\" text-anchor=\"middle\">+2</text>';
  arcs.innerHTML += '<circle cx=\"500\" cy=\"85\" r=\"5\" fill=\"#34d399\"/>';
  document.getElementById('sim4Feedback').innerHTML = '🎉 Jump +2: 414 + 2 = <span style=\"color:#34d399; font-size:16px;\">416</span>! Total = 364 + 50 + 2 = 416.';
}
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">📦 Subtraction Part-Whole Order Packer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim5SetScenario(230, 75, 'Saplings')">230 - 75 = ?</button>
      <button class="sim-btn" onclick="sim5SetScenario(340, 125, 'Boxes')">340 - 125 = ?</button>
      <button class="sim-btn" onclick="sim5SetScenario(500, 180, 'Pencils')">500 - 180 = ?</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:16px;">
    <!-- Whole Bar Container -->
    <div style="width:100%; max-width:540px; margin-bottom:12px;">
      <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:4px;">
        <span>TOTAL ORDER REQUIRED</span>
        <span id="sim5WholeVal" style="color:#38bdf8; font-size:15px;">Whole = 230</span>
      </div>
      <div style="height:44px; width:100%; background:linear-gradient(90deg, #1e3a8a, #2563eb); border-radius:8px; border:2px solid #60a5fa; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:16px;">
        <span id="sim5WholeText">Total Order = 230</span>
      </div>
    </div>
    <!-- Subtraction Split Bar -->
    <div style="width:100%; max-width:540px; margin-bottom:16px;">
      <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:4px;">
        <span style="color:#34d399;">ALREADY PACKED</span>
        <span style="color:#f87171;">STILL TO PACK (?)</span>
      </div>
      <div style="display:flex; height:44px; width:100%; gap:4px;">
        <div id="sim5Packed" style="width:33%; background:linear-gradient(90deg, #059669, #10b981); border-radius:8px 0 0 8px; border:2px solid #34d399; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">
          75 Packed
        </div>
        <div id="sim5Remaining" style="width:67%; background:linear-gradient(90deg, #dc2626, #ef4444); border-radius:0 8px 8px 0; border:2px solid #f87171; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">
          155 Remaining
        </div>
      </div>
    </div>
    <div id="sim5Feedback" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 24px; text-align:center;">
      Total (230) - Packed (75) = <span style="color:#ef4444;">155 Remaining to pack</span>!
    </div>
  </div>
</div>
<script>
function sim5SetScenario(total, packed, unit) {
  document.querySelectorAll('#sim5 .sim-controls button').forEach(b => {
    b.classList.remove('active');
    if (b.innerText.includes(total + ' - ' + packed)) b.classList.add('active');
  });
  const rem = total - packed;
  const pct1 = Math.round((packed / total) * 100);
  const pct2 = 100 - pct1;
  document.getElementById('sim5Packed').style.width = pct1 + '%';
  document.getElementById('sim5Packed').innerText = packed + ' Packed';
  document.getElementById('sim5Remaining').style.width = pct2 + '%';
  document.getElementById('sim5Remaining').innerText = rem + ' Remaining';
  document.getElementById('sim5WholeVal').innerText = 'Whole = ' + total;
  document.getElementById('sim5WholeText').innerText = 'Total ' + unit + ' = ' + total;
  document.getElementById('sim5Feedback').innerHTML = 'Total (' + total + ') - Packed (' + packed + ') = <span style=\"color:#ef4444;\">' + rem + ' ' + unit + ' remaining</span>!';
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🔄 Step-by-Step Borrowing / Unbundling Subtractor</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Reset()">Reset (230 - 75)</button>
      <button class="sim-btn" id="sim6StepBtn" onclick="sim6NextStep()">Next Borrow Step ⏩</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Subtraction Column Display -->
    <div style="background:rgba(0,0,0,0.4); border-radius:12px; border:1px solid rgba(255,255,255,0.2); padding:12px 20px; width:100%; max-width:380px;">
      <!-- Header Row -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-weight:bold; border-bottom:2px solid rgba(255,255,255,0.2); padding-bottom:6px; margin-bottom:8px;">
        <span style="color:#cbd5e1;">Op</span>
        <span style="color:#f87171;">H (100)</span>
        <span style="color:#fbbf24;">T (10)</span>
        <span style="color:#34d399;">O (1)</span>
      </div>
      <!-- Unbundled / Borrowed Row -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:13px; height:22px; color:#cbd5e1;">
        <span>New:</span>
        <span id="sim6NewH" style="color:#f87171; font-weight:bold;"></span>
        <span id="sim6NewT" style="color:#fbbf24; font-weight:bold;"></span>
        <span id="sim6NewO" style="color:#34d399; font-weight:bold;"></span>
      </div>
      <!-- Minuend Row: 2 3 0 -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:18px; font-weight:bold; color:#fff; padding:4px 0;">
        <span></span>
        <span id="sim6OrigH" style="color:#fca5a5;">2</span>
        <span id="sim6OrigT" style="color:#fde047;">3</span>
        <span id="sim6OrigO" style="color:#86efac;">0</span>
      </div>
      <!-- Subtrahend Row: - 0 7 5 -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:18px; font-weight:bold; color:#fff; padding:4px 0; border-bottom:2px solid #ef4444;">
        <span style="color:#ef4444;">-</span>
        <span style="color:#64748b;">0</span>
        <span style="color:#fde047;">7</span>
        <span style="color:#86efac;">5</span>
      </div>
      <!-- Result Row -->
      <div style="display:grid; grid-template-columns: 70px 70px 70px 70px; gap:8px; text-align:center; font-size:22px; font-weight:bold; padding-top:6px;">
        <span style="color:#38bdf8;">=</span>
        <span id="sim6ResH" style="color:#f87171;">-</span>
        <span id="sim6ResT" style="color:#fbbf24;">-</span>
        <span id="sim6ResO" style="color:#34d399;">-</span>
      </div>
    </div>
    <!-- Step feedback message -->
    <div id="sim6Feedback" style="margin-top:12px; font-size:14px; color:#e2e8f0; text-align:center; background:rgba(0,0,0,0.3); border-radius:8px; padding:6px 16px; border:1px solid rgba(255,255,255,0.15);">
      Ready: 230 - 75. Click "Next Borrow Step" to begin with Ones column!
    </div>
  </div>
</div>
<script>
let sim6Step = 0;

function sim6Reset() {
  sim6Step = 0;
  document.getElementById('sim6NewH').innerText = '';
  document.getElementById('sim6NewT').innerText = '';
  document.getElementById('sim6NewO').innerText = '';
  document.getElementById('sim6OrigH').style.textDecoration = 'none';
  document.getElementById('sim6OrigT').style.textDecoration = 'none';
  document.getElementById('sim6OrigO').style.textDecoration = 'none';
  document.getElementById('sim6ResH').innerText = '-';
  document.getElementById('sim6ResT').innerText = '-';
  document.getElementById('sim6ResO').innerText = '-';
  document.getElementById('sim6Feedback').innerHTML = 'Ready: 230 - 75. Click "Next Borrow Step" to subtract Ones column.';
  document.getElementById('sim6StepBtn').disabled = false;
  document.getElementById('sim6StepBtn').innerText = 'Next Borrow Step ⏩';
}

function sim6NextStep() {
  sim6Step++;
  if (sim6Step === 1) {
    document.getElementById('sim6OrigO').style.textDecoration = 'line-through';
    document.getElementById('sim6OrigT').style.textDecoration = 'line-through';
    document.getElementById('sim6NewT').innerText = '2';
    document.getElementById('sim6NewO').innerText = '10';
    document.getElementById('sim6ResO').innerText = '5';
    document.getElementById('sim6Feedback').innerHTML = 'Step 1 (Ones): 0 - 5 impossible. Borrow 1 ten (3 tens become 2 tens). Now 10 ones - 5 = <b style=\"color:#34d399;\">5 Ones</b>!';
  } else if (sim6Step === 2) {
    document.getElementById('sim6OrigH').style.textDecoration = 'line-through';
    document.getElementById('sim6NewH').innerText = '1';
    document.getElementById('sim6NewT').innerText = '12';
    document.getElementById('sim6ResT').innerText = '5';
    document.getElementById('sim6Feedback').innerHTML = 'Step 2 (Tens): 2 tens - 7 tens impossible. Borrow 1 hundred (2 hundreds become 1 hundred). Now 12 tens - 7 = <b style=\"color:#fbbf24;\">5 Tens</b>!';
  } else if (sim6Step === 3) {
    document.getElementById('sim6ResH').innerText = '1';
    document.getElementById('sim6Feedback').innerHTML = 'Step 3 (Hundreds): 1 hundred - 0 = <b style=\"color:#f87171;\">1 Hundred</b>. Final answer = <b style=\"color:#38bdf8; font-size:17px;\">155</b>! 🎉';
    document.getElementById('sim6StepBtn').disabled = true;
    document.getElementById('sim6StepBtn').innerText = 'Completed! ✅';
  }
}
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">📚 Community Library Word Scenario Solver</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Load(1)">Scenario 1: Story & Puzzle Books</button>
      <button class="sim-btn" onclick="sim7Load(2)">Scenario 2: Fiction & Science Books</button>
      <button class="sim-btn" onclick="sim7Load(3)">Scenario 3: Book Borrow Return</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:14px;">
    <!-- Problem Card -->
    <div id="sim7Card" style="background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.2); padding:14px 20px; width:100%; max-width:540px; margin-bottom:12px;">
      <div id="sim7Text" style="font-size:15px; color:#e2e8f0; line-height:1.5; margin-bottom:10px;">
        A community library has a collection of <b>540 total books</b>. There are <b>210 storybooks</b>, and the rest are puzzle books. How many puzzle books are there?
      </div>
      <div style="display:flex; justify-content:space-around; background:rgba(255,255,255,0.05); padding:8px; border-radius:8px;">
        <span id="sim7Given1" style="color:#38bdf8; font-size:13px; font-weight:bold;">Total = 540</span>
        <span id="sim7Given2" style="color:#fbbf24; font-size:13px; font-weight:bold;">Storybooks = 210</span>
        <span id="sim7Target" style="color:#f87171; font-size:13px; font-weight:bold;">Puzzle Books = ?</span>
      </div>
    </div>
    <!-- Visual Bar comparison -->
    <div id="sim7Feedback" style="font-size:16px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 24px; text-align:center;">
      Calculation: 540 - 210 = <span style="font-size:18px;">330 Puzzle Books</span>!
    </div>
  </div>
</div>
<script>
function sim7Load(scen) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(scen.toString()));
  });
  if (scen === 1) {
    document.getElementById('sim7Text').innerHTML = 'A community library has <b>540 total books</b>. There are <b>210 storybooks</b>, and the rest are puzzle books. How many puzzle books are there?';
    document.getElementById('sim7Given1').innerText = 'Total = 540';
    document.getElementById('sim7Given2').innerText = 'Storybooks = 210';
    document.getElementById('sim7Target').innerText = 'Puzzle Books = ?';
    document.getElementById('sim7Feedback').innerHTML = 'Calculation: 540 - 210 = <span style=\"font-size:18px;\">330 Puzzle Books</span>!';
  } else if (scen === 2) {
    document.getElementById('sim7Text').innerHTML = 'The library bought <b>325 fiction novels</b> and <b>168 science encyclopedias</b>. How many books were purchased in total?';
    document.getElementById('sim7Given1').innerText = 'Fiction = 325';
    document.getElementById('sim7Given2').innerText = 'Science = 168';
    document.getElementById('sim7Target').innerText = 'Total = ?';
    document.getElementById('sim7Feedback').innerHTML = 'Calculation: 325 + 168 = <span style=\"font-size:18px;\">493 Total Books</span>!';
  } else if (scen === 3) {
    document.getElementById('sim7Text').innerHTML = 'Out of <b>460 registered books</b>, readers borrowed <b>185 books</b> this week. How many books remain on the shelves?';
    document.getElementById('sim7Given1').innerText = 'Total = 460';
    document.getElementById('sim7Given2').innerText = 'Borrowed = 185';
    document.getElementById('sim7Target').innerText = 'On Shelves = ?';
    document.getElementById('sim7Feedback').innerHTML = 'Calculation: 460 - 185 = <span style=\"font-size:18px;\">275 Books Remaining</span>!';
  }
}
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🔢 Hundreds Number Grid Navigator</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim8Move(0, -10)">⬆️ Up (-10)</button>
      <button class="sim-btn" onclick="sim8Move(0, 10)">⬇️ Down (+10)</button>
      <button class="sim-btn" onclick="sim8Move(-1, 0)">⬅️ Left (-1)</button>
      <button class="sim-btn" onclick="sim8Move(1, 0)">➡️ Right (+1)</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim8Reset()">Center (495)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- 5x5 Subgrid Around Current Number -->
    <div id="sim8Grid" style="display:grid; grid-template-columns: repeat(5, 52px); gap:6px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.2); padding:10px;">
      <!-- Injected 25 cells -->
    </div>
    <div id="sim8Feedback" style="margin-top:10px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Active cell: <span style="color:#fbbf24;">495</span>. Vertical moves alter Tens by ±10; Horizontal moves alter Ones by ±1!
    </div>
  </div>
</div>
<script>
let sim8Val = 495;

function sim8RenderGrid() {
  const grid = document.getElementById('sim8Grid');
  grid.innerHTML = '';
  // Show 5x5 window: rows = sim8Val - 20 to + 20, cols = -2 to +2
  const centerTen = Math.floor(sim8Val / 10) * 10;
  for (let r = -2; r <= 2; r++) {
    const rowStart = centerTen + (r * 10);
    for (let c = -2; c <= 2; c++) {
      const cellVal = (sim8Val % 10) + (r * 10) + c;
      const actualVal = sim8Val + (r * 10) + c;
      const isCur = actualVal === sim8Val;
      const bg = isCur ? '#f59e0b' : 'rgba(255,255,255,0.06)';
      const color = isCur ? '#000' : '#cbd5e1';
      const border = isCur ? '2px solid #fde68a' : '1px solid rgba(255,255,255,0.1)';
      grid.innerHTML += '<div onclick=\"sim8SelectCell(' + actualVal + ')\" style=\"height:36px; display:flex; align-items:center; justify-content:center; background:' + bg + '; color:' + color + '; border-radius:6px; font-weight:bold; font-size:13px; cursor:pointer; border:' + border + ';\">' + actualVal + '</div>';
    }
  }
}

function sim8SelectCell(v) {
  sim8Val = v;
  sim8RenderGrid();
  document.getElementById('sim8Feedback').innerHTML = 'Active cell: <b style=\"color:#fbbf24;\">' + sim8Val + '</b>. Tens digit changes up/down; Ones digit changes left/right!';
}

function sim8Move(dx, dy) {
  sim8Val += (dx + dy);
  sim8RenderGrid();
  document.getElementById('sim8Feedback').innerHTML = 'Moved to: <b style=\"color:#fbbf24;\">' + sim8Val + '</b> (Change: ' + (dy !== 0 ? (dy > 0 ? '+10 Tens' : '-10 Tens') : (dx > 0 ? '+1 Ones' : '-1 Ones')) + ')';
}

function sim8Reset() {
  sim8Val = 495;
  sim8RenderGrid();
  document.getElementById('sim8Feedback').innerHTML = 'Reset to center cell: <b style=\"color:#fbbf24;\">495</b>.';
}
sim8RenderGrid();
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1 to 8).")
    for k in sorted(sims_part1.keys()):
        print(f"Sim {k}: length {len(sims_part1[k])} chars")

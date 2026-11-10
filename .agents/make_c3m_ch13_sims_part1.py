#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 13: Time Goes On
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">📅 July Monthly Calendar Grid Constructor</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Build('all')">Complete Month (31 Days)</button>
      <button class="sim-btn" onclick="sim1Build('week1')">Week 1 Only</button>
      <button class="sim-btn" onclick="sim1Build('sundays')">Highlight Sundays</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim1Reset()">Clear Grid</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Month Title Header -->
    <div style="font-size:16px; font-weight:bold; color:#fbbf24; margin-bottom:8px;">
      JULY 2024 (31 Days • Starts on Monday)
    </div>
    <!-- Calendar Table Grid -->
    <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.2); border-radius:12px; padding:10px; width:100%; max-width:440px;">
      <!-- Weekday Headers -->
      <div style="display:grid; grid-template-columns: repeat(7, 1fr); gap:4px; text-align:center; font-size:11px; font-weight:bold; color:#94a3b8; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:6px; margin-bottom:6px;">
        <span style="color:#f87171;">Mon</span>
        <span>Tue</span>
        <span>Wed</span>
        <span>Thu</span>
        <span>Fri</span>
        <span>Sat</span>
        <span style="color:#fbbf24;">Sun</span>
      </div>
      <!-- 5 Rows of Dates Grid -->
      <div id="sim1Grid" style="display:grid; grid-template-columns: repeat(7, 1fr); gap:4px; text-align:center;">
        <!-- Injected date cells -->
      </div>
    </div>
    <div id="sim1Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      July starts on Monday, July 1 and ends on Wednesday, July 31. Total 31 days!
    </div>
  </div>
</div>
<script>
function sim1Build(mode) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  const grid = document.getElementById('sim1Grid');
  grid.innerHTML = '';
  const totalDays = 31;
  // July 2024: Day 1 is Monday (index 0)
  const maxDay = (mode === 'week1') ? 7 : totalDays;
  for (let d = 1; d <= maxDay; d++) {
    const col = (d - 1) % 7; // 0=Mon, 6=Sun
    let bg = 'rgba(255,255,255,0.06)';
    let color = '#f8fafc';
    let border = '1px solid rgba(255,255,255,0.1)';
    if (col === 6) { // Sunday
      color = '#fbbf24';
      if (mode === 'sundays') {
        bg = 'rgba(245,158,11,0.3)';
        border = '1px solid #fbbf24';
      }
    }
    grid.innerHTML += '<div style=\"height:30px; display:flex; align-items:center; justify-content:center; background:' + bg + '; border:' + border + '; border-radius:6px; font-size:13px; font-weight:bold; color:' + color + ';\">' + d + '</div>';
  }
  const fb = document.getElementById('sim1Feedback');
  if (mode === 'week1') {
    fb.innerHTML = 'Week 1: July 1 (Monday) to July 7 (Sunday). First 7 days placed!';
  } else if (mode === 'sundays') {
    fb.innerHTML = 'July 2024 Sundays: <b style=\"color:#fbbf24;\">July 7, 14, 21, 28</b> (4 Sundays in total).';
  } else {
    fb.innerHTML = 'Complete month: July 1 (Monday) to July 31 (Wednesday). Exactly 31 days!';
  }
}

function sim1Reset() {
  document.getElementById('sim1Grid').innerHTML = '<div style=\"grid-column: span 7; color:#64748b; font-size:13px; padding:20px;\">Grid cleared. Click "Complete Month" to rebuild!</div>';
  document.getElementById('sim1Feedback').innerHTML = 'Grid empty. Ready to construct!';
}
sim1Build('all');
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">🔍 July Calendar Date Query Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2Query('sundays')">All Sundays</button>
      <button class="sim-btn" onclick="sim2Query('thursdays')">All Thursdays</button>
      <button class="sim-btn" onclick="sim2Query('picnic')">3 Days After July 22</button>
      <button class="sim-btn" onclick="sim2Query('reopen')">Next Week Start (Aug 5)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Miniature Grid with Highlighting -->
    <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px; width:100%; max-width:380px;">
      <div style="display:grid; grid-template-columns: repeat(7, 1fr); gap:3px; text-align:center; font-size:10px; font-weight:bold; color:#94a3b8; margin-bottom:4px;">
        <span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span style="color:#fbbf24;">S</span>
      </div>
      <div id="sim2Grid" style="display:grid; grid-template-columns: repeat(7, 1fr); gap:3px; text-align:center;">
        <!-- Injected 31 dates -->
      </div>
    </div>
    <!-- Result Explanation Card -->
    <div id="sim2Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Sundays in July 2024: July 7, 14, 21, and 28 (Total = 4 Sundays).
    </div>
  </div>
</div>
<script>
function sim2Query(type) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(type));
  });
  const grid = document.getElementById('sim2Grid');
  grid.innerHTML = '';
  const fb = document.getElementById('sim2Feedback');
  
  for (let d = 1; d <= 31; d++) {
    const col = (d - 1) % 7; // 0=Mon, 3=Thu, 6=Sun
    let isTarget = false;
    let targetColor = '#38bdf8';

    if (type === 'sundays' && col === 6) {
      isTarget = true;
      targetColor = '#fbbf24';
    } else if (type === 'thursdays' && col === 3) {
      isTarget = true;
      targetColor = '#34d399';
    } else if (type === 'picnic' && d === 25) {
      isTarget = true;
      targetColor = '#f43f5e';
    } else if (type === 'reopen' && d === 31) {
      isTarget = true;
      targetColor = '#a855f7';
    }

    const bg = isTarget ? targetColor : 'rgba(255,255,255,0.06)';
    const textCol = isTarget ? '#000' : '#cbd5e1';
    grid.innerHTML += '<div style=\"height:24px; display:flex; align-items:center; justify-content:center; background:' + bg + '; border-radius:4px; font-size:11px; font-weight:bold; color:' + textCol + ';\">' + d + '</div>';
  }

  if (type === 'sundays') {
    fb.innerHTML = 'Sundays in July 2024: <b style=\"color:#fbbf24;\">July 7, 14, 21, 28</b> (4 Sundays).';
  } else if (type === 'thursdays') {
    fb.innerHTML = 'Thursdays in July 2024: <b style=\"color:#34d399;\">July 4, 11, 18, 25</b> (Jump of +7 days each row).';
  } else if (type === 'picnic') {
    fb.innerHTML = '3 days after July 22 is <b style=\"color:#f43f5e;\">July 25</b> (22 + 3 = 25, a Thursday)!';
  } else if (type === 'reopen') {
    fb.innerHTML = 'July 31 is Wednesday. The next month of August starts on Thursday, August 1!';
  }
}
sim2Query('sundays');
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🎉 Annual Cultural Festival Date Tracker</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Show(1)">Independence Day (Fixed)</button>
      <button class="sim-btn" onclick="sim3Show(2)">Republic Day (Fixed)</button>
      <button class="sim-btn" onclick="sim3Show(3)">Gandhi Jayanti (Fixed)</button>
      <button class="sim-btn" onclick="sim3Show(4)">Lunar Festivals (Shifting)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:14px;">
    <!-- Festival Info Badge -->
    <div id="sim3Card" style="background:rgba(0,0,0,0.3); border-radius:12px; border:2px solid #38bdf8; padding:14px 20px; width:100%; max-width:480px; text-align:center;">
      <div id="sim3Name" style="font-size:18px; color:#f8fafc; font-weight:bold; margin-bottom:6px;">
        🇮🇳 Independence Day
      </div>
      <div id="sim3Date" style="font-size:24px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">
        15 August (15/08)
      </div>
      <div id="sim3Type" style="font-size:12px; color:#cbd5e1; font-weight:bold; background:rgba(56,189,248,0.2); border-radius:6px; padding:4px 10px; display:inline-block;">
        Fixed Solar Calendar Date • Every Year
      </div>
    </div>
    <div id="sim3Feedback" style="margin-top:12px; font-size:14px; font-weight:bold; color:#cbd5e1; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      National holidays remain on the exact same solar date every single year!
    </div>
  </div>
</div>
<script>
function sim3Show(id) {
  document.querySelectorAll('#sim3 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  if (id === 1) {
    document.querySelectorAll('#sim3 .sim-controls button')[0].classList.add('active');
    document.getElementById('sim3Name').innerText = '🇮🇳 Independence Day';
    document.getElementById('sim3Date').innerText = '15 August (15/08)';
    document.getElementById('sim3Date').style.color = '#38bdf8';
    document.getElementById('sim3Type').innerText = 'Fixed Solar Calendar Date • Every Year';
    document.getElementById('sim3Feedback').innerHTML = 'Celebrates freedom since 1947. Fixed on <b>15 August</b> every calendar year.';
  } else if (id === 2) {
    document.querySelectorAll('#sim3 .sim-controls button')[1].classList.add('active');
    document.getElementById('sim3Name').innerText = '🇮🇳 Republic Day';
    document.getElementById('sim3Date').innerText = '26 January (26/01)';
    document.getElementById('sim3Date').style.color = '#fbbf24';
    document.getElementById('sim3Type').innerText = 'Fixed Solar Calendar Date • Every Year';
    document.getElementById('sim3Feedback').innerHTML = 'Marks the Indian Constitution in 1950. Fixed on <b>26 January</b> every year.';
  } else if (id === 3) {
    document.querySelectorAll('#sim3 .sim-controls button')[2].classList.add('active');
    document.getElementById('sim3Name').innerText = '🕊️ Gandhi Jayanti';
    document.getElementById('sim3Date').innerText = '2 October (02/10)';
    document.getElementById('sim3Date').style.color = '#34d399';
    document.getElementById('sim3Type').innerText = 'Fixed Solar Calendar Date • Every Year';
    document.getElementById('sim3Feedback').innerHTML = 'Commemorates Mahatma Gandhi\'s birthday. Fixed on <b>2 October</b> every year.';
  } else if (id === 4) {
    document.querySelectorAll('#sim3 .sim-controls button')[3].classList.add('active');
    document.getElementById('sim3Name').innerText = '🌙 Eid, Deepawali, Ganesh Chaturthi';
    document.getElementById('sim3Date').innerText = 'Dates Vary Annually';
    document.getElementById('sim3Date').style.color = '#f43f5e';
    document.getElementById('sim3Type').innerText = 'Shifting Lunar Calendar System';
    document.getElementById('sim3Feedback').innerHTML = 'Lunar festivals depend on moon phases, so their solar calendar dates shift each year!';
  }
}
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">📊 Yearly Calendar Statistics Visualizer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4SetMode('std')">Standard Year (365 Days)</button>
      <button class="sim-btn" onclick="sim4SetMode('leap')">Leap Year (366 Days)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- 12 Month Day Counts Overview -->
    <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap; max-width:540px; margin-bottom:12px;">
      <div style="background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:6px 12px; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; display:block;">7 Months with 31 Days</span>
        <span style="font-size:15px; color:#38bdf8; font-weight:bold;">Jan, Mar, May, Jul, Aug, Oct, Dec</span>
      </div>
      <div style="background:rgba(245,158,11,0.2); border:1px solid #fbbf24; border-radius:8px; padding:6px 12px; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; display:block;">4 Months with 30 Days</span>
        <span style="font-size:15px; color:#fbbf24; font-weight:bold;">Apr, Jun, Sep, Nov</span>
      </div>
      <div id="sim4FebCard" style="background:rgba(244,63,94,0.2); border:1px solid #f43f5e; border-radius:8px; padding:6px 12px; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; display:block;">February (Special)</span>
        <span id="sim4FebText" style="font-size:15px; color:#f43f5e; font-weight:bold;">28 Days (Standard)</span>
      </div>
    </div>
    <!-- Mathematical Calculation Breakdown -->
    <div id="sim4Math" style="background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.15); padding:8px 20px; font-size:15px; font-weight:bold; color:#f8fafc; text-align:center;">
      365 Days = 52 Full Weeks (52 × 7 = 364 days) + <span style="color:#fbbf24;">1 Extra Day</span>
    </div>
  </div>
</div>
<script>
function sim4SetMode(mode) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  if (mode === 'std') {
    document.querySelectorAll('#sim4 .sim-controls button')[0].classList.add('active');
    document.getElementById('sim4FebText').innerText = '28 Days (Standard)';
    document.getElementById('sim4Math').innerHTML = '365 Days = 52 Full Weeks (52 × 7 = 364) + <span style=\"color:#fbbf24;\">1 Extra Day</span>';
  } else {
    document.querySelectorAll('#sim4 .sim-controls button')[1].classList.add('active');
    document.getElementById('sim4FebText').innerText = '29 Days (Leap Year)';
    document.getElementById('sim4Math').innerHTML = '366 Days = 52 Full Weeks (52 × 7 = 364) + <span style=\"color:#34d399;\">2 Extra Days</span>';
  }
}
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">⏳ Generational Age Gap Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim5Shift(-5)">-5 Years Past</button>
      <button class="sim-btn active" onclick="sim5Reset()">Current Day</button>
      <button class="sim-btn" onclick="sim5Shift(5)">+5 Years Future</button>
      <button class="sim-btn" onclick="sim5Shift(10)">+10 Years Future</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- 3 Generation Age Cards -->
    <div style="display:flex; justify-content:center; gap:16px; width:100%; max-width:520px; margin-bottom:12px;">
      <!-- Child -->
      <div style="background:rgba(255,255,255,0.06); border:2px solid #34d399; border-radius:10px; padding:10px; width:30%; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold;">STUDENT</span>
        <div id="sim5ChildAge" style="font-size:26px; color:#34d399; font-weight:bold; margin-top:4px;">8</div>
        <span style="font-size:10px; color:#94a3b8;">years old</span>
      </div>
      <!-- Mother -->
      <div style="background:rgba(255,255,255,0.06); border:2px solid #38bdf8; border-radius:10px; padding:10px; width:30%; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold;">MOTHER</span>
        <div id="sim5MotherAge" style="font-size:26px; color:#38bdf8; font-weight:bold; margin-top:4px;">32</div>
        <span style="font-size:10px; color:#94a3b8;">years old</span>
      </div>
      <!-- Grandmother -->
      <div style="background:rgba(255,255,255,0.06); border:2px solid #fbbf24; border-radius:10px; padding:10px; width:30%; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold;">GRANDMOTHER</span>
        <div id="sim5GrandAge" style="font-size:26px; color:#fbbf24; font-weight:bold; margin-top:4px;">60</div>
        <span style="font-size:10px; color:#94a3b8;">years old</span>
      </div>
    </div>
    <!-- Constant Age Gap Formula Display -->
    <div id="sim5Feedback" style="font-size:14px; font-weight:bold; color:#f8fafc; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 20px; text-align:center;">
      Age Gap: Mother - Student = <b style="color:#38bdf8;">24 years</b> | Grandmother - Mother = <b style="color:#fbbf24;">28 years</b> (Always constant!)
    </div>
  </div>
</div>
<script>
let sim5Delta = 0;

function sim5Shift(d) {
  sim5Delta += d;
  sim5Update();
}

function sim5Reset() {
  sim5Delta = 0;
  sim5Update();
}

function sim5Update() {
  const c = 8 + sim5Delta;
  const m = 32 + sim5Delta;
  const g = 60 + sim5Delta;
  document.getElementById('sim5ChildAge').innerText = c;
  document.getElementById('sim5MotherAge').innerText = m;
  document.getElementById('sim5GrandAge').innerText = g;
  document.getElementById('sim5Feedback').innerHTML = 'Year Offset: <b>' + (sim5Delta >= 0 ? '+' : '') + sim5Delta + ' years</b>. Age Gap: Mother - Student = <b style=\"color:#38bdf8;\">' + (m - c) + ' years</b>. The age gap never changes!';
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">📜 Official Birth Certificate Field Reader</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Highlight('dob')">Date of Birth</button>
      <button class="sim-btn" onclick="sim6Highlight('milestone2026')">Age in 2026</button>
      <button class="sim-btn" onclick="sim6Highlight('reg')">Registration Date</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Certificate Card Mockup -->
    <div style="background:linear-gradient(135deg, #1e293b, #0f172a); border:2px solid #94a3b8; border-radius:12px; padding:12px 18px; width:100%; max-width:480px; box-shadow:0 4px 12px rgba(0,0,0,0.5);">
      <div style="text-align:center; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:6px; margin-bottom:8px;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold; letter-spacing:1px;">GRAM PANCHAYAT BIRTH RECORD</span>
      </div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:12px;">
        <div>
          <span style="color:#94a3b8; display:block;">Registration No:</span>
          <span id="sim6RegNo" style="font-weight:bold; color:#f8fafc;">GP-2016-0842</span>
        </div>
        <div>
          <span style="color:#94a3b8; display:block;">Gender:</span>
          <span style="font-weight:bold; color:#f8fafc;">Female</span>
        </div>
        <div id="sim6DobBox" style="grid-column:span 2; background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:6px; padding:6px;">
          <span style="color:#cbd5e1; display:block; font-size:11px;">Date of Birth (DD/MM/YYYY):</span>
          <span style="font-size:16px; font-weight:bold; color:#38bdf8;">02 / 05 / 2016 (Second May Two Thousand Sixteen)</span>
        </div>
      </div>
    </div>
    <div id="sim6Feedback" style="margin-top:10px; font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Date of Birth: 02/05/2016. Month 05 represents May!
    </div>
  </div>
</div>
<script>
function sim6Highlight(mode) {
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });
  const fb = document.getElementById('sim6Feedback');
  const dobBox = document.getElementById('sim6DobBox');
  if (mode === 'dob') {
    dobBox.style.borderColor = '#38bdf8';
    dobBox.style.background = 'rgba(56,189,248,0.2)';
    fb.innerHTML = 'Born on <b>02/05/2016</b> (2nd of May 2016). Month number 05 = May!';
  } else if (mode === 'milestone2026') {
    dobBox.style.borderColor = '#34d399';
    dobBox.style.background = 'rgba(16,185,129,0.2)';
    fb.innerHTML = 'In 2026: 2026 - 2016 = <b style=\"color:#34d399; font-size:16px;\">10 years old</b> (10th Birthday)!';
  } else if (mode === 'reg') {
    dobBox.style.borderColor = '#fbbf24';
    dobBox.style.background = 'rgba(245,158,11,0.2)';
    fb.innerHTML = 'Registered under official village panchayat registry in May 2016.';
  }
}
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">📈 School Milestone Historical Timeline</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim7Select(2016)">2016: Born</button>
      <button class="sim-btn" onclick="sim7Select(2019)">2019: Nursery</button>
      <button class="sim-btn" onclick="sim7Select(2022)">2022: Grade 1</button>
      <button class="sim-btn active" onclick="sim7Select(2024)">2024: Grade 3</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Horizontal Timeline SVG -->
    <svg viewBox="0 0 540 80" style="width:100%; max-width:540px; height:80px; background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Base Axis Line -->
      <line x1="40" y1="45" x2="500" y2="45" stroke="#64748b" stroke-width="3" stroke-linecap="round"/>
      <!-- Milestone Nodes: 2016, 2019, 2022, 2024 -->
      <circle cx="60" cy="45" r="9" fill="#38bdf8"/>
      <text x="60" y="68" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">2016</text>
      
      <circle cx="180" cy="45" r="9" fill="#fbbf24"/>
      <text x="180" y="68" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">2019</text>
      
      <circle cx="320" cy="45" r="9" fill="#f43f5e"/>
      <text x="320" y="68" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">2022</text>
      
      <circle id="sim7Highlight" cx="440" cy="45" r="13" fill="#34d399" stroke="#fff" stroke-width="3"/>
      <text x="440" y="68" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">2024</text>
    </svg>
    <div id="sim7Feedback" style="margin-top:12px; font-size:14px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      2024: Grade 3 (Age 8 years). Timeline progresses from left to right!
    </div>
  </div>
</div>
<script>
function sim7Select(year) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(year.toString()));
  });
  const hl = document.getElementById('sim7Highlight');
  const fb = document.getElementById('sim7Feedback');
  if (year === 2016) {
    hl.setAttribute('cx', '60');
    fb.innerHTML = '2016: Child is born! Age = 0 years.';
  } else if (year === 2019) {
    hl.setAttribute('cx', '180');
    fb.innerHTML = '2019: Joins Nursery School (Age 3 years).';
  } else if (year === 2022) {
    hl.setAttribute('cx', '320');
    fb.innerHTML = '2022: Enters Primary Grade 1 (Age 6 years).';
  } else if (year === 2024) {
    hl.setAttribute('cx', '440');
    fb.innerHTML = '2024: Currently studying in Grade 3 (Age 8 years). Progression = 8 years!';
  }
}
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">⏰ Analog Clock Anatomy & Hands Manipulator</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim8AddMin(5)">+5 Mins</button>
      <button class="sim-btn" onclick="sim8AddMin(15)">+15 Mins</button>
      <button class="sim-btn" onclick="sim8AddHour(1)">+1 Hour</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim8Reset()">Reset (12:00)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- SVG Analog Clock Dial -->
    <svg viewBox="0 0 200 200" style="width:160px; height:160px;">
      <!-- Outer Dial Circle -->
      <circle cx="100" cy="100" r="90" fill="#1e293b" stroke="#475569" stroke-width="6"/>
      <circle cx="100" cy="100" r="82" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
      <!-- Numbers 1 to 12 -->
      <text x="100" y="32" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">12</text>
      <text x="168" y="105" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">3</text>
      <text x="100" y="174" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">6</text>
      <text x="32" y="105" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">9</text>
      <!-- Hour Hand (Red/Orange) -->
      <line id="sim8HourHand" x1="100" y1="100" x2="100" y2="55" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
      <!-- Minute Hand (Blue/Cyan) -->
      <line id="sim8MinHand" x1="100" y1="100" x2="100" y2="30" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
      <!-- Center Pin -->
      <circle cx="100" cy="100" r="4" fill="#fbbf24"/>
    </svg>
    <div id="sim8Feedback" style="margin-top:8px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Clock Time: <span id="sim8TimeStr" style="color:#fbbf24;">12:00</span> (Hour hand points at 12, Minute hand at 12)
    </div>
  </div>
</div>
<script>
let sim8H = 12;
let sim8M = 0;

function sim8Render() {
  const minAngle = sim8M * 6; // 360 / 60
  const hourAngle = (sim8H % 12) * 30 + (sim8M * 0.5);
  
  const radM = (minAngle - 90) * (Math.PI / 180);
  const radH = (hourAngle - 90) * (Math.PI / 180);
  
  const xm = 100 + 70 * Math.cos(radM);
  const ym = 100 + 70 * Math.sin(radM);
  document.getElementById('sim8MinHand').setAttribute('x2', xm);
  document.getElementById('sim8MinHand').setAttribute('y2', ym);
  
  const xh = 100 + 45 * Math.cos(radH);
  const yh = 100 + 45 * Math.sin(radH);
  document.getElementById('sim8HourHand').setAttribute('x2', xh);
  document.getElementById('sim8HourHand').setAttribute('y2', yh);
  
  const mStr = sim8M < 10 ? '0' + sim8M : sim8M;
  document.getElementById('sim8TimeStr').innerText = sim8H + ':' + mStr;
}

function sim8AddMin(mins) {
  sim8M += mins;
  while (sim8M >= 60) {
    sim8M -= 60;
    sim8H = (sim8H % 12) + 1;
  }
  sim8Render();
}

function sim8AddHour(hrs) {
  sim8H = ((sim8H - 1 + hrs) % 12) + 1;
  sim8Render();
}

function sim8Reset() {
  sim8H = 12;
  sim8M = 0;
  sim8Render();
}
sim8Render();
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1 to 8).")
    for k in sorted(sims_part1.keys()):
        print(f"Sim {k}: length {len(sims_part1[k])} chars")

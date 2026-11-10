#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 13: Time Goes On
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">🕒 Clock Fractional Benchmark Demonstrator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Set('qpast')">Quarter Past (8:15)</button>
      <button class="sim-btn" onclick="sim9Set('half')">Half Past (8:30)</button>
      <button class="sim-btn" onclick="sim9Set('qto')">Quarter To (8:45)</button>
      <button class="sim-btn" onclick="sim9Set('oclock')">8 O'Clock (8:00)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- Clock SVG with Shaded Fraction Wedge -->
    <svg viewBox="0 0 200 200" style="width:160px; height:160px;">
      <!-- Outer Dial -->
      <circle cx="100" cy="100" r="90" fill="#1e293b" stroke="#475569" stroke-width="6"/>
      <!-- Shaded Sector Wedge -->
      <path id="sim9Wedge" d="M 100 100 L 100 20 A 80 80 0 0 1 180 100 Z" fill="rgba(56,189,248,0.25)"/>
      <!-- Hour Numbers -->
      <text x="100" y="32" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">12</text>
      <text x="168" y="105" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">3</text>
      <text x="100" y="174" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">6</text>
      <text x="32" y="105" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">9</text>
      <!-- Hour Hand -->
      <line id="sim9HourHand" x1="100" y1="100" x2="65" y2="120" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
      <!-- Minute Hand -->
      <line id="sim9MinHand" x1="100" y1="100" x2="170" y2="100" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
      <circle cx="100" cy="100" r="4" fill="#fbbf24"/>
    </svg>
    <div id="sim9Feedback" style="margin-top:10px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Quarter Past 8 (8:15) • Minute hand at 3 • 1/4 of circle (15 mins)
    </div>
  </div>
</div>
<script>
function sim9Set(mode) {
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode));
  });
  const wedge = document.getElementById('sim9Wedge');
  const minHand = document.getElementById('sim9MinHand');
  const hourHand = document.getElementById('sim9HourHand');
  const fb = document.getElementById('sim9Feedback');

  if (mode === 'qpast') {
    wedge.setAttribute('d', 'M 100 100 L 100 20 A 80 80 0 0 1 180 100 Z');
    wedge.setAttribute('fill', 'rgba(56,189,248,0.3)');
    minHand.setAttribute('x2', '170'); minHand.setAttribute('y2', '100');
    hourHand.setAttribute('x2', '65'); hourHand.setAttribute('y2', '125');
    fb.innerHTML = '✨ <b>Quarter Past 8 (8:15)</b>: Minute hand at 3. Completed 1/4 of dial (15 minutes).';
  } else if (mode === 'half') {
    wedge.setAttribute('d', 'M 100 100 L 100 20 A 80 80 0 0 1 100 180 Z');
    wedge.setAttribute('fill', 'rgba(245,158,11,0.3)');
    minHand.setAttribute('x2', '100'); minHand.setAttribute('y2', '170');
    hourHand.setAttribute('x2', '60'); hourHand.setAttribute('y2', '135');
    fb.innerHTML = '✨ <b>Half Past 8 (8:30)</b>: Minute hand at 6. Completed 1/2 of dial (30 minutes).';
  } else if (mode === 'qto') {
    wedge.setAttribute('d', 'M 100 100 L 100 20 A 80 80 0 0 1 20 100 Z');
    wedge.setAttribute('fill', 'rgba(244,63,94,0.3)');
    minHand.setAttribute('x2', '30'); minHand.setAttribute('y2', '100');
    hourHand.setAttribute('x2', '55'); hourHand.setAttribute('y2', '110');
    fb.innerHTML = '✨ <b>Quarter to 9 (8:45)</b>: Minute hand at 9. 45 minutes passed, 15 minutes left to 9:00.';
  } else if (mode === 'oclock') {
    wedge.setAttribute('d', 'M 100 100 L 100 20 Z');
    minHand.setAttribute('x2', '100'); minHand.setAttribute('y2', '30');
    hourHand.setAttribute('x2', '60'); hourHand.setAttribute('y2', '120');
    fb.innerHTML = '✨ <b>8 O\'Clock (8:00)</b>: Minute hand at 12. Exactly 0 minutes past the hour.';
  }
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🗓️ Daily Schedule Activity & Clock Mapper</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Select('wake')">6:30 AM: Wake Up</button>
      <button class="sim-btn" onclick="sim10Select('school')">8:00 AM: School</button>
      <button class="sim-btn" onclick="sim10Select('lunch')">12:30 PM: Lunch</button>
      <button class="sim-btn" onclick="sim10Select('play')">4:30 PM: Play</button>
      <button class="sim-btn" onclick="sim10Select('sleep')">9:00 PM: Sleep</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Selected Event Display -->
    <div style="display:flex; align-items:center; gap:20px; background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.15); padding:12px 24px; max-width:480px; width:100%;">
      <!-- Mini Clock -->
      <svg viewBox="0 0 100 100" style="width:70px; height:70px; flex-shrink:0;">
        <circle cx="50" cy="50" r="45" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
        <line id="sim10H" x1="50" y1="50" x2="50" y2="70" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
        <line id="sim10M" x1="50" y1="50" x2="50" y2="85" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="50" cy="50" r="3" fill="#fbbf24"/>
      </svg>
      <div>
        <div id="sim10Title" style="font-size:16px; font-weight:bold; color:#f8fafc;">Morning Wake Up & Yoga</div>
        <div id="sim10Time" style="font-size:22px; font-weight:bold; color:#fbbf24; margin-top:2px;">6:30 AM (Half past six)</div>
      </div>
    </div>
    <div id="sim10Feedback" style="margin-top:12px; font-size:14px; font-weight:bold; color:#cbd5e1; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Mapping daily habits to clock times establishes healthy discipline throughout the day.
    </div>
  </div>
</div>
<script>
function sim10Select(type) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(type));
  });
  const hHand = document.getElementById('sim10H');
  const mHand = document.getElementById('sim10M');
  const title = document.getElementById('sim10Title');
  const time = document.getElementById('sim10Time');

  if (type === 'wake') {
    title.innerText = 'Morning Wake Up & Exercise';
    time.innerText = '6:30 AM (Half past six)';
    hHand.setAttribute('x2', '50'); hHand.setAttribute('y2', '72');
    mHand.setAttribute('x2', '50'); mHand.setAttribute('y2', '85');
  } else if (type === 'school') {
    title.innerText = 'Morning School Assembly';
    time.innerText = '8:00 AM (Eight o\'clock)';
    hHand.setAttribute('x2', '28'); hHand.setAttribute('y2', '62');
    mHand.setAttribute('x2', '50'); mHand.setAttribute('y2', '15');
  } else if (type === 'lunch') {
    title.innerText = 'Mid-Day Lunch Recess';
    time.innerText = '12:30 PM (Half past twelve)';
    hHand.setAttribute('x2', '52'); hHand.setAttribute('y2', '28');
    mHand.setAttribute('x2', '50'); mHand.setAttribute('y2', '85');
  } else if (type === 'play') {
    title.innerText = 'Outdoor Sports & Games';
    time.innerText = '4:30 PM (Half past four)';
    hHand.setAttribute('x2', '68'); hHand.setAttribute('y2', '64');
    mHand.setAttribute('x2', '50'); mHand.setAttribute('y2', '85');
  } else if (type === 'sleep') {
    title.innerText = 'Bedtime & Night Sleep';
    time.innerText = '9:00 PM (Nine o\'clock)';
    hHand.setAttribute('x2', '25'); hHand.setAttribute('y2', '50');
    mHand.setAttribute('x2', '50'); mHand.setAttribute('y2', '15');
  }
}
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🌱 Long Duration Activity Classifier (Months, Weeks, Days)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Filter('months')">Takes Months</button>
      <button class="sim-btn" onclick="sim11Filter('weeks')">Takes Weeks</button>
      <button class="sim-btn" onclick="sim11Filter('days')">Takes Days</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Activities Card Container -->
    <div id="sim11CardsWrap" style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; max-width:540px; margin-bottom:12px;">
      <!-- Injected activities -->
    </div>
    <div id="sim11Feedback" style="font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Processes like crop growth and season transitions require several continuous months.
    </div>
  </div>
</div>
<script>
function sim11Filter(unit) {
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(unit));
  });
  const wrap = document.getElementById('sim11CardsWrap');
  wrap.innerHTML = '';
  const fb = document.getElementById('sim11Feedback');

  if (unit === 'months') {
    wrap.innerHTML += '<div style=\"background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🌾 Growing Wheat Crop (3-4 Months)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🍂 Summer to Winter Shift (5-6 Months)</div>';
    fb.innerHTML = 'Measured in <b>Months</b>: Agricultural cycles and seasonal transitions take multiple months.';
  } else if (unit === 'weeks') {
    wrap.innerHTML += '<div style=\"background:rgba(245,158,11,0.2); border:1px solid #fbbf24; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🔬 Science Fair Model (2-3 Weeks)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(245,158,11,0.2); border:1px solid #fbbf24; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">📚 Finishing a Math Chapter (2 Weeks)</div>';
    fb.innerHTML = 'Measured in <b>Weeks</b>: Thorough learning units and detailed school projects span weeks.';
  } else if (unit === 'days') {
    wrap.innerHTML += '<div style=\"background:rgba(52,211,153,0.2); border:1px solid #34d399; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🧶 Knitting a Sweater (4-6 Days)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(52,211,153,0.2); border:1px solid #34d399; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🧱 Curing Clay Bricks (3 Days)</div>';
    fb.innerHTML = 'Measured in <b>Days</b>: Hand-crafting clothes and curing materials take several days.';
  }
}
sim11Filter('months');
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">⚡ Short Duration Activity Classifier (Hours, Minutes, Seconds)</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim12Filter('hours')">Takes Hours</button>
      <button class="sim-btn active" onclick="sim12Filter('minutes')">Takes Minutes</button>
      <button class="sim-btn" onclick="sim12Filter('seconds')">Takes Seconds</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Activities Card Display -->
    <div id="sim12CardsWrap" style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; max-width:540px; margin-bottom:12px;">
      <!-- Injected activities -->
    </div>
    <div id="sim12Feedback" style="font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Routine daily self-care actions are measured in minutes.
    </div>
  </div>
</div>
<script>
function sim12Filter(unit) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(unit));
  });
  const wrap = document.getElementById('sim12CardsWrap');
  wrap.innerHTML = '';
  const fb = document.getElementById('sim12Feedback');

  if (unit === 'hours') {
    wrap.innerHTML += '<div style=\"background:rgba(168,85,247,0.2); border:1px solid #a855f7; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🧵 Stitching a Shirt (2-3 Hours)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(168,85,247,0.2); border:1px solid #a855f7; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🚂 District Train Journey (4 Hours)</div>';
    fb.innerHTML = 'Measured in <b>Hours</b>: Garment tailoring and travel between towns require hours.';
  } else if (unit === 'minutes') {
    wrap.innerHTML += '<div style=\"background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🪥 Brushing Teeth (2-3 Minutes)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🥛 Boiling Milk (5-8 Minutes)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(56,189,248,0.2); border:1px solid #38bdf8; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🚿 Taking a Shower (10 Minutes)</div>';
    fb.innerHTML = 'Measured in <b>Minutes</b>: Everyday tasks like brushing, cooking, and bathing take minutes.';
  } else if (unit === 'seconds') {
    wrap.innerHTML += '<div style=\"background:rgba(244,63,94,0.2); border:1px solid #f43f5e; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">👁️ Blinking Your Eye (< 1 Second)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(244,63,94,0.2); border:1px solid #f43f5e; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">👏 Clapping Hands (1 Second)</div>';
    wrap.innerHTML += '<div style=\"background:rgba(244,63,94,0.2); border:1px solid #f43f5e; border-radius:8px; padding:10px 16px; color:#fff; font-weight:bold;\">🍂 Catching a Falling Leaf (2 Seconds)</div>';
    fb.innerHTML = 'Measured in <b>Seconds</b>: Blinking, snapping, and catching happen almost instantaneously!';
  }
}
sim12Filter('minutes');
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">⏱️ Minute Interval Estimator & Internal Clock Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Set(1)">1 Minute (Pencil Sharpening)</button>
      <button class="sim-btn" onclick="sim13Set(5)">5 Minutes (Bag Packing)</button>
      <button class="sim-btn" onclick="sim13Set(15)">15 Minutes (Lunch Meal)</button>
      <button class="sim-btn" onclick="sim13Set(45)">45 Minutes (Class Period)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Visual Progress Bar for Duration -->
    <div style="width:100%; max-width:480px; margin-bottom:12px;">
      <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:4px;">
        <span id="sim13TaskName">Task: Sharpening a Pencil</span>
        <span id="sim13DurationText" style="color:#fbbf24; font-size:14px;">1 Minute</span>
      </div>
      <div style="height:24px; background:rgba(255,255,255,0.1); border-radius:12px; overflow:hidden; border:1px solid rgba(255,255,255,0.2);">
        <div id="sim13Bar" style="width:1.6%; height:100%; background:linear-gradient(90deg, #38bdf8, #34d399); border-radius:12px; transition:width 0.4s ease;"></div>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:10px; color:#64748b; margin-top:2px;">
        <span>0 min</span><span>15 min</span><span>30 min</span><span>45 min</span><span>60 min (1 hr)</span>
      </div>
    </div>
    <div id="sim13Feedback" style="font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      1 minute is 1/60 of an hour. Perfect for sharpening a pencil or tying shoelaces!
    </div>
  </div>
</div>
<script>
function sim13Set(mins) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes('(' + mins + ')'));
  });
  const pct = (mins / 60) * 100;
  document.getElementById('sim13Bar').style.width = pct + '%';
  document.getElementById('sim13DurationText').innerText = mins + ' Minutes (' + Math.round(pct) + '% of an hour)';
  const tName = document.getElementById('sim13TaskName');
  const fb = document.getElementById('sim13Feedback');

  if (mins === 1) {
    tName.innerText = 'Task: Sharpening a Wooden Pencil';
    fb.innerHTML = '<b>1 Minute</b>: 1/60 of an hour. Quick and simple routine tasks!';
  } else if (mins === 5) {
    tName.innerText = 'Task: Packing School Bag with Books';
    fb.innerHTML = '<b>5 Minutes</b>: 1/12 of an hour. Organizing notebooks, timetable, and pencil case.';
  } else if (mins === 15) {
    tName.innerText = 'Task: Eating Warm Lunch Meal';
    fb.innerHTML = '<b>15 Minutes</b>: Exactly one quarter (1/4) of an hour!';
  } else if (mins === 45) {
    tName.innerText = 'Task: Full Classroom Study Period';
    fb.innerHTML = '<b>45 Minutes</b>: Exactly three quarters (3/4) of an hour!';
  }
}
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">⏳ Start & End Elapsed Time Calculator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Set(4, 15, 5, 0, 'Reading')">4:15 PM → 5:00 PM</button>
      <button class="sim-btn" onclick="sim14Set(10, 20, 11, 5, 'Painting')">10:20 AM → 11:05 AM</button>
      <button class="sim-btn" onclick="sim14Set(2, 10, 3, 25, 'Sports')">2:10 PM → 3:25 PM</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Side-by-side Start & End Clocks -->
    <div style="display:flex; justify-content:space-around; align-items:center; width:100%; max-width:520px; margin-bottom:12px;">
      <!-- Start Box -->
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); border-radius:10px; padding:10px 16px; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold;">START TIME</span>
        <div id="sim14StartStr" style="font-size:22px; color:#38bdf8; font-weight:bold; margin-top:2px;">4:15 PM</div>
      </div>
      <!-- Arrow -->
      <div style="font-size:24px; color:#fbbf24; font-weight:bold;">➜</div>
      <!-- End Box -->
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); border-radius:10px; padding:10px 16px; text-align:center;">
        <span style="font-size:11px; color:#cbd5e1; font-weight:bold;">END TIME</span>
        <div id="sim14EndStr" style="font-size:22px; color:#34d399; font-weight:bold; margin-top:2px;">5:00 PM</div>
      </div>
    </div>
    <!-- Elapsed Result Box -->
    <div id="sim14Feedback" style="font-size:16px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 24px; text-align:center;">
      Elapsed Time: <span style="color:#34d399;">45 Minutes</span> (60 - 15 = 45 mins)
    </div>
  </div>
</div>
<script>
function sim14Set(sh, sm, eh, em, act) {
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(act));
  });
  const sStr = sh + ':' + (sm < 10 ? '0' + sm : sm);
  const eStr = eh + ':' + (em < 10 ? '0' + em : em);
  document.getElementById('sim14StartStr').innerText = sStr;
  document.getElementById('sim14EndStr').innerText = eStr;

  const totalStartMins = sh * 60 + sm;
  const totalEndMins = eh * 60 + em;
  const elapsed = totalEndMins - totalStartMins;
  const hrs = Math.floor(elapsed / 60);
  const mins = elapsed % 60;

  let resStr = '';
  if (hrs > 0) resStr += hrs + ' Hour ';
  if (mins > 0 || hrs === 0) resStr += mins + ' Minutes';

  document.getElementById('sim14Feedback').innerHTML = 'Activity: <b>' + act + '</b> • Elapsed Duration: <span style=\"color:#34d399;\">' + resStr + '</span>!';
}
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">🚉 12-Hour vs 24-Hour Railway Clock Converter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Set(18, 2)">18:02 (6:02 PM)</button>
      <button class="sim-btn" onclick="sim15Set(13, 15)">13:15 (1:15 PM)</button>
      <button class="sim-btn" onclick="sim15Set(21, 30)">21:30 (9:30 PM)</button>
      <button class="sim-btn" onclick="sim15Set(8, 45)">08:45 (8:45 AM)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Dual Display Screens -->
    <div style="display:flex; gap:16px; justify-content:center; align-items:center; width:100%; max-width:520px; margin-bottom:12px;">
      <!-- 24-Hour Railway Board -->
      <div style="background:#022c22; border:2px solid #059669; border-radius:10px; padding:10px 16px; text-align:center; width:45%;">
        <span style="font-size:10px; color:#6ee7b7; font-weight:bold; letter-spacing:1px; display:block;">RAILWAY / 24-HOUR TIME</span>
        <span id="sim15RailTime" style="font-size:26px; font-weight:bold; color:#a7f3d0; font-family:monospace;">18:02</span>
      </div>
      <div style="font-size:20px; color:#fbbf24; font-weight:bold;">⇄</div>
      <!-- 12-Hour Standard Clock -->
      <div style="background:#1e1b4b; border:2px solid #6366f1; border-radius:10px; padding:10px 16px; text-align:center; width:45%;">
        <span style="font-size:10px; color:#a5b4fc; font-weight:bold; letter-spacing:1px; display:block;">CIVILIAN / 12-HOUR TIME</span>
        <span id="sim15CivilTime" style="font-size:26px; font-weight:bold; color:#c7d2fe; font-family:monospace;">6:02 PM</span>
      </div>
    </div>
    <!-- Conversion Rule Explanation -->
    <div id="sim15Feedback" style="font-size:14px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      After 12:00 noon, subtract 12 from the 24-hour time: 18 - 12 = 6, so 18:02 = 6:02 PM!
    </div>
  </div>
</div>
<script>
function sim15Set(h24, m) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes('(' + h24 + ','));
  });
  const railStr = (h24 < 10 ? '0' + h24 : h24) + ':' + (m < 10 ? '0' + m : m);
  let civH = h24;
  let ampm = 'AM';
  if (h24 >= 12) {
    ampm = 'PM';
    if (h24 > 12) civH = h24 - 12;
  }
  if (h24 === 0) civH = 12;
  const civStr = civH + ':' + (m < 10 ? '0' + m : m) + ' ' + ampm;

  document.getElementById('sim15RailTime').innerText = railStr;
  document.getElementById('sim15CivilTime').innerText = civStr;

  const fb = document.getElementById('sim15Feedback');
  if (h24 >= 12) {
    fb.innerHTML = 'Rule: ' + h24 + ' - 12 = <b style=\"color:#a7f3d0;\">' + civH + '</b>. Thus, ' + railStr + ' = <b style=\"color:#c7d2fe;\">' + civStr + '</b>!';
  } else {
    fb.innerHTML = 'Morning hours (before 12 noon) are identical: ' + railStr + ' = <b style=\"color:#c7d2fe;\">' + civStr + '</b>.';
  }
}
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">⏳ Interactive Sand Clock (Hourglass) Timer</div>
    <div class="sim-controls">
      <button class="sim-btn active" id="sim16StartBtn" onclick="sim16Toggle()">Start Flow ⏳</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim16Flip()">Flip Timer 🔄</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px;">
    <!-- Hourglass SVG -->
    <svg viewBox="0 0 100 120" style="width:90px; height:108px;">
      <!-- Glass Outline -->
      <path d="M 20 10 L 80 10 L 55 60 L 80 110 L 20 110 L 45 60 Z" fill="rgba(255,255,255,0.06)" stroke="#94a3b8" stroke-width="3"/>
      <!-- Top Sand Bulb -->
      <polygon id="sim16TopSand" points="26,14 74,14 50,60" fill="#fbbf24"/>
      <!-- Stream -->
      <line id="sim16Stream" x1="50" y1="58" x2="50" y2="105" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="2 2"/>
      <!-- Bottom Sand Heap -->
      <polygon id="sim16BottomSand" points="50,108 50,108 50,108" fill="#fbbf24"/>
    </svg>
    <!-- Elapsed seconds display -->
    <div id="sim16Display" style="margin-top:6px; font-size:16px; font-weight:bold; color:#fbbf24;">
      Timer: <span id="sim16Secs">0</span>s / 60s
    </div>
    <div id="sim16Feedback" style="margin-top:6px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:4px 18px; text-align:center;">
      Gravity pulls sand downward at a steady, reliable flow rate!
    </div>
  </div>
</div>
<script>
let sim16Running = false;
let sim16Elapsed = 0;
let sim16Interval = null;

function sim16Toggle() {
  if (sim16Running) {
    clearInterval(sim16Interval);
    sim16Running = false;
    document.getElementById('sim16StartBtn').innerText = 'Resume Flow ⏳';
  } else {
    sim16Running = true;
    document.getElementById('sim16StartBtn').innerText = 'Pause Flow ⏸️';
    sim16Interval = setInterval(() => {
      if (sim16Elapsed < 60) {
        sim16Elapsed++;
        document.getElementById('sim16Secs').innerText = sim16Elapsed;
        // Adjust visual sand levels
        const topH = 14 + (sim16Elapsed / 60) * 44;
        document.getElementById('sim16TopSand').setAttribute('points', '26,' + topH + ' 74,' + topH + ' 50,60');
        const bW = (sim16Elapsed / 60) * 26;
        document.getElementById('sim16BottomSand').setAttribute('points', (50 - bW) + ',108 ' + (50 + bW) + ',108 50,' + (108 - (sim16Elapsed / 60) * 30));
      } else {
        clearInterval(sim16Interval);
        sim16Running = false;
        document.getElementById('sim16StartBtn').innerText = 'Finished! ✅';
        document.getElementById('sim16Feedback').innerHTML = '🎉 <b>1 Full Minute Completed!</b> All sand has poured into bottom bulb.';
      }
    }, 100);
  }
}

function sim16Flip() {
  clearInterval(sim16Interval);
  sim16Running = false;
  sim16Elapsed = 0;
  document.getElementById('sim16Secs').innerText = '0';
  document.getElementById('sim16TopSand').setAttribute('points', '26,14 74,14 50,60');
  document.getElementById('sim16BottomSand').setAttribute('points', '50,108 50,108 50,108');
  document.getElementById('sim16StartBtn').innerText = 'Start Flow ⏳';
  document.getElementById('sim16Feedback').innerHTML = 'Timer flipped and reset to 0 seconds. Ready to run!';
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9 to 16).")
    for k in sorted(sims_part2.keys()):
        print(f"Sim {k}: length {len(sims_part2[k])} chars")

#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 12: Give and Take
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">⚡ Digit Change Pattern Analyzer</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim9Operate(100)">+100 (Hundreds)</button>
      <button class="sim-btn" onclick="sim9Operate(10)">+10 (Tens)</button>
      <button class="sim-btn" onclick="sim9Operate(1)">+1 (Ones)</button>
      <button class="sim-btn" onclick="sim9Operate(-100)">-100 (Hundreds)</button>
      <button class="sim-btn" onclick="sim9Operate(-10)">-10 (Tens)</button>
      <button class="sim-btn" onclick="sim9Operate(-1)">-1 (Ones)</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim9Reset()">Reset (454)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Large 3-Digit Display with Place Highlighting -->
    <div style="display:flex; gap:16px; margin-bottom:14px;">
      <!-- Hundreds -->
      <div style="display:flex; flex-direction:column; align-items:center;">
        <span style="font-size:12px; color:#f87171; font-weight:bold; margin-bottom:4px;">HUNDREDS</span>
        <div id="sim9DigitH" style="width:70px; height:80px; background:rgba(239,68,68,0.2); border:2px solid #f87171; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:40px; font-weight:bold;">
          4
        </div>
      </div>
      <!-- Tens -->
      <div style="display:flex; flex-direction:column; align-items:center;">
        <span style="font-size:12px; color:#fbbf24; font-weight:bold; margin-bottom:4px;">TENS</span>
        <div id="sim9DigitT" style="width:70px; height:80px; background:rgba(245,158,11,0.2); border:2px solid #fbbf24; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:40px; font-weight:bold;">
          5
        </div>
      </div>
      <!-- Ones -->
      <div style="display:flex; flex-direction:column; align-items:center;">
        <span style="font-size:12px; color:#34d399; font-weight:bold; margin-bottom:4px;">ONES</span>
        <div id="sim9DigitO" style="width:70px; height:80px; background:rgba(16,185,129,0.2); border:2px solid #34d399; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; font-size:40px; font-weight:bold;">
          4
        </div>
      </div>
    </div>
    <div id="sim9Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Starting value: 454. Click any operation to see which digit responds!
    </div>
  </div>
</div>
<script>
let sim9Val = 454;

function sim9UpdateDisplay(changedCol) {
  const h = Math.floor(sim9Val / 100);
  const t = Math.floor((sim9Val % 100) / 10);
  const o = sim9Val % 10;
  
  const elH = document.getElementById('sim9DigitH');
  const elT = document.getElementById('sim9DigitT');
  const elO = document.getElementById('sim9DigitO');
  
  elH.innerText = h;
  elT.innerText = t;
  elO.innerText = o;
  
  elH.style.boxShadow = changedCol === 'H' ? '0 0 16px #f87171' : 'none';
  elT.style.boxShadow = changedCol === 'T' ? '0 0 16px #fbbf24' : 'none';
  elO.style.boxShadow = changedCol === 'O' ? '0 0 16px #34d399' : 'none';
}

function sim9Operate(delta) {
  const prev = sim9Val;
  sim9Val = Math.max(100, Math.min(999, sim9Val + delta));
  let col = 'O';
  if (Math.abs(delta) === 10) col = 'T';
  if (Math.abs(delta) === 100) col = 'H';
  sim9UpdateDisplay(col);
  const sign = delta > 0 ? '+' : '-';
  const name = col === 'H' ? 'Hundreds' : (col === 'T' ? 'Tens' : 'Ones');
  document.getElementById('sim9Feedback').innerHTML = prev + ' ' + sign + ' ' + Math.abs(delta) + ' = <b style=\"color:#fff; font-size:17px;\">' + sim9Val + '</b>. Notice how the <b style=\"color:#fbbf24;\">' + name + '</b> digit shifted!';
}

function sim9Reset() {
  sim9Val = 454;
  sim9UpdateDisplay('');
  document.getElementById('sim9Feedback').innerHTML = 'Reset to 454. Ready for next experiment.';
}
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">🌾 Ancient Barter Trade & Double Coincidence Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Test(1)">Trade 1: Clay Pots for Wheat</button>
      <button class="sim-btn" onclick="sim10Test(2)">Trade 2: Clay Pots for Wool</button>
      <button class="sim-btn" onclick="sim10Test(3)">Trade 3: Universal Currency Trade</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Trader Boxes Comparison -->
    <div style="display:flex; gap:20px; justify-content:center; align-items:center; width:100%; max-width:540px; margin-bottom:12px;">
      <!-- Trader A -->
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); border-radius:10px; padding:10px; width:45%; text-align:center;">
        <div style="font-size:12px; color:#cbd5e1; font-weight:bold;">YOU (VILLAGE POTTER)</div>
        <div id="sim10HasA" style="font-size:14px; color:#34d399; font-weight:bold; margin-top:4px;">Has: 🏺 5 Clay Pots</div>
        <div id="sim10WantsA" style="font-size:13px; color:#fbbf24; margin-top:2px;">Wants: 🌾 2 Sacks Wheat</div>
      </div>
      <!-- Exchange Symbol -->
      <div id="sim10Symbol" style="font-size:24px; font-weight:bold; color:#f87171;">
        ⇄
      </div>
      <!-- Trader B -->
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); border-radius:10px; padding:10px; width:45%; text-align:center;">
        <div id="sim10NameB" style="font-size:12px; color:#cbd5e1; font-weight:bold;">FARMER</div>
        <div id="sim10HasB" style="font-size:14px; color:#34d399; font-weight:bold; margin-top:4px;">Has: 🌾 2 Sacks Wheat</div>
        <div id="sim10WantsB" style="font-size:13px; color:#fbbf24; margin-top:2px;">Wants: 🐑 Goat Wool</div>
      </div>
    </div>
    <!-- Result Banner -->
    <div id="sim10Feedback" style="font-size:15px; font-weight:bold; color:#f87171; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 20px; text-align:center;">
      ❌ TRADE BLOCKED: Double coincidence failed! Farmer does not need pots.
    </div>
  </div>
</div>
<script>
function sim10Test(mode) {
  document.querySelectorAll('#sim10 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(mode.toString()));
  });
  if (mode === 1) {
    document.getElementById('sim10NameB').innerText = 'FARMER';
    document.getElementById('sim10HasB').innerText = 'Has: 🌾 2 Sacks Wheat';
    document.getElementById('sim10WantsB').innerText = 'Wants: 🐑 Goat Wool';
    document.getElementById('sim10Symbol').innerHTML = '<span style=\"color:#f87171;\">✖️</span>';
    document.getElementById('sim10Feedback').innerHTML = '❌ <b style=\"color:#f87171;\">TRADE BLOCKED</b>: Double coincidence failed! The farmer has wheat but needs wool, not your clay pots.';
  } else if (mode === 2) {
    document.getElementById('sim10NameB').innerText = 'WEAVER';
    document.getElementById('sim10HasB').innerText = 'Has: 🐑 Goat Wool';
    document.getElementById('sim10WantsB').innerText = 'Wants: 🏺 Clay Pots';
    document.getElementById('sim10Symbol').innerHTML = '<span style=\"color:#34d399;\">✔️</span>';
    document.getElementById('sim10Feedback').innerHTML = '✔️ <b style=\"color:#34d399;\">BARTER SUCCESSFUL</b>: Both sides want each other\'s goods exactly!';
  } else if (mode === 3) {
    document.getElementById('sim10NameB').innerText = 'MODERN MARKETPLACE';
    document.getElementById('sim10HasB').innerText = 'Accepts: 🪙 Rupee Currency';
    document.getElementById('sim10WantsB').innerText = 'Provides: 🌾 Any Goods';
    document.getElementById('sim10Symbol').innerHTML = '<span style=\"color:#38bdf8;\">🪙</span>';
    document.getElementById('sim10Feedback').innerHTML = '🪙 <b style=\"color:#38bdf8;\">CURRENCY SOLUTION</b>: Money eliminates the need for double coincidence. Anyone can sell pots for money and buy wheat!';
  }
}
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">💵 Indian Currency Payment Box (₹10, ₹20, ₹50, ₹100)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11SetTarget(70)">Target: ₹70</button>
      <button class="sim-btn" onclick="sim11SetTarget(130)">Target: ₹130</button>
      <button class="sim-btn" onclick="sim11SetTarget(180)">Target: ₹180</button>
      <button class="sim-btn" onclick="sim11SetTarget(240)">Target: ₹240</button>
      <button class="sim-btn" style="background:#ef4444;" onclick="sim11Clear()">Clear Notes</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Available Notes Clicker -->
    <div style="display:flex; gap:10px; margin-bottom:12px;">
      <button class="sim-btn" style="background:#0284c7; padding:8px 14px;" onclick="sim11AddNote(10)">+ ₹10 Note</button>
      <button class="sim-btn" style="background:#059669; padding:8px 14px;" onclick="sim11AddNote(20)">+ ₹20 Note</button>
      <button class="sim-btn" style="background:#d97706; padding:8px 14px;" onclick="sim11AddNote(50)">+ ₹50 Note</button>
      <button class="sim-btn" style="background:#7c3aed; padding:8px 14px;" onclick="sim11AddNote(100)">+ ₹100 Note</button>
    </div>
    <!-- Payment Tray -->
    <div style="background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.2); padding:10px; width:100%; max-width:540px; min-height:60px; display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:center;" id="sim11Tray">
      <span style="color:#64748b; font-size:13px;">Click note buttons above to place cash in the payment tray...</span>
    </div>
    <!-- Current sum vs target display -->
    <div id="sim11Feedback" style="margin-top:10px; font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Current Total: ₹0 | Target: ₹70 (Need ₹70 more)
    </div>
  </div>
</div>
<script>
let sim11Target = 70;
let sim11Notes = [];

function sim11SetTarget(tgt) {
  sim11Target = tgt;
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('₹' + tgt));
  });
  sim11Clear();
}

function sim11AddNote(val) {
  sim11Notes.push(val);
  sim11Render();
}

function sim11Clear() {
  sim11Notes = [];
  sim11Render();
}

function sim11Render() {
  const tray = document.getElementById('sim11Tray');
  tray.innerHTML = '';
  if (sim11Notes.length === 0) {
    tray.innerHTML = '<span style=\"color:#64748b; font-size:13px;\">Click note buttons above to place cash in the payment tray...</span>';
  } else {
    sim11Notes.forEach(v => {
      let bg = '#0284c7';
      if (v === 20) bg = '#059669';
      if (v === 50) bg = '#d97706';
      if (v === 100) bg = '#7c3aed';
      tray.innerHTML += '<div style=\"padding:4px 10px; background:' + bg + '; border-radius:6px; color:#fff; font-weight:bold; font-size:13px; box-shadow:0 2px 6px rgba(0,0,0,0.3);\">₹' + v + '</div>';
    });
  }
  const curTotal = sim11Notes.reduce((a, b) => a + b, 0);
  const fb = document.getElementById('sim11Feedback');
  if (curTotal === sim11Target) {
    fb.innerHTML = '🎉 <b style=\"color:#34d399;\">EXACT MATCH! Total = ₹' + curTotal + ' paid successfully!</b>';
  } else if (curTotal < sim11Target) {
    fb.innerHTML = 'Current Total: <b>₹' + curTotal + '</b> | Target: <b>₹' + sim11Target + '</b> (Need ₹' + (sim11Target - curTotal) + ' more)';
  } else {
    fb.innerHTML = '⚠️ Overpaid! Current Total: <b>₹' + curTotal + '</b> | Target: <b>₹' + sim11Target + '</b> (₹' + (curTotal - sim11Target) + ' change due)';
  }
}
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🏦 High Currency Note Bundling (₹500 Equivalence)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12SetBundle(100, 5)">5 × ₹100 Notes</button>
      <button class="sim-btn" onclick="sim12SetBundle(50, 10)">10 × ₹50 Notes</button>
      <button class="sim-btn" onclick="sim12SetBundle(20, 25)">25 × ₹20 Notes</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Two Sides of Equivalence -->
    <div style="display:flex; justify-content:space-around; align-items:center; width:100%; max-width:560px; margin-bottom:12px;">
      <!-- Bundle notes tray -->
      <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.2); border-radius:10px; padding:10px; width:55%; min-height:90px; text-align:center;">
        <div id="sim12BundleTitle" style="font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:6px;">5 × ₹100 Notes</div>
        <div id="sim12NotesWrap" style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
          <!-- Injected notes -->
        </div>
      </div>
      <!-- Equals symbol -->
      <div style="font-size:28px; font-weight:bold; color:#fbbf24;">
        =
      </div>
      <!-- High note ₹500 -->
      <div style="background:linear-gradient(135deg, #475569, #334155); border:2px solid #94a3b8; border-radius:10px; width:35%; height:90px; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.4);">
        <div style="font-size:11px; color:#94a3b8; font-weight:bold;">RESERVE BANK OF INDIA</div>
        <div style="font-size:26px; color:#f8fafc; font-weight:bold;">₹500</div>
        <div style="font-size:10px; color:#cbd5e1;">ONE FIVE HUNDRED NOTE</div>
      </div>
    </div>
    <!-- Feedback Formula -->
    <div id="sim12Feedback" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 24px; text-align:center;">
      5 × ₹100 = <span style="color:#34d399;">₹500</span> (Exactly equivalent monetary value!)
    </div>
  </div>
</div>
<script>
function sim12SetBundle(denom, count) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(count + ' × ₹' + denom));
  });
  document.getElementById('sim12BundleTitle').innerText = count + ' × ₹' + denom + ' Notes';
  const wrap = document.getElementById('sim12NotesWrap');
  wrap.innerHTML = '';
  let color = '#7c3aed';
  if (denom === 50) color = '#d97706';
  if (denom === 20) color = '#059669';
  for (let i = 0; i < count; i++) {
    wrap.innerHTML += '<div style=\"background:' + color + '; border-radius:4px; padding:2px 6px; font-size:11px; font-weight:bold; color:#fff;\">₹' + denom + '</div>';
  }
  document.getElementById('sim12Feedback').innerHTML = count + ' × ₹' + denom + ' = <span style=\"color:#34d399;\">₹500</span> (Exactly equivalent monetary value!)';
}
sim12SetBundle(100, 5);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🏪 General Store Cash Register Earnings Calculator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim13Load(756, 465)">Day 1: ₹756 - ₹465</button>
      <button class="sim-btn" onclick="sim13Load(890, 520)">Day 2: ₹890 - ₹520</button>
      <button class="sim-btn" onclick="sim13Load(634, 318)">Day 3: ₹634 - ₹318</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Register Balance Breakdown -->
    <div style="background:rgba(0,0,0,0.3); border-radius:12px; border:1px solid rgba(255,255,255,0.2); padding:12px 24px; width:100%; max-width:440px; margin-bottom:12px;">
      <div style="display:flex; justify-content:space-between; padding:4px 0; border-bottom:1px solid rgba(255,255,255,0.1); font-size:14px;">
        <span style="color:#cbd5e1;">Evening Total Cash in Drawer:</span>
        <span id="sim13Evening" style="color:#38bdf8; font-weight:bold;">₹756</span>
      </div>
      <div style="display:flex; justify-content:space-between; padding:4px 0; border-bottom:2px solid #f87171; font-size:14px;">
        <span style="color:#cbd5e1;">Minus Morning Opening Float:</span>
        <span id="sim13Morning" style="color:#f87171; font-weight:bold;">- ₹465</span>
      </div>
      <div style="display:flex; justify-content:space-between; padding:6px 0; font-size:16px;">
        <span style="color:#34d399; font-weight:bold;">Today's Actual Net Sales:</span>
        <span id="sim13Profit" style="color:#34d399; font-weight:bold; font-size:18px;">= ₹291</span>
      </div>
    </div>
    <!-- Step explanation -->
    <div id="sim13Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Net Daily Takings = ₹756 - ₹465 = <span style="color:#34d399;">₹291</span>!
    </div>
  </div>
</div>
<script>
function sim13Load(eve, morn) {
  document.querySelectorAll('#sim13 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('₹' + eve + ' - ₹' + morn));
  });
  const net = eve - morn;
  document.getElementById('sim13Evening').innerText = '₹' + eve;
  document.getElementById('sim13Morning').innerText = '- ₹' + morn;
  document.getElementById('sim13Profit').innerText = '= ₹' + net;
  document.getElementById('sim13Feedback').innerHTML = 'Net Daily Takings = ₹' + eve + ' - ₹' + morn + ' = <span style=\"color:#34d399;\">₹' + net + '</span>!';
}
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🎯 Nearest Hundred Interactive Estimator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14SetVal(374)">374 → 400</button>
      <button class="sim-btn" onclick="sim14SetVal(228)">228 → 200</button>
      <button class="sim-btn" onclick="sim14SetVal(450)">450 → 500</button>
      <button class="sim-btn" onclick="sim14SetVal(185)">185 → 200</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Interactive Range Slider -->
    <div style="width:100%; max-width:520px; margin-bottom:12px;">
      <div style="display:flex; justify-content:space-between; font-size:13px; color:#cbd5e1; font-weight:bold; margin-bottom:6px;">
        <span id="sim14LowerH">Lower Hundred: 300</span>
        <span id="sim14Midpoint" style="color:#fbbf24;">Midpoint: 350</span>
        <span id="sim14UpperH">Upper Hundred: 400</span>
      </div>
      <input type="range" id="sim14Range" min="300" max="400" value="374" style="width:100%; accent-color:#38bdf8;" oninput="sim14OnSlide(this.value)">
    </div>
    <!-- Visual Display -->
    <div style="display:flex; gap:20px; align-items:center; justify-content:center; margin-bottom:10px;">
      <div style="background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.2); padding:8px 16px; text-align:center;">
        <div style="font-size:11px; color:#cbd5e1;">SELECTED NUMBER</div>
        <div id="sim14CurNum" style="font-size:24px; color:#38bdf8; font-weight:bold;">374</div>
      </div>
      <div style="font-size:24px; color:#fbbf24; font-weight:bold;">➜</div>
      <div style="background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(255,255,255,0.2); padding:8px 16px; text-align:center;">
        <div style="font-size:11px; color:#cbd5e1;">NEAREST HUNDRED</div>
        <div id="sim14Rounded" style="font-size:24px; color:#34d399; font-weight:bold;">400</div>
      </div>
    </div>
    <div id="sim14Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      374 is 74 past 300, and only 26 away from 400. Rounds UP to 400!
    </div>
  </div>
</div>
<script>
function sim14SetVal(v) {
  const lowH = Math.floor(v / 100) * 100;
  const highH = lowH + 100;
  const slider = document.getElementById('sim14Range');
  slider.min = lowH;
  slider.max = highH;
  slider.value = v;
  document.getElementById('sim14LowerH').innerText = 'Lower Hundred: ' + lowH;
  document.getElementById('sim14Midpoint').innerText = 'Midpoint: ' + (lowH + 50);
  document.getElementById('sim14UpperH').innerText = 'Upper Hundred: ' + highH;
  sim14OnSlide(v);
}

function sim14OnSlide(val) {
  val = parseInt(val);
  const lowH = Math.floor(val / 100) * 100;
  const highH = lowH + 100;
  const dLow = val - lowH;
  const dHigh = highH - val;
  const rounded = (val % 100 >= 50) ? highH : lowH;
  
  document.getElementById('sim14CurNum').innerText = val;
  document.getElementById('sim14Rounded').innerText = rounded;
  
  const fb = document.getElementById('sim14Feedback');
  if (val % 100 >= 50) {
    fb.innerHTML = val + ' has tens digit ≥ 5 (closer to ' + highH + ' by ' + dHigh + '). Rounds <b style=\"color:#34d399;\">UP to ' + highH + '</b>!';
  } else {
    fb.innerHTML = val + ' has tens digit < 5 (closer to ' + lowH + ' by ' + dLow + '). Rounds <b style=\"color:#38bdf8;\">DOWN to ' + lowH + '</b>!';
  }
}
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">⚖️ Mental Math Arithmetic Comparison Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Load(1)">Pair 1: Addition Greater</button>
      <button class="sim-btn" onclick="sim15Load(2)">Pair 2: Subtraction Smaller</button>
      <button class="sim-btn" onclick="sim15Load(3)">Pair 3: Equal Sum Balancer</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Balance Comparison Scales -->
    <div style="display:flex; justify-content:space-around; align-items:center; width:100%; max-width:540px; margin-bottom:12px;">
      <!-- Expression Left -->
      <div id="sim15BoxL" style="background:rgba(255,255,255,0.08); border:2px solid #38bdf8; border-radius:12px; padding:12px; width:40%; text-align:center;">
        <div style="font-size:12px; color:#cbd5e1; font-weight:bold;">EXPRESSION A</div>
        <div id="sim15ExprL" style="font-size:20px; color:#38bdf8; font-weight:bold; margin-top:4px;">340 + 120</div>
        <div id="sim15ValL" style="font-size:13px; color:#94a3b8; margin-top:2px;">= 460</div>
      </div>
      <!-- Comparison Sign -->
      <div id="sim15Sign" style="font-size:32px; font-weight:bold; color:#fbbf24;">
        &lt;
      </div>
      <!-- Expression Right -->
      <div id="sim15BoxR" style="background:rgba(255,255,255,0.08); border:2px solid #34d399; border-radius:12px; padding:12px; width:40%; text-align:center;">
        <div style="font-size:12px; color:#cbd5e1; font-weight:bold;">EXPRESSION B</div>
        <div id="sim15ExprR" style="font-size:20px; color:#34d399; font-weight:bold; margin-top:4px;">340 + 150</div>
        <div id="sim15ValR" style="font-size:13px; color:#94a3b8; margin-top:2px;">= 490</div>
      </div>
    </div>
    <!-- Feedback rule -->
    <div id="sim15Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:8px 20px; text-align:center;">
      Mental Rule: Both start with 340. Adding 150 adds more than adding 120, so Expression B is greater!
    </div>
  </div>
</div>
<script>
function sim15Load(pair) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(pair.toString()));
  });
  if (pair === 1) {
    document.getElementById('sim15ExprL').innerText = '340 + 120';
    document.getElementById('sim15ValL').innerText = '= 460';
    document.getElementById('sim15Sign').innerHTML = '&lt;';
    document.getElementById('sim15ExprR').innerText = '340 + 150';
    document.getElementById('sim15ValR').innerText = '= 490';
    document.getElementById('sim15Feedback').innerHTML = 'Mental Rule: Both start at 340. Adding 150 adds more than 120, so <b style=\"color:#34d399;\">340 + 150 is greater</b>!';
  } else if (pair === 2) {
    document.getElementById('sim15ExprL').innerText = '500 - 60';
    document.getElementById('sim15ValL').innerText = '= 440';
    document.getElementById('sim15Sign').innerHTML = '&gt;';
    document.getElementById('sim15ExprR').innerText = '500 - 80';
    document.getElementById('sim15ValR').innerText = '= 420';
    document.getElementById('sim15Feedback').innerHTML = 'Mental Rule: Subtracting a smaller number (60) leaves a <b style=\"color:#38bdf8;\">larger remainder</b> than subtracting 80!';
  } else if (pair === 3) {
    document.getElementById('sim15ExprL').innerText = '410 + 90';
    document.getElementById('sim15ValL').innerText = '= 500';
    document.getElementById('sim15Sign').innerHTML = '=';
    document.getElementById('sim15ExprR').innerText = '400 + 100';
    document.getElementById('sim15ValR').innerText = '= 500';
    document.getElementById('sim15Feedback').innerHTML = 'Mental Rule: 410 + 90 = 500 and 400 + 100 = 500. They are <b style=\"color:#fbbf24;\">exactly equal</b>!';
  }
}
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🧩 Digit Card Problem Puzzle Solver (Cards 0, 1, 2, 3, 4, 5)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16SetMode('max')">Max Sum: 541 + 320</button>
      <button class="sim-btn" onclick="sim16SetMode('min')">Min Sum: 104 + 235</button>
      <button class="sim-btn" onclick="sim16SetMode('diff')">Difference: 543 - 210</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Available Cards Display -->
    <div style="font-size:12px; color:#cbd5e1; font-weight:bold; margin-bottom:6px;">AVAILABLE DIGIT CARDS:</div>
    <div style="display:flex; gap:8px; margin-bottom:12px;">
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">0</div>
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">1</div>
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">2</div>
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">3</div>
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">4</div>
      <div class="sim-btn" style="background:#475569; width:34px; height:38px; display:flex; align-items:center; justify-content:center; font-size:18px;">5</div>
    </div>
    <!-- Slot Placement -->
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
      <!-- Number 1 -->
      <div id="sim16Num1" style="display:flex; gap:4px; background:rgba(0,0,0,0.3); padding:6px; border-radius:8px; border:1px solid rgba(255,255,255,0.2);">
        <span style="font-size:22px; font-weight:bold; color:#f87171;">5</span>
        <span style="font-size:22px; font-weight:bold; color:#fbbf24;">4</span>
        <span style="font-size:22px; font-weight:bold; color:#34d399;">1</span>
      </div>
      <span id="sim16Op" style="font-size:24px; font-weight:bold; color:#38bdf8;">+</span>
      <!-- Number 2 -->
      <div id="sim16Num2" style="display:flex; gap:4px; background:rgba(0,0,0,0.3); padding:6px; border-radius:8px; border:1px solid rgba(255,255,255,0.2);">
        <span style="font-size:22px; font-weight:bold; color:#f87171;">3</span>
        <span style="font-size:22px; font-weight:bold; color:#fbbf24;">2</span>
        <span style="font-size:22px; font-weight:bold; color:#34d399;">0</span>
      </div>
      <span style="font-size:24px; font-weight:bold; color:#cbd5e1;">=</span>
      <!-- Total -->
      <div id="sim16Result" style="font-size:24px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid #38bdf8; padding:4px 14px; border-radius:8px;">
        861
      </div>
    </div>
    <div id="sim16Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      Max Sum Strategy: Place largest digits (5 and 3 or 5 and 4) in the Hundreds place! 541 + 320 = 861.
    </div>
  </div>
</div>
<script>
function sim16SetMode(mode) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach(b => {
    b.classList.remove('active');
  });
  if (mode === 'max') {
    document.querySelectorAll('#sim16 .sim-controls button')[0].classList.add('active');
    document.getElementById('sim16Num1').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">5</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">4</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">1</span>';
    document.getElementById('sim16Op').innerText = '+';
    document.getElementById('sim16Num2').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">3</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">2</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">0</span>';
    document.getElementById('sim16Result').innerText = '861';
    document.getElementById('sim16Feedback').innerHTML = 'Max Sum: Place greatest digits (5 and 3 or 5 and 4) in hundreds place! 541 + 320 = <b style=\"color:#34d399;\">861</b>.';
  } else if (mode === 'min') {
    document.querySelectorAll('#sim16 .sim-controls button')[1].classList.add('active');
    document.getElementById('sim16Num1').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">1</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">0</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">4</span>';
    document.getElementById('sim16Op').innerText = '+';
    document.getElementById('sim16Num2').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">2</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">3</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">5</span>';
    document.getElementById('sim16Result').innerText = '339';
    document.getElementById('sim16Feedback').innerHTML = 'Min Sum: Place smallest non-zero digits (1 and 2) in hundreds place! 104 + 235 = <b style=\"color:#34d399;\">339</b>.';
  } else if (mode === 'diff') {
    document.querySelectorAll('#sim16 .sim-controls button')[2].classList.add('active');
    document.getElementById('sim16Num1').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">5</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">4</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">3</span>';
    document.getElementById('sim16Op').innerText = '-';
    document.getElementById('sim16Num2').innerHTML = '<span style=\"font-size:22px; font-weight:bold; color:#f87171;\">2</span><span style=\"font-size:22px; font-weight:bold; color:#fbbf24;\">1</span><span style=\"font-size:22px; font-weight:bold; color:#34d399;\">0</span>';
    document.getElementById('sim16Result').innerText = '333';
    document.getElementById('sim16Feedback').innerHTML = 'Difference Calculation: 543 - 210 = <b style=\"color:#34d399;\">333</b> using all 6 distinct cards!';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9 to 16).")
    for k in sorted(sims_part2.keys()):
        print(f"Sim {k}: length {len(sims_part2[k])} chars")

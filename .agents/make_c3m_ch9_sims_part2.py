#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Part 2: Simulators for Slides 9 to 16
"""

sims_part2 = {
    9: """
<div class="sim-container" id="sim9">
  <div class="sim-header">
    <div class="sim-title">⚖️ Visual Balance Scale Equation Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim9Target(400)">Target 400</button>
      <button class="sim-btn" onclick="sim9Target(775)">Target 775</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; max-width:620px; margin-bottom:14px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:14px; padding:16px;">
      <div style="flex:1; text-align:center; border-right:1px solid rgba(255,255,255,0.1); padding-right:12px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold; text-transform:uppercase;">Left Pan (Fixed Target)</div>
        <div id="sim9TargetVal" style="font-size:32px; font-weight:bold; color:#38bdf8; margin-top:4px;">400</div>
      </div>
      <div style="padding:0 12px; font-size:24px; font-weight:bold; color:#f59e0b;" id="sim9BalanceIcon">⚖️</div>
      <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.1); padding-left:12px;">
        <div style="font-size:12px; color:#94a3b8; font-weight:bold; text-transform:uppercase;">Right Pan (Expression)</div>
        <div id="sim9ExprVal" style="font-size:24px; font-weight:bold; color:#a7f3d0; margin-top:4px;">200 + 200</div>
      </div>
    </div>
    <div id="sim9Options" style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; max-width:620px; margin-bottom:12px;">
      <!-- Buttons dynamically populated -->
    </div>
    <div id="sim9Verdict" style="font-size:16px; font-weight:bold; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:6px 18px; text-align:center;">
      Perfect Balance! 200 + 200 = 400
    </div>
  </div>
</div>
<script>
let sim9CurrentTarget = 400;
const sim9Data = {
  400: [
    { expr: '200 + 200', val: 400, correct: true },
    { expr: '500 - 100', val: 400, correct: true },
    { expr: '350 + 50', val: 400, correct: true },
    { expr: '450 - 50', val: 400, correct: true },
    { expr: '300 + 80', val: 380, correct: false },
    { expr: '600 - 150', val: 450, correct: false }
  ],
  775: [
    { expr: '700 + 75', val: 775, correct: true },
    { expr: '800 - 25', val: 775, correct: true },
    { expr: '750 + 25', val: 775, correct: true },
    { expr: '1000 - 225', val: 775, correct: true },
    { expr: '700 + 85', val: 785, correct: false },
    { expr: '800 - 35', val: 765, correct: false }
  ]
};

function sim9Target(target) {
  sim9CurrentTarget = target;
  document.querySelectorAll('#sim9 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes('' + target));
  });
  document.getElementById('sim9TargetVal').innerText = target;

  const container = document.getElementById('sim9Options');
  container.innerHTML = '';
  sim9Data[target].forEach((item, idx) => {
    const btn = document.createElement('button');
    btn.className = 'sim-btn' + (idx === 0 ? ' active' : '');
    btn.innerText = item.expr;
    btn.onclick = () => sim9SelectExpr(item, btn);
    container.appendChild(btn);
  });
  sim9SelectExpr(sim9Data[target][0], container.firstChild);
}

function sim9SelectExpr(item, btn) {
  document.querySelectorAll('#sim9Options button').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  document.getElementById('sim9ExprVal').innerText = item.expr;
  const verdict = document.getElementById('sim9Verdict');
  const icon = document.getElementById('sim9BalanceIcon');

  if (item.val === sim9CurrentTarget) {
    icon.innerText = '⚖️ (Balanced)';
    verdict.style.color = '#34d399';
    verdict.style.background = 'rgba(16,185,129,0.15)';
    verdict.style.borderColor = '#10b981';
    verdict.innerText = '✨ Perfect Balance! ' + item.expr + ' = ' + item.val;
  } else if (item.val < sim9CurrentTarget) {
    icon.innerText = '↙️ (Right Under)';
    verdict.style.color = '#fbbf24';
    verdict.style.background = 'rgba(245,158,11,0.15)';
    verdict.style.borderColor = '#f59e0b';
    verdict.innerText = '⚠️ Unbalanced! ' + item.expr + ' = ' + item.val + ' (Too Low by ' + (sim9CurrentTarget - item.val) + ')';
  } else {
    icon.innerText = '↘️ (Right Over)';
    verdict.style.color = '#f87171';
    verdict.style.background = 'rgba(239,68,68,0.15)';
    verdict.style.borderColor = '#ef4444';
    verdict.innerText = '⚠️ Unbalanced! ' + item.expr + ' = ' + item.val + ' (Too High by ' + (item.val - sim9CurrentTarget) + ')';
  }
}
setTimeout(() => sim9Target(400), 100);
</script>
""",

    10: """
<div class="sim-container" id="sim10">
  <div class="sim-header">
    <div class="sim-title">📊 Real-World Magnitude Estimation Sorter</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim10Pick(0)">Classroom Kids</button>
      <button class="sim-btn" onclick="sim10Pick(1)">Fingers & Toes</button>
      <button class="sim-btn" onclick="sim10Pick(2)">Truck Rice Sacks</button>
      <button class="sim-btn" onclick="sim10Pick(3)">Night Sky Stars</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim10Prompt" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 20px; text-align:center;">
      Item: "Number of students in a typical school classroom"
    </div>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; width:100%; max-width:620px; margin-bottom:12px;">
      <button class="sim-btn" id="sim10Bin0" onclick="sim10Guess(0)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#60a5fa;">&lt; 10</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Single Digits</div>
      </button>
      <button class="sim-btn" id="sim10Bin1" onclick="sim10Guess(1)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#34d399;">10 – 100</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Tens Range</div>
      </button>
      <button class="sim-btn" id="sim10Bin2" onclick="sim10Guess(2)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#fbbf24;">100 – 1,000</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Hundreds Range</div>
      </button>
      <button class="sim-btn" id="sim10Bin3" onclick="sim10Guess(3)" style="padding:12px 6px; text-align:center; height:100%;">
        <div style="font-size:16px; font-weight:bold; color:#f87171;">&gt; 1,000</div>
        <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Thousands+</div>
      </button>
    </div>
    <div id="sim10Feedback" style="font-size:15px; font-weight:bold; color:#38bdf8; text-align:center;">
      Click a magnitude bin above to categorize this real-world quantity!
    </div>
  </div>
</div>
<script>
let sim10Cur = 0;
const sim10Items = [
  { name: 'Number of students in a typical school classroom', bin: 1, explanation: 'A classroom usually has 30 to 45 students, which falls between 10 and 100!' },
  { name: 'Total fingers and toes on one human person', bin: 1, explanation: 'A person has 10 fingers and 10 toes, totaling 20 (between 10 and 100)!' },
  { name: 'Sacks of grains loaded into a large cargo transport truck', bin: 2, explanation: 'A large cargo truck carries hundreds of sacks (typically 200 to 800 sacks)!' },
  { name: 'Visible stars twinkling in a clear midnight sky', bin: 3, explanation: 'Stars visible on a clear night stretch into many thousands and millions!' }
];

function sim10Pick(idx) {
  sim10Cur = idx;
  document.querySelectorAll('#sim10 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });
  document.getElementById('sim10Prompt').innerText = 'Item: "' + sim10Items[idx].name + '"';
  document.getElementById('sim10Feedback').innerText = 'Click a magnitude bin above to categorize this real-world quantity!';
  document.querySelectorAll('#sim10 [id^=sim10Bin]').forEach(b => {
    b.style.borderColor = '';
    b.style.background = '';
  });
}

function sim10Guess(binIdx) {
  const item = sim10Items[sim10Cur];
  const fb = document.getElementById('sim10Feedback');
  const clickedBtn = document.getElementById('sim10Bin' + binIdx);

  if (binIdx === item.bin) {
    clickedBtn.style.borderColor = '#10b981';
    clickedBtn.style.background = 'rgba(16,185,129,0.2)';
    fb.innerHTML = '🎉 <span style="color:#34d399;">Correct!</span> ' + item.explanation;
  } else {
    clickedBtn.style.borderColor = '#ef4444';
    clickedBtn.style.background = 'rgba(239,68,68,0.2)';
    fb.innerHTML = '❌ <span style="color:#f87171;">Try again!</span> Think about whether this is less than 10, in tens, in hundreds, or thousands.';
  }
}
setTimeout(() => sim10Pick(0), 100);
</script>
""",

    11: """
<div class="sim-container" id="sim11">
  <div class="sim-header">
    <div class="sim-title">🧩 Century & Half-Century Riddle Solver</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim11Select(1)">Century + Half</button>
      <button class="sim-btn" onclick="sim11Select(2)">Double Century - 10</button>
      <button class="sim-btn" onclick="sim11Select(3)">Triple + 25</button>
      <button class="sim-btn" onclick="sim11Select(4)">Mid 400 & 500</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim11Clue" style="font-size:16px; font-weight:bold; color:#cbd5e1; margin-bottom:8px;">
        "I am a century plus a half century. Who am I?"
      </div>
      <div id="sim11AnswerBox" style="font-size:26px; font-weight:bold; color:#38bdf8;">
        ?
      </div>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="sim-btn active" onclick="sim11Reveal()" style="padding:8px 20px;">💡 Reveal Step-by-Step Breakdown</button>
    </div>
    <div id="sim11Reasoning" style="font-size:14px; color:#a7f3d0; font-weight:600; margin-top:10px; text-align:center;">
      Click the button above to unpack the riddle's number terms!
    </div>
  </div>
</div>
<script>
let sim11Cur = 1;
const sim11Data = {
  1: { clue: '"I am a century plus a half century. Who am I?"', ans: '150', reason: 'Term Breakdown: Century = 100. Half Century = 50. Total = 100 + 50 = 150!' },
  2: { clue: '"I am double century minus 10. Who am I?"', ans: '190', reason: 'Term Breakdown: Double Century = 2 × 100 = 200. Minus 10 = 200 - 10 = 190!' },
  3: { clue: '"I am triple century plus twenty-five. Who am I?"', ans: '325', reason: 'Term Breakdown: Triple Century = 300. Add 25 = 300 + 25 = 325!' },
  4: { clue: '"I am the exact middle number between 400 and 500. Who am I?"', ans: '450', reason: 'Term Breakdown: Distance between 400 and 500 is 100. Halfway point = 400 + 50 = 450!' }
};

function sim11Select(idx) {
  sim11Cur = idx;
  document.querySelectorAll('#sim11 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(idx === 1 ? 'Century + Half' : idx === 2 ? 'Double Century' : idx === 3 ? 'Triple' : 'Mid'));
  });
  document.getElementById('sim11Clue').innerText = sim11Data[idx].clue;
  document.getElementById('sim11AnswerBox').innerText = '?';
  document.getElementById('sim11Reasoning').innerText = 'Click the button above to unpack the riddle\'s number terms!';
}

function sim11Reveal() {
  const item = sim11Data[sim11Cur];
  document.getElementById('sim11AnswerBox').innerHTML = '<span style="color:#34d399;">' + item.ans + '</span>';
  document.getElementById('sim11Reasoning').innerHTML = '🎯 ' + item.reason;
}
setTimeout(() => sim11Select(1), 100);
</script>
""",

    12: """
<div class="sim-container" id="sim12">
  <div class="sim-header">
    <div class="sim-title">🔍 Special Sequence & Pattern Detector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim12Select('stepUp')">Step-Up</button>
      <button class="sim-btn" onclick="sim12Select('stepDown')">Step-Down</button>
      <button class="sim-btn" onclick="sim12Select('triplets')">Triplets</button>
      <button class="sim-btn" onclick="sim12Select('mirrors')">Palindromes</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim12Display" style="display:flex; gap:10px; justify-content:center; max-width:620px; margin-bottom:14px; flex-wrap:wrap;">
      <!-- Populated by JS -->
    </div>
    <div id="sim12RuleCard" style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:12px 20px; width:100%; max-width:620px; text-align:center;">
      <div id="sim12RuleTitle" style="font-size:16px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">Consecutive Step-Up Pattern</div>
      <div id="sim12RuleDesc" style="font-size:13px; color:#cbd5e1;">Each consecutive digit increases by exactly 1: 2→3→4, 3→4→5, 4→5→6!</div>
    </div>
  </div>
</div>
<script>
const sim12Patterns = {
  stepUp: {
    title: 'Consecutive Step-Up Pattern',
    desc: 'Each digit steps up by 1 (+1 each place): 234, 345, 456, 567, 678!',
    nums: ['234', '345', '456', '567', '678']
  },
  stepDown: {
    title: 'Consecutive Step-Down Pattern',
    desc: 'Each digit steps down by 1 (-1 each place): 765, 654, 543, 432, 321!',
    nums: ['765', '654', '543', '432', '321']
  },
  triplets: {
    title: 'Repeating Identical Triplet Digits',
    desc: 'All three digits (Hundreds, Tens, Ones) are completely identical!',
    nums: ['111', '222', '333', '444', '555']
  },
  mirrors: {
    title: 'Mirrored Palindromic Numbers',
    desc: 'The number reads exactly the same forwards and backwards! (First digit = Last digit)',
    nums: ['121', '343', '565', '787', '909']
  }
};

function sim12Select(key) {
  document.querySelectorAll('#sim12 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.onclick.toString().includes(key));
  });

  const pat = sim12Patterns[key];
  document.getElementById('sim12RuleTitle').innerText = pat.title;
  document.getElementById('sim12RuleDesc').innerText = pat.desc;

  const disp = document.getElementById('sim12Display');
  disp.innerHTML = '';
  pat.nums.forEach(num => {
    const card = document.createElement('div');
    card.style.background = 'rgba(59,130,246,0.15)';
    card.style.border = '1px solid #3b82f6';
    card.style.borderRadius = '10px';
    card.style.padding = '10px 18px';
    card.style.fontSize = '22px';
    card.style.fontWeight = 'bold';
    card.style.color = '#fff';
    card.innerText = num;
    disp.appendChild(card);
  });
}
setTimeout(() => sim12Select('stepUp'), 100);
</script>
""",

    13: """
<div class="sim-container" id="sim13">
  <div class="sim-header">
    <div class="sim-title">🎟️ 6 Place Value Slips Number Maker</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim13Preset('max')">Max (600)</button>
      <button class="sim-btn" onclick="sim13Preset('min')">Min (6)</button>
      <button class="sim-btn" onclick="sim13Preset('target321')">Make 321</button>
      <button class="sim-btn" onclick="sim13Reset()">Reset Slips</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#94a3b8; font-weight:bold; margin-bottom:10px;">
      Total Available Slips: <span id="sim13Remaining" style="color:#fbbf24; font-size:16px;">6 / 6 Available</span>
    </div>
    <div style="display:flex; justify-content:center; gap:16px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- Hundreds Slip Column -->
      <div style="flex:1; background:rgba(59,130,246,0.12); border:1px solid #3b82f6; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#60a5fa;">[100] Slips</div>
        <div id="sim13CountH" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('H', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('H', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValH" style="font-size:11px; color:#93c5fd; margin-top:4px;">0 Units</div>
      </div>
      <!-- Tens Slip Column -->
      <div style="flex:1; background:rgba(245,158,11,0.12); border:1px solid #f59e0b; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#fbbf24;">[10] Slips</div>
        <div id="sim13CountT" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('T', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('T', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValT" style="font-size:11px; color:#fde68a; margin-top:4px;">0 Units</div>
      </div>
      <!-- Ones Slip Column -->
      <div style="flex:1; background:rgba(16,185,129,0.12); border:1px solid #10b981; border-radius:12px; padding:10px; text-align:center;">
        <div style="font-size:12px; font-weight:bold; color:#34d399;">[1] Slips</div>
        <div id="sim13CountO" style="font-size:24px; font-weight:bold; color:#fff; margin:6px 0;">0</div>
        <div style="display:flex; justify-content:center; gap:6px;">
          <button class="sim-btn" onclick="sim13Mod('O', -1)" style="padding:2px 10px;">-</button>
          <button class="sim-btn" onclick="sim13Mod('O', 1)" style="padding:2px 10px;">+</button>
        </div>
        <div id="sim13ValO" style="font-size:11px; color:#a7f3d0; margin-top:4px;">0 Units</div>
      </div>
    </div>
    <div id="sim13TotalBox" style="font-size:20px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Constructed Number: 0
    </div>
  </div>
</div>
<script>
let sim13Counts = { H: 0, T: 0, O: 0 };
const sim13MaxSlips = 6;

function sim13Update() {
  const used = sim13Counts.H + sim13Counts.T + sim13Counts.O;
  const rem = sim13MaxSlips - used;
  document.getElementById('sim13Remaining').innerText = rem + ' / ' + sim13MaxSlips + ' Available';

  document.getElementById('sim13CountH').innerText = sim13Counts.H;
  document.getElementById('sim13ValH').innerText = (sim13Counts.H * 100) + ' Units';

  document.getElementById('sim13CountT').innerText = sim13Counts.T;
  document.getElementById('sim13ValT').innerText = (sim13Counts.T * 10) + ' Units';

  document.getElementById('sim13CountO').innerText = sim13Counts.O;
  document.getElementById('sim13ValO').innerText = sim13Counts.O + ' Units';

  const sum = sim13Counts.H * 100 + sim13Counts.T * 10 + sim13Counts.O;
  document.getElementById('sim13TotalBox').innerHTML = 'Constructed Total: <span style="color:#fbbf24;">' + sum + '</span> (' + used + ' slips used)';
}

function sim13Mod(type, delta) {
  const used = sim13Counts.H + sim13Counts.T + sim13Counts.O;
  if (delta > 0 && used >= sim13MaxSlips) return;
  if (delta < 0 && sim13Counts[type] <= 0) return;
  sim13Counts[type] += delta;
  sim13Update();
}

function sim13Preset(type) {
  if (type === 'max') {
    sim13Counts = { H: 6, T: 0, O: 0 };
  } else if (type === 'min') {
    sim13Counts = { H: 0, T: 0, O: 6 };
  } else if (type === 'target321') {
    sim13Counts = { H: 3, T: 2, O: 1 };
  }
  sim13Update();
}

function sim13Reset() {
  sim13Counts = { H: 0, T: 0, O: 0 };
  sim13Update();
}
setTimeout(() => sim13Preset('target321'), 100);
</script>
""",

    14: """
<div class="sim-container" id="sim14">
  <div class="sim-header">
    <div class="sim-title">🔢 Digit Combination & Permutation Explorer (Digits 3 & 8)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim14Mode(2)">2-Digit Permutations</button>
      <button class="sim-btn" onclick="sim14Mode(3)">3-Digit Permutations</button>
      <button class="sim-btn" onclick="sim14Sort()">Toggle Sort Order</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div id="sim14Summary" style="font-size:14px; color:#cbd5e1; font-weight:bold; margin-bottom:12px; text-align:center;">
      Showing all combinations using digits 3 and 8:
    </div>
    <div id="sim14Cards" style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center; max-width:620px; margin-bottom:14px;">
      <!-- Injected by JS -->
    </div>
    <div id="sim14MinMax" style="font-size:16px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:8px 24px; text-align:center;">
      Smallest: 33 | Largest: 88
    </div>
  </div>
</div>
<script>
let sim14Digits = 2;
let sim14Asc = true;
const sim14Data = {
  2: [33, 38, 83, 88],
  3: [333, 338, 383, 388, 833, 838, 883, 888]
};

function sim14Mode(digits) {
  sim14Digits = digits;
  document.querySelectorAll('#sim14 .sim-controls button').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(digits + '-Digit'));
  });
  sim14Render();
}

function sim14Sort() {
  sim14Asc = !sim14Asc;
  sim14Render();
}

function sim14Render() {
  const list = [...sim14Data[sim14Digits]];
  list.sort((a, b) => sim14Asc ? a - b : b - a);

  document.getElementById('sim14Summary').innerText = 'Showing ' + list.length + ' distinct ' + sim14Digits + '-digit combinations (Ordered ' + (sim14Asc ? 'Ascending' : 'Descending') + '):';

  const cardsContainer = document.getElementById('sim14Cards');
  cardsContainer.innerHTML = '';
  list.forEach(num => {
    const d = document.createElement('div');
    d.style.background = 'rgba(245,158,11,0.15)';
    d.style.border = '1px solid #f59e0b';
    d.style.borderRadius = '10px';
    d.style.padding = '8px 16px';
    d.style.fontSize = '20px';
    d.style.fontWeight = 'bold';
    d.style.color = '#fff';
    d.innerText = num;
    cardsContainer.appendChild(d);
  });

  const min = Math.min(...list);
  const max = Math.max(...list);
  document.getElementById('sim14MinMax').innerHTML = 'Smallest: <span style="color:#34d399;">' + min + '</span> | Largest: <span style="color:#f87171;">' + max + '</span>';
}
setTimeout(() => sim14Mode(2), 100);
</script>
""",

    15: """
<div class="sim-container" id="sim15">
  <div class="sim-header">
    <div class="sim-title">📜 Bhutasankhya Cultural Symbol Decoder</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim15Select(0)">Moon (1)</button>
      <button class="sim-btn" onclick="sim15Select(1)">Eyes (2)</button>
      <button class="sim-btn" onclick="sim15Select(2)">Times (3)</button>
      <button class="sim-btn" onclick="sim15Select(3)">Directions (4)</button>
      <button class="sim-btn" onclick="sim15Select(4)">Hand/Palm (5)</button>
      <button class="sim-btn" onclick="sim15Select(5)">Notes (7)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.15); max-width:620px; width:100%; text-align:center; margin-bottom:12px;">
      <div id="sim15Icon" style="font-size:40px; margin-bottom:6px;">🌙</div>
      <div id="sim15Sanskrit" style="font-size:22px; font-weight:bold; color:#fbbf24; margin-bottom:4px;">Chandra / Shashi (Moon)</div>
      <div id="sim15Digit" style="font-size:32px; font-weight:bold; color:#38bdf8; margin-bottom:6px;">Numeral: 1</div>
      <div id="sim15Meaning" style="font-size:13px; color:#cbd5e1; line-height:1.5;">
        Represents 1 because in our observable natural world, there is exactly one moon orbiting Earth!
      </div>
    </div>
    <div style="font-size:12px; color:#94a3b8; font-style:italic;">
      Ancient Indian mathematicians used poetry & nature words to record numbers effortlessly in verse!
    </div>
  </div>
</div>
<script>
const sim15Symbols = [
  { icon: '🌙', name: 'Chandra / Shashi (Moon)', num: 1, desc: 'Represents 1 because in our natural world, there is only one moon orbiting Earth!' },
  { icon: '👀', name: 'Netra / Lochana (Eyes)', num: 2, desc: 'Represents 2 because humans and animals see through a pair of two eyes!' },
  { icon: '⏳', name: 'Trikala (Three Times)', num: 3, desc: 'Represents 3 because time flows through three states: Past, Present, and Future!' },
  { icon: '🧭', name: 'Disha (Cardinal Directions)', num: 4, desc: 'Represents 4 because geography is framed by four directions: North, South, East, West!' },
  { icon: '✋', name: 'Pani / Kara (Palm Fingers)', num: 5, desc: 'Represents 5 because a single human hand holds five fingers!' },
  { icon: '🎵', name: 'Saptasvara (Musical Notes)', num: 7, desc: 'Represents 7 because classical Indian music is built on seven sacred notes: Sa, Re, Ga, Ma, Pa, Dha, Ni!' }
];

function sim15Select(idx) {
  document.querySelectorAll('#sim15 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });

  const item = sim15Symbols[idx];
  document.getElementById('sim15Icon').innerText = item.icon;
  document.getElementById('sim15Sanskrit').innerText = item.name;
  document.getElementById('sim15Digit').innerText = 'Numeral: ' + item.num;
  document.getElementById('sim15Meaning').innerText = item.desc;
}
setTimeout(() => sim15Select(0), 100);
</script>
""",

    16: """
<div class="sim-container" id="sim16">
  <div class="sim-header">
    <div class="sim-title">🔄 Right-to-Left Word Numeral Decoder (*Ankanam Vamato Gatih*)</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim16Preset(0)">Netra-Agni-Shashi</button>
      <button class="sim-btn" onclick="sim16Preset(1)">Kha-Bana-Chandra</button>
      <button class="sim-btn" onclick="sim16Preset(2)">Veda-Netra-Ritu</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
    <div style="font-size:13px; color:#fbbf24; font-weight:bold; margin-bottom:8px;">
      Rule: 'Ankanam Vamato Gatih' (Words are spoken left-to-right, but digits fill Units → Tens → Hundreds!)
    </div>
    <!-- Card sequence container -->
    <div id="sim16Cards" style="display:flex; justify-content:center; gap:12px; width:100%; max-width:620px; margin-bottom:14px;">
      <!-- Injected by JS -->
    </div>
    <!-- Final decoded standard number -->
    <div id="sim16Decoded" style="font-size:22px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:10px 24px; text-align:center;">
      Decoded Number: 132
    </div>
  </div>
</div>
<script>
const sim16Data = [
  {
    name: 'Netra-Agni-Shashi',
    cards: [
      { word: 'Netra (Eyes)', digit: 2, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Agni (Fires)', digit: 3, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Shashi (Moon)', digit: 1, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 132
  },
  {
    name: 'Kha-Bana-Chandra',
    cards: [
      { word: 'Kha (Void/Sky)', digit: 0, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Bana (Arrows)', digit: 5, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Chandra (Moon)', digit: 1, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 150
  },
  {
    name: 'Veda-Netra-Ritu',
    cards: [
      { word: 'Veda (Vedas)', digit: 4, place: 'Units (Ones)', color: '#10b981' },
      { word: 'Netra (Eyes)', digit: 2, place: 'Tens (×10)', color: '#f59e0b' },
      { word: 'Ritu (Seasons)', digit: 6, place: 'Hundreds (×100)', color: '#3b82f6' }
    ],
    num: 624
  }
];

function sim16Preset(idx) {
  document.querySelectorAll('#sim16 .sim-controls button').forEach((b, i) => {
    b.classList.toggle('active', i === idx);
  });

  const item = sim16Data[idx];
  const container = document.getElementById('sim16Cards');
  container.innerHTML = '';

  item.cards.forEach((card, i) => {
    const col = document.createElement('div');
    col.style.flex = '1';
    col.style.background = 'rgba(255,255,255,0.05)';
    col.style.border = '1px solid ' + card.color;
    col.style.borderRadius = '12px';
    col.style.padding = '10px';
    col.style.textAlign = 'center';

    col.innerHTML = `
      <div style="font-size:11px; color:#94a3b8; font-weight:bold;">Word ${i + 1}</div>
      <div style="font-size:14px; font-weight:bold; color:${card.color}; margin:4px 0;">${card.word}</div>
      <div style="font-size:24px; font-weight:bold; color:#fff;">${card.digit}</div>
      <div style="font-size:11px; color:#cbd5e1; margin-top:4px;">➡️ Fills ${card.place}</div>
    `;
    container.appendChild(col);
  });

  document.getElementById('sim16Decoded').innerHTML = 'Decoded 3-Digit Numeral: <span style="color:#fbbf24; font-size:26px;">' + item.num + '</span> <span style="font-size:14px; color:#94a3b8;">(' + item.cards[2].digit + '00 + ' + item.cards[1].digit + '0 + ' + item.cards[0].digit + ')</span>';
}
setTimeout(() => sim16Preset(0), 100);
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Slides 9-16.")
    for k in sorted(sims_part2.keys()):
        print(f"  Slide {k}: {len(sims_part2[k])} chars")

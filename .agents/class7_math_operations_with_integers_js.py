# -*- coding: utf-8 -*-
SIMULATORS_JS = r"""
    // ==========================================
    // CHAPTER 10: OPERATIONS WITH INTEGERS JS ENGINES
    // ==========================================

    // --- Simulator 1: Integer Puzzle ---
    let currentPuzzleTarget = { val: -5, type: 'sum' };

    function updateIntegerPuzzle() {
      const a = parseInt(document.getElementById('puzzleSliderA')?.value || 3);
      const b = parseInt(document.getElementById('puzzleSliderB')?.value || -8);

      const valA = document.getElementById('puzzleValA');
      const valB = document.getElementById('puzzleValB');
      if (valA) valA.textContent = a > 0 ? `+${a}` : `${a}`;
      if (valB) valB.textContent = b > 0 ? `+${b}` : `${b}`;

      const sum = a + b;
      const diff = a - b;

      const sumExpr = document.getElementById('puzzleSumExpr');
      const sumRes = document.getElementById('puzzleSumResult');
      const diffExpr = document.getElementById('puzzleDiffExpr');
      const diffRes = document.getElementById('puzzleDiffResult');

      if (sumExpr) sumExpr.textContent = `${a} + (${b})`;
      if (sumRes) {
        sumRes.textContent = sum > 0 ? `+${sum}` : `${sum}`;
        sumRes.className = sum === currentPuzzleTarget.val && currentPuzzleTarget.type === 'sum' ?
          'text-2xl font-extrabold text-emerald-400 font-mono animate-pulse' :
          'text-xl font-extrabold text-amber-400 font-mono';
      }

      if (diffExpr) diffExpr.textContent = `${a} - (${b})`;
      if (diffRes) {
        diffRes.textContent = diff > 0 ? `+${diff}` : `${diff}`;
        diffRes.className = diff === currentPuzzleTarget.val && currentPuzzleTarget.type === 'diff' ?
          'text-2xl font-extrabold text-emerald-400 font-mono animate-pulse' :
          'text-xl font-extrabold text-emerald-400 font-mono';
      }

      const feedback = document.getElementById('puzzleFeedback');
      if (feedback) {
        if (currentPuzzleTarget.type === 'sum' && sum === currentPuzzleTarget.val) {
          feedback.textContent = `🎯 Target Matched! ${a} + (${b}) = ${sum}!`;
          feedback.className = 'text-xs font-bold text-emerald-400 mt-1';
        } else if (currentPuzzleTarget.type === 'diff' && diff === currentPuzzleTarget.val) {
          feedback.textContent = `🎯 Target Matched! ${a} - (${b}) = ${diff}!`;
          feedback.className = 'text-xs font-bold text-emerald-400 mt-1';
        } else {
          feedback.textContent = `Current target: ${currentPuzzleTarget.type.toUpperCase()} = ${currentPuzzleTarget.val}. Adjust sliders to match!`;
          feedback.className = 'text-xs font-semibold text-slate-400 mt-1';
        }
      }
    }
    window.updateIntegerPuzzle = updateIntegerPuzzle;

    function setPuzzleTarget(val, type) {
      sfx.playClick();
      currentPuzzleTarget = { val, type };
      updateIntegerPuzzle();
    }
    window.setPuzzleTarget = setPuzzleTarget;


    // --- Simulator 2: Carrom Number Line ---
    let carromPos = 0;

    function renderCarromTrack() {
      const g = document.getElementById('carromTicksGroup');
      if (!g) return;
      g.innerHTML = '';

      for (let i = -10; i <= 10; i++) {
        const x = i * 28; // spacing 28px per unit
        const isOrigin = (i === 0);
        const tickHeight = isOrigin ? 20 : 12;

        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x);
        line.setAttribute('y1', -tickHeight / 2);
        line.setAttribute('x2', x);
        line.setAttribute('y2', tickHeight / 2);
        line.setAttribute('stroke', isOrigin ? '#f59e0b' : '#64748b');
        line.setAttribute('stroke-width', isOrigin ? '2.5' : '1.5');
        g.appendChild(line);

        const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txt.setAttribute('x', x);
        txt.setAttribute('y', 26);
        txt.setAttribute('text-anchor', 'middle');
        txt.setAttribute('font-size', isOrigin ? '11' : '9');
        txt.setAttribute('font-weight', isOrigin ? 'bold' : 'normal');
        txt.setAttribute('fill', isOrigin ? '#fbbf24' : '#94a3b8');
        txt.setAttribute('font-family', 'monospace');
        txt.textContent = i > 0 ? `+${i}` : `${i}`;
        g.appendChild(txt);
      }
      updateCarromView();
    }
    window.renderCarromTrack = renderCarromTrack;

    function updateCarromView() {
      const puck = document.getElementById('carromPuck');
      const posText = document.getElementById('coinPosText');
      const puckText = document.getElementById('puckText');

      const x = carromPos * 28;
      if (puck) puck.setAttribute('transform', `translate(${x}, 0)`);
      if (posText) posText.textContent = carromPos > 0 ? `+${carromPos}` : `${carromPos}`;
      if (puckText) puckText.textContent = carromPos;
    }

    function strikeCarrom(delta) {
      sfx.playClick();
      const oldPos = carromPos;
      carromPos = Math.max(-10, Math.min(10, carromPos + delta));

      const traj = document.getElementById('coinTrajectory');
      if (traj) {
        const x1 = oldPos * 28;
        const x2 = carromPos * 28;
        const midX = (x1 + x2) / 2;
        const arcY = delta > 0 ? -35 : -35;
        traj.setAttribute('d', `M ${x1},0 Q ${midX},${arcY} ${x2},0`);
      }

      const msg = document.getElementById('carromActionMsg');
      if (msg) {
        msg.textContent = `Strike: ${oldPos} + (${delta > 0 ? '+' + delta : delta}) = ${carromPos}!`;
      }
      updateCarromView();
    }
    window.strikeCarrom = strikeCarrom;

    function resetCarrom() {
      sfx.playClick();
      carromPos = 0;
      const traj = document.getElementById('coinTrajectory');
      if (traj) traj.setAttribute('d', '');
      const msg = document.getElementById('carromActionMsg');
      if (msg) msg.textContent = 'Puck resting at Origin (0). Click a strike vector!';
      updateCarromView();
    }
    window.resetCarrom = resetCarrom;


    // --- Simulator 3: Zero Pair Tokens ---
    let tokensList = [1, 1, 1, -1, -1];

    function renderTokens() {
      const grid = document.getElementById('tokenGrid');
      if (!grid) return;
      grid.innerHTML = '';

      let greenCount = 0;
      let redCount = 0;

      tokensList.forEach((val, idx) => {
        if (val === 1) greenCount++;
        else redCount++;

        const token = document.createElement('div');
        token.className = val === 1 ?
          'w-9 h-9 rounded-full bg-emerald-500 border-2 border-emerald-300 flex items-center justify-center font-bold text-black text-sm shadow cursor-pointer transition-transform hover:scale-110' :
          'w-9 h-9 rounded-full bg-rose-500 border-2 border-rose-300 flex items-center justify-center font-bold text-white text-sm shadow cursor-pointer transition-transform hover:scale-110';
        token.textContent = val === 1 ? '+1' : '-1';
        token.title = 'Click to remove token';
        token.onclick = () => {
          sfx.playClick();
          tokensList.splice(idx, 1);
          renderTokens();
        };
        grid.appendChild(token);
      });

      const net = greenCount - redCount;
      const netSpan = document.getElementById('tokenNetVal');
      if (netSpan) {
        netSpan.textContent = net > 0 ? `+${net}` : `${net}`;
        netSpan.className = net >= 0 ? 'text-emerald-400 text-sm font-mono font-extrabold' : 'text-rose-400 text-sm font-mono font-extrabold';
      }

      const cg = document.getElementById('countGreen');
      const cr = document.getElementById('countRed');
      const cz = document.getElementById('countZeroPairs');
      if (cg) cg.textContent = greenCount;
      if (cr) cr.textContent = redCount;
      if (cz) cz.textContent = Math.min(greenCount, redCount);
    }
    window.renderTokens = renderTokens;

    function addToken(val) {
      sfx.playClick();
      tokensList.push(val);
      renderTokens();
    }
    window.addToken = addToken;

    function annihilateZeroPairs() {
      sfx.playChime();
      let greens = tokensList.filter(t => t === 1);
      let reds = tokensList.filter(t => t === -1);

      const pairs = Math.min(greens.length, reds.length);
      greens.splice(0, pairs);
      reds.splice(0, pairs);

      tokensList = [...greens, ...reds];
      renderTokens();
    }
    window.annihilateZeroPairs = annihilateZeroPairs;

    function resetTokens() {
      sfx.playClick();
      tokensList = [];
      renderTokens();
    }
    window.resetTokens = resetTokens;


    // --- Simulator 4: Subtraction Transformer ---
    function setSubCase(a, b) {
      sfx.playClick();
      const orig = document.getElementById('subOrigExpr');
      const inv = document.getElementById('subInvExpr');
      const stepBox = document.getElementById('subStepBox');

      const invB = -b;
      const result = a - b;

      if (orig) orig.textContent = `(${a > 0 ? '+' + a : a}) - (${b > 0 ? '+' + b : b})`;
      if (inv) inv.textContent = `(${a > 0 ? '+' + a : a}) + (${invB > 0 ? '+' + invB : invB}) = ${result > 0 ? '+' + result : result}`;

      if (stepBox) {
        stepBox.innerHTML = `
          <div class="text-amber-300 font-bold mb-1">Step-by-Step Derivation:</div>
          <div>1. Subtracting <strong>${b > 0 ? '+' + b : b}</strong> is identical to adding its Additive Inverse: <strong>${invB > 0 ? '+' + invB : invB}</strong>.</div>
          <div>2. Calculation: ${a} + (${invB}) = <strong>${result}</strong>.</div>
          <div class="text-emerald-400 mt-1">✓ Concrete Token Insight: Removing ${Math.abs(b)} ${b > 0 ? 'green (+1)' : 'red (-1)'} tokens leaves exactly ${result} net tokens!</div>
        `;
      }
    }
    window.setSubCase = setSubCase;


    // --- Simulator 5: Pos Times Neg ---
    function updatePosTimesNeg() {
      const groups = parseInt(document.getElementById('ptnSliderGroups')?.value || 3);
      const size = parseInt(document.getElementById('ptnSliderSize')?.value || 4);

      const gVal = document.getElementById('ptnGroupsVal');
      const sVal = document.getElementById('ptnSizeVal');
      if (gVal) gVal.textContent = groups;
      if (sVal) sVal.textContent = `-${size}`;

      const total = groups * (-size);
      const expr = document.getElementById('ptnExpr');
      if (expr) expr.textContent = `${groups} × (-${size}) = ${total}`;

      const tray = document.getElementById('ptnTray');
      if (tray) {
        tray.innerHTML = '';
        for (let g = 1; g <= groups; g++) {
          const groupDiv = document.createElement('div');
          groupDiv.className = 'p-2 rounded bg-rose-950/40 border border-rose-500/40 flex flex-col items-center gap-1.5';
          groupDiv.innerHTML = `<span class="text-[10px] text-rose-300 font-bold">Group ${g} (-${size})</span>`;

          const tokensDiv = document.createElement('div');
          tokensDiv.className = 'flex gap-1';
          for (let s = 1; s <= size; s++) {
            tokensDiv.innerHTML += `<span class="w-5 h-5 rounded-full bg-rose-500 text-white font-bold text-[10px] flex items-center justify-center">-</span>`;
          }
          groupDiv.appendChild(tokensDiv);
          tray.appendChild(groupDiv);
        }
      }

      const sum = document.getElementById('ptnSummary');
      if (sum) {
        const terms = Array(groups).fill(`(-${size})`).join(' + ');
        sum.textContent = `${groups} groups of (-${size}) = ${terms} = ${total} tokens!`;
      }
    }
    window.updatePosTimesNeg = updatePosTimesNeg;


    // --- Simulator 6: Neg Times Pos ---
    let ntpStage = 0;

    function stepNtpRemoval() {
      sfx.playClick();
      const grid = document.getElementById('ntpBankGrid');
      const title = document.getElementById('ntpBankTitle');
      const desc = document.getElementById('ntpExplanation');
      const btn = document.getElementById('btnNtpStep');

      if (ntpStage === 0) {
        // Step 1: Put 12 Zero Pairs
        ntpStage = 1;
        if (title) title.textContent = 'Bank State: 12 Zero Pairs (Net Value = 0)';
        if (grid) {
          grid.innerHTML = '';
          for (let i = 0; i < 12; i++) {
            grid.innerHTML += `
              <div class="zero-pair-chip p-1 rounded bg-slate-900 border border-slate-700 flex items-center gap-1" id="ntpPair_${i}">
                <span class="w-5 h-5 rounded-full bg-emerald-500 text-black font-bold text-[10px] flex items-center justify-center">+</span>
                <span class="w-5 h-5 rounded-full bg-rose-500 text-white font-bold text-[10px] flex items-center justify-center">-</span>
              </div>
            `;
          }
        }
        if (btn) btn.textContent = '2. Remove 3 Groups of (+4) Positive Tokens';
        if (desc) desc.textContent = 'Neutral bank initialized with 12 zero pairs. Total net value is exactly 0. Now, click step 2 to remove 3 groups of (+4) green tokens!';
      } else if (ntpStage === 1) {
        // Step 2: Extract positive tokens
        ntpStage = 2;
        sfx.playChime();
        if (title) title.textContent = 'Bank State: 12 Red Tokens Remain (Net Value = -12)';
        if (grid) {
          grid.innerHTML = '';
          for (let i = 0; i < 12; i++) {
            grid.innerHTML += `
              <div class="p-1 rounded bg-rose-950/60 border border-rose-500/40 flex items-center justify-center animate-bounce">
                <span class="w-6 h-6 rounded-full bg-rose-500 text-white font-bold text-xs flex items-center justify-center">-</span>
              </div>
            `;
          }
        }
        if (btn) btn.textContent = 'Completed (Result: -12)';
        if (desc) desc.textContent = '✓ All 12 green positive tokens were extracted! Only 12 red debt tokens remain. Net value = -12! Thus (-3) × (+4) = -12.';
      }
    }
    window.stepNtpRemoval = stepNtpRemoval;

    function resetNtp() {
      sfx.playClick();
      ntpStage = 0;
      const grid = document.getElementById('ntpBankGrid');
      const title = document.getElementById('ntpBankTitle');
      const desc = document.getElementById('ntpExplanation');
      const btn = document.getElementById('btnNtpStep');

      if (grid) grid.innerHTML = '';
      if (title) title.textContent = 'Bank State: Empty (0)';
      if (btn) btn.textContent = '1. Populate Neutral Bank (12 Zero Pairs)';
      if (desc) desc.textContent = "Click 'Populate Neutral Bank' to create 12 zero pairs with net value 0.";
    }
    window.resetNtp = resetNtp;


    // --- Simulator 7: Neg Times Neg ---
    let ntnStage = 0;

    function stepNtnSimulation() {
      sfx.playClick();
      const grid = document.getElementById('ntnBankGrid');
      const status = document.getElementById('ntnBankStatus');
      const desc = document.getElementById('ntnDesc');
      const btn = document.getElementById('btnNtnAction');

      if (ntnStage === 0) {
        ntnStage = 1;
        if (status) status.textContent = 'Bank Value: 12 Zero Pairs (Net Value = 0)';
        if (grid) {
          grid.innerHTML = '';
          for (let i = 0; i < 12; i++) {
            grid.innerHTML += `
              <div class="p-1 rounded bg-slate-900 border border-slate-700 flex items-center gap-1" id="ntnPair_${i}">
                <span class="w-5 h-5 rounded-full bg-emerald-500 text-black font-bold text-[10px] flex items-center justify-center">+</span>
                <span class="w-5 h-5 rounded-full bg-rose-500 text-white font-bold text-[10px] flex items-center justify-center">-</span>
              </div>
            `;
          }
        }
        if (btn) btn.textContent = '2. Remove 3 Debts of (-4) Red Tokens';
        if (desc) desc.textContent = '12 Zero pairs placed (net 0). Click step 2 to remove 3 groups of (-4) red debt tokens!';
      } else if (ntnStage === 1) {
        ntnStage = 2;
        sfx.playChime();
        if (status) status.textContent = 'Bank Value: 12 Green Tokens (Net Value = +12)!';
        if (grid) {
          grid.innerHTML = '';
          for (let i = 0; i < 12; i++) {
            grid.innerHTML += `
              <div class="p-1 rounded bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-center animate-pulse">
                <span class="w-6 h-6 rounded-full bg-emerald-500 text-black font-bold text-xs flex items-center justify-center">+</span>
              </div>
            `;
          }
        }
        if (btn) btn.textContent = 'Completed (Result: +12)';
        if (desc) desc.textContent = '✨ Removing the debts (red tokens) left pure positive wealth (green tokens)! Thus (-3) × (-4) = +12!';
      }
    }
    window.stepNtnSimulation = stepNtnSimulation;

    function resetNtn() {
      sfx.playClick();
      ntnStage = 0;
      const grid = document.getElementById('ntnBankGrid');
      const status = document.getElementById('ntnBankStatus');
      const desc = document.getElementById('ntnDesc');
      const btn = document.getElementById('btnNtnAction');

      if (grid) grid.innerHTML = '';
      if (status) status.textContent = 'Bank Value: 0';
      if (btn) btn.textContent = '1. Place 12 Zero Pairs (Net Value 0)';
      if (desc) desc.textContent = 'Click step 1 to place 12 zero pairs (12 green +, 12 red -). Net value is exactly 0.';
    }
    window.resetNtn = resetNtn;


    // --- Simulator 8: Multiplication Patterns ---
    let currentMultiplicand = -3;

    function setPatternMultiplicand(m) {
      sfx.playClick();
      currentMultiplicand = m;
      const fixVal = document.getElementById('mpFixedVal');
      if (fixVal) fixVal.textContent = m;

      const container = document.getElementById('patternRowsContainer');
      if (!container) return;
      container.innerHTML = '';

      const stepDiff = Math.abs(m);

      for (let k = 4; k >= -4; k--) {
        const prod = k * m;
        const row = document.createElement('div');
        row.className = k === 0 ?
          'flex justify-between items-center p-1 rounded bg-amber-950/40 border border-amber-500/40 text-amber-300 font-bold' :
          (k < 0 ?
            'flex justify-between items-center p-1 rounded bg-emerald-950/30 border border-emerald-500/30 text-emerald-300 font-bold' :
            'flex justify-between items-center p-1 rounded bg-slate-900 border border-slate-800 text-slate-300');

        row.innerHTML = `
          <span>${k >= 0 ? '+' + k : k} × (${m}) = ${prod > 0 ? '+' + prod : prod}</span>
          <span class="text-[10px] text-sky-400 font-semibold">(steps by +${stepDiff})</span>
        `;
        container.appendChild(row);
      }
    }
    window.setPatternMultiplicand = setPatternMultiplicand;


    // --- Simulator 9: Sign Matrix ---
    function selectSignQuad(quad) {
      sfx.playClick();
      const res = document.getElementById('signTestResult');
      if (!res) return;

      switch(quad) {
        case 'pp':
          res.innerHTML = '<strong>(+) × (+) = (+)</strong>: Like positive signs preserve positive direction.';
          break;
        case 'pn':
          res.innerHTML = '<strong>(+) × (-) = (-)</strong>: Adding groups of negative debt yields negative.';
          break;
        case 'np':
          res.innerHTML = '<strong>(-) × (+) = (-)</strong>: Removing groups of positive assets leaves negative.';
          break;
        case 'nn':
          res.innerHTML = '<strong>(-) × (-) = (+)</strong>: Removing negative debts produces positive net worth!';
          break;
      }
    }
    window.selectSignQuad = selectSignQuad;

    function testSpecialMultiplier(m) {
      sfx.playClick();
      const input = document.getElementById('signTestInput');
      const val = parseInt(input?.value || 17);
      const res = document.getElementById('signTestResult');
      if (!res) return;

      const product = val * m;
      if (m === 1) {
        res.innerHTML = `Multiplicative Identity: ${val} × 1 = <strong>${product}</strong> (Value and sign unchanged).`;
      } else if (m === -1) {
        res.innerHTML = `The Inverter: ${val} × (-1) = <strong>${product}</strong> (Sign flipped to Additive Inverse).`;
      } else {
        res.innerHTML = `Multiplication by Zero: ${val} × 0 = <strong>0</strong> (Annihilates to origin zero).`;
      }
    }
    window.testSpecialMultiplier = testSpecialMultiplier;


    // --- Simulator 10: Brahmagupta Scroll ---
    function demonstrateBrahmaguptaRule(rule) {
      sfx.playClick();
      const beam = document.getElementById('scaleBeam');
      const leftPan = document.getElementById('leftPanTokens');
      const rightPan = document.getElementById('rightPanTokens');
      const text = document.getElementById('brahmaTextDisplay');

      if (!leftPan || !rightPan || !text) return;

      leftPan.innerHTML = '';
      rightPan.innerHTML = '';

      if (rule === 'dhana_dhana') {
        if (beam) beam.setAttribute('transform', 'rotate(-10, 200, 60)');
        leftPan.innerHTML = `
          <circle cx="-10" cy="-5" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
          <circle cx="10" cy="-5" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
          <circle cx="0" cy="-15" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
        `;
        text.innerHTML = `
          <strong>Brahmagupta Shloka:</strong> <em>\"Dhanayor-ghāto dhanam\"</em><br>
          \"The product of two fortunes (wealth) is a fortune!\" (+3) × (+4) = +12 Dhana.
        `;
      } else if (rule === 'rna_rna') {
        if (beam) beam.setAttribute('transform', 'rotate(-10, 200, 60)');
        leftPan.innerHTML = `
          <circle cx="0" cy="-10" r="8" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
          <text x="0" y="-7" font-size="8" fill="#ffffff" text-anchor="middle" font-weight="bold">+12</text>
        `;
        text.innerHTML = `
          <strong>Brahmagupta Shloka:</strong> <em>\"Ṛṇayor-ghāto dhanam\"</em><br>
          \"The product of two debts is a fortune!\" (-3) × (-4) = +12 Dhana. Removing debts leaves wealth.
        `;
      } else {
        if (beam) beam.setAttribute('transform', 'rotate(10, 200, 60)');
        rightPan.innerHTML = `
          <circle cx="0" cy="-10" r="8" fill="#f43f5e" stroke="#e11d48" stroke-width="1.5"/>
          <text x="0" y="-7" font-size="8" fill="#ffffff" text-anchor="middle" font-weight="bold">-12</text>
        `;
        text.innerHTML = `
          <strong>Brahmagupta Shloka:</strong> <em>\"Ṛṇa-dhanayor-ghāto rnam\"</em><br>
          \"The product of a fortune and a debt is a debt!\" (+3) × (-4) = -12 Ṛṇa.
        `;
      }
    }
    window.demonstrateBrahmaguptaRule = demonstrateBrahmaguptaRule;


    // --- Simulator 11: Real World Integers ---
    function setRwTab(tab) {
      sfx.playClick();
      const elev = document.getElementById('rwElevatorView');
      const quiz = document.getElementById('rwQuizView');
      if (tab === 'elevator') {
        if (elev) elev.style.display = 'flex';
        if (quiz) quiz.style.display = 'none';
        updateElevatorSim();
      } else {
        if (elev) elev.style.display = 'none';
        if (quiz) quiz.style.display = 'flex';
        updateQuizSim();
      }
    }
    window.setRwTab = setRwTab;

    function updateElevatorSim() {
      const t = parseInt(document.getElementById('elevatorTimeSlider')?.value || 35);
      const timeVal = document.getElementById('elevatorTimeVal');
      if (timeVal) timeVal.textContent = `${t} min`;

      const descent = t * (-6);
      const position = 10 + descent;

      const calc = document.getElementById('elevatorCalc');
      const res = document.getElementById('elevatorDepthResult');

      if (calc) calc.textContent = `Position = 10 + [${t} × (-6)] = 10 - ${t * 6}`;
      if (res) res.textContent = `${position} m (${Math.abs(position)} m Depth)`;
    }
    window.updateElevatorSim = updateElevatorSim;

    function updateQuizSim() {
      const c = parseInt(document.getElementById('quizCorrSlider')?.value || 12);
      const w = parseInt(document.getElementById('quizWrongSlider')?.value || 5);

      const cVal = document.getElementById('quizCorrVal');
      const wVal = document.getElementById('quizWrongVal');
      if (cVal) cVal.textContent = c;
      if (wVal) wVal.textContent = w;

      const score = (c * 4) + (w * (-2));
      const expr = document.getElementById('quizCalcExpr');
      const res = document.getElementById('quizTotalResult');

      if (expr) expr.textContent = `(${c} × 4) + [${w} × (-2)] = ${c * 4} - ${w * 2}`;
      if (res) res.textContent = `${score} Marks`;
    }
    window.updateQuizSim = updateQuizSim;


    // --- Simulator 12: Comm & Assoc ---
    function setPropTab(tab) {
      sfx.playClick();
      const comm = document.getElementById('propCommView');
      const assoc = document.getElementById('propAssocView');
      if (tab === 'comm') {
        if (comm) comm.style.display = 'flex';
        if (assoc) assoc.style.display = 'none';
      } else {
        if (comm) comm.style.display = 'none';
        if (assoc) assoc.style.display = 'flex';
      }
    }
    window.setPropTab = setPropTab;

    let commSwapped = false;
    function swapCommutativeOrder() {
      sfx.playClick();
      commSwapped = !commSwapped;
      const e1 = document.getElementById('commExpr1');
      const e2 = document.getElementById('commExpr2');
      if (commSwapped) {
        if (e1) e1.textContent = '4 × (-6) = -24';
        if (e2) e2.textContent = '(-6) × 4 = -24';
      } else {
        if (e1) e1.textContent = '(-6) × 4 = -24';
        if (e2) e2.textContent = '4 × (-6) = -24';
      }
    }
    window.swapCommutativeOrder = swapCommutativeOrder;

    let assocShifted = false;
    function shiftAssociativeBrackets() {
      sfx.playClick();
      assocShifted = !assocShifted;
      const e1 = document.getElementById('assocExpr1');
      const e2 = document.getElementById('assocExpr2');
      if (assocShifted) {
        if (e1) e1.textContent = '[4 × (-5)] × (-3)';
        if (e2) e2.textContent = '4 × [(-5) × (-3)]';
      } else {
        if (e1) e1.textContent = '[(-3) × 4] × (-5)';
        if (e2) e2.textContent = '(-3) × [4 × (-5)]';
      }
    }
    window.shiftAssociativeBrackets = shiftAssociativeBrackets;


    // --- Simulator 13: Distributive Grid ---
    function updateDistributiveGrid() {
      const a = parseInt(document.getElementById('distSliderA')?.value || -4);
      const b = parseInt(document.getElementById('distSliderB')?.value || 6);
      const c = parseInt(document.getElementById('distSliderC')?.value || 4);

      const valA = document.getElementById('distValA');
      const valB = document.getElementById('distValB');
      const valC = document.getElementById('distValC');
      if (valA) valA.textContent = a;
      if (valB) valB.textContent = b;
      if (valC) valC.textContent = c;

      const p1 = a * b;
      const p2 = a * c;
      const total = a * (b + c);

      const tLeft = document.getElementById('rectLeftText');
      const tRight = document.getElementById('rectRightText');
      if (tLeft) tLeft.textContent = `(${a}) × ${b} = ${p1}`;
      if (tRight) tRight.textContent = `(${a}) × ${c} = ${p2}`;

      const sum = document.getElementById('distribEvalSummary');
      if (sum) {
        sum.textContent = `(${a}) × (${b} + ${c}) = (${a}) × ${b + c} = ${total} = [(${p1}) + (${p2})]!`;
      }
    }
    window.updateDistributiveGrid = updateDistributiveGrid;


    // --- Simulator 14: Multiple Integers Parity ---
    let chainFactors = [-2, -3, 4, -5, 2];

    function renderFactorsChain() {
      const list = document.getElementById('factorsChainList');
      const badge = document.getElementById('parityCountBadge');
      const cancelBox = document.getElementById('pairwiseCancellationBox');
      const resMsg = document.getElementById('parityResultMsg');

      if (!list || !badge || !cancelBox || !resMsg) return;

      list.innerHTML = '';
      let negCount = 0;
      let product = 1;

      chainFactors.forEach((f, idx) => {
        product *= f;
        if (f < 0) negCount++;

        const chip = document.createElement('div');
        chip.className = f < 0 ?
          'px-3 py-1.5 rounded-lg bg-rose-950/60 border border-rose-500/50 text-rose-300 font-mono font-bold text-xs' :
          'px-3 py-1.5 rounded-lg bg-emerald-950/60 border border-emerald-500/50 text-emerald-300 font-mono font-bold text-xs';
        chip.textContent = f > 0 ? `+${f}` : `${f}`;
        list.appendChild(chip);

        if (idx < chainFactors.length - 1) {
          const mult = document.createElement('span');
          mult.className = 'text-slate-400 font-bold';
          mult.textContent = '×';
          list.appendChild(mult);
        }
      });

      const isEven = (negCount % 2 === 0);
      badge.textContent = `Negatives: ${negCount} (${isEven ? 'EVEN' : 'ODD'})`;
      badge.className = isEven ? 'text-xs font-mono font-bold text-emerald-400' : 'text-xs font-mono font-bold text-rose-400';

      const pairs = Math.floor(negCount / 2);
      const unpaired = negCount % 2;

      cancelBox.innerHTML = `
        <span class="text-slate-300">Negative Sign Pairing:</span>
        <span class="text-emerald-400 font-bold">${pairs} Pair(s) cancel to (+)</span>
        ${unpaired > 0 ? '<span class="text-rose-400 font-bold">1 Leftover (-) flips to NEGATIVE</span>' : '<span class="text-emerald-300 font-bold">0 Leftover (-) $\implies$ Pure POSITIVE</span>'}
      `;

      resMsg.textContent = `Result = ${product > 0 ? '+' + product : product} (${isEven ? 'POSITIVE' : 'NEGATIVE'})`;
      resMsg.className = isEven ? 'font-mono font-bold text-emerald-400 text-sm' : 'font-mono font-bold text-rose-400 text-sm';
    }
    window.renderFactorsChain = renderFactorsChain;

    function randomizeFactorsChain() {
      sfx.playClick();
      const count = 4 + Math.floor(Math.random() * 2); // 4 or 5
      chainFactors = [];
      for (let i = 0; i < count; i++) {
        const sign = Math.random() > 0.5 ? 1 : -1;
        const val = 1 + Math.floor(Math.random() * 5);
        chainFactors.push(sign * val);
      }
      renderFactorsChain();
    }
    window.randomizeFactorsChain = randomizeFactorsChain;


    // --- Simulator 15: Missing Factor ---
    function setDivExample(a, b) {
      sfx.playClick();
      const task = document.getElementById('divTaskExpr');
      const eq = document.getElementById('divEqExpr');
      const box = document.getElementById('divSolutionBox');

      if (!task || !eq || !box) return;

      if (b === 0) {
        task.textContent = `(${a}) ÷ 0 = ?`;
        eq.textContent = `0 × ? = ${a}`;
        box.className = 'p-2 rounded bg-rose-950/40 border border-rose-500/30 text-xs font-mono text-rose-300 w-full text-center';
        box.textContent = `⚠️ Impossible! Since 0 × (any number) = 0, no number can satisfy 0 × ? = ${a}. Division by zero is UNDEFINED!`;
        return;
      }

      const quotient = Math.floor(a / b);
      task.textContent = `(${a}) ÷ (${b}) = ?`;
      eq.textContent = `(${b}) × ? = ${a}`;
      box.className = 'p-2 rounded bg-emerald-950/40 border border-emerald-500/30 text-xs font-mono text-emerald-300 w-full text-center';
      box.textContent = `✓ Missing Factor: Since (${b}) × (${quotient}) = ${a}, the answer is ${quotient}! Thus (${a}) ÷ (${b}) = ${quotient}.`;
    }
    window.setDivExample = setDivExample;


    // --- Simulator 16: Division Rules Diagnostic ---
    function updateDivisionDiagnostic() {
      const a = parseInt(document.getElementById('divSliderA')?.value || -20);
      let b = parseInt(document.getElementById('divSliderB')?.value || 5);
      if (b === 0) b = 1; // avoid div by 0 for diagnostic

      const valA = document.getElementById('divNonCommValA');
      const valB = document.getElementById('divNonCommValB');
      if (valA) valA.textContent = a;
      if (valB) valB.textContent = b;

      const q1 = (a / b).toFixed(2);
      const q2 = (b / a).toFixed(2);

      const r1 = document.getElementById('divDiagRes1');
      const r2 = document.getElementById('divDiagRes2');
      if (r1) r1.textContent = `(${a}) ÷ (${b}) = ${q1}`;
      if (r2) r2.textContent = `(${b}) ÷ (${a}) = ${q2}`;

      const verdict = document.getElementById('divDiagVerdict');
      if (verdict) {
        verdict.textContent = `${q1} ≠ ${q2}. Division of integers is strictly NOT commutative!`;
      }
    }
    window.updateDivisionDiagnostic = updateDivisionDiagnostic;
"""

# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 7 Mathematics - Chapter 2: Arithmetic Expressions
Simulators 1 to 16
"""

SIMULATORS_JS = r"""
    // ========================================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 2 Arithmetic Expressions)
    // ========================================================

    // Slide 1: Expression Tree Visualizer
    function simSimpleExpressionsTree() {
      simHeaderTitle.textContent = "Interactive Arithmetic Expression Tree Visualizer";
      let activePreset = 0;
      const presets = [
        { label: "8 + 7", expr: "8 + 7", left: 8, op: "+", right: 7, res: 15, type: "simple" },
        { label: "24 - 9", expr: "24 - 9", left: 24, op: "-", right: 9, res: 15, type: "simple" },
        { label: "6 × 7", expr: "6 × 7", left: 6, op: "×", right: 7, res: 42, type: "simple" },
        { label: "54 ÷ 6", expr: "54 ÷ 6", left: 54, op: "÷", right: 6, res: 9, type: "simple" },
        { label: "3 + 4 × 5", expr: "3 + (4 × 5)", left: 3, op: "+", right: "4 × 5", subLeft: 4, subOp: "×", subRight: 5, subRes: 20, res: 23, type: "compound" }
      ];

      function render() {
        const p = presets[activePreset];
        let treeSvg = "";

        if (p.type === "simple") {
          treeSvg = `
            <!-- Root Result Node -->
            <line x1="270" y1="90" x2="190" y2="180" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>
            <line x1="270" y1="90" x2="350" y2="180" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4"/>

            <circle cx="270" cy="90" r="34" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
            <text x="270" y="85" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">RESULT</text>
            <text x="270" y="104" fill="#f8fafc" font-size="18" font-weight="900" text-anchor="middle">${p.res}</text>

            <!-- Operator Node -->
            <circle cx="270" cy="135" r="18" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
            <text x="270" y="141" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">${p.op}</text>

            <!-- Left Leaf -->
            <circle cx="190" cy="180" r="28" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
            <text x="190" y="176" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">LEAF 1</text>
            <text x="190" y="193" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">${p.left}</text>

            <!-- Right Leaf -->
            <circle cx="350" cy="180" r="28" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
            <text x="350" y="176" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">LEAF 2</text>
            <text x="350" y="193" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">${p.right}</text>
          `;
        } else {
          treeSvg = `
            <!-- Root Result Node -->
            <line x1="270" y1="70" x2="160" y2="160" stroke="#38bdf8" stroke-width="3"/>
            <line x1="270" y1="70" x2="380" y2="150" stroke="#38bdf8" stroke-width="3"/>

            <circle cx="270" cy="70" r="32" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
            <text x="270" y="65" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">FINAL RESULT</text>
            <text x="270" y="83" fill="#f8fafc" font-size="18" font-weight="900" text-anchor="middle">${p.res}</text>

            <!-- Main Op Node -->
            <circle cx="270" cy="115" r="16" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
            <text x="270" y="121" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">${p.op}</text>

            <!-- Left Leaf -->
            <circle cx="160" cy="160" r="26" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
            <text x="160" y="156" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">TERM 1</text>
            <text x="160" y="173" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">${p.left}</text>

            <!-- Subtree Right Branch -->
            <circle cx="380" cy="150" r="28" fill="#1e293b" stroke="#a855f7" stroke-width="2.5"/>
            <text x="380" y="145" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle">TERM 2</text>
            <text x="380" y="162" fill="#f8fafc" font-size="15" font-weight="900" text-anchor="middle">${p.subRes}</text>

            <!-- Subtree Children -->
            <line x1="380" y1="150" x2="330" y2="230" stroke="#a855f7" stroke-width="2"/>
            <line x1="380" y1="150" x2="430" y2="230" stroke="#a855f7" stroke-width="2"/>

            <circle cx="380" cy="190" r="14" fill="#a855f7" stroke="#e9d5ff" stroke-width="1.5"/>
            <text x="380" y="195" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${p.subOp}</text>

            <circle cx="330" cy="230" r="22" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
            <text x="330" y="235" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">${p.subLeft}</text>

            <circle cx="430" cy="230" r="22" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
            <text x="430" y="235" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">${p.subRight}</text>
          `;
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <radialGradient id="treeBg" cx="50%" cy="50%" r="75%">
                <stop offset="0%" stop-color="#0f172a"/>
                <stop offset="100%" stop-color="#020617"/>
              </radialGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="url(#treeBg)"/>

            <!-- Header Badge -->
            <rect x="140" y="15" width="260" height="32" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Expression: ${p.expr} = ${p.res}</text>

            <!-- Tree Structure -->
            ${treeSvg}

            <!-- Bottom Insight Card -->
            <rect x="30" y="268" width="480" height="50" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#64748b" stroke-width="1"/>
            <text x="270" y="288" fill="#94a3b8" font-size="10.5" font-weight="600" text-anchor="middle">An arithmetic expression simplifies upwards through operations to a single number.</text>
            <text x="270" y="306" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Numbers are the leaves, operations are branches, and the final value is the root!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Select Expression:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.label}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 2: Pan Balance Scale
    function simComparingExpressionsBalance() {
      simHeaderTitle.textContent = "Comparing Expressions: Two-Pan Balance Scale Simulator";
      let leftVal = 24, rightVal = 24;
      let leftExpr = "4 × 6", rightExpr = "15 + 9";

      const pairs = [
        { lExpr: "4 × 6", lVal: 24, rExpr: "15 + 9", rVal: 24, label: "24 = 24 (Balanced)" },
        { lExpr: "5 × 7", lVal: 35, rExpr: "6 × 6", rVal: 36, label: "35 < 36 (Right Heavier)" },
        { lExpr: "100 - 32", lVal: 68, rExpr: "8 × 8", rVal: 64, label: "68 > 64 (Left Heavier)" },
        { lExpr: "48 ÷ 4", lVal: 12, rExpr: "3 × 4", rVal: 12, label: "12 = 12 (Balanced)" }
      ];

      function render(lE, lV, rE, rV) {
        leftExpr = lE; leftVal = lV; rightExpr = rE; rightVal = rV;
        const diff = rightVal - leftVal; // positive means right is heavier
        const tiltDeg = Math.max(-12, Math.min(12, diff * 3));
        const relation = leftVal === rightVal ? "=" : (leftVal > rightVal ? ">" : "<");
        const statusColor = leftVal === rightVal ? "#10b981" : "#f59e0b";
        const statusText = leftVal === rightVal ? "BALANCED: Expressions are EQUIVALENT!" : (leftVal > rightVal ? "LEFT IS HEAVIER: Greater Value" : "RIGHT IS HEAVIER: Greater Value");

        // Pan positions with tilt
        const rad = (tiltDeg * Math.PI) / 180;
        const armLength = 150;
        const pivotX = 270, pivotY = 110;
        const leftX = pivotX - armLength * Math.cos(rad);
        const leftY = pivotY - armLength * Math.sin(rad);
        const rightX = pivotX + armLength * Math.cos(rad);
        const rightY = pivotY + armLength * Math.sin(rad);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <linearGradient id="metalArm" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#94a3b8"/>
                <stop offset="50%" stop-color="#f8fafc"/>
                <stop offset="100%" stop-color="#94a3b8"/>
              </linearGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Fulcrum / Stand -->
            <polygon points="270,110 245,260 295,260" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <rect x="220" y="255" width="100" height="15" rx="4" fill="#334155" stroke="#64748b"/>
            <circle cx="270" cy="110" r="10" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>

            <!-- Balance Arm -->
            <line x1="${leftX}" y1="${leftY}" x2="${rightX}" y2="${rightY}" stroke="url(#metalArm)" stroke-width="7" stroke-linecap="round"/>

            <!-- Left Strings and Pan -->
            <line x1="${leftX}" y1="${leftY}" x2="${leftX - 35}" y2="${leftY + 65}" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="${leftX}" y1="${leftY}" x2="${leftX + 35}" y2="${leftY + 65}" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M ${leftX - 45} ${leftY + 65} Q ${leftX} ${leftY + 80} ${leftX + 45} ${leftY + 65} Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

            <!-- Left Pan Content -->
            <rect x="${leftX - 42}" y="${leftY + 15}" width="84" height="42" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="${leftX}" y="${leftY + 32}" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">${leftExpr}</text>
            <text x="${leftX}" y="${leftY + 50}" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">Val: ${leftVal}</text>

            <!-- Right Strings and Pan -->
            <line x1="${rightX}" y1="${rightY}" x2="${rightX - 35}" y2="${rightY + 65}" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="${rightX}" y1="${rightY}" x2="${rightX + 35}" y2="${rightY + 65}" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M ${rightX - 45} ${rightY + 65} Q ${rightX} ${rightY + 80} ${rightX + 45} ${rightY + 65} Z" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>

            <!-- Right Pan Content -->
            <rect x="${rightX - 42}" y="${rightY + 15}" width="84" height="42" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="${rightX}" y="${rightY + 32}" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">${rightExpr}</text>
            <text x="${rightX}" y="${rightY + 50}" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">Val: ${rightVal}</text>

            <!-- Comparison Center Badge -->
            <rect x="180" y="20" width="180" height="45" rx="10" fill="rgba(15, 23, 42, 0.9)" stroke="${statusColor}" stroke-width="2"/>
            <text x="270" y="44" fill="${statusColor}" font-size="18" font-weight="900" text-anchor="middle">${leftExpr} ${relation} ${rightExpr}</text>
            <text x="270" y="58" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">(${leftVal} ${relation} ${rightVal})</text>

            <!-- Bottom Status Banner -->
            <rect x="50" y="280" width="440" height="36" rx="8" fill="rgba(30, 41, 59, 0.7)" stroke="${statusColor}" stroke-width="1"/>
            <text x="270" y="302" fill="${statusColor}" font-size="12" font-weight="800" text-anchor="middle">${statusText}</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Pair:</span>
          ${pairs.map((p, idx) => `<button class="sim-btn ${idx === 0 ? 'active' : ''}" data-idx="${idx}">${p.label}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const p = pairs[parseInt(btn.dataset.idx)];
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render(p.lExpr, p.lVal, p.rExpr, p.rVal);
          sfx.playClick();
        });
      });

      render(pairs[0].lExpr, pairs[0].lVal, pairs[0].rExpr, pairs[0].rVal);
    }

    // Slide 3: Order of Operations Precedence Engine
    function simOrderOfOperationsPrecedence() {
      simHeaderTitle.textContent = "BODMAS Priority Engine: Multiplication & Division First";
      let activePreset = 0;
      const presets = [
        {
          expr: "5 + 3 × 4",
          naiveSteps: ["(5 + 3) = 8", "8 × 4 = 32 (WRONG!)"],
          naiveVal: 32,
          correctSteps: ["3 × 4 = 12 (Multiply First)", "5 + 12 = 17 (CORRECT)"],
          correctVal: 17,
          opHighlight: "3 × 4"
        },
        {
          expr: "20 - 8 ÷ 2",
          naiveSteps: ["(20 - 8) = 12", "12 ÷ 2 = 6 (WRONG!)"],
          naiveVal: 6,
          correctSteps: ["8 ÷ 2 = 4 (Divide First)", "20 - 4 = 16 (CORRECT)"],
          correctVal: 16,
          opHighlight: "8 ÷ 2"
        },
        {
          expr: "6 × 4 - 15 ÷ 3",
          naiveSteps: ["6 × 4 = 24", "24 - 15 = 9", "9 ÷ 3 = 3 (WRONG!)"],
          naiveVal: 3,
          correctSteps: ["6 × 4 = 24 and 15 ÷ 3 = 5", "24 - 5 = 19 (CORRECT)"],
          correctVal: 19,
          opHighlight: "6 × 4 and 15 ÷ 3"
        }
      ];

      function render() {
        const p = presets[activePreset];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090e1a"/>

            <!-- Main Title Banner -->
            <rect x="120" y="15" width="300" height="38" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Expression: ${p.expr}</text>

            <!-- Left Card: The Naive Mistake -->
            <g transform="translate(25, 68)">
              <rect x="0" y="0" width="235" height="185" rx="10" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
              <rect x="15" y="12" width="205" height="26" rx="6" fill="rgba(239, 68, 68, 0.2)"/>
              <text x="117" y="29" fill="#fca5a5" font-size="11" font-weight="800" text-anchor="middle">❌ Naive Left-to-Right</text>

              <text x="18" y="60" fill="#94a3b8" font-size="10">Ignores operational precedence:</text>
              ${p.naiveSteps.map((st, i) => `
                <text x="18" y="${82 + i * 22}" fill="${i === p.naiveSteps.length - 1 ? '#f87171' : '#cbd5e1'}" font-size="11" font-weight="700">Step ${i+1}: ${st}</text>
              `).join('')}

              <rect x="25" y="132" width="185" height="38" rx="6" fill="#1e1b2e" stroke="#ef4444" stroke-width="1"/>
              <text x="117" y="150" fill="#94a3b8" font-size="9" text-anchor="middle">Incorrect Result</text>
              <text x="117" y="164" fill="#f87171" font-size="14" font-weight="900" text-anchor="middle">${p.naiveVal}</text>
            </g>

            <!-- Right Card: The BODMAS Standard -->
            <g transform="translate(280, 68)">
              <rect x="0" y="0" width="235" height="185" rx="10" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
              <rect x="15" y="12" width="205" height="26" rx="6" fill="rgba(16, 185, 129, 0.2)"/>
              <text x="117" y="29" fill="#6ee7b7" font-size="11" font-weight="800" text-anchor="middle">✅ BODMAS / Correct Rule</text>

              <text x="18" y="60" fill="#94a3b8" font-size="10">High priority: ${p.opHighlight}</text>
              ${p.correctSteps.map((st, i) => `
                <text x="18" y="${82 + i * 22}" fill="${i === p.correctSteps.length - 1 ? '#4ade80' : '#cbd5e1'}" font-size="11" font-weight="700">Step ${i+1}: ${st}</text>
              `).join('')}

              <rect x="25" y="132" width="185" height="38" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
              <text x="117" y="150" fill="#a7f3d0" font-size="9" text-anchor="middle">Authentic Mathematical Value</text>
              <text x="117" y="164" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${p.correctVal}</text>
            </g>

            <!-- Bottom Rule Banner -->
            <rect x="25" y="265" width="490" height="50" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1"/>
            <text x="270" y="286" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Golden Law: Multiplication (×) and Division (÷) bind tighter than (+) and (-)</text>
            <text x="270" y="304" fill="#94a3b8" font-size="10" text-anchor="middle">Always compute × and ÷ before + and - unless brackets explicitly command otherwise.</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Select Problem:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.expr}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 4: Brackets Nested Evaluator
    function simBracketsNestedEvaluator() {
      simHeaderTitle.textContent = "Brackets Powerhouse: Step-by-Step Nested Bracket Resolver";
      let step = 0;
      const steps = [
        {
          stage: "Full Expression",
          disp: "3 × [ 4 + ( 8 - 2 ) ]",
          desc: "Expression contains nested brackets. Inner bracket: (8 - 2)",
          activeBox: "inner",
          innerVal: "(8 - 2)",
          outerVal: "[4 + ...]",
          totalVal: "Waiting..."
        },
        {
          stage: "Step 1: Innermost Bracket",
          disp: "3 × [ 4 + 6 ]",
          desc: "Inner round brackets resolved: (8 - 2) = 6",
          activeBox: "outer",
          innerVal: "6",
          outerVal: "[4 + 6]",
          totalVal: "Waiting..."
        },
        {
          stage: "Step 2: Square Brackets",
          disp: "3 × 10",
          desc: "Square brackets resolved: [4 + 6] = 10",
          activeBox: "mult",
          innerVal: "6",
          outerVal: "10",
          totalVal: "Waiting..."
        },
        {
          stage: "Step 3: Final Product",
          disp: "30",
          desc: "Final multiplication performed: 3 × 10 = 30",
          activeBox: "done",
          innerVal: "6",
          outerVal: "10",
          totalVal: "30"
        }
      ];

      function render() {
        const s = steps[step];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Current Expression Display -->
            <rect x="40" y="20" width="460" height="60" rx="12" fill="rgba(15, 23, 42, 0.9)" stroke="#a855f7" stroke-width="2"/>
            <text x="270" y="44" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">${s.stage}</text>
            <text x="270" y="66" fill="#f8fafc" font-size="18" font-weight="900" text-anchor="middle">${s.disp}</text>

            <!-- Nested Visual Boxes -->
            <g transform="translate(60, 100)">
              <!-- Outer Bracket Container -->
              <rect x="0" y="0" width="420" height="120" rx="10" fill="rgba(30, 41, 59, 0.6)" stroke="${s.activeBox === 'outer' ? '#fbbf24' : '#64748b'}" stroke-width="${s.activeBox === 'outer' ? 3 : 1.5}"/>
              <text x="15" y="24" fill="#fbbf24" font-size="11" font-weight="800">[ Square Bracket Scope: 4 + (8 - 2) ]</text>

              <!-- Inner Bracket Container -->
              <rect x="180" y="35" width="210" height="65" rx="8" fill="rgba(56, 189, 248, 0.15)" stroke="${s.activeBox === 'inner' ? '#38bdf8' : '#0284c7'}" stroke-width="${s.activeBox === 'inner' ? 3 : 1.5}"/>
              <text x="195" y="55" fill="#38bdf8" font-size="10" font-weight="800">( Innermost Parentheses )</text>
              <text x="285" y="80" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">${step === 0 ? "8 - 2" : "= 6"}</text>

              <text x="80" y="75" fill="#e2e8f0" font-size="16" font-weight="800">4  +</text>
            </g>

            <!-- Step Explanation Card -->
            <rect x="40" y="240" width="460" height="65" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="270" y="264" fill="#60a5fa" font-size="12" font-weight="800" text-anchor="middle">${s.desc}</text>
            <text x="270" y="288" fill="#94a3b8" font-size="10" text-anchor="middle">Rule: Innermost ( ) must be solved first, then { }, then [ ], working outward!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnPrevStep">⏮ Previous Step</button>
          <span id="stepIndicator" style="font-weight:700; color:#38bdf8; font-size:0.95rem;">Step 1 of 4</span>
          <button class="sim-btn active" id="btnNextStep">Next Step ⏭</button>
          <button class="sim-btn" id="btnResetStep">🔄 Reset</button>
        </div>
      `;

      function updateControls() {
        document.getElementById('stepIndicator').textContent = `Step ${step + 1} of ${steps.length}`;
        document.getElementById('btnPrevStep').disabled = (step === 0);
        document.getElementById('btnNextStep').disabled = (step === steps.length - 1);
      }

      document.getElementById('btnPrevStep').onclick = () => {
        if (step > 0) { step--; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnNextStep').onclick = () => {
        if (step < steps.length - 1) { step++; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnResetStep').onclick = () => {
        step = 0; render(); updateControls(); sfx.playClick();
      };

      render();
      updateControls();
    }

    // Slide 5: Terms Boundary Detector
    function simTermsBoundaryDetector() {
      simHeaderTitle.textContent = "Signposts of Arithmetic: Detecting Terms Separated by + and -";
      let activePreset = 0;
      const presets = [
        {
          expr: "15 + 4 × 3 - 18 ÷ 2",
          terms: [
            { raw: "15", val: 15, sign: "+", op: "Constant" },
            { raw: "4 × 3", val: 12, sign: "+", op: "Multiplication" },
            { raw: "18 ÷ 2", val: 9, sign: "-", op: "Division" }
          ],
          result: 18
        },
        {
          expr: "50 - (6 + 4) × 2 + 8",
          terms: [
            { raw: "50", val: 50, sign: "+", op: "Constant" },
            { raw: "(6 + 4) × 2", val: 20, sign: "-", op: "Bracketed Product" },
            { raw: "8", val: 8, sign: "+", op: "Constant" }
          ],
          result: 38
        },
        {
          expr: "100 ÷ 5 + 6 × 7 - 14",
          terms: [
            { raw: "100 ÷ 5", val: 20, sign: "+", op: "Division" },
            { raw: "6 × 7", val: 42, sign: "+", op: "Multiplication" },
            { raw: "14", val: 14, sign: "-", op: "Constant" }
          ],
          result: 48
        }
      ];

      function render() {
        const p = presets[activePreset];
        const colors = ["#38bdf8", "#a855f7", "#f59e0b", "#10b981"];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <rect x="50" y="15" width="440" height="38" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Expression: ${p.expr}</text>

            <!-- Train Metaphor / Compartments -->
            <g transform="translate(30, 75)">
              <text x="240" y="15" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">🚂 Expression Train: Each Term is an Independent Wagon</text>

              ${p.terms.map((t, idx) => {
                const x = idx * 160;
                return `
                  <!-- Signpost / Boundary -->
                  ${idx > 0 ? `
                    <circle cx="${x - 10}" cy="80" r="14" fill="${t.sign === '+' ? '#10b981' : '#ef4444'}" stroke="#ffffff" stroke-width="1.5"/>
                    <text x="${x - 10}" y="${86}" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">${t.sign}</text>
                  ` : ''}

                  <!-- Term Wagon -->
                  <g transform="translate(${x + 10}, 40)">
                    <rect x="0" y="0" width="130" height="85" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${colors[idx]}" stroke-width="2"/>
                    <text x="65" y="20" fill="${colors[idx]}" font-size="10" font-weight="800" text-anchor="middle">TERM ${idx + 1}</text>
                    <text x="65" y="44" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${t.raw}</text>
                    <line x1="15" y1="52" x2="115" y2="52" stroke="rgba(255,255,255,0.2)"/>
                    <text x="65" y="68" fill="#4ade80" font-size="12" font-weight="800" text-anchor="middle">Value = ${t.val}</text>
                  </g>
                `;
              }).join('')}
            </g>

            <!-- Bottom Evaluation Card -->
            <rect x="40" y="235" width="460" height="75" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="258" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Term-by-Term Simplification:</text>
            <text x="270" y="280" fill="#f8fafc" font-size="15" font-weight="900" text-anchor="middle">
              ${p.terms.map((t, i) => `${i > 0 ? ' ' + t.sign + ' ' : ''}${t.val}`).join('')} = ${p.result}
            </text>
            <text x="270" y="298" fill="#94a3b8" font-size="9.5" text-anchor="middle">+ and - outside brackets act as boundaries separating expressions into terms.</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Select Expression:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.expr}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 6: Multi-Term Evaluator Engine
    function simMultiTermEvalEngine() {
      simHeaderTitle.textContent = "Multi-Term Parallel Evaluation Flow";
      let phase = 0; // 0: Raw, 1: Sub-terms computed, 2: Final sum

      simCanvas.innerHTML = `
        <svg viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

          <rect x="80" y="15" width="380" height="36" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Expression: 8 × 5 + 36 ÷ 4 - 7 × 3</text>

          <!-- 3 Term Blocks -->
          <g transform="translate(30, 70)">
            <!-- Term 1 -->
            <rect x="0" y="0" width="140" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <text x="70" y="24" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Term 1</text>
            <text x="70" y="55" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">8 × 5</text>
            <rect x="15" y="70" width="110" height="28" rx="6" fill="#0f172a" stroke="#38bdf8"/>
            <text id="term1Val" x="70" y="88" fill="#34d399" font-size="13" font-weight="900" text-anchor="middle">?</text>

            <!-- Sign 1 -->
            <circle cx="165" cy="55" r="14" fill="#10b981"/>
            <text x="165" y="61" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">+</text>

            <!-- Term 2 -->
            <rect x="190" y="0" width="140" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
            <text x="260" y="24" fill="#c084fc" font-size="11" font-weight="800" text-anchor="middle">Term 2</text>
            <text x="260" y="55" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">36 ÷ 4</text>
            <rect x="205" y="70" width="110" height="28" rx="6" fill="#0f172a" stroke="#a855f7"/>
            <text id="term2Val" x="260" y="88" fill="#34d399" font-size="13" font-weight="900" text-anchor="middle">?</text>

            <!-- Sign 2 -->
            <circle cx="355" cy="55" r="14" fill="#ef4444"/>
            <text x="355" y="61" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">-</text>

            <!-- Term 3 -->
            <rect x="380" y="0" width="130" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
            <text x="445" y="24" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Term 3</text>
            <text x="445" y="55" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">7 × 3</text>
            <rect x="390" y="70" width="110" height="28" rx="6" fill="#0f172a" stroke="#f59e0b"/>
            <text id="term3Val" x="445" y="88" fill="#34d399" font-size="13" font-weight="900" text-anchor="middle">?</text>
          </g>

          <!-- Final Assembly Box -->
          <rect x="70" y="215" width="400" height="85" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#34d399" stroke-width="2"/>
          <text id="phaseDesc" x="270" y="240" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Phase 1: Identify 3 distinct terms</text>
          <text id="phaseFormula" x="270" y="268" fill="#f8fafc" font-size="18" font-weight="900" text-anchor="middle">[ Term 1 ] + [ Term 2 ] - [ Term 3 ]</text>
          <text id="phaseSub" x="270" y="288" fill="#94a3b8" font-size="10" text-anchor="middle">Compute each term independently, then combine!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnPhase1">1. Identify Terms</button>
          <button class="sim-btn" id="btnPhase2">2. Evaluate Terms</button>
          <button class="sim-btn" id="btnPhase3">3. Final Combine</button>
        </div>
      `;

      function setPhase(p) {
        phase = p;
        simControls.querySelectorAll('.sim-btn').forEach((b, i) => {
          b.classList.toggle('active', i === p);
        });

        const t1 = document.getElementById('term1Val');
        const t2 = document.getElementById('term2Val');
        const t3 = document.getElementById('term3Val');
        const desc = document.getElementById('phaseDesc');
        const form = document.getElementById('phaseFormula');
        const sub = document.getElementById('phaseSub');

        if (p === 0) {
          t1.textContent = "?"; t2.textContent = "?"; t3.textContent = "?";
          desc.textContent = "Phase 1: Identify 3 distinct terms separated by + and -";
          form.textContent = "[ Term 1 ] + [ Term 2 ] - [ Term 3 ]";
          sub.textContent = "Each term will be simplified into a single integer.";
        } else if (p === 1) {
          t1.textContent = "40"; t2.textContent = "9"; t3.textContent = "21";
          desc.textContent = "Phase 2: Evaluate each term independently";
          form.textContent = "40 + 9 - 21";
          sub.textContent = "8 × 5 = 40, 36 ÷ 4 = 9, 7 × 3 = 21";
        } else {
          t1.textContent = "40"; t2.textContent = "9"; t3.textContent = "21";
          desc.textContent = "Phase 3: Final Left-to-Right Addition & Subtraction";
          form.textContent = "40 + 9 - 21 = 49 - 21 = 28";
          sub.textContent = "Final result evaluated seamlessly!";
        }
        sfx.playClick();
      }

      document.getElementById('btnPhase1').onclick = () => setPhase(0);
      document.getElementById('btnPhase2').onclick = () => setPhase(1);
      document.getElementById('btnPhase3').onclick = () => setPhase(2);
      setPhase(0);
    }

    // Slide 7: Everyday Order Commutative
    function simEverydayOrderCommutative() {
      simHeaderTitle.textContent = "Everyday Order: Commutative vs Non-Commutative Actions";
      let activeItem = 0;
      const scenarios = [
        {
          name: "Socks vs Shoes",
          orderA: "Put on Socks ➔ Then Shoes",
          orderB: "Put on Shoes ➔ Then Socks",
          isCommutative: false,
          resultA: "Warm & fitted feet ✅",
          resultB: "Socks stretched over shoes! Ridiculous ❌",
          mathParallel: "Subtraction / Division: Order changes outcome completely! 10 - 4 ≠ 4 - 10"
        },
        {
          name: "Left Sock vs Right Sock",
          orderA: "Left Sock First ➔ Then Right",
          orderB: "Right Sock First ➔ Then Left",
          isCommutative: true,
          resultA: "Both feet neatly dressed ✅",
          resultB: "Both feet neatly dressed ✅",
          mathParallel: "Addition: a + b = b + a. Order does not matter at all!"
        },
        {
          name: "Milk & Sugar in Tea",
          orderA: "Pour Milk ➔ Then Stir Sugar",
          orderB: "Stir Sugar ➔ Then Pour Milk",
          isCommutative: true,
          resultA: "Sweet delicious cup of tea ☕",
          resultB: "Identical sweet delicious tea ☕",
          mathParallel: "Multiplication: a × b = b × a. Commutative property holds!"
        },
        {
          name: "Shower vs Getting Dressed",
          orderA: "Take Shower ➔ Then Wear Clothes",
          orderB: "Wear Clothes ➔ Then Take Shower",
          isCommutative: false,
          resultA: "Clean, fresh, and dry ✅",
          resultB: "Soaked, ruined clothes! Disaster ❌",
          mathParallel: "Operations inside vs outside brackets: Order of execution is critical!"
        }
      ];

      function render() {
        const s = scenarios[activeItem];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="100" y="15" width="340" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Scenario: ${s.name}</text>

            <!-- Order 1 Card -->
            <g transform="translate(35, 68)">
              <rect x="0" y="0" width="220" height="135" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#3b82f6" stroke-width="1.5"/>
              <text x="110" y="24" fill="#60a5fa" font-size="11" font-weight="800" text-anchor="middle">Sequence A (Standard)</text>
              <text x="110" y="55" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">${s.orderA}</text>
              <rect x="10" y="75" width="200" height="45" rx="6" fill="#1e293b"/>
              <text x="110" y="102" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">${s.resultA}</text>
            </g>

            <!-- Order 2 Card -->
            <g transform="translate(285, 68)">
              <rect x="0" y="0" width="220" height="135" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="${s.isCommutative ? '#10b981' : '#ef4444'}" stroke-width="1.5"/>
              <text x="110" y="24" fill="${s.isCommutative ? '#34d399' : '#f87171'}" font-size="11" font-weight="800" text-anchor="middle">Sequence B (Swapped)</text>
              <text x="110" y="55" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">${s.orderB}</text>
              <rect x="10" y="75" width="200" height="45" rx="6" fill="#1e293b"/>
              <text x="110" y="102" fill="${s.isCommutative ? '#34d399' : '#f87171'}" font-size="10.5" font-weight="700" text-anchor="middle">${s.resultB}</text>
            </g>

            <!-- Verdict Badge -->
            <rect x="50" y="215" width="440" height="32" rx="6" fill="${s.isCommutative ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)'}" stroke="${s.isCommutative ? '#10b981' : '#ef4444'}"/>
            <text x="270" y="236" fill="${s.isCommutative ? '#34d399' : '#f87171'}" font-size="12" font-weight="900" text-anchor="middle">
              ${s.isCommutative ? "COMMUTATIVE: Swapping the order preserved the outcome!" : "NON-COMMUTATIVE: Swapping the order broke the outcome!"}
            </text>

            <!-- Mathematical Parallel -->
            <rect x="35" y="258" width="470" height="55" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#fbbf24" stroke-width="1"/>
            <text x="270" y="278" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Mathematical Significance:</text>
            <text x="270" y="298" fill="#f8fafc" font-size="10" font-weight="600" text-anchor="middle">${s.mathParallel}</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Action:</span>
          ${scenarios.map((s, idx) => `<button class="sim-btn ${idx === activeItem ? 'active' : ''}" data-idx="${idx}">${s.name}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activeItem = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 8: Commutative & Associative Tile Array
    function simCommutativeAssociativeTile() {
      simHeaderTitle.textContent = "Commutative & Associative Tile Array Simulator";
      let mode = "comm"; // "comm" or "assoc"
      let isRotated = false;
      let assocGroup = 0; // 0: (2+3)+4, 1: 2+(3+4)

      function render() {
        if (mode === "comm") {
          const rows = isRotated ? 5 : 3;
          const cols = isRotated ? 3 : 5;
          const expr = isRotated ? "5 × 3 = 15" : "3 × 5 = 15";

          simCanvas.innerHTML = `
            <svg viewBox="0 0 540 330" width="100%" height="100%">
              <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

              <rect x="130" y="15" width="280" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Array Area: ${expr}</text>

              <!-- Tile Grid -->
              <g transform="translate(${270 - (cols * 40) / 2}, ${140 - (rows * 22) / 2})">
                ${Array.from({ length: rows }).map((_, r) =>
                  Array.from({ length: cols }).map((_, c) => `
                    <rect x="${c * 40}" y="${r * 22}" width="36" height="18" rx="3" fill="#3b82f6" stroke="#60a5fa" stroke-width="1"/>
                  `).join('')
                ).join('')}
              </g>

              <!-- Rotation Arrow & Info -->
              <rect x="50" y="250" width="440" height="60" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#10b981" stroke-width="1"/>
              <text x="270" y="274" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Commutative Law: a × b = b × a</text>
              <text x="270" y="295" fill="#94a3b8" font-size="10" text-anchor="middle">Rotating a rectangle array swaps its length and width, but the total count of tiles remains exactly 15!</text>
            </svg>
          `;
        } else {
          // Associative: (2 + 3) + 4 vs 2 + (3 + 4)
          const bracketLabel = assocGroup === 0 ? "( 2 + 3 ) + 4 = 5 + 4 = 9" : "2 + ( 3 + 4 ) = 2 + 7 = 9";

          simCanvas.innerHTML = `
            <svg viewBox="0 0 540 330" width="100%" height="100%">
              <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

              <rect x="100" y="15" width="340" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#a855f7" stroke-width="1.5"/>
              <text x="270" y="38" fill="#c084fc" font-size="14" font-weight="900" text-anchor="middle">${bracketLabel}</text>

              <!-- Grouping Visualizer -->
              <g transform="translate(60, 85)">
                <!-- Group 1: 2 tiles (Cyan) -->
                <rect x="0" y="20" width="80" height="50" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="40" y="50" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">2</text>

                <text x="100" y="52" fill="#94a3b8" font-size="20" font-weight="900">+</text>

                <!-- Group 2: 3 tiles (Amber) -->
                <rect x="120" y="20" width="120" height="50" rx="6" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
                <text x="180" y="50" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">3</text>

                <text x="260" y="52" fill="#94a3b8" font-size="20" font-weight="900">+</text>

                <!-- Group 3: 4 tiles (Emerald) -->
                <rect x="280" y="20" width="140" height="50" rx="6" fill="#059669" stroke="#34d399" stroke-width="2"/>
                <text x="350" y="50" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">4</text>

                <!-- Highlight bracket box around active grouping -->
                ${assocGroup === 0 ? `
                  <rect x="-10" y="10" width="260" height="70" rx="10" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6"/>
                  <text x="120" y="5" fill="#f43f5e" font-size="11" font-weight="800" text-anchor="middle">( Grouped First: 2 + 3 = 5 )</text>
                ` : `
                  <rect x="110" y="10" width="320" height="70" rx="10" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6"/>
                  <text x="270" y="5" fill="#f43f5e" font-size="11" font-weight="800" text-anchor="middle">( Grouped Second: 3 + 4 = 7 )</text>
                `}
              </g>

              <rect x="50" y="250" width="440" height="60" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#a855f7" stroke-width="1"/>
              <text x="270" y="274" fill="#c084fc" font-size="12" font-weight="800" text-anchor="middle">Associative Law: (a + b) + c = a + (b + c)</text>
              <text x="270" y="295" fill="#94a3b8" font-size="10" text-anchor="middle">Changing which adjacent pair is grouped first never changes the overall sum!</text>
            </svg>
          `;
        }
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnModeComm">Commutative Grid (3×5 vs 5×3)</button>
          <button class="sim-btn" id="btnRotateGrid">🔄 Rotate Array</button>
          <button class="sim-btn" id="btnModeAssoc">Associative Grouping ((a+b)+c)</button>
          <button class="sim-btn" id="btnToggleAssoc">🔀 Regroup Pairs</button>
        </div>
      `;

      document.getElementById('btnModeComm').onclick = () => {
        mode = "comm";
        document.getElementById('btnModeComm').classList.add('active');
        document.getElementById('btnModeAssoc').classList.remove('active');
        render(); sfx.playClick();
      };
      document.getElementById('btnRotateGrid').onclick = () => {
        mode = "comm";
        isRotated = !isRotated;
        document.getElementById('btnModeComm').classList.add('active');
        document.getElementById('btnModeAssoc').classList.remove('active');
        render(); sfx.playClick();
      };
      document.getElementById('btnModeAssoc').onclick = () => {
        mode = "assoc";
        document.getElementById('btnModeAssoc').classList.add('active');
        document.getElementById('btnModeComm').classList.remove('active');
        render(); sfx.playClick();
      };
      document.getElementById('btnToggleAssoc').onclick = () => {
        mode = "assoc";
        assocGroup = assocGroup === 0 ? 1 : 0;
        document.getElementById('btnModeAssoc').classList.add('active');
        document.getElementById('btnModeComm').classList.remove('active');
        render(); sfx.playClick();
      };

      render();
    }

    // Slide 9: Fraction Bar as Hidden Bracket
    function simFractionBarBracket() {
      simHeaderTitle.textContent = "The Vinculum: The Fraction Bar as a Hidden Bracket";
      let showBrackets = true;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <rect x="100" y="15" width="340" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Horizontal Fraction Bar (Vinculum)</text>

            <!-- Fraction Presentation -->
            <g transform="translate(140, 75)">
              <rect x="0" y="0" width="260" height="120" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#60a5fa" stroke-width="1.5"/>

              <!-- Numerator -->
              <text x="130" y="45" fill="${showBrackets ? '#38bdf8' : '#f8fafc'}" font-size="20" font-weight="900" text-anchor="middle">
                ${showBrackets ? "( 18 + 6 )" : "18 + 6"}
              </text>

              <!-- Vinculum Horizontal Bar -->
              <line x1="30" y1="62" x2="230" y2="62" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>

              <!-- Denominator -->
              <text x="130" y="95" fill="${showBrackets ? '#a855f7' : '#f8fafc'}" font-size="20" font-weight="900" text-anchor="middle">
                ${showBrackets ? "( 2 × 3 )" : "2 × 3"}
              </text>
            </g>

            <!-- Equivalence arrow and step -->
            <g transform="translate(100, 210)">
              <rect x="0" y="0" width="340" height="42" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#10b981" stroke-width="1.5"/>
              <text x="170" y="26" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">
                = ( 24 ) ÷ ( 6 ) = 4
              </text>
            </g>

            <!-- Warning Callout -->
            <rect x="30" y="265" width="480" height="52" rx="8" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="1"/>
            <text x="270" y="285" fill="#f87171" font-size="10.5" font-weight="800" text-anchor="middle">⚠️ Calculator Trap: Typing 18 + 6 ÷ 2 × 3 computes 18 + 3 × 3 = 27 !</text>
            <text x="270" y="303" fill="#cbd5e1" font-size="9.5" text-anchor="middle">You MUST explicitly add brackets: (18 + 6) ÷ (2 × 3) to get the true answer 4!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnToggleBrackets">👁 Reveal / Hide Hidden Brackets</button>
        </div>
      `;

      document.getElementById('btnToggleBrackets').onclick = () => {
        showBrackets = !showBrackets;
        render(); sfx.playClick();
      };

      render();
    }

    // Slide 10: Signed Terms on Number Line (Brahmagupta's Fortune & Debt)
    function simSignedTermsNumberline() {
      simHeaderTitle.textContent = "Brahmagupta's Fortune (Dhana) & Debt (Rina) on the Number Line";
      let currentVal = 0;
      let activePreset = 0;
      const presets = [
        { label: "+5 - 8 + 6", steps: [{ v: 5, t: "+5 (Dhana/Fortune)" }, { v: -8, t: "-8 (Rina/Debt)" }, { v: 6, t: "+6 (Dhana/Fortune)" }], target: 3 },
        { label: "+10 - 15 + 7", steps: [{ v: 10, t: "+10" }, { v: -15, t: "-15" }, { v: 7, t: "+7" }], target: 2 },
        { label: "-4 + 9 - 3", steps: [{ v: -4, t: "-4" }, { v: 9, t: "+9" }, { v: -3, t: "-3" }], target: 2 }
      ];

      let stepIdx = 0;
      let historyPositions = [0];

      function render() {
        const p = presets[activePreset];
        const val = historyPositions[stepIdx];

        // Number line bounds from -10 to +12
        const minN = -10, maxN = 12;
        const totalSpan = maxN - minN;
        const mapX = (n) => 40 + ((n - minN) / totalSpan) * 460;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="120" y="15" width="300" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Expression: ${p.label}</text>

            <!-- Number Line -->
            <g transform="translate(0, 150)">
              <!-- Axis Line -->
              <line x1="30" y1="0" x2="510" y2="0" stroke="#64748b" stroke-width="3"/>
              <!-- Arrow Heads -->
              <polygon points="30,0 42,-5 42,5" fill="#64748b"/>
              <polygon points="510,0 498,-5 498,5" fill="#64748b"/>

              <!-- Zero Marker -->
              <line x1="${mapX(0)}" y1="-15" x2="${mapX(0)}" y2="15" stroke="#f59e0b" stroke-width="3"/>
              <text x="${mapX(0)}" y="30" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">0</text>

              <!-- Ticks -->
              ${Array.from({ length: totalSpan + 1 }).map((_, i) => {
                const n = minN + i;
                if (n === 0) return '';
                const x = mapX(n);
                return `
                  <line x1="${x}" y1="-6" x2="${x}" y2="6" stroke="#475569" stroke-width="1.5"/>
                  ${n % 2 === 0 ? `<text x="${x}" y="20" fill="#94a3b8" font-size="9" text-anchor="middle">${n > 0 ? '+' + n : n}</text>` : ''}
                `;
              }).join('')}

              <!-- Hopping Token -->
              <circle cx="${mapX(val)}" cy="-20" r="14" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
              <text x="${mapX(val)}" y="-15" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">📍</text>
            </g>

            <!-- Position Display -->
            <rect x="70" y="70" width="400" height="50" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="92" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Current Position on Number Line</text>
            <text x="270" y="112" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">Position: ${val > 0 ? '+' + val : val} ${val > 0 ? '(Fortune)' : (val < 0 ? '(Debt)' : '(Neutral)')}</text>

            <!-- Ancient Indian Heritage Box -->
            <rect x="40" y="240" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1"/>
            <text x="270" y="262" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Acharya Brahmagupta's 7th-Century Principles:</text>
            <text x="270" y="280" fill="#e2e8f0" font-size="10" text-anchor="middle">"A fortune subtracted from zero is a debt, and a debt subtracted from zero is a fortune."</text>
            <text x="270" y="296" fill="#94a3b8" font-size="9.5" text-anchor="middle">Positive terms add wealth (move right); negative terms add debt (move left).</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnNextHop">Next Step 🦘</button>
          <button class="sim-btn" id="btnResetLine">🔄 Reset</button>
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8; margin-left:1rem;">Preset:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === 0 ? 'active' : ''}" data-idx="${idx}">${p.label}</button>`).join('')}
        </div>
      `;

      function computeHistory() {
        const p = presets[activePreset];
        historyPositions = [0];
        let running = 0;
        p.steps.forEach(st => {
          running += st.v;
          historyPositions.push(running);
        });
        stepIdx = 0;
      }

      computeHistory();

      document.getElementById('btnNextHop').onclick = () => {
        if (stepIdx < historyPositions.length - 1) {
          stepIdx++;
          render();
          sfx.playClick();
        }
      };

      document.getElementById('btnResetLine').onclick = () => {
        stepIdx = 0;
        render();
        sfx.playClick();
      };

      simControls.querySelectorAll('[data-idx]').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('[data-idx]').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          computeHistory();
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 11: Distributive Property Geometric Area Model
    function simDistributiveRectangleArea() {
      simHeaderTitle.textContent = "The Distributive Property: Split-Rectangle Geometric Model";
      let a = 4, b = 6, c = 3;

      function render() {
        const area1 = a * b;
        const area2 = a * c;
        const totalArea = a * (b + c);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Formula Banner -->
            <rect x="60" y="15" width="420" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              ${a} × ( ${b} + ${c} ) = ( ${a} × ${b} ) + ( ${a} × ${c} ) = ${totalArea}
            </text>

            <!-- Visual Split Rectangle -->
            <g transform="translate(100, 75)">
              <!-- Total Width Top Bracket -->
              <text x="170" y="15" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">Total Width: ${b} + ${c} = ${b + c}</text>
              <line x1="20" y1="22" x2="320" y2="22" stroke="#94a3b8" stroke-width="1.5"/>

              <!-- Height Left Label -->
              <text x="5" y="85" fill="#f59e0b" font-size="12" font-weight="900" text-anchor="middle">Height: ${a}</text>

              <!-- Rectangle 1: a * b (Cyan) -->
              <rect x="20" y="30" width="${(b / (b + c)) * 300}" height="110" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2"/>
              <text x="${20 + ((b / (b + c)) * 150)}" y="75" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Area 1</text>
              <text x="${20 + ((b / (b + c)) * 150)}" y="95" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${a} × ${b} = ${area1}</text>

              <!-- Rectangle 2: a * c (Emerald) -->
              <rect x="${20 + (b / (b + c)) * 300}" y="30" width="${(c / (b + c)) * 300}" height="110" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
              <text x="${20 + (b / (b + c)) * 300 + ((c / (b + c)) * 150)}" y="75" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Area 2</text>
              <text x="${20 + (b / (b + c)) * 300 + ((c / (b + c)) * 150)}" y="95" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${a} × ${c} = ${area2}</text>
            </g>

            <!-- Bottom Proof Box -->
            <rect x="50" y="245" width="440" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="268" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Geometric Proof: Both methods yield identical area</text>
            <text x="270" y="292" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">
              One Big Box: ${a} × ${b + c} = ${totalArea}  |  Two Split Boxes: ${area1} + ${area2} = ${totalArea}
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:1rem; justify-content:center; align-items:center;">
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Height (a): <input type="range" id="rngA" min="2" max="6" value="4"></label>
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Width 1 (b): <input type="range" id="rngB" min="3" max="8" value="6"></label>
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Width 2 (c): <input type="range" id="rngC" min="2" max="6" value="3"></label>
        </div>
      `;

      document.getElementById('rngA').oninput = (e) => { a = parseInt(e.target.value); render(); };
      document.getElementById('rngB').oninput = (e) => { b = parseInt(e.target.value); render(); };
      document.getElementById('rngC').oninput = (e) => { c = parseInt(e.target.value); render(); };

      render();
    }

    // Slide 12: Tinker the Terms (Friendly Tens & Hundreds)
    function simTinkerTermsFriendlyTens() {
      simHeaderTitle.textContent = "Tinker the Terms: Friendly Tens & Hundreds Mental Pairing";
      let paired = false;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="90" y="15" width="360" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Problem: 28 + 47 + 72 + 53</text>

            ${!paired ? `
              <!-- Unpaired View -->
              <g transform="translate(60, 80)">
                <rect x="0" y="0" width="90" height="70" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
                <text x="45" y="42" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">28</text>

                <text x="105" y="42" fill="#94a3b8" font-size="20" font-weight="900">+</text>

                <rect x="120" y="0" width="90" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                <text x="165" y="42" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">47</text>

                <text x="225" y="42" fill="#94a3b8" font-size="20" font-weight="900">+</text>

                <rect x="240" y="0" width="90" height="70" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
                <text x="285" y="42" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">72</text>

                <text x="345" y="42" fill="#94a3b8" font-size="20" font-weight="900">+</text>

                <rect x="360" y="0" width="90" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                <text x="405" y="42" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">53</text>
              </g>

              <rect x="50" y="210" width="440" height="90" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#64748b" stroke-width="1.5"/>
              <text x="270" y="240" fill="#94a3b8" font-size="12" font-weight="800" text-anchor="middle">Unpaired Standard Calculation (Slow):</text>
              <text x="270" y="265" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle">28 + 47 = 75, then 75 + 72 = 147, then 147 + 53 = 200</text>
              <text x="270" y="285" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Can we rearrange the terms using Commutative Law to make it fast?</text>
            ` : `
              <!-- Paired View -->
              <g transform="translate(60, 80)">
                <!-- Pair 1: 28 + 72 -->
                <rect x="0" y="0" width="190" height="70" rx="10" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
                <text x="95" y="25" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Friendly Pair 1 (Sum = 100)</text>
                <text x="95" y="52" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">( 28 + 72 )</text>

                <text x="210" y="42" fill="#94a3b8" font-size="24" font-weight="900">+</text>

                <!-- Pair 2: 47 + 53 -->
                <rect x="230" y="0" width="190" height="70" rx="10" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2"/>
                <text x="325" y="25" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Friendly Pair 2 (Sum = 100)</text>
                <text x="325" y="52" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">( 47 + 53 )</text>
              </g>

              <rect x="50" y="200" width="440" height="100" rx="10" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2"/>
              <text x="270" y="230" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">⚡ Mental Math Lightning Shortcut!</text>
              <text x="270" y="258" fill="#f8fafc" font-size="18" font-weight="900" text-anchor="middle">= 100 + 100 = 200</text>
              <text x="270" y="282" fill="#a7f3d0" font-size="11" font-weight="700" text-anchor="middle">By tinkering and grouping terms that complement each other to 100, we solve it in seconds!</text>
            `}
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${!paired ? 'active' : ''}" id="btnUnpaired">Standard Order</button>
          <button class="sim-btn ${paired ? 'active' : ''}" id="btnPaired">⚡ Group Friendly Pairs (100)</button>
        </div>
      `;

      document.getElementById('btnUnpaired').onclick = () => {
        paired = false;
        document.getElementById('btnUnpaired').classList.add('active');
        document.getElementById('btnPaired').classList.remove('active');
        render(); sfx.playClick();
      };

      document.getElementById('btnPaired').onclick = () => {
        paired = true;
        document.getElementById('btnPaired').classList.add('active');
        document.getElementById('btnUnpaired').classList.remove('active');
        render(); sfx.playClick();
      };

      render();
    }

    // Slide 13: Removing Brackets: Minus Sign Inversion Switch
    function simMinusBracketSignFlip() {
      simHeaderTitle.textContent = "Removing Brackets: The Minus Sign Inversion Switch";
      let isRemoved = false;
      let activePreset = 0;
      const presets = [
        { orig: "-( 7 + 5 )", inside: "+7 + 5", flipped: "-7 - 5", val: -12 },
        { orig: "-( 9 - 4 )", inside: "+9 - 4", flipped: "-9 + 4", val: -5 },
        { orig: "15 - ( 8 - 3 )", inside: "15 - (+8 - 3)", flipped: "15 - 8 + 3", val: 10 }
      ];

      function render() {
        const p = presets[activePreset];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <rect x="90" y="15" width="360" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Expression: ${p.orig}</text>

            <!-- Bracket Switch Display -->
            <g transform="translate(70, 75)">
              <rect x="0" y="0" width="400" height="120" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="${isRemoved ? '#10b981' : '#f43f5e'}" stroke-width="2"/>

              ${!isRemoved ? `
                <text x="200" y="35" fill="#f43f5e" font-size="12" font-weight="800" text-anchor="middle">Preceded by Minus Sign (-): Guard is Active!</text>
                <text x="200" y="75" fill="#ffffff" font-size="24" font-weight="900" text-anchor="middle">${p.orig}</text>
                <text x="200" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">Click "Flip Sign & Remove Bracket" below to watch each sign invert!</text>
              ` : `
                <text x="200" y="35" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Bracket Removed: Every Internal Sign Inverted!</text>
                <text x="200" y="75" fill="#f8fafc" font-size="24" font-weight="900" text-anchor="middle">${p.flipped} = ${p.val}</text>
                <text x="200" y="105" fill="#a7f3d0" font-size="10" text-anchor="middle">Minus distributed to every term like multiplying by -1.</text>
              `}
            </g>

            <!-- Bottom Law Card -->
            <rect x="40" y="225" width="460" height="85" rx="10" fill="rgba(30, 41, 59, 0.85)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="248" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">Universal Bracket Removal Rules:</text>
            <text x="270" y="272" fill="#e2e8f0" font-size="11" font-weight="700" text-anchor="middle">+( a + b ) = a + b  and  +( a - b ) = a - b (Signs remain unchanged)</text>
            <text x="270" y="294" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">-( a + b ) = -a - b  and  -( a - b ) = -a + b (EVERY sign flips!)</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnToggleFlip">🔄 ${isRemoved ? 'Restore Bracket' : 'Flip Sign & Remove Bracket'}</button>
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8; margin-left:1rem;">Presets:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.orig}</button>`).join('')}
        </div>
      `;

      document.getElementById('btnToggleFlip').onclick = () => {
        isRemoved = !isRemoved;
        document.getElementById('btnToggleFlip').textContent = isRemoved ? 'Restore Bracket' : 'Flip Sign & Remove Bracket';
        render(); sfx.playClick();
      };

      simControls.querySelectorAll('[data-idx]').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('[data-idx]').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          isRemoved = false;
          document.getElementById('btnToggleFlip').textContent = 'Flip Sign & Remove Bracket';
          render(); sfx.playClick();
        });
      });

      render();
    }

    // Slide 14: Nested Brackets Unpacker
    function simNestedBracketsUnpacker() {
      simHeaderTitle.textContent = "Excavation of Nested Brackets: ( ) then { } then [ ]";
      let layer = 0;
      const layers = [
        {
          name: "Original Expression",
          disp: "50 - [ 20 + { 15 - ( 6 + 3 ) } ]",
          desc: "Three layers of nesting. Target the innermost round brackets first: ( 6 + 3 )",
          activeColor: "#38bdf8"
        },
        {
          name: "Layer 1: Innermost ( ) Solved",
          disp: "50 - [ 20 + { 15 - 9 } ]",
          desc: "( 6 + 3 ) evaluated to 9. Now target curly braces: { 15 - 9 }",
          activeColor: "#fbbf24"
        },
        {
          name: "Layer 2: Curly Braces { } Solved",
          disp: "50 - [ 20 + 6 ]",
          desc: "{ 15 - 9 } evaluated to 6. Now target square brackets: [ 20 + 6 ]",
          activeColor: "#a855f7"
        },
        {
          name: "Layer 3: Square Brackets [ ] Solved",
          disp: "50 - 26 = 24",
          desc: "[ 20 + 6 ] evaluated to 26. Final subtraction: 50 - 26 = 24!",
          activeColor: "#10b981"
        }
      ];

      function render() {
        const l = layers[layer];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="80" y="15" width="380" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">BODMAS Hierarchy: Parentheses ➔ Braces ➔ Brackets</text>

            <!-- Nested Visual Concentric Boxes -->
            <g transform="translate(50, 70)">
              <!-- Square Bracket Box -->
              <rect x="0" y="0" width="440" height="140" rx="12" fill="rgba(168, 85, 247, 0.08)" stroke="#a855f7" stroke-width="2"/>
              <text x="20" y="25" fill="#c084fc" font-size="11" font-weight="800">[ Square Brackets: Outer Layer ]</text>

              <!-- Curly Brace Box -->
              <rect x="140" y="35" width="280" height="90" rx="10" fill="rgba(245, 158, 11, 0.1)" stroke="#f59e0b" stroke-width="2"/>
              <text x="155" y="55" fill="#fbbf24" font-size="10" font-weight="800">{ Curly Braces: Middle Layer }</text>

              <!-- Parentheses Box -->
              <rect x="250" y="65" width="150" height="50" rx="8" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2"/>
              <text x="260" y="85" fill="#38bdf8" font-size="9" font-weight="800">( Parentheses: Innermost )</text>
              <text x="325" y="103" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${layer === 0 ? "6 + 3" : "= 9"}</text>

              <text x="50" y="85" fill="#ffffff" font-size="15" font-weight="800">20 +</text>
              <text x="180" y="95" fill="#ffffff" font-size="15" font-weight="800">15 -</text>
            </g>

            <!-- Current Stage Callout -->
            <rect x="40" y="230" width="460" height="80" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="${l.activeColor}" stroke-width="2"/>
            <text x="270" y="252" fill="${l.activeColor}" font-size="12" font-weight="800" text-anchor="middle">${l.name}</text>
            <text x="270" y="278" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">${l.disp}</text>
            <text x="270" y="298" fill="#94a3b8" font-size="9.5" text-anchor="middle">${l.desc}</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnUnpackPrev">⏮ Previous Layer</button>
          <span id="layerIndicator" style="font-weight:700; color:#38bdf8; font-size:0.95rem;">Layer 1 of 4</span>
          <button class="sim-btn active" id="btnUnpackNext">Next Layer ⏭</button>
          <button class="sim-btn" id="btnUnpackReset">🔄 Reset</button>
        </div>
      `;

      function updateControls() {
        document.getElementById('layerIndicator').textContent = `Layer ${layer + 1} of ${layers.length}`;
        document.getElementById('btnUnpackPrev').disabled = (layer === 0);
        document.getElementById('btnUnpackNext').disabled = (layer === layers.length - 1);
      }

      document.getElementById('btnUnpackPrev').onclick = () => {
        if (layer > 0) { layer--; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnUnpackNext').onclick = () => {
        if (layer < layers.length - 1) { layer++; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnUnpackReset').onclick = () => {
        layer = 0; render(); updateControls(); sfx.playClick();
      };

      render();
      updateControls();
    }

    // Slide 15: Word Problem Expression Builder
    function simWordProblemExpressionBuilder() {
      simHeaderTitle.textContent = "Real-World Expression Architect: Picnic & School Supply Budget";
      let activeScenario = 0;
      const scenarios = [
        {
          title: "School Field Trip Vans",
          story: "A school hires 5 vans. In each van, there are 8 boys and 6 girls.",
          formula: "5 × ( 8 + 6 )",
          step1: "In each van: 8 + 6 = 14 students",
          step2: "Across 5 vans: 5 × 14 = 70 students total",
          val: 70
        },
        {
          title: "Book & Pen Shopping with Coupon",
          story: "Rohan buys 4 notebooks at ₹25 each and 3 pens at ₹10 each. He has a ₹15 discount coupon.",
          formula: "( 4 × 25 + 3 × 10 ) - 15",
          step1: "Items cost: (100 + 30) = ₹130",
          step2: "After discount: 130 - 15 = ₹115 to pay",
          val: 115
        },
        {
          title: "Cupcake Bakery Boxes",
          story: "Baker makes 6 trays of 12 cupcakes. 8 are kept on display. The rest are packed equally into 4 boxes.",
          formula: "( 6 × 12 - 8 ) ÷ 4",
          step1: "Remaining cupcakes: 72 - 8 = 64 cupcakes",
          step2: "Per box: 64 ÷ 4 = 16 cupcakes in each box",
          val: 16
        }
      ];

      function render() {
        const s = scenarios[activeScenario];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <rect x="80" y="15" width="380" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Story: ${s.title}</text>

            <!-- Story Description Box -->
            <rect x="40" y="65" width="460" height="55" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#64748b"/>
            <text x="270" y="88" fill="#cbd5e1" font-size="10.5" font-weight="600" text-anchor="middle">${s.story}</text>
            <text x="270" y="106" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">How do we translate this story into a single mathematical expression?</text>

            <!-- Constructed Expression Card -->
            <rect x="50" y="135" width="440" height="65" rx="10" fill="rgba(30, 41, 59, 0.95)" stroke="#38bdf8" stroke-width="2"/>
            <text x="270" y="158" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Mathematical Expression Model</text>
            <text x="270" y="186" fill="#f8fafc" font-size="20" font-weight="900" text-anchor="middle">${s.formula}</text>

            <!-- Evaluation Steps -->
            <g transform="translate(60, 215)">
              <rect x="0" y="0" width="420" height="95" rx="10" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1.5"/>
              <text x="210" y="24" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Step-by-Step Evaluation:</text>
              <text x="210" y="48" fill="#cbd5e1" font-size="11" font-weight="700" text-anchor="middle">${s.step1}</text>
              <text x="210" y="70" fill="#f8fafc" font-size="11" font-weight="800" text-anchor="middle">${s.step2}</text>
              <text x="210" y="88" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">Final Answer = ${s.val}</text>
            </g>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Story:</span>
          ${scenarios.map((s, idx) => `<button class="sim-btn ${idx === activeScenario ? 'active' : ''}" data-idx="${idx}">${s.title}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activeScenario = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 16: The 24 Puzzle Game & Four 4s Challenge
    function simArithmeticPuzzle24Game() {
      simHeaderTitle.textContent = "The Grand Arithmetic Challenge: The 24 Puzzle Game";
      let activePuzzle = 0;
      let userExpr = "";
      const puzzles = [
        { numbers: [4, 6, 8, 2], solution: "( 8 - 4 ) × 6 = 24", hint: "Subtract 4 from 8, then multiply by 6!" },
        { numbers: [3, 3, 8, 8], solution: "8 ÷ ( 3 - 8 ÷ 3 ) = 24", hint: "Ancient fraction trick: 3 - 8/3 = 1/3, and 8 ÷ (1/3) = 24!" },
        { numbers: [1, 2, 3, 4], solution: "1 × 2 × 3 × 4 = 24", hint: "Direct continuous product: 1 × 2 = 2, 2 × 3 = 6, 6 × 4 = 24!" },
        { numbers: [4, 4, 4, 4], solution: "( 4 × 4 ) + 4 + 4 = 24", hint: "Four 4s challenge: 16 + 4 + 4 = 24!" }
      ];

      function render() {
        const p = puzzles[activePuzzle];
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Header Badge -->
            <rect x="110" y="15" width="320" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="38" fill="#fbbf24" font-size="14" font-weight="900" text-anchor="middle">Goal: Combine Numbers to Reach 24!</text>

            <!-- Given Numbers -->
            <g transform="translate(60, 65)">
              <text x="210" y="15" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Your 4 Numbers to Use Exactly Once:</text>
              ${p.numbers.map((num, i) => `
                <rect x="${i * 105 + 10}" y="25" width="85" height="55" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <text x="${i * 105 + 52}" y="62" fill="#ffffff" font-size="22" font-weight="900" text-anchor="middle">${num}</text>
              `).join('')}
            </g>

            <!-- Working Display -->
            <rect x="60" y="165" width="420" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#3b82f6" stroke-width="2"/>
            <text x="270" y="188" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Working Expression:</text>
            <text id="calcWorking" x="270" y="214" fill="#f8fafc" font-size="17" font-weight="900" text-anchor="middle">${userExpr || "Use buttons below or reveal secret solution"}</text>

            <!-- Solution Callout Box -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="268" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">💡 Solution Formula:</text>
            <text x="270" y="290" fill="#f8fafc" font-size="15" font-weight="900" text-anchor="middle">${p.solution}</text>
            <text x="270" y="306" fill="#94a3b8" font-size="9" text-anchor="middle">Hint: ${p.hint}</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Puzzle:</span>
          ${puzzles.map((p, idx) => `<button class="sim-btn ${idx === activePuzzle ? 'active' : ''}" data-idx="${idx}">Puzzle ${idx + 1} [${p.numbers.join(',')}]</button>`).join('')}
          <button class="sim-btn" id="btnRevealSol">✨ Reveal Solution</button>
        </div>
      `;

      simControls.querySelectorAll('[data-idx]').forEach(btn => {
        btn.addEventListener('click', () => {
          activePuzzle = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('[data-idx]').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          userExpr = "";
          render();
          sfx.playClick();
        });
      });

      document.getElementById('btnRevealSol').onclick = () => {
        userExpr = puzzles[activePuzzle].solution;
        render();
        sfx.playCelebration();
      };

      render();
    }
""";


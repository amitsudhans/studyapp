# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 7 Mathematics: Chapter 7 - Finding the Unknown
JavaScript Simulator Engine
"""

SIMULATORS_JS = r"""
// Master Simulator Dispatcher for Chapter 7: Finding the Unknown
function initSimulatorForSlide(slideId, container) {
  if (!container) return;
  switch (slideId) {
    case 1: initMysterySackScaleSim(container); break;
    case 2: initBalanceOpsSim(container); break;
    case 3: initMatchstickPatternSim(container); break;
    case 4: initEquationAnatomySim(container); break;
    case 5: initTrialErrorTesterSim(container); break;
    case 6: initAddSubtractMachineSim(container); break;
    case 7: initMulDivIsolatorSim(container); break;
    case 8: initTwoStepUnwrapperSim(container); break;
    case 9: initTranspositionBridgeSim(container); break;
    case 10: initDualPanVariablesSim(container); break;
    case 11: initGeomWordProblemSim(container); break;
    case 12: initBudgetMagicTrickSim(container); break;
    case 13: initTranspositionTrapSim(container); break;
    case 14: initDistribDivisionTrapSim(container); break;
    case 15: initBijaganitaTimelineSim(container); break;
    case 16: initBrahmaguptaLinearSolverSim(container); break;
  }
}

// -------------------------------------------------------------
// 1. Mystery Sack & Balance Scale Simulator
// -------------------------------------------------------------
function initMysterySackScaleSim(container) {
  const svg = container.querySelector('#sackScaleSvg');
  const slider = container.querySelector('#sackWeightSlider');
  const weightVal = container.querySelector('#sackWeightVal');
  const statusSpan = container.querySelector('#sackScaleStatus');
  if (!svg || !slider) return;

  function render() {
    const x = parseInt(slider.value, 10);
    if (weightVal) weightVal.textContent = x + ' kg';

    const lhsWeight = x + 3;
    const rhsWeight = 8;
    const diff = lhsWeight - rhsWeight;

    // Angle of tilt: max +- 12 degrees
    const tiltAngle = Math.max(-12, Math.min(12, diff * 3));
    const rad = (tiltAngle * Math.PI) / 180;

    if (statusSpan) {
      if (diff === 0) {
        statusSpan.textContent = "BALANCED (8 kg = 8 kg) ✔";
        statusSpan.className = "text-emerald-400 font-bold font-mono";
      } else if (diff < 0) {
        statusSpan.textContent = `TILTED RIGHT (LHS ${lhsWeight}kg < RHS 8kg)`;
        statusSpan.className = "text-amber-400 font-bold font-mono";
      } else {
        statusSpan.textContent = `TILTED LEFT (LHS ${lhsWeight}kg > RHS 8kg)`;
        statusSpan.className = "text-rose-400 font-bold font-mono";
      }
    }

    const fulcrumX = 250, fulcrumY = 160;
    const armLen = 140;

    const leftX = fulcrumX - armLen * Math.cos(rad);
    const leftY = fulcrumY - armLen * Math.sin(rad);
    const rightX = fulcrumX + armLen * Math.cos(rad);
    const rightY = fulcrumY + armLen * Math.sin(rad);

    svg.innerHTML = `
      <!-- Stand Base -->
      <polygon points="210,270 290,270 260,170 240,170" fill="#334155" stroke="#475569" stroke-width="2" />
      <circle cx="${fulcrumX}" cy="${fulcrumY}" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
      
      <!-- Balance Beam -->
      <line x1="${leftX}" y1="${leftY}" x2="${rightX}" y2="${rightY}" stroke="#94a3b8" stroke-width="6" stroke-linecap="round" />
      
      <!-- Center Pointer -->
      <line x1="${fulcrumX}" y1="${fulcrumY}" x2="${fulcrumX + 35 * Math.sin(rad)}" y2="${fulcrumY - 35 * Math.cos(rad)}" stroke="#ef4444" stroke-width="2.5" />
      
      <!-- Left Pan Strings & Pan -->
      <line x1="${leftX}" y1="${leftY}" x2="${leftX - 35}" y2="${leftY + 60}" stroke="#64748b" stroke-width="1.5" />
      <line x1="${leftX}" y1="${leftY}" x2="${leftX + 35}" y2="${leftY + 60}" stroke="#64748b" stroke-width="1.5" />
      <path d="M ${leftX - 45} ${leftY + 60} Q ${leftX} ${leftY + 75} ${leftX + 45} ${leftY + 60} Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      
      <!-- Right Pan Strings & Pan -->
      <line x1="${rightX}" y1="${rightY}" x2="${rightX - 35}" y2="${rightY + 60}" stroke="#64748b" stroke-width="1.5" />
      <line x1="${rightX}" y1="${rightY}" x2="${rightX + 35}" y2="${rightY + 60}" stroke="#64748b" stroke-width="1.5" />
      <path d="M ${rightX - 45} ${rightY + 60} Q ${rightX} ${rightY + 75} ${rightX + 45} ${rightY + 60} Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      
      <!-- Items on Left Pan: Mystery Sack x + 3kg brass -->
      <!-- Sack -->
      <path d="M ${leftX - 30} ${leftY + 58} C ${leftX - 35} ${leftY + 25}, ${leftX - 10} ${leftY + 15}, ${leftX - 5} ${leftY + 20} C ${leftX} ${leftY + 15}, ${leftX + 25} ${leftY + 25}, ${leftX + 20} ${leftY + 58} Z" fill="#b45309" stroke="#f59e0b" stroke-width="2" />
      <circle cx="${leftX - 5}" cy="${leftY + 20}" r="3" fill="#fde68a" />
      <text x="${leftX - 12}" y="${leftY + 45}" fill="#ffffff" font-size="14" font-weight="extrabold">x</text>
      
      <!-- 3kg Brass Weight -->
      <rect x="${leftX + 15}" y="${leftY + 38}" width="20" height="20" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
      <text x="${leftX + 18}" y="${leftY + 52}" fill="#ffffff" font-size="10" font-weight="bold">3kg</text>
      
      <!-- Items on Right Pan: 8kg Brass Weight -->
      <rect x="${rightX - 25}" y="${rightY + 25}" width="50" height="35" rx="4" fill="#059669" stroke="#34d399" stroke-width="2" />
      <text x="${rightX - 16}" y="${rightY + 47}" fill="#ffffff" font-size="14" font-weight="extrabold">8 kg</text>
      
      <!-- Equation Tag -->
      <text x="30" y="35" fill="#fde047" font-size="13" font-weight="bold">Equation Model: x + 3 = 8</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Left Pan Weight: ${lhsWeight} kg | Right Pan Weight: 8 kg</text>
      <text x="30" y="75" fill="#38bdf8" font-size="11">Subtract 3 from both sides: x = 8 - 3 = 5 kg</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 2. Balance Operations Simulator
// -------------------------------------------------------------
function initBalanceOpsSim(container) {
  const svg = container.querySelector('#balanceOpsSvg');
  const opBtns = container.querySelectorAll('.balOpBtn');
  const resetBtn = container.querySelector('#balResetBtn');
  const eqText = container.querySelector('#balanceEquationText');
  const badge = container.querySelector('#balanceOpsBadge');
  if (!svg) return;

  let lhs = 10;
  let rhs = 10;

  function render() {
    const diff = lhs - rhs;
    const tiltAngle = Math.max(-14, Math.min(14, diff * 2));
    const rad = (tiltAngle * Math.PI) / 180;

    if (eqText) eqText.textContent = `LHS: ${lhs} kg | RHS: ${rhs} kg`;

    if (badge) {
      if (diff === 0) {
        badge.textContent = "BALANCED (LHS = RHS)";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
      } else {
        badge.textContent = "UNBALANCED! (Equality Broken)";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
      }
    }

    const fx = 250, fy = 160;
    const arm = 140;
    const lx = fx - arm * Math.cos(rad);
    const ly = fy - arm * Math.sin(rad);
    const rx = fx + arm * Math.cos(rad);
    const ry = fy + arm * Math.sin(rad);

    svg.innerHTML = `
      <!-- Stand Base -->
      <polygon points="210,270 290,270 260,170 240,170" fill="#334155" stroke="#475569" stroke-width="2" />
      <circle cx="${fx}" cy="${fy}" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
      
      <!-- Balance Beam -->
      <line x1="${lx}" y1="${ly}" x2="${rx}" y2="${ry}" stroke="#94a3b8" stroke-width="6" stroke-linecap="round" />
      
      <!-- Left Pan -->
      <line x1="${lx}" y1="${ly}" x2="${lx - 35}" y2="${ly + 60}" stroke="#64748b" stroke-width="1.5" />
      <line x1="${lx}" y1="${ly}" x2="${lx + 35}" y2="${ly + 60}" stroke="#64748b" stroke-width="1.5" />
      <path d="M ${lx - 45} ${ly + 60} Q ${lx} ${ly + 75} ${lx + 45} ${ly + 60} Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      <rect x="${lx - 25}" y="${ly + 25}" width="50" height="35" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="2" />
      <text x="${lx - 16}" y="${ly + 47}" fill="#ffffff" font-size="14" font-weight="extrabold">${lhs} kg</text>
      
      <!-- Right Pan -->
      <line x1="${rx}" y1="${ry}" x2="${rx - 35}" y2="${ry + 60}" stroke="#64748b" stroke-width="1.5" />
      <line x1="${rx}" y1="${ry}" x2="${rx + 35}" y2="${ry + 60}" stroke="#64748b" stroke-width="1.5" />
      <path d="M ${rx - 45} ${ry + 60} Q ${rx} ${ry + 75} ${rx + 45} ${ry + 60} Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      <rect x="${rx - 25}" y="${ry + 25}" width="50" height="35" rx="4" fill="#10b981" stroke="#047857" stroke-width="2" />
      <text x="${rx - 16}" y="${ry + 47}" fill="#ffffff" font-size="14" font-weight="extrabold">${rhs} kg</text>
      
      <!-- Status Notice -->
      <text x="30" y="35" fill="#f8fafc" font-size="12" font-weight="bold">The Balance Invariant Law:</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Identical operations on both sides preserve equilibrium.</text>
      <text x="30" y="75" fill="${diff === 0 ? '#34d399' : '#f87171'}" font-size="12" font-weight="bold">
        ${diff === 0 ? 'Equilibrium Maintained: LHS = RHS' : 'Warning: Unilateral change destroyed balance!'}
      </text>
    `;
  }

  opBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const op = btn.dataset.op;
      if (op === 'addBoth') { lhs += 2; rhs += 2; }
      else if (op === 'subBoth') { lhs = Math.max(0, lhs - 2); rhs = Math.max(0, rhs - 2); }
      else if (op === 'mulBoth') { lhs *= 2; rhs *= 2; }
      else if (op === 'addLeft') { lhs += 3; }
      render();
    });
  });

  if (resetBtn) resetBtn.addEventListener('click', () => { lhs = 10; rhs = 10; render(); });
  render();
}

// -------------------------------------------------------------
// 3. Matchstick Linear Sequencer Simulator
// -------------------------------------------------------------
function initMatchstickPatternSim(container) {
  const svg = container.querySelector('#matchstickSvg');
  const slider = container.querySelector('#matchstickSlider');
  const nVal = container.querySelector('#matchstickNVal');
  const totalVal = container.querySelector('#matchstickTotalVal');
  if (!svg || !slider) return;

  function render() {
    const n = parseInt(slider.value, 10);
    const sticks = 2 * n + 1;
    if (nVal) nVal.textContent = `n = ${n}`;
    if (totalVal) totalVal.textContent = `S = 2(${n}) + 1 = ${sticks} sticks`;

    const baseY = 210;
    const topY = 120;
    const sideW = 45;
    const startX = 40;

    let content = `
      <text x="30" y="35" fill="#fde047" font-size="13" font-weight="bold">Linear Expression Model: Total Sticks S = 2n + 1</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Unit 1: 3 sticks | Each extra triangle: +2 sticks</text>
    `;

    // Draw baseline stick 1 (the initial vertical or base)
    // Triangles pattern: base line stick (0 to sideW), then zigzags
    // Standard connected triangle chain:
    // Vertices: V0=(x, baseY), V1=(x+w/2, topY), V2=(x+w, baseY), V3=(x+1.5w, topY), ...
    for (let i = 0; i < n; i++) {
      const x0 = startX + i * sideW;
      const x1 = startX + (i + 0.5) * sideW;
      const x2 = startX + (i + 1) * sideW;

      // Base stick (horizontal)
      content += `
        <!-- Base stick ${i+1} -->
        <line x1="${x0}" y1="${baseY}" x2="${x2}" y2="${baseY}" stroke="#b45309" stroke-width="4" stroke-linecap="round" />
        <circle cx="${x2}" cy="${baseY}" r="3.5" fill="#ef4444" />
      `;

      // Upward side stick
      if (i === 0) {
        // First left side stick
        content += `
          <line x1="${x0}" y1="${baseY}" x2="${x1}" y2="${topY}" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
          <circle cx="${x1}" cy="${topY}" r="3.5" fill="#ef4444" />
        `;
      }
      // Right side stick
      content += `
        <line x1="${x1}" y1="${topY}" x2="${x2}" y2="${baseY}" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
        <circle cx="${x2}" cy="${baseY}" r="3.5" fill="#ef4444" />
      `;
      if (i < n - 1) {
        const nextTopX = startX + (i + 1.5) * sideW;
        content += `
          <line x1="${x2}" y1="${baseY}" x2="${nextTopX}" y2="${topY}" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
          <circle cx="${nextTopX}" cy="${topY}" r="3.5" fill="#ef4444" />
        `;
      }

      // Triangle label
      content += `<text x="${x1 - 5}" y="${baseY - 25}" fill="#67e8f9" font-size="11" font-weight="bold">#${i+1}</text>`;
    }

    // Table preview on right
    content += `
      <g transform="translate(350, 80)">
        <rect x="0" y="0" width="120" height="150" fill="#0f172a" stroke="#334155" rx="6" />
        <text x="15" y="22" fill="#38bdf8" font-size="11" font-weight="bold">n (Triangles)</text>
        <text x="75" y="22" fill="#34d399" font-size="11" font-weight="bold">S (Sticks)</text>
        <line x1="5" y1="28" x2="115" y2="28" stroke="#334155" />
        <text x="30" y="48" fill="#94a3b8" font-size="10">1</text><text x="85" y="48" fill="#cbd5e1" font-size="10">3</text>
        <text x="30" y="68" fill="#94a3b8" font-size="10">2</text><text x="85" y="68" fill="#cbd5e1" font-size="10">5</text>
        <text x="30" y="88" fill="#94a3b8" font-size="10">3</text><text x="85" y="88" fill="#cbd5e1" font-size="10">7</text>
        <text x="30" y="108" fill="#94a3b8" font-size="10">4</text><text x="85" y="108" fill="#cbd5e1" font-size="10">9</text>
        <text x="25" y="132" fill="#fde047" font-size="11" font-weight="bold">n</text>
        <text x="65" y="132" fill="#fde047" font-size="11" font-weight="bold">2n + 1</text>
      </g>
    `;

    svg.innerHTML = content;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 4. Equation Anatomy Seesaw Simulator
// -------------------------------------------------------------
function initEquationAnatomySim(container) {
  const svg = container.querySelector('#anatomySvg');
  const slider = container.querySelector('#anatomyXSlider');
  const xVal = container.querySelector('#anatomyXVal');
  const evalSpan = container.querySelector('#anatomyEvaluation');
  if (!svg || !slider) return;

  function render() {
    const x = parseInt(slider.value, 10);
    const lhs = 3 * x + 4;
    const rhs = 19;
    const diff = lhs - rhs;

    if (xVal) xVal.textContent = `x = ${x}`;
    if (evalSpan) {
      if (diff === 0) {
        evalSpan.textContent = `LHS: 3(${x}) + 4 = 19 = RHS (EQUAL!) ✔`;
        evalSpan.className = "text-emerald-400 font-bold font-mono";
      } else {
        evalSpan.textContent = `LHS: 3(${x}) + 4 = ${lhs} ≠ 19 (RHS)`;
        evalSpan.className = "text-rose-400 font-bold font-mono";
      }
    }

    const tiltAngle = Math.max(-12, Math.min(12, diff * 1.5));
    const rad = (tiltAngle * Math.PI) / 180;
    const fx = 250, fy = 160;
    const arm = 140;
    const lx = fx - arm * Math.cos(rad);
    const ly = fy - arm * Math.sin(rad);
    const rx = fx + arm * Math.cos(rad);
    const ry = fy + arm * Math.sin(rad);

    svg.innerHTML = `
      <!-- Fulcrum -->
      <polygon points="220,260 280,260 255,170 245,170" fill="#334155" stroke="#475569" stroke-width="2" />
      <circle cx="${fx}" cy="${fy}" r="7" fill="#c084fc" />
      <text x="${fx - 5}" y="${fy + 4}" fill="#ffffff" font-size="10" font-weight="bold">=</text>
      
      <!-- Beam -->
      <line x1="${lx}" y1="${ly}" x2="${rx}" y2="${ry}" stroke="#94a3b8" stroke-width="6" stroke-linecap="round" />
      
      <!-- Left Pan (LHS Box) -->
      <rect x="${lx - 50}" y="${ly - 45}" width="100" height="40" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2" />
      <text x="${lx - 35}" y="${ly - 28}" fill="#818cf8" font-size="10" font-weight="bold">LHS Expression</text>
      <text x="${lx - 38}" y="${ly - 12}" fill="#ffffff" font-size="13" font-weight="bold">3x + 4 = ${lhs}</text>
      
      <!-- Right Pan (RHS Box) -->
      <rect x="${rx - 50}" y="${ry - 45}" width="100" height="40" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="${rx - 35}" y="${ry - 28}" fill="#34d399" font-size="10" font-weight="bold">RHS Expression</text>
      <text x="${rx - 15}" y="${ry - 12}" fill="#ffffff" font-size="13" font-weight="bold">19</text>
      
      <!-- Equation Banner -->
      <text x="30" y="35" fill="#c084fc" font-size="13" font-weight="bold">Equation Anatomy: 3x + 4 = 19</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Only x = 5 satisfies LHS = RHS. Any other value tilts the equality seesaw!</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 5. Trial-and-Error Needle Meter Simulator
// -------------------------------------------------------------
function initTrialErrorTesterSim(container) {
  const svg = container.querySelector('#trialMeterSvg');
  const slider = container.querySelector('#trialXSlider');
  const xVal = container.querySelector('#trialXVal');
  const lhsText = container.querySelector('#trialLhsText');
  const badge = container.querySelector('#trialVerdictBadge');
  if (!svg || !slider) return;

  function render() {
    const x = parseInt(slider.value, 10);
    const lhs = 4 * x - 3;
    const rhs = 13;
    const gap = lhs - rhs;

    if (xVal) xVal.textContent = `x = ${x}`;
    if (lhsText) {
      lhsText.textContent = `4(${x}) - 3 = ${lhs} ${gap === 0 ? '(MATCH! Solution Found)' : gap < 0 ? '(Too Small)' : '(Too Large)'}`;
      lhsText.className = gap === 0 ? "text-emerald-400 font-bold font-mono text-sm" : "text-rose-300 font-bold font-mono text-sm";
    }

    if (badge) {
      if (gap === 0) {
        badge.textContent = "ROOT FOUND: x = 4 ✔";
        badge.className = "px-2.5 py-1 rounded bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 font-bold text-xs";
      } else {
        badge.textContent = `Gap: ${gap > 0 ? '+' : ''}${gap}`;
        badge.className = "px-2.5 py-1 rounded bg-rose-950/60 border border-rose-500/30 text-rose-300 font-bold text-xs";
      }
    }

    // Needle Angle: 0 gap = straight up (-90 deg), -12 gap = -150 deg, +12 gap = -30 deg
    const needleDeg = -90 + gap * 5.5;
    const rad = (needleDeg * Math.PI) / 180;
    const cx = 250, cy = 200;
    const r = 110;

    svg.innerHTML = `
      <!-- Gauge Arc -->
      <path d="M 140 200 A 110 110 0 0 1 360 200" fill="none" stroke="#334155" stroke-width="14" stroke-linecap="round" />
      <path d="M 235 91 A 110 110 0 0 1 265 91" fill="none" stroke="#10b981" stroke-width="16" />
      
      <!-- Needle Pivot -->
      <circle cx="${cx}" cy="${cy}" r="12" fill="#0f172a" stroke="#f43f5e" stroke-width="3" />
      
      <!-- Needle Line -->
      <line x1="${cx}" y1="${cy}" x2="${cx + r * Math.cos(rad)}" y2="${cy + r * Math.sin(rad)}" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" />
      <circle cx="${cx + r * Math.cos(rad)}" cy="${cy + r * Math.sin(rad)}" r="5" fill="#facc15" />
      
      <!-- Labels -->
      <text x="130" y="225" fill="#f87171" font-size="11" font-weight="bold">Too Small (LHS < 13)</text>
      <text x="238" y="75" fill="#34d399" font-size="12" font-weight="bold">13 (TARGET)</text>
      <text x="330" y="225" fill="#f87171" font-size="11" font-weight="bold">Too Large (LHS > 13)</text>
      
      <!-- Current Status -->
      <text x="30" y="35" fill="#f43f5e" font-size="13" font-weight="bold">Trial-and-Error Testing: 4x - 3 = 13</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Current Trial x = ${x} ⟹ LHS = ${lhs}</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 6. Add & Subtract Machine Simulator
// -------------------------------------------------------------
function initAddSubtractMachineSim(container) {
  const svg = container.querySelector('#addSubtractSvg');
  const stepBtn = container.querySelector('#addsubStepBtn');
  const resetBtn = container.querySelector('#addsubResetBtn');
  const statusText = container.querySelector('#addsubStatusText');
  if (!svg) return;

  let step = 0; // 0, 1, 2

  function render() {
    let content = `
      <text x="30" y="35" fill="#2dd4bf" font-size="13" font-weight="bold">Inverse Addition Machine: x + 7 = 19</text>
    `;

    if (step === 0) {
      if (statusText) statusText.textContent = "Step 0: Initial Equation: x + 7 = 19";
      content += `
        <!-- Left Pan -->
        <rect x="80" y="100" width="140" height="90" rx="8" fill="#134e4a" stroke="#2dd4bf" stroke-width="2" />
        <text x="110" y="152" fill="#ffffff" font-size="22" font-weight="bold">x + 7</text>
        
        <!-- Equals Sign -->
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <!-- Right Pan -->
        <rect x="280" y="100" width="140" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="330" y="152" fill="#ffffff" font-size="22" font-weight="bold">19</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">Goal: Isolate x by undoing the +7 addition.</text>
      `;
    } else if (step === 1) {
      if (statusText) statusText.textContent = "Step 1: Subtract 7 from BOTH sides: x + 7 - 7 = 19 - 7";
      content += `
        <!-- Left Pan with -7 operation -->
        <rect x="60" y="100" width="170" height="90" rx="8" fill="#134e4a" stroke="#2dd4bf" stroke-width="2" />
        <text x="75" y="152" fill="#ffffff" font-size="18" font-weight="bold">x + 7 <tspan fill="#f87171">- 7</tspan></text>
        
        <!-- Equals Sign -->
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <!-- Right Pan with -7 operation -->
        <rect x="270" y="100" width="170" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="295" y="152" fill="#ffffff" font-size="18" font-weight="bold">19 <tspan fill="#f87171">- 7</tspan></text>
        
        <text x="30" y="55" fill="#f87171" font-size="12" font-weight="bold">Subtract 7 simultaneously from both sides!</text>
      `;
    } else {
      if (statusText) statusText.textContent = "Step 2: +7 - 7 = 0 cleanly cancelled! Result: x = 12 ✔";
      content += `
        <!-- Left Pan Isolated -->
        <rect x="100" y="100" width="110" height="90" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="145" y="155" fill="#ffffff" font-size="26" font-weight="bold">x</text>
        
        <!-- Equals Sign -->
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <!-- Right Pan Resolved -->
        <rect x="290" y="100" width="110" height="90" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="330" y="155" fill="#ffffff" font-size="26" font-weight="bold">12</text>
        
        <text x="30" y="55" fill="#34d399" font-size="12" font-weight="bold">Success! Variable x is isolated: x = 12.</text>
        <text x="30" y="240" fill="#94a3b8" font-size="11">Check: LHS = 12 + 7 = 19 = RHS. Invariant satisfied.</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (step < 2) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 7. Multiply & Divide Isolator Simulator
// -------------------------------------------------------------
function initMulDivIsolatorSim(container) {
  const svg = container.querySelector('#mulDivSvg');
  const stepBtn = container.querySelector('#muldivStepBtn');
  const resetBtn = container.querySelector('#muldivResetBtn');
  const statusText = container.querySelector('#muldivStatusText');
  if (!svg) return;

  let step = 0;

  function render() {
    let content = `
      <text x="30" y="35" fill="#38bdf8" font-size="13" font-weight="bold">Multiplication Isolator: 5x = 35</text>
    `;

    if (step === 0) {
      if (statusText) statusText.textContent = "State: 5x = 35";
      content += `
        <!-- Left: 5x block -->
        <rect x="90" y="100" width="120" height="90" rx="8" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2" />
        <text x="130" y="155" fill="#ffffff" font-size="24" font-weight="bold">5x</text>
        
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <!-- Right: 35 block -->
        <rect x="290" y="100" width="120" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="330" y="155" fill="#ffffff" font-size="24" font-weight="bold">35</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">Goal: Neutralize multiplying factor 5 by division.</text>
      `;
    } else if (step === 1) {
      if (statusText) statusText.textContent = "Step 1: Divide BOTH sides by 5: (5x)/5 = 35/5";
      content += `
        <rect x="80" y="100" width="130" height="90" rx="8" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2" />
        <text x="110" y="135" fill="#ffffff" font-size="18" font-weight="bold">5x</text>
        <line x1="100" y1="145" x2="190" y2="145" stroke="#f87171" stroke-width="3" />
        <text x="140" y="170" fill="#f87171" font-size="18" font-weight="bold">5</text>
        
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <rect x="290" y="100" width="130" height="90" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="335" y="135" fill="#ffffff" font-size="18" font-weight="bold">35</text>
        <line x1="310" y1="145" x2="400" y2="145" stroke="#f87171" stroke-width="3" />
        <text x="350" y="170" fill="#f87171" font-size="18" font-weight="bold">5</text>
        
        <text x="30" y="55" fill="#f87171" font-size="12" font-weight="bold">Divide both sides by 5!</text>
      `;
    } else {
      if (statusText) statusText.textContent = "Step 2: 5/5 = 1 ⟹ 1·x = 7 ✔";
      content += `
        <rect x="100" y="100" width="110" height="90" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="145" y="155" fill="#ffffff" font-size="26" font-weight="bold">x</text>
        
        <circle cx="250" cy="145" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
        <text x="243" y="152" fill="#fbbf24" font-size="20" font-weight="bold">=</text>
        
        <rect x="290" y="100" width="110" height="90" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="335" y="155" fill="#ffffff" font-size="26" font-weight="bold">7</text>
        
        <text x="30" y="55" fill="#34d399" font-size="12" font-weight="bold">Root found: x = 7. Verified: 5 × 7 = 35.</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (step < 2) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 8. Two-Step Unwrapper Simulator
// -------------------------------------------------------------
function initTwoStepUnwrapperSim(container) {
  const svg = container.querySelector('#twoStepSvg');
  const nextBtn = container.querySelector('#twoStepNextBtn');
  const resetBtn = container.querySelector('#twoStepResetBtn');
  const badge = container.querySelector('#twoStepBadge');
  const desc = container.querySelector('#twoStepDesc');
  const result = container.querySelector('#twoStepResult');
  if (!svg) return;

  let step = 0; // 0, 1, 2

  function render() {
    if (badge) badge.textContent = `Step ${step} of 2`;

    let content = `
      <text x="30" y="35" fill="#f59e0b" font-size="13" font-weight="bold">Two-Step Unwrapping: 3x + 5 = 26</text>
    `;

    if (step === 0) {
      if (desc) desc.textContent = "Step 0: The unknown x is trapped inside multiplication (×3) and wrapped in addition (+5).";
      if (result) result.textContent = "Initial: 3x + 5 = 26";
      content += `
        <!-- Outer Gift Box (Addition Layer +5) -->
        <rect x="60" y="80" width="170" height="130" rx="12" fill="#b45309" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 3" />
        <text x="75" y="105" fill="#fde68a" font-size="11" font-weight="bold">Layer 1: Addition (+5)</text>
        
        <!-- Inner Gift Box (Multiplication Layer ×3) -->
        <rect x="85" y="120" width="120" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <text x="125" y="162" fill="#ffffff" font-size="20" font-weight="bold">3x</text>
        
        <!-- Equal Sign -->
        <text x="240" y="155" fill="#fbbf24" font-size="24" font-weight="bold">=</text>
        
        <!-- RHS -->
        <rect x="270" y="110" width="130" height="80" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="315" y="160" fill="#ffffff" font-size="26" font-weight="bold">26</text>
      `;
    } else if (step === 1) {
      if (desc) desc.textContent = "Step 1: Unwrap Addition first! Subtract 5 from both sides: 3x = 26 - 5 = 21.";
      if (result) result.textContent = "After Layer 1: 3x = 21";
      content += `
        <!-- Addition Layer Unwrapped! -->
        <rect x="85" y="110" width="120" height="80" rx="8" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2.5" />
        <text x="125" y="160" fill="#ffffff" font-size="24" font-weight="bold">3x</text>
        
        <text x="240" y="155" fill="#fbbf24" font-size="24" font-weight="bold">=</text>
        
        <rect x="270" y="110" width="130" height="80" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="315" y="160" fill="#ffffff" font-size="26" font-weight="bold">21</text>
        <text x="280" y="85" fill="#f87171" font-size="12" font-weight="bold">26 - 5 = 21</text>
      `;
    } else {
      if (desc) desc.textContent = "Step 2: Unwrap Multiplication! Divide both sides by 3: x = 21 / 3 = 7. Solved!";
      if (result) result.textContent = "Final Root: x = 7 ✔";
      content += `
        <!-- Fully Unwrapped Variable x -->
        <rect x="95" y="110" width="100" height="80" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="135" y="160" fill="#ffffff" font-size="28" font-weight="bold">x</text>
        
        <text x="240" y="155" fill="#fbbf24" font-size="24" font-weight="bold">=</text>
        
        <rect x="280" y="110" width="100" height="80" rx="8" fill="#047857" stroke="#10b981" stroke-width="3" />
        <text x="320" y="160" fill="#ffffff" font-size="28" font-weight="bold">7</text>
        <text x="280" y="85" fill="#34d399" font-size="12" font-weight="bold">21 / 3 = 7</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { if (step < 2) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 9. Transposition Bridge Simulator
// -------------------------------------------------------------
function initTranspositionBridgeSim(container) {
  const svg = container.querySelector('#bridgeSvg');
  const transBtn = container.querySelector('#bridgeTransposeBtn');
  const resetBtn = container.querySelector('#bridgeResetBtn');
  const eqText = container.querySelector('#bridgeEquationText');
  if (!svg) return;

  let crossed = false;

  function render() {
    let content = `
      <!-- River Below -->
      <path d="M 0 230 C 150 210, 350 250, 500 230 L 500 300 L 0 300 Z" fill="#082f49" />
      <text x="210" y="270" fill="#0284c7" font-size="11" font-style="italic">River of Operations</text>
      
      <!-- Bridge Arch with '=' sign -->
      <path d="M 190 220 Q 250 140 310 220" fill="none" stroke="#64748b" stroke-width="8" />
      <circle cx="250" cy="170" r="16" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
      <text x="243" y="177" fill="#fbbf24" font-size="18" font-weight="bold">=</text>
      <text x="205" y="130" fill="#fbbf24" font-size="11" font-weight="bold">The Equal Bridge</text>
      
      <text x="30" y="35" fill="#c084fc" font-size="13" font-weight="bold">Transposition Law: Crossing the '=' Bridge Inverts Signs!</text>
    `;

    if (!crossed) {
      if (eqText) eqText.textContent = "Current State: x + 7 = 20";
      content += `
        <!-- Left Bank: x and +7 -->
        <rect x="50" y="150" width="60" height="50" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2" />
        <text x="73" y="182" fill="#ffffff" font-size="20" font-weight="bold">x</text>
        
        <rect x="120" y="150" width="60" height="50" rx="6" fill="#047857" stroke="#10b981" stroke-width="2" />
        <text x="133" y="182" fill="#ffffff" font-size="18" font-weight="bold">+7</text>
        
        <!-- Right Bank: 20 -->
        <rect x="340" y="150" width="70" height="50" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="360" y="182" fill="#ffffff" font-size="20" font-weight="bold">20</text>
      `;
    } else {
      if (eqText) eqText.textContent = "Transposed: x = 20 - 7 = 13 ✔";
      content += `
        <!-- Left Bank: x only -->
        <rect x="70" y="150" width="70" height="50" rx="6" fill="#047857" stroke="#10b981" stroke-width="2.5" />
        <text x="98" y="182" fill="#ffffff" font-size="22" font-weight="bold">x</text>
        
        <!-- Right Bank: 20 and -7 (Flipped!) -->
        <rect x="330" y="150" width="60" height="50" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="348" y="182" fill="#ffffff" font-size="18" font-weight="bold">20</text>
        
        <rect x="400" y="150" width="60" height="50" rx="6" fill="#881337" stroke="#f43f5e" stroke-width="2" />
        <text x="415" y="182" fill="#fecdd3" font-size="18" font-weight="bold">-7</text>
        
        <!-- Motion Arrow over Bridge -->
        <path d="M 150 140 Q 250 80 430 140" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4 3" />
        <text x="210" y="95" fill="#f43f5e" font-size="11" font-weight="bold">+7 flipped to -7</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (transBtn) transBtn.addEventListener('click', () => { crossed = true; render(); });
  if (resetBtn) resetBtn.addEventListener('click', () => { crossed = false; render(); });
  render();
}

// -------------------------------------------------------------
// 10. Dual-Pan Dual-Variable Balance Simulator
// -------------------------------------------------------------
function initDualPanVariablesSim(container) {
  const svg = container.querySelector('#dualPanSvg');
  const stepBtn = container.querySelector('#dualPanStepBtn');
  const resetBtn = container.querySelector('#dualPanResetBtn');
  const badge = container.querySelector('#dualPanBadge');
  const statusSpan = container.querySelector('#dualPanStatus');
  if (!svg) return;

  let step = 0; // 0, 1, 2, 3

  function render() {
    if (badge) badge.textContent = `Step ${step} of 3`;

    let content = `
      <!-- Stand Base & Beam (Always balanced) -->
      <polygon points="210,270 290,270 260,170 240,170" fill="#334155" stroke="#475569" stroke-width="2" />
      <circle cx="250" cy="160" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
      <line x1="110" y1="160" x2="390" y2="160" stroke="#94a3b8" stroke-width="6" stroke-linecap="round" />
      
      <!-- Left Pan -->
      <line x1="110" y1="160" x2="75" y2="220" stroke="#64748b" stroke-width="1.5" />
      <line x1="110" y1="160" x2="145" y2="220" stroke="#64748b" stroke-width="1.5" />
      <path d="M 65 220 Q 110 235 155 220 Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      
      <!-- Right Pan -->
      <line x1="390" y1="160" x2="355" y2="220" stroke="#64748b" stroke-width="1.5" />
      <line x1="390" y1="160" x2="425" y2="220" stroke="#64748b" stroke-width="1.5" />
      <path d="M 345 220 Q 390 235 435 220 Z" fill="#475569" stroke="#94a3b8" stroke-width="2" />
      
      <text x="30" y="35" fill="#34d399" font-size="13" font-weight="bold">Variables on Both Sides: 5x + 3 = 2x + 18</text>
    `;

    if (step === 0) {
      if (statusSpan) statusSpan.textContent = "Step 0: Initial Scale: 5x + 3 = 2x + 18";
      content += `
        <!-- Left: 5 sacks + 3kg -->
        <rect x="75" y="185" width="45" height="30" rx="3" fill="#b45309" stroke="#f59e0b" />
        <text x="85" y="205" fill="#ffffff" font-size="12" font-weight="bold">5x</text>
        <rect x="125" y="195" width="22" height="20" rx="2" fill="#0284c7" />
        <text x="129" y="210" fill="#ffffff" font-size="10" font-weight="bold">3k</text>
        
        <!-- Right: 2 sacks + 18kg -->
        <rect x="355" y="185" width="30" height="30" rx="3" fill="#b45309" stroke="#f59e0b" />
        <text x="362" y="205" fill="#ffffff" font-size="12" font-weight="bold">2x</text>
        <rect x="390" y="180" width="35" height="35" rx="3" fill="#059669" />
        <text x="395" y="203" fill="#ffffff" font-size="12" font-weight="bold">18k</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">Goal: Remove the smaller variable term (2x) from both pans.</text>
      `;
    } else if (step === 1) {
      if (statusSpan) statusSpan.textContent = "Step 1: Removed 2x from both pans ⟹ 3x + 3 = 18";
      content += `
        <!-- Left: 3 sacks + 3kg -->
        <rect x="75" y="185" width="45" height="30" rx="3" fill="#b45309" stroke="#f59e0b" />
        <text x="85" y="205" fill="#ffffff" font-size="12" font-weight="bold">3x</text>
        <rect x="125" y="195" width="22" height="20" rx="2" fill="#0284c7" />
        <text x="129" y="210" fill="#ffffff" font-size="10" font-weight="bold">3k</text>
        
        <!-- Right: 18kg only -->
        <rect x="370" y="180" width="40" height="35" rx="3" fill="#059669" />
        <text x="378" y="203" fill="#ffffff" font-size="12" font-weight="bold">18k</text>
        <text x="30" y="55" fill="#38bdf8" font-size="11">Next: Remove 3 kg constant from both pans.</text>
      `;
    } else if (step === 2) {
      if (statusSpan) statusSpan.textContent = "Step 2: Removed 3 kg from both pans ⟹ 3x = 15";
      content += `
        <!-- Left: 3 sacks only -->
        <rect x="85" y="185" width="50" height="30" rx="3" fill="#b45309" stroke="#f59e0b" />
        <text x="98" y="205" fill="#ffffff" font-size="13" font-weight="bold">3x</text>
        
        <!-- Right: 15kg only -->
        <rect x="370" y="180" width="40" height="35" rx="3" fill="#059669" />
        <text x="378" y="203" fill="#ffffff" font-size="12" font-weight="bold">15k</text>
        <text x="30" y="55" fill="#f59e0b" font-size="11">Next: Divide 15 kg evenly across the 3 sacks.</text>
      `;
    } else {
      if (statusSpan) statusSpan.textContent = "Step 3: Divided by 3 ⟹ x = 5 kg ✔";
      content += `
        <!-- Left: 1 sack x -->
        <rect x="90" y="185" width="40" height="30" rx="3" fill="#047857" stroke="#34d399" stroke-width="2" />
        <text x="105" y="205" fill="#ffffff" font-size="14" font-weight="bold">x</text>
        
        <!-- Right: 5kg weight -->
        <rect x="375" y="185" width="30" height="30" rx="3" fill="#047857" stroke="#34d399" stroke-width="2" />
        <text x="383" y="205" fill="#ffffff" font-size="12" font-weight="bold">5k</text>
        <text x="30" y="55" fill="#34d399" font-size="12" font-weight="bold">Solved: x = 5 kg! Check: 5(5)+3 = 2(5)+18 = 28.</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (step < 3) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 11. Geometry Word Problem Simulator
// -------------------------------------------------------------
function initGeomWordProblemSim(container) {
  const svg = container.querySelector('#geomWordSvg');
  const slider = container.querySelector('#geomWidthSlider');
  const wVal = container.querySelector('#geomWidthVal');
  const perimText = container.querySelector('#geomPerimText');
  if (!svg || !slider) return;

  function render() {
    const w = parseInt(slider.value, 10);
    const l = w + 4;
    const p = 2 * (l + w);
    const isMatch = (p === 40);

    if (wVal) wVal.textContent = `w = ${w} m`;
    if (perimText) {
      perimText.textContent = `l = ${l} m, w = ${w} m ⟹ P = 2(${l} + ${w}) = ${p} m ${isMatch ? '(MATCH!) ✔' : '(Target: 40 m)'}`;
      perimText.className = isMatch ? "text-emerald-400 font-bold font-mono text-xs" : "text-amber-400 font-bold font-mono text-xs";
    }

    const scale = 11;
    const rectW = l * scale;
    const rectH = w * scale;
    const rx = 250 - rectW / 2;
    const ry = 160 - rectH / 2;

    svg.innerHTML = `
      <text x="30" y="35" fill="#818cf8" font-size="13" font-weight="bold">Garden Plot Perimeter: P = 2(l + w) = 40 m</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Given: Length is 4 m more than width ⟹ l = w + 4</text>
      
      <!-- Garden Rectangle -->
      <rect x="${rx}" y="${ry}" width="${rectW}" height="${rectH}" rx="6" 
            fill="${isMatch ? '#065f46' : '#1e1b4b'}" 
            stroke="${isMatch ? '#34d399' : '#818cf8'}" stroke-width="${isMatch ? 3 : 2}" />
      
      <!-- Width Labels (Left and Right) -->
      <text x="${rx - 35}" y="${ry + rectH/2 + 4}" fill="#fde047" font-size="12" font-weight="bold">w = ${w}m</text>
      <text x="${rx + rectW + 10}" y="${ry + rectH/2 + 4}" fill="#fde047" font-size="12" font-weight="bold">w = ${w}m</text>
      
      <!-- Length Labels (Top and Bottom) -->
      <text x="${rx + rectW/2 - 35}" y="${ry - 12}" fill="#38bdf8" font-size="12" font-weight="bold">l = w + 4 = ${l}m</text>
      <text x="${rx + rectW/2 - 35}" y="${ry + rectH + 20}" fill="#38bdf8" font-size="12" font-weight="bold">l = w + 4 = ${l}m</text>
      
      <!-- Center Badge -->
      <text x="${rx + rectW/2 - 40}" y="${ry + rectH/2 + 5}" fill="#ffffff" font-size="13" font-weight="bold">Perimeter: ${p}m</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 12. Mind-Reading Number Trick Simulator
// -------------------------------------------------------------
function initBudgetMagicTrickSim(container) {
  const svg = container.querySelector('#magicTrickSvg');
  const xInput = container.querySelector('#magicXInput');
  const nextBtn = container.querySelector('#magicNextStepBtn');
  const resetBtn = container.querySelector('#magicResetBtn');
  const formulaReadout = container.querySelector('#magicFormulaReadout');
  if (!svg) return;

  let step = 0; // 0, 1, 2, 3, 4

  function render() {
    let x = parseInt(xInput.value, 10);
    if (isNaN(x) || x < 1) x = 7;

    const stepsData = [
      { num: x, expr: "x", desc: `1. Think of secret number: ${x}` },
      { num: 2 * x, expr: "2x", desc: `2. Double it: 2(${x}) = ${2 * x}` },
      { num: 2 * x + 10, expr: "2x + 10", desc: `3. Add 10: ${2 * x} + 10 = ${2 * x + 10}` },
      { num: x + 5, expr: "x + 5", desc: `4. Divide by 2: (${2 * x + 10})/2 = ${x + 5}` },
      { num: 5, expr: "5", desc: `5. Subtract secret number: (${x + 5}) - ${x} = 5! (MAGIC!)` }
    ];

    const cur = stepsData[step];
    if (formulaReadout) formulaReadout.textContent = cur.desc;

    let content = `
      <text x="30" y="35" fill="#fde047" font-size="13" font-weight="bold">The Mind-Reading Math Trick: Why It Always Equals 5!</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Variable elimination identity: [(2x + 10) / 2] - x = (x + 5) - x = 5</text>
      
      <!-- Stage Box -->
      <rect x="120" y="85" width="260" height="130" rx="12" fill="#0f172a" stroke="#d97706" stroke-width="2.5" />
      <text x="140" y="115" fill="#fde68a" font-size="12" font-weight="bold">Step ${step + 1}: Current Result</text>
      
      <!-- Number Display -->
      <circle cx="250" cy="160" r="35" fill="#b45309" stroke="#f59e0b" stroke-width="2" />
      <text x="${cur.num >= 10 ? 238 : 243}" y="${168}" fill="#ffffff" font-size="24" font-weight="extrabold">${cur.num}</text>
      
      <!-- Algebraic Expression -->
      <text x="215" y="240" fill="#38bdf8" font-size="14" font-weight="bold">Algebra: ${cur.expr}</text>
    `;

    if (step === 4) {
      content += `
        <text x="150" y="270" fill="#34d399" font-size="13" font-weight="bold">The secret x canceled out completely: x - x = 0!</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { if (step < 4) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  if (xInput) xInput.addEventListener('input', () => { render(); });
  render();
}

// -------------------------------------------------------------
// 13. Transposition Trap Diagnostic Simulator
// -------------------------------------------------------------
function initTranspositionTrapSim(container) {
  const svg = container.querySelector('#trapClinicSvg');
  const mendBtn = container.querySelector('#mendMistakeBtn');
  const badge = container.querySelector('#trapStatusBadge');
  const diagText = container.querySelector('#trapDiagnosisText');
  if (!svg) return;

  let isMended = false;

  function render() {
    let content = `
      <text x="30" y="35" fill="#f43f5e" font-size="13" font-weight="bold">Diagnostic Clinic: Spot & Fix the Transposition Trap</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Equation: 4x - 9 = 15</text>
    `;

    if (!isMended) {
      if (badge) {
        badge.textContent = "BUG DETECTED ❌";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
      }
      if (diagText) diagText.innerHTML = "<span class='text-rose-400 font-bold'>Error:</span> -9 was transposed as -9 instead of +9!";

      content += `
        <rect x="60" y="80" width="380" height="150" rx="10" fill="#4c0519" fill-opacity="0.4" stroke="#f43f5e" stroke-width="2" />
        
        <text x="90" y="115" fill="#fca5a5" font-size="14" font-weight="bold">Step 1: 4x - 9 = 15</text>
        <text x="90" y="145" fill="#f87171" font-size="14" font-weight="bold">Step 2: 4x = 15 - 9 <tspan fill="#ef4444">(TRAP! Sign not flipped)</tspan></text>
        <text x="90" y="175" fill="#fca5a5" font-size="14" font-weight="bold">Step 3: 4x = 6 ⟹ x = 1.5 <tspan fill="#ef4444">❌ INCORRECT</tspan></text>
        <text x="90" y="210" fill="#fecdd3" font-size="11">Check: 4(1.5) - 9 = 6 - 9 = -3 ≠ 15. The solution fails verification!</text>
      `;
    } else {
      if (badge) {
        badge.textContent = "MISTAKE MENDED ✔";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
      }
      if (diagText) diagText.innerHTML = "<span class='text-emerald-400 font-bold'>Mended:</span> -9 crosses '=' and correctly becomes +9!";

      content += `
        <rect x="60" y="80" width="380" height="150" rx="10" fill="#064e3b" fill-opacity="0.4" stroke="#34d399" stroke-width="2" />
        
        <text x="90" y="115" fill="#a7f3d0" font-size="14" font-weight="bold">Step 1: 4x - 9 = 15</text>
        <text x="90" y="145" fill="#34d399" font-size="14" font-weight="bold">Step 2: 4x = 15 + 9 <tspan fill="#34d399">(CORRECT! -9 inverts to +9)</tspan></text>
        <text x="90" y="175" fill="#a7f3d0" font-size="14" font-weight="bold">Step 3: 4x = 24 ⟹ x = 24/4 = 6 <tspan fill="#34d399">✔ SOLVED</tspan></text>
        <text x="90" y="210" fill="#a7f3d0" font-size="11">Check: 4(6) - 9 = 24 - 9 = 15 = RHS. Flawless verification!</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (mendBtn) mendBtn.addEventListener('click', () => { isMended = !isMended; render(); });
  render();
}

// -------------------------------------------------------------
// 14. Distributive & Whole-Side Division Diagnostic Simulator
// -------------------------------------------------------------
function initDistribDivisionTrapSim(container) {
  const svg = container.querySelector('#distribSvg');
  const btns = container.querySelectorAll('.distribChoiceBtn');
  const resText = container.querySelector('#distribResultText');
  if (!svg) return;

  let mode = 'partial'; // 'partial' or 'whole'

  function render() {
    let content = `
      <text x="30" y="35" fill="#c084fc" font-size="13" font-weight="bold">Diagnostic: Whole-Side Division vs Partial Division</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Problem: 2x + 6 = 14 (Dividing by 2)</text>
    `;

    if (mode === 'partial') {
      if (resText) resText.textContent = "Bug: x + 6 = 7 (6 was not divided!) ⟹ x = 1 (WRONG)";
      content += `
        <!-- Buggy Split -->
        <rect x="70" y="80" width="360" height="150" rx="10" fill="#4c0519" fill-opacity="0.3" stroke="#f43f5e" stroke-width="2" />
        <text x="100" y="115" fill="#f87171" font-size="14" font-weight="bold">Student Error (Partial Division):</text>
        <text x="100" y="145" fill="#fca5a5" font-size="13">Divided 2x by 2 (giving x), and 14 by 2 (giving 7)</text>
        <text x="100" y="170" fill="#fca5a5" font-size="13">BUT forgot to divide the term +6 by 2!</text>
        <text x="100" y="200" fill="#ef4444" font-size="14" font-weight="bold">x + 6 = 7 ⟹ x = 1 ❌ (Fails: 2(1)+6 = 8 ≠ 14)</text>
      `;
    } else {
      if (resText) resText.textContent = "Correct: (2x+6)/2 = 14/2 ⟹ x + 3 = 7 ⟹ x = 4 ✔";
      content += `
        <!-- Correct Split -->
        <rect x="70" y="80" width="360" height="150" rx="10" fill="#064e3b" fill-opacity="0.3" stroke="#34d399" stroke-width="2" />
        <text x="100" y="115" fill="#34d399" font-size="14" font-weight="bold">Correct Method (Whole-Side Division):</text>
        <text x="100" y="145" fill="#a7f3d0" font-size="13">Divide EVERY term on the LHS by 2: (2x)/2 + 6/2</text>
        <text x="100" y="170" fill="#a7f3d0" font-size="13">x + 3 = 7</text>
        <text x="100" y="200" fill="#34d399" font-size="14" font-weight="bold">x = 7 - 3 = 4 ✔ (Verified: 2(4)+6 = 8+6 = 14)</text>
      `;
    }

    svg.innerHTML = content;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "distribChoiceBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition");
      btn.className = btn.dataset.mode === 'partial' ? "distribChoiceBtn px-3 py-1.5 rounded-lg bg-rose-600 text-xs font-semibold text-white transition" : "distribChoiceBtn px-3 py-1.5 rounded-lg bg-emerald-600 text-xs font-semibold text-white transition";
      mode = btn.dataset.mode;
      render();
    });
  });

  render();
}

// -------------------------------------------------------------
// 15. Bījagaṇita Timeline Simulator
// -------------------------------------------------------------
function initBijaganitaTimelineSim(container) {
  const svg = container.querySelector('#timelineSvg');
  const btns = container.querySelectorAll('.timelineBtn');
  if (!svg) return;

  let currentEpoch = 'brahmagupta';

  const details = {
    aryabhata: {
      name: "Āryabhaṭa (476–550 CE)",
      work: "Āryabhaṭīya (499 CE)",
      contrib: "Invented the Kuṭṭaka ('pulverizer') algorithm to solve linear indeterminate equations ax - by = c, and introduced phonetic alphabetical variables."
    },
    brahmagupta: {
      name: "Acharya Brahmagupta (598–668 CE)",
      work: "Brāhmasphuṭasiddhānta (628 CE)",
      contrib: "Chapter 18 (Kuṭṭakādhyāya) codified the first rules for zero, debt/negative (ṛṇa), fortune/positive (dhana), and the universal linear equation formula x = (D-B)/(A-C)."
    },
    alkhwarizmi: {
      name: "Muhammad ibn Musa al-Khwarizmi (780–850 CE)",
      work: "Kitab al-Jabr wa-l-Muqabala (825 CE, Baghdad)",
      contrib: "Synthesized Indian algebra and decimal numbers at the House of Wisdom. The term 'al-Jabr' (restoration of negatives via transposition) became 'Algebra'."
    },
    bhaskara: {
      name: "Bhāskarāchārya / Bhāskara II (1114–1185 CE)",
      work: "Līlāvatī & Bījagaṇita (1150 CE)",
      contrib: "Framed algebraic linear and quadratic systems through poetic riddles, mastered multi-variable systems with color names, and analyzed division by zero."
    }
  };

  function render() {
    const d = details[currentEpoch];

    svg.innerHTML = `
      <!-- Timeline Horizontal Bar -->
      <line x1="50" y1="80" x2="450" y2="80" stroke="#475569" stroke-width="4" stroke-linecap="round" />
      
      <!-- Nodes -->
      <circle cx="90" cy="80" r="10" fill="${currentEpoch === 'aryabhata' ? '#f59e0b' : '#334155'}" stroke="#fbbf24" stroke-width="2" />
      <text x="65" y="60" fill="#94a3b8" font-size="10">499 CE</text>
      
      <circle cx="190" cy="80" r="10" fill="${currentEpoch === 'brahmagupta' ? '#f59e0b' : '#334155'}" stroke="#fbbf24" stroke-width="2" />
      <text x="165" y="60" fill="#94a3b8" font-size="10">628 CE</text>
      
      <circle cx="290" cy="80" r="10" fill="${currentEpoch === 'alkhwarizmi' ? '#f59e0b' : '#334155'}" stroke="#fbbf24" stroke-width="2" />
      <text x="265" y="60" fill="#94a3b8" font-size="10">825 CE</text>
      
      <circle cx="410" cy="80" r="10" fill="${currentEpoch === 'bhaskara' ? '#f59e0b' : '#334155'}" stroke="#fbbf24" stroke-width="2" />
      <text x="385" y="60" fill="#94a3b8" font-size="10">1150 CE</text>
      
      <!-- Detail Card -->
      <rect x="50" y="110" width="400" height="150" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="2" />
      
      <text x="70" y="140" fill="#fde68a" font-size="15" font-weight="extrabold">${d.name}</text>
      <text x="70" y="165" fill="#38bdf8" font-size="12" font-weight="bold">Master Treatise: ${d.work}</text>
      
      <!-- Contribution paragraph wrapped -->
      <foreignObject x="70" y="180" width="360" height="70">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 11px; color: #cbd5e1; line-height: 1.4;">
          ${d.contrib}
        </div>
      </foreignObject>
    `;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "timelineBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition");
      btn.className = "timelineBtn px-2.5 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition";
      currentEpoch = btn.dataset.epoch;
      render();
    });
  });

  render();
}

// -------------------------------------------------------------
// 16. Brahmagupta Linear Equation Solver Simulator
// -------------------------------------------------------------
function initBrahmaguptaLinearSolverSim(container) {
  const svg = container.querySelector('#brahmaSolverSvg');
  const inA = container.querySelector('#brahmaA');
  const inB = container.querySelector('#brahmaB');
  const inC = container.querySelector('#brahmaC');
  const inD = container.querySelector('#brahmaD');
  if (!svg || !inA || !inB || !inC || !inD) return;

  function render() {
    const A = parseFloat(inA.value) || 0;
    const B = parseFloat(inB.value) || 0;
    const C = parseFloat(inC.value) || 0;
    const D = parseFloat(inD.value) || 0;

    const diffCoeff = A - C;
    const diffConst = D - B;

    let resText = "";
    let isSpecial = false;

    if (diffCoeff === 0) {
      isSpecial = true;
      if (diffConst === 0) {
        resText = "Identity! Infinite solutions (True for all x).";
      } else {
        resText = "Contradiction! NO solution (Parallel lines).";
      }
    } else {
      const x = diffConst / diffCoeff;
      resText = `x = ${diffConst} / ${diffCoeff} = ${Number.isInteger(x) ? x : x.toFixed(3)}`;
    }

    svg.innerHTML = `
      <text x="30" y="35" fill="#34d399" font-size="13" font-weight="bold">Brahmagupta's Universal Equation Law (628 CE)</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Form: Ax + B = Cx + D ⟹ x = (D - B) / (A - C)</text>
      
      <!-- Equation Box -->
      <rect x="60" y="80" width="380" height="150" rx="12" fill="#064e3b" fill-opacity="0.3" stroke="#34d399" stroke-width="2" />
      
      <text x="100" y="115" fill="#a7f3d0" font-size="15" font-weight="bold">
        ${A}x + ${B} = ${C}x + ${D}
      </text>
      
      <text x="100" y="145" fill="#fde68a" font-size="13">
        Numerator: D - B = ${D} - ${B} = ${diffConst}
      </text>
      <text x="100" y="170" fill="#fde68a" font-size="13">
        Denominator: A - C = ${A} - ${C} = ${diffCoeff}
      </text>
      
      <text x="100" y="205" fill="${isSpecial ? '#f87171' : '#34d399'}" font-size="16" font-weight="extrabold">
        Result: ${resText}
      </text>
    `;
  }

  [inA, inB, inC, inD].forEach(input => input.addEventListener('input', render));
  render();
}
"""

if __name__ == "__main__":
    with open(".agents/class7_math_finding_the_unknown_js.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Mathematics Chapter 7: Finding the Unknown JS Engine"""\n\n')
        f.write("SIMULATORS_JS = " + repr(SIMULATORS_JS) + "\n")
    print("Generated .agents/class7_math_finding_the_unknown_js.py successfully.")


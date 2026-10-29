# -*- coding: utf-8 -*-
"""
Script to generate .agents/class7_math_another_peek_beyond_the_point_js.py
Contains all 16 interactive JavaScript simulator engines for Chapter 12: Another Peek Beyond the Point.
"""

simulators_js = r"""
function initSimulators() {
  initPlaceValueMatrix();
  initExpandedDeconstructor();
  initFractionDecimalBridge();
  initFriendlyMultiplierScaler();
  initWholeDecimalMultiplier();
  initGridMultiplicationArea();
  initMultiplicationAlgorithmStepper();
  initMagnitudeParadoxScale();
  initPower10ShiftSlider();
  initPlaceValueRegroupDivision();
  initDecimalDivisorTransformer();
  initCyclicWheel142857();
  initEarthOrbitDrift();
  initLeapYearDecisionTree();
  initHidatoGridPuzzle();
  initMadhavaDecimalSeries();
}

// 1. Place Value Matrix
function initPlaceValueMatrix() {
  const sTh = document.getElementById('mat-slide-th');
  const sHth = document.getElementById('mat-slide-hth');
  const sTth = document.getElementById('mat-slide-tth');
  if (!sTh || !sHth || !sTth) return;

  function update() {
    const th = parseInt(sTh.value);
    const hth = parseInt(sHth.value);
    const tth = parseInt(sTth.value);

    document.getElementById('val-th').textContent = th;
    document.getElementById('val-hth').textContent = hth;
    document.getElementById('val-tth').textContent = tth;

    document.getElementById('mat-th').textContent = th;
    document.getElementById('mat-hth').textContent = hth;
    document.getElementById('mat-tth').textContent = tth;

    const fullNum = `347.${th}${hth}${tth}`;
    document.getElementById('mat-full-num').textContent = fullNum;

    const preview = document.getElementById('mat-expanded-preview');
    if (preview) {
      preview.innerHTML = `$${fullNum} = 300 + 40 + 7 + \\frac{${th}}{10} + \\frac{${hth}}{100} + \\frac{${tth}}{1000}$`;
      if (window.triggerMathRender) window.triggerMathRender(preview);
    }
  }

  sTh.addEventListener('input', update);
  sHth.addEventListener('input', update);
  sTth.addEventListener('input', update);
  update();
}

// 2. Expanded Deconstructor
function initExpandedDeconstructor() {
  const buttons = document.querySelectorAll('.btn-decon');
  if (!buttons.length) return;

  function deconstruct(valStr) {
    const targetEl = document.getElementById('decon-target');
    const slicesEl = document.getElementById('decon-slices');
    const formulaEl = document.getElementById('decon-total-formula');
    if (!targetEl || !slicesEl || !formulaEl) return;

    targetEl.textContent = valStr;
    const parts = valStr.split('.');
    const whole = parts[0] || '0';
    const frac = parts[1] || '';

    let html = '';
    let fracEqParts = [];

    // Wholes
    const wholeNum = parseInt(whole);
    if (wholeNum >= 100) {
      const h = Math.floor(wholeNum / 100) * 100;
      html += `<div class="p-1.5 bg-slate-900 rounded border border-slate-700 flex justify-between"><span class="text-sky-400 font-bold">${h}</span><span class="text-slate-400">${h/100} hundreds</span></div>`;
      fracEqParts.push(`${h}`);
    }
    if (wholeNum >= 10) {
      const t = Math.floor((wholeNum % 100) / 10) * 10;
      if (t > 0) {
        html += `<div class="p-1.5 bg-slate-900 rounded border border-slate-700 flex justify-between"><span class="text-sky-300 font-bold">${t}</span><span class="text-slate-400">${t/10} tens</span></div>`;
        fracEqParts.push(`${t}`);
      }
    }
    const o = wholeNum % 10;
    if (o > 0 || wholeNum === 0) {
      html += `<div class="p-1.5 bg-slate-900 rounded border border-slate-700 flex justify-between"><span class="text-emerald-400 font-bold">${o}</span><span class="text-slate-400">${o} ones</span></div>`;
      fracEqParts.push(`${o}`);
    }

    // Fraction digits
    if (frac.length > 0 && frac[0] !== '0') {
      const d = frac[0];
      html += `<div class="p-1.5 bg-amber-950/40 rounded border border-amber-800/50 flex justify-between"><span class="text-amber-300 font-bold">0.${d}</span><span class="text-amber-400">$\\frac{${d}}{10}$ (${d} tenths)</span></div>`;
      fracEqParts.push(`\\frac{${d}}{10}`);
    }
    if (frac.length > 1 && frac[1] !== '0') {
      const d = frac[1];
      html += `<div class="p-1.5 bg-amber-950/40 rounded border border-amber-800/50 flex justify-between"><span class="text-amber-300 font-bold">0.0${d}</span><span class="text-amber-400">$\\frac{${d}}{100}$ (${d} hundredths)</span></div>`;
      fracEqParts.push(`\\frac{${d}}{100}`);
    }
    if (frac.length > 2 && frac[2] !== '0') {
      const d = frac[2];
      html += `<div class="p-1.5 bg-amber-950/40 rounded border border-amber-800/50 flex justify-between"><span class="text-amber-300 font-bold">0.00${d}</span><span class="text-amber-400">$\\frac{${d}}{1000}$ (${d} thousandths)</span></div>`;
      fracEqParts.push(`\\frac{${d}}{1000}`);
    }

    slicesEl.innerHTML = html;
    formulaEl.innerHTML = `$${valStr} = ${fracEqParts.join(' + ')}$`;
    if (window.triggerMathRender) {
      window.triggerMathRender(slicesEl);
      window.triggerMathRender(formulaEl);
    }
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.replace('bg-indigo-600', 'bg-slate-800'));
      btn.classList.replace('bg-slate-800', 'bg-indigo-600');
      deconstruct(btn.dataset.val);
    });
  });

  deconstruct('23.456');
}

// 3. Fraction Decimal Bridge
function initFractionDecimalBridge() {
  let activeDen = 10;
  const denBtns = document.querySelectorAll('.btn-bridge-den');
  const slider = document.getElementById('bridge-num-slider');
  const numDisplay = document.getElementById('bridge-num-display');
  const fillBar = document.getElementById('bridge-fill-bar');
  const fracText = document.getElementById('bridge-frac-text');
  const decText = document.getElementById('bridge-dec-text');
  if (!slider || !fillBar) return;

  function update() {
    const num = parseInt(slider.value);
    numDisplay.textContent = num;
    const ratio = num / activeDen;
    const barWidth = Math.min(360, Math.max(0, ratio * 360));
    fillBar.setAttribute('width', barWidth.toFixed(1));

    let decStr = ratio.toFixed(activeDen === 10 ? 1 : (activeDen === 100 ? 2 : 3));
    fracText.innerHTML = `$\\frac{${num}}{${activeDen}}$`;
    decText.innerHTML = `$\\mathbf{${decStr}}$`;

    if (window.triggerMathRender) {
      window.triggerMathRender(fracText);
      window.triggerMathRender(decText);
    }
  }

  denBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      denBtns.forEach(b => {
        b.classList.remove('bg-cyan-950/40', 'border-cyan-700/50');
        b.classList.add('bg-slate-800', 'border-slate-700');
      });
      btn.classList.add('bg-cyan-950/40', 'border-cyan-700/50');
      btn.classList.remove('bg-slate-800', 'border-slate-700');

      activeDen = parseInt(btn.dataset.den);
      if (activeDen === 10) {
        slider.max = "10";
        slider.value = "7";
      } else if (activeDen === 100) {
        slider.max = "100";
        slider.value = "43";
      } else {
        slider.max = "1000";
        slider.value = "389";
      }
      update();
    });
  });

  slider.addEventListener('input', update);
  update();
}

// 4. Friendly Multiplier Scaler
function initFriendlyMultiplierScaler() {
  const buttons = document.querySelectorAll('.btn-scaler');
  if (!buttons.length) return;

  const targetEl = document.getElementById('scaler-target-power');
  const multiEl = document.getElementById('scaler-multiplier');
  const eqEl = document.getElementById('scaler-equation');

  const scaleMap = {
    '2': { target: 10, mult: 5 },
    '4': { target: 100, mult: 25 },
    '5': { target: 10, mult: 2 },
    '8': { target: 1000, mult: 125 },
    '25': { target: 100, mult: 4 },
    '20': { target: 100, mult: 5 }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-emerald-950/40', 'text-emerald-300', 'border-emerald-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-emerald-950/40', 'text-emerald-300', 'border-emerald-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      const num = parseInt(btn.dataset.num);
      const den = btn.dataset.den;
      const data = scaleMap[den];
      if (!data) return;

      const newNum = num * data.mult;
      const decVal = (newNum / data.target).toFixed(data.target === 10 ? 1 : (data.target === 100 ? 2 : 3));

      targetEl.textContent = data.target;
      multiEl.textContent = `× ${data.mult}`;
      eqEl.innerHTML = `$\\frac{${num}}{${den}} = \\frac{${num} \\times ${data.mult}}{${den} \\times ${data.mult}} = \\frac{${newNum}}{${data.target}} = \\mathbf{${decVal}}$`;

      if (window.triggerMathRender) window.triggerMathRender(eqEl);
    });
  });
}

// 5. Whole Decimal Multiplier
function initWholeDecimalMultiplier() {
  const sizeSlider = document.getElementById('step-size-slider');
  const countSlider = document.getElementById('step-count-slider');
  const sizeVal = document.getElementById('step-size-val');
  const countVal = document.getElementById('step-count-val');
  const svg = document.getElementById('stepper-svg');
  const eq = document.getElementById('stepper-equation');
  if (!sizeSlider || !countSlider || !svg) return;

  function render() {
    const stepSize = parseInt(sizeSlider.value) * 0.1;
    const count = parseInt(countSlider.value);
    sizeVal.textContent = stepSize.toFixed(1);
    countVal.textContent = count;

    const total = stepSize * count;
    const maxVal = Math.max(3.0, Math.ceil(total * 1.3));

    let html = `
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>
      <!-- Base Line -->
      <line x1="20" y1="65" x2="380" y2="65" stroke="#475569" stroke-width="2" />
    `;

    // Ticks
    const numTicks = 6;
    for (let i = 0; i <= numTicks; i++) {
      const tickVal = (i * maxVal) / numTicks;
      const x = 20 + (i / numTicks) * 360;
      html += `
        <line x1="${x}" y1="60" x2="${x}" y2="70" stroke="#94a3b8" stroke-width="1.5" />
        <text x="${x}" y="82" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="monospace">${tickVal.toFixed(1)}</text>
      `;
    }

    // Jumps
    let currentX = 20;
    for (let h = 0; h < count; h++) {
      const nextX = 20 + (((h + 1) * stepSize) / maxVal) * 360;
      const midX = (currentX + nextX) / 2;
      const jumpHeight = 35 - (h % 2) * 5;
      html += `
        <path d="M ${currentX} 65 Q ${midX} ${jumpHeight} ${nextX} 65" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />
        <text x="${midX}" y="${jumpHeight - 4}" fill="#7dd3fc" font-size="8" font-weight="bold" text-anchor="middle">+${stepSize.toFixed(1)}</text>
      `;
      currentX = nextX;
    }

    // Final point marker
    html += `<circle cx="${currentX}" cy="65" r="4" fill="#fbbf24" stroke="#d97706" stroke-width="1.5" />`;

    svg.innerHTML = html;

    const repAdd = Array(count).fill(stepSize.toFixed(1)).join(' + ');
    eq.innerHTML = `$${stepSize.toFixed(1)} \\times ${count} = ${repAdd} = \\mathbf{${total.toFixed(2)}}$`;
    if (window.triggerMathRender) window.triggerMathRender(eq);
  }

  sizeSlider.addEventListener('input', render);
  countSlider.addEventListener('input', render);
  render();
}

// 6. Grid Multiplication Area
function initGridMultiplicationArea() {
  const f1Slider = document.getElementById('grid-f1-slider');
  const f2Slider = document.getElementById('grid-f2-slider');
  const f1Val = document.getElementById('grid-f1-val');
  const f2Val = document.getElementById('grid-f2-val');
  const svg = document.getElementById('unit-grid-svg');
  const resText = document.getElementById('grid-result-text');
  if (!f1Slider || !f2Slider || !svg) return;

  function render() {
    const f1 = parseInt(f1Slider.value); // tenths in rows
    const f2 = parseInt(f2Slider.value); // tenths in cols
    f1Val.textContent = (f1 * 0.1).toFixed(1);
    f2Val.textContent = (f2 * 0.1).toFixed(1);

    const cellSize = 18;
    const startX = 10;
    const startY = 10;

    let html = '';
    // Draw cells
    for (let r = 0; r < 10; r++) {
      for (let c = 0; c < 10; c++) {
        const x = startX + c * cellSize;
        const y = startY + r * cellSize;
        const inR = r < f1;
        const inC = c < f2;

        let fill = '#0f172a';
        let stroke = '#1e293b';

        if (inR && inC) {
          fill = '#10b981'; // Green overlap
          stroke = '#059669';
        } else if (inR) {
          fill = '#0284c7'; // Blue row
          stroke = '#0369a1';
        } else if (inC) {
          fill = '#d97706'; // Amber col
          stroke = '#b45309';
        }

        html += `<rect x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" fill="${fill}" stroke="${stroke}" stroke-width="0.8" rx="1.5" />`;
      }
    }

    svg.innerHTML = html;

    const overlapCount = f1 * f2;
    const prod = (overlapCount / 100).toFixed(2);
    resText.innerHTML = `$0.${f1} \\times 0.${f2} = \\frac{${f1}}{10} \\times \\frac{${f2}}{10} = \\frac{${overlapCount}}{100} = \\mathbf{${prod}}$ (${overlapCount} hundredths)`;
    if (window.triggerMathRender) window.triggerMathRender(resText);
  }

  f1Slider.addEventListener('input', render);
  f2Slider.addEventListener('input', render);
  render();
}

// 7. Multiplication Algorithm Stepper
function initMultiplicationAlgorithmStepper() {
  const buttons = document.querySelectorAll('.btn-alg-sample');
  if (!buttons.length) return;

  const s1 = document.getElementById('alg-step1');
  const s2 = document.getElementById('alg-step2');
  const s3 = document.getElementById('alg-step3');
  const finalEq = document.getElementById('alg-final-eq');

  function calculate(aStr, bStr) {
    const aPlaces = (aStr.split('.')[1] || '').length;
    const bPlaces = (bStr.split('.')[1] || '').length;
    const totalPlaces = aPlaces + bPlaces;

    const aInt = parseInt(aStr.replace('.', ''));
    const bInt = parseInt(bStr.replace('.', ''));
    const intProd = aInt * bInt;

    s1.textContent = `${aInt} × ${bInt} = ${intProd}`;
    s2.textContent = `${aPlaces} (in ${aStr}) + ${bPlaces} (in ${bStr}) = ${totalPlaces} places`;

    let intProdStr = intProd.toString();
    while (intProdStr.length < totalPlaces) {
      intProdStr = '0' + intProdStr;
    }
    const decProd = (intProd / Math.pow(10, totalPlaces)).toFixed(totalPlaces);

    s3.textContent = decProd;
    finalEq.innerHTML = `$\\mathbf{${aStr} \\times ${bStr} = ${decProd}}$`;
    if (window.triggerMathRender) window.triggerMathRender(finalEq);
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-fuchsia-950/40', 'text-fuchsia-300', 'border-fuchsia-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-fuchsia-950/40', 'text-fuchsia-300', 'border-fuchsia-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      calculate(btn.dataset.a, btn.dataset.b);
    });
  });

  calculate('0.12', '0.4');
}

// 8. Magnitude Paradox Scale
function initMagnitudeParadoxScale() {
  const baseSlider = document.getElementById('scale-base-slider');
  const factorSlider = document.getElementById('scale-factor-slider');
  const baseVal = document.getElementById('scale-base-val');
  const factorVal = document.getElementById('scale-factor-val');
  const beamSvg = document.getElementById('scale-beam-svg');
  const verdict = document.getElementById('scale-verdict');
  if (!baseSlider || !factorSlider || !beamSvg) return;

  function render() {
    const base = parseInt(baseSlider.value);
    const factor = parseInt(factorSlider.value) * 0.1;
    baseVal.textContent = base;
    factorVal.textContent = factor.toFixed(1);

    const product = base * factor;
    const diff = product - base;
    const angle = Math.max(-20, Math.min(20, diff * 3));

    let html = `
      <!-- Fulcrum -->
      <polygon points="200,60 185,85 215,85" fill="#475569" stroke="#64748b" stroke-width="1.5" />
      <circle cx="200" cy="60" r="4" fill="#fbbf24" />
      
      <!-- Tilting Beam -->
      <g transform="rotate(${angle}, 200, 60)">
        <line x1="60" y1="60" x2="340" y2="60" stroke="#cbd5e1" stroke-width="3" stroke-linecap="round" />
        
        <!-- Left Pan (Original Base) -->
        <line x1="80" y1="60" x2="80" y2="75" stroke="#94a3b8" stroke-width="1" />
        <rect x="55" y="75" width="50" height="8" rx="2" fill="#38bdf8" />
        <text x="80" y="70" fill="#7dd3fc" font-size="9" font-weight="bold" text-anchor="middle">Base: ${base}</text>
        
        <!-- Right Pan (Product) -->
        <line x1="320" y1="60" x2="320" y2="75" stroke="#94a3b8" stroke-width="1" />
        <rect x="295" y="75" width="50" height="8" rx="2" fill="${factor < 1 ? '#f43f5e' : '#10b981'}" />
        <text x="320" y="70" fill="${factor < 1 ? '#fda4af' : '#6ee7b7'}" font-size="9" font-weight="bold" text-anchor="middle">Prod: ${product.toFixed(1)}</text>
      </g>
    `;

    beamSvg.innerHTML = html;

    if (factor < 1) {
      verdict.innerHTML = `$${base} \\times ${factor.toFixed(1)} = \\mathbf{${product.toFixed(1)}} \\lt ${base}$ <span class="text-rose-400 font-bold">(Multiplier &lt; 1 &rArr; Product Shrunk!)</span>`;
    } else if (factor === 1) {
      verdict.innerHTML = `$${base} \\times 1.0 = \\mathbf{${base}}$ <span class="text-amber-400 font-bold">(Neutral Identity)</span>`;
    } else {
      verdict.innerHTML = `$${base} \\times ${factor.toFixed(1)} = \\mathbf{${product.toFixed(1)}} \\gt ${base}$ <span class="text-emerald-400 font-bold">(Multiplier &gt; 1 &rArr; Product Grew!)</span>`;
    }

    if (window.triggerMathRender) window.triggerMathRender(verdict);
  }

  baseSlider.addEventListener('input', render);
  factorSlider.addEventListener('input', render);
  render();
}

// 9. Power 10 Shift Slider
function initPower10ShiftSlider() {
  let startNum = 73.8;
  let activeDiv = 1;

  const presets = document.querySelectorAll('.btn-shift-preset');
  const divBtns = document.querySelectorAll('.btn-shift-div');
  const resEl = document.getElementById('shift-result-num');
  const expEl = document.getElementById('shift-explanation');
  const startEl = document.getElementById('shift-start-num');

  function update() {
    startEl.textContent = startNum;
    const res = startNum / activeDiv;

    let placesShift = 0;
    if (activeDiv === 10) placesShift = 1;
    if (activeDiv === 100) placesShift = 2;
    if (activeDiv === 1000) placesShift = 3;

    resEl.textContent = `${startNum} ÷ ${activeDiv} = ${res.toFixed(placesShift + 1).replace(/0+$/, '').replace(/\.$/, '')}`;
    expEl.textContent = placesShift === 0 ? "Decimal point remains stationary." : `Decimal point shifted ${placesShift} place${placesShift > 1 ? 's' : ''} to the left.`;
  }

  presets.forEach(btn => {
    btn.addEventListener('click', () => {
      startNum = parseFloat(btn.dataset.val);
      update();
    });
  });

  divBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      divBtns.forEach(b => {
        b.classList.remove('bg-teal-950/40', 'text-teal-300', 'border-teal-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-teal-950/40', 'text-teal-300', 'border-teal-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      activeDiv = parseInt(btn.dataset.div);
      update();
    });
  });

  update();
}

// 10. Place Value Regroup Division
function initPlaceValueRegroupDivision() {
  const buttons = document.querySelectorAll('.btn-regroup-sample');
  if (!buttons.length) return;

  const problemEl = document.getElementById('regroup-problem');
  const quotEl = document.getElementById('regroup-quotient');
  const stepsEl = document.getElementById('regroup-steps');

  const dataMap = {
    '15.6_4': {
      prob: '15.6 ÷ 4',
      quot: '3.9',
      steps: [
        '1. Divide Ones: 15 ÷ 4 = 3 ones (Remainder = 3 ones)',
        '2. Decimal Point: Place point in quotient (3.)',
        '3. Regroup: 3 ones = 30 tenths + 6 tenths = 36 tenths',
        '4. Divide Tenths: 36 tenths ÷ 4 = 9 tenths',
        '5. Complete Result: 3.9 (Remainder 0)'
      ]
    },
    '7.0_2': {
      prob: '7 ÷ 2',
      quot: '3.5',
      steps: [
        '1. Divide Ones: 7 ÷ 2 = 3 ones (Remainder = 1 one)',
        '2. Decimal Point: Place point in quotient (3.)',
        '3. Regroup: 1 one = 10 tenths',
        '4. Divide Tenths: 10 tenths ÷ 2 = 5 tenths',
        '5. Complete Result: 3.5 (Remainder 0)'
      ]
    },
    '7.0_4': {
      prob: '7 ÷ 4',
      quot: '1.75',
      steps: [
        '1. Divide Ones: 7 ÷ 4 = 1 one (Remainder = 3 ones)',
        '2. Regroup: 3 ones = 30 tenths. 30 ÷ 4 = 7 tenths (Rem 2 tenths)',
        '3. Regroup: 2 tenths = 20 hundredths. 20 ÷ 4 = 5 hundredths',
        '4. Complete Result: 1.75 (Terminating decimal)'
      ]
    },
    '18.6_3': {
      prob: '18.6 ÷ 3',
      quot: '6.2',
      steps: [
        '1. Divide Wholes: 18 ÷ 3 = 6 wholes (Rem 0)',
        '2. Decimal Point: Align point in quotient (6.)',
        '3. Divide Tenths: 6 tenths ÷ 3 = 2 tenths',
        '4. Complete Result: 6.2 (Exact division)'
      ]
    }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-indigo-950/40', 'text-indigo-300', 'border-indigo-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-indigo-950/40', 'text-indigo-300', 'border-indigo-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      const key = `${btn.dataset.div}_${btn.dataset.by}`;
      const d = dataMap[key];
      if (!d) return;

      problemEl.textContent = d.prob;
      quotEl.textContent = d.quot;
      stepsEl.innerHTML = d.steps.map(s => `<div class="p-1 bg-slate-900 rounded border border-slate-800 text-slate-300">${s}</div>`).join('');
    });
  });

  // Init default
  const defaultD = dataMap['15.6_4'];
  stepsEl.innerHTML = defaultD.steps.map(s => `<div class="p-1 bg-slate-900 rounded border border-slate-800 text-slate-300">${s}</div>`).join('');
}

// 11. Decimal Divisor Transformer
function initDecimalDivisorTransformer() {
  const buttons = document.querySelectorAll('.btn-trans-sample');
  if (!buttons.length) return;

  const origEl = document.getElementById('trans-orig');
  const factorEl = document.getElementById('trans-factor');
  const transformedEl = document.getElementById('trans-transformed');
  const resultEl = document.getElementById('trans-result');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-purple-950/40', 'text-purple-300', 'border-purple-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-purple-950/40', 'text-purple-300', 'border-purple-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      const num = parseFloat(btn.dataset.num);
      const den = parseFloat(btn.dataset.den);

      const denPlaces = (btn.dataset.den.split('.')[1] || '').length;
      const scale = Math.pow(10, denPlaces);

      const newNum = Math.round(num * scale);
      const newDen = Math.round(den * scale);
      const quot = (newNum / newDen).toFixed(2).replace(/\.00$/, '');

      origEl.textContent = `${btn.dataset.num} ÷ ${btn.dataset.den}`;
      factorEl.textContent = `× ${scale}`;
      transformedEl.textContent = `${newNum} ÷ ${newDen}`;

      resultEl.innerHTML = `$\\frac{${btn.dataset.num}}{${btn.dataset.den}} = \\frac{${newNum}}{${newDen}} = \\mathbf{${quot}}$ ${den < 1 ? '(Magnification: quotient &gt; dividend!)' : ''}`;
      if (window.triggerMathRender) window.triggerMathRender(resultEl);
    });
  });
}

// 12. Cyclic Wheel 142857
function initCyclicWheel142857() {
  const buttons = document.querySelectorAll('.btn-cyclic');
  const svg = document.getElementById('cyclic-wheel-svg');
  const disp = document.getElementById('cyclic-display');
  if (!buttons.length || !svg) return;

  const digits = ['1', '4', '2', '8', '5', '7'];
  const startMap = { 1: 0, 2: 2, 3: 1, 4: 4, 5: 3, 6: 5 }; // starts: 1->1, 2->2, 3->4, 4->5, 5->7, 6->8

  function render(k) {
    const startIndex = startMap[k] || 0;
    const cx = 100, cy = 100, r = 68;

    let html = `
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="3,3" />
    `;

    // Connect arrows
    for (let i = 0; i < 6; i++) {
      const angle1 = (i * 60 - 90) * (Math.PI / 180);
      const angle2 = (((i + 1) % 6) * 60 - 90) * (Math.PI / 180);
      const x1 = cx + (r - 12) * Math.cos(angle1);
      const y1 = cy + (r - 12) * Math.sin(angle1);
      const x2 = cx + (r - 12) * Math.cos(angle2);
      const y2 = cy + (r - 12) * Math.sin(angle2);
      html += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#64748b" stroke-width="1.2" opacity="0.6" />`;
    }

    // Nodes
    let cycleStr = '';
    for (let i = 0; i < 6; i++) {
      const actualIdx = (startIndex + i) % 6;
      cycleStr += digits[actualIdx];

      const angle = (actualIdx * 60 - 90) * (Math.PI / 180);
      const nx = cx + r * Math.cos(angle);
      const ny = cy + r * Math.sin(angle);
      const isStart = (i === 0);

      html += `
        <circle cx="${nx}" cy="${ny}" r="${isStart ? 14 : 11}" fill="${isStart ? '#ec4899' : '#1e293b'}" stroke="${isStart ? '#f472b6' : '#475569'}" stroke-width="2" />
        <text x="${nx}" y="${ny + 4}" fill="${isStart ? '#ffffff' : '#e2e8f0'}" font-size="${isStart ? 13 : 11}" font-weight="bold" text-anchor="middle" font-family="monospace">${digits[actualIdx]}</text>
      `;
    }

    svg.innerHTML = html;
    disp.innerHTML = `$\\frac{${k}}{7} = 0.\\overline{\\mathbf{${cycleStr}}}$ (Cycle starts at digit ${digits[startIndex]})`;
    if (window.triggerMathRender) window.triggerMathRender(disp);
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-pink-950/40', 'text-pink-300', 'border-pink-700/50');
        b.classList.add('bg-slate-800', 'text-slate-300', 'border-slate-700');
      });
      btn.classList.add('bg-pink-950/40', 'text-pink-300', 'border-pink-700/50');
      btn.classList.remove('bg-slate-800', 'text-slate-300', 'border-slate-700');

      render(parseInt(btn.dataset.k));
    });
  });

  render(1);
}

// 13. Earth Orbit Drift
function initEarthOrbitDrift() {
  const slider = document.getElementById('orbit-years-slider');
  const yearsVal = document.getElementById('orbit-years-val');
  const svg = document.getElementById('orbit-svg');
  const extraEl = document.getElementById('orbit-extra-days');
  const slipEl = document.getElementById('orbit-slip-status');
  if (!slider || !svg) return;

  function render() {
    const years = parseInt(slider.value);
    yearsVal.textContent = `${years} yrs`;

    const extra = years * 0.2422;
    extraEl.textContent = `${extra.toFixed(4)} days`;

    const daysLate = Math.round(extra);
    slipEl.textContent = `~${daysLate} day${daysLate !== 1 ? 's' : ''} late`;

    const angle = ((years * 0.2422) % 1) * 360;
    const rad = (angle - 90) * (Math.PI / 180);
    const ex = 200 + 75 * Math.cos(rad);
    const ey = 50 + 35 * Math.sin(rad);

    let html = `
      <!-- Sun -->
      <circle cx="200" cy="50" r="14" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
      <text x="200" y="54" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">Sun</text>
      
      <!-- Elliptical Orbit Track -->
      <ellipse cx="200" cy="50" rx="75" ry="35" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3" />
      
      <!-- Calender 365 Point -->
      <line x1="200" y1="10" x2="200" y2="20" stroke="#06b6d4" stroke-width="2" />
      <text x="200" y="8" fill="#38bdf8" font-size="8" text-anchor="middle">Nominal Calendar Marker</text>
      
      <!-- True Earth Position -->
      <circle cx="${ex}" cy="${ey}" r="6" fill="#3b82f6" stroke="#93c5fd" stroke-width="1.5" />
      <text x="${ex}" y="${ey + 14}" fill="#bfdbfe" font-size="8" text-anchor="middle">Earth</text>
    `;

    svg.innerHTML = html;
  }

  slider.addEventListener('input', render);
  render();
}

// 14. Leap Year Decision Tree
function initLeapYearDecisionTree() {
  const input = document.getElementById('leap-input-year');
  const btn = document.getElementById('btn-test-leap');
  const quickBtns = document.querySelectorAll('.btn-year-quick');

  const g4 = document.getElementById('leap-gate-4');
  const g100 = document.getElementById('leap-gate-100');
  const g400 = document.getElementById('leap-gate-400');
  const ans4 = document.getElementById('gate-4-ans');
  const ans100 = document.getElementById('gate-100-ans');
  const ans400 = document.getElementById('gate-400-ans');
  const verdict = document.getElementById('leap-final-verdict');

  function evaluate(year) {
    if (isNaN(year)) return;
    input.value = year;

    const div4 = (year % 4 === 0);
    const div100 = (year % 100 === 0);
    const div400 = (year % 400 === 0);

    // Reset styles
    [g4, g100, g400].forEach(g => {
      g.className = 'p-2 rounded border border-slate-800 bg-slate-950/70 text-slate-400';
    });

    ans4.textContent = div4 ? `Yes (${year} ÷ 4 = ${year/4})` : `No (Remainder ${year % 4})`;
    g4.className = `p-2 rounded border ${div4 ? 'border-emerald-600 bg-emerald-950/30 text-emerald-300' : 'border-rose-600 bg-rose-950/30 text-rose-300'}`;

    if (!div4) {
      ans100.textContent = 'Skipped';
      ans400.textContent = 'Skipped';
      verdict.className = 'p-2.5 rounded-xl border border-rose-600 bg-rose-950/40 text-center font-bold text-sm text-rose-300';
      verdict.textContent = `❌ ${year} is NOT a leap year (365 Days, not divisible by 4)`;
      return;
    }

    ans100.textContent = div100 ? `Yes (${year} is a Century year)` : `No (${year} is not a century)`;
    g100.className = `p-2 rounded border ${div100 ? 'border-amber-600 bg-amber-950/30 text-amber-300' : 'border-emerald-600 bg-emerald-950/30 text-emerald-300'}`;

    if (!div100) {
      ans400.textContent = 'Not Applicable';
      verdict.className = 'p-2.5 rounded-xl border border-emerald-600 bg-emerald-950/40 text-center font-bold text-sm text-emerald-300';
      verdict.textContent = `🎉 ${year} IS A LEAP YEAR (366 Days, Feb 29 exists)`;
      return;
    }

    ans400.textContent = div400 ? `Yes (${year} ÷ 400 = ${year/400})` : `No (${year} ÷ 400 has remainder)`;
    g400.className = `p-2 rounded border ${div400 ? 'border-emerald-600 bg-emerald-950/30 text-emerald-300' : 'border-rose-600 bg-rose-950/30 text-rose-300'}`;

    if (div400) {
      verdict.className = 'p-2.5 rounded-xl border border-emerald-600 bg-emerald-950/40 text-center font-bold text-sm text-emerald-300';
      verdict.textContent = `🎉 ${year} IS A LEAP YEAR (400-Year Century Override)`;
    } else {
      verdict.className = 'p-2.5 rounded-xl border border-rose-600 bg-rose-950/40 text-center font-bold text-sm text-rose-300';
      verdict.textContent = `❌ ${year} is NOT a leap year (Century year not divisible by 400)`;
    }
  }

  if (btn) btn.addEventListener('click', () => evaluate(parseInt(input.value)));
  quickBtns.forEach(b => b.addEventListener('click', () => evaluate(parseInt(b.dataset.y))));
  evaluate(2024);
}

// 15. Hidato Grid Puzzle
function initHidatoGridPuzzle() {
  const boardEl = document.getElementById('hidato-board');
  const nextValEl = document.getElementById('hidato-next-val');
  const statusEl = document.getElementById('hidato-status');
  const btnHint = document.getElementById('btn-hidato-hint');
  const btnSolve = document.getElementById('btn-hidato-solve');
  const btnReset = document.getElementById('btn-hidato-reset');
  if (!boardEl) return;

  // 4x4 Hidato solution path
  const solution = [
    [1,  2,  3,  4],
    [8,  7,  6,  5],
    [9,  10, 15, 16],
    [12, 11, 14, 13]
  ];

  const given = {
    '0,0': 1,
    '0,3': 4,
    '1,0': 8,
    '3,0': 12,
    '2,3': 16
  };

  let gridState = {};
  let currentNum = 2;

  function renderBoard() {
    boardEl.innerHTML = '';
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 4; c++) {
        const key = `${r},${c}`;
        const isGiven = given[key] !== undefined;
        const val = isGiven ? given[key] : (gridState[key] || '');

        const cell = document.createElement('div');
        cell.className = `w-11 h-11 rounded-lg flex items-center justify-center font-bold font-mono text-sm cursor-pointer border transition-all ${
          isGiven 
            ? 'bg-indigo-900/60 text-indigo-200 border-indigo-500/50' 
            : (val ? 'bg-slate-800 text-cyan-300 border-cyan-500/40' : 'bg-slate-900/80 text-slate-500 border-slate-800 hover:border-slate-600')
        }`;
        cell.textContent = val;

        if (!isGiven) {
          cell.addEventListener('click', () => {
            if (val) {
              delete gridState[key];
            } else {
              gridState[key] = currentNum;
              findNextNumber();
            }
            renderBoard();
            checkVictory();
          });
        }

        boardEl.appendChild(cell);
      }
    }
  }

  function findNextNumber() {
    for (let n = 1; n <= 16; n++) {
      let found = false;
      for (let k in given) { if (given[k] === n) found = true; }
      for (let k in gridState) { if (gridState[k] === n) found = true; }
      if (!found) {
        currentNum = n;
        nextValEl.textContent = currentNum;
        return;
      }
    }
    nextValEl.textContent = 'Done!';
  }

  function checkVictory() {
    let filled = 0;
    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 4; c++) {
        const key = `${r},${c}`;
        const val = given[key] || gridState[key];
        if (val === solution[r][c]) filled++;
      }
    }
    if (filled === 16) {
      statusEl.innerHTML = `<span class="text-emerald-400 font-bold">🎉 Hidato Path Solved! All 16 consecutive links complete!</span>`;
    }
  }

  if (btnHint) {
    btnHint.addEventListener('click', () => {
      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          const key = `${r},${c}`;
          if (solution[r][c] === currentNum && !given[key]) {
            gridState[key] = currentNum;
            findNextNumber();
            renderBoard();
            checkVictory();
            return;
          }
        }
      }
    });
  }

  if (btnSolve) {
    btnSolve.addEventListener('click', () => {
      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          const key = `${r},${c}`;
          if (!given[key]) gridState[key] = solution[r][c];
        }
      }
      findNextNumber();
      renderBoard();
      checkVictory();
    });
  }

  if (btnReset) {
    btnReset.addEventListener('click', () => {
      gridState = {};
      currentNum = 2;
      nextValEl.textContent = '2';
      statusEl.textContent = 'Click empty cells to enter numbers in sequence. Next number to place: 2';
      renderBoard();
    });
  }

  renderBoard();
}

// 16. Madhava Decimal Series
function initMadhavaDecimalSeries() {
  const slider = document.getElementById('madhava-terms-slider');
  const termsVal = document.getElementById('madhava-terms-val');
  const approxEl = document.getElementById('madhava-pi-approx');
  const statusEl = document.getElementById('madhava-status');
  if (!slider || !approxEl) return;

  function update() {
    const N = parseInt(slider.value);
    termsVal.textContent = N;

    let sum = 0;
    for (let k = 0; k < N; k++) {
      const term = Math.pow(-1, k) / (2 * k + 1);
      sum += term;
    }
    const approxPi = (4 * sum).toFixed(7);

    // Exact: 3.1415926
    const exact = "3.1415926";
    let formatted = '';
    for (let i = 0; i < approxPi.length; i++) {
      if (approxPi[i] === exact[i]) {
        formatted += `<span class="text-emerald-400 font-bold">${approxPi[i]}</span>`;
      } else {
        formatted += `<span class="text-slate-400">${approxPi[i]}</span>`;
      }
    }

    approxEl.innerHTML = formatted;
    statusEl.innerHTML = `Computed with $N = ${N}$ terms. Kerala School expansions converge monotonically!`;
    if (window.triggerMathRender) window.triggerMathRender(statusEl);
  }

  slider.addEventListener('input', update);
  update();
}
"""

output_path = '.agents/class7_math_another_peek_beyond_the_point_js.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nSimulator JavaScript engines for Class 7 Mathematics - Another Peek Beyond the Point\n"""\n\n')
    f.write("SIMULATORS_JS = " + repr(simulators_js) + "\n")

print(f"Generated {output_path} successfully!")


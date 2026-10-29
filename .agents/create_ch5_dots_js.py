#!/usr/bin/env python3
"""
Generates the interactive JavaScript engines for the 16 laboratory simulators
for NCERT Class 7 Mathematics - Chapter 5: Connecting the Dots...
"""

JS_CONTENT = r'''
function initSimulators() {
  initQuestionsClassifier();
  initStatementsAnalyzer();
  initFairShareBalancer();
  initMeanBalanceBeam();
  initDotPlotGenerator();
  initOutlierDisrupter();
  initMedianFinder();
  initHeightDistribution();
  initTimeEstimator();
  initGraphTypeSelector();
  initDoubleBarBuilder();
  initMultistepExtractor();
  initGrowthTrendsTracker();
  initMisleadingGraphBuster();
  initDataDetectiveHub();
}
window.initSimulators = initSimulators;

// 1. Questions Classifier
function initQuestionsClassifier() {
  const cardText = document.getElementById('qc-card-text');
  const cardHint = document.getElementById('qc-card-hint');
  const btnNonStat = document.getElementById('qc-btn-nonstat');
  const btnStat = document.getElementById('qc-btn-stat');
  const feedback = document.getElementById('qc-feedback');
  const idxDisplay = document.getElementById('qc-idx');
  const scorePill = document.getElementById('qc-score-pill');
  const btnNext = document.getElementById('qc-btn-next');

  if (!cardText || !btnStat) return;

  const questions = [
    {
      text: "How many books did each student in your class read this summer?",
      isStat: true,
      hint: "Will the answer vary from student to student?",
      exp: "Statistical! Reading habits vary across different students, generating a data distribution."
    },
    {
      text: "How tall is Mount Everest?",
      isStat: false,
      hint: "Is this a fixed geographical measurement?",
      exp: "Non-Statistical! Mount Everest has a single fixed height (8,848.86 m) with no variability."
    },
    {
      text: "What are the monthly prices of onions in Delhi over the past year?",
      isStat: true,
      hint: "Do market prices fluctuate over months?",
      exp: "Statistical! Market prices fluctuate month-to-month due to supply, rainfall, and demand."
    },
    {
      text: "What is the capital of India?",
      isStat: false,
      hint: "Can this question yield multiple varying values?",
      exp: "Non-Statistical! New Delhi is the single, deterministic answer."
    },
    {
      text: "How much time do students spend commuting to school each morning?",
      isStat: true,
      hint: "Do all students live at the exact same distance?",
      exp: "Statistical! Commute times differ widely based on distance and transportation mode."
    },
    {
      text: "How many days are in the month of July?",
      isStat: false,
      hint: "Does July's calendar length ever change?",
      exp: "Non-Statistical! July always has exactly 31 days in all years."
    }
  ];

  let currentQ = 0;
  let score = 0;
  let answered = false;

  function loadCard(idx) {
    answered = false;
    currentQ = idx;
    idxDisplay.textContent = idx + 1;
    const q = questions[idx];
    cardText.textContent = `"${q.text}"`;
    cardHint.textContent = `Consider: ${q.hint}`;
    feedback.className = 'p-2 rounded-lg text-xs text-center min-h-[36px] flex items-center justify-center bg-slate-950/60 border border-slate-800 text-slate-300';
    feedback.textContent = 'Click a category above to classify the displayed question.';
    btnStat.disabled = false;
    btnNonStat.disabled = false;
  }

  function handleAnswer(userChoice) {
    if (answered) return;
    answered = true;
    btnStat.disabled = true;
    btnNonStat.disabled = true;

    const q = questions[currentQ];
    if (userChoice === q.isStat) {
      score++;
      if (window.sfx && window.sfx.playCorrect) window.sfx.playCorrect();
      feedback.className = 'p-2 rounded-lg text-xs text-center min-h-[36px] flex items-center justify-center bg-emerald-950/40 border border-emerald-500/50 text-emerald-300 font-semibold';
      feedback.innerHTML = `✓ Correct! ${q.exp}`;
    } else {
      if (window.sfx && window.sfx.playWrong) window.sfx.playWrong();
      feedback.className = 'p-2 rounded-lg text-xs text-center min-h-[36px] flex items-center justify-center bg-rose-950/40 border border-rose-500/50 text-rose-300 font-semibold';
      feedback.innerHTML = `✗ Not quite. ${q.exp}`;
    }

    scorePill.textContent = `Score: ${score} / ${questions.length}`;
  }

  btnStat.onclick = () => handleAnswer(true);
  btnNonStat.onclick = () => handleAnswer(false);

  btnNext.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    loadCard((currentQ + 1) % questions.length);
  };

  loadCard(0);
}

// 2. Statements Analyzer (Sample Size & Credibility)
function initStatementsAnalyzer() {
  const slider = document.getElementById('sa-sample-slider');
  const sampleVal = document.getElementById('sa-sample-val');
  const errorVal = document.getElementById('sa-error-val');
  const errorBar = document.getElementById('sa-error-bar');
  const verdict = document.getElementById('sa-verdict');

  if (!slider) return;

  function update() {
    const n = parseInt(slider.value);
    sampleVal.textContent = `${n} households`;

    // Margin of error approx: 1 / sqrt(n)
    const moe = Math.min(45, (1 / Math.sqrt(n)) * 100).toFixed(1);
    errorVal.textContent = `±${moe}%`;

    const barWidth = Math.min(100, Math.max(5, (moe / 45) * 100));
    errorBar.style.width = `${barWidth}%`;

    if (n < 30) {
      verdict.textContent = "Unreliable (Tiny sample can swing widely by chance)";
      verdict.className = "font-bold text-rose-400";
      errorBar.className = "bg-rose-500 h-full";
    } else if (n < 150) {
      verdict.textContent = "Moderate Reliability (Acceptable for school project)";
      verdict.className = "font-bold text-amber-400";
      errorBar.className = "bg-amber-500 h-full";
    } else {
      verdict.textContent = "Highly Reliable & Statistically Robust!";
      verdict.className = "font-bold text-emerald-400";
      errorBar.className = "bg-emerald-500 h-full";
    }
  }

  slider.addEventListener('input', update);
  update();
}

// 3. Fair-Share Balancer (Samamiti / Samīkaraṇa)
function initFairShareBalancer() {
  const colA = document.getElementById('fs-col-a');
  const colB = document.getElementById('fs-col-b');
  const colC = document.getElementById('fs-col-c');
  const colD = document.getElementById('fs-col-d');
  const valA = document.getElementById('fs-val-a');
  const valB = document.getElementById('fs-val-b');
  const valC = document.getElementById('fs-val-c');
  const valD = document.getElementById('fs-val-d');
  const mathBox = document.getElementById('fs-math-box');
  const btnLevel = document.getElementById('fs-btn-level');
  const btnStep = document.getElementById('fs-btn-step');
  const btnReset = document.getElementById('fs-btn-reset');

  if (!colA || !btnLevel) return;

  let values = [14, 6, 12, 8];
  const initial = [14, 6, 12, 8];
  const targetMean = 10;

  function renderCols() {
    valA.textContent = values[0];
    valB.textContent = values[1];
    valC.textContent = values[2];
    valD.textContent = values[3];

    colA.style.height = `${values[0] * 8}px`;
    colB.style.height = `${values[1] * 8}px`;
    colC.style.height = `${values[2] * 8}px`;
    colD.style.height = `${values[3] * 8}px`;

    const isLeveled = values.every(v => v === targetMean);
    if (isLeveled) {
      mathBox.innerHTML = `<b>✨ Leveled! (Samīkaraṇa achieved)</b> Every friend now holds exactly $\\mathbf{${targetMean}}$ blocks.`;
      mathBox.className = "p-2.5 bg-emerald-950/40 rounded-xl border border-emerald-500/50 text-xs font-mono text-center text-emerald-300";
    } else {
      mathBox.innerHTML = `Total Blocks = $${values[0]} + ${values[1]} + ${values[2]} + ${values[3]} = 40$ blocks | $\\text{Mean} = \\frac{40}{4} = \\mathbf{10}$`;
      mathBox.className = "p-2.5 bg-slate-800/80 rounded-xl border border-slate-700 text-xs font-mono text-center text-amber-200";
    }
    if (window.triggerMathRender) window.triggerMathRender(mathBox);
  }

  btnLevel.onclick = () => {
    if (window.sfx && window.sfx.playCorrect) window.sfx.playCorrect();
    values = [10, 10, 10, 10];
    renderCols();
  };

  btnStep.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    // Move 1 from max to min
    let maxIdx = 0, minIdx = 0;
    for (let i = 1; i < 4; i++) {
      if (values[i] > values[maxIdx]) maxIdx = i;
      if (values[i] < values[minIdx]) minIdx = i;
    }
    if (values[maxIdx] > targetMean && values[minIdx] < targetMean) {
      values[maxIdx] -= 2;
      values[minIdx] += 2;
    } else {
      values = [10, 10, 10, 10];
    }
    renderCols();
  };

  btnReset.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    values = [...initial];
    renderCols();
  };

  renderCols();
}

// 4. Mean Balance Beam (Fulcrum Seesaw)
function initMeanBalanceBeam() {
  const svg = document.getElementById('bb-svg');
  const weightsList = document.getElementById('bb-weights-list');
  const meanDisplay = document.getElementById('bb-mean-display');
  const btnClear = document.getElementById('bb-btn-clear');

  if (!svg) return;

  let weights = [4, 8, 12, 16];

  function renderSeesaw() {
    const sum = weights.reduce((a, b) => a + b, 0);
    const mean = weights.length > 0 ? (sum / weights.length) : 10;

    weightsList.textContent = `[${weights.join(', ')}]`;
    meanDisplay.textContent = `Mean = ${mean.toFixed(1)}`;

    const width = 340;
    const startX = 30;
    const endX = 310;
    const beamY = 70;

    // Convert value (0 to 20) to SVG X
    function valToX(v) {
      return startX + (v / 20) * (endX - startX);
    }

    const fulcrumX = valToX(mean);

    let html = `
      <!-- Base Horizon Ground -->
      <line x1="20" y1="120" x2="320" y2="120" stroke="#334155" stroke-width="2" />

      <!-- Fulcrum Triangle -->
      <polygon points="${fulcrumX},${beamY} ${fulcrumX - 14},120 ${fulcrumX + 14},120" fill="#f59e0b" stroke="#d97706" stroke-width="1.5" />
      <circle cx="${fulcrumX}" cy="${beamY}" r="4" fill="#fbbf24" />
      <text x="${fulcrumX}" y="135" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">Mean: ${mean.toFixed(1)}</text>

      <!-- Balanced Beam -->
      <line x1="${startX - 10}" y1="${beamY}" x2="${endX + 10}" y2="${beamY}" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />

      <!-- Ruler Ticks -->
    `;

    for (let i = 0; i <= 20; i += 2) {
      const x = valToX(i);
      html += `
        <line x1="${x}" y1="${beamY - 4}" x2="${x}" y2="${beamY + 4}" stroke="#64748b" stroke-width="1.2" />
        <text x="${x}" y="${beamY + 14}" fill="#94a3b8" font-size="8" text-anchor="middle" font-family="monospace">${i}</text>
      `;
    }

    // Stack weights at positions
    const counts = {};
    weights.forEach(w => { counts[w] = (counts[w] || 0) + 1; });

    Object.keys(counts).forEach(wStr => {
      const w = parseInt(wStr);
      const c = counts[w];
      const x = valToX(w);
      for (let stack = 0; stack < c; stack++) {
        const cy = beamY - 8 - (stack * 12);
        html += `
          <rect x="${x - 5}" y="${cy - 8}" width="10" height="10" rx="2" fill="#06b6d4" stroke="#0891b2" stroke-width="1" />
        `;
      }
    });

    svg.innerHTML = html;
  }

  svg.onclick = (e) => {
    const rect = svg.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const startX = 30;
    const endX = 310;
    const rawVal = Math.round(((clickX - startX) / (endX - startX)) * 20);
    const clamped = Math.max(0, Math.min(20, rawVal));

    if (weights.length >= 10) weights.shift();
    weights.push(clamped);
    weights.sort((a, b) => a - b);
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    renderSeesaw();
  };

  btnClear.onclick = () => {
    weights = [10];
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    renderSeesaw();
  };

  renderSeesaw();
}

// 6. Dot Plot Frequency Generator
function initDotPlotGenerator() {
  const svg = document.getElementById('dp-svg');
  const countEl = document.getElementById('dp-count');
  const rangeEl = document.getElementById('dp-range');
  const meanEl = document.getElementById('dp-mean');
  const modeEl = document.getElementById('dp-mode');
  const btnSample = document.getElementById('dp-btn-sample');
  const btnReset = document.getElementById('dp-btn-reset');

  if (!svg) return;

  let values = [];

  function renderPlot() {
    const minVal = 10;
    const maxVal = 30;
    const startX = 25;
    const endX = 315;
    const axisY = 120;

    function valToX(v) {
      return startX + ((v - minVal) / (maxVal - minVal)) * (endX - startX);
    }

    let html = `
      <!-- Axis Line -->
      <line x1="${startX - 10}" y1="${axisY}" x2="${endX + 10}" y2="${axisY}" stroke="#475569" stroke-width="2" />
    `;

    for (let i = minVal; i <= maxVal; i += 2) {
      const x = valToX(i);
      html += `
        <line x1="${x}" y1="${axisY - 4}" x2="${x}" y2="${axisY + 4}" stroke="#64748b" stroke-width="1.2" />
        <text x="${x}" y="${axisY + 14}" fill="#94a3b8" font-size="8" text-anchor="middle" font-family="monospace">${i}</text>
      `;
    }

    // Stack dots
    const counts = {};
    values.forEach(v => { counts[v] = (counts[v] || 0) + 1; });

    Object.keys(counts).forEach(vStr => {
      const v = parseInt(vStr);
      const c = counts[v];
      const x = valToX(v);
      for (let s = 0; s < c; s++) {
        const cy = axisY - 8 - (s * 11);
        html += `
          <circle cx="${x}" cy="${cy}" r="4.5" fill="#14b8a6" stroke="#0d9488" stroke-width="1.2" />
        `;
      }
    });

    svg.innerHTML = html;

    // Update Metrics
    if (values.length === 0) {
      countEl.textContent = '0';
      rangeEl.textContent = '-';
      meanEl.textContent = '-';
      modeEl.textContent = '-';
      return;
    }

    countEl.textContent = values.length;
    const min = Math.min(...values);
    const max = Math.max(...values);
    rangeEl.textContent = `${max - min}`;
    const sum = values.reduce((a, b) => a + b, 0);
    meanEl.textContent = (sum / values.length).toFixed(1);

    // Mode
    let bestCount = 0;
    let modeVal = '-';
    Object.keys(counts).forEach(k => {
      if (counts[k] > bestCount) {
        bestCount = counts[k];
        modeVal = k;
      }
    });
    modeEl.textContent = bestCount > 1 ? modeVal : 'None';
  }

  svg.onclick = (e) => {
    const rect = svg.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const startX = 25;
    const endX = 315;
    const rawVal = Math.round(10 + ((clickX - startX) / (endX - startX)) * 20);
    const clamped = Math.max(10, Math.min(30, rawVal));

    values.push(clamped);
    values.sort((a, b) => a - b);
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    renderPlot();
  };

  btnSample.onclick = () => {
    values = [12, 14, 14, 16, 16, 16, 18, 18, 20, 22, 28];
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    renderPlot();
  };

  btnReset.onclick = () => {
    values = [];
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    renderPlot();
  };

  renderPlot();
}

// 7. Outlier Disruption Simulator
function initOutlierDisrupter() {
  const slider = document.getElementById('od-slider');
  const outlierVal = document.getElementById('od-outlier-val');
  const meanVal = document.getElementById('od-mean-val');
  const meanShift = document.getElementById('od-mean-shift');
  const medianVal = document.getElementById('od-median-val');
  const medianShift = document.getElementById('od-median-shift');

  if (!slider) return;

  const baseSalaries = [10, 11, 10, 12, 11];

  function update() {
    const executive = parseInt(slider.value);
    outlierVal.textContent = `₹${executive},000`;

    const all = [...baseSalaries, executive];
    all.sort((a, b) => a - b);

    // Mean
    const sum = all.reduce((a, b) => a + b, 0);
    const mean = (sum / all.length);
    meanVal.textContent = `₹${(mean * 1000).toLocaleString('en-IN', {maximumFractionDigits: 0})}`;

    const baseMean = 10.8;
    const pctShift = Math.round(((mean - baseMean) / baseMean) * 100);
    meanShift.textContent = `+${pctShift}% inflated by outlier!`;

    // Median (6 items: 3rd and 4th average)
    const mid1 = all[2];
    const mid2 = all[3];
    const median = (mid1 + mid2) / 2;
    medianVal.textContent = `₹${(median * 1000).toLocaleString('en-IN', {maximumFractionDigits: 0})}`;

    if (executive > 50) {
      medianShift.textContent = "Unmoved & True (Rock-Steady)";
      medianShift.className = "text-[10px] text-emerald-300 block mt-1 font-bold";
    } else {
      medianShift.textContent = "Stable middle value";
      medianShift.className = "text-[10px] text-slate-400 block mt-1";
    }
  }

  slider.addEventListener('input', update);
  update();
}

// 8. Median Finder (Step-by-step Sort & Locate)
function initMedianFinder() {
  const container = document.getElementById('mf-cards-container');
  const btnSort = document.getElementById('mf-btn-sort');
  const btnLocate = document.getElementById('mf-btn-locate');
  const btnOdd = document.getElementById('mf-btn-odd');
  const btnEven = document.getElementById('mf-btn-even');
  const expBox = document.getElementById('mf-explanation');

  if (!container || !btnSort) return;

  let isOdd = true;
  let items = [14, 8, 22, 16, 5, 19, 11];

  function renderCards(highlightIdx = []) {
    container.innerHTML = '';
    items.forEach((num, idx) => {
      const card = document.createElement('div');
      const isHighlighted = highlightIdx.includes(idx);
      card.className = `w-10 h-12 rounded-lg flex items-center justify-center font-mono font-bold text-sm transition-all duration-300 ${
        isHighlighted
          ? 'bg-emerald-500 text-slate-950 scale-110 shadow-lg shadow-emerald-500/40 border-2 border-white'
          : 'bg-slate-800 text-cyan-300 border border-slate-700'
      }`;
      card.textContent = num;
      container.appendChild(card);
    });
  }

  btnOdd.onclick = () => {
    isOdd = true;
    items = [14, 8, 22, 16, 5, 19, 11];
    btnOdd.className = "px-2 py-0.5 rounded bg-emerald-600 text-white font-bold text-[11px]";
    btnEven.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    btnSort.disabled = false;
    btnLocate.disabled = true;
    expBox.textContent = 'Odd dataset loaded (n = 7). Click "1. Sort Ascending".';
    renderCards();
  };

  btnEven.onclick = () => {
    isOdd = false;
    items = [12, 18, 6, 24, 14, 10];
    btnEven.className = "px-2 py-0.5 rounded bg-emerald-600 text-white font-bold text-[11px]";
    btnOdd.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    btnSort.disabled = false;
    btnLocate.disabled = true;
    expBox.textContent = 'Even dataset loaded (n = 6). Click "1. Sort Ascending".';
    renderCards();
  };

  btnSort.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    items.sort((a, b) => a - b);
    btnSort.disabled = true;
    btnLocate.disabled = false;
    expBox.textContent = `Sorted in order: [${items.join(', ')}]. Now click "2. Locate Median".`;
    renderCards();
  };

  btnLocate.onclick = () => {
    if (window.sfx && window.sfx.playCorrect) window.sfx.playCorrect();
    if (isOdd) {
      const mid = Math.floor(items.length / 2);
      renderCards([mid]);
      expBox.innerHTML = `Middle position $\\frac{7+1}{2} = 4\\text{th}$ item. $\\mathbf{\\text{Median} = ${items[mid]}}$.`;
    } else {
      const mid1 = (items.length / 2) - 1;
      const mid2 = items.length / 2;
      renderCards([mid1, mid2]);
      const med = (items[mid1] + items[mid2]) / 2;
      expBox.innerHTML = `Middle two items are $${items[mid1]}$ and $${items[mid2]}$. $\\text{Median} = \\frac{${items[mid1]} + ${items[mid2]}}{2} = \\mathbf{${med}}$.`;
    }
    if (window.triggerMathRender) window.triggerMathRender(expBox);
  };

  renderCards();
}

// 9. Classroom Height Distribution
function initHeightDistribution() {
  const svg = document.getElementById('hd-svg');
  if (!svg) return;

  const bins = [
    { label: "130-135", count: 2 },
    { label: "136-140", count: 4 },
    { label: "141-145", count: 7 }, // Peak / mode
    { label: "146-150", count: 4 },
    { label: "151-155", count: 2 },
    { label: "156-160", count: 1 }
  ];

  const maxCount = 8;
  const startX = 35;
  const barW = 42;
  const gap = 6;
  const baseY = 115;

  let html = `
    <!-- Baseline -->
    <line x1="20" y1="${baseY}" x2="330" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
  `;

  bins.forEach((b, i) => {
    const x = startX + i * (barW + gap);
    const h = (b.count / maxCount) * 85;
    const y = baseY - h;

    html += `
      <!-- Bar -->
      <rect x="${x}" y="${y}" width="${barW}" height="${h}" rx="3" fill="#0d9488" stroke="#14b8a6" stroke-width="1" />
      <text x="${x + barW / 2}" y="${y - 4}" fill="#5eead4" font-size="9" font-weight="bold" text-anchor="middle" font-family="monospace">${b.count}</text>
      <text x="${x + barW / 2}" y="${baseY + 12}" fill="#94a3b8" font-size="7.5" text-anchor="middle" font-family="monospace">${b.label}</text>
    `;
  });

  // Median / Mean line at 144.5 (in bin 3)
  const lineX = startX + 2.6 * (barW + gap);
  html += `
    <line x1="${lineX}" y1="15" x2="${lineX}" y2="${baseY}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3" />
    <text x="${lineX}" y="12" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Mean: 144.5 cm</text>
  `;

  svg.innerHTML = html;
}

// 10. Time Estimation Stopwatch Experiment
function initTimeEstimator() {
  const display = document.getElementById('te-timer-display');
  const promptText = document.getElementById('te-prompt-text');
  const btnStart = document.getElementById('te-btn-start');
  const btnStop = document.getElementById('te-btn-stop');
  const trialCount = document.getElementById('te-trial-count');
  const classMean = document.getElementById('te-class-mean');

  if (!display || !btnStart) return;

  let timerId = null;
  let startTime = 0;
  let trials = [25.2, 28.1, 31.4, 27.8, 29.5, 33.1, 26.0, 28.9, 30.2, 27.5, 29.0, 28.4];

  btnStart.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    btnStart.disabled = true;
    btnStop.disabled = false;
    display.textContent = "⏱️ Testing...";
    display.className = "font-mono font-black text-2xl text-slate-400 tracking-wider animate-pulse";
    promptText.textContent = "Count 30 seconds silently in your head. Hit STOP when ready!";
    startTime = Date.now();
  };

  btnStop.onclick = () => {
    const elapsedMs = Date.now() - startTime;
    const elapsedSec = (elapsedMs / 1000).toFixed(1);
    btnStart.disabled = false;
    btnStop.disabled = true;

    trials.push(parseFloat(elapsedSec));
    const sum = trials.reduce((a, b) => a + b, 0);
    const mean = (sum / trials.length).toFixed(1);

    display.textContent = `${elapsedSec}s`;
    display.className = "font-mono font-black text-3xl text-emerald-400 tracking-wider";

    const diff = (elapsedSec - 30.0).toFixed(1);
    promptText.innerHTML = `Your guess was <b>${elapsedSec}s</b> (Error: ${diff > 0 ? '+' + diff : diff}s).`;

    trialCount.textContent = `${trials.length} trials`;
    classMean.textContent = `${mean} seconds`;

    if (window.sfx && window.sfx.playCorrect) window.sfx.playCorrect();
  };
}

// 11. Single vs Double Bar Graph Visualizer
function initGraphTypeSelector() {
  const svg = document.getElementById('gt-svg');
  const btnSingle = document.getElementById('gt-btn-single');
  const btnDouble = document.getElementById('gt-btn-double');
  const infoBox = document.getElementById('gt-info-box');

  if (!svg || !btnSingle) return;

  let isDouble = true;

  function render() {
    const sports = ["Cricket", "Football", "Badminton"];
    const boys = [60, 45, 35];
    const girls = [20, 35, 55];
    const maxVal = 70;
    const startX = 40;
    const clusterW = 65;
    const gap = 30;
    const baseY = 120;

    let html = `
      <line x1="25" y1="${baseY}" x2="325" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
    `;

    sports.forEach((sp, i) => {
      const cx = startX + i * (clusterW + gap);
      if (isDouble) {
        const w = 26;
        const h1 = (boys[i] / maxVal) * 85;
        const h2 = (girls[i] / maxVal) * 85;
        // Boys Bar
        html += `
          <rect x="${cx}" y="${baseY - h1}" width="${w}" height="${h1}" fill="#3b82f6" rx="2" />
          <text x="${cx + w/2}" y="${baseY - h1 - 3}" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle font-family="monospace">${boys[i]}</text>
          <!-- Girls Bar -->
          <rect x="${cx + w + 3}" y="${baseY - h2}" width="${w}" height="${h2}" fill="#f59e0b" rx="2" />
          <text x="${cx + w + 3 + w/2}" y="${baseY - h2 - 3}" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle" font-family="monospace">${girls[i]}</text>
          <text x="${cx + w}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle">${sp}</text>
        `;
      } else {
        const w = 45;
        const total = boys[i] + girls[i];
        const h = (total / 120) * 85;
        html += `
          <rect x="${cx + 10}" y="${baseY - h}" width="${w}" height="${h}" fill="#8b5cf6" rx="2" />
          <text x="${cx + 10 + w/2}" y="${baseY - h - 3}" fill="#c4b5fd" font-size="8" font-weight="bold" text-anchor="middle" font-family="monospace">${total}</text>
          <text x="${cx + 10 + w/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle">${sp}</text>
        `;
      }
    });

    svg.innerHTML = html;
  }

  btnSingle.onclick = () => {
    isDouble = false;
    btnSingle.className = "px-2 py-0.5 rounded bg-purple-600 text-white font-bold text-[11px]";
    btnDouble.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    infoBox.innerHTML = `
      <div class="font-bold text-purple-300 mb-1">Single Bar Graph Active</div>
      <p class="text-slate-300 text-[11px]">Shows total combined players per sport. Cannot see how boys vs girls compare separately.</p>
    `;
    render();
  };

  btnDouble.onclick = () => {
    isDouble = true;
    btnDouble.className = "px-2 py-0.5 rounded bg-purple-600 text-white font-bold text-[11px]";
    btnSingle.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    infoBox.innerHTML = `
      <div class="font-bold text-purple-300 mb-1">Clustered Column Graph Active</div>
      <p class="text-slate-300 text-[11px]">Boys (Blue) and Girls (Amber) are paired side-by-side. Notice girls dominate Badminton while boys dominate Cricket!</p>
    `;
    render();
  };

  render();
}

// 12. Double Bar Graph Builder
function initDoubleBarBuilder() {
  const svg = document.getElementById('db-svg');
  const inM1 = document.getElementById('db-in-m1');
  const inM2 = document.getElementById('db-in-m2');
  const inS1 = document.getElementById('db-in-s1');
  const inS2 = document.getElementById('db-in-s2');
  const inE1 = document.getElementById('db-in-e1');
  const inE2 = document.getElementById('db-in-e2');
  const btnUpdate = document.getElementById('db-btn-update');

  if (!svg || !inM1) return;

  function render() {
    const subjects = ["Maths", "Science", "English"];
    const t1 = [parseInt(inM1.value) || 0, parseInt(inS1.value) || 0, parseInt(inE1.value) || 0];
    const t2 = [parseInt(inM2.value) || 0, parseInt(inS2.value) || 0, parseInt(inE2.value) || 0];
    const maxVal = 100;
    const startX = 40;
    const clusterW = 65;
    const gap = 30;
    const baseY = 115;

    let html = `
      <!-- Vertical Axis Line & Ticks -->
      <line x1="30" y1="15" x2="30" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
      <line x1="30" y1="${baseY}" x2="325" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
    `;

    for (let mark = 0; mark <= 100; mark += 25) {
      const y = baseY - (mark / maxVal) * 85;
      html += `
        <line x1="26" y1="${y}" x2="30" y2="${y}" stroke="#64748b" stroke-width="1" />
        <text x="22" y="${y + 3}" fill="#64748b" font-size="7.5" text-anchor="end" font-family="monospace">${mark}</text>
      `;
    }

    subjects.forEach((sub, i) => {
      const cx = startX + i * (clusterW + gap);
      const w = 26;
      const h1 = (t1[i] / maxVal) * 85;
      const h2 = (t2[i] / maxVal) * 85;

      html += `
        <!-- Term 1 Bar (Blue) -->
        <rect x="${cx}" y="${baseY - h1}" width="${w}" height="${h1}" fill="#3b82f6" rx="2" />
        <text x="${cx + w/2}" y="${baseY - h1 - 3}" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle" font-family="monospace">${t1[i]}</text>

        <!-- Term 2 Bar (Amber) -->
        <rect x="${cx + w + 3}" y="${baseY - h2}" width="${w}" height="${h2}" fill="#f59e0b" rx="2" />
        <text x="${cx + w + 3 + w/2}" y="${baseY - h2 - 3}" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle" font-family="monospace">${t2[i]}</text>

        <text x="${cx + w}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle font-weight="bold">${sub}</text>
      `;
    });

    svg.innerHTML = html;
  }

  btnUpdate.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    render();
  };

  render();
}

// 13. Multi-Step Data Extractor
function initMultistepExtractor() {
  const card = document.getElementById('me-result-card');
  const btnQ1 = document.getElementById('me-btn-q1');
  const btnQ2 = document.getElementById('me-btn-q2');
  const btnQ3 = document.getElementById('me-btn-q3');

  if (!card || !btnQ1) return;

  function setQuery(btnActive, qTitle, mathContent, ansText) {
    [btnQ1, btnQ2, btnQ3].forEach(b => {
      b.className = "p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] text-center";
    });
    btnActive.className = "p-2 rounded-lg bg-teal-600 text-white font-bold text-[11px] text-center";

    card.innerHTML = `
      <div class="font-bold text-teal-300">${qTitle}</div>
      <div class="text-slate-300 font-mono text-[11px] leading-relaxed">${mathContent}</div>
      <div class="p-2 bg-emerald-950/30 rounded border border-emerald-800/50 text-emerald-300 font-bold">
        ${ansText}
      </div>
    `;
    if (window.triggerMathRender) window.triggerMathRender(card);
  }

  btnQ1.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    setQuery(
      btnQ1,
      "Question: Which subject showed the largest numerical improvement?",
      "• Maths: $85 - 60 = \\mathbf{+25\\text{ marks}}$<br>• Science: $75 - 70 = +5\\text{ marks}$<br>• English: $70 - 80 = -10\\text{ marks}$",
      "🎉 Answer: Mathematics with a spectacular $+25$ mark surge!"
    );
  };

  btnQ2.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    setQuery(
      btnQ2,
      "Question: What was the combined total marks across all three subjects in Term 2?",
      "• Term 2 Maths: $85\\text{ marks}$<br>• Term 2 Science: $75\\text{ marks}$<br>• Term 2 English: $70\\text{ marks}$<br>$$\\text{Total} = 85 + 75 + 70 = \\mathbf{230\\text{ marks}}$$",
      "📊 Answer: Total Term 2 score is 230 out of 300 (76.7%)"
    );
  };

  btnQ3.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    setQuery(
      btnQ3,
      "Question: In which subject did performance decline from Term 1 to Term 2?",
      "• Maths: Improved ($+25$)<br>• Science: Improved ($+5$)<br>• English: Dropped from $80$ down to $70$ ($80 - 70 = 10\\text{ marks drop}$)",
      "⚠️ Answer: English is the only subject with negative growth (-10 marks)."
    );
  };
}

// 14. Child Growth Trends Over Decades
function initGrowthTrendsTracker() {
  const slider = document.getElementById('gt-year-slider');
  const yearVal = document.getElementById('gt-year-val');
  const heightVal = document.getElementById('gt-height-val');
  const diffVal = document.getElementById('gt-diff-val');
  const driverVal = document.getElementById('gt-driver-val');

  if (!slider) return;

  const data = {
    1920: { h: 135.0, driver: "Baseline Period: High childhood illness rates & limited dairy intake." },
    1940: { h: 137.5, driver: "Early Public Health: First municipal tap water systems and basic hygiene." },
    1960: { h: 141.0, driver: "Antibiotics Era: Mass vaccinations against polio, measles, and tuberculosis." },
    1980: { h: 144.2, driver: "Green Revolution: Caloric abundance, diversified protein and school lunches." },
    2000: { h: 147.5, driver: "Modern Nutrition: Micronutrient fortification (iron, iodine) and sanitation." },
    2025: { h: 150.0, driver: "Contemporary Frontier: Universal immunization and pediatric wellness tracking." }
  };

  function update() {
    const yr = parseInt(slider.value);
    yearVal.textContent = `Year ${yr}`;

    // Interpolate nearest
    const keys = [1920, 1940, 1960, 1980, 2000, 2025];
    let closest = 1920;
    for (let k of keys) {
      if (Math.abs(k - yr) < Math.abs(closest - yr)) closest = k;
    }

    const d = data[closest];
    heightVal.textContent = `${d.h.toFixed(1)} cm`;
    const diff = (d.h - 135.0).toFixed(1);
    diffVal.textContent = `+${diff} cm since 1920`;
    driverVal.textContent = d.driver;
  }

  slider.addEventListener('input', update);
  update();
}

// 15. Misleading Graph Buster
function initMisleadingGraphBuster() {
  const svg = document.getElementById('mg-svg');
  const btnTruncated = document.getElementById('mg-btn-truncated');
  const btnHonest = document.getElementById('mg-btn-honest');
  const expBox = document.getElementById('mg-explanation');

  if (!svg || !btnTruncated) return;

  let isTruncated = true;

  function render() {
    const aVal = 98.0;
    const bVal = 99.0;
    const baseY = 115;
    const startX = 70;
    const barW = 55;
    const gap = 60;

    let html = `
      <line x1="30" y1="${baseY}" x2="310" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
      <line x1="40" y1="15" x2="40" y2="${baseY}" stroke="#475569" stroke-width="1.5" />
    `;

    if (isTruncated) {
      // Scale from 95 to 100
      const minY = 95;
      const maxY = 100;
      const hA = ((aVal - minY) / (maxY - minY)) * 85;
      const hB = ((bVal - minY) / (maxY - minY)) * 85;

      html += `
        <!-- Truncation Kink symbol -->
        <text x="32" y="105" fill="#f43f5e" font-size="12" font-weight="bold">〰</text>
        <text x="35" y="${baseY + 12}" fill="#f43f5e" font-size="8" font-family="monospace">95%</text>
        <text x="35" y="25" fill="#64748b" font-size="8" font-family="monospace">100%</text>

        <!-- Brand A -->
        <rect x="${startX}" y="${baseY - hA}" width="${barW}" height="${hA}" fill="#3b82f6" rx="2" />
        <text x="${startX + barW/2}" y="${baseY - hA - 4}" fill="#93c5fd" font-size="9" font-weight="bold" text-anchor="middle font-family="monospace">98%</text>
        <text x="${startX + barW/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle">Brand A</text>

        <!-- Brand B -->
        <rect x="${startX + barW + gap}" y="${baseY - hB}" width="${barW}" height="${hB}" fill="#f43f5e" rx="2" />
        <text x="${startX + barW + gap + barW/2}" y="${baseY - hB - 4}" fill="#fda4af" font-size="9" font-weight="bold" text-anchor="middle font-family="monospace">99%</text>
        <text x="${startX + barW + gap + barW/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle font-weight="bold">Brand B</text>
      `;
    } else {
      // Honest scale: 0 to 100
      const hA = (aVal / 100) * 85;
      const hB = (bVal / 100) * 85;

      html += `
        <text x="35" y="${baseY + 12}" fill="#64748b" font-size="8" font-family="monospace">0%</text>
        <text x="35" y="25" fill="#64748b" font-size="8" font-family="monospace">100%</text>

        <!-- Brand A -->
        <rect x="${startX}" y="${baseY - hA}" width="${barW}" height="${hA}" fill="#3b82f6" rx="2" />
        <text x="${startX + barW/2}" y="${baseY - hA - 4}" fill="#93c5fd" font-size="9" font-weight="bold" text-anchor="middle font-family="monospace">98%</text>
        <text x="${startX + barW/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle">Brand A</text>

        <!-- Brand B -->
        <rect x="${startX + barW + gap}" y="${baseY - hB}" width="${barW}" height="${hB}" fill="#10b981" rx="2" />
        <text x="${startX + barW + gap + barW/2}" y="${baseY - hB - 4}" fill="#6ee7b7" font-size="9" font-weight="bold" text-anchor="middle font-family="monospace">99%</text>
        <text x="${startX + barW + gap + barW/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="9" text-anchor="middle font-weight="bold">Brand B</text>
      `;
    }

    svg.innerHTML = html;
  }

  btnTruncated.onclick = () => {
    isTruncated = true;
    btnTruncated.className = "px-2 py-0.5 rounded bg-rose-600 text-white font-bold text-[11px]";
    btnHonest.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    expBox.className = "p-2.5 bg-rose-950/30 border border-rose-800/50 rounded-xl text-xs text-rose-200";
    expBox.innerHTML = "<b>⚠️ Optical Deception Active:</b> Baseline starts at $95\\%$. The $99\\%$ bar appears TRIPLE the height of the $98\\%$ bar!";
    if (window.triggerMathRender) window.triggerMathRender(expBox);
    render();
  };

  btnHonest.onclick = () => {
    isTruncated = false;
    btnHonest.className = "px-2 py-0.5 rounded bg-emerald-600 text-white font-bold text-[11px]";
    btnTruncated.className = "px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]";
    expBox.className = "p-2.5 bg-emerald-950/30 border border-emerald-800/50 rounded-xl text-xs text-emerald-200";
    expBox.innerHTML = "<b>✓ Honest Representation:</b> Baseline starts at $0\\%$. Brand A ($98\\%$) and Brand B ($99\\%$) are visually revealed as virtually identical!";
    if (window.triggerMathRender) window.triggerMathRender(expBox);
    render();
  };

  render();
}

// 16. Data Detective Master Console
function initDataDetectiveHub() {
  const inputEl = document.getElementById('dd-input-data');
  const btnAnalyze = document.getElementById('dd-btn-analyze');
  const outMean = document.getElementById('dd-out-mean');
  const outMedian = document.getElementById('dd-out-median');
  const outRange = document.getElementById('dd-out-range');
  const outOutlier = document.getElementById('dd-out-outlier');
  const svg = document.getElementById('dd-svg');

  if (!inputEl || !btnAnalyze) return;

  function analyze() {
    const raw = inputEl.value;
    const nums = raw.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
    if (nums.length === 0) return;

    nums.sort((a, b) => a - b);
    const n = nums.length;

    // Mean
    const sum = nums.reduce((a, b) => a + b, 0);
    const mean = sum / n;
    outMean.textContent = mean.toFixed(1);

    // Median
    let median = 0;
    if (n % 2 === 1) {
      median = nums[Math.floor(n / 2)];
    } else {
      median = (nums[n / 2 - 1] + nums[n / 2]) / 2;
    }
    outMedian.textContent = median.toFixed(1);

    // Range
    const min = nums[0];
    const max = nums[n - 1];
    outRange.textContent = `${(max - min).toFixed(0)}`;

    // Outlier heuristic: > mean + 1.5 * range or isolated
    const q3 = nums[Math.floor(n * 0.75)];
    const q1 = nums[Math.floor(n * 0.25)];
    const iqr = q3 - q1;
    const potentialOutlier = nums.find(v => v > q3 + 1.5 * iqr || v < q1 - 1.5 * iqr);
    outOutlier.textContent = potentialOutlier !== undefined ? `${potentialOutlier}` : 'None';

    // Render mini dot plot
    const startX = 25;
    const endX = 315;
    const axisY = 65;

    function valToX(v) {
      return startX + ((v - min) / Math.max(1, (max - min))) * (endX - startX);
    }

    let html = `
      <line x1="15" y1="${axisY}" x2="325" y2="${axisY}" stroke="#475569" stroke-width="1.5" />
    `;

    const counts = {};
    nums.forEach(v => { counts[v] = (counts[v] || 0) + 1; });

    Object.keys(counts).forEach(vStr => {
      const v = parseFloat(vStr);
      const c = counts[vStr];
      const x = valToX(v);
      for (let s = 0; s < c; s++) {
        const cy = axisY - 6 - (s * 9);
        const isOutlier = (v === potentialOutlier);
        html += `
          <circle cx="${x}" cy="${cy}" r="3.5" fill="${isOutlier ? '#f43f5e' : '#38bdf8'}" stroke="${isOutlier ? '#e11d48' : '#0284c7'}" stroke-width="1" />
        `;
      }
    });

    svg.innerHTML = html;
  }

  btnAnalyze.onclick = () => {
    if (window.sfx && window.sfx.playClick) window.sfx.playClick();
    analyze();
  };

  analyze();
}
'''

# Write to .agents/class7_math_connecting_the_dots_js.py
output_path = ".agents/class7_math_connecting_the_dots_js.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Generated JavaScript for NCERT Class 7 Mathematics - Chapter 5: Connecting the Dots...\n\n")
    f.write(f"SIMULATORS_JS = {repr(JS_CONTENT)}\n")

print(f"Generated {output_path} successfully!")


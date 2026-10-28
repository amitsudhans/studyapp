js_content = r"""
// ==========================================
// 16 BESPOKE SIMULATOR INTERACTIVE ENGINES FOR FRACTIONS
// ==========================================

// Helper: Greatest Common Divisor
function gcd(a, b) {
  a = Math.abs(Math.round(a));
  b = Math.abs(Math.round(b));
  while (b) {
    const t = b;
    b = a % b;
    a = t;
  }
  return a || 1;
}

// ----------------------------------------------------
// 1. Fraction Anatomy Studio
// ----------------------------------------------------
let fvViewMode = 'pie';

function setFvView(mode) {
  fvViewMode = mode;
  const pieBtn = document.getElementById('fvPieBtn');
  const barBtn = document.getElementById('fvBarBtn');
  if (pieBtn && barBtn) {
    if (mode === 'pie') {
      pieBtn.className = 'flex-1 py-1 font-semibold rounded bg-amber-500/30 text-amber-200 border border-amber-500/50';
      barBtn.className = 'flex-1 py-1 font-semibold rounded bg-slate-800 text-slate-300 border border-slate-700';
    } else {
      barBtn.className = 'flex-1 py-1 font-semibold rounded bg-amber-500/30 text-amber-200 border border-amber-500/50';
      pieBtn.className = 'flex-1 py-1 font-semibold rounded bg-slate-800 text-slate-300 border border-slate-700';
    }
  }
  updateFractionVisualizer();
}

function updateFractionVisualizer() {
  const numSlider = document.getElementById('fvNumSlider');
  const denSlider = document.getElementById('fvDenSlider');
  if (!numSlider || !denSlider) return;

  const a = parseInt(numSlider.value) || 1;
  const b = parseInt(denSlider.value) || 1;

  const numVal = document.getElementById('fvNumVal');
  const denVal = document.getElementById('fvDenVal');
  const fracDisp = document.getElementById('fvFractionDisp');
  const decDisp = document.getElementById('fvDecimalDisp');
  const typeBadge = document.getElementById('fvTypeBadge');
  const narration = document.getElementById('fvNarration');
  const svg = document.getElementById('fvSvg');

  if (numVal) numVal.textContent = a;
  if (denVal) denVal.textContent = b;
  if (fracDisp) fracDisp.textContent = `${a} / ${b}`;
  if (decDisp) decDisp.textContent = (a / b).toFixed(2);

  if (typeBadge && narration) {
    if (a < b) {
      typeBadge.textContent = 'Proper Fraction (< 1)';
      typeBadge.className = 'px-2 py-0.5 text-xs font-bold rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
      narration.innerHTML = `Numerator <strong>${a}</strong> < Denominator <strong>${b}</strong>. Since you chose fewer parts than the whole unit, this is a <strong>Proper Fraction</strong> strictly less than 1.`;
    } else if (a === b) {
      typeBadge.textContent = 'Whole Unit (= 1)';
      typeBadge.className = 'px-2 py-0.5 text-xs font-bold rounded bg-blue-500/20 text-blue-300 border border-blue-500/40';
      narration.innerHTML = `Numerator <strong>${a}</strong> = Denominator <strong>${b}</strong>. All equal parts are chosen, representing exactly <strong>1 whole unit</strong>.`;
    } else {
      const whole = Math.floor(a / b);
      const rem = a % b;
      typeBadge.textContent = `Improper Fraction (> 1) = ${whole} ${rem}/${b}`;
      typeBadge.className = 'px-2 py-0.5 text-xs font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/40';
      narration.innerHTML = `Numerator <strong>${a}</strong> > Denominator <strong>${b}</strong>. This is an <strong>Improper Fraction</strong>, equivalent to the mixed number <strong>${whole} ${rem}/${b}</strong>.`;
    }
  }

  if (!svg) return;
  svg.innerHTML = '';

  if (fvViewMode === 'pie') {
    const cx = 120, cy = 100, r = 75;
    // If improper fraction, show how many full circles + remaining slice
    const totalCircles = Math.ceil(a / b);
    if (totalCircles === 1) {
      // Single circle
      for (let i = 0; i < b; i++) {
        const startAngle = (i / b) * 2 * Math.PI - Math.PI / 2;
        const endAngle = ((i + 1) / b) * 2 * Math.PI - Math.PI / 2;
        const x1 = cx + r * Math.cos(startAngle);
        const y1 = cy + r * Math.sin(startAngle);
        const x2 = cx + r * Math.cos(endAngle);
        const y2 = cy + r * Math.sin(endAngle);
        const largeArc = (endAngle - startAngle > Math.PI) ? 1 : 0;
        const pathData = (b === 1)
          ? `M ${cx - r} ${cy} A ${r} ${r} 0 1 0 ${cx + r} ${cy} A ${r} ${r} 0 1 0 ${cx - r} ${cy}`
          : `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`;

        const isFilled = i < a;
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', pathData);
        path.setAttribute('fill', isFilled ? '#f59e0b' : 'rgba(30, 41, 59, 0.7)');
        path.setAttribute('stroke', '#0f172a');
        path.setAttribute('stroke-width', '2');
        svg.appendChild(path);
      }
    } else {
      // Multiple mini pies
      const miniR = 38;
      let partsRemaining = a;
      const count = Math.min(totalCircles, 3);
      for (let c = 0; c < count; c++) {
        const miniCx = 50 + c * 70;
        const miniCy = 100;
        for (let i = 0; i < b; i++) {
          const startAngle = (i / b) * 2 * Math.PI - Math.PI / 2;
          const endAngle = ((i + 1) / b) * 2 * Math.PI - Math.PI / 2;
          const x1 = miniCx + miniR * Math.cos(startAngle);
          const y1 = miniCy + miniR * Math.sin(startAngle);
          const x2 = miniCx + miniR * Math.cos(endAngle);
          const y2 = miniCy + miniR * Math.sin(endAngle);
          const largeArc = (endAngle - startAngle > Math.PI) ? 1 : 0;
          const pathData = (b === 1)
            ? `M ${miniCx - miniR} ${miniCy} A ${miniR} ${miniR} 0 1 0 ${miniCx + miniR} ${miniCy} A ${miniR} ${miniR} 0 1 0 ${miniCx - miniR} ${miniCy}`
            : `M ${miniCx} ${miniCy} L ${x1} ${y1} A ${miniR} ${miniR} 0 ${largeArc} 1 ${x2} ${y2} Z`;

          const isFilled = partsRemaining > 0;
          if (isFilled) partsRemaining--;

          const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path.setAttribute('d', pathData);
          path.setAttribute('fill', isFilled ? '#f59e0b' : 'rgba(30, 41, 59, 0.7)');
          path.setAttribute('stroke', '#0f172a');
          path.setAttribute('stroke-width', '1.5');
          svg.appendChild(path);
        }
      }
    }
  } else {
    // Strip Bar mode
    const totalBars = Math.ceil(a / b);
    const count = Math.min(totalBars, 3);
    let partsRemaining = a;
    for (let c = 0; c < count; c++) {
      const barY = 30 + c * 55;
      const barW = 200, barH = 35;
      const stepW = barW / b;
      for (let i = 0; i < b; i++) {
        const isFilled = partsRemaining > 0;
        if (isFilled) partsRemaining--;
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', 20 + i * stepW);
        rect.setAttribute('y', barY);
        rect.setAttribute('width', stepW);
        rect.setAttribute('height', barH);
        rect.setAttribute('fill', isFilled ? '#06b6d4' : 'rgba(30, 41, 59, 0.7)');
        rect.setAttribute('stroke', '#0f172a');
        rect.setAttribute('stroke-width', '2');
        svg.appendChild(rect);
      }
    }
  }
}

// ----------------------------------------------------
// 2. Repeated Addition
// ----------------------------------------------------
let raA = 2, raB = 5;

function setRaFraction(a, b) {
  raA = a;
  raB = b;
  updateRepeatedAddition();
}

function updateRepeatedAddition() {
  const slider = document.getElementById('raNSlider');
  if (!slider) return;
  const n = parseInt(slider.value) || 3;
  const nVal = document.getElementById('raNVal');
  if (nVal) nVal.textContent = n;

  const sumExpr = document.getElementById('raSumExpr');
  const prodExpr = document.getElementById('raProductExpr');
  const tip = document.getElementById('raTip');

  const terms = Array(n).fill(`${raA}/${raB}`).join(' + ');
  const numTot = n * raA;
  const g = gcd(numTot, raB);
  const simpNum = numTot / g;
  const simpDen = raB / g;

  let mixedStr = '';
  if (numTot >= raB) {
    const w = Math.floor(numTot / raB);
    const r = numTot % raB;
    mixedStr = (r === 0) ? ` = ${w}` : ` = ${w} ${r}/${raB}`;
  }

  if (sumExpr) sumExpr.textContent = terms;
  if (prodExpr) prodExpr.textContent = `${n} × (${raA}/${raB}) = ${numTot}/${raB}${mixedStr}`;
  if (tip) tip.textContent = `Each jump spans ${raA}/${raB}. After ${n} jumps, the total distance covered is ${numTot}/${raB}.`;

  const svg = document.getElementById('raSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Draw number line from 0 to 4
  const maxUnits = Math.max(3, Math.ceil(numTot / raB) + 1);
  const startX = 30, endX = 490;
  const lineY = 120;
  const unitPx = (endX - startX) / maxUnits;

  // Axis line
  const axis = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  axis.setAttribute('x1', startX - 10);
  axis.setAttribute('y1', lineY);
  axis.setAttribute('x2', endX + 10);
  axis.setAttribute('y2', lineY);
  axis.setAttribute('stroke', '#64748b');
  axis.setAttribute('stroke-width', '2');
  svg.appendChild(axis);

  // Tick marks
  for (let u = 0; u <= maxUnits; u++) {
    const x = startX + u * unitPx;
    const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    tick.setAttribute('x1', x);
    tick.setAttribute('y1', lineY - 8);
    tick.setAttribute('x2', x);
    tick.setAttribute('y2', lineY + 8);
    tick.setAttribute('stroke', '#cbd5e1');
    tick.setAttribute('stroke-width', '2');
    svg.appendChild(tick);

    const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt.setAttribute('x', x);
    txt.setAttribute('y', lineY + 24);
    txt.setAttribute('text-anchor', 'middle');
    txt.setAttribute('fill', '#f8fafc');
    txt.setAttribute('font-size', '12');
    txt.setAttribute('font-weight', 'bold');
    txt.textContent = u;
    svg.appendChild(txt);

    // Subdivisions
    if (u < maxUnits) {
      for (let s = 1; s < raB; s++) {
        const sx = x + s * (unitPx / raB);
        const subTick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        subTick.setAttribute('x1', sx);
        subTick.setAttribute('y1', lineY - 4);
        subTick.setAttribute('x2', sx);
        subTick.setAttribute('y2', lineY + 4);
        subTick.setAttribute('stroke', '#475569');
        subTick.setAttribute('stroke-width', '1');
        svg.appendChild(subTick);
      }
    }
  }

  // Draw Jump Arcs
  const stepPx = (raA / raB) * unitPx;
  for (let j = 0; j < n; j++) {
    const jStartX = startX + j * stepPx;
    const jEndX = startX + (j + 1) * stepPx;
    const midX = (jStartX + jEndX) / 2;
    const arcH = Math.min(50, stepPx * 0.6);

    const arc = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    arc.setAttribute('d', `M ${jStartX} ${lineY} Q ${midX} ${lineY - arcH} ${jEndX} ${lineY}`);
    arc.setAttribute('fill', 'none');
    arc.setAttribute('stroke', '#f59e0b');
    arc.setAttribute('stroke-width', '2.5');
    svg.appendChild(arc);

    // Arrowhead
    const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    dot.setAttribute('cx', jEndX);
    dot.setAttribute('cy', lineY);
    dot.setAttribute('r', '4');
    dot.setAttribute('fill', '#10b981');
    svg.appendChild(dot);
  }
}

// ----------------------------------------------------
// 3. Fraction of a Fraction ("Of" Operator)
// ----------------------------------------------------
let fofBaseNum = 3, fofBaseDen = 4;
let fofPartNum = 1, fofPartDen = 2;

function setFofBase(n, d) {
  fofBaseNum = n;
  fofBaseDen = d;
  updateFractionOfFraction();
}

function setFofPortion(n, d) {
  fofPartNum = n;
  fofPartDen = d;
  updateFractionOfFraction();
}

function updateFractionOfFraction() {
  const res = document.getElementById('fofResult');
  const desc = document.getElementById('fofDesc');
  const prodNum = fofPartNum * fofBaseNum;
  const prodDen = fofPartDen * fofBaseDen;
  const g = gcd(prodNum, prodDen);

  if (res) {
    const simpStr = (g > 1) ? ` = ${prodNum / g}/${prodDen / g}` : '';
    res.textContent = `${fofPartNum}/${fofPartDen} of ${fofBaseNum}/${fofBaseDen} = ${prodNum}/${prodDen}${simpStr}`;
  }
  if (desc) {
    desc.innerHTML = `First slice horizontally into <strong>${fofBaseDen}</strong> bands and shade <strong>${fofBaseNum}</strong>. Then cut vertically into <strong>${fofPartDen}</strong> columns and keep <strong>${fofPartNum}</strong> of those bands. The overlapping cross-hatched cells equal exactly <strong>${prodNum}</strong> out of <strong>${prodDen}</strong>!`;
  }

  const svg = document.getElementById('fofSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const x0 = 30, y0 = 20, size = 160;
  const rowH = size / fofBaseDen;
  const colW = size / fofPartDen;

  // Draw background grid
  for (let r = 0; r < fofBaseDen; r++) {
    for (let c = 0; c < fofPartDen; c++) {
      const inBase = r < fofBaseNum;
      const inPart = c < fofPartNum;

      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', x0 + c * colW);
      rect.setAttribute('y', y0 + r * rowH);
      rect.setAttribute('width', colW);
      rect.setAttribute('height', rowH);
      rect.setAttribute('stroke', '#0f172a');
      rect.setAttribute('stroke-width', '1.5');

      if (inBase && inPart) {
        rect.setAttribute('fill', '#f59e0b'); // Overlap
      } else if (inBase) {
        rect.setAttribute('fill', 'rgba(6, 182, 212, 0.35)'); // Base fraction only
      } else {
        rect.setAttribute('fill', 'rgba(30, 41, 59, 0.7)');
      }
      svg.appendChild(rect);
    }
  }

  // Outer border
  const border = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  border.setAttribute('x', x0);
  border.setAttribute('y', y0);
  border.setAttribute('width', size);
  border.setAttribute('height', size);
  border.setAttribute('fill', 'none');
  border.setAttribute('stroke', '#f8fafc');
  border.setAttribute('stroke-width', '2');
  svg.appendChild(border);
}

// ----------------------------------------------------
// 4. Unit Square Grid Area Model
// ----------------------------------------------------
function updateUnitSquareGrid() {
  const aSlider = document.getElementById('usgASlider');
  const bSlider = document.getElementById('usgBSlider');
  const cSlider = document.getElementById('usgCSlider');
  const dSlider = document.getElementById('usgDSlider');
  if (!aSlider || !bSlider || !cSlider || !dSlider) return;

  let a = parseInt(aSlider.value) || 2;
  let b = parseInt(bSlider.value) || 3;
  let c = parseInt(cSlider.value) || 3;
  let d = parseInt(dSlider.value) || 5;

  if (a >= b) a = b - 1; // Keep proper fraction
  if (c >= d) c = d - 1;

  aSlider.max = b;
  cSlider.max = d;

  const lenTxt = document.getElementById('usgLenTxt');
  const brdTxt = document.getElementById('usgBrdTxt');
  const totalCellsEl = document.getElementById('usgTotalCells');
  const shadedCellsEl = document.getElementById('usgShadedCells');
  const formulaEl = document.getElementById('usgAreaFormula');

  if (lenTxt) lenTxt.textContent = `${a} / ${b}`;
  if (brdTxt) brdTxt.textContent = `${c} / ${d}`;

  const tot = b * d;
  const shaded = a * c;
  const g = gcd(shaded, tot);

  if (totalCellsEl) totalCellsEl.textContent = tot;
  if (shadedCellsEl) shadedCellsEl.textContent = shaded;
  if (formulaEl) {
    const simp = (g > 1) ? ` = ${shaded / g}/${tot / g}` : '';
    formulaEl.textContent = `Area = (${a} × ${c}) / (${b} × ${d}) = ${shaded}/${tot}${simp}`;
  }

  const svg = document.getElementById('usgSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const x0 = 35, y0 = 25, size = 160;
  const cellW = size / b;
  const cellH = size / d;

  for (let col = 0; col < b; col++) {
    for (let row = 0; row < d; row++) {
      const isShaded = col < a && row < c;
      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', x0 + col * cellW);
      rect.setAttribute('y', y0 + row * cellH);
      rect.setAttribute('width', cellW);
      rect.setAttribute('height', cellH);
      rect.setAttribute('fill', isShaded ? '#10b981' : 'rgba(30, 41, 59, 0.7)');
      rect.setAttribute('stroke', '#0f172a');
      rect.setAttribute('stroke-width', '1');
      svg.appendChild(rect);
    }
  }

  // Bounding box
  const outer = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  outer.setAttribute('x', x0);
  outer.setAttribute('y', y0);
  outer.setAttribute('width', size);
  outer.setAttribute('height', size);
  outer.setAttribute('fill', 'none');
  outer.setAttribute('stroke', '#38bdf8');
  outer.setAttribute('stroke-width', '2');
  svg.appendChild(outer);
}

// ----------------------------------------------------
// 5. Brahmagupta's Product Law Engine
// ----------------------------------------------------
function setBgPreset(a, b, c, d) {
  const n1 = document.getElementById('bgNum1');
  const d1 = document.getElementById('bgDen1');
  const n2 = document.getElementById('bgNum2');
  const d2 = document.getElementById('bgDen2');
  if (n1) n1.value = a;
  if (d1) d1.value = b;
  if (n2) n2.value = c;
  if (d2) d2.value = d;
  calcBrahmaguptaProduct();
}

function calcBrahmaguptaProduct() {
  const a = parseInt(document.getElementById('bgNum1')?.value) || 1;
  const b = parseInt(document.getElementById('bgDen1')?.value) || 1;
  const c = parseInt(document.getElementById('bgNum2')?.value) || 1;
  const d = parseInt(document.getElementById('bgDen2')?.value) || 1;

  const rawNum = a * c;
  const rawDen = b * d;
  const g = gcd(rawNum, rawDen);
  const sNum = rawNum / g;
  const sDen = rawDen / g;

  const prodNumEl = document.getElementById('bgProdNum');
  const prodDenEl = document.getElementById('bgProdDen');
  const simpNumEl = document.getElementById('bgSimpNum');
  const simpDenEl = document.getElementById('bgSimpDen');
  const expEl = document.getElementById('bgExplanation');

  if (prodNumEl) prodNumEl.textContent = rawNum;
  if (prodDenEl) prodDenEl.textContent = rawDen;
  if (simpNumEl) simpNumEl.textContent = sNum;
  if (simpDenEl) simpDenEl.textContent = sDen;
  if (expEl && window.triggerMathRender) setTimeout(() => triggerMathRender(expEl), 10);

  if (expEl) {
    if (g > 1) {
      expEl.innerHTML = `Brahmagupta's Rule: Numerators multiply ($${a} \\times ${c} = ${rawNum}$) and denominators multiply ($${b} \\times ${d} = ${rawDen}$). Reduced by common factor <strong>${g}</strong> to lowest terms: <strong>${sNum}/${sDen}</strong>.`;
    } else {
      expEl.innerHTML = `Brahmagupta's Rule: Numerators multiply ($${a} \\times ${c} = ${rawNum}$) and denominators multiply ($${b} \\times ${d} = ${rawDen}$). Already in irreducible lowest terms!`;
    }
  }
}

// ----------------------------------------------------
// 6. Cross-Cancelling Studio
// ----------------------------------------------------
let ccA1 = 3, ccB1 = 8, ccA2 = 4, ccB2 = 9;

function setCcProblem(a1, b1, a2, b2) {
  ccA1 = a1; ccB1 = b1; ccA2 = a2; ccB2 = b2;
  const elA1 = document.getElementById('ccA1');
  const elB1 = document.getElementById('ccB1');
  const elA2 = document.getElementById('ccA2');
  const elB2 = document.getElementById('ccB2');
  if (elA1) elA1.textContent = a1;
  if (elB1) elB1.textContent = b1;
  if (elA2) elA2.textContent = a2;
  if (elB2) elB2.textContent = b2;

  // Hide slashes
  ['ccSlashA1', 'ccSubA1', 'ccSlashB1', 'ccSubB1', 'ccSlashA2', 'ccSubA2', 'ccSlashB2', 'ccSubB2'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.add('hidden');
  });

  const rawNum = a1 * a2;
  const rawDen = b1 * b2;
  const g = gcd(rawNum, rawDen);
  const rNum = document.getElementById('ccResNum');
  const rDen = document.getElementById('ccResDen');
  if (rNum) rNum.textContent = rawNum / g;
  if (rDen) rDen.textContent = rawDen / g;

  const st = document.getElementById('ccStatusText');
  if (st) st.textContent = `Problem set: (${a1}/${b1}) × (${a2}/${b2}). Click "Slash Common Factors" to cross-cancel!`;
}

function animateCrossCancel() {
  const g1 = gcd(ccA1, ccB2); // Cross diagonal 1
  const g2 = gcd(ccA2, ccB1); // Cross diagonal 2

  if (g1 > 1) {
    const s1 = document.getElementById('ccSlashA1');
    const u1 = document.getElementById('ccSubA1');
    const s2 = document.getElementById('ccSlashB2');
    const u2 = document.getElementById('ccSubB2');
    if (s1) s1.classList.remove('hidden');
    if (u1) { u1.textContent = ccA1 / g1; u1.classList.remove('hidden'); }
    if (s2) s2.classList.remove('hidden');
    if (u2) { u2.textContent = ccB2 / g1; u2.classList.remove('hidden'); }
  }

  if (g2 > 1) {
    const s3 = document.getElementById('ccSlashA2');
    const u3 = document.getElementById('ccSubA2');
    const s4 = document.getElementById('ccSlashB1');
    const u4 = document.getElementById('ccSubB1');
    if (s3) s3.classList.remove('hidden');
    if (u3) { u3.textContent = ccA2 / g2; u3.classList.remove('hidden'); }
    if (s4) s4.classList.remove('hidden');
    if (u4) { u4.textContent = ccB1 / g2; u4.classList.remove('hidden'); }
  }

  const st = document.getElementById('ccStatusText');
  if (st) {
    st.innerHTML = `<span class='text-emerald-400 font-bold'>✓ Cross-cancelled!</span> Diagonal GCDs divided out before multiplying!`;
  }
}

// ----------------------------------------------------
// 7. Product Size Comparator
// ----------------------------------------------------
function setPscCase(caseType) {
  const badge = document.getElementById('pscCategoryBadge');
  const verdict = document.getElementById('pscVerdict');
  const svg = document.getElementById('pscSvg');
  if (!svg) return;
  svg.innerHTML = '';

  let f1 = 0.5, f2 = 0.75, prod = 0.375;
  let lbl1 = '1/2 (0.5)', lbl2 = '3/4 (0.75)', lblP = '3/8 (0.375)';

  if (caseType === 'proper_proper') {
    if (badge) {
      badge.textContent = 'Proper × Proper (< 1)';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/40';
    }
    if (verdict) verdict.textContent = '3/8 < 1/2 and 3/8 < 3/4. Multiplying two proper fractions produces a product smaller than both!';
  } else if (caseType === 'proper_improper') {
    f1 = 0.67; f2 = 2.5; prod = 1.67;
    lbl1 = '2/3 (0.67)'; lbl2 = '5/2 (2.50)'; lblP = '5/3 (1.67)';
    if (badge) {
      badge.textContent = 'Proper × Improper';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40';
    }
    if (verdict) verdict.textContent = '2/3 < 5/3 < 5/2. The product lies strictly between the proper fraction and improper fraction!';
  } else {
    f1 = 1.5; f2 = 1.33; prod = 2.0;
    lbl1 = '3/2 (1.50)'; lbl2 = '4/3 (1.33)'; lblP = '2/1 (2.00)';
    if (badge) {
      badge.textContent = 'Improper × Improper (> 1)';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
    }
    if (verdict) verdict.textContent = '2.0 > 1.5 and 2.0 > 1.33. Multiplying two improper fractions produces a product larger than both!';
  }

  // Draw 3 horizontal comparison bars
  const maxVal = Math.max(f1, f2, prod, 2.5);
  const barY1 = 40, barY2 = 85, barY3 = 130;
  const startX = 130, availW = 320;

  function drawBar(y, val, color, label, valLabel) {
    const w = (val / maxVal) * availW;
    const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt.setAttribute('x', '15');
    txt.setAttribute('y', y + 16);
    txt.setAttribute('fill', '#cbd5e1');
    txt.setAttribute('font-size', '11');
    txt.setAttribute('font-weight', 'bold');
    txt.textContent = label;
    svg.appendChild(txt);

    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    rect.setAttribute('x', startX);
    rect.setAttribute('y', y);
    rect.setAttribute('width', Math.max(10, w));
    rect.setAttribute('height', '22');
    rect.setAttribute('rx', '4');
    rect.setAttribute('fill', color);
    svg.appendChild(rect);

    const valTxt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    valTxt.setAttribute('x', startX + w + 8);
    valTxt.setAttribute('y', y + 16);
    valTxt.setAttribute('fill', color);
    valTxt.setAttribute('font-size', '12');
    valTxt.setAttribute('font-weight', 'bold');
    valTxt.setAttribute('font-family', 'monospace');
    valTxt.textContent = valLabel;
    svg.appendChild(valTxt);
  }

  drawBar(barY1, f1, '#38bdf8', 'Factor 1', lbl1);
  drawBar(barY2, f2, '#f59e0b', 'Factor 2', lbl2);
  drawBar(barY3, prod, '#10b981', 'Product P', lblP);
}

// ----------------------------------------------------
// 8. Commutativity Rotator
// ----------------------------------------------------
let crAngle = 0;

function rotateCommutativity() {
  crAngle = (crAngle + 90) % 360;
  const lbl = document.getElementById('crAngleLabel');
  const fTxt = document.getElementById('crFormulaText');
  if (lbl) lbl.textContent = `Rotation: ${crAngle}°`;
  if (fTxt) {
    if (crAngle === 90 || crAngle === 270) {
      fTxt.textContent = '(3/4) × (2/3) = 6/12 = 1/2';
    } else {
      fTxt.textContent = '(2/3) × (3/4) = 6/12 = 1/2';
    }
  }

  const svg = document.getElementById('crSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const cx = 230, cy = 100;
  const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  g.setAttribute('transform', `rotate(${crAngle} ${cx} ${cy})`);

  // Draw 3x4 grid centered at cx, cy
  const w = 150, h = 120;
  const x0 = cx - w / 2, y0 = cy - h / 2;
  const cols = 4, rows = 3;
  const cw = w / cols, rh = h / rows;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const isShaded = (r < 2 && c < 3); // 2 rows of 3 cols = 6 cells
      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', x0 + c * cw);
      rect.setAttribute('y', y0 + r * rh);
      rect.setAttribute('width', cw);
      rect.setAttribute('height', rh);
      rect.setAttribute('fill', isShaded ? '#f59e0b' : 'rgba(30, 41, 59, 0.7)');
      rect.setAttribute('stroke', '#0f172a');
      rect.setAttribute('stroke-width', '1.5');
      g.appendChild(rect);
    }
  }

  const outer = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  outer.setAttribute('x', x0);
  outer.setAttribute('y', y0);
  outer.setAttribute('width', w);
  outer.setAttribute('height', h);
  outer.setAttribute('fill', 'none');
  outer.setAttribute('stroke', '#38bdf8');
  outer.setAttribute('stroke-width', '2');
  g.appendChild(outer);

  svg.appendChild(g);
}

// ----------------------------------------------------
// 9. Reciprocal Multiplicative Inverse
// ----------------------------------------------------
function setReciprocalFraction(a, b) {
  const num = document.getElementById('rfNum');
  const den = document.getElementById('rfDen');
  const invNum = document.getElementById('rfInvNum');
  const invDen = document.getElementById('rfInvDen');
  const notice = document.getElementById('rfNotice');

  if (num) num.textContent = a;
  if (den) den.textContent = b;
  if (invNum) invNum.textContent = b;
  if (invDen) invDen.textContent = a;

  if (notice) {
    notice.innerHTML = `Original: <strong>${a}/${b}</strong> &rarr; Reciprocal (Multiplicative Inverse): <strong>${b}/${a}</strong>. Product: $(${a}/${b}) \\times (${b}/${a}) = \\frac{${a*b}}{${a*b}} = \\mathbf{1}$.`;
  }
}

function triggerZeroReciprocalWarning() {
  const notice = document.getElementById('rfNotice');
  if (notice) {
    notice.innerHTML = `<span class='text-rose-400 font-bold'>⚠️ Zero has no reciprocal!</span> Inverting $0 = \\frac{0}{1}$ gives $\\frac{1}{0}$, which is undefined in mathematics because division by zero is impossible!`;
  }
}

// ----------------------------------------------------
// 10. Fraction Division as Grouping
// ----------------------------------------------------
function setDgScenario(dividend, divisor, label) {
  const expl = document.getElementById('dgExplanation');
  const quotient = Math.round(dividend / divisor);
  if (expl) {
    expl.innerHTML = `<strong>${label} = ${quotient}</strong>. You can form exactly <strong>${quotient}</strong> portions of size ${divisor} from a total of ${dividend}!`;
  }

  const svg = document.getElementById('dgSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Draw cakes or blocks
  const cakes = Math.ceil(dividend);
  const r = 35;
  for (let c = 0; c < cakes; c++) {
    const cx = 80 + c * 100;
    const cy = 100;

    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', cx);
    circle.setAttribute('cy', cy);
    circle.setAttribute('r', r);
    circle.setAttribute('fill', 'rgba(245, 158, 11, 0.2)');
    circle.setAttribute('stroke', '#f59e0b');
    circle.setAttribute('stroke-width', '2');
    svg.appendChild(circle);

    // Slices
    const slices = Math.round(1 / divisor);
    for (let s = 0; s < slices; s++) {
      const ang = (s / slices) * 2 * Math.PI - Math.PI / 2;
      const x2 = cx + r * Math.cos(ang);
      const y2 = cy + r * Math.sin(ang);
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', cx);
      line.setAttribute('y1', cy);
      line.setAttribute('x2', x2);
      line.setAttribute('y2', y2);
      line.setAttribute('stroke', '#38bdf8');
      line.setAttribute('stroke-width', '2');
      svg.appendChild(line);
    }

    const cakeLbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    cakeLbl.setAttribute('x', cx);
    cakeLbl.setAttribute('y', cy + 55);
    cakeLbl.setAttribute('text-anchor', 'middle');
    cakeLbl.setAttribute('fill', '#94a3b8');
    cakeLbl.setAttribute('font-size', '11');
    cakeLbl.textContent = `Whole Unit ${c + 1}`;
    svg.appendChild(cakeLbl);
  }
}

// ----------------------------------------------------
// 11. Division Inverter Transformer
// ----------------------------------------------------
let diA = 5, diB = 6, diC = 2, diD = 3;
let diIsInverted = false;

function setDiProblem(a, b, c, d) {
  diA = a; diB = b; diC = c; diD = d;
  diIsInverted = false;

  const n1 = document.getElementById('diNum1');
  const d1 = document.getElementById('diDen1');
  const n2 = document.getElementById('diNum2');
  const d2 = document.getElementById('diDen2');
  const badge = document.getElementById('diOpBadge');
  const btn = document.getElementById('diActionBtn');
  const help = document.getElementById('diHelp');

  if (n1) n1.textContent = a;
  if (d1) d1.textContent = b;
  if (n2) n2.textContent = c;
  if (d2) d2.textContent = d;
  if (badge) {
    badge.textContent = '÷';
    badge.className = 'p-2 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/40 text-xl';
  }
  if (btn) btn.textContent = '↻ Step: Invert Divisor!';
  if (help) help.textContent = `Problem set: (${a}/${b}) ÷ (${c}/${d}). Click Invert Divisor to see the transformation!`;

  calcDiResult();
}

function toggleInvertStep() {
  diIsInverted = !diIsInverted;
  const n2 = document.getElementById('diNum2');
  const d2 = document.getElementById('diDen2');
  const badge = document.getElementById('diOpBadge');
  const btn = document.getElementById('diActionBtn');
  const help = document.getElementById('diHelp');

  if (diIsInverted) {
    if (n2) n2.textContent = diD;
    if (d2) d2.textContent = diC;
    if (badge) {
      badge.textContent = '×';
      badge.className = 'p-2 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/40 text-xl';
    }
    if (btn) btn.textContent = '↺ Reset to Division';
    if (help) help.innerHTML = `<span class='text-emerald-400 font-bold'>Brahmagupta's Law Applied:</span> Operation transformed to multiplication by multiplying the dividend by the reciprocal (${diD}/${diC})!`;
  } else {
    setDiProblem(diA, diB, diC, diD);
  }
}

function calcDiResult() {
  const prodNum = diA * diD;
  const prodDen = diB * diC;
  const g = gcd(prodNum, prodDen);
  const sNum = prodNum / g;
  const sDen = prodDen / g;

  const rNum = document.getElementById('diResNum');
  const rDen = document.getElementById('diResDen');
  const mixed = document.getElementById('diMixed');

  if (rNum) rNum.textContent = sNum;
  if (rDen) rDen.textContent = sDen;
  if (mixed) {
    if (sNum >= sDen && sDen > 1) {
      const w = Math.floor(sNum / sDen);
      const rem = sNum % sDen;
      mixed.textContent = (rem === 0) ? `= ${w}` : `= ${w} ${rem}/${sDen}`;
    } else {
      mixed.textContent = '';
    }
  }
}

// ----------------------------------------------------
// 12. Quotient Behavior Dial
// ----------------------------------------------------
function updateQuotientMagnifier() {
  const slider = document.getElementById('qmDivisorSlider');
  if (!slider) return;
  const val = parseInt(slider.value) || 5;
  const divisor = val / 10; // 0.1 to 3.0
  const dividend = 6;
  const quotient = dividend / divisor;

  const dText = document.getElementById('qmDivisorText');
  const calcText = document.getElementById('qmCalculation');
  const badge = document.getElementById('qmEffectBadge');
  const expl = document.getElementById('qmRuleExplanation');

  if (dText) dText.textContent = `${divisor.toFixed(1)}`;
  if (calcText) calcText.textContent = `6 ÷ ${divisor.toFixed(1)} = ${quotient.toFixed(2)}`;

  if (badge && expl) {
    if (divisor < 1.0) {
      badge.textContent = 'Quotient Expands! (> Dividend)';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} < 1</strong>, division magnifies the dividend: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} > 6$.`;
    } else if (divisor === 1.0) {
      badge.textContent = 'Quotient Unchanged (= Dividend)';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/40';
      expl.innerHTML = `Dividing by 1 leaves the dividend exactly unchanged: $6 \\div 1 = 6$.`;
    } else {
      badge.textContent = 'Quotient Shrinks! (< Dividend)';
      badge.className = 'text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40';
      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} > 1</strong>, division shrinks the value: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} < 6$.`;
    }
  }

  const svg = document.getElementById('qmSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Draw visual comparison bars
  const maxBar = 30; // max quotient possible
  const barW = (quotient / maxBar) * 320;

  // Dividend bar
  const divBarW = (dividend / maxBar) * 320;
  const divRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  divRect.setAttribute('x', '110');
  divRect.setAttribute('y', '50');
  divRect.setAttribute('width', divBarW);
  divRect.setAttribute('height', '24');
  divRect.setAttribute('rx', '4');
  divRect.setAttribute('fill', '#f59e0b');
  svg.appendChild(divRect);

  const divTxt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  divTxt.setAttribute('x', '15');
  divTxt.setAttribute('y', '67');
  divTxt.setAttribute('fill', '#f59e0b');
  divTxt.setAttribute('font-size', '12');
  divTxt.setAttribute('font-weight', 'bold');
  divTxt.textContent = 'Dividend (6)';
  svg.appendChild(divTxt);

  // Quotient bar
  const qColor = divisor < 1.0 ? '#10b981' : (divisor === 1.0 ? '#38bdf8' : '#f43f5e');
  const qRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  qRect.setAttribute('x', '110');
  qRect.setAttribute('y', '100');
  qRect.setAttribute('width', Math.min(360, Math.max(10, barW)));
  qRect.setAttribute('height', '24');
  qRect.setAttribute('rx', '4');
  qRect.setAttribute('fill', qColor);
  svg.appendChild(qRect);

  const qTxt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  qTxt.setAttribute('x', '15');
  qTxt.setAttribute('y', '117');
  qTxt.setAttribute('fill', qColor);
  qTxt.setAttribute('font-size', '12');
  qTxt.setAttribute('font-weight', 'bold');
  qTxt.textContent = `Quotient (${quotient.toFixed(1)})`;
  svg.appendChild(qTxt);
}

// ----------------------------------------------------
// 13. Practical Rates & Speed/Milk
// ----------------------------------------------------
let prMode = 'milk';

function setPrMode(mode) {
  prMode = mode;
  const mBtn = document.getElementById('prMilkBtn');
  const sBtn = document.getElementById('prSpeedBtn');
  if (mBtn && sBtn) {
    if (mode === 'milk') {
      mBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50';
      sBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
    } else {
      sBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50';
      mBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
    }
  }
  updatePrDisplay();
}

function updatePrDisplay() {
  const sumEl = document.getElementById('prResultSummary');
  const svg = document.getElementById('prSvg');
  if (!svg) return;
  svg.innerHTML = '';

  if (prMode === 'milk') {
    if (sumEl) sumEl.textContent = 'Milk: (3/4 L) ÷ (1/8 L per cup) = 6 cups filled';
    // Draw 1 jug and 6 cups
    const jug = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    jug.setAttribute('x', '40');
    jug.setAttribute('y', '40');
    jug.setAttribute('width', '70');
    jug.setAttribute('height', '110');
    jug.setAttribute('rx', '8');
    jug.setAttribute('fill', 'rgba(56, 189, 248, 0.2)');
    jug.setAttribute('stroke', '#38bdf8');
    jug.setAttribute('stroke-width', '2');
    svg.appendChild(jug);

    const jugFill = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    jugFill.setAttribute('x', '45');
    jugFill.setAttribute('y', '70');
    jugFill.setAttribute('width', '60');
    jugFill.setAttribute('height', '75');
    jugFill.setAttribute('fill', '#f8fafc');
    svg.appendChild(jugFill);

    const jugTxt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    jugTxt.setAttribute('x', '75');
    jugTxt.setAttribute('y', '170');
    jugTxt.setAttribute('text-anchor', 'middle');
    jugTxt.setAttribute('fill', '#38bdf8');
    jugTxt.setAttribute('font-size', '12');
    jugTxt.setAttribute('font-weight', 'bold');
    jugTxt.textContent = '3/4 L Milk';
    svg.appendChild(jugTxt);

    // 6 cups
    for (let i = 0; i < 6; i++) {
      const cx = 160 + (i % 3) * 80;
      const cy = (i < 3) ? 70 : 135;
      const cup = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      cup.setAttribute('x', cx);
      cup.setAttribute('y', cy);
      cup.setAttribute('width', '45');
      cup.setAttribute('height', '45');
      cup.setAttribute('rx', '4');
      cup.setAttribute('fill', '#f59e0b');
      cup.setAttribute('stroke', '#d97706');
      cup.setAttribute('stroke-width', '1.5');
      svg.appendChild(cup);

      const cupTxt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      cupTxt.setAttribute('x', cx + 22);
      cupTxt.setAttribute('y', cy + 27);
      cupTxt.setAttribute('text-anchor', 'middle');
      cupTxt.setAttribute('fill', '#0f172a');
      cupTxt.setAttribute('font-size', '11');
      cupTxt.setAttribute('font-weight', 'bold');
      cupTxt.textContent = '1/8 L';
      svg.appendChild(cupTxt);
    }
  } else {
    if (sumEl) sumEl.textContent = 'Speed: (15/2 km) ÷ (3/4 hr) = (15/2) × (4/3) = 10 km/hr';
    // Draw speed line
    const axis = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    axis.setAttribute('x1', '40');
    axis.setAttribute('y1', '100');
    axis.setAttribute('x2', '460');
    axis.setAttribute('y2', '100');
    axis.setAttribute('stroke', '#64748b');
    axis.setAttribute('stroke-width', '3');
    svg.appendChild(axis);

    const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt.setAttribute('x', '250');
    txt.setAttribute('y', '70');
    txt.setAttribute('text-anchor', 'middle');
    txt.setAttribute('fill', '#10b981');
    txt.setAttribute('font-size', '14');
    txt.setAttribute('font-weight', 'bold');
    txt.textContent = 'Distance = 7 1/2 km in 45 min (3/4 hr)';
    svg.appendChild(txt);

    const txt2 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt2.setAttribute('x', '250');
    txt2.setAttribute('y', '140');
    txt2.setAttribute('text-anchor', 'middle');
    txt2.setAttribute('fill', '#38bdf8');
    txt2.setAttribute('font-size', '13');
    txt2.setAttribute('font-weight', 'bold');
    txt2.textContent = 'Uniform Speed = 10 km/hr';
    svg.appendChild(txt2);
  }
}

// ----------------------------------------------------
// 14. Sulbasutra Bricklaying
// ----------------------------------------------------
function setSbBrick(type) {
  const bHalf = document.getElementById('sbBtnHalf');
  const bQuarter = document.getElementById('sbBtnQuarter');
  const bEighth = document.getElementById('sbBtnEighth');
  const countEl = document.getElementById('sbBrickCount');
  const formulaEl = document.getElementById('sbFormula');
  const svg = document.getElementById('sbSvg');
  if (!svg) return;
  svg.innerHTML = '';

  let brickCount = 4;
  let fractionStr = '1/4';
  let rows = 2, cols = 2;

  if (type === 'half') {
    brickCount = 2; fractionStr = '1/2'; rows = 2; cols = 1;
    if (bHalf) bHalf.className = 'flex-1 py-1 bg-amber-500/20 text-amber-300 rounded border border-amber-500/40';
    if (bQuarter) bQuarter.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
    if (bEighth) bEighth.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
  } else if (type === 'quarter') {
    brickCount = 4; fractionStr = '1/4'; rows = 2; cols = 2;
    if (bQuarter) bQuarter.className = 'flex-1 py-1 bg-amber-500/20 text-amber-300 rounded border border-amber-500/40';
    if (bHalf) bHalf.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
    if (bEighth) bEighth.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
  } else {
    brickCount = 8; fractionStr = '1/8'; rows = 4; cols = 2;
    if (bEighth) bEighth.className = 'flex-1 py-1 bg-amber-500/20 text-amber-300 rounded border border-amber-500/40';
    if (bHalf) bHalf.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
    if (bQuarter) bQuarter.className = 'flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
  }

  if (countEl) countEl.textContent = `${brickCount} Bricks`;
  if (formulaEl) formulaEl.textContent = `1 ÷ (${fractionStr}) = 1 × (${brickCount}/1) = ${brickCount} Bricks`;

  const x0 = 35, y0 = 25, size = 160;
  const rw = size / cols;
  const rh = size / rows;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', x0 + c * rw);
      rect.setAttribute('y', y0 + r * rh);
      rect.setAttribute('width', rw);
      rect.setAttribute('height', rh);
      rect.setAttribute('fill', ((r + c) % 2 === 0) ? '#d97706' : '#b45309');
      rect.setAttribute('stroke', '#1e293b');
      rect.setAttribute('stroke-width', '2');
      svg.appendChild(rect);
    }
  }
}

// ----------------------------------------------------
// 15. Cistern Fountain Filling Rates
// ----------------------------------------------------
let cfInterval = null;
let cfLevel = 0;

function toggleCisternFlow() {
  const btn = document.getElementById('cfFlowBtn');
  const st = document.getElementById('cfStatus');

  if (cfInterval) {
    clearInterval(cfInterval);
    cfInterval = null;
    if (btn) btn.textContent = '▶ Open All Fountains!';
    if (st) st.textContent = 'Status: Paused';
  } else {
    if (cfLevel >= 100) cfLevel = 0;
    if (btn) btn.textContent = '⏸ Pause Fountains';
    if (st) st.textContent = 'Status: Fountains Flowing!';

    cfInterval = setInterval(() => {
      cfLevel += 4;
      renderCisternLevel(cfLevel);
      if (cfLevel >= 100) {
        clearInterval(cfInterval);
        cfInterval = null;
        if (btn) btn.textContent = '↻ Refill Again';
        if (st) st.innerHTML = `<span class='text-emerald-400 font-bold'>✓ Cistern Filled in Exactly 1 Hour!</span>`;
      }
    }, 100);
  }
}

function renderCisternLevel(lvl) {
  const svg = document.getElementById('cfSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Tank outline
  const tank = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  tank.setAttribute('x', '100');
  tank.setAttribute('y', '60');
  tank.setAttribute('width', '300');
  tank.setAttribute('height', '120');
  tank.setAttribute('rx', '6');
  tank.setAttribute('fill', 'rgba(15, 23, 42, 0.8)');
  tank.setAttribute('stroke', '#38bdf8');
  tank.setAttribute('stroke-width', '2.5');
  svg.appendChild(tank);

  // Water level
  const maxH = 114;
  const currentH = (lvl / 100) * maxH;
  if (currentH > 0) {
    const water = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    water.setAttribute('x', '103');
    water.setAttribute('y', 60 + (maxH - currentH) + 3);
    water.setAttribute('width', '294');
    water.setAttribute('height', currentH);
    water.setAttribute('fill', '#0284c7');
    water.setAttribute('opacity', '0.75');
    svg.appendChild(water);
  }

  // 3 Fountain Pipes above
  [150, 250, 350].forEach((pipeX, idx) => {
    const pipe = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    pipe.setAttribute('x1', pipeX);
    pipe.setAttribute('y1', '20');
    pipe.setAttribute('x2', pipeX);
    pipe.setAttribute('y2', '60');
    pipe.setAttribute('stroke', '#f59e0b');
    pipe.setAttribute('stroke-width', '6');
    svg.appendChild(pipe);

    // Stream
    if (cfInterval && lvl < 100) {
      const stream = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      stream.setAttribute('x1', pipeX);
      stream.setAttribute('y1', '60');
      stream.setAttribute('x2', pipeX);
      stream.setAttribute('y2', '170');
      stream.setAttribute('stroke', '#38bdf8');
      stream.setAttribute('stroke-width', '3');
      stream.setAttribute('stroke-dasharray', '4 4');
      svg.appendChild(stream);
    }
  });
}

// ----------------------------------------------------
// 16. Lilavati Donation Riddle
// ----------------------------------------------------
function updateLilavatiRiddle() {
  const inp = document.getElementById('lvFinalInput');
  const fCoins = document.getElementById('lvFinalCoins');
  if (inp && fCoins) {
    const val = parseInt(inp.value) || 20;
    fCoins.textContent = `${val} Coins`;
  }
}

function revealLilavatiSolution() {
  const inp = document.getElementById('lvFinalInput');
  const val = parseInt(inp?.value) || 20;
  const init = val * 3;

  const initCoins = document.getElementById('lvInitCoins');
  const rem1 = document.getElementById('lvRem1');
  const rem2 = document.getElementById('lvRem2');
  const box = document.getElementById('lvDeductionBox');

  if (initCoins) initCoins.textContent = `${init} Coins`;
  if (rem1) rem1.textContent = `${init / 2} Coins (1/2)`;
  if (rem2) rem2.textContent = `${val} Coins (1/3 of init)`;

  if (box) {
    box.innerHTML = `<span class='text-amber-400 font-bold'>Bhāskara II's Viparīta-vidhi (Method of Inversion):</span><br>
    Final remainder = $20$ coins, which represents $1 - \\frac{1}{2} - \\frac{1}{6} = \\frac{1}{3}$ of the original wealth $x$.<br>
    Therefore: $x \\times \\frac{1}{3} = 20 \\implies x = 20 \\div \\frac{1}{3} = 20 \\times 3 = \\mathbf{${init}\\text{ coins}}$!`;
  }
}

// ----------------------------------------------------
// MASTER SIMULATOR INITIALIZER ON SLIDE CHANGE
// ----------------------------------------------------
function initSimulators(slideIndex) {
  switch (slideIndex) {
    case 0: // Slide 1
      updateFractionVisualizer();
      break;
    case 1: // Slide 2
      updateRepeatedAddition();
      break;
    case 2: // Slide 3
      updateFractionOfFraction();
      break;
    case 3: // Slide 4
      updateUnitSquareGrid();
      break;
    case 4: // Slide 5
      calcBrahmaguptaProduct();
      break;
    case 5: // Slide 6
      setCcProblem(3, 8, 4, 9);
      break;
    case 6: // Slide 7
      setPscCase('proper_proper');
      break;
    case 7: // Slide 8
      rotateCommutativity();
      break;
    case 8: // Slide 9
      setReciprocalFraction(3, 7);
      break;
    case 9: // Slide 10
      setDgScenario(2, 0.5, '2 ÷ (1/2)');
      break;
    case 10: // Slide 11
      setDiProblem(5, 6, 2, 3);
      break;
    case 11: // Slide 12
      updateQuotientMagnifier();
      break;
    case 12: // Slide 13
      updatePrDisplay();
      break;
    case 13: // Slide 14
      setSbBrick('quarter');
      break;
    case 14: // Slide 15
      renderCisternLevel(0);
      break;
    case 15: // Slide 16
      updateLilavatiRiddle();
      break;
  }
}
"""

with open('.agents/class7_math_working_with_fractions_js.py', 'w') as f:
    f.write(f"SIMULATORS_JS = {repr(js_content)}\n")

print("Created .agents/class7_math_working_with_fractions_js.py successfully!")


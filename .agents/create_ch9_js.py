# -*- coding: utf-8 -*-
"""
Generator for NCERT Class 7 Mathematics - Chapter 9: Geometric Twins (Congruence) JS Interactive Engines
Generates .agents/class7_math_geometric_twins_js.py with 16 bespoke simulator engines.
"""

js_content = r"""
// ==========================================
// 16 BESPOKE SIMULATOR INTERACTIVE ENGINES FOR CONGRUENCE
// ==========================================

// Helper: Degree to Radian
function degToRad(deg) {
  return (deg * Math.PI) / 180;
}

// ----------------------------------------------------
// 1. Superposition & Rigid Motion Studio
// ----------------------------------------------------
let supShiftX = 0;
let supRotation = 0;

function updateSuperposition() {
  const xSlider = document.getElementById('supXSlider');
  const rSlider = document.getElementById('supRotSlider');
  const xVal = document.getElementById('supXVal');
  const rVal = document.getElementById('supRotVal');
  const badge = document.getElementById('supStatusBadge');
  const expl = document.getElementById('supExplanation');

  if (xSlider) supShiftX = parseFloat(xSlider.value) || 0;
  if (rSlider) supRotation = parseFloat(rSlider.value) || 0;

  if (xVal) xVal.textContent = `${Math.round(supShiftX)} px`;
  if (rVal) rVal.textContent = `${Math.round(supRotation)}°`;

  const isAligned = Math.abs(supShiftX - 200) < 6 && (Math.abs(supRotation - 360) < 6 || Math.abs(supRotation) < 6);

  if (badge) {
    if (isAligned) {
      badge.textContent = '✓ Perfectly Superimposed! (T1 ≅ T2)';
      badge.className = 'px-2 py-0.5 text-xs font-bold rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
      if (expl) expl.innerHTML = `<span class='text-emerald-400 font-bold'>Congruence Verified!</span> Triangle A covers Triangle B with zero gap and zero overlap!`;
    } else {
      badge.textContent = 'Not Superimposed';
      badge.className = 'px-2 py-0.5 text-xs font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/40';
      if (expl) expl.textContent = 'Slide horizontal shift to 200 px to superimpose Triangle A over Triangle B!';
    }
  }

  const svg = document.getElementById('supSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Base Target Triangle (T2) at right
  const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly2.setAttribute('points', '350,160 450,160 400,60');
  poly2.setAttribute('fill', 'rgba(16, 185, 129, 0.15)');
  poly2.setAttribute('stroke', '#10b981');
  poly2.setAttribute('stroke-width', '2.5');
  poly2.setAttribute('stroke-dasharray', '4 4');
  svg.appendChild(poly2);

  const t2Lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  t2Lbl.setAttribute('x', '400');
  t2Lbl.setAttribute('y', '140');
  t2Lbl.setAttribute('text-anchor', 'middle');
  t2Lbl.setAttribute('fill', '#10b981');
  t2Lbl.setAttribute('font-size', '12');
  t2Lbl.setAttribute('font-weight', 'bold');
  t2Lbl.textContent = 'Target (T2)';
  svg.appendChild(t2Lbl);

  // Moving Triangle (T1) starting at left (150,160 250,160 200,60)
  const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  const cx = 200 + supShiftX;
  const cy = 126;
  g.setAttribute('transform', `translate(${supShiftX}, 0) rotate(${supRotation} 200 126)`);

  const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly1.setAttribute('points', '150,160 250,160 200,60');
  poly1.setAttribute('fill', isAligned ? 'rgba(56, 189, 248, 0.4)' : 'rgba(245, 158, 11, 0.3)');
  poly1.setAttribute('stroke', isAligned ? '#38bdf8' : '#f59e0b');
  poly1.setAttribute('stroke-width', '2.5');
  g.appendChild(poly1);

  const t1Lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  t1Lbl.setAttribute('x', '200');
  t1Lbl.setAttribute('y', '140');
  t1Lbl.setAttribute('text-anchor', 'middle');
  t1Lbl.setAttribute('fill', '#f59e0b');
  t1Lbl.setAttribute('font-size', '12');
  t1Lbl.setAttribute('font-weight', 'bold');
  t1Lbl.textContent = 'Movable (T1)';
  g.appendChild(t1Lbl);

  svg.appendChild(g);
}

function snapSuperposition() {
  const xSlider = document.getElementById('supXSlider');
  const rSlider = document.getElementById('supRotSlider');
  if (xSlider) xSlider.value = 200;
  if (rSlider) rSlider.value = 0;
  updateSuperposition();
}

function resetSuperposition() {
  const xSlider = document.getElementById('supXSlider');
  const rSlider = document.getElementById('supRotSlider');
  if (xSlider) xSlider.value = 0;
  if (rSlider) rSlider.value = 0;
  updateSuperposition();
}

// ----------------------------------------------------
// 2. Simple Figures Congruence
// ----------------------------------------------------
let sfMode = 'lines';
let sfParam = 120; // Length / Radius / Angle

function setSimpleFigureMode(mode) {
  sfMode = mode;
  ['lines', 'angles', 'circles', 'rects'].forEach(m => {
    const btn = document.getElementById(`sf${m.charAt(0).toUpperCase() + m.slice(1)}Btn`);
    if (btn) {
      if (m === mode) {
        btn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50';
      } else {
        btn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
      }
    }
  });

  const controls = document.getElementById('sfControls');
  if (!controls) return;

  if (mode === 'lines') {
    controls.innerHTML = `
      <span class="text-slate-400">Length Segment 2:</span>
      <input type="range" min="80" max="160" value="120" oninput="updateSimpleFigures(this.value)" class="w-32 accent-cyan-400">
      <span id="sfValText" class="text-cyan-300 font-bold font-mono">120 px</span>
    `;
  } else if (mode === 'angles') {
    controls.innerHTML = `
      <span class="text-slate-400">Angle 2 Measure:</span>
      <input type="range" min="30" max="120" value="60" oninput="updateSimpleFigures(this.value)" class="w-32 accent-amber-400">
      <span id="sfValText" class="text-amber-300 font-bold font-mono">60°</span>
    `;
  } else if (mode === 'circles') {
    controls.innerHTML = `
      <span class="text-slate-400">Radius Circle 2:</span>
      <input type="range" min="30" max="65" value="45" oninput="updateSimpleFigures(this.value)" class="w-32 accent-emerald-400">
      <span id="sfValText" class="text-emerald-300 font-bold font-mono">45 px</span>
    `;
  } else {
    controls.innerHTML = `
      <span class="text-slate-400">Width Rect 2:</span>
      <input type="range" min="80" max="140" value="100" oninput="updateSimpleFigures(this.value)" class="w-32 accent-purple-400">
      <span id="sfValText" class="text-purple-300 font-bold font-mono">100 px</span>
    `;
  }

  updateSimpleFigures(sfMode === 'angles' ? 60 : (sfMode === 'circles' ? 45 : (sfMode === 'rects' ? 100 : 120)));
}

function updateSimpleFigures(val) {
  const v = parseFloat(val);
  const valText = document.getElementById('sfValText');
  const verdict = document.getElementById('sfVerdict');
  const svg = document.getElementById('sfSvg');
  if (!svg) return;
  svg.innerHTML = '';

  if (sfMode === 'lines') {
    if (valText) valText.textContent = `${Math.round(v)} px`;
    const isCongruent = Math.abs(v - 120) < 2;
    if (verdict) {
      verdict.textContent = isCongruent ? '✓ Equal Lengths (120 px): AB ≅ CD!' : `Lengths differ (120 px vs ${Math.round(v)} px): Not Congruent`;
      verdict.className = isCongruent ? 'font-mono text-emerald-300 font-bold' : 'font-mono text-rose-400 font-bold';
    }

    // Line 1: fixed 120
    const l1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    l1.setAttribute('x1', '60'); l1.setAttribute('y1', '90');
    l1.setAttribute('x2', '180'); l1.setAttribute('y2', '90');
    l1.setAttribute('stroke', '#38bdf8'); l1.setAttribute('stroke-width', '4');
    svg.appendChild(l1);

    // Line 2: dynamic
    const l2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    l2.setAttribute('x1', '300'); l2.setAttribute('y1', '90');
    l2.setAttribute('x2', `${300 + v}`); l2.setAttribute('y2', '90');
    l2.setAttribute('stroke', isCongruent ? '#10b981' : '#f59e0b');
    l2.setAttribute('stroke-width', '4');
    svg.appendChild(l2);

  } else if (sfMode === 'angles') {
    if (valText) valText.textContent = `${Math.round(v)}°`;
    const isCongruent = Math.abs(v - 60) < 2;
    if (verdict) {
      verdict.textContent = isCongruent ? '✓ Equal Measures (60°): ∠ABC ≅ ∠DEF!' : `Measures differ (60° vs ${Math.round(v)}°): Not Congruent`;
      verdict.className = isCongruent ? 'font-mono text-emerald-300 font-bold' : 'font-mono text-rose-400 font-bold';
    }

    // Draw fixed 60° angle at (140, 130)
    // Draw dynamic angle v at (360, 130)
    const rad = degToRad(v);
    const ax2 = 360 + 80 * Math.cos(rad);
    const ay2 = 130 - 80 * Math.sin(rad);

    const path1 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path1.setAttribute('d', 'M 220 130 L 140 130 L 180 61');
    path1.setAttribute('fill', 'none'); path1.setAttribute('stroke', '#38bdf8'); path1.setAttribute('stroke-width', '3');
    svg.appendChild(path1);

    const path2 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path2.setAttribute('d', `M 440 130 L 360 130 L ${ax2} ${ay2}`);
    path2.setAttribute('fill', 'none'); path2.setAttribute('stroke', isCongruent ? '#10b981' : '#f59e0b'); path2.setAttribute('stroke-width', '3');
    svg.appendChild(path2);

  } else if (sfMode === 'circles') {
    if (valText) valText.textContent = `r = ${Math.round(v)} px`;
    const isCongruent = Math.abs(v - 45) < 2;
    if (verdict) {
      verdict.textContent = isCongruent ? '✓ Equal Radii (r = 45): Circle 1 ≅ Circle 2!' : `Radii differ (r=45 vs r=${Math.round(v)}): Not Congruent`;
      verdict.className = isCongruent ? 'font-mono text-emerald-300 font-bold' : 'font-mono text-rose-400 font-bold';
    }

    const c1 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    c1.setAttribute('cx', '140'); c1.setAttribute('cy', '90'); c1.setAttribute('r', '45');
    c1.setAttribute('fill', 'rgba(56, 189, 248, 0.2)'); c1.setAttribute('stroke', '#38bdf8'); c1.setAttribute('stroke-width', '2.5');
    svg.appendChild(c1);

    const c2 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    c2.setAttribute('cx', '360'); c2.setAttribute('cy', '90'); c2.setAttribute('r', `${v}`);
    c2.setAttribute('fill', isCongruent ? 'rgba(16, 185, 129, 0.2)' : 'rgba(245, 158, 11, 0.2)');
    c2.setAttribute('stroke', isCongruent ? '#10b981' : '#f59e0b'); c2.setAttribute('stroke-width', '2.5');
    svg.appendChild(c2);
  }
}

// ----------------------------------------------------
// 3. Triangle Vertex Correspondence Studio
// ----------------------------------------------------
function highlightCorrespondence(vtx) {
  const details = document.getElementById('tcDetails');
  if (details) {
    if (vtx === 'A') {
      details.innerHTML = `<span class='text-amber-400 font-bold'>Vertex A &harr; P:</span> Angle &ang;A = &ang;P. Opposite sides: <strong>BC = QR</strong> (Red alignment).`;
    } else if (vtx === 'B') {
      details.innerHTML = `<span class='text-cyan-400 font-bold'>Vertex B &harr; Q:</span> Angle &ang;B = &ang;Q. Opposite sides: <strong>AC = PR</strong> (Cyan alignment).`;
    } else {
      details.innerHTML = `<span class='text-emerald-400 font-bold'>Vertex C &harr; R:</span> Angle &ang;C = &ang;R. Opposite sides: <strong>AB = PQ</strong> (Green alignment).`;
    }
    if (window.triggerMathRender) setTimeout(() => triggerMathRender(details), 10);
  }
  renderTriangleCorrespondence(vtx);
}

function renderTriangleCorrespondence(activeVtx) {
  const svg = document.getElementById('tcSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Triangle 1: ABC (80,160 220,160 140,50)
  // Triangle 2: PQR (300,160 440,160 360,50)
  const drawTri = (ox, pLbl, qLbl, rLbl) => {
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${ox},160 ${ox+140},160 ${ox+60},50`);
    poly.setAttribute('fill', 'rgba(15, 23, 42, 0.7)');
    poly.setAttribute('stroke', '#475569');
    poly.setAttribute('stroke-width', '2');
    svg.appendChild(poly);

    // Vertices dots
    const makeDot = (cx, cy, col, lbl, lx, ly) => {
      const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      dot.setAttribute('cx', cx); dot.setAttribute('cy', cy); dot.setAttribute('r', '7');
      dot.setAttribute('fill', col); dot.setAttribute('stroke', '#fff'); dot.setAttribute('stroke-width', '1.5');
      svg.appendChild(dot);

      const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      txt.setAttribute('x', lx); txt.setAttribute('y', ly);
      txt.setAttribute('fill', col); txt.setAttribute('font-size', '13'); txt.setAttribute('font-weight', 'bold');
      txt.textContent = lbl;
      svg.appendChild(txt);
    };

    makeDot(ox+60, 50, (activeVtx === 'A') ? '#f59e0b' : '#94a3b8', pLbl, ox+55, 38);
    makeDot(ox, 160, (activeVtx === 'B') ? '#06b6d4' : '#94a3b8', qLbl, ox-16, 175);
    makeDot(ox+140, 160, (activeVtx === 'C') ? '#10b981' : '#94a3b8', rLbl, ox+146, 175);
  };

  drawTri(80, 'A', 'B', 'C');
  drawTri(300, 'P', 'Q', 'R');
}

// ----------------------------------------------------
// 4. SSS Congruence Lab
// ----------------------------------------------------
function updateSSS() {
  const sA = document.getElementById('sssASlider')?.value || 8;
  const sB = document.getElementById('sssBSlider')?.value || 7;
  const sC = document.getElementById('sssCSlider')?.value || 6;

  const aVal = document.getElementById('sssAVal');
  const bVal = document.getElementById('sssBVal');
  const cVal = document.getElementById('sssCVal');
  const verdict = document.getElementById('sssVerdict');

  if (aVal) aVal.textContent = `${sA} cm`;
  if (bVal) bVal.textContent = `${sB} cm`;
  if (cVal) cVal.textContent = `${sC} cm`;

  if (verdict) {
    verdict.textContent = `All 3 side lengths match: a=${sA} cm, b=${sB} cm, c=${sC} cm. Therefore, △ABC ≅ △DEF by SSS!`;
  }

  const svg = document.getElementById('sssSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Draw 2 identical triangles side by side
  [70, 290].forEach((ox, idx) => {
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${ox},140 ${ox + sA * 14},140 ${ox + 40},50`);
    poly.setAttribute('fill', 'rgba(245, 158, 11, 0.2)');
    poly.setAttribute('stroke', '#f59e0b');
    poly.setAttribute('stroke-width', '2.5');
    svg.appendChild(poly);

    const lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    lbl.setAttribute('x', ox + 40); lbl.setAttribute('y', 110);
    lbl.setAttribute('fill', '#fde68a'); lbl.setAttribute('font-size', '12'); lbl.setAttribute('font-weight', 'bold');
    lbl.textContent = (idx === 0) ? '△ABC' : '△DEF';
    svg.appendChild(lbl);
  });
}

// ----------------------------------------------------
// 5. SAS Congruence Lab
// ----------------------------------------------------
function updateSAS() {
  const s1 = parseFloat(document.getElementById('sasS1Slider')?.value) || 6;
  const ang = parseFloat(document.getElementById('sasAngSlider')?.value) || 55;
  const s2 = parseFloat(document.getElementById('sasS2Slider')?.value) || 8;

  const s1Val = document.getElementById('sasS1Val');
  const angVal = document.getElementById('sasAngVal');
  const s2Val = document.getElementById('sasS2Val');
  const verdict = document.getElementById('sasVerdict');

  if (s1Val) s1Val.textContent = `${s1} cm`;
  if (angVal) angVal.textContent = `${Math.round(ang)}°`;
  if (s2Val) s2Val.textContent = `${s2} cm`;

  if (verdict) {
    verdict.textContent = `Sides ${s1} cm and ${s2} cm with included angle ${Math.round(ang)}° lock the triangle: △ABC ≅ △PQR by SAS!`;
  }

  const svg = document.getElementById('sasSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const rad = degToRad(ang);
  [80, 290].forEach((ox, idx) => {
    const p1x = ox, p1y = 140;
    const p2x = ox + s2 * 14, p2y = 140;
    const p3x = ox + s1 * 14 * Math.cos(rad);
    const p3y = 140 - s1 * 14 * Math.sin(rad);

    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${p1x},${p1y} ${p2x},${p2y} ${p3x},${p3y}`);
    poly.setAttribute('fill', 'rgba(6, 182, 212, 0.2)');
    poly.setAttribute('stroke', '#06b6d4');
    poly.setAttribute('stroke-width', '2.5');
    svg.appendChild(poly);

    // Angle Arc at vertex p1
    const arc = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    const arcX = p1x + 24 * Math.cos(rad);
    const arcY = p1y - 24 * Math.sin(rad);
    arc.setAttribute('d', `M ${p1x + 24} ${p1y} A 24 24 0 0 0 ${arcX} ${arcY}`);
    arc.setAttribute('fill', 'none');
    arc.setAttribute('stroke', '#f43f5e');
    arc.setAttribute('stroke-width', '2');
    svg.appendChild(arc);
  });
}

// ----------------------------------------------------
// 6. Included Angle Trap
// ----------------------------------------------------
let trapMode = 'included';

function setTrapMode(mode) {
  trapMode = mode;
  const incBtn = document.getElementById('trapIncBtn');
  const nonBtn = document.getElementById('trapNonBtn');
  const expl = document.getElementById('trapExplanation');

  if (incBtn && nonBtn) {
    if (mode === 'included') {
      incBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/30 text-emerald-300 border border-emerald-500/50';
      nonBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
      if (expl) expl.textContent = 'In SAS, the angle is firmly sandwiched between the two arms, fixing the closing side uniquely!';
    } else {
      nonBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-rose-500/30 text-rose-300 border border-rose-500/50';
      incBtn.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
      if (expl) expl.textContent = 'In SSA, the non-included side can swing like a clock pendulum, hitting the base in two places!';
    }
  }

  const svg = document.getElementById('trapSvg');
  if (!svg) return;
  svg.innerHTML = '';

  if (mode === 'included') {
    // Unique clamped triangle
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', '180,160 320,160 240,60');
    poly.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
    poly.setAttribute('stroke', '#10b981');
    poly.setAttribute('stroke-width', '3');
    svg.appendChild(poly);

    const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt.setAttribute('x', '250'); txt.setAttribute('y', '120');
    txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('fill', '#10b981'); txt.setAttribute('font-weight', 'bold');
    txt.textContent = '1 Unique Triangle (SAS Clamped)';
    svg.appendChild(txt);
  } else {
    // Two swinging triangles
    const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly1.setAttribute('points', '120,160 360,160 220,60');
    poly1.setAttribute('fill', 'rgba(244, 63, 94, 0.15)');
    poly1.setAttribute('stroke', '#f43f5e');
    poly1.setAttribute('stroke-width', '2');
    svg.appendChild(poly1);

    const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly2.setAttribute('points', '120,160 260,160 220,60');
    poly2.setAttribute('fill', 'rgba(245, 158, 11, 0.25)');
    poly2.setAttribute('stroke', '#f59e0b');
    poly2.setAttribute('stroke-width', '2');
    poly2.setAttribute('stroke-dasharray', '4 4');
    svg.appendChild(poly2);

    const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    txt.setAttribute('x', '250'); txt.setAttribute('y', '185');
    txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('fill', '#f43f5e'); txt.setAttribute('font-weight', 'bold');
    txt.textContent = 'Ambiguous: Acute △ and Obtuse △ share identical SSA data!';
    svg.appendChild(txt);
  }
}

// ----------------------------------------------------
// 7. ASA Congruence Lab
// ----------------------------------------------------
function updateASA() {
  const b = parseFloat(document.getElementById('asaBSlider')?.value) || 60;
  const base = parseFloat(document.getElementById('asaBaseSlider')?.value) || 10;
  const c = parseFloat(document.getElementById('asaCSlider')?.value) || 50;

  const bVal = document.getElementById('asaBVal');
  const baseVal = document.getElementById('asaBaseVal');
  const cVal = document.getElementById('asaCVal');
  const verdict = document.getElementById('asaVerdict');

  if (bVal) bVal.textContent = `${Math.round(b)}°`;
  if (baseVal) baseVal.textContent = `${base} cm`;
  if (cVal) cVal.textContent = `${Math.round(c)}°`;

  if (verdict) {
    verdict.textContent = `Base ${base} cm with angles ∠B=${Math.round(b)}° and ∠C=${Math.round(c)}° fix apex A uniquely: △ABC ≅ △PQR by ASA!`;
  }

  const svg = document.getElementById('asaSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const radB = degToRad(b);
  const radC = degToRad(c);
  const a = 180 - (b + c);
  const radA = degToRad(a);

  // Law of sines to find height
  const w = base * 13;
  const h = (w * Math.sin(radB) * Math.sin(radC)) / Math.sin(radA);
  const apexX = (h / Math.tan(radB));

  [70, 280].forEach(ox => {
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${ox},150 ${ox + w},150 ${ox + apexX},${150 - Math.min(100, h)}`);
    poly.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
    poly.setAttribute('stroke', '#10b981');
    poly.setAttribute('stroke-width', '2.5');
    svg.appendChild(poly);
  });
}

// ----------------------------------------------------
// 8. AAS Congruence Lab
// ----------------------------------------------------
function updateAAS() {
  const a = parseFloat(document.getElementById('aasASlider')?.value) || 50;
  const b = parseFloat(document.getElementById('aasBSlider')?.value) || 70;
  const c = 180 - (a + b);

  const aVal = document.getElementById('aasAVal');
  const bVal = document.getElementById('aasBVal');
  const cComp = document.getElementById('aasCComputed');

  if (aVal) aVal.textContent = `${Math.round(a)}°`;
  if (bVal) bVal.textContent = `${Math.round(b)}°`;
  if (cComp) cComp.textContent = `∠C = 180° - (${Math.round(a)}° + ${Math.round(b)}°) = ${Math.round(c)}°`;

  const svg = document.getElementById('aasSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly.setAttribute('points', '160,150 340,150 250,55');
  poly.setAttribute('fill', 'rgba(56, 189, 248, 0.2)');
  poly.setAttribute('stroke', '#38bdf8');
  poly.setAttribute('stroke-width', '2.5');
  svg.appendChild(poly);

  const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  txt.setAttribute('x', '250'); txt.setAttribute('y', '125');
  txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('fill', '#38bdf8'); txt.setAttribute('font-weight', 'bold');
  txt.textContent = `AAS automatically guarantees ASA!`;
  svg.appendChild(txt);
}

// ----------------------------------------------------
// 9. RHS Congruence Lab
// ----------------------------------------------------
function updateRHS() {
  const hyp = parseFloat(document.getElementById('rhsHypSlider')?.value) || 10;
  const leg = parseFloat(document.getElementById('rhsLegSlider')?.value) || 6;
  const third = Math.sqrt(Math.max(1, hyp * hyp - leg * leg));

  const hypVal = document.getElementById('rhsHypVal');
  const legVal = document.getElementById('rhsLegVal');
  const thirdLeg = document.getElementById('rhsThirdLeg');

  if (hypVal) hypVal.textContent = `${hyp} cm`;
  if (legVal) legVal.textContent = `${leg} cm`;
  if (thirdLeg) thirdLeg.textContent = `BC = √(${hyp}² - ${leg}²) = ${third.toFixed(1)} cm`;

  const svg = document.getElementById('rhsSvg');
  if (!svg) return;
  svg.innerHTML = '';

  [90, 290].forEach(ox => {
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', `${ox},140 ${ox + third * 12},140 ${ox},${140 - leg * 14}`);
    poly.setAttribute('fill', 'rgba(245, 158, 11, 0.2)');
    poly.setAttribute('stroke', '#f59e0b');
    poly.setAttribute('stroke-width', '2.5');
    svg.appendChild(poly);

    // 90° square at (ox, 140)
    const sq = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    sq.setAttribute('x', ox); sq.setAttribute('y', 140 - 16);
    sq.setAttribute('width', '16'); sq.setAttribute('height', '16');
    sq.setAttribute('fill', 'none'); sq.setAttribute('stroke', '#f43f5e'); sq.setAttribute('stroke-width', '1.5');
    svg.appendChild(sq);
  });
}

// ----------------------------------------------------
// 10. AAA Counterexample Dilation Studio
// ----------------------------------------------------
function updateAAA() {
  const scale = (parseFloat(document.getElementById('aaaScaleSlider')?.value) || 18) / 10;
  const scaleText = document.getElementById('aaaScaleText');
  const proof = document.getElementById('aaaAngleProof');

  if (scaleText) scaleText.textContent = `${scale.toFixed(1)}× Scale`;
  if (proof) proof.textContent = `Angles: 50°, 60°, 70° match identically, but Area is ${(scale * scale).toFixed(2)}× larger!`;

  const svg = document.getElementById('aaaSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Triangle 1: Base (100, 160 190, 160 145, 80)
  const poly1 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly1.setAttribute('points', '70,160 170,160 120,80');
  poly1.setAttribute('fill', 'rgba(56, 189, 248, 0.25)');
  poly1.setAttribute('stroke', '#38bdf8');
  poly1.setAttribute('stroke-width', '2');
  svg.appendChild(poly1);

  // Scaled Triangle 2
  const ox2 = 280;
  const w2 = 100 * scale;
  const h2 = 80 * scale;
  const poly2 = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly2.setAttribute('points', `${ox2},160 ${ox2 + w2},160 ${ox2 + w2/2},${160 - h2}`);
  poly2.setAttribute('fill', 'rgba(244, 63, 94, 0.25)');
  poly2.setAttribute('stroke', '#f43f5e');
  poly2.setAttribute('stroke-width', '2');
  svg.appendChild(poly2);
}

// ----------------------------------------------------
// 11. SSA Ambiguous Case
// ----------------------------------------------------
let ssaState = 'acute';

function setSsaPosition(pos) {
  ssaState = pos;
  const aBtn = document.getElementById('ssaAcuteBtn');
  const oBtn = document.getElementById('ssaObtuseBtn');
  const st = document.getElementById('ssaStatus');

  if (aBtn && oBtn) {
    if (pos === 'acute') {
      aBtn.className = 'px-3 py-1 bg-amber-500/30 text-amber-300 rounded border border-amber-500/50';
      oBtn.className = 'px-3 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
      if (st) st.textContent = 'Acute Triangle: Swinging side a hits at outer point B1.';
    } else {
      oBtn.className = 'px-3 py-1 bg-amber-500/30 text-amber-300 rounded border border-amber-500/50';
      aBtn.className = 'px-3 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700';
      if (st) st.textContent = 'Obtuse Triangle: Swinging side a hits at inner point B2.';
    }
  }
  renderSSAPendulum();
}

function toggleSsaSwing() {
  setSsaPosition(ssaState === 'acute' ? 'obtuse' : 'acute');
}

function renderSSAPendulum() {
  const svg = document.getElementById('ssaSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Baseline ray
  const baseLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  baseLine.setAttribute('x1', '60'); baseLine.setAttribute('y1', '150');
  baseLine.setAttribute('x2', '450'); baseLine.setAttribute('y2', '150');
  baseLine.setAttribute('stroke', '#64748b'); baseLine.setAttribute('stroke-width', '2');
  svg.appendChild(baseLine);

  // Arm b from (100, 150) to (220, 60)
  const armB = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  armB.setAttribute('x1', '100'); armB.setAttribute('y1', '150');
  armB.setAttribute('x2', '220'); armB.setAttribute('y2', '60');
  armB.setAttribute('stroke', '#38bdf8'); armB.setAttribute('stroke-width', '3');
  svg.appendChild(armB);

  // Swinging arc of radius 110 from (220, 60)
  const arc = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  arc.setAttribute('d', 'M 160 150 A 110 110 0 0 0 320 150');
  arc.setAttribute('fill', 'none'); arc.setAttribute('stroke', '#f43f5e'); arc.setAttribute('stroke-dasharray', '3 3');
  svg.appendChild(arc);

  const bTargetX = (ssaState === 'acute') ? 310 : 170;
  const swingArm = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  swingArm.setAttribute('x1', '220'); swingArm.setAttribute('y1', '60');
  swingArm.setAttribute('x2', `${bTargetX}`); swingArm.setAttribute('y2', '150');
  swingArm.setAttribute('stroke', '#f59e0b'); swingArm.setAttribute('stroke-width', '3');
  svg.appendChild(swingArm);
}

// ----------------------------------------------------
// 12. Isosceles Base Angles Proof
// ----------------------------------------------------
function updateIsosceles() {
  const apex = parseFloat(document.getElementById('isoApexSlider')?.value) || 50;
  const baseAng = (180 - apex) / 2;

  const aVal = document.getElementById('isoApexVal');
  const bAngles = document.getElementById('isoBaseAngles');

  if (aVal) aVal.textContent = `${Math.round(apex)}°`;
  if (bAngles) bAngles.textContent = `∠B = ∠C = (180° - ${Math.round(apex)}°) / 2 = ${baseAng.toFixed(1)}°`;

  const svg = document.getElementById('isoSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const w = 180;
  const h = 130;
  const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly.setAttribute('points', `160,160 ${160 + w},160 ${160 + w/2},${160 - h}`);
  poly.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
  poly.setAttribute('stroke', '#10b981');
  poly.setAttribute('stroke-width', '2.5');
  svg.appendChild(poly);

  // Altitude AD
  const alt = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  alt.setAttribute('x1', `${160 + w/2}`); alt.setAttribute('y1', `${160 - h}`);
  alt.setAttribute('x2', `${160 + w/2}`); alt.setAttribute('y2', '160');
  alt.setAttribute('stroke', '#f43f5e'); alt.setAttribute('stroke-width', '2');
  alt.setAttribute('stroke-dasharray', '4 4');
  svg.appendChild(alt);
}

function foldIsosceles() {
  const svg = document.getElementById('isoSvg');
  if (!svg) return;
  svg.innerHTML = '';

  // Folded triangle (half)
  const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly.setAttribute('points', '250,160 340,160 250,30');
  poly.setAttribute('fill', 'rgba(6, 182, 212, 0.4)');
  poly.setAttribute('stroke', '#06b6d4');
  poly.setAttribute('stroke-width', '3');
  svg.appendChild(poly);

  const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  txt.setAttribute('x', '250'); txt.setAttribute('y', '185');
  txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('fill', '#06b6d4'); txt.setAttribute('font-weight', 'bold');
  txt.textContent = 'Folded along AD: △ABD matches △ACD identically!';
  svg.appendChild(txt);
}

// ----------------------------------------------------
// 13. Equilateral 60 Degree Harmony
// ----------------------------------------------------
let eqAxesVisible = false;

function toggleEquilateralAxes() {
  eqAxesVisible = !eqAxesVisible;
  updateEquilateral();
}

function updateEquilateral() {
  const s = parseFloat(document.getElementById('eqSideSlider')?.value) || 10;
  const sVal = document.getElementById('eqSideVal');
  if (sVal) sVal.textContent = `${s} cm`;

  const svg = document.getElementById('eqSvg');
  if (!svg) return;
  svg.innerHTML = '';

  const w = s * 14;
  const h = w * (Math.sqrt(3) / 2);
  const cx = 250;
  const cy = 160;

  const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
  poly.setAttribute('points', `${cx - w/2},${cy} ${cx + w/2},${cy} ${cx},${cy - h}`);
  poly.setAttribute('fill', 'rgba(245, 158, 11, 0.2)');
  poly.setAttribute('stroke', '#f59e0b');
  poly.setAttribute('stroke-width', '2.5');
  svg.appendChild(poly);

  if (eqAxesVisible) {
    // 3 symmetry axes
    const makeAxis = (x1, y1, x2, y2) => {
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', x1); line.setAttribute('y1', y1);
      line.setAttribute('x2', x2); line.setAttribute('y2', y2);
      line.setAttribute('stroke', '#38bdf8'); line.setAttribute('stroke-width', '1.5'); line.setAttribute('stroke-dasharray', '3 3');
      svg.appendChild(line);
    };
    makeAxis(cx, cy - h, cx, cy);
    makeAxis(cx - w/2, cy, cx + w/4, cy - h/2);
    makeAxis(cx + w/2, cy, cx - w/4, cy - h/2);
  }
}

// ----------------------------------------------------
// 14. Master Criteria Sorter
// ----------------------------------------------------
const mcsScenarios = [
  { text: "Scenario 1: Sides AB = DE, BC = EF, and included ∠B = ∠E.", correct: "SAS" },
  { text: "Scenario 2: All 3 side lengths match: AB = PQ, BC = QR, CA = RP.", correct: "SSS" },
  { text: "Scenario 3: In right triangles, hypotenuses match and one leg matches.", correct: "RHS" },
  { text: "Scenario 4: Angles ∠A = ∠D, ∠B = ∠E, and included side AB = DE.", correct: "ASA" },
  { text: "Scenario 5: All 3 angles match identically, but no sides are measured.", correct: "INVALID" }
];
let mcsIndex = 0;
let mcsCorrectCount = 0;

function answerCriteriaSort(choice) {
  const sc = mcsScenarios[mcsIndex];
  const fb = document.getElementById('mcsFeedback');
  const scText = document.getElementById('mcsScenarioText');
  const score = document.getElementById('mcsScore');

  if (choice === sc.correct) {
    mcsCorrectCount++;
    if (fb) fb.innerHTML = `<span class='text-emerald-400 font-bold'>✓ Correct!</span> ${choice} is the exact mathematical match.`;
  } else {
    if (fb) fb.innerHTML = `<span class='text-rose-400 font-bold'>✗ Incorrect.</span> The correct answer is <strong>${sc.correct}</strong>.`;
  }

  mcsIndex = (mcsIndex + 1) % mcsScenarios.length;
  if (scText) scText.textContent = mcsScenarios[mcsIndex].text;
  if (score) score.textContent = `Score: ${mcsCorrectCount} / 5`;
}

// ----------------------------------------------------
// 15. Real World Twins & Tessellations
// ----------------------------------------------------
function setRwMode(mode) {
  const desc = document.getElementById('rwDescription');
  const bBridge = document.getElementById('rwBridgeBtn');
  const bButt = document.getElementById('rwButterflyBtn');
  const bTess = document.getElementById('rwTessBtn');
  const svg = document.getElementById('rwSvg');
  if (!svg) return;
  svg.innerHTML = '';

  if (bBridge && bButt && bTess) {
    bBridge.className = (mode === 'bridge') ? 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50' : 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
    bButt.className = (mode === 'butterfly') ? 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50' : 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
    bTess.className = (mode === 'tessellation') ? 'px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50' : 'px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700';
  }

  if (mode === 'bridge') {
    if (desc) desc.textContent = 'Warren Truss: Prefabricated congruent equilateral triangles distribute heavy bridge loads uniformly.';
    // Draw 4 congruent triangles in truss
    for (let i = 0; i < 4; i++) {
      const ox = 70 + i * 80;
      const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
      poly.setAttribute('points', `${ox},140 ${ox + 80},140 ${ox + 40},60`);
      poly.setAttribute('fill', 'rgba(245, 158, 11, 0.15)');
      poly.setAttribute('stroke', '#f59e0b'); poly.setAttribute('stroke-width', '2.5');
      svg.appendChild(poly);
    }
  } else if (mode === 'butterfly') {
    if (desc) desc.textContent = 'Bilateral Reflectional Symmetry: Left wing and right wing are congruent mirror twins across the central axis.';
    // Central line
    const axis = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    axis.setAttribute('x1', '250'); axis.setAttribute('y1', '30'); axis.setAttribute('x2', '250'); axis.setAttribute('y2', '170');
    axis.setAttribute('stroke', '#cbd5e1'); axis.setAttribute('stroke-dasharray', '4 4');
    svg.appendChild(axis);

    // Left wing & Right wing
    const wL = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    wL.setAttribute('points', '250,90 130,50 160,150');
    wL.setAttribute('fill', 'rgba(6, 182, 212, 0.3)'); wL.setAttribute('stroke', '#06b6d4'); wL.setAttribute('stroke-width', '2');
    svg.appendChild(wL);

    const wR = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    wR.setAttribute('points', '250,90 370,50 340,150');
    wR.setAttribute('fill', 'rgba(6, 182, 212, 0.3)'); wR.setAttribute('stroke', '#06b6d4'); wR.setAttribute('stroke-width', '2');
    svg.appendChild(wR);
  } else {
    if (desc) desc.textContent = 'Triangular Regular Tessellation: Identical congruent triangles tile a flat 2D plane with zero gaps.';
    for (let r = 0; r < 2; r++) {
      for (let c = 0; c < 5; c++) {
        const ox = 70 + c * 70;
        const oy = 60 + r * 60;
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', `${ox},${oy+50} ${ox+70},${oy+50} ${ox+35},${oy}`);
        poly.setAttribute('fill', ((r+c)%2 === 0) ? 'rgba(16, 185, 129, 0.2)' : 'rgba(56, 189, 248, 0.2)');
        poly.setAttribute('stroke', '#475569'); poly.setAttribute('stroke-width', '1.5');
        svg.appendChild(poly);
      }
    }
  }
}

// ----------------------------------------------------
// 16. Congruence Detective & CPCTC Solver
// ----------------------------------------------------
function revealCpctcStep1() {
  const box = document.getElementById('cpctcResultBox');
  if (box) {
    box.innerHTML = `<span class='text-amber-400 font-bold'>Step 1 (Side Equality):</span> $3x - 4 = 14 \\implies 3x = 18 \\implies \\mathbf{x = 6\\text{ cm}}$!`;
    if (window.triggerMathRender) setTimeout(() => triggerMathRender(box), 10);
  }
}

function revealCpctcStep2() {
  const box = document.getElementById('cpctcResultBox');
  if (box) {
    box.innerHTML = `<span class='text-cyan-400 font-bold'>Step 2 (Angle Equality):</span> $2y + 10^\\circ = 80^\\circ \\implies 2y = 70^\\circ \\implies \\mathbf{y = 35^\\circ}$!`;
    if (window.triggerMathRender) setTimeout(() => triggerMathRender(box), 10);
  }
}

function resetCpctcPuzzle() {
  const box = document.getElementById('cpctcResultBox');
  if (box) {
    box.textContent = 'Click Step 1 or Step 2 to deduce the algebraic values of x and y using CPCTC!';
  }
}

// ----------------------------------------------------
// MASTER SIMULATOR INITIALIZER ON SLIDE CHANGE
// ----------------------------------------------------
function initSimulators(slideIndex) {
  switch (slideIndex) {
    case 0:
      updateSuperposition();
      break;
    case 1:
      setSimpleFigureMode('lines');
      break;
    case 2:
      renderTriangleCorrespondence('A');
      break;
    case 3:
      updateSSS();
      break;
    case 4:
      updateSAS();
      break;
    case 5:
      setTrapMode('included');
      break;
    case 6:
      updateASA();
      break;
    case 7:
      updateAAS();
      break;
    case 8:
      updateRHS();
      break;
    case 9:
      updateAAA();
      break;
    case 10:
      renderSSAPendulum();
      break;
    case 11:
      updateIsosceles();
      break;
    case 12:
      updateEquilateral();
      break;
    case 13:
      // Sorter scenario 1
      break;
    case 14:
      setRwMode('bridge');
      break;
    case 15:
      resetCpctcPuzzle();
      break;
  }
}
"""

with open('.agents/class7_math_geometric_twins_js.py', 'w', encoding='utf-8') as f:
    f.write(f"SIMULATORS_JS = {repr(js_content)}\n")

print("Created .agents/class7_math_geometric_twins_js.py successfully!")


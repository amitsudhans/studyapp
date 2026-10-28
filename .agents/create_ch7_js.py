js_content = r"""
// ==========================================
// 16 BESPOKE SIMULATOR INTERACTIVE ENGINES
// ==========================================

// 1. Triangle Anatomy
let anatomyLabelsVisible = true;
function updateAnatomyApex(xVal) {
  const x = parseFloat(xVal);
  const vC = document.getElementById('vC');
  const triPoly = document.getElementById('triPoly');
  const lineAC = document.getElementById('lineAC');
  const lineBC = document.getElementById('lineBC');
  const lblA = document.getElementById('txtAngleA');
  const lblB = document.getElementById('txtAngleB');
  const lblC = document.getElementById('txtAngleC');
  const lblSideB = document.getElementById('lblSideB');
  const lblSideA = document.getElementById('lblSideA');

  if (!vC || !triPoly) return;

  vC.setAttribute('cx', x);
  triPoly.setAttribute('points', `100,200 400,200 ${x},50`);

  // Update line AC and BC extensions
  if (lineAC) {
    const slopeAC = (50 - 200) / (x - 100);
    lineAC.setAttribute('x1', 100 - 60);
    lineAC.setAttribute('y1', 200 - 60 * slopeAC);
    lineAC.setAttribute('x2', x + 50);
    lineAC.setAttribute('y2', 50 + 50 * slopeAC);
  }
  if (lineBC) {
    const slopeBC = (50 - 200) / (x - 400);
    lineBC.setAttribute('x1', 400 + 60);
    lineBC.setAttribute('y1', 200 + 60 * slopeBC);
    lineBC.setAttribute('x2', x - 50);
    lineBC.setAttribute('y2', 50 - 50 * slopeBC);
  }

  // Calculate angles
  const angA = Math.atan2(150, x - 100) * (180 / Math.PI);
  const angB = Math.atan2(150, 400 - x) * (180 / Math.PI);
  const angC = 180 - (angA + angB);

  if (lblA) lblA.textContent = `${angA.toFixed(1)}°`;
  if (lblB) lblB.textContent = `${angB.toFixed(1)}°`;
  if (lblC) lblC.textContent = `${angC.toFixed(1)}°`;

  if (lblSideB) {
    lblSideB.setAttribute('x', ((100 + x) / 2) - 25);
    lblSideB.setAttribute('y', 125);
  }
  if (lblSideA) {
    lblSideA.setAttribute('x', ((400 + x) / 2) + 25);
    lblSideA.setAttribute('y', 125);
  }
}

function resetAnatomy() {
  const slider = document.getElementById('apexSlider');
  if (slider) slider.value = 250;
  updateAnatomyApex(250);
}

function toggleAnatomyLabels() {
  anatomyLabelsVisible = !anatomyLabelsVisible;
  const labels = ['lblSideA', 'lblSideB', 'lblSideC'];
  labels.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.style.display = anatomyLabelsVisible ? 'block' : 'none';
  });
}

// 2. Equilateral Triangle Compass
function stepEquilateral(step) {
  const arcA = document.getElementById('eqArcA');
  const arcB = document.getElementById('eqArcB');
  const apex = document.getElementById('eqApexPt');
  const apexLbl = document.getElementById('eqApexLbl');
  const sideAC = document.getElementById('eqSideAC');
  const sideBC = document.getElementById('eqSideBC');
  const angleTags = document.getElementById('eqAngleTags');
  const status = document.getElementById('eqStatus');

  if (!arcA) return;

  // Arc path definitions: radius = 180 px
  // Arc from A(160, 190): angle from -75 deg to -45 deg
  arcA.setAttribute('d', 'M 215 48 A 180 180 0 0 0 285 24');
  // Arc from B(340, 190): angle from -135 deg to -105 deg
  arcB.setAttribute('d', 'M 215 24 A 180 180 0 0 0 285 48');

  if (step === 1) {
    arcA.style.opacity = '0';
    arcB.style.opacity = '0';
    apex.style.opacity = '0';
    apexLbl.style.opacity = '0';
    sideAC.style.opacity = '0';
    sideBC.style.opacity = '0';
    angleTags.style.opacity = '0';
    if (status) status.innerHTML = '<strong>Step 1:</strong> Base segment $AB$ of length $s = 180\\text{ px}$ is laid down with a ruler.';
  } else if (step === 2) {
    arcA.style.opacity = '1';
    arcB.style.opacity = '0';
    apex.style.opacity = '0';
    apexLbl.style.opacity = '0';
    sideAC.style.opacity = '0';
    sideBC.style.opacity = '0';
    angleTags.style.opacity = '0';
    if (status) status.innerHTML = '<strong>Step 2:</strong> Compass opened to radius $s = 180\\text{ px}$, centered at $A$, swings an arc above the base.';
  } else if (step === 3) {
    arcA.style.opacity = '1';
    arcB.style.opacity = '1';
    apex.style.opacity = '1';
    apexLbl.style.opacity = '1';
    sideAC.style.opacity = '0';
    sideBC.style.opacity = '0';
    angleTags.style.opacity = '0';
    if (status) status.innerHTML = '<strong>Step 3:</strong> Compass with same radius $s$, centered at $B$, swings second arc intersecting at point $C$.';
  } else if (step === 4) {
    arcA.style.opacity = '0.5';
    arcB.style.opacity = '0.5';
    apex.style.opacity = '1';
    apexLbl.style.opacity = '1';
    sideAC.style.opacity = '1';
    sideBC.style.opacity = '1';
    angleTags.style.opacity = '1';
    if (status) status.innerHTML = '<strong>Step 4:</strong> Join $AC$ and $BC$. Triangle $ABC$ is equilateral: 3 equal sides and three $60^\\circ$ angles!';
  }
}

// 3. Triangle Inequality Tester
function setInequalityPreset(a, b, c) {
  const sA = document.getElementById('sliderA');
  const sB = document.getElementById('sliderB');
  const sC = document.getElementById('sliderC');
  if (sA) sA.value = a;
  if (sB) sB.value = b;
  if (sC) sC.value = c;
  updateInequality();
}

function updateInequality() {
  const a = parseFloat(document.getElementById('sliderA')?.value || 6);
  const b = parseFloat(document.getElementById('sliderB')?.value || 8);
  const c = parseFloat(document.getElementById('sliderC')?.value || 10);

  document.getElementById('valA').textContent = `${a} cm`;
  document.getElementById('valB').textContent = `${b} cm`;
  document.getElementById('valC').textContent = `${c} cm`;

  const chk1 = a + b > c;
  const chk2 = b + c > a;
  const chk3 = c + a > b;

  const elChk1 = document.getElementById('chk1');
  const elChk2 = document.getElementById('chk2');
  const elChk3 = document.getElementById('chk3');
  if (elChk1) {
    elChk1.textContent = `a + b > c (${a}+${b} ${chk1 ? '>' : '≤'} ${c}) ${chk1 ? '✓' : '✗'}`;
    elChk1.className = chk1 ? 'text-emerald-400' : 'text-rose-400 font-bold';
  }
  if (elChk2) {
    elChk2.textContent = `b + c > a (${b}+${c} ${chk2 ? '>' : '≤'} ${a}) ${chk2 ? '✓' : '✗'}`;
    elChk2.className = chk2 ? 'text-emerald-400' : 'text-rose-400 font-bold';
  }
  if (elChk3) {
    elChk3.textContent = `c + a > b (${c}+${a} ${chk3 ? '>' : '≤'} ${b}) ${chk3 ? '✓' : '✗'}`;
    elChk3.className = chk3 ? 'text-emerald-400' : 'text-rose-400 font-bold';
  }

  const armA = document.getElementById('ineqArmA');
  const armB = document.getElementById('ineqArmB');
  const apex = document.getElementById('ineqApex');
  const badgeRect = document.getElementById('ineqBadgeRect');
  const badgeText = document.getElementById('ineqBadgeText');

  const baseX1 = 100;
  const baseX2 = 100 + c * 25; // Scale: 25 px per cm
  const baseLine = document.getElementById('ineqBase');
  if (baseLine) {
    baseLine.setAttribute('x1', baseX1);
    baseLine.setAttribute('x2', baseX2);
  }
  const baseLbl = document.getElementById('ineqBaseLbl');
  if (baseLbl) {
    baseLbl.setAttribute('x', (baseX1 + baseX2) / 2);
    baseLbl.textContent = `Base c = ${c} cm`;
  }

  if (chk1 && chk2 && chk3) {
    // Triangle exists! Calculate apex by circle intersection
    // x = (c^2 + a^2 - b^2) / (2c)
    const xDist = (c * c + a * a - b * b) / (2 * c);
    const yDist = Math.sqrt(Math.max(0, a * a - xDist * xDist));

    const apexX = baseX1 + xDist * 25;
    const apexY = 180 - yDist * 25;

    if (armA) { armA.setAttribute('x1', baseX1); armA.setAttribute('y1', 180); armA.setAttribute('x2', apexX); armA.setAttribute('y2', apexY); }
    if (armB) { armB.setAttribute('x1', baseX2); armB.setAttribute('y1', 180); armB.setAttribute('x2', apexX); armB.setAttribute('y2', apexY); }
    if (apex) { apex.setAttribute('cx', apexX); apex.setAttribute('cy', apexY); apex.style.opacity = '1'; }

    if (badgeRect) { badgeRect.setAttribute('fill', '#10b981'); badgeRect.setAttribute('width', 160); badgeRect.setAttribute('x', 170); }
    if (badgeText) { badgeText.textContent = 'TRIANGLE FORMED ✓'; badgeText.setAttribute('fill', '#10b981'); }
  } else if (a + b === c) {
    // Flat line collapse
    const meetX = baseX1 + a * 25;
    if (armA) { armA.setAttribute('x1', baseX1); armA.setAttribute('y1', 180); armA.setAttribute('x2', meetX); armA.setAttribute('y2', 180); }
    if (armB) { armB.setAttribute('x1', baseX2); armB.setAttribute('y1', 180); armB.setAttribute('x2', meetX); armB.setAttribute('y2', 180); }
    if (apex) { apex.setAttribute('cx', meetX); apex.setAttribute('cy', 180); apex.style.opacity = '1'; }

    if (badgeRect) { badgeRect.setAttribute('fill', '#f59e0b'); badgeRect.setAttribute('width', 220); badgeRect.setAttribute('x', 140); }
    if (badgeText) { badgeText.textContent = 'FLAT LINE: a + b = c (No Area)'; badgeText.setAttribute('fill', '#f59e0b'); }
  } else {
    // Gap: impossible
    const reachA = baseX1 + a * 25 * 0.95;
    const reachB = baseX2 - b * 25 * 0.95;
    if (armA) { armA.setAttribute('x1', baseX1); armA.setAttribute('y1', 180); armA.setAttribute('x2', reachA); armA.setAttribute('y2', 180); }
    if (armB) { armB.setAttribute('x1', baseX2); armB.setAttribute('y1', 180); armB.setAttribute('x2', reachB); armB.setAttribute('y2', 180); }
    if (apex) apex.style.opacity = '0';

    if (badgeRect) { badgeRect.setAttribute('fill', '#f43f5e'); badgeRect.setAttribute('width', 220); badgeRect.setAttribute('x', 140); }
    if (badgeText) { badgeText.textContent = 'IMPOSSIBLE GAP: a + b < c'; badgeText.setAttribute('fill', '#f43f5e'); }
  }
}

// 4. Circle Intersections
function updateCircleIntersections() {
  const rA = parseFloat(document.getElementById('slideRadA')?.value || 110);
  const rB = parseFloat(document.getElementById('slideRadB')?.value || 100);

  document.getElementById('txtRadA').textContent = `${rA} px`;
  document.getElementById('txtRadB').textContent = `${rB} px`;

  const circA = document.getElementById('circA');
  const circB = document.getElementById('circB');
  if (circA) circA.setAttribute('r', rA);
  if (circB) circB.setAttribute('r', rB);

  const d = 180; // distance between A(160, 110) and B(340, 110)
  const badge = document.getElementById('circCaseLabel');
  const pt1 = document.getElementById('circPt1');
  const pt2 = document.getElementById('circPt2');
  const lbl1 = document.getElementById('circLbl1');
  const lbl2 = document.getElementById('circLbl2');
  const tri1 = document.getElementById('triTop1');
  const tri2 = document.getElementById('triTop2');

  if (rA + rB < d) {
    // Non-intersecting
    if (badge) { badge.textContent = '0 Intersections: Too Far Apart (No Triangle)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40'; }
    if (pt1) pt1.style.opacity = '0';
    if (pt2) pt2.style.opacity = '0';
    if (lbl1) lbl1.style.opacity = '0';
    if (lbl2) lbl2.style.opacity = '0';
    if (tri1) tri1.style.opacity = '0';
    if (tri2) tri2.style.opacity = '0';
  } else if (Math.abs(rA + rB - d) < 3) {
    // Externally tangent (1 point)
    if (badge) { badge.textContent = '1 Intersection: Tangent on Line AB (Degenerate)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
    const tx = 160 + rA;
    if (pt1) { pt1.setAttribute('cx', tx); pt1.setAttribute('cy', 110); pt1.style.opacity = '1'; }
    if (pt2) pt2.style.opacity = '0';
    if (lbl1) { lbl1.setAttribute('x', tx); lbl1.setAttribute('y', 95); lbl1.textContent = 'Tangent Point'; lbl1.style.opacity = '1'; }
    if (lbl2) lbl2.style.opacity = '0';
    if (tri1) tri1.style.opacity = '0';
    if (tri2) tri2.style.opacity = '0';
  } else if (Math.abs(rA - rB) > d) {
    // Nested inside
    if (badge) { badge.textContent = '0 Intersections: One Circle Inside Another'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40'; }
    if (pt1) pt1.style.opacity = '0';
    if (pt2) pt2.style.opacity = '0';
    if (lbl1) lbl1.style.opacity = '0';
    if (lbl2) lbl2.style.opacity = '0';
    if (tri1) tri1.style.opacity = '0';
    if (tri2) tri2.style.opacity = '0';
  } else {
    // 2 intersections
    if (badge) { badge.textContent = '2 Intersections: Top & Mirror Congruent Triangles'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40'; }
    const xDist = (d * d + rA * rA - rB * rB) / (2 * d);
    const yDist = Math.sqrt(Math.max(0, rA * rA - xDist * xDist));
    const cx = 160 + xDist;
    const cy1 = 110 - yDist;
    const cy2 = 110 + yDist;

    if (pt1) { pt1.setAttribute('cx', cx); pt1.setAttribute('cy', cy1); pt1.style.opacity = '1'; }
    if (pt2) { pt2.setAttribute('cx', cx); pt2.setAttribute('cy', cy2); pt2.style.opacity = '1'; }
    if (lbl1) { lbl1.setAttribute('x', cx); lbl1.setAttribute('y', cy1 - 10); lbl1.textContent = 'C₁ (Top Triangle)'; lbl1.style.opacity = '1'; }
    if (lbl2) { lbl2.setAttribute('x', cx); lbl2.setAttribute('y', cy2 + 15); lbl2.textContent = 'C₂ (Mirror Triangle)'; lbl2.style.opacity = '1'; }

    if (tri1) { tri1.setAttribute('x2', cx); tri1.setAttribute('y2', cy1); tri1.style.opacity = '1'; }
    if (tri2) { tri2.setAttribute('x2', cx); tri2.setAttribute('y2', cy1); tri2.style.opacity = '1'; }
  }
}

// 5. SSS Construction
function setSSSPreset(type) {
  const desc = document.getElementById('sssDescription');
  const arcA = document.getElementById('sssArcA');
  const arcB = document.getElementById('sssArcB');
  const apex = document.getElementById('sssApex');
  const sideA = document.getElementById('sssSideA');
  const sideB = document.getElementById('sssSideB');
  const lblA = document.getElementById('sssLblA');
  const lblB = document.getElementById('sssLblB');
  const baseTxt = document.getElementById('sssBaseText');

  if (type === 'scalene') {
    if (desc) desc.textContent = 'Scalene Triangle: All three sides are distinct (7 cm, 5 cm, 4 cm).';
    if (baseTxt) baseTxt.textContent = 'c = 7 cm';
    if (lblB) lblB.textContent = 'b = 5 cm';
    if (lblA) lblA.textContent = 'a = 4 cm';
    if (apex) { apex.setAttribute('cx', 210); apex.setAttribute('cy', 55); }
    if (sideB) { sideB.setAttribute('x2', 210); sideB.setAttribute('y2', 55); }
    if (sideA) { sideA.setAttribute('x2', 210); sideA.setAttribute('y2', 55); }
    if (arcA) arcA.setAttribute('d', 'M 180 70 A 155 155 0 0 0 240 45');
    if (arcB) arcB.setAttribute('d', 'M 190 45 A 190 190 0 0 0 230 70');
  } else if (type === 'isosceles') {
    if (desc) desc.textContent = 'Isosceles Triangle: Two sides are equal (6 cm, 6 cm, base 4 cm). Equal base angles!';
    if (baseTxt) baseTxt.textContent = 'c = 4 cm (base)';
    if (lblB) lblB.textContent = 'b = 6 cm';
    if (lblA) lblA.textContent = 'a = 6 cm';
    if (apex) { apex.setAttribute('cx', 250); apex.setAttribute('cy', 40); }
    if (sideB) { sideB.setAttribute('x2', 250); sideB.setAttribute('y2', 40); }
    if (sideA) { sideA.setAttribute('x2', 250); sideA.setAttribute('y2', 40); }
    if (arcA) arcA.setAttribute('d', 'M 220 50 A 180 180 0 0 0 280 30');
    if (arcB) arcB.setAttribute('d', 'M 220 30 A 180 180 0 0 0 280 50');
  } else if (type === 'equilateral') {
    if (desc) desc.textContent = 'Equilateral Triangle: All three sides equal (5 cm, 5 cm, 5 cm). Symmetry of 60°!';
    if (baseTxt) baseTxt.textContent = 's = 5 cm';
    if (lblB) lblB.textContent = 's = 5 cm';
    if (lblA) lblA.textContent = 's = 5 cm';
    if (apex) { apex.setAttribute('cx', 250); apex.setAttribute('cy', 45); }
    if (sideB) { sideB.setAttribute('x2', 250); sideB.setAttribute('y2', 45); }
    if (sideA) { sideA.setAttribute('x2', 250); sideA.setAttribute('y2', 45); }
    if (arcA) arcA.setAttribute('d', 'M 220 55 A 160 160 0 0 0 280 35');
    if (arcB) arcB.setAttribute('d', 'M 220 35 A 160 160 0 0 0 280 55');
  }
}

function animateSSSConstruction() {
  const arcA = document.getElementById('sssArcA');
  const arcB = document.getElementById('sssArcB');
  if (arcA && arcB) {
    arcA.style.opacity = '0';
    arcB.style.opacity = '0';
    setTimeout(() => { arcA.style.transition = 'opacity 0.4s'; arcA.style.opacity = '1'; }, 200);
    setTimeout(() => { arcB.style.transition = 'opacity 0.4s'; arcB.style.opacity = '1'; }, 700);
  }
}

// 6. SAS Construction
function updateSAS() {
  const deg = parseFloat(document.getElementById('sasSliderAngle')?.value || 50);
  const bCm = parseFloat(document.getElementById('sasSliderB')?.value || 50) / 10;

  document.getElementById('sasValAngle').textContent = `${deg}°`;
  document.getElementById('sasValB').textContent = `${bCm.toFixed(1)} cm`;

  const rad = deg * (Math.PI / 180);
  const bPx = bCm * 28; // Scale factor

  const cx = 120 + bPx * Math.cos(rad);
  const cy = 180 - bPx * Math.sin(rad);

  const sideB = document.getElementById('sasSideB');
  const sideA = document.getElementById('sasSideA');
  const ray = document.getElementById('sasRay');
  const vC = document.getElementById('sasVertexC');
  const txtC = document.getElementById('sasTextC');
  const lblB = document.getElementById('sasLblB');
  const lblA = document.getElementById('sasLblA');
  const arc = document.getElementById('sasAngleArc');
  const txtAng = document.getElementById('sasAngleText');

  if (sideB) { sideB.setAttribute('x2', cx); sideB.setAttribute('y2', cy); }
  if (sideA) { sideA.setAttribute('x1', cx); sideA.setAttribute('y1', cy); }
  if (vC) { vC.setAttribute('cx', cx); vC.setAttribute('cy', cy); }
  if (txtC) { txtC.setAttribute('x', cx); txtC.setAttribute('y', cy - 12); }

  if (ray) {
    const rayLen = 220;
    ray.setAttribute('x2', 120 + rayLen * Math.cos(rad));
    ray.setAttribute('y2', 180 - rayLen * Math.sin(rad));
  }

  // Update angle arc
  const arcR = 35;
  const arcEndX = 120 + arcR * Math.cos(rad);
  const arcEndY = 180 - arcR * Math.sin(rad);
  if (arc) arc.setAttribute('d', `M ${120 + arcR} 180 A ${arcR} ${arcR} 0 0 0 ${arcEndX} ${arcEndY}`);
  if (txtAng) {
    txtAng.setAttribute('x', 120 + 45 * Math.cos(rad / 2));
    txtAng.setAttribute('y', 180 - 45 * Math.sin(rad / 2));
    txtAng.textContent = `${deg}°`;
  }

  // Cosine law for third side a: a^2 = b^2 + c^2 - 2bc cos(deg)
  const cCm = 6.0;
  const aCm = Math.sqrt(bCm * bCm + cCm * cCm - 2 * bCm * cCm * Math.cos(rad));
  const calcText = document.getElementById('sasCalcSide');
  if (calcText) calcText.textContent = `Side a (locked) = ${aCm.toFixed(2)} cm`;
  if (lblA) lblA.textContent = `a = ${aCm.toFixed(1)} cm`;
  if (lblB) lblB.textContent = `b = ${bCm.toFixed(1)} cm`;
}

// 7. ASA Construction
function updateASA() {
  const bDeg = parseFloat(document.getElementById('asaSlideB')?.value || 60);
  const cDeg = parseFloat(document.getElementById('asaSlideC')?.value || 50);

  document.getElementById('asaValB').textContent = `${bDeg}°`;
  document.getElementById('asaValC').textContent = `${cDeg}°`;

  const sum = bDeg + cDeg;
  const sumEl = document.getElementById('asaAngleSum');
  const angAEl = document.getElementById('asaAngleA');
  const badge = document.getElementById('asaStatusBadge');

  const rayB = document.getElementById('asaRayB');
  const rayC = document.getElementById('asaRayC');
  const apex = document.getElementById('asaApex');
  const apexLbl = document.getElementById('asaApexLbl');

  if (sumEl) sumEl.textContent = `Sum: ${bDeg}° + ${cDeg}° = ${sum}° (${sum < 180 ? '< 180°' : '≥ 180°'})`;

  if (sum < 180) {
    const aDeg = 180 - sum;
    if (angAEl) angAEl.textContent = `Calculated Angle A: ${aDeg}°`;
    if (badge) { badge.textContent = `Convergent: Triangle Exists (∠A = ${aDeg}°)`; badge.className = 'px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40'; }

    // Intersecting rays
    const bRad = bDeg * (Math.PI / 180);
    const cRad = cDeg * (Math.PI / 180);
    // Base BC length = 260 px (from 120 to 380)
    // x = 120 + 260 * (tan(c) / (tan(b) + tan(c)))
    const tanB = Math.tan(bRad);
    const tanC = Math.tan(cRad);
    const h = 260 / ((1 / tanB) + (1 / tanC));
    const ax = 120 + h / tanB;
    const ay = 180 - h;

    if (rayB) { rayB.setAttribute('x2', ax); rayB.setAttribute('y2', ay); }
    if (rayC) { rayC.setAttribute('x2', ax); rayC.setAttribute('y2', ay); }
    if (apex) { apex.setAttribute('cx', ax); apex.setAttribute('cy', ay); apex.style.opacity = '1'; }
    if (apexLbl) { apexLbl.setAttribute('x', ax); apexLbl.setAttribute('y', ay - 12); apexLbl.style.opacity = '1'; }
  } else if (sum === 180) {
    if (angAEl) angAEl.textContent = `Angle A = 0° (Parallel Lines)`;
    if (badge) { badge.textContent = 'Parallel Rays: Never Meet! (Sum = 180°)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
    if (rayB) { rayB.setAttribute('x2', 120 + 150 * Math.cos(bDeg * Math.PI / 180)); rayB.setAttribute('y2', 180 - 150 * Math.sin(bDeg * Math.PI / 180)); }
    if (rayC) { rayC.setAttribute('x2', 380 - 150 * Math.cos(cDeg * Math.PI / 180)); rayC.setAttribute('y2', 180 - 150 * Math.sin(cDeg * Math.PI / 180)); }
    if (apex) apex.style.opacity = '0';
    if (apexLbl) apexLbl.style.opacity = '0';
  } else {
    if (angAEl) angAEl.textContent = `Angle A < 0° (Divergent)`;
    if (badge) { badge.textContent = 'Divergent Rays: Rays Drift Apart! (Sum > 180°)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40'; }
    if (rayB) { rayB.setAttribute('x2', 120 + 120 * Math.cos(bDeg * Math.PI / 180)); rayB.setAttribute('y2', 180 - 120 * Math.sin(bDeg * Math.PI / 180)); }
    if (rayC) { rayC.setAttribute('x2', 380 - 120 * Math.cos(cDeg * Math.PI / 180)); rayC.setAttribute('y2', 180 - 120 * Math.sin(cDeg * Math.PI / 180)); }
    if (apex) apex.style.opacity = '0';
    if (apexLbl) apexLbl.style.opacity = '0';
  }
}

// 8. Angle Sum Proof
function setAngleSumMode(mode) {
  const line = document.getElementById('parallelLine');
  const lbl = document.getElementById('lblLineXY');
  const alt = document.getElementById('alternateAngles');
  const arc = document.getElementById('straightAngleArc');
  const expl = document.getElementById('aspExplanation');
  const btnP = document.getElementById('btnSumParallel');
  const btnT = document.getElementById('btnSumTearoff');

  if (mode === 'parallel') {
    if (line) line.style.opacity = '1';
    if (lbl) lbl.style.opacity = '1';
    if (alt) alt.style.opacity = '1';
    if (arc) arc.style.opacity = '1';
    if (expl) expl.innerHTML = 'Line $XY$ through vertex $A$ is parallel to base $BC$. Alternate interior angles give $\\angle XAB = \\angle 2$ and $\\angle YAC = \\angle 3$. Together on straight line $XY$: $\\angle 2 + \\angle 1 + \\angle 3 = 180^\\circ$.';
    if (btnP) { btnP.className = 'px-2.5 py-1 text-xs font-semibold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
    if (btnT) { btnT.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600'; }
  } else {
    if (expl) expl.innerHTML = '<strong>Paper Tear-Off Activity:</strong> When all 3 corners $\\angle 1, \\angle 2, \\angle 3$ are cut and assembled with their apexes touching, they form a flawless continuous straight line of $180^\\circ$!';
    if (btnT) { btnT.className = 'px-2.5 py-1 text-xs font-semibold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
    if (btnP) { btnP.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600'; }
  }
}

// 9. Exterior Angle Theorem
function updateExtAngle(xVal) {
  const x = parseFloat(xVal);
  const vA = document.getElementById('extVertexA');
  const sideAB = document.getElementById('extSideAB');
  const sideAC = document.getElementById('extSideAC');
  const lblA = document.getElementById('extLblA');
  const lblB = document.getElementById('extLblB');
  const lblExt = document.getElementById('extLblExt');
  const lblAdj = document.getElementById('extLblAdj');
  const eq = document.getElementById('extTheoremEq');

  if (vA) vA.setAttribute('cx', x);
  if (sideAB) { sideAB.setAttribute('x2', x); sideAB.setAttribute('y2', 50); }
  if (sideAC) { sideAC.setAttribute('x1', x); sideAC.setAttribute('y1', 50); }

  const angB = Math.atan2(120, x - 80) * (180 / Math.PI);
  const angC_int = Math.atan2(120, 320 - x) * (180 / Math.PI);
  const angA = 180 - (angB + angC_int);
  const angExt = 180 - angC_int;

  if (lblA) { lblA.setAttribute('x', x); lblA.textContent = `A (${angA.toFixed(0)}°)`; }
  if (lblB) lblB.textContent = `${angB.toFixed(0)}°`;
  if (lblAdj) lblAdj.textContent = `${angC_int.toFixed(0)}°`;
  if (lblExt) lblExt.textContent = `${angExt.toFixed(0)}° (Ext)`;
  if (eq) eq.textContent = `∠ACD (${angExt.toFixed(0)}°) = ∠A (${angA.toFixed(0)}°) + ∠B (${angB.toFixed(0)}°)`;
}

// 10. Altitude Definition
function updateAltDef(xVal) {
  const x = parseFloat(xVal);
  const apex = document.getElementById('altDefApex');
  const apexLbl = document.getElementById('altDefApexLbl');
  const ab = document.getElementById('altDefAB');
  const ac = document.getElementById('altDefAC');
  const line = document.getElementById('altDefLine');
  const foot = document.getElementById('altDefFoot');
  const footLbl = document.getElementById('altDefFootLbl');
  const rt = document.getElementById('altDefRtSymbol');
  const stats = document.getElementById('altStats');

  if (apex) apex.setAttribute('cx', x);
  if (apexLbl) apexLbl.setAttribute('x', x);
  if (ab) ab.setAttribute('x2', x);
  if (ac) ac.setAttribute('x2', x);

  if (line) { line.setAttribute('x1', x); line.setAttribute('x2', x); }
  if (foot) foot.setAttribute('cx', x);
  if (footLbl) footLbl.setAttribute('x', x);
  if (rt) rt.setAttribute('d', `M ${x} 165 L ${x + 15} 165 L ${x + 15} 180`);

  const baseLen = 280;
  const height = 130;
  const area = 0.5 * baseLen * height;
  if (stats) stats.textContent = `Base b = ${baseLen} px | Height h = ${height} px | Area = ${area} sq px`;
}

// 11. Drafting Altitudes with Set Square
function updateSetSquarePos(val) {
  const el = document.getElementById('movableSetSquare');
  if (el) el.setAttribute('transform', `translate(${val}, 0)`);
}

function snapAndDropAltitude() {
  const slider = document.getElementById('setSquareSlider');
  if (slider) slider.value = 250;
  updateSetSquarePos(250);

  const alt = document.getElementById('sqAltLine');
  const rt = document.getElementById('sqRtCorner');
  if (alt) alt.style.opacity = '1';
  if (rt) rt.style.opacity = '1';
}

// 12. Altitudes in Special Triangles (Inside, On, Outside)
function setAltCase(type) {
  const poly = document.getElementById('altCasePoly');
  const vA = document.getElementById('altCaseVA');
  const txtA = document.getElementById('altCaseTxtA');
  const vB = document.getElementById('altCaseVB');
  const txtB = document.getElementById('altCaseTxtB');
  const alt1 = document.getElementById('altCaseLine1');
  const foot1 = document.getElementById('altCaseFoot1');
  const ext = document.getElementById('altCaseExt');
  const desc = document.getElementById('altCaseDesc');

  const btnA = document.getElementById('btnCaseAcute');
  const btnR = document.getElementById('btnCaseRight');
  const btnO = document.getElementById('btnCaseObtuse');

  if (type === 'acute') {
    if (poly) poly.setAttribute('points', '140,170 380,170 240,50');
    if (vA) { vA.setAttribute('cx', 240); vA.setAttribute('cy', 50); }
    if (txtA) { txtA.setAttribute('x', 240); txtA.setAttribute('y', 38); }
    if (vB) { vB.setAttribute('cx', 140); vB.setAttribute('cy', 170); }
    if (txtB) { txtB.setAttribute('x', 125); txtB.setAttribute('y', 185); }
    if (alt1) { alt1.setAttribute('x1', 240); alt1.setAttribute('y1', 50); alt1.setAttribute('x2', 240); alt1.setAttribute('y2', 170); }
    if (foot1) { foot1.setAttribute('cx', 240); foot1.setAttribute('cy', 170); }
    if (ext) ext.style.opacity = '0';
    if (desc) desc.textContent = 'Acute Triangle: All three angles < 90°. All three altitudes land strictly INSIDE the triangle!';
    if (btnA) btnA.className = 'px-2.5 py-1 text-xs font-semibold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40';
    if (btnR) btnR.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (btnO) btnO.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
  } else if (type === 'right') {
    if (poly) poly.setAttribute('points', '140,170 380,170 140,50');
    if (vA) { vA.setAttribute('cx', 140); vA.setAttribute('cy', 50); }
    if (txtA) { txtA.setAttribute('x', 140); txtA.setAttribute('y', 38); }
    if (vB) { vB.setAttribute('cx', 140); vB.setAttribute('cy', 170); }
    if (txtB) { txtB.setAttribute('x', 120); txtB.setAttribute('y', 185); }
    if (alt1) { alt1.setAttribute('x1', 140); alt1.setAttribute('y1', 50); alt1.setAttribute('x2', 140); alt1.setAttribute('y2', 170); }
    if (foot1) { foot1.setAttribute('cx', 140); foot1.setAttribute('cy', 170); }
    if (ext) ext.style.opacity = '0';
    if (desc) desc.textContent = 'Right-Angled Triangle: The two legs are themselves altitudes! Altitude from A coincides with leg AB, and altitude from C coincides with leg BC.';
    if (btnR) btnR.className = 'px-2.5 py-1 text-xs font-semibold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40';
    if (btnA) btnA.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (btnO) btnO.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
  } else if (type === 'obtuse') {
    if (poly) poly.setAttribute('points', '160,170 380,170 80,50');
    if (vA) { vA.setAttribute('cx', 80); vA.setAttribute('cy', 50); }
    if (txtA) { txtA.setAttribute('x', 80); txtA.setAttribute('y', 38); }
    if (vB) { vB.setAttribute('cx', 160); vB.setAttribute('cy', 170); }
    if (txtB) { txtB.setAttribute('x', 175); txtB.setAttribute('y', 185); }
    if (alt1) { alt1.setAttribute('x1', 80); alt1.setAttribute('y1', 50); alt1.setAttribute('x2', 80); alt1.setAttribute('y2', 170); }
    if (foot1) { foot1.setAttribute('cx', 80); foot1.setAttribute('cy', 170); }
    if (ext) { ext.setAttribute('x1', 60); ext.setAttribute('x2', 160); ext.style.opacity = '1'; }
    if (desc) desc.textContent = 'Obtuse Triangle: Angle B > 90°. The altitude from acute vertex A falls OUTSIDE the triangle onto the extended dashed base line!';
    if (btnO) btnO.className = 'px-2.5 py-1 text-xs font-semibold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40';
    if (btnA) btnA.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (btnR) btnR.className = 'px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600';
  }
}

// 13. Orthocenter Concurrency
function updateOrthocenter(xVal) {
  const x = parseFloat(xVal);
  const poly = document.getElementById('orthoPoly');
  const vA = document.getElementById('orthoVA');
  const altA = document.getElementById('orthoAltA');
  const ptH = document.getElementById('orthoPtH');
  const lblH = document.getElementById('orthoLblH');
  const badge = document.getElementById('orthoPositionBadge');

  if (vA) vA.setAttribute('cx', x);
  if (poly) poly.setAttribute('points', `120,170 380,170 ${x},50`);

  // Altitude from A: x = xVal, goes to base y = 170
  // Slope of AC = (170 - 50) / (380 - x) = 120 / (380 - x)
  // Altitude from B(120, 170): slope = -(380 - x) / 120
  // Equation: y - 170 = m * (x_H - 120) ==> y_H = 170 - ((380 - x) / 120) * (x - 120)
  const yH = 170 - ((380 - x) * (x - 120)) / 120;

  if (altA) { altA.setAttribute('x1', x); altA.setAttribute('x2', x); altA.setAttribute('y2', Math.max(yH, 170)); }
  if (ptH) { ptH.setAttribute('cx', x); ptH.setAttribute('cy', yH); }
  if (lblH) { lblH.setAttribute('x', x + 15); lblH.setAttribute('y', yH + 4); }

  if (x > 130 && x < 370) {
    if (badge) { badge.textContent = 'Orthocenter INSIDE Triangle (Acute)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-cyan-500/20 text-cyan-300 rounded border border-cyan-500/40'; }
  } else if (Math.abs(x - 120) <= 10) {
    if (badge) { badge.textContent = 'Orthocenter ON Vertex B (Right Angle 90°)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
  } else {
    if (badge) { badge.textContent = 'Orthocenter OUTSIDE Triangle (Obtuse)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40'; }
  }
}

// 14. Classification by Sides
function setSideFamily(fam) {
  const poly = document.getElementById('sideFamPoly');
  const axes = document.getElementById('sideSymAxes');
  const lbl1 = document.getElementById('sideLbl1');
  const lbl2 = document.getElementById('sideLbl2');
  const lbl3 = document.getElementById('sideLbl3');
  const info = document.getElementById('sideFamInfo');

  const bE = document.getElementById('btnFamEqui');
  const bI = document.getElementById('btnFamIso');
  const bS = document.getElementById('btnFamScal');

  if (fam === 'equi') {
    if (poly) poly.setAttribute('points', '160,180 340,180 250,24.1');
    if (axes) axes.style.opacity = '1';
    if (lbl1) lbl1.textContent = '18 cm';
    if (lbl2) lbl2.textContent = '18 cm';
    if (lbl3) lbl3.textContent = '18 cm';
    if (info) info.innerHTML = '<span class="text-cyan-300 font-bold">Equilateral Triangle</span><span>Lines of Symmetry: <strong>3</strong> | Angles: <strong>60°, 60°, 60°</strong></span>';
    if (bE) bE.className = 'px-2 py-0.5 text-xs bg-cyan-500/20 text-cyan-300 rounded border border-cyan-500/40';
    if (bI) bI.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (bS) bS.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
  } else if (fam === 'iso') {
    if (poly) poly.setAttribute('points', '170,180 330,180 250,50');
    if (axes) axes.innerHTML = '<line x1="250" y1="20" x2="250" y2="190" stroke="#f43f5e" stroke-dasharray="4 3" stroke-width="1.5" />';
    if (lbl1) lbl1.textContent = '16 cm';
    if (lbl2) lbl2.textContent = '15 cm';
    if (lbl3) lbl3.textContent = '15 cm';
    if (info) info.innerHTML = '<span class="text-amber-300 font-bold">Isosceles Triangle</span><span>Lines of Symmetry: <strong>1</strong> (central vertical) | 2 Equal Base Angles</span>';
    if (bI) bI.className = 'px-2 py-0.5 text-xs bg-amber-500/20 text-amber-300 rounded border border-amber-500/40';
    if (bE) bE.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (bS) bS.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
  } else if (fam === 'scall') {
    if (poly) poly.setAttribute('points', '130,180 370,180 220,60');
    if (axes) axes.innerHTML = '';
    if (lbl1) lbl1.textContent = '24 cm (Longest)';
    if (lbl2) lbl2.textContent = '15 cm';
    if (lbl3) lbl3.textContent = '19 cm';
    if (info) info.innerHTML = '<span class="text-rose-300 font-bold">Scalene Triangle</span><span>Lines of Symmetry: <strong>0</strong> | All 3 sides and angles unequal</span>';
    if (bS) bS.className = 'px-2 py-0.5 text-xs bg-rose-500/20 text-rose-300 rounded border border-rose-500/40';
    if (bE) bE.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
    if (bI) bI.className = 'px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600';
  }
}

// 15. Classification by Angles
function setAngleClass(cls) {
  const poly = document.getElementById('angPoly');
  const tagA = document.getElementById('angTagA');
  const tagB = document.getElementById('angTagB');
  const tagC = document.getElementById('angTagC');
  const hyp = document.getElementById('angHypotenuse');
  const hypLbl = document.getElementById('angHypLbl');
  const badge = document.getElementById('angClassBadge');

  if (cls === 'acute') {
    if (poly) poly.setAttribute('points', '130,170 370,170 250,45');
    if (tagA) { tagA.setAttribute('x', 250); tagA.setAttribute('y', 32); tagA.textContent = '∠A = 60°'; }
    if (tagB) { tagB.setAttribute('x', 100); tagB.setAttribute('y', 175); tagB.textContent = '∠B = 60°'; }
    if (tagC) { tagC.setAttribute('x', 380); tagC.setAttribute('y', 175); tagC.textContent = '∠C = 60°'; }
    if (hyp) hyp.style.opacity = '0';
    if (hypLbl) hypLbl.style.opacity = '0';
    if (badge) { badge.textContent = 'Acute-Angled Triangle (All 3 < 90°)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40'; }
  } else if (cls === 'right') {
    if (poly) poly.setAttribute('points', '130,170 370,170 130,45');
    if (tagA) { tagA.setAttribute('x', 130); tagA.setAttribute('y', 32); tagA.textContent = '∠A = 50°'; }
    if (tagB) { tagB.setAttribute('x', 95); tagB.setAttribute('y', 185); tagB.textContent = '∠B = 90° (Right)'; }
    if (tagC) { tagC.setAttribute('x', 380); tagC.setAttribute('y', 175); tagC.textContent = '∠C = 40°'; }
    if (hyp) { hyp.setAttribute('x1', 130); hyp.setAttribute('y1', 45); hyp.setAttribute('x2', 370); hyp.setAttribute('y2', 170); hyp.style.opacity = '1'; }
    if (hypLbl) { hypLbl.setAttribute('x', 240); hypLbl.setAttribute('y', 95); hypLbl.style.opacity = '1'; }
    if (badge) { badge.textContent = 'Right-Angled Triangle (One 90° + Hypotenuse)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40'; }
  } else if (cls === 'obtuse') {
    if (poly) poly.setAttribute('points', '180,170 400,170 100,65');
    if (tagA) { tagA.setAttribute('x', 95); tagA.setAttribute('y', 52); tagA.textContent = '∠A = 35°'; }
    if (tagB) { tagB.setAttribute('x', 195); tagB.setAttribute('y', 185); tagB.textContent = '∠B = 120° (Obtuse)'; }
    if (tagC) { tagC.setAttribute('x', 410); tagC.setAttribute('y', 175); tagC.textContent = '∠C = 25°'; }
    if (hyp) hyp.style.opacity = '0';
    if (hypLbl) hypLbl.style.opacity = '0';
    if (badge) { badge.textContent = 'Obtuse-Angled Triangle (One > 90°)'; badge.className = 'px-2 py-0.5 text-xs font-bold bg-rose-500/20 text-rose-300 rounded border border-rose-500/40'; }
  }
}

// 16. Master Matrix & Sulba Sutra Heritage
function setSulbaTriple(a, b, c) {
  const desc = document.getElementById('sulbaDesc');
  const a2 = a * a;
  const b2 = b * b;
  const c2 = c * c;
  if (desc) desc.textContent = `Triple ${a}:${b}:${c} → ${a2} + ${b2} = ${c2} (Exact 90° Right Angle)`;
}
"""

with open('.agents/class7_math_tale_of_three_intersecting_lines_js.py', 'w') as f:
    f.write(f"SIMULATORS_JS = {repr(js_content)}\n")

print("Created .agents/class7_math_tale_of_three_intersecting_lines_js.py successfully!")

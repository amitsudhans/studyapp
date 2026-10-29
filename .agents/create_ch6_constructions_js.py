# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 7 Mathematics: Chapter 6 - Constructions and Tilings
JavaScript Simulator Engine
"""

SIMULATORS_JS = r"""
// Master Simulator Dispatcher for Chapter 6: Constructions and Tilings
function initSimulatorForSlide(slideId, container) {
  if (!container) return;
  switch (slideId) {
    case 1: initVesicaPiscisSim(container); break;
    case 2: initPerpBisectorSim(container); break;
    case 3: initErect90PointSim(container); break;
    case 4: initSulbaSutraAltarSim(container); break;
    case 5: initAngleBisectorStudioSim(container); break;
    case 6: initMandalaRosetteGeneratorSim(container); break;
    case 7: initAngleCopierSim(container); break;
    case 8: initParallelLineTransversalSim(container); break;
    case 9: initHistoricArchArchitectSim(container); break;
    case 10: initEquilateral60ConstructorSim(container); break;
    case 11: initAngleHierarchyShatkonaSim(container); break;
    case 12: initRegularHexagonStepperSim(container); break;
    case 13: initTangramTessellationSim(container); break;
    case 14: initDominoGridTilingSim(container); break;
    case 15: initMutilatedChessboardSim(container); break;
    case 16: initMasterTessellationStudioSim(container); break;
  }
}

// -------------------------------------------------------------
// 1. Vesica Piscis (Symmetric Eye) Simulator
// -------------------------------------------------------------
function initVesicaPiscisSim(container) {
  const svg = container.querySelector('#vesicaSvg');
  const slider = container.querySelector('#vesicaRadiusSlider');
  const radVal = container.querySelector('#vesicaRadiusVal');
  if (!svg || !slider) return;

  function render() {
    const r = parseInt(slider.value, 10);
    if (radVal) radVal.textContent = r + ' px';
    const cx = 250, cy = 150;
    const ax = cx - r / 2, ay = cy;
    const bx = cx + r / 2, by = cy;
    const h = Math.sqrt(Math.max(0, r * r - (r / 2) * (r / 2)));
    const xx = cx, xy = cy - h;
    const yx = cx, yy = cy + h;

    svg.innerHTML = `
      <defs>
        <clipPath id="circleClipA"><circle cx="${ax}" cy="${ay}" r="${r}" /></clipPath>
      </defs>
      <!-- Grid & Axes -->
      <line x1="20" y1="${cy}" x2="480" y2="${cy}" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5" />
      <line x1="${cx}" y1="20" x2="${cx}" y2="280" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5" />
      
      <!-- Intersecting Lens Region (Eye) -->
      <circle cx="${bx}" cy="${by}" r="${r}" fill="#f59e0b" fill-opacity="0.25" clip-path="url(#circleClipA)" />
      
      <!-- Two Circles -->
      <circle cx="${ax}" cy="${ay}" r="${r}" fill="none" stroke="#38bdf8" stroke-width="2" />
      <circle cx="${bx}" cy="${by}" r="${r}" fill="none" stroke="#34d399" stroke-width="2" />
      
      <!-- Rhombus AXBY -->
      <polygon points="${ax},${ay} ${xx},${xy} ${bx},${by} ${yx},${yy}" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5 3" />
      
      <!-- Horizontal Segment AB -->
      <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f8fafc" stroke-width="3" />
      
      <!-- Vertical Chord XY (Perpendicular Bisector) -->
      <line x1="${xx}" y1="${xy}" x2="${yx}" y2="${yy}" stroke="#ec4899" stroke-width="2.5" />
      
      <!-- Right Angle Square -->
      <rect x="${cx}" y="${cy - 12}" width="12" height="12" fill="none" stroke="#ec4899" stroke-width="1.5" />
      
      <!-- Points -->
      <circle cx="${ax}" cy="${ay}" r="5" fill="#38bdf8" />
      <text x="${ax - 15}" y="${ay + 18}" fill="#38bdf8" font-size="12" font-weight="bold">A</text>
      
      <circle cx="${bx}" cy="${by}" r="5" fill="#34d399" />
      <text x="${bx + 8}" y="${ay + 18}" fill="#34d399" font-size="12" font-weight="bold">B</text>
      
      <circle cx="${xx}" cy="${xy}" r="5" fill="#ec4899" />
      <text x="${xx + 8}" y="${xy - 6}" fill="#ec4899" font-size="12" font-weight="bold">X</text>
      
      <circle cx="${yx}" cy="${yy}" r="5" fill="#ec4899" />
      <text x="${yx + 8}" y="${yy + 16}" fill="#ec4899" font-size="12" font-weight="bold">Y</text>
      
      <!-- Center M -->
      <circle cx="${cx}" cy="${cy}" r="3" fill="#fbbf24" />
      <text x="${cx + 6}" y="${cy - 6}" fill="#fbbf24" font-size="10">M</text>
      
      <!-- Labels -->
      <text x="30" y="35" fill="#94a3b8" font-size="11">Radius r = ${r}px</text>
      <text x="30" y="55" fill="#38bdf8" font-size="11">Circle A: (x - ${ax.toFixed(0)})² + y² = r²</text>
      <text x="30" y="75" fill="#34d399" font-size="11">Circle B: (x - ${bx.toFixed(0)})² + y² = r²</text>
      <text x="350" y="35" fill="#fbbf24" font-size="11" font-weight="bold">AX = AY = BX = BY = r</text>
      <text x="350" y="55" fill="#ec4899" font-size="11" font-weight="bold">XY ⊥ AB (90.0°)</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 2. Perpendicular Bisector Stepper Simulator
// -------------------------------------------------------------
function initPerpBisectorSim(container) {
  const svg = container.querySelector('#perpBisectorSvg');
  const prevBtn = container.querySelector('#perpPrevBtn');
  const nextBtn = container.querySelector('#perpNextBtn');
  const resetBtn = container.querySelector('#perpResetBtn');
  const stepBadge = container.querySelector('#perpStepBadge');
  const stepDesc = container.querySelector('#perpStepDesc');
  if (!svg) return;

  let currentStep = 1;
  const ax = 150, ay = 150;
  const bx = 350, by = 150;
  const mx = 250, my = 150;
  const r = 135;
  const h = Math.sqrt(r * r - 100 * 100);
  const px = 250, py = 150 - h;
  const qx = 250, qy = 150 + h;

  const descriptions = [
    "Step 1: Baseline line segment AB is placed on the plane (length = 200px).",
    "Step 2: Compass radius set to r = 135px (> AB/2 = 100px). Arcs drawn above & below from endpoint A.",
    "Step 3: With the exact same radius r = 135px, intersecting arcs drawn from endpoint B to locate points P and Q.",
    "Step 4: Draw straight line PQ. It intersects AB at midpoint M at an exact 90° right angle (AM = MB = 100px)!"
  ];

  function render() {
    if (stepBadge) stepBadge.textContent = `Step ${currentStep} of 4`;
    if (stepDesc) stepDesc.textContent = descriptions[currentStep - 1];

    let content = `
      <!-- Segment AB -->
      <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#38bdf8" stroke-width="3" />
      <circle cx="${ax}" cy="${ay}" r="5" fill="#38bdf8" />
      <text x="${ax - 18}" y="${ay + 5}" fill="#38bdf8" font-size="14" font-weight="bold">A</text>
      <circle cx="${bx}" cy="${by}" r="5" fill="#38bdf8" />
      <text x="${bx + 10}" y="${ay + 5}" fill="#38bdf8" font-size="14" font-weight="bold">B</text>
    `;

    if (currentStep >= 2) {
      content += `
        <!-- Arcs from A -->
        <path d="M ${ax + 80} ${ay - 110} A ${r} ${r} 0 0 1 ${ax + 120} ${ay - 70}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2" />
        <path d="M ${ax + 80} ${ay + 110} A ${r} ${r} 0 0 0 ${ax + 120} ${ay + 70}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2" />
        <text x="110" y="50" fill="#f59e0b" font-size="11">Radius r = 135px (> 100px)</text>
      `;
    }

    if (currentStep >= 3) {
      content += `
        <!-- Arcs from B -->
        <path d="M ${bx - 80} ${by - 110} A ${r} ${r} 0 0 0 ${bx - 120} ${by - 70}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2" />
        <path d="M ${bx - 80} ${by + 110} A ${r} ${r} 0 0 1 ${bx - 120} ${by + 70}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2" />
        
        <!-- Intersection Points P and Q -->
        <circle cx="${px}" cy="${py}" r="5" fill="#ec4899" />
        <text x="${px + 8}" y="${py - 5}" fill="#ec4899" font-size="13" font-weight="bold">P</text>
        <circle cx="${qx}" cy="${qy}" r="5" fill="#ec4899" />
        <text x="${qx + 8}" y="${qy + 15}" fill="#ec4899" font-size="13" font-weight="bold">Q</text>
        
        <!-- Equidistant chords AP, BP -->
        <line x1="${ax}" y1="${ay}" x2="${px}" y2="${py}" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3" />
        <line x1="${bx}" y1="${by}" x2="${px}" y2="${py}" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3" />
      `;
    }

    if (currentStep >= 4) {
      content += `
        <!-- Perpendicular Bisector Line PQ -->
        <line x1="${px}" y1="20" x2="${qx}" y2="280" stroke="#ec4899" stroke-width="2.5" />
        <circle cx="${mx}" cy="${my}" r="4" fill="#fbbf24" />
        <text x="${mx - 18}" y="${my - 8}" fill="#fbbf24" font-size="12" font-weight="bold">M</text>
        
        <!-- Right Angle Square at M -->
        <rect x="${mx}" y="${my - 14}" width="14" height="14" fill="none" stroke="#ec4899" stroke-width="1.5" />
        <text x="300" y="270" fill="#34d399" font-size="12" font-weight="bold">AM = MB = 100px | ∠AMP = 90°</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { if (currentStep < 4) { currentStep++; render(); } });
  if (prevBtn) prevBtn.addEventListener('click', () => { if (currentStep > 1) { currentStep--; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { currentStep = 1; render(); });
  render();
}

// -------------------------------------------------------------
// 3. Erect 90° Angle at Point P Simulator
// -------------------------------------------------------------
function initErect90PointSim(container) {
  const svg = container.querySelector('#erect90Svg');
  const posSpan = container.querySelector('#erectPPos');
  if (!svg) return;

  let px = 250;
  const lineY = 180;
  const r1 = 60;
  const r2 = 85;

  function render() {
    if (posSpan) posSpan.textContent = `x = ${px} px`;
    const ax = px - r1, ay = lineY;
    const bx = px + r1, by = lineY;
    const h = Math.sqrt(r2 * r2 - r1 * r1);
    const cx = px, cy = lineY - h;

    svg.innerHTML = `
      <!-- Baseline Line L -->
      <line x1="30" y1="${lineY}" x2="470" y2="${lineY}" stroke="#64748b" stroke-width="2.5" />
      <text x="475" y="${lineY + 4}" fill="#64748b" font-size="13" font-weight="bold">L</text>
      
      <!-- Point P -->
      <circle cx="${px}" cy="${lineY}" r="6" fill="#f59e0b" />
      <text x="${px - 5}" y="${lineY + 22}" fill="#f59e0b" font-size="13" font-weight="bold">P</text>
      
      <!-- Arcs from P marking A and B -->
      <path d="M ${ax} ${lineY - 20} A ${r1} ${r1} 0 0 1 ${ax} ${lineY + 20}" fill="none" stroke="#38bdf8" stroke-width="2" />
      <path d="M ${bx} ${lineY - 20} A ${r1} ${r1} 0 0 0 ${bx} ${lineY + 20}" fill="none" stroke="#38bdf8" stroke-width="2" />
      
      <!-- Points A and B -->
      <circle cx="${ax}" cy="${ay}" r="4" fill="#38bdf8" />
      <text x="${ax - 12}" y="${ay + 18}" fill="#38bdf8" font-size="11">A</text>
      <circle cx="${bx}" cy="${by}" r="4" fill="#38bdf8" />
      <text x="${bx + 6}" y="${by + 18}" fill="#38bdf8" font-size="11">B</text>
      
      <!-- Equidistant Arcs from A and B intersecting at C -->
      <path d="M ${cx - 25} ${cy - 10} A ${r2} ${r2} 0 0 1 ${cx + 25} ${cy + 15}" fill="none" stroke="#10b981" stroke-width="2" />
      <path d="M ${cx + 25} ${cy - 10} A ${r2} ${r2} 0 0 0 ${cx - 25} ${cy + 15}" fill="none" stroke="#10b981" stroke-width="2" />
      
      <!-- Point C -->
      <circle cx="${cx}" cy="${cy}" r="5" fill="#10b981" />
      <text x="${cx + 8}" y="${cy}" fill="#10b981" font-size="12" font-weight="bold">C</text>
      
      <!-- Dashed construction lines AC and BC -->
      <line x1="${ax}" y1="${ay}" x2="${cx}" y2="${cy}" stroke="#475569" stroke-dasharray="3 3" stroke-width="1.5" />
      <line x1="${bx}" y1="${by}" x2="${cx}" y2="${cy}" stroke="#475569" stroke-dasharray="3 3" stroke-width="1.5" />
      
      <!-- Erected Perpendicular Ray PC -->
      <line x1="${px}" y1="${lineY}" x2="${cx}" y2="30" stroke="#ec4899" stroke-width="3" />
      
      <!-- Right Angle Indicator -->
      <rect x="${px}" y="${lineY - 14}" width="14" height="14" fill="none" stroke="#ec4899" stroke-width="1.5" />
      <circle cx="${px + 7}" cy="${lineY - 7}" r="1.5" fill="#ec4899" />
      
      <!-- Labels -->
      <text x="30" y="40" fill="#94a3b8" font-size="11">Step 1: Equal arcs r₁ = 60px ⟹ AP = PB</text>
      <text x="30" y="60" fill="#94a3b8" font-size="11">Step 2: Equal arcs r₂ = 85px from A and B ⟹ AC = BC</text>
      <text x="30" y="80" fill="#ec4899" font-size="12" font-weight="bold">Result: Ray PC ⊥ Line L at point P (90.0°)</text>
      <text x="${px - 60}" y="270" fill="#f59e0b" font-size="10">Drag horizontally to move point P</text>
    `;
  }

  function handleMove(e) {
    const rect = svg.getBoundingClientRect();
    const clientX = e.clientX || (e.touches && e.touches[0].clientX);
    if (!clientX) return;
    const scale = 500 / rect.width;
    let newX = (clientX - rect.left) * scale;
    px = Math.max(120, Math.min(380, newX));
    render();
  }

  let isDragging = false;
  svg.addEventListener('mousedown', (e) => { isDragging = true; handleMove(e); });
  window.addEventListener('mousemove', (e) => { if (isDragging) handleMove(e); });
  window.addEventListener('mouseup', () => { isDragging = false; });
  svg.addEventListener('touchstart', (e) => { isDragging = true; handleMove(e); }, { passive: true });
  window.addEventListener('touchmove', (e) => { if (isDragging) handleMove(e); }, { passive: true });
  window.addEventListener('touchend', () => { isDragging = false; });

  render();
}

// -------------------------------------------------------------
// 4. Kātyāyana Śulba-Sūtra Altar Simulator
// -------------------------------------------------------------
function initSulbaSutraAltarSim(container) {
  const svg = container.querySelector('#sulbaSvg');
  const btn1 = container.querySelector('#sulbaAltarBtn1');
  const btn2 = container.querySelector('#sulbaAltarBtn2');
  const animBtn = container.querySelector('#sulbaAnimateBtn');
  if (!svg) return;

  let altarType = 'square'; // 'square' or 'circle'
  let animProgress = 1.0;

  function render() {
    const cx = 250, cy = 150;
    const praciLen = 180;
    const ax = cx - praciLen, ay = cy;
    const bx = cx + praciLen, by = cy;

    let content = `
      <!-- Earth ground background -->
      <rect x="0" y="0" width="500" height="300" fill="#0f172a" />
      
      <!-- Prācī (East-West Cardinal Axis) -->
      <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 3" />
      <text x="${ax - 35}" y="${ay + 5}" fill="#f59e0b" font-size="12" font-weight="bold">West</text>
      <text x="${bx + 10}" y="${by + 5}" fill="#f59e0b" font-size="12" font-weight="bold">East (Prācī)</text>
      
      <!-- North-South Meridian -->
      <line x1="${cx}" y1="30" x2="${cx}" y2="270" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 4" />
      <text x="${cx + 6}" y="45" fill="#38bdf8" font-size="11">North</text>
      <text x="${cx + 6}" y="265" fill="#38bdf8" font-size="11">South</text>
      
      <!-- Solar Shadow Gnomon Peg at Center -->
      <circle cx="${cx}" cy="${cy}" r="6" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
      <text x="${cx + 8}" y="${cy - 8}" fill="#fbbf24" font-size="10">Śanku (Gnomon)</text>
    `;

    if (altarType === 'square') {
      const s = 110;
      content += `
        <!-- Āhavanīya Square Altar Outline -->
        <rect x="${cx - s/2}" y="${cy - s/2}" width="${s}" height="${s}" fill="#b45309" fill-opacity="0.3" stroke="#f59e0b" stroke-width="3" rx="4" />
        
        <!-- Cord Diagonals -->
        <line x1="${cx - s/2}" y1="${cy - s/2}" x2="${cx + s/2}" y2="${cy + s/2}" stroke="#fbbf24" stroke-dasharray="3 3" stroke-width="1.5" />
        <line x1="${cx + s/2}" y1="${cy - s/2}" x2="${cx - s/2}" y2="${cy + s/2}" stroke="#fbbf24" stroke-dasharray="3 3" stroke-width="1.5" />
        
        <!-- Sacred Flame -->
        <circle cx="${cx}" cy="${cy}" r="14" fill="#ef4444" fill-opacity="0.6" />
        <circle cx="${cx}" cy="${cy - 4}" r="8" fill="#f59e0b" />
        <text x="${cx - 50}" y="105" fill="#fde68a" font-size="12" font-weight="bold">Āhavanīya Altar (Square)</text>
        <text x="30" y="280" fill="#94a3b8" font-size="11">Rope Knot Method: Equal diagonals guarantee 90° right corners</text>
      `;
    } else {
      const r = 65;
      content += `
        <!-- Gārhapatya Circular Altar -->
        <circle cx="${cx}" cy="${cy}" r="${r}" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="3" />
        <circle cx="${cx}" cy="${cy}" r="14" fill="#ef4444" fill-opacity="0.6" />
        <circle cx="${cx}" cy="${cy - 4}" r="8" fill="#f59e0b" />
        <text x="${cx - 55}" y="105" fill="#a7f3d0" font-size="12" font-weight="bold">Gārhapatya Altar (Circular)</text>
        <text x="30" y="280" fill="#94a3b8" font-size="11">Equal Area Transformation: Area(Circle) = Area(Square) via Baudhayana Sulba</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (btn1) btn1.addEventListener('click', () => { altarType = 'square'; btn1.className = "px-3 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition"; btn2.className = "px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition"; render(); });
  if (btn2) btn2.addEventListener('click', () => { altarType = 'circle'; btn2.className = "px-3 py-1.5 rounded-lg bg-emerald-600 text-xs font-semibold text-white transition"; btn1.className = "px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition"; render(); });
  if (animBtn) animBtn.addEventListener('click', () => { render(); });
  render();
}

// -------------------------------------------------------------
// 5. Angle Bisector Studio Simulator
// -------------------------------------------------------------
function initAngleBisectorStudioSim(container) {
  const svg = container.querySelector('#bisectorSvg');
  const slider = container.querySelector('#bisectorAngleSlider');
  const angleVal = container.querySelector('#bisectorAngleVal');
  const halfVal = container.querySelector('#bisectorHalfVal');
  if (!svg || !slider) return;

  function render() {
    const deg = parseFloat(slider.value);
    const halfDeg = (deg / 2).toFixed(1);
    if (angleVal) angleVal.textContent = deg + '°';
    if (halfVal) halfVal.textContent = `∠AOC = ∠BOC = ${halfDeg}°`;

    const ox = 100, oy = 230;
    const len = 190;
    const r1 = 120;
    const r2 = 90;

    const radTotal = (deg * Math.PI) / 180;
    const radHalf = (deg / 2 * Math.PI) / 180;

    // Point A along horizontal
    const ax = ox + len, ay = oy;
    // Point B along angle deg
    const bx = ox + len * Math.cos(radTotal), by = oy - len * Math.sin(radTotal);
    // Point P on OA at r1
    const px = ox + r1, py = oy;
    // Point Q on OB at r1
    const qx = ox + r1 * Math.cos(radTotal), qy = oy - r1 * Math.sin(radTotal);

    // Bisector ray C
    const cx = ox + len * Math.cos(radHalf), cy = oy - len * Math.sin(radHalf);

    svg.innerHTML = `
      <!-- Base ray OA -->
      <line x1="${ox}" y1="${oy}" x2="${ax + 20}" y2="${ay}" stroke="#94a3b8" stroke-width="2.5" />
      <text x="${ax + 25}" y="${ay + 4}" fill="#94a3b8" font-size="12" font-weight="bold">A</text>
      
      <!-- Ray OB -->
      <line x1="${ox}" y1="${oy}" x2="${bx}" y2="${by}" stroke="#94a3b8" stroke-width="2.5" />
      <text x="${bx + 8}" y="${by - 6}" fill="#94a3b8" font-size="12" font-weight="bold">B</text>
      
      <!-- Vertex O -->
      <circle cx="${ox}" cy="${oy}" r="5" fill="#f8fafc" />
      <text x="${ox - 18}" y="${oy + 5}" fill="#f8fafc" font-size="13" font-weight="bold">O</text>
      
      <!-- Primary Arc from O cutting OA and OB at P and Q -->
      <path d="M ${px} ${py} A ${r1} ${r1} 0 0 0 ${qx} ${qy}" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="4 2" />
      <circle cx="${px}" cy="${py}" r="4" fill="#a855f7" />
      <text x="${px - 4}" y="${py + 18}" fill="#a855f7" font-size="11">P</text>
      <circle cx="${qx}" cy="${qy}" r="4" fill="#a855f7" />
      <text x="${qx - 14}" y="${qy - 6}" fill="#a855f7" font-size="11">Q</text>
      
      <!-- Intersecting Arcs from P and Q -->
      <circle cx="${cx * 0.85}" cy="${cy * 0.85 + (oy - cy)*0.15}" r="3" fill="#10b981" />
      
      <!-- Bisector Ray OC -->
      <line x1="${ox}" y1="${oy}" x2="${cx}" y2="${cy}" stroke="#10b981" stroke-width="3" />
      <text x="${cx + 8}" y="${cy}" fill="#10b981" font-size="13" font-weight="bold">C (Bisector)</text>
      
      <!-- Shaded angle sectors -->
      <path d="M ${ox} ${oy} L ${ox + 45} ${oy} A 45 45 0 0 0 ${ox + 45 * Math.cos(radHalf)} ${oy - 45 * Math.sin(radHalf)} Z" fill="#3b82f6" fill-opacity="0.3" />
      <path d="M ${ox} ${oy} L ${ox + 45 * Math.cos(radHalf)} ${oy - 45 * Math.sin(radHalf)} A 45 45 0 0 0 ${ox + 45 * Math.cos(radTotal)} ${oy - 45 * Math.sin(radTotal)} Z" fill="#10b981" fill-opacity="0.3" />
      
      <text x="${ox + 55}" y="${oy - 12}" fill="#60a5fa" font-size="11">${halfDeg}°</text>
      <text x="${ox + 45 * Math.cos(radHalf) + 10}" y="${oy - 45 * Math.sin(radHalf) - 8}" fill="#34d399" font-size="11">${halfDeg}°</text>
      
      <!-- SSS Congruence Label -->
      <text x="280" y="40" fill="#c084fc" font-size="12" font-weight="bold">△OPC ≅ △OQC by SSS</text>
      <text x="280" y="60" fill="#94a3b8" font-size="11">OP = OQ = r₁</text>
      <text x="280" y="78" fill="#94a3b8" font-size="11">PC = QC = r₂ | OC is common</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 6. Mandala & Rosette Generator Simulator
// -------------------------------------------------------------
function initMandalaRosetteGeneratorSim(container) {
  const svg = container.querySelector('#mandalaSvg');
  const petalBtns = container.querySelectorAll('.mandalaPetalBtn');
  const guidesToggle = container.querySelector('#mandalaGuidesToggle');
  if (!svg) return;

  let petalCount = 8;
  let showGuides = true;

  function render() {
    const cx = 250, cy = 150;
    const rOuter = 100;
    const rInner = 50;

    let content = `
      <!-- Background Circle -->
      <circle cx="${cx}" cy="${cy}" r="${rOuter}" fill="#0f172a" stroke="#475569" stroke-width="1.5" />
      <circle cx="${cx}" cy="${cy}" r="${rInner}" fill="none" stroke="#334155" stroke-dasharray="3 3" />
    `;

    // Radial axis lines
    for (let i = 0; i < petalCount; i++) {
      const angle = (i * 2 * Math.PI) / petalCount;
      const x2 = cx + rOuter * Math.cos(angle);
      const y2 = cy + rOuter * Math.sin(angle);
      if (showGuides) {
        content += `<line x1="${cx}" y1="${cy}" x2="${x2}" y2="${y2}" stroke="#334155" stroke-dasharray="2 2" stroke-width="1" />`;
      }
    }

    // Intersecting circular petal arcs
    for (let i = 0; i < petalCount; i++) {
      const a1 = (i * 2 * Math.PI) / petalCount;
      const a2 = ((i + 1) * 2 * Math.PI) / petalCount;
      const aMid = (a1 + a2) / 2;

      const p1x = cx + rOuter * Math.cos(a1);
      const p1y = cy + rOuter * Math.sin(a1);
      const p2x = cx + rOuter * Math.cos(a2);
      const p2y = cy + rOuter * Math.sin(a2);
      const tipX = cx + (rOuter + 25) * Math.cos(aMid);
      const tipY = cy + (rOuter + 25) * Math.sin(aMid);

      // Petal filled shape
      content += `
        <path d="M ${cx} ${cy} Q ${p1x} ${p1y} ${tipX} ${tipY} Q ${p2x} ${p2y} ${cx} ${cy}" 
              fill="#f43f5e" fill-opacity="0.35" stroke="#fb7185" stroke-width="2" />
        <circle cx="${tipX}" cy="${tipY}" r="3" fill="#fde047" />
      `;
    }

    content += `
      <!-- Center Star Hub -->
      <circle cx="${cx}" cy="${cy}" r="12" fill="#fde047" stroke="#b45309" stroke-width="2" />
      <text x="30" y="35" fill="#fda4af" font-size="12" font-weight="bold">${petalCount}-Petalled Mandala Rosette</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Central Angle Partition: 360° / ${petalCount} = ${(360 / petalCount).toFixed(1)}° per sector</text>
    `;

    svg.innerHTML = content;
  }

  petalBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      petalBtns.forEach(b => b.className = "mandalaPetalBtn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-xs font-bold text-slate-200 transition");
      btn.className = "mandalaPetalBtn px-2.5 py-1 rounded-lg bg-rose-600 text-xs font-bold text-white transition";
      petalCount = parseInt(btn.dataset.petals, 10);
      render();
    });
  });

  if (guidesToggle) {
    guidesToggle.addEventListener('change', (e) => {
      showGuides = e.target.checked;
      render();
    });
  }

  render();
}

// -------------------------------------------------------------
// 7. Angle Copier Simulator
// -------------------------------------------------------------
function initAngleCopierSim(container) {
  const svg = container.querySelector('#angleCopierSvg');
  const stepBtn = container.querySelector('#copyAngleStepBtn');
  const resetBtn = container.querySelector('#copyAngleResetBtn');
  if (!svg) return;

  let step = 0;
  const deg = 52;
  const rad = (deg * Math.PI) / 180;
  const R = 80;

  // Left side: original angle at (110, 200)
  const o1x = 110, o1y = 200;
  const x1x = o1x + R, x1y = o1y;
  const y1x = o1x + R * Math.cos(rad), y1y = o1y - R * Math.sin(rad);
  const chordD = Math.sqrt((x1x - y1x)**2 + (x1y - y1y)**2);

  // Right side: copied angle at (320, 200)
  const o2x = 320, o2y = 200;
  const x2x = o2x + R, x2y = o2y;
  const y2x = o2x + R * Math.cos(rad), y2y = o2y - R * Math.sin(rad);

  function render() {
    let content = `
      <!-- Divider -->
      <line x1="240" y1="20" x2="240" y2="280" stroke="#334155" stroke-dasharray="4 4" />
      
      <!-- LEFT: Original Angle -->
      <text x="30" y="35" fill="#38bdf8" font-size="12" font-weight="bold">Original Angle ∠O = 52°</text>
      <line x1="${o1x}" y1="${o1y}" x2="${o1x + 110}" y2="${o1y}" stroke="#94a3b8" stroke-width="2.5" />
      <line x1="${o1x}" y1="${o1y}" x2="${o1x + 110 * Math.cos(rad)}" y2="${o1y - 110 * Math.sin(rad)}" stroke="#94a3b8" stroke-width="2.5" />
      <circle cx="${o1x}" cy="${o1y}" r="4" fill="#38bdf8" />
      <text x="${o1x - 18}" y="${o1y + 4}" fill="#38bdf8" font-size="12">O</text>
      
      <!-- Arc of radius R on Original -->
      <path d="M ${x1x} ${x1y} A ${R} ${R} 0 0 0 ${y1x} ${y1y}" fill="none" stroke="#f59e0b" stroke-width="2" />
      <circle cx="${x1x}" cy="${x1y}" r="4" fill="#f59e0b" />
      <text x="${x1x + 4}" y="${x1y + 16}" fill="#f59e0b" font-size="10">X</text>
      <circle cx="${y1x}" cy="${y1y}" r="4" fill="#f59e0b" />
      <text x="${y1x - 8}" y="${y1y - 8}" fill="#f59e0b" font-size="10">Y</text>
      
      <!-- Chord XY -->
      <line x1="${x1x}" y1="${x1y}" x2="${y1x}" y2="${y1y}" stroke="#ec4899" stroke-dasharray="3 3" stroke-width="1.5" />
      <text x="75" y="145" fill="#ec4899" font-size="10">Chord d</text>
      
      <!-- RIGHT: Copied Angle Destination -->
      <text x="270" y="35" fill="#2dd4bf" font-size="12" font-weight="bold">Copied Angle at Vertex P</text>
      <line x1="${o2x}" y1="${o2y}" x2="${o2x + 110}" y2="${o2y}" stroke="#94a3b8" stroke-width="2.5" />
      <circle cx="${o2x}" cy="${o2y}" r="4" fill="#2dd4bf" />
      <text x="${o2x - 18}" y="${o2y + 4}" fill="#2dd4bf" font-size="12">P</text>
    `;

    if (step >= 1) {
      content += `
        <!-- Step 1: Arc of radius R at P -->
        <path d="M ${x2x} ${x2y} A ${R} ${R} 0 0 0 ${o2x + R * Math.cos(rad * 1.3)} ${o2y - R * Math.sin(rad * 1.3)}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2" />
        <circle cx="${x2x}" cy="${x2y}" r="4" fill="#f59e0b" />
        <text x="${x2x + 4}" y="${x2y + 16}" fill="#f59e0b" font-size="10">X'</text>
        <text x="270" y="60" fill="#f59e0b" font-size="11">1. Sweep arc of radius R from P</text>
      `;
    }

    if (step >= 2) {
      content += `
        <!-- Step 2: Arc of chord width d from X' -->
        <path d="M ${y2x - 15} ${y2y + 15} A ${chordD} ${chordD} 0 0 1 ${y2x + 15} ${y2y - 15}" fill="none" stroke="#ec4899" stroke-width="2" stroke-dasharray="4 2" />
        <circle cx="${y2x}" cy="${y2y}" r="5" fill="#ec4899" />
        <text x="${y2x + 8}" y="${y2y - 6}" fill="#ec4899" font-size="11" font-weight="bold">Y'</text>
        <text x="270" y="80" fill="#ec4899" font-size="11">2. Strike chord distance d from X'</text>
      `;
    }

    if (step >= 3) {
      content += `
        <!-- Step 3: Draw Ray PY' -->
        <line x1="${o2x}" y1="${o2y}" x2="${o2x + 110 * Math.cos(rad)}" y2="${o2y - 110 * Math.sin(rad)}" stroke="#2dd4bf" stroke-width="3" />
        <text x="270" y="100" fill="#2dd4bf" font-size="12" font-weight="bold">3. Ray PY' drawn: ∠P = 52.0°</text>
        <text x="270" y="260" fill="#34d399" font-size="12" font-weight="bold">△OXY ≅ △PX'Y' (SSS Congruence)</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (step < 3) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 8. Parallel Line via Transversal Simulator
// -------------------------------------------------------------
function initParallelLineTransversalSim(container) {
  const svg = container.querySelector('#parallelSvg');
  const slider = container.querySelector('#parallelAngleSlider');
  const angleVal = container.querySelector('#parallelAngleVal');
  const matchSpan = container.querySelector('#parallelAngleMatch');
  if (!svg || !slider) return;

  let py = 120;
  const lineY = 220;
  const qx = 160;

  function render() {
    const deg = parseFloat(slider.value);
    if (angleVal) angleVal.textContent = deg + '°';
    if (matchSpan) matchSpan.textContent = deg.toFixed(1) + '°';

    const rad = (deg * Math.PI) / 180;
    // P position
    const px = qx + (lineY - py) / Math.tan(rad);

    svg.innerHTML = `
      <!-- Line L (Base) -->
      <line x1="30" y1="${lineY}" x2="470" y2="${lineY}" stroke="#64748b" stroke-width="2.5" />
      <text x="475" y="${lineY + 4}" fill="#64748b" font-size="13" font-weight="bold">L</text>
      
      <!-- Line m (Parallel through P) -->
      <line x1="30" y1="${py}" x2="470" y2="${py}" stroke="#38bdf8" stroke-width="2.5" />
      <text x="475" y="${py + 4}" fill="#38bdf8" font-size="13" font-weight="bold">m</text>
      
      <!-- Transversal Line through Q and P -->
      <line x1="${qx - 40}" y1="${lineY + 40 * Math.tan(rad)}" x2="${px + 50}" y2="${py - 50 * Math.tan(rad)}" stroke="#f59e0b" stroke-width="2" />
      
      <!-- Point Q on Line L -->
      <circle cx="${qx}" cy="${lineY}" r="5" fill="#f59e0b" />
      <text x="${qx - 18}" y="${lineY + 18}" fill="#f59e0b" font-size="12" font-weight="bold">Q</text>
      
      <!-- Point P on Line m -->
      <circle cx="${px}" cy="${py}" r="6" fill="#ec4899" />
      <text x="${px - 18}" y="${py - 8}" fill="#ec4899" font-size="13" font-weight="bold">P</text>
      
      <!-- Corresponding Angle Arc at Q -->
      <path d="M ${qx + 35} ${lineY} A 35 35 0 0 0 ${qx + 35 * Math.cos(rad)} ${lineY - 35 * Math.sin(rad)}" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2" />
      <text x="${qx + 40}" y="${lineY - 10}" fill="#10b981" font-size="11" font-weight="bold">∠1 = ${deg}°</text>
      
      <!-- Corresponding Angle Arc at P -->
      <path d="M ${px + 35} ${py} A 35 35 0 0 0 ${px + 35 * Math.cos(rad)} ${py - 35 * Math.sin(rad)}" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2" />
      <text x="${px + 40}" y="${py - 10}" fill="#10b981" font-size="11" font-weight="bold">∠2 = ${deg}°</text>
      
      <!-- Labels -->
      <text x="30" y="35" fill="#38bdf8" font-size="12" font-weight="bold">Corresponding Angles Axiom: ∠1 = ∠2 ⟹ Line m ∥ Line L</text>
      <text x="30" y="55" fill="#94a3b8" font-size="11">Perpendicular separation d = ${(lineY - py)} px (strictly invariant across all points)</text>
      <text x="30" y="275" fill="#ec4899" font-size="11">Drag point P up/down to test parallel invariance</text>
    `;
  }

  function handleDrag(e) {
    const rect = svg.getBoundingClientRect();
    const clientY = e.clientY || (e.touches && e.touches[0].clientY);
    if (!clientY) return;
    const scale = 300 / rect.height;
    let newY = (clientY - rect.top) * scale;
    py = Math.max(60, Math.min(180, newY));
    render();
  }

  let dragging = false;
  svg.addEventListener('mousedown', (e) => { dragging = true; handleDrag(e); });
  window.addEventListener('mousemove', (e) => { if (dragging) handleDrag(e); });
  window.addEventListener('mouseup', () => { dragging = false; });
  svg.addEventListener('touchstart', (e) => { dragging = true; handleDrag(e); }, { passive: true });
  window.addEventListener('touchmove', (e) => { if (dragging) handleDrag(e); }, { passive: true });
  window.addEventListener('touchend', () => { dragging = false; });

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 9. Historic Arch Architect Simulator
// -------------------------------------------------------------
function initHistoricArchArchitectSim(container) {
  const svg = container.querySelector('#archSvg');
  const typeBtns = container.querySelectorAll('.archTypeBtn');
  const centersToggle = container.querySelector('#archCentersToggle');
  if (!svg) return;

  let currentType = 'trefoil';
  let showCenters = true;

  function render() {
    const cx = 250, baseY = 240;
    const span = 180;
    const ax = cx - span / 2, ay = baseY;
    const bx = cx + span / 2, by = baseY;

    let content = `
      <!-- Base ground & pillars -->
      <rect x="0" y="${baseY}" width="500" height="60" fill="#0f172a" stroke="#334155" />
      <rect x="${ax - 20}" y="120" width="20" height="${baseY - 120}" fill="#1e293b" stroke="#475569" />
      <rect x="${bx}" y="120" width="20" height="${baseY - 120}" fill="#1e293b" stroke="#475569" />
      <circle cx="${ax}" cy="120" r="4" fill="#fbbf24" />
      <circle cx="${bx}" cy="120" r="4" fill="#fbbf24" />
    `;

    if (currentType === 'pointed') {
      const springY = 120;
      content += `
        <!-- Equilateral Pointed Arch -->
        <!-- Arc from A to Apex C (radius = span) -->
        <path d="M ${ax} ${springY} A ${span} ${span} 0 0 1 ${cx} ${springY - span * Math.sqrt(3)/2}" fill="none" stroke="#f59e0b" stroke-width="4" />
        <path d="M ${bx} ${springY} A ${span} ${span} 0 0 0 ${cx} ${springY - span * Math.sqrt(3)/2}" fill="none" stroke="#f59e0b" stroke-width="4" />
        <circle cx="${cx}" cy="${springY - span * Math.sqrt(3)/2}" r="5" fill="#ef4444" />
        <text x="${cx - 15}" y="${springY - span * Math.sqrt(3)/2 - 10}" fill="#ef4444" font-size="12" font-weight="bold">Apex C</text>
      `;

      if (showCenters) {
        content += `
          <!-- Equilateral construction triangle -->
          <polygon points="${ax},${springY} ${bx},${springY} ${cx},${springY - span * Math.sqrt(3)/2}" fill="none" stroke="#38bdf8" stroke-dasharray="4 4" stroke-width="1.5" />
          <text x="${ax - 30}" y="${springY + 15}" fill="#38bdf8" font-size="10">Center 1</text>
          <text x="${bx + 8}" y="${springY + 15}" fill="#38bdf8" font-size="10">Center 2</text>
          <text x="30" y="35" fill="#f59e0b" font-size="12" font-weight="bold">Equilateral Pointed Arch: Radius = Span AB (${span}px)</text>
        `;
      }
    } else if (currentType === 'trefoil') {
      const r = 50;
      const c1x = cx - r, c1y = 150;
      const c2x = cx + r, c2y = 150;
      const c3x = cx, c3y = 150 - r * Math.sqrt(3);

      content += `
        <!-- Trefoil 3-lobed Arch (Diwan-i-Aam) -->
        <path d="M ${ax} 120 Q ${ax} 100 ${cx - r - 20} 100" stroke="#f59e0b" stroke-width="3" fill="none" />
        <circle cx="${c1x}" cy="${c1y}" r="${r}" fill="#fbbf24" fill-opacity="0.1" stroke="#f59e0b" stroke-width="3" stroke-dasharray="1 1" />
        <circle cx="${c2x}" cy="${c2y}" r="${r}" fill="#fbbf24" fill-opacity="0.1" stroke="#f59e0b" stroke-width="3" stroke-dasharray="1 1" />
        <circle cx="${c3x}" cy="${c3y}" r="${r}" fill="#fbbf24" fill-opacity="0.1" stroke="#f59e0b" stroke-width="3" stroke-dasharray="1 1" />
      `;

      if (showCenters) {
        content += `
          <polygon points="${c1x},${c1y} ${c2x},${c2y} ${c3x},${c3y}" fill="none" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="3 3" />
          <circle cx="${c1x}" cy="${c1y}" r="4" fill="#ec4899" />
          <circle cx="${c2x}" cy="${c2y}" r="4" fill="#ec4899" />
          <circle cx="${c3x}" cy="${c3y}" r="4" fill="#ec4899" />
          <text x="30" y="35" fill="#f59e0b" font-size="12" font-weight="bold">Trefoil Cusped Arch: 3 Centers on Equilateral Triangle</text>
          <text x="30" y="55" fill="#94a3b8" font-size="11">Characteristic of Red Fort (Diwan-i-Aam) and Mughal arcades</text>
        `;
      }
    } else {
      // Ogee arch
      content += `
        <!-- Ogee Arch (S-curve reverse arcs) -->
        <path d="M ${ax} 120 C ${ax} 80, ${cx - 50} 80, ${cx - 30} 50 C ${cx - 15} 30, ${cx} 25, ${cx} 20" fill="none" stroke="#f59e0b" stroke-width="3.5" />
        <path d="M ${bx} 120 C ${bx} 80, ${cx + 50} 80, ${cx + 30} 50 C ${cx + 15} 30, ${cx} 25, ${cx} 20" fill="none" stroke="#f59e0b" stroke-width="3.5" />
        <text x="30" y="35" fill="#f59e0b" font-size="12" font-weight="bold">Ogee Arch: Convex lower arc + Concave upper arc</text>
      `;
    }

    svg.innerHTML = content;
  }

  typeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      typeBtns.forEach(b => b.className = "archTypeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition");
      btn.className = "archTypeBtn px-3 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition";
      currentType = btn.dataset.type;
      render();
    });
  });

  if (centersToggle) {
    centersToggle.addEventListener('change', (e) => {
      showCenters = e.target.checked;
      render();
    });
  }

  render();
}

// -------------------------------------------------------------
// 10. Equilateral 60° Constructor Simulator
// -------------------------------------------------------------
function initEquilateral60ConstructorSim(container) {
  const svg = container.querySelector('#equilateral60Svg');
  const stepBtn = container.querySelector('#eq60StepBtn');
  const resetBtn = container.querySelector('#eq60ResetBtn');
  if (!svg) return;

  let step = 0;
  const ox = 175, oy = 210;
  const r = 150;
  const ax = ox + r, ay = oy;
  const bx = ox + r * Math.cos(Math.PI / 3), by = oy - r * Math.sin(Math.PI / 3);

  function render() {
    let content = `
      <!-- Base Ray from O -->
      <line x1="${ox}" y1="${oy}" x2="${ax + 40}" y2="${ay}" stroke="#94a3b8" stroke-width="2.5" />
      <circle cx="${ox}" cy="${oy}" r="5" fill="#f8fafc" />
      <text x="${ox - 18}" y="${oy + 5}" fill="#f8fafc" font-size="13" font-weight="bold">O</text>
    `;

    if (step >= 1) {
      content += `
        <!-- Arc from O of radius r cutting ray at A -->
        <path d="M ${ax} ${ay} A ${r} ${r} 0 0 0 ${bx + 20} ${by - 20}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2" />
        <circle cx="${ax}" cy="${ay}" r="5" fill="#f59e0b" />
        <text x="${ax + 8}" y="${ay + 18}" fill="#f59e0b" font-size="13" font-weight="bold">A (r = 150px)</text>
        <text x="30" y="35" fill="#f59e0b" font-size="11">1. Sweep arc of radius r from O to mark A</text>
      `;
    }

    if (step >= 2) {
      content += `
        <!-- Arc from A of same radius r intersecting at B -->
        <path d="M ${bx - 20} ${by + 20} A ${r} ${r} 0 0 1 ${bx + 20} ${by - 20}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2" />
        <circle cx="${bx}" cy="${by}" r="5" fill="#10b981" />
        <text x="${bx + 8}" y="${by - 8}" fill="#10b981" font-size="13" font-weight="bold">B</text>
        <text x="30" y="55" fill="#10b981" font-size="11">2. Strike same radius r from A to locate B</text>
      `;
    }

    if (step >= 3) {
      content += `
        <!-- Ray OB and Segment AB -->
        <line x1="${ox}" y1="${oy}" x2="${bx}" y2="${by}" stroke="#ec4899" stroke-width="3" />
        <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3 3" />
        
        <!-- Equilateral triangle fill -->
        <polygon points="${ox},${oy} ${ax},${ay} ${bx},${by}" fill="#10b981" fill-opacity="0.15" />
        
        <!-- Angle Arcs -->
        <path d="M ${ox + 35} ${oy} A 35 35 0 0 0 ${ox + 35 * Math.cos(Math.PI/3)} ${oy - 35 * Math.sin(Math.PI/3)}" fill="#ec4899" fill-opacity="0.3" stroke="#ec4899" stroke-width="2" />
        <text x="${ox + 42}" y="${oy - 12}" fill="#ec4899" font-size="12" font-weight="bold">60.0°</text>
        
        <text x="270" y="35" fill="#10b981" font-size="12" font-weight="bold">OA = AB = OB = r = 150px</text>
        <text x="270" y="55" fill="#94a3b8" font-size="11">△OAB is equilateral ⟹ all angles = 60°</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (step < 3) { step++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { step = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 11. Angle Hierarchy & Shatkona Simulator
// -------------------------------------------------------------
function initAngleHierarchyShatkonaSim(container) {
  const svg = container.querySelector('#shatkonaSvg');
  const angleBtns = container.querySelectorAll('.angleChoiceBtn');
  const starBtn = container.querySelector('#toggleShatkonaStarBtn');
  if (!svg) return;

  let mode = 'angle'; // 'angle' or 'star'
  let currentAngle = 60;

  function render() {
    const cx = 250, cy = 150;
    const r = 100;

    if (mode === 'star') {
      // 6-pointed Shatkona Hexagram
      // Triangle 1 (pointing up)
      const t1_1 = [cx, cy - r];
      const t1_2 = [cx + r * Math.cos(Math.PI / 6), cy + r * Math.sin(Math.PI / 6)];
      const t1_3 = [cx - r * Math.cos(Math.PI / 6), cy + r * Math.sin(Math.PI / 6)];

      // Triangle 2 (pointing down)
      const t2_1 = [cx, cy + r];
      const t2_2 = [cx + r * Math.cos(Math.PI / 6), cy - r * Math.sin(Math.PI / 6)];
      const t2_3 = [cx - r * Math.cos(Math.PI / 6), cy - r * Math.sin(Math.PI / 6)];

      svg.innerHTML = `
        <!-- Circumscribing Circle -->
        <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#475569" stroke-dasharray="3 3" />
        
        <!-- Triangle 1 (Upward: Purusha / Shiva) -->
        <polygon points="${t1_1.join(',')} ${t1_2.join(',')} ${t1_3.join(',')}" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="2.5" />
        
        <!-- Triangle 2 (Downward: Prakriti / Shakti) -->
        <polygon points="${t2_1.join(',')} ${t2_2.join(',')} ${t2_3.join(',')}" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2.5" />
        
        <!-- Central Regular Hexagon -->
        <polygon points="${cx},${cy - r/2} ${cx + r*Math.sqrt(3)/4},${cy - r/4} ${cx + r*Math.sqrt(3)/4},${cy + r/4} ${cx},${cy + r/2} ${cx - r*Math.sqrt(3)/4},${cy + r/4} ${cx - r*Math.sqrt(3)/4},${cy - r/4}" fill="#fbbf24" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2" />
        
        <!-- Center Origin -->
        <circle cx="${cx}" cy="${cy}" r="3" fill="#fbbf24" />
        
        <text x="30" y="35" fill="#c084fc" font-size="13" font-weight="bold">Shatkona (Ancient 6-Pointed Star Hexagram)</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">Constructed from two congruent equilateral triangles rotated by 60°</text>
        <text x="30" y="275" fill="#fbbf24" font-size="11">Core forms a perfect regular hexagon of side r/√3</text>
      `;
    } else {
      // Angle Ray Display
      const ox = 150, oy = 210;
      const len = 170;
      const rad = (currentAngle * Math.PI) / 180;
      const ex = ox + len * Math.cos(rad), ey = oy - len * Math.sin(rad);

      svg.innerHTML = `
        <!-- Base Ray -->
        <line x1="${ox}" y1="${oy}" x2="${ox + len + 30}" y2="${oy}" stroke="#94a3b8" stroke-width="2.5" />
        
        <!-- Angle Ray -->
        <line x1="${ox}" y1="${oy}" x2="${ex}" y2="${ey}" stroke="#c084fc" stroke-width="3" />
        <circle cx="${ox}" cy="${oy}" r="5" fill="#f8fafc" />
        
        <!-- Angle Arc -->
        <path d="M ${ox + 50} ${oy} A 50 50 0 0 0 ${ox + 50 * Math.cos(rad)} ${oy - 50 * Math.sin(rad)}" fill="#a855f7" fill-opacity="0.3" stroke="#a855f7" stroke-width="2" />
        <text x="${ox + 60 * Math.cos(rad/2) + 5}" y="${oy - 60 * Math.sin(rad/2) - 5}" fill="#c084fc" font-size="13" font-weight="bold">${currentAngle}°</text>
        
        <!-- Decomposition Hint -->
        <text x="30" y="35" fill="#c084fc" font-size="13" font-weight="bold">Constructed Angle: ${currentAngle}°</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">Decomposition: ${getAngleDecompText(currentAngle)}</text>
      `;
    }
  }

  function getAngleDecompText(a) {
    if (a === 15) return "Bisect 30° (or bisect 60° twice)";
    if (a === 30) return "Bisect 60° equilateral angle";
    if (a === 45) return "Bisect 90° right angle";
    if (a === 60) return "Equilateral triangle step (side = radius)";
    if (a === 75) return "60° + 15° (bisect interval between 60° and 90°)";
    if (a === 105) return "90° + 15° (or 60° + 45°)";
    return "";
  }

  angleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      mode = 'angle';
      currentAngle = parseInt(btn.dataset.deg, 10);
      render();
    });
  });

  if (starBtn) {
    starBtn.addEventListener('click', () => {
      mode = (mode === 'star') ? 'angle' : 'star';
      render();
    });
  }

  render();
}

// -------------------------------------------------------------
// 12. Regular Hexagon Radius Stepper Simulator
// -------------------------------------------------------------
function initRegularHexagonStepperSim(container) {
  const svg = container.querySelector('#hexagonSvg');
  const stepBtn = container.querySelector('#hexStepBtn');
  const resetBtn = container.querySelector('#hexResetBtn');
  const stepCountSpan = container.querySelector('#hexStepCount');
  const angleSumSpan = container.querySelector('#hexAngleSum');
  if (!svg) return;

  let steps = 0;
  const cx = 250, cy = 150;
  const r = 95;

  function render() {
    if (stepCountSpan) stepCountSpan.textContent = steps;
    if (angleSumSpan) angleSumSpan.textContent = `${steps * 60}°`;

    let content = `
      <!-- Center O -->
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#475569" stroke-dasharray="3 3" />
      <circle cx="${cx}" cy="${cy}" r="4" fill="#38bdf8" />
      <text x="${cx + 6}" y="${cy - 6}" fill="#38bdf8" font-size="11">O</text>
    `;

    // Coordinates of 6 vertices
    const pts = [];
    for (let i = 0; i < 6; i++) {
      const angle = (i * Math.PI) / 3;
      pts.push([cx + r * Math.cos(angle), cy - r * Math.sin(angle)]);
    }

    // Drawn steps
    for (let i = 0; i < steps; i++) {
      const p1 = pts[i];
      const p2 = pts[(i + 1) % 6];
      // Triangle spoke to center
      content += `
        <polygon points="${cx},${cy} ${p1[0]},${p1[1]} ${p2[0]},${p2[1]}" fill="#06b6d4" fill-opacity="0.2" stroke="#22d3ee" stroke-width="2" />
        <circle cx="${p1[0]}" cy="${p1[1]}" r="5" fill="#f59e0b" />
        <text x="${p1[0] + 8}" y="${p1[1] + 4}" fill="#f59e0b" font-size="11" font-weight="bold">P${i+1}</text>
      `;
    }

    if (steps === 6) {
      content += `
        <!-- Full perimeter outline -->
        <polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="none" stroke="#ec4899" stroke-width="3" />
        <text x="30" y="35" fill="#22d3ee" font-size="13" font-weight="bold">Complete Regular Hexagon Inscribed!</text>
        <text x="30" y="55" fill="#94a3b8" font-size="11">6 Equilateral Triangles Meet: 6 × 60° = 360° | Side s = Radius r = ${r}px</text>
      `;
    }

    svg.innerHTML = content;
  }

  if (stepBtn) stepBtn.addEventListener('click', () => { if (steps < 6) { steps++; render(); } });
  if (resetBtn) resetBtn.addEventListener('click', () => { steps = 0; render(); });
  render();
}

// -------------------------------------------------------------
// 13. Tangram Tiling Simulator
// -------------------------------------------------------------
function initTangramTessellationSim(container) {
  const svg = container.querySelector('#tangramSvg');
  const shapeBtns = container.querySelectorAll('.tangramShapeBtn');
  if (!svg) return;

  let currentShape = 'square';

  function render() {
    const cx = 250, cy = 150;

    let content = `
      <text x="30" y="30" fill="#818cf8" font-size="12" font-weight="bold">Tangram Configuration: ${currentShape.toUpperCase()}</text>
      <text x="30" y="50" fill="#94a3b8" font-size="11">Conservation of Area: All 7 pieces strictly sum to 100% area</text>
    `;

    if (currentShape === 'square') {
      const s = 140;
      const x0 = cx - s/2, y0 = cy - s/2;
      content += `
        <!-- 7 pieces assembling a 140x140 square -->
        <!-- Large Triangle 1 -->
        <polygon points="${x0},${y0} ${x0 + s},${y0} ${x0 + s/2},${y0 + s/2}" fill="#3b82f6" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Large Triangle 2 -->
        <polygon points="${x0},${y0} ${x0},${y0 + s} ${x0 + s/2},${y0 + s/2}" fill="#10b981" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Medium Triangle -->
        <polygon points="${x0 + s},${y0} ${x0 + s},${y0 + s} ${x0 + s/2},${y0 + s/2}" fill="#f59e0b" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Small Triangle 1 -->
        <polygon points="${x0 + s/2},${y0 + s/2} ${x0 + s*3/4},${y0 + s*3/4} ${x0 + s/4},${y0 + s*3/4}" fill="#ec4899" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Small Triangle 2 -->
        <polygon points="${x0},${y0 + s} ${x0 + s/4},${y0 + s*3/4} ${x0 + s/2},${y0 + s}" fill="#a855f7" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Square -->
        <polygon points="${x0 + s/2},${y0 + s/2} ${x0 + s*3/4},${y0 + s*3/4} ${x0 + s/2},${y0 + s} ${x0 + s/4},${y0 + s*3/4}" fill="#06b6d4" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
        <!-- Parallelogram -->
        <polygon points="${x0 + s/2},${y0 + s} ${x0 + s},${y0 + s} ${x0 + s*3/4},${y0 + s*3/4} ${x0 + s/4},${y0 + s*3/4}" fill="#eab308" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" />
      `;
    } else if (currentShape === 'candle') {
      content += `
        <!-- Tangram Candle Form -->
        <polygon points="250,40 240,65 260,65" fill="#ef4444" stroke="#1e293b" stroke-width="2" />
        <rect x="235" y="65" width="30" height="90" fill="#3b82f6" stroke="#1e293b" stroke-width="2" />
        <polygon points="210,155 290,155 250,230" fill="#10b981" stroke="#1e293b" stroke-width="2" />
        <polygon points="170,230 330,230 250,260" fill="#f59e0b" stroke="#1e293b" stroke-width="2" />
      `;
    } else {
      // Swan form
      content += `
        <!-- Tangram Swan Form -->
        <polygon points="160,80 180,60 190,85" fill="#ec4899" stroke="#1e293b" stroke-width="2" />
        <polygon points="180,85 240,160 210,180" fill="#3b82f6" stroke="#1e293b" stroke-width="2" />
        <polygon points="240,160 320,160 270,220" fill="#10b981" stroke="#1e293b" stroke-width="2" />
        <polygon points="320,160 360,180 320,200" fill="#f59e0b" stroke="#1e293b" stroke-width="2" />
      `;
    }

    svg.innerHTML = content;
  }

  shapeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      shapeBtns.forEach(b => b.className = "tangramShapeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition");
      btn.className = "tangramShapeBtn px-3 py-1.5 rounded-lg bg-indigo-600 text-xs font-semibold text-white transition";
      currentShape = btn.dataset.shape;
      render();
    });
  });

  render();
}

// -------------------------------------------------------------
// 14. Domino Grid Tiling Simulator
// -------------------------------------------------------------
function initDominoGridTilingSim(container) {
  const svg = container.querySelector('#dominoSvg');
  const rSlider = container.querySelector('#dominoRowsSlider');
  const cSlider = container.querySelector('#dominoColsSlider');
  const rVal = container.querySelector('#dominoRowsVal');
  const cVal = container.querySelector('#dominoColsVal');
  const totalCells = container.querySelector('#dominoTotalCells');
  const statusText = container.querySelector('#dominoStatusText');
  const badge = container.querySelector('#dominoParityBadge');
  if (!svg || !rSlider || !cSlider) return;

  function render() {
    const rows = parseInt(rSlider.value, 10);
    const cols = parseInt(cSlider.value, 10);
    if (rVal) rVal.textContent = rows;
    if (cVal) cVal.textContent = cols;
    const total = rows * cols;
    if (totalCells) totalCells.textContent = `${total} cells (${rows} × ${cols})`;

    const isEven = (total % 2 === 0);
    if (isEven) {
      if (badge) {
        badge.textContent = "Tilable (Area Even)";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
      }
      if (statusText) {
        statusText.textContent = `Possible (${total / 2} dominoes)`;
        statusText.className = "font-bold text-emerald-400 font-mono";
      }
    } else {
      if (badge) {
        badge.textContent = "Impossible (Area Odd)";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
      }
      if (statusText) {
        statusText.textContent = `IMPOSSIBLE! 1 cell left uncovered (${total} = 2k + 1)`;
        statusText.className = "font-bold text-rose-400 font-mono";
      }
    }

    const cellSize = 36;
    const startX = 250 - (cols * cellSize) / 2;
    const startY = 150 - (rows * cellSize) / 2;

    let content = ``;

    // Draw base cells
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const x = startX + c * cellSize;
        const y = startY + r * cellSize;
        content += `<rect x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" fill="#1e293b" stroke="#334155" stroke-width="1.5" />`;
      }
    }

    // Draw dominoes if even
    if (isEven) {
      // If cols is even, place horizontal dominoes
      if (cols % 2 === 0) {
        for (let r = 0; r < rows; r++) {
          for (let c = 0; c < cols; c += 2) {
            const x = startX + c * cellSize;
            const y = startY + r * cellSize;
            const color = ((r + c/2) % 2 === 0) ? '#10b981' : '#3b82f6';
            content += `
              <rect x="${x + 2}" y="${y + 2}" width="${cellSize * 2 - 4}" height="${cellSize - 4}" rx="6" fill="${color}" fill-opacity="0.85" stroke="#f8fafc" stroke-width="1.5" />
              <circle cx="${x + cellSize*0.5}" cy="${y + cellSize*0.5}" r="3" fill="#ffffff" />
              <circle cx="${x + cellSize*1.5}" cy="${y + cellSize*0.5}" r="3" fill="#ffffff" />
            `;
          }
        }
      } else {
        // Rows must be even, place vertical dominoes
        for (let r = 0; r < rows; r += 2) {
          for (let c = 0; c < cols; c++) {
            const x = startX + c * cellSize;
            const y = startY + r * cellSize;
            const color = ((r/2 + c) % 2 === 0) ? '#10b981' : '#a855f7';
            content += `
              <rect x="${x + 2}" y="${y + 2}" width="${cellSize - 4}" height="${cellSize * 2 - 4}" rx="6" fill="${color}" fill-opacity="0.85" stroke="#f8fafc" stroke-width="1.5" />
              <circle cx="${x + cellSize*0.5}" cy="${y + cellSize*0.5}" r="3" fill="#ffffff" />
              <circle cx="${x + cellSize*0.5}" cy="${y + cellSize*1.5}" r="3" fill="#ffffff" />
            `;
          }
        }
      }
    } else {
      // Odd area: Place as many dominoes as possible and mark the remainder red
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols - 1; c += 2) {
          const x = startX + c * cellSize;
          const y = startY + r * cellSize;
          content += `
            <rect x="${x + 2}" y="${y + 2}" width="${cellSize * 2 - 4}" height="${cellSize - 4}" rx="6" fill="#64748b" fill-opacity="0.6" stroke="#475569" stroke-width="1.5" />
          `;
        }
      }
      // Rightmost column: pairs of vertical dominoes except last cell
      for (let r = 0; r < rows - 1; r += 2) {
        const x = startX + (cols - 1) * cellSize;
        const y = startY + r * cellSize;
        content += `
          <rect x="${x + 2}" y="${y + 2}" width="${cellSize - 4}" height="${cellSize * 2 - 4}" rx="6" fill="#64748b" fill-opacity="0.6" stroke="#475569" stroke-width="1.5" />
        `;
      }
      // The single orphan cell
      const orphanX = startX + (cols - 1) * cellSize;
      const orphanY = startY + (rows - 1) * cellSize;
      content += `
        <rect x="${orphanX + 2}" y="${orphanY + 2}" width="${cellSize - 4}" height="${cellSize - 4}" fill="#ef4444" fill-opacity="0.8" stroke="#f87171" stroke-width="2" />
        <text x="${orphanX + cellSize/2 - 5}" y="${orphanY + cellSize/2 + 5}" fill="#ffffff" font-size="14" font-weight="bold">✕</text>
      `;
    }

    svg.innerHTML = content;
  }

  rSlider.addEventListener('input', render);
  cSlider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 15. Mutilated Chessboard Simulator
// -------------------------------------------------------------
function initMutilatedChessboardSim(container) {
  const svg = container.querySelector('#chessboardSvg');
  const toggleBtn = container.querySelector('#toggleMutilatedBtn');
  const wCount = container.querySelector('#whiteCellCount');
  const bCount = container.querySelector('#blackCellCount');
  const verdict = container.querySelector('#parityVerdict');
  const badge = container.querySelector('#chessboardBadge');
  if (!svg || !toggleBtn) return;

  let isMutilated = false;

  function render() {
    const size = 30;
    const startX = 250 - 4 * size;
    const startY = 150 - 4 * size;

    if (isMutilated) {
      if (wCount) wCount.textContent = "30";
      if (bCount) bCount.textContent = "32";
      if (verdict) {
        verdict.textContent = "IMPOSSIBLE (30 White ≠ 32 Black)";
        verdict.className = "text-rose-400 font-bold";
      }
      if (badge) {
        badge.textContent = "Mutilated: 62 Squares";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
      }
      toggleBtn.textContent = "↺ Restore 8×8 Full Board";
    } else {
      if (wCount) wCount.textContent = "32";
      if (bCount) bCount.textContent = "32";
      if (verdict) {
        verdict.textContent = "Balanced (32W = 32B)";
        verdict.className = "text-emerald-400 font-bold";
      }
      if (badge) {
        badge.textContent = "Full 8×8 Board (64 Squares)";
        badge.className = "px-2 py-0.5 rounded text-[11px] font-bold bg-slate-700 text-slate-300 border border-slate-600";
      }
      toggleBtn.textContent = "✂ Cut Diagonally Opposite Corners";
    }

    let content = ``;

    for (let r = 0; r < 8; r++) {
      for (let c = 0; c < 8; c++) {
        // Check if mutilated corner (top-left 0,0 and bottom-right 7,7)
        if (isMutilated && ((r === 0 && c === 0) || (r === 7 && c === 7))) {
          const x = startX + c * size;
          const y = startY + r * size;
          content += `
            <rect x="${x}" y="${y}" width="${size}" height="${size}" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 2" />
            <line x1="${x+4}" y1="${y+4}" x2="${x+size-4}" y2="${y+size-4}" stroke="#ef4444" stroke-width="2" />
            <line x1="${x+size-4}" y1="${y+4}" x2="${x+4}" y2="${y+size-4}" stroke="#ef4444" stroke-width="2" />
          `;
          continue;
        }

        const isWhite = (r + c) % 2 === 0;
        const color = isWhite ? '#f8fafc' : '#334155';
        const x = startX + c * size;
        const y = startY + r * size;
        content += `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="${color}" stroke="#1e293b" stroke-width="1" />`;
      }
    }

    svg.innerHTML = content;
  }

  toggleBtn.addEventListener('click', () => {
    isMutilated = !isMutilated;
    render();
  });

  render();
}

// -------------------------------------------------------------
// 16. Master Tessellation Studio Simulator
// -------------------------------------------------------------
function initMasterTessellationStudioSim(container) {
  const svg = container.querySelector('#tessellationSvg');
  const typeBtns = container.querySelectorAll('.tessTypeBtn');
  const readout = container.querySelector('#tessAngleReadout');
  if (!svg) return;

  let currentType = 'hex';

  function render() {
    const cx = 250, cy = 150;

    let content = ``;

    if (currentType === 'hex') {
      if (readout) readout.textContent = "3 × 120° = 360° (0° gap) | Honeycomb Optimal (Min Perimeter)";
      const r = 32;
      const dx = r * Math.sqrt(3);
      const dy = r * 1.5;

      for (let row = -3; row <= 3; row++) {
        for (let col = -3; col <= 3; col++) {
          const x = cx + col * dx + (row % 2 !== 0 ? dx / 2 : 0);
          const y = cy + row * dy;
          if (x < 30 || x > 470 || y < 20 || y > 280) continue;

          const pts = [];
          for (let i = 0; i < 6; i++) {
            const a = (i * Math.PI) / 3;
            pts.push([x + r * Math.cos(a), y + r * Math.sin(a)]);
          }
          content += `<polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="#f59e0b" fill-opacity="0.25" stroke="#fbbf24" stroke-width="1.5" />`;
        }
      }
      // Highlight central vertex
      content += `
        <circle cx="${cx}" cy="${cy}" r="5" fill="#ef4444" />
        <text x="${cx + 8}" y="${cy - 8}" fill="#ef4444" font-size="12" font-weight="bold">Vertex: 3 Hexagons Meet (120° × 3 = 360°)</text>
      `;
    } else if (currentType === 'square') {
      if (readout) readout.textContent = "4 × 90° = 360° (0° gap) | Standard Grid Tessellation";
      const s = 45;
      for (let x = cx - 4 * s; x <= cx + 3 * s; x += s) {
        for (let y = cy - 3 * s; y <= cy + 2 * s; y += s) {
          if (x < 30 || x + s > 470 || y < 20 || y + s > 280) continue;
          content += `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#3b82f6" fill-opacity="0.25" stroke="#60a5fa" stroke-width="1.5" />`;
        }
      }
      content += `
        <circle cx="${cx}" cy="${cy}" r="5" fill="#ef4444" />
        <text x="${cx + 8}" y="${cy - 8}" fill="#ef4444" font-size="12" font-weight="bold">Vertex: 4 Squares Meet (90° × 4 = 360°)</text>
      `;
    } else if (currentType === 'triangle') {
      if (readout) readout.textContent = "6 × 60° = 360° (0° gap) | Triangular Isometric Tessellation";
      const s = 55;
      const h = s * Math.sqrt(3) / 2;

      for (let row = -3; row <= 3; row++) {
        for (let col = -4; col <= 4; col++) {
          const x = cx + col * s + (row % 2 !== 0 ? s / 2 : 0);
          const y = cy + row * h;
          if (x < 20 || x > 480 || y < 20 || y > 280) continue;

          // Upward triangle
          content += `<polygon points="${x},${y} ${x + s},${y} ${x + s/2},${y - h}" fill="#10b981" fill-opacity="0.2" stroke="#34d399" stroke-width="1.5" />`;
          // Downward triangle
          content += `<polygon points="${x},${y} ${x + s},${y} ${x + s/2},${y + h}" fill="#059669" fill-opacity="0.2" stroke="#34d399" stroke-width="1.5" />`;
        }
      }
      content += `
        <circle cx="${cx}" cy="${cy}" r="5" fill="#ef4444" />
        <text x="${cx + 8}" y="${cy - 8}" fill="#ef4444" font-size="12" font-weight="bold">Vertex: 6 Triangles Meet (60° × 6 = 360°)</text>
      `;
    } else {
      // Regular Pentagons (Fail!)
      if (readout) readout.textContent = "3 × 108° = 324° (Leaves 36° GAP!) | Pentagons CANNOT Tile Alone";
      const r = 55;
      // Draw 3 regular pentagons sharing central vertex cx, cy
      for (let p = 0; p < 3; p++) {
        const startAngle = (p * 108 * Math.PI) / 180;
        const pts = [];
        for (let i = 0; i < 5; i++) {
          const a = startAngle + (i * 72 * Math.PI) / 180;
          pts.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]);
        }
        content += `<polygon points="${pts.map(pt => pt.join(',')).join(' ')}" fill="#ef4444" fill-opacity="0.3" stroke="#f87171" stroke-width="2" />`;
      }
      // Highlight the 36° gap
      content += `
        <circle cx="${cx}" cy="${cy}" r="6" fill="#fde047" />
        <path d="M ${cx} ${cy} L ${cx + 70 * Math.cos(324 * Math.PI / 180)} ${cy + 70 * Math.sin(324 * Math.PI / 180)} A 70 70 0 0 1 ${cx + 70} ${cy} Z" fill="#facc15" fill-opacity="0.5" stroke="#fde047" stroke-width="2" stroke-dasharray="3 3" />
        <text x="${cx + 45}" y="${cy + 25}" fill="#fde047" font-size="13" font-weight="bold">36° GAP!</text>
        <text x="30" y="35" fill="#f87171" font-size="13" font-weight="bold">Regular Pentagons Fail: 3 × 108° = 324° ≠ 360°</text>
      `;
    }

    svg.innerHTML = content;
  }

  typeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      typeBtns.forEach(b => b.className = "tessTypeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition");
      if (btn.dataset.type === 'pentagon') {
        btn.className = "tessTypeBtn px-2.5 py-1.5 rounded-lg bg-rose-600 text-xs font-semibold text-white transition";
      } else {
        btn.className = "tessTypeBtn px-2.5 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition";
      }
      currentType = btn.dataset.type;
      render();
    });
  });

  render();
}
"""

if __name__ == "__main__":
    with open(".agents/class7_math_constructions_js.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Mathematics Chapter 6: Constructions and Tilings JS Engine"""\n\n')
        f.write("SIMULATORS_JS = " + repr(SIMULATORS_JS) + "\n")
    print("Generated .agents/class7_math_constructions_js.py successfully.")


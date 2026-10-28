# -*- coding: utf-8 -*-
"""
Helper to write .agents/class7_math_parallel_intersecting_lines_sims.py
"""

sims_code = r'''# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 7 Mathematics - Chapter 5: Parallel and Intersecting Lines
Simulators 1 to 16
"""

SIMULATORS_JS = r"""
    // ========================================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 5 Parallel & Intersecting Lines)
    // ========================================================

    // Slide 1: Intersecting Lines & Scissor Angles
    function simIntersectingLinesScissors() {
      simHeaderTitle.textContent = "Intersecting Lines: Vertically Opposite Angles & Scissor Effect";
      let theta = 50; // angle in degrees

      function render() {
        const rad = (theta * Math.PI) / 180;
        const oppTheta = 180 - theta;
        const L = 160;

        // Line 1: along horizontal axis
        const x1 = 270 - L, y1 = 165;
        const x2 = 270 + L, y2 = 165;

        // Line 2: tilted at theta
        const dx = L * Math.cos(rad);
        const dy = L * Math.sin(rad);
        const x3 = 270 - dx, y3 = 165 + dy;
        const x4 = 270 + dx, y4 = 165 - dy;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <radialGradient id="crossGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
                <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
              </radialGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="35" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">
              Intersection Point O &nbsp;|&nbsp; Acute Angle = ${theta}° &nbsp;|&nbsp; Obtuse Angle = ${oppTheta}°
            </text>

            <!-- Center glow -->
            <circle cx="270" cy="165" r="80" fill="url(#crossGlow)"/>

            <!-- Line 1 (Horizontal AB) -->
            <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#94a3b8" stroke-width="3.5" stroke-linecap="round"/>
            <text x="${x1 - 15}" y="${y1 + 5}" fill="#cbd5e1" font-size="12" font-weight="800">A</text>
            <text x="${x2 + 10}" y="${y2 + 5}" fill="#cbd5e1" font-size="12" font-weight="800">B</text>

            <!-- Line 2 (Tilted CD) -->
            <line x1="${x3}" y1="${y3}" x2="${x4}" y2="${y4}" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round"/>
            <text x="${x3 - 10}" y="${y3 + 15}" fill="#38bdf8" font-size="12" font-weight="800">C</text>
            <text x="${x4 + 10}" y="${y4 - 5}" fill="#38bdf8" font-size="12" font-weight="800">D</text>

            <!-- Intersection Point O -->
            <circle cx="270" cy="165" r="5" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
            <text x="260" y="155" fill="#f8fafc" font-size="11" font-weight="800">O</text>

            <!-- Angle Arcs & Labels -->
            <!-- Right Acute Angle (theta) -->
            <path d="M 320 165 A 50 50 0 0 0 ${270 + 50 * Math.cos(rad)} ${165 - 50 * Math.sin(rad)}" fill="none" stroke="#10b981" stroke-width="3"/>
            <text x="335" y="150" fill="#34d399" font-size="13" font-weight="900">∠1 = ${theta}°</text>

            <!-- Left Acute Angle (theta - vertically opposite to ∠1) -->
            <path d="M 220 165 A 50 50 0 0 0 ${270 - 50 * Math.cos(rad)} ${165 + 50 * Math.sin(rad)}" fill="none" stroke="#10b981" stroke-width="3"/>
            <text x="180" y="195" fill="#34d399" font-size="13" font-weight="900">∠3 = ${theta}°</text>

            <!-- Top Obtuse Angle (180 - theta) -->
            <text x="270" y="105" fill="#fbbf24" font-size="14" font-weight="900" text-anchor="middle">∠2 = ${oppTheta}°</text>

            <!-- Bottom Obtuse Angle (180 - theta) -->
            <text x="270" y="235" fill="#fbbf24" font-size="14" font-weight="900" text-anchor="middle">∠4 = ${oppTheta}°</text>

            <!-- Bottom Insight Card -->
            <rect x="40" y="252" width="460" height="68" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="272" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">
              Vertically Opposite Angles are EQUAL: ∠1 = ∠3 = ${theta}° &nbsp;|&nbsp; ∠2 = ∠4 = ${oppTheta}°
            </text>
            <text x="270" y="292" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Adjacent Angles Form a Linear Pair: ${theta}° + ${oppTheta}° = 180° (Straight Line)
            </text>
            <text x="270" y="308" fill="#94a3b8" font-size="10" text-anchor="middle">
              Drag the slider below to watch the scissor angles update simultaneously!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.6rem; align-items:center;">
          <div style="display:flex; gap:0.4rem; flex-wrap:wrap; justify-content:center;">
            <button class="sim-btn ${theta === 30 ? 'active' : ''}" data-val="30">30°</button>
            <button class="sim-btn ${theta === 45 ? 'active' : ''}" data-val="45">45°</button>
            <button class="sim-btn ${theta === 60 ? 'active' : ''}" data-val="60">60°</button>
            <button class="sim-btn ${theta === 90 ? 'active' : ''}" data-val="90">90° (Perpendicular)</button>
            <button class="sim-btn ${theta === 120 ? 'active' : ''}" data-val="120">120°</button>
          </div>
          <div style="display:flex; align-items:center; gap:0.8rem; color:#94a3b8; font-size:0.85rem;">
            <span>Rotate Angle (θ):</span>
            <input type="range" id="thetaSlider" min="20" max="160" value="${theta}" style="width:200px; accent-color:#38bdf8; cursor:pointer;">
            <span id="thetaVal" style="color:#38bdf8; font-weight:800; min-width:35px;">${theta}°</span>
          </div>
        </div>
      `;

      simControls.querySelectorAll('button[data-val]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          theta = parseInt(e.target.getAttribute('data-val'));
          simControls.querySelector('#thetaSlider').value = theta;
          simControls.querySelector('#thetaVal').textContent = `${theta}°`;
          simControls.querySelectorAll('button[data-val]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      const slider = simControls.querySelector('#thetaSlider');
      slider.addEventListener('input', (e) => {
        theta = parseInt(e.target.value);
        simControls.querySelector('#thetaVal').textContent = `${theta}°`;
        simControls.querySelectorAll('button[data-val]').forEach(b => b.classList.remove('active'));
        render();
      });

      render();
    }

    // Slide 2: Linear Pair Balance
    function simLinearPairSlider() {
      simHeaderTitle.textContent = "Linear Pair Explorer: Straight Line Angle Split (180°)";
      let x = 65;

      function render() {
        const y = 180 - x;
        const rad = (x * Math.PI) / 180;
        const rayLen = 130;
        const rayX = 270 - rayLen * Math.cos(rad);
        const rayY = 200 - rayLen * Math.sin(rad);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="15" width="460" height="40" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="40" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              Linear Pair Theorem: ∠AOC + ∠BOC = ${x}° + ${y}° = 180°
            </text>

            <!-- Baseline Straight Line AB -->
            <line x1="90" y1="200" x2="450" y2="200" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>
            <circle cx="90" cy="200" r="4" fill="#94a3b8"/>
            <circle cx="450" cy="200" r="4" fill="#94a3b8"/>
            <text x="75" y="205" fill="#cbd5e1" font-size="13" font-weight="800">A</text>
            <text x="460" y="205" fill="#cbd5e1" font-size="13" font-weight="800">B</text>

            <!-- Vertex O -->
            <circle cx="270" cy="200" r="6" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
            <text x="268" y="222" fill="#f8fafc" font-size="12" font-weight="900" text-anchor="middle">O</text>

            <!-- Splitting Ray OC -->
            <line x1="270" y1="200" x2="${rayX}" y2="${rayY}" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
            <circle cx="${rayX}" cy="${rayY}" r="4" fill="#fbbf24"/>
            <text x="${rayX - 5}" y="${rayY - 10}" fill="#fbbf24" font-size="13" font-weight="800">C</text>

            <!-- Angle Arcs -->
            <!-- Left Angle (180 - x) -->
            <path d="M 210 200 A 60 60 0 0 1 ${270 - 60 * Math.cos(rad)} ${200 - 60 * Math.sin(rad)}" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <text x="${270 - 75 * Math.cos(rad / 2)}" y="${200 - 45 * Math.sin(rad / 2)}" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">${y}°</text>

            <!-- Right Angle (x) -->
            <path d="M 330 200 A 60 60 0 0 0 ${270 - 60 * Math.cos(rad)} ${200 - 60 * Math.sin(rad)}" fill="none" stroke="#10b981" stroke-width="3"/>
            <text x="${270 + 75 * Math.cos(rad / 2)}" y="${200 - 45 * Math.sin(rad / 2)}" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">${x}°</text>

            <!-- Bottom Progress Gauge -->
            <g transform="translate(70, 245)">
              <rect x="0" y="0" width="400" height="20" rx="10" fill="#1e293b"/>
              <rect x="0" y="0" width="${(y / 180) * 400}" height="20" rx="10" fill="#0284c7"/>
              <rect x="${(y / 180) * 400}" y="0" width="${(x / 180) * 400}" height="20" rx="10" fill="#059669"/>
              <text x="${((y / 180) * 400) / 2}" y="14" fill="#ffffff" font-size="10" font-weight="800" text-anchor="middle">∠AOC: ${y}°</text>
              <text x="${(y / 180) * 400 + ((x / 180) * 400) / 2}" y="14" fill="#ffffff" font-size="10" font-weight="800" text-anchor="middle">∠BOC: ${x}°</text>
            </g>

            <text x="270" y="295" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">
              Two adjacent angles on a straight line are always supplementary: together they fill a half-circle (180°).
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Adjust Right Angle x:</span>
          <input type="range" id="lpSlider" min="15" max="165" value="${x}" style="width:200px; accent-color:#10b981; cursor:pointer;">
          <span id="lpVal" style="color:#10b981; font-weight:800; font-size:1.1rem; min-width:35px;">${x}°</span>
          <button class="sim-btn" id="lp90Btn">Set Right Angle (90° - 90°)</button>
        </div>
      `;

      const slider = simControls.querySelector('#lpSlider');
      slider.addEventListener('input', (e) => {
        x = parseInt(e.target.value);
        simControls.querySelector('#lpVal').textContent = `${x}°`;
        render();
      });

      simControls.querySelector('#lp90Btn').addEventListener('click', () => {
        x = 90;
        slider.value = 90;
        simControls.querySelector('#lpVal').textContent = "90°";
        render();
      });

      render();
    }

    // Slide 3: Perpendicular Lines Cross
    function simPerpendicularLinesCross() {
      simHeaderTitle.textContent = "Perpendicular Lines: The Universal 90° Right Angle Cross";
      let angle = 90;

      function render() {
        const isPerp = (angle === 90);
        const rad = (angle * Math.PI) / 180;
        const L = 120;
        const dx = L * Math.cos(rad);
        const dy = L * Math.sin(rad);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Status Banner -->
            <rect x="40" y="15" width="460" height="42" rx="10" fill="${isPerp ? '#064e3b' : '#1e293b'}" stroke="${isPerp ? '#10b981' : '#f59e0b'}" stroke-width="${isPerp ? 2.5 : 1.5}"/>
            <text x="270" y="41" fill="${isPerp ? '#34d399' : '#fbbf24'}" font-size="14" font-weight="900" text-anchor="middle">
              ${isPerp ? 'PERPENDICULAR LOCK: AB ⊥ CD (All 4 Angles = 90°)' : `Lines Intersecting at ${angle}° (Not Perpendicular)`}
            </text>

            <!-- Line 1: Horizontal AB -->
            <line x1="120" y1="160" x2="420" y2="160" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
            <text x="100" y="165" fill="#cbd5e1" font-size="13" font-weight="800">A</text>
            <text x="430" y="165" fill="#cbd5e1" font-size="13" font-weight="800">B</text>

            <!-- Line 2: CD -->
            <line x1="${270 - dx}" y1="${160 + dy}" x2="${270 + dx}" y2="${160 - dy}" stroke="${isPerp ? '#38bdf8' : '#f43f5e'}" stroke-width="4" stroke-linecap="round"/>
            <text x="${270 - dx - 10}" y="${160 + dy + 15}" fill="${isPerp ? '#38bdf8' : '#f43f5e'}" font-size="13" font-weight="800">C</text>
            <text x="${270 + dx + 10}" y="${160 - dy - 5}" fill="${isPerp ? '#38bdf8' : '#f43f5e'}" font-size="13" font-weight="800">D</text>

            <!-- Vertex O -->
            <circle cx="270" cy="160" r="5" fill="#ffffff"/>
            <text x="255" y="150" fill="#ffffff" font-size="11" font-weight="700">O</text>

            <!-- Perpendicular Corner Square Symbols (∟) or Arcs -->
            ${isPerp ? `
              <!-- Four 90 degree square markers -->
              <rect x="270" y="136" width="24" height="24" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
              <rect x="246" y="136" width="24" height="24" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
              <rect x="246" y="160" width="24" height="24" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
              <rect x="270" y="160" width="24" height="24" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>

              <text x="310" y="145" fill="#34d399" font-size="12" font-weight="900">90° (∟)</text>
              <text x="225" y="145" fill="#34d399" font-size="12" font-weight="900">90° (∟)</text>
              <text x="225" y="185" fill="#34d399" font-size="12" font-weight="900">90° (∟)</text>
              <text x="310" y="185" fill="#34d399" font-size="12" font-weight="900">90° (∟)</text>
            ` : `
              <text x="315" y="150" fill="#fbbf24" font-size="12" font-weight="800">${angle}°</text>
              <text x="220" y="150" fill="#fbbf24" font-size="12" font-weight="800">${180 - angle}°</text>
            `}

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Symbol of Perpendicularity is ⊥
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              When two lines are perpendicular, all four angles are equal to 90 degrees.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Everyday examples: window mullions, graph paper grids, crossroads, and plumb-lines!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Intersection Angle:</span>
          <input type="range" id="perpSlider" min="45" max="135" value="${angle}" style="width:180px; accent-color:#38bdf8; cursor:pointer;">
          <span id="perpVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:35px;">${angle}°</span>
          <button class="sim-btn ${angle === 90 ? 'active' : ''}" id="snap90Btn">Snap to 90° (Perpendicular)</button>
        </div>
      `;

      const slider = simControls.querySelector('#perpSlider');
      slider.addEventListener('input', (e) => {
        angle = parseInt(e.target.value);
        simControls.querySelector('#perpVal').textContent = `${angle}°`;
        simControls.querySelector('#snap90Btn').classList.toggle('active', angle === 90);
        render();
      });

      simControls.querySelector('#snap90Btn').addEventListener('click', () => {
        angle = 90;
        slider.value = 90;
        simControls.querySelector('#perpVal').textContent = "90°";
        simControls.querySelector('#snap90Btn').classList.add('active');
        render();
      });

      render();
    }

    // Slide 4: Between Lines - Parallel Lines & Constant Distance
    function simParallelRailwayTracks() {
      simHeaderTitle.textContent = "Parallel Lines: Invariant Perpendicular Distance (Equidistant)";
      let dist = 65; // distance between rails

      function render() {
        const yTop = 160 - dist / 2;
        const yBottom = 160 + dist / 2;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <linearGradient id="railGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#94a3b8"/>
                <stop offset="50%" stop-color="#f8fafc"/>
                <stop offset="100%" stop-color="#475569"/>
              </linearGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="15" width="460" height="40" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="40" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              Parallel Property: Distance d = ${dist} mm (Constant Everywhere!)
            </text>

            <!-- Railway Sleepers (Wood Ties) -->
            <g transform="translate(0, 0)">
              ${Array.from({ length: 11 }).map((_, i) => `
                <rect x="${55 + i * 40}" y="${yTop - 10}" width="16" height="${dist + 20}" rx="3" fill="#78350f" stroke="#92400e" stroke-width="1.5"/>
              `).join('')}
            </g>

            <!-- Top Rail (Line l) -->
            <line x1="30" y1="${yTop}" x2="510" y2="${yTop}" stroke="url(#railGrad)" stroke-width="6"/>
            <!-- Single Chevron Arrow Notation -->
            <polygon points="265,${yTop - 6} 275,${yTop} 265,${yTop + 6}" fill="#38bdf8"/>
            <text x="495" y="${yTop - 10}" fill="#38bdf8" font-size="13" font-weight="900">Line l</text>

            <!-- Bottom Rail (Line m) -->
            <line x1="30" y1="${yBottom}" x2="510" y2="${yBottom}" stroke="url(#railGrad)" stroke-width="6"/>
            <!-- Matching Single Chevron Arrow Notation -->
            <polygon points="265,${yBottom - 6} 275,${yBottom} 265,${yBottom + 6}" fill="#38bdf8"/>
            <text x="495" y="${yBottom + 20}" fill="#38bdf8" font-size="13" font-weight="900">Line m</text>

            <!-- Perpendicular Caliper Measurements at 3 distinct points -->
            <!-- Caliper 1 at x = 110 -->
            <line x1="115" y1="${yTop}" x2="115" y2="${yBottom}" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
            <circle cx="115" cy="${yTop}" r="3" fill="#10b981"/>
            <circle cx="115" cy="${yBottom}" r="3" fill="#10b981"/>
            <text x="115" y="165" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">d = ${dist}</text>

            <!-- Caliper 2 at x = 270 -->
            <line x1="270" y1="${yTop}" x2="270" y2="${yBottom}" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
            <circle cx="270" cy="${yTop}" r="3" fill="#10b981"/>
            <circle cx="270" cy="${yBottom}" r="3" fill="#10b981"/>
            <text x="270" y="165" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">d = ${dist}</text>

            <!-- Caliper 3 at x = 425 -->
            <line x1="435" y1="${yTop}" x2="435" y2="${yBottom}" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
            <circle cx="435" cy="${yTop}" r="3" fill="#10b981"/>
            <circle cx="435" cy="${yBottom}" r="3" fill="#10b981"/>
            <text x="435" y="165" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">d = ${dist}</text>

            <!-- Bottom Insight Card -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Axiom: Parallel Lines are Strictly Equidistant Everywhere ($l \parallel m$)
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              No matter how far train tracks are extended, the two rails never cross each other.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              The perpendicular distance between them remains exactly identical at all locations!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Track Gauge Distance (d):</span>
          <input type="range" id="gaugeSlider" min="40" max="90" value="${dist}" style="width:200px; accent-color:#38bdf8; cursor:pointer;">
          <span id="gaugeVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:40px;">${dist} mm</span>
          <button class="sim-btn" id="extendTrackBtn">🚀 Extend 1,000 km to Infinity</button>
        </div>
      `;

      const slider = simControls.querySelector('#gaugeSlider');
      slider.addEventListener('input', (e) => {
        dist = parseInt(e.target.value);
        simControls.querySelector('#gaugeVal').textContent = `${dist} mm`;
        render();
      });

      simControls.querySelector('#extendTrackBtn').addEventListener('click', () => {
        alert("Even if you extend the railway tracks across 1,000 kilometers,\nthe perpendicular distance remains strictly " + dist + " mm!\n\nParallel lines on a plane never meet!");
      });

      render();
    }

    // Slide 5: Paper Folding - Perpendicular Creases
    function simPaperFoldingPerpendicular() {
      simHeaderTitle.textContent = "Origami Geometry: Folding a Perpendicular Crease (90°)";
      let step = 0; // 0: baseline, 1: folded in half, 2: unfolded with 90° crease

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Progress Tracker -->
            <g transform="translate(80, 20)">
              <!-- Step 1 -->
              <circle cx="30" cy="15" r="14" fill="${step >= 0 ? '#38bdf8' : '#334155'}"/>
              <text x="30" y="20" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <text x="30" y="42" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Baseline</text>

              <line x1="45" y1="15" x2="165" y2="15" stroke="${step >= 1 ? '#38bdf8' : '#334155'}" stroke-width="3"/>

              <!-- Step 2 -->
              <circle cx="180" cy="15" r="14" fill="${step >= 1 ? '#38bdf8' : '#334155'}"/>
              <text x="180" y="20" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">2</text>
              <text x="180" y="42" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Fold Edge</text>

              <line x1="195" y1="15" x2="315" y2="15" stroke="${step >= 2 ? '#38bdf8' : '#334155'}" stroke-width="3"/>

              <!-- Step 3 -->
              <circle cx="330" cy="15" r="14" fill="${step >= 2 ? '#38bdf8' : '#334155'}"/>
              <text x="330" y="20" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">3</text>
              <text x="330" y="42" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">90° Crease</text>
            </g>

            <!-- Paper Sheet Display Area -->
            <g transform="translate(100, 75)">
              ${step === 0 ? `
                <!-- Step 0: Flat Paper with Baseline AB -->
                <rect x="0" y="0" width="340" height="150" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <line x1="20" y1="75" x2="320" y2="75" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
                <text x="25" y="65" fill="#0284c7" font-size="11" font-weight="800">A</text>
                <text x="310" y="65" fill="#0284c7" font-size="11" font-weight="800">B</text>
                <circle cx="170" cy="75" r="4" fill="#ef4444"/>
                <text x="170" y="65" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">P</text>
                <text x="170" y="115" fill="#475569" font-size="11" font-weight="700" text-anchor="middle">1. Baseline crease AB with marked point P</text>
              ` : step === 1 ? `
                <!-- Step 1: Folded Over -->
                <rect x="0" y="0" width="170" height="150" rx="6" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
                <polygon points="170,0 230,20 230,130 170,150" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
                <line x1="20" y1="75" x2="170" y2="75" stroke="#0284c7" stroke-width="4"/>
                <text x="85" y="65" fill="#0284c7" font-size="11" font-weight="800" text-anchor="middle">Segment AP & BP Match!</text>
                <circle cx="170" cy="75" r="5" fill="#ef4444"/>
                <text x="170" y="115" fill="#0369a1" font-size="11" font-weight="800" text-anchor="middle">2. Fold paper so line AP superimposes over line BP</text>
              ` : `
                <!-- Step 2: Unfolded with Perpendicular Crease -->
                <rect x="0" y="0" width="340" height="150" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <!-- Baseline -->
                <line x1="20" y1="75" x2="320" y2="75" stroke="#0284c7" stroke-width="3"/>
                <!-- Perpendicular Crease PQ -->
                <line x1="170" y1="10" x2="170" y2="140" stroke="#ef4444" stroke-width="3.5" stroke-dasharray="4"/>
                <!-- Right Angle Square Symbol -->
                <rect x="170" y="55" width="20" height="20" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
                <text x="180" y="70" fill="#047857" font-size="10" font-weight="900">90°</text>

                <circle cx="170" cy="75" r="4" fill="#ef4444"/>
                <text x="160" y="70" fill="#ef4444" font-size="11" font-weight="800">P</text>
                <text x="170" y="145" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">Q</text>
                <text x="170" y="25" fill="#047857" font-size="12" font-weight="900" text-anchor="middle">3. Unfold: Crease PQ ⊥ AB (90° Guaranteed!)</text>
              `}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Why Paper Folding Creates an Exact 90° Right Angle:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              A straight angle has 180°. Folding a line onto itself divides 180° into two equal symmetric halves:
            </text>
            <text x="270" y="303" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">
              180° ÷ 2 = 90° (Right Angle marked by the square corner symbol ∟)
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:0.6rem; justify-content:center;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">Step 1: Baseline AB</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">Step 2: Fold Over</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">Step 3: Unfold (90° Crease)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-step]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          step = parseInt(e.target.getAttribute('data-step'));
          simControls.querySelectorAll('button[data-step]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 6: Paper Folding - Parallel Creases
    function simPaperFoldingParallel() {
      simHeaderTitle.textContent = "Paper Folding: Double Perpendicular to Construct Parallel Lines";
      let showArrows = true;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="15" width="460" height="40" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="40" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              Double-Perpendicular Principle: l ⊥ t and m ⊥ t ➔ l ∥ m
            </text>

            <!-- Sheet of Paper -->
            <g transform="translate(70, 70)">
              <rect x="0" y="0" width="400" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>

              <!-- Transversal fold (t) -->
              <line x1="200" y1="15" x2="200" y2="140" stroke="#64748b" stroke-width="3" stroke-dasharray="4"/>
              <text x="200" y="10" fill="#64748b" font-size="11" font-weight="800" text-anchor="middle">Transversal Crease (t)</text>

              <!-- Crease 1: Line l (Perpendicular to t at P) -->
              <line x1="30" y1="45" x2="370" y2="45" stroke="#0284c7" stroke-width="3.5"/>
              <rect x="200" y="45" width="16" height="16" fill="rgba(2, 132, 199, 0.2)" stroke="#0284c7" stroke-width="1.5"/>
              <text x="380" y="49" fill="#0284c7" font-size="12" font-weight="900">Line l</text>

              <!-- Crease 2: Line m (Perpendicular to t at Q) -->
              <line x1="30" y1="110" x2="370" y2="110" stroke="#059669" stroke-width="3.5"/>
              <rect x="200" y="94" width="16" height="16" fill="rgba(5, 150, 105, 0.2)" stroke="#059669" stroke-width="1.5"/>
              <text x="380" y="114" fill="#059669" font-size="12" font-weight="900">Line m</text>

              ${showArrows ? `
                <!-- Matching Chevron Arrows on l and m -->
                <polygon points="100,39 110,45 100,51" fill="#38bdf8"/>
                <polygon points="112,39 122,45 112,51" fill="#38bdf8"/>

                <polygon points="100,104 110,110 100,116" fill="#34d399"/>
                <polygon points="112,104 122,110 112,116" fill="#34d399"/>

                <text x="135" y="42" fill="#0284c7" font-size="10" font-weight="800">Double Chevron (≫)</text>
                <text x="135" y="107" fill="#059669" font-size="10" font-weight="800">Double Chevron (≫)</text>
              ` : ''}

              <!-- Distance indicator -->
              <line x1="310" y1="45" x2="310" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/>
              <text x="325" y="82" fill="#d97706" font-size="11" font-weight="800">d = 65 mm</text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Standard Arrowhead Geometry Notation:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Matching single chevrons (>) or double chevrons (≫) on line segments indicate they are parallel.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Carpenters use this rule: two saw-cuts perpendicular to the same board edge will be strictly parallel!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn ${showArrows ? 'active' : ''}" id="toggleArrowsBtn">
            ${showArrows ? 'Hide Chevron Arrowheads' : 'Show Chevron Arrowheads (≫)'}
          </button>
        </div>
      `;

      simControls.querySelector('#toggleArrowsBtn').addEventListener('click', () => {
        showArrows = !showArrows;
        render();
      });

      render();
    }

    // Slide 7: Transversals - The 8-Angle Intersection Machine
    function simTransversalEightAngles() {
      simHeaderTitle.textContent = "The Transversal: 8 Angles Formed at a Double Intersection";
      let filterMode = 'all'; // 'all', 'interior', 'exterior'

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">
              ${filterMode === 'interior' ? 'INTERIOR ANGLES: Located inside between lines l and m (∠3, ∠4, ∠5, ∠6)' : filterMode === 'exterior' ? 'EXTERIOR ANGLES: Located outside the lines (∠1, ∠2, ∠7, ∠8)' : 'Transversal t crosses Lines l & m: 8 Total Angles'}
            </text>

            <!-- Interior Region Shading -->
            ${filterMode === 'interior' || filterMode === 'all' ? `
              <rect x="40" y="100" width="460" height="80" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4"/>
              <text x="60" y="145" fill="#38bdf8" font-size="11" font-weight="800">INTERIOR REGION</text>
            ` : ''}

            <!-- Line l (Top) -->
            <line x1="50" y1="100" x2="490" y2="100" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="95" fill="#94a3b8" font-size="13" font-weight="900">l</text>

            <!-- Line m (Bottom) -->
            <line x1="50" y1="180" x2="490" y2="180" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="185" fill="#94a3b8" font-size="13" font-weight="900">m</text>

            <!-- Transversal Line t (Slanted) -->
            <line x1="180" y1="50" x2="360" y2="230" stroke="#f59e0b" stroke-width="3.5"/>
            <text x="365" y="240" fill="#fbbf24" font-size="13" font-weight="900">t (transversal)</text>

            <!-- Intersection 1 (top): x = 230, y = 100 -->
            <!-- Angle 1: Top-Right (Exterior) -->
            <circle cx="250" cy="80" r="13" fill="${filterMode === 'interior' ? '#1e293b' : '#0284c7'}" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="250" y="84" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">1</text>

            <!-- Angle 2: Top-Left (Exterior) -->
            <circle cx="210" cy="80" r="13" fill="${filterMode === 'interior' ? '#1e293b' : '#0284c7'}" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="210" y="84" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">2</text>

            <!-- Angle 3: Bottom-Left (Interior) -->
            <circle cx="210" cy="120" r="13" fill="${filterMode === 'exterior' ? '#1e293b' : '#059669'}" stroke="#10b981" stroke-width="1.5"/>
            <text x="210" y="124" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">3</text>

            <!-- Angle 4: Bottom-Right (Interior) -->
            <circle cx="250" cy="120" r="13" fill="${filterMode === 'exterior' ? '#1e293b' : '#059669'}" stroke="#10b981" stroke-width="1.5"/>
            <text x="250" y="124" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">4</text>

            <!-- Intersection 2 (bottom): x = 310, y = 180 -->
            <!-- Angle 5: Top-Right (Interior) -->
            <circle cx="330" cy="160" r="13" fill="${filterMode === 'exterior' ? '#1e293b' : '#059669'}" stroke="#10b981" stroke-width="1.5"/>
            <text x="330" y="164" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">5</text>

            <!-- Angle 6: Top-Left (Interior) -->
            <circle cx="290" cy="160" r="13" fill="${filterMode === 'exterior' ? '#1e293b' : '#059669'}" stroke="#10b981" stroke-width="1.5"/>
            <text x="290" y="164" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">6</text>

            <!-- Angle 7: Bottom-Left (Exterior) -->
            <circle cx="290" cy="200" r="13" fill="${filterMode === 'interior' ? '#1e293b' : '#0284c7'}" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="290" y="204" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">7</text>

            <!-- Angle 8: Bottom-Right (Exterior) -->
            <circle cx="330" cy="200" r="13" fill="${filterMode === 'interior' ? '#1e293b' : '#0284c7'}" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="330" y="204" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">8</text>

            <!-- Bottom Insight -->
            <rect x="40" y="248" width="460" height="68" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="268" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Transversal Anatomy Summary:
            </text>
            <text x="270" y="288" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Green: <tspan fill="#34d399" font-weight="bold">Interior Angles</tspan> (∠3, ∠4, ∠5, ∠6) | Blue: <tspan fill="#38bdf8" font-weight="bold">Exterior Angles</tspan> (∠1, ∠2, ∠7, ∠8)
            </text>
            <text x="270" y="304" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">
              Notice: Even if lines l and m are NOT parallel, these 8 positions still exist!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${filterMode === 'all' ? 'active' : ''}" data-mode="all">Show All 8 Angles</button>
          <button class="sim-btn ${filterMode === 'interior' ? 'active' : ''}" data-mode="interior">Highlight Interior (∠3, 4, 5, 6)</button>
          <button class="sim-btn ${filterMode === 'exterior' ? 'active' : ''}" data-mode="exterior">Highlight Exterior (∠1, 2, 7, 8)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-mode]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          filterMode = e.target.getAttribute('data-mode');
          simControls.querySelectorAll('button[data-mode]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 8: Corresponding Angles - The F-Shape Explorer
    function simCorrespondingAnglesFShape() {
      simHeaderTitle.textContent = "Corresponding Angles: Matching Relative Positions & The F-Shape";
      let activePair = 'tr'; // 'tr' (1,5), 'tl' (2,6), 'br' (4,8), 'bl' (3,7)
      let isParallel = true;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">
              ${activePair === 'tr' ? 'Top-Right Pair: ∠1 and ∠5 (Equal: 65°)' : activePair === 'tl' ? 'Top-Left Pair: ∠2 and ∠6 (Equal: 115°)' : activePair === 'br' ? 'Bottom-Right Pair: ∠4 and ∠8 (Equal: 115°)' : 'Bottom-Left Pair: ∠3 and ∠7 (Equal: 65°)'}
            </text>

            <!-- Line l -->
            <line x1="50" y1="100" x2="490" y2="100" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="95" fill="#94a3b8" font-size="12" font-weight="800">l</text>

            <!-- Line m (tilted if non-parallel) -->
            <line x1="50" y1="${isParallel ? 180 : 160}" x2="490" y2="${isParallel ? 180 : 200}" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="${isParallel ? 185 : 205}" fill="#94a3b8" font-size="12" font-weight="800">m</text>

            <!-- Transversal line t -->
            <line x1="190" y1="50" x2="350" y2="230" stroke="#f59e0b" stroke-width="3"/>
            <text x="355" y="240" fill="#fbbf24" font-size="12" font-weight="800">t</text>

            <!-- The Bold F-Shape Overlay -->
            <g stroke="#06b6d4" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85">
              <!-- Backbone of F along transversal -->
              <line x1="234" y1="100" x2="306" y2="180"/>
              <!-- Top Arm of F along line l -->
              <line x1="234" y1="100" x2="340" y2="100"/>
              <!-- Bottom Arm of F along line m -->
              <line x1="306" y1="180" x2="410" y2="180"/>
            </g>

            <!-- Matching Highlighted Angles -->
            ${activePair === 'tr' ? `
              <circle cx="260" cy="85" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="260" y="90" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠1</text>
              <circle cx="335" cy="165" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="335" y="170" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠5</text>
            ` : activePair === 'tl' ? `
              <circle cx="210" cy="85" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="210" y="90" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠2</text>
              <circle cx="280" cy="165" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="280" y="170" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠6</text>
            ` : activePair === 'br' ? `
              <circle cx="260" cy="115" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="260" y="120" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠4</text>
              <circle cx="335" cy="195" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="335" y="200" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠8</text>
            ` : `
              <circle cx="210" cy="115" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="210" y="120" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠3</text>
              <circle cx="280" cy="195" r="16" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="280" y="200" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠7</text>
            `}

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The 'F-Shape' Memory Aid for Corresponding Angles:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Angles sitting at matching arms of the letter F are corresponding.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              When lines are parallel ($l \parallel m$), corresponding angles are ALWAYS equal!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${activePair === 'tr' ? 'active' : ''}" data-pair="tr">Top-Right (∠1 & ∠5)</button>
          <button class="sim-btn ${activePair === 'tl' ? 'active' : ''}" data-pair="tl">Top-Left (∠2 & ∠6)</button>
          <button class="sim-btn ${activePair === 'br' ? 'active' : ''}" data-pair="br">Bottom-Right (∠4 & ∠8)</button>
          <button class="sim-btn ${activePair === 'bl' ? 'active' : ''}" data-pair="bl">Bottom-Left (∠3 & ∠7)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-pair]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activePair = e.target.getAttribute('data-pair');
          simControls.querySelectorAll('button[data-pair]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 9: Parallelism Detector (Converse Test)
    function simParallelismDetector() {
      simHeaderTitle.textContent = "Converse Parallelism Detector: Are Lines Parallel?";
      const alpha = 58; // fixed angle on top line l
      let beta = 45; // user adjustable angle on line m

      function render() {
        const isParallel = (alpha === beta);
        const radBeta = (beta * Math.PI) / 180;
        const L = 220;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Detector Status Banner -->
            <rect x="40" y="15" width="460" height="42" rx="10" fill="${isParallel ? '#064e3b' : '#450a0a'}" stroke="${isParallel ? '#10b981' : '#f43f5e'}" stroke-width="2"/>
            <text x="270" y="41" fill="${isParallel ? '#34d399' : '#fca5a5'}" font-size="14" font-weight="900" text-anchor="middle">
              ${isParallel ? '✔ PARALLEL CONFIRMED: Corresponding Angles α = β = 58° (l ∥ m)' : `✖ NOT PARALLEL: α = 58° ≠ β = ${beta}° (Lines will intersect!)`}
            </text>

            <!-- Line l (Fixed at 58° to transversal) -->
            <line x1="50" y1="100" x2="490" y2="100" stroke="#38bdf8" stroke-width="3.5"/>
            <text x="495" y="95" fill="#38bdf8" font-size="13" font-weight="800">Line l</text>

            <!-- Transversal line t -->
            <line x1="200" y1="40" x2="330" y2="240" stroke="#f59e0b" stroke-width="3.5"/>
            <text x="335" y="245" fill="#fbbf24" font-size="13" font-weight="800">t</text>

            <!-- Top Angle alpha arc -->
            <text x="280" y="85" fill="#38bdf8" font-size="14" font-weight="900">α = 58°</text>

            <!-- Line m (Tilting based on beta) -->
            <!-- Intersection at (290, 180) -->
            <line x1="${290 - L * Math.cos((beta - 58) * Math.PI / 180)}" y1="${180 - L * Math.sin((beta - 58) * Math.PI / 180)}" x2="${290 + L * Math.cos((beta - 58) * Math.PI / 180)}" y2="${180 + L * Math.sin((beta - 58) * Math.PI / 180)}" stroke="${isParallel ? '#10b981' : '#f43f5e'}" stroke-width="3.5"/>
            <text x="495" y="${180 + L * Math.sin((beta - 58) * Math.PI / 180) + 5}" fill="${isParallel ? '#10b981' : '#f43f5e'}" font-size="13" font-weight="800">Line m</text>

            <!-- Bottom Angle beta display -->
            <text x="335" y="165" fill="${isParallel ? '#34d399' : '#fca5a5'}" font-size="14" font-weight="900">β = ${beta}°</text>

            <!-- Convergence warning indicator -->
            ${!isParallel ? `
              <text x="270" y="235" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">
                ${beta < 58 ? 'Lines converge towards the right side!' : 'Lines converge towards the left side!'}
              </text>
            ` : `
              <text x="270" y="235" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">
                Lines never meet: Invariant perpendicular distance maintained!
              </text>
            `}

            <!-- Bottom Insight -->
            <rect x="40" y="250" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="270" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Converse of Corresponding Angles Postulate:
            </text>
            <text x="270" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">
              If a pair of corresponding angles is equal, then the two lines are GUARANTEED to be parallel.
            </text>
            <text x="270" y="306" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Use the slider to tune angle β to exactly 58° to lock in parallelism!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Adjust Angle β:</span>
          <input type="range" id="betaSlider" min="35" max="80" value="${beta}" style="width:200px; accent-color:#f43f5e; cursor:pointer;">
          <span id="betaVal" style="color:#f43f5e; font-weight:800; font-size:1.1rem; min-width:35px;">${beta}°</span>
          <button class="sim-btn" id="lockParallelBtn">Lock Parallel (β = 58°)</button>
        </div>
      `;

      const slider = simControls.querySelector('#betaSlider');
      slider.addEventListener('input', (e) => {
        beta = parseInt(e.target.value);
        simControls.querySelector('#betaVal').textContent = `${beta}°`;
        simControls.querySelector('#betaVal').style.color = (beta === alpha) ? '#10b981' : '#f43f5e';
        render();
      });

      simControls.querySelector('#lockParallelBtn').addEventListener('click', () => {
        beta = 58;
        slider.value = 58;
        simControls.querySelector('#betaVal').textContent = "58°";
        simControls.querySelector('#betaVal').style.color = '#10b981';
        render();
      });

      render();
    }

    // Slide 10: Drawing Parallel Lines with Ruler and Set Square
    function simRulerSetSquareConstruction() {
      simHeaderTitle.textContent = "Drawing Parallel Lines: Ruler and Set Square Sliding Construction";
      let step = 0; // 0 to 3

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${step === 0 ? 'Step 1: Given line l and external point P' : step === 1 ? 'Step 2: Align set square edge with line l' : step === 2 ? 'Step 3: Place ruler firmly against set square edge (transversal)' : 'Step 4: Slide set square up to point P and draw line m!'}
            </text>

            <!-- Drafting Board Canvas -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="420" height="170" rx="8" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Baseline l -->
              <line x1="30" y1="130" x2="390" y2="130" stroke="#38bdf8" stroke-width="3"/>
              <text x="400" y="135" fill="#38bdf8" font-size="12" font-weight="800">Line l</text>

              <!-- External Point P -->
              <circle cx="210" cy="50" r="5" fill="#ef4444"/>
              <text x="210" y="40" fill="#ef4444" font-size="12" font-weight="900" text-anchor="middle">P</text>

              <!-- Step 1 & beyond: Set Square -->
              ${step >= 1 ? `
                <!-- Set Square (Triangle) at bottom or sliding -->
                <polygon points="${step >= 3 ? '130,50 210,50 130,130' : '130,130 210,130 130,50'}" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2"/>
                <text x="155" y="${step >= 3 ? '75' : '110'}" fill="#bae6fd" font-size="10" font-weight="700">Set Square</text>
              ` : ''}

              <!-- Step 2 & beyond: Fixed Ruler -->
              ${step >= 2 ? `
                <!-- Straight Ruler along vertical hypotenuse -->
                <rect x="80" y="20" width="45" height="140" rx="3" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
                <text x="102" y="95" fill="#fef08a" font-size="10" font-weight="800" transform="rotate(-90 102 95)" text-anchor="middle">Ruler (Transversal)</text>
              ` : ''}

              <!-- Step 3: Newly drawn parallel line m through P -->
              ${step === 3 ? `
                <line x1="30" y1="50" x2="390" y2="50" stroke="#10b981" stroke-width="3.5"/>
                <polygon points="300,44 310,50 300,56" fill="#10b981"/>
                <polygon points="300,124 310,130 300,136" fill="#38bdf8"/>
                <text x="400" y="55" fill="#10b981" font-size="12" font-weight="900">Line m ∥ l</text>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="248" width="460" height="68" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="268" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Mathematical Foundation of the Construction:
            </text>
            <text x="270" y="288" fill="#cbd5e1" font-size="11" text-anchor="middle">
              The ruler edge acts as a transversal. Sliding the set square preserves the angle orientation.
            </text>
            <text x="270" y="304" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Since corresponding angles are kept exactly equal, the drawn line m is strictly parallel to line l!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">1. Setup Point P</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">2. Place Set Square</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">3. Align Ruler</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">4. Slide & Rule Line m</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-step]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          step = parseInt(e.target.getAttribute('data-step'));
          simControls.querySelectorAll('button[data-step]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 11: Alternate Interior Angles - The Z-Shape Explorer
    function simAlternateInteriorZShape() {
      simHeaderTitle.textContent = "Alternate Interior Angles: The 'Z-Shape' & Rigorous Proof";
      let activePair = 'z'; // 'z' (3,5) or 'rev' (4,6)

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${activePair === 'z' ? 'Z-Shape Pair: ∠3 = ∠5 = 62° (Alternate Interior)' : 'Reversed Z-Shape Pair: ∠4 = ∠6 = 118° (Alternate Interior)'}
            </text>

            <!-- Line l -->
            <line x1="50" y1="100" x2="490" y2="100" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="95" fill="#94a3b8" font-size="12" font-weight="800">l</text>

            <!-- Line m -->
            <line x1="50" y1="180" x2="490" y2="180" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="185" fill="#94a3b8" font-size="12" font-weight="800">m</text>

            <!-- Transversal line t -->
            <line x1="190" y1="50" x2="350" y2="230" stroke="#f59e0b" stroke-width="3"/>
            <text x="355" y="240" fill="#fbbf24" font-size="12" font-weight="800">t</text>

            <!-- The Bold Z-Shape Overlay -->
            ${activePair === 'z' ? `
              <g stroke="#ec4899" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85">
                <!-- Top horizontal bar of Z -->
                <line x1="120" y1="100" x2="234" y2="100"/>
                <!-- Diagonal transversal stroke -->
                <line x1="234" y1="100" x2="306" y2="180"/>
                <!-- Bottom horizontal bar of Z -->
                <line x1="306" y1="180" x2="420" y2="180"/>
              </g>

              <!-- Alternate Interior Angles ∠3 and ∠5 -->
              <circle cx="210" cy="120" r="16" fill="#ec4899" stroke="#fbcfe8" stroke-width="2"/>
              <text x="210" y="125" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠3</text>

              <circle cx="330" cy="160" r="16" fill="#ec4899" stroke="#fbcfe8" stroke-width="2"/>
              <text x="330" y="165" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠5</text>
            ` : `
              <g stroke="#8b5cf6" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85">
                <!-- Top horizontal bar of reverse Z -->
                <line x1="350" y1="100" x2="234" y2="100"/>
                <!-- Diagonal transversal stroke -->
                <line x1="234" y1="100" x2="306" y2="180"/>
                <!-- Bottom horizontal bar of reverse Z -->
                <line x1="306" y1="180" x2="190" y2="180"/>
              </g>

              <!-- Alternate Interior Angles ∠4 and ∠6 -->
              <circle cx="255" cy="120" r="16" fill="#8b5cf6" stroke="#ddd6fe" stroke-width="2"/>
              <text x="255" y="125" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠4</text>

              <circle cx="285" cy="160" r="16" fill="#8b5cf6" stroke="#ddd6fe" stroke-width="2"/>
              <text x="285" y="165" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠6</text>
            `}

            <!-- Deductive Proof Card -->
            <g transform="translate(60, 245)">
              <rect x="0" y="0" width="420" height="70" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="210" y="20" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">DEDUCTIVE PROOF OF EQUALITY</text>
              <text x="210" y="40" fill="#f8fafc" font-size="11" text-anchor="middle">
                1. ∠1 = ∠5 (Corresponding) &nbsp;|&nbsp; 2. ∠1 = ∠3 (Vertically Opposite)
              </text>
              <text x="210" y="60" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">
                Therefore: ∠3 = ∠5 &nbsp;➔&nbsp; Alternate Interior Angles are ALWAYS EQUAL!
              </text>
            </g>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem;">
          <button class="sim-btn ${activePair === 'z' ? 'active' : ''}" data-pair="z">Z-Shape Pair (∠3 & ∠5)</button>
          <button class="sim-btn ${activePair === 'rev' ? 'active' : ''}" data-pair="rev">Reversed Z-Shape Pair (∠4 & ∠6)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-pair]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activePair = e.target.getAttribute('data-pair');
          simControls.querySelectorAll('button[data-pair]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 12: Alternate Exterior Angles
    function simAlternateExteriorAngles() {
      simHeaderTitle.textContent = "Alternate Exterior Angles: Outer Zigzag Balance";
      let activePair = 'pair1'; // 'pair1' (1,7) or 'pair2' (2,8)

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${activePair === 'pair1' ? 'Alternate Exterior Pair 1: ∠1 = ∠7 = 64°' : 'Alternate Exterior Pair 2: ∠2 = ∠8 = 116°'}
            </text>

            <!-- Line l -->
            <line x1="50" y1="110" x2="490" y2="110" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="105" fill="#94a3b8" font-size="12" font-weight="800">l</text>

            <!-- Line m -->
            <line x1="50" y1="170" x2="490" y2="170" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="175" fill="#94a3b8" font-size="12" font-weight="800">m</text>

            <!-- Transversal line t -->
            <line x1="190" y1="50" x2="350" y2="230" stroke="#f59e0b" stroke-width="3"/>
            <text x="355" y="240" fill="#fbbf24" font-size="12" font-weight="800">t</text>

            ${activePair === 'pair1' ? `
              <!-- ∠1 (Top-Right Exterior) -->
              <circle cx="260" cy="85" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="260" y="90" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠1</text>

              <!-- ∠7 (Bottom-Left Exterior) -->
              <circle cx="280" cy="195" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="280" y="200" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠7</text>

              <!-- Zigzag connecting line -->
              <line x1="260" y1="85" x2="280" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
            ` : `
              <!-- ∠2 (Top-Left Exterior) -->
              <circle cx="210" cy="85" r="16" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
              <text x="210" y="90" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠2</text>

              <!-- ∠8 (Bottom-Right Exterior) -->
              <circle cx="330" cy="195" r="16" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
              <text x="330" y="200" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">∠8</text>

              <!-- Zigzag connecting line -->
              <line x1="210" y1="85" x2="330" y2="195" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4"/>
            `}

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Why Alternate Exterior Angles are Equal:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              ∠1 = ∠5 (Corresponding) and ∠5 = ∠7 (Vertically opposite) ➔ ∠1 = ∠7!
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Both angles live on the outer sides of the parallel lines on opposite sides of the transversal!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem;">
          <button class="sim-btn ${activePair === 'pair1' ? 'active' : ''}" data-pair="pair1">Pair 1: ∠1 & ∠7 (Acute Exterior)</button>
          <button class="sim-btn ${activePair === 'pair2' ? 'active' : ''}" data-pair="pair2">Pair 2: ∠2 & ∠8 (Obtuse Exterior)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-pair]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activePair = e.target.getAttribute('data-pair');
          simControls.querySelectorAll('button[data-pair]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 13: Co-Interior Angles - The C-Shape Explorer
    function simCoInteriorCShape() {
      simHeaderTitle.textContent = "Co-Interior Angles: The 'C-Shape' 180° Supplementary Rule";
      let angle4 = 115; // obtuse interior angle

      function render() {
        const angle5 = 180 - angle4;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Co-Interior Angles Sum: ∠4 + ∠5 = ${angle4}° + ${angle5}° = 180° (Supplementary)
            </text>

            <!-- Line l -->
            <line x1="50" y1="100" x2="490" y2="100" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="95" fill="#94a3b8" font-size="12" font-weight="800">l</text>

            <!-- Line m -->
            <line x1="50" y1="180" x2="490" y2="180" stroke="#94a3b8" stroke-width="3"/>
            <text x="495" y="185" fill="#94a3b8" font-size="12" font-weight="800">m</text>

            <!-- Transversal line t -->
            <line x1="190" y1="50" x2="350" y2="230" stroke="#f59e0b" stroke-width="3"/>
            <text x="355" y="240" fill="#fbbf24" font-size="12" font-weight="800">t</text>

            <!-- The Bold C-Shape Overlay on right interior -->
            <g stroke="#f59e0b" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85">
              <!-- Top bar of C -->
              <line x1="330" y1="100" x2="234" y2="100"/>
              <!-- Spine of C along transversal -->
              <line x1="234" y1="100" x2="306" y2="180"/>
              <!-- Bottom bar of C -->
              <line x1="306" y1="180" x2="400" y2="180"/>
            </g>

            <!-- Angle 4 (Top right interior) -->
            <circle cx="260" cy="120" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <text x="260" y="125" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">∠4</text>
            <text x="295" y="125" fill="#38bdf8" font-size="13" font-weight="900">${angle4}°</text>

            <!-- Angle 5 (Bottom right interior) -->
            <circle cx="335" cy="160" r="16" fill="#059669" stroke="#10b981" stroke-width="2"/>
            <text x="335" y="165" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">∠5</text>
            <text x="370" y="165" fill="#34d399" font-size="13" font-weight="900">${angle5}°</text>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The 'C-Shape' (Allied Angles) Theorem:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Interior angles on the same side of a transversal are NOT equal—they add up to 180°!
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Proof: ∠4 + ∠1 = 180° (linear pair) and ∠1 = ∠5 (corresponding) ➔ ∠4 + ∠5 = 180°!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Adjust Angle ∠4:</span>
          <input type="range" id="cAngleSlider" min="95" max="155" value="${angle4}" style="width:180px; accent-color:#0284c7; cursor:pointer;">
          <span id="cAngleVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:40px;">${angle4}°</span>
          <button class="sim-btn" id="perpCBtn">Perpendicular (90° + 90°)</button>
        </div>
      `;

      const slider = simControls.querySelector('#cAngleSlider');
      slider.addEventListener('input', (e) => {
        angle4 = parseInt(e.target.value);
        simControls.querySelector('#cAngleVal').textContent = `${angle4}°`;
        render();
      });

      simControls.querySelector('#perpCBtn').addEventListener('click', () => {
        angle4 = 90;
        slider.value = 90;
        simControls.querySelector('#cAngleVal').textContent = "90°";
        render();
      });

      render();
    }

    // Slide 14: Parallel Illusions - The Café Wall Illusion
    function simCafeWallIllusion() {
      simHeaderTitle.textContent = "Geometric Illusions: The Famous Café Wall Optical Mystery";
      let offset = 25; // 0 to 50 px shift
      let showGuides = false;

      function render() {
        const rows = 5;
        const tileW = 50;
        const tileH = 26;

        let rowsSvg = '';
        for (let r = 0; r < rows; r++) {
          const shift = (r % 2 === 1) ? offset : 0;
          const y = 80 + r * (tileH + 4);

          let tiles = '';
          for (let c = -1; c < 10; c++) {
            const x = c * tileW + shift;
            const fill = (c % 2 === 0) ? '#0f172a' : '#f8fafc';
            tiles += `<rect x="${x}" y="${y}" width="${tileW}" height="${tileH}" fill="${fill}" stroke="#475569" stroke-width="0.5"/>`;
          }

          rowsSvg += `
            <g>${tiles}</g>
            <!-- Mortar Line -->
            <line x1="20" y1="${y + tileH + 2}" x2="520" y2="${y + tileH + 2}" stroke="#94a3b8" stroke-width="3"/>
            ${showGuides ? `
              <line x1="20" y1="${y + tileH + 2}" x2="520" y2="${y + tileH + 2}" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6"/>
            ` : ''}
          `;
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${offset === 0 ? 'Zero Offset: Standard Chessboard (Lines Look Completely Straight!)' : 'Offset Tiles: Brain Perceives Wedges, but All Grey Lines are 100% Parallel!'}
            </text>

            <!-- Tiled Wall -->
            <g>
              ${rowsSvg}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              Why Your Brain Gets Tricked:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Staggered black-and-white tiles trigger acute-angle expansion in the visual cortex.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Turn on the green guide lasers or set offset to 0 to prove every mortar line is parallel!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Tile Stagger Offset:</span>
          <input type="range" id="offsetSlider" min="0" max="50" value="${offset}" style="width:160px; accent-color:#38bdf8; cursor:pointer;">
          <span id="offsetVal" style="color:#38bdf8; font-weight:800; min-width:30px;">${offset}px</span>
          <button class="sim-btn ${showGuides ? 'active' : ''}" id="toggleGuideBtn">
            ${showGuides ? 'Hide Green Lasers' : 'Show Green Laser Guides'}
          </button>
        </div>
      `;

      const slider = simControls.querySelector('#offsetSlider');
      slider.addEventListener('input', (e) => {
        offset = parseInt(e.target.value);
        simControls.querySelector('#offsetVal').textContent = `${offset}px`;
        render();
      });

      simControls.querySelector('#toggleGuideBtn').addEventListener('click', () => {
        showGuides = !showGuides;
        render();
      });

      render();
    }

    // Slide 15: Hering & Zöllner Illusions
    function simHeringZollnerIllusions() {
      simHeaderTitle.textContent = "Geometric Illusions: The Hering & Zöllner Space Warps";
      let illusionType = 'hering'; // 'hering' or 'zollner'
      let showBackground = true;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${illusionType === 'hering' ? 'Hering Illusion (1861): Red Lines Appear to Bow Outwards!' : 'Zöllner Illusion (1860): Diagonal Hatches Make Parallel Lines Look Tilted!'}
            </text>

            <g transform="translate(70, 60)">
              <rect x="0" y="0" width="400" height="175" rx="8" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              ${illusionType === 'hering' ? `
                <!-- Hering Illusion: Radial Spokes radiating from (200, 87) -->
                ${showBackground ? `
                  <g stroke="#475569" stroke-width="1.5">
                    ${Array.from({ length: 36 }).map((_, i) => {
                      const ang = (i * 10 * Math.PI) / 180;
                      return `<line x1="200" y1="87" x2="${200 + 220 * Math.cos(ang)}" y2="${87 + 220 * Math.sin(ang)}"/>`;
                    }).join('')}
                  </g>
                ` : ''}

                <!-- Two Straight Parallel Red Lines -->
                <line x1="140" y1="15" x2="140" y2="160" stroke="#ef4444" stroke-width="4"/>
                <line x1="260" y1="15" x2="260" y2="160" stroke="#ef4444" stroke-width="4"/>

                <text x="140" y="172" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">Line 1</text>
                <text x="260" y="172" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">Line 2 (Parallel!)</text>
              ` : `
                <!-- Zöllner Illusion: 4 Parallel Lines with alternating diagonal hatch marks -->
                <g stroke="#ef4444" stroke-width="3.5">
                  <line x1="40" y1="35" x2="360" y2="35"/>
                  <line x1="40" y1="75" x2="360" y2="75"/>
                  <line x1="40" y1="115" x2="360" y2="115"/>
                  <line x1="40" y1="155" x2="360" y2="155"/>
                </g>

                ${showBackground ? `
                  <g stroke="#38bdf8" stroke-width="2">
                    <!-- Row 1: tilt +45 -->
                    ${Array.from({ length: 14 }).map((_, i) => `
                      <line x1="${55 + i * 22 - 8}" y1="43" x2="${55 + i * 22 + 8}" y2="27"/>
                    `).join('')}

                    <!-- Row 2: tilt -45 -->
                    ${Array.from({ length: 14 }).map((_, i) => `
                      <line x1="${55 + i * 22 - 8}" y1="67" x2="${55 + i * 22 + 8}" y2="83"/>
                    `).join('')}

                    <!-- Row 3: tilt +45 -->
                    ${Array.from({ length: 14 }).map((_, i) => `
                      <line x1="${55 + i * 22 - 8}" y1="123" x2="${55 + i * 22 + 8}" y2="107"/>
                    `).join('')}

                    <!-- Row 4: tilt -45 -->
                    ${Array.from({ length: 14 }).map((_, i) => `
                      <line x1="${55 + i * 22 - 8}" y1="147" x2="${55 + i * 22 + 8}" y2="163"/>
                    `).join('')}
                  </g>
                ` : ''}
              `}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Reality Behind the Illusion:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Our brain overestimates acute angles where intersecting spokes cross the parallel lines.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Toggle the background lines off to see the red lines snap into undeniable straight parallel lines!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${illusionType === 'hering' ? 'active' : ''}" data-type="hering">Hering Illusion (Bowing)</button>
          <button class="sim-btn ${illusionType === 'zollner' ? 'active' : ''}" data-type="zollner">Zöllner Illusion (Hatching)</button>
          <button class="sim-btn ${showBackground ? 'active' : ''}" id="toggleBgBtn">
            ${showBackground ? 'Strip Distracting Lines' : 'Restore Distracting Lines'}
          </button>
        </div>
      `;

      simControls.querySelectorAll('button[data-type]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          illusionType = e.target.getAttribute('data-type');
          simControls.querySelectorAll('button[data-type]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      simControls.querySelector('#toggleBgBtn').addEventListener('click', () => {
        showBackground = !showBackground;
        render();
      });

      render();
    }

    // Slide 16: Baudhayana Sulba Sutra Heritage
    function simBaudhayanaSulbaRopes() {
      simHeaderTitle.textContent = "Acharya Baudhayana's Cord & Peg (Sanku-Rajju) Geometry";
      let step = 0; // 0: East-West line, 1: Arcs from East & West pegs, 2: North-South perpendicular, 3: Parallel altar boundary

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="270" y="36" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">
              ${step === 0 ? 'Step 1: Gnomon (Sanku) Shadows Establish True East-West Baseline' : step === 1 ? 'Step 2: Cords (Rajju) Strike Circular Arcs from East & West Pegs' : step === 2 ? 'Step 3: Line Connecting Arc Intersections Forms True North-South Perpendicular' : 'Step 4: Erecting Equal Cord Perpendiculars Produces Exact Parallel Altar Lines!'}
            </text>

            <!-- Altar Ground Canvas -->
            <g transform="translate(60, 60)">
              <rect x="0" y="0" width="420" height="175" rx="8" fill="#1e1b4b" stroke="#4338ca" stroke-width="1.5"/>

              <!-- Baseline East-West (Prachi) -->
              <line x1="40" y1="87" x2="380" y2="87" stroke="#fbbf24" stroke-width="3"/>
              <!-- Pegs -->
              <circle cx="90" cy="87" r="5" fill="#f59e0b"/>
              <text x="90" y="105" fill="#fef08a" font-size="10" font-weight="800" text-anchor="middle">West Peg</text>

              <circle cx="330" cy="87" r="5" fill="#f59e0b"/>
              <text x="330" y="105" fill="#fef08a" font-size="10" font-weight="800" text-anchor="middle">East Peg</text>

              <circle cx="210" cy="87" r="5" fill="#ffffff"/>
              <text x="210" y="105" fill="#ffffff" font-size="10" font-weight="800" text-anchor="middle">Center Sanku</text>

              <!-- Step 1+: Intersecting Arcs from East and West Pegs -->
              ${step >= 1 ? `
                <!-- Arc from West peg -->
                <path d="M 210 20 A 140 140 0 0 1 210 155" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
                <!-- Arc from East peg -->
                <path d="M 210 20 A 140 140 0 0 0 210 155" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>

                <!-- Arc intersection points -->
                <circle cx="210" cy="25" r="4" fill="#38bdf8"/>
                <circle cx="210" cy="150" r="4" fill="#38bdf8"/>
              ` : ''}

              <!-- Step 2+: North-South Perpendicular -->
              ${step >= 2 ? `
                <line x1="210" y1="15" x2="210" y2="160" stroke="#38bdf8" stroke-width="3.5"/>
                <rect x="210" y="71" width="16" height="16" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="210" y="10" fill="#38bdf8" font-size="10" font-weight="900" text-anchor="middle">North</text>
                <text x="210" y="172" fill="#38bdf8" font-size="10" font-weight="900" text-anchor="middle">South</text>
              ` : ''}

              <!-- Step 3: Northern Parallel Altar Boundary -->
              ${step === 3 ? `
                <!-- Equal perpendicular cord at West peg -->
                <line x1="90" y1="87" x2="90" y2="35" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
                <circle cx="90" cy="35" r="4" fill="#10b981"/>

                <!-- Equal perpendicular cord at East peg -->
                <line x1="330" y1="87" x2="330" y2="35" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
                <circle cx="330" cy="35" r="4" fill="#10b981"/>

                <!-- Parallel Line joining tops -->
                <line x1="40" y1="35" x2="380" y2="35" stroke="#10b981" stroke-width="3.5"/>
                <polygon points="260,29 270,35 260,41" fill="#10b981"/>
                <polygon points="260,81 270,87 260,93" fill="#fbbf24"/>
                <text x="390" y="40" fill="#10b981" font-size="11" font-weight="900">Altar Parallel Line</text>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="245" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              Baudhayana Sulba Sutra Heritage (c. 800 BCE):
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              By using simple ropes (*rajju*) and pegs (*sanku*), ancient Indian geometers laid out
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              flawless parallel lines and right angles for magnificent altars like the Shyena-chiti (Falcon Altar)!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">1. East-West Baseline</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">2. Strike Cord Arcs</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">3. North-South Perpendicular</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">4. Construct Parallel Altar</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-step]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          step = parseInt(e.target.getAttribute('data-step'));
          simControls.querySelectorAll('button[data-step]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }
"""
'''

with open('.agents/class7_math_parallel_intersecting_lines_sims.py', 'w', encoding='utf-8') as f:
    f.write(sims_code)

print("Successfully generated .agents/class7_math_parallel_intersecting_lines_sims.py")

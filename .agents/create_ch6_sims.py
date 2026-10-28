# -*- coding: utf-8 -*-
"""
Helper to write .agents/class7_math_number_play_sims.py
"""

sims_code = r'''# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 7 Mathematics - Chapter 6: Number Play
Simulators 1 to 16
"""

SIMULATORS_JS = r"""
    // ========================================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 6 Number Play)
    // ========================================================

    // Slide 1: Height Queue Decoder
    function simHeightQueueDecoder() {
      simHeaderTitle.textContent = "Positional Deduction: The Height Queue Decoder";
      // 5 students with heights 1 to 5 (5 is tallest)
      // queue order: array of heights from position 1 (front) to 5 (back)
      let queue = [3, 1, 5, 2, 4]; // sample heights

      function getCallouts() {
        return queue.map((h, idx) => {
          let tallerAhead = 0;
          for (let i = 0; i < idx; i++) {
            if (queue[i] > h) tallerAhead++;
          }
          return tallerAhead;
        });
      }

      function render() {
        const callouts = getCallouts();

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <linearGradient id="stickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#38bdf8"/>
                <stop offset="100%" stop-color="#0284c7"/>
              </linearGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">
              Queue Callouts: [ ${callouts.join(', ')} ] &nbsp;|&nbsp; Students facing FRONT (Left) ➔
            </text>

            <!-- Front of Queue Indicator -->
            <polygon points="40,165 60,150 60,180" fill="#f59e0b"/>
            <text x="50" y="200" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">FRONT</text>

            <!-- Ground Line -->
            <line x1="60" y1="210" x2="490" y2="210" stroke="#475569" stroke-width="3"/>

            <!-- 5 Students in Single File Line -->
            <g transform="translate(60, 0)">
              ${queue.map((h, idx) => {
                const x = 50 + idx * 75;
                const bodyH = h * 24 + 15;
                const yHead = 210 - bodyH;
                const isTallest = (h === 5);

                return `
                  <!-- Callout Bubble -->
                  <rect x="${x - 22}" y="${yHead - 48}" width="44" height="28" rx="6" fill="#1e293b" stroke="${isTallest ? '#10b981' : '#f59e0b'}" stroke-width="2"/>
                  <text x="${x}" y="${yHead - 30}" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${callouts[idx]}</text>
                  <!-- Bubble Pointer -->
                  <polygon points="${x - 4},${yHead - 20} ${x + 4},${yHead - 20} ${x},${yHead - 14}" fill="#1e293b"/>

                  <!-- Student Figure -->
                  <!-- Head -->
                  <circle cx="${x}" cy="${yHead}" r="11" fill="${isTallest ? '#34d399' : '#38bdf8'}"/>
                  <!-- Body -->
                  <rect x="${x - 7}" y="${yHead + 11}" width="14" height="${bodyH - 11}" rx="3" fill="url(#stickGrad)"/>

                  <!-- Position & Height Tag -->
                  <text x="${x}" y="228" fill="#cbd5e1" font-size="11" font-weight="800" text-anchor="middle">Pos ${idx + 1}</text>
                  <text x="${x}" y="242" fill="#94a3b8" font-size="9.5" text-anchor="middle">H = ${h}</text>
                `;
              }).join('')}
            </g>

            <!-- Bottom Insight Card -->
            <rect x="40" y="255" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="274" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              The Height Queue Invariant Rules:
            </text>
            <text x="270" y="293" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1. Position 1 always calls out 0 &nbsp;|&nbsp; 2. The tallest student (H=5) ALWAYS calls out 0
            </text>
            <text x="270" y="309" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click 'Shuffle Line' to see callout numbers transform based on heights!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem; flex-wrap:wrap;">
          <button class="sim-btn" id="shufBtn">🎲 Shuffle Line</button>
          <button class="sim-btn" id="sortAscBtn">Sort Short to Tall (1 to 5)</button>
          <button class="sim-btn" id="sortDescBtn">Sort Tall to Short (5 to 1)</button>
        </div>
      `;

      simControls.querySelector('#shufBtn').addEventListener('click', () => {
        queue = queue.sort(() => Math.random() - 0.5);
        render();
      });

      simControls.querySelector('#sortAscBtn').addEventListener('click', () => {
        queue = [1, 2, 3, 4, 5];
        render();
      });

      simControls.querySelector('#sortDescBtn').addEventListener('click', () => {
        queue = [5, 4, 3, 2, 1];
        render();
      });

      render();
    }

    // Slide 2: Positional Logic & Stepwise Invariants
    function simPositionalLineupInvariants() {
      simHeaderTitle.textContent = "Detective Logic: Step-by-Step Queue Reconstruction";
      let step = 0; // 0 to 4
      // Target queue: [2, 4, 1, 3] with callouts [0, 0, 2, 1]

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Target Clue Sequence: [ 0, 0, 2, 1 ] for Heights {1, 2, 3, 4}
            </text>

            <!-- Deduction Board -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- 4 Position Slots -->
              ${[1, 2, 3, 4].map((pos, idx) => `
                <g transform="translate(${25 + idx * 95}, 20)">
                  <rect x="0" y="0" width="80" height="90" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
                  <text x="40" y="18" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">SLOT ${pos}</text>

                  <!-- Contents based on step -->
                  ${step >= 1 && pos === 2 ? `
                    <circle cx="40" cy="45" r="16" fill="#10b981"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 4</text>
                    <text x="40" y="78" fill="#34d399" font-size="9" font-weight="800" text-anchor="middle">Tallest!</text>
                  ` : ''}

                  ${step >= 2 && pos === 4 ? `
                    <circle cx="40" cy="45" r="16" fill="#38bdf8"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 3</text>
                    <text x="40" y="78" fill="#38bdf8" font-size="9" font-weight="800" text-anchor="middle">1 Taller</text>
                  ` : ''}

                  ${step >= 3 && pos === 1 ? `
                    <circle cx="40" cy="45" r="16" fill="#f59e0b"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 2</text>
                    <text x="40" y="78" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">0 Taller</text>
                  ` : ''}

                  ${step >= 4 && pos === 3 ? `
                    <circle cx="40" cy="45" r="16" fill="#ec4899"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 1</text>
                    <text x="40" y="78" fill="#f472b6" font-size="9" font-weight="800" text-anchor="middle">2 Taller</text>
                  ` : ''}
                </g>
              `).join('')}

              <!-- Deduction Step Explanation -->
              <rect x="25" y="125" width="370" height="38" rx="6" fill="#0f172a"/>
              <text x="210" y="148" fill="#f8fafc" font-size="11" font-weight="800" text-anchor="middle">
                ${step === 0 ? 'Clue: Start by placing the tallest student (H=4)...' : step === 1 ? 'Step 1: H=4 must have callout 0. Slot 2 has 0, so H=4 fits at Slot 2!' : step === 2 ? 'Step 2: H=3 has callout 1. One taller ahead (H=4 at Slot 2) ➔ Slot 4!' : step === 3 ? 'Step 3: H=2 has callout 0 ➔ Placed in front at Slot 1!' : 'Solved! Slot 3 is the remaining spot for shortest student H=1!'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="250" width="460" height="68" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="270" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              The Backward Elimination Strategy:
            </text>
            <text x="270" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Always place the tallest elements first, because their callouts depend on nobody else!
            </text>
            <text x="270" y="306" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Every set of callout numbers corresponds to exactly ONE unique ordering.
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">Reset</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">Step 1: Place H=4</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">Step 2: Place H=3</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">Step 3: Place H=2</button>
          <button class="sim-btn ${step === 4 ? 'active' : ''}" data-step="4">Step 4: Place H=1 (Done)</button>
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

    // Slide 3: Picking Parity - Visual Pair-Matching
    function simParityPairMatching() {
      simHeaderTitle.textContent = "The Geometry of Parity: Perfect Pairs vs Solitary Dots";
      let n = 9; // 1 to 20

      function render() {
        const isEven = (n % 2 === 0);
        const pairs = Math.floor(n / 2);
        const hasLeftover = (n % 2 !== 0);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Status Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="${isEven ? '#064e3b' : '#78350f'}" stroke="${isEven ? '#10b981' : '#f59e0b'}" stroke-width="2"/>
            <text x="270" y="36" fill="${isEven ? '#34d399' : '#fef08a'}" font-size="14" font-weight="900" text-anchor="middle">
              ${n} is ${isEven ? 'EVEN: Exactly ' + pairs + ' Complete Pairs (0 Remainder)' : 'ODD: ' + pairs + ' Pairs + 1 Lonely Unpaired Dot!'}
            </text>

            <!-- 2-Row Dot Pairing Grid -->
            <g transform="translate(60, 75)">
              <rect x="0" y="0" width="420" height="150" rx="12" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Row 1: Top dots -->
              ${Array.from({ length: pairs }).map((_, i) => `
                <!-- Pair box -->
                <rect x="${25 + i * 36}" y="25" width="28" height="85" rx="6" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Top Dot -->
                <circle cx="${39 + i * 36}" cy="45" r="10" fill="#38bdf8"/>
                <!-- Bottom Dot -->
                <circle cx="${39 + i * 36}" cy="90" r="10" fill="#38bdf8"/>
                <text x="${39 + i * 36}" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Pair ${i + 1}</text>
              `).join('')}

              <!-- Solitary Dot if Odd -->
              ${hasLeftover ? `
                <g transform="translate(${25 + pairs * 36}, 25)">
                  <rect x="0" y="0" width="28" height="85" rx="6" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
                  <circle cx="14" cy="45" r="10" fill="#ef4444"/>
                  <!-- Empty Partner Slot -->
                  <circle cx="14" cy="90" r="10" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="14" y="93" fill="#fca5a5" font-size="8" text-anchor="middle">Empty</text>
                  <text x="14" y="125" fill="#f87171" font-size="9" font-weight="900" text-anchor="middle">+1</text>
                </g>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="240" width="460" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Formal Algebraic Definitions of Parity:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              ${isEven ? `Even Number: ${n} = 2 × ${pairs} ➔ General form is 2k (Divisible by 2)` : `Odd Number: ${n} = 2 × ${pairs} + 1 ➔ General form is 2k + 1 (Remainder 1)`}
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Slide the controller below to observe how every number alternates between Even and Odd!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Test Number (n):</span>
          <input type="range" id="paritySlider" min="1" max="20" value="${n}" style="width:200px; accent-color:#38bdf8; cursor:pointer;">
          <span id="parityVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">${n}</span>
          <button class="sim-btn" id="randParityBtn">🎲 Random Number</button>
        </div>
      `;

      const slider = simControls.querySelector('#paritySlider');
      slider.addEventListener('input', (e) => {
        n = parseInt(e.target.value);
        simControls.querySelector('#parityVal').textContent = n;
        render();
      });

      simControls.querySelector('#randParityBtn').addEventListener('click', () => {
        n = Math.floor(Math.random() * 20) + 1;
        slider.value = n;
        simControls.querySelector('#parityVal').textContent = n;
        render();
      });

      render();
    }

    // Slide 4: Parity Arithmetic Laws
    function simParityArithmeticMatrix() {
      simHeaderTitle.textContent = "Parity Arithmetic: Why Odd + Odd Always Equals Even";
      let opType = 'odd_odd'; // 'even_even', 'odd_odd', 'even_odd'

      function render() {
        let titleText = "Odd + Odd = Even (Two Lonely Dots Combine into a Pair!)";
        let num1 = 5, num2 = 3;
        let sum = 8;
        let isResultEven = true;

        if (opType === 'even_even') {
          titleText = "Even + Even = Even (Both sets already paired; 0 leftovers!)";
          num1 = 4; num2 = 6; sum = 10; isResultEven = true;
        } else if (opType === 'even_odd') {
          titleText = "Even + Odd = Odd (One lonely dot remains without a partner!)";
          num1 = 4; num2 = 5; sum = 9; isResultEven = false;
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${titleText}
            </text>

            <!-- Visual Equation Cards -->
            <g transform="translate(40, 65)">
              <!-- Term 1 Card -->
              <rect x="0" y="0" width="130" height="150" rx="10" fill="#111827" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="65" y="24" fill="#38bdf8" font-size="12" font-weight="900" text-anchor="middle">
                ${num1 % 2 === 0 ? 'EVEN' : 'ODD'} (${num1})
              </text>
              <g transform="translate(15, 40)">
                ${Array.from({ length: Math.floor(num1 / 2) }).map((_, i) => `
                  <circle cx="20" cy="${i * 22 + 10}" r="7" fill="#38bdf8"/>
                  <circle cx="45" cy="${i * 22 + 10}" r="7" fill="#38bdf8"/>
                `).join('')}
                ${num1 % 2 !== 0 ? `
                  <circle cx="20" cy="${Math.floor(num1 / 2) * 22 + 10}" r="7" fill="#ef4444"/>
                  <text x="65" y="${Math.floor(num1 / 2) * 22 + 14}" fill="#ef4444" font-size="10" font-weight="800">Lonely!</text>
                ` : ''}
              </g>

              <!-- Plus Sign -->
              <text x="155" y="80" fill="#fbbf24" font-size="28" font-weight="900" text-anchor="middle">+</text>

              <!-- Term 2 Card -->
              <rect x="180" y="0" width="130" height="150" rx="10" fill="#111827" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="245" y="24" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">
                ${num2 % 2 === 0 ? 'EVEN' : 'ODD'} (${num2})
              </text>
              <g transform="translate(195, 40)">
                ${Array.from({ length: Math.floor(num2 / 2) }).map((_, i) => `
                  <circle cx="20" cy="${i * 22 + 10}" r="7" fill="#fbbf24"/>
                  <circle cx="45" cy="${i * 22 + 10}" r="7" fill="#fbbf24"/>
                `).join('')}
                ${num2 % 2 !== 0 ? `
                  <circle cx="20" cy="${Math.floor(num2 / 2) * 22 + 10}" r="7" fill="#ef4444"/>
                  <text x="65" y="${Math.floor(num2 / 2) * 22 + 14}" fill="#ef4444" font-size="10" font-weight="800">Lonely!</text>
                ` : ''}
              </g>

              <!-- Equals Sign -->
              <text x="335" y="80" fill="#10b981" font-size="28" font-weight="900" text-anchor="middle">=</text>

              <!-- Result Card -->
              <rect x="360" y="0" width="100" height="150" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
              <text x="410" y="24" fill="#a7f3d0" font-size="11" font-weight="900" text-anchor="middle">SUM: ${sum}</text>
              <text x="410" y="55" fill="#ffffff" font-size="20" font-weight="900" text-anchor="middle">
                ${isResultEven ? 'EVEN' : 'ODD'}
              </text>
              <text x="410" y="85" fill="#6ee7b7" font-size="10" text-anchor="middle">
                ${opType === 'odd_odd' ? '2 Lonely dots joined into 1 pair!' : opType === 'even_even' ? 'All dots paired!' : '1 Dot remains lonely!'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Universal Parity Arithmetic Table:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              • Even + Even = Even &nbsp;|&nbsp; • Odd + Odd = Even &nbsp;|&nbsp; • Even + Odd = Odd
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              • Odd × Odd = Odd &nbsp;|&nbsp; • Even × Any Integer = ALWAYS Even!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem; flex-wrap:wrap;">
          <button class="sim-btn ${opType === 'odd_odd' ? 'active' : ''}" data-op="odd_odd">Odd + Odd = Even (5 + 3 = 8)</button>
          <button class="sim-btn ${opType === 'even_even' ? 'active' : ''}" data-op="even_even">Even + Even = Even (4 + 6 = 10)</button>
          <button class="sim-btn ${opType === 'even_odd' ? 'active' : ''}" data-op="even_odd">Even + Odd = Odd (4 + 5 = 9)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-op]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          opType = e.target.getAttribute('data-op');
          simControls.querySelectorAll('button[data-op]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 5: Parity in Grids & Chessboard Tiling
    function simGridSquaresParity() {
      simHeaderTitle.textContent = "Grid Parity: Checkerboard Coloring & The Mutilated Board";
      let cornersRemoved = false;

      function render() {
        const whiteCount = cornersRemoved ? 30 : 32;
        const blackCount = 32;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${cornersRemoved ? 'Mutilated Board: 30 White & 32 Black Squares ➔ Tiling is IMPOSSIBLE!' : 'Complete 8×8 Chessboard: 32 White & 32 Black Squares (32 Dominoes Fit)'}
            </text>

            <!-- 8x8 Chessboard Grid -->
            <g transform="translate(60, 60)">
              ${Array.from({ length: 8 }).map((_, r) => {
                return Array.from({ length: 8 }).map((_, c) => {
                  const isWhite = (r + c) % 2 === 0;
                  // check if opposite white corners: (0,0) and (7,7)
                  const isRemoved = cornersRemoved && ((r === 0 && c === 0) || (r === 7 && c === 7));
                  if (isRemoved) {
                    return `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="#ef4444" stroke="#475569" stroke-width="0.5"/>
                            <text x="${c * 20 + 10}" y="${r * 20 + 14}" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">✕</text>`;
                  }
                  return `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="${isWhite ? '#f8fafc' : '#334155'}" stroke="#475569" stroke-width="0.5"/>`;
                }).join('');
              }).join('')}
            </g>

            <!-- Domino Card & Statistics -->
            <g transform="translate(260, 60)">
              <rect x="0" y="0" width="220" height="160" rx="10" fill="#111827" stroke="${cornersRemoved ? '#ef4444' : '#10b981'}" stroke-width="2"/>
              <text x="110" y="24" fill="${cornersRemoved ? '#fca5a5' : '#a7f3d0'}" font-size="12" font-weight="900" text-anchor="middle">COLOR PARITY BALANCE</text>

              <!-- Domino sample -->
              <g transform="translate(45, 38)">
                <rect x="0" y="0" width="60" height="26" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <rect x="0" y="0" width="30" height="26" fill="#f8fafc"/>
                <rect x="30" y="0" width="30" height="26" fill="#334155"/>
                <text x="65" y="18" fill="#cbd5e1" font-size="10">1 Domino</text>
              </g>

              <g transform="translate(20, 80)">
                <text x="0" y="16" fill="#cbd5e1" font-size="11">White Squares: <tspan fill="#f8fafc" font-weight="bold">${whiteCount}</tspan></text>
                <text x="0" y="34" fill="#cbd5e1" font-size="11">Black Squares: <tspan fill="#94a3b8" font-weight="bold">${blackCount}</tspan></text>
                <text x="0" y="52" fill="#cbd5e1" font-size="11">Total Squares: <tspan fill="#38bdf8" font-weight="bold">${whiteCount + blackCount}</tspan></text>
                <text x="0" y="70" fill="${cornersRemoved ? '#ef4444' : '#10b981'}" font-size="11" font-weight="900">
                  ${cornersRemoved ? 'IMBALANCE: 30 ≠ 32!' : 'BALANCED: 32 = 32'}
                </text>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Power of Parity Invariants:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Every single 2×1 domino MUST cover exactly 1 white and 1 black square.
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Since 31 dominoes need 31 whites and 31 blacks, 30 whites can NEVER be covered!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn ${!cornersRemoved ? 'active' : ''}" id="fullBoardBtn">Standard 8×8 Board (64 Sq)</button>
          <button class="sim-btn ${cornersRemoved ? 'active' : ''}" id="cutCornersBtn">Cut 2 Opposite Corners (62 Sq)</button>
        </div>
      `;

      simControls.querySelector('#fullBoardBtn').addEventListener('click', () => {
        cornersRemoved = false;
        render();
      });

      simControls.querySelector('#cutCornersBtn').addEventListener('click', () => {
        cornersRemoved = true;
        render();
      });

      render();
    }

    // Slide 6: Algebraic Parity & Collatz 3n+1
    function simAlgebraicParityNthTerm() {
      simHeaderTitle.textContent = "Algebraic Parity & The Famous Collatz 3n + 1 Loop";
      let startNum = 7;

      function getCollatzSequence(start) {
        let seq = [start];
        let cur = start;
        while (cur !== 1 && seq.length < 18) {
          if (cur % 2 === 0) cur = cur / 2;
          else cur = 3 * cur + 1;
          seq.push(cur);
        }
        return seq;
      }

      function render() {
        const seq = getCollatzSequence(startNum);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Collatz Rules: If Even ➔ n/2 &nbsp;|&nbsp; If Odd ➔ 3n + 1 (Start at ${startNum})
            </text>

            <!-- Sequence Stepping Blocks -->
            <g transform="translate(30, 65)">
              <rect x="0" y="0" width="480" height="155" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <g transform="translate(15, 20)">
                ${seq.slice(0, 16).map((num, i) => {
                  const x = (i % 8) * 56;
                  const y = Math.floor(i / 8) * 60;
                  const isEven = (num % 2 === 0);

                  return `
                    <g transform="translate(${x}, ${y})">
                      <rect x="0" y="0" width="50" height="42" rx="6" fill="${isEven ? '#0284c7' : '#d97706'}" stroke="${isEven ? '#38bdf8' : '#fbbf24'}" stroke-width="1.5"/>
                      <text x="25" y="24" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${num}</text>
                      <text x="25" y="36" fill="${isEven ? '#bae6fd' : '#fef08a'}" font-size="8" font-weight="700" text-anchor="middle">${isEven ? 'EVEN' : 'ODD'}</text>
                    </g>
                  `;
                }).join('')}
              </g>

              <text x="240" y="145" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">
                Notice: All numbers eventually plummet into the eternal loop: 4 ➔ 2 ➔ 1!
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Parity Shifts in 3n + 1:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              When n is odd, 3n is odd, so 3n + 1 is GUARANTEED to be even!
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Every odd jump is immediately followed by at least one division by 2.
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Choose Starting Number:</span>
          <input type="range" id="collatzSlider" min="2" max="25" value="${startNum}" style="width:160px; accent-color:#38bdf8; cursor:pointer;">
          <span id="collatzVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">${startNum}</span>
          <button class="sim-btn" data-start="7">Try 7</button>
          <button class="sim-btn" data-start="9">Try 9</button>
          <button class="sim-btn" data-start="12">Try 12</button>
        </div>
      `;

      const slider = simControls.querySelector('#collatzSlider');
      slider.addEventListener('input', (e) => {
        startNum = parseInt(e.target.value);
        simControls.querySelector('#collatzVal').textContent = startNum;
        render();
      });

      simControls.querySelectorAll('button[data-start]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          startNum = parseInt(e.target.getAttribute('data-start'));
          slider.value = startNum;
          simControls.querySelector('#collatzVal').textContent = startNum;
          render();
        });
      });

      render();
    }

    // Slide 7: Explorations in Grids - Magic Square Basics
    function simMagicSquare3x3() {
      simHeaderTitle.textContent = "Magic Squares: The Harmonious 3 × 3 Grid with Sum = 15";
      // Standard Lo Shu grid
      const grid = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
      ];

      function render() {
        const rowSums = grid.map(r => r.reduce((a, b) => a + b, 0));
        const colSums = [0, 1, 2].map(c => grid[0][c] + grid[1][c] + grid[2][c]);
        const diag1 = grid[0][0] + grid[1][1] + grid[2][2];
        const diag2 = grid[0][2] + grid[1][1] + grid[2][0];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              Magic Constant S = 15 &nbsp;|&nbsp; Every Row, Column & Diagonal = 15!
            </text>

            <!-- 3x3 Magic Square Canvas -->
            <g transform="translate(150, 65)">
              <!-- Outer Border -->
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

              ${grid.map((row, r) => row.map((val, c) => `
                <rect x="${c * 60}" y="${r * 60}" width="60" height="60" fill="${val === 5 ? '#0284c7' : '#111827'}" stroke="#334155" stroke-width="1.5"/>
                <text x="${c * 60 + 30}" y="${r * 60 + 38}" fill="${val === 5 ? '#ffffff' : '#f8fafc'}" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              `).join('')).join('')}

              <!-- Row Sum Indicators on Right -->
              ${rowSums.map((sum, r) => `
                <text x="195" y="${r * 60 + 38}" fill="#10b981" font-size="13" font-weight="900">➔ ${sum}</text>
              `).join('')}

              <!-- Column Sum Indicators Below -->
              ${colSums.map((sum, c) => `
                <text x="${c * 60 + 30}" y="205" fill="#10b981" font-size="13" font-weight="900" text-anchor="middle">↓ ${sum}</text>
              `).join('')}

              <!-- Diagonal indicators -->
              <text x="-25" y="-8" fill="#fbbf24" font-size="12" font-weight="900">↘ ${diag1}</text>
              <text x="205" y="-8" fill="#fbbf24" font-size="12" font-weight="900">↙ ${diag2}</text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="260" width="460" height="58" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="280" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Total Sum of Digits 1 to 9 = 45 ➔ 45 ÷ 3 Rows = 15 per Line!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Notice: Even numbers (2, 4, 6, 8) sit in the corners; Odd numbers (1, 3, 7, 9) sit on the edges!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn active" id="inspectLoShuBtn">Standard Lo Shu Square (Digits 1–9)</button>
        </div>
      `;

      render();
    }

    // Slide 8: The Center Cell Rule & Structural Symmetry
    function simMagicSquareCenterRule() {
      simHeaderTitle.textContent = "The Center Cell Rule: Why the Center is ALWAYS S / 3 = 5";
      let rotation = 0; // 0, 90, 180, 270

      function getRotatedGrid(deg) {
        if (deg === 90) return [[8, 3, 4], [1, 5, 9], [6, 7, 2]];
        if (deg === 180) return [[6, 1, 8], [7, 5, 3], [2, 9, 4]];
        if (deg === 270) return [[2, 7, 6], [9, 5, 1], [4, 3, 8]];
        return [[4, 9, 2], [3, 5, 7], [8, 1, 6]];
      }

      function render() {
        const curGrid = getRotatedGrid(rotation);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Center Cell Theorem: Center = Magic Sum / 3 = 15 / 3 = 5 (Rotation: ${rotation}°)
            </text>

            <!-- 3x3 Grid Display -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#111827" stroke="#38bdf8" stroke-width="2"/>

              ${curGrid.map((row, r) => row.map((val, c) => `
                <rect x="${c * 60}" y="${r * 60}" width="60" height="60" fill="${val === 5 ? '#0284c7' : '#1e293b'}" stroke="#334155" stroke-width="1.5"/>
                <text x="${c * 60 + 30}" y="${r * 60 + 38}" fill="${val === 5 ? '#ffffff' : '#f8fafc'}" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              `).join('')).join('')}
            </g>

            <!-- Mathematical Proof Diagram Card on Right -->
            <g transform="translate(260, 65)">
              <rect x="0" y="0" width="220" height="180" rx="10" fill="#111827" stroke="#10b981" stroke-width="1.5"/>
              <text x="110" y="24" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">THE 4-LINE CENTER HUB</text>

              <g transform="translate(15, 36)">
                <text x="0" y="18" fill="#cbd5e1" font-size="10.5">4 Lines pass through center (C):</text>
                <text x="0" y="34" fill="#38bdf8" font-size="10.5">• Row 2 &nbsp;• Col 2 &nbsp;• 2 Diagonals</text>
                <text x="0" y="52" fill="#fbbf24" font-size="10.5">Sum of 4 lines = 4 × 15 = 60</text>
                <text x="0" y="70" fill="#cbd5e1" font-size="10">All 9 cells + 3C = 60</text>
                <text x="0" y="88" fill="#cbd5e1" font-size="10">45 + 3C = 60</text>
                <text x="0" y="108" fill="#10b981" font-size="13" font-weight="900">3C = 15 ➔ C = 5!</text>
              </g>

              <text x="110" y="165" fill="#bae6fd" font-size="10" font-weight="800" text-anchor="middle">
                Center is unshakeable under all rotations!
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="260" width="460" height="58" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="280" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Complementary Pairs with 5:
            </text>
            <text x="270" y="298" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1+9 = 10, 2+8 = 10, 3+7 = 10, 4+6 = 10. Opposites across the center always add up to 10!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${rotation === 0 ? 'active' : ''}" data-rot="0">Rotation: 0°</button>
          <button class="sim-btn ${rotation === 90 ? 'active' : ''}" data-rot="90">Rotate 90°</button>
          <button class="sim-btn ${rotation === 180 ? 'active' : ''}" data-rot="180">Rotate 180°</button>
          <button class="sim-btn ${rotation === 270 ? 'active' : ''}" data-rot="270">Rotate 270°</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-rot]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          rotation = parseInt(e.target.getAttribute('data-rot'));
          simControls.querySelectorAll('button[data-rot]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 9: The Chautīsa Yantra (4x4 Magic Square)
    function simChautisaYantra4x4() {
      simHeaderTitle.textContent = "The Chautīsa Yantra: Khajuraho's 4 × 4 Masterwork of 34";
      let activeHighlight = 'corners'; // 'corners', 'center', 'diagonals', 'quadrants'

      const yantra = [
        [7, 12, 1, 14],
        [2, 13, 8, 11],
        [16, 3, 10, 5],
        [9, 6, 15, 4]
      ];

      function isHighlighted(r, c) {
        if (activeHighlight === 'corners') {
          return (r === 0 || r === 3) && (c === 0 || c === 3);
        }
        if (activeHighlight === 'center') {
          return (r === 1 || r === 2) && (c === 1 || c === 2);
        }
        if (activeHighlight === 'diagonals') {
          return (r === c) || (r + c === 3);
        }
        if (activeHighlight === 'quadrants') {
          return (r < 2 && c < 2); // top-left quadrant sample
        }
        return false;
      }

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="270" y="36" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">
              Khajuraho Temple Inscription (c. 10th Century CE) • Magic Constant = 34
            </text>

            <!-- 4x4 Yantra Grid Canvas -->
            <g transform="translate(70, 60)">
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#111827" stroke="#f59e0b" stroke-width="2"/>

              ${yantra.map((row, r) => row.map((val, c) => {
                const hl = isHighlighted(r, c);
                return `
                  <rect x="${c * 45}" y="${r * 45}" width="45" height="45" fill="${hl ? '#b45309' : '#1e293b'}" stroke="#334155" stroke-width="1.5"/>
                  <text x="${c * 45 + 22.5}" y="${r * 45 + 29}" fill="${hl ? '#fef08a' : '#f8fafc'}" font-size="16" font-weight="900" text-anchor="middle">${val}</text>
                `;
              }).join('')).join('')}
            </g>

            <!-- Symmetry Explanation Card -->
            <g transform="translate(270, 60)">
              <rect x="0" y="0" width="220" height="180" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
              <text x="110" y="24" fill="#a5b4fc" font-size="12" font-weight="900" text-anchor="middle">ACTIVE 34 PATTERN</text>

              <g transform="translate(15, 36)">
                ${activeHighlight === 'corners' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">The 4 Corner Cells:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 14 + 9 + 4 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">Even the outer boundary corners balance to 34!</text>
                ` : activeHighlight === 'center' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">The 4 Center Cells:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">13 + 8 + 3 + 10 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">The central 2×2 hub balances to 34!</text>
                ` : activeHighlight === 'diagonals' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">Both Main Diagonals:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 13 + 10 + 4 = 34</text>
                  <text x="0" y="58" fill="#ffffff" font-size="14" font-weight="900">14 + 8 + 3 + 9 = 34</text>
                ` : `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">Each 2×2 Quadrant:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 12 + 2 + 13 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">Every 2×2 corner block sums to 34!</text>
                `}
              </g>

              <text x="110" y="165" fill="#fef08a" font-size="10" font-weight="800" text-anchor="middle">
                Total sum of 1 to 16 = 136 = 4 × 34
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="255" width="480" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="274" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Pandiagonal Perfection:
            </text>
            <text x="270" y="293" fill="#cbd5e1" font-size="11" text-anchor="middle">
              In this grid, there are over 16 DIFFERENT sub-combinations of 4 numbers that sum to 34!
            </text>
            <text x="270" y="309" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click the buttons below to illuminate each magical pattern!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${activeHighlight === 'corners' ? 'active' : ''}" data-hl="corners">4 Corners (34)</button>
          <button class="sim-btn ${activeHighlight === 'center' ? 'active' : ''}" data-hl="center">4 Center Cells (34)</button>
          <button class="sim-btn ${activeHighlight === 'diagonals' ? 'active' : ''}" data-hl="diagonals">2 Diagonals (34)</button>
          <button class="sim-btn ${activeHighlight === 'quadrants' ? 'active' : ''}" data-hl="quadrants">2×2 Quadrant (34)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-hl]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activeHighlight = e.target.getAttribute('data-hl');
          simControls.querySelectorAll('button[data-hl]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 10: Virahāńka-Fibonacci - Poetic Syllable Origins
    function simVirahankaPoeticMeter() {
      simHeaderTitle.textContent = "Poetic Prosody Origins: Pingala & Virahāńka's Syllable Beats";
      let beats = 4; // 1 to 5

      const patterns = {
        1: [["L"]],
        2: [["L", "L"], ["G"]],
        3: [["L", "L", "L"], ["L", "G"], ["G", "L"]],
        4: [["L", "L", "L", "L"], ["L", "L", "G"], ["L", "G", "L"], ["G", "L", "L"], ["G", "G"]],
        5: [
          ["L","L","L","L","L"], ["L","L","L","G"], ["L","L","G","L"], ["L","G","L","L"],
          ["G","L","L","L"], ["L","G","G"], ["G","L","G"], ["G","G","L"]
        ]
      };

      function render() {
        const list = patterns[beats] || patterns[4];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Virahāńka Prosody: Beats = ${beats} ➔ Exactly ${list.length} Combinations! (F_${beats} = ${list.length})
            </text>

            <!-- Syllable Blocks Display -->
            <g transform="translate(40, 65)">
              <rect x="0" y="0" width="460" height="165" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Legend -->
              <g transform="translate(20, 15)">
                <rect x="0" y="0" width="30" height="18" rx="3" fill="#0284c7"/>
                <text x="15" y="13" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">L</text>
                <text x="36" y="13" fill="#cbd5e1" font-size="10">Laghu (Short = 1 beat)</text>

                <rect x="180" y="0" width="45" height="18" rx="3" fill="#d97706"/>
                <text x="202" y="13" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">G</text>
                <text x="232" y="13" fill="#cbd5e1" font-size="10">Guru (Long = 2 beats)</text>
              </g>

              <!-- Combinations Grid -->
              <g transform="translate(20, 45)">
                ${list.map((comb, idx) => {
                  const x = (idx % 4) * 110;
                  const y = Math.floor(idx / 4) * 50;

                  return `
                    <g transform="translate(${x}, ${y})">
                      <rect x="0" y="0" width="100" height="36" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                      <text x="8" y="22" fill="#94a3b8" font-size="10" font-weight="700">${idx + 1}.</text>
                      <g transform="translate(24, 8)">
                        ${comb.map((s, si) => `
                          <rect x="${si * 22}" y="0" width="${s === 'L' ? 18 : 20}" height="20" rx="3" fill="${s === 'L' ? '#0284c7' : '#d97706'}"/>
                          <text x="${si * 22 + (s === 'L' ? 9 : 10)}" y="14" fill="#ffffff" font-size="10" font-weight="900" text-anchor="middle">${s}</text>
                        `).join('')}
                      </g>
                    </g>
                  `;
                }).join('')}
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Recurrence Origin (c. 700 CE):
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              To form n beats: End with a Laghu (needs n-1 beats) OR end with a Guru (needs n-2 beats).
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Therefore: Ways(n) = Ways(n-1) + Ways(n-2) ➔ The sequence 1, 2, 3, 5, 8, 13 is born!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${beats === 1 ? 'active' : ''}" data-beats="1">1 Beat (1 way)</button>
          <button class="sim-btn ${beats === 2 ? 'active' : ''}" data-beats="2">2 Beats (2 ways)</button>
          <button class="sim-btn ${beats === 3 ? 'active' : ''}" data-beats="3">3 Beats (3 ways)</button>
          <button class="sim-btn ${beats === 4 ? 'active' : ''}" data-beats="4">4 Beats (5 ways)</button>
          <button class="sim-btn ${beats === 5 ? 'active' : ''}" data-beats="5">5 Beats (8 ways)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-beats]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          beats = parseInt(e.target.getAttribute('data-beats'));
          simControls.querySelectorAll('button[data-beats]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 11: The Recurrence Machine & Golden Ratio
    function simFibonacciVirahankaSequence() {
      simHeaderTitle.textContent = "The Additive Machine: Virahāńka Sequence & Golden Ratio";
      let nTerm = 7;

      const seq = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377];

      function render() {
        const val = seq[nTerm - 1];
        const prevVal = seq[nTerm - 2];
        const ratio = (val / prevVal).toFixed(5);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              F_${nTerm} = ${val} &nbsp;|&nbsp; Ratio F_${nTerm} / F_${nTerm - 1} = ${val} / ${prevVal} = ${ratio}
            </text>

            <!-- Recurrence Stepper Display -->
            <g transform="translate(40, 65)">
              <rect x="0" y="0" width="460" height="160" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Preceding Two Terms Adder -->
              <g transform="translate(40, 25)">
                <rect x="0" y="0" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="50" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">F_${nTerm - 2}</text>
                <text x="50" y="44" fill="#38bdf8" font-size="18" font-weight="900" text-anchor="middle">${seq[nTerm - 3] || 1}</text>

                <text x="125" y="35" fill="#f59e0b" font-size="24" font-weight="900" text-anchor="middle">+</text>

                <rect x="150" y="0" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="200" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">F_${nTerm - 1}</text>
                <text x="200" y="44" fill="#38bdf8" font-size="18" font-weight="900" text-anchor="middle">${prevVal}</text>

                <text x="275" y="35" fill="#10b981" font-size="24" font-weight="900" text-anchor="middle">=</text>

                <rect x="300" y="0" width="100" height="55" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                <text x="350" y="20" fill="#a7f3d0" font-size="10" text-anchor="middle">F_${nTerm}</text>
                <text x="350" y="44" fill="#ffffff" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              </g>

              <!-- Golden Ratio Meter -->
              <g transform="translate(40, 105)">
                <text x="0" y="16" fill="#cbd5e1" font-size="11" font-weight="700">Golden Ratio Convergence:</text>
                <text x="220" y="16" fill="#fbbf24" font-size="13" font-weight="900">Φ ≈ 1.618033...</text>
                <rect x="0" y="25" width="380" height="14" rx="7" fill="#1e293b"/>
                <rect x="0" y="25" width="${Math.min(380, (parseFloat(ratio) / 2) * 380)}" height="14" rx="7" fill="#10b981"/>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Recurrence Formula: F_n = F_{n-1} + F_{n-2}
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              As you calculate larger and larger terms, the ratio of successive numbers locks onto 1.618!
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Use the slider below to step through higher terms and watch the ratio stabilize!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Term Number (n):</span>
          <input type="range" id="fibSlider" min="3" max="12" value="${nTerm}" style="width:180px; accent-color:#38bdf8; cursor:pointer;">
          <span id="fibVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">n = ${nTerm}</span>
        </div>
      `;

      const slider = simControls.querySelector('#fibSlider');
      slider.addEventListener('input', (e) => {
        nTerm = parseInt(e.target.value);
        simControls.querySelector('#fibVal').textContent = `n = ${nTerm}`;
        render();
      });

      render();
    }

    // Slide 12: Nature's Spirals & Petals
    function simNaturePetalsSpirals() {
      simHeaderTitle.textContent = "Botanical Gallery: Flower Petal Counts & Sunflower Spirals";
      let activeItem = 'buttercup'; // 'lily', 'buttercup', 'delphinium', 'sunflower'

      const flowers = {
        lily: { name: "Lily / Iris", petals: 3, virahankaIndex: "F_3", desc: "Lilies exhibit 3-fold floral symmetry with exactly 3 petals." },
        buttercup: { name: "Wild Buttercup", petals: 5, virahankaIndex: "F_4", desc: "Buttercups and wild roses almost universally feature 5 golden petals." },
        delphinium: { name: "Delphinium", petals: 8, virahankaIndex: "F_5", desc: "Delphiniums proudly display 8 distinct blooming petals." },
        sunflower: { name: "Sunflower Head", petals: "21 & 34 Spirals", virahankaIndex: "F_7 & F_8", desc: "Interlocking clockwise (21) and counter-clockwise (34) seed spirals pack with 100% space efficiency!" }
      };

      function render() {
        const item = flowers[activeItem];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              ${item.name} ➔ ${item.petals} Petals (${item.virahankaIndex})
            </text>

            <!-- Flower Illustration Display Area -->
            <g transform="translate(60, 60)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Central Flower Canvas -->
              <g transform="translate(140, 85)">
                ${activeItem === 'lily' ? `
                  <!-- 3 Petals at 120 deg -->
                  ${[0, 120, 240].map(deg => `
                    <ellipse cx="0" cy="-35" rx="16" ry="32" fill="#38bdf8" opacity="0.85" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#fbbf24"/>
                ` : activeItem === 'buttercup' ? `
                  <!-- 5 Petals at 72 deg -->
                  ${[0, 72, 144, 216, 288].map(deg => `
                    <ellipse cx="0" cy="-35" rx="18" ry="30" fill="#fbbf24" opacity="0.9" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#f59e0b"/>
                ` : activeItem === 'delphinium' ? `
                  <!-- 8 Petals at 45 deg -->
                  ${[0, 45, 90, 135, 180, 225, 270, 315].map(deg => `
                    <ellipse cx="0" cy="-35" rx="14" ry="28" fill="#818cf8" opacity="0.85" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#fbbf24"/>
                ` : `
                  <!-- Sunflower Spirals -->
                  <circle cx="0" cy="0" r="55" fill="#78350f"/>
                  ${Array.from({ length: 45 }).map((_, i) => {
                    const r = 8 + i * 1.0;
                    const theta = i * 2.39996; // golden angle
                    return `<circle cx="${r * Math.cos(theta)}" cy="${r * Math.sin(theta)}" r="2.5" fill="#fef08a"/>`;
                  }).join('')}
                `}
              </g>

              <!-- Description Box on Right -->
              <g transform="translate(230, 25)">
                <rect x="0" y="0" width="170" height="125" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <text x="85" y="24" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">${item.name}</text>
                <foreignObject x="12" y="32" width="146" height="85">
                  <div xmlns="http://www.w3.org/1999/xhtml" style="color:#cbd5e1; font-size:10.5px; line-height:1.35; text-align:center;">
                    ${item.desc}
                  </div>
                </foreignObject>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              Nature's Mathematical Optimization:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              By rotating each new seed or leaf by the Golden Angle (137.5°), plants avoid overlapping.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              This optimal packing geometry directly generates the Virahāńka sequence in nature!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${activeItem === 'lily' ? 'active' : ''}" data-flower="lily">Lily (3 Petals)</button>
          <button class="sim-btn ${activeItem === 'buttercup' ? 'active' : ''}" data-flower="buttercup">Buttercup (5 Petals)</button>
          <button class="sim-btn ${activeItem === 'delphinium' ? 'active' : ''}" data-flower="delphinium">Delphinium (8 Petals)</button>
          <button class="sim-btn ${activeItem === 'sunflower' ? 'active' : ''}" data-flower="sunflower">Sunflower (21 & 34 Spirals)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-flower]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activeItem = e.target.getAttribute('data-flower');
          simControls.querySelectorAll('button[data-flower]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 13: Virahāńka Sequence Parity Cycle
    function simVirahankaParityCycle() {
      simHeaderTitle.textContent = "The Parity Rhythm: Why Every 3rd Virahāńka Number is Even";
      let testIndex = 9;

      const seq = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233];

      function render() {
        const val = seq[testIndex - 1];
        const isEven = (val % 2 === 0);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Repeating Period-3 Parity Pattern: [ Odd, Odd, Even ] Forever!
            </text>

            <!-- 12-Term Parity Ribbon -->
            <g transform="translate(30, 65)">
              <rect x="0" y="0" width="480" height="160" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <g transform="translate(10, 20)">
                ${seq.map((num, i) => {
                  const ev = (num % 2 === 0);
                  const isSel = (i + 1 === testIndex);
                  const x = i * 38;

                  return `
                    <g transform="translate(${x}, 0)">
                      <rect x="0" y="0" width="34" height="60" rx="6" fill="${ev ? '#0284c7' : '#d97706'}" stroke="${isSel ? '#ffffff' : '#475569'}" stroke-width="${isSel ? 2.5 : 1}"/>
                      <text x="17" y="16" fill="#ffffff" font-size="9" text-anchor="middle">n=${i + 1}</text>
                      <text x="17" y="36" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">${num}</text>
                      <text x="17" y="52" fill="${ev ? '#bae6fd' : '#fef08a'}" font-size="8" font-weight="800" text-anchor="middle">${ev ? 'E' : 'O'}</text>
                    </g>
                  `;
                }).join('')}
              </g>

              <!-- Inspector Card -->
              <rect x="30" y="95" width="420" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
              <text x="240" y="116" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">
                Selected Term F_${testIndex} = ${val} ➔ Parity is <tspan fill="${isEven ? '#38bdf8' : '#fbbf24'}" font-weight="bold">${isEven ? 'EVEN' : 'ODD'}</tspan>
              </text>
              <text x="240" y="134" fill="#94a3b8" font-size="10.5" text-anchor="middle">
                Index ${testIndex} ${testIndex % 3 === 0 ? 'IS a multiple of 3 ➔ GUARANTEED EVEN!' : 'is NOT a multiple of 3 ➔ ODD'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="240" width="480" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Why Every 3rd Term is Even:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Odd + Even = Odd ➔ Even + Odd = Odd ➔ Odd + Odd = EVEN!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Therefore, F_30, F_60, and F_3000 are all guaranteed to be even numbers!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Inspect Term (n):</span>
          <input type="range" id="cycleSlider" min="1" max="12" value="${testIndex}" style="width:180px; accent-color:#38bdf8; cursor:pointer;">
          <span id="cycleVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">n = ${testIndex}</span>
        </div>
      `;

      const slider = simControls.querySelector('#cycleSlider');
      slider.addEventListener('input', (e) => {
        testIndex = parseInt(e.target.value);
        simControls.querySelector('#cycleVal').textContent = `n = ${testIndex}`;
        render();
      });

      render();
    }

    // Slide 14: Digits in Disguise - Cryptarithm Warmup
    function simCryptarithmSingleDigit() {
      simHeaderTitle.textContent = "Cryptarithm Detective: Unmasking AB + B = BC";
      let bVal = 8; // try B = 6, 7, 8, 9

      function render() {
        // A = B - 1 (since carry is 1)
        const aVal = bVal - 1;
        const ab = aVal * 10 + bVal;
        const sum = ab + bVal;
        const cVal = sum % 10;
        const resultBC = bVal * 10 + cVal;

        // check uniqueness: A, B, C distinct
        const isDistinct = (aVal !== bVal) && (bVal !== cVal) && (aVal !== cVal);
        const isValid = isDistinct && (sum === resultBC);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${isValid ? '✔ SOLUTION FOUND: 78 + 8 = 86 (A=7, B=8, C=6 Distinct!)' : `Testing B = ${bVal} ➔ ${ab} + ${bVal} = ${sum} (Check Distinctness)`}
            </text>

            <!-- Column Addition Card -->
            <g transform="translate(100, 60)">
              <rect x="0" y="0" width="340" height="175" rx="10" fill="#111827" stroke="${isValid ? '#10b981' : '#f59e0b'}" stroke-width="2"/>

              <!-- Letters Addition -->
              <g transform="translate(40, 25)">
                <text x="80" y="30" fill="#38bdf8" font-size="28" font-weight="900">A B</text>
                <text x="50" y="65" fill="#f59e0b" font-size="24" font-weight="900">+</text>
                <text x="100" y="65" fill="#f59e0b" font-size="28" font-weight="900">B</text>
                <line x1="40" y1="78" x2="135" y2="78" stroke="#ffffff" stroke-width="2.5"/>
                <text x="80" y="110" fill="#10b981" font-size="28" font-weight="900">B C</text>
              </g>

              <!-- Values Evaluation -->
              <g transform="translate(200, 25)">
                <text x="60" y="30" fill="#cbd5e1" font-size="20" font-weight="800">${aVal} ${bVal}</text>
                <text x="35" y="65" fill="#cbd5e1" font-size="20" font-weight="800">+</text>
                <text x="75" y="65" fill="#cbd5e1" font-size="20" font-weight="800">${bVal}</text>
                <line x1="25" y1="78" x2="105" y2="78" stroke="#94a3b8" stroke-width="2"/>
                <text x="60" y="110" fill="${isValid ? '#34d399' : '#f87171'}" font-size="22" font-weight="900">${sum}</text>
              </g>

              <!-- Status -->
              <text x="170" y="155" fill="${isValid ? '#34d399' : '#fbbf24'}" font-size="11.5" font-weight="800" text-anchor="middle">
                ${isValid ? 'Letters represent unique digits: A=7, B=8, C=6!' : (aVal === cVal ? 'Violation: A and C cannot both be ' + aVal + '!' : 'Testing digits...')}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="250" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="270" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Cryptarithm Deduction Rules:
            </text>
            <text x="270" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1. Each letter is a unique digit 0–9 &nbsp;|&nbsp; 2. Leading digits cannot be zero
            </text>
            <text x="270" y="306" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Since A + carry = B, there must be a carry of 1, meaning B = A + 1!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${bVal === 7 ? 'active' : ''}" data-b="7">Try B = 7 (67 + 7 = 74)</button>
          <button class="sim-btn ${bVal === 8 ? 'active' : ''}" data-b="8">Try B = 8 (78 + 8 = 86) [Solution!]</button>
          <button class="sim-btn ${bVal === 9 ? 'active' : ''}" data-b="9">Try B = 9 (89 + 9 = 98)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-b]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          bVal = parseInt(e.target.getAttribute('data-b'));
          simControls.querySelectorAll('button[data-b]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 15: Classic Alphametic Deduction - SEND + MORE = MONEY
    function simClassicAlphameticDeduction() {
      simHeaderTitle.textContent = "The Master Alphametic: Solving SEND + MORE = MONEY";
      let step = 0; // 0 to 4

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${step === 0 ? 'Dudeney (1924): SEND + MORE = MONEY Puzzle' : step === 1 ? 'Step 1: Carry into 5th column forces M = 1!' : step === 2 ? 'Step 2: S + 1 forces O = 0 and S = 9!' : step === 3 ? 'Step 3: Column carries yield E = 5, N = 6, R = 8!' : 'Solved: 9567 + 1085 = 10652! All digits unique!'}
            </text>

            <!-- Column Addition Display -->
            <g transform="translate(60, 60)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Cryptarithm Letters & Substituted Digits -->
              <g transform="translate(60, 25)">
                <!-- Row 1: SEND -->
                <text x="60" y="25" fill="#38bdf8" font-size="20" font-weight="900">
                  ${step >= 2 ? '9' : 'S'} &nbsp;${step >= 3 ? '5' : 'E'} &nbsp;${step >= 3 ? '6' : 'N'} &nbsp;${step >= 4 ? '7' : 'D'}
                </text>

                <!-- Row 2: MORE -->
                <text x="20" y="60" fill="#f59e0b" font-size="20" font-weight="900">+</text>
                <text x="38" y="60" fill="#f59e0b" font-size="20" font-weight="900">
                  ${step >= 1 ? '1' : 'M'} &nbsp;${step >= 2 ? '0' : 'O'} &nbsp;${step >= 3 ? '8' : 'R'} &nbsp;${step >= 3 ? '5' : 'E'}
                </text>

                <line x1="15" y1="72" x2="185" y2="72" stroke="#ffffff" stroke-width="2"/>

                <!-- Row 3: MONEY -->
                <text x="38" y="105" fill="#10b981" font-size="22" font-weight="900">
                  ${step >= 1 ? '1' : 'M'} &nbsp;${step >= 2 ? '0' : 'O'} &nbsp;${step >= 3 ? '6' : 'N'} &nbsp;${step >= 3 ? '5' : 'E'} &nbsp;${step >= 4 ? '2' : 'Y'}
                </text>
              </g>

              <!-- Step Deduction Description Box on Right -->
              <g transform="translate(260, 20)">
                <rect x="0" y="0" width="145" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
                <text x="72" y="22" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">LOGICAL CLUES</text>
                <foreignObject x="8" y="30" width="130" height="95">
                  <div xmlns="http://www.w3.org/1999/xhtml" style="color:#cbd5e1; font-size:9.5px; line-height:1.3;">
                    ${step === 0 ? 'Adding two 4-digit numbers creates a 5-digit number. Start at the fifth column!' : step === 1 ? 'The carry from two 4-digit numbers can only be 1. Since M ≠ 0, M MUST be 1!' : step === 2 ? 'S + 1 = 10 + O. Since S ≤ 9, O must be 0, and S must be 9!' : step === 3 ? 'With M=1, O=0, S=9, columns deduce E=5, N=6, R=8.' : 'D=7, E=5 forces Y=2. Check: 9567 + 1085 = 10652!'}
                  </div>
                </foreignObject>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Art of Mathematical Deduction:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              No trial-and-error guessing needed! Every digit is forced by carryover constraints.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click the step buttons to watch the puzzle unlock column by column!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">Start</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">1. Find M = 1</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">2. Find O=0, S=9</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">3. Find E, N, R</button>
          <button class="sim-btn ${step === 4 ? 'active' : ''}" data-step="4">4. Complete Solution</button>
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

    // Slide 16: Heritage Review - Meru Prastara (Pingala's Triangle)
    function simHeritageNumberPlay() {
      simHeaderTitle.textContent = "Meru Prastara: Pingala's Ancient Combinatorial Mountain";
      let showFibonacci = false;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="270" y="36" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">
              Acharya Pingala's Meru Prastara (The Staircase of Mount Meru, c. 300 BCE)
            </text>

            <!-- Meru Prastara Pyramid (Pascal's Triangle) -->
            <g transform="translate(270, 65)">
              <!-- Row 0: 1 -->
              <circle cx="0" cy="10" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="0" y="14" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 1: 1 1 -->
              <circle cx="-20" cy="36" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-20" y="40" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="20" cy="36" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="20" y="40" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 2: 1 2 1 -->
              <circle cx="-40" cy="62" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-40" y="66" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="0" cy="62" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="0" y="66" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">2</text>
              <circle cx="40" cy="62" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="40" y="66" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 3: 1 3 3 1 -->
              <circle cx="-60" cy="88" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-60" y="92" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-20" cy="88" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-20" y="92" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">3</text>
              <circle cx="20" cy="88" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="20" y="92" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">3</text>
              <circle cx="60" cy="88" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="60" y="92" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 4: 1 4 6 4 1 -->
              <circle cx="-80" cy="114" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-80" y="118" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-40" cy="114" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-40" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">4</text>
              <circle cx="0" cy="114" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="0" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">6</text>
              <circle cx="40" cy="114" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="40" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">4</text>
              <circle cx="80" cy="114" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="80" y="118" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 5: 1 5 10 10 5 1 -->
              <circle cx="-100" cy="140" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-100" y="144" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-60" cy="140" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-60" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">5</text>
              <circle cx="-20" cy="140" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="-20" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">10</text>
              <circle cx="20" cy="140" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="20" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">10</text>
              <circle cx="60" cy="140" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="60" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">5</text>
              <circle cx="100" cy="140" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="100" y="144" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              ${showFibonacci ? `
                <!-- Shallow Diagonals showing Virahanka numbers -->
                <line x1="-120" y1="140" x2="30" y2="40" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
                <text x="-135" y="145" fill="#f59e0b" font-size="12" font-weight="900">Sum = 8!</text>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="240" width="480" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              1,800 Years Before Pascal:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Halayudha's 10th-century commentary on Pingala gave the rule: add the two numbers above!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Amazingly, summing the shallow diagonals in Meru Prastara generates the Virahāńka sequence!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn ${showFibonacci ? 'active' : ''}" id="toggleFibDiagBtn">
            ${showFibonacci ? 'Hide Shallow Diagonals' : 'Reveal Virahāńka Numbers in Diagonals'}
          </button>
        </div>
      `;

      simControls.querySelector('#toggleFibDiagBtn').addEventListener('click', () => {
        showFibonacci = !showFibonacci;
        render();
      });

      render();
    }
"""
'''

with open('.agents/class7_math_number_play_sims.py', 'w', encoding='utf-8') as f:
    f.write(sims_code)

print("Successfully generated .agents/class7_math_number_play_sims.py")

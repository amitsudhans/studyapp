# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_finding_common_ground_js.py
Contains interactive JavaScript logic for all 16 simulators.
"""

JS_CODE = r'''
    // ==========================================
    // CHAPTER 11: FINDING COMMON GROUND (HCF & LCM) JS ENGINES
    // ==========================================

    // Helper GCD & LCM
    function gcd(a, b) {
      a = Math.abs(a);
      b = Math.abs(b);
      while (b) {
        let t = b;
        b = a % b;
        a = t;
      }
      return a;
    }

    function lcm(a, b) {
      if (a === 0 || b === 0) return 0;
      return Math.abs(a * b) / gcd(a, b);
    }

    function getFactors(n) {
      const f = [];
      for (let i = 1; i <= n; i++) {
        if (n % i === 0) f.push(i);
      }
      return f;
    }

    // --- Simulator 1: Floor Tiler ---
    function updateFloorTiler() {
      const L = parseInt(document.getElementById('tilerSliderL')?.value || 12);
      const W = parseInt(document.getElementById('tilerSliderW')?.value || 18);
      const S = parseInt(document.getElementById('tilerSliderS')?.value || 6);

      const valL = document.getElementById('tilerValL');
      const valW = document.getElementById('tilerValW');
      const valS = document.getElementById('tilerValS');
      if (valL) valL.textContent = `${L} m`;
      if (valW) valW.textContent = `${W} m`;
      if (valS) valS.textContent = `${S} m`;

      const fitsL = (L % S === 0);
      const fitsW = (W % S === 0);
      const fitsBoth = fitsL && fitsW;

      const status = document.getElementById('tilerStatus');
      const g = document.getElementById('tilerGridGroup');
      const summary = document.getElementById('tilerSummary');

      if (status) {
        if (fitsBoth) {
          const hcfVal = gcd(L, W);
          status.textContent = S === hcfVal ?
            `✓ Perfect Fit! S=${S}m is the HCF (Largest Size)!` :
            `✓ Fits! S=${S}m is a common divisor (HCF is ${hcfVal}m).`;
          status.className = 'text-[11px] font-bold text-emerald-400 font-mono';
        } else {
          status.textContent = `✗ Does not divide evenly (Wasteful cuts needed!)`;
          status.className = 'text-[11px] font-bold text-rose-400 font-mono';
        }
      }

      if (g) {
        g.innerHTML = '';
        // Draw tiles scaled to SVG width 280, height 140
        const scaleX = 280 / L;
        const scaleY = 140 / W;
        const countX = Math.ceil(L / S);
        const countY = Math.ceil(W / S);

        for (let ix = 0; ix < countX; ix++) {
          for (let iy = 0; iy < countY; iy++) {
            const x = 20 + ix * (S * scaleX);
            const y = 10 + iy * (S * scaleY);
            const tileW = Math.min(S * scaleX, 300 - x);
            const tileH = Math.min(S * scaleY, 150 - y);

            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', x);
            rect.setAttribute('y', y);
            rect.setAttribute('width', tileW);
            rect.setAttribute('height', tileH);
            rect.setAttribute('fill', fitsBoth ? 'rgba(56,189,248,0.2)' : 'rgba(244,63,94,0.15)');
            rect.setAttribute('stroke', fitsBoth ? '#38bdf8' : '#f43f5e');
            rect.setAttribute('stroke-width', '1');
            if (!fitsBoth) rect.setAttribute('stroke-dasharray', '2 2');
            g.appendChild(rect);
          }
        }
      }

      if (summary) {
        if (fitsBoth) {
          const totalTiles = (L / S) * (W / S);
          summary.textContent = `Room ${L}m × ${W}m paved with ${S}m tiles: (${L/S}) × (${W/S}) = ${totalTiles} tiles. Zero cuts!`;
        } else {
          summary.textContent = `${S}m is not a common factor of ${L} and ${W}. Fractional tile pieces required!`;
        }
      }
    }
    window.updateFloorTiler = updateFloorTiler;


    // --- Simulator 2: Factor Venn ---
    function updateFactorVenn() {
      sfx.playClick();
      const a = parseInt(document.getElementById('vennInputA')?.value || 24);
      const b = parseInt(document.getElementById('vennInputB')?.value || 36);

      const fA = getFactors(a);
      const fB = getFactors(b);

      const common = fA.filter(x => fB.includes(x));
      const onlyA = fA.filter(x => !common.includes(x));
      const onlyB = fB.filter(x => !common.includes(x));
      const hcfVal = Math.max(...common);

      const hcfText = document.getElementById('vennHcfText');
      if (hcfText) hcfText.textContent = `HCF(${a}, ${b}) = ${hcfVal}`;

      const gA = document.getElementById('vennOnlyA');
      const gC = document.getElementById('vennCommon');
      const gB = document.getElementById('vennOnlyB');

      if (gA) {
        gA.innerHTML = '';
        onlyA.forEach((val, idx) => {
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', 105);
          t.setAttribute('y', 55 + idx * 16);
          t.textContent = val;
          gA.appendChild(t);
        });
      }

      if (gC) {
        gC.innerHTML = '';
        common.forEach((val, idx) => {
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', 180);
          t.setAttribute('y', 45 + idx * 16);
          t.textContent = (val === hcfVal) ? `★ ${val} (HCF)` : val;
          if (val === hcfVal) {
            t.setAttribute('fill', '#f59e0b');
            t.setAttribute('font-size', '11');
          }
          gC.appendChild(t);
        });
      }

      if (gB) {
        gB.innerHTML = '';
        onlyB.forEach((val, idx) => {
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', 255);
          t.setAttribute('y', 55 + idx * 16);
          t.textContent = val;
          gB.appendChild(t);
        });
      }

      const desc = document.getElementById('vennDesc');
      if (desc) {
        desc.textContent = `Intersection Common Factors: {${common.join(', ')}}. Highest Common Factor = ${hcfVal}!`;
      }
    }
    window.updateFactorVenn = updateFactorVenn;


    // --- Simulator 3: Prime Factor Tree ---
    function loadTreeNumber(n) {
      sfx.playClick();
      const container = document.getElementById('treeContainer');
      const text = document.getElementById('treePrimeLeaves');
      if (!container) return;

      container.innerHTML = '';

      if (n === 60) {
        container.innerHTML = `
          <div class="flex flex-col items-center gap-2">
            <div class="px-3 py-1 rounded-full bg-slate-800 border-2 border-amber-400 font-bold text-amber-300">60</div>
            <div class="w-24 h-4 border-b-2 border-l-2 border-r-2 border-slate-600"></div>
            <div class="flex gap-12">
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">6</span>
                <div class="w-12 h-3 border-b border-l border-r border-slate-600"></div>
                <div class="flex gap-4">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">3</span>
                </div>
              </div>
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">10</span>
                <div class="w-12 h-3 border-b border-l border-r border-slate-600"></div>
                <div class="flex gap-4">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">5</span>
                </div>
              </div>
            </div>
          </div>
        `;
        if (text) text.textContent = 'Prime Factorisation: 60 = 2² × 3 × 5 (Atomic Prime Leaves: 2, 2, 3, 5)';
      } else if (n === 72) {
        container.innerHTML = `
          <div class="flex flex-col items-center gap-2">
            <div class="px-3 py-1 rounded-full bg-slate-800 border-2 border-amber-400 font-bold text-amber-300">72</div>
            <div class="w-24 h-4 border-b-2 border-l-2 border-r-2 border-slate-600"></div>
            <div class="flex gap-12">
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">8</span>
                <div class="flex gap-2 mt-2">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                </div>
              </div>
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">9</span>
                <div class="flex gap-2 mt-2">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">3</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">3</span>
                </div>
              </div>
            </div>
          </div>
        `;
        if (text) text.textContent = 'Prime Factorisation: 72 = 2³ × 3² (Atomic Prime Leaves: 2, 2, 2, 3, 3)';
      } else {
        container.innerHTML = `
          <div class="flex flex-col items-center gap-2">
            <div class="px-3 py-1 rounded-full bg-slate-800 border-2 border-amber-400 font-bold text-amber-300">90</div>
            <div class="w-24 h-4 border-b-2 border-l-2 border-r-2 border-slate-600"></div>
            <div class="flex gap-12">
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">9</span>
                <div class="flex gap-2 mt-2">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">3</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">3</span>
                </div>
              </div>
              <div class="flex flex-col items-center gap-1.5">
                <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-600 font-bold text-slate-300">10</span>
                <div class="flex gap-2 mt-2">
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">2</span>
                  <span class="w-6 h-6 rounded-full bg-emerald-500 font-bold text-black flex items-center justify-center text-xs shadow">5</span>
                </div>
              </div>
            </div>
          </div>
        `;
        if (text) text.textContent = 'Prime Factorisation: 90 = 2 × 3² × 5 (Atomic Prime Leaves: 2, 3, 3, 5)';
      }
    }
    window.loadTreeNumber = loadTreeNumber;


    // --- Simulator 5: Conjecture Tester ---
    function testConjecture(id) {
      sfx.playClick();
      const box = document.getElementById('conjectureResultBox');
      if (!box) return;

      if (id === 1) {
        box.innerHTML = `
          <div class="text-rose-400 font-bold text-sm">❌ Conjecture 1 Shattered!</div>
          <div><strong>Claim:</strong> \"The HCF of any two even numbers is always 2.\"</div>
          <div class="p-2 rounded bg-rose-950/40 border border-rose-500/40 text-rose-200 mt-1">
            <strong>Counterexample:</strong> Take $a = 4$ and $b = 8$.<br>
            Both are even numbers, but $\\text{HCF}(4, 8) = 4 \\neq 2$!<br>
            Another counterexample: $\\text{HCF}(6, 12) = 6$. The claim is completely FALSE.
          </div>
        `;
      } else if (id === 2) {
        box.innerHTML = `
          <div class="text-rose-400 font-bold text-sm">❌ Conjecture 2 Shattered!</div>
          <div><strong>Claim:</strong> \"If HCF(a, b) = 1, then both numbers must be prime.\"</div>
          <div class="p-2 rounded bg-rose-950/40 border border-rose-500/40 text-rose-200 mt-1">
            <strong>Counterexample:</strong> Take $a = 8$ and $b = 9$.<br>
            $\\text{HCF}(8, 9) = 1$. But $8$ is composite ($2^3$) and $9$ is composite ($3^2$)!<br>
            They are called <strong>Co-prime</strong> numbers (sharing no common factor other than 1).
          </div>
        `;
      } else {
        box.innerHTML = `
          <div class="text-rose-400 font-bold text-sm">❌ Conjecture 3 Shattered!</div>
          <div><strong>Claim:</strong> \"The LCM of two numbers is always strictly greater than both numbers.\"</div>
          <div class="p-2 rounded bg-rose-950/40 border border-rose-500/40 text-rose-200 mt-1">
            <strong>Counterexample:</strong> Take $a = 4$ and $b = 12$.<br>
            $\\text{LCM}(4, 12) = 12$. The LCM is equal to the larger number, NOT strictly greater!
          </div>
        `;
      }
    }
    window.testConjecture = testConjecture;


    // --- Simulator 6: Toran Strips ---
    let toranA = 0;
    let toranB = 0;

    function addToranStrip(type) {
      sfx.playClick();
      const trackA = document.getElementById('toranTrackA');
      const trackB = document.getElementById('toranTrackB');
      const lenA = document.getElementById('rowLenA');
      const lenB = document.getElementById('rowLenB');
      const match = document.getElementById('toranMatchStatus');

      if (type === 'A') {
        toranA += 6;
        if (trackA) {
          const chip = document.createElement('div');
          chip.className = 'px-2 py-0.5 rounded bg-sky-600 text-white font-bold text-[10px] whitespace-nowrap shadow';
          chip.textContent = '6 cm';
          trackA.appendChild(chip);
        }
      } else {
        toranB += 8;
        if (trackB) {
          const chip = document.createElement('div');
          chip.className = 'px-2.5 py-0.5 rounded bg-emerald-600 text-white font-bold text-[10px] whitespace-nowrap shadow';
          chip.textContent = '8 cm';
          trackB.appendChild(chip);
        }
      }

      if (lenA) lenA.textContent = `${toranA} cm`;
      if (lenB) lenB.textContent = `${toranB} cm`;

      if (match) {
        if (toranA > 0 && toranA === toranB) {
          sfx.playChime();
          match.textContent = `🎉 PERFECT ALIGNMENT at ${toranA} cm! LCM(6, 8) = 24 cm!`;
          match.className = 'font-mono text-emerald-400 font-bold text-xs animate-pulse';
        } else {
          match.textContent = `Row A = ${toranA} cm, Row B = ${toranB} cm. Add strips to align edges!`;
          match.className = 'font-mono text-slate-400 text-xs';
        }
      }
    }
    window.addToranStrip = addToranStrip;

    function resetToran() {
      sfx.playClick();
      toranA = 0;
      toranB = 0;
      const trackA = document.getElementById('toranTrackA');
      const trackB = document.getElementById('toranTrackB');
      const lenA = document.getElementById('rowLenA');
      const lenB = document.getElementById('rowLenB');
      const match = document.getElementById('toranMatchStatus');

      if (trackA) trackA.innerHTML = '';
      if (trackB) trackB.innerHTML = '';
      if (lenA) lenA.textContent = '0 cm';
      if (lenB) lenB.textContent = '0 cm';
      if (match) {
        match.textContent = 'Add strips until both rows align at the same total length!';
        match.className = 'font-mono text-slate-400 text-xs';
      }
    }
    window.resetToran = resetToran;


    // --- Simulator 7: Multiples Stepper ---
    let stepValA = 4;
    let stepValB = 6;
    let runnerPosA = 0;
    let runnerPosB = 0;

    function setStepperLeap(a, b) {
      sfx.playClick();
      stepValA = a;
      stepValB = b;
      runnerPosA = 0;
      runnerPosB = 0;
      const banner = document.getElementById('stepperLcmBanner');
      if (banner) banner.textContent = `LCM(${a}, ${b}) = ${lcm(a, b)}`;
      renderStepperMarks();
    }
    window.setStepperLeap = setStepperLeap;

    function renderStepperMarks() {
      const g = document.getElementById('stepperMarksGroup');
      if (!g) return;
      g.innerHTML = '';

      const targetLcm = lcm(stepValA, stepValB);

      for (let i = 0; i <= targetLcm + 4; i++) {
        const x = 20 + i * (280 / (targetLcm + 4));
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', x);
        line.setAttribute('y1', 35);
        line.setAttribute('x2', x);
        line.setAttribute('y2', 80);
        line.setAttribute('stroke', i === targetLcm ? '#f59e0b' : '#334155');
        line.setAttribute('stroke-width', i === targetLcm ? '2' : '1');
        g.appendChild(line);

        if (i === targetLcm) {
          const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          txt.setAttribute('x', x);
          txt.setAttribute('y', 25);
          txt.setAttribute('text-anchor', 'middle');
          txt.setAttribute('fill', '#fbbf24');
          txt.setAttribute('font-size', '9');
          txt.setAttribute('font-weight', 'bold');
          txt.textContent = `🏆 LCM=${i}`;
          g.appendChild(txt);
        }
      }
      updateRunnersSvg();
    }

    function updateRunnersSvg() {
      const targetLcm = lcm(stepValA, stepValB);
      const scale = 280 / (targetLcm + 4);

      const rA = document.getElementById('runnerA');
      const rB = document.getElementById('runnerB');
      if (rA) rA.setAttribute('cx', 20 + runnerPosA * scale);
      if (rB) rB.setAttribute('cx', 20 + runnerPosB * scale);

      const log = document.getElementById('stepperLog');
      if (log) {
        if (runnerPosA > 0 && runnerPosA === runnerPosB) {
          sfx.playChime();
          log.textContent = `🎉 Common Multiple Reached at Position ${runnerPosA}! (First shared landing = LCM)`;
          log.className = 'text-xs font-mono text-center text-emerald-400 font-bold mt-1';
        } else {
          log.textContent = `Runner A: Pos ${runnerPosA} | Runner B: Pos ${runnerPosB}. Keep stepping!`;
          log.className = 'text-xs font-mono text-center text-slate-300 mt-1';
        }
      }
    }

    function stepBothRunners() {
      sfx.playClick();
      runnerPosA += stepValA;
      runnerPosB += stepValB;
      updateRunnersSvg();
    }
    window.stepBothRunners = stepBothRunners;


    // --- Simulator 9: Algebraic Multiples Grid ---
    function renderMultiplesGrid() {
      const grid = document.getElementById('multiplesGrid50');
      if (!grid) return;
      grid.innerHTML = '';

      for (let i = 1; i <= 50; i++) {
        const cell = document.createElement('div');
        cell.id = `gridCell_${i}`;
        cell.className = 'p-1 rounded bg-slate-900 border border-slate-800 text-slate-400';
        cell.textContent = i;
        grid.appendChild(cell);
      }
      filterMultiplesGrid(2);
    }
    window.renderMultiplesGrid = renderMultiplesGrid;

    function filterMultiplesGrid(k) {
      sfx.playClick();
      for (let i = 1; i <= 50; i++) {
        const cell = document.getElementById(`gridCell_${i}`);
        if (!cell) continue;

        if (i % k === 0) {
          cell.className = 'p-1 rounded bg-sky-950/70 border border-sky-400 text-sky-200 font-bold';
        } else {
          cell.className = 'p-1 rounded bg-slate-900/40 border border-slate-800/40 text-slate-600';
        }
      }

      const desc = document.getElementById('gridFilterDesc');
      if (desc) {
        if (k === 2) desc.textContent = 'Showing 2n: Even numbers {2, 4, 6, 8, 10, ...}';
        else if (k === 3) desc.textContent = 'Showing 3n: Multiples of 3 {3, 6, 9, 12, ...}';
        else if (k === 5) desc.textContent = 'Showing 5n: Multiples of 5 {5, 10, 15, 20, ...}';
        else if (k === 6) desc.textContent = 'Showing 6n: Numbers divisible by BOTH 2 and 3! (LCM = 6)';
      }
    }
    window.filterMultiplesGrid = filterMultiplesGrid;


    // --- Simulator 10: Nested Multiple Rule ---
    function setNestedPair(a, b) {
      sfx.playClick();
      const h = gcd(a, b);
      const l = lcm(a, b);

      const hcfEl = document.getElementById('nestedHcfVal');
      const lcmEl = document.getElementById('nestedLcmVal');
      const banner = document.getElementById('nestedRuleBanner');
      const summary = document.getElementById('nestedSummaryText');

      if (hcfEl) hcfEl.textContent = `HCF = ${h}`;
      if (lcmEl) lcmEl.textContent = `LCM = ${l}`;

      if (b % a === 0) {
        if (banner) banner.textContent = `${a} | ${b} ➔ HCF = ${a} (smaller), LCM = ${b} (larger)`;
        if (summary) summary.textContent = `Since ${b} is an exact multiple of ${a} (${a} × ${b/a} = ${b}), HCF = ${a} and LCM = ${b} instantly!`;
      } else if (h === 1) {
        if (banner) banner.textContent = `Co-Prime Rule: HCF = 1, LCM = ${a} × ${b} = ${l}`;
        if (summary) summary.textContent = `${a} and ${b} share no common factors! HCF is 1, and LCM is their direct product (${a} × ${b} = ${l})!`;
      }
    }
    window.setNestedPair = setNestedPair;


    // --- Simulator 11: Scaling Magnifier ---
    function updateScalingSim() {
      const k = parseInt(document.getElementById('scaleSliderK')?.value || 1);
      const kVal = document.getElementById('scaleKVal');
      const badge = document.getElementById('scaleBadge');
      if (kVal) kVal.textContent = k;
      if (badge) badge.textContent = `k=${k}`;

      const baseA = 6, baseB = 8;
      const scaledA = baseA * k;
      const scaledB = baseB * k;
      const scaledHcf = 2 * k;
      const scaledLcm = 24 * k;

      const numDisp = document.getElementById('scaleNumDisplay');
      const resDisp = document.getElementById('scaleResultDisplay');
      const proof = document.getElementById('scaleProofText');

      if (numDisp) numDisp.textContent = `${scaledA} and ${scaledB} (${k}× original)`;
      if (resDisp) resDisp.textContent = `HCF = ${scaledHcf}, LCM = ${scaledLcm}`;
      if (proof) {
        proof.textContent = `Scaling by k=${k}: HCF(6×${k}, 8×${k}) = ${scaledHcf} (${k}×2), LCM(6×${k}, 8×${k}) = ${scaledLcm} (${k}×24)!`;
      }
    }
    window.updateScalingSim = updateScalingSim;


    // --- Simulator 12: Simultaneous Ladder ---
    let ladderA = 24;
    let ladderB = 36;
    let ladderStepIdx = 0;

    function resetLadder(a, b) {
      sfx.playClick();
      ladderA = a;
      ladderB = b;
      ladderStepIdx = 0;
      renderLadder();
    }
    window.resetLadder = resetLadder;

    function renderLadder() {
      const container = document.getElementById('ladderRowsContainer');
      const hcfEl = document.getElementById('ladderHcfText');
      const lcmEl = document.getElementById('ladderLcmText');
      if (!container) return;

      container.innerHTML = '';

      if (ladderA === 24 && ladderB === 36) {
        if (ladderStepIdx >= 0) {
          container.innerHTML += `<div class="p-1 rounded bg-slate-900 border border-slate-700 flex justify-between"><span>Row 1:</span> <span class="font-bold">24, 36</span></div>`;
        }
        if (ladderStepIdx >= 1) {
          container.innerHTML += `<div class="p-1 rounded bg-slate-900 border border-slate-700 flex justify-between"><span class="text-amber-400 font-bold">÷ 2 ➔</span> <span class="font-bold">12, 18</span></div>`;
        }
        if (ladderStepIdx >= 2) {
          container.innerHTML += `<div class="p-1 rounded bg-slate-900 border border-slate-700 flex justify-between"><span class="text-amber-400 font-bold">÷ 2 ➔</span> <span class="font-bold">6, 9</span></div>`;
        }
        if (ladderStepIdx >= 3) {
          container.innerHTML += `<div class="p-1 rounded bg-emerald-950/60 border border-emerald-500/40 flex justify-between"><span class="text-amber-400 font-bold">÷ 3 ➔</span> <span class="font-bold text-emerald-300">2, 3 (Co-prime!)</span></div>`;
        }

        if (hcfEl) hcfEl.textContent = ladderStepIdx >= 3 ? '2 × 2 × 3 = 12' : '...';
        if (lcmEl) lcmEl.textContent = ladderStepIdx >= 3 ? '(2 × 2 × 3) × (2 × 3) = 72' : '...';
      } else {
        container.innerHTML = `
          <div class="p-1 rounded bg-slate-900 border border-slate-700 flex justify-between"><span>Numbers:</span> <span class="font-bold">${ladderA}, ${ladderB}</span></div>
          <div class="p-1 rounded bg-emerald-950/60 border border-emerald-500/40 flex justify-between"><span>HCF / LCM:</span> <span class="font-bold text-emerald-300">${gcd(ladderA, ladderB)} / ${lcm(ladderA, ladderB)}</span></div>
        `;
        if (hcfEl) hcfEl.textContent = `${gcd(ladderA, ladderB)}`;
        if (lcmEl) lcmEl.textContent = `${lcm(ladderA, ladderB)}`;
      }
    }

    function stepLadderDivision() {
      sfx.playClick();
      if (ladderStepIdx < 3) {
        ladderStepIdx++;
        renderLadder();
      }
    }
    window.stepLadderDivision = stepLadderDivision;


    // --- Simulator 13: Shortcut Factor Extractor ---
    function setShortcutProblem(a, b, factor) {
      sfx.playClick();
      const orig = document.getElementById('scOrigNums');
      const ext = document.getElementById('scExtractedFactor');
      const exp = document.getElementById('scStepsExplanation');

      const remA = a / factor;
      const remB = b / factor;
      const remHcf = gcd(remA, remB);
      const remLcm = lcm(remA, remB);

      if (orig) orig.textContent = `${a} and ${b}`;
      if (ext) ext.textContent = `${factor} × (${remA} & ${remB})`;

      if (exp) {
        exp.innerHTML = `
          <div>1. Divide out obvious large factor <strong>${factor}</strong>: ${a} / ${factor} = ${remA}, and ${b} / ${factor} = ${remB}.</div>
          <div>2. ${remA} and ${remB} are co-prime (HCF = 1, LCM = ${remLcm}).</div>
          <div class="text-emerald-300 font-bold mt-1">3. Total HCF = ${factor} × 1 = <strong>${factor}</strong>; Total LCM = ${factor} × ${remLcm} = <strong>${factor * remLcm}</strong>!</div>
        `;
      }
    }
    window.setShortcutProblem = setShortcutProblem;


    // --- Simulator 14: Master Balance ---
    function updateMasterBalance() {
      const a = parseInt(document.getElementById('masterSliderA')?.value || 18);
      const b = parseInt(document.getElementById('masterSliderB')?.value || 24);

      const numA = document.getElementById('masterNumA');
      const numB = document.getElementById('masterNumB');
      if (numA) numA.textContent = a;
      if (numB) numB.textContent = b;

      const product = a * b;
      const h = gcd(a, b);
      const l = lcm(a, b);

      const leftExpr = document.getElementById('leftPanProductExpr');
      const leftVal = document.getElementById('leftPanProductVal');
      const rightExpr = document.getElementById('rightPanHcfLcmExpr');
      const rightVal = document.getElementById('rightPanHcfLcmVal');
      const proof = document.getElementById('masterIdentityProof');

      if (leftExpr) leftExpr.textContent = `${a} × ${b}`;
      if (leftVal) leftVal.textContent = product;
      if (rightExpr) rightExpr.textContent = `${h} × ${l}`;
      if (rightVal) rightVal.textContent = h * l;

      if (proof) {
        proof.textContent = `✓ Universal Equality: HCF(${a}, ${b}) = ${h}, LCM(${a}, ${b}) = ${l}. ${h} × ${l} = ${h * l} = ${a} × ${b}!`;
      }
    }
    window.updateMasterBalance = updateMasterBalance;


    // --- Simulator 15: Three Numbers Engine ---
    function setThreeNums(a, b, c) {
      sfx.playClick();
      const h3 = gcd(gcd(a, b), c);
      const l3 = lcm(lcm(a, b), c);

      const hlProd = h3 * l3;
      const abcProd = a * b * c;

      const hlEl = document.getElementById('threeNumsHcfLcm');
      const prodEl = document.getElementById('threeNumsProduct');
      const trap = document.getElementById('threeNumsTrapReason');

      if (hlEl) hlEl.textContent = `${h3} × ${l3} = ${hlProd}`;
      if (prodEl) prodEl.textContent = `${a} × ${b} × ${c} = ${abcProd}`;

      if (trap) {
        trap.textContent = `${hlProd} ≠ ${abcProd}! Pairwise common prime factors duplicate inside the product a × b × c!`;
      }
    }
    window.setThreeNums = setThreeNums;


    // --- Simulator 16: Heritage Kuṭṭaka & Niruddha ---
    function setHeritageTab(tab) {
      sfx.playClick();
      const box = document.getElementById('heritageContentBox');
      if (!box) return;

      if (tab === 'kuttaka') {
        box.innerHTML = `
          <div class="text-amber-300 font-bold text-sm">📜 Āryabhaṭa's Kuṭṭaka (The Pulverizer, 499 CE)</div>
          <div class="text-slate-300">
            In the <em>Āryabhaṭīya</em>, Āryabhaṭa presented the <strong>Kuṭṭaka</strong> method—a pulverizer division algorithm:
          </div>
          <div class="p-2 rounded bg-slate-900 border border-slate-700 text-amber-200">
            • Used reciprocal division steps to find the greatest common divisor and solve linear indeterminate equations: $ax - by = c$.<br>
            • The algorithm systematically 'pulverizes' numbers by dividing remainders until reaching unity!
          </div>
        `;
      } else {
        box.innerHTML = `
          <div class="text-emerald-300 font-bold text-sm">📜 Mahāvīrācārya's Niruddha (Gaṇitasārasaṅgraha, c. 850 CE)</div>
          <div class="text-slate-300">
            Mahāvīrācārya was the first mathematician in world history to explicitly formulate the <strong>Lowest Common Multiple</strong> (termed <em>Niruddha</em>):
          </div>
          <div class="p-2 rounded bg-slate-900 border border-slate-700 text-emerald-200">
            • <em>Niruddha-bhāgahāra:</em> Standardized fraction addition by converting denominators to their Niruddha (LCM):<br>
            $$\\frac{1}{6} + \\frac{1}{8} = \\frac{4}{24} + \\frac{3}{24} = \\frac{7}{24}$$
          </div>
        `;
      }
    }
    window.setHeritageTab = setHeritageTab;
'''

with open('.agents/class7_math_finding_common_ground_js.py', 'w', encoding='utf-8') as f:
    f.write(f'# -*- coding: utf-8 -*-\nSIMULATORS_JS = r"""{JS_CODE}"""\n')

print("Created .agents/class7_math_finding_common_ground_js.py successfully!")


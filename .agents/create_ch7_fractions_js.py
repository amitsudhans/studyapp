# -*- coding: utf-8 -*-
"""
Interactive JavaScript Logic for NCERT Class 6 Mathematics Chapter 7: Fractions
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, etc.).
Clean Unicode everywhere (1/2, 3/4, 5/2, 1 1/2, ×, ÷, +, −, etc.).
"""

JS_CODE = r"""
let currentSlide = 1;
const totalSlides = 20;
let audioEnabled = false;
let synth = window.speechSynthesis;
let currentUtterance = null;

// Audio toggle
function toggleAudio() {
    audioEnabled = !audioEnabled;
    const btn = document.getElementById('muteBtn');
    if (audioEnabled) {
        btn.innerHTML = '🔊';
        btn.classList.add('text-amber-400');
        speakCurrentSlide();
    } else {
        btn.innerHTML = '🔇';
        btn.classList.remove('text-amber-400');
        if (synth) synth.cancel();
    }
}

function speakCurrentSlide() {
    if (!audioEnabled || !synth) return;
    synth.cancel();
    const activeSlide = document.getElementById(`slide-${currentSlide}`);
    if (!activeSlide) return;
    const summary = activeSlide.querySelector('.slide-summary');
    const textToSpeak = summary ? summary.textContent.trim() : "";
    if (!textToSpeak) return;

    currentUtterance = new SpeechSynthesisUtterance(textToSpeak);
    currentUtterance.rate = 0.95;
    currentUtterance.pitch = 1.0;
    synth.speak(currentUtterance);
}

// Slide Navigation
function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));

    const target = document.getElementById(`slide-${n}`);
    if (target) {
        target.classList.remove('hidden');
        currentSlide = n;
    }

    // Update Counter & Progress
    const counter = document.getElementById('slideCounter');
    if (counter) counter.textContent = `${currentSlide} / ${totalSlides}`;

    const progressBar = document.getElementById('progressBar');
    if (progressBar) progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;

    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);

    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    // Terminal Slide Requirement
    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastSlideNotice) lastSlideNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastSlideNotice) lastSlideNotice.style.display = 'none';
    }

    if (audioEnabled) speakCurrentSlide();

    // Trigger simulator initializations
    setTimeout(initCurrentSimulator, 50);
}

function nextSlide() {
    if (currentSlide < totalSlides) goToSlide(currentSlide + 1);
}

function prevSlide() {
    if (currentSlide > 1) goToSlide(currentSlide - 1);
}

// Checkpoint Answer Checker
function checkAnswer(cpId, selectedIdx, correctIdx, explanation) {
    const card = document.getElementById(cpId);
    if (!card) return;
    const btns = card.querySelectorAll('.option-btn');
    const feedback = card.querySelector('.checkpoint-feedback');

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        btn.classList.remove('bg-slate-800', 'hover:bg-slate-700/80');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx) {
            btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    if (feedback) {
        feedback.classList.remove('hidden');
        if (selectedIdx === correctIdx) {
            feedback.innerHTML = `<div class="p-2.5 rounded-lg bg-emerald-950/70 border border-emerald-500/40 text-emerald-300 text-xs mt-2 flex items-start gap-2"><span>✅</span><span><strong>Correct!</strong> ${explanation}</span></div>`;
        } else {
            feedback.innerHTML = `<div class="p-2.5 rounded-lg bg-rose-950/70 border border-rose-500/40 text-rose-300 text-xs mt-2 flex items-start gap-2"><span>❌</span><span><strong>Not quite.</strong> ${explanation}</span></div>`;
        }
    }
}

// Quiz Selection
function selectQuizOption(qId, selectedIdx, correctIdx) {
    const card = document.getElementById(`quiz-q-${qId}`);
    if (!card) return;
    const btns = card.querySelectorAll('.quiz-option-btn');

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        btn.classList.remove('bg-slate-800', 'hover:bg-slate-700/80');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx) {
            btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    const solBtn = card.querySelector('.view-solution-btn');
    if (solBtn) solBtn.classList.remove('hidden');
}

// Pop-up Solution Modal
function openSolution(qId) {
    const qData = QUIZ_QUESTIONS_MAP[qId];
    if (!qData) return;
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionTitle');
    const body = document.getElementById('solutionBody');

    if (title) title.textContent = `Solution — Question ${qId}`;
    if (body) {
        body.innerHTML = `
            <div class="space-y-3 text-xs sm:text-sm">
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                    <span class="text-slate-400 font-mono text-[11px] block mb-1">QUESTION</span>
                    <p class="text-slate-100 font-medium">${qData.question}</p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/40">
                    <div class="flex items-center gap-1.5 text-emerald-400 font-bold mb-1">
                        <span>✓</span>
                        <span>Correct Answer: Option ${['A', 'B', 'C', 'D'][qData.correct]}</span>
                    </div>
                    <p class="text-emerald-200 font-mono font-semibold">${qData.options[qData.correct]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-slate-300 leading-relaxed">
                    <span class="text-amber-400 font-mono text-[11px] font-bold block mb-1">STEP-BY-STEP EXPLANATION</span>
                    <p>${qData.solution}</p>
                </div>
            </div>
        `;
    }
    if (modal) modal.style.display = 'flex';
}

function closeSolution() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// Keyboard navigation
window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
    if (e.key === 'Escape') closeSolution();
});

// ==========================================
// SIMULATOR LOGIC (1 to 16)
// ==========================================

function initCurrentSimulator() {
    switch (currentSlide) {
        case 1: updateSim1(); break;
        case 2: updateSim2(); break;
        case 3: initSim3(); break;
        case 4: setSim4Mode('stripes'); break;
        case 5: setSim5Folds(2); break;
        case 6: updateSim6(); break;
        case 7: updateSim7(); break;
        case 8: resetSim8(); break;
        case 9: updateSim9(); break;
        case 10: updateSim10(); break;
        case 11: buildSim11Wall(); break;
        case 12: updateSim12(); break;
        case 13: updateSim13(); break;
        case 14: updateSim14(); break;
        case 15: updateSim15(); break;
        case 16: updateSim16(); break;
    }
}

// Sim 1: Roti Sharing
function updateSim1() {
    const n = parseInt(document.getElementById('sim1_n')?.value || 2);
    const nVal = document.getElementById('sim1_n_val');
    const badge = document.getElementById('sim1_badge');
    const readout = document.getElementById('sim1_readout');
    const svg = document.getElementById('sim1_svg');

    if (nVal) nVal.textContent = n;
    if (badge) badge.textContent = `1/${n} Roti Each`;
    if (readout) readout.textContent = `1 whole roti ÷ ${n} children = 1/${n} share`;

    if (!svg) return;
    svg.innerHTML = '';

    const cx = 100, cy = 100, r = 80;
    const colors = ['#f59e0b', '#38bdf8', '#10b981', '#ec4899', '#8b5cf6', '#f97316', '#06b6d4', '#84cc16', '#a855f7', '#14b8a6', '#eab308', '#6366f1'];

    if (n === 1) {
        svg.innerHTML = `
            <circle cx="${cx}" cy="${cy}" r="${r}" fill="#f59e0b" fill-opacity="0.8" stroke="#fbbf24" stroke-width="3" />
            <text x="${cx}" y="${cy+5}" text-anchor="middle" fill="#0f172a" font-weight="bold" font-family="monospace" font-size="16">1 Whole</text>
        `;
        return;
    }

    const angleStep = (2 * Math.PI) / n;
    for (let i = 0; i < n; i++) {
        const startAngle = i * angleStep - Math.PI / 2;
        const endAngle = (i + 1) * angleStep - Math.PI / 2;
        const x1 = cx + r * Math.cos(startAngle);
        const y1 = cy + r * Math.sin(startAngle);
        const x2 = cx + r * Math.cos(endAngle);
        const y2 = cy + r * Math.sin(endAngle);
        const largeArc = (endAngle - startAngle > Math.PI) ? 1 : 0;
        const color = colors[i % colors.length];

        const pathData = `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`;
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', pathData);
        path.setAttribute('fill', color);
        path.setAttribute('fill-opacity', i === 0 ? '0.95' : '0.6');
        path.setAttribute('stroke', '#0f172a');
        path.setAttribute('stroke-width', '2');
        svg.appendChild(path);

        // Slice label
        const midAngle = (startAngle + endAngle) / 2;
        const lx = cx + (r * 0.65) * Math.cos(midAngle);
        const ly = cy + (r * 0.65) * Math.sin(midAngle) + 4;
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', lx);
        text.setAttribute('y', ly);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#ffffff');
        text.setAttribute('font-size', n > 8 ? '9' : '11');
        text.setAttribute('font-family', 'monospace');
        text.setAttribute('font-weight', 'bold');
        text.textContent = `1/${n}`;
        svg.appendChild(text);
    }
}

// Sim 2: Comparing Unit Fractions
function updateSim2() {
    const a = parseInt(document.getElementById('sim2_a')?.value || 3);
    const b = parseInt(document.getElementById('sim2_b')?.value || 6);

    const aLbl = document.getElementById('sim2_a_label');
    const bLbl = document.getElementById('sim2_b_label');
    const aPct = document.getElementById('sim2_a_pct');
    const bPct = document.getElementById('sim2_b_pct');
    const res = document.getElementById('sim2_result');

    if (aLbl) aLbl.textContent = a;
    if (bLbl) bLbl.textContent = b;
    if (aPct) aPct.textContent = `${(100 / a).toFixed(1)}% of whole`;
    if (bPct) bPct.textContent = `${(100 / b).toFixed(1)}% of whole`;

    if (res) {
        if (a < b) res.textContent = `1/${a} > 1/${b}`;
        else if (a > b) res.textContent = `1/${a} < 1/${b}`;
        else res.textContent = `1/${a} = 1/${b}`;
    }

    const stripA = document.getElementById('sim2_strip_a');
    if (stripA) {
        stripA.innerHTML = '';
        for (let i = 0; i < a; i++) {
            const cell = document.createElement('div');
            cell.style.width = `${100 / a}%`;
            cell.className = `h-full border-r border-slate-900 flex items-center justify-center font-mono text-[10px] font-bold ${i === 0 ? 'bg-amber-500 text-slate-950 shadow-inner' : 'bg-slate-700/60 text-slate-400'}`;
            cell.textContent = `1/${a}`;
            stripA.appendChild(cell);
        }
    }

    const stripB = document.getElementById('sim2_strip_b');
    if (stripB) {
        stripB.innerHTML = '';
        for (let i = 0; i < b; i++) {
            const cell = document.createElement('div');
            cell.style.width = `${100 / b}%`;
            cell.className = `h-full border-r border-slate-900 flex items-center justify-center font-mono text-[10px] font-bold ${i === 0 ? 'bg-cyan-500 text-slate-950 shadow-inner' : 'bg-slate-700/60 text-slate-400'}`;
            cell.textContent = `1/${b}`;
            stripB.appendChild(cell);
        }
    }
}

// Sim 3: Parts of a Whole (Chikki)
let sim3Total = 8;
let sim3Selected = [true, true, true, false, false, false, false, false];

function initSim3() {
    setSim3Size(8);
}

function setSim3Size(size) {
    sim3Total = size;
    sim3Selected = new Array(size).fill(false);
    for (let i = 0; i < Math.floor(size / 2); i++) sim3Selected[i] = true;
    renderSim3();
}

function toggleSim3Piece(idx) {
    sim3Selected[idx] = !sim3Selected[idx];
    renderSim3();
}

function renderSim3() {
    const grid = document.getElementById('sim3_grid');
    if (!grid) return;
    grid.innerHTML = '';

    let cols = 4;
    if (sim3Total === 4) cols = 2;
    if (sim3Total === 6) cols = 3;
    if (sim3Total === 8) cols = 4;
    if (sim3Total === 12) cols = 4;

    grid.style.gridTemplateColumns = `repeat(${cols}, minmax(0, 1fr))`;

    let count = 0;
    sim3Selected.forEach((sel, i) => {
        if (sel) count++;
        const btn = document.createElement('button');
        btn.onclick = () => toggleSim3Piece(i);
        btn.className = `w-14 h-12 rounded-lg border flex flex-col items-center justify-center font-mono text-xs font-bold transition-all ${
            sel ? 'bg-amber-600 border-amber-400 text-amber-100 shadow-md scale-95' : 'bg-slate-800 border-slate-700 text-slate-500 hover:bg-slate-750'
        }`;
        btn.innerHTML = `<span>1/${sim3Total}</span><span class="text-[9px]">${sel ? 'Selected' : 'Piece'}</span>`;
        grid.appendChild(btn);
    });

    const frac = document.getElementById('sim3_frac');
    const cEl = document.getElementById('sim3_count');
    const tEl = document.getElementById('sim3_total');
    const rem = document.getElementById('sim3_rem');

    if (frac) frac.textContent = `${count}/${sim3Total}`;
    if (cEl) cEl.textContent = count;
    if (tEl) tEl.textContent = sim3Total;
    if (rem) rem.textContent = `${sim3Total - count}/${sim3Total}`;
}

// Sim 4: Different Shapes, Same Share (1/4)
function setSim4Mode(mode) {
    const svg = document.getElementById('sim4_svg');
    const desc = document.getElementById('sim4_desc');
    if (!svg) return;
    svg.innerHTML = '';

    if (mode === 'stripes') {
        if (desc) desc.textContent = 'Mode: 4 Vertical Columns (Stripes) — Width = 45px each';
        svg.innerHTML = `
            <rect x="10" y="10" width="45" height="180" fill="#f59e0b" fill-opacity="0.9" stroke="#fbbf24" stroke-width="2" />
            <text x="32" y="105" text-anchor="middle" fill="#0f172a" font-weight="bold" font-family="monospace" font-size="14">1/4</text>
            <rect x="55" y="10" width="45" height="180" fill="#334155" stroke="#475569" stroke-width="1.5" />
            <rect x="100" y="10" width="45" height="180" fill="#1e293b" stroke="#475569" stroke-width="1.5" />
            <rect x="145" y="10" width="45" height="180" fill="#334155" stroke="#475569" stroke-width="1.5" />
        `;
    } else if (mode === 'grid') {
        if (desc) desc.textContent = 'Mode: 2×2 Corner Grid — 4 Equal Small Squares';
        svg.innerHTML = `
            <rect x="10" y="10" width="90" height="90" fill="#06b6d4" fill-opacity="0.9" stroke="#22d3ee" stroke-width="2" />
            <text x="55" y="60" text-anchor="middle" fill="#0f172a" font-weight="bold" font-family="monospace" font-size="14">1/4</text>
            <rect x="100" y="10" width="90" height="90" fill="#334155" stroke="#475569" stroke-width="1.5" />
            <rect x="10" y="100" width="90" height="90" fill="#1e293b" stroke="#475569" stroke-width="1.5" />
            <rect x="100" y="100" width="90" height="90" fill="#334155" stroke="#475569" stroke-width="1.5" />
        `;
    } else if (mode === 'diagonals') {
        if (desc) desc.textContent = 'Mode: 2 Diagonals — 4 Congruent Right Triangles';
        svg.innerHTML = `
            <polygon points="10,10 190,10 100,100" fill="#10b981" fill-opacity="0.9" stroke="#34d399" stroke-width="2" />
            <text x="100" y="50" text-anchor="middle" fill="#0f172a" font-weight="bold" font-family="monospace" font-size="14">1/4</text>
            <polygon points="190,10 190,190 100,100" fill="#334155" stroke="#475569" stroke-width="1.5" />
            <polygon points="190,190 10,190 100,100" fill="#1e293b" stroke="#475569" stroke-width="1.5" />
            <polygon points="10,190 10,10 100,100" fill="#334155" stroke="#475569" stroke-width="1.5" />
        `;
    }
}

// Sim 5: Paper Strip Folding
function setSim5Folds(folds) {
    const paper = document.getElementById('sim5_paper');
    const text = document.getElementById('sim5_text');
    const badge = document.getElementById('sim5_badge');
    if (!paper) return;

    paper.innerHTML = '';
    let totalParts = 2;
    let label = '1/2';

    if (folds === 1) {
        totalParts = 2;
        label = '1/2';
        if (badge) badge.textContent = '2 Halves';
        if (text) text.textContent = '1 fold in half = 2 equal halves (Crease at 1/2)';
    } else if (folds === 2) {
        totalParts = 4;
        label = '1/4';
        if (badge) badge.textContent = '4 Quarters';
        if (text) text.textContent = '2 folds in half = 2 × 2 = 4 equal sections (Unit: 1/4)';
    } else if (folds === 3) {
        totalParts = 8;
        label = '1/8';
        if (badge) badge.textContent = '8 Eighths';
        if (text) text.textContent = '3 folds in half = 2 × 2 × 2 = 8 equal sections (Unit: 1/8)';
    } else if (folds === 6) {
        totalParts = 6;
        label = '1/6';
        if (badge) badge.textContent = '6 Sixths';
        if (text) text.textContent = 'Folded into thirds, then folded in half = 3 × 2 = 6 parts (Unit: 1/6)';
    }

    for (let i = 0; i < totalParts; i++) {
        const seg = document.createElement('div');
        seg.style.width = `${100 / totalParts}%`;
        seg.className = `h-full border-r-2 border-dashed border-amber-500/80 flex items-center justify-center font-mono text-xs font-bold ${
            i % 2 === 0 ? 'bg-amber-200/90 text-amber-950' : 'bg-amber-100 text-amber-900'
        }`;
        seg.textContent = label;
        paper.appendChild(seg);
    }
}

// Sim 6: Numerator vs Denominator
function updateSim6() {
    const num = parseInt(document.getElementById('sim6_num')?.value || 5);
    const den = parseInt(document.getElementById('sim6_den')?.value || 3);

    const numVal = document.getElementById('sim6_num_val');
    const denVal = document.getElementById('sim6_den_val');
    const numDisp = document.getElementById('sim6_num_disp');
    const denDisp = document.getElementById('sim6_den_disp');
    const countWord = document.getElementById('sim6_count_word');
    const unitWord = document.getElementById('sim6_unit_word');
    const sumExpr = document.getElementById('sim6_sum_expr');

    if (numVal) numVal.textContent = num;
    if (denVal) denVal.textContent = den;
    if (numDisp) numDisp.textContent = num;
    if (denDisp) denDisp.textContent = den;
    if (countWord) countWord.textContent = num;
    if (unitWord) unitWord.textContent = `1/${den}`;

    if (sumExpr) {
        const terms = new Array(num).fill(`1/${den}`).join(' + ');
        sumExpr.textContent = terms;
    }

    const blocks = document.getElementById('sim6_blocks');
    if (blocks) {
        blocks.innerHTML = '';
        for (let i = 0; i < num; i++) {
            const b = document.createElement('div');
            b.className = 'w-9 h-9 rounded bg-cyan-500/20 border border-cyan-400 text-cyan-200 font-mono text-[10px] font-bold flex items-center justify-center shadow-sm';
            b.textContent = `1/${den}`;
            blocks.appendChild(b);
        }
    }
}

// Sim 7: Number Line Plotter
function updateSim7() {
    const den = parseInt(document.getElementById('sim7_den')?.value || 4);
    const num = parseInt(document.getElementById('sim7_num')?.value || 3);

    const denVal = document.getElementById('sim7_den_val');
    const numVal = document.getElementById('sim7_num_val');
    const badge = document.getElementById('sim7_badge');
    const desc = document.getElementById('sim7_desc');
    const svg = document.getElementById('sim7_svg');

    if (denVal) denVal.textContent = den;
    if (numVal) numVal.textContent = num;
    if (badge) badge.textContent = `Point = ${num}/${den}`;
    if (desc) desc.textContent = `Interval split into ${den} equal segments. Step ${num} times from 0 → ${num}/${den}.`;

    if (!svg) return;
    svg.innerHTML = '';

    const startX = 20, endX = 300, y = 45;
    const unitWidth = 140; // width of 1 unit (0 to 1)

    // Main axis line
    svg.innerHTML += `
        <line x1="${startX}" y1="${y}" x2="${endX}" y2="${y}" stroke="#64748b" stroke-width="2" />
        <polygon points="${endX+5},${y} ${endX-5},${y-4} ${endX-5},${y+4}" fill="#64748b" />
    `;

    // Major integer ticks (0, 1, 2)
    for (let u = 0; u <= 2; u++) {
        const ux = startX + u * unitWidth;
        if (ux <= endX) {
            svg.innerHTML += `
                <line x1="${ux}" y1="${y-8}" x2="${ux}" y2="${y+8}" stroke="#f8fafc" stroke-width="2.5" />
                <text x="${ux}" y="${y+22}" text-anchor="middle" fill="#f8fafc" font-family="monospace" font-weight="bold" font-size="12">${u}</text>
            `;
        }
    }

    // Sub-ticks for denominator
    const totalSegments = den * 2;
    for (let s = 1; s <= totalSegments; s++) {
        if (s % den === 0) continue; // skip whole numbers
        const sx = startX + (s / den) * unitWidth;
        if (sx <= endX) {
            svg.innerHTML += `
                <line x1="${sx}" y1="${y-5}" x2="${sx}" y2="${y+5}" stroke="#94a3b8" stroke-width="1.5" />
                <text x="${sx}" y="${y+18}" text-anchor="middle" fill="#94a3b8" font-family="monospace" font-size="8">${s}/${den}</text>
            `;
        }
    }

    // Target pointer
    const targetX = startX + (num / den) * unitWidth;
    if (targetX <= endX) {
        svg.innerHTML += `
            <circle cx="${targetX}" cy="${y}" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
            <line x1="${targetX}" y1="${y-22}" x2="${targetX}" y2="${y-8}" stroke="#f59e0b" stroke-width="2" />
            <polygon points="${targetX},${y-6} ${targetX-4},${y-12} ${targetX+4},${y-12}" fill="#f59e0b" />
            <text x="${targetX}" y="${y-25}" text-anchor="middle" fill="#f59e0b" font-family="monospace" font-weight="bold" font-size="11">${num}/${den}</text>
        `;
    }
}

// Sim 8: Density Microscope
let sim8Denom = 2;

function resetSim8() {
    sim8Denom = 2;
    renderSim8();
}

function zoomSim8() {
    if (sim8Denom < 64) sim8Denom *= 2;
    renderSim8();
}

function renderSim8() {
    const lvl = document.getElementById('sim8_level');
    const txt = document.getElementById('sim8_text');
    const svg = document.getElementById('sim8_svg');

    if (lvl) lvl.textContent = `Zoom: 1/${sim8Denom}`;
    if (txt) txt.textContent = `Bisecting midpoint: 0 ... 1/${sim8Denom} ... 1/${sim8Denom/2 || 1}`;

    if (!svg) return;
    svg.innerHTML = '';

    const startX = 25, endX = 295, y = 45;
    svg.innerHTML += `
        <line x1="${startX}" y1="${y}" x2="${endX}" y2="${y}" stroke="#475569" stroke-width="2" />
        <line x1="${startX}" y1="${y-8}" x2="${startX}" y2="${y+8}" stroke="#f8fafc" stroke-width="2" />
        <text x="${startX}" y="${y+20}" text-anchor="middle" fill="#f8fafc" font-mono font-size="10">0</text>
        <line x1="${endX}" y1="${y-8}" x2="${endX}" y2="${y+8}" stroke="#f8fafc" stroke-width="2" />
        <text x="${endX}" y="${y+20}" text-anchor="middle" fill="#f8fafc" font-mono font-size="10">1</text>
    `;

    // Render midpoints up to current denom
    let d = 2;
    while (d <= sim8Denom) {
        const x = startX + (1 / d) * (endX - startX);
        const isCurrent = (d === sim8Denom);
        svg.innerHTML += `
            <circle cx="${x}" cy="${y}" r="${isCurrent ? 5 : 3}" fill="${isCurrent ? '#06b6d4' : '#f59e0b'}" />
            <line x1="${x}" y1="${y-6}" x2="${x}" y2="${y+6}" stroke="${isCurrent ? '#06b6d4' : '#f59e0b'}" stroke-width="1.5" />
            <text x="${x}" y="${y-10}" text-anchor="middle" fill="${isCurrent ? '#22d3ee' : '#fbbf24'}" font-family="monospace" font-size="${isCurrent ? '10' : '8'}" font-weight="bold">1/${d}</text>
        `;
        d *= 2;
    }
}

// Sim 9: Proper vs Improper Sorter
function updateSim9() {
    const num = parseInt(document.getElementById('sim9_num')?.value || 3);
    const den = parseInt(document.getElementById('sim9_den')?.value || 4);

    const numVal = document.getElementById('sim9_num_val');
    const denVal = document.getElementById('sim9_den_val');
    const badge = document.getElementById('sim9_badge');
    const status = document.getElementById('sim9_status');
    const pies = document.getElementById('sim9_pies');

    if (numVal) numVal.textContent = num;
    if (denVal) denVal.textContent = den;

    const val = num / den;
    if (badge) {
        if (num < den) {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.textContent = 'Proper Fraction (< 1)';
        } else if (num === den) {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.textContent = 'Equal to One (= 1)';
        } else {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30';
            badge.textContent = 'Improper Fraction (> 1)';
        }
    }

    if (status) {
        status.textContent = `Value = ${num}/${den} = ${val.toFixed(2)} (${num < den ? 'Less than 1 whole' : (num === den ? 'Exactly 1 whole' : 'Greater than 1 whole')})`;
    }

    if (!pies) return;
    pies.innerHTML = '';

    const wholePies = Math.ceil(num / den);
    let remaining = num;

    for (let p = 0; p < wholePies; p++) {
        const pieSlices = Math.min(den, remaining);
        remaining -= pieSlices;

        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 100 100');
        svg.setAttribute('class', 'w-16 h-16 drop-shadow');

        const cx = 50, cy = 50, r = 40;
        const angleStep = (2 * Math.PI) / den;

        for (let i = 0; i < den; i++) {
            const startAngle = i * angleStep - Math.PI / 2;
            const endAngle = (i + 1) * angleStep - Math.PI / 2;
            const x1 = cx + r * Math.cos(startAngle);
            const y1 = cy + r * Math.sin(startAngle);
            const x2 = cx + r * Math.cos(endAngle);
            const y2 = cy + r * Math.sin(endAngle);
            const largeArc = (endAngle - startAngle > Math.PI) ? 1 : 0;
            const isFilled = (i < pieSlices);

            const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            path.setAttribute('d', `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`);
            path.setAttribute('fill', isFilled ? (num > den ? '#f43f5e' : '#10b981') : '#334155');
            path.setAttribute('stroke', '#0f172a');
            path.setAttribute('stroke-width', '1.5');
            svg.appendChild(path);
        }
        pies.appendChild(svg);
    }
}

// Sim 10: Mixed Numbers Converter
function updateSim10() {
    const num = parseInt(document.getElementById('sim10_num')?.value || 7);
    const den = parseInt(document.getElementById('sim10_den')?.value || 3);

    const numVal = document.getElementById('sim10_num_val');
    const denVal = document.getElementById('sim10_den_val');
    const impEl = document.getElementById('sim10_improper');
    const mixEl = document.getElementById('sim10_mixed');
    const divEl = document.getElementById('sim10_division');

    if (numVal) numVal.textContent = num;
    if (denVal) denVal.textContent = den;

    const whole = Math.floor(num / den);
    const rem = num % den;

    if (impEl) impEl.textContent = `${num}/${den}`;
    if (mixEl) {
        if (rem === 0) mixEl.textContent = `${whole}`;
        else mixEl.textContent = `${whole} ${rem}/${den}`;
    }
    if (divEl) {
        divEl.textContent = `Division: ${num} ÷ ${den} = ${whole} with remainder ${rem} → ${whole} wholes + ${rem}/${den}`;
    }
}

// Sim 11: Fraction Wall
function buildSim11Wall() {
    const wall = document.getElementById('sim11_wall');
    if (!wall) return;
    wall.innerHTML = '';

    const denoms = [1, 2, 3, 4, 5, 6, 8, 10];
    const colors = ['#f59e0b', '#38bdf8', '#10b981', '#ec4899', '#8b5cf6', '#f97316', '#06b6d4', '#84cc16'];

    denoms.forEach((d, idx) => {
        const row = document.createElement('div');
        row.className = 'w-full h-5.5 rounded flex border border-slate-700/80 overflow-hidden';
        for (let i = 0; i < d; i++) {
            const cell = document.createElement('div');
            cell.style.width = `${100 / d}%`;
            cell.className = 'h-full border-r border-slate-900 flex items-center justify-center font-mono text-[9px] font-bold text-slate-900 select-none';
            cell.style.backgroundColor = colors[idx % colors.length];
            cell.textContent = d === 1 ? '1 Whole' : `1/${d}`;
            row.appendChild(cell);
        }
        wall.appendChild(row);
    });
}

function setSim11Laser(pct, label) {
    const laser = document.getElementById('sim11_laser');
    const readout = document.getElementById('sim11_readout');
    if (laser) laser.style.left = `${pct * 100}%`;
    if (readout) {
        if (label === '1/2') readout.textContent = 'Aligning 1/2 = 2/4 = 3/6 = 4/8 = 5/10';
        else if (label === '1/4') readout.textContent = 'Aligning 1/4 = 2/8';
        else if (label === '1/3') readout.textContent = 'Aligning 1/3 = 2/6';
        else if (label === '3/4') readout.textContent = 'Aligning 3/4 = 6/8';
    }
}

// Sim 12: Equivalent Fractions Multiplier
function updateSim12() {
    const k = parseInt(document.getElementById('sim12_k')?.value || 2);
    const kVal = document.getElementById('sim12_k_val');
    const formula = document.getElementById('sim12_formula');
    const math = document.getElementById('sim12_math');

    if (kVal) kVal.textContent = k;
    const baseN = 2, baseD = 3;
    const newN = baseN * k, newD = baseD * k;

    if (formula) formula.textContent = `${baseN}/${baseD} = ${newN}/${newD}`;
    if (math) math.textContent = `Multiply top & bottom by ${k}: (${baseN} × ${k}) / (${baseD} × ${k}) = ${newN}/${newD}`;

    drawSim12Svg('sim12_svg1', baseN, baseD);
    drawSim12Svg('sim12_svg2', newN, newD);
}

function drawSim12Svg(svgId, n, d) {
    const svg = document.getElementById(svgId);
    if (!svg) return;
    svg.innerHTML = '';

    const cx = 50, cy = 50, r = 42;
    const angleStep = (2 * Math.PI) / d;

    for (let i = 0; i < d; i++) {
        const startAngle = i * angleStep - Math.PI / 2;
        const endAngle = (i + 1) * angleStep - Math.PI / 2;
        const x1 = cx + r * Math.cos(startAngle);
        const y1 = cy + r * Math.sin(startAngle);
        const x2 = cx + r * Math.cos(endAngle);
        const y2 = cy + r * Math.sin(endAngle);
        const largeArc = (endAngle - startAngle > Math.PI) ? 1 : 0;
        const isFilled = (i < n);

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`);
        path.setAttribute('fill', isFilled ? '#f59e0b' : '#334155');
        path.setAttribute('stroke', '#0f172a');
        path.setAttribute('stroke-width', '1.5');
        svg.appendChild(path);
    }
}

// Sim 13: Simplest Form
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

function updateSim13() {
    const num = parseInt(document.getElementById('sim13_num')?.value || 24);
    const den = parseInt(document.getElementById('sim13_den')?.value || 36);

    const numVal = document.getElementById('sim13_num_val');
    const denVal = document.getElementById('sim13_den_val');
    const initEl = document.getElementById('sim13_init');
    const finalEl = document.getElementById('sim13_final');
    const hcfEl = document.getElementById('sim13_hcf');
    const steps = document.getElementById('sim13_steps');

    if (numVal) numVal.textContent = num;
    if (denVal) denVal.textContent = den;
    if (initEl) initEl.textContent = `${num}/${den}`;

    const g = gcd(num, den);
    const simpN = num / g;
    const simpD = den / g;

    if (finalEl) finalEl.textContent = `${simpN}/${simpD}`;
    if (hcfEl) hcfEl.textContent = `HCF = ${g}`;
    if (steps) {
        if (g === 1) {
            steps.textContent = `HCF is 1: ${num} and ${den} are co-prime, already in simplest form!`;
        } else {
            steps.textContent = `Divide both by HCF (${g}): (${num} ÷ ${g}) / (${den} ÷ ${g}) = ${simpN}/${simpD} (Lowest terms!)`;
        }
    }
}

// Sim 14: Comparing Fractions
function updateSim14() {
    const n1 = parseInt(document.getElementById('sim14_n1')?.value || 3);
    const d1 = parseInt(document.getElementById('sim14_d1')?.value || 4);
    const n2 = parseInt(document.getElementById('sim14_n2')?.value || 5);
    const d2 = parseInt(document.getElementById('sim14_d2')?.value || 6);

    const f1Disp = document.getElementById('sim14_f1_disp');
    const f2Disp = document.getElementById('sim14_f2_disp');
    const f1Equiv = document.getElementById('sim14_f1_equiv');
    const f2Equiv = document.getElementById('sim14_f2_equiv');
    const winner = document.getElementById('sim14_winner');
    const cross = document.getElementById('sim14_cross');

    if (f1Disp) f1Disp.textContent = `${n1}/${d1}`;
    if (f2Disp) f2Disp.textContent = `${n2}/${d2}`;

    const l = (d1 * d2) / gcd(d1, d2);
    const eq1 = n1 * (l / d1);
    const eq2 = n2 * (l / d2);

    if (f1Equiv) f1Equiv.textContent = `= ${eq1}/${l}`;
    if (f2Equiv) f2Equiv.textContent = `= ${eq2}/${l}`;

    const cross1 = n1 * d2;
    const cross2 = n2 * d1;

    let op = '=';
    if (cross1 > cross2) op = '>';
    if (cross1 < cross2) op = '<';

    if (winner) winner.textContent = `${n1}/${d1} ${op} ${n2}/${d2}`;
    if (cross) {
        cross.textContent = `Cross-products: ${n1} × ${d2} = ${cross1} ${op} ${d1} × ${n2} = ${cross2} → ${n1}/${d1} ${op} ${n2}/${d2}!`;
    }
}

// Sim 15: Adding Like Fractions
let sim15Mode = 'add';

function setSim15Op(op) {
    sim15Mode = op;
    const btnAdd = document.getElementById('sim15_btn_add');
    const btnSub = document.getElementById('sim15_btn_sub');
    if (op === 'add') {
        if (btnAdd) btnAdd.className = 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnSub) btnSub.className = 'px-2.5 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
    } else {
        if (btnSub) btnSub.className = 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnAdd) btnAdd.className = 'px-2.5 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
    }
    updateSim15();
}

function updateSim15() {
    const d = parseInt(document.getElementById('sim15_d')?.value || 5);
    const na = parseInt(document.getElementById('sim15_na')?.value || 2);
    const nb = parseInt(document.getElementById('sim15_nb')?.value || 1);

    const denLbl = document.getElementById('sim15_den_lbl');
    const opLbl = document.getElementById('sim15_op_lbl');
    const badge = document.getElementById('sim15_badge');
    const math = document.getElementById('sim15_math');
    const strip = document.getElementById('sim15_strip');

    if (denLbl) denLbl.textContent = d;

    let res = (sim15Mode === 'add') ? na + nb : na - nb;
    if (res < 0) res = 0;

    const opSymbol = (sim15Mode === 'add') ? '+' : '−';
    if (opLbl) opLbl.textContent = `${na} units ${opSymbol} ${nb} units = ${res} units`;
    if (badge) badge.textContent = `${na}/${d} ${opSymbol} ${nb}/${d} = ${res}/${d}`;
    if (math) math.textContent = `(${na} ${opSymbol} ${nb}) / ${d} = ${res}/${d}`;

    if (!strip) return;
    strip.innerHTML = '';

    for (let i = 0; i < d; i++) {
        const seg = document.createElement('div');
        seg.style.width = `${100 / d}%`;
        let colorCls = 'bg-slate-800 text-slate-500';
        if (i < res) colorCls = 'bg-emerald-500 text-slate-950 font-bold';
        seg.className = `h-full border-r border-slate-900 flex items-center justify-center font-mono text-[10px] ${colorCls}`;
        seg.textContent = `1/${d}`;
        strip.appendChild(seg);
    }
}

// Sim 16: Brahmagupta's Algorithm
function updateSim16() {
    const a = parseInt(document.getElementById('sim16_a')?.value || 1);
    const b = parseInt(document.getElementById('sim16_b')?.value || 3);
    const c = parseInt(document.getElementById('sim16_c')?.value || 1);
    const d = parseInt(document.getElementById('sim16_d')?.value || 4);

    const step1 = document.getElementById('sim16_step1');
    const step2 = document.getElementById('sim16_step2');

    const commonD = b * d;
    const numCross = (a * d) + (b * c);
    const g = gcd(numCross, commonD);
    const simpN = numCross / g;
    const simpD = commonD / g;

    if (step1) step1.textContent = `${a}/${b} + ${c}/${d} = (${a}×${d} + ${b}×${c}) / (${b}×${d})`;
    if (step2) {
        if (g > 1) {
            step2.textContent = `= (${a*d} + ${b*c}) / ${commonD} = ${numCross}/${commonD} = ${simpN}/${simpD}`;
        } else {
            step2.textContent = `= (${a*d} + ${b*c}) / ${commonD} = ${numCross}/${commonD}`;
        }
    }
}

function loadEgyptianPuzzle() {
    const eg = document.getElementById('sim16_egyptian');
    if (eg) eg.classList.toggle('hidden');
}
"""

def verify_js():
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in JS_CODE:
            raise ValueError(f"Found forbidden LaTeX token in JS_CODE: {word}")
    for ch in JS_CODE:
        if 0xD800 <= ord(ch) <= 0xDFFF:
            raise ValueError(f"Found surrogate in JS_CODE: {ch}")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in JS module!")

if __name__ == "__main__":
    verify_js()
    with open(".agents/class6_math_fractions_js.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("INTERACTIVE_JS = '''" + JS_CODE + "'''\n")
    print("Successfully generated .agents/class6_math_fractions_js.py.")


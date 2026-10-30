# -*- coding: utf-8 -*-
INTERACTIVE_JS = '''
let currentSlide = 1;
const totalSlides = 20;
let audioEnabled = false;
let synth = window.speechSynthesis;
let currentUtterance = null;

// Audio narration toggle
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
        case 3: setSim3Mode('wave'); break;
        case 4: updateSim4(); break;
        case 5: testSim5('ABCD'); break;
        case 6: updateSim6(); break;
        case 7: setSim7Step(1); break;
        case 8: updateSim8(); break;
        case 9: updateSim9(); break;
        case 10: setSim10Count(2); break;
        case 11: setSim11Mode('hole'); break;
        case 12: updateSim12(); break;
        case 13: setSim13Mode('rectangle'); break;
        case 14: updateSim14(); break;
        case 15: updateSim15(); break;
        case 16: renderSim16(); break;
    }
}

// Sim 1: Ruler & Compass
let sim1Mode = 'ruler';

function setSim1Mode(mode) {
    sim1Mode = mode;
    const btnR = document.getElementById('sim1_btn_ruler');
    const btnC = document.getElementById('sim1_btn_compass');
    const badge = document.getElementById('sim1_badge');
    const sliderLbl = document.getElementById('sim1_slider_label');

    if (mode === 'ruler') {
        if (btnR) btnR.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnC) btnC.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Mode: Straightedge';
        if (sliderLbl) sliderLbl.textContent = 'Length:';
    } else {
        if (btnC) btnC.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnR) btnR.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Mode: Compass Arc';
        if (sliderLbl) sliderLbl.textContent = 'Radius:';
    }
    updateSim1();
}

function updateSim1() {
    const val = parseInt(document.getElementById('sim1_slider')?.value || 60);
    const cm = (val / 10).toFixed(1);
    const valText = document.getElementById('sim1_val');
    const readout = document.getElementById('sim1_readout');
    const svg = document.getElementById('sim1_svg');

    if (valText) valText.textContent = `${cm} cm`;
    if (!svg) return;
    svg.innerHTML = '';

    if (sim1Mode === 'ruler') {
        if (readout) readout.textContent = `Segment AB = ${cm} cm`;
        const startX = 30, endX = startX + val * 2, y = 80;
        svg.innerHTML = `
            <line x1="${startX}" y1="${y}" x2="${endX}" y2="${y}" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" />
            <circle cx="${startX}" cy="${y}" r="4" fill="#fbbf24" />
            <text x="${startX}" y="${y+20}" fill="#fbbf24" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">A</text>
            <circle cx="${endX}" cy="${y}" r="4" fill="#fbbf24" />
            <text x="${endX}" y="${y+20}" fill="#fbbf24" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">B</text>
            <text x="${(startX+endX)/2}" y="${y-12}" fill="#38bdf8" font-family="monospace" font-size="11" text-anchor="middle">${cm} cm</text>
        `;
    } else {
        if (readout) readout.textContent = `Compass Arc: Radius r = ${cm} cm from center P`;
        const cx = 60, cy = 110, r = val * 1.5;
        svg.innerHTML = `
            <circle cx="${cx}" cy="${cy}" r="4" fill="#f43f5e" />
            <text x="${cx}" y="${cy+18}" fill="#f43f5e" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">P (Needle)</text>
            <path d="M ${cx + r * Math.cos(-Math.PI/6)} ${cy + r * Math.sin(-Math.PI/6)} A ${r} ${r} 0 0 0 ${cx + r * Math.cos(-Math.PI/2)} ${cy - r}" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,3" />
            <line x1="${cx}" y1="${cy}" x2="${cx + r * Math.cos(-Math.PI/4)}" y2="${cy + r * Math.sin(-Math.PI/4)}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2" />
            <text x="${cx + (r/2) * Math.cos(-Math.PI/4)}" y="${cy + (r/2) * Math.sin(-Math.PI/4) - 5}" fill="#f59e0b" font-family="monospace" font-size="10">r = ${cm} cm</text>
        `;
    }
}

// Sim 2: Circle Radius & Boundary
function updateSim2() {
    const r = parseInt(document.getElementById('sim2_r')?.value || 40);
    const d = parseInt(document.getElementById('sim2_d')?.value || 40);

    const rCm = (r / 10).toFixed(1);
    const dCm = (d / 10).toFixed(1);

    const rVal = document.getElementById('sim2_r_val');
    const dVal = document.getElementById('sim2_d_val');
    const status = document.getElementById('sim2_status');
    const readout = document.getElementById('sim2_readout');
    const svg = document.getElementById('sim2_svg');

    if (rVal) rVal.textContent = `${rCm} cm`;
    if (dVal) dVal.textContent = `${dCm} cm`;

    if (status) {
        if (Math.abs(r - d) <= 1) {
            status.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            status.textContent = 'On Boundary (d = r)';
        } else if (d < r) {
            status.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30';
            status.textContent = 'Inside Circle (d < r)';
        } else {
            status.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30';
            status.textContent = 'Outside Circle (d > r)';
        }
    }

    if (readout) readout.textContent = `Radius r = ${rCm} cm | Distance PQ = ${dCm} cm`;

    if (!svg) return;
    const cx = 100, cy = 80;
    const qx = cx + d * 1.6, qy = cy;

    svg.innerHTML = `
        <circle cx="${cx}" cy="${cy}" r="${r * 1.6}" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="2" />
        <circle cx="${cx}" cy="${cy}" r="3.5" fill="#f43f5e" />
        <text x="${cx-10}" y="${cy-8}" fill="#f43f5e" font-family="monospace" font-size="10" font-weight="bold">P (Center)</text>
        <line x1="${cx}" y1="${cy}" x2="${qx}" y2="${qy}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,2" />
        <circle cx="${qx}" cy="${qy}" r="4.5" fill="#38bdf8" />
        <text x="${qx}" y="${qy+16}" fill="#38bdf8" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">Q</text>
    `;
}

// Sim 3: Wave & Eye Motif
let sim3Mode = 'wave';

function setSim3Mode(mode) {
    sim3Mode = mode;
    const btnW = document.getElementById('sim3_btn_wave');
    const btnE = document.getElementById('sim3_btn_eye');
    const badge = document.getElementById('sim3_badge');
    const desc = document.getElementById('sim3_desc');
    const svg = document.getElementById('sim3_svg');

    if (mode === 'wave') {
        if (btnW) btnW.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnE) btnE.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Alternating Wave';
        if (desc) desc.textContent = 'Baseline AB = 8 cm | 4 Alternating Semicircles';
        if (svg) {
            svg.innerHTML = `
                <line x1="20" y1="70" x2="220" y2="70" stroke="#475569" stroke-width="1.5" />
                <path d="M 20,70 A 25,25 0 0,1 70,70 A 25,25 0 0,0 120,70 A 25,25 0 0,1 170,70 A 25,25 0 0,0 220,70" fill="none" stroke="#38bdf8" stroke-width="2.5" />
                <circle cx="45" cy="70" r="2.5" fill="#f59e0b" /><circle cx="95" cy="70" r="2.5" fill="#f59e0b" />
                <circle cx="145" cy="70" r="2.5" fill="#f59e0b" /><circle cx="195" cy="70" r="2.5" fill="#f59e0b" />
                <text x="20" y="90" fill="#94a3b8" font-mono font-size="10">A</text>
                <text x="215" y="90" fill="#94a3b8" font-mono font-size="10">B</text>
            `;
        }
    } else {
        if (btnE) btnE.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnW) btnW.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Symmetrical Eye Motif';
        if (desc) desc.textContent = 'Dual Intersecting Arcs from Centers B and C (Radius = BC)';
        if (svg) {
            svg.innerHTML = `
                <line x1="60" y1="70" x2="180" y2="70" stroke="#475569" stroke-width="1" stroke-dasharray="2,2" />
                <path d="M 60,70 A 120,120 0 0,1 180,70" fill="none" stroke="#f59e0b" stroke-width="2.5" />
                <path d="M 60,70 A 120,120 0 0,0 180,70" fill="none" stroke="#f59e0b" stroke-width="2.5" />
                <circle cx="60" cy="70" r="3.5" fill="#38bdf8" />
                <circle cx="180" cy="70" r="3.5" fill="#38bdf8" />
                <circle cx="120" cy="70" r="14" fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5" />
                <circle cx="120" cy="70" r="6" fill="#0f172a" />
                <text x="50" y="75" fill="#38bdf8" font-mono font-size="10">B</text>
                <text x="185" y="75" fill="#38bdf8" font-mono font-size="10">C</text>
            `;
        }
    }
}

// Sim 4: Rectangles & Squares Property Inspector
function updateSim4() {
    const l = parseInt(document.getElementById('sim4_l')?.value || 6);
    const b = parseInt(document.getElementById('sim4_b')?.value || 4);

    const lVal = document.getElementById('sim4_l_val');
    const bVal = document.getElementById('sim4_b_val');
    const badge = document.getElementById('sim4_badge');
    const s1 = document.getElementById('sim4_s1');
    const svg = document.getElementById('sim4_svg');

    if (lVal) lVal.textContent = `${l} cm`;
    if (bVal) bVal.textContent = `${b} cm`;

    const isSq = (l === b);
    if (badge) {
        if (isSq) {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.textContent = 'Square (Special Rectangle!)';
        } else {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30';
            badge.textContent = 'Rectangle';
        }
    }

    if (s1) {
        if (isSq) {
            s1.className = 'p-1 rounded bg-slate-800/80 border border-slate-700 text-emerald-300';
            s1.textContent = '✓ All sides equal (S1)';
        } else {
            s1.className = 'p-1 rounded bg-slate-800/80 border border-slate-700 text-slate-500';
            s1.textContent = '✗ All sides equal (S1)';
        }
    }

    if (!svg) return;
    const wPx = l * 18, hPx = b * 18;
    const x = (200 - wPx) / 2, y = (130 - hPx) / 2;

    svg.innerHTML = `
        <rect x="${x}" y="${y}" width="${wPx}" height="${hPx}" fill="${isSq ? '#10b981' : '#f59e0b'}" fill-opacity="0.15" stroke="${isSq ? '#10b981' : '#f59e0b'}" stroke-width="2.5" />
        <!-- 90 deg corner markers -->
        <rect x="${x}" y="${y}" width="10" height="10" fill="none" stroke="#64748b" stroke-width="1.5" />
        <rect x="${x+wPx-10}" y="${y}" width="10" height="10" fill="none" stroke="#64748b" stroke-width="1.5" />
        <rect x="${x+wPx-10}" y="${y+hPx-10}" width="10" height="10" fill="none" stroke="#64748b" stroke-width="1.5" />
        <rect x="${x}" y="${y+hPx-10}" width="10" height="10" fill="none" stroke="#64748b" stroke-width="1.5" />
        <text x="${x+wPx/2}" y="${y-6}" fill="#f8fafc" font-mono font-size="10" text-anchor="middle">${l} cm</text>
        <text x="${x+wPx+8}" y="${y+hPx/2+4}" fill="#f8fafc" font-mono font-size="10">${b} cm</text>
    `;
}

// Sim 5: Cyclical Vertex Naming Checker
function testSim5(name) {
    const badge = document.getElementById('sim5_badge');
    const readout = document.getElementById('sim5_readout');
    const svg = document.getElementById('sim5_svg');

    const isValid = (name === 'ABCD' || name === 'BCDA' || name === 'CDAB' || name === 'DABC' || name === 'DCBA' || name === 'CBAD');
    if (badge) {
        if (isValid) {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.textContent = `VALID: ${name}`;
        } else {
            badge.className = 'text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30';
            badge.textContent = `INVALID: ${name}`;
        }
    }

    if (readout) {
        if (isValid) {
            readout.textContent = `Sequence: ${name.split('').join(' → ')} (Valid cyclical perimeter order!)`;
        } else {
            readout.textContent = `Sequence: ${name.split('').join(' → ')} (Jumps across diagonal! Invalid!)`;
        }
    }

    if (!svg) return;
    const pts = {
        'A': [40, 30],
        'B': [160, 30],
        'C': [160, 110],
        'D': [40, 110]
    };

    let pathD = `M ${pts[name[0]][0]} ${pts[name[0]][1]}`;
    for (let i = 1; i < name.length; i++) {
        pathD += ` L ${pts[name[i]][0]} ${pts[name[i]][1]}`;
    }
    pathD += ` Z`;

    svg.innerHTML = `
        <rect x="40" y="30" width="120" height="80" fill="none" stroke="#334155" stroke-width="1.5" />
        <path d="${pathD}" fill="${isValid ? '#10b981' : '#f43f5e'}" fill-opacity="0.15" stroke="${isValid ? '#10b981' : '#f43f5e'}" stroke-width="2.5" />
        ${Object.keys(pts).map(k => `
            <circle cx="${pts[k][0]}" cy="${pts[k][1]}" r="5" fill="#f59e0b" />
            <text x="${pts[k][0] + (k==='A'||k==='D'?-14:14)}" y="${pts[k][1] + (k==='A'||k==='B'?-6:14)}" fill="#f59e0b" font-mono font-size="12" font-weight="bold" text-anchor="middle">${k}</text>
        `).join('')}
    `;
}

// Sim 6: Rotated Shape Invariance
function updateSim6() {
    const deg = parseInt(document.getElementById('sim6_slider')?.value || 0);
    const degText = document.getElementById('sim6_deg');
    const txt = document.getElementById('sim6_text');
    const svg = document.getElementById('sim6_svg');

    if (degText) degText.textContent = `${deg}°`;
    if (txt) txt.textContent = `Rotation: ${deg}° | 4 sides equal | 4 right angles = 90° (Still a Square!)`;

    if (!svg) return;
    svg.innerHTML = '';

    // Dot grid
    for (let r = 20; r <= 130; r += 20) {
        for (let c = 20; c <= 180; c += 20) {
            svg.innerHTML += `<circle cx="${c}" cy="${r}" r="1.5" fill="#475569" />`;
        }
    }

    svg.innerHTML += `
        <g transform="rotate(${deg} 100 75)">
            <rect x="65" y="40" width="70" height="70" fill="#f59e0b" fill-opacity="0.25" stroke="#f59e0b" stroke-width="2.5" />
            <rect x="65" y="40" width="8" height="8" fill="none" stroke="#64748b" stroke-width="1" />
            <rect x="127" y="40" width="8" height="8" fill="none" stroke="#64748b" stroke-width="1" />
            <rect x="127" y="102" width="8" height="8" fill="none" stroke="#64748b" stroke-width="1" />
            <rect x="65" y="102" width="8" height="8" fill="none" stroke="#64748b" stroke-width="1" />
        </g>
    `;
}

// Sim 7: Square Construction Stepper
function setSim7Step(step) {
    const badge = document.getElementById('sim7_step_badge');
    const desc = document.getElementById('sim7_desc');
    const svg = document.getElementById('sim7_svg');

    if (badge) badge.textContent = `Step ${step} of 4`;
    if (!svg) return;

    if (step === 1) {
        if (desc) desc.textContent = 'Step 1: Draw horizontal baseline segment AB = 6 cm using a ruler.';
        svg.innerHTML = `
            <line x1="40" y1="120" x2="160" y2="120" stroke="#38bdf8" stroke-width="3" />
            <circle cx="40" cy="120" r="4" fill="#fbbf24" /><text x="40" y="140" fill="#fbbf24" font-mono font-size="11">A</text>
            <circle cx="160" cy="120" r="4" fill="#fbbf24" /><text x="160" y="140" fill="#fbbf24" font-mono font-size="11">B</text>
            <text x="100" y="112" fill="#38bdf8" font-mono font-size="10" text-anchor="middle">6 cm</text>
        `;
    } else if (step === 2) {
        if (desc) desc.textContent = 'Step 2: Erect 90° perpendicular rays upward at vertex A and vertex B.';
        svg.innerHTML = `
            <line x1="40" y1="120" x2="160" y2="120" stroke="#38bdf8" stroke-width="2" />
            <line x1="40" y1="120" x2="40" y2="20" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,2" />
            <line x1="160" y1="120" x2="160" y2="20" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,2" />
            <rect x="40" y="110" width="10" height="10" fill="none" stroke="#f43f5e" stroke-width="1.5" />
            <rect x="150" y="110" width="10" height="10" fill="none" stroke="#f43f5e" stroke-width="1.5" />
            <circle cx="40" cy="120" r="3" fill="#fbbf24" /><text x="40" y="136" fill="#fbbf24" font-mono font-size="10">A</text>
            <circle cx="160" cy="120" r="3" fill="#fbbf24" /><text x="160" y="136" fill="#fbbf24" font-mono font-size="10">B</text>
        `;
    } else if (step === 3) {
        if (desc) desc.textContent = 'Step 3: Strike 6 cm arcs with compass from A and B to locate points D and C.';
        svg.innerHTML = `
            <line x1="40" y1="120" x2="160" y2="120" stroke="#38bdf8" stroke-width="2" />
            <line x1="40" y1="120" x2="40" y2="20" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,2" />
            <line x1="160" y1="120" x2="160" y2="20" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,2" />
            <path d="M 30,40 A 60,60 0 0,0 50,40" stroke="#f59e0b" stroke-width="2.5" />
            <circle cx="40" cy="40" r="4" fill="#10b981" /><text x="26" y="42" fill="#10b981" font-mono font-size="11" font-weight="bold">D</text>
            <path d="M 150,40 A 60,60 0 0,0 170,40" stroke="#f59e0b" stroke-width="2.5" />
            <circle cx="160" cy="40" r="4" fill="#10b981" /><text x="174" y="42" fill="#10b981" font-mono font-size="11" font-weight="bold">C</text>
            <circle cx="40" cy="120" r="3" fill="#fbbf24" /><text x="40" y="136" fill="#fbbf24" font-mono font-size="10">A</text>
            <circle cx="160" cy="120" r="3" fill="#fbbf24" /><text x="160" y="136" fill="#fbbf24" font-mono font-size="10">B</text>
        `;
    } else if (step === 4) {
        if (desc) desc.textContent = 'Step 4: Connect point D to C. Square ABCD is complete with side 6 cm!';
        svg.innerHTML = `
            <rect x="40" y="40" width="120" height="80" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2.5" />
            <circle cx="40" cy="120" r="3.5" fill="#fbbf24" /><text x="40" y="136" fill="#fbbf24" font-mono font-size="10">A</text>
            <circle cx="160" cy="120" r="3.5" fill="#fbbf24" /><text x="160" y="136" fill="#fbbf24" font-mono font-size="10">B</text>
            <circle cx="160" cy="40" r="3.5" fill="#10b981" /><text x="165" y="36" fill="#10b981" font-mono font-size="10">C</text>
            <circle cx="40" cy="40" r="3.5" fill="#10b981" /><text x="32" y="36" fill="#10b981" font-mono font-size="10">D</text>
            <text x="100" y="85" fill="#10b981" font-mono font-size="12" font-weight="bold" text-anchor="middle">Square ABCD</text>
        `;
    }
}

// Sim 8: Constructing Rectangles
function updateSim8() {
    const l = parseInt(document.getElementById('sim8_l')?.value || 6);
    const b = parseInt(document.getElementById('sim8_b')?.value || 4);

    const lVal = document.getElementById('sim8_l_val');
    const bVal = document.getElementById('sim8_b_val');
    const badge = document.getElementById('sim8_badge');
    const desc = document.getElementById('sim8_desc');
    const svg = document.getElementById('sim8_svg');

    if (lVal) lVal.textContent = `${l} cm`;
    if (bVal) bVal.textContent = `${b} cm`;
    if (badge) badge.textContent = `${l} cm × ${b} cm`;
    if (desc) desc.textContent = `Base AB = ${l} cm | Perpendiculars AD = BC = ${b} cm | CD = ${l} cm`;

    if (!svg) return;
    const w = l * 20, h = b * 20;
    const x = (240 - w) / 2, y = (140 - h) / 2;

    svg.innerHTML = `
        <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2.5" />
        <text x="${x+w/2}" y="${y+h+14}" fill="#38bdf8" font-mono font-size="10" text-anchor="middle">Base AB = ${l} cm</text>
        <text x="${x-10}" y="${y+h/2+4}" fill="#f59e0b" font-mono font-size="10" text-anchor="end">${b} cm</text>
        <circle cx="${x}" cy="${y+h}" r="3" fill="#fbbf24" /><text x="${x-6}" y="${y+h+10}" fill="#fbbf24" font-mono font-size="9">A</text>
        <circle cx="${x+w}" cy="${y+h}" r="3" fill="#fbbf24" /><text x="${x+w+6}" y="${y+h+10}" fill="#fbbf24" font-mono font-size="9">B</text>
        <circle cx="${x+w}" cy="${y}" r="3" fill="#fbbf24" /><text x="${x+w+6}" y="${y-4}" fill="#fbbf24" font-mono font-size="9">C</text>
        <circle cx="${x}" cy="${y}" r="3" fill="#fbbf24" /><text x="${x-6}" y="${y-4}" fill="#fbbf24" font-mono font-size="9">D</text>
    `;
}

// Sim 9: Dynamic Point Distance (XY)
function updateSim9() {
    const xPct = parseInt(document.getElementById('sim9_x')?.value || 0) / 100;
    const yPct = parseInt(document.getElementById('sim9_y')?.value || 0) / 100;

    const badge = document.getElementById('sim9_badge');
    const svg = document.getElementById('sim9_svg');

    // Rectangle 7cm x 4cm
    const lengthCm = 7, breadthCm = 4;
    const xCm = xPct * lengthCm;
    const yCm = yPct * lengthCm;
    const deltaX = Math.abs(xCm - yCm);
    const distCm = Math.sqrt(deltaX * deltaX + breadthCm * breadthCm);

    if (badge) badge.textContent = `XY = ${distCm.toFixed(2)} cm`;

    if (!svg) return;
    const rx = 30, ry = 25, rw = 180, rh = 80;
    const xPos = rx + xPct * rw;
    const yPos = rx + yPct * rw;

    svg.innerHTML = `
        <rect x="${rx}" y="${ry}" width="${rw}" height="${rh}" fill="#1e293b" stroke="#475569" stroke-width="2" />
        <line x1="${xPos}" y1="${ry}" x2="${yPos}" y2="${ry+rh}" stroke="#f43f5e" stroke-width="2.5" />
        <circle cx="${xPos}" cy="${ry}" r="4.5" fill="#f59e0b" />
        <text x="${xPos}" y="${ry-8}" fill="#f59e0b" font-mono font-size="10" font-weight="bold" text-anchor="middle">X</text>
        <circle cx="${yPos}" cy="${ry+rh}" r="4.5" fill="#38bdf8" />
        <text x="${yPos}" y="${ry+rh+16}" fill="#38bdf8" font-mono font-size="10" font-weight="bold" text-anchor="middle">Y</text>
        <text x="${rx+rw/2}" y="${ry+rh+28}" fill="#64748b" font-mono font-size="9" text-anchor="middle">Length = 7 cm | Breadth = 4 cm</text>
    `;
}

// Sim 10: Rectangles from Squares
function setSim10Count(k) {
    const badge = document.getElementById('sim10_badge');
    const desc = document.getElementById('sim10_desc');
    const svg = document.getElementById('sim10_svg');

    if (badge) badge.textContent = `${k} Congruent Squares`;
    if (desc) desc.textContent = `${k * 4} cm × 4 cm = ${k} Squares of 4 cm × 4 cm`;

    if (!svg) return;
    svg.innerHTML = '';

    const sqSize = 55;
    const totalW = k * sqSize;
    const startX = (240 - totalW) / 2, startY = 35;

    for (let i = 0; i < k; i++) {
        svg.innerHTML += `
            <rect x="${startX + i * sqSize}" y="${startY}" width="${sqSize}" height="${sqSize}" fill="${i % 2 === 0 ? '#06b6d4' : '#f59e0b'}" fill-opacity="0.2" stroke="#f8fafc" stroke-width="2" />
            <text x="${startX + i * sqSize + sqSize/2}" y="${startY + sqSize/2 + 4}" fill="#f8fafc" font-mono font-size="11" font-weight="bold" text-anchor="middle">Sq ${i+1}</text>
        `;
    }
}

// Sim 11: Nested Shapes & Holes
function setSim11Mode(mode) {
    const badge = document.getElementById('sim11_badge');
    const desc = document.getElementById('sim11_desc');
    const svg = document.getElementById('sim11_svg');

    if (mode === 'hole') {
        if (badge) badge.textContent = 'Circular Center Hole';
        if (desc) desc.textContent = 'Diagonal intersection crosshair pinpoints exact center for compass hole!';
        if (svg) {
            svg.innerHTML = `
                <rect x="20" y="10" width="120" height="120" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" />
                <line x1="20" y1="10" x2="140" y2="130" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2" />
                <line x1="140" y1="10" x2="20" y2="130" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2" />
                <circle cx="80" cy="70" r="28" fill="#020617" stroke="#38bdf8" stroke-width="2" />
                <circle cx="80" cy="70" r="3" fill="#f43f5e" />
                <text x="80" y="74" fill="#38bdf8" font-mono font-size="8" text-anchor="middle">Hole</text>
            `;
        }
    } else {
        if (badge) badge.textContent = 'Concentric Inner Square';
        if (desc) desc.textContent = 'Concentric nested square sharing the same diagonal center.';
        if (svg) {
            svg.innerHTML = `
                <rect x="20" y="10" width="120" height="120" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="2" />
                <line x1="20" y1="10" x2="140" y2="130" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2" />
                <line x1="140" y1="10" x2="20" y2="130" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2" />
                <rect x="50" y="40" width="60" height="60" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2" />
                <circle cx="80" cy="70" r="3" fill="#f43f5e" />
                <text x="80" y="74" fill="#10b981" font-mono font-size="9" text-anchor="middle">Nested</text>
            `;
        }
    }
}

// Sim 12: Diagonals of Quadrilaterals
function updateSim12() {
    const l = parseInt(document.getElementById('sim12_l')?.value || 6);
    const b = parseInt(document.getElementById('sim12_b')?.value || 4);

    const lVal = document.getElementById('sim12_l_val');
    const bVal = document.getElementById('sim12_b_val');
    const badge = document.getElementById('sim12_badge');
    const readout = document.getElementById('sim12_readout');
    const svg = document.getElementById('sim12_svg');

    if (lVal) lVal.textContent = `${l} cm`;
    if (bVal) bVal.textContent = `${b} cm`;

    const diag = Math.sqrt(l * l + b * b).toFixed(2);
    const half = (diag / 2).toFixed(2);

    if (badge) badge.textContent = `AC = BD = ${diag} cm`;
    if (readout) readout.textContent = `Diagonals bisect at M: AM = MC = BM = MD = ${half} cm`;

    if (!svg) return;
    const w = l * 20, h = b * 20;
    const x = (220 - w) / 2, y = (130 - h) / 2;

    svg.innerHTML = `
        <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#1e293b" stroke="#64748b" stroke-width="2" />
        <line x1="${x}" y1="${y}" x2="${x+w}" y2="${y+h}" stroke="#38bdf8" stroke-width="2" />
        <line x1="${x}" y1="${y+h}" x2="${x+w}" y2="${y}" stroke="#f59e0b" stroke-width="2" />
        <circle cx="${x+w/2}" cy="${y+h/2}" r="3.5" fill="#f43f5e" />
        <text x="${x+w/2}" y="${y+h/2-8}" fill="#f43f5e" font-mono font-size="10" font-weight="bold" text-anchor="middle">M</text>
        <text x="${x-6}" y="${y-4}" fill="#94a3b8" font-mono font-size="9">A</text>
        <text x="${x+w+4}" y="${y-4}" fill="#94a3b8" font-mono font-size="9">B</text>
        <text x="${x+w+4}" y="${y+h+10}" fill="#94a3b8" font-mono font-size="9">C</text>
        <text x="${x-6}" y="${y+h+10}" fill="#94a3b8" font-mono font-size="9">D</text>
    `;
}

// Sim 13: Diagonal Angle Splits
function setSim13Mode(mode) {
    const badge = document.getElementById('sim13_badge');
    const txt = document.getElementById('sim13_text');
    const btnR = document.getElementById('sim13_btn_rect');
    const btnS = document.getElementById('sim13_btn_sq');
    const svg = document.getElementById('sim13_svg');

    if (mode === 'rectangle') {
        if (btnR) btnR.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnS) btnS.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Unequal Split (56.3° & 33.7°)';
        if (txt) txt.textContent = 'Rectangle: 56.3° and 33.7° (Sum = 90°, not an angle bisector!)';
        if (svg) {
            svg.innerHTML = `
                <rect x="30" y="25" width="140" height="80" fill="#1e293b" stroke="#475569" stroke-width="2" />
                <line x1="30" y1="105" x2="170" y2="25" stroke="#38bdf8" stroke-width="2.5" />
                <path d="M 50,105 A 20,20 0 0,0 45,95" fill="none" stroke="#f59e0b" stroke-width="2" />
                <text x="56" y="100" fill="#f59e0b" font-mono font-size="9">33.7°</text>
                <path d="M 30,85 A 20,20 0 0,1 45,95" fill="none" stroke="#10b981" stroke-width="2" />
                <text x="35" y="80" fill="#10b981" font-mono font-size="9">56.3°</text>
                <circle cx="30" cy="105" r="3.5" fill="#f8fafc" /><text x="18" y="115" fill="#f8fafc" font-mono font-size="10">A</text>
            `;
        }
    } else {
        if (btnS) btnS.className = 'flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs';
        if (btnR) btnR.className = 'flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs';
        if (badge) badge.textContent = 'Exact Bisector (45° & 45°)';
        if (txt) txt.textContent = 'Square: Exactly bisects the 90° corner into 45° and 45°!';
        if (svg) {
            svg.innerHTML = `
                <rect x="55" y="25" width="80" height="80" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                <line x1="55" y1="105" x2="135" y2="25" stroke="#38bdf8" stroke-width="2.5" />
                <path d="M 75,105 A 20,20 0 0,0 69,91" fill="none" stroke="#f59e0b" stroke-width="2" />
                <text x="78" y="100" fill="#f59e0b" font-mono font-size="9">45°</text>
                <path d="M 55,85 A 20,20 0 0,1 69,91" fill="none" stroke="#f59e0b" stroke-width="2" />
                <text x="60" y="80" fill="#f59e0b" font-mono font-size="9">45°</text>
                <circle cx="55" cy="105" r="3.5" fill="#f8fafc" /><text x="44" y="115" fill="#f8fafc" font-mono font-size="10">A</text>
            `;
        }
    }
}

// Sim 14: Constructing from Diagonals
function updateSim14() {
    const val = parseInt(document.getElementById('sim14_diag')?.value || 70);
    const diagCm = (val / 10).toFixed(1);
    const diagVal = document.getElementById('sim14_diag_val');
    const desc = document.getElementById('sim14_desc');
    const svg = document.getElementById('sim14_svg');

    if (diagVal) diagVal.textContent = `${diagCm} cm`;

    const baseCm = 5.0;
    const breadthCm = Math.sqrt(diagCm * diagCm - baseCm * baseCm).toFixed(2);
    if (desc) desc.textContent = `Base AB = 5 cm | Diagonal AC = ${diagCm} cm → Height BC = ${breadthCm} cm`;

    if (!svg) return;
    const scale = 18;
    const ax = 30, ay = 110;
    const bx = ax + baseCm * scale, by = ay;
    const cy = ay - breadthCm * scale;

    svg.innerHTML = `
        <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#38bdf8" stroke-width="2.5" />
        <text x="${(ax+bx)/2}" y="${ay+16}" fill="#38bdf8" font-mono font-size="9" text-anchor="middle">AB = 5 cm</text>
        <line x1="${bx}" y1="${by}" x2="${bx}" y2="20" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,2" />
        <rect x="${bx-8}" y="${by-8}" width="8" height="8" fill="none" stroke="#64748b" stroke-width="1" />
        <!-- Diagonal AC line -->
        <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${cy}" stroke="#f59e0b" stroke-width="2.5" />
        <text x="${(ax+bx)/2-10}" y="${(ay+cy)/2-6}" fill="#f59e0b" font-mono font-size="9">AC = ${diagCm} cm</text>
        <!-- Arc cut at C -->
        <circle cx="${bx}" cy="${cy}" r="4" fill="#10b981" />
        <text x="${bx+8}" y="${cy+4}" fill="#10b981" font-mono font-size="10" font-weight="bold">C</text>
        <circle cx="${ax}" cy="${ay}" r="3.5" fill="#fbbf24" /><text x="${ax-8}" y="${ay+6}" fill="#fbbf24" font-mono font-size="9">A</text>
        <circle cx="${bx}" cy="${by}" r="3.5" fill="#fbbf24" /><text x="${bx+8}" y="${by+6}" fill="#fbbf24" font-mono font-size="9">B</text>
    `;
}

// Sim 15: Equidistant Points (Dual Arc)
function updateSim15() {
    const val = parseInt(document.getElementById('sim15_r')?.value || 50);
    const rCm = (val / 10).toFixed(1);
    const rVal = document.getElementById('sim15_r_val');
    const badge = document.getElementById('sim15_badge');
    const desc = document.getElementById('sim15_desc');
    const svg = document.getElementById('sim15_svg');

    if (rVal) rVal.textContent = `${rCm} cm`;

    const distBC = 6.0;
    const canMeet = (parseFloat(rCm) >= distBC / 2);

    if (badge) {
        if (canMeet) {
            badge.className = 'text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
            badge.textContent = `Point A Located (AB = AC = ${rCm} cm)`;
        } else {
            badge.className = 'text-[11px] font-mono px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30';
            badge.textContent = "Arcs Don't Meet (r < 3 cm)";
        }
    }

    if (desc) {
        if (canMeet) {
            const h = Math.sqrt(rCm * rCm - 9.0).toFixed(2);
            desc.textContent = `BC = 6 cm | Radii = ${rCm} cm → Isosceles Triangle Height = ${h} cm!`;
        } else {
            desc.textContent = 'Radius must be at least 3 cm (half of BC) for arcs to meet!';
        }
    }

    if (!svg) return;
    const scale = 20;
    const bx = 60, by = 110;
    const cx = bx + distBC * scale, cy = by;
    const rPx = rCm * scale;

    svg.innerHTML = `
        <line x1="${bx}" y1="${by}" x2="${cx}" y2="${cy}" stroke="#64748b" stroke-width="2" />
        <circle cx="${bx}" cy="${by}" r="3.5" fill="#38bdf8" /><text x="${bx-10}" y="${by+6}" fill="#38bdf8" font-mono font-size="10">B</text>
        <circle cx="${cx}" cy="${cy}" r="3.5" fill="#38bdf8" /><text x="${cx+8}" y="${by+6}" fill="#38bdf8" font-mono font-size="10">C</text>
        <path d="M ${bx + rPx * Math.cos(-Math.PI/6)} ${by + rPx * Math.sin(-Math.PI/6)} A ${rPx} ${rPx} 0 0 0 ${bx + rPx * Math.cos(-Math.PI/2)} ${by - rPx}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,2" />
        <path d="M ${cx + rPx * Math.cos(-Math.PI/2)} ${cy - rPx} A ${rPx} ${rPx} 0 0 0 ${cx - rPx * Math.cos(-Math.PI/6)} ${cy + rPx * Math.sin(-Math.PI/6)}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="3,2" />
    `;

    if (canMeet) {
        const ax = (bx + cx) / 2;
        const hPx = Math.sqrt(rPx * rPx - (distBC * scale / 2) * (distBC * scale / 2));
        const ay = by - hPx;

        svg.innerHTML += `
            <line x1="${bx}" y1="${by}" x2="${ax}" y2="${ay}" stroke="#f59e0b" stroke-width="2" />
            <line x1="${cx}" y1="${cy}" x2="${ax}" y2="${ay}" stroke="#10b981" stroke-width="2" />
            <circle cx="${ax}" cy="${ay}" r="4.5" fill="#f43f5e" />
            <text x="${ax}" y="${ay-8}" fill="#f43f5e" font-mono font-size="11" font-weight="bold" text-anchor="middle">A</text>
        `;
    }
}

// Sim 16: The Composite House
let sim16Layers = { walls: true, door: true, eave: true, roof: true };

function toggleSim16(layer) {
    sim16Layers[layer] = !sim16Layers[layer];
    const btn = document.getElementById({ walls: 'sim16_b1', door: 'sim16_b2', eave: 'sim16_b3', roof: 'sim16_b4' }[layer]);
    if (btn) {
        if (sim16Layers[layer]) {
            btn.className = 'py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30';
        } else {
            btn.className = 'py-1 rounded bg-slate-800 text-slate-500 border border-slate-700';
        }
    }
    renderSim16();
}

function renderSim16() {
    const svg = document.getElementById('sim16_svg');
    if (!svg) return;

    svg.innerHTML = '';
    // House base coordinate
    const bx = 60, by = 130, size = 80;

    if (sim16Layers.walls) {
        svg.innerHTML += `
            <rect x="${bx}" y="${by-size}" width="${size}" height="${size}" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
            <text x="${bx+4}" y="${by-size-4}" fill="#f59e0b" font-mono font-size="8">D</text>
            <text x="${bx+size+2}" y="${by-size-4}" fill="#f59e0b" font-mono font-size="8">C</text>
        `;
    }
    if (sim16Layers.door) {
        svg.innerHTML += `
            <rect x="${bx + 26}" y="${by - 40}" width="28" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
        `;
    }
    if (sim16Layers.eave) {
        svg.innerHTML += `
            <path d="M ${bx + 22},${by - 40} A 18,10 0 0,1 ${bx + 58},${by - 40}" fill="none" stroke="#10b981" stroke-width="2" />
        `;
    }
    if (sim16Layers.roof) {
        const apexX = bx + size / 2, apexY = by - size - 45;
        svg.innerHTML += `
            <polygon points="${bx},${by-size} ${bx+size},${by-size} ${apexX},${apexY}" fill="#8b5cf6" fill-opacity="0.25" stroke="#a855f7" stroke-width="2" />
            <circle cx="${apexX}" cy="${apexY}" r="3" fill="#f43f5e" />
            <text x="${apexX}" y="${apexY-6}" fill="#f43f5e" font-mono font-size="9" font-weight="bold" text-anchor="middle">R (Apex)</text>
        `;
    }
}
'''

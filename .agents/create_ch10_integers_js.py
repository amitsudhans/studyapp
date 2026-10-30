import re

js_code = r'''
// Integers Chapter Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis
let isSpeaking = false;
function speakMentor(text) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    if (isSpeaking) {
        isSpeaking = false;
        return;
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    utterance.pitch = 1.0;
    utterance.onend = () => { isSpeaking = false; };
    utterance.onerror = () => { isSpeaking = false; };
    isSpeaking = true;
    window.speechSynthesis.speak(utterance);
}

// Navigation
function updateSlideDisplay() {
    for (let i = 1; i <= totalSlides; i++) {
        const slide = document.getElementById(`slide-${i}`);
        if (slide) {
            slide.style.display = (i === currentSlide) ? 'block' : 'none';
        }
    }
    const indicator = document.getElementById('slideIndicator');
    if (indicator) {
        indicator.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }
    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;
    }
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
    }
    if (nextBtn) {
        if (currentSlide === totalSlides) {
            nextBtn.style.display = 'none';
        } else {
            nextBtn.style.display = 'inline-flex';
        }
    }
    if (lastSlideNotice) {
        lastSlideNotice.style.display = (currentSlide === totalSlides) ? 'block' : 'none';
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        currentSlide++;
        updateSlideDisplay();
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        currentSlide--;
        updateSlideDisplay();
    }
}

function goToSlide(n) {
    if (n >= 1 && n <= totalSlides) {
        currentSlide = n;
        updateSlideDisplay();
    }
}

// Checkpoint Verification
function checkCheckpoint(cpId, selectedOption, correctOption, explanation) {
    const feedbackEl = document.getElementById(`cp-feedback-${cpId}`);
    const badgeEl = document.getElementById(`cp-badge-${cpId}`);
    if (!feedbackEl) return;

    if (selectedOption === correctOption) {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-emerald-950/40 border border-emerald-500/50 text-emerald-300';
        feedbackEl.innerHTML = `<strong>Correct!</strong> ` + explanation;
        if (badgeEl) {
            badgeEl.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
            badgeEl.textContent = 'Solved';
        }
    } else {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-rose-950/40 border border-rose-500/50 text-rose-300';
        feedbackEl.innerHTML = `<strong>Try again:</strong> Review the integer rules and elevator motion!`;
    }
    feedbackEl.style.display = 'block';
}

// Solution Modal
function openSolutionModal(title, question, correctAnswer, explanation) {
    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const questionEl = document.getElementById('modalQuestion');
    const answerEl = document.getElementById('modalAnswer');
    const explanationEl = document.getElementById('modalExplanation');

    if (modal && titleEl && questionEl && answerEl && explanationEl) {
        titleEl.textContent = title;
        questionEl.innerHTML = `<strong>Question:</strong> ${question}`;
        answerEl.innerHTML = `<strong>Correct Answer:</strong> ${correctAnswer}`;
        explanationEl.innerHTML = `<strong>Detailed Step-by-Step Solution:</strong><br>${explanation}`;
        modal.style.display = 'flex';
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Quiz Option Selection
function selectQuizOption(qId, selectedOpt, correctOpt, title, questionText, explanation) {
    const btnContainer = document.getElementById(`q-options-${qId}`);
    const feedbackBox = document.getElementById(`q-feedback-${qId}`);
    const solutionBtn = document.getElementById(`q-sol-btn-${qId}`);

    if (btnContainer) {
        const buttons = btnContainer.querySelectorAll('button');
        buttons.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === correctOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-emerald-500/20 border-emerald-400 text-emerald-200';
            } else if (idx === selectedOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-rose-500/20 border-rose-400 text-rose-200';
            } else {
                btn.className = 'w-full text-left p-3 rounded-xl border text-sm font-medium transition bg-slate-800/40 border-slate-700/60 text-slate-400 opacity-60';
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.style.display = 'block';
        if (selectedOpt === correctOpt) {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-sm bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
            feedbackBox.innerHTML = `<strong>Great job!</strong> ${explanation}`;
        } else {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-sm bg-rose-950/40 border border-rose-500/40 text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect.</strong> Click "View Step-by-Step Solution" below for full breakdown.`;
        }
    }

    if (solutionBtn) {
        solutionBtn.style.display = 'inline-flex';
    }
}

// -------------------------------------------------------------
// Simulator 1: Number Evolution
// -------------------------------------------------------------
let sim1Stage = 'natural';

function setSim1Stage(stage) {
    sim1Stage = stage;
    const svg = document.getElementById('sim1-svg');
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    ['natural', 'whole', 'integers'].forEach(s => {
        const btn = document.getElementById(`sim1-btn-${s}`);
        if (btn) {
            btn.className = (s === stage) ?
                'px-3 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    let lineSvg = '';
    if (stage === 'natural') {
        badge.textContent = "1. Counting Numbers (N)";
        desc.innerHTML = "Counting numbers began at 1 and extended rightwards: 1, 2, 3, 4, 5... Used for counting sheep, grain sheaves, and coins.";
        lineSvg = `
            <!-- Ray starting at 1 -->
            <line x1="200" y1="80" x2="470" y2="80" stroke="#38bdf8" stroke-width="3" />
            <polygon points="480,80 465,75 465,85" fill="#38bdf8"/>
            <circle cx="200" cy="80" r="5" fill="#38bdf8"/>
            <text x="200" y="110" fill="#38bdf8" font-size="12" text-anchor="middle" font-weight="bold">1</text>
            <circle cx="260" cy="80" r="4" fill="#38bdf8"/>
            <text x="260" y="110" fill="#38bdf8" font-size="12" text-anchor="middle">2</text>
            <circle cx="320" cy="80" r="4" fill="#38bdf8"/>
            <text x="320" y="110" fill="#38bdf8" font-size="12" text-anchor="middle">3</text>
            <circle cx="380" cy="80" r="4" fill="#38bdf8"/>
            <text x="380" y="110" fill="#38bdf8" font-size="12" text-anchor="middle">4</text>
            <circle cx="440" cy="80" r="4" fill="#38bdf8"/>
            <text x="440" y="110" fill="#38bdf8" font-size="12" text-anchor="middle">5</text>
            <text x="340" y="45" fill="#94a3b8" font-size="11" text-anchor="middle">Counting Number Ray (Starts at 1 →)</text>
        `;
    } else if (stage === 'whole') {
        badge.textContent = "2. Whole Numbers (W)";
        desc.innerHTML = "Zero (0) was born to represent emptiness or absence. The ray expanded left to start at 0: 0, 1, 2, 3, 4...";
        lineSvg = `
            <!-- Ray starting at 0 -->
            <line x1="140" y1="80" x2="470" y2="80" stroke="#fbbf24" stroke-width="3" />
            <polygon points="480,80 465,75 465,85" fill="#fbbf24"/>
            <circle cx="140" cy="80" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
            <text x="140" y="110" fill="#fbbf24" font-size="13" text-anchor="middle" font-weight="bold">0</text>
            <circle cx="200" cy="80" r="4" fill="#fbbf24"/>
            <text x="200" y="110" fill="#fbbf24" font-size="12" text-anchor="middle">1</text>
            <circle cx="260" cy="80" r="4" fill="#fbbf24"/>
            <text x="260" y="110" fill="#fbbf24" font-size="12" text-anchor="middle">2</text>
            <circle cx="320" cy="80" r="4" fill="#fbbf24"/>
            <text x="320" y="110" fill="#fbbf24" font-size="12" text-anchor="middle">3</text>
            <circle cx="380" cy="80" r="4" fill="#fbbf24"/>
            <text x="380" y="110" fill="#fbbf24" font-size="12" text-anchor="middle">4</text>
            <text x="300" y="45" fill="#fbbf24" font-size="11" text-anchor="middle">Whole Number Ray (Origin at 0 →)</text>
        `;
    } else {
        badge.textContent = "3. Complete Integers (Z)";
        desc.innerHTML = "The ray extends in BOTH directions! Negative numbers (−1, −2, −3...) populate the realm left of zero, creating the infinite two-sided Number Line.";
        lineSvg = `
            <!-- Infinite line extending left and right -->
            <line x1="20" y1="80" x2="480" y2="80" stroke="#a855f7" stroke-width="3" />
            <polygon points="10,80 25,75 25,85" fill="#a855f7"/>
            <polygon points="490,80 475,75 475,85" fill="#a855f7"/>
            <!-- Negative Numbers (Red/Purple) -->
            <circle cx="70" cy="80" r="4" fill="#f43f5e"/>
            <text x="70" y="110" fill="#f43f5e" font-size="12" text-anchor="middle" font-weight="bold">−3</text>
            <circle cx="130" cy="80" r="4" fill="#f43f5e"/>
            <text x="130" y="110" fill="#f43f5e" font-size="12" text-anchor="middle" font-weight="bold">−2</text>
            <circle cx="190" cy="80" r="4" fill="#f43f5e"/>
            <text x="190" y="110" fill="#f43f5e" font-size="12" text-anchor="middle" font-weight="bold">−1</text>
            <!-- Zero Origin (Amber) -->
            <circle cx="250" cy="80" r="6" fill="#fbbf24" stroke="#fff" stroke-width="1.5"/>
            <text x="250" y="110" fill="#fbbf24" font-size="13" text-anchor="middle" font-weight="bold">0</text>
            <!-- Positive Numbers (Green/Cyan) -->
            <circle cx="310" cy="80" r="4" fill="#10b981"/>
            <text x="310" y="110" fill="#10b981" font-size="12" text-anchor="middle" font-weight="bold">+1</text>
            <circle cx="370" cy="80" r="4" fill="#10b981"/>
            <text x="370" y="110" fill="#10b981" font-size="12" text-anchor="middle" font-weight="bold">+2</text>
            <circle cx="430" cy="80" r="4" fill="#10b981"/>
            <text x="430" y="110" fill="#10b981" font-size="12" text-anchor="middle" font-weight="bold">+3</text>
            <text x="130" y="45" fill="#f43f5e" font-size="11" text-anchor="middle">← Negative Integers</text>
            <text x="370" y="45" fill="#10b981" font-size="11" text-anchor="middle">Positive Integers →</text>
        `;
    }
    svg.innerHTML = lineSvg;
}

// -------------------------------------------------------------
// Simulator 2: Bela's Fun Elevator
// -------------------------------------------------------------
let sim2CurFloor = 0;

function sim2GoTo(targetFloor) {
    sim2CurFloor = targetFloor;
    renderSim2();
}

function renderSim2() {
    const svg = document.getElementById('sim2-svg');
    const badge = document.getElementById('sim2-floor-badge');
    const status = document.getElementById('sim2-status');

    const floorNames = {
        3: "+3 Roof Terrace",
        2: "+2 Sundae Parlor",
        1: "+1 Cone Bakery",
        0: "0 Ground Lobby (Street Entrance)",
        "-1": "−1 Cold Storage Basement",
        "-2": "−2 Chocolate Vault Basement",
        "-3": "−3 Deep Freeze Vault"
    };

    badge.textContent = `Floor ${sim2CurFloor > 0 ? '+' : ''}${sim2CurFloor}`;
    badge.className = sim2CurFloor > 0 ?
        'px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' :
        (sim2CurFloor < 0 ?
            'px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30' :
            'px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30');

    status.textContent = `Doors open at ${floorNames[sim2CurFloor]}!`;

    // Map floor -3..3 to y positions: 3 is top (y=25), 0 is middle (y=130), -3 is bottom (y=235)
    // y = 130 - floor * 35
    const cabY = 130 - sim2CurFloor * 35 - 15;

    let floorsSvg = '';
    for (let f = 3; f >= -3; f--) {
        const lineY = 130 - f * 35;
        const isGround = (f === 0);
        floorsSvg += `
            <line x1="60" y1="${lineY}" x2="260" y2="${lineY}" stroke="${isGround ? '#f59e0b' : '#334155'}" stroke-width="${isGround ? 2 : 1}" stroke-dasharray="${isGround ? 'none' : '3,3'}"/>
            <text x="45" y="${lineY + 4}" fill="${f > 0 ? '#34d399' : (f < 0 ? '#f87171' : '#fbbf24')}" font-size="11" font-weight="bold" text-anchor="end">${f > 0 ? '+' + f : f}</text>
        `;
    }

    svg.innerHTML = `
        <!-- Elevator shaft tracks -->
        <line x1="80" y1="10" x2="80" y2="250" stroke="#475569" stroke-width="2"/>
        <line x1="160" y1="10" x2="160" y2="250" stroke="#475569" stroke-width="2"/>
        ${floorsSvg}
        <!-- Ground Line Indicator -->
        <text x="210" y="125" fill="#fbbf24" font-size="10" font-weight="bold">Ground Level (0)</text>
        <!-- Elevator Cable -->
        <line x1="120" y1="10" x2="120" y2="${cabY}" stroke="#94a3b8" stroke-width="1.5"/>
        <!-- Elevator Cabin -->
        <rect x="85" y="${cabY}" width="70" height="30" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="120" y="${cabY + 19}" fill="#38bdf8" font-size="11" text-anchor="middle" font-weight="bold">Bela 👧 [${sim2CurFloor > 0 ? '+' : ''}${sim2CurFloor}]</text>
    `;
}

// -------------------------------------------------------------
// Simulator 3: Signs & Direction
// -------------------------------------------------------------
let sim3Dir = 1;

function setSim3Dir(dir) {
    sim3Dir = dir;
    document.getElementById('sim3-btn-up').className = (dir === 1) ?
        'py-2.5 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition flex items-center justify-center space-x-1.5' :
        'py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition flex items-center justify-center space-x-1.5';
    document.getElementById('sim3-btn-down').className = (dir === -1) ?
        'py-2.5 rounded-xl text-xs font-bold bg-rose-500 text-slate-950 transition flex items-center justify-center space-x-1.5' :
        'py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition flex items-center justify-center space-x-1.5';
    updateSim3();
}

function updateSim3() {
    const dist = parseInt(document.getElementById('sim3-dist').value, 10);
    document.getElementById('sim3-dist-val').textContent = `${dist} Floors`;
    const badge = document.getElementById('sim3-badge');
    const svg = document.getElementById('sim3-svg');

    const signedVal = sim3Dir * dist;
    badge.textContent = sim3Dir === 1 ? `Upward Motion (+${dist})` : `Downward Motion (−${dist})`;
    badge.className = sim3Dir === 1 ?
        'px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' :
        'px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30';

    const startY = sim3Dir === 1 ? 160 : 40;
    const endY = sim3Dir === 1 ? (160 - dist * 24) : (40 + dist * 24);
    const color = sim3Dir === 1 ? '#10b981' : '#f43f5e';

    svg.innerHTML = `
        <line x1="120" y1="20" x2="120" y2="180" stroke="#334155" stroke-width="2"/>
        <circle cx="120" cy="${startY}" r="6" fill="#f59e0b"/>
        <text x="100" y="${startY + 4}" fill="#f59e0b" font-size="11" text-anchor="end">Start</text>
        
        <!-- Vector Arrow -->
        <line x1="120" y1="${startY}" x2="120" y2="${endY}" stroke="${color}" stroke-width="4"/>
        <polygon points="120,${endY} 113,${sim3Dir === 1 ? endY + 12 : endY - 12} 127,${sim3Dir === 1 ? endY + 12 : endY - 12}" fill="${color}"/>
        <circle cx="120" cy="${endY}" r="6" fill="${color}"/>
        <text x="100" y="${endY + 4}" fill="${color}" font-size="11" text-anchor="end" font-weight="bold">End</text>
        
        <!-- Formula Display Card -->
        <rect x="180" y="55" width="190" height="85" rx="8" fill="#1e293b" stroke="${color}" stroke-width="1.5"/>
        <text x="275" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">Signed Displacement</text>
        <text x="275" y="115" fill="${color}" font-size="20" text-anchor="middle" font-weight="bold">${signedVal > 0 ? '+' + signedVal : signedVal}</text>
    `;
}

// -------------------------------------------------------------
// Simulator 4: Tracking Movement
// -------------------------------------------------------------
function updateSim4() {
    const start = parseInt(document.getElementById('sim4-start').value, 10);
    const move = parseInt(document.getElementById('sim4-move').value, 10);
    const target = start + move;

    document.getElementById('sim4-start-val').textContent = `${start > 0 ? '+' : ''}${start}`;
    document.getElementById('sim4-move-val').textContent = `${move > 0 ? '+' : ''}${move} (${move >= 0 ? 'Up' : 'Down'})`;
    document.getElementById('sim4-eq-badge').textContent = `(${start > 0 ? '+' : ''}${start}) + (${move > 0 ? '+' : ''}${move}) = ${target > 0 ? '+' : ''}${target}`;

    const svg = document.getElementById('sim4-svg');
    const info = document.getElementById('sim4-info');
    info.textContent = `Starting at Floor ${start > 0 ? '+' : ''}${start}, moving ${Math.abs(move)} floors ${move >= 0 ? 'up' : 'down'} lands on Floor ${target > 0 ? '+' : ''}${target}.`;

    // Map -7 to 7 on scale x from 40 to 410
    const mapX = (val) => 225 + val * 24;
    const startX = mapX(start);
    const targetX = mapX(target);

    let ticksSvg = '';
    for (let i = -7; i <= 7; i++) {
        const x = mapX(i);
        const isZero = (i === 0);
        ticksSvg += `
            <line x1="${x}" y1="85" x2="${x}" y2="95" stroke="${isZero ? '#f59e0b' : '#475569'}" stroke-width="${isZero ? 2.5 : 1}"/>
            <text x="${x}" y="115" fill="${isZero ? '#f59e0b' : '#94a3b8'}" font-size="${isZero ? 12 : 10}" text-anchor="middle" font-weight="${isZero ? 'bold' : 'normal'}">${i > 0 ? '+' + i : i}</text>
        `;
    }

    // Arc from start to target
    const midX = (startX + targetX) / 2;
    const arcHeight = Math.min(60, Math.abs(startX - targetX) * 0.4);
    const arcY = 90 - arcHeight;

    svg.innerHTML = `
        <line x1="30" y1="90" x2="420" y2="90" stroke="#64748b" stroke-width="2"/>
        ${ticksSvg}
        <!-- Motion Arc -->
        <path d="M${startX},90 Q${midX},${arcY} ${targetX},90" fill="none" stroke="${move >= 0 ? '#10b981' : '#f43f5e'}" stroke-width="3"/>
        <circle cx="${startX}" cy="90" r="5" fill="#38bdf8"/>
        <text x="${startX}" y="70" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">Start</text>
        <circle cx="${targetX}" cy="90" r="6" fill="${move >= 0 ? '#10b981' : '#f43f5e'}"/>
        <text x="${targetX}" y="70" fill="${move >= 0 ? '#10b981' : '#f43f5e'}" font-size="10" text-anchor="middle" font-weight="bold">Target</text>
    `;
}

// -------------------------------------------------------------
// Simulator 5: Additive Inverses
// -------------------------------------------------------------
let sim5InverseTriggered = false;

function updateSim5() {
    sim5InverseTriggered = false;
    const val = parseInt(document.getElementById('sim5-val').value, 10);
    document.getElementById('sim5-val-display').textContent = val;
    renderSim5();
}

function triggerSim5Inverse() {
    sim5InverseTriggered = true;
    renderSim5();
}

function renderSim5() {
    const val = parseInt(document.getElementById('sim5-val').value, 10);
    const svg = document.getElementById('sim5-svg');
    const status = document.getElementById('sim5-status');

    const mapX = (v) => 225 + v * 30;
    const zeroX = mapX(0);
    const posX = mapX(val);

    let ticksSvg = '';
    for (let i = -6; i <= 6; i++) {
        const x = mapX(i);
        const isZero = (i === 0);
        ticksSvg += `
            <line x1="${x}" y1="85" x2="${x}" y2="95" stroke="${isZero ? '#f59e0b' : '#475569'}" stroke-width="${isZero ? 2.5 : 1}"/>
            <text x="${x}" y="115" fill="${isZero ? '#f59e0b' : '#94a3b8'}" font-size="${isZero ? 12 : 10}" text-anchor="middle" font-weight="${isZero ? 'bold' : 'normal'}">${i > 0 ? '+' + i : i}</text>
        `;
    }

    let inverseArcSvg = '';
    if (sim5InverseTriggered) {
        inverseArcSvg = `
            <path d="M${posX},90 Q${(posX + zeroX)/2},135 ${zeroX},90" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4,3"/>
            <polygon points="${zeroX},90 ${zeroX + 10},96 ${zeroX + 10},84" fill="#f43f5e"/>
            <text x="${(posX + zeroX)/2}" y="150" fill="#f43f5e" font-size="11" text-anchor="middle" font-weight="bold">−${val} (Return to Zero)</text>
        `;
        status.innerHTML = `<span class="text-emerald-400 font-semibold">Cancelled!</span> (+${val}) + (−${val}) = 0. The additive inverse returned the elevator precisely back to the ground origin.`;
    } else {
        status.innerHTML = `<span class="text-slate-300">Initial forward jump of +${val}. Click "Apply Inverse" to return to 0.</span>`;
    }

    svg.innerHTML = `
        <line x1="30" y1="90" x2="420" y2="90" stroke="#64748b" stroke-width="2"/>
        ${ticksSvg}
        <!-- Initial Forward Arc -->
        <path d="M${zeroX},90 Q${(zeroX + posX)/2},40 ${posX},90" fill="none" stroke="#10b981" stroke-width="3"/>
        <polygon points="${posX},90 ${posX - 10},84 ${posX - 10},96" fill="#10b981"/>
        <text x="${(zeroX + posX)/2}" y="35" fill="#10b981" font-size="11" text-anchor="middle" font-weight="bold">+${val}</text>
        ${inverseArcSvg}
    `;
}

// -------------------------------------------------------------
// Simulator 6: Floor Heights Comparison
// -------------------------------------------------------------
function updateSim6() {
    const a = parseInt(document.getElementById('sim6-slider-a').value, 10);
    const b = parseInt(document.getElementById('sim6-slider-b').value, 10);

    document.getElementById('sim6-val-a').textContent = `${a > 0 ? '+' : ''}${a}`;
    document.getElementById('sim6-val-b').textContent = `${b > 0 ? '+' : ''}${b}`;

    const badge = document.getElementById('sim6-comp-badge');
    const conclusion = document.getElementById('sim6-conclusion');

    let symbol = '=';
    let textDesc = '';
    if (a > b) {
        symbol = '>';
        textDesc = `Floor ${a > 0 ? '+' : ''}${a} is higher up than Floor ${b > 0 ? '+' : ''}${b}, so (${a > 0 ? '+' : ''}${a}) > (${b > 0 ? '+' : ''}${b}).`;
    } else if (a < b) {
        symbol = '<';
        textDesc = `Floor ${a > 0 ? '+' : ''}${a} is lower/deeper than Floor ${b > 0 ? '+' : ''}${b}, so (${a > 0 ? '+' : ''}${a}) < (${b > 0 ? '+' : ''}${b}).`;
    } else {
        symbol = '=';
        textDesc = `Both elevators are on the exact same level (${a}).`;
    }

    badge.textContent = `(${a > 0 ? '+' : ''}${a}) ${symbol} (${b > 0 ? '+' : ''}${b})`;
    conclusion.textContent = textDesc;

    const svg = document.getElementById('sim6-svg');
    // Map -6..6 to vertical shaft y: +6 is 20, 0 is 100, -6 is 180 -> y = 100 - val * 13
    const yA = 100 - a * 13;
    const yB = 100 - b * 13;

    let linesSvg = '';
    for (let f = 6; f >= -6; f--) {
        const y = 100 - f * 13;
        linesSvg += `<line x1="80" y1="${y}" x2="360" y2="${y}" stroke="${f === 0 ? '#f59e0b' : '#334155'}" stroke-dasharray="${f === 0 ? 'none' : '2,3'}"/>`;
    }

    svg.innerHTML = `
        <line x1="140" y1="10" x2="140" y2="190" stroke="#475569" stroke-width="2"/>
        <line x1="300" y1="10" x2="300" y2="190" stroke="#475569" stroke-width="2"/>
        ${linesSvg}
        <text x="70" y="104" fill="#f59e0b" font-size="10" font-weight="bold">Floor 0</text>
        
        <!-- Cab A -->
        <rect x="115" y="${yA - 10}" width="50" height="20" rx="3" fill="#065f46" stroke="#10b981" stroke-width="2"/>
        <text x="140" y="${yA + 4}" fill="#ecfdf5" font-size="10" text-anchor="middle" font-weight="bold">A [${a > 0 ? '+' : ''}${a}]</text>
        
        <!-- Cab B -->
        <rect x="275" y="${yB - 10}" width="50" height="20" rx="3" fill="#881337" stroke="#f43f5e" stroke-width="2"/>
        <text x="300" y="${yB + 4}" fill="#fff1f2" font-size="10" text-anchor="middle" font-weight="bold">B [${b > 0 ? '+' : ''}${b}]</text>
    `;
}

// -------------------------------------------------------------
// Simulator 7: Finding the Shift
// -------------------------------------------------------------
function updateSim7() {
    const start = parseInt(document.getElementById('sim7-start').value, 10);
    const target = parseInt(document.getElementById('sim7-target').value, 10);
    const movement = target - start;

    document.getElementById('sim7-start-txt').textContent = `${start > 0 ? '+' : ''}${start}`;
    document.getElementById('sim7-target-txt').textContent = `${target > 0 ? '+' : ''}${target}`;
    document.getElementById('sim7-badge').textContent = `(${target > 0 ? '+' : ''}${target}) − (${start > 0 ? '+' : ''}${start}) = ${movement > 0 ? '+' : ''}${movement}`;

    const explanation = document.getElementById('sim7-explanation');
    explanation.textContent = `To travel from Floor ${start > 0 ? '+' : ''}${start} to Floor ${target > 0 ? '+' : ''}${target}, Bela must move ${Math.abs(movement)} floors ${movement >= 0 ? 'UP (+)' : 'DOWN (−)'}.`;

    const svg = document.getElementById('sim7-svg');
    const mapX = (v) => 225 + v * 35;
    const startX = mapX(start);
    const targetX = mapX(target);

    let ticksSvg = '';
    for (let i = -5; i <= 5; i++) {
        const x = mapX(i);
        const isZero = (i === 0);
        ticksSvg += `
            <line x1="${x}" y1="85" x2="${x}" y2="95" stroke="${isZero ? '#f59e0b' : '#475569'}" stroke-width="${isZero ? 2 : 1}"/>
            <text x="${x}" y="115" fill="${isZero ? '#f59e0b' : '#94a3b8'}" font-size="${isZero ? 12 : 10}" text-anchor="middle">${i > 0 ? '+' + i : i}</text>
        `;
    }

    svg.innerHTML = `
        <line x1="30" y1="90" x2="420" y2="90" stroke="#64748b" stroke-width="2"/>
        ${ticksSvg}
        <!-- Directed Vector -->
        <line x1="${startX}" y1="90" x2="${targetX}" y2="90" stroke="${movement >= 0 ? '#10b981' : '#f43f5e'}" stroke-width="4"/>
        <circle cx="${startX}" cy="90" r="6" fill="#38bdf8"/>
        <circle cx="${targetX}" cy="90" r="6" fill="${movement >= 0 ? '#10b981' : '#f43f5e'}"/>
        <text x="${startX}" y="65" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">Start (${start})</text>
        <text x="${targetX}" y="65" fill="${movement >= 0 ? '#10b981' : '#f43f5e'}" font-size="10" text-anchor="middle" font-weight="bold">Target (${target})</text>
    `;
}

// -------------------------------------------------------------
// Simulator 8: Mine Shafts & Scales
// -------------------------------------------------------------
function updateSim8() {
    const elev = parseInt(document.getElementById('sim8-slider').value, 10);
    document.getElementById('sim8-elevation-val').textContent = `${elev > 0 ? '+' : ''}${elev} m`;
    const desc = document.getElementById('sim8-text');

    if (elev > 0) {
        desc.innerHTML = `Miner is <strong class="text-emerald-400">${elev} meters ABOVE ground</strong> on the mountain processing conveyor.`;
    } else if (elev < 0) {
        desc.innerHTML = `Miner is <strong class="text-rose-400">${Math.abs(elev)} meters DEEP UNDERGROUND</strong> in the drainage extraction tunnel.`;
    } else {
        desc.innerHTML = `Miner is at <strong class="text-amber-400">0 m Ground Baseline</strong>.`;
    }

    const svg = document.getElementById('sim8-svg');
    // Map -500 to 500 to y from 180 down to 20: y = 100 - elev * 0.16
    const cabY = 100 - elev * 0.16;

    svg.innerHTML = `
        <!-- Sky and Ground Divider -->
        <rect x="40" y="20" width="370" height="80" fill="#0284c7" fill-opacity="0.1"/>
        <rect x="40" y="100" width="370" height="80" fill="#78350f" fill-opacity="0.15"/>
        <line x1="30" y1="100" x2="420" y2="100" stroke="#f59e0b" stroke-width="2"/>
        <text x="380" y="95" fill="#f59e0b" font-size="10" font-weight="bold">0 m Surface</text>
        
        <!-- Mine Shaft Cable Track -->
        <line x1="160" y1="20" x2="160" y2="180" stroke="#64748b" stroke-width="2"/>
        <line x1="160" y1="20" x2="160" y2="${cabY}" stroke="#e2e8f0" stroke-width="1.5"/>
        
        <!-- Miner Elevator Cage -->
        <rect x="135" y="${cabY - 12}" width="50" height="24" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="160" y="${cabY + 4}" fill="#f59e0b" font-size="10" text-anchor="middle" font-weight="bold">Cage</text>
        
        <!-- Elevation Label -->
        <text x="210" y="${cabY + 4}" fill="${elev >= 0 ? '#34d399' : '#f87171'}" font-size="12" font-weight="bold">
            ${elev > 0 ? '+' : ''}${elev} m
        </text>
    `;
}

// -------------------------------------------------------------
// Simulator 9: Double Negative Visualizer
// -------------------------------------------------------------
let sim9Scenario = 'debt';

function setSim9Scenario(scen) {
    sim9Scenario = scen;
    document.getElementById('sim9-btn-debt').className = (scen === 'debt') ?
        'w-1/2 py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'w-1/2 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim9-btn-walker').className = (scen === 'walker') ?
        'w-1/2 py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition' :
        'w-1/2 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    renderSim9();
}

function renderSim9() {
    const svg = document.getElementById('sim9-svg');
    const msg = document.getElementById('sim9-msg');

    if (sim9Scenario === 'debt') {
        msg.innerHTML = `<strong>Financial Law:</strong> Your account balance is ₹1,000. The bank discovers an erroneous debt of ₹300 (−300) and <em>cancels (subtracts)</em> it. <br><span class="text-cyan-300 font-mono">1000 − (−300) = 1000 + 300 = ₹1,300!</span> Taking away debt increases wealth!`;
        svg.innerHTML = `
            <rect x="60" y="30" width="140" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <text x="130" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Initial Balance</text>
            <text x="130" y="95" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">+₹1,000</text>
            
            <text x="225" y="85" fill="#f59e0b" font-size="22" font-weight="bold" text-anchor="middle">−</text>
            <text x="225" y="105" fill="#f43f5e" font-size="11" text-anchor="middle">(−₹300)</text>
            
            <rect x="250" y="30" width="140" height="100" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
            <text x="320" y="60" fill="#a7f3d0" font-size="11" text-anchor="middle">New Net Wealth</text>
            <text x="320" y="95" fill="#ecfdf5" font-size="20" font-weight="bold" text-anchor="middle">+₹1,300</text>
        `;
    } else {
        msg.innerHTML = `<strong>Walking Dynamics:</strong> A walker faces the Negative Direction (Left). Subtraction commands walking <em>BACKWARDS</em>. Walking backwards while facing left causes the body to travel <strong>FORWARDS TO THE RIGHT (+)</strong>!`;
        svg.innerHTML = `
            <line x1="30" y1="100" x2="420" y2="100" stroke="#64748b" stroke-width="2"/>
            <polygon points="425,100 410,95 410,105" fill="#64748b"/>
            <!-- Zero Origin -->
            <circle cx="150" cy="100" r="5" fill="#f59e0b"/>
            <text x="150" y="125" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">0</text>
            
            <!-- Hiker facing left -->
            <g transform="translate(150, 65)">
                <circle cx="0" cy="0" r="12" fill="#38bdf8"/>
                <text x="0" y="4" fill="#0f172a" font-size="10" text-anchor="middle" font-weight="bold">👀←</text>
            </g>
            <!-- Backward Walking Vector (Moves Right) -->
            <line x1="165" y1="65" x2="310" y2="65" stroke="#10b981" stroke-width="4"/>
            <polygon points="320,65 305,58 305,72" fill="#10b981"/>
            <text x="240" y="50" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Walk Backwards = Move Right (+)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 10: Horizontal Shift
// -------------------------------------------------------------
let sim10Rotated = false;

function toggleSim10Rotation() {
    sim10Rotated = !sim10Rotated;
    document.getElementById('sim10-badge').textContent = sim10Rotated ? "Horizontal Number Line Mode" : "Vertical Shaft Mode";
    document.getElementById('sim10-status').textContent = sim10Rotated ?
        "Rotated 90°! The vertical shaft has transformed into the horizontal number line. Up became Right (+), Down became Left (−)." :
        "Vertical elevator shaft mode. Up is positive (+), Down is negative (−), Ground is Floor 0.";
    renderSim10();
}

function renderSim10() {
    const svg = document.getElementById('sim10-svg');
    if (!sim10Rotated) {
        // Vertical shaft
        svg.innerHTML = `
            <g transform="translate(225, 100)">
                <line x1="0" y1="-80" x2="0" y2="80" stroke="#38bdf8" stroke-width="3"/>
                <circle cx="0" cy="0" r="6" fill="#f59e0b"/>
                <text x="20" y="4" fill="#f59e0b" font-size="11" font-weight="bold">Floor 0</text>
                <circle cx="0" cy="-40" r="4" fill="#10b981"/>
                <text x="20" y="-36" fill="#10b981" font-size="11">+1 (Up)</text>
                <circle cx="0" cy="-70" r="4" fill="#10b981"/>
                <text x="20" y="-66" fill="#10b981" font-size="11">+2 (Up)</text>
                <circle cx="0" cy="40" r="4" fill="#f43f5e"/>
                <text x="20" y="44" fill="#f43f5e" font-size="11">−1 (Down)</text>
                <circle cx="0" cy="70" r="4" fill="#f43f5e"/>
                <text x="20" y="74" fill="#f43f5e" font-size="11">−2 (Down)</text>
            </g>
        `;
    } else {
        // Horizontal line
        svg.innerHTML = `
            <g transform="translate(225, 100)">
                <line x1="-160" y1="0" x2="160" y2="0" stroke="#818cf8" stroke-width="3"/>
                <polygon points="170,0 155,-5 155,5" fill="#818cf8"/>
                <polygon points="-170,0 -155,-5 -155,5" fill="#818cf8"/>
                <circle cx="0" cy="0" r="6" fill="#f59e0b"/>
                <text x="0" y="25" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">0 (Origin)</text>
                <circle cx="60" cy="0" r="4" fill="#10b981"/>
                <text x="60" y="25" fill="#10b981" font-size="11" text-anchor="middle">+1 (Right)</text>
                <circle cx="120" cy="0" r="4" fill="#10b981"/>
                <text x="120" y="25" fill="#10b981" font-size="11" text-anchor="middle">+2 (Right)</text>
                <circle cx="-60" cy="0" r="4" fill="#f43f5e"/>
                <text x="-60" y="25" fill="#f43f5e" font-size="11" text-anchor="middle">−1 (Left)</text>
                <circle cx="-120" cy="0" r="4" fill="#f43f5e"/>
                <text x="-120" y="25" fill="#f43f5e" font-size="11" text-anchor="middle">−2 (Left)</text>
            </g>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 11: The Unmarked Line
// -------------------------------------------------------------
let sim11Problem = 1;

function setSim11Problem(p) {
    sim11Problem = p;
    ['p1', 'p2', 'p3'].forEach((id, idx) => {
        const btn = document.getElementById(`sim11-${id}`);
        if (btn) {
            btn.className = (idx + 1 === p) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });
    renderSim11();
}

function renderSim11() {
    const svg = document.getElementById('sim11-svg');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (sim11Problem === 1) {
        badge.textContent = "(−35) + (+50) = +15";
        desc.innerHTML = "From −35, leap +35 right to reach the <strong>0 Bridge</strong>. The remaining jump is 50 − 35 = +15 to the right, landing safely at <strong>+15</strong>.";
        svg.innerHTML = `
            <line x1="30" y1="100" x2="420" y2="100" stroke="#64748b" stroke-width="2"/>
            <circle cx="210" cy="100" r="6" fill="#f59e0b"/>
            <text x="210" y="125" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">0 (Bridge)</text>
            <!-- Start at -35 -->
            <circle cx="90" cy="100" r="5" fill="#f43f5e"/>
            <text x="90" y="125" fill="#f43f5e" font-size="11" text-anchor="middle" font-weight="bold">−35</text>
            <!-- Arc 1: -35 to 0 (+35) -->
            <path d="M90,100 Q150,50 210,100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="150" y="45" fill="#38bdf8" font-size="10" text-anchor="middle">+35 Jump</text>
            <!-- Arc 2: 0 to +15 (+15) -->
            <circle cx="290" cy="100" r="6" fill="#10b981"/>
            <text x="290" y="125" fill="#10b981" font-size="11" text-anchor="middle" font-weight="bold">+15</text>
            <path d="M210,100 Q250,65 290,100" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <text x="250" y="60" fill="#10b981" font-size="10" text-anchor="middle">+15 Remaining</text>
        `;
    } else if (sim11Problem === 2) {
        badge.textContent = "(+18) + (−30) = −12";
        desc.innerHTML = "From +18, jump 18 left to hit <strong>0</strong>. Then jump the remaining 30 − 18 = 12 further left, landing at <strong>−12</strong>.";
        svg.innerHTML = `
            <line x1="30" y1="100" x2="420" y2="100" stroke="#64748b" stroke-width="2"/>
            <circle cx="230" cy="100" r="6" fill="#f59e0b"/>
            <text x="230" y="125" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">0</text>
            <!-- Start at +18 -->
            <circle cx="330" cy="100" r="5" fill="#10b981"/>
            <text x="330" y="125" fill="#10b981" font-size="11" text-anchor="middle" font-weight="bold">+18</text>
            <!-- Arc 1: +18 to 0 (-18) -->
            <path d="M330,100 Q280,55 230,100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="280" y="50" fill="#38bdf8" font-size="10" text-anchor="middle">−18 Jump</text>
            <!-- Arc 2: 0 to -12 (-12) -->
            <circle cx="150" cy="100" r="6" fill="#f43f5e"/>
            <text x="150" y="125" fill="#f43f5e" font-size="11" text-anchor="middle" font-weight="bold">−12</text>
            <path d="M230,100 Q190,65 150,100" fill="none" stroke="#f43f5e" stroke-width="2.5"/>
            <text x="190" y="60" fill="#f43f5e" font-size="10" text-anchor="middle">−12 Remaining</text>
        `;
    } else {
        badge.textContent = "(−120) − (−150) = +30";
        desc.innerHTML = "Subtracting −150 is adding +150! From −120, jump 120 right to reach <strong>0</strong>, then jump the remaining 30 right to land at <strong>+30</strong>.";
        svg.innerHTML = `
            <line x1="30" y1="100" x2="420" y2="100" stroke="#64748b" stroke-width="2"/>
            <circle cx="250" cy="100" r="6" fill="#f59e0b"/>
            <text x="250" y="125" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">0</text>
            <circle cx="70" cy="100" r="5" fill="#f43f5e"/>
            <text x="70" y="125" fill="#f43f5e" font-size="11" text-anchor="middle" font-weight="bold">−120</text>
            <path d="M70,100 Q160,40 250,100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="160" y="35" fill="#38bdf8" font-size="10" text-anchor="middle">+120</text>
            <circle cx="330" cy="100" r="6" fill="#10b981"/>
            <text x="330" y="125" fill="#10b981" font-size="11" text-anchor="middle" font-weight="bold">+30</text>
            <path d="M250,100 Q290,65 330,100" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <text x="290" y="60" fill="#10b981" font-size="10" text-anchor="middle">+30</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 12: The Token Model
// -------------------------------------------------------------
let sim12Tokens = [
    { type: 'pos', id: 1 },
    { type: 'pos', id: 2 },
    { type: 'pos', id: 3 },
    { type: 'pos', id: 4 },
    { type: 'neg', id: 5 },
    { type: 'neg', id: 6 }
];

function addSim12Token(type) {
    if (sim12Tokens.length >= 16) return;
    sim12Tokens.push({ type, id: Date.now() + Math.random() });
    renderSim12();
}

function clearSim12Tokens() {
    sim12Tokens = [];
    renderSim12();
}

function pairSim12ZeroPairs() {
    let posCount = sim12Tokens.filter(t => t.type === 'pos').length;
    let negCount = sim12Tokens.filter(t => t.type === 'neg').length;
    const cancelCount = Math.min(posCount, negCount);

    if (cancelCount === 0) {
        document.getElementById('sim12-status').innerHTML = "No zero pairs available to cancel!";
        return;
    }

    // Keep remaining
    const remainingPos = posCount - cancelCount;
    const remainingNeg = negCount - cancelCount;
    sim12Tokens = [];
    for (let i = 0; i < remainingPos; i++) sim12Tokens.push({ type: 'pos', id: i });
    for (let i = 0; i < remainingNeg; i++) sim12Tokens.push({ type: 'neg', id: i + 100 });

    renderSim12();
    document.getElementById('sim12-status').innerHTML = `<span class="text-emerald-400 font-semibold">Cancelled ${cancelCount} Zero Pair(s)!</span> Positives and negatives eliminated each other.`;
}

function renderSim12() {
    const tray = document.getElementById('sim12-token-tray');
    if (!tray) return;

    let posCount = 0;
    let negCount = 0;
    let html = '';

    sim12Tokens.forEach(t => {
        if (t.type === 'pos') {
            posCount++;
            html += `<div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow-lg shadow-emerald-500/20 border-2 border-emerald-300 animate-fade">+1</div>`;
        } else {
            negCount++;
            html += `<div class="w-10 h-10 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-sm shadow-lg shadow-rose-500/20 border-2 border-rose-300 animate-fade">−1</div>`;
        }
    });

    if (sim12Tokens.length === 0) {
        html = '<span class="text-slate-500 text-xs italic">Tray is empty (0). Add tokens below!</span>';
    }
    tray.innerHTML = html;

    const net = posCount - negCount;
    const badge = document.getElementById('sim12-sum-badge');
    badge.textContent = `Net Value: ${net > 0 ? '+' : ''}${net}`;
    badge.className = net > 0 ?
        'font-mono text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20' :
        (net < 0 ?
            'font-mono text-xs font-bold text-rose-400 bg-rose-500/10 px-2.5 py-1 rounded-lg border border-rose-500/20' :
            'font-mono text-xs font-bold text-amber-400 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20');

    const status = document.getElementById('sim12-status');
    status.textContent = `${posCount} Green Tokens (+${posCount}) and ${negCount} Red Tokens (−${negCount}).`;
}

// -------------------------------------------------------------
// Simulator 13: Token Subtraction
// -------------------------------------------------------------
let sim13Step = 1;

function setSim13Step(s) {
    sim13Step = s;
    ['step1', 'step2', 'step3'].forEach((id, idx) => {
        const btn = document.getElementById(`sim13-${id}`);
        if (btn) {
            btn.className = (idx + 1 === s) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });
    renderSim13();
}

function renderSim13() {
    const display = document.getElementById('sim13-token-display');
    const desc = document.getElementById('sim13-desc');

    if (sim13Step === 1) {
        desc.innerHTML = "<strong>Step 1:</strong> You have 2 green tokens (+2). You must subtract −3 (take away 3 red tokens). But there are NO red tokens to take away!";
        display.innerHTML = `
            <div class="flex items-center justify-center space-x-3 p-4 bg-slate-900/60 rounded-xl border border-slate-800">
                <div class="w-12 h-12 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-base shadow">+1</div>
                <div class="w-12 h-12 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-base shadow">+1</div>
            </div>
            <p class="text-xs text-center text-slate-400">Total: +2 | Red tokens to take away: 0 found!</p>
        `;
    } else if (sim13Step === 2) {
        desc.innerHTML = "<strong>Step 2: Inject 3 Zero Pairs!</strong> Each (+1, −1) pair equals 0, so adding 3 pairs does not change the net value (+2). Now we have 3 red tokens available to remove!";
        display.innerHTML = `
            <div class="flex items-center justify-center space-x-4 p-4 bg-slate-900/60 rounded-xl border border-slate-800">
                <!-- Original -->
                <div class="flex space-x-2 border-r border-slate-700 pr-3">
                    <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-xs">+1</div>
                    <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-xs">+1</div>
                </div>
                <!-- Injected Pairs -->
                <div class="flex space-x-2">
                    <div class="p-1 rounded-lg border border-amber-500/40 bg-amber-500/5 flex flex-col items-center space-y-1">
                        <div class="w-8 h-8 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-[10px]">+1</div>
                        <div class="w-8 h-8 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-[10px]">−1</div>
                    </div>
                    <div class="p-1 rounded-lg border border-amber-500/40 bg-amber-500/5 flex flex-col items-center space-y-1">
                        <div class="w-8 h-8 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-[10px]">+1</div>
                        <div class="w-8 h-8 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-[10px]">−1</div>
                    </div>
                    <div class="p-1 rounded-lg border border-amber-500/40 bg-amber-500/5 flex flex-col items-center space-y-1">
                        <div class="w-8 h-8 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-[10px]">+1</div>
                        <div class="w-8 h-8 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-[10px]">−1</div>
                    </div>
                </div>
            </div>
            <p class="text-xs text-center text-amber-300">5 Green (+5) and 3 Red (−3) = Net Value is still +2!</p>
        `;
    } else {
        desc.innerHTML = "<strong>Step 3: Remove the 3 Red Tokens!</strong> Taking away the 3 red tokens leaves behind exactly 5 green tokens: <strong>(+2) − (−3) = +5</strong>!";
        display.innerHTML = `
            <div class="flex items-center justify-center space-x-2.5 p-4 bg-emerald-950/20 rounded-xl border border-emerald-500/30">
                <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow">+1</div>
                <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow">+1</div>
                <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow">+1</div>
                <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow">+1</div>
                <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-sm shadow">+1</div>
            </div>
            <p class="text-xs text-center text-emerald-400 font-bold">Result: 5 Green Tokens Remaining (+5)!</p>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 14: Real-World Balances
// -------------------------------------------------------------
let sim14Mode = 'bank';

function setSim14Mode(mode) {
    sim14Mode = mode;
    ['bank', 'sea', 'temp'].forEach(m => {
        const btn = document.getElementById(`sim14-btn-${m}`);
        if (btn) {
            btn.className = (m === mode) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });
    renderSim14();
}

function renderSim14() {
    const svg = document.getElementById('sim14-svg');
    const title = document.getElementById('sim14-gauge-title');
    const desc = document.getElementById('sim14-desc');

    if (sim14Mode === 'bank') {
        title.textContent = "Banking Ledger (Credits & Debits)";
        desc.innerHTML = "Depositing ₹500 is <strong>+₹500</strong>. Spending or paying a penalty of ₹300 is <strong>−₹300</strong>. Overdrawn accounts display negative balances.";
        svg.innerHTML = `
            <rect x="50" y="30" width="350" height="120" rx="8" fill="#1e293b" stroke="#334155"/>
            <text x="70" y="60" fill="#94a3b8" font-size="11">Opening Balance:</text>
            <text x="380" y="60" fill="#38bdf8" font-size="11" text-anchor="end">+₹1,200</text>
            <text x="70" y="85" fill="#f43f5e" font-size="11">Debit (Purchase):</text>
            <text x="380" y="85" fill="#f43f5e" font-size="11" text-anchor="end">−₹450</text>
            <line x1="70" y1="100" x2="380" y2="100" stroke="#475569"/>
            <text x="70" y="125" fill="#a7f3d0" font-size="12" font-weight="bold">Net Current Balance:</text>
            <text x="380" y="125" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="end">+₹750</text>
        `;
    } else if (sim14Mode === 'sea') {
        title.textContent = "Geographical Elevation & Sea Depth";
        desc.innerHTML = "Sea level is the universal reference datum (<strong>0 m</strong>). Mt. Everest stands at <strong>+8,848 m</strong> above sea level; the Mariana Trench plunges to <strong>−10,994 m</strong>.";
        svg.innerHTML = `
            <path d="M40,90 Q90,30 140,80 Q190,40 240,90 L240,160 L40,160 Z" fill="#475569" fill-opacity="0.4"/>
            <text x="140" y="55" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Mountain (+2,500 m)</text>
            
            <line x1="40" y1="90" x2="410" y2="90" stroke="#38bdf8" stroke-width="2"/>
            <text x="390" y="85" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="end">Sea Level (0 m)</text>
            
            <rect x="240" y="90" width="170" height="70" fill="#0369a1" fill-opacity="0.3"/>
            <text x="325" y="135" fill="#93c5fd" font-size="11" text-anchor="middle">Submarine Trench (−1,200 m)</text>
        `;
    } else {
        title.textContent = "Celsius Temperature Scale";
        desc.innerHTML = "The melting point of ice / freezing point of water is <strong>0 °C</strong>. Boiling water reaches <strong>+100 °C</strong>, while Antarctic winters plunge below <strong>−60 °C</strong>.";
        svg.innerHTML = `
            <!-- Horizontal thermometer -->
            <rect x="60" y="70" width="330" height="20" rx="10" fill="#1e293b" stroke="#64748b"/>
            <!-- Mercury -->
            <rect x="60" y="72" width="165" height="16" rx="8" fill="#f43f5e"/>
            <circle cx="60" cy="80" r="16" fill="#f43f5e" stroke="#fff" stroke-width="1.5"/>
            <!-- 0 Degree Mark -->
            <line x1="225" y1="60" x2="225" y2="100" stroke="#f59e0b" stroke-width="2"/>
            <text x="225" y="50" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">0 °C (Freezing)</text>
            
            <text x="120" y="115" fill="#f87171" font-size="10" text-anchor="middle">−15 °C (Sub-Zero)</text>
            <text x="330" y="115" fill="#34d399" font-size="10" text-anchor="middle">+25 °C (Warm)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 15: Magic Border Grids
// -------------------------------------------------------------
// 3x3 grid with empty center: [0,0], [0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2]
let sim15Values = [
    +2, -3, +1,
    -1,     +1,
    -1, +3, -2
];

function renderSim15() {
    const board = document.getElementById('sim15-grid-board');
    if (!board) return;

    // Cells:
    // [0] [1] [2]  (Top: 0, 1, 2)
    // [3]     [4]  (Left: 0, 3, 5; Right: 2, 4, 7)
    // [5] [6] [7]  (Bottom: 5, 6, 7)
    const topSum = sim15Values[0] + sim15Values[1] + sim15Values[2];
    const botSum = sim15Values[5] + sim15Values[6] + sim15Values[7];
    const leftSum = sim15Values[0] + sim15Values[3] + sim15Values[5];
    const rightSum = sim15Values[2] + sim15Values[4] + sim15Values[7];

    document.getElementById('sim15-top-sum').textContent = topSum;
    document.getElementById('sim15-bot-sum').textContent = botSum;
    document.getElementById('sim15-left-sum').textContent = leftSum;
    document.getElementById('sim15-right-sum').textContent = rightSum;

    let html = '';
    const indices = [0, 1, 2, 3, 'center', 4, 5, 6, 7];

    indices.forEach(idx => {
        if (idx === 'center') {
            html += `<div class="bg-slate-950/40 rounded-lg flex items-center justify-center text-[10px] text-slate-600 font-mono">Center</div>`;
        } else {
            const v = sim15Values[idx];
            html += `
                <div onclick="cycleSim15Cell(${idx})" 
                     class="rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 flex items-center justify-center font-bold text-sm cursor-pointer select-none transition ${v > 0 ? 'text-emerald-400' : (v < 0 ? 'text-rose-400' : 'text-amber-400')}">
                    ${v > 0 ? '+' + v : v}
                </div>
            `;
        }
    });

    board.innerHTML = html;

    const status = document.getElementById('sim15-status');
    if (topSum === botSum && topSum === leftSum && topSum === rightSum) {
        status.innerHTML = `<span class="text-emerald-400 font-bold">Perfect Balance!</span> All four border sums equal <strong>${topSum}</strong>. Symmetrical harmony achieved!`;
    } else {
        status.innerHTML = `<span class="text-slate-400">Click any border tile to cycle its integer value. Try to balance all 4 side sums to 0!</span>`;
    }
}

function cycleSim15Cell(idx) {
    // Cycle from -4 to +4
    sim15Values[idx] = sim15Values[idx] + 1;
    if (sim15Values[idx] > 4) sim15Values[idx] = -4;
    renderSim15();
}

// -------------------------------------------------------------
// Simulator 16: Brahmagupta's Laws Table
// -------------------------------------------------------------
const sim16Data = {
    ff: {
        title: "Fortune + Fortune = Fortune",
        sanskrit: "धनयोर्धनम् (Dhanayordhanam)",
        formula: "(+a) + (+b) = +(a + b)",
        example: "(+50) + (+30) = +80",
        explanation: "Combining two fortunes yields a greater fortune. Adding two positive numbers accumulates positive wealth."
    },
    dd: {
        title: "Debt + Debt = Debt",
        sanskrit: "ऋणयोर्ऋणम् (Ṛṇayorṛṇam)",
        formula: "(−a) + (−b) = −(a + b)",
        example: "(−40) + (−25) = −65",
        explanation: "Combining two debts increases the total obligation. Adding two negative numbers increases the total negative magnitude."
    },
    fd: {
        title: "Fortune + Debt = Difference",
        sanskrit: "धनर्णयोर्विशेषः (Dhanarṇayorviśeṣaḥ)",
        formula: "(+a) + (−b) = a − b",
        example: "(+100) + (−40) = +60 | (+30) + (−70) = −40",
        explanation: "When fortune and debt meet, they cancel each other out. The result retains the sign of whichever had the larger magnitude."
    },
    sub: {
        title: "Zero − Debt = Fortune",
        sanskrit: "खादृणं धनम् (Khādṛṇaṁ dhanam)",
        formula: "0 − (−a) = +a",
        example: "0 − (−500) = +500",
        explanation: "Subtracting a debt from nothing produces a fortune! Removing an obligation is legally and mathematically identical to receiving wealth."
    }
};

function showSim16Rule(key) {
    ['ff', 'dd', 'fd', 'sub'].forEach(k => {
        const btn = document.getElementById(`sim16-btn-${k}`);
        if (btn) {
            btn.className = (k === key) ?
                'p-3 rounded-xl border border-slate-700 bg-cyan-500 text-slate-950 font-bold text-left transition' :
                'p-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 font-semibold text-left transition';
        }
    });

    const rule = sim16Data[key];
    const box = document.getElementById('sim16-detail-box');
    box.innerHTML = `
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-400 uppercase">${rule.sanskrit}</span>
            <span class="text-xs font-mono font-bold text-cyan-300 bg-cyan-500/10 px-2 py-0.5 rounded">${rule.formula}</span>
        </div>
        <h4 class="text-sm font-bold text-white">${rule.title}</h4>
        <p class="text-xs text-slate-300 leading-relaxed">${rule.explanation}</p>
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono text-emerald-400">
            <strong>Example:</strong> ${rule.example}
        </div>
    `;
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    setSim1Stage('natural');
    renderSim2();
    updateSim3();
    updateSim4();
    updateSim5();
    updateSim6();
    updateSim7();
    updateSim8();
    renderSim9();
    renderSim10();
    renderSim11();
    renderSim12();
    renderSim13();
    renderSim14();
    renderSim15();
    showSim16Rule('ff');

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''

# Verify zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')
matches = raw_latex_pattern.findall(js_code)
if matches:
    print("WARNING: Found potential raw LaTeX in JS code:", set(matches))
else:
    print("VERIFIED PASS: Zero raw LaTeX in JS code!")

with open(".agents/class6_math_integers_js.py", "w", encoding="utf-8") as f:
    f.write('"""\nJavaScript Code for Class 6 Math Chapter 10 Integers Interactive Lab\n"""\n\n')
    f.write('JS_CODE = ' + repr(js_code) + '\n')

print("Successfully wrote .agents/class6_math_integers_js.py")

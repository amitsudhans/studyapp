"""NCERT Class 6 Mathematics Chapter 6: Perimeter and Area JavaScript Module."""

INTERACTIVE_JS = """
// State & Navigation
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis
let isMuted = false;
let currentUtterance = null;

function toggleAudio() {
    isMuted = !isMuted;
    const btn = document.getElementById('muteBtn');
    if (isMuted) {
        if (window.speechSynthesis) window.speechSynthesis.cancel();
        if (btn) btn.innerHTML = '🔇';
    } else {
        if (btn) btn.innerHTML = '🔊';
        speakSlide(currentSlide);
    }
}

function speakSlide(slideNum) {
    if (isMuted || !('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const slideElem = document.getElementById(`slide-${slideNum}`);
    if (!slideElem) return;
    const summaryElem = slideElem.querySelector('.slide-summary');
    if (!summaryElem) return;
    const text = summaryElem.innerText;
    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.rate = 1.0;
    currentUtterance.pitch = 1.0;
    window.speechSynthesis.speak(currentUtterance);
}

function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    
    // Hide current
    const curr = document.getElementById(`slide-${currentSlide}`);
    if (curr) curr.classList.add('hidden');
    
    currentSlide = n;
    
    // Show target
    const target = document.getElementById(`slide-${currentSlide}`);
    if (target) target.classList.remove('hidden');
    
    // Update counter & progress
    const counter = document.getElementById('slideCounter');
    if (counter) counter.innerText = `${currentSlide} / ${totalSlides}`;
    
    const progress = document.getElementById('progressBar');
    if (progress) progress.style.width = `${(currentSlide / totalSlides) * 100}%`;
    
    // Update nav buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);
    
    // Terminal Slide Constraint
    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) {
            lastNotice.style.display = 'block';
            lastNotice.innerText = 'You have reached the last slide of this chapter.';
        }
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }
    
    // Speak narration
    speakSlide(currentSlide);
    
    // Trigger slide-specific sim setups
    if (currentSlide === 1) setWalkShape('rect');
    else if (currentSlide === 2) updateRectFormula();
    else if (currentSlide === 3) updateRegPoly();
    else if (currentSlide === 4) resetTrack();
    else if (currentSlide === 5) loadDotShape('crown');
    else if (currentSlide === 6) setSplitConfig('square');
    else if (currentSlide === 7) setTessellationMode('squares');
    else if (currentSlide === 8) setCarpetPreset(5, 4, 3, 3);
    else if (currentSlide === 10) initLeafGrid();
    else if (currentSlide === 11) setVaryDimensions(4, 6);
    else if (currentSlide === 12) attachSquare('reset');
    else if (currentSlide === 14) initMaze();
    else if (currentSlide === 16) initCompositeGrid();
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
}

// In-Slide Checkpoints
function checkAnswer(cpId, selectedOption, correctIndex, explanation) {
    const cpContainer = document.getElementById(cpId);
    if (!cpContainer) return;
    
    const buttons = cpContainer.querySelectorAll('.option-btn');
    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIndex) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedOption) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        }
    });
    
    const feedbackBox = cpContainer.querySelector('.checkpoint-feedback');
    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOption === correctIndex) {
            feedbackBox.innerHTML = `
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-emerald-300 text-xs mt-2">
                    <strong class="font-bold">✓ Correct!</strong> ${explanation}
                </div>`;
        } else {
            feedbackBox.innerHTML = `
                <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 text-rose-300 text-xs mt-2">
                    <strong class="font-bold">✗ Not Quite.</strong> ${explanation}
                </div>`;
        }
    }
}

// Quiz Selection & Solution Modal
const quizState = {};

function selectQuizOption(qId, selectedIdx, correctIdx) {
    quizState[qId] = selectedIdx;
    const qCard = document.getElementById(`quiz-q-${qId}`);
    if (!qCard) return;
    
    const btns = qCard.querySelectorAll('.quiz-option-btn');
    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        }
    });
    
    const solBtn = qCard.querySelector('.view-solution-btn');
    if (solBtn) solBtn.classList.remove('hidden');
}

function openSolution(qId) {
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionTitle');
    const body = document.getElementById('solutionBody');
    if (!modal || !title || !body) return;
    
    const questionObj = QUIZ_QUESTIONS_MAP[qId];
    if (!questionObj) return;
    
    title.innerText = `Question ${qId} • Step-by-Step Solution`;
    const letters = ['A', 'B', 'C', 'D'];
    const correctLetter = letters[questionObj.correct];
    const correctText = questionObj.options[questionObj.correct];
    
    body.innerHTML = `
        <div class="space-y-3 text-slate-200 text-xs sm:text-sm">
            <div class="p-3 rounded-lg bg-slate-900 border border-slate-700">
                <span class="text-slate-400 font-bold block mb-1">Question Prompt:</span>
                <p class="font-medium text-slate-100">${questionObj.question}</p>
            </div>
            <div class="p-3 rounded-lg bg-emerald-950/50 border border-emerald-500/40 text-emerald-200">
                <span class="font-bold text-emerald-400 block mb-1">Correct Answer:</span>
                <p class="font-bold">${correctLetter}. ${correctText}</p>
            </div>
            <div class="p-3 rounded-lg bg-amber-950/30 border border-amber-500/30 text-amber-200">
                <span class="font-bold text-amber-300 block mb-1">Mastery Explanation:</span>
                <p class="leading-relaxed text-slate-300">${questionObj.explanation}</p>
            </div>
        </div>
    `;
    modal.style.display = 'flex';
}

function closeSolution() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// -------------------------------------------------------------
// Interactive Simulators Handlers
// -------------------------------------------------------------

// Sim 1: Boundary Walk Simulator
let currentWalkPoints = [[60, 160], [260, 160], [260, 60], [60, 60]];
let currentWalkLengths = [10, 6, 10, 6];

function setWalkShape(type) {
    const poly = document.getElementById('walkPolygon');
    const labels = document.getElementById('walkSideLabels');
    const badge = document.getElementById('walkPerimeterBadge');
    const ant = document.getElementById('walkAntDot');
    if (!poly || !labels) return;
    
    if (type === 'rect') {
        currentWalkPoints = [[60, 160], [260, 160], [260, 60], [60, 60]];
        currentWalkLengths = [10, 5, 10, 5];
        if (badge) badge.innerText = 'Perimeter: 10 + 5 + 10 + 5 = 30 cm';
    } else if (type === 'tri') {
        currentWalkPoints = [[60, 160], [260, 160], [160, 40]];
        currentWalkLengths = [12, 10, 10];
        if (badge) badge.innerText = 'Perimeter: 12 + 10 + 10 = 32 cm';
    } else if (type === 'pent') {
        currentWalkPoints = [[80, 160], [240, 160], [270, 90], [160, 40], [50, 90]];
        currentWalkLengths = [8, 6, 7, 7, 6];
        if (badge) badge.innerText = 'Perimeter: 8 + 6 + 7 + 7 + 6 = 34 cm';
    }
    
    const ptsStr = currentWalkPoints.map(p => `${p[0]},${p[1]}`).join(' ');
    poly.setAttribute('points', ptsStr);
    
    if (ant) {
        ant.setAttribute('cx', currentWalkPoints[0][0]);
        ant.setAttribute('cy', currentWalkPoints[0][1]);
    }
    
    let labelsHtml = '';
    for (let i = 0; i < currentWalkPoints.length; i++) {
        const p1 = currentWalkPoints[i];
        const p2 = currentWalkPoints[(i + 1) % currentWalkPoints.length];
        const midX = (p1[0] + p2[0]) / 2;
        const midY = (p1[1] + p2[1]) / 2;
        labelsHtml += `<text x="${midX}" y="${midY}" fill="#38bdf8" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">${currentWalkLengths[i]}cm</text>`;
    }
    labels.innerHTML = labelsHtml;
}

function startBoundaryWalk() {
    const ant = document.getElementById('walkAntDot');
    if (!ant) return;
    
    let step = 0;
    const totalSteps = currentWalkPoints.length;
    
    const interval = setInterval(() => {
        step++;
        const targetPt = currentWalkPoints[step % totalSteps];
        ant.setAttribute('cx', targetPt[0]);
        ant.setAttribute('cy', targetPt[1]);
        
        if (step === totalSteps) {
            clearInterval(interval);
        }
    }, 400);
}

// Sim 2: Dynamic Rectangle & Square Perimeter Calculator
function updateRectFormula() {
    const sLen = document.getElementById('sliderLength');
    const sBrd = document.getElementById('sliderBreadth');
    const lVal = document.getElementById('sliderLenVal');
    const bVal = document.getElementById('sliderBrdVal');
    const badge = document.getElementById('rectFormulaBadge');
    const res = document.getElementById('rectPResult');
    const group = document.getElementById('rectShapeGroup');
    const lock = document.getElementById('lockSquareCheck');
    
    let l = parseInt(sLen?.value || 8);
    let b = parseInt(sBrd?.value || 5);
    
    if (lock && lock.checked) {
        b = l;
        if (sBrd) sBrd.value = l;
    }
    
    if (lVal) lVal.innerText = `${l} cm`;
    if (bVal) bVal.innerText = `${b} cm`;
    
    const p = (lock && lock.checked) ? (4 * l) : (2 * (l + b));
    if (badge) {
        badge.innerText = (lock && lock.checked) ? `4 × ${l} = ${p} cm` : `2(${l} + ${b}) = ${p} cm`;
    }
    if (res) res.innerText = `Perimeter = ${p} cm`;
    
    if (!group) return;
    
    const pxW = l * 16;
    const pxH = b * 16;
    const x = (320 - pxW) / 2;
    const y = (180 - pxH) / 2;
    
    group.innerHTML = `
        <rect x="${x}" y="${y}" width="${pxW}" height="${pxH}" rx="6" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
        <text x="${x + pxW/2}" y="${y - 6}" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">${l} cm</text>
        <text x="${x + pxW + 8}" y="${y + pxH/2 + 4}" fill="#38bdf8" font-size="11" font-weight="bold" font-family="monospace">${b} cm</text>
    `;
}

function toggleSquareLock() {
    const lock = document.getElementById('lockSquareCheck');
    const sBrd = document.getElementById('sliderBreadth');
    if (lock && lock.checked && sBrd) {
        const sLen = document.getElementById('sliderLength');
        if (sLen) sBrd.value = sLen.value;
    }
    updateRectFormula();
}

// Sim 3: Regular Polygon Perimeter Lab
let currentRegSides = 6;

function setRegPolySides(n) {
    currentRegSides = n;
    updateRegPoly();
}

function updateRegPoly() {
    const slider = document.getElementById('regSideSlider');
    const valText = document.getElementById('regSideVal');
    const badge = document.getElementById('regPolyBadge');
    const poly = document.getElementById('regPolygonPath');
    if (!poly) return;
    
    const s = parseInt(slider?.value || 6);
    if (valText) valText.innerText = `${s} cm`;
    
    const n = currentRegSides;
    const p = n * s;
    const names = { 3: 'Triangle', 4: 'Square', 5: 'Pentagon', 6: 'Hexagon', 8: 'Octagon' };
    
    if (badge) badge.innerText = `${names[n]}: ${n} × ${s} = ${p} cm`;
    
    const cx = 120, cy = 90, r = 65;
    const pts = [];
    for (let i = 0; i < n; i++) {
        const angle = (i / n) * 2 * Math.PI - Math.PI / 2;
        pts.push(`${cx + r * Math.cos(angle)},${cy + r * Math.sin(angle)}`);
    }
    poly.setAttribute('points', pts.join(' '));
}

// Sim 4: Concentric Race Track Stagger Simulator
function applyFairStagger() {
    const runnerOuter = document.getElementById('runnerOuter');
    const badge = document.getElementById('staggerFeedbackBadge');
    if (runnerOuter) {
        runnerOuter.setAttribute('cx', '200'); // shift forward 40px
    }
    if (badge) {
        badge.innerText = '✓ Runner 2 staggered 8m ahead! Fair race!';
        badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
    }
}

function resetTrack() {
    const runnerOuter = document.getElementById('runnerOuter');
    const badge = document.getElementById('staggerFeedbackBadge');
    if (runnerOuter) {
        runnerOuter.setAttribute('cx', '160');
    }
    if (badge) {
        badge.innerText = 'Lane 2 is 8m longer (Side-by-side: Unfair!)';
        badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
    }
}

// Sim 5: Dot Grid Perimeter Explorer
function loadDotShape(type) {
    const dotsGroup = document.getElementById('dotGridDotsGroup');
    const linesGroup = document.getElementById('dotGridLinesGroup');
    const badge = document.getElementById('dotPerimeterBadge');
    if (!dotsGroup || !linesGroup) return;
    
    // Draw 6x6 dots
    let dotsHtml = '';
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 6; c++) {
            dotsHtml += `<circle cx="${30 + c * 35}" cy="${25 + r * 35}" r="2" fill="#64748b"/>`;
        }
    }
    dotsGroup.innerHTML = dotsHtml;
    
    let path = '';
    let perimText = '';
    if (type === 'arrow') {
        path = 'M 65,95 L 135,95 L 135,60 L 205,95 L 135,130 L 135,95';
        perimText = 'Perimeter: 6s + 2d';
    } else if (type === 'crown') {
        path = 'M 65,130 L 205,130 L 205,60 L 170,95 L 135,60 L 100,95 L 65,60 Z';
        perimText = 'Perimeter: 6s + 4d';
    } else if (type === 'diamond') {
        path = 'M 135,25 L 205,95 L 135,165 L 65,95 Z';
        perimText = 'Perimeter: 0s + 4d';
    }
    
    linesGroup.innerHTML = `<path d="${path}" fill="#0284c7" fill-opacity="0.25" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>`;
    if (badge) badge.innerText = perimText;
}

// Sim 6: Split & Rejoin Paradox Lab
function setSplitConfig(type) {
    const container = document.getElementById('splitShapeContainer');
    const aVal = document.getElementById('splitAreaVal');
    const pVal = document.getElementById('splitPerimeterVal');
    const badge = document.getElementById('splitParadoxBadge');
    if (!container) return;
    
    if (type === 'square') {
        container.innerHTML = `
            <div class="w-24 h-24 bg-cyan-600/60 border-2 border-cyan-400 rounded-lg flex items-center justify-center font-bold text-xs text-cyan-100 shadow-md">
                4 cm × 4 cm
            </div>
        `;
        if (pVal) pVal.innerText = '16 cm (2 × 8)';
        if (badge) badge.innerText = 'Area = 16 cm² • P = 16 cm';
    } else if (type === 'rect') {
        container.innerHTML = `
            <div class="w-44 h-12 bg-amber-600/60 border-2 border-amber-400 rounded-lg flex items-center justify-center font-bold text-xs text-amber-100 shadow-md">
                8 cm × 2 cm
            </div>
        `;
        if (pVal) pVal.innerText = '20 cm (2 × 10)';
        if (badge) badge.innerText = 'Area = 16 cm² • P = 20 cm (Increased!)';
    } else if (type === 'strip') {
        container.innerHTML = `
            <div class="w-64 h-6 bg-rose-600/60 border-2 border-rose-400 rounded-lg flex items-center justify-center font-bold text-[10px] text-rose-100 shadow-md">
                16 cm × 1 cm Strip
            </div>
        `;
        if (pVal) pVal.innerText = '34 cm (2 × 17)';
        if (badge) badge.innerText = 'Area = 16 cm² • P = 34 cm (Massive!)';
    }
    if (aVal) aVal.innerText = '16 cm² (Constant)';
}

// Sim 7: Why Squares Tile (Tessellation Comparison)
function setTessellationMode(mode) {
    const group = document.getElementById('tessellationGroup');
    const badge = document.getElementById('tileCompareBadge');
    if (!group) return;
    
    let html = '';
    if (mode === 'squares') {
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 5; c++) {
                html += `<rect x="${30 + c * 36}" y="${20 + r * 36}" width="36" height="36" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>`;
            }
        }
        if (badge) {
            badge.innerText = 'Square Tiles: Seamless Flat Tiling (Zero Gaps)';
            badge.className = 'font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40';
        }
    } else {
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 5; c++) {
                html += `<circle cx="${48 + c * 36}" cy="${38 + r * 36}" r="17" fill="#e11d48" fill-opacity="0.3" stroke="#f43f5e" stroke-width="1.5"/>`;
            }
        }
        if (badge) {
            badge.innerText = 'Circular Tiles: Unfilled Diamond Voids (Gaps!)';
            badge.className = 'font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40';
        }
    }
    group.innerHTML = html;
}

// Sim 8: Room & Carpet Area Subtraction
function setCarpetPreset(fl, fb, cl, cb) {
    const badge = document.getElementById('carpetResultBadge');
    const patch = document.getElementById('carpetPatch');
    if (!patch) return;
    
    const floorArea = fl * fb;
    const carpetArea = cl * cb;
    const diff = floorArea - carpetArea;
    
    if (badge) badge.innerText = `Floor: ${floorArea}m² − Carpet: ${carpetArea}m² = Uncarpeted: ${diff}m²`;
}

// Sim 9: Tangram Dissection & Relative Units
function selectTangramPiece(name, area) {
    const info = document.getElementById('tangramPieceInfo');
    if (info) info.innerHTML = `<strong class="text-amber-400">${name}</strong>: Area = <strong>${area} units</strong> (${Math.round((area/16)*100)}% of total square)`;
}

function resetTangramInspect() {
    const info = document.getElementById('tangramPieceInfo');
    if (info) info.innerText = 'Click any piece to inspect relative area';
}

// Sim 10: Grid Area Estimator (4-Step Protocol)
function initLeafGrid() {
    const bg = document.getElementById('leafGridBack');
    if (!bg) return;
    
    let html = '';
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 10; c++) {
            html += `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="none" stroke="#334155" stroke-width="1"/>`;
        }
    }
    bg.innerHTML = html;
}

// Sim 11: Same Area, Varied Perimeters Lab
function setVaryDimensions(l, b) {
    const badge = document.getElementById('varyPBadge');
    const group = document.getElementById('varyRectGroup');
    if (!group) return;
    
    const p = 2 * (l + b);
    if (badge) badge.innerText = `${l} × ${b}: Perimeter = ${p} cm`;
    
    const pxW = l * 12;
    const pxH = b * 12;
    const x = (320 - pxW) / 2;
    const y = (180 - pxH) / 2;
    
    group.innerHTML = `
        <rect x="${x}" y="${y}" width="${pxW}" height="${pxH}" rx="6" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
        <text x="${x + pxW/2}" y="${y - 6}" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">${l} cm</text>
        <text x="${x + pxW + 6}" y="${y + pxH/2 + 4}" fill="#38bdf8" font-size="11" font-weight="bold">${b} cm</text>
    `;
}

// Sim 12: Making It More or Less (Unit Square Surgery)
function attachSquare(mode) {
    const badge = document.getElementById('surgeryBadge');
    const addedGroup = document.getElementById('surgeryAddedGroup');
    const baseGroup = document.getElementById('surgeryBaseGroup');
    if (!addedGroup || !baseGroup) return;
    
    // Draw 3x3 L-shape base
    baseGroup.innerHTML = `
        <rect x="70" y="50" width="60" height="60" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
        <rect x="130" y="80" width="30" height="30" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
    `;
    
    if (mode === 'edge') {
        addedGroup.innerHTML = `<rect x="70" y="20" width="30" height="30" fill="#10b981" fill-opacity="0.8" stroke="#34d399" stroke-width="2"/>`;
        if (badge) badge.innerText = 'Flat Edge Attachment: +3 new, −1 shared = +2 Net Perimeter!';
    } else if (mode === 'corner') {
        addedGroup.innerHTML = `<rect x="130" y="50" width="30" height="30" fill="#f59e0b" fill-opacity="0.8" stroke="#fbbf24" stroke-width="2"/>`;
        if (badge) badge.innerText = 'L-Corner Slot: +2 new, −2 shared = 0 Change (Perimeter Unaltered!)';
    } else if (mode === 'pocket') {
        addedGroup.innerHTML = `<rect x="130" y="50" width="30" height="30" fill="#ef4444" fill-opacity="0.8" stroke="#f87171" stroke-width="2"/>`;
        if (badge) badge.innerText = 'Gap Pocket Fill: +1 new, −3 shared = −2 Perimeter Decreases!';
    } else {
        addedGroup.innerHTML = '';
        if (badge) badge.innerText = 'Base Shape: Perimeter = 14 units';
    }
}

// Sim 13: Architectural Floor Plan Navigator
function inspectRoom(name, l, b, a) {
    const info = document.getElementById('roomInspectInfo');
    if (info) info.innerHTML = `<strong class="text-amber-400">${name}</strong>: ${l} m × ${b} m = <strong>${a} m²</strong>`;
}

// Sim 14: Area Maze Logic Puzzle (Menseki Meiro)
let mazeStep = 0;
function initMaze() {
    mazeStep = 0;
    const txt = document.getElementById('mazeDeductionText');
    const qm = document.getElementById('mazeQuestionMark');
    if (txt) txt.innerText = 'Click Deduce to solve';
    if (qm) qm.innerText = '? cm';
}

function revealMazeStep() {
    mazeStep = (mazeStep + 1) % 3;
    const txt = document.getElementById('mazeDeductionText');
    const qm = document.getElementById('mazeQuestionMark');
    
    if (mazeStep === 1) {
        if (txt) txt.innerText = 'Step 1: Height = 18 ÷ 3 = 6 cm';
    } else if (mazeStep === 2) {
        if (txt) txt.innerText = 'Step 2: Width = 24 ÷ 6 = 4 cm!';
        if (qm) qm.innerText = '4 cm ✓';
    } else {
        initMaze();
    }
}

// Sim 15: Triangle Diagonal Split Lab
let triFlipped = false;
function toggleTriangleHighlight() {
    const poly = document.getElementById('triHighlightPoly');
    if (!poly) return;
    triFlipped = !triFlipped;
    poly.setAttribute('points', triFlipped ? '40,30 240,30 40,150' : '40,150 240,150 240,30');
}

// Sim 16: Composite Grid Shape Decomposer
let compDecomposed = false;
function initCompositeGrid() {
    const bg = document.getElementById('compositeGridBg');
    if (!bg) return;
    let html = '';
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 14; c++) {
            html += `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="none" stroke="#1e293b" stroke-width="1"/>`;
        }
    }
    bg.innerHTML = html;
}

function toggleCompositeDecompose() {
    compDecomposed = !compDecomposed;
    const shaft = document.getElementById('compShaft');
    const head = document.getElementById('compHead');
    const badge = document.getElementById('compositeTotalBadge');
    
    if (compDecomposed) {
        if (shaft) shaft.setAttribute('x', '40');
        if (head) head.setAttribute('points', '190,40 250,90 190,140');
        if (badge) badge.innerText = 'Decomposed: 12 (Shaft) + 9 (Head) = 21';
    } else {
        if (shaft) shaft.setAttribute('x', '50');
        if (head) head.setAttribute('points', '170,40 230,90 170,140');
        if (badge) badge.innerText = 'Merged Arrow: Total Area = 21 sq units';
    }
}

// Keyboard navigation & modal close
window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') nextSlide();
    else if (e.key === 'ArrowLeft') prevSlide();
    else if (e.key === 'Escape') closeSolution();
});

// Click outside modal to close
window.addEventListener('click', (e) => {
    const modal = document.getElementById('solutionModal');
    if (modal && e.target === modal) {
        closeSolution();
    }
});
"""

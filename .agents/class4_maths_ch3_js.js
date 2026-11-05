
// State Management
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;

// Speech Engine - Indian English Male Teacher Priority
function selectIndianMaleVoice() {
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const indianMalePriority = [
        'Microsoft Prabhat Online (Natural) - Hindi (India)',
        'Microsoft Prabhat',
        'Rishi',
        'Microsoft Ravi Online (Natural) - Hindi (India)',
        'Microsoft Ravi',
        'Pradeep',
        'Madhav',
        'Karan',
        'Mohan'
    ];

    const femaleKeywords = [
        'female', 'woman', 'girl', 'zira', 'jenny', 'aria',
        'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera',
        'aditi', 'kavya', 'ananya', 'shreya', 'sunita'
    ];

    function isFemale(name) {
        const lower = name.toLowerCase();
        return femaleKeywords.some(kw => lower.includes(kw));
    }

    // 1. Try exact Indian English male match
    for (const name of indianMalePriority) {
        const found = voices.find(v => v.name.includes(name) && !isFemale(v.name));
        if (found) return found;
    }

    // 2. Try any Indian voice that is not female
    const anyIndianMale = voices.find(v => (v.lang === 'en-IN' || v.lang === 'hi-IN') && !isFemale(v.name));
    if (anyIndianMale) return anyIndianMale;

    // 3. Fallback male voices
    const fallbackMales = [
        'Google UK English Male',
        'Microsoft David - English (United States)',
        'Microsoft David',
        'Microsoft Mark - English (United States)',
        'Microsoft Mark',
        'Alex'
    ];

    for (const name of fallbackMales) {
        const found = voices.find(v => v.name.includes(name) && !isFemale(v.name));
        if (found) return found;
    }

    // 4. Any English non-female
    const anyEnglishMale = voices.find(v => v.lang.startsWith('en') && !isFemale(v.name));
    return anyEnglishMale || voices[0];
}

function stopAudioLecture() {
    if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
    }
    if (keepAliveTimer) {
        clearInterval(keepAliveTimer);
        keepAliveTimer = null;
    }
    isSpeaking = false;
    updateAudioBtnUI();
}

function updateAudioBtnUI() {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (isSpeaking) {
        btn.innerHTML = `<svg class="w-4 h-4 animate-spin text-amber-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg><span class="text-xs font-bold text-amber-300">Stop Teacher Lecture</span>`;
        btn.classList.add('ring-2', 'ring-amber-400');
    } else {
        btn.innerHTML = `<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg><span class="text-xs font-bold text-emerald-300">Listen Teacher Lecture</span>`;
        btn.classList.remove('ring-2', 'ring-amber-400');
    }
}

function playAudioLecture() {
    if (!('speechSynthesis' in window)) {
        alert("Speech synthesis is not supported in this browser.");
        return;
    }

    if (isSpeaking) {
        stopAudioLecture();
        return;
    }

    stopAudioLecture();

    const slideData = SLIDES.find(s => s.id === currentSlide);
    if (!slideData || !slideData.speech) return;

    currentUtterance = new SpeechSynthesisUtterance(slideData.speech);
    currentUtterance.voice = selectIndianMaleVoice();
    currentUtterance.rate = 0.94;
    currentUtterance.pitch = 0.85;

    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioBtnUI();
        keepAliveTimer = setInterval(() => {
            if (window.speechSynthesis.speaking) {
                window.speechSynthesis.pause();
                window.speechSynthesis.resume();
            }
        }, 10000);
    };

    currentUtterance.onend = () => {
        stopAudioLecture();
    };

    currentUtterance.onerror = () => {
        stopAudioLecture();
    };

    window.speechSynthesis.speak(currentUtterance);
}

// Navigation Engine
function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;
    stopAudioLecture();

    // Hide all slides
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));

    currentSlide = slideNum;
    const activeSlide = document.getElementById(`slide-${currentSlide}`);
    if (activeSlide) {
        activeSlide.classList.remove('hidden');
    }

    // Update Header / Nav
    const currentNumDisplay = document.getElementById('currentSlideNum');
    if (currentNumDisplay) currentNumDisplay.textContent = currentSlide;

    const progressBar = document.getElementById('chapterProgressBar');
    if (progressBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progressBar.style.width = `${pct}%`;
    }

    // Prev / Next button states
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastSlideNotice) {
            lastSlideNotice.style.display = 'block';
            lastSlideNotice.classList.remove('hidden');
        }
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.classList.remove('hidden');
            nextBtn.disabled = false;
        }
        if (lastSlideNotice) {
            lastSlideNotice.style.display = 'none';
            lastSlideNotice.classList.add('hidden');
        }
    }

    // Hide/Show Audio Lecture Button for Challenge Slides (17-20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }

    // Initialize Simulator for current slide
    initSlideSim(currentSlide);
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

// Checkpoint Interaction
function checkCheckpoint(slideId, qIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints) return;
    const cp = slide.checkpoints[qIdx];
    if (!cp) return;

    const fbEl = document.getElementById(`cp-fb-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${qIdx}`);

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === cp.ans) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-600', 'border-emerald-500', 'text-white');
        } else if (idx === optIdx && optIdx !== cp.ans) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-600', 'border-rose-500', 'text-white');
        }
    });

    if (fbEl) {
        fbEl.classList.remove('hidden');
        if (optIdx === cp.ans) {
            fbEl.innerHTML = `<div class="p-2 bg-emerald-950/60 border border-emerald-500/40 rounded text-emerald-300 text-xs"><strong>Correct!</strong> ${cp.exp}</div>`;
        } else {
            fbEl.innerHTML = `<div class="p-2 bg-rose-950/60 border border-rose-500/40 rounded text-rose-300 text-xs"><strong>Incorrect.</strong> ${cp.exp}</div>`;
        }
    }
}

// Quiz Interaction for Challenge Slides (17-20)
function selectQuizOption(qId, optIdx) {
    let targetQ = null;
    let slideObj = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const f = s.quiz.find(item => item.id === qId);
            if (f) {
                targetQ = f;
                slideObj = s;
                break;
            }
        }
    }
    if (!targetQ) return;

    const fbEl = document.getElementById(`quiz-fb-${qId}`);
    const btns = document.querySelectorAll(`.quiz-opt-btn-${qId}`);

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === targetQ.ans) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-600', 'border-emerald-500', 'text-white');
        } else if (idx === optIdx && optIdx !== targetQ.ans) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-600', 'border-rose-500', 'text-white');
        }
    });

    if (fbEl) {
        fbEl.classList.remove('hidden');
        const isCorrect = (optIdx === targetQ.ans);
        fbEl.innerHTML = `
            <div class="p-2.5 rounded-lg border text-xs ${isCorrect ? 'bg-emerald-950/60 border-emerald-500/40 text-emerald-200' : 'bg-rose-950/60 border-rose-500/40 text-rose-200'}">
                <div class="font-bold mb-1">${isCorrect ? '🎉 Correct Answer!' : '❌ Not Quite Right'}</div>
                <div>${targetQ.explanation}</div>
                <button onclick="openSolutionModal(${qId})" class="mt-2 inline-flex items-center gap-1 px-2.5 py-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded text-[11px] shadow">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    <span>View Step-by-Step Solution</span>
                </button>
            </div>
        `;
    }
}

function openSolutionModal(qId) {
    let targetQ = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const f = s.quiz.find(item => item.id === qId);
            if (f) {
                targetQ = f;
                break;
            }
        }
    }
    if (!targetQ) return;

    const modal = document.getElementById('solutionModal');
    const content = document.getElementById('solutionModalContent');
    const title = document.getElementById('solutionModalTitle');

    if (title) title.textContent = `Question ${qId} • Step-by-Step Solution`;
    if (content) {
        content.innerHTML = `
            <div class="mb-3 font-semibold text-slate-200 text-sm">${targetQ.q}</div>
            <div class="mb-3 text-xs text-slate-400 font-mono bg-slate-900 p-2 rounded border border-slate-800">Correct Option: <span class="text-emerald-400 font-bold">${targetQ.options[targetQ.ans]}</span></div>
            ${targetQ.sol}
        `;
    }
    if (modal) modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// Simulator State & Rendering Engine
// Sim 1: Orchard Grid
let orchardRows = 4;
let orchardCols = 6;
let isHarvested = false;

function changeOrchardGrid(dRow, dCol) {
    orchardRows = Math.max(2, Math.min(6, orchardRows + dRow));
    orchardCols = Math.max(3, Math.min(8, orchardCols + dCol));
    isHarvested = false;
    renderOrchardGrid();
}

function harvestCoconuts() {
    isHarvested = !isHarvested;
    renderOrchardGrid();
}

function renderOrchardGrid() {
    const wrap = document.getElementById('orchardGridSvgWrap');
    if (!wrap) return;

    const totalTrees = orchardRows * orchardCols;
    const totalHarvest = totalTrees * 5;

    document.getElementById('orchardDimDisplay').textContent = `${orchardRows} Rows × ${orchardCols} Columns`;
    document.getElementById('orchardTreeTotal').textContent = `${totalTrees} Trees`;
    document.getElementById('orchardHarvestTotal').textContent = `${totalHarvest} Coconuts`;

    const svgWidth = 420;
    const svgHeight = 220;
    const startX = 35;
    const startY = 30;
    const cellW = (svgWidth - startX - 20) / orchardCols;
    const cellH = (svgHeight - startY - 20) / orchardRows;

    let treeElements = '';
    for (let r = 0; r < orchardRows; r++) {
        for (let c = 0; c < orchardCols; c++) {
            const cx = startX + c * cellW + cellW / 2;
            const cy = startY + r * cellH + cellH / 2;
            const harvestBadge = isHarvested ? `<circle cx="${cx + 10}" cy="${cy - 10}" r="7" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/><text x="${cx + 10}" y="${cy - 7}" font-size="8" font-weight="bold" fill="#78350f" text-anchor="middle">5</text>` : '';
            treeElements += `
                <g class="transition-all duration-300">
                    <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy + 12}" stroke="#78350f" stroke-width="4" stroke-linecap="round"/>
                    <circle cx="${cx}" cy="${cy - 4}" r="12" fill="#15803d" stroke="#166534" stroke-width="1.5"/>
                    <path d="M ${cx - 10} ${cy - 4} Q ${cx} ${cy - 14} ${cx + 10} ${cy - 4}" stroke="#22c55e" stroke-width="2" fill="none"/>
                    <path d="M ${cx} ${cy - 14} Q ${cx + 12} ${cy - 6} ${cx + 6} ${cy + 6}" stroke="#22c55e" stroke-width="2" fill="none"/>
                    <path d="M ${cx} ${cy - 14} Q ${cx - 12} ${cy - 6} ${cx - 6} ${cy + 6}" stroke="#22c55e" stroke-width="2" fill="none"/>
                    <circle cx="${cx - 2}" cy="${cy - 2}" r="2" fill="#92400e"/>
                    <circle cx="${cx + 2}" cy="${cy - 2}" r="2" fill="#92400e"/>
                    ${harvestBadge}
                </g>
            `;
        }
    }

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[220px]">
            <rect width="${svgWidth}" height="${svgHeight}" fill="#064e3b" rx="8" opacity="0.4"/>
            <!-- Grid Row Guides -->
            ${Array.from({length: orchardRows}).map((_, r) => {
                const y = startY + r * cellH + cellH / 2;
                return `<text x="12" y="${y + 4}" font-size="10" font-weight="bold" fill="#34d399">R${r + 1}</text>`;
            }).join('')}
            <!-- Grid Col Guides -->
            ${Array.from({length: orchardCols}).map((_, c) => {
                const x = startX + c * cellW + cellW / 2;
                return `<text x="${x}" y="18" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">C${c + 1}</text>`;
            }).join('')}
            ${treeElements}
        </svg>
    `;
}

// Sim 2: Pottery Workshop
let potteryType = 'cups';
let potteryStacks = 5;
let cupsPerStack = 6;
let platesPerStack = 8;

function setPotteryType(t) {
    potteryType = t;
    const cBtn = document.getElementById('potteryCupsBtn');
    const pBtn = document.getElementById('potteryPlatesBtn');
    if (t === 'cups') {
        cBtn.className = 'px-2.5 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';
        pBtn.className = 'px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all';
    } else {
        pBtn.className = 'px-2.5 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';
        cBtn.className = 'px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all';
    }
    renderPotteryStacks();
}

function changePotteryStacks(d) {
    potteryStacks = Math.max(3, Math.min(6, potteryStacks + d));
    renderPotteryStacks();
}

function renderPotteryStacks() {
    const wrap = document.getElementById('potterySvgWrap');
    if (!wrap) return;

    const perStack = (potteryType === 'cups') ? cupsPerStack : platesPerStack;
    const total = potteryStacks * perStack;
    const label = (potteryType === 'cups') ? 'Cups' : 'Plates';

    document.getElementById('potteryStacksDisplay').textContent = `${potteryStacks} Stacks`;
    document.getElementById('potteryPerStackDisplay').textContent = `${perStack} ${label} Each`;
    document.getElementById('potteryTotalDisplay').textContent = `${potteryStacks} × ${perStack} = ${total} ${label}`;

    const svgWidth = 420;
    const svgHeight = 220;
    const colW = svgWidth / (potteryStacks + 1);

    let stackItemsSvg = '';
    for (let s = 0; s < potteryStacks; s++) {
        const colX = (s + 1) * colW;
        const baseY = 190;
        const itemStep = (potteryType === 'cups') ? 18 : 14;

        for (let i = 0; i < perStack; i++) {
            const itemY = baseY - (i * itemStep);
            if (potteryType === 'cups') {
                stackItemsSvg += `
                    <g transform="translate(${colX - 16}, ${itemY - 14})">
                        <path d="M 4 2 L 28 2 L 24 16 L 8 16 Z" fill="#c25e38" stroke="#7c2d12" stroke-width="1.5"/>
                        <ellipse cx="16" cy="2" rx="12" ry="3" fill="#ea580c"/>
                        <path d="M 26 4 C 32 4, 32 12, 24 14" fill="none" stroke="#7c2d12" stroke-width="1.5"/>
                    </g>
                `;
            } else {
                stackItemsSvg += `
                    <g transform="translate(${colX - 22}, ${itemY - 8})">
                        <ellipse cx="22" cy="6" rx="20" ry="5" fill="#f97316" stroke="#9a3412" stroke-width="1.5"/>
                        <ellipse cx="22" cy="5" rx="14" ry="3" fill="#fdba74"/>
                    </g>
                `;
            }
        }
        stackItemsSvg += `<text x="${colX}" y="208" font-size="10" font-weight="bold" fill="#fdba74" text-anchor="middle">Stack ${s + 1}</text>`;
    }

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[220px]">
            <!-- Wooden Potter Workbench -->
            <rect x="10" y="195" width="${svgWidth - 20}" height="14" fill="#78350f" rx="3" stroke="#451a03" stroke-width="2"/>
            <line x1="20" y1="209" x2="20" y2="220" stroke="#451a03" stroke-width="4"/>
            <line x1="${svgWidth - 20}" y1="209" x2="${svgWidth - 20}" y2="220" stroke="#451a03" stroke-width="4"/>
            ${stackItemsSvg}
        </svg>
    `;
}

// Sim 3: Sweet Trays
let sweetTiers = 1;

function changeSweetTiers(t) {
    sweetTiers = t;
    renderSweetTrays();
}

function renderSweetTrays() {
    const wrap = document.getElementById('sweetTraysSvgWrap');
    if (!wrap) return;

    const totalLaddoos = sweetTiers * 9;
    const totalPedas = sweetTiers * 16;
    const totalSweets = totalLaddoos + totalPedas;

    document.getElementById('sweetLaddoosDisplay').textContent = `9 per tray (Total: ${totalLaddoos})`;
    document.getElementById('sweetPedasDisplay').textContent = `16 per tray (Total: ${totalPedas})`;
    document.getElementById('sweetTotalDisplay').textContent = `${totalSweets} Sweets (${sweetTiers} ${sweetTiers === 1 ? 'Tray' : 'Trays'})`;

    const svgWidth = 420;
    const svgHeight = 220;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[220px]">
            <!-- Tray Border -->
            <rect x="110" y="10" width="200" height="200" rx="10" fill="#451a03" stroke="#d97706" stroke-width="4"/>
            <rect x="116" y="16" width="188" height="188" rx="6" fill="#78350f" opacity="0.6"/>

            <!-- Symmetrical Cross Layout of Laddoos -->
            <!-- Center Horiz Row of 5 Laddoos (y = 110) -->
            ${[-40, -20, 0, 20, 40].map(dx => `
                <circle cx="${210 + dx}" cy="110" r="8" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="${210 + dx - 2}" cy="108" r="1.5" fill="#eab308"/>
            `).join('')}
            <!-- Vertical Arms of Cross (2 top, 2 bottom) -->
            ${[-40, -20, 20, 40].map(dy => `
                <circle cx="210" cy="${110 + dy}" r="8" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <circle cx="208" cy="${110 + dy - 2}" r="1.5" fill="#eab308"/>
            `).join('')}

            <!-- 4 Corner Clusters of 4 Pedas each -->
            <!-- Top-Left Quadrant -->
            <circle cx="150" cy="50" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="150" cy="50" r="1.5" fill="#15803d"/>
            <circle cx="170" cy="50" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="170" cy="50" r="1.5" fill="#15803d"/>
            <circle cx="150" cy="70" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="150" cy="70" r="1.5" fill="#15803d"/>
            <circle cx="170" cy="70" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="170" cy="70" r="1.5" fill="#15803d"/>

            <!-- Top-Right Quadrant -->
            <circle cx="250" cy="50" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="250" cy="50" r="1.5" fill="#15803d"/>
            <circle cx="270" cy="50" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="270" cy="50" r="1.5" fill="#15803d"/>
            <circle cx="250" cy="70" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="250" cy="70" r="1.5" fill="#15803d"/>
            <circle cx="270" cy="70" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="270" cy="70" r="1.5" fill="#15803d"/>

            <!-- Bottom-Left Quadrant -->
            <circle cx="150" cy="150" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="150" cy="150" r="1.5" fill="#15803d"/>
            <circle cx="170" cy="150" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="170" cy="150" r="1.5" fill="#15803d"/>
            <circle cx="150" cy="170" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="150" cy="170" r="1.5" fill="#15803d"/>
            <circle cx="170" cy="170" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="170" cy="170" r="1.5" fill="#15803d"/>

            <!-- Bottom-Right Quadrant -->
            <circle cx="250" cy="150" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="250" cy="150" r="1.5" fill="#15803d"/>
            <circle cx="270" cy="150" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="270" cy="150" r="1.5" fill="#15803d"/>
            <circle cx="250" cy="170" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="250" cy="170" r="1.5" fill="#15803d"/>
            <circle cx="270" cy="170" r="7" fill="#fed7aa" stroke="#c2410c" stroke-width="1.5"/><circle cx="270" cy="170" r="1.5" fill="#15803d"/>

            <!-- Multi-Tier Indicator Badge -->
            <g transform="translate(320, 20)">
                <rect width="90" height="40" rx="6" fill="#1e293b" stroke="#475569"/>
                <text x="45" y="18" font-size="10" fill="#94a3b8" text-anchor="middle">Active Tiers</text>
                <text x="45" y="34" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">× ${sweetTiers}</text>
            </g>
        </svg>
    `;
}

// Sim 4: Money Mandala
let activeRings = { notes: true, five: true, two: true, one: true };

function toggleMoneyRing(ring) {
    activeRings[ring] = !activeRings[ring];
    renderMoneyMandala();
}

function renderMoneyMandala() {
    const wrap = document.getElementById('moneyMandalaSvgWrap');
    if (!wrap) return;

    const valNotes = activeRings.notes ? 40 : 0;
    const valFive = activeRings.five ? 20 : 0;
    const valTwo = activeRings.two ? 16 : 0;
    const valOne = activeRings.one ? 8 : 0;
    const grandTotal = valNotes + valFive + valTwo + valOne;

    document.getElementById('mandalaNotesVal').textContent = `₹${valNotes}`;
    document.getElementById('mandalaFiveVal').textContent = `₹${valFive}`;
    document.getElementById('mandalaTwoVal').textContent = `₹${valTwo}`;
    document.getElementById('mandalaOneVal').textContent = `₹${valOne}`;
    document.getElementById('mandalaGrandTotal').textContent = `₹${valNotes} + ₹${valFive} + ₹${valTwo} + ₹${valOne} = ₹${grandTotal}`;

    const svgWidth = 420;
    const svgHeight = 220;
    const cx = svgWidth / 2;
    const cy = svgHeight / 2;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[220px]">
            <!-- Outer Ring ₹1 Coins (radius = 90) -->
            ${activeRings.one ? Array.from({length: 8}).map((_, i) => {
                const angle = (i * 45) * Math.PI / 180;
                const x = cx + 90 * Math.cos(angle);
                const y = cy + 90 * Math.sin(angle);
                return `
                    <g transform="translate(${x}, ${y})">
                        <circle cx="0" cy="0" r="11" fill="#10b981" stroke="#065f46" stroke-width="1.5"/>
                        <text x="0" y="4" font-size="10" font-weight="bold" fill="#064e3b" text-anchor="middle">₹1</text>
                    </g>
                `;
            }).join('') : ''}

            <!-- Middle Ring ₹2 Coins (radius = 65, offset angle = 22.5 deg) -->
            ${activeRings.two ? Array.from({length: 8}).map((_, i) => {
                const angle = (i * 45 + 22.5) * Math.PI / 180;
                const x = cx + 65 * Math.cos(angle);
                const y = cy + 65 * Math.sin(angle);
                return `
                    <g transform="translate(${x}, ${y})">
                        <circle cx="0" cy="0" r="13" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
                        <text x="0" y="4" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">₹2</text>
                    </g>
                `;
            }).join('') : ''}

            <!-- Inner Cardinal ₹5 Coins (radius = 40, angles = 0, 90, 180, 270) -->
            ${activeRings.five ? [0, 90, 180, 270].map(deg => {
                const angle = deg * Math.PI / 180;
                const x = cx + 42 * Math.cos(angle);
                const y = cy + 42 * Math.sin(angle);
                return `
                    <g transform="translate(${x}, ${y})">
                        <circle cx="0" cy="0" r="15" fill="#eab308" stroke="#854d0e" stroke-width="2"/>
                        <text x="0" y="4" font-size="12" font-weight="bold" fill="#713f12" text-anchor="middle">₹5</text>
                    </g>
                `;
            }).join('') : ''}

            <!-- Central Stack ₹10 Notes -->
            ${activeRings.notes ? `
                <g transform="translate(${cx - 24}, ${cy - 16})">
                    <rect x="4" y="-4" width="40" height="24" rx="3" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                    <rect x="2" y="-2" width="40" height="24" rx="3" fill="#d97706" stroke="#92400e" stroke-width="1"/>
                    <rect x="0" y="0" width="40" height="24" rx="3" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
                    <text x="20" y="15" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">₹10 (×4)</text>
                </g>
            ` : ''}
        </svg>
    `;
}

// Sim 5: Target Amount Builder
let currentTargetAmount = 36;
let walletItems = [];

function setTargetAmount(amt) {
    currentTargetAmount = amt;
    clearTargetWallet();
}

function addWalletItem(val) {
    walletItems.push(val);
    renderWallet();
}

function clearTargetWallet() {
    walletItems = [];
    renderWallet();
}

function renderWallet() {
    const sum = walletItems.reduce((acc, curr) => acc + curr, 0);
    const container = document.getElementById('walletItemsContainer');
    const targetDisp = document.getElementById('targetAmountDisplay');
    const sumDisp = document.getElementById('walletSumDisplay');
    const statusDisp = document.getElementById('walletStatusDisplay');

    if (targetDisp) targetDisp.textContent = `₹${currentTargetAmount}`;
    if (sumDisp) sumDisp.textContent = `₹${sum}`;

    if (statusDisp) {
        if (sum === currentTargetAmount) {
            statusDisp.className = 'font-bold text-emerald-400 text-xs';
            statusDisp.textContent = 'Exact Amount Reached! 🎯';
        } else if (sum < currentTargetAmount) {
            statusDisp.className = 'font-bold text-amber-400 text-xs';
            statusDisp.textContent = `Needs ₹${currentTargetAmount - sum} more`;
        } else {
            statusDisp.className = 'font-bold text-rose-400 text-xs';
            statusDisp.textContent = `Exceeded by ₹${sum - currentTargetAmount}`;
        }
    }

    if (container) {
        if (walletItems.length === 0) {
            container.innerHTML = `<span class="text-xs text-slate-500 italic">Click denomination buttons above to build the target amount.</span>`;
        } else {
            container.innerHTML = walletItems.map((val, idx) => {
                let colorCls = 'bg-slate-700 text-slate-200';
                if (val >= 100) colorCls = 'bg-purple-800 text-purple-200 border-purple-500';
                else if (val >= 50) colorCls = 'bg-cyan-800 text-cyan-200 border-cyan-500';
                else if (val >= 20) colorCls = 'bg-amber-800 text-amber-200 border-amber-500';
                else if (val >= 10) colorCls = 'bg-orange-800 text-orange-200 border-orange-500';
                else if (val >= 5) colorCls = 'bg-yellow-800 text-yellow-200 border-yellow-500';
                else if (val === 1) colorCls = 'bg-emerald-800 text-emerald-200 border-emerald-500';

                return `<span class="px-2 py-1 rounded text-xs font-bold border shadow ${colorCls} animate-fade-in">₹${val}</span>`;
            }).join('');
        }
    }
}

// Sim 6: Quantity Distributions
let distMode = '2x6';

function setDistributionMode(mode) {
    distMode = mode;
    const b1 = document.getElementById('dist2x6Btn');
    const b2 = document.getElementById('dist3x4Btn');
    const b3 = document.getElementById('distPairsBtn');

    [b1, b2, b3].forEach(b => b.className = 'px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700');
    if (mode === '2x6') b1.className = 'px-2 py-1 bg-blue-500 text-slate-950 font-bold text-xs rounded transition-all';
    if (mode === '3x4') b2.className = 'px-2 py-1 bg-blue-500 text-slate-950 font-bold text-xs rounded transition-all';
    if (mode === 'pairs') b3.className = 'px-2 py-1 bg-blue-500 text-slate-950 font-bold text-xs rounded transition-all';

    renderDistribution();
}

function renderDistribution() {
    const wrap = document.getElementById('distributionSvgWrap');
    const exp = document.getElementById('distributionExplanation');
    if (!wrap) return;

    const svgWidth = 420;
    const svgHeight = 200;
    let coinsSvg = '';

    if (distMode === '2x6') {
        exp.textContent = '12 Coins arranged into 2 rows of 6 coins. Each coin in the top row has a matching partner below (Splits into 2 equal halves of 6).';
        for (let r = 0; r < 2; r++) {
            for (let c = 0; c < 6; c++) {
                const cx = 80 + c * 52;
                const cy = 60 + r * 70;
                coinsSvg += `
                    <g transform="translate(${cx}, ${cy})">
                        <circle cx="0" cy="0" r="18" fill="#eab308" stroke="#854d0e" stroke-width="2"/>
                        <circle cx="0" cy="0" r="14" fill="#facc15"/>
                        <text x="0" y="5" font-size="12" font-weight="bold" fill="#713f12" text-anchor="middle">₹</text>
                    </g>
                `;
            }
        }
    } else if (distMode === '3x4') {
        exp.textContent = '12 Coins arranged into 3 rows of 4 columns. Visualizes that 12 is a multiple of 3 and 4.';
        for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 4; c++) {
                const cx = 110 + c * 65;
                const cy = 40 + r * 55;
                coinsSvg += `
                    <g transform="translate(${cx}, ${cy})">
                        <circle cx="0" cy="0" r="18" fill="#eab308" stroke="#854d0e" stroke-width="2"/>
                        <circle cx="0" cy="0" r="14" fill="#facc15"/>
                        <text x="0" y="5" font-size="12" font-weight="bold" fill="#713f12" text-anchor="middle">₹</text>
                    </g>
                `;
            }
        }
    } else {
        exp.textContent = '12 Coins arranged into 6 distinct coupled pairs of 2. Proves that 12 leaves 0 unpaired items (Even Number!).';
        for (let p = 0; p < 6; p++) {
            const px = 60 + (p % 3) * 150;
            const py = 60 + Math.floor(p / 3) * 80;
            coinsSvg += `
                <rect x="${px - 32}" y="${py - 24}" width="64" height="48" rx="8" fill="#1e3a8a" opacity="0.4" stroke="#3b82f6" stroke-dasharray="3 3"/>
                <g transform="translate(${px - 14}, ${py})">
                    <circle cx="0" cy="0" r="13" fill="#eab308" stroke="#854d0e" stroke-width="2"/>
                    <text x="0" y="4" font-size="10" font-weight="bold" fill="#713f12" text-anchor="middle">₹</text>
                </g>
                <g transform="translate(${px + 14}, ${py})">
                    <circle cx="0" cy="0" r="13" fill="#eab308" stroke="#854d0e" stroke-width="2"/>
                    <text x="0" y="4" font-size="10" font-weight="bold" fill="#713f12" text-anchor="middle">₹</text>
                </g>
            `;
        }
    }

    wrap.innerHTML = `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">${coinsSvg}</svg>`;
}

// Sim 7: Concept of Pairs
let pairItemCount = 10;
let isPairGrouped = false;

function changePairCount(d) {
    pairItemCount = Math.max(1, Math.min(20, pairItemCount + d));
    isPairGrouped = false;
    renderPairingLab();
}

function animatePairingAction() {
    isPairGrouped = true;
    renderPairingLab();
}

function renderPairingLab() {
    const wrap = document.getElementById('pairingLabSvgWrap');
    if (!wrap) return;

    const pairs = Math.floor(pairItemCount / 2);
    const leftover = pairItemCount % 2;
    const isEven = (leftover === 0);

    document.getElementById('pairItemCountDisplay').textContent = `${pairItemCount} Items`;
    document.getElementById('pairsCountDisplay').textContent = `${pairs} Pairs (${pairs * 2} Items)`;
    document.getElementById('leftoverCountDisplay').textContent = `${leftover} Leftover`;
    document.getElementById('parityFamilyDisplay').textContent = isEven ? 'EVEN NUMBER' : 'ODD NUMBER';
    document.getElementById('parityFamilyDisplay').className = `font-bold text-sm ${isEven ? 'text-emerald-400' : 'text-rose-400'}`;

    const svgWidth = 420;
    const svgHeight = 200;
    let itemsSvg = '';

    if (!isPairGrouped) {
        // Scatter / row display
        for (let i = 0; i < pairItemCount; i++) {
            const x = 30 + (i % 10) * 40;
            const y = 60 + Math.floor(i / 10) * 70;
            itemsSvg += `
                <g transform="translate(${x}, ${y})">
                    <circle cx="0" cy="0" r="14" fill="#14b8a6" stroke="#0f766e" stroke-width="2"/>
                    <circle cx="0" cy="0" r="4" fill="#ccfbf1"/>
                </g>
            `;
        }
    } else {
        // Grouped into pairs
        for (let p = 0; p < pairs; p++) {
            const px = 50 + (p % 5) * 80;
            const py = 50 + Math.floor(p / 5) * 80;
            itemsSvg += `
                <rect x="${px - 26}" y="${py - 18}" width="52" height="36" rx="18" fill="#134e4a" stroke="#2dd4bf" stroke-width="1.5"/>
                <circle cx="${px - 12}" cy="${py}" r="11" fill="#14b8a6" stroke="#0f766e" stroke-width="1.5"/>
                <circle cx="${px + 12}" cy="${py}" r="11" fill="#14b8a6" stroke="#0f766e" stroke-width="1.5"/>
            `;
        }
        if (leftover > 0) {
            const lx = 50 + (pairs % 5) * 80;
            const ly = 50 + Math.floor(pairs / 5) * 80;
            itemsSvg += `
                <rect x="${lx - 20}" y="${ly - 20}" width="40" height="40" rx="20" fill="#881337" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 2"/>
                <circle cx="${lx}" cy="${ly}" r="12" fill="#f43f5e" stroke="#9f1239" stroke-width="2"/>
                <text x="${lx}" y="${ly + 32}" font-size="9" font-weight="bold" fill="#fda4af" text-anchor="middle">Leftover: 1</text>
            `;
        }
    }

    wrap.innerHTML = `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">${itemsSvg}</svg>`;
}

// Sim 8: Even Number Pairing
let currentEvenNum = 8;
let isEvenSplit = false;

function setEvenNumber(n) {
    currentEvenNum = n;
    isEvenSplit = false;
    renderEvenPairing();
}

function toggleEvenSplit() {
    isEvenSplit = !isEvenSplit;
    renderEvenPairing();
}

function renderEvenPairing() {
    const wrap = document.getElementById('evenPairingSvgWrap');
    const text = document.getElementById('evenAnalysisText');
    if (!wrap) return;

    const pairs = currentEvenNum / 2;
    text.textContent = `${currentEvenNum} items form ${pairs} complete pairs. Both parallel rows have equal length (${pairs} and ${pairs}). Remainder = 0. Therefore, ${currentEvenNum} is an EVEN number.`;

    const svgWidth = 420;
    const svgHeight = 200;
    const colW = Math.min(36, 360 / pairs);
    const startX = (svgWidth - (pairs * colW)) / 2 + (colW / 2);

    let dotsSvg = '';
    for (let c = 0; c < pairs; c++) {
        const x = startX + c * colW;
        dotsSvg += `
            <g>
                <circle cx="${x}" cy="65" r="12" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <circle cx="${x}" cy="135" r="12" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <line x1="${x}" y1="77" x2="${x}" y2="123" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3 3"/>
            </g>
        `;
    }

    let splitLine = '';
    if (isEvenSplit) {
        splitLine = `
            <line x1="20" y1="100" x2="${svgWidth - 20}" y2="100" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 4"/>
            <text x="30" y="94" font-size="11" font-weight="bold" fill="#38bdf8">Upper Half: ${pairs}</text>
            <text x="30" y="118" font-size="11" font-weight="bold" fill="#38bdf8">Lower Half: ${pairs}</text>
        `;
    }

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            ${dotsSvg}
            ${splitLine}
        </svg>
    `;
}

// Sim 9: Odd Number Remainder
let currentOddNum = 7;
let isOddRemainderHighlighted = false;

function setOddNumber(n) {
    currentOddNum = n;
    isOddRemainderHighlighted = false;
    renderOddPairing();
}

function highlightOddRemainder() {
    isOddRemainderHighlighted = !isOddRemainderHighlighted;
    renderOddPairing();
}

function renderOddPairing() {
    const wrap = document.getElementById('oddPairingSvgWrap');
    const text = document.getElementById('oddAnalysisText');
    if (!wrap) return;

    const pairs = Math.floor(currentOddNum / 2);
    text.textContent = `${currentOddNum} items form ${pairs} complete pairs (${pairs * 2} items), leaving exactly 1 lonely remainder item! (${currentOddNum} = 2 × ${pairs} + 1). Therefore, ${currentOddNum} is an ODD number.`;

    const svgWidth = 420;
    const svgHeight = 200;
    const colW = Math.min(36, 360 / (pairs + 1));
    const startX = (svgWidth - ((pairs + 1) * colW)) / 2 + (colW / 2);

    let dotsSvg = '';
    for (let c = 0; c < pairs; c++) {
        const x = startX + c * colW;
        dotsSvg += `
            <g>
                <circle cx="${x}" cy="65" r="12" fill="#f43f5e" stroke="#be123c" stroke-width="2"/>
                <circle cx="${x}" cy="135" r="12" fill="#f43f5e" stroke="#be123c" stroke-width="2"/>
                <line x1="${x}" y1="77" x2="${x}" y2="123" stroke="#fda4af" stroke-width="1.5" stroke-dasharray="3 3"/>
            </g>
        `;
    }

    // Remainder dot
    const remX = startX + pairs * colW;
    const halo = isOddRemainderHighlighted ? `<circle cx="${remX}" cy="65" r="22" fill="#fbbf24" opacity="0.3" class="animate-pulse"/><rect x="${remX - 35}" y="100" width="70" height="20" rx="4" fill="#78350f" stroke="#fbbf24"/><text x="${remX}" y="114" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Remainder: 1</text>` : '';
    dotsSvg += `
        <g>
            ${halo}
            <circle cx="${remX}" cy="65" r="12" fill="#fbbf24" stroke="#b45309" stroke-width="2"/>
            <text x="${remX}" y="42" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Leftover</text>
        </g>
    `;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            ${dotsSvg}
        </svg>
    `;
}

// Sim 10: Numbers 1 to 20
let numbersFilterMode = 'all';

function filterNumbersMode(mode) {
    numbersFilterMode = mode;
    const b1 = document.getElementById('filterAllBtn');
    const b2 = document.getElementById('filterEvensBtn');
    const b3 = document.getElementById('filterOddsBtn');

    [b1, b2, b3].forEach(b => b.className = 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700');
    if (mode === 'all') b1.className = 'px-2 py-0.5 bg-indigo-600 text-white font-bold text-xs rounded';
    if (mode === 'evens') b2.className = 'px-2 py-0.5 bg-indigo-600 text-white font-bold text-xs rounded';
    if (mode === 'odds') b3.className = 'px-2 py-0.5 bg-indigo-600 text-white font-bold text-xs rounded';

    renderNumbers1to20Grid();
}

function renderNumbers1to20Grid() {
    const container = document.getElementById('numbers1to20Grid');
    if (!container) return;

    let itemsHtml = '';
    for (let i = 1; i <= 20; i++) {
        const isEven = (i % 2 === 0);
        let opacity = 'opacity-100';
        if (numbersFilterMode === 'evens' && !isEven) opacity = 'opacity-20';
        if (numbersFilterMode === 'odds' && isEven) opacity = 'opacity-20';

        const bgCls = isEven ? 'bg-blue-900/60 border-blue-500 text-blue-200' : 'bg-amber-900/60 border-amber-500 text-amber-200';
        const badge = isEven ? 'Even' : 'Odd';

        itemsHtml += `
            <div class="p-2 rounded-lg border flex flex-col items-center justify-center font-mono ${bgCls} ${opacity} transition-all">
                <span class="text-base font-black">${i}</span>
                <span class="text-[9px] uppercase tracking-wider font-bold mt-0.5">${badge}</span>
            </div>
        `;
    }
    container.innerHTML = itemsHtml;
}

// Sim 11: Crayon Number Grid (1-50)
let crayonCircleOdds = false;
let crayonSquareEvens = false;

function toggleCrayonMarks(type) {
    if (type === 'odds') crayonCircleOdds = !crayonCircleOdds;
    if (type === 'evens') crayonSquareEvens = !crayonSquareEvens;
    renderCrayonGrid();
}

function resetCrayonGrid() {
    crayonCircleOdds = false;
    crayonSquareEvens = false;
    renderCrayonGrid();
}

function renderCrayonGrid() {
    const container = document.getElementById('crayonGridContainer');
    if (!container) return;

    let cellsHtml = '';
    for (let i = 1; i <= 50; i++) {
        const isEven = (i % 2 === 0);
        let markClass = 'border-slate-800 bg-slate-900/60 text-slate-300';

        if (crayonCircleOdds && !isEven) {
            markClass = 'border-amber-400 bg-amber-950/80 text-amber-300 rounded-full font-bold shadow-lg';
        } else if (crayonSquareEvens && isEven) {
            markClass = 'border-blue-400 bg-blue-950/80 text-blue-300 rounded-none font-bold shadow-lg';
        }

        cellsHtml += `<div class="p-1 border text-xs flex items-center justify-center transition-all ${markClass}">${i}</div>`;
    }
    container.innerHTML = cellsHtml;
}

// Sim 12: Book Page Parity
let currentBookLeftPage = 42;

function turnBookPage(dir) {
    currentBookLeftPage = Math.max(2, currentBookLeftPage + (dir * 2));
    renderBookSpread();
}

function renderBookSpread() {
    const leftNum = currentBookLeftPage;
    const rightNum = currentBookLeftPage + 1;
    const sum = leftNum + rightNum;

    document.getElementById('bookLeftPageNum').textContent = leftNum;
    document.getElementById('bookRightPageNum').textContent = rightNum;
    document.getElementById('bookSpreadSumText').textContent = `Page ${leftNum} (Even) + Page ${rightNum} (Odd) = ${sum} (Always ODD!)`;
}

// Sim 13: Multi-Digit Parity Rule
let scannedNumber = 415;

function scanMultiDigit(num) {
    scannedNumber = num;
    renderDigitBreakdown();
}

function renderDigitBreakdown() {
    const container = document.getElementById('digitBreakdownDisplay');
    const exp = document.getElementById('multiDigitExplanation');
    if (!container) return;

    const str = scannedNumber.toString();
    const len = str.length;
    const onesDigit = parseInt(str[len - 1]);
    const isEven = (onesDigit % 2 === 0);

    let digitsHtml = '';
    for (let i = 0; i < len; i++) {
        const digit = str[i];
        const isLast = (i === len - 1);
        if (isLast) {
            digitsHtml += `
                <div class="flex flex-col items-center">
                    <span class="text-[9px] font-bold text-cyan-400 uppercase tracking-widest mb-1">Ones (Decider!)</span>
                    <div class="w-14 h-16 bg-cyan-950 border-2 border-cyan-400 rounded-lg flex items-center justify-center text-3xl font-black text-cyan-200 font-mono shadow-lg ring-4 ring-cyan-500/20">${digit}</div>
                    <span class="text-[10px] font-bold mt-1 ${isEven ? 'text-emerald-400' : 'text-rose-400'}">${isEven ? 'EVEN DIGIT' : 'ODD DIGIT'}</span>
                </div>
            `;
        } else {
            const placeLabel = (len - 1 - i === 1) ? 'Tens' : (len - 1 - i === 2) ? 'Hundreds' : 'Thousands';
            digitsHtml += `
                <div class="flex flex-col items-center opacity-60">
                    <span class="text-[9px] text-slate-400 uppercase tracking-widest mb-1">${placeLabel}</span>
                    <div class="w-14 h-16 bg-slate-800 border border-slate-700 rounded-lg flex items-center justify-center text-3xl font-black text-slate-300 font-mono">${digit}</div>
                    <span class="text-[9px] text-slate-500 mt-1">Paired (Even)</span>
                </div>
            `;
        }
    }

    container.innerHTML = digitsHtml;
    exp.textContent = `In ${scannedNumber}, the ones digit is ${onesDigit}. Since ${onesDigit} is ${isEven ? 'an even' : 'an odd'} digit, the entire number ${scannedNumber} is ${isEven ? 'EVEN' : 'ODD'}!`;
}

// Sim 14: Digit Permutation Parity
let permTens = 1;
let permOnes = 6;

function loadPermutationPair(d1, d2) {
    permTens = d1;
    permOnes = d2;
    renderPermutationCards();
}

function swapDigitCards() {
    const temp = permTens;
    permTens = permOnes;
    permOnes = temp;
    renderPermutationCards();
}

function renderPermutationCards() {
    const tensEl = document.getElementById('tensCard');
    const onesEl = document.getElementById('onesCard');
    const textEl = document.getElementById('permutationAnalysisText');

    if (tensEl) tensEl.textContent = permTens;
    if (onesEl) onesEl.textContent = permOnes;

    const num = permTens * 10 + permOnes;
    const isEven = (permOnes % 2 === 0);

    if (textEl) {
        textEl.textContent = `Assembled Number: ${num}. Ones digit is ${permOnes} (${isEven ? 'Even' : 'Odd'}) -> ${num} is an ${isEven ? 'EVEN' : 'ODD'} number.`;
    }
}

// Sim 15: Consecutive Number Alternation
let consecutiveStart = 41;

function shiftConsecutiveWindow(d) {
    consecutiveStart = Math.max(1, Math.min(85, consecutiveStart + d));
    renderConsecutiveStrip();
}

function renderConsecutiveStrip() {
    const container = document.getElementById('consecutiveStripContainer');
    if (!container) return;

    let stripHtml = '';
    for (let i = 0; i < 10; i++) {
        const num = consecutiveStart + i;
        const isEven = (num % 2 === 0);
        const bgCls = isEven ? 'bg-blue-900/60 border-blue-500 text-blue-200' : 'bg-amber-900/60 border-amber-500 text-amber-200';
        stripHtml += `
            <div class="flex-1 py-3 px-1 rounded-lg border text-center font-mono ${bgCls}">
                <span class="text-sm font-black block">${num}</span>
                <span class="text-[8px] font-bold uppercase tracking-wider block mt-1">${isEven ? 'Even' : 'Odd'}</span>
            </div>
        `;
    }
    container.innerHTML = stripHtml;
}

// Sim 16: Range Parity Balance
let balanceRangeVal = 100;

function setBalanceRange(rng) {
    balanceRangeVal = rng;
    renderBalanceScale();
}

function renderBalanceScale() {
    const wrap = document.getElementById('balanceScaleSvgWrap');
    if (!wrap) return;

    const count = balanceRangeVal / 2;
    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Central Scale Base & Pillar -->
            <polygon points="210,160 190,195 230,195" fill="#475569"/>
            <line x1="210" y1="60" x2="210" y2="160" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
            <circle cx="210" cy="60" r="8" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>

            <!-- Balance Beam (Horizontally Balanced) -->
            <line x1="70" y1="60" x2="350" y2="60" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>

            <!-- Left Pan: Odd Numbers -->
            <line x1="100" y1="60" x2="70" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="100" y1="60" x2="130" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M 60 120 Q 100 145 140 120 Z" fill="#92400e" stroke="#f59e0b" stroke-width="2"/>
            <text x="100" y="112" font-size="11" font-weight="bold" fill="#fde68a" text-anchor="middle">${count} Odd Numbers</text>
            <text x="100" y="136" font-size="9" fill="#fef08a" text-anchor="middle">1, 3, 5... ${balanceRangeVal - 1}</text>

            <!-- Right Pan: Even Numbers -->
            <line x1="320" y1="60" x2="290" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="320" y1="60" x2="350" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M 280 120 Q 320 145 360 120 Z" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
            <text x="320" y="112" font-size="11" font-weight="bold" fill="#bae6fd" text-anchor="middle">${count} Even Numbers</text>
            <text x="320" y="136" font-size="9" fill="#e0f2fe" text-anchor="middle">2, 4, 6... ${balanceRangeVal}</text>

            <!-- Center Invariant Badge -->
            <rect x="160" y="20" width="100" height="24" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="210" y="36" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">50-50 Balance</text>
        </svg>
    `;
}

// Master Dispatcher for Simulator Initialization
function initSlideSim(slideId) {
    if (slideId === 1) renderOrchardGrid();
    if (slideId === 2) renderPotteryStacks();
    if (slideId === 3) renderSweetTrays();
    if (slideId === 4) renderMoneyMandala();
    if (slideId === 5) renderWallet();
    if (slideId === 6) renderDistribution();
    if (slideId === 7) renderPairingLab();
    if (slideId === 8) renderEvenPairing();
    if (slideId === 9) renderOddPairing();
    if (slideId === 10) renderNumbers1to20Grid();
    if (slideId === 11) renderCrayonGrid();
    if (slideId === 12) renderBookSpread();
    if (slideId === 13) renderDigitBreakdown();
    if (slideId === 14) renderPermutationCards();
    if (slideId === 15) renderConsecutiveStrip();
    if (slideId === 16) renderBalanceScale();
}

// On Page Load
document.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            selectIndianMaleVoice();
        };
    }
});

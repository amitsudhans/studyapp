
// State Management
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;

// Audio Feedback Chime (Web Audio API)
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playChime(isCorrect) {
    if (!audioCtx) return;
    try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        const now = audioCtx.currentTime;
        if (isCorrect) {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(523.25, now);
            osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.12);
            osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.25);
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
            osc.start(now);
            osc.stop(now + 0.35);
        } else {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(220, now);
            osc.frequency.exponentialRampToValueAtTime(160, now + 0.2);
            gain.gain.setValueAtTime(0.12, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        }
    } catch(e) {}
}

// Speech Engine - Indian English Male Teacher Priority
function selectIndianMaleVoice() {
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    const femaleKeywords = [
        'female', 'woman', 'girl', 'zira', 'jenny', 'aria',
        'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera',
        'aditi', 'kavya', 'ananya', 'shreya', 'sunita'
    ];

    function isFemale(name) {
        const lower = name.toLowerCase();
        return femaleKeywords.some(kw => lower.includes(kw));
    }

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

    for (const name of indianMalePriority) {
        const found = voices.find(v => v.name.includes(name) && !isFemale(v.name));
        if (found) return found;
    }

    const anyIndianMale = voices.find(v => (v.lang === 'en-IN' || v.lang === 'hi-IN') && !isFemale(v.name));
    if (anyIndianMale) return anyIndianMale;

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

    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));

    currentSlide = slideNum;
    const activeSlide = document.getElementById(`slide-${currentSlide}`);
    if (activeSlide) {
        activeSlide.classList.remove('hidden');
    }

    const currentNumDisplay = document.getElementById('currentSlideNum');
    if (currentNumDisplay) currentNumDisplay.textContent = currentSlide;

    const progressBar = document.getElementById('chapterProgressBar');
    if (progressBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progressBar.style.width = `${pct}%`;
    }

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

    // Terminal Slide Invariant for Slide 20
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

    // Hide audio button on challenge slides
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }

    initSlideSim(currentSlide);
    window.scrollTo({ top: 0, behavior: 'smooth' });
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

    const isCorrect = (optIdx === cp.ans);
    playChime(isCorrect);

    if (fbEl) {
        fbEl.classList.remove('hidden');
        if (isCorrect) {
            fbEl.innerHTML = `<div class="p-2 bg-emerald-950/60 border border-emerald-500/40 rounded text-emerald-300 text-xs"><strong>Correct!</strong> ${cp.exp}</div>`;
        } else {
            fbEl.innerHTML = `<div class="p-2 bg-rose-950/60 border border-rose-500/40 rounded text-rose-300 text-xs"><strong>Incorrect.</strong> ${cp.exp}</div>`;
        }
    }
}

// Quiz Interaction for Challenge Slides (17-20)
function selectQuizOption(qId, optIdx) {
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

    const isCorrect = (optIdx === targetQ.ans);
    playChime(isCorrect);

    if (fbEl) {
        fbEl.classList.remove('hidden');
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

// ==============================================
// 16 BESPOKE SIMULATOR CONTROLLER FUNCTIONS
// ==============================================

// Sim 1: Pantry Inventory
let currentPantryItem = 'rice';
const pantryData = {
    rice: { val: 68, unit: 'kg', name: 'Fragrant Rice', h: 0, t: 6, o: 8, exp: '60 + 8' },
    flour: { val: 45, unit: 'kg', name: 'Wheat Flour', h: 0, t: 4, o: 5, exp: '40 + 5' },
    oil: { val: 32, unit: 'L', name: 'Cooking Oil', h: 0, t: 3, o: 2, exp: '30 + 2' },
    veggies: { val: 240, unit: 'kg', name: 'Seasonal Veggies', h: 2, t: 4, o: 0, exp: '200 + 40 + 0' }
};

function selectPantryItem(itemKey) {
    currentPantryItem = itemKey;
    const btnRice = document.getElementById('pantryRiceBtn');
    const btnFlour = document.getElementById('pantryFlourBtn');
    const btnOil = document.getElementById('pantryOilBtn');
    const btnVeg = document.getElementById('pantryVegBtn');

    [btnRice, btnFlour, btnOil, btnVeg].forEach(b => {
        if (b) b.className = 'px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700';
    });

    if (itemKey === 'rice' && btnRice) btnRice.className = 'px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';
    if (itemKey === 'flour' && btnFlour) btnFlour.className = 'px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';
    if (itemKey === 'oil' && btnOil) btnOil.className = 'px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';
    if (itemKey === 'veggies' && btnVeg) btnVeg.className = 'px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all';

    renderPantryInventory();
}

function renderPantryInventory() {
    const wrap = document.getElementById('pantrySvgWrap');
    if (!wrap) return;

    const data = pantryData[currentPantryItem];
    document.getElementById('pantryItemDisplay').textContent = `${data.val} ${data.unit} (${data.name})`;
    document.getElementById('pantryPlaceBreakdown').textContent = data.h > 0 ? `${data.h} Hundreds + ${data.t} Tens + ${data.o} Ones` : `${data.t} Tens + ${data.o} Ones`;
    document.getElementById('pantryExpandedDisplay').textContent = data.exp;

    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Pantry Shelf -->
            <rect x="20" y="160" width="${svgWidth - 40}" height="14" fill="#78350f" rx="3" stroke="#451a03"/>
            <!-- Sacks / Canisters -->
            <g transform="translate(160, 40)">
                <path d="M 20 20 Q 50 10 80 20 Q 95 60 90 120 Q 50 125 10 120 Q 5 60 20 20 Z" fill="#d97706" stroke="#92400e" stroke-width="2"/>
                <ellipse cx="50" cy="20" rx="30" ry="8" fill="#b45309"/>
                <text x="50" y="65" font-size="16" font-weight="black" fill="#451a03" text-anchor="middle" font-mono>${data.val} ${data.unit}</text>
                <text x="50" y="85" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">${data.name}</text>
                <rect x="22" y="98" width="56" height="16" rx="3" fill="#fef3c7" opacity="0.8"/>
                <text x="50" y="110" font-size="9" font-weight="bold" fill="#92400e" text-anchor="middle">${data.exp}</text>
            </g>
        </svg>
    `;
}

// Sim 2: Attendance Block Tracker
let currentAttendanceSlot = 3;
const attendanceData = {
    1: { time: '11:00 AM', count: 52, h: 0, t: 5, o: 2, desc: 'Opening morning shift: 52 guests (0 Hundreds + 5 Tens + 2 Ones).' },
    2: { time: '12:00 PM', count: 325, h: 3, t: 2, o: 5, desc: 'Early afternoon lunch rush: 325 guests (3 Hundreds + 2 Tens + 5 Ones).' },
    3: { time: '1:00 PM', count: 508, h: 5, t: 0, o: 8, desc: 'Peak shift: 508 guests! 5 Hundreds + 0 Tens + 8 Ones. Zero holds tens place!' },
    4: { time: '2:00 PM', count: 145, h: 1, t: 4, o: 5, desc: 'Late afternoon lunch: 145 guests (1 Hundred + 4 Tens + 5 Ones).' }
};

function setAttendanceSlot(s) {
    currentAttendanceSlot = s;
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`slot${i}Btn`);
        if (btn) {
            btn.className = (i === s) ? 'px-2 py-1 bg-blue-500 text-slate-950 text-xs rounded font-bold shadow' : 'px-2 py-1 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700 font-bold';
        }
    }
    renderAttendanceTracker();
}

function renderAttendanceTracker() {
    const wrap = document.getElementById('attendanceSvgWrap');
    const exp = document.getElementById('attendanceExplanation');
    if (!wrap) return;

    const data = attendanceData[currentAttendanceSlot];
    if (exp) exp.textContent = `${data.time} Slot: ${data.count} Diners. ${data.desc}`;

    const svgWidth = 420;
    const svgHeight = 200;

    let hundredsBlocks = '';
    for (let i = 0; i < data.h; i++) {
        const bx = 30 + i * 28;
        hundredsBlocks += `<rect x="${bx}" y="60" width="24" height="24" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" rx="2"/>`;
    }

    let tensRods = '';
    for (let i = 0; i < data.t; i++) {
        const rx = 185 + i * 14;
        tensRods += `<rect x="${rx}" y="60" width="8" height="40" fill="#eab308" stroke="#a16207" stroke-width="1.5" rx="1"/>`;
    }
    if (data.t === 0) {
        tensRods = `<text x="210" y="85" font-size="12" font-weight="bold" fill="#64748b" text-anchor="middle">0 Tens</text>`;
    }

    let onesCubes = '';
    for (let i = 0; i < data.o; i++) {
        const ox = 310 + (i % 4) * 16;
        const oy = 60 + Math.floor(i / 4) * 16;
        onesCubes += `<rect x="${ox}" y="${oy}" width="10" height="10" fill="#10b981" stroke="#047857" stroke-width="1.5" rx="1"/>`;
    }

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Column Labels -->
            <rect x="20" y="20" width="140" height="24" rx="4" fill="#1e3a8a" opacity="0.4"/>
            <text x="90" y="36" font-size="11" font-weight="bold" fill="#60a5fa" text-anchor="middle">Hundreds (${data.h})</text>

            <rect x="170" y="20" width="110" height="24" rx="4" fill="#854d0e" opacity="0.4"/>
            <text x="225" y="36" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">Tens (${data.t})</text>

            <rect x="290" y="20" width="110" height="24" rx="4" fill="#065f46" opacity="0.4"/>
            <text x="345" y="36" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Ones (${data.o})</text>

            ${hundredsBlocks}
            ${tensRods}
            ${onesCubes}

            <!-- Total Banner -->
            <text x="210" y="175" font-size="16" font-weight="black" fill="#f8fafc" text-anchor="middle" font-mono>Total Attendees: ${data.count}</text>
        </svg>
    `;
}

// Sim 3: Digit Manipulation
let curHundredsCard = 8;
let curTensCard = 7;
let curOnesCard = 5;

function presetDigitChallenge(type) {
    const b1 = document.getElementById('btnLargest3d');
    const b2 = document.getElementById('btnSmallest3d');
    const b3 = document.getElementById('btnUnder550');
    const exp = document.getElementById('digitCardExplanation');

    [b1, b2, b3].forEach(b => { if (b) b.className = 'px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700'; });

    if (type === 'largest') {
        if (b1) b1.className = 'px-2 py-0.5 bg-violet-600 text-white font-bold text-xs rounded';
        curHundredsCard = 8; curTensCard = 7; curOnesCard = 5;
        if (exp) exp.textContent = "Largest 3-Digit Value: 875. Formed by selecting 8 (Hundreds), 7 (Tens), and 5 (Ones).";
    } else if (type === 'smallest') {
        if (b2) b2.className = 'px-2 py-0.5 bg-violet-600 text-white font-bold text-xs rounded';
        curHundredsCard = 3; curTensCard = 0; curOnesCard = 5;
        if (exp) exp.textContent = "Smallest Valid 3-Digit Value: 305. 0 cannot occupy hundreds place! 3 (Hundreds), 0 (Tens), 5 (Ones).";
    } else {
        if (b3) b3.className = 'px-2 py-0.5 bg-violet-600 text-white font-bold text-xs rounded';
        curHundredsCard = 5; curTensCard = 3; curOnesCard = 7;
        if (exp) exp.textContent = "Number Strictly Under 550: 537. 5 Hundreds + 3 Tens + 7 Ones (537 < 550).";
    }

    const hSlot = document.getElementById('cardHundredsSlot');
    const tSlot = document.getElementById('cardTensSlot');
    const oSlot = document.getElementById('cardOnesSlot');

    if (hSlot) hSlot.textContent = curHundredsCard;
    if (tSlot) tSlot.textContent = curTensCard;
    if (oSlot) oSlot.textContent = curOnesCard;
}

// Sim 4: Number Line Skip Counter
let currentLineVal = 340;

function skipNumberLine(delta) {
    currentLineVal = Math.max(200, Math.min(600, currentLineVal + delta));
    renderNumberLine();
}

function resetNumberLine(v) {
    currentLineVal = v;
    renderNumberLine();
}

function renderNumberLine() {
    const wrap = document.getElementById('numberLineSvgWrap');
    if (!wrap) return;

    document.getElementById('numberLineCurrentVal').textContent = currentLineVal;
    document.getElementById('numberLinePrevVal').textContent = currentLineVal - 10;
    document.getElementById('numberLineNextVal').textContent = currentLineVal + 10;

    const svgWidth = 420;
    const svgHeight = 200;
    const minVal = 200;
    const maxVal = 600;
    const trackX1 = 40;
    const trackX2 = svgWidth - 40;
    const trackY = 100;

    const markerX = trackX1 + ((currentLineVal - minVal) / (maxVal - minVal)) * (trackX2 - trackX1);

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Main Axis Line -->
            <line x1="${trackX1}" y1="${trackY}" x2="${trackX2}" y2="${trackY}" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>

            <!-- Major 50 Ticks -->
            ${[200, 250, 300, 350, 400, 450, 500, 550, 600].map(val => {
                const tx = trackX1 + ((val - minVal) / (maxVal - minVal)) * (trackX2 - trackX1);
                return `
                    <line x1="${tx}" y1="${trackY - 10}" x2="${tx}" y2="${trackY + 10}" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="${tx}" y="${trackY + 26}" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle" font-mono>${val}</text>
                `;
            }).join('')}

            <!-- Active Position Marker -->
            <g transform="translate(${markerX}, ${trackY})">
                <circle cx="0" cy="0" r="10" fill="#14b8a6" stroke="#0f766e" stroke-width="3" class="animate-pulse"/>
                <polygon points="0,-14 -8,-24 8,-24" fill="#f59e0b"/>
                <rect x="-24" y="-48" width="48" height="22" rx="4" fill="#0f172a" stroke="#14b8a6" stroke-width="1.5"/>
                <text x="0" y="-33" font-size="11" font-weight="black" fill="#2dd4bf" text-anchor="middle" font-mono>${currentLineVal}</text>
            </g>
        </svg>
    `;
}

// Sim 5: Indian System Multiplier
let indianDigit = 5;

function setIndianSystemDigit(d) {
    indianDigit = d;
    renderIndianSystem();
}

function renderIndianSystem() {
    const wrap = document.getElementById('indianSystemSvgWrap');
    const text = document.getElementById('indianSystemText');
    if (!wrap) return;

    if (text) {
        text.textContent = `Each step to the left multiplies place value by 10: ${indianDigit} in Ones = ${indianDigit}, in Tens = ${indianDigit * 10}, in Hundreds = ${indianDigit * 100}, in Thousands = ${indianDigit * 1000}!`;
    }

    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- 4 Place Columns -->
            <!-- Thousands -->
            <g transform="translate(30, 40)">
                <rect width="80" height="110" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
                <text x="40" y="24" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Thousands (×1000)</text>
                <text x="40" y="68" font-size="32" font-weight="black" fill="#818cf8" text-anchor="middle" font-mono>${indianDigit}</text>
                <text x="40" y="96" font-size="10" font-weight="bold" fill="#c7d2fe" text-anchor="middle">${indianDigit * 1000}</text>
            </g>

            <!-- Arrow 1 -->
            <path d="M 120 95 L 135 95" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrowhead)"/>
            <text x="128" y="85" font-size="9" font-weight="bold" fill="#f59e0b" text-anchor="middle">÷10</text>

            <!-- Hundreds -->
            <g transform="translate(130, 40)">
                <rect width="75" height="110" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
                <text x="37" y="24" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Hundreds (×100)</text>
                <text x="37" y="68" font-size="32" font-weight="black" fill="#818cf8" text-anchor="middle" font-mono>${indianDigit}</text>
                <text x="37" y="96" font-size="10" font-weight="bold" fill="#c7d2fe" text-anchor="middle">${indianDigit * 100}</text>
            </g>

            <!-- Tens -->
            <g transform="translate(225, 40)">
                <rect width="75" height="110" rx="6" fill="#1e1b4b" stroke="#a5b4fc" stroke-width="2"/>
                <text x="37" y="24" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Tens (×10)</text>
                <text x="37" y="68" font-size="32" font-weight="black" fill="#818cf8" text-anchor="middle" font-mono>${indianDigit}</text>
                <text x="37" y="96" font-size="10" font-weight="bold" fill="#c7d2fe" text-anchor="middle">${indianDigit * 10}</text>
            </g>

            <!-- Ones -->
            <g transform="translate(320, 40)">
                <rect width="75" height="110" rx="6" fill="#1e1b4b" stroke="#c7d2fe" stroke-width="2"/>
                <text x="37" y="24" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Ones (×1)</text>
                <text x="37" y="68" font-size="32" font-weight="black" fill="#818cf8" text-anchor="middle" font-mono>${indianDigit}</text>
                <text x="37" y="96" font-size="10" font-weight="bold" fill="#c7d2fe" text-anchor="middle">${indianDigit}</text>
            </g>
        </svg>
    `;
}

// Sim 6: Threshold Counter
let thresholdCountVal = 999;

function stepThresholdCounter(d) {
    thresholdCountVal = Math.max(990, Math.min(1010, thresholdCountVal + d));
    renderThresholdCounter();
}

function resetThresholdCounter(val) {
    thresholdCountVal = val;
    renderThresholdCounter();
}

function renderThresholdCounter() {
    const container = document.getElementById('thresholdOdometerDisplay');
    const badge = document.getElementById('thresholdMilestoneBadge');
    const exp = document.getElementById('thresholdExplanation');
    if (!container) return;

    const str = thresholdCountVal.toString();
    const is4Digit = thresholdCountVal >= 1000;

    let digitsHtml = '';
    for (let i = 0; i < str.length; i++) {
        const d = str[i];
        const isThousands = (is4Digit && i === 0);
        const bg = isThousands ? 'bg-amber-500 text-slate-950 font-black ring-4 ring-amber-400/40' : 'bg-slate-800 text-slate-100 font-bold';
        digitsHtml += `<div class="w-14 h-20 rounded-xl flex items-center justify-center text-4xl shadow-inner font-mono border border-slate-700 ${bg}">${d}</div>`;
    }

    container.innerHTML = digitsHtml;

    if (badge) {
        if (thresholdCountVal === 999) {
            badge.className = 'mt-3 px-3 py-1 bg-amber-500/20 border border-amber-500/40 rounded-full text-amber-300 text-xs font-bold animate-pulse';
            badge.textContent = 'Largest 3-Digit Number!';
        } else if (thresholdCountVal === 1000) {
            badge.className = 'mt-3 px-3 py-1 bg-emerald-500/20 border border-emerald-500/40 rounded-full text-emerald-300 text-xs font-bold animate-bounce';
            badge.textContent = '🎉 Smallest 4-Digit Number Milestone (1,000)!';
        } else if (thresholdCountVal > 1000) {
            badge.className = 'mt-3 px-3 py-1 bg-cyan-500/20 border border-cyan-500/40 rounded-full text-cyan-300 text-xs font-bold';
            badge.textContent = 'Four-Digit Counting Sequence';
        } else {
            badge.className = 'mt-3 px-3 py-1 bg-slate-800 border border-slate-700 rounded-full text-slate-400 text-xs font-bold';
            badge.textContent = 'Three-Digit Range';
        }
    }

    if (exp) {
        if (thresholdCountVal === 1000) {
            exp.textContent = 'One Thousand (1,000) Reached! Ten hundreds bundled into 1 Thousand column on the left.';
        } else if (thresholdCountVal === 999) {
            exp.textContent = 'At 999, all 3 columns are full. Adding 1 unit triggers complete regrouping into 1,000!';
        } else {
            exp.textContent = `Sequential counter at ${thresholdCountVal}. Observe how units and tens advance sequentially.`;
        }
    }
}

// Sim 7: Real-World Thousands
let currentHeritageFact = 'temple';
const heritageData = {
    temple: {
        title: 'Thousand Pillars Temple',
        loc: 'Moodubidiri, Karnataka',
        val: '1,000 Pillars',
        desc: 'Saavira Kambada Basadi (built in 1500s) is famous for its 1,000 carved granite pillars where no two pillars are identical!'
    },
    rhino: {
        title: 'Indian Rhinoceros Conservation',
        loc: 'Kaziranga, Assam',
        val: '4,000+ Rhinos',
        desc: 'Dedicated conservation rebounded the rhino population from under 200 animals to over 4,000 today! Adult males weigh up to 2,700 kg.'
    },
    coast: {
        title: 'Coastline of India',
        loc: 'Indian Ocean & Arabian Sea',
        val: '7,500 km',
        desc: 'India stretches across 7,500 kilometers of magnificent coastal shoreline, bordered by 9 coastal states and 4 island territories.'
    },
    districts: {
        title: 'Administrative Districts',
        loc: 'All India',
        val: '788 Districts',
        desc: 'India is divided into 788 administrative districts across 28 states and 8 union territories, celebrating over 1,000 local festivals!'
    }
};

function selectHeritageFact(key) {
    currentHeritageFact = key;
    const b1 = document.getElementById('factTempleBtn');
    const b2 = document.getElementById('factRhinoBtn');
    const b3 = document.getElementById('factCoastBtn');
    const b4 = document.getElementById('factDistBtn');

    [b1, b2, b3, b4].forEach(b => {
        if (b) b.className = 'px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700';
    });

    if (key === 'temple' && b1) b1.className = 'px-2 py-1 bg-orange-500 text-slate-950 font-bold text-xs rounded';
    if (key === 'rhino' && b2) b2.className = 'px-2 py-1 bg-orange-500 text-slate-950 font-bold text-xs rounded';
    if (key === 'coast' && b3) b3.className = 'px-2 py-1 bg-orange-500 text-slate-950 font-bold text-xs rounded';
    if (key === 'districts' && b4) b4.className = 'px-2 py-1 bg-orange-500 text-slate-950 font-bold text-xs rounded';

    renderHeritageFact();
}

function renderHeritageFact() {
    const wrap = document.getElementById('heritageSvgWrap');
    const desc = document.getElementById('heritageDescriptionText');
    if (!wrap) return;

    const data = heritageData[currentHeritageFact];
    if (desc) desc.textContent = `${data.title} (${data.loc}): ${data.desc}`;

    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <rect width="${svgWidth}" height="${svgHeight}" rx="8" fill="#431407" opacity="0.4"/>
            <circle cx="210" cy="85" r="50" fill="#78350f" stroke="#f97316" stroke-width="2"/>
            <text x="210" y="78" font-size="18" font-weight="black" fill="#fed7aa" text-anchor="middle">${data.val}</text>
            <text x="210" y="98" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">${data.title}</text>
            <text x="210" y="155" font-size="11" fill="#fdba74" text-anchor="middle font-medium">${data.loc}</text>
        </svg>
    `;
}

// Sim 8: Base-Ten Block Builder
let baseTenStage = 4;

function setBaseTenStage(s) {
    baseTenStage = s;
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnStage${i}`);
        if (btn) {
            btn.className = (i === s) ? 'px-2 py-0.5 bg-cyan-500 text-slate-950 font-bold text-xs rounded shadow' : 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700';
        }
    }
    renderBaseTenBlocks();
}

function renderBaseTenBlocks() {
    const wrap = document.getElementById('baseTenSvgWrap');
    const exp = document.getElementById('baseTenExplanation');
    if (!wrap) return;

    const svgWidth = 420;
    const svgHeight = 200;

    let contentSvg = '';
    if (baseTenStage === 1) {
        if (exp) exp.textContent = "1 Unit Cube = Represents 1 single unit.";
        contentSvg = `
            <g transform="translate(195, 80)">
                <rect width="30" height="30" fill="#38bdf8" stroke="#0284c7" stroke-width="2" rx="2"/>
                <text x="15" y="55" font-size="12" font-weight="bold" fill="#bae6fd" text-anchor="middle">1 Unit</text>
            </g>
        `;
    } else if (baseTenStage === 2) {
        if (exp) exp.textContent = "1 Ten-Rod = 10 single units connected side by side (1 Ten = 10).";
        contentSvg = `
            <g transform="translate(130, 85)">
                <rect width="160" height="20" fill="#eab308" stroke="#a16207" stroke-width="2" rx="2"/>
                ${Array.from({length: 10}).map((_, i) => `<line x1="${i * 16}" y1="0" x2="${i * 16}" y2="20" stroke="#713f12" stroke-width="1"/>`).join('')}
                <text x="80" y="42" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">1 Ten-Rod (10)</text>
            </g>
        `;
    } else if (baseTenStage === 3) {
        if (exp) exp.textContent = "1 Hundred-Flat = 10 ten-rods fused into a flat square (10 × 10 = 100).";
        contentSvg = `
            <g transform="translate(160, 40)">
                <rect width="100" height="100" fill="#10b981" stroke="#047857" stroke-width="2" rx="3"/>
                ${Array.from({length: 10}).map((_, i) => `<line x1="${i * 10}" y1="0" x2="${i * 10}" y2="100" stroke="#064e3b" stroke-width="1"/>`).join('')}
                ${Array.from({length: 10}).map((_, i) => `<line x1="0" y1="${i * 10}" x2="100" y2="${i * 10}" stroke="#064e3b" stroke-width="1"/>`).join('')}
                <text x="50" y="125" font-size="12" font-weight="bold" fill="#6ee7b7" text-anchor="middle">1 Hundred-Flat (100)</text>
            </g>
        `;
    } else {
        if (exp) exp.textContent = "1 Thousand-Cube = 10 Hundred-Flats stacked into a 3D cube (10 × 100 = 1,000)!";
        contentSvg = `
            <g transform="translate(160, 45)">
                <!-- Isometric 3D Cube -->
                <polygon points="50,0 110,25 60,60 0,35" fill="#38bdf8" stroke="#0369a1" stroke-width="1.5"/>
                <polygon points="0,35 60,60 60,120 0,95" fill="#0284c7" stroke="#0369a1" stroke-width="1.5"/>
                <polygon points="60,60 110,25 110,85 60,120" fill="#0ea5e9" stroke="#0369a1" stroke-width="1.5"/>
                <text x="55" y="145" font-size="13" font-weight="black" fill="#7dd3fc" text-anchor="middle">1 Thousand-Cube (1000)</text>
            </g>
        `;
    }

    wrap.innerHTML = `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">${contentSvg}</svg>`;
}

// Sim 9: Decomposing 1,000 (Orange Slice Complements)
let orangeSliceIdx = 0;
const orangePairs = [
    { a: 900, b: 100 },
    { a: 850, b: 150 },
    { a: 670, b: 330 },
    { a: 497, b: 503 }
];

function selectOrangeSlice(idx) {
    orangeSliceIdx = idx;
    renderOrangeSlice();
}

function renderOrangeSlice() {
    const wrap = document.getElementById('orangeSliceSvgWrap');
    const eq = document.getElementById('orangeEquationText');
    if (!wrap) return;

    const pair = orangePairs[orangeSliceIdx];
    if (eq) eq.textContent = `${pair.a} + ${pair.b} = 1,000 (Complementary Pair)`;

    const svgWidth = 420;
    const svgHeight = 200;
    const cx = svgWidth / 2;
    const cy = 100;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Orange Circle Background -->
            <circle cx="${cx}" cy="${cy}" r="75" fill="#f97316" stroke="#c2410c" stroke-width="4"/>
            <circle cx="${cx}" cy="${cy}" r="70" fill="#ffedd5"/>

            <!-- Semicircle 1 (A) -->
            <path d="M ${cx} ${cy - 65} A 65 65 0 0 1 ${cx} ${cy + 65} Z" fill="#ea580c"/>
            <text x="${cx + 30}" y="${cy + 6}" font-size="16" font-weight="black" fill="#ffffff" text-anchor="middle" font-mono>${pair.b}</text>

            <!-- Semicircle 2 (B) -->
            <path d="M ${cx} ${cy - 65} A 65 65 0 0 0 ${cx} ${cy + 65} Z" fill="#f59e0b"/>
            <text x="${cx - 30}" y="${cy + 6}" font-size="16" font-weight="black" fill="#451a03" text-anchor="middle" font-mono>${pair.a}</text>

            <line x1="${cx}" y1="${cy - 65}" x2="${cx}" y2="${cy + 65}" stroke="#ffffff" stroke-width="3"/>
        </svg>
    `;
}

// Sim 10: Place-Value Regrouping
let regroupCase = 1;

function loadRegroupCase(c) {
    regroupCase = c;
    for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`rgCase${i}Btn`);
        if (btn) {
            btn.className = (i === c) ? 'px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded' : 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700';
        }
    }
    renderRegrouping();
}

function renderRegrouping() {
    const container = document.getElementById('regroupAnimationContainer');
    const exp = document.getElementById('regroupExplanationText');
    if (!container) return;

    if (regroupCase === 1) {
        container.innerHTML = `
            <div class="p-3 bg-slate-900 border border-slate-700 rounded-lg text-center font-mono">
                <span class="text-xs text-slate-400 block mb-1">Ungrouped</span>
                <span class="text-lg font-bold text-amber-300">1 Ten + 27 Ones</span>
            </div>
            <div class="text-emerald-400 font-bold text-xl">➔</div>
            <div class="p-3 bg-emerald-950 border border-emerald-500 rounded-lg text-center font-mono">
                <span class="text-xs text-emerald-300 block mb-1">Regrouped</span>
                <span class="text-xl font-black text-emerald-200">37 (3T + 7O)</span>
            </div>
        `;
        if (exp) exp.textContent = "1 Ten + 27 Ones: 27 Ones bundles into 2 Tens + 7 Ones. 1 Ten + 2 Tens = 3 Tens. Total = 37!";
    } else if (regroupCase === 2) {
        container.innerHTML = `
            <div class="p-3 bg-slate-900 border border-slate-700 rounded-lg text-center font-mono">
                <span class="text-xs text-slate-400 block mb-1">Ungrouped</span>
                <span class="text-lg font-bold text-amber-300">10 Tens + 6 Ones</span>
            </div>
            <div class="text-emerald-400 font-bold text-xl">➔</div>
            <div class="p-3 bg-emerald-950 border border-emerald-500 rounded-lg text-center font-mono">
                <span class="text-xs text-emerald-300 block mb-1">Regrouped</span>
                <span class="text-xl font-black text-emerald-200">106 (1H + 0T + 6O)</span>
            </div>
        `;
        if (exp) exp.textContent = "10 Tens + 6 Ones: 10 Tens bundles directly into 1 Hundred. Total = 106 (notice 0 tens placeholder)!";
    } else if (regroupCase === 3) {
        container.innerHTML = `
            <div class="p-3 bg-slate-900 border border-slate-700 rounded-lg text-center font-mono">
                <span class="text-xs text-slate-400 block mb-1">Ungrouped</span>
                <span class="text-lg font-bold text-amber-300">11 Tens + 14 Ones</span>
            </div>
            <div class="text-emerald-400 font-bold text-xl">➔</div>
            <div class="p-3 bg-emerald-950 border border-emerald-500 rounded-lg text-center font-mono">
                <span class="text-xs text-emerald-300 block mb-1">Regrouped</span>
                <span class="text-xl font-black text-emerald-200">124 (1H + 2T + 4O)</span>
            </div>
        `;
        if (exp) exp.textContent = "11 Tens + 14 Ones: 14 Ones -> 1 Ten + 4 Ones. 11 Tens + 1 Ten = 12 Tens -> 1 Hundred + 2 Tens. Total = 124!";
    } else if (regroupCase === 4) {
        container.innerHTML = `
            <div class="p-3 bg-slate-900 border border-slate-700 rounded-lg text-center font-mono">
                <span class="text-xs text-slate-400 block mb-1">Ungrouped</span>
                <span class="text-lg font-bold text-amber-300">35 Tens</span>
            </div>
            <div class="text-emerald-400 font-bold text-xl">➔</div>
            <div class="p-3 bg-emerald-950 border border-emerald-500 rounded-lg text-center font-mono">
                <span class="text-xs text-emerald-300 block mb-1">Regrouped</span>
                <span class="text-xl font-black text-emerald-200">350 (3H + 5T + 0O)</span>
            </div>
        `;
        if (exp) exp.textContent = "35 Tens: 30 Tens = 3 Hundreds (300). 5 Tens = 50. Total = 350!";
    } else {
        container.innerHTML = `
            <div class="p-3 bg-slate-900 border border-slate-700 rounded-lg text-center font-mono">
                <span class="text-xs text-slate-400 block mb-1">Ungrouped</span>
                <span class="text-lg font-bold text-amber-300">2H + 13T + 7O</span>
            </div>
            <div class="text-emerald-400 font-bold text-xl">➔</div>
            <div class="p-3 bg-emerald-950 border border-emerald-500 rounded-lg text-center font-mono">
                <span class="text-xs text-emerald-300 block mb-1">Regrouped</span>
                <span class="text-xl font-black text-emerald-200">337 (3H + 3T + 7O)</span>
            </div>
        `;
        if (exp) exp.textContent = "2 Hundreds + 13 Tens + 7 Ones: 13 Tens = 1 Hundred + 3 Tens. 2 Hundreds + 1 Hundred = 3 Hundreds. Total = 337!";
    }
}

// Sim 11: Color-Coded Token Model
let tokenNumberVal = 3019;

function setTokenNumber(val) {
    tokenNumberVal = val;
    renderTokenModel();
}

function renderTokenModel() {
    const wrap = document.getElementById('tokenModelSvgWrap');
    if (!wrap) return;

    const th = Math.floor(tokenNumberVal / 1000);
    const h = Math.floor((tokenNumberVal % 1000) / 100);
    const t = Math.floor((tokenNumberVal % 100) / 10);
    const o = tokenNumberVal % 10;

    const expStr = `${th * 1000} + ${h * 100} + ${t * 10} + ${o}`;
    let words = '';
    if (tokenNumberVal === 3019) words = 'Three thousand nineteen';
    else if (tokenNumberVal === 4508) words = 'Four thousand five hundred eight';
    else if (tokenNumberVal === 2008) words = 'Two thousand eight';
    else words = `${tokenNumberVal}`;

    document.getElementById('tokenExpandedDisplay').textContent = expStr;
    document.getElementById('tokenWordsDisplay').textContent = words;

    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Blue 1000 Tokens -->
            <g transform="translate(40, 20)">
                <text x="35" y="16" font-size="11" font-weight="bold" fill="#60a5fa" text-anchor="middle">1000 Tokens (${th})</text>
                ${Array.from({length: th}).map((_, i) => `<circle cx="${35}" cy="${40 + i * 26}" r="12" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/><text x="35" y="${44 + i * 26}" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">1k</text>`).join('')}
            </g>

            <!-- Red 100 Tokens -->
            <g transform="translate(130, 20)">
                <text x="35" y="16" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">100 Tokens (${h})</text>
                ${Array.from({length: h}).map((_, i) => `<circle cx="${35}" cy="${40 + i * 22}" r="10" fill="#dc2626" stroke="#991b1b" stroke-width="2"/><text x="35" y="${43 + i * 22}" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">100</text>`).join('')}
                ${h === 0 ? '<text x="35" y="60" font-size="11" fill="#64748b" text-anchor="middle">0 Tokens</text>' : ''}
            </g>

            <!-- Yellow 10 Tokens -->
            <g transform="translate(220, 20)">
                <text x="35" y="16" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">10 Tokens (${t})</text>
                ${Array.from({length: t}).map((_, i) => `<circle cx="${35}" cy="${40 + i * 22}" r="10" fill="#eab308" stroke="#854d0e" stroke-width="2"/><text x="35" y="${43 + i * 22}" font-size="8" font-weight="bold" fill="#713f12" text-anchor="middle">10</text>`).join('')}
                ${t === 0 ? '<text x="35" y="60" font-size="11" fill="#64748b" text-anchor="middle">0 Tokens</text>' : ''}
            </g>

            <!-- Green 1 Tokens -->
            <g transform="translate(310, 20)">
                <text x="45" y="16" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">1 Tokens (${o})</text>
                ${Array.from({length: o}).map((_, i) => {
                    const gx = 20 + (i % 3) * 22;
                    const gy = 40 + Math.floor(i / 3) * 22;
                    return `<circle cx="${gx}" cy="${gy}" r="9" fill="#10b981" stroke="#065f46" stroke-width="1.5"/><text x="${gx}" y="${gy + 3}" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>`;
                }).join('')}
            </g>
        </svg>
    `;
}

// Sim 12: Place Value Slider
let sliderTh = 1;
let sliderH = 8;
let sliderT = 9;
let sliderO = 5;

function applySliderOffset(place, amount) {
    if (place === 'ones') {
        sliderO = (sliderO + amount) % 10;
    } else if (place === 'tens') {
        sliderT += amount;
        if (sliderT >= 10) {
            sliderT -= 10;
            sliderH += 1;
            if (sliderH >= 10) {
                sliderH -= 10;
                sliderTh += 1;
            }
        }
    }
    updateSliderUI();
}

function togglePlaceholderTrap() {
    sliderTh = 7;
    sliderH = 0;
    sliderT = 2;
    sliderO = 4;
    updateSliderUI();
    const exp = document.getElementById('sliderExplanationText');
    if (exp) exp.textContent = "Misconception Alert! 7 Thousands 0 Hundreds 2 Tens 4 Ones is 7024 (NOT 724!). Zero must hold the Hundreds column.";
}

function stepSliderCol(col, d) {
    if (col === 'th') sliderTh = Math.max(0, Math.min(9, sliderTh + d));
    if (col === 'h') sliderH = Math.max(0, Math.min(9, sliderH + d));
    if (col === 't') sliderT = Math.max(0, Math.min(9, sliderT + d));
    if (col === 'o') sliderO = Math.max(0, Math.min(9, sliderO + d));
    updateSliderUI();
}

function updateSliderUI() {
    document.getElementById('slideThBox').textContent = sliderTh;
    document.getElementById('slideHBox').textContent = sliderH;
    document.getElementById('slideTBox').textContent = sliderT;
    document.getElementById('slideOBox').textContent = sliderO;
    const num = sliderTh * 1000 + sliderH * 100 + sliderT * 10 + sliderO;
    const exp = document.getElementById('sliderExplanationText');
    if (exp && sliderH !== 0) {
        exp.textContent = `Current Slider Number: ${num}. (${sliderTh} Thousands + ${sliderH} Hundreds + ${sliderT} Tens + ${sliderO} Ones).`;
    }
}

// Sim 13: 4-Digit Number Scale
let scaleRangeMode = 1;

function setScaleRange(mode) {
    scaleRangeMode = mode;
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`scaleBtn${i}`);
        if (btn) {
            btn.className = (i === mode) ? 'px-2 py-0.5 bg-teal-600 text-white font-bold text-xs rounded' : 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700';
        }
    }
    renderFourDigitScale();
}

function renderFourDigitScale() {
    const wrap = document.getElementById('fourDigitScaleSvgWrap');
    const exp = document.getElementById('scaleExplanationText');
    if (!wrap) return;

    const svgWidth = 420;
    const svgHeight = 200;
    let scaleContent = '';

    if (scaleRangeMode === 1) {
        if (exp) exp.textContent = "Scale 1000 to 1100: Divided into 10 intervals of 10. Midpoint sits at 1050.";
        scaleContent = `
            <line x1="40" y1="100" x2="380" y2="100" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
            ${[1000, 1020, 1040, 1050, 1060, 1080, 1100].map(v => {
                const x = 40 + ((v - 1000) / 100) * 340;
                return `
                    <line x1="${x}" y1="90" x2="${x}" y2="110" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="${x}" y="126" font-size="9" font-weight="bold" fill="#94a3b8" text-anchor="middle" font-mono>${v}</text>
                `;
            }).join('')}
            <circle cx="210" cy="100" r="8" fill="#14b8a6"/>
            <text x="210" y="80" font-size="11" font-weight="bold" fill="#2dd4bf" text-anchor="middle">Midpoint 1050</text>
        `;
    } else if (scaleRangeMode === 2) {
        if (exp) exp.textContent = "Scale 2000 to 2500: Divided into increments of 50. Midpoint sits at 2250.";
        scaleContent = `
            <line x1="40" y1="100" x2="380" y2="100" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
            ${[2000, 2100, 2200, 2250, 2300, 2400, 2500].map(v => {
                const x = 40 + ((v - 2000) / 500) * 340;
                return `
                    <line x1="${x}" y1="90" x2="${x}" y2="110" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="${x}" y="126" font-size="9" font-weight="bold" fill="#94a3b8" text-anchor="middle" font-mono>${v}</text>
                `;
            }).join('')}
            <circle cx="210" cy="100" r="8" fill="#14b8a6"/>
            <text x="210" y="80" font-size="11" font-weight="bold" fill="#2dd4bf" text-anchor="middle">Midpoint 2250</text>
        `;
    } else if (scaleRangeMode === 3) {
        if (exp) exp.textContent = "Scale 5500 to 5700: Midpoint sits at 5600.";
        scaleContent = `
            <line x1="40" y1="100" x2="380" y2="100" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
            ${[5500, 5550, 5600, 5650, 5700].map(v => {
                const x = 40 + ((v - 5500) / 200) * 340;
                return `
                    <line x1="${x}" y1="90" x2="${x}" y2="110" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="${x}" y="126" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle" font-mono>${v}</text>
                `;
            }).join('')}
        `;
    } else {
        if (exp) exp.textContent = "Range Filter: Highlighting numbers strictly between 2226 and 3226 (such as 2850).";
        scaleContent = `
            <line x1="40" y1="100" x2="380" y2="100" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
            <!-- Highlighted Range -->
            <line x1="100" y1="100" x2="300" y2="100" stroke="#14b8a6" stroke-width="6"/>
            <text x="100" y="126" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">2226</text>
            <text x="300" y="126" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">3226</text>
            <circle cx="210" cy="100" r="8" fill="#f59e0b"/>
            <text x="210" y="80" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">2850 (Inside Range)</text>
        `;
    }

    wrap.innerHTML = `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">${scaleContent}</svg>`;
}

// Sim 14: Overlapping Arrow Cards
let arrowCardMode = 'assembled';

function setArrowCardMode(mode) {
    arrowCardMode = mode;
    const b1 = document.getElementById('arrowAssembledBtn');
    const b2 = document.getElementById('arrowExpandedBtn');
    const txt = document.getElementById('arrowCardText');

    if (mode === 'assembled') {
        b1.className = 'px-2.5 py-1 bg-fuchsia-600 text-white font-bold text-xs rounded shadow';
        b2.className = 'px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700';
        if (txt) txt.textContent = "Assembled Arrow Cards: 3000 + 400 + 50 + 2 overlap to display the standard 4-digit numeral 3452!";
    } else {
        b2.className = 'px-2.5 py-1 bg-fuchsia-600 text-white font-bold text-xs rounded shadow';
        b1.className = 'px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700';
        if (txt) txt.textContent = "Disassembled (Expanded Form): Pulling the cards apart reveals 3000 + 400 + 50 + 2.";
    }

    renderArrowCards();
}

function renderArrowCards() {
    const wrap = document.getElementById('arrowCardSvgWrap');
    if (!wrap) return;

    const svgWidth = 420;
    const svgHeight = 200;

    let cardsSvg = '';
    if (arrowCardMode === 'assembled') {
        cardsSvg = `
            <g transform="translate(110, 65)">
                <!-- 3000 Base Card -->
                <path d="M 0 0 L 170 0 L 195 35 L 170 70 L 0 70 Z" fill="#6b21a8" stroke="#a855f7" stroke-width="2"/>
                <text x="30" y="46" font-size="34" font-weight="black" fill="#f3e8ff" font-mono>3</text>

                <!-- 400 Overlap -->
                <path d="M 50 0 L 170 0 L 195 35 L 170 70 L 50 70 Z" fill="#4338ca" stroke="#818cf8" stroke-width="2"/>
                <text x="75" y="46" font-size="34" font-weight="black" fill="#e0e7ff" font-mono>4</text>

                <!-- 50 Overlap -->
                <path d="M 95 0 L 170 0 L 195 35 L 170 70 L 95 70 Z" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                <text x="120" y="46" font-size="34" font-weight="black" fill="#e0f2fe" font-mono>5</text>

                <!-- 2 Overlap -->
                <path d="M 140 0 L 170 0 L 195 35 L 170 70 L 140 70 Z" fill="#047857" stroke="#34d399" stroke-width="2"/>
                <text x="155" y="46" font-size="34" font-weight="black" fill="#d1fae5" font-mono>2</text>
            </g>
        `;
    } else {
        cardsSvg = `
            <!-- Pull Apart View -->
            <g transform="translate(20, 20)">
                <path d="M 0 0 L 160 0 L 180 18 L 160 36 L 0 36 Z" fill="#6b21a8" stroke="#a855f7" stroke-width="1.5"/>
                <text x="80" y="24" font-size="18" font-weight="black" fill="#f3e8ff" font-mono text-anchor="middle">3000</text>
            </g>
            <text x="215" y="45" font-size="20" font-weight="bold" fill="#a855f7">+</text>
            <g transform="translate(240, 20)">
                <path d="M 0 0 L 120 0 L 140 18 L 120 36 L 0 36 Z" fill="#4338ca" stroke="#818cf8" stroke-width="1.5"/>
                <text x="60" y="24" font-size="18" font-weight="black" fill="#e0e7ff" font-mono text-anchor="middle">400</text>
            </g>

            <g transform="translate(60, 110)">
                <path d="M 0 0 L 90 0 L 110 18 L 90 36 L 0 36 Z" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="45" y="24" font-size="18" font-weight="black" fill="#e0f2fe" font-mono text-anchor="middle">50</text>
            </g>
            <text x="185" y="135" font-size="20" font-weight="bold" fill="#38bdf8">+</text>
            <g transform="translate(210, 110)">
                <path d="M 0 0 L 50 0 L 70 18 L 50 36 L 0 36 Z" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
                <text x="25" y="24" font-size="18" font-weight="black" fill="#d1fae5" font-mono text-anchor="middle">2</text>
            </g>
        `;
    }

    wrap.innerHTML = `<svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">${cardsSvg}</svg>`;
}

// Sim 15: Comparing Place Values
let comparePairId = 1;

function comparePair(id) {
    comparePairId = id;
    for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`cmpPair${i}Btn`);
        if (btn) {
            btn.className = (i === id) ? 'px-2 py-0.5 bg-cyan-600 text-white font-bold text-xs rounded' : 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700';
        }
    }
    renderComparison();
}

function renderComparison() {
    const wrap = document.getElementById('compareBalanceSvgWrap');
    const exp = document.getElementById('compareExplanationText');
    if (!wrap) return;

    let v1 = 1213, v2 = 2121, op = '<';
    if (comparePairId === 2) { v1 = 1300; v2 = 2300; op = '<'; }
    if (comparePairId === 3) { v1 = 3425; v2 = 3452; op = '<'; }

    if (exp) {
        if (comparePairId === 1) exp.textContent = `Comparing 1213 vs 2121: Compare Thousands column first: 1 Thousand < 2 Thousands. Thus, 1213 < 2121!`;
        if (comparePairId === 2) exp.textContent = `Comparing 1300 vs 2300: 1 Thousand in September < 2 Thousands in October. Thus, 1300 < 2300!`;
        if (comparePairId === 3) exp.textContent = `Comparing 3425 vs 3452: Thousands match (3=3), Hundreds match (4=4). In Tens column: 2 Tens < 5 Tens. Thus, 3425 < 3452!`;
    }

    const svgWidth = 420;
    const svgHeight = 200;

    wrap.innerHTML = `
        <svg viewBox="0 0 ${svgWidth} ${svgHeight}" class="w-full h-full max-h-[200px]">
            <!-- Card 1 -->
            <g transform="translate(60, 50)">
                <rect width="110" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <text x="55" y="44" font-size="24" font-weight="black" fill="#f8fafc" text-anchor="middle" font-mono>${v1}</text>
            </g>

            <!-- Operator Symbol -->
            <g transform="translate(210, 85)">
                <circle cx="0" cy="0" r="22" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                <text x="0" y="9" font-size="28" font-weight="black" fill="#f59e0b" text-anchor="middle">${op}</text>
            </g>

            <!-- Card 2 -->
            <g transform="translate(250, 50)">
                <rect width="110" height="70" rx="8" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
                <text x="55" y="44" font-size="24" font-weight="black" fill="#ffffff" text-anchor="middle" font-mono>${v2}</text>
            </g>
        </svg>
    `;
}

// Sim 16: Ordering Real-World Records
let orderTheme = 'mountains';

function loadOrderingTheme(th) {
    orderTheme = th;
    const b1 = document.getElementById('themeMtnBtn');
    const b2 = document.getElementById('themePricesBtn');
    const b3 = document.getElementById('themeCricketBtn');
    const sum = document.getElementById('orderingSummaryText');

    [b1, b2, b3].forEach(b => {
        if (b) b.className = 'px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700';
    });

    if (th === 'mountains' && b1) b1.className = 'px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded';
    if (th === 'prices' && b2) b2.className = 'px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded';
    if (th === 'cricket' && b3) b3.className = 'px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded';

    const container = document.getElementById('orderingRecordsContainer');
    if (!container) return;

    if (th === 'mountains') {
        if (sum) sum.textContent = "Himalayan Peaks in Decreasing Order: Kangchenjunga (8586 m) > Nanda Devi (7816 m) > Chaukhamba (7138 m).";
        container.innerHTML = `
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">1. Kangchenjunga (Highest)</span>
                <span class="font-mono font-black text-emerald-400 text-sm">8,586 m</span>
            </div>
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">2. Nanda Devi</span>
                <span class="font-mono font-black text-cyan-400 text-sm">7,816 m</span>
            </div>
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">3. Chaukhamba I</span>
                <span class="font-mono font-black text-amber-400 text-sm">7,138 m</span>
            </div>
        `;
    } else if (th === 'prices') {
        if (sum) sum.textContent = "Appliance Prices in Increasing Order: ₹1099 < ₹1899 < ₹1986.";
        container.innerHTML = `
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">1. Toaster (Cheapest)</span>
                <span class="font-mono font-black text-emerald-400 text-sm">₹1,099</span>
            </div>
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">2. Mixer Grinder</span>
                <span class="font-mono font-black text-cyan-400 text-sm">₹1,899</span>
            </div>
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">3. Microwave Oven</span>
                <span class="font-mono font-black text-amber-400 text-sm">₹1,986</span>
            </div>
        `;
    } else {
        if (sum) sum.textContent = "Career ODI Cricket Runs: Legendary Batter (7805 runs) > International Star (5114 runs). Difference = 2691 runs!";
        container.innerHTML = `
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">1. Legendary Captain</span>
                <span class="font-mono font-black text-emerald-400 text-sm">7,805 Runs</span>
            </div>
            <div class="p-2.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-between">
                <span class="font-bold text-slate-200 text-xs">2. International Star</span>
                <span class="font-mono font-black text-cyan-400 text-sm">5,114 Runs</span>
            </div>
        `;
    }
}

// Master Dispatcher for Simulator Initialization
function initSlideSim(slideId) {
    if (slideId === 1) renderPantryInventory();
    if (slideId === 2) renderAttendanceTracker();
    if (slideId === 3) presetDigitChallenge('largest');
    if (slideId === 4) renderNumberLine();
    if (slideId === 5) renderIndianSystem();
    if (slideId === 6) renderThresholdCounter();
    if (slideId === 7) renderHeritageFact();
    if (slideId === 8) renderBaseTenBlocks();
    if (slideId === 9) renderOrangeSlice();
    if (slideId === 10) renderRegrouping();
    if (slideId === 11) renderTokenModel();
    if (slideId === 12) updateSliderUI();
    if (slideId === 13) renderFourDigitScale();
    if (slideId === 14) renderArrowCards();
    if (slideId === 15) renderComparison();
    if (slideId === 16) loadOrderingTheme('mountains');
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


// ============================================================================
// State Management & Audio Setup
// ============================================================================
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;

// Audio SFX Synthesizer
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSuccessSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2);
        
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        
        osc.start(now);
        osc.stop(now + 0.35);
    } catch(e) {}
}

function playErrorSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(146.83, now + 0.2);
        
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        
        osc.start(now);
        osc.stop(now + 0.25);
    } catch(e) {}
}

function playClickSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.05);
        
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.06);
        
        osc.start(now);
        osc.stop(now + 0.06);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Voice Engine
// ============================================================================
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    const femaleTerms = ['female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera', 'kavya'];
    const malePreferred = ['microsoft prabhat', 'rishi', 'microsoft ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'google uk english male', 'microsoft david', 'microsoft mark', 'alex'];
    
    for (const pref of malePreferred) {
        const found = voices.find(v => {
            const name = v.name.toLowerCase();
            const lang = v.lang.toLowerCase();
            const isFemale = femaleTerms.some(f => name.includes(f));
            return !isFemale && (name.includes(pref) || (lang.includes('en-in') && name.includes(pref)));
        });
        if (found) return found;
    }
    
    const anyIndian = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;
    
    const fallback = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.startsWith('en');
    });
    return fallback || voices[0];
}

function playAudioLecture() {
    if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
    }
    
    if (isSpeaking) {
        stopAudioLecture();
        return;
    }
    
    const slide = SLIDES.find(s => s.id === currentSlide);
    if (!slide || !slide.speech || slide.speech.trim() === '') {
        return;
    }
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(slide.speech);
    currentUtterance.pitch = 0.85;
    currentUtterance.rate = 0.94;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
    keepAliveTimer = setInterval(() => {
        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        } else {
            clearInterval(keepAliveTimer);
        }
    }, 10000);
    
    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
    };
    
    currentUtterance.onend = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    currentUtterance.onerror = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    window.speechSynthesis.speak(currentUtterance);
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    clearInterval(keepAliveTimer);
    isSpeaking = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (playing) {
        btn.classList.add('bg-rose-600', 'text-white', 'animate-pulse');
        btn.classList.remove('bg-indigo-600');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clip-rule="evenodd"></path></svg>
            Stop Audio
        `;
    } else {
        btn.classList.remove('bg-rose-600', 'animate-pulse');
        btn.classList.add('bg-indigo-600', 'text-white');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            Audio Lecture
        `;
    }
}

// ============================================================================
// Slide Navigation & Terminal Slide Invariant
// ============================================================================
function showSlide(num) {
    if (num < 1 || num > totalSlides) return;
    stopAudioLecture();
    
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));
    
    const target = document.getElementById(`slide-${num}`);
    if (target) {
        target.classList.remove('hidden');
    }
    
    currentSlide = num;
    const curNumEl = document.getElementById('currentSlideNum');
    if (curNumEl) curNumEl.innerText = currentSlide;
    
    const progressPct = (currentSlide / totalSlides) * 100;
    const pbar = document.getElementById('chapterProgressBar');
    if (pbar) pbar.style.width = `${progressPct}%`;
    
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = true;
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = false;
        }
    }
    
    // Terminal Slide Invariant (Strict Rule for Slide 20)
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    // Audio button visibility for non-speech slides (slides 17 to 20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        playClickSfx();
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        playClickSfx();
        showSlide(currentSlide - 1);
    }
}

// ============================================================================
// Checkpoint Validation
// ============================================================================
function checkCheckpoint(slideId, cpIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;
    
    const cp = slide.checkpoints[cpIdx];
    const fb = document.getElementById(`cp-fb-${slideId}-${cpIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${cpIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = cp.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${cp.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${cp.exp}`;
    }
}

// ============================================================================
// Quiz Validation & Solution Modals
// ============================================================================
function checkQuiz(slideId, qIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const fb = document.getElementById(`qz-fb-${slideId}-${qIdx}`);
    const solBtn = document.getElementById(`qz-sol-btn-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.qz-btn-${slideId}-${qIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = qz.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${qz.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${qz.exp}`;
    }
    
    if (solBtn) {
        solBtn.classList.remove('hidden');
    }
}

function openSolutionModal(slideId, qIdx) {
    playClickSfx();
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const modal = document.getElementById('solutionModal');
    const modalContent = document.getElementById('solutionModalContent');
    if (!modal || !modalContent) return;
    
    modalContent.innerHTML = `
        <div class="mb-4">
            <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Question ${qIdx + 1}</span>
            <h4 class="text-base font-bold text-white mt-1 leading-snug">${qz.q}</h4>
        </div>
        ${qz.sol}
    `;
    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    playClickSfx();
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// ============================================================================
// Interactive Simulator Logic for Chapter 11
// ============================================================================

// --- Slide 1: Ink Blot Studio ---
let currentInkColor = '#ec4899';
let inkDrops = [];

function setInkColor(c) {
    playClickSfx();
    currentInkColor = c;
    document.querySelectorAll('.ink-c-btn').forEach(btn => {
        btn.classList.remove('ring-2', 'ring-white');
    });
    event.currentTarget.classList.add('ring-2', 'ring-white');
}

function addInkDrop(e) {
    playClickSfx();
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    inkDrops.push({ x, y, color: currentInkColor });
    renderInkDrops();
}

function renderInkDrops() {
    const leftContainer = document.getElementById('ink-left-drops');
    const rightContainer = document.getElementById('ink-right-drops');
    if (!leftContainer || !rightContainer) return;
    
    leftContainer.innerHTML = '';
    rightContainer.innerHTML = '';
    
    const halfWidth = 144; // Half of 288px width
    
    inkDrops.forEach(d => {
        // Left drop
        const dotLeft = document.createElement('div');
        dotLeft.className = 'absolute rounded-full shadow-lg';
        dotLeft.style.width = '14px';
        dotLeft.style.height = '14px';
        dotLeft.style.backgroundColor = d.color;
        dotLeft.style.left = `${d.x - 7}px`;
        dotLeft.style.top = `${d.y - 7}px`;
        leftContainer.appendChild(dotLeft);
        
        // Mirrored right drop
        const mirroredX = halfWidth - d.x; // symmetrical from fold line
        const dotRight = document.createElement('div');
        dotRight.className = 'absolute rounded-full shadow-lg';
        dotRight.style.width = '14px';
        dotRight.style.height = '14px';
        dotRight.style.backgroundColor = d.color;
        dotRight.style.left = `${mirroredX - 7}px`;
        dotRight.style.top = `${d.y - 7}px`;
        rightContainer.appendChild(dotRight);
    });
}

function foldAndPressInk() {
    if (inkDrops.length === 0) return;
    playSuccessSfx();
    const rightHalf = document.getElementById('ink-right-drops');
    const status = document.getElementById('ink-status');
    if (rightHalf) {
        rightHalf.classList.remove('opacity-0');
        rightHalf.classList.add('opacity-100');
    }
    if (status) {
        status.innerHTML = `<span class="text-pink-400 font-bold">Paper unfolded! Identical mirror drops stamped across the fold line of symmetry!</span>`;
    }
}

function clearInkBlot() {
    playClickSfx();
    inkDrops = [];
    renderInkDrops();
    const rightHalf = document.getElementById('ink-right-drops');
    const status = document.getElementById('ink-status');
    if (rightHalf) {
        rightHalf.classList.remove('opacity-100');
        rightHalf.classList.add('opacity-0');
    }
    if (status) {
        status.innerText = 'Click anywhere on the left half to deposit wet ink drops, then press Fold & Press.';
    }
}

// --- Slide 2: Paper Airplane Aerodynamics ---
let gliderMode = 'symmetric';

function setPlaneMode(mode) {
    playClickSfx();
    gliderMode = mode;
    const symBtn = document.getElementById('plane-sym-btn');
    const asymBtn = document.getElementById('plane-asym-btn');
    const modeLabel = document.getElementById('glider-mode-label');
    const telemetry = document.getElementById('flight-telemetry');
    const plane = document.getElementById('plane-avatar');
    
    if (plane) {
        plane.style.left = '8px';
        plane.style.transform = 'rotate(0deg)';
    }
    
    if (mode === 'symmetric') {
        if (symBtn) symBtn.className = 'px-3 py-1.5 rounded-xl bg-cyan-600 text-white font-bold transition';
        if (asymBtn) asymBtn.className = 'px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 transition';
        if (modeLabel) {
            modeLabel.className = 'text-emerald-400 font-bold';
            modeLabel.innerText = 'Mode: Balanced Symmetrical Glider';
        }
        if (telemetry) {
            telemetry.innerText = 'Lift Balance: Left Wing 100% | Right Wing 100% • Stable Linear Glide';
        }
    } else {
        if (asymBtn) asymBtn.className = 'px-3 py-1.5 rounded-xl bg-rose-600 text-white font-bold transition';
        if (symBtn) symBtn.className = 'px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 transition';
        if (modeLabel) {
            modeLabel.className = 'text-rose-400 font-bold';
            modeLabel.innerText = 'Mode: Asymmetrical Fold (Bent Wing)';
        }
        if (telemetry) {
            telemetry.innerText = 'Lift Balance: Left Wing 100% | Right Wing 45% • Unbalanced Air Drag & Tilt';
        }
    }
}

function launchGlider() {
    playClickSfx();
    const plane = document.getElementById('plane-avatar');
    const telemetry = document.getElementById('flight-telemetry');
    if (!plane) return;
    
    plane.style.left = '8px';
    plane.style.transform = 'rotate(0deg)';
    
    setTimeout(() => {
        if (gliderMode === 'symmetric') {
            plane.style.left = '85%';
            plane.style.transform = 'rotate(0deg)';
            playSuccessSfx();
            if (telemetry) telemetry.innerText = 'Perfect Flight! Symmetrical wings maintained level flight over 15 meters!';
        } else {
            plane.style.left = '50%';
            plane.style.transform = 'rotate(70deg) translateY(25px)';
            playErrorSfx();
            if (telemetry) telemetry.innerText = 'Crash! Asymmetrical wing drag caused spiral roll and stall!';
        }
    }, 100);
}

// --- Slide 3: Holes and Cuts Lab ---
const cutPresets = {
    corner_diamond: {
        folded: '<div class="w-6 h-6 bg-slate-950 absolute top-0 left-0 -translate-x-3 -translate-y-3 rotate-45 border border-amber-400"></div>',
        unfolded: '<div class="absolute inset-0 flex items-center justify-center"><div class="w-8 h-8 bg-slate-950 border-2 border-amber-400 rotate-45 shadow"></div></div>',
        count: '1 Centered Diamond Window (Rhombus)'
    },
    edge_circle: {
        folded: '<div class="w-3.5 h-3.5 bg-slate-950 rounded-full border border-cyan-400 absolute right-1 top-6"></div>',
        unfolded: '<div class="absolute inset-0 flex items-center justify-between px-1"><div class="w-3 h-3 bg-slate-950 border border-cyan-400 rounded-full"></div><div class="w-3 h-3 bg-slate-950 border border-cyan-400 rounded-full"></div></div><div class="absolute inset-0 flex flex-col justify-between items-center py-1"><div class="w-3 h-3 bg-slate-950 border border-cyan-400 rounded-full"></div><div class="w-3 h-3 bg-slate-950 border border-cyan-400 rounded-full"></div></div>',
        count: '4 Symmetrical Circular Edge Holes'
    },
    side_triangle: {
        folded: '<div class="w-4 h-4 bg-slate-950 rotate-45 border-l border-b border-rose-400 absolute bottom-0 left-6 -translate-y-2"></div>',
        unfolded: '<div class="absolute inset-0 flex items-center justify-around"><div class="w-4 h-4 bg-slate-950 rotate-45 border border-rose-400"></div><div class="w-4 h-4 bg-slate-950 rotate-45 border border-rose-400"></div></div>',
        count: '2 Symmetrical Cutout Diamonds along Fold Line'
    }
};

function setPaperCut(type) {
    playClickSfx();
    document.querySelectorAll('.cut-btn').forEach(b => {
        b.className = 'cut-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'cut-btn px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold';
    
    const data = cutPresets[type];
    if (!data) return;
    
    const foldedEl = document.getElementById('folded-preview');
    const unfoldedEl = document.getElementById('unfolded-preview');
    const countEl = document.getElementById('unfolded-cut-count');
    
    if (foldedEl) foldedEl.innerHTML = data.folded;
    if (unfoldedEl) unfoldedEl.innerHTML = data.unfolded;
    if (countEl) countEl.innerText = data.count;
}

// --- Slide 4: Dot Grid Symmetry Canvas ---
const dotPresets = {
    butterfly: [[1, 2], [2, 1], [3, 0], [4, 1], [5, 2]],
    vase: [[1, 1], [2, 2], [3, 2], [4, 1], [5, 0]],
    arrow: [[1, 2], [2, 1], [3, 0], [3, 1], [5, 1]],
    tree: [[1, 2], [2, 1], [3, 2], [4, 0], [5, 2]]
};

let activeDotPreset = 'butterfly';

function loadDotPreset(p) {
    playClickSfx();
    activeDotPreset = p;
    document.querySelectorAll('.dot-btn').forEach(b => {
        b.className = 'dot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'dot-btn px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold';
    renderDotGrid();
}

function renderDotGrid() {
    const board = document.getElementById('dot-grid-board');
    if (!board) return;
    board.innerHTML = '';
    
    const points = dotPresets[activeDotPreset] || [];
    // 7x7 grid: cols 0..6, center mirror line at col 3
    for (let r = 0; r < 7; r++) {
        for (let c = 0; c < 7; c++) {
            const isLeftPt = points.some(pt => pt[0] === r && pt[1] === c);
            // Mirrored col = 6 - c
            const mirroredCol = 6 - c;
            const isRightPt = points.some(pt => pt[0] === r && pt[1] === (6 - c));
            const isCenterLine = (c === 3);
            
            const dot = document.createElement('div');
            if (isLeftPt) {
                dot.className = 'w-3.5 h-3.5 rounded-full bg-indigo-500 ring-2 ring-indigo-300 shadow';
            } else if (isRightPt && !isCenterLine) {
                dot.className = 'w-3.5 h-3.5 rounded-full bg-cyan-400 ring-2 ring-cyan-200 shadow';
            } else {
                dot.className = 'w-2 h-2 rounded-full bg-slate-700';
            }
            board.appendChild(dot);
        }
    }
}

// --- Slide 5: Border Shape Symmetry Tester ---
const borderShapes = {
    star: { icon: '⭐', lines: '5 Lines of Symmetry (Regular Star)', desc: 'Folds symmetrically through each apex vertex to the opposite notch.' },
    oval: { icon: '🥚', lines: '2 Lines of Symmetry (Horizontal & Vertical)', desc: 'Folds identically along its major and minor axes.' },
    heart: { icon: '❤️', lines: '1 Line of Symmetry (Vertical Midline)', desc: 'Left curved lobe superimposes exactly over right lobe.' },
    arrow: { icon: '➔', lines: '1 Line of Symmetry (Horizontal Midline)', desc: 'Top pointed half folds seamlessly onto bottom half.' },
    paisley: { icon: '🪶', lines: '0 Lines of Symmetry (Asymmetrical Motif)', desc: 'Curving tail breaks symmetry; no folding line matches both halves.' }
};

function testBorderShape(sh) {
    playClickSfx();
    document.querySelectorAll('.bsh-btn').forEach(b => {
        b.className = 'bsh-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'bsh-btn px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold';
    
    const data = borderShapes[sh];
    if (!data) return;
    
    const view = document.getElementById('border-shape-view');
    const info = document.getElementById('border-shape-analysis');
    if (view) view.innerText = data.icon;
    if (info) {
        info.innerHTML = `
            <div class="${sh === 'paisley' ? 'text-rose-400' : 'text-emerald-400'} font-bold">${data.lines}</div>
            <div class="text-slate-400 text-[11px]">${data.desc}</div>
        `;
    }
}

// --- Slide 6: Mirror Reflection Digit Lab ---
function setMirrorDigit(num) {
    playClickSfx();
    document.querySelectorAll('.mir-btn').forEach(b => {
        b.className = 'mir-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'mir-btn px-2.5 py-1 rounded-lg bg-purple-600 text-white font-bold';
    
    const dView = document.getElementById('direct-num-view');
    const rView = document.getElementById('reflected-num-view');
    const verdict = document.getElementById('mirror-verdict');
    
    if (dView) dView.innerText = num;
    if (rView) rView.innerText = num;
    
    if (verdict) {
        if (num === '181' || num === '808') {
            verdict.className = 'text-[10px] text-emerald-400 font-bold mt-1';
            verdict.innerText = 'Reflects Identically!';
        } else {
            verdict.className = 'text-[10px] text-rose-400 font-bold mt-1';
            verdict.innerText = 'Reversed & Inverted!';
        }
    }
}

// --- Slide 7: Ambulance Word Mirror ---
function setAmbulanceWord(w) {
    playClickSfx();
    document.querySelectorAll('.amb-btn').forEach(b => {
        b.className = 'amb-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'amb-btn px-2.5 py-1 rounded-lg bg-red-600 text-white font-bold';
    
    const hood = document.getElementById('amb-hood-text');
    const mir = document.getElementById('amb-mirror-text');
    if (hood) hood.innerText = w;
    if (mir) mir.innerText = w;
}

// --- Slide 8: Completing Symmetrical Drawings ---
const partialFigs = {
    butterfly: '🦋',
    teapot: '🫖',
    star: '⭐'
};

function setPartialFig(f) {
    playClickSfx();
    document.querySelectorAll('.pfig-btn').forEach(b => {
        b.className = 'pfig-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'pfig-btn px-2.5 py-1 rounded-lg bg-teal-600 text-white font-bold';
    
    const icon = partialFigs[f] || '🦋';
    const left = document.getElementById('pfig-left');
    const right = document.getElementById('pfig-right');
    if (left) left.innerText = icon;
    if (right) {
        right.innerText = icon;
        right.classList.add('opacity-20');
        right.classList.remove('opacity-100');
    }
}

function revealCompleteFigure() {
    playSuccessSfx();
    const right = document.getElementById('pfig-right');
    if (right) {
        right.classList.remove('opacity-20');
        right.classList.add('opacity-100');
    }
}

function resetPartialFigure() {
    playClickSfx();
    const right = document.getElementById('pfig-right');
    if (right) {
        right.classList.remove('opacity-100');
        right.classList.add('opacity-20');
    }
}

// --- Slide 9: Polygon Symmetry Line Explorer ---
const polyData = {
    eq_triangle: { icon: '🔺', title: 'Equilateral Triangle: 3 Lines of Symmetry', desc: '3 equal sides • 3 equal 60° angles • Lines bisect each vertex' },
    iso_triangle: { icon: '📐', title: 'Isosceles Triangle: 1 Line of Symmetry', desc: '2 equal sides • 1 line bisecting apex vertex to base midpoint' },
    sca_triangle: { icon: '⚠️', title: 'Scalene Triangle: 0 Lines of Symmetry', desc: 'All sides and angles unequal • Completely asymmetrical' },
    square: { icon: '⬛', title: 'Square: 4 Lines of Symmetry', desc: '2 side midpoint lines + 2 diagonal corner lines' },
    rectangle: { icon: '▭', title: 'Rectangle: 2 Lines of Symmetry', desc: '2 lines connecting opposite side midpoints (diagonals do not match)' },
    hexagon: { icon: '🛑', title: 'Regular Hexagon: 6 Lines of Symmetry', desc: '3 vertex-to-vertex diagonals + 3 opposite side midpoint lines' }
};

function setPolygonSymmetry(p) {
    playClickSfx();
    document.querySelectorAll('.poly-btn').forEach(b => {
        b.className = 'poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'poly-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold';
    
    const data = polyData[p];
    if (!data) return;
    
    const svgCont = document.getElementById('polygon-svg-container');
    const info = document.getElementById('polygon-info');
    if (svgCont) svgCont.innerHTML = `<span class="text-6xl">${data.icon}</span>`;
    if (info) {
        info.innerHTML = `
            <div class="text-blue-400 font-bold">${data.title}</div>
            <div class="text-slate-400 text-[11px]">${data.desc}</div>
        `;
    }
}

// --- Slide 10: Tessellation Angle Laboratory ---
const tessData = {
    square: { calc: '4 × 90° = 360°', verdict: 'Tessellates Seamlessly! No gaps or overlaps.', pass: true },
    triangle: { calc: '6 × 60° = 360°', verdict: 'Tessellates Seamlessly! 6 triangles meet at vertex.', pass: true },
    hexagon: { calc: '3 × 120° = 360°', verdict: 'Tessellates Seamlessly! Honeycomb pattern.', pass: true },
    pentagon: { calc: '3 × 108° = 324° (36° Gap!)', verdict: 'Fails to Tessellate Alone! Leaves gaps or overlaps.', pass: false }
};

function testTessellationShape(sh) {
    playClickSfx();
    document.querySelectorAll('.tess-btn').forEach(b => {
        b.className = 'tess-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'tess-btn px-2.5 py-1 rounded-lg bg-yellow-500 text-slate-950 font-bold';
    
    const data = tessData[sh];
    if (!data) return;
    
    const calcEl = document.getElementById('tess-calc');
    const verdEl = document.getElementById('tess-verdict');
    if (calcEl) calcEl.innerText = data.calc;
    if (verdEl) {
        verdEl.innerText = data.verdict;
        if (data.pass) {
            verdEl.className = 'text-xs text-emerald-400 font-bold bg-emerald-950/40 py-1 px-3 rounded-lg inline-block border border-emerald-800/60';
        } else {
            verdEl.className = 'text-xs text-rose-400 font-bold bg-rose-950/40 py-1 px-3 rounded-lg inline-block border border-rose-800/60';
        }
    }
}

// --- Slide 11: Tile Motion Transformations ---
let tileRot = 0;
let tileFlip = 1;
let tileShift = 0;

function applyTileMotion(mot) {
    playClickSfx();
    document.querySelectorAll('.mot-btn').forEach(b => {
        b.className = 'mot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'mot-btn px-2.5 py-1 rounded-lg bg-lime-600 text-white font-bold';
    
    const tile = document.getElementById('animated-tile');
    const exp = document.getElementById('mot-explanation');
    if (!tile) return;
    
    if (mot === 'slide') {
        tileShift = (tileShift === 0) ? 40 : 0;
        tile.style.transform = `translateX(${tileShift}px) rotate(${tileRot}deg) scaleX(${tileFlip})`;
        if (exp) exp.innerText = 'Slide (Translation): Shifts tile smoothly without turning or flipping.';
    } else if (mot === 'flip') {
        tileFlip = (tileFlip === 1) ? -1 : 1;
        tile.style.transform = `translateX(${tileShift}px) rotate(${tileRot}deg) scaleX(${tileFlip})`;
        if (exp) exp.innerText = 'Flip (Reflection): Turns tile over across an edge to create a mirror image.';
    } else if (mot === 'rotate') {
        tileRot += 90;
        tile.style.transform = `translateX(${tileShift}px) rotate(${tileRot}deg) scaleX(${tileFlip})`;
        if (exp) exp.innerText = `Rotate (Turn): Rotated by 90° clockwise (current angle: ${tileRot % 360}°).`;
    } else if (mot === 'orientation') {
        const isStanding = tile.classList.contains('w-12');
        if (isStanding) {
            tile.className = 'w-20 h-12 bg-lime-500/20 border-2 border-lime-400 rounded-lg flex items-center justify-center font-bold text-lime-300 text-sm shadow transition-all duration-500';
            if (exp) exp.innerText = 'Orientation: Sleeping (Horizontal rectangular brick).';
        } else {
            tile.className = 'w-12 h-20 bg-lime-500/20 border-2 border-lime-400 rounded-lg flex items-center justify-center font-bold text-lime-300 text-sm shadow transition-all duration-500';
            if (exp) exp.innerText = 'Orientation: Standing (Vertical upright rectangular brick).';
        }
    }
}

// --- Slide 13: Floor Pattern Designer ---
function setFloorPattern(pat) {
    playClickSfx();
    const btnStk = document.getElementById('fl-pat-stacked');
    const btnRun = document.getElementById('fl-pat-running');
    const btnHer = document.getElementById('fl-pat-herring');
    const canvas = document.getElementById('floor-canvas');
    const note = document.getElementById('floor-note');
    if (!canvas) return;
    
    if (btnStk) btnStk.className = 'fl-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300';
    if (btnRun) btnRun.className = 'fl-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300';
    if (btnHer) btnHer.className = 'fl-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300';
    
    if (pat === 'stacked') {
        if (btnStk) btnStk.className = 'fl-btn px-3 py-1.5 rounded-xl bg-orange-600 text-white font-bold';
        canvas.innerHTML = `
            <div class="grid grid-cols-4 gap-1 w-full text-center text-[10px] font-mono text-slate-400">
                <div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div>
                <div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div><div class="p-2 bg-slate-900 border border-slate-700">Tile</div>
            </div>
        `;
        if (note) note.innerText = 'Stacked Grid: Continuous straight 4-way grout lines. Simple, but susceptible to linear stress cracks.';
    } else if (pat === 'running') {
        if (btnRun) btnRun.className = 'fl-btn px-3 py-1.5 rounded-xl bg-orange-600 text-white font-bold';
        canvas.innerHTML = `
            <div class="space-y-1 w-full text-[10px] font-mono text-slate-400">
                <div class="flex gap-1 justify-center"><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div></div>
                <div class="flex gap-1 justify-center -translate-x-3"><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div><div class="w-14 p-1.5 bg-slate-900 border border-slate-700 text-center">Tile</div></div>
            </div>
        `;
        if (note) note.innerText = 'Running bond staggers vertical seams by 50%, distributing loads and preventing continuous crack propagation.';
    } else {
        if (btnHer) btnHer.className = 'fl-btn px-3 py-1.5 rounded-xl bg-orange-600 text-white font-bold';
        canvas.innerHTML = `
            <div class="flex justify-center items-center gap-1.5 text-[10px] font-mono text-slate-400">
                <div class="w-6 h-14 bg-slate-900 border border-slate-700 flex items-center justify-center font-bold">V</div>
                <div class="w-14 h-6 bg-slate-900 border border-slate-700 flex items-center justify-center font-bold">H</div>
                <div class="w-6 h-14 bg-slate-900 border border-slate-700 flex items-center justify-center font-bold">V</div>
                <div class="w-14 h-6 bg-slate-900 border border-slate-700 flex items-center justify-center font-bold">H</div>
            </div>
        `;
        if (note) note.innerText = 'Herringbone: Alternates vertical (standing) and horizontal (sleeping) bricks in interlocking zigzags.';
    }
}

// --- Slide 15: Nature Walk Symmetry ---
const natureData = {
    butterfly: { icon: '🦋', desc: '<span class="font-bold text-emerald-400">Bilateral Wing Symmetry:</span> Left and right wings exhibit identical contours and mirrored spot markings.' },
    peepal: { icon: '🍃', desc: '<span class="font-bold text-emerald-400">Botanical Midrib Symmetry:</span> Central leaf midrib divides blade into symmetrical halves with matching branching lateral veins.' },
    flower: { icon: '🌼', desc: '<span class="font-bold text-emerald-400">Radiant Radial Symmetry:</span> Identical flower petals radiate evenly from central core like spokes on a wagon wheel.' }
};

function setNatureSpecimen(s) {
    playClickSfx();
    document.querySelectorAll('.nat-btn').forEach(b => {
        b.className = 'nat-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
    });
    event.currentTarget.className = 'nat-btn px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold';
    
    const data = natureData[s];
    if (!data) return;
    
    const icon = document.getElementById('nature-icon');
    const desc = document.getElementById('nature-desc');
    if (icon) {
        icon.innerHTML = `${data.icon}<div id="nature-mirror-line" class="absolute top-0 bottom-0 left-1/2 w-0.5 bg-emerald-400 -translate-x-1/2 shadow-[0_0_8px_rgba(52,211,153,0.8)]"></div>`;
    }
    if (desc) desc.innerHTML = data.desc;
}

// --- Slide 16: Leaf Imprint Studio ---
let currentLeafColor = '#10b981';

function setLeafPaint(c) {
    playClickSfx();
    currentLeafColor = c;
    document.querySelectorAll('.leaf-c-btn').forEach(b => {
        b.classList.remove('ring-2', 'ring-white');
    });
    event.currentTarget.classList.add('ring-2', 'ring-white');
}

function stampLeafImprint() {
    playSuccessSfx();
    const right = document.getElementById('leaf-canvas-right');
    const status = document.getElementById('leaf-studio-status');
    if (right) {
        right.classList.remove('opacity-0');
        right.classList.add('opacity-100');
    }
    if (status) {
        status.innerHTML = `<span class="text-teal-400 font-bold">Paper unfolded! Bilateral botanical imprint successfully created across the central fold!</span>`;
    }
}

function clearLeafImprint() {
    playClickSfx();
    const right = document.getElementById('leaf-canvas-right');
    const status = document.getElementById('leaf-studio-status');
    if (right) {
        right.classList.remove('opacity-100');
        right.classList.add('opacity-0');
    }
    if (status) {
        status.innerText = 'Choose paint color and press Stamp & Fold Imprint to generate a bilateral botanical print.';
    }
}

// ============================================================================
// Initialization
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ') {
            nextSlide();
        } else if (e.key === 'ArrowLeft') {
            prevSlide();
        } else if (e.key === 'Escape') {
            closeSolutionModal();
        }
    });
    
    // Init speech synthesis voices
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            window.speechSynthesis.getVoices();
        };
    }
    
    // Initialize active simulators
    renderDotGrid();
    setPaperCut('corner_diamond');
    testBorderShape('star');
    setMirrorDigit('181');
    setAmbulanceWord('AMBULANCE');
    setPartialFig('butterfly');
    setPolygonSymmetry('eq_triangle');
    testTessellationShape('square');
    setFloorPattern('running');
    setNatureSpecimen('butterfly');
    
    showSlide(1);
});

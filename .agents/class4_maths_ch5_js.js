
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
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1); // E5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2); // G5
        
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
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        
        osc.start(now);
        osc.stop(now + 0.08);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Narration Engine
// ============================================================================
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    const femaleTerms = ['female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera', 'kavya'];
    const malePreferred = ['microsoft prabhat', 'rishi', 'microsoft ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'google uk english male', 'microsoft david', 'microsoft mark', 'alex'];
    
    // 1. Look for prioritized Indian Male voices
    for (const pref of malePreferred) {
        const found = voices.find(v => {
            const name = v.name.toLowerCase();
            const lang = v.lang.toLowerCase();
            const isFemale = femaleTerms.some(f => name.includes(f));
            return !isFemale && (name.includes(pref) || (lang.includes('en-in') && name.includes(pref)));
        });
        if (found) return found;
    }
    
    // 2. Any Indian English non-female voice
    const anyIndian = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;
    
    // 3. Any English non-female fallback
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
    if (!slide || currentSlide > 16) {
        alert('Classroom lecture is only available on Slides 1 to 16.');
        return;
    }
    
    const lectureText = slide.speech || slide.lecture;
    if (!lectureText) return;
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(lectureText);
    currentUtterance.rate = 0.94;
    currentUtterance.pitch = 0.85;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
    // Chrome keep-alive watchdog
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

function updateAudioButtonUI(speaking) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (speaking) {
        btn.innerHTML = `
            <svg class="w-4 h-4 text-rose-400 animate-pulse" fill="currentColor" viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>
            <span class="text-xs font-bold text-rose-300">Stop Lecture</span>
        `;
        btn.classList.add('border-rose-500/50', 'bg-rose-500/10');
    } else {
        btn.innerHTML = `
            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span class="text-xs font-bold text-emerald-300">Listen Teacher Lecture</span>
        `;
        btn.classList.remove('border-rose-500/50', 'bg-rose-500/10');
    }
}

// Preload voices
if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
    };
}

// ============================================================================
// Slide Navigation & Terminal Slide Invariant
// ============================================================================
function showSlide(num) {
    if (num < 1 || num > totalSlides) return;
    stopAudioLecture();
    
    // Hide all slides
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));
    
    // Show current slide
    const target = document.getElementById(`slide-${num}`);
    if (target) {
        target.classList.remove('hidden');
    }
    
    currentSlide = num;
    document.getElementById('currentSlideNum').innerText = currentSlide;
    
    // Progress bar
    const progressPct = ((currentSlide) / totalSlides) * 100;
    const pbar = document.getElementById('chapterProgressBar');
    if (pbar) pbar.style.width = `${progressPct}%`;
    
    // Previous button state
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
    
    // Initialize slide-specific simulators if needed
    initSlideSimulator(currentSlide);
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
    
    const correctIdx = (cp.ans !== undefined) ? cp.ans : cp.answer;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        btns[optIdx].classList.remove('bg-emerald-600/30');
        btns[optIdx].classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        fb.innerHTML = `
            <div class="p-2.5 rounded-xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex items-start gap-2">
                <span>✅</span> <span><strong>Correct!</strong> ${cp.exp || cp.explanation}</span>
            </div>
        `;
    } else {
        playErrorSfx();
        btns[optIdx].classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        fb.innerHTML = `
            <div class="p-2.5 rounded-xl bg-rose-500/15 border border-rose-500/40 text-rose-300 text-xs font-semibold flex items-start gap-2">
                <span>❌</span> <span><strong>Try Again!</strong> ${cp.exp || cp.explanation}</span>
            </div>
        `;
    }
    fb.classList.remove('hidden');
}

// ============================================================================
// Mastery Quiz & Pop-up Solution Modal
// ============================================================================
function selectQuizOption(qId, optIdx) {
    let qData = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const found = s.quiz.find(item => item.id === qId);
            if (found) {
                qData = found;
                break;
            }
        }
    }
    if (!qData) return;
    
    const fb = document.getElementById(`quiz-fb-${qId}`);
    const btns = document.querySelectorAll(`.quiz-opt-btn-${qId}`);
    if (!fb || !btns) return;
    
    const correctIdx = (qData.ans !== undefined) ? qData.ans : qData.answer;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        btns[optIdx].classList.remove('bg-emerald-600/30');
        btns[optIdx].classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex flex-col gap-2">
                <div class="flex items-center justify-between">
                    <span>✅ Correct! ${qData.exp || ''}</span>
                    <button onclick="openSolutionModal(${qId})" class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-[11px] transition shadow">View Solution</button>
                </div>
            </div>
        `;
    } else {
        playErrorSfx();
        btns[optIdx].classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        fb.innerHTML = `
            <div class="p-3 rounded-xl bg-rose-500/15 border border-rose-500/40 text-rose-300 text-xs font-semibold flex flex-col gap-2">
                <div class="flex items-center justify-between">
                    <span>❌ Not quite! ${qData.exp || ''}</span>
                    <button onclick="openSolutionModal(${qId})" class="px-2.5 py-1 rounded bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-[11px] transition shadow">View Solution</button>
                </div>
            </div>
        `;
    }
    fb.classList.remove('hidden');
}

function openSolutionModal(qId) {
    let qData = null;
    for (const s of SLIDES) {
        if (s.quiz) {
            const found = s.quiz.find(item => item.id === qId);
            if (found) {
                qData = found;
                break;
            }
        }
    }
    if (!qData) return;
    
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionModalTitle');
    const content = document.getElementById('solutionModalContent');
    if (!modal || !title || !content) return;
    
    title.innerHTML = `<span>💡</span> Question ${qId} Detailed Solution`;
    content.innerHTML = `
        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm font-semibold text-slate-200">
            ${qData.q}
        </div>
        <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300 font-medium">
            <strong>Hint:</strong> ${qData.hint || 'Carefully analyze the problem constraints.'}
        </div>
        <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Step-by-Step Derivation</h4>
            ${qData.sol || makeDefaultSol(qData)}
        </div>
    `;
    modal.classList.remove('hidden');
    playClickSfx();
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
    playClickSfx();
}

function makeDefaultSol(qData) {
    const correctIdx = (qData.ans !== undefined) ? qData.ans : qData.answer;
    const correctOpt = qData.options[correctIdx];
    return `
        <ol class="space-y-1.5 list-none pl-0">
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> Understand the question requirements and note given values.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> Apply the appropriate fraction relationship or division rule.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> Confirm that the correct answer is <strong>${correctOpt}</strong>.</li>
        </ol>
    `;
}

// ============================================================================
// Interactive Simulator Handlers (Simulators 1 to 16)
// ============================================================================

// Simulator 1: Halves vs Quarters
function setPaperCompare(mode) {
    playClickSfx();
    const halfGroup = document.getElementById('paperHalfGroup');
    const quartersGroup = document.getElementById('paperQuartersGroup');
    const overlayGroup = document.getElementById('paperOverlayGroup');
    const desc = document.getElementById('paperCompareDesc');
    
    const btnHalf = document.getElementById('btn-comp-half');
    const btnQuarters = document.getElementById('btn-comp-two-quarters');
    const btnOverlay = document.getElementById('btn-comp-overlay');
    
    [btnHalf, btnQuarters, btnOverlay].forEach(b => {
        if (b) {
            b.classList.remove('bg-amber-500', 'text-slate-950');
            b.classList.add('bg-slate-800', 'text-slate-300');
        }
    });
    
    halfGroup.classList.add('hidden');
    quartersGroup.classList.add('hidden');
    overlayGroup.classList.add('hidden');
    
    if (mode === 'half') {
        halfGroup.classList.remove('hidden');
        btnHalf.classList.add('bg-amber-500', 'text-slate-950');
        desc.innerText = "One half (1/2) covers 50% of the rectangular sheet.";
    } else if (mode === 'two-quarters') {
        quartersGroup.classList.remove('hidden');
        btnQuarters.classList.add('bg-amber-500', 'text-slate-950');
        desc.innerText = "Two quarters (1/4 + 1/4 = 2/4) cover exactly 50% of the sheet.";
    } else {
        overlayGroup.classList.remove('hidden');
        btnOverlay.classList.add('bg-amber-500', 'text-slate-950');
        desc.innerText = "Direct Overlay: 2 quarters fit perfectly inside 1 half. Both are identical in area!";
    }
}

// Simulator 2: Fraction Anatomy
function setFractionAnatomy(n) {
    playClickSfx();
    [2, 3, 4, 5].forEach(d => {
        const btn = document.getElementById(`btn-anat-${d}`);
        if (btn) {
            btn.classList.remove('bg-indigo-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });
    const activeBtn = document.getElementById(`btn-anat-${n}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
        activeBtn.classList.add('bg-indigo-600', 'text-white');
    }
    
    document.getElementById('anatDenominatorText').innerText = n;
    document.getElementById('anatDenomLabel').innerText = n;
    
    const container = document.getElementById('anatStripContainer');
    container.innerHTML = '';
    
    const colors = ['bg-amber-500', 'bg-slate-800', 'bg-slate-800', 'bg-slate-800', 'bg-slate-800'];
    for (let i = 0; i < n; i++) {
        const part = document.createElement('div');
        part.className = `flex-1 ${i === 0 ? 'bg-amber-500/80 text-slate-950' : 'bg-slate-800/80 text-slate-400'} border-r border-slate-700 last:border-r-0 flex items-center justify-center font-bold text-xs transition`;
        part.innerText = `1/${n}`;
        container.appendChild(part);
    }
    
    const names = { 2: "Halves", 3: "Thirds", 4: "Quarters", 5: "Fifths" };
    document.getElementById('anatExplanation').innerText = `1 out of ${n} equal parts is shaded, written as 1/${n} (${names[n]}).`;
}

// Simulator 3: Origami Paper Folding
function setPaperFold(type) {
    playClickSfx();
    ['vertical', 'horizontal', 'diagonal', 'quarters'].forEach(t => {
        const btn = document.getElementById(`btn-fold-${t}`);
        if (btn) {
            btn.classList.remove('bg-emerald-500', 'text-slate-950');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });
    const active = document.getElementById(`btn-fold-${type}`);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-emerald-500', 'text-slate-950');
    }
    
    const group = document.getElementById('foldDisplayGroup');
    const desc = document.getElementById('foldDesc');
    
    if (type === 'vertical') {
        group.innerHTML = `
            <rect x="20" y="20" width="150" height="140" rx="6" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
            <line x1="170" y1="20" x2="170" y2="160" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 5"/>
            <text x="95" y="95" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">1/2 Shaded</text>
            <text x="245" y="95" fill="#94a3b8" font-size="14" font-weight="bold" text-anchor="middle">1/2 Plain</text>
        `;
        desc.innerText = "Vertical midline crease splits the rectangle into two identical tall halves.";
    } else if (type === 'horizontal') {
        group.innerHTML = `
            <rect x="20" y="20" width="300" height="70" rx="6" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
            <line x1="20" y1="90" x2="320" y2="90" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 5"/>
            <text x="170" y="60" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">1/2 Shaded</text>
            <text x="170" y="130" fill="#94a3b8" font-size="14" font-weight="bold" text-anchor="middle">1/2 Plain</text>
        `;
        desc.innerText = "Horizontal midline crease splits the rectangle into two wide horizontal halves.";
    } else if (type === 'diagonal') {
        group.innerHTML = `
            <polygon points="20,20 320,20 320,160" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
            <line x1="20" y1="20" x2="320" y2="160" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 5"/>
            <text x="230" y="65" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">1/2 Triangle</text>
            <text x="110" y="125" fill="#94a3b8" font-size="13" font-weight="bold" text-anchor="middle">1/2 Triangle</text>
        `;
        desc.innerText = "Diagonal fold across corners creates two congruent right-angled triangles of equal area.";
    } else {
        group.innerHTML = `
            <rect x="20" y="20" width="150" height="70" fill="#10b981" fill-opacity="0.4" stroke="#10b981" stroke-width="1.5"/>
            <line x1="170" y1="20" x2="170" y2="160" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
            <line x1="20" y1="90" x2="320" y2="90" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
            <text x="95" y="60" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">1/4 Shaded</text>
            <text x="245" y="60" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
            <text x="95" y="130" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
            <text x="245" y="130" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
        `;
        desc.innerText = "Folding both horizontally and vertically forms a grid of 4 equal quarters (1/4 each).";
    }
}

// Simulator 4: Steamed Dhokla Sharing
let currentDhoklaGuests = 2;
function changeDhoklaGuests(n) {
    playClickSfx();
    currentDhoklaGuests = n;
    document.getElementById('dhoklaGuestCount').innerText = n;
    
    const tray = document.getElementById('dhoklaTray');
    tray.innerHTML = '';
    
    for (let i = 0; i < n; i++) {
        const piece = document.createElement('div');
        piece.className = 'flex-1 h-full bg-amber-400 rounded-lg flex flex-col items-center justify-center font-bold text-slate-950 border border-amber-300 shadow-sm transition hover:scale-[1.02]';
        piece.innerHTML = `<span class="text-xs">Guest ${i+1}</span><span class="text-xs font-black text-amber-900">1/${n}</span>`;
        tray.appendChild(piece);
    }
    
    document.getElementById('dhoklaStatus').innerHTML = `
        Shared equally among ${n} guests. Each guest receives exactly <span class="text-amber-400 font-bold">1/${n}</span> of the platter.
    `;
}

function passDhoklaShare() {
    playClickSfx();
    currentDhoklaGuests = 5;
    document.getElementById('dhoklaGuestCount').innerText = 5;
    
    const tray = document.getElementById('dhoklaTray');
    tray.innerHTML = '';
    
    // 5 pieces, but piece 1 has 2/5 (received share from guest 5)
    for (let i = 0; i < 4; i++) {
        const piece = document.createElement('div');
        if (i === 0) {
            piece.className = 'flex-[2] h-full bg-indigo-500 rounded-lg flex flex-col items-center justify-center font-bold text-white border-2 border-indigo-400 shadow-md';
            piece.innerHTML = `<span class="text-xs">Host</span><span class="text-sm font-black text-amber-300">2/5 Share</span>`;
        } else {
            piece.className = 'flex-1 h-full bg-amber-400 rounded-lg flex flex-col items-center justify-center font-bold text-slate-950 border border-amber-300 shadow-sm';
            piece.innerHTML = `<span class="text-xs">Guest ${i+1}</span><span class="text-xs font-black text-amber-900">1/5</span>`;
        }
        tray.appendChild(piece);
    }
    
    document.getElementById('dhoklaStatus').innerHTML = `
        Guest 5 passed their share to the Host: 1/5 + 1/5 = <span class="text-indigo-400 font-bold">2/5 of the whole dhokla!</span>
    `;
}

// Simulator 5: Inverse Sharing Law
function updateDenomSlider(val) {
    const n = parseInt(val);
    document.getElementById('denomSliderVal').innerText = n;
    
    const pct = (100 / n).toFixed(1);
    document.getElementById('denomFractionText').innerText = `1/${n} (${pct}%)`;
    document.getElementById('denomProgressBar').style.width = `${pct}%`;
    
    // Draw pie slice in SVG
    const svg = document.getElementById('denomCircleSvg');
    const angle = 360 / n;
    const rad = (angle - 90) * (Math.PI / 180);
    const x = 60 + 50 * Math.cos(rad);
    const y = 60 + 50 * Math.sin(rad);
    const largeArc = angle > 180 ? 1 : 0;
    
    svg.innerHTML = `
        <circle cx="60" cy="60" r="50" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        <path d="M 60 60 L 60 10 A 50 50 0 ${largeArc} 1 ${x} ${y} Z" fill="#f43f5e" stroke="#fda4af" stroke-width="1.5"/>
        <circle cx="60" cy="60" r="3" fill="#ffffff"/>
    `;
}

// Simulator 6: 5-Bed Flower Garden
const gardenBeds = [false, false, false, false, false];
const flowerEmojis = ['🌹', '🌼', '🌸', '🌻', '🌺'];
const flowerNames = ['Rose', 'Mogra', 'Lily', 'Marigold', 'Jasmine'];
const flowerColors = ['bg-rose-500/30 text-rose-300 border-rose-500', 'bg-amber-400/30 text-amber-200 border-amber-400', 'bg-pink-400/30 text-pink-200 border-pink-400', 'bg-orange-500/30 text-orange-200 border-orange-500', 'bg-purple-500/30 text-purple-200 border-purple-500'];

function toggleGardenBed(idx) {
    playClickSfx();
    gardenBeds[idx] = !gardenBeds[idx];
    
    const plot = document.getElementById(`garden-plot-${idx}`);
    const btn = document.getElementById(`bed-btn-${idx}`);
    
    if (gardenBeds[idx]) {
        plot.className = `rounded-xl border-2 flex flex-col items-center justify-center text-xs font-bold transition shadow ${flowerColors[idx]}`;
        plot.innerHTML = `<span class="text-xl">${flowerEmojis[idx]}</span><span>${flowerNames[idx]}</span><span class="text-[10px]">1/5</span>`;
        if (btn) btn.classList.add('bg-pink-600', 'text-white');
    } else {
        plot.className = `rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition`;
        plot.innerHTML = `Bed ${idx+1}<span class="text-[10px]">1/5</span>`;
        if (btn) btn.classList.remove('bg-pink-600', 'text-white');
    }
    
    const count = gardenBeds.filter(Boolean).length;
    const disp = document.getElementById('gardenFractionDisplay');
    if (count === 5) {
        disp.innerText = `5/5 (1 Complete Whole Garden!)`;
        disp.className = "text-emerald-400 text-sm font-black";
        playSuccessSfx();
    } else if (count === 0) {
        disp.innerText = `0/5 (Empty)`;
        disp.className = "text-slate-400 text-sm font-bold";
    } else {
        disp.innerText = `${count}/5 Cultivated`;
        disp.className = "text-pink-400 text-sm font-bold";
    }
}

// Simulator 7: 7-Strip Flower Garden
function updateSeventhGarden() {
    const roses = parseInt(document.getElementById('sliderRoses').value);
    const sun = parseInt(document.getElementById('sliderSun').value);
    const lav = parseInt(document.getElementById('sliderLav').value);
    
    document.getElementById('stripValRoses').innerText = `${roses}/7`;
    document.getElementById('stripValSun').innerText = `${sun}/7`;
    document.getElementById('stripValLav').innerText = `${lav}/7`;
    
    const container = document.getElementById('seventhStripsContainer');
    container.innerHTML = '';
    
    const total = roses + sun + lav;
    
    for (let i = 0; i < 7; i++) {
        const strip = document.createElement('div');
        strip.className = 'flex-1 h-full border-r border-slate-700 last:border-r-0 flex items-center justify-center text-[10px] font-bold transition';
        
        if (i < roses) {
            strip.className += ' bg-rose-500 text-white';
            strip.innerText = '🌹';
        } else if (i < roses + sun) {
            strip.className += ' bg-amber-500 text-slate-950';
            strip.innerText = '🌻';
        } else if (i < total) {
            strip.className += ' bg-indigo-500 text-white';
            strip.innerText = '🪻';
        } else {
            strip.className += ' bg-slate-800 text-slate-500';
            strip.innerText = '1/7';
        }
        container.appendChild(strip);
    }
    
    const textEl = document.getElementById('seventhSumText');
    if (total === 7) {
        textEl.innerHTML = `${roses}/7 (Roses) + ${sun}/7 (Sunflowers) + ${lav}/7 (Lavender) = <span class="text-teal-400 font-black">7/7 (1 Whole Garden!)</span>`;
    } else {
        textEl.innerHTML = `${roses}/7 + ${sun}/7 + ${lav}/7 = <span class="text-amber-400 font-black">${total}/7</span> (Difference: ${Math.abs(7 - total)} strips)`;
    }
}

// Simulator 8: Dream Dosa Designer
function setDosaMode(slices) {
    playClickSfx();
    const btn3 = document.getElementById('btn-dosa-3');
    const btn8 = document.getElementById('btn-dosa-8');
    
    if (slices === 3) {
        btn3.className = "px-3 py-1 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow";
        btn8.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        renderDosa3();
    } else {
        btn8.className = "px-3 py-1 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow";
        btn3.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        renderDosa8();
    }
}

function renderDosa3() {
    const svg = document.getElementById('dosaSvg');
    svg.innerHTML = `
        <circle cx="80" cy="80" r="70" fill="#fef3c7" stroke="#d97706" stroke-width="4"/>
        <!-- 2/3 Onion (0 to 240 deg) -->
        <path d="M 80 80 L 80 10 A 70 70 0 1 1 19.38 115 Z" fill="#f97316" fill-opacity="0.55" stroke="#ea580c" stroke-width="2"/>
        <!-- 1/3 Potato (240 to 360 deg) -->
        <path d="M 80 80 L 19.38 115 A 70 70 0 0 1 80 10 Z" fill="#eab308" fill-opacity="0.55" stroke="#ca8a04" stroke-width="2"/>
        <line x1="80" y1="80" x2="80" y2="10" stroke="#78350f" stroke-width="2"/>
        <line x1="80" y1="80" x2="19.38" y2="115" stroke="#78350f" stroke-width="2"/>
        <circle cx="80" cy="80" r="5" fill="#78350f"/>
    `;
    document.getElementById('dosaLegend').innerHTML = `
        <div class="flex items-center gap-2"><span class="w-3.5 h-3.5 rounded-full bg-orange-500"></span> <span><strong>2/3:</strong> Spicy Onion Masala</span></div>
        <div class="flex items-center gap-2"><span class="w-3.5 h-3.5 rounded-full bg-yellow-500"></span> <span><strong>1/3:</strong> Classic Potato Mash</span></div>
        <div class="pt-1 text-slate-400 font-semibold text-[11px]">2/3 + 1/3 = 3/3 (1 Whole Dosa)</div>
    `;
}

function renderDosa8() {
    const svg = document.getElementById('dosaSvg');
    svg.innerHTML = `
        <circle cx="80" cy="80" r="70" fill="#fef3c7" stroke="#d97706" stroke-width="4"/>
        <!-- 3/8 Paneer (0 to 135 deg) -->
        <path d="M 80 80 L 80 10 A 70 70 0 0 1 129.5 129.5 Z" fill="#06b6d4" fill-opacity="0.5" stroke="#0891b2" stroke-width="1.5"/>
        <!-- 1/8 Tomato (135 to 180 deg) -->
        <path d="M 80 80 L 129.5 129.5 A 70 70 0 0 1 80 150 Z" fill="#f43f5e" fill-opacity="0.55" stroke="#e11d48" stroke-width="1.5"/>
        <!-- 4/8 Cheese (180 to 360 deg) -->
        <path d="M 80 80 L 80 150 A 70 70 0 0 1 80 10 Z" fill="#eab308" fill-opacity="0.5" stroke="#ca8a04" stroke-width="1.5"/>
        <circle cx="80" cy="80" r="5" fill="#78350f"/>
    `;
    document.getElementById('dosaLegend').innerHTML = `
        <div class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-cyan-500"></span> <span><strong>3/8:</strong> Chilly Paneer</span></div>
        <div class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-rose-500"></span> <span><strong>1/8:</strong> Tangy Tomato</span></div>
        <div class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-yellow-500"></span> <span><strong>4/8 (1/2):</strong> Golden Cheese</span></div>
        <div class="pt-1 text-slate-400 font-semibold text-[11px]">3/8 + 1/8 + 4/8 = 8/8 (1 Whole Dosa)</div>
    `;
}

// Simulator 9: Fractions of Collections
function setCollectionMode(type) {
    playClickSfx();
    const btnLamps = document.getElementById('btn-col-lamps');
    const btnCookies = document.getElementById('btn-col-cookies');
    const cookieCtrls = document.getElementById('cookieSharerControls');
    
    if (type === 'lamps') {
        btnLamps.className = "px-3 py-1 rounded-xl bg-yellow-500 text-slate-950 font-bold text-xs shadow";
        btnCookies.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        cookieCtrls.classList.add('hidden');
        renderLamps();
    } else {
        btnCookies.className = "px-3 py-1 rounded-xl bg-yellow-500 text-slate-950 font-bold text-xs shadow";
        btnLamps.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        cookieCtrls.classList.remove('hidden');
        updateCookieShare(3);
    }
}

function renderLamps() {
    const c = document.getElementById('collectionItemsContainer');
    c.innerHTML = '';
    // 4 groups of 2 lamps
    for (let g = 0; g < 4; g++) {
        const grp = document.createElement('div');
        grp.className = `p-2 rounded-xl border ${g === 0 ? 'bg-amber-500/20 border-amber-500' : 'bg-slate-800/60 border-slate-700'} flex items-center gap-1.5`;
        grp.innerHTML = `<span class="text-xl">🪔</span><span class="text-xl">🪔</span>`;
        c.appendChild(grp);
    }
    document.getElementById('collectionExplanation').innerHTML = `
        8 oil lamps divided into 4 equal groups = <span class="text-yellow-400 font-bold">2 lamps per group (1/4)</span>.
    `;
}

function updateCookieShare(sharers) {
    playClickSfx();
    const c = document.getElementById('collectionItemsContainer');
    c.innerHTML = '';
    const cookiesPerSharer = 12 / sharers;
    
    for (let s = 0; s < sharers; s++) {
        const grp = document.createElement('div');
        grp.className = `p-1.5 rounded-xl border ${s === 0 ? 'bg-amber-500/20 border-amber-500' : 'bg-slate-800/60 border-slate-700'} flex flex-col items-center gap-1`;
        let cookiesHtml = '';
        for (let k = 0; k < cookiesPerSharer; k++) {
            cookiesHtml += `<span class="text-base">🍪</span>`;
        }
        grp.innerHTML = `<div class="flex gap-1">${cookiesHtml}</div><span class="text-[10px] text-amber-300 font-bold">Child ${s+1}</span>`;
        c.appendChild(grp);
    }
    
    document.getElementById('collectionExplanation').innerHTML = `
        12 cookies shared among ${sharers} children = <span class="text-yellow-400 font-bold">1/${sharers} of 12 = ${cookiesPerSharer} cookies each</span>.
    `;
}

// Simulator 10: Return Gifts Distribution
function setGiftMode(mode) {
    playClickSfx();
    const btnHb = document.getElementById('btn-gift-hairbands');
    const btnPots = document.getElementById('btn-gift-pots');
    const grid = document.getElementById('giftGridContainer');
    const summary = document.getElementById('giftSummaryText');
    
    grid.innerHTML = '';
    
    if (mode === 'hairbands') {
        btnHb.className = "px-3.5 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow";
        btnPots.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        grid.className = "grid grid-cols-6 gap-2 max-w-[340px]";
        
        // 18 items: 6 silver, 12 gold
        for (let i = 0; i < 18; i++) {
            const item = document.createElement('div');
            if (i < 6) {
                item.className = "w-10 h-10 rounded-lg bg-slate-300/30 border border-slate-300 flex items-center justify-center text-sm shadow";
                item.innerHTML = '✨';
            } else {
                item.className = "w-10 h-10 rounded-lg bg-amber-400/30 border border-amber-400 flex items-center justify-center text-sm shadow";
                item.innerHTML = '👑';
            }
            grid.appendChild(item);
        }
        summary.innerHTML = `
            <div>18 Hairbands Total: <span class="text-slate-300 font-bold">6 Silver (1/3)</span> and <span class="text-amber-400 font-bold">12 Golden (2/3)</span></div>
            <div class="text-[11px] text-slate-400">18 / 3 = 6 per third; 6 × 2 = 12 for two thirds.</div>
        `;
    } else {
        btnPots.className = "px-3.5 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow";
        btnHb.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        grid.className = "grid grid-cols-6 gap-2 max-w-[340px]";
        
        // 24 pots: 6 marigold (1/4), 12 roses (2/4), 6 unplanted (1/4)
        for (let i = 0; i < 24; i++) {
            const item = document.createElement('div');
            if (i < 6) {
                item.className = "w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-500 flex items-center justify-center text-sm";
                item.innerHTML = '🌻';
            } else if (i < 18) {
                item.className = "w-10 h-10 rounded-lg bg-rose-500/30 border border-rose-500 flex items-center justify-center text-sm";
                item.innerHTML = '🌹';
            } else {
                item.className = "w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-sm";
                item.innerHTML = '🏺';
            }
            grid.appendChild(item);
        }
        summary.innerHTML = `
            <div>24 Clay Pots Total: <span class="text-amber-400 font-bold">6 Marigold (1/4)</span>, <span class="text-rose-400 font-bold">12 Rose (2/4)</span>, and <span class="text-slate-400 font-bold">6 Unplanted (1/4)</span></div>
            <div class="text-[11px] text-slate-400">1/4 of 24 = 6 pots; 2/4 of 24 = 12 pots.</div>
        `;
    }
}

// Simulator 11: Everyday Fraction Scenarios
function setEverydayScenario(scen) {
    playClickSfx();
    const btnB = document.getElementById('btn-scen-barfi');
    const btnR = document.getElementById('btn-scen-ribbon');
    const boxB = document.getElementById('barfiContainer');
    const boxR = document.getElementById('ribbonContainer');
    const desc = document.getElementById('everydayDesc');
    
    if (scen === 'barfi') {
        btnB.className = "px-3.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow";
        btnR.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        boxB.classList.remove('hidden');
        boxR.classList.add('hidden');
        desc.innerText = "Dividing 16 barfis among 4 people gives 4 barfis per 1/4 share.";
        setBarfiShare(1);
    } else {
        btnR.className = "px-3.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow";
        btnB.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        boxB.classList.add('hidden');
        boxR.classList.remove('hidden');
        desc.innerText = "A 20 cm satin ribbon cut by 1/5 loses 4 cm, leaving 16 cm (4/5).";
    }
}

function setBarfiShare(shares) {
    playClickSfx();
    const grid = document.getElementById('barfiGrid');
    grid.innerHTML = '';
    const eatenCount = shares * 4;
    
    for (let i = 0; i < 16; i++) {
        const piece = document.createElement('div');
        if (i < eatenCount) {
            piece.className = "rounded-lg bg-amber-400/90 border border-amber-300 flex items-center justify-center font-bold text-[10px] text-slate-950 shadow";
            piece.innerText = "🍬";
        } else {
            piece.className = "rounded-lg bg-slate-900 border border-slate-800 flex items-center justify-center text-[10px] text-slate-700";
            piece.innerText = "·";
        }
        grid.appendChild(piece);
    }
    document.getElementById('everydayDesc').innerHTML = `
        ${shares}/4 of 16 barfis = <span class="text-cyan-400 font-bold">${eatenCount} barfis</span> eaten. (${16 - eatenCount} remaining).
    `;
}

// Simulator 12: Paper Folding Equivalence
function setEquivFamily(fam) {
    playClickSfx();
    const btnT = document.getElementById('btn-equiv-thirds');
    const btnH = document.getElementById('btn-equiv-halves');
    const container = document.getElementById('equivStripsContainer');
    const formula = document.getElementById('equivMathFormula');
    
    if (fam === 'thirds') {
        btnT.className = "px-3.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow";
        btnH.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        
        container.innerHTML = `
            <div class="space-y-1">
                <span class="text-[11px] font-bold text-slate-400">Step 1: Folded into 3 equal parts (1/3 shaded)</span>
                <div class="w-full flex h-8 rounded-lg overflow-hidden border border-slate-700">
                    <div class="w-1/3 bg-blue-500/80 flex items-center justify-center font-bold text-xs text-white">1/3</div>
                    <div class="w-1/3 bg-slate-800 flex items-center justify-center font-bold text-xs text-slate-400">1/3</div>
                    <div class="w-1/3 bg-slate-800 flex items-center justify-center font-bold text-xs text-slate-400">1/3</div>
                </div>
            </div>
            <div class="space-y-1">
                <span class="text-[11px] font-bold text-slate-400">Step 2: Folded in half again (2/6 shaded)</span>
                <div class="w-full flex h-8 rounded-lg overflow-hidden border border-slate-700">
                    <div class="w-1/6 bg-blue-500/80 border-r border-blue-400 flex items-center justify-center font-bold text-[10px] text-white">1/6</div>
                    <div class="w-1/6 bg-blue-500/80 flex items-center justify-center font-bold text-[10px] text-white">1/6</div>
                    <div class="w-1/6 bg-slate-800 border-r border-slate-700 flex items-center justify-center font-bold text-[10px] text-slate-500">1/6</div>
                    <div class="w-1/6 bg-slate-800 border-r border-slate-700 flex items-center justify-center font-bold text-[10px] text-slate-500">1/6</div>
                    <div class="w-1/6 bg-slate-800 border-r border-slate-700 flex items-center justify-center font-bold text-[10px] text-slate-500">1/6</div>
                    <div class="w-1/6 bg-slate-800 flex items-center justify-center font-bold text-[10px] text-slate-500">1/6</div>
                </div>
            </div>
        `;
        formula.innerText = "(1 × 2) / (3 × 2) = 2/6. The shaded area is identical!";
    } else {
        btnH.className = "px-3.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow";
        btnT.className = "px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700";
        
        container.innerHTML = `
            <div class="space-y-1">
                <span class="text-[11px] font-bold text-slate-400">1/2 Shaded</span>
                <div class="w-full flex h-6 rounded-lg overflow-hidden border border-slate-700">
                    <div class="w-1/2 bg-blue-500/80 flex items-center justify-center font-bold text-xs text-white">1/2</div>
                    <div class="w-1/2 bg-slate-800"></div>
                </div>
            </div>
            <div class="space-y-1">
                <span class="text-[11px] font-bold text-slate-400">2/4 Shaded</span>
                <div class="w-full flex h-6 rounded-lg overflow-hidden border border-slate-700">
                    <div class="w-1/4 bg-blue-500/80 border-r border-blue-400 flex items-center justify-center font-bold text-[10px] text-white">1/4</div>
                    <div class="w-1/4 bg-blue-500/80 flex items-center justify-center font-bold text-[10px] text-white">1/4</div>
                    <div class="w-1/4 bg-slate-800 border-r border-slate-700"></div>
                    <div class="w-1/4 bg-slate-800"></div>
                </div>
            </div>
            <div class="space-y-1">
                <span class="text-[11px] font-bold text-slate-400">4/8 Shaded</span>
                <div class="w-full flex h-6 rounded-lg overflow-hidden border border-slate-700">
                    <div class="w-1/8 bg-blue-500/80 border-r border-blue-400 flex items-center justify-center text-[9px] text-white">1/8</div>
                    <div class="w-1/8 bg-blue-500/80 border-r border-blue-400 flex items-center justify-center text-[9px] text-white">1/8</div>
                    <div class="w-1/8 bg-blue-500/80 border-r border-blue-400 flex items-center justify-center text-[9px] text-white">1/8</div>
                    <div class="w-1/8 bg-blue-500/80 flex items-center justify-center text-[9px] text-white">1/8</div>
                    <div class="w-1/2 bg-slate-800"></div>
                </div>
            </div>
        `;
        formula.innerText = "1/2 = 2/4 = 4/8. All represent the exact same 50% area!";
    }
}

// Simulator 13: Fraction Chart Wall
function alignFractionWall(ratio) {
    playClickSfx();
    const guide = document.getElementById('fractionWallGuide');
    const fb = document.getElementById('fractionWallFeedback');
    const leftPct = ratio * 100;
    guide.style.left = `${leftPct}%`;
    
    if (ratio === 0.5) {
        fb.innerHTML = `Aligned at <span class="text-rose-400 font-bold">1/2</span>: Matches <strong>2/4</strong>, <strong>3/6</strong>, and <strong>5/10</strong>!`;
    } else if (ratio === 0.333) {
        fb.innerHTML = `Aligned at <span class="text-rose-400 font-bold">1/3</span>: Matches exactly with <strong>2/6</strong>!`;
    } else if (ratio === 0.25) {
        fb.innerHTML = `Aligned at <span class="text-rose-400 font-bold">1/4</span>: Matches halfway through 1/2.`;
    } else {
        fb.innerHTML = `Aligned at <span class="text-rose-400 font-bold">1 Whole</span>: Exactly 2 halves, 3 thirds, 4 fourths, 6 sixths, 10 tenths!`;
    }
}

// Simulator 14: 12-Box Grid Shading
const grid12State = new Array(12).fill(false);
function initGrid12() {
    const c = document.getElementById('grid12Boxes');
    if (!c) return;
    c.innerHTML = '';
    for (let i = 0; i < 12; i++) {
        const box = document.createElement('button');
        box.id = `box12-${i}`;
        box.onclick = () => toggleGrid12Box(i);
        box.className = "rounded-lg border-2 border-slate-700 bg-slate-900 transition hover:border-amber-400 flex items-center justify-center font-bold text-xs";
        c.appendChild(box);
    }
    setGridShadingPreset(4);
}

function toggleGrid12Box(idx) {
    playClickSfx();
    grid12State[idx] = !grid12State[idx];
    updateGrid12UI();
}

function setGridShadingPreset(count) {
    playClickSfx();
    for (let i = 0; i < 12; i++) {
        grid12State[i] = (i < count);
    }
    updateGrid12UI();
}

function clearGridShading() {
    playClickSfx();
    grid12State.fill(false);
    updateGrid12UI();
}

function updateGrid12UI() {
    let shaded = 0;
    for (let i = 0; i < 12; i++) {
        const box = document.getElementById(`box12-${i}`);
        if (!box) continue;
        if (grid12State[i]) {
            shaded++;
            box.className = "rounded-lg border-2 border-amber-400 bg-amber-500/80 text-slate-950 font-bold text-xs flex items-center justify-center shadow";
            box.innerText = "✓";
        } else {
            box.className = "rounded-lg border-2 border-slate-700 bg-slate-900 text-slate-500 font-bold text-xs flex items-center justify-center hover:border-amber-400/50";
            box.innerText = "";
        }
    }
    
    document.getElementById('grid12Count').innerText = shaded;
    const status = document.getElementById('grid12Status');
    
    if (shaded === 4) {
        status.innerHTML = `<span class="text-emerald-400">4/12 = 1/3 (Valid Claim!)</span>`;
    } else if (shaded === 3) {
        status.innerHTML = `<span class="text-amber-400">3/12 = 1/4 (Not 1/3!)</span>`;
    } else if (shaded === 6) {
        status.innerHTML = `<span class="text-indigo-400">6/12 = 1/2 (Halfway!)</span>`;
    } else {
        status.innerHTML = `<span class="text-slate-300">${shaded}/12</span>`;
    }
}

// Simulator 15: Composite Rangoli Pattern
const rangoliState = new Array(16).fill(false);
function initRangoli() {
    const svg = document.getElementById('rangoliSvg');
    if (!svg) return;
    svg.innerHTML = '';
    
    // 4x4 grid split into 16 triangles (diagonals across each of the 4 big squares)
    // 4 quadrants: Top-Left, Top-Right, Bottom-Left, Bottom-Right.
    // Each has 4 triangles meeting at quadrant center.
    let triPoints = [
        // Quadrant 1 (TL, center 40, 40)
        "40,40 0,0 80,0", "40,40 80,0 80,80", "40,40 80,80 0,80", "40,40 0,80 0,0",
        // Quadrant 2 (TR, center 120, 40)
        "120,40 80,0 160,0", "120,40 160,0 160,80", "120,40 160,80 80,80", "120,40 80,80 80,0",
        // Quadrant 3 (BL, center 40, 120)
        "40,120 0,80 80,80", "40,120 80,80 80,160", "40,120 80,160 0,160", "40,120 0,160 0,80",
        // Quadrant 4 (BR, center 120, 120)
        "120,120 80,80 160,80", "120,120 160,80 160,160", "120,120 160,160 80,160", "120,120 80,160 80,80"
    ];
    
    triPoints.forEach((pts, idx) => {
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', pts);
        poly.setAttribute('id', `r-tri-${idx}`);
        poly.setAttribute('fill', '#1e293b');
        poly.setAttribute('stroke', '#64748b');
        poly.setAttribute('stroke-width', '1.5');
        poly.setAttribute('class', 'cursor-pointer hover:opacity-80 transition');
        poly.onclick = () => toggleRangoliTriangle(idx);
        svg.appendChild(poly);
    });
    
    setRangoliPreset('diamond');
}

function toggleRangoliTriangle(idx) {
    playClickSfx();
    rangoliState[idx] = !rangoliState[idx];
    updateRangoliUI();
}

function setRangoliPreset(preset) {
    playClickSfx();
    rangoliState.fill(false);
    if (preset === 'diamond') {
        // Inner facing triangles meeting at (80,80): indices 1, 2, 6, 7, 9, 8, 12, 15
        [1, 2, 6, 7, 8, 9, 12, 15].forEach(i => rangoliState[i] = true);
    } else if (preset === 'corners') {
        // 4 outer corner triangles: 0, 4, 10, 14
        [0, 4, 10, 14].forEach(i => rangoliState[i] = true);
    } else if (preset === 'cross') {
        [0, 1, 2, 4, 6, 7, 8, 9, 11, 12, 14, 15].forEach(i => rangoliState[i] = true);
    }
    updateRangoliUI();
}

function updateRangoliUI() {
    let count = 0;
    for (let i = 0; i < 16; i++) {
        const el = document.getElementById(`r-tri-${i}`);
        if (!el) continue;
        if (rangoliState[i]) {
            count++;
            el.setAttribute('fill', '#ec4899');
            el.setAttribute('stroke', '#fbcfe8');
        } else {
            el.setAttribute('fill', '#1e293b');
            el.setAttribute('stroke', '#64748b');
        }
    }
    
    const textEl = document.getElementById('rangoliFractionText');
    const frac = simplifyFraction(count, 16);
    textEl.innerHTML = `Shaded Triangles: <span class="text-pink-400 font-black">${count}</span> / 16 = <span class="text-amber-400 font-black">${frac}</span>`;
}

function simplifyFraction(num, den) {
    if (num === 0) return "0";
    if (num === den) return "1 Whole";
    const gcd = (a, b) => b ? gcd(b, a % b) : a;
    const g = gcd(num, den);
    return `${num / g}/${den / g}`;
}

// Simulator 16: 18-Cell Target Shading
let targetGoalCells = 12;
let targetGoalLabel = '2/3';
const grid18State = new Array(18).fill(false);

function initGrid18() {
    const c = document.getElementById('grid18Container');
    if (!c) return;
    c.innerHTML = '';
    for (let i = 0; i < 18; i++) {
        const cell = document.createElement('button');
        cell.id = `cell18-${i}`;
        cell.onclick = () => toggleGrid18Cell(i);
        cell.className = "rounded-lg border-2 border-slate-700 bg-slate-900 transition hover:border-teal-400 flex items-center justify-center font-bold text-xs";
        c.appendChild(cell);
    }
    setShadeGoal(12, '2/3');
}

function toggleGrid18Cell(idx) {
    playClickSfx();
    grid18State[idx] = !grid18State[idx];
    updateGrid18UI();
}

function setShadeGoal(target, label) {
    playClickSfx();
    targetGoalCells = target;
    targetGoalLabel = label;
    
    ['12', '6', '9'].forEach(g => {
        const btn = document.getElementById(`btn-goal-${g}`);
        if (btn) {
            btn.className = (parseInt(g) === target)
                ? "px-2.5 py-1 rounded bg-teal-600 text-white font-bold"
                : "px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold";
        }
    });
    
    updateGrid18UI();
}

function reset18Cells() {
    playClickSfx();
    grid18State.fill(false);
    updateGrid18UI();
}

function updateGrid18UI() {
    let shaded = 0;
    for (let i = 0; i < 18; i++) {
        const cell = document.getElementById(`cell18-${i}`);
        if (!cell) continue;
        if (grid18State[i]) {
            shaded++;
            cell.className = "rounded-lg border-2 border-teal-400 bg-teal-500/80 text-slate-950 font-bold text-xs flex items-center justify-center shadow";
            cell.innerText = "✓";
        } else {
            cell.className = "rounded-lg border-2 border-slate-700 bg-slate-900 text-slate-500 font-bold text-xs flex items-center justify-center hover:border-teal-400/50";
            cell.innerText = "";
        }
    }
    
    document.getElementById('grid18Count').innerText = shaded;
    const fb = document.getElementById('grid18Feedback');
    
    if (shaded === targetGoalCells) {
        fb.innerHTML = `🎉 <span class="text-emerald-400 font-black">Target Reached!</span> ${shaded}/18 equals ${targetGoalLabel}!`;
        playSuccessSfx();
    } else if (shaded > targetGoalCells) {
        fb.innerHTML = `⚠️ <span class="text-rose-400 font-bold">Too many!</span> Current: ${shaded}/18. (Target: ${targetGoalCells} for ${targetGoalLabel})`;
    } else {
        fb.innerHTML = `Current: <span class="text-teal-400 font-bold">${shaded}</span> / 18 cells shaded. (Target: ${targetGoalCells} cells for ${targetGoalLabel})`;
    }
}

// ============================================================================
// Simulator Dispatcher on Slide Load
// ============================================================================
function initSlideSimulator(slideNum) {
    if (slideNum === 1) setPaperCompare('half');
    if (slideNum === 2) setFractionAnatomy(2);
    if (slideNum === 3) setPaperFold('vertical');
    if (slideNum === 4) changeDhoklaGuests(2);
    if (slideNum === 5) updateDenomSlider(2);
    if (slideNum === 7) updateSeventhGarden();
    if (slideNum === 8) setDosaMode(3);
    if (slideNum === 9) setCollectionMode('lamps');
    if (slideNum === 10) setGiftMode('hairbands');
    if (slideNum === 11) setEverydayScenario('barfi');
    if (slideNum === 12) setEquivFamily('thirds');
    if (slideNum === 13) alignFractionWall(0.5);
    if (slideNum === 14) initGrid12();
    if (slideNum === 15) initRangoli();
    if (slideNum === 16) initGrid18();
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});

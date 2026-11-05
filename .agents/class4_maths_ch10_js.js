
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
// Interactive Simulator Logic for Chapter 10
// ============================================================================

// --- Slide 1: Nim Game (to 10) ---
let nimCurrentTotal = 0;
let nimPlayer = 1;

function updateNimUI() {
    const totalEl = document.getElementById('nim-total');
    const statusEl = document.getElementById('nim-status');
    if (totalEl) totalEl.innerText = nimCurrentTotal;
    
    for (let i = 0; i <= 10; i++) {
        const stepEl = document.getElementById(`nim-step-${i}`);
        if (stepEl) {
            if (i === nimCurrentTotal) {
                stepEl.className = 'py-1.5 rounded-lg bg-emerald-500 text-slate-950 font-bold border border-emerald-400 scale-105 transition';
            } else if (i < nimCurrentTotal) {
                stepEl.className = 'py-1.5 rounded-lg bg-emerald-950/40 text-emerald-400 border border-emerald-900/60';
            } else if (i === 10) {
                stepEl.className = 'py-1.5 rounded-lg bg-amber-500/20 text-amber-300 font-bold border border-amber-500/40';
            } else {
                stepEl.className = 'py-1.5 rounded-lg bg-slate-800/60 text-slate-400';
            }
        }
    }
    
    const btn1 = document.getElementById('nim-btn-1');
    const btn2 = document.getElementById('nim-btn-2');
    
    if (nimCurrentTotal >= 10) {
        if (btn1) btn1.disabled = true;
        if (btn2) btn2.disabled = true;
        if (statusEl) {
            statusEl.innerHTML = `<span class="font-bold text-amber-400 text-sm">Player ${nimPlayer} reached 10 and WINS!</span>`;
        }
        playSuccessSfx();
    } else {
        if (btn1) btn1.disabled = (nimCurrentTotal + 1 > 10);
        if (btn2) btn2.disabled = (nimCurrentTotal + 2 > 10);
        if (statusEl) {
            statusEl.innerHTML = `Turn: <span class="font-bold ${nimPlayer === 1 ? 'text-emerald-400' : 'text-cyan-400'}">Player ${nimPlayer}</span>. Choose to add 1 or 2.`;
        }
    }
}

function nimAdd(step) {
    if (nimCurrentTotal + step > 10) return;
    playClickSfx();
    nimCurrentTotal += step;
    if (nimCurrentTotal < 10) {
        nimPlayer = (nimPlayer === 1) ? 2 : 1;
    }
    updateNimUI();
}

function resetNim() {
    playClickSfx();
    nimCurrentTotal = 0;
    nimPlayer = 1;
    updateNimUI();
}

// --- Slide 2: Winning Position Analyzer ---
function inspectNimNode(nodeVal) {
    playClickSfx();
    document.querySelectorAll('.nim-node').forEach(n => {
        n.classList.remove('bg-cyan-500/20', 'border-cyan-500', 'text-cyan-300');
        n.classList.add('bg-slate-800', 'border-slate-700');
    });
    
    const active = document.getElementById(`nim-node-${nodeVal}`);
    if (active) {
        active.classList.remove('bg-slate-800', 'border-slate-700');
        active.classList.add('bg-cyan-500/20', 'border-cyan-500', 'text-cyan-300');
    }
    
    const exp = document.getElementById('nim-node-exp');
    if (!exp) return;
    
    if (nodeVal === 1) {
        exp.innerHTML = `<div class="font-bold text-white text-sm">Controlling Milestone 1:</div><div>As the first player, choosing <strong>1</strong> starts your winning sequence. Opponent can choose 2 (you reach 4 by adding 2) or 3 (you reach 4 by adding 1). Milestone 1 guarantees reaching 4!</div>`;
    } else if (nodeVal === 4) {
        exp.innerHTML = `<div class="font-bold text-white text-sm">Controlling Milestone 4:</div><div>From 4, opponent can say <strong>5</strong> (you add 2 to hit 7) or <strong>6</strong> (you add 1 to hit 7). Reaching 4 ensures you can always claim 7!</div>`;
    } else if (nodeVal === 7) {
        exp.innerHTML = `<div class="font-bold text-white text-sm">Controlling Milestone 7:</div><div>From 7, opponent can only choose <strong>8</strong> (add 1) or <strong>9</strong> (add 2). From 8, you add 2 to hit 10! From 9, you add 1 to hit 10! Milestone 7 secures instant victory!</div>`;
    } else if (nodeVal === 10) {
        exp.innerHTML = `<div class="font-bold text-white text-sm">Reaching Milestone 10:</div><div>Target milestone 10 is the ultimate victory line. The player who claims 10 wins the game according to Nim addition rules!</div>`;
    }
}

// --- Slide 3: 13x13 Addition Chart Explorer ---
let activeChartSum = 9;

function renderAdditionChart() {
    const grid = document.getElementById('addition-grid');
    if (!grid) return;
    grid.innerHTML = '';
    
    // Header row
    const corner = document.createElement('div');
    corner.className = 'p-1 rounded bg-slate-800 font-bold text-slate-400 text-[10px]';
    corner.innerText = '+';
    grid.appendChild(corner);
    
    for (let c = 0; c <= 6; c++) {
        const h = document.createElement('div');
        h.className = 'p-1 rounded bg-slate-800 font-bold text-cyan-400 text-[10px]';
        h.innerText = c;
        grid.appendChild(h);
    }
    
    // 7 rows (0 to 6)
    for (let r = 0; r <= 6; r++) {
        const rh = document.createElement('div');
        rh.className = 'p-1 rounded bg-slate-800 font-bold text-cyan-400 text-[10px]';
        rh.innerText = r;
        grid.appendChild(rh);
        
        for (let c = 0; c <= 6; c++) {
            const sum = r + c;
            const cell = document.createElement('div');
            const isMatch = (sum === activeChartSum);
            cell.className = `p-1 rounded transition text-[11px] ${
                isMatch ? 'bg-amber-500 text-slate-950 font-black scale-105' : 'bg-slate-900/80 text-slate-300'
            }`;
            cell.innerText = sum;
            cell.title = `${r} + ${c} = ${sum}`;
            cell.onclick = () => highlightChartSum(sum);
            grid.appendChild(cell);
        }
    }
}

function highlightChartSum(sum) {
    playClickSfx();
    activeChartSum = sum;
    renderAdditionChart();
    
    const badge = document.getElementById('chart-stat-badge');
    if (!badge) return;
    if (sum === -1) {
        badge.innerText = 'Click any cell or sum button above to inspect constant-sum diagonals.';
    } else {
        const count = sum <= 12 ? (sum + 1) : (25 - sum);
        badge.innerText = `Sum ${sum} appears across ${count} cells forming a slanted anti-diagonal!`;
    }
}

// --- Slide 4: 3x3 Window Frame Centroid ---
function setWindowCenter(c) {
    playClickSfx();
    document.querySelectorAll('.wc-btn').forEach(btn => {
        btn.classList.remove('bg-purple-600', 'text-white', 'font-bold');
        btn.classList.add('bg-slate-800', 'text-slate-300');
    });
    event.currentTarget.classList.add('bg-purple-600', 'text-white', 'font-bold');
    
    renderWindowFrame(c);
}

function renderWindowFrame(c) {
    const container = document.getElementById('window-frame-cells');
    if (!container) return;
    container.innerHTML = '';
    
    // 3x3 values centered on c:
    // row 1: c-2, c-1, c
    // row 2: c-1, c, c+1
    // row 3: c, c+1, c+2
    const matrix = [
        [c - 2, c - 1, c],
        [c - 1, c, c + 1],
        [c, c + 1, c + 2]
    ];
    
    for (let r = 0; r < 3; r++) {
        for (let col = 0; col < 3; col++) {
            const val = matrix[r][col];
            const isCenter = (r === 1 && col === 1);
            const cell = document.createElement('div');
            cell.className = `p-2.5 rounded-xl border font-bold text-sm transition ${
                isCenter ? 'bg-purple-600 border-purple-400 text-white shadow-lg scale-105' : 'bg-slate-800 border-slate-700 text-slate-200'
            }`;
            cell.innerText = val;
            container.appendChild(cell);
        }
    }
    
    const rowSumEl = document.getElementById('row-sum-val');
    const totalSumEl = document.getElementById('total-sum-val');
    if (rowSumEl) rowSumEl.innerText = `${c - 1} + ${c} + ${c + 1} = ${3 * c}`;
    if (totalSumEl) totalSumEl.innerText = `9 × ${c} = ${9 * c}`;
}

// --- Slide 5: Reverse-and-Add Palindrome Lab ---
function setReverseNum(num) {
    playClickSfx();
    document.querySelectorAll('.rev-btn').forEach(b => {
        b.classList.remove('bg-rose-600', 'text-white', 'font-bold');
        b.classList.add('bg-slate-800', 'text-slate-300');
    });
    event.currentTarget.classList.add('bg-rose-600', 'text-white', 'font-bold');
    
    const orig = num;
    const a = Math.floor(num / 10);
    const b = num % 10;
    const swap = b * 10 + a;
    const total = orig + swap;
    const digitSum = a + b;
    
    const origEl = document.getElementById('rev-orig');
    const swapEl = document.getElementById('rev-swap');
    const totalEl = document.getElementById('rev-total');
    const formulaEl = document.getElementById('rev-formula');
    const noteEl = document.getElementById('rev-palindrome-note');
    
    if (origEl) origEl.innerText = orig;
    if (swapEl) swapEl.innerText = swap;
    if (totalEl) totalEl.innerText = total;
    if (formulaEl) formulaEl.innerText = `11 × (${a} + ${b}) = 11 × ${digitSum} = ${total}`;
    
    const isPal = String(total) === String(total).split('').reverse().join('');
    if (noteEl) {
        noteEl.innerText = `${total} is an exact multiple of 11 (11 × ${digitSum})${isPal ? ' and a symmetric palindrome!' : '!'}`;
    }
}

// --- Slide 6: Wildlife Census Explorer ---
const wildlifeData = {
    elephants: [
        { state: 'Karnataka', count: '6,049' },
        { state: 'Assam', count: '5,719' },
        { state: 'Kerala', count: '3,054' },
        { state: 'Meghalaya', count: '1,754' }
    ],
    tigers: [
        { state: 'Madhya Pradesh', count: '785' },
        { state: 'Karnataka', count: '563' },
        { state: 'Uttarakhand', count: '560' },
        { state: 'Maharashtra', count: '444' }
    ],
    leopards: [
        { state: 'Madhya Pradesh', count: '3,907' },
        { state: 'Maharashtra', count: '1,985' },
        { state: 'Karnataka', count: '1,879' },
        { state: 'Tamil Nadu', count: '1,070' }
    ]
};

function setWildlifeSpecies(sp) {
    playClickSfx();
    document.querySelectorAll('.wl-tab').forEach(t => {
        t.classList.remove('bg-teal-500', 'text-slate-950', 'font-bold');
        t.classList.add('bg-slate-800', 'text-slate-300');
    });
    const active = document.getElementById(`wl-tab-${sp}`);
    if (active) active.classList.add('bg-teal-500', 'text-slate-950', 'font-bold');
    
    const cards = document.getElementById('wildlife-cards');
    if (!cards) return;
    cards.innerHTML = '';
    
    const items = wildlifeData[sp] || [];
    items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'bg-slate-950/70 p-2.5 rounded-xl border border-slate-800';
        card.innerHTML = `
            <div class="text-slate-400 text-[11px]">${item.state}</div>
            <div class="text-lg font-black text-teal-400 mt-1">${item.count}</div>
        `;
        cards.appendChild(card);
    });
    
    const summary = document.getElementById('wildlife-summary');
    if (summary) {
        if (sp === 'elephants') {
            summary.innerHTML = `Karnataka (6,049) + Kerala (3,054) = <span class="font-bold text-teal-400">9,103 wild elephants</span>`;
        } else if (sp === 'tigers') {
            summary.innerHTML = `Maharashtra (444) + Uttarakhand (560) + MP (785) = <span class="font-bold text-teal-400">1,789 Bengal tigers</span>`;
        } else {
            summary.innerHTML = `MP (3,907) + Maharashtra (1,985) = <span class="font-bold text-teal-400">5,892 Indian leopards</span>`;
        }
    }
}

// --- Slide 12: Bank Deposit Slip ---
const depositPresets = {
    2850: { c500: 5, c100: 3, c50: 1, c10: 0, total: '₹2,850' },
    1420: { c500: 2, c100: 4, c50: 0, c10: 2, total: '₹1,420' },
    3650: { c500: 7, c100: 1, c50: 1, c10: 0, total: '₹3,650' }
};

function setDepositPreset(amt) {
    playClickSfx();
    document.querySelectorAll('.dep-btn').forEach(b => {
        b.classList.remove('bg-green-600', 'text-white', 'font-bold');
        b.classList.add('bg-slate-800', 'text-slate-300');
    });
    event.currentTarget.classList.add('bg-green-600', 'text-white', 'font-bold');
    
    const data = depositPresets[amt];
    if (!data) return;
    
    const c500 = document.getElementById('dep-c500');
    const c100 = document.getElementById('dep-c100');
    const c50 = document.getElementById('dep-c50');
    const c10 = document.getElementById('dep-c10');
    
    const calc500 = document.getElementById('dep-calc500');
    const calc100 = document.getElementById('dep-calc100');
    const calc50 = document.getElementById('dep-calc50');
    const calc10 = document.getElementById('dep-calc10');
    
    const amt500 = document.getElementById('dep-amt500');
    const amt100 = document.getElementById('dep-amt100');
    const amt50 = document.getElementById('dep-amt50');
    const amt10 = document.getElementById('dep-amt10');
    const gTotal = document.getElementById('dep-grand-total');
    
    if (c500) c500.innerText = data.c500;
    if (c100) c100.innerText = data.c100;
    if (c50) c50.innerText = data.c50;
    if (c10) c10.innerText = data.c10;
    
    if (calc500) calc500.innerText = `${data.c500} × 500`;
    if (calc100) calc100.innerText = `${data.c100} × 100`;
    if (calc50) calc50.innerText = `${data.c50} × 50`;
    if (calc10) calc10.innerText = `${data.c10} × 10`;
    
    if (amt500) amt500.innerText = `₹${(data.c500 * 500).toLocaleString()}`;
    if (amt100) amt100.innerText = `₹${(data.c100 * 100).toLocaleString()}`;
    if (amt50) amt50.innerText = `₹${(data.c50 * 50).toLocaleString()}`;
    if (amt10) amt10.innerText = `₹${(data.c10 * 10).toLocaleString()}`;
    if (gTotal) gTotal.innerText = data.total;
}

// --- Slide 13: Four-Digit Column Algorithms ---
function setColMode(mode) {
    playClickSfx();
    const btnAdd = document.getElementById('col-mode-add');
    const btnSub = document.getElementById('col-mode-sub');
    const board = document.getElementById('col-board');
    if (!board) return;
    
    if (mode === 'add') {
        if (btnAdd) { btnAdd.className = 'col-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold'; }
        if (btnSub) { btnSub.className = 'col-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300'; }
        board.innerHTML = `
            <div class="grid grid-cols-5 gap-1 text-[11px] text-slate-400 border-b border-slate-800 pb-1 mb-1 font-semibold">
                <span></span><span>Th</span><span>H</span><span>T</span><span>O</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-xs text-amber-400 font-bold mb-1">
                <span>Carry:</span><span>1</span><span>1</span><span>1</span><span>-</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white">
                <span class="text-slate-400">Addend 1:</span><span>4</span><span>7</span><span>8</span><span>6</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white border-b border-slate-700 pb-1">
                <span class="text-slate-400">+ Addend 2:</span><span>3</span><span>8</span><span>4</span><span>7</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-base font-black text-indigo-400 pt-1">
                <span class="text-slate-400 text-xs">Sum:</span><span>8</span><span>6</span><span>3</span><span>3</span>
            </div>
        `;
    } else {
        if (btnSub) { btnSub.className = 'col-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold'; }
        if (btnAdd) { btnAdd.className = 'col-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300'; }
        board.innerHTML = `
            <div class="grid grid-cols-5 gap-1 text-[11px] text-slate-400 border-b border-slate-800 pb-1 mb-1 font-semibold">
                <span></span><span>Th</span><span>H</span><span>T</span><span>O</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-xs text-cyan-400 font-bold mb-1">
                <span>Borrow:</span><span>6</span><span>11</span><span>10</span><span>15</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white">
                <span class="text-slate-400">Minuend:</span><span>7</span><span>2</span><span>1</span><span>5</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white border-b border-slate-700 pb-1">
                <span class="text-slate-400">- Subtrahend:</span><span>3</span><span>6</span><span>4</span><span>8</span>
            </div>
            <div class="grid grid-cols-5 gap-1 text-base font-black text-emerald-400 pt-1">
                <span class="text-slate-400 text-xs">Difference:</span><span>3</span><span>5</span><span>6</span><span>7</span>
            </div>
        `;
    }
}

// --- Slide 14: Mental Math Compensation ---
function setCompensation(base, delta) {
    playClickSfx();
    document.querySelectorAll('.comp-btn').forEach(b => {
        b.classList.remove('bg-pink-600', 'text-white', 'font-bold');
        b.classList.add('bg-slate-800', 'text-slate-300');
    });
    event.currentTarget.classList.add('bg-pink-600', 'text-white', 'font-bold');
    
    const step1El = document.getElementById('comp-step1');
    const step2El = document.getElementById('comp-step2');
    const summaryEl = document.getElementById('comp-summary');
    
    if (delta === -99) {
        if (step1El) step1El.innerText = `${base} - 100 = ${base - 100}`;
        if (step2El) step2El.innerText = `${base - 100} + 1 = ${base - 99}`;
        if (summaryEl) summaryEl.innerText = `${base} - 99 = ${base - 99} (Subtract 100, add 1 back!)`;
    } else if (delta === 99) {
        if (step1El) step1El.innerText = `${base} + 100 = ${base + 100}`;
        if (step2El) step2El.innerText = `${base + 100} - 1 = ${base + 99}`;
        if (summaryEl) summaryEl.innerText = `${base} + 99 = ${base + 99} (Add 100, subtract 1!)`;
    } else if (delta === -999) {
        if (step1El) step1El.innerText = `${base} - 1,000 = ${base - 1000}`;
        if (step2El) step2El.innerText = `${base - 1000} + 1 = ${base - 999}`;
        if (summaryEl) summaryEl.innerText = `${base} - 999 = ${base - 999} (Subtract 1,000, add 1 back!)`;
    }
}

// --- Slide 15: Inequality Comparator ---
function setInequality(caseId) {
    playClickSfx();
    document.querySelectorAll('.ineq-btn').forEach(b => {
        b.classList.remove('bg-sky-600', 'text-white', 'font-bold');
        b.classList.add('bg-slate-800', 'text-slate-300');
    });
    event.currentTarget.classList.add('bg-sky-600', 'text-white', 'font-bold');
    
    const leftEl = document.getElementById('ineq-left');
    const symEl = document.getElementById('ineq-symbol');
    const rightEl = document.getElementById('ineq-right');
    const reasonEl = document.getElementById('ineq-reason');
    
    if (caseId === 1) {
        if (leftEl) leftEl.innerText = '2,450 + 320';
        if (symEl) symEl.innerText = '>';
        if (rightEl) rightEl.innerText = '2,450 + 310';
        if (reasonEl) reasonEl.innerText = 'Both expressions share common base 2,450. Since 320 > 310, the left side is strictly greater without performing addition!';
    } else if (caseId === 2) {
        if (leftEl) leftEl.innerText = '4,500 - 200';
        if (symEl) symEl.innerText = '>';
        if (rightEl) rightEl.innerText = '4,500 - 250';
        if (reasonEl) reasonEl.innerText = 'Both expressions start from 4,500. Subtracting a smaller amount (200 < 250) leaves a larger remainder behind!';
    } else if (caseId === 3) {
        if (leftEl) leftEl.innerText = '2,500 + 1,200';
        if (symEl) symEl.innerText = '=';
        if (rightEl) rightEl.innerText = '2,400 + 1,300';
        if (reasonEl) reasonEl.innerText = 'Transferring 100 from 2,500 to 1,200 creates 2,400 + 1,300. The sum remains invariant (both equal 3,700)!';
    }
}

// --- Slide 16: Neighbouring Square Parity Grid ---
const defaultParityGrid = [
    { num: 1, type: 'odd' },
    { num: 2, type: 'even' },
    { num: 3, type: 'odd' },
    { num: 4, type: 'even' },
    { num: 5, type: 'odd' },
    { num: 6, type: 'even' },
    { num: 7, type: 'odd' },
    { num: 8, type: 'even' },
    { num: 9, type: 'odd' }
];

function renderParityGrid(items) {
    const grid = document.getElementById('parity-grid');
    if (!grid) return;
    grid.innerHTML = '';
    
    items.forEach(item => {
        const cell = document.createElement('div');
        const isEven = (item.type === 'even');
        cell.className = `p-3 rounded-xl font-black text-lg border transition shadow ${
            isEven ? 'bg-cyan-500/20 border-cyan-500 text-cyan-300' : 'bg-amber-500/20 border-amber-500 text-amber-300'
        }`;
        cell.innerHTML = `<div>${item.num}</div><div class="text-[9px] uppercase tracking-wider font-semibold opacity-80">${item.type}</div>`;
        grid.appendChild(cell);
    });
}

function revealParityPattern() {
    playSuccessSfx();
    // Chessboard pattern: 5 odds at corners and center, 4 evens at edges
    const pattern = [
        { num: 1, type: 'odd' },  { num: 2, type: 'even' }, { num: 3, type: 'odd' },
        { num: 4, type: 'even' }, { num: 5, type: 'odd' },  { num: 6, type: 'even' },
        { num: 7, type: 'odd' },  { num: 8, type: 'even' }, { num: 9, type: 'odd' }
    ];
    renderParityGrid(pattern);
}

function resetParityGrid() {
    playClickSfx();
    renderParityGrid(defaultParityGrid);
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
    updateNimUI();
    renderAdditionChart();
    renderWindowFrame(10);
    setReverseNum(27);
    setWildlifeSpecies('elephants');
    setDepositPreset(2850);
    setColMode('add');
    setCompensation(546, -99);
    setInequality(1);
    resetParityGrid();
    
    showSlide(1);
});

# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Compiled JS Engine String
"""

JS_ENGINE = '''
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
    
    // Hide audio lecture button on challenge slides (17-20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.style.display = 'none';
        } else {
            audioBtn.style.display = 'flex';
        }
    }
    
    // Trigger any per-slide simulator setup
    initSimulatorForSlide(currentSlide);
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
// Interactive Checkpoint & Quiz Evaluation
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

function showSolutionModal(slideId, qIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalQuestionTitle');
    const content = document.getElementById('modalSolutionContent');
    
    if (modal && title && content) {
        playClickSfx();
        title.innerText = `Question ${qIdx + 1}: ${qz.q}`;
        content.innerHTML = qz.sol;
        modal.classList.remove('hidden');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

function toggleHint(slideId, qIdx) {
    const hintEl = document.getElementById(`qz-hint-${slideId}-${qIdx}`);
    if (hintEl) {
        playClickSfx();
        hintEl.classList.toggle('hidden');
    }
}


// ============================================================================
// SIMULATOR 1: Survey Question Evaluator
// ============================================================================
function selectSurveyQuestion(type) {
    playClickSfx();
    const btnOpen = document.getElementById('sq-btn-open');
    const btnSpec = document.getElementById('sq-btn-spec');
    const respBox = document.getElementById('sq-responses-box');
    const statusEl = document.getElementById('sq-data-status');
    const cardEl = document.getElementById('sq-analysis-card');
    
    if (type === 'open') {
        if (btnOpen) {
            btnOpen.classList.add('ring-2', 'ring-rose-500');
        }
        if (btnSpec) {
            btnSpec.classList.remove('ring-2', 'ring-emerald-500');
        }
        if (statusEl) {
            statusEl.innerText = 'Messy Multi-Option Data';
            statusEl.className = 'text-rose-400 font-medium';
        }
        if (respBox) {
            respBox.innerHTML = `
                <div class="p-2 rounded bg-slate-900 border border-rose-900/40 text-slate-300">
                    <span class="text-rose-400 font-bold">Child 1:</span> "I like Mathematics, Art, and playing Football in P.E."
                </div>
                <div class="p-2 rounded bg-slate-900 border border-rose-900/40 text-slate-300">
                    <span class="text-rose-400 font-bold">Child 2:</span> "Languages and The World Around Us are both fun."
                </div>
                <div class="p-2 rounded bg-slate-900 border border-rose-900/40 text-slate-300">
                    <span class="text-rose-400 font-bold">Child 3:</span> "Drawing in Arts and playing outdoor sports."
                </div>
            `;
        }
        if (cardEl) {
            cardEl.className = 'bg-rose-950/20 border border-rose-800/40 p-3 rounded-xl text-xs text-rose-300 leading-relaxed';
            cardEl.innerHTML = '<strong>Challenge:</strong> Multiple answers per respondent create overlapping categories that cannot be easily summed or graphed into simple frequencies.';
        }
    } else {
        if (btnSpec) {
            btnSpec.classList.add('ring-2', 'ring-emerald-500');
        }
        if (btnOpen) {
            btnOpen.classList.remove('ring-2', 'ring-rose-500');
        }
        if (statusEl) {
            statusEl.innerText = 'Clean Single-Choice Data';
            statusEl.className = 'text-emerald-400 font-medium';
        }
        if (respBox) {
            respBox.innerHTML = `
                <div class="p-2 rounded bg-slate-900 border border-emerald-900/40 text-slate-300 flex items-center justify-between">
                    <span><strong class="text-emerald-400">Child 1:</strong> Mathematics</span>
                    <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-mono">Code: M</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-emerald-900/40 text-slate-300 flex items-center justify-between">
                    <span><strong class="text-emerald-400">Child 2:</strong> Languages</span>
                    <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono">Code: L</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-emerald-900/40 text-slate-300 flex items-center justify-between">
                    <span><strong class="text-emerald-400">Child 3:</strong> Physical Education</span>
                    <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-mono">Code: P.E.</span>
                </div>
            `;
        }
        if (cardEl) {
            cardEl.className = 'bg-emerald-950/20 border border-emerald-800/40 p-3 rounded-xl text-xs text-emerald-300 leading-relaxed';
            cardEl.innerHTML = '<strong>Survey Design Insight:</strong> Asking for the single most favorite subject produces exactly one category per student, allowing fast, unambiguous tallying and direct frequency tabulation.';
        }
    }
}

// ============================================================================
// SIMULATOR 2: Student Response Stream Recorder
// ============================================================================
const RAW_CLASS_CODES = [
    'M','L','T','PE','M','A','M','L','T',
    'PE','M','M','L','A','PE','M','L','T',
    'PE','M','A','L','M','PE','T','M','L',
    'PE','M','A','L','T','M','PE','M','L',
    'T','PE','M','A','L','PE','M','PE','T'
];

function generateFullStream() {
    playSuccessSfx();
    const grid = document.getElementById('stream-chips-grid');
    const badge = document.getElementById('stream-count-badge');
    if (!grid) return;
    
    grid.innerHTML = '';
    const colorMap = {
        'M': 'bg-blue-600/30 text-blue-300 border-blue-500/40',
        'L': 'bg-emerald-600/30 text-emerald-300 border-emerald-500/40',
        'T': 'bg-purple-600/30 text-purple-300 border-purple-500/40',
        'A': 'bg-amber-600/30 text-amber-300 border-amber-500/40',
        'PE': 'bg-rose-600/30 text-rose-300 border-rose-500/40'
    };
    
    RAW_CLASS_CODES.forEach((code, idx) => {
        const chip = document.createElement('div');
        chip.className = `p-1.5 rounded border ${colorMap[code]} font-mono font-bold text-center`;
        chip.innerText = code;
        chip.title = `Student ${idx + 1}: ${code}`;
        grid.appendChild(chip);
    });
    
    if (badge) badge.innerText = '45 / 45 Recorded';
}

function clearStreamLog() {
    playClickSfx();
    const grid = document.getElementById('stream-chips-grid');
    const badge = document.getElementById('stream-count-badge');
    if (grid) grid.innerHTML = '<div class="col-span-full py-4 text-slate-500 text-center font-sans font-normal">Click "Generate Full 45" to populate the classroom log stream.</div>';
    if (badge) badge.innerText = '0 / 45 Recorded';
}

// ============================================================================
// SIMULATOR 3: Interactive Frequency Table Builder
// ============================================================================
const SUBJECT_COUNTS = {
    'M': { name: 'Mathematics', count: 14, color: 'text-blue-400', badge: 'bg-blue-900/40 text-blue-300' },
    'L': { name: 'Languages', count: 9, color: 'text-emerald-400', badge: 'bg-emerald-900/40 text-emerald-300' },
    'T': { name: 'World Around Us', count: 7, color: 'text-purple-400', badge: 'bg-purple-900/40 text-purple-300' },
    'A': { name: 'Visual Arts', count: 5, color: 'text-amber-400', badge: 'bg-amber-900/40 text-amber-300' },
    'PE': { name: 'Physical Education', count: 10, color: 'text-rose-400', badge: 'bg-rose-900/40 text-rose-300' }
};
let activeTabulated = {};

function makeTallySvg(count) {
    const bundles = Math.floor(count / 5);
    const rem = count % 5;
    let out = '<div class="flex items-center gap-1.5">';
    
    for (let b = 0; b < bundles; b++) {
        out += `
            <svg class="w-7 h-5 text-emerald-400" viewBox="0 0 28 20">
                <line x1="4" y1="2" x2="4" y2="18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                <line x1="9" y1="2" x2="9" y2="18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                <line x1="14" y1="2" x2="14" y2="18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                <line x1="19" y1="2" x2="19" y2="18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                <line x1="2" y1="18" x2="22" y2="2" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
        `;
    }
    if (rem > 0) {
        out += '<svg class="w-7 h-5 text-emerald-400" viewBox="0 0 28 20">';
        for (let r = 0; r < rem; r++) {
            const x = 4 + r * 5;
            out += `<line x1="${x}" y1="2" x2="${x}" y2="18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>`;
        }
        out += '</svg>';
    }
    out += '</div>';
    return out;
}

function renderFreqTable() {
    const tbody = document.getElementById('freq-table-body');
    const grandEl = document.getElementById('freq-grand-total');
    if (!tbody) return;
    
    tbody.innerHTML = '';
    let runningTotal = 0;
    
    for (const [code, info] of Object.entries(SUBJECT_COUNTS)) {
        const isAdded = activeTabulated[code];
        const count = isAdded ? info.count : 0;
        runningTotal += count;
        
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-950/40';
        tr.innerHTML = `
            <td class="py-2.5 px-3 font-sans font-medium text-white">${info.name}</td>
            <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded ${info.badge} font-bold text-[10px]">${code}</span></td>
            <td class="py-2.5 px-3">${isAdded ? makeTallySvg(info.count) : '<span class="text-slate-600">-</span>'}</td>
            <td class="py-2.5 px-3 text-right font-bold ${info.color}">${count}</td>
        `;
        tbody.appendChild(tr);
    }
    
    if (grandEl) grandEl.innerText = `${runningTotal} / 45`;
}

function tabulateCategory(code) {
    playClickSfx();
    activeTabulated[code] = true;
    renderFreqTable();
}

function tabulateAllCategories() {
    playSuccessSfx();
    activeTabulated = { 'M': true, 'L': true, 'T': true, 'A': true, 'PE': true };
    renderFreqTable();
}

// ============================================================================
// SIMULATOR 4: Data Table Analyzer
// ============================================================================
function analyzeTableMetric(type) {
    playClickSfx();
    const badge = document.getElementById('analyzer-badge');
    const title = document.getElementById('analyzer-title');
    const desc = document.getElementById('analyzer-desc');
    const stat = document.getElementById('analyzer-stat');
    
    if (type === 'most') {
        badge.innerText = 'Most Popular';
        title.innerText = 'Favorite Classroom Subject';
        desc.innerText = 'Mathematics received 14 votes out of 45 students, making it the most preferred subject across the entire class.';
        stat.innerText = '14 (M)';
        stat.className = 'text-3xl font-black font-mono text-blue-400 shrink-0 bg-blue-950/40 px-5 py-3 rounded-xl border border-blue-800/50';
    } else if (type === 'least') {
        badge.innerText = 'Least Popular';
        title.innerText = 'Lowest Selected Subject';
        desc.innerText = 'Visual Arts received 5 votes, which is the lowest frequency in our surveyed table.';
        stat.innerText = '5 (Arts)';
        stat.className = 'text-3xl font-black font-mono text-amber-400 shrink-0 bg-amber-950/40 px-5 py-3 rounded-xl border border-amber-800/50';
    } else if (type === 'diff') {
        badge.innerText = 'Margin of Difference';
        title.innerText = 'Mathematics vs Visual Arts';
        desc.innerText = 'Subtracting Arts (5) from Mathematics (14): 14 − 5 = 9. Mathematics surpassed Arts by 9 student votes.';
        stat.innerText = '+9 Votes';
        stat.className = 'text-3xl font-black font-mono text-emerald-400 shrink-0 bg-emerald-950/40 px-5 py-3 rounded-xl border border-emerald-800/50';
    } else if (type === 'stem') {
        badge.innerText = 'STEM Combination';
        title.innerText = 'Mathematics + World Around Us';
        desc.innerText = 'Combining Mathematics (14) and The World Around Us (7): 14 + 7 = 21 students chose these analytical subjects.';
        stat.innerText = '21 Students';
        stat.className = 'text-3xl font-black font-mono text-purple-400 shrink-0 bg-purple-950/40 px-5 py-3 rounded-xl border border-purple-800/50';
    } else if (type === 'pe_ratio') {
        badge.innerText = 'Proportion';
        title.innerText = 'Physical Education Share';
        desc.innerText = '10 out of 45 students picked Physical Education, representing exactly 10/45 (simplifies to 2/9) of the classroom.';
        stat.innerText = '10 / 45';
        stat.className = 'text-3xl font-black font-mono text-rose-400 shrink-0 bg-rose-950/40 px-5 py-3 rounded-xl border border-rose-800/50';
    }
}

// ============================================================================
// SIMULATOR 5: Ice Gola Tally Counter
// ============================================================================
const tallyCounts = { kk: 13, or: 18, rs: 9, mg: 15 };

function renderTallyBoard() {
    for (const [flavor, val] of Object.entries(tallyCounts)) {
        const cntEl = document.getElementById(`tally-count-${flavor}`);
        const svgEl = document.getElementById(`tally-svg-${flavor}`);
        if (cntEl) cntEl.innerText = val;
        if (svgEl) svgEl.innerHTML = makeTallySvg(val);
    }
}

function adjustTally(flavor, delta) {
    playClickSfx();
    const nextVal = tallyCounts[flavor] + delta;
    if (nextVal >= 0 && nextVal <= 30) {
        tallyCounts[flavor] = nextVal;
        renderTallyBoard();
    }
}

// ============================================================================
// SIMULATOR 6: Ice Gola Pictograph Studio
// ============================================================================
let currentPictoScale = 4;
const PICTO_SALES = { kk: 28, or: 36, rs: 20, mg: 24 };

function setPictoScale(scale) {
    playClickSfx();
    currentPictoScale = scale;
    const btn2 = document.getElementById('picto-scale-2');
    const btn4 = document.getElementById('picto-scale-4');
    
    if (scale === 2) {
        btn2.classList.add('border-pink-500', 'bg-pink-900/40', 'text-pink-300', 'ring-2', 'ring-pink-500');
        btn2.classList.remove('border-slate-700', 'bg-slate-800', 'text-slate-300');
        btn4.classList.remove('border-pink-500', 'bg-pink-900/40', 'text-pink-300', 'ring-2', 'ring-pink-500');
        btn4.classList.add('border-slate-700', 'bg-slate-800', 'text-slate-300');
    } else {
        btn4.classList.add('border-pink-500', 'bg-pink-900/40', 'text-pink-300', 'ring-2', 'ring-pink-500');
        btn4.classList.remove('border-slate-700', 'bg-slate-800', 'text-slate-300');
        btn2.classList.remove('border-pink-500', 'bg-pink-900/40', 'text-pink-300', 'ring-2', 'ring-pink-500');
        btn2.classList.add('border-slate-700', 'bg-slate-800', 'text-slate-300');
    }
    renderPictographRows();
}

function makeCupIcon(colorHex) {
    return `
        <svg class="w-5 h-6 shrink-0" viewBox="0 0 20 24" fill="none">
            <path d="M4 2L16 2L14 18C14 20 12 21 10 21C8 21 6 20 6 18L4 2Z" fill="${colorHex}" stroke="#e2e8f0" stroke-width="1.5"/>
            <path d="M10 2V21" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
            <circle cx="10" cy="5" r="3" fill="#ffffff" opacity="0.7"/>
        </svg>
    `;
}

function renderPictographRows() {
    const colors = { kk: '#a855f7', or: '#f97316', rs: '#f43f5e', mg: '#eab308' };
    for (const [flavor, total] of Object.entries(PICTO_SALES)) {
        const row = document.getElementById(`picto-row-${flavor}`);
        const badge = document.getElementById(`picto-badge-${flavor}`);
        if (!row) continue;
        
        const numIcons = Math.floor(total / currentPictoScale);
        let html = '';
        for (let i = 0; i < numIcons; i++) {
            html += makeCupIcon(colors[flavor]);
        }
        row.innerHTML = html;
        if (badge) badge.innerText = `${numIcons} cups (= ${total})`;
    }
}

// ============================================================================
// SIMULATOR 7 & 8: Two-Way Classification Matrix & Contingency
// ============================================================================
function highlightMatrixCell(cell) {
    playClickSfx();
    const box = document.getElementById('matrix-info-box');
    if (!box) return;
    
    if (cell === 'both') {
        box.innerHTML = '<strong>Plays Both Cricket & Chess (11 Students):</strong> 6 boys and 5 girls enjoy playing both sports during activity hour.';
    } else if (cell === 'only_chess') {
        box.innerHTML = '<strong>Plays Only Chess (11 Students):</strong> 4 boys and 7 girls focus exclusively on chess strategy without cricket.';
    } else if (cell === 'only_cricket') {
        box.innerHTML = '<strong>Plays Only Cricket (20 Students):</strong> 12 boys and 8 girls play cricket but do not participate in chess.';
    } else if (cell === 'neither') {
        box.innerHTML = '<strong>Plays Neither Sport (6 Students):</strong> 2 boys and 4 girls participate in other school activities instead of chess or cricket.';
    }
}

// ============================================================================
// SIMULATOR 9: Bal Mela Food Pictograph
// ============================================================================
const BAL_MELA_DATA = {
    fri: { chaat: 20, sand: 30, chaatPlates: 4, sandPlates: 6, total: 50 },
    sat: { chaat: 40, sand: 50, chaatPlates: 8, sandPlates: 10, total: 90 },
    sun: { chaat: 30, sand: 40, chaatPlates: 6, sandPlates: 8, total: 70 },
    all: { chaat: 90, sand: 120, chaatPlates: 18, sandPlates: 24, total: 210 }
};

function makePlateSvg(colorHex) {
    return `
        <svg class="w-6 h-6 shrink-0" viewBox="0 0 24 24" fill="none">
            <ellipse cx="12" cy="12" rx="10" ry="8" fill="${colorHex}" stroke="#ffffff" stroke-width="1.5"/>
            <ellipse cx="12" cy="12" rx="6" ry="4" fill="#ffffff" opacity="0.3"/>
        </svg>
    `;
}

function showBalMelaDay(day) {
    playClickSfx();
    ['fri', 'sat', 'sun', 'all'].forEach(d => {
        const btn = document.getElementById(`bm-tab-${d}`);
        if (btn) {
            if (d === day) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const dData = BAL_MELA_DATA[day];
    const chaatIcons = document.getElementById('bm-chaat-icons');
    const sandIcons = document.getElementById('bm-sand-icons');
    const chaatStat = document.getElementById('bm-chaat-stat');
    const sandStat = document.getElementById('bm-sand-stat');
    const totalEl = document.getElementById('bm-day-total');
    
    if (chaatStat) chaatStat.innerText = `${dData.chaatPlates} plates = ${dData.chaat} portions`;
    if (sandStat) sandStat.innerText = `${dData.sandPlates} plates = ${dData.sand} portions`;
    if (totalEl) totalEl.innerText = `Day Total: ${dData.total} Portions`;
    
    if (chaatIcons) {
        let h = '';
        for (let i = 0; i < dData.chaatPlates; i++) h += makePlateSvg('#10b981');
        chaatIcons.innerHTML = h;
    }
    if (sandIcons) {
        let h = '';
        for (let i = 0; i < dData.sandPlates; i++) h += makePlateSvg('#f59e0b');
        sandIcons.innerHTML = h;
    }
}

// ============================================================================
// SIMULATOR 10: Food Sales Analysis
// ============================================================================
function analyzeFoodSales(type) {
    playClickSfx();
    const box = document.getElementById('food-analysis-box');
    const rowFri = document.getElementById('row-fri');
    const rowSat = document.getElementById('row-sat');
    const rowSun = document.getElementById('row-sun');
    
    [rowFri, rowSat, rowSun].forEach(r => r && r.classList.remove('bg-red-950/40', 'ring-2', 'ring-red-500'));
    
    if (type === 'peak') {
        if (rowSat) rowSat.classList.add('bg-red-950/40', 'ring-2', 'ring-red-500');
        if (box) box.innerHTML = '<strong>Peak Day Highlight:</strong> Saturday generated 90 snack sales and ₹1,150 revenue, making it the most profitable day due to heavy weekend crowd footfall.';
    } else if (type === 'diff') {
        if (box) box.innerHTML = '<strong>Product Comparison:</strong> 120 Sandwiches − 90 Fruit Chaats = <strong>30 more sandwiches</strong> sold over the weekend.';
    } else if (type === 'revenue') {
        if (box) box.innerHTML = '<strong>Total Revenue:</strong> (90 Fruit Chaats × ₹10 = ₹900) + (120 Sandwiches × ₹15 = ₹1,800) = <strong>₹2,700 Grand Total</strong>.';
    }
}

// ============================================================================
// SIMULATOR 11: Base-Ten Dienes Blocks
// ============================================================================
const dienesState = { th: 1, h: 2, t: 3, u: 4 };

function renderDienesBlocks() {
    const canvas = document.getElementById('dienes-canvas');
    const expEl = document.getElementById('dienes-expanded');
    const totalEl = document.getElementById('dienes-total');
    if (!canvas) return;
    
    let html = '';
    // Thousands Cube (Isometric 3D Cube)
    for (let i = 0; i < dienesState.th; i++) {
        html += `
            <div class="flex flex-col items-center">
                <svg class="w-12 h-12" viewBox="0 0 40 40">
                    <polygon points="20,4 36,12 20,20 4,12" fill="#f59e0b" stroke="#b45309" stroke-width="1"/>
                    <polygon points="4,12 20,20 20,36 4,28" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                    <polygon points="36,12 20,20 20,36 36,28" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                </svg>
                <span class="text-[9px] text-amber-400 font-mono font-bold">1,000</span>
            </div>
        `;
    }
    // Hundreds Flat (10x10 Flat)
    for (let i = 0; i < dienesState.h; i++) {
        html += `
            <div class="flex flex-col items-center">
                <svg class="w-10 h-10" viewBox="0 0 30 30">
                    <rect x="2" y="2" width="26" height="26" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1"/>
                    <line x1="8" y1="2" x2="8" y2="28" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="14" y1="2" x2="14" y2="28" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="20" y1="2" x2="20" y2="28" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="8" x2="28" y2="8" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="14" x2="28" y2="14" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="20" x2="28" y2="20" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                </svg>
                <span class="text-[9px] text-blue-400 font-mono font-bold">100</span>
            </div>
        `;
    }
    // Tens Rod (1x10 Rod)
    for (let i = 0; i < dienesState.t; i++) {
        html += `
            <div class="flex flex-col items-center">
                <svg class="w-4 h-10" viewBox="0 0 10 30">
                    <rect x="2" y="2" width="6" height="26" fill="#10b981" stroke="#047857" stroke-width="1"/>
                    <line x1="2" y1="7" x2="8" y2="7" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="12" x2="8" y2="12" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="17" x2="8" y2="17" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                    <line x1="2" y1="22" x2="8" y2="22" stroke="#ffffff" stroke-width="0.5" opacity="0.6"/>
                </svg>
                <span class="text-[9px] text-emerald-400 font-mono font-bold">10</span>
            </div>
        `;
    }
    // Unit Cubes
    for (let i = 0; i < dienesState.u; i++) {
        html += `
            <div class="flex flex-col items-center">
                <svg class="w-4 h-4" viewBox="0 0 10 10">
                    <rect x="2" y="2" width="6" height="6" fill="#f43f5e" stroke="#be123c" stroke-width="1"/>
                </svg>
                <span class="text-[9px] text-rose-400 font-mono font-bold">1</span>
            </div>
        `;
    }
    
    canvas.innerHTML = html;
    const total = dienesState.th * 1000 + dienesState.h * 100 + dienesState.t * 10 + dienesState.u;
    if (expEl) expEl.innerText = `${dienesState.th * 1000} + ${dienesState.h * 100} + ${dienesState.t * 10} + ${dienesState.u}`;
    if (totalEl) totalEl.innerText = total.toLocaleString('en-IN');
}

function adjustDienes(unit, delta) {
    playClickSfx();
    const next = dienesState[unit] + delta;
    if (next >= 0 && next <= 9) {
        dienesState[unit] = next;
        const valEl = document.getElementById(`dienes-val-${unit}`);
        if (valEl) valEl.innerText = next;
        renderDienesBlocks();
    }
}

// ============================================================================
// SIMULATOR 12: 3D Shape Net Folder
// ============================================================================
let currentNetShape = 'cube';
let currentNetFoldAngle = 0;

function selectNetShape(shape) {
    playClickSfx();
    currentNetShape = shape;
    ['cube', 'cuboid', 'prism', 'pyramid'].forEach(s => {
        const btn = document.getElementById(`net-btn-${s}`);
        if (btn) {
            if (s === shape) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    renderNetVisual();
}

function updateNetFold(angle) {
    currentNetFoldAngle = parseInt(angle, 10);
    const badge = document.getElementById('net-angle-badge');
    if (badge) badge.innerText = `Fold Angle: ${angle}° (${angle === '0' ? 'Flat' : angle === '90' ? 'Closed Solid' : 'Folding'})`;
    renderNetVisual();
}

function renderNetVisual() {
    const svg = document.getElementById('net-svg-display');
    const desc = document.getElementById('net-description');
    if (!svg) return;
    
    const angleRatio = currentNetFoldAngle / 90;
    const scale = 1 - (angleRatio * 0.3);
    const rot = angleRatio * 25;
    
    if (currentNetShape === 'cube') {
        svg.innerHTML = `
            <g transform="translate(150, 80) scale(${scale}) rotate(${rot}) translate(-150, -80)">
                <!-- Center Square -->
                <rect x="130" y="60" width="40" height="40" fill="#0d9488" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Top flap -->
                <rect x="130" y="${60 - 40 * (1 - angleRatio)}" width="40" height="${40 * (1 - angleRatio)}" fill="#14b8a6" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Bottom flap -->
                <rect x="130" y="100" width="40" height="${40 * (1 - angleRatio)}" fill="#14b8a6" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Left flap -->
                <rect x="${130 - 40 * (1 - angleRatio)}" y="60" width="${40 * (1 - angleRatio)}" height="40" fill="#14b8a6" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Right flap -->
                <rect x="170" y="60" width="${40 * (1 - angleRatio)}" height="40" fill="#14b8a6" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Extra top flap for cube closure -->
                <rect x="130" y="${60 - 80 * (1 - angleRatio)}" width="40" height="${40 * (1 - angleRatio)}" fill="#2dd4bf" stroke="#ffffff" stroke-width="1.5"/>
            </g>
        `;
        if (desc) desc.innerText = 'Cube: 6 congruent square faces folding along right angles to enclose a hollow solid.';
    } else if (currentNetShape === 'cuboid') {
        svg.innerHTML = `
            <g transform="translate(150, 80) scale(${scale}) rotate(${rot}) translate(-150, -80)">
                <rect x="120" y="55" width="60" height="40" fill="#0284c7" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="120" y="${55 - 30 * (1 - angleRatio)}" width="60" height="${30 * (1 - angleRatio)}" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="120" y="95" width="60" height="${30 * (1 - angleRatio)}" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="${120 - 35 * (1 - angleRatio)}" y="55" width="${35 * (1 - angleRatio)}" height="40" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="180" y="55" width="${35 * (1 - angleRatio)}" height="40" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="120" y="${55 - 70 * (1 - angleRatio)}" width="60" height="${40 * (1 - angleRatio)}" fill="#7dd3fc" stroke="#ffffff" stroke-width="1.5"/>
            </g>
        `;
        if (desc) desc.innerText = 'Cuboid (Rectangular Prism): 6 rectangular faces paired in three opposite congruent sets.';
    } else if (currentNetShape === 'prism') {
        svg.innerHTML = `
            <g transform="translate(150, 80) scale(${scale}) rotate(${rot}) translate(-150, -80)">
                <rect x="125" y="60" width="50" height="40" fill="#8b5cf6" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="${125 - 45 * (1 - angleRatio)}" y="60" width="${45 * (1 - angleRatio)}" height="40" fill="#a78bfa" stroke="#ffffff" stroke-width="1.5"/>
                <rect x="175" y="60" width="${45 * (1 - angleRatio)}" height="40" fill="#a78bfa" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="125,60 175,60 150,${60 - 35 * (1 - angleRatio)}" fill="#c4b5fd" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="125,100 175,100 150,${100 + 35 * (1 - angleRatio)}" fill="#c4b5fd" stroke="#ffffff" stroke-width="1.5"/>
            </g>
        `;
        if (desc) desc.innerText = 'Triangular Prism: 2 identical triangular bases connected by 3 rectangular sides.';
    } else if (currentNetShape === 'pyramid') {
        svg.innerHTML = `
            <g transform="translate(150, 80) scale(${scale}) rotate(${rot}) translate(-150, -80)">
                <rect x="130" y="60" width="40" height="40" fill="#ec4899" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="130,60 170,60 150,${60 - 45 * (1 - angleRatio)}" fill="#f472b6" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="130,100 170,100 150,${100 + 45 * (1 - angleRatio)}" fill="#f472b6" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="130,60 130,100 ${130 - 45 * (1 - angleRatio)},80" fill="#f472b6" stroke="#ffffff" stroke-width="1.5"/>
                <polygon points="170,60 170,100 ${170 + 45 * (1 - angleRatio)},80" fill="#f472b6" stroke="#ffffff" stroke-width="1.5"/>
            </g>
        `;
        if (desc) desc.innerText = 'Square Pyramid: 1 central square base surrounded by 4 triangular flaps meeting at a single apex.';
    }
}

// ============================================================================
// SIMULATOR 13: Place Value Arrow Cards
// ============================================================================
let arrowCardMode = 'expanded';

function setArrowCardMode(mode) {
    playClickSfx();
    arrowCardMode = mode;
    const btnStack = document.getElementById('ac-btn-stack');
    const btnExp = document.getElementById('ac-btn-expand');
    
    if (mode === 'stacked') {
        if (btnStack) btnStack.className = 'px-4 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs shadow ring-2 ring-sky-400';
        if (btnExp) btnExp.className = 'px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs';
    } else {
        if (btnExp) btnExp.className = 'px-4 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs shadow ring-2 ring-sky-400';
        if (btnStack) btnStack.className = 'px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs';
    }
    updateArrowCards();
}

function updateArrowCards() {
    const th = document.getElementById('ac-th')?.value || '4000';
    const h = document.getElementById('ac-h')?.value || '300';
    const t = document.getElementById('ac-t')?.value || '20';
    const u = document.getElementById('ac-u')?.value || '5';
    const container = document.getElementById('arrow-cards-visual');
    if (!container) return;
    
    if (arrowCardMode === 'expanded') {
        container.innerHTML = `
            <div class="px-3 py-2 rounded-l-lg rounded-r-2xl bg-amber-500/20 border border-amber-500 text-amber-300">${th}</div>
            <span class="text-slate-500 font-sans">+</span>
            <div class="px-3 py-2 rounded-l-lg rounded-r-2xl bg-blue-500/20 border border-blue-500 text-blue-300">${h}</div>
            <span class="text-slate-500 font-sans">+</span>
            <div class="px-3 py-2 rounded-l-lg rounded-r-2xl bg-emerald-500/20 border border-emerald-500 text-emerald-300">${t}</div>
            <span class="text-slate-500 font-sans">+</span>
            <div class="px-3 py-2 rounded-l-lg rounded-r-2xl bg-rose-500/20 border border-rose-500 text-rose-300">${u}</div>
        `;
    } else {
        const compact = (parseInt(th, 10) + parseInt(h, 10) + parseInt(t, 10) + parseInt(u, 10)).toLocaleString('en-IN');
        container.innerHTML = `
            <div class="px-6 py-3 rounded-l-xl rounded-r-3xl bg-sky-600 text-white text-xl font-bold tracking-widest border border-sky-400 shadow-lg flex items-center gap-1">
                <span class="text-amber-300">${th[0]}</span>
                <span class="text-blue-300">${h !== '0' ? h[0] : '0'}</span>
                <span class="text-emerald-300">${t !== '0' ? t[0] : '0'}</span>
                <span class="text-rose-300">${u}</span>
                <span class="ml-2 text-xs font-sans font-normal opacity-80">(Standard Numeral: ${compact})</span>
            </div>
        `;
    }
}

// ============================================================================
// SIMULATOR 14: Fraction Strip Kit
// ============================================================================
function highlightFractionEquiv(type) {
    playClickSfx();
    resetFractionHighlights();
    const box = document.getElementById('fraction-feedback-box');
    
    if (type === 'half') {
        const half = document.getElementById('fs-half-1');
        const q1 = document.getElementById('fs-q-1');
        const q2 = document.getElementById('fs-q-2');
        if (half) half.classList.add('ring-2', 'ring-white', 'bg-blue-600');
        if (q1) q1.classList.add('ring-2', 'ring-white', 'bg-emerald-600');
        if (q2) q2.classList.add('ring-2', 'ring-white', 'bg-emerald-600');
        if (box) box.innerHTML = '<strong>Equivalence Proof:</strong> 1/2 (12 cm) = 2/4 (6 cm + 6 cm = 12 cm) = 4/8 (3 cm × 4 = 12 cm).';
    } else if (type === 'third') {
        if (box) box.innerHTML = '<strong>Thirds Equivalence:</strong> 1/3 (8 cm) = 2/6 (4 cm + 4 cm = 8 cm) = 4/12 (2 cm × 4 = 8 cm).';
    } else if (type === 'quarter') {
        const q1 = document.getElementById('fs-q-1');
        if (q1) q1.classList.add('ring-2', 'ring-white', 'bg-emerald-600');
        if (box) box.innerHTML = '<strong>Quarter Equivalence:</strong> 1/4 (6 cm) = 2/8 (3 cm + 3 cm = 6 cm).';
    }
}

function resetFractionHighlights() {
    document.querySelectorAll('[id^="fs-"]').forEach(el => {
        el.classList.remove('ring-2', 'ring-white');
    });
    const box = document.getElementById('fraction-feedback-box');
    if (box) box.innerText = 'Fraction strips benchmark against a 24 cm whole unit.';
}

// ============================================================================
// SIMULATOR 15: Word Problem Bar Models
// ============================================================================
function selectWordProblemModel(type) {
    playClickSfx();
    ['combine', 'compare', 'change'].forEach(m => {
        const btn = document.getElementById(`wp-tab-${m}`);
        if (btn) {
            if (m === type) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-green-500 bg-green-950/40 text-green-300 font-bold ring-2 ring-green-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const probEl = document.getElementById('wp-problem-text');
    const diagEl = document.getElementById('wp-diagram-container');
    const eqEl = document.getElementById('wp-equation');
    const badgeEl = document.getElementById('wp-operation-badge');
    
    if (type === 'combine') {
        if (probEl) probEl.innerText = 'In our class sports survey, 24 boys and 24 girls participated. What is the total combined number of students?';
        if (diagEl) {
            diagEl.innerHTML = `
                <div class="flex gap-2">
                    <div class="flex-1 p-2 rounded bg-blue-900/60 border border-blue-500 text-center text-blue-200 font-mono font-bold">Part 1: 24 Boys</div>
                    <div class="flex-1 p-2 rounded bg-pink-900/60 border border-pink-500 text-center text-pink-200 font-mono font-bold">Part 2: 24 Girls</div>
                </div>
                <div class="w-full p-2.5 rounded bg-emerald-950/60 border border-emerald-500 text-center text-emerald-300 font-mono font-bold">
                    Whole: ? (Combined Total = 48)
                </div>
            `;
        }
        if (eqEl) eqEl.innerText = '24 + 24 = 48 Students';
        if (badgeEl) badgeEl.innerText = 'Operation: Addition';
    } else if (type === 'compare') {
        if (probEl) probEl.innerText = 'At the Bal Mela stall, 120 sandwiches and 90 fruit chaats were sold. How many more sandwiches were sold than fruit chaats?';
        if (diagEl) {
            diagEl.innerHTML = `
                <div class="space-y-2">
                    <div class="w-full flex">
                        <div class="w-3/4 p-2 rounded bg-amber-900/60 border border-amber-500 text-center text-amber-200 font-mono font-bold">Sandwiches: 120</div>
                    </div>
                    <div class="w-full flex items-center gap-2">
                        <div class="w-[56%] p-2 rounded bg-emerald-900/60 border border-emerald-500 text-center text-emerald-200 font-mono font-bold">Chaat: 90</div>
                        <div class="flex-1 p-2 rounded bg-rose-950/60 border border-rose-500 border-dashed text-center text-rose-300 font-mono font-bold">Diff: 30</div>
                    </div>
                </div>
            `;
        }
        if (eqEl) eqEl.innerText = '120 − 90 = 30 More Sandwiches';
        if (badgeEl) badgeEl.innerText = 'Operation: Subtraction (Difference)';
    } else if (type === 'change') {
        if (probEl) probEl.innerText = 'A library corner started with 85 math workbooks. After pupils checked out some copies, 58 remained. How many books were borrowed?';
        if (diagEl) {
            diagEl.innerHTML = `
                <div class="w-full p-2.5 rounded bg-indigo-950/60 border border-indigo-500 text-center text-indigo-200 font-mono font-bold mb-2">
                    Initial Whole: 85 Books
                </div>
                <div class="flex gap-2">
                    <div class="w-[68%] p-2 rounded bg-emerald-900/60 border border-emerald-500 text-center text-emerald-200 font-mono font-bold">Remaining: 58</div>
                    <div class="flex-1 p-2 rounded bg-rose-900/60 border border-rose-500 border-dashed text-center text-rose-200 font-mono font-bold">Borrowed (?): 27</div>
                </div>
            `;
        }
        if (eqEl) eqEl.innerText = '85 − 58 = 27 Borrowed Books';
        if (badgeEl) badgeEl.innerText = 'Operation: Subtraction (Change)';
    }
}

// ============================================================================
// SIMULATOR 16: Comprehensive Statistical Dashboard
// ============================================================================
function switchDashboardView(view) {
    playClickSfx();
    ['overview', 'table', 'picto', 'matrix'].forEach(v => {
        const btn = document.getElementById(`dash-tab-${v}`);
        if (btn) {
            if (v === view) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const content = document.getElementById('dashboard-view-content');
    if (!content) return;
    
    if (view === 'overview') {
        content.innerHTML = `
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                <div class="p-3 bg-slate-900 rounded-xl border border-blue-900/40 text-center space-y-1">
                    <span class="text-[10px] uppercase font-bold text-slate-400">Class Survey</span>
                    <div class="text-xl font-bold font-mono text-blue-400">45 Students</div>
                    <span class="text-[10px] text-slate-500">Top: Math (14)</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-orange-900/40 text-center space-y-1">
                    <span class="text-[10px] uppercase font-bold text-slate-400">Bal Mela Sales</span>
                    <div class="text-xl font-bold font-mono text-orange-400">210 Portions</div>
                    <span class="text-[10px] text-slate-500">Peak: Sat (90)</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-teal-900/40 text-center space-y-1">
                    <span class="text-[10px] uppercase font-bold text-slate-400">Sports Matrix</span>
                    <div class="text-xl font-bold font-mono text-teal-400">48 Students</div>
                    <span class="text-[10px] text-slate-500">Both: 11 (23%)</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-purple-900/40 text-center space-y-1">
                    <span class="text-[10px] uppercase font-bold text-slate-400">Total Revenue</span>
                    <div class="text-xl font-bold font-mono text-purple-400">₹2,700</div>
                    <span class="text-[10px] text-slate-500">120 Sand + 90 Chaat</span>
                </div>
            </div>
        `;
    } else if (view === 'table') {
        content.innerHTML = `
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs font-mono">
                    <tr class="text-slate-400 border-b border-slate-800"><th>Subject</th><th>Votes</th><th>Percent</th></tr>
                    <tr><td class="text-blue-400 py-1">Mathematics</td><td>14</td><td>31.1%</td></tr>
                    <tr><td class="text-rose-400 py-1">Physical Education</td><td>10</td><td>22.2%</td></tr>
                    <tr><td class="text-emerald-400 py-1">Languages</td><td>9</td><td>20.0%</td></tr>
                    <tr><td class="text-purple-400 py-1">World Around Us</td><td>7</td><td>15.6%</td></tr>
                    <tr><td class="text-amber-400 py-1">Visual Arts</td><td>5</td><td>11.1%</td></tr>
                    <tr class="font-bold text-white border-t border-slate-800"><td>Total</td><td>45</td><td>100.0%</td></tr>
                </table>
            </div>
        `;
    } else if (view === 'picto') {
        content.innerHTML = `
            <div class="space-y-2 text-xs">
                <div class="flex items-center justify-between"><span class="text-emerald-400">Fruit Chaat: 90 Portions</span><span class="text-slate-400 font-mono">18 Plates (🍽️=5)</span></div>
                <div class="flex items-center justify-between"><span class="text-amber-400">Sandwiches: 120 Portions</span><span class="text-slate-400 font-mono">24 Plates (🍽️=5)</span></div>
                <div class="p-2 rounded bg-slate-900 text-slate-400 text-center mt-2 border border-slate-800">Weekend Total: 210 Portions Sold</div>
            </div>
        `;
    } else if (view === 'matrix') {
        content.innerHTML = `
            <div class="grid grid-cols-2 gap-2 text-xs text-center font-mono">
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800">Cricket Only: <strong class="text-amber-400">20</strong></div>
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800">Chess Only: <strong class="text-blue-400">11</strong></div>
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800">Both Sports: <strong class="text-indigo-400">11</strong></div>
                <div class="p-2.5 bg-slate-900 rounded border border-slate-800">Neither Sport: <strong class="text-slate-400">6</strong></div>
            </div>
        `;
    }
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSimulatorForSlide(slideNum) {
    if (slideNum === 1) selectSurveyQuestion('specific');
    if (slideNum === 2) generateFullStream();
    if (slideNum === 3) tabulateAllCategories();
    if (slideNum === 4) analyzeTableMetric('most');
    if (slideNum === 5) renderTallyBoard();
    if (slideNum === 6) renderPictographRows();
    if (slideNum === 9) showBalMelaDay('all');
    if (slideNum === 10) analyzeFoodSales('peak');
    if (slideNum === 11) renderDienesBlocks();
    if (slideNum === 12) renderNetVisual();
    if (slideNum === 13) updateArrowCards();
    if (slideNum === 15) selectWordProblemModel('combine');
    if (slideNum === 16) switchDashboardView('overview');
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            // Voices pre-loaded
        };
    }
});
'''

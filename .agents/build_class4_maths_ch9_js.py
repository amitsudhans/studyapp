# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 9: Equal Groups
Generates the complete JavaScript Engine for Chapter 9.
"""

import sys
import os

js_code = r'''
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
    if (!slide || currentSlide > 16) {
        alert('Classroom lecture is only available on Slides 1 to 16.');
        return;
    }
    
    const lectureText = slide.speech;
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
// Quiz Question Handlers & Solution Modal
// ============================================================================
function checkQuiz(slideId, qIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qData = slide.quizzes[qIdx];
    const fb = document.getElementById(`quiz-fb-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.quiz-btn-${slideId}-${qIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = qData.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${qData.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Incorrect.</strong> ${qData.exp}`;
    }
}

function toggleHint(slideId, qIdx) {
    playClickSfx();
    const hintEl = document.getElementById(`quiz-hint-${slideId}-${qIdx}`);
    if (hintEl) {
        hintEl.classList.toggle('hidden');
    }
}

function openSolutionModal(slideId, qIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    const qData = slide.quizzes[qIdx];
    
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('solutionModalTitle');
    const content = document.getElementById('solutionModalContent');
    if (!modal || !title || !content) return;
    
    title.innerHTML = `<span>💡</span> Detailed Solution - Question ${qIdx + 1}`;
    content.innerHTML = `
        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm font-semibold text-slate-200">
            ${qData.q}
        </div>
        <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300 font-medium">
            <strong>Hint:</strong> ${qData.hint || 'Carefully note the numbers and grouping operations.'}
        </div>
        <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
            <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider">Step-by-Step Solution</h4>
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
    const correctOpt = qData.options[qData.ans];
    return `
        <ol class="space-y-1.5 list-none pl-0">
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> Note the given group size and number of groups.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> Apply the appropriate multiplication or division relationship.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> Conclude that the correct answer is <strong>${correctOpt}</strong>.</li>
        </ol>
    `;
}

// ============================================================================
// Interactive Simulator Handlers (Simulators 1 to 16)
// ============================================================================

// Simulator 1: Animal Jump Multiples
let activeJumpStep = 3;
let activeJumpName = 'Frog';

function setJumpAnimal(step, name) {
    playClickSfx();
    activeJumpStep = step;
    activeJumpName = name;
    document.querySelectorAll('.ja-btn').forEach(b => {
        b.className = 'ja-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`ja-btn-${step}`);
    if (btn) btn.className = 'ja-btn px-2.5 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';
    
    const slider = document.getElementById('jumpSlider');
    if (slider) updateAnimalJumps(slider.value);
}

function updateAnimalJumps(jumps) {
    const count = parseInt(jumps);
    const label = document.getElementById('jumpCountLabel');
    const formula = document.getElementById('jumpFormulaLabel');
    const container = document.getElementById('trailMarkersContainer');
    const desc = document.getElementById('jumpDescCard');
    if (!label || !formula || !container || !desc) return;

    const totalPos = count * activeJumpStep;
    label.innerText = `${count} Jumps`;
    formula.innerText = `${count} × ${activeJumpStep} = Step ${totalPos}`;

    let html = '';
    for (let i = 1; i <= 8; i++) {
        const stepNum = i * activeJumpStep;
        const isCurrent = i === count;
        const isPast = i <= count;
        const bg = isCurrent ? 'bg-emerald-500 text-slate-950 font-black ring-2 ring-emerald-300 scale-105' : 
                   isPast ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-600' : 'bg-slate-900 text-slate-500 border border-slate-800';
        html += `
            <div class="px-2.5 py-2 rounded-lg text-xs text-center flex flex-col items-center justify-center transition-all ${bg}">
                <span class="text-[9px] text-slate-400">#${i}</span>
                <span class="font-mono text-sm">${stepNum}</span>
            </div>
        `;
    }
    container.innerHTML = html;
    desc.innerHTML = `<strong>${activeJumpName} Multiples:</strong> After ${count} jumps of ${activeJumpStep} steps, the ${activeJumpName.toLowerCase()} lands on <strong>Step ${totalPos}</strong>!`;
}

// Simulator 2: Target Step Paths
function setTargetMilestone(num) {
    playClickSfx();
    document.querySelectorAll('.tm-btn').forEach(b => {
        b.className = 'tm-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'tm-btn px-2.5 py-1 rounded-lg bg-teal-500 text-slate-950 text-xs font-bold shadow';

    const activeNum = document.getElementById('activeTargetNum');
    if (activeNum) activeNum.innerText = num;

    const animals = [
        { id: 'reach-frog', name: 'Frog (3)', step: 3 },
        { id: 'reach-squirrel', name: 'Squirrel (4)', step: 4 },
        { id: 'reach-rabbit', name: 'Rabbit (6)', step: 6 },
        { id: 'reach-kangaroo', name: 'Kangaroo (8)', step: 8 }
    ];

    animals.forEach(a => {
        const el = document.getElementById(a.id);
        if (!el) return;
        const q = Math.floor(num / a.step);
        const rem = num % a.step;
        if (rem === 0) {
            el.innerHTML = `
                <span class="block text-slate-400 text-[10px]">${a.name}</span>
                <strong class="text-emerald-400 text-sm">${q} Jumps</strong>
                <span class="block text-[10px] text-slate-500">${num} ÷ ${a.step} = ${q} (Exact)</span>
            `;
        } else {
            const before = q * a.step;
            const after = (q + 1) * a.step;
            el.innerHTML = `
                <span class="block text-slate-400 text-[10px]">${a.name}</span>
                <strong class="text-rose-400 text-sm">Skips!</strong>
                <span class="block text-[10px] text-slate-500">Lands on ${before}, ${after}</span>
            `;
        }
    });

    const summary = document.getElementById('reachSummaryText');
    if (summary) {
        if (num === 67) {
            summary.innerHTML = '<strong>Milestone 67:</strong> 67 is not divisible by 3, 4, 6, or 8! ALL four animals skip milestone 67!';
        } else {
            summary.innerHTML = `<strong>Milestone ${num}:</strong> Check divisibility: exact divisions land directly on the stone; non-zero remainders skip past!`;
        }
    }
}

// Simulator 3: Shared Landing Numbers
function setSharedPair(pairKey) {
    playClickSfx();
    document.querySelectorAll('.sp-btn').forEach(b => {
        b.className = 'sp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'sp-btn px-2.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition';

    const lcmLabel = document.getElementById('lcmLabel');
    const display = document.getElementById('dualTrailDisplay');
    const list = document.getElementById('commonMultiplesList');
    if (!lcmLabel || !display || !list) return;

    if (pairKey === 'frog_squirrel') {
        lcmLabel.innerText = 'First Meeting: Step 12';
        list.innerHTML = '<strong>Shared Landing Stones:</strong> <span class="text-cyan-300 font-bold font-mono">12, 24, 36, 48</span> (Multiples of 12)';
        display.innerHTML = `
            <div class="flex items-center gap-2 text-[11px] text-emerald-400">
                <span class="w-16 font-semibold">Frog (3):</span>
                <span class="font-mono text-slate-300">3, 6, 9, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">12</strong>, 15, 18, 21, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">24</strong>, 27, 30, 33, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">36</strong>, 39, 42, 45, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">48</strong></span>
            </div>
            <div class="flex items-center gap-2 text-[11px] text-amber-400">
                <span class="w-16 font-semibold">Squirrel (4):</span>
                <span class="font-mono text-slate-300">4, 8, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">12</strong>, 16, 20, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">24</strong>, 28, 32, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">36</strong>, 40, 44, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">48</strong></span>
            </div>
        `;
    } else {
        lcmLabel.innerText = 'First Meeting: Step 24';
        list.innerHTML = '<strong>Shared Landing Stones:</strong> <span class="text-cyan-300 font-bold font-mono">24, 48, 72</span> (Multiples of 24)';
        display.innerHTML = `
            <div class="flex items-center gap-2 text-[11px] text-teal-400">
                <span class="w-20 font-semibold">Rabbit (6):</span>
                <span class="font-mono text-slate-300">6, 12, 18, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">24</strong>, 30, 36, 42, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">48</strong></span>
            </div>
            <div class="flex items-center gap-2 text-[11px] text-purple-400">
                <span class="w-20 font-semibold">Kangaroo (8):</span>
                <span class="font-mono text-slate-300">8, 16, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">24</strong>, 32, 40, <strong class="text-cyan-400 bg-cyan-950/60 px-1 rounded">48</strong></span>
            </div>
        `;
    }
}

// Simulator 4: Cat Rat Chase
let chaseTurn = 0;
let mousePos = 24;
let catPos = 12;

function advanceChaseTurn() {
    playClickSfx();
    if (chaseTurn >= 8 || mousePos >= 40) return;
    
    chaseTurn++;
    mousePos += 2;
    catPos += 3;
    updateChaseUI();
}

function resetChaseGame() {
    playClickSfx();
    chaseTurn = 0;
    mousePos = 24;
    catPos = 12;
    updateChaseUI();
}

function updateChaseUI() {
    const turnEl = document.getElementById('chaseTurnDisplay');
    const mouseEl = document.getElementById('mousePosDisplay');
    const catEl = document.getElementById('catPosDisplay');
    const alertEl = document.getElementById('chaseStatusAlert');
    const btn = document.getElementById('btnChaseAdvance');
    if (!turnEl || !mouseEl || !catEl || !alertEl) return;

    turnEl.innerText = chaseTurn;
    mouseEl.innerText = `Step ${mousePos}`;
    catEl.innerText = `Step ${catPos}`;

    if (mousePos >= 40) {
        alertEl.className = 'p-2.5 rounded-lg bg-emerald-950/70 border border-emerald-800 text-xs text-center text-emerald-300 font-bold';
        alertEl.innerHTML = '🎉 The mouse reached the safety hole at Step 40! Cat was only at Step 36. Mouse escaped safely!';
        if (btn) btn.disabled = true;
        playSuccessSfx();
    } else if (catPos >= mousePos) {
        alertEl.className = 'p-2.5 rounded-lg bg-rose-950/70 border border-rose-800 text-xs text-center text-rose-300 font-bold';
        alertEl.innerHTML = 'Cat caught the mouse!';
        if (btn) btn.disabled = true;
    } else {
        alertEl.className = 'p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-center text-slate-300 font-medium';
        alertEl.innerHTML = `Bound ${chaseTurn}: Mouse is at ${mousePos}, Cat is at ${catPos}. Mouse is ${mousePos - catPos} steps ahead!`;
        if (btn) btn.disabled = false;
    }
}

// Simulator 5: Grid Equation Hunt
const huntGridNumbers = [
    5, 6, 30, 4,
    7, 8, 56, 3,
    9, 4, 36, 12,
    24, 4, 6, 8
];
let huntSelected = [];
let huntFoundCount = 0;

function clickHuntCell(idx) {
    playClickSfx();
    if (huntSelected.includes(idx)) {
        huntSelected = huntSelected.filter(i => i !== idx);
    } else {
        if (huntSelected.length < 3) {
            huntSelected.push(idx);
        }
    }
    renderHuntGrid();
}

function renderHuntGrid() {
    const matrix = document.getElementById('huntGridMatrix');
    const text = document.getElementById('huntSelectedText');
    const msg = document.getElementById('huntFeedbackMsg');
    if (!matrix || !text || !msg) return;

    text.innerText = huntSelected.map(i => huntGridNumbers[i]).join(', ') || 'None';

    let html = '';
    huntGridNumbers.forEach((val, idx) => {
        const isSel = huntSelected.includes(idx);
        const bg = isSel ? 'bg-indigo-600 text-white font-black ring-2 ring-indigo-400' : 'bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800';
        html += `<button onclick="clickHuntCell(${idx})" class="p-3 rounded-lg text-xs font-mono font-bold transition ${bg}">${val}</button>`;
    });
    matrix.innerHTML = html;

    if (huntSelected.length === 3) {
        const nums = huntSelected.map(i => huntGridNumbers[i]);
        const a = nums[0], b = nums[1], c = nums[2];
        if (a * b === c) {
            msg.className = 'p-2 rounded-lg bg-emerald-950 border border-emerald-800 text-xs text-center text-emerald-300 font-bold';
            msg.innerText = `Valid Multiplication: ${a} × ${b} = ${c}!`;
            huntFoundCount++;
            document.getElementById('huntEquationsFound').innerText = huntFoundCount;
            playSuccessSfx();
        } else if (a / b === c) {
            msg.className = 'p-2 rounded-lg bg-emerald-950 border border-emerald-800 text-xs text-center text-emerald-300 font-bold';
            msg.innerText = `Valid Division: ${a} ÷ ${b} = ${c}!`;
            huntFoundCount++;
            document.getElementById('huntEquationsFound').innerText = huntFoundCount;
            playSuccessSfx();
        } else {
            msg.className = 'p-2 rounded-lg bg-rose-950 border border-rose-800 text-xs text-center text-rose-300 font-medium';
            msg.innerText = `Not an equation: [${nums.join(', ')}]. Try another triplet!`;
            playErrorSfx();
        }
    }
}

function resetHuntGrid() {
    huntSelected = [];
    huntFoundCount = 0;
    const foundEl = document.getElementById('huntEquationsFound');
    if (foundEl) foundEl.innerText = '0';
    renderHuntGrid();
}

// Simulator 6: Flower Petal Groups
let currentFlowerMode = 'lily';

function setFlowerMode(mode) {
    playClickSfx();
    currentFlowerMode = mode;
    document.querySelectorAll('.fm-btn').forEach(b => {
        b.className = 'fm-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'fm-btn px-3 py-1.5 rounded-xl bg-pink-500 text-slate-950 font-bold text-xs shadow transition';

    const slider = document.getElementById('flowerCountSlider');
    const sLabel = document.getElementById('flowerSliderLabel');
    if (slider && sLabel) {
        if (mode === 'lily') {
            sLabel.innerText = 'Number of Lily Blossoms (Multiplier):';
            slider.max = 15;
            slider.value = 12;
        } else {
            sLabel.innerText = 'Harvested Hibiscus Petals (Total Whole):';
            slider.max = 50;
            slider.step = 5;
            slider.value = 35;
        }
        updateFlowerMath(slider.value);
    }
}

function updateFlowerMath(val) {
    const num = parseInt(val);
    const sVal = document.getElementById('flowerSliderVal');
    const mult = document.getElementById('termMultiplier');
    const cand = document.getElementById('termMultiplicand');
    const prod = document.getElementById('termProduct');
    const note = document.getElementById('flowerExplNote');
    if (!sVal || !mult || !cand || !prod || !note) return;

    if (currentFlowerMode === 'lily') {
        sVal.innerText = `${num} Flowers`;
        mult.innerText = `${num}`;
        cand.innerText = '6';
        const total = num * 6;
        prod.innerText = `${total}`;
        note.innerHTML = `<strong>Multiplication:</strong> Multiplier (${num} flowers) × Multiplicand (6 petals) = Product (<strong>${total} petals</strong>).`;
    } else {
        sVal.innerText = `${num} Petals`;
        const flowers = num / 5;
        mult.innerText = `${num}`;
        cand.innerText = '5';
        prod.innerText = `${flowers}`;
        note.innerHTML = `<strong>Division:</strong> ${num} total petals ÷ 5 petals per flower = <strong>${flowers} hibiscus flowers</strong> harvested!`;
    }
}

// Simulator 7: Rectangular Planting Arrays
let arrayRows = 4;
let arrayCols = 6;

function updateArrayDimensions() {
    const rSlider = document.getElementById('arrayRowsSlider');
    const cSlider = document.getElementById('arrayColsSlider');
    const rLabel = document.getElementById('arrayRowsLabel');
    const cLabel = document.getElementById('arrayColsLabel');
    const formula = document.getElementById('arrayFormulaText');
    const grid = document.getElementById('seedlingGridContainer');
    if (!rSlider || !cSlider || !rLabel || !cLabel || !formula || !grid) return;

    arrayRows = parseInt(rSlider.value);
    arrayCols = parseInt(cSlider.value);
    rLabel.innerText = `${arrayRows} Rows`;
    cLabel.innerText = `${arrayCols} Columns`;

    const total = arrayRows * arrayCols;
    formula.innerText = `${arrayRows} Rows × ${arrayCols} Columns = ${total} Saplings`;

    let html = '';
    for (let r = 0; r < arrayRows; r++) {
        html += '<div class="flex gap-2">';
        for (let c = 0; c < arrayCols; c++) {
            html += '<span class="w-5 h-5 rounded-full bg-emerald-500 shadow-sm flex items-center justify-center text-[9px] text-slate-950 font-black">🌱</span>';
        }
        html += '</div>';
    }
    grid.innerHTML = html;
}

function rotateArray() {
    playClickSfx();
    const temp = arrayRows;
    arrayRows = arrayCols;
    arrayCols = temp;

    const rSlider = document.getElementById('arrayRowsSlider');
    const cSlider = document.getElementById('arrayColsSlider');
    if (rSlider && cSlider) {
        rSlider.value = arrayRows;
        cSlider.value = arrayCols;
    }
    updateArrayDimensions();
}

// Simulator 8: Doubling Magic Patterns
let magicVal = 3;

function doubleMagicNumber() {
    playClickSfx();
    magicVal = magicVal * 2;
    updateMagicDoubleUI();
}

function resetMagicDouble() {
    playClickSfx();
    magicVal = 3;
    updateMagicDoubleUI();
}

function updateMagicDoubleUI() {
    const numDisplay = document.getElementById('magicNumberDisplay');
    const formula = document.getElementById('magicFormulaText');
    const onesEl = document.getElementById('magicOnesDigit');
    const badge = document.getElementById('magicParityBadge');
    const nextEl = document.getElementById('magicNextDouble');
    if (!numDisplay || !formula || !onesEl || !badge || !nextEl) return;

    numDisplay.innerText = magicVal;
    formula.innerText = `Value: ${magicVal}`;
    const ones = magicVal % 10;
    onesEl.innerText = ones;

    const isEven = magicVal % 2 === 0;
    if (isEven) {
        badge.className = 'px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold';
        badge.innerText = 'EVEN';
    } else {
        badge.className = 'px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold';
        badge.innerText = 'ODD';
    }
    nextEl.innerText = magicVal * 2;
}

// Simulator 9: Table Grid Symmetry
function setGridSymmetryPair(r, c) {
    playClickSfx();
    const status = document.getElementById('gridSymmetryStatus');
    const note = document.getElementById('gridNoteText');
    if (!status || !note) return;

    const prod = r * c;
    status.innerText = `Row ${r} Col ${c} (${prod}) mirrors Row ${c} Col ${r} (${prod}) across the diagonal!`;
    note.innerHTML = `<strong>Commutative Symmetry:</strong> ${r} × ${c} = ${c} × ${r} = ${prod}. Symmetrical across the diagonal!`;
    renderMiniTable(r, c);
}

function toggleRow8Cycle() {
    playClickSfx();
    const status = document.getElementById('gridSymmetryStatus');
    const note = document.getElementById('gridNoteText');
    if (!status || !note) return;

    status.innerText = 'Row 8 Ones Digits: 8, 6, 4, 2, 0, 8, 6, 4, 2, 0';
    note.innerHTML = '<strong>Row 8 Pattern:</strong> Products end in a repeating sequence of even digits: 8, 6, 4, 2, 0.';
    renderMiniTable(8, 0, true);
}

function renderMiniTable(hiR, hiC, isRow8 = false) {
    const table = document.getElementById('miniTableGrid');
    if (!table) return;

    let html = '<thead><tr class="bg-slate-900"><th class="p-1 border border-slate-800">×</th>';
    for (let c = 1; c <= 8; c++) html += `<th class="p-1 border border-slate-800 text-slate-400">${c}</th>`;
    html += '</tr></thead><tbody>';

    for (let r = 1; r <= 8; r++) {
        html += `<tr><th class="p-1 border border-slate-800 text-slate-400 bg-slate-900">${r}</th>`;
        for (let c = 1; c <= 8; c++) {
            const val = r * c;
            let bg = 'bg-slate-950 text-slate-300';
            if (r === c) bg = 'bg-slate-800 text-slate-400'; // Diagonal
            if ((r === hiR && c === hiC) || (r === hiC && c === hiR)) bg = 'bg-sky-500 text-slate-950 font-black';
            if (isRow8 && r === 8) bg = 'bg-amber-500 text-slate-950 font-bold';
            html += `<td class="p-1 border border-slate-800 ${bg}">${val}</td>`;
        }
        html += '</tr>';
    }
    html += '</tbody>';
    table.innerHTML = html;
}

// Simulator 10: Scaling Tens Products
let activeVehicleWheels = 3;
let activeVehicleName = 'Tricycles';

function setScalingVehicle(wheels, name) {
    playClickSfx();
    activeVehicleWheels = wheels;
    activeVehicleName = name;
    document.querySelectorAll('.sv-btn').forEach(b => {
        b.className = 'sv-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold border border-slate-700 text-xs';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'sv-btn px-2.5 py-1 rounded-lg bg-blue-500 text-slate-950 font-bold text-xs shadow';

    const slider = document.getElementById('tensCountSlider');
    if (slider) updateTensFleetMath(slider.value);
}

function updateTensFleetMath(val) {
    const count = parseInt(val);
    const label = document.getElementById('tensFleetCountLabel');
    const base = document.getElementById('baseFactText');
    const scaled = document.getElementById('scaledProductText');
    if (!label || !base || !scaled) return;

    label.innerText = `${count} ${activeVehicleName}`;
    const tens = count / 10;
    const baseProd = tens * activeVehicleWheels;
    const totalWheels = count * activeVehicleWheels;

    base.innerText = `${tens} × ${activeVehicleWheels} = ${baseProd}`;
    scaled.innerText = `${count} × ${activeVehicleWheels} = ${totalWheels}`;
}

// Simulator 11: Tens Breakdown Area
function setBreakdownProblem(num, mult, title) {
    playClickSfx();
    document.querySelectorAll('.bp-btn').forEach(b => {
        b.className = 'bp-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'bp-btn px-3 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs shadow';

    const heading = document.getElementById('breakdownHeading');
    const sumEl = document.getElementById('breakdownFinalSum');
    const tensLabel = document.getElementById('tensLabel');
    const tensVal = document.getElementById('tensVal');
    const onesLabel = document.getElementById('onesLabel');
    const onesVal = document.getElementById('onesVal');
    if (!heading || !sumEl || !tensLabel || !tensVal || !onesLabel || !onesVal) return;

    const tensPart = Math.floor(num / 10) * 10;
    const onesPart = num % 10;
    const p1 = tensPart * mult;
    const p2 = onesPart * mult;
    const total = p1 + p2;

    heading.innerText = `${num} × ${mult} = (${tensPart} + ${onesPart}) × ${mult}`;
    sumEl.innerText = `${p1} + ${p2} = ${total}`;
    tensLabel.innerText = `${tensPart} × ${mult}`;
    tensVal.innerText = `${p1}`;
    onesLabel.innerText = `${onesPart} × ${mult}`;
    onesVal.innerText = `${p2}`;
}

// Simulator 12: Animal Leg Counts
function updateAnimalLegsMath() {
    const gSlider = document.getElementById('geeseSlider');
    const sSlider = document.getElementById('sheepSlider');
    const gLabel = document.getElementById('geeseCountLabel');
    const sLabel = document.getElementById('sheepCountLabel');
    const gText = document.getElementById('geeseLegsText');
    const sText = document.getElementById('sheepLegsText');
    const totalText = document.getElementById('totalAnimalLegsText');
    if (!gSlider || !sSlider || !gLabel || !sLabel || !gText || !sText || !totalText) return;

    const geese = parseInt(gSlider.value);
    const sheep = parseInt(sSlider.value);
    gLabel.innerText = `${geese} Geese`;
    sLabel.innerText = `${sheep} Sheep`;

    const gLegs = geese * 2;
    const sLegs = sheep * 4;
    const totalLegs = gLegs + sLegs;

    gText.innerText = `${geese} × 2 = ${gLegs}`;
    sText.innerText = `${sheep} × 4 = ${sLegs}`;
    totalText.innerText = `${gLegs} + ${sLegs} = ${totalLegs} Legs`;
}

// Simulator 13: Partial Quotient Division
function setDivisionProblem(dividend, divisor, title) {
    playClickSfx();
    document.querySelectorAll('.dp-btn').forEach(b => {
        b.className = 'dp-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'dp-btn px-3 py-1.5 rounded-xl bg-purple-500 text-slate-950 font-bold text-xs shadow';

    const label = document.getElementById('divProblemLabel');
    const res = document.getElementById('divQuotientResult');
    const steps = document.getElementById('chunkingStepsArea');
    if (!label || !res || !steps) return;

    const quotient = dividend / divisor;
    label.innerText = `${dividend} Total ÷ ${divisor} per Group (${title})`;
    res.innerText = `Quotient: ${quotient}`;

    if (dividend === 48 && divisor === 3) {
        steps.innerHTML = `
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 1: 10 groups of 3 = 30</span>
                <span class="text-purple-300">48 - 30 = 18 left</span>
            </div>
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 2: 6 groups of 3 = 18</span>
                <span class="text-emerald-400">18 - 18 = 0 left!</span>
            </div>
            <div class="text-right text-purple-400 font-bold font-sans pt-1">
                Total Groups = 10 + 6 = 16
            </div>
        `;
    } else {
        steps.innerHTML = `
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 1: 10 groups of 4 = 40</span>
                <span class="text-purple-300">64 - 40 = 24 left</span>
            </div>
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 2: 6 groups of 4 = 24</span>
                <span class="text-emerald-400">24 - 24 = 0 left!</span>
            </div>
            <div class="text-right text-purple-400 font-bold font-sans pt-1">
                Total Tubes = 10 + 6 = 16
            </div>
        `;
    }
}

// Simulator 14: Scaling Hundreds Math
function setHundredsScenario(type) {
    playClickSfx();
    document.querySelectorAll('.hs-btn').forEach(b => {
        b.className = 'hs-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'hs-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow';

    const eq = document.getElementById('hundredsEquationLabel');
    const tot = document.getElementById('hundredsTotalLabel');
    const card = document.getElementById('hundredsBreakdownCard');
    if (!eq || !tot || !card) return;

    if (type === 'cars') {
        eq.innerText = '500 Cars × 4 Passengers';
        tot.innerText = '2,000 Passengers';
        card.innerHTML = `
            <div>Base Fact: <strong>5 × 4 = 20</strong></div>
            <div>Scale by 100: <strong>20 hundreds = 2,000</strong></div>
        `;
    } else if (type === 'bus') {
        eq.innerText = '8 Shuttles × 125 Passengers';
        tot.innerText = '1,000 Passengers';
        card.innerHTML = `
            <div>Expanded: <strong>(100 × 8) + (20 × 8) + (5 × 8)</strong></div>
            <div>Partial Sums: <strong>800 + 160 + 40 = 1,000</strong></div>
        `;
    } else if (type === 'cups') {
        eq.innerText = '6 Crates × 174 Cups';
        tot.innerText = '1,044 Cups';
        card.innerHTML = `
            <div>Expanded: <strong>(100 × 6) + (70 × 6) + (4 × 6)</strong></div>
            <div>Partial Sums: <strong>600 + 420 + 24 = 1,044</strong></div>
        `;
    }
}

// Simulator 15: Sharing Measure Division
function setDivType(type) {
    playClickSfx();
    document.querySelectorAll('.dt-btn').forEach(b => {
        b.className = 'dt-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'dt-btn px-3 py-1.5 rounded-xl bg-pink-500 text-slate-950 font-bold text-xs shadow';

    const title = document.getElementById('divConceptTitle');
    const formula = document.getElementById('divConceptFormula');
    const desc = document.getElementById('divConceptDesc');
    const icons = document.getElementById('divVisualIcons');
    if (!title || !formula || !desc || !icons) return;

    if (type === 'sharing') {
        title.innerText = '72 People Shared Across 9 Boats';
        formula.innerText = '72 ÷ 9 = 8 per boat';
        desc.innerHTML = '<strong>Sharing (Partitive):</strong> Number of boats (9) is known. Division finds each boat\'s passenger capacity: 8 travelers per boat.';
        let h = '';
        for (let i = 1; i <= 9; i++) {
            h += `<div class="px-2 py-1 bg-slate-800 rounded text-[10px] text-pink-300 font-bold">🛶 Boat #${i}: 8 pax</div>`;
        }
        icons.innerHTML = h;
    } else {
        title.innerText = '48 Tires Fitted (6 Tires Per Truck)';
        formula.innerText = '48 ÷ 6 = 8 trucks';
        desc.innerHTML = '<strong>Measurement (Quotative):</strong> Group size (6 tires/truck) is known. Division finds how many trucks can be equipped: 8 trucks total.';
        let h = '';
        for (let i = 1; i <= 8; i++) {
            h += `<div class="px-2 py-1 bg-slate-800 rounded text-[10px] text-sky-300 font-bold">🚛 Truck #${i}: 6 tires</div>`;
        }
        icons.innerHTML = h;
    }
}

// Simulator 16: Logical Reasoning Statements
function setLogicClaim(claimId) {
    playClickSfx();
    document.querySelectorAll('.lc-btn').forEach(b => {
        b.className = 'lc-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'lc-btn p-2 rounded-xl bg-emerald-500 text-slate-950 font-bold shadow';

    const stmt = document.getElementById('logicStatementText');
    const badge = document.getElementById('logicVerdictBadge');
    const proof = document.getElementById('logicProofText');
    if (!stmt || !badge || !proof) return;

    if (claimId === 1) {
        stmt.innerText = 'The product of any two even numbers is always even.';
        badge.className = 'px-3 py-1 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 font-bold';
        badge.innerText = 'ALWAYS TRUE';
        proof.innerHTML = 'Testing: 2 × 4 = 8 (Even), 6 × 8 = 48 (Even). Even numbers have a factor of 2, so their product always contains a factor of 2.';
    } else if (claimId === 2) {
        stmt.innerText = 'Dividing a number by 2 always produces an even number.';
        badge.className = 'px-3 py-1 rounded-full bg-amber-950 text-amber-400 border border-amber-800 font-bold';
        badge.innerText = 'SOMETIMES TRUE';
        proof.innerHTML = 'Counterexample: 8 ÷ 2 = 4 (Even), but 10 ÷ 2 = 5 (Odd)! Since it fails for 10, the statement is only Sometimes True.';
    } else if (claimId === 3) {
        stmt.innerText = 'The product of two odd numbers is always even.';
        badge.className = 'px-3 py-1 rounded-full bg-rose-950 text-rose-400 border border-rose-800 font-bold';
        badge.innerText = 'NEVER TRUE';
        proof.innerHTML = 'Testing: 3 × 5 = 15 (Odd), 7 × 9 = 63 (Odd). Odd numbers contain no factor of 2, so their product is NEVER even!';
    }
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSlideSimulator(slideNum) {
    if (slideNum === 1) setJumpAnimal(3, 'Frog');
    else if (slideNum === 2) setTargetMilestone(60);
    else if (slideNum === 3) setSharedPair('frog_squirrel');
    else if (slideNum === 4) resetChaseGame();
    else if (slideNum === 5) renderHuntGrid();
    else if (slideNum === 6) setFlowerMode('lily');
    else if (slideNum === 7) updateArrayDimensions();
    else if (slideNum === 8) updateMagicDoubleUI();
    else if (slideNum === 9) setGridSymmetryPair(3, 7);
    else if (slideNum === 10) setScalingVehicle(3, 'Tricycles');
    else if (slideNum === 11) setBreakdownProblem(18, 4, 'Book Rack Screws');
    else if (slideNum === 12) updateAnimalLegsMath();
    else if (slideNum === 13) setDivisionProblem(48, 3, 'Rickshaw Wheels');
    else if (slideNum === 14) setHundredsScenario('cars');
    else if (slideNum === 15) setDivType('sharing');
    else if (slideNum === 16) setLogicClaim(1);
}

document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});
'''

# Write to .agents/class4_maths_ch9_js.js
js_path = os.path.join(os.path.dirname(__file__), "class4_maths_ch9_js.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

# Write to .agents/class4_maths_ch9_js.py
py_path = os.path.join(os.path.dirname(__file__), "class4_maths_ch9_js.py")
with open(py_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 9 JavaScript Engine"""\n\n')
    f.write("js_engine = r'''")
    f.write(js_code)
    f.write("'''\n")

print(f"Generated {js_path} and {py_path}")


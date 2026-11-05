# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 6: Measuring Length
Generates the complete JavaScript Engine for Chapter 6.
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
    const curNumEl = document.getElementById('currentSlideNum');
    if (curNumEl) curNumEl.innerText = currentSlide;
    
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
            <strong>Hint:</strong> ${qData.hint || 'Carefully note the measurement units and conversion factors.'}
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
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> Understand the measurement values and units given.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> Apply the standard relation: 1 metre = 100 centimetres.</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> Conclude that the correct answer is <strong>${correctOpt}</strong>.</li>
        </ol>
    `;
}

// ============================================================================
// Interactive Simulator Handlers (Simulators 1 to 16)
// ============================================================================

// Simulator 1: Stadiometer Height Measurement
function setStudentHeight(cm) {
    playClickSfx();
    const txt = document.getElementById('stadiometerText');
    const desc = document.getElementById('stadiometerDesc');
    const headpiece = document.getElementById('stadiometerHeadpiece');
    const studentHead = document.getElementById('studentHead');
    const studentBody = document.getElementById('studentBody');
    if (!txt || !desc || !headpiece || !studentHead || !studentBody) return;

    // Active button styling
    document.querySelectorAll('.h-btn').forEach(b => {
        if (b.innerText.includes(cm.toString())) {
            b.className = 'h-btn px-3 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs transition shadow';
        } else {
            b.className = 'h-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700';
        }
    });

    // Map cm (115 to 142) to Y coordinate
    // 150cm = y:30; 90cm = y:170 => slope = (170-30)/(90-150) = 140 / -60 = -2.333
    const headY = 170 - (cm - 90) * 2.333;
    headpiece.setAttribute('transform', `translate(0, ${headY - 67})`);
    studentHead.setAttribute('cy', headY + 18);
    studentBody.setAttribute('y', headY + 36);
    studentBody.setAttribute('height', 180 - (headY + 36));

    txt.innerText = `${cm} cm`;
    const metres = Math.floor(cm / 100);
    const remCm = cm % 100;
    desc.innerHTML = `Recorded height: <span class="text-teal-400 font-bold">${cm} cm</span> = <span class="text-amber-400 font-bold">${metres} metre ${remCm} centimetres</span>`;
}

// Simulator 2: 1-Metre Classroom Benchmark
function compareMetre(item) {
    playClickSfx();
    const group = document.getElementById('benchObjectGroup');
    const verdict = document.getElementById('benchVerdict');
    const desc = document.getElementById('benchDesc');
    if (!group || !verdict || !desc) return;

    document.querySelectorAll('.bench-btn').forEach(b => {
        b.className = 'bench-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700';
    });
    const activeBtn = document.getElementById(`btn-bench-${item}`);
    if (activeBtn) activeBtn.className = 'bench-btn px-2.5 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs transition shadow';

    if (item === 'door') {
        group.innerHTML = `
            <rect x="180" y="30" width="70" height="150" fill="#818cf8" fill-opacity="0.25" stroke="#818cf8" stroke-width="2" rx="4"/>
            <circle cx="235" cy="110" r="4" fill="#fbbf24"/>
            <line x1="160" y1="30" x2="160" y2="180" stroke="#a5b4fc" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="215" y="20" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Door Height: ~2 Metres</text>
        `;
        verdict.innerText = 'Greater than 1 m';
        desc.innerHTML = 'A classroom door measures about 2 metres, which is <span class="text-emerald-400 font-bold">longer than 1 metre</span>.';
    } else if (item === 'board') {
        group.innerHTML = `
            <rect x="150" y="50" width="160" height="90" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="2" rx="4"/>
            <text x="230" y="100" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Blackboard (~3 Metres)</text>
        `;
        verdict.innerText = 'Greater than 1 m';
        desc.innerHTML = 'The width of a blackboard is approximately 3 metres, which is <span class="text-emerald-400 font-bold">longer than 1 metre</span>.';
    } else if (item === 'table') {
        group.innerHTML = `
            <rect x="170" y="80" width="130" height="20" fill="#f59e0b" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2" rx="3"/>
            <line x1="180" y1="100" x2="180" y2="180" stroke="#d97706" stroke-width="4"/>
            <line x1="290" y1="100" x2="290" y2="180" stroke="#d97706" stroke-width="4"/>
            <text x="235" y="70" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Study Desk (~1 Metre)</text>
        `;
        verdict.innerText = 'Equal to 1 m';
        desc.innerHTML = 'A single classroom desk is approximately <span class="text-amber-400 font-bold">equal to 1 metre</span> in length.';
    } else if (item === 'duster') {
        group.innerHTML = `
            <rect x="200" y="150" width="60" height="30" fill="#f43f5e" fill-opacity="0.35" stroke="#f43f5e" stroke-width="2" rx="4"/>
            <text x="230" y="170" fill="#fda4af" font-size="10" font-weight="bold" text-anchor="middle">Duster (15 cm)</text>
        `;
        verdict.innerText = 'Less than 1 m';
        desc.innerHTML = 'A felt blackboard duster is only 15 cm, which is <span class="text-rose-400 font-bold">much less than 1 metre</span>.';
    }
}

// Simulator 3: Modular Fraction Ropes
function setRopeMode(mode) {
    playClickSfx();
    const group = document.getElementById('ropeSegmentsGroup');
    const desc = document.getElementById('ropeFractionDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.rope-btn').forEach(b => {
        b.className = 'rope-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700';
    });

    if (mode === 'half_half') {
        const btn = document.getElementById('btn-rope-1');
        if (btn) btn.className = 'rope-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs transition shadow';
        group.innerHTML = `
            <text x="20" y="45" fill="#34d399" font-size="10" font-weight="bold">Active Combined Rope:</text>
            <rect x="20" y="55" width="160" height="22" rx="4" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
            <text x="100" y="70" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">1/2 m (50 cm)</text>
            <rect x="180" y="55" width="160" height="22" rx="4" fill="#059669" fill-opacity="0.35" stroke="#059669" stroke-width="2"/>
            <text x="260" y="70" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">1/2 m (50 cm)</text>
            <circle cx="180" cy="66" r="5" fill="#f59e0b"/>
        `;
        desc.innerHTML = '<span class="text-emerald-400 font-bold">50 cm + 50 cm = 100 cm</span> = Exactly <span class="text-amber-400 font-bold">1 Metre</span>!';
    } else if (mode === 'quarter_quarter') {
        const btn = document.getElementById('btn-rope-2');
        if (btn) btn.className = 'rope-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs transition shadow';
        group.innerHTML = `
            <text x="20" y="45" fill="#38bdf8" font-size="10" font-weight="bold">Active Combined Rope:</text>
            <rect x="20" y="55" width="80" height="22" rx="4" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="2"/>
            <text x="60" y="70" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">1/4 m (25cm)</text>
            <rect x="100" y="55" width="80" height="22" rx="4" fill="#0369a1" fill-opacity="0.4" stroke="#0369a1" stroke-width="2"/>
            <text x="140" y="70" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">1/4 m (25cm)</text>
            <circle cx="100" cy="66" r="5" fill="#f59e0b"/>
        `;
        desc.innerHTML = '<span class="text-cyan-400 font-bold">25 cm + 25 cm = 50 cm</span> = Exactly <span class="text-amber-400 font-bold">Half a Metre (1/2 m)</span>!';
    } else if (mode === 'four_quarters') {
        const btn = document.getElementById('btn-rope-3');
        if (btn) btn.className = 'rope-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs transition shadow';
        group.innerHTML = `
            <text x="20" y="45" fill="#a855f7" font-size="10" font-weight="bold">Active Combined Rope:</text>
            <rect x="20" y="55" width="80" height="22" rx="3" fill="#9333ea" fill-opacity="0.35" stroke="#9333ea" stroke-width="1.5"/><text x="60" y="70" fill="#e9d5ff" font-size="9" text-anchor="middle">1/4 m</text>
            <rect x="100" y="55" width="80" height="22" rx="3" fill="#7e22ce" fill-opacity="0.35" stroke="#7e22ce" stroke-width="1.5"/><text x="140" y="70" fill="#e9d5ff" font-size="9" text-anchor="middle">1/4 m</text>
            <rect x="180" y="55" width="80" height="22" rx="3" fill="#9333ea" fill-opacity="0.35" stroke="#9333ea" stroke-width="1.5"/><text x="220" y="70" fill="#e9d5ff" font-size="9" text-anchor="middle">1/4 m</text>
            <rect x="260" y="55" width="80" height="22" rx="3" fill="#7e22ce" fill-opacity="0.35" stroke="#7e22ce" stroke-width="1.5"/><text x="300" y="70" fill="#e9d5ff" font-size="9" text-anchor="middle">1/4 m</text>
            <circle cx="100" cy="66" r="4" fill="#fbbf24"/><circle cx="180" cy="66" r="4" fill="#fbbf24"/><circle cx="260" cy="66" r="4" fill="#fbbf24"/>
        `;
        desc.innerHTML = '<span class="text-purple-400 font-bold">4 × 25 cm = 100 cm</span> = Exactly <span class="text-amber-400 font-bold">1 Whole Metre</span>!';
    } else if (mode === 'half_quarter') {
        const btn = document.getElementById('btn-rope-4');
        if (btn) btn.className = 'rope-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs transition shadow';
        group.innerHTML = `
            <text x="20" y="45" fill="#f59e0b" font-size="10" font-weight="bold">Active Combined Rope:</text>
            <rect x="20" y="55" width="160" height="22" rx="4" fill="#d97706" fill-opacity="0.35" stroke="#d97706" stroke-width="2"/>
            <text x="100" y="70" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">1/2 m (50 cm)</text>
            <rect x="180" y="55" width="80" height="22" rx="4" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="2"/>
            <text x="220" y="70" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">1/4 m (25 cm)</text>
            <circle cx="180" cy="66" r="5" fill="#fbbf24"/>
        `;
        desc.innerHTML = '<span class="text-amber-400 font-bold">50 cm + 25 cm = 75 cm</span> = Exactly <span class="text-cyan-400 font-bold">Three-Quarters of a Metre (3/4 m)</span>!';
    }
}

// Simulator 4: Walking & Jumping Lines
function setWalkDistance(m) {
    playClickSfx();
    const fpGroup = document.getElementById('footprintsGroup');
    const dimText = document.getElementById('walkTrackDimText');
    const desc = document.getElementById('walkTrackDesc');
    if (!fpGroup || !dimText || !desc) return;

    document.querySelectorAll('.walk-btn').forEach(b => {
        b.className = 'walk-btn px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-walk-${m}m`);
    if (btn) btn.className = 'walk-btn px-3.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition';

    dimText.innerText = `Total Distance: ${m} Metres`;

    if (m === 1) {
        fpGroup.innerHTML = `
            <circle cx="180" cy="85" r="9" fill="#06b6d4" fill-opacity="0.85"/>
            <text x="180" y="88" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">1 pace</text>
        `;
        desc.innerHTML = '1 metre equals approximately <span class="text-cyan-400 font-bold">1 large adult step</span> or 2 small children paces.';
    } else if (m === 5) {
        let dots = '';
        for (let i = 1; i <= 5; i++) {
            const cx = 30 + i * 60;
            dots += `<circle cx="${cx}" cy="85" r="7" fill="#06b6d4" fill-opacity="0.8"/><text x="${cx}" y="88" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">${i}</text>`;
        }
        fpGroup.innerHTML = dots;
        desc.innerHTML = 'Covering 5 metres requires about <span class="text-cyan-400 font-bold">5 large steps (1m each)</span> or 10 normal paces (50cm each).';
    } else if (m === 10) {
        let dots = '';
        for (let i = 1; i <= 10; i++) {
            const cx = 30 + i * 30;
            dots += `<circle cx="${cx}" cy="85" r="5" fill="#06b6d4" fill-opacity="0.8"/><text x="${cx}" y="88" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">${i}</text>`;
        }
        fpGroup.innerHTML = dots;
        desc.innerHTML = 'A 10-metre corridor line takes about <span class="text-cyan-400 font-bold">10 giant strides</span> or 20 ordinary walking steps!';
    }
}

// Simulator 5: Long Jump Sand Pit
function triggerJump(cm) {
    playSuccessSfx();
    const traj = document.getElementById('jumpTrajectory');
    const sandDent = document.getElementById('sandDent');
    const landingGroup = document.getElementById('landingMarkGroup');
    const tape = document.getElementById('jumpTape');
    const tapeEnd = document.getElementById('jumpTapeEnd');
    const tapeText = document.getElementById('jumpTapeText');
    const desc = document.getElementById('longJumpDesc');
    if (!traj || !sandDent || !landingGroup || !tape || !tapeEnd || !tapeText || !desc) return;

    document.querySelectorAll('.jump-btn').forEach(b => {
        b.className = 'jump-btn px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition';
    });
    event.currentTarget.className = 'jump-btn px-3 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow transition';

    // Map cm (120 to 210) to X pixel coordinate: 48 + (cm/240)*280
    const landX = 48 + (cm / 240) * 280;
    const midX = (48 + landX) / 2;

    traj.setAttribute('d', `M 48 95 Q ${midX} 15 ${landX} 100`);
    sandDent.setAttribute('cx', landX);
    const label = landingGroup.querySelector('text');
    if (label) label.setAttribute('x', landX);

    tape.setAttribute('x2', landX);
    tapeEnd.setAttribute('cx', landX);
    tapeText.setAttribute('x', (48 + landX) / 2);

    const m = Math.floor(cm / 100);
    const rem = cm % 100;
    tapeText.innerText = `${m} m ${rem} cm`;
    desc.innerHTML = `Recorded jump: <span class="text-orange-400 font-bold">${m} m ${rem} cm</span> = <span class="text-yellow-300 font-bold">${cm} centimetres</span> total distance!`;
}

// Simulator 6: Animal Length Scales
function selectAnimalScale(animal) {
    playClickSfx();
    const group = document.getElementById('animalGraphicGroup');
    const desc = document.getElementById('animalScaleDesc');
    if (!group || !desc) return;

    document.querySelectorAll('.scale-btn').forEach(b => {
        b.className = 'scale-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-scale-${animal}`);
    if (btn) btn.className = 'scale-btn px-2.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs transition shadow';

    if (animal === 'whale') {
        group.innerHTML = `
            <rect x="20" y="60" width="320" height="50" rx="25" fill="#3b82f6" fill-opacity="0.35" stroke="#3b82f6" stroke-width="2"/>
            <circle cx="315" cy="80" r="3" fill="#ffffff"/>
            <path d="M 20 85 L 10 70 L 10 100 Z" fill="#3b82f6"/>
            <text x="180" y="90" fill="#bfdbfe" font-size="13" font-weight="bold" text-anchor="middle">Blue Whale: 30 Metres Long</text>
        `;
        desc.innerHTML = 'A gigantic Blue Whale spans <span class="text-blue-400 font-bold">30 metres</span>, equivalent to three 10-metre buses parked end-to-end!';
    } else if (animal === 'bus') {
        group.innerHTML = `
            <rect x="20" y="70" width="107" height="40" rx="6" fill="#f59e0b" fill-opacity="0.35" stroke="#f59e0b" stroke-width="2"/>
            <circle cx="45" cy="110" r="6" fill="#1e293b"/>
            <circle cx="105" cy="110" r="6" fill="#1e293b"/>
            <text x="73" y="94" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Bus (10m)</text>
        `;
        desc.innerHTML = 'A full-size school bus is roughly <span class="text-amber-400 font-bold">10 metres</span> long.';
    } else if (animal === 'croc') {
        group.innerHTML = `
            <rect x="20" y="75" width="43" height="25" rx="5" fill="#10b981" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
            <text x="41" y="92" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">Croc (4m)</text>
        `;
        desc.innerHTML = 'An adult saltwater crocodile grows up to <span class="text-emerald-400 font-bold">4 metres</span> long.';
    } else if (animal === 'ostrich') {
        group.innerHTML = `
            <rect x="20" y="80" width="27" height="25" rx="4" fill="#ec4899" fill-opacity="0.4" stroke="#ec4899" stroke-width="1.5"/>
            <text x="33" y="96" fill="#fbcfe8" font-size="9" font-weight="bold" text-anchor="middle">2.5m</text>
        `;
        desc.innerHTML = 'A tall ostrich stands about <span class="text-pink-400 font-bold">2.5 metres</span> (250 cm) tall.';
    }
}

// Simulator 7: Length Ratio Puzzles
function setRatioPuzzle(type) {
    playClickSfx();
    const blocks = document.getElementById('ratioBlocksGroup');
    const mathText = document.getElementById('ratioMathText');
    const desc = document.getElementById('ratioPuzzleDesc');
    if (!blocks || !mathText || !desc) return;

    document.querySelectorAll('.ratio-btn').forEach(b => {
        b.className = 'ratio-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'ratio-btn px-2.5 py-1.5 rounded-xl bg-pink-600 text-white font-bold text-xs transition shadow';

    if (type === 'whale_bus') {
        blocks.innerHTML = `
            <rect x="20" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/><text x="70" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 1 (10m)</text>
            <rect x="130" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/><text x="180" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 2 (10m)</text>
            <rect x="240" y="90" width="100" height="35" rx="4" fill="#a855f7" fill-opacity="0.4" stroke="#a855f7" stroke-width="1.5"/><text x="290" y="112" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Bus 3 (10m)</text>
        `;
        mathText.innerText = '30 m ÷ 10 m = 3 Times';
        desc.innerHTML = 'A 30-metre blue whale is exactly <span class="text-pink-400 font-bold">3 times as long</span> as a 10-metre school bus!';
    } else if (type === 'bus_croc') {
        blocks.innerHTML = `
            <rect x="20" y="90" width="60" height="35" rx="4" fill="#06b6d4" fill-opacity="0.4" stroke="#06b6d4" stroke-width="1.5"/><text x="50" y="112" fill="#cffafe" font-size="9" text-anchor="middle">Desk (2m)</text>
            <rect x="85" y="90" width="60" height="35" rx="4" fill="#06b6d4" fill-opacity="0.4" stroke="#06b6d4" stroke-width="1.5"/><text x="115" y="112" fill="#cffafe" font-size="9" text-anchor="middle">Desk (2m)</text>
            <rect x="150" y="90" width="60" height="35" rx="4" fill="#06b6d4" fill-opacity="0.4" stroke="#06b6d4" stroke-width="1.5"/><text x="180" y="112" fill="#cffafe" font-size="9" text-anchor="middle">Desk (2m)</text>
            <rect x="215" y="90" width="60" height="35" rx="4" fill="#06b6d4" fill-opacity="0.4" stroke="#06b6d4" stroke-width="1.5"/><text x="245" y="112" fill="#cffafe" font-size="9" text-anchor="middle">Desk (2m)</text>
            <rect x="280" y="90" width="60" height="35" rx="4" fill="#06b6d4" fill-opacity="0.4" stroke="#06b6d4" stroke-width="1.5"/><text x="310" y="112" fill="#cffafe" font-size="9" text-anchor="middle">Desk (2m)</text>
        `;
        mathText.innerText = '10 m ÷ 2 m = 5 Times';
        desc.innerHTML = 'A 10-metre bus equals the length of <span class="text-cyan-400 font-bold">5 study desks (2m each)</span> placed end-to-end!';
    } else if (type === 'croc_cat') {
        blocks.innerHTML = `
            <rect x="20" y="90" width="75" height="35" rx="4" fill="#f59e0b" fill-opacity="0.4" stroke="#f59e0b" stroke-width="1.5"/><text x="57" y="112" fill="#fef08a" font-size="9" text-anchor="middle">50 cm</text>
            <rect x="100" y="90" width="75" height="35" rx="4" fill="#f59e0b" fill-opacity="0.4" stroke="#f59e0b" stroke-width="1.5"/><text x="137" y="112" fill="#fef08a" font-size="9" text-anchor="middle">50 cm</text>
            <rect x="180" y="90" width="75" height="35" rx="4" fill="#f59e0b" fill-opacity="0.4" stroke="#f59e0b" stroke-width="1.5"/><text x="217" y="112" fill="#fef08a" font-size="9" text-anchor="middle">50 cm</text>
            <rect x="260" y="90" width="75" height="35" rx="4" fill="#f59e0b" fill-opacity="0.4" stroke="#f59e0b" stroke-width="1.5"/><text x="297" y="112" fill="#fef08a" font-size="9" text-anchor="middle">50 cm</text>
        `;
        mathText.innerText = '200 cm ÷ 50 cm = 4 Times';
        desc.innerHTML = 'A 2-metre bench (200 cm) contains exactly <span class="text-amber-400 font-bold">4 half-metre sections (50 cm each)</span>!';
    }
}

// Simulator 8: Small Centimetre Units
function measureSmallItem(item) {
    playClickSfx();
    const itemGroup = document.getElementById('activeSmallItem');
    const desc = document.getElementById('rulerMeasureDesc');
    if (!itemGroup || !desc) return;

    document.querySelectorAll('.item-btn').forEach(b => {
        b.className = 'item-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-item-${item}`);
    if (btn) btn.className = 'item-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow';

    // 0 cm is at x=30. Each cm = 20px.
    if (item === 'eraser') {
        itemGroup.innerHTML = `
            <rect x="30" y="45" width="80" height="35" rx="5" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
            <text x="70" y="67" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Eraser</text>
            <line x1="30" y1="45" x2="30" y2="90" stroke="#0284c7" stroke-dasharray="2 2"/>
            <line x1="110" y1="45" x2="110" y2="90" stroke="#0284c7" stroke-dasharray="2 2"/>
        `;
        desc.innerHTML = 'Aligned from mark 0 to mark 4: <span class="text-amber-400 font-bold">Length = 4 centimetres (4 cm)</span>';
    } else if (item === 'sharpener') {
        itemGroup.innerHTML = `
            <rect x="30" y="45" width="60" height="35" rx="5" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
            <text x="60" y="67" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Sharpener</text>
            <line x1="30" y1="45" x2="30" y2="90" stroke="#e11d48" stroke-dasharray="2 2"/>
            <line x1="90" y1="45" x2="90" y2="90" stroke="#e11d48" stroke-dasharray="2 2"/>
        `;
        desc.innerHTML = 'Aligned from mark 0 to mark 3: <span class="text-rose-400 font-bold">Length = 3 centimetres (3 cm)</span>';
    } else if (item === 'pencil') {
        itemGroup.innerHTML = `
            <polygon points="30,62 50,52 270,52 270,72 50,72" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <polygon points="30,62 38,58 38,66" fill="#1e293b"/>
            <text x="160" y="66" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Lead Pencil (12 cm)</text>
            <line x1="30" y1="45" x2="30" y2="90" stroke="#059669" stroke-dasharray="2 2"/>
            <line x1="270" y1="45" x2="270" y2="90" stroke="#059669" stroke-dasharray="2 2"/>
        `;
        desc.innerHTML = 'Aligned from mark 0 to mark 12: <span class="text-emerald-400 font-bold">Length = 12 centimetres (12 cm)</span>';
    } else if (item === 'clip') {
        itemGroup.innerHTML = `
            <rect x="30" y="50" width="100" height="25" rx="12" fill="none" stroke="#a855f7" stroke-width="4"/>
            <rect x="45" y="56" width="70" height="13" rx="6" fill="none" stroke="#a855f7" stroke-width="2.5"/>
            <line x1="30" y1="45" x2="30" y2="90" stroke="#a855f7" stroke-dasharray="2 2"/>
            <line x1="130" y1="45" x2="130" y2="90" stroke="#a855f7" stroke-dasharray="2 2"/>
        `;
        desc.innerHTML = 'Aligned from mark 0 to mark 5: <span class="text-purple-400 font-bold">Length = 5 centimetres (5 cm)</span>';
    }
}

// Simulator 9: Metre Scale Division
function setMetreDivision(mode) {
    playClickSfx();
    const box = document.getElementById('metreHighlightBox');
    const text = document.getElementById('metreDivisionText');
    const desc = document.getElementById('metreDivisionDesc');
    const bracket = document.getElementById('metreBracket');
    if (!box || !text || !desc || !bracket) return;

    document.querySelectorAll('.div-btn').forEach(b => {
        b.className = 'div-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });

    if (mode === 'full') {
        const btn = document.getElementById('btn-div-full');
        if (btn) btn.className = 'div-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';
        box.setAttribute('width', '320');
        bracket.setAttribute('d', 'M 20 115 L 20 125 L 180 125 L 180 135 L 180 125 L 340 125 L 340 115');
        text.setAttribute('x', '180');
        text.innerText = '100 cm = 1 Metre';
        desc.innerHTML = 'A standard metre stick contains exactly <span class="text-emerald-400 font-bold">100 centimetres</span>.';
    } else if (mode === 'half') {
        const btn = document.getElementById('btn-div-half');
        if (btn) btn.className = 'div-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';
        box.setAttribute('width', '160');
        bracket.setAttribute('d', 'M 20 115 L 20 125 L 100 125 L 100 135 L 100 125 L 180 125 L 180 115');
        text.setAttribute('x', '100');
        text.innerText = '50 cm = 1/2 Metre';
        desc.innerHTML = 'Half of 100 centimetres is <span class="text-emerald-400 font-bold">50 centimetres (1/2 metre)</span>.';
    } else if (mode === 'quarter') {
        const btn = document.getElementById('btn-div-quarter');
        if (btn) btn.className = 'div-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';
        box.setAttribute('width', '80');
        bracket.setAttribute('d', 'M 20 115 L 20 125 L 60 125 L 60 135 L 60 125 L 100 125 L 100 115');
        text.setAttribute('x', '60');
        text.innerText = '25 cm = 1/4 Metre';
        desc.innerHTML = 'One quarter of 100 centimetres is <span class="text-emerald-400 font-bold">25 centimetres (1/4 metre)</span>.';
    } else if (mode === 'three_quarter') {
        const btn = document.getElementById('btn-div-three');
        if (btn) btn.className = 'div-btn px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition';
        box.setAttribute('width', '240');
        bracket.setAttribute('d', 'M 20 115 L 20 125 L 140 125 L 140 135 L 140 125 L 260 125 L 260 115');
        text.setAttribute('x', '140');
        text.innerText = '75 cm = 3/4 Metre';
        desc.innerHTML = 'Three quarters of 100 centimetres equals <span class="text-emerald-400 font-bold">75 centimetres (3/4 metre)</span>.';
    }
}

// Simulator 10: Estimation vs Measurement
function setEstItem(item) {
    playClickSfx();
    const estBar = document.getElementById('estBar');
    const actBar = document.getElementById('actBar');
    const estVal = document.getElementById('estValText');
    const actVal = document.getElementById('actValText');
    const diff = document.getElementById('diffCalloutText');
    const desc = document.getElementById('estMeasureDesc');
    if (!estBar || !actBar || !estVal || !actVal || !diff || !desc) return;

    document.querySelectorAll('.est-btn').forEach(b => {
        b.className = 'est-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-est-${item}`);
    if (btn) btn.className = 'est-btn px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow';

    let est = 25, act = 28, name = 'Math Book';
    if (item === 'bottle') { est = 20; act = 23; name = 'Water Bottle'; }
    else if (item === 'box') { est = 18; act = 19; name = 'Pencil Box'; }
    else if (item === 'handspan') { est = 12; act = 15; name = 'Hand Span'; }

    estBar.setAttribute('width', (est * 6.5).toString());
    actBar.setAttribute('width', (act * 6.5).toString());
    estVal.setAttribute('x', (35 + est * 6.5).toString());
    estVal.innerText = `${est} cm`;
    actVal.setAttribute('x', (35 + act * 6.5).toString());
    actVal.innerText = `${act} cm`;

    const err = Math.abs(act - est);
    diff.innerText = `Estimation Error: ${err} cm (${name})`;
    desc.innerHTML = `Your visual guess: <strong>${est} cm</strong>. Actual measurement: <strong>${act} cm</strong>. Difference is only <span class="text-emerald-400 font-bold">${err} cm</span>!`;
}

// Simulator 11: Toy Car Ramp Distance
function launchCar(surface) {
    playSuccessSfx();
    const car = document.getElementById('toyCarGraphic');
    const line = document.getElementById('carDistanceLine');
    const lineEnd = document.getElementById('carDistanceLineEnd');
    const text = document.getElementById('carDistanceText');
    const desc = document.getElementById('carRampDesc');
    if (!car || !line || !lineEnd || !text || !desc) return;

    document.querySelectorAll('.car-btn').forEach(b => {
        b.className = 'car-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-car-${surface}`);
    if (btn) btn.className = 'car-btn px-3 py-1.5 rounded-xl bg-red-500 text-white font-bold text-xs shadow transition';

    let dist = 95, speedName = 'smooth tiles';
    if (surface === 'wood') { dist = 65; speedName = 'a wooden board'; }
    else if (surface === 'carpet') { dist = 35; speedName = 'a rough carpet'; }

    // Map 0 to 150 cm onto runway (80 to 320 px => 240px span / 150cm = 1.6 px/cm)
    const targetX = 80 + dist * 1.6;
    car.setAttribute('transform', `translate(${targetX - 75}, 0)`);
    line.setAttribute('x2', targetX);
    lineEnd.setAttribute('cx', targetX);
    text.setAttribute('x', (80 + targetX) / 2);
    text.innerText = `Distance: ${dist} cm`;

    desc.innerHTML = `On ${speedName}, the toy car rolled <span class="text-red-400 font-bold">${dist} cm</span>!`;
}

// Simulator 12: Treasure Grid Routes
function selectGridRoute(route) {
    playClickSfx();
    const path = document.getElementById('gridRoutePath');
    const desc = document.getElementById('treasureGridDesc');
    if (!path || !desc) return;

    document.querySelectorAll('.grid-btn').forEach(b => {
        b.className = 'grid-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'grid-btn px-3 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow transition';

    if (route === 'routeA') {
        path.setAttribute('points', '60,115 150,115 150,55 300,55');
        desc.innerHTML = 'Route A (Direct): <span class="text-purple-400 font-bold">8 grid cm</span> = <span class="text-amber-400 font-bold">16 metres ground distance</span> (Scale: 1 cm = 2 m).';
    } else if (route === 'routeB') {
        path.setAttribute('points', '60,115 60,145 240,145 240,55 300,55');
        desc.innerHTML = 'Route B (Detour): <span class="text-purple-400 font-bold">12 grid cm</span> = <span class="text-amber-400 font-bold">24 metres ground distance</span>.';
    } else if (route === 'routeC') {
        path.setAttribute('points', '60,115 60,25 210,25 210,115 300,115 300,55');
        desc.innerHTML = 'Route C (Scenic): <span class="text-purple-400 font-bold">16 grid cm</span> = <span class="text-amber-400 font-bold">32 metres ground distance</span>.';
    }
}

// Simulator 13: Broken Ruler Challenges
function setBrokenCase(c) {
    playClickSfx();
    const objGroup = document.getElementById('brokenObjectGroup');
    const formula = document.getElementById('brokenFormulaText');
    const desc = document.getElementById('brokenRulerDesc');
    if (!objGroup || !formula || !desc) return;

    document.querySelectorAll('.broken-btn').forEach(b => {
        b.className = 'broken-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-broken-${c.toLowerCase().replace('case', '')}`);
    if (btn) btn.className = 'broken-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs transition shadow';

    // 20px per cm. 0 is at 20px. Mark 3 = 80px, Mark 5 = 120px, Mark 7 = 160px
    if (c === 'caseA') {
        // Starts at 3 (80px), ends at 11 (240px) => 8cm (160px)
        objGroup.innerHTML = `
            <rect x="80" y="32" width="160" height="28" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
            <text x="160" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Blue Crayon</text>
            <line x1="80" y1="32" x2="80" y2="70" stroke="#0284c7" stroke-dasharray="2 2"/>
            <line x1="240" y1="32" x2="240" y2="70" stroke="#0284c7" stroke-dasharray="2 2"/>
        `;
        formula.innerText = 'Length = 11 cm - 3 cm = 8 cm';
        desc.innerHTML = 'Never read only the end point! Subtract: <span class="text-orange-400 font-bold">11 cm - 3 cm = 8 cm</span>.';
    } else if (c === 'caseB') {
        // Starts at 5 (120px), ends at 14 (300px) => 9cm (180px)
        objGroup.innerHTML = `
            <rect x="120" y="32" width="180" height="28" rx="4" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <text x="210" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Wooden Stick</text>
            <line x1="120" y1="32" x2="120" y2="70" stroke="#059669" stroke-dasharray="2 2"/>
            <line x1="300" y1="32" x2="300" y2="70" stroke="#059669" stroke-dasharray="2 2"/>
        `;
        formula.innerText = 'Length = 14 cm - 5 cm = 9 cm';
        desc.innerHTML = 'Subtracted initial reading: <span class="text-emerald-400 font-bold">14 cm - 5 cm = 9 cm</span>.';
    } else if (c === 'caseC') {
        // Starts at 7 (160px), ends at 13 (280px) => 6cm (120px)
        objGroup.innerHTML = `
            <rect x="160" y="32" width="120" height="28" rx="4" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
            <text x="220" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Strip of Paper</text>
            <line x1="160" y1="32" x2="160" y2="70" stroke="#e11d48" stroke-dasharray="2 2"/>
            <line x1="280" y1="32" x2="280" y2="70" stroke="#e11d48" stroke-dasharray="2 2"/>
        `;
        formula.innerText = 'Length = 13 cm - 7 cm = 6 cm';
        desc.innerHTML = 'Subtracted initial reading: <span class="text-rose-400 font-bold">13 cm - 7 cm = 6 cm</span>.';
    }
}

// Simulator 14: Sticker Border Math
function setCardBorder(l, w) {
    playClickSfx();
    const rect = document.getElementById('cardRect');
    const ribbon = document.getElementById('cardBorderRibbon');
    const dimLabel = document.getElementById('cardDimLabel');
    const topL = document.getElementById('cardTopLen');
    const botL = document.getElementById('cardBotLen');
    const leftL = document.getElementById('cardLeftLen');
    const rightL = document.getElementById('cardRightLen');
    const desc = document.getElementById('stickerBorderDesc');
    if (!rect || !ribbon || !dimLabel || !topL || !botL || !leftL || !rightL || !desc) return;

    document.querySelectorAll('.card-btn').forEach(b => {
        b.className = 'card-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'card-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold text-xs shadow transition';

    dimLabel.innerText = `${l} cm × ${w} cm`;
    topL.innerText = `${l} cm`;
    botL.innerText = `${l} cm`;
    leftL.innerText = `${w} cm`;
    rightL.innerText = `${w} cm`;

    const perimeter = 2 * (l + w);
    desc.innerHTML = `Total border ribbon: ${l} + ${w} + ${l} + ${w} = <span class="text-indigo-400 font-bold">${perimeter} cm of lace / ribbon needed</span>.`;
}

// Simulator 15: Metre-Centimetre Converter
function setWellDepth(m, cm) {
    playClickSfx();
    const rope = document.getElementById('wellRopeLine');
    const bucket = document.getElementById('wellBucket');
    const mPart = document.getElementById('convMetrePart');
    const cmPart = document.getElementById('convCmPart');
    const desc = document.getElementById('wellDepthDesc');
    if (!rope || !bucket || !mPart || !cmPart || !desc) return;

    document.querySelectorAll('.depth-btn').forEach(b => {
        b.className = 'depth-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'depth-btn px-2.5 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs transition shadow';

    // Map depth (2 to 8 m) to rope Y (50 to 115 px)
    const ropeY = 40 + (m / 8) * 75;
    rope.setAttribute('y2', ropeY);
    bucket.setAttribute('points', `93,${ropeY} 107,${ropeY} 104,${ropeY+17} 96,${ropeY+17}`);

    const totalCm = m * 100 + cm;
    const padCm = cm < 10 ? `0${cm}` : cm;
    mPart.innerText = `${m} m ${padCm} cm`;
    cmPart.innerText = `${totalCm} cm`;
    desc.innerHTML = `Rule: Multiply metres by 100 and add centimetres: <span class="text-teal-400 font-bold">(${m} × 100) + ${cm} = ${totalCm} cm</span>.`;
}

// Simulator 16: Fixed-Perimeter Vegetable Garden
function setGardenShape(l, w) {
    playClickSfx();
    const bed = document.getElementById('gardenBedRect');
    const topL = document.getElementById('gardenTopLabel');
    const sideL = document.getElementById('gardenSideLabel');
    const pText = document.getElementById('gardenPerimeterText');
    const desc = document.getElementById('gardenFenceDesc');
    if (!bed || !topL || !sideL || !pText || !desc) return;

    document.querySelectorAll('.garden-btn').forEach(b => {
        b.className = 'garden-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    event.currentTarget.className = 'garden-btn px-2.5 py-1.5 rounded-xl bg-green-500 text-slate-950 font-bold text-xs transition shadow';

    // Scale 1m = 25px. Center around (180, 80)
    const pixelW = l * 25;
    const pixelH = w * 22;
    const startX = 180 - pixelW / 2;
    const startY = 80 - pixelH / 2;

    bed.setAttribute('x', startX);
    bed.setAttribute('y', startY);
    bed.setAttribute('width', pixelW);
    bed.setAttribute('height', pixelH);

    topL.innerText = `Length: ${l} Metres`;
    topL.setAttribute('y', (startY - 10).toString());
    sideL.innerText = `Width: ${w}m`;
    sideL.setAttribute('x', (startX - 35).toString());
    sideL.setAttribute('y', (startY + pixelH / 2 + 4).toString());

    const area = l * w;
    pText.innerText = `Perimeter = ${l} + ${w} + ${l} + ${w} = 20 Metres`;
    desc.innerHTML = `Fixed perimeter: <span class="text-green-400 font-bold">20 metres of fence wire</span>! Garden area = <strong>${area} sq. metres</strong>.`;
}

// Initializer helper for each slide
function initSlideSimulator(slideId) {
    if (slideId === 1) setStudentHeight(128);
    else if (slideId === 2) compareMetre('door');
    else if (slideId === 3) setRopeMode('half_half');
    else if (slideId === 4) setWalkDistance(5);
    else if (slideId === 5) triggerJump(165);
    else if (slideId === 6) selectAnimalScale('whale');
    else if (slideId === 7) setRatioPuzzle('whale_bus');
    else if (slideId === 8) measureSmallItem('eraser');
    else if (slideId === 9) setMetreDivision('full');
    else if (slideId === 10) setEstItem('book');
    else if (slideId === 11) launchCar('smooth');
    else if (slideId === 12) selectGridRoute('routeA');
    else if (slideId === 13) setBrokenCase('caseA');
    else if (slideId === 14) setCardBorder(12, 8);
    else if (slideId === 15) setWellDepth(2, 45);
    else if (slideId === 16) setGardenShape(6, 4);
}

// Document ready bootstrap
document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});
'''

output_js = os.path.join(os.path.dirname(__file__), 'class4_maths_ch6_js.js')
with open(output_js, 'w', encoding='utf-8') as f:
    f.write(js_code)

output_py = os.path.join(os.path.dirname(__file__), 'class4_maths_ch6_js.py')
with open(output_py, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 6 JavaScript Engine"""\n\n')
    f.write(f"js_code = r'''{js_code}'''\n")

print(f"Generated {output_js} and {output_py}")


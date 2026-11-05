# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Generates the complete JavaScript Engine for Chapter 8.
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
            <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span class="text-xs font-bold text-amber-300">Listen Teacher Lecture</span>
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
            <strong>Hint:</strong> ${qData.hint || 'Carefully note standard metric conversions.'}
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
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> Note the question details and identifying units (kilograms, grams, litres, or millilitres).</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> Apply standard conversion identities (1 kg = 1000 g, 1 L = 1000 ml).</li>
            <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> Conclude that the correct answer is <strong>${correctOpt}</strong>.</li>
        </ol>
    `;
}

// ============================================================================
// Interactive Simulator Handlers (Simulators 1 to 16)
// ============================================================================

// Simulator 1: Market Weight Estimates
function setPumpkinMode(mode) {
    playClickSfx();
    const beam = document.getElementById('pumpkinBeamGroup');
    const leftLoad = document.getElementById('leftScaleLoad');
    const rightLoad = document.getElementById('rightScaleLoad');
    const statusText = document.getElementById('pumpkinSvgStatus');
    const descCard = document.getElementById('pumpkinDescCard');
    if (!beam || !leftLoad || !rightLoad || !statusText || !descCard) return;

    document.querySelectorAll('.pm-btn').forEach(b => {
        b.className = 'pm-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`btn-pm-${mode}`);
    if (btn) btn.className = 'pm-btn px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition';

    if (mode === 'half') {
        beam.setAttribute('transform', 'rotate(0, 180, 120)');
        leftLoad.innerHTML = `
            <path d="M 60 145 C 60 125, 100 125, 100 145 Z" fill="url(#pumpkinGrad)" stroke="#78350f" stroke-width="1.5"/>
            <rect x="78" y="122" width="4" height="6" fill="#15803d" rx="1"/>
            <text x="80" y="140" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Half 1kg</text>
        `;
        rightLoad.innerHTML = `
            <rect x="260" y="133" width="18" height="12" rx="2" fill="#64748b" stroke="#94a3b8"/>
            <text x="269" y="142" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">500g</text>
            <rect x="282" y="133" width="18" height="12" rx="2" fill="#64748b" stroke="#94a3b8"/>
            <text x="291" y="142" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">500g</text>
        `;
        statusText.textContent = 'Scale: Balanced (1 kg = 1000 g)';
        descCard.innerHTML = '<strong>Observation:</strong> The half pumpkin balances two 500 g metal counterweights (500 g + 500 g = 1000 g = 1 kg). Therefore, the whole pumpkin weighed 2 kg!';
    } else if (mode === 'whole') {
        beam.setAttribute('transform', 'rotate(0, 180, 120)');
        leftLoad.innerHTML = `
            <circle cx="80" cy="133" r="14" fill="url(#pumpkinGrad)" stroke="#78350f" stroke-width="1.5"/>
            <rect x="78" y="116" width="4" height="5" fill="#15803d" rx="1"/>
            <text x="80" y="136" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Whole 2kg</text>
        `;
        rightLoad.innerHTML = `
            <rect x="260" y="130" width="22" height="15" rx="2" fill="#475569" stroke="#94a3b8"/>
            <text x="271" y="141" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">1 kg</text>
            <rect x="285" y="130" width="22" height="15" rx="2" fill="#475569" stroke="#94a3b8"/>
            <text x="296" y="141" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">1 kg</text>
        `;
        statusText.textContent = 'Scale: Balanced (2 kg = 2000 g)';
        descCard.innerHTML = '<strong>Whole Pumpkin:</strong> Two 1 kg iron weights balance the entire uncut pumpkin. 1 kg + 1 kg = 2 kg total pumpkin mass!';
    } else if (mode === 'animals') {
        beam.setAttribute('transform', 'rotate(-10, 180, 120)');
        leftLoad.innerHTML = `
            <rect x="62" y="125" width="36" height="20" rx="4" fill="#ea580c"/>
            <text x="80" y="138" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Tiger 200kg</text>
        `;
        rightLoad.innerHTML = `
            <circle cx="280" cy="135" r="10" fill="url(#pumpkinGrad)"/>
            <text x="280" y="138" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">2kg</text>
        `;
        statusText.textContent = 'Tilts Left: Tiger is 100× Heavier!';
        descCard.innerHTML = '<strong>Animal Scale:</strong> A striped tiger weighs ~200 kg, which is 100 times heavier than a 2 kg pumpkin and 50 times heavier than a 4 kg domestic cat!';
    }
}

// Simulator 2: Kilograms And Grams
function setKgFraction(val) {
    playClickSfx();
    const slider = document.getElementById('massSlider');
    if (slider) {
        slider.value = val;
        updateMassSlider(val);
    }
}

function updateMassSlider(val) {
    const num = parseFloat(val);
    const grams = Math.round(num * 1000);
    const label = document.getElementById('sliderKgLabel');
    const fill = document.getElementById('fractionBarFill');
    const pctText = document.getElementById('fractionPctText');
    const info = document.getElementById('kgConversionInfo');
    if (!label || !fill || !pctText || !info) return;

    label.innerText = `${num.toFixed(2)} kg = ${grams} g`;
    const pct = Math.min(100, Math.round((num / 1.0) * 100));
    fill.style.width = `${pct}%`;
    fill.innerText = `${grams} g`;
    pctText.innerText = `${pct}% of 1 kg`;

    if (num === 0.25) {
        info.innerHTML = '<strong>One-Quarter Kilogram (1/4 kg):</strong> 1000 g ÷ 4 = 250 g. Common for spice powders and butter.';
    } else if (num === 0.5) {
        info.innerHTML = '<strong>One-Half Kilogram (1/2 kg):</strong> 1000 g ÷ 2 = 500 g. Two 500 g packets make a whole kilogram.';
    } else if (num === 0.75) {
        info.innerHTML = '<strong>Three-Quarter Kilogram (3/4 kg):</strong> 250 g × 3 = 750 g. Exactly three 250 g packets.';
    } else if (num >= 1.0) {
        info.innerHTML = `<strong>Full Kilogram Multiple:</strong> ${num.toFixed(2)} kg = ${grams} grams. Always multiply kilograms by 1000 to find grams!`;
    }
}

// Simulator 3: Balancing Beam Scales
let leftPanMass = 500;
let rightPanMass = 500;

function adjustPan(pan, delta) {
    playClickSfx();
    if (pan === 'left') {
        leftPanMass = Math.max(0, Math.min(2000, leftPanMass + delta));
    } else {
        rightPanMass = Math.max(0, Math.min(2000, rightPanMass + delta));
    }
    updateBeamScaleUI();
}

function clearPan(pan) {
    playClickSfx();
    if (pan === 'left') leftPanMass = 0;
    else rightPanMass = 0;
    updateBeamScaleUI();
}

function updateBeamScaleUI() {
    const leftText = document.getElementById('leftPanWeightDisplay');
    const rightText = document.getElementById('rightPanWeightDisplay');
    const svgLeft = document.getElementById('svgLeftPanMassText');
    const svgRight = document.getElementById('svgRightPanMassText');
    const beam = document.getElementById('dynamicBeamGroup');
    const readout = document.getElementById('beamScaleReadout');
    if (!leftText || !rightText || !svgLeft || !svgRight || !beam || !readout) return;

    leftText.innerText = leftPanMass;
    rightText.innerText = rightPanMass;
    svgLeft.textContent = `${leftPanMass}g`;
    svgRight.textContent = `${rightPanMass}g`;

    const diff = rightPanMass - leftPanMass;
    const angle = Math.max(-14, Math.min(14, diff / 40));
    beam.setAttribute('transform', `rotate(${angle}, 170, 80)`);

    if (diff === 0) {
        readout.textContent = 'EQUILIBRIUM: BALANCED';
        readout.setAttribute('fill', '#22c55e');
    } else if (diff < 0) {
        readout.textContent = `LEFT TILTS DOWN (+${Math.abs(diff)}g)`;
        readout.setAttribute('fill', '#38bdf8');
    } else {
        readout.textContent = `RIGHT TILTS DOWN (+${diff}g)`;
        readout.setAttribute('fill', '#f59e0b');
    }
}

// Simulator 4: Sweet Box Packaging
function setSweetBox(grams) {
    playClickSfx();
    document.querySelectorAll('.sb-btn').forEach(b => {
        b.className = 'sb-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700';
    });
    const active = document.getElementById(`sb-btn-${grams}`);
    if (active) active.className = 'sb-btn px-2.5 py-1 rounded-lg bg-purple-500 text-slate-950 text-xs font-bold shadow';

    const eq = document.getElementById('sweetEquation');
    const container = document.getElementById('sweetBoxContainer');
    if (!eq || !container) return;

    const count = 1000 / grams;
    eq.innerText = `1000 g ÷ ${grams} g = ${count} Boxes Needed`;

    let html = '';
    for (let i = 1; i <= count; i++) {
        html += `
            <div class="px-2 py-1.5 rounded-lg bg-purple-900/60 border border-purple-500/50 flex flex-col items-center justify-center text-[10px] text-purple-200 font-bold">
                <span>Box #${i}</span>
                <span class="text-[9px] text-purple-400 font-mono">${grams}g</span>
            </div>
        `;
    }
    container.innerHTML = html;
}

// Simulator 5: Object Weight Comparisons
let targetSpiceGrams = 10;
let currentErasers = 2;

function setSpiceTarget(grams) {
    playClickSfx();
    targetSpiceGrams = grams;
    document.querySelectorAll('.sp-btn').forEach(b => {
        b.className = 'sp-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700';
    });
    const btn = document.getElementById(`sp-btn-${grams}`);
    if (btn) btn.className = 'sp-btn px-2.5 py-1 rounded-lg bg-rose-500 text-slate-950 text-xs font-bold shadow';

    const label = document.getElementById('spicePanLabel');
    if (label) {
        if (grams === 10) label.innerText = '10g Turmeric';
        else if (grams === 20) label.innerText = '20g Saffron';
        else if (grams === 50) label.innerText = '50g Masala';
    }
    updateEraserComparison();
}

function addEraser(delta) {
    playClickSfx();
    currentErasers = Math.max(0, currentErasers + delta);
    updateEraserComparison();
}

function resetErasers() {
    playClickSfx();
    currentErasers = 0;
    updateEraserComparison();
}

function updateEraserComparison() {
    const countDisplay = document.getElementById('eraserCountDisplay');
    const eraserLabel = document.getElementById('eraserPanLabel');
    const status = document.getElementById('eraserMatchStatus');
    if (!countDisplay || !eraserLabel || !status) return;

    const eraserMass = currentErasers * 5;
    countDisplay.innerText = `${currentErasers}`;
    eraserLabel.innerText = `${currentErasers} Erasers (${eraserMass}g)`;

    if (eraserMass === targetSpiceGrams) {
        status.className = 'font-bold text-emerald-400';
        status.innerText = `PERFECT BALANCE (${currentErasers} × 5g = ${targetSpiceGrams}g)`;
        playSuccessSfx();
    } else if (eraserMass < targetSpiceGrams) {
        status.className = 'font-bold text-amber-400';
        status.innerText = `Lighter by ${targetSpiceGrams - eraserMass}g (Need more erasers)`;
    } else {
        status.className = 'font-bold text-rose-400';
        status.innerText = `Heavier by ${eraserMass - targetSpiceGrams}g (Remove erasers)`;
    }
}

// Simulator 6: Weighing Machine Types
function setScaleTab(tab) {
    playClickSfx();
    document.querySelectorAll('.st-btn').forEach(b => {
        b.className = 'st-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition';
    });
    const active = document.getElementById(`st-btn-${tab}`);
    if (active) active.className = 'st-btn p-2 rounded-xl bg-sky-500 text-slate-950 font-bold text-xs transition';

    const title = document.getElementById('scaleTitle');
    const usage = document.getElementById('scaleUsage');
    const desc = document.getElementById('scaleDesc');
    if (!title || !usage || !desc) return;

    if (tab === 'beam') {
        title.innerText = 'Beam Balance Scale';
        usage.innerText = 'Market Produce';
        desc.innerText = 'Compares loads directly against iron counterweights using mechanical gravitational equilibrium. Found across traditional market carts.';
    } else if (tab === 'spring') {
        title.innerText = 'Spring Balance Scale';
        usage.innerText = 'Hanging Loads & Cylinders';
        desc.innerText = 'Measures suspended weight via the physical stretch of an internal steel spring. Widely used for domestic gas cylinders and freight luggage.';
    } else if (tab === 'digital') {
        title.innerText = 'Digital Electronic Scale';
        usage.innerText = 'Sweets & Precision Spices';
        desc.innerText = 'Employs electronic strain sensors to show instant digital weight down to single grams. Used in sweet shops, grocery counters, and laboratories.';
    } else if (tab === 'platform') {
        title.innerText = 'Heavy Platform Scale';
        usage.innerText = 'Bulk Harvest & Freight Sacks';
        desc.innerText = 'Heavy cast-iron base platform capable of measuring heavy sacks of grain, wheat flour, and agricultural produce weighing up to 200 kg.';
    }
}

// Simulator 7: Heavy Load Multiples
let sackUnitKg = 25;
let sackQty = 4;

function setHeavySack(kg) {
    playClickSfx();
    sackUnitKg = kg;
    document.querySelectorAll('.hs-btn').forEach(b => {
        b.className = 'hs-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700';
    });
    const btn = document.getElementById(`hs-btn-${kg}`);
    if (btn) btn.className = 'hs-btn px-2.5 py-1 rounded-lg bg-orange-500 text-slate-950 text-xs font-bold shadow';
    updateHeavyCalculation();
}

function adjustSackCount(delta) {
    playClickSfx();
    sackQty = Math.max(1, Math.min(20, sackQty + delta));
    updateHeavyCalculation();
}

function updateHeavyCalculation() {
    const qtyDisplay = document.getElementById('sackCountDisplay');
    const totalDisplay = document.getElementById('heavyTotalDisplay');
    const benchmark = document.getElementById('heavyBenchmarkText');
    if (!qtyDisplay || !totalDisplay || !benchmark) return;

    const total = sackUnitKg * sackQty;
    qtyDisplay.innerText = sackQty;
    totalDisplay.innerText = `${total} kg`;

    const cylinders = (total / 14).toFixed(1);
    const dogs = (total / 25).toFixed(1);
    benchmark.innerText = `Equivalent to about ${cylinders} gas cylinders (14kg each) or ${dogs} medium dogs (25kg each).`;
}

// Simulator 8: Olympic Weightlifting Feat
function updateOlympicMath() {
    const bwSlider = document.getElementById('athleteWeightSlider');
    const liftSlider = document.getElementById('liftedWeightSlider');
    const bwLabel = document.getElementById('athleteWeightLabel');
    const liftLabel = document.getElementById('liftedWeightLabel');
    const ratioDisplay = document.getElementById('liftRatioDisplay');
    const expl = document.getElementById('liftRatioExplanation');
    if (!bwSlider || !liftSlider || !bwLabel || !liftLabel || !ratioDisplay || !expl) return;

    const bw = parseFloat(bwSlider.value);
    const lift = parseFloat(liftSlider.value);
    bwLabel.innerText = `${bw} kg`;
    liftLabel.innerText = `${lift} kg`;

    const ratio = (lift / bw).toFixed(2);
    ratioDisplay.innerText = `${ratio}×`;
    expl.innerText = `The athlete hoisted ${ratio} times her bodyweight! (${lift} kg ÷ ${bw} kg = ${ratio})`;
}

// Simulator 9: Litres And Millilitres
function setLiquidPreset(ml, name) {
    playClickSfx();
    const slider = document.getElementById('cylinderSlider');
    if (slider) {
        slider.value = ml;
        updateCylinderSlider(ml, name);
    }
}

function updateCylinderSlider(val, nameOverride) {
    const ml = parseInt(val);
    const label = document.getElementById('cylinderVolumeLabel');
    const fill = document.getElementById('liquidFillRect');
    const containerLabel = document.getElementById('containerNameLabel');
    const fractionLabel = document.getElementById('cylinderFractionLabel');
    if (!label || !fill || !containerLabel || !fractionLabel) return;

    label.innerText = `${ml} ml`;
    // Max height in SVG is 170px (from y=200 down to y=30)
    const fillHeight = (ml / 1000) * 170;
    const fillY = 200 - fillHeight;
    fill.setAttribute('y', fillY);
    fill.setAttribute('height', fillHeight);

    if (nameOverride) {
        containerLabel.innerText = nameOverride;
    } else {
        if (ml <= 150) containerLabel.innerText = 'Teacup';
        else if (ml <= 250) containerLabel.innerText = 'Glass Tumbler';
        else if (ml <= 500) containerLabel.innerText = 'Milk Pouch';
        else containerLabel.innerText = 'Reusable Bottle';
    }

    if (ml === 250) fractionLabel.innerText = '1/4 Litre (Quarter)';
    else if (ml === 500) fractionLabel.innerText = '1/2 Litre (Half)';
    else if (ml === 750) fractionLabel.innerText = '3/4 Litre (Three-Quarters)';
    else if (ml === 1000) fractionLabel.innerText = '1 Full Litre';
    else fractionLabel.innerText = `${(ml / 1000).toFixed(2)} Litres`;
}

// Simulator 10: Fractional Litre Measures
function setFractionLitre(ml) {
    playClickSfx();
    document.querySelectorAll('.fl-btn').forEach(b => {
        b.className = 'fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`fl-btn-${ml}`);
    if (btn) btn.className = 'fl-btn p-2 rounded-xl bg-teal-500 text-slate-950 font-bold shadow transition';

    const text = document.getElementById('activeFractionText');
    const activeBlocks = ml / 250;
    if (text) text.innerText = `${activeBlocks} of 4 Quarters Filled (${ml} ml)`;

    for (let i = 1; i <= 4; i++) {
        const blk = document.getElementById(`qblock-${i}`);
        if (!blk) continue;
        if (i <= activeBlocks) {
            blk.className = 'h-14 rounded-lg bg-teal-500 flex flex-col items-center justify-center text-slate-950 font-bold text-xs transition';
        } else {
            blk.className = 'h-14 rounded-lg bg-slate-800 border border-slate-700 flex flex-col items-center justify-center text-slate-400 font-bold text-xs transition';
        }
    }
}

// Simulator 11: Droppers And Spoons
let activeDispenserMl = 5;
let accumulatedDose = 5;

function setDispenser(ml, name) {
    playClickSfx();
    activeDispenserMl = ml;
    document.querySelectorAll('.md-btn').forEach(b => {
        b.className = 'md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition';
    });
    const clicked = event.currentTarget;
    if (clicked) clicked.className = 'md-btn p-2 rounded-xl bg-indigo-500 text-slate-950 font-bold shadow transition';
}

function addDose() {
    playClickSfx();
    accumulatedDose = Math.min(100, accumulatedDose + activeDispenserMl);
    updateMedicineBottleUI();
}

function resetDose() {
    playClickSfx();
    accumulatedDose = 0;
    updateMedicineBottleUI();
}

function updateMedicineBottleUI() {
    const totalDisplay = document.getElementById('totalDoseDisplay');
    const remainingLabel = document.getElementById('bottleRemainingLabel');
    const pbar = document.getElementById('bottleProgressBar');
    const daysLabel = document.getElementById('daysLastText');
    if (!totalDisplay || !remainingLabel || !pbar || !daysLabel) return;

    totalDisplay.innerText = `${accumulatedDose} ml`;
    const remaining = 100 - accumulatedDose;
    remainingLabel.innerText = `${remaining} ml remaining`;
    pbar.style.width = `${accumulatedDose}%`;

    const daysRemaining = (remaining / 10).toFixed(1);
    daysLabel.innerText = `At 10 ml/day dose, remaining syrup will last ${daysRemaining} days!`;
}

// Simulator 12: Perfumed Oil Bottles
function setOilBottleSize(ml) {
    playClickSfx();
    document.querySelectorAll('.ob-btn').forEach(b => {
        b.className = 'ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700';
    });
    const btn = document.getElementById(`ob-btn-${ml}`);
    if (btn) btn.className = 'ob-btn px-2.5 py-1 rounded-lg bg-pink-500 text-slate-950 text-xs font-bold shadow';

    const eq = document.getElementById('oilEquationText');
    const grid = document.getElementById('oilBottlesGrid');
    if (!eq || !grid) return;

    const count = 1000 / ml;
    eq.innerText = `1000 ml ÷ ${ml} ml = ${count} Bottles Filled`;

    let html = '';
    for (let i = 1; i <= count; i++) {
        html += `
            <div class="px-2 py-1.5 rounded-lg bg-pink-900/60 border border-pink-500/50 flex flex-col items-center justify-center text-[10px] text-pink-200 font-bold">
                <span>Vial #${i}</span>
                <span class="text-[9px] text-pink-400 font-mono">${ml}ml</span>
            </div>
        `;
    }
    grid.innerHTML = html;
}

// Simulator 13: Milk Measuring Cans
let milkOrderTarget = 750;
let totalMilkPoured = 0;

function setMilkOrder(target) {
    playClickSfx();
    milkOrderTarget = target;
    document.querySelectorAll('.mo-btn').forEach(b => {
        b.className = 'mo-btn px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 text-xs';
    });
    const active = document.getElementById(`mo-btn-${target}`);
    if (active) active.className = 'mo-btn px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs';
    updateMilkStatus();
}

function pourMilkScoop(ml) {
    playClickSfx();
    totalMilkPoured += ml;
    updateMilkStatus();
}

function resetMilkJug() {
    playClickSfx();
    totalMilkPoured = 0;
    updateMilkStatus();
}

function updateMilkStatus() {
    const totalEl = document.getElementById('pouredMilkTotal');
    const feedback = document.getElementById('milkPourFeedback');
    if (!totalEl || !feedback) return;

    totalEl.innerText = `${totalMilkPoured} ml`;

    if (totalMilkPoured === milkOrderTarget) {
        feedback.innerHTML = `<span class="text-emerald-400 font-bold">PERFECT MATCH! Measured exactly ${milkOrderTarget} ml!</span><button onclick="resetMilkJug()" class="text-[10px] text-slate-400 underline">Clear Jug</button>`;
        playSuccessSfx();
    } else if (totalMilkPoured < milkOrderTarget) {
        const diff = milkOrderTarget - totalMilkPoured;
        feedback.innerHTML = `<span>Target: ${milkOrderTarget} ml (Need ${diff} ml more)</span><button onclick="resetMilkJug()" class="text-[10px] text-slate-400 underline">Clear Jug</button>`;
    } else {
        const over = totalMilkPoured - milkOrderTarget;
        feedback.innerHTML = `<span class="text-rose-400 font-bold">Overfilled by ${over} ml!</span><button onclick="resetMilkJug()" class="text-[10px] text-slate-400 underline">Clear Jug</button>`;
    }
}

// Simulator 15: Leaking Tap Investigation
function setLeakTime(timeframe) {
    playClickSfx();
    document.querySelectorAll('.lt-btn').forEach(b => {
        b.className = 'lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition';
    });
    const btn = document.getElementById(`lt-btn-${timeframe}`);
    if (btn) btn.className = 'lt-btn p-2 rounded-xl bg-red-500 text-slate-950 font-bold shadow transition';

    const formula = document.getElementById('leakFormulaLabel');
    const volume = document.getElementById('leakVolumeDisplay');
    if (!formula || !volume) return;

    if (timeframe === 'hour') {
        formula.innerText = '1 L/hour × 1 hour';
        volume.innerText = '1 Litre Lost!';
    } else if (timeframe === 'day') {
        formula.innerText = '1 L/hour × 24 hours';
        volume.innerText = '24 Litres Lost!';
    } else if (timeframe === 'week') {
        formula.innerText = '24 L/day × 7 days';
        volume.innerText = '168 Litres Lost!';
    } else if (timeframe === 'month') {
        formula.innerText = '24 L/day × 30 days';
        volume.innerText = '720 Litres Lost!';
    }
}

// Simulator 16: Conservation Volume Math
function updateConservationMath(students) {
    const sCount = parseInt(students);
    const countLabel = document.getElementById('studentCountLabel');
    const daily = document.getElementById('dailySchoolSavings');
    const monthly = document.getElementById('monthlySchoolSavings');
    const tanker = document.getElementById('tankerEquivLabel');
    if (!countLabel || !daily || !monthly || !tanker) return;

    countLabel.innerText = `${sCount} Students`;
    const dailyL = sCount * 19;
    const monthlyL = dailyL * 30;
    const tankers = (monthlyL / 10000).toFixed(1);

    daily.innerText = `${dailyL.toLocaleString()} L`;
    monthly.innerText = `${monthlyL.toLocaleString()} L`;
    tanker.innerText = `~${tankers} Large Tankers (10,000L each)`;
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSlideSimulator(slideNum) {
    if (slideNum === 1) setPumpkinMode('half');
    else if (slideNum === 2) setKgFraction(0.5);
    else if (slideNum === 3) updateBeamScaleUI();
    else if (slideNum === 4) setSweetBox(250);
    else if (slideNum === 5) setSpiceTarget(10);
    else if (slideNum === 6) setScaleTab('beam');
    else if (slideNum === 7) setHeavySack(25);
    else if (slideNum === 8) updateOlympicMath();
    else if (slideNum === 9) setLiquidPreset(500, 'Milk Pouch');
    else if (slideNum === 10) setFractionLitre(500);
    else if (slideNum === 11) updateMedicineBottleUI();
    else if (slideNum === 12) setOilBottleSize(100);
    else if (slideNum === 13) setMilkOrder(750);
    else if (slideNum === 15) setLeakTime('day');
    else if (slideNum === 16) updateConservationMath(500);
}

// On document load
document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
});
'''

# Write to .agents/class4_maths_ch8_js.js
js_path = os.path.join(os.path.dirname(__file__), "class4_maths_ch8_js.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

# Write to .agents/class4_maths_ch8_js.py
py_path = os.path.join(os.path.dirname(__file__), "class4_maths_ch8_js.py")
with open(py_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 8 JavaScript Engine"""\n\n')
    f.write("js_engine = r'''")
    f.write(js_code)
    f.write("'''\n")

print(f"Generated {js_path} and {py_path}")


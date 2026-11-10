# -*- coding: utf-8 -*-
"""Builder script to generate class3_maths_ch3_js.js."""

import json

js_code = r'''// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 3 Mathematics - Chapter 3: Double Century
// =========================================================================

let currentSlide = 1;
const totalSlides = 20;
let isAudioPlaying = false;
let currentUtterance = null;
let synth = window.speechSynthesis;
let selectedVoice = null;
let allVoices = [];
let speechKeepAliveTimer = null;

// Audio Context for Chimes & Acoustics
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

// Live High/Low Feedback Chimes
function playSuccessChime() {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(523.25, now); // C5
        osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.12); // E5
        osc1.frequency.exponentialRampToValueAtTime(783.99, now + 0.24); // G5

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(659.25, now);
        osc2.frequency.exponentialRampToValueAtTime(783.99, now + 0.12);
        osc2.frequency.exponentialRampToValueAtTime(1046.50, now + 0.24); // C6

        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.38);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.4);
        osc2.stop(now + 0.4);
    } catch (e) {
        console.warn('Audio chime error:', e);
    }
}

function playErrorChime() {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220.00, now); // A3
        osc.frequency.linearRampToValueAtTime(164.81, now + 0.25); // E3

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.32);
    } catch (e) {
        console.warn('Audio chime error:', e);
    }
}

function playTone(freq, type = 'sine', duration = 0.15, gainVol = 0.2) {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = type;
        osc.frequency.setValueAtTime(freq, now);

        gain.gain.setValueAtTime(gainVol, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + duration);
    } catch (e) {}
}

// =========================================================================
// PURE INDIAN MALE TEACHER SPEECH ENGINE
// =========================================================================
const femaleBlockList = [
    'female', 'woman', 'zira', 'heera', 'neerja', 'veena', 'priya', 
    'kalpana', 'swara', 'sangeeta', 'ananya', 'aditi', 'kavya', 'geeta'
];

function isBlockedVoice(name) {
    const lower = name.toLowerCase();
    return femaleBlockList.some(f => lower.includes(f));
}

function pickIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;

    // 1. Check Indian English or Hindi explicitly mentioning male / known male names
    const preferredNames = ['ravi', 'prabhat', 'google हिन्दी', 'google english (india)', 'microsoft ravi'];
    for (const pref of preferredNames) {
        const match = voices.find(v => v.name.toLowerCase().includes(pref) && !isBlockedVoice(v.name));
        if (match) return match;
    }

    // 2. Any en-IN or hi-IN voice not blocked by female names
    const indianVoices = voices.filter(v => (v.lang === 'en-IN' || v.lang === 'hi-IN' || v.lang.startsWith('en_IN') || v.lang.startsWith('hi_IN')) && !isBlockedVoice(v.name));
    if (indianVoices.length > 0) {
        return indianVoices[0];
    }

    // 3. Any English voice with 'male' in name
    const maleVoice = voices.find(v => v.name.toLowerCase().includes('male') && !isBlockedVoice(v.name));
    if (maleVoice) return maleVoice;

    // 4. Fallback to first non-blocked English voice
    const enFallback = voices.find(v => v.lang.startsWith('en') && !isBlockedVoice(v.name));
    if (enFallback) return enFallback;

    return voices[0];
}

function initSpeechEngine() {
    if (!synth) return;

    function populate() {
        allVoices = synth.getVoices();
        selectedVoice = pickIndianMaleVoice(allVoices);

        const voiceSelect = document.getElementById('voiceSelect');
        if (voiceSelect && allVoices.length > 0) {
            voiceSelect.innerHTML = '';
            allVoices.forEach((v, idx) => {
                const opt = document.createElement('option');
                opt.value = idx;
                opt.textContent = `${v.name} (${v.lang})${isBlockedVoice(v.name) ? ' [Female]' : ''}`;
                if (selectedVoice && v.name === selectedVoice.name) {
                    opt.selected = true;
                }
                voiceSelect.appendChild(opt);
            });
            voiceSelect.onchange = (e) => {
                selectedVoice = allVoices[e.target.value];
            };
        }
    }

    populate();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populate;
    }
}

function speakText(text, onEndCallback = null) {
    if (!synth) return;
    synth.cancel();
    if (speechKeepAliveTimer) clearInterval(speechKeepAliveTimer);

    if (!text || text.trim() === '') {
        isAudioPlaying = false;
        updateAudioBtnState();
        return;
    }

    currentUtterance = new SpeechSynthesisUtterance(text);
    if (!selectedVoice) {
        selectedVoice = pickIndianMaleVoice(allVoices);
    }
    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }

    // Pure Indian Male Teacher Calibration
    currentUtterance.pitch = 0.88;
    currentUtterance.rate = 0.90;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioBtnState();
    };

    currentUtterance.onend = () => {
        isAudioPlaying = false;
        updateAudioBtnState();
        if (speechKeepAliveTimer) clearInterval(speechKeepAliveTimer);
        if (onEndCallback) onEndCallback();
    };

    currentUtterance.onerror = () => {
        isAudioPlaying = false;
        updateAudioBtnState();
        if (speechKeepAliveTimer) clearInterval(speechKeepAliveTimer);
    };

    // Speech keep-alive for longer utterances on Chrome
    speechKeepAliveTimer = setInterval(() => {
        if (synth.speaking) {
            synth.pause();
            synth.resume();
        } else {
            clearInterval(speechKeepAliveTimer);
        }
    }, 12000);

    synth.speak(currentUtterance);
}

function toggleAudio() {
    if (!synth) return;
    if (isAudioPlaying) {
        synth.cancel();
        isAudioPlaying = false;
        updateAudioBtnState();
    } else {
        const slideSpeech = SLIDE_DATA[currentSlide - 1]?.speech;
        if (slideSpeech) {
            speakText(slideSpeech);
        }
    }
}

function replayCurrentAudio() {
    const slideSpeech = SLIDE_DATA[currentSlide - 1]?.speech;
    if (slideSpeech) {
        speakText(slideSpeech);
    }
}

function stopAudio() {
    if (!synth) return;
    synth.cancel();
    isAudioPlaying = false;
    updateAudioBtnState();
}

function updateAudioBtnState() {
    const btn = document.getElementById('audioToggleBtn');
    const label = document.getElementById('audioBtnLabel');
    const icon = document.getElementById('audioBtnIcon');
    if (!btn) return;

    if (isAudioPlaying) {
        btn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500');
        btn.classList.add('bg-amber-600', 'hover:bg-amber-500');
        if (label) label.textContent = 'Pause Lecture';
        if (icon) icon.textContent = '⏸️';
    } else {
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500');
        btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500');
        if (label) label.textContent = 'Listen Lecture';
        if (icon) icon.textContent = '🔊';
    }
}

function speakQuestion(qIndex) {
    const slide = SLIDE_DATA[currentSlide - 1];
    if (!slide || !slide.questions || !slide.questions[qIndex]) return;
    const q = slide.questions[qIndex];
    let fullText = `Question ${qIndex + 1}. ${q.question}. Options are: `;
    q.options.forEach((opt, idx) => {
        const letter = String.fromCharCode(65 + idx);
        fullText += `Option ${letter}: ${opt}. `;
    });
    speakText(fullText);
}

// =========================================================================
// SLIDE NAVIGATION & TERMINAL INVARIANT
// =========================================================================
function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;
    stopAudio();

    currentSlide = slideNum;

    // Toggle slide view visibility
    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) {
            if (i === currentSlide) {
                el.classList.remove('hidden');
                el.classList.add('block');
            } else {
                el.classList.remove('block');
                el.classList.add('hidden');
            }
        }
    }

    // Update Progress Bar & Counter
    const progBar = document.getElementById('progressBar');
    if (progBar) {
        const pct = ((currentSlide) / totalSlides) * 100;
        progBar.style.width = `${pct}%`;
    }

    const badge = document.getElementById('slideNumberBadge');
    if (badge) {
        badge.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }

    const titleEl = document.getElementById('activeSlideTitle');
    if (titleEl && SLIDE_DATA[currentSlide - 1]) {
        titleEl.textContent = SLIDE_DATA[currentSlide - 1].title;
    }

    // Terminal Invariant Check for Slide 20
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.style.display = 'block';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.style.display = 'none';
    }

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        prevBtn.style.opacity = (currentSlide === 1) ? '0.5' : '1';
    }

    // Trigger Simulator initializers when landing on relevant slide
    initSlideSimulator(currentSlide);

    // Scroll to top of slide
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

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevSlide();
    }
});

// =========================================================================
// CHECKPOINT HANDLERS (Slides 1 to 16)
// =========================================================================
function checkCheckpoint(slideId, cpIdx, selectedIdx, correctIdx, explanation) {
    const parent = document.getElementById(`cp-${slideId}-${cpIdx}`);
    if (!parent) return;

    const buttons = parent.querySelectorAll('.cp-option-btn');
    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-600', 'border-emerald-400', 'text-white', 'font-bold');
        } else if (idx === selectedIdx && selectedIdx !== correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-600', 'border-rose-400', 'text-white');
        }
    });

    const fb = parent.querySelector('.cp-feedback');
    if (fb) {
        fb.classList.remove('hidden');
        if (selectedIdx === correctIdx) {
            playSuccessChime();
            fb.classList.add('bg-emerald-950/60', 'border-emerald-600/50', 'text-emerald-200');
            fb.innerHTML = `<strong>✨ Correct!</strong> ${explanation}`;
        } else {
            playErrorChime();
            fb.classList.add('bg-rose-950/60', 'border-rose-600/50', 'text-rose-200');
            fb.innerHTML = `<strong>⚠️ Keep Going!</strong> ${explanation}`;
        }
    }
}

// =========================================================================
// CHALLENGE QUIZ HANDLERS (Slides 17 to 20)
// =========================================================================
function handleQuizChoice(qKey, selectedIdx, correctIdx, explanation) {
    const container = document.getElementById(`quiz-q-${qKey}`);
    if (!container) return;

    const buttons = container.querySelectorAll('.quiz-opt-btn');
    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-emerald-600', 'border-emerald-400', 'text-white', 'font-bold');
        } else if (idx === selectedIdx && selectedIdx !== correctIdx) {
            btn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'border-slate-700');
            btn.classList.add('bg-rose-600', 'border-rose-400', 'text-white');
        }
    });

    const fb = container.querySelector('.quiz-feedback');
    if (fb) {
        fb.classList.remove('hidden');
        if (selectedIdx === correctIdx) {
            playSuccessChime();
            fb.classList.add('bg-emerald-950/60', 'border-emerald-600/50', 'text-emerald-200');
            fb.innerHTML = `<strong>✨ Brilliant!</strong> ${explanation}`;
        } else {
            playErrorChime();
            fb.classList.add('bg-rose-950/60', 'border-rose-600/50', 'text-rose-200');
            fb.innerHTML = `<strong>⚠️ Review:</strong> ${explanation}`;
        }
    }
}

function toggleHint(qKey) {
    const hintBox = document.getElementById(`hint-${qKey}`);
    if (hintBox) {
        hintBox.classList.toggle('hidden');
    }
}

function openSolutionModal(qKey, s1, s2, s3) {
    const modal = document.getElementById('solutionModal');
    const content = document.getElementById('solutionModalContent');
    if (!modal || !content) return;

    content.innerHTML = `
        <div class="space-y-3">
            <div class="bg-slate-900 border border-indigo-700/50 p-3 rounded-xl">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wide block mb-1">Step 1: Identify Given Information</span>
                <p class="text-sm text-slate-200">${s1}</p>
            </div>
            <div class="bg-slate-900 border border-emerald-700/50 p-3 rounded-xl">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wide block mb-1">Step 2: Mathematical Concept & Operation</span>
                <p class="text-sm text-slate-200">${s2}</p>
            </div>
            <div class="bg-slate-900 border border-amber-700/50 p-3 rounded-xl">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide block mb-1">Step 3: Verification & Concluding Result</span>
                <p class="text-sm text-slate-200">${s3}</p>
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
    }
}

// =========================================================================
// SIMULATOR 1: PREHISTORIC TALLYING
// =========================================================================
let tallyCount = 17;
let tallyGroupSize = 5;

function addTally(delta) {
    tallyCount = Math.max(0, Math.min(60, tallyCount + delta));
    playTone(440, 'triangle', 0.08);
    renderTally();
}

function setTallyGroup(size) {
    tallyGroupSize = size;
    ['btnGroup5', 'btnGroup10', 'btnGroup20'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-amber-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });
    const active = document.getElementById(`btnGroup${size}`);
    if (active) {
        active.classList.add('bg-amber-600', 'text-white');
    }
    playTone(520, 'sine', 0.1);
    renderTally();
}

function resetTally() {
    tallyCount = 0;
    renderTally();
}

function renderTally() {
    const area = document.getElementById('tallyDisplayArea');
    const badge = document.getElementById('tallyCountBadge');
    const summary = document.getElementById('tallyGroupingSummary');
    if (!area || !badge) return;

    badge.textContent = `Total Marks: ${tallyCount}`;

    const bundles = Math.floor(tallyCount / tallyGroupSize);
    const singles = tallyCount % tallyGroupSize;

    if (summary) {
        summary.textContent = `Grouping: ${bundles} bundle${bundles !== 1 ? 's' : ''} of ${tallyGroupSize} + ${singles} single scratch${singles !== 1 ? 'es' : ''} = ${tallyCount} marks`;
    }

    let html = '';
    // Draw bundles
    for (let b = 0; b < bundles; b++) {
        html += `<div class="bg-stone-900 border border-amber-600/60 p-2 rounded-lg flex items-center gap-1.5 shadow">
            <span class="text-[10px] text-amber-400 font-mono font-bold mr-1">[${tallyGroupSize}]</span>
            <div class="flex gap-1">`;
        for (let i = 0; i < Math.min(tallyGroupSize, 10); i++) {
            html += `<div class="w-1.5 h-7 bg-amber-400 rounded-full"></div>`;
        }
        if (tallyGroupSize > 10) {
            html += `<span class="text-xs text-amber-300 font-mono">+${tallyGroupSize - 10}</span>`;
        }
        html += `</div></div>`;
    }

    // Draw singles
    if (singles > 0) {
        html += `<div class="bg-stone-900/50 border border-stone-700 p-2 rounded-lg flex items-center gap-1.5">
            <span class="text-[10px] text-stone-400 font-mono mr-1">[Loose]</span>
            <div class="flex gap-1.5">`;
        for (let s = 0; s < singles; s++) {
            html += `<div class="w-1.5 h-6 bg-stone-300 rounded-full"></div>`;
        }
        html += `</div></div>`;
    }

    if (tallyCount === 0) {
        html = `<div class="text-xs text-stone-500 italic p-2">Cave surface is clear. Click +1 or +5 to carve tally scratches!</div>`;
    }

    area.innerHTML = html;
}

// =========================================================================
// SIMULATOR 2: INDIAN BASE TEN SYSTEM
// =========================================================================
let digitH = 1;
let digitT = 4;
let digitO = 6;

function changeDigit(col, delta) {
    if (col === 'h') {
        digitH = Math.max(0, Math.min(9, digitH + delta));
    } else if (col === 't') {
        digitT = Math.max(0, Math.min(9, digitT + delta));
    } else if (col === 'o') {
        digitO = Math.max(0, Math.min(9, digitO + delta));
    }
    playTone(350 + (col === 'h' ? 200 : col === 't' ? 100 : 0), 'sine', 0.08);
    updateBaseTenView();
}

function setBaseTenPreset(h, t, o) {
    digitH = h;
    digitT = t;
    digitO = o;
    playSuccessChime();
    updateBaseTenView();
}

function updateBaseTenView() {
    const elH = document.getElementById('digitH');
    const elT = document.getElementById('digitT');
    const elO = document.getElementById('digitO');
    const vH = document.getElementById('valH');
    const vT = document.getElementById('valT');
    const vO = document.getElementById('valO');
    const eq = document.getElementById('baseTenEquation');
    const nameEl = document.getElementById('baseTenWordName');

    if (!elH || !elT || !elO) return;

    elH.textContent = digitH;
    elT.textContent = digitT;
    elO.textContent = digitO;

    if (vH) vH.textContent = `${digitH * 100}`;
    if (vT) vT.textContent = `${digitT * 10}`;
    if (vO) vO.textContent = `${digitO}`;

    const total = (digitH * 100) + (digitT * 10) + digitO;
    if (eq) {
        eq.textContent = `${digitH * 100} + ${digitT * 10} + ${digitO} = ${total}`;
    }

    if (nameEl) {
        nameEl.textContent = `"${numberToWords(total)}"`;
    }
}

function numberToWords(n) {
    if (n === 0) return 'Zero';
    const ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
    const tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];

    let words = '';
    if (Math.floor(n / 100) > 0) {
        words += ones[Math.floor(n / 100)] + ' Hundred ';
        n %= 100;
        if (n > 0) words += 'and ';
    }
    if (n > 0) {
        if (n < 20) {
            words += ones[n];
        } else {
            words += tens[Math.floor(n / 10)];
            if (n % 10 > 0) {
                words += '-' + ones[n % 10];
            }
        }
    }
    return words.trim();
}

// =========================================================================
// SIMULATOR 3: POWER OF ZERO PLACEHOLDER
// =========================================================================
function setZeroDemo(val) {
    playTone(480, 'sine', 0.1);
    const boxWith = document.getElementById('withZeroBox');
    const boxWithout = document.getElementById('withoutZeroBox');
    if (!boxWith || !boxWithout) return;

    if (val === 105) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">With Zero Placeholder (105)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40">
                    <span class="text-[10px] text-indigo-300 block">HUNDREDS</span>
                    <span class="text-2xl font-black font-mono text-indigo-300">1</span>
                    <span class="text-[10px] text-slate-400 block">1 bundle (100)</span>
                </div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40">
                    <span class="text-[10px] text-cyan-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-cyan-300">0</span>
                    <span class="text-[10px] text-cyan-400 block font-bold">Empty space</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">5</span>
                    <span class="text-[10px] text-slate-400 block">5 singles</span>
                </div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 100 + 0 + 5 = <strong class="text-cyan-300 text-sm">105</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Zero (Collapsed: 15)</span>
            <div class="grid grid-cols-2 gap-2 w-3/4 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40">
                    <span class="text-[10px] text-rose-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-rose-300">1</span>
                    <span class="text-[10px] text-slate-400 block">1 ten (10)</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">5</span>
                    <span class="text-[10px] text-slate-400 block">5 singles</span>
                </div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 10 + 5 = <strong class="text-rose-400 text-sm">15 (Disaster! Lost 90!)</strong></div>
        `;
    } else if (val === 150) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">With Zero in Ones (150)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40">
                    <span class="text-[10px] text-indigo-300 block">HUNDREDS</span>
                    <span class="text-2xl font-black font-mono text-indigo-300">1</span>
                    <span class="text-[10px] text-slate-400 block">100</span>
                </div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40">
                    <span class="text-[10px] text-cyan-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-cyan-300">5</span>
                    <span class="text-[10px] text-slate-400 block">50</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">0</span>
                    <span class="text-[10px] text-cyan-400 block font-bold">Zero ones</span>
                </div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 100 + 50 + 0 = <strong class="text-cyan-300 text-sm">150</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Ones Zero (15)</span>
            <div class="grid grid-cols-2 gap-2 w-3/4 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40">
                    <span class="text-[10px] text-rose-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-rose-300">1</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">5</span>
                </div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 15 (Lost 135 units!)</div>
        `;
    } else if (val === 200) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Double Century (200)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40">
                    <span class="text-[10px] text-indigo-300 block">HUNDREDS</span>
                    <span class="text-2xl font-black font-mono text-indigo-300">2</span>
                    <span class="text-[10px] text-slate-400 block">200</span>
                </div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40">
                    <span class="text-[10px] text-cyan-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-cyan-300">0</span>
                    <span class="text-[10px] text-cyan-400 block font-bold">0 tens</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">0</span>
                    <span class="text-[10px] text-cyan-400 block font-bold">0 ones</span>
                </div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 200 + 0 + 0 = <strong class="text-cyan-300 text-sm">200</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Two Zeros (Collapsed: 2)</span>
            <div class="grid grid-cols-1 gap-2 w-1/3 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40">
                    <span class="text-[10px] text-rose-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-rose-300">2</span>
                </div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 2 (Lost 198 items!)</div>
        `;
    }
}

// =========================================================================
// SIMULATOR 4: MARKETPLACE COUNTING
// =========================================================================
let currentStall = 'laddoos';
let stallBoxes = 4;
let stallSingles = 7;

function selectMarketStall(type) {
    currentStall = type;
    ['stallBtnLaddoos', 'stallBtnBangles', 'stallBtnBananas'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-orange-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = {
        laddoos: 'stallBtnLaddoos',
        bangles: 'stallBtnBangles',
        bananas: 'stallBtnBananas'
    };
    const active = document.getElementById(activeMap[type]);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-orange-600', 'text-white');
    }

    if (type === 'laddoos') { stallBoxes = 4; stallSingles = 7; }
    else if (type === 'bangles') { stallBoxes = 5; stallSingles = 3; }
    else if (type === 'bananas') { stallBoxes = 6; stallSingles = 8; }

    playTone(460, 'sine', 0.1);
    renderMarketStall();
}

function adjustMarketItem(kind, delta) {
    if (kind === 'box') {
        stallBoxes = Math.max(0, Math.min(9, stallBoxes + delta));
    } else {
        stallSingles = Math.max(0, Math.min(9, stallSingles + delta));
    }
    playTone(380 + (kind === 'box' ? 120 : 0), 'sine', 0.08);
    renderMarketStall();
}

function renderMarketStall() {
    const title = document.getElementById('stallItemTitle');
    const badge = document.getElementById('stallTotalBadge');
    const container = document.getElementById('stallVisualContainer');
    const tensEl = document.getElementById('stallTensCount');
    const onesEl = document.getElementById('stallOnesCount');

    if (!container || !badge) return;

    const names = {
        laddoos: { name: 'Laddoo Sweet Stall', box: 'Box of 10 Laddoos', single: 'Single Laddoo', icon: '🟡', boxIcon: '📦' },
        bangles: { name: 'Glass Bangle Stall', box: 'Packet of 10 Bangles', single: 'Loose Bangle', icon: '⭕', boxIcon: '🎁' },
        bananas: { name: 'Fresh Banana Stall', box: 'Bunch of 10 Bananas', single: 'Single Banana', icon: '🍌', boxIcon: '🧺' }
    };

    const cfg = names[currentStall];
    if (title) title.textContent = `${cfg.name}: Packed Tens & Loose Items`;

    const total = (stallBoxes * 10) + stallSingles;
    badge.textContent = `Total: ${total}`;

    if (tensEl) tensEl.textContent = `${stallBoxes} packed (${stallBoxes * 10})`;
    if (onesEl) onesEl.textContent = `${stallSingles} loose singles (${stallSingles})`;

    let html = '';
    // Render boxes
    for (let b = 0; b < stallBoxes; b++) {
        html += `<div class="bg-orange-950/60 border border-orange-600/60 p-2 rounded-xl flex items-center gap-2 shadow">
            <span class="text-2xl">${cfg.boxIcon}</span>
            <div class="text-left">
                <span class="text-xs font-bold text-orange-300 block font-mono">Ten (10)</span>
                <span class="text-[10px] text-slate-400 block">${currentStall}</span>
            </div>
        </div>`;
    }

    // Render singles
    if (stallSingles > 0) {
        html += `<div class="bg-amber-950/40 border border-amber-600/40 p-2 rounded-xl flex flex-wrap items-center gap-1.5 max-w-xs">`;
        for (let s = 0; s < stallSingles; s++) {
            html += `<span class="text-xl" title="1 single">${cfg.icon}</span>`;
        }
        html += `</div>`;
    }

    if (stallBoxes === 0 && stallSingles === 0) {
        html = `<div class="text-xs text-slate-500 italic p-2">Stall is empty. Add boxes or loose items to begin!</div>`;
    }

    container.innerHTML = html;
}

// =========================================================================
// SIMULATOR 5: SNAKES AND LADDERS 100-GRID
// =========================================================================
let gridPos = 24;

function initSnakesGrid() {
    const grid = document.getElementById('snakesMiniGrid');
    if (!grid) return;

    let html = '';
    // 10 rows from 100 down to 1
    for (let r = 9; r >= 0; r--) {
        const isEvenRow = (r % 2 === 1);
        for (let c = 0; c < 10; c++) {
            const num = isEvenRow ? (r * 10 + (10 - c)) : (r * 10 + (c + 1));
            html += `<div id="gridCell${num}" onclick="setGridPos(${num})" class="text-[10px] font-mono flex items-center justify-center rounded cursor-pointer transition ${getCellColor(num)}">
                ${num}
            </div>`;
        }
    }
    grid.innerHTML = html;
    updateGridDisplay();
}

function getCellColor(n) {
    if (n === 34 || n === 85) return 'bg-emerald-900/60 text-emerald-200 border border-emerald-500'; // ladder tops
    if (n === 12 || n === 55) return 'bg-emerald-950/40 text-emerald-300'; // ladder bottoms
    if (n === 21 || n === 52) return 'bg-rose-950/40 text-rose-300'; // snake tails
    if (n === 43 || n === 88) return 'bg-rose-900/60 text-rose-200 border border-rose-500'; // snake heads
    return 'bg-slate-800/80 text-slate-300 hover:bg-slate-700';
}

function setGridPos(n) {
    gridPos = Math.max(1, Math.min(100, n));
    playTone(400 + (n * 3), 'sine', 0.08);
    updateGridDisplay();
}

function stepGridPos(delta) {
    const next = gridPos + delta;
    if (next >= 1 && next <= 100) {
        setGridPos(next);
    }
}

function rollSnakesDice() {
    const roll = Math.floor(Math.random() * 6) + 1;
    playTone(600, 'triangle', 0.1);
    let next = gridPos + roll;
    if (next > 100) next = 100;

    // Check ladders & snakes
    let statusText = `Rolled a ${roll}! Moved to ${next}.`;
    if (next === 12) {
        next = 34;
        statusText = `Rolled a ${roll}! Landed on 12, climbed a ladder to 34!`;
        playSuccessChime();
    } else if (next === 55) {
        next = 85;
        statusText = `Rolled a ${roll}! Big ladder! Climbed to 85!`;
        playSuccessChime();
    } else if (next === 43) {
        next = 21;
        statusText = `Oh no! Bitten by snake at 43! Slid down to 21.`;
        playErrorChime();
    } else if (next === 88) {
        next = 52;
        statusText = `Snake slide! Landed at 88, fell to 52.`;
        playErrorChime();
    }

    gridPos = next;
    updateGridDisplay();
    const st = document.getElementById('gridActionStatus');
    if (st) st.textContent = statusText;
}

function resetGridPos() {
    setGridPos(1);
    const st = document.getElementById('gridActionStatus');
    if (st) st.textContent = 'Reset to start position: 1';
}

function updateGridDisplay() {
    // Clear old token styles
    for (let i = 1; i <= 100; i++) {
        const c = document.getElementById(`gridCell${i}`);
        if (c) {
            c.classList.remove('ring-2', 'ring-amber-400', 'bg-amber-500', 'text-slate-950', 'font-black');
            if (i === gridPos) {
                c.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500', 'text-slate-950', 'font-black');
            }
        }
    }

    const posEl = document.getElementById('gridPlayerPos');
    const bundleEl = document.getElementById('gridBundleNotation');
    if (posEl) posEl.textContent = gridPos;

    if (bundleEl) {
        const tens = Math.floor(gridPos / 10);
        const ones = gridPos % 10;
        bundleEl.textContent = `${tens} tens bundle${tens !== 1 ? 's' : ''} + ${ones} loose stick${ones !== 1 ? 's' : ''}`;
    }
}

// =========================================================================
// SIMULATOR 6: THE TALKING POT
// =========================================================================
function activateTalkingPot() {
    const input = document.getElementById('potInputNumber');
    if (!input) return;
    const n = parseInt(input.value, 10);
    if (isNaN(n)) return;

    const next = n + 1;
    playSuccessChime();

    const potSvg = document.getElementById('potSvg');
    const potBubble = document.getElementById('potBubble');
    const speechEl = document.getElementById('potSpeechOutput');

    if (potSvg) {
        potSvg.classList.add('scale-110');
        setTimeout(() => potSvg.classList.remove('scale-110'), 300);
    }

    if (potBubble) {
        potBubble.textContent = `${next}!`;
        potBubble.classList.remove('scale-0');
        potBubble.classList.add('scale-100');
    }

    if (speechEl) {
        speechEl.textContent = `"You gave me ${n}... so the next number is ${next} (${numberToWords(next)})!"`;
    }

    speakText(`The number after ${n} is ${next}!`);
}

function quickFeedPot(n) {
    const input = document.getElementById('potInputNumber');
    if (input) input.value = n;
    activateTalkingPot();
}

// =========================================================================
// SIMULATOR 7: DEFINING ONE HUNDRED
// =========================================================================
function setHundredView(view) {
    ['hViewTabCricket', 'hViewTabBundles', 'hViewTabSuccessor', 'hViewTabBindis'].forEach(id => {
        const tab = document.getElementById(id);
        if (tab) {
            tab.classList.remove('bg-yellow-600', 'text-white');
            tab.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = {
        cricket: 'hViewTabCricket',
        bundles: 'hViewTabBundles',
        successor: 'hViewTabSuccessor',
        bindis: 'hViewTabBindis'
    };
    const active = document.getElementById(activeMap[view]);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-yellow-600', 'text-white');
    }

    playTone(550, 'sine', 0.1);
    const panel = document.getElementById('hundredViewPanel');
    if (!panel) return;

    if (view === 'cricket') {
        panel.innerHTML = `
            <div class="text-center space-y-2">
                <span class="text-4xl">🏏 💯 🎆</span>
                <div class="text-lg font-black text-yellow-300 font-mono">BATSMAN SCORES A CENTURY!</div>
                <p class="text-xs text-slate-300 max-w-sm">
                    In cricket, when a batsman scores exactly 100 runs, it is celebrated as a "Century". The crowd erupts and teammates applaud!
                </p>
                <div class="inline-block bg-yellow-950/60 border border-yellow-500/40 px-3 py-1 rounded text-xs font-mono text-yellow-200">
                    Runs: 100 = 100 Runs Milestone
                </div>
            </div>
        `;
    } else if (view === 'bundles') {
        let bHtml = '<div class="flex flex-wrap gap-2 justify-center my-2 max-w-md">';
        for (let i = 0; i < 10; i++) {
            bHtml += `<div class="bg-indigo-900/70 border border-indigo-400 p-1.5 rounded flex flex-col items-center">
                <span class="text-[10px] text-indigo-300 font-bold">10</span>
                <span class="text-xs">🪵</span>
            </div>`;
        }
        bHtml += '</div>';

        panel.innerHTML = `
            <div class="text-center space-y-1">
                <div class="text-sm font-bold text-indigo-300">10 Bundles of 10 Matchsticks</div>
                ${bHtml}
                <div class="text-xs font-mono text-yellow-300 font-bold">10 × 10 = 100 Matchsticks</div>
            </div>
        `;
    } else if (view === 'successor') {
        panel.innerHTML = `
            <div class="text-center space-y-2">
                <div class="text-3xl font-black font-mono text-white">99 + 1 = 100</div>
                <div class="text-xs text-slate-300 max-w-sm">
                    99 is the biggest 2-digit number (9 tens and 9 ones). When you add just 1 single more, the ones place bursts, triggering a double regrouping into the first 3-digit number: 100!
                </div>
                <div class="text-xs font-mono text-emerald-400 font-bold">99 Ones + 1 One = 10 Tens = 1 Hundred</div>
            </div>
        `;
    } else if (view === 'bindis') {
        let cardsHtml = '<div class="grid grid-cols-5 gap-1.5 justify-center my-2 max-w-xs">';
        for (let i = 0; i < 10; i++) {
            cardsHtml += `<div class="bg-rose-950/50 border border-rose-500/50 p-1 rounded text-center">
                <span class="text-[9px] text-rose-300 font-bold block">Card ${i+1}</span>
                <span class="text-[11px]">🔴🔴🔴</span>
            </div>`;
        }
        cardsHtml += '</div>';

        panel.innerHTML = `
            <div class="text-center space-y-1">
                <div class="text-sm font-bold text-rose-300">10 Packets of 10 Decorative Bindis</div>
                ${cardsHtml}
                <div class="text-xs font-mono text-yellow-300 font-bold">10 Packets × 10 Bindis = 100 Bindis</div>
            </div>
        `;
    }
}

// =========================================================================
// SIMULATOR 8: MAKING ONE HUNDRED (GINLADI 100-BEAD STRING)
// =========================================================================
let ginladiVal = 60;

function updateGinladi(val) {
    ginladiVal = parseInt(val, 10);
    const splitEl = document.getElementById('beadSplitValue');
    const sliderDisp = document.getElementById('sliderValDisplay');
    const eq = document.getElementById('hundredPairEquation');
    const exp = document.getElementById('hundredPairExplanation');
    const slider = document.getElementById('ginladiSlider');

    if (splitEl) splitEl.textContent = ginladiVal;
    if (sliderDisp) sliderDisp.textContent = ginladiVal;
    if (slider && slider.value !== String(ginladiVal)) slider.value = ginladiVal;

    const complement = 100 - ginladiVal;
    if (eq) {
        eq.textContent = `${ginladiVal} + ${complement} = 100`;
    }
    if (exp) {
        exp.textContent = `Part A: ${ginladiVal} beads + Part B: ${complement} beads = 100 beads in total`;
    }

    renderGinladiBeads();
}

function setGinladiVal(val) {
    playTone(490, 'sine', 0.08);
    updateGinladi(val);
}

function renderGinladiBeads() {
    const track = document.getElementById('ginladiBeadTrack');
    if (!track) return;

    let html = '';
    for (let i = 1; i <= 100; i++) {
        // Group of 10 color alternation
        const groupTen = Math.floor((i - 1) / 10);
        const isRedGroup = (groupTen % 2 === 0);

        const isPartA = (i <= ginladiVal);
        const opacityClass = isPartA ? 'opacity-100 ring-1 ring-teal-400' : 'opacity-40';
        const colorClass = isRedGroup ? 'bg-rose-500' : 'bg-slate-200';

        html += `<div title="Bead ${i}" class="w-2.5 h-2.5 sm:w-3 sm:h-3 rounded-full ${colorClass} ${opacityClass} transition"></div>`;
    }
    track.innerHTML = html;
}

// =========================================================================
// SIMULATOR 9: FLOWER PETAL PUZZLES
// =========================================================================
const petalSets = [
    [25, 75, 40, 60, 15, 85, 30, 70],
    [10, 90, 35, 65, 45, 55, 20, 80],
    [5, 95, 50, 50, 18, 82, 32, 68]
];
let currentPetalSetIdx = 0;
let selectedPetalIdx = null;

function renderFlowerPetals() {
    const container = document.getElementById('flowerPetalsContainer');
    if (!container) return;

    const petals = petalSets[currentPetalSetIdx];
    let html = '';

    const radius = 95; // px from center
    const cx = 140; // center x
    const cy = 140; // center y

    petals.forEach((val, idx) => {
        const angle = (idx * (360 / petals.length)) * (Math.PI / 180);
        const x = cx + radius * Math.cos(angle) - 24;
        const y = cy + radius * Math.sin(angle) - 24;

        html += `<button onclick="selectPetal(${idx})" id="petalBtn${idx}" style="left: ${x}px; top: ${y}px;" class="absolute w-12 h-12 rounded-full bg-pink-700/80 hover:bg-pink-600 border-2 border-pink-400 flex items-center justify-center font-mono font-bold text-white text-sm shadow transition transform hover:scale-110 active:scale-95">
            ${val}
        </button>`;
    });

    container.innerHTML = html;
}

function selectPetal(idx) {
    const petals = petalSets[currentPetalSetIdx];
    const status = document.getElementById('petalPairStatus');

    if (selectedPetalIdx === null) {
        selectedPetalIdx = idx;
        const btn = document.getElementById(`petalBtn${idx}`);
        if (btn) btn.classList.add('ring-4', 'ring-amber-300', 'bg-pink-500');
        playTone(420, 'sine', 0.1);
        if (status) status.innerHTML = `Selected <strong class="text-pink-300">${petals[idx]}</strong>. Now click the matching petal that adds to 100!`;
    } else {
        if (selectedPetalIdx === idx) {
            // Deselect
            const btn = document.getElementById(`petalBtn${idx}`);
            if (btn) btn.classList.remove('ring-4', 'ring-amber-300', 'bg-pink-500');
            selectedPetalIdx = null;
            if (status) status.textContent = 'Petal deselected. Click any first petal to start!';
            return;
        }

        const v1 = petals[selectedPetalIdx];
        const v2 = petals[idx];
        const sum = v1 + v2;

        if (sum === 100) {
            playSuccessChime();
            const btn1 = document.getElementById(`petalBtn${selectedPetalIdx}`);
            const btn2 = document.getElementById(`petalBtn${idx}`);
            if (btn1) btn1.classList.add('bg-emerald-600', 'border-emerald-300');
            if (btn2) btn2.classList.add('bg-emerald-600', 'border-emerald-300');
            if (status) status.innerHTML = `🎉 <strong>Match Made!</strong> ${v1} + ${v2} = 100! Excellent calculation!`;
            selectedPetalIdx = null;
        } else {
            playErrorChime();
            if (status) status.innerHTML = `⚠️ <strong>Not 100:</strong> ${v1} + ${v2} = ${sum}. Try another partner!`;
            const btn = document.getElementById(`petalBtn${selectedPetalIdx}`);
            if (btn) btn.classList.remove('ring-4', 'ring-amber-300', 'bg-pink-500');
            selectedPetalIdx = null;
        }
    }
}

function resetFlowerPuzzle() {
    currentPetalSetIdx = (currentPetalSetIdx + 1) % petalSets.length;
    selectedPetalIdx = null;
    const status = document.getElementById('petalPairStatus');
    if (status) status.textContent = 'Click any first petal to start pairing!';
    renderFlowerPetals();
}

// =========================================================================
// SIMULATOR 10: COUNTING BEYOND HUNDRED (101 to 124)
// =========================================================================
let seqNum = 108;

function stepSeq(delta) {
    const next = seqNum + delta;
    if (next >= 100 && next <= 130) {
        setSeqNum(next);
    }
}

function setSeqNum(n) {
    seqNum = n;
    playTone(380 + ((n - 100) * 10), 'sine', 0.08);
    updateSeqView();
}

function updateSeqView() {
    const numEl = document.getElementById('seqNumberDisplay');
    const wordEl = document.getElementById('seqWordDisplay');
    const tensVal = document.getElementById('seqTensVal');
    const tensTxt = document.getElementById('seqTensTxt');
    const onesVal = document.getElementById('seqOnesVal');
    const onesTxt = document.getElementById('seqOnesTxt');
    const eq = document.getElementById('seqEquation');

    if (!numEl) return;

    numEl.textContent = seqNum;
    if (wordEl) wordEl.textContent = `"${numberToWords(seqNum)}"`;

    const remainder = seqNum - 100;
    const tens = Math.floor(remainder / 10);
    const ones = remainder % 10;

    if (tensVal) tensVal.textContent = tens;
    if (tensTxt) tensTxt.textContent = `${tens} tens (${tens * 10})`;
    if (onesVal) onesVal.textContent = ones;
    if (onesTxt) onesTxt.textContent = `${ones} loose singles (${ones})`;

    if (eq) {
        eq.textContent = `100 + ${tens * 10} + ${ones} = ${seqNum}`;
    }
}

// =========================================================================
// SIMULATOR 11: MATCHSTICK BUNDLES TO 150
// =========================================================================
let matchH = 1;
let matchT = 3;
let matchO = 6;

function adjustMatchUnit(col, delta) {
    if (col === 'h') matchH = Math.max(0, Math.min(2, matchH + delta));
    else if (col === 't') matchT = Math.max(0, Math.min(9, matchT + delta));
    else if (col === 'o') matchO = Math.max(0, Math.min(9, matchO + delta));

    playTone(300 + (col === 'h' ? 250 : col === 't' ? 120 : 0), 'sine', 0.08);
    renderMatchsticks();
}

function setMatchPreset(h, t, o) {
    matchH = h;
    matchT = t;
    matchO = o;
    playSuccessChime();
    renderMatchsticks();
}

function renderMatchsticks() {
    const badge = document.getElementById('matchstickTotalBadge');
    const tensDisp = document.getElementById('matchTensDisplay');
    const onesDisp = document.getElementById('matchOnesDisplay');
    const hCount = document.getElementById('matchCountH');
    const tCount = document.getElementById('matchCountT');
    const oCount = document.getElementById('matchCountO');
    const eq = document.getElementById('matchSummaryEquation');

    if (!badge) return;

    const total = (matchH * 100) + (matchT * 10) + matchO;
    badge.textContent = `${total} Matchsticks`;

    if (hCount) hCount.textContent = `${matchH} bundle${matchH !== 1 ? 's' : ''} = ${matchH * 100}`;
    if (tCount) tCount.textContent = `${matchT} bundle${matchT !== 1 ? 's' : ''} = ${matchT * 10}`;
    if (oCount) oCount.textContent = `${matchO} single${matchO !== 1 ? 's' : ''} = ${matchO}`;

    if (tensDisp) {
        let tHtml = '';
        for (let i = 0; i < matchT; i++) {
            tHtml += `<div class="w-6 h-10 bg-emerald-900 border border-emerald-400 rounded flex items-center justify-center text-[10px] text-emerald-200 font-bold" title="Bundle of 10">10</div>`;
        }
        if (matchT === 0) tHtml = '<span class="text-[11px] text-slate-500 italic">0 bundles</span>';
        tensDisp.innerHTML = tHtml;
    }

    if (onesDisp) {
        let oHtml = '';
        for (let i = 0; i < matchO; i++) {
            oHtml += `<div class="w-1.5 h-8 bg-amber-400 rounded-full" title="Single stick"></div>`;
        }
        if (matchO === 0) oHtml = '<span class="text-[11px] text-slate-500 italic">0 loose</span>';
        onesDisp.innerHTML = oHtml;
    }

    if (eq) {
        eq.textContent = `Total: ${matchH * 100} + ${matchT * 10} + ${matchO} = ${total} Matchsticks`;
    }
}

// =========================================================================
// SIMULATOR 12: COUNTING TO ONE-FIFTY RANGE EXPLORER
// =========================================================================
function updateRange150(val) {
    const num = parseInt(val, 10);
    const numEl = document.getElementById('range150Number');
    const wordEl = document.getElementById('range150Word');
    const dist100 = document.getElementById('rangeDist100');
    const dist150 = document.getElementById('rangeDist150');
    const nearestTen = document.getElementById('rangeNearestTen');

    if (!numEl) return;

    numEl.textContent = num;
    if (wordEl) wordEl.textContent = `"${numberToWords(num)}"`;

    if (dist100) dist100.textContent = `+${num - 100}`;
    if (dist150) dist150.textContent = `${150 - num} to go`;
    if (nearestTen) nearestTen.textContent = `${Math.round(num / 10) * 10}`;
}

function setRange150Val(val) {
    const slider = document.getElementById('sliderRange150');
    if (slider) slider.value = val;
    playTone(400 + (val - 100) * 3, 'sine', 0.08);
    updateRange150(val);
}

// =========================================================================
// SIMULATOR 13: CLAP SNAP PAT RHYTHM GAME
// =========================================================================
let rhythmSequence = [];

function triggerRhythm(action) {
    if (action === 'clap') {
        // Deep resonant hand clap
        playTone(180, 'triangle', 0.25, 0.4);
        rhythmSequence.push({ type: 'clap', val: 100, icon: '👏', label: '100' });
    } else if (action === 'snap') {
        // Crisp finger snap
        playTone(850, 'square', 0.08, 0.25);
        rhythmSequence.push({ type: 'snap', val: 10, icon: '🫰', label: '10' });
    } else if (action === 'pat') {
        // Warm thigh pat
        playTone(320, 'sine', 0.15, 0.3);
        rhythmSequence.push({ type: 'pat', val: 1, icon: '🦵', label: '1' });
    }

    renderRhythmLog();
}

function clearRhythm() {
    rhythmSequence = [];
    renderRhythmLog();
}

function playRhythmTarget(target) {
    clearRhythm();
    const h = Math.floor(target / 100);
    const rem = target % 100;
    const t = Math.floor(rem / 10);
    const o = rem % 10;

    for (let i = 0; i < h; i++) rhythmSequence.push({ type: 'clap', val: 100, icon: '👏', label: '100' });
    for (let i = 0; i < t; i++) rhythmSequence.push({ type: 'snap', val: 10, icon: '🫰', label: '10' });
    for (let i = 0; i < o; i++) rhythmSequence.push({ type: 'pat', val: 1, icon: '🦵', label: '1' });

    playSuccessChime();
    renderRhythmLog();
}

function renderRhythmLog() {
    const log = document.getElementById('rhythmSoundLog');
    const totalEl = document.getElementById('rhythmTotalNumber');
    const breakEl = document.getElementById('rhythmBreakdownTxt');

    if (!log || !totalEl) return;

    let sum = 0;
    let claps = 0, snaps = 0, pats = 0;
    let html = '';

    rhythmSequence.forEach(item => {
        sum += item.val;
        if (item.type === 'clap') claps++;
        else if (item.type === 'snap') snaps++;
        else if (item.type === 'pat') pats++;

        html += `<span class="px-2 py-1 bg-slate-800 rounded border border-slate-700 font-mono text-sm shadow">
            ${item.icon} <strong class="text-xs text-slate-300">${item.label}</strong>
        </span>`;
    });

    if (rhythmSequence.length === 0) {
        html = '<span class="text-xs text-slate-500 italic">Tap Clap (100), Snap (10), or Pat (1) to start rhythm!</span>';
    }

    log.innerHTML = html;
    totalEl.textContent = sum;

    if (breakEl) {
        breakEl.textContent = `${claps} Clap${claps !== 1 ? 's' : ''} (${claps * 100}) + ${snaps} Snap${snaps !== 1 ? 's' : ''} (${snaps * 10}) + ${pats} Pat${pats !== 1 ? 's' : ''} (${pats}) = ${sum}`;
    }
}

// =========================================================================
// SIMULATOR 14: PLACE VALUE BREAKDOWNS (150 TO 159)
// =========================================================================
function setChart150(n) {
    playTone(450 + ((n - 150) * 15), 'sine', 0.08);

    const targetEl = document.getElementById('chartTargetNum');
    const onesDigit = document.getElementById('chartOnesDigit');
    const onesVal = document.getElementById('chartOnesValue');
    const eq = document.getElementById('chartExpandedForm');
    const word = document.getElementById('chartWordName');

    if (!targetEl) return;

    targetEl.textContent = n;
    const ones = n % 10;

    if (onesDigit) onesDigit.textContent = ones;
    if (onesVal) onesVal.textContent = `= ${ones}`;

    if (eq) eq.textContent = `100 + 50 + ${ones} = ${n}`;
    if (word) word.textContent = `"${numberToWords(n)}"`;
}

// =========================================================================
// SIMULATOR 15: NUMBER LINE JUMPS (100 TO 200)
// =========================================================================
let jumperPos = 140;

function leapStep(delta) {
    let next = jumperPos + delta;
    if (next > 200) next = 200;
    jumperPos = next;
    playTone(350 + (delta * 12), 'triangle', 0.12);
    if (jumperPos === 200) playSuccessChime();
    updateJumperView();
}

function resetJumper() {
    jumperPos = 100;
    playTone(350, 'sine', 0.08);
    updateJumperView();
}

function updateJumperView() {
    const posEl = document.getElementById('jumpCurrentPos');
    const token = document.getElementById('jumperToken');
    const log = document.getElementById('jumpActionLog');

    if (!posEl || !token) return;

    posEl.textContent = jumperPos;

    // Map 100..200 to x: 30..570 (range = 540)
    const pct = (jumperPos - 100) / 100;
    const cx = 30 + (pct * 540);
    token.setAttribute('cx', cx);

    if (log) {
        const past = jumperPos - 100;
        const left = 200 - jumperPos;
        log.textContent = `Current Spot: ${jumperPos} is ${past} steps past 100, and ${left} steps away from 200!`;
    }
}

// =========================================================================
// SIMULATOR 16: DOUBLE CENTURY GOAL (200)
// =========================================================================
function triggerDoubleCenturyCheer() {
    playSuccessChime();
    const banner = document.getElementById('doubleCenturyCelebration');
    if (banner) {
        banner.classList.remove('bg-amber-500/10');
        banner.classList.add('bg-amber-500/30', 'ring-2', 'ring-amber-400');
        setTimeout(() => {
            banner.classList.remove('bg-amber-500/30', 'ring-2', 'ring-amber-400');
            banner.classList.add('bg-amber-500/10');
        }, 1200);
    }
    speakText("Sensational achievement! You have reached two hundred, the grand Double Century! Two hundred ones, twenty tens, and two whole hundreds!");
}

// =========================================================================
// INITIALIZE SIMULATORS WHEN ENTERING SLIDE
// =========================================================================
function initSlideSimulator(slideId) {
    if (slideId === 1) renderTally();
    else if (slideId === 2) updateBaseTenView();
    else if (slideId === 3) setZeroDemo(105);
    else if (slideId === 4) renderMarketStall();
    else if (slideId === 5) initSnakesGrid();
    else if (slideId === 7) setHundredView('cricket');
    else if (slideId === 8) renderGinladiBeads();
    else if (slideId === 9) renderFlowerPetals();
    else if (slideId === 10) updateSeqView();
    else if (slideId === 11) renderMatchsticks();
    else if (slideId === 12) updateRange150(125);
    else if (slideId === 13) renderRhythmLog();
    else if (slideId === 14) setChart150(154);
    else if (slideId === 15) updateJumperView();
}

// =========================================================================
// INITIALIZATION ON DOM READY
// =========================================================================
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    goToSlide(1);
});
'''

with open(".agents/class3_maths_ch3_js.js", "w") as f:
    f.write(js_code)

print("Generated .agents/class3_maths_ch3_js.js successfully!")


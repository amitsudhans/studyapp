# -*- coding: utf-8 -*-
"""
Generate Pure Indian Male Teacher JavaScript Engine for Class 4 Science Chapter 4: Growing up with Nature
Outputs .agents/class4_science_ch4_js.js and .agents/class4_science_ch4_js.py
"""

import os

js_content = r'''
// Class 4 Science Chapter 4: Growing up with Nature - Pure Indian Male Teacher Audio Engine
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;
let cachedVoices = [];
let userPreferredVoice = "";

// Audio Feedback Chime (Web Audio API)
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {
            audioCtx = new AudioContext();
        }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playTeacherSound(isCorrect) {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (isCorrect) {
            // Melodic ascending teacher approval chime (C5 -> E5 -> G5)
            osc.type = 'sine';
            osc.frequency.setValueAtTime(523.25, now);
            osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.10);
            osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.22);
            gain.gain.setValueAtTime(0.14, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.38);
            osc.start(now);
            osc.stop(now + 0.38);
        } else {
            // Gentle encouragement tone (C4 -> A3)
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(261.63, now);
            osc.frequency.exponentialRampToValueAtTime(220.00, now + 0.14);
            gain.gain.setValueAtTime(0.10, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.26);
            osc.start(now);
            osc.stop(now + 0.26);
        }
    } catch (e) {}
}

// =================== PURE INDIAN MALE TEACHER VOICE LOGIC ===================
const femaleBlockList = [
    'female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya',
    'swara', 'veena', 'neerja', 'heera', 'kavya', 'ananya', 'aditi', 'pallavi',
    'shreya', 'vani', 'maya', 'pooja', 'sunita', 'geeta', 'seema', 'rekha',
    'victoria', 'karen', 'tessa', 'fiona', 'moira', 'alice', 'salli', 'joanna',
    'ivy', 'kendra', 'kimberly', 'amy', 'emma', 'nicole', 'russell', 'sangeeta',
    'leena', 'lekha', 'google us english', 'google english (india)', 'google हिन्दी',
    'google uk english female', 'en-in-x-end', 'en-in-x-ene', 'en-in-x-enf',
    'hi-in-x-cfc', 'hi-in-x-hie', 'hi-in-x-hid', 'shravani', 'shruti', 'alva',
    'sara', 'libby', 'sonia', 'natasha', 'clara', 'hazel', 'susan', 'catherine',
    'linda', 'mia', 'ava'
];

function isFemaleVoice(v) {
    const name = (v.name || '').toLowerCase();
    return femaleBlockList.some(kw => name.includes(kw));
}

function isIndianMaleVoice(v) {
    if (isFemaleVoice(v)) return false;
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();

    // Specific Indian Male names & neural voice codes
    const indianMaleKeywords = [
        'prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'karan', 'mohan',
        'deepak', 'kumar', 'sanjay', 'ajay', 'vijay', 'amit', 'rahul',
        'rajesh', 'vikram', 'arun', 'manish', 'suresh', 'ramesh', 'anil',
        'sunil', 'en-in-x-ahp', 'en-in-x-cxx', 'en-in-standard-b',
        'en-in-standard-c', 'en-in-wavenet-b', 'en-in-wavenet-c', 'en-in-neural2-b',
        'hi-in-standard-b', 'hi-in-standard-c', 'hi-in-wavenet-b', 'hi-in-wavenet-c'
    ];
    if (indianMaleKeywords.some(k => name.includes(k))) return true;

    // en-IN or hi-IN locale with explicit male keyword
    if ((lang.includes('en-in') || lang.includes('en_in') || lang.includes('hi-in') || lang.includes('hi_in') || name.includes('india')) && name.includes('male')) {
        return true;
    }

    return false;
}

function isGeneralMaleVoice(v) {
    if (isFemaleVoice(v)) return false;
    const name = (v.name || '').toLowerCase();
    const maleKeywords = [
        'male', 'google uk english male', 'david', 'george', 'mark', 'alex',
        'guy', 'daniel', 'oliver', 'brian', 'james', 'richard', 'ryan',
        'christopher', 'eric'
    ];
    return maleKeywords.some(k => name.includes(k));
}

function getBestVoice() {
    if (!('speechSynthesis' in window)) return null;
    let voices = cachedVoices;
    if (!voices || voices.length === 0) {
        voices = window.speechSynthesis.getVoices();
    }
    if (!voices || voices.length === 0) return null;

    // User preference priority
    if (userPreferredVoice) {
        const userChosen = voices.find(v => v.name === userPreferredVoice);
        if (userChosen) return userChosen;
    }

    // 1. Top Tier: Indian Male Teacher Voice (Prabhat, Rishi, Ravi, etc.)
    const inMale = voices.find(v => isIndianMaleVoice(v));
    if (inMale) return inMale;

    // 2. Second Tier: Dignified Male Teacher Voice
    const genMale = voices.find(v => isGeneralMaleVoice(v));
    if (genMale) return genMale;

    // 3. Third Tier: Any non-female English voice
    const nonFemaleEn = voices.find(v => (v.lang || '').toLowerCase().startsWith('en') && !isFemaleVoice(v));
    if (nonFemaleEn) return nonFemaleEn;

    // 4. Any voice not explicitly blocked as female
    const nonFemaleAny = voices.find(v => !isFemaleVoice(v));
    if (nonFemaleAny) return nonFemaleAny;

    return voices[0] || null;
}

function populateVoiceList() {
    if (!('speechSynthesis' in window)) return;
    cachedVoices = window.speechSynthesis.getVoices() || [];
    const selector = document.getElementById('voiceSelect');
    if (!selector || cachedVoices.length === 0) return;

    selector.innerHTML = '';

    // Sort voices: Indian Male first, other Male second, others last
    const sorted = [...cachedVoices].sort((a, b) => {
        const aIn = isIndianMaleVoice(a) ? 2 : (isGeneralMaleVoice(a) ? 1 : 0);
        const bIn = isIndianMaleVoice(b) ? 2 : (isGeneralMaleVoice(b) ? 1 : 0);
        return bIn - aIn;
    });

    sorted.forEach(v => {
        const opt = document.createElement('option');
        opt.value = v.name;
        if (isIndianMaleVoice(v)) {
            opt.textContent = `🇮🇳 ${v.name} [Indian Male Teacher]`;
        } else if (isGeneralMaleVoice(v)) {
            opt.textContent = `👨 ${v.name} [Male Teacher]`;
        } else if (isFemaleVoice(v)) {
            opt.textContent = `👩 ${v.name} (${v.lang})`;
        } else {
            opt.textContent = `${v.name} (${v.lang})`;
        }
        selector.appendChild(opt);
    });

    // Check stored user preference
    let stored = null;
    try {
        stored = localStorage.getItem('study_lab_voice_nature_ch4');
    } catch(e) {}

    if (stored && cachedVoices.some(v => v.name === stored)) {
        userPreferredVoice = stored;
        selector.value = stored;
    } else {
        const best = getBestVoice();
        if (best) {
            selector.value = best.name;
            userPreferredVoice = best.name;
        }
    }
}

function onVoiceChange() {
    const selector = document.getElementById('voiceSelect');
    if (!selector) return;
    userPreferredVoice = selector.value;
    try {
        localStorage.setItem('study_lab_voice_nature_ch4', userPreferredVoice);
    } catch(e) {}

    if (isSpeaking) {
        // Immediately switch voice and restart current speech
        stopAudioLecture();
        playAudioLecture();
    }
}

// Preload & Cache Voices for Instant Speech
function loadVoices() {
    if ('speechSynthesis' in window) {
        cachedVoices = window.speechSynthesis.getVoices();
        populateVoiceList();
    }
}
loadVoices();
if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = loadVoices;
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    loadVoices();
    showSlide(1);
});

function showSlide(n) {
    if (n < 1 || n > totalSlides) return;
    currentSlide = n;

    // Stop ongoing speech immediately on slide transition
    stopAudioLecture();

    // Toggle slide panes
    for (let i = 1; i <= totalSlides; i++) {
        const pane = document.getElementById(`slide-${i}`);
        if (pane) {
            if (i === currentSlide) {
                pane.classList.remove('hidden');
            } else {
                pane.classList.add('hidden');
            }
        }
    }

    // Update Slide counter & progress bar
    const currentNumEl = document.getElementById('currentSlideNum');
    if (currentNumEl) currentNumEl.textContent = currentSlide;

    const progBar = document.getElementById('chapterProgressBar');
    if (progBar) {
        const pct = (currentSlide / totalSlides) * 100;
        progBar.style.width = `${pct}%`;
    }

    // Previous Button control
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-50', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }
    }

    // Next Button & Terminal Invariant
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
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

    // Exercises (slides 17-20) are excluded from teacher lecture synthesis
    if (currentSlide > 16) {
        alert("Challenge questions are interactive quiz slides without spoken lectures.");
        return;
    }

    const slideData = SLIDES.find(s => s.id === currentSlide);
    if (!slideData || !slideData.speech || slideData.speech.trim() === '') return;

    window.speechSynthesis.cancel();
    stopSpeechKeepAlive();

    currentUtterance = new SpeechSynthesisUtterance(slideData.speech);
    
    // Explicit Indian English parameters
    currentUtterance.lang = 'en-IN';
    currentUtterance.pitch = 0.88; // Deep, resonant, patient Indian male teacher pitch
    currentUtterance.rate = 0.90;  // Articulate, measured classroom pacing for primary students

    const selectedVoice = getBestVoice();
    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
        if (isIndianMaleVoice(selectedVoice)) {
            currentUtterance.lang = selectedVoice.lang || 'en-IN';
            currentUtterance.pitch = 0.88;
            currentUtterance.rate = 0.90;
        } else {
            currentUtterance.pitch = 0.84;
            currentUtterance.rate = 0.92;
        }
        // Keep selector synced
        const selector = document.getElementById('voiceSelect');
        if (selector && selector.value !== selectedVoice.name) {
            selector.value = selectedVoice.name;
        }
    }

    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
        startSpeechKeepAlive();
    };

    currentUtterance.onend = () => {
        stopAudioLecture();
    };

    currentUtterance.onerror = () => {
        stopAudioLecture();
    };

    window.speechSynthesis.speak(currentUtterance);
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    stopSpeechKeepAlive();
    isSpeaking = false;
    currentUtterance = null;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(active) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (active) {
        btn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500');
        btn.classList.add('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
            <span class="text-xs font-bold">Stop Teacher Sound</span>
        `;
    } else {
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            <span class="text-xs font-bold">Teacher Sound Lecture</span>
        `;
    }
}

function startSpeechKeepAlive() {
    stopSpeechKeepAlive();
    keepAliveTimer = setInterval(() => {
        if (window.speechSynthesis && window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        } else {
            stopSpeechKeepAlive();
        }
    }, 9000);
}

function stopSpeechKeepAlive() {
    if (keepAliveTimer) {
        clearInterval(keepAliveTimer);
        keepAliveTimer = null;
    }
}

// =================== CHECKPOINTS & QUIZZES ===================
function checkCheckpoint(slideId, cpIdx, selectedOpt) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;

    const cp = slide.checkpoints[cpIdx];
    const isCorrect = (selectedOpt === cp.ans);
    const fbEl = document.getElementById(`cp-fb-${slideId}-${cpIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${cpIdx}`);

    // Play classroom sound
    playTeacherSound(isCorrect);

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === cp.ans) {
            btn.classList.remove('bg-slate-800', 'text-slate-300');
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        } else if (idx === selectedOpt && !isCorrect) {
            btn.classList.remove('bg-slate-800', 'text-slate-300');
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        }
    });

    if (fbEl) {
        fbEl.classList.remove('hidden');
        if (isCorrect) {
            fbEl.innerHTML = `
                <div class="p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-800/60 text-emerald-300 text-xs">
                    <strong>✓ Excellent!</strong> ${cp.exp}
                </div>
            `;
        } else {
            fbEl.innerHTML = `
                <div class="p-2.5 rounded-xl bg-rose-950/60 border border-rose-800/60 text-rose-300 text-xs">
                    <strong>✗ Let us explore:</strong> ${cp.exp}
                </div>
            `;
        }
    }
}

function checkQuiz(slideId, qIdx, selectedOpt) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;

    const q = slide.quizzes[qIdx];
    const isCorrect = (selectedOpt === q.ans);
    const fbEl = document.getElementById(`qz-fb-${slideId}-${qIdx}`);
    const solBtn = document.getElementById(`qz-sol-btn-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.qz-btn-${slideId}-${qIdx}`);

    // Play classroom sound
    playTeacherSound(isCorrect);

    btns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === q.ans) {
            btn.classList.remove('bg-slate-800', 'text-slate-300');
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        } else if (idx === selectedOpt && !isCorrect) {
            btn.classList.remove('bg-slate-800', 'text-slate-300');
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        }
    });

    if (solBtn) solBtn.classList.remove('hidden');

    if (fbEl) {
        fbEl.classList.remove('hidden');
        if (isCorrect) {
            fbEl.innerHTML = `
                <div class="p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-800/60 text-emerald-300 text-xs">
                    <strong>✓ Correct!</strong> ${q.explanation}
                </div>
            `;
        } else {
            fbEl.innerHTML = `
                <div class="p-2.5 rounded-xl bg-rose-950/60 border border-rose-800/60 text-rose-300 text-xs">
                    <strong>✗ Review:</strong> ${q.explanation}
                </div>
            `;
        }
    }
}

function toggleHint(slideId, qIdx) {
    const hintEl = document.getElementById(`qz-hint-${slideId}-${qIdx}`);
    if (hintEl) {
        hintEl.classList.toggle('hidden');
    }
}

function showSolutionModal(slideId, qIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;

    const q = slide.quizzes[qIdx];
    const modal = document.getElementById('solutionModal');
    const content = document.getElementById('modalSolutionContent');
    const title = document.getElementById('modalQuestionTitle');

    if (title) title.innerHTML = `<span>💡</span> Step-by-Step Solution: Problem ${qIdx + 1}`;

    const stepsHtml = (q.solution_steps || []).map(step => `
        <li class="flex items-start gap-2 text-xs sm:text-sm text-slate-300">
            <span class="text-amber-400 font-bold shrink-0">▸</span>
            <span>${step}</span>
        </li>
    `).join('');

    if (content) {
        content.innerHTML = `
            <div class="space-y-3">
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                    <p class="text-xs font-semibold text-slate-400">Question:</p>
                    <p class="text-xs sm:text-sm text-slate-200 mt-1">${q.q}</p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/50">
                    <p class="text-xs font-semibold text-emerald-400">Correct Answer:</p>
                    <p class="text-xs sm:text-sm text-emerald-200 mt-1 font-bold">${q.options[q.ans]}</p>
                </div>
                <div class="space-y-1.5">
                    <p class="text-xs font-bold text-slate-400">Detailed Explanatory Steps:</p>
                    <ul class="space-y-2 p-3 rounded-xl bg-slate-950 border border-slate-800">
                        ${stepsHtml}
                    </ul>
                </div>
            </div>
        `;
    }

    if (modal) modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// =================== SIMULATORS INTERACTIVITY ===================

// Sim 1: Solar Microgrid
function updateSim1(val) {
    const intensity = parseInt(val, 10);
    const sunLabel = document.getElementById('sim1-sun-label');
    const genVal = document.getElementById('sim1-gen-val');
    const batVal = document.getElementById('sim1-bat-val');
    const sunEl = document.getElementById('sim1-sun');
    const lampEl = document.getElementById('sim1-lamp');
    const skyEl = document.getElementById('sim1-sky');

    const kw = ((intensity / 100) * 5.6).toFixed(1);
    const batPct = Math.min(100, Math.round(50 + (intensity * 0.5)));

    if (sunLabel) sunLabel.textContent = `${intensity}% (${intensity > 70 ? 'Bright Sun' : intensity > 30 ? 'Moderate Sun' : 'Overcast / Sunset'})`;
    if (genVal) genVal.textContent = `${kw} kW`;
    if (batVal) batVal.textContent = `${batPct}%`;

    if (sunEl) {
        sunEl.setAttribute('r', 15 + (intensity * 0.1));
        sunEl.setAttribute('opacity', (intensity / 100) * 0.9 + 0.1);
    }

    if (lampEl) {
        lampEl.setAttribute('fill', batPct > 20 ? '#fbbf24' : '#64748b');
    }

    if (skyEl) {
        if (intensity < 30) skyEl.setAttribute('fill', '#020617');
        else if (intensity < 70) skyEl.setAttribute('fill', '#0f172a');
        else skyEl.setAttribute('fill', '#1e293b');
    }
}

function setSim1Power(mode) {
    const badge = document.getElementById('sim1-mode-badge');
    const carbonVal = document.getElementById('sim1-carbon-val');

    if (mode === 'solar') {
        if (badge) {
            badge.className = "absolute top-2 right-2 px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
            badge.textContent = "Mode: Solar Powered (Silent & Clean)";
        }
        if (carbonVal) {
            carbonVal.className = "text-base font-bold text-cyan-400";
            carbonVal.textContent = "0.0 kg (Zero)";
        }
    } else {
        if (badge) {
            badge.className = "absolute top-2 right-2 px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
            badge.textContent = "Mode: Diesel Generator (Fumes & Noise)";
        }
        if (carbonVal) {
            carbonVal.className = "text-base font-bold text-rose-400";
            carbonVal.textContent = "18.5 kg / hr (High)";
        }
    }
}

// Sim 2: Palash Tree Explorer
let sim2PollinatorIdx = 0;
const sim2Pollinators = [
    { name: "Purple Sunbird", text: "Purple Sunbird feeding on sweet nectar with its slender curved bill!", x: 130, y: 35 },
    { name: "Rose-Ringed Parakeet", text: "Rose-Ringed Parakeet nibbling flower petals and dusting yellow pollen!", x: 260, y: 40 },
    { name: "Bumblebee", text: "Bumblebee collecting nectar droplets and transferring pollen across blossoms!", x: 180, y: 15 }
];

function clickPalashBlossom() {
    sim2PollinatorIdx = (sim2PollinatorIdx + 1) % sim2Pollinators.length;
    const cur = sim2Pollinators[sim2PollinatorIdx];
    const polEl = document.getElementById('sim2-pollinator');
    const fbEl = document.getElementById('sim2-feedback');

    if (polEl) {
        polEl.setAttribute('transform', `translate(${cur.x}, ${cur.y})`);
    }
    if (fbEl) {
        fbEl.textContent = `Visitor: ${cur.text}`;
    }
}

function setPalashView(mode) {
    const box = document.getElementById('sim2-desc-box');
    if (!box) return;

    if (mode === 'nectar') {
        box.innerHTML = `<strong class="text-amber-400">Sweet Nectar:</strong> Each curved orange flower petal holds abundant nectar reserves, serving as a vital springtime food lifeline for dozens of forest bird species!`;
    } else if (mode === 'pollinators') {
        box.innerHTML = `<strong class="text-emerald-400">Avian Pollinators:</strong> Sunbirds and parakeets insert slender bills deep into petals. As they feed, golden pollen sticks to their plumage, ensuring cross-pollination!`;
    } else {
        box.innerHTML = `<strong class="text-rose-400">Natural Dye Heritage:</strong> In Gujarat and across India, dried Palash (Kesuda) petals are soaked in warm water to brew bright saffron-orange natural dye for festival play!`;
    }
}

// Sim 3: Eco-House Thermal Wall Simulator
function updateSim3Thermal(outdoor) {
    const outTemp = parseInt(outdoor, 10);
    const outLabel = document.getElementById('sim3-out-temp');
    const earthTemp = document.getElementById('sim3-earth-temp');
    const concTemp = document.getElementById('sim3-conc-temp');

    if (outLabel) outLabel.textContent = `${outTemp}°C (${outTemp > 38 ? 'Blazing Afternoon' : outTemp > 28 ? 'Warm Sun' : 'Pleasant'})`;

    const eTemp = Math.round(20 + (outTemp - 15) * 0.25);
    const cTemp = Math.round(18 + (outTemp - 15) * 0.72);

    if (earthTemp) earthTemp.textContent = `${eTemp}°C`;
    if (concTemp) concTemp.textContent = `${cTemp}°C`;
}

// Sim 4: Traditional Rice Murals
let muralMotifCount = 0;
const muralSymbols = {
    tree: `<g transform="translate(__X__, __Y__)"><line x1="20" y1="50" x2="20" y2="10" stroke="#ffffff" stroke-width="3"/><circle cx="20" cy="15" r="14" fill="none" stroke="#ffffff" stroke-width="2"/><path d="M 10 22 L 30 22 M 14 10 L 26 10 M 20 0 L 20 30" stroke="#ffffff" stroke-width="1.5"/></g>`,
    peacock: `<g transform="translate(__X__, __Y__)"><ellipse cx="20" cy="30" rx="10" ry="6" fill="none" stroke="#ffffff" stroke-width="2"/><circle cx="28" cy="24" r="4" fill="#ffffff"/><path d="M 12 30 Q 0 10 20 0 Q 15 20 18 28" fill="none" stroke="#ffffff" stroke-width="2"/></g>`,
    deer: `<g transform="translate(__X__, __Y__)"><line x1="10" y1="25" x2="35" y2="25" stroke="#ffffff" stroke-width="2.5"/><line x1="12" y1="25" x2="10" y2="45" stroke="#ffffff" stroke-width="2"/><line x1="33" y1="25" x2="35" y2="45" stroke="#ffffff" stroke-width="2"/><path d="M 35 25 L 42 12 M 40 10 L 44 2 M 38 6 L 42 6" stroke="#ffffff" stroke-width="1.5"/></g>`,
    dancers: `<g transform="translate(__X__, __Y__)"><circle cx="15" cy="12" r="4" fill="#ffffff"/><line x1="15" y1="16" x2="15" y2="30" stroke="#ffffff" stroke-width="2"/><line x1="5" y1="22" x2="25" y2="22" stroke="#ffffff" stroke-width="2"/><line x1="10" y1="42" x2="15" y2="30" stroke="#ffffff" stroke-width="2"/><line x1="20" y1="42" x2="15" y2="30" stroke="#ffffff" stroke-width="2"/></g>`
};

function stampMuralMotif(type) {
    const group = document.getElementById('sim4-motifs-group');
    const placeholder = document.getElementById('sim4-placeholder');
    if (!group) return;

    if (placeholder) placeholder.style.display = 'none';

    muralMotifCount++;
    const xPos = 20 + ((muralMotifCount * 70) % 280);
    const yPos = 20 + ((Math.floor(muralMotifCount / 4) * 50) % 70);

    const template = muralSymbols[type] || muralSymbols.tree;
    const motifHtml = template.replace('__X__', xPos).replace('__Y__', yPos);

    group.innerHTML += motifHtml;
}

function clearMuralWall() {
    const group = document.getElementById('sim4-motifs-group');
    const placeholder = document.getElementById('sim4-placeholder');
    if (group) group.innerHTML = '';
    if (placeholder) placeholder.style.display = 'block';
    muralMotifCount = 0;
}

// Sim 5: Botanical Dye Extraction
const dyePalette = {
    marigold: { color: "#facc15", text: "Bright Golden Yellow", hex: "#ca8a04", name: "Marigold Petals" },
    beetroot: { color: "#e11d48", text: "Deep Crimson-Magenta", hex: "#9f1239", name: "Beetroot Slices" },
    hibiscus: { color: "#dc2626", text: "Vibrant Scarlet Red", hex: "#991b1b", name: "Hibiscus Blossoms" },
    acacia: { color: "#78350f", text: "Earthy Bark Brown", hex: "#451a03", name: "Acacia Tree Bark" }
};

function extractDye(ingredient) {
    const data = dyePalette[ingredient] || dyePalette.marigold;
    const liquid = document.getElementById('sim5-liquid');
    const swatch = document.getElementById('sim5-swatch');
    const swatchText = document.getElementById('sim5-swatch-text');
    const steam = document.getElementById('sim5-steam');
    const potStatus = document.getElementById('sim5-pot-status');

    if (steam) steam.classList.remove('hidden');
    if (potStatus) potStatus.textContent = `Boiling: ${data.name}`;

    if (liquid) liquid.setAttribute('fill', data.color);

    if (swatch) swatch.style.backgroundColor = data.color;
    if (swatchText) {
        swatchText.textContent = data.text;
        swatchText.style.color = (ingredient === 'marigold' ? '#713f12' : '#ffffff');
    }
}

// Sim 6: Gond Patterning Studio
function setGondPattern(style) {
    const overlay = document.getElementById('sim6-pattern-overlay');
    const status = document.getElementById('sim6-status');
    if (!overlay) return;

    if (style === 'dots') {
        overlay.innerHTML = `
            <circle cx="80" cy="65" r="2" fill="#ffffff"/>
            <circle cx="95" cy="70" r="2" fill="#ffffff"/>
            <circle cx="110" cy="75" r="2" fill="#ffffff"/>
            <circle cx="125" cy="80" r="2" fill="#ffffff"/>
            <circle cx="90" cy="80" r="2" fill="#fef08a"/>
            <circle cx="105" cy="85" r="2" fill="#fef08a"/>
            <circle cx="120" cy="90" r="2" fill="#fef08a"/>
        `;
        if (status) status.textContent = "Selected Pattern: Traditional Dots (Geru Red & White Lime)";
    } else if (style === 'dashes') {
        overlay.innerHTML = `
            <line x1="75" y1="62" x2="85" y2="62" stroke="#ffffff" stroke-width="1.5"/>
            <line x1="90" y1="68" x2="100" y2="68" stroke="#ffffff" stroke-width="1.5"/>
            <line x1="105" y1="74" x2="115" y2="74" stroke="#ffffff" stroke-width="1.5"/>
            <line x1="85" y1="78" x2="95" y2="78" stroke="#fde047" stroke-width="1.5"/>
            <line x1="100" y1="84" x2="110" y2="84" stroke="#fde047" stroke-width="1.5"/>
        `;
        if (status) status.textContent = "Selected Pattern: Parallel Dashes (Ramraj Yellow Soil)";
    } else {
        overlay.innerHTML = `
            <path d="M 75 65 Q 85 58 95 65 Q 105 72 115 65" stroke="#ffffff" stroke-width="1.5" fill="none"/>
            <path d="M 80 75 Q 90 68 100 75 Q 110 82 120 75" stroke="#a7f3d0" stroke-width="1.5" fill="none"/>
        `;
        if (status) status.textContent = "Selected Pattern: Undulating Waves (Crushed Leaf Green)";
    }
}

// Sim 7: Organic Pest Control
let sim7NeemActive = true;
let sim7PlasterActive = true;

function toggleSim7Neem() {
    sim7NeemActive = !sim7NeemActive;
    const btn = document.getElementById('sim7-neem-btn');
    const layer = document.getElementById('sim7-neem-layer');

    if (btn) {
        btn.textContent = `🌿 Neem Lining: ${sim7NeemActive ? 'Active' : 'Disabled'}`;
        btn.className = sim7NeemActive
            ? "p-2.5 rounded-xl bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 text-xs font-semibold text-center transition"
            : "p-2.5 rounded-xl bg-slate-800 text-slate-400 border border-slate-700 text-xs font-semibold text-center transition";
    }
    if (layer) layer.style.opacity = sim7NeemActive ? "1" : "0";
    evaluateSim7Status();
}

function toggleSim7Plaster() {
    sim7PlasterActive = !sim7PlasterActive;
    const btn = document.getElementById('sim7-plaster-btn');
    const pot = document.getElementById('sim7-pot-body');

    if (btn) {
        btn.textContent = `🧱 Dung Plaster: ${sim7PlasterActive ? 'Sealed' : 'Cracked / None'}`;
        btn.className = sim7PlasterActive
            ? "p-2.5 rounded-xl bg-amber-600/30 text-amber-300 border border-amber-500/40 text-xs font-semibold text-center transition"
            : "p-2.5 rounded-xl bg-slate-800 text-slate-400 border border-slate-700 text-xs font-semibold text-center transition";
    }
    if (pot) pot.setAttribute('stroke', sim7PlasterActive ? "#7c2d12" : "#ef4444");
    evaluateSim7Status();
}

function evaluateSim7Status() {
    const pestStatus = document.getElementById('sim7-pest-status');
    const lifeStatus = document.getElementById('sim7-life-status');

    if (sim7NeemActive && sim7PlasterActive) {
        if (pestStatus) { pestStatus.textContent = "0% (Completely Repelled)"; pestStatus.className = "text-sm font-bold text-emerald-400"; }
        if (lifeStatus) { lifeStatus.textContent = "12+ Months"; lifeStatus.className = "text-sm font-bold text-amber-400"; }
    } else if (sim7NeemActive || sim7PlasterActive) {
        if (pestStatus) { pestStatus.textContent = "15% (Partial Vulnerability)"; pestStatus.className = "text-sm font-bold text-amber-400"; }
        if (lifeStatus) { lifeStatus.textContent = "4 - 6 Months"; lifeStatus.className = "text-sm font-bold text-amber-400"; }
    } else {
        if (pestStatus) { pestStatus.textContent = "80% Severe Weevil Infestation!"; pestStatus.className = "text-sm font-bold text-rose-500"; }
        if (lifeStatus) { lifeStatus.textContent = "< 1 Month (Grains Spoil)"; lifeStatus.className = "text-sm font-bold text-rose-400"; }
    }
}

// Sim 8: Jenu Kuruba Honey Harvest Protocol
function runSim8Step(step) {
    const prompt = document.getElementById('sim8-prompt');
    const smoke = document.getElementById('sim8-smoke');
    const outerComb = document.getElementById('sim8-outer-honey');

    if (step === 'song') {
        if (prompt) prompt.textContent = "Step 2: Gentle apology song completed with humility. Now apply herbal smoke!";
        if (smoke) smoke.style.opacity = "0";
    } else if (step === 'smoke') {
        if (prompt) prompt.textContent = "Step 3: Mild herbal smoke calms the colony safely. Slice only outer surplus!";
        if (smoke) smoke.style.opacity = "1";
    } else if (step === 'harvest') {
        if (prompt) prompt.textContent = "Harvest Success: Outer surplus honey gathered! Brood comb remains 100% intact.";
        if (outerComb) outerComb.style.opacity = "0.3";
    }
}

// Sim 9: Himalayan Tumri Bottle Gourd Crafting Lab
function setTumriStage(stage) {
    const body = document.getElementById('sim9-gourd-body');
    const name = document.getElementById('sim9-stage-name');
    const temp = document.getElementById('sim9-water-temp');

    if (stage === 1) {
        if (body) body.setAttribute('fill', '#65a30d');
        if (name) name.textContent = "Stage 1: Fresh Green Bottle Gourd";
        if (temp) temp.textContent = "Not Cured Yet";
    } else if (stage === 2) {
        if (body) body.setAttribute('fill', '#eab308');
        if (name) name.textContent = "Stage 2: Sun-Drying on Mountain Terraces";
        if (temp) temp.textContent = "Rind Hardening...";
    } else if (stage === 3) {
        if (body) body.setAttribute('fill', '#854d0e');
        if (name) name.textContent = "Stage 3: Smoke-Cured Woody Shell";
        if (temp) temp.textContent = "Waterproof Inner Core";
    } else {
        if (body) body.setAttribute('fill', '#ca8a04');
        if (name) name.textContent = "Stage 4: Cured Tumri Vessel in Daily Use";
        if (temp) temp.textContent = "14°C (Naturally Cold Spring Water)";
    }
}

// Sim 10: Forest First-Aid & Repellent Station
function setSim10Remedy(type) {
    const icon = document.getElementById('sim10-icon-box');
    const title = document.getElementById('sim10-title');
    const desc = document.getElementById('sim10-desc');
    const tag = document.getElementById('sim10-tag');

    if (type === 'repellent') {
        if (icon) icon.textContent = "🦟";
        if (title) title.textContent = "Neem Mosquito Shield";
        if (desc) desc.textContent = "Blend cold-pressed neem seed oil with coconut oil. Apply to arms and ankles to safely repel biting mosquitoes.";
        if (tag) tag.textContent = "Active: Azadirachtin Bio-Shield";
    } else {
        if (icon) icon.textContent = "🩹";
        if (title) title.textContent = "Turmeric Scratch Healer";
        if (desc) desc.textContent = "Wash trail scratch with clean water. Apply fresh golden turmeric paste to prevent bacterial infection.";
        if (tag) tag.textContent = "Active: Curcumin Antiseptic";
    }
}

// Sim 11: Kitchen Ayurvedic Pharmacy
const herbDetails = {
    tulsi: { icon: "🌿", name: "Tulsi (Holy Basil)", part: "Leaves", use: "Brewed with black pepper and honey to soothe persistent coughs, colds, and bronchial irritation.", comp: "Key Compound: Eugenol & Antioxidants" },
    ajwain: { icon: "🌾", name: "Ajwain (Carom)", part: "Seeds", use: "Chewed with rock salt to quickly release thymol oils that ease indigestion, gas, and stomach cramps.", comp: "Key Compound: Volatile Thymol" },
    ginger: { icon: "🫚", name: "Adrak (Ginger)", part: "Rhizome", use: "Crushed in hot herbal tea to warm digestive fire, relieve nausea, and soothe throat soreness.", comp: "Key Compound: Gingerols & Shogaols" },
    mint: { icon: "🍃", name: "Pudina (Mint)", part: "Leaves", use: "Infused in cool water to reduce body heat, relieve headaches, and freshen digestive breath.", comp: "Key Compound: Menthol Essential Oil" }
};

function selectHerb(herb) {
    const data = herbDetails[herb] || herbDetails.tulsi;
    const icon = document.getElementById('sim11-plant-icon');
    const name = document.getElementById('sim11-plant-name');
    const part = document.getElementById('sim11-plant-part');
    const use = document.getElementById('sim11-remedy-use');
    const comp = document.getElementById('sim11-compound');

    if (icon) icon.textContent = data.icon;
    if (name) name.textContent = data.name;
    if (part) part.textContent = data.part;
    if (use) use.textContent = data.use;
    if (comp) comp.textContent = data.comp;
}

// Sim 12: Solar Harvest Night Celebration
let drumBeatCount = 0;
function playHarvestDrum(drum) {
    drumBeatCount++;
    const fb = document.getElementById('sim12-rhythm-feedback');
    const wave = document.getElementById('sim12-wave');
    const dancers = document.getElementById('sim12-dancers');

    const soundText = (drum === 'dhol') ? "DHUM-DHUM! Heavy bass resonance reverberates!" : "TAK-TAK-DHIN! Crisp bronze nagada strike!";
    if (fb) fb.textContent = `Rhythm ${drumBeatCount}: ${soundText}`;

    if (wave) {
        wave.setAttribute('opacity', '0.8');
        wave.setAttribute('r', '40');
        setTimeout(() => {
            wave.setAttribute('opacity', '0');
            wave.setAttribute('r', '20');
        }, 300);
    }

    if (dancers) {
        const angle = (drumBeatCount % 2 === 0) ? 3 : -3;
        dancers.setAttribute('transform', `rotate(${angle}, 150, 110)`);
    }
}

// Sim 13: Protected Sacred Grove & Hydrology
function triggerGroveRain() {
    const drops = document.getElementById('sim13-raindrops');
    const aquifer = document.getElementById('sim13-aquifer');
    const absorb = document.getElementById('sim13-absorb');
    const spring = document.getElementById('sim13-spring');

    if (drops) drops.style.opacity = "1";
    if (absorb) absorb.textContent = "98% (Infiltrating Subsoil)";
    if (spring) spring.textContent = "Replenishing Village Aquifers!";

    setTimeout(() => {
        if (drops) drops.style.opacity = "0";
        if (absorb) absorb.textContent = "95% (Natural Sponge)";
        if (spring) spring.textContent = "Flowing Year-Round";
    }, 1800);
}

// Sim 14: Regional Nature Festivals
const festivalDetails = {
    vat: { icon: "🌳", name: "Vat Purnima", region: "Maharashtra & Gujarat", desc: "Women tie sacred threads around ancient Banyan trees, honoring their sprawling canopies that generate abundant oxygen and protect wildlife.", action: "Ecological Focus: Air Purification & Tree Longevity" },
    hari: { icon: "🌱", name: "Hari Jiroti", region: "Central Farming Belts", desc: "Families plant saplings of native fruit trees like mango, jamun, and amla along roads and field borders before monsoon rains arrive.", action: "Ecological Focus: Native Fruit Tree Planting" },
    elephant: { icon: "🐘", name: "Kaziranga Elephant Festival", region: "Assam", desc: "Celebrates wild Asian elephants as ecosystem engineers that disperse seeds and create natural clearings across dense rainforests.", action: "Ecological Focus: Keystone Wildlife Conservation" }
};

function setFestival(fest) {
    const data = festivalDetails[fest] || festivalDetails.vat;
    const icon = document.getElementById('sim14-badge-icon');
    const name = document.getElementById('sim14-fest-name');
    const region = document.getElementById('sim14-region');
    const desc = document.getElementById('sim14-fest-desc');
    const action = document.getElementById('sim14-action');

    if (icon) icon.textContent = data.icon;
    if (name) name.textContent = data.name;
    if (region) region.textContent = data.region;
    if (desc) desc.textContent = data.desc;
    if (action) action.textContent = data.action;
}

// Sim 15: Everyday Conservation Action Tracker
function updateSim15Score() {
    let score = 0;
    if (document.getElementById('sim15-chk-paper')?.checked) score += 25;
    if (document.getElementById('sim15-chk-plastic')?.checked) score += 25;
    if (document.getElementById('sim15-chk-water')?.checked) score += 25;
    if (document.getElementById('sim15-chk-compost')?.checked) score += 25;

    const scoreEl = document.getElementById('sim15-score');
    const badgeEl = document.getElementById('sim15-badge');

    if (scoreEl) scoreEl.textContent = score;

    if (badgeEl) {
        if (score === 100) {
            badgeEl.className = "px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-bold";
            badgeEl.textContent = "🌟 Forest Guardian";
        } else if (score >= 50) {
            badgeEl.className = "px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-bold";
            badgeEl.textContent = "🌿 Eco Apprentice";
        } else {
            badgeEl.className = "px-3 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 text-xs font-bold";
            badgeEl.textContent = "🌱 Getting Started";
        }
    }
}

// Sim 16: Custom Herbal Garden Planner
const gardenPlots = [
    [
        { icon: "🌿", label: "Tulsi (Sun)" },
        { icon: "🫚", label: "Ginger (Rhizome)" },
        { icon: "🌾", label: "Lemongrass (Sun)" }
    ],
    [
        { icon: "🪨", label: "Pebble Path" },
        { icon: "🧱", label: "Terracotta Border" }
    ],
    [
        { icon: "🌼", label: "Marigold (Pest Guard)" },
        { icon: "🌺", label: "Hibiscus (Bloom)" }
    ],
    [
        { icon: "🪴", label: "Aloe Vera (Shade)" },
        { icon: "🌱", label: "Coriander (Partial Shade)" }
    ],
    [
        { icon: "🥣", label: "Bird Water Pot" },
        { icon: "🛖", label: "Mini Composter" }
    ],
    [
        { icon: "🍃", label: "Mint (Cool Shade)" },
        { icon: "🌿", label: "Brahmi (Moist Shade)" }
    ]
];

const cellIndices = [0, 0, 0, 0, 0, 0];

function plantGardenCell(cellIdx) {
    const cell = document.getElementById(`sim16-cell-${cellIdx}`);
    if (!cell || !gardenPlots[cellIdx]) return;

    cellIndices[cellIdx] = (cellIndices[cellIdx] + 1) % gardenPlots[cellIdx].length;
    const current = gardenPlots[cellIdx][cellIndices[cellIdx]];

    cell.innerHTML = `
        <span class="text-lg">${current.icon}</span>
        <span class="text-[10px] text-amber-300 font-bold">${current.label}</span>
    `;
}
'''.strip()

out_js_path = ".agents/class4_science_ch4_js.js"
with open(out_js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

out_py_path = ".agents/class4_science_ch4_js.py"
with open(out_py_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Science Chapter 4 JavaScript Engine Python Wrapper"""\n\n')
    f.write(f"JS_ENGINE = {repr(js_content)}\n")

print(f"Generated {out_js_path} and {out_py_path} successfully!")

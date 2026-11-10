# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 5: Food for Health JavaScript Engine Builder
Generates .agents/class4_science_ch5_js.js and .agents/class4_science_ch5_js.py
"""

import os

js_code = """// Class 4 Science Chapter 5: Food for Health - Pure Indian Male Teacher Audio Engine
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
        stored = localStorage.getItem('study_lab_voice_food_ch5');
    } catch (e) {}

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
        localStorage.setItem('study_lab_voice_food_ch5', userPreferredVoice);
    } catch (e) {}

    if (isSpeaking) {
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

    // Stop active audio lecture when moving between slides
    if (isSpeaking) {
        stopAudioLecture();
    }

    // Hide all slides
    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) {
            el.classList.add('hidden');
        }
    }

    // Show target slide
    const target = document.getElementById(`slide-${n}`);
    if (target) {
        target.classList.remove('hidden');
    }

    // Update Header / Progress
    const currentNumEl = document.getElementById('currentSlideNum');
    if (currentNumEl) currentNumEl.textContent = n;

    const progBar = document.getElementById('chapterProgressBar');
    if (progBar) {
        const pct = (n / totalSlides) * 100;
        progBar.style.width = `${pct}%`;
    }

    // Update Audio Lecture Button state
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (n > 16) {
            audioBtn.style.opacity = '0.5';
            audioBtn.title = "Challenge questions are interactive quiz slides without spoken lectures.";
        } else {
            audioBtn.style.opacity = '1';
            audioBtn.title = "Listen to Pure Indian Male Teacher Lecture";
        }
    }

    // Previous Button
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.disabled = (n === 1);
        if (n === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
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
        btn.classList.add('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clip-rule="evenodd"></path></svg>
            <span class="text-xs font-bold">Stop Lecture</span>
        `;
    } else {
        btn.classList.remove('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
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

// =================== CHECKPOINTS & QUIZ HANDLERS ===================
function checkAnswer(slideId, cpIdx, selectedOption, btn) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;

    const cp = slide.checkpoints[cpIdx];
    const isCorrect = (selectedOption === cp.ans);
    const parentContainer = btn.closest('.checkpoint-card');

    if (parentContainer) {
        const optionBtns = parentContainer.querySelectorAll('button');
        optionBtns.forEach(b => {
            b.disabled = true;
            b.classList.remove('hover:border-emerald-500', 'hover:bg-slate-800');
        });
    }

    const fb = document.getElementById(`fb-${slideId}-${cpIdx}`);

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500', 'font-bold');
        playTeacherSound(true);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-emerald-950/80 border border-emerald-800 text-xs text-emerald-300">
                    <span class="font-bold">✓ Splendid scientific reasoning!</span> ${cp.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500', 'font-bold');
        playTeacherSound(false);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-amber-950/80 border border-amber-800 text-xs text-amber-300">
                    <span class="font-bold">Notice carefully:</span> Correct answer is <strong>${cp.ans}</strong>. ${cp.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    }
}

function checkQuizAnswer(qId, selectedOption, btn) {
    let question = null;
    for (let s of SLIDES) {
        if (s.questions) {
            const found = s.questions.find(q => q.id === qId);
            if (found) {
                question = found;
                break;
            }
        }
    }
    if (!question) return;

    const isCorrect = (selectedOption === question.ans);
    const parentCard = btn.closest('.quiz-question-card');

    if (parentCard) {
        const optionBtns = parentCard.querySelectorAll('.quiz-option-btn');
        optionBtns.forEach(b => {
            b.disabled = true;
            b.classList.remove('hover:border-emerald-500', 'hover:bg-slate-800');
        });
    }

    const fb = document.getElementById(`quiz-fb-${qId}`);

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500', 'font-bold');
        playTeacherSound(true);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-emerald-950/80 border border-emerald-800 text-xs text-emerald-300">
                    <span class="font-bold">✓ Outstanding answer!</span> ${question.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500', 'font-bold');
        playTeacherSound(false);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-amber-950/80 border border-amber-800 text-xs text-amber-300">
                    <span class="font-bold">Review Scientific Principle:</span> Correct answer is <strong>${question.ans}</strong>. ${question.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    }
}

function showModalSolution(qId) {
    let question = null;
    for (let s of SLIDES) {
        if (s.questions) {
            const found = s.questions.find(q => q.id === qId);
            if (found) {
                question = found;
                break;
            }
        }
    }
    if (!question) return;

    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const contentEl = document.getElementById('modalContent');
    if (!modal || !titleEl || !contentEl) return;

    titleEl.textContent = `Scientific Solution: ${question.q}`;
    contentEl.innerHTML = `
        <div class="space-y-3 text-xs sm:text-sm text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="font-bold text-amber-400 block mb-1">Step 1: Identifying Core Principles</span>
                <p>${question.solution_steps.step1}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="font-bold text-emerald-400 block mb-1">Step 2: Analyzing Biological Context</span>
                <p>${question.solution_steps.step2}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="font-bold text-cyan-400 block mb-1">Step 3: Conclusive Nutritional Deduction</span>
                <p>${question.solution_steps.step3}</p>
            </div>
            <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/40 text-emerald-300">
                <strong>Correct Conclusion:</strong> ${question.ans}
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}

function closeModalSolution() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// =================== BESPOKE SIMULATOR INTERACTIVE SCRIPTS ===================
// Sim 1: Regional Culinary Map Explorer
const regionalData = {
    west: {
        badge: "Western India",
        icon: "🧆",
        name: "Steamed Dhokla",
        state: "Gujarat",
        ingredients: "Fermented gram flour (besan), ginger, turmeric, and light mustard tempering.",
        benefit: "Light, easily digestible plant protein enriched by natural microbial fermentation."
    },
    north: {
        badge: "Northern India",
        icon: "🥟",
        name: "Litti Chokha & Siddu",
        state: "Bihar & Himachal Pradesh",
        ingredients: "Roasted whole wheat, spiced sattu (roasted gram), mashed brinjal, and walnut siddu.",
        benefit: "Dense complex carbohydrates, dietary fiber, and plant protein for sustained stamina."
    },
    east: {
        badge: "Eastern India",
        icon: "🍮",
        name: "Chhena Poda",
        state: "Odisha",
        ingredients: "Fresh cottage cheese (chhena), cardamom, unrefined jaggery, baked in sal leaves.",
        benefit: "Concentrated dairy protein and bioavailable calcium for sturdy bone development."
    },
    south: {
        badge: "Southern India",
        icon: "🍘",
        name: "Ragi Laddu & Jowar Upma",
        state: "Karnataka & Andhra Pradesh",
        ingredients: "Roasted finger millet (ragi), cracked sorghum (jowar), curry leaves, and mustard seeds.",
        benefit: "Exceptional dietary calcium, iron, and slow-release fiber that prevents fatigue."
    }
};

function setRegionalDish(reg) {
    const data = regionalData[reg] || regionalData.west;
    const badge = document.getElementById('sim1-badge');
    const icon = document.getElementById('sim1-dish-icon');
    const name = document.getElementById('sim1-dish-name');
    const state = document.getElementById('sim1-state');
    const ing = document.getElementById('sim1-dish-ingredients');
    const ben = document.getElementById('sim1-benefit');

    if (badge) badge.textContent = data.badge;
    if (icon) icon.textContent = data.icon;
    if (name) name.textContent = data.name;
    if (state) state.textContent = data.state;
    if (ing) ing.textContent = data.ingredients;
    if (ben) ben.textContent = data.benefit;
}

// Sim 2: Ugadi Pachadi Flavor Blender
const pachadiIngredients = {
    neem: { name: "Neem Flowers", taste: "Bitter (Tikta)", color: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30" },
    jaggery: { name: "Jaggery", taste: "Sweet (Madhura)", color: "bg-amber-500/20 text-amber-300 border-amber-500/30" },
    mango: { name: "Raw Mango", taste: "Astringent (Kashaya)", color: "bg-lime-500/20 text-lime-300 border-lime-500/30" },
    tamarind: { name: "Tamarind Juice", taste: "Sour (Amla)", color: "bg-yellow-500/20 text-yellow-300 border-yellow-500/30" },
    salt: { name: "Rock Salt", taste: "Salty (Lavana)", color: "bg-cyan-500/20 text-cyan-300 border-cyan-500/30" },
    chili: { name: "Green Chili", taste: "Pungent (Katu)", color: "bg-rose-500/20 text-rose-300 border-rose-500/30" }
};
let addedPachadi = new Set();

function addPachadiIngredient(key) {
    if (pachadiIngredients[key]) {
        addedPachadi.add(key);
    }
    updatePachadiUI();
}

function resetPachadi() {
    addedPachadi.clear();
    updatePachadiUI();
}

function updatePachadiUI() {
    const count = addedPachadi.size;
    const countEl = document.getElementById('sim2-count');
    const statusEl = document.getElementById('sim2-status');
    const progEl = document.getElementById('sim2-progress');
    const tagsEl = document.getElementById('sim2-bowl-tags');

    if (countEl) countEl.textContent = `${count} of 6 Tastes Added`;
    if (progEl) progEl.style.width = `${(count / 6) * 100}%`;

    if (statusEl) {
        if (count === 6) {
            statusEl.textContent = "🌟 Perfect Sensory & Digestive Harmony!";
            statusEl.className = "text-emerald-400 font-bold";
        } else if (count > 0) {
            statusEl.textContent = "Blending Complementary Tastes...";
            statusEl.className = "text-amber-400 font-semibold";
        } else {
            statusEl.textContent = "Bowl is Empty";
            statusEl.className = "text-slate-400";
        }
    }

    if (tagsEl) {
        if (count === 0) {
            tagsEl.innerHTML = '<span class="text-[10px] text-slate-500 italic">No ingredients mixed yet.</span>';
        } else {
            let html = '';
            addedPachadi.forEach(k => {
                const item = pachadiIngredients[k];
                html += `<span class="px-2 py-0.5 rounded text-[10px] font-bold border ${item.color}">${item.name} (${item.taste})</span>`;
            });
            tagsEl.innerHTML = html;
        }
    }
}

// Sim 3: Ayurvedic Shad Rasa Taste Wheel
const rasaData = {
    sweet: {
        badge: "Madhura (Sweet)",
        sanskrit: "Madhura Rasa",
        icon: "🍯",
        action: "Energy & Tissue Growth",
        sources: "Ripe fruits, pure honey, whole grains, sugarcane, sweet potato.",
        role: "Builds bodily tissues, supplies sustained cellular energy, and calms nerve excitement."
    },
    sour: {
        badge: "Amla (Sour)",
        sanskrit: "Amla Rasa",
        icon: "🍋",
        action: "Digestive Fire & Salivation",
        sources: "Lemons, curd, tamarind, amla, fermented foods.",
        role: "Stimulates gastric secretions, sharpens appetite, and enhances mineral absorption."
    },
    salty: {
        badge: "Lavana (Salty)",
        sanskrit: "Lavana Rasa",
        icon: "🧂",
        action: "Electrolyte & Fluid Balance",
        sources: "Rock salt (sendha namak), sea salt, natural kelp.",
        role: "Maintains hydration balance, regulates nerve impulses, and stimulates digestive acids."
    },
    pungent: {
        badge: "Katu (Pungent)",
        sanskrit: "Katu Rasa",
        icon: "🌶️",
        action: "Circulation & Mucus Clearance",
        sources: "Ginger, black pepper, green chilies, mustard seeds.",
        role: "Stimulates warm blood flow, clears respiratory passages, and kindles sluggish metabolism."
    },
    bitter: {
        badge: "Tikta (Bitter)",
        sanskrit: "Tikta Rasa",
        icon: "🌿",
        action: "Internal Cleansing & Immunity",
        sources: "Neem, bitter gourd (karela), fenugreek (methi), turmeric.",
        role: "Detoxifies bodily tissues, tones the liver, and strengthens natural immunity."
    },
    astringent: {
        badge: "Kashaya (Astringent)",
        sanskrit: "Kashaya Rasa",
        icon: "🍌",
        action: "Tissue Toning & Gut Firming",
        sources: "Raw bananas, pomegranate seeds, dried lentils, triphala.",
        role: "Tones internal mucous membranes, reduces excess secretions, and aids healthy stool formation."
    }
};

function selectRasa(taste) {
    const data = rasaData[taste] || rasaData.sweet;
    const badge = document.getElementById('sim3-badge');
    const sanskrit = document.getElementById('sim3-sanskrit');
    const icon = document.getElementById('sim3-icon');
    const action = document.getElementById('sim3-action-tag');
    const sources = document.getElementById('sim3-sources');
    const role = document.getElementById('sim3-role');

    if (badge) badge.textContent = data.badge;
    if (sanskrit) sanskrit.textContent = data.sanskrit;
    if (icon) icon.textContent = data.icon;
    if (action) action.textContent = data.action;
    if (sources) sources.textContent = data.sources;
    if (role) role.textContent = data.role;
}

// Sim 4: Climate-Smart Millet Superfood Analyzer
const milletData = {
    ragi: {
        badge: "Ragi (Finger Millet)",
        calciumWidth: "95%",
        calciumVal: "344 mg / 100g (Highest of all grains)",
        ironWidth: "60%",
        ironVal: "3.9 mg / 100g",
        fiberWidth: "85%",
        fiberVal: "11.5 g / 100g",
        dish: "Steamed Ragi Laddu and Ragi Mudde with vegetable stew for sturdy bone density."
    },
    bajra: {
        badge: "Bajra (Pearl Millet)",
        calciumWidth: "42%",
        calciumVal: "42 mg / 100g",
        ironWidth: "95%",
        ironVal: "8.0 mg / 100g (Super Iron Power)",
        fiberWidth: "80%",
        fiberVal: "11.3 g / 100g",
        dish: "Winter Bajra Rotla with white butter and jaggery for internal warmth and stamina."
    },
    jowar: {
        badge: "Jowar (Sorghum)",
        calciumWidth: "25%",
        calciumVal: "25 mg / 100g",
        ironWidth: "65%",
        ironVal: "4.1 mg / 100g",
        fiberWidth: "75%",
        fiberVal: "9.7 g / 100g (Digestive Cleanse)",
        dish: "Fluffy Jowar Upma and crisp Jowar Bhakri for smooth digestion and steady energy."
    },
    barley: {
        badge: "Barley (Jau)",
        calciumWidth: "33%",
        calciumVal: "33 mg / 100g",
        ironWidth: "55%",
        ironVal: "3.6 mg / 100g",
        fiberWidth: "95%",
        fiberVal: "17.3 g / 100g (Highest Fiber)",
        dish: "Nutritious Jau Daliya (porridge) and cooling barley water for kidney flushing."
    }
};

function inspectMillet(grain) {
    const data = milletData[grain] || milletData.ragi;
    const badge = document.getElementById('sim4-badge');
    const barC = document.getElementById('sim4-bar-calcium');
    const valC = document.getElementById('sim4-val-calcium');
    const barI = document.getElementById('sim4-bar-iron');
    const valI = document.getElementById('sim4-val-iron');
    const barF = document.getElementById('sim4-bar-fiber');
    const valF = document.getElementById('sim4-val-fiber');
    const dish = document.getElementById('sim4-dish');

    if (badge) badge.textContent = data.badge;
    if (barC) barC.style.width = data.calciumWidth;
    if (valC) valC.textContent = data.calciumVal;
    if (barI) barI.style.width = data.ironWidth;
    if (valI) valI.textContent = data.ironVal;
    if (barF) barF.style.width = data.fiberWidth;
    if (valF) valF.textContent = data.fiberVal;
    if (dish) dish.textContent = data.dish;
}

// Sim 5: Nutrient Synergy Biological Engine
const synergyDetails = {
    carbs: {
        icon: "⚡",
        organ: "Brain & Muscle Cellular Fuel",
        desc: "Breaks down into circulating blood glucose, powering cognitive focus in class and active sprinting on the playground.",
        example: "Top Sources: Brown rice, whole wheat rotis, sweet potatoes, and millets."
    },
    protein: {
        icon: "🧱",
        organ: "Muscle Tissue & Cellular Repair",
        desc: "Constructs muscular fibers, synthesizes antibodies against germs, and repairs damaged tissues after minor scrapes.",
        example: "Top Sources: Soybean, yellow lentils, paneer, curd, eggs, and cracked nuts."
    },
    fat: {
        icon: "🛡️",
        organ: "Organ Cushioning & Vitamin Absorption",
        desc: "Insulates internal organs against cold temperatures and enables absorption of fat-soluble vitamins (A, D, E, K).",
        example: "Top Sources: Pure cow ghee, white butter, mustard oil, and roasted almonds."
    },
    vitamins: {
        icon: "🌟",
        organ: "Immune Armor & Vision Sharpness",
        desc: "Mobilizes white blood cells against viral pathogens and maintains clear night vision and healthy skin.",
        example: "Top Sources: Fresh amla, ripe papaya, sweet oranges, and crisp carrots."
    },
    minerals: {
        icon: "🦴",
        organ: "Bone Matrix & Oxygen Transport",
        desc: "Builds dense calcium bone lattices and provides iron to construct oxygen-carrying hemoglobin in red blood cells.",
        example: "Top Sources: Ragi, dark spinach, fenugreek leaves, and sesame seeds."
    }
};

function activateSynergy(nutrient) {
    const data = synergyDetails[nutrient] || synergyDetails.carbs;
    const icon = document.getElementById('sim5-icon');
    const organ = document.getElementById('sim5-organ');
    const desc = document.getElementById('sim5-desc');
    const example = document.getElementById('sim5-example');

    if (icon) icon.textContent = data.icon;
    if (organ) organ.textContent = data.organ;
    if (desc) desc.textContent = data.desc;
    if (example) example.textContent = data.example;
}

// Sim 6: Metabolic Energy Calorie Meter
function selectCalorieFuel(type) {
    const readout = document.getElementById('sim6-readout');
    const gauge = document.getElementById('sim6-gauge');

    if (type === 'carb') {
        if (readout) readout.textContent = "1g Carbohydrate yields 4 kcal of steady, fast-acting glucose for brain and muscles.";
        if (gauge) gauge.textContent = "⚡ Fast Cellular Release";
    } else {
        if (readout) readout.textContent = "1g Healthy Fat yields 9 kcal: more than 2x concentrated metabolic energy reserve!";
        if (gauge) gauge.textContent = "🔥 Dense Long-Lasting Fuel";
    }
}

// Sim 7: Protein Cellular Muscle Builder
function repairMuscleFiber() {
    const f1 = document.getElementById('sim7-fiber1');
    const f2 = document.getElementById('sim7-fiber2');
    const bridge = document.getElementById('sim7-bridge');
    const status = document.getElementById('sim7-status');

    if (f1) { f1.classList.remove('bg-rose-500'); f1.classList.add('bg-emerald-500', 'w-24'); }
    if (f2) { f2.classList.remove('bg-rose-500'); f2.classList.add('bg-emerald-500', 'w-24'); }
    if (bridge) bridge.textContent = "🤝";
    if (status) {
        status.textContent = "✨ Amino acids synthesized new muscle fibers! Tissues repaired stronger and more resilient.";
        status.className = "text-emerald-300 font-bold";
    }

    setTimeout(() => {
        if (f1) { f1.classList.remove('bg-emerald-500', 'w-24'); f1.classList.add('bg-rose-500', 'w-20'); }
        if (f2) { f2.classList.remove('bg-emerald-500', 'w-24'); f2.classList.add('bg-rose-500', 'w-20'); }
        if (bridge) bridge.textContent = "⚡";
        if (status) {
            status.textContent = "Tissues fatigued after sports play. Click 'Supply Protein' to weave new fibers!";
            status.className = "text-amber-300 font-semibold";
        }
    }, 3200);
}

// Sim 8: Immune Shield Vitamin Defender
function deployShield(food) {
    const score = document.getElementById('sim8-score');
    const msg = document.getElementById('sim8-msg');
    const badge = document.getElementById('sim8-badge');

    if (food === 'amla') {
        if (msg) msg.textContent = "🍈 Amla Vitamin C deployed: White blood cells multiplied, destroying microbial invaders!";
        if (badge) { badge.textContent = "Germs Neutralized"; badge.className = "px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold"; }
        if (score) score.textContent = "Immunity: 100%";
    } else if (food === 'carrot') {
        if (msg) msg.textContent = "🥕 Carrot Vitamin A deployed: Epithelial skin barrier fortified & visual acuity sharpened!";
        if (badge) { badge.textContent = "Cellular Barrier Strong"; badge.className = "px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold"; }
    } else {
        if (msg) msg.textContent = "🥬 Spinach Iron deployed: Hemoglobin replenished, circulating oxygen to every organ!";
        if (badge) { badge.textContent = "Oxygen Rich"; badge.className = "px-2 py-0.5 rounded bg-lime-500/20 text-lime-300 border border-lime-500/30 font-bold"; }
    }
}

// Sim 9: Processed Snack Nutrient Stripper
function compareSnack(type) {
    const badge = document.getElementById('sim9-badge');
    const vit = document.getElementById('sim9-vit');
    const risk = document.getElementById('sim9-risk');
    const rec = document.getElementById('sim9-rec');

    if (type === 'junk') {
        if (badge) { badge.textContent = "Junk Warning"; badge.className = "text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold"; }
        if (vit) { vit.textContent = "Almost Zero (Stripped during processing)"; vit.className = "text-rose-400 font-bold"; }
        if (risk) { risk.textContent = "Extremely High (Trans fats, sodium, refined sugar)"; risk.className = "text-rose-400 font-bold"; }
        if (rec) rec.textContent = "Avoid regular consumption; leads to dental cavities and metabolic fatigue.";
    } else {
        if (badge) { badge.textContent = "Nutrient Dense"; badge.className = "text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold"; }
        if (vit) { vit.textContent = "Rich in Magnesium, Calcium, Fiber & Natural Vitamins"; vit.className = "text-emerald-400 font-bold"; }
        if (risk) { risk.textContent = "Zero Harmful Trans Fats & Zero Synthetic Additives"; risk.className = "text-emerald-400 font-bold"; }
        if (rec) rec.textContent = "Excellent everyday choice for clean physical stamina and long-term vitality.";
    }
}

// Sim 11: Pan-Indian Thali Builder
const thaliData = {
    gujarat: {
        badge: "Gujarati Thali",
        title: "Traditional Gujarati Thali",
        items: [
            { icon: "🫓", name: "Rotli / Thepla", desc: "Energy Grains" },
            { icon: "🥣", name: "Sweet-Tart Dal", desc: "Protein & Spices" },
            { icon: "🥬", name: "Ringan Shaak", desc: "Protective Veg" },
            { icon: "🥛", name: "Chhaas (Buttermilk)", desc: "Gut Probiotics" }
        ]
    },
    rajasthan: {
        badge: "Rajasthani Thali",
        title: "Hearty Rajasthani Thali",
        items: [
            { icon: "🫓", name: "Bajra Rotla & Bati", desc: "Warming Energy" },
            { icon: "🥣", name: "Panchmel Dal", desc: "5-Pulse Protein" },
            { icon: "🫘", name: "Ker Sangri", desc: "Desert Minerals" },
            { icon: "🧈", name: "Fresh Cow Ghee", desc: "Vitamin Carrier" }
        ]
    },
    south: {
        badge: "Southern Thali",
        title: "Traditional South Indian Thali",
        items: [
            { icon: "🍚", name: "Steamed Rice", desc: "Clean Starch" },
            { icon: "🍲", name: "Drumstick Sambar", desc: "Protein & Fiber" },
            { icon: "🥣", name: "Pepper Rasam", desc: "Digestive Spices" },
            { icon: "🥥", name: "Beans Poriyal", desc: "Protective Veg" }
        ]
    },
    bengal: {
        badge: "Eastern Thali",
        title: "Nutritious Eastern Thali",
        items: [
            { icon: "🍚", name: "Aush Rice", desc: "Complex Energy" },
            { icon: "🥬", name: "Palong Saag", desc: "Iron & Folate" },
            { icon: "🫘", name: "Moong Dal & Bori", desc: "Light Protein" },
            { icon: "🍮", name: "Chhena / Mishti Doi", desc: "Dairy Calcium" }
        ]
    }
};

function buildThali(reg) {
    const data = thaliData[reg] || thaliData.gujarat;
    const badge = document.getElementById('sim11-badge');
    const title = document.getElementById('sim11-title');
    const itemsEl = document.getElementById('sim11-items');

    if (badge) badge.textContent = data.badge;
    if (title) title.textContent = data.title;
    if (itemsEl) {
        let html = '';
        data.items.forEach(it => {
            html += `
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center">
                    <div class="text-lg">${it.icon}</div>
                    <div class="font-bold text-slate-200">${it.name}</div>
                    <div class="text-[10px] text-slate-400">${it.desc}</div>
                </div>
            `;
        });
        itemsEl.innerHTML = html;
    }
}

// Sim 12: Physiological Hydration Chamber
function hydrateBody() {
    const level = document.getElementById('sim12-level');
    const status = document.getElementById('sim12-status');
    const temp = document.getElementById('sim12-temp');
    const kidney = document.getElementById('sim12-kidney');

    if (level) level.textContent = "72% (Peak Hydration)";
    if (status) { status.textContent = "💧 Flushed & Revitalized!"; status.className = "text-cyan-400 font-bold"; }
    if (temp) temp.textContent = "Perspiration cooling skin smoothly";
    if (kidney) kidney.textContent = "Kidneys filtering urea smoothly into clear urine";

    setTimeout(() => {
        if (level) level.textContent = "70% (Optimal Hydration)";
        if (status) { status.textContent = "✨ Alert & Energetic"; status.className = "text-emerald-400 font-semibold"; }
    }, 2800);
}

// Sim 13: Cooking Method & Nutrient Preservation Lab
const cookingDetails = {
    steaming: {
        badge: "Steaming (Best)",
        name: "Steaming (Idli / Dhokla)",
        retention: "Vitamin Retention: 95%",
        width: "95%",
        color: "bg-emerald-400",
        desc: "Gentle steam vapor softens tough cellulose without leaching water-soluble vitamins into discard water."
    },
    boiling: {
        badge: "Boiling (Good with Broth)",
        name: "Boiling (Dal & Soups)",
        retention: "Vitamin Retention: 75% (Keep Broth)",
        width: "75%",
        color: "bg-cyan-400",
        desc: "Softens pulses and tubers; using the nutrient-rich cooking broth retains minerals and vitamins."
    },
    roasting: {
        badge: "Roasting (Aromatic)",
        name: "Roasting (Roti / Corn)",
        retention: "Vitamin Retention: 80%",
        width: "80%",
        color: "bg-amber-400",
        desc: "Cooks evenly with minimal fat; caramelizes natural grain starches for easy digestion."
    },
    frying: {
        badge: "Deep Frying (Unhealthy)",
        name: "Deep Frying (Chips / Puri)",
        retention: "Vitamin Retention: 35% (Degraded)",
        width: "35%",
        color: "bg-rose-500",
        desc: "Extreme oil temperatures degrade sensitive vitamins, create trans fats, and make food heavy."
    }
};

function testCookingMethod(m) {
    const data = cookingDetails[m] || cookingDetails.steaming;
    const badge = document.getElementById('sim13-badge');
    const name = document.getElementById('sim13-method-name');
    const ret = document.getElementById('sim13-retention');
    const bar = document.getElementById('sim13-bar');
    const desc = document.getElementById('sim13-desc');

    if (badge) badge.textContent = data.badge;
    if (name) name.textContent = data.name;
    if (ret) ret.textContent = data.retention;
    if (bar) { bar.style.width = data.width; bar.className = `h-2.5 rounded-full transition-all duration-300 ${data.color}`; }
    if (desc) desc.textContent = data.desc;
}

// Sim 14: Solar Thermal Box Cooker Harness
function boostSunlight() {
    const temp = document.getElementById('sim14-temp');
    if (temp) {
        temp.textContent = "135°C (Simmering Yellow Dal & Rice)";
        temp.className = "text-emerald-400 font-bold animate-pulse";
    }
    setTimeout(() => {
        if (temp) {
            temp.textContent = "115°C (Cooking Active)";
            temp.className = "text-amber-400 font-bold";
        }
    }, 2800);
}

// Sim 15: Packaged Food Label Detective
const labelDetails = {
    expiry: {
        title: "📅 Expiry / Best Before Date Check",
        indicator: "Mfg: 10/2026 | Exp: 04/2027",
        info: "Always check before purchase! Consuming food past its expiry date risks severe bacterial contamination and food poisoning."
    },
    ingredients: {
        title: "📜 Ingredient Order by Weight",
        indicator: "1st: Whole Rolled Oats (65%)",
        info: "Ingredients appear in descending order by weight. If sugar or palm oil appears at the top, avoid regular consumption."
    },
    vegdot: {
        title: "🟢 Mandatory Dietary Symbol",
        indicator: "Green Circle = 100% Vegetarian",
        info: "Mandated by FSSAI: Green circle inside square indicates vegetarian; brown circle indicates non-vegetarian ingredients."
    },
    nutrition: {
        title: "📊 Nutrition Facts Panel",
        indicator: "Dietary Fiber: 8g | Added Sugar: 0g",
        info: "Scrutinize grams of added sugars, saturated fats, and sodium per serving to spot disguised junk snacks."
    }
};

function inspectLabel(zone) {
    const data = labelDetails[zone] || labelDetails.expiry;
    const title = document.getElementById('sim15-title');
    const ind = document.getElementById('sim15-indicator');
    const info = document.getElementById('sim15-info');

    if (title) title.textContent = data.title;
    if (ind) ind.textContent = data.indicator;
    if (info) info.textContent = data.info;
}

// Sim 16: School Food Festival Stall Planner
function updateSim16Score() {
    let score = 0;
    if (document.getElementById('sim16-chk-wash')?.checked) score += 25;
    if (document.getElementById('sim16-chk-cover')?.checked) score += 25;
    if (document.getElementById('sim16-chk-millet')?.checked) score += 25;
    if (document.getElementById('sim16-chk-eco')?.checked) score += 25;

    const scoreEl = document.getElementById('sim16-score');
    const statusEl = document.getElementById('sim16-status');
    const badgeEl = document.getElementById('sim16-badge');

    if (scoreEl) scoreEl.textContent = `Score: ${score} / 100`;

    if (score === 100) {
        if (statusEl) statusEl.textContent = "🌟 Festival Ready! Exceptional hygiene, diverse nutrition, and zero plastic waste.";
        if (badgeEl) { badgeEl.textContent = "Grand Opening Approved"; badgeEl.className = "px-2.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold"; }
    } else if (score >= 50) {
        if (statusEl) statusEl.textContent = "Good progress! Finish checking hygiene and compostable leaf plate requirements.";
        if (badgeEl) { badgeEl.textContent = "In Progress"; badgeEl.className = "px-2.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold"; }
    } else {
        if (statusEl) statusEl.textContent = "Complete all checklist items to open the school festival!";
        if (badgeEl) { badgeEl.textContent = "Planning Stage"; badgeEl.className = "px-2.5 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700 font-bold"; }
    }
}
"""

# Write to JS file
js_file = os.path.join(os.path.dirname(__file__), "class4_science_ch5_js.js")
with open(js_file, "w", encoding="utf-8") as f:
    f.write(js_code)

# Write to Python wrapper
py_file = os.path.join(os.path.dirname(__file__), "class4_science_ch5_js.py")
with open(py_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Science Chapter 5 JavaScript Engine Python Wrapper"""\n\n')
    f.write(f"JS_ENGINE = {repr(js_code)}\n")

print(f"Generated {js_file} and {py_file} successfully!")


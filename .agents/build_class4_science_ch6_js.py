# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 6: Happy and Healthy Living JavaScript Engine Builder
Generates .agents/class4_science_ch6_js.js and .agents/class4_science_ch6_js.py
"""

import os

js_code = """// Class 4 Science Chapter 6: Happy and Healthy Living - Pure Indian Male Teacher Audio Engine
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
        stored = localStorage.getItem('study_lab_voice_happy_ch6');
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
        localStorage.setItem('study_lab_voice_happy_ch6', userPreferredVoice);
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

// =================== SLIDE NAVIGATION & INVARIANTS ===================
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

// =================== AUDIO LECTURE PLAYBACK ===================
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
        startSpeechKeepAlive();
        const btn = document.getElementById('audioLectureBtn');
        if (btn) {
            btn.innerHTML = `
                <svg class="w-4 h-4 animate-spin text-amber-300" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg>
                <span class="text-xs font-bold text-amber-300">Teacher Speaking...</span>
            `;
            btn.classList.remove('bg-teal-600', 'hover:bg-teal-500');
            btn.classList.add('bg-amber-600', 'hover:bg-amber-500');
        }
    };

    currentUtterance.onend = () => {
        stopAudioLecture();
    };

    currentUtterance.onerror = (e) => {
        console.error("Speech synthesis error:", e);
        stopAudioLecture();
    };

    window.speechSynthesis.speak(currentUtterance);
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    stopSpeechKeepAlive();
    const btn = document.getElementById('audioLectureBtn');
    if (btn) {
        btn.innerHTML = `
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            <span class="text-xs font-bold">Teacher Sound Lecture</span>
        `;
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500');
        btn.classList.add('bg-teal-600', 'hover:bg-teal-500');
    }
}

// Keep-alive timer for Chrome SpeechSynthesis bug (stops at ~15s)
function startSpeechKeepAlive() {
    stopSpeechKeepAlive();
    keepAliveTimer = setInterval(() => {
        if (!window.speechSynthesis) return;
        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        }
    }, 12000);
}

function stopSpeechKeepAlive() {
    if (keepAliveTimer) {
        clearInterval(keepAliveTimer);
        keepAliveTimer = null;
    }
}

// =================== INTERACTIVE CHECKPOINTS ===================
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
            b.classList.remove('hover:border-teal-500', 'hover:bg-slate-800');
        });
    }

    const fb = document.getElementById(`fb-${slideId}-${cpIdx}`);

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-teal-600', 'text-white', 'border-teal-500', 'font-bold');
        playTeacherSound(true);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-teal-950/80 border border-teal-800 text-xs text-teal-300">
                    <span class="font-bold">✓ Splendid scientific reasoning!</span> ${cp.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-900/60', 'text-rose-200', 'border-rose-700');
        playTeacherSound(false);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    <span class="text-rose-400 font-bold">Incorrect.</span> <strong>Correct answer:</strong> <span class="text-teal-400 font-semibold">${cp.ans}</span>. ${cp.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    }
}

// =================== CHALLENGE QUESTIONS (17-20) ===================
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
            b.classList.remove('hover:border-teal-500', 'hover:bg-slate-800');
        });
    }

    const fb = document.getElementById(`quiz-fb-${qId}`);

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-teal-600', 'text-white', 'border-teal-500', 'font-bold');
        playTeacherSound(true);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-teal-950/80 border border-teal-800 text-xs text-teal-300">
                    <span class="font-bold">✓ Outstanding answer!</span> ${question.explanation}
                </div>
            `;
            fb.classList.remove('hidden');
        }
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-900/60', 'text-rose-200', 'border-rose-700');
        playTeacherSound(false);
        if (fb) {
            fb.innerHTML = `
                <div class="mt-2.5 p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                    <span class="text-rose-400 font-bold">Incorrect.</span> <strong>Correct:</strong> <span class="text-teal-400 font-semibold">${question.ans}</span>. ${question.explanation}
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
                <span class="font-bold text-teal-400 block mb-1">Step 2: Analyzing Biological Context</span>
                <p>${question.solution_steps.step2}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="font-bold text-cyan-400 block mb-1">Step 3: Conclusive Nutritional Deduction</span>
                <p>${question.solution_steps.step3}</p>
            </div>
            <div class="p-3 rounded-xl bg-teal-950/40 border border-teal-800/40 text-teal-300">
                <strong>Correct Conclusion:</strong> ${question.ans}
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}

function closeModalSolution() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

// =================== BESPOKE SIMULATOR INTERACTIVE SCRIPTS (1-16) ===================

// Sim 1: Farm-to-Plate Grain Conveyor
const farmStages = [
    {
        icon: "🚜",
        num: "Stage 1 of 6",
        name: "Soil Preparation & Aeration",
        desc: "Farmers till and loosen the earth with ploughs. This loosens dense soil clods, allows air and moisture to circulate freely, and prepares a fertile seedbed for planting.",
        meta: "Tools: Tractor & Steel Plough",
        fact: "Scientific Goal: Increases soil pore volume for root oxygenation",
        pct: "16.6%"
    },
    {
        icon: "🌱",
        num: "Stage 2 of 6",
        name: "Sowing & Natural Nourishment",
        desc: "High-quality certified seeds are sown at optimal depth. Sun, water, fertile soil, and earthworms provide the foundational nourishment for seedlings to germinate and grow.",
        meta: "Nature: Sunlight, Water & Earthworms",
        fact: "Germination: Seed absorbs moisture and sprouts root radicle",
        pct: "33.3%"
    },
    {
        icon: "🌾",
        num: "Stage 3 of 6",
        name: "Crop Ripening & Harvesting",
        desc: "Over three to four months, golden stalks of wheat mature under the sun. Farmers harvest the ripe crop using sickles and combine harvesters.",
        meta: "Season: Rabi Crop Harvest (March-April)",
        fact: "Threshing: Edible grains are separated from dry stalk husks",
        pct: "50.0%"
    },
    {
        icon: "🏬",
        num: "Stage 4 of 6",
        name: "Sun-Drying & Granary Storage",
        desc: "Grains are sun-dried on wide courtyards to eliminate moisture that invites fungal mold. Dried neem leaves are added to jute bags to repel insects naturally.",
        meta: "Preservation: Dry Neem Leaves & Jute Bags",
        fact: "Moisture Control: Below 12% moisture prevents fungal rot",
        pct: "66.6%"
    },
    {
        icon: "🚚",
        num: "Stage 5 of 6",
        name: "Transport Logistics & Wholesale Mandis",
        desc: "Truck drivers and freight trains transport tons of grain sacks across hundreds of kilometers from rural farms to city wholesale mandis and neighborhood grocery shops.",
        meta: "Logistics: Supply Chain Contributors",
        fact: "Distribution: Connects rural harvest to urban kitchens",
        pct: "83.3%"
    },
    {
        icon: "🫓",
        num: "Stage 6 of 6",
        name: "Kitchen Transformation & Plate Gratitude",
        desc: "Grains are milled into flour, kneaded into dough with water, and roasted into soft chapatis. The family enjoys nutritious meals with deep appreciation for all contributors.",
        meta: "Meal: Warm Homemade Chapatis",
        fact: "Final Reward: Carbohydrates, fiber, and energy for growing bodies",
        pct: "100%"
    }
];
let currentFarmStage = 0;

function selectFarmStage(idx) {
    currentFarmStage = idx;
    updateFarmDisplay();
}

function nextFarmStage() {
    currentFarmStage = (currentFarmStage + 1) % farmStages.length;
    updateFarmDisplay();
}

function prevFarmStage() {
    currentFarmStage = (currentFarmStage - 1 + farmStages.length) % farmStages.length;
    updateFarmDisplay();
}

function updateFarmDisplay() {
    const s = farmStages[currentFarmStage];
    const iconEl = document.getElementById('farmStageIcon');
    const numEl = document.getElementById('farmStageNumber');
    const nameEl = document.getElementById('farmStageName');
    const descEl = document.getElementById('farmStageDesc');
    const metaEl = document.getElementById('farmStageMeta');
    const factEl = document.getElementById('farmStageFact');
    const barEl = document.getElementById('farmProgressBar');

    if (iconEl) iconEl.textContent = s.icon;
    if (numEl) numEl.textContent = s.num;
    if (nameEl) nameEl.textContent = s.name;
    if (descEl) descEl.textContent = s.desc;
    if (metaEl) metaEl.textContent = s.meta;
    if (factEl) factEl.textContent = s.fact;
    if (barEl) barEl.style.width = s.pct;

    const btns = document.querySelectorAll('.farm-stage-btn');
    btns.forEach((btn, idx) => {
        btn.classList.toggle('active', idx === currentFarmStage);
        btn.classList.toggle('border-emerald-500/50', idx === currentFarmStage);
        btn.classList.toggle('bg-emerald-950/40', idx === currentFarmStage);
    });
}

// Sim 2: Food Ecosystem Contributor Network
const contribData = {
    sun: {
        icon: "☀️",
        title: "Solar Energy & Radiance",
        role: "Primary Natural Contributor (Abiotic Power)",
        desc: "Sunlight provides radiant photons captured by chlorophyll in green leaves to drive photosynthesis, synthesizing all food carbohydrates.",
        impact: "Fuels 100% of global plant biomass",
        grat: "Honored during Makar Sankranti & Chhath Puja"
    },
    earthworm: {
        icon: "🪱",
        title: "Soil Aerator & Vermicomposter",
        role: "Vital Underground Animal Contributor",
        desc: "Earthworms swallow organic litter and soil, boring deep tunnels that aerate roots and excreting vermicompost castings loaded with nitrogen and phosphorus.",
        impact: "Increases root water infiltration by 500%",
        grat: "Celebrated as the farmer's supreme biological helper"
    },
    farmer: {
        icon: "👨‍🌾",
        title: "Crop Cultivator & Caregiver",
        role: "Primary Human Agricultural Contributor",
        desc: "Farmers wake at dawn to plough, sow, weed, irrigate, protect, and harvest grains through extreme summer heat and winter cold.",
        impact: "Produces food sustenance for over 8 billion people",
        grat: "Honored in every regional harvest festival across the nation"
    },
    transporter: {
        icon: "🚛",
        title: "Logistics & Freight Drivers",
        role: "Vital Supply Chain Bridge",
        desc: "Truckers and freight workers drive through night highways, navigating fog, monsoon floods, and rough terrain to deliver food sacks to city hubs.",
        impact: "Transports over 300 million tons of grains annually",
        grat: "Keeps grocery shelves stocked in every town"
    },
    shopkeeper: {
        icon: "🏪",
        title: "Neighborhood Grocery Shopkeeper",
        role: "Community Distribution Link",
        desc: "Maintains dry, clean, pest-free stores, measures portions accurately, and ensures local households receive daily flour, rice, and pulses safely.",
        impact: "Essential daily food distribution to homes",
        grat: "Provides friendly, reliable neighborhood access to food"
    },
    cook: {
        icon: "👩‍🍳",
        title: "Home Cook & Family Caregiver",
        role: "Nourishment Specialist",
        desc: "Skillfully transforms raw flour and pulses into hot, wholesome, hygienically prepared meals that fuel family members with love and balanced nutrition.",
        impact: "Turns raw agriculture into digestible, warm meals",
        grat: "Deserves thanks after every single lunch and dinner"
    },
    rain: {
        icon: "🌧️",
        title: "Monsoon Rains & Groundwater",
        role: "Vital Life-Giving Hydration",
        desc: "Rainclouds deliver pure freshwater that fills rivers, lakes, and soil water tables, supplying the universal solvent needed for cellular crop growth.",
        impact: "Irrigates over 60% of Indian farmland naturally",
        grat: "Celebrated in Raja Utsav and Teej festivals"
    },
    soil: {
        icon: "🌱",
        title: "Mother Soil & Mineral Bed",
        role: "The Living Terrestrial Foundation",
        desc: "A single teaspoon of healthy soil holds billions of microorganisms, fungi, and rich minerals that anchor plant roots and feed plant nutrition.",
        impact: "Living substrate for all land-based life",
        grat: "Treated with reverent care and organic compost"
    }
};

function selectContributor(type) {
    const data = contribData[type] || contribData.sun;
    const iconEl = document.getElementById('contribIcon');
    const titleEl = document.getElementById('contribTitle');
    const roleEl = document.getElementById('contribRole');
    const descEl = document.getElementById('contribDesc');
    const impactEl = document.getElementById('contribImpact');
    const gratEl = document.getElementById('contribGratitude');

    if (iconEl) iconEl.textContent = data.icon;
    if (titleEl) titleEl.textContent = data.title;
    if (roleEl) roleEl.textContent = data.role;
    if (descEl) descEl.textContent = data.desc;
    if (impactEl) impactEl.textContent = `Impact: ${data.impact}`;
    if (gratEl) gratEl.textContent = `Gratitude: ${data.grat}`;

    const btns = document.querySelectorAll('.contrib-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-amber-500/50', 'bg-amber-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-amber-500/50', 'bg-amber-950/40');
    }
}

// Sim 3: Gratitude Letter Workshop
let selectedRecipient = 'Hardworking Farmer';
let selectedIcon = '🌾';

function setGratitudeRecipient(name, icon) {
    selectedRecipient = name;
    selectedIcon = icon;
    updateGratitudeLetter();

    const btns = document.querySelectorAll('.grat-recip-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'bg-rose-950/40', 'border-rose-500/50');
        b.classList.add('bg-slate-800/60', 'border-slate-700');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'bg-rose-950/40', 'border-rose-500/50');
        window.event.currentTarget.classList.remove('bg-slate-800/60', 'border-slate-700');
    }
}

function updateGratitudeLetter() {
    const toEl = document.getElementById('letterTo');
    const iconEl = document.getElementById('cardIcon');
    const bodyEl = document.getElementById('letterBody');
    const select = document.getElementById('gratitudeSentiment');

    if (toEl) toEl.textContent = `Dearest ${selectedRecipient},`;
    if (iconEl) iconEl.textContent = selectedIcon;

    if (bodyEl && select) {
        const text = select.options[select.selectedIndex].text;
        bodyEl.textContent = `"${text} Every grain on our plate represents your unwavering dedication."`;
    }
}

function dispatchGratitude() {
    const stamp = document.getElementById('stampStatus');
    if (stamp) {
        stamp.textContent = '✓ SEALED & DELIVERED';
        stamp.className = 'font-bold text-emerald-700 uppercase tracking-widest bg-emerald-100 px-2.5 py-0.5 rounded border border-emerald-400';
    }
    playTeacherSound(true);
}

// Sim 4: Pan-Indian Harvest Festival Explorer
const festData = {
    sankranti: {
        icon: "🪁",
        name: "Makar Sankranti",
        region: "Pan-India (January 14/15)",
        significance: "Celebrates the sun entering Makara (Capricorn) and honors the first winter harvest of sesame, jaggery, sugarcane, and fresh rice.",
        foods: "Til-gur laddus, khichdi, rewri, sugarcane chunks, fresh roasted peanut chikki.",
        ritual: "Flying colorful kites to absorb healthy winter vitamin D from the sun and singing thanksgiving folk tunes.",
        eco: "Honoring solar energy that nurtured the crops through winter months.",
        tag: "Key Value: Community sharing of newly harvested grains"
    },
    onam: {
        icon: "🛶",
        name: "Onam Harvest Festival",
        region: "Kerala (August-September)",
        significance: "Celebrates the annual return of legendary King Mahabali and the bountiful harvest of paddy and tropical fruits.",
        foods: "Grand 26-dish Onasadya served traditionally on fresh banana leaves, payasam, avial.",
        ritual: "Snake boat races (Vallam Kali), Pookkalam flower carpets, and traditional Pulikali tiger dances.",
        eco: "Commemorates soil fertility and freshwater backwater abundance.",
        tag: "Key Value: Unity, equality, and celebration on plant leaves"
    },
    lohri: {
        icon: "🔥",
        name: "Lohri Bonfire Thanksgiving",
        region: "Punjab & Northern India (January 13)",
        significance: "Marks the culmination of winter and the harvest of the Rabi sugarcane and wheat crops.",
        foods: "Makki di roti, sarson da saag, gur, rewri, gajak, and puffed corn.",
        ritual: "Gathering around a sacred bonfire, offering harvested grains to the flames, and dancing Bhangra.",
        eco: "Celebrating the warmth of fire that sustained communities through winter.",
        tag: "Key Value: Gratitude to fire and agricultural abundance"
    },
    raja: {
        icon: "🪘",
        name: "Raja Utsav (Rajo)",
        region: "Odisha (Mid-June)",
        significance: "A unique 3-day festival celebrating Mother Earth's fertility right before the arrival of the life-giving monsoon rains.",
        foods: "Poda Pitha (slow-baked rice and coconut cake), sweet Raja paan, chakuli pitha.",
        ritual: "Farming activity halts completely to let the earth rest; girls play on decorated rope swings.",
        eco: "Giving Mother Earth three days of rest before monsoon ploughing.",
        tag: "Key Value: Reverence for soil renewal and female fertility"
    },
    akshaya: {
        icon: "🪙",
        name: "Akshay Tritya",
        region: "National Celebration (April-May)",
        significance: "Celebrates eternal prosperity, agricultural abundance, and the auspicious commencement of new ploughing seasons.",
        foods: "Sweet sattu porridge, mango shrikhand, barley porridge, seasonal cooling sherbets.",
        ritual: "Farmers offer prayers to their ploughs and cattle, distributing grains to the needy.",
        eco: "Recognizing that true wealth originates from fertile agricultural earth.",
        tag: "Key Value: Eternal renewal and charitable food sharing"
    },
    bihu: {
        icon: "🥁",
        name: "Magh Bihu (Bhogali Bihu)",
        region: "Assam & Northeast (Mid-January)",
        significance: "The grand harvest festival of Assam marking the completion of the winter paddy harvesting season.",
        foods: "Pitha rice cakes, laru sesame sweets, chira with fresh curd and jaggery.",
        ritual: "Building temporary straw pavilions called Meji and feasting inside them before burning them in thanksgiving.",
        eco: "Gratitude to the Brahmaputra river valley for nourishing paddy fields.",
        tag: "Key Value: Feasting and communal harmony after hard harvest labor"
    }
};

function selectFestival(festId) {
    const data = festData[festId] || festData.sankranti;
    const iconEl = document.getElementById('festIcon');
    const nameEl = document.getElementById('festName');
    const regEl = document.getElementById('festRegion');
    const sigEl = document.getElementById('festSignificance');
    const foodEl = document.getElementById('festFoods');
    const ritEl = document.getElementById('festRitual');
    const ecoEl = document.getElementById('festEcoLesson');
    const tagEl = document.getElementById('festTag');

    if (iconEl) iconEl.textContent = data.icon;
    if (nameEl) nameEl.textContent = data.name;
    if (regEl) regEl.textContent = data.region;
    if (sigEl) sigEl.textContent = data.significance;
    if (foodEl) foodEl.textContent = data.foods;
    if (ritEl) ritEl.textContent = data.ritual;
    if (ecoEl) ecoEl.textContent = data.eco;
    if (tagEl) tagEl.textContent = data.tag;

    const btns = document.querySelectorAll('.fest-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-cyan-500/50', 'bg-cyan-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-cyan-500/50', 'bg-cyan-950/40');
    }
}

// Sim 5: Peanut Sensory Awareness Chamber
const senseData = {
    touch: {
        visual: "🥜",
        badge: "Sense 1: Tactile Touch",
        title: "Feel the Ridged Shell & Smooth Seed",
        detail: "Roll the peanut gently between your fingertips. Notice the hard fibrous outer pod with its rough textured ridges, followed by the silky smooth red skin protecting the twin seed halves inside.",
        receptor: "Mechanoreceptors in fingertip skin",
        mindfulness: "Physical touch grounds focus in the present moment"
    },
    sight: {
        visual: "🔍",
        badge: "Sense 2: Visual Sight",
        title: "Observe Warm Golden Hues & Symmetry",
        detail: "Look closely at the peanut under clear light. Observe the delicate web-like lattice ridges, the natural earth-brown tint, and the twin symmetry of the inner cotyledons.",
        receptor: "Retinal photoreceptors (rods & cones)",
        mindfulness: "Visual appreciation stimulates anticipatory digestive saliva"
    },
    smell: {
        visual: "👃",
        badge: "Sense 3: Olfactory Aroma",
        title: "Inhale the Earthy, Roasted Fragrance",
        detail: "Bring the peanut close to your nostrils and inhale deeply. Notice the rich nutty, warm aroma released by natural plant lipids and proteins.",
        receptor: "Olfactory sensory neurons in nasal cavity",
        mindfulness: "Smell triggers the vagus nerve to awaken stomach gastric juices"
    },
    sound: {
        visual: "🔊",
        badge: "Sense 4: Auditory Sound",
        title: "Listen to the Crisp Snap and Crunch",
        detail: "Crack open the pod near your ear. Listen to the dry snap of the shell, the gentle rattle of loose kernels, and the crisp crunch when your teeth make the first bite.",
        receptor: "Cochlear hair cells in inner ear",
        mindfulness: "Auditory awareness slows down meal pacing naturally"
    },
    taste: {
        visual: "👅",
        badge: "Sense 5: Gustatory Taste",
        title: "Savor the Creamy, Rich, Nutty Flavor",
        detail: "Chew slowly without swallowing. Notice how the dry crunchy kernel blends with saliva, releasing savory, rich oils and a mild natural sweetness.",
        receptor: "Taste receptor buds on lingual papillae",
        mindfulness: "Savoring flavor signals satisfaction before overeating occurs"
    }
};

function inspectSense(sense) {
    const data = senseData[sense] || senseData.touch;
    const visEl = document.getElementById('senseVisual');
    const badgeEl = document.getElementById('senseBadge');
    const titleEl = document.getElementById('senseTitle');
    const detEl = document.getElementById('senseDetail');
    const recEl = document.getElementById('senseReceptor');
    const mindEl = document.getElementById('senseMindfulness');

    if (visEl) visEl.textContent = data.visual;
    if (badgeEl) badgeEl.textContent = data.badge;
    if (titleEl) titleEl.textContent = data.title;
    if (detEl) detEl.textContent = data.detail;
    if (recEl) recEl.textContent = `Receptor: ${data.receptor}`;
    if (mindEl) mindEl.textContent = `Mindful Insight: ${data.mindfulness}`;

    const btns = document.querySelectorAll('.sense-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-yellow-500/50', 'bg-yellow-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-yellow-500/50', 'bg-yellow-950/40');
    }
}

// Sim 6: Salivary Mastication Engine
function updateChewSim(val) {
    const countEl = document.getElementById('chewCountVal');
    const texEl = document.getElementById('chewTexture');
    const texDescEl = document.getElementById('chewTextureDesc');
    const sugEl = document.getElementById('chewSugarStatus');
    const sugDescEl = document.getElementById('chewSugarDesc');
    const easeEl = document.getElementById('chewEaseStatus');
    const easeDescEl = document.getElementById('chewEaseDesc');

    if (countEl) countEl.textContent = `${val} Chews`;

    if (val < 15) {
        if (texEl) texEl.innerHTML = '<span>🥖</span> Coarse Grain Chunks';
        if (texDescEl) texDescEl.textContent = 'Food particles remain large, requiring high stomach acid workload.';
        if (sugEl) sugEl.innerHTML = '<span>🧪</span> Partial Hydrolysis';
        if (sugDescEl) sugDescEl.textContent = 'Very little starch broken down; no sweetness felt yet.';
        if (easeEl) easeEl.innerHTML = '<span>⚠️</span> High Stomach Strain';
        if (easeDescEl) easeDescEl.textContent = 'Stomach must churn excessively, risking acid reflux.';
    } else if (val < 28) {
        if (texEl) texEl.innerHTML = '<span>🥣</span> Moist Crumbled Bolus';
        if (texDescEl) texDescEl.textContent = 'Saliva lubricates bolus; particles reduced to medium size.';
        if (sugEl) sugEl.innerHTML = '<span>🍯</span> Maltose Emerging';
        if (sugDescEl) sugDescEl.textContent = 'Salivary amylase breaks starch bonds; noticeable sweet hint.';
        if (easeEl) easeEl.innerHTML = '<span>✅</span> Moderate Ease';
        if (easeDescEl) easeDescEl.textContent = 'Gastric juices penetrate surface area smoothly.';
    } else {
        if (texEl) texEl.innerHTML = '<span>🥛</span> Smooth Liquid Bolus';
        if (texDescEl) texDescEl.textContent = 'Pulverized into microscopic emulsion ready for effortless swallowing.';
        if (sugEl) sugEl.innerHTML = '<span>✨</span> Full Starch Breakdown';
        if (sugDescEl) sugDescEl.textContent = 'Extensive amylase enzymatic action creates rich sweet flavor!';
        if (easeEl) easeEl.innerHTML = '<span>🌟</span> Perfect Digestion Ease';
        if (easeDescEl) easeDescEl.textContent = 'Zero stomach strain; maximum immediate nutrient absorption.';
    }
}

function setChewsTo32() {
    const slider = document.getElementById('chewSlider');
    if (slider) {
        slider.value = 32;
        updateChewSim(32);
    }
}

// Sim 7: Food Waste & Resource Impact Calculator
function updateWasteSim(val) {
    const qEl = document.getElementById('wasteQuantityVal');
    const wEl = document.getElementById('lostWaterVal');
    const dEl = document.getElementById('lostDieselVal');
    const lEl = document.getElementById('lostLaborVal');

    const water = val * 150;
    const diesel = val * 60;
    const labor = val * 22;

    if (qEl) qEl.textContent = `${val} Chapatis / ${Math.round(val * 0.5)} Bowls Rice`;
    if (wEl) wEl.textContent = `${water} Litres`;
    if (dEl) dEl.textContent = `${diesel} Millilitres`;
    if (lEl) lEl.textContent = `${labor} Minutes`;
}

function zeroWasteCommitment() {
    alert("🌟 Congratulations! You have committed to the Zero-Waste Clean Plate Pledge. Serve only what you can eat, and take second helpings only when hungry!");
    playTeacherSound(true);
}

// Sim 8: Mindful Meal Pacing Log & Weekly Diary
const diaryRecords = {
    Mon: { chew: "28 Chews / bite", colors: "4 Natural Colors", clean: "100% Clean Plate", grat: "Deeply Grateful", score: "94% Excellent" },
    Tue: { chew: "30 Chews / bite", colors: "5 Rainbow Foods", clean: "100% Clean Plate", grat: "Mindful Pause Taken", score: "96% Superior" },
    Wed: { chew: "25 Chews / bite", colors: "3 Natural Colors", clean: "95% Clean Plate", grat: "Expressed Thanks", score: "88% Good" },
    Thu: { chew: "32 Chews / bite", colors: "5 Rainbow Foods", clean: "100% Clean Plate", grat: "Deeply Grateful", score: "98% Outstanding" },
    Fri: { chew: "27 Chews / bite", colors: "4 Natural Colors", clean: "100% Clean Plate", grat: "Mindful Pause Taken", score: "92% Excellent" },
    Sat: { chew: "31 Chews / bite", colors: "4 Natural Colors", clean: "100% Clean Plate", grat: "Grateful to Family Cook", score: "95% Superior" },
    Sun: { chew: "32 Chews / bite", colors: "6 Festive Colors", clean: "100% Clean Plate", grat: "Harvest Gratitude Shared", score: "99% Masterful" }
};

function selectDiaryDay(day) {
    const data = diaryRecords[day] || diaryRecords.Mon;
    const chewEl = document.getElementById('diaryChew');
    const colEl = document.getElementById('diaryColors');
    const cleanEl = document.getElementById('diaryClean');
    const gratEl = document.getElementById('diaryGrat');
    const scoreEl = document.getElementById('diaryScore');

    if (chewEl) chewEl.innerHTML = `<span>⏱️</span> ${data.chew}`;
    if (colEl) colEl.innerHTML = `<span>🥗</span> ${data.colors}`;
    if (cleanEl) cleanEl.innerHTML = `<span>✨</span> ${data.clean}`;
    if (gratEl) gratEl.innerHTML = `<span>🙏</span> ${data.grat}`;
    if (scoreEl) scoreEl.textContent = data.score;

    const btns = document.querySelectorAll('.diary-day-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-indigo-500/50', 'bg-indigo-950/40', 'text-white');
        b.classList.add('border-slate-700', 'bg-slate-800/50', 'text-slate-300');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-indigo-500/50', 'bg-indigo-950/40', 'text-white');
        window.event.currentTarget.classList.remove('border-slate-700', 'bg-slate-800/50', 'text-slate-300');
    }
}

function logTodayMeal() {
    alert("📝 Today's meal logged successfully: 32 Chews / bite, 4 rainbow colors, zero waste, heartfelt gratitude!");
    playTeacherSound(true);
}

// Sim 9: Heart Rate & Stamina Meter
const activityData = {
    sitting: {
        bpm: "75 BPM",
        o2: "14 Breaths/min",
        endorphin: "Baseline 20%",
        heartDesc: "Calm steady resting rhythm",
        lungDesc: "Standard tidal volume",
        brainDesc: "Normal neural state"
    },
    walking: {
        bpm: "98 BPM",
        o2: "20 Breaths/min",
        endorphin: "Elevated 45%",
        heartDesc: "Moderate pumping, gentle dilation",
        lungDesc: "Expanded tidal ventilation",
        brainDesc: "Pleasant alertness and calm"
    },
    skipping: {
        bpm: "135 BPM",
        o2: "28 Breaths/min",
        endorphin: "High 75%",
        heartDesc: "Vigorous aerobic conditioning",
        lungDesc: "Deep lung capacity activation",
        brainDesc: "Dopamine & endorphin rush"
    },
    khokho: {
        bpm: "160 BPM",
        o2: "36 Breaths/min",
        endorphin: "Peak 95%",
        heartDesc: "Sprint maximum stamina training",
        lungDesc: "Peak VO2 oxygen utilization",
        brainDesc: "Euphoric runner's high & team joy"
    }
};

function selectActivity(act) {
    const data = activityData[act] || activityData.sitting;
    const bpmEl = document.getElementById('actBpm');
    const o2El = document.getElementById('actO2');
    const endEl = document.getElementById('actEndorphin');
    const hDesc = document.getElementById('actHeartDesc');
    const lDesc = document.getElementById('actLungDesc');
    const bDesc = document.getElementById('actBrainDesc');

    if (bpmEl) bpmEl.textContent = data.bpm;
    if (o2El) o2El.textContent = data.o2;
    if (endEl) endEl.textContent = data.endorphin;
    if (hDesc) hDesc.textContent = data.heartDesc;
    if (lDesc) lDesc.textContent = data.lungDesc;
    if (bDesc) bDesc.textContent = data.brainDesc;

    const btns = document.querySelectorAll('.activity-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-red-500/50', 'bg-red-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-red-500/50', 'bg-red-950/40');
    }
}

// Sim 10: Spinal Alignment & Yoga Posture Chamber
const asanaData = {
    vrikshasana: {
        icon: "🧘",
        badge: "Balance & Stability",
        name: "Vrikshasana (Tree Pose)",
        desc: "Stand firmly on one foot, place the opposite sole on inner thigh, and join palms overhead. Trains cerebellar balance, strengthens ankles, and promotes single-pointed mental concentration.",
        spine: "Spine Effect: Aligns 33 vertebrae vertically",
        correction: "Counteracts: Forward desk slouching and poor posture"
    },
    bhujangasana: {
        icon: "🐍",
        badge: "Spinal Flexibility",
        name: "Bhujangasana (Cobra Pose)",
        desc: "Lie prone and lift chest off the mat with palms beneath shoulders. Expands chest volume, stimulates adrenal glands, and stretches tight abdominal muscles.",
        spine: "Spine Effect: Decompresses lumbar discs with backward arc",
        correction: "Counteracts: Rounded shoulders and hunched upper back"
    },
    tadasana: {
        icon: "⛰️",
        badge: "Core Alignment",
        name: "Tadasana (Mountain Pose)",
        desc: "Stand tall with feet parallel, engage thigh muscles, lengthen neck, and reach arms upward. Establishes the anatomical blueprint of perfect upright posture.",
        spine: "Spine Effect: Natural S-curve spinal neutrality",
        correction: "Counteracts: Uneven hip and shoulder tilting"
    },
    balasana: {
        icon: "🌱",
        badge: "Rest & Decompression",
        name: "Balasana (Child's Pose)",
        desc: "Kneel and fold forward, resting forehead on the mat with arms relaxed forward. Gently lengthens the entire spine, calms the central nervous system, and relieves fatigue.",
        spine: "Spine Effect: Passive elongation of dorsal muscles",
        correction: "Counteracts: Stress tension and lower back tightness"
    }
};

function selectAsana(asana) {
    const data = asanaData[asana] || asanaData.vrikshasana;
    const iconEl = document.getElementById('asanaIcon');
    const badgeEl = document.getElementById('asanaBadge');
    const nameEl = document.getElementById('asanaName');
    const descEl = document.getElementById('asanaDesc');
    const spineEl = document.getElementById('asanaSpine');
    const corrEl = document.getElementById('asanaCorrection');

    if (iconEl) iconEl.textContent = data.icon;
    if (badgeEl) badgeEl.textContent = data.badge;
    if (nameEl) nameEl.textContent = data.name;
    if (descEl) descEl.textContent = data.desc;
    if (spineEl) spineEl.textContent = data.spine;
    if (corrEl) corrEl.textContent = data.correction;

    const btns = document.querySelectorAll('.asana-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-emerald-500/50', 'bg-emerald-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-emerald-500/50', 'bg-emerald-950/40');
    }
}

// Sim 11: Brain Glymphatic Cleansing Simulator
function setSleepState(state) {
    const flowEl = document.getElementById('glymphFlow');
    const flowDescEl = document.getElementById('glymphFlowDesc');
    const memEl = document.getElementById('glymphMemory');
    const memDescEl = document.getElementById('glymphMemoryDesc');
    const hormEl = document.getElementById('glymphHormone');
    const hormDescEl = document.getElementById('glymphHormoneDesc');

    if (state === 'sleep') {
        if (flowEl) flowEl.innerHTML = '<span>🌊</span> +60% Cerebrospinal Surge';
        if (flowDescEl) flowDescEl.textContent = 'Brain interstitial space expands, allowing fluid to flush out metabolic waste.';
        if (memEl) memEl.innerHTML = '<span>💾</span> Long-Term Consolidation';
        if (memDescEl) memDescEl.textContent = 'Hippocampus transfers school facts into stable cerebral cortex storage.';
        if (hormEl) hormEl.innerHTML = '<span>📈</span> Peak Secretion Active';
        if (hormDescEl) hormDescEl.textContent = 'Stimulates bone lengthening, cell regeneration, and muscle tissue repair.';
    } else {
        if (flowEl) flowEl.innerHTML = '<span>⏳</span> Constricted Waste Flow';
        if (flowDescEl) flowDescEl.textContent = 'Daytime brain cells are tightly packed; fluid wash operates at low baseline.';
        if (memEl) memEl.innerHTML = '<span>⚡</span> Active Encoding Mode';
        if (memDescEl) memDescEl.textContent = 'Taking in new sensory facts; memories are fragile and unorganized.';
        if (hormEl) hormEl.innerHTML = '<span>📉</span> Low Daytime Baseline';
        if (hormDescEl) hormDescEl.textContent = 'Growth hormone rests; energy diverted to muscle movement and study.';
    }

    const btns = document.querySelectorAll('.sleep-toggle-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-violet-500/50', 'bg-violet-950/40', 'text-white');
        b.classList.add('border-slate-700', 'bg-slate-800/50', 'text-slate-300');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-violet-500/50', 'bg-violet-950/40', 'text-white');
        window.event.currentTarget.classList.remove('border-slate-700', 'bg-slate-800/50', 'text-slate-300');
    }
}

// Sim 12: Circadian Melatonin Clock Cycle
let blueScreenOn = false;

function updateCircadianSim(hour) {
    const timeEl = document.getElementById('circadianTimeVal');
    const melEl = document.getElementById('circadianMelatonin');
    const melDescEl = document.getElementById('circadianMelatoninDesc');
    const tempEl = document.getElementById('circadianTemp');
    const tempDescEl = document.getElementById('circadianTempDesc');
    const alertEl = document.getElementById('circadianAlert');
    const alertDescEl = document.getElementById('circadianAlertDesc');

    let h = parseInt(hour, 10);
    let ampm = h >= 12 ? 'PM' : 'AM';
    let displayH = h % 12 === 0 ? 12 : h % 12;

    if (timeEl) timeEl.textContent = `${displayH}:00 ${ampm} (${getCircadianLabel(h)})`;

    if (h >= 21 || h <= 5) {
        // Night
        if (blueScreenOn) {
            if (melEl) melEl.innerHTML = '<span>⚠️</span> Suppressed (12 pg/mL)';
            if (melDescEl) melDescEl.textContent = 'Blue screen light tricks pineal gland into halting melatonin!';
            if (alertEl) alertEl.innerHTML = '<span>👀</span> Artificial Insomnia';
            if (alertDescEl) alertDescEl.textContent = 'Brain is falsely stimulated; sleep onset delayed by 1-2 hours.';
        } else {
            if (melEl) melEl.innerHTML = '<span>🧪</span> High (65-80 pg/mL)';
            if (melDescEl) melDescEl.textContent = 'Darkness stimulates peak melatonin; eyes feel heavy.';
            if (alertEl) alertEl.innerHTML = '<span>😴</span> Deep Restorative Sleep';
            if (alertDescEl) alertDescEl.textContent = 'Delta brainwaves dominate; cells regenerate rapidly.';
        }
        if (tempEl) tempEl.innerHTML = '<span>🌡️</span> 36.2°C (Cooled Core)';
        if (tempDescEl) tempDescEl.textContent = 'Basal temperature drops to conserve cellular energy.';
    } else {
        // Day
        if (melEl) melEl.innerHTML = '<span>☀️</span> Minimal (3 pg/mL)';
        if (melDescEl) melDescEl.textContent = 'Bright sunlight suppresses melatonin, boosting alertness.';
        if (tempEl) tempEl.innerHTML = '<span>🌡️</span> 37.0°C (Active Core)';
        if (tempDescEl) tempDescEl.textContent = 'Peak metabolic heat for active learning and physical play.';
        if (alertEl) alertEl.innerHTML = '<span>⚡</span> Bright Alertness';
        if (alertDescEl) alertDescEl.textContent = 'Cortisol peaks; intellectual focus and motor skills optimal.';
    }
}

function getCircadianLabel(h) {
    if (h >= 6 && h <= 8) return "Morning Awakening";
    if (h > 8 && h <= 15) return "School & Active Learning";
    if (h > 15 && h <= 18) return "Outdoor Sports & Play";
    if (h > 18 && h <= 20) return "Family Dinner & Study";
    if (h > 20 && h <= 21) return "Bedtime Wind-Down";
    return "Deep Nighttime Slumber";
}

function toggleBlueScreen() {
    blueScreenOn = !blueScreenOn;
    const btn = document.getElementById('screenToggleBtn');
    if (btn) {
        if (blueScreenOn) {
            btn.textContent = 'Screen ON (Suppresses Melatonin)';
            btn.className = 'px-2 py-0.5 rounded text-xs font-bold bg-rose-950 text-rose-300 border border-rose-700';
        } else {
            btn.textContent = 'Screen OFF (Healthy)';
            btn.className = 'px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-700';
        }
    }
    const slider = document.getElementById('circadianSlider');
    if (slider) updateCircadianSim(slider.value);
}

// Sim 13: Safe vs Unsafe Boundary Radar
const touchScenarios = [
    {
        icon: "🤗",
        title: "SAFE TOUCH: Warm, Open & Caring",
        type: "Consensual, respectful interaction from family",
        badge: "SAFE & HEALTHY",
        desc: "A warm hug from parents or caregivers makes a child feel loved, secure, and respected. It is done openly without secrecy or fear.",
        action: "Action: Enjoy and reciprocate affection with family members",
        gut: "Internal Gut Check: Feels calm and happy"
    },
    {
        icon: "✋",
        title: "SAFE TOUCH: Celebratory Teamwork Gesture",
        type: "Public sports camaraderie with peers",
        badge: "SAFE & RESPECTFUL",
        desc: "A high-five or handshake after scoring a goal in Kho-Kho or Kabaddi. It is spontaneous, mutual, public, and respects personal space.",
        action: "Action: Celebrate team victories with joy and sportsmanship",
        gut: "Internal Gut Check: Feels energetic and proud"
    },
    {
        icon: "⚠️",
        title: "UNSAFE TOUCH: Red-Flag Boundary Breach",
        type: "Secretive, uncomfortable, or non-consensual contact",
        badge: "DANGEROUS RED FLAG",
        desc: "Someone touching private swimsuit zones, demanding secrets ('Do not tell your parents'), or making you feel uneasy, scared, or confused.",
        action: "Action: Use 3-Step Rule -> Shout NO! Run to safety! Tell a trusted adult!",
        gut: "Internal Gut Check: Stomach knots, anxiety, fear alarm sounds"
    }
];

function evaluateTouchScenario(idx) {
    const s = touchScenarios[idx] || touchScenarios[0];
    const iconEl = document.getElementById('touchRadarIcon');
    const titleEl = document.getElementById('touchRadarTitle');
    const typeEl = document.getElementById('touchRadarType');
    const badgeEl = document.getElementById('touchRadarBadge');
    const descEl = document.getElementById('touchRadarDesc');
    const actEl = document.getElementById('touchRadarAction');
    const gutEl = document.getElementById('touchRadarGut');

    if (iconEl) iconEl.textContent = s.icon;
    if (titleEl) titleEl.textContent = s.title;
    if (typeEl) typeEl.textContent = s.type;
    if (badgeEl) {
        badgeEl.textContent = s.badge;
        badgeEl.className = idx === 2
            ? 'text-xs font-extrabold px-2.5 py-1 rounded bg-rose-950 text-rose-300 border border-rose-700'
            : 'text-xs font-extrabold px-2.5 py-1 rounded bg-teal-950 text-teal-300 border border-teal-700';
    }
    if (descEl) descEl.textContent = s.desc;
    if (actEl) actEl.textContent = s.action;
    if (gutEl) gutEl.textContent = s.gut;

    const btns = document.querySelectorAll('.touch-scene-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-teal-500/50', 'bg-teal-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-teal-500/50', 'bg-teal-950/40');
    }
}

// Sim 14: Swimsuit Boundary Defense Shield
const zoneRules = {
    chest: {
        icon: "🎽",
        title: "Chest & Torso Zone",
        rule: "Covered completely by swimsuits. No one has any right to touch this area, look at it, photograph it, or ask you to touch theirs.",
        doctor: "Doctor Checkup Rule: Allowed ONLY for medical checkups when a parent or guardian is standing right beside you inside the room!"
    },
    groin: {
        icon: "🩳",
        title: "Groin & Private Zone (Between Legs)",
        rule: "Strictly private anatomical area covered by underwear and swimwear. Absolutely no one is permitted to touch or view this zone.",
        doctor: "Doctor Checkup Rule: Strictly requires parental presence and medical purpose (e.g. treating an infection or injury)."
    },
    buttocks: {
        icon: "🛡️",
        title: "Buttocks & Lower Back Zone",
        rule: "Private zone covered by swimsuits. Off-limits to anyone. No secrets should ever be kept regarding any touch to this zone.",
        doctor: "Doctor Checkup Rule: Only examined with parent in the room for medical injections or clinical diagnoses."
    },
    mouth: {
        icon: "👄",
        title: "Mouth & Lips Zone",
        rule: "Personal private zone. No one has the right to force kisses or touch your mouth against your will.",
        doctor: "Dentist / Doctor Rule: Certified medical examination of throat/teeth with family present."
    }
};

function inspectZone(zone) {
    const data = zoneRules[zone] || zoneRules.chest;
    const iconEl = document.getElementById('zoneIcon');
    const titleEl = document.getElementById('zoneTitle');
    const ruleEl = document.getElementById('zoneRule');
    const docEl = document.getElementById('zoneDoctorRule');

    if (iconEl) iconEl.textContent = data.icon;
    if (titleEl) titleEl.textContent = data.title;
    if (ruleEl) ruleEl.textContent = data.rule;
    if (docEl) docEl.textContent = data.doctor;
}

// Sim 15: Three-Step Safety Action Hero
const actionSteps = {
    1: {
        icon: "🗣️",
        title: "Step 1: Use Your Bold Voice — Say 'NO!'",
        subtitle: "Stand tall, look them directly in the eye",
        desc: "Say clearly and loudly: 'NO! Stop this! I do not like this!' You never have to be polite to anyone who is crossing your body boundaries.",
        fact: "Voice power stops unwanted behavior in its tracks"
    },
    2: {
        icon: "🏃",
        title: "Step 2: Escape Quickly — Run Away!",
        subtitle: "Do not argue or hesitate; head to safety",
        desc: "Dash immediately to a bright, open public space where other people are present—such as a crowded hallway, main office, or busy playground.",
        fact: "Open public spaces deter unsafe behavior instantly"
    },
    3: {
        icon: "📢",
        title: "Step 3: Tell a Trusted Adult in Your Safety Circle",
        subtitle: "Break the secrecy; speak up until you are protected",
        desc: "Tell your parents, school teacher, or school counselor right away. If the first adult does not listen, keep telling until someone takes action!",
        fact: "Safe adults will believe you; you are 100% free of blame"
    }
};

function selectActionStep(step) {
    const data = actionSteps[step] || actionSteps[1];
    const iconEl = document.getElementById('actionStepIcon');
    const titleEl = document.getElementById('actionStepTitle');
    const subEl = document.getElementById('actionStepSubtitle');
    const descEl = document.getElementById('actionStepDesc');
    const factEl = document.getElementById('actionStepFact');

    if (iconEl) iconEl.textContent = data.icon;
    if (titleEl) titleEl.textContent = data.title;
    if (subEl) subEl.textContent = data.subtitle;
    if (descEl) descEl.textContent = data.desc;
    if (factEl) factEl.textContent = data.fact;

    const btns = document.querySelectorAll('.action-step-btn');
    btns.forEach((b, idx) => {
        b.classList.toggle('active', (idx + 1) === step);
        b.classList.toggle('border-rose-500/50', (idx + 1) === step);
        b.classList.toggle('bg-rose-950/40', (idx + 1) === step);
    });
}

// Sim 16: 24-Hour Holistic Health Planner
const routineData = {
    morning: {
        icon: "🌅",
        title: "Morning Awakening: 6:00 AM - 8:00 AM",
        subtitle: "Foundation for physical energy & mental clarity",
        desc: "Wake up at a consistent time. Drink a glass of warm water, stretch the spine with Tadasana and Vrikshasana, and enjoy a nutritious breakfast of millets and fruits for sustained glucose energy.",
        g1: "💧 Hydration: Warm water kickstarts metabolism",
        g2: "🧘 Movement: 10 mins gentle spinal alignment",
        g3: "🥗 Fuel: Whole grain millet breakfast"
    },
    school: {
        icon: "🎒",
        title: "School Hours: 8:00 AM - 3:00 PM",
        subtitle: "Intellectual growth & mindful dining",
        desc: "Engage enthusiastically in classroom inquiries. At lunch, sit quietly, chew food 30 times, and feel gratitude for the farmers and cooks who made the meal possible.",
        g1: "📚 Focus: Active listening and curious questions",
        g2: "🥪 Mindful Lunch: 30 chews per mouthful",
        g3: "🛡️ Safety: Maintain personal body boundaries"
    },
    afternoon: {
        icon: "⚽",
        title: "Afternoon Active Play: 4:00 PM - 6:00 PM",
        subtitle: "Vigorous aerobic play & team friendships",
        desc: "Spend at least 60 minutes playing outdoor games like Kho-Kho, Kabaddi, cycling, or skipping rope. Strengthens heart muscle, builds bone density, and releases joy endorphins.",
        g1: "🏃 Cardio: 60 minutes vigorous running",
        g2: "🤝 Teamwork: Sportsmanship and laughter",
        g3: "☀️ Sunshine: Natural vitamin D absorption"
    },
    night: {
        icon: "🌙",
        title: "Night Routine & Sleep: 8:00 PM - 6:00 AM",
        subtitle: "Circadian hygiene & restorative glymphatic rest",
        desc: "Turn off all mobile phones and televisions by 8:00 PM. Read a relaxing book, dim the lights, and sleep for 9 to 10 uninterrupted hours in a dark, quiet room.",
        g1: "📵 Digital Curfew: Screens OFF 1 hr before bed",
        g2: "🧠 Brain Rinse: 9-10 hours deep glymphatic wash",
        g3: "🌱 Growth: Pituitary hormone repair cycle"
    }
};

function selectRoutinePhase(phase) {
    const data = routineData[phase] || routineData.morning;
    const iconEl = document.getElementById('routineIcon');
    const titleEl = document.getElementById('routineTitle');
    const subEl = document.getElementById('routineSubtitle');
    const descEl = document.getElementById('routineDesc');
    const g1El = document.getElementById('routineGoal1');
    const g2El = document.getElementById('routineGoal2');
    const g3El = document.getElementById('routineGoal3');

    if (iconEl) iconEl.textContent = data.icon;
    if (titleEl) titleEl.textContent = data.title;
    if (subEl) subEl.textContent = data.subtitle;
    if (descEl) descEl.textContent = data.desc;
    if (g1El) g1El.textContent = data.g1;
    if (g2El) g2El.textContent = data.g2;
    if (g3El) g3El.textContent = data.g3;

    const btns = document.querySelectorAll('.routine-btn');
    btns.forEach(b => {
        b.classList.remove('active', 'border-teal-500/50', 'bg-teal-950/40');
    });
    if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('active', 'border-teal-500/50', 'bg-teal-950/40');
    }
}

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    loadVoices();
    showSlide(1);
});
"""

# Write to JS file
js_file = os.path.join(os.path.dirname(__file__), "class4_science_ch6_js.js")
with open(js_file, "w", encoding="utf-8") as f:
    f.write(js_code)

# Write to Python wrapper
py_file = os.path.join(os.path.dirname(__file__), "class4_science_ch6_js.py")
with open(py_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Science Chapter 6 JavaScript Engine Python Wrapper"""\n\n')
    f.write(f"JS_ENGINE = {repr(js_code)}\n")

print(f"Generated {js_file} and {py_file} successfully!")

// Class 4 Science Chapter 7: How Things Work - Pure Indian Male Teacher Audio & Simulation Engine
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;
let cachedVoices = [];
let userPreferredVoice = "";

// Web Audio API Sound Generator for Melodic Indian Teacher Feedback
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
    } catch (e) {
        console.warn("AudioContext error:", e);
    }
}

// =================== PURE INDIAN MALE TEACHER VOICE LOGIC ===================
// Comprehensive female filter: blocks all female identifiers and female Chrome voices (Google हिन्दी, Google English (India) are female!)
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
    if (!v) return false;
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

    // 1. User manual preference from selector / localStorage
    if (userPreferredVoice) {
        const userChosen = voices.find(v => v.name === userPreferredVoice);
        if (userChosen) return userChosen;
    }

    // 2. Top Tier: Genuine Indian Male Voice (Prabhat, Rishi, Ravi, Pradeep, Mohan, etc.)
    const inMale = voices.find(v => isIndianMaleVoice(v));
    if (inMale) return inMale;

    // 3. Second Tier: Dignified Academic Male Teacher Voice
    const genMale = voices.find(v => isGeneralMaleVoice(v));
    if (genMale) return genMale;

    // 4. Third Tier: Any non-female English voice
    const nonFemaleEn = voices.find(v => (v.lang || '').toLowerCase().startsWith('en') && !isFemaleVoice(v));
    if (nonFemaleEn) return nonFemaleEn;

    // 5. Any voice not explicitly blocked as female
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
        stored = localStorage.getItem('study_lab_voice_science_ch7');
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

function onVoiceChange() {
    const selector = document.getElementById('voiceSelect');
    if (!selector) return;
    userPreferredVoice = selector.value;
    try {
        localStorage.setItem('study_lab_voice_science_ch7', userPreferredVoice);
    } catch (e) {}

    if (isSpeaking) {
        stopAudio();
        playAudio();
    }
}

// Speak Any Text with Pure Indian Male Teacher Sound
window.speakText = function(text) {
    if (!('speechSynthesis' in window) || !text) return;
    window.speechSynthesis.cancel();
    stopSpeechKeepAlive();

    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-IN';
    u.pitch = 0.88; // Warm, deep Indian male teacher pitch
    u.rate = 0.90;  // Measured, didactic Indian classroom cadence

    const selectedVoice = getBestVoice();
    if (selectedVoice) {
        u.voice = selectedVoice;
        if (isIndianMaleVoice(selectedVoice)) {
            u.lang = selectedVoice.lang || 'en-IN';
            u.pitch = 0.88;
            u.rate = 0.90;
        } else {
            u.pitch = 0.84;
            u.rate = 0.92;
        }
    }

    u.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
        startSpeechKeepAlive();
    };

    u.onend = () => {
        stopAudio();
    };

    u.onerror = () => {
        stopAudio();
    };

    window.speechSynthesis.speak(u);
};

function playAudio() {
    if (!('speechSynthesis' in window)) {
        alert("Speech synthesis is not supported in this browser.");
        return;
    }

    if (isSpeaking) {
        stopAudio();
        return;
    }

    // Challenge slides 17-20 are interactive quizzes without automatic lecture
    if (currentSlide > 16) {
        alert("Challenge questions are interactive quiz slides. You can tap the 🔊 speaker button on any question to hear it spoken aloud!");
        return;
    }

    const slideData = window.slideCurriculumData ? window.slideCurriculumData[currentSlide - 1] : null;
    if (!slideData || !slideData.speech || slideData.speech.trim() === '') return;

    window.speechSynthesis.cancel();
    stopSpeechKeepAlive();

    currentUtterance = new SpeechSynthesisUtterance(slideData.speech);
    currentUtterance.lang = 'en-IN';
    currentUtterance.pitch = 0.88; // Dignified baritone Indian male teacher tone
    currentUtterance.rate = 0.90;  // Clear, patient primary school teaching cadence

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
        stopAudio();
    };

    currentUtterance.onerror = () => {
        stopAudio();
    };

    window.speechSynthesis.speak(currentUtterance);
}

function stopAudio() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    stopSpeechKeepAlive();
    isSpeaking = false;
    currentUtterance = null;
    updateAudioButtonUI(false);
}

function toggleAudio() {
    if (isSpeaking) {
        stopAudio();
    } else {
        playAudio();
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

function updateAudioButtonUI(speaking) {
    const playIcon = document.getElementById('audioPlayIcon');
    const audioText = document.getElementById('audioButtonText');
    const audioBtn = document.getElementById('audioLectureBtn') || document.getElementById('audioToggleBtn');
    if (!audioBtn) return;

    if (speaking) {
        if (playIcon) playIcon.textContent = '⏸️';
        if (audioText) audioText.textContent = 'Stop Lecture';
        audioBtn.classList.remove('bg-cyan-600', 'hover:bg-cyan-500');
        audioBtn.classList.add('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
    } else {
        if (playIcon) playIcon.textContent = '🔊';
        if (audioText) audioText.textContent = 'Play Voice Lecture';
        audioBtn.classList.remove('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
        audioBtn.classList.add('bg-cyan-600', 'hover:bg-cyan-500');
    }
}

// Slide Navigation
function showSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    stopAudio();
    currentSlide = slideNum;

    // Toggle slide visibility
    for (let i = 1; i <= totalSlides; i++) {
        const slideEl = document.getElementById(`slide-${i}`);
        if (slideEl) {
            if (i === currentSlide) {
                slideEl.classList.remove('hidden');
            } else {
                slideEl.classList.add('hidden');
            }
        }
    }

    // Update Counter & Progress Bar
    const counterEl = document.getElementById('slideCounter');
    if (counterEl) counterEl.textContent = `${currentSlide} / ${totalSlides}`;

    const progressEl = document.getElementById('progressBar');
    if (progressEl) {
        const pct = (currentSlide / totalSlides) * 100;
        progressEl.style.width = `${pct}%`;
    }

    // Update Prev / Next buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.disabled = false;
        }
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    // Audio button header state: dimmed on challenge slides 17-20
    const audioBtn = document.getElementById('audioLectureBtn') || document.getElementById('audioToggleBtn');
    if (audioBtn) {
        if (currentSlide > 16) {
            audioBtn.style.opacity = '0.5';
            audioBtn.title = "Challenge questions are interactive quiz slides. Use 🔊 on questions to read aloud.";
        } else {
            audioBtn.style.opacity = '1';
            audioBtn.title = "Listen to Pure Indian Male Teacher Lecture";
        }
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

// Checkpoint Verification System
function checkAnswer(slideId, cpIdx, optIdx, correctText) {
    const cpContainer = document.getElementById(`cp-${slideId}-${cpIdx}`);
    if (!cpContainer) return;

    const optButtons = cpContainer.querySelectorAll('.checkpoint-opt-btn');
    const feedbackBox = document.getElementById(`fb-${slideId}-${cpIdx}`);
    const selectedBtn = optButtons[optIdx];
    const isCorrect = (selectedBtn && selectedBtn.getAttribute('data-opt-val') === correctText);

    optButtons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800', 'border-slate-700');
        if (btn.getAttribute('data-opt-val') === correctText) {
            btn.classList.add('bg-emerald-950/70', 'border-emerald-500', 'text-emerald-200');
        }
    });

    if (isCorrect) {
        playTeacherSound(true);
        if (selectedBtn) {
            selectedBtn.classList.add('ring-2', 'ring-emerald-400');
        }
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs flex items-start gap-2">
                    <span class="text-base">✅</span>
                    <div>
                        <strong>Excellent! Correct understanding!</strong>
                        <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                    </div>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    } else {
        playTeacherSound(false);
        if (selectedBtn) {
            selectedBtn.classList.add('bg-rose-950/70', 'border-rose-500', 'text-rose-200', 'ring-2', 'ring-rose-400');
        }
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs flex items-start gap-2">
                    <span class="text-base">💡</span>
                    <div>
                        <strong>Let's think carefully:</strong>
                        <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                    </div>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    }
}

// Challenge Quiz System
function checkQuizAnswer(qId, selectedOption, correctOption) {
    const qContainer = document.getElementById(`quiz-q-${qId}`);
    if (!qContainer) return;

    const optButtons = qContainer.querySelectorAll('.quiz-opt-btn');
    const feedbackBox = document.getElementById(`quiz-fb-${qId}`);
    const isCorrect = (selectedOption === correctOption);

    optButtons.forEach(btn => {
        btn.disabled = true;
        const optVal = btn.getAttribute('data-opt-val');
        if (optVal === correctOption) {
            btn.classList.add('bg-emerald-950/70', 'border-emerald-500', 'text-emerald-200');
        } else if (optVal === selectedOption && !isCorrect) {
            btn.classList.add('bg-rose-950/70', 'border-rose-500', 'text-rose-200');
        }
    });

    if (isCorrect) {
        playTeacherSound(true);
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs flex items-start justify-between gap-2">
                    <div class="flex items-start gap-2">
                        <span class="text-base">🌟</span>
                        <div>
                            <strong>Mastery Achieved! Correct!</strong>
                            <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                        </div>
                    </div>
                    <button onclick="window.showSolutionModal('${qId}')" class="px-2.5 py-1 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-lg text-[11px] whitespace-nowrap shadow">
                        Step Solution
                    </button>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    } else {
        playTeacherSound(false);
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs flex items-start justify-between gap-2">
                    <div class="flex items-start gap-2">
                        <span class="text-base">🔍</span>
                        <div>
                            <strong>Re-examine the evidence:</strong>
                            <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                        </div>
                    </div>
                    <button onclick="window.showSolutionModal('${qId}')" class="px-2.5 py-1 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-lg text-[11px] whitespace-nowrap shadow">
                        Step Solution
                    </button>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    }
}

// 3-Step Solution Modal System
function showSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalContent = document.getElementById('modalContent');
    if (!modal || !modalTitle || !modalContent) return;

    let targetQuestion = null;
    if (window.slideCurriculumData) {
        for (const slide of window.slideCurriculumData) {
            if (slide.questions) {
                const found = slide.questions.find(q => q.id === qId);
                if (found) {
                    targetQuestion = found;
                    break;
                }
            }
        }
    }

    if (!targetQuestion) return;

    modalTitle.textContent = `Comprehensive Scientific Solution: Question ${targetQuestion.id.toUpperCase()}`;
    const steps = targetQuestion.solution_steps || [];

    modalContent.innerHTML = `
        <div class="mb-4 p-3 bg-slate-900 rounded-xl border border-slate-800">
            <span class="text-xs text-cyan-400 font-semibold block mb-1">Question Inquiry:</span>
            <p class="text-sm text-slate-200 font-medium">${targetQuestion.q}</p>
            <div class="mt-2 text-xs font-bold text-emerald-300">
                Correct Answer: <span class="text-slate-100">${targetQuestion.ans}</span>
            </div>
        </div>

        <div class="flex flex-col gap-3">
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-cyan-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-cyan-300">Step 1: Identify Core Physics & Variables</span>
                <p class="text-xs text-slate-300">${steps[0] ? steps[0].replace('Step 1: ', '') : ''}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-amber-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-amber-300">Step 2: Scientific Analysis & Mechanisms</span>
                <p class="text-xs text-slate-300">${steps[1] ? steps[1].replace('Step 2: ', '') : ''}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-emerald-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-emerald-300">Step 3: Conclusive Verification</span>
                <p class="text-xs text-slate-300">${steps[2] ? steps[2].replace('Step 3: ', '') : ''}</p>
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

// ==========================================
// BESPOKE SIMULATOR LOGIC (SIMS 1 - 16)
// ==========================================

// SIM 1: Spinning Objects Motion Lab
let spinObjInterval = null;
let currentSpinAngle = 0;
let currentSpinSpeed = 0;
let selectedSpinObj = 'coin';

const spinObjConfigs = {
    coin: {
        name: "Round Coin",
        stability: "High Symmetry",
        desc: "Coins spin smoothly on their edge when flicked with balanced torque, gradually wobbling into a ringing chatter as rotational speed decreases.",
        svg: `<circle cx="80" cy="80" r="70" fill="#0f172a" stroke="#38bdf8" stroke-width="4" stroke-dasharray="12 6" /><circle cx="80" cy="80" r="16" fill="#0284c7" /><line x1="80" y1="10" x2="80" y2="150" stroke="#bae6fd" stroke-width="3" stroke-linecap="round" /><line x1="10" y1="80" x2="150" y2="80" stroke="#bae6fd" stroke-width="3" stroke-linecap="round" /><circle cx="80" cy="80" r="5" fill="#f8fafc" />`
    },
    bangle: {
        name: "Glass Bangle",
        stability: "Hollow Ring Inertia",
        desc: "A bangle has its mass distributed along the outer circumference, creating high rotational inertia and smooth spinning along its diameter.",
        svg: `<circle cx="80" cy="80" r="68" fill="none" stroke="#a855f7" stroke-width="8" stroke-dasharray="20 8" /><circle cx="80" cy="80" r="54" fill="none" stroke="#d8b4fe" stroke-width="2" /><line x1="80" y1="12" x2="80" y2="148" stroke="#f3e8ff" stroke-width="2" stroke-dasharray="4 2" />`
    },
    top: {
        name: "Wooden Top",
        stability: "Gyroscopic Precision",
        desc: "Designed with an upright pointed axle, spinning tops exhibit gyroscopic stability, staying perfectly vertical before gentle precession begins.",
        svg: `<polygon points="80,15 140,75 80,145 20,75" fill="#d97706" stroke="#fbbf24" stroke-width="3" /><circle cx="80" cy="75" r="14" fill="#92400e" /><circle cx="80" cy="75" r="4" fill="#fef3c7" /><line x1="80" y1="5" x2="80" y2="155" stroke="#ef4444" stroke-width="3" stroke-linecap="round" />`
    },
    eraser: {
        name: "Flat Eraser",
        stability: "Irregular Wobble",
        desc: "With asymmetric rectangular mass and flat friction edges, an eraser wobbles violently and collapses quickly due to uncentered torque.",
        svg: `<rect x="35" y="45" width="90" height="70" rx="8" fill="#e11d48" stroke="#fda4af" stroke-width="3" /><rect x="80" y="45" width="45" height="70" rx="8" fill="#2563eb" stroke="#93c5fd" stroke-width="3" /><circle cx="80" cy="80" r="6" fill="#ffffff" />`
    }
};

window.setSpinObject = function(objKey) {
    selectedSpinObj = objKey;
    const config = spinObjConfigs[objKey];
    const nameEl = document.getElementById('spinObjName');
    const stabEl = document.getElementById('spinStability');
    const descEl = document.getElementById('spinObjDesc');
    const svgEl = document.getElementById('spinVisualSvg');

    if (nameEl) nameEl.textContent = config.name;
    if (stabEl) stabEl.textContent = config.stability;
    if (descEl) descEl.textContent = config.desc;
    if (svgEl) svgEl.innerHTML = config.svg;

    document.querySelectorAll('.spin-obj-btn').forEach(b => {
        b.classList.remove('active', 'border-cyan-500/50', 'bg-cyan-950/40');
    });
    const activeBtn = document.getElementById(`spin-obj-${objKey}`);
    if (activeBtn) activeBtn.classList.add('active', 'border-cyan-500/50', 'bg-cyan-950/40');

    window.stopSpin();
};

window.launchSpin = function() {
    window.stopSpin();
    const slider = document.getElementById('spinForceSlider');
    const force = slider ? parseInt(slider.value) : 70;
    currentSpinSpeed = (force / 100) * 35;

    const badge = document.getElementById('spinStatusBadge');
    if (badge) badge.textContent = `Spinning rapidly! (${Math.round(currentSpinSpeed * 40)} RPM)`;

    const svgEl = document.getElementById('spinVisualSvg');
    spinObjInterval = setInterval(() => {
        currentSpinAngle = (currentSpinAngle + currentSpinSpeed) % 360;
        if (svgEl) {
            svgEl.style.transform = `rotate(${currentSpinAngle}deg)`;
        }
        currentSpinSpeed *= 0.992; // Gradual friction damping
        if (currentSpinSpeed < 0.2) {
            window.stopSpin();
            if (badge) badge.textContent = "Motion stopped due to friction and air resistance.";
        }
    }, 20);
};

window.stopSpin = function() {
    clearInterval(spinObjInterval);
    spinObjInterval = null;
    currentSpinSpeed = 0;
};

// SIM 2: Rotational Pivot Center Lab
let currentPivotShape = 'square';
let currentPivotLoc = 'center';
let pivotAnimInterval = null;

window.setPivotShape = function(shape) {
    currentPivotShape = shape;
    document.querySelectorAll('.pivot-shape-btn').forEach(b => {
        b.classList.remove('active', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`shape-${shape}`);
    if (btn) btn.classList.add('active', 'border-amber-500/60', 'bg-amber-950/40');

    const svg = document.getElementById('pivotSvg');
    if (!svg) return;

    let shapeSvg = '';
    if (shape === 'square') {
        shapeSvg = `<rect id="pivotShapeElem" x="30" y="30" width="100" height="100" rx="8" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="3" />`;
    } else if (shape === 'circle') {
        shapeSvg = `<circle id="pivotShapeElem" cx="80" cy="80" r="55" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="3" />`;
    } else if (shape === 'triangle') {
        shapeSvg = `<polygon id="pivotShapeElem" points="80,25 135,125 25,125" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="3" />`;
    }

    const pinY = (currentPivotLoc === 'center') ? 80 : 45;
    const pinX = (currentPivotLoc === 'center') ? 80 : 110;

    svg.innerHTML = `
        ${shapeSvg}
        <circle id="pivotPinElem" cx="${pinX}" cy="${pinY}" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2" />
        <circle cx="${pinX}" cy="${pinY}" r="2" fill="#ffffff" />
    `;
};

window.setPivotLocation = function(loc) {
    currentPivotLoc = loc;
    document.querySelectorAll('.pivot-loc-btn').forEach(b => {
        b.classList.remove('active', 'border-emerald-500/60', 'bg-emerald-950/40', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`pivot-${loc}`);
    if (btn) btn.classList.add('active', 'border-emerald-500/60', 'bg-emerald-950/40');

    const outcome = document.getElementById('pivotOutcomeText');
    if (outcome) {
        if (loc === 'center') {
            outcome.textContent = "Centered Pivot: Symmetrical mass distribution ensures smooth, stable rotation!";
            outcome.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        } else {
            outcome.textContent = "Off-Center Pivot: Unbalanced center of gravity causes violent wobble and rapid fall!";
            outcome.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        }
    }

    window.setPivotShape(currentPivotShape);
};

window.testPivotSpin = function() {
    window.resetPivotTest();
    const svg = document.getElementById('pivotSvg');
    if (!svg) return;

    let angle = 0;
    let speed = 25;

    pivotAnimInterval = setInterval(() => {
        angle = (angle + speed) % 360;
        if (currentPivotLoc === 'offcenter') {
            const wobbleX = Math.sin(angle * Math.PI / 180) * 18;
            const wobbleY = Math.cos(angle * Math.PI / 180) * 18;
            svg.style.transform = `translate(${wobbleX}px, ${wobbleY}px) rotate(${angle}deg)`;
            speed *= 0.95; // Dies down fast
        } else {
            svg.style.transform = `rotate(${angle}deg)`;
            speed *= 0.99; // Smooth sustained spin
        }

        if (speed < 0.3) {
            clearInterval(pivotAnimInterval);
        }
    }, 20);
};

window.resetPivotTest = function() {
    clearInterval(pivotAnimInterval);
    const svg = document.getElementById('pivotSvg');
    if (svg) svg.style.transform = 'none';
};

// SIM 3: Persistence of Vision & Optical Illusions
let opticMode = 'newton';
window.setOpticMode = function(mode) {
    opticMode = mode;
    document.querySelectorAll('.optic-btn').forEach(b => {
        b.classList.remove('active', 'border-indigo-500/60', 'bg-indigo-950/40');
    });
    const btn = document.getElementById(`optic-mode-${mode}`);
    if (btn) btn.classList.add('active', 'border-indigo-500/60', 'bg-indigo-950/40');

    const svg = document.getElementById('opticSvg');
    if (!svg) return;

    if (mode === 'newton') {
        svg.innerHTML = `
            <g id="newtonSectors">
                <path d="M80,80 L80,10 A70,70 0 0,1 140.6,45 Z" fill="#ef4444" />
                <path d="M80,80 L140.6,45 A70,70 0 0,1 150,80 Z" fill="#f97316" />
                <path d="M80,80 L150,80 A70,70 0 0,1 130,135 Z" fill="#eab308" />
                <path d="M80,80 L130,135 A70,70 0 0,1 80,150 Z" fill="#22c55e" />
                <path d="M80,80 L80,150 A70,70 0 0,1 30,135 Z" fill="#06b6d4" />
                <path d="M80,80 L30,135 A70,70 0 0,1 10,80 Z" fill="#3b82f6" />
                <path d="M80,80 L10,80 A70,70 0 0,1 80,10 Z" fill="#8b5cf6" />
            </g>
            <circle id="opticBlendOverlay" cx="80" cy="80" r="70" fill="#f8fafc" opacity="0" />
            <circle cx="80" cy="80" r="8" fill="#1e293b" stroke="#ffffff" stroke-width="2" />
        `;
    } else {
        svg.innerHTML = `
            <g id="squareCardGroup">
                <rect x="35" y="35" width="90" height="90" fill="#3b82f6" stroke="#93c5fd" stroke-width="3" rx="4" />
                <circle id="squareBlurOverlay" cx="80" cy="80" r="55" fill="#60a5fa" opacity="0" />
                <circle cx="80" cy="80" r="8" fill="#1e293b" stroke="#ffffff" stroke-width="2" />
            </g>
        `;
    }
};

window.updateOpticSpeed = function(rpm) {
    const rpmVal = parseInt(rpm);
    const rpmLabel = document.getElementById('rpmLabel');
    const readout = document.getElementById('opticFpsReadout');
    const svg = document.getElementById('opticSvg');
    if (rpmLabel) rpmLabel.textContent = `${rpmVal} RPM`;

    const blendRatio = Math.min(rpmVal / 900, 0.85);

    if (opticMode === 'newton') {
        const overlay = document.getElementById('opticBlendOverlay');
        if (overlay) overlay.setAttribute('opacity', blendRatio);

        if (readout) {
            if (rpmVal === 0) {
                readout.textContent = "Speed: 0 RPM | Eye Perception: Distinct 7 Rainbow Colors";
            } else if (rpmVal < 350) {
                readout.textContent = `Speed: ${rpmVal} RPM | Eye Perception: Flickering Rainbow Blur`;
            } else {
                readout.textContent = `Speed: ${rpmVal} RPM | Eye Perception: Fused Grayish-White Circle!`;
            }
        }
    } else {
        const overlay = document.getElementById('squareBlurOverlay');
        if (overlay) overlay.setAttribute('opacity', blendRatio * 0.9);

        if (readout) {
            if (rpmVal === 0) {
                readout.textContent = "Speed: 0 RPM | Eye Perception: Distinct Sharp Square Corners";
            } else if (rpmVal < 350) {
                readout.textContent = `Speed: ${rpmVal} RPM | Eye Perception: Corners Flickering Fast`;
            } else {
                readout.textContent = `Speed: ${rpmVal} RPM | Eye Perception: Smooth Translucent Circle!`;
            }
        }
    }

    if (svg) {
        if (rpmVal > 0) {
            svg.style.animation = `spin ${Math.max(0.04, 30 / rpmVal)}s linear infinite`;
        } else {
            svg.style.animation = 'none';
        }
    }
};

// SIM 4: Traditional Indian Lattu Lab
let lattuWraps = 6;
let lattuInterval = null;

window.setLattuStringWraps = function(wraps) {
    lattuWraps = wraps;
    document.querySelectorAll('.lattu-wrap-btn').forEach(b => {
        b.classList.remove('active', 'border-orange-500/60', 'bg-orange-950/40');
    });
    const btn = document.getElementById(`wrap-${wraps}`);
    if (btn) btn.classList.add('active', 'border-orange-500/60', 'bg-orange-950/40');

    const status = document.getElementById('lattuStatusText');
    if (status) status.textContent = `Lattu wound with ${wraps} string coils. Ready to release!`;
};

window.launchLattu = function() {
    window.resetLattu();
    const svg = document.getElementById('lattuSvg');
    const status = document.getElementById('lattuStatusText');
    const coils = document.getElementById('lattuCoilsGroup');
    if (coils) coils.style.display = 'none';

    let speed = lattuWraps * 5;
    let angle = 0;
    let tilt = 0;

    lattuInterval = setInterval(() => {
        angle = (angle + speed) % 360;
        speed *= 0.994;

        if (speed < 12) {
            tilt = (12 - speed) * 2;
        }

        if (svg) {
            svg.style.transform = `rotate(${angle}deg) rotateX(${tilt}deg)`;
        }

        if (status) {
            status.textContent = `Lattu spinning stably! Angular velocity: ${Math.round(speed * 30)} RPM`;
        }

        if (speed < 0.2) {
            clearInterval(lattuInterval);
            if (status) status.textContent = "Lattu toppled after energy lost to ground contact friction.";
        }
    }, 20);
};

window.resetLattu = function() {
    clearInterval(lattuInterval);
    const svg = document.getElementById('lattuSvg');
    if (svg) svg.style.transform = 'none';
    const coils = document.getElementById('lattuCoilsGroup');
    if (coils) coils.style.display = 'block';
};

// SIM 5: Historic Charkha Pulley Ratio Lab
let charkhaInterval = null;
let charkhaAngleBig = 0;
let charkhaAngleSmall = 0;

window.crankCharkha = function() {
    window.stopCharkha();
    const bigWheel = document.getElementById('charkhaBigWheel');
    const spindle = document.getElementById('charkhaSpindle');
    const bigSpeedEl = document.getElementById('charkhaBigSpeed');
    const smallSpeedEl = document.getElementById('charkhaSpindleSpeed');

    charkhaInterval = setInterval(() => {
        charkhaAngleBig = (charkhaAngleBig + 3) % 360;
        charkhaAngleSmall = (charkhaAngleSmall + 60) % 360; // 20:1 ratio

        if (bigWheel) bigWheel.style.transform = `rotate(${charkhaAngleBig}deg)`;
        if (spindle) spindle.style.transform = `rotate(${charkhaAngleSmall}deg)`;

        if (bigSpeedEl) bigSpeedEl.textContent = '60';
        if (smallSpeedEl) smallSpeedEl.textContent = '1200';
    }, 25);
};

window.stopCharkha = function() {
    clearInterval(charkhaInterval);
    const bigSpeedEl = document.getElementById('charkhaBigSpeed');
    const smallSpeedEl = document.getElementById('charkhaSpindleSpeed');
    if (bigSpeedEl) bigSpeedEl.textContent = '0';
    if (smallSpeedEl) smallSpeedEl.textContent = '0';
};

// SIM 6: Surface Friction & Spin Duration Lab
let currentFricSurf = 'glass';
let fricTimer = null;
let fricStartTime = 0;

const fricConfigs = {
    glass: { name: "Polished Glass", duration: 42.0, mu: "0.05", textClass: "text-sky-200", bgClass: "bg-sky-400/20" },
    wood: { name: "Smooth Wood", duration: 22.0, mu: "0.20", textClass: "text-amber-200", bgClass: "bg-amber-400/20" },
    paper: { name: "Paper Sheet", duration: 11.5, mu: "0.45", textClass: "text-slate-200", bgClass: "bg-slate-400/20" },
    carpet: { name: "Rough Carpet", duration: 3.2, mu: "0.85", textClass: "text-rose-200", bgClass: "bg-rose-400/20" }
};

window.setFrictionSurface = function(surf) {
    currentFricSurf = surf;
    document.querySelectorAll('.fric-btn').forEach(b => {
        b.classList.remove('active', 'border-rose-500/60', 'bg-rose-950/40');
    });
    const btn = document.getElementById(`fric-${surf}`);
    if (btn) btn.classList.add('active', 'border-rose-500/60', 'bg-rose-950/40');

    const cfg = fricConfigs[surf];
    const textureEl = document.getElementById('fricSurfaceTexture');
    if (textureEl) {
        textureEl.textContent = `${cfg.name} (μ = ${cfg.mu})`;
        textureEl.className = `absolute bottom-0 w-full h-8 ${cfg.bgClass} flex items-center justify-center text-[10px] ${cfg.textClass}`;
    }

    window.resetFrictionTest();
};

window.startFrictionTest = function() {
    window.resetFrictionTest();
    const cfg = fricConfigs[currentFricSurf];
    const timerText = document.getElementById('fricTimerText');
    const statusText = document.getElementById('fricStatusText');
    const svg = document.getElementById('fricSpinSvg');

    if (svg) svg.style.animation = 'spin 0.15s linear infinite';
    if (statusText) statusText.textContent = 'Spinning...';

    fricStartTime = Date.now();
    fricTimer = setInterval(() => {
        const elapsed = (Date.now() - fricStartTime) / 1000;
        if (timerText) timerText.textContent = `${elapsed.toFixed(1)}s`;

        if (elapsed >= cfg.duration) {
            clearInterval(fricTimer);
            if (svg) svg.style.animation = 'none';
            if (statusText) statusText.textContent = `Stopped! Max time: ${cfg.duration}s`;
        }
    }, 100);
};

window.resetFrictionTest = function() {
    clearInterval(fricTimer);
    const timerText = document.getElementById('fricTimerText');
    const statusText = document.getElementById('fricStatusText');
    const svg = document.getElementById('fricSpinSvg');
    if (timerText) timerText.textContent = '0.0s';
    if (statusText) statusText.textContent = 'Ready';
    if (svg) svg.style.animation = 'none';
};

// SIM 7: Classroom Float vs Sink Basin
const floatSinkItems = {
    leaf: { name: "Dry Leaf", floats: true, icon: "🍃", y: 55 },
    nail: { name: "Iron Nail", floats: false, icon: "🔩", y: 155 },
    bowl: { name: "Steel Bowl", floats: true, icon: "🥣", y: 62 },
    stone: { name: "Pebble", floats: false, icon: "🪨", y: 155 },
    bottle: { name: "Plastic Bottle", floats: true, icon: "🍾", y: 58 },
    wood: { name: "Wood Block", floats: true, icon: "🪵", y: 56 }
};

let droppedItems = new Set();

window.testFloatSinkItem = function(itemKey) {
    const item = floatSinkItems[itemKey];
    if (!item) return;
    droppedItems.add(itemKey);

    renderFloatSinkTank();
    const summary = document.getElementById('floatSinkSummary');
    if (summary) {
        if (item.floats) {
            summary.textContent = `${item.name} FLOATS! Buoyant force balances its weight.`;
            summary.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        } else {
            summary.textContent = `${item.name} SINKS! Its density is higher than water.`;
            summary.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        }
    }
};

function renderFloatSinkTank() {
    const floatGroup = document.getElementById('floatingItemsGroup');
    const sunkGroup = document.getElementById('sunkItemsGroup');
    if (!floatGroup || !sunkGroup) return;

    let floatSvg = '';
    let sunkSvg = '';
    let floatX = 50;
    let sunkX = 50;

    droppedItems.forEach(key => {
        const item = floatSinkItems[key];
        if (item.floats) {
            floatSvg += `<text x="${floatX}" y="${item.y}" font-size="20">${item.icon}</text>`;
            floatX += 45;
        } else {
            sunkSvg += `<text x="${sunkX}" y="${item.y}" font-size="20">${item.icon}</text>`;
            sunkX += 45;
        }
    });

    floatGroup.innerHTML = floatSvg;
    sunkGroup.innerHTML = sunkSvg;
}

window.dropAllFloatSink = function() {
    Object.keys(floatSinkItems).forEach(k => droppedItems.add(k));
    renderFloatSinkTank();
    const summary = document.getElementById('floatSinkSummary');
    if (summary) {
        summary.textContent = "All items tested: Leaves, bowls, wood, and bottles float; nails and stones sink!";
        summary.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-blue-950/80 text-blue-300 border border-blue-700/60";
    }
};

window.resetFloatSinkTank = function() {
    droppedItems.clear();
    renderFloatSinkTank();
    const summary = document.getElementById('floatSinkSummary');
    if (summary) {
        summary.textContent = "Tank reset. Click any item above to test.";
        summary.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700";
    }
};

// SIM 8: Water Buoyancy & Spring Balance Lab
window.submergeStone = function() {
    const assembly = document.getElementById('springBalanceAssembly');
    const needle = document.getElementById('balanceNeedle');
    const vector = document.getElementById('buoyancyVector');
    const weightVal = document.getElementById('apparentWeightVal');

    if (assembly) assembly.style.transform = 'translateY(40px)';
    if (needle) needle.setAttribute('y1', '50'), needle.setAttribute('y2', '50');
    if (vector) vector.setAttribute('opacity', '1');
    if (weightVal) weightVal.textContent = '320 grams (Apparent Weight)';
};

window.liftStone = function() {
    const assembly = document.getElementById('springBalanceAssembly');
    const needle = document.getElementById('balanceNeedle');
    const vector = document.getElementById('buoyancyVector');
    const weightVal = document.getElementById('apparentWeightVal');

    if (assembly) assembly.style.transform = 'translateY(0px)';
    if (needle) needle.setAttribute('y1', '65'), needle.setAttribute('y2', '65');
    if (vector) vector.setAttribute('opacity', '0');
    if (weightVal) weightVal.textContent = '500 grams (Actual Weight)';
};

// SIM 9: Shape Affects Flotation
window.setClayShape = function(shape) {
    document.querySelectorAll('.clay-shape-btn').forEach(b => {
        b.classList.remove('active', 'border-cyan-500/60', 'bg-cyan-950/40');
    });
    const btn = document.getElementById(`clay-${shape}-btn`);
    if (btn) btn.classList.add('active', 'border-cyan-500/60', 'bg-cyan-950/40');

    const item = document.getElementById('clayItemElement');
    const readout = document.getElementById('clayStatusReadout');

    if (shape === 'ball') {
        if (item) {
            item.style.transform = 'translateY(0px)';
            item.innerHTML = `<circle cx="160" cy="150" r="16" fill="#ea580c" stroke="#fed7aa" stroke-width="2" />`;
        }
        if (readout) {
            readout.textContent = "Solid Ball Sinks: Small volume displaces very little water; gravitational pull exceeds buoyant force.";
            readout.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-800/60";
        }
    } else {
        if (item) {
            item.style.transform = 'translateY(-90px)';
            item.innerHTML = `<path d="M110,145 Q160,185 210,145 Z" fill="#ea580c" stroke="#fed7aa" stroke-width="2" />`;
        }
        if (readout) {
            readout.textContent = "Hollow Boat Floats: Wide bowl encloses air, displacing more water than its own weight!";
            readout.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-800/60";
        }
    }
};

// SIM 10: Displacement And Buoyancy
window.lowerArchimedesObject = function() {
    const obj = document.getElementById('archimedesObject');
    const cylinderWater = document.getElementById('cylinderDisplacedWater');
    const stream = document.getElementById('waterStream');
    const readout = document.getElementById('displacedWaterVal');

    if (obj) obj.style.transform = 'translateY(65px)';
    if (stream) stream.setAttribute('opacity', '1');

    setTimeout(() => {
        if (cylinderWater) cylinderWater.setAttribute('height', '50'), cylinderWater.setAttribute('y', '150');
        if (readout) readout.textContent = '35 mL (35 g water weight displaced)';
    }, 400);
};

window.resetArchimedes = function() {
    const obj = document.getElementById('archimedesObject');
    const cylinderWater = document.getElementById('cylinderDisplacedWater');
    const stream = document.getElementById('waterStream');
    const readout = document.getElementById('displacedWaterVal');

    if (obj) obj.style.transform = 'translateY(0px)';
    if (stream) stream.setAttribute('opacity', '0');
    if (cylinderWater) cylinderWater.setAttribute('height', '0'), cylinderWater.setAttribute('y', '198');
    if (readout) readout.textContent = '0 mL (0 g)';
};

// SIM 11: Crafting Model Boats
let boatMaterial = 'plain';
let boatSoakTimer = null;
let boatSoakLevel = 0;

window.selectBoatMaterial = function(mat) {
    boatMaterial = mat;
    document.querySelectorAll('.boat-mat-btn').forEach(b => {
        b.classList.remove('active', 'border-blue-500/60', 'bg-blue-950/40');
    });
    const btn = document.getElementById(`mat-${mat}`);
    if (btn) btn.classList.add('active', 'border-blue-500/60', 'bg-blue-950/40');

    window.resetBoatMaterial();
};

window.testBoatInWater = function() {
    window.resetBoatMaterial();
    const bar = document.getElementById('soakProgressBar');
    const label = document.getElementById('soakPercentLabel');
    const boat = document.getElementById('modelBoatGraphic');

    const rates = { plain: 20, waxed: 3, wood: 1 };
    const rate = rates[boatMaterial] || 15;

    boatSoakTimer = setInterval(() => {
        boatSoakLevel += rate;
        if (boatSoakLevel > 100) boatSoakLevel = 100;

        if (bar) bar.style.width = `${boatSoakLevel}%`;
        if (label) label.textContent = `${boatSoakLevel}%`;

        if (boatSoakLevel >= 80 && boatMaterial === 'plain') {
            if (boat) boat.style.transform = 'translateY(25px) rotate(20deg)';
        }

        if (boatSoakLevel >= 100) {
            clearInterval(boatSoakTimer);
        }
    }, 300);
};

window.resetBoatMaterial = function() {
    clearInterval(boatSoakTimer);
    boatSoakLevel = 0;
    const bar = document.getElementById('soakProgressBar');
    const label = document.getElementById('soakPercentLabel');
    const boat = document.getElementById('modelBoatGraphic');
    if (bar) bar.style.width = '0%';
    if (label) label.textContent = '0%';
    if (boat) boat.style.transform = 'none';
};

// SIM 12: Natural Shell Vessels
let shellCargoCount = 0;
let shellType = 'coconut';
const shellLimits = { coconut: 12, walnut: 3, leaf: 2 };

window.setShellVessel = function(type) {
    shellType = type;
    document.querySelectorAll('.shell-btn').forEach(b => {
        b.classList.remove('active', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`vessel-${type}`);
    if (btn) btn.classList.add('active', 'border-amber-500/60', 'bg-amber-950/40');

    const body = document.getElementById('shellBody');
    if (body) {
        if (type === 'coconut') {
            body.setAttribute('d', 'M110,65 Q160,115 210,65 Z');
            body.setAttribute('fill', '#78350f');
        } else if (type === 'walnut') {
            body.setAttribute('d', 'M125,65 Q160,105 195,65 Z');
            body.setAttribute('fill', '#a16207');
        } else {
            body.setAttribute('d', 'M95,68 Q160,85 225,68 Z');
            body.setAttribute('fill', '#15803d');
        }
    }

    window.resetShellVessel();
};

window.addShellCargo = function() {
    const limit = shellLimits[shellType];
    if (shellCargoCount < limit + 1) {
        shellCargoCount++;
    }

    const group = document.getElementById('shellCargoGroup');
    const status = document.getElementById('shellCargoStatus');
    const graphic = document.getElementById('shellGraphicGroup');

    if (group) {
        let dots = '';
        for (let i = 0; i < shellCargoCount; i++) {
            dots += `<circle cx="${140 + (i % 5) * 8}" cy="${60 - Math.floor(i / 5) * 6}" r="3" fill="#94a3b8" />`;
        }
        group.innerHTML = dots;
    }

    if (status) {
        if (shellCargoCount > limit) {
            status.textContent = `OVERLOADED! Max capacity exceeded! Vessel swamped!`;
            status.className = "mt-1 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
            if (graphic) graphic.style.transform = 'translateY(30px) rotate(15deg)';
        } else {
            status.textContent = `Pebble Cargo: ${shellCargoCount} / Max Safe: ${limit}`;
            status.className = "mt-1 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700";
            if (graphic) graphic.style.transform = `translateY(${shellCargoCount * 1.5}px)`;
        }
    }
};

window.resetShellVessel = function() {
    shellCargoCount = 0;
    const group = document.getElementById('shellCargoGroup');
    const status = document.getElementById('shellCargoStatus');
    const graphic = document.getElementById('shellGraphicGroup');
    if (group) group.innerHTML = '';
    if (status) {
        status.textContent = `Pebble Cargo: 0 / Max Safe: ${shellLimits[shellType]}`;
        status.className = "mt-1 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700";
    }
    if (graphic) graphic.style.transform = 'none';
};

// SIM 13: Boat Stability Dynamics
let currentHullType = 'wide';
window.setHullType = function(type) {
    currentHullType = type;
    document.querySelectorAll('.hull-type-btn').forEach(b => {
        b.classList.remove('active', 'border-violet-500/60', 'bg-violet-950/40');
    });
    const btn = document.getElementById(`hull-${type}`);
    if (btn) btn.classList.add('active', 'border-violet-500/60', 'bg-violet-950/40');

    const hullPoly = document.getElementById('hullPolygon');
    const mastLine = document.getElementById('hullMastLine');
    const mastWeight = document.getElementById('hullMastWeight');
    const cgMarker = document.getElementById('cgMarker');
    const cgLabel = document.getElementById('cgLabel');

    if (type === 'wide') {
        if (hullPoly) hullPoly.setAttribute('points', '90,75 230,75 200,115 120,115');
        if (mastLine) mastLine.setAttribute('y2', '45');
        if (mastWeight) mastWeight.setAttribute('cy', '45');
        if (cgMarker) cgMarker.setAttribute('cy', '85');
        if (cgLabel) cgLabel.setAttribute('y', '88');
    } else {
        if (hullPoly) hullPoly.setAttribute('points', '130,75 190,75 175,120 145,120');
        if (mastLine) mastLine.setAttribute('y2', '15');
        if (mastWeight) mastWeight.setAttribute('cy', '15');
        if (cgMarker) cgMarker.setAttribute('cy', '45');
        if (cgLabel) cgLabel.setAttribute('y', '48');
    }

    const slider = document.getElementById('tiltSlider');
    if (slider) window.updateTiltAngle(slider.value);
};

window.updateTiltAngle = function(deg) {
    const val = parseInt(deg);
    const label = document.getElementById('tiltDegreeLabel');
    const boat = document.getElementById('tiltingBoatGroup');
    const status = document.getElementById('stabilityStatus');
    if (label) label.textContent = `${val}°`;

    if (currentHullType === 'tall' && Math.abs(val) > 25) {
        if (boat) boat.style.transform = `rotate(${val > 0 ? 90 : -90}deg)`;
        if (status) {
            status.textContent = "CAPSIZED! High center of gravity created destabilizing tipping moment!";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        }
    } else {
        if (boat) boat.style.transform = `rotate(${val}deg)`;
        if (status) {
            status.textContent = "Stable Equilibrium: Wide hull generates strong righting torque to restore upright balance.";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        }
    }
};

// SIM 14: Load Capacity Testing
let bargeCoinCount = 0;
const maxSafeCoins = 8;

window.addBargeCoin = function() {
    if (bargeCoinCount >= 12) return;
    bargeCoinCount++;

    const barge = document.getElementById('cargoBargeGroup');
    const coinsGroup = document.getElementById('bargeCoinsGroup');
    const countVal = document.getElementById('coinCountVal');
    const freeboardVal = document.getElementById('freeboardVal');
    const badge = document.getElementById('overloadBadge');

    if (countVal) countVal.textContent = bargeCoinCount;

    const remainingFreeboard = Math.max(0, 15 - bargeCoinCount * 1.8);
    if (freeboardVal) freeboardVal.textContent = `${remainingFreeboard.toFixed(1)} mm`;

    if (barge) barge.style.transform = `translateY(${bargeCoinCount * 2.2}px)`;

    if (coinsGroup) {
        let coinsSvg = '';
        for (let i = 0; i < bargeCoinCount; i++) {
            coinsSvg += `<circle cx="${115 + (i % 6) * 18}" cy="${50 - Math.floor(i / 6) * 8}" r="7" fill="#fbbf24" stroke="#d97706" stroke-width="1.5" />`;
        }
        coinsGroup.innerHTML = coinsSvg;
    }

    if (badge) {
        if (bargeCoinCount > maxSafeCoins) {
            badge.textContent = 'OVERLOADED (Sinking Risk!)';
            badge.className = 'text-rose-400 font-bold';
        } else {
            badge.textContent = 'SAFE';
            badge.className = 'text-emerald-400 font-bold';
        }
    }
};

window.resetBargeLoad = function() {
    bargeCoinCount = 0;
    const barge = document.getElementById('cargoBargeGroup');
    const coinsGroup = document.getElementById('bargeCoinsGroup');
    const countVal = document.getElementById('coinCountVal');
    const freeboardVal = document.getElementById('freeboardVal');
    const badge = document.getElementById('overloadBadge');

    if (barge) barge.style.transform = 'translateY(0px)';
    if (coinsGroup) coinsGroup.innerHTML = '';
    if (countVal) countVal.textContent = '0';
    if (freeboardVal) freeboardVal.textContent = '15 mm';
    if (badge) {
        badge.textContent = 'SAFE';
        badge.className = 'text-emerald-400 font-bold';
    }
};

// SIM 15: Modifying Object Buoyancy
window.setBallastState = function(state) {
    document.querySelectorAll('.ballast-btn').forEach(b => {
        b.classList.remove('active', 'border-cyan-500/60', 'bg-cyan-950/40');
    });
    const btn = document.getElementById(`ballast-${state}`);
    if (btn) btn.classList.add('active', 'border-cyan-500/60', 'bg-cyan-950/40');

    const sub = document.getElementById('subVesselGroup');
    const water = document.getElementById('subBallastWater');
    const stateText = document.getElementById('ballastStateText');
    const densityText = document.getElementById('avgDensityText');

    if (state === 'surface') {
        if (sub) sub.style.transform = 'translateY(0px)';
        if (water) water.setAttribute('height', '10');
        if (stateText) stateText.textContent = 'Air Filled (Floating)';
        if (densityText) densityText.textContent = '0.45 g/cm³';
    } else if (state === 'neutral') {
        if (sub) sub.style.transform = 'translateY(45px)';
        if (water) water.setAttribute('height', '20');
        if (stateText) stateText.textContent = 'Half Flooded (Neutral Hover)';
        if (densityText) densityText.textContent = '1.00 g/cm³';
    } else {
        if (sub) sub.style.transform = 'translateY(85px)';
        if (water) water.setAttribute('height', '32');
        if (stateText) stateText.textContent = 'Fully Flooded (Deep Dive)';
        if (densityText) densityText.textContent = '1.35 g/cm³';
    }
};

// SIM 16: Balanced Mobile Structures
let balanceMode = 'weighted';
window.setBalanceMode = function(mode) {
    balanceMode = mode;
    document.querySelectorAll('.bal-mode-btn').forEach(b => {
        b.classList.remove('active', 'border-emerald-500/60', 'bg-emerald-950/40');
    });
    const btn = document.getElementById(`bal-${mode}`);
    if (btn) btn.classList.add('active', 'border-emerald-500/60', 'bg-emerald-950/40');

    const leftWeight = document.getElementById('leftWingWeight');
    const rightWeight = document.getElementById('rightWingWeight');
    const cgIndicator = document.getElementById('birdCgIndicator');
    const status = document.getElementById('balanceBirdStatus');

    if (mode === 'weighted') {
        if (leftWeight) leftWeight.setAttribute('opacity', '1');
        if (rightWeight) rightWeight.setAttribute('opacity', '1');
        if (cgIndicator) cgIndicator.setAttribute('opacity', '1');
        if (status) {
            status.textContent = "Stable Equilibrium: Wing weights pull overall Center of Gravity well below the beak pivot!";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        }
    } else {
        if (leftWeight) leftWeight.setAttribute('opacity', '0');
        if (rightWeight) rightWeight.setAttribute('opacity', '0');
        if (cgIndicator) cgIndicator.setAttribute('opacity', '0');
        if (status) {
            status.textContent = "Unstable: Center of Gravity rises above the beak; bird instantly topples when touched!";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        }
    }

    window.resetBalancingBird();
};

window.nudgeBalancingBird = function() {
    const assembly = document.getElementById('birdAssemblyGroup');
    if (!assembly) return;

    if (balanceMode === 'weighted') {
        assembly.style.transform = 'rotate(25deg)';
        setTimeout(() => {
            assembly.style.transform = 'rotate(-18deg)';
            setTimeout(() => {
                assembly.style.transform = 'rotate(10deg)';
                setTimeout(() => {
                    assembly.style.transform = 'rotate(0deg)';
                }, 300);
            }, 300);
        }, 300);
    } else {
        assembly.style.transform = 'rotate(95deg) translateY(40px)';
    }
};

window.resetBalancingBird = function() {
    const assembly = document.getElementById('birdAssemblyGroup');
    if (assembly) assembly.style.transform = 'none';
};

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    loadVoices();
    showSlide(1);
});

// Class 4 Science Chapter 8: How Things are Made - Pure Indian Male Teacher Audio & Simulation Engine
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

    const indianMaleKeywords = [
        'prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'karan', 'mohan',
        'deepak', 'kumar', 'sanjay', 'ajay', 'vijay', 'amit', 'rahul',
        'rajesh', 'vikram', 'arun', 'manish', 'suresh', 'ramesh', 'anil',
        'sunil', 'en-in-x-ahp', 'en-in-x-cxx', 'en-in-standard-b',
        'en-in-standard-c', 'en-in-wavenet-b', 'en-in-wavenet-c', 'en-in-neural2-b',
        'hi-in-standard-b', 'hi-in-standard-c', 'hi-in-wavenet-b', 'hi-in-wavenet-c'
    ];
    if (indianMaleKeywords.some(k => name.includes(k))) return true;

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

    if (userPreferredVoice) {
        const userChosen = voices.find(v => v.name === userPreferredVoice);
        if (userChosen) return userChosen;
    }

    const inMale = voices.find(v => isIndianMaleVoice(v));
    if (inMale) return inMale;

    const genMale = voices.find(v => isGeneralMaleVoice(v));
    if (genMale) return genMale;

    const nonFemaleEn = voices.find(v => (v.lang || '').toLowerCase().startsWith('en') && !isFemaleVoice(v));
    if (nonFemaleEn) return nonFemaleEn;

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

    let stored = null;
    try {
        stored = localStorage.getItem('study_lab_voice_science_ch8');
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
        localStorage.setItem('study_lab_voice_science_ch8', userPreferredVoice);
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
    u.pitch = 0.88;
    u.rate = 0.90;

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
    currentUtterance.pitch = 0.88;
    currentUtterance.rate = 0.90;

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
        audioBtn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500');
        audioBtn.classList.add('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
    } else {
        if (playIcon) playIcon.textContent = '🔊';
        if (audioText) audioText.textContent = 'Teacher Sound Lecture';
        audioBtn.classList.remove('bg-rose-600', 'hover:bg-rose-500', 'ring-2', 'ring-rose-400', 'animate-pulse');
        audioBtn.classList.add('bg-emerald-600', 'hover:bg-emerald-500');
    }
}

// Slide Navigation
function showSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    stopAudio();
    currentSlide = slideNum;

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

    const counterEl = document.getElementById('slideCounter');
    if (counterEl) counterEl.textContent = `${currentSlide} / ${totalSlides}`;

    const progressEl = document.getElementById('progressBar');
    if (progressEl) {
        const pct = (currentSlide / totalSlides) * 100;
        progressEl.style.width = `${pct}%`;
    }

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
                    <button onclick="window.showSolutionModal('${qId}')" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-lg text-[11px] whitespace-nowrap shadow">
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
                    <button onclick="window.showSolutionModal('${qId}')" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-lg text-[11px] whitespace-nowrap shadow">
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
            <span class="text-xs text-emerald-400 font-semibold block mb-1">Question Inquiry:</span>
            <p class="text-sm text-slate-200 font-medium">${targetQuestion.q}</p>
            <div class="mt-2 text-xs font-bold text-emerald-300">
                Correct Answer: <span class="text-slate-100">${targetQuestion.ans}</span>
            </div>
        </div>

        <div class="flex flex-col gap-3">
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-emerald-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-emerald-300">Step 1: Identify Core Scientific Principle</span>
                <p class="text-xs text-slate-300">${steps[0] ? steps[0].replace('Step 1: ', '') : ''}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-amber-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-amber-300">Step 2: Scientific Analysis & Mechanism</span>
                <p class="text-xs text-slate-300">${steps[1] ? steps[1].replace('Step 2: ', '') : ''}</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/90 border-l-4 border-cyan-400 flex flex-col gap-1">
                <span class="text-xs font-bold text-cyan-300">Step 3: Conclusive Verification</span>
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

// SIM 1: Tree To Paper Source Explorer
const paperSourceItems = {
    notebook: { icon: "📓", name: "School Notebook", expl: "School Notebook: Made from chemically refined, bleached wood pulp from forest trees." },
    newspaper: { icon: "📰", name: "Daily Newspaper", expl: "Daily Newspaper: Printed on lightweight mechanical groundwood pulp containing shortened fibers." },
    napkin: { icon: "🧻", name: "Paper Napkin", expl: "Paper Napkin: Highly porous, creped cellulose tissue engineered for rapid liquid absorption." },
    box: { icon: "📦", name: "Shipping Box", expl: "Shipping Box: Heavy, unbleached kraft cardboard layered with corrugated flutes for structural strength." }
};

window.setPaperSourceItem = function(itemKey) {
    const data = paperSourceItems[itemKey];
    if (!data) return;

    document.querySelectorAll('.src-item-btn').forEach(b => {
        b.classList.remove('active', 'border-emerald-500/60', 'bg-emerald-950/40');
    });
    const activeBtn = document.getElementById(`src-${itemKey}`);
    if (activeBtn) activeBtn.classList.add('active', 'border-emerald-500/60', 'bg-emerald-950/40');

    const iconEl = document.getElementById('productIconSvg');
    const labelEl = document.getElementById('productLabelSvg');
    const explEl = document.getElementById('sourceExplText');

    if (iconEl) iconEl.textContent = data.icon;
    if (labelEl) labelEl.textContent = data.name;
    if (explEl) explEl.textContent = data.expl;
};

// SIM 2: Paper Surface Texture Microscope
let currentTextureSample = 'virgin';
window.setTextureSample = function(sample) {
    currentTextureSample = sample;
    document.querySelectorAll('.tex-btn').forEach(b => {
        b.classList.remove('active', 'border-cyan-500/60', 'bg-cyan-950/40');
    });
    const btn = document.getElementById(`tex-${sample}`);
    if (btn) btn.classList.add('active', 'border-cyan-500/60', 'bg-cyan-950/40');

    renderMicroscopeView();
};

window.updateMicroscopeZoom = function(zoom) {
    const val = parseInt(zoom);
    const label = document.getElementById('zoomLevelText');
    if (label) label.textContent = `${val}x`;
    renderMicroscopeView();
};

function renderMicroscopeView() {
    const group = document.getElementById('microscopeSampleGroup');
    const readout = document.getElementById('textureReadoutBadge');
    if (!group) return;

    if (currentTextureSample === 'virgin') {
        group.innerHTML = `
            <rect x="0" y="0" width="160" height="160" fill="#f8fafc" />
            <line x1="10" y1="30" x2="150" y2="30" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="20" y1="80" x2="140" y2="80" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6 3" />
            <line x1="15" y1="130" x2="145" y2="130" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 5" />
            <circle cx="80" cy="80" r="6" fill="#94a3b8" opacity="0.4" />
        `;
        if (readout) {
            readout.textContent = "Smooth Texture: Mineral kaolin coating and heavy factory rollers seal fiber pores.";
            readout.className = "mt-3 text-xs font-semibold px-3 py-1 rounded-full bg-cyan-950/80 text-cyan-300 border border-cyan-700/60";
        }
    } else {
        group.innerHTML = `
            <rect x="0" y="0" width="160" height="160" fill="#fef3c7" />
            <!-- Entangled organic fibers -->
            <path d="M10,20 Q80,70 150,25" stroke="#b45309" stroke-width="4" fill="none" stroke-linecap="round" />
            <path d="M20,140 Q90,90 140,145" stroke="#92400e" stroke-width="5" fill="none" stroke-linecap="round" />
            <path d="M30,80 Q80,120 130,70" stroke="#d97706" stroke-width="4.5" fill="none" stroke-linecap="round" />
            <path d="M80,10 Q60,80 85,150" stroke="#78350f" stroke-width="3.5" fill="none" stroke-linecap="round" />
            <circle cx="50" cy="60" r="4" fill="#a16207" />
            <circle cx="110" cy="110" r="5" fill="#a16207" />
        `;
        if (readout) {
            readout.textContent = "Rough Texture: Shortened, hand-pressed fibers create natural organic ridges and pores.";
            readout.className = "mt-3 text-xs font-semibold px-3 py-1 rounded-full bg-amber-950/80 text-amber-300 border border-amber-700/60";
        }
    }
}

// SIM 3: Paper Shredding & Fiber Release Lab
let tearDirection = 'grain';
window.setTearDirection = function(dir) {
    tearDirection = dir;
    document.querySelectorAll('.tear-btn').forEach(b => {
        b.classList.remove('active', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`tear-${dir}`);
    if (btn) btn.classList.add('active', 'border-amber-500/60', 'bg-amber-950/40');

    window.resetTearAction();
};

window.performTearAction = function() {
    const leftHalf = document.getElementById('tearLeftHalf');
    const rightHalf = document.getElementById('tearRightHalf');
    const status = document.getElementById('tearStatusText');

    if (tearDirection === 'grain') {
        if (leftHalf) leftHalf.style.transform = 'translateX(-20px)';
        if (rightHalf) rightHalf.style.transform = 'translateX(20px)';
        if (status) {
            status.textContent = "Clean Tear: Tearing along the grain splits parallel fibers cleanly with low resistance!";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        }
    } else {
        if (leftHalf) leftHalf.style.transform = 'translateX(-25px) rotate(-6deg)';
        if (rightHalf) rightHalf.style.transform = 'translateX(25px) rotate(6deg)';
        if (status) {
            status.textContent = "Jagged Tear: Tearing across the grain snaps across strong cellulose fibers, producing ragged fringes!";
            status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-amber-950/80 text-amber-300 border border-amber-700/60";
        }
    }
};

window.resetTearAction = function() {
    const leftHalf = document.getElementById('tearLeftHalf');
    const rightHalf = document.getElementById('tearRightHalf');
    const status = document.getElementById('tearStatusText');
    if (leftHalf) leftHalf.style.transform = 'none';
    if (rightHalf) rightHalf.style.transform = 'none';
    if (status) {
        status.textContent = "Ready: Select direction and pull paper sheet to test tearing dynamics.";
        status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700";
    }
};

// SIM 4: Methi Seed Mucilage Binding Engine
window.setMethiSoak = function(hours) {
    document.querySelectorAll('.methi-soak-btn').forEach(b => {
        b.classList.remove('active', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`soak-${hours}`);
    if (btn) btn.classList.add('active', 'border-amber-500/60', 'bg-amber-950/40');

    const hoursLabel = document.getElementById('methiHoursLabel');
    const viscLabel = document.getElementById('viscosityLabel');
    const integLabel = document.getElementById('integrityLabel');
    const bar = document.getElementById('strengthBarElem');
    const valText = document.getElementById('strengthValText');
    const halos = document.getElementById('mucilageHalosGroup');

    if (hoursLabel) hoursLabel.textContent = `${hours} Hours`;

    if (hours === 0) {
        if (viscLabel) viscLabel.textContent = "Watery (None)";
        if (integLabel) integLabel.textContent = "Fragile (Powdery)";
        if (bar) bar.style.width = "15px", bar.setAttribute('fill', '#ef4444');
        if (valText) valText.textContent = "Low (Crumbly)";
        if (halos) halos.setAttribute('opacity', '0.1');
    } else if (hours === 6) {
        if (viscLabel) viscLabel.textContent = "Medium Gel";
        if (integLabel) integLabel.textContent = "Moderate";
        if (bar) bar.style.width = "38px", bar.setAttribute('fill', '#eab308');
        if (valText) valText.textContent = "Medium Strength";
        if (halos) halos.setAttribute('opacity', '0.5');
    } else {
        if (viscLabel) viscLabel.textContent = "Thick Sticky Mucilage";
        if (integLabel) integLabel.textContent = "Resilient & Cohesive";
        if (bar) bar.style.width = "60px", bar.setAttribute('fill', '#10b981');
        if (valText) valText.textContent = "High (Optimal)";
        if (halos) halos.setAttribute('opacity', '0.9');
    }
};

// SIM 5: Pulp Mashing & Consistency Tank
let blenderTimer = null;
let currentBlenderAngle = 0;

window.setPulpSlurryMode = function(mode) {
    document.querySelectorAll('.slurry-btn').forEach(b => {
        b.classList.remove('active', 'border-blue-500/60', 'bg-blue-950/40');
    });
    const btn = document.getElementById(`slurry-${mode}`);
    if (btn) btn.classList.add('active', 'border-blue-500/60', 'bg-blue-950/40');

    const text = document.getElementById('slurryOutcomeText');
    if (text) {
        if (mode === 'thick') {
            text.textContent = "Thick Paste: Fibers are clumped together like bread dough, producing an overly thick, uneven sheet.";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        } else if (mode === 'optimal') {
            text.textContent = "Optimal Consistency: Fibers float freely, ready to form an even, continuous sheet!";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        } else {
            text.textContent = "Watery Slurry: Too few fibers per volume, causing hollow pinholes and fragile paper.";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-amber-950/80 text-amber-300 border border-amber-700/60";
        }
    }
};

window.stirPulpBlender = function() {
    window.stopPulpBlender();
    const shaft = document.getElementById('blenderShaft');
    blenderTimer = setInterval(() => {
        currentBlenderAngle = (currentBlenderAngle + 30) % 360;
        if (shaft) shaft.style.transform = `rotate(${Math.sin(currentBlenderAngle * Math.PI / 180) * 15}deg)`;
    }, 50);
};

window.stopPulpBlender = function() {
    clearInterval(blenderTimer);
    const shaft = document.getElementById('blenderShaft');
    if (shaft) shaft.style.transform = 'none';
};

// SIM 6: Mesh Screen Deckle & Water Press Lab
window.submergeDeckle = function() {
    const frame = document.getElementById('deckleFrameGroup');
    const mat = document.getElementById('wetMatOnMesh');
    const bar = document.getElementById('moistureBarElem');
    const label = document.getElementById('moisturePctLabel');
    const drops = document.getElementById('drainingDropsGroup');

    if (frame) frame.style.transform = 'translateY(35px)';
    if (mat) mat.setAttribute('opacity', '0.4');
    if (bar) bar.style.width = '100%';
    if (label) label.textContent = '100% (Submerged in Slurry)';
    if (drops) drops.setAttribute('opacity', '0');
};

window.liftDeckle = function() {
    const frame = document.getElementById('deckleFrameGroup');
    const mat = document.getElementById('wetMatOnMesh');
    const bar = document.getElementById('moistureBarElem');
    const label = document.getElementById('moisturePctLabel');
    const drops = document.getElementById('drainingDropsGroup');

    if (frame) frame.style.transform = 'translateY(-20px)';
    if (mat) mat.setAttribute('opacity', '0.9');
    if (bar) bar.style.width = '60%';
    if (label) label.textContent = '60% (Water Drained through Mesh)';
    if (drops) drops.setAttribute('opacity', '1');
};

window.pressSponge = function() {
    const frame = document.getElementById('deckleFrameGroup');
    const mat = document.getElementById('wetMatOnMesh');
    const bar = document.getElementById('moistureBarElem');
    const label = document.getElementById('moisturePctLabel');
    const drops = document.getElementById('drainingDropsGroup');

    if (frame) frame.style.transform = 'translateY(0px)';
    if (mat) mat.setAttribute('opacity', '1');
    if (bar) bar.style.width = '20%';
    if (label) label.textContent = '20% (Moisture Squeezed, Fibers Bonded)';
    if (drops) drops.setAttribute('opacity', '0');
};

// SIM 7: Botanical Dye Extraction Chamber
let currentDye = 'turmeric';
window.selectBotanicalDye = function(dyeKey) {
    currentDye = dyeKey;
    document.querySelectorAll('.botanical-dye-btn').forEach(b => {
        b.classList.remove('active', 'border-yellow-500/60', 'bg-yellow-950/40');
    });
    const btn = document.getElementById(`dye-${dyeKey}`);
    if (btn) btn.classList.add('active', 'border-yellow-500/60', 'bg-yellow-950/40');

    window.resetBotanicalDye();
};

window.addAlkalineSoap = function() {
    if (currentDye !== 'turmeric') {
        alert("pH color shift test is demonstrated with Curcumin (Turmeric dye). Select Turmeric to observe the shift!");
        return;
    }

    const flask = document.getElementById('flaskFluid');
    const sheet = document.getElementById('tintedPaperSheet');
    const text = document.getElementById('dyeScientificReadout');

    if (flask) flask.setAttribute('fill', '#dc2626');
    if (sheet) sheet.setAttribute('fill', '#ea580c');
    if (text) {
        text.textContent = "pH Indicator Shift! Alkaline baking soda changes yellow curcumin into vibrant vermillion red-orange!";
        text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
    }
};

window.resetBotanicalDye = function() {
    const flask = document.getElementById('flaskFluid');
    const sheet = document.getElementById('tintedPaperSheet');
    const text = document.getElementById('dyeScientificReadout');

    if (currentDye === 'turmeric') {
        if (flask) flask.setAttribute('fill', '#eab308');
        if (sheet) sheet.setAttribute('fill', '#fef08a');
        if (text) {
            text.textContent = "Curcumin Pigment: Brilliant golden-yellow dye harvested from organic turmeric rhizomes.";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-yellow-950/80 text-yellow-300 border border-yellow-700/60";
        }
    } else if (currentDye === 'beetroot') {
        if (flask) flask.setAttribute('fill', '#be123c');
        if (sheet) sheet.setAttribute('fill', '#f43f5e');
        if (text) {
            text.textContent = "Betalain Pigment: Rich ruby-magenta botanical dye extracted by simmering fresh beetroot.";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60";
        }
    } else {
        if (flask) flask.setAttribute('fill', '#15803d');
        if (sheet) sheet.setAttribute('fill', '#86efac');
        if (text) {
            text.textContent = "Chlorophyll Pigment: Earthy green natural dye harvested from crushed fresh spinach leaves.";
            text.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
        }
    }
};

// SIM 8: Greeting Card Upcycling Workshop
window.addCardEmbellishment = function(type) {
    const leaf = document.getElementById('cardLeafElem');
    const bow = document.getElementById('cardBowElem');
    const badge = document.getElementById('cardStatusBadge');

    if (type === 'leaf') {
        if (leaf) leaf.setAttribute('opacity', '1');
        if (badge) badge.textContent = "Pressed Leaf Added! Botanical foliage brings nature's beauty to handmade cards.";
    } else {
        if (bow) bow.setAttribute('opacity', '1');
        if (badge) badge.textContent = "Jute Twine Bow Added! Natural plant fiber bow secures the card with rustic elegance.";
    }
};

// SIM 9: Industrial Paper Mill Process Flow
const millStages = [
    { title: "Stage 1: Debarking & Chipping", desc: "Tree trunks are mechanically debarked and sliced into small wood chips.", logOp: "1", digOp: "0.2", rollOp: "0.2" },
    { title: "Stage 2: Chemical Digestion", desc: "Wood chips are cooked with steam and chemicals to dissolve lignin and free cellulose.", logOp: "0.2", digOp: "1", rollOp: "0.2" },
    { title: "Stage 3: Fourdrinier Wire Web", desc: "Watery pulp is sprayed across high-speed wire conveyors to form a continuous web.", logOp: "0.2", digOp: "0.2", rollOp: "0.7" },
    { title: "Stage 4: Heated Calender Rollers", desc: "Steam-heated steel cylinders press, dry, and wind finished paper into giant rolls.", logOp: "0.2", digOp: "0.2", rollOp: "1" }
];

window.setMillStage = function(idx) {
    document.querySelectorAll('.mill-stage-btn').forEach(b => {
        b.classList.remove('active', 'border-indigo-500/60', 'bg-indigo-950/40');
    });
    const btn = document.getElementById(`mill-stage-${idx}`);
    if (btn) btn.classList.add('active', 'border-indigo-500/60', 'bg-indigo-950/40');

    const data = millStages[idx];
    const badge = document.getElementById('millStageDescBadge');
    const logs = document.getElementById('millGraphicLogs');
    const digester = document.getElementById('millGraphicDigester');
    const rollers = document.getElementById('millGraphicRollers');

    if (badge) badge.textContent = data.desc;
    if (logs) logs.setAttribute('opacity', data.logOp);
    if (digester) digester.setAttribute('opacity', data.digOp);
    if (rollers) rollers.setAttribute('opacity', data.rollOp);
};

// SIM 10: Ancient Writing Surfaces Interactive Museum
const ancientSurfaces = {
    talapatra: { name: "Talapatra (Palm Leaf)", desc: "Talapatra: Seasoned palm leaves inscribed with an iron stylus and highlighted with lampblack soot." },
    bhojpatra: { name: "Bhojpatra (Birch Bark)", desc: "Bhojpatra: Papery inner bark of the Himalayan birch tree, celebrated for spiritual manuscripts." },
    phalka: { name: "Phalka (Wooden Slate)", desc: "Phalka: Smooth wooden board used with washable natural chalk in traditional village schools." },
    pata: { name: "Pata (Starched Cloth)", desc: "Pata: Hand-woven cotton cloth layered with rice paste and tamarind glue for narrative paintings." }
};

window.selectAncientSurface = function(key) {
    const data = ancientSurfaces[key];
    if (!data) return;

    document.querySelectorAll('.ancient-surf-btn').forEach(b => {
        b.classList.remove('active', 'border-amber-500/60', 'bg-amber-950/40');
    });
    const btn = document.getElementById(`surf-${key}`);
    if (btn) btn.classList.add('active', 'border-amber-500/60', 'bg-amber-950/40');

    const readout = document.getElementById('ancientSurfaceReadout');
    if (readout) readout.textContent = data.desc;
};

// SIM 11: Banana Stem Fiber Extraction Lab
window.runBananaDecorticator = function() {
    const stalk = document.getElementById('bananaStalkGraphic');
    const fibers = document.getElementById('extractedFibersGraphic');
    const status = document.getElementById('decorticatorStatusText');

    if (stalk) stalk.style.transform = 'translateX(40px)';
    if (fibers) fibers.setAttribute('opacity', '1');
    if (status) {
        status.textContent = "Fibers Extracted! Strong, gleaming white cellulose strands harvested without cutting down a single tree!";
        status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60";
    }
};

window.resetBananaDecorticator = function() {
    const stalk = document.getElementById('bananaStalkGraphic');
    const fibers = document.getElementById('extractedFibersGraphic');
    const status = document.getElementById('decorticatorStatusText');
    if (stalk) stalk.style.transform = 'none';
    if (fibers) fibers.setAttribute('opacity', '0.2');
    if (status) {
        status.textContent = "Decorticator Ready: Feed post-harvest banana pseudostem through rollers!";
        status.className = "mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700";
    }
};

// SIM 12: Paper Thickness & Absorbency Analyzer
const paperGrades = {
    tissue: { height: 4, fill: "#f8fafc", rate: "Instant (0.2s)", crush: "Very Low", spreadRx: 45, spreadRy: 6 },
    notebook: { height: 8, fill: "#f1f5f9", rate: "Moderate (2.5s)", crush: "Medium", spreadRx: 20, spreadRy: 5 },
    cardstock: { height: 16, fill: "#e2e8f0", rate: "Slow (8.0s)", crush: "High", spreadRx: 10, spreadRy: 4 },
    corrugated: { height: 26, fill: "#d97706", rate: "Very Slow", crush: "Tremendous (Fluted Arch)", spreadRx: 8, spreadRy: 4 }
};

let currentGrade = 'tissue';
window.setPaperGrade = function(key) {
    currentGrade = key;
    document.querySelectorAll('.paper-grade-btn').forEach(b => {
        b.classList.remove('active', 'border-cyan-500/60', 'bg-cyan-950/40');
    });
    const btn = document.getElementById(`grade-${key}`);
    if (btn) btn.classList.add('active', 'border-cyan-500/60', 'bg-cyan-950/40');

    const cfg = paperGrades[key];
    const rect = document.getElementById('gradeSampleRect');
    const rateText = document.getElementById('absorbRateText');
    const crushText = document.getElementById('crushStrengthText');

    if (rect) {
        rect.setAttribute('height', cfg.height);
        rect.setAttribute('fill', cfg.fill);
        rect.setAttribute('y', 90 - cfg.height / 2);
    }
    if (rateText) rateText.textContent = cfg.rate;
    if (crushText) crushText.textContent = cfg.crush;

    window.resetGradeTest();
};

window.dropWaterOnGrade = function() {
    const pipette = document.getElementById('pipetteDropGroup');
    const spread = document.getElementById('capillarySpreadCircle');
    const cfg = paperGrades[currentGrade];

    if (pipette) pipette.style.transform = 'translateY(35px)';
    setTimeout(() => {
        if (spread) {
            spread.setAttribute('rx', cfg.spreadRx);
            spread.setAttribute('ry', cfg.spreadRy);
        }
    }, 300);
};

window.resetGradeTest = function() {
    const pipette = document.getElementById('pipetteDropGroup');
    const spread = document.getElementById('capillarySpreadCircle');
    if (pipette) pipette.style.transform = 'none';
    if (spread) {
        spread.setAttribute('rx', '0');
        spread.setAttribute('ry', '0');
    }
};

// SIM 13: Braille Dot Matrix Embossing Lab
const brailleLetters = {
    A: { active: [1], text: "Letter A: Dot 1 embossed. Heavy cardstock fibers stretch into a firm, permanent tactile dome!" },
    B: { active: [1, 2], text: "Letter B: Dots 1 and 2 embossed in the left column for easy touch identification." },
    C: { active: [1, 4], text: "Letter C: Dots 1 and 4 embossed across the top horizontal row." },
    L: { active: [1, 2, 3], text: "Letter L: Dots 1, 2, and 3 embossed in a complete vertical left-column line." }
};

window.setBrailleChar = function(char) {
    document.querySelectorAll('.braille-char-btn').forEach(b => {
        b.classList.remove('active', 'border-violet-500/60', 'bg-violet-950/40');
    });
    const btn = document.getElementById(`br-char-${char}`);
    if (btn) btn.classList.add('active', 'border-violet-500/60', 'bg-violet-950/40');

    const cfg = brailleLetters[char];
    for (let i = 1; i <= 6; i++) {
        const dot = document.getElementById(`bdot-${i}`);
        if (dot) {
            if (cfg.active.includes(i)) {
                dot.setAttribute('fill', '#7c3aed');
            } else {
                dot.setAttribute('fill', '#e2e8f0');
            }
        }
    }

    const text = document.getElementById('brailleMeaningText');
    if (text) text.textContent = cfg.text;
};

// SIM 14: 5Rs Waste Hierarchy Sorting Machine
const fiveRData = {
    refuse: { icon: "🚫", title: "Refuse: Stop Waste at the Source", sub: "Say NO to single-use plastics and unnecessary disposables", ex: "Example: Politely decline single-use plastic drinking straws, disposable cups, and plastic gift wrappers." },
    reduce: { icon: "📉", title: "Reduce: Consume Mindfully", sub: "Use fewer resources to accomplish tasks", ex: "Example: Write on both sides of every notebook page and print documents only when strictly necessary." },
    reuse: { icon: "🔁", title: "Reuse: Use Multiple Times", sub: "Extend an item's working life without reprocessing", ex: "Example: Pass school textbooks to younger students and carry durable cloth bags for shopping." },
    repurpose: { icon: "🎨", title: "Repurpose: Invent New Functions", sub: "Find creative uses for items destined for the bin", ex: "Example: Paint old glass jam jars to hold pencils, and craft newspaper sheets into gift envelopes and toys." },
    recycle: { icon: "♻️", title: "Recycle: Remanufacture Materials", sub: "Process sorted waste into brand new raw materials", ex: "Example: Send clean scrap paper to mills to be re-pulped and turned into fresh recycled paper." }
};

window.select5RAction = function(key) {
    const data = fiveRData[key];
    if (!data) return;

    document.querySelectorAll('.r-btn').forEach(b => {
        b.classList.remove('active', 'border-emerald-500/60', 'bg-emerald-950/40');
    });
    const btn = document.getElementById(`r-${key}`);
    if (btn) btn.classList.add('active', 'border-emerald-500/60', 'bg-emerald-950/40');

    const iconEl = document.getElementById('rIcon');
    const titleEl = document.getElementById('rTitle');
    const subEl = document.getElementById('rSubtitle');
    const exEl = document.getElementById('rExample');

    if (iconEl) iconEl.textContent = data.icon;
    if (titleEl) titleEl.textContent = data.title;
    if (subEl) subEl.textContent = data.sub;
    if (exEl) exEl.textContent = data.ex;
};

// SIM 15: Kinetic Newspaper Toy Workshop
let currentToy = 'butterfly';
window.setKineticToy = function(toyKey) {
    currentToy = toyKey;
    document.querySelectorAll('.kinetic-toy-btn').forEach(b => {
        b.classList.remove('active', 'border-pink-500/60', 'bg-pink-950/40');
    });
    const btn = document.getElementById(`toy-${toyKey}`);
    if (btn) btn.classList.add('active', 'border-pink-500/60', 'bg-pink-950/40');

    const svg = document.getElementById('kineticToySvg');
    const text = document.getElementById('toyActionText');

    if (toyKey === 'butterfly') {
        svg.innerHTML = `
            <g id="butterflyToyGroup">
                <path id="bLeftWing" d="M160,90 C120,40 80,60 90,110 C95,130 140,120 160,90 Z" fill="#ec4899" stroke="#fbcfe8" stroke-width="2" style="transform-origin: 160px 90px; transition: transform 0.3s ease;" />
                <path id="bRightWing" d="M160,90 C200,40 240,60 230,110 C225,130 180,120 160,90 Z" fill="#ec4899" stroke="#fbcfe8" stroke-width="2" style="transform-origin: 160px 90px; transition: transform 0.3s ease;" />
                <line x1="160" y1="65" x2="160" y2="125" stroke="#831843" stroke-width="4" stroke-linecap="round" />
                <line x1="160" y1="65" x2="152" y2="52" stroke="#831843" stroke-width="2" />
                <line x1="160" y1="65" x2="168" y2="52" stroke="#831843" stroke-width="2" />
            </g>
        `;
        if (text) text.textContent = "Origami Butterfly: Pleated newspaper wings flap when pull tabs are tugged!";
    } else if (toyKey === 'dancer') {
        svg.innerHTML = `
            <g id="dancerToyGroup">
                <circle cx="160" cy="50" r="14" fill="#fb7185" />
                <line x1="160" y1="64" x2="160" y2="110" stroke="#f43f5e" stroke-width="4" />
                <!-- Skirt made of folded pleated newspaper fan -->
                <polygon id="dancerSkirt" points="160,90 120,135 200,135" fill="#f43f5e" stroke="#ffe4e6" stroke-width="2" style="transform-origin: 160px 90px; transition: transform 0.3s ease;" />
                <!-- Toothpick pivot stand -->
                <line x1="160" y1="135" x2="160" y2="165" stroke="#94a3b8" stroke-width="2.5" />
            </g>
        `;
        if (text) text.textContent = "Balancing Dancer: Low center of gravity keeps the paper figure pirouetting on a toothpick point!";
    } else {
        svg.innerHTML = `
            <g id="gliderToyGroup" style="transform-origin: 160px 90px; transition: transform 0.5s ease;">
                <polygon points="160,35 120,140 160,120 200,140" fill="#38bdf8" stroke="#bae6fd" stroke-width="2" />
                <line x1="160" y1="35" x2="160" y2="120" stroke="#0284c7" stroke-width="2.5" />
            </g>
        `;
        if (text) text.textContent = "Aerodynamic Glider: Sleek delta-wing creases generate upward aerodynamic lift!";
    }
};

window.animateToyMotion = function() {
    if (currentToy === 'butterfly') {
        const lWing = document.getElementById('bLeftWing');
        const rWing = document.getElementById('bRightWing');
        if (lWing && rWing) {
            lWing.style.transform = 'scaleX(0.4)';
            rWing.style.transform = 'scaleX(0.4)';
            setTimeout(() => {
                lWing.style.transform = 'scaleX(1)';
                rWing.style.transform = 'scaleX(1)';
            }, 300);
        }
    } else if (currentToy === 'dancer') {
        const skirt = document.getElementById('dancerSkirt');
        if (skirt) {
            skirt.style.transform = 'rotate(15deg)';
            setTimeout(() => {
                skirt.style.transform = 'rotate(-15deg)';
                setTimeout(() => skirt.style.transform = 'none', 200);
            }, 200);
        }
    } else {
        const glider = document.getElementById('gliderToyGroup');
        if (glider) {
            glider.style.transform = 'translateY(-30px) scale(1.1)';
            setTimeout(() => glider.style.transform = 'none', 600);
        }
    }
};

window.resetToyMotion = function() {
    window.setKineticToy(currentToy);
};

// SIM 16: Classroom Paper Conservation Tracker
let activePledges = new Set(['double', 'scrap', 'cloth']);

window.togglePledge = function(pledgeKey) {
    if (activePledges.has(pledgeKey)) {
        activePledges.delete(pledgeKey);
    } else {
        activePledges.add(pledgeKey);
    }

    const btn = document.getElementById(`pl-${pledgeKey}`);
    if (btn) {
        if (activePledges.has(pledgeKey)) {
            btn.classList.add('active', 'border-emerald-500/50', 'bg-emerald-950/40', 'text-emerald-200');
            btn.classList.remove('border-slate-700', 'bg-slate-800/40', 'text-slate-400');
        } else {
            btn.classList.remove('active', 'border-emerald-500/50', 'bg-emerald-950/40', 'text-emerald-200');
            btn.classList.add('border-slate-700', 'bg-slate-800/40', 'text-slate-400');
        }
    }

    const count = activePledges.size;
    const trees = count * 4;
    const water = count * 8000;
    const energy = count * 1600;

    const countText = document.getElementById('pledgeCountText');
    const treesEl = document.getElementById('treesSavedCount');
    const waterEl = document.getElementById('waterSavedCount');
    const energyEl = document.getElementById('energySavedCount');

    if (countText) countText.textContent = `${count} Active Habits`;
    if (treesEl) treesEl.textContent = `${trees} Trees`;
    if (waterEl) waterEl.textContent = `${water.toLocaleString()} Liters`;
    if (energyEl) energyEl.textContent = `${energy.toLocaleString()} kWh`;
};

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    loadVoices();
    showSlide(1);
});

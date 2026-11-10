// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 3 Mathematics - Chapter 2: Toy Joy
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
        osc1.stop(now + 0.38);
        osc2.stop(now + 0.38);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
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
        osc.frequency.setValueAtTime(261.63, now); // C4
        osc.frequency.exponentialRampToValueAtTime(196.00, now + 0.20); // G3

        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.28);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.28);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
    }
}

// Female blocker list to guarantee Pure Indian Male Voice
const femaleBlockList = [
    'female', 'woman', 'girl', 'zira', 'kavya', 'kalpana', 'veena',
    'siri', 'samantha', 'victoria', 'karen', 'moira', 'tessa', 'fiona',
    'helena', 'catherine', 'monica', 'paulina', 'lucia', 'sara', 'anna',
    'jenny', 'aria', 'google हिन्दी', 'google english (india)', 'neerja',
    'heera', 'priya', 'swara', 'ananya', 'aditi', 'pallavi', 'shreya',
    'vani', 'maya', 'pooja', 'sunita', 'geeta', 'seema', 'rekha'
];

function isIndianMaleVoice(v) {
    if (!v) return false;
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();

    for (let f of femaleBlockList) {
        if (name.includes(f)) return false;
    }

    const indianMaleKeywords = [
        'prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'mohan',
        'deepak', 'kumar', 'sanjay', 'ajay', 'vijay', 'amit',
        'rahul', 'rajesh', 'vikram', 'arun', 'manish', 'suresh',
        'ramesh', 'anil', 'sunil', 'ahp', 'cxx'
    ];
    for (let k of indianMaleKeywords) {
        if (name.includes(k)) return true;
    }

    if (lang.includes('en-in') || lang.includes('hi-in') || lang.includes('ta-in') || lang.includes('mr-in')) {
        return !name.includes('female');
    }

    return false;
}

function initSpeechEngine() {
    if (!synth) return;

    function populateVoices() {
        allVoices = synth.getVoices() || [];
        const voiceSelect = document.getElementById('voiceSelect');
        if (!voiceSelect) return;

        voiceSelect.innerHTML = '';
        let indianMaleVoices = [];
        let otherMaleVoices = [];

        allVoices.forEach((v, index) => {
            const nameLower = (v.name || '').toLowerCase();
            let isFemale = femaleBlockList.some(f => nameLower.includes(f));
            if (isFemale) return;

            if (isIndianMaleVoice(v)) {
                indianMaleVoices.push({ voice: v, index: index });
            } else if (nameLower.includes('male') || nameLower.includes('david') || nameLower.includes('george') || nameLower.includes('guy')) {
                otherMaleVoices.push({ voice: v, index: index });
            }
        });

        const sortedCandidates = [...indianMaleVoices, ...otherMaleVoices];

        if (sortedCandidates.length === 0) {
            allVoices.forEach((v, index) => {
                if (!femaleBlockList.some(f => (v.name || '').toLowerCase().includes(f))) {
                    sortedCandidates.push({ voice: v, index: index });
                }
            });
        }

        sortedCandidates.forEach(item => {
            const opt = document.createElement('option');
            opt.value = item.index;
            opt.textContent = `${item.voice.name} (${item.voice.lang})${isIndianMaleVoice(item.voice) ? ' 🇮🇳 Pure Indian Male' : ' 👨 Male'}`;
            voiceSelect.appendChild(opt);
        });

        if (sortedCandidates.length > 0) {
            selectedVoice = sortedCandidates[0].voice;
            voiceSelect.value = sortedCandidates[0].index;
        }
    }

    populateVoices();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoices;
    }
}

function onVoiceChange() {
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect || !allVoices) return;
    const idx = parseInt(voiceSelect.value);
    if (!isNaN(idx) && allVoices[idx]) {
        selectedVoice = allVoices[idx];
        if (isAudioPlaying) {
            speakLecture();
        }
    }
}

function toggleAudio() {
    if (isAudioPlaying) {
        stopSpeaking();
    } else {
        speakLecture();
    }
}

function stopSpeaking() {
    if (synth) {
        synth.cancel();
    }
    stopKeepAlive();
    isAudioPlaying = false;
    updateAudioButtonUI(false);
}

function startKeepAlive() {
    stopKeepAlive();
    speechKeepAliveTimer = setInterval(() => {
        if (synth && synth.speaking) {
            synth.pause();
            synth.resume();
        } else {
            stopKeepAlive();
        }
    }, 8000);
}

function stopKeepAlive() {
    if (speechKeepAliveTimer) {
        clearInterval(speechKeepAliveTimer);
        speechKeepAliveTimer = null;
    }
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    const icon = document.getElementById('audioPlayIcon');
    const label = document.getElementById('audioButtonText');
    if (!btn || !icon || !label) return;

    if (playing) {
        btn.classList.remove('bg-cyan-600', 'hover:bg-cyan-500');
        btn.classList.add('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        icon.textContent = '⏹️';
        label.textContent = 'Pause Lecture';
    } else {
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        btn.classList.add('bg-cyan-600', 'hover:bg-cyan-500');
        icon.textContent = '🔊';
        label.textContent = 'Teacher Sound Lecture';
    }
}

function speakLecture() {
    if (!synth) return;
    stopSpeaking();

    if (currentSlide > 16) {
        alert("Challenge questions are interactive quiz slides. Use the 🔊 speaker button on any question to hear it spoken aloud!");
        return;
    }

    const currentSlideData = window.slideCurriculumData ? window.slideCurriculumData.find(s => s.id === currentSlide) : null;
    if (!currentSlideData || !currentSlideData.speech) return;

    const speechText = currentSlideData.speech;
    currentUtterance = new SpeechSynthesisUtterance(speechText);

    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }
    currentUtterance.rate = 0.90;
    currentUtterance.pitch = 0.88;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioButtonUI(true);
        startKeepAlive();
    };

    currentUtterance.onend = () => {
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        stopKeepAlive();
    };

    currentUtterance.onerror = (e) => {
        console.warn("Speech synthesis error:", e);
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        stopKeepAlive();
    };

    synth.speak(currentUtterance);
}

window.speakText = function(text) {
    if (!synth || !text) return;
    synth.cancel();
    stopKeepAlive();

    const u = new SpeechSynthesisUtterance(text);
    if (selectedVoice) {
        u.voice = selectedVoice;
    }
    u.rate = 0.90;
    u.pitch = 0.88;
    synth.speak(u);
};

// Slide Navigation & Invariant Enforcement
function showSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    stopSpeaking();
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

    // STRICT INVARIANT FOR SLIDE 20: Next button hidden, Last slide notice shown
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

    const audioBtn = document.getElementById('audioLectureBtn');
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

// Checkpoint Answer Checking
function checkCheckpoint(slideId, cpIdx, selectedBtn, selectedOption, correctAns, explanation) {
    const parentContainer = selectedBtn.closest('.checkpoint-container');
    const buttons = parentContainer.querySelectorAll('.checkpoint-opt');
    const feedbackBox = parentContainer.querySelector('.checkpoint-feedback');

    buttons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800', 'border-slate-700');
        if (btn.dataset.option === correctAns) {
            btn.classList.add('bg-emerald-700', 'text-white', 'border-emerald-500');
        } else if (btn === selectedBtn) {
            btn.classList.add('bg-rose-700', 'text-white', 'border-rose-500');
        } else {
            btn.classList.add('opacity-50');
        }
    });

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOption === correctAns) {
            playSuccessChime();
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs">
                    <span class="font-bold">✅ Excellent!</span> ${explanation}
                </div>
            `;
        } else {
            playErrorChime();
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs">
                    <span class="font-bold">❌ Not quite!</span> Correct answer: <strong>${correctAns}</strong>.<br>${explanation}
                </div>
            `;
        }
    }
}

// Challenge Question Handler
function handleChallengeOption(qId, selectedBtn, selectedOption, correctAns, explanation) {
    const card = document.getElementById(`qcard-${qId}`);
    if (!card) return;

    const buttons = card.querySelectorAll('.q-opt-btn');
    const feedback = card.querySelector('.q-feedback-box');

    buttons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800');
        if (btn.dataset.option === correctAns) {
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        } else if (btn === selectedBtn) {
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    if (feedback) {
        feedback.classList.remove('hidden');
        if (selectedOption === correctAns) {
            playSuccessChime();
            feedback.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/70 border border-emerald-500/60 text-emerald-200 text-xs">
                    <span class="font-bold">🎉 Correct!</span> ${explanation}
                </div>
            `;
        } else {
            playErrorChime();
            feedback.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/70 border border-rose-500/60 text-rose-200 text-xs">
                    <span class="font-bold">❌ Incorrect!</span> Correct answer: <strong>${correctAns}</strong>.<br>${explanation}
                </div>
            `;
        }
    }
}

function toggleHint(qId) {
    const el = document.getElementById(`hint-${qId}`);
    if (el) el.classList.toggle('hidden');
}

function showSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body || !window.challengeQuestionsMap) return;

    const q = window.challengeQuestionsMap[qId];
    if (!q) return;

    body.innerHTML = `
        <div class="space-y-3 text-slate-200 text-xs sm:text-sm">
            <div class="font-bold text-amber-300 text-sm sm:text-base">${q.q}</div>
            <div class="p-2.5 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-emerald-300 font-semibold">
                Correct Answer: ${q.ans}
            </div>
            <div class="space-y-2 pt-2">
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold">Step 1:</span> ${q.solution_steps.step1}
                </div>
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-sky-400 font-bold">Step 2:</span> ${q.solution_steps.step2}
                </div>
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold">Step 3:</span> ${q.solution_steps.step3}
                </div>
            </div>
            <div class="pt-2 text-slate-400 text-xs border-t border-slate-800">
                <strong>Explanation:</strong> ${q.explanation}
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}


// =========================================================================
// 16 BESPOKE INTERACTIVE SIMULATOR IMPLEMENTATIONS
// =========================================================================

// Simulator 1: Box and Bottle Crafting
let craftCurrentItem = 'carton';
let craftFeatures = { ears: true, face: true };

const craftConfig = {
    carton: {
        shape: 'Rectangular Cuboid',
        animal: '🐶 Puppy Face Box',
        desc: 'A rectangular biscuit carton decorated with floppy felt ears, round button eyes, and a whiskered snout.',
        form: 'Cuboid',
        render: () => `
            <!-- Rectangular Biscuit Box Base -->
            <rect x="160" y="80" width="140" height="100" rx="4" fill="#d97706" stroke="#b45309" stroke-width="3"/>
            <polygon points="160,80 190,55 330,55 300,80" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
            <polygon points="300,80 330,55 330,155 300,180" fill="#92400e" stroke="#78350f" stroke-width="2"/>

            <!-- Animal Features -->
            ${craftFeatures.ears ? `
                <!-- Puppy Floppy Ears -->
                <path d="M 155,75 Q 120,95 140,140 Q 165,115 165,80 Z" fill="#78350f" stroke="#451a03" stroke-width="2"/>
                <path d="M 295,75 Q 330,95 310,140 Q 285,115 285,80 Z" fill="#78350f" stroke="#451a03" stroke-width="2"/>
            ` : ''}

            ${craftFeatures.face ? `
                <!-- Puppy Eyes and Snout -->
                <circle cx="205" cy="115" r="8" fill="#1e293b"/>
                <circle cx="203" cy="112" r="2.5" fill="#fff"/>
                <circle cx="255" cy="115" r="8" fill="#1e293b"/>
                <circle cx="253" cy="112" r="2.5" fill="#fff"/>
                <!-- Snout & Nose -->
                <ellipse cx="230" cy="140" rx="16" ry="12" fill="#fed7aa"/>
                <polygon points="230,132 222,140 238,140" fill="#451a03"/>
                <path d="M 230,140 L 230,146 M 224,146 Q 230,152 236,146" stroke="#451a03" stroke-width="2" fill="none"/>
            ` : ''}
        `
    },
    can: {
        shape: 'Cylinder',
        animal: '🐷 Piggy Tin Can',
        desc: 'A metallic tin can wrapped in pink felt with triangular pig ears and a two-hole snout.',
        form: 'Cylinder',
        render: () => `
            <!-- Upright Cylinder Can -->
            <rect x="180" y="80" width="100" height="100" rx="4" fill="#f472b6" stroke="#db2777" stroke-width="3"/>
            <ellipse cx="230" cy="80" rx="50" ry="16" fill="#fbcfe8" stroke="#db2777" stroke-width="2"/>
            <ellipse cx="230" cy="180" rx="50" ry="16" fill="#ec4899" stroke="#db2777" stroke-width="2"/>

            ${craftFeatures.ears ? `
                <!-- Piggy Pointy Ears -->
                <polygon points="185,75 170,40 205,65" fill="#f43f5e" stroke="#be123c" stroke-width="2"/>
                <polygon points="275,75 290,40 255,65" fill="#f43f5e" stroke="#be123c" stroke-width="2"/>
            ` : ''}

            ${craftFeatures.face ? `
                <!-- Piggy Eyes and Snout -->
                <circle cx="205" cy="110" r="5" fill="#1e293b"/>
                <circle cx="255" cy="110" r="5" fill="#1e293b"/>
                <!-- Big Round Snout -->
                <ellipse cx="230" cy="135" rx="18" ry="13" fill="#fda4af" stroke="#f43f5e" stroke-width="2"/>
                <ellipse cx="224" cy="135" rx="3" ry="5" fill="#9f1239"/>
                <ellipse cx="236" cy="135" rx="3" ry="5" fill="#9f1239"/>
            ` : ''}
        `
    },
    party_hat: {
        shape: 'Cone',
        animal: '🐦 Birdie Cone Hat',
        desc: 'A pointed party cone turned into a cheerful chick with feather crest and sharp orange beak.',
        form: 'Cone',
        render: () => `
            <!-- Cone Hat Base -->
            <polygon points="230,45 160,180 300,180" fill="#facc15" stroke="#eab308" stroke-width="3"/>
            <ellipse cx="230" cy="180" rx="70" ry="16" fill="#ca8a04" stroke="#eab308" stroke-width="2"/>

            ${craftFeatures.ears ? `
                <!-- Bird Feather Crest -->
                <path d="M 230,45 Q 210,15 230,10 Q 240,25 230,45" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
                <path d="M 230,45 Q 245,20 255,18 Q 245,35 230,45" fill="#f97316" stroke="#c2410c" stroke-width="2"/>
            ` : ''}

            ${craftFeatures.face ? `
                <!-- Bird Eyes & Beak -->
                <circle cx="210" cy="120" r="6" fill="#1e293b"/>
                <circle cx="250" cy="120" r="6" fill="#1e293b"/>
                <!-- Orange Pointed Beak -->
                <polygon points="230,130 215,145 245,145" fill="#f97316" stroke="#c2410c" stroke-width="2"/>
            ` : ''}
        `
    },
    cube_box: {
        shape: 'Cube',
        animal: '🐱 Kitten Chalk Box',
        desc: 'A square chalk box transformed into a playful cat with triangular ears and whiskers.',
        form: 'Cube',
        render: () => `
            <!-- Isometric Cube Base -->
            <polygon points="230,60 295,95 230,130 165,95" fill="#38bdf8" stroke="#0284c7" stroke-width="2.5"/>
            <polygon points="165,95 230,130 230,195 165,160" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
            <polygon points="230,130 295,95 295,160 230,195" fill="#0369a1" stroke="#075985" stroke-width="2.5"/>

            ${craftFeatures.ears ? `
                <!-- Cat Triangular Ears -->
                <polygon points="175,85 160,50 195,75" fill="#ec4899" stroke="#be185d" stroke-width="2"/>
                <polygon points="285,85 300,50 265,75" fill="#ec4899" stroke="#be185d" stroke-width="2"/>
            ` : ''}

            ${craftFeatures.face ? `
                <!-- Cat Eyes and Nose on Left Face -->
                <circle cx="185" cy="130" r="4.5" fill="#facc15"/>
                <circle cx="210" cy="130" r="4.5" fill="#facc15"/>
                <polygon points="197,140 193,145 201,145" fill="#f43f5e"/>
                <!-- Whiskers -->
                <line x1="175" y1="140" x2="160" y2="138" stroke="#fff" stroke-width="1.5"/>
                <line x1="175" y1="145" x2="160" y2="148" stroke="#fff" stroke-width="1.5"/>
                <line x1="220" y1="140" x2="235" y2="138" stroke="#fff" stroke-width="1.5"/>
                <line x1="220" y1="145" x2="235" y2="148" stroke="#fff" stroke-width="1.5"/>
            ` : ''}
        `
    }
};

function selectCraftItem(type) {
    craftCurrentItem = type;
    ['btnCraftCarton', 'btnCraftCan', 'btnCraftHat', 'btnCraftCube'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-amber-500', 'text-slate-950');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = {
        carton: 'btnCraftCarton',
        can: 'btnCraftCan',
        party_hat: 'btnCraftHat',
        cube_box: 'btnCraftCube'
    };
    const activeBtn = document.getElementById(activeMap[type]);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
        activeBtn.classList.add('bg-amber-500', 'text-slate-950');
    }

    renderCraftStage();
}

function toggleAnimalFeature(feat) {
    craftFeatures[feat] = !craftFeatures[feat];
    const btnMap = { ears: 'btnFeatureEars', face: 'btnFeatureFace' };
    const btn = document.getElementById(btnMap[feat]);
    if (btn) {
        const on = craftFeatures[feat];
        btn.textContent = feat === 'ears' ? `🐾 Ears: ${on ? 'ON' : 'OFF'}` : `👀 Face: ${on ? 'ON' : 'OFF'}`;
        if (on) {
            btn.className = "px-2 py-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 text-[11px] font-semibold text-center";
        } else {
            btn.className = "px-2 py-1.5 rounded-lg bg-slate-800 text-slate-500 border border-slate-700 text-[11px] font-semibold text-center";
        }
    }
    renderCraftStage();
}

function renderCraftStage() {
    const group = document.getElementById('craftDisplayGroup');
    const shapeNameEl = document.getElementById('craftShapeName');
    const animalTitleEl = document.getElementById('craftAnimalTitle');
    const shapeDescEl = document.getElementById('craftShapeDesc');
    const formBadgeEl = document.getElementById('craftFormBadge');

    const cfg = craftConfig[craftCurrentItem];
    if (group && cfg) {
        group.innerHTML = cfg.render();
    }
    if (shapeNameEl) shapeNameEl.textContent = cfg.shape;
    if (animalTitleEl) animalTitleEl.textContent = cfg.animal;
    if (shapeDescEl) shapeDescEl.textContent = cfg.desc;
    if (formBadgeEl) formBadgeEl.textContent = cfg.form;
}


// Simulator 2: Anatomy of 3D Cube
function highlightCubePart(part) {
    ['btnAnatomyFaces', 'btnAnatomyEdges', 'btnAnatomyVertices'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-emerald-600', 'bg-sky-600', 'bg-amber-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const faceTop = document.getElementById('cubeFaceTop');
    const faceLeft = document.getElementById('cubeFaceLeft');
    const faceRight = document.getElementById('cubeFaceRight');
    const edgesGroup = document.getElementById('cubeEdgesGroup');
    const verticesGroup = document.getElementById('cubeVerticesGroup');
    const header = document.getElementById('anatomyDetailHeader');
    const text = document.getElementById('anatomyDetailText');

    if (part === 'faces') {
        const btn = document.getElementById('btnAnatomyFaces');
        if (btn) btn.className = "px-2.5 py-1.5 rounded-xl bg-emerald-600 text-white font-bold text-xs transition shadow";
        if (faceTop) faceTop.setAttribute('opacity', '0.95');
        if (faceLeft) faceLeft.setAttribute('opacity', '0.95');
        if (faceRight) faceRight.setAttribute('opacity', '0.95');
        if (edgesGroup) edgesGroup.setAttribute('opacity', '0.15');
        if (verticesGroup) verticesGroup.setAttribute('opacity', '0.1');

        if (header) header.textContent = "Faces Highlighted (6 Square Faces)";
        if (text) text.innerHTML = "A cube has <span class='text-emerald-400 font-bold'>6 flat square faces</span>. 3 are directly visible from this angle, while 3 rest on the opposite sides.";
    } else if (part === 'edges') {
        const btn = document.getElementById('btnAnatomyEdges');
        if (btn) btn.className = "px-2.5 py-1.5 rounded-xl bg-sky-600 text-white font-bold text-xs transition shadow";
        if (faceTop) faceTop.setAttribute('opacity', '0.4');
        if (faceLeft) faceLeft.setAttribute('opacity', '0.4');
        if (faceRight) faceRight.setAttribute('opacity', '0.4');
        if (edgesGroup) edgesGroup.setAttribute('opacity', '1');
        if (verticesGroup) verticesGroup.setAttribute('opacity', '0.1');

        if (header) header.textContent = "Edges Highlighted (12 Straight Edges)";
        if (text) text.innerHTML = "A cube has <span class='text-sky-400 font-bold'>12 straight edges</span> where faces intersect: 4 on the top, 4 vertical pillars, and 4 on the bottom!";
    } else if (part === 'vertices') {
        const btn = document.getElementById('btnAnatomyVertices');
        if (btn) btn.className = "px-2.5 py-1.5 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow";
        if (faceTop) faceTop.setAttribute('opacity', '0.3');
        if (faceLeft) faceLeft.setAttribute('opacity', '0.3');
        if (faceRight) faceRight.setAttribute('opacity', '0.3');
        if (edgesGroup) edgesGroup.setAttribute('opacity', '0.4');
        if (verticesGroup) verticesGroup.setAttribute('opacity', '1');

        if (header) header.textContent = "Corners Highlighted (8 Sharp Vertices)";
        if (text) text.innerHTML = "A cube has <span class='text-amber-400 font-bold'>8 sharp corners</span> (vertices) where three straight edges meet at right angles.";
    }
}


// Simulator 3: Space Rocket Geometric Assembly Dock
let rocketParts = { cuboid: false, cube: false, cylinder: false, cone: false };

function toggleRocketPart(part) {
    rocketParts[part] = !rocketParts[part];
    const groupMap = {
        cuboid: 'rocketTierCuboid',
        cube: 'rocketTierCube',
        cylinder: 'rocketTierCylinder',
        cone: 'rocketTierCone'
    };
    const badgeMap = {
        cuboid: 'badgePartCuboid',
        cube: 'badgePartCube',
        cylinder: 'badgePartCylinder',
        cone: 'badgePartCone'
    };

    const g = document.getElementById(groupMap[part]);
    const b = document.getElementById(badgeMap[part]);

    if (g) {
        g.setAttribute('opacity', rocketParts[part] ? '1' : '0.2');
    }
    if (b) {
        if (rocketParts[part]) {
            b.textContent = 'Installed';
            b.className = 'text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold';
        } else {
            b.textContent = 'Pending';
            b.className = 'text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400';
        }
    }

    const count = Object.values(rocketParts).filter(Boolean).length;
    const countEl = document.getElementById('rocketInstalledCount');
    if (countEl) countEl.textContent = `${count} / 4 Parts`;

    if (count === 4) {
        playSuccessChime();
    }
}

function resetRocketAssembly() {
    rocketParts = { cuboid: false, cube: false, cylinder: false, cone: false };
    ['cuboid', 'cube', 'cylinder', 'cone'].forEach(part => {
        const groupMap = { cuboid: 'rocketTierCuboid', cube: 'rocketTierCube', cylinder: 'rocketTierCylinder', cone: 'rocketTierCone' };
        const badgeMap = { cuboid: 'badgePartCuboid', cube: 'badgePartCube', cylinder: 'badgePartCylinder', cone: 'badgePartCone' };
        const g = document.getElementById(groupMap[part]);
        const b = document.getElementById(badgeMap[part]);
        if (g) g.setAttribute('opacity', '0.2');
        if (b) {
            b.textContent = 'Pending';
            b.className = 'text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400';
        }
    });
    const countEl = document.getElementById('rocketInstalledCount');
    if (countEl) countEl.textContent = '0 / 4 Parts';
}


// Simulator 4: Toy Locomotive Component Inspector
const trainPartsData = {
    boiler: {
        name: 'Horizontal Steam Boiler',
        shape: 'Cylinder',
        qty: '1',
        desc: 'Forms the long red pressurized tank holding steam, resting horizontally along the chassis.'
    },
    stack: {
        name: 'Puffing Smokestack Chimney',
        shape: 'Cone',
        qty: '1',
        desc: 'Perched atop the boiler, this yellow cone releases steam and smoke into the air.'
    },
    cabin: {
        name: "Sheltered Driver's Cabin",
        shape: 'Cuboid',
        qty: '1',
        desc: 'A tall grey box with rectangular window cutouts where the train driver steers.'
    },
    tender: {
        name: 'Solid Coal Storage Tender',
        shape: 'Cube',
        qty: '1',
        desc: 'A compact blue cube box hitched to the rear to hold fuel coals for the furnace.'
    },
    wheels: {
        name: 'Rotating Locomotive Wheels',
        shape: 'Flat Cylinders',
        qty: '6',
        desc: 'Six flat circular discs with depth that rotate smoothly along the railway tracks.'
    }
};

function selectTrainPart(part) {
    const data = trainPartsData[part];
    if (!data) return;

    const nameEl = document.getElementById('trainPartName');
    const shapeEl = document.getElementById('trainPartShape');
    const qtyEl = document.getElementById('trainPartQty');
    const descEl = document.getElementById('trainPartDesc');
    const badgeEl = document.getElementById('trainPartsInspectedBadge');

    if (nameEl) nameEl.textContent = data.name;
    if (shapeEl) shapeEl.textContent = data.shape;
    if (qtyEl) qtyEl.textContent = data.qty;
    if (descEl) descEl.textContent = data.desc;
    if (badgeEl) badgeEl.textContent = `Inspecting: ${data.shape}`;

    playSuccessChime();
}


// Simulator 5: Dimension Morphing Lab (Cube vs Cuboid)
function updateMorphBox() {
    const slLen = document.getElementById('sliderLen');
    const slWid = document.getElementById('sliderWid');
    const slHei = document.getElementById('sliderHei');
    if (!slLen || !slWid || !slHei) return;

    const l = parseInt(slLen.value);
    const w = parseInt(slWid.value);
    const h = parseInt(slHei.value);

    const lblLen = document.getElementById('labelLen');
    const lblWid = document.getElementById('labelWid');
    const lblHei = document.getElementById('labelHei');
    if (lblLen) lblLen.textContent = `${l} px`;
    if (lblWid) lblWid.textContent = `${w} px`;
    if (lblHei) lblHei.textContent = `${h} px`;

    // Render isometric 3D box
    const group = document.getElementById('morphBoxGroup');
    const cx = 190;
    const cy = 140;

    const dx1 = -l * 0.7;
    const dy1 = l * 0.35;
    const dx2 = w * 0.7;
    const dy2 = w * 0.35;

    const p0 = [cx, cy];
    const p1 = [cx + dx1, cy + dy1];
    const p2 = [cx + dx1 + dx2, cy + dy1 + dy2];
    const p3 = [cx + dx2, cy + dy2];

    const topPoints = `${p0[0]},${p0[1] - h} ${p1[0]},${p1[1] - h} ${p2[0]},${p2[1] - h} ${p3[0]},${p3[1] - h}`;
    const leftPoints = `${p1[0]},${p1[1] - h} ${p2[0]},${p2[1] - h} ${p2[0]},${p2[1]} ${p1[0]},${p1[1]}`;
    const rightPoints = `${p2[0]},${p2[1] - h} ${p3[0]},${p3[1] - h} ${p3[0]},${p3[1]} ${p2[0]},${p2[1]}`;

    const isCube = (Math.abs(l - w) <= 4 && Math.abs(w - h) <= 4);

    if (group) {
        group.innerHTML = `
            <polygon points="${topPoints}" fill="${isCube ? '#10b981' : '#0ea5e9'}" stroke="#fff" stroke-width="2"/>
            <polygon points="${leftPoints}" fill="${isCube ? '#059669' : '#0284c7'}" stroke="#fff" stroke-width="2"/>
            <polygon points="${rightPoints}" fill="${isCube ? '#047857' : '#0369a1'}" stroke="#fff" stroke-width="2"/>
        `;
    }

    const badge = document.getElementById('morphClassificationBadge');
    const note = document.getElementById('morphStatusSummary');

    if (isCube) {
        if (badge) {
            badge.textContent = "Cube (Special Cuboid!)";
            badge.className = "text-xs px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold font-mono";
        }
        if (note) {
            note.innerHTML = "✨ <strong class='text-emerald-300'>Perfect Cube!</strong> Length = Width = Height! All 6 faces are equal squares. Every cube is a special cuboid!";
        }
    } else {
        if (badge) {
            badge.textContent = "General Cuboid";
            badge.className = "text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold font-mono";
        }
        if (note) {
            note.innerHTML = "When length, width, and height are unequal, faces are rectangular (cuboid). Equalize all three to form a cube!";
        }
    }
}

function makeDimensionsEqual() {
    const slLen = document.getElementById('sliderLen');
    const slWid = document.getElementById('sliderWid');
    const slHei = document.getElementById('sliderHei');
    if (slLen && slWid && slHei) {
        slLen.value = 90;
        slWid.value = 90;
        slHei.value = 90;
        updateMorphBox();
        playSuccessChime();
    }
}


// Simulator 6: Inclined Ramp Motion Laboratory
let currentRampShape = 'sphere';

const rampShapeData = {
    sphere: {
        name: 'Sphere (Cricket Ball)',
        motion: 'Rolling',
        contact: 'Continuous Curved',
        desc: 'A sphere contacts the incline at a single point and rotates continuously down the ramp without sliding.',
        render: () => `<circle cx="0" cy="0" r="16" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>`
    },
    cube: {
        name: 'Cube (Wooden Block)',
        motion: 'Sliding',
        contact: 'Flat Square Face',
        desc: 'A cube rests flat against the ramp; its flat face slides smoothly down without tumbling.',
        render: () => `<rect x="-15" y="-15" width="30" height="30" rx="2" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>`
    },
    cylinder_curved: {
        name: 'Cylinder on Curved Side',
        motion: 'Rolling',
        contact: 'Curved Lateral Surface',
        desc: 'Placed on its rounded flank, the cylinder rolls rapidly like a wheel or rolling pin.',
        render: () => `
            <rect x="-18" y="-12" width="36" height="24" rx="4" fill="#10b981" stroke="#34d399" stroke-width="2"/>
            <ellipse cx="-18" cy="0" rx="4" ry="12" fill="#059669"/>
        `
    },
    cylinder_flat: {
        name: 'Cylinder on Flat Base',
        motion: 'Sliding',
        contact: 'Flat Circular Face',
        desc: 'Placed upright on its flat circular base, the cylinder slides like a hockey puck without rolling.',
        render: () => `
            <ellipse cx="0" cy="0" rx="18" ry="8" fill="#10b981" stroke="#34d399" stroke-width="2"/>
            <rect x="-18" y="-16" width="36" height="16" fill="#059669" opacity="0.6"/>
        `
    }
};

function selectRampShape(shape) {
    currentRampShape = shape;
    ['btnRampSphere', 'btnRampCube', 'btnRampCylSide', 'btnRampCylFlat'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-amber-500', 'text-slate-950');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = {
        sphere: 'btnRampSphere',
        cube: 'btnRampCube',
        cylinder_curved: 'btnRampCylSide',
        cylinder_flat: 'btnRampCylFlat'
    };
    const activeBtn = document.getElementById(activeMap[shape]);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
        activeBtn.classList.add('bg-amber-500', 'text-slate-950');
    }

    const data = rampShapeData[shape];
    const obj = document.getElementById('rampMovingObject');
    if (obj) {
        obj.setAttribute('transform', 'translate(65, 55)');
        obj.innerHTML = data.render();
    }

    const mType = document.getElementById('rampMotionType');
    const cSurf = document.getElementById('rampContactSurface');
    const exp = document.getElementById('rampExplanation');

    if (mType) mType.textContent = data.motion;
    if (cSurf) cSurf.textContent = data.contact;
    if (exp) exp.textContent = data.desc;
}

function releaseRampObject() {
    const obj = document.getElementById('rampMovingObject');
    if (!obj) return;

    let progress = 0;
    const startX = 65, startY = 55;
    const rampEndX = 310, rampEndY = 175;
    const flatEndX = 410, flatEndY = 175;

    playSuccessChime();

    const interval = setInterval(() => {
        progress += 0.04;
        if (progress <= 0.7) {
            const t = progress / 0.7;
            const curX = startX + (rampEndX - startX) * t;
            const curY = startY + (rampEndY - startY) * t;
            const rot = (currentRampShape.includes('sphere') || currentRampShape === 'cylinder_curved') ? t * 720 : 25;
            obj.setAttribute('transform', `translate(${curX}, ${curY}) rotate(${rot})`);
        } else if (progress <= 1.0) {
            const t = (progress - 0.7) / 0.3;
            const curX = rampEndX + (flatEndX - rampEndX) * t;
            const curY = flatEndY;
            const rot = (currentRampShape.includes('sphere') || currentRampShape === 'cylinder_curved') ? (720 + t * 360) : 0;
            obj.setAttribute('transform', `translate(${curX}, ${curY}) rotate(${rot})`);
        } else {
            clearInterval(interval);
            setTimeout(() => {
                obj.setAttribute('transform', 'translate(65, 55)');
            }, 1200);
        }
    }, 20);
}


// Simulator 7: Shape Mystery Descriptions (Collaborative Game)
const mysteryDesigns = [
    {
        target: ['cuboid', 'cylinder', 'cone'],
        instruction: "1. Lay a rectangular cuboid flat as base. 2. Place an upright cylinder in center. 3. Crown top with a pointed cone."
    },
    {
        target: ['cuboid', 'cuboid', 'cylinder'],
        instruction: "1. Lay a broad cuboid foundation. 2. Stack a second matching cuboid. 3. Finish with a rolling cylinder on top."
    },
    {
        target: ['cylinder', 'cuboid', 'cone'],
        instruction: "1. Stand a cylinder upright as pillar. 2. Balance a horizontal cuboid beam on top. 3. Cap with a sharp cone apex."
    }
];

let currentMysteryGoalIndex = 0;
let studentStack = [];

function generateNewMysteryGoal() {
    currentMysteryGoalIndex = (currentMysteryGoalIndex + 1) % mysteryDesigns.length;
    studentStack = [];
    renderArchitectStack();
    const instEl = document.getElementById('architectInstruction');
    if (instEl) {
        instEl.textContent = `"${mysteryDesigns[currentMysteryGoalIndex].instruction}"`;
    }
}

function addArchitectShape(shape) {
    if (studentStack.length >= 3) {
        alert("Stack is full! Maximum 3 tiers. Click 'Clear Stack' to rebuild.");
        return;
    }
    studentStack.push(shape);
    renderArchitectStack();

    if (studentStack.length === 3) {
        const goal = mysteryDesigns[currentMysteryGoalIndex].target;
        const isMatch = studentStack.every((s, i) => s === goal[i]);
        if (isMatch) {
            playSuccessChime();
            const statusEl = document.getElementById('architectMatchStatus');
            if (statusEl) {
                statusEl.innerHTML = "<span class='text-emerald-400 font-bold'>🎉 Flawless Match!</span>";
            }
        } else {
            playErrorChime();
            const statusEl = document.getElementById('architectMatchStatus');
            if (statusEl) {
                statusEl.innerHTML = "<span class='text-rose-400 font-bold'>❌ Shape order mismatch!</span>";
            }
        }
    }
}

function clearArchitectStack() {
    studentStack = [];
    renderArchitectStack();
}

function renderArchitectStack() {
    const t1 = document.getElementById('placedTier1');
    const t2 = document.getElementById('placedTier2');
    const t3 = document.getElementById('placedTier3');
    const statusEl = document.getElementById('architectMatchStatus');

    if (t1) t1.innerHTML = '';
    if (t2) t2.innerHTML = '';
    if (t3) t3.innerHTML = '';

    const tierGroups = [t1, t2, t3];
    const tierOffsetsY = [160, 115, 70];

    studentStack.forEach((shape, idx) => {
        const g = tierGroups[idx];
        const y = tierOffsetsY[idx];
        if (!g) return;

        if (shape === 'cuboid') {
            g.innerHTML = `<rect x="130" y="${y}" width="100" height="35" rx="3" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>`;
        } else if (shape === 'cylinder') {
            g.innerHTML = `
                <rect x="155" y="${y}" width="50" height="40" rx="3" fill="#06b6d4" stroke="#67e8f9" stroke-width="2"/>
                <ellipse cx="180" cy="${y}" rx="25" ry="6" fill="#0891b2"/>
            `;
        } else if (shape === 'cone') {
            g.innerHTML = `<polygon points="180,${y - 15} 155,${y + 35} 205,${y + 35}" fill="#f59e0b" stroke="#fcd34d" stroke-width="2"/>`;
        }
    });

    if (statusEl && studentStack.length < 3) {
        statusEl.textContent = `Stack Height: ${studentStack.length} / 3`;
    }
}


// Simulator 8: Classroom Shape Hunt
let safariFoundItems = new Set();

function clickSafariItem(item) {
    if (safariFoundItems.has(item)) return;
    safariFoundItems.add(item);

    playSuccessChime();

    const rowMap = {
        globe: 'tallyRowGlobe',
        chalk_box: 'tallyRowChalk',
        bottle: 'tallyRowBottle',
        hat: 'tallyRowHat',
        cube: 'tallyRowCube'
    };

    const row = document.getElementById(rowMap[item]);
    if (row) {
        row.classList.remove('opacity-50');
        row.classList.add('bg-emerald-950/40', 'border-emerald-500/50');
    }

    const countEl = document.getElementById('safariFoundCount');
    if (countEl) {
        countEl.textContent = `Found: ${safariFoundItems.size} / 5 Shapes`;
    }
}


// Simulator 9: Sorting Solid Shapes (Property Bins)
let selectedSorterShape = null;

const sorterData = {
    sphere: { name: 'Sphere', correctBin: 'roll' },
    cube: { name: 'Cube', correctBin: 'slide' },
    cuboid: { name: 'Cuboid', correctBin: 'slide' },
    cylinder: { name: 'Cylinder', correctBin: 'both' },
    cone: { name: 'Cone', correctBin: 'both' }
};

function selectSorterShape(shape) {
    selectedSorterShape = shape;
    ['poolSphere', 'poolCube', 'poolCuboid', 'poolCylinder', 'poolCone'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) btn.classList.remove('ring-2', 'ring-amber-400');
    });

    const activeMap = {
        sphere: 'poolSphere',
        cube: 'poolCube',
        cuboid: 'poolCuboid',
        cylinder: 'poolCylinder',
        cone: 'poolCone'
    };
    const activeBtn = document.getElementById(activeMap[shape]);
    if (activeBtn) activeBtn.classList.add('ring-2', 'ring-amber-400');
}

function dropIntoBin(binType) {
    if (!selectedSorterShape) {
        alert("First select a solid shape from the pool above!");
        return;
    }

    const data = sorterData[selectedSorterShape];
    if (data.correctBin === binType) {
        playSuccessChime();
        const binContentMap = {
            roll: 'binRollContent',
            slide: 'binSlideContent',
            both: 'binBothContent'
        };
        const binEl = document.getElementById(binContentMap[binType]);
        if (binEl) {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'text-[11px] p-1.5 rounded bg-slate-900 border border-emerald-500/40 text-emerald-300 font-semibold flex items-center justify-between';
            itemDiv.innerHTML = `<span>✅ ${data.name}</span> <span class='text-[10px] text-slate-500'>Sorted</span>`;
            binEl.appendChild(itemDiv);
        }

        const poolBtnMap = {
            sphere: 'poolSphere',
            cube: 'poolCube',
            cuboid: 'poolCuboid',
            cylinder: 'poolCylinder',
            cone: 'poolCone'
        };
        const poolBtn = document.getElementById(poolBtnMap[selectedSorterShape]);
        if (poolBtn) {
            poolBtn.disabled = true;
            poolBtn.classList.add('opacity-30', 'line-through');
        }

        selectedSorterShape = null;
    } else {
        playErrorChime();
        alert(`Try again! A ${data.name} does not belong in the '${binType}' bin. Consider its flat vs curved surfaces!`);
    }
}

function resetMotionSorter() {
    ['binRollContent', 'binSlideContent', 'binBothContent'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerHTML = '';
    });
    ['poolSphere', 'poolCube', 'poolCuboid', 'poolCylinder', 'poolCone'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.disabled = false;
            btn.classList.remove('opacity-30', 'line-through', 'ring-2', 'ring-amber-400');
        }
    });
    selectedSorterShape = null;
}


// Simulator 10: Clay Ball & Matchstick Skeleton Workbench
function selectSkeletonShape(shape) {
    ['btnSkelCube', 'btnSkelCuboid', 'btnSkelPyramid'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-amber-500', 'text-slate-950');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = { cube: 'btnSkelCube', cuboid: 'btnSkelCuboid', pyramid: 'btnSkelPyramid' };
    const activeBtn = document.getElementById(activeMap[shape]);
    if (activeBtn) {
        activeBtn.classList.remove('bg-slate-800', 'text-slate-300');
        activeBtn.classList.add('bg-amber-500', 'text-slate-950');
    }

    const titleEl = document.getElementById('skeletonShapeTitle');
    const clayEl = document.getElementById('countClayBalls');
    const stickEl = document.getElementById('countMatchsticks');
    const descEl = document.getElementById('skeletonAssemblyDesc');
    const group = document.getElementById('skeletonDrawingGroup');

    playSuccessChime();

    if (shape === 'cube') {
        if (titleEl) titleEl.textContent = 'Cube Skeleton Frame';
        if (clayEl) clayEl.textContent = '8';
        if (stickEl) stickEl.textContent = '12';
        if (descEl) descEl.textContent = '4 sticks form the square base, 4 vertical sticks form pillars, and 4 sticks cap the top square.';
        if (group) {
            group.innerHTML = `
                <!-- 12 Sticks -->
                <g stroke="#38bdf8" stroke-width="4" stroke-linecap="round">
                    <line x1="140" y1="80" x2="230" y2="40"/>
                    <line x1="230" y1="40" x2="310" y2="80"/>
                    <line x1="310" y1="80" x2="220" y2="120"/>
                    <line x1="220" y1="120" x2="140" y2="80"/>

                    <line x1="140" y1="80" x2="140" y2="155"/>
                    <line x1="230" y1="40" x2="230" y2="115" stroke-dasharray="4,4"/>
                    <line x1="310" y1="80" x2="310" y2="155"/>
                    <line x1="220" y1="120" x2="220" y2="195"/>

                    <line x1="140" y1="155" x2="230" y2="115" stroke-dasharray="4,4"/>
                    <line x1="230" y1="115" x2="310" y2="155" stroke-dasharray="4,4"/>
                    <line x1="310" y1="155" x2="220" y2="195"/>
                    <line x1="220" y1="195" x2="140" y2="155"/>
                </g>
                <!-- 8 Clay Balls -->
                <g fill="#f59e0b" stroke="#78350f" stroke-width="2">
                    <circle cx="140" cy="80" r="7"/>
                    <circle cx="230" cy="40" r="7"/>
                    <circle cx="310" cy="80" r="7"/>
                    <circle cx="220" cy="120" r="7"/>
                    <circle cx="140" cy="155" r="7"/>
                    <circle cx="230" cy="115" r="6" opacity="0.7"/>
                    <circle cx="310" cy="155" r="7"/>
                    <circle cx="220" cy="195" r="7"/>
                </g>
            `;
        }
    } else if (shape === 'cuboid') {
        if (titleEl) titleEl.textContent = 'Cuboid Skeleton Frame';
        if (clayEl) clayEl.textContent = '8';
        if (stickEl) stickEl.textContent = '12';
        if (descEl) descEl.textContent = 'Requires 3 sets of 4 equal sticks (4 for length, 4 for width, 4 for height) meeting at 8 clay vertices.';
        if (group) {
            group.innerHTML = `
                <!-- 12 Elongated Sticks -->
                <g stroke="#38bdf8" stroke-width="4" stroke-linecap="round">
                    <line x1="110" y1="90" x2="260" y2="45"/>
                    <line x1="260" y1="45" x2="330" y2="80"/>
                    <line x1="330" y1="80" x2="180" y2="125"/>
                    <line x1="180" y1="125" x2="110" y2="90"/>

                    <line x1="110" y1="90" x2="110" y2="155"/>
                    <line x1="260" y1="45" x2="260" y2="110" stroke-dasharray="4,4"/>
                    <line x1="330" y1="80" x2="330" y2="145"/>
                    <line x1="180" y1="125" x2="180" y2="190"/>

                    <line x1="110" y1="155" x2="260" y2="110" stroke-dasharray="4,4"/>
                    <line x1="260" y1="110" x2="330" y2="145" stroke-dasharray="4,4"/>
                    <line x1="330" y1="145" x2="180" y2="190"/>
                    <line x1="180" y1="190" x2="110" y2="155"/>
                </g>
                <g fill="#f59e0b" stroke="#78350f" stroke-width="2">
                    <circle cx="110" cy="90" r="7"/>
                    <circle cx="260" cy="45" r="7"/>
                    <circle cx="330" cy="80" r="7"/>
                    <circle cx="180" cy="125" r="7"/>
                    <circle cx="110" cy="155" r="7"/>
                    <circle cx="260" cy="110" r="6" opacity="0.7"/>
                    <circle cx="330" cy="145" r="7"/>
                    <circle cx="180" cy="190" r="7"/>
                </g>
            `;
        }
    } else if (shape === 'pyramid') {
        if (titleEl) titleEl.textContent = 'Square Pyramid Skeleton';
        if (clayEl) clayEl.textContent = '5';
        if (stickEl) stickEl.textContent = '8';
        if (descEl) descEl.textContent = '4 sticks form the square base, and 4 slant sticks rise from corners to meet at 1 top apex clay ball.';
        if (group) {
            group.innerHTML = `
                <!-- 8 Sticks -->
                <g stroke="#38bdf8" stroke-width="4" stroke-linecap="round">
                    <line x1="130" y1="160" x2="220" y2="130" stroke-dasharray="4,4"/>
                    <line x1="220" y1="130" x2="290" y2="160" stroke-dasharray="4,4"/>
                    <line x1="290" y1="160" x2="200" y2="190"/>
                    <line x1="200" y1="190" x2="130" y2="160"/>

                    <line x1="130" y1="160" x2="210" y2="45"/>
                    <line x1="220" y1="130" x2="210" y2="45" stroke-dasharray="4,4"/>
                    <line x1="290" y1="160" x2="210" y2="45"/>
                    <line x1="200" y1="190" x2="210" y2="45"/>
                </g>
                <!-- 5 Clay Balls -->
                <g fill="#f59e0b" stroke="#78350f" stroke-width="2">
                    <circle cx="210" cy="45" r="8"/> <!-- Apex -->
                    <circle cx="130" cy="160" r="7"/>
                    <circle cx="220" cy="130" r="6" opacity="0.7"/>
                    <circle cx="290" cy="160" r="7"/>
                    <circle cx="200" cy="190" r="7"/>
                </g>
            `;
        }
    }
}


// Simulator 11: Toy Joy Geometric Board Game
let boardTokenPos = 1;

const boardTilesData = [
    { num: 1, title: 'Toy Workshop Gate', desc: 'Starting line of our geometric voyage.' },
    { num: 2, title: 'Cylinder Can', desc: '2 flat circular faces and 1 curved surface.' },
    { num: 3, title: 'Cube Building Block', desc: '6 equal square faces.' },
    { num: 4, title: 'Edge Bridge', desc: 'Count 12 edges on a storage box!' },
    { num: 5, title: 'Rolling Sphere Meadow', desc: 'Zero flat faces means non-stop rolling!' },
    { num: 6, title: 'Birthday Cone Hat', desc: '1 circular base and 1 pointed apex.' },
    { num: 7, title: 'Matchbox Cuboid', desc: 'Length, width, and height form 6 rectangular faces.' },
    { num: 8, title: 'Curved Slip', desc: 'Spheres cannot stack stably; slide back 1 space!' },
    { num: 9, title: 'Dice Dot Checkpoint', desc: 'Opposite faces always sum to 7!' },
    { num: 10, title: 'Twin Cubes Junction', desc: 'Joining two cubes creates a rectangular cuboid.' },
    { num: 11, title: 'Clay Corner Station', desc: '8 clay balls form the vertices of a cube.' },
    { num: 12, title: 'Sliding Ramp', desc: 'Flat faces slide smoothly on inclines.' },
    { num: 13, title: 'Boiler Locomotive', desc: 'Identify the horizontal cylinder boiler.' },
    { num: 14, title: 'Rocket Launch Silo', desc: 'Assemble nose cone on cylinder fuselage.' },
    { num: 15, title: 'Tri-Cube Corner Block', desc: '3 cubes in an L-shape form a triomino solid.' },
    { num: 16, title: 'Hidden Cube Staircase', desc: 'Deduce foundation blocks under upper steps.' },
    { num: 17, title: 'Special Cuboid Secret', desc: 'Every cube is a special type of cuboid!' },
    { num: 18, title: 'Mechanical Sorter', desc: 'Sort cylinders and cones into both roll & slide.' },
    { num: 19, title: 'Master Matrix Gate', desc: 'Review faces, edges, and corners before the finish.' },
    { num: 20, title: 'Toy Joy Crown 🏆', desc: 'Congratulations! You have mastered 3D solid geometry!' }
];

function initBoardTiles() {
    const group = document.getElementById('boardTilesGroup');
    if (!group) return;

    let html = '';
    // 20 tiles in 4 rows of 5
    for (let i = 0; i < 20; i++) {
        const row = Math.floor(i / 5);
        const col = (row % 2 === 0) ? (i % 5) : (4 - (i % 5));
        const x = 35 + col * 80;
        const y = 30 + row * 45;

        html += `
            <rect x="${x - 30}" y="${y - 18}" width="60" height="36" rx="6" fill="#1e293b" stroke="#334155" stroke-width="2"/>
            <text x="${x}" y="${y + 4}" fill="#f1f5f9" font-size="11" font-weight="bold" font-family="monospace" text-anchor="middle">${i + 1}</text>
        `;
    }
    group.innerHTML = html;
}

function rollGameBoardDie() {
    const roll = Math.floor(Math.random() * 6) + 1;
    const resEl = document.getElementById('boardDieRollResult');
    if (resEl) resEl.textContent = `🎲 Rolled a ${roll}!`;

    boardTokenPos += roll;
    if (boardTokenPos > 20) boardTokenPos = 20;

    // Special tile 8 trap
    if (boardTokenPos === 8) {
        boardTokenPos = 7;
        alert("Curved Slip! A sphere rolled off the stack. Moved back to tile 7!");
    }

    const tData = boardTilesData[boardTokenPos - 1];
    const curNum = document.getElementById('boardCurrentTileNum');
    const curTitle = document.getElementById('boardTileTitle');
    const curText = document.getElementById('boardTileText');

    if (curNum) curNum.textContent = `Tile ${tData.num}`;
    if (curTitle) curTitle.textContent = tData.title;
    if (curText) curText.textContent = tData.desc;

    // Move token SVG
    const token = document.getElementById('playerTokenGroup');
    if (token) {
        const i = boardTokenPos - 1;
        const row = Math.floor(i / 5);
        const col = (row % 2 === 0) ? (i % 5) : (4 - (i % 5));
        const x = 35 + col * 80;
        const y = 30 + row * 45;
        token.setAttribute('transform', `translate(${x}, ${y})`);
    }

    playSuccessChime();
}


// Simulator 12: Standard Dice Opposite Sum Explorer
const diceDotLayouts = {
    1: [[55, 55]],
    2: [[30, 30], [80, 80]],
    3: [[30, 30], [55, 55], [80, 80]],
    4: [[30, 30], [80, 30], [30, 80], [80, 80]],
    5: [[30, 30], [80, 30], [55, 55], [30, 80], [80, 80]],
    6: [[30, 25], [80, 25], [30, 55], [80, 55], [30, 85], [80, 85]]
};

function selectDieFace(num) {
    for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`btnDieFace${i}`);
        if (btn) {
            if (i === num) {
                btn.className = "px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs";
            } else {
                btn.className = "px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs";
            }
        }
    }

    const oppNum = 7 - num;

    const gFront = document.getElementById('diceDotsFrontGroup');
    const gBack = document.getElementById('diceDotsBackGroup');

    if (gFront) {
        let dotsHtml = '';
        (diceDotLayouts[num] || []).forEach(([x, y]) => {
            dotsHtml += `<circle cx="${50 + x}" cy="${50 + y}" r="8" fill="#0f172a"/>`;
        });
        gFront.innerHTML = dotsHtml;
    }

    if (gBack) {
        let dotsHtml = '';
        (diceDotLayouts[oppNum] || []).forEach(([x, y]) => {
            dotsHtml += `<circle cx="${220 + x}" cy="${50 + y}" r="8" fill="#78350f"/>`;
        });
        gBack.innerHTML = dotsHtml;
    }

    const selVal = document.getElementById('dieSelectedVal');
    const oppVal = document.getElementById('dieOppositeVal');
    const sumVal = document.getElementById('dieSumVal');

    if (selVal) selVal.textContent = num;
    if (oppVal) oppVal.textContent = `7 - ${num} = ${oppNum}`;
    if (sumVal) sumVal.textContent = `${num} + ${oppNum} = 7`;

    playSuccessChime();
}


// Simulator 13: Twin Cube Fusion Laboratory
let twoCubesFused = false;

function toggleJoinTwoCubes() {
    twoCubesFused = !twoCubesFused;
    const btn = document.getElementById('btnJoinCubes');
    const status = document.getElementById('joinShapeStatus');
    const dims = document.getElementById('joinDimensions');
    const hidden = document.getElementById('joinHiddenFaces');
    const exposed = document.getElementById('joinExposedFaces');
    const note = document.getElementById('joinAnalysisNote');
    const group = document.getElementById('joinCubesDisplayGroup');

    if (twoCubesFused) {
        if (btn) btn.innerHTML = "🔓 Separate Cubes";
        if (status) {
            status.textContent = "1 Rectangular Cuboid";
            status.className = "text-xs px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold font-mono";
        }
        if (dims) dims.textContent = "10cm × 5cm × 5cm";
        if (hidden) hidden.textContent = "2 square faces";
        if (exposed) exposed.textContent = "10 unit squares (6 cuboid faces)";
        if (note) note.innerHTML = "✨ When joined, length doubles to 10cm! 2 square faces are sealed inside the seam: 12 - 2 = 10 exposed unit faces.";

        if (group) {
            group.innerHTML = `
                <!-- Fused Cuboid: Two joined cubes -->
                <polygon points="120,70 200,45 320,80 240,105" fill="#10b981" stroke="#fff" stroke-width="2"/>
                <polygon points="120,70 240,105 240,175 120,140" fill="#059669" stroke="#fff" stroke-width="2"/>
                <polygon points="240,105 320,80 320,150 240,175" fill="#047857" stroke="#fff" stroke-width="2"/>
                <!-- Seam Line Indicator -->
                <line x1="180" y1="88" x2="180" y2="158" stroke="#facc15" stroke-width="3" stroke-dasharray="4,4"/>
                <line x1="180" y1="88" x2="260" y2="62" stroke="#facc15" stroke-width="3" stroke-dasharray="4,4"/>
                <text x="220" y="30" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Hidden Contact Seam</text>
            `;
        }
    } else {
        if (btn) btn.innerHTML = "🔗 Join Face-to-Face";
        if (status) {
            status.textContent = "Two Separate Cubes";
            status.className = "text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold font-mono";
        }
        if (dims) dims.textContent = "5cm × 5cm each";
        if (hidden) hidden.textContent = "0 faces";
        if (exposed) exposed.textContent = "12 faces total (6 + 6)";
        if (note) note.textContent = "Click 'Join Face-to-Face' to fuse the two cubes and watch length double while 2 faces disappear into the seam!";

        if (group) {
            group.innerHTML = `
                <!-- Cube 1 -->
                <g transform="translate(-35, 0)">
                    <polygon points="120,70 170,50 220,70 170,90" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
                    <polygon points="120,70 170,90 170,150 120,130" fill="#0284c7" stroke="#fff" stroke-width="2"/>
                    <polygon points="170,90 220,70 220,130 170,150" fill="#0369a1" stroke="#fff" stroke-width="2"/>
                </g>
                <!-- Cube 2 -->
                <g transform="translate(65, 0)">
                    <polygon points="170,70 220,50 270,70 220,90" fill="#a855f7" stroke="#fff" stroke-width="2"/>
                    <polygon points="170,70 220,90 220,150 170,130" fill="#9333ea" stroke="#fff" stroke-width="2"/>
                    <polygon points="220,90 270,70 270,150 220,150" fill="#7e22ce" stroke="#fff" stroke-width="2"/>
                </g>
            `;
        }
    }

    playSuccessChime();
}


// Simulator 14: Tri-Cube Architecture Configurations
function setTriCubeLayout(type) {
    const btnLine = document.getElementById('btnTriLine');
    const btnCorner = document.getElementById('btnTriCorner');
    const title = document.getElementById('triConfigTitle');
    const solid = document.getElementById('triSolidClassification');
    const exposed = document.getElementById('triExposedCount');
    const note = document.getElementById('triConfigNote');
    const group = document.getElementById('triCubeRenderGroup');

    if (type === 'line') {
        if (btnLine) {
            btnLine.className = "px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow";
        }
        if (btnCorner) {
            btnCorner.className = "px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition";
        }
        if (title) title.textContent = "Configuration: Straight Bar (3×1×1)";
        if (solid) solid.textContent = "Rectangular Cuboid";
        if (exposed) exposed.textContent = "14 unit squares";
        if (note) note.textContent = "All 3 cubes aligned in a straight line produce an elongated cuboid of dimensions 3×1×1.";

        if (group) {
            group.innerHTML = `
                <!-- 3 Cubes in Line -->
                <polygon points="80,80 180,45 320,80 220,115" fill="#f59e0b" stroke="#fff" stroke-width="2"/>
                <polygon points="80,80 220,115 220,170 80,135" fill="#d97706" stroke="#fff" stroke-width="2"/>
                <polygon points="220,115 320,80 320,135 220,170" fill="#b45309" stroke="#fff" stroke-width="2"/>
                <!-- Seams -->
                <line x1="127" y1="92" x2="127" y2="147" stroke="#fff" stroke-width="1.5" stroke-dasharray="3,3"/>
                <line x1="174" y1="104" x2="174" y2="159" stroke="#fff" stroke-width="1.5" stroke-dasharray="3,3"/>
            `;
        }
    } else {
        if (btnLine) {
            btnLine.className = "px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition";
        }
        if (btnCorner) {
            btnCorner.className = "px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow";
        }
        if (title) title.textContent = "Configuration: L-Shaped Corner";
        if (solid) solid.textContent = "Triomino Composite Solid";
        if (exposed) exposed.textContent = "14 unit squares";
        if (note) note.textContent = "Bent at a right angle, this triomino has the same 3-cube volume (and 14 outer faces) but is no longer a simple cuboid!";

        if (group) {
            group.innerHTML = `
                <!-- L-Shaped Corner Assembly -->
                <g transform="translate(10, 10)">
                    <!-- Base Corner Cube -->
                    <polygon points="150,90 200,75 250,90 200,105" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
                    <polygon points="150,90 200,105 200,165 150,150" fill="#2563eb" stroke="#fff" stroke-width="2"/>
                    <polygon points="200,105 250,90 250,150 200,165" fill="#1d4ed8" stroke="#fff" stroke-width="2"/>

                    <!-- Left Arm Cube -->
                    <polygon points="100,105 150,90 200,105 150,120" fill="#06b6d4" stroke="#fff" stroke-width="2"/>
                    <polygon points="100,105 150,120 150,180 100,165" fill="#0891b2" stroke="#fff" stroke-width="2"/>
                    <polygon points="150,120 200,105 200,165 150,180" fill="#0e7490" stroke="#fff" stroke-width="2"/>

                    <!-- Upright Top Cube -->
                    <polygon points="150,30 200,15 250,30 200,45" fill="#8b5cf6" stroke="#fff" stroke-width="2"/>
                    <polygon points="150,30 200,45 200,105 150,90" fill="#7c3aed" stroke="#fff" stroke-width="2"/>
                    <polygon points="200,45 250,30 250,90 200,105" fill="#6d28d9" stroke="#fff" stroke-width="2"/>
                </g>
            `;
        }
    }

    playSuccessChime();
}


// Simulator 15: Composite Model Stacks (Staircase & Hidden Blocks)
let isStaircaseXray = false;

function toggleBlockStackXray() {
    isStaircaseXray = !isStaircaseXray;
    const btn = document.getElementById('btnBlockXray');
    if (btn) {
        if (isStaircaseXray) {
            btn.className = "px-3 py-1.5 rounded-xl bg-cyan-600 text-white font-bold text-xs transition shadow flex items-center gap-1";
            btn.innerHTML = "✨ X-Ray Active (Hidden Cubes Shown!)";
        } else {
            btn.className = "px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-500/40 font-bold text-xs transition shadow flex items-center gap-1";
            btn.innerHTML = "🔍 Toggle X-Ray View";
        }
    }

    renderStaircaseCubes();
    playSuccessChime();
}

function renderStaircaseCubes() {
    const group = document.getElementById('staircaseCubesGroup');
    if (!group) return;

    if (isStaircaseXray) {
        // Wireframe / Transparent view showing 3 hidden cubes underneath
        group.innerHTML = `
            <!-- Foundation Hidden Cubes (Semi-transparent) -->
            <!-- Under Column 2: 1 Hidden Cube -->
            <g opacity="0.85">
                <rect x="160" y="145" width="40" height="40" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="180" y="170" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Hidden 1</text>
            </g>
            <!-- Under Column 3: 2 Hidden Cubes -->
            <g opacity="0.85">
                <rect x="220" y="145" width="40" height="40" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="240" y="170" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Hidden 2</text>
                <rect x="220" y="105" width="40" height="40" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="240" y="130" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Hidden 3</text>
            </g>

            <!-- Visible Outer Cubes -->
            <!-- Step 1 -->
            <rect x="100" y="145" width="40" height="40" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="120" y="170" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">#1</text>
            <!-- Step 2 Top -->
            <rect x="160" y="105" width="40" height="40" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="180" y="130" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">#2</text>
            <!-- Step 3 Top -->
            <rect x="220" y="65" width="40" height="40" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="240" y="90" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">#3</text>
        `;
    } else {
        // Solid Isometric Staircase
        group.innerHTML = `
            <!-- Step 1 (Height 1) -->
            <g transform="translate(-40, 25)">
                <polygon points="140,110 170,95 200,110 170,125" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
                <polygon points="140,110 170,125 170,165 140,150" fill="#0284c7" stroke="#fff" stroke-width="2"/>
                <polygon points="170,125 200,110 200,150 170,165" fill="#0369a1" stroke="#fff" stroke-width="2"/>
            </g>
            <!-- Step 2 (Height 2) -->
            <g transform="translate(10, -5)">
                <polygon points="140,80 170,65 200,80 170,95" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
                <polygon points="140,80 170,95 170,165 140,150" fill="#0284c7" stroke="#fff" stroke-width="2"/>
                <polygon points="170,95 200,80 200,150 170,165" fill="#0369a1" stroke="#fff" stroke-width="2"/>
            </g>
            <!-- Step 3 (Height 3) -->
            <g transform="translate(60, -35)">
                <polygon points="140,50 170,35 200,50 170,65" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
                <polygon points="140,50 170,65 170,165 140,150" fill="#0284c7" stroke="#fff" stroke-width="2"/>
                <polygon points="170,65 200,50 200,150 170,165" fill="#0369a1" stroke="#fff" stroke-width="2"/>
            </g>
        `;
    }
}


// Simulator 16: Master 3D Solid Geometry Matrix
function filterMatrixShape(shape) {
    const rows = ['rowMatrixCube', 'rowMatrixCuboid', 'rowMatrixCylinder', 'rowMatrixCone', 'rowMatrixSphere'];
    rows.forEach(rId => {
        const row = document.getElementById(rId);
        if (row) row.classList.remove('bg-amber-500/20', 'ring-1', 'ring-amber-400');
    });

    if (shape === 'all') return;

    const rowMap = {
        cube: 'rowMatrixCube',
        cuboid: 'rowMatrixCuboid',
        cylinder: 'rowMatrixCylinder',
        cone: 'rowMatrixCone',
        sphere: 'rowMatrixSphere'
    };

    const targetRow = document.getElementById(rowMap[shape]);
    if (targetRow) {
        targetRow.classList.add('bg-amber-500/20', 'ring-1', 'ring-amber-400');
    }
    playSuccessChime();
}


// =========================================================================
// INITIALIZATION ON DOM READY
// =========================================================================
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    renderCraftStage();
    updateMorphBox();
    initBoardTiles();
    selectDieFace(1);
    toggleJoinTwoCubes(); // Initialize two cubes joined or separate
    setTriCubeLayout('line');
    renderStaircaseCubes();
});

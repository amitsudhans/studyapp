// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 4 Science - Chapter 10: Our Sky
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

// Concept Checkpoint Verification
window.checkAnswer = function(slideId, cpIdx, optIdx, correctText) {
    const cpContainer = document.getElementById(`cp-${slideId}-${cpIdx}`);
    if (!cpContainer) return;

    const optButtons = cpContainer.querySelectorAll('.checkpoint-opt-btn');
    const feedbackBox = document.getElementById(`fb-${slideId}-${cpIdx}`);
    const selectedBtn = optButtons[optIdx];
    const isCorrect = (selectedBtn && selectedBtn.getAttribute('data-opt-val') === correctText);

    optButtons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800', 'border-slate-800');
        if (btn.getAttribute('data-opt-val') === correctText) {
            btn.classList.add('bg-emerald-950/70', 'border-emerald-500', 'text-emerald-200');
        }
    });

    if (isCorrect) {
        playSuccessChime();
        if (selectedBtn) {
            selectedBtn.classList.add('ring-2', 'ring-emerald-400');
        }
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs flex items-start gap-2">
                    <span class="text-base">✅</span>
                    <div>
                        <strong>Excellent! Accurate Observation!</strong>
                        <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                    </div>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    } else {
        playErrorChime();
        if (selectedBtn) {
            selectedBtn.classList.add('bg-rose-950/70', 'border-rose-500', 'text-rose-200', 'ring-2', 'ring-rose-400');
        }
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs flex items-start gap-2">
                    <span class="text-base">💡</span>
                    <div>
                        <strong>Scientific Reflection:</strong>
                        <p class="mt-0.5 text-slate-300">${feedbackBox.getAttribute('data-explanation') || ''}</p>
                    </div>
                </div>
            `;
            feedbackBox.classList.remove('hidden');
        }
    }
};

// Challenge Quiz Verification
window.checkQuizAnswer = function(qId, selectedOption, correctOption) {
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
        playSuccessChime();
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs flex items-start justify-between gap-2">
                    <div class="flex items-start gap-2">
                        <span class="text-base">🌟</span>
                        <div>
                            <strong>Mastery Confirmed! Correct Answer!</strong>
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
        playErrorChime();
        if (feedbackBox) {
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs flex items-start justify-between gap-2">
                    <div class="flex items-start gap-2">
                        <span class="text-base">🔍</span>
                        <div>
                            <strong>Let's Analyze the Science:</strong>
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
};

// 3-Step Scientific Solution Modal
window.showSolutionModal = function(qId) {
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

    modalTitle.textContent = `Scientific Solution: ${targetQuestion.id.toUpperCase()}`;
    const steps = targetQuestion.solution_steps || {
        step1: "Observe the core natural phenomenon in the sky.",
        step2: "Apply the fundamental scientific principle governing the observation.",
        step3: "Synthesize the empirical evidence to deduce the correct conclusion."
    };

    modalContent.innerHTML = `
        <div class="space-y-4">
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider">Question Context</span>
                <p class="text-xs sm:text-sm text-slate-200 mt-1">${targetQuestion.q}</p>
            </div>

            <div class="space-y-2.5">
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-800/40 text-xs">
                    <span class="font-bold text-cyan-300 block mb-1">Step 1: Scientific Premise</span>
                    <p class="text-slate-300">${steps.step1}</p>
                </div>
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-800/40 text-xs">
                    <span class="font-bold text-blue-300 block mb-1">Step 2: Empirical Analysis</span>
                    <p class="text-slate-300">${steps.step2}</p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/40 text-xs">
                    <span class="font-bold text-emerald-300 block mb-1">Step 3: Verified Deduction</span>
                    <p class="text-slate-300">${steps.step3}</p>
                </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                <span class="text-xs text-slate-400">Correct Scientific Option:</span>
                <span class="text-xs font-bold text-emerald-400">${targetQuestion.ans}</span>
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
};

window.closeSolutionModal = function() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
};

// =========================================================================
// 16 INTERACTIVE BESPOKE SIMULATOR CONTROLLERS
// =========================================================================

// SIM 1: Changing Daily Sky
window.updateDailySkyTime = function(val) {
    const hour = parseInt(val);
    const timeDisp = document.getElementById('timeDisplayVal');
    const skyBg = document.getElementById('skyBackgroundRect');
    const sunGroup = document.getElementById('celestialSunGroup');
    const moonGroup = document.getElementById('celestialMoonGroup');
    const phaseDesc = document.getElementById('skyPhaseDesc');
    const elevVal = document.getElementById('solarElevVal');
    const colorVal = document.getElementById('skyColorVal');
    const actVal = document.getElementById('natureActVal');

    let timeStr = "";
    let ampm = hour < 12 ? "AM" : "PM";
    let displayHour = hour % 12;
    if (displayHour === 0) displayHour = 12;
    timeStr = `${displayHour < 10 ? '0' : ''}${displayHour}:00 ${ampm}`;

    let sunX = 0, sunY = 0, sunOpacity = 1;
    let moonOpacity = 0;

    if (hour >= 5 && hour < 8) {
        // Dawn
        if (timeDisp) timeDisp.innerHTML = `${timeStr} <span class="text-amber-400 font-bold">(Dawn)</span>`;
        if (skyBg) skyBg.setAttribute('fill', '#f97316');
        sunOpacity = 1;
        sunX = 80 + (hour - 5) * 40;
        sunY = 160 - (hour - 5) * 40;
        if (phaseDesc) phaseDesc.textContent = "Soft amber & rose hues brighten the eastern horizon as the Sun rises.";
        if (elevVal) elevVal.textContent = "15° (Low East)";
        if (colorVal) colorVal.textContent = "Amber, Gold, Rose Pink";
        if (actVal) actVal.textContent = "Birds leave nests, flowers open, cool breeze";
    } else if (hour >= 8 && hour < 16) {
        // Daytime / Midday
        if (timeDisp) timeDisp.innerHTML = `${timeStr} <span class="text-yellow-300 font-bold">(Daytime)</span>`;
        if (skyBg) skyBg.setAttribute('fill', '#38bdf8');
        sunOpacity = 1;
        let progress = (hour - 8) / 8;
        sunX = 200 + progress * 100;
        sunY = 50 + Math.abs(progress - 0.5) * 70;
        if (phaseDesc) phaseDesc.textContent = "The Sun shines brilliantly overhead at its highest altitude, scattering blue light.";
        if (elevVal) elevVal.textContent = hour === 12 ? "90° (Direct Overhead Zenith)" : "65° (High Sky)";
        if (colorVal) colorVal.textContent = "Crisp Azure Blue";
        if (actVal) actVal.textContent = "Photosynthesis peaks, animals forage, active humans";
    } else if (hour >= 16 && hour < 19) {
        // Twilight / Sunset
        if (timeDisp) timeDisp.innerHTML = `${timeStr} <span class="text-orange-400 font-bold">(Sunset)</span>`;
        if (skyBg) skyBg.setAttribute('fill', '#c2410c');
        sunOpacity = 1;
        sunX = 380 + (hour - 16) * 35;
        sunY = 100 + (hour - 16) * 30;
        if (phaseDesc) phaseDesc.textContent = "Sun sinks toward western horizon, scattering longer red and orange light rays.";
        if (elevVal) elevVal.textContent = "12° (Low West)";
        if (colorVal) colorVal.textContent = "Crimson, Purple, Fiery Orange";
        if (actVal) actVal.textContent = "Birds return to roost, lotus blossoms close";
    } else {
        // Night
        if (timeDisp) timeDisp.innerHTML = `${timeStr} <span class="text-indigo-400 font-bold">(Night)</span>`;
        if (skyBg) skyBg.setAttribute('fill', '#020617');
        sunOpacity = 0;
        moonOpacity = 1;
        if (phaseDesc) phaseDesc.textContent = "Sun is below opposite horizon; darkness reveals the shining Moon and starry constellations.";
        if (elevVal) elevVal.textContent = "Below Horizon (-45°)";
        if (colorVal) colorVal.textContent = "Velvet Midnight Black";
        if (actVal) actVal.textContent = "Owls hunt, bats take flight, nocturnal blooms";
    }

    if (sunGroup) {
        sunGroup.setAttribute('opacity', sunOpacity);
        sunGroup.setAttribute('transform', `translate(${sunX - 100}, ${sunY - 140})`);
    }
    if (moonGroup) {
        moonGroup.setAttribute('opacity', moonOpacity);
    }
};

// SIM 2: The Radiant Sun
window.triggerSolarFlare = function() {
    const core = document.getElementById('solarCoreGlow');
    if (!core) return;

    playSuccessChime();
    core.classList.add('scale-125', 'ring-8', 'ring-yellow-300');
    setTimeout(() => {
        core.classList.remove('scale-125', 'ring-8', 'ring-yellow-300');
    }, 900);
};

// SIM 3: Daytime Biological Rhythms
window.setCircadianMode = function(mode) {
    const btnDay = document.getElementById('btnCircDay');
    const btnNight = document.getElementById('btnCircNight');

    const fIcon = document.getElementById('circFloraIcon');
    const fTitle = document.getElementById('circFloraTitle');
    const fDesc = document.getElementById('circFloraDesc');

    const bIcon = document.getElementById('circBirdIcon');
    const bTitle = document.getElementById('circBirdTitle');
    const bDesc = document.getElementById('circBirdDesc');

    const mIcon = document.getElementById('circMammalIcon');
    const mTitle = document.getElementById('circMammalTitle');
    const mDesc = document.getElementById('circMammalDesc');

    if (mode === 'day') {
        if (btnDay) { btnDay.className = "px-3 py-1 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition"; }
        if (btnNight) { btnNight.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition"; }

        if (fIcon) fIcon.textContent = "🌻";
        if (fTitle) fTitle.textContent = "Sunflowers & Lotus";
        if (fDesc) fDesc.textContent = "Petals open wide to capture radiant solar rays for photosynthesis, tracking the Sun across the sky.";

        if (bIcon) bIcon.textContent = "🐦";
        if (bTitle) bTitle.textContent = "Sparrows & Parrots";
        if (bDesc) bDesc.textContent = "Vocalize actively at sunrise, forage across grasslands for seeds, and navigate using daylight vision.";

        if (mIcon) mIcon.textContent = "🐄";
        if (mTitle) mTitle.textContent = "Cattle & Squirrels";
        if (mDesc) mDesc.textContent = "Graze openly in pastures, active throughout daytime hours, and rest peacefully as dusk settles.";
    } else {
        if (btnDay) { btnDay.className = "px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition"; }
        if (btnNight) { btnNight.className = "px-3 py-1 rounded-xl bg-indigo-600 text-white font-bold text-xs transition"; }

        if (fIcon) fIcon.textContent = "🌸";
        if (fTitle) fTitle.textContent = "Night-Blooming Jasmine";
        if (fDesc) fDesc.textContent = "Blooms exclusively under moonlight (Raat ki Rani) releasing intense fragrance to attract night moths.";

        if (bIcon) bIcon.textContent = "🦉";
        if (bTitle) bTitle.textContent = "Barn Owls & Nightjars";
        if (bDesc) bDesc.textContent = "Equipped with expansive pupils and acute binaural hearing to silently hunt nocturnal rodents in total darkness.";

        if (mIcon) mIcon.textContent = "🦇";
        if (mTitle) mTitle.textContent = "Fruit Bats & Civets";
        if (mDesc) mDesc.textContent = "Roost upside-down in caves by day, emerging at night to navigate and forage using ultrasonic echolocation.";
    }
};

// SIM 4: Forming Light Shadows
window.setShadowMaterial = function(mat) {
    const btnOp = document.getElementById('btnMatOpaque');
    const btnTr = document.getElementById('btnMatTranslucent');
    const btnTp = document.getElementById('btnMatTransparent');

    const barRect = document.getElementById('barrierRect');
    const barLabel = document.getElementById('barrierLabel');
    const transRays = document.getElementById('transmittedRaysGroup');
    const castShad = document.getElementById('castShadowRect');
    const shadLabel = document.getElementById('shadowLabel');
    const lawText = document.getElementById('opticsLawText');
    const densVal = document.getElementById('shadowDensityVal');

    [btnOp, btnTr, btnTp].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    if (mat === 'opaque') {
        if (btnOp) btnOp.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (barRect) barRect.setAttribute('fill', '#92400e');
        if (barLabel) barLabel.textContent = "Opaque Wood Barrier";
        if (transRays) transRays.setAttribute('opacity', '0');
        if (castShad) {
            castShad.setAttribute('opacity', '0.95');
            castShad.setAttribute('width', '55');
        }
        if (shadLabel) shadLabel.textContent = "Dark, Crisp Shadow (Umbra)";
        if (lawText) lawText.textContent = "Light travels in straight lines. Opaque matter completely obstructs photons, casting a dense, sharp shadow.";
        if (densVal) densVal.textContent = "100% Solid Umbra (No Light Transmitted)";
    } else if (mat === 'translucent') {
        if (btnTr) btnTr.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (barRect) barRect.setAttribute('fill', '#e2e8f0');
        if (barLabel) barLabel.textContent = "Translucent Butter Paper";
        if (transRays) transRays.setAttribute('opacity', '0.4');
        if (castShad) {
            castShad.setAttribute('opacity', '0.35');
            castShad.setAttribute('width', '45');
        }
        if (shadLabel) shadLabel.textContent = "Faint, Soft Shadow";
        if (lawText) lawText.textContent = "Translucent materials scatter and transmit some light rays, casting a pale, diffused shadow.";
        if (densVal) densVal.textContent = "40% Partial Penumbra (Diffused Transmission)";
    } else {
        if (btnTp) btnTp.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (barRect) barRect.setAttribute('fill', '#67e8f9');
        if (barLabel) barLabel.textContent = "Transparent Clear Glass";
        if (transRays) transRays.setAttribute('opacity', '1');
        if (castShad) {
            castShad.setAttribute('opacity', '0.05');
            castShad.setAttribute('width', '0');
        }
        if (shadLabel) shadLabel.textContent = "No Shadow Formed";
        if (lawText) lawText.textContent = "Transparent glass permits nearly all light waves to pass uninterrupted; hence, no detectable shadow appears.";
        if (densVal) densVal.textContent = "0% (Zero Obstruction / Free Passage)";
    }
};

// SIM 5: Daylong Shadow Shifts
window.updateGnomonShadow = function(val) {
    const p = parseInt(val);
    const sunOrb = document.getElementById('gnomonSunOrb');
    const castShad = document.getElementById('gnomonCastShadow');
    const statusText = document.getElementById('gnomonStatusText');
    const lenVal = document.getElementById('shadowLengthVal');
    const dirVal = document.getElementById('shadowDirVal');
    const zenVal = document.getElementById('solarZenithVal');

    // Values: 1: Early Morning (07:00 AM), 2: Mid-Morning (10:00 AM), 3: Noon (12:00 PM), 4: Mid-Afternoon (03:00 PM), 5: Evening (05:30 PM)
    if (p === 1) {
        if (sunOrb) { sunOrb.setAttribute('cx', '60'); sunOrb.setAttribute('cy', '150'); }
        if (castShad) { castShad.setAttribute('x1', '250'); castShad.setAttribute('y1', '190'); castShad.setAttribute('x2', '410'); castShad.setAttribute('y2', '190'); castShad.setAttribute('stroke-width', '14'); }
        if (statusText) statusText.textContent = "Sun low in Eastern sky. Rays strike at a sharp slant, casting a very long shadow toward the West.";
        if (lenVal) lenVal.textContent = "Very Long (160 cm)";
        if (dirVal) dirVal.textContent = "Points West (Opposite to East Sun)";
        if (zenVal) zenVal.textContent = "15° Slant Angle";
    } else if (p === 2) {
        if (sunOrb) { sunOrb.setAttribute('cx', '140'); sunOrb.setAttribute('cy', '90'); }
        if (castShad) { castShad.setAttribute('x1', '250'); castShad.setAttribute('y1', '190'); castShad.setAttribute('x2', '340'); castShad.setAttribute('y2', '190'); castShad.setAttribute('stroke-width', '12'); }
        if (statusText) statusText.textContent = "Sun climbs higher toward the southeast. Shadow steadily shortens as solar elevation angle increases.";
        if (lenVal) lenVal.textContent = "Medium (90 cm)";
        if (dirVal) dirVal.textContent = "Points West-Northwest";
        if (zenVal) zenVal.textContent = "50° Elevation";
    } else if (p === 3) {
        if (sunOrb) { sunOrb.setAttribute('cx', '250'); sunOrb.setAttribute('cy', '40'); }
        if (castShad) { castShad.setAttribute('x1', '250'); castShad.setAttribute('y1', '190'); castShad.setAttribute('x2', '265'); castShad.setAttribute('y2', '190'); castShad.setAttribute('stroke-width', '16'); }
        if (statusText) statusText.textContent = "Sun reaches midday zenith overhead! Rays strike almost vertically, producing the shortest shadow of the day.";
        if (lenVal) lenVal.textContent = "Shortest of the Day (15 cm)";
        if (dirVal) dirVal.textContent = "Directly Beneath Base";
        if (zenVal) zenVal.textContent = "88° Overhead Zenith";
    } else if (p === 4) {
        if (sunOrb) { sunOrb.setAttribute('cx', '360'); sunOrb.setAttribute('cy', '90'); }
        if (castShad) { castShad.setAttribute('x1', '250'); castShad.setAttribute('y1', '190'); castShad.setAttribute('x2', '160'); castShad.setAttribute('y2', '190'); castShad.setAttribute('stroke-width', '12'); }
        if (statusText) statusText.textContent = "Sun descends into southwestern sky. Shadow reverses direction, pointing eastwards and lengthening steadily.";
        if (lenVal) lenVal.textContent = "Medium (90 cm)";
        if (dirVal) dirVal.textContent = "Points East-Northeast";
        if (zenVal) zenVal.textContent = "50° Elevation";
    } else {
        if (sunOrb) { sunOrb.setAttribute('cx', '440'); sunOrb.setAttribute('cy', '150'); }
        if (castShad) { castShad.setAttribute('x1', '250'); castShad.setAttribute('y1', '190'); castShad.setAttribute('x2', '90'); castShad.setAttribute('y2', '190'); castShad.setAttribute('stroke-width', '14'); }
        if (statusText) statusText.textContent = "Sun sinks low in Western sky. Long evening rays cast a prominent, elongated shadow pointing straight East.";
        if (lenVal) lenVal.textContent = "Very Long (160 cm)";
        if (dirVal) dirVal.textContent = "Points East (Opposite to West Sun)";
        if (zenVal) zenVal.textContent = "15° Slant Angle";
    }
};

// SIM 6: Torchlight Shadow Lab
window.updateTorchLab = function(val) {
    const dist = parseInt(val); // 20 (close) to 100 (far)
    const torchGrp = document.getElementById('torchSvgGroup');
    const wallShadow = document.getElementById('wallShadowRect');
    const status = document.getElementById('torchLabStatus');

    if (torchGrp) {
        // Move torch along X: when dist is 20 -> torch is near x=120; when dist is 100 -> torch is at x=20
        const xOffset = (100 - dist) * 1.0;
        torchGrp.setAttribute('transform', `translate(${xOffset}, 0)`);
    }

    if (wallShadow) {
        // When torch is close to object (dist small), shadow is magnified
        const shadowHeight = 40 + (100 - dist) * 0.9;
        const shadowY = 110 - (shadowHeight / 2);
        wallShadow.setAttribute('height', shadowHeight);
        wallShadow.setAttribute('y', shadowY);
    }

    if (status) {
        if (dist < 40) {
            status.textContent = "Torch Close to Obstacle: Large angular spread blocks more light rays, casting a hugely magnified shadow!";
        } else if (dist > 75) {
            status.textContent = "Torch Far from Obstacle: Beam angle subtends smaller spread, producing a smaller, crisper shadow on the screen.";
        } else {
            status.textContent = "Moderate Torch Distance: Standard proportional shadow formed on the projection surface.";
        }
    }
};

// SIM 7: Historical Shadow Sundials
let currentSundialHour = 12;
window.stepSundialHour = function(delta) {
    currentSundialHour += delta;
    if (currentSundialHour < 7) currentSundialHour = 7;
    if (currentSundialHour > 17) currentSundialHour = 17;

    const timeText = document.getElementById('sundialTimeText');
    const shadLine = document.getElementById('sundialShadowLine');
    const accText = document.getElementById('sundialAccuracyText');

    let ampm = currentSundialHour < 12 ? "AM" : "PM";
    let dispH = currentSundialHour % 12;
    if (dispH === 0) dispH = 12;

    if (timeText) timeText.textContent = `${dispH}:00 ${ampm} (${currentSundialHour === 12 ? 'Noon' : (currentSundialHour < 12 ? 'Morning' : 'Afternoon')})`;

    if (shadLine) {
        // Angle spans from -60 deg (at 7 AM) to +60 deg (at 5 PM)
        const angle = (currentSundialHour - 12) * 12;
        shadLine.setAttribute('transform', `rotate(${angle}, 250, 180)`);
    }

    if (accText) {
        accText.textContent = `Samrat Yantra Angle: ${(currentSundialHour - 12) * 15}° from meridian. Calibrated marble scales read solar time with 2-second precision!`;
    }
};

// SIM 8: Creative Shadow Puppetry
window.setShadowPuppet = function(puppet) {
    const btnDeer = document.getElementById('btnPupDeer');
    const btnBird = document.getElementById('btnPupBird');
    const btnDog = document.getElementById('btnPupDog');
    const btnTholu = document.getElementById('btnPupTholu');

    const display = document.getElementById('puppetFigureDisplay');
    const title = document.getElementById('puppetTraditionTitle');
    const desc = document.getElementById('puppetTraditionDesc');

    [btnDeer, btnBird, btnDog, btnTholu].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    if (puppet === 'deer') {
        if (btnDeer) btnDeer.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (display) display.innerHTML = `<span class="text-7xl drop-shadow-[0_10px_10px_rgba(0,0,0,0.8)] filter grayscale contrast-200">🦌</span>`;
        if (title) title.textContent = "Hand Silhouette: Leaping Deer (Hiran)";
        if (desc) desc.textContent = "Interlocking fingers create antlers while the thumbs shape a slender neck, casting an unmistakable deer profile on the white screen.";
    } else if (puppet === 'bird') {
        if (btnBird) btnBird.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (display) display.innerHTML = `<span class="text-7xl drop-shadow-[0_10px_10px_rgba(0,0,0,0.8)] filter grayscale contrast-200">🦅</span>`;
        if (title) title.textContent = "Hand Silhouette: Soaring Eagle (Garuda)";
        if (desc) desc.textContent = "Hooking thumbs together and flapping outstretched fingers simulates aerodynamic wings in flight against the illuminated backdrop.";
    } else if (puppet === 'dog') {
        if (btnDog) btnDog.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (display) display.innerHTML = `<span class="text-7xl drop-shadow-[0_10px_10px_rgba(0,0,0,0.8)] filter grayscale contrast-200">🐕</span>`;
        if (title) title.textContent = "Hand Silhouette: Barking Dog (Kutta)";
        if (desc) desc.textContent = "Folding the palm with index finger raised as ears and pinky moving as the jaw creates a playful barking animal shadow.";
    } else {
        if (btnTholu) btnTholu.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (display) display.innerHTML = `<span class="text-7xl drop-shadow-[0_10px_10px_rgba(0,0,0,0.8)] filter contrast-150">🎭</span>`;
        if (title) title.textContent = "Traditional Indian Shadow Theatre: Tholu Bommalata";
        if (desc) desc.textContent = "Perforated, translucent goat-leather figures painted with vegetable dyes cast vibrant, articulated shadows in Andhra Pradesh and Karnataka folk puppetry.";
    }
};

// SIM 9: Dazzling Night Sky
let constellationLinesVisible = false;
window.toggleConstellationLines = function() {
    const linesGroup = document.getElementById('constellationLinesGroup');
    const btn = document.getElementById('btnConstLines');
    const status = document.getElementById('stargazingStatusText');

    constellationLinesVisible = !constellationLinesVisible;

    if (linesGroup) {
        linesGroup.setAttribute('opacity', constellationLinesVisible ? '1' : '0');
    }

    if (btn) {
        btn.textContent = constellationLinesVisible ? "Hide Constellation Lines" : "✨ Connect Saptarishi Stars";
        btn.className = constellationLinesVisible 
            ? "px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition" 
            : "px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition";
    }

    if (status) {
        status.textContent = constellationLinesVisible 
            ? "Saptarishi Pattern Linked! Follow the pointer stars (Kratu and Pulaha) straight north: they point directly to Polaris (Dhruva Tara), the stationary northern anchor!" 
            : "Look towards the northern sky to locate the seven distinct stars forming the great ladle of Saptarishi.";
    }
};

// SIM 10: Moon Surface Glow
let moonRaysReflecting = false;
window.toggleSunbeamReflection = function() {
    const overlay = document.getElementById('moonReflectOverlay');
    moonRaysReflecting = !moonRaysReflecting;
    if (overlay) {
        overlay.classList.toggle('opacity-100', moonRaysReflecting);
        overlay.classList.toggle('opacity-0', !moonRaysReflecting);
    }
    playSuccessChime();
};

// SIM 11: Phases of the Moon
let currentMoonPhaseIdx = 0;
const moonPhaseData = [
    { name: "1. New Moon (Amavasya)", day: "Day 1", illum: "0% (Completely Dark)", desc: "Moon is situated directly between Earth and Sun. Its unlit hemisphere faces Earth, making it invisible in night sky.", visual: "🌑" },
    { name: "2. Waxing Crescent", day: "Day 3 - 4", illum: "15% Slender Curve", desc: "A slender silver sliver appears in the western evening sky after sunset, growing slightly thicker each night.", visual: "🌒" },
    { name: "3. First Quarter (Half Moon)", day: "Day 7", illum: "50% Illuminated", desc: "One-half of the visible lunar disc shines brightly one week after Amavasya, marking the first quarter orbit.", visual: "🌓" },
    { name: "4. Waxing Gibbous", day: "Day 10 - 11", illum: "85% Swollen Glow", desc: "More than half the visible side is illuminated as the Moon approaches the full alignment opposite the Sun.", visual: "🌔" },
    { name: "5. Full Moon (Poornima)", day: "Day 14 - 15", illum: "100% Round Orb", desc: "Earth sits between Sun and Moon. The entire illuminated hemisphere faces us, casting silvery night radiance.", visual: "🌕" },
    { name: "6. Waning Gibbous", day: "Day 18 - 19", illum: "85% Shrinking Orb", desc: "The illuminated disc begins to shrink (wane) day by day, rising later and later in the night.", visual: "🌖" },
    { name: "7. Third Quarter", day: "Day 22", illum: "50% Illuminated", desc: "Exactly half of the lunar surface is illuminated in reverse orientation, visible predominantly in the morning sky.", visual: "🌗" },
    { name: "8. Waning Crescent", day: "Day 26 - 27", illum: "15% Morning Sliver", desc: "A delicate crescent Moon rises just before dawn in the eastern sky, completing the 29.5-day synodic lunar month.", visual: "🌘" }
];

window.stepMoonPhase = function(delta) {
    currentMoonPhaseIdx += delta;
    if (currentMoonPhaseIdx < 0) currentMoonPhaseIdx = moonPhaseData.length - 1;
    if (currentMoonPhaseIdx >= moonPhaseData.length) currentMoonPhaseIdx = 0;

    const cur = moonPhaseData[currentMoonPhaseIdx];
    const badge = document.getElementById('phaseDisplayBadge');
    const visual = document.getElementById('lunarPhaseVisual');
    const name = document.getElementById('lunarPhaseName');
    const day = document.getElementById('lunarPhaseDay');
    const desc = document.getElementById('lunarPhaseDesc');
    const illum = document.getElementById('lunarIllumVal');
    const prog = document.getElementById('lunarProgressVal');

    if (badge) badge.textContent = cur.name;
    if (visual) visual.textContent = cur.visual;
    if (name) name.textContent = cur.name;
    if (day) day.textContent = cur.day;
    if (desc) desc.textContent = cur.desc;
    if (illum) illum.textContent = cur.illum;
    if (prog) prog.textContent = `Phase ${currentMoonPhaseIdx + 1} of 8 (${Math.round(((currentMoonPhaseIdx + 1) / 8) * 100)}% cycle)`;
};

// SIM 12: Lunar Calendar Festivals
window.selectFestival = function(fest) {
    const btnDiwali = document.getElementById('btnFestDiwali');
    const btnEid = document.getElementById('btnFestEid');
    const btnBuddha = document.getElementById('btnFestBuddha');
    const btnKarva = document.getElementById('btnFestKarva');

    const icon = document.getElementById('festEmojiIcon');
    const heading = document.getElementById('festNameHeading');
    const phaseTag = document.getElementById('festPhaseTag');
    const desc = document.getElementById('festDescText');
    const link = document.getElementById('festAstroLink');

    [btnDiwali, btnEid, btnBuddha, btnKarva].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    if (fest === 'diwali') {
        if (btnDiwali) btnDiwali.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (icon) icon.textContent = "🪔";
        if (heading) heading.textContent = "Diwali (Festival of Lights)";
        if (phaseTag) phaseTag.textContent = "Kartik Amavasya (New Moon Night)";
        if (desc) desc.textContent = "Celebrated on the darkest night of the lunar month (Amavasya) in the Hindu month of Kartik. Millions of clay diyas and lamps illuminate homes to welcome prosperity.";
        if (link) link.textContent = "Astronomical Link: Marked by the total absence of moonlight in the night sky.";
    } else if (fest === 'eid') {
        if (btnEid) btnEid.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (icon) icon.textContent = "🌙";
        if (heading) heading.textContent = "Eid-ul-Fitr (Festival of Breaking Fast)";
        if (phaseTag) phaseTag.textContent = "Waxing Crescent (Hilal Sighting)";
        if (desc) desc.textContent = "Celebrated upon the confirmed visual sighting of the delicate first waxing crescent Moon (Hilal), marking the auspicious conclusion of the holy month of Ramadan.";
        if (link) link.textContent = "Astronomical Link: Lunar calendar month Shawwal begins on Day 1 of the new crescent.";
    } else if (fest === 'buddha') {
        if (btnBuddha) btnBuddha.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (icon) icon.textContent = "🌕";
        if (heading) heading.textContent = "Buddha Poornima & Guru Poornima";
        if (phaseTag) phaseTag.textContent = "Vaisakha / Ashadha Poornima (Full Moon)";
        if (desc) desc.textContent = "Commemorated on the radiant full moon night. Traditional festivals like Holi, Raksha Bandhan, and Buddha Poornima align precisely with Poornima's lunar splendour.";
        if (link) link.textContent = "Astronomical Link: The complete lunar hemisphere reflects maximum solar light.";
    } else {
        if (btnKarva) btnKarva.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (icon) icon.textContent = "✨";
        if (heading) heading.textContent = "Karva Chauth";
        if (phaseTag) phaseTag.textContent = "Krishna Paksha Chaturthi (Waning Crescent Moon)";
        if (desc) desc.textContent = "Observed on the fourth day after Poornima. The daylong fast concludes only when the rising Moon is sighted through a delicate sieve and offerings of water are made.";
        if (link) link.textContent = "Astronomical Link: Precise timing depends on lunar moonrise in the late evening sky.";
    }
};

// SIM 13: Chandrayaan-3 Vikram Landing
window.executeVikramLanding = function() {
    const btn = document.getElementById('btnLandVikram');
    const lander = document.getElementById('vikramLanderGroup');
    const plume = document.getElementById('retroRocketPlume');
    const status = document.getElementById('vikramStatusText');

    if (!lander || !btn) return;

    btn.disabled = true;
    btn.textContent = "Landing in Progress...";
    if (plume) plume.setAttribute('opacity', '1');

    if (lander) {
        lander.style.transition = "transform 3s cubic-bezier(0.25, 0.46, 0.45, 0.94)";
        lander.setAttribute('transform', 'translate(0, 95)');
    }

    if (status) {
        status.textContent = "4 Throttleable Liquid Engines firing to arrest vertical velocity at 2 m/s...";
    }

    setTimeout(() => {
        if (plume) plume.setAttribute('opacity', '0');
        playSuccessChime();
        if (status) {
            status.textContent = "Touchdown Successful! Vikram soft-lands at 69.37° S near Shiv Shakti Point! India is the 1st nation near the Lunar South Pole!";
        }
        btn.textContent = "✅ Touchdown Accomplished!";
        btn.className = "px-3 py-1.5 rounded-xl bg-emerald-600 text-white font-bold text-xs transition";
    }, 3100);
};

// SIM 14: Pragyan Rover Surface Exploration
let roverDrivenDistance = 0;
window.drivePragyanRover = function() {
    const rover = document.getElementById('pragyanRoverGroup');
    const tracks = document.getElementById('pragyanTracksGroup');
    const status = document.getElementById('pragyanStatusText');

    roverDrivenDistance += 30;
    if (roverDrivenDistance > 240) roverDrivenDistance = 30;

    if (rover) {
        rover.style.transition = "transform 0.6s ease-out";
        rover.setAttribute('transform', `translate(${roverDrivenDistance}, 0)`);
    }

    if (tracks) {
        tracks.setAttribute('opacity', '1');
    }

    if (status) {
        status.textContent = `Pragyan Rover traversed ${roverDrivenDistance / 10} metres across lunar regolith, embossing Ashoka Pillar & ISRO insignia!`;
    }
};

window.fireLaserSpectroscope = function() {
    const beam = document.getElementById('roverLaserBeam');
    const spark = document.getElementById('laserSparkDot');
    const result = document.getElementById('spectralResultVal');

    if (beam) beam.setAttribute('opacity', '1');
    if (spark) spark.setAttribute('opacity', '1');
    playSuccessChime();

    setTimeout(() => {
        if (beam) beam.setAttribute('opacity', '0');
        if (spark) spark.setAttribute('opacity', '0');
        if (result) {
            result.textContent = "LIBS Spectrometer Confirmed: Sulfur (S), Aluminium (Al), Calcium (Ca), Iron (Fe), Titanium (Ti), and Oxygen (O) detected on lunar soil!";
        }
    }, 700);
};

// SIM 15: Apparent Solar Motion & Earth Axial Spin
let earthSpinAngle = 0;
window.rotateEarthPlanet = function() {
    earthSpinAngle += 45;
    const earthVisual = document.getElementById('earthGlobeVisual');
    if (earthVisual) {
        earthVisual.style.transition = "transform 0.8s ease-in-out";
        earthVisual.style.transform = `rotate(${earthSpinAngle}deg)`;
    }
    playSuccessChime();
};

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
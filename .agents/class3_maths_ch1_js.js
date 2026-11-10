// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 3 Mathematics - Chapter 1: What's in a Name?
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
                        <strong>Excellent Mathematical Thinking! Correct!</strong>
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
                        <strong>Let's Reflect Mathematically:</strong>
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
                            <strong>Let's Analyze the Math:</strong>
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

    modalTitle.textContent = `Mathematical Solution: ${targetQuestion.id.toUpperCase()}`;
    const steps = targetQuestion.solution_steps || {
        step1: "Observe the core numerical or categorical premise.",
        step2: "Apply the foundational counting or grouping rule.",
        step3: "Deduce the verified correct answer."
    };

    modalContent.innerHTML = `
        <div class="space-y-4">
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider">Question Context</span>
                <p class="text-xs sm:text-sm text-slate-200 mt-1">${targetQuestion.q}</p>
            </div>

            <div class="space-y-2.5">
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-800/40 text-xs">
                    <span class="font-bold text-cyan-300 block mb-1">Step 1: Problem Premise</span>
                    <p class="text-slate-300">${steps.step1}</p>
                </div>
                <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-800/40 text-xs">
                    <span class="font-bold text-blue-300 block mb-1">Step 2: Mathematical Rule</span>
                    <p class="text-slate-300">${steps.step2}</p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/40 text-xs">
                    <span class="font-bold text-emerald-300 block mb-1">Step 3: Verified Answer</span>
                    <p class="text-slate-300">${steps.step3}</p>
                </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
                <span class="text-xs text-slate-400">Correct Mathematical Option:</span>
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

// SIM 1: Pre-Numerical Counting (Pebble Correspondence)
let pastureCowsCount = 0;
window.dispatchCowToPasture = function() {
    if (pastureCowsCount >= 10) return;
    pastureCowsCount++;
    playSuccessChime();
    renderPastureState();
};

window.returnCowToCorral = function() {
    if (pastureCowsCount <= 0) return;
    pastureCowsCount--;
    playSuccessChime();
    renderPastureState();
};

function renderPastureState() {
    const mGroup = document.getElementById('meadowCattleGroup');
    const pJar = document.getElementById('pebbleJarDisplay');
    const badge = document.getElementById('pebbleCountBadge');
    const status = document.getElementById('correspondenceStatus');

    if (mGroup) {
        let cowsHtml = '';
        const positions = [
            [50, 70], [120, 80], [180, 60], [240, 90], [80, 140],
            [150, 150], [220, 140], [60, 190], [130, 195], [200, 190]
        ];
        for (let i = 0; i < pastureCowsCount; i++) {
            const [x, y] = positions[i] || [50 + i * 20, 100];
            cowsHtml += `<text x="${x}" y="${y}" font-size="24">🐄</text>`;
        }
        mGroup.innerHTML = cowsHtml;
    }

    if (pJar) {
        let pebblesHtml = '';
        for (let i = 0; i < pastureCowsCount; i++) {
            pebblesHtml += `<span class="w-4 h-4 rounded-full bg-amber-400 border border-amber-200 inline-block shadow"></span>`;
        }
        pJar.innerHTML = pebblesHtml;
    }

    if (badge) {
        badge.textContent = `${pastureCowsCount} Pebbles in Pot`;
    }

    if (status) {
        if (pastureCowsCount === 0) {
            status.innerHTML = "Corral is full! All cattle are inside. Pot is empty (0 pebbles).";
        } else {
            status.innerHTML = `<b>One-to-one match:</b> Exactly <b>${pastureCowsCount} cows</b> grazing in meadow paired with <b>${pastureCowsCount} pebbles</b> in the clay pot!`;
        }
    }
}

// SIM 2: Clay Wall Scratch Tally Simulator
let wallMarks = []; // items: { id, struck: bool }
window.addWallScratch = function() {
    if (wallMarks.length >= 16) return;
    wallMarks.push({ id: wallMarks.length, struck: false });
    playSuccessChime();
    renderWallMarks();
};

window.strikeWallScratch = function() {
    const unstruck = wallMarks.filter(m => !m.struck);
    if (unstruck.length === 0) return;
    unstruck[0].struck = true;
    playSuccessChime();
    renderWallMarks();
};

window.resetWallTally = function() {
    wallMarks = [];
    renderWallMarks();
};

function renderWallMarks() {
    const group = document.getElementById('wallMarksGroup');
    const outEl = document.getElementById('wallOutCount');
    const retEl = document.getElementById('wallReturnedCount');
    const uncEl = document.getElementById('wallUncancelledCount');
    const msg = document.getElementById('wallStatusMsg');

    const totalOut = wallMarks.length;
    const returned = wallMarks.filter(m => m.struck).length;
    const uncancelled = totalOut - returned;

    if (group) {
        let svgHtml = '';
        wallMarks.forEach((m, idx) => {
            const x = 30 + (idx * 24);
            svgHtml += `<line x1="${x}" y1="40" x2="${x}" y2="140" stroke="#fef3c7" stroke-width="4" stroke-linecap="round"/>`;
            if (m.struck) {
                svgHtml += `<line x1="${x - 8}" y1="45" x2="${x + 8}" y2="135" stroke="#ea580c" stroke-width="3" stroke-linecap="round"/>`;
            }
        });
        group.innerHTML = svgHtml;
    }

    if (outEl) outEl.textContent = totalOut;
    if (retEl) retEl.textContent = returned;
    if (uncEl) uncEl.textContent = uncancelled;

    if (msg) {
        if (totalOut === 0) {
            msg.textContent = "Clay wall is blank. Scratch a mark for each departing cow.";
        } else if (uncancelled === 0) {
            msg.textContent = `All ${totalOut} cows have returned! Every vertical stroke is safely struck through.`;
        } else {
            msg.textContent = `${uncancelled} uncancelled marks remaining! Exactly ${uncancelled} cows are still out in the field.`;
        }
    }
}

// SIM 3: Tracking Missing Cattle & Lantern Search Party
window.launchSearchParty = function() {
    const beam = document.getElementById('lanternBeamCone');
    const lostCows = document.getElementById('lostCowsGroup');
    const status = document.getElementById('searchRescueStatus');
    const btn = document.getElementById('btnSearchParty');

    if (beam) beam.setAttribute('opacity', '0.6');
    if (lostCows) lostCows.setAttribute('opacity', '1');
    playSuccessChime();

    if (btn) {
        btn.disabled = true;
        btn.textContent = "Rescuing Missing Cattle...";
    }

    if (status) {
        status.innerHTML = "Lantern beam illuminated the bamboo grove! <b>2 missing cows discovered safely!</b> Leading them back to the shed...";
    }

    setTimeout(() => {
        if (status) {
            status.innerHTML = " Touchdown at shed! All 10 cows are safely inside. <b>Both final wall marks struck through!</b>";
        }
        if (btn) {
            btn.textContent = " All Cattle Rescued Safely!";
            btn.className = "px-3 py-1.5 rounded-xl bg-emerald-600 text-white font-bold text-xs transition";
        }
    }, 2000);
};

// SIM 4: Modern 5-Bundle Tally Generator
window.updateTallyBundles = function(val) {
    const num = parseInt(val);
    const sliderNum = document.getElementById('tallySliderNum');
    const grid = document.getElementById('tallyBundlesGrid');
    const eqBox = document.getElementById('tallyEquationBox');
    const bText = document.getElementById('numBundlesText');
    const lText = document.getElementById('numLooseText');

    if (sliderNum) sliderNum.textContent = num;

    const fullBundles = Math.floor(num / 5);
    const loose = num % 5;

    if (grid) {
        let bundlesHtml = '';
        for (let b = 0; b < fullBundles; b++) {
            bundlesHtml += `
                <div class="relative w-16 h-20 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-center p-1">
                    <svg viewBox="0 0 60 70" class="w-full h-full">
                        <line x1="12" y1="12" x2="12" y2="58" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <line x1="22" y1="12" x2="22" y2="58" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <line x1="32" y1="12" x2="32" y2="58" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <line x1="42" y1="12" x2="42" y2="58" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <line x1="6" y1="58" x2="48" y2="12" stroke="#f43f5e" stroke-width="3.5" stroke-linecap="round"/>
                    </svg>
                    <span class="absolute bottom-1 right-1 text-[9px] font-bold text-emerald-400">5</span>
                </div>
            `;
        }

        if (loose > 0) {
            bundlesHtml += `
                <div class="relative w-16 h-20 bg-slate-900 border border-slate-800 rounded-lg flex items-center justify-center p-1">
                    <svg viewBox="0 0 60 70" class="w-full h-full">
            `;
            for (let l = 0; l < loose; l++) {
                const lx = 14 + (l * 10);
                bundlesHtml += `<line x1="${lx}" y1="12" x2="${lx}" y2="58" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>`;
            }
            bundlesHtml += `
                    </svg>
                    <span class="absolute bottom-1 right-1 text-[9px] font-bold text-amber-400">${loose}</span>
                </div>
            `;
        }
        grid.innerHTML = bundlesHtml;
    }

    if (eqBox) {
        let parts = [];
        for (let i = 0; i < fullBundles; i++) parts.push('5');
        if (loose > 0) parts.push(loose.toString());
        eqBox.textContent = `${parts.join(' + ')} = ${num}`;
    }

    if (bText) bText.textContent = `${fullBundles} bundle${fullBundles !== 1 ? 's' : ''} (${fullBundles * 5})`;
    if (lText) lText.textContent = `${loose} loose stroke${loose !== 1 ? 's' : ''}`;
};

// SIM 5: Animal Letter Teams
const animalTournamentData = [
    { name: "OX", count: 2, icon: "🐂" },
    { name: "RAT", count: 3, icon: "🐀" },
    { name: "DOG", count: 3, icon: "🐕" },
    { name: "LION", count: 4, icon: "🦁" },
    { name: "DEER", count: 4, icon: "🦌" },
    { name: "GOAT", count: 4, icon: "🐐" },
    { name: "TIGER", count: 5, icon: "🐅" },
    { name: "SNAKE", count: 5, icon: "🐍" },
    { name: "MONKEY", count: 6, icon: "🐒" },
    { name: "ELEPHANT", count: 8, icon: "🐘" }
];

window.filterAnimalTeams = function(team) {
    const grid = document.getElementById('animalCardsGrid');
    const summary = document.getElementById('teamSummaryText');
    const badge = document.getElementById('teamCountBadge');
    const btnAll = document.getElementById('btnTeamAll');
    const btnShort = document.getElementById('btnTeamShort');
    const btnLong = document.getElementById('btnTeamLong');

    [btnAll, btnShort, btnLong].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    let filtered = animalTournamentData;
    if (team === 'short') {
        filtered = animalTournamentData.filter(a => a.count <= 4);
        if (btnShort) btnShort.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (summary) summary.textContent = "Team Short: Animals with 4 or fewer letters in their written name.";
    } else if (team === 'long') {
        filtered = animalTournamentData.filter(a => a.count >= 5);
        if (btnLong) btnLong.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (summary) summary.textContent = "Team Long: Animals with 5 or more letters in their written name.";
    } else {
        if (btnAll) btnAll.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (summary) summary.textContent = "Displaying all 10 forest animals sorted by name letter count.";
    }

    if (badge) badge.textContent = `${filtered.length} Animals`;

    if (grid) {
        let cardsHtml = '';
        filtered.forEach(a => {
            cardsHtml += `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-center space-y-1">
                    <span class="text-2xl">${a.icon}</span>
                    <div class="text-xs font-bold text-white tracking-wide">${a.name}</div>
                    <div class="text-[10px] px-1.5 py-0.5 rounded ${a.count <= 4 ? 'bg-amber-500/20 text-amber-300' : 'bg-cyan-500/20 text-cyan-300'} font-semibold">${a.count} Letters</div>
                </div>
            `;
        });
        grid.innerHTML = cardsHtml;
    }
    playSuccessChime();
};

// SIM 6: Name Length Analysis Ruler
window.measurePresetName = function(name) {
    const container = document.getElementById('rulerBoxesContainer');
    const nameText = document.getElementById('measuredNameText');
    const lengthBadge = document.getElementById('measuredLengthBadge');
    const compText = document.getElementById('measuredComparisonText');

    if (nameText) nameText.textContent = name;
    const len = name.length;
    if (lengthBadge) lengthBadge.textContent = `${len} Units`;

    if (container) {
        let boxesHtml = '';
        for (let i = 0; i < len; i++) {
            boxesHtml += `
                <div class="w-10 h-12 bg-cyan-950/60 border-2 border-cyan-500 rounded-lg flex flex-col items-center justify-center shadow">
                    <span class="text-lg font-bold text-white">${name[i]}</span>
                    <span class="text-[9px] text-cyan-300 font-mono">${i + 1}</span>
                </div>
            `;
        }
        container.innerHTML = boxesHtml;
    }

    if (compText) {
        if (name === 'OM') compText.textContent = "Shortest name in sample (2 letters)";
        else if (name === 'SHRINATHAN') compText.textContent = "Longest name in sample (10 letters)";
        else compText.textContent = `${len - 2} letters longer than OM (2)`;
    }
    playSuccessChime();
};

// SIM 7: Alphabet Letter Frequencies
window.sortLetterFreq = function(mode) {
    const container = document.getElementById('freqDistributionContainer');
    const insight = document.getElementById('freqInsightText');
    const btnInit = document.getElementById('btnFreqInit');
    const btnVowel = document.getElementById('btnFreqVowel');

    if (mode === 'initial') {
        if (btnInit) btnInit.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (btnVowel) btnVowel.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
        if (container) {
            container.innerHTML = `
                <div class="space-y-2 text-xs">
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">A</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-emerald-500 h-full w-[40%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">4 (Aarav, Ananya, Amit, Anvi) ★ Mode</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">S</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-cyan-500 h-full w-[30%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">3 (Sanjay, Sunil, Simran)</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">P</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-indigo-500 h-full w-[20%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">2 (Priya, Pooja)</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">R</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-purple-500 h-full w-[10%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">1 (Rohan)</span>
                    </div>
                </div>
            `;
        }
        if (insight) insight.innerHTML = "Letter <b>A</b> is the statistical mode, starting 4 out of 10 student names!";
    } else {
        if (btnInit) btnInit.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
        if (btnVowel) btnVowel.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (container) {
            container.innerHTML = `
                <div class="space-y-2 text-xs">
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">A</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-emerald-500 h-full w-[70%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">14 occurrences ★ High Frequency</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">I</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-cyan-500 h-full w-[35%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">7 occurrences</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">O</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-indigo-500 h-full w-[20%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">4 occurrences</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <span class="w-8 font-bold text-amber-300">U</span>
                        <div class="flex-1 bg-slate-900 rounded-full h-4 overflow-hidden border border-slate-800">
                            <div class="bg-purple-500 h-full w-[10%] rounded-full"></div>
                        </div>
                        <span class="font-bold text-white">2 occurrences</span>
                    </div>
                </div>
            `;
        }
        if (insight) insight.innerHTML = "Vowel <b>A</b> occurs most frequently (14 times) across classroom names!";
    }
    playSuccessChime();
};

// SIM 8: Number Name Cards
window.inspectNumberCard = function(num, word, letters) {
    const detail = document.getElementById('cardInspectDetail');
    if (detail) {
        detail.innerHTML = `Selected Number: <b>${num}</b> (${word}). It has <b>${letters} alphabet letters</b>. Notice that 70 (SEVENTY, 7 letters) has fewer letters than 17 (SEVENTEEN, 9 letters)! Word length follows phonetic spelling, not numerical size.`;
    }
    playSuccessChime();
};

// SIM 9: Extreme Place Names
window.selectExtremePlace = function(place) {
    const display = document.getElementById('placeNameDisplay');
    const count = document.getElementById('placeLetterCount');
    const calc = document.getElementById('placeDiffCalculation');
    const btnL = document.getElementById('btnPlaceLong');
    const btnIb = document.getElementById('btnPlaceIb');
    const btnOd = document.getElementById('btnPlaceOd');

    [btnL, btnIb, btnOd].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    if (place === 'longest') {
        if (btnL) btnL.className = "px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition";
        if (display) display.textContent = "Venkatanarasimharajuvaripeta (Andhra Pradesh)";
        if (count) count.textContent = "28 Letters";
        if (calc) calc.innerHTML = "28 letters (AP) - 2 letters (Ib/Od) = <b>26 letters difference!</b> Longest railway name in India.";
    } else if (place === 'shortest_ib') {
        if (btnIb) btnIb.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (display) display.textContent = "Ib (Odisha, beside Ib River)";
        if (count) count.textContent = "2 Letters";
        if (calc) calc.innerHTML = "28 letters - 2 letters = <b>26 letters shorter</b> than Venkatanarasimharajuvaripeta!";
    } else {
        if (btnOd) btnOd.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (display) display.textContent = "Od (Anand District, Gujarat)";
        if (count) count.textContent = "2 Letters";
        if (calc) calc.innerHTML = "28 letters - 2 letters = <b>26 letters shorter</b> than Venkatanarasimharajuvaripeta!";
    }
    playSuccessChime();
};

// SIM 10: Number Word Riddles
window.testRiddleCandidate = function(cand, name, w1, w2, sum) {
    const candName = document.getElementById('riddleCandName');
    const tag = document.getElementById('riddleStatusTag');
    const elW1 = document.getElementById('riddleW1');
    const elW2 = document.getElementById('riddleW2');
    const elSum = document.getElementById('riddleSum');

    if (candName) candName.textContent = `${cand} ("${name}")`;
    const words = name.split(' ');
    const isSolved = (w1 === 5 && w2 === 5 && sum === 7);

    if (tag) {
        if (isSolved) {
            tag.className = "px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold";
            tag.textContent = "✅ Solves All Clues!";
            playSuccessChime();
        } else {
            tag.className = "px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30 font-bold";
            tag.textContent = "❌ Does Not Match All Clues";
            playErrorChime();
        }
    }

    if (elW1) elW1.textContent = `${words[0]} (${w1} letters) ${w1 === 5 ? '✅' : '❌'}`;
    if (elW2) elW2.textContent = `${words[1]} (${w2} letters) ${w2 === 5 ? '✅' : '❌'}`;
    if (elSum) elSum.textContent = `Digits sum to ${sum} ${sum === 7 ? '✅' : '❌'}`;
};

// SIM 11: Proximity to Hundred
window.updateProximityDistance = function(val) {
    const d = parseInt(val);
    const sliderVal = document.getElementById('distSliderVal');
    const leftText = document.getElementById('proxLeftText');
    const rightText = document.getElementById('proxRightText');
    const leftCir = document.getElementById('proxLeftCircle');
    const rightCir = document.getElementById('proxRightCircle');
    const eqL = document.getElementById('proxEqLeft');
    const eqR = document.getElementById('proxEqRight');

    const leftVal = 100 - d;
    const rightVal = 100 + d;

    if (sliderVal) sliderVal.textContent = `${d} Unit${d !== 1 ? 's' : ''}`;
    if (leftText) { leftText.textContent = leftVal; leftText.setAttribute('x', 250 - (d * 12)); }
    if (rightText) { rightText.textContent = rightVal; rightText.setAttribute('x', 250 + (d * 12)); }
    if (leftCir) leftCir.setAttribute('cx', 250 - (d * 12));
    if (rightCir) rightCir.setAttribute('cx', 250 + (d * 12));

    if (eqL) eqL.textContent = `100 - ${d} = ${leftVal}`;
    if (eqR) eqR.textContent = `100 + ${d} = ${rightVal}`;
};

// SIM 12: Living Things Classification
const livingCardsData = [
    { name: "Cow", icon: "🐄", eats: true, desc: "Eats fresh green grass" },
    { name: "Wooden Chair", icon: "🪑", eats: false, desc: "Non-living furniture" },
    { name: "Sparrow", icon: "🐦", eats: true, desc: "Pecks grain seeds" },
    { name: "Clay Pot", icon: "🏺", eats: false, desc: "Non-living earthen pot" },
    { name: "Elephant", icon: "🐘", eats: true, desc: "Eats sugarcane & leaves" },
    { name: "School Bag", icon: "🎒", eats: false, desc: "Non-living fabric item" },
    { name: "Goldfish", icon: "🐟", eats: true, desc: "Consumes water plants" },
    { name: "Pencil Box", icon: "✏️", eats: false, desc: "Non-living stationery" }
];

window.filterLivingCards = function(filter) {
    const grid = document.getElementById('livingCardsGrid');
    const summary = document.getElementById('livingCategorySummary');
    const badge = document.getElementById('livingCategoryBadge');
    const btnAll = document.getElementById('btnLivAll');
    const btnEat = document.getElementById('btnLivEat');
    const btnNo = document.getElementById('btnLivNo');

    [btnAll, btnEat, btnNo].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    let items = livingCardsData;
    if (filter === 'living') {
        items = livingCardsData.filter(i => i.eats);
        if (btnEat) btnEat.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (summary) summary.textContent = "Category A: Living creatures that eat food and grow.";
    } else if (filter === 'nonliving') {
        items = livingCardsData.filter(i => !i.eats);
        if (btnNo) btnNo.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (summary) summary.textContent = "Category B: Non-living items that do not consume food.";
    } else {
        if (btnAll) btnAll.className = "px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition";
        if (summary) summary.textContent = "Displaying all 8 items categorized by biological nourishment.";
    }

    if (badge) badge.textContent = `${items.length} Items`;

    if (grid) {
        let cardsHtml = '';
        items.forEach(c => {
            cardsHtml += `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-center space-y-1">
                    <span class="text-2xl">${c.icon}</span>
                    <div class="text-xs font-bold text-white">${c.name}</div>
                    <div class="text-[10px] ${c.eats ? 'text-emerald-400' : 'text-slate-400'}">${c.desc}</div>
                </div>
            `;
        });
        grid.innerHTML = cardsHtml;
    }
    playSuccessChime();
};

// SIM 13: Electric Appliance Sorting
const applianceCardsData = [
    { name: "Ceiling Fan", icon: "🌀", electric: true, desc: "Electric motor spins blades" },
    { name: "Wooden Broom", icon: "🧹", electric: false, desc: "Manual sweeping action" },
    { name: "Refrigerator", icon: "🧊", electric: true, desc: "Electric compressor cooling" },
    { name: "Steel Spoon", icon: "🥄", electric: false, desc: "Manual scooping utensil" },
    { name: "Television", icon: "📺", electric: true, desc: "Electric circuit display" },
    { name: "Water Bucket", icon: "🪣", electric: false, desc: "Manual liquid container" },
    { name: "Table Lamp", icon: "💡", electric: true, desc: "Electric bulb illumination" },
    { name: "Claw Hammer", icon: "🔨", electric: false, desc: "Manual striking tool" }
];

window.filterApplianceCards = function(filter) {
    const grid = document.getElementById('applianceCardsGrid');
    const summary = document.getElementById('applianceSummaryText');
    const badge = document.getElementById('applianceBadgeText');
    const btnAll = document.getElementById('btnAppAll');
    const btnElec = document.getElementById('btnAppElec');
    const btnMan = document.getElementById('btnAppMan');

    [btnAll, btnElec, btnMan].forEach(b => {
        if (b) b.className = "px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition";
    });

    let items = applianceCardsData;
    if (filter === 'electric') {
        items = applianceCardsData.filter(i => i.electric);
        if (btnElec) btnElec.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (summary) summary.textContent = "Group 1: Household appliances requiring electrical power.";
    } else if (filter === 'manual') {
        items = applianceCardsData.filter(i => !i.electric);
        if (btnMan) btnMan.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (summary) summary.textContent = "Group 2: Manual tools operated by human muscle power.";
    } else {
        if (btnAll) btnAll.className = "px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition";
        if (summary) summary.textContent = "Showing all 8 household tools categorized by operating energy.";
    }

    if (badge) badge.textContent = `${items.length} Items`;

    if (grid) {
        let cardsHtml = '';
        items.forEach(c => {
            cardsHtml += `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-center space-y-1">
                    <span class="text-2xl">${c.icon}</span>
                    <div class="text-xs font-bold text-white">${c.name}</div>
                    <div class="text-[10px] ${c.electric ? 'text-cyan-300' : 'text-slate-400'}">${c.desc}</div>
                </div>
            `;
        });
        grid.innerHTML = cardsHtml;
    }
    playSuccessChime();
};

// SIM 14: Hairstyle Data Collection
let hairSurveyData = { ponytails: 0, single_pony: 0, braids: 0, short: 0, curls: 0 };
window.recordHairstyleVote = function(style) {
    if (!hairSurveyData.hasOwnProperty(style)) return;
    hairSurveyData[style]++;
    playSuccessChime();
    renderHairSurvey();
};

window.resetHairstyleSurvey = function() {
    hairSurveyData = { ponytails: 0, single_pony: 0, braids: 0, short: 0, curls: 0 };
    renderHairSurvey();
};

function renderHairSurvey() {
    const elPonytails = document.getElementById('countPonytails');
    const elSinglePony = document.getElementById('countSinglePony');
    const elBraids = document.getElementById('countBraids');
    const elShort = document.getElementById('countShort');
    const elCurls = document.getElementById('countCurls');
    const elTotal = document.getElementById('totalSurveyCount');

    if (elPonytails) elPonytails.textContent = `${hairSurveyData.ponytails} Recorded`;
    if (elSinglePony) elSinglePony.textContent = `${hairSurveyData.single_pony} Recorded`;
    if (elBraids) elBraids.textContent = `${hairSurveyData.braids} Recorded`;
    if (elShort) elShort.textContent = `${hairSurveyData.short} Recorded`;
    if (elCurls) elCurls.textContent = `${hairSurveyData.curls} Recorded`;

    const total = Object.values(hairSurveyData).reduce((a, b) => a + b, 0);
    if (elTotal) elTotal.textContent = `${total} Students`;
}

// SIM 16: Pictograph Data Displays
const pictographSurveyCounts = [
    { label: "Short Hair", count: 8, icon: "👦" },
    { label: "Two Ponytails", count: 6, icon: "👧" },
    { label: "Braids", count: 5, icon: "🧕" },
    { label: "Single Ponytail", count: 4, icon: "👱‍♀️" },
    { label: "Curly Hair", count: 2, icon: "🧑‍🦱" }
];

window.updatePictographScale = function(scaleVal) {
    const scale = parseInt(scaleVal); // 1 or 2
    const container = document.getElementById('pictographRowsContainer');
    const summary = document.getElementById('pictoSummaryText');

    if (container) {
        let rowsHtml = '';
        pictographSurveyCounts.forEach(r => {
            const numIcons = Math.ceil(r.count / scale);
            let iconsHtml = '';
            for (let i = 0; i < numIcons; i++) {
                iconsHtml += `<span class="text-base" title="1 icon = ${scale} student(s)">😊</span>`;
            }
            rowsHtml += `
                <div class="flex flex-col sm:flex-row sm:items-center justify-between p-2 rounded-lg bg-slate-900 border border-slate-800 gap-2">
                    <span class="w-32 font-bold text-xs text-white flex items-center gap-1.5">${r.icon} ${r.label}</span>
                    <div class="flex items-center gap-1.5 flex-wrap">${iconsHtml}</div>
                    <span class="text-xs font-mono font-bold text-cyan-300 w-16 text-right">${r.count} students</span>
                </div>
            `;
        });
        container.innerHTML = rowsHtml;
    }

    if (summary) {
        if (scale === 1) {
            summary.innerHTML = "Key: <b>😊 = 1 student</b>. Short hair has the longest row (8 icons).";
        } else {
            summary.innerHTML = "Key: <b>😊 = 2 students</b>. Short hair row has 4 icons (4 × 2 = 8 students).";
        }
    }
    playSuccessChime();
};

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);

    // Initialize Simulators
    renderPastureState();
    renderWallMarks();
    updateTallyBundles(17);
    filterAnimalTeams('all');
    measurePresetName('PRIYA');
    sortLetterFreq('initial');
    filterLivingCards('all');
    filterApplianceCards('all');
    renderHairSurvey();
    updatePictographScale(1);
});
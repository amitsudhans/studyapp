"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 7: Energy - How Things Work
Enhanced with Indian Male Voice priority, female voice filtering, Voice Selector UI,
modal solution system, checkpoint handling, and 16 bespoke simulators.
Zero raw LaTeX! Clean Unicode symbols.
"""

JS_CODE = r'''
// Global State
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis State
let speechQueue = [];
let speechQueueIndex = 0;
let isSpeaking = false;
let currentSlideSpeaking = null;
let selectedMaleVoice = null;

// Comprehensive Female Filter Keywords
const femaleKeywords = [
    'female', 'zira', 'jenny', 'aria', 'samantha', 'victoria', 'karen', 'susan',
    'neerja', 'heera', 'hazel', 'catherine', 'linda', 'eva', 'ava', 'siri',
    'swara', 'veena', 'priya', 'kalpana', 'shruti', 'sunita', 'aditi', 'anjali',
    'geeta', 'roshni', 'meera', 'rekha', 'rani', 'woman', 'girl'
];

function isFemaleVoice(v) {
    const name = (v.name || '').toLowerCase();
    return femaleKeywords.some(fk => name.includes(fk));
}

// Dedicated Indian Male Voice Selector
function getIndianMaleVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    // Explicit Indian Male names across Edge, Windows, Mac, Android, Chrome
    const explicitIndianMale = [
        'prabhat', 'rishi', 'ravi', 'madhav', 'pradeep', 'karan', 'amit', 'anil',
        'ajay', 'deepak', 'mohan', 'hemant', 'aravind', 'arun', 'madhur'
    ];

    // Filter Indian voices (en-IN or containing india/hindi)
    const inVoices = voices.filter(v =>
        (v.lang && (v.lang.toLowerCase() === 'en-in' || v.lang.toLowerCase().startsWith('en_in') || v.lang.toLowerCase() === 'hi-in')) ||
        (v.name && v.name.toLowerCase().includes('india'))
    );

    // 1. Priority 1: Indian voice matching explicit male name and NOT female
    for (const mk of explicitIndianMale) {
        const match = inVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemaleVoice(v));
        if (match) return match;
    }

    // 2. Priority 2: Indian voice containing 'male' in name and NOT female
    const inMale = inVoices.find(v => (v.name || '').toLowerCase().includes('male') && !isFemaleVoice(v));
    if (inMale) return inMale;

    // 3. Priority 3: Any Indian voice that is not marked female (excluding Google Indian English which is female)
    const anyInNonFemale = inVoices.find(v => !isFemaleVoice(v) && !(v.name || '').toLowerCase().includes('google indian english'));
    if (anyInNonFemale) return anyInNonFemale;

    // 4. Priority 4: Authoritative English Male voices (deep, resonant baritone when pitched)
    const enVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    const generalMaleKeywords = ['male', 'david', 'mark', 'george', 'daniel', 'guy', 'stefan', 'oliver', 'arthur', 'james', 'richard', 'brian', 'sean', 'alex', 'fred', 'neil'];
    for (const mk of generalMaleKeywords) {
        const match = enVoices.find(v => (v.name || '').toLowerCase().includes(mk) && !isFemaleVoice(v));
        if (match) return match;
    }

    // 5. Priority 5: Any non-female English voice
    const nonFemale = enVoices.find(v => !isFemaleVoice(v));
    if (nonFemale) return nonFemale;

    // 6. Absolute Fallback
    return inVoices[0] || voices[0] || null;
}

function populateVoiceList() {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    const select = document.getElementById("voiceSelect");
    if (!select || voices.length === 0) return;

    select.innerHTML = "";
    if (!selectedMaleVoice) {
        selectedMaleVoice = getIndianMaleVoice();
    }

    voices.forEach((v, idx) => {
        const opt = document.createElement("option");
        opt.value = idx;
        const isSelected = selectedMaleVoice && selectedMaleVoice.name === v.name;
        let prefix = "🎙️ ";
        if ((v.lang && v.lang.toLowerCase().includes("in")) || (v.name && v.name.toLowerCase().includes("india"))) {
            prefix = isFemaleVoice(v) ? "🇮🇳 (Female) " : "🇮🇳 (Male) ";
        } else if (isFemaleVoice(v)) {
            prefix = "👩 ";
        } else {
            prefix = "👨 ";
        }
        opt.textContent = prefix + v.name + " (" + v.lang + ")";
        if (isSelected) opt.selected = true;
        select.appendChild(opt);
    });
}

function onUserVoiceChange(idxStr) {
    if (idxStr === "") return;
    const voices = window.speechSynthesis.getVoices();
    const idx = parseInt(idxStr, 10);
    if (voices[idx]) {
        selectedMaleVoice = voices[idx];
    }
}

if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        selectedMaleVoice = getIndianMaleVoice();
        populateVoiceList();
    };
    selectedMaleVoice = getIndianMaleVoice();
}

function stopCurrentSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    speechQueue = [];
    speechQueueIndex = 0;
    updateAudioUI(false);
}

function updateAudioUI(speaking) {
    const globalBtn = document.getElementById("globalSpeechBtn");
    if (globalBtn) {
        globalBtn.innerHTML = speaking ? "<span>⏸️</span><span>Pause Audio</span>" : "<span>▶</span><span>Play Slide Audio</span>";
        if (speaking) {
            globalBtn.classList.add("bg-amber-500/30", "border-amber-500");
        } else {
            globalBtn.classList.remove("bg-amber-500/30", "border-amber-500");
        }
    }
    if (currentSlideSpeaking) {
        const badge = document.getElementById("slide-audio-badge-" + currentSlideSpeaking);
        const btn = document.getElementById("slide-audio-btn-" + currentSlideSpeaking);
        if (badge) {
            badge.textContent = speaking ? "Narrating..." : "Audio Lecture Ready";
            badge.className = speaking ? "px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 animate-pulse" : "px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30";
        }
        if (btn) {
            btn.innerHTML = speaking ? "<span>⏸️</span><span>Pause Lecture</span>" : "<span>▶</span><span>Listen to Full Lecture</span>";
        }
    }
}

function speakNextSentence() {
    if (speechQueueIndex >= speechQueue.length) {
        isSpeaking = false;
        updateAudioUI(false);
        return;
    }
    const text = speechQueue[speechQueueIndex++];
    if (!text || text.trim().length === 0) {
        speakNextSentence();
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text.trim());
    if (!selectedMaleVoice) {
        selectedMaleVoice = getIndianMaleVoice();
    }
    if (selectedMaleVoice) {
        utterance.voice = selectedMaleVoice;
    }
    utterance.rate = 0.94;
    utterance.pitch = 0.85; // Deep, authoritative masculine lecture baritone

    utterance.onend = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };
    utterance.onerror = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };
    window.speechSynthesis.speak(utterance);
}

function startLectureSpeech(rawText, slideNo) {
    if (isSpeaking && currentSlideSpeaking === slideNo) {
        stopCurrentSpeech();
        return;
    }
    stopCurrentSpeech();
    if (!rawText || rawText.trim().length === 0) return;

    currentSlideSpeaking = slideNo;
    isSpeaking = true;
    updateAudioUI(true);

    const sentences = rawText.match(/[^.!?]+[.!?]+/g) || [rawText];
    speechQueue = sentences.map(s => s.trim()).filter(s => s.length > 0);
    speechQueueIndex = 0;
    speakNextSentence();
}

function toggleCurrentSlideLecture() {
    if (isSpeaking) {
        stopCurrentSpeech();
    } else {
        const spokenDiv = document.getElementById("slide-spoken-text-" + currentSlide);
        if (spokenDiv && spokenDiv.textContent) {
            startLectureSpeech(spokenDiv.textContent, currentSlide);
        }
    }
}

// Slide Navigation
function showSlide(slideNo) {
    if (slideNo < 1 || slideNo > totalSlides) return;
    stopCurrentSpeech();

    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById("slide-" + i);
        if (el) el.style.display = (i === slideNo) ? "block" : "none";
    }

    currentSlide = slideNo;

    const counter = document.getElementById("slideCounter");
    if (counter) counter.textContent = currentSlide + " / " + totalSlides;

    const select = document.getElementById("slideJumpSelect");
    if (select) select.value = currentSlide;

    const prevBtn = document.getElementById("prevBtn");
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);

    const nextBtn = document.getElementById("nextBtn");
    const lastNotice = document.getElementById("lastSlideNotice");

    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = "none";
        if (lastNotice) lastNotice.classList.remove("hidden");
    } else {
        if (nextBtn) nextBtn.style.display = "inline-flex";
        if (lastNotice) lastNotice.classList.add("hidden");
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
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

function goToSlide(n) {
    showSlide(n);
}

// Formative Checkpoint Verification
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const feedbackBox = document.getElementById("cp-feedback-" + cpId);
    if (!feedbackBox) return;

    feedbackBox.classList.remove("hidden");
    if (selectedIdx === correctIdx) {
        feedbackBox.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs mt-2";
        feedbackBox.innerHTML = "<strong>✅ Correct!</strong> " + explanation;
    } else {
        feedbackBox.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-300 text-xs mt-2";
        feedbackBox.innerHTML = "<strong>❌ Not quite.</strong> " + explanation;
    }
}

// Mastery Quiz Selection
function selectQuizOption(qId, selectedIdx, correctIdx, title, question, explanation) {
    const fb = document.getElementById("q-fb-" + qId);
    const solBtn = document.getElementById("q-sol-btn-" + qId);
    if (fb) {
        fb.classList.remove("hidden");
        if (selectedIdx === correctIdx) {
            fb.className = "p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs mt-2";
            fb.innerHTML = "<strong>✅ Excellent!</strong> " + explanation;
        } else {
            fb.className = "p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-300 text-xs mt-2";
            fb.innerHTML = "<strong>❌ Incorrect.</strong> Review the concept or click 'View Solution'.";
        }
    }
    if (solBtn) {
        solBtn.classList.remove("hidden");
        solBtn.classList.add("inline-flex");
    }
}

// Solution Modal Handlers
function openSolutionModal(title, question, solutionHtml) {
    const modal = document.getElementById("solutionModal");
    const modalTitle = document.getElementById("modalTitle");
    const modalQuestion = document.getElementById("modalQuestion");
    const modalBody = document.getElementById("modalBody");

    if (modalTitle) modalTitle.textContent = title;
    if (modalQuestion) modalQuestion.innerHTML = "<strong>Inquiry:</strong> " + question;
    if (modalBody) modalBody.innerHTML = solutionHtml;
    if (modal) {
        modal.classList.remove("hidden");
        modal.classList.add("flex");
    }
}

function closeSolutionModal() {
    const modal = document.getElementById("solutionModal");
    if (modal) {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
    }
}

// ==================== 16 BESPOKE SIMULATOR INTERACTIVE ENGINES ====================

// SIM 1: Energy Transformer Matrix
function activateSim1Mode(mode) {
    const title = document.getElementById('sim1EffectTitle');
    const desc = document.getElementById('sim1EffectDesc');
    const status = document.getElementById('sim1Status');

    if (mode === 'motion') {
        if (title) title.textContent = 'Kinetic Motion (Work)';
        if (desc) desc.textContent = 'Forces mass into acceleration (E = 0.5mv²)';
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Kinetic Energy:</span> Moving vehicles, swinging hammers, and running legs possess kinetic energy that performs active physical work!';
        }
    } else if (mode === 'light') {
        if (title) title.textContent = 'Radiant Light (Photons)';
        if (desc) desc.textContent = 'Electromagnetic waves illuminate space';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Light Energy:</span> The Sun, lamps, and stars emit electromagnetic radiation, allowing our eyes to see and plants to perform photosynthesis!';
        }
    } else if (mode === 'sound') {
        if (title) title.textContent = 'Acoustic Sound Waves';
        if (desc) desc.textContent = 'Pressure vibrations through air medium';
        if (status) {
            status.innerHTML = '<span class="text-purple-400 font-bold">Sound Energy:</span> Mechanical oscillations strike air particles, creating compression waves that travel to our eardrums as music or speech!';
        }
    } else if (mode === 'heat') {
        if (title) title.textContent = 'Thermal Heat Energy';
        if (desc) desc.textContent = 'Microscopic molecular kinetic excitation';
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Thermal Energy:</span> Heat flows from warmer to cooler bodies, speeding up internal molecular jiggling and causing temperature changes!';
        }
    }
}

// SIM 2: Balloon Air Rocket Launcher (Activity 1)
let balloonInflated = false;
function inflateBalloon() {
    balloonInflated = true;
    const body = document.getElementById('balloonBody');
    const neck = document.getElementById('balloonNeck');
    const speedText = document.getElementById('rocketSpeedText');
    const jet = document.getElementById('airJetStream');
    const status = document.getElementById('sim2Status');
    const assembly = document.getElementById('balloonRocketAssembly');

    if (assembly) assembly.style.transform = 'translate(50px, 120px)';
    if (body) {
        body.setAttribute('rx', '45');
        body.setAttribute('ry', '30');
    }
    if (neck) {
        neck.setAttribute('points', '-45,32 -60,26 -60,44 -45,38');
    }
    if (jet) jet.classList.add('opacity-0');
    if (speedText) speedText.textContent = 'Stored: High Potential';
    if (status) {
        status.innerHTML = '<span class="text-amber-400 font-bold">Air Compressed:</span> The rubber balloon is stretched tight, storing elastic potential energy waiting to propel the rocket forward!';
    }
}

function launchBalloonRocket() {
    if (!balloonInflated) {
        inflateBalloon();
        setTimeout(launchBalloonRocket, 600);
        return;
    }
    balloonInflated = false;
    const assembly = document.getElementById('balloonRocketAssembly');
    const jet = document.getElementById('airJetStream');
    const body = document.getElementById('balloonBody');
    const speedText = document.getElementById('rocketSpeedText');
    const status = document.getElementById('sim2Status');

    if (jet) jet.classList.remove('opacity-0');
    if (speedText) speedText.textContent = 'Speed: 4.8 m/s (Thrust!)';

    if (assembly) {
        assembly.style.transition = 'transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1)';
        assembly.style.transform = 'translate(310px, 120px)';
    }

    setTimeout(() => {
        if (body) {
            body.setAttribute('rx', '15');
            body.setAttribute('ry', '12');
        }
        if (jet) jet.classList.add('opacity-0');
        if (speedText) speedText.textContent = 'Distance: 10 m (Arrived)';
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Newton\'s Law:</span> As compressed air rushed backward, an equal and opposite forward reaction thrust launched the rocket across the room!';
        }
    }, 800);
}

// SIM 3: Rubber Band Guitar Frequency & Pitch Lab (Activity 2)
function pluckString(num) {
    const freqText = document.getElementById('freqMeterText');
    const pitchText = document.getElementById('pitchDescText');
    const status = document.getElementById('sim3Status');
    const str = document.getElementById('rubberStr' + num);

    if (str) {
        str.style.transform = 'scaleY(2.5)';
        str.style.transition = 'transform 0.1s ease-in-out';
        setTimeout(() => { str.style.transform = 'scaleY(1)'; }, 150);
    }

    if (num === 1) {
        if (freqText) freqText.textContent = '440 Hz (A4 Note)';
        if (pitchText) pitchText.textContent = 'High Pitch (Fast Vibrations)';
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Thin Band (440 Hz):</span> Less mass per unit length allows the thin band to oscillate 440 times per second, producing a crisp, high-pitched musical note!';
        }
    } else if (num === 2) {
        if (freqText) freqText.textContent = '261 Hz (Middle C)';
        if (pitchText) pitchText.textContent = 'Medium Frequency / Tone';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Medium Band (261 Hz):</span> Moderate tension and mass produce Middle C, resonating clearly inside the cardboard soundbox!';
        }
    } else {
        if (freqText) freqText.textContent = '110 Hz (A2 Bass)';
        if (pitchText) pitchText.textContent = 'Deep Bass Tone (Slow Wave)';
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Thick Band (110 Hz):</span> Greater mass resists rapid acceleration, oscillating more slowly to produce a deep, rumbling acoustic bass!';
        }
    }
}

// SIM 4: Solar Water Heating & Molecular Thermometer (Activity 3)
function updateSolarHeating(mins) {
    const m = parseInt(mins);
    const label = document.getElementById('sunTimeLabel');
    const tempB = document.getElementById('tempTextB');
    const liquidB = document.getElementById('thermoLiquidB');
    const status = document.getElementById('sim4Status');

    // Temperature rises from 24°C up to 40°C over 120 mins
    const calculatedTemp = 24 + Math.round((m / 120) * 16);
    if (label) {
        label.textContent = m + ' Minutes (' + (m >= 90 ? 'High Heat' : m >= 40 ? 'Warming' : 'Initial') + ')';
    }
    if (tempB) {
        tempB.textContent = calculatedTemp + '°C';
    }
    if (liquidB) {
        // Height expands upward
        const h = 25 + Math.round((m / 120) * 30);
        const y = 140 - h;
        liquidB.setAttribute('y', y);
        liquidB.setAttribute('height', h);
    }
    if (status) {
        status.innerHTML = '<span class="text-amber-400 font-bold">Thermal Rise:</span> Bowl A in shade remains at 24°C, while Bowl B in sunlight warmed to ' + calculatedTemp + '°C by absorbing radiant infrared photons!';
    }
}

// SIM 5: Human Food Battery & Metabolism Lab
let currentCharge = 85;
function performActivity(act) {
    const fill = document.getElementById('batteryFill');
    const text = document.getElementById('batteryPctText');
    const status = document.getElementById('sim5Status');

    if (act === 'eat') {
        currentCharge = Math.min(100, currentCharge + 25);
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Meal Digested:</span> Nutrients broken down into glucose recharge liver glycogen and muscle energy stores to ' + currentCharge + '%!';
        }
    } else if (act === 'run') {
        currentCharge = Math.max(10, currentCharge - 30);
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">High Exertion:</span> Running sprint burns glucose rapidly through cellular respiration with oxygen, dropping reserve to ' + currentCharge + '%!';
        }
    } else if (act === 'study') {
        currentCharge = Math.max(10, currentCharge - 10);
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Mental Focus:</span> The human brain consumes 20% of resting metabolic glucose energy while studying, leaving battery at ' + currentCharge + '%!';
        }
    }

    if (text) text.textContent = currentCharge + '%';
    if (fill) {
        const h = Math.round((currentCharge / 100) * 98);
        const y = 123 - h;
        fill.setAttribute('height', h);
        fill.setAttribute('y', y);
        fill.setAttribute('fill', currentCharge > 50 ? '#22c55e' : currentCharge > 25 ? '#f59e0b' : '#ef4444');
    }
}

// SIM 6: Combustion Engine Cylinder Lab
let fuelInjected = false;
function injectFuel() {
    fuelInjected = true;
    const cycleText = document.getElementById('engineCycleText');
    const status = document.getElementById('sim6Status');
    const fire = document.getElementById('fireChamber');
    if (fire) fire.style.opacity = '0';
    if (cycleText) cycleText.textContent = 'Fuel/Air Injected';
    if (status) {
        status.innerHTML = '<span class="text-cyan-400 font-bold">Intake Stroke:</span> A fine atomized mist of petrol and atmospheric oxygen enters the cylinder, ready for compression.';
    }
}

function sparkIgnite() {
    if (!fuelInjected) {
        injectFuel();
        setTimeout(sparkIgnite, 400);
        return;
    }
    fuelInjected = false;
    const spark = document.getElementById('sparkIgnition');
    const fire = document.getElementById('fireChamber');
    const piston = document.getElementById('pistonGroup');
    const cycleText = document.getElementById('engineCycleText');
    const status = document.getElementById('sim6Status');

    if (spark) spark.classList.remove('opacity-0');
    if (fire) fire.style.opacity = '0.9';
    if (cycleText) cycleText.textContent = 'POWER STROKE!';

    if (piston) {
        piston.style.transform = 'translate(150px, 110px)';
    }

    setTimeout(() => {
        if (spark) spark.classList.add('opacity-0');
        if (fire) fire.style.opacity = '0';
        if (piston) piston.style.transform = 'translate(150px, 70px)';
        if (cycleText) cycleText.textContent = 'Shaft Spun (Cycle Complete)';
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Power Stroke Triumph:</span> Chemical combustion generated expanding gas that pushed the piston down, turning the crankshaft to drive the wheels!';
        }
    }, 600);
}

// SIM 7: Diya Capillary Siphon & Flame Chemistry (Activity 4)
function toggleOilLevel(level) {
    const reservoir = document.getElementById('diyaOilReservoir');
    const flame = document.getElementById('diyaFlame');
    const statusText = document.getElementById('oilStatusText');
    const arrows = document.getElementById('capillaryArrows');
    const status = document.getElementById('sim7Status');

    if (level === 'empty') {
        if (reservoir) reservoir.setAttribute('opacity', '0.1');
        if (flame) flame.style.display = 'none';
        if (arrows) arrows.classList.add('opacity-0');
        if (statusText) {
            statusText.textContent = 'Oil Level: Exhausted';
            statusText.style.color = '#ef4444';
        }
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Flame Extinguished:</span> Without liquid oil fuel climbing the wick, the cotton thread chars and the flame goes out immediately!';
        }
    } else {
        if (reservoir) reservoir.setAttribute('opacity', '0.8');
        if (flame) flame.style.display = 'inline';
        if (arrows) arrows.classList.remove('opacity-0');
        if (statusText) {
            statusText.textContent = 'Oil Level: Full';
            statusText.style.color = '#eab308';
        }
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Capillary Action:</span> Microscopic pores draw liquid oil upward to the tip, where it vaporizes and combusts with a steady golden flame!';
        }
    }
}

// SIM 8: Universal Electric Circuit & Appliance Hub
let circuitSwitchClosed = false;
let currentAppliance = 'motor';

function toggleCircuitSwitch() {
    circuitSwitchClosed = !circuitSwitchClosed;
    const knife = document.getElementById('switchKnife');
    const text = document.getElementById('switchText');
    const dots = document.getElementById('electronDots');
    const aura = document.getElementById('applianceAura');
    const status = document.getElementById('sim8Status');

    if (circuitSwitchClosed) {
        if (knife) knife.setAttribute('y2', '0');
        if (text) {
            text.textContent = 'Switch: CLOSED (ON)';
            text.style.fill = '#4ade80';
        }
        if (dots) dots.classList.remove('opacity-0');
        if (aura) aura.setAttribute('opacity', '0.6');
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Current Flowing:</span> Continuous conductive loop allows electrons to drift, powering the ' + currentAppliance + '!';
        }
    } else {
        if (knife) knife.setAttribute('y2', '-18');
        if (text) {
            text.textContent = 'Switch: OPEN (OFF)';
            text.style.fill = '#94a3b8';
        }
        if (dots) dots.classList.add('opacity-0');
        if (aura) aura.setAttribute('opacity', '0.1');
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Circuit Broken:</span> Air gap halts electron drift instantly, terminating power delivery.';
        }
    }
}

function setAppliance(app) {
    currentAppliance = app;
    const icon = document.getElementById('applianceIcon');
    const name = document.getElementById('applianceName');
    const status = document.getElementById('sim8Status');

    if (app === 'motor') {
        if (icon) icon.textContent = '🌀';
        if (name) name.textContent = 'Electric Motor (Motion)';
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Kinetic Rotation:</span> Electromagnetic forces in the motor spin fans, washing machine drums, and vehicle wheels!';
        }
    } else if (app === 'heater') {
        if (icon) icon.textContent = '♨️';
        if (name) name.textContent = 'Nichrome Coil (Heat)';
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Joule Heating:</span> High electrical resistance in the coil generates soothing heat for toasters and geysers!';
        }
    } else if (app === 'bulb') {
        if (icon) icon.textContent = '💡';
        if (name) name.textContent = 'Solid-State LED (Light)';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Electroluminescence:</span> Semiconductor chips emit cool, brilliant visible light with maximum efficiency!';
        }
    }
}

// SIM 9: Filament Bulb vs Modern LED Duel
function toggleBulbComparison(type) {
    const status = document.getElementById('sim9Status');
    if (type === 'filament') {
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Filament Inefficiency:</span> The 60W tungsten bulb forces wire to over 2,500°C. 90% of electricity is wasted as scorching heat!';
        }
    } else {
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">LED Efficiency:</span> The 9W solid-state LED stays cool, converting over 80% of current directly into bright light, saving 85% energy!';
        }
    }
}

// SIM 10: Electric Safety Simulator & MCB Circuit Breaker
let isWetHands = false;
function setHandMoisture(wet) {
    isWetHands = wet;
    const icon = document.getElementById('skinStateIcon');
    const text = document.getElementById('skinStateText');
    const resText = document.getElementById('skinResistanceText');
    const status = document.getElementById('sim10Status');

    if (wet) {
        if (icon) icon.textContent = '💧✋';
        if (text) {
            text.textContent = 'WET (LETHAL HAZARD!)';
            text.style.color = '#ef4444';
        }
        if (resText) resText.textContent = '< 1,000 Ω (Extreme Danger)';
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">ELECTRICAL DANGER:</span> Wet skin lowers resistance below 1,000 ohms! Touching any switch can deliver a fatal shock. Never touch switches with wet hands!';
        }
    } else {
        if (icon) icon.textContent = '✋';
        if (text) {
            text.textContent = 'Dry (Safe)';
            text.style.color = '#34d399';
        }
        if (resText) resText.textContent = '100,000 Ω';
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Safe Resistance:</span> Dry skin provides high natural resistance against minor static discharges, but always use insulated footwear!';
        }
    }
}

function simulateCircuitOverload() {
    const mcbLever = document.getElementById('mcbLever');
    const mcbText = document.getElementById('mcbStateText');
    const loadText = document.getElementById('currentLoadText');
    const loadStatus = document.getElementById('loadStatusText');
    const status = document.getElementById('sim10Status');

    if (loadText) {
        loadText.textContent = '28 A (Surge!)';
        loadText.style.color = '#ef4444';
    }
    if (loadStatus) loadStatus.textContent = 'OVERLOAD DETECTED';

    setTimeout(() => {
        if (mcbLever) {
            mcbLever.setAttribute('y', '50');
            mcbLever.setAttribute('fill', '#ef4444');
        }
        if (mcbText) {
            mcbText.textContent = 'MCB: TRIPPED (OFF)';
            mcbText.style.fill = '#ef4444';
        }
        if (loadText) {
            loadText.textContent = '0 A (Safe)';
            loadText.style.color = '#34d399';
        }
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Automatic Safety Trip:</span> The MCB electromagnet detected dangerous current overload and instantly popped open, preventing house wire fires!';
        }
    }, 400);
}

// SIM 11: Clean Energy vs Coal Emission Monitor
function inspectPowerType(type) {
    const status = document.getElementById('sim11Status');
    if (type === 'coal') {
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Fossil Fuel Impact:</span> Burning coal releases particulate soot (PM2.5), sulfur dioxide, and greenhouse gases driving global warming and respiratory disease.';
        }
    } else {
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Renewable Future:</span> Solar panels and wind turbines generate clean electricity with zero emissions, protecting our health and climate forever!';
        }
    }
}

// SIM 12: Aerodynamic Pinwheel Wind Tunnel
function updatePinwheelSpeed(val) {
    const v = parseInt(val);
    const label = document.getElementById('pinwheelSliderLabel');
    const rpmText = document.getElementById('pinwheelRpmText');
    const speedText = document.getElementById('pinwheelSpeedText');
    const rotor = document.getElementById('pinwheelRotor');
    const status = document.getElementById('sim12Status');

    const rpm = v * 8;
    if (label) {
        label.textContent = v + ' km/h (' + (v > 40 ? 'Gale Wind' : v > 15 ? 'Brisk Breeze' : 'Calm') + ')';
    }
    if (rpmText) rpmText.textContent = rpm + ' RPM';
    if (speedText) speedText.textContent = 'Wind: ' + v + ' km/h';

    if (rotor) {
        // Rotate visual simulation
        rotor.style.transform = 'translate(224px, 115px) rotate(' + (v * 15) + 'deg)';
        rotor.style.transition = 'transform 0.1s linear';
    }

    if (status) {
        status.innerHTML = '<span class="text-cyan-400 font-bold">Wind Kinetic Force:</span> Air moving at ' + v + ' km/h spins the curved blades at ' + rpm + ' RPM, demonstrating how modern wind turbines generate clean electricity!';
    }
}

// SIM 13: Convex Sun Lens Focal Ignition Lab (Activity 7)
function updateLensFocus(heightVal) {
    const h = parseInt(heightVal);
    const label = document.getElementById('lensHeightLabel');
    const tempText = document.getElementById('focalTempText');
    const statusText = document.getElementById('focalStatusText');
    const hotSpot = document.getElementById('focalHotSpot');
    const smoke = document.getElementById('leafSmoke');
    const status = document.getElementById('sim13Status');

    // Optimal focal point is at h = 80
    const diff = Math.abs(h - 80);
    const calculatedTemp = Math.max(30, 265 - (diff * 4));

    if (diff < 8) {
        if (label) label.textContent = 'Optimal Focus (Sharp Point)';
        if (tempText) {
            tempText.textContent = calculatedTemp + '°C (Ignition!)';
            tempText.style.color = '#ef4444';
        }
        if (statusText) statusText.textContent = 'Leaf Smouldering & Smoking';
        if (hotSpot) hotSpot.style.display = 'inline';
        if (smoke) smoke.style.display = 'inline';
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Focal Point Reached:</span> Parallel rays converge to a microscopic point, spiking temperature over 250°C to ignite dry leaves!';
        }
    } else {
        if (label) label.textContent = 'Blurred Dispersion (' + h + ' mm)';
        if (tempText) {
            tempText.textContent = calculatedTemp + '°C (Warm)';
            tempText.style.color = '#f59e0b';
        }
        if (statusText) statusText.textContent = 'Rays Dispersed';
        if (hotSpot) hotSpot.style.display = 'none';
        if (smoke) smoke.style.display = 'none';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Dispersed Rays:</span> When the lens is out of focus, radiant energy spreads over a wide circle, warming the leaf without burning it.';
        }
    }
}

// SIM 14: Homemade Water Wheel & Mechanical Hoist (Activity 8)
let waterFlowActive = false;
function toggleWaterStream(flowing) {
    waterFlowActive = flowing;
    const stream = document.getElementById('fallingStream');
    const wheel = document.getElementById('waterWheelGroup');
    const weight = document.getElementById('hoistWeight');
    const rateText = document.getElementById('waterFlowRateText');
    const status = document.getElementById('sim14Status');

    if (flowing) {
        if (stream) stream.style.display = 'inline';
        if (wheel) {
            wheel.style.transform = 'translate(190px, 115px) rotate(180deg)';
            wheel.style.transition = 'transform 0.8s ease-in-out';
        }
        if (weight) {
            weight.setAttribute('y', '140');
            weight.style.transition = 'y 0.8s ease-in-out';
        }
        if (rateText) {
            rateText.textContent = 'Pouring Stream (Active)';
            rateText.style.color = '#38bdf8';
        }
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Rotational Hoisting:</span> Gravitational water stream rotates the spoon paddles, winding the axle string to lift the weight against gravity!';
        }
    } else {
        if (stream) stream.style.display = 'none';
        if (wheel) {
            wheel.style.transform = 'translate(190px, 115px) rotate(0deg)';
        }
        if (weight) {
            weight.setAttribute('y', '185');
        }
        if (rateText) {
            rateText.textContent = 'No Flow (At Rest)';
            rateText.style.color = '#94a3b8';
        }
        if (status) {
            status.innerHTML = '<span class="text-slate-400 font-bold">Water Stopped:</span> Without falling water, zero torque is applied and the wheel rests.';
        }
    }
}

// SIM 15: Traditional Himalayan Gharaat (Watermill)
function toggleGharaatFlow(diverted) {
    const runner = document.getElementById('gharaatRunner');
    const statusText = document.getElementById('gharaatStatusText');
    const status = document.getElementById('sim15Status');

    if (diverted) {
        if (runner) {
            runner.style.transform = 'translate(260px, 185px) rotate(180deg)';
            runner.style.transition = 'transform 0.6s linear';
        }
        if (statusText) {
            statusText.textContent = 'Water Mill Grinding Flour';
            statusText.style.color = '#34d399';
        }
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Clean Milling Power:</span> Mountain water jet drives the submerged wooden turbine, smoothly rotating the upper stone mill to grind nutritious grain!';
        }
    } else {
        if (runner) runner.style.transform = 'translate(260px, 185px) rotate(0deg)';
        if (statusText) {
            statusText.textContent = 'Sluice Gate Closed (Halted)';
            statusText.style.color = '#94a3b8';
        }
        if (status) {
            status.innerHTML = '<span class="text-slate-400 font-bold">Gharaat Halted:</span> When the water sluice is diverted back to the main river, the stone stops rotating safely.';
        }
    }
}

// SIM 16: Eco-Smart Home & Renewable Grid Dashboard
let ecoScore = 5;
function toggleEcoAction(action) {
    const score = document.getElementById('ecoStarScore');
    const status = document.getElementById('sim16Status');

    if (action === 'lights') {
        const w1 = document.getElementById('houseWindow1');
        if (w1) w1.setAttribute('fill', '#1e293b');
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Power Saved:</span> Switching off lights in empty rooms cuts phantom lighting waste instantly!';
        }
    } else if (action === 'unplug') {
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Vampire Load Eliminated:</span> Unplugged phone chargers stop consuming standby electricity!';
        }
    } else if (action === 'clothes') {
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Zero-Carbon Drying:</span> Natural sunshine and wind dried clothes without consuming 3,000 watts of dryer power!';
        }
    }
    if (score) score.textContent = '★★★★★';
}

// Document Ready Initialization
document.addEventListener('DOMContentLoaded', () => {
    showSlide(1);

    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            selectedMaleVoice = getIndianMaleVoice();
            populateVoiceList();
        };
        selectedMaleVoice = getIndianMaleVoice();
        populateVoiceList();
    }

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextSlide();
        else if (e.key === 'ArrowLeft') prevSlide();
        else if (e.key === ' ' && e.target.tagName !== 'BUTTON' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'SELECT') {
            e.preventDefault();
            toggleCurrentSlideLecture();
        }
    });
});
'''


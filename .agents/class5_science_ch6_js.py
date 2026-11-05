"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 6: Some Unique Places
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
            globalBtn.classList.add("bg-cyan-500/30", "border-cyan-500");
        } else {
            globalBtn.classList.remove("bg-cyan-500/30", "border-cyan-500");
        }
    }
    if (currentSlideSpeaking) {
        const badge = document.getElementById("slide-audio-badge-" + currentSlideSpeaking);
        const btn = document.getElementById("slide-audio-btn-" + currentSlideSpeaking);
        if (badge) {
            badge.textContent = speaking ? "Narrating..." : "Audio Lecture Ready";
            badge.className = speaking ? "px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 animate-pulse" : "px-2 py-0.5 rounded text-xs font-semibold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
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

    // Slide Counter
    const counter = document.getElementById("slideCounter");
    if (counter) counter.textContent = currentSlide + " / " + totalSlides;

    // Dropdown sync
    const select = document.getElementById("slideJumpSelect");
    if (select) select.value = currentSlide;

    // Previous Button
    const prevBtn = document.getElementById("prevBtn");
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);

    // Next Button & Terminal Notice
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

// SIM 1: Island Explorer & Indira Point Compass
let sim1WaterActive = false;
function toggleIslandWaterCheck() {
    sim1WaterActive = !sim1WaterActive;
    const arrows = document.getElementById('waterFlowArrows');
    const btn = document.getElementById('sim1WaterBtn');
    const status = document.getElementById('sim1Status');

    if (arrows) {
        if (sim1WaterActive) {
            arrows.classList.remove('opacity-0');
            arrows.classList.add('opacity-100');
        } else {
            arrows.classList.remove('opacity-100');
            arrows.classList.add('opacity-0');
        }
    }
    if (btn) {
        btn.textContent = sim1WaterActive ? 'Hide Water Boundaries' : 'Verify Water Surround';
    }
    if (status) {
        status.innerHTML = sim1WaterActive
            ? '<span class="text-cyan-400 font-bold">Island Verification:</span> 360° water confirmation! North, South, East, and West are all open seawater (Bay of Bengal & Andaman Sea).'
            : '<span class="text-cyan-400 font-bold">Island Fact:</span> An island has 360° water boundaries. India\'s mainland is a peninsula (water on 3 sides), while the Andaman & Nicobar group is a true island archipelago!';
    }
}

function zoomIndiraPoint() {
    const status = document.getElementById('sim1Status');
    const marker = document.getElementById('indiraMarker');
    if (marker) {
        marker.style.transform = 'translate(268px, 214px) scale(1.4)';
        setTimeout(() => { marker.style.transform = 'translate(268px, 214px) scale(1)'; }, 1000);
    }
    if (status) {
        status.innerHTML = '<span class="text-rose-400 font-bold">Indira Point:</span> Located on Great Nicobar at 6°45\' N latitude, this lighthouse station is India\'s southernmost territorial point!';
    }
}

// SIM 2: Buttress Root Structural Physics Lab
function updateWindPhysics(speed) {
    const s = parseInt(speed);
    const speedLabel = document.getElementById('windSpeedLabel');
    const forceText = document.getElementById('windForceText');
    const standardTree = document.getElementById('standardTree');
    const buttressTree = document.getElementById('buttressTree');
    const status = document.getElementById('sim2Status');

    if (speedLabel) {
        speedLabel.textContent = s + ' km/h ' + (s > 100 ? '(Cyclone!)' : s > 60 ? '(Gale)' : '(Moderate)');
    }
    if (forceText) {
        forceText.textContent = 'Wind: ' + s + ' km/h';
    }

    if (standardTree) {
        const angle = s > 90 ? 45 : s > 50 ? (s - 50) * 0.8 : 0;
        standardTree.style.transform = 'translate(100px, 190px) rotate(' + angle + 'deg)';
        standardTree.style.transformOrigin = 'bottom center';
        standardTree.style.transition = 'transform 0.3s ease-out';
    }

    if (buttressTree) {
        buttressTree.style.transform = 'translate(280px, 190px) rotate(0deg)';
    }

    if (status) {
        if (s > 90) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Cyclonic Gale:</span> Standard shallow root tree topples over! The buttress tree absorbs the massive lateral wind torque through ground tension.';
        } else {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Biomechanical Principle:</span> Wide triangular buttress roots act like external cathedral flying buttresses, converting horizontal gale wind shear into tensile anchoring forces along the ground!';
        }
    }
}

// SIM 3: Endemic Island Bird Observatory
function selectBird(bird) {
    const pigeonAura = document.getElementById('pigeonAura');
    const hornbillAura = document.getElementById('hornbillAura');
    const status = document.getElementById('sim3Status');

    if (bird === 'pigeon') {
        if (pigeonAura) pigeonAura.classList.remove('hidden');
        if (hornbillAura) hornbillAura.classList.add('hidden');
        if (status) {
            status.innerHTML = '<span class="text-purple-400 font-bold">Andaman Wood Pigeon (State Bird):</span> Endemic to Andaman & Nicobar evergreen canopies. Feeds on wild figs, palm fruits, and berries, dispersing seeds across isolated islands!';
        }
    } else {
        if (hornbillAura) hornbillAura.classList.remove('hidden');
        if (pigeonAura) pigeonAura.classList.add('hidden');
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Andaman / Narcondam Hornbill:</span> Distinctive hollow casque ridge over its beak. Pairs nest in natural tree hollows; father feeds mother and chick through a small mud slit!';
        }
    }
}

// SIM 4: Coral Polyp & Reef Ecosystem Builder
let sim4StormActive = false;
function toggleWaveStorm() {
    sim4StormActive = !sim4StormActive;
    const btn = document.getElementById('sim4StormBtn');
    const status = document.getElementById('sim4Status');
    const waveText = document.getElementById('waveReductionText');
    const wavePath = document.getElementById('stormWavePath');

    if (sim4StormActive) {
        if (btn) btn.textContent = 'Calm Ocean Swell';
        if (waveText) waveText.textContent = '97% Absorbed';
        if (wavePath) wavePath.setAttribute('d', 'M 0,50 Q 50,10 100,60 T 180,60 L 180,240 L 0,240 Z');
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Wave Energy Dissipation:</span> Heavy ocean swells smash into the outer coral wall. 97% of the mechanical energy is absorbed, leaving the coastal lagoon tranquil!';
        }
    } else {
        if (btn) btn.textContent = 'Simulate High Ocean Swell';
        if (waveText) waveText.textContent = 'Normal Wave Buffer';
        if (wavePath) wavePath.setAttribute('d', 'M 0,80 Q 50,30 100,75 T 180,80 L 180,240 L 0,240 Z');
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Symbiosis Secret:</span> Coral polyps are tiny animals that secrete calcium carbonate cups. Microscopic algae (zooxanthellae) living inside provide 90% of their nutrients through sunlight photosynthesis!';
        }
    }
}

function inspectPolypSymbiosis() {
    const status = document.getElementById('sim4Status');
    if (status) {
        status.innerHTML = '<span class="text-emerald-400 font-bold">Zooxanthellae Symbiosis:</span> Green microalgae live inside polyp tissues, using sunlight to make sugars. The polyp provides safe shelter and carbon dioxide!';
    }
}

// SIM 5: North Sentinel Island & Tsunami Wisdom
function setSentinelCondition(mode) {
    const birdAlarms = document.getElementById('birdAlarms');
    const ocean = document.getElementById('sentinelOcean');
    const modeText = document.getElementById('sentinelModeText');
    const status = document.getElementById('sim5Status');
    const camp = document.getElementById('tribeCamp');

    if (mode === 'tsunami') {
        if (birdAlarms) birdAlarms.classList.remove('opacity-0');
        if (ocean) ocean.setAttribute('d', 'M 0,200 L 150,200 Q 200,200 220,225 L 0,225 Z');
        if (modeText) {
            modeText.textContent = 'Tsunami Approach (Water Receding!)';
            modeText.classList.remove('text-cyan-400');
            modeText.classList.add('text-rose-400');
        }
        if (camp) camp.style.transform = 'translate(305px, 75px)';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Nature\'s Alarm:</span> Ocean water quickly receded hundreds of meters and birds shrieked. The Sentinelese recognized ancestral survival signs and climbed high forested ridges!';
        }
    } else {
        if (birdAlarms) birdAlarms.classList.add('opacity-0');
        if (ocean) ocean.setAttribute('d', 'M 0,160 L 150,160 Q 200,160 220,185 L 0,185 Z');
        if (modeText) {
            modeText.textContent = 'Calm Sea (Normal Tide)';
            modeText.classList.remove('text-rose-400');
            modeText.classList.add('text-cyan-400');
        }
        if (camp) camp.style.transform = 'translate(305px, 88px)';
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Sustainable Solitude:</span> For tens of thousands of years, Sentinelese hunter-gatherers have lived in harmony with their island, hunting with bows and collecting wild honey.';
        }
    }
}

// SIM 6: Sundarbans Tidal Delta Flow Engine
function updateTideLevel(val) {
    const v = parseInt(val);
    const rect = document.getElementById('tideWaterRect');
    const label = document.getElementById('tideLevelLabel');
    const salinity = document.getElementById('salinityText');
    const status = document.getElementById('sim6Status');

    const newY = 190 - (v * 0.7);
    const newH = 240 - newY;

    if (rect) {
        rect.setAttribute('y', newY);
        rect.setAttribute('height', newH);
    }

    if (label) {
        label.textContent = v > 70 ? 'High Tide (Saltwater Surge)' : v < 30 ? 'Low Tide (Mudflats Exposed)' : 'Mid Tide (Brackish Mix)';
    }

    if (salinity) {
        if (v > 70) salinity.textContent = 'High Salinity (Seawater Dominant)';
        else if (v < 30) salinity.textContent = 'Low Salinity (River Dominant)';
        else salinity.textContent = 'Brackish Water (Mixed)';
    }

    if (status) {
        if (v > 70) {
            status.innerHTML = '<span class="text-teal-400 font-bold">High Tide:</span> Seawater surges into river channels. Tangled mangrove roots hold silt firmly, preventing delta erosion!';
        } else if (v < 30) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Low Tide:</span> Mudflats and pneumatophores emerge into open air to absorb oxygen before the next tide returns!';
        } else {
            status.innerHTML = '<span class="text-teal-400 font-bold">Brackish Water:</span> Mixing of Ganga-Brahmaputra fresh water and Bay of Bengal salty tides supports lush Sundari forests!';
        }
    }
}

// SIM 7: Mangrove Pneumatophore Respiration Simulator
let sim7LenticelOpen = false;
let sim7Submerged = false;

function toggleLenticelZoom() {
    sim7LenticelOpen = !sim7LenticelOpen;
    const callout = document.getElementById('lenticelZoom');
    const status = document.getElementById('sim7Status');

    if (callout) {
        if (sim7LenticelOpen) {
            callout.classList.remove('opacity-0');
            callout.classList.add('opacity-100');
        } else {
            callout.classList.remove('opacity-100');
            callout.classList.add('opacity-0');
        }
    }
    if (status) {
        status.innerHTML = sim7LenticelOpen
            ? '<span class="text-yellow-400 font-bold">Lenticel Structure:</span> Lenticels are spongy cork openings that allow atmospheric oxygen to diffuse directly into internal aerenchyma air-channels down to underground roots.'
            : '<span class="text-emerald-400 font-bold">Negative Geotropism:</span> While regular roots grow downward with gravity (+geotropism), mangrove pneumatophores grow straight up into the air (-geotropism) to breathe!';
    }
}

function simulateTideSubmersion() {
    sim7Submerged = !sim7Submerged;
    const btn = document.getElementById('tideSubmergeBtn');
    const o2Flow = document.getElementById('oxygenFlow');
    const status = document.getElementById('sim7Status');

    if (sim7Submerged) {
        if (btn) btn.textContent = 'Simulate Low Tide Emergence';
        if (o2Flow) o2Flow.classList.add('opacity-20');
        if (status) {
            status.innerHTML = '<span class="text-cyan-400 font-bold">Submerged at High Tide:</span> Water seals lenticel pores temporarily. Stored internal oxygen keeps subterranean root cells alive until the tide recedes!';
        }
    } else {
        if (btn) btn.textContent = 'Simulate High Tide Cover';
        if (o2Flow) o2Flow.classList.remove('opacity-20');
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Low Tide Respiration:</span> Pneumatophores breathe freely in open air, replenishing oxygen reservoirs throughout the subterranean cable root network.';
        }
    }
}

// SIM 8: Sundarbans Tiger Ambush & Mask Defense
function toggleTigerMask(isOn) {
    const rearMask = document.getElementById('rearMask');
    const tiger = document.getElementById('stalkingTiger');
    const statusDesc = document.getElementById('tigerStatusDesc');
    const statusTitle = document.getElementById('tigerStatusTitle');
    const statusBox = document.getElementById('tigerStatusBox');
    const status = document.getElementById('sim8Status');

    if (isOn) {
        if (rearMask) {
            rearMask.classList.remove('opacity-0');
            rearMask.classList.add('opacity-100');
        }
        if (tiger) {
            tiger.style.transform = 'translate(330px, 150px) scale(0.9)';
        }
        if (statusTitle) statusTitle.textContent = 'Tiger Confused!';
        if (statusDesc) statusDesc.textContent = 'Sees eyes watching; retreats!';
        if (statusBox) {
            statusBox.setAttribute('stroke', '#10b981');
        }
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Mask Protection Success:</span> The tiger believes the human is looking directly at it! Because ambush predators will not attack when seen, it slinks away safely.';
        }
    } else {
        if (rearMask) {
            rearMask.classList.remove('opacity-100');
            rearMask.classList.add('opacity-0');
        }
        if (tiger) {
            tiger.style.transform = 'translate(260px, 150px) scale(1.05)';
        }
        if (statusTitle) statusTitle.textContent = 'Tiger Stalking!';
        if (statusDesc) statusDesc.textContent = 'Creeping up from behind...';
        if (statusBox) {
            statusBox.setAttribute('stroke', '#ea580c');
        }
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Vulnerable to Ambush:</span> Without a rear-facing mask, a honey collector\'s back is exposed. Tigers exploit blind spots to launch sudden sneak attacks.';
        }
    }
}

// SIM 9: Northeast India Eco-Map
const neStateData = {
    'assam': {
        name: 'Assam (Dispur)',
        eco1: 'Brahmaputra Valley & Kaziranga Grasslands',
        eco2: 'Hargila Stork Sanctuary & One-horned Rhinos',
        eco3: 'Lush Tea Gardens & Extensive Wetlands'
    },
    'meghalaya': {
        name: 'Meghalaya (Shillong)',
        eco1: 'Abode of Clouds (Mawsynram/Cherrapunji)',
        eco2: 'Jingkieng Jri (Living Root Bridges)',
        eco3: 'Mawphlang Ancient Sacred Groves'
    },
    'sikkim': {
        name: 'Sikkim (Gangtok)',
        eco1: 'World\'s 1st 100% Certified Organic State',
        eco2: 'Mt. Kangchenjunga (8,586 m) Biosphere',
        eco3: 'Rhododendron Sanctuaries & Red Pandas'
    },
    'manipur': {
        name: 'Manipur (Imphal)',
        eco1: 'Loktak Lake & Floating Phumdis (Biomass Islands)',
        eco2: 'Keibul Lamjao (Only Floating National Park)',
        eco3: 'Endangered Sangai Brow-antlered Deer'
    },
    'arunachal': {
        name: 'Arunachal Pradesh (Itanagar)',
        eco1: 'Land of Dawn-lit Mountains & Glaciers',
        eco2: 'Namdapha Flying Squirrel & Clouded Leopard',
        eco3: 'Extensive Sub-Himalayan Rainforests'
    },
    'nagaland': {
        name: 'Nagaland (Kohima)',
        eco1: 'Dzukou Valley & Blyth\'s Tragopan',
        eco2: 'Khonoma Community Forest & Green Village',
        eco3: 'Traditional Terraced Wet-Rice Farming'
    },
    'mizoram': {
        name: 'Mizoram (Aizawl)',
        eco1: 'Dampa Tiger Reserve & Clouded Leopards',
        eco2: 'Lush Bamboo Forests & Blue Mountain (Phawngpui)',
        eco3: 'Community-protected Forest Groves'
    },
    'tripura': {
        name: 'Tripura (Agartala)',
        eco1: 'Sepahijala Wildlife Sanctuary & Phayre\'s Langur',
        eco2: 'Clouded Leopard National Park',
        eco3: 'Rich Bamboo Biodiversity & Rubber Plantations'
    }
};

function selectNEState(key) {
    const data = neStateData[key];
    if (!data) return;

    const nameEl = document.getElementById('cardStateName');
    const eco1El = document.getElementById('cardStateEco1');
    const eco2El = document.getElementById('cardStateEco2');
    const eco3El = document.getElementById('cardStateEco3');
    const status = document.getElementById('sim9Status');

    if (nameEl) nameEl.textContent = data.name;
    if (eco1El) eco1El.textContent = data.eco1;
    if (eco2El) eco2El.textContent = data.eco2;
    if (eco3El) eco3El.textContent = data.eco3;

    if (status) {
        status.innerHTML = '<span class="text-emerald-400 font-bold">' + data.name + ':</span> ' + data.eco1 + '. ' + data.eco2 + '.';
    }
}

// SIM 10: Hargila Stork Nesting & Conservation Heroines
let sim10NetDeployed = false;
let sim10ChickFallen = false;

function deploySafetyNet() {
    sim10NetDeployed = !sim10NetDeployed;
    const net = document.getElementById('safetyNet');
    const btn = document.getElementById('netDeployBtn');
    const status = document.getElementById('sim10Status');

    if (net) {
        if (sim10NetDeployed) {
            net.classList.remove('opacity-0');
            net.classList.add('opacity-100');
        } else {
            net.classList.remove('opacity-100');
            net.classList.add('opacity-0');
        }
    }
    if (btn) {
        btn.textContent = sim10NetDeployed ? 'Safety Net Deployed (Active)' : '1. Deploy Safety Catch Net';
    }
    if (status) {
        status.innerHTML = sim10NetDeployed
            ? '<span class="text-emerald-400 font-bold">Net Armed:</span> Woven nylon nets tied beneath nesting trees catch chicks that accidentally tumble, saving them from fatal ground impact!'
            : '<span class="text-amber-400 font-bold">Community Action:</span> Dr. Purnima Devi Barman formed the Hargila Army to protect nests with custom safety nets.';
    }
}

function simulateChickSlip() {
    const chick = document.getElementById('storkChick');
    const rescueText = document.getElementById('hargilaRescueText');
    const status = document.getElementById('sim10Status');

    if (!sim10ChickFallen) {
        sim10ChickFallen = true;
        if (chick) {
            chick.style.transform = sim10NetDeployed ? 'translate(185px, 160px)' : 'translate(185px, 205px)';
        }
        if (rescueText) {
            rescueText.textContent = sim10NetDeployed ? 'Chick Caught Safely in Net!' : 'Chick on Ground (Rescue Needed!)';
            rescueText.style.color = sim10NetDeployed ? '#34d399' : '#f87171';
        }
        if (status) {
            status.innerHTML = sim10NetDeployed
                ? '<span class="text-emerald-400 font-bold">Saved!</span> The chick tumbled from the high nest but bounced safely into the Hargila Army\'s net! Rescuers check its wings and return it to the treetop.'
                : '<span class="text-rose-400 font-bold">Danger:</span> The chick fell directly onto the ground! Deploy the safety net to protect future nestlings.';
        }
    } else {
        sim10ChickFallen = false;
        if (chick) chick.style.transform = 'translate(185px, 45px)';
        if (rescueText) {
            rescueText.textContent = 'Chicks Safe in Nest';
            rescueText.style.color = '#38bdf8';
        }
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Chick Reset:</span> Nestling safely back in high tree hollow nest.';
        }
    }
}

// SIM 11: Living Root Bridge Bio-Architect
function updateRootBridgeAge(years) {
    const y = parseInt(years);
    const label = document.getElementById('bridgeYearsLabel');
    const ageText = document.getElementById('rootBridgeAgeText');
    const span1 = document.getElementById('rootSpan1');
    const span2 = document.getElementById('rootSpan2');
    const status = document.getElementById('sim11Status');

    if (label) {
        label.textContent = y + ' Years (' + (y >= 50 ? 'Mature Living Bridge' : y >= 25 ? 'Strengthening' : 'Juvenile Roots') + ')';
    }

    const thickness = 2 + (y * 0.08);
    if (span1) span1.setAttribute('stroke-width', thickness);
    if (span2) span2.setAttribute('stroke-width', thickness * 0.8);

    if (ageText) {
        if (y >= 50) ageText.textContent = 'Year ' + y + ': Rock-Solid Canopy';
        else if (y >= 25) ageText.textContent = 'Year ' + y + ': Supporting Footsteps';
        else ageText.textContent = 'Year ' + y + ': Thin Guided Strands';
    }

    if (status) {
        if (y >= 50) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Self-Strengthening Wonder:</span> At 50+ years, the rubber fig roots have merged (anastomosed) into dense living timber that can hold 50 people simultaneously without snapping!';
        } else {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Living Architecture:</span> Guided through hollow betel palm trunks, the aerial roots seek soil on the opposite river bank, anchoring and growing thicker every monsoon season.';
        }
    }
}

// SIM 12: Western Ghats Endemic Wildlife Tracker
function selectGhatsAnimal(animal) {
    const macaqueAura = document.getElementById('macaqueAura');
    const squirrelAura = document.getElementById('squirrelAura');
    const title = document.getElementById('ghatsAnimalTitle');
    const desc = document.getElementById('ghatsAnimalDesc');
    const status = document.getElementById('sim12Status');

    if (animal === 'macaque') {
        if (macaqueAura) macaqueAura.classList.remove('hidden');
        if (squirrelAura) squirrelAura.classList.add('hidden');
        if (title) title.textContent = 'Lion-Tailed Macaque (Old World Monkey)';
        if (desc) desc.textContent = 'Endemic silver-white mane; fruit & seed feeder';
        if (status) {
            status.innerHTML = '<span class="text-amber-400 font-bold">Lion-Tailed Macaque:</span> One of the world\'s rarest primates. Recognizable by its grand silver-white mane and lion-like tail tuft, it lives exclusively in the dense rainforest canopies of the Western Ghats!';
        }
    } else {
        if (squirrelAura) squirrelAura.classList.remove('hidden');
        if (macaqueAura) macaqueAura.classList.add('hidden');
        if (title) title.textContent = 'Malabar Giant Squirrel - Shekru';
        if (desc) desc.textContent = 'Multi-colored coat (maroon & cream); 2-foot bushy tail';
        if (status) {
            status.innerHTML = '<span class="text-pink-400 font-bold">Shekru (Giant Squirrel):</span> Maharashtra\'s State Animal. Weighing up to 2-3 kilograms with a majestic bushy tail, it leaps up to 6 meters between high branches without touching the forest floor!';
        }
    }
}

// SIM 13: Mountain River Springs & Botanical Pharmacy
const springInfo = {
    'godavari': {
        name: 'Trimbakeshwar (Godavari River)',
        state: 'Maharashtra (Western Ghats)',
        desc: 'Originates near Nashik, flowing 1,465 km east across peninsular India to the Bay of Bengal.'
    },
    'krishna': {
        name: 'Mahabaleshwar (Krishna River)',
        state: 'Maharashtra (Western Ghats)',
        desc: 'Emerges from a Gomukh spring at 1,300 m elevation, irrigating Maharashtra, Karnataka, and Andhra Pradesh.'
    },
    'cauvery': {
        name: 'Talakaveri (Cauvery River)',
        state: 'Kodagu, Karnataka (Brahmagiri Range)',
        desc: 'The sacred river of South India, sustained by the sponge action of Shola-grassland mountain forests.'
    }
};

function inspectSpring(key) {
    const data = springInfo[key];
    if (!data) return;

    ['godavari', 'krishna', 'cauvery'].forEach(k => {
        const btn = document.getElementById('btn' + k.charAt(0).toUpperCase() + k.slice(1));
        if (btn) {
            if (k === key) {
                btn.className = 'py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 border border-cyan-500/40 text-cyan-200';
            } else {
                btn.className = 'py-1.5 px-2 rounded-xl font-bold bg-slate-800 border border-slate-700 text-slate-200';
            }
        }
    });

    const status = document.getElementById('sim13Status');
    if (status) {
        status.innerHTML = '<span class="text-cyan-400 font-bold">' + data.name + ':</span> ' + data.desc + ' The Western Ghats also host 4,000+ medicinal plants like Ashwagandha and Sarpagandha!';
    }
}

// SIM 14: Citizen Science Mango Diversity Vault
const mangoInfo = {
    'appemidi': {
        name: 'Appemidi (Wild Pickling King)',
        traits: 'Small, intensely pungent, resinous, evergreen riverbank variety of the Western Ghats.',
        use: 'Heirloom whole tender pickle preserved for years under mustard oil.'
    },
    'alphonso': {
        name: 'Alphonso (Hapus)',
        traits: 'Saffron-golden skin, fibreless velvety pulp, rich aromatic fragrance from Konkan coast.',
        use: 'Premium dessert mango celebrated globally for exquisite sweetness.'
    },
    'totapuri': {
        name: 'Totapuri (Parrot Beak)',
        traits: 'Prominent hooked curved beak at the bottom, crisp greenish-yellow skin.',
        use: 'Popular for tangy salads, mango pulp processing, and spiced summer slices.'
    },
    'neelam': {
        name: 'Neelam (Late Harvest Jewel)',
        traits: 'Compact smooth oval shape, bright orange flesh, delightful floral aroma.',
        use: 'Ripens late in the season, prolonging the joyous summer bounty.'
    }
};

function inspectMango(key) {
    const data = mangoInfo[key];
    if (!data) return;

    ['appemidi', 'alphonso', 'totapuri', 'neelam'].forEach(k => {
        const aura = document.getElementById('aura' + k.charAt(0).toUpperCase() + k.slice(1));
        if (aura) {
            if (k === key) aura.classList.remove('hidden');
            else aura.classList.add('hidden');
        }
    });

    const titleEl = document.getElementById('mangoRegistryTitle');
    const descEl = document.getElementById('mangoRegistryDesc');
    const status = document.getElementById('sim14Status');

    if (titleEl) titleEl.textContent = 'Cultivar: ' + data.name;
    if (descEl) descEl.textContent = data.traits;

    if (status) {
        status.innerHTML = '<span class="text-amber-400 font-bold">' + data.name + ':</span> ' + data.traits + ' ' + data.use;
    }
}

// SIM 15: Silent Valley Rainforest Ecosystem Monitor
function setValleyState(mode) {
    const damGroup = document.getElementById('proposedDamGroup');
    const levelText = document.getElementById('soundscapeLevelText');
    const dbText = document.getElementById('soundscapeDbText');
    const status = document.getElementById('sim15Status');
    const btnSanctuary = document.getElementById('btnValleySanctuary');
    const btnDam = document.getElementById('btnValleyDam');

    if (mode === 'dam') {
        if (damGroup) damGroup.classList.remove('opacity-0');
        if (levelText) {
            levelText.textContent = 'Submerged Rainforest (Dam Built)';
            levelText.style.color = '#f87171';
        }
        if (dbText) {
            dbText.textContent = 'Habitat Destroyed (Macaques Lost)';
            dbText.style.color = '#cbd5e1';
        }
        if (btnDam) {
            btnDam.className = 'py-2 px-3 rounded-xl text-xs font-bold bg-rose-600 text-white';
        }
        if (btnSanctuary) {
            btnSanctuary.className = 'py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 text-slate-300';
        }
        if (status) {
            status.innerHTML = '<span class="text-rose-400 font-bold">Ecological Catastrophe:</span> The proposed dam would have flooded 8.3 sq km of ancient rainforest, wiping out riverine biodiversity and lion-tailed macaques forever.';
        }
    } else {
        if (damGroup) damGroup.classList.add('opacity-0');
        if (levelText) {
            levelText.textContent = 'Tranquil (No Cicada Screech)';
            levelText.style.color = '#34d399';
        }
        if (dbText) {
            dbText.textContent = '~ 25 dB (Gentle Breeze & Brook)';
            dbText.style.color = '#7dd3fc';
        }
        if (btnSanctuary) {
            btnSanctuary.className = 'py-2 px-3 rounded-xl text-xs font-bold bg-emerald-600 text-white';
        }
        if (btnDam) {
            btnDam.className = 'py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 text-slate-300';
        }
        if (status) {
            status.innerHTML = '<span class="text-emerald-400 font-bold">Protected National Park:</span> Thanks to the Save Silent Valley public movement, the dam was abandoned and the free-flowing Kunthipuzha river remains pristine!';
        }
    }
}

// SIM 16: India's Unique Places Expedition Passport
const stampedRegions = {
    andaman: false,
    sundarbans: false,
    northeast: false,
    ghats: false
};

function stampPassport(key) {
    stampedRegions[key] = true;
    const seal = document.getElementById('seal' + key.charAt(0).toUpperCase() + key.slice(1));
    const sealText = document.getElementById('sealText' + key.charAt(0).toUpperCase() + key.slice(1));

    if (seal) seal.setAttribute('opacity', '0.9');
    if (sealText) sealText.textContent = 'VERIFIED VISA ✓';

    checkAllPassportStamps();
}

function stampAllPassport() {
    ['andaman', 'sundarbans', 'northeast', 'ghats'].forEach(k => stampPassport(k));
}

function checkAllPassportStamps() {
    const allDone = Object.values(stampedRegions).every(v => v === true);
    const status = document.getElementById('sim16Status');
    if (allDone && status) {
        status.innerHTML = '<span class="text-cyan-400 font-bold">Explorer Certified! ★★★★★</span> You have completed your expedition across Andaman & Nicobar, Sundarbans, Northeast India, and the Western Ghats! Congratulations, Junior Ecological Guardian!';
    }
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

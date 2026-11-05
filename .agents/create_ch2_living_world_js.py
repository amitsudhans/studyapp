"""
Script to generate updated .agents/class6_science_ch2_js.py with enhanced lecture speech engine
and zero lecturer persona names.
"""

js_body = r'''
// Science Chapter 2 Interactive JavaScript
let currentSlide = 1;
const totalSlides = 20;

// Speech Synthesis Engine (Sentence-by-Sentence Queue to prevent Chromium timeout)
let isSpeaking = false;
let currentSpeakingSlide = null;
let speechQueue = [];
let speechIndex = 0;

function stopSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    currentSpeakingSlide = null;
    speechQueue = [];
    speechIndex = 0;
    updateAllAudioButtons();
}

function speakNextSentence() {
    if (!isSpeaking || speechIndex >= speechQueue.length) {
        stopSpeech();
        return;
    }
    const text = speechQueue[speechIndex];
    speechIndex++;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    utterance.pitch = 1.0;

    utterance.onend = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };
    utterance.onerror = (e) => {
        console.warn("Speech error, advancing to next sentence:", e);
        if (isSpeaking) {
            speakNextSentence();
        }
    };

    window.speechSynthesis.speak(utterance);
}

function startLectureSpeech(fullText, slideNo) {
    if (!('speechSynthesis' in window)) {
        alert("Text-to-speech is not supported in this browser.");
        return;
    }

    if (isSpeaking && currentSpeakingSlide === slideNo) {
        stopSpeech();
        return;
    }

    stopSpeech();

    // Clean text and split by sentences (periods, exclamation, question marks)
    const cleanText = fullText.replace(/<[^>]+>/g, ' ').split(' ').filter(Boolean).join(' ').trim();
    const rawSentences = cleanText.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [cleanText];
    speechQueue = rawSentences.map(s => s.trim()).filter(s => s.length > 0);

    if (speechQueue.length === 0) return;

    isSpeaking = true;
    currentSpeakingSlide = slideNo;
    speechIndex = 0;

    updateAllAudioButtons();
    speakNextSentence();
}

function toggleCurrentSlideLecture() {
    if (currentSlide > 16) {
        alert("This slide contains interactive mastery exercises for self-study and practice.");
        return;
    }
    const slideDataEl = document.getElementById(`slide-spoken-text-${currentSlide}`);
    if (slideDataEl) {
        const textToSpeak = slideDataEl.textContent.trim();
        startLectureSpeech(textToSpeak, currentSlide);
    }
}

function updateAllAudioButtons() {
    // Global Header Button
    const globalBtn = document.getElementById('globalAudioBtn');
    if (globalBtn) {
        if (isSpeaking) {
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center space-x-1.5 animate-pulse transition';
            globalBtn.innerHTML = '<span>⏹</span><span>Stop Lecture</span>';
        } else {
            globalBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500/20 text-emerald-300 hover:bg-emerald-500/30 border border-emerald-500/30 flex items-center space-x-1.5 transition';
            globalBtn.innerHTML = '<span>🔊</span><span>Listen to Lecture</span>';
        }
    }

    // Per-slide buttons
    for (let i = 1; i <= 16; i++) {
        const btn = document.getElementById(`slide-audio-btn-${i}`);
        const badge = document.getElementById(`slide-audio-badge-${i}`);
        if (btn) {
            if (isSpeaking && currentSpeakingSlide === i) {
                btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center space-x-1.5 animate-pulse transition';
                btn.innerHTML = '<span>⏹</span><span>Stop Audio</span>';
                if (badge) {
                    badge.textContent = 'Speaking Lecture...';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-rose-500/20 text-rose-300 border border-rose-500/30';
                }
            } else {
                btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30 flex items-center space-x-1.5 transition';
                btn.innerHTML = '<span>▶</span><span>Listen to Full Lecture</span>';
                if (badge) {
                    badge.textContent = 'Audio Lecture Ready';
                    badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
                }
            }
        }
    }
}

// Navigation
function updateSlideDisplay() {
    stopSpeech();

    for (let i = 1; i <= totalSlides; i++) {
        const slide = document.getElementById(`slide-${i}`);
        if (slide) {
            slide.style.display = (i === currentSlide) ? 'block' : 'none';
        }
    }
    const indicator = document.getElementById('slideIndicator');
    if (indicator) {
        indicator.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }
    const progressBar = document.getElementById('progressBar');
    if (progressBar) {
        progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;
    }
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
    }
    if (nextBtn) {
        if (currentSlide === totalSlides) {
            nextBtn.style.display = 'none';
        } else {
            nextBtn.style.display = 'inline-flex';
        }
    }
    if (lastSlideNotice) {
        lastSlideNotice.style.display = (currentSlide === totalSlides) ? 'block' : 'none';
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        currentSlide++;
        updateSlideDisplay();
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        currentSlide--;
        updateSlideDisplay();
    }
}

function goToSlide(n) {
    if (n >= 1 && n <= totalSlides) {
        currentSlide = n;
        updateSlideDisplay();
    }
}

// Checkpoint Verification
function checkCheckpoint(cpId, selectedOption, correctOption, explanation) {
    const feedbackEl = document.getElementById(`cp-feedback-${cpId}`);
    const badgeEl = document.getElementById(`cp-badge-${cpId}`);
    if (!feedbackEl) return;

    if (selectedOption === correctOption) {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-emerald-950/40 border border-emerald-500/50 text-emerald-300';
        feedbackEl.innerHTML = `<strong>Correct!</strong> ` + explanation;
        if (badgeEl) {
            badgeEl.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
            badgeEl.textContent = 'Solved';
        }
    } else {
        feedbackEl.className = 'mt-3 p-3 rounded-lg text-sm bg-rose-950/40 border border-rose-500/50 text-rose-300';
        feedbackEl.innerHTML = `<strong>Try again:</strong> Re-examine the morphological traits or biological rule carefully!`;
    }
    feedbackEl.style.display = 'block';
}

// Solution Modal
function openSolutionModal(title, question, correctAnswer, explanation) {
    const modal = document.getElementById('solutionModal');
    const titleEl = document.getElementById('modalTitle');
    const questionEl = document.getElementById('modalQuestion');
    const answerEl = document.getElementById('modalAnswer');
    const explanationEl = document.getElementById('modalExplanation');

    if (modal && titleEl && questionEl && answerEl && explanationEl) {
        titleEl.textContent = title;
        questionEl.innerHTML = `<strong>Question:</strong> ${question}`;
        answerEl.innerHTML = `<strong>Correct Answer:</strong> ${correctAnswer}`;
        explanationEl.innerHTML = `<strong>Detailed Step-by-Step Solution:</strong><br>${explanation}`;
        modal.style.display = 'flex';
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Quiz Option Selection
function selectQuizOption(qId, selectedOpt, correctOpt, title, questionText, explanation) {
    const btnContainer = document.getElementById(`q-options-${qId}`);
    const feedbackBox = document.getElementById(`q-feedback-${qId}`);
    const solutionBtn = document.getElementById(`q-sol-btn-${qId}`);

    if (btnContainer) {
        const buttons = btnContainer.querySelectorAll('button');
        buttons.forEach((btn, index) => {
            const optLetter = String.fromCharCode(65 + index);
            btn.disabled = true;
            if (optLetter === correctOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-semibold bg-emerald-950/60 border border-emerald-500/60 text-emerald-300 shadow-sm';
            } else if (optLetter === selectedOpt) {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-semibold bg-rose-950/60 border border-rose-500/60 text-rose-300 shadow-sm';
            } else {
                btn.className = 'w-full text-left p-3 rounded-xl text-xs sm:text-sm font-medium bg-slate-900/40 border border-slate-800/80 text-slate-500 opacity-60';
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.style.display = 'block';
        if (selectedOpt === correctOpt) {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-xs sm:text-sm bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
            feedbackBox.innerHTML = `<strong>Correct! (${correctOpt})</strong> Outstanding biological reasoning!`;
        } else {
            feedbackBox.className = 'mt-3 p-3 rounded-xl text-xs sm:text-sm bg-rose-950/40 border border-rose-500/40 text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect (${selectedOpt}).</strong> The correct answer is <strong>${correctOpt}</strong>.`;
        }
    }

    if (solutionBtn) {
        solutionBtn.style.display = 'inline-flex';
    }
}

// -------------------------------------------------------------
// Simulator 1: The Nature Walk Explorer
// -------------------------------------------------------------
function setSim1Spot(spot) {
    ['bird', 'tree', 'monkey', 'butterfly'].forEach(k => {
        const btn = document.getElementById(`sim1-btn-${k}`);
        if (btn) {
            btn.className = (k === spot) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim1-svg');
    const badge = document.getElementById('sim1-badge');
    const desc = document.getElementById('sim1-desc');

    if (spot === 'bird') {
        badge.textContent = "Birdsong Mimicry & Listening";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20";
        desc.innerHTML = "Cupping hands and whistling a gentle melodic call prompts a black drongo deep in the canopy to reply with twin notes! Students observe birds through binoculars without disturbing active nests.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#064e3b" fill-opacity="0.2" rx="12"/>
            <circle cx="225" cy="50" r="70" fill="#047857" fill-opacity="0.4"/>
            <circle cx="160" cy="80" r="50" fill="#059669" fill-opacity="0.4"/>
            <circle cx="290" cy="75" r="55" fill="#10b981" fill-opacity="0.3"/>
            <path d="M120,110 Q200,95 330,120" stroke="#78350f" stroke-width="8" fill="none" stroke-linecap="round"/>
            <ellipse cx="230" cy="85" rx="14" ry="10" fill="#0284c7"/>
            <circle cx="242" cy="80" r="7" fill="#38bdf8"/>
            <polygon points="249,79 257,81 249,83" fill="#f59e0b"/>
            <path d="M260,75 Q266,80 260,85" stroke="#38bdf8" stroke-width="2" fill="none"/>
            <path d="M265,70 Q275,80 265,90" stroke="#38bdf8" stroke-width="2" fill="none"/>
            <text x="225" y="155" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Field Rule: 'Listen first, walk quietly, let nature speak!'</text>
        `;
    } else if (spot === 'tree') {
        badge.textContent = "Banyan Tree & Prop Roots";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20";
        desc.innerHTML = "Examining the massive woody trunk of an ancient banyan tree reveals aerial prop roots descending from heavy horizontal branches into the soil, functioning like monumental support pillars.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#1e293b" fill-opacity="0.3" rx="12"/>
            <rect x="210" y="70" width="30" height="90" fill="#78350f" rx="3"/>
            <ellipse cx="225" cy="55" rx="110" ry="45" fill="#15803d" fill-opacity="0.6"/>
            <line x1="160" y1="65" x2="160" y2="160" stroke="#92400e" stroke-width="4"/>
            <line x1="290" y1="65" x2="290" y2="160" stroke="#92400e" stroke-width="4"/>
            <line x1="40" y1="160" x2="410" y2="160" stroke="#334155" stroke-width="3"/>
            <text x="160" y="145" fill="#fde68a" font-size="9" text-anchor="middle">Prop Root</text>
            <text x="290" y="145" fill="#fde68a" font-size="9" text-anchor="middle">Prop Root</text>
            <text x="225" y="175" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Aerial Roots Provide Monumental Pillar Support</text>
        `;
    } else if (spot === 'monkey') {
        badge.textContent = "Canopy Troop Dynamics";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20";
        desc.innerHTML = "Observing monkey troops high up in the treetops: their agile prehensile limbs allow swift brachiation across branches while foraging on wild figs and dropping seeds to the forest floor.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#1e1b4b" fill-opacity="0.3" rx="12"/>
            <path d="M50,110 Q225,80 400,105" stroke="#78350f" stroke-width="10" fill="none"/>
            <ellipse cx="180" cy="85" rx="16" ry="12" fill="#a16207"/>
            <circle cx="170" cy="78" r="9" fill="#ca8a04"/>
            <path d="M195,85 Q210,70 205,55" stroke="#a16207" stroke-width="3" fill="none"/>
            <circle cx="280" cy="90" r="12" fill="#ca8a04"/>
            <line x1="280" y1="90" x2="295" y2="105" stroke="#a16207" stroke-width="4"/>
            <text x="225" y="150" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">Canopy Tree Dwelling: Adapted for Climbing & Leaping</text>
        `;
    } else {
        badge.textContent = "Pollinator Observation";
        badge.className = "px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20";
        desc.innerHTML = "A vibrant common mormon butterfly hovers near wild Lantana flowers. Its slender proboscis sips sweet nectar while its fuzzy legs brush pollen grains, ensuring plant fertilization!";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#4c0519" fill-opacity="0.2" rx="12"/>
            <path d="M225,160 Q220,110 225,85" stroke="#16a34a" stroke-width="4" fill="none"/>
            <circle cx="225" cy="85" r="8" fill="#f59e0b"/>
            <circle cx="215" cy="80" r="6" fill="#f43f5e"/>
            <circle cx="235" cy="80" r="6" fill="#f43f5e"/>
            <circle cx="225" cy="72" r="6" fill="#f43f5e"/>
            <ellipse cx="225" cy="45" rx="4" ry="12" fill="#0f172a"/>
            <path d="M225,40 C200,20 190,55 225,48" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
            <path d="M225,40 C250,20 260,55 225,48" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
            <text x="225" y="145" fill="#fbcfe8" font-size="11" font-weight="bold" text-anchor="middle">Pollinator Interdependence: Nectar Reward for Pollen Transfer</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 2: Web of Biodiversity & Mutual Interdependence
// -------------------------------------------------------------
function setSim2Link(link) {
    ['shelter', 'seed', 'pollinate', 'soil'].forEach(k => {
        const btn = document.getElementById(`sim2-btn-${k}`);
        if (btn) {
            btn.className = (k === link) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim2-svg');
    const badge = document.getElementById('sim2-badge');
    const desc = document.getElementById('sim2-desc');

    if (link === 'shelter') {
        badge.textContent = "Tree Provides Shelter & Habitat";
        desc.innerHTML = "Plants form the physical foundation of ecosystems: bird nests, tree frogs, squirrels, and arboreal insects rely on branch canopies for microclimates, predator protection, and shade.";
        svg.innerHTML = `
            <rect x="70" y="30" width="120" height="90" rx="10" fill="#065f46" fill-opacity="0.3" stroke="#10b981"/>
            <text x="130" y="65" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Mature Tree</text>
            <text x="130" y="85" fill="#6ee7b7" font-size="10" text-anchor="middle">Canopy & Trunk</text>
            <line x1="190" y1="75" x2="260" y2="75" stroke="#f59e0b" stroke-width="3"/>
            <rect x="260" y="30" width="120" height="90" rx="10" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b"/>
            <text x="320" y="65" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">Wildlife Shelter</text>
            <text x="320" y="85" fill="#fcd34d" font-size="10" text-anchor="middle">Nests, Roosts & Cavities</text>
            <text x="225" y="155" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Direct Habitat Provisioning (Primary Producers)</text>
        `;
    } else if (link === 'seed') {
        badge.textContent = "Animals Disperse Seeds Far & Wide";
        desc.innerHTML = "Frugivorous animals eat sweet fruits and travel away from the parent tree. Seeds pass safely through animal digestive tracts and are deposited in nutrient-rich dung, colonizing new ground!";
        svg.innerHTML = `
            <circle cx="100" cy="75" r="40" fill="#b91c1c" fill-opacity="0.3" stroke="#ef4444" stroke-width="2"/>
            <text x="100" y="70" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">Parent Tree</text>
            <text x="100" y="88" fill="#f87171" font-size="9" text-anchor="middle">Produces Fruit</text>
            <path d="M145,75 Q225,35 305,75" stroke="#38bdf8" stroke-width="3" fill="none" stroke-dasharray="6,4"/>
            <circle cx="340" cy="75" r="40" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
            <text x="340" y="70" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">New Sapling</text>
            <text x="340" y="88" fill="#6ee7b7" font-size="9" text-anchor="middle">500m Away</text>
            <text x="225" y="150" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Endozoochory: Animal Vectors Expand Forest Boundaries</text>
        `;
    } else if (link === 'pollinate') {
        badge.textContent = "Pollination: Mutual Survival";
        desc.innerHTML = "Over 75% of flowering plants depend on insect and bird pollinators. As bees forage for protein-rich pollen and nectar, they cross-pollinate blossoms, ensuring seed formation.";
        svg.innerHTML = `
            <ellipse cx="110" cy="75" rx="45" ry="35" fill="#831843" fill-opacity="0.3" stroke="#f43f5e" stroke-width="2"/>
            <text x="110" y="72" fill="#fbcfe8" font-size="12" font-weight="bold" text-anchor="middle">Flower A</text>
            <text x="110" y="88" fill="#f472b6" font-size="9" text-anchor="middle">Pollen Source</text>
            <path d="M160,75 Q225,50 280,75" stroke="#f59e0b" stroke-width="3" fill="none"/>
            <ellipse cx="330" cy="75" rx="45" ry="35" fill="#831843" fill-opacity="0.3" stroke="#f43f5e" stroke-width="2"/>
            <text x="330" y="72" fill="#fbcfe8" font-size="12" font-weight="bold" text-anchor="middle">Flower B</text>
            <text x="330" y="88" fill="#f472b6" font-size="9" text-anchor="middle">Fertilized Ovary</text>
            <text x="225" y="150" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Bees & Butterflies Transfer Genetic Material</text>
        `;
    } else {
        badge.textContent = "Decomposers & Soil Micro-organisms";
        desc.innerHTML = "Earthworms, mycorrhizal fungi, and soil microbes break down fallen leaves and biological waste into humus, liberating mineral nitrates and phosphates that roots reabsorb.";
        svg.innerHTML = `
            <rect x="50" y="45" width="100" height="60" rx="8" fill="#78350f" fill-opacity="0.4" stroke="#d97706"/>
            <text x="100" y="75" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Leaf Litter</text>
            <line x1="150" y1="75" x2="200" y2="75" stroke="#10b981" stroke-width="3"/>
            <rect x="200" y="45" width="100" height="60" rx="8" fill="#14532d" fill-opacity="0.4" stroke="#22c55e"/>
            <text x="250" y="75" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Earthworms</text>
            <line x1="300" y1="75" x2="350" y2="75" stroke="#10b981" stroke-width="3"/>
            <rect x="350" y="45" width="80" height="60" rx="8" fill="#0369a1" fill-opacity="0.4" stroke="#38bdf8"/>
            <text x="390" y="75" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">Soil Humus</text>
            <text x="225" y="150" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Nutrient Cycling Closes the Ecological Circle</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 3: The Classification Sorting Station
// -------------------------------------------------------------
function setSim3Criterion(crit) {
    ['stem', 'mobility', 'habitat'].forEach(k => {
        const btn = document.getElementById(`sim3-btn-${k}`);
        if (btn) {
            btn.className = (k === crit) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim3-svg');
    const badge = document.getElementById('sim3-badge');
    const desc = document.getElementById('sim3-desc');

    if (crit === 'stem') {
        badge.textContent = "Criterion: Stem Rigidity & Texture";
        desc.textContent = "Sorting Group A (Hard Woody Stems: Trees & Shrubs like Mango, Rose) vs Group B (Soft Green Stems: Herbs like Tomato, Coriander).";
        svg.innerHTML = `
            <rect x="30" y="30" width="180" height="110" rx="10" fill="#78350f" fill-opacity="0.2" stroke="#d97706" stroke-width="2"/>
            <text x="120" y="55" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Woody Stems</text>
            <rect x="50" y="70" width="60" height="30" rx="6" fill="#451a03"/><text x="80" y="90" fill="#fde047" font-size="10" text-anchor="middle">Mango</text>
            <rect x="125" y="70" width="65" height="30" rx="6" fill="#451a03"/><text x="157" y="90" fill="#fde047" font-size="10" text-anchor="middle">Rose Bush</text>

            <rect x="240" y="30" width="180" height="110" rx="10" fill="#065f46" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
            <text x="330" y="55" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">Green Soft Stems</text>
            <rect x="255" y="70" width="65" height="30" rx="6" fill="#064e3b"/><text x="287" y="90" fill="#86efac" font-size="10" text-anchor="middle">Tomato</text>
            <rect x="335" y="70" width="65" height="30" rx="6" fill="#064e3b"/><text x="367" y="90" fill="#86efac" font-size="10" text-anchor="middle">Spinach</text>
            <text x="225" y="165" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Criterion segregates woody structural perennials from tender annuals</text>
        `;
    } else if (crit === 'mobility') {
        badge.textContent = "Criterion: Locomotion Capability";
        desc.textContent = "Sorting Group A (Active Mobile Organisms: Animals like Camel, Tiger, Fish) vs Group B (Rooted Stationary Organisms: Plants like Mango, Grass).";
        svg.innerHTML = `
            <rect x="30" y="30" width="180" height="110" rx="10" fill="#1e1b4b" fill-opacity="0.3" stroke="#6366f1" stroke-width="2"/>
            <text x="120" y="55" fill="#c7d2fe" font-size="12" font-weight="bold" text-anchor="middle">Active Locomotion</text>
            <rect x="50" y="70" width="65" height="30" rx="6" fill="#312e81"/><text x="82" y="90" fill="#a5b4fc" font-size="10" text-anchor="middle">Camel</text>
            <rect x="125" y="70" width="65" height="30" rx="6" fill="#312e81"/><text x="157" y="90" fill="#a5b4fc" font-size="10" text-anchor="middle">Kingfisher</text>

            <rect x="240" y="30" width="180" height="110" rx="10" fill="#064e3b" fill-opacity="0.3" stroke="#22c55e" stroke-width="2"/>
            <text x="330" y="55" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">Rooted / Stationary</text>
            <rect x="255" y="70" width="65" height="30" rx="6" fill="#065f46"/><text x="287" y="90" fill="#86efac" font-size="10" text-anchor="middle">Banyan</text>
            <rect x="335" y="70" width="65" height="30" rx="6" fill="#065f46"/><text x="367" y="90" fill="#86efac" font-size="10" text-anchor="middle">Neem Tree</text>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Separates heterotrophic movers from photosynthetic sessile plants</text>
        `;
    } else {
        badge.textContent = "Criterion: Ecological Medium (Habitat)";
        desc.textContent = "Sorting Group A (Terrestrial: Desert Camel, Banyan, Mountain Leopard) vs Group B (Aquatic: Rohu Fish, Lotus, Water Lily).";
        svg.innerHTML = `
            <rect x="30" y="30" width="180" height="110" rx="10" fill="#713f12" fill-opacity="0.3" stroke="#eab308" stroke-width="2"/>
            <text x="120" y="55" fill="#fef08a" font-size="12" font-weight="bold" text-anchor="middle">Terrestrial (Land)</text>
            <rect x="50" y="70" width="65" height="30" rx="6" fill="#451a03"/><text x="82" y="90" fill="#fde047" font-size="10" text-anchor="middle">Desert Camel</text>
            <rect x="125" y="70" width="65" height="30" rx="6" fill="#451a03"/><text x="157" y="90" fill="#fde047" font-size="10" text-anchor="middle">Neem Tree</text>

            <rect x="240" y="30" width="180" height="110" rx="10" fill="#0c4a6e" fill-opacity="0.3" stroke="#0ea5e9" stroke-width="2"/>
            <text x="330" y="55" fill="#bae6fd" font-size="12" font-weight="bold" text-anchor="middle">Aquatic (Water)</text>
            <rect x="255" y="70" width="65" height="30" rx="6" fill="#075985"/><text x="287" y="90" fill="#7dd3fc" font-size="10" text-anchor="middle">Rohu Fish</text>
            <rect x="335" y="70" width="65" height="30" rx="6" fill="#075985"/><text x="367" y="90" fill="#7dd3fc" font-size="10" text-anchor="middle">Lotus</text>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Distinguishes breathing in open air vs extracting dissolved oxygen</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 4: Plant Architecture (Trees, Shrubs & Herbs)
// -------------------------------------------------------------
function setSim4Category(cat) {
    ['tree', 'shrub', 'herb'].forEach(k => {
        const btn = document.getElementById(`sim4-btn-${k}`);
        if (btn) {
            btn.className = (k === cat) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim4-svg');
    const badge = document.getElementById('sim4-badge');
    const desc = document.getElementById('sim4-desc');

    if (cat === 'tree') {
        badge.textContent = "Tree Architecture (Tall & Single Trunk)";
        desc.innerHTML = "<strong>Trees:</strong> Tall plants with a hard, thick, brown woody trunk. Primary branching occurs high above the ground level (e.g., Mango, Peepal, Banyan, Neem).";
        svg.innerHTML = `
            <line x1="30" y1="160" x2="420" y2="160" stroke="#475569" stroke-width="2"/>
            <rect x="210" y="80" width="30" height="80" fill="#78350f" rx="3"/>
            <circle cx="225" cy="50" r="45" fill="#15803d" fill-opacity="0.7"/>
            <circle cx="190" cy="65" r="30" fill="#16a34a" fill-opacity="0.6"/>
            <circle cx="260" cy="65" r="30" fill="#16a34a" fill-opacity="0.6"/>
            <line x1="120" y1="20" x2="120" y2="160" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
            <text x="110" y="90" fill="#fde68a" font-size="11" text-anchor="end">> 3 to 20+ Meters</text>
            <text x="225" y="175" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Branches initiate well above ground on single massive trunk</text>
        `;
    } else if (cat === 'shrub') {
        badge.textContent = "Shrub Architecture (Medium & Bushy Ground Branching)";
        desc.innerHTML = "<strong>Shrubs:</strong> Medium-sized plants with hard, thin, woody stems. Branching starts directly near the soil base with no dominant high trunk (e.g., Rose, Hibiscus, Lemon, Henna).";
        svg.innerHTML = `
            <line x1="30" y1="160" x2="420" y2="160" stroke="#475569" stroke-width="2"/>
            <path d="M225,160 L180,90" stroke="#92400e" stroke-width="5"/>
            <path d="M225,160 L225,80" stroke="#92400e" stroke-width="5"/>
            <path d="M225,160 L270,90" stroke="#92400e" stroke-width="5"/>
            <circle cx="180" cy="85" r="25" fill="#15803d" fill-opacity="0.6"/>
            <circle cx="225" cy="75" r="28" fill="#16a34a" fill-opacity="0.7"/>
            <circle cx="270" cy="85" r="25" fill="#15803d" fill-opacity="0.6"/>
            <circle cx="180" cy="75" r="6" fill="#f43f5e"/>
            <circle cx="270" cy="75" r="6" fill="#f43f5e"/>
            <text x="110" y="115" fill="#fde68a" font-size="11" text-anchor="end">1 to 3 Meters</text>
            <text x="225" y="175" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Multiple thin woody stems radiate near base, creating dense bush</text>
        `;
    } else {
        badge.textContent = "Herb Architecture (Short & Tender Green Stem)";
        desc.innerHTML = "<strong>Herbs:</strong> Small, short plants usually less than 1 meter tall with soft, delicate, green stems. They lack woody tissue (e.g., Tomato, Coriander, Wheat, Mint, Mustard).";
        svg.innerHTML = `
            <line x1="30" y1="160" x2="420" y2="160" stroke="#475569" stroke-width="2"/>
            <path d="M225,160 Q220,130 225,100" stroke="#22c55e" stroke-width="4" fill="none"/>
            <ellipse cx="210" cy="120" rx="15" ry="6" fill="#16a34a" transform="rotate(-25 210 120)"/>
            <ellipse cx="240" cy="115" rx="15" ry="6" fill="#16a34a" transform="rotate(25 240 115)"/>
            <circle cx="225" cy="95" r="8" fill="#ef4444"/>
            <text x="110" y="130" fill="#86efac" font-size="11" text-anchor="end">< 1 Meter</text>
            <text x="225" y="175" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Tender, non-woody, succulent green stem; easily bent without snapping</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 5: Climbers vs Creepers
// -------------------------------------------------------------
function setSim5Type(type) {
    const isClimber = (type === 'climber');
    document.getElementById('sim5-btn-climber').className = isClimber ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim5-btn-creeper').className = !isClimber ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim5-svg');
    const badge = document.getElementById('sim5-badge');
    const desc = document.getElementById('sim5-desc');

    if (isClimber) {
        badge.textContent = "Climber: Coiling Tendrils";
        desc.innerHTML = "<strong>Climbers:</strong> Weak green stems that cannot stand upright alone, but produce thread-like spiraling <em>tendrils</em> that clasp fences, trellises, or trees to climb towards sunlight (e.g., Pea plant, Money plant, Grapevine).";
        svg.innerHTML = `
            <line x1="40" y1="160" x2="410" y2="160" stroke="#475569" stroke-width="2"/>
            <rect x="220" y="20" width="10" height="140" fill="#78350f" rx="2"/>
            <path d="M205,160 Q235,140 215,120 Q240,100 220,80 Q235,60 225,40" stroke="#22c55e" stroke-width="5" fill="none"/>
            <path d="M225,80 C245,75 250,90 230,90" stroke="#16a34a" stroke-width="2" fill="none"/>
            <path d="M220,120 C240,115 245,130 225,130" stroke="#16a34a" stroke-width="2" fill="none"/>
            <ellipse cx="200" cy="70" rx="10" ry="6" fill="#15803d"/>
            <ellipse cx="245" cy="50" rx="10" ry="6" fill="#15803d"/>
            <text x="225" y="175" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Tendrils coil tightly around vertical support for mechanical lift</text>
        `;
    } else {
        badge.textContent = "Creeper: Ground Sprawling (Heavy Fruits)";
        desc.innerHTML = "<strong>Creepers:</strong> Weak horizontal stems that sprawl across the soil surface because they bear large, heavy fruits (e.g., Watermelon, Pumpkin, Muskmelon, Bottle gourd) that would break upright branches!";
        svg.innerHTML = `
            <line x1="40" y1="150" x2="410" y2="150" stroke="#475569" stroke-width="2"/>
            <path d="M60,145 Q150,140 220,146 Q310,140 400,145" stroke="#22c55e" stroke-width="6" fill="none"/>
            <ellipse cx="225" cy="130" rx="36" ry="24" fill="#15803d" stroke="#166534" stroke-width="3"/>
            <path d="M200,118 Q225,145 250,118" stroke="#14532d" stroke-width="3" fill="none"/>
            <path d="M195,130 Q225,150 255,130" stroke="#14532d" stroke-width="3" fill="none"/>
            <ellipse cx="120" cy="140" rx="12" ry="7" fill="#16a34a"/>
            <ellipse cx="320" cy="140" rx="12" ry="7" fill="#16a34a"/>
            <text x="225" y="90" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Heavy 5-10 kg Fruit Supported by Soil Bed</text>
            <text x="225" y="172" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Gravity safety: Cannot climb vertical stakes without collapse</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 6: Leaf Venation Microscope
// -------------------------------------------------------------
function setSim6Venation(ven) {
    const isRet = (ven === 'reticulate');
    document.getElementById('sim6-btn-reticulate').className = isRet ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim6-btn-parallel').className = !isRet ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim6-svg');
    const badge = document.getElementById('sim6-badge');
    const desc = document.getElementById('sim6-desc');

    if (isRet) {
        badge.textContent = "Reticulate Venation (Net-like)";
        desc.innerHTML = "<strong>Reticulate Venation:</strong> Veins form an intricate, interconnected web-like mesh radiating outward from a prominent central midrib (e.g., Hibiscus, Peepal, Mango, Rose, Mustard). Characteristic of Dicots!";
        svg.innerHTML = `
            <path d="M140,140 Q130,50 225,25 Q320,50 310,140 Q225,170 140,140 Z" fill="#15803d" fill-opacity="0.3" stroke="#22c55e" stroke-width="2"/>
            <line x1="225" y1="25" x2="225" y2="165" stroke="#86efac" stroke-width="4"/>
            <line x1="225" y1="50" x2="175" y2="70" stroke="#86efac" stroke-width="2"/>
            <line x1="225" y1="50" x2="275" y2="70" stroke="#86efac" stroke-width="2"/>
            <line x1="225" y1="80" x2="160" y2="105" stroke="#86efac" stroke-width="2"/>
            <line x1="225" y1="80" x2="290" y2="105" stroke="#86efac" stroke-width="2"/>
            <line x1="225" y1="115" x2="165" y2="135" stroke="#86efac" stroke-width="2"/>
            <line x1="225" y1="115" x2="285" y2="135" stroke="#86efac" stroke-width="2"/>
            <line x1="175" y1="70" x2="165" y2="85" stroke="#4ade80" stroke-width="1.2"/>
            <line x1="275" y1="70" x2="285" y2="85" stroke="#4ade80" stroke-width="1.2"/>
            <line x1="160" y1="105" x2="150" y2="120" stroke="#4ade80" stroke-width="1.2"/>
            <line x1="290" y1="105" x2="300" y2="120" stroke="#4ade80" stroke-width="1.2"/>
            <text x="225" y="175" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Intricate Web-like Net Pattern (Predicts Taproot System!)</text>
        `;
    } else {
        badge.textContent = "Parallel Venation (Side-by-Side Lines)";
        desc.innerHTML = "<strong>Parallel Venation:</strong> Veins run straight alongside one another from the leaf base to the tip without forming a cross-linking mesh (e.g., Grass, Maize, Wheat, Banana, Bamboo). Characteristic of Monocots!";
        svg.innerHTML = `
            <path d="M185,160 Q190,40 225,15 Q260,40 265,160 Z" fill="#15803d" fill-opacity="0.3" stroke="#22c55e" stroke-width="2"/>
            <line x1="225" y1="15" x2="225" y2="160" stroke="#86efac" stroke-width="3"/>
            <line x1="210" y1="35" x2="205" y2="160" stroke="#4ade80" stroke-width="2"/>
            <line x1="240" y1="35" x2="245" y2="160" stroke="#4ade80" stroke-width="2"/>
            <line x1="198" y1="60" x2="195" y2="160" stroke="#4ade80" stroke-width="1.5"/>
            <line x1="252" y1="60" x2="255" y2="160" stroke="#4ade80" stroke-width="1.5"/>
            <text x="225" y="175" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Straight Parallel Striped Veins (Predicts Fibrous Root System!)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 7: Sub-Soil Root System Excavator
// -------------------------------------------------------------
function setSim7Root(root) {
    const isTap = (root === 'taproot');
    document.getElementById('sim7-btn-taproot').className = isTap ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim7-btn-fibrous').className = !isTap ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim7-svg');
    const badge = document.getElementById('sim7-badge');
    const desc = document.getElementById('sim7-desc');

    if (isTap) {
        badge.textContent = "Taproot Architecture";
        desc.innerHTML = "<strong>Taproot System:</strong> Features a single, thick, dominant vertical <em>primary root</em> penetrating deep into the subsoil, with smaller lateral roots branching off (e.g., Mustard, Gram, Pea, Carrot, Mango).";
        svg.innerHTML = `
            <rect x="40" y="40" width="370" height="120" fill="#451a03" fill-opacity="0.3"/>
            <line x1="40" y1="40" x2="410" y2="40" stroke="#854d0e" stroke-width="3"/>
            <text x="50" y="32" fill="#a3e635" font-size="10" font-weight="bold">Stem above soil</text>
            <text x="50" y="60" fill="#fde68a" font-size="10">Sub-soil strata</text>
            <polygon points="221,40 229,40 226,145 224,145" fill="#f59e0b"/>
            <line x1="225" y1="65" x2="175" y2="85" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
            <line x1="225" y1="65" x2="275" y2="85" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
            <line x1="225" y1="95" x2="185" y2="115" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="225" y1="95" x2="265" y2="115" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="225" y1="120" x2="200" y2="135" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
            <line x1="225" y1="120" x2="250" y2="135" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
            <text x="225" y="172" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Single Main Primary Taproot + Lateral Rootlets</text>
        `;
    } else {
        badge.textContent = "Fibrous Root Architecture";
        desc.innerHTML = "<strong>Fibrous Root System:</strong> Lacks any primary central root. Instead, a dense cluster of slender, thread-like roots of nearly equal thickness originates directly from the base of the stem (e.g., Wheat, Grass, Maize, Onion).";
        svg.innerHTML = `
            <rect x="40" y="40" width="370" height="120" fill="#451a03" fill-opacity="0.3"/>
            <line x1="40" y1="40" x2="410" y2="40" stroke="#854d0e" stroke-width="3"/>
            <text x="50" y="32" fill="#a3e635" font-size="10" font-weight="bold">Stem above soil</text>
            <text x="50" y="60" fill="#fde68a" font-size="10">Sub-soil strata</text>
            <path d="M225,40 Q215,80 170,120" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
            <path d="M225,40 Q220,85 190,135" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
            <line x1="225" y1="40" x2="210" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
            <line x1="225" y1="40" x2="225" y2="145" stroke="#38bdf8" stroke-width="2.5"/>
            <line x1="225" y1="40" x2="240" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
            <path d="M225,40 Q230,85 260,135" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
            <path d="M225,40 Q235,80 280,120" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
            <text x="225" y="172" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Equal Hair-like Thread Roots Radiating from Stem Base</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 8: The Golden Plant Rule
// -------------------------------------------------------------
function setSim8Plant(plant) {
    const isDicot = (plant === 'dicot');
    document.getElementById('sim8-btn-dicot').className = isDicot ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim8-btn-monocot').className = !isDicot ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim8-svg');
    const badge = document.getElementById('sim8-badge');
    const desc = document.getElementById('sim8-desc');

    if (isDicot) {
        badge.textContent = "Dicot Botanical Trilogy";
        desc.innerHTML = "<strong>The Golden Dicot Rule:</strong> Reticulate Leaf Venation ↔ Taproot System ↔ Two Seed Cotyledons (e.g., Mustard, Gram, Pea, Mango). You can tell the root type just by glancing at the leaf veins—no uprooting required!";
        svg.innerHTML = `
            <rect x="25" y="30" width="115" height="100" rx="10" fill="#065f46" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
            <text x="82" y="55" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">1. Leaf Venation</text>
            <text x="82" y="80" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Reticulate</text>
            <text x="82" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(Net-like veins)</text>

            <line x1="140" y1="80" x2="165" y2="80" stroke="#f59e0b" stroke-width="3"/>

            <rect x="165" y="30" width="115" height="100" rx="10" fill="#78350f" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
            <text x="222" y="55" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">2. Root System</text>
            <text x="222" y="80" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Taproot</text>
            <text x="222" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(Deep primary)</text>

            <line x1="280" y1="80" x2="305" y2="80" stroke="#f59e0b" stroke-width="3"/>

            <rect x="305" y="30" width="120" height="100" rx="10" fill="#831843" fill-opacity="0.4" stroke="#ec4899" stroke-width="2"/>
            <text x="365" y="55" fill="#fbcfe8" font-size="11" font-weight="bold" text-anchor="middle">3. Seed Class</text>
            <text x="365" y="80" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">Dicotyledon</text>
            <text x="365" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(2 Cotyledons)</text>

            <text x="225" y="165" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">Reticulate ↔ Taproot ↔ Dicot (Invariable Law!)</text>
        `;
    } else {
        badge.textContent = "Monocot Botanical Trilogy";
        desc.innerHTML = "<strong>The Golden Monocot Rule:</strong> Parallel Leaf Venation ↔ Fibrous Root System ↔ Single Seed Cotyledon (e.g., Grass, Maize, Wheat, Rice, Bamboo).";
        svg.innerHTML = `
            <rect x="25" y="30" width="115" height="100" rx="10" fill="#075985" fill-opacity="0.4" stroke="#0284c7" stroke-width="2"/>
            <text x="82" y="55" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">1. Leaf Venation</text>
            <text x="82" y="80" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Parallel</text>
            <text x="82" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(Side-by-side lines)</text>

            <line x1="140" y1="80" x2="165" y2="80" stroke="#38bdf8" stroke-width="3"/>

            <rect x="165" y="30" width="115" height="100" rx="10" fill="#1e1b4b" fill-opacity="0.4" stroke="#6366f1" stroke-width="2"/>
            <text x="222" y="55" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">2. Root System</text>
            <text x="222" y="80" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">Fibrous</text>
            <text x="222" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(Clustered tuft)</text>

            <line x1="280" y1="80" x2="305" y2="80" stroke="#38bdf8" stroke-width="3"/>

            <rect x="305" y="30" width="120" height="100" rx="10" fill="#14532d" fill-opacity="0.4" stroke="#22c55e" stroke-width="2"/>
            <text x="365" y="55" fill="#bbf7d0" font-size="11" font-weight="bold" text-anchor="middle">3. Seed Class</text>
            <text x="365" y="80" fill="#86efac" font-size="13" font-weight="bold" text-anchor="middle">Monocotyledon</text>
            <text x="365" y="105" fill="#cbd5e1" font-size="9" text-anchor="middle">(1 Cotyledon)</text>

            <text x="225" y="165" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Parallel ↔ Fibrous ↔ Monocot (Invariable Law!)</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 9: Seed Dissection Lab
// -------------------------------------------------------------
function setSim9Seed(seed) {
    const isDicot = (seed === 'dicot');
    document.getElementById('sim9-btn-dicot').className = isDicot ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim9-btn-monocot').className = !isDicot ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim9-svg');
    const badge = document.getElementById('sim9-badge');
    const desc = document.getElementById('sim9-desc');

    if (isDicot) {
        badge.textContent = "Dicotyledon (Chickpea/Gram Split)";
        desc.innerHTML = "When a soaked chickpea seed coat is peeled away, the seed naturally parts into <strong>two swollen, starch-rich cotyledons</strong> flanking the baby plant embryo (plumule shoots upward, radicle roots downward).";
        svg.innerHTML = `
            <path d="M210,40 C160,40 150,130 210,130 Z" fill="#d97706" fill-opacity="0.6" stroke="#f59e0b" stroke-width="2"/>
            <text x="180" y="85" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Cotyledon 1</text>
            <path d="M240,40 C290,40 300,130 240,130 Z" fill="#d97706" fill-opacity="0.6" stroke="#f59e0b" stroke-width="2"/>
            <text x="270" y="85" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Cotyledon 2</text>
            <line x1="225" y1="50" x2="225" y2="120" stroke="#22c55e" stroke-width="4"/>
            <circle cx="225" cy="50" r="4" fill="#a3e635"/>
            <text x="225" y="32" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Plumule (Baby Shoot)</text>
            <circle cx="225" cy="120" r="4" fill="#fbbf24"/>
            <text x="225" y="145" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Radicle (Baby Root)</text>
            <text x="225" y="172" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Two Food-Storing Seed Leaves (Cotyledons)</text>
        `;
    } else {
        badge.textContent = "Monocotyledon (Single Cotyledon Maize)";
        desc.innerHTML = "A maize or wheat grain contains only <strong>one shield-shaped cotyledon (scutellum)</strong> closely joined to a massive starch reserve called the <em>endosperm</em>. It cannot be split into two halves!";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="55" ry="60" fill="#eab308" fill-opacity="0.4" stroke="#facc15" stroke-width="2"/>
            <path d="M175,80 C175,35 275,35 275,80 Z" fill="#fef08a" fill-opacity="0.5"/>
            <text x="225" y="60" fill="#ca8a04" font-size="11" font-weight="bold" text-anchor="middle">Endosperm (Starch)</text>
            <ellipse cx="225" cy="115" rx="28" ry="20" fill="#15803d" fill-opacity="0.6" stroke="#22c55e"/>
            <text x="225" y="118" fill="#bbf7d0" font-size="9" font-weight="bold" text-anchor="middle">Single Cotyledon</text>
            <text x="225" y="172" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Monocot: Cannot split into two equal halves</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 10: Animal Locomotion Modes & Specialized Organs
// -------------------------------------------------------------
function setSim10Mode(mode) {
    ['run', 'fly', 'swim', 'crawl', 'hop'].forEach(k => {
        const btn = document.getElementById(`sim10-btn-${k}`);
        if (btn) {
            btn.className = (k === mode) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim10-svg');
    const badge = document.getElementById('sim10-badge');
    const desc = document.getElementById('sim10-desc');

    if (mode === 'run') {
        badge.textContent = "Running: 4 Muscular Limbs";
        desc.innerHTML = "<strong>Cheetah / Deer:</strong> Quadrupedal locomotion powered by flexible spine articulation and muscular limb tendons, propelling high-speed terrestrial sprint.";
        svg.innerHTML = `
            <ellipse cx="225" cy="75" rx="40" ry="16" fill="#ca8a04"/>
            <circle cx="270" cy="65" r="12" fill="#eab308"/>
            <line x1="200" y1="85" x2="190" y2="135" stroke="#a16207" stroke-width="5" stroke-linecap="round"/>
            <line x1="210" y1="85" x2="215" y2="135" stroke="#a16207" stroke-width="5" stroke-linecap="round"/>
            <line x1="240" y1="85" x2="235" y2="135" stroke="#a16207" stroke-width="5" stroke-linecap="round"/>
            <line x1="250" y1="85" x2="265" y2="135" stroke="#a16207" stroke-width="5" stroke-linecap="round"/>
            <line x1="40" y1="135" x2="410" y2="135" stroke="#475569" stroke-width="2"/>
            <text x="225" y="165" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Muscular Jointed Legs for Ground Push-off</text>
        `;
    } else if (mode === 'fly') {
        badge.textContent = "Flying: Feathered Wings & Hollow Bones";
        desc.innerHTML = "<strong>Birds (Pigeon/Eagle):</strong> Forelimbs modified into feathered aerodynamic airfoils (wings) powered by massive breast flight muscles and lightweight pneumatic bones.";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="20" ry="12" fill="#0284c7"/>
            <circle cx="245" cy="80" r="8" fill="#38bdf8"/>
            <path d="M225,80 C180,30 150,60 215,85" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
            <path d="M225,80 C270,30 300,60 235,85" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
            <text x="225" y="165" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Modified Forelimb Airfoils Generating Aerodynamic Lift</text>
        `;
    } else if (mode === 'swim') {
        badge.textContent = "Swimming: Caudal Thrust & Stabilizing Fins";
        desc.innerHTML = "<strong>Fish:</strong> Streamlined spindle body oscillating laterally; caudal tail fin delivers forward driving thrust while dorsal and pectoral fins maintain trim and balance.";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="45" ry="20" fill="#0ea5e9" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
            <polygon points="180,85 150,65 150,105" fill="#0284c7"/>
            <polygon points="225,65 240,50 250,65" fill="#0284c7"/>
            <circle cx="255" cy="80" r="3" fill="#ffffff"/>
            <text x="225" y="165" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Lateral Body Flexion + Caudal Fin Thrust</text>
        `;
    } else if (mode === 'crawl') {
        badge.textContent = "Slithering: Belly Scales & Muscle Waves";
        desc.innerHTML = "<strong>Snakes:</strong> Legless reptiles utilizing ventral belly scales (scutes) that grip soil micro-textures while undulating body muscular waves push against ground obstacles.";
        svg.innerHTML = `
            <path d="M120,95 Q170,60 225,95 Q280,130 330,95" stroke="#15803d" stroke-width="12" fill="none" stroke-linecap="round"/>
            <circle cx="335" cy="93" r="7" fill="#166534"/>
            <circle cx="337" cy="91" r="2" fill="#facc15"/>
            <text x="225" y="165" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Ventral Scutes Anchor Body During Undulating Waves</text>
        `;
    } else {
        badge.textContent = "Hopping: Elongated Hind Limbs";
        desc.innerHTML = "<strong>Frog:</strong> Highly elongated, Z-folded muscular hind limbs act as biological spring coils, releasing kinetic energy for explosive forward aerial jumps.";
        svg.innerHTML = `
            <ellipse cx="215" cy="90" rx="22" ry="15" fill="#16a34a"/>
            <circle cx="232" cy="82" r="7" fill="#22c55e"/>
            <path d="M195,95 L175,75 L180,115" stroke="#15803d" stroke-width="6" fill="none" stroke-linecap="round"/>
            <line x1="40" y1="120" x2="410" y2="120" stroke="#475569" stroke-width="2"/>
            <text x="225" y="165" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Elastic Tendons in Elongated Hind Legs Act as Springs</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 11: Earth Habitats & Environmental Pressures
// -------------------------------------------------------------
function setSim11Biome(biome) {
    ['forest', 'desert', 'mountain', 'ocean'].forEach(k => {
        const btn = document.getElementById(`sim11-btn-${k}`);
        if (btn) {
            btn.className = (k === biome) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim11-svg');
    const badge = document.getElementById('sim11-badge');
    const desc = document.getElementById('sim11-desc');

    if (biome === 'forest') {
        badge.textContent = "Terrestrial Forest Biome";
        desc.innerHTML = "Abundant rainfall and sunlight create multi-tier canopies with extreme biodiversity—monkeys, birds, tigers, and orchids thrive across distinct vertical forest strata.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#064e3b" fill-opacity="0.3" rx="12"/>
            <circle cx="150" cy="60" r="50" fill="#047857" fill-opacity="0.6"/>
            <circle cx="280" cy="50" r="60" fill="#059669" fill-opacity="0.6"/>
            <rect x="140" y="90" width="20" height="60" fill="#78350f"/>
            <rect x="270" y="90" width="22" height="60" fill="#78350f"/>
            <line x1="20" y1="150" x2="430" y2="150" stroke="#14532d" stroke-width="4"/>
            <text x="225" y="172" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Dense Multi-Layer Canopy & Rich Humus Soil</text>
        `;
    } else if (biome === 'desert') {
        badge.textContent = "Arid Desert Biome";
        desc.innerHTML = "Extreme heat, scorching diurnal sun, freezing nights, and acute water scarcity force organisms to adopt radical water retention adaptations (cacti, camels, burrowing rats).";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#78350f" fill-opacity="0.3" rx="12"/>
            <circle cx="360" cy="45" r="22" fill="#f59e0b"/>
            <path d="M0,150 Q120,90 240,140 Q340,110 450,150 L450,180 L0,180 Z" fill="#b45309" fill-opacity="0.6"/>
            <text x="225" y="172" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">High Diurnal Heat & Acute Water Scarcity</text>
        `;
    } else if (biome === 'mountain') {
        badge.textContent = "Alpine Mountain Biome";
        desc.innerHTML = "Sub-zero temperatures, howling winds, thin atmospheric air, and heavy snow require conifer trees to be conical and animals to bear dense fur and snowshoe paws.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#0f172a" rx="12"/>
            <polygon points="80,150 160,50 240,150" fill="#334155"/>
            <polygon points="130,85 160,50 190,85" fill="#f8fafc"/>
            <polygon points="200,150 290,30 380,150" fill="#475569"/>
            <polygon points="255,80 290,30 325,80" fill="#f8fafc"/>
            <text x="225" y="172" fill="#e2e8f0" font-size="11" font-weight="bold" text-anchor="middle">Freezing Winds, Snow Loading & Low Oxygen</text>
        `;
    } else {
        badge.textContent = "Aquatic Biome (Freshwater & Marine)";
        desc.innerHTML = "Liquid water covers 71% of Earth. Aquatic organisms extract dissolved oxygen using gills and navigate viscous buoyancy through hydrodynamic body shapes.";
        svg.innerHTML = `
            <rect x="0" y="0" width="450" height="180" fill="#0369a1" fill-opacity="0.4" rx="12"/>
            <path d="M0,50 Q110,30 225,50 Q340,70 450,50" stroke="#38bdf8" stroke-width="3" fill="none"/>
            <path d="M0,80 Q110,60 225,80 Q340,100 450,80" stroke="#38bdf8" stroke-width="2" fill="none"/>
            <ellipse cx="225" cy="110" rx="35" ry="12" fill="#0284c7" stroke="#7dd3fc"/>
            <text x="225" y="172" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Viscous Drag, Hydrostatic Pressure & Dissolved Gases</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 12: Desert Adaptations Lab
// -------------------------------------------------------------
function setSim12Type(type) {
    ['cactus', 'hot_camel', 'cold_camel'].forEach(k => {
        const btn = document.getElementById(`sim12-btn-${k === 'cactus' ? 'cactus' : (k === 'hot_camel' ? 'hot' : 'cold')}`);
        if (btn) {
            btn.className = (k === type) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim12-svg');
    const badge = document.getElementById('sim12-badge');
    const desc = document.getElementById('sim12-desc');

    if (type === 'cactus') {
        badge.textContent = "Cactus: Spines & Succulent Stem";
        desc.innerHTML = "Leaves are reduced to <strong>sharp spines</strong> to prevent transpiration water loss. Photosynthesis is carried out entirely by the <strong>fleshy, wax-coated green stem</strong> which stores water!";
        svg.innerHTML = `
            <rect x="205" y="45" width="40" height="100" rx="20" fill="#15803d" stroke="#22c55e" stroke-width="3"/>
            <path d="M205,90 H175 V65" stroke="#22c55e" stroke-width="14" fill="none" stroke-linecap="round"/>
            <path d="M245,80 H275 V60" stroke="#22c55e" stroke-width="14" fill="none" stroke-linecap="round"/>
            <line x1="205" y1="60" x2="195" y2="58" stroke="#facc15" stroke-width="2"/>
            <line x1="245" y1="60" x2="255" y2="58" stroke="#facc15" stroke-width="2"/>
            <line x1="205" y1="120" x2="195" y2="120" stroke="#facc15" stroke-width="2"/>
            <line x1="245" y1="120" x2="255" y2="120" stroke="#facc15" stroke-width="2"/>
            <line x1="40" y1="145" x2="410" y2="145" stroke="#78350f" stroke-width="2"/>
            <text x="225" y="172" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Stem Photosynthesizes + Spines Eliminate Evaporation</text>
        `;
    } else if (type === 'hot_camel') {
        badge.textContent = "Thar Hot Desert Camel (Single Hump)";
        desc.innerHTML = "<strong>Ship of the Desert:</strong> One fatty hump for energy, extremely long legs elevating body above scorching sand, wide padded hooves that don't sink, and concentrated urine to conserve every drop.";
        svg.innerHTML = `
            <ellipse cx="220" cy="80" rx="35" ry="20" fill="#b45309"/>
            <circle cx="215" cy="55" r="16" fill="#92400e"/>
            <path d="M255,80 Q275,50 280,35" stroke="#b45309" stroke-width="10" fill="none" stroke-linecap="round"/>
            <line x1="200" y1="100" x2="195" y2="145" stroke="#b45309" stroke-width="5"/>
            <line x1="235" y1="100" x2="240" y2="145" stroke="#b45309" stroke-width="5"/>
            <ellipse cx="195" cy="145" rx="8" ry="4" fill="#78350f"/>
            <ellipse cx="240" cy="145" rx="8" ry="4" fill="#78350f"/>
            <line x1="40" y1="148" x2="410" y2="148" stroke="#d97706" stroke-width="2"/>
            <text x="225" y="172" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Padded Hooves + Long Clearance Above Hot Sand</text>
        `;
    } else {
        badge.textContent = "Ladakh Bactrian Camel (Two Humps)";
        desc.innerHTML = "<strong>Cold Desert Adaptations:</strong> Found in high-altitude Nubra Valley (Ladakh). Possesses <strong>two fat-storing humps</strong> and a shaggy woolly coat that insulates against bone-chilling sub-zero Himalayan winds!";
        svg.innerHTML = `
            <ellipse cx="220" cy="85" rx="42" ry="22" fill="#78350f"/>
            <circle cx="200" cy="58" r="14" fill="#451a03"/>
            <circle cx="240" cy="58" r="14" fill="#451a03"/>
            <path d="M180,105 Q220,115 260,105" stroke="#d97706" stroke-width="6" fill="none"/>
            <line x1="195" y1="105" x2="195" y2="145" stroke="#78350f" stroke-width="7"/>
            <line x1="245" y1="105" x2="245" y2="145" stroke="#78350f" stroke-width="7"/>
            <text x="225" y="172" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Two Humps + Heavy Wool Coat Against Ladakh Freezing Winds</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 13: Mountain Adaptations (Alpine Snow-Shedding)
// -------------------------------------------------------------
function setSim13Subject(subj) {
    const isConifer = (subj === 'conifer');
    document.getElementById('sim13-btn-conifer').className = isConifer ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim13-btn-leopard').className = !isConifer ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim13-svg');
    const badge = document.getElementById('sim13-badge');
    const desc = document.getElementById('sim13-desc');

    if (isConifer) {
        badge.textContent = "Conical Deodar Conifer";
        desc.innerHTML = "<strong>Conical Slope Morphology:</strong> Deodar and pine trees have sloping, cone-shaped branches and needle-like leaves with a waxy cuticle. Snow and rainwater slide right off without breaking branches!";
        svg.innerHTML = `
            <rect x="220" y="120" width="10" height="30" fill="#78350f"/>
            <polygon points="225,30 180,75 270,75" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
            <polygon points="225,65 165,105 285,105" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
            <polygon points="225,95 150,135 300,135" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
            <path d="M175,70 L155,90" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
            <path d="M275,70 L295,90" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
            <text x="225" y="172" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">Sloping Conical Branches Naturally Shed Heavy Snow Loads</text>
        `;
    } else {
        badge.textContent = "Snow Leopard: Snowshoe Paws & Dense Fur";
        desc.innerHTML = "<strong>Apex Alpine Predator:</strong> Massive wide paws covered with thick fur act as snowshoes, preventing the leopard from sinking in deep powder. Its long bushy tail wraps around its face for warmth!";
        svg.innerHTML = `
            <ellipse cx="225" cy="80" rx="38" ry="18" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="210" cy="78" r="3" fill="#334155"/>
            <circle cx="235" cy="82" r="3" fill="#334155"/>
            <ellipse cx="195" cy="125" rx="12" ry="8" fill="#cbd5e1"/>
            <ellipse cx="255" cy="125" rx="12" ry="8" fill="#cbd5e1"/>
            <path d="M190,80 Q160,110 180,125" stroke="#cbd5e1" stroke-width="10" fill="none" stroke-linecap="round"/>
            <line x1="40" y1="133" x2="410" y2="133" stroke="#f1f5f9" stroke-width="3"/>
            <text x="225" y="172" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Wide Fur-Padded Paws Distribute Weight to Walk on Snow</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 14: Ocean Life & Fins
// -------------------------------------------------------------
function setSim14Feature(feat) {
    ['streamline', 'fins', 'gills', 'scales'].forEach(k => {
        const btn = document.getElementById(`sim14-btn-${k}`);
        if (btn) {
            btn.className = (k === feat) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim14-svg');
    const badge = document.getElementById('sim14-badge');
    const desc = document.getElementById('sim14-desc');

    if (feat === 'streamline') {
        badge.textContent = "Streamlined Spindle Shape";
        desc.innerHTML = "Both head and tail taper smoothly while the middle body is wider. Water streamlines slide past without turbulence or resistance, allowing effortless forward gliding!";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="60" ry="24" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
            <path d="M120,60 Q225,45 330,60" stroke="#7dd3fc" stroke-width="2" stroke-dasharray="4,4" fill="none"/>
            <path d="M120,110 Q225,125 330,110" stroke="#7dd3fc" stroke-width="2" stroke-dasharray="4,4" fill="none"/>
            <text x="225" y="172" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Tapered Ends Drastically Reduce Viscous Hydrodynamic Drag</text>
        `;
    } else if (feat === 'fins') {
        badge.textContent = "Fins: Steering, Balance & Caudal Thrust";
        desc.innerHTML = "Pectoral and pelvic fins steer and brake; the dorsal fin maintains upright stability (prevents rolling); and the caudal tail fin flexes side-to-side to generate driving thrust!";
        svg.innerHTML = `
            <ellipse cx="225" cy="85" rx="55" ry="22" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8"/>
            <polygon points="215,63 235,40 250,63" fill="#f59e0b"/>
            <polygon points="170,85 130,55 130,115" fill="#ef4444"/>
            <polygon points="245,95 260,115 235,105" fill="#10b981"/>
            <text x="225" y="172" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Red: Caudal (Thrust) | Yellow: Dorsal (Balance) | Green: Pectoral (Steer)</text>
        `;
    } else if (feat === 'gills') {
        badge.textContent = "Gills: Dissolved Oxygen Absorption";
        desc.innerHTML = "Gills are densely packed with microscopic capillary blood vessels. Water taken through the mouth washes over gill filaments, where dissolved oxygen diffuses into the blood!";
        svg.innerHTML = `
            <circle cx="225" cy="85" r="45" fill="#1e293b" stroke="#64748b"/>
            <path d="M210,60 Q230,85 210,110" stroke="#ef4444" stroke-width="4" fill="none"/>
            <path d="M220,60 Q240,85 220,110" stroke="#ef4444" stroke-width="4" fill="none"/>
            <path d="M230,60 Q250,85 230,110" stroke="#ef4444" stroke-width="4" fill="none"/>
            <line x1="170" y1="85" x2="200" y2="85" stroke="#38bdf8" stroke-width="3"/>
            <text x="225" y="172" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Dissolved O2 Absorbed Across Thin Capillary Membranes</text>
        `;
    } else {
        badge.textContent = "Slippery Waterproof Scales";
        desc.innerHTML = "Overlapping scales covered with an oily mucus layer waterproof the fish's skin, prevent osmotic bloat, protect from parasitic infection, and smooth water flow.";
        svg.innerHTML = `
            <rect x="150" y="50" width="150" height="70" rx="8" fill="#075985" fill-opacity="0.4" stroke="#0ea5e9"/>
            <path d="M170,70 Q180,85 190,70 Q200,85 210,70 Q220,85 230,70" stroke="#7dd3fc" stroke-width="2" fill="none"/>
            <path d="M180,85 Q190,100 200,85 Q210,100 220,85 Q230,100 240,85" stroke="#7dd3fc" stroke-width="2" fill="none"/>
            <text x="225" y="172" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Mucus Coat Waterproofs Skin & Minimizes Skin-Friction Drag</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 15: Wildlife Conservation & Sacred Groves
// -------------------------------------------------------------
function setSim15Reserve(res) {
    ['tiger', 'cheetah', 'groves'].forEach(k => {
        const btn = document.getElementById(`sim15-btn-${k}`);
        if (btn) {
            btn.className = (k === res) ?
                'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
                'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
        }
    });

    const svg = document.getElementById('sim15-svg');
    const badge = document.getElementById('sim15-badge');
    const desc = document.getElementById('sim15-desc');

    if (res === 'tiger') {
        badge.textContent = "Project Tiger (Launched 1973)";
        desc.innerHTML = "One of the world's most successful conservation initiatives! Protecting the apex Royal Bengal Tiger secured entire umbrella habitats—from Corbett to Ranthambore and Sundarbans.";
        svg.innerHTML = `
            <circle cx="225" cy="80" r="45" fill="#c2410c" fill-opacity="0.3" stroke="#f97316" stroke-width="2"/>
            <text x="225" y="75" fill="#fed7aa" font-size="13" font-weight="bold" text-anchor="middle">Project Tiger</text>
            <text x="225" y="95" fill="#f97316" font-size="11" font-weight="bold" text-anchor="middle">1973 - Present</text>
            <text x="225" y="172" fill="#fdba74" font-size="11" font-weight="bold" text-anchor="middle">Umbrella Protection: Conserving Apex Predator Preserves Whole Forests</text>
        `;
    } else if (res === 'cheetah') {
        badge.textContent = "Cheetah Reintroduction (Kuno 2022)";
        desc.innerHTML = "Historic re-wilding project restoring the extinct Asiatic cheetah niche to India! African cheetahs brought to Kuno National Park revive open grassland ecosystems.";
        svg.innerHTML = `
            <circle cx="225" cy="80" r="45" fill="#854d0e" fill-opacity="0.3" stroke="#eab308" stroke-width="2"/>
            <text x="225" y="75" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle">Kuno Re-wilding</text>
            <text x="225" y="95" fill="#eab308" font-size="11" font-weight="bold" text-anchor="middle">September 2022</text>
            <text x="225" y="172" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Grassland Ecosystem Restoration & Biodiversity Recovery</text>
        `;
    } else {
        badge.textContent = "Sacred Groves (Community Forest Patches)";
        desc.innerHTML = "Traditional community protection: <em>Devrais</em> (Maharashtra), <em>Orans</em> (Rajasthan), and <em>Kavu</em> (Kerala) protect pristine undisturbed pockets of virgin endemic flora and sacred fauna!";
        svg.innerHTML = `
            <rect x="120" y="40" width="210" height="80" rx="12" fill="#065f46" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="70" fill="#a7f3d0" font-size="13" font-weight="bold" text-anchor="middle">Devrais, Orans & Kavu</text>
            <text x="225" y="90" fill="#6ee7b7" font-size="10" text-anchor="middle">Community Faith-Based Sanctuaries</text>
            <text x="225" y="172" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Zero Axe Logging: Preserving Endemic Gene Pools For Centuries</text>
        `;
    }
}

// -------------------------------------------------------------
// Simulator 16: Heroes of Biodiversity Field Journal
// -------------------------------------------------------------
function setSim16Hero(hero) {
    const isAmmal = (hero === 'ammal');
    document.getElementById('sim16-btn-ammal').className = isAmmal ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
    document.getElementById('sim16-btn-ali').className = !isAmmal ?
        'py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition' :
        'py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';

    const svg = document.getElementById('sim16-svg');
    const badge = document.getElementById('sim16-badge');
    const desc = document.getElementById('sim16-desc');

    if (isAmmal) {
        badge.textContent = "Dr. E.K. Janaki Ammal (1897-1984)";
        desc.innerHTML = "<strong>Pioneering Botanist & Cytogeneticist:</strong> First Indian woman with a doctorate in botany! Developed sweet indigenous sugarcane hybrids, headed Botanical Survey of India, and spearheaded the historic <em>Save Silent Valley</em> rainforest campaign.";
        svg.innerHTML = `
            <rect x="100" y="35" width="250" height="90" rx="10" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
            <text x="225" y="65" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">Dr. E.K. Janaki Ammal</text>
            <text x="225" y="85" fill="#a7f3d0" font-size="10" text-anchor="middle">Sugarcane Genetics & BSI Director</text>
            <text x="225" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Champion of 'Save Silent Valley' Movement</text>
            <text x="225" y="172" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Saved Kerala's Tropical Evergreen Rainforest from Submergence</text>
        `;
    } else {
        badge.textContent = "Dr. Salim Ali (1896-1987)";
        desc.innerHTML = "<strong>The Birdman of India:</strong> Conducted pioneering nationwide bird surveys, authored the monumental 10-volume <em>Handbook of the Birds of India and Pakistan</em>, and saved Keoladeo Ghana & Ranganathittu Bird Sanctuaries!";
        svg.innerHTML = `
            <rect x="100" y="35" width="250" height="90" rx="10" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
            <text x="225" y="65" fill="#7dd3fc" font-size="13" font-weight="bold" text-anchor="middle">Dr. Salim Ali (Birdman of India)</text>
            <text x="225" y="85" fill="#bae6fd" font-size="10" text-anchor="middle">Keoladeo & Ranganathittu Sanctuaries</text>
            <text x="225" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Father of Modern Indian Ornithology</text>
            <text x="225" y="172" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Instrumental in Creating India's Premier Bird Sanctuaries</text>
        `;
    }
}

// Global Initialization
window.addEventListener('DOMContentLoaded', () => {
    updateSlideDisplay();
    setSim1Spot('bird');
    setSim2Link('shelter');
    setSim3Criterion('stem');
    setSim4Category('tree');
    setSim5Type('climber');
    setSim6Venation('reticulate');
    setSim7Root('taproot');
    setSim8Plant('dicot');
    setSim9Seed('dicot');
    setSim10Mode('run');
    setSim11Biome('forest');
    setSim12Type('cactus');
    setSim13Subject('conifer');
    setSim14Feature('streamline');
    setSim15Reserve('tiger');
    setSim16Hero('ammal');

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
        if (e.key === 'Escape') closeSolutionModal();
    });
});
'''

with open(".agents/class6_science_ch2_js.py", "w", encoding="utf-8") as f:
    f.write('"""\nJavaScript Code for Class 6 Science Chapter 2 Interactive Lab\n"""\n\n')
    f.write('JS_CODE = ' + repr(js_body) + '\n')

print("Generated updated .agents/class6_science_ch2_js.py successfully.")

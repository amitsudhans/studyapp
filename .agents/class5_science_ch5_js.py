"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 5: Our Vibrant Country
Enhanced with robust Indian Male Voice priority, female voice filtering, Voice Selector UI, and 16 bespoke simulators.
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
            globalBtn.classList.add("bg-orange-500/30", "border-orange-500");
        } else {
            globalBtn.classList.remove("bg-orange-500/30", "border-orange-500");
        }
    }
    if (currentSlideSpeaking) {
        const badge = document.getElementById("slide-audio-badge-" + currentSlideSpeaking);
        const btn = document.getElementById("slide-audio-btn-" + currentSlideSpeaking);
        if (badge) {
            badge.textContent = speaking ? "Narrating..." : "Audio Lecture Ready";
            badge.className = speaking ? "px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 animate-pulse" : "px-2 py-0.5 rounded text-xs font-semibold bg-orange-500/20 text-orange-300 border border-orange-500/30";
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

    // Split text into coherent sentences
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

// Simulator 1: Flagpole & Petal Shower
let flagState = "base";
function hoistFlag() {
    const flag = document.getElementById("flagGroup");
    const text = document.getElementById("flagStatusText");
    if (flag) {
        flag.setAttribute("transform", "translate(202, 25)");
    }
    flagState = "hoisted";
    if (text) {
        text.innerHTML = "Flag hoisted to top! Click <strong>Unfurl Petals</strong> to shower fragrant roses!";
    }
}

function unfurlFlag() {
    const petals = document.getElementById("petalShower");
    const text = document.getElementById("flagStatusText");
    if (flagState !== "hoisted") {
        hoistFlag();
    }
    if (petals) {
        petals.classList.remove("hidden");
    }
    if (text) {
        text.innerHTML = "🌸 The tricolour is unfurled! Petals flutter down as Jana Gana Mana resounds across the school!";
    }
}

// Simulator 2: Preamble Explorer
function selectPreambleWord(word) {
    const details = document.getElementById("preambleDetails");
    if (!details) return;

    if (word === "justice") {
        details.innerHTML = "<strong class='text-indigo-400 block mb-1'>⚖️ JUSTICE (Social, Economic, Political):</strong> Assures that laws protect the vulnerable, court decisions are honest and fair, and every citizen enjoys safety regardless of background.";
    } else if (word === "liberty") {
        details.innerHTML = "<strong class='text-sky-400 block mb-1'>🕊️ LIBERTY of Thought, Expression & Belief:</strong> Grants every individual the freedom to express creative ideas, learn, and practice their faith without fear.";
    } else if (word === "equality") {
        details.innerHTML = "<strong class='text-emerald-400 block mb-1'>🤝 EQUALITY of Status and Opportunity:</strong> Forbids discrimination, ensuring boys and girls from any community receive equal educational and career opportunities.";
    } else if (word === "fraternity") {
        details.innerHTML = "<strong class='text-amber-400 block mb-1'>🌺 FRATERNITY (Dignity & National Unity):</strong> Nurtures a deep spirit of common brotherhood among all Indians, transcending regional or linguistic differences.";
    }
}

// Simulator 3: Currency Detective
function scanCurrencyFeature(feat) {
    const box = document.getElementById("currencyScanResult");
    const wm = document.getElementById("gandhiWatermark");
    const th = document.getElementById("securityThread");
    if (!box) return;

    if (feat === "watermark") {
        if (wm) wm.setAttribute("opacity", "0.85");
        box.innerHTML = "💡 <strong>Optical Watermark Revealed:</strong> Backlight illumination reveals Mahatma Gandhi's three-dimensional watermark portrait inside the white window.";
    } else if (feat === "thread") {
        if (th) th.setAttribute("stroke", "#0284c7");
        box.innerHTML = "🟢 <strong>Optically Variable Thread:</strong> When tilted in light, the vertical security thread shifts colour from vivid green to rich blue, exposing 'RBI' micro-lettering.";
    } else if (feat === "swachh") {
        box.innerHTML = "👓 <strong>Swachh Bharat Spectacles:</strong> The historic glasses of Mahatma Gandhi with 'Swachh' on the left lens and 'Bharat' on the right lens urge national cleanliness.";
    }
}

// Simulator 4: Accessibility Tester & MANI App
function setAccessibilityNote(denom) {
    const title = document.getElementById("tactileNoteTitle");
    const badge = document.getElementById("tactileShapeBadge");
    const desc = document.getElementById("tactileDesc");

    if (denom === 100) {
        if (title) title.textContent = "₹100 Banknote";
        if (badge) { badge.textContent = "Triangle Symbol"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300"; }
        if (desc) desc.innerHTML = "<p><strong>Raised Bleed Lines:</strong> 4 lines on left and right borders.</p><p><strong>Tactile Shape:</strong> Raised triangle above the emblem.</p>";
    } else if (denom === 200) {
        if (title) title.textContent = "₹200 Banknote";
        if (badge) { badge.textContent = "Circles & 4 Lines"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300"; }
        if (desc) desc.innerHTML = "<p><strong>Raised Bleed Lines:</strong> 4 lines with 2 circular dots between them.</p><p><strong>Tactile Shape:</strong> Raised circle symbol.</p>";
    } else if (denom === 500) {
        if (title) title.textContent = "₹500 Banknote";
        if (badge) { badge.textContent = "Circle Symbol"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300"; }
        if (desc) desc.innerHTML = "<p><strong>Raised Bleed Lines:</strong> 5 diagonal lines on both edges.</p><p><strong>Tactile Shape:</strong> Raised circular shape above Ashoka Pillar.</p>";
    }
}

function triggerMANIVoice() {
    const out = document.getElementById("maniAudioOutput");
    if (!out) return;
    out.classList.remove("hidden");
    out.innerHTML = "🔊 <strong>MANI App Voice:</strong> 'Five Hundred Rupees (पाँच सौ रुपये) detected.' Note successfully identified for accessibility!";
}

// Simulator 5: National Emblem Perspective
function showEmblemPerspective(view) {
    const box = document.getElementById("emblemInfoBox");
    if (!box) return;

    if (view === "front") {
        box.innerHTML = "🏛️ <strong>2D National Emblem View:</strong> Three Asiatic lions are visible facing left, front, and right on the abacus above the Ashoka Chakra, galloping horse, and bull.";
    } else {
        box.innerHTML = "🦁 <strong>3D Sarnath Reality:</strong> Four majestic lions sit back-to-back facing all 4 cardinal directions (North, South, East, West), guarding the realm in complete vigilance!";
    }
}

// Simulator 6: Tiger Camouflage
let camoActive = true;
function toggleTigerCamouflage() {
    const reeds = document.getElementById("tallGrassReeds");
    const btn = document.getElementById("camoToggleBtn");
    const text = document.getElementById("tigerCamoText");

    if (camoActive) {
        if (reeds) reeds.style.display = "none";
        if (btn) btn.innerHTML = "🌾 Restore Grass Reeds";
        if (text) text.innerHTML = "Tiger outline is fully exposed! Notice how vital tall grassland and bamboo are for predatory stealth.";
        camoActive = false;
    } else {
        if (reeds) reeds.style.display = "block";
        if (btn) btn.innerHTML = "🌾 Remove Grass Reeds";
        if (text) text.innerHTML = "Camouflage restored! Vertical dark stripes dissolve into grass shadows, concealing the apex hunter.";
        camoActive = true;
    }
}

function showTigerCensus() {
    const text = document.getElementById("tigerCamoText");
    if (text) {
        text.innerHTML = "📈 <strong>Project Tiger Triumph:</strong> From barely 1,800 tigers in 1973, India's strict reserve network now shelters over 3,682 wild tigers—75% of the planet's total!";
    }
}

// Simulator 7: Peacock Photonic Optics
function setPeacockOptics(val) {
    const label = document.getElementById("lightAngleVal");
    const desc = document.getElementById("featherOpticDesc");
    const eyes = [document.getElementById("eye1"), document.getElementById("eye2"), document.getElementById("eye3"), document.getElementById("eye4"), document.getElementById("eye5")];

    let color = "#0369a1";
    let descText = "";

    if (val < 30) {
        color = "#15803d";
        if (label) label.textContent = val + "° (Emerald Green)";
        descText = "Low sunbeam angles trigger light wave interference reflecting vibrant emerald green!";
    } else if (val < 60) {
        color = "#0284c7";
        if (label) label.textContent = val + "° (Cobalt Blue)";
        descText = "Direct midday light reflects intense cobalt sapphire blue from the 2D keratin lattice.";
    } else {
        color = "#4338ca";
        if (label) label.textContent = val + "° (Violet Blue)";
        descText = "High grazing angle shifts reflected photons toward deep indigo and shimmering violet.";
    }

    eyes.forEach(e => {
        if (e) e.setAttribute("fill", color);
    });

    if (desc) desc.textContent = descText;
}

// Simulator 8: Sacred Symbols
function selectSacredSymbol(sym) {
    const disp = document.getElementById("sacredSymbolDisplay");
    if (!disp) return;

    if (sym === "banyan") {
        disp.innerHTML = "<strong class='text-emerald-400 block mb-1'>🌳 BANYAN TREE (Ficus benghalensis):</strong> Sends woody aerial prop roots downward into the soil that turn into supportive secondary trunks, allowing a single tree to create a whole shaded forest!";
    } else if (sym === "lotus") {
        disp.innerHTML = "<strong class='text-pink-400 block mb-1'>🪷 LOTUS FLOWER (Nelumbo nucifera):</strong> Rises clean above stagnant mud. Its leaves have microscopic wax bumps that force water droplets to roll off, sweeping dirt away in the famous self-cleaning Lotus Effect.";
    } else if (sym === "dolphin") {
        disp.innerHTML = "<strong class='text-cyan-400 block mb-1'>🐬 GANGES RIVER DOLPHIN (Platanista gangetica):</strong> Navigates murky silt-filled waters without functional eyes by sending ultrasonic clicks and listening to the returning sound echoes.";
    } else if (sym === "elephant") {
        disp.innerHTML = "<strong class='text-amber-400 block mb-1'>🐘 INDIAN ELEPHANT (Elephas maximus):</strong> The beloved National Heritage Animal. Acts as a mega-gardener of forests by clearing trails and dispersing seeds across miles.";
    }
}

// Simulator 9: Greetings & Scripts
function displayGreeting(lang) {
    const word = document.getElementById("greetingWord");
    const script = document.getElementById("greetingScript");
    const desc = document.getElementById("greetingDesc");

    if (lang === "hindi") {
        if (word) word.textContent = "नमस्ते (Namaste)";
        if (script) script.textContent = "Devanagari Script";
        if (desc) desc.textContent = "Rooted in Sanskrit, meaning 'I bow to the divine presence within you'. Written in Devanagari, derived from ancient Brahmi.";
    } else if (lang === "tamil") {
        if (word) word.textContent = "வணக்கம் (Vanakkam)";
        if (script) script.textContent = "Tamil Script";
        if (desc) desc.textContent = "Ancient classical Dravidian greeting expressing warmth and deep respect. Tamil literature dates back over 2,000 years to the Sangam era.";
    } else if (lang === "bengali") {
        if (word) word.textContent = "নমস্কার (Nomoshkar)";
        if (script) script.textContent = "Eastern Nagari / Bengali Script";
        if (desc) desc.textContent = "Graceful greeting used across Bengal, rich with literary heritage from Rabindranath Tagore and Bankim Chandra Chatterjee.";
    } else if (lang === "punjabi") {
        if (word) word.textContent = "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ (Sat Sri Akal)";
        if (script) script.textContent = "Gurmukhi Script";
        if (desc) desc.textContent = "Spirited greeting meaning 'Truth is the Timeless Divine Lord', celebrating steadfast righteousness and courage.";
    }
}

// Simulator 10: Garden vs Forest
function triggerEcoCrisis(type) {
    const gEmoji = document.getElementById("gardenEmoji");
    const gStatus = document.getElementById("gardenStatus");
    const fEmoji = document.getElementById("forestEmoji");
    const fStatus = document.getElementById("forestStatus");
    const res = document.getElementById("ecoSimResult");

    if (type === "pest") {
        if (gEmoji) gEmoji.textContent = "🥀 🥀 🥀";
        if (gStatus) { gStatus.textContent = "Total monoculture crop failure!"; gStatus.className = "text-[10px] text-rose-400 block font-bold"; }
        if (fEmoji) fEmoji.textContent = "🌲 🐞 🐦 🌿";
        if (fStatus) { fStatus.textContent = "Resilient! Ladybirds & birds ate the pests."; fStatus.className = "text-[10px] text-emerald-400 block font-bold"; }
        if (res) res.innerHTML = "💥 <strong>Result:</strong> Monocultures lack defense when pests strike. The biodiverse forest sustained natural balance!";
    } else {
        if (gEmoji) gEmoji.textContent = "🌹 🌹 🌹";
        if (gStatus) { gStatus.textContent = "Healthy under artificial care"; gStatus.className = "text-[10px] text-slate-400 block"; }
        if (fEmoji) fEmoji.textContent = "🌲 🍄 🐦 🌿";
        if (fStatus) { fStatus.textContent = "Thriving self-sustaining web"; fStatus.className = "text-[10px] text-slate-400 block"; }
        if (res) res.textContent = "Ecosystems reset to normal baseline.";
    }
}

// Simulator 11: Regional Headgear
function equipHeadgear(item) {
    const name = document.getElementById("headgearName");
    const region = document.getElementById("headgearRegion");
    const phys = document.getElementById("headgearPhysics");

    if (item === "saafa") {
        if (name) name.textContent = "Rajasthani Saafa (Pagri)";
        if (region) { region.textContent = "Thar Desert, Rajasthan"; region.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500/20 text-orange-300"; }
        if (phys) phys.textContent = "Multi-metre folded cotton creates insulating dead-air pockets, shielding the head from 48°C radiant solar rays.";
    } else if (item === "topi") {
        if (name) name.textContent = "Himachali Kullu Topi";
        if (region) { region.textContent = "Himalayan Ranges, Himachal Pradesh"; region.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300"; }
        if (phys) phys.textContent = "Tightly felted wool fibres trap body heat, preventing cranial thermal loss during sub-zero mountain freezes.";
    } else if (item === "peta") {
        if (name) name.textContent = "Mysore Peta (Karnataka)";
        if (region) { region.textContent = "Southern Heritage, Karnataka"; region.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300"; }
        if (phys) phys.textContent = "Golden zari silk turban worn during university convocations and weddings as a traditional mark of scholarship and honor.";
    } else if (item === "helmet") {
        if (name) name.textContent = "Shock-Absorbing Safety Helmet";
        if (region) { region.textContent = "Universal Modern Safety Standards"; region.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300"; }
        if (phys) phys.textContent = "Tough polycarbonate shell disperses kinetic impact; internal EPS foam compresses gradually, preventing severe brain trauma.";
    }
}

// Simulator 12: Indian Drum Acoustics
function setDrumTuning(mode) {
    const patch = document.getElementById("syahiPatchCircle");
    const res = document.getElementById("acousticSoundResult");

    if (mode === "unloaded") {
        if (patch) patch.setAttribute("fill", "#e2e8f0");
        if (res) res.innerHTML = "⚪ <strong>Unloaded Membrane:</strong> Vibrates in non-integer Bessel modes, producing harsh discordant noise without a musical note.";
    } else {
        if (patch) patch.setAttribute("fill", "#0f172a");
        if (res) res.innerHTML = "⚫ <strong>Syahi Loaded:</strong> Iron filings and starch mass shift circular vibration into harmonic overtones (1:2:3:4), tuning the drum to match the tanpura!";
    }
}

// Simulator 13: Dance Mudras
function selectMudra(mudra) {
    const name = document.getElementById("mudraName");
    const dance = document.getElementById("mudraDance");
    const meaning = document.getElementById("mudraMeaning");

    if (mudra === "mayura") {
        if (name) name.textContent = "Mayura Mudra (Peacock Gesture)";
        if (dance) dance.textContent = "Bharatanatyam, Kathak & Odissi";
        if (meaning) meaning.textContent = "Ring finger touches the thumb while other fingers stand straight like peacock feathers, used to depict peacocks, applying sacred tilak, and birds.";
    } else if (mudra === "hamsasya") {
        if (name) name.textContent = "Hamsasya Mudra (Swan Beak)";
        if (dance) dance.textContent = "Classical Kathakali & Kuchipudi";
        if (meaning) meaning.textContent = "Thumb and index finger press together to portray a delicate swan, holding a single pearl, or painting fine lines.";
    } else if (mudra === "padma") {
        if (name) name.textContent = "Padmakosha Mudra (Lotus Bud)";
        if (dance) dance.textContent = "All 8 Classical Dance Styles";
        if (meaning) meaning.textContent = "Fingers curved like circular petals opening outward to depict the blossoming of a holy lotus flower or offering fruit.";
    }
}

// Simulator 14: Ayurvedic Bioactive Lab
function extractBioactive(herb) {
    const title = document.getElementById("herbTitle");
    const details = document.getElementById("herbDetails");

    if (herb === "turmeric") {
        if (title) title.textContent = "Turmeric (Haldi / Haridra)";
        if (details) details.innerHTML = "Contains <strong>Curcumin</strong>: a powerful anti-inflammatory antioxidant that inhibits bacterial enzymes and accelerates skin tissue regeneration.";
    } else if (herb === "tulsi") {
        if (title) title.textContent = "Holy Basil (Tulsi)";
        if (details) details.innerHTML = "Rich in <strong>Eugenol & Camphene</strong>: volatile aromatic terpenes that clear respiratory pathways and boost immune antibody production.";
    } else if (herb === "neem") {
        if (title) title.textContent = "Neem (Azadirachta indica)";
        if (details) details.innerHTML = "Yields <strong>Azadirachtin & Nimbidin</strong>: bitter compounds that disrupt bacterial cell membranes and protect against fungal skin infections.";
    }
}

function testPranayamaBreathing() {
    const eff = document.getElementById("pranayamaEffect");
    if (!eff) return;
    eff.classList.remove("hidden");
    eff.innerHTML = "🧘 <strong>Biomedical Effect:</strong> 60 seconds of slow rhythmic inhalation (Puraka) and exhalation (Rechaka) stimulates the vagus nerve, reducing heart rate from 92 bpm down to 68 bpm and enhancing focus!";
}

// Simulator 15: Modern Innovation Hub
function runTechDemo(tech) {
    const title = document.getElementById("techTitle");
    const badge = document.getElementById("techBadge");
    const desc = document.getElementById("techDesc");

    if (tech === "isro") {
        if (title) title.textContent = "Chandrayaan-3 South Pole Landing";
        if (badge) { badge.textContent = "Space Exploration"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500/20 text-orange-300"; }
        if (desc) desc.textContent = "On 23 August 2023, ISRO's Vikram lander made history as the world's first touchdown near the lunar south pole, detecting sulphur and water-ice signatures.";
    } else if (tech === "upi") {
        if (title) title.textContent = "UPI Real-Time Payments";
        if (badge) { badge.textContent = "Digital Public Good"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300"; }
        if (desc) desc.textContent = "Powers over 13 billion transactions monthly with instant QR scanning, connecting roadside farmers and metropolitan stores with zero transaction friction.";
    } else if (tech === "train") {
        if (title) title.textContent = "Vande Bharat Semi-High-Speed Rail";
        if (badge) { badge.textContent = "Indigenous Engineering"; badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300"; }
        if (desc) desc.textContent = "Aerodynamic electric multiple-unit train built at Integral Coach Factory (ICF) Chennai, featuring regenerative braking and cutting travel time across Indian states.";
    }
}

// Simulator 16: The Vibrant Unity Tapestry
let strandsCount = 4;
function weaveTapestry(type) {
    const loom = document.getElementById("tapestryLoom");
    const badge = document.getElementById("threadCountBadge");
    const msg = document.getElementById("tapestryMessage");
    strandsCount++;

    let strandEmoji = "🧵";
    let typeName = "Strand";
    if (type === "language") { strandEmoji = "🗣️"; typeName = "Language"; }
    else if (type === "festival") { strandEmoji = "🪔"; typeName = "Festival"; }
    else if (type === "science") { strandEmoji = "🚀"; typeName = "Science & Tech"; }
    else if (type === "dance") { strandEmoji = "💃"; typeName = "Classical Dance"; }

    if (loom) loom.innerHTML += " " + strandEmoji;
    if (badge) badge.textContent = strandsCount + " Cultural Strands Woven";
    if (msg) msg.innerHTML = "✨ Added <strong>" + typeName + "</strong> to our national fabric! The more threads we interweave, the stronger and more magnificent India becomes!";
}

// Document Load Init
document.addEventListener("DOMContentLoaded", () => {
    showSlide(1);
    populateVoiceList();
});
'''

print(f"Updated JS_CODE authored ({len(JS_CODE)} bytes)!")

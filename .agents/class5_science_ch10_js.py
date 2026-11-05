"""
Interactive JavaScript Engine for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
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

    // 3. Priority 3: Any Indian voice that is NOT female
    const inNonFemale = inVoices.filter(v => !isFemaleVoice(v));
    if (inNonFemale.length > 0) return inNonFemale[0];

    // 4. Fallback: General English male voice (David, Mark, George, Guy, etc.)
    const generalMaleKeywords = ['david', 'mark', 'george', 'guy', 'james', 'richard', 'charles', 'male'];
    const generalMale = voices.find(v => {
        const name = (v.name || '').toLowerCase();
        const lang = (v.lang || '').toLowerCase();
        return lang.startsWith('en') && generalMaleKeywords.some(gm => name.includes(gm)) && !isFemaleVoice(v);
    });
    if (generalMale) return generalMale;

    // 5. Final Fallback: First non-female English voice
    const fallbackEn = voices.find(v => (v.lang || '').toLowerCase().startsWith('en') && !isFemaleVoice(v));
    return fallbackEn || voices[0];
}

// Populate Voice Selector in header
function populateVoiceList() {
    const selector = document.getElementById('voiceSelect');
    if (!selector || !('speechSynthesis' in window)) return;

    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return;

    selector.innerHTML = '';
    const maleVoices = voices.filter(v => !isFemaleVoice(v));
    const listToRender = maleVoices.length > 0 ? maleVoices : voices;

    listToRender.forEach((v) => {
        const opt = document.createElement('option');
        opt.value = v.name;
        opt.textContent = `${v.name} (${v.lang})`;
        if (selectedMaleVoice && v.name === selectedMaleVoice.name) {
            opt.selected = true;
        }
        selector.appendChild(opt);
    });
}

function onUserVoiceChange(voiceName) {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    const chosen = voices.find(v => v.name === voiceName);
    if (chosen) {
        selectedMaleVoice = chosen;
        if (isSpeaking && currentSlideSpeaking) {
            const spokenDiv = document.getElementById("slide-spoken-text-" + currentSlideSpeaking);
            if (spokenDiv) {
                startLectureSpeech(spokenDiv.textContent, currentSlideSpeaking);
            }
        }
    }
}

// Stop Current Speech
function stopCurrentSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;
    currentSlideSpeaking = null;
    speechQueue = [];
    speechQueueIndex = 0;
    updateAudioUI(false);
}

function updateAudioUI(isPlaying) {
    const globalBtn = document.getElementById('globalSpeechBtn');
    if (globalBtn) {
        globalBtn.innerHTML = isPlaying
            ? '<span>❚❚</span> <span>Pause Lecture</span>'
            : '<span>▶</span> <span>Play Slide Audio</span>';
    }

    for (let i = 1; i <= totalSlides; i++) {
        const badge = document.getElementById('slide-audio-badge-' + i);
        const btn = document.getElementById('slide-audio-btn-' + i);
        if (badge && btn) {
            if (isPlaying && currentSlideSpeaking === i) {
                badge.textContent = 'Speaking...';
                badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-sky-500 text-slate-950';
                btn.innerHTML = '<span>❚❚</span> <span>Pause Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-sky-500 text-slate-950 text-xs font-bold flex items-center space-x-1.5 transition shadow-sm';
            } else {
                badge.textContent = 'Audio Lecture Ready';
                badge.className = 'px-2 py-0.5 rounded text-xs font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30';
                btn.innerHTML = '<span>▶</span> <span>Listen to Full Lecture</span>';
                btn.className = 'px-3 py-1.5 rounded-xl bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 text-xs font-bold flex items-center space-x-1.5 border border-sky-500/30 transition shadow-sm';
            }
        }
    }
}

function speakNextSentence() {
    if (!isSpeaking || speechQueueIndex >= speechQueue.length) {
        stopCurrentSpeech();
        return;
    }

    const sentence = speechQueue[speechQueueIndex];
    speechQueueIndex++;

    const utt = new SpeechSynthesisUtterance(sentence);
    if (!selectedMaleVoice) {
        selectedMaleVoice = getIndianMaleVoice();
    }
    if (selectedMaleVoice) {
        utt.voice = selectedMaleVoice;
    }

    // Authentic Indian male teacher tuning: deep baritone pitch, paced tempo
    utt.rate = 0.94;
    utt.pitch = 0.85;

    utt.onend = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };

    utt.onerror = () => {
        if (isSpeaking) {
            speakNextSentence();
        }
    };

    window.speechSynthesis.speak(utt);
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

// ==========================================
// 16 BESPOKE SIMULATORS FOR CHAPTER 10
// ==========================================

// SIM 1: One Shared Home (ISS Orbit Simulator)
let sim1IsDay = true;
function toggleDayNightOrbit() {
    sim1IsDay = !sim1IsDay;
    const earth = document.getElementById('sim1EarthCurve');
    const land = document.getElementById('sim1Landmass');
    const modeText = document.getElementById('orbitModeText');
    const status = document.getElementById('sim1Status');

    if (sim1IsDay) {
        if (earth) earth.setAttribute('fill', '#0284c7');
        if (land) land.setAttribute('fill', '#15803d');
        if (modeText) modeText.textContent = "Day Orbit (Blue Oceans)";
        if (status) status.innerHTML = "<strong>Day Orbit:</strong> Vast sparkling blue oceans, green continents, and cloud ribbons unfold below. Not a single border line is visible!";
    } else {
        if (earth) earth.setAttribute('fill', '#020617');
        if (land) land.setAttribute('fill', '#0f172a');
        if (modeText) modeText.textContent = "Night Orbit (Golden Lights)";
        if (status) status.innerHTML = "<strong>Night Orbit:</strong> The dark continents glow with human city lights like clusters of stars, connected by shared roads without borders!";
    }
}

function zoomISSView() {
    const status = document.getElementById('sim1Status');
    if (status) {
        status.innerHTML = "<span class='text-sky-300 font-bold'>The Overview Effect:</span> Floating in the quiet vacuum of space, astronauts realize that our Earth is a single, fragile, living sanctuary that belongs to all creatures together!";
    }
}

// SIM 2: The Blue Planet Surface Analyzer
function analyzeEarthSurface(surface) {
    const featureText = document.getElementById('featureAnalyzed');
    const status = document.getElementById('sim2Status');

    if (surface === 'oceans') {
        if (featureText) featureText.textContent = "71% Liquid Oceans";
        if (status) status.innerHTML = "<strong>Oceans (71%):</strong> Deep liquid water covers 361 million sq km, absorbing red wavelengths of sunlight and scattering brilliant blue light into space!";
    } else if (surface === 'continents') {
        if (featureText) featureText.textContent = "29% Landmasses";
        if (status) status.innerHTML = "<strong>Continents (29%):</strong> Mountain ranges, tropical forests, grasslands, and deserts provide diverse terrestrial habitats for land life!";
    } else if (surface === 'atmosphere') {
        if (featureText) featureText.textContent = "Atmospheric Blanket";
        if (status) status.innerHTML = "<strong>Atmosphere:</strong> A thin, fragile gaseous veil (78% Nitrogen, 21% Oxygen) shielding surface life from solar radiation and cosmic cold!";
    }
}

// SIM 3: Boundless Nature
function accelerateWinds() {
    const status = document.getElementById('sim3Status');
    if (status) {
        status.innerHTML = "<span class='text-teal-300 font-bold'>Trade Winds in Motion:</span> Atmospheric air streams circulate around the equator, carrying moisture, cloud systems, and heat across all continents freely!";
    }
}

function disperseSeeds() {
    const seed = document.getElementById('floatingSeed');
    const status = document.getElementById('sim3Status');

    if (seed) {
        seed.setAttribute('transform', 'translate(180, 100) scale(1.2)');
        setTimeout(() => {
            seed.setAttribute('transform', 'translate(300, 70) scale(1)');
            setTimeout(() => seed.setAttribute('transform', 'translate(60, 130) scale(1)'), 1200);
        }, 800);
    }
    if (status) {
        status.innerHTML = "<span class='text-amber-300 font-bold'>Seed Dispersion:</span> Dandelion parachutes and coconut husks ride wind and ocean currents across vast seas to colonize distant islands without passports!";
    }
}

// SIM 4: Travelling Birds (Rosy Starling Migration)
function flyStarlingFlock() {
    const bird = document.getElementById('starlingBird');
    const status = document.getElementById('sim4Status');

    if (bird) {
        bird.setAttribute('transform', 'translate(250, 145) scale(1.15)');
        setTimeout(() => {
            bird.setAttribute('transform', 'translate(180, 105) scale(1)');
        }, 1000);
    }
    if (status) {
        status.innerHTML = "<span class='text-pink-300 font-bold'>Murmuration in Flight:</span> Thousands of rosy starlings soar synchronously over the Himalayas, flying 5,000 kilometres from Russia to warm Indian pastures!";
    }
}

function feedOnLocusts() {
    const locusts = document.getElementById('locustPestGroup');
    const status = document.getElementById('sim4Status');

    if (locusts) {
        locusts.setAttribute('opacity', '0.2');
        setTimeout(() => locusts.setAttribute('opacity', '1'), 1500);
    }
    if (status) {
        status.innerHTML = "<span class='text-emerald-300 font-bold'>Natural Pest Busters:</span> The rosy starlings devour crop-destroying locust swarms, saving fields of wheat and millet for Indian farmers without pesticides!";
    }
}

// SIM 5: Yoga's Gift (Global Harmony)
let currentPoseIdx = 0;
const poseDescriptions = [
    "Padmasana (Lotus Pose): Fosters inner peace and spinal alignment.",
    "Tadasana (Mountain Pose): Establishes grounded posture and mental focus.",
    "Vrikshasana (Tree Pose): Teaches balance and deep connection with roots.",
    "Surya Namaskar (Sun Salutation): Harmonizes body vitality with solar energy."
];

function cycleYogaPose() {
    currentPoseIdx = (currentPoseIdx + 1) % poseDescriptions.length;
    const status = document.getElementById('sim5Status');
    if (status) {
        status.innerHTML = `<strong>${poseDescriptions[currentPoseIdx]}</strong> - Practiced worldwide across 177 United Nations member countries!`;
    }
}

function guidePranayamaBreath() {
    const aura = document.getElementById('breathAura');
    const status = document.getElementById('sim5Status');

    if (aura) {
        aura.setAttribute('stroke', '#38bdf8');
        aura.setAttribute('stroke-width', '3');
        setTimeout(() => {
            aura.setAttribute('stroke-width', '1.5');
        }, 2000);
    }
    if (status) {
        status.innerHTML = "<span class='text-cyan-300 font-bold'>Pranayama Breath:</span> Inhale calmness... exhale anxiety. Mindful breathing restores balance to nervous systems across all cultures.";
    }
}

// SIM 6: Chilli's Journey
function sailChilliShip() {
    const ship = document.getElementById('traderShip');
    const status = document.getElementById('sim6Status');

    if (ship) {
        ship.setAttribute('transform', 'translate(220, 85) scale(1.1)');
        setTimeout(() => {
            ship.setAttribute('transform', 'translate(180, 85) scale(1)');
        }, 1000);
    }
    if (status) {
        status.innerHTML = "<span class='text-rose-400 font-bold'>Ship Arrived in Goa:</span> Portuguese caravels carried vibrant red chilli seeds from South America into Indian ports 500 years ago!";
    }
}

function comparePepperChilli() {
    const status = document.getElementById('sim6Status');
    if (status) {
        status.innerHTML = "<strong>Pepper vs Chilli:</strong> Indigenous black pepper from Kerala provided subtle heat for 3,000 years; fiery imported chillies adapted so well they became India's national spice!";
    }
}

// SIM 7: Sweet Sugar
function crushSugarcaneJuice() {
    const status = document.getElementById('sim7Status');
    if (status) {
        status.innerHTML = "<span class='text-amber-400 font-bold'>Boiling Jaggery (Gur):</span> Ancient Indian farmers pressed raw sugarcane stalks, clarifying and boiling the rich sweet juice into solid golden jaggery blocks!";
    }
}

function crystallizeSugar() {
    const status = document.getElementById('sim7Status');
    if (status) {
        status.innerHTML = "<span class='text-yellow-300 font-bold'>Sarkara Crystals:</span> Further refinement created white sparkling sugar crystals ('Sarkara'). The English words 'sugar' and 'candy' originate directly from Sanskrit!";
    }
}

// SIM 8: Mexican Marigold
function stringMarigoldGarland() {
    const status = document.getElementById('sim8Status');
    if (status) {
        status.innerHTML = "<span class='text-orange-400 font-bold'>Festive Garlands:</span> Stringing golden Genda Phool blossoms for Diwali! The bright flowers travelled from Mexico to become India's festive symbol of prosperity.";
    }
}

function testNematodeDefense() {
    const status = document.getElementById('sim8Status');
    if (status) {
        status.innerHTML = "<span class='text-emerald-300 font-bold'>Natural Companion Defense:</span> Marigold roots secrete natural alpha-terthienyl compounds that naturally eliminate destructive root-knot nematodes in vegetable beds!";
    }
}

// SIM 9: Cows in Brazil
function testHeatTolerance() {
    const status = document.getElementById('sim9Status');
    if (status) {
        status.innerHTML = "<span class='text-amber-300 font-bold'>42°C Heat Immunity:</span> While European cattle pant and overheat, Indian Gir and Ongole cows stay cool thanks to abundant sweat glands and loose, cooling dewlaps!";
    }
}

function inspectBrazilianStamp() {
    const status = document.getElementById('sim9Status');
    if (status) {
        status.innerHTML = "<span class='text-emerald-300 font-bold'>Honored on Stamps:</span> Brazil honors Indian Zebu cattle on national postage stamps and coins in gratitude for revolutionizing its national dairy herd!";
    }
}

// SIM 10: Web of Life
function selectWebNode(node) {
    const status = document.getElementById('sim10Status');
    if (node === 'sun') {
        if (status) status.innerHTML = "<strong>Sun Energy:</strong> The ultimate source of energy for 99.9% of all living ecosystems on Earth, powering plant photosynthesis!";
    } else if (node === 'plants') {
        if (status) status.innerHTML = "<strong>Producers:</strong> Green plants and phytoplankton turn solar light into chemical energy and release oxygen for all animals to breathe!";
    } else if (node === 'pollinators') {
        if (status) status.innerHTML = "<strong>Pollinators & Birds:</strong> Bees, butterflies, and starlings fertilize three out of every four crops we eat, keeping food systems alive!";
    } else if (node === 'herbivores') {
        if (status) status.innerHTML = "<strong>Animals & Humans:</strong> Depend directly on plants and water for life, serving as stewards of our shared planetary home!";
    } else if (node === 'decomposers') {
        if (status) status.innerHTML = "<strong>Soil Decomposers:</strong> Earthworms and microbes break down organic matter, recycling minerals back into soil to complete nature's zero-waste circle!";
    }
}

// SIM 11: World Family (Vasudhaiva Kutumbakam)
let familyRotation = 0;
function rotateFamilyWheel() {
    familyRotation = (familyRotation + 72) % 360;
    const mandala = document.getElementById('familyMandalaGroup');
    const status = document.getElementById('sim11Status');

    if (mandala) {
        mandala.setAttribute('transform', `translate(200, 120) rotate(${familyRotation})`);
    }
    if (status) {
        status.innerHTML = "<span class='text-purple-300 font-bold'>Planetary Family Revolving:</span> Humans, animals, trees, rivers, and atmosphere unite in one sacred cosmic household!";
    }
}

function reciteUniversalMotto() {
    const status = document.getElementById('sim11Status');
    if (status) {
        status.innerHTML = "<strong>वसुधैव कुटुम्बकम्:</strong> <em>'Ayam nijah paro veti ganana laghucetasam, udaracaritanam tu vasudhaiva kutumbakam'</em> (For generous hearts, the whole Earth is one family).";
    }
}

// SIM 12: Nature Protects (Prakriti Rakshati Rakshita)
function launchCycloneSurge() {
    const wave = document.getElementById('cycloneSurgeWave');
    const status = document.getElementById('sim12Status');

    if (wave) {
        wave.setAttribute('transform', 'scale(1.25) translate(10, -20)');
        setTimeout(() => {
            wave.setAttribute('transform', 'scale(1) translate(0, 0)');
        }, 1200);
    }
    if (status) {
        status.innerHTML = "<span class='text-sky-300 font-bold'>Fierce Cyclone Waves:</span> Towering storm surge waves hit the coast, but tangled mangrove stilt roots absorb the force and protect homes!";
    }
}

function reinforceMangroves() {
    const status = document.getElementById('sim12Status');
    if (status) {
        status.innerHTML = "<span class='text-emerald-300 font-bold'>Mangrove Nursery Planted:</span> Communities plant young Sundari and Rhizophora saplings. When we protect nature, nature shields our children!";
    }
}

// SIM 13: Global Travelers (Lunchbox)
function inspectLunchItem(item) {
    const title = document.getElementById('lunchItemTitle');
    const region = document.getElementById('lunchItemRegion');
    const country = document.getElementById('lunchItemCountry');
    const age = document.getElementById('lunchItemAge');
    const status = document.getElementById('sim13Status');

    if (item === 'potato') {
        if (title) title.textContent = "Potato Origin";
        if (region) region.textContent = "Andes Mountains";
        if (country) country.textContent = "(Peru / Bolivia)";
        if (age) age.textContent = "~400 Years Ago";
        if (status) status.innerHTML = "<strong>Potato:</strong> Cultivated by Inca farmers in South America, potatoes crossed oceans to become the beloved heart of Indian Aloo Parathas and samosas!";
    } else if (item === 'tomato') {
        if (title) title.textContent = "Tomato Origin";
        if (region) region.textContent = "Central & South America";
        if (country) country.textContent = "(Mexico & Andes)";
        if (age) age.textContent = "~400 Years Ago";
        if (status) status.innerHTML = "<strong>Tomato:</strong> Named 'Tomatl' by Aztecs in Mexico, tomatoes travelled to India and became essential for rich dal tadkas and curries!";
    } else if (item === 'rice') {
        if (title) title.textContent = "Rice & Sugar";
        if (region) region.textContent = "Ancient India";
        if (country) country.textContent = "(Indus & Gangetic Plains)";
        if (age) age.textContent = ">3,500 Years Ago";
        if (status) status.innerHTML = "<strong>Rice & Sugar:</strong> India gave the world fragrant Basmati rice and the sweet secret of turning sugarcane into crystal sugar (Sarkara)!";
    } else if (item === 'paper') {
        if (title) title.textContent = "Paper Invention";
        if (region) region.textContent = "Ancient China";
        if (country) country.textContent = "(Han Dynasty, Cai Lun)";
        if (age) age.textContent = "~1,900 Years Ago";
        if (status) status.innerHTML = "<strong>Paper:</strong> Invented in China c. 105 CE, paper travelled along the Silk Road into India, replacing palm leaves for notebooks!";
    }
}

// SIM 14: Earth Guardians (Action Checklist)
let ecoActions = { tap: true, power: false, plastic: true, tree: false };

function toggleAction(act) {
    ecoActions[act] = !ecoActions[act];
    updateEcoDashboard();
}

function updateEcoDashboard() {
    let score = 25;
    let water = 10;
    let power = 0.5;
    let plastic = 2;
    let tree = 0;

    if (ecoActions.tap) { score += 20; water += 14; }
    if (ecoActions.power) { score += 20; power += 0.7; }
    if (ecoActions.plastic) { score += 20; plastic += 2; }
    if (ecoActions.tree) { score += 20; tree += 1; }

    const meter = document.getElementById('ecoMeterArc');
    const scoreText = document.getElementById('ecoScoreText');
    const waterEl = document.getElementById('waterSavedMetric');
    const powerEl = document.getElementById('energySavedMetric');
    const plasticEl = document.getElementById('plasticAvoidedMetric');
    const treeEl = document.getElementById('treesPlantedMetric');
    const status = document.getElementById('sim14Status');

    if (meter) meter.setAttribute('stroke-dashoffset', 377 - (377 * (score / 100)));
    if (scoreText) scoreText.textContent = `${score}%`;
    if (waterEl) waterEl.textContent = `${water} Litres`;
    if (powerEl) powerEl.textContent = `${power.toFixed(1)} kWh`;
    if (plasticEl) plasticEl.textContent = `${plastic} Bags`;
    if (treeEl) treeEl.textContent = `${tree} Neem Tree`;

    if (status) {
        status.innerHTML = `<strong>Guardian Score: ${score}%</strong> - Every small step saves water, reduces coal consumption, and protects our shared planetary oasis!`;
    }
}

// SIM 15: Seasons Across Borders
function setSolsticeSeason(month) {
    const status = document.getElementById('sim15Status');
    if (month === 'june') {
        if (status) status.innerHTML = "<strong>June Solstice:</strong> Northern Hemisphere (India) tilts toward the Sun, enjoying long summer days, while Southern Hemisphere (Australia) tilts away into winter!";
    } else if (month === 'december') {
        if (status) status.innerHTML = "<strong>December Solstice:</strong> India tilts away into chilly winter, while Australia experiences warm summer sunshine and beach holidays!";
    }
}

// SIM 16: Our Living Earth (Four Spheres)
function inspectSphere(sphere) {
    const title = document.getElementById('sphereTitle');
    const d1 = document.getElementById('sphereDesc1');
    const d2 = document.getElementById('sphereDesc2');
    const d3 = document.getElementById('sphereDesc3');
    const d4 = document.getElementById('sphereDesc4');
    const status = document.getElementById('sim16Status');

    if (sphere === 'atmosphere') {
        if (title) title.textContent = "Atmosphere (Air Shield)";
        if (d1) d1.textContent = "• 78% Nitrogen, 21% O₂";
        if (d2) d2.textContent = "• Shields UV with Ozone";
        if (d3) d3.textContent = "• Circulates rainclouds";
        if (d4) d4.textContent = "• Traps warmth (Greenhouse)";
        if (status) status.innerHTML = "<strong>Atmosphere:</strong> The continuous breath of our planet. The air you breathe in India circulated around distant mountains last month!";
    } else if (sphere === 'hydrosphere') {
        if (title) title.textContent = "Hydrosphere (Water Layer)";
        if (d1) d1.textContent = "• 71% of Earth's surface";
        if (d2) d2.textContent = "• Regulates global climate";
        if (d3) d3.textContent = "• Evaporation & rainfall cycle";
        if (d4) d4.textContent = "• Nourishes all cellular life";
        if (status) status.innerHTML = "<strong>Hydrosphere:</strong> All oceans, rivers, and icecaps connect into one global water cycle that nourishes forests and communities!";
    } else if (sphere === 'biosphere') {
        if (title) title.textContent = "Biosphere (Living Web)";
        if (d1) d1.textContent = "• Microbes to blue whales";
        if (d2) d2.textContent = "• Interconnected food webs";
        if (d3) d3.textContent = "• Pollinators fertilize crops";
        if (d4) d4.textContent = "• Humans are caretakers";
        if (status) status.innerHTML = "<strong>Biosphere:</strong> The vibrant realm of life. Every bird, bee, tree, and child is an integral member of the global family!";
    } else if (sphere === 'geosphere') {
        if (title) title.textContent = "Geosphere (Solid Ground)";
        if (d1) d1.textContent = "• Rocks, crust & fertile soil";
        if (d2) d2.textContent = "• Stores mineral nutrients";
        if (d3) d3.textContent = "• Anchors roots of forests";
        if (d4) d4.textContent = "• Recharges aquifers";
        if (status) status.innerHTML = "<strong>Geosphere:</strong> The bedrock of our home. Soil, enriched by decomposers, provides the foundation for our food and forests!";
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

